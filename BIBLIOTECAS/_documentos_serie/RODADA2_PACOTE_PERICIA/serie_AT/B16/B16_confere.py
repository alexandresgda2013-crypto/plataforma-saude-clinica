#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere coerencia autor+ano entre rótulo do Briefing e PubMed (G1)."""
import json,re
res=json.load(open('/home/user/BIBLIOTECAS/B16_Neurogenese/producao/g1_resolvidos.json'))
GEN=re.compile(r'^\(?[a-zà-ú0-9 /+\-]*\)?\s*\d{4}',re.I)  # autor genérico vazio tipo '(revisão) 2020'
prob=[]; gen=[]
for p,m in res.items():
    au=m['authors'][0] if m['authors'] else ''
    sob=au.split()[0].lower().replace(',','')
    rot=m['autor_ano']
    sob_rot=rot.split()[0].lower().strip('()*,.')
    ano_pub=(m['pubdate'] or '')[:4]
    m_ano=re.search(r'(19|20)\d{2}',rot)
    ano_rot=m_ano.group(0) if m_ano else '?'
    d1=sob_rot not in sob and sob not in sob_rot
    d2=ano_rot!='?' and ano_pub and ano_rot!=ano_pub
    if '(' in rot.split()[0] or rot[0].isdigit():
        gen.append((p,rot,'->',au,m['pubdate'],m['journal'][:40]))
    elif d1 or d2:
        prob.append((p,rot,'->',au,m['pubdate'],(m['title'] or '')[:70]))
print('AUTOR GENERICO (precisa nome real):',len(gen))
for g in gen: print('  ',g)
print()
print('DIVERGENCIA autor/ano:',len(prob))
for x in prob: print('  ',x)
# ancora-teto check
ANC={'9809557':'Eriksson','23746839':'Spalding','12907793':'Santarelli','29513649':'Sorrells',
'29625071':'Boldrini','30911133':'Moreno-Jimenez','11124987':'Malberg','21814201':'Snyder',
'29950730':'Anacker','29162814':'Ma','38413417':'Rawat','42629468':'Peng','40608919':'Dumitru',
'40957417':'Marquez-Valadez','41741649':'Disouky','41855330':'Ding','41663429':'Ware',
'41249553':'Xu','20862278':'Fuss','18178625':'Koo','22071871':'Zunszain','37790349':'Agrimi','38352378':'Chang'}
print()
print('ANCORAS-TECO:')
for p,esp in ANC.items():
    m=res.get(p)
    if m: print(f"  {p} [{esp}] -> {m['authors'][0] if m['authors'] else '?'} | {m['pubdate']} | {m['journal'][:38]} | {(m['title'] or '')[:60]}")
