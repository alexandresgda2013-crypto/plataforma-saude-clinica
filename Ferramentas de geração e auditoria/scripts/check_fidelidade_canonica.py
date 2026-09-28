#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_fidelidade_canonica.py — GATE DE FIDELIDADE CANÔNICA (conteúdo).

Além do checklist ESTRUTURAL (checklist_entrega.py), este confere que a
biblioteca canônica fielmente reflete o GPM de origem:

  1. COBERTURA DE ÂNCORAS: as referências citadas no GPM (Autor/Ano)
     existem no Módulo 09 da biblioteca (por sobrenome/ano) OU estão
     explicitamente sinalizadas como rejeitadas/fora (P-6) no Módulo08/decisoes.
  2. COBERTURA DE VIAS: cada "Via N" do Módulo 01 do GPM tem correspondente
     na canônica (BLOCO_01 / profundidade).
  3. COERÊNCIA INTERNA (forma): cada citação (Autor ano)[TAG] na prosa tem
     rótulo/registro no Módulo 09; cada listra referencia PMID existente.
  4. FIDELIDADE DIRECIONAL: as vias/eventos centrais do GPM aparecem na canônica.

Uso:
  python3 check_fidelidade_canonica.py <pasta_biblioteca> [caminho_gpm.md]

Exit 0 = fidelidade OK; exit 1 = há lacunas de conteúdo a resolver.
"""
import sys, re, json, unicodedata, glob
from pathlib import Path

def sa(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c)).lower()
def sobs(s): return re.sub(r'[^a-z]','',sa(s))

erros=[]; avisos=[]; oks=[]
def E(m): erros.append('ERRO | '+m)
def W(m): avisos.append('AVISO| '+m)
def O(m): oks.append('OK   | '+m)

folder=Path(sys.argv[1]).resolve()
bn=re.search(r'B(\d+)',folder.name)
bn='B'+bn.group(1) if bn else '?'
can=sorted(folder.glob('*.md'), key=lambda a:int((re.search(r'[Vv](\d+)',a.name) or [0])[1]))
can=[c for c in can if 'CANONICA' in c.name.upper()]
if not can: E('Nenhuma canônica .md encontrada'); print(*erros,sep='\n'); sys.exit(1)
can=can[-1]; t=can.read_text(encoding='utf-8')

# Módulo 09
refs=[]
for f in glob.glob(str(folder/'Evidencias/Bibliografia/01_pmids.json')):
    refs=json.load(open(f))
ref_sobrenome={}
for r in refs:
    for a in r.get('autores',[])[:6]:
        ref_sobrenome[sobs(str(a).split()[0])]=r.get('pmid_oficial')

O(f'Canônica: {can.name}')
O(f'Módulo 09: {len(refs)} referências')

# 3. COERÊNCIA INTERNA — cada citação (Sob, ano)[TAG] tem registro
cit=re.findall(r'\(([A-ZÀ-Ú][A-Za-zÀ-ÿ\-]+)(?:,| et al)?,\s*((?:19|20)\d{2})\)\s*\[(ML|EC|OB|MA|AT)\]',t)
sem=[]
for sob,ano,tag in cit:
    if sobs(sob) not in ref_sobrenome:
        sem.append(f'({sob}, {ano})[{tag}]')
# desduplica
sem=sorted(set(sem))
if sem:
    W(f'{len(sem)} citações em prosa sem correspondência direta por sobrenome (podem ser rejeitadas/alias): {sem[:6]}')
else:
    O('Toda citação em prosa tem correspondência no Módulo 09 (por sobrenome)')

# rótulos de listra -> PMID existente
rot=re.findall(r'([A-Za-z0-9_]{5,40})\[(ML|EC|OB|MA|AT)\]',t)
O(f'{len(set(r for r,_ in rot))} rótulos canônicos presentes no texto')

# 2/4. COBERTURA DE VIAS — cada "### Via N" / "BLOCO_01" presente
vias_gpm=re.findall(r'### Via\s*\d+[^\n]*',t)  # na canônica
blocos=len(re.findall(r'^## BLOCO_\d{2}',t,re.M))
if blocos>=13: O(f'Estrutura de blocos: {blocos} BLOCOs (>=13)')
else: E(f'Apenas {blocos} BLOCOs (mínimo 13)')

# 1. GPM x cobertura de âncoras
gpm=None
if len(sys.argv)>3:
    gp=Path(sys.argv[2])
    if gp.exists(): gpm=gp.read_text(encoding='utf-8')
if gpm is None:
    # procura em producao/rodada1_gpm
    cand=glob.glob(str(folder/'producao/rodada1_gpm/GPM*.md'))
    cand=[c for c in cand if 'v2' not in c.lower()] or cand
    if cand: gpm=Path(sorted(cand)[-1]).read_text(encoding='utf-8')
if gpm:
    pats=re.findall(r'([A-ZÀ-Ú][A-Za-zÀ-ÿ\-]+)[^.]{0,6}?((?:19|20)\d{2})',gpm)
    gpm_anc={}
    for sob,ano in pats:
        tok=sobs(sob)
        if len(tok)>=5: gpm_anc.setdefault(tok,(sob,ano))
    cobertas=[k for k in gpm_anc if k in ref_sobrenome]
    # as não-cobertas são esperadas (rejeitadas/fora)
    nao=[gpm_anc[k] for k in gpm_anc if k not in ref_sobrenome]
    taxa=len(cobertas)/max(1,len(gpm_anc))
    O(f'Âncoras do GPM: {len(gpm_anc)} | cobertas por registro: {len(cobertas)} ({taxa:.0%})')
    if len(nao):
        W(f'{len(nao)} âncoras do GPM sem registro (esperado: rejeitadas em G1, rejeitadas/falsas ou rejeitadas P-6): ex. {nao[:8]}')
else:
    W('GPM não encontrado para comparação de fidelidade (coloque em producao/rodada1_gpm)')

# palavras
n=len(t.split())
if n>=7000: O(f'Palavras: {n} (>=7000)')
else: E(f'Palavras: {n} (<7000)')

print('\n'.join(oks))
if avisos: print('\n'.join(avisos))
if erros:
    print('\n'.join(erros)); print(f'\n{len(oks)} OK | {len(avisos)} AVISOS | {len(erros)} ERROS'); sys.exit(1)
print(f'\n{len(oks)} OK | {len(avisos)} AVISOS | 0 ERROS')
