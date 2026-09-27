#!/usr/bin/env python3
"""Prepare Product #10 capture states from the REAL packaged workbook.

Nothing is reconstructed. Both states are copies of
../Rental-Property-Spreadsheet.xlsx (the QA'd customer workbook):

  after  : the packaged workbook exactly as shipped (sample data loaded).
  before : the same workbook with ONE input cleared - May 2026 "Payment 1"
           for unit P1-U1 (Rent Tracker H5 = 1000, I5 = 2026-05-04) - i.e.
           the moment before the landlord logs that partial payment.

Only print settings change in the copies (Rent Tracker print area = the
header + unit P1-U1 rows, other sheets hidden), so LibreOffice exports just
the rows being filmed. Every value is recalculated by LibreOffice from the
product's own formulas.

Usage: python prepare_states.py OUT_DIR
"""
import sys
from pathlib import Path

from copy import copy

from openpyxl import load_workbook

SRC = Path(__file__).resolve().parents[1] / "Rental-Property-Spreadsheet.xlsx"
PRINT_AREA = "A3:P9"          # header row + P1-U1 Apr..Sep 2026
INPUT_CELLS = ("H5", "I5")    # May 2026 Payment 1 (1000) + its date


def build(state: str, out: Path) -> Path:
    wb = load_workbook(SRC)
    rt = wb["Rent Tracker"]
    if state == "before":
        for c in INPUT_CELLS:
            rt[c].value = None
    for ws in wb.worksheets:
        if ws.title != "Rent Tracker":
            ws.sheet_state = "hidden"
    wb.active = wb.worksheets.index(rt)
    # Fonts saved without a name render in the workbook's default font in Excel
    # (Normal style = Calibri). LibreOffice would substitute a serif instead,
    # so make that default explicit. Rendering only - no value or layout change.
    default = wb._fonts[0].name or "Calibri"
    for row in rt[PRINT_AREA]:
        for c in row:
            if c.font is not None and not c.font.name:
                f = copy(c.font)
                f.name = default
                c.font = f
    rt.print_area = PRINT_AREA
    rt.page_setup.orientation = "landscape"
    rt.sheet_properties.pageSetUpPr.fitToPage = True
    rt.page_setup.fitToWidth = 1
    rt.page_setup.fitToHeight = 1
    rt.print_options.gridLines = True
    p = out / f"p10_{state}.xlsx"
    wb.save(p)
    return p


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    out.mkdir(parents=True, exist_ok=True)
    for st in ("before", "after"):
        print(build(st, out))
