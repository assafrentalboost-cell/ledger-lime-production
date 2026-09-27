"""Brand template loading: colours, fonts, text measurement and drawing helpers."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ENGINE_ROOT = Path(__file__).resolve().parents[1]


def hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


class Brand:
    def __init__(self, name_or_path: str):
        p = Path(name_or_path)
        if not p.suffix:
            p = ENGINE_ROOT / "templates" / f"{name_or_path}.json"
        self.path = p
        self.t = json.loads(p.read_text())
        self.colors = {k: hex_rgb(v) for k, v in self.t["colors"].items()}
        self.layout = self.t["layout"]
        self.type = self.t["type"]
        self.motion = self.t["motion"]
        self.hl = self.t["highlight"]
        self.end = self.t["end_card"]

    def color(self, key_or_hex: str) -> tuple[int, int, int]:
        return hex_rgb(key_or_hex) if key_or_hex.startswith("#") else self.colors[key_or_hex]

    def font_path(self, role: str) -> Path:
        return ENGINE_ROOT / self.t["fonts"][role]

    def font(self, role: str, size: int) -> ImageFont.FreeTypeFont:
        return _font(str(self.font_path(role)), int(size))

    def missing_glyphs(self, role: str, text: str) -> set[str]:
        cmap = _cmap(str(self.font_path(role)))
        return {ch for ch in text if not ch.isspace() and ord(ch) not in cmap}


@lru_cache(maxsize=64)
def _font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


@lru_cache(maxsize=16)
def _cmap(path: str) -> frozenset:
    return frozenset(TTFont(path).getBestCmap().keys())


def text_width(font: ImageFont.FreeTypeFont, text: str, tracking: float = 0) -> float:
    if not tracking:
        return font.getlength(text)
    return sum(font.getlength(c) for c in text) + tracking * max(0, len(text) - 1)


def render_text(text: str, font: ImageFont.FreeTypeFont, color, tracking: float = 0,
                opacity: float = 1.0) -> tuple[Image.Image, int]:
    """Render text to a tight RGBA layer. Returns (layer, ascent) where ascent is
    the distance from the layer's top to the baseline."""
    ascent, descent = font.getmetrics()
    w = int(text_width(font, text, tracking) + 4)
    layer = Image.new("RGBA", (max(w, 1), ascent + descent + 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    fill = tuple(color) + (int(255 * opacity),)
    if tracking:
        x = 0.0
        for c in text:
            d.text((x, 0), c, font=font, fill=fill)
            x += font.getlength(c) + tracking
    else:
        d.text((0, 0), text, font=font, fill=fill)
    return layer, ascent
