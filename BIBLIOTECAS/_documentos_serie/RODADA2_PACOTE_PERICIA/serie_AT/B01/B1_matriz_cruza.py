#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cruza insumo MATRIZ B1 vs B1 V3 CANONICA: (1) verificacao autor/ano dos resolvidos;
(2) cobertura ja existente; (3) busca dos declassados sem ID."""
import json,re,unicodedata,urllib.request,urllib.parse,time
def sem(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c)).lower()
res=json.load(open('/home/user/BIBLIOTECAS/B01_Neuroinflamacao/producao/insumos/matriz_b1_g1.json'))
b1=json.load(open('/home/user/BIBLIOTECAS/B01_Neuroinflamacao/Evidencias/Bibliografia/01_pmids.json'))
b1refs=b1 if isinstance(b1,list) else list(b1.values())
b1pmids={str(r.get('pmid_oficial')) for r in b1refs}
# sobrenomes presentes na B1 (para achar cobertura por label mesmo se pmid difere)
print('=== VERIFICACAO AUTOR/ANO (insumo x PubMed) ===')
mismatch=[]
for ident,m in res.items():
    decl=m['declarado']; sob=decl.split()[0].replace('&','').replace('et','').strip()
    ano=re.search(r'(19|20)\d{2}',decl)
    ano=ano.group(0) if ano else ''
    autores=[a for a in m.get('authors',[])]
    ano_pub=(m.get('pubdate') or '')[:4]
    ok_sob=any(sem(sob)[:6] in sem(a) for a in autores) or sem(sob) in sem(m.get('title','')) or sob.lower() in ('pyroptose','nlrp3','il-33','fluoxetina')
    ok_ano=(not ano) or (ano_pub==ano) or (ano in ('2025','2026') and ano_pub in ('2025','2026'))
    if not ok_sob or (ano and ano_pub and ano!=ano_pub and abs(int(ano_pub)-int(ano))>1 and ano not in ('2025','2026')):
        mismatch.append((ident,m['pmid'],decl,'->',autores[0] if autores else '?',ano_pub,(m.get('title') or '')[:70]))
for x in mismatch: print(' MISMATCH:',x)
print(len(mismatch),'incompatibilidades autor/ano')
print()
print('=== COBERTURA NA B1 V3 ===')
novos=[]; cobertos=[]
for ident,m in res.items():
    if m['pmid'] in b1pmids: cobertos.append((m['bloco'],m['pmid'],m['declarado']))
    else: novos.append((m['bloco'],m['pmid'],m['declarado'],(m.get('title') or '')[:64]))
print('JA COBERTOS:',len(cobertos))
for x in cobertos: print('  ',x[0],'|',x[1],'|',x[2])
print()
print('NOVOS (nao estao na B1):',len(novos))
for x in novos: print('  ',x[0],'|',x[1],'|',x[2],'|',x[3])
json.dump({'cobertos':[list(c) for c in cobertos],'novos':[list(n) for n in novos],'mismatch':mismatch},
          open('/home/user/BIBLIOTECAS/B01_Neuroinflamacao/producao/insumos/matriz_b1_cruzamento.json','w'),ensure_ascii=False,indent=1)
# === classico sem ID: busca esearch autor+ano+palavra ===
BASE='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def esearch(term):
    u=BASE+'esearch.fcgi?'+urllib.parse.urlencode({'db':'pubmed','term':term,'retmode':'json'})
    for _ in range(3):
        try:
            time.sleep(0.34); return json.load(urllib.request.urlopen(u,timeout=30))['esearchresult']['idlist']
        except Exception: time.sleep(1.2)
    return []
BUSCAS={
'Dantzer & Walker 2014':'Dantzer R[au] AND Walker AK[au] AND 2014[dp]',
'Bay-Richter 2014':'Bay-Richter C[au] AND 2014[dp]',
'Müller & Schwarz 2007':'Muller N[au] AND Schwarz M[au] AND 2007[dp] AND (immune OR serotonin OR glutamate)',
'Serafini 2017':'Serafini G[au] AND 2017[dp] AND (inflammation OR cytokines) AND suicide',
'Bryleva & Brundin 2016':'Bryleva E[au] AND Brundin L[au] AND 2016[dp]',
'Parrott 2016 check':'Parrott JM[au] AND 2016[dp] AND kynurenine',
}
print()
print('=== CLASSICOS SEM ID (esearch dirigida) ===')
for nome,q in BUSCAS.items():
    ids=esearch(q)
    flag='(JA NA B1)' if ids and ids[0] in b1pmids else ''
    print(f"  {nome:28s} -> {ids[:3]} {flag}")
