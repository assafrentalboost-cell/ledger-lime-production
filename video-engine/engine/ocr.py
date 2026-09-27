"""Tesseract helpers: locate text in source captures and read text back from frames."""
from __future__ import annotations

import csv
import io
import re
import shutil
import subprocess
from functools import lru_cache
from pathlib import Path

from PIL import Image


def available() -> bool:
    return shutil.which("tesseract") is not None


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9%]+", "", s.lower())


def _tsv(img: Image.Image, psm: int = 11) -> list[dict]:
    buf = io.BytesIO()
    img.convert("RGB").save(buf, format="PNG")
    out = subprocess.run(["tesseract", "stdin", "stdout", "--psm", str(psm), "tsv"],
                         input=buf.getvalue(), capture_output=True, check=True).stdout.decode()
    rows = list(csv.DictReader(io.StringIO(out), delimiter="\t", quoting=csv.QUOTE_NONE))
    words = []
    for r in rows:
        t = (r.get("text") or "").strip()
        if t and float(r.get("conf", -1)) > 30:
            words.append({"text": t, "x": int(r["left"]), "y": int(r["top"]),
                          "w": int(r["width"]), "h": int(r["height"]),
                          "line": (r["block_num"], r["par_num"], r["line_num"])})
    return words


@lru_cache(maxsize=32)
def _words_for(path: str) -> tuple:
    return tuple(tuple(sorted(w.items())) for w in _tsv(Image.open(path)))


def locate(path: str | Path, phrase: str, occurrence: int = 1) -> tuple[int, int, int, int]:
    """Return (x, y, w, h) of the Nth occurrence of `phrase` in an image.

    Matches consecutive words on the same OCR line; comparison ignores case
    and punctuation. Raises LookupError when not found.
    """
    words = [dict(w) for w in _words_for(str(Path(path).resolve()))]
    target = [_norm(p) for p in phrase.split() if _norm(p)]
    hits = []
    for i in range(len(words)):
        seq = words[i:i + len(target)]
        if len(seq) < len(target) or len({w["line"] for w in seq}) != 1:
            continue
        if all(_norm(w["text"]) == t for w, t in zip(seq, target)):
            x0 = min(w["x"] for w in seq); y0 = min(w["y"] for w in seq)
            x1 = max(w["x"] + w["w"] for w in seq); y1 = max(w["y"] + w["h"] for w in seq)
            hits.append((x0, y0, x1 - x0, y1 - y0))
    hits.sort(key=lambda b: (b[1], b[0]))
    if len(hits) < occurrence:
        raise LookupError(f'"{phrase}" not found in {path} (found {len(hits)} match(es))')
    return hits[occurrence - 1]


def strip_color(img: Image.Image, rgb, tol: float = 70) -> Image.Image:
    """Paint pixels close to `rgb` white. Used to remove highlight strokes:
    Tesseract tends to drop text that sits inside a closed rectangle."""
    import numpy as np
    a = np.asarray(img.convert("RGB")).copy()
    d = np.sqrt(((a.astype(int) - np.array(rgb)) ** 2).sum(-1))
    a[d < tol] = 255
    return Image.fromarray(a)


def read_text(img: Image.Image, tiles: int = 2, strip=None) -> str:
    """OCR a frame: one full pass plus overlapping tile passes (text next to
    highlight strokes is easily missed in a single full-frame pass).
    `strip`: list of RGB colours (e.g. the highlight stroke) removed first."""
    for rgb in strip or []:
        img = strip_color(img, rgb)
    def one(im):
        big = im.resize((im.width * 2, im.height * 2), Image.LANCZOS) if im.width < 2400 else im
        return " ".join(w["text"] for w in _tsv(big, psm=11))
    parts = [one(img)]
    W, H = img.size
    tw, th = W / tiles, H / tiles
    for i in range(tiles):
        for j in range(tiles):
            box = (int(max(0, i * tw - tw * 0.15)), int(max(0, j * th - th * 0.15)),
                   int(min(W, (i + 1) * tw + tw * 0.15)), int(min(H, (j + 1) * th + th * 0.15)))
            parts.append(one(img.crop(box)))
    return " | ".join(parts)


def contains(haystack: str, needle: str) -> bool:
    return _norm(needle) in _norm(haystack)
