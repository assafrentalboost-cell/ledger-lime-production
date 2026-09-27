# VIDEO QA REPORT - IEP Caseload & Goal Progress Tracker V3.1 FINAL

- **Verdict:** **PASS (owner-approved reconstruction captures)**
- **Video:** `P13-IEP-Tracker-Etsy-Video-V3.1-FINAL.mp4` - 1920x1080, 15.00s, h264 High, yuv420p, 30/1 fps, 5.93 MB
- **Config:** `configs/product13_iep_tracker.json`
- **Generated:** 2026-09-27 11:28 UTC by `render_video.py` (automated)
- **Checks:** 100 pass, 0 warn, 0 fail

## Source provenance (product truth)

- `source_status`: **reconstruction**
- Rendered pointer shown: **no**
- Notes: Original Product #13 workbook / raw clips were not in the repository. Captures are from a reconstruction workbook (sources/p13-iep-tracker/workbook/build_workbook.py) whose values are produced by real formulas recalculated in LibreOffice. The only change between states is ONE appended Progress Log row. No pointer is shown. Students appear only as privacy-safe identifiers (STU-001...STU-006).
- Listing approval: **approved by Assaf (owner) on 2026-09-27** - V3 creative direction approved; owner requested V3.1/FINAL without internal labels and with privacy-safe identifiers.

| Truth key | Before | After |
|---|---|---|
| latest_progress | 60% | 90% |
| status | No Recent Data | Improving |
| needs_attention | 2 | 1 |
- truth verified: before.latest_progress = '60%' (Dashboard!G13)
- truth verified: before.status = 'No Recent Data' (Dashboard!J13)
- truth verified: before.needs_attention = '2' (Dashboard!E6)
- truth verified: after.latest_progress = '90%' (Dashboard!G13)
- truth verified: after.status = 'Improving' (Dashboard!J13)
- truth verified: after.needs_attention = '1' (Dashboard!E6)

## Timeline

