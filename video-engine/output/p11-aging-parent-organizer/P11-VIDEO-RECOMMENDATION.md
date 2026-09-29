# Product #11: Video Recommendation for the 2026-10-04 Checkpoint

**Recommendation: REPLACE WITH NEW, but only after the 2026-10-04 title-experiment checkpoint has been read and recorded.** Until then the new file stays **OFFLINE ONLY**.

Nothing on Etsy was changed in this session: title, tags, price, hero, description, images, files and video are all untouched. Ads are OFF, promotions are OFF, and spend is $0.

## Candidate

| | |
|---|---|
| File | `video-engine/output/p11-aging-parent-organizer/P11-Aging-Parent-Organizer-Etsy-Video-V1.mp4` |
| SHA-256 | `b4c3cac2583e87e56b65bef23f503cd837e0b4745fa5f5d9f40aa9504992e161` (4,863,177 bytes) |
| Specs | 1920x1080, 15.00 s, H.264 High 4.1, yuv420p, BT.709, 30 fps, no audio, +faststart, ~4.9 MB |
| QA | **PASS**: 118 pass / 0 warn / 0 fail (`VIDEO-QA-REPORT-P11.md`) |
| Values | before/after verified cell by cell against the delivered workbook (`P11-BEFORE-AFTER-MANIFEST.md`) |

## Side-by-side

| | Current live video (id 843528305) | New V1 |
|---|---|---|
| What is on screen | Slides rendered from values pulled through the Sheets API: stylised HTML-like tables and number tiles, **not the workbook's own UI** | **The real delivered workbook's own sheets**: real headers, formats and conditional fills, recalculated by LibreOffice |
| Story | Dashboard → E5 Pending → Michael pays $34.50 → E5 Reimbursed → Dashboard 3→2, $124.50→$90.00 → Handoff | Dashboard (4 pending, $164.50) → record reimbursement C7 → E7 Pending→Reimbursed, $40→$0 → Dashboard 4→3, $164.50→$124.50 |
| Value truth | True. I re-ran its edit on a scratch copy and got E5 Reimbursed, Pending 3→2, Outstanding $124.50→$90.00. But its "after" state is a **demo edit that is not in the delivered file**. | AFTER **is** the delivered file (0 differing cells), so a buyer opening the download sees exactly the end state shown |
| Mechanism shown | Result only: two separate tables, no visible link between payment and expense | The full chain: Related Expense ID → Applied Amount (auto) → Reimbursed / Remaining / Status (auto) → Dashboard |
| Frame | 1920x1280 (3:2), 24 fps, no colour tags, 127 kb/s | 1920x1080 (16:9), 30 fps, BT.709 tagged |
| Phone legibility (390 px) | Table text ≈ 18 px at 1920 wide, so ≈ 3.7 px on a phone: unreadable. Key change only in small green footnote text. | Captions 15.8 px; value chips 12.2 px (e.g. "4 → 3", "$164.50 → $124.50") |
| Space use | Table slides are ~80 % empty card (one row per table) | Real tables fill the card; chips sit in the free area |
| Timing | 14.0 s, holds only (no highlights) | 15.0 s, highlight ring + chips per scene, hard cuts, no blank flash, no ghosting |

**Verdict: materially better.** The two videos tell the same buyer story (a family member gets paid back and the dashboard updates). The new one shows it in the actual product, with values a buyer can reproduce from the file they download, and it is readable on a phone.

## Why wait until after 2026-10-04

Product #11 is inside the title experiment (#1, #2, #5, #7, #11). Changing the video before the checkpoint would add a second variable to the experiment readout.

## Replacement procedure (after the checkpoint, and only with a fresh go-ahead)

1. **Record a baseline.** Read the listing with GET and save the current video id (843528305), title, tags, price, image ranks and files.
2. **Upload the new video.** Upload `P11-Aging-Parent-Organizer-Etsy-Video-V1.mp4` with an explicit `name` field; the build report found Etsy needs one. Upload the video only; change nothing else.
3. **Read back.** Check that exactly 1 video is present with the new id, and that title, tags, price, images and files are unchanged.
4. **Rollback.** Re-upload `sources/p11-aging-parent-organizer/reference/listing-video.mp4` (SHA-256 `6e3846b0…3f43`).
