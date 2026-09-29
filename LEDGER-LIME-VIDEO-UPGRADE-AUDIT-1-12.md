# Ledger & Lime - Video Upgrade Audit, Products #1-#12

**Sprint status (2026-09-27): IN PROGRESS.** Source packages for #9, #10 and #12 arrived in commit 65cd4c6. #10 (V1.1), #12 (V1) and #9 (V1) are done offline. Etsy has not been touched.

Benchmark: Product #13 Video V3.3 FINAL (`video-engine/output/p13-iep-tracker/`). Engine: Ledger & Lime Automated Etsy Video Engine V1, unchanged in this sprint.

## Why the audit could not run

| Input needed | Status in this cloud session |
|---|---|
| Product #1-#12 build / QA docs | Not present. The repository contains only the video engine and Product #13. |
| Product #1-#12 workbooks (.xlsx / Google Sheets) | Not present. The engine requires a real workbook, or real captures of it, to show real product behaviour. |
| Current Etsy listings + videos (read) | No Etsy connector. EverBee Research is read-only market data: it has no Ledger & Lime shop match under "Ledger" names and exposes no listing videos. |
| Etsy video replacement (write) | No Etsy connector. No live change is possible from this session. |
| Live Ledger & Lime Master (Google Drive) | No Google Drive connector. |

Reconstructing #1-#12 workbooks from product names was rejected. It would show product behaviour that has not been verified against the real files, which breaks the sprint's "real product behavior / no fake functionality" rule. #9 in particular must use the mechanism found in its actual workbook.

## Title-experiment protection (until the Day-7 checkpoint on 2026-10-04)

#1, #2, #5, #7, #11: **HELD FOR EXPERIMENT**. These are offline-only even once inputs arrive.

## Per-product record

| # | Product | Current video | Action | Core mechanism | New video | QA | Etsy |
|---|---|---|---|---|---|---|---|
| 1 | - | NOT AUDITED | pending | - | NOT CREATED | - | HELD FOR EXPERIMENT |
| 2 | - | NOT AUDITED | pending | - | NOT CREATED | - | HELD FOR EXPERIMENT |
| 3 | Simple Budget Spreadsheet | NOT AUDITED | pending | - | NOT CREATED | - | NOT TOUCHED |
| 4 | Biweekly Paycheck / Between Paydays | NOT AUDITED | pending | - | NOT CREATED | - | NOT TOUCHED |
| 5 | - | NOT AUDITED | pending | - | NOT CREATED | - | HELD FOR EXPERIMENT |
| 6 | ADHD-Friendly Budget Spreadsheet | NOT AUDITED | pending | - | NOT CREATED | - | NOT TOUCHED |
| 7 | - | NOT AUDITED | pending | - | NOT CREATED | - | HELD FOR EXPERIMENT |
| 8 | Mortgage Payoff Tracker | NOT AUDITED | pending | - | NOT CREATED | - | NOT TOUCHED |
| 9 | Premium Wedding Budget & Payment System | NOT AUDITED (no Etsy access) | ADD / REPLACE (offline file ready) | Vendor payment logged → Balance Remaining + auto Status update → Dashboard Total Paid / Overdue update (verified in workbook formulas) | CREATED: `video-engine/output/p09-wedding-budget/P09-Wedding-Budget-Etsy-Video-V1.mp4` | PASS (107/0/0) | NOT TOUCHED |
| 10 | Rental Property Spreadsheet | NOT AUDITED (no Etsy access) | ADD / REPLACE (offline file ready) | Partial rent payment → remaining balance → carried into the next month (verified in the workbook formulas and sample data) | CREATED: V1.1 `video-engine/output/p10-rental-property/P10-Rental-Property-Etsy-Video-V1.1.mp4` (V1 kept) | PASS (108/0/0) | NOT TOUCHED |
| 11 | Aging Parent Financial Organizer | AUDITED vs package copy of live video 843528305 (3:2 rendered slides, not workbook UI) | REPLACE WITH NEW after the 2026-10-04 checkpoint (offline file ready) | Reimbursement recorded (C7 → E7) → Applied Amount → E7 Pending → Reimbursed, $40 → $0 → Dashboard Pending 4 → 3, Outstanding $164.50 → $124.50 (verified in workbook formulas) | CREATED: `video-engine/output/p11-aging-parent-organizer/P11-Aging-Parent-Organizer-Etsy-Video-V1.mp4` | PASS (118/0/0) | HELD FOR EXPERIMENT (to 2026-10-04) - NOT TOUCHED |
| 12 | Estate Settlement Command Center | NOT AUDITED (no Etsy access) | ADD / REPLACE (offline file ready) | Liability marked Paid → auto-warning clears → Command Center "Unpaid / Disputed Liabilities" 4 → 3 (verified in workbook formulas) | CREATED: `video-engine/output/p12-estate-settlement/P12-Estate-Settlement-Etsy-Video-V1.mp4` | PASS (102/0/0) | NOT TOUCHED |

