#!/usr/bin/env python3
# B9 — G1: esearch DOI[aid] -> esummary (validação autor+ano+tema) para as 164 entradas
import json, time, urllib.request, urllib.parse, xml.etree.ElementTree as ET

BASE='/home/user/BIBLIOTECAS/B09_DisfuncaoMitocondrial'
ent=[e for e in json.load(open(f'{BASE}/producao/insumos/b9_anexo_entries.json')) if e.get('doi')]
assert len(ent)==164
EP='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def get(url,tries=3):
    for k in range(tries):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'arena-audit/1.0'})
            return urllib.request.urlopen(req,timeout=60).read()
        except Exception as ex:
            time.sleep(2+2*k)
    return b''
def esearch(term):
    u=EP+'esearch.fcgi?db=pubmed&retmode=json&term='+urllib.parse.quote(term)
    try: return json.loads(get(u))['esearchresult']['idlist']
    except Exception: return []
def esummary(ids):
    u=EP+'esummary.fcgi?db=pubmed&retmode=json&id='+','.join(ids)
    try: return json.loads(get(u))['result']
    except Exception: return {}

out={}; fails=[]
for i,e in enumerate(ent):
    doi=e['doi']; ids=esearch(f'{doi}[aid]')
    pmid=ids[0] if ids else None
    rec={'decl':e,'pmid':pmid,'via':'esearch DOI[aid]'}
    out[doi]=rec
    if not pmid: fails.append(doi)
    if i%10==0: time.sleep(0.4); print(i+1,'/',len(ent),'pmids ok:',len(ent)-len(fails))
print('RESOLVIDOS:',len(ent)-len(fails),'| FALHAS:',len(fails),fails)

# esummary em lotes para validar autor+ano+titulo
pmids=[r['pmid'] for r in out.values() if r['pmid']]
summ={}
for i in range(0,len(pmids),40):
    r=esummary(pmids[i:i+40])
    for uid in r.get('uids',[]):
        it=r[uid]
        a1=it['authors'][0]['name'] if it.get('authors') else ''
        summ[uid]={'real_a1':a1,'real_ano':(it.get('pubdate') or '')[:4],'real_titulo':it.get('title',''),
                   'fonte':it.get('fulljournalname',''),'sortpubdate':it.get('sortpubdate',''),'epubdate':it.get('epubdate','')}
    time.sleep(0.5)
for r in out.values():
    if r['pmid']: r.update(summ.get(r['pmid'],{}))

# validação decl vs real
alertas=[]
for r in out.values():
    if not r['pmid']: continue
    d=r['decl']['decl_autor'].lower().replace('-','').replace('ü','u').replace('ä','a').replace('ö','o').replace('é','e').replace('è','e').replace('ç','c').replace('í','i').replace('ó','o').replace('á','a').replace('ã','a').replace('ñ','n')
    r1=(r.get('real_a1') or '').split()[0].lower().replace('-','').replace('ü','u').replace('ä','a').replace('ö','o').replace('é','e').replace('ç','c')
    y_d=r['decl']['decl_ano']; y_r=r.get('real_ano','')
    y_ep=(r.get('epubdate') or '')[:4]
    ok_a = d in r1 or r1 in d
    ok_y = y_d==y_r or y_d==y_ep
    r['autor_ok']=ok_a; r['ano_ok']=ok_y
    if not (ok_a and ok_y):
        alertas.append((r['pmid'],d,r1,y_d,y_r,y_ep,r['decl']['decl_titulo'][:60],(r.get('real_titulo') or '')[:60]))
print('ALERTAS decl≠real:',len(alertas))
for a in alertas: print('  ',a)
json.dump({'ok':out,'falha_doi':fails}, open(f'{BASE}/producao/insumos/matriz_b9_g1.json','w'), ensure_ascii=False, indent=1)
print('gravado matriz_b9_g1.json')
