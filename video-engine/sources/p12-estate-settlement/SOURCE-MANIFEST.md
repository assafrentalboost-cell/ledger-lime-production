# SOURCE MANIFEST — Product #12: Estate Settlement Command Center

## Source files (this folder)
- `Estate-Settlement-Command-Center.xlsx` — the real, QA'd customer workbook (sample-data-loaded), copied from `products/estate-settlement-command-center/release/`.
- `Estate-Settlement-Command-Center-SAMPLE-v1.xlsx` — the build-stage sample workbook (byte-identical content to the release copy at time of packaging; kept as a build-traceable alternate).
- `03-cause-and-effect.png`, `04-reconciliation.png`, `07-closeout-review.png` — real, data-driven listing images already showing the mechanism below (note: image 07 has a disclosed, still-open minor cosmetic text clip on the disclaimer line per `PRODUCT-12-FINAL-CLOSURE-REPORT.md` at time of that report; verify current state before using as a final asset).

## Strongest real interactive mechanism
The connected Reconciliation + Closeout Review engine: `10_RECONCILIATION` computes `Expected Ending Cash = Starting Estate Cash + Recorded Inflows − Recorded Outflows` and compares it to a user-entered `Actual Estate Cash Balance`; `11_CLOSEOUT_REVIEW` rolls up every register's unresolved-item flags (including the Liability Register) into one of `SET UP ESTATE` / `NOT READY` / `REVIEW` / `ORGANIZATION COMPLETE`. Both are independently re-derived in Python and cross-checked against live Excel COM computation — not decorative. A real design defect (Closeout status precedence was originally backwards — any open, non-overdue task forced the harshest `NOT READY` status) was found and fixed during this product's own QA, not merely disclosed after shipping.

## BEFORE state
Reconciliation shows Expected Ending Cash $37,490.00 vs. Actual Estate Cash Balance $9,430.00 — a −$28,060.00 difference (an intentional mismatch built into the sample data specifically to demonstrate the "Review Needed" status). Separately, the Liability Register's "Unpaid Verified / Disputed Liabilities" count sits at 5.

## INPUT / ACTION
A new liability row is added: ID `L-DEMO`, amount $8,500, status "Verified, Unpaid."

## AUTOMATIC CHANGE
The Liability Register's Unpaid Verified/Disputed count updates from 5 → 6 automatically, and the Closeout Review's own rollup reflects the new unresolved item — confirmed as a real, independently-verified KPI change during this product's own build QA (`PRODUCT-12-BUILD-AND-QA-REPORT.md`: "a real liability write, a real KPI count change (5→6, independently confirmed), a real Closeout Review capture reflecting the change — not staged or fabricated").

## BUYER OUTCOME
An executor sees, at a glance, exactly which money records don't yet add up and which tasks/liabilities/documents still need attention — without manually cross-checking every register by hand.

## Privacy / safety note
All estate, asset, liability, and beneficiary data in the workbook is fictional sample data. The product is explicitly organizational-only: it never determines probate requirements, creditor priority, legal beneficiary entitlement, or tax outcomes, and its status labels never imply "safe to distribute" or "legally ready" — this boundary is enforced in the workbook's own language, not just in marketing copy.

## Sufficiency for automated rendering
SUFFICIENT for a Cloud session to render via the existing data-driven-rendering approach (same method proven for Products #10/#11/#13). The 3 included listing images already show real visual treatments of this exact mechanism and can guide scene composition directly. Flag: re-verify image 07's disclosed cosmetic clip is still present or was since fixed before treating it as final-quality source material — the manifest author did not re-run that specific visual check during this packaging pass.
