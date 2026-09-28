# Ledger & Lime - Video Upgrade Audit, Products #1-#12

**Sprint status (2026-09-27): IN PROGRESS.** Source packages for #9, #10 and #12 arrived in commit 65cd4c6. #10 (V1.1) and #12 (V1) are done offline. #9 is not started (per instruction). Etsy has not been touched.

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
| 9 | Premium Wedding Budget & Payment System | NOT AUDITED | pending | to be found in workbook | NOT CREATED | - | NOT TOUCHED |
| 10 | Rental Property Spreadsheet | NOT AUDITED (no Etsy access) | ADD / REPLACE (offline file ready) | Partial rent payment → remaining balance → carried into the next month (verified in the workbook formulas and sample data) | CREATED: V1.1 `video-engine/output/p10-rental-property/P10-Rental-Property-Etsy-Video-V1.1.mp4` (V1 kept) | PASS (108/0/0) | NOT TOUCHED |
| 11 | - | NOT AUDITED | pending | - | NOT CREATED | - | HELD FOR EXPERIMENT |
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
