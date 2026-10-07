# ASTRA SOURCE PACK — ENTRANT-FIRST DISCOVERY — 2026-10-07

**All sales, revenue and keyword figures are EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.**

This folder is self-contained. Discovery was **not** re-run: the inputs are the frozen EverBee pulls from the original run (commit 08d5ad8).

- The provisional market is unchanged: **ADHD Adult Life Admin, NOT APPROVED.**
- Nothing was built, listed, published, advertised or spent.

## 1. Reproduce

```sh
cd astra-pack
sh run_all.sh        # Python 3.8+, standard library only; about 5 seconds (use sh: unzipping may drop the exec bit)
cat verify_output.txt
```

- `run_all.sh` regenerates every derived file from `raw/`.
- `verify_output.txt` checks each headline claim of the report against the regenerated data.
- Nothing in the CSVs or tables was edited by hand.

## 2. Inputs (`raw/`, 42 files, frozen)

| Prefix | Count | What | Filters (exact params inside each file under `params`) |
|---|---|---|---|
| `Q-<word>-p1-<hash>.json` | 29 | **Entrant pulls** (`view_listings`) | `listing_type=download`, `shop_age_month_max=24`, `transaction_sold_count_max=15000`, `est_mo_sales_min=100`, `time_range=last_12_months`, `order_by=est_mo_sales desc`, `per_page=100`, `title_include=<word>` (`broad` = no word) |
| `F-<word>-p1-<hash>.json` | 3 | **Young-listing / flood pulls** (adhd, wedding planner, food list) | `listing_type=download`, `listing_age_in_months_max=3`, any shop age, `time_range=last_12_months`, `order_by=est_mo_sales desc`, `per_page=100` |
| `K-<seed>.json` | 10 | **Keyword suggestion pulls** (`view_keyword`) | seed term; `order_by=new_volume desc` |

Every file carries `captured` (UTC timestamp), `tool`, `params` and the `rows` as EverBee returned them, with only image URLs removed.

`raw/extract_from_transcript.py` rebuilt these files from the session transcript. Astra does not need it; it is included to show provenance.

Field meanings (EverBee):

| Field | Meaning |
|---|---|
| `est_mo_sales` | **12-month total** (because `time_range=last_12_months`) |
| `trends` | 12 monthly values, oldest first |
| `listing_age_in_months`, `shop_age_month` | Whole months |
| `transaction_sold_count` | Shop lifetime sales |
| `price` | Listed price as shown; no sale or crossed-out price is available, so "effective price" = listed price |

## 3. Scripts, in run order

| Script | Input | Output | Logic |
|---|---|---|---|
| `entrants.py` | `raw/Q-*.json` | `all_listings_classified.json` | **Dedupe** by `listing_id` across pulls (keeps which queries surfaced it). **Classify** (see §4). |
| `grouping.py` | classified listings | `clusters.json`, `overlay_adhd.json`, `grouping_output.txt` | First-match regex over title → 27 buyer/job clusters (`RULES`, ordered). Per-cluster stats. **ADHD_ADULT overlay** (see §4). |
| `clone_check.py` | `clusters.json`, `overlay_adhd.json`, `raw/F-*.json` | `clone_check.json`, `clone_check_output.txt` | Title-duplication and young-pool metrics (see §4). |
| `entrant_table.py` | `clusters.json` | `ENTRANT-TABLE.md` | Top 3 CLEAN shops per cluster, plus every CLEAN ADHD shop. |
| `summary.py` | all of the above | `adhd_depth.json`, `summary_output.txt` | Step-4 gates, same-buyer job depth, provisional ordering (lexicographic, no weights). |
| `keyword_map.py` | `raw/K-*.json` | `keyword_map.json`, `keyword_map_output.txt` | Typo-echo removal and variant collapse (see the docstring). |
| `astra_tables.py` | all of the above | `ADHD-*.csv`, `RUNNERUP-*.csv`, `astra_tables_output.txt` | Audit tables requested by Astra (§5). |
| `verify_headlines.py` | CSVs and outputs | `verify_output.txt` | Claim-by-claim check. |

