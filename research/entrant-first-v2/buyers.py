"""Stage 2: group entrant listings by EXACT buyer. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.

Each passing listing (CLEAN / NEAR-CLEAN) gets the FIRST buyer rule whose regex matches its title. Rule order puts
merch/decor/design-asset intent (bought BY a fan or gifter, not BY the professional) ahead of professional buyers, so a
"Nurse PNG tumbler wrap" is NOT counted as a nurse-workflow purchase.

Per buyer: clean_shops, active_shops (ACTIVE health), units, top_shop_share, price bands (unit share), median price.
`status` labels: EXCLUDED_BY_BRIEF (ADHD / clinical-therapy / notary / household-readiness paths),
LIVE_LL (L&L already sells it: budget #1-#7, co-parenting #17, wedding budget #9, reseller #14, home bakery #15),
VAGUE (buyer too broad per brief), DESIGN (decor/craft/merch, not an admin buyer), CANDIDATE."""
import json, os, re, statistics
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__))

BUYERS = [  # (buyer, status, regex) — first match wins
 ('IP / fan merch', 'DESIGN', r'pok[eé]mon|pok[eé]dex|\bpkmn\b|ms rachel|toy story|mcqueen|frozen|sonic|winnie|pooh|elmo|disney|bluey|monopoly'),
 ('Merch / decor / design assets (any buyer)', 'DESIGN', r'\bpng\b|\bsvg\b|clip ?art|sublimation|tumbler|mug wrap|embroidery|\bstl\b|laser|wall art|poster|print set|preset|\bluts?\b|mockup|sticker|shirt|t-shirt|monogram|cricut|font'),
 ('Crafter (patterns)', 'DESIGN', r'crochet|knit|sewing|pattern|quilt|cross stitch|amigurumi|woodworking|plans \(pdf\)|build plans'),
 ('ADHD adult (excluded by brief)', 'EXCLUDED_BY_BRIEF', r'adhd|neurodivergent|executive function'),
 ('Therapist / BCBA / counselor (excluded: Dept #2 clinical path)', 'EXCLUDED_BY_BRIEF', r'therap|bcba|\baba\b|rbt\b|counsel|lcsw|lpc\b|dsm|iep|speech'),
 ('Notary (excluded: Dept #2)', 'EXCLUDED_BY_BRIEF', r'notary|loan signing'),
 ('Household readiness / end-of-life (excluded: Dept #1)', 'EXCLUDED_BY_BRIEF', r'end of life|emergency binder|just in case|death binder|in case of emergency|household binder|home management'),
 ('Separated parent (co-parenting #17 live)', 'LIVE_LL', r'co-?parent|custody|visitation|parenting time'),
 ('Household budgeter (#1-#7 live)', 'LIVE_LL', r'budget|debt|savings|sinking fund|paycheck|bill tracker|net worth|finance dashboard'),
 ('Online reseller (#14 live)', 'LIVE_LL', r'reseller|ebay|poshmark|depop|vinted|mercari'),
 ('Home baker (#15 live)', 'LIVE_LL', r'bakery|recipe cost|cottage food|baker'),
 ('Nurse / nursing student', 'CANDIDATE', r'\bnurs(e|es|ing)\b|\brn\b|sbar|head.to.toe|nclex|\bcna\b|\blpn\b|ccrn|report sheet|brain sheet|medsurg|med surg'),
 ('Allied-health student (non-nursing)', 'CANDIDATE', r'anatomy|pharmacolog|phlebotomy|medical (coding|terminology|assistant)|radiolog|laboratory science|\bbls\b|study guide|cheat sheet|flashcards'),
 ('Real estate agent', 'CANDIDATE', r'realtor|real estate|open house|listing presentation|pre-listing|buyer (guide|questionnaire|consultation|roadmap|packet)|seller guide|broker|farming|just listed|closing day'),
 ('Esthetician / lash / nail / hair pro', 'CANDIDATE', r'\besthetic|salon|\blash|nail tech|hair ?stylist|braid|\bbrow|\bwax|\bmua\b|makeup artist|spray tan|med ?spa|\bwig|hair vendor|booking (flyer|site|website)|acuity|aftercare|beauty (salon|business)'),
 ('Home daycare / childcare provider', 'CANDIDATE', r'daycare|childcare|child care|in-home|preschool forms|infant daily report|daily report'),
 ('Engaged couple (wedding admin)', 'CANDIDATE', r'wedding.*(planner|planning|spreadsheet|binder|checklist|timeline|guest list|itinerary|day.of|blueprint|budget)|bachelorette.*itinerary|bridesmaid.*questionnaire'),
 ('Wedding guest-facing decor', 'DESIGN', r'wedding|bridal|bride|save.the.date|rsvp|bachelorette|engagement'),
 ('Landlord (legal forms)', 'CANDIDATE', r'landlord|tenant|lease|rental (agreement|application|contract)|eviction|rent receipt|notice to vacate|roommate'),
 ('Short-term rental host', 'CANDIDATE', r'airbnb|vacation rental|welcome book|guest guide|house manual|superhost'),
 ('Photographer', 'CANDIDATE', r'photograph'),
 ('Cleaning-business owner', 'CANDIDATE', r'cleaning (service|business|company)|housekeeper|maid|walkthrough folder|new client packet'),
 ('Teacher (classroom)', 'CANDIDATE', r'teacher|classroom|bulletin board|lesson plan|gradebook|sub plan|end of (the )?year'),
 ('Homeschool parent', 'CANDIDATE', r'homeschool'),
 ('Caregiver (#11/#16 adjacent)', 'LIVE_LL', r'caregiver|medication|care plan|\bmar\b|medical binder|medical log'),
 ('Expecting / new parent', 'VAGUE', r'birth plan|pregnancy|baby|newborn|first foods|nursery'),
 ('Traveler', 'VAGUE', r'travel|trip|itinerary|vacation'),
 ('Student (general)', 'VAGUE', r'student|study|college|university|academic'),
 ('Productivity planner user', 'VAGUE', r'notion|planner|journal|habit|goodnotes|to do|tracker'),
 ('Kids learning / party host', 'DESIGN', r'worksheet|preschool|curriculum|tracing|coloring|activit|craft|invitation|invite|birthday|party|game|card|tag|label|template|flyer|logo|instagram|canva'),
]
BUYERS = [(b, s, re.compile(rx, re.I)) for b, s, rx in BUYERS]
def assign(title):
    for b, s, rx in BUYERS:
        if rx.search(title): return b, s
    return 'Unassigned', 'VAGUE'

