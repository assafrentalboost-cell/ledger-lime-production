"""Astra audit tables. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.
Reads only files produced by run_all.sh and raw/*.json. Writes the five CSVs + astra_tables_output.txt (headline checks).
All rules are defined in this file or imported from the pipeline scripts; nothing is hand-entered."""
import csv, glob, json, os, re, statistics, difflib
from collections import defaultdict
from summary import ADHD_JOBS, KID as DEPTH_EXCLUDE, ADHD
from grouping import assign
from clone_check import dups, PLR
H = os.path.dirname(os.path.abspath(__file__))
LABEL = 'EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA'
OVERLAY_EXCLUDE = re.compile(r'kids?|toddler|child|classroom|student|teacher|visual schedule|png|clip ?art|\bstl\b|fidget', re.I)  # = grouping.py OVERLAYS
def num(s):
    s = str(s).replace('$', '').replace(',', '').replace(' Mo.', '').strip()
    try: return float(s)
    except: return 0.0
def q(v, p):
    v = sorted(v)
    if not v: return ''
    k = (len(v) - 1) * p; f = int(k); c = min(f + 1, len(v) - 1)
    return round(v[f] + (v[c] - v[f]) * (k - f), 2)

# ---------- formats (title regex; product files were NOT inspected — Etsy pages are blocked) ----------
FORMATS = [('Notion', r'notion'), ('Sheets', r'google sheet|sheets'), ('Excel', r'excel'), ('Canva', r'canva'),
           ('app/web', r'\bapp\b|chatgpt|\bai assistant|web app'), ('Digital planner (Goodnotes/Notability)', r'goodnotes|notability|digital planner|ipad|hyperlinked'),
           ('PDF', r'pdf|printable|print')]
def fmt(t):
    hit = [f for f, rx in FORMATS if re.search(rx, t, re.I)]
    if 'Sheets' in hit and 'Excel' in hit and len(hit) == 2: return 'Sheets+Excel'
    if not hit: return 'unstated'
    return hit[0] if len(hit) == 1 else 'hybrid (' + '+'.join(hit) + ')'
def fmt_family(f):
    if f.startswith('hybrid'): return 'hybrid'
    return {'Sheets+Excel': 'Sheets/Excel', 'Sheets': 'Sheets/Excel', 'Excel': 'Sheets/Excel'}.get(f, f)

# ---------- job + ADHD-depth classes ----------
def job(title):
    if DEPTH_EXCLUDE.search(title): return ''
    for j, rx in ADHD_JOBS:
        if rx.search(title): return j
    return ''
NATIVE = re.compile(r'brain dump|brain reset|task paralysis|executive (dys)?function|dopamine|overwhelm|adhd coach|adhd.friendly|for adhd|neurodivergent|neurospicy|second brain for adhd', re.I)
def adhd_class(title):
    """ADHD-NATIVE : the title names an ADHD-specific mechanism or need (brain dump, task paralysis, executive function, dopamine,
                     overwhelm, 'ADHD-friendly', 'for ADHD', neurodivergent, made by an ADHD coach).
       ADHD-BOLT-ON: not native AND the first 'adhd' appears at character >= 40 (ADHD appended to a generic product name).
       ADHD-ADAPTED: otherwise (ADHD is in the product name but no ADHD-specific mechanism is named).
       Title-level only. Whether the PRODUCT differs from a generic one cannot be verified without the files."""
    if NATIVE.search(title): return 'ADHD-NATIVE'
    m = re.search(r'adhd', title, re.I)
    if m and m.start() >= 40: return 'ADHD-BOLT-ON'
    return 'ADHD-ADAPTED'
BUNDLE = re.compile(r'bundle|all.in.one|mega|whole shop|\d+\+? ?(pages|checklists|tabs)|kit\b|system', re.I)
PERSONA = {'Bills, budget & paycheck': 'adult with ADHD who misses bills / pays late fees',
           'Cleaning & chore system': 'adult with ADHD overwhelmed by housework',
           'Daily / weekly planner': 'adult with ADHD needing day/week structure',
           'Life OS / second brain (all-in-one)': 'adult with ADHD wanting one place for everything',
           'Brain dump / task paralysis / prioritising': 'adult with ADHD stuck starting tasks',
           'Habits, goals & routines': 'adult with ADHD building routines'}
