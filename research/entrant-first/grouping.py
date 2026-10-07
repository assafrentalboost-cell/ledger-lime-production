"""Buyer/job grouping of entrant listings. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.

Input : all_listings_classified.json (from entrants.py)
Output: clusters.json + printed table

Rules
- Every passing listing (CLEAN / NEAR-CLEAN) gets the FIRST cluster whose regex matches its title (order matters,
  more specific jobs first). Unmatched -> OTHER.
- Clusters are defined by BUYER + REAL-LIFE JOB, not by file format.
- Entrant = shop. A shop counts once per cluster (best listing = most units). Cluster stats:
    clean_shops      distinct shops with >=1 CLEAN listing in the cluster
    near_shops       distinct shops with only NEAR-CLEAN listings in the cluster
    units            sum of 12-mo units over passing listings
    top_shop_share   units of the largest shop / cluster units
    price_median/q3  over passing listings (listing-level, unweighted), list price as shown
    premium_sustained listings priced >= $20 with CLEAN status (active >= 8/12)
- fit / prior are fixed labels (not scores) taken from the L&L brief and the repo's research history.
No weighted score is computed. Ranking in the report uses explicit gates (see GATES below)."""
import json, os, re, statistics
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__))

def num(s):
    s = str(s).replace('$', '').replace(',', '').replace(' Mo.', '').strip()
    try: return float(s)
    except: return 0.0