## To unblock (fastest path: #10, #12, #9 first)

1. **Workbooks.** Add each product's delivered .xlsx to the repo under `video-engine/sources/pNN-<slug>/workbook/`. For Google Sheets products, add File → Download → .xlsx copies, or before/after screenshots at the same zoom.
2. **Connectors.** Connect Etsy and Google Drive at https://claude.ai/customize/connectors, then start a new session. Connectors load when a session starts.
3. **Shop handle.** Provide the Etsy shop handle and listing IDs for #1-#12.

Once the workbooks are present, each product follows the documented flow: capture → config → one command → QA report. Live replacement then follows the sprint's baseline / rollback / readback procedure, and only for #3, #4, #6, #8, #9, #10, #12.

## Product #10 - details (2026-09-27)

**Source.** The packaged workbook `video-engine/sources/p10-rental-property/Rental-Property-Spreadsheet.xlsx` (commit 65cd4c6), recalculated by LibreOffice.
- AFTER is the workbook exactly as shipped: 0 differing cells against the packaged workbook's own recalculation.
- BEFORE is the same workbook with one input cleared: Rent Tracker H5/I5, the May 2026 Payment 1 for unit P1-U1 (tenant T1).
- Builder: `sources/p10-rental-property/capture/prepare_states.py`.

**Values, all verified cell-by-cell and shown in the video.**

| Cell | Meaning | Before | After |
|---|---|---|---|
| N5 | May paid | $0.00 | $1,000.00 (input, May 4, 2026) |
| O5 | May remaining balance | $1,500.00 | $500.00 |
| P5 | May status | Unpaid | Partial |
| F6 | June Prior Balance (carried) | $1,500.00 | $500.00 |
| G6 | June Total Due | $3,000.00 | $2,000.00 |

The manifest's "$1,000 due / $600 paid" example is a QA test case and is not in the packaged sample data, so it is not used. The packaged listing image `03-partial-payments-carried-balances.png` matches the workbook's P1-U1 rows exactly.

**Product finding - Dashboard "Outstanding Rent" overstates what is owed.** The dashboard's outstanding figure was deliberately left out of the video because of this.
- Dashboard B7 = Rent Tracker B339 = `SUMPRODUCT((P<>"Vacant")*(O>0)*O)` over all rows.
- Each month's Remaining Balance already includes the balance carried from earlier months, so one unpaid amount is counted again in every later month.
- In the packaged sample, B7 shows **$4,300**. The latest month per unit sums to **$100** actually owed: P2-U2 owes $100 and P1-U1 holds a $400 credit.
- The dashboard does recalculate on input (B7 $8,000 → $4,300; B15 "Overdue/Partial" 8 → 6, a row count with the same issue).
- Showing it would present an inflated "who still owes" number to buyers. Recommend fixing the formula to the latest row per unit, then adding a dashboard beat.

**Other polish finding.** Several Rent Tracker headers are clipped at the shipped column widths ("Remaining Balan…", "Payment Statu…", "Payment 1 Dat…"). The video shows them faithfully.

### Product #10 V1.1 - framing / readability only (2026-09-27)

