# Product #11 — Aging Parent Financial Organizer — Source Manifest

**Purpose:** the real delivered workbook plus reference material for the offline Product #11 video replacement prep. Nothing here was rebuilt, regenerated, reconstructed or edited.

**Prepared:** 2026-09-29, local machine. Copies made with `cp -p`, which preserves bytes and timestamps.

## Workbook (the source of truth)

**Path:** `workbook/Aging-Parent-Financial-Organizer.xlsx`

**Copied from:** `products/aging-parent-financial-organizer/release/Aging-Parent-Financial-Organizer.xlsx`. That folder is local and not in the repo.

| Property | Value |
|---|---|
| Size | **223,940 bytes** |
| SHA-256 | `eaaac91d7078d09ed66363638ad0d6ba47870126d7e0117281ed6e3cc0029f23` |
| Byte check | Identical to the local release file (same SHA-256; `cmp` clean) |
| Workbook metadata | creator `openpyxl`, created 2026-09-21 04:33:50, modified 2026-09-21 04:33:52 (UTC, as stored). Read-only open; never saved. |
| Sheets (10) | Start Here · Parent & Family Setup · Bills & Recurring Payments · Expenses & Receipts · Family Contributions · Accounts & Important Documents · Subscriptions Review · Decisions & Handoff Log · Monthly Family Handoff · Dashboard |

**Why this is the real delivered Product #11 workbook** (not a draft, scratch, export or reconstruction):

1. **It matches the file Etsy delivers to buyers.** Live read-only check of listing **4579424851** (state **active**, "Aging Parent Financial Organizer | Caregiver Expense Tracker…"), done 2026-09-29 via `GET /shops/67926325/listings/4579424851/files`:
   - Etsy's buyer file `Aging-Parent-Financial-Organizer.xlsx` has **size_bytes 223940**, exactly this file.
   - The Quick Start PDF also matches: 10,889 bytes.
2. **It is the release copy.** It comes from the product's `release/` folder, the delivery folder named in `reference/listing.json` and `reference/PRODUCT-11-BUILD-AND-QA-REPORT.md`.
3. **Every other copy is byte-identical.** The local build and QA copies (`build/Aging-Parent-Financial-Organizer-v1.xlsx`, `build/_qa_scratch.xlsx`, `build/_qa_adversarial_scratch.xlsx`) all have the same SHA-256. No differing variant exists locally.
4. **The sheet architecture matches the build report.** The report describes exactly these 10 sheets, including the shortened names "Family Contributions" and "Subscriptions Review".

Etsy's API does not let a seller download the delivered file, so a byte-level hash against Etsy's copy is not possible. The match rests on the exact byte size, the filename and the local provenance above.

## Listing images: `listing-images/` (8 PNG)

Copied from the local `release/listing-images/`:
- 01-hero
- 02-family-money-system
- 03-reimbursement-engine
- 04-family-dashboard
- 05-bills-subscriptions
- 06-account-document-map
- 07-family-handoff
- 08-easy-setup

**Note:** the live Etsy listing currently has **9** images. The 9th was added after the local build (not in the build folder), so it is not included here.

## Reference: `reference/`

| File | What it is |
|---|---|
| `PRODUCT-11-BUILD-AND-QA-REPORT.md` | The original build + QA report (2026-09-21) |
| `listing.json` | Listing title / tags / description as built |
| `Aging-Parent-Financial-Organizer-Quick-Start.pdf` | Buyer PDF (10,889 bytes = Etsy's delivered PDF) |
| `listing-video.mp4` | The CURRENT video (221,549 bytes; SHA-256 `6e3846b0…3f43`), for comparison only. Live Etsy video id 843528305 (active). |

**No separate SOURCE-MANIFEST or source-screenshot set existed locally for Product #11.** This file is the first.

## Rules for the video replacement prep

- Capture only from `workbook/Aging-Parent-Financial-Organizer.xlsx`. Before/after states must be copies with the minimum real input change, recalculated by Excel.
- Do not modify this file.
- No Etsy changes · Ads OFF · Promotions OFF · Spend $0.
