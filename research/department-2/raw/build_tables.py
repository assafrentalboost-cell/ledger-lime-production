"""Rebuild Department #2 evidence tables from the raw EverBee pulls in this folder.
All figures: EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.
Run: python3 -I research/department-2/raw/build_tables.py > /tmp/tables.md
"""
import json, glob, os, difflib
D = os.path.dirname(os.path.abspath(__file__))
def num(s):
    s = str(s).replace('$','').replace(',','').replace(' Mo.','').strip()
    try: return float(s)
    except: return 0.0
L = {}   # listing_id -> merged row
SHOPS = {}
for f in sorted(glob.glob(os.path.join(D, '*.json'))):
    d = json.load(open(f)); name = os.path.basename(f)
    if name.startswith('00-'): continue
    q = d['input'].get('params', {}).get('title_include') or ('shop:' + d['input'].get('shop_name', ''))
    for r in d['rows']:
        if 'listing_id' not in r:
            SHOPS[r['shop_name']] = r; continue
        cur = L.setdefault(r['listing_id'], dict(r, queries=[]))
        cur['queries'].append(f"{name.split('-')[0]}:'{q}'")
        for k, v in r.items():
            if k not in cur or cur[k] in (None, ''): cur[k] = v
SUB = {
 'BCBA fieldwork': ['4380241497','1363909460','4520133617','1618746219'],
 'RBT supervision': ['1778866660','4309930507','1727988688'],
 'LPC / counselor hours (credential/state)': ['1825428434','4331852387','4319768804','4331925377','1723260304','1862536485','1879121281','1864554741','1556858576','1581431583','1511655580','1882679873','4365438517'],
 'Generic clinical-hours tracker': ['4416002573','4487902011','1893032061','4370846790','4372579394','4524212812','4370668185','1760844761','1771810201','4332303912'],
 'Social-work / clinical supervision hours': ['4307174109','1864198989','4309739011','1838145081','1280717084','4358019328','1399006907','1391502922','1701065441'],
 'Practicum / internship': ['4539272511','1725095822','1750302814','1399460427','4487232723'],
 'CEU tracker': ['1884629149','1493338141','4417800076','4491599082','4313588474','4356445353','1212478346','1712088974','4385702221','1890114952','4453244817','4482588465'],
 'Therapist practice admin (ADJACENT)': ['4442307353','4487203440','4461077565','4418550110','4389483411','4367226738','1904251623','1737172248','4416316995','4341129684','4334790433','4333738546','4348261860','4483073779','1411679125','1859430925'],
}
NOTARY = {
 'Notary business spreadsheet': ['1863823432','4333630601'],
 'Mileage / expense / bookkeeping': ['1903095693'],
 'Appointment / signing checklist': ['1863431297','4304170765','1423661437'],
 'Client intake (form, not tracker)': ['4303181586','4354699283'],
 'Journal / log (printable)': ['1765115180','1779309427','1782442268','1796624155','1284782788','4360610081'],
 'Signing guide / scripts (content)': ['4334034182','1633708336','1384464588','981156493','1883823644'],
 'Practice loan packages (content)': ['1890575020','1692569221','1692149683','1484292572','1487531354'],
 'Notarial certificates / forms (legal)': ['1899285799','1850888986','1847781350','4365474382','1734627614','4495876623','4495878446','4384798510','1373599120'],
 'Marketing (Canva / social)': ['1759564813','4326546815','4330883882','4349743402','1837342645','1441947581','1891310634','4362843532','1826148877','4350170529','4331522432','1810051123','4298091392','1873682281','1705137162','1432078903','1522057522'],
}
def act(t): return sum(1 for x in (t or []) if x > 0)
def row(lid, tag):
    r = L.get(lid)
    if not r: return f"| {lid} | NOT IN RAW FILES | | | | | | | | | | | {tag} |"
    sh = SHOPS.get(r.get('shop_name'), {})
    rev = r.get('est_mo_revenue') or f"n/c (≈${num(r['price'])*num(r['est_mo_sales']):,.0f} = price×units)"
    t = r.get('trends') or []
    return (f"| {lid} | {r.get('shop_name','')} | {r['title'][:70]} | {r['price']} | {r['listing_age_in_months']} | {r.get('shop_age_month','')} | "
            f"{sh.get('listing_active_count','n/p')} | {r.get('transaction_sold_count','')} | {r['est_mo_sales']} | {rev} | {t} | {act(t)}/12 | {'; '.join(r['queries'])} | {tag} |")
