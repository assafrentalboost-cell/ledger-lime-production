"""Frame compositor for the Ledger & Lime template.

Every frame is composed in Python (Pillow) and piped to FFmpeg. Camera moves
use sub-pixel affine resampling from a mip pyramid, so zooms and pans are
smooth and text does not shimmer. All overlay geometry is recorded in a
layout manifest that QA uses for clipping / occlusion checks.
"""
from __future__ import annotations

import math

from PIL import Image, ImageChops, ImageDraw, ImageFilter

from .brand import Brand, render_text
from .config import resolve
from .sources import ImageSource, VideoSource

SS = 4  # supersampling factor for vector shapes


def clamp01(x): return 0.0 if x < 0 else 1.0 if x > 1 else x
def in_out_cubic(p): p = clamp01(p); return 4 * p ** 3 if p < 0.5 else 1 - (-2 * p + 2) ** 3 / 2
def out_cubic(p): p = clamp01(p); return 1 - (1 - p) ** 3


def fade(layer: Image.Image, o: float) -> Image.Image:
    if o >= 0.999:
        return layer
    out = layer.copy()
    out.putalpha(layer.getchannel("A").point(lambda v: int(v * o)))
    return out


def rounded_rect_layer(w, h, radius, fill=None, outline=None, width=0, frac=(0.0, 0.0), margin=0):
    """Anti-aliased rounded rectangle on a transparent layer (supersampled).
    `frac` is a sub-pixel offset so moving shapes glide instead of stepping."""
    W, H = int(math.ceil(w + 2 * margin + 2)), int(math.ceil(h + 2 * margin + 2))
    big = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    x0, y0 = (margin + frac[0]) * SS, (margin + frac[1]) * SS
    d.rounded_rectangle([x0, y0, x0 + w * SS, y0 + h * SS], radius=radius * SS,
                        fill=fill, outline=outline, width=int(round(width * SS)))
    return big.reduce(SS)


