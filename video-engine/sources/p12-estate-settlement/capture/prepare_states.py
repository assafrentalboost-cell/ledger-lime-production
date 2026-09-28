#!/usr/bin/env python3
"""Prepare Product #12 capture states from the REAL packaged workbook.

Nothing is reconstructed. Both states are copies of
../Estate-Settlement-Command-Center.xlsx (the QA'd customer workbook):

  after  : the packaged workbook exactly as shipped (sample data loaded).
           Liability L3 (Lakeside Funeral Home, $8,900 verified) is Paid:
           Amount Paid 8900, Payment Date 2026-07-16.
  before : the same workbook with that ONE liability record not yet updated,
           using the sample's own convention for unpaid rows (see L4/L5):
           Status "Verified, Unpaid", Amount Paid 0, Payment Date blank.

Only view settings change in the copies: two sheets visible (Command Center,
Liability Register) with print areas on the filmed rows, the workbook's
default font made explicit, and columns widened just enough that headers /
auto-warnings read in full. Every value is recalculated by LibreOffice.

Usage: python prepare_states.py OUT_DIR
"""
import json
import sys
from pathlib import Path

from openpyxl import load_workbook

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from tools.capture_prep import (explicit_default_font, fit_column_to_text,  # noqa: E402
                                fit_columns, print_one_page)

SRC = Path(__file__).resolve().parents[1] / "Estate-Settlement-Command-Center.xlsx"
LR, CC = "04_LIABILITY_REGISTER", "01_COMMAND_CENTER"
LR_AREA = "A3:K8"      # header + L1..L5
CC_AREA = "A12:B19"    # closeout status + NEEDS ATTENTION NOW
BEFORE = {"H6": "Verified, Unpaid", "I6": 0, "J6": None}   # liability L3, pre-update


def build(state: str, out: Path) -> tuple[Path, dict]:
    wb = load_workbook(SRC)
    lr, cc = wb[LR], wb[CC]
    if state == "before":
        for cell, v in BEFORE.items():
            lr[cell].value = v
    for ws in wb.worksheets:
        if ws.title not in (LR, CC):
            ws.sheet_state = "hidden"
    wb.active = wb.worksheets.index(cc)
    explicit_default_font(wb, lr, LR_AREA)
    explicit_default_font(wb, cc, CC_AREA)
    widened = {LR: fit_columns(lr, [3]), CC: fit_columns(cc, list(range(12, 20)), ["A"])}
    k = fit_column_to_text(lr, "K", ["⚠ unpaid verified balance", "⚠ disputed item"],
                           lr["K4"].font.name, lr["K4"].font.sz or 11)
    if k:
        widened[LR]["K"] = k
    print_one_page(lr, LR_AREA)
    print_one_page(cc, CC_AREA, landscape=False)
    p = out / f"p12_{state}.xlsx"
    wb.save(p)
    return p, widened


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    out.mkdir(parents=True, exist_ok=True)
    for st in ("before", "after"):
        p, widened = build(st, out)
        print(p)
    (out / "widened-columns.json").write_text(json.dumps(
        {sh: {c: {"shipped": a, "capture": b} for c, (a, b) in cols.items()} for sh, cols in widened.items()}, indent=1))
