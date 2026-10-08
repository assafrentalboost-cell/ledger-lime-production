"""Stage 13 keyword maps for the 3 strongest finalists. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.
Same dedupe as V1 (research/entrant-first/keyword_map.py): drop competition<100 and typo echoes (another term within 10% volume
with >=10x competition), collapse word-order/plural variants (sorted token set, trailing 's' stripped), keep the most-competed
spelling, sort by volume, cap 30. Then each kept term is mapped to a job door with the finalist's job regexes from jobs.py."""
import json, os, re
from jobs import FIN
H = os.path.dirname(os.path.abspath(__file__))
SEEDS = {'Nurse / nursing student': 'nurse-report-sheet', 'Homeschool parent': 'homeschool-planner', 'Esthetician / lash / nail / hair pro': 'lash-tech'}
def num(s):
    try: return float(str(s).replace(',', ''))
    except: return 0.0
def sig(k): return tuple(sorted({re.sub(r's$', '', t) for t in re.findall(r'[a-z0-9]+', k.lower())}))
def build(name, seed):
    rows = json.load(open(os.path.join(H, 'raw', f'K-{seed}.json')))['rows']
    echo = lambda r: any(o is not r and abs(num(o['new_volume']) - num(r['new_volume'])) <= 0.1 * num(r['new_volume']) and num(o['competition']) >= 10 * num(r['competition']) for o in rows)
    best = {}
    for r in rows:
        if num(r['competition']) < 100 or echo(r): continue
        g = sig(r['keyword'])
        if g not in best or num(r['competition']) > num(best[g]['competition']): best[g] = r
    jobs = [(j, re.compile(rx, re.I)) for j, rx, *_ in FIN[name]['jobs']]
    out = []
    for r in sorted(best.values(), key=lambda r: -num(r['new_volume']))[:30]:
        door = next((j for j, rx in jobs if rx.search(r['keyword'])), '(generic buyer door)')
        out.append(dict(keyword=r['keyword'], volume=r['new_volume'], competition=r['competition'], job_door=door))
    return out
if __name__ == '__main__':
    out = {n: build(n, s) for n, s in SEEDS.items()}
    json.dump(out, open(os.path.join(H, 'keyword_map.json'), 'w'), indent=1)
    for n, L in out.items():
        doors = {}
        for r in L: doors[r['job_door']] = doors.get(r['job_door'], 0) + 1
        print(f'\n## {n}: {len(L)} terms; doors = {doors}')
        for r in L: print(f"  {r['keyword']:45} vol={r['volume']:>6} comp={r['competition']:>7}  -> {r['job_door']}")
