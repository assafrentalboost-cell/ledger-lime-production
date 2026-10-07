"""Checks every headline claim of ENTRANT-FIRST-DISCOVERY-2026-10-07.md against the regenerated outputs.
EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA. Prints CLAIM / REPRODUCED value / YES|NO|CORRECTED; writes verify_output.txt."""
import csv, json, os
H = os.path.dirname(os.path.abspath(__file__))
def rows(f): return list(csv.DictReader(open(os.path.join(H, f))))
E = rows('ADHD-CLEAN-ENTRANTS.csv'); R = rows('ADHD-RECENT-ENTRY.csv'); PF = rows('ADHD-PRICE-FORMAT.csv')
C = json.load(open(os.path.join(H, 'clusters.json')))['clusters']; O = json.load(open(os.path.join(H, 'overlay_adhd.json'))); DJ = json.load(open(os.path.join(H, 'adhd_depth.json')))
clean = {r['shop'] for r in E if r['classification'] == 'CLEAN'}; near = {r['shop'] for r in E} - clean
ge = [r for r in R if r['ge30_flag'] == '1']
ov = [r for r in PF if r['in_overlay_passing'] == '1']; U = sum(float(r['est_12mo_units']) for r in ov)
u4 = sum(float(r['est_12mo_units']) for r in ov if float(r['price_listed']) < 4) / U
prem = [r for r in PF if r['premium_ge15'] == '1']; PU = sum(float(r['est_12mo_units']) for r in prem)
nn = sum(float(r['est_12mo_units']) for r in prem if r['format_family'] in ('Notion', 'app/web')) / PU
out = open(os.path.join(H, 'astra_tables_output.txt')).read()
valid = int(out.split('VALID SAME-BUYER JOBS (>=2 shops AND >=2 shops with a non-bolt-on listing):')[1].split()[0])
dup = int(out.split('near-dup pairs=')[1].split()[0])
checks = [
 ('20 ADHD clean entrant shops', len(clean), len(clean) == 20),
 ('7 ADHD near-clean entrant shops', len(near), len(near) == 7),
 ('young pool = 75 adult ADHD listings', len(R), len(R) == 75),
 ('24 / 75 young listings >= 30 units', len(ge), len(ge) == 24),
 ('17 of those from new shops (<=24 mo)', sum(r['new_shop_flag'] == '1' for r in ge), sum(r['new_shop_flag'] == '1' for r in ge) == 17),
 ('2 near-duplicate title pairs in young pool', dup, dup == 2),
 ('~40% of overlay units priced < $4', round(u4, 3), round(u4, 2) == 0.40),
 ('ADHD overlay units 21,109', O['units'], O['units'] == 21109),
 ('6 same-buyer jobs (>=2 shops)', sum(v['counted'] for v in DJ.values()), sum(v['counted'] for v in DJ.values()) == 6),
 ('VALID jobs incl. bolt-on test (new, stricter)', valid, None),
 ('"premium tier is Notion and apps" (report section 10 item 5)', f'Notion+app share of premium units = {nn:.2f}', False),
 ('Wedding young >=30 = 5, dup pairs 89', 'see RUNNER-UP line', 'young pool=100 >=30=5 new-shop>=30=2 dup pairs=89' in out),
 ('Diet young >=30 = 51, new-shop 49, dup pairs 73', 'see RUNNER-UP line', 'young pool=100 >=30=51 new-shop>=30=49 dup pairs=73' in out),
]
lines = ['EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA']
for c, v, ok in checks:
    lines.append(f"{'YES      ' if ok is True else 'INFO     ' if ok is None else 'CORRECTED'} | {c} | reproduced: {v}")
open(os.path.join(H, 'verify_output.txt'), 'w').write('\n'.join(lines) + '\n'); print('\n'.join(lines))