## 4. Formulas, filters and thresholds

### Entrant classification (`entrants.py`)

**CLEAN** requires ALL of the following:

| Test | Threshold |
|---|---|
| shop age | ≤24 months |
| shop lifetime sales | ≤15,000 |
| 12-month units | ≥100 |
| active months (`trends` > 0) | ≥8 of 12 |
| sum of the last 3 `trends` values | >0 |
| PLR/MRR/resell | not matched in title (`\b(plr\|mrr\|resell\|master resell\|private label)\b`) or in shop name (`plr\|mrr`) |
| contribution = 12-month units ÷ shop lifetime sales | ≥0.05 |

**NEAR-CLEAN:** every CLEAN test passes except active months <8, AND listing age <12, AND active months ≥ 0.7 × min(listing age, 12).

**REJECT:** everything else. The reason is stored in `why`.

**Entrant = shop.** A shop is a CLEAN entrant if it has ≥1 CLEAN listing. It is NEAR-CLEAN if it has only NEAR-CLEAN listings.

### ADHD_ADULT overlay

- **Include:** title matches `adhd|neurodivergent|executive (dys)?function`.
- **Exclude:** title matches `kids?|toddler|child|classroom|student|teacher|visual schedule|png|clip ?art|\bstl\b|fidget` (child, school and design-asset items).
- Applied to passing (CLEAN or NEAR-CLEAN) listings only.

### Step-4 gates (`summary.py`)

- **G1:** ≥2 CLEAN shops.
- **G2:** top shop holds <60% of cluster units.
- **G3:** cluster is not IP, legal or fraud.

### Provisional ordering (lexicographic)

1. Fit STRONG/MEDIUM.
2. More young listings with ≥30 units.
3. Fewer young near-duplicate pairs.
4. More CLEAN shops.

### Near-duplicate title

- A pair of listings from **different shops** whose first 60 characters (lowercased) have `difflib.SequenceMatcher` ratio ≥0.70.
- An identical title is an exact lowercased match across shops.

### Flood rating (`clone_check.py`)

- **HIGH** if any of:
  - ≥3 entrant near-duplicate pairs
  - ≥40% of entrant listings under $4
  - ≥20 young-pool near-duplicate pairs
- **MEDIUM** if ≥1 pair or ≥20% of entrant listings under $4.
- **LOW** otherwise.
- "(tier-specific)" is appended when ≥3 CLEAN shops sell at ≥$15.

### Young pool for ADHD

- `raw/F-adhd-*.json` minus the overlay exclusion: 100 → **75** rows.
- "New shop" = shop age ≤24 months.
- "Winner" = ≥30 units.

### Same-buyer job

- First-match regex (`summary.ADHD_JOBS`) over: overlay listings + young listings with ≥30 units.
- Excluded from depth: `summary.KID`, which is the overlay exclusion plus `worksheet|therapy|therapist`.
- A job counts when it has ≥2 distinct shops.

### ADHD class (`astra_tables.adhd_class`; title-level only)

| Class | Rule |
|---|---|
| ADHD-NATIVE | Title names an ADHD-specific mechanism or need: brain dump, brain reset, task paralysis, executive function, dopamine, overwhelm, ADHD-friendly, "for ADHD", neurodivergent, neurospicy, ADHD coach |
| ADHD-BOLT-ON | Not native, and the first "adhd" appears at character ≥40 (appended to a generic product name) |
| ADHD-ADAPTED | Otherwise |

**Valid job (stricter, new for Astra):** ≥2 shops AND ≥2 shops with a non-bolt-on listing.

### Format (title regex only; product files were not inspected)

- Categories: Notion, Sheets, Excel, Canva, app/web, digital planner (Goodnotes/Notability), PDF.
- Two or more categories in one title = **hybrid**.
- Sheets + Excel only = **Sheets/Excel**.

## 5. Audit tables

