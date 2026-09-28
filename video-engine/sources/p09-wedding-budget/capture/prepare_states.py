#!/usr/bin/env python3
"""Prepare Product #9 capture states from the REAL packaged workbook.

Nothing is reconstructed. Both states are copies of
../Premium-Wedding-Budget-System.xlsx (the QA'd customer workbook):

  after  : the packaged workbook exactly as shipped (sample data loaded).
           Tasty Catering Co (Catering & Bar): Contracted $8,500,
           Total Paid To Date $8,500 -> PAID IN FULL.
  before : the same workbook with that ONE vendor's final payment not yet
           logged, using the sample's own convention for vendors with an open
           balance (every other vendor row: Total Paid To Date = Deposit
           Required): Total Paid To Date = its $1,000 deposit.

Status and the Dashboard's overdue figures compare due dates with
Settings!B7 = TODAY() ("auto - do not edit"), so both states are captured in
the same run and the capture date is recorded.

Only view settings change in the copies: two sheets visible (Vendor &
Payments, Dashboard) with print areas on the filmed rows, the workbook's
default font made explicit, and columns widened just enough for headers to
read in full. Every value is recalculated by LibreOffice.

Usage: python prepare_states.py OUT_DIR
"""
import json
import sys
from pathlib import Path

from openpyxl import load_workbook

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from tools.capture_prep import explicit_default_font, fit_columns, print_one_page  # noqa: E402

SRC = Path(__file__).resolve().parents[1] / "Premium-Wedding-Budget-System.xlsx"
VP, DB = "Vendor & Payments", "Dashboard"
VP_AREA = "A3:I8"     # header + the 5 sample vendors
DB_AREA = "A5:B12"    # Total Committed .. Overdue Payments - Amount


def build(state: str, out: Path):
    wb = load_workbook(SRC)
    vp, db = wb[VP], wb[DB]
    if state == "before":
        vp["E5"].value = vp["D5"].value      # catering: deposit paid, final payment not yet logged
    for ws in wb.worksheets:
        if ws.title not in (VP, DB):
            ws.sheet_state = "hidden"
    wb.active = wb.worksheets.index(vp)
    explicit_default_font(wb, vp, VP_AREA)
    explicit_default_font(wb, db, DB_AREA)
    widened = {VP: fit_columns(vp, [3]), DB: fit_columns(db, list(range(5, 13)), ["A"])}
    print_one_page(vp, VP_AREA)
    print_one_page(db, DB_AREA, landscape=False)
    p = out / f"p09_{state}.xlsx"
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
