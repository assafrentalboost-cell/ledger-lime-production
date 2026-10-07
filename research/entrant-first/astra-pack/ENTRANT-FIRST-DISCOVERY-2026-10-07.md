# LEDGER & LIME — ENTRANT-FIRST MARKET DISCOVERY — 2026-10-07

**Status:** research only. Nothing was built, published, listed, advertised or spent, and Etsy was not touched. The live Master was **not** changed; see `MASTER-APPEND-2026-10-07-ENTRANT-FIRST.md`.

**Every EverBee figure here is EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA** (units = 12-month estimated sales).

**Reproduce:** run `./run_all.sh`. Every number below comes from a script output (`*_output.txt`, `*.json`). Nothing is hand-computed. No weighted score is used anywhere.

---

## 0. Answer first

- **PROVISIONAL MARKET = ADHD Adult Life Admin.** The buyer is an adult with ADHD who is running a household. NOT APPROVED.
- **Top 3:**
  1. ADHD Adult Life Admin
  2. Wedding Planning Admin
  3. Diet-Change Food Guides
- **Why this market won:**
  - It is the only finalist where new listings (≤3 months old) from new shops **still sell**: 24 of the top 75 young adult-ADHD listings reach ≥30 units, 17 of them from shops ≤24 months old.
  - Its young listings show almost no clone wave: 2 duplicate-title pairs, against 89 for wedding.
  - It has 6 distinct same-buyer jobs, each with ≥2 independent shops.
- **The catch, stated up front:**
  - L&L already sells **#6 ADHD Budget**, so this is a **new department grown around one existing door**, not virgin territory.
  - The budget and cleaning doors are cloned at $1–3.
  - Most volume sits below $12.

---

## 1. Method (Steps 1–3)

### 1.1 Entrant pulls

There are 29 EverBee `view_listings` entrant pulls in `raw/Q-*.json`.

Fixed filters on every pull:
- digital listings only
- shop age ≤24 months
- shop lifetime sales ≤15,000
- ≥100 units in the last 12 months
- sorted by units, descending, 100 per page

Each pull adds one neutral title word to widen domain coverage:
- **Generic words:** broad (none), planner, tracker, spreadsheet, checklist, log, binder, forms, calculator, notion
- **Business words:** business, client, contract, invoice, inventory
- **Life-event words:** budget, wedding, baby, vehicle, homeschool, pet, teacher, travel, meal, rental, cleaning, medical, co-parent, adhd

`adhd` was added **after** ADHD titles had surfaced on their own in the budget, cleaning, planner and tracker pulls. "fundrais" returned no listings.

Department #2's supplementary pulls (ceu, rbt, practicum, supervision, notary) were removed. They had no shop-age filter.

### 1.2 Entrant classification (`entrants.py`)

The script deduplicates by listing ID across pulls. Each listing is then classified:

| Class | Rule |
|---|---|
| CLEAN | shop ≤24 mo · shop sales ≤15k · ≥100 units · active ≥8/12 months · last-3-month units >0 · not PLR/MRR/resell (title **or shop name**) · listing ≥5% of shop lifetime sales |
| NEAR-CLEAN | Fails only the active-month rule, because the listing is young: active ≥ 0.7 × min(listing age, 12) and listing age <12 |

- **Result:** 1,654 unique listings → **577 CLEAN + 201 NEAR-CLEAN** listings from **608 distinct shops**. The other 876 were rejected.
- **Shop listing count:** not pulled. Shop lifetime sales (≤15k) and the ≥5% contribution rule stand in as the "not a mass factory" proxy. This is a disclosed gap.

### 1.3 Grouping (`grouping.py`)

- Each passing listing goes to the **first** regex rule that matches, in a fixed order of 27 buyer/job clusters (specific jobs first; IP, legal and fraud rules first of all).
- Clusters are buyer + job, never format.
- A **buyer overlay** (ADHD_ADULT) spans job clusters. It matches adhd / neurodivergent / executive function in the title and excludes kids, classroom, PNG/clipart and STL items.
- The exact rules are in the code.

### 1.4 Entrant table

