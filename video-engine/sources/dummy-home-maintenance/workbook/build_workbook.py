#!/usr/bin/env python3
"""DUMMY product for the engine reusability test (not a Ledger & Lime listing).

"Home Maintenance Planner & Service Log": a real formula-driven workbook.
States (each is a real workbook, recalculated by LibreOffice on capture):
  step0 / before : service log without the new entry
  step1          : date typed
  step2          : date + task typed
  step3 / after  : full entry (date, task, cost, note)

Logging "Replace HVAC filter" moves that task from Overdue to Scheduled,
Overdue 3 -> 2 and On Schedule 58% -> 67% - all via formulas.

Usage: python build_workbook.py OUT_DIR
"""
import sys
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.page import PageMargins

TEAL, SAND, INK, MUTED, LINE = "1F4E5A", "F3EFE6", "1E2A2E", "6B7280", "D5D0C4"
REPORT_DATE = date(2026, 9, 25)
TASKS = [  # task, area, every N days
    ("Replace HVAC filter", "HVAC", 90), ("Clean gutters", "Exterior", 180),
    ("Test smoke detectors", "Safety", 30), ("Flush water heater", "Plumbing", 365),
    ("Clean dryer vent", "Laundry", 180), ("Service lawn mower", "Garden", 365),
    ("Check fire extinguisher", "Safety", 180), ("Clean fridge coils", "Kitchen", 180),
    ("Inspect roof", "Exterior", 365), ("Test GFCI outlets", "Electrical", 90),
    ("Seal grout", "Bathroom", 365), ("Clean range hood filter", "Kitchen", 90),
]
LOG = [
    (date(2026, 5, 20), "Replace HVAC filter", 24), (date(2026, 3, 2), "Clean gutters", 180),
    (date(2026, 8, 10), "Test smoke detectors", 0), (date(2026, 1, 15), "Flush water heater", 0),
    (date(2026, 9, 2), "Clean dryer vent", 0), (date(2026, 4, 12), "Service lawn mower", 85),
    (date(2026, 6, 1), "Check fire extinguisher", 0), (date(2026, 7, 20), "Clean fridge coils", 0),
    (date(2026, 5, 5), "Inspect roof", 150), (date(2026, 8, 1), "Test GFCI outlets", 0),
    (date(2026, 2, 14), "Seal grout", 18), (date(2026, 7, 30), "Clean range hood filter", 0),
]
NEW = (date(2026, 9, 24), "Replace HVAC filter", 24, "MERV 11, 20x25x1")

thin = Side(style="thin", color=LINE)
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
HDR = PatternFill("solid", fgColor=TEAL)


def setup(ws, area, landscape=True):
    ws.page_setup.orientation = "landscape" if landscape else "portrait"
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = ws.page_setup.fitToHeight = 1
    ws.page_margins = PageMargins(left=0.3, right=0.3, top=0.3, bottom=0.3, header=0, footer=0)
    ws.print_area = area


def header(ws, row, heads, col0=1):
    for i, h in enumerate(heads):
        c = ws.cell(row=row, column=col0 + i, value=h)
        c.font = Font(name="Liberation Sans", size=11, bold=True, color="FFFFFF")
        c.fill = HDR
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.border = BOX
    ws.row_dimensions[row].height = 22


