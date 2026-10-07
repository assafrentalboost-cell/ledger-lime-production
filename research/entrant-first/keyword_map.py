"""Keyword maps for the top 3 clusters (Step 10). EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.
Dedupe logic (deterministic):
  1. drop typo artefacts: competition < 100, OR another term within 10% volume has >= 10x the competition
     (EverBee echoes a misspelling with the parent term's volume but few listings: 'ad hd', 'weds planner', 'foodlist')
  2. collapse word-order / plural / spacing variants: signature = sorted set of tokens with a trailing 's' stripped
  3. keep the highest-competition (most common real) spelling per signature; sort by volume desc; cap 30
Volumes are EverBee estimates and have been 10-25x off official Insights before (Dept #1). They map doors; they do not size demand."""
import json, os, glob, re
H = os.path.dirname(os.path.abspath(__file__))
def num(s):
    try: return float(str(s).replace(',', ''))
    except: return 0.0
SEEDS = {'ADHD_ADULT': ['adhd', 'adhd-budget', 'adhd-cleaning', 'adhd-brain-dump', 'adhd-bill-tracker', 'adhd-notion'],
         'WEDDING_PLAN_ADMIN': ['wedding-planner', 'wedding-budget-spreadsheet'],
         'DIET_CONDITION': ['food-list', 'diabetic-food-list']}
DROP = {'WEDDING_PLAN_ADMIN': re.compile(r'gift|red\b|planly', re.I)}  # gift intent = buying for a planner, not planning
def sig(k): return tuple(sorted({re.sub(r's$', '', t) for t in re.findall(r'[a-z0-9]+', k.lower())}))
def build(c):
    rows = []
    for s in SEEDS[c]:
        rows += json.load(open(os.path.join(H, 'raw', f'K-{s}.json')))['rows']
    def echo(r):
        v, k = num(r['new_volume']), num(r['competition'])
        return any(o is not r and abs(num(o['new_volume']) - v) <= 0.10 * v and num(o['competition']) >= 10 * k for o in rows)
    best = {}
    for r in rows:
        if num(r['competition']) < 100 or echo(r) or (c in DROP and DROP[c].search(r['keyword'])): continue
        g = sig(r['keyword'])
        if g not in best or num(r['competition']) > num(best[g]['competition']): best[g] = r
    return sorted(best.values(), key=lambda r: -num(r['new_volume']))[:30]
if __name__ == '__main__':
    out = {c: build(c) for c in SEEDS}
    json.dump(out, open(os.path.join(H, 'keyword_map.json'), 'w'), indent=1)
    for c, L in out.items():
        print(f'\n## {c} ({len(L)} terms)')
        for r in L: print(f"  {r['keyword']:55} vol={r['new_volume']:>6} comp={r['competition']}")