- **Headers in full.** The shipped column widths clip 10 of 17 Rent Tracker headers, so the camera alone could not reveal them. The V1.1 capture copies widen only those columns, just enough to fit the header text (B, E, F, H-M, O, P). This is a view-only change, like dragging a column edge; see `capture/states/widened-columns.json`. Values were re-verified: 0 differing cells against the packaged workbook.
- **Header row never touches the card edge.** V1's downward camera drift clipped the header row (5.70 s on the phone sheet). V1.1 keeps white margin above and below via a 4-sided `canvas_pad`. New `must_show` validation proves each scene's header + rows stay fully in frame for the whole camera move.
- **Right edge.** The balance scenes now end with white margin past the table's right edge instead of cutting flush.
- **Total Paid column.** Dropped from the two balance scenes to keep numbers at V1 size on phones. Keeping it would shrink them about 25%.
- **Unchanged.** Story, timing, captions, verified values, highlight cells (rings inset a few px), chips and end card.

## Product #12 - details (2026-09-28)

**Source.** The packaged workbook `video-engine/sources/p12-estate-settlement/Estate-Settlement-Command-Center.xlsx` (commit 65cd4c6; byte-identical to the SAMPLE-v1 copy), recalculated by LibreOffice.
- AFTER is the workbook exactly as shipped: 0 differing cells.
- BEFORE is the same workbook with one liability record not yet updated. Liability L3 (Lakeside Funeral Home, $8,900 verified) is set back to the sample's own unpaid convention (Status "Verified, Unpaid", Amount Paid 0, Payment Date blank).
- Builder: `sources/p12-estate-settlement/capture/prepare_states.py`.

**Mechanism.**
- Register K: `⚠ unpaid verified balance` while the Status is "Verified, Unpaid" and verified > paid.
- Closeout Review B7 = unpaid-verified + disputed count.
- Command Center B17 "Unpaid / Disputed Liabilities" mirrors B7.
- The closeout status (B12) stays REVIEW because other items remain open. That is what the "still needs attention" beat shows.

**Values, all verified cell-by-cell.**

| Cell | Before | After |
|---|---|---|
| 04 H6 L3 Status | Verified, Unpaid | Paid |
| 04 I6 L3 Amount Paid | $0.00 | $8,900.00 |
| 04 J6 L3 Payment Date | (blank) | Jul 16, 2026 |
| 04 K6 L3 Warning | ⚠ unpaid verified balance | (clear) |
| 01 B17 Unpaid / Disputed Liabilities | 4 | 3 |
| 01 B12 Closeout Status | REVIEW | REVIEW |

**Manifest discrepancies.**
- SOURCE-MANIFEST says the count "sits at 5" and cites an L-DEMO add taking it 5 → 6. The shipped workbook computes **3**.
- Adding a liability moves the count the wrong way for the buyer outcome ("fewer unresolved"), so the video uses the real resolving action already present in the sample data. The L-DEMO story is not used.

**Privacy.** No creditor or person names appear in any crop. The register crops show only the Status, Amount Paid, Payment Date and Warning columns; the one on-screen label is the business name "Lakeside Funeral Home". No legal / probate / tax claims appear.

## Product #9 - details (2026-09-28)

**Source.** The packaged workbook `video-engine/sources/p09-wedding-budget/Premium-Wedding-Budget-System.xlsx` (commit 65cd4c6), recalculated by LibreOffice on 2026-09-28.
- The SOURCE-MANIFEST states it has no extracted before/after numbers, so every value below was derived from the workbook.
- AFTER is the workbook exactly as shipped: 0 differing cells.
- BEFORE is the same workbook with one vendor's final payment not yet logged. For Tasty Catering Co, Total Paid To Date is set to its $1,000 deposit. That is the sample's own convention: every other vendor with an open balance has paid exactly its deposit.
- Builder: `sources/p09-wedding-budget/capture/prepare_states.py`.

