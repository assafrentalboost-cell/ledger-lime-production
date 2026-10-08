"""Rebuild raw/*.json from the session transcript: every EverBee view_listings / view_keyword call made after START.
Inline results are parsed directly; oversized results are read from the tool-results file the harness saved.
usage: python3 -I extract_from_transcript.py <transcript.jsonl> <START_ISO>"""
import json,sys,re,os,hashlib
J,START=sys.argv[1],sys.argv[2]
OUT=os.path.dirname(os.path.abspath(__file__))
uses={};n=0
for line in open(J):
    try: d=json.loads(line)
    except: continue
    c=(d.get('message') or {}).get('content')
    if not isinstance(c,list): continue
    for b in c:
        if b.get('type')=='tool_use' and (b.get('name','').endswith('view_listings') or b.get('name','').endswith('view_keyword')):
            uses[b['id']]=(b['input'],d.get('timestamp') or '')
        if b.get('type')=='tool_result' and b.get('tool_use_id') in uses:
            inp,ts=uses[b['tool_use_id']]
            if ts<START: continue
            cont=b.get('content'); txt=cont if isinstance(cont,str) else ''.join(x.get('text','') for x in cont if isinstance(x,dict))
            m=re.search(r'saved to (\S+\.txt)',txt)
            try: data=json.load(open(m.group(1))) if m else json.loads(txt)
            except Exception as e: print('skip',ts,e); continue
            rows=data['state']['rows']
            for r in rows:
                for k in list(r):
                    if 'image' in k: r.pop(k)
            if 'keyword' in inp:  # EverBee keyword suggestions (view_keyword)
                fn=f"K-{re.sub('[^a-z0-9]+','-',inp['keyword'].lower())}.json"
                json.dump({'label':'EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA','captured':ts,'tool':'view_keyword','keyword':inp['keyword'],'params':inp['params'],'rows':rows},open(os.path.join(OUT,fn),'w'),indent=1)
                n+=1; print(fn,len(rows)); continue
            p=inp['params']; tag=p.get('title_include') or 'broad'
            h=hashlib.md5(json.dumps(p,sort_keys=True).encode()).hexdigest()[:6]
            pre="Q" if p.get("shop_age_month_max") else ("F" if p.get("listing_age_in_months_max") else "X")  # Q = entrant pull, F = young-listing flood pull, X = exploratory any-shop pull
            fn=f"{pre}-{re.sub('[^a-z0-9]+','-',tag.lower())}-p{p.get('page',1)}-{h}.json"
            json.dump({'label':'EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA','captured':ts,'tool':'view_listings','params':p,'rows':rows},open(os.path.join(OUT,fn),'w'),indent=1)
            n+=1; print(fn,len(rows))
print('files',n)
