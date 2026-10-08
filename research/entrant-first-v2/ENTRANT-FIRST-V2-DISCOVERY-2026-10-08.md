# LEDGER & LIME — ENTRANT-FIRST DISCOVERY V2 — 2026-10-08

**Result: NO WINNER.** No buyer cluster passed all seven Stage-15 gates, so no department is forced.

- Nothing was built, published, listed, advertised or spent. Etsy was not touched.
- The live Master is unchanged; see `MASTER-APPEND-2026-10-08-ENTRANT-FIRST-V2.md`.
- All figures are **EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA**.
- Reproduce with `sh run_all.sh`. Every number below is in `*_output.txt`, `*.json` or `*.csv`.

---

## 1. What changed from V1

The ADHD lesson was applied: **family depth is tested early, per job, and by code.**

**Stage 2 (buyer grouping)** assigns each listing to an exact buyer. Purchases made *for* the professional by fans or gift-givers are removed first: PNG/SVG, tumblers, shirts, embroidery and stickers. A "Nurse PNG" is not a nurse-workflow purchase.

**Stage 3 (five-job test)** gives every finalist 5–9 candidate jobs, each defined by:
- a regex
- a trigger
- an acquisition phrase
- a brand-fit label

**A job is VALID** when all three hold:
- ≥2 selling shops
- ≥1 CLEAN or ACTIVE shop
- it is not a SUBSTITUTE for the rest of the family

**A job is CREDIBLE** when it is VALID **and** its brand fit is not WEAK. WEAK covers design, gift and clinical/education content.

**Stage 4 (substitution)** labels each job COMPLEMENTARY, PARTIAL or SUBSTITUTE, with a one-line reason in `jobs.py`. Two data checks back the labels:
- **all-in-one unit share:** the share of a finalist's units sold by listings whose titles cover ≥3 jobs
- **substitute-job unit share:** the share of units in jobs labelled SUBSTITUTE

**Stage 7 (health)** classifies every listing with ≥100 units:
- **ACTIVE:** last-3-month units ≥15% of 12-month units
- **FADING:** below that
- **HISTORIC:** 0 units in the last 3 months
- **OTHER**

**Stage 15 gates** are coded in `jobs.py` and applied identically to every finalist. There are no weights:

| Gate | Rule |
|---|---|
| G1 | ≥2 clean entrants on the core job |
| G2 | ≥5 credible same-buyer jobs |
| G3 | ≥3 credible jobs with repeated paid evidence (≥2 selling shops) |
| G4 | ≥4 complementary relationships among credible jobs |
| G5 | Substitute-job units <50% |
| G6 | Flood survivable: not HIGH, or HIGH but ≥3 new shops still win among young listings |
| G7 | Price credible: <$5 unit share <50% **and** ≥2 credible jobs with median ≥$7 |

## 2. Stage 1 — broad entrant scan

**Pulls:** 50 entrant pulls with identical filters:
- digital listings only
- shop ≤24 months old
- shop sales ≤15k
- ≥100 units in the last 12 months
- sorted by units

They break down as:
- **29 V1 pulls,** reused unchanged as `raw/V1-Q-*`.
- **21 new V2 pulls** aimed at specific buyers: photographer, salon, esthetician, lash, breeder, landlord, Airbnb, contractor, realtor, real estate, daycare, childcare, nanny, nurse, nursing, RN, student, vendor, seller, horse, cleaning business.

**Further pulls:**
- 5 young-listing flood pulls (`F-`): nurse, real estate, esthetician, homeschool, wedding planner (V1).
- 3 exploratory any-shop pulls (`X-`): travel nurse, nurse planner, nurse schedule.
- 3 keyword pulls (`K-`).

**Result:** 2,099 unique listings → **653 CLEAN + 243 NEAR-CLEAN listings**, from **707 shops**, of which **520 have a CLEAN listing**.

Health split: 571 ACTIVE / 325 FADING / 431 HISTORIC / 772 OTHER.

There are **116 promising entrant shops** in specific-buyer clusters, against a target of 40–60; see `ENTRANT-SHOPS.csv`.

