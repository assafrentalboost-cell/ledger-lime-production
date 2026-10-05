# PRODUCT #19 — CLAUDE BUILD HANDOFF

**Budget Mensuel & Annuel — Reste à Vivre** (French Monthly & Annual Budget Planner)

- Gate: `PRODUCT-19-FINAL-GATE.md` (BUILD, controlled portfolio experiment).
- Factory sequence: Build → QA → visuals/video → Etsy **draft** only after the gate §10 check → final pre-live audit → Assaf publish decision. No publish, Ads or spend without Assaf.

---

## 1. Product definition

- **Buyer:** French-speaking household (France, Belgium, Switzerland, Québec, …) that wants to manage its monthly budget in a spreadsheet.
- **Trigger:** start of the month or the year (pay day, New Year, "this month I'm getting control of my budget").
- **Job:** see what is left to live on after fixed charges and savings, then follow monthly spending against envelopes, and get the year in review without retyping anything.
- **Hero promise (2–3 seconds):** « Votre **reste à vivre**, calculé automatiquement. » (Your "left to live on", calculated automatically.)
- **Why preferable:**
  - **vs Etsy competitors:** a native French product built around *reste à vivre* (no competitor uses the term), with envelopes and an automatic annual review.
  - **vs a free template or AI:** correct French formats, protected formulas, 12 months pre-wired, Quick Start in French.
  - **vs L&L #1–#7:** a different language and search door. No English duplicate.

## 2. Architecture

Six visible tabs plus one hidden. All visible UI is in French: tab names, headers, instructions, statuses, chart titles.

| # | Tab | Purpose |
|---|---|---|
| 1 | **Démarrer** | 4 setup steps; year (input); currency symbol (list: €, CHF, $ CA); first month of the budget year (default janvier) |
| 2 | **Catégories** | Planned monthly amounts per category in 4 blocks: Revenus (≤8), Charges fixes (≤15), Enveloppes / dépenses variables (≤15), Épargne programmée (≤8) |
| 3 | **Journal** | Every transaction: Date, Libellé, Catégorie (dropdown from Catégories), Type (auto), Montant, Moyen de paiement (list), Note. 1,000 rows |
| 4 | **Tableau mensuel** | Month selector (dropdown of 12 French month names). KPIs, envelope table, planned vs actual |
| 5 | **Bilan annuel** | 12-month grid by category (actuals), totals, savings rate, 2 charts |
| 6 | **Mode d'emploi** | In-sheet guide (French), FAQ, formats note |
| — | **Listes** (hidden) | Month names FR, payment methods, types, status labels, currency list |

## 3. Core formulas and automation

**Month window.** On *Tableau mensuel*, the selected month name maps to a month index via MATCH against Listes!MoisFR. Then:
- `Début = DATE(Année; IndexMois; 1)`
- `Fin = EOMONTH(Début; 0)`

Do **not** derive month names with TEXT(date;"mmmm"). It is locale-dependent; always use the Listes lookup.

**Type.** Journal *Type* = lookup of the category's block (Revenu / Charge fixe / Enveloppe / Épargne) from Catégories. It is not typed by the user.

**Actuals per category:** `SUMIFS(Journal!Montant; Journal!Catégorie; cat; Journal!Date; ">="&Début; Journal!Date; "<="&Fin)`. Amounts are entered as positive numbers; the type decides the sign in the KPIs.

**KPIs (Tableau mensuel):**
- **Revenus du mois** = Σ actual revenue (falls back to planned revenue when no revenue is entered yet; label shows « prévu »).
- **Charges fixes** = Σ max(planned, actual) per fixed charge. A planned rent still counts before it is paid.
- **Épargne programmée** = Σ planned savings.
- **Reste à vivre** = Revenus − Charges fixes − Épargne programmée.
- **Dépenses variables** = Σ actual envelope spending.
- **Reste à dépenser** = Reste à vivre − Dépenses variables.
- **Taux d'épargne** = Σ actual savings ÷ Revenus (blank if Revenus = 0).

