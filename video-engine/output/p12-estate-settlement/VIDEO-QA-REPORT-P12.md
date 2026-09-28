# VIDEO QA REPORT - Estate Settlement Command Center V1

- **Verdict:** **PASS**
- **Video:** `P12-Estate-Settlement-Etsy-Video-V1.mp4` - 1920x1080, 15.00s, h264 High, yuv420p, 30/1 fps, 3.42 MB
- **Config:** `configs/product12_estate_settlement.json`
- **Generated:** 2026-09-28 06:06 UTC by `render_video.py` (automated)
- **Checks:** 102 pass, 0 warn, 0 fail

## Source provenance (product truth)

- `source_status`: **product_capture**
- Rendered pointer shown: **no**
- Notes: Captured from the real packaged customer workbook sources/p12-estate-settlement/Estate-Settlement-Command-Center.xlsx (commit 65cd4c6; byte-identical to the SAMPLE-v1 copy), recalculated by LibreOffice. AFTER = packaged workbook as shipped (0 differing cells vs its own recalculation). BEFORE = the same workbook with ONE liability record (L3, Lakeside Funeral Home, $8,900 verified) not yet updated, using the sample's own convention for unpaid rows: Status 'Verified, Unpaid', Amount Paid 0, Payment Date blank. Capture copies change view settings only (2 sheets visible, print areas, workbook default font explicit, columns widened just enough for headers/auto-warnings to read in full - see capture/states/widened-columns.json). Overdue Tasks uses TODAY(); both states were captured on the same day. No pointer is shown; no creditor or person names are in any crop.

| Truth key | Before | After |
|---|---|---|
| l3_status | Verified, Unpaid | Paid |
| l3_paid | $0.00 | $8,900.00 |
| unpaid_disputed | 4 | 3 |
| closeout_status | REVIEW | REVIEW |
- truth verified: before.l3_status = 'Verified, Unpaid' (04_LIABILITY_REGISTER!H6)
- truth verified: before.l3_paid = '$0.00' (04_LIABILITY_REGISTER!I6)
- truth verified: before.unpaid_disputed = '4' (01_COMMAND_CENTER!B17)
- truth verified: before.closeout_status = 'REVIEW' (01_COMMAND_CENTER!B12)
- truth verified: after.l3_status = 'Paid' (04_LIABILITY_REGISTER!H6)
- truth verified: after.l3_paid = '$8,900.00' (04_LIABILITY_REGISTER!I6)
- truth verified: after.unpaid_disputed = '3' (01_COMMAND_CENTER!B17)
- truth verified: after.closeout_status = 'REVIEW' (01_COMMAND_CENTER!B12)

## Timeline

