# VIDEO QA REPORT - Rental Property Spreadsheet V1

- **Verdict:** **PASS**
- **Video:** `P10-Rental-Property-Etsy-Video-V1.mp4` - 1920x1080, 15.00s, h264 High, yuv420p, 30/1 fps, 3.86 MB
- **Config:** `configs/product10_rental_property.json`
- **Generated:** 2026-09-27 18:00 UTC by `render_video.py` (automated)
- **Checks:** 104 pass, 0 warn, 0 fail

## Source provenance (product truth)

- `source_status`: **product_capture**
- Rendered pointer shown: **no**
- Notes: Captured from the real packaged customer workbook sources/p10-rental-property/Rental-Property-Spreadsheet.xlsx (commit 65cd4c6), recalculated by LibreOffice. AFTER = packaged workbook as shipped (0 differing cells vs the packaged workbook's own recalculation). BEFORE = the same workbook with ONE input cleared: Rent Tracker H5/I5, the May 2026 Payment 1 of $1,000 for unit P1-U1 (tenant T1). Capture copies change print settings only (print area A3:P9, other sheets hidden) and make the workbook default font (Calibri, rendered with metric-compatible Carlito) explicit on header cells saved without a font name. No pointer is shown.

| Truth key | Before | After |
|---|---|---|
| may_paid | $0.00 | $1,000.00 |
| may_remaining | $1,500.00 | $500.00 |
| may_status | Unpaid | Partial |
| june_prior | $1,500.00 | $500.00 |
| june_total_due | $3,000.00 | $2,000.00 |
| dashboard_outstanding | $8,000.00 | $4,300.00 |
| dashboard_overdue_partial | 8 | 6 |
- truth verified: before.may_paid = '$0.00' (Rent Tracker!N5)
- truth verified: before.may_remaining = '$1,500.00' (Rent Tracker!O5)
- truth verified: before.may_status = 'Unpaid' (Rent Tracker!P5)
- truth verified: before.june_prior = '$1,500.00' (Rent Tracker!F6)
- truth verified: before.june_total_due = '$3,000.00' (Rent Tracker!G6)
- truth verified: before.dashboard_outstanding = '$8,000.00' (Dashboard!B7)
- truth verified: before.dashboard_overdue_partial = '8' (Dashboard!B15)
- truth verified: after.may_paid = '$1,000.00' (Rent Tracker!N5)
- truth verified: after.may_remaining = '$500.00' (Rent Tracker!O5)
- truth verified: after.may_status = 'Partial' (Rent Tracker!P5)
- truth verified: after.june_prior = '$500.00' (Rent Tracker!F6)
- truth verified: after.june_total_due = '$2,000.00' (Rent Tracker!G6)
- truth verified: after.dashboard_outstanding = '$4,300.00' (Dashboard!B7)
- truth verified: after.dashboard_overdue_partial = '6' (Dashboard!B15)

## Timeline

| # | Scene | Type | Start | End | Caption |
|---|---|---|---|---|---|
| 1 | before-unpaid | screen | 0.00s | 3.00s | May rent is still unpaid. |
| 2 | input-partial-payment | morph | 3.00s | 6.00s | Log a partial payment. |
| 3 | balance-updates | morph | 6.00s | 9.00s | The balance updates itself. |
| 4 | carry-forward | morph | 9.00s | 12.00s | Know who still owes — automatically. |
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
| PASS | Etsy: file < 100 MB | 3.86 MB |
| PASS | No audio track (Etsy plays muted) | 0 audio stream(s) |
| PASS | Web fast-start (moov before mdat) | moov -> mdat |
| PASS | Full decode without errors | clean |
| PASS | Frame count | 450 decoded (expected 450) |
| PASS | No black frames (blackdetect) | none detected |
| PASS | Static holds > 1.5 s (informational) | 13.10s (end card hold is expected) |
| PASS | First frame is a composed shot (not blank) | luma mean 216, stdev 72 |
| PASS | No ghosting: one spreadsheet state per frame | scene transition = dip, before/after = cut; checked every frame |
| PASS | No white flash (blank card > 100 ms) | 0 blank-card frames |
| PASS | Clean cut at 3.00s into input-partial-payment: no blank flash | 0 blank frames within 0.3 s of the cut |
| PASS | Clean cut at 6.00s into balance-updates: no blank flash | 0 blank frames within 0.3 s of the cut |
| PASS | Clean cut at 9.00s into carry-forward: no blank flash | 0 blank frames within 0.3 s of the cut |
| PASS | Mobile preview video written | mobile/mobile-preview-780w.mp4 |
| PASS | OCR readback @2.50s: "May rent is still unpaid" | found in encoded frame |
| PASS | OCR readback @2.50s: "$1,500.00" | found in encoded frame |
| PASS | OCR readback @2.50s: "Unpaid" | found in encoded frame |
| PASS | OCR readback @5.60s: "Log a partial payment" | found in encoded frame |
| PASS | OCR readback @5.60s: "$1,000.00" | found in encoded frame |
| PASS | OCR readback @5.60s: "May 4, 2026" | found in encoded frame |
| PASS | OCR readback @8.70s: "The balance updates itself" | found in encoded frame |
| PASS | OCR readback @8.70s: "$500.00" | found in encoded frame |
| PASS | OCR readback @8.70s: "Partial" | found in encoded frame |
| PASS | OCR readback @11.70s: "Know who still owes" | found in encoded frame |
| PASS | OCR readback @11.70s: "$500.00" | found in encoded frame |
| PASS | OCR readback @11.70s: "$2,000.00" | found in encoded frame |
| PASS | OCR readback @14.50s: "Rental Property Spreadsheet" | found in encoded frame |
| PASS | OCR readback @14.50s: "Carried Balances" | found in encoded frame |
| PASS | OCR readback @14.50s: "LEDGER" | found in encoded frame |
| PASS | Phone-size OCR: caption "May rent is still unpaid." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "Log a partial payment." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "The balance updates itself." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "Know who still owes — automatically." | read back from a 390px-wide frame |
| PASS | No clipping: wordmark "LEDGER & LIME" (global) | bbox [1603, 92, 1835, 108] within frame safe area |
| PASS | No clipping: caption "May rent is still unpaid." (s1:before-unpaid) | bbox [82, 67, 800, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s1:before-unpaid) | bbox [588, 404, 1825, 572] within card |
| PASS | No clipping: caption "Log a partial payment." (s2:input-partial-payment) | bbox [81, 67, 763, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s2:input-partial-payment) | bbox [651, 388, 1839, 587] within card |
| PASS | No clipping: caption "The balance updates itself." (s3:balance-updates) | bbox [83, 67, 880, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s3:balance-updates) | bbox [588, 404, 1825, 574] within card |
| PASS | No clipping: chip "May balance: $1,500.00 -> $500.00" (s3:balance-updates) | bbox [114, 819, 827, 990] within card |
| PASS | No clipping: chip "Status: Unpaid -> Partial" (s3:balance-updates) | bbox [849, 819, 1409, 990] within card |
| PASS | No clipping: caption "Know who still owes — automatically." (s4:carry-forward) | bbox [81, 67, 1237, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s4:carry-forward) | bbox [672, 529, 1836, 719] within card |
| PASS | No clipping: highlight_label "Carried from May" (s4:carry-forward) | bbox [146, 555, 660, 692] within card |
| PASS | No clipping: chip "Carried into June: $1,500.00 -> $500.00" (s4:carry-forward) | bbox [114, 819, 827, 990] within card |
| PASS | No clipping: chip "June total due: $3,000.00 -> $2,000.00" (s4:carry-forward) | bbox [849, 819, 1633, 990] within card |
| PASS | No clipping: end_title "Rental Property Spreadsheet" (s5:end-card) | bbox [464, 417, 1454, 507] within frame safe area |
| PASS | No clipping: end_subtitle "Rent • Partial Payments • Carried Balanc" (s5:end-card) | bbox [554, 626, 1364, 662] within frame safe area |
| PASS | No clipping: end_brand "LEDGER & LIME" (s5:end-card) | bbox [795, 919, 1122, 941] within frame safe area |
| PASS | Chips never cover a visible highlight (s3:balance-updates) | checked every frame |
| PASS | Chips never cover a visible highlight (s4:carry-forward) | checked every frame |
| PASS | Readable dwell >= 0.6s: caption "May rent is still unpaid." | fully visible 3.00s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.17s |
| PASS | Readable dwell >= 0.6s: caption "Log a partial payment." | fully visible 2.53s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 1.57s |
| PASS | Readable dwell >= 0.6s: caption "The balance updates itself." | fully visible 2.53s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.47s |
| PASS | Readable dwell >= 0.6s: chip "May balance: $1,500.00 -> $500.0" | fully visible 1.63s |
| PASS | Readable dwell >= 0.6s: chip "Status: Unpaid -> Partial" | fully visible 1.43s |
| PASS | Readable dwell >= 0.6s: caption "Know who still owes — automatica" | fully visible 2.57s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.50s |
| PASS | Readable dwell >= 0.6s: chip "Carried into June: $1,500.00 -> " | fully visible 1.67s |
| PASS | Readable dwell >= 0.6s: chip "June total due: $3,000.00 -> $2," | fully visible 1.47s |
| PASS | Readable dwell >= 0.6s: end_title "Rental Property Spreadsheet" | fully visible 2.37s |
| PASS | Caption rendered: "May rent is still unpaid." |  |
| PASS | Caption rendered: "Log a partial payment." |  |
| PASS | Caption rendered: "The balance updates itself." |  |
| PASS | Caption rendered: "Know who still owes — automatically." |  |
| PASS | Phone legibility (primary): caption "May rent is still unpaid." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "Log a partial payment." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "The balance updates itself." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "May balance: $1,500.00 -> $500" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Status: Unpaid -> Partial" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "Know who still owes — automati" | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): highlight_label "Carried from May" | 56px -> 11.4px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Carried into June: $1,500.00 -" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "June total due: $3,000.00 -> $" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): end_title "Rental Property Spreadsheet" | 88px -> 17.9px on a 390px phone (min 11.0) |
| PASS | Phone legibility (secondary): end_subtitle "Rent • Partial Payments • Carr" | 38px -> 7.7px on a 390px phone (min 6.0) |
| PASS | Phone legibility (secondary): end_brand "LEDGER & LIME" | 30px -> 6.1px on a 390px phone (min 6.0) |
| PASS | Phone legibility (secondary): chip labels | 30px -> 6.1px |
| PASS | Source not over-upscaled (s1:before-unpaid) | max upscale 1.13x, source px per output px 0.885-0.885 |
| PASS | Source not over-upscaled (s2:input-partial-payment) | max upscale 1.266x, source px per output px 0.79-0.79 |
| PASS | Source not over-upscaled (s3:balance-updates) | max upscale 1.13x, source px per output px 0.885-0.885 |
| PASS | Source not over-upscaled (s4:carry-forward) | max upscale 1.205x, source px per output px 0.83-0.83 |
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
| 2.50s | before-unpaid | May rent is still unpaid | found | found |
| 2.50s | before-unpaid | $1,500.00 | found | found |
| 2.50s | before-unpaid | Unpaid | found | found |
| 5.60s | input-partial-payment | Log a partial payment | found | found |
| 5.60s | input-partial-payment | $1,000.00 | found | not legible |
| 5.60s | input-partial-payment | May 4, 2026 | found | not legible |
| 8.70s | balance-updates | The balance updates itself | found | found |
| 8.70s | balance-updates | $500.00 | found | found |
| 8.70s | balance-updates | Partial | found | found |
| 11.70s | carry-forward | Know who still owes | found | found |
| 11.70s | carry-forward | $500.00 | found | found |
| 11.70s | carry-forward | $2,000.00 | found | found |
| 14.50s | end-card | Rental Property Spreadsheet | found | not legible |
| 14.50s | end-card | Carried Balances | found | found |
| 14.50s | end-card | LEDGER | found | found |

Phone-frame OCR is a legibility proxy: spreadsheet cell text is expected to be too small at 390px; captions and value chips carry the message on phones.

## Mobile legibility (overlay text at 390px phone width)

| Element | Text | Render px | Phone px | Min |
|---|---|---|---|---|
| caption | May rent is still unpaid. | 78 | 15.8 | 11.0 |
| caption | Log a partial payment. | 78 | 15.8 | 11.0 |
| caption | The balance updates itself. | 78 | 15.8 | 11.0 |
| chip | May balance: $1,500.00 -> $500.00 | 60 | 12.2 | 11.0 |
| chip | Status: Unpaid -> Partial | 60 | 12.2 | 11.0 |
| caption | Know who still owes — automatically. | 78 | 15.8 | 11.0 |
| highlight_label | Carried from May | 56 | 11.4 | 11.0 |
| chip | Carried into June: $1,500.00 -> $500.00 | 60 | 12.2 | 11.0 |
| chip | June total due: $3,000.00 -> $2,000.00 | 60 | 12.2 | 11.0 |
| end_title | Rental Property Spreadsheet | 88 | 17.9 | 11.0 |
| end_subtitle | Rent • Partial Payments • Carried Balanc | 38 | 7.7 | 6.0 |
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
