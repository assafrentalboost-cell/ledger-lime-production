#!/usr/bin/env python3
"""Assemble stepwise captures (e.g. a workbook captured after each typed cell)
into a short MP4 clip that can be used as a `"type": "video"` source.

    python tools/stills_to_clip.py OUT.mp4 step0.png step1.png step2.png step3.png --hold 0.8 0.6 0.6 1.5

Every frame of the clip is one of the real captured states - nothing is
interpolated or drawn. No pointer is added.
"""
import argparse
import subprocess
import tempfile
from pathlib import Path

from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("out")
ap.add_argument("stills", nargs="+")
ap.add_argument("--hold", nargs="+", type=float, required=True, help="seconds per still")
ap.add_argument("--fps", type=int, default=30)
a = ap.parse_args()
assert len(a.hold) == len(a.stills), "one --hold value per still"
sizes = {Image.open(s).size for s in a.stills}
assert len(sizes) == 1, f"stills must share one size (same capture geometry), got {sizes}"
w, h = sizes.pop()
with tempfile.TemporaryDirectory() as td:
    lst = Path(td) / "list.txt"
    lines = []
    for s, d in zip(a.stills, a.hold):
        lines += [f"file '{Path(s).resolve()}'", f"duration {d}"]
    lines.append(f"file '{Path(a.stills[-1]).resolve()}'")
    lst.write_text("\n".join(lines) + "\n")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-vf", f"fps={a.fps},pad=ceil(iw/2)*2:ceil(ih/2)*2:color=white,format=yuv444p",
                    "-c:v", "libx264", "-crf", "10", "-preset", "slow", "-movflags", "+faststart",
                    a.out], check=True)
print(a.out, f"{w}x{h}", f"{sum(a.hold):.2f}s")
