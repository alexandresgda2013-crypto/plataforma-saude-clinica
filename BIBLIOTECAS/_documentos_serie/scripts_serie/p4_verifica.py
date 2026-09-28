#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica P-4 (Fidelidade Canonica) itens A/B/C/E para cada biblioteca B1-B14.
Nao autocertifica verdade cientifica; apenas checa condicoes verificaveis por artefato."""
import json,re,glob,os
from pathlib import Path

ROOT=Path('/home/user/BIBLIOTECAS')
def sem(s): return s

def achar(n):
    cands=list(ROOT.glob(f'B{n:02d}_*'))+list(ROOT.glob(f'B{n}_*'))
    return cands[0] if cands else None

TAGre=re.compile(r'([A-Za-zÀ-ÿ0-9_]+)\[(ML|EC|OB|MA|AT)\]')
for n in range(1,15):
    f=achar(n)
    if not f: print(f'B{n}: PASTA NAO ENCONTRADA'); continue
    cans=list(f.glob('*.md'))+list(f.glob('*CANONICA*.md'))
    can=next((p for p in f.glob('*.md') if 'CANONICA' in p.name.upper()), None)
    bib=f/'Evidencias'/'Bibliografia'
    p01=bib/'01_pmids.json'
    vincp=f/'Evidencias'/'Vinculos'/'vinculos_referencia_afirmacao.json'
    # ledger
    led=list(f.glob(f'Auditoria*/ledger_auditoria_B{n}.json'))
    refs=json.load(open(p01)) if p01.exists() else []
    vinc=json.load(open(vincp)) if vincp.exists() else []
    ledger=json.load(open(led[0])) if led else []
    t=can.read_text(encoding='utf-8') if can else ''
    corpo=re.split(r'APÊNDICE DE REFERÊNCIAS|APENDICE DE REFERENCIAS',t)[0]
    # ids
    refids=set(r.get('id_referencia_interna','') for r in refs)
    labs=set(x.replace('REF_','') for x in refids)
    usadas=set(m.group(1) for m in TAGre.finditer(corpo))
    # A1: labels citados sem registro (descontar prosa: token so de digitos = ano)
    sem_reg=sorted(l for l in usadas if l not in labs and not re.fullmatch(r'(19|20)\d{2}[a-z]?',l))
    # A2: refs rejeitadas/ruido no corpo
    ruido=[r.get('id_referencia_interna','').replace('REF_','') for r in refs
           if str(r.get('status_auditoria','')).upper() in ('EXCLUIDO_RUIDO','NAO_LOCALIZADO','CITACAO_INCORRETA','NAO_SUSTENTA_CLAIM')]
    ruido_corpo=[l for l in ruido if re.search(r'\b'+re.escape(l)+r'\[',corpo)]
    naoconf=[r.get('id_referencia_interna','') for r in refs
             if str(r.get('status_auditoria','')).upper() not in ('CONFIRMADO','PARCIALMENTE_CONFIRMADO','EXCLUIDO_RUIDO','')]
    # A3
    orig=set(str(r.get('origem_pipeline','')) for r in refs)
    # C1 orfaos
    orfaos=[v.get('id_referencia_interna','') for v in vinc if v.get('id_referencia_interna','') not in refids]
    # C2
    sem_trecho=[x for x in vinc if not str(x.get('trecho_ancora','')).strip()]
    sem_forca=[x for x in vinc if not x.get('forca_causal')]
    enum={'CONFIRMADO','PARCIALMENTE_CONFIRMADO','NAO_LOCALIZADO','CITACAO_INCORRETA','NAO_SUSTENTA_CLAIM'}
    sem_status=[x for x in vinc if str(x.get('status_auditoria','')).strip() not in enum]
    # E1/E2/E3
    e1=all(r.get('g1_metodo')=='eutils_automatico' for r in refs) if refs else False
    def ruim_g3(g): return re.search(r'eutils|script|retrofit',str(g),re.I) is not None or not str(g).strip()
    e2bad=[r.get('id_referencia_interna','') for r in refs if r.get('verification_status')=='verificado' and ruim_g3(r.get('g3_verificado_por',''))]
    # trecho do ledger: listra literal?
    def literal(tx):
        tx=tx.strip()
        return tx.endswith('*') or tx.rstrip().endswith(('.','!','?'))
    e3bad=[e.get('id_auditoria','?') for e in ledger if not literal(e.get('trecho_ancora',''))]
    fallback=[e.get('id_auditoria','?') for e in ledger if 'Módulo 09' in e.get('trecho_ancora','') or 'Modulo 09' in e.get('trecho_ancora','')]
    # C3/C4/C5
    grade=bool(re.search(r'GRADE\s+[A-D]',t.upper()))
    pmid=bool(re.search(r'\b\d{7,8}\b',corpo))
    doi=bool(re.search(r'10\.\d{4}/',t))
    p20='exame_' in t; p16='mecanismo_B16_neurogenese' in t
    print(f'==== B{n} ({f.name}) ====')
    print(f'  refs={len(refs)} vinc={len(vinc)} ledger={len(ledger)} palavras={len(t.split())}')
    print(f'  A1 sem_registro={len(sem_reg)} {sem_reg[:4]}')
    print(f'  A2 ruido_no_corpo={len(ruido_corpo)} status_nao_conf={len(naoconf)} {naoconf[:3]}')
    print(f'  A3 origem={orig}')
    print(f'  C1 orfaos={len(orfaos)} | C2 sem_trecho={len(sem_trecho)} sem_forca={len(sem_forca)} sem_status={len(sem_status)}')
    print(f'  C2 trecho_literal={sum(1 for v in vinc if literal(v.get("trecho_ancora","")))}/{len(vinc)} | fallback_mod09={len(fallback)}')
    print(f'  E1 eutils_todas={e1} | E2 verificado_sem_avaliador={len(e2bad)} {e2bad[:3]} | E3 trecho_truncado={len(e3bad)} {e3bad[:3]}')
    print(f'  C3 grade={grade} | C4 pmid_texto={pmid} doi={doi} | C5 exame={p20} B16={p16}')
    print()
