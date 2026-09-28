#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrai as ancoras (PMIDs) das tabelas A-N do Briefing B16."""
import re, json
BR='/home/user/BIBLIOTECAS/B16_Neurogenese/producao/rodada1_gpm/BRIEFING_B16.md'
lines=open(BR,encoding='utf-8').read().splitlines()
bloco='?'; rows=[]
hdr=re.compile(r'^###?\s+([A-N])\.')
pmid_re=re.compile(r'\b(\d{7,8})\b')
for ln in lines:
    m=hdr.match(ln.strip())
    if m: bloco=m.group(1)
    if not ln.strip().startswith('|'): continue
    cells=[c.strip() for c in ln.strip().strip('|').split('|')]
    if len(cells)<3: continue
    joined=' '.join(cells).lower()
    if 'tema' in joined and ('pmid' in joined or 'autor' in joined): continue
    if set(joined.replace(' ','').replace('-',''))<=set(':|-'): continue
    tema=re.sub(r'\*+','',cells[0]).strip()
    autor=re.sub(r'\*+','',cells[1]).strip() if len(cells)>1 else ''
    tipo=re.sub(r'\*+','',cells[-1]).strip()
    for p in pmid_re.findall(' '.join(cells)):
        rows.append({'pmid':p,'bloco':bloco,'tema':tema,'autor':autor,'tipo':tipo})
by={}
for r in rows:
    if r['pmid'] in by:
        if r['bloco'] not in by[r['pmid']]['blocos']: by[r['pmid']]['blocos'].append(r['bloco'])
    else:
        r['blocos']=[r['bloco']]; del r['bloco']; by[r['pmid']]=r
tabela=list(by.values())
print('PMIDs unicos extraidos:',len(tabela))
from collections import Counter
print('Por bloco:',dict(Counter(r['blocos'][0] for r in tabela)))
json.dump(tabela,open('/tmp/b16_tabela.json','w'),ensure_ascii=False,indent=1)
for r in tabela[:5]: print(r['pmid'],r['blocos'],'|',r['autor'][:40],'|',r['tema'][:55])
