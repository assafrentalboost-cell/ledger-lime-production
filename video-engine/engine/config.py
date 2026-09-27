"""Config loading + validation.

Validation is strict on purpose: a config that could produce a misleading or
broken video fails here, before a single frame is rendered.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image

from . import ocr
from .brand import ENGINE_ROOT, Brand, text_width

SCENE_TYPES = {"screen", "morph", "end_card"}
SOURCE_STATUSES = {"product_capture", "reconstruction", "dummy"}
# On-screen text must never make compliance / legal / certification claims.
CLAIM_PATTERNS = [r"complian", r"\bFERPA\b", r"\bHIPAA\b", r"\bIDEA\b", r"certified", r"guarantee",
                  r"\blegal(ly)?\b", r"audit[- ]?proof", r"approved by", r"\bofficial\b", r"\bFDA\b"]


class ConfigError(Exception):
    pass


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def err(self, m): self.errors.append(m)
    def warn(self, m): self.warnings.append(m)
    def note(self, m): self.notes.append(m)


def resolve(p: str) -> Path:
    q = Path(p)
    return q if q.is_absolute() else (ENGINE_ROOT / q)


def source_size(src: dict) -> tuple[int, int]:
    path = resolve(src["path"])
    if src.get("type", "image") == "image":
        with Image.open(path) as im:
            return im.size
    from .sources import probe_video
    return probe_video(path)[:2]


def load(path: str | Path) -> tuple[dict, Brand, Report]:
    """Load + validate + normalise a product config. Raises ConfigError on errors."""
    cfg_path = Path(path).resolve()
    cfg = json.loads(cfg_path.read_text())
    cfg["_path"] = str(cfg_path)
    rep = Report()
    brand = Brand(cfg.get("template", "ledger_lime"))
    _validate(cfg, brand, rep)
    if rep.errors:
        raise ConfigError("\n".join(f"  - {e}" for e in rep.errors))
    return cfg, brand, rep


def _fmt_value(v, fmt: str | None) -> str:
    if fmt == "percent" and isinstance(v, (int, float)):
        return f"{round(v * 100)}%"
    if fmt == "int" and isinstance(v, (int, float)):
        return str(int(round(v)))
    if fmt in ("currency", "currency0") and isinstance(v, (int, float)):
        body = f"{abs(v):,.2f}" if fmt == "currency" else f"{abs(round(v)):,}"
        return ("-$" if v < 0 else "$") + body   # matches Excel "$"#,##0.00
    return str(v)


def _validate(cfg: dict, brand: Brand, rep: Report) -> None:
    for k in ("product", "output", "provenance", "truth", "sources", "scenes"):
        if k not in cfg:
            rep.err(f"missing top-level key '{k}'")
    if rep.errors:
        return
    prod, out, prov, truth = cfg["product"], cfg["output"], cfg["provenance"], cfg["truth"]
    for k in ("id", "title"):
        if not prod.get(k):
            rep.err(f"product.{k} is required")

    # ---- output ----
    out.setdefault("width", 1920); out.setdefault("height", 1080); out.setdefault("fps", 30)
    out.setdefault("min_duration", 5.0); out.setdefault("max_duration", 15.0)
    out.setdefault("filename", f"{prod.get('id', 'video')}.mp4")
    if (out["width"], out["height"]) != (brand.t["canvas"]["width"], brand.t["canvas"]["height"]):
        rep.err(f"output {out['width']}x{out['height']} does not match template canvas "
                f"{brand.t['canvas']['width']}x{brand.t['canvas']['height']} (V1 supports 16:9 1920x1080)")

    # ---- provenance: product truth gate ----
    st = prov.get("source_status")
    if st not in SOURCE_STATUSES:
        rep.err(f"provenance.source_status must be one of {sorted(SOURCE_STATUSES)}")
    appr = prov.get("listing_approval", {})
    if appr.get("approved"):
        if st == "dummy":
            rep.err("provenance.listing_approval cannot approve 'dummy' sources")
        for k in ("by", "date", "note"):
            if not appr.get(k):
                rep.err(f"provenance.listing_approval.{k} is required when approved is true")
        if st != "product_capture":
            rep.warn(f"source_status = '{st}' approved for listing by {appr.get('by')} on {appr.get('date')}: "
                     "no DRAFT tag; owner must confirm the screens match the shipping product")
    elif st != "product_capture":
        rep.warn(f"provenance.source_status = '{st}': sources are NOT captures of the shipping product; "
                 "the video is watermarked DRAFT and must not be used on Etsy")
    if prov.get("pointer_rendered"):
        rep.err("provenance.pointer_rendered is true: a rendered pointer must not be presented as live "
                "mouse capture. Remove the pointer clip or re-capture.")

    # ---- truth ----
    states = truth.get("states", {})
    if set(states) != {"before", "after"}:
        rep.err("truth.states must define exactly 'before' and 'after'")
    else:
        if set(states["before"]) != set(states["after"]):
            rep.err("truth.states.before and .after must have the same keys")
        for k in states["before"]:
            if str(states["before"][k]) == str(states["after"][k]):
                rep.warn(f"truth key '{k}' is identical before and after")
    verify = truth.get("verify")
    if verify:
        for state in ("before", "after"):
            f = resolve(verify[state])
            if not f.exists():
                rep.err(f"truth.verify.{state}: {f} not found")
                continue
            data = json.loads(f.read_text())
            for key, loc in verify.get("cells", {}).items():
                actual = _fmt_value(data.get(loc["sheet"], {}).get(loc["cell"]), loc.get("format"))
                claimed = str(states.get(state, {}).get(key))
                if actual != claimed:
                    rep.err(f"PRODUCT TRUTH: {state}.{key} claims '{claimed}' but workbook "
                            f"{loc['sheet']}!{loc['cell']} recalculates to '{actual}'")
                else:
                    rep.note(f"truth verified: {state}.{key} = '{claimed}' ({loc['sheet']}!{loc['cell']})")
    elif st == "product_capture":
        rep.warn("truth.verify not set - values are checked only by OCR readback in QA")

    # ---- sources ----
    sizes = {}
    for sid, src in cfg["sources"].items():
        p = resolve(src.get("path", ""))
        if not p.exists():
            rep.err(f"source '{sid}': file not found: {p}")
            continue
        try:
            sizes[sid] = source_size(src)
        except Exception as e:  # noqa: BLE001
            rep.err(f"source '{sid}': unreadable ({e})")
    cfg["_source_sizes"] = sizes

    # ---- scenes ----
    card = brand.layout["card"]
    aspect = card[2] / card[3]
    t = 0.0
    for i, sc in enumerate(cfg["scenes"]):
        tag = f"scene {i + 1} ({sc.get('id', sc.get('type'))})"
        typ = sc.get("type")
        if typ not in SCENE_TYPES:
            rep.err(f"{tag}: type must be one of {sorted(SCENE_TYPES)}")
            continue
        d = sc.get("duration")
        if not isinstance(d, (int, float)) or d <= 0:
            rep.err(f"{tag}: duration must be > 0")
            continue
        tr = sc.setdefault("transition", brand.motion["transition"] if i else 0)
        if i and tr > min(d, cfg["scenes"][i - 1].get("duration", 0)) / 2:
            rep.err(f"{tag}: transition {tr}s is longer than half an adjacent scene")
        sc["_start"] = t
        t += d
        if sc.get("caption"):
            _check_text(rep, brand, tag, "caption", sc["caption"], "serif",
                        brand.type["caption_size"], brand.layout["caption"]["max_width"])
        if typ == "end_card":
            for k, role, size, trk in (("title", "serif", "end_title_size", 0),
                                       ("subtitle", "sans", "end_subtitle_size", "end_subtitle_tracking"),
                                       ("brand", "sans_medium", "end_brand_size", "end_brand_tracking")):
                if sc.get(k):
                    _check_text(rep, brand, tag, k, sc[k], role, brand.type[size],
                                cfg["output"]["width"] * (1 - 2 * brand.layout["safe_margin"]) - 80,
                                brand.type[trk] if trk else 0)
            if not sc.get("title"):
                rep.err(f"{tag}: end_card needs a title")
            continue

        # screen / morph
        src_ids = [sc.get("source")] if typ == "screen" else [sc.get("source_from"), sc.get("source_to")]
        if any(s not in cfg["sources"] for s in src_ids):
            rep.err(f"{tag}: unknown source(s) {src_ids}")
            continue
        if any(s not in sizes for s in src_ids):
            continue
        if typ == "morph":
            sa = sc.setdefault("swap_at", d / 2)
            sd = sc.setdefault("swap_duration", brand.motion["morph_dissolve"])
            if sa + sd > d:
                rep.err(f"{tag}: swap_at + swap_duration exceeds scene duration")
            if sizes[src_ids[0]] != sizes[src_ids[1]]:
                rep.warn(f"{tag}: morph sources differ in size {sizes[src_ids[0]]} vs {sizes[src_ids[1]]}; "
                         "they are top-left aligned on a common canvas - make sure the captures share geometry")
        # extra white margin so the camera can frame past an edge:
        # [right, bottom] or [left, top, right, bottom]. Config coordinates stay in
        # source pixels; they are shifted onto the padded canvas here.
        pad = [int(v) for v in sc.get("canvas_pad", [0, 0])]
        pl, pt, pr, pb = pad if len(pad) == 4 else (0, 0, pad[0], pad[1])
        W = max(sizes[s][0] for s in src_ids) + pl + pr
        H = max(sizes[s][1] for s in src_ids) + pt + pb
        sc["_canvas"] = (W, H)
        sc["_offset"] = (pl, pt)
        cam = sc.get("camera")
        if not cam or "from" not in cam:
            rep.err(f"{tag}: camera.from [x, y, w, h] is required")
            continue
        cam.setdefault("to", cam["from"])
        for k in ("from", "to"):
            r = list(cam[k])
            cam[k] = _fit_rect(rep, f"{tag} camera.{k}", [r[0] + pl, r[1] + pt, r[2], r[3]], aspect, W, H)
        # must_show: source rects (e.g. a header row) that must stay fully in frame
        # for the whole camera move - sampled with the renderer's interpolation.
        for j, ms in enumerate(sc.get("must_show", [])):
            mx, my, mw, mh = ms[0] + pl, ms[1] + pt, ms[2], ms[3]
            f0, t0 = cam["from"], cam["to"]
            bad = []
            for i in range(21):
                e = i / 20
                w = f0[2] * (t0[2] / f0[2]) ** e
                h = w / aspect
                cxm = (f0[0] + f0[2] / 2) + ((t0[0] + t0[2] / 2) - (f0[0] + f0[2] / 2)) * e
                cym = (f0[1] + f0[3] / 2) + ((t0[1] + t0[3] / 2) - (f0[1] + f0[3] / 2)) * e
                x0, y0 = cxm - w / 2, cym - h / 2
                if mx < x0 - 0.5 or my < y0 - 0.5 or mx + mw > x0 + w + 0.5 or my + mh > y0 + h + 0.5:
                    bad.append(round(e, 2))
            if bad:
                rep.err(f"{tag}: must_show {j + 1} {ms} leaves the frame during the camera move (progress {bad[:4]})")
            else:
                rep.note(f"must_show verified: {tag} region {j + 1} {ms} stays fully in frame")
        scale_min = min(cam["from"][2], cam["to"][2]) / card[2]
        if scale_min < 1 / 1.35:
            rep.warn(f"{tag}: camera upscales the source {1 / scale_min:.2f}x - text may look soft; "
                     "capture at a higher resolution or widen the crop")
        # highlights
        for j, h in enumerate(sc.get("highlights", [])):
            htag = f"{tag} highlight {j + 1}"
            if "find" in h:
                which = h.get("in", "from" if typ == "morph" else None)
                sid = sc["source"] if typ == "screen" else (sc["source_from"] if which == "from" else sc["source_to"])
                if not ocr.available():
                    rep.err(f"{htag}: 'find' requires tesseract; give explicit rect instead")
                    continue
                try:
                    r = list(ocr.locate(resolve(cfg["sources"][sid]["path"]), h["find"], h.get("occurrence", 1)))
                except LookupError as e:
                    rep.err(f"{htag}: {e}")
                    continue
                ex = h.get("expand", [0, 0, 0, 0])
                h["rect"] = [r[0] - ex[0], r[1] - ex[1], r[2] + ex[0] + ex[2], r[3] + ex[1] + ex[3]]
                rep.note(f"{htag}: '{h['find']}' located at {r} -> rect {h['rect']}")
            if "rect" not in h:
                rep.err(f"{htag}: needs 'rect' [x, y, w, h] or 'find'")
                continue
            h["rect"] = [h["rect"][0] + pl, h["rect"][1] + pt, h["rect"][2], h["rect"][3]]
            x, y, w, hh = h["rect"]
            if x < 0 or y < 0 or x + w > W or y + hh > H:
                rep.err(f"{htag}: rect {h['rect']} outside source {W}x{H}")
            if h.get("label"):
                _check_text(rep, brand, htag, "label", h["label"], "sans_semibold",
                            brand.type["highlight_label_size"], card[2] * 0.6)
        # chips: values come ONLY from truth
        for j, c in enumerate(sc.get("chips", [])):
            ctag = f"{tag} chip {j + 1}"
            k = c.get("truth_key")
            if not isinstance(states, dict) or k not in states.get("before", {}):
                rep.err(f"{ctag}: truth_key '{k}' not in truth.states - chip values must come from truth")
                continue
            c["_from"], c["_to"] = str(states["before"][k]), str(states["after"][k])
            label = c.get("label") or truth.get("labels", {}).get(k, k)
            c["_label"] = label
            for role, txt in (("sans_medium", label.upper()), ("sans_semibold", c["_from"] + c["_to"])):
                miss = brand.missing_glyphs(role, txt)
                if miss:
                    rep.err(f"{ctag}: font '{role}' has no glyph for {sorted(miss)}")

    texts = [sc.get(k, "") for sc in cfg["scenes"] for k in ("caption", "title", "subtitle")]
    texts += [h.get("label", "") for sc in cfg["scenes"] for h in sc.get("highlights", [])]
    texts += list(truth.get("labels", {}).values())
    for txt in texts:
        for pat in CLAIM_PATTERNS:
            if txt and re.search(pat, txt, re.I):
                rep.err(f"on-screen text '{txt}' matches claim pattern {pat!r} - no compliance/legal claims")

    cfg["_duration"] = round(t, 3)
    if t < out["min_duration"] or t > out["max_duration"]:
        rep.err(f"total duration {t:.2f}s outside [{out['min_duration']}, {out['max_duration']}]s")
    if t > 15.0:
        rep.warn("Etsy listing videos over 15 s are trimmed; keep <= 15 s")
    if not any(s.get("type") == "end_card" for s in cfg["scenes"]):
        rep.note("no end card (optional)")


def _check_text(rep, brand, tag, what, text, role, size, max_w, tracking=0):
    miss = brand.missing_glyphs(role, text)
    if miss:
        rep.err(f"{tag}: {what} uses characters missing from font '{role}': {sorted(miss)} "
                "(would render as boxes)")
    w = text_width(brand.font(role, size), text, tracking)
    if w > max_w:
        rep.err(f"{tag}: {what} '{text}' is {w:.0f}px wide at {size}px, max {max_w:.0f}px - shorten it")


def _fit_rect(rep, tag, r, aspect, W, H):
    x, y, w, h = map(float, r)
    if abs((w / h) / aspect - 1) > 0.005:
        nh = w / aspect
        if abs(nh / h - 1) > 0.03:
            rep.warn(f"{tag}: {r} adjusted to card aspect {aspect:.3f} (height {h:.0f} -> {nh:.0f}, centre kept)")
        y += (h - nh) / 2
        h = nh
    if w > W or h > H:
        rep.err(f"{tag}: crop {w:.0f}x{h:.0f} larger than source {W}x{H}")
        return [x, y, w, h]
    nx, ny = min(max(x, 0), W - w), min(max(y, 0), H - h)
    if (nx, ny) != (x, y):
        rep.warn(f"{tag}: crop shifted inside source bounds ({x:.0f},{y:.0f}) -> ({nx:.0f},{ny:.0f})")
    return [nx, ny, w, h]
