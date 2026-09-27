# VIDEO QA REPORT - Home Maintenance Planner & Service Log reusability-test

- **Verdict:** **NEEDS REVISION (technical QA passed; sources are stand-ins)**
- **Video:** `DUMMY-Home-Maintenance-Etsy-Video.mp4` - 1920x1080, 12.50s, h264 High, yuv420p, 30/1 fps, 6.02 MB
- **Config:** `configs/dummy_home_maintenance.json`
- **Generated:** 2026-09-27 10:02 UTC by `render_video.py` (automated)
- **Checks:** 82 pass, 1 warn, 0 fail

## Source provenance (product truth)

- `source_status`: **dummy**
- Rendered pointer shown: **no**
- Notes: Engine reusability test only - not a Ledger & Lime listing. Formula-driven workbook built by sources/dummy-home-maintenance/workbook/build_workbook.py, captured after each typed cell; the input clip is those real captured states in sequence (tools/stills_to_clip.py).

> **Not for Etsy.** The sources are not captures of the shipping product, so every frame carries a DRAFT tag. Capture the real workbook in the same before/after states, update `sources` and crop/rect coordinates, set `source_status` to `product_capture`, and re-run the same command.

| Truth key | Before | After |
|---|---|---|
| overdue | 3 | 2 |
| hvac_status | Overdue | Scheduled |
| on_schedule | 75% | 83% |
- truth verified: before.overdue = '3' (Plan!A5)
- truth verified: before.hvac_status = 'Overdue' (Plan!F7)
- truth verified: before.on_schedule = '75%' (Plan!E5)
- truth verified: after.overdue = '2' (Plan!A5)
- truth verified: after.hvac_status = 'Scheduled' (Plan!F7)
- truth verified: after.on_schedule = '83%' (Plan!E5)

## Timeline

| # | Scene | Type | Start | End | Caption |
|---|---|---|---|---|---|
| 1 | overdue-before | screen | 0.00s | 3.00s | Spot what is overdue. |
| 2 | log-service | screen | 3.00s | 6.50s | Record the service. |
| 3 | plan-updates | morph | 6.50s | 10.00s | The plan reschedules itself. |
| 4 | end-card | end_card | 10.00s | 12.50s | - |

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
| PASS | Duration matches timeline | 12.500s (expected 12.500s) |
| PASS | Duration within 10-15s | 12.50s |
| PASS | Etsy: <= 15 s (longer is trimmed) | 12.50s |
| PASS | Etsy: file < 100 MB | 6.02 MB |
| PASS | No audio track (Etsy plays muted) | 0 audio stream(s) |
| PASS | Web fast-start (moov before mdat) | moov -> mdat |
| PASS | Full decode without errors | clean |
| PASS | Frame count | 375 decoded (expected 375) |
| PASS | No black frames (blackdetect) | none detected |
| PASS | Static holds > 1.5 s (informational) | none |
| PASS | First frame is a composed shot (not blank) | luma mean 228, stdev 53 |
| PASS | Mobile preview video written | mobile/mobile-preview-780w.mp4 |
| PASS | OCR readback @2.60s: "Spot what is overdue" | found in encoded frame |
| PASS | OCR readback @2.60s: "Overdue" | found in encoded frame |
| PASS | OCR readback @2.60s: "Past due" | found in encoded frame |
| PASS | OCR readback @6.20s: "Record the service" | found in encoded frame |
| PASS | OCR readback @6.20s: "2026-09-24" | found in encoded frame |
| PASS | OCR readback @6.20s: "$24" | found in encoded frame |
| PASS | OCR readback @9.70s: "reschedules itself" | found in encoded frame |
| PASS | OCR readback @9.70s: "Scheduled" | found in encoded frame |
| PASS | OCR readback @9.70s: "83%" | found in encoded frame |
| PASS | OCR readback @12.20s: "Home Maintenance Planner" | found in encoded frame |
| PASS | OCR readback @12.20s: "Service History" | found in encoded frame |
| PASS | Phone-size OCR: caption "Spot what is overdue." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "Record the service." | read back from a 390px-wide frame |
| PASS | Phone-size OCR: caption "The plan reschedules itself." | read back from a 390px-wide frame |
| PASS | No clipping: wordmark "LEDGER & LIME" (global) | bbox [1603, 92, 1835, 108] within frame safe area |
| PASS | No clipping: caption "Spot what is overdue." (s1:overdue-before) | bbox [85, 67, 734, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s1:overdue-before) | bbox [522, 236, 656, 353] within card |
| PASS | No clipping: highlight "highlight 2" (s1:overdue-before) | bbox [1549, 379, 1835, 470] within card |
| PASS | No clipping: highlight_label "Past due" (s1:overdue-before) | bbox [1261, 377, 1539, 472] within card |
| PASS | No clipping: caption "Record the service." (s2:log-service) | bbox [82, 67, 657, 126] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s2:log-service) | bbox [83, 757, 1570, 873] within card |
| PASS | No clipping: caption "The plan reschedules itself." (s3:plan-updates) | bbox [83, 67, 894, 146] within frame safe area |
| PASS | No clipping: highlight "highlight 1" (s3:plan-updates) | bbox [1470, 404, 1834, 536] within card |
| PASS | No clipping: highlight "highlight 2" (s3:plan-updates) | bbox [1278, 243, 1562, 378] within card |
| PASS | No clipping: chip "Overdue tasks: 3 -> 2" (s3:plan-updates) | bbox [177, 819, 535, 990] within card |
| PASS | No clipping: chip "HVAC filter: Overdue -> Scheduled" (s3:plan-updates) | bbox [557, 819, 1283, 990] within card |
| PASS | No clipping: chip "On schedule: 75% -> 83%" (s3:plan-updates) | bbox [1305, 819, 1742, 990] within card |
| PASS | No clipping: end_title "Home Maintenance Planner & Service Log" (s4:end-card) | bbox [221, 418, 1696, 507] within frame safe area |
| PASS | No clipping: end_subtitle "Tasks • Schedules • Service History" (s4:end-card) | bbox [616, 626, 1302, 662] within frame safe area |
| PASS | No clipping: end_brand "LEDGER & LIME" (s4:end-card) | bbox [795, 919, 1122, 941] within frame safe area |
| PASS | Chips never cover a visible highlight (s3:plan-updates) | checked every frame |
| PASS | Readable dwell >= 0.6s: caption "Spot what is overdue." | fully visible 3.20s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 2.47s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 2" | fully visible 1.97s |
| PASS | Readable dwell >= 0.6s: caption "Record the service." | fully visible 3.23s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 1.27s |
| PASS | Readable dwell >= 0.6s: caption "The plan reschedules itself." | fully visible 3.33s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 1" | fully visible 3.27s |
| PASS | Readable dwell >= 0.6s: highlight "highlight 2" | fully visible 2.07s |
| PASS | Readable dwell >= 0.6s: chip "Overdue tasks: 3 -> 2" | fully visible 1.93s |
| PASS | Readable dwell >= 0.6s: chip "HVAC filter: Overdue -> Schedule" | fully visible 1.77s |
| PASS | Readable dwell >= 0.6s: chip "On schedule: 75% -> 83%" | fully visible 1.63s |
| PASS | Readable dwell >= 0.6s: end_title "Home Maintenance Planner & Servi" | fully visible 1.87s |
| PASS | Caption rendered: "Spot what is overdue." |  |
| PASS | Caption rendered: "Record the service." |  |
| PASS | Caption rendered: "The plan reschedules itself." |  |
| PASS | Phone legibility (primary): caption "Spot what is overdue." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): highlight_label "Past due" | 56px -> 11.4px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "Record the service." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): caption "The plan reschedules itself." | 78px -> 15.8px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "Overdue tasks: 3 -> 2" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "HVAC filter: Overdue -> Schedu" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): chip "On schedule: 75% -> 83%" | 60px -> 12.2px on a 390px phone (min 11.0) |
| PASS | Phone legibility (primary): end_title "Home Maintenance Planner & Ser" | 88px -> 17.9px on a 390px phone (min 11.0) |
| PASS | Phone legibility (secondary): end_subtitle "Tasks • Schedules • Service Hi" | 38px -> 7.7px on a 390px phone (min 6.0) |
| PASS | Phone legibility (secondary): end_brand "LEDGER & LIME" | 30px -> 6.1px on a 390px phone (min 6.0) |
| PASS | Phone legibility (secondary): chip labels | 30px -> 6.1px |
| PASS | Source not over-upscaled (s1:overdue-before) | max upscale 1.0x, source px per output px 1.455-1.471 |
| PASS | Source not over-upscaled (s2:log-service) | max upscale 1.0x, source px per output px 1.051-1.322 |
| PASS | Source not over-upscaled (s3:plan-updates) | max upscale 1.0x, source px per output px 1.13-1.301 |
| PASS | Product truth: before/after values verified against workbook | 6 value(s) verified against recalculated workbook cells |
| PASS | No rendered pointer presented as live capture | provenance.pointer_rendered = false |
| PASS | No compliance / legal claims in on-screen text | none found |
| WARN | Sources are captures of the shipping product | source_status = dummy -> DRAFT watermark applied; replace sources before Etsy use |

