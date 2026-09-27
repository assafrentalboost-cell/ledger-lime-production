"""FFmpeg encoder: RGB frames on stdin -> H.264 / yuv420p / BT.709 / faststart MP4 (web + Etsy safe)."""
from __future__ import annotations

import subprocess
from pathlib import Path


def ffmpeg_cmd(out: Path, w: int, h: int, fps: int, crf: int = 17, preset: str = "slow") -> list[str]:
    return ["ffmpeg", "-y", "-v", "error",
            "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", str(fps), "-i", "-",
            "-vf", "scale=out_color_matrix=bt709:out_range=tv,format=yuv420p",
            "-c:v", "libx264", "-preset", preset, "-crf", str(crf),
            "-profile:v", "high", "-level:v", "4.1", "-g", str(fps * 2), "-bf", "2",
            "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
            "-movflags", "+faststart", "-an", str(out)]


def encode(renderer, out: Path, progress=None, crf: int = 17, preset: str = "slow") -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.Popen(ffmpeg_cmd(out, renderer.W, renderer.H, renderer.fps, crf, preset),
                            stdin=subprocess.PIPE)
    try:
        for n in range(renderer.nframes):
            proc.stdin.write(renderer.frame(n).tobytes())
            if progress:
                progress(n + 1, renderer.nframes)
    finally:
        proc.stdin.close()
        rc = proc.wait()
        renderer.close()
    if rc != 0:
        raise RuntimeError(f"ffmpeg exited with {rc}")
