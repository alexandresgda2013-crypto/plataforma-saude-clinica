#!/usr/bin/env python3
# B7 — cruzamento final: fila 188 x V1 vigente x briefing rodada0 x masters GPM
import json, re

BASE='/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro'
d=json.load(open(f'{BASE}/producao/insumos/matriz_b7_g1.json'))
ok=d['ok']; ab=d['abstracts']; por=d['por_pmid']
entries=json.load(open(f'{BASE}/producao/insumos/b7_anexo_entries.json'))
print('entries:',len(entries), type(entries), json.dumps(entries[0],ensure_ascii=False)[:250] if entries else '')

canon=open(f'{BASE}/B7 EIXO INTESTINO CEREBRO V1 CANONICA.md',encoding='utf-8').read()
# IDs vigentes
refs=sorted(set(re.findall(r'REF_[A-ZÀ-Ü_&\-\.]+_\d{4}[a-z]?', canon)))
print('refs vigentes na V1:', len(refs))

# PMIDs da V1 (do json de pmids)
pmids_v1=set()
try:
    pj=json.load(open(f'{BASE}/Evidencias/Bibliografia/01_pmids.json'))
    def walk(o):
        if isinstance(o,dict):
            for k,v in o.items():
                if 'pmid' in k.lower() and isinstance(v,str): pmids_v1.add(v)
                else: walk(v)
        elif isinstance(o,list):
            for x in o: walk(x)
    walk(pj)
except Exception as e:
    print('pmids json err',e)
print('pmids vigentes:',len(pmids_v1))

# fila 188 = ok(192) + Carabotti(por_pmid) - overlap 5? reconstruir do zero
# masters GPM: coletar pmids master do relatorio anterior (re-derivar do briefing)
brief=open('/home/user/uploads/BRIEFING_B7_EIXO_INTESTINO_CEREBRO_RODADA0.md',encoding='utf-8').read()
# tabela-mestra: linhas com PMID de 8 digitos
mast=re.findall(r'(\b\d{8}\b)', brief)
from collections import Counter
print('pmids no briefing (freq):', Counter(mast).most_common(50))
