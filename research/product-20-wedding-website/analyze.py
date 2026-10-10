"""Product #20 wedding-website gate numbers. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.
Reads raw/F-wedding-website-*.json (last_12_months, >=100 units). Writes COMPETITORS.csv. usage: python3 -I analyze.py"""
import csv, glob, json, os, statistics
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__)); L = 'EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA'
n = lambda s: float(str(s).replace('$', '').replace(',', '').replace(' Mo.', '').replace('—', '0') or 0)
rows = json.load(open(glob.glob(os.path.join(H, 'raw', 'F-wedding-website-*.json'))[0]))['rows']
# keep couple-facing wedding websites; drop photographer Showit sites and seating-chart QR sites (different job)
def job(t):
    t = t.lower()
    if 'showit' in t or 'photographer' in t: return 'OTHER (photographer site)'
    if 'seating' in t: return 'ADJACENT (seating-chart site)'
    if 'save the date' in t and 'website' in t: return 'WEDDING WEBSITE (save-the-date variant)'
    return 'WEDDING WEBSITE'
out = []
for r in rows:
    t = r['trends']; u = n(r['est_mo_sales']); sa = n(r['shop_age_month']); ss = n(r['transaction_sold_count'])
    out.append(dict(data_label=L, listing_id=r['listing_id'], shop=r['shop_name'], job=job(r['title']), price=n(r['price']), est_12mo_units=u,
                    last3=sum(t[-3:]), first9=sum(t[:9]), trend=' '.join(map(str, t)), active_months=sum(x > 0 for x in t), reviews=n(r['est_reviews']),
                    listing_age=n(r['listing_age_in_months']), shop_age=sa, shop_sales=ss, young_shop=sa <= 24, rsvp='rsvp' in r['title'].lower(),
                    invitation='invitation' in r['title'].lower() or 'invite' in r['title'].lower(), title=r['title']))
with open(os.path.join(H, 'COMPETITORS.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
W = [o for o in out if o['job'].startswith('WEDDING WEBSITE')]
U = sum(o['est_12mo_units'] for o in W)
print(f"wedding-website listings >=100 units: {len(W)} | units {U:.0f} | shops {len({o['shop'] for o in W})}")
print(f"price median ${statistics.median(o['price'] for o in W):.2f} | unit-weighted ${sum(o['price']*o['est_12mo_units'] for o in W)/U:.2f}")
for lo, hi in ((0, 10), (10, 20), (20, 30), (30, 40), (40, 1e9)):
    print(f"  ${lo}-{hi if hi<1e9 else '+'}: {sum(o['est_12mo_units'] for o in W if lo<=o['price']<hi)/U:.0%} of units")
y = [o for o in W if o['young_shop']]
print(f"young shops (<=24 mo): {len({o['shop'] for o in y})}/{len({o['shop'] for o in W})} shops, {sum(o['est_12mo_units'] for o in y)/U:.0%} of units")
print(f"listings <=6 mo old: {sum(o['listing_age']<=6 for o in W)} | with RSVP in title: {sum(o['rsvp'] for o in W)} | 'invitation' in title: {sum(o['invitation'] for o in W)}")
S = defaultdict(lambda: [0, 0, 0, 0, 0])
for o in W: s = S[o['shop']]; s[0] += o['est_12mo_units']; s[1] += 1; s[2] = o['shop_age']; s[3] = o['shop_sales']; s[4] += o['last3']
print('shop | listings | units | last3 | shop_age | shop_sales')
for k, v in sorted(S.items(), key=lambda x: -x[1][0]): print(f"  {k:22} {v[1]:>2} {v[0]:>6.0f} {v[4]:>5.0f} {v[2]:>4.0f} {v[3]:>7.0f}")
top = sorted(S.items(), key=lambda x: -x[1][0]); print(f"top shop share {top[0][1][0]/U:.0%}, top-3 {sum(v[0] for _, v in top[:3])/U:.0%}")