**Envelope status** (per envelope, ratio = actual ÷ planned):
- **OK** if ratio ≤ 0.8
- **Attention** if 0.8 < ratio ≤ 1
- **Dépassé** if ratio > 1
- **—** if planned = 0 and actual = 0
- **Non prévu** if planned = 0 and actual > 0

**Banner:** if Reste à dépenser < 0 → red « Budget dépassé de X ». Otherwise green « Il vous reste X pour ce mois ».

**Bilan annuel:** the same SUMIFS per category × 12 month windows; row and column totals; annual savings rate. Charts: (1) Revenus vs Dépenses by month (columns); (2) spending by category (bar).

## 4. Inputs and outputs

- **Inputs:** Démarrer (year, currency, start month); Catégories (names and planned amounts); Journal rows.
- **Outputs:** the Tableau mensuel KPIs, envelope statuses and banner; the Bilan annuel grid and charts.

## 5. Formats (critical)

- Dates: `dd/mm/yyyy`.
- Currency format uses the symbol from Démarrer through three pre-built number formats chosen by conditional formatting, or a symbol column. Keep it simple: one selected symbol displayed in a header cell, with amounts in `# ##0,00` (French grouping in a fr_FR locale).
- **Google Sheets master:** spreadsheet locale **France (fr_FR)**, time zone Europe/Paris. Formulas are written with English function names through the API; Sheets localizes the display (`;` separators, `SOMME.SI.ENS`). Verify that the decimal comma renders and that typed input `12,50` parses as a number.
- **Excel (.xlsx, openpyxl):** store formulas with English function names and comma separators (Excel's internal format). French Excel displays them localized automatically. Number format `#,##0.00`; it shows as `1 234,56` on French-locale machines. Date format `dd/mm/yyyy`.
- Test on a French-locale Excel if available; otherwise verify with LibreOffice at locale fr-FR.

## 6. Sample data (realistic, France, one household)

- Year 2026; currency €.
- **Revenus:** Salaire A 2 150 €, Salaire B 1 680 €, CAF 140 €.
- **Charges fixes:** Loyer 950 €, Électricité/Gaz 95 €, Assurance habitation 22 €, Assurance auto 58 €, Internet + mobiles 55 €, Mutuelle 64 €, Abonnement transport 86 €, Crédit auto 210 €.
- **Épargne programmée:** Livret A 200 €, Vacances 100 €.
- **Enveloppes:** Courses 560 €, Carburant 140 €, Loisirs 120 €, Restaurants 90 €, Enfants 150 €, Santé 40 €, Cadeaux 50 €, Divers 60 €.
- **Journal:** ~140 rows across 3 months (janvier–mars).
- **Required visible states:** in mars, *Courses* = Attention (≈ 92%) and *Restaurants* = Dépassé (≈ 118%). Résultat: Reste à vivre ≈ 2 130 € and Reste à dépenser positive. All hero and video numbers must come from the real recalculated file.

## 7. Protection

- Warning-only protection on formula columns and KPI cells. No password locks (L&L reviews punish them).
- No macros or Apps Script.
- Input cells styled light, formula cells tinted.

## 8. QA matrix

| Area | Test | Pass |
|---|---|---|
| Month window | Transactions on 01/03, 31/03, 01/04 | 31/03 counted in mars; 01/04 not |
| Leap year | Year 2028, février | 29/02 included |
| Start month | Budget year starting septembre | Bilan columns ordered sept → août; month windows correct across the year boundary |
| KPIs | Zero revenue | Taux d'épargne blank; no #DIV/0! |
| Charges fixes | Planned 950, actual 0 | Counts 950; after paying 950 still 950; paying 980 → 980 |
| Envelopes | Ratio exactly 0.8 / 1.0 | OK / Attention |
| Envelopes | Planned 0, actual 25 | « Non prévu » |
| Banner | Reste à dépenser −1 | Red, « dépassé de 1,00 » |
| Categories | Rename a category | Journal dropdown and all sums follow (reference by cell, not hard-coded text) |
| Journal | Blank rows inside the data; 1,000th row | No errors; sums include row 1,000 |
| Locale | Type `12,50` in Sheets fr_FR | Numeric 12.5 |
| Parity | Excel vs Sheets | Identical KPIs and Bilan totals |
| Sheets visual | Headers | No mid-word wrapping (P16 lesson) |
| Copy | Make-a-Copy | Protection survives; 0 errors |
| Print | Tableau mensuel | One A4 page, portrait |

**Adversarial tests:** text in the Montant column; negative amount entered; date typed as text (`03/15/2026`, US order); category deleted from Catégories while still used in Journal (must surface « Catégorie inconnue », not silently drop); 3 currencies switched mid-year (display only; no conversion claimed); future-dated transactions (counted only in their own month).

## 9. Quick Start (French PDF, 2 pages)

1. Faire une copie (Sheets) or open the .xlsx (Excel).
2. Onglet Démarrer: year, currency, first month.
3. Onglet Catégories: replace the example amounts.
4. Onglet Journal: add your transactions; choose the month in Tableau mensuel.

Also include a « Formats » box (dates jj/mm/aaaa, virgule décimale) and FAQ: deleting the example data, adding a category, a second year (« Fichier → Faire une copie »).

## 10. Creative plan

- **Hero (L2 before/after, real UI only, 3000×2250):** the Tableau mensuel. Left: *Reste à dépenser 412,00 €*, Restaurants « Attention ». Right, after one Journal line « Restaurant — 48,00 € »: *364,00 €*, Restaurants « Dépassé ». Single accent on the status flip.
- **Carousel (French copy):**
  1. Hero
  2. « Ce que vous recevez » (6 tabs)
  3. Reste à vivre explained
  4. Enveloppes
  5. Bilan annuel charts
  6. Google Sheets + Excel
  7. Quick Start
  8. FAQ
- **Real-action video (10–15 s, video engine, real Sheets capture):**
  1. Select « mars » → the KPIs load.
  2. Type a Journal line « Courses — 64,30 € » → *Courses* moves to Attention.
  3. Cut to Tableau mensuel: Reste à dépenser drops by 64,30 €.
  4. End card: Bilan annuel chart.

## 11. Listing direction

- **Title** (135 characters, no "&"; final lead depends on gate §10): Budget Mensuel et Annuel Google Sheets Excel, Tableau Budget Français, Reste à Vivre, Suivi Dépenses, Planificateur Budgétaire, Épargne
- **Tags** (13, all ≤ 20 characters): budget mensuel, tableau budget, budget français, planificateur budget, budget familial, suivi dépenses, budget annuel, budget excel, budget google sheets, gestion budget, reste à vivre, épargne, enveloppes budget
- **Description:** French first, with a short English line ("French-language budget planner") for English searchers.
- **Price:** ₪49 (≈ $13). No discount without Assaf.

## 12. Disclaimers (French)

« Outil d'organisation budgétaire personnel. Ne constitue pas un conseil financier, fiscal ou bancaire. Aucune connexion bancaire : vos données restent dans votre propre fichier. »

(Personal budgeting tool. Not financial, tax or banking advice. No bank connection: your data stays in your own file.)

## 13. Exact exclusions

- No debt payoff module (that is #2) or couples split (#7).
- No bank import, CSV automation or Apps Script.
- No tax, CAF or impôts calculations.
- No currency conversion.
- No multi-year engine in V1. A new year means a new copy.
- No English UI toggle in V1.

## 14. Known commercial uncertainties

1. Official French search volume (gate §10, pre-draft).
2. French review evidence (blocked).
3. The category leader is reactivating after a July–September pause.
4. French support load.
5. Etsy translation mechanics for an English-language shop.
6. Durable price evidence tops out around $14. ₪49 is deliberate.
