# VIDEO QA REPORT - Aging Parent Financial Organizer V1

- **Verdict:** **PASS**
- **Video:** `P11-Aging-Parent-Organizer-Etsy-Video-V1.mp4` - 1920x1080, 15.00s, h264 High, yuv420p, 30/1 fps, 4.86 MB
- **Config:** `configs/product11_aging_parent.json`
- **Generated:** 2026-09-29 15:27 UTC by `render_video.py` (automated)
- **Checks:** 118 pass, 0 warn, 0 fail

## Source provenance (product truth)

- `source_status`: **product_capture**
- Rendered pointer shown: **no**
- Notes: Captured from the real delivered customer workbook sources/p11-aging-parent-organizer/workbook/Aging-Parent-Financial-Organizer.xlsx (Etsy buyer file for listing 4579424851, 223,940 bytes, SHA-256 eaaac91d...9f23, commit 09e83c4; never modified), recalculated by LibreOffice. AFTER = delivered workbook as shipped (0 differing cells vs its own recalculation; Dashboard matches the build report: Pending 3, Outstanding $124.50, Contributions $790.00). BEFORE = the same workbook with ONE reimbursement not yet recorded: contribution row C7 (Parent Account -> $40 for expense E7, Dental copay) left empty, the workbook's own convention for an unused row. Capture copies change view settings only (3 sheets visible, print areas, workbook default font explicit, columns widened just enough for headers / sample text to read in full - see capture/states/widened-columns.json). None of the filmed values use TODAY(). No pointer is shown. Names on screen are the workbook's fictional sample family.

| Truth key | Before | After |
|---|---|---|
| c7_applied | $0.00 | $40.00 |
| e7_status | Pending | Reimbursed |
| e7_reimbursed | $0.00 | $40.00 |
| e7_remaining | $40.00 | $0.00 |
| pending_count | 4 | 3 |
| contributions_applied | $750.00 | $790.00 |
| outstanding | $164.50 | $124.50 |
- truth verified: before.c7_applied = '$0.00' (Family Contributions!G10)
- truth verified: before.e7_status = 'Pending' (Expenses & Receipts!L10)
- truth verified: before.e7_reimbursed = '$0.00' (Expenses & Receipts!M10)
- truth verified: before.e7_remaining = '$40.00' (Expenses & Receipts!N10)
- truth verified: before.pending_count = '4' (Dashboard!B5)
- truth verified: before.contributions_applied = '$750.00' (Dashboard!B6)
- truth verified: before.outstanding = '$164.50' (Dashboard!B7)
- truth verified: after.c7_applied = '$40.00' (Family Contributions!G10)
- truth verified: after.e7_status = 'Reimbursed' (Expenses & Receipts!L10)
- truth verified: after.e7_reimbursed = '$40.00' (Expenses & Receipts!M10)
- truth verified: after.e7_remaining = '$0.00' (Expenses & Receipts!N10)
- truth verified: after.pending_count = '3' (Dashboard!B5)
- truth verified: after.contributions_applied = '$790.00' (Dashboard!B6)
- truth verified: after.outstanding = '$124.50' (Dashboard!B7)

## Timeline

| # | Scene | Type | Start | End | Caption |
|---|---|---|---|---|---|
| 1 | before-still-owed | screen | 0.00s | 3.00s | See who’s still waiting to be paid back. |
| 2 | record-reimbursement | morph | 3.00s | 6.00s | Record a family reimbursement. |
| 3 | expense-updates | morph | 6.00s | 9.00s | The expense updates itself. |
| 4 | dashboard-updates | morph | 9.00s | 12.00s | The whole family sees what’s still owed. |
| 5 | end-card | end_card | 12.00s | 15.00s | - |

## Automated checks

