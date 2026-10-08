"""Stages 3-5, 7-10: five-job test, substitution, per-job entrant proof, health, flood, price, format.
EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.

Pools (all from raw/, nothing hand-entered):
  ENTRANT pool = every listing in all_listings_classified.json (any status; each already has >=100 12-mo units and a shop <=24 mo).
                 "Selling shop" for a job = distinct shop with >=1 listing in that job (paid-product evidence).
                 "Clean shop" = shop with a CLEAN listing in the job. "Active shop" = shop with an ACTIVE-health listing.
  YOUNG pool   = raw/F-<tag>-*.json (listing age <=3 mo, any shop, top 100 by units). Winner = >=30 units; new shop = shop <=24 mo.
Buyer filter = the finalist's buyer regex below AND NOT the merch/decor regex (fan-gift purchases are excluded).
Job = FIRST job regex that matches the title (order inside each buyer matters; it is listed in code).

A JOB IS VALID when: >=2 selling shops AND >=1 CLEAN or ACTIVE shop AND its relationship to the rest of the family is not SUBSTITUTE.
Substitution labels are analyst judgements, written below with a one-line reason each, and checked against one data test:
  ALL-IN-ONE SHARE = units of buyer listings whose title matches >=3 different job regexes / buyer units (a high share means one
  bundle is replacing the family)."""
import json, os, re, glob, statistics, difflib
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__))
MERCH = re.compile(r'\bpng\b|\bsvg\b|clip ?art|sublimation|tumbler|mug|embroidery|\bstl\b|shirt|sewing|pattern|sticker|nursery|crochet|murder mystery|baby shower', re.I)
def num(s):
    s = str(s).replace('$', '').replace(',', '').replace(' Mo.', '').strip()
    try: return float(s)
    except: return 0.0

