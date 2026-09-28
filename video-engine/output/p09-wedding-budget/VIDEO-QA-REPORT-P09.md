# VIDEO QA REPORT - Premium Wedding Budget & Payment System V1

- **Verdict:** **PASS**
- **Video:** `P09-Wedding-Budget-Etsy-Video-V1.mp4` - 1920x1080, 15.00s, h264 High, yuv420p, 30/1 fps, 4.33 MB
- **Config:** `configs/product09_wedding_budget.json`
- **Generated:** 2026-09-28 09:40 UTC by `render_video.py` (automated)
- **Checks:** 107 pass, 0 warn, 0 fail

## Source provenance (product truth)

- `source_status`: **product_capture**
- Rendered pointer shown: **no**
- Notes: Captured from the real packaged customer workbook sources/p09-wedding-budget/Premium-Wedding-Budget-System.xlsx (commit 65cd4c6), recalculated by LibreOffice on 2026-09-28. AFTER = packaged workbook as shipped (0 differing cells vs its own recalculation): Tasty Catering Co, Contracted $8,500, Total Paid To Date $8,500, PAID IN FULL. BEFORE = the same workbook with that ONE vendor's final payment not yet logged, using the sample's own convention for vendors with an open balance (Total Paid To Date = Deposit Required = $1,000). Status / overdue figures compare due dates with Settings!B7 = TODAY(); both states were captured in the same run on 2026-09-28. Capture copies change view settings only (2 sheets visible, print areas, workbook default font explicit, columns widened just enough for headers to read in full - see capture/states/widened-columns.json). No pointer is shown; no personal names appear (payers are 'Partner 1/2', 'Family').

| Truth key | Before | After |
|---|---|---|
| catering_paid | $1,000.00 | $8,500.00 |
| catering_balance | $7,500.00 | $0.00 |
| catering_status | OVERDUE | PAID IN FULL |
| total_paid | $3,800.00 | $11,300.00 |
| total_remaining | $29,700.00 | $22,200.00 |
| overdue_count | 3 | 2 |
| overdue_amount | $11,500.00 | $4,000.00 |
- truth verified: before.catering_paid = '$1,000.00' (Vendor & Payments!E5)
- truth verified: before.catering_balance = '$7,500.00' (Vendor & Payments!F5)
- truth verified: before.catering_status = 'OVERDUE' (Vendor & Payments!I5)
- truth verified: before.total_paid = '$3,800.00' (Dashboard!B6)
- truth verified: before.total_remaining = '$29,700.00' (Dashboard!B7)
- truth verified: before.overdue_count = '3' (Dashboard!B11)
- truth verified: before.overdue_amount = '$11,500.00' (Dashboard!B12)
- truth verified: after.catering_paid = '$8,500.00' (Vendor & Payments!E5)
- truth verified: after.catering_balance = '$0.00' (Vendor & Payments!F5)
- truth verified: after.catering_status = 'PAID IN FULL' (Vendor & Payments!I5)
- truth verified: after.total_paid = '$11,300.00' (Dashboard!B6)
- truth verified: after.total_remaining = '$22,200.00' (Dashboard!B7)
- truth verified: after.overdue_count = '2' (Dashboard!B11)
- truth verified: after.overdue_amount = '$4,000.00' (Dashboard!B12)

## Timeline

