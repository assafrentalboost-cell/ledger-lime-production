# Ledger & Lime - Automated Etsy Video Engine V1

Status: **engine READY - Product #13 V3.3 FINAL rendered (QA PASS, owner-approved reconstruction captures)**
Date: 2026-09-27. Branch: `claude/wonderful-cray-aqbfyp`. Etsy was not touched.

## 1. What it is

`video-engine/` is a reusable, config-driven renderer for Etsy listing videos of interactive spreadsheet products. Adding a product needs only:

- source captures (screenshots or clips),
- crop coordinates (or text to locate by OCR),
- before and after values,
- captions, including the buyer-outcome text,
- the product title and end-card line,
- timing.

Then one command renders, QA-checks, and reports:

```
cd video-engine
python render_video.py configs/product13_iep_tracker.json
```

## 2. Cloud environment findings (2026-09-27)

| Tool | State at start | Action |
|---|---|---|
| FFmpeg / ffprobe | missing | **INSTALLED** via apt (6.1.1, libx264) |
| Python | 3.11 available | pip: pillow, openpyxl, numpy, fonttools |
| Node.js | v22 available | not needed |
| ImageMagick | missing | installed (6.9); not required by the engine |
| Remotion | not present | **not used** (see §4) |
| LibreOffice | core only (no Calc) | installed `libreoffice-calc`, used to recalculate workbooks and capture sheets |
| Tesseract | missing | installed (5.3.4), used for OCR readback and text locating |
| Fonts | system fonts only | Inter + Cormorant Garamond (SIL OFL) from npm `@fontsource` and bundled; GitHub raw is blocked by egress policy |
| Existing video scripts/assets | **repository was empty** | none reusable |
| Product #13 source assets | **not present in the repository or anywhere this session can reach** | built a formula-driven reconstruction (see §6) |

Everything is free and open-source. `video-engine/tools/setup_env.sh` reproduces the setup.

## 3. Standard video story (spreadsheet products)

| # | Beat | Scene type | Typical duration |
|---|---|---|---|
| 1 | Problem / before | `screen` on the BEFORE dashboard with highlights | 2.5 s |
| 2 | Real input / action | `morph` of input sheet before→after (the new row appears), or a `video` clip of stepwise captures | 3-3.5 s |
| 3 | Automatic change | `morph` of dashboard before→after in place, with highlights and value chips from `truth` | 3 s |
| 4 | Buyer outcome | `screen` on the AFTER dashboard with a count chip | 3 s |
| 5 | Branded end card (optional) | `end_card`: title, gold rule, feature line, LEDGER & LIME | 2.5-3 s |

Total length is 12-15 s. Etsy trims longer videos, so validation enforces `max_duration`.

## 4. Technical design

- **Compositor**: Python + Pillow composes every frame (1920x1080, 30 fps) and pipes raw RGB to FFmpeg.
  - Camera moves use sub-pixel affine resampling from a mip pyramid, with geometric zoom interpolation and cubic easing. The result is a smooth push/pan with no text shimmer.
  - Shapes are 4x supersampled with sub-pixel offsets, so rings glide rather than step.
- **Encode**: libx264 High 4.1, CRF 17, preset slow, yuv420p, BT.709 tags, `+faststart`, no audio.
- **Why not Remotion**: it would add a Node/Chromium render stack and a React template layer without improving this minimal-motion style. The Python compositor is one dependency-light process, deterministic, and records exact layout geometry for QA. Remotion stays an option for V2 if richer motion is ever wanted.
- **Why not Canva**: not required at any step. The brand template is `templates/ledger_lime.json`.

## 5. Brand template (`templates/ledger_lime.json`)

- **Colours**: navy `#14213D`, cream `#F6F1E7`, paper `#FBF8F2`, restrained gold `#B89B5E`, ink `#1B2433`.
- **Type**:
  - Captions: Cormorant Garamond SemiBold, 78 px.
  - UI and chips: Inter.
  - Wordmark: LEDGER & LIME, letter-spaced, gold.
- **Layout**: a cream canvas with the product in a rounded card (1760x840, soft navy shadow), the caption top-left, and the wordmark top-right.
- **Motion** (all timings in the template):
  - One slow camera move per scene.
  - 0.5 s dip-to-blank transitions between scenes (V3.2; never two tables at once).
  - Clean in-place cut for before→after (V3.2).
  - Highlights: a gold ring, with a paper wash dimming everything else.
  - Captions and chips fade and rise 14-16 px.
  - No bounces, zoom-blurs, spins, or fake UI.
- **End card**: navy background, cream serif title, a gold rule that grows from the centre, the feature line, and the brand line.

## 6. Product truth rules (enforced in code)