# (cluster, buyer / job, regex) — first match wins
RULES = [
 ('IP_RISK', 'fan merch (trademark)', r'pok[eé]mon|pok[eé]dex|pokedex|\bpkmn\b|ms rachel|toy story|lightning mcqueen|\bcars\b (birthday|party)|frozen|sonic|winnie|pooh|elmo|disney|bluey|barbie'),
 ('REJECT_RISK', 'fraud / legal / service', r"doctor'?s? (note|excuse)|excuse note|power of attorney|\bpoa\b|rental agreement|lease|tenan|roommate|waiver|contract|car buyer report|vin report|vin check"),
 ('CO_PARENTING', 'separated parent: custody documentation', r'co-?parent|custody|visitation|parenting time'),
 ('WEDDING_PLAN_ADMIN', 'engaged couple: plan/budget/run the wedding',
  r'wedding.*(planner|planning|budget|spreadsheet|binder|checklist|timeline|guest list|vendor|itinerary|day.of|blueprint|organizer|tracker)|(planner|budget|binder|checklist|timeline|guest list|itinerary|questionnaire).*(wedding|bridal|bride|bachelorette|bridesmaid)|bachelorette.*itinerary|bridesmaid.*questionnaire|day.of.coordinator'),
 ('DESIGN_ASSETS', 'designer/maker: digital design assets', r'\bstl\b|3d print|laser cut|\bsvg\b|preset|\bluts?\b|mockup|clipart|\bpng\b|wall art|\bposters?\b|portrait|overlay|embroidery (design|font)|\bdxf\b'),
 ('WEDDING_DECOR', 'engaged couple: invitations/signs/websites', r'wedding|bridal|bride|save.the.date|rsvp|bachelorette|bridesmaid|engagement'),
 ('PERSONAL_BUDGET', 'household: budget/debt/savings', r'budget|debt|savings|sinking fund|paycheck|bill tracker|finance|financial|income (and|&) expense|net worth|expense tracker|money'),
 ('VEHICLE_PRIVATE_SALE', 'private car seller/buyer: sale paperwork', r'bill of sale|vehicle (checklist|inspection|maintenance|log|record|purchase|sale)|car (sale|inspection|maintenance|buying)|used car|auto (repair|sale)'),
 ('STR_HOST', 'short-term rental host', r'airbnb|vacation rental|welcome book|house manual|guest guide|\bhost\b|superhost|vrbo'),
 ('NEW_PARENT_ORG', 'expecting / new parent: plan & track baby care', r'birth plan|first foods|baby.*(log|tracker|feeding|milestone|schedule|sleep|checklist)|newborn.*(log|tracker|checklist|schedule)|feeding (log|tracker|schedule)|pregnancy (planner|tracker|journal|checklist)|hospital bag|baby led weaning|blw'),
 ('BABY_SHOWER_DECOR', 'baby shower host: games/invites', r'baby shower|gender reveal|pregnancy announcement|baby announcement|sprinkle'),
 ('CAREGIVER_HEALTH', 'family/agency caregiver: care records', r'caregiver|care plan|medication|\bmar\b|medical (binder|record|log|history|organizer|tracker)|health (tracker|log|binder|record)|symptom|blood (pressure|sugar)|home care|client assessment'),
 ('PET_RECORDS', 'pet owner/sitter: pet care records', r'pet (health|record|care|sitter|sitting|vaccin|medical|binder|planner)|dog (health|vaccin|record|care|walk)|vet (record|visit)|puppy (schedule|record|checklist)'),
 ('CLEANING_HOME', 'household: cleaning/chores/declutter', r'cleaning|chore|declutter|home organi|house ?keeping|laundry'),
 ('DIET_CONDITION', 'newly diagnosed / diet-change eater: what to eat', r'(food (list|chart|guide)|diet|meal plan|grocery).*?(diabet|fodmap|ibs|keto|low carb|glp|ozempic|gallbladder|gallstone|liver|mediterranean|heart healthy|cholesterol|protein|anti.inflammatory|diverticul|kidney|renal|gout|pcos|celiac|gluten)|(diabet|fodmap|ibs|keto|low carb|glp|gallbladder|liver|mediterranean|heart healthy|diverticul|kidney|renal|gout|pcos|celiac|anti.inflammatory|prediabet).*?(food|diet|meal|grocery|eating)|allergy card'),
 ('MEAL_PLANNING', 'household cook: meal plan & grocery', r'meal (plan|planner|prep)|grocery|menu planner|pantry|recipe (binder|book|card|organizer|cost)'),
 ('TRAVEL_PLANNING', 'traveler: trip itinerary/budget/packing', r'travel|trip|itinerary|packing list|vacation planner'),
 ('HOMESCHOOL_ADMIN', 'homeschool parent: records/planning', r'homeschool.*(planner|transcript|record|diploma|attendance|report card|portfolio|tracker)|(transcript|diploma).*homeschool'),
 ('TEACHER_ADMIN', 'teacher: classroom admin', r'teacher.*(planner|binder|gradebook|grade book|lesson plan|sub plan|substitute|log|tracker|organizer)|lesson plan|gradebook|sub plans?|classroom management|parent.teacher|iep'),
 ('SMALL_BIZ_ADMIN', 'small business / seller: money & clients', r'invoice|crm|client (tracker|intake|database|management)|p&l|profit|bookkeep|small business|reseller|inventory|sales tracker|order tracker|pricing calculator|cost calculator|receipt|mileage'),
 ('CREATOR_MARKETING', 'service business: flyers/logos/social', r'flyer|logo|instagram|social media|canva template for|business card|price list|booking|n8n|mockup'),
 ('LIFE_PLANNER', 'individual: life/productivity planner', r'notion|life planner|digital planner|adhd planner|goodnotes|bullet journal|planner bundle|daily planner|habit|journal'),
 ('HOBBY_TRACKER', 'hobbyist: reading/collection trackers', r'reading|book tracker|tbr|thread (chart|tracker)|dmc|collection tracker'),
 ('CRAFT_PATTERNS', 'maker: craft patterns', r'crochet|knit|sewing|pattern|quilt|embroider|cross stitch|amigurumi|woodworking|svg|cricut|sublimation|procreate|brush'),
 ('KIDS_EDU_CONTENT', 'parent/teacher: kids learning content', r'worksheet|preschool|curriculum|tracing|coloring|activit|flash ?card|phonics|montessori|bible|sunday school|lesson'),
 ('PARTY_GIFT_DECOR', 'gift/party/decor buyer', r'invitation|invite|birthday|party|wall art|print|poster|sticker|clipart|png|font|ticket|magazine|gift|card|sign|template'),
]
RULES = [(c, b, re.compile(rx, re.I)) for c, b, rx in RULES]