| # | Scene | Type | Start | End | Caption |
|---|---|---|---|---|---|
| 1 | before-overdue | screen | 0.00s | 3.00s | See which payments are overdue. |
| 2 | log-final-payment | morph | 3.00s | 6.00s | Log the final payment. |
| 3 | balance-status-update | morph | 6.00s | 9.00s | Balance and status update themselves. |
| 4 | dashboard-updates | morph | 9.00s | 12.00s | See what’s paid — and what’s still owed. |
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
| PASS | Etsy: file < 100 MB | 4.33 MB |
| PASS | No audio track (Etsy plays muted) | 0 audio stream(s) |
| PASS | Web fast-start (moov before mdat) | moov -> mdat |
| PASS | Full decode without errors | clean |
| PASS | Frame count | 450 decoded (expected 450) |
| PASS | No black frames (blackdetect) | none detected |
| PASS | Static holds > 1.5 s (informational) | none |
| PASS | First frame is a composed shot (not blank) | luma mean 240, stdev 45 |
| PASS | No ghosting: one spreadsheet state per frame | scene transition = dip, before/after = cut; checked every frame |
| PASS | No white flash (blank card > 100 ms) | 0 blank-card frames |
| PASS | Clean cut at 3.00s into log-final-payment: no blank flash | 0 blank frames within 0.3 s of the cut |
| PASS | Clean cut at 6.00s into balance-status-update: no blank flash | 0 blank frames within 0.3 s of the cut |
| PASS | Clean cut at 9.00s into dashboard-updates: no blank flash | 0 blank frames within 0.3 s of the cut |
| PASS | Mobile preview video written | mobile/mobile-preview-780w.mp4 |
| PASS | OCR readback @2.50s: "See which payments are overdue" | found in encoded frame |
| PASS | OCR readback @2.50s: "Overdue Payments" | found in encoded frame |
| PASS | OCR readback @2.50s: "$11,500.00" | found in encoded frame |
| PASS | OCR readback @5.60s: "Log the final payment" | found in encoded frame |
| PASS | OCR readback @5.60s: "$8,500.00" | found in encoded frame |
| PASS | OCR readback @5.60s: "Total Paid To Date" | found in encoded frame |
| PASS | OCR readback @8.70s: "update themselves" | found in encoded frame |
| PASS | OCR readback @8.70s: "$0.00" | found in encoded frame |
| PASS | OCR readback @8.70s: "PAID IN FULL" | found in encoded frame |
| PASS | OCR readback @11.70s: "still owed" | found in encoded frame |
| PASS | OCR readback @11.70s: "$11,300.00" | found in encoded frame |
| PASS | OCR readback @11.70s: "$4,000.00" | found in encoded frame |
| PASS | OCR readback @14.50s: "Wedding Budget" | found in encoded frame |
| PASS | OCR readback @14.50s: "Vendor Payments" | found in encoded frame |
| PASS | OCR readback @14.50s: "LEDGER" | found in encoded frame |
| PASS | Phone-size OCR: caption "See which payments are overdue." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "Log the final payment." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "Balance and status update themselves." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "See what’s paid — and what’s still owed." | read back from a 390px-wide frame |
| PASS | No clipping: wordmark "LEDGER & LIME" (global) | bbox [1603, 92, 1835, 108] within frame safe area |
| PASS | No clipping: caption "See which payments are overdue." (s1:before-overdue) | bbox [85, 67, 1084, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s1:before-overdue) | bbox [109, 647, 1825, 818] within card |
| PASS | No clipping: caption "Log the final payment." (s2:log-final-payment) | bbox [81, 67, 765, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s2:log-final-payment) | bbox [1251, 518, 1834, 615] within card |
| PASS | No clipping: highlight_label "Tasty Catering Co" (s2:log-final-payment) | bbox [1278, 620, 1805, 715] within card |
| PASS | No clipping: caption "Balance and status update themselves." (s3:balance-status-update) | bbox [82, 67, 1234, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s3:balance-status-update) | bbox [84, 355, 1819, 432] within card |
| PASS | No clipping: chip "Catering balance: $7,500.00 -> $0.00" (s3:balance-status-update) | bbox [114, 819, 753, 990] within card |
| PASS | No clipping: chip "Status: OVERDUE -> PAID IN FULL" (s3:balance-status-update) | bbox [775, 819, 1608, 990] within card |
| PASS | No clipping: caption "See what’s paid — and what’s still owed." (s4:dashboard-updates) | bbox [85, 67, 1294, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s4:dashboard-updates) | bbox [109, 272, 1824, 368] within card |
| PASS | No clipping: highlight "highlight 2" (s4:dashboard-updates) | bbox [109, 647, 1824, 818] within card |
| PASS | No clipping: chip "Overdue payments: 3 -> 2" (s4:dashboard-updates) | bbox [114, 819, 549, 990] within card |
| PASS | No clipping: chip "Overdue amount: $11,500.00 -> $4,000.00" (s4:dashboard-updates) | bbox [571, 819, 1368, 990] within card |
| PASS | No clipping: end_title "Premium Wedding Budget & Payment System" (s5:end-card) | bbox [169, 417, 1751, 507] within frame safe area |
| PASS | No clipping: end_subtitle "Budget • Vendor Payments • Cash Flow" (s5:end-card) | bbox [583, 626, 1335, 662] within frame safe area |
| PASS | No clipping: end_brand "LEDGER & LIME" (s5:end-card) | bbox [795, 919, 1122, 941] within frame safe area |
| PASS | Chips never cover a visible highlight (s3:balance-status-update) | checked every frame |
| PASS | Chips never cover a visible highlight (s4:dashboard-updates) | checked every frame |
| PASS | Readable dwell >= 0.6s: caption "See which payments are overdue." | fully visible 3.00s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.17s |
| PASS | Readable dwell >= 0.6s: caption "Log the final payment." | fully visible 2.53s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 1.57s |
| PASS | Readable dwell >= 0.6s: caption "Balance and status update themse" | fully visible 2.53s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.47s |
| PASS | Readable dwell >= 0.6s: chip "Catering balance: $7,500.00 -> $" | fully visible 1.63s |
| PASS | Readable dwell >= 0.6s: chip "Status: OVERDUE -> PAID IN FULL" | fully visible 1.43s |
| PASS | Readable dwell >= 0.6s: caption "See what’s paid — and what’s sti" | fully visible 2.57s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.50s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 2" | fully visible 2.50s |
| PASS | Readable dwell >= 0.6s: chip "Overdue payments: 3 -> 2" | fully visible 1.67s |
| PASS | Readable dwell >= 0.6s: chip "Overdue amount: $11,500.00 -> $4" | fully visible 1.47s |
| PASS | Readable dwell >= 0.6s: end_title "Premium Wedding Budget & Payment" | fully visible 2.37s |
| PASS | Caption rendered: "See which payments are overdue." |  |
| PASS | Caption rendered: "Log the final payment." |  |
| PASS | Caption rendered: "Balance and status update themselves." |  |
| PASS | Caption rendered: "See what’s paid — and what’s still owed." |  |
| PASS | Phone legibility (primary): caption "See which payments are overdue" | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "Log the final payment." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): highlight_label "Tasty Catering Co" | 56px -> 11.4px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "Balance and status update them" | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Catering balance: $7,500.00 ->" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Status: OVERDUE -> PAID IN FUL" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "See what’s paid — and what’s s" | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Overdue payments: 3 -> 2" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Overdue amount: $11,500.00 -> " | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): end_title "Premium Wedding Budget & Payme" | 88px -> 17.9px on a 390px phone (min 11.0) |
| PASS | Phone legibility (secondary): end_subtitle "Budget • Vendor Payments • Cas" | 38px -> 7.7px on a 390px phone (min 6.0) |
| PASS | Phone legibility (secondary): end_brand "LEDGER & LIME" | 30px -> 6.1px on a 390px phone (min 6.0) |
| PASS | Phone legibility (secondary): chip labels | 30px -> 6.1px |
| PASS | Source not over-upscaled (s1:before-overdue) | max upscale 1.0x, source px per output px 3.321-3.352 |
| PASS | Source not over-upscaled (s2:log-final-payment) | max upscale 1.0x, source px per output px 2.131-2.131 |
| PASS | Source not over-upscaled (s3:balance-status-update) | max upscale 1.0x, source px per output px 2.784-2.784 |
| PASS | Source not over-upscaled (s4:dashboard-updates) | max upscale 1.0x, source px per output px 3.321-3.352 |
| PASS | Required region fully in frame (scene 1 (before-overdue)) | scene 1 (before-overdue) region 1 [24, 24, 5643, 2001] stays fully in frame |
| PASS | Required region fully in frame (scene 2 (log-final-payment)) | scene 2 (log-final-payment) region 1 [2833, 24, 3724, 991] stays fully in frame |
| PASS | Required region fully in frame (scene 3 (balance-status-update)) | scene 3 (balance-status-update) region 1 [6557, 24, 4822, 991] stays fully in frame |
| PASS | Required region fully in frame (scene 4 (dashboard-updates)) | scene 4 (dashboard-updates) region 1 [24, 24, 5643, 2001] stays fully in frame |
| PASS | Product truth: before/after values verified against workbook | 14 value(s) verified against recalculated workbook cells |
| PASS | No rendered pointer presented as live capture | provenance.pointer_rendered = false |
| PASS | No compliance / legal claims in on-screen text | none found |
| PASS | Sources cleared for listing | source_status = product_capture |
| PASS | No internal / QA labels in any frame | OCR of 12 key frames: none found |

