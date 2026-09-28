#!/usr/bin/env python3
# B9 — G1b: busca dirigida dos 3 DOI-falhos + conferências efetch (29801445; 21145355; 35732695; Lu2024; european psychiatry)
import json, time, urllib.request, urllib.parse, xml.etree.ElementTree as ET

EP='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def get(url,tries=3):
    for k in range(tries):
        try: return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'arena-audit/1.0'}),timeout=60).read()
        except Exception: time.sleep(2+2*k)
    return b''
def esearch(term):
    try: return json.loads(get(EP+'esearch.fcgi?db=pubmed&retmode=json&term='+urllib.parse.quote(term)))['esearchresult']['idlist']
    except Exception: return []
def efetch(ids):
    raw=get(EP+'efetch.fcgi?db=pubmed&id='+','.join(ids)+'&rettype=abstract&retmode=xml')
    root=ET.fromstring(raw)
    r={}
    for a in root.iter('PubmedArticle'):
        pm=a.findtext('.//PMID'); r[pm]=a
    return r

# 1) qual entrada decl tinha o DOI falho 10.1192/j.eurpsy.2023.1449 ?
ent=json.load(open('/home/user/BIBLIOTECAS/B09_DisfuncaoMitocondrial/producao/insumos/b9_anexo_entries.json'))
for e in ent:
    if e.get('doi')=='10.1192/j.eurpsy.2023.1449':
        print('DOI falho é:', e['decl_autor'], e['decl_ano'], '|', e['decl_titulo'][:120])
        titulo=e['decl_titulo']; a1=e['decl_autor']

# 2) busca dirigida por título
ids=esearch(f'"{titulo}"[Title]')
print('busca por título ->', ids)
if not ids:
    ids=esearch(titulo.split(':')[0].replace('"','')+'[Title] AND '+a1.split(',')[0]+'[Author]')
    print('busca alternativa ->', ids)

# 3) efetch checks
checks=[i for i in ['29801445','21145355','35732695','39197553','39684566'] ]
art=efetch(checks+ids[:1])
for pm in checks+ids[:1]:
    if pm not in art: print(pm,'SEM REGISTRO'); continue
    a=art[pm]
    auths=[(au.findtext('LastName') or '')+' '+(au.findtext('Initials') or '') for au in a.findall('.//Article/AuthorList/Author')]
    ttl=''.join(a.find('.//Article/ArticleTitle').itertext())
    iso=a.findtext('.//Article/Journal/ISOAbbreviation')
    pd=a.find('.//Article/Journal/JournalIssue/PubDate')
    pyr=pd.findtext('Year') if pd is not None else None
    if not pyr and pd is not None: pyr=(pd.findtext('MedlineDate') or '')[:4]
    doi=''
    for aid in a.findall('.//PubmedData/ArticleIdList/ArticleId'):
        if aid.get('IdType')=='doi': doi=aid.text
    abs_=' '.join(''.join(x.itertext()) for x in a.findall('.//Abstract/AbstractText'))
    print('---',pm,'| print',pyr,'|',iso,'| doi',doi)
    print('   A1..A3:',auths[:3],'| n autores',len(auths))
    print('   título:',ttl[:130])
    print('   abs[:300]:',abs_[:300])
