# Final Source Selection: Global "X → Google Sheets" Micro-SaaS

**Date:** 2026-10-08 · **Mode:** research only. Nothing was built, no accounts or partner applications were created, nobody was contacted, nothing was spent.
**Builds on:** `GLOBAL-MARKETPLACE-MICRO-SAAS-2026-10.md` (same folder)

## Evidence labels and an important limit

- **VERIFIED**: confirmed this session or in the prior report from first-party docs or listing extractions (cited).
- **COMPANY-CLAIMED**: a company's own figure.
- **ESTIMATE**: my estimate.
- **UNVERIFIED (prior knowledge)**: from my background knowledge, **not checked this session**. **Treat it as a hypothesis.**
- **UNKNOWN**: not established.

**Research-limit disclosure:**
- The web-search tool hit a **session limit partway through** this task ("session limit · resets 8:50pm UTC").
- Fresh searches this session covered **Etsy** (API tiers + competitors), **Calendly**, **Pipedrive** and **Asana**.
- Data for ClickUp, Notion, Hospitable, Hostaway, Shopify and the Workspace-Marketplace mechanics comes from **this folder's previous reports** (VERIFIED there).
- All other sources are scored from **UNVERIFIED prior knowledge**, are capped in confidence, and appear in a verification checklist (§Q).
- **No source with UNVERIFIED API access can be declared the winner.** That rule drives the verdict below.

---

## A. EXECUTIVE VERDICT

# **NO BUILD YET**

