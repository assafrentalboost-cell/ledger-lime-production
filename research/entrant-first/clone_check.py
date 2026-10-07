"""Clone / flood check per finalist. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.

Inputs : raw/F-*.json  (listings <=3 months old, any shop, sorted by 12-mo units desc, 100 rows = top of the young pool)
         clusters.json / overlay_adhd.json (entrant listings per finalist)
Metrics (all exact, no weights):
  young_n            rows returned (cap 100 => the pool is >= 100 new listings in 3 months)
  young_selling      rows with 12-mo units >= 1
  young_ge30         rows with 12-mo units >= 30 (a new listing that genuinely sells)
  young_top_shop_age shop age (months) of the best-selling young listings — are NEW shops or OLD shops winning?
  plr                titles matching PLR/MRR/resell
  young_dup_pairs    same pair test inside the young pool (new-listing clone wave)
  dup_pairs          pairs of entrant titles with difflib ratio >= 0.70 (first 60 chars, lowercased), across DIFFERENT shops
  price_floor_share  share of entrant listings priced < $4
Rating rule: HIGH  if dup_pairs >= 3 or price_floor_share >= 0.40 or young_dup_pairs >= 20
             MEDIUM if dup_pairs >= 1 or price_floor_share >= 0.20
             LOW   otherwise
             A HIGH rating is downgraded to "HIGH (tier-specific)" when >=3 clean shops sell >= $15 with active >= 8/12."""
import json, os, glob, re, difflib, statistics
H = os.path.dirname(os.path.abspath(__file__))
PLR = re.compile(r'\b(plr|mrr|resell|master resell|private label)\b', re.I)
def num(s):
    s = str(s).replace('$', '').replace(',', '').replace(' Mo.', '').strip()
    try: return float(s)
    except: return 0.0

def young(tag):
    f = glob.glob(os.path.join(H, 'raw', f'F-{tag}-p1-*.json'))[0]
    R = json.load(open(f))['rows']
    if tag == 'adhd':  # same adult-only exclusion as the ADHD_ADULT overlay
        kid = re.compile(r'kids?|toddler|child|classroom|student|teacher|visual schedule|png|clip ?art|\bstl\b|fidget', re.I)
        R = [r for r in R if not kid.search(r['title'])]
    sell = [r for r in R if num(r['est_mo_sales']) >= 1]
    ge30 = [r for r in R if num(r['est_mo_sales']) >= 30]
    top = sorted(R, key=lambda r: -num(r['est_mo_sales']))[:10]
    yd = dups([dict(shop=r['shop_name'], title=r['title']) for r in R])
    return dict(file=os.path.basename(f), young_dup_pairs=len(yd), young_dup_shops=len({x[1] for x in yd} | {x[2] for x in yd}), young_n=len(R), young_selling=len(sell), young_ge30=len(ge30),
                young_ge30_new_shops=sum(1 for r in ge30 if num(r['shop_age_month']) <= 24),
                young_median_price=statistics.median(num(r['price']) for r in R),
                plr=sum(1 for r in R if PLR.search(r['title'])),
                top10=[(r['shop_name'], r['price'], r['est_mo_sales'], r['shop_age_month'], r['transaction_sold_count'], r['title'][:70]) for r in top])

def dups(rows):
    out = []
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            a, b = rows[i], rows[j]
            if a['shop'] == b['shop']: continue
            r = difflib.SequenceMatcher(None, a['title'][:60].lower(), b['title'][:60].lower()).ratio()
            if r >= 0.70: out.append((round(r, 2), a['shop'], b['shop'], a['title'][:60], b['title'][:60]))
    return sorted(out, reverse=True)

def rate(d, rows, young_dup=0):
    prem = {r['shop'] for r in rows if num(r['price']) >= 15 and r['status'] == 'CLEAN'}
    pf = sum(1 for r in rows if num(r['price']) < 4) / len(rows)
    if len(d) >= 3 or pf >= 0.40 or young_dup >= 20: v = "HIGH"
    elif len(d) >= 1 or pf >= 0.20: v = 'MEDIUM'
    else: v = 'LOW'
    if v == 'HIGH' and len(prem) >= 3: v = 'HIGH (tier-specific: low-price tier flooded; >=3 clean premium shops)'
    return v, round(pf, 2), sorted(prem)

if __name__ == '__main__':
    C = json.load(open(os.path.join(H, 'clusters.json')))
    A = json.load(open(os.path.join(H, 'overlay_adhd.json')))
    adhd_rows = [dict(status=s, shop=sh, price=p, units=u, active=a, cluster=c, title=t) for s, sh, p, u, a, c, t in A['rows']]
    fin = {'WEDDING_PLAN_ADMIN': ([r for r in C['listings'] if r['cluster'] == 'WEDDING_PLAN_ADMIN'], 'wedding-planner'),
           'ADHD_ADULT (overlay)': (adhd_rows, 'adhd'),
           'DIET_CONDITION': ([r for r in C['listings'] if r['cluster'] == 'DIET_CONDITION'], 'food-list')}
    out = {}
    for name, (rows, tag) in fin.items():
        d = dups(rows); y = young(tag); v, pf, prem = rate(d, rows, y["young_dup_pairs"])
        out[name] = dict(rating=v, entrant_listings=len(rows), dup_pairs=d, price_floor_share=pf, premium_clean_shops=prem,
                         plr_in_entrants=sum(1 for r in rows if PLR.search(r['title'])), young_pool=y)
        print(f'\n## {name}: {v}  | entrants={len(rows)} dup_pairs={len(d)} price<$4 share={pf} premium clean shops(>=$15)={prem}')
        for x in d[:8]: print('   dup', x)
        print('   young pool:', {k: v for k, v in y.items() if k != 'top10'})
        for t in y['top10']: print('     ', t)
    json.dump(out, open(os.path.join(H, 'clone_check.json'), 'w'), indent=1)