| Result | Check | Detail |
|---|---|---|
| PASS | File readable by ffprobe |  |
| PASS | Container MP4 | mov,mp4,m4a,3gp,3g2,mj2 |
| PASS | Codec H.264 (High) | h264 / High / level 41 |
| PASS | Resolution | 1920x1080 (expected 1920x1080) |
| PASS | Pixel format yuv420p | yuv420p |
| PASS | Frame rate | 30/1 |
| PASS | Colour tagged BT.709 | bt709/bt709/bt709 |
| PASS | Duration matches timeline | 15.000s (expected 15.000s) |
| PASS | Duration within 12-15s | 15.00s |
| PASS | Etsy: <= 15 s (longer is trimmed) | 15.00s |
| PASS | Etsy: file < 100 MB | 4.86 MB |
| PASS | No audio track (Etsy plays muted) | 0 audio stream(s) |
| PASS | Web fast-start (moov before mdat) | moov -> mdat |
| PASS | Full decode without errors | clean |
| PASS | Frame count | 450 decoded (expected 450) |
| PASS | No black frames (blackdetect) | none detected |
| PASS | Static holds > 1.5 s (informational) | 13.13s (end card hold is expected) |
| PASS | First frame is a composed shot (not blank) | luma mean 241, stdev 41 |
| PASS | No ghosting: one spreadsheet state per frame | scene transition = dip, before/after = cut; checked every frame |
| PASS | No white flash (blank card > 100 ms) | 0 blank-card frames |
| PASS | Clean cut at 3.00s into record-reimbursement: no blank flash | 0 blank frames within 0.3 s of the cut |
| PASS | Clean cut at 6.00s into expense-updates: no blank flash | 0 blank frames within 0.3 s of the cut |
| PASS | Clean cut at 9.00s into dashboard-updates: no blank flash | 0 blank frames within 0.3 s of the cut |
| PASS | Mobile preview video written | mobile/mobile-preview-780w.mp4 |
| PASS | OCR readback @2.50s: "waiting to be paid back" | found in encoded frame |
| PASS | OCR readback @2.50s: "Reimbursements Pending" | found in encoded frame |
| PASS | OCR readback @2.50s: "$164.50" | found in encoded frame |
| PASS | OCR readback @5.60s: "Record a family reimbursement" | found in encoded frame |
| PASS | OCR readback @5.60s: "Applied Amount" | found in encoded frame |
| PASS | OCR readback @5.60s: "$40.00" | found in encoded frame |
| PASS | OCR readback @8.70s: "expense updates" | found in encoded frame |
| PASS | OCR readback @8.70s: "Reimbursed" | found in encoded frame |
| PASS | OCR readback @8.70s: "$40.00" | found in encoded frame |
| PASS | OCR readback @11.70s: "still owed" | found in encoded frame |
| PASS | OCR readback @11.70s: "$124.50" | found in encoded frame |
| PASS | OCR readback @11.70s: "Reimbursements Pending" | found in encoded frame |
| PASS | OCR readback @14.50s: "Aging Parent Financial Organizer" | found in encoded frame |
| PASS | OCR readback @14.50s: "Reimbursements" | found in encoded frame |
| PASS | OCR readback @14.50s: "LEDGER" | found in encoded frame |
| PASS | Phone-size OCR: caption "See who’s still waiting to be paid back." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "Record a family reimbursement." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "The expense updates itself." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "The whole family sees what’s still owed." | read back from a 390px-wide frame |
| PASS | No clipping: wordmark "LEDGER & LIME" (global) | bbox [1603, 92, 1835, 108] within frame safe area |
| PASS | No clipping: caption "See who’s still waiting to be paid back." (s1:before-still-owed) | bbox [85, 67, 1249, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s1:before-still-owed) | bbox [278, 449, 1641, 523] within card |
| PASS | No clipping: highlight "highlight 2" (s1:before-still-owed) | bbox [278, 565, 1641, 640] within card |
| PASS | No clipping: caption "Record a family reimbursement." (s2:record-reimbursement) | bbox [82, 67, 1063, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s2:record-reimbursement) | bbox [83, 503, 1838, 561] within card |
| PASS | No clipping: highlight_label "Related Expense ID: E7" (s2:record-reimbursement) | bbox [631, 568, 1290, 662] within card |
| PASS | No clipping: chip "Applied to expense: $0.00 -> $40.00" (s2:record-reimbursement) | bbox [114, 819, 671, 990] within card |
| PASS | No clipping: caption "The expense updates itself." (s3:expense-updates) | bbox [83, 67, 886, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s3:expense-updates) | bbox [97, 606, 1819, 676] within card |
| PASS | No clipping: highlight_label "E7 • Dental copay" (s3:expense-updates) | bbox [698, 677, 1217, 777] within card |
| PASS | No clipping: chip "Reimbursement status: Pending -> Reimbur" (s3:expense-updates) | bbox [114, 819, 868, 990] within card |
| PASS | No clipping: chip "Still owed: $40.00 -> $0.00" (s3:expense-updates) | bbox [890, 819, 1447, 990] within card |
| PASS | No clipping: caption "The whole family sees what’s still owed." (s4:dashboard-updates) | bbox [83, 67, 1276, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s4:dashboard-updates) | bbox [279, 449, 1641, 523] within card |
| PASS | No clipping: highlight "highlight 2" (s4:dashboard-updates) | bbox [279, 565, 1641, 640] within card |
| PASS | No clipping: chip "Reimbursements pending: 4 -> 3" (s4:dashboard-updates) | bbox [114, 819, 669, 990] within card |
| PASS | No clipping: chip "Outstanding reimbursement: $164.50 -> $1" (s4:dashboard-updates) | bbox [691, 819, 1330, 990] within card |
| PASS | No clipping: end_title "Aging Parent Financial Organizer" (s5:end-card) | bbox [374, 418, 1540, 507] within frame safe area |
| PASS | No clipping: end_subtitle "Expenses • Reimbursements • Family Hando" (s5:end-card) | bbox [523, 625, 1396, 662] within frame safe area |
| PASS | No clipping: end_brand "LEDGER & LIME" (s5:end-card) | bbox [795, 919, 1122, 941] within frame safe area |
| PASS | Chips never cover a visible highlight (s2:record-reimbursement) | checked every frame |
| PASS | Chips never cover a visible highlight (s3:expense-updates) | checked every frame |
| PASS | Chips never cover a visible highlight (s4:dashboard-updates) | checked every frame |
| PASS | Readable dwell >= 0.6s: caption "See who’s still waiting to be pa" | fully visible 3.00s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.17s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 2" | fully visible 2.17s |
| PASS | Readable dwell >= 0.6s: caption "Record a family reimbursement." | fully visible 2.53s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 1.57s |
| PASS | Readable dwell >= 0.6s: chip "Applied to expense: $0.00 -> $40" | fully visible 1.33s |
| PASS | Readable dwell >= 0.6s: caption "The expense updates itself." | fully visible 2.53s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.47s |
| PASS | Readable dwell >= 0.6s: chip "Reimbursement status: Pending ->" | fully visible 1.63s |
| PASS | Readable dwell >= 0.6s: chip "Still owed: $40.00 -> $0.00" | fully visible 1.43s |
| PASS | Readable dwell >= 0.6s: caption "The whole family sees what’s sti" | fully visible 2.57s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.50s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 2" | fully visible 2.50s |
| PASS | Readable dwell >= 0.6s: chip "Reimbursements pending: 4 -> 3" | fully visible 1.67s |
| PASS | Readable dwell >= 0.6s: chip "Outstanding reimbursement: $164." | fully visible 1.47s |
| PASS | Readable dwell >= 0.6s: end_title "Aging Parent Financial Organizer" | fully visible 2.37s |
| PASS | Caption rendered: "See who’s still waiting to be paid back." |  |
| PASS | Caption rendered: "Record a family reimbursement." |  |
| PASS | Caption rendered: "The expense updates itself." |  |
| PASS | Caption rendered: "The whole family sees what’s still owed." |  |
| PASS | Phone legibility (primary): caption "See who’s still waiting to be " | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "Record a family reimbursement." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): highlight_label "Related Expense ID: E7" | 56px -> 11.4px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Applied to expense: $0.00 -> $" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "The expense updates itself." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): highlight_label "E7 • Dental copay" | 56px -> 11.4px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Reimbursement status: Pending " | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Still owed: $40.00 -> $0.00" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "The whole family sees what’s s" | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Reimbursements pending: 4 -> 3" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Outstanding reimbursement: $16" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): end_title "Aging Parent Financial Organiz" | 88px -> 17.9px on a 390px phone (min 11.0) |
| PASS | Phone legibility (secondary): end_subtitle "Expenses • Reimbursements • Fa" | 38px -> 7.7px on a 390px phone (min 6.0) |
| PASS | Phone legibility (secondary): end_brand "LEDGER & LIME" | 30px -> 6.1px on a 390px phone (min 6.0) |
| PASS | Phone legibility (secondary): chip labels | 30px -> 6.1px |
| PASS | Source not over-upscaled (s1:before-still-owed) | max upscale 1.0x, source px per output px 2.837-2.882 |
| PASS | Source not over-upscaled (s2:record-reimbursement) | max upscale 1.0x, source px per output px 2.352-2.352 |
| PASS | Source not over-upscaled (s3:expense-updates) | max upscale 1.0x, source px per output px 1.398-1.398 |
| PASS | Source not over-upscaled (s4:dashboard-updates) | max upscale 1.0x, source px per output px 2.837-2.882 |
| PASS | Required region fully in frame (scene 1 (before-still-owed)) | scene 1 (before-still-owed) region 1 [24, 24, 3823, 1693] stays fully in frame |
| PASS | Required region fully in frame (scene 2 (record-reimbursement)) | scene 2 (record-reimbursement) region 1 [681, 24, 4105, 885] stays fully in frame |
| PASS | Required region fully in frame (scene 3 (expense-updates)) | scene 3 (expense-updates) region 1 [5142, 24, 2416, 547] stays fully in frame |
| PASS | Required region fully in frame (scene 4 (dashboard-updates)) | scene 4 (dashboard-updates) region 1 [24, 24, 3823, 1693] stays fully in frame |
| PASS | Product truth: before/after values verified against workbook | 14 value(s) verified against recalculated workbook cells |
| PASS | No rendered pointer presented as live capture | provenance.pointer_rendered = false |
| PASS | No compliance / legal claims in on-screen text | none found |
| PASS | Sources cleared for listing | source_status = product_capture |
| PASS | No internal / QA labels in any frame | OCR of 12 key frames: none found |
| PASS | Privacy: no person-name labels in workbook data | 0 cell values scanned |
| PASS | Privacy: identifiers use the safe ID format | no IDs found in workbook data |
| PASS | Privacy: no person-name labels in any frame (OCR) | 12 key frames scanned |