## OCR readback (text read from the encoded MP4)

| Time | Scene | Expected text | 1920px frame | 390px phone frame |
|---|---|---|---|---|
| 2.60s | overdue-before | Spot what is overdue | found | found |
| 2.60s | overdue-before | Overdue | found | found |
| 2.60s | overdue-before | Past due | found | found |
| 6.20s | log-service | Record the service | found | found |
| 6.20s | log-service | 2026-09-24 | found | not legible |
| 6.20s | log-service | $24 | found | found |
| 9.70s | plan-updates | reschedules itself | found | found |
| 9.70s | plan-updates | Scheduled | found | found |
| 9.70s | plan-updates | 83% | found | found |
| 12.20s | end-card | Home Maintenance Planner | found | not legible |
| 12.20s | end-card | Service History | found | found |

Phone-frame OCR is a legibility proxy: spreadsheet cell text is expected to be too small at 390px; captions and value chips carry the message on phones.

## Mobile legibility (overlay text at 390px phone width)

| Element | Text | Render px | Phone px | Min |
|---|---|---|---|---|
| caption | Spot what is overdue. | 78 | 15.8 | 11.0 |
| highlight_label | Past due | 56 | 11.4 | 11.0 |
| caption | Record the service. | 78 | 15.8 | 11.0 |
| caption | The plan reschedules itself. | 78 | 15.8 | 11.0 |
| chip | Overdue tasks: 3 -> 2 | 60 | 12.2 | 11.0 |
| chip | HVAC filter: Overdue -> Scheduled | 60 | 12.2 | 11.0 |
| chip | On schedule: 75% -> 83% | 60 | 12.2 | 11.0 |
| end_title | Home Maintenance Planner & Service Log | 88 | 17.9 | 11.0 |
| end_subtitle | Tasks • Schedules • Service History | 38 | 7.7 | 6.0 |
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
