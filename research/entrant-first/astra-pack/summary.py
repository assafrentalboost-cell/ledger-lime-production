"""Gate summary + same-buyer job depth. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.

ENTRANT-BACKED CLUSTER (Step 4), all must hold, no weights:
  G1 clean_shops >= 2            (independent shops with a CLEAN listing)
  G2 top_shop_share < 0.60       (one shop does not explain the cluster)
  G3 fit != EXCLUDED             (IP / legal / fraud)
FINALIST ELIGIBILITY (Steps 9, 1): G1-G3 + clean_shops >= 3 + fit in STRONG/MEDIUM + not a LIVE product family.
Overlays (buyer spanning several job clusters) are evaluated with the same gates. ADHD_ADULT fit = STRONG for the money/admin
jobs, MEDIUM for cleaning/planner jobs; it touches live #6 (ADHD Budget) through ONE door, so it is not excluded as LIVE.
PROVISIONAL choice, lexicographic (no weights): (1) fit STRONG/MEDIUM, (2) young-pool sell-through young_ge30 (clone_check.json),
(3) fewer young-pool duplicate pairs, (4) clean_shops.

SAME-BUYER DEPTH: a job counts when >= 2 distinct shops sell it (entrant overlay rows + young pool rows with >= 30 units)."""
import json, os, re, glob
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__))
def num(s):
    s = str(s).replace('$', '').replace(',', '').replace(' Mo.', '').strip()
    try: return float(s)
    except: return 0.0

ADHD_JOBS = [  # first match wins
 ('Bills, budget & paycheck', r'budget|bill|paycheck|money|savings|debt|finance'),
 ('Cleaning & chore system', r'clean|chore|declutter|housework|zone'),
 ('Brain dump / task paralysis / prioritising', r'brain dump|brain reset|task paralysis|thought organi|priority|eisenhower|to.do'),
 ('Life OS / second brain (all-in-one)', r'second brain|life (system|planner|management|os)|all.in.one|command center'),
 ('12-month task & deadline calendar', r'task calendar|12.month|deadline|appointment'),
 ('Habits, goals & routines', r'habit|goal|routine|workbook'),
 ('Daily / weekly planner', r'daily|weekly|planner'),
 ('Symptom & medication log', r'symptom|medication'),
 ('Reading tracker (hobby)', r'reading|book tracker|series tracker'),
]
ADHD_JOBS = [(j, re.compile(rx, re.I)) for j, rx in ADHD_JOBS]
KID = re.compile(r'kids?|toddler|child|classroom|student|teacher|visual schedule|png|clip ?art|stl|worksheet|therapy|therapist', re.I)
ADHD = re.compile(r'adhd|neurodivergent|executive (dys)?function', re.I)

def adhd_depth():
    rows = [dict(shop=r[1], price=r[2], units=r[3], src='entrant', title=r[6]) for r in json.load(open(os.path.join(H, 'overlay_adhd.json')))['rows']]
    for f in glob.glob(os.path.join(H, 'raw', 'F-adhd-p1-*.json')):
        for r in json.load(open(f))['rows']:
            if num(r['est_mo_sales']) >= 30 and ADHD.search(r['title']) and not KID.search(r['title']):
                rows.append(dict(shop=r['shop_name'], price=r['price'], units=r['est_mo_sales'], src='young<=3mo', title=r['title']))
    J = defaultdict(list)
    for r in rows:
        if KID.search(r['title']): continue
        for j, rx in ADHD_JOBS:
            if rx.search(r['title']): J[j].append(r); break
    out = {}
    for j, _ in ADHD_JOBS:
        L = J.get(j, []); shops = sorted({r['shop'] for r in L})
        out[j] = dict(shops=len(shops), units=int(sum(num(r['units']) for r in L)), counted=len(shops) >= 2,
                      examples=[(r['shop'], r['price'], r['units'], r['src'], r['title'][:70]) for r in sorted(L, key=lambda r: -num(r['units']))[:4]])
    return out

if __name__ == '__main__':
    C = json.load(open(os.path.join(H, 'clusters.json')))['clusters']
    O = json.load(open(os.path.join(H, 'overlay_adhd.json')))
    K = json.load(open(os.path.join(H, 'clone_check.json')))
    backed = {k: v for k, v in C.items() if v['clean_shops'] >= 2 and v['top_shop_share'] < 0.6 and v['fit'] != 'EXCLUDED' and k != 'OTHER'}
    print('ENTRANT-BACKED JOB CLUSTERS (G1-G3):', len(backed), sorted(backed))
    print('ADHD_ADULT overlay passes G1-G3:', O['clean_shops'] >= 2 and O['top_shop_share'] < 0.6)
    elig = {k: v for k, v in backed.items() if v['clean_shops'] >= 3 and v['fit'] in ('STRONG', 'MEDIUM') and not v['prior'].startswith('LIVE')}
    print('FINALIST-ELIGIBLE job clusters:', sorted(elig))
    yg = {'WEDDING_PLAN_ADMIN': K['WEDDING_PLAN_ADMIN']['young_pool']['young_ge30'], 'ADHD_ADULT': K['ADHD_ADULT (overlay)']['young_pool']['young_ge30'],
          'DIET_CONDITION': K['DIET_CONDITION']['young_pool']['young_ge30']}
    print('young-pool listings (<=3 mo) with >=30 units, top-100 pool:', yg)
    d = adhd_depth(); json.dump(d, open(os.path.join(H, 'adhd_depth.json'), 'w'), indent=1)
    print('\nADHD same-buyer jobs (>=2 shops):', sum(1 for v in d.values() if v['counted']))
    for j, v in d.items():
        print(f"  [{'x' if v['counted'] else ' '}] {j}: shops={v['shops']} units={v['units']}")
        for e in v['examples']: print('       ', e)
    cand = {'ADHD_ADULT': ('STRONG/MEDIUM', K['ADHD_ADULT (overlay)']['young_pool'], O['clean_shops']),
            'WEDDING_PLAN_ADMIN': ('STRONG', K['WEDDING_PLAN_ADMIN']['young_pool'], C['WEDDING_PLAN_ADMIN']['clean_shops']),
            'DIET_CONDITION': ('WEAK', K['DIET_CONDITION']['young_pool'], C['DIET_CONDITION']['clean_shops'])}
    order = sorted(cand, key=lambda k: (cand[k][0] == 'WEAK', -cand[k][1]['young_ge30'], cand[k][1]['young_dup_pairs'], -cand[k][2]))
    print('\nTOP 3 ORDER:', order)
    for k in order: print(f"  {k}: fit={cand[k][0]} young_ge30={cand[k][1]['young_ge30']} young_dup_pairs={cand[k][1]['young_dup_pairs']} clean_shops={cand[k][2]}")
    print('PROVISIONAL =', order[0])
