#!/usr/bin/env python3
"""Capture every sheet of an .xlsx workbook as a high-resolution PNG.

The workbook is opened by LibreOffice (headless), which RECALCULATES every
formula on load, then exported to PDF and rasterised with pdftoppm. The
resulting PNGs are therefore genuine renders of real workbook state - no
values are painted on afterwards.

Usage:
    python tools/capture_workbook.py WORKBOOK.xlsx OUT_DIR [--dpi 220] [--prefix before_]

Produces OUT_DIR/<prefix><sheet-slug>.png (one per sheet, in sheet order)
plus OUT_DIR/<prefix>recalculated.json with the recalculated cell values of
every sheet (read back from LibreOffice's own .xlsx re-save) so the numbers
used in a video can be verified against the workbook.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def soffice_convert(src: Path, fmt: str, outdir: Path) -> Path:
    cmd = ["soffice", "--headless", "--norestore", "--convert-to", fmt,
           "--outdir", str(outdir), str(src)]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    ext = fmt.split(":")[0]
    out = outdir / f"{src.stem}.{ext}"
    if not out.exists():
        raise RuntimeError(f"LibreOffice did not produce {out}")
    return out


def trim_white(png: Path, pad: int = 24) -> None:
    from PIL import Image, ImageChops
    im = Image.open(png).convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    bbox = ImageChops.difference(im, bg).getbbox()
    if bbox:
        l, t, r, b = bbox
        im = im.crop((max(0, l - pad), max(0, t - pad), min(im.width, r + pad), min(im.height, b + pad)))
    im.save(png, optimize=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("workbook")
    ap.add_argument("out_dir")
    ap.add_argument("--dpi", type=int, default=220)
    ap.add_argument("--prefix", default="")
    a = ap.parse_args()

    wb_path = Path(a.workbook).resolve()
    out = Path(a.out_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)

    import openpyxl
    # hidden sheets are not exported to PDF, so only visible sheets map to pages
    sheet_names = [ws.title for ws in openpyxl.load_workbook(wb_path).worksheets if ws.sheet_state == "visible"]

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        # 1) Recalculated values: let LibreOffice load (recalc) and re-save as xlsx.
        recalc_dir = td / "recalc"
        recalc_dir.mkdir()
        recalc = soffice_convert(wb_path, "xlsx:Calc MS Excel 2007 XML", recalc_dir)
        vals = {}
        rwb = openpyxl.load_workbook(recalc, data_only=True)
        for ws in rwb.worksheets:
            cells = {}
            for row in ws.iter_rows():
                for c in row:
                    if c.value is not None:
                        v = c.value
                        cells[c.coordinate] = v if isinstance(v, (int, float, str, bool)) else str(v)
            vals[ws.title] = cells
        (out / f"{a.prefix}recalculated.json").write_text(json.dumps(vals, indent=1, default=str))

        # 2) Visual capture: PDF (one page per sheet, per the workbook's page setup) -> PNG.
        pdf = soffice_convert(wb_path, "pdf", td)
        subprocess.run(["pdftoppm", "-r", str(a.dpi), "-png", str(pdf), str(td / "page")], check=True)
        pages = sorted(td.glob("page-*.png"))
        if len(pages) != len(sheet_names):
            print(f"warning: {len(pages)} pages for {len(sheet_names)} sheets; "
                  "set fitToPage so each sheet prints on one page", file=sys.stderr)
        for name, page in zip(sheet_names, pages):
            dst = out / f"{a.prefix}{slug(name)}.png"
            shutil.move(str(page), dst)
            trim_white(dst)
            print(dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