FIN = {
 'Nurse / nursing student': dict(
    buyer=r'\bnurs(e|es|ing)\b|\brn\b|sbar|head.to.toe|nclex|\bcna\b|\blpn\b|ccrn|report sheet|brain sheet|med.?surg', young='nurse',
    jobs=[('Shift report / handoff sheet', r'report sheet|brain sheet|sbar|handoff|report template', 'start of every shift; hand-off at shift change', 'nurse report sheet', 'STRONG (documentation / handoff)'),
          ('Patient assessment template', r'head.to.toe|assessment (template|checklist)', 'clinical rotation or new unit', 'head to toe assessment template', 'STRONG (documentation)'),
          ('Career documents (resume / pivot)', r'resume|\bcv\b|consultant|interview', 'job change, new-grad hiring, career pivot', 'nurse resume template', 'MEDIUM (career admin)'),
          ('Unit recognition / staff appreciation', r'award|superlative|appreciation|treat tag|thank you card', 'Nurses Week, preceptor thank-you (bought by charge nurse / manager)', 'nurse appreciation awards', 'WEAK (gift)'),
          ('School planner / clinical tracker', r'planner|tracker|clinical (hours|log)', 'semester start', 'nursing school planner', 'STRONG (planning / records)'),
          ('Drug / pharmacology reference', r'pharmacolog|meds guide|\bdrug', 'pharm course; new meds on unit', 'pharmacology cheat sheet', 'WEAK (clinical content; liability)'),
          ('Bedside quick-reference', r'cheat sheet|reference guide|dosing|cranial nerve', 'new specialty unit / float', 'nurse cheat sheet', 'WEAK (clinical content; liability)'),
          ('Course / exam study notes', r'anatomy|nclex|study|ccrn|concept map|notes|flashcard|med.?surg|critical care', 'exam / course', 'nursing study guide', 'WEAK (education content)')]),
 'Esthetician / lash / nail / hair pro': dict(
    buyer=r'\besthetic|salon|\blash|nail tech|hair ?stylist|braid|\bbrow|\bwax|\bmua\b|makeup artist|spray tan|med ?spa|\bwig|hair vendor|acuity|aftercare', young='esthetician',
    jobs=[('Contracts / client policy / consent', r'contract|agreement|policy|consent|intake', 'opening a suite / renting a booth', 'salon booth rental agreement', 'STRONG (admin / records)'),
          ('Client aftercare cards', r'aftercare|care card', 'every appointment', 'lash aftercare card', 'MEDIUM (client documentation)'),
          ('Training / course materials', r'training|course|textbook|manual|student', 'teaching students / launching a course', 'lash training manual', 'MEDIUM'),
          ('Service menu / price list', r'price ?list|pricelist|menu|pricing', 'price change, new services', 'salon price list template', 'MEDIUM (pricing)'),
          ('Online booking site', r'acuity|booking (site|website|page)|square|website', 'going independent / new booking system', 'acuity scheduling template', 'WEAK (web design)'),
          ('Brand identity (logo / card)', r'logo|business card|branding', 'launching the business', 'lash tech business card', 'WEAK (design)'),
          ('Social content (posts / reels)', r'instagram|reels|social media|posts|stories', 'ongoing marketing', 'esthetician instagram templates', 'WEAK (design)'),
          ('Promotion / booking flyers', r'flyer|special|sale|book now|bookings', 'monthly / seasonal promotion', 'booking flyer', 'WEAK (design)')]),
 'Homeschool parent': dict(
    buyer=r'homeschool|home school', young='homeschool',
    jobs=[('High-school transcript', r'transcript', 'teen applying to college / job', 'homeschool transcript template', 'STRONG (records)'),
          ('Diploma / graduation', r'diploma|graduat', 'graduation', 'homeschool diploma', 'MEDIUM (document)'),
          ('Attendance / compliance / progress records', r'attendance|hours|portfolio|report card|progress', 'state reporting, annual review', 'homeschool attendance record', 'STRONG (records / compliance)'),
          ('Planner / lesson scheduling', r'planner|lesson plan|schedule|checklist|organizer', 'school-year start', 'homeschool planner', 'STRONG (planning)'),
          ('Faith / Bible crafts', r'bible|sunday school|church|creation|prayer|jesus', 'weekly lesson', 'bible craft printable', 'WEAK (content)'),
          ('Curriculum / worksheets', r'curriculum|worksheet|workbook|activit|tracing|math|reading|bundle|lesson', 'subject gap / new grade', 'homeschool curriculum', 'WEAK (education content)')]),
 'Real estate agent': dict(
    buyer=r'realtor|real estate|open house|listing presentation|pre-listing|buyer (guide|questionnaire|consultation|roadmap|packet)|seller guide|broker', young='real-estate',
    jobs=[('Licence exam prep', r'exam|license', 'pre-licence course', 'real estate exam cheat sheet', 'WEAK (education)'),
          ('Buyer consultation / guide', r'buyer', 'new buyer client', 'real estate buyer guide', 'MEDIUM (client documentation)'),
          ('Seller / listing presentation', r'seller|listing presentation|pre-listing|cma', 'listing appointment', 'listing presentation template', 'MEDIUM'),
          ('Open house kit', r'open house|sign in|feedback', 'each open house', 'open house sign in sheet', 'MEDIUM (records)'),
          ('Transaction / closing', r'closing|contract to close|timeline|checklist', 'under contract', 'real estate closing checklist', 'STRONG (workflow)'),
          ('Prospecting mail / farming', r'postcard|newsletter|farming|letter|brochure|neighbor', 'monthly prospecting', 'real estate postcard', 'WEAK (marketing design)'),
          ('Listing marketing (flyer / sign)', r'flyer|yard sign|just listed|sign rider', 'each new listing', 'real estate flyer', 'WEAK (design)'),
          ('Social content', r'instagram|reels|social media|posts', 'ongoing marketing', 'realtor instagram templates', 'WEAK (design)'),
          ('Client gifts', r'portrait|gift|housewarming', 'closing gift', 'realtor closing gift', 'WEAK (gift)')]),
 'Engaged couple (wedding admin)': dict(
    buyer=r'wedding|bachelorette|bridesmaid', young='wedding-planner',
    jobs=[('Budget / vendor payments', r'budget|payment|vendor', 'after engagement, booking vendors', 'wedding budget spreadsheet', 'STRONG (money)'),
          ('Guest list / RSVP / seating', r'guest list|rsvp|seating', 'invitations', 'wedding guest list', 'STRONG (records)'),
          ('Day-of timeline / binder', r'timeline|day.of|itinerary|blueprint', 'final month', 'wedding day timeline', 'STRONG (scheduling)'),
          ('Master planner / binder', r'planner|binder|planning|checklist|spreadsheet', 'start of planning', 'wedding planner spreadsheet', 'STRONG (planning)'),
          ('Bridesmaid / bachelorette admin', r'bridesmaid|bachelorette', 'wedding party', 'bachelorette itinerary', 'MEDIUM')]),
}