HDR = "| Listing ID | Shop | Title (70 ch) | Price | Listing age | Shop age | Shop active listings | Shop total sales | 12-mo units | 12-mo revenue | Monthly trend (oldest→newest) | Active | Query that surfaced it | Core/Adjacent |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"
def section(groups, coretag):
    out=[]
    for g, ids in groups.items():
        tag = 'ADJACENT' if 'ADJACENT' in g or g in ('Journal / log (printable)','Signing guide / scripts (content)','Practice loan packages (content)','Notarial certificates / forms (legal)','Marketing (Canva / social)','Client intake (form, not tracker)') else 'CORE'
        tot = sum(num(L[i]['est_mo_sales']) for i in ids if i in L)
        out.append(f"\n#### {g} — {len(ids)} listings, {int(tot):,} units (EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA)\n\n{HDR}")
        out += [row(i, tag) for i in sorted(ids, key=lambda i: -num(L[i]['est_mo_sales']) if i in L else 0)]
    return '\n'.join(out)
print('## CLINICAL LISTINGS'); print(section(SUB,'')) 
print('\n## NOTARY LISTINGS'); print(section(NOTARY,''))
# totals
def tot(ids): return int(sum(num(L[i]['est_mo_sales']) for i in ids if i in L))
core = [i for g,ids in SUB.items() if 'ADJ' not in g for i in ids]
adj = SUB['Therapist practice admin (ADJACENT)']
print(f"\nCLINICAL core units = {tot(core):,} over {len(core)} listings; adjacent practice admin = {tot(adj):,} over {len(adj)}")
nc = NOTARY['Notary business spreadsheet']+NOTARY['Mileage / expense / bookkeeping']+NOTARY['Appointment / signing checklist']
na = [i for g,ids in NOTARY.items() for i in ids if i not in nc]
print(f"NOTARY core-admin units = {tot(nc):,} over {len(nc)} listings; other notary = {tot(na):,} over {len(na)}")
# 57% reconstruction
orig = ['4416002573','1893032061','4370846790','4372579394','1882679873','4309739011','4307174109','4332303912','4358019328','4524212812','4370668185','1760844761','1771810201','4365438517','4487902011']
o = tot(orig); print(f"\n57% ORIGINAL SUBSET: numerator ExclusiveDesignLab 4416002573 = {int(num(L['4416002573']['est_mo_sales']))}; denominator = {o} over {len(orig)} hand-picked listings; share = {num(L['4416002573']['est_mo_sales'])/o:.1%}")
for i in orig: print(f"   {i} {L[i]['shop_name']} {L[i]['est_mo_sales']}")
for label, f in [('20 hours tracker (all 30 rows, any topic)','20-hours-tracker.json'),('22 licensure (22 rows)','22-licensure.json'),('S34 supervision (25 rows)','S34-supervision.json')]:
    rows = json.load(open(os.path.join(D,f)))['rows']
    t = sum(num(r['est_mo_sales']) for r in rows); e = sum(num(r['est_mo_sales']) for r in rows if r['shop_name']=='ExclusiveDesignLab' and r['listing_id']=='4416002573')
    print(f"   alt denominator {label}: {int(t)} units; ExclusiveDesignLab clinical listing share {e/t:.1%}")
g = SUB['Generic clinical-hours tracker']; print(f"   alt: generic clinical-hours group as defined above: {tot(g)} units; share {num(L['4416002573']['est_mo_sales'])/tot(g):.1%}")
allcore = tot(core); print(f"   alt: all clinical CORE listings: {allcore} units; share {num(L['4416002573']['est_mo_sales'])/allcore:.1%}")
# title duplication
pairs=[('4416002573','4487902011'),('1893032061','4370668185'),('4416002573','4524212812'),('4380241497','4520133617')]
print('\nTITLE SIMILARITY')
for a,b in pairs:
    ta,tb=L[a]['title'],L[b]['title']; print(f"{a} vs {b}: identical={ta==tb} ratio={difflib.SequenceMatcher(None,ta.lower(),tb.lower()).ratio():.2f}")