def build(step: int, path: Path):
    wb = Workbook()
    d = wb.active
    d.title = "Plan"
    lg = wb.create_sheet("Service Log")

    # ---- Service Log ----
    for col, w in zip("ABCD", (14, 28, 10, 26)):
        lg.column_dimensions[col].width = w
    lg["A1"] = "Service Log"
    lg["A1"].font = Font(name="Liberation Sans", size=16, bold=True, color=TEAL)
    header(lg, 3, ["Date", "Task", "Cost", "Note"])
    rows = [(a, b, c, "") for a, b, c in LOG]
    partial = [None, None, None, None]
    if step >= 1: partial[0] = NEW[0]
    if step >= 2: partial[1] = NEW[1]
    if step >= 3: partial[2], partial[3] = NEW[2], NEW[3]
    for r in range(4, 4 + len(rows) + 3):
        vals = rows[r - 4] if r - 4 < len(rows) else (partial if r - 4 == len(rows) else [None] * 4)
        for i, v in enumerate(vals, 1):
            c = lg.cell(row=r, column=i, value=v)
            c.font = Font(name="Liberation Sans", size=11, color=INK)
            c.border = BOX
            c.alignment = Alignment(horizontal="left" if i in (2, 4) else "center", vertical="center")
        lg.cell(row=r, column=1).number_format = "yyyy-mm-dd"
        lg.cell(row=r, column=3).number_format = '"$"#,##0'
        lg.row_dimensions[r].height = 19
    setup(lg, f"A1:D{4 + len(rows) + 2}", landscape=False)

    # ---- Plan (dashboard) ----
    d.sheet_view.showGridLines = False
    for col, w in zip("ABCDEFG", (26, 12, 10, 13, 13, 13, 3)):
        d.column_dimensions[col].width = w
    d.merge_cells("A1:F1")
    d["A1"] = "Home Maintenance Planner"
    d["A1"].font = Font(name="Liberation Sans", size=18, bold=True, color=TEAL)
    d["A2"] = "As of"
    d["B2"] = REPORT_DATE
    d["B2"].number_format = "yyyy-mm-dd"
    for c in ("A2", "B2"):
        d[c].font = Font(name="Liberation Sans", size=10, color=MUTED)
    first, last = 7, 7 + len(TASKS) - 1
    st = f"F{first}:F{last}"
    d["A4"], d["C4"], d["E4"] = "Overdue", "Due in 14 days", "On Schedule"
    d["A5"] = f'=COUNTIF({st},"Overdue")'
    d["C5"] = f'=COUNTIF({st},"Due Soon")'
    d["E5"] = f'=COUNTIF({st},"Scheduled")/COUNTA(A{first}:A{last})'
    d["E5"].number_format = "0%"
    for c in ("A4", "C4", "E4"):
        d[c].font = Font(name="Liberation Sans", size=10, bold=True, color=MUTED)
    for c in ("A5", "C5", "E5"):
        d[c].font = Font(name="Liberation Sans", size=22, bold=True, color=TEAL)
    for row in d["A4:F5"]:
        for c in row:
            c.fill = PatternFill("solid", fgColor=SAND)
    d.row_dimensions[5].height = 34
    header(d, 6, ["Task", "Area", "Every", "Last Done", "Next Due", "Status"])
    L, T = "'Service Log'!$A$4:$A$40", "'Service Log'!$B$4:$B$40"
    for n, (task, area, every) in enumerate(TASKS):
        r = first + n
        vals = [task, area, every, f"=SUMPRODUCT(MAX(({T}=A{r})*{L}))", f"=D{r}+C{r}",
                f'=IF(E{r}<$B$2,"Overdue",IF(E{r}-$B$2<=14,"Due Soon","Scheduled"))']
        for i, v in enumerate(vals, 1):
            c = d.cell(row=r, column=i, value=v)
            c.font = Font(name="Liberation Sans", size=11, color=INK, bold=(i == 6))
            c.border = Border(bottom=thin)
            c.alignment = Alignment(horizontal="left" if i == 1 else "center", vertical="center")
        d.cell(row=r, column=3).number_format = '0" d"'
        d.cell(row=r, column=4).number_format = "yyyy-mm-dd"
        d.cell(row=r, column=5).number_format = "yyyy-mm-dd"
        d.row_dimensions[r].height = 21
    for text, bg, fg in (("Overdue", "F6D8D3", "8E2A1F"), ("Due Soon", "FBEBC8", "7A5300"), ("Scheduled", "DCEBE7", "1F4E5A")):
        d.conditional_formatting.add(st, FormulaRule(formula=[f'F{first}="{text}"'],
                                                     fill=PatternFill("solid", fgColor=bg, bgColor=bg),
                                                     font=Font(color=fg, bold=True)))
    setup(d, f"A1:F{last}")
    wb.save(path)


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    out.mkdir(parents=True, exist_ok=True)
    for s in range(4):
        p = out / f"home_maintenance_step{s}.xlsx"
        build(s, p)
        print(p)
