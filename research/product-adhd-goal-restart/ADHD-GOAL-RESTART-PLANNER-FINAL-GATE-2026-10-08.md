# FINAL PRODUCT GATE — ADHD Goal & Restart Planner — 2026-10-08

> Every sales, units, review and keyword figure here is an **EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA**.
> I did not build anything, change Etsy, publish, run ads or spend money.
> This gate does **not** inherit BUILD approval from the department selection (ADHD Adult Life Admin, confidence MEDIUM).

## Verdict

**PRODUCT = HOLD / VALIDATION INCOMPLETE**

The product idea survives the fatal checks. It is not a generic planner with "ADHD" added, and it is not a clone of the listings I could see. But five critical gaps remain, and any of them could reverse a BUILD (§15). The biggest is that I could not open the one listing that proves this job (NeurodivergentHQ 4440940588). Etsy returned 403, so I could not check whether it already ships the full restart mechanism, and I could not read any buyer reviews. Official Marketplace Insights was also not run.

## What I could and could not read

| Required input | Status |
|---|---|
| Live Master | **NOT IN REPO.** Not read. This gate goes to an append file (`MASTER-APPEND-2026-10-08-ADHD-GOAL-RESTART.md`). |
| Astra final department decision | **NOT IN REPO.** Not read. |
| ADHD source pack | Read: `research/entrant-first/astra-pack/` (CSVs and README). |
| #6 ADHD Budget history | Read: catalog map in `research/product-19/PRODUCT-19-FINAL-GATE.md`. #6's primary door is "adhd budget". |
| ADHD competitor evidence | Read: astra-pack, plus 9 new EverBee pulls (`raw/`). |
| Etsy listing pages and reviews | **403.** No review text, page counts or complaints were readable. |
| Official Marketplace Insights | **NOT ACCESSIBLE** to me (it is UI-only). Assaf must run it manually (V1 below). |

## 1. Marketplace Insights

Official Insights was **not run**; it is required manual task V1. The table below is an EverBee keyword **proxy** only (`raw/K-adhd-goal-planner.json`). It is not Etsy search data.

| Term (EverBee) | Volume | Competition | Note |
|---|---|---|---|
| adhd goal planner | 545 | 5,664 | Biggest head term; crowded |
| **adhd goal setting planner** | **385** | **1,949** | Best volume-to-competition ratio. The anchor's tags use "goal setting pdf". |
| digital goal planner adhd | 342 | 3,474 | Tablet/Notion intent; wrong format for us |
| adhd goal setting digital planner | 257 | 1,296 | |
| adhd goal planner printable | 117 | 2,637 | Format-matching long tail |

On secondary terms:
- **adhd reset planner:** listing pulls show 25+ listings with "ADHD … reset". Nearly all are about cleaning, rooms, mornings or overwhelm, not goals. In EverBee, "reset" means cleaning or brain-dump.
- **adhd productivity planner:** dominated by old all-in-one planners (PlannerGate, SapphireCreationsAU).
- **adhd goal tracker:** dominated by Google Sheets habit trackers.
- None of these justify a separate door yet.

**Provisional primary door: "adhd goal setting planner".** Insights must confirm it.

## 2. Exact competitors

Full table: `COMPETITORS.csv`, built by `competitors.py` from `raw/`. Format, mechanism and hero are read from **titles only**. Page count and complaints are **UNVERIFIED (403)**. Units are the last 12 months. Status follows the entrant rule from `research/entrant-first`.

