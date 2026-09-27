# SOURCE MANIFEST — Product #10: Rental Property Spreadsheet

## Source files (this folder)
- `Rental-Property-Spreadsheet.xlsx` — the real, QA'd customer workbook (sample-data-loaded), copied from `products/rental-property-spreadsheet/release/`.
- `03-partial-payments-carried-balances.png` — real, data-driven listing image already showing the mechanism below.
- `04-portfolio-dashboard.png` — real, data-driven listing image of the portfolio dashboard.

## Strongest real interactive mechanism
Partial rent payment + carried-forward balance tracking on the Rent Tracker sheet. This is the product's documented core differentiator (per `PRODUCT-10-BUILD-AND-QA-REPORT.md`, Section 3), independently re-derived in Python and confirmed via a real Excel COM recalculation and a real Google Sheets live-edit test — not a decorative feature.

## BEFORE state
A tenant row shows: Total Due $1,000, Paid $600, Remaining Balance $400, Status "Partial."

## INPUT / ACTION
The next month's row for the same unit: new Base Rent Due $1,000, Prior Balance pulls forward the $400 owed automatically (a direct cell reference to the prior row's Remaining Balance, not a manual re-entry) — Total Due becomes $1,400.

## AUTOMATIC CHANGE
Total Due updates to $1,400 the moment the prior row's balance is set — no manual copying of the carried amount. This exact scenario ($1,000 due/$600 paid → $400 remaining/Partial → next row $1,000 + $400 carried = $1,400 total) is the literal test case used in this product's own real Google Sheets live-edit QA test (Section titled "Excel Customer QA" / live-edit test, `PRODUCT-10-BUILD-AND-QA-REPORT.md`).

## BUYER OUTCOME
A landlord never has to manually track who still owes what from a prior month — the workbook carries it forward and totals it automatically, every month, without the buyer doing arithmetic.

## Privacy / safety note
All tenant names and unit data in the workbook are fictional sample data (e.g. "John Smith," "Marcus Webb" — established placeholder names used throughout this product's own build/QA process). No real customer or tenant data exists anywhere in this product.

## Sufficiency for automated rendering
SUFFICIENT for a Cloud session to render via the existing `video-engine/render.py` engine using the data-driven-rendering approach already proven for Products #11/#13 (pull real values via openpyxl/Excel COM or the Sheets API and render clean KPI cards/highlighted cells — this project has no safe literal screen-recording-with-cursor method, documented repeatedly in this project's history). The 2 included listing images already demonstrate the mechanism visually and can serve as direct visual reference for scene composition. NOT sufficient if literal OS-level screen capture is expected — that method is explicitly avoided in this project after a real privacy incident during this product's own build (an OS-level capture attempt captured unrelated content actually on the user's screen).
