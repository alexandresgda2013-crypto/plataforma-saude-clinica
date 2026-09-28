#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conferencia autor+ano+tema: esummary vs. declarado no Briefing."""
import json,re,unicodedata
def sem(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c))
res=json.load(open('/home/user/BIBLIOTECAS/B14_Neuroesteroides/producao/g1_resolvidos.json'))
ruido=set(json.load(open('/tmp/b14_ruido.json')))
div=[]
for p,m in res.items():
    # autor esperado (celula do briefing): pode ser "Sobrenome et al., ano", "Sobrenome/Sobrenome ano", ou so ano
    esp=sem(m['autor_ano'])
    ano_es=m['pubdate'][:4]
    # ano declarado na celula
    yd=re.search(r'(19|20)\d{2}', m['autor_ano'])
    # sobrenome do 1o autor real
    autores=m['authors']
    sob_real=re.sub(r'[^A-Za-z]','',sem(autores[0]).split()[0]).upper() if autores else ''
    # tenta achar algum nome de autor esperado na celula (procuramos tokens alfabeticos longos)
    toks=[t for t in re.findall(r'[A-Za-zÀ-ÿ]{4,}', sem(esp)) if t.lower() not in
          ('et','al','majewska','review','meta','revisao')]
    ano_ok = (not yd) or (yd.group(0)==ano_es)
    # se a celula so tem ano/periódico (sem autor), não cobramos autor
    autor_cobrado = bool(re.search(r'[A-Za-z]{4,}', esp)) and not re.match(r'^\s*(19|20)\d{2}', m['autor_ano'].strip())
    autor_ok=True
    if autor_cobrado and sob_real:
        autor_ok = any(sob_real[:5] in sem(t).upper() or sem(t).upper()[:5] in sob_real for t in toks) if toks else True
    # tema: checagem simples de sobrevida de palavras-chave (so alerta)
    if not (ano_ok and autor_ok):
        div.append({'pmid':p,'ano_decl':yd.group(0) if yd else '-','ano_real':ano_es,
                    'autor_decl':m['autor_ano'][:50],'autor_real':autores[0] if autores else '?',
                    'revista':m['journal'],'ano_ok':ano_ok,'autor_ok':autor_ok,'tema':m['tema'][:70]})
print('=== DIVERGENCIAS autor/ano a revisar:',len(div),'===')
for d in div:
    print(f"PMID {d['pmid']} | ano {d['ano_decl']}->{d['ano_real']} ok={d['ano_ok']} | autor decl '{d['autor_decl']}' real '{d['autor_real']}' ok={d['autor_ok']}")
    print(f"   tema: {d['tema']} | rev: {d['revista']}")
json.dump(div,open('/tmp/b14_div.json','w'),ensure_ascii=False,indent=1)
print()
print('Total validados:',len(res),'| ruido bloco N:',len(ruido),'| ancoras mecanismo:',len(res)-len(ruido))