class Renderer:
    def __init__(self, cfg: dict, brand: Brand):
        self.cfg, self.b = cfg, brand
        o = cfg["output"]
        self.W, self.H, self.fps = o["width"], o["height"], o["fps"]
        self.card = brand.layout["card"]
        self.draft = cfg["provenance"]["source_status"] != "product_capture"
        self.scenes = cfg["scenes"]
        self.duration = cfg["_duration"]
        self.nframes = int(round(self.duration * self.fps))
        self.manifest = {"elements": {}, "scenes": []}
        self._build_static()
        self._prepare_scenes()

    # ------------------------------------------------------------------ static
    def _build_static(self):
        b, (cx, cy, cw, ch) = self.b, self.card
        base = Image.new("RGB", (self.W, self.H), b.color(b.t["canvas"]["background"]))
        sh = b.layout["card_shadow"]
        shadow = Image.new("L", (self.W, self.H), 0)
        ImageDraw.Draw(shadow).rounded_rectangle(
            [cx, cy + sh["offset_y"], cx + cw, cy + ch + sh["offset_y"]], radius=b.layout["card_radius"],
            fill=int(255 * sh["opacity"]))
        shadow = shadow.filter(ImageFilter.GaussianBlur(sh["blur"]))
        base.paste(Image.new("RGB", base.size, b.color("navy")), (0, 0), shadow)
        border = rounded_rect_layer(cw + 2, ch + 2, b.layout["card_radius"] + 1, fill=b.color("card_border") + (255,))
        base.paste(border, (cx - 1, cy - 1), border)
        self.card_mask = rounded_rect_layer(cw, ch, b.layout["card_radius"], fill=(255, 255, 255, 255)).getchannel("A").crop((0, 0, cw, ch))
        # wordmark
        wm = b.layout["wordmark"]
        f = b.font("sans_medium", b.type["wordmark_size"])
        layer, _ = render_text("LEDGER & LIME", f, b.color("gold"), b.type["wordmark_tracking"])
        cap = f.getbbox("H")
        self.wordmark = (layer, (int(wm["right"] - layer.width), int(wm["center_y"] - (cap[1] + cap[3]) / 2)))
        base.paste(layer, self.wordmark[1], layer)
        self._record("global", "wordmark", "LEDGER & LIME", b.type["wordmark_size"],
                     self._bbox(layer, self.wordmark[1]), "frame")
        self.base = base
        # end-card background
        self.end_bg = Image.new("RGB", (self.W, self.H), b.color(b.end["background"]))
        # draft tag
        self.draft_tag = None
        if self.draft:
            dt = b.layout["draft_tag"]
            f = b.font("sans_medium", b.type["draft_tag_size"])
            txt = f"DRAFT  ·  {self.cfg['provenance']['source_status'].upper()} SOURCES  ·  NOT FOR LISTING"
            t_layer, _ = render_text(txt, f, b.color("ink"), 1.5)
            pill = rounded_rect_layer(t_layer.width + 28, t_layer.height + 10, 8, fill=b.color("cream") + (225,))
            pill.alpha_composite(t_layer, (14, 5))
            capb = f.getbbox("H")
            pos = (int(dt["right"] - pill.width), int(dt["center_y"] - 5 - (capb[1] + capb[3]) / 2))
            self.draft_tag = (pill, pos)

    # ------------------------------------------------------------------ scenes
    def _prepare_scenes(self):
        b = self.b
        for i, sc in enumerate(self.scenes):
            st = {"i": i, "sc": sc, "tag": f"s{i + 1}:{sc.get('id', sc['type'])}"}
            if sc["type"] in ("screen", "morph"):
                ids = [sc["source"]] if sc["type"] == "screen" else [sc["source_from"], sc["source_to"]]
                srcs = []
                for sid in ids:
                    s = self.cfg["sources"][sid]
                    p = resolve(s["path"])
                    if s.get("type", "image") == "video":
                        srcs.append(VideoSource(p, self.fps, s.get("in", 0.0)))
                    else:
                        srcs.append(ImageSource(p, tuple(sc["_canvas"])))
                st["srcs"] = srcs
                cam = sc["camera"]
                smin = min(cam["from"][2], cam["to"][2]) / self.card[2]
                smax = max(cam["from"][2], cam["to"][2]) / self.card[2]
                st["level"] = srcs[0].level_for(smin)
                self.manifest["scenes"].append({"scene": st["tag"], "scale_min": round(smin, 3),
                                                "scale_max": round(smax, 3), "pyramid_level": st["level"],
                                                "max_upscale": round(max(1.0, 1 / smin), 3)})
                st["chips"] = [self._chip_layer(c) for c in sc.get("chips", [])]
                st["hl_labels"] = [self._label_layer(h["label"]) if h.get("label") else None
                                   for h in sc.get("highlights", [])]
            if sc.get("caption"):
                f = b.font("serif", b.type["caption_size"])
                layer, _ = render_text(sc["caption"], f, b.color("navy"))
                cap = f.getbbox("H")
                c = b.layout["caption"]
                st["caption"] = (layer, (int(c["x"]), int(c["center_y"] - (cap[1] + cap[3]) / 2)))
            if sc["type"] == "end_card":
                st["end"] = self._end_layers(sc)
            self.__dict__.setdefault("_st", []).append(st)

    def _label_layer(self, text):
        b = self.b
        f = b.font("sans_semibold", b.type["highlight_label_size"])
        t, _ = render_text(text, f, b.color("navy"))
        pill = rounded_rect_layer(t.width + 36, t.height + 16, 10, fill=b.color("gold") + (255,))
        pill.alpha_composite(t, (18, 7))
        return pill

    def _chip_layer(self, c):
        b = self.b
        S = 2  # render chip at 2x then reduce for smooth edges
        lf = b.font("sans_medium", b.type["chip_label_size"] * S)
        vf = b.font("sans_semibold", b.type["chip_value_size"] * S)
        label, _ = render_text(c["_label"].upper(), lf, b.color("gold_soft"), b.type["chip_label_tracking"] * S)
        v_from, _ = render_text(c["_from"], vf, b.color("cream"), opacity=0.62)
        v_to, _ = render_text(c["_to"], vf, b.color("cream"))
        arrow_w, gap = 54 * S, 22 * S
        px, py, lg = 34 * S, 24 * S, 14 * S
        vbox = vf.getbbox("0%Hg")
        vh = vbox[3]
        w = px * 2 + max(label.width, v_from.width + gap + arrow_w + gap + v_to.width)
        h = py * 2 + label.height + lg + vh
        chip = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(chip).rounded_rectangle([0, 0, w - 1, h - 1], radius=20 * S, fill=b.color("navy") + (246,))
        chip.alpha_composite(label, (px, py))
        y = py + label.height + lg
        chip.alpha_composite(v_from, (px, y))
        # vector arrow (fonts have no U+2192)
        d = ImageDraw.Draw(chip)
        ax0 = px + v_from.width + gap
        cap = vf.getbbox("0")
        ay = y + (cap[1] + cap[3]) / 2
        gold = b.color("gold") + (255,)
        d.line([(ax0, ay), (ax0 + arrow_w - 4 * S, ay)], fill=gold, width=4 * S)
        d.line([(ax0 + arrow_w - 18 * S, ay - 13 * S), (ax0 + arrow_w - 2 * S, ay),
                (ax0 + arrow_w - 18 * S, ay + 13 * S)], fill=gold, width=4 * S, joint="curve")
        chip.alpha_composite(v_to, (int(ax0 + arrow_w + gap), y))
        chip = chip.resize((w // S, h // S), Image.LANCZOS)
        return {"img": chip, "cfg": c, "text": f"{c['_label']}: {c['_from']} -> {c['_to']}"}

    def _end_layers(self, sc):
        b, e = self.b, self.b.end
        out = {}
        specs = [("title", "serif", b.type["end_title_size"], 0, e["title_color"], 455),
                 ("subtitle", "sans", b.type["end_subtitle_size"], b.type["end_subtitle_tracking"], e["subtitle_color"], 640),
                 ("brand", "sans_medium", b.type["end_brand_size"], b.type["end_brand_tracking"], e["brand_color"], 930)]
        for key, role, size, trk, col, cy in specs:
            txt = sc.get(key)
            if not txt:
                continue
            txt = txt.upper() if key == "brand" else txt
            f = b.font(role, size)
            layer, _ = render_text(txt, f, b.color(col), trk)
            cap = f.getbbox("H")
            out[key] = (layer, (int((self.W - layer.width) / 2), int(cy - (cap[1] + cap[3]) / 2)), size, txt)
        return out

    # ------------------------------------------------------------------ helpers
    def _bbox(self, layer, pos):
        bb = layer.getbbox() or (0, 0, 0, 0)
        return [pos[0] + bb[0], pos[1] + bb[1], pos[0] + bb[2], pos[1] + bb[3]]

    def _record(self, scene, kind, text, font_px, bbox, container):
        key = f"{scene}|{kind}|{text}"
        e = self.manifest["elements"].get(key)
        if e is None:
            e = self.manifest["elements"][key] = {"scene": scene, "kind": kind, "text": text,
                                                  "font_px": font_px, "container": container,
                                                  "bbox": list(bbox), "frames": 0}
        u = e["bbox"]
        e["bbox"] = [min(u[0], bbox[0]), min(u[1], bbox[1]), max(u[2], bbox[2]), max(u[3], bbox[3])]
        e["frames"] += 1

    def _card_image(self, st, src_i, rect, t_local):
        src = st["srcs"][src_i]
        x, y, w, h = rect
        cw, ch = self.card[2], self.card[3]
        if isinstance(src, ImageSource):
            k = st["level"]
            img, f = src.levels[k], 2 ** k
        else:
            img, _ = src.frame(max(0.0, t_local))
            f = 1
        s = w / cw
        return img.transform((cw, ch), Image.AFFINE, (s / f, 0, x / f, 0, s / f, y / f),
                             resample=Image.BICUBIC, fillcolor=(255, 255, 255))

    # ------------------------------------------------------------------ scene frame
    def scene_frame(self, st, u: float) -> Image.Image:
        sc, b = st["sc"], self.b
        m = b.motion
        if sc["type"] == "end_card":
            return self._end_frame(st, u)
        d = sc["duration"]
        cam = sc["camera"]
        e = in_out_cubic(u / d)
        f, t = cam["from"], cam["to"]
        # zoom interpolated geometrically (perceptually even), centre linearly
        w = f[2] * (t[2] / f[2]) ** e
        h = w * self.card[3] / self.card[2]
        cxm = (f[0] + f[2] / 2) + ((t[0] + t[2] / 2) - (f[0] + f[2] / 2)) * e
        cym = (f[1] + f[3] / 2) + ((t[1] + t[3] / 2) - (f[1] + f[3] / 2)) * e
        rect = (cxm - w / 2, cym - h / 2, w, h)
        s = w / self.card[2]
        img = self._card_image(st, 0, rect, u)
        if sc["type"] == "morph":
            mp = in_out_cubic((u - sc["swap_at"]) / sc["swap_duration"])
            if mp > 0:
                img = Image.blend(img, self._card_image(st, 1, rect, u), mp)
        cx, cy, cw, ch = self.card
        # --- highlights (card coordinates) ---
        hls = []
        for j, hcfg in enumerate(sc.get("highlights", [])):
            a0 = hcfg.get("appear", 0.3)
            a1 = hcfg.get("disappear", d + 10)
            o = out_cubic((u - a0) / m["highlight_fade"]) * (1 - out_cubic((u - a1) / m["highlight_fade"]))
            if o <= 0.01:
                continue
            x, y, hw, hh = hcfg["rect"]
            pad = hcfg.get("pad", b.hl["pad"]) + m["highlight_inflate"] * (1 - out_cubic((u - a0) / m["highlight_fade"]))
            X0, Y0 = (x - rect[0]) / s - pad, (y - rect[1]) / s - pad
            X1, Y1 = (x + hw - rect[0]) / s + pad, (y + hh - rect[1]) / s + pad
            hls.append((o, (X0, Y0, X1, Y1), j))
        if hls:
            dim = max(o for o, _, _ in hls) * b.hl["dim"]
            mask = Image.new("L", (cw, ch), int(255 * dim))
            md = ImageDraw.Draw(mask)
            for _, (X0, Y0, X1, Y1), _ in hls:
                md.rounded_rectangle([X0, Y0, X1, Y1], radius=b.hl["radius"], fill=0)
            mask = mask.filter(ImageFilter.GaussianBlur(1.5))
            img = Image.composite(Image.new("RGB", (cw, ch), b.color(b.hl.get("dim_color", "navy"))), img, mask)
        frame = self.base.copy()
        frame.paste(img, (cx, cy), self.card_mask)
        full = st["tag"]
        for o, (X0, Y0, X1, Y1), j in hls:
            sw = b.hl["stroke"]
            gx, gy = cx + X0 - sw, cy + Y0 - sw
            ix, iy = math.floor(gx), math.floor(gy)
            # stroke sits just outside the padded rect (PIL strokes inward from the bounds)
            ring = rounded_rect_layer(X1 - X0 + 2 * sw, Y1 - Y0 + 2 * sw, b.hl["radius"] + sw,
                                      outline=b.color(b.hl["color"]) + (255,), width=sw,
                                      frac=(gx - ix, gy - iy))
            frame.paste(fade(ring, o), (ix, iy), fade(ring, o))
            bbox = [cx + X0 - sw, cy + Y0 - sw, cx + X1 + sw, cy + Y1 + sw]
            if o > 0.99:
                self._record(full, "highlight", sc["highlights"][j].get("find") or f"highlight {j + 1}",
                             0, bbox, "card")
            lab = st["hl_labels"][j]
            if lab is not None:
                side = sc["highlights"][j].get("label_side", "above")
                if side in ("left", "right"):
                    lx = int(bbox[0] - 12 - lab.width if side == "left" else bbox[2] + 12)
                    ly = int((bbox[1] + bbox[3]) / 2 - lab.height / 2)
                else:
                    lx = int(min(max((bbox[0] + bbox[2]) / 2 - lab.width / 2, cx + 12), cx + cw - 12 - lab.width))
                    ly = int(bbox[1] - 12 - lab.height if side == "above" else bbox[3] + 12)
                    if side == "above" and ly < cy + 12:
                        ly = int(bbox[3] + 12)
                lab_o = fade(lab, o)
                frame.paste(lab_o, (lx, ly), lab_o)
                if o > 0.99:
                    self._record(full, "highlight_label", sc["highlights"][j]["label"],
                                 b.type["highlight_label_size"], [lx, ly, lx + lab.width, ly + lab.height], "card")
        # --- chips ---
        chip_boxes = []
        anchors = {}
        for chip in st["chips"]:
            anchors.setdefault(chip["cfg"].get("anchor", "bottom-left"), []).append(chip)
        ins, gap = b.layout["chip_inset"], b.layout["chip_gap"]
        for anchor, chips in anchors.items():
            total = sum(c["img"].width for c in chips) + gap * (len(chips) - 1)
            vert, horiz = anchor.split("-")
            x = {"left": cx + ins, "right": cx + cw - ins - total, "center": cx + (cw - total) / 2}[horiz]
            for c in chips:
                ci = c["img"]
                a0 = c["cfg"].get("appear", 0.5)
                p = out_cubic((u - a0) / m["chip_fade"])
                if p > 0.01:
                    y = (cy + ch - ins - ci.height) if vert == "bottom" else (cy + ins)
                    y += m["chip_rise"] * (1 - p)
                    layer = fade(ci, p)
                    frame.paste(layer, (int(x), int(y)), layer)
                    chip_boxes.append((c["text"], [x, y, x + ci.width, y + ci.height]))
                    if p > 0.99:
                        self._record(full, "chip", c["text"], b.type["chip_value_size"],
                                     [int(x), int(y), int(x) + ci.width, int(y) + ci.height], "card")
                x += ci.width + gap
        # occlusion bookkeeping: a visible chip must never sit on a visible highlight
        for text, cb in chip_boxes:
            for o, (X0, Y0, X1, Y1), j in hls:
                hb = [cx + X0 - b.hl["stroke"], cy + Y0 - b.hl["stroke"], cx + X1 + b.hl["stroke"], cy + Y1 + b.hl["stroke"]]
                if o > 0.05 and not (cb[2] <= hb[0] or hb[2] <= cb[0] or cb[3] <= hb[1] or hb[3] <= cb[1]):
                    self.manifest.setdefault("overlaps", []).append(
                        {"scene": full, "t_local": round(u, 3), "chip": text, "highlight": j + 1})
        self._caption(frame, st, u)
        return frame

    def _caption(self, frame, st, u):
        if "caption" not in st:
            return
        m = self.b.motion
        layer, (x, y) = st["caption"]
        p = 1.0 if st["i"] == 0 else out_cubic((u - m["caption_delay"]) / m["caption_fade"])
        if p <= 0.01:
            return
        y = y + m["caption_rise"] * (1 - p)
        lay = fade(layer, p)
        frame.paste(lay, (int(x), int(y)), lay)
        if p > 0.99:
            self._record(st["tag"], "caption", st["sc"]["caption"], self.b.type["caption_size"],
                         self._bbox(layer, (int(x), int(y))), "frame")

    def _end_frame(self, st, u):
        frame = self.end_bg.copy()
        L = st["end"]
        timing = {"title": 0.15, "subtitle": 0.75, "brand": 1.0}
        for key, (layer, (x, y), size, txt) in L.items():
            p = out_cubic((u - timing[key]) / 0.6)
            if p <= 0.01:
                continue
            yy = int(y + 12 * (1 - p))
            lay = fade(layer, p)
            frame.paste(lay, (x, yy), lay)
            if p > 0.99:
                self._record(st["tag"], f"end_{key}", txt, size, self._bbox(layer, (x, yy)), "frame")
        # gold rule grows from centre
        rp = in_out_cubic((u - 0.45) / 0.7)
        if rp > 0:
            rw = self.b.end["rule_width"] * rp
            d = ImageDraw.Draw(frame)
            d.rectangle([self.W / 2 - rw / 2, 548, self.W / 2 + rw / 2, 550], fill=self.b.color(self.b.end["rule_color"]))
        return frame

    # ------------------------------------------------------------------ timeline
    def frame(self, n: int) -> Image.Image:
        t = n / self.fps
        idx = 0
        for i, sc in enumerate(self.scenes):
            if t >= sc["_start"]:
                idx = i
        st = self._st[idx]
        img = self.scene_frame(st, t - st["sc"]["_start"])
        # crossfade into the NEXT scene (centred on the cut) / out of the PREVIOUS one
        if idx + 1 < len(self.scenes):
            nxt = self._st[idx + 1]
            tr = nxt["sc"]["transition"]
            cut = nxt["sc"]["_start"]
            if tr and t > cut - tr / 2:
                p = in_out_cubic((t - (cut - tr / 2)) / tr)
                img = Image.blend(img, self.scene_frame(nxt, t - cut), p)
        if idx > 0:
            tr = st["sc"]["transition"]
            cut = st["sc"]["_start"]
            if tr and t < cut + tr / 2:
                prv = self._st[idx - 1]
                p = in_out_cubic((t - (cut - tr / 2)) / tr)
                img = Image.blend(self.scene_frame(prv, t - prv["sc"]["_start"]), img, p)
        if self.draft_tag:
            pill, pos = self.draft_tag
            img.paste(pill, pos, pill)
        return img

    def close(self):
        for st in self._st:
            for s in st.get("srcs", []):
                if isinstance(s, VideoSource):
                    s.close()
