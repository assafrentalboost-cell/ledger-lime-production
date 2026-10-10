# MASTER + DECISION LOG APPEND — 2026-10-10 — PRODUCT #20 FINAL BUILD GATE

> **Append only, to the SAME live Master and Decision Log. Keep all prior history.** Neither file is in the repo, so Business HQ must paste this in.
>
> All figures: **EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA**.
> Evidence: `research/product-20-wedding-website/`.

## Decision Log entry

| Date | Item | Decision | Reason |
|---|---|---|---|
| 2026-10-10 | #20 Elegant Wedding Website & Matching Digital Invitation Kit (Canva) | **HOLD** | The market passes. The pre-build standard cannot be met: the Canva connector is unauthorized; canva.com, my.canva.site and etsy.com are 403 in the build environment; official Insights is missing; there is no hands-on competitor teardown. Nothing was built, and there was no Etsy draft. |

## Master: material findings

- **Market:**
  - 37 couple-facing wedding-website SKUs with ≥100 units: 23 shops, 8,317 units in 12 months.
  - Median price $29.99; unit-weighted $26.28. 47% of units at $30–40, 3% under $10.
- **Entry:**
  - Young shops (≤24 months) are 15 of 23 shops and hold 81% of units, so the shop-authority barrier is low.
  - Rising new entrants: OleInkandCo ($35.05, 215), VeiledHaus ($15.87, 149, shop 5 months old), TheMoonveilAU ($25.10, 117, shop 4 months old).
- **Leaders:**
  - STUDIOGWYN: 1,819 units over 4 SKUs, shop 13 months old.
  - Oct19CreativeStudio: a premium SKU at $47.09 sold 210.
  - Top shop 22% of units; top three 48%.
- **Fashion cycle (contradiction kept):** EleventhEdit (1,179 units, 26 in the last 3 months), EasyAisleStudio (722, 30) and Rosie 4360112610 (149 → 0) faded within about 6 months. The product needs a multi-colourway catalog.
- **Search (EverBee proxy, not Insights):**
  - "wedding website templates" 656 searches, 10.6k competing listings
  - "canva template wedding websites" 613, 6.5k
  - "wedding website invitation template canva" 552, 5.2k
  - "canva wedding website template with rsvp" 280
  - "digital wedding invitation" family about 870–996, but 116k–253k competing listings (flooded; secondary wording only)
- **Canva rules (secondary sources; primary page blocked):**
  - Pro-content templates may be sold only as template links.
  - Free accounts publish to my.canva.site: 5 sites, and ≤10 sections per page at publish.
  - A custom domain needs Pro.
  - RSVP is not native to Canva; sellers use a Google Form or Jotform embed or link.
- **Proposed mechanism:** "The RSVP that counts itself." The website's RSVP feeds a Google Form, which fills an L&L count sheet (attending, meals, unanswered guests). Uniqueness is unverified.
- **Proposed price:** list $32 (≈ ₪119), about $24 / ₪89 effective at 25% off.
- **Brand-fit risk kept:** this is design-led and fashion-cycle. Entrant-first V2 rejected wedding-couple doors as design-led. The #20 selection is preserved, not reopened.

## HOLD-clearing gates

- **H1:** authorize the Canva connector, or Assaf builds in Canva.
- **H2:** official Insights on 7 wedding-website terms.
- **H3:** read Canva's license and Websites help primary text.
- **H4:** phone teardown of 5 competitor demos, including whether any ships an RSVP tally.
- **H5:** free-account prototype published to my.canva.site and tested on iOS and Android.
- **H6:** at least 3 colourways at launch.

**Decision rule:**
- **BUILD** if H1–H5 pass and no competitor ships a tally.
- **REFRAME** to an RSVP Count Sheet add-on if a competitor does.
- **REJECT** if template-link resale is not permitted.

## Closing lines

- PRODUCT #20 = HOLD
- No Etsy writes, ads or spend.