`ENTRANT-TABLE.md` has 73 distinct entrant shops with every required field:
- **Section A:** 60 shops across 23 domains (the top 3 CLEAN shops per job cluster).
- **Section B:** all 20 CLEAN ADHD-adult shops.

---

## 2. Cluster table (Step 3–4) — `grouping_output.txt`

Column key: **CLEAN** = clean shops; **NEAR** = near-clean shops; **Top shop** = top-shop share of cluster units.

| Cluster (buyer → job) | Fit | CLEAN | NEAR | Units | Top shop | Median $ | Q3 $ | Prior history |
|---|---|---|---|---|---|---|---|---|
| Design assets (SVG/PNG/presets/STL) | WEAK | 85 | 33 | 83,193 | 6% | 6.73 | 11.27 | — |
| Craft patterns | WEAK | 80 | 21 | 172,564 | 4% | 6.10 | 8.00 | — |
| Party / gift / decor | WEAK | 37 | 21 | 42,709 | 8% | 5.00 | 8.40 | — |
| Wedding decor (invites, signs, websites) | WEAK | 36 | 15 | 36,658 | 8% | 8.20 | 19.44 | — |
| Personal budget / debt | STRONG | 31 | 7 | 41,462 | 18% | 6.70 | 11.99 | **LIVE core #1–#7** |
| Fan merch (IP) | EXCLUDED | 29 | 11 | 54,540 | 13% | 4.99 | 6.00 | — |
| Life / productivity planner | WEAK | 24 | 6 | 19,973 | 12% | 8.78 | 16.15 | — |
| Kids learning content | WEAK | 22 | 7 | 15,390 | 13% | 6.00 | 14.46 | — |
| **Wedding planning admin** | STRONG | **17** | 0 | 11,820 | 16% | 10.22 | 21.82 | #9 V2 HOLD; #9 Wedding Budget live |
| Travel planning | MEDIUM | 16 | 9 | 5,792 | 10% | 7.00 | 11.99 | Dropped (Discovery 2.0); mostly decor/sewing |
| Baby shower decor | WEAK | 15 | 2 | 19,764 | 18% | 4.50 | 7.24 | — |
| **Diet-change food guides** | WEAK | **13** | 1 | 5,730 | 17% | 7.68 | 14.47 | GLP-1 dropped (Discovery 2.0) |
| Creator marketing | WEAK | 12 | 2 | 5,347 | 16% | 5.00 | 13.91 | — |
| Small-business admin | STRONG | 10 | 4 | 4,071 | 20% | 3.62 | 9.40 | Bookkeeping/invoice rejected; #14, #15 live |
| Cleaning / chores | MEDIUM | 8 | 4 | 11,601 | 28% | 5.64 | 8.27 | Dept #1 household failed |
| Caregiver / health records | STRONG | 8 | 2 | 4,048 | 16% | 3.33 | 8.38 | #11, #16 adjacent |
| Meal planning | MEDIUM | 5 | 1 | 2,853 | 42% | 5.17 | 6.00 | — |
| New-parent organisation | MEDIUM | 5 | 2 | 2,564 | 26% | 3.50 | 6.07 | — |
| Homeschool admin | STRONG | 5 | 1 | 1,996 | 36% | 7.00 | 7.58 | Dropped (Discovery 2.0) |
| Co-parenting | STRONG | 2 | 0 | 2,267 | **64%** | 18.99 | 18.99 | **LIVE #17** |
| Vehicle private sale / STR host / teacher admin / reading | — | 1–3 | — | <2k | ≥60% | — | — | One shop dominates each |
| **ADHD adult (buyer overlay)** | STRONG/MEDIUM | **20** | 7 | **21,109** | 16% | 7.99 | 11.66 | **#6 ADHD Budget live (one door)** |

### Step-4 gates

Every gate is applied in `summary.py`; there are no weights.
- **G1:** ≥2 clean shops.
- **G2:** top-shop share <60%.
- **G3:** not IP, legal or fraud.