# Substitution relationships (analyst judgement, one reason each). C=COMPLEMENTARY, P=PARTIAL OVERLAP, S=SUBSTITUTE.
SUBST = {
 'Nurse / nursing student': {
   'Shift report / handoff sheet': ('CORE', 'daily bedside workflow; re-bought per unit/specialty'),
   'Patient assessment template': ('P', 'many report sheets already contain an assessment block'),
   'Career documents (resume / pivot)': ('C', 'different trigger (job change); never replaced by a report sheet'),
   'Unit recognition / staff appreciation': ('C', 'different buyer role (charge nurse/manager) and occasion'),
   'School planner / clinical tracker': ('C', 'student-phase scheduling; different artifact'),
   'Drug / pharmacology reference': ('P', 'overlaps study bundles and bedside cheat sheets'),
   'Bedside quick-reference': ('P', 'overlaps pharmacology reference and study bundles'),
   'Course / exam study notes': ('S', '4,400-page "nursing school notes" mega bundles replace single study guides')},
 'Esthetician / lash / nail / hair pro': {
   'Online booking site': ('CORE', 'one-time set-up of the booking front door'),
   'Contracts / client policy / consent': ('C', 'legal/admin artifact, different trigger'),
   'Client aftercare cards': ('C', 'per-service client hand-out'),
   'Training / course materials': ('C', 'only for pros who teach'),
   'Service menu / price list': ('P', 'often bundled into branding kits'),
   'Brand identity (logo / card)': ('P', 'branding kits bundle logo + card + IG'),
   'Social content (posts / reels)': ('P', 'branding kits bundle IG templates'),
   'Promotion / booking flyers': ('C', 'monthly re-purchase; seasonal')},
 'Homeschool parent': {
   'Planner / lesson scheduling': ('CORE', 'yearly planning'),
   'High-school transcript': ('C', 'records for college applications'),
   'Diploma / graduation': ('C', 'one-time graduation document'),
   'Attendance / compliance / progress records': ('P', 'all-in-one homeschool planners often include attendance'),
   'Faith / Bible crafts': ('C', 'content, different budget line'),
   'Curriculum / worksheets': ('C', 'content; different supplier choice')},
 'Real estate agent': {
   'Buyer consultation / guide': ('CORE', 'per buyer client'),
   'Seller / listing presentation': ('C', 'per listing appointment'),
   'Open house kit': ('C', 'per open house'),
   'Transaction / closing': ('C', 'per contract'),
   'Prospecting mail / farming': ('P', 'mega marketing bundles cover mail + social'),
   'Listing marketing (flyer / sign)': ('P', 'mega marketing bundles'),
   'Social content': ('P', 'mega marketing bundles (1000+ templates)'),
   'Client gifts': ('C', 'closing gift'),
   'Licence exam prep': ('C', 'pre-licence phase; different moment')},
 'Engaged couple (wedding admin)': {
   'Master planner / binder': ('CORE', 'start of planning'),
   'Budget / vendor payments': ('S', 'all-in-one wedding planner spreadsheets include budget + guests + timeline'),
   'Guest list / RSVP / seating': ('S', 'included in all-in-one planner spreadsheets'),
   'Day-of timeline / binder': ('P', 'day-of binders are sold separately but planners include timelines'),
   'Bridesmaid / bachelorette admin': ('C', 'different occasion and buyer (maid of honour)')},
}

FORMATS = [('Notion', r'notion'), ('Sheets/Excel', r'google sheet|excel|spreadsheet|sheets'), ('Canva', r'canva'), ('Word/Docs', r'\bword\b|google docs|docx'),
           ('fillable PDF', r'fillable|editable pdf'), ('PDF', r'pdf|printable|print'), ('app/web', r'\bapp\b|website|acuity|square')]
def fmt(t):
    for f, rx in FORMATS:
        if re.search(rx, t, re.I): return f
    return 'unstated'
BANDS = [('<$5', 0, 5), ('$5-9.99', 5, 10), ('$10-14.99', 10, 15), ('$15-24.99', 15, 25), ('$25+', 25, 1e9)]

def dups(rows):
    n = 0
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            if rows[i]['shop'] != rows[j]['shop'] and difflib.SequenceMatcher(None, rows[i]['title'][:60].lower(), rows[j]['title'][:60].lower()).ratio() >= 0.70: n += 1
    return n

