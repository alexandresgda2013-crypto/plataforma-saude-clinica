#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G1 da B13: valida os PMIDs do Briefing (tabelas A-Q) via eutils."""
import json,urllib.request,urllib.parse,time,unicodedata,re
def sa(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c)).lower()
BASE='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def esum(ids):
    u=BASE+'esummary.fcgi?'+urllib.parse.urlencode({'db':'pubmed','id':','.join(ids),'retmode':'json'})
    for _ in range(3):
        try:
            time.sleep(0.3); d=json.load(urllib.request.urlopen(u,timeout=40))['result']
            return {i:d[i] for i in ids if i in d}
        except Exception: time.sleep(1.5)
    return {}
tabela=json.load(open('/tmp/b13_tabela.json'))
pmids=[r['pmid'] for r in tabela]
meta={}
for i in range(0,len(pmids),50):
    meta.update(esum(pmids[i:i+50]))
res={}; falt=[]
for r in tabela:
    p=r['pmid']
    if p in meta:
        m=meta[p]
        res[p]={'pmid':p,'title':m.get('title','').rstrip('.'),'journal':m.get('fulljournalname',m.get('source','')),
                'pubdate':m.get('pubdate',''),'authors':[a['name'] for a in m.get('authors',[])[:6]],
                'tema':r['tema'],'autor_ano':r['autor'],'tipo':r['tipo']}
    else: falt.append(p)
json.dump(res,open('/home/user/BIBLIOTECAS/B13_SistemaEndocanabinoide/producao/g1_resolvidos.json','w'),ensure_ascii=False,indent=1)
json.dump(falt,open('/home/user/BIBLIOTECAS/B13_SistemaEndocanabinoide/producao/g1_sem.json','w'))
print('validados:',len(res),'| sem:',len(falt),falt)