BANDS = [('<$5', 0, 5), ('$5-9.99', 5, 10), ('$10-14.99', 10, 15), ('$15-24.99', 15, 25), ('$25+', 25, 1e9)]
def bands(L):
    U = sum(r['units'] for r in L) or 1
    return {k: round(sum(r['units'] for r in L if lo <= r['price'] < hi) / U, 3) for k, lo, hi in BANDS}

def build():
    rows = json.load(open(os.path.join(H, 'all_listings_classified.json')))
    ok = [r for r in rows if r['status'] != 'REJECT']
    G = defaultdict(list)
    for r in ok:
        b, s = assign(r['title']); r['buyer'] = b; r['buyer_status'] = s; G[b].append(r)
    out = {}
    for b, L in G.items():
        su = defaultdict(float)
        for r in L: su[r['shop']] += r['units']
        U = sum(su.values()); top = max(su, key=su.get)
        out[b] = dict(buyer=b, status=L[0]['buyer_status'], listings=len(L), shops=len(su),
                      clean_shops=len({r['shop'] for r in L if r['status'] == 'CLEAN'}),
                      active_shops=len({r['shop'] for r in L if r['health'] == 'ACTIVE'}),
                      units=int(U), top_shop=top, top_shop_share=round(su[top] / U, 3),
                      median_price=round(statistics.median(r['price'] for r in L), 2), bands=bands(L))
    json.dump(dict(buyers=out, listings=ok), open(os.path.join(H, 'buyers.json'), 'w'), indent=1)
    return out

if __name__ == '__main__':
    out = build()
    print(f"{'buyer':58} {'status':17} {'cln':>3} {'act':>3} {'lst':>4} {'units':>7} {'top%':>5} {'med$':>6}  bands(unit share)")
    for k in sorted(out.values(), key=lambda k: (k['status'] != 'CANDIDATE', -k['clean_shops'])):
        print(f"{k['buyer'][:58]:58} {k['status']:17} {k['clean_shops']:>3} {k['active_shops']:>3} {k['listings']:>4} {k['units']:>7} {k['top_shop_share']*100:>4.0f}% {k['median_price']:>6}  {k['bands']}")