| # | Listing | Shop | Shop age / sales | Listing age | Price | 12-mo units | Trend (12 mo) | Reviews | Format | Mechanism (title) | ADHD | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 4440940588 | NeurodivergentHQ | 10 mo / 558 | 8 mo | $15.00 (shows ~$9.90 on sale) | 379 | 0 0 0 0 2 128 26 70 93 6 14 40 | 28 | Fillable A4 PDF | Undated "Start Anytime" goal workbook; tags: anti-shame, energy audit, life audit | NATIVE | **CLEAN** |
| 2 | 4372860145 | DragonHoardTemplates | 14 mo / 177 | 13 mo | $29.99 | 145 | 5 7 13 15 10 8 22 27 14 10 6 8 | 13 | Notion | Gamified RPG life OS | ADAPTED | CLEAN (numeric) |
| 3 | 4399348526 | Templix8 | 13 mo / 4,727 | 11 mo | $3.96 | 255 | 0 0 17 0 17 0 17 51 82 37 17 17 | 15 | Printable PDF | Brain dump, task tracker, time-blocking bundle | ADAPTED | CLEAN (numeric) |
| 4 | 4338845135 | YourColorfulJourney | 31 mo / 8,640 | 15 mo | $11.16 | 505 | 48 59 73 92 44 25 32 27 32 27 22 24 | 24 | Fillable PDF | Multi-topic executive-function workbook bundle | NATIVE | WEAK (shop age) |
| 5 | 4525115768 | PaperoxStd | 19 mo / 17,485 | 4 mo | $14.98 | 238 | … 4 64 14 156 | 7 | Printable PDF | ADHD planner + EF worksheets | ADAPTED | WEAK (shop size) |
| 6 | 1331622566 | FutureADHD | 122 mo / 60,752 | 47 mo | $24.33 | 235 | 38 54 58 55 6 8 8 2 2 3 0 1 (fading) | 409 | Tablet planner | Dated planner + goal/habit tracker | ADAPTED | WEAK |
| 7 | 4333479096 | SelfEmbark | 57 mo / 8,506 | 15 mo | $7.00 | 96 | 0 16 32 0 12 0 0 36 0 0 0 0 | 20 | PDF workbook | Life systems: prep, flow, follow-through | NATIVE | NONE |
| 8 | 4538664912 | PsychBlueprints | 18 mo / 493 | 3 mo | $8.36 | 70 | single month 70 | 1 | Excel | Life system: habits, goals, time | ADAPTED | NONE |
| 9 | 4519215685 | TheEditReadyStudio | 7 mo / 1,513 | 4 mo | $6.00 | 19 | … 1 9 9 0 | 2 | PDF | Shutdown/burnout recovery sheet | NATIVE | NONE |
| 10 | 4523178000 | JiarnaDigital | 5 mo / 1,130 | 4 mo | $4.04 | 15 | … 10 3 2 | 1 | Printable PDF | "ADHD Reset Planner", mental declutter | NATIVE | NONE |
| 11 | 4521017598 | JiarnaDigital | 5 mo / 1,130 | 4 mo | $4.04 | 10 | … 1 4 4 1 | 1 | Printable PDF | Low-energy / burnout day planner | NATIVE | NONE |
| 12 | 1751200137 | plannwander | 39 mo / 395 | 28 mo | $26.00 | 12 | fading | 11 | Printable PDF | Gamified goal quest | ADAPTED | NONE |
| 13 | 4474225910 | FocusFlowDegi | 6 mo / 5 | 1 mo | $6.70 | 5 | — | 1 | PDF | "Shame-free" ADHD goal-setting planner | NATIVE | NONE |
| 14 | 4495991824 | TemplateVaultHub | 0 mo / 0 | 1 mo | $5.84 | 0 | — | 0 | Printable PDF | ADHD goal-setting planner | ADAPTED | NONE |
| 15 | 1807870237 | PlannersByBee | 46 mo / 25,627 | 7 mo | $5.94 | 0 | — | 0 | Printable | Weekly goal planner | BOLT-ON | NONE |

**Substitutes** (generic or bolt-on planners that win the same search door at scale):
- SapphireCreationsAU 1782173723: $5.21, 744 units, 206 reviews.
- Digicarft 1344352293: $16.99, 1,658 units, 393 reviews.

