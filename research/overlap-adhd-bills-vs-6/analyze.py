"""Bills-vs-#6 overlap numbers. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA. usage: python3 -I analyze.py"""
import json, os, statistics
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, 'raw')
n = lambda s: float(str(s).replace('$', '').replace(',', '').replace(' Mo.', '') or 0)
A = json.load(open(os.path.join(R, 'F-adhd-bill-p1-3d9a6b.json')))['rows']
G = json.load(open(os.path.join(R, 'F-bill-tracker-p1-f03140.json')))['rows']
print(f"ADHD-titled bill listings: {len(A)} | with >=10 units/12mo: {sum(n(r['est_mo_sales'])>=10 for r in A)} | max units: {max(n(r['est_mo_sales']) for r in A):.0f} | total units: {sum(n(r['est_mo_sales']) for r in A):.0f}")
print(f"  of which <=6 mo old: {sum(n(r['listing_age_in_months'])<=6 for r in A)}")
U = [n(r['est_mo_sales']) for r in G]; P = [n(r['price']) for r in G]
w = sum(u*p for u, p in zip(U, P)) / sum(U)
print(f"Generic 'bill tracker' listings (>=30 units/12mo): {len(G)} | units {sum(U):.0f} | median price ${statistics.median(P):.2f} | unit-weighted price ${w:.2f} | share of units < $5: {sum(u for u,p in zip(U,P) if p<5)/sum(U):.0%} | >= $10: {sum(u for u,p in zip(U,P) if p>=10)/sum(U):.0%}")
young = [r for r in G if n(r['shop_age_month']) <= 24 and n(r['est_mo_sales']) >= 100]
print('Young-shop (<=24mo) generic bill sellers >=100 units:', [(r['shop_name'], r['price'], r['est_mo_sales']) for r in young])