**Gap:** shop listing counts were not pulled. The proxy for "not a mass factory" is shop sales ≤15k plus the rule that a listing makes up ≥5% of shop sales. That rule also removes broad specialist catalogs; see SmartAgentDocs in §5.

## 3. Stage 2 — exact-buyer clusters (`buyers_output.txt`, 31 clusters)

| Buyer | Status | CLEAN shops | ACTIVE shops | Units | Top shop | Median $ |
|---|---|---|---|---|---|---|
| Esthetician / lash / nail / hair pro | candidate | 16 | 14 | 8,333 | 10% | 6.03 |
| Engaged couple (wedding admin) | candidate (#9 live, V2 HOLD) | 16 | 8 | 8,051 | 23% | 9.76 |
| **Nurse / nursing student** | candidate | 14 | 12 | 11,377 | 22% | 7.74 |
| Homeschool parent | candidate | 14 | 11 | 8,556 | 23% | 4.28 |
| Teacher (classroom) | candidate | 12 | 19 | 9,076 | 18% | 3.97 |
| Allied-health student | candidate | 5 | 5 | 2,132 | 23% | 15.50 |
| Landlord (legal forms) | candidate | 3 | 4 | 1,573 | 54% | 3.27 |
| Real estate agent | candidate | 3 | 3 | 1,276 | 40% | 20.00 |
| STR host / daycare provider / cleaning-business owner / photographer | candidate | 1–2 each | — | <1.7k each | ≥28% | — |
| ADHD, therapist/BCBA, notary, household readiness | **excluded by brief** | — | — | — | — | — |
| Budget, co-parenting, reseller, home baker, caregiver | live L&L families | — | — | — | — | — |
| Merch/design assets, crafts, IP, party/kids content, wedding decor | design buyers | 97 / 94 / 30 / 27 / 30 | — | — | — | — |

Two clusters were dropped before the five-job test:
- **Teacher (classroom)** is mostly gifts *for* teachers bought by parents, plus classroom decor; 68% of units sell under $5. Its buyer is not the teacher.
- **Allied-health student** is study content split across several professions.

**Finalists sent to the five-job test (5):** nurse, beauty service pro, homeschool parent, real estate agent, wedding couple (as a reference point).

## 4. Stages 3–5 and 15 — five-job test and gates (`jobs_output.txt`, `GATES.csv`)

| Finalist | Valid jobs | **Credible jobs** | Complementary (credible) | Flood | <$5 units | Substitute units | G1 | G2 | G3 | G4 | G5 | G6 | G7 | Pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Nurse / nursing student** | 7 | **4** | 2 | LOW | 21% | 34% | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | **NO** |
| Homeschool parent | 5 | 3 | 2 | MEDIUM | 76% | 0% | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | NO |
| Beauty service pro | 5 | 1 | 1 | **HIGH** | 65% | 0% | ✓ | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | NO |
| Real estate agent | 3 | 2 | 1 | **HIGH** | 10% | 0% | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | NO |
| Wedding couple | 2 | 2 | 0 | HIGH (89 young duplicate-title pairs) | 17% | **64%** | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | NO |

**Every finalist fails G2.** No buyer has five credible, distinct jobs with paid entrant proof.

## 5. Top 3 finalists

### 1. Nurse / nursing student — closest near-miss

**Buyer:** a working RN or a nursing student in clinicals. They overlap: students buy report sheets for clinicals.

**Jobs:**

| Job | Selling shops | Clean | Active | Units | Median $ | Relation | Fit | Credible |
|---|---|---|---|---|---|---|---|---|
| Shift report / handoff sheet | 7 | 3 | 2 | 2,865 | $5.00 | CORE | STRONG | ✓ |
| Patient assessment template | 2 | 1 | 0 | 910 | $7.04 | PARTIAL (report sheets embed assessment) | STRONG | ✓ |
| Career documents (resume, legal-nurse pivot) | 3 | 2 | 1 | 1,144 | $11.90 | COMPLEMENTARY | MEDIUM | ✓ |
| School planner / clinical tracker | 4 | 2 | 1 | 1,494 | $2.80 | COMPLEMENTARY | STRONG | ✓ |
| Unit recognition / Nurses Week | 5 | 0 | 1 | 897 | $4.00 | COMPLEMENTARY, but a different role (charge nurse) | WEAK (gift) | ✗ |
| Pharmacology reference | 7 | 3 | 4 | 2,054 | $10.00 | PARTIAL | WEAK (clinical liability) | ✗ |
| Bedside quick-reference | 6 | 2 | 0 | 1,771 | $8.00 | PARTIAL | WEAK (clinical liability) | ✗ |
| Course / exam study notes | 9 | 5 | 3 | 5,721 | $17.00 | **SUBSTITUTE** (4,400-page mega-note bundles) | WEAK | ✗ |

**Clean entrant examples:**
- TheNurseNest: report sheet, $6.66, 1,136 units, 12 of 12 months active, last 3 months 90/90/63
- RNGrind: SBAR sheet, $3.14, 320 units, 12 of 12 months active
- yournursebestieco: ICU report sheet, $5, 165 units
- ResumeInn: nurse resume, $11.90, 449 units
- AdvanceNursing: pharmacology, $6.42, 506 units
- SnookToSky, VetloSchool, Drumy: study content

**Recent entry:** 20 nurse-workflow listings ≤3 months old reached ≥30 units, 14 of them from new shops, with **0 duplicate-title pairs**.

**Why it fails:** the demand is one job in many variants.
- The exploratory "nurse planner" and "nurse schedule" pulls return report-sheet and shift-organizer variants across about 20 shops: 1/3/4/5/6/8-patient, CNA, charge nurse, LTC, ICU, MedSurg, hourly to-do.
- Every keyword door in the nurse map points to "report sheet" (11 of 14 terms; the other 3 are generic).
- Under the brief's rule, daily vs weekly versions and one sheet sold per specialty are variants of one job, not separate jobs.
- There is **no paid evidence** for money/admin jobs that would fit L&L. "Travel nurse" returns one $27 guide with 25 units. Pay, overtime, CEU and licence trackers do not appear.

**Remaining checks:**
- **Buyer language:** new grads must customise a brain sheet, and some units mandate their own sheet, which is an employer substitute ([nurse brain template page](https://tech.mozilla.com.tw/en/nurse-brain-template.html)). Many free templates exist.
- **Price:** MIXED. 21% of units sell under $5; report sheets have a median of $5; resumes $11.90.
- **Format:** PDF/Canva printable, plus Word for resumes.
- **Brand cost:** half the demand is clinical/education content, outside L&L, with liability risk.
- **Catalog overlap:** none; this would be a true expansion.

### 2. Homeschool parent

**Credible jobs (3):** planner (13 selling shops, 5 clean), transcript (3), diploma (2).

**Not credible:**
- **Attendance/compliance records:** 1 selling shop; invalid.
- **Curriculum and Bible crafts:** valid but WEAK, because they are content. The Bible-craft buyer also drifts to Sunday-school teachers.

**Entry and supply:** 95 young winners, 62 from new shops. The flood is mostly curriculum content.

**Why it fails:** price. **76% of units sell under $5**, and the planner, transcript and diploma medians are $3.50–$3.98.

**Buyer language:** record keeping is "a common worry" for state-law compliance and transcripts, but free templates are everywhere ([homeschool.com](https://homeschool.com/?p=149404), [AOP](https://www.aop.com/blog/how-to-create-a-homeschool-transcript)).

**History:** screened and dropped in Discovery 2.0; this pass confirms that.

### 3. Beauty service pro (esthetician, lash, nail, hair)

**Breadth:** the widest buyer: 175 listings in the pool, 16 clean shops, and 8 distinct jobs.

**But the depth is design, not admin:**
- Booking sites (Acuity), flyers, logos/cards and Instagram/reels are the only jobs with volume, and all are WEAK fit.
- The admin jobs have no clean or active shops: contracts/consent (1 shop), aftercare cards (2), price lists (10 shops).

**Flood is HIGH:**
- 47 duplicate-title pairs among young listings.
- Only 6 of 97 young listings reached ≥30 units.
- Monthly "booking flyers" at $1.99–3.99 sell for 1–5 months, then stop.

**Price:** 65% of units sell under $5.

**Buyer language:** consent, policy and aftercare forms are real needs, but free JotForm/MakeForm builders cover them ([JotForm lash consent](https://form.jotform.com/253348977780070)). Dept #2 already dropped salon/esthetician as Canva-led.

### Not in the top 3

- **Real estate agent:** SmartAgentDocs (20 months, 8.5k sales, ~40 listings) dominates every job; most of its listings fall under the 5% contribution rule. Design-led, with 53 young duplicate-title pairs.
- **Wedding couple:** all-in-one planners substitute for budget and guest-list jobs (64% of units); late entrants fail (5 of 94 young listings win).

## 6. Clone/flood, price and format summary (`FINALIST-JOBS.csv`)

| Finalist | Young listings | Young winners (≥30 units) | Winners from new shops | Duplicate-title pairs | PLR | <$5 | $5–9.99 | $10–14.99 | $15–24.99 | $25+ | Dominant format |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Nurse | 20 | 20 | 14 | 0 | 0 | 17% | 39% | 10% | 19% | 16% | PDF / Canva / Word |
| Homeschool | 95 | 95 | 62 | 5 | 0 | 56% | 34% | 0% | 3% | 8% | PDF |
| Beauty pro | 97 | 6 | 4 | 47 | 0 | 47% | 36% | 3% | 7% | 8% | Canva / app-web |

- Price-band shares are of units, per `buyers.json`.
- "Clone" here means **near-duplicate titles only**. No product files were inspected (Etsy returns 403).
- Young pools are top-100 *best-selling* samples, so they are not sell-through rates (V1 erratum E1).

## 7. Stage 13 — keyword doors (`keyword_map_output.txt`)

These were mapped diagnostically only, since no finalist passed. After deduplication:

| Finalist | Distinct terms | Where they point |
|---|---|---|
| Nurse | 14 | **11 are the report-sheet door** (nurse report sheet 555; medsurg 373; ICU 340; brain sheet 426); the other 3 are generic |
| Homeschool | 8 | **All 8 are the planner door** (home school planner 1,535) |
| Beauty pro | 11 | **All 11 are generic** "lash tech template / booking" terms |

The keyword space confirms the job-depth finding: **each buyer has one dominant door, not five.**

The brief's target was 15–30 terms per cluster. Deduplication left fewer, because the suggestions are mostly word-order variants of one door.

## 8. Stage 12 — catalog check

None of the three finalists overlaps #1–#18 or #19. All would be true expansions with no internal anchor product.

## 9. Recommendation

**Do not open a department from this pass.**

If Business HQ wants a follow-up, the only cluster with entrant health and low flood is **nursing workflow**. It would need *new* paid evidence for at least two L&L-fit nurse admin/money jobs, such as shift and overtime pay, CEU/licence renewal, or a new-grad job-search tracker. Those must come from listings that actually sell, not from seller ideas. Until then, nursing is a one-door market (report sheets), not a department.

---

```
MARKETS SCREENED = 31 buyer clusters (from 50 entrant pulls + 5 young-listing + 3 exploratory pulls)
CLEAN ENTRANTS REVIEWED = 520 shops with a CLEAN listing (707 incl. NEAR-CLEAN; 116 in specific-buyer clusters)
FINALIST BUYER CLUSTERS = 5 (nurse, homeschool parent, beauty service pro, real estate agent, wedding couple)
PROVISIONAL MARKET = NONE
CORE BUYER = NONE
VALID SAME-BUYER JOBS = 0 for a winner (closest: Nurse — 7 valid, 4 credible)
JOBS WITH >=2 SELLING SHOPS = 0 for a winner (closest: Nurse — 8)
VALID CLEAN ENTRANTS = 0 for a winner (closest: Nurse — 15 CLEAN shops; 3 on the core report-sheet job)
SUBSTITUTION RISK = MEDIUM (closest finalist: PARTIAL overlap between report and assessment sheets; study content is SUBSTITUTE, 34% of units)
CLONE/FLOOD RISK = LOW (closest finalist: 0 young duplicate-title pairs; beauty and real estate are HIGH)
PRICE DURABILITY = MIXED (closest finalist: 21% of units under $5; core job median $5; resume $11.90)
READY FOR ASTRA RED-TEAM = YES — to red-team the NO-WINNER decision, not a market
```
