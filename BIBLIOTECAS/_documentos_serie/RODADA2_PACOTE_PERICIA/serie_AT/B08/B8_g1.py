#!/usr/bin/env python3
# B8 — G1: DOI[aid] -> esearch; esummary lote; efetch abstracts; conferência de rótulos
import json, time, urllib.request, urllib.parse, xml.etree.ElementTree as ET, re

BASE='/home/user/BIBLIOTECAS/B08_Micronutrientes'
entries=json.load(open(f'{BASE}/producao/insumos/b8_anexo_entries.json'))
UA={'User-Agent':'arena-b8-audit/1.0 (contact: research)'}
def get(url, data=None):
    req=urllib.request.Request(url, data=data, headers=UA)
    for tent in range(4):
        try: return urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:
            if tent==3: raise
            time.sleep(1.5*(tent+1))
def esearch(doi):
    q=urllib.parse.quote(f'{doi}[aid]')
    x=ET.fromstring(get(f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={q}&retmode=xml'))
    ids=[i.text for i in x.iter('Id')]
    return ids
def esummary(ids):
    if not ids: return {}
    url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi'
    raw=get(url, data=f'db=pubmed&id={",".join(ids)}&retmode=json'.encode())
    return json.loads(raw)['result']

ok={}; falha={}
for e in entries:
    doi=e['doi']
    if not doi:
        falha[f'sem-doi:{e["decl_autor"]} {e["decl_ano"]}']={'motivo':'sem DOI no anexo'}
        continue
    try:
        ids=esearch(doi)
    except Exception as ex:
        falha[f'doi:{doi}']={'motivo':f'esearch erro {ex}'}; continue
    if not ids:
        falha[f'doi:{doi}']={'motivo':'DOI sem hit no PubMed','decl':(e['decl_autor'],e['decl_ano'],e['decl_titulo'][:80])}
    else:
        e['_pmid']=ids[0]
    time.sleep(0.34)
print('hits:',sum(1 for e in entries if e.get('_pmid')),'falhas:',len(falha))

pmids=[e['_pmid'] for e in entries if e.get('_pmid')]
meta={}
for i in range(0,len(pmids),50):
    r=esummary(pmids[i:i+50])
    for pid in pmids[i:i+50]:
        d=r[pid]
        a1=(d['authors'][0]['name'] if d.get('authors') else '?')
        meta[pid]={'real_a1':a1,'real_ano':(d.get('pubdate','')[:4]),'real_titulo':d.get('title','').rstrip('.'),
                   'fonte':d.get('fulljournalname') or d.get('source'),'pubtype':d.get('pubtype',[])}
    time.sleep(0.4)

for e in entries:
    pid=e.get('_pmid')
    if pid and pid in meta:
        m=meta[pid]; e.update({'pmid':pid,**m})

# conferência de rótulos autor/ano
def norm(s): return re.sub(r'[^a-z]','', (s or '').lower())
alertas=[]
for e in entries:
    if not e.get('pmid'): continue
    da,ra=e['decl_autor'],e['real_a1']
    n1,n2=norm(da),norm(ra)
    if n1[:5]!=n2[:5]:
        alertas.append((e['decl_autor'],e['decl_ano'],'->',ra,e['real_ano'],e['real_titulo'][:60]))
    elif e['decl_ano']!=e['real_ano'] and e['decl_ano']!='?':
        alertas.append(('ANO',e['decl_autor'],e['decl_ano'],'->',ra,e['real_ano'],e['real_titulo'][:60]))
print('alertas rótulo:',len(alertas))
for a in alertas: print(' ',a)

# efetch abstracts
ids=[e['pmid'] for e in entries if e.get('pmid')]
absx={}
for i in range(0,len(ids),30):
    raw=get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',
            data=f'db=pubmed&id={",".join(ids[i:i+30])}&rettype=abstract&retmode=xml'.encode())
    root=ET.fromstring(raw)
    for a in root.iter('PubmedArticle'):
        pm=a.findtext('.//PMID')
        txt=' '.join(''.join(x.itertext()) for x in a.findall('.//Abstract/AbstractText')).strip()
        absx[pm]={'abstract':txt}
    time.sleep(0.5)
sem_abs=[e['pmid'] for e in entries if e.get('pmid') and not absx.get(e['pmid'],{}).get('abstract')]
print('sem abstract:',[(e['decl_autor'],e['decl_ano'],e['pmid']) for e in entries if e.get('pmid') and not absx.get(e['pmid'],{}).get('abstract')])

json.dump({'ok':{f"doi:{e['doi']}":e for e in entries if e.get('pmid')},
           'falha':falha,'por_pmid':{},'abstracts':absx},
          open(f'{BASE}/producao/insumos/matriz_b8_g1.json','w'), ensure_ascii=False, indent=1)
print('G1 gravado. ok=',len([e for e in entries if e.get('pmid')]),'falha=',len(falha))