FIT = {  # L&L = practical financial / administrative organization for real-life situations
 'WEDDING_PLAN_ADMIN': 'STRONG', 'CO_PARENTING': 'STRONG', 'PERSONAL_BUDGET': 'STRONG', 'VEHICLE_PRIVATE_SALE': 'STRONG',
 'STR_HOST': 'MEDIUM', 'NEW_PARENT_ORG': 'MEDIUM', 'CAREGIVER_HEALTH': 'STRONG', 'PET_RECORDS': 'MEDIUM', 'CLEANING_HOME': 'MEDIUM',
 'MEAL_PLANNING': 'MEDIUM', 'TRAVEL_PLANNING': 'MEDIUM', 'HOMESCHOOL_ADMIN': 'STRONG', 'TEACHER_ADMIN': 'MEDIUM', 'SMALL_BIZ_ADMIN': 'STRONG',
 'LIFE_PLANNER': 'WEAK', 'HOBBY_TRACKER': 'WEAK', 'CRAFT_PATTERNS': 'WEAK', 'KIDS_EDU_CONTENT': 'WEAK', 'PARTY_GIFT_DECOR': 'WEAK',
 'WEDDING_DECOR': 'WEAK', 'BABY_SHOWER_DECOR': 'WEAK', 'CREATOR_MARKETING': 'WEAK', 'IP_RISK': 'EXCLUDED', 'REJECT_RISK': 'EXCLUDED', 'OTHER': 'WEAK'}
PRIOR = {  # repo research history (research/product-19, department-1, department-2)
 'CO_PARENTING': 'LIVE PRODUCT #17 (not new)', 'PERSONAL_BUDGET': 'LIVE CORE (#1,#3-#7; not new)',
 'WEDDING_PLAN_ADMIN': 'explored: #9 V2 HOLD', 'CAREGIVER_HEALTH': 'explored: #11/#16 live-adjacent',
 'SMALL_BIZ_ADMIN': 'explored: bookkeeping/invoice rejected, #14 inventory', 'TRAVEL_PLANNING': 'screened & dropped (Discovery 2.0)',
 'HOMESCHOOL_ADMIN': 'screened & dropped (Discovery 2.0)', 'HOBBY_TRACKER': 'book tracker dropped', 'STR_HOST': 'Dept #1 alternative',
 'CLEANING_HOME': 'Dept #1 household (failed)', 'VEHICLE_PRIVATE_SALE': 'Dept #1 data reused (not a finalist)'}

# per-cluster exclusions: a title matching the exclusion falls through to later rules
EXCLUDE = {'WEDDING_PLAN_ADMIN': re.compile(r'newspaper|magazine|invitation|invite|\bsigns?\b|website|program', re.I)}

def assign(title):
    for c, b, rx in RULES:
        if rx.search(title) and not (c in EXCLUDE and EXCLUDE[c].search(title)): return c, b
    return 'OTHER', 'unclassified'

def q(vals, p):
    v = sorted(vals)
    if not v: return 0
    k = (len(v) - 1) * p; f = int(k); c = min(f + 1, len(v) - 1)
    return round(v[f] + (v[c] - v[f]) * (k - f), 2)

def build():
    rows = json.load(open(os.path.join(H, 'all_listings_classified.json')))
    ok = [r for r in rows if r['status'] != 'REJECT']
    C = defaultdict(list)
    for r in ok:
        c, b = assign(r['title']); r['cluster'] = c; r['buyer_job'] = b; C[c].append(r)
    out = {}
    for c, L in C.items():
        shops = defaultdict(list)
        for r in L: shops[r['shop']].append(r)
        clean = {s for s, rs in shops.items() if any(x['status'] == 'CLEAN' for x in rs)}
        near = set(shops) - clean
        units = sum(num(r['units']) for r in L)
        shop_units = {s: sum(num(x['units']) for x in rs) for s, rs in shops.items()}
        top = max(shop_units, key=shop_units.get)
        prices = [num(r['price']) for r in L]
        prem = [r for r in L if num(r['price']) >= 20 and r['status'] == 'CLEAN']
        out[c] = dict(cluster=c, buyer_job=L[0]['buyer_job'], fit=FIT.get(c, 'WEAK'), prior=PRIOR.get(c, 'new'),
                      listings=len(L), clean_shops=len(clean), near_shops=len(near), units=int(units),
                      top_shop=top, top_shop_share=round(shop_units[top] / units, 3) if units else 0,
                      price_median=q(prices, .5), price_q3=q(prices, .75), price_max=max(prices),
                      premium_sustained=[(r['shop'], r['price'], r['units'], r['active']) for r in prem],
                      shops=sorted(((s, int(u)) for s, u in shop_units.items()), key=lambda x: -x[1]))
    json.dump(dict(clusters=out, listings=ok), open(os.path.join(H, 'clusters.json'), 'w'), indent=1)
    return out

