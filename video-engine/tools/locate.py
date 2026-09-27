#!/usr/bin/env python3
"""Print pixel coordinates of text in a capture - use them for crops/highlights.

    python tools/locate.py sources/p13-iep-tracker/captures/before_dashboard.png "No Recent Data" "Needs Attention"
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from engine import ocr  # noqa: E402

img, *phrases = sys.argv[1:]
for p in phrases:
    try:
        print(f'{p!r}: [x, y, w, h] = {list(ocr.locate(img, p))}')
    except LookupError as e:
        print(e)
