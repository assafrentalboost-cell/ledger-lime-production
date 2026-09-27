"""Source media: still captures (with a mip pyramid for clean zooms) and video clips."""
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

from PIL import Image


def probe_video(path: Path) -> tuple[int, int, float, float]:
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height,r_frame_rate:format=duration", "-of", "json", str(path)],
                         capture_output=True, check=True, text=True).stdout
    j = json.loads(out)
    s = j["streams"][0]
    n, d = s["r_frame_rate"].split("/")
    return int(s["width"]), int(s["height"]), float(n) / float(d), float(j["format"]["duration"])


class ImageSource:
    def __init__(self, path: Path, canvas: tuple[int, int] | None = None, offset: tuple[int, int] = (0, 0)):
        im = Image.open(path).convert("RGB")
        if canvas and (canvas != im.size or offset != (0, 0)):  # common / padded canvas
            c = Image.new("RGB", canvas, (255, 255, 255))
            c.paste(im, tuple(offset))
            im = c
        self.size = im.size
        self.levels = [im]
        while min(self.levels[-1].size) > 256:
            prev = self.levels[-1]
            self.levels.append(prev.resize((prev.width // 2, prev.height // 2), Image.LANCZOS))

    def frame(self, t: float) -> tuple[Image.Image, float]:
        return self.levels[0], 1.0

    def level_for(self, min_scale: float) -> int:
        """Pyramid level so the residual resample never upsamples a reduced level."""
        return max(0, min(len(self.levels) - 1, int(math.floor(math.log2(max(min_scale, 1.0))))))


class VideoSource:
    """Sequential decoder: frames are requested in increasing time order."""

    def __init__(self, path: Path, fps: float, start: float = 0.0):
        self.path, self.fps, self.start = path, fps, start
        w, h, _, dur = probe_video(path)
        self.size, self.duration = (w, h), dur
        self.levels = None
        self._proc = None
        self._idx = -1
        self._last = Image.new("RGB", self.size, (255, 255, 255))

    def _open(self):
        self._proc = subprocess.Popen(
            ["ffmpeg", "-v", "error", "-ss", f"{self.start:.3f}", "-i", str(self.path), "-vf",
             f"fps={self.fps}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
            stdout=subprocess.PIPE)

    def frame(self, t: float) -> tuple[Image.Image, float]:
        want = max(0, int(round(t * self.fps)))
        if self._proc is None:
            self._open()
        n = self.size[0] * self.size[1] * 3
        while self._idx < want:
            buf = self._proc.stdout.read(n)
            if len(buf) < n:  # clip ended: hold last frame
                break
            self._last = Image.frombytes("RGB", self.size, buf)
            self._idx += 1
        return self._last, 1.0

    def level_for(self, min_scale: float) -> int:
        return 0

    def close(self):
        if self._proc:
            self._proc.stdout.close()
            self._proc.kill()
            self._proc = None