## OCR readback (text read from the encoded MP4)

| Time | Scene | Expected text | 1920px frame | 390px phone frame |
|---|---|---|---|---|
| 2.50s | before-still-owed | waiting to be paid back | found | found |
| 2.50s | before-still-owed | Reimbursements Pending | found | found |
| 2.50s | before-still-owed | $164.50 | found | found |
| 5.60s | record-reimbursement | Record a family reimbursement | found | found |
| 5.60s | record-reimbursement | Applied Amount | found | not legible |
| 5.60s | record-reimbursement | $40.00 | found | found |
| 8.70s | expense-updates | expense updates | found | found |
| 8.70s | expense-updates | Reimbursed | found | found |
| 8.70s | expense-updates | $40.00 | found | found |
| 11.70s | dashboard-updates | still owed | found | found |
| 11.70s | dashboard-updates | $124.50 | found | found |
| 11.70s | dashboard-updates | Reimbursements Pending | found | not legible |
| 14.50s | end-card | Aging Parent Financial Organizer | found | found |
| 14.50s | end-card | Reimbursements | found | found |
| 14.50s | end-card | LEDGER | found | not legible |

Phone-frame OCR is a legibility proxy: spreadsheet cell text is expected to be too small at 390px; captions and value chips carry the message on phones.