1. **Chip values come only from `truth.states`.** Free-typed numbers cannot reach the screen.
2. **Truth values are checked against the workbook.** `truth.verify` maps each truth key to a workbook cell, read from LibreOffice-recalculated values. A mismatch fails validation. For example, claiming 95% when the cell computes 90% is rejected; this was tested.
3. **No rendered pointer.** `provenance.pointer_rendered: true` fails validation.
4. **No compliance or legal claims.** Captions, titles, subtitles, labels, and chip labels are scanned (compliant, FERPA, HIPAA, IDEA, certified, guarantee, legal, …). A match fails validation and QA.
5. **Stand-in sources are watermarked.** If `source_status` is not `product_capture`, a DRAFT tag is burned into every frame and the verdict is capped at NEEDS REVISION.
6. **Fictional sample data is allowed**; fabricated behaviour is not. Every before/after pair must be real workbook states, and the capture tool guarantees this for .xlsx sources.

## 7. Automated QA (`qa/run_qa.py`)

All checks run on the encoded MP4 unless noted.

- **ffprobe**: container, H.264 High, 1920x1080, yuv420p, 30 fps, BT.709 tags, duration versus timeline (±1.5 frames), Etsy ≤ 15 s, < 100 MB, no audio, moov before mdat (fast-start).
- **Corruption**: a full decode must produce zero errors, and the decoded frame count must equal the expected count.
- **Black frames**: `blackdetect`. `freezedetect` is reported as information only (the end-card hold is expected).
- **Key frames**: the first frame (Etsy poster, which must not be blank), plus the middle and end of every scene and the last frame.
  - Output: `qa/contact-sheet.png`.
- **Mobile**:
  - Previews: a 780 px phone preview MP4 and `qa/mobile-contact-sheet.png` at a true 390 px phone width.
  - Geometric legibility: primary overlay text must be ≥ 11 px and secondary text ≥ 6 px at 390 px width.
  - Captions must still OCR-read at phone size.
- **OCR readback**: every `expect_text` phrase is read from frames extracted from the MP4. Gold highlight strokes are keyed out first, because Tesseract drops text inside closed boxes.
- **Layout** (from the render manifest, measured every frame):
  - Captions and end-card text stay inside the 3.5 % title-safe area.
  - Highlights, labels, and chips stay inside the card.
  - A chip never covers a visible highlight.
  - Captions, chips, and highlights each stay fully visible for ≥ 0.6 s.
  - Captions are actually rendered.
- **Source sharpness**: warns if the camera upscales a capture by more than 1.35x.
- **Report**: `VIDEO-QA-REPORT-*.md`, containing the verdict, provenance, truth table, timeline, every check, the OCR table, the legibility table, and a manual checklist.

**Left to a human** (listed in the report):
- pacing feel and brand tone,
- whether the highlight targets are the most persuasive,
- a final watch on a real phone.

## 7a. Etsy video requirements checked

MP4 · H.264 · ≤ 15 s · < 100 MB · 1080p · plays muted · fast-start. Etsy recommends 5-15 s; the engine default range is 12-15 s.

## 8. Product #13 - IEP Caseload & Goal Progress Tracker - Video V3

- **Output**: `video-engine/output/p13-iep-tracker/P13-IEP-Tracker-Etsy-Video-V3.mp4` (1920x1080, 15.00 s, 5.94 MB).
- **QA**: `video-engine/output/p13-iep-tracker/VIDEO-QA-REPORT-P13.md` records 93 pass, 0 fail, and 1 warning (stand-in sources).

| Time | Beat | On screen |
|---|---|---|
| 0:00-2.5 | Dashboard before | "See what needs attention." Rings on **Needs Attention = 2** and **No Recent Data** |
| 2.5-6.0 | Progress input | "Log progress once." The Progress Log gains one row (2026-09-24 · Mia T. · G-104 · 90%), ringed |
| 6.0-9.0 | Automatic change | "Updates automatically." The row dissolves in place from **60%** to **90%** and **No Recent Data** to **Improving**; chips read *Goal progress 60% → 90%* and *Status No Recent Data → Improving* |
| 9.0-12.0 | Dashboard after | "Know what needs attention next." Ring on **Needs Attention = 1**; chip reads *Needs attention 2 → 1* |
| 12.0-15.0 | End card | IEP Caseload & Goal Progress Tracker / Track Goals • Progress • Service Minutes / LEDGER & LIME |

- **No pointer.** The prior raw clips, which may have contained a rendered pointer, were not available and are not used.
- **No compliance claims.**

**Why the verdict is NEEDS REVISION:**

- The original Product #13 workbook and clips were not in this repository.
- V3 therefore uses a reconstruction workbook (`sources/p13-iep-tracker/workbook/build_workbook.py`). It implements the documented Product #13 behaviour with real formulas, and LibreOffice recalculates it.
- The six before/after values match the brief exactly and are verified cell-by-cell.
- However, the screens are not the shipping product's UI. Every frame carries a DRAFT tag.

