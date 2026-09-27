#!/usr/bin/env python3
"""Ledger & Lime Automated Etsy Video Engine - one command per product.

    python render_video.py configs/product13_iep_tracker.json

Steps: 1) validate config (incl. product-truth checks)  2) render frames
3) encode H.264 MP4  4) run automated QA  5) write QA artifacts + report.

Options:
    --validate-only   stop after step 1
    --skip-qa         render without QA (not recommended)
    --draft           fast encode (preset veryfast) for layout iteration
Exit code: 0 = rendered and QA PASS/PASS-WITH-NOTES, 1 = validation error, 2 = QA FAIL.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from engine import config as cfgmod  # noqa: E402
from engine.encode import encode  # noqa: E402
from engine.render import Renderer  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("config")
    ap.add_argument("--validate-only", action="store_true")
    ap.add_argument("--skip-qa", action="store_true")
    ap.add_argument("--draft", action="store_true")
    a = ap.parse_args()

    print(f"[1/5] validating {a.config}")
    try:
        cfg, brand, rep = cfgmod.load(a.config)
    except cfgmod.ConfigError as e:
        print(f"CONFIG INVALID:\n{e}")
        return 1
    for w in rep.warnings:
        print(f"  warning: {w}")
    for n in rep.notes:
        print(f"  note: {n}")
    print(f"  ok - {len(cfg['scenes'])} scenes, {cfg['_duration']:.2f}s")
    if a.validate_only:
        return 0

    out_dir = ROOT / "output" / cfg["product"]["id"]
    out_dir.mkdir(parents=True, exist_ok=True)
    mp4 = out_dir / cfg["output"]["filename"]

    print(f"[2/5] rendering {cfg['_duration']:.2f}s @ {cfg['output']['fps']} fps")
    r = Renderer(cfg, brand)
    t0 = time.time()

    def prog(i, n):
        if i % 30 == 0 or i == n:
            print(f"  frame {i}/{n}  ({time.time() - t0:.0f}s)", flush=True)

    print(f"[3/5] encoding -> {mp4.relative_to(ROOT)}")
    encode(r, mp4, prog, preset="veryfast" if a.draft else "slow")
    manifest = {"config": str(Path(a.config)), "duration": cfg["_duration"], "fps": cfg["output"]["fps"],
                "nframes": r.nframes, "card": brand.layout["card"],
                "safe_margin": brand.layout["safe_margin"], "width": r.W, "height": r.H,
                "draft_watermark": r.draft, "validation": rep.__dict__,
                "scenes": r.manifest["scenes"], "elements": list(r.manifest["elements"].values()),
                "overlaps": r.manifest.get("overlaps", []),
                "double_table": r.manifest.get("double_table", []),
                "transitions": {"scene": brand.motion.get("scene_transition", "crossfade"),
                                "morph": brand.motion.get("morph_style", "dissolve")},
                "timeline": [{"id": s.get("id", s["type"]), "type": s["type"], "start": s["_start"],
                              "duration": s["duration"], "caption": s.get("caption", ""),
                              "expect_text": s.get("expect_text", [])} for s in cfg["scenes"]]}
    (out_dir / "render-manifest.json").write_text(json.dumps(manifest, indent=1))
    if a.skip_qa:
        print("QA skipped")
        return 0

    print("[4/5] running QA")
    from qa.run_qa import run_qa
    verdict, report = run_qa(cfg, mp4, out_dir, manifest)
    print(f"[5/5] QA verdict: {verdict}\n  report: {report.relative_to(ROOT)}")
    return 2 if verdict.startswith("FAIL") else 0


if __name__ == "__main__":
    sys.exit(main())
