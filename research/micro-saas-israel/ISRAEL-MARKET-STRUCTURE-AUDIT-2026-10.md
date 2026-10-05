# Israel Market Structure Audit for Proven Micro-SaaS Patterns

**Date:** 2026-10-05 · **Mode:** research only. Nothing was built, no accounts were created, no businesses were contacted, nothing was spent.
**Earlier work in this folder:** `BORING-MICRO-SAAS-IMPORT-US-EU-TO-ISRAEL-2026-10.md`, `VALIDATION-DOC-CHASER-VS-SERVICE-RECALL-2026-10.md`

**Labels used:**
- **VERIFIED**: an official, first-party or directory source, as extracted by search.
- **FOUNDER-REPORTED**: a claim made by a founder.
- **3RD-PARTY EST.**: a third party's estimate.
- **INFERENCE**: my reasoning from verified facts.
- **UNKNOWN**: not established.

**Method limits:**
1. This environment blocks direct page fetches from Capterra, G2, Trustpilot and many Israeli vendor sites. All facts come from **search-engine extractions**.
2. Directory counts from **Dapei Zahav (d.co.il)** are *listings*, not audited firm counts. Some businesses appear in several categories, and some are inactive. I treat a listing count as an **upper-bound proxy for sellable businesses** and apply a 0.6–0.8 haircut where noted.
3. Facebook groups are not searchable from here. **Local pain evidence is therefore mostly indirect:** job postings, consultant pages, incumbent features, legal-liability articles. This is the weakest part of the evidence. §6 marks it.

---

## A. EXECUTIVE VERDICT

**No strong candidate. One qualified, moderate candidate; one legally constrained candidate.**

**The central structural finding:**
- **In Israel, almost every regulated or professional vertical already has Hebrew vertical software with the foreign pattern built in.**

  | Vertical | Hebrew software that already does the workflow |
  |---|---|
  | Dental recall | Rapid One, SmileCloud, BINA 2000, Medform |
  | Vet vaccine reminders | SmileCloud, ClinicaOnline, Rapid Vet, VetProClinic |
  | Insurance renewals | Surense ("thousands of agencies"), Vibit; insurers' own digital renewal interfaces |
  | Mortgage-file document collection | banta, Wise (₪119/mo), Eitan, EZplan |
  | Building committees | Build App (130+ companies, 7,000+ buildings), VaadPlus, Ding, Bllink, Dayarim, Binah |
  | Garages | Eyal Software, Mosikit, BotMotors |
  | Accountants | SUMIT, Finbot, Rivhit DOCS |
  | Pest control | PestBoss, Modular365 |
  | Driving instructors | DriveLog, Sivan, Dio |
  | Studios / clinics | Arbox, Easybizy, Timing, Clickinder |