| # | Scene | Type | Start | End | Caption |
|---|---|---|---|---|---|
| 1 | problem-before | screen | 0.00s | 2.50s | See what needs attention. |
| 2 | real-input | morph | 2.50s | 6.00s | Log progress once. |
| 3 | automatic-change | morph | 6.00s | 9.00s | Updates automatically. |
| 4 | buyer-outcome | screen | 9.00s | 12.00s | Know what needs attention next. |
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
| PASS | Etsy: file < 100 MB | 5.93 MB |
| PASS | No audio track (Etsy plays muted) | 0 audio stream(s) |
| PASS | Web fast-start (moov before mdat) | moov -> mdat |
| PASS | Full decode without errors | clean |
| PASS | Frame count | 450 decoded (expected 450) |
| PASS | No black frames (blackdetect) | none detected |
| PASS | Static holds > 1.5 s (informational) | 13.13s (end card hold is expected) |
| PASS | First frame is a composed shot (not blank) | luma mean 223, stdev 63 |
| PASS | Mobile preview video written | mobile/mobile-preview-780w.mp4 |
| PASS | OCR readback @2.10s: "See what needs attention" | found in encoded frame |
| PASS | OCR readback @2.10s: "Needs Attention" | found in encoded frame |
| PASS | OCR readback @2.10s: "No Recent Data" | found in encoded frame |
| PASS | OCR readback @5.60s: "Log progress once" | found in encoded frame |
| PASS | OCR readback @5.60s: "2026-09-24" | found in encoded frame |
| PASS | OCR readback @5.60s: "STU-004" | found in encoded frame |
| PASS | OCR readback @5.60s: "90%" | found in encoded frame |
| PASS | OCR readback @8.80s: "Updates automatically" | found in encoded frame |
| PASS | OCR readback @8.80s: "Improving" | found in encoded frame |
| PASS | OCR readback @8.80s: "90%" | found in encoded frame |
| PASS | OCR readback @11.70s: "Know what needs attention next" | found in encoded frame |
| PASS | OCR readback @11.70s: "Needs Attention" | found in encoded frame |
| PASS | OCR readback @14.50s: "IEP Caseload" | found in encoded frame |
| PASS | OCR readback @14.50s: "Goal Progress Tracker" | found in encoded frame |
| PASS | OCR readback @14.50s: "Service Minutes" | found in encoded frame |
| PASS | OCR readback @14.50s: "LEDGER" | found in encoded frame |
| PASS | Phone-size OCR: caption "See what needs attention." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "Log progress once." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "Updates automatically." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "Know what needs attention next." | read back from a 390px-wide frame |
| PASS | No clipping: wordmark "LEDGER & LIME" (global) | bbox [1603, 92, 1835, 108] within frame safe area |
| PASS | No clipping: caption "See what needs attention." (s1:problem-before) | bbox [85, 67, 858, 126] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s1:problem-before) | bbox [230, 189, 635, 408] within card |
| PASS | No clipping: highlight "No Recent Data" (s1:problem-before) | bbox [1449, 794, 1832, 899] within card |
| PASS | No clipping: caption "Log progress once." (s2:real-input) | bbox [81, 75, 642, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s2:real-input) | bbox [90, 708, 1823, 843] within card |
| PASS | No clipping: caption "Updates automatically." (s3:automatic-change) | bbox [81, 67, 774, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s3:automatic-change) | bbox [99, 618, 449, 837] within card |
| PASS | No clipping: highlight "highlight 2" (s3:automatic-change) | bbox [1307, 618, 1831, 837] within card |
| PASS | No clipping: chip "Goal progress: 60% -> 90%" (s3:automatic-change) | bbox [114, 819, 560, 990] within card |
| PASS | No clipping: chip "Status: No Recent Data -> Improving" (s3:automatic-change) | bbox [582, 819, 1491, 990] within card |
| PASS | No clipping: caption "Know what needs attention next." (s4:buyer-outcome) | bbox [81, 67, 1087, 126] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s4:buyer-outcome) | bbox [232, 190, 637, 409] within card |
| PASS | No clipping: chip "Needs attention: 2 -> 1" (s4:buyer-outcome) | bbox [114, 819, 508, 990] within card |
| PASS | No clipping: end_title "IEP Caseload & Goal Progress Tracker" (s5:end-card) | bbox [299, 417, 1619, 507] within frame safe area |
| PASS | No clipping: end_subtitle "Track Goals • Progress • Service Minutes" (s5:end-card) | bbox [565, 626, 1352, 662] within frame safe area |
| PASS | No clipping: end_brand "LEDGER & LIME" (s5:end-card) | bbox [795, 919, 1122, 941] within frame safe area |
| PASS | Chips never cover a visible highlight (s3:automatic-change) | checked every frame |
| PASS | Chips never cover a visible highlight (s4:buyer-outcome) | checked every frame |
| PASS | Readable dwell >= 0.6s: caption "See what needs attention." | fully visible 2.77s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.10s |
| PASS | Readable dwell >= 0.6s: highlight "No Recent Data" | fully visible 1.73s |
| PASS | Readable dwell >= 0.6s: caption "Log progress once." | fully visible 3.30s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 1.83s |
| PASS | Readable dwell >= 0.6s: caption "Updates automatically." | fully visible 2.80s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.63s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 2" | fully visible 2.63s |
| PASS | Readable dwell >= 0.6s: chip "Goal progress: 60% -> 90%" | fully visible 1.40s |
| PASS | Readable dwell >= 0.6s: chip "Status: No Recent Data -> Improv" | fully visible 1.20s |
| PASS | Readable dwell >= 0.6s: caption "Know what needs attention next." | fully visible 2.90s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.63s |
| PASS | Readable dwell >= 0.6s: chip "Needs attention: 2 -> 1" | fully visible 2.20s |
| PASS | Readable dwell >= 0.6s: end_title "IEP Caseload & Goal Progress Tra" | fully visible 2.37s |
| PASS | Caption rendered: "See what needs attention." |  |
| PASS | Caption rendered: "Log progress once." |  |
| PASS | Caption rendered: "Updates automatically." |  |
| PASS | Caption rendered: "Know what needs attention next." |  |
| PASS | Phone legibility (primary): caption "See what needs attention." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "Log progress once." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "Updates automatically." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Goal progress: 60% -> 90%" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Status: No Recent Data -> Impr" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "Know what needs attention next" | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Needs attention: 2 -> 1" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): end_title "IEP Caseload & Goal Progress T" | 88px -> 17.9px on a 390px phone (min 11.0) |
| PASS | Phone legibility (secondary): end_subtitle "Track Goals • Progress • Servi" | 38px -> 7.7px on a 390px phone (min 6.0) |
| PASS | Phone legibility (secondary): end_brand "LEDGER & LIME" | 30px -> 6.1px on a 390px phone (min 6.0) |
| PASS | Phone legibility (secondary): chip labels | 30px -> 6.1px |
| PASS | Source not over-upscaled (s1:problem-before) | max upscale 1.0x, source px per output px 1.446-1.477 |
| PASS | Source not over-upscaled (s2:real-input) | max upscale 1.0x, source px per output px 1.375-1.676 |
| PASS | Source not over-upscaled (s3:automatic-change) | max upscale 1.0x, source px per output px 1.062-1.108 |
| PASS | Source not over-upscaled (s4:buyer-outcome) | max upscale 1.0x, source px per output px 1.446-1.477 |
| PASS | Product truth: before/after values verified against workbook | 6 value(s) verified against recalculated workbook cells |
| PASS | No rendered pointer presented as live capture | provenance.pointer_rendered = false |
| PASS | No compliance / legal claims in on-screen text | none found |
| PASS | Sources cleared for listing | source_status = reconstruction; listing approved by Assaf (owner) on 2026-09-27: V3 creative direction approved; owner requested V3.1/FINAL without internal labels and with privacy-safe identifiers. |
| PASS | No internal / QA labels in any frame | OCR of 12 key frames: none found |
| PASS | Privacy: no person-name labels in workbook data | 313 cell values scanned |
| PASS | Privacy: student identifiers use the safe ID format | STU-001, STU-002, STU-003, STU-004, STU-005, STU-006 |
| PASS | Privacy: no person-name labels in any frame (OCR) | 12 key frames scanned |
| PASS | Privacy: safe identifiers visible on screen | STU-002, STU-004, STU-005, STU-006 |

