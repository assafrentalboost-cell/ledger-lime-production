# Boring Micro-SaaS Import Research — US/UK/EU → Israel

**Date:** 2026-10-05 · **Mode:** research only (nothing bought, no accounts created, no companies contacted, no forms submitted)

---

## 0. Read this first: method, limits, and labels

**Labels used throughout**
- **[VERIFIED]**: stated on a first-party page, or by a marketplace/review platform, as surfaced in search results this session.
- **[FOUNDER-REPORTED]**: a revenue claim from the founder (interviews, Indie Hackers, podcasts). It is not audited.
- **[3RD-PARTY EST.]**: an estimate from Latka or a similar database. Treat it as weak.
- **[ESTIMATE]**: my own calculation or judgment.
- **[ASSUMPTION]**: a premise I chose so the work could continue. Check it before relying on it.

**Research limits (stated honestly)**
1. The research proxy blocked direct page fetches of Capterra, G2, Software Advice, Indie Hackers, Green Invoice (Morning) and reepli.ai. Pricing, review counts and review themes therefore come from **search-engine extractions of those pages and of first-party pricing pages**, not from my own reading of each page. Numbers may lag the live page by weeks.
2. **Task 4 (reading 20+ recent reviews per product) was not fully met.** I mined review *themes* from aggregated review summaries and from third-party review write-ups that quote reviewers. I did **not** read 20 individual reviews for each of the top 20. §4 marks each product's review evidence as THEMES-ONLY or THIN. Before committing build money to the winner, read the raw Capterra/G2 reviews by hand (about 1 hour).
3. Some reference products are from **Australia, Canada or New Zealand** (Content Snare, Paidnice, NiceJob, TutorBird, FileInvite). They are kept because they are the best-documented proof for their pattern. Each is flagged.
4. Review counts are **not** paying-customer counts, and downloads are **not** revenue. This report never treats one as the other.

---

## A. EXECUTIVE CONCLUSION

**Verdict: VALIDATE, DON'T BUILD YET.** One candidate is strong enough to justify a 14-day paid-validation sprint. None is strong enough to justify building blind.

**Winner to validate first: WhatsApp-first "missing documents chaser" for Israeli accounting and bookkeeping offices.** It works like this:
- Each client gets a checklist (bi-monthly VAT materials, annual-report documents such as Form 106, Form 867, donation receipts and life-insurance certificates).
- The client gets a personal mobile upload link.
- WhatsApp reminders go out automatically until the file is complete. They respect Shabbat and Jewish holidays.
- The office sees one status board: who is still missing what.

**Why this one:**
- **Strongest foreign proof in the set.** Content Snare, a chase-clients-for-documents tool, is founder-reported at $1M+ ARR. Accounting is its #1 vertical at about 40% of the business ([Indie Hackers via search](https://www.indiehackers.com/post/tech/stuck-at-300k-arr-until-pivoting-to-an-unlikely-industry-took-his-product-to-the-next-level-4q8N27PMPTYGDWwx0lmr)). Public pricing is $35–$215/mo ([Portico](https://www.portico.run/blog/post/content-snare-pricing)).
- **Structurally recurring pain.** Israeli bookkeeping runs on a monthly or bi-monthly VAT cycle plus an annual-report season. The office chases the same clients for the same documents, every cycle, forever.
- **Real Israeli advantage beyond translation:**
  - Israeli clients send documents on WhatsApp, not by email.
  - The checklist items are Israel-specific (106, 867, section 46 donations, credit points).
  - The calendar must follow Shabbat and holidays.
  - Content Snare's top complaint is that clients ignore emails from an unknown vendor domain ([search summary of G2 reviews](https://www.portico.run/blog/post/content-snare-review)). A WhatsApp message from the office itself fixes that.
