# SOURCE MANIFEST — Product #9: Premium Wedding Budget & Payment System

## Source files (this folder)
- `Premium-Wedding-Budget-System.xlsx` — the real, QA'd customer workbook (sample-data-loaded), copied from `products/wedding-budget-system/release-candidate/excel-bonus/`.
- `04_vendor_payments.png` — real raw screenshot of the Vendor & Payments sheet.
- `05_cashflow_timeline.png` — real raw screenshot of the Cash-Flow Timeline sheet.
- `02_dashboard.png` — real raw screenshot of the Dashboard sheet.

## Strongest real interactive mechanism
Vendor & Payments is the single source of truth for this product: its Contracted/Paid columns drive a `SUMIF`-based Balance Remaining, which propagates into the Cash-Flow Timeline (via `SUMPRODUCT` month-matching against vendor due dates), Contributions (via `SUMIF` against a "Paid By" field), Contingency (via Master Budget's variance column), and the Dashboard — confirmed via a real Excel COM test scenario (5 vendors, 3 contributors, one over-budget category) with every result independently re-derived in Python, not trusted from the workbook's own formulas (`PRODUCT-9-BUILD-AND-QA-REPORT.md`).

## BEFORE state
A vendor row shows a Contracted amount with a partial amount already Paid, leaving a nonzero Balance Remaining reflected on the Dashboard and Cash-Flow Timeline.

## INPUT / ACTION
A new payment is entered against that vendor's Paid column (a real value, to be pulled directly from the actual sample data already in the workbook rather than invented for the video — the exact current sample figures were not re-extracted during this packaging pass; a Cloud rendering session should read them directly from the included .xlsx before finalizing the on-screen numbers).

## AUTOMATIC CHANGE
Balance Remaining decreases by the paid amount; the Cash-Flow Timeline's month-matched total and the Dashboard's aggregate figures update in the same automatic chain — this cross-sheet propagation is the product's real, QA-verified mechanism, not a claim.

## BUYER OUTCOME
A couple planning a wedding sees exactly what's been paid, what's still owed to which vendor, and how that affects their cash flow and contingency buffer — without re-adding numbers across separate sheets by hand.

## Privacy / safety note
All vendor, contributor, and guest data in the workbook is fictional sample data. No real customer, vendor, or financial-account information exists anywhere in this product.

## Sufficiency for automated rendering
PARTIALLY SUFFICIENT — honestly flagged, not overstated. The mechanism, source workbook, and 3 real raw screenshots are all real and usable. However, unlike Products #10 and #12 (where this packaging pass had exact, previously-QA-verified before/after numeric values on hand from their build reports), this manifest does NOT include a specific extracted before/after number pair for Product #9's vendor-payment scenario — the build report documents the mechanism and QA methodology thoroughly but this packaging pass did not re-open the real workbook to pull one exact current sample figure. A Cloud rendering session (or a short follow-up script) should read the actual current Vendor & Payments sample data directly from `Premium-Wedding-Budget-System.xlsx` to get the exact real before/after numbers before finalizing on-screen text, rather than the render engine or a human inventing plausible-sounding figures.
