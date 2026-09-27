#!/usr/bin/env python3
"""Automated QA for a rendered Etsy video.

Standalone:  python qa/run_qa.py configs/product13_iep_tracker.json
(re-checks output/<product-id>/<filename> using its render-manifest.json)

Everything is measured on the ENCODED MP4 (ffprobe / ffmpeg decode / frames
extracted from the file), except layout-geometry checks, which use the
render manifest the compositor wrote while drawing each frame.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw, ImageStat

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine import ocr  # noqa: E402
from engine.brand import Brand  # noqa: E402
from engine.config import CLAIM_PATTERNS  # noqa: E402

MOBILE_W = 390           # CSS px width of a phone showing the listing video full-width
PRIMARY_MIN_PX = 11.0    # min on-phone size for primary overlay text (captions, values, titles)
SECONDARY_MIN_PX = 6.0   # min for secondary text (chip labels, subtitle, brand line)
TIERS = {"caption": "primary", "chip": "primary", "highlight_label": "primary", "end_title": "primary",
         "end_subtitle": "secondary", "end_brand": "secondary", "wordmark": "decorative"}
ETSY_MAX_BYTES = 100 * 1024 * 1024


def sh(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


class Checks:
    def __init__(self):
        self.rows = []

    def add(self, name, ok, detail="", level="fail"):
        """level: 'fail' (hard), 'warn' (soft), 'info'."""
        status = "PASS" if ok else ("FAIL" if level == "fail" else "WARN" if level == "warn" else "INFO")
        self.rows.append({"check": name, "status": status, "detail": detail})
        return ok

    @property
    def failed(self): return [r for r in self.rows if r["status"] == "FAIL"]
    @property
    def warned(self): return [r for r in self.rows if r["status"] == "WARN"]


def extract_frame(mp4: Path, t: float, dst: Path, width: int | None = None) -> Image.Image:
    vf = ["-vf", f"scale={width}:-2:flags=lanczos"] if width else []
    dst.unlink(missing_ok=True)  # never read back a stale frame from an earlier render
    sh(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", str(mp4), "-frames:v", "1", *vf, str(dst)])
    if not dst.exists():  # seeking onto the final frame: decode the tail and keep the last picture
        sh(["ffmpeg", "-y", "-v", "error", "-sseof", "-0.5", "-i", str(mp4), *vf, "-update", "1", str(dst)])
    return Image.open(dst).convert("RGB")


def atoms_order(mp4: Path) -> list[str]:
    order, data = [], mp4.read_bytes()
    i = 0
    while i + 8 <= len(data):
        size = int.from_bytes(data[i:i + 4], "big")
        typ = data[i + 4:i + 8].decode("latin1")
        order.append(typ)
        if size == 1:
            size = int.from_bytes(data[i + 8:i + 16], "big")
        if size < 8:
            break
        i += size
    return order


def run_qa(cfg: dict, mp4: Path, out_dir: Path, manifest: dict) -> tuple[str, Path]:
    qa = out_dir / "qa"
    (qa / "keyframes").mkdir(parents=True, exist_ok=True)
    (qa / "mobile").mkdir(parents=True, exist_ok=True)
    C = Checks()
    o = cfg["output"]
    fps, W, H = o["fps"], o["width"], o["height"]
    exp_dur = manifest["duration"]
    brand = Brand(cfg.get("template", "ledger_lime"))

    # ---------------- 1. ffprobe ----------------
    pr = sh(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(mp4)])
    probe = json.loads(pr.stdout) if pr.returncode == 0 else {}
    C.add("File readable by ffprobe", pr.returncode == 0, pr.stderr.strip()[:200])
    vs = [s for s in probe.get("streams", []) if s["codec_type"] == "video"]
    aus = [s for s in probe.get("streams", []) if s["codec_type"] == "audio"]
    v = vs[0] if vs else {}
    fmt = probe.get("format", {})
    dur = float(fmt.get("duration", 0))
    size = int(fmt.get("size", 0))
    C.add("Container MP4", "mp4" in fmt.get("format_name", ""), fmt.get("format_name", ""))
    C.add("Codec H.264 (High)", v.get("codec_name") == "h264" and v.get("profile") == "High",
          f"{v.get('codec_name')} / {v.get('profile')} / level {v.get('level')}")
    C.add("Resolution", (v.get("width"), v.get("height")) == (W, H), f"{v.get('width')}x{v.get('height')} (expected {W}x{H})")
    C.add("Pixel format yuv420p", v.get("pix_fmt") == "yuv420p", v.get("pix_fmt", ""))
    C.add("Frame rate", v.get("r_frame_rate") == f"{fps}/1", v.get("r_frame_rate", ""))
    C.add("Colour tagged BT.709", v.get("color_space") == "bt709", f"{v.get('color_space')}/{v.get('color_primaries')}/{v.get('color_transfer')}", "warn")
    C.add("Duration matches timeline", abs(dur - exp_dur) <= 1.5 / fps, f"{dur:.3f}s (expected {exp_dur:.3f}s)")
    C.add(f"Duration within {o['min_duration']}-{o['max_duration']}s", o["min_duration"] <= dur <= o["max_duration"] + 1 / fps, f"{dur:.2f}s")
    C.add("Etsy: <= 15 s (longer is trimmed)", dur <= 15.0 + 1 / fps, f"{dur:.2f}s")
    C.add("Etsy: file < 100 MB", 0 < size < ETSY_MAX_BYTES, f"{size / 1e6:.2f} MB")
    C.add("No audio track (Etsy plays muted)", not aus, f"{len(aus)} audio stream(s)", "warn")
    order = [a for a in atoms_order(mp4) if a in ("moov", "mdat")]
    C.add("Web fast-start (moov before mdat)", order[:1] == ["moov"], " -> ".join(order))

    # ---------------- 2. corruption / decode ----------------
    dec = sh(["ffmpeg", "-v", "error", "-i", str(mp4), "-f", "null", "-"])
    C.add("Full decode without errors", dec.returncode == 0 and not dec.stderr.strip(), dec.stderr.strip()[:300] or "clean")
    cnt = sh(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
              "stream=nb_read_frames", "-of", "csv=p=0", str(mp4)])
    nread = int(cnt.stdout.strip() or 0)
    C.add("Frame count", nread == manifest["nframes"], f"{nread} decoded (expected {manifest['nframes']})")

    # ---------------- 3. black / frozen frames ----------------
    bd = sh(["ffmpeg", "-v", "info", "-i", str(mp4), "-vf", "blackdetect=d=0.05:pix_th=0.05:pic_th=0.98",
             "-an", "-f", "null", "-"])
    blacks = re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", bd.stderr)
    C.add("No black frames (blackdetect)", not blacks, ", ".join(f"{a}-{b}s" for a, b in blacks) or "none detected")
    fz = sh(["ffmpeg", "-v", "info", "-i", str(mp4), "-vf", "freezedetect=n=0.0005:d=1.5", "-an", "-f", "null", "-"])
    freezes = re.findall(r"freeze_start: ([\d.]+)", fz.stderr)
    C.add("Static holds > 1.5 s (informational)", True,
          (", ".join(f"{float(x):.2f}s" for x in freezes) + " (end card hold is expected)") if freezes else "none", "info")

    # ---------------- 4. key frames + contact sheet ----------------
    timeline = manifest["timeline"]
    shots = [(0.0, timeline[0]["id"], "first frame (Etsy poster)")]
    for s in timeline:
        shots.append((s["start"] + s["duration"] * 0.5, s["id"], "mid"))
        shots.append((s["start"] + s["duration"] - 0.3, s["id"], "end"))
    shots.append((exp_dur - 1 / fps, timeline[-1]["id"], "last frame"))
    keyframes = []
    for i, (t, sid, what) in enumerate(shots):
        dst = qa / "keyframes" / f"{i:02d}_{t:05.2f}s_{sid}.png"
        keyframes.append((t, sid, what, dst, extract_frame(mp4, t, dst)))
    contact = contact_sheet(keyframes, qa / "contact-sheet.png", cfg["product"]["title"], 3, 600)

    first = keyframes[0][4]
    st = ImageStat.Stat(first.convert("L"))
    C.add("First frame is a composed shot (not blank)", st.stddev[0] > 20, f"luma mean {st.mean[0]:.0f}, stdev {st.stddev[0]:.0f}")

    # ---------------- 5. mobile previews ----------------
    mob = qa / "mobile"
    sh(["ffmpeg", "-y", "-v", "error", "-i", str(mp4), "-vf", f"scale={MOBILE_W * 2}:-2:flags=lanczos",
        "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an",
        str(mob / f"mobile-preview-{MOBILE_W * 2}w.mp4")])
    mob_frames = []
    for t, sid, what, dst, _ in keyframes:
        if what in ("mid", "end"):
            p = mob / f"m_{dst.name}"
            mob_frames.append((t, sid, what, p, extract_frame(mp4, t, p, MOBILE_W)))
    contact_sheet(mob_frames, qa / "mobile-contact-sheet.png", f"{cfg['product']['title']} - phone size ({MOBILE_W}px)",
                  2, MOBILE_W)
    C.add("Mobile preview video written", (mob / f"mobile-preview-{MOBILE_W * 2}w.mp4").exists(), f"mobile/mobile-preview-{MOBILE_W * 2}w.mp4")

    # ---------------- 6. OCR readback (full size + phone size) ----------------
    ocr_rows = []
    if ocr.available():
        for s in timeline:
            for e in s.get("expect_text", []):
                t = s["start"] + e["at"]
                big = extract_frame(mp4, t, qa / "keyframes" / f"ocr_{t:05.2f}s.png")
                txt = ocr.read_text(big, strip=[brand.color(brand.hl["color"])])
                small = extract_frame(mp4, t, qa / "mobile" / f"ocr_m_{t:05.2f}s.png", MOBILE_W)
                small_up = small.resize((small.width * 4, small.height * 4), Image.LANCZOS)
                txt_m = ocr.read_text(small_up, strip=[brand.color(brand.hl["color"])])
                for phrase in e["text"]:
                    ok = ocr.contains(txt, phrase)
                    ok_m = ocr.contains(txt_m, phrase)
                    ocr_rows.append({"t": t, "scene": s["id"], "phrase": phrase, "full": ok, "mobile": ok_m})
                    C.add(f"OCR readback @{t:.2f}s: \"{phrase}\"", ok, "found in encoded frame" if ok else f"NOT found; OCR saw: {txt[:160]}")
        # captions must also survive phone-size OCR (a proxy for legibility)
        for s in timeline:
            if s.get("caption"):
                hit = [r for r in ocr_rows if r["scene"] == s["id"] and ocr._norm(r["phrase"]) in ocr._norm(s["caption"])]
                if hit:
                    C.add(f"Phone-size OCR: caption \"{s['caption']}\"", all(r["mobile"] for r in hit),
                          f"read back from a {MOBILE_W}px-wide frame", "warn")
    else:
        C.add("OCR readback", False, "tesseract not installed - verify text manually", "warn")

    # ---------------- 7. layout: clipping / occlusion / dwell ----------------
    m = manifest["safe_margin"]
    safe = [W * m, H * m, W * (1 - m), H * (1 - m)]
    cx, cy, cw, ch = manifest["card"]
    card = [cx, cy, cx + cw, cy + ch]
    inside = lambda b, c: b[0] >= c[0] - 0.5 and b[1] >= c[1] - 0.5 and b[2] <= c[2] + 0.5 and b[3] <= c[3] + 0.5
    els = manifest["elements"]
    for e in els:
        cont = safe if e["container"] == "frame" else card
        C.add(f"No clipping: {e['kind']} \"{e['text'][:40]}\" ({e['scene']})", inside(e["bbox"], cont),
              f"bbox {[round(x) for x in e['bbox']]} within {e['container']} {'safe area' if e['container'] == 'frame' else ''}".strip())
    ovl = manifest.get("overlaps", [])
    for sc in sorted({e["scene"] for e in els if e["kind"] == "chip"}):
        hits = [x for x in ovl if x["scene"] == sc]
        C.add(f"Chips never cover a visible highlight ({sc})", not hits,
              f"{len(hits)} overlapping frame(s), first at {hits[0]['t_local']}s" if hits else "checked every frame")
    min_dwell = 0.6
    for e in els:
        if e["kind"] in ("caption", "chip", "highlight", "end_title"):
            C.add(f"Readable dwell >= {min_dwell}s: {e['kind']} \"{e['text'][:32]}\"", e["frames"] / fps >= min_dwell,
                  f"fully visible {e['frames'] / fps:.2f}s")
    # expected overlays actually drawn
    for s in timeline:
        if s.get("caption"):
            C.add(f"Caption rendered: \"{s['caption']}\"", any(e["kind"] == "caption" and e["text"] == s["caption"] for e in els))

    # ---------------- 8. mobile legibility (geometry) ----------------
    k = MOBILE_W / W
    leg_rows = []
    for e in els:
        tier = TIERS.get(e["kind"])
        if tier in ("primary", "secondary") and e["font_px"]:
            px = e["font_px"] * k
            lim = PRIMARY_MIN_PX if tier == "primary" else SECONDARY_MIN_PX
            leg_rows.append((e["kind"], e["text"], e["font_px"], px, lim))
            C.add(f"Phone legibility ({tier}): {e['kind']} \"{e['text'][:30]}\"", px >= lim,
                  f"{e['font_px']}px -> {px:.1f}px on a {MOBILE_W}px phone (min {lim})")
    lab = brand.type["chip_label_size"] * k
    if any(e["kind"] == "chip" for e in els):
        C.add("Phone legibility (secondary): chip labels", lab >= SECONDARY_MIN_PX, f"{brand.type['chip_label_size']}px -> {lab:.1f}px")

    # ---------------- 9. source sharpness ----------------
    for s in manifest["scenes"]:
        C.add(f"Source not over-upscaled ({s['scene']})", s["max_upscale"] <= 1.35,
              f"max upscale {s['max_upscale']}x, source px per output px {s['scale_min']}-{s['scale_max']}", "warn")

    # ---------------- 10. product truth + claims ----------------
    prov = cfg["provenance"]
    verified = [n for n in manifest["validation"]["notes"] if n.startswith("truth verified")]
    C.add("Product truth: before/after values verified against workbook", bool(verified) or prov["source_status"] == "product_capture",
          f"{len(verified)} value(s) verified against recalculated workbook cells" if verified else "no workbook verification; relies on OCR readback", "warn")
    C.add("No rendered pointer presented as live capture", not prov.get("pointer_rendered", False), "provenance.pointer_rendered = false")
    texts = [s.get(k2, "") for s in cfg["scenes"] for k2 in ("caption", "title", "subtitle", "brand")]
    texts += [h.get("label", "") for s in cfg["scenes"] for h in s.get("highlights", [])]
    texts += [c.get("_label", "") for s in cfg["scenes"] for c in s.get("chips", [])]
    hits = sorted({t for t in texts if t for p in CLAIM_PATTERNS if re.search(p, t, re.I)})
    C.add("No compliance / legal claims in on-screen text", not hits, "; ".join(hits) or "none found")
    approval = prov.get("listing_approval", {})
    approved = bool(approval.get("approved"))
    gate = prov["source_status"] == "product_capture" or approved
    C.add("Sources cleared for listing", gate,
          f"source_status = {prov['source_status']}" + (
              "" if prov["source_status"] == "product_capture" else
              f"; listing approved by {approval.get('by')} on {approval.get('date')}: {approval.get('note')}" if approved else
              " -> DRAFT watermark applied; replace sources (or record listing_approval) before Etsy use"),
          "warn")

    # ---------------- 11. internal labels + privacy (OCR of every key frame) ----------------
    frame_text = {}
    if ocr.available():
        strip = [brand.color(brand.hl["color"])]
        for t, sid, what, dst, im in keyframes:
            frame_text[dst.name] = ocr.read_text(im, strip=strip)
        internal = [r"\bDRAFT\b", r"RECONSTRUCTION", r"NOT\s*FOR\s*LISTING", r"\bDUMMY\b", r"STAND-?IN", r"\bINTERNAL\b"]
        hits = sorted({f"{n}: {m.group(0)}" for n, txt in frame_text.items() for p in internal
                       for m in [re.search(p, txt, re.I)] if m})
        watermark_expected = manifest.get("draft_watermark", False)
        C.add("No internal / QA labels in any frame", not hits,
              ("; ".join(hits[:6]) + (" (DRAFT tag intended for stand-in sources)" if watermark_expected else ""))
              if hits else f"OCR of {len(frame_text)} key frames: none found",
              "info" if watermark_expected else "fail")
    priv = cfg.get("qa", {}).get("privacy")
    if priv:
        name_re = re.compile(priv.get("name_pattern", r"\b[A-Z][a-z]{1,15} [A-Z]\.(?=\s|$|\|)"))
        id_re = re.compile(priv.get("id_pattern", r"STU-\d{3}"))
        src_vals = []
        for f in priv.get("source_values", []):
            data = json.loads((ROOT / f).read_text())
            src_vals += [str(v) for sheet in data.values() for v in sheet.values()]
        bad_src = sorted({v for v in src_vals if name_re.search(v)})
        C.add("Privacy: no person-name labels in workbook data", not bad_src,
              ", ".join(bad_src[:8]) or f"{len(src_vals)} cell values scanned")
        ids = sorted({m for v in src_vals for m in id_re.findall(v)})
        C.add("Privacy: student identifiers use the safe ID format", bool(ids) or not src_vals,
              ", ".join(ids) if ids else "no IDs found in workbook data")
        bad_frames = sorted({f"{n}: {m}" for n, txt in frame_text.items() for m in name_re.findall(txt)})
        C.add("Privacy: no person-name labels in any frame (OCR)", not bad_frames,
              "; ".join(bad_frames[:6]) or f"{len(frame_text)} key frames scanned")
        ids_on_screen = sorted({m for txt in frame_text.values() for m in id_re.findall(txt)})
        C.add("Privacy: safe identifiers visible on screen", bool(ids_on_screen),
              ", ".join(ids_on_screen) or "none read", "warn")

    # ---------------- verdict + report ----------------
    if C.failed:
        verdict = "FAIL"
    elif not gate:
        verdict = "NEEDS REVISION (technical QA passed; sources are stand-ins)"
    elif approved and prov["source_status"] != "product_capture" and not C.warned:
        verdict = "PASS (owner-approved reconstruction captures)"
    elif C.warned:
        verdict = "PASS WITH WARNINGS"
    else:
        verdict = "PASS"
    results = {"verdict": verdict, "checks": C.rows, "ocr": ocr_rows, "probe": {"video": v, "format": fmt},
               "generated": datetime.now(timezone.utc).isoformat()}
    (qa / "qa-results.json").write_text(json.dumps(results, indent=1, default=str))
    report = out_dir / cfg.get("qa", {}).get("report_name", "VIDEO-QA-REPORT.md")
    report.write_text(render_report(cfg, manifest, mp4, out_dir, verdict, C, ocr_rows, leg_rows, v, dur, size))
    return verdict, report


def contact_sheet(frames, dst: Path, title: str, cols: int, tw: int) -> Path:
    from engine.brand import ENGINE_ROOT
    from PIL import ImageFont
    th = int(tw * 9 / 16)
    pad, lab, top = 16, 30, 64
    rows = (len(frames) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (tw + pad) + pad, top + rows * (th + lab + pad) + pad), (246, 241, 231))
    d = ImageDraw.Draw(sheet)
    f = ImageFont.truetype(str(ENGINE_ROOT / "assets/fonts/Inter-Medium.ttf"), 16)
    ft = ImageFont.truetype(str(ENGINE_ROOT / "assets/fonts/CormorantGaramond-SemiBold.ttf"), 34)
    d.text((pad, 14), title, font=ft, fill=(20, 33, 61))
    for i, (t, sid, what, _, im) in enumerate(frames):
        x = pad + (i % cols) * (tw + pad)
        y = top + (i // cols) * (th + lab + pad)
        sheet.paste(im.resize((tw, th), Image.LANCZOS) if im.width != tw else im, (x, y))
        d.rectangle([x - 1, y - 1, x + tw, y + th], outline=(210, 200, 180))
        d.text((x, y + th + 6), f"{t:05.2f}s  {sid}  ({what})", font=f, fill=(27, 36, 51))
    sheet.save(dst, optimize=True)
    return dst


def render_report(cfg, manifest, mp4, out_dir, verdict, C, ocr_rows, leg_rows, v, dur, size) -> str:
    rel = lambda p: Path(p).relative_to(out_dir).as_posix()
    prov = cfg["provenance"]
    L = []
    L.append(f"# VIDEO QA REPORT - {cfg['product']['title']} {cfg['product'].get('version', '')}".rstrip())
    L.append("")
    L.append(f"- **Verdict:** **{verdict}**")
    L.append(f"- **Video:** `{rel(mp4)}` - {v.get('width')}x{v.get('height')}, {dur:.2f}s, "
             f"{v.get('codec_name')} {v.get('profile')}, {v.get('pix_fmt')}, {v.get('r_frame_rate')} fps, {size / 1e6:.2f} MB")
    L.append(f"- **Config:** `{manifest['config']}`")
    L.append(f"- **Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} by `render_video.py` (automated)")
    L.append(f"- **Checks:** {sum(r['status'] == 'PASS' for r in C.rows)} pass, {len(C.warned)} warn, {len(C.failed)} fail")
    L.append("")
    L.append("## Source provenance (product truth)")
    L.append("")
    L.append(f"- `source_status`: **{prov['source_status']}**")
    L.append(f"- Rendered pointer shown: **{'yes' if prov.get('pointer_rendered') else 'no'}**")
    L.append(f"- Notes: {prov.get('notes', '')}")
    appr = prov.get("listing_approval", {})
    if appr.get("approved"):
        L.append(f"- Listing approval: **approved by {appr.get('by')} on {appr.get('date')}** - {appr.get('note')}")
    if prov["source_status"] != "product_capture" and not appr.get("approved"):
        L.append("")
        L.append("> **Not for Etsy.** The sources are not captures of the shipping product, so every frame carries a "
                 "DRAFT tag. Capture the real workbook in the same before/after states, update `sources` and crop/rect "
                 "coordinates, set `source_status` to `product_capture`, and re-run the same command.")
    L.append("")
    L.append("| Truth key | Before | After |")
    L.append("|---|---|---|")
    for k in cfg["truth"]["states"]["before"]:
        L.append(f"| {k} | {cfg['truth']['states']['before'][k]} | {cfg['truth']['states']['after'][k]} |")
    for n in manifest["validation"]["notes"]:
        if n.startswith("truth verified"):
            L.append(f"- {n}")
    L.append("")
    L.append("## Timeline")
    L.append("")
    L.append("| # | Scene | Type | Start | End | Caption |")
    L.append("|---|---|---|---|---|---|")
    for i, s in enumerate(manifest["timeline"], 1):
        L.append(f"| {i} | {s['id']} | {s['type']} | {s['start']:.2f}s | {s['start'] + s['duration']:.2f}s | {s['caption'] or '-'} |")
    L.append("")
    L.append("## Automated checks")
    L.append("")
    L.append("| Result | Check | Detail |")
    L.append("|---|---|---|")
    for r in C.rows:
        L.append(f"| {r['status']} | {r['check']} | {str(r['detail']).replace('|', '/')} |")
    L.append("")
    if ocr_rows:
        L.append("## OCR readback (text read from the encoded MP4)")
        L.append("")
        L.append("| Time | Scene | Expected text | 1920px frame | 390px phone frame |")
        L.append("|---|---|---|---|---|")
        for r in ocr_rows:
            L.append(f"| {r['t']:.2f}s | {r['scene']} | {r['phrase']} | {'found' if r['full'] else 'MISSING'} | "
                     f"{'found' if r['mobile'] else 'not legible'} |")
        L.append("")
        L.append("Phone-frame OCR is a legibility proxy: spreadsheet cell text is expected to be too small at 390px; "
                 "captions and value chips carry the message on phones.")
        L.append("")
    L.append("## Mobile legibility (overlay text at 390px phone width)")
    L.append("")
    L.append("| Element | Text | Render px | Phone px | Min |")
    L.append("|---|---|---|---|---|")
    for kind, text, fpx, px, lim in leg_rows:
        L.append(f"| {kind} | {text[:40]} | {fpx} | {px:.1f} | {lim} |")
    L.append("")
    L.append("## Artifacts")
    L.append("")
    L.append(f"- Contact sheet: `qa/contact-sheet.png`")
    L.append(f"- Phone-size contact sheet: `qa/mobile-contact-sheet.png`")
    L.append(f"- Phone preview video: `qa/mobile/mobile-preview-{MOBILE_W * 2}w.mp4`")
    L.append(f"- Key frames: `qa/keyframes/`")
    L.append(f"- Machine-readable results: `qa/qa-results.json`; layout manifest: `render-manifest.json`")
    L.append("")
    L.append("## Manual review (automation cannot judge these)")
    L.append("")
    L.append("- [ ] Pacing feels calm, not rushed; each caption readable in one glance")
    L.append("- [ ] Highlights point at the right cells and feel restrained (no cheesy motion)")
    L.append("- [ ] The before/after change reads clearly as ONE real input causing the update")
    L.append("- [ ] Screens are real product captures (no mocked or fake UI)")
    L.append("- [ ] Brand feel: navy / cream / restrained gold, premium and quiet")
    L.append("- [ ] Watch `qa/mobile/mobile-preview-780w.mp4` on an actual phone")
    L.append("")
    return "\n".join(L)


def main():
    from engine import config as cfgmod
    cfg, _, _ = cfgmod.load(sys.argv[1])
    out_dir = ROOT / "output" / cfg["product"]["id"]
    manifest = json.loads((out_dir / "render-manifest.json").read_text())
    verdict, report = run_qa(cfg, out_dir / cfg["output"]["filename"], out_dir, manifest)
    print(verdict, report)


if __name__ == "__main__":
    main()
