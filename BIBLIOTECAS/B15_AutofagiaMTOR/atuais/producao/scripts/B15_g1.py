#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G1 da B15: valida os 140 PMIDs do Briefing via eutils (esummary)."""
import json,urllib.request,urllib.parse,time
BASE='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def esum(ids):
    u=BASE+'esummary.fcgi?'+urllib.parse.urlencode({'db':'pubmed','id':','.join(ids),'retmode':'json'})
    for _ in range(4):
        try:
            time.sleep(0.34); d=json.load(urllib.request.urlopen(u,timeout=45))['result']
            return {i:d[i] for i in ids if i in d}
        except Exception: time.sleep(1.5)
    return {}
tabela=json.load(open('/tmp/b15_tabela.json'))
pmids=[r['pmid'] for r in tabela]
meta={}
for i in range(0,len(pmids),50):
    meta.update(esum(pmids[i:i+50])); print(f'  lote {i//50+1}: acumulado {len(meta)}')
res={}; falt=[]
for r in tabela:
    p=r['pmid']
    if p in meta:
        m=meta[p]
        res[p]={'pmid':p,'title':m.get('title','').rstrip('.'),'journal':m.get('fulljournalname',m.get('source','')),
                'pubdate':m.get('pubdate',''),'authors':[a['name'] for a in m.get('authors',[])[:6]],
                'tema':r['tema'],'autor_ano':r['autor'],'tipo':r['tipo'],'blocos':r['blocos']}
    else: falt.append(p)
out='/home/user/BIBLIOTECAS/B15_AutofagiaMTOR/producao'
json.dump(res,open(out+'/g1_resolvidos.json','w'),ensure_ascii=False,indent=1)
json.dump(falt,open(out+'/g1_sem.json','w'))
print('VALIDADOS:',len(res),'| SEM RESOLUCAO:',len(falt),falt)