## OCR readback (text read from the encoded MP4)

| Time | Scene | Expected text | 1920px frame | 390px phone frame |
|---|---|---|---|---|
| 2.10s | problem-before | See what needs attention | found | found |
| 2.10s | problem-before | Needs Attention | found | found |
| 2.10s | problem-before | No Recent Data | found | not legible |
| 5.60s | real-input | Log progress once | found | found |
| 5.60s | real-input | 2026-09-24 | found | found |
| 5.60s | real-input | STU-004 | found | found |
| 5.60s | real-input | 90% | found | not legible |
| 8.80s | automatic-change | Updates automatically | found | found |
| 8.80s | automatic-change | Improving | found | found |
| 8.80s | automatic-change | 90% | found | found |
| 11.70s | buyer-outcome | Know what needs attention next | found | found |
| 11.70s | buyer-outcome | Needs Attention | found | found |
| 14.50s | end-card | IEP Caseload | found | found |
| 14.50s | end-card | Goal Progress Tracker | found | found |
| 14.50s | end-card | Service Minutes | found | found |
| 14.50s | end-card | LEDGER | found | found |

Phone-frame OCR is a legibility proxy: spreadsheet cell text is expected to be too small at 390px; captions and value chips carry the message on phones.

## Mobile legibility (overlay text at 390px phone width)

| Element | Text | Render px | Phone px | Min |
|---|---|---|---|---|
| caption | See what needs attention. | 78 | 15.8 | 11.0 |
| caption | Log progress once. | 78 | 15.8 | 11.0 |
| caption | Updates automatically. | 78 | 15.8 | 11.0 |
| chip | Goal progress: 60% -> 90% | 60 | 12.2 | 11.0 |
| chip | Status: No Recent Data -> Improving | 60 | 12.2 | 11.0 |
| caption | Know what needs attention next. | 78 | 15.8 | 11.0 |
| chip | Needs attention: 2 -> 1 | 60 | 12.2 | 11.0 |
| end_title | IEP Caseload & Goal Progress Tracker | 88 | 17.9 | 11.0 |
| end_subtitle | Track Goals • Progress • Service Minutes | 38 | 7.7 | 6.0 |
| end_brand | LEDGER & LIME | 30 | 6.1 | 6.0 |

## Artifacts

- Contact sheet: `qa/contact-sheet.png`
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