| File | Rows | Content |
|---|---|---|
| `ADHD-CLEAN-ENTRANTS.csv` | 31 listings / 20 CLEAN + 7 NEAR-CLEAN shops | Every claimed ADHD entrant listing. Columns: shop, shop age, shop total sales, listing ID, title, listing age, price, 12-month units and revenue, 12-month trend, last 3 months, queries that surfaced it, grouping cluster, buyer job, format, class, and **the exact rule values** that produced the class |
| `ADHD-JOB-DEPTH.csv` | 46 | Every listing supporting each of the 6 jobs: persona, acquisition phrase, standalone or bundled, same buyer as #6, ADHD class, "same without ADHD wording" |
| `ADHD-RECENT-ENTRY.csv` | 75 | The young pool exactly as used: listing ID, shop, shop age, listing age, units, price, title, ADHD job, grouping cluster, new-shop flag, ≥30 flag |
| `ADHD-PRICE-FORMAT.csv` | 145 | Every adult-ADHD listing held (overlay, rejected entrant rows and the young pool): price, units, trend, active months, format, ≥$15 flag, active ≥10 months flag, new vs established shop |
| `ADHD-CLONE-FLOOD.csv` | 6 | Per job subcluster: sampled, ≤1 month old, ≤3 months old, near-duplicate pairs and shops, identical pairs, PLR examples, units total and from new shops, price min/median/Q3/max, share under $4, pair detail |
| `RUNNERUP-WEDDING-ENTRANTS.csv`, `RUNNERUP-DIET-ENTRANTS.csv` | 19 / 22 | Entrant listings for #2 and #3 with class rules |
| `RUNNERUP-WEDDING-RECENT-ENTRY.csv`, `RUNNERUP-DIET-RECENT-ENTRY.csv` | 100 / 100 | Young pools for #2 and #3 |
| `ENTRANT-TABLE.md` | 73 shops | Cross-domain entrant table from the report |
| `keyword_map.json` | 30 / 19 / 26 | Keyword maps for the top 3 |

## 6. Headline reproduction (`verify_output.txt`)

| Claim | Reproduced | Status |
|---|---|---|
| 20 ADHD CLEAN entrant shops | 20 | YES |
| 7 ADHD NEAR-CLEAN shops | 7 | YES (LinkDigitalStudio, PlanoraNotion, RichvaleCreatives, SunnyKiteHill, Webudding, fikadoodle, habitualsheets) |
| 24 / 75 young listings ≥30 units | 24 / 75 | YES, with a caveat (E1) |
| 17 of those from new shops | 17 | YES, with a caveat (E1) |
| 2 near-duplicate titles in the young pool | 2 pairs | YES |
| ~40% of units under $4 | 40.4% (overlay base); 36.0% (all 145 ADHD listings held) | YES |
| 6 same-buyer jobs | 6 | YES under the original rule; **5** under the stricter bolt-on test (E3) |
| Premium tier is "Notion and apps" | Notion + app/web = 17% of premium units | **CORRECTED** (E4) |
| Wedding young 5 / 100, 89 duplicate pairs; Diet young 51 / 100, 49 new-shop, 73 pairs | Same | YES |

## 7. ERRATA — corrections to `ENTRANT-FIRST-DISCOVERY-2026-10-07.md`

The original report is kept unchanged in this folder for audit. These corrections apply to it.

### E1 — 24/75 is a top-sellers sample, not a sell-through rate

- The F-pull returns the **top 100 young listings by units**.
- All 100 had ≥1 sale, so the cap was hit and the full population of new ADHD listings is unknown.
- 24/75 means "of the 75 best-selling adult ADHD listings ≤3 months old, 24 reached ≥30 units". It does **not** mean 32% of new entrants succeed.
- The cross-market comparison (ADHD 24/75, Wedding 5/100, Diet 51/100) uses the same method and stays valid as a *relative* signal.
- 7 of the 24 are not counted in any of the 6 life-admin jobs:
  - ConventionKids JW convention notebook (217 units, a 122-month, 55k-sale shop)
  - SuccessInSocialWork rumination workbook
  - TheSoulfulSystems decision-fatigue worksheet
  - **GodsSweetheartStudio "500,000 Mega Bundle … PLR MRR"** (a resell bundle that should not count as a winner)
  - HappySmartCookie kids' feelings worksheet
  - PaperoxStd executive-functioning workbook
  - PrezcsentDigitals "ADHD Friendly Paycheck Budget Planner … Worksheet" (a genuine bills product, dropped by the `worksheet` exclusion)
