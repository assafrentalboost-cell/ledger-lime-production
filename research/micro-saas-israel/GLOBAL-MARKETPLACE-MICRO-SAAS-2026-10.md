# Global Micro-SaaS with Built-in Marketplace Distribution

**Date:** 2026-10-08 · **Mode:** research only. Nothing was built, no accounts were created, nothing was submitted, nobody was contacted, nothing was spent.
**Earlier reports in this folder:** Israel-local micro-SaaS studies, which concluded that distribution, not product, is the bottleneck.

**Labels used:**
- **VERIFIED**: official docs or the marketplace listing itself, as extracted by search.
- **FOUNDER-REPORTED**: a claim made by a founder.
- **3RD-PARTY EST.**: a third party's estimate.
- **INFERENCE**: my reasoning from verified facts.
- **UNKNOWN**: not established.

**Method limits:**
1. This environment blocks direct page fetches from apps.shopify.com, marketplace.atlassian.com, Capterra, G2, Indie Hackers and others (DNS or egress blocked; tested). All listing data (ratings, review counts, installs, prices) comes from **search-engine extractions of those listing pages**. Snapshots differ by date, and where sources conflict I show the range.
2. **Raw review mining was not possible.** Task 6 review themes come from review snippets quoted in listing extractions and third-party write-ups (marked THEMES-ONLY). This is the largest evidence gap. The 14-day plan includes reading raw reviews by hand.
3. Install counts ≠ paying customers ≠ revenue. Revenue is UNKNOWN unless a founder disclosed it.

---

## A. EXECUTIVE VERDICT

**One moderately strong pattern is worth validating.** It is not a single obviously-winning product. No candidate is strong enough to build blind.

**What the evidence says about marketplaces:**

| Marketplace | Finding | Implication |
|---|---|---|
| **Shopify** | Highest buyer intent and best billing (0% fee on the first **$1M lifetime**, then 15%; VERIFIED). Also the most saturated: about **18k–22.5k apps** (3RD-PARTY EST.). Developers report that the **first 10–50 installs rarely come from App Store search** and need outreach (forum anecdotes). Every boring utility we checked has entrenched leaders (Report Pundit ~1,800 reviews, Simprosys ~4,250, Matrixify ~1,700), is free from competitors (redirects), or is **native in Shopify Flow** (low-stock alerts, tagging) | Not a fast, solo-friendly entry in 2026 without a sharp wedge |
| **Atlassian** | Best economics for a solo developer: **Forge apps keep 100% of revenue until $1M lifetime** (from 1 Jan 2026; VERIFIED). Per-user tier pricing produces high ARPU (e.g., Better Excel Exporter is $319/mo at 100 users; VERIFIED vendor price). Buyers (Jira admins) shop *inside* the marketplace. One disclosed solo result: **$4,149 MRR after 18 months** (Agile Docs, FOUNDER-REPORTED, older post) | Strong distribution and ARPU. Many obvious niches are taken, and native Jira automation covers simple reminders |
| **monday.com** | Israeli platform; **native billing is mandatory** for new apps (no Stripe problem); only **869 apps** at end-2025 (VERIFIED, SEC filing); a vendor-published case of a **$30K MRR app portfolio** (Pioneera) | Less saturated than Shopify. However, the most-requested gap we checked (item → PDF) already has 6+ apps and a native Quotes & Invoices feature |
| **Google Workspace** | External billing; no listing fee; installs come from Marketplace search. The best-documented solo successes in this whole study are here: **Notion2Sheets/Sync2Sheets ($5k → $8.4k MRR, ~1% of installs paying; FOUNDER-REPORTED / 3RD-PARTY)** and **ClickUp to Sheets (21K+ installs, $7–$32/mo; vendor-reported)**. The founder says: *"users search for Notion, and Notion2Sheets is the first option they see"* | The clearest proof of "marketplace search produces paying users" for a boring sync tool |

**Winner to validate first (§G–§H):**
- **A Google Sheets add-on that live-syncs data from a popular SaaS that lacks a native Sheets sync.**
- **First instance:** short-term-rental PMS data (Hostaway / Hospitable / others) → auto-updating reservations, payout and owner-report tabs in Google Sheets.
- Today this needs a CSV export or a DIY Zapier setup (VERIFIED: Hospitable offers CSV exports; Zapier publishes Hospitable→Sheets templates). Zapier publishing ready-made templates for exactly this job is a demand signal.
- It matches the operator's STR expertise.
- **Distribution comes from two marketplaces:** the Workspace Marketplace search and the PMS's own app marketplace. Hospitable promises partners an Apps-page listing and co-marketing to about 18,000 subscribers (VERIFIED, dated marketing figure). Hostaway runs a partner marketplace with about 200 partners.

**Why it is not a sure thing:**
- The STR niche is small.
- Install→paid conversion on Workspace runs about **1%** (FOUNDER-REPORTED benchmark).
- Hospitable OAuth access requires **partner approval**.

**The 14-day plan therefore starts with a hard source-selection scan** (§K). If the STR instance fails its gates, the same build is pointed at the best-scoring alternative source.

---

## B. BEST MARKETPLACE TO ENTER

**Google Workspace Marketplace, for the first product.** It has:
- the clearest solo-founder proof for boring sync tools;
- no revenue share;
- Apps Script, which needs almost no hosting;
- a 1–3 week build;
- discovery through intent-based search.

Billing is external: **Paddle supports Israeli sellers** (VERIFIED via adircpa; Stripe does not support Israeli merchants).

**Atlassian (Forge) is the best second marketplace,** for higher ARPU once a validated niche is found (§D2).

**monday.com is the third.** Native billing and low saturation make it good for a follow-on app, but only after a quantitative gap scan.

---

## C. TOP 10 PRODUCT OPPORTUNITIES

| Rank | Product pattern | Marketplace | Foreign reference | Price | Reviews / installs | Marketplace discovery (0–10) | Competition | MVP difficulty | Build time | First-money window | Customers for $3k MRR | Main risk | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SaaS → Google Sheets live sync** (STR PMS first) | Workspace Marketplace + PMS app marketplace | Sync2Sheets/Notion2Sheets; ClickUp to Sheets; Unito Spreadsheet Sync | $9–$39/mo | Notion2Sheets: 40–66k+ installs, 400 paying (FR); ClickUp to Sheets: 21K installs (vendor) | **7** | LOW–MEDIUM (per source) | EASY | 2–3 weeks | MEDIUM (1–3 months) | ~158 at $19 | Small niche TAM; partner approval; ~1% conversion | **72** |
| 2 | Jira due-date / stale-issue reminder digests | Atlassian (Forge) | Reminder for Jira (Teamlead, 1,222 installs), Simple Reminder (111), e-Reminders, Due Date Alerts (6) | per-user tiers (~$1–$3/user at small sizes) | as listed | **8** | MEDIUM | EASY–MEDIUM | 2–3 weeks | MEDIUM | ~60–100 instances | Jira Automation covers basics natively | **64** |
| 3 | monday.com narrow utility (chosen by gap scan) | monday (native billing) | Pioneera portfolio ($30K MRR, vendor case study); Same Item Multiple Boards (4.9/98, 9.6K installs) | $8–$45/mo | as listed | **6** | VARIES | EASY–MEDIUM | 2–3 weeks | MEDIUM | ~100–200 | Picking a niche monday won't build natively | **60** |
| 4 | Shopify scheduled report / export to email/Sheets/FTP | Shopify | EZ Exporter (5.0/~100–120, $29.95+), Report Pundit (4.9/~1,800, $9–$35), Better Reports, SyncWith, Data Export IO | $9–$49 | as listed | 6 | **HIGH** | EASY | 2 weeks | MEDIUM–SLOW | ~100–150 | Entrenched leaders; first installs need outreach | **57** |
| 5 | Shopify → Google Sheets order sync | Shopify | Exportsy (4.8/27), eCommix (4.9/28), WEBI (4.3/15), OSync (4.1/9), GoSheet, Exportly | $5–$15 | as listed | 6 | MEDIUM (many weak apps) | EASY | 1–2 weeks | MEDIUM | 200–600 | Low price ceiling | **55** |
| 6 | Workspace Forms → PDF / document generation | Workspace | Form Publisher ($99/yr individual; $690/yr business), Document Studio (Digital Inspiration) | $8–$58/mo | large (UNKNOWN counts) | 7 | HIGH | MEDIUM | 3 weeks | SLOW | ~150 | Incumbents; Drive-scope verification (CASA risk) | **53** |
| 7 | Confluence page-review / expiry reminders | Atlassian | Better Content Archiving (Midori), Page Review Manager, Page Reminders, Outdated, Content Retention Manager, Breeze | per-user tiers | UNKNOWN counts | 7 | HIGH | EASY–MEDIUM | 2–3 weeks | MEDIUM | ~60–100 | Midori incumbent + native automation workaround | **52** |
| 8 | Shopify backups | Shopify | Rewind (4.3/628, $19+), Talon (4.3/42, $9+) | $9–$39 | as listed | 6 | MEDIUM | **HARD** (restore) | 6–10 weeks | SLOW | ~150 | Trust, restore complexity, support | **48** |
| 9 | HubSpot dedupe / data cleanup | HubSpot | Dedupely (4.9/~225), Insycle (4.7/65, ~7K installs) | $25–$100+ | as listed | 5 | HIGH + native dedupe | MEDIUM | 3–4 weeks | SLOW | ~60 | Certification gate (60 installs); native feature | **45** |
| 10 | Shopify 404 / redirect monitor | Shopify | SC Easy Redirects (4.6/~281, $14.99–$39.99), Redirect Ninja (4.9/61, free tier), Nabu (free) | $5–$15 | as listed | 6 | HIGH (free competitors) | EASY | 1 week | SLOW | 300+ | Free alternatives | **44** |