def run():
    allr = json.load(open(os.path.join(H, 'all_listings_classified.json')))
    out = {}
    for name, F in FIN.items():
        brx = re.compile(F['buyer'], re.I); jobs = [(j, re.compile(rx, re.I), trig, phrase, fit) for j, rx, trig, phrase, fit in F['jobs']]
        pool = [r for r in allr if brx.search(r['title']) and not MERCH.search(r['title'])]
        young = []
        if F['young']:
            for r in json.load(open(glob.glob(os.path.join(H, 'raw', f"F-{F['young']}-p1-*.json"))[0]))['rows']:
                if brx.search(r['title']) and not MERCH.search(r['title']):
                    young.append(dict(listing_id=r['listing_id'], shop=r['shop_name'], title=r['title'], units=num(r['est_mo_sales']), price=num(r['price']),
                                      shop_age=num(r['shop_age_month']), listing_age=num(r['listing_age_in_months'])))
        def job_of(t):
            for j, rx, *_ in jobs:
                if rx.search(t): return j
            return None
        nj = lambda t: sum(1 for j, rx, *_ in jobs if rx.search(t))
        U = sum(r['units'] for r in pool) or 1
        aio = sum(r['units'] for r in pool if nj(r['title']) >= 3) / U
        J = {}
        for j, rx, trig, phrase, fit in jobs:
            L = [r for r in pool if job_of(r['title']) == j]; Y = [r for r in young if job_of(r['title']) == j]
            sel = {r['shop'] for r in L}; cln = {r['shop'] for r in L if r['status'] == 'CLEAN'}; act = {r['shop'] for r in L if r['health'] == 'ACTIVE'}
            yw = [r for r in Y if r['units'] >= 30]
            rel, why = SUBST[name][j]
            JU = sum(r['units'] for r in L) or 1
            J[j] = dict(trigger=trig, acquisition_phrase=phrase, brand_fit=fit, relationship=rel, relationship_reason=why,
                        selling_shops=len(sel), clean_shops=len(cln), active_shops=len(act),
                        health={h: len({r['shop'] for r in L if r['health'] == h}) for h in ('ACTIVE', 'FADING', 'HISTORIC', 'OTHER')},
                        units=int(sum(r['units'] for r in L)), young_listings=len(Y), young_winners=len(yw), young_winner_new_shops=sum(1 for r in yw if r['shop_age'] <= 24),
                        young_le1mo=sum(1 for r in Y if r['listing_age'] <= 1), young_dup_pairs=dups(Y),
                        plr=sum(1 for r in L + Y if re.search(r'\b(plr|mrr|resell)\b', r['title'] + ' ' + r['shop'], re.I)),
                        price_median=round(statistics.median([r['price'] for r in L]), 2) if L else None,
                        price_bands={k: round(sum(r['units'] for r in L if lo <= r['price'] < hi) / JU, 2) for k, lo, hi in BANDS},
                        formats={f: sum(1 for r in L if fmt(r['title']) == f) for f in {fmt(r['title']) for r in L}},
                        valid=len(sel) >= 2 and (len(cln) + len(act)) > 0 and rel != 'S',
                        evidence=[(r['listing_id'], r['shop'], r['price'], int(r['units']), r['status'], r['health'], r['title'][:80]) for r in sorted(L, key=lambda r: -r['units'])[:6]],
                        young_evidence=[(r['listing_id'], r['shop'], r['price'], int(r['units']), int(r['shop_age']), r['title'][:70]) for r in sorted(yw, key=lambda r: -r['units'])[:4]])
        valid = [j for j, v in J.items() if v['valid']]
        rels = [v['relationship'] for v in J.values() if v['valid']]
        out[name] = dict(pool_listings=len(pool), pool_units=int(U), clean_shops=len({r['shop'] for r in pool if r['status'] == 'CLEAN'}),
                         active_shops=len({r['shop'] for r in pool if r['health'] == 'ACTIVE'}),
                         all_in_one_unit_share=round(aio, 3), valid_jobs=len(valid), jobs_ge2_selling=sum(1 for v in J.values() if v['selling_shops'] >= 2),
                         complementary=rels.count('C'), partial=rels.count('P'), substitute=sum(1 for v in J.values() if v['relationship'] == 'S'),
                         young_pool=len(young), young_winners=sum(1 for r in young if r['units'] >= 30), young_winner_new=sum(1 for r in young if r['units'] >= 30 and r['shop_age'] <= 24),
                         young_dup_pairs=dups(young), jobs=J)
    # STAGE 15 GATES (all must pass; no weights)
    for name, o in out.items():
        J = o['jobs']
        credible = [j for j, v in J.items() if v['valid'] and not v['brand_fit'].startswith('WEAK')]
        core = [j for j, v in J.items() if v['relationship'] == 'CORE']
        o['credible_jobs'] = credible
        o['credible_complementary'] = sum(1 for j in credible if J[j]['relationship'] == 'C')
        o['credible_with_repeat_paid'] = sum(1 for j in credible if J[j]['selling_shops'] >= 2)
        sub_units = sum(v['units'] for v in J.values() if v['relationship'] == 'S') / max(1, sum(v['units'] for v in J.values()))
        flood = 'HIGH' if o['young_dup_pairs'] >= 20 else 'MEDIUM' if o['young_dup_pairs'] >= 5 else 'LOW'
        lt5 = sum(v['units'] * v['price_bands']['<$5'] for v in J.values()) / max(1, sum(v['units'] for v in J.values()))
        mid_jobs = sum(1 for j in credible if J[j]['price_median'] and J[j]['price_median'] >= 7)
        G = {'G1 >=2 clean entrants on core job': bool(core) and J[core[0]]['clean_shops'] >= 2,
             'G2 >=5 credible same-buyer jobs (valid AND brand fit not WEAK)': len(credible) >= 5,
             'G3 >=3 credible jobs with repeated paid evidence (>=2 selling shops)': o['credible_with_repeat_paid'] >= 3,
             'G4 >=4 complementary relationships among credible jobs': o['credible_complementary'] >= 4,
             'G5 not dominated by substitutes (substitute-job units < 50%)': sub_units < 0.5,
             'G6 flood survivable (not HIGH, or HIGH with young winners from >=3 new shops)': flood != 'HIGH' or o['young_winner_new'] >= 3,
             'G7 price credible (<$5 unit share < 50% AND >=2 credible jobs with median >= $7)': lt5 < 0.5 and mid_jobs >= 2}
        o.update(flood_rating=flood, substitute_unit_share=round(sub_units, 3), under5_unit_share=round(lt5, 3), mid_price_credible_jobs=mid_jobs,
                 gates=G, passes=all(G.values()))
    json.dump(out, open(os.path.join(H, 'jobs.json'), 'w'), indent=1)
    return out

