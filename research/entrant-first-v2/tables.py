"""Stage 16 tables. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA. Generated from buyers.json / jobs.json; do not hand-edit.
ENTRANT-SHOPS.csv  every shop with a CLEAN or NEAR-CLEAN listing: best listing, buyer, health, queries
BUYER-CLUSTERS.csv every buyer cluster (Stage 2) with status and stats
FINALIST-JOBS.csv  finalist x job: trigger, door, fit, relationship, selling/clean/active shops, health split, young pool, flood, price bands, formats
JOB-EVIDENCE.csv   listing-level evidence behind every finalist job (entrant pool + young winners)
GATES.csv          Stage 15 gate results per finalist"""
import csv, json, os
H = os.path.dirname(os.path.abspath(__file__))
L = 'EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA'
def w(name, rows):
    with open(os.path.join(H, name), 'w', newline='') as f:
        x = csv.writer(f); x.writerow(['data_label'] + list(rows[0])); [x.writerow([L] + list(r.values())) for r in rows]
if __name__ == '__main__':
    B = json.load(open(os.path.join(H, 'buyers.json'))); J = json.load(open(os.path.join(H, 'jobs.json')))
    best = {}
    for r in B['listings']:
        if r['shop'] not in best or r['units'] > best[r['shop']]['units']: best[r['shop']] = r
    w('ENTRANT-SHOPS.csv', [dict(shop=s, shop_age_months=r['shop_age'], shop_total_sales=r['shop_sales'], best_listing_id=r['listing_id'], title=r['title'],
                                 listing_age_months=r['listing_age'], price=r['price'], est_12mo_units=r['units'], trend_12mo=' '.join(map(str, r['trend'])),
                                 last_3=' '.join(map(str, r['last3'])), active_months=r['active'], contribution=r['contrib'], status=r['status'], health=r['health'],
                                 buyer=r['buyer'], buyer_status=r['buyer_status'], queries=';'.join(r['queries']))
                            for s, r in sorted(best.items(), key=lambda x: (x[1]['buyer_status'] != 'CANDIDATE', -x[1]['units']))])
    w('BUYER-CLUSTERS.csv', [dict(buyer=b, status=v['status'], listings=v['listings'], shops=v['shops'], clean_shops=v['clean_shops'], active_shops=v['active_shops'],
                                  units=v['units'], top_shop=v['top_shop'], top_shop_share=v['top_shop_share'], median_price=v['median_price'],
                                  **{'units_' + k: x for k, x in v['bands'].items()}) for b, v in sorted(B['buyers'].items(), key=lambda x: -x[1]['clean_shops'])])
    fj, ev, gt = [], [], []
    for n, o in J.items():
        for j, v in o['jobs'].items():
            fj.append(dict(finalist=n, job=j, trigger=v['trigger'], acquisition_phrase=v['acquisition_phrase'], brand_fit=v['brand_fit'], relationship=v['relationship'],
                           relationship_reason=v['relationship_reason'], valid=v['valid'], credible=j in o['credible_jobs'], selling_shops=v['selling_shops'],
                           clean_shops=v['clean_shops'], active_shops=v['active_shops'], health_active=v['health']['ACTIVE'], health_fading=v['health']['FADING'],
                           health_historic=v['health']['HISTORIC'], health_other=v['health']['OTHER'], units=v['units'], young_listings=v['young_listings'],
                           young_winners=v['young_winners'], young_winner_new_shops=v['young_winner_new_shops'], young_le1mo=v['young_le1mo'],
                           young_dup_pairs=v['young_dup_pairs'], plr=v['plr'], price_median=v['price_median'],
                           **{'units_' + k: x for k, x in v['price_bands'].items()}, formats=json.dumps(v['formats'])))
            for e in v['evidence']: ev.append(dict(finalist=n, job=j, pool='entrant', listing_id=e[0], shop=e[1], price=e[2], units=e[3], status=e[4], health=e[5], shop_age='', title=e[6]))
            for e in v['young_evidence']: ev.append(dict(finalist=n, job=j, pool='young<=3mo winner', listing_id=e[0], shop=e[1], price=e[2], units=e[3], status='', health='', shop_age=e[4], title=e[5]))
        gt.append(dict(finalist=n, credible_jobs=len(o['credible_jobs']), credible_complementary=o['credible_complementary'], flood=o['flood_rating'],
                       under5_unit_share=o['under5_unit_share'], substitute_unit_share=o['substitute_unit_share'],
                       **{g.split(' ')[0]: ok for g, ok in o['gates'].items()}, passes=o['passes']))
    w('FINALIST-JOBS.csv', fj); w('JOB-EVIDENCE.csv', ev); w('GATES.csv', gt)
    print('ENTRANT-SHOPS', len(best), '| candidate-buyer shops', sum(1 for r in best.values() if r['buyer_status'] == 'CANDIDATE'),
          '| BUYER-CLUSTERS', len(B['buyers']), '| FINALIST-JOBS', len(fj), '| JOB-EVIDENCE', len(ev))