Results:
- **18 job clusters + 1 buyer overlay = 19 entrant-backed clusters.**
- **Finalist-eligible** (≥3 clean shops, STRONG/MEDIUM fit, not a live product family): wedding planning admin, travel, small-business admin, cleaning, caregiver, meal, new-parent, homeschool. ADHD-adult is also eligible: it touches live #6 through one door only, which is disclosed below.
- **Rejected at the gates:**
  - Co-parenting (one shop holds 64%, and it is already live #17).
  - Vehicle sale, STR host, teacher admin (single-shop clusters).
  - IP and legal clusters.
  - Decor and craft clusters as provisional (WEAK fit), although they are commercially huge.

**Side finding:** the co-parenting cluster now shows 2 CLEAN shops (TheTreasuredTreetop, LovingSheets) plus OutsideTheBoxPro and TikTakTemplates just under the rules. That is more than the "one clean shop" found on 2026-10-04. It does not change anything here, because #17 is already live.

### Why the small eligible clusters did not make the top 3

| Cluster | Reason |
|---|---|
| Travel | 25 listings, but most are passports-for-kids, sewing patterns and posters. Only one real itinerary planner (SoftRebelsShop $2.50). |
| Small-business admin | Mixed buyers (resellers, bakers, invoicing); median $3.62; prior rejects. |
| Cleaning | 9,720 of its 11,601 units are ADHD-titled. It is absorbed into the ADHD overlay. |
| Caregiver | Median $3.33; buyers split between agencies and families. |
| Meal / new-parent / homeschool | ≤2,900 units each, Q3 ≤$7.58, top-shop share 26–42%. |

---

## 3. Top 3 entrant-backed markets (Step 11)

All figures are EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.

| | 1. ADHD Adult Life Admin | 2. Wedding Planning Admin | 3. Diet-Change Food Guides |
|---|---|---|---|
| **Buyer** | Adult with ADHD running a household and money | Engaged couple planning a wedding | Person told to change diet (diabetes, IBS/FODMAP, cholesterol, gallbladder, kidney, GLP-1) |
| **Job family** | Pay bills on time, keep the house running, get tasks started, see everything in one place | Budget and vendor payments, guest list/RSVP, timeline, day-of binder, checklist | "What can I eat / avoid", grocery list, starter meal plan |
| **Clean entrants** | **20 CLEAN + 7 NEAR** shops | 17 CLEAN | 13 CLEAN + 1 NEAR |
| **Entrant examples** | CustomGroupGifts budget $1.94 (3,396, 12/12); LifePrintableStore cleaning $6.70 (2,621); PlanMindco planner $8.30 (1,640, 12/12); EzPlanningStudio bill spreadsheet $7.88 (764, 12/12); BossMeansBusiness $11.34 (609); MadeForFunction brain dump $37 (274, 11/12); TemplateMuseAlchemy $46 (217); DragonHoardTemplates $29.99 (145, 12/12); NeurodivergentHQ $15 (379) | RoyalTemplatesShop binder $33.42 (1,867, 11/12); IvyRepublicDesigns $57.97 (587, 12/12) and $45.97 (428, 12/12); AravellaCreative $26.41 (1,127, but last 3 months 0/18/0); SheetDesignLab $3.32 (1,127); ForeverMomentStudio $3.99 (1,056); PaperieHeaven checklist $6.21 (450) | UnstoppablesCo keto $1.86 (574) and protein $2.49 (414); FamcarCreates FODMAP $7.17 (651); BeBalancedEditables diabetic $17.49 (365) and Mediterranean $16.99 (246); TheGenlePlate GLP-1 $14.90 (317) |
| **New listings ≤3 mo (top pool)** | 75 adult rows; **24 ≥30 units, 17 from new shops**; median $5.03 | 100 rows; **5 ≥30 units, 2 from new shops**; median $7.98 | 100 rows; **51 ≥30 units, 49 from new shops**; median $6.72 |
| **Price: median / Q3** | $7.99 / $11.66 | $10.22 / $21.82 | $7.68 / $14.47 |
| **Unit share by price** | <$4: 40%; $4–12: 48%; $12–20: 8.5%; ≥$20: 3% | <$4: 23%; ≥$15: 50% | — |
| **Sustained premium (CLEAN, ≥$15)** | 4 shops: $15, $29.99, $37, $46 (145–379 units) | 7 shops: $15–$57.97 | 1 shop ($16.99–17.49) |
| **Clone risk** (`clone_check.py`) | **HIGH (tier-specific)**: 11 cross-shop duplicate pairs among entrants (cleaning and budget doors); young pool **2 pairs** | **HIGH (tier-specific)**: 11 pairs among entrants; young pool **89 pairs across 41 shops**; 4 PLR | **HIGH**: young pool 73 pairs across 26 shops ("Eat / Limit / Avoid" template wave) |
| **Buyer language** | "ADHD tax"; late fees and forgotten subscriptions; "clean the house is not a task"; out of sight, out of mind; task paralysis; brain dump; "for overwhelmed brains" | Budget, vendor deposits and balances, due dates, guest count; free templates (Bridebook) compete | Etsy titles only: "eat, limit, avoid", "foods to avoid" |
| **Same-buyer distinct jobs** | **6** (§5) | ≈6, but already explored (#9 V2 HOLD) | 1 job across many conditions (variants, not distinct jobs) |
| **Demand signal (EverBee keywords)** | adhd planner 3,225; adhd cleaning 785; adhd notion 470; budget planner adhd 485; adhd brain dump 137 | wedding planners 1,425; wedding budget spreadsheet 324 | food list chart 5,507; diabetic food list 1,731 |
| **Main risks** | #6 overlap and cannibalization; low-price clone tier; medical-claims language; credibility (rivals sell "made by an ADHD coach") | Late-entrant failure; flooded title wave; one-time purchase; free templates; prior HOLD | Health and medical-advice liability; content, not admin; per-condition SKU sprawl; template wave |
| **Brand fit** | **STRONG** for money and admin jobs; MEDIUM for cleaning and planners | STRONG (budget/payment admin), but event-bound | **WEAK** (nutrition content) |

### Why #1 beats #2 and #3

`summary.py` ranks lexicographically:
1. Fit STRONG/MEDIUM.
2. Young-pool sell-through.
3. Fewer young duplicate pairs.
4. Clean shops.

How each finalist falls out:
- **Diet** has the best young sell-through, but WEAK fit and health liability block it as the provisional. Under the brief, a commercially strong market is not rejected *only* for brand distance; here the medical-content risk is the deciding factor, not brand distance.
- **Wedding** has the best premium tier, but new entrants in the last 3 months mostly fail: 5 of 100 reach ≥30 units, against 24 of 75 for ADHD.

---

## 4. Clone / flood detail (Step 5) — `clone_check_output.txt`

### Rule (in code)

- **HIGH** if any of these holds:
  - ≥3 cross-shop title pairs with difflib ≥0.70 among entrants
  - ≥40% of entrant listings under $4
  - ≥20 duplicate pairs in the young pool
- **MEDIUM** if ≥1 duplicate pair or ≥20% of entrant listings under $4.
- **LOW** otherwise.
- **"Tier-specific"** is appended when ≥3 CLEAN shops sell at ≥$15.

### ADHD findings

- The cleaning door is a clone cluster. LifePrintableStore / LinkDigitalStudio score 0.92. Five shops share "ADHD Cleaning Planner Bundle…".
- The budget door has a clone pair: CustomGroupGifts / Heart2HeartbyYoli (0.77), both priced $1.94–2.99.
- Brain dump, life OS, habits and the planner doors show no clone pairs.
- Young pool: only 2 duplicate pairs among 75 listings.
- Young winners priced $12.99–$39.38:
  - Webudding $16.99 (306)
  - EverydayApps $19 (67)
  - MasterMoneyBudget budget app $15.99 (67)
  - LumenResetCo cleaning deck $12.99 (66, 4-month shop)
  - ElthivarDigitalCo $17.59 (62)
  - EzPlanningStudio paycheck app $39.38 (58)
- **Conclusion:** the flood is concentrated in the $1–3 cleaning and budget doors. New shops still sell at $12–20 when the product is differentiated.

### Wedding findings

- The young pool is a title wave: 89 pairs across 41 shops; "Wedding Planner Spreadsheet…" variants dominate.
- The best young listing is an old 10,658-sale shop (HumbleArtPrint, 104 months, $4.99, 392 units).
- 4 PLR listings.

### Diet findings

- New shops win (49 of 51 young listings at ≥30 units come from shops ≤24 months old).
- They win with near-identical "Food List Printable, Eat Limit Avoid" titles at $6–7.

---

## 5. Same-buyer depth — ADHD Adult (Step 7) — `adhd_depth.json`

**Rule:** a job counts only when ≥2 distinct shops sell it. Evidence comes from the entrant overlay plus young-pool listings with ≥30 units.

| # | Job | Shops | Units | Acquisition door | Buyer need | Format | Purchase reason / evidence |
|---|---|---|---|---|---|---|---|
| 1 | **Bills, budget & paycheck** (live #6 door) | 6 | 4,862 | adhd budget / budget planner adhd | Stop late fees and "ADHD tax"; see what is due | Google Sheets | CustomGroupGifts, EzPlanningStudio (bill spreadsheet 12/12), Heart2HeartbyYoli, MasterMoneyBudget $15.99 (young) |
| 2 | **Cleaning & chore system** | 9 | 9,893 | adhd cleaning planner / adhd cleaning checklist | "Clean the house" turned into small checkable steps | Sheets / printable / cards | LifePrintableStore, fikadoodle, TheTreasuredTreetop, BaileysWonderland, LumenResetCo $12.99 (young) |
| 3 | **Daily / weekly planner** | 10 | 3,801 | adhd planner / adhd daily planner | Structure the day | Digital planner / Sheets | PlanMindco 12/12, BossMeansBusiness, Webudding $16.99 |
| 4 | **Life OS / all-in-one dashboard** | 6 | 1,555 | adhd notion / adhd life planner | Everything in one place | Notion / Sheets | TemplateMuseAlchemy $46, PlanoraNotion $19.70, Webudding |
| 5 | **Brain dump / task paralysis / prioritising** | 4 | 773 | adhd brain dump | Get unstuck; choose what to do first | Printable / Sheets | MadeForFunction $37 (11/12), CellRise Eisenhower, RichvaleCreatives, DailyPlansCoStore |
| 6 | **Habits, goals & routines** | 4 | 826 | adhd habit tracker / adhd workbook | Build routines that stick | PDF / Sheets / Notion | NeurodivergentHQ $15, DragonHoardTemplates $29.99 12/12, AravellaCreative, EverydayApps (young) |

**SAME-BUYER DISTINCT PRODUCT JOBS = 6.**

Not counted:
- 12-month task / deadline calendar (EzPlanningStudio, 150 units, failed the 5% contribution rule).
- Symptom / medication log (TemplateMountain, 13.5k-sale catalog; health-adjacent).
- Reading tracker (1 shop).

**Fit split:**
- Jobs 1, 4 and 5 are L&L's core competence: money, records, recurring admin.
- Jobs 2, 3 and 6 are MEDIUM fit, but they are the same buyer's highest-volume doors.

---

## 6. Price durability (Step 8)

### ADHD Adult

- **Median and Q3:** median $7.99, Q3 $11.66.
- **Volume skew:** 40% of units sell under $4, and only 11.5% at ≥$12.
- **Sustained premium (CLEAN, ≥8/12 months):**
  - NeurodivergentHQ $15
  - DragonHoardTemplates $29.99
  - MadeForFunction $37
  - TemplateMuseAlchemy $46
  - These sell 145–379 units each, so the tier is real but small.
- **Young premium winners:** $15.99–$39.38.
- **Verdict:** per the brief, **do not position premium at the door**, because most volume is low-price commodity. The defensible band is **$9–16 for single jobs** plus a **bundle at ≈$25–35**, which follows the MadeForFunction "whole shop" $37 precedent. No crossed-out prices were used; EverBee shows list price.

### Wedding

- Median $10.22, Q3 $21.82.
- 50% of units sell at ≥$15. This is the strongest premium of the three, but it is earned by older entrants.

### Diet

- Median $7.68, Q3 $14.47.
- Only one shop sustains ≥$15.

---

## 7. Buyer language (Step 6)

Sources are public pages, not Etsy reviews; Etsy review text is blocked (403), as in Departments #1 and #2.

- **"ADHD tax":** money lost to "late fees and forgotten subscriptions", overdraft fees and unused subscriptions ([ReachLink](https://www.reachlink.com/es/consejos/adhd/the-hidden-cost-of-having-adhd-nobody-calculates/)).
- **Bills:** "Forgetfulness … can lead to … late fees and credit score damage when bills are missed"; systems that "require too much time and attention" fail ([ADDitude](https://www.additudemag.com/pay-bills-money-management-adhd-organization/), [Inflow](https://www.getinflow.io/post/adhd-budgeting)).
- **Cleaning:** "'clean the house' is not a task — it is an open-ended project with no clear start, no defined end"; "losing track of what you've already done" ([Focus Bear](https://focusbear.io/blog-post/simple-steps-to-create-an-effective-adhd-cleaning-schedule), [Psych Central](https://psychcentral.com/blog/7-tips-for-getting-chores-done-for-adults-with-adhd/)). ADDitude gives away a free ADHD cleaning checklist, which is a free-substitute risk.
- **Etsy seller vocabulary** (titles of selling listings): "task paralysis", "brain dump", "executive function", "dopamine task deck for overwhelmed brains", "out of sight", "made by an ADHD coach".
- **Not invented:** no readiness, automation, compliance or reporting job is claimed. Every job in §5 maps to a selling listing and to the phrasing above.
- **Wedding:** buyers talk about vendor deposits, balances and due dates, and guest count. Free Bridebook templates compete ([Bridebook](https://bridebook.com/au-en/article/wedding-planning-spreadsheet)).

---

## 8. Keyword maps (Step 10) — `keyword_map_output.txt`

EverBee keyword volumes have been 10–25× off official Insights before (Department #1). They map doors; they do not size demand.

Deduplication:
- Drop typo echoes (low competition at the parent term's volume).
- Collapse word-order and plural variants.
- Cap at 30 terms.

| Cluster | Terms kept |
|---|---|
| ADHD Adult | 30 |
| Wedding | 19 |
| Diet | 26 |

### ADHD Adult — key doors (volume)

**Planner doors:**
- adhd planner 3,225
- digital adhd planner 2,532
- daily planner adhd 2,471
- weekly adhd 2,316
- adhd notability planner 1,157

**Cleaning doors:**
- adhd planner clean 930
- adhd cleaning 785
- cleaning adhd planner 758
- cleaning planner adhd checklist 711
- adhd cleaning schedules 687
- adhd cleaning checklist 661

**Notion doors:**
- adhd digital planner notion 507
- adhd notion 470
- notion templates adhd 445

**Budget doors:**
- budget planner adhd 485
- adhd budget planner digital 323
- budget templates adhd 289
- adhd monthly budget 287
- adhd budgeting 276
- adhd budget 275

**Smaller doors** (outside the 30-term cap):
- adhd planner brain dump 234
- adhd brain dump 137
- adhd bill tracker 32

### Wedding

- wedding planners 1,425
- wedding planner books 866
- checklist wedding planner 769
- wedding budget spreadsheets 324
- wedding budget tracker spreadsheet 156

### Diet

- food list chart 5,507
- diabetic foods list 1,731
- diabetes food list chart 1,548
- diabetic food grocery list 1,277

---

## 9. Provisional winner — NOT APPROVED

**PROVISIONAL MARKET = ADHD Adult Life Admin.**

- **Department shape:** a buyer-centred family of 6 jobs, with the existing #6 ADHD Budget as the money door.
- **What would be new:** cleaning system, planner/dashboard, life OS, brain-dump/prioritiser, and habits/routines.
- **Not decided here:** product order, format and price. That waits for ASTRA and Insights.

### Marketplace Insights checks (8) — Assaf, UI-only

1. adhd planner
2. adhd cleaning planner
3. adhd budget planner
4. adhd brain dump
5. adhd notion template
6. adhd life planner
7. adhd bill tracker
8. wedding planner spreadsheet (runner-up switch check)

### Decision rules (pre-registered)

- **CONFIRM:** at least 2 of terms 1–4 show ≥100 searches at Typical-or-better conversion.
- **SWITCH to Wedding Planning Admin:** terms 1–4 are all <50 searches or Very low conversion, **and** term 8 is ≥100 at Typical+.
- **RE-RUN:** both fail.

---

## 10. Reasons this may be wrong (for ASTRA)

1. **Not new.** #6 ADHD Budget is live. If #6 sells poorly, that is first-party evidence against the buyer. #6 sales data was **not** available in this repo and should be checked first.
2. **Commodity volume.** 40% of units sell under $4; the cleaning door is a clone cluster.
3. **Trend risk.** "ADHD" may be a title fad that sellers bolt onto generic planners. Some entrant titles only append ADHD (CellRise Eisenhower matrix, RichvaleCreatives task tracker).
4. **Medical-claim and credibility risk.** Rivals lean on "made by an ADHD coach". L&L has no clinical voice, and the copy must avoid treatment claims.
5. **Format split.** The premium tier is Notion and apps; L&L is Sheets-first.
6. **Free substitutes.** ADDitude's free cleaning checklist and budgeting apps.
7. **Grouping bias.** Grouping is regex-driven and order-dependent. Moving a rule changes counts (for example, cleaning was absorbed into the ADHD overlay).
8. **Missing shop data.** Shop listing counts were not pulled; the "modest catalog" condition is proxied.
9. **Wedding is the commercially richer premium market.** A red team that weights price over late-entrant sell-through flips #1 and #2.
10. **Diet beats both on entrant sell-through.** Excluding it rests on fit and liability judgement, not data.

---

## 11. Files

| File | What |
|---|---|
| `raw/Q-*.json` (29) | Entrant pulls, with exact params and capture time |
| `raw/F-*.json` (3) | Young-listing flood pulls |
| `raw/K-*.json` (10) | Keyword pulls |
| `raw/extract_from_transcript.py` | Rebuilds `raw/` from the session transcript |
| `entrants.py` | Classification and listing-ID dedupe → `all_listings_classified.json` |
| `grouping.py` | Cluster rules, cluster stats and ADHD overlay → `clusters.json`, `overlay_adhd.json`, `grouping_output.txt` |
| `clone_check.py` | Flood/clone rule → `clone_check.json`, `clone_check_output.txt` |
| `entrant_table.py` | → `ENTRANT-TABLE.md` |
| `summary.py` | Gates, same-buyer depth and provisional ordering → `adhd_depth.json`, `summary_output.txt` |
| `keyword_map.py` | Keyword deduplication → `keyword_map.json`, `keyword_map_output.txt` |
| `run_all.sh` | One command to reproduce |

---

```
CLEAN / NEAR-CLEAN ENTRANTS REVIEWED = 608 shops (577 CLEAN + 201 NEAR-CLEAN listings; 73 shops tabled in ENTRANT-TABLE.md)
ENTRANT-BACKED MARKET CLUSTERS = 19 (18 job clusters + 1 buyer overlay passing G1–G3)
TOP 3 = ADHD Adult Life Admin; Wedding Planning Admin; Diet-Change Food Guides
PROVISIONAL MARKET = ADHD Adult Life Admin (NOT APPROVED)
CLEAN ENTRANTS IN PROVISIONAL MARKET = 20 (+7 NEAR-CLEAN)
SAME-BUYER DISTINCT PRODUCT JOBS = 6
CLONE/FLOOD RISK = HIGH (tier-specific: $1–3 cleaning/budget doors cloned; young pool 2 duplicate pairs; new shops still selling at $12–20)
MARKETPLACE INSIGHTS CHECKS REQUIRED = 8
READY FOR ASTRA RED-TEAM = YES
```

---

## Errata (added 2026-10-07, Astra source pack)

Six corrections (E1–E6) are listed in `astra-pack/README.md` §7. The body above is left unchanged for audit. In short:

- **E1:** 24/75 is a top-sellers sample, not a sell-through rate. Restricted to the 6 jobs it is 17 winners, 13 from new shops.
- **E2:** per-job shop and unit counts were computed on titles truncated to 90 characters; corrected values are in the README. Still 6 jobs.
- **E3:** brain dump fails a stricter bolt-on test, so **5 valid jobs** before Astra (6 if the "worksheet" exclusion is narrowed).
- **E4:** the claim that premium sits in Notion and apps is **retracted**. Notion and app/web are 17% of premium units.
- **E5:** "clone" means near-duplicate titles only. Product copying was not verified.
- **E6:** listing age is in whole months.

The provisional market is unchanged.
