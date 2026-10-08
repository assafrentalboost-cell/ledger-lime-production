"""V2 entrant filter + dedupe + health class. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.

Inputs : raw/Q-*.json (V2 entrant pulls) + raw/V1-Q-*.json (V1 entrant pulls, copied unchanged).
         Every Q pull used the same filters: download, shop_age<=24 mo, shop sales<=15,000, 12-mo units>=100, sorted by units.
Dedupe : by listing_id across all pulls; the queries that surfaced a listing are kept.

STATUS (same rules as V1):
  CLEAN      shop<=24 mo; shop sales<=15,000; units>=100; active>=8/12; last-3-month units>0; not PLR/MRR/resell (title or shop);
             listing units / shop lifetime sales >= 0.05
  NEAR-CLEAN all of the above except active<8, because the listing is young: listing age<12 and active>=0.7*min(age,12)
  REJECT     anything else (reason kept in `why`)

HEALTH (Stage 7), applied to every listing with units>=100:
  ACTIVE    CLEAN or NEAR-CLEAN, and last-3-month units >= 15% of 12-month units (i.e. not fading)
  FADING    CLEAN or NEAR-CLEAN, but last-3-month units < 15% of 12-month units
  HISTORIC  last-3-month units == 0 (sold in the year, not now)
  OTHER     failed for another reason (old/large shop, PLR, low contribution, too few active months)"""
import json, glob, os, re
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
def num(s):
    s = str(s).replace('$', '').replace(',', '').replace(' Mo.', '').strip()
    try: return float(s)
    except: return 0.0
PLR = re.compile(r'\b(plr|mrr|resell|master resell|private label)\b', re.I)

def load():
    L = {}
    for f in sorted(glob.glob(os.path.join(H, 'raw', 'Q-*.json')) + glob.glob(os.path.join(H, 'raw', 'V1-Q-*.json'))):
        d = json.load(open(f)); q = ('v1:' if 'V1-' in f else '') + (d['params'].get('title_include') or 'broad').strip()
        for r in d['rows']:
            x = L.setdefault(r['listing_id'], dict(r, queries=[]))
            if q not in x['queries']: x['queries'].append(q)
    return L

def classify(r):
    t = r.get('trends') or [0] * 12; act = sum(1 for v in t if v > 0); last3 = sum(t[-3:])
    sa, tx, u, la = num(r['shop_age_month']), num(r['transaction_sold_count']), num(r['est_mo_sales']), num(r['listing_age_in_months'])
    contrib = u / tx if tx else 0
    why = []
    if sa > 24: why.append('shop>24mo')
    if tx > 15000: why.append('shop>15k sales')
    if u < 100: why.append('<100 units')
    if last3 <= 0: why.append('no sales last 3 mo')
    if PLR.search(r['title']) or re.search(r'plr|mrr', r['shop_name'], re.I): why.append('PLR/resell')
    if contrib < 0.05: why.append('listing <5% of shop sales')
    if why: status = 'REJECT'
    elif act >= 8: status = 'CLEAN'
    elif act >= 0.7 * min(la, 12) and la < 12: status, why = 'NEAR-CLEAN', ['young listing']
    else: status, why = 'REJECT', [f'active {act}/12']
    if status != 'REJECT': health = 'ACTIVE' if last3 >= 0.15 * u else 'FADING'
    elif last3 <= 0: health = 'HISTORIC'
    else: health = 'OTHER'
    return status, health, act, last3, contrib, why

def build():
    rows = []
    for lid, r in load().items():
        s, h, act, last3, contrib, why = classify(r)
        t = r.get('trends') or [0] * 12
        rows.append(dict(listing_id=lid, shop=r['shop_name'], shop_age=num(r['shop_age_month']), shop_sales=num(r['transaction_sold_count']),
                         title=r['title'], listing_age=num(r['listing_age_in_months']), price=num(r['price']), units=num(r['est_mo_sales']),
                         revenue=r.get('est_mo_revenue', ''), trend=t, last3=t[-3:], active=act, contrib=round(contrib, 3),
                         queries=r['queries'], status=s, health=h, why=why))
    return rows

if __name__ == '__main__':
    rows = build()
    json.dump(rows, open(os.path.join(H, 'all_listings_classified.json'), 'w'), indent=1)
    ok = [x for x in rows if x['status'] != 'REJECT']
    print('listings', len(rows), Counter(x['status'] for x in rows), Counter(x['health'] for x in rows))
    print('shops passing (CLEAN or NEAR-CLEAN):', len({x['shop'] for x in ok}), '| CLEAN shops:', len({x['shop'] for x in rows if x['status'] == 'CLEAN'}))
    print('pulls:', len(glob.glob(os.path.join(H, 'raw', 'Q-*.json'))), 'V2 +', len(glob.glob(os.path.join(H, 'raw', 'V1-Q-*.json'))), 'V1')
