#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrai todas as ancoras (PMIDs) das tabelas do Briefing B14, com bloco/tema/autor/tipo."""
import re, json, unicodedata
def sem(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c))

BR='/home/user/BIBLIOTECAS/B14_Neuroesteroides/producao/rodada1_gpm/BRIEFING_B14.md'
lines=open(BR,encoding='utf-8').read().splitlines()

bloco='?'
rows=[]
hdr_re=re.compile(r'^###?\s+([A-Q])\.')          # ### A. ...  ou **O1.**
subhdr_re=re.compile(r'\*\*([OQP][0-9])\.')
pmid_re=re.compile(r'\b(\d{7,8})\b')

for ln in lines:
    m=hdr_re.match(ln.strip())
    if m: bloco=m.group(1)
    m2=re.search(r'\*\*([OPQ][0-9])\.', ln)
    sub = m2.group(1) if m2 else bloco
    if not ln.strip().startswith('|'): continue
    cells=[c.strip() for c in ln.strip().strip('|').split('|')]
    if len(cells)<3: continue
    # pula cabecalhos e separadores
    joined=' '.join(cells).lower()
    if 'tema' in joined and ('pmid' in joined or 'autor' in joined): continue
    if set(joined.replace(' ','').replace('-',''))<=set(':|-'): continue
    tema=re.sub(r'\*+','',cells[0]).strip()
    autor=re.sub(r'\*+','',cells[1]).strip() if len(cells)>1 else ''
    # procura PMID em qualquer celula
    pmids=pmid_re.findall(' '.join(cells))
    tipo=re.sub(r'\*+','',cells[-1]).strip()
    for p in pmids:
        rows.append({'pmid':p,'bloco':sub,'tema':tema,'autor':autor,'tipo':tipo})

# deduplica por pmid (mantem primeira ocorrencia, mas registra blocos)
by={}
for r in rows:
    if r['pmid'] in by:
        if r['bloco'] not in by[r['pmid']]['blocos']:
            by[r['pmid']]['blocos'].append(r['bloco'])
    else:
        r['blocos']=[r['bloco']]; del r['bloco']; by[r['pmid']]=r

tabela=list(by.values())
print('PMIDs unicos extraidos das tabelas:', len(tabela))
from collections import Counter
print('Por bloco (primeira ocorrencia):', Counter(r['blocos'][0] for r in tabela))

# Bloco N = ruido de intervencao (acupuntura/TCM/fitoterapico/natural) -> marcar como ruido
RUIM_KW=['acupunt','cannh','hemp','cânhamo','canhamo','shuyu','crisina','isoflav','soja',
         'nutricion','exercicio','exerc[íi]cio','mente-corpo','fitoterap','oleo de semente']
ruim=[]
for r in tabela:
    txt=sem((r['tema']+' '+r['tipo'])).lower()
    if r['blocos'][0]=='N' or any(re.search(k,txt) for k in RUIM_KW):
        ruim.append(r['pmid'])
print('PMIDs de RUIDO (bloco N / intervencao nao-mecanismo):', len(ruim), ruim)

json.dump(tabela, open('/tmp/b14_tabela.json','w'), ensure_ascii=False, indent=1)
json.dump(ruim, open('/tmp/b14_ruido.json','w'))
print('--- amostra 3 ---')
for r in tabela[:3]: print(r['pmid'], r['blocos'], '|', r['autor'][:40], '|', r['tema'][:60])
