"""Shared helpers for preparing capture copies of a real product workbook.

All helpers change VIEW settings only (fonts made explicit, column widths,
print areas). They never change a value, formula or number format.
"""
from __future__ import annotations

import math
from copy import copy

from PIL import ImageFont

# Metric-compatible open fonts LibreOffice uses for common Office fonts.
METRIC_FONTS = {
    "calibri": ("/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf",
                "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf"),
    "arial": ("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"),
}


def _font(name: str | None, bold: bool, size_pt: float) -> ImageFont.FreeTypeFont:
    reg, bld = METRIC_FONTS.get((name or "calibri").lower(), METRIC_FONTS["calibri"])
    return ImageFont.truetype(bld if bold else reg, round(size_pt * 96 / 72))


def explicit_default_font(wb, ws, area: str) -> None:
    """Fonts saved without a name render in the workbook default in Excel;
    LibreOffice would substitute a different face, so make it explicit."""
    default = wb._fonts[0].name or "Calibri"
    for row in ws[area]:
        for c in row:
            if c.font is not None and not c.font.name:
                f = copy(c.font)
                f.name = default
                c.font = f


def width_needed(text: str, font_name: str | None, bold: bool, size_pt: float) -> int:
    """Excel width units (~7 px of the default font at 96 dpi, +10 px padding)."""
    px = _font(font_name, bold, size_pt).getlength(str(text))
    return math.ceil((px + 10) / 7) + 1


def fit_columns(ws, rows: list[int], columns: list[str] | None = None) -> dict:
    """Widen (never narrow) columns so the text in `rows` fits inside the cell,
    the same view-only change as dragging a column edge. Returns {col: (old, new)}."""
    widened = {}
    for r in rows:
        for c in ws[r]:
            if c.value in (None, "") or (columns and c.column_letter not in columns):
                continue
            if isinstance(c.value, str) and c.value.startswith("="):
                continue
            f = c.font
            need = width_needed(c.value, f.name if f else None, bool(f and f.b), (f.sz if f and f.sz else 11))
            dim = ws.column_dimensions[c.column_letter]
            old = dim.width or 8.43
            if old < need:
                widened[c.column_letter] = (widened.get(c.column_letter, (old,))[0], need)
                dim.width = need
    return widened


def fit_column_to_text(ws, column: str, texts: list[str], font_name: str | None, size_pt: float,
                       bold: bool = False) -> tuple[float, int] | None:
    """Widen a column so given (formula-computed) display texts fit, e.g. auto warnings."""
    need = max(width_needed(t, font_name, bold, size_pt) for t in texts)
    dim = ws.column_dimensions[column]
    old = dim.width or 8.43
    if old < need:
        dim.width = need
        return (old, need)
    return None


def print_one_page(ws, area: str, landscape: bool = True, gridlines: bool = True) -> None:
    ws.print_area = area
    ws.page_setup.orientation = "landscape" if landscape else "portrait"
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1
    ws.print_options.gridLines = gridlines