**To finish:**

1. Capture the real Product #13 workbook in the same two states.
2. Replace the four PNGs in `sources/p13-iep-tracker/captures/`.
3. Adjust the rects if the layout differs (use `tools/locate.py`).
4. Set `source_status` to `product_capture`.
5. Re-run the same command.

## 8a. Product #13 - Video V3.1 FINAL (2026-09-27)

Owner-approved corrections to V3; the creative direction is unchanged.

- **Output:** `video-engine/output/p13-iep-tracker/P13-IEP-Tracker-Etsy-Video-V3.1-FINAL.mp4` (1920x1080, 15.00 s, 5.93 MB).
- **QA:** `video-engine/output/p13-iep-tracker/VIDEO-QA-REPORT-P13-V3.1.md` records **PASS: 100 pass, 0 warn, 0 fail**.

Changes from V3:

1. **Internal footer removed.** The DRAFT tag is now suppressed only by an explicit, recorded `provenance.listing_approval` (owner, date, note). A new QA check OCR-scans every key frame for internal labels (DRAFT, RECONSTRUCTION, NOT FOR LISTING, DUMMY, STAND-IN, INTERNAL); none were found.
2. **Privacy-safe identifiers.** STU-001 to STU-006 replace the name-style labels in the workbook, so the Dashboard and Progress Log captures were re-made. New QA checks:
   - no person-name patterns in any of the 313 workbook cell values or in any frame,
   - student IDs follow the safe `STU-###` format,
   - the IDs are visible on screen.
3. **Scene-2 ring re-centred.** The ring on the new Progress Log row sat about 20 px low and showed a gridline inside it. It now sits on the row's measured gridlines (y 1517-1613).
4. **QA fix.** Key-frame extraction now deletes any earlier file first, so a stale frame from a previous render can never be read back.

All values are unchanged and still verified against recalculated cells: 60% → 90%, No Recent Data → Improving, Needs Attention 2 → 1.

**Remaining owner confirmation:** the screens are still the formula-driven reconstruction, not a capture of the shipping file. Listing them relies on the owner's approval that they match the shipping Product #13 workbook (columns, status labels, KPI tile).

## 8b. Product #13 - Video V3.2 FINAL (2026-09-27)

V3.1 is the base. The only change is at template level, to transitions.

- **Output:** `video-engine/output/p13-iep-tracker/P13-IEP-Tracker-Etsy-Video-V3.2-FINAL.mp4` (1920x1080, 15.00 s, 5.42 MB).
- **QA:** `video-engine/output/p13-iep-tracker/VIDEO-QA-REPORT-P13-V3.2.md` records **PASS: 101 pass, 0 warn, 0 fail**.

Changes:

- `motion.scene_transition: "dip"`. Over the same 0.5 s (0.7 s into the end card), the outgoing scene fades fully to an empty card (or to the end card's navy) before the incoming scene fades in. Two tables, or a table and end-card text, are never on screen together.
- `motion.morph_style: "cut"`. Before→after is a clean in-place cut at the midpoint of the old dissolve window, so 60%/90% and No Recent Data/Improving never overlap.
- **New QA check:** "No ghosting: one spreadsheet state per frame". The renderer logs every frame where two table states would be composited, and QA fails on any.
- **New QA artifact:** `qa/transition-strip.png`, showing every 2nd frame around each cut and swap, extracted from the MP4.
- **OCR readback hardening:** each phrase is read from 3 adjacent frames, so single-frame codec noise can't flip a digit.

Unchanged: crops, STU IDs, 60% → 90%, No Recent Data → Improving, Needs Attention 2 → 1, typography, colours, highlights, scene timing, and the end card.

## 8c. Product #13 - Video V3.3 FINAL (2026-09-27)

V3.2 is the exact base, with one correction.

- **Output:** `video-engine/output/p13-iep-tracker/P13-IEP-Tracker-Etsy-Video-V3.3-FINAL.mp4` (1920x1080, 15.00 s, 5.32 MB).
- **QA:** `video-engine/output/p13-iep-tracker/VIDEO-QA-REPORT-P13-V3.3.md` records **PASS: 103 pass, 0 warn, 0 fail**.

The change:

- The Automatic Result → Final Dashboard transition is now a clean direct cut at exactly 9.00 s (`"transition": 0` on `buyer-outcome`). It replaces the dip that showed a blank white card for about 167 ms. This is a config change only; the engine and template are unchanged.
- A frame-by-frame diff against V3.2 shows only 8.80-9.17 s changed. Elsewhere the mean pixel difference is ≤ 0.19/255, i.e. encode noise.
- **New QA check:** blank-card intervals are measured on every decoded frame of the MP4. Any scene set to a clean cut (`transition: 0`) fails if a blank frame appears within 0.3 s of it.
- **Still present (not changed on request):** the 2.43 s (167 ms) and 5.93 s (133 ms) dips.

## 8d. Product #10 - Rental Property Spreadsheet V1 (2026-09-27)

- **Output:** `video-engine/output/p10-rental-property/`.
- **QA:** PASS, 104/0/0.
- **Source:** the real packaged workbook; see `LEDGER-LIME-VIDEO-UPGRADE-AUDIT-1-12.md`.

Engine / tooling changes (reusable, no renderer or template change):

- `tools/capture_workbook.py`: maps PDF pages to *visible* sheets only. Hidden sheets were previously mis-labelling captures.
- `engine/config.py`: `currency` / `currency0` truth formats matching Excel `"$"#,##0.00`.
- `qa/run_qa.py`:
  - global "No white flash" check (blank card > `qa.max_blank_ms`, default 100 ms);
  - `qa.privacy.require_ids_on_screen` option;
  - generic privacy labels.
- Environment: `fonts-crosextra-carlito` (metric-compatible Calibri) for faithful LibreOffice rendering of Calibri workbooks.

P10 V1.1 (framing only) adds reusable engine options:
- `canvas_pad` accepts `[left, top, right, bottom]`; config coordinates stay in source pixels.
- `must_show` validates that listed source regions (e.g. header rows) stay fully in frame for the whole camera move. It is reported in QA.

Note: under the new global white-flash check, a re-QA of P13 V3.3 would flag its two remaining approved dips (2.43 s 167 ms, 5.93 s 133 ms).

## 9. Reusability test - PASS

`configs/dummy_home_maintenance.json` covers a dummy product, "Home Maintenance Planner & Service Log". Compared with Product #13 it uses:

- a different title, labels, and values (Overdue 3 → 2; HVAC filter Overdue → Scheduled; On schedule 75% → 83%),
- different sources: its own formula workbook, plus a **video clip source** assembled from stepwise real captures,
- different timing (12.5 s, 4 scenes),
- OCR-located and labelled highlights,
- three centred chips.

It rendered through the same command with no engine changes specific to the product, and QA recorded 82 pass, 0 fail, and 1 warning (dummy sources).

## 10. Manual steps per future product

1. Capture BEFORE and AFTER states of the real workbook. Use `tools/capture_workbook.py` for .xlsx, or same-geometry screenshots for Google Sheets.
2. Copy `configs/example_product.json` and fill in the title, truth values, captions, end-card line, and timing.
3. Pick the crop and highlight coordinates, using `tools/locate.py` or `"find"`.
4. Run `python render_video.py configs/<product>.json`.
5. Review the QA report, contact sheet, and phone preview. Approve.
6. Upload to Etsy manually. The engine never publishes.

## 11. Known limits (V1)

- 16:9 1920x1080 only; vertical formats would need a second template.
- Google Sheets products need manual screenshots, because the capture tool handles .xlsx only.
- OCR can't judge persuasion or taste; a human review is still required.
- Spreadsheet cell text is small at phone size by nature, so captions and chips carry the message on mobile.

## 12. MASTER UPDATE REQUIRED

This session has no Google Drive connection, so the live Master could not be edited. Append the following:

> **2026-09-27 - Automated Etsy Video Engine V1 (cloud build)**
>
> **Engine**
> - READY. Stack: Python/Pillow compositor + FFmpeg + Tesseract. No Canva or Remotion dependency; $0 spent.
> - Repository: `ledger-lime-production`, branch `claude/wonderful-cray-aqbfyp`, folder `video-engine/`.
> - One command per product: `python render_video.py configs/<product>.json`. It validates, renders, encodes H.264 1080p MP4, runs QA, and writes a report.
>
> **Product truth, enforced in code**
> - Chip values come only from config truth, verified against LibreOffice-recalculated workbook cells.
> - A rendered pointer is rejected.
> - Compliance/legal words are rejected.
> - Stand-in sources are watermarked DRAFT.
>
> **P13 Video V3**
> - Rendered, 15.0 s: before (Needs Attention 2, No Recent Data) → one Progress Log entry → 60%→90%, No Recent Data→Improving → Needs Attention 1 → end card.
> - Technical QA: 93 pass / 0 fail.
> - Verdict: NEEDS REVISION. The original P13 workbook and clips were not in the cloud repo, so V3 uses a formula-driven reconstruction; the values are verified, but the screens are not the shipping product.
> - Next action: supply real P13 captures (before/after dashboard + progress log), then re-run the same command.
> - The P13 Etsy video was NOT replaced; nothing was published.
>
> **Reusability test**: PASS. A dummy "Home Maintenance Planner" rendered from config only.
>
> **Material finding**: prior P13 raw clips may contain a rendered pointer. V3 contains no pointer, and the engine now blocks presenting a rendered pointer as live capture.