**What the table says:**
- Only 6 of 15 exact-job listings sold ≥100 units.
- The only ADHD-NATIVE listing that is also CLEAN and sells at scale is the anchor.
- New "reset", "low-energy" and "shame-free" goal sheets from young shops (#9–#14) sell 0–19 units. Copycats are arriving and are not winning yet.

## 3. Second clean entrant: **WEAK → SECOND CLEAN ENTRANT = NO**

- **Against "NO":** two listings pass the numeric CLEAN rule.
  - **DragonHoardTemplates:** a Notion gamified **Life OS** at $29.99. That is the format and scope this product explicitly excludes.
  - **Templix8:** a $3.96 brain-dump/time-blocking bundle. Its "reset" is overwhelm triage, not goal restart. Its trend in steps of 17 is an EverBee step artifact, and it is a high-SKU shop (4,727 sales).
- **Neither does this job.** Neither is "one goal → next action → low-energy fallback → restart" in a fillable or printable PDF.
- **Result:** the exact job has one clean proof (the anchor) and a WEAK second.
- **Confidence downgraded but not auto-rejected,** as the brief requires.
- **The anchor itself is not smooth:**
  - 128 of its 379 units (34%) fall in one month.
  - Months 10–11 were 6 and 14.
  - Its price in EverBee is $15, but it displays ~$9.90 (sale).

## 4. Buyer language

- **REAL BUYER LANGUAGE: NONE CAPTURED.** Review pages are 403. The anchor's 28 reviews, YourColorfulJourney's 24 and SelfEmbark's 20 were not read. I am not inferring buyer words from seller copy.
- **SELLER ADHD MARKETING** (titles and tags; this is not buyer evidence):
  - "Start Anytime", "Undated", "anti shame planner", "energy audit", "flexible planning" (anchor)
  - "Shame-Free" (FocusFlowDegi)
  - "Low Energy", "Burnout Recovery", "Bare Minimum" (JiarnaDigital, InspiringCraftStore)
  - "Get Back on Track Fast" (SimpleFocusLabDesign)
  - "Prep, Flow & Follow-Through" (SelfEmbark)
- **Signal:** sellers are converging on restart/anti-shame framing, and only the anchor converts it at volume.
- **No clinical inference** is drawn.

## 5. Generic-planner test (fatal check): **PASSES, but specificity is MIXED**

Removing "ADHD" gives "Goal & Restart Planner". Is it the same product as a generic goal planner? **No.** Generic goal planners (SMART, yearly, vision board, 12-week year, habit streak) plan for a perfect run. This mechanism plans for the lapse.

But the mechanism is not exclusive to ADHD. It also fits burnout, chronic illness (spoonie) and depression-recovery buyers. So **ADHD-SPECIFICITY = MIXED**. This is not fatal, but the ADHD link must come from friction-specific UI ("too many pages = abandon", "missed a week = shame spiral"), not from claims.

| Mechanism part | Seen in a competitor title or tags? |
|---|---|
| One commitment | No title says "one goal". Every other listing is multi-goal or all-in-one. |
| Next action | Not in titles. Templix8/PaperoxStd use task breakdown (adjacent). |
| Low-energy fallback | Yes, as **standalone** day planners (JiarnaDigital, InspiringCraftStore, TheEditReadyStudio). Not attached to a goal. |
| Restart point | Anchor ("Start Anytime"), FocusFlowDegi ("shame-free"). Depth unknown. |
| No broken-streak logic | Anchor ("anti shame", "undated"). Unverified. |
| Review what changed | Not in titles. |
| Resume without rebuilding | Anchor (implied). Unverified. |

**The combination of all 7 was not seen in any title.** The anchor may cover 3–4 of them. It is the one listing that could already be this product, and it is unreadable (gap G2).

## 6. Wedge: "Plan for the restart, not just the perfect streak."

| Test | Result |
|---|---|
| Unique | **PROBABLE, UNVERIFIED.** No title combines goal + low-energy version + restart. The anchor's page structure is unknown. |
| Meaningful | **YES (logic).** The lapse is the moment existing planners lose the buyer. |
| Supported by buyers | **UNVERIFIED.** No review text was read (gap G3). |
| Visually demonstrable | **YES.** One card shows Goal / Next Action / Low-Energy Version / Status: RESTARTED, which reads in 2–3 seconds. |

## 7. Format: **Fillable + printable PDF (A4 + US Letter), one file each**

- **Support for this format:**
  - The anchor is a fillable A4 PDF.
  - YourColorfulJourney (505 units) is a fillable PDF.
  - Restart pages get reused, so printable matters.
- **Why not Sheets:** Sheets wins the "goal tracker" door only at $1–3 habit grids (ProductivePenguinCo, HeyMorning). That is a different job and a price war, so a spreadsheet is **not forced**.
- **Why not Notion:** Notion is DragonHoard's Life OS lane, which is excluded.
- **Gap:** the anchor is A4 only, so US Letter is a cheap edge.

## 8. Scope (if built): about 12–16 pages

| Section | Pages |
|---|---|
| Start Here | 1 |
| One Goal + Why It Matters | 1 |
| Next Action ladder | 1 |
| Low-Energy Version | 1 |
| Restart Plan | 1 |
| Weekly Check-In | ×4, printable to repeat |
| Progress Without Streaks | 1 |
| Reset Page ("Missed a week? Start here") | 1 |
| Sample filled pages | 2 |

**Excluded:**
- 100-page planners
- budgeting (that is #6)
- cleaning
- meal planning
- Life OS
- medication or symptom tracking

## 9. Price

At a 25% sale. FX assumption: 3.70 ILS/USD (assumed, not checked live).

| Regular | Sale (−25%) | ≈ USD |
|---|---|---|
| ₪44 | ₪33.00 | $8.92 |
| **₪51** | **₪38.25** | **$10.34** |
| ₪59 | ₪44.25 | $11.96 |
| ₪64 | ₪48.00 | $12.97 |

**Recommend ₪51.** Its effective price of ~$10.3 matches the anchor's displayed ~$9.90.
- The $10–15 PDF band holds most of the exact-job PDF units: anchor $15, PaperoxStd $14.98, YourColorfulJourney $11.16.
- The exact-job median list price is $7.00, so ₪59–64 is **not** proven.
- A $15+ effective price is **not** assumed. The anchor's $15 is a list price shown on sale.

## 10. Medical and trust check

Etsy's House Rules prohibit items that make medical claims, i.e. claims to treat, prevent, mitigate, cure or diagnose a disease or medical condition. A disclaimer does not cure a claim ([Etsy House Rules – prohibited items](https://www.etsy.com/help/article/4525), [listing content rules](https://www.etsy.com/help/article/4507)). Etsy's pages I found do not single out digital items, so I assume they are covered.

| Never use | Use |
|---|---|
| "treat / reduce ADHD symptoms" | "designed for adults with ADHD" |
| "improve executive function" | "low-friction", "flexible", "restart-friendly" |
| "therapy / therapist-approved" | "one goal at a time", "no streaks to break" |
| "diagnosis / clinical / evidence-based treatment" | "simple visual pages" |

Avoid tags such as "executive function" or "executive dysfunction help" as claims. The anchor uses "executive function" as a tag; we should not copy it into copy that implies improvement.

**Risk: LOW** if this list is followed. Competitors such as SuccessInSocialWork, TherapistToolkitLib and KOREHealing sit in the therapy-framed lane we stay out of.

## 11. Cannibalization vs #6 ADHD Budget: **LOW**

| Axis | #6 ADHD Budget | Goal & Restart |
|---|---|---|
| Title/tags | "adhd budget", money words | "adhd goal setting planner", goal/restart words. The only shared token is "adhd". |
| Buyer | Adult with ADHD | Same buyer (a cross-sell, not a split) |
| Workflow | Money / bills | One goal / next action / restart |
| Acquisition door | "adhd budget" | "adhd goal setting planner" |
| Format | (budget family) | Fillable PDF |

There is no overlap with existing planners in the catalog (#1–#18).

## 12. Hero, for when the gate clears

**Option A wins:** "MISSED A WEEK? START HERE."

It shows one real product card:
- Goal: Write portfolio
- Next Action: Open document
- Low-Energy Version: Write one sentence
- Status: RESTARTED

It reads in 2–3 seconds and shows the wedge.

Option B ("One Goal. One Next Step. Easy Restart.") is the fallback and would be the title line.

Rules:
- Real product UI only.
- No clinical words.
- No #17/#18 layout clone.

## 13. Video, for when the gate clears (12–18 s, real product only)

| Seconds | Shot |
|---|---|
| 0–2 | Overwhelmed list of 8 goals |
| 2–4 | One circled → One Goal page |
| 4–7 | Next Action typed into the fillable field |
| 7–10 | Low-Energy Version typed |
| 10–13 | Calendar "missed a week" → Reset Page |
| 13–16 | Status flips to RESTARTED and the same goal resumes (no new setup) |

Use the video engine. No fake UI and no static slideshow.

## 14. Support load: **LOW–MEDIUM**

| Risk | Mitigation |
|---|---|
| Fillable fields don't save in browser viewers | Start Here: "Open in Adobe Acrobat Reader (free) or Xodo. Browsers may not save." |
| Mobile editing | iOS/Android Acrobat tested; tablet tip on page 1 |
| Printing | A4 + US Letter files, no full-bleed, grayscale-safe |
| "Restart" misunderstood (app? reset of the file?) | Description line: "a printable/fillable PDF — no app, no account" |
| Coaching expectation | "This is a planner, not coaching or therapy" (non-medical wording) |
| Field overflow | Auto-shrink font on long fields; 2 sample pages |
| Accessibility | ≥12 pt, high contrast, tagged PDF, logical tab order, no colour-only meaning |

## 15. Hard pre-build gate

| # | Critical gap | Could it reverse BUILD? | How to close it |
|---|---|---|---|
| G1 | Official Marketplace Insights not run | Yes. If "adhd goal setting planner" has no real Etsy searches, there is no door. | V1 |
| G2 | Anchor 4440940588 unread (pages and mechanism) | **Yes.** If it already ships one goal + low-energy + restart, our wedge is a clone. | V2 |
| G3 | Zero real buyer language | Yes. The restart need is seller-asserted only. | V3 |
| G4 | Second clean entrant on the exact job = NO (WEAK) | Downgrades confidence; not fatal alone | V5 (30-day recheck) |
| G5 | Live Master and Astra decision unread | Yes, if either set a conflicting rule | V4 |

**Result: HOLD / VALIDATION INCOMPLETE.** No BUILD HANDOFF was created.

### Manual validation (Assaf, about 45 minutes, no spend)

- **V1. Marketplace Insights** for adhd goal planner, adhd goal setting planner, adhd goal workbook, adhd reset planner, adhd goal tracker and adhd productivity planner.
  - Record searches, clicks and the top-10 result formats.
  - **PASS** if "adhd goal setting planner" or "adhd goal planner" shows steady searches and its top 10 are mostly PDF/printable (not Notion/Sheets).
- **V2. Open 4440940588.** List its sections and page count. Note whether it has (a) a single-goal page, (b) a low-energy version, (c) a restart/missed-week page.
  - **2 or fewer of the three:** wedge holds.
  - **All three:** REFRAME or REJECT.
- **V3. Read reviews** of 4440940588 (28), 4338845135 (24) and 4333479096 (20). Copy them verbatim.
  - **PASS** if 3 or more reviews mention starting again, falling off, too many pages, guilt/shame, or "finally finished".
- **V4. Read the live Master V20+ and the Astra decision.** Confirm there is no rule against this product.
- **V5 (optional).** Re-pull EverBee in 30 days for a second shop with ≥100 units on a goal/restart/low-energy PDF.

**Decision rule:**
- V1, V2, V3 and V4 pass → **BUILD.** Write the handoff then.
- V2 shows the anchor already does the full mechanism → **REJECT** (or REFRAME to a new wedge).
- V1 fails → **REJECT** for lack of a door.

## Contradictory evidence kept

**For the product:**
- One young (10-month) shop with 4 digital listings sold an estimated 379 units of an ADHD-native, undated, anti-shame goal workbook at a $15 list price.
- That listing is 68% of the shop's sales, so it is a real single-product signal, not a catalog effect.
- 1,676 favourites and 28 reviews.

**Against the product:**
- 34% of the anchor's units fall in one month, and recent months are 6/14/40.
- The anchor shows ~$9.90 (sale), not $15.
- The two numerically CLEAN "second entrants" do a different job.
- Eight young shops copying reset, low-energy and shame-free wording sell 0–19 units each.
- Big bolt-on all-in-one planners (744 and 1,658 units) win the head term on volume.
- The exact-job median price is $7.00.

## Reproduce

```
sh run_all.sh   # rebuilds COMPETITORS.csv from raw/
```

The `raw/` pulls were extracted from the session transcript with `raw/extract_from_transcript.py` (start 2026-10-08T11:04:29Z). Pull notes:
- Two pulls (`F-adhd-reset-p1-bc2dc8`, `F-adhd-productivity-planner-p1-b775e4`, no sales floor) returned zero-unit listings only. They are kept as evidence of crowding by new listings.
- The `F-adhd-goal-setting-p1-b8d946` pull also has no sales floor.

Sources: [Etsy House Rules (4525)](https://www.etsy.com/help/article/4525), [Etsy listing content rules (4507)](https://www.etsy.com/help/article/4507), [Etsy prohibited items](https://etsy.com/legal/prohibited)
