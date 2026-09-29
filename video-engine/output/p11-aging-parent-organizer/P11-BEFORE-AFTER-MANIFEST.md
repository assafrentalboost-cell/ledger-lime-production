# Product #11: Before/After Manifest (Video V1)

**Product:** Aging Parent Financial Organizer (Etsy listing 4579424851).
**Prepared:** 2026-09-29. **Status:** offline only. Nothing on Etsy was changed.

## Source of truth

| Item | Value |
|---|---|
| Workbook | `video-engine/sources/p11-aging-parent-organizer/workbook/Aging-Parent-Financial-Organizer.xlsx` (commit 09e83c4) |
| Size | 223,940 bytes, the same as Etsy's buyer file |
| SHA-256 | `eaaac91d7078d09ed66363638ad0d6ba47870126d7e0117281ed6e3cc0029f23`, re-checked before and after capture: unchanged |
| Modified? | No. Both states are copies saved under `sources/p11-aging-parent-organizer/capture/states/`. |
| Recalculation | LibreOffice headless. The delivered file stores no cached formula values: it was written by openpyxl with `fullCalcOnLoad="1"`, so Excel and Sheets recalculate it on open. |

## The two states

- **AFTER** is the delivered workbook exactly as shipped. Its LibreOffice recalculation differs from the AFTER capture in **0 cells**. The Dashboard matches the original build report exactly:
  - Monthly Bills $2,585.99
  - Expenses YTD $1,156.50
  - Pending 3
  - Contributions $790.00
  - Outstanding $124.50
  - Active Recurring 9
  - Review 3
  - Open Tasks 4
- **BEFORE** is the same workbook with **one reimbursement not yet recorded**:
  - The input cells of contribution row **C7** (Family Contributions row 10: Sep 19, 2026 · Parent Account → Michael Brooks · Reimbursement · $40.00 · Related Expense ID **E7**) are left empty. That is the workbook's own convention for an unused row.
  - The formula columns G and H of that row were not touched.
- Builder script: `sources/p11-aging-parent-organizer/capture/prepare_states.py`.

The capture copies change **view settings only**:
- Three sheets are visible.
- Print areas are set on the filmed rows.
- The default font is made explicit.
- Columns are widened just enough for headers and sample text to read in full; see `capture/states/widened-columns.json`.

## Formula chain (read from the workbook, not assumed)

1. `Family Contributions!G10` (Applied Amount, auto) = `IF(A10="",0,IF(I10="",0,F10))`. This is $40.00 once the row names Related Expense **E7**.
2. `Expenses & Receipts!M10` (Reimbursed Amount, auto) = `SUMIF('Family Contributions'!I:I, "E7", 'Family Contributions'!G:G)`.
3. `Expenses & Receipts!N10` (Remaining Reimbursement, auto) = `G10 − M10`, because Reimbursable? = Yes.
4. `Expenses & Receipts!L10` (Reimbursement Status, auto) is chosen in this order:
   - Disputed?
   - Not Reimbursable?
   - M ≤ 0.004 → "Pending"
   - N ≤ 0.004 → "Reimbursed"
   - otherwise "Partially Reimbursed"
5. The Dashboard reads these results:
   - `Dashboard!B5` Reimbursements Pending = COUNTIF(L, "Pending") + COUNTIF(L, "Partially Reimbursed").
   - `Dashboard!B7` Outstanding Reimbursement = SUMPRODUCT over rows that are Pending or Partially Reimbursed × N.
   - `Dashboard!B6` Family Contributions = SUM(Applied Amount).

None of the filmed values depend on `TODAY()`.

## Every cell that differs between BEFORE and AFTER (21 cells, complete list)

| Sheet!Cell | Before | After | Kind |
|---|---|---|---|
| Family Contributions!A10:F10, I10 | empty | C7 · Sep 19, 2026 · Parent Account · Michael Brooks · Reimbursement · $40.00 · E7 | input (the one change) |
| Family Contributions!G10 Applied Amount | $0.00 | **$40.00** | formula |
| Family Contributions!H10 Remaining Available | blank | $0.00 | formula |
| Expenses & Receipts!L10 Status (E7 Dental copay) | **Pending** | **Reimbursed** | formula |
| Expenses & Receipts!M10 Reimbursed Amount | $0.00 | **$40.00** | formula |
| Expenses & Receipts!N10 Remaining Reimbursement | **$40.00** | **$0.00** | formula |
| Dashboard!B5 Reimbursements Pending | **4** | **3** | formula |
| Dashboard!B14 Pending Reimbursements (Needs Attention) | 4 | 3 | formula (= B5) |
| Dashboard!B6 Family Contributions | $750.00 | $790.00 | formula |
| Dashboard!B7 Outstanding Reimbursement | **$164.50** | **$124.50** | formula |
| Monthly Family Handoff!B5 Outstanding Reimbursements | $164.50 | $124.50 | formula |
| Monthly Family Handoff!B7 Contributions This Month | $750.00 | $790.00 | formula |
| Dashboard!B119, B121, C144 (chart-data helper cells) | 2 / 1 / $410 | 1 / 2 / $450 | formula |

## Independent verification

- **Plain Python re-derivation** from the input cells only; no formulas were evaluated:
  - BEFORE: E7 = (Pending, $0, $40), Pending = 4, Outstanding = $164.50, Applied = $750.
  - AFTER: E7 = (Reimbursed, $40, $0), Pending = 3, Outstanding = $124.50, Applied = $790.
  - Both states **match LibreOffice exactly**.
- **Engine truth gate:** all 14 on-screen truth values (7 keys × 2 states) were checked against the recalculated cells at render time (see `VIDEO-QA-REPORT-P11.md`).

## Values shown on screen

| Scene | Truth chip / highlight | Before → After |
|---|---|---|
| 1 Dashboard (before) | rings on Reimbursements Pending and Outstanding Reimbursement | 4 · $164.50 |
| 2 Family Contributions | C7 row ring, label "Related Expense ID: E7", chip "Applied to expense" | $0.00 → $40.00 |
| 3 Expenses & Receipts | E7 row ring, label "E7 • Dental copay", chips "Reimbursement status" and "Still owed" | Pending → Reimbursed · $40.00 → $0.00 |
| 4 Dashboard (after) | chips "Reimbursements pending" and "Outstanding reimbursement" | 4 → 3 · $164.50 → $124.50 |

## Workbook defects

**None found in the filmed metrics.** Two behaviours look odd but are documented design, so the video does not rely on them:
- E3 is over-reimbursed ($60 paid on a $50 expense). It shows Remaining −$10.00 and status "Reimbursed"; the build report defines a negative remaining as a credit.
- E4 is Disputed, with $160 remaining. It is excluded from Pending and Outstanding by design.

## Privacy

- On-screen names are the workbook's fictional sample family (Sarah Chen, Michael / Rachel / Robert Brooks).
- No email column, parent profile or account data is filmed.
- An OCR privacy scan found no `@example.com` addresses and no parent name in any key frame.