| # | Scene | Type | Start | End | Caption |
|---|---|---|---|---|---|
| 1 | before-needs-attention | screen | 0.00s | 3.00s | Open estate bills need attention. |
| 2 | record-payment | morph | 3.00s | 6.00s | Record the payment. |
| 3 | warning-clears | morph | 6.00s | 9.00s | See what’s settled — |
| 4 | outcome-still-open | morph | 9.00s | 12.00s | and what still needs attention. |
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
| PASS | Etsy: file < 100 MB | 3.42 MB |
| PASS | No audio track (Etsy plays muted) | 0 audio stream(s) |
| PASS | Web fast-start (moov before mdat) | moov -> mdat |
| PASS | Full decode without errors | clean |
| PASS | Frame count | 450 decoded (expected 450) |
| PASS | No black frames (blackdetect) | none detected |
| PASS | Static holds > 1.5 s (informational) | 13.23s (end card hold is expected) |
| PASS | First frame is a composed shot (not blank) | luma mean 240, stdev 43 |
| PASS | No ghosting: one spreadsheet state per frame | scene transition = dip, before/after = cut; checked every frame |
| PASS | No white flash (blank card > 100 ms) | 0 blank-card frames |
| PASS | Clean cut at 3.00s into record-payment: no blank flash | 0 blank frames within 0.3 s of the cut |
| PASS | Clean cut at 6.00s into warning-clears: no blank flash | 0 blank frames within 0.3 s of the cut |
| PASS | Clean cut at 9.00s into outcome-still-open: no blank flash | 0 blank frames within 0.3 s of the cut |
| PASS | Mobile preview video written | mobile/mobile-preview-780w.mp4 |
| PASS | OCR readback @2.50s: "Open estate bills need attention" | found in encoded frame |
| PASS | OCR readback @2.50s: "NEEDS ATTENTION NOW" | found in encoded frame |
| PASS | OCR readback @2.50s: "Unpaid / Disputed Liabilities" | found in encoded frame |
| PASS | OCR readback @5.60s: "Record the payment" | found in encoded frame |
| PASS | OCR readback @5.60s: "Paid" | found in encoded frame |
| PASS | OCR readback @5.60s: "$8,900.00" | found in encoded frame |
| PASS | OCR readback @8.70s: "settled" | found in encoded frame |
| PASS | OCR readback @8.70s: "Jul 16, 2026" | found in encoded frame |
| PASS | OCR readback @8.70s: "Paid" | found in encoded frame |
| PASS | OCR readback @11.70s: "and what still needs attention" | found in encoded frame |
| PASS | OCR readback @11.70s: "REVIEW" | found in encoded frame |
| PASS | OCR readback @11.70s: "Unpaid / Disputed Liabilities" | found in encoded frame |
| PASS | OCR readback @14.50s: "Estate Settlement Command Center" | found in encoded frame |
| PASS | OCR readback @14.50s: "Reconcile" | found in encoded frame |
| PASS | OCR readback @14.50s: "LEDGER" | found in encoded frame |
| PASS | Phone-size OCR: caption "Open estate bills need attention." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "Record the payment." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "See what’s settled —" | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "and what still needs attention." | read back from a 390px-wide frame |
| PASS | No clipping: wordmark "LEDGER & LIME" (global) | bbox [1603, 92, 1835, 108] within frame safe area |
| PASS | No clipping: caption "Open estate bills need attention." (s1:before-needs-attention) | bbox [84, 67, 1072, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s1:before-needs-attention) | bbox [93, 576, 1833, 663] within card |
| PASS | No clipping: caption "Record the payment." (s2:record-payment) | bbox [82, 67, 715, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s2:record-payment) | bbox [81, 593, 1838, 728] within card |
| PASS | No clipping: highlight_label "Lakeside Funeral Home" (s2:record-payment) | bbox [624, 491, 1295, 588] within card |
| PASS | No clipping: caption "See what’s settled —" (s3:warning-clears) | bbox [85, 67, 696, 126] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s3:warning-clears) | bbox [86, 514, 1762, 619] within card |
| PASS | No clipping: chip "Funeral home bill: Verified, Unpaid -> P" (s3:warning-clears) | bbox [114, 819, 876, 990] within card |
| PASS | No clipping: caption "and what still needs attention." (s4:outcome-still-open) | bbox [84, 67, 1000, 126] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s4:outcome-still-open) | bbox [94, 576, 1833, 663] within card |
| PASS | No clipping: chip "Unpaid / disputed liabilities: 4 -> 3" (s4:outcome-still-open) | bbox [114, 819, 732, 990] within card |
| PASS | No clipping: end_title "Estate Settlement Command Center" (s5:end-card) | bbox [331, 417, 1588, 483] within frame safe area |
| PASS | No clipping: end_subtitle "Track • Reconcile • Close Out" (s5:end-card) | bbox [676, 626, 1243, 654] within frame safe area |
| PASS | No clipping: end_brand "LEDGER & LIME" (s5:end-card) | bbox [795, 919, 1122, 941] within frame safe area |
| PASS | Chips never cover a visible highlight (s3:warning-clears) | checked every frame |
| PASS | Chips never cover a visible highlight (s4:outcome-still-open) | checked every frame |
| PASS | Readable dwell >= 0.6s: caption "Open estate bills need attention" | fully visible 3.00s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.17s |
| PASS | Readable dwell >= 0.6s: caption "Record the payment." | fully visible 2.53s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 1.57s |
| PASS | Readable dwell >= 0.6s: caption "See what’s settled —" | fully visible 2.53s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.47s |
| PASS | Readable dwell >= 0.6s: chip "Funeral home bill: Verified, Unp" | fully visible 1.63s |
| PASS | Readable dwell >= 0.6s: caption "and what still needs attention." | fully visible 2.57s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.50s |
| PASS | Readable dwell >= 0.6s: chip "Unpaid / disputed liabilities: 4" | fully visible 1.67s |
| PASS | Readable dwell >= 0.6s: end_title "Estate Settlement Command Center" | fully visible 2.37s |
| PASS | Caption rendered: "Open estate bills need attention." |  |
| PASS | Caption rendered: "Record the payment." |  |
| PASS | Caption rendered: "See what’s settled —" |  |
| PASS | Caption rendered: "and what still needs attention." |  |
| PASS | Phone legibility (primary): caption "Open estate bills need attenti" | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "Record the payment." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): highlight_label "Lakeside Funeral Home" | 56px -> 11.4px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "See what’s settled —" | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Funeral home bill: Verified, U" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "and what still needs attention" | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Unpaid / disputed liabilities:" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): end_title "Estate Settlement Command Cent" | 88px -> 17.9px on a 390px phone (min 11.0) |
| PASS | Phone legibility (secondary): end_subtitle "Track • Reconcile • Close Out" | 38px -> 7.7px on a 390px phone (min 6.0) |
| PASS | Phone legibility (secondary): end_brand "LEDGER & LIME" | 30px -> 6.1px on a 390px phone (min 6.0) |
| PASS | Phone legibility (secondary): chip labels | 30px -> 6.1px |
| PASS | Source not over-upscaled (s1:before-needs-attention) | max upscale 1.0x, source px per output px 3.548-3.594 |
| PASS | Source not over-upscaled (s2:record-payment) | max upscale 1.0x, source px per output px 1.051-1.051 |
| PASS | Source not over-upscaled (s3:warning-clears) | max upscale 1.0x, source px per output px 1.5-1.5 |
| PASS | Source not over-upscaled (s4:outcome-still-open) | max upscale 1.0x, source px per output px 3.548-3.594 |
| PASS | Required region fully in frame (scene 1 (before-needs-attention)) | scene 1 (before-needs-attention) region 1 [24, 24, 6100, 1850] stays fully in frame |
| PASS | Required region fully in frame (scene 2 (record-payment)) | scene 2 (record-payment) region 1 [7013, 24, 1845, 757] stays fully in frame |
| PASS | Required region fully in frame (scene 3 (warning-clears)) | scene 3 (warning-clears) region 1 [8858, 24, 2516, 757] stays fully in frame |
| PASS | Required region fully in frame (scene 4 (outcome-still-open)) | scene 4 (outcome-still-open) region 1 [24, 24, 6100, 1850] stays fully in frame |
| PASS | Product truth: before/after values verified against workbook | 8 value(s) verified against recalculated workbook cells |
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
| 2.50s | before-needs-attention | Open estate bills need attention | found | found |
| 2.50s | before-needs-attention | NEEDS ATTENTION NOW | found | found |
| 2.50s | before-needs-attention | Unpaid / Disputed Liabilities | found | found |
| 5.60s | record-payment | Record the payment | found | found |
| 5.60s | record-payment | Paid | found | found |
| 5.60s | record-payment | $8,900.00 | found | found |
| 8.70s | warning-clears | settled | found | found |
| 8.70s | warning-clears | Jul 16, 2026 | found | found |
| 8.70s | warning-clears | Paid | found | found |
| 11.70s | outcome-still-open | and what still needs attention | found | found |
| 11.70s | outcome-still-open | REVIEW | found | found |
| 11.70s | outcome-still-open | Unpaid / Disputed Liabilities | found | not legible |
| 14.50s | end-card | Estate Settlement Command Center | found | found |
| 14.50s | end-card | Reconcile | found | found |
| 14.50s | end-card | LEDGER | found | not legible |

Phone-frame OCR is a legibility proxy: spreadsheet cell text is expected to be too small at 390px; captions and value chips carry the message on phones.

## Mobile legibility (overlay text at 390px phone width)

| Element | Text | Render px | Phone px | Min |
|---|---|---|---|---|
| caption | Open estate bills need attention. | 78 | 15.8 | 11.0 |
| caption | Record the payment. | 78 | 15.8 | 11.0 |
| highlight_label | Lakeside Funeral Home | 56 | 11.4 | 11.0 |
| caption | See what’s settled — | 78 | 15.8 | 11.0 |
| chip | Funeral home bill: Verified, Unpaid -> P | 60 | 12.2 | 11.0 |
| caption | and what still needs attention. | 78 | 15.8 | 11.0 |
| chip | Unpaid / disputed liabilities: 4 -> 3 | 60 | 12.2 | 11.0 |
| end_title | Estate Settlement Command Center | 88 | 17.9 | 11.0 |
| end_subtitle | Track • Reconcile • Close Out | 38 | 7.7 | 6.0 |
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