PHRASE = {'Bills, budget & paycheck': 'adhd budget planner / budget planner adhd', 'Cleaning & chore system': 'adhd cleaning planner / adhd cleaning checklist',
          'Daily / weekly planner': 'adhd planner / adhd daily planner', 'Life OS / second brain (all-in-one)': 'adhd notion / adhd life planner',
          'Brain dump / task paralysis / prioritising': 'adhd brain dump', 'Habits, goals & routines': 'adhd habit tracker / adhd workbook'}
SAME_AS_6 = {'Bills, budget & paycheck': 'YES — same buyer, SAME door as #6 (overlap/cannibalisation)'}

def entrant_rule(r):
    if r['status'] == 'CLEAN':
        return (f"CLEAN: shop {r['shop_age']}<=24mo; shop sales {r['shop_sales']}<=15,000; units {r['units']}>=100; active {r['active']}/12>=8; "
                f"last3 {sum(r['last3'])}>0; not PLR (title+shop); contribution {r['contrib']}>=0.05")
    return (f"NEAR-CLEAN: passes all CLEAN rules except active {r['active']}/12<8; listing age {r['listing_age']}<12 and "
            f"active >= 0.7*min(listing age,12)={0.7*min(num(r['listing_age']),12):.1f}")

def write(name, rows, cols):
    with open(os.path.join(H, name), 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['data_label'] + cols)
        for r in rows: w.writerow([LABEL] + [r.get(c, '') for c in cols])

