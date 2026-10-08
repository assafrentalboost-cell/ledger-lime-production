"""ADHD Goal & Restart Planner — competitor table + second-entrant test. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.
Reads raw/*.json (EverBee pulls captured 2026-10-08, last_12_months window, so est_mo_sales = 12-month units).
Annotations (format / mechanism / hero / ADHD class) are read from the TITLE ONLY — listing pages and reviews returned 403,
so page count, complaints and the real mechanism are UNVERIFIED unless the title states them.
Entrant rule (same as research/entrant-first): CLEAN = shop <=24 mo, shop sales <=15k, >=100 units, active >=8/12 mo,
last-3 units >0, listing >=5% of shop sales. NEAR-CLEAN = CLEAN except active <8 because listing age <12 mo.
WEAK = sells on the job but fails CLEAN on size/age/consistency. NONE = <100 units.
usage: python3 -I competitors.py"""
import csv, glob, json, os
H = os.path.dirname(os.path.abspath(__file__))
L = 'EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA'

# listing_id: (format, mechanism, hero claim, ADHD class, restart/low-energy element in title?)
# ADHD class: NATIVE = job framed around ADHD friction (anti-shame / start-anytime / low-energy / reset);
# ADAPTED = generic planner structure with ADHD positioning; BOLT-ON = ADHD only as a keyword in a generic title.
EXACT = {
 '4440940588': ('Fillable A4 PDF', 'Undated goal workbook; life audit + energy audit (tags)', 'Start Anytime', 'NATIVE', 'YES (start anytime / anti-shame)'),
 '4474225910': ('PDF', 'Goal setting planner + focus/productivity tracker', 'Shame-Free', 'NATIVE', 'PARTIAL (shame-free)'),
 '4495991824': ('Printable PDF', 'Goal setting planner + tracker', 'ADHD Goal Setting Planner', 'ADAPTED', 'NO'),
 '1807870237': ('Printable', 'Weekly goal planner, new-year goals, goal review', 'New Year Life Goals', 'BOLT-ON', 'NO'),
 '4538664912': ('Excel', 'Life system: habits, goals, time lab', 'ADHD Life System', 'ADAPTED', 'NO'),
 '4372860145': ('Notion', 'Gamified RPG life OS: habits, goals, rewards', 'Gamified RPG', 'ADAPTED', 'NO'),
 '1331622566': ('Digital planner (tablet)', 'Dated planner + goal & habit tracker', 'ADHD Digital Planner', 'ADAPTED', 'NO'),
 '1751200137': ('Printable PDF', 'Gamified goal quest', 'ADHD Productivity Quest', 'ADAPTED', 'NO'),
 '4338845135': ('Fillable PDF', 'Executive-function workbook bundle (multi-topic)', 'Neuro-Affirming Tools', 'NATIVE', 'NO'),
 '4333479096': ('PDF workbook', 'Life systems: prep, flow, follow-through', 'Building Life Systems', 'NATIVE', 'PARTIAL (follow-through)'),
 '4525115768': ('Printable PDF', 'ADHD planner + executive-function worksheets', 'ADHD Workbook for Teens Adults', 'ADAPTED', 'NO'),
 '4399348526': ('Printable PDF', 'Brain dump, task tracker, time blocking bundle', 'ADHD Brain Reset', 'ADAPTED', 'PARTIAL (reset = brain dump)'),
 '4523178000': ('Printable PDF', 'Mental declutter workbook + life organizer', 'ADHD Reset Planner', 'NATIVE', 'PARTIAL (overwhelm reset)'),
 '4521017598': ('Printable PDF', 'Low-energy / burnout day planner', 'ADHD Low Energy Planner', 'NATIVE', 'YES (low-energy)'),
 '4519215685': ('PDF', 'Shutdown / burnout recovery worksheet', 'ADHD Shutdown Recovery', 'NATIVE', 'YES (low-energy reset)'),
}
# Substitutes: generic/bundle planners that win the same search door at scale
BENCH = {
 '1782173723': ('Printable PDF', 'All-in-one ADHD planner pages', 'Adhd Planner Adult', 'BOLT-ON', 'NO'),
 '1344352293': ('Printable bundle', 'Ultimate life planner bundle', 'Ultimate Life planner', 'BOLT-ON', 'NO'),
}
num = lambda s: float(str(s).replace('$', '').replace(',', '').replace(' Mo.', '').replace('—', 'nan') or 'nan')

def rows():
    seen = {}
    for f in sorted(glob.glob(os.path.join(H, 'raw', 'F-*.json'))):
        for r in json.load(open(f))['rows']:
            seen.setdefault(r['listing_id'], r)
    return seen

def status(r):
    u, sa, ss, la = num(r['est_mo_sales']), num(r['shop_age_month']), num(r['transaction_sold_count']), num(r['listing_age_in_months'])
    t = r['trends']; act = sum(1 for x in t if x > 0); last3 = sum(t[-3:])
    contrib = u / ss if ss else 0
    if u < 100: return 'NONE', act, contrib
    base = sa <= 24 and ss <= 15000 and last3 > 0 and contrib >= 0.05
    if base and act >= 8: return 'CLEAN', act, contrib
    if base and la < 12: return 'NEAR-CLEAN', act, contrib
    return 'WEAK', act, contrib

if __name__ == '__main__':
    R = rows(); out = []
    for group, M in (('EXACT', EXACT), ('SUBSTITUTE', BENCH)):
        for lid, (fmt, mech, hero, cls, restart) in M.items():
            r = R[lid]; st, act, c = status(r)
            out.append(dict(data_label=L, group=group, listing_id=lid, shop=r['shop_name'], shop_age_months=r['shop_age_month'].replace(' Mo.', ''),
                            listing_age_months=r['listing_age_in_months'].replace(' Mo.', ''), price=r['price'], shop_total_sales=r['transaction_sold_count'],
                            est_12mo_units=r['est_mo_sales'], trend_12mo=' '.join(map(str, r['trends'])), active_months=act, listing_share_of_shop=round(c, 3),
                            reviews=r['est_reviews'], entrant_status=st, format_title_only=fmt, mechanism_title_only=mech, hero_claim_title_only=hero,
                            adhd_class=cls, restart_or_low_energy_in_title=restart, page_count='UNVERIFIED (403)', complaints='UNVERIFIED (403)', title=r['title']))
    with open(os.path.join(H, 'COMPETITORS.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    for o in out:
        print(f"{o['group']:10} {o['listing_id']} {o['shop'][:22]:22} {o['price']:>7} u={o['est_12mo_units']:>5} shop={o['shop_age_months']:>3}mo/{o['shop_total_sales']:>7} act={o['active_months']:>2} {o['entrant_status']:10} {o['adhd_class']}")
    ex = [o for o in out if o['group'] == 'EXACT']
    print('EXACT CLEAN/NEAR-CLEAN:', [(o['shop'], o['entrant_status']) for o in ex if o['entrant_status'] in ('CLEAN', 'NEAR-CLEAN')])
    print('EXACT with >=100 units:', sum(1 for o in ex if num(o['est_12mo_units']) >= 100), '/', len(ex))