if __name__ == '__main__':
    out = run()
    for name, o in out.items():
        print(f"\n### {name}: pool={o['pool_listings']} units={o['pool_units']} clean_shops={o['clean_shops']} active_shops={o['active_shops']} "
              f"all-in-one={o['all_in_one_unit_share']} VALID_JOBS={o['valid_jobs']} jobs>=2 selling={o['jobs_ge2_selling']} C/P/S={o['complementary']}/{o['partial']}/{o['substitute']} "
              f"young={o['young_pool']} winners={o['young_winners']} (new {o['young_winner_new']}) dup={o['young_dup_pairs']}")
        for j, v in o['jobs'].items():
            print(f"   [{'V' if v['valid'] else ' '}{'C' if j in o['credible_jobs'] else ' '}] {j:42} sell={v['selling_shops']:>2} clean={v['clean_shops']:>2} act={v['active_shops']:>2} units={v['units']:>5} "
                  f"yW={v['young_winners']:>2}/{v['young_listings']:>2} dup={v['young_dup_pairs']:>2} med${v['price_median']} {v['relationship']} | {v['brand_fit']}")
        print(f"   credible={len(o['credible_jobs'])} complementary={o['credible_complementary']} flood={o['flood_rating']} <$5={o['under5_unit_share']} substitute={o['substitute_unit_share']}")
        for g, ok in o['gates'].items(): print(f"      {'PASS' if ok else 'FAIL'}  {g}")
        print(f"   => {'PASSES ALL GATES' if o['passes'] else 'DOES NOT PASS'}")
    winners = [n for n, o in out.items() if o['passes']]
    print('\nPROVISIONAL MARKET =', winners[0] if len(winners) == 1 else ('TIE: ' + ', '.join(winners) if winners else 'NONE'))
