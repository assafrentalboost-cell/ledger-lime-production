# Ledger & Lime - Video Upgrade Audit, Products #1-#12

**Sprint status: BLOCKED ON INPUTS (2026-09-27).** Nothing was audited, rendered, or changed on Etsy.

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
| 10 | Rental Property Spreadsheet | NOT AUDITED | pending | partial rent payment + carried-forward balance (per brief; verify in workbook) | NOT CREATED | - | NOT TOUCHED |
| 11 | - | NOT AUDITED | pending | - | NOT CREATED | - | HELD FOR EXPERIMENT |
| 12 | Estate Settlement Command Center | NOT AUDITED | pending | estate reconciliation + unresolved-item detection (per brief; verify in workbook) | NOT CREATED | - | NOT TOUCHED |

## To unblock (fastest path: #10, #12, #9 first)

1. **Workbooks.** Add each product's delivered .xlsx to the repo under `video-engine/sources/pNN-<slug>/workbook/`. For Google Sheets products, add File → Download → .xlsx copies, or before/after screenshots at the same zoom.
2. **Connectors.** Connect Etsy and Google Drive at https://claude.ai/customize/connectors, then start a new session. Connectors load when a session starts.
3. **Shop handle.** Provide the Etsy shop handle and listing IDs for #1-#12.

Once the workbooks are present, each product follows the documented flow: capture → config → one command → QA report. Live replacement then follows the sprint's baseline / rollback / readback procedure, and only for #3, #4, #6, #8, #9, #10, #12.
