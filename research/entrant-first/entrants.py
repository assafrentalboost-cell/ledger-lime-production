"""Entrant filter + dedupe. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.
CLEAN      : shop<=24mo, shop lifetime sales<=15,000, 12-mo units>=100, active>=8/12, last-3-month units>0, not PLR/resell
NEAR-CLEAN : same but active<8 because the listing is young: active >= 0.7*min(listing_age,12) and last-3 > 0
Contribution: listing 12-mo units / shop lifetime sales >= 0.05 (product matters to the shop)
Dedupe: by listing_id across queries; entrant = shop (best listing kept, siblings listed)."""
import json,glob,os,re
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'raw')
def num(s):
    s=str(s).replace('$','').replace(',','').replace(' Mo.','').strip()
    try: return float(s)
    except: return 0.0
PLR=re.compile(r'\b(plr|mrr|resell|master resell|private label)\b',re.I)
L={}
for f in sorted(glob.glob(os.path.join(D,'Q-*.json'))):
    d=json.load(open(f)); q=d['params'].get('title_include') or 'broad'
    for r in d['rows']:
        x=L.setdefault(r['listing_id'],dict(r,queries=[]))
        if q not in x['queries']: x['queries'].append(q)
def classify(r):
    t=r.get('trends') or [0]*12; act=sum(1 for v in t if v>0); last3=sum(t[-3:])
    sa,tx,u,la=num(r['shop_age_month']),num(r['transaction_sold_count']),num(r['est_mo_sales']),num(r['listing_age_in_months'])
    contrib=u/tx if tx else 0
    reasons=[]
    if sa>24: reasons.append('shop>24mo')
    if tx>15000: reasons.append('shop>15k sales')
    if u<100: reasons.append('<100 units')
    if last3<=0: reasons.append('no sales last 3 mo')
    if PLR.search(r['title']) or re.search(r'plr|mrr', r['shop_name'], re.I): reasons.append('PLR/resell')
    if contrib<0.05: reasons.append('listing <5% of shop sales')
    if reasons: return 'REJECT',act,last3,contrib,reasons
    if act>=8: return 'CLEAN',act,last3,contrib,[]
    if act>=0.7*min(la,12) and la<12: return 'NEAR-CLEAN',act,last3,contrib,['young listing']
    return 'REJECT',act,last3,contrib,[f'active {act}/12']
rows=[]
for lid,r in L.items():
    c,act,last3,contrib,why=classify(r)
    rows.append(dict(listing_id=lid,shop=r['shop_name'],shop_age=r['shop_age_month'],shop_sales=r['transaction_sold_count'],title=r['title'],listing_age=r['listing_age_in_months'],price=r['price'],units=r['est_mo_sales'],revenue=r.get('est_mo_revenue',''),trend=r.get('trends'),last3=(r.get('trends') or [0]*12)[-3:],active=act,contrib=round(contrib,3),category=r.get('main_category',''),queries=r['queries'],status=c,why=why))
if __name__=='__main__':
    json.dump(rows,open(os.path.join(os.path.dirname(D),'all_listings_classified.json'),'w'),indent=1)
    from collections import Counter
    print(Counter(x['status'] for x in rows), 'listings', len(rows))
    ok=[x for x in rows if x['status']!='REJECT']
    print('shops passing', len({x['shop'] for x in ok}))