**Leading candidate (the only one I'd validate):** **Etsy → Google Sheets: an automatic "Etsy Profit & Bookkeeping Workbook"** (orders, fees, payouts, refunds, ads and shipping costs, auto-refreshed, with monthly profit and tax-ready tabs).

**The single missing proof:**
> **Etsy Commercial Access approval for this exact use (syncing a seller's orders and payment ledger into the seller's own Google Sheet).**

Why this is gating:
- Etsy's Open API v3 requires a **Personal App → manual Commercial Access review** before an app can be used by sellers "at a broader scale". Review weighs the API Terms (including **caching rules**), branding, OAuth and "proposed use of Etsy data" (VERIFIED, Etsy developer docs via search).
- Until approved, API access is **PARTNER-GATED**. The decision rule forbids a BUILD verdict on a gated source.

**Why Etsy leads despite the gate:**

| Criterion | Evidence |
|---|---|
| Largest relevant buyer base among non-dominated sources | Millions of active sellers; UNVERIFIED prior knowledge, about 5–9M |
| **Strongest visible search intent for exactly this job** | Someone **sells "Automated Etsy Orders Export to Google Sheets" as an Etsy listing**; a Chrome extension (Etsy2Sheet), SyncRange, Coupler.io guides, and MESA/Make/n8n templates all target it (VERIFIED, this session) |
| **No dominant Workspace add-on found** | Competition is fragmented: a one-click Chrome export, horizontal connectors, DIY templates |
| Recurring need is STRONG | Monthly bookkeeping, fees, taxes, profit per listing |
| Native gap | Etsy offers **manual CSV downloads only**; no scheduled Sheets sync (UNVERIFIED prior knowledge; recheck) |

**Why the obvious alternatives lose:**
- **ClickUp / Notion / Pipedrive / Asana** each already have a same-pattern incumbent or a native add-on:
  - ClickUp to Sheets, 21K installs.
  - Sync2Sheets, dominant for Notion.
  - **PipedriveSheets** (two-way, $12.99–$39.99).
  - **Asana Exports**, Asana's own add-on (all VERIFIED).
- **STR PMSs** (Hostaway / Hospitable) have VERY STRONG need but small user bases, weak Workspace search demand, and partner gates. Hospitable OAuth is partner-approved; Hostaway's commercial terms are UNKNOWN. **The user's rule "don't choose STR from familiarity" is respected.**
- **Calendly** is open and uncontested in the Workspace Marketplace, but its recurring need is only MODERATE. Calendly has native analytics on paid plans (UNVERIFIED), and Zapier covers the basic row-append (VERIFIED: Zapier/n8n/Integrately flows).

**What to do now:**
1. Run the 14-day pre-build validation (§M). It **includes applying for Etsy Personal App / Commercial Access**. That is the operator's action, outside this research. Apply only when the operator chooses.
2. Run a demand test with zero ad spend.
3. **Convert to BUILD only if Commercial Access is granted** and the demand thresholds pass.

---

## B. ALL-SOURCE SCORECARD

Weights: API 15 · Users 10 · Recurring need 15 · Native gap 10 · Competition survivability 10 · Marketplace discovery 15 · MVP simplicity 10 · Retention 5 · Pricing power 5 · Platform risk (low risk = high score) 5.

Side scores (0–10): **TB** = time to build, **TM** = time to first money, **BD** = built-in distribution, **MRR** = MRR potential.

**Confidence:** V = VERIFIED inputs dominate; P = partly verified; U = mostly UNVERIFIED (prior knowledge).

| Source | API access class | API /15 | Users /10 | Need /15 | Gap /10 | Comp /10 | Disc /15 | MVP /10 | Ret /5 | Price /5 | Risk /5 | **Total** | TB | TM | BD | MRR | Conf. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Etsy** | **PARTNER-GATED** (Commercial Access review) | 6 | 10 | 13 | 8 | 7 | 12 | 8 | 4 | 3 | 2 | **73** | 7 | 4 | 7 | 7 | P |
| Pipedrive | MOSTLY OPEN (U) | 13 | 7 | 12 | 6 | 4 | 10 | 8 | 4 | 3 | 4 | 71 | 8 | 6 | 6 | 5 | P |
| ClickUp | OPEN (U) | 13 | 9 | 10 | 6 | 3 | 11 | 8 | 4 | 3 | 4 | 71 | 8 | 5 | 6 | 4 | P |
| Klaviyo | OPEN (U) | 13 | 7 | 13 | 6 | 4 | 8 | 7 | 4 | 4 | 4 | 70 | 6 | 5 | 5 | 6 | U |
| Calendly | OPEN (U); webhooks likely paid-plan (U) | 12 | 9 | 9 | 6 | 8 | 9 | 9 | 3 | 2 | 3 | 70 | 9 | 5 | 5 | 4 | P |
| WooCommerce | OPEN (store REST keys) (U) | 13 | 9 | 12 | 5 | 3 | 8 | 7 | 4 | 3 | 4 | 68 | 7 | 4 | 5 | 5 | U |
| Hostaway | MOSTLY OPEN?: "Hostaway Public API" option for non-partners (V); commercial terms UNKNOWN | 9 | 3 | 14 | 8 | 9 | 6 | 8 | 4 | 4 | 3 | 68 | 7 | 4 | 4 | 4 | P |
| Airtable | OPEN (U) | 13 | 7 | 9 | 6 | 5 | 9 | 8 | 4 | 3 | 4 | 68 | 8 | 5 | 5 | 4 | U |
| HubSpot | OPEN for OAuth apps (U) | 12 | 9 | 12 | 4 | 3 | 9 | 7 | 4 | 4 | 4 | 68 | 6 | 4 | 5 | 5 | U |
| monday.com | OPEN (U); Pioneera GSheet Automation exists (V) | 12 | 8 | 10 | 5 | 4 | 9 | 8 | 4 | 3 | 4 | 67 | 7 | 5 | 6 | 4 | P |
| Stripe | OPEN (U) | 15 | 10 | 13 | 3 | 2 | 9 | 8 | 4 | 3 | 4 | 71→**64** (override: saturated, metrics tools dominate) | 8 | 4 | 5 | 4 | U |
| Shopify | OPEN (Shopify-app route) (V) | 13 | 10 | 12 | 5 | 2 | 6 | 7 | 4 | 2 | 4 | 65 | 6 | 4 | 6 | 4 | V |
| Lodgify | API key on paid plans (U) | 10 | 3 | 13 | 8 | 9 | 4 | 8 | 4 | 4 | 3 | 66 | 7 | 4 | 3 | 3 | U |
| Guesty | Open API for customers (U); marketplace partner-gated (V) | 8 | 3 | 14 | 7 | 8 | 4 | 7 | 4 | 4 | 3 | 62 | 6 | 3 | 4 | 4 | P |
| Webflow | OPEN (U) | 13 | 6 | 6 | 6 | 8 | 6 | 8 | 3 | 3 | 4 | 63 | 8 | 4 | 4 | 3 | U |
| Notion | OPEN (V prior) | 14 | 10 | 10 | 6 | 1 | 10 | 8 | 4 | 2 | 4 | 69→**60** (override: Sync2Sheets dominant) | 8 | 4 | 6 | 3 | V |
| Hospitable | **PARTNER-GATED** (OAuth approval; personal tokens not for third parties) (V) | 4 | 3 | 14 | 8 | 9 | 5 | 8 | 4 | 4 | 3 | 62 | 7 | 3 | 5 | 3 | V |
| PriceLabs | Customer API (U) | 7 | 3 | 10 | 7 | 8 | 3 | 7 | 4 | 3 | 3 | 55 | 6 | 3 | 2 | 2 | U |
| Asana | OPEN (U); **native "Asana Exports" add-on** (V) | 13 | 8 | 9 | 2 | 3 | 7 | 8 | 4 | 2 | 4 | 60→**55** (native) | 8 | 3 | 3 | 2 | V |
| Trello | OPEN (U) | 13 | 9 | 7 | 5 | 5 | 7 | 8 | 3 | 2 | 4 | 63 | 8 | 4 | 4 | 3 | U (search failed) |
| Google Ads | Developer token approval (U) | 7 | 10 | 14 | 1 | 1 | 6 | 6 | 4 | 3 | 2 | 54→**45** (Google's own Sheets add-on; Supermetrics et al.) | 5 | 3 | 4 | 4 | U |
| Meta Ads | **HARD** (App Review / advanced access for third-party ads_read) (U) | 3 | 10 | 14 | 3 | 1 | 6 | 5 | 4 | 3 | 1 | 50→**42** | 4 | 2 | 4 | 4 | U |
| Typeform / Jotform | OPEN (U); **native Google Sheets integrations** (U) | 13 | 9 | 5 | 1 | 2 | 5 | 9 | 2 | 1 | 4 | 51→**40** | 9 | 3 | 3 | 1 | U |
| Airbnb (direct) | **BLOCKED** for independent developers (U) | 0 | 10 | 14 | — | — | — | — | — | — | — | **REJECT** | — | — | — | — | U |

## C. TOP 5 SOURCES

| Rank | Source | Why it ranks | Fatal question |
|---|---|---|---|
| 1 | **Etsy** | Biggest base with the clearest DIY-demand evidence; fragmented competition; strong bookkeeping recurrence | **Commercial Access approval** |
| 2 | Pipedrive | Open API (U), B2B WTP, strong pipeline-reporting need | Can we beat **PipedriveSheets** (two-way, $12.99–$39.99) and Coefficient? |
| 3 | ClickUp | Huge base, proven demand | **ClickUp to Sheets already has 21K installs at $7–$32**, so we'd be the second entrant |
| 4 | Klaviyo | Strong marketing-reporting need; brands pay | Horizontal connectors (Supermetrics, Coupler, Porter; U) already cover it |
| 5 | Calendly | Open API (U); **no dedicated Workspace add-on found** | Recurring need only MODERATE; Zapier covers the basic row-append; $19 is hard for solo users |

## D. SOURCES REJECTED AND WHY

| Source | Reason |
|---|---|
| Notion | Dominated by Sync2Sheets (FR $5–8.4k MRR, 40–66k+ installs) |
| Asana | **Native** "Asana Exports" Workspace add-on (VERIFIED) + Coefficient + Unito |
| Typeform / Jotform | Native Google Sheets integrations (U) remove most of the value |
| Google Ads | Google's own Sheets add-on + Supermetrics-class tools (U); developer-token approval |
| Meta Ads | Third-party ads_read access needs App Review (U, HARD); dominated by reporting connectors |
| Stripe | Saturated; metrics SaaS (Baremetrics etc.) own the recurring-reporting job (U) |
| Shopify | 7+ existing Sheets-sync apps on the Shopify App Store (VERIFIED prior), price ceiling $5–$15 |
| Hospitable | **PARTNER-GATED**: OAuth partner approval required; personal tokens are explicitly not for third parties (VERIFIED) |
| Hostaway / Lodgify / Guesty / PriceLabs | Recurring need VERY STRONG, but **user bases are small** (thousands of PMs, U), Workspace search intent is weak, and commercial API terms are UNKNOWN. Not chosen; "don't pick STR from familiarity" |
| Airbnb | No public API for independent developers (U): BLOCKED |
| Webflow | Recurring need weak (CMS content isn't reviewed monthly in sheets) |
| Trello | Lower data value; weaker WTP (U). Search did not complete |

## E. ONE WINNER

**Etsy**, as the **leading candidate under a NO BUILD YET verdict**. It is not cleared to build until Commercial Access is granted.

## F. EXACT PRODUCT

| Item | Spec |
|---|---|
| Source platform | **Etsy Open API v3** (OAuth 2.0; seller-authorized; read scopes only, e.g. shops, listings, transactions/receipts, ledger/payments; exact scope names per Etsy docs) |
| Exact workflow | Install from the Workspace Marketplace → "Connect Etsy shop" (OAuth) → choose template → first import (last 12–24 months) → daily auto-refresh → workbook tabs update |
| Data synced | Receipts/orders, transactions (line items), listings (SKU, price, cost field kept by the user in the sheet), shop payment ledger entries (fees, Etsy Ads, shipping labels, refunds, deposits), currency. **Buyer PII minimized.** |
| Workbook tabs | 1 `Orders` (upsert by receipt ID) · 2 `Line Items` · 3 `Fees & Ledger` · 4 `Product Costs` (user-entered COGS per SKU) · 5 `Profit by Month` · 6 `Profit by Listing` · 7 `Tax Summary` (sales, refunds, fees by month/quarter) · 8 `Payouts Reconciliation` · 9 `Sync Log` |
| Recurring value | Every month the seller needs real profit after Etsy's fees, ads and shipping, plus bookkeeping/tax totals. Today that means downloading monthly CSVs and rebuilding sheets |
| Target customer | Etsy sellers doing roughly $1k–$50k/month who already use spreadsheets for bookkeeping (often with an accountant). Physical- and digital-product sellers |
| Pricing (proposal) | **Starter $19/mo** (1 shop, daily sync, all tabs) · **Pro $39/mo** (up to 3 shops, hourly sync, monthly email summary, 24-month history) · **Accountant $69/mo** (up to 10 client shops). Annual: 2 months free. No $5–$9 tier; a 14-day free trial instead |

## G. API / APPROVAL STATUS

| Item | Status |
|---|---|
| Public API + docs | **OPEN** (VERIFIED: Etsy Open API v3 docs) |
| Use on own shop (Seller App) | **OPEN** (VERIFIED: light approval) |
| Limited third-party use (Personal App) | **GATED** (detailed review; limited scale) (VERIFIED) |
| Broad third-party SaaS (Commercial Access) | **GATED** (manual review; "proposed use of Etsy data", caching rules, branding, OAuth) (VERIFIED) |
| Rate limits, ledger endpoint coverage, webhooks | **UNKNOWN** this session (prior knowledge: rate-limited per app; **no general webhooks, so polling**; UNVERIFIED) |
| Overall | **GATED** |

## H. DIRECT COMPETITORS

All VERIFIED as existing this session; pricing and installs not checked.

| Competitor | Type | Notes |
|---|---|---|
| **Etsy2Sheet** | Chrome extension | One-click export from the Orders page; dedupes by Order ID; **not automatic** |
| **SyncRange** | SaaS | Etsy OAuth → Sheets/BigQuery/Excel/Looker; on-demand or scheduled; horizontal |
| **Coupler.io** | Workspace add-on (horizontal) | Etsy → Sheets scheduled exports |
| **MESA / Make / n8n / Appy Pie** | Workflow templates | Row per order; DIY setup; no profit workbook |
| **"Automated Etsy Orders Export to Google Sheets"** | **A template sold on Etsy** | Proof sellers pay for this outcome |
| Bookkeeping/profit apps (e.g., Craftybase-type tools) | SaaS | UNVERIFIED pricing; adjacent, not Sheets-native |

**Competition class: MEDIUM (fragmented). No dominant Workspace add-on was found. Re-check the live Marketplace (§Q).**

## I. WHY WE CAN STILL WIN

1. **Outcome, not pipe.** Competitors move rows. We deliver *profit after all Etsy fees, ads and shipping* plus tax totals: the monthly job sellers actually do by hand.
2. **Sheets-native and accountant-friendly.** Plain formulas the seller and their accountant can edit. No new dashboard to learn.
3. **Automatic, unlike the Chrome-extension export.** Simpler and cheaper than horizontal connectors for this one job.
4. **Search intent already exists.** It shows up as DIY templates, a paid Etsy listing and how-to guides.
5. **Operator advantage, not used as a selection reason.** The operator runs an Etsy business (this repo), so dogfooding is immediate.

## J. EXACT MVP (build only after §O gates pass)

| Component | Spec | Classification |
|---|---|---|
| OAuth | Etsy OAuth 2.0 (PKCE) via a tiny backend (the token exchange needs the API key + redirect) | DAY-1 |
| Source connection | One shop per Sheet | DAY-1 |
| Destination | The current Sheet (`spreadsheets.currentonly` scope; **avoid Drive/Gmail restricted scopes**) | DAY-1 |
| Initial import | Paginated backfill, 12 months (24 on Pro) | DAY-1 |
| Scheduled sync | Daily time-driven trigger (Apps Script) calling the backend for fresh data | DAY-1 |
| Field mapping | Fixed schema (no custom mapping in v1) | DAY-1 |
| Dedup | Upsert by receipt ID / transaction ID / ledger entry ID | DAY-1 |
| Refresh status | `Sync Log` tab + "last synced" cell | DAY-1 |
| Error handling | Token refresh; retry/backoff; email-on-failure | DAY-1 |
| Billing | **Paddle** (merchant of record; supports Israeli sellers per the prior report) + license key | DAY-1 |
| Onboarding | 3-step sidebar + 60-second video + sample sheet | DAY-1 |
| Product layer | Profit/Tax/Payout tabs (formulas) | DAY-1 (core value) |
| Monthly email summary, multi-shop, accountant mode | — | POST-VALIDATION |
| Two-way edits, inventory writes, AI | — | DO NOT BUILD |

**Effort and cost:**
- **Hours (AI-assisted):** ~60–90.
- **Calendar time:** **2–3 weeks**.
- **Backend:** required, but tiny. It is needed for OAuth token storage/refresh, Etsy API-key secrecy and a license check.
- **Apps Script feasibility:** high for the sidebar, writer and scheduler.
- **Database:** minimal (tokens + license), e.g. Supabase free/Pro or Cloudflare D1/KV.
- **Infrastructure for the first 100 customers:** **$10–$40/mo** (ESTIMATE).
- **Support burden:** low–medium (OAuth reconnects; COGS-entry questions).
- **Class:** **EASY–MEDIUM**.

## K. EXACT TECH STACK

| Layer | Choice |
|---|---|
| Add-on | Google Apps Script (Editor add-on, HTML Service sidebar), published to the Workspace Marketplace |
| Backend | Cloudflare Workers (OAuth callback, token refresh, Etsy API proxy, license check) |
| Storage | Cloudflare KV/D1 (encrypted tokens), or Supabase |
| Billing | Paddle (subscriptions + license keys); webhooks to the Worker |
| Monitoring | Cloudflare logs + email alerts |
| Data residency | **No order data stored server-side.** Data passes through to the user's Sheet (simplifies privacy and Etsy caching compliance; to be confirmed against Etsy's API Terms §1) |

## L. EXACT BUILD-TIME ESTIMATE

| Phase | Hours |
|---|---|
| OAuth + token store (Worker) | 10–15 |
| Etsy API client (receipts, transactions, ledger, listings, pagination, rate-limit handling) | 15–20 |
| Apps Script sidebar + writer/upsert + triggers | 12–18 |
| Workbook templates (Profit, Tax, Payouts) | 10–15 |
| Paddle billing + license | 6–10 |
| Marketplace listing, OAuth consent, privacy policy/ToS | 6–10 |
| **Total** | **~60–90 h → 2–3 calendar weeks** for a solo operator using AI coding |

## M. EXACT 14-DAY PRE-BUILD VALIDATION

No ad spend, no contacting strangers. Steps marked (operator) are the operator's own decisions.

| Day | Action | Threshold / output |
|---|---|---|
| 1 | Re-run the blocked searches (§Q checklist): Workspace Marketplace "Etsy" query results with installs; Etsy API rate limits and ledger endpoints; caching terms | If an Etsy→Sheets add-on with >10k installs and a profit workbook exists, **kill** (dominated) |
| 1 | (Operator) Create an **Etsy Seller App** for their own shop (light approval) | API access to own data |
| 2–4 | Build a **manual prototype in a Google Sheet** on the operator's own shop: Profit by Month, Fees & Ledger, Tax Summary. Confirm the Etsy API exposes every needed ledger line | **Kill** if ledger/fee data is not available via the API at the needed granularity |
| 3 | (Operator) Submit the **Personal App** request with the exact use description. Prepare the **Commercial Access** request text | Submission done |
| 5–6 | Landing page with screenshots of the prototype (synthetic data) + waitlist + **"Founding seller $19/mo: reserve with a refundable $1 pre-authorization or a $0 commitment form"** (choose per payment-provider capability) | Live page |
| 6–12 | Traffic without ads: (a) the operator's own seller-community posts where self-promotion rules allow; (b) a **free** "Etsy Profit Sheet (manual CSV version)" template (on the operator's site, or as a free Etsy listing if policy allows) that funnels to the waitlist | **≥75 waitlist signups** and **≥15 "would pay $19+"** declarations, or **≥5 refundable pre-commitments** |
| 13 | Usability test: 5 waitlisted sellers paste their own CSVs into the manual version (self-serve, no calls required) | ≥3 of 5 say "I'd use this every month" |
| 14 | Decision: **BUILD only if** Commercial Access is granted (or the Personal App is approved and Commercial is pending with no objection) **and** the thresholds pass | Go / no-go |

## N. EXACT 30-DAY LAUNCH PLAN (if §M passes)

| Days | Action | Target |
|---|---|---|
| 15–28 | Build the MVP (§J). Dogfood on the operator's shop. Private test with 5 waitlisters (Personal App scale) | Stable daily sync for 7 days |
| 29–35 | OAuth consent screen + Marketplace listing submission (operator) | Listing approved |
| 36–44 | Invite the full waitlist; 14-day trial; founding price $19 locked for 12 months | 30 installs, 10 paying |
| 45 | Review: install→trial→paid funnel, sync errors, support time | Go / iterate |

## O. STRICT KILL CRITERIA

| Gate | Kill if |
|---|---|
| API | Etsy denies Personal App or Commercial Access for this use, **or** its API Terms forbid writing seller data into third-party destinations such as Google Sheets |
| Data | Fee/ledger detail needed for profit isn't available via the API (only partial order data) |
| Competition | A live Workspace or Etsy-ecosystem add-on already delivers an automatic *profit/tax workbook* with >10k installs |
| Demand (day 14) | Fewer than 75 waitlist signups or fewer than 15 "would pay $19+" (or fewer than 5 pre-commitments) |
| Usability (day 13) | Fewer than 3 of 5 testers would use it monthly |
| Launch (day 45) | Fewer than 10 paying, or trial→paid below 10% |
| Day 90 | Below $1k MRR, or monthly churn above 10% |

## P. $1K / $3K / $10K MRR MATH

Blended ARPU assumption ≈ **$27** (70% Starter $19, 25% Pro $39, 5% Accountant $69; ESTIMATE).

| Target | Customers needed |
|---|---|
| $1k MRR | ~37 |
| $3k MRR | ~111 |
| $10k MRR | ~370 |

**Gross margin (ESTIMATE):**

| Line | Value |
|---|---|
| Paddle | ~5% + $0.50 per transaction |
| Infrastructure | ~$0.30 per customer |
| Support | ~$1 per customer |
| Etsy API cost | $0 |
| Gross margin | **≈ 88–90%** |

**Funnel reality check:**
- At the Workspace benchmark of ~1% install→paid (Notion2Sheets, FR), 111 customers need ~11k installs.
- With a higher-intent funnel (free template → waitlist → trial; assume 5–10% trial→paid), 111 customers need ~1.1k–2.2k trials. **This is the assumption the day-14 test checks.**

## Q. SOURCES / EVIDENCE APPENDIX

### This session (VERIFIED)
- Etsy API tiers / Commercial Access: [Etsy Developer Portal](https://www.etsy.com/developers) · [Open API v3 docs](https://developers.etsy.com/documentation/) · [Authentication](https://developer.etsy.com/documentation/essentials/authentication/) · [How to Use Etsy's API (Help)](https://help.etsy.com/hc/en-us/articles/360025870013-How-to-Use-Etsy-s-API) · [VorpLabs on the commercial-access gate](https://vorplabs.com/agent-tools/etsy-api) · [API2Cart guide](https://api2cart.com/api-technology/etsy-developer-api/)
- Etsy → Sheets competition/demand: [Etsy listing "Automated Etsy Orders Export to Google Sheets"](https://www.etsy.com/listing/4334735689/automated-etsy-orders-export-to-google) · [Etsy2Sheet (Chrome)](https://chromewebstore.google.com/detail/etsy2sheet/lmojpijdhakpkeaijchijcojjbgjioah) · [SyncRange Etsy](https://syncrange.com/apps/etsy/) · [Coupler Etsy export](https://blog.coupler.io/etsy-to-csv/) · [MESA template](https://www.getmesa.com/templates/send-etsy-orders-to-google-sheets) · [Make Etsy↔Sheets](https://www.make.com/en/integrations/etsy/google-sheets) · [Appy Pie](https://www.appypie.com/connect/apps/etsy/integrations/google-sheets)
- Calendly: [Zapier Calendly→Sheets](https://zapier.com/blog/add-calendly-events-to-google-sheets/) · [n8n template](https://n8n.io/workflows/8032-auto-add-new-calendly-bookings-to-google-sheets/) · [Integrately](https://integrately.com/integrations/calendly/google-sheets) · [Calendar Event to Sheet add-on](https://workspace.google.com/marketplace/app/calendar_event_to_sheet/172591772513)
- Pipedrive: [PipedriveSheets (Pipedrive Marketplace)](https://www.pipedrive.com/en/marketplace/app/pipedrive-sheets/f48c99e028029bab) · [PipedriveSheets (Workspace)](https://workspace.google.com/marketplace/app/pipedrivesheets/194751097190) · [Outfunnel Google Sheets Sync](https://www.pipedrive.com/en/marketplace/app/google-sheets-sync/4430d70b162f8004) · [Coefficient guide](https://coefficient.io/save-pipedrive-deals-to-google-sheets)
- Asana: [Asana Exports (Workspace)](https://workspace.google.com/marketplace/app/asana/923474483785) · [Asana help: Google Sheets](https://help.asana.com/s/article/google-sheets-asana?language=en_US) · [Unito Spreadsheet Sync](https://workspace.google.com/marketplace/app/unito_spreadsheet_sync/548272798607)

### Prior report in this folder (VERIFIED there)
- Sync2Sheets/Notion2Sheets MRR and installs; ClickUp to Sheets (21K installs, $7–$32); Hospitable partner gating and PAT restrictions; Hostaway public API / partner selection; Shopify Sheets-sync app density; Paddle supports Israeli sellers; Workspace Marketplace mechanics (no fee, no paid featuring, ~1% install→paid benchmark).

### Verification checklist (blocked by the search limit; do on day 1)
1. Workspace Marketplace live search for "Etsy": listings, installs, ratings.
2. Etsy API rate limits; availability of ledger/payment endpoints and their granularity; webhook availability.
3. Etsy API Terms §1 caching and third-party-destination rules.
4. Calendly API access per plan and native analytics scope.
5. Pipedrive, ClickUp, Klaviyo, Airtable, HubSpot, Trello: confirm API terms and live Sheets competitors.
6. Typeform/Jotform native Sheets integrations (expected yes).
7. Meta / Google Ads developer access requirements.
8. Lodgify/Guesty/PriceLabs API access per plan.
9. Etsy active-seller count (latest 10-K).
