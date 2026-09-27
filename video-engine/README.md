# Ledger & Lime - Automated Etsy Video Engine (V1)

Config-driven renderer for 12-15 s Etsy listing videos of interactive spreadsheet products.
Stack: **Python + Pillow (compositing) + FFmpeg (encode/QA) + Tesseract (OCR checks)**.
There is no Canva or Remotion dependency, and no paid services are used.

```
python render_video.py configs/product13_iep_tracker.json
```

That single command:

1. **Validates** the config: schema, source files, crop bounds, text width, font glyph coverage, and total duration. It also enforces product truth (before/after values must match recalculated workbook cells) and rejects rendered pointers and compliance/legal claims.
2. **Renders** every frame: camera push/pan, before→after dissolve, highlights, value chips, captions, and the branded end card.
3. **Encodes** H.264 High / yuv420p / BT.709 / 30 fps / 1920x1080 / faststart MP4 with no audio (Etsy plays muted).
4. **Runs QA** on the encoded file: ffprobe, full decode, frame count, black-frame detection, OCR readback, clipping/occlusion checks, phone legibility, and Etsy limits.
5. **Writes QA artifacts**: `VIDEO-QA-REPORT-*.md`, a contact sheet, a phone-size contact sheet, a phone preview MP4, key frames, and `qa-results.json`.

Exit code: `0` = rendered and QA passed (verdict may be NEEDS REVISION for stand-in sources), `1` = config invalid, `2` = QA FAIL.

## Layout

```
video-engine/
  render_video.py            one-command entry point
  engine/                    config validation, compositor, sources, encoder, OCR helpers
  templates/ledger_lime.json brand tokens: colours, fonts, layout, type sizes, motion timings
  configs/                   one JSON per product (+ example_product.json template)
  sources/<product>/         captures (+ optional workbook builder / recalculated values)
  qa/run_qa.py               QA suite (also runnable standalone)
  tools/                     capture_workbook.py, locate.py, stills_to_clip.py, setup_env.sh
  assets/fonts/              Inter + Cormorant Garamond (SIL OFL, licences included)
  output/<product-id>/       final MP4, QA report, render manifest, qa/ artifacts
```

## Setup (once per machine)

```
bash tools/setup_env.sh      # apt: ffmpeg tesseract-ocr libreoffice-calc poppler-utils; pip: requirements.txt
```

## New product in 6 steps

1. **Capture the real workbook** in its BEFORE and AFTER states. The only difference between them should be one real input.
   - If you have the .xlsx, run `python tools/capture_workbook.py product.xlsx sources/pNN/captures --prefix before_ --dpi 400` once per state. LibreOffice recalculates every formula, exports each sheet as a PNG, and writes `*_recalculated.json`.
   - Otherwise, use screenshots taken at the same zoom and window size for both states. Before/after images must share geometry.
2. `cp configs/example_product.json configs/productNN_slug.json`.
3. Fill in `product`, `truth.states` (before/after values), `sources`, captions, and end-card text.
4. Find coordinates: `python tools/locate.py sources/pNN/captures/before_dashboard.png "Needs Attention" "No Recent Data"`, or use `"find": "text"` in a highlight to have the engine locate it by OCR.
5. `python render_video.py configs/productNN_slug.json --validate-only`, then iterate with `--draft` if needed.
6. `python render_video.py configs/productNN_slug.json`, then review `output/<id>/VIDEO-QA-REPORT-*.md` and `qa/contact-sheet.png`.

## Config reference (key fields)

| Field | Meaning |
|---|---|
| `provenance.source_status` | `product_capture` (real product), `reconstruction`, or `dummy`. Anything other than `product_capture` gets a DRAFT tag burned in and a NEEDS REVISION verdict. |
| `provenance.listing_approval` | `{"approved": true, "by", "date", "note"}`: the owner's recorded approval to list non-`product_capture` sources. Removes the DRAFT tag (not allowed for `dummy`). |
| `qa.privacy` | `{"id_pattern": "STU-\\d{3}", "source_values": [recalculated json...]}`: fails QA on person-name labels in workbook data or any frame, and checks that safe IDs are used. |
| `provenance.pointer_rendered` | Must be `false`. A rendered pointer is never shown as live capture. |
| `truth.states.before/after` | The only source of numbers/states shown in value chips. |
| `truth.verify` | Maps truth keys to workbook cells in `*_recalculated.json`. Any mismatch fails validation. |
| `sources.<id>` | `{"path": ...}` for an image, or `{"path": ..., "type": "video", "in": 0}` for a clip. |
| `scenes[].type` | `screen` (one source), `morph` (before→after dissolve on identical geometry), or `end_card`. |
| `scenes[].camera.from/to` | `[x, y, w, h]` crop in source pixels. Eased push/pan; aspect is auto-fitted. |
| `scenes[].highlights[]` | `rect` or `find` (+`expand`, `occurrence`), `appear`, optional `pad`, `label`, `label_side`. |
| `scenes[].chips[]` | `truth_key`, `anchor` (`bottom-left`, `bottom-right`, `bottom-center`, `top-*`), `appear`. |
| `scenes[].canvas_pad` | `[right, bottom]` or `[left, top, right, bottom]` white margin, so the camera can frame past the capture edge. Coordinates stay in source pixels. |
| `scenes[].must_show` | `[[x, y, w, h], ...]` source regions (e.g. a header row) that must stay fully in frame for the whole camera move. Validation fails otherwise. |
| `scenes[].expect_text[]` | `{"at": seconds, "text": [...]}`: QA OCR-reads these from the encoded MP4. |
| `scenes[].transition` | Crossfade seconds into this scene (template default 0.5). |

## Commands

```
python render_video.py configs/product13_iep_tracker.json            # Product #13 V3
python render_video.py configs/dummy_home_maintenance.json           # reusability test
python render_video.py configs/<new>.json --validate-only            # check a config
python render_video.py configs/<new>.json --draft                    # fast encode while iterating
python qa/run_qa.py configs/<new>.json                               # re-run QA on an existing render
python tools/locate.py <capture.png> "text" ["text" ...]             # coordinates for crops/highlights
python tools/capture_workbook.py <book.xlsx> <out_dir> --prefix before_ --dpi 400
python tools/stills_to_clip.py <out.mp4> s0.png s1.png s2.png --hold 0.7 0.6 1.5
```

See `../LEDGER-LIME-AUTOMATED-ETSY-VIDEO-ENGINE-V1.md` for the design, rules, and QA definitions.