if __name__ == '__main__':
    out = []
    P = lambda *a: (out.append(' '.join(str(x) for x in a)), print(*a))
    d = json.load(open(os.path.join(H, 'clusters.json')))
    # ===== 1. ADHD-CLEAN-ENTRANTS.csv : every passing listing in the ADHD_ADULT overlay =====
    ent = [r for r in d['listings'] if ADHD.search(r['title']) and not OVERLAY_EXCLUDE.search(r['title'])]
    rows = []
    for r in sorted(ent, key=lambda r: (r['status'], -num(r['units']))):
        rows.append(dict(shop=r['shop'], shop_age_months=num(r['shop_age']), shop_total_sales=r['shop_sales'], listing_id=r['listing_id'], title=r['title'],
                         listing_age_months=num(r['listing_age']), price=r['price'], est_12mo_units=r['units'], est_12mo_revenue=r['revenue'],
                         trend_12mo=' '.join(map(str, r['trend'])), last_3_months=' '.join(map(str, r['last3'])), queries=';'.join(r['queries']),
                         job_cluster_grouping=r['cluster'], buyer_job=job(r['title']) or '(not counted in depth: excluded/other)', format=fmt(r['title']),
                         classification=r['status'], rule=entrant_rule(r)))
    write('ADHD-CLEAN-ENTRANTS.csv', rows, list(rows[0]))
    shops = defaultdict(set)
    for r in ent: shops[r['shop']].add(r['status'])
    clean = {s for s, v in shops.items() if 'CLEAN' in v}; near = set(shops) - clean
    P('ADHD listings in overlay:', len(ent), '| CLEAN shops:', len(clean), '| NEAR-CLEAN-only shops:', len(near), sorted(near))

    # ===== 2. ADHD-JOB-DEPTH.csv : the exact rows summary.adhd_depth() counted =====
    young = json.load(open(glob.glob(os.path.join(H, 'raw', 'F-adhd-p1-*.json'))[0]))['rows']
    sup = [dict(src='entrant', listing_id=r['listing_id'], shop=r['shop'], price=r['price'], units=r['units'], title=r['title']) for r in ent]
    sup += [dict(src='young<=3mo', listing_id=r['listing_id'], shop=r['shop_name'], price=r['price'], units=r['est_mo_sales'], title=r['title'])
            for r in young if num(r['est_mo_sales']) >= 30 and ADHD.search(r['title']) and not DEPTH_EXCLUDE.search(r['title'])]
    jr = []; per = defaultdict(lambda: dict(shops=set(), units=0, classes=defaultdict(int)))
    for r in sup:
        j = job(r['title'])
        if not j or j not in PERSONA: continue
        c = adhd_class(r['title']); per[j]['shops'].add(r['shop']); per[j]['units'] += num(r['units']); per[j]['classes'][c] += 1
        jr.append(dict(job=j, source=r['src'], listing_id=r['listing_id'], shop=r['shop'], price=r['price'], est_12mo_units=r['units'], title=r['title'],
                       buyer_persona=PERSONA[j], acquisition_phrase=PHRASE[j], standalone_or_bundled='BUNDLED' if BUNDLE.search(r['title']) else 'STANDALONE',
                       same_buyer_as_product_6=SAME_AS_6.get(j, 'YES — same buyer persona, different job from #6'),
                       adhd_class=c, same_without_adhd_wording={'ADHD-BOLT-ON': 'LIKELY YES', 'ADHD-ADAPTED': 'UNVERIFIED (title only)', 'ADHD-NATIVE': 'LIKELY NO'}[c]))
    write('ADHD-JOB-DEPTH.csv', sorted(jr, key=lambda r: (r['job'], -num(r['est_12mo_units']))), list(jr[0]))
    P('\nJOB DEPTH (rule: >=2 distinct shops). Same-row note: a young listing that is also an entrant row is counted once per shop, not per row.')
    valid = 0
    for j in PERSONA:
        v = per[j]; ok = len(v['shops']) >= 2
        nonbolt = {s for s in v['shops'] if any(x['shop'] == s and x['job'] == j and x['adhd_class'] != 'ADHD-BOLT-ON' for x in jr)}
        valid += ok and len(nonbolt) >= 2
        P(f"  {j}: shops={len(v['shops'])} units={int(v['units'])} classes={dict(v['classes'])} | shops with a non-bolt-on listing={len(nonbolt)} -> "
          f"{'VALID' if ok and len(nonbolt) >= 2 else 'WEAK'}")
    P('VALID SAME-BUYER JOBS (>=2 shops AND >=2 shops with a non-bolt-on listing):', valid)
    # sensitivity: summary.KID also drops 'worksheet|therapy|therapist' (meant for kids/clinical worksheets). It removes Templix8's adult
    # 'ADHD Brain Reset Bundle ... Brain Dump Worksheet'. Re-test brain dump with the overlay exclusion only:
    bd = {r['shop'] for r in ent if not OVERLAY_EXCLUDE.search(r['title']) and re.search(ADHD_JOBS[2][1].pattern, r['title'], re.I)
          and not re.search(ADHD_JOBS[0][1].pattern + '|' + ADHD_JOBS[1][1].pattern, r['title'], re.I) and adhd_class(r['title']) != 'ADHD-BOLT-ON'}
    P('   sensitivity — brain-dump shops with a non-bolt-on listing if "worksheet" is not excluded:', len(bd), sorted(bd))

    # ===== 3. ADHD-RECENT-ENTRY.csv : the young pool exactly as clone_check.young('adhd') used it =====
    Y = [r for r in young if not OVERLAY_EXCLUDE.search(r['title'])]
    yr = []
    for r in sorted(Y, key=lambda r: -num(r['est_mo_sales'])):
        j = job(r['title']); g = assign(r['title'])[0]
        yr.append(dict(listing_id=r['listing_id'], shop=r['shop_name'], shop_age_months=num(r['shop_age_month']), shop_total_sales=r['transaction_sold_count'],
                       listing_age_months=num(r['listing_age_in_months']), est_12mo_units=r['est_mo_sales'], price=r['price'], title=r['title'],
                       adhd_job=j or '(none — not an adult life-admin job)', grouping_cluster=g, new_shop_flag=int(num(r['shop_age_month']) <= 24),
                       ge30_flag=int(num(r['est_mo_sales']) >= 30)))
    write('ADHD-RECENT-ENTRY.csv', yr, list(yr[0]))
    n = len(Y); ge = [r for r in yr if r['ge30_flag']]; ns = [r for r in ge if r['new_shop_flag']]
    dp = dups([dict(shop=r['shop_name'], title=r['title']) for r in Y])
    P(f'\nRECENT ENTRY: pool={n} (raw pull={len(young)}; {len(young)-n} removed by overlay exclusion) | >=30 units={len(ge)} | of which new shop={len(ns)} | near-dup pairs={len(dp)}')
    for x in dp: P('   dup pair', x)
    ge_job = [r for r in ge if not r['adhd_job'].startswith('(none')]
    P(f'   sensitivity: >=30 units AND in one of the 6 life-admin jobs = {len(ge_job)}; of which new shop = {sum(r["new_shop_flag"] for r in ge_job)}')
    P(f'   pool definition: top 100 listings with listing age <=3 months and "adhd" in title, ANY shop, sorted by 12-mo units desc. '
      f'All {len(young)} raw rows have units>=1, so the pool cap was hit: this is a TOP-SELLERS sample, not all new listings; 24/75 is not a sell-through rate.')
    ages = sorted({num(r['listing_age_in_months']) for r in Y}); P('   listing ages present (months):', ages)

    # ===== 4. ADHD-PRICE-FORMAT.csv : all adult-ADHD listings we hold (entrant overlay + young pool + rejected entrant rows) =====
    allc = {r['listing_id']: r for r in json.load(open(os.path.join(H, 'all_listings_classified.json')))}
    pool = {}
    for r in allc.values():
        if ADHD.search(r['title']) and not OVERLAY_EXCLUDE.search(r['title']):
            pool[r['listing_id']] = dict(source='entrant pull (' + r['status'] + ')', shop=r['shop'], shop_age=num(r['shop_age']), price=num(r['price']),
                                         units=num(r['units']), trend=r['trend'], title=r['title'], status=r['status'])
    for r in Y:
        pool.setdefault(r['listing_id'], dict(source='young pool (<=3mo, any shop)', shop=r['shop_name'], shop_age=num(r['shop_age_month']), price=num(r['price']),
                                             units=num(r['est_mo_sales']), trend=r['trends'], title=r['title'], status='young'))
    pr = []
    for lid, r in sorted(pool.items(), key=lambda x: -x[1]['units']):
        t = r['trend'] or []; f = fmt(r['title'])
        pr.append(dict(listing_id=lid, source=r['source'], shop=r['shop'], price_listed=f"{r['price']:.2f}", est_12mo_units=int(r['units']),
                       trend_12mo=' '.join(map(str, t)), active_months=sum(1 for v in t if v > 0), format=f, format_family=fmt_family(f),
                       premium_ge15=int(r['price'] >= 15), active_10plus=int(sum(1 for v in t if v > 0) >= 10),
                       shop_type='new (<=24mo)' if r['shop_age'] <= 24 else 'established (>24mo)', in_overlay_passing=int(r['status'] in ('CLEAN', 'NEAR-CLEAN')),
                       title=r['title']))
    write('ADHD-PRICE-FORMAT.csv', pr, list(pr[0]))
    def share(rows):
        U = sum(r['est_12mo_units'] for r in rows)
        return {k: round(sum(r['est_12mo_units'] for r in rows if lo <= float(r['price_listed']) < hi) / U, 3) for k, lo, hi in
                [('<$4', 0, 4), ('$4-12', 4, 12), ('$12-15', 12, 15), ('>=$15', 15, 1e9)]}, int(U)
    ov = [r for r in pr if r['in_overlay_passing']]
    P('\nPRICE: unit share by price band — overlay passing listings (the report base):', share(ov))
    P('PRICE: same — every adult-ADHD listing held (incl. rejected + young):', share(pr))
    prem = [r for r in pr if r['premium_ge15']]
    fam = defaultdict(lambda: [0, 0, set()])
    for r in prem: fam[r['format_family']][0] += 1; fam[r['format_family']][1] += r['est_12mo_units']; fam[r['format_family']][2].add(r['shop'])
    P('PREMIUM (>=$15) listings:', len(prem), '| by format family (listings, units, shops):', {k: (v[0], v[1], len(v[2])) for k, v in fam.items()})
    pu = sum(v[1] for v in fam.values()); nn = sum(v[1] for k, v in fam.items() if k in ('Notion', 'app/web'))
    P(f'PREMIUM units in Notion or app/web = {nn}/{pu} = {nn/pu:.2f}')
    for r in prem: P('   premium', r['shop'], r['price_listed'], r['est_12mo_units'], 'active', r['active_months'], r['format'], r['source'], '|', r['title'][:60])

    # ===== 5. ADHD-CLONE-FLOOD.csv : per job subcluster over the same listing pool =====
    sub = defaultdict(list)
    for lid, r in pool.items():
        j = job(r['title'])
        if j in PERSONA: sub[j].append(dict(r, listing_id=lid))
    yage = {r['listing_id']: num(r['listing_age_in_months']) for r in young}
    lage = {lid: num(r['listing_age']) for lid, r in allc.items()}
    cf = []
    P('\nCLONE/FLOOD per subcluster (TITLE-level evidence only; product files not inspected, so no PRODUCT cloning is claimed):')
    for j in PERSONA:
        L = sub[j]; ages = [yage.get(r['listing_id'], lage.get(r['listing_id'], 99)) for r in L]
        dpj = dups([dict(shop=r['shop'], title=r['title']) for r in L])
        ident = sum(1 for a in range(len(L)) for b in range(a + 1, len(L)) if L[a]['shop'] != L[b]['shop'] and L[a]['title'].strip().lower() == L[b]['title'].strip().lower())
        plr = [r['shop'] + ': ' + r['title'][:50] for r in L if PLR.search(r['title']) or re.search(r'plr|mrr', r['shop'], re.I)]
        prices = [r['price'] for r in L]
        row = dict(subcluster=j, listings_sampled=len(L), listings_le_1mo=sum(1 for a in ages if a <= 1), listings_le_3mo=sum(1 for a in ages if a <= 3),
                   near_duplicate_title_pairs=len(dpj), near_duplicate_shops=len({x[1] for x in dpj} | {x[2] for x in dpj}), identical_title_pairs=ident,
                   plr_resell_examples=' | '.join(plr) or 'none', units_total=int(sum(r['units'] for r in L)),
                   units_new_shops=int(sum(r['units'] for r in L if r['shop_age'] <= 24)), price_min=min(prices), price_median=q(prices, .5), price_q3=q(prices, .75),
                   price_max=max(prices), share_listings_under_4=round(sum(1 for p in prices if p < 4) / len(prices), 2),
                   duplicate_pairs_detail=' || '.join(f'{x[0]} {x[1]} ~ {x[2]}' for x in dpj))
        cf.append(row); P('  ', {k: v for k, v in row.items() if k != 'duplicate_pairs_detail'})
    write('ADHD-CLONE-FLOOD.csv', cf, list(cf[0]))
    P('   note: listing age is whole months in EverBee; "<=30 days" is approximated by listing_age_in_months <= 1, "<=90 days" by <= 3.')
    # ===== 6. Runner-up tables: Wedding Planning Admin and Diet-Change Food Guides =====
    for c, tag, fn in [('WEDDING_PLAN_ADMIN', 'wedding-planner', 'RUNNERUP-WEDDING'), ('DIET_CONDITION', 'food-list', 'RUNNERUP-DIET')]:
        L = [r for r in d['listings'] if r['cluster'] == c]
        er = [dict(shop=r['shop'], shop_age_months=num(r['shop_age']), shop_total_sales=r['shop_sales'], listing_id=r['listing_id'], title=r['title'],
                   listing_age_months=num(r['listing_age']), price=r['price'], est_12mo_units=r['units'], est_12mo_revenue=r['revenue'],
                   trend_12mo=' '.join(map(str, r['trend'])), last_3_months=' '.join(map(str, r['last3'])), queries=';'.join(r['queries']), format=fmt(r['title']),
                   classification=r['status'], rule=entrant_rule(r)) for r in sorted(L, key=lambda r: -num(r['units']))]
        write(fn + '-ENTRANTS.csv', er, list(er[0]))
        YY = json.load(open(glob.glob(os.path.join(H, 'raw', f'F-{tag}-p1-*.json'))[0]))['rows']
        yy = [dict(listing_id=r['listing_id'], shop=r['shop_name'], shop_age_months=num(r['shop_age_month']), shop_total_sales=r['transaction_sold_count'],
                   listing_age_months=num(r['listing_age_in_months']), est_12mo_units=r['est_mo_sales'], price=r['price'], title=r['title'],
                   new_shop_flag=int(num(r['shop_age_month']) <= 24), ge30_flag=int(num(r['est_mo_sales']) >= 30),
                   plr_flag=int(bool(PLR.search(r['title'])))) for r in sorted(YY, key=lambda r: -num(r['est_mo_sales']))]
        write(fn + '-RECENT-ENTRY.csv', yy, list(yy[0]))
        P(f"\nRUNNER-UP {c}: entrant listings={len(er)} clean shops={len({r['shop'] for r in er if r['classification']=='CLEAN'})} | young pool={len(yy)} "
          f">=30={sum(r['ge30_flag'] for r in yy)} new-shop>=30={sum(r['ge30_flag'] and r['new_shop_flag'] for r in yy)} "
          f"dup pairs={len(dups([dict(shop=r['shop'], title=r['title']) for r in yy]))}")
    open(os.path.join(H, 'astra_tables_output.txt'), 'w').write(LABEL + '\n' + '\n'.join(out) + '\n')