- **Restricted to the 6 jobs: 17 winners, 13 from new shops.**

### E2 — Job-depth figures were computed on titles truncated to 90 characters

`overlay_adhd.json` stored titles cut to 90 characters, and `summary.py` ran the job regex on them. This is fixed in `grouping.py` (full titles). Corrected figures, with the report's figure in brackets:

| Job | Shops | Units |
|---|---|---|
| Bills | 7 [6] | 5,031 [4,862] |
| Daily/weekly planner | 9 [10] | 3,632 [3,801] |
| Life OS | 7 [6] | 1,700 [1,555] |
| Habits | 3 [4] | 681 [826] |
| Cleaning | 9 (unchanged) | 9,893 (unchanged) |
| Brain dump | 4 (unchanged) | 773 (unchanged) |

The count of jobs with ≥2 shops is still **6**.

### E3 — Brain dump fails the stricter bolt-on test

- 3 of its 4 shops are ADHD-BOLT-ON titles: CellRise Eisenhower matrix, RichvaleCreatives task tracker, DailyPlansCoStore work-day planner.
- Only MadeForFunction ($37, 11/12 active months) is native.
- **VALID SAME-BUYER JOBS BEFORE ASTRA = 5.**
- Sensitivity: `summary.KID` drops titles containing "worksheet". That removes Templix8's adult "ADHD Brain Reset Bundle … Brain Dump Worksheet" (CLEAN, 255 units). Narrowing that exclusion to children's worksheets makes brain dump valid (2 non-bolt-on shops) and restores 6.
- The rule is left as written; Astra decides.

### E4 — Premium is not concentrated in Notion or apps

- 20 listings sell at ≥$15. Their 2,889 units split by format:

| Format | Listings | Units |
|---|---|---|
| Hybrid | 5 | 848 |
| PDF | 6 | 766 |
| Unstated | 3 | 465 |
| Notion | 2 | 357 |
| Digital planner | 1 | 306 |
| App/web | 3 | 147 |

- Notion + app/web = **17%** of premium units. Premium is spread across formats, with PDF and hybrid bundles the largest.
- Report §10 item 5 ("the premium tier is Notion and apps") is **retracted**. The format-split risk becomes: "the highest-priced listings ($29.99–$46) are Notion; the $15–20 band is format-mixed".
- Sustained premium (CLEAN, ≥8 active months) is still exactly 4 shops: NeurodivergentHQ $15, DragonHoardTemplates $29.99, MadeForFunction $37, TemplateMuseAlchemy $46.

### E5 — "Clone" means title duplication only

- Etsy product pages and files were blocked (403). No product-level comparison was possible.
- Every "clone" statement in the report means **near-duplicate titles across different shops**, not proven product copying.
- Per subcluster (`ADHD-CLONE-FLOOD.csv`):
  - cleaning: 27 near-duplicate pairs across 12 shops, 0 identical titles
  - bills: 1 pair
  - planner: 1 pair
  - life OS: 2 pairs, plus 3 PLR-style "1000 ADHD Life Planner" listings (PLRxMRR, TheSelfMaderPLRMRR, StarOfPlannerStore)
  - brain dump: 0
  - habits: 0

### E6 — Listing-age granularity

- EverBee reports whole months.
- "≤30 days" is approximated by listing age ≤1 month, and "≤90 days" by ≤3 months.

## 8. Known limits (unchanged from the report)

- Shop listing counts were not pulled; shop lifetime sales of ≤15,000 is the proxy.
- Format and ADHD class are read from titles, not from product files.
- Regex grouping is order-dependent; the rule order is in `grouping.RULES`.
- EverBee keyword volumes are unverified against official Insights.
- **#6 ADHD Budget first-party Etsy Stats were not available.**