# GATES (Step 4 of the brief) — pass/fail, no weights
def gates(k):
    return dict(two_clean_shops=k['clean_shops'] >= 2, three_clean_shops=k['clean_shops'] >= 3,
                not_one_shop=k['top_shop_share'] < 0.6, fit_ok=k['fit'] in ('STRONG', 'MEDIUM'),
                not_excluded=k['fit'] != 'EXCLUDED')

# BUYER OVERLAYS: a buyer can span several job clusters. Overlay = regex on title, reported with its job mix.
OVERLAYS = {'ADHD_ADULT': (re.compile(r'adhd|neurodivergent|executive (dys)?function', re.I),
                           re.compile(r'kids?|toddler|child|classroom|student|teacher|visual schedule|png|clip ?art|\bstl\b|fidget', re.I))}

def overlay(name):
    inc, exc = OVERLAYS[name]
    d = json.load(open(os.path.join(H, 'clusters.json')))
    L = [r for r in d['listings'] if inc.search(r['title']) and not exc.search(r['title'])]
    shops = defaultdict(list)
    for r in L: shops[r['shop']].append(r)
    clean = {s for s, rs in shops.items() if any(x['status'] == 'CLEAN' for x in rs)}
    units = sum(num(r['units']) for r in L)
    jobs = defaultdict(lambda: [0, set()])
    for r in L: jobs[r['cluster']][0] += num(r['units']); jobs[r['cluster']][1].add(r['shop'])
    su = {s: sum(num(x['units']) for x in rs) for s, rs in shops.items()}; top = max(su, key=su.get)
    prices = [num(r['price']) for r in L]
    return dict(overlay=name, listings=len(L), clean_shops=len(clean), near_shops=len(set(shops) - clean), units=int(units),
                top_shop=top, top_shop_share=round(su[top] / units, 3), price_median=q(prices, .5), price_q3=q(prices, .75),
                jobs={k: dict(units=int(v[0]), shops=sorted(v[1])) for k, v in jobs.items()},
                rows=[(r['status'], r['shop'], r['price'], r['units'], r['active'], r['cluster'], r['title'][:90]) for r in sorted(L, key=lambda r: -num(r['units']))])

if __name__ == '__main__':
    out = build()
    print(f"{'cluster':22} {'fit':8} {'cln':>3} {'nr':>3} {'lst':>4} {'units':>7} {'top%':>5} {'med$':>6} {'q3$':>6} {'prem':>4}  prior")
    for k in sorted(out.values(), key=lambda k: (-k['clean_shops'], -k['units'])):
        print(f"{k['cluster']:22} {k['fit']:8} {k['clean_shops']:>3} {k['near_shops']:>3} {k['listings']:>4} {k['units']:>7} {k['top_shop_share']*100:>4.0f}% {k['price_median']:>6} {k['price_q3']:>6} {len(k['premium_sustained']):>4}  {k['prior']}")
    o = overlay('ADHD_ADULT'); json.dump(o, open(os.path.join(H, 'overlay_adhd.json'), 'w'), indent=1)
    print('\nOVERLAY ADHD_ADULT', {k: v for k, v in o.items() if k not in ('rows', 'jobs')})
    for k, v in sorted(o['jobs'].items(), key=lambda x: -x[1]['units']): print(f"  {k:20} units={v['units']:>6} shops={len(v['shops'])}")
    for r in o['rows']: print('  ', *r)