**Rejected on native-feature grounds:**
- **Shopify low-stock alerts:** Shopify Flow, free on Basic and up, includes a "notify when variant inventory is low" template (VERIFIED via guides).
- **Shopify order/product auto-tagging:** Flow can tag.

## D. TOP 3 BUILD CANDIDATES (each only after its validation gate passes)

1. **"[SaaS] → Sheets Live Sync" Workspace add-on, STR PMS first.**
2. **Jira reminder/digest Forge app.** Wedge: a scheduled JQL digest delivered to Slack/email plus per-assignee overdue nudges with snooze. It must beat what Jira Automation does natively. Proof the category sells: Teamlead's paid app has 1,222 installs.
3. **One monday.com utility app** in a niche selected by install-velocity data (apps-for-monday.com publishes installs per month per app). Native billing removes payment friction for an Israeli developer.

## E. TOP 3 RESEARCH-ONLY CANDIDATES

1. **Shopify scheduled reports.** Only with a sharp wedge (e.g., a WhatsApp/Slack daily KPI digest for small stores at $5–$9), and only if review mining shows leaders are too complex or expensive for micro-stores.
2. **Confluence content-review reminders.** Demand is real (community threads ask for it, and Confluence has no native review expiry; VERIFIED), but there are 6+ apps, including Midori's 15-year incumbent.
3. **STR PMS-native apps beyond Sheets** (owner statements, cleaner payouts) on the Hostaway / Hospitable / Guesty marketplaces. Partner approval gates apply, partner fees are UNKNOWN, and the user base is small.

## F. REJECTED ECOSYSTEMS (for this project, now)

| Ecosystem | Reason |
|---|---|
| Chrome Web Store | Native payments were shut down in 2020–21 (VERIFIED). Paid discovery is weak; disclosed outcomes like **20k users → 10 payers → $60 MRR** (TimeYourWeb, FOUNDER-REPORTED) are common |
| Figma Community | 15% fee, but a recent forum report says Figma is **not approving new paid sellers** (VERIFIED forum staff quote, recent) |
| Notion Marketplace | Templates only (8% + $0.40; VERIFIED), waitlist, limited payout countries. A content business, not SaaS |
| Bubble | 25% commission; developers report "pennies" and most earn under $100/mo (forum / 3RD-PARTY) |
| Slack Marketplace | Needs **10 active workspace installs before submission** and up to **10-week functional review** (VERIFIED). Standups and polls are dominated by Geekbot, Polly and others |
| HubSpot | Certification requires **60 active installs + 6 months listed** (VERIFIED). Dedupe/cleanup is crowded and partly native |
| Zapier / Make / n8n | No marketplace billing. n8n templates are free (12k+); paid templates are sold off-platform. Useful as *channels* for a SaaS, not as marketplaces |
| Framer | 100% of revenue to the creator (VERIFIED), but the plugin buyer base is small and template-led |
| Webflow Apps | Billing / revenue-share terms not confirmable from official sources; small buyer base for paid utilities |
| WordPress.org | Discovery only works for free plugins. Premium conversion via Freemius (7% + gateway; VERIFIED) is support-heavy and crowded. Possible later, not first |

## G. ONE WINNER TO VALIDATE FIRST

**Google Sheets add-on: live sync from a vacation-rental PMS (Hostaway first, Hospitable second) into a ready-made Sheets workbook** (Reservations, Payouts, Owner Report, Cleaning Schedule tabs). The same engine is reusable for other SaaS sources if the STR instance fails §M.

**Why this, over the higher-scoring-on-paper Atlassian idea:**
- (a) It is the only pattern with **multiple founder-reported solo revenue disclosures driven by marketplace search.**
- (b) It has the cheapest build and infrastructure (Apps Script).
- (c) It fits the operator's existing STR knowledge, so listing copy, templates and early users come from a community the operator already understands.
- (d) The source's own marketplace adds a second discovery channel.

**Explicit override:** the Jira idea has stronger marketplace discovery (8 vs 7), but higher native-feature risk. It is kept as candidate #2.

## H. EXACT PRODUCT CONCEPT