- **The gaps that remain sit in fragmented, owner-operated trades** that run on WhatsApp plus a cheap invoicing app. In those trades, **willingness to pay is anchored very low**: Tik-Tok quotes ₪34/mo, Bizli from ₪29, Fiix ₪69, Morning ₪29–₪74 (all VERIFIED). Many of them sell to **consumers**, so recall or reactivation messaging runs into the **anti-spam law** (an offer to book a new service to someone who didn't ask = advertising; up to ₪1,000 per message).

**The one pair that passes every gate (score 63/100):**

> **Pattern 8 + 10 (Compliance / Inspection Reminder + Recurring Maintenance Scheduler) for small B2B "compliance-service" contractors**, i.e. firms that service *businesses* on a legally or contractually mandated cycle:
> - Fire-extinguisher and fire-safety service (annual, Israeli Standard 129)
> - Commercial kitchen hood / duct cleaning ("Form 16" fire-authority certificate; up to monthly for charcoal grills under IS 1001)
> - Pest control for food businesses
> - Commercial AC maintenance contracts
>
> Why it passes:
> - B2B, so spam exposure is lower (contractual notices; lawyer to confirm).
> - The due date is externally enforced, so pain is real and the ROI is measurable.
> - The current stack is ERP, generic CRM or Excel. Only pest control has a vertical tool.
> - Foreign proof: Uptick ($180/user/mo), Fire Inspected ($49–$99), Inspect Point, ServiceTrade, GorillaDesk (277 reviews · 4.8).
>
> **Weakness:** combined market size is **MEDIUM (~800–2,000 firms, INFERENCE)**, and fire-safety / hood-cleaning firm counts are **UNKNOWN**.

**Second pair: residential AC/HVAC recall** (2,166 AC-technician listings; real gap). Its legal risk is **HIGH** for the consumer recall it depends on. It is viable only with a consent-capture design. Treat it as a service test, not a SaaS bet.

**Everything else failed the gap gate.** See §B and §E.

**Recommendation:**
- Run **one 14-day service-first test** on the B2B compliance-service pair (§F–§K).
- **Build nothing** unless it passes.
- If it fails, the honest answer is **NO GOOD CANDIDATE** in this pattern set for Israel at this time.

---

## B. TOP 10 INDUSTRY/PATTERN MATRIX

"Gate" = Task 4 gap classification. Only REAL or STRONG gaps qualify. Rows that failed the gate are kept to show why.

| Rank | Pattern | Israeli industry | Est. sellable businesses | Current software | Missing workflow | Foreign reference | Suggested price | Customers for ₪30k MRR | Acquisition method | Legal risk | MVP difficulty | Time to first money (0–10) | Gap gate | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Compliance reminder + maintenance scheduler (+ digital certificate) | **B2B compliance-service contractors** (fire safety, hood cleaning, pest-for-food, commercial AC) | **~800–2,000** (INFERENCE; see §2) | Excel, ERP field-service modules (Priority add-ons), generic CRMs; PestBoss/Modular365 for pest only | Site-level due list → automatic B2B reminders (60/30/14 days) → booking → digital inspection certificate → next due date | Uptick, Fire Inspected, Inspect Point, ServiceTrade, GorillaDesk | ₪299–₪449 | ~86 at ₪349 | Directory-built owner lists + safety consultants + equipment suppliers | **MEDIUM** | MEDIUM | 6 | **REAL** | **63** |
| 2 | Quote follow-up | Renovation contractors | 8,682 listings → ~5,000–6,500 | Tik-Tok (₪34, status dashboard), Bizli (open tracking), Kala CRM (automatic follow-up), Morning "Quote Plus", Fiix (₪69) | Automatic multi-touch WhatsApp follow-up on unsigned quotes | Jobber (automatic quote follow-ups; 200k+ users), Hatch | ₪69–₪149 | 201–435 | Facebook groups, suppliers | LOW–MEDIUM | EASY | 6 | **SMALL** ✖ | 59 |
| 3 | Service recall | **Residential AC/HVAC technicians** | 2,166 listings → ~1,300–1,700 | Generic CRMs (BaseCRM, Senzey, Lista), WhatsApp, notebooks | Due-customer list + consented reminders + reply routing | GorillaDesk, Kukui, Skimmer | ₪149–₪249 | ~151 at ₪199 | Directory + supplier distributors | **HIGH** (consumer spam) | EASY | 7 | **REAL** | **58** |
| 4 | Document chasing | Accounting offices | ~6,000–10,000 practices (INFERENCE) | SUMIT (automatic reminders), Finbot, Rivhit DOCS, Paperless, iCount, Morning | Non-expense annual-report documents for non-portal offices | Content Snare, TaxDome, Financial Cents | ₪99–₪149 | 201–303 | Resellers / groups | HIGH (privacy) | MEDIUM | 4 | **SMALL** ✖ | 58 |
| 5 | Renewal reminder | Insurance agencies | ~1,400 agency corporations; ~12,000 licensed agents (VERIFIED) | Surense, Vibit, insurer portals, TextMe SMS | — | Agency CRMs | — | — | — | MEDIUM | — | — | **NO GAP** ✖ | 54 |
| 6 | Recurring visits + billing reminders | Gardeners / landscapers | 2,755 listings → ~1,600–2,200 | Morning/iCount (recurring documents and payment reminders), generic CRMs | Visit log tied to monthly billing | Jobber, Yardbook | ₪49–₪99 | 300–600 | Directory | LOW | EASY | 5 | **SMALL** ✖ | 52 |
| 7 | Service recall | Pest control (residential) | 1,305 listings; 2,133 licensed exterminators (individuals) | PestBoss, Modular365 | Consumer recall (spam-constrained) | GorillaDesk, PestPac | ₪149–₪249 | 120–200 | Licensee registry | HIGH | EASY | 5 | **SMALL** ✖ | 51 |
| 8 | Document chasing | Mortgage advisors | ~2,500 advisors (3RD-PARTY EST.) → ~1,500–2,000 offices | banta (AI document extraction), Wise (₪119), Eitan, EZplan, Smartnpv | Little | FileInvite | — | — | — | HIGH (financial) | — | — | **SMALL** ✖ | 50 |
| 9 | Test/service recall | Garages | ~5,000 (Ministry of Transport, 2010; stale) | Eyal Software, Mosikit, BotMotors, SMS vendors | Little | Kukui, Demandforce | — | — | — | MEDIUM | — | — | **SMALL** ✖ | 50 |
| 10 | Recall | Dental clinics | 9,100 dentists (VERIFIED); clinics UNKNOWN (~3,000–5,000, INFERENCE) | Rapid One, SmileCloud, BINA 2000, Medform, CRMOnline | None | Weave, RevenueWell | — | — | — | HIGH (health) | — | — | **NO GAP** ✖ | 50 |

---

## C. TOP 3 REAL CANDIDATES

Only two pairs cleared the gap gate. **There is no honest third.**

1. **B2B compliance-service reminder + maintenance scheduler + digital certificate** (score 63). The best overall: B2B, externally enforced due dates, measurable ROI, MEDIUM legal risk.
2. **Residential AC/HVAC service recall** (score 58). The gap is real and the market is LARGE. However, **consumer anti-spam exposure is HIGH**, so it is only viable with consent capture going forward plus documented existing-customer status. Treat it as a **service-first** offer, not a SaaS bet.
3. **Empty slot.** The nearest miss is **quote follow-up for renovation contractors** (59). The market is huge, but the gap is **SMALL**: Kala CRM already automates follow-up, and Tik-Tok, Bizli and Morning already track quote status. Price anchors are ₪29–₪69/mo, so pricing power is close to zero. It could only work as a feature inside candidate 1 or 2.

## D. TOP 3 RESEARCH-ONLY CANDIDATES

1. **Fire-safety firms as a standalone niche.** It is the strongest *sub-niche* of candidate 1, but the **firm count is UNKNOWN**. The Israel Standards Institution's list of approved inspection companies was not retrievable. If fewer than ~300 firms exist, it only works at ₪500+/mo.
2. **Solar PV operations-and-maintenance recall** (panel cleaning, inverter checks for home and commercial systems). Installer count and existing monitoring tools are UNKNOWN; worth one research pass.
3. **Commercial AC / refrigeration service contracts** (B2B preventive maintenance). Size is UNKNOWN (a subset of the 2,166 AC listings plus refrigeration firms), and ERP field-service modules may already cover larger firms.

## E. REJECTED INDUSTRIES

| Industry / pattern | Reason |
|---|---|
| Dental, veterinary, physiotherapy, beauty, studios, optometry (recall/reminders) | **NO GAP**: Hebrew clinic software already does recall plus WhatsApp/SMS. Health data also makes privacy risk HIGH |
| Insurance agencies (renewals, documents) | **NO GAP**: Surense, Vibit, insurer portals; renewal handling is a core CRM feature |
| Mortgage advisors (document chasing) | **SMALL gap**: banta, Wise, Eitan, EZplan. Financial data makes privacy risk HIGH |
| Accountants (document chasing) | **SMALL gap** (see the previous report): SUMIT/Finbot/Rivhit/Morning; the state is pre-filling documents |
| Building management / committees | **NO GAP**: crowded (Build App, VaadPlus, Ding, Bllink, Dayarim, Binah, Darimpo, Hombi) |
| Garages (MOT/service recall) | **SMALL gap**: Eyal, Mosikit, BotMotors |
| Driving instructors | **NO GAP**: DriveLog, Sivan, Dio, Wheel It, Adi Mobile |
| Elevator maintenance | **TINY** (~91 maintenance companies, VERIFIED), dominated by 6 large firms |
| Swimming-pool service | **TINY** (~30 d.co.il listings) |
| Water-filter dealers | **SMALL** (119 listings). Brands (e.g., Tami4) run their own service; consumer spam risk |
| Leak detection | **SMALL** (~175 listings); one-off jobs, not recurring |
| Plumbers / electricians / locksmiths (missed-call recovery) | **NO GAP**: free Israeli missed-call apps (Sendy, Responder, Dial My App); low willingness to pay |
| Any vertical (review requests) | **SMALL gap / crowded**: Be5, Reepli, Holy Flow, MaxStars, B144 at ₪29 |
| Gardeners, cleaning companies (recurring billing / payment reminders) | **SMALL gap**: Morning/iCount handle recurring documents and reminders; staff scheduling is solved (EasyWeek, Mishmarot, EZshift); price anchors under ₪100 |
| Renovation contractors (quote follow-up) | **SMALL gap** + low pricing power (see §C.3) |
| Pest control (residential recall) | **SMALL gap** (PestBoss, Modular365) + consumer spam risk. The B2B part folds into candidate 1 |

## F. ONE BEST SERVICE-FIRST TEST

**"Compliance Due-Date Desk" for B2B compliance-service contractors.** Start with fire-extinguisher / fire-safety service firms and kitchen hood-cleaning firms (both issue certificates that their business customers need for fire approval and business licensing). Add pest-control firms serving food businesses third.

We take the firm's list of client sites and last service dates. We build the due list, send B2B reminders in the firm's name 60, 30 and 14 days before expiry, route replies to the firm, and deliver a monthly "due / booked / overdue" report.

## G. ONE BEST SAAS CANDIDATE (only if F validates)

**A site-level compliance scheduler for small B2B service contractors.** Core loop:
1. Client sites, each with service types and next-due dates.
2. Automatic B2B reminder sequence.
3. One-click booking reply.
4. Technician completes a short mobile form.
5. Branded PDF certificate/report sent to the client.
6. The next due date is set automatically.

The **certificate step** is what makes it stickier than a reminder tool: the client's compliance record lives in it. Foreign pattern: Fire Inspected / Uptick / Inspect Point, simplified for 1–10-technician Israeli firms.

## H. EXACT FIRST OFFER

> **"לא מפספסים אף בדיקה שנתית"** ("Never miss an annual inspection")
> - We take your client list (Excel, invoicing-system export, or even photos of a notebook) and build a due list per site.
> - Your business clients get a reminder in your company's name before their inspection, certificate or cleaning expires. Replies come straight to you.
> - Every month you get a report: who is due, who booked, who is overdue.
> - **Price for the first 5 firms:** ₪0 setup, **₪390/month** for up to 300 client sites. **First month free.** Cancel anytime.
> - **Alternative (performance):** ₪290 setup + **₪40 per booked visit**, with setup refunded below 5 bookings in the first 30 days.
> - **Compliance:** we only contact business clients you hold an existing service relationship with, every message identifies your company and includes an opt-out, and wording is reviewed by a lawyer before sending.

## I. EXACT FIRST 20-CUSTOMER CHANNEL

**Primary: owner-direct outreach built from public directories**, using 1:1 phone first, then WhatsApp/LinkedIn identified with an opt-out.
- **Fire safety:** d.co.il categories for fire-extinguisher service and fire-safety systems; Google Maps "בדיקת מטפים" (extinguisher inspection) by city.
- **Hood cleaning:** d.co.il / Google Maps "ניקוי מנדפים" / "ניקוי ארובות" (hood / duct cleaning).
- **Pest control for businesses:** the **Ministry of Environmental Protection public registry of licensed exterminators** (2,133 licenses; [govil dataset](https://govil.ai/datasets/%D7%9E%D7%93%D7%91%D7%99%D7%A8%D7%99%D7%9D-%D7%9E%D7%95%D7%A8%D7%A9%D7%99%D7%9D-fecc5a5f/)), cross-referenced with firms that advertise "הדברה לעסקים" (pest control for businesses).

**Secondary (partner/referral, toward lower lead dependence):**
- **Safety consultants** (d.co.il "safety consultant" category; they tell businesses which inspections they need).
- **Equipment distributors** that supply extinguisher and hood-cleaning service firms.
- **Business-licensing consultants** (רישוי עסקים) who chase these certificates for restaurants.

## J. EXACT 14-DAY VALIDATION PLAN

| Day | Action | Target numbers | Output |
|---|---|---|---|
| 1 | Build the prospect sheet: fire-safety service, hood-cleaning, pest-control-for-business firms (directories + licensee registry). Draft the scripts. List lawyer questions (message classification for B2B contractual notices) | **120 prospects** (50 fire safety, 30 hood cleaning, 40 pest-for-business) | Sheet + scripts |
| 2–4 | Owner-direct calls (12-minute discovery, no pitch until the end) | **Reach 60 → 15 conversations** | Pain, list quality, current tool, consent/contract status |
| 3–5 | Recruit 3 partner-channel contacts (safety consultants / licensing consultants / distributor) | **3 partner conversations** | Referral willingness |
| 5–7 | Onboard pilots: clean lists, compute due dates, send the first reminders (business clients only), route replies | **3 pilots** (≥1 fire safety, ≥1 hood cleaning) | Pilots live |
| 8–12 | Follow-ups, booking tally, mid-pilot report | — | Bookings per 100 due sites |
| 13–14 | Present results; ask for ₪390/mo or invoice the performance option; go/kill | — | Paid / not paid |

**Discovery questions:**
- How many active business clients/sites do you have?
- How do you know who is due?
- Who reminds them, and how?
- How many expire unnoticed per year?
- What does a missed renewal cost you?
- What software do you use?
- Do you issue the certificate on paper or as a PDF?
- Would a monthly due report plus automatic reminders be worth ₪390?

## K. STRICT KILL CRITERIA

| If, by day 14… | Then |
|---|---|
| Fewer than **8 of 15** owners say due-date tracking is manual (Excel/memory/paper) **and** that clients lapse or are late at least sometimes | **KILL** |
| More than **half** already use software that sends automatic due reminders (field-service ERP, PestBoss/Modular365, or similar) | **KILL** that sub-niche |
| Fewer than **3** agree to a pilot | **KILL** |
| Pilots book fewer than **5 visits per 100 due sites** (or no improvement over the owner's own baseline) | **KILL** |
| Fewer than **2** firms pay (₪390/mo or a performance invoice) | **KILL** |
| A lawyer classifies B2B renewal notices as advertising requiring consent **and** firms can't document an existing-customer basis | **KILL** the messaging format |
| Desk research finds **fewer than 300** fire-safety + hood-cleaning + pest-for-business firms combined | **KILL** the SaaS (keep it only as a service if profitable per hour) |
| Day 30: fewer than **3 paying** firms, or fewer than **1 partner** referral | No SaaS build |

## L. MVP ONLY IF VALIDATED

| Component | Spec | Classification |
|---|---|---|
| Login | Firm owner + technicians (magic link) | DAY-1 |
| Client sites | Client → sites → service types (extinguisher / hood / pest / AC) → last date → interval → next due | DAY-1 |
| Workflow rules | Reminders at 60/30/14 days and on the due date; stop on booking/reply; overdue escalation to the owner | DAY-1 |
| Notifications | WhatsApp Cloud API (B2B templates), SMS fallback, email; sender = firm name; opt-out handling | DAY-1 |
| Booking | Reply-to-book (a human confirms) | DAY-1; calendar sync POST |
| Technician form | Mobile checklist per service type (photos, items checked, signature) | DAY-1 for 1 service type; others POST |
| Certificate | Branded PDF report sent to the client and stored; next due date set automatically | DAY-1 |
| Dashboard | Due this month / booked / overdue / lost; revenue at risk | DAY-1 |
| Import | Excel import with date normalization | DAY-1 |
| Billing | Israeli recurring billing (Grow/Cardcom/PayPlus/Tranzila) + Morning invoices; Stripe is unavailable to Israeli merchants (VERIFIED) | DAY-1 (manual at first) |
| Audit log | Who changed dates, who sent what | DAY-1 |
| Integrations | Morning/iCount (pull last invoices as service dates) | POST |
| Route planning, quoting, inventory, AI | — | DO NOT BUILD |

- **Stack:** Next.js + Supabase (EU) + n8n + WhatsApp Cloud API + Resend + PDF generation (server-side).
- **Build time:** about **2–3 weeks** with AI-assisted coding (INFERENCE).
- **Infrastructure for the first 100 firms:** about **$150–$300/mo** plus pass-through message costs (B2B utility-classified messages ~$0.005 each; marketing ~$0.035–$0.041 in Israel).
- **Complexity:** **MEDIUM**, because of the certificate forms per service type.
- **Support burden:** medium (imports, form tweaks).
- **Maintenance burden:** medium (WhatsApp template policy, forms per standard).

---

# DETAILED WORK (Tasks 1–16)

## §1. Long list of Israeli industries (Task 1)

| # | Industry | Patterns that might apply | Size signal | Size class |
|---|---|---|---|---|
| 1 | Residential AC/HVAC technicians | 1, 9, 10 | 2,166 d.co.il listings (VERIFIED) | LARGE |
| 2 | Commercial AC / refrigeration service | 8, 10 | UNKNOWN (subset of #1 + refrigeration) | MEDIUM? |
| 3 | Pest control | 1, 8, 10 | ~1,305 listings; 2,133 licensed exterminators (individuals) (VERIFIED) | MEDIUM |
| 4 | Water-filter / water-bar dealers | 1, 10 | 119 listings (VERIFIED) | SMALL |
| 5 | Swimming-pool service | 10 | ~30 listings (VERIFIED) | TINY |
| 6 | Solar water-heater service | 1 | Subset of plumbers; UNKNOWN | ? |
| 7 | Fire-safety / extinguisher service | 8, 10 | UNKNOWN; INFERENCE 150–400 | SMALL |
| 8 | Kitchen hood / duct cleaning | 8, 10 | UNKNOWN; INFERENCE 50–150 | TINY–SMALL |
| 9 | Garages | 1, 4, 8 | ~5,000 (Ministry of Transport 2010; VERIFIED but stale) | LARGE |
| 10 | Tire shops | 1, 4 | UNKNOWN | ? |
| 11 | Dental clinics | 1, 4, 9 | 9,100 dentists (VERIFIED); clinics UNKNOWN | LARGE |
| 12 | Cosmetic / beauty clinics | 1, 4, 9 | Large; heavily served | LARGE |
| 13 | Physiotherapy | 1, 9 | UNKNOWN | ? |
| 14 | Optometry | 1, 8 | UNKNOWN | ? |
| 15 | Veterinary | 1, 8 | UNKNOWN; heavily served | ? |
| 16 | Cleaning companies | 6, 7 | ~1,929 listings (VERIFIED) | MEDIUM |
| 17 | Electricians | 2, 3 | ~3,500 listings (VERIFIED via d.co.il text) | LARGE |
| 18 | Plumbers | 2, 3 | ~2,500 listings (VERIFIED via d.co.il text) | LARGE |
| 19 | Locksmiths | 3 | UNKNOWN | ? |
| 20 | Solar PV installers | 1, 10 | UNKNOWN | ? |
| 21 | Alarm / security systems | 8, 10 | UNKNOWN | ? |
| 22 | Elevator maintenance | 8, 10 | ~91 companies (VERIFIED) | TINY |
| 23 | Network / IT technicians | 7, 10 | ~591 listings (VERIFIED) | MEDIUM |
| 24 | Gardeners / landscaping | 7, 10 | ~2,755 listings (VERIFIED) | LARGE |
| 25 | Renovation contractors | 2, 4 | ~8,682 listings (VERIFIED) | LARGE |
| 26 | Painters | 2 | ~1,366 listings (VERIFIED) | MEDIUM |
| 27 | Building management companies / committees | 5, 7 | Build App alone: 130+ companies, 7,000+ buildings (VERIFIED) | MEDIUM |
| 28 | Accounting offices | 5, 6, 7 | ~6,000–10,000 practices (INFERENCE) | LARGE |
| 29 | Law offices | 5, 6 | Large; UNKNOWN firm count | LARGE |
| 30 | Insurance agencies | 1, 5, 8 | ~1,400 corporate agencies; ~12,000 licensed agents (VERIFIED) | LARGE |
| 31 | Mortgage advisors | 5, 6 | ~2,500 (3RD-PARTY EST.) | MEDIUM–LARGE |
| 32 | Driving instructors | 1, 7 | Heavily served | LARGE |
| 33 | Leak detection | 2, 3 | ~175 listings (VERIFIED) | SMALL |
| 34 | Safety consultants / licensing consultants | 8 | UNKNOWN (d.co.il category exists) | ? (partner channel) |
| 35 | Payroll / HR providers | 5, 6 | UNKNOWN | ? |

## §2. Real market size: sellable businesses (Task 2), serious candidates

| Industry | Raw count | What it counts | Sellable estimate | Class |
|---|---|---|---|---|
| Residential AC technicians | 2,166 | d.co.il listings | 1,300–1,700 (0.6–0.8 haircut) | LARGE |
| Renovation contractors | 8,682 | Listings | 5,000–6,500 | LARGE |
| Gardeners | 2,755 | Listings | 1,600–2,200 | LARGE |
| Cleaning companies | 1,929 | Listings | 1,150–1,550 | MEDIUM |
| Pest control | 1,305 listings / 2,133 licenses | Listings vs. **individual** licenses (not firms) | 800–1,100 firms | MEDIUM |
| Fire safety / extinguisher | UNKNOWN | Standards Institution-approved companies (list not retrievable) | 150–400 (INFERENCE) | SMALL |
| Hood / duct cleaning | UNKNOWN | — | 50–150 (INFERENCE) | TINY–SMALL |
| **B2B compliance-service combined** | — | Fire safety + hood + pest-for-business + commercial AC subset | **~800–2,000 (INFERENCE)** | **MEDIUM** |
| Insurance agencies | ~1,400 corporate; ~12,000 individual licenses | Corporate agencies are the buyer; solo agents also buy | 3,000–6,000 buying units (INFERENCE) | LARGE |
| Mortgage advisors | ~2,500 advisors (~1,800 in the association) | People | 1,500–2,000 offices | MEDIUM |
| Dental clinics | 9,100 dentists; 694 institutional clinics run by 491 operators | People ≠ clinics | 3,000–5,000 private clinics (INFERENCE) | LARGE |
| Garages | ~5,000 (2010) | Licensed garages | 4,000–5,500 | LARGE |
| Elevators | ~91 | Maintenance companies | 91 | TINY |
| Pools | ~30 | Listings | <50 | TINY |
| Water filters | 119 | Listings | 80–100 | TINY |

## §3–§4. Current software and feature-gap matrix (Tasks 3–4)

Legend: ✔ already handled by common incumbent software · ~ partially · ✖ missing.

| Capability | AC residential | B2B compliance service | Renovation (quotes) | Pest (residential) | Gardeners / cleaning | Dental | Insurance | Mortgage | Garages | Building management |
|---|---|---|---|---|---|---|---|---|---|---|
| Customer records | ~ (generic CRM / phone) | ~ (Excel/ERP) | ✔ (Tik-Tok/Bizli CRM) | ✔ (PestBoss) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Due dates per asset/site | ✖ | ~ | n/a | ✔ | ~ | ✔ | ✔ | n/a | ✔ | ✔ |
| Automatic reminders | ✖ (unless configured in a generic CRM) | ✖/~ | ~ (Kala CRM ✔) | ~ | ✔ (Morning payment reminders) | ✔ | ✔ | ✔ | ✔ | ✔ |
| WhatsApp | manual | manual | ✔ (sharing) | ? | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Booking | ✖ | ✖ | n/a | ✔ | ~ | ✔ | n/a | ✔ | ✔ | ✔ |
| Quote tracking | ~ | ~ | ✔ | ~ | ~ | ✔ | ✔ | ✔ | ✔ | n/a |
| Document / certificate output | ✖ | ~ (paper forms / ERP) | ✔ | ✔ (Ministry-format certificates) | n/a | ✔ | ✔ | ✔ | ✔ | ✔ |
| Renewal alerts to the *end customer* | ✖ | **✖** | n/a | ~ | n/a | ✔ | ✔ | n/a | ✔ | n/a |
| Dashboards | ✖ | ✖/~ | ✔ | ✔ | ~ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Payment reminders | ✔ (Morning/iCount) | ✔ (Morning/iCount/ERP) | ✔ | ✔ | ✔ | ✔ | n/a | n/a | ✔ | ✔ |
| Customer reactivation | ✖ | ✖ | ✖ | ~ | ✖ | ✔ | ✔ | ✖ | ✔ | n/a |
| **Gap class** | **REAL** | **REAL** | **SMALL** | **SMALL** | **SMALL** | **NO GAP** | **NO GAP** | **SMALL** | **SMALL** | **NO GAP** |

Sources for incumbents are in §M.

## §5. Foreign proof for the surviving pairs (Task 5)

| Pair | Product | Country | Workflow | Pricing | Reviews / customers | Revenue | Evidence |
|---|---|---|---|---|---|---|---|
| B2B compliance | **Uptick** | Australia → US | Fire-protection scheduling, inspections, quoting, invoicing | From **$180/user/mo** | G2/Capterra **4.5** (count n/v) | U | MODERATE |
| B2B compliance | **Fire Inspected** | US (n/v) | Extinguisher inspections, barcode, NFPA forms, PDF, **30/14/7-day due reminders** | Free / $49 / $99 | New; few reviews | U | WEAK–MODERATE |
| B2B compliance | **Inspect Point** | US | Fire-protection inspection forms + reports | Up to ~$129/user (annual) | Value-for-money 3.2/5 | U | MODERATE |
| B2B compliance | **ServiceTrade** | US | Commercial HVAC/fire field service (multi-vertical) | Custom | n/v | U | MODERATE |
| B2B compliance / recall | **GorillaDesk** | US | Recurring route service (pest/lawn/pool) with reminders | $49–$149 | **277 reviews · 4.8** (Software Advice) | U | STRONG |
| AC recall | GorillaDesk, Kukui ($200–$500), Skimmer ($1–$2 per pool) | US | Recurring service + reminders / reactivation | As listed | As listed | U | MODERATE (recall is bundled in suites) |
| (Quote follow-up, failed the gate) | Jobber | Canada | Automatic quote follow-ups at 3 and 7 days | $49–$249 | 200,000+ users (3RD-PARTY) | U | STRONG, but the Israeli gap is SMALL |

## §6. Local customer pain (Task 6), with honest evidence quality

| Pair | Evidence found | Quality |
|---|---|---|
| B2B compliance | (a) **Legal duty**: annual extinguisher inspection under IS 129 by approved inspectors, a condition for fire approval ([Timrot](https://www.timrot.co.il/fire-extinguisher-inspection/), [Midrag](https://www.midrag.co.il/Content/Tip/12561)). (b) Hood cleaning under **IS 1001 part 6**, with a "**Form 16**" fire-authority approval; monthly cleaning for charcoal grills ([White Air](https://www.white-air.co.il/article104), [mindafim](https://www.mindafim.co.il/%D7%90%D7%99%D7%A9%D7%95%D7%A8-%D7%A0%D7%99%D7%A7%D7%95%D7%99-%D7%9E%D7%A0%D7%93%D7%A4%D7%99%D7%9D-%D7%94%D7%9B%D7%9C-%D7%A2%D7%9C-%D7%98%D7%95%D7%A4%D7%A1-16-%D7%9B%D7%91%D7%90%D7%95%D7%AA/)). (c) Food businesses must keep pest-control documentation for licensing ([Nevo regulations](https://www.nevo.co.il/law_html/law00/4867.htm)). (d) Vendor blogs repeatedly urge businesses to "remember the annual inspection", which implies customers forget (INFERENCE) | **Indirect but structural.** The due date is real; whether *contractors* feel the reminder pain is **unproven**. That is the first thing interviews must establish |
| AC residential | Job postings for AC-company secretaries that include **"follow-ups on quotes" and coordinating technicians** ([mizug-avir.org](https://www.mizug-avir.org/%D7%93%D7%A8%D7%95%D7%A9%D7%99%D7%9D)); annual-cleaning recommendations on consumer sites | Weak–indirect |
| Insurance (rejected) | Agent liability for missed renewals ([sarfati-law](https://sarfati-law.co.il/insurance-agent-liability), [ronkinlaw](https://www.ronkinlaw.co.il/%D7%97%D7%99%D7%93%D7%95%D7%A9-%D7%A4%D7%95%D7%9C%D7%99%D7%A1%D7%94/)), so the pain is real, but it is already served | Strong pain, no gap |
| Renovation quotes (rejected) | Only generic sales-advice content on follow-up timing | Weak |

**No raw Israeli user complaints were found for any pair.** Facebook groups are not indexable. This is the main reason the plan is interview-first.

## §7. Willingness to pay (Task 7)

**Israeli price anchors:**

| Anchor | Price | Label |
|---|---|---|
| Tik-Tok (quotes) | ₪34/mo | VERIFIED |
| Bizli | ₪29–₪219 | VERIFIED |
| Fiix | ₪69 | VERIFIED |
| Morning | ₪29–₪74 | VERIFIED |
| Wise (mortgage) | ₪119 | VERIFIED |
| Clickinder | ₪99 | VERIFIED |
| Reepli | ₪299 + agents | VERIFIED |
| SUMIT | ₪15 per file | VERIFIED |

**Value of one recovered job:**

| Job | Value | Label |
|---|---|---|
| Extinguisher inspection per building | ₪400–₪800; ₪150–₪300 for 1–2 units | VERIFIED |
| Hood cleaning | Hundreds to thousands of ₪ per visit, recurring monthly to quarterly | INFERENCE |
| Residential AC cleaning | ₪189–₪500 | VERIFIED |
| Pest treatment | ~₪250–₪350 | VERIFIED |

| Candidate | ₪99 | ₪149 | ₪199 | ₪299 | ₪399 | ₪499 | ₪799+ | Best price | ₪10k MRR | ₪30k MRR | ₪50k MRR | Feasible vs. market? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **B2B compliance** | easy | easy | easy | justified if ≥1 recovered site per month | **target** | firms with 300+ sites | rare | **₪349–₪399** | 26–29 | **76–86** | 126–144 | 4–11% of ~800–2,000. **Feasible only if the upper size estimate holds** |
| AC residential | ok | **target** | ok | hard | ✖ | ✖ | ✖ | ₪149–₪199 | 51–68 | 151–202 | 252–336 | 9–15% of ~1,300–1,700. **Demanding** |
| Renovation quotes (rejected) | **ceiling** | hard | ✖ | ✖ | ✖ | ✖ | ✖ | ₪69–₪99 | 102–145 | 304–435 | 506–725 | Unrealistic against ₪34–₪69 anchors |

## §8. Acquisition reality (Task 8)

| Candidate | Reachable businesses | Owner findable? | Phone dependence | WhatsApp | Email | Trust barrier | Demo needed? | Sales cycle |
|---|---|---|---|---|---|---|---|---|
| B2B compliance | ~800–2,000 via d.co.il, Google Maps, the licensed-exterminator registry | **Yes**: owner-operated, the number is on the listing | High at first | Usually | Sometimes | Medium (their client list is their asset) | Short screen-share | 1–3 weeks |
| AC residential | ~1,300–1,700 | Yes | High | Yes | Rarely | Medium | No | Days–2 weeks |

## §9. Low-lead-dependence test (Task 9), scored 0–5

| | A. Direct outbound dependence (5 = low) | B. Partner/reseller | C. Marketplace/directory discovery | D. Word of mouth | E. Embedded distribution | F. Self-serve purchase | Total /30 |
|---|---|---|---|---|---|---|---|
| **B2B compliance** | 2 | **4** (safety consultants, licensing consultants, equipment distributors) | 1 | 3 (small trade communities) | **3** (the certificate PDF reaches every end client, so clients see the brand) | 2 | **15** |
| AC residential | 1 | 2 (parts/AC distributors) | 1 | 2 | 1 | 2 | 9 |
| Renovation quotes (rejected) | 2 | 2 | 2 | 2 | 2 (the quote reaches end clients) | 4 | 14 |

## §10. Service-first versions (Task 10)

| Candidate | Exact offer | Price | Manual tools | Automation | Onboarding | Delivery | Validation metric |
|---|---|---|---|---|---|---|---|
| **B2B compliance** | See §H | ₪390/mo or ₪290 + ₪40 per booked visit | Google Sheets due list, a phone call to clean data | n8n schedule; WhatsApp Cloud API B2B templates / SMS fallback; reply forwarding; monthly report | 2–4 hours per firm | Continuous; first reminders by day 2 | Bookings per 100 due sites; % of due sites renewed on time vs. baseline; firm pays |
| AC residential | Consented-only recall sprint (from the previous report) | ₪290 + ₪35 per booked job | Same | Same + consent tracking | 3–5 hours | 7–10 days | Bookings per 100 *consented* contacts; opt-out rate |

## §11. Legal / privacy / spam (Task 11). Not legal advice; items for a lawyer

| Item | B2B compliance | AC residential |
|---|---|---|
| Anti-spam law §30A | **MEDIUM**: recipients are businesses with an existing service relationship. Notices about an expiring contractual or statutory service may still be "advertising" if they offer a new paid booking. **Lawyer to classify.** | **HIGH**: an offer to book a new service to a consumer who didn't ask = advertising; needs consent or the full existing-customer exception ([consumers.org.il](https://www.consumers.org.il/category/email-spam-law), [Bizportal](https://www.bizportal.co.il/financialconsumerism/news/article/20043454)) |
| WhatsApp policy | Utility vs. marketing template classification; opt-out | Marketing templates need opt-in under Meta policy |
| Privacy (Amendment 13, in force 14.8.2025) | **LOW–MEDIUM**: business contacts, site addresses, service records; a processor agreement with each firm | **LOW–MEDIUM**: consumer names, phones, addresses |
| Sensitive data | None (no health or financial documents) | None |
| Retention | Define retention + deletion on request | Same |
| Security expectations | Standard (encryption, access control, audit log) | Standard |

**For the lawyer:**
1. Template classification (B2B renewal notice vs. advertising).
2. Mechanics of the existing-customer exception.
3. Processor agreement under Data Security Regulation 15.
4. Whether certificates we generate carry any regulatory form requirements (IS 129 forms, Form 16).

## §12. Technical MVP complexity (Task 12)

| Candidate | Smallest SaaS | Build time (AI-assisted) | Infrastructure (first 100 customers) | Third-party API cost | Support | Maintenance | Class |
|---|---|---|---|---|---|---|---|
| B2B compliance | §L | 2–3 weeks | ~$150–$300/mo | WhatsApp ~$0.005 (utility) to ~$0.04 (marketing) per message; SMS ~₪0.08 | Medium | Medium (forms per standard) | **MEDIUM** |
| AC residential | Due list + consent + campaigns + replies | 1–2 weeks | ~$70–$150/mo + pass-through messages | Mostly marketing-rate messages | Medium (messy lists) | Low | **EASY** |

## §13. Scores (Task 13)

Weights: Market 15 · Proof 10 · Local pain 15 · Gap 20 · Recurring 10 · Acquisition 10 · Low lead dependence 5 · MVP 5 · Low legal 5 · Pricing 5.

| Pair | Mkt | Proof | Pain | Gap | Recur | Acq | LeadDep | MVP | Legal | Price | **Total** | Time to money /10 | SaaS /10 | Service-first /10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **B2B compliance service** | 8 | 7 | 8 | 13 | 8 | 6 | 3 | 3 | 4 | 3 | **63** | 6 | **6** | **7** |
| Renovation quote follow-up ✖gate | 14 | 8 | 6 | 6 | 6 | 6 | 3 | 5 | 4 | 1 | 59 | 6 | 3 | 4 |
| **AC residential recall** | 12 | 6 | 7 | 12 | 6 | 6 | 2 | 4 | 1 | 2 | **58** | **7** | 4 | 6 |
| Accounting doc chasing ✖gate | 12 | 9 | 7 | 5 | 9 | 5 | 3 | 4 | 1 | 3 | 58 | 4 | 4 | 4 |
| Insurance renewals ✖gate | 12 | 7 | 7 | 2 | 9 | 5 | 3 | 3 | 2 | 4 | 54 | 3 | 2 | 2 |
| Gardeners billing/visits ✖gate | 12 | 6 | 5 | 5 | 8 | 5 | 2 | 4 | 4 | 1 | 52 | 5 | 2 | 3 |
| Pest residential recall ✖gate | 9 | 6 | 6 | 6 | 7 | 6 | 3 | 4 | 2 | 2 | 51 | 5 | 3 | 4 |
| Mortgage doc chasing ✖gate | 8 | 8 | 6 | 5 | 5 | 6 | 3 | 4 | 2 | 3 | 50 | 4 | 3 | 3 |
| Garage recall ✖gate | 12 | 6 | 5 | 4 | 8 | 5 | 2 | 4 | 2 | 2 | 50 | 4 | 2 | 3 |
| Dental recall ✖gate | 12 | 8 | 6 | 1 | 9 | 4 | 2 | 3 | 1 | 4 | 50 | 2 | 1 | 1 |

**Judgment overrides:**
- **Renovation quote follow-up scores 59 on raw points** (huge market, strong foreign proof) **but fails the gap gate.** Local tools already track quote status, and Kala CRM automates follow-up. Price anchors of ₪29–₪69 make it unsellable as a standalone product. **Not a candidate.**
- **AC residential (58) beats it on gap, but its legal score is 1 of 5.** It is only defensible as a consent-based service, which caps the SaaS upside.
- **B2B compliance (63) wins** because it is the only pair with a REAL gap *and* acceptable legal risk *and* partner channels (consultants, distributors) *and* embedded distribution (the client-facing certificate). **Its weakness is size uncertainty.** That is why the first kill criterion is a firm count.

## §14. Top 10 matrix (Task 14)

See §B.

## §15. Deep dive (Task 15)

The task asked for a top 5; only 2 pairs passed the gate. The other 3 slots are covered by the rejection reasons in §E and the research-only notes in §D.

### 15.1 B2B compliance-service contractors

- **Exact ICP:** an owner-operated firm with 1–10 technicians that services **business** clients on a mandated or contractual cycle:
  - fire extinguishers / fire-safety systems (IS 129);
  - restaurant hood/duct cleaning (IS 1001-6; Form 16);
  - pest control for food businesses;
  - commercial AC maintenance contracts.

  It has 100–1,500 client sites and tracks due dates in Excel, an old ERP or paper.
- **Market size:** ~800–2,000 firms combined (INFERENCE). Fire-safety and hood-cleaning counts are UNKNOWN. **Verifying them is the first task.**
- **Current workflow (INFERENCE):** after service, the technician fills a paper or ERP form and sticks a label on the extinguisher. The owner or secretary later scans an Excel sheet, or relies on clients calling. Clients often forget until a fire inspector or business-licensing visit forces them.
- **Incumbent software:**
  - ERP field-service modules (Priority add-ons, Mobile4ERP).
  - Generic CRMs (BaseCRM, Senzey, Lista).
  - Tachzukanit / CONBOX / 2Link for service calls.
  - PestBoss / Modular365 (pest only).
  - The Israeli Safety Center's software targets *the business's internal* safety management, not the contractor.
- **Exact gap:** a site-level due list → automatic client-facing reminders → reply-to-book → digital certificate → auto-reset of the next due date, priced for 1–10-person firms.
- **Why the customer would pay:**
  - Each lapsed site is lost recurring revenue: extinguisher inspections ₪150–₪800, hood cleaning recurring monthly to quarterly.
  - Professional digital certificates differentiate them from competitors.
  - Fewer client complaints when inspectors arrive.
- **Foreign proof:** Uptick ($180/user), Fire Inspected ($49–$99), Inspect Point, ServiceTrade, GorillaDesk (277 · 4.8).
- **Realistic monthly price:** ₪349–₪399 (₪249 for very small firms).
- **First 20 route:** §I. Owner-direct from directories and the licensee registry, plus 3 partner channels (safety consultants, licensing consultants, distributors).
- **Service-first offer:** §H.
- **Exact MVP:** §L.
- **Technical stack:** Next.js, Supabase (EU), n8n, WhatsApp Cloud API, Resend, PDF rendering, Israeli recurring billing.
- **Legal issues:** MEDIUM (§11).
- **Biggest reason it could fail:**
  - The combined niche is smaller than ~500 firms, or
  - Firms already get adequate reminders from their ERP or field-service tool, or
  - Owners see their client list as too sensitive to share.
- **Evidence still missing:**
  - Firm counts.
  - Raw owner pain (interviews).
  - Current tools in use.
  - The baseline lapse rate (how many sites renew late or churn).
  - Lawyer classification of the notices.

### 15.2 Residential AC/HVAC recall

- **ICP:** an AC service business with 1–5 technicians and 500+ past residential customers recorded in a phone or invoicing app.
- **Market:** ~1,300–1,700 businesses.
- **Workflow today:** reactive. Customers call in heat waves; some businesses send ad-hoc WhatsApp broadcasts (legally risky).
- **Incumbents:** generic CRMs; invoicing apps (Morning/iCount).
- **Gap:** a due list plus a *consented* recall programme.
- **Why pay:** pre-season bookings smooth demand (₪189–₪500 per cleaning).
- **Foreign proof:** GorillaDesk, Kukui (recall as a paid feature).
- **Price:** ₪149–₪199, or per booked job.
- **First 20:** directory + AC-parts distributors.
- **Service-first:** a consent-only sprint (previous report).
- **MVP:** due list, consent flag, campaign, reply inbox.
- **Legal:** **HIGH**.
- **Biggest failure reason:** too few consented contacts to matter; seasonality (peak March–May, so October is off-season).
- **Missing evidence:** share of customers with documented consent or existing-customer notice; booking rate.

## §16. Falsification (Task 16)

| Candidate | Evidence that would kill it immediately |
|---|---|
| B2B compliance | (1) Fewer than **300** relevant firms combined. (2) More than half of interviewed firms already get automatic client-facing due reminders from their current software. (3) Owners won't share client lists, or lists lack last-service dates. (4) A lawyer says B2B renewal notices need prior consent that firms can't show. (5) Pilots book fewer than 5 visits per 100 due sites. (6) No firm pays ₪299+. (7) Each firm wants custom certificate forms, so support burden explodes |
| AC residential | (1) Fewer than 20% of a typical customer list has documented consent / existing-customer notice. (2) Opt-out rate above 10%. (3) Bookings below 5 per 100 consented contacts. (4) Owners say "summer is full anyway". (5) Any spam claim |
| (For completeness) Renovation quote follow-up | Already falsified: Kala CRM automates follow-up; Tik-Tok, Bizli and Morning track status; price anchors are ₪29–₪69 |
| (For completeness) Dental / insurance / building management / mortgage / accountants | Already falsified: incumbent Hebrew vertical software includes the workflow |

---

## M. SOURCES / EVIDENCE APPENDIX

### Market size
- d.co.il listing counts:
  - [AC technicians 2,166](https://www.d.co.il/h-c26250-e0-p0-l0/)
  - [pest control ~1,305](https://www.d.co.il/h-c13110-e0-p0-l0/)
  - [renovation ~8,682](https://www.d.co.il/h-c48570-e0-p0-l0/)
  - [gardeners ~2,755](https://www.d.co.il/h-c11000-e0-p0-l0/recommended/)
  - [cleaning ~1,929](https://www.d.co.il/h-c2295-e0-p0-l0/recommended/)
  - [painters ~1,366](https://www.d.co.il/h-c41160-e0-p0-l0/)
  - [network technicians ~591](https://www.d.co.il/h-c25825-e0-p0-l0/)
  - [leak detection ~175](https://www.d.co.il/h-c2815-e0-p0-l0/)
  - [water systems (119)](https://www.d.co.il/h-c26540-e0-p0-l0/)
  - [pools](https://www.d.co.il/h-c7260-e0-p0-l0/)
  - [plumbers page (incl. ~3,500 electricians / ~2,500 plumbers text)](https://www.d.co.il/h-c2550-e0-p0-l0/)
  - [safety consultants](https://www.d.co.il/h-c5520-e0-p0-l0/)
- Licensed exterminators 2,133 (Ministry of Environmental Protection dataset): [govil.ai](https://govil.ai/datasets/%D7%9E%D7%93%D7%91%D7%99%D7%A8%D7%99%D7%9D-%D7%9E%D7%95%D7%A8%D7%A9%D7%99%D7%9D-fecc5a5f/)
- Insurance agents (~12,000–12,500) / ~1,400 agency corporations: [polisa.news](https://polisa.news/%D7%94%D7%93%D7%95%D7%97-%D7%94%D7%A9%D7%A0%D7%AA%D7%99-%D7%A9%D7%9C-%D7%94%D7%A8%D7%A9%D7%95%D7%AA-%D7%9C-2025-%D7%A2%D7%9C%D7%99%D7%99%D7%94-%D7%91%D7%A9%D7%99%D7%A2%D7%95%D7%A8-%D7%94%D7%A2%D7%9E/) · [Art Invest](https://www.artinvest.co.il/2025/03/08/ilinsurancebrokers/)
- Mortgage advisors (~2,500; ~1,800 in the association): [Calcalist](https://www.calcalist.co.il/real-estate/article/bjy11rmqfqjgl) · [Wikipedia](https://he.wikipedia.org/wiki/%D7%99%D7%95%D7%A2%D7%A5_%D7%9E%D7%A9%D7%9B%D7%A0%D7%AA%D7%90%D7%95%D7%AA)
- Dentists 9,100; institutional clinics: [dentalmarketing](https://www.dentalmarketing.co.il/video/blog/?ContentID=10275) · [State Comptroller](https://library.mevaker.gov.il/sites/DigitalLibrary/Documents/65c/2015-65c-211-BeriutHashen.pdf)
- Garages ~5,000 (2010): [State Comptroller](https://library.mevaker.gov.il/sites/DigitalLibrary/Pages/Reports/623-39.aspx)
- Elevator maintenance companies (~91): [Rips Group](https://www.rips-group.co.il/knowledge/companies/)
- Accounting practices: see `VALIDATION-DOC-CHASER-VS-SERVICE-RECALL-2026-10.md`

### Incumbent software
- Dental: [Rapid One](https://www.rapid-image.com/dentists-crm-software-ai/) · [SmileCloud](https://smilecloud.co.il/dental-clinic) · [BINA 2000](https://bina-2000.com/) · [Medform](https://medform.co.il/dentistry-module/) · [CRMOnline](https://www.crmonline.co.il/he/dental-clinic)
- Vet: [SmileCloud vet](https://smilecloud.co.il/vet-clinic) · [ClinicaOnline](https://ww2.clinicaonline.co.il/) · [Priza VetPro](http://www.priza.info/index3.aspx)
- Insurance: [Surense](https://www.surense.co.il/) · [Vibit](https://www.vibit.co.il/%D7%AA%D7%95%D7%9B%D7%A0%D7%94-%D7%9C%D7%A1%D7%95%D7%9B%D7%A0%D7%99-%D7%91%D7%99%D7%98%D7%95%D7%97/) · [Phoenix digital renewal interface](https://www.adifplus.co.il/%D7%94%D7%A4%D7%A0%D7%99%D7%A7%D7%A1-%D7%9E%D7%A0%D7%99%D7%A2%D7%94-%D7%9E%D7%9E%D7%A9%D7%A7-%D7%93%D7%99%D7%92%D7%99%D7%98%D7%9C%D7%99-%D7%9C%D7%A1%D7%95%D7%9B%D7%A0%D7%99%D7%9D-%D7%A2%D7%93%D7%9B/) · [TextMe insurance](https://textme.co.il/industries/sms-%D7%9C%D7%91%D7%99%D7%98%D7%95%D7%97/)
- Mortgage: [banta](https://banta.co.il/) · [Wise ₪119](https://wisecard.co.il/crm/) · [Eitan](https://info.m-eitan.co.il/) · [EZplan](https://www.ezplan.co.il/) · [Smartnpv](https://www.snpv.co.il/about/our_products)
- Building management: [Build App](https://www.build-app.co.il/) · [VaadPlus](https://vaadplus.co.il/) · [Ding](https://www.ding.co.il/) · [Bllink](https://bllink.co/) · [Dayarim](https://www.dayarim.co.il/) · [Binah](https://www.binaw.com/%D7%90%D7%97%D7%96%D7%A7%D7%AA-%D7%91%D7%A0%D7%99%D7%99%D7%A0%D7%99%D7%9D/) · [Hombi](https://hombi.co/)
- Pest: [PestBoss](https://www.pestboss.com/he/web/) · [Modular365](https://www.modular365.co.il/)
- Quotes: [Tik-Tok](https://tik-tok.co.il/) · [Bizli](https://bizli.co.il/) · [Fiix](https://fiix.co.il/) · [Kala CRM follow-up](https://www.kala-crm.co.il/%D7%9E%D7%A2%D7%A8%D7%9B%D7%AA-%D7%94%D7%A6%D7%A2%D7%95%D7%AA-%D7%9E%D7%97%D7%99%D7%A8) · [Quote Plus](https://quoteplus.co.il/) · [Morning proposals plus](https://www.greeninvoice.co.il/help-center/proposals-plus/)
- Field service / generic CRM: [Mobile4ERP](https://www.mobile4erp.com/%D7%AA%D7%95%D7%9B%D7%A0%D7%AA-%D7%9E%D7%A1%D7%95%D7%A4%D7%95%D7%A0%D7%99%D7%9D-%D7%9C%D7%98%D7%9B%D7%A0%D7%90%D7%99%D7%9D/) · [BaseCRM](https://basecrm.co.il/pro/customer-management/) · [Senzey](https://senzey.com/modules/item/1) · [Israeli Safety Center software](https://i-safety.co.il/%D7%AA%D7%95%D7%9B%D7%A0%D7%94-%D7%9C%D7%A0%D7%99%D7%94%D7%95%D7%9C-%D7%91%D7%98%D7%99%D7%97%D7%95%D7%AA/)
- Cleaning: [EasyWeek](https://easyweek.co.il/business/solutions/cleaning) · [Mishmarot](https://mishmarot.com/) · [EZshift](https://www.ezshift.co.il/)
- Garages / missed-call / reviews / appointments / accountants: see the two earlier reports in this folder

### Foreign proof
- [Uptick vs ServiceTrade](https://www.uptickhq.com/compare/uptick-vs-service-trade) · [Fire Inspected pricing](https://fireinspected.com/pricing/) · [Inspect Point review (FireITM)](https://fireitm.com/software/inspect-point/) · [Fire inspection software comparison](https://fireinspected.com/blog/fire-extinguisher-inspection-software-comparison/)
- [GorillaDesk (Software Advice)](https://www.softwareadvice.com/field-service/gorilladesk-profile/) · [Kukui](https://www.capterra.com/p/164990/Kukui-All-in-One-Success-Platform/) · [Skimmer pricing](https://www.getskimmer.com/pricing)
- [Jobber automation](https://www.getjobber.com/features/automate-repetitive-tasks/) · [Jobber review (pricing/users)](https://contractortoolstack.com/software/jobber/)

### Compliance drivers
- Extinguishers (IS 129): [Timrot](https://www.timrot.co.il/fire-extinguisher-inspection/) · [Midrag](https://www.midrag.co.il/Content/Tip/12561) · [Gil Safety](https://gilsafety.co.il/blog-bdikat-matafim-129.html)
- Hood cleaning (IS 1001-6, Form 16): [White Air](https://www.white-air.co.il/article104) · [mindafim Form 16](https://www.mindafim.co.il/%D7%90%D7%99%D7%A9%D7%95%D7%A8-%D7%A0%D7%99%D7%A7%D7%95%D7%99-%D7%9E%D7%A0%D7%93%D7%A4%D7%99%D7%9D-%D7%94%D7%9B%D7%9C-%D7%A2%D7%9C-%D7%98%D7%95%D7%A4%D7%A1-16-%D7%9B%D7%91%D7%90%D7%95%D7%AA/)
- Food-business sanitation regulations: [Nevo](https://www.nevo.co.il/law_html/law00/4867.htm)

### Pain / labour signals
- AC company secretary job (quote follow-ups, coordination): [mizug-avir.org](https://www.mizug-avir.org/%D7%93%D7%A8%D7%95%D7%A9%D7%99%D7%9D)
- Insurance renewal liability: [sarfati-law](https://sarfati-law.co.il/insurance-agent-liability) · [ronkinlaw](https://www.ronkinlaw.co.il/%D7%97%D7%99%D7%93%D7%95%D7%A9-%D7%A4%D7%95%D7%9C%D7%99%D7%A1%D7%94/)

### Legal
- Anti-spam: [consumers.org.il](https://www.consumers.org.il/category/email-spam-law) · [Bizportal damages](https://www.bizportal.co.il/financialconsumerism/news/article/20043454) · [Chamber of Commerce](https://www.chamber.org.il/serviceslobby/legal/74023/115485/)
- Privacy Amendment 13: [Goldfarb](https://www.goldfarb.com/he/%D7%9B%D7%A0%D7%99%D7%A1%D7%AA-%D7%AA%D7%99%D7%A7%D7%95%D7%9F-13-%D7%9C%D7%97%D7%95%D7%A7-%D7%94%D7%92%D7%A0%D7%AA-%D7%94%D7%A4%D7%A8%D7%98%D7%99%D7%95%D7%AA-%D7%9C%D7%AA%D7%95%D7%A7%D7%A3/) · [IAPP](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform)
- Stripe unavailable to Israeli merchants: [adircpa](https://adircpa.com/en/guides/stripe-israel-tax)
- WhatsApp Israel rates: [EngageLab](https://www.engagelab.com/blog/whatsapp-business-api-pricing) · [FlowCall](https://www.flowcall.co/blog/whatsapp-business-api-pricing)