## Mobile legibility (overlay text at 390px phone width)

| Element | Text | Render px | Phone px | Min |
|---|---|---|---|---|
| caption | See who’s still waiting to be paid back. | 78 | 15.8 | 11.0 |
| caption | Record a family reimbursement. | 78 | 15.8 | 11.0 |
| highlight_label | Related Expense ID: E7 | 56 | 11.4 | 11.0 |
| chip | Applied to expense: $0.00 -> $40.00 | 60 | 12.2 | 11.0 |
| caption | The expense updates itself. | 78 | 15.8 | 11.0 |
| highlight_label | E7 • Dental copay | 56 | 11.4 | 11.0 |
| chip | Reimbursement status: Pending -> Reimbur | 60 | 12.2 | 11.0 |
| chip | Still owed: $40.00 -> $0.00 | 60 | 12.2 | 11.0 |
| caption | The whole family sees what’s still owed. | 78 | 15.8 | 11.0 |
| chip | Reimbursements pending: 4 -> 3 | 60 | 12.2 | 11.0 |
| chip | Outstanding reimbursement: $164.50 -> $1 | 60 | 12.2 | 11.0 |
| end_title | Aging Parent Financial Organizer | 88 | 17.9 | 11.0 |
| end_subtitle | Expenses • Reimbursements • Family Hando | 38 | 7.7 | 6.0 |
| end_brand | LEDGER & LIME | 30 | 6.1 | 6.0 |

## Artifacts

- Contact sheet: `qa/contact-sheet.png`
- Transition strip (frames around every cut / swap): `qa/transition-strip.png`
- Phone-size contact sheet: `qa/mobile-contact-sheet.png`
- Phone preview video: `qa/mobile/mobile-preview-780w.mp4`
- Key frames: `qa/keyframes/`
- Machine-readable results: `qa/qa-results.json`; layout manifest: `render-manifest.json`

## Manual review (automation cannot judge these)

- [ ] Pacing feels calm, not rushed; each caption readable in one glance
- [ ] Highlights point at the right cells and feel restrained (no cheesy motion)
- [ ] The before/after change reads clearly as ONE real input causing the update
- [ ] Screens are real product captures (no mocked or fake UI)
- [ ] Brand feel: navy / cream / restrained gold, premium and quiet
- [ ] Watch `qa/mobile/mobile-preview-780w.mp4` on an actual phone