> **"RentalSheets: your rental data, live in Google Sheets."** (Working name; trademark check pending. Must not include "Hostaway", "Hospitable" or "Airbnb" in the brand. Those names may only appear descriptively, per each platform's partner rules.)

| Element | Spec |
|---|---|
| Who | Short-term-rental operators and co-hosts with 3–100 listings who already live in spreadsheets (owner reports, cleaner pay, occupancy tracking) |
| Job | Get reservations and payouts into Google Sheets automatically, and keep them updated, without Zapier wiring or weekly CSV exports |
| How | Sidebar in Sheets → connect PMS (API key/OAuth) → choose template → hourly/daily auto-refresh → owner-report tab with formulas per owner/property/month |
| Why monthly | The data changes daily (bookings, cancellations, payouts). The value is that the sheet stays current |
| Pricing | Free: 1 property, manual refresh. **Host $9/mo** (≤10 properties, daily sync). **Pro $19/mo** (≤50 properties, hourly sync, owner-report template). **Manager $39/mo** (unlimited, multiple PMS accounts). Annual: 2 months free |
| Billing | Paddle (merchant of record; supports Israeli sellers, VERIFIED via adircpa) with license-key check from Apps Script |

## I. EXACT MARKETPLACE LISTING (draft; English)

- **Title:** "RentalSheets – Sync Vacation Rental Reservations to Google Sheets"
- **Short description (≤200 characters):** "Auto-sync reservations, payouts and owner reports from your vacation rental software into Google Sheets. No Zapier, no CSV exports."
- **Long description:**
  > Running your rentals from spreadsheets? RentalSheets keeps them up to date automatically.
  > • Connect your property management software in two minutes
  > • Reservations, guests, nights, payouts and fees land in a clean, auto-refreshing sheet
  > • Ready-made Owner Report, Cleaning Schedule and Monthly Performance tabs, built with normal formulas you can edit
  > • Hourly or daily refresh. Cancellations update in place, with no duplicate rows
  > • Your data stays in your Google account. We only store your connection settings
  > Free for 1 property. Paid plans from $9/month.
- **Screenshots (5):**
  1. Before/after: CSV export chaos vs. live sheet.
  2. The sidebar connect flow.
  3. The Owner Report tab with a monthly payout table.
  4. The Cleaning Schedule tab sorted by checkout date.
  5. The "Last synced 10 minutes ago" indicator plus settings.
  - Use synthetic demo data only.
- **Demo:** a 60-second screen recording, with a sample sheet viewers can copy.
- **Categories:** Business tools / Productivity. **Keywords to target in the listing copy:** "vacation rental", "Airbnb reservations Google Sheets", "owner statement", "Hostaway", "Hospitable", "property management spreadsheet".

## J. EXACT MVP (Apps Script add-on; build only after the §K days 1–5 gates pass)

| Module | Day-1 | Later | Never (initially) |
|---|---|---|---|
| Sidebar UI (HTML Service) | Connect, pick template, sync now, schedule | Multi-account | — |
| PMS connector | **1 PMS** (Hostaway public API key flow, or Hospitable OAuth once approved) | 2nd/3rd PMS | Scraping Airbnb (never: ToS risk) |
| Sheets writer | Upsert by reservation ID; status changes; no duplicates | Custom column mapping | — |
| Templates | Reservations, Payouts, Owner Report (formulas), Cleaning Schedule | Occupancy/ADR dashboard | — |
| Scheduler | Time-driven triggers (daily/hourly) | — | Real-time webhooks (needs a server) |
| Licensing | Paddle checkout + license key stored in UserProperties; plan limits | Team licenses | — |
| Storage | None server-side beyond license checks (Paddle) | — | Storing reservation data on our servers |
| Scopes | `spreadsheets.currentonly` + `script.external_request` + `script.scriptapp` (triggers). **Avoid Drive/Gmail restricted scopes, so no CASA** (classification to verify) | — | — |
| AI | None | — | — |

**Infrastructure for 100 customers:** ≈ **$0–$20/mo**. Apps Script quotas apply. A tiny Cloudflare Worker for license validation would cost ~$0–$5.

**Fees:** Paddle ~5% + $0.50 per transaction (INFERENCE: typical merchant-of-record pricing; verify).

## K. EXACT 14-DAY ACTION PLAN (no money, no accounts beyond free ones, no outreach)

| Day | Action | Gate / output |
|---|---|---|
| 1 | **Source-selection scan** across 12 candidate sources: Hostaway, Hospitable, Guesty, OwnerRez, Lodgify, Smoobu, Asana, Trello, Calendly, Pipedrive, Airtable, Etsy. For each record: (a) existing Workspace add-ons and their installs; (b) Zapier "X + Google Sheets" templates; (c) native Sheets sync (yes/no); (d) API access without partner approval (yes/no); (e) user-base estimate | Pick the top 2 sources. **STR wins ties.** |
| 2 | Read raw Workspace listings and reviews for Sync2Sheets, ClickUp to Sheets, Unito Spreadsheet Sync, Coupler.io. Extract complaints (pricing, sync failures, limits) | Pain list + wedge |
| 3 | Read Hostaway/Hospitable API docs and partner pages. Confirm rate limits, fields, auth, partner requirements, and whether a third-party Sheets tool may use customer API keys | **Kill** the STR instance if third-party use needs approval that's unlikely for a solo developer → switch to the next source |
| 4 | Check OAuth scope classification in a free Google Cloud project (no app submitted) | **Kill** the add-on approach if sensitive-scope verification is unavoidable and slow → consider a web app with `drive.file` |
| 5 | Write the listing draft + 5 screenshot mockups (Figma/Canva with fake data) | Listing ready |
| 6–7 | **Demand test without contacting anyone:** publish a free landing page + waitlist (free hosting). Post a *non-promotional* how-to in public STR communities the operator already belongs to, only where self-promotion is allowed (operator decision; no DMs) | ≥30 waitlist signups is a positive signal |
| 8–13 | Build the MVP (§J) for the chosen source, using the operator's own PMS account/sandbox and synthetic data | Working add-on, unlisted |
| 14 | Go/no-go on submitting to the Marketplace (submission is the operator's decision, outside this research) | Decision |

## L. EXACT 30-DAY ACTION PLAN (after day 14, operator-approved)

| Days | Action | Target |
|---|---|---|
| 15–18 | Submit to the Workspace Marketplace (private test → public). Apply for the PMS partner listing if relevant | Listing live or in review |
| 19–25 | Onboard waitlist users manually (screen-share). Fix setup friction. Ask for honest reviews | 20 installs, 10 active syncs |
| 26–30 | Turn on paid plans. Offer founding-user pricing ($5/mo locked for 12 months). Measure install→active→paid | ≥5 paying users |

## M. STRICT KILL CRITERIA

| By | Kill if… |
|---|---|
| Day 3 | The chosen PMS forbids or gates third-party API-key use for this purpose, and no other STR PMS with open access exists → switch to the best non-STR source from the day-1 scan. Kill the pattern if no source scores ≥3 of the 5 day-1 gates |
| Day 1 | A free or native Sheets sync with >5k installs already exists for the chosen source → move to the next source |
| Day 4 | The Sheets add-on cannot avoid restricted scopes (CASA cost/time) → re-scope to a web app or kill |
| Day 7 | Fewer than **15** waitlist signups from organic posts and the listing preview → STR instance killed. Retry with the next source once; if that also fails → **NO GOOD CANDIDATE** in this ecosystem |
| Day 30 after listing | Fewer than **50 installs** or fewer than **5 paying** users → stop paid development; keep it free or archive |
| Day 90 after listing | Below **$500 MRR**, or install growth flat for 4 weeks → archive; move to candidate #2 (Jira Forge) |

---

# DETAILED WORK (Tasks 1–17)

## §1. Ecosystem map (Task 1)

| Marketplace | Size (approx.) | Paid apps / billing | Fee / revenue share | Listing / review gate | Israel developers | Discoverability | Acquisition quality |
|---|---|---|---|---|---|---|---|
| **Shopify App Store** | ~18k–22.5k apps (3RD-PARTY, 2026) | Mandatory Shopify Billing API | **0% on first $1M lifetime** (counted from 1 Jan 2025), then 15%; 15% on everything for big developers; 2.9% processing (VERIFIED docs) | App review; quality standards | INFERENCE: yes (Israeli app companies operate; payout country list not confirmed) | Search, categories, reviews-driven ranking, paid search ads | **STRONG intent / brutal competition** |
| **Atlassian Marketplace** | 8,000+ apps, 1,800 partners (VERIFIED/3RD-PARTY) | Atlassian billing; per-user tiers | Forge: partner gets 84%, moving to 83% (Oct 2026); **100% until $1M lifetime Forge revenue** (from 1 Jan 2026); Connect 75–80% (VERIFIED) | Forge-only for new apps since Sep 2025; EULA, privacy policy, support desk | INFERENCE: yes | Search, categories, badges (Runs on Atlassian), reviews | **STRONG** |
| **monday.com Marketplace** | 869 apps; 704 natively monetized (VERIFIED, SEC filing) | **Native billing mandatory for new apps since Jul 2024**; seat-bucket pricing; trials required for seat-based apps | 15% only after $200K lifetime revenue (VERIFIED) | Review of app and pricing (72 business hours for pricing) | Yes (Israeli company) | Search, categories, editor's choice | **MODERATE–STRONG** |
| **Google Workspace Marketplace** | Very large (UNKNOWN count) | External billing | None (no listing fee; can't pay for featuring) (VERIFIED) | OAuth verification for sensitive scopes; **CASA for restricted scopes** (~$500–$1,800/yr Tier 2; 3RD-PARTY) | Yes | Search; editor's choice needs 10k–100k installs | **MODERATE–STRONG** (proven for sync tools) |
| **Wix App Market** | UNKNOWN | Wix billing | **100% first 12 months**, then 80/20 after 2.5% fee (VERIFIED docs) | Review | Yes (Israeli company) | Search/categories | MODERATE (lower-WTP users, INFERENCE) |
| **Slack Marketplace** | ~2,600+ apps (3RD-PARTY) | External | None stated | **≥10 active workspace installs before submission**; review up to 10 weeks (VERIFIED) | Yes | Search | WEAK–MODERATE |
| **HubSpot App Marketplace** | UNKNOWN | External (3RD-PARTY) | No listing fee (3RD-PARTY) | Listing via review; **certification needs 60 installs + 6 months** (VERIFIED) | Yes | Search, certification badge | MODERATE |
| **Chrome Web Store** | Very large | **None** (native payments ended 2021; VERIFIED) → ExtensionPay (5% + Stripe) etc. | — | Review | Yes (but Stripe not for Israeli merchants) | Search; weak for paid | **WEAK** for paid |
| **Figma Community** | Large | Figma payments | 15% (VERIFIED) | **New paid sellers reportedly not being approved** (recent forum) | Country list UNKNOWN | Search | WEAK (gated) |
| **Notion Marketplace** | Large (templates) | Notion payments (templates) | 8% + $0.40 (VERIFIED help page) | Waitlist + approval + Stripe onboarding | Country list restricted, UNKNOWN for Israel | Search | WEAK for SaaS |
| **Bubble Plugins** | UNKNOWN | Bubble billing ($1–$100/mo subscriptions) | **25%** (VERIFIED policy) | Review | Yes | Search | WEAK (low $) |
| **Framer Marketplace** | UNKNOWN | Framer | **Creator keeps 100%** (VERIFIED help center) | Submission review | UNKNOWN | Search | WEAK–MODERATE (small) |
| **Webflow Apps** | 300+ apps (3RD-PARTY) | UNKNOWN | UNKNOWN (20–30% unsourced claim) | Review | UNKNOWN | Search | WEAK–MODERATE |
| **Zapier / Make / n8n** | 12k+ n8n free templates | **No billing** | — | Integration review (Zapier) | Yes | Directory listing for SaaS integrations | Channel only |
| **WordPress.org** | 60k+ plugins (INFERENCE) | No paid on .org; Freemius 7% + gateway (VERIFIED) | — | Plugin review | Yes (Freemius is Israeli-founded, INFERENCE) | Strong for free plugins | MODERATE (freemium funnel) |
| **Hostaway Marketplace** (niche) | ~200 partners (VERIFIED) | External | Partner terms UNKNOWN | Partner application + certification (VERIFIED) | Yes | In-product marketplace | MODERATE (small but high-intent) |
| **Hospitable Apps** (niche) | UNKNOWN | External | UNKNOWN | **OAuth partner approval** required for marketplace listing (VERIFIED) | Yes | Apps page + co-marketing to ~18k subscribers (dated, VERIFIED marketing) | MODERATE |

## §2–§3. 50+ real products with commercial evidence (Tasks 2–3)

Evidence class:
- **S** = STRONG: hundreds+ reviews/installs + paid tiers, or founder revenue.
- **M** = MODERATE: dozens of reviews + paid tiers.
- **W** = WEAK: few reviews.
- **U** = UNKNOWN.

Revenue is UNKNOWN unless stated.

| # | Product | Marketplace | Problem | Price | Reviews · rating | Installs/users | Complexity | Evidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Matrixify | Shopify | Bulk import/export/migrate via Excel/CSV/Sheets | Free demo → paid | ~1,700–1,744 · 4.9 | — | HARD | S |
| 2 | Report Pundit | Shopify | Custom + scheduled reports | Free, $9, $19, $35 | ~1,735–1,809 · 4.9 | — | MEDIUM | S |
| 3 | Better Reports | Shopify | Custom reports, scheduled email/Sheets | $19.90–$299.90 by Shopify plan | ~577–1,200 · ~5.0 | — | MEDIUM | S |
| 4 | EZ Exporter | Shopify | Scheduled exports to FTP/Sheets/email | $29.95–$149.95 | ~100–120 · 5.0 | — | MEDIUM | M |
| 5 | Sufio | Shopify | Professional invoices | $7–$129 (+$499 Sufio+) | 419 · 4.9 | — | MEDIUM | S |
| 6 | Ablestar Bulk Product Editor | Shopify | Bulk edits with undo/history | Free, $30, $60, $120 | 523 · 4.9 | — | MEDIUM | S |
| 7 | syncX Stock Sync | Shopify | Supplier feed → inventory/price sync | Free → paid by SKU | ~844–928 · 4.7 | — | MEDIUM | S |
| 8 | Stock sync: Inventory autosync (Tible) | Shopify | Multi-store stock sync | $7–$20 | 2 | — | MEDIUM | W |
| 9 | Simprosys Google Shopping Feed | Shopify | Google/Meta product feeds | $2.99–$17.99+ by products | ~4,252 · 4.9 | — | MEDIUM | S |
| 10 | SC Easy URL Redirects | Shopify | 404 tracking + redirects | Free, $14.99, $39.99 | ~254–284 · 4.6 | — | EASY | M |
| 11 | Redirect Ninja | Shopify | AI 404 fixes | Free tier | 61 · 4.9 | — | EASY | W–M |
| 12 | SEOFlow 404 Link Redirect | Shopify | 404 redirects | $6 | 0 | — | EASY | W |
| 13 | Rewind Backups | Shopify | Store backup/restore | $19, $99… | 628 · 4.3 | — | HARD | S |
| 14 | Talon Backups | Shopify | Backup | $9–$69 | 42 · 4.3 | — | HARD | M |
| 15 | O: Auto Tag Order & Customer | Shopify | Rule-based tagging | Free, $7.99–$16.99 + usage | 76 · 4.9 | — | EASY | M |
| 16 | Auto Tags (all-in-one) | Shopify | Tagging | $8–$15 | 146 · 4.9 (3rd-party) | — | EASY | M |
| 17 | TR: Auto Tag Orders, Customers | Shopify | Tagging | Free tier | 43 · 4.9 | — | EASY | W–M |
| 18 | Shopaw Order Tagger | Shopify | Tagging | $4.99–$9.99 | 5 · 4.6 | — | EASY | W |
| 19 | LSA Low Stock Alert | Shopify | Low-stock emails | from $5.99 | 32 · 4.5 | — | EASY | W–M |
| 20 | MB Low Stock Alert | Shopify | Low-stock alerts | Free, $9.99–$19.99 | 7 · 5.0 | — | EASY | W |
| 21 | iAlert Low Stock | Shopify | Email/Slack alerts | Free, $2.99 | UNKNOWN | — | EASY | W |
| 22 | Exportsy Sync to Google Sheets | Shopify | Orders → Sheets | Free + paid | 27 · 4.8 | — | EASY | M |
| 23 | eCommix Google Sheets Sync | Shopify | Two-way Sheets sync | Free + paid | 28 · 4.9 | — | MEDIUM | M |
| 24 | WEBI Orders to Google Sheets | Shopify | Orders → Sheets | $9.99 | 15 · 4.3 | — | EASY | W–M |
| 25 | OSync: Export Orders to Sheet | Shopify | Orders → Sheets | Free (50 orders) + paid | 8–9 · 4.1–4.2 | — | EASY | W |
| 26 | GoSheet | Shopify | Orders → Sheets | Free, $8.99, $14.99 | UNKNOWN | — | EASY | W |
| 27 | Exportly Google Sheets Sync | Shopify | Orders → Sheets | $4.99 / $49 yr | 0 | — | EASY | W |
| 28 | Sync2Sheets (Notion2Sheets) | Workspace | Notion DB → Sheets live sync | Paid tiers | — | 40k–66k+ installs (FR/3RD) | EASY | **S** (FR: $5k–$8.4k MRR; 400 paying; Latka est. $75.9K ARR) |
| 29 | ClickUp to Sheets | Workspace | ClickUp ↔ Sheets sync | $7–$32 | 4.8 (vendor) | **21K+ installs (vendor)** | EASY–MEDIUM | M–S |
| 30 | Unito Spreadsheet Sync | Workspace | Multi-tool ↔ Sheets | UNKNOWN | UNKNOWN | UNKNOWN | HARD | U |
| 31 | BudgetSheet | Workspace (Sheets) | Bank-feed budgeting in Sheets | Paid | UNKNOWN | UNKNOWN | MEDIUM (bank → excluded category) | M (FR $1.6k MRR) |
| 32 | Form Publisher (Talarian) | Workspace | Forms → PDF/Docs | Free; $99/yr; $690/yr | UNKNOWN | UNKNOWN | MEDIUM | M |
| 33 | Document Studio (Digital Inspiration) | Workspace | Docs/PDF/email from Sheets/Forms | Free (25/mo) + paid | UNKNOWN | UNKNOWN | MEDIUM | M |
| 34 | Email Notifications for Google Forms | Workspace | Form → email rules | Free + paid | UNKNOWN | UNKNOWN | EASY | M |
| 35 | Timepiece – Time in Status (OBSS) | Atlassian | Status-duration reports | Free ≤10 users; ~$13.2/mo tier | 270 · ~4.8 | ~4,339–4,439 installs | MEDIUM | S |
| 36 | Time in Status (SaaSJet) | Atlassian | Same | ~$12.65 tier | 207 · ~4.5 | 5,256 installs | MEDIUM | S |
| 37 | Better Excel Exporter (Midori) | Atlassian | Jira → Excel | Free ≤10 users; $319/mo @100 users | UNKNOWN | UNKNOWN | MEDIUM | M |
| 38 | JXL for Jira | Atlassian | Spreadsheet view | Tiered per user | UNKNOWN | UNKNOWN | HARD | M |
| 39 | Agile Docs | Atlassian | Estimate rollups | Paid | UNKNOWN | UNKNOWN | MEDIUM | M (FR $4,149 MRR, older) |
| 40 | Reminder for Jira (Teamlead) | Atlassian | Issue reminders, recurring | Paid via Atlassian | UNKNOWN | 1,222 installs | EASY | M |
| 41 | Simple Reminder | Atlassian | JQL/due-date reminders | UNKNOWN | UNKNOWN | 111 installs | EASY | W |
| 42 | Due Date Alerts (addressHQ) | Atlassian | 7/3/1-day due emails | UNKNOWN | UNKNOWN | 6 installs | EASY | W |
| 43 | e-Reminders for Jira | Atlassian | Scheduled JQL email | Paid | UNKNOWN | UNKNOWN | EASY | W |
| 44 | Better Content Archiving (Midori) | Atlassian | Confluence lifecycle | Per user | UNKNOWN | UNKNOWN | MEDIUM | M |
| 45 | Page Review Manager | Atlassian | Confluence review cadence | Per user | UNKNOWN | UNKNOWN | EASY | W |
| 46 | Page Reminders for Confluence | Atlassian | Page reminders | Per user | UNKNOWN | UNKNOWN | EASY | W |
| 47 | Same Item Multiple Boards (Pioneera) | monday | Sync items across boards | Paid (native) | 98 · 4.9 | 9.6K installs | MEDIUM | S (portfolio $30K MRR, vendor case) |
| 48 | DocExport PDF Generator | monday | Board/item → PDF/DOCX | $15 (≤10 users) / $45 (scraper sample) | 44 · 5.0 (sample) | ~5,500 (sample) | MEDIUM | M |
| 49 | Board Print to PDF (Tower Apps) | monday | Free board → PDF | Free | UNKNOWN | 1,552 | EASY | W (free funnel) |
| 50 | Export Items & Subitems to PDF | monday | Item → PDF | Paid | UNKNOWN | 61 (+5/mo) | EASY | W |
| 51 | DocCreate | monday | Automated Word/PDF docs | Paid | UNKNOWN | UNKNOWN | MEDIUM | U |
| 52 | The PDF Maker | monday | Docs + e-sign | Paid | UNKNOWN | UNKNOWN | MEDIUM | U |
| 53 | DocuGen | monday/HubSpot | Docs + e-sign | Paid | UNKNOWN | UNKNOWN | MEDIUM | U |
| 54 | GetSign | monday | Quotes/invoices + e-sign | Paid | UNKNOWN | UNKNOWN | MEDIUM | U |
| 55 | Insycle | HubSpot | Data cleanup/dedupe | Record-based | 65 · 4.7 (G2: 192) | ~7K installs | HARD | S |
| 56 | Dedupely | HubSpot | Dedupe | Paid | ~225 · 4.9 | UNKNOWN | MEDIUM | S |
| 57 | Geekbot | Slack | Async standups | $3/user/mo; free ≤10 | — | 200k users (claim) | MEDIUM | S |
| 58 | TimeYourWeb | Chrome | Time tracking | Paid tier | — | 20k users → **10 payers, $60 MRR (FR)** | EASY | W (counter-example) |

## §4–§5. Boring winners and competitor density (Tasks 4–5)

| Pattern | Close competitors | Top competitor reviews | Typical price | Dominated? | Native feature? | Density |
|---|---|---|---|---|---|---|
| SaaS → Sheets sync, **per source** | 0–3 per source (Notion: Sync2Sheets + others; ClickUp: ClickUp to Sheets; STR PMS: **none found; Zapier templates only**) | Sync2Sheets/ClickUp to Sheets in their niches | $7–$39 | By source | Usually no (Hospitable: CSV only, VERIFIED) | **LOW–MEDIUM** |
| Jira reminders/digests | ~6 apps; the largest has 1,222 installs | Low | Per user | No | **Jira Automation can schedule JQL emails** (community workaround) | MEDIUM |
| Shopify scheduled reports | 8+ | 1,800+ | $9–$150 | Yes | No native scheduling (3RD-PARTY) | HIGH |
| Shopify → Sheets orders | 7+ weak apps | 27–28 | $5–$15 | No | No | MEDIUM (low price) |
| Shopify low-stock alerts | 5+ | 32 | $3–$20 | No | **Flow template** | REJECT |
| Shopify tagging | 6+ | 146 | $5–$17 | No | **Flow** | REJECT |
| Shopify redirects/404 | 6+ incl. free | 281 | $0–$40 | No | Partial native | HIGH |
| Shopify backups | 5+ | 628 | $9–$99 | Rewind | No | MEDIUM (hard build) |
| monday docs/PDF | 6+ (DocExport, DocCreate, PDF Maker, DocuGen, GetSign, Eledo, Export Items to PDF) | ~44 | $15–$45 | No | Native Quotes & Invoices (CRM) + dashboard PDF scheduling | HIGH |
| Confluence review reminders | 6+ incl. 15-year Midori | UNKNOWN | Per user | Midori | No native expiry (VERIFIED) | HIGH |
| HubSpot dedupe | 4+ | 225 | $25+ | — | Native dedupe in paid tiers | HIGH |

## §6. Review mining (Task 6): THEMES-ONLY (raw pages blocked)

| Product / category | Users love | Complaints | Gap we could exploit |
|---|---|---|---|
| Matrixify | Handles huge catalogs; dry runs; 24/7 Slack support | Learning curve; price "a bit high"; a Sep-2026 billing complaint | Simpler single-purpose tools for small stores |
| EZ Exporter | Custom formats; support | "Best for someone very familiar with Shopify… some programming" | No-code template presets for non-technical users |
| Report Pundit / Better Reports | Prebuilt + custom reports; support builds reports | "Not intuitive enough"; limited scheduling (Better Reports) | Opinionated digest instead of a report builder |
| syncX Stock Sync | Automation of supplier feeds | Delayed/slow syncs; billing counted all SKUs | Transparent pricing; reliability |
| Rewind | Reliability | **$9 → $19 price increase**; no offline copy | Cheaper/offline backup (but hard build) |
| Low-stock apps | Easy setup | Dashboards failing; emails not sent (LSA) | Moot: Flow is native |
| Sync2Sheets (pattern) | "First option" in search; time saved | Conversion only ~1%; quiet months (FR) | Vertical templates (owner reports) raise perceived value vs. a generic sync |
| ClickUp to Sheets | Two-way sync, scheduled | Two-way locked to paid tiers | — |
| Timepiece / Time in Status | Find bottlenecks; support | Per-user billing on the whole instance (community question) | Small-team-friendly pricing |
| TaxDome-style portals (earlier report) | — | Login friction | **No-login, in-tool** experiences win: Sheets add-ons live where users already work |

**PAIN USERS PAY FOR (across categories):**
1. Getting data out of a closed tool into a sheet/report **without manual exports**.
2. **Staying current** automatically.
3. Templates that turn raw data into a business view (report, statement).
4. Responsive support during setup.

**GAP WE COULD EXPLOIT:** vertical, template-led Sheets sync for an industry whose software lacks it, starting with STR. The operator knows that workflow.

## §7. Buildability (Task 7), top candidates

| Candidate | Frontend | Backend | DB | Auth | Billing | Platform auth/API | Webhooks | Cron | Storage | AI | Build time | First-version hours | Infra / 100 customers | Class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **#1 Sheets sync (STR)** | Apps Script HTML sidebar | Apps Script (+ optional tiny license worker) | None (UserProperties) | Google account | Paddle + license key | PMS API key/OAuth | No (polling) | Time-driven triggers | None | No | **2–3 weeks** | 40–70 | **$0–$20** | **EASY** |
| #2 Jira reminders (Forge) | Forge UI Kit | Forge functions | Forge storage | Atlassian | Atlassian billing | Jira REST via Forge | Optional | Forge scheduled triggers | Forge KVS | Optional | 2–3 weeks | 50–80 | ~$0 (Forge-hosted; INFERENCE) | EASY–MEDIUM |
| #3 monday utility | React (monday views) | Node (serverless) or monday code | Small | monday OAuth | **monday native** | monday GraphQL API | Yes | Yes | Small | Optional | 2–3 weeks | 60–90 | $20–$50 | EASY–MEDIUM |
| #4 Shopify scheduled digest | Remix/Polaris embedded app | Node | Postgres | Shopify OAuth | Shopify Billing API | Admin GraphQL | Yes (GDPR webhooks required) | Yes | Small | Optional | 3 weeks | 80–120 | $20–$60 | MEDIUM |
| #7 Confluence review reminders | Forge | Forge | Forge storage | Atlassian | Atlassian | Confluence REST | — | Scheduled triggers | KVS | No | 2–3 weeks | 50–80 | ~$0 | EASY–MEDIUM |

## §8. Platform dependency risk (Task 8)

| Candidate | API limits | Policy risk | Feature-copy risk | Billing restrictions | Review rejection | Deprecated APIs | Suspension | **Overall** |
|---|---|---|---|---|---|---|---|---|
| #1 Sheets sync | Apps Script quotas; PMS rate limits | Google scope policy; PMS partner terms | PMS adds a native Sheets sync (MEDIUM) | None (external) | Low–medium (OAuth verification) | Low | Low | **MEDIUM** (two platforms) |
| #2 Jira reminders | Forge limits | Atlassian policy | **Jira Automation improvements (MEDIUM–HIGH)** | Atlassian billing | Medium | Connect→Forge done | Low | **MEDIUM** |
| #3 monday utility | monday API complexity limits | Mandatory native billing | monday builds natively (MEDIUM) | Native only | Medium | Low | Low | **MEDIUM** |
| #4 Shopify digest | Generous | App Store rules strict | Shopify analytics improvements | Billing API mandatory | Medium | Low | Low | **MEDIUM** |

## §9. Economics (Task 9)

| Candidate | Price points | Blended ARPU | $1k MRR | $3k MRR | $10k MRR | Fees | Infrastructure | Gross margin | Churn risk |
|---|---|---|---|---|---|---|---|---|---|
| #1 Sheets sync | $9 / $19 / $39 | ~$19 | 53 | **158** | 527 | Paddle ~5% + $0.50 (INFERENCE) | ~$0–$20 | **~90%+** | Medium (seasonal hosts) |
| #2 Jira reminders | Per-user tiers (≈$10–$50/instance small–mid) | ~$30 | 34 | 100 | 334 | 0% up to $1M Forge revenue | ~$0 | ~95% | Low (embedded) |
| #3 monday utility | $8–$45 | ~$20 | 50 | 150 | 500 | 0% until $200K, then 15% | $20–$50 | ~90% | Medium |
| #4 Shopify digest | $9 / $19 | ~$12 | 84 | 250 | 834 | 0% until $1M + 2.9% | $20–$60 | ~90% | High (store churn) |

**Feasibility check for #1 (INFERENCE):**
- At the Workspace benchmark of ~1% install→paid, $3k MRR needs ~16k installs. **That is unrealistic for an STR-only niche via Workspace search alone.**
- The STR instance only reaches $3k MRR if:
  - **(a)** PMS-marketplace and community traffic converts much better (B2B operators with an explicit pain; assume 3–8%), and/or
  - **(b)** the engine is extended to 2–3 PMSs plus 1 large horizontal source.

  The day-1 scan decides this.

## §10. Distribution reality (Task 10)

| Candidate | How users discover it | Keywords | Free plan helps ranking? | Listing converts alone? | External marketing still needed? | **Marketplace discovery 0–10** |
|---|---|---|---|---|---|---|
| #1 Sheets sync | Workspace search ("Hostaway Google Sheets", "Airbnb reservations sheet", "owner statement"); PMS Apps page; Zapier template seekers | Listed in §I | Yes (installs and reviews feed editor's choice thresholds) | Partly. Notion2Sheets says search + good images/copy drove installs (FR) | Some: STR community posts (no paid ads) | **7** |
| #2 Jira reminders | Atlassian search ("reminder", "due date", "digest") | reminder, due date, overdue, digest | Free ≤10-user tier is standard | Yes, for Jira admins | Low | **8** |
| #3 monday utility | monday search + categories; community answers (Pioneera tactic) | Niche-specific | Trials mandatory | Yes | Low–medium | **6** |
| #4 Shopify digest | App Store search; first 10–50 installs need outreach (forum consensus) | "scheduled report", "daily sales email" | Yes | No (crowded) | Medium | **6** |

## §11. Time to first money (Task 11)

| Candidate | Build | Review | Listing | First install | First paid | First payout | Class |
|---|---|---|---|---|---|---|---|
| #1 Sheets sync | 2–3 weeks | OAuth verification days–weeks (if sensitive scopes) + Marketplace review (UNKNOWN) | 1–3 days | 1–3 weeks after listing | 3–8 weeks | Paddle payout cycle (~monthly; INFERENCE) | **MEDIUM (1–3 months)** |
| #2 Jira reminders | 2–3 weeks | Atlassian approval (UNKNOWN, typically weeks) | — | Weeks | 1–3 months (trial periods) | Monthly | MEDIUM |
| #3 monday utility | 2–3 weeks | App + pricing review (72 business hours for pricing) | — | Weeks | 1–2 months | Monthly | MEDIUM |
| #4 Shopify digest | 3 weeks | App review (weeks; one team reported 72 days, anecdote) | — | Weeks–months | 2–4 months | Monthly | SLOW |

## §12. Solo-operator fit (Task 12)

| Candidate | Dev | Support | Bug fixing | Onboarding | Billing | Marketplace updates | **Solo fit /10** |
|---|---|---|---|---|---|---|---|
| #1 Sheets sync | Easy | Low–medium (API-key setup help) | Low | Self-serve + video | Paddle handles it | Low | **8** |
| #2 Jira reminders | Easy–medium | Low | Low | Self-serve | Atlassian handles it | Medium (platform changes) | 8 |
| #3 monday utility | Easy–medium | Medium | Medium | Self-serve | monday handles it | Medium | 7 |
| #4 Shopify digest | Medium | Medium–high (merchants) | Medium | Self-serve | Shopify handles it | High (frequent API versions) | 6 |

## §13. Replication ethics / legality (Task 13)

- **May learn:** the workflow (source → sheet upsert + templates), pricing structures, problem framing, feature lists from public listings.
- **Must not copy:**
  - names ("Notion2Sheets", "ClickUp to Sheets" style trademarks);
  - listing text, screenshots, code, templates or proprietary datasets;
  - platform trademarks in our brand name (use only descriptively, e.g., "works with Hostaway", and only if the partner terms allow).
- **Patent risk:** none known for spreadsheet sync. LOW, but not searched (UNKNOWN).
- **ToS risk:** **never scrape Airbnb/Booking.** Use official PMS APIs only.

## §14. Scores, top 20 patterns (Task 14)

Weights: Proof 15 · Discovery 20 · MVP 15 · Recurring 15 · Competition survivability 10 · Solo fit 10 · Margin 5 · Platform risk (low = high score) 5 · Time to money 5.

| # | Pattern | Proof | Disc | MVP | Recur | Comp | Solo | Margin | Plat | Time | **Total** | Tech /10 | Distrib /10 | MRR pot /10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SaaS→Sheets sync (STR first) | 11 | 14 | 13 | 12 | 8 | 8 | 5 | 3 | 3 | **77→72** (−5 TAM override) | 9 | 7 | 5 |
| 2 | Jira reminders/digests (Forge) | 9 | 16 | 12 | 12 | 5 | 8 | 5 | 3 | 3 | **73→64** (−9 native-automation override) | 8 | 8 | 6 |
| 3 | monday utility (gap-scan) | 9 | 12 | 12 | 11 | 5 | 7 | 4 | 3 | 3 | **66→60** (−6 niche unknown) | 8 | 6 | 6 |
| 4 | Shopify scheduled digest | 12 | 12 | 12 | 12 | 2 | 6 | 4 | 3 | 2 | **65→57** (−8 saturation) | 7 | 6 | 6 |
| 5 | Shopify→Sheets orders | 9 | 12 | 13 | 11 | 5 | 8 | 4 | 3 | 3 | **68→55** (−13 low ceiling) | 9 | 6 | 3 |
| 6 | Workspace Forms→PDF | 10 | 14 | 9 | 11 | 2 | 6 | 4 | 2 | 2 | 60→53 | 6 | 7 | 5 |
| 7 | Confluence review reminders | 7 | 14 | 12 | 11 | 3 | 8 | 5 | 3 | 3 | 66→52 | 8 | 7 | 5 |
| 8 | Shopify backups | 12 | 12 | 4 | 13 | 5 | 4 | 4 | 3 | 1 | 58→48 | 3 | 6 | 6 |
| 9 | HubSpot dedupe | 12 | 10 | 8 | 11 | 2 | 5 | 4 | 2 | 1 | 55→45 | 5 | 5 | 6 |
| 10 | Shopify 404 monitor | 9 | 12 | 13 | 9 | 1 | 8 | 4 | 3 | 2 | 61→44 | 9 | 6 | 2 |
| 11 | monday item→PDF | 9 | 12 | 10 | 10 | 1 | 6 | 4 | 3 | 2 | 57→44 | 7 | 6 | 4 |
| 12 | Slack standup bot | 13 | 6 | 9 | 13 | 1 | 6 | 4 | 2 | 1 | 55→42 | 6 | 3 | 5 |
| 13 | Shopify tagging | 10 | 12 | 13 | 10 | 2 | 8 | 4 | 1 | 2 | 62→40 (native Flow) | 9 | 6 | 2 |
| 14 | Shopify low-stock alerts | 8 | 12 | 14 | 10 | 2 | 8 | 4 | 1 | 2 | 61→38 (native Flow) | 9 | 6 | 2 |
| 15 | Chrome paid utility | 6 | 4 | 13 | 8 | 3 | 8 | 4 | 2 | 3 | 51→40 | 9 | 2 | 3 |
| 16 | STR PMS native app (non-Sheets) | 6 | 8 | 10 | 12 | 7 | 7 | 4 | 2 | 2 | 58→52 (gated) | 7 | 5 | 4 |
| 17 | WordPress premium plugin | 10 | 12 | 9 | 10 | 2 | 4 | 4 | 4 | 2 | 57→46 | 6 | 6 | 5 |
| 18 | Wix app utility | 6 | 10 | 10 | 10 | 5 | 7 | 4 | 3 | 2 | 57→50 | 7 | 5 | 4 |
| 19 | Bubble plugin | 3 | 8 | 12 | 8 | 5 | 8 | 3 | 2 | 3 | 52→38 | 8 | 4 | 1 |
| 20 | Notion template | 6 | 10 | 14 | 3 | 3 | 9 | 4 | 3 | 4 | 56→40 (not SaaS) | 10 | 5 | 2 |

**Overrides explained:**
- **#1 loses 5** for niche TAM.
- **#2 loses 9** because Jira Automation can already send scheduled JQL emails (native-copy risk).
- **Several Shopify utilities lose heavily** for saturation or native Flow coverage.
- **Proof scores reflect visible evidence, not revenue.** Revenue is UNKNOWN for most apps.

## §15. Top 10 table (Task 15)

See §C.

## §16. Deep dives, top 5 (Task 16)

### 16.1 SaaS → Sheets live sync (STR first): the winner
- **Exact references:** Sync2Sheets/Notion2Sheets (Workspace; FR $5k–$8.4k MRR; 2-week MVP; acquisition via Marketplace search); ClickUp to Sheets (21K installs, $7–$32/mo, vendor-reported); Unito Spreadsheet Sync; Coupler.io (large horizontal).
- **Workflow:**
  1. Install from the Marketplace.
  2. The sidebar opens.
  3. Connect the source (API key/OAuth).
  4. Pick a template.
  5. The first sync writes tabs.
  6. Scheduled triggers keep the data current.
  7. Owner-report formulas update.
- **Why monthly:** live data. Value disappears if the sync stops.
- **Review evidence:** THEMES-ONLY. Users credit marketplace search and copy/images (FR); weak conversion is the main founder concern.
- **Competition:** no STR-PMS Sheets add-on found. Zapier templates exist (generic, DIY, paid Zapier plan).
- **Wedge:** vertical templates (owner statement, cleaning schedule, monthly performance) plus a no-Zapier setup.
- **MVP / features / not-to-build:** see §J.
- **Stack:** Apps Script, Paddle, optional Cloudflare Worker.
- **Approval:** Google OAuth consent + Marketplace listing review; PMS partner application if OAuth is required.
- **Monthly cost:** $0–$20.
- **Pricing:** $9 / $19 / $39.
- **First 20 customers:**
  - The operator's own STR network and existing community memberships (value posts, no DMs to strangers).
  - The PMS marketplace listing.
  - Workspace search.
- **Listing / screenshots:** see §I.
- **14/30-day plans:** see §K / §L.
- **Kill criteria:** see §M.

### 16.2 Jira reminder/digest (Forge)
- **References:** Reminder for Jira (Teamlead, 1,222 installs, paid via Atlassian), Simple Reminder (111), e-Reminders, Due Date Alerts (6).
- **Workflow:** a JQL or due-date rule → per-assignee digest (email/Slack) → snooze/acknowledge buttons → weekly manager summary.
- **Why monthly:** per-user licensing on the instance.
- **Competition:** MEDIUM. The leader is small (1,222 installs).
- **Wedge:** the "overdue + stale (no update in X days)" digest per person, with snooze. One digest instead of many notifications.
- **Native risk:** Jira Automation scheduled rules. **Kill if** interviews or community posts show admins are satisfied with Automation.
- **MVP:** Forge scheduled trigger + JQL + email/Slack webhook + admin settings page. 2–3 weeks.
- **Pricing:** standard Atlassian per-user tiers, free ≤10 users.
- **First 20:** Marketplace search + answering Atlassian Community questions (Pioneera-style community answering, used here in Atlassian's community).
- **Listing title:** "Overdue & Stale Issue Digest for Jira – Reminders That Don't Spam".
- **Validation:** count community threads asking for due-date reminders over 90 days. Kill if Jira Automation templates already solve the top asks.

### 16.3 monday.com utility (native billing)
- **References:** Pioneera (Same Item Multiple Boards, 4.9/98, 9.6K installs; portfolio $30K MRR per a vendor case study); the doc-gen apps (HIGH density, avoid).
- **Method:** pull apps-for-monday.com install-velocity data. Shortlist categories where the top app has under ~1,000 installs but rising monthly installs, and where community feature requests are unanswered (e.g., item-card print was requested but is now covered by apps, so avoid).
- **Build:** 2–3 weeks.
- **Billing:** native.
- **Kill if** no category shows unmet demand with at most 2 competitors.

### 16.4 Shopify scheduled KPI digest (research-only)
- **References:** Report Pundit, Better Reports, EZ Exporter, SyncWith, Data Export IO.
- **Possible wedge:** a tiny "daily sales digest to WhatsApp/Slack/email" for micro-stores at $5–$9, with zero configuration.
- **Problems:** HIGH competition; the price ceiling is low; the first installs need outreach (forum consensus).
- **Gate:** read 50 raw reviews of the leaders. Proceed only if "too complex/expensive for a small store" appears repeatedly.

### 16.5 Confluence content-review reminders (research-only)
- **References:** Midori Better Content Archiving (incumbent), Page Review Manager, Page Reminders, Outdated, Content Retention Manager, Breeze.
- **Real need:** Confluence has no native review expiry; community threads ask for this.
- **Wedge:** a "page owner + review cadence + one-click 'still accurate'" flow at small-team pricing.
- **Gate:** if Midori and Breeze already offer a cheap small-team tier, kill.

## §17. Marketplace comparison and ranking (Task 17)

| Rank | Marketplace | Easiest entry | Buyer intent | Fastest monetization | Approval difficulty | Competition | Recurring billing | Fit for this operator |
|---|---|---|---|---|---|---|---|---|
| 1 | **Google Workspace** | High | High (search) | Medium | Medium (OAuth; avoid restricted scopes) | Low–medium per niche | External (Paddle) | **Best**: Apps Script, Sheets skills, proven solo outcomes |
| 2 | **Atlassian** | Medium | **Very high** | Medium | Medium | Medium–high | Native, per-user | Strong: high ARPU, 0% fee to $1M |
| 3 | **monday.com** | Medium | Medium–high | Medium | Medium | Medium | **Native mandatory** | Strong: Israeli company, no payment friction |
| 4 | Shopify | Medium | **Very high** | Slow (outreach for first installs) | Medium–high | **Very high** | Native | Medium |
| 5 | Wix | Medium | Medium | Medium | Medium | Medium | Native (100% first year) | Medium |
| 6 | Hostaway / Hospitable / Guesty (niche) | Low (partner gating) | High (operators) | Medium | High (approval) | Low | External | **High domain fit**, small TAM |
| 7 | HubSpot | Medium | High | Slow | Medium (certification gates) | High | External | Low–medium |
| 8 | WordPress plugins | High | High (free) | Slow | Low | Very high | External (Freemius) | Medium (support-heavy) |
| 9 | Slack | Low (10-install gate) | Medium | Slow | High (10-week review) | High | External | Low |
| 10 | Zapier ecosystem | Medium | Medium | n/a (channel) | Medium | — | None | Channel only |
| 11 | Make ecosystem | Medium | Low–medium | n/a | Medium | — | None | Channel only |
| 12 | n8n ecosystem | High | Low (templates free) | n/a | Low | — | None | Channel only |
| 13 | Framer | High | Low–medium | Medium | Low | Low | Framer (100% to creator) | Low |
| 14 | Chrome Web Store | High ($5 fee, INFERENCE) | Low for paid | Slow | Low | Very high | None native | Low |
| 15 | Notion Marketplace | Low (waitlist) | Medium (templates) | Fast for templates | Medium | High | Templates only | Low (not SaaS) |
| 16 | Figma | Blocked (new paid sellers reportedly not approved) | Medium | — | High | High | Native 15% | Low |
| 17 | Bubble | High | Low | Slow | Low | Medium | Native 25% | Low |

---

## N. SOURCES / EVIDENCE APPENDIX

### Marketplace terms
- Shopify revenue share: [shopify.dev revenue share](https://shopify.dev/docs/apps/launch/distribution/revenue-share) · [App Store review](https://shopify.dev/docs/apps/launch/app-store-review) · app counts: [GapQuery](https://www.gapquery.com/shopify-app-store-statistics), [AppNavigator](https://appnavigator.io/statistics/), [RevenueHunt 2026](https://revenuehunt.com/state-of-the-shopify-app-economy/)
- Shopify first installs (anecdotes): [Shopify dev forum](https://community.shopify.dev/t/got-approved-3-weeks-ago-what-actually-worked-for-your-first-50-installs/37237) · [Shopify community](https://community.shopify.com/t/how-did-you-get-your-first-10-organic-app-installations-in-2026/643974?page=2) · [Indie Hackers (72-day approval)](https://www.indiehackers.com/post/we-got-our-shopify-app-approved-in-72-days-now-were-stuck-at-distribution-and-people-keep-offering-us-paid-reviews-df8505401d)
- Shopify Flow native: [MESA Flow templates](https://www.getmesa.com/blog/shopify-flow-templates) · [notify-me low stock native](https://notify-me.io/post/how-to-add-low-stock-alerts-on-shopify) · [Flow on plans](https://www.getservicify.com/post/which-shopify-plans-include-shopify-flow)
- Shopify no native scheduled reports: [Report Pundit guide](https://www.reportpundit.com/post/automate-shopify-reports) · [Shopify community thread](https://community.shopify.com/t/do-shopify-merchants-need-scheduled-weekly-or-monthly-sales-reports-by-email/580335)
- Atlassian: [revenue share docs](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/) · [2026 update](https://www.atlassian.com/blog/development/updates-to-marketplace-revenue-share-2026) · [Forge listing](https://developer.atlassian.com/platform/marketplace/listing-forge-apps/) · [Indie Hackers $4,149 MRR](https://www.indiehackers.com/post/reaching-4149-mrr-in-the-atlassian-marketplace-a3cc93a067)
- monday.com: [revenue share program](https://developer.monday.com/apps/changelog/announcing-the-revshare-program) · [Partner Program](https://developer.monday.com/apps/docs/partner-program) · [plans & pricing](https://developer.monday.com/apps/docs/plans-and-pricing) · [SEC filing (869 apps)](https://www.sec.gov/Archives/edgar/data/1845338/000117891326000870/zk2634436.htm) · [$30K MRR case](https://monday.com/appdeveloper/blog/build-30k-saas-monday-marketplace/) · [apps-for-monday directory](https://apps-for-monday.com/)
- Wix: [monetizing your app](https://dev.wix.com/docs/build-apps/launch-your-app/pricing-and-billing/about-monetizing-your-app) · [payments FAQ](https://dev.wix.com/docs/build-apps/launch-your-app/pricing-and-billing/payments-and-billing-faqs)
- Google Workspace: [get featured](https://developers.google.com/workspace/marketplace/get-featured) · [scopes](https://developers.google.com/workspace/add-ons/concepts/editor-scopes) · [OAuth verification](https://developers.google.com/apps-script/guides/client-verification) · [CASA cost (3rd-party)](https://bright-softwares.com/blog/en/google-workspace/the-50000-gmail-add-on-myth-what-google-s-casa-certification-really-costs)
- Slack: [guidelines](https://docs.slack.dev/slack-marketplace/slack-marketplace-app-guidelines-and-requirements/) · [install requirement 2026](https://docs.slack.dev/changelog/2026/09/01/slack-marketplace-install-requirement/) · [review guide](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide/)
- HubSpot: [certification requirements](https://developers.hubspot.com/docs/apps/developer-platform/list-apps/apply-for-certification/certification-requirements) · [May 2026 updates](https://developers.hubspot.com/changelog/app-listing-and-app-certification-requirement-updates-for-may-2026)
- Chrome: [payments deprecation](https://github.com/GoogleChrome/developer.chrome.com/blob/main/site/en/docs/webstore/cws-payments-deprecation/index.md) · [ExtensionPay](https://extensionpay.com/) · [TimeYourWeb $60 MRR](https://www.indiehackers.com/post/i-built-a-chrome-extension-in-2-weeks-10-years-later-20-000-users-10-paying-customers-60-mrr-YaK5THoaKqXgTlgBjHgO)
- Figma: [selling help](https://help.figma.com/hc/en-us/articles/12067637274519-About-selling-Community-resources) · [approval forum thread](https://forum.figma.com/ask-the-community-7/how-do-i-become-an-approved-seller-for-paid-plugins-56625)
- Notion: [selling on Marketplace](https://www.notion.com/help/selling-on-marketplace)
- Bubble: [marketplace policies](https://manual.bubble.io/account-and-marketplace/marketplace-policies) · [forum pricing thread](https://forum.bubble.io/t/plugin-pricing-model/23827?page=2)
- Framer: [creator program](https://www.framer.com/help/articles/how-the-creator-program-works/)
- Freemius: [WordPress pricing](https://freemius.com/wordpress/pricing/)
- n8n templates: [goodspeed](https://goodspeed.studio/blog/n8n-templates) · [community proposal](https://community.n8n.io/t/empowering-template-creators-a-game-changing-affiliate-program-proposal/35277?tl=en)
- Hostaway: [marketplace](https://www.hostaway.com/marketplace/) · [marketplace FAQ](https://support.hostaway.com/hc/en-us/articles/4406922627611-Hostaway-Marketplace-Your-Gateway-to-Powerful-Integrations) · [public API](https://api.hostaway.com/documentation) · [API keys](https://support.hostaway.com/hc/en-us/articles/360002576293-Hostaway-Public-API-Account-Secret-Key)
- Hospitable: [become an integration partner](https://help.hospitable.com/en/articles/16234154-how-can-i-become-an-integration-partner-with-hospitable-com-and-list-my-integration) · [PAT (not for third parties)](https://help.hospitable.com/en/articles/8609392-accessing-the-public-api-with-a-personal-access-token-pat) · [core integration (18k subscribers)](https://hospitable.com/hospitable-core-integration) · [exports](https://help.hospitable.com/en/articles/5625450-getting-started-with-exports) · [Zapier Hospitable↔Sheets](https://zapier.com/apps/google-sheets/integrations/hospitable) · [Zapier Hostaway↔Sheets](https://zapier.com/apps/google-sheets/integrations/hostaway)
- Guesty: [marketplace overview](https://help.guesty.com/hc/en-gb/articles/9371171208733-Marketplace-overview)
- Billing from Israel: [Stripe in Israel / Paddle](https://adircpa.com/en/guides/stripe-israel-tax)

### Products
- Shopify:
  - [Matrixify reviews](https://apps.shopify.com/excel-export-import/reviews)
  - [Sufio](https://apps.shopify.com/sufio?)
  - [EZ Exporter reviews](https://apps.shopify.com/ez-exporter/reviews?page=2)
  - [Ablestar](https://apps.shopify.com/bulk-product-editor)
  - [syncX Stock Sync](https://apps.shopify.com/stock-sync/reviews)
  - [Tible Stock sync](https://apps.shopify.com/multi-store-stock-sync)
  - [Simprosys](https://apps.shopify.com/google-shopping-feed)
  - [SC Easy Redirects](https://apps.shopify.com/easyredirects?page=3)
  - [SEOFlow](https://apps.shopify.com/easy-404-redirects)
  - [Rewind](https://apps.shopify.com/backup)
  - [Talon](https://apps.shopify.com/backup-1)
  - [Omega Auto Tag](https://apps.shopify.com/order-tagger-by-omega)
  - [EE Tagging](https://apps.shopify.com/order-auto-tagger)
  - [Shopaw](https://apps.shopify.com/order-tagger)
  - [HKT Auto Tag](https://apps.shopify.com/hkt-auto-tag)
  - [LSA Low Stock](https://apps.shopify.com/low-stock-alert)
  - [MB Low Stock](https://apps.shopify.com/low-stock-alert-1)
  - [iAlert](https://apps.shopify.com/low-stock-notifier)
  - [OSync](https://apps.shopify.com/osync-export-orders-to-sheets)
  - [Exportsy](https://apps.shopify.com/exportsi-google-sheets-orders)
  - [eCommix](https://apps.shopify.com/ecommix-google-sheets-sync)
  - [GoSheet](https://apps.shopify.com/go-sheets-export-orders)
  - [Exportly](https://apps.shopify.com/exportly-google-sheets-sync)
  - [WEBI](https://apps.shopify.com/ordersheet-auto-order-sync)
  - [Report Pundit](https://apps.shopify.com/report-pundit)
  - [Better Reports](https://apps.shopify.com/betterreports)
  - [SyncWith reports](https://apps.shopify.com/simple-reports-and-data-export)
- Workspace:
  - [Form Publisher](https://workspace.google.com/marketplace/app/form_publisher/827172627657) · [pricing](https://form-publisher.com/pricing/)
  - [Document Studio](https://workspace.google.com/marketplace/app/document_studio/429444628321)
  - [Email Notifications for Forms](https://workspace.google.com/marketplace/app/email_notifications_for_google_forms/984866591130)
  - [Sync2Sheets listing](https://workspace.google.com/marketplace/app/sync2sheets_notion_a_sheets_en_tiempo_re/887187948180?hl=ar) · [Founder Club $5k MRR](https://www.founderclub.com/notion2sheets/) · [IndieHustle $8.4k](https://www.indiehustle.co/p/a-micro-saas-for-notion-making-8400) · [Latka est.](https://getlatka.com/companies/notion2sheets#customers)
  - [ClickUp to Sheets](https://workspace.google.com/marketplace/app/clickup_to_sheets/359672242762) · [vendor site](https://clickuptosheets.com/)
  - [Unito Spreadsheet Sync](https://workspace.google.com/marketplace/app/unito_spreadsheet_sync/548272798607)
  - [BudgetSheet $1.6k MRR](https://vancelucas.com/blog/how-i-built-a-google-sheets-extension-making-1-6k-mrr/)
- Atlassian:
  - [Timepiece](https://marketplace.atlassian.com/apps/1211756/timepiece-time-in-status-for-jira)
  - [SaaSJet Time in Status](https://marketplace.atlassian.com/apps/1219732/time-in-status)
  - [Better Excel Exporter pricing](https://www.midori-global.com/products/better-excel-exporter-for-jira/cloud/buy)
  - [JXL](https://jxl.app/)
  - [Reminder for Jira (Teamlead)](https://marketplace.atlassian.com/apps/1217030/reminder-for-jira-follow-ups-deadlines-notifications)
  - [Simple Reminder](https://marketplace.atlassian.com/apps/1232417/simple-reminder-email-notifications)
  - [Due Date Alerts](https://marketplace.atlassian.com/apps/4284872603/due-date-alerts)
  - [e-Reminders](https://marketplace.atlassian.com/apps/1211430/e-reminders-add-on-for-jira?tab=overview&hosting=cloud)
  - [Page Review Manager](https://marketplace.atlassian.com/apps/2847619197/page-review-manager-for-confluence)
  - [Page Reminders](https://marketplace.atlassian.com/apps/1221018/page-reminders-for-confluence)
  - [Better Content Archiving](https://marketplace.atlassian.com/apps/123/better-content-archiving-and-analytics-for-confluence)
  - [Confluence review community thread](https://community.atlassian.com/forums/Confluence-questions/Document-Review-Reminder/qaq-p/2906433)
- monday:
  - [DocExport](https://www.docexport.com/)
  - [Board Print to PDF](https://apps-for-monday.com/apps/10000465/)
  - [DocCreate](https://community.monday.com/t/new-app-introducing-doccreate-the-most-powerful-automated-document-creation-app-on-monday-com/114180)
  - [The PDF Maker](https://community.monday.com/monday-pulse/post/we-built-the-pdf-maker-a-document-generation-and-esignature-app-that-DkJbemXu5FgNVQz)
  - [DocuGen](https://monday.com/marketplace/listing/12/docugen)
  - [GetSign](https://getsign.io/how-tos/generate-quotes-and-invoices-on-monday-com/)
  - [native Quotes & Invoices](https://support.monday.com/hc/en-us/articles/21050405375762-The-new-Quotes-Invoices)
  - [item→PDF feature request](https://community.monday.com/t/export-an-item-to-pdf/62664)
  - [dashboard PDF scheduling](https://support.monday.com/hc/en-us/articles/26237863849490-Share-and-present-your-Dashboard)
  - [Apify scraper sample (DocExport)](https://apify.com/needy_hammock/monday-marketplace-scraper)
- HubSpot: [Insycle](https://ecosystem.hubspot.com/marketplace/apps/insycle?eco_tools=SALES_CONTACT_MANAGEMENT) · [Dedupely](https://ecosystem.hubspot.com/marketplace/listing/dedupely)
- Slack: [Geekbot pricing](https://help.geekbot.com/en/articles/4280827-how-much-does-geekbot-cost)
