#!/usr/bin/env python3
"""Prepare Product #11 capture states from the REAL delivered workbook.

Nothing is reconstructed. Both states are copies of
../workbook/Aging-Parent-Financial-Organizer.xlsx (Etsy buyer file, 223,940
bytes, SHA-256 eaaac91d...9f23; never modified - copies are saved elsewhere):

  after  : the delivered workbook exactly as shipped (sample family loaded).
           Expense E7 (Dental copay, $40, paid by a sibling) is matched by
           contribution C7 ($40 from the Parent Account, Related Expense E7)
           -> Reimbursement Status "Reimbursed", Remaining $0.
  before : the same workbook with that ONE reimbursement not yet recorded:
           the C7 row's input cells are empty (the workbook's own convention
           for an unused row - its auto columns then return 0 / blank).

Formula chain (unchanged): Family Contributions G (Applied) = F when a
Related Expense ID is set -> Expenses M (Reimbursed) = SUMIF on that ID ->
N (Remaining) = G - M -> L (Status) -> Dashboard B5 (Reimbursements Pending
= COUNTIF Pending + Partially Reimbursed) and B7 (Outstanding Reimbursement
= SUMPRODUCT of N over Pending/Partial rows). None of the filmed values use
TODAY().

Only view settings change in the copies: three sheets visible (Expenses &
Receipts, Family Contributions, Dashboard) with print areas on the filmed
rows, the workbook's default font made explicit, and columns widened just
enough for headers (and the sample Description / Category text) to read
in full. Every value is recalculated by
LibreOffice.

Usage: python prepare_states.py OUT_DIR
"""
import json
import sys
from pathlib import Path

from openpyxl import load_workbook

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from tools.capture_prep import explicit_default_font, fit_columns, print_one_page  # noqa: E402

SRC = Path(__file__).resolve().parents[1] / "workbook" / "Aging-Parent-Financial-Organizer.xlsx"
EX, FC, DB = "Expenses & Receipts", "Family Contributions", "Dashboard"
EX_AREA = "A3:N10"    # header + the 7 sample expenses (E1-E7)
FC_AREA = "A3:J11"    # header + the 8 sample contributions (C1-C8)
DB_AREA = "A1:B10"    # title + Monthly Bills .. Open Financial Tasks
C7_ROW = 10           # contribution C7 -> E7
C7_INPUTS = "ABCDEFIJ"  # input columns only; G/H are formulas and stay


def build(state: str, out: Path):
    wb = load_workbook(SRC)
    ex, fc, db = wb[EX], wb[FC], wb[DB]
    assert fc[f"A{C7_ROW}"].value == "C7" and fc[f"I{C7_ROW}"].value == "E7"
    if state == "before":
        for col in C7_INPUTS:
            fc[f"{col}{C7_ROW}"].value = None      # reimbursement not yet recorded
    keep = (EX, FC, DB)
    for ws in wb.worksheets:
        if ws.title not in keep:
            ws.sheet_state = "hidden"
    wb.active = wb.worksheets.index(ex)
    explicit_default_font(wb, ex, EX_AREA)
    explicit_default_font(wb, fc, FC_AREA)
    explicit_default_font(wb, db, DB_AREA)
    widened = {EX: fit_columns(ex, [3]) | fit_columns(ex, list(range(4, 11)), ["D"]),
               FC: fit_columns(fc, [3]) | fit_columns(fc, list(range(4, 12)), ["E"]),
               DB: fit_columns(db, list(range(3, 11)), ["A"])}
    print_one_page(ex, EX_AREA)
    print_one_page(fc, FC_AREA)
    print_one_page(db, DB_AREA, landscape=False)
    p = out / f"p11_{state}.xlsx"
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