- **B2B buyer with a known pain and a clear willingness-to-pay range** (₪149–₪549/mo). There are 32,148 active CPA licenses in Israel ([Wikipedia/Ministry of Justice register via search](https://he.wikipedia.org/wiki/%D7%9C%D7%A9%D7%9B%D7%AA_%D7%A8%D7%95%D7%90%D7%99_%D7%97%D7%A9%D7%91%D7%95%D7%9F_%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C)), plus tax advisors and bookkeepers. ₪10k MRR needs about 34 offices; ₪30k needs about 100.

**What could kill it (be skeptical):**
- **SUMIT** gives its clients a free upload portal, including WhatsApp intake ([SUMIT](https://www.sumit.co.il/books)).
- **Rivhit** and **Finbot** have document intake.
- **WellyBox** and **Lazy Invoice** collect receipts for business owners.
- Several Israeli automation freelancers already sell custom WhatsApp chase bots to accountants ([achiya-automation](https://achiya-automation.com/industries/accountants/), [auto-flow](https://auto-flow.co.il/%D7%90%D7%95%D7%98%D7%95%D7%9E%D7%A6%D7%99%D7%94-%D7%9C%D7%A8%D7%95%D7%90%D7%99-%D7%97%D7%A9%D7%91%D7%95%D7%9F/)).
- Local competition is therefore **MODERATE, not empty**. The bet is that a standalone chaser that works with any accounting software is simpler than switching to SUMIT, and more productized than a custom freelancer build. **The 14-day sprint exists to test exactly that bet.**

**Runner-up and fastest cash: "periodic-service recall" for Israeli technicians.** Targets are AC cleaning, water filters, pest control and fire-extinguisher servicing. It is sold **service-first** (we run the WhatsApp campaign that rebooks overdue customers and get paid per campaign or per booked job). It has the best time-to-first-shekel (8/10), but weaker standalone-SaaS proof and higher churn risk.

**Categories that look attractive abroad but are crowded in Israel:**
- **Appointment reminders.** Timing, Clickinder (₪99), Simple Tor (₪80) and Arbox already cover it.
- **Missed-call text-back.** Free Israeli apps exist: Sendy, Responder, Dial My App.
- **Review requests.** Be5 (₪150–₪500), Reepli (₪299 + ₪150 per agent), Holy Flow (₪989), RepuCare, MaxStars, B144 (₪29) and many agencies.
- **Payment chasing for micro-businesses.** Morning (Green Invoice) already sends automatic payment reminders to its 160k+ businesses.

---

## B. TOP 10 TABLE

| Rank | Product pattern | Foreign reference | Target customer (IL) | Foreign monthly price | Proof of payment | Israel competition | MVP difficulty | First-customer difficulty | Suggested Israeli price | MRR potential (12–18 mo) [ESTIMATE] | Main risk | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Client-document chaser for accounting offices | Content Snare, FileInvite, Clustdoc | CPA / tax-advisor / bookkeeping offices, 1–15 staff | $35–$215 (CS); Clustdoc from $190 | A: STRONG | MODERATE | EASY | MEDIUM | ₪149 / ₪299 / ₪549 | ₪15k–₪40k | SUMIT's free portal; conservative buyers | **78** |
| 2 | Periodic-service recall for technicians | GorillaDesk, Skimmer, Fire Inspected, Kukui | AC, water-filter, pest-control and extinguisher service firms | $49–$149 (GD); $49–$99 (FI); $200–$500 (Kukui) | B: MODERATE (recall is bundled in FSM suites) | LIGHT–MODERATE | EASY | EASY (service-first) | ₪199 / ₪349 / ₪599, or per booked job | ₪8k–₪25k | Messy customer data; anti-spam law; seasonality | **72** |
| 3 | Quote follow-up for contractors | Hatch, Followup CRM, Better Proposals | Renovation, solar, AC-install, aluminium and kitchen firms | Hatch ~$600–$900 (user-reported); BP from $19/user | B: MODERATE | MODERATE | EASY | MEDIUM | ₪199 / ₪349 | ₪8k–₪25k | Already a feature of CRMs and Reepli | **69** |
| 4 | Review-request automation | NiceJob, GatherUp, Grade.us | Local service businesses | $75–$125 (NiceJob); $99 (GatherUp) | A: STRONG | MODERATE–HEAVY | VERY EASY | MEDIUM (saturated pitch) | ₪149 / ₪249 | ₪5k–₪15k | Commoditized in IL; Google policy on gating | **68** |
| 5 | Payment-chasing add-on (WhatsApp escalation) | Chaser, Paidnice, InvoiceSherpa | B2B SMBs invoicing on net-30/60 terms (שוטף+) | £199+ (Chaser); $69+ (Paidnice); $49–$199 (IS) | A: STRONG | MODERATE–HEAVY | MEDIUM | MEDIUM | ₪199 / ₪399 | ₪6k–₪20k | Morning's built-in reminders; API needs Morning "Best" plan | **68** |
| 6 | Digital food-safety logs (HACCP-lite) | FoodDocs, Trail | Restaurants, caterers, central kitchens | $79–$299 (FD); £32–£71.5/site (Trail) | B: MODERATE | LIGHT (no Hebrew app found) | MEDIUM | HARD | ₪199 / site | ₪5k–₪20k | Unclear regulatory pull; restaurant churn | **67** |
| 7 | Supplier / subcontractor certificate tracking | Expiration Reminder, Remindax, TrackMyVendor | Construction firms, facility managers, mid-size SMB finance teams | $49–$499 (ER); $29+ (Remindax); $39–$59 (TMV) | B: MODERATE | MODERATE (ERPs, Visitt) | EASY | HARD (bigger buyer) | ₪299 / ₪599 | ₪5k–₪20k | Sales friction; ERP features | **64** |
| 8 | Appointment reminders | Apptoto, GoReminders | Clinics, salons, therapists | $30–$39 (Apptoto); $8–$30 (GoReminders) | A: STRONG | HEAVY | VERY EASY | HARD (crowded) | ₪79–₪99 | low | Price war with Israeli incumbents | **63** |
| 9 | Safety-service inspection log + due reminders | Fire Inspected, Inspect Point | Extinguisher and fire-safety service firms | $49–$99 (FI); up to $129/user (IP) | C: WEAK–MODERATE | LIGHT (not deeply verified) | MEDIUM | MEDIUM | ₪299 | ₪3k–₪10k | Tiny niche; IL standard forms unknown | **63** |
| 10 | STR digital guidebook | Touch Stay | Israeli STR hosts and managers | $99/yr for 1st property, down to $20/property/yr | B: MODERATE | LIGHT–MODERATE | EASY | EASY (operator network) | ₪39/property/mo | ₪2k–₪8k | Fails size filter (ARPU too low) | **62** |

How each score is built is in §12. Judgment overrides are explained there too.

---

## C. TOP 3 BUILD CANDIDATES (build only after the validation gate passes)

1. **Accounting-office document chaser** (#1). This is the best mix of proof, recurrence, retention and reachable buyers.
2. **Technician periodic-service recall** (#2). Build after 3+ service-first campaigns show booked-job ROI.
3. **Quote follow-up for contractors** (#3). Build only as a WhatsApp-first single-purpose tool, and only if interviews show contractors are not already using a CRM's follow-up feature.

## D. TOP 3 SERVICE-FIRST VALIDATION CANDIDATES

1. **Technician recall campaign as a service.** "Give us your customer list and we'll rebook your overdue customers on WhatsApp." Price: ₪490 per campaign, or ₪40–₪60 per booked job. This is the fastest route to first money.
2. **Concierge VAT-materials chasing for accounting offices.** We run the chase for one cycle for 30–50 of their clients, using n8n plus a simple upload page. Free first cycle, then ₪149/mo.
3. **Done-for-you quote follow-up.** We take the contractor's open-quotes list and run a 3-touch WhatsApp sequence. ₪390/mo, or a success fee.

## E. TOP 3 RESEARCH-ONLY CANDIDATES

1. **Digital food-safety logs.** No Hebrew product was found, but I could not verify whether Israeli enforcement actually forces restaurants to keep logs. Without a regulatory pull, restaurants will not pay.
2. **Supplier/subcontractor certificate tracking.** Strong Israel-specific document set (bookkeeping certificate, withholding-tax certificate, certificate of insurance, contractor license). However, the buyer is mid-size, sales take longer, and ERPs and Visitt partly cover it.
3. **Payment-chasing add-on for Morning/iCount/SUMIT users.** Strong foreign proof, but Morning already sends automatic reminders. The gap is only WhatsApp escalation plus statements for B2B net-terms businesses. Validate later as an *expansion* of the winner (accountants can resell it to their clients).

## F. REJECTED CATEGORIES

| Category | Why rejected |
|---|---|
| Appointment reminders / no-show tools | HEAVY Israeli competition: Timing (₪0–₪199), Clickinder (₪99), Simple Tor (₪80), Arbox, Easybizy, Senzey. Low ARPU; ₪10k MRR needs about 100+ customers ([search results](https://timingapps.com/), [Clickinder](https://www.clickynder.com/), [Simple Tor](https://simpletor.app/pricing)) |
| Missed-call text-back (standalone) | Free or cheap Israeli apps already do missed-call → WhatsApp: Sendy, Responder, Dial My App ([Sendy](https://www.sendy-auto-app.com/app/), [Ringless guide](https://ringless.co.il/u/0747916021/%D7%91%D7%9C%D7%95%D7%92/134/%D7%9E%D7%A2%D7%A0%D7%94-%D7%90%D7%95%D7%98%D7%95%D7%9E%D7%98%D7%99-%D7%91%D7%95%D7%95%D7%90%D7%98%D7%A1%D7%90%D7%A4)). Keep it only as a feature |
| Generic "AI WhatsApp agent for SMBs" | Saturated with agencies and productized offers: Reepli (₪299 + agents), Holy Flow (₪989), SmartRise (from ₪97), many freelancers. Also on the exclusion list (generic chatbot) |
| Driving-instructor management | HEAVY: DriveLog (₪179), Sivan, Dio, Wheel It, Adi Mobile ([search](https://www.cma-sivan.co.il/), [DriveLog](https://ai-lab.co.il/drivelog/index.html)) |
| Studio waivers / health declarations | HEAVY: Arbox, Fizikal, Tazman, Leap, Weekin bundle it; 2sign and FillFaster offer standalone forms |
| Tutor / class admin | Crowded: BaseCRM tutors module, Arbox for classes; TutorBird-style tool would be a "full system" |
| Garage MOT/service recall | MODERATE–HEAVY: Eyal Software, Mosikit, BotMotors, SMS vendors |
| STR cleaning marketplace (Turno-style) | Two-sided marketplace with network effects; outside the micro-SaaS profile |
| Testimonial collection (Senja / Testimonial.to) | Strong foreign revenue proof but **no** Israeli advantage. The global tool already serves Israel. Acquisition is SEO/PLG-driven |
| Agency client reporting (Swydo/Reportz) | Global tools and Looker Studio already serve Israeli agencies; no local advantage |
| GBP / local-SEO dashboards (Localo) | Heavy global tools plus B144 at ₪29/mo; data-heavy; localization is mostly translation |
| Failed-payment recovery (Churn Buster) | Needs processor integrations; Israeli processors are fragmented; the vendor itself says it only fits at roughly $500K+ ARR |
| Previous candidates: Debt Payoff Planner, Itemlist, Sweepy/Tody, DogLog, generic household apps | Consumer, low willingness to pay, local or free alternatives (unchanged from previous research) |

## G. ONE WINNER TO VALIDATE FIRST

**Accounting-office document chaser (WhatsApp-first).**
- Working name: **"TikMale" (תיק מלא, "full file")**. Trademark not checked.
- Positioning: *"Your clients' missing documents arrive by themselves. You only see who's still missing what."*

## H. EXACT 14-DAY PLAN

See §13.1 "14-day validation plan". In short:
- Days 1–3: build a list of 150 small offices; join 4 professional groups; write the interview script.
- Days 3–6: 15 short problem interviews; draft the Hebrew landing page.
- Days 5–10: run a concierge pilot with 3 offices on their *current* VAT cycle (30–50 clients each). Built with n8n + WhatsApp + a simple upload page. No SaaS build.
- Days 11–14: report completion metrics to each pilot office, ask for payment, decide go or kill.

## I. EXACT FIRST CUSTOMER OFFER

> **"Founding Office" offer (limited to 10 offices).**
> - We set everything up for you: we import your client list and write your checklists. No setup fee.
> - **First cycle free** (one VAT cycle or 50 annual-report clients).
> - From cycle 2: **₪149/month** for up to 100 active clients, **price locked for 12 months**, cancel anytime.
> - **Guarantee:** if completion by the deadline isn't better than your previous cycle, you don't pay for the next month.
> - Messages go out under your office's name, in polite Hebrew, never on Shabbat or holidays.

## J. EXACT MVP SPEC

See §13.1 "Exact MVP" (v0 click-to-send → v1 automated WhatsApp). The core is:
- Client list import
- Checklist templates
- Per-client magic-link upload page (RTL, mobile, camera)
- Reminder schedule with Shabbat/holiday blocking
- Status board
- Daily digest
- ZIP export

What it is not: no OCR, no bookkeeping, no accounting-software integration in v0.

## K. KILL CRITERIA

Stop (or pivot to runner-up #2) if **any** of these is true by day 14/30:
1. Fewer than **8 of 15** interviewed offices rank client-document chasing as a top-3 recurring pain.
2. **More than 50%** of interviewed offices already use SUMIT's portal (or a similar one) *and* are satisfied with it.
3. Fewer than **3 of 15** agree to a free concierge pilot.
4. The pilots fail to show a **≥25% relative improvement** in on-time completion (or ≥3 staff-hours saved per cycle, as reported by the office).
5. Fewer than **2 offices pay ≥₪149** by day 30.
6. Meta/WhatsApp blocks the use case (template rejection or verification failure) **and** the SMS fallback completion rate is under half the WhatsApp rate.

## L. SOURCES / EVIDENCE APPENDIX

See §15 at the end of this document.

---

# DETAILED WORK (Tasks 1–14)

## §1–2. TASK 1 + 2: 42 real products, monetization evidence

**Monetization evidence classes:**
- **A = STRONG:** public pricing, a large review base, and founder revenue or a large marketplace footprint.
- **B = MODERATE:** public pricing and dozens to hundreds of reviews.
- **C = WEAK:** pricing only, or very few reviews.
- **D = UNKNOWN.**

**Revenue type:**
- **V** = VERIFIED
- **FR** = FOUNDER-REPORTED
- **3P** = THIRD-PARTY ESTIMATE
- **U** = UNKNOWN

Country/founded marked "n/v" were not verified this session.

| # | Product | URL | Country | Founded | Exact problem solved | Target customer | Monthly price | Annual price | Trial / free | Core workflow | Integrations / dependencies | B2B/C | Reviews (count · rating · source) | Revenue (type) | Evidence class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Content Snare | contentsnare.com | Australia (flag: outside US/UK/EU) | 2017 | Chasing clients for documents and info | Accountants (about 40%), lawyers, brokers, agencies | $42–$258 monthly billing | $35–$215/mo billed annually | Free trial | Request template → client portal → auto-reminders → collected files | Zapier, Xero app, Practice Ignition | B2B | Capterra 34 · 4.9; G2 54 · 4.7 (search) | $1M+ ARR (FR, Indie Hackers Dec-2024); ~$990K (3P Latka) | **A** |
| 2 | FileInvite | fileinvite.com | NZ/US (flag) | n/v | Document collection for lending | Lenders, mortgage brokers | Older: $829–$2,499 | From $9,900/yr | Demo | Request → portal → reminders | Lending systems | B2B | Capterra: 97% positive (search) | U | **B** |
| 3 | Clustdoc | clustdoc.com | France | n/v | Client onboarding plus doc collection plus KYC | SMB/corporate onboarding teams | From $190 (3 seats) | n/v | Trial | Process template → forms/docs/e-sign → approval | KYC, e-sign | B2B | G2/Capterra 4.7 (search) | U | **B** |
| 4 | Chaser | chaserhq.com | UK | n/v | Chasing overdue invoices | SMBs on Xero/QBO | £199 (≤£4m turnover), £599, £899 | £179 / £539 | Trial | Sync invoices → schedules → email/SMS/call reminders → debt-collection escalation | Xero, QBO, Sage | B2B | Capterra UK (count n/v) | U | **A** (public tiered pricing, long-running) |
| 5 | Paidnice | paidnice.com | Australia (flag) | n/v | Payment reminders, late fees | SMBs on Xero/QBO | From $69 | n/v | Free trial | Sync → reminders/statements from own domain | Xero, QBO | B2B | Xero App Store 83 · 5.0; Capterra 14 · 4.9; Trustpilot 29 · 4.7 | U | **A** |
| 6 | InvoiceSherpa | invoicesherpa.com | US | n/v | Automated invoice reminders | SMBs | $49–$199 | n/v | Trial | Sync → reminder cadence → pay link | Xero, QBO, Wave, Sage, FreshBooks, Harvest | B2B | SelectHub/SA (count n/v) | U | **B** |
| 7 | Kolleno | kolleno.com | UK | n/v | Credit control and reconciliation | SMB/mid finance teams | $650/user ($545 annual) | — | Demo | AR workflows, portal | Accounting systems | B2B | G2 117 · 4.9 | U | **B** (priced above micro) |
| 8 | Churn Buster | churnbuster.io | US | ~2013 per vendor | Failed subscription payment recovery | Subscription businesses | From $249–$279 | — | — | Retries + email/SMS dunning | Stripe, Recharge, Shopify | B2B | Few public | U | **B** |
| 9 | NiceJob | nicejob.com | Canada (flag) | n/v | Automated review requests | Home/local services | $75 Reviews; $125 Pro | n/v | Trial | Job done → SMS/email request → follow-ups → widgets | Jobber, Housecall Pro, QBO… | B2B | Capterra 201–202 · 4.9; G2 305 · 4.8; Trustpilot 25 · 3.7 | U | **A** |
| 10 | GatherUp | gatherup.com | US | n/v | Review requests and NPS | Local businesses, multi-location | $99 single; $60/location (2–10) | n/v | Trial | Request → feedback → review | GBP, POS | B2B | Capterra/SA (count n/v); acquired Dec 2025 | U | **A** |
| 11 | Grade.us | grade.us | US | n/v | White-label review management | Agencies | $110 single; $40/location at 10 seats | n/v | Trial | Same as GatherUp | GBP | B2B | n/v | U | **B** |
| 12 | Trustindex | trustindex.io | Hungary | n/v | Display Google reviews on a site | SMB websites | — | $65 / $125 / $349 per yr | Free tier | Widget pulls reviews | 130+ review platforms | B2B | WP.org 2,524 · 4.9; 900k+ active installs | U | **A** (installs ≠ payers) |
| 13 | Senja | senja.io | UK/remote | 2022 | Collect and display testimonials | Creators, SaaS, SMB | Tiered (n/v) | n/v | Free tier | Form → collect → widget | Many | B2B | n/v | $1M ARR Nov-2025 (FR); $300K (3P 2024) | **A** |
| 14 | Testimonial.to | testimonial.to | US | 2020 | Video/text testimonials | Creators, SMB | Tiered (n/v) | n/v | Free tier | Same | Many | B2B | n/v | $1M+ ARR Apr-2025 (FR) | **A** |
| 15 | Localo | localo.com | Poland | n/v | Google Business Profile, local SEO tasks | Local SMBs, agencies | $39 single (annual); $149 Pro | yes | 14-day trial | GBP sync → tasks → posts/reviews | GBP | B2B | G2 136 · 4.9 | U | **B** |
| 16 | Apptoto | apptoto.com | US | n/v | Appointment reminders | Service practices | $39 (3 calendars) | $30 | Trial | Calendar sync → SMS/email/call reminders | Google/Outlook calendars, practice software | B2B | Capterra 94 · 4.8 | U | **A** |
| 17 | GoReminders | goreminders.com | US | n/v | SMS appointment reminders | Small practices | $8–$30 | yes | Trial | Calendar → reminders | Calendars | B2B | G2 219 · 4.9; Capterra 259 · 4.8 | U | **A** |
| 18 | Quo (ex-OpenPhone) | quo.com | US | n/v | Business phone incl. missed-call auto-reply | SMB teams | From $15/user | yes | Trial | Number → auto-replies | CRM integrations | B2B | n/v | U | **A** (but a broad phone system) |
| 19 | UpFirst.ai | upfirst.ai | n/v | n/v | AI answering + missed-call text | SMBs | From $24.95 | n/v | n/v | Answer/text/schedule | Calendar | B2B | n/v | U | **C** |
| 20 | TextBackMissedCall | textbackmissedcall.com | n/v | n/v | Missed-call text-back | Contractors | $100 + $100 setup | — | n/v | Missed call → SMS | Phone carrier | B2B | n/v | U | **C** |
| 21 | Hatch | usehatchapp.com | US | n/v | Estimate follow-up, lead reactivation | Home-improvement firms | ~$600–$900 (user-reported, no public price) | annual contracts | Demo | Unsold estimates → multi-touch SMS/email/voice | FSM/CRM (e.g., Hearth) | B2B | 77 · 4.3; Capterra 40 (35% negative) | U | **B** |
| 22 | Better Proposals | betterproposals.io | UK | n/v | Proposals with tracking and follow-up | Agencies, freelancers | From $19/user | yes | Trial | Template → send → track opens → sign/pay | Stripe, CRMs | B2B | Capterra 167 · 4.8; G2 50 · 4.3 | U | **A** |
| 23 | Followup CRM | followupcrm.com | US | n/v | Bid tracking and follow-up | Commercial contractors | ~$4,500/yr for 5 users (3rd-party report) | — | Demo | Bid pipeline → follow-up tasks | Construction tools | B2B | 312+ · 4.4 (aggregate) | U | **B** |
| 24 | Expiration Reminder | expirationreminder.com | US | n/v | Tracking expiring licenses, certificates, contracts | Ops/HR/compliance admins | $49–$499 (tiers $99/$179/$349) | n/v | Trial | Records + docs → email/SMS/WhatsApp reminders | Email/SMS/WhatsApp | B2B | 49 reviews, 94% positive | U | **B** |
| 25 | Remindax | remindax.com | n/v | n/v | Document expiry reminders | SMBs | From $29 | n/v | Free plan | Docs → reminders (WhatsApp on paid) | WhatsApp/SMS | B2B | 18 · 4.6 | U | **C** |
| 26 | TrackMyVendor | trackmyvendor.com | US (n/v) | n/v | Vendor COI tracking | Small contractors/PMs | $39–$59 | n/v | n/v | Vendor → COI upload → expiry alerts | — | B2B | n/v | U | **C** |
| 27 | FoodDocs | fooddocs.com | Estonia | n/v | Digital HACCP plan and food-safety logs | Restaurants, food producers | $99 / $199 / $299 | $79 / $167 / $250 | 14-day trial | Generate HACCP → daily log tasks → audit records | Sensors (optional) | B2B | 4.9 overall, 96% positive | U | **B** |
| 28 | Trail | trailapp.com | UK | n/v | Daily hospitality checklists and food-safety records | Restaurants, multi-site | £38/site (Team, monthly) | £32 / £65 / £71.5 per site | 14-day trial | Checklists per shift → evidence → reports | Sensors | B2B | Capterra 7 · 4.9 (thin) | U | **B** |
| 29 | Touch Stay | touchstay.com | UK | n/v | Digital guest guidebook | STR hosts, B&Bs | — | $99/yr first property; $20–$51 per extra | Trial | Build guide → auto-send to guest | PMS/channel managers | B2B | Thousands of hosts (vendor claim) | U | **B** |
| 30 | Turno | turno.com | US | n/v | STR cleaning scheduling and marketplace | STR hosts | $8/property (free for 1) + 5% per clean | $72/yr | Free tier | Calendar sync → auto-assign cleaner → pay | Airbnb, PMS | B2B | Cleaners app iOS ~1,000 · 3.8; 82–167 · 4.6–4.7 | U | **B** |
| 31 | Smartwaiver | smartwaiver.com | US | n/v | Digital liability waivers | Activity businesses, gyms | From $18 (usage-based) | n/v | Free version | Waiver link/kiosk → signed record | — | B2B | Capterra 51 · 4.8 | U | **B** |
| 32 | GorillaDesk | gorilladesk.com | US | n/v | Recurring route service (pest/lawn/pool) | Small service firms | $49 / $99 / $149 | n/v | 14-day trial | Recurring jobs → routes → reminders → invoicing | QBO, payments | B2B | Software Advice 277 · 4.8; Capterra 4.9; 290+ across G2/Capterra | U | **A** |
| 33 | Skimmer | getskimmer.com | US | n/v | Pool-route service | Pool-service firms | $1/pool (min $49) or $2/pool (min $98) | n/v | First month free | Route → service log → customer emails → billing | Payments | B2B | Mixed; complaints about price increases | U | **B** |
| 34 | Squeegee | squeeg.ee | UK | n/v | Round management for window cleaners | Window/round cleaners | From £9.80–£19 | n/v | Free tier | Rounds → reminders → payments | Payments | B2B | Google Play 295 · 4.1; Trustpilot 4.9 | U | **B** |
| 35 | Fire Inspected | fireinspected.com | n/v | n/v | Extinguisher inspections and due reminders | Fire-safety service firms | Free / $49 / $99 | — | Free tier | Barcode → NFPA form → PDF → 30/14/7-day reminders | — | B2B | n/v (new product) | U | **C** |
| 36 | Inspect Point | inspectpoint.com | US | n/v | Fire-protection inspections | Fire-protection contractors | Up to $129/user (annual) | annual | Demo | Inspection forms → reports → billing | — | B2B | value-for-money 3.2/5 | U | **B** |
| 37 | Kukui | kukui.com | US | n/v | Auto-shop marketing, service reminders | Auto repair shops | $200–$500+ | n/v | Demo | Shop management system data → mileage/date reminders → reactivation | Shop management systems | B2B | Capterra 4.8 (count n/v) | U | **B** |
| 38 | TutorBird | tutorbird.com | Canada (flag) | n/v | Tutor scheduling, invoicing, payment chasing | Private tutors, small schools | From $16.95 | yes | Trial | Calendar → attendance → invoice → reminders | Payments | B2B | Capterra 263 · 4.8 | U | **A** |
| 39 | Total Drive | totaldrive.co.uk | UK | n/v | Driving-instructor diary, pupils, payments | Driving instructors | £18–£26 | n/v | 30-day trial | Diary → lessons → progress → payments | Payments | B2B | 30 · 5.0 | U | **B** |
| 40 | Swydo | swydo.com | Netherlands | n/v | Automated client reporting | Marketing agencies | From $69 (10 sources) | −10% | Trial | Connect sources → scheduled reports | Ads/analytics APIs | B2B | G2/Capterra positive (count n/v) | U | **B** |
| 41 | Reportz | reportz.io | n/v | n/v | SEO client dashboards | SEO agencies | $9.90/dashboard | n/v | Trial | Connect → dashboards | SEO APIs | B2B | n/v | U | **C** |
| 42 | Fixflo | fixflo.com | UK | n/v | Tenant repair reporting and triage | Letting agents, block managers | £50 + £0.35–£0.95/property | n/v | Demo | Tenant reports issue → triage → contractor | PMS | B2B | Trustpilot mixed; claims 40% of UK letting agents | U | **A** (market share claim is the vendor's) |

**Israeli reference points (not part of the 42):**
- Gaviti (Tel Aviv, AR automation, mid-market, quote-based)
- WellyBox (Tel Aviv, receipt collection, from ~$19/mo)
- Morning/Green Invoice (160k+ businesses; Basic ₪29, Extra ₪74)
- SUMIT
- Reepli, Be5, Holy Flow
- Timing, Clickinder, Simple Tor
- DriveLog, Sivan, Dio
- Visitt
- Arbox

## §3. TASK 3: size filter

Reference revenue math (Task 3):
- 50 × ₪199 = **₪9,950 MRR**
- 100 × ₪299 = **₪29,900 MRR**
- 200 × ₪399 = **₪79,800 MRR**

**Rejected or flagged by the size filter** (needs hundreds or thousands of payers, or ARPU under ₪100):
- Appointment reminders (₪79–₪99)
- STR guidebook (about ₪39 per property; needs about 260 paid properties for ₪10k)
- Squeegee-style round apps
- Driving instructors (₪150–₪180, with crowded supply)
- Testimonial widgets
- Trustindex-style widgets (annual, low ARPU)

**Passes** (one customer can reasonably pay ₪149–₪999/mo):
- Accounting-office chaser
- Technician recall
- Quote follow-up
- Certificate tracking
- Food-safety logs (per site)
- Payment-chasing add-on
- Review requests (borderline at ₪149–₪249)

## §4. TASK 4: review mining → "Product Gap" summaries (top 20)

Evidence depth is labeled **THEMES-ONLY** (aggregated review summaries plus quoted reviewer lines from third-party write-ups) or **THIN** (fewer than 15 public reviews).

| # | Pattern / reference | Most loved | Main complaints | Missing / wanted | Cancellation & pricing signals | Evidence depth | **Product Gap for Israel** |
|---|---|---|---|---|---|---|---|
| 1 | Doc chaser / Content Snare, FileInvite, Clustdoc | Automatic reminders mean "I stopped chasing"; templates; one place for files | **Emails come from the vendor's domain, so clients ignore them or mark them as spam**; setup of reminder rules is confusing; non-technical clients struggle; no digest, so per-comment emails pile up ([Portico/G2 themes](https://www.portico.run/blog/post/content-snare-review)) | Sending from the firm's own identity; simpler client UX; e-sign/payments bundled (Clustdoc) | Pro tier ($119+) seen as pricey vs. all-in-one suites; Clustdoc gates basics behind tiers | THEMES-ONLY | **WhatsApp from the office's own name; zero-login magic link; Israeli doc checklists; Shabbat-aware schedule; daily digest instead of per-event noise** |
| 2 | Recall / GorillaDesk, Skimmer, Kukui | Reminders cut no-shows; customers confirm by text; recurring scheduling | Support gaps; sync bugs; hard to turn off reminders for specific customers; **price increases** (Skimmer reportedly $1→$2 per pool) | Simpler recall without the full FSM; per-customer control | Price hikes are the main churn trigger | THEMES-ONLY | **Recall-only tool (no dispatch/invoicing) on WhatsApp, priced flat; "due list" from a messy Excel** |
| 3 | Quote follow-up / Hatch, Followup CRM, Better Proposals | Follow-up timing; open tracking; persistence closes deals | Hatch: 35% negative on Capterra (sample 40); Followup: 60-day cancellation clause, billing after cancellation; expensive | Lightweight, month-to-month, no CRM migration | Contracts and price are the core complaints | THEMES-ONLY | **No contract, no CRM: forward a quote PDF or connect Morning quotes → 3-touch WhatsApp sequence** |
| 4 | Reviews / NiceJob, GatherUp | Set-and-forget review requests; review count rises | Review gating gray area; reviews disappearing; cold-call sales; billing after cancel (Trustpilot 3.7) | Honest, compliant flow; cheaper | "A little pricey" for very small businesses | THEMES-ONLY | Gap is small in Israel (already crowded). Only defensible as a **feature** of #1–#3 |
| 5 | Payment chasing / Chaser, Paidnice, InvoiceSherpa | "Paid for itself"; reminders that run alone; statements | Chaser repriced to £199+ (turnover bands) and alienates small firms; Kolleno far too expensive for SMBs | Cheap, simple, WhatsApp | Price bands are the main friction | THEMES-ONLY | **WhatsApp escalation + statement of account + "חשבון עסקה" logic for net-terms B2B**. But Morning covers the basics |
| 6 | Food logs / FoodDocs, Trail | Easier HACCP; cheaper than consultants; daily checklists | Monthly fee "challenging" for one-person food businesses; features still in development (Trail) | Cheaper tier; sensors optional | Price for micro-kitchens | THEMES-ONLY / THIN (Trail 7 reviews) | Hebrew tablet checklist + temperature log + PDF for inspector, **but the regulatory pull is unverified** |
| 7 | Certificates / Expiration Reminder, Remindax | Never miss a renewal; central dashboard | Remindax: customer-service responsiveness, doc deletion concerns | Supplier self-upload; WhatsApp | — | THIN | **Israeli certificate types + supplier WhatsApp self-upload link** |
| 8 | Appointment reminders / Apptoto, GoReminders | Fewer no-shows (one cites −80%); easy | Price increases ("others cheaper even free") | — | Cheaper alternatives | THEMES-ONLY | No gap (Israel crowded) |
| 9 | Safety inspection / Inspect Point, Fire Inspected | Industry forms; field ease | Value-for-money 3.2/5; iOS-only; annual contracts; setup fee | Android, month-to-month, cheap | Contracts and price | THIN | Hebrew forms per Israeli standard + Android + WhatsApp due reminders (niche) |
| 10 | STR guidebook / Touch Stay | Fewer guest questions; better reviews | (few public complaints) | — | Low ARPU | THIN | Hebrew/English guide + WhatsApp delivery; too small |
| 11 | Testimonials / Senja | Easy collection, widgets | — | — | — | THIN | No local gap |
| 12 | GBP / Localo | Clear tasks; easy | Visibility numbers don't match Google | — | — | THEMES-ONLY | B144 ₪29 + agencies; no gap |
| 13 | Agency reporting / Swydo | Easy, customizable reports | Cost scales with data sources | — | Per-source pricing | THEMES-ONLY | No local gap |
| 14 | Missed-call / Quo etc. | Captures leads | — | — | — | THIN | Free IL apps; no gap |
| 15 | Tutors / TutorBird | All-in-one; value | Invoices confuse parents | — | — | THEMES-ONLY | Crowded IL |
| 16 | Driving / Total Drive | Saves time daily; support | — | — | — | THIN | Crowded IL |
| 17 | Waivers / Smartwaiver | Simple, effective | Pricey; links only | — | — | THEMES-ONLY | Crowded IL (studio suites) |
| 18 | Repairs / Fixflo | Fewer calls/arguments; work halved | Mixed contractor quality | — | — | THEMES-ONLY | Visitt + ועד בית apps; medium gap, bigger buyer |
| 19 | Garage recall / Kukui | Reminders, reactivation, reviews | Price | — | — | THIN | Eyal/Mosikit/BotMotors; crowded |
| 20 | Turno | Automation of cleaning | 5% fee per clean adds up | — | — | THEMES-ONLY | Marketplace; out of scope |

## §5. TASK 5: Israel competitor check (top 20)

| # | Pattern | Israeli players found | Class | Why |
|---|---|---|---|---|
| 1 | Accounting doc chaser | SUMIT (free client portal incl. WhatsApp intake for SUMIT offices), Rivhit (scanned-doc intake), Finbot (AI doc scanning), Formally (client archive), WellyBox and Lazy Invoice (receipt collection for business owners), TextMe (SMS for accountants), automation freelancers (achiya-automation, auto-flow, STSiconic) | **MODERATE** | Strong players exist, but they are **suites** (switching cost) or **custom builds** (agency cost). I found no standalone Hebrew "checklist + WhatsApp chase + status board" product that works with any accounting software. Freelancers selling exactly this workflow is a demand signal, not an absence of competition |
| 2 | Technician recall | Field-service suites (Tachzukanit/Ramdor, CONBOX, 2Link, Priority add-ons), CRMs with reminders (Senzey, BaseCRM, Easybizy), generic WhatsApp/SMS senders (ActiveTrail, TextMe, SMS4Free) | **LIGHT–MODERATE** | No recall-specific product for small technician firms was found. Generic tools can do it if someone configures them |
| 3 | Quote follow-up | Kala CRM (quotes + automatic follow-up), tik-tok.co.il (quotes + CRM + e-sign), Gold Systems (renovation quotes), Reepli (follow-up agent ₪150), Powerlink/Fireberry/Monday CRMs | **MODERATE** | Exists as a CRM feature; few sell it standalone |
| 4 | Review requests | Be5 (₪150–₪500 + per-survey fee), Reepli, Holy Flow (₪989), RepuCare, MaxStars, B144 GBP (₪29), many agencies | **MODERATE–HEAVY** | Crowded; prices already anchored low (₪29–₪150) |
| 5 | Payment chasing | Morning built-in auto reminders (160k+ businesses), SUMIT, iCount, Gaviti (mid-market), Sogomatic/Otomation WhatsApp collection bots, DigiShops, Build App (ועד בית) | **MODERATE–HEAVY** | The low end is covered inside invoicing tools |
| 6 | Food-safety logs | None found in Hebrew; Ministry of Health guidance requires temperature documentation in some contexts; consultants run paper logs | **LIGHT** (search depth limited) | No Hebrew SaaS surfaced; paper and Excel dominate |
| 7 | Certificate tracking | ERPs (Priority, Hashavshevet withholding-tax interface), Visitt (insurance certificates for buildings), Excel | **MODERATE** | Partially covered in ERPs; SMB gap is unclear |
| 8 | Appointment reminders | Timing, Clickinder, Simple Tor, Touri, Arbox, Easybizy, Plannie, SMS vendors | **HEAVY** | — |
| 9 | Safety-inspection log | Not found specifically; general FSM tools | **LIGHT** (not deeply verified) | — |
| 10 | STR guidebook | Duve (Israeli, hotel-focused), Hostfully/Touch Stay used directly, PMS built-ins (Hospitable, Hostaway) | **LIGHT–MODERATE** | — |
| 11 | Testimonials | Global tools serve Israel | **HEAVY (global)** | — |
| 12 | GBP / local SEO | B144, agencies, Localo | **HEAVY** | — |
| 13 | Agency reporting | Global tools, Looker Studio | **HEAVY (global)** | — |
| 14 | Missed-call | Sendy, Responder, Dial My App (free), Voicenter features | **HEAVY** | — |
| 15 | Tutors / classes | BaseCRM tutors, Arbox | **HEAVY** | — |
| 16 | Driving instructors | DriveLog, Sivan, Dio, Wheel It, Adi Mobile | **HEAVY** | — |
| 17 | Waivers / health declarations | Arbox, Fizikal, Tazman, Leap, 2sign, FillFaster | **HEAVY** | — |
| 18 | Repair reporting | Visitt, Build App, ועד בית apps | **MODERATE** | — |
| 19 | Garage recall | Eyal Software, Mosikit, BotMotors | **MODERATE–HEAVY** | — |
| 20 | STR cleaning marketplace | Turno usable in Israel; local cleaners via WhatsApp groups | **MODERATE** | — |

## §6. TASK 6: Israeli localization advantage (beyond translation)

| # | Pattern | Genuine Israeli advantages | Translation-only? |
|---|---|---|---|
| 1 | Doc chaser | **WhatsApp-first** (Israeli clients send docs via WhatsApp); **Israeli doc taxonomy** (106, 867, section 46 donation receipts, life-insurance/pension certificates, credit-point forms, reserve-duty documents); **VAT cycle cadence** (monthly or bi-monthly); **Shabbat/holiday-aware sending**; Israeli phone normalization; **independent of accounting software** (Hashavshevet/Rivhit/Priority/SUMIT); office-branded messages | **No**, real workflow fit |
| 2 | Technician recall | WhatsApp booking replies; Israeli seasons (pre-summer AC cleaning, pre-winter heating); local service intervals (water-filter changes, extinguisher annual checks); Bit/payment-link deposit | No |
| 3 | Quote follow-up | WhatsApp; "הצעת מחיר → חשבון עסקה" document flow (Morning quote webhook); Israeli negotiation culture (fast reply, price objections) | Partly |
| 4 | Reviews | WhatsApp delivery; Hebrew | **Mostly translation** (rejected as standalone) |
| 5 | Payment chasing | שוטף+30/60 culture; "חשבון עסקה" before tax invoice; Bit/Grow payment links; WhatsApp escalation | Partly, but the incumbent already localized |
| 6 | Food logs | Hebrew staff UI, kashrut/mashgiach notes, Israeli regulator forms | Partly (regulatory pull unverified) |
| 7 | Certificates | Bookkeeping and withholding-tax certificates (annual), standard certificate-of-insurance form, contractor license | **No**, strongly local |

## §7. TASK 7: MVP replication analysis (top 20, condensed)

Common stack [ASSUMPTION]:
- Next.js (or Lovable/Bolt-generated React) with RTL Tailwind on Vercel
- Supabase (Postgres, Auth, Storage, Edge Functions, cron) in an **EU region**
- n8n (self-hosted ~$10/mo, or cloud) for sequences
- WhatsApp Cloud API via Meta directly, or an Israeli/global BSP
- SMS fallback via an Israeli provider (e.g., 019/InforU/TextMe)
- Email via Resend
- Sentry and Better Stack free tiers

**Billing:** Stripe does not support Israeli-registered merchants [ASSUMPTION, verify]. Use Grow (Meshulam), Cardcom, PayPlus or Tranzila recurring billing, plus Morning for invoices. A merchant-of-record such as Paddle is an alternative.

| # | Pattern | Frontend needs | Backend / automation | AI needed? | Integrations | Build time (AI-assisted) [EST.] | Infra / 100 customers [EST.] | Complexity | Main tech risk | Maintenance risk | Support burden |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Doc chaser | Office login; client import (CSV/Excel); checklist templates; status board; settings (sender name, schedule); **client magic-link mobile upload page (no login, RTL, camera)** | Postgres tables (offices, clients, requests, items, files, reminders); cron for reminders; holiday calendar (Hebcal); storage with signed URLs; ZIP export | **No for MVP.** Later, a vision model to auto-classify uploads ("is this a 106?") | WhatsApp Cloud API (or v0 click-to-send wa.me links); SMS fallback; email | **v0: 5–7 days; v1: 2–3 weeks** | ~$350–$600/mo (Supabase Pro $25 + storage ~$10 + hosting $20 + WhatsApp ≈ 100 offices × ~800 utility msgs × ~$0.005 ≈ $400) | **EASY** (v0) → **MEDIUM** (per-office WhatsApp numbers via Embedded Signup) | WhatsApp template approval and sender identity; Meta business verification | Meta policy and pricing changes (e.g., the Oct-2026 change) | Client upload help ("my link doesn't work"); office onboarding |
| 2 | Technician recall | Customer import, "due list", campaign builder, reply inbox | Due-date rules per service type; cron; reply routing to owner WhatsApp | Optional: parse messy Excel | WhatsApp (marketing vs. utility classification), SMS, Google Calendar (optional), payment link | 1–2 weeks | ~$150–$500 (message-volume driven) | EASY | Template classified as **marketing** (higher cost, opt-in rules) | Data hygiene | Owners send messy lists |
| 3 | Quote follow-up | Quote list, sequence settings, status | Morning webhook "document created (quote)" → sequence; stop on reply/approval | Optional reply classification | Morning API (needs **Best** plan), WhatsApp | 1–2 weeks | ~$100–$300 | EASY–MEDIUM | Detecting "won" status | Morning API changes | Low |
| 4 | Reviews | Contact upload, request link, private feedback page | Trigger → request → 1 follow-up | Optional reply drafting | WhatsApp, GBP review link | 3–5 days | ~$100 | VERY EASY | Google gating policy | Low | Low |
| 5 | Payment chasing | Debtor list, cadence, statement page | Sync open invoices; cadence; stop on payment | No | Morning/iCount/SUMIT APIs, WhatsApp, payment links | 2–3 weeks | ~$150 | MEDIUM | Reliable "paid" status sync | 3 integrations | Medium (disputes) |
| 6 | Food logs | Tablet checklist UI, temp entry, photo, manager PDF | Task schedules per shift; overdue alerts | No | Optional Bluetooth/LoRa sensors (later) | 2–3 weeks | ~$100 | MEDIUM | Offline kitchen Wi-Fi | Content per regulation | Medium (staff training) |
| 7 | Certificates | Supplier list, required docs, expiry board | Supplier self-upload link; expiry reminders; optional OCR of expiry date | Optional OCR | WhatsApp, email | 1–2 weeks | ~$100 | EASY | Extracting expiry dates | Low | Low–medium |
| 8 | Appointment reminders | Calendar sync | Reminder jobs | No | Google Calendar | 1 week | ~$200 (SMS) | VERY EASY | — | — | Medium |
| 9 | Safety inspection | Mobile forms, barcode, PDF | Due rules | No | — | 2–3 weeks | ~$100 | MEDIUM | Offline mobile | Standards content | Medium |
| 10 | STR guidebook | Guide builder, guest page | Auto-send on booking | Optional | iCal/PMS | 1–2 weeks | ~$50 | EASY | PMS integrations | Low | Low |
| 11–20 | Rejected patterns | — | — | — | — | — | — | Mostly EASY–MEDIUM | — | — | — |

**Legal and privacy notes (all top candidates):**
- **Anti-spam law:** Israel's Communications Law §30A requires prior consent for *advertising* messages. Recall and marketing campaigns need an existing-customer basis or consent, and must include an opt-out. Service and transactional reminders (document requests, payment reminders) are lower risk. [ASSUMPTION: legal interpretation, get counsel]
- **Privacy:**
  - The Privacy Protection Law (Amendment 13, in force Aug-2025) and the Data Security Regulations (2017) apply.
  - Doc chaser specifically: the files include IDs and income data. Expect "medium" or "high" security level, encryption at rest, access logs, and a processor agreement with each office.
  - Host in the EU (Israel has EU adequacy).
- **WhatsApp Business policy:** utility templates must be non-promotional. Business verification is required for scale.

## §8. TASK 8: business economics (Israeli pricing)

Arithmetic is exact at the stated ARPU. Margins and churn are [ESTIMATE].

| # | Pattern | Proposed tiers | Blended ARPU | ₪10k MRR | ₪30k MRR | ₪50k MRR | Variable cost / customer / mo | Gross margin | Support cost | Churn risk | Upsell | Annual plan | Setup fee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Doc chaser | ₪149 (≤100 clients) / ₪299 (≤300) / ₪549 (≤800, multi-staff) | ₪299 | 34 | 101 | 168 | ₪15–₪40 (messages + storage) | **85–92%** | Low after onboarding; seasonal peaks | **Low–medium** (embedded in a recurring cycle) | AI doc-check, client e-sign, payment-chasing add-on, annual-report season pack | Yes (2 months free) | ₪0–₪490 (import service) |
| 2 | Technician recall | ₪199 / ₪349 / ₪599, or ₪40–₪60 per booked job | ₪349 | 29 | 86 | 144 | ₪30–₪120 (marketing templates) | 70–85% | Medium (lists, replies) | **Medium–high** (seasonal; "I have enough work") | Review requests, quote follow-up | Possible | ₪490 list clean-up |
| 3 | Quote follow-up | ₪199 / ₪349 | ₪249 | 41 | 121 | 201 | ₪10–₪30 | 88–92% | Low | Medium | Payment chasing | Yes | ₪0 |
| 4 | Reviews | ₪149 / ₪249 | ₪199 | 51 | 151 | 252 | ₪5–₪15 | 90%+ | Low | **High** (value saturates) | Reply drafting | Yes | ₪0 |
| 5 | Payment chasing | ₪199 / ₪399 | ₪249 | 41 | 121 | 201 | ₪10–₪30 | 88% | Medium (disputes) | Medium | Collections escalation | Yes | ₪0 |
| 6 | Food logs | ₪199 per site | ₪249 | 41 | 121 | 201 | ₪5 | 90% | Medium | High (restaurant churn) | Sensors | Yes | ₪490 HACCP setup |
| 7 | Certificates | ₪299 / ₪599 | ₪399 | 26 | 76 | 126 | ₪10 | 90% | Low–medium | Low | Supplier onboarding pack | Yes | ₪990 |
| 8 | Appointments | ₪79–₪99 | ₪89 | 113 | 338 | 562 | ₪20 SMS | 70% | Medium | High | — | — | — |
| 9 | Safety inspection | ₪299 | ₪299 | 34 | 101 | 168 | ₪5 | 90% | Medium | Low | — | Yes | ₪490 |
| 10 | STR guidebook | ₪39/property | ₪39 | 257 props | 770 | 1,283 | ₪2 | 90% | Low | Medium | Upsells | Yes | — |

(The rejected patterns 11–20 fail on competition or ARPU before economics matter.)

## §9. TASK 9: acquisition path (first 20 Israeli customers)

| # | Pattern | Easiest first channel | Other channels | Sales friction | Demo needed? | Phone selling? | Self-serve realistic? |
|---|---|---|---|---|---|---|---|
| 1 | Doc chaser | **Direct WhatsApp/LinkedIn messages to small offices** (1–10 staff) from public CPA/bookkeeper directories, plus **posts in accountant/bookkeeper Facebook groups** showing a before/after completion stat | Bookkeeping-course alumni; partnerships with bookkeeping trainers; later Google Ads on high-intent Hebrew keywords (e.g., "איסוף מסמכים מלקוחות") | **Medium**: conservative, trust-driven buyers; time-poor in deadline weeks | Yes (10-min screen share) | Light (15 interviews, not mass calling) | After ~20 customers, yes |
| 2 | Technician recall | **Direct WhatsApp to owner-operators** listed on d.co.il / pro.co.il (e.g., 2,166 AC-technician listings on d.co.il), with an ROI offer ("pay per booked job") | Supplier distributors (filter and AC-parts wholesalers) as referral partners | **Low–medium**: the outcome is concrete money | No (results-based) | Some | Low initially (service-first) |
| 3 | Quote follow-up | Direct to renovation/solar/AC-install firms; Morning-user groups | Contractor FB groups | Medium | Yes | Some | Medium |
| 4 | Reviews | Direct outreach showing competitor review gaps | Agencies (white-label) | Medium–high (saturated pitch) | No | Yes | Yes |
| 5 | Payment chasing | **Via accountants** (they see clients' receivables) | Morning-user groups | Medium | Yes | Some | Medium |
| 6 | Food logs | **Food-safety consultants** as resellers | Restaurant groups | High | Yes | Yes | Low |
| 7 | Certificates | Finance managers in construction/facility firms (LinkedIn) | Insurance brokers as partners | High | Yes | Yes | Low |

**Penalties applied:**
- Reviews: saturated pitch.
- Food logs: restaurants are hard to sell to, and churn is high.
- Certificates: longer B2B cycle.
- Appointments: price war.
- Testimonials, GBP: SEO-dependent.

## §10. TASK 10: service-first options

| # | Manual service | Price | Delivery | Customers to validate | What becomes software |
|---|---|---|---|---|---|
| 1 | "We chase your clients' missing VAT or annual-report documents for one cycle" | First cycle free → ₪149/mo | Office's client list → n8n + WhatsApp (or click-to-send) + Tally/Supabase upload page → weekly status sheet | 3 pilots, 2 paying | Checklist engine, magic-link uploads, reminder scheduler, status board |
| 2 | "We rebook your overdue customers" | ₪490/campaign or ₪40–₪60 per booked job | Clean Excel → segment due customers → WhatsApp campaign → replies forwarded to owner | 3 campaigns with ≥10 bookings each | Due-date engine, campaign builder, reply inbox |
| 3 | "We follow up every open quote" | ₪390/mo or 2% of won quote value | Weekly list of open quotes → 3-touch sequence | 3 firms | Morning-webhook sequence engine |
| 4 | Review generation done-for-you | ₪149–₪249/mo | Post-job list → WhatsApp request | 3 | Request automation (commodity) |
| 5 | Collections desk for overdue invoices | ₪299/mo + success fee | Accountant shares aged-debtors list → WhatsApp/phone cadence | 3 | Cadence engine |

## §11. TASK 11: copyability and defensibility (1 = low, 5 = high)

| # | Pattern | Technical replication ease | Incumbent lock-in | Switching cost (once ours) | Network effects | Data moat | Integration moat | Regulatory moat | Local moat | Differentiation difficulty | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Doc chaser | 5 | 2 (SUMIT users locked; others free) | **4** (client lists, templates, history) | 1 | 2 | 2 | 2 (privacy compliance as a trust moat) | **4** | 3 | **Good**: easy to build, low incumbent lock-in for non-SUMIT offices, sticky once adopted |
| 2 | Recall | 5 | 1 | 3 | 1 | 2 | 1 | 1 | 3 | 3 | Good for service; thin moat as SaaS |
| 3 | Quote follow-up | 5 | 3 (CRMs) | 3 | 1 | 1 | 3 (Morning webhook) | 1 | 3 | 4 | Medium |
| 4 | Reviews | 5 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 5 | Poor |
| 5 | Payment chasing | 4 | 4 (Morning built-in) | 3 | 1 | 2 | 3 | 1 | 3 | 4 | Medium–poor |
| 6 | Food logs | 4 | 1 | 4 | 1 | 2 | 1 | 3 | 4 | 2 | Good *if* the regulatory pull exists |
| 7 | Certificates | 5 | 3 (ERPs) | 4 | 2 (supplier side) | 2 | 2 | 2 | 4 | 3 | Medium |

## §12. TASK 12: scores (0–100) and time-to-first-paying-customer (0–10)

**Weights:** Proof 20 · Israel gap 15 · MVP simplicity 15 · Recurring value 15 · Acquisition 15 · Low support 10 · Margin 5 · Expansion 5.

| Rank | Pattern | Proof /20 | Gap /15 | MVP /15 | Recur /15 | Acq /15 | Support /10 | Margin /5 | Expand /5 | **Total** | **TTFPC /10** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Accounting doc chaser | 17 | 9 | 12 | 14 | 10 | 7 | 5 | 4 | **78** | 6 |
| 2 | Technician recall | 13 | 10 | 13 | 11 | 11 | 6 | 4 | 4 | **72** | **8** |
| 3 | Quote follow-up | 14 | 7 | 12 | 11 | 9 | 7 | 5 | 4 | **69** | 6 |
| 4 | Review requests | 18 | 4 | 14 | 8 | 8 | 8 | 5 | 3 | **68** | 6 |
| 5 | Payment-chasing add-on | 18 | 4 | 10 | 13 | 8 | 6 | 5 | 4 | **68** | 5 |
| 6 | Food-safety logs | 13 | 11 | 11 | 12 | 6 | 5 | 5 | 4 | **67** | 3 |
| 7 | Certificate tracking | 12 | 8 | 13 | 10 | 6 | 7 | 5 | 3 | **64** | 3 |
| 8 | Appointment reminders | 17 | 2 | 13 | 13 | 5 | 7 | 4 | 2 | **63** | 4 |
| 9 | Safety-inspection log | 10 | 9 | 10 | 13 | 7 | 6 | 5 | 3 | **63** | 4 |
| 10 | STR guidebook | 13 | 8 | 13 | 6 | 8 | 7 | 5 | 2 | **62** | 7 |
| 11 | Testimonials | 17 | 3 | 12 | 7 | 4 | 8 | 5 | 3 | 59 | 4 |
| 12 | Garage recall | 12 | 5 | 11 | 10 | 8 | 6 | 4 | 3 | 59 | 5 |
| 13 | Tutors / classes | 16 | 2 | 9 | 13 | 6 | 5 | 5 | 2 | 58 | 4 |
| 14 | Waivers / health declarations | 13 | 2 | 13 | 9 | 6 | 8 | 5 | 2 | 58 | 4 |
| 15 | Repair reporting | 14 | 5 | 9 | 11 | 5 | 5 | 5 | 3 | 57 | 3 |
| 16 | GBP / local SEO | 14 | 4 | 8 | 9 | 7 | 6 | 4 | 3 | 55 | 5 |
| 17 | Agency reporting | 14 | 3 | 8 | 12 | 6 | 5 | 4 | 3 | 55 | 4 |
| 18 | Missed-call text-back | 12 | 1 | 12 | 9 | 6 | 7 | 5 | 2 | 54 | 6 |
| 19 | Driving instructors | 11 | 1 | 9 | 13 | 8 | 5 | 5 | 1 | 53 | 4 |
| 20 | STR cleaning marketplace | 13 | 4 | 6 | 11 | 5 | 4 | 4 | 3 | 50 | 3 |

**Judgment overrides (why I am not simply taking the arithmetic order):**
- **Reviews (#4) and payment chasing (#5) score well only because their foreign proof is excellent.** In Israel, both are already sold cheaply or bundled (B144 ₪29; Morning's automatic reminders). They are demoted to *features* or *research-only*.
- **Technician recall (#2) beats the winner on time-to-first-cash (8 vs. 6)**, but its proof is for *bundled* field-service suites, not standalone recall. Its churn is seasonal. It is kept as the **parallel cash test**, not the primary build.
- **Food logs (#6) has the biggest visible Israel gap (no Hebrew SaaS found).** It is still research-only, because an empty market without a verified regulatory or buyer pull is the "low competition is not enough" trap from previous rounds.
- **STR guidebook (#10)** matches the operator's skills but **fails the size filter**.

## §13. TASK 13: deep dives, top 7

### 13.1 Accounting-office document chaser (WINNER)

- **Foreign references:**
  - **Content Snare** (AU): $35–$215/mo; founder-reported $1M+ ARR; accounting is about 40% of the business.
  - **FileInvite** (lending, $9.9k+/yr).
  - **Clustdoc** (FR, from $190/mo).
  - Adjacent proof: Israeli freelancers sell custom chase automations to accountants.
- **Evidence of payment:**
  - Public paid tiers (Content Snare, Clustdoc, FileInvite).
  - Content Snare: Capterra 34 reviews · 4.9 and G2 54 · 4.7 (search).
  - Founder revenue disclosure (Indie Hackers, Dec-2024).
  - Note: review counts are modest. The strongest proof is the founder ARR plus years of paid tiers.
- **Exact workflow (Israel):**
  1. The office imports its client list from an Excel export.
  2. It picks a template, such as "דו-חודשי מע״מ – עוסק מורשה" or "דוח שנתי – שכיר עם החזר".
  3. The system sends each client a WhatsApp message from the office's name with a personal link.
  4. The client photographs or uploads each item, or marks "לא רלוונטי".
  5. Reminders go out on day 3, 7 and 12. None go out on Friday afternoon, Shabbat or holidays.
  6. The office sees a board (מלא / חלקי / לא התחיל) and gets a daily digest.
  7. The office downloads a ZIP per client and period.
- **Why customers pay monthly:**
  - The chasing never ends. VAT runs monthly or bi-monthly and annual reports come every year.
  - Each missed document delays a filing, risks a fine, and costs staff time.
  - Content Snare's buyers pay *because* reminders replace a person.
- **What reviews reveal:**
  - Clients ignore messages from unknown senders.
  - Reminder configuration is confusing.
  - Too many notifications.
  - Non-technical clients struggle.
  - All four are solvable with office-branded WhatsApp, fixed sensible defaults, a digest, and a no-login link.
- **Israeli competition:** MODERATE (see §5). The key threat is SUMIT's free portal for SUMIT-using offices. Positioning: "Works with whatever bookkeeping software you use."
- **Israeli differentiation:**
  - WhatsApp-first
  - Israeli document checklists
  - Holiday-aware cadence
  - Office-branded sender
  - Hebrew microcopy for older clients
  - Works alongside Hashavshevet/Rivhit/Priority/SUMIT
- **Exact MVP:**
  - **v0 (5–7 days), no WhatsApp API:**
    - Office login (Supabase magic link).
    - Client import (CSV/XLSX paste) with 05X → +9725X normalization.
    - 4 templates (VAT bi-monthly, VAT monthly, annual-report salaried, annual-report self-employed), editable.
    - Request creation (bulk) with due date.
    - Client magic-link page: RTL, mobile, camera, multi-file, "not relevant" toggle, progress bar.
    - Reminder queue that produces **click-to-send wa.me links** for staff (sent from their own WhatsApp; no Meta approval needed).
    - Status board.
    - Daily email digest.
    - ZIP export.
    - Holiday calendar (Hebcal).
    - Audit log.
  - **v1 (+1–2 weeks):**
    - Automated WhatsApp Cloud API sending with approved Hebrew utility templates, from a verified shared sender showing the office name. Later, per-office numbers via Embedded Signup.
    - SMS fallback.
    - Tiered limits.
    - Recurring billing (Grow/Cardcom/PayPlus).
- **What NOT to build:**
  - OCR or data extraction
  - Bookkeeping
  - Integrations with Hashavshevet/Rivhit
  - E-signature
  - Client chat
  - Native mobile app
  - Payments
  - AI chatbot
  - Multi-language
- **Likely stack:** Next.js + Supabase (EU) + n8n + WhatsApp Cloud API + Resend + Hebcal API. Build time: v0 about 1 week, v1 about 3 weeks total [ESTIMATE].
- **Monthly infra:** about $50 at 10 customers; about $350–$600 at 100 customers, mostly WhatsApp messages [ESTIMATE].
- **Pricing:**
  - ₪149 (≤100 active clients)
  - ₪299 (≤300)
  - ₪549 (≤800, 5 staff)
  - Annual plan: 2 months free
  - Founding offices: ₪149 locked for 12 months
- **First 20-customer plan:**
  1. Build a list of 150 small offices (public CPA directories, d.co.il, Google Maps).
  2. Send 15 personal WhatsApp/LinkedIn messages a day. The hook is a 60-second screen-recording of the client upload flow.
  3. Post a value piece in 3–4 accountant/bookkeeper Facebook groups: "How we cut missing-document chasing by X% in one VAT cycle", using data from the concierge pilots.
  4. Run 3 concierge pilots → 3 case studies → referral ask (accountants talk to accountants).
  5. Target 20 paying offices within about 60–90 days [ESTIMATE].
- **Service-first version:** see §10 row 1.
- **Landing headline:** *"המסמכים של הלקוחות מגיעים לבד. אתם רואים רק מי עוד חסר."* ("Your clients' documents arrive on their own. You only see who's still missing.")
- **Offer:** see §I.
- **3 names** (trademark checks pending): **TikMale (תיק מלא)**, **Hasser (חסר)**, **Shalem (שלם)**.
- **14-day validation plan:**

  | Day | Action | Output |
  |---|---|---|
  | 1 | List 150 offices; join 4 groups; write the interview script (current process, tools, hours per cycle, % late clients, SUMIT use, willingness to pay) | List + script |
  | 2–3 | Send 50 personal messages; book 15 × 15-minute calls | 15 interviews booked |
  | 3–6 | Run interviews; draft the Hebrew landing page (Lovable/WordPress) with a waitlist and the founding-office offer | Pain ranking, SUMIT-use rate |
  | 4–6 | Concierge stack: Tally/Supabase upload page per client + n8n reminder schedule + click-to-send WhatsApp | Working pilot kit |
  | 6–10 | 3 pilots on their live cycle (30–50 clients each) | Completion data vs. last cycle |
  | 11–12 | Send each pilot a one-page result; ask for ₪149/mo from the next cycle | Payment decisions |
  | 13–14 | Go/kill review against §K | Decision |

- **30-day plan:**
  - Days 15–21: build v0 (only if ≥2 of 3 pilots agree to pay).
  - Days 15–30: 30 more outreach messages and 1 group post with case-study numbers; target 5 paying offices.
  - Day 30: kill or continue (≥5 paying, or ≥2 paying plus ≥10 qualified trials).
- **Kill criteria:** see §K.
- **Remaining unknowns:**
  - Share of small offices on SUMIT (and their satisfaction with its portal).
  - Whether offices accept a third-party processor holding client IDs and income documents.
  - Meta template approval for Hebrew document-request templates.
  - Willingness to pay ₪149+ when WhatsApp itself is "free".
  - Seasonality of annual-report demand vs. VAT steadiness.

### 13.2 Technician periodic-service recall

- **Foreign references and proof:**
  - **GorillaDesk:** $49–$149; 277 reviews · 4.8 on Software Advice. Recurring service is its core.
  - **Skimmer:** $1–$2 per pool.
  - **Kukui:** $200–$500 auto-shop reminders and reactivation.
  - **Fire Inspected:** $49–$99 with 30/14/7-day due reminders.
  - **Proof class B:** recall is proven as a *paid feature* inside suites. Standalone recall-only revenue is unproven.
- **Workflow:**
  1. Import past customers with last service date and type.
  2. The rules engine computes who is due (AC 12 mo, water filter 6–12 mo, pest 3 mo, extinguisher 12 mo).
  3. Send a WhatsApp offer with reply buttons (Book / Later / Stop).
  4. Replies go to the owner.
  5. Booked jobs are counted.
- **Why monthly:** a steady flow of rebookings; seasonal spikes before summer and winter.
- **Reviews:** price hikes and complexity are the churn triggers. Owners want simple, per-customer control.
- **Israeli competition:** LIGHT–MODERATE (FSM suites, generic senders).
- **Differentiation:** recall-only, WhatsApp-native, Hebrew, Israeli seasons, pay-per-result entry.
- **MVP:** importer + rules + campaign + reply routing (1–2 weeks).
- **NOT:** dispatch, invoicing, routes, technician app.
- **Pricing:** ₪199 / ₪349 / ₪599, or ₪40–₪60 per booked job in the service phase.
- **First 20:**
  - Direct WhatsApp to owner-operators listed on d.co.il / pro.co.il (AC, filters, pest control, extinguishers).
  - Offer: "No booked jobs → no pay".
  - Partner with filter and parts wholesalers.
- **Headline:** *"הלקוחות הישנים שלכם כבר צריכים טיפול. אנחנו נזכיר להם."* ("Your past customers already need a service. We'll remind them.")
- **Names:** BaZman (בזמן), TorHaba (התור הבא), Tipul Kavua (טיפול קבוע).
- **14-day:**
  1. 20 owner conversations.
  2. 3 campaigns run manually with n8n.
  3. Measure booked jobs per 100 messages.
  - Kill if under 3 bookings per 100 due customers, or owners refuse to pay ₪490 after seeing results.
- **Unknowns:**
  - Message classification (marketing pricing and anti-spam law consent)
  - Data quality
  - Seasonality

### 13.3 Quote follow-up for contractors

- **References:**
  - **Hatch:** about $600–$900/mo user-reported; vendor data says 43% of deals close on days 2–30.
  - **Followup CRM:** 312+ reviews.
  - **Better Proposals:** Capterra 167 · 4.8.
- **Israel:** MODERATE (Kala CRM, tik-tok.co.il, Gold Systems, Reepli follow-up agent).
- **Wedge:**
  - A Morning "quote created" webhook → 3-touch WhatsApp sequence that stops when the quote is converted. Needs the Morning **Best** plan for API access.
  - Or forward a quote PDF to a WhatsApp number.
- **MVP:** 1–2 weeks.
- **Pricing:** ₪199–₪349.
- **First 20:** Morning-user and contractor groups; renovation/solar firms.
- **Names:** Sagarnu (סגרנו), Hatzaa Chama (הצעה חמה), Follo.
- **Headline:** *"כל הצעת מחיר מקבלת מעקב. אף עסקה לא נשכחת."* ("Every quote gets followed up. No deal gets forgotten.")
- **Kill:** if more than 50% of interviewees already use CRM follow-ups, or fewer than 3 of 15 pilot.
- **Unknowns:** how many contractors issue quotes in Morning vs. Word/WhatsApp text.

### 13.4 Review requests (feature-grade, not standalone)

- **References:** NiceJob ($75–$125; Capterra 201 · 4.9; G2 305 · 4.8; Trustpilot 3.7/25), GatherUp ($99), Grade.us ($110).
- **Israel:** MODERATE–HEAVY. Recommendation: **bundle** as a free add-on to #2/#3. Do not launch standalone.
- **Names:** Kochav, Hamlatza, Tov Lishmoa.
- **Kill:** if any standalone test fails to beat Be5/Reepli on price and outcome.

### 13.5 Payment-chasing add-on

- **References:** Chaser (£199–£899 by turnover band), Paidnice ($69+; Xero 83 · 5.0), InvoiceSherpa ($49–$199), Kolleno (G2 117 · 4.9, $545+).
- **Israel:** Morning sends automatic reminders already. Gaviti covers mid-market.
- **Wedge:** a WhatsApp escalation ladder plus statement of account for B2B net-terms firms, sold **through accountants** as an upsell of the winner.
- **Status:** research-only until the winner has 20 offices.
- **Names:** Shotef (שוטף), Tashlum Ba, Gvia Ezra.

### 13.6 Food-safety logs

- **References:** FoodDocs ($79–$299; 4.9 overall), Trail (£32–£71.5/site; only 7 Capterra reviews).
- **Israel:** LIGHT (no Hebrew SaaS found). The Ministry of Health requires temperature documentation in some contexts, but the enforcement pull on restaurants is unverified.
- **Validate via 10 food-safety consultants (יועצי תברואה)** as a reseller channel before anything else.
- **Names:** Yoman Mitbach, Kar-Cham (קר-חם), BikoretOK.
- **Kill:** if consultants say inspectors accept paper and owners won't pay ₪199/site.

### 13.7 Supplier/subcontractor certificate tracking

- **References:**
  - **Expiration Reminder:** $49–$499; 49 reviews.
  - **Remindax:** $29+; 18 reviews.
  - **TrackMyVendor:** $39–$59.
  - The US COI market (myCOI/illumend, Jones) proves enterprise demand.
- **Israel:**
  - The bookkeeping and withholding-tax certificates renew annually. Withholding-tax certificates are valid until March 31 and often renew automatically.
  - The standard certificate-of-insurance form applies to contractors.
  - Visitt covers buildings; ERPs cover part of it.
- **Buyer:** construction and facility firms. Longer sales cycle.
- **Research-only.**
- **Names:** Betokef (בתוקף), Ishurim, Tokef.

## §14. TASK 14: finalists vs. old candidates

Cell codes:
- **B** = finalist BETTER than the comparator
- **W** = WORSE
- **U** = UNCLEAR

"RentalBoost" is assumed to be the operator's existing STR-host service business [ASSUMPTION].

Dimensions: Speed to first money · Recurring value · Build difficulty (B = easier) · Competition (B = less) · Acquisition (B = easier) · Retention · MRR potential.

**vs. Debt Payoff Planner (consumer)**

| Finalist | Speed | Recur | Build | Compet. | Acquis. | Retention | MRR |
|---|---|---|---|---|---|---|---|
| Doc chaser | B | B | U | U | B | B | B |
| Tech recall | B | B | U | B | B | U | B |
| Quote f/u | B | B | U | U | B | B | B |
| Reviews | B | U | B | W | U | U | B |
| Payment add-on | U | B | W | W | U | B | B |
| Food logs | W | B | W | B | W | U | B |
| Certificates | W | B | U | U | W | B | B |

Debt Payoff Planner sits on free calculators, faces a financial-advice boundary, and makes about ₪20 per user. Every B2B finalist wins on MRR.

**vs. Itemlist / Sweepy / Tody (consumer household apps):** the same pattern as above. All finalists win on willingness to pay, MRR potential and the acquisition path (a reachable buyer list vs. app-store luck). They are U or W only on build simplicity, where the consumer apps are similar or simpler.

**vs. generic AI video SaaS**

| Finalist | Speed | Recur | Build | Compet. | Acquis. | Retention | MRR |
|---|---|---|---|---|---|---|---|
| Doc chaser | B | B | B | B | B | B | U |
| Tech recall | B | B | B | B | B | U | U |
| All others | B | B | B | B | U | B | U |

Generic AI video SaaS is commoditized with high inference costs. The finalists are boring, so competitors are less motivated to enter, and their margins are higher.

**vs. generic AI lead-follow-up SaaS**

| Finalist | Speed | Recur | Build | Compet. | Acquis. | Retention | MRR |
|---|---|---|---|---|---|---|---|
| Doc chaser | U | B | B | **B** | B | B | U |
| Tech recall | B | U | B | B | B | U | U |
| Quote f/u | U | U | U | U (overlaps) | U | U | U |
| Reviews | U | W | B | W | W | W | W |

Israel already has Reepli, Holy Flow, SmartRise and dozens of agencies selling "AI WhatsApp follow-up". The doc chaser avoids that arena entirely. Its buyer (an accountant) is not targeted by those players.

**vs. RentalBoost as a service business [ASSUMPTION about its nature]**

| Finalist | Speed | Recur | Build | Compet. | Acquis. | Retention | MRR |
|---|---|---|---|---|---|---|---|
| Doc chaser | W | B | W | U | W | B | B |
| Tech recall | U | U | W | U | U | W | U |
| STR guidebook | B | U | W | U | B | U | W |

RentalBoost is faster to cash, because it is an existing network and needs no build. The doc chaser has better recurring value per hour of labor and a higher automation ceiling. **Recommendation:** keep RentalBoost as the cash engine, and run the 14-day doc-chaser sprint alongside it (about 1–1.5 hours a day).

---

## §15. SOURCES / EVIDENCE APPENDIX

### Foreign products: pricing, reviews, revenue
- Content Snare pricing: [Portico pricing breakdown](https://www.portico.run/blog/post/content-snare-pricing) · [Capterra profile](https://www.capterra.com/p/167019/Content-Snare/) · [Portico review (G2 complaint themes)](https://www.portico.run/blog/post/content-snare-review) · [Capterra reviews](https://www.capterra.com/p/167019/Content-Snare/reviews/) · [G2 reviews](https://www.g2.com/products/content-snare/reviews) · [Xero App Store reviews](https://apps.xero.com/us/app/content-snare/reviews)
- Content Snare revenue: [Indie Hackers – $300k ARR plateau to $1M+ (FR)](https://www.indiehackers.com/post/tech/stuck-at-300k-arr-until-pivoting-to-an-unlikely-industry-took-his-product-to-the-next-level-4q8N27PMPTYGDWwx0lmr) · [Latka estimate (3P)](https://getlatka.com/companies/contentsnare.com) · [Starter Story](https://www.starterstory.com/content-snare-breakdown) · [About](https://contentsnare.com/about/)
- FileInvite: [pricing](https://www.fileinvite.com/pricing) · [Capterra reviews](https://capterra.com/p/138728/FileInvite/reviews/)
- Clustdoc: [G2](https://www.g2.com/products/clustdoc/reviews) · [Portico review](https://www.portico.run/blog/post/clustdoc-review)
- Chaser: [pricing](https://www.chaserhq.com/chaser-pricing) · [Paidnice analysis of Chaser bands](https://www.paidnice.com/blog/chaser-pricing-alternatives)
- Paidnice: [reminder software page](https://www.paidnice.com/reminder-software) · [Capterra](https://www.capterra.com/p/254868/Paidnice/)
- InvoiceSherpa: [SelectHub](https://www.selecthub.com/p/accounts-receivable-software/invoicesherpa/)
- Kolleno: [Trove pricing analysis](https://trove.works/kolleno-pricing-alternatives/)
- Churn Buster: [dunning page](https://churnbuster.io/dunning/) · [SubRevival review](https://subrevival.com/reviews/churn-buster-review)
- NiceJob: [pricing](https://get.nicejob.com/pricing) · [Capterra](https://www.capterra.com/p/142037/NiceJob/) · [Fervor Studio review (Trustpilot split, gating)](https://fervorstudio.ca/news/nicejob-review-pricing-alternatives/)
- GatherUp / Grade.us: [Capterra GatherUp](https://www.capterra.com/p/239159/GatherUp/) · [Reputation Insider](https://www.reputation-insider.com/gatherup-review/)
- Trustindex: [WiserReview plugin test](https://wiserreview.com/blog/google-reviews-plugin-for-wordpress/)
- Senja: [Latka (3P)](https://getlatka.com/companies/senja.io#funding) · [IdeaIndex case study (FR)](https://www.ideaindex.so/case-studies/senja)
- Testimonial.to: [Creator Economy interview (FR)](https://creatoreconomy.so/p/damon-chen-engineer-to-one-million) · [Bootstrapped Founder](https://thebootstrappedfounder.com/a-conversation-with-damon-chen/)
- Localo: [pricing](https://localo.com/pricing) · [Search Atlas review](https://searchatlas.com/blog/localo-review/)
- Apptoto: [pricing](https://www.apptoto.com/pricing) · [Capterra reviews](https://www.capterra.com/p/168852/Apptoto/reviews/)
- GoReminders: [reviews page](https://www.goreminders.com/reviews-ratings)
- Missed-call tools: [Quo roundup](https://www.quo.com/blog/missed-call-text-back-software/) · [HelpGenie pricing](https://helpgenie.ai/blog/missed-call-text-back-software-pricing/) · [TextBackMissedCall](https://textbackmissedcall.com/) · [UpFirst](https://upfirst.ai/solutions/missed-call-text-back)
- Hatch: [estimate follow-up](https://www.usehatchapp.com/solutions/estimate-follow-up) · [ServiceAgent pricing write-up](https://serviceagent.ai/blogs/hatch-pricing/) · [Capterra pricing](https://www.capterra.com/p/174914/Hatch/pricing/)
- Better Proposals: [Capterra](https://www.capterra.com/p/153794/Better-Proposals/)
- Followup CRM: [Vertigraph comparison](https://www.vertigraph.com/vs/followup-crm-alternative) · [Software Finder](https://softwarefinder.com/construction/followup-crm)
- Expiration Reminder: [Capterra](https://www.capterra.com/p/172196/Expiration-Reminder/) · [Software Advice](https://www.softwareadvice.com/cms/expiration-reminder-profile/)
- Remindax: [Capterra CA](https://www.capterra.ca/software/167502/remindax) · [features](https://www.remindax.com/features)
- COI tracking market: [Vertikal pricing guide](https://www.vertikalrms.com/article/how-much-does-coi-tracking-software-cost-2026-pricing-guide/) · [TrackMyVendor comparison](https://trackmyvendor.com/compare-coi-tracking-software)
- FoodDocs: [pricing](https://www.fooddocs.com/pricing) · [G2](https://www.g2.com/products/fooddocs/reviews)
- Trail: [pricing](https://trailapp.com/pricing) · [Capterra](https://www.capterra.com/p/176765/Trail/)
- Touch Stay: [site](https://touchstay.com/) · [27 cents a day page](https://touchstay.com/happier-guests-for-just-27-cents-a-day)
- Turno: [site](https://turno.com/) · [App Store](https://apps.apple.com/us/app/turno-cleaners/id1263301809)
- Smartwaiver: [Capterra](https://www.capterra.com/p/168238/Smartwaiver/)
- GorillaDesk: [Software Advice](https://www.softwareadvice.com/field-service/gorilladesk-profile/) · [Capterra reviews](https://www.capterra.com/p/130290/GorillaDesk/reviews/)
- Skimmer: [pricing](https://www.getskimmer.com/pricing) · [Jobber alternatives article](https://www.getjobber.com/academy/pool-service/skimmer-pool-software-alternatives/)
- Squeegee: [Trustpilot](https://uk.trustpilot.com/review/squeeg.ee) · [Google Play](https://play.google.com/store/apps/details?id=com.squeegee&hl=en_GB)
- Fire Inspected: [pricing](https://fireinspected.com/pricing/) · Inspect Point: [FireITM review](https://fireitm.com/software/inspect-point/)
- Kukui: [Capterra](https://www.capterra.com/p/164990/Kukui-All-in-One-Success-Platform/)
- TutorBird: [Capterra reviews](https://www.capterra.com/p/181623/TutorBird/reviews/)
- Total Drive: [site](https://totaldrive.co.uk/) · [PassReady price check](https://passready.co.uk/blog/best-driving-instructor-software-2026.html)
- Swydo / Reportz: [Swydo automation tools](https://www.swydo.com/blog/best-report-automation-tools/)
- Fixflo: [lettings](https://www.fixflo.com/solutions/lettings) · [Software Finder](https://softwarefinder.com/property-management-software/fixflo-lettings)

### Israel: competitors and market
- Morning / Green Invoice: [auto payment reminder help page](https://www.greeninvoice.co.il/help-center/app-payment-reminder/) · [pricing](https://www.greeninvoice.co.il/pricing/) · [API plan requirement notes (community)](https://github.com/danielrosehill/Green-Invoice-API-My-Notes) · [Apiary API](https://jsapi.apiary.io/apis/greeninvoice.html)
- SUMIT: [books / portal](https://www.sumit.co.il/books) · [portal help collection](https://help.sumit.co.il/he/collections/3233254-%D7%A4%D7%95%D7%A8%D7%98%D7%9C-%D7%94%D7%A0%D7%94%D7%9C%D7%AA-%D7%97%D7%A9%D7%91%D7%95%D7%A0%D7%95%D7%AA)
- Rivhit for accountants: [page](https://www.rivhit.co.il/%D7%A4%D7%AA%D7%A8%D7%95%D7%A0%D7%95%D7%AA-%D7%9C%D7%A0%D7%99%D7%94%D7%95%D7%9C-%D7%9E%D7%A9%D7%A8%D7%93%D7%99-%D7%9E%D7%99%D7%99%D7%A6%D7%92%D7%99%D7%9D/) · Finbot: [site](https://www.fin-bot.co.il/) · Formally: [page](http://www.formally.co.il/AccountsForms.aspx)
- WellyBox: [Hebrew site](https://he.wellybox.com/) · Lazy Invoice: [site](https://lazyinvoice.co.il/)
- Accountant automation freelancers: [achiya-automation](https://achiya-automation.com/industries/accountants/) · [auto-flow](https://auto-flow.co.il/%D7%90%D7%95%D7%98%D7%95%D7%9E%D7%A6%D7%99%D7%94-%D7%9C%D7%A8%D7%95%D7%90%D7%99-%D7%97%D7%A9%D7%91%D7%95%D7%9F/) · [TextMe for accountants](https://textme.co.il/industries/sms-%D7%9C%D7%A8%D7%95%D7%90%D7%99-%D7%97%D7%A9%D7%91%D7%95%D7%9F/)
- CPA count: [Hebrew Wikipedia – לשכת רואי חשבון](https://he.wikipedia.org/wiki/%D7%9C%D7%A9%D7%9B%D7%AA_%D7%A8%D7%95%D7%90%D7%99_%D7%97%D7%A9%D7%91%D7%95%D7%9F_%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C) · [dinvecheshbon directory](https://dinvecheshbon.co.il/)
- Reviews in IL: [Be5](https://be5.co.il/) · [Reepli WhatsApp guide/pricing](https://www.reepli.ai/he/resources/whatsapp-customer-service-guide/) · [Holy Flow](https://www.holyflow.tech/) · [RepuCare](https://repucare.co.il/) · [MaxStars pricing](https://maxstars.me/he/pricing) · [eBrand on B144 ₪29 offer](https://www.ebrand.co.il/%D7%A0%D7%99%D7%94%D7%95%D7%9C-%D7%91%D7%99%D7%A7%D7%95%D7%A8%D7%95%D7%AA-%D7%93%D7%A8%D7%9A-b144-%D7%91-29-%D7%A9%D7%97-%D7%9C%D7%97%D7%95%D7%93%D7%A9-%D7%9E%D7%94-%D7%91%D7%90%D7%9E%D7%AA-%D7%9E/)
- Missed-call IL: [Sendy](https://www.sendy-auto-app.com/app/) · [Webbers guide](https://www.webbers.co.il/post/auto-message) · [Flow](https://flow-il.com/)
- Appointments IL: [Timing](https://timingapps.com/) · [Clickinder](https://www.clickynder.com/) · [Simple Tor pricing](https://simpletor.app/pricing) · [SMS4Free](https://sms4free.co.il/) · [TextMe small business](https://textme.co.il/sms-%D7%9C%D7%A2%D7%A1%D7%A7%D7%99%D7%9D-%D7%A7%D7%98%D7%A0%D7%99%D7%9D/)
- Collections IL: [Gaviti (Capterra IL)](https://www.capterra.co.il/software/169544/gaviti) · [Sogomatic WhatsApp collection bot](https://sogomatic.com/solutions/whatsapp-payment-bot/) · [DigiShops](https://digishops.co.il/) · [Build App ועד בית](https://www.build-app.co.il/%D7%AA%D7%96%D7%9B%D7%95%D7%A8%D7%95%D7%AA-%D7%90%D7%95%D7%98%D7%95%D7%9E%D7%98%D7%99%D7%95%D7%AA-%D7%9C%D7%AA%D7%A9%D7%9C%D7%95%D7%9D-%D7%95%D7%A2%D7%93-%D7%91%D7%99%D7%AA-%D7%90%D7%99%D7%9A-%D7%9C/)
- Quotes IL: [Kala CRM](https://www.kala-crm.co.il/%D7%9E%D7%A2%D7%A8%D7%9B%D7%AA-%D7%94%D7%A6%D7%A2%D7%95%D7%AA-%D7%9E%D7%97%D7%99%D7%A8) · [tik-tok.co.il](https://tik-tok.co.il/) · [Gold Systems](https://gold-sys.co.il/%D7%AA%D7%95%D7%9B%D7%A0%D7%95%D7%AA-%D7%A2%D7%A1%D7%A7%D7%99%D7%95%D7%AA/%D7%AA%D7%95%D7%9B%D7%A0%D7%94-%D7%9C%D7%91%D7%A0%D7%99%D7%94-%D7%95%D7%A0%D7%99%D7%94%D7%95%D7%9C-%D7%94%D7%A6%D7%A2%D7%95%D7%AA-%D7%9E%D7%97%D7%99%D7%A8-%D7%9C%D7%A7%D7%91%D7%9C%D7%A0%D7%99-%D7%A9/)
- Field service IL: [Tachzukanit / Ramdor](https://www.ramdor.co.il/price-table/) · [CONBOX](https://conbox.co.il/) · [2Link](https://www.2link.co.il/%D7%AA%D7%95%D7%9B%D7%A0%D7%94-%D7%9C%D7%A0%D7%99%D7%94%D7%95%D7%9C-%D7%A7%D7%A8%D7%99%D7%90%D7%95%D7%AA-%D7%A9%D7%A8%D7%95%D7%AA) · [d.co.il AC technicians listing](https://www.d.co.il/h-c26250-e0-p0-l0/)
- Garages IL: [Eyal Software](https://www.eyalcomp.co.il/) · [BotMotors](https://botmotors-ai.com/)
- Driving instructors IL: [Sivan](https://www.cma-sivan.co.il/) · [DriveLog](https://ai-lab.co.il/drivelog/index.html) · [Dio](https://diodrive.co.il/) · [Wheel It](https://wheelit.co.il/)
- Studios IL: [Arbox](https://www.arbox.co.il/) · [2sign health declaration](https://www.2sign.co.il/%D7%94%D7%A6%D7%94%D7%A8%D7%AA-%D7%91%D7%A8%D7%99%D7%90%D7%95%D7%AA-%D7%97%D7%93%D7%A8-%D7%9B%D7%95%D7%A9%D7%A8/)
- Certificates IL: [Visitt insurance certificates help](http://help.visitt.io/he/articles/11813819-%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D-%D7%91%D7%99%D7%98%D7%95%D7%97%D7%99%D7%99%D7%9D-%D7%9C%D7%93%D7%99%D7%99%D7%A8%D7%99%D7%9D-%D7%95%D7%9C%D7%A7%D7%91%D7%9C%D7%A0%D7%99-%D7%9E%D7%A9%D7%A0%D7%94) · [Hyp on withholding certificates](https://hyp.co.il/blog/withholding-tax/) · [iCount on bookkeeping certificate](https://www.icount.co.il/blog/bookkeeping-authorization/)
- Food safety IL: [MoH food-business sanitation guide (Modiin)](https://www.modiin.muni.il/ModiinMobile/ArticlePage?PageID=1554_11145) · [idan-solutions MoH overview](https://idan-solutions.co.il/ministry-of-health-restaurants/)
- WhatsApp pricing: [Spike – Israel WhatsApp pricing](https://www.spike.co.il/blog/whatsapp-business-pricing) · [EngageLab Oct-2026 changes](https://www.engagelab.com/blog/whatsapp-business-api-pricing) · [FlowCall rates by country](https://www.flowcall.co/blog/whatsapp-business-api-pricing)

---

*All revenue figures are labeled by source type. No revenue or customer counts were invented. Review counts are not paying customers. Where an Israeli claim could not be verified, it is marked as an assumption or as "not verified".*