**Mechanism.**
- Vendor & Payments: F = MAX(Contracted − Paid, 0).
- I = PAID IN FULL / OVERDUE / DUE SOON / UPCOMING, comparing the due date with Settings!B7 = TODAY().
- Dashboard: Total Paid comes from Master Budget (SUMIF of vendor paid); Overdue Count / Amount are COUNTIF / SUMIF on Status.
- The same single input also updates the Cash-Flow Timeline, Contributions and Master Budget (36 cells in all).

**Values, all verified cell-by-cell.**

| Cell | Before | After |
|---|---|---|
| V&P E5 Catering Total Paid To Date | $1,000.00 | $8,500.00 (input) |
| V&P F5 Balance Remaining | $7,500.00 | $0.00 |
| V&P I5 Status | OVERDUE | PAID IN FULL |
| Dashboard B6 Total Paid | $3,800.00 | $11,300.00 |
| Dashboard B7 Total Remaining | $29,700.00 | $22,200.00 |
| Dashboard B11 Overdue Payments — Count | 3 | 2 |
| Dashboard B12 Overdue Payments — Amount | $11,500.00 | $4,000.00 |

**Date dependence.** OVERDUE depends on the capture date (catering was due Aug 15, 2026). Both states were captured on 2026-09-28. A re-render after Nov 13, 2026 would also turn the Venue row OVERDUE, so re-verify numbers if this video is re-rendered later.

**Privacy.** Payers appear only as "Partner 1 / Partner 2 / Family". Vendors are fictional businesses.

## Product #11 - details (2026-09-29, resumed)

**Source.** The delivered workbook in `video-engine/sources/p11-aging-parent-organizer/workbook/`, added in commit 09e83c4. Its SHA-256 `eaaac91d…9f23` and size of 223,940 bytes were verified and are unchanged after capture.
- AFTER is the workbook exactly as shipped: 0 differing cells, and the Dashboard matches the build report.
- BEFORE is the same workbook with one reimbursement row (C7: Parent Account → $40 for expense E7, Dental copay) not yet recorded.
- Builder: `sources/p11-aging-parent-organizer/capture/prepare_states.py`.
- Full cell list, formula chain and independent Python re-derivation: `video-engine/output/p11-aging-parent-organizer/P11-BEFORE-AFTER-MANIFEST.md`.

**Values.**

| Cell | Before | After |
|---|---|---|
| Family Contributions G10 Applied Amount | $0.00 | $40.00 |
| Expenses L10 Status (E7) | Pending | Reimbursed |
| Expenses N10 Remaining (E7) | $40.00 | $0.00 |
| Dashboard B5 Reimbursements Pending | 4 | 3 |
| Dashboard B7 Outstanding Reimbursement | $164.50 | $124.50 |

**Current live video.** The package copy is 1920x1280, 24 fps, 14 s: slides rendered from Sheets API values, not the workbook UI.
- Its numbers are true: the E5 $34.50 edit reproduces Pending 3 → 2 and $124.50 → $90.00.
- But its end state is a demo edit that is not in the delivered file.
- Its table text is about 3.7 px on a phone.

**Recommendation.** REPLACE WITH NEW, after the 2026-10-04 checkpoint only. See `video-engine/output/p11-aging-parent-organizer/P11-VIDEO-RECOMMENDATION.md`.

**Workbook defects.** None found in the filmed metrics.

**Privacy.** Only the workbook's fictional sample family appears. No emails or parent profile are shown.

### Earlier status: Product #11 - blocked (2026-09-29)

This was a replacement-video prep request, offline only; Product #11 is held for the title experiment until 2026-10-04. It stopped before any rendering because the source of truth is missing. The repository has no Product #11 workbook or package on any branch; `video-engine/sources/` holds only p09, p10, p12, p13 and a dummy. The live Master is also unreachable: there is no Google Drive connector in this session.

Needed inputs:
- `video-engine/sources/p11-aging-parent-organizer/` containing the delivered customer workbook (.xlsx).
- A SOURCE-MANIFEST.md, same format as #9 / #10 / #12.
- Any existing listing images.

Nothing was created and Etsy was not touched.
