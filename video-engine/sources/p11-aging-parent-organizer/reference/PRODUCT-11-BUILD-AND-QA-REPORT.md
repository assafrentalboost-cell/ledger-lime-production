# Product #11 — Aging Parent Financial Organizer & Caregiver Reimbursement System
## Build & QA Report

**Date:** 2026-09-21. **Status:** BUILD COMPLETE. Etsy DRAFT created (listing_id `4579424851`, state `draft`). **Publication NOT performed and NOT approved.**

No separate build-brief file (`LEDGER-LIME-PRODUCT-11-AGING-PARENT-FINANCIAL-CONTROL-BUILD-BRIEF.md`) existed anywhere in this repo. Assaf was told this and also told that today's own EverBee research rated Caregiver/Aging Parent as WEAK (0/9 tested listings showed sales signal — the weakest of any candidate tested today). He explicitly chose to proceed using the pasted build-sprint spec itself as the complete, authoritative brief. See `research/evidence-summary.md` for the full honest framing.

---

## 1. Architecture

10 sheets: Start Here, Parent & Family Setup, Bills & Recurring Payments, Expenses & Receipts, Family Contributions (sheet-name shortened from the brief's "Family Contributions & Cost Sharing" — see Section 2), Accounts & Important Documents, Subscriptions Review (shortened from "Subscriptions & Money Leak Review"), Decisions & Handoff Log, Dashboard, Monthly Family Handoff.

**Core differentiator — the family reimbursement/accountability engine:** one-directional data flow, no circular references. Expenses & Receipts' `Reimbursed Amount` / `Remaining Reimbursement` / `Reimbursement Status` are formulas that READ from Family Contributions (via `SUMIF` on Related Expense ID); Family Contributions' own `Applied Amount` / `Remaining Available` never read from Expenses. This supports: one sibling paying for multiple expenses, multiple siblings sharing one expense, parent-account + sibling reimbursement combined, partial reimbursement, over-reimbursement (shown as a negative remaining = credit), disputed expenses (a manual "Flag as Disputed?" helper column, checked first in the status formula), non-reimbursable expenses, and unapplied "family pool" contributions (a Contribution row with a blank Related Expense ID).

**Worked-example verification (from the build brief itself):** $600 home repair (E1), Sarah pays in full, family agreement is Parent $300 + Michael $150 + Rachel $150, but Michael only pays $100 — the workbook correctly computes Reimbursed Amount $550, Remaining Reimbursement $50, Status "Partially Reimbursed" — i.e. **Michael owes Sarah $50**, exactly as specified. Verified via three independent methods: plain-Python re-derivation, live Excel COM recalculation, and a live edit directly against the Google Sheets master.

**Capacity (built in from day one, not retrofitted — Product #10 factory lesson):** 50 family/caregiver records, 300 bills, 1,000 expenses, 1,000 reimbursement/contribution transactions, 300 decisions, 300 account/document items. All dropdowns, formulas, summaries, and Dashboard/Handoff totals verified to reach the true capacity boundary (`qa_capacity.py`, 20/20 checks), including live far-boundary edit tests on Bills, Accounts, Decisions, and Subscriptions.

## 2. Real defects found and fixed during this build (in order found)

1. **Two sheet names exceeded Excel's hard 31-character limit** ("Family Contributions & Cost Sharing" = 35 chars, "Subscriptions & Money Leak Review" = 34 chars). openpyxl does not truncate or error — it silently writes an invalid file that real Excel could refuse to open or corrupt. Shortened to "Family Contributions" (21) and "Subscriptions Review" (20) throughout; the full descriptive names remain as in-sheet titles.
2. **Sample-data authoring mistake**: the deliberate blank/deleted-row simulation (Expense E8) had a literal `"E8"` ID instead of `None`, so it wasn't actually blank.
3. **Blank-row formula defect**: `Remaining Reimbursement` returned `""` (text) for blank rows, which threw `#VALUE!` in every downstream `SUMPRODUCT` that summed it (Dashboard/Monthly Handoff "Outstanding Reimbursement"). Fixed to return `0`.
4. **Same defect class, second column**: `Family Contributions`' `Applied Amount` had the identical `""`-for-blank-rows problem, breaking a different downstream `SUMPRODUCT`. Same fix (`0` instead of `""`).
5. **Same defect class, third column**: `Subscriptions Review`'s `Monthly Equivalent` had the identical problem, feeding into the "Potential Monthly Savings" `SUMPRODUCT`. Same fix.
6. **A genuine Excel-COM reliability finding**: `SUMPRODUCT(condition * IF(ISNUMBER(range), range, 0))` is reliable when the `ISNUMBER` guard wraps a **single cell** (used safely elsewhere in this file, matching Product #10's precedent), but **not** when it wraps an entire multi-hundred-row range as one array argument, entered as a normal (non-array-confirmed) formula via openpyxl — a genuinely non-numeric value anywhere in that range still produced `#VALUE!`, discovered via adversarial QA's "#35 text in Amount field" test. Fixed by replacing both affected formulas ("Expenses This Month" on Monthly Handoff, and the Dashboard's "Expenses by Month" chart-data table) with `SUMIFS`, which natively skips non-numeric `sum_range` cells without erroring — no array-IF trick needed at all.
7. **A Python f-string / `.replace()` construction bug**: the "Bills Due Next 30 Days" formula built its range references as bare `$K$4:$K$303` via an f-string, then tried to retrofit the sheet-name prefix with `.replace()` calls searching for a literal `{BILL_FIRST}` placeholder — but an f-string interpolates `{BILL_FIRST}` immediately (it's a real variable in scope), so every `.replace()` silently no-op'd. The formula ended up referencing the wrong sheet (itself) instead of Bills & Recurring Payments — a **silent wrong-sheet reference, not a formula error**, so it never appeared in any error scan; only caught by manually comparing the computed value (0) against a hand-count (8). Fixed by writing the sheet-qualified reference directly.
8. **A self-inflicted testing mistake that damaged the live Google Sheets master**: an earlier verification script's cleanup step called `values().clear()` on `Family Contributions!A500:J500` — the Sheets API's `clear()` removes **formulas**, not just literal input values, and that range included the formula columns G:H, wiping row 500's `Applied Amount`/`Remaining Available` formulas in the master itself (every subsequent copy inherited the gap). Found via a failing copy-test, root-caused, fixed by restoring `G4:H1003` in one batch (idempotent), and verified with a comprehensive formula-presence scan across every formula column on every sheet to confirm this was the only casualty. Both culprit scripts were fixed to only clear literal input columns going forward.
9. **A malformed-glyph visual defect**: the ✓ (U+2713) checkmark on listing image 6 ("No Password Storage Required") rendered as a broken tofu box — `arialbd.ttf` has no glyph for that character (bullet `•` and em-dash `—` elsewhere in the same file render correctly, so this was specific to that one character). Found by visually inspecting the actual rendered image, not assumed. Fixed by removing the checkmark character.
10. **A video-encoding script bug**: ffmpeg's `frame_%04d.png` glob reads sequentially until a number is *missing* — it does not stop at however many frames the current run wrote. A prior run's leftover `frame_0028+` files silently got included alongside a later run's fresher, shorter frame set, so the video's duration stayed wrong (15.5s) even after hold times were shortened to a nominal 14.0s. Fixed by wiping the frame directory before each run.
11. **Etsy API title constraint**: Etsy rejected the initial title with `too_many_invalid_characters: "& can only be used once"` — the title had two ampersands. Fixed by changing the second to "and".

## 3. QA results

- **`qa_product.py` (independent re-derivation + live Excel COM):** 60/60 PASS, including the exact worked-example numbers from the build brief.
- **`qa_adversarial.py` (bad-data injection, 35 scenarios covering brief items #11-14, #21-22, #26, #28, #32, #34/40, #35-39, #43-44 — items #1-10/15-20/23-25 are covered as passing baseline data in `qa_product.py`; #41-42 covered in the Google Sheets phase; #45 covered authoritatively in `qa_customer.py`):** 35/35 PASS. Includes a mandatory **QA scanner self-test** (deliberately inject a `#DIV/0!`, confirm detection, remove it, confirm clean) before trusting any "0 errors" result — Product #10's own factory lesson, applied from the start here rather than discovered late.
- **`qa_capacity.py`:** 20/20 PASS — declared capacities verified live (not assumed), cross-sheet dropdowns confirmed to reach the true boundary at both early and far rows, and live far-boundary edits on Bills/Accounts/Decisions/Subscriptions confirmed to flow into Dashboard/Handoff totals.
- **`qa_customer.py` (against the actual FINAL RELEASE file, not a scratch copy):** 11/11 PASS — every sheet reports `ProtectContents = True`; a real COM write test confirms an input cell accepts a write and a formula cell genuinely rejects one (not just a settings check); zero formula errors on the released file; the worked example re-confirmed correct on the exact file being shipped.
- **Total: 126/126 local Excel checks pass**, with 11 real defects found and fixed along the way (listed above).

## 4. Google Sheets

Master spreadsheet ID `1ZKqXKco1Eb9yIt30tSQYquePq848OrCJLtkuasT69v4`, created via `create_master.py` (`api/google_sheets_client.py`'s `prepare_customer_master()`, which sets `locale=en_US` as the permanent factory default per Product #10's fix). Verified via `verify_sheets_master.py` (8/8 PASS): locale is `en_US`, dates render in English month names (not the account's Hebrew default), the reapplied cross-sheet dropdowns (Paid By, Contributor, Intended For, Related Expense ID — none of which reliably survive xlsx→Sheets conversion) are present at far rows, and a real live edit against the master correctly zeroes E1's remaining balance and reverts cleanly.

Real copy test (`copy_test.py`, 7/7 PASS after the Section-2-item-8 master-damage fix): locale, protection, charts, English dates, and the reimbursement engine's live recalculation all confirmed to survive in an actual Drive copy (not just the master), with a short retry loop added after an initial run hit real calc-propagation delay immediately after the copy operation.

## 5. Quick Start PDF

6 pages (Welcome; Make a Copy + Excel option; Setup steps; Account/Document Map + Privacy warning; Dashboard/Handoff/Compatibility/Disclaimer; FAQ). Verified via PyPDF2: a real clickable link annotation (not just visible text) pointing at the exact live master's `/copy` URL, no placeholder text anywhere.

## 6. Listing images (8) and video

Per Product #10's documented privacy incident (OS-level screen capture malfunctioned and captured unrelated content on Assaf's screen), **no screen capture was attempted anywhere in this product's asset pipeline.** All 8 images (`generate_listing_images.py`) and the video are rendered from real data pulled directly from the live Google Sheets master via the API — every number traces to the real sample data (see Section 1's worked example, and the Dashboard pull: Monthly Bills $2,585.99, Expenses YTD $1,156.50, Reimbursements Pending 3, Family Contributions $790.00, Outstanding Reimbursement $124.50, Active Recurring Payments 9, Review/Cancel Candidates 3, Open Financial Tasks 4). Each image was visually inspected after rendering (see defect #9 above, found this way).

**Video** (`create_listing_video.py`, 14.0 seconds, 1920x1280, .mp4): ffmpeg was not installed system-wide, but `imageio-ffmpeg` (a Python package bundling a static ffmpeg 7.1 binary) was already available and confirmed working — no admin rights needed, unlike Product #10 where video was optional and blocked. The video's before/after reimbursement numbers were captured from an **actual edit performed against the live Google Sheets master** (Michael reimbursing Sarah $34.50 for expense E5, then reverted) — not fabricated. Sequence: Dashboard (before) → Expenses & Receipts (E5 Pending) → Family Contributions (recording the payment) → Expenses & Receipts (E5 now Reimbursed) → Dashboard (after, Reimbursements Pending 3→2) → Monthly Family Handoff → end card.

## 7. Listing metadata and cannibalization

Title (135 chars, exactly 1 ampersand — Etsy rejects a title with more than one): "Aging Parent Financial Organizer | Caregiver Expense & Reimbursement Tracker | Family Bills and Money Spreadsheet | Google Sheets Excel". Price ₪69. Taxonomy `12487` (Personal Finance Templates, matching all prior products). 13 tags, each ≤20 chars, checked programmatically against the **live, freshly-pulled** tags of all 10 existing products (130 tags total, 122 unique) — **zero overlap**.

No tax/legal/medical/benefits/fiduciary/audit-proof/court-ready claims anywhere in the description (checked against the build brief's explicit prohibition list); the required privacy warning (no passwords/PINs/SSNs/full account numbers) is present in the description, the Start Here sheet, the Accounts & Documents sheet, and the Quick Start PDF.

## 8. Etsy draft creation and fresh verification

Created via `create_etsy_draft.py` (direct API calls, no interactive confirmation prompt — matching this project's standing "draft creation never requires approval" rule). **listing_id `4579424851`, state `draft`.**

Two real API findings worth keeping for future products:
- **Images use the bare `/listings/{id}/images` path**; files use the **shop-scoped** `/shops/{shop_id}/listings/{id}/files` path (the opposite convention for each) — confirmed by testing both.
- **Etsy rejects a title containing more than one `&`** (`too_many_invalid_characters`) — not previously documented in this project.
- **Video upload requires an explicit `name` field** in the multipart data (`{"name": filename}`) — a bare `files={"video": f}` returns `400: A valid name must be provided`.

Fresh, independent GET verification (not trusted from any creation response): `state=draft`, price ₪69.00, title/13 tags/taxonomy exact, 2 files present (via the shop-scoped path), 8 images present at ranks 1-8 with no gaps or duplicates (rank 1 = the hero, first uploaded), 1 video present. `type`/`is_digital` read back as `None` on GET — confirmed this is a pre-existing API quirk, not a Product #11-specific defect, by checking the same fields on the already-live Product #10 listing, which shows the identical `None`.

**Products #1-10 safety check:** fresh GET on all 10, prices confirmed unchanged and matching known values (₪69/39/24/64/34/39/49/29/95/59). **One change found, not made by this session: listing `4579173470` (Product #10, Rental Property Spreadsheet) is now `state=active`**, having been `draft` as of the last check earlier in this conversation. This is consistent with Assaf's own final-audit result (GO-LIVE READY: YES) and appears to be his own subsequent action outside this build session — it is flagged here for the record, not treated as an error, and this session made no change to it (its price, title, and tags are all unchanged from the known-good values).

## 9. Publication status (superseded — see Section 10)

Publication was NOT performed as of the initial build. Product #11 existed only as an Etsy draft at that point. See Section 10 for the final fix + publish pass that followed.

## 10. FINAL FIX + PUBLISH PASS (2026-09-21)

Assaf requested a "PRODUCT #11 — FINAL FIX + PUBLISH PASS" covering two confirmed visual defects found by direct inspection after the initial build, plus a pipeline-hygiene cleanup, and gave explicit, scoped publication approval conditional on all fixes passing ("Assaf has now explicitly approved publication of Product #11 after the targeted fixes above PASS... Publish / activate ONLY listing: 4579424851").

**Task 1 — Quick Start PDF, 2 real defects fixed:**
- **Defect A (HTML-entity bug):** page 1's "What You Received" card was drawn via `canvas.drawString` (which never interprets markup) but contained the literal source string `"&amp;"` — a copy-paste artifact from the `Paragraph`-based text elsewhere in the same file (which *does* need `&amp;`, since it uses reportlab's XML-like mini-markup). Fixed by using a plain `&` in the `drawString` line. Verified via PyPDF2 text extraction across all 6 pages: zero occurrences of literal `&amp;` remain.
- **Defect B (page 4 privacy header):** this was actually two separate bugs presenting as one visual defect. (1) The header used `⚠` (U+2713... actually U+26A0 WARNING SIGN), which the standard PDF "Helvetica-Bold" font (WinAnsi encoding) does not support — removed per Assaf's preferred plain-text approach: `"Privacy — Do NOT store in this spreadsheet:"`. (2) Independently of the glyph, the paragraph-body y-position formula (`y - 0.6*inch - h + 0.35*inch`) placed the body text's *top* edge almost exactly at the header's own top edge — a real off-by-`0.35*inch` layout bug, not merely a symptom of the missing glyph. Removing only the glyph would NOT have fixed the collision. Fixed by removing the erroneous `+ 0.35 * inch` term. Verified by rendering the actual PDF page to an image (via PyMuPDF) and visually inspecting it — the header and body now have clean, non-overlapping spacing.
- Re-verified after both fixes: all 6 pages render, zero literal `&amp;` anywhere, no placeholder text, and the Make-a-Copy link retains its real clickable `/URI` annotation pointing at the correct, current master (`.../d/1ZKqXKco1Eb9yIt30tSQYquePq848OrCJLtkuasT69v4/copy`).

**Task 2 — asset naming cleanup:** the 8 listing images (content unchanged, byte-identical, confirmed by file size) were renamed from leftover Product #10-style names to Product #11-accurate ones: `02-family-money-system.png`, `03-reimbursement-engine.png`, `04-family-dashboard.png`, `06-account-document-map.png`, `07-family-handoff.png` (`01-hero.png`, `05-bills-subscriptions.png`, `08-easy-setup.png` were already correctly named). `listing.json`'s `image_paths` updated to match. `build/generate_listing_images.py`'s own output filenames were also updated (same rename, not a content change) so a future regeneration doesn't reintroduce the stale names.

**Task 3 — final regression, no rebuild:** `qa_product.py` 60/60, `qa_adversarial.py` 35/35, `qa_customer.py` 11/11 (against the actual release `.xlsx`, real COM protection write-test) — **106/106, zero regressions** from the PDF/filename-only changes above. Google Sheets master re-verified (`verify_sheets_master.py`, 8/8): locale still `en_US`, English dates, live edit test correct. Fresh real copy test (`copy_test.py`, 7/7): locale/protection/charts/dates/reimbursement-engine all survive in a real Drive copy; temp copy deleted after. Listing video re-verified by extracting and visually inspecting 4 actual frames (0.5s, 5s, 9s, 13.5s) via ffmpeg — real Dashboard "before" numbers, the real Michael→Sarah $34.50 reimbursement entry, a mathematically consistent Dashboard "after" ($124.50 − $34.50 = $90.00 exactly, Reimbursements Pending 3→2), and a clean end card — no screen-capture artifacts or unrelated content anywhere in the video.

**Task 4 — draft updated in place (no second listing created):** the stale PDF (`listing_file_id 1516579592106`, the buggy 10.77 KB version) was deleted from draft `4579424851` via the shop-scoped files endpoint, and the corrected PDF was uploaded in its place (`listing_file_id 1517828320285`, 10.63 KB). Images were NOT re-uploaded — Etsy's stored image bytes are independent of local filenames, so the local rename in Task 2 required no Etsy-side change; verified the 8 already-uploaded images remain correct at ranks 1-8. Fresh GET confirmed: state=draft, price ₪69, title/description/13 tags/taxonomy exact, exactly 2 files (corrected PDF + unchanged Excel), 8 images ranks 1-8 no gaps/duplicates, 1 video.

**Task 5 — pre-publish safety check:** fresh GET on all of Products #1-10: all `state=active`, all prices exactly matching known-good values (₪69/39/24/64/34/39/49/29/95/59). Product #10 confirmed stable at `active`/₪59 (Assaf's own prior action, untouched by this session). Product #11 reconfirmed `state=draft` immediately before Task 6. Ads: not independently verifiable via API (standing project finding — Etsy exposes no promotions/Ads resource); no evidence of any spend.

**Task 6 — PUBLISHED.** All Task 1-5 checks genuinely passed with no unresolved defect. Per Assaf's explicit, scoped approval, `PATCH /shops/67926325/listings/4579424851` set `state: "active"`. API response confirmed `state: active`, `state_timestamp: 1789971740`.

**Task 7 — post-publish verification, fresh and independent (separate GET calls, not trusted from the PATCH response):** `state=active`, price ₪69.00, title exact, 13 tags, 8 images at ranks 1-8, 1 video, 2 files (corrected PDF + Excel), public URL `https://www.etsy.com/listing/4579424851/aging-parent-financial-organizer` (this session cannot independently browser-verify the URL resolves publicly — no general web-browsing access in this environment — so that specific claim is reported as unverified-by-this-session, not confirmed). Products #1-10 re-verified unchanged a second time, post-publish: zero cross-contamination.

**FINAL REPORT:**
```
PDF FIX: PASS
ASSET NAMING CLEANUP: PASS
EXCEL FINAL: PASS
GOOGLE SHEETS FINAL: PASS
COPY TEST: PASS
VIDEO FINAL: PASS
ETSY DRAFT UPDATE: PASS
PRODUCT #11 PUBLISHED: YES
LIVE STATE: ACTIVE
LIVE PRICE: ₪69 CONFIRMED
8 IMAGES: PASS
VIDEO: PASS
2 DIGITAL FILES: PASS
PRODUCTS #1-10 UNCHANGED: PASS
ADS: OFF (unverifiable via API; no evidence of activation or spend)
BLOCKERS: none
```

**Product #11 is now live: listing `4579424851`, https://www.etsy.com/listing/4579424851/aging-parent-financial-organizer, ₪69.** This is Ledger & Lime's second published product from today's build thread (after Product #10), and — per the standing research caveat carried since the initial build — the underlying commercial evidence for the Aging Parent/Caregiver niche remains the weakest of any candidate tested in today's research (0/9 listings showed a sales signal in the original EverBee sprint). The build/QA quality is not in question; the commercial outcome is unproven and should be watched the same way Product #10's Day-0 baseline was.