## OCR readback (text read from the encoded MP4)

| Time | Scene | Expected text | 1920px frame | 390px phone frame |
|---|---|---|---|---|
| 2.50s | before-overdue | See which payments are overdue | found | found |
| 2.50s | before-overdue | Overdue Payments | found | found |
| 2.50s | before-overdue | $11,500.00 | found | found |
| 5.60s | log-final-payment | Log the final payment | found | found |
| 5.60s | log-final-payment | $8,500.00 | found | found |
| 5.60s | log-final-payment | Total Paid To Date | found | found |
| 8.70s | balance-status-update | update themselves | found | found |
| 8.70s | balance-status-update | $0.00 | found | found |
| 8.70s | balance-status-update | PAID IN FULL | found | found |
| 11.70s | dashboard-updates | still owed | found | found |
| 11.70s | dashboard-updates | $11,300.00 | found | found |
| 11.70s | dashboard-updates | $4,000.00 | found | found |
| 14.50s | end-card | Wedding Budget | found | found |
| 14.50s | end-card | Vendor Payments | found | found |
| 14.50s | end-card | LEDGER | found | found |

Phone-frame OCR is a legibility proxy: spreadsheet cell text is expected to be too small at 390px; captions and value chips carry the message on phones.

## Mobile legibility (overlay text at 390px phone width)

| Element | Text | Render px | Phone px | Min |
|---|---|---|---|---|
| caption | See which payments are overdue. | 78 | 15.8 | 11.0 |
| caption | Log the final payment. | 78 | 15.8 | 11.0 |
| highlight_label | Tasty Catering Co | 56 | 11.4 | 11.0 |
| caption | Balance and status update themselves. | 78 | 15.8 | 11.0 |
| chip | Catering balance: $7,500.00 -> $0.00 | 60 | 12.2 | 11.0 |
| chip | Status: OVERDUE -> PAID IN FULL | 60 | 12.2 | 11.0 |
| caption | See what’s paid — and what’s still owed. | 78 | 15.8 | 11.0 |
| chip | Overdue payments: 3 -> 2 | 60 | 12.2 | 11.0 |
| chip | Overdue amount: $11,500.00 -> $4,000.00 | 60 | 12.2 | 11.0 |
| end_title | Premium Wedding Budget & Payment System | 88 | 17.9 | 11.0 |
| end_subtitle | Budget • Vendor Payments • Cash Flow | 38 | 7.7 | 6.0 |
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
