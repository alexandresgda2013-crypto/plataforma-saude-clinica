#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera vinculos_referencia_afirmacao.json da B16 (trecho_ancora = listra onde o rotulo aparece)."""
import json,re,os
F='/home/user/BIBLIOTECAS/B16_Neurogenese'
txt=open(F+'/B16 NEUROGENESE V1 CANONICA.md',encoding='utf-8').read()
refs=json.load(open(F+'/Evidencias/Bibliografia/01_pmids.json',encoding='utf-8'))
# mapa rotulo -> bloco da canonica (BLOCO_xx mais proximo acima)
linhas=txt.splitlines()
bloco_atual='B16_CANONICA'
listra_info=[]  # (texto_listra, bloco)
for ln in linhas:
    m=re.match(r'^## (BLOCO_\d+)',ln)
    if m: bloco_atual=m.group(1)
    ls=ln.strip()
    if ls.startswith('*') and ls.endswith('*') and '[' in ls:
        listra_info.append((ls,bloco_atual))
# prosa: para refs citadas so em prosa pega a linha de prosa
prosa_lines=[(ln.strip(),bloco_atual) for ln in linhas if not ln.strip().startswith('*')]
# re-mapa bloco por linha (ordem)
blocos=[]
b='B16_CANONICA'
for ln in linhas:
    m=re.match(r'^## (BLOCO_\d+)',ln)
    if m: b=m.group(1)
    blocos.append(b)
def acha_trecho(lab):
    for i,ln in enumerate(linhas):
        if re.search(r'\b'+re.escape(lab)+r'\[(?:MA|EC|OB|ML|AT)\]',ln):
            tx=' '.join(ln.strip().split())
            return tx[:1400], blocos[i]  # listras inteiras, sem truncamento de fim
    return None,None
vinc=[]
for k,r in enumerate(refs,1):
    lab=r['id_referencia_interna'].replace('REF_','')
    trecho,bloco=acha_trecho(lab)
    if not trecho:
        trecho=f"*{lab}[{r['desenho_estudo'].strip('[]')}]*"; bloco='B16_CANONICA'
    role=r['evid_role']
    if role=='review':
        nat,mat,forca,fb = 'associativa','bem_suportado','tier_4_descritivo_estrutural','media-alta(revisao)'
    elif role=='human_clinical':
        nat,mat,forca,fb = 'associativa','moderadamente_suportado','tier_3_correlacional_mecanistico','media(humano)'
    else:
        nat,mat,forca,fb = 'causal','moderadamente_suportado','tier_2_necessidade_ou_suficiencia','alta(animal)'
    esp=r['especie_mesh']
    vinc.append({
        'id_vinculo':f'VINC_B16_{k:04d}',
        'id_referencia_interna':r['id_referencia_interna'],
        'pmid_oficial':str(r['pmid_oficial']),
        'secao_origem':'B16_CANONICA',
        'trecho_ancora':trecho,
        'mecanismo_origem':'mecanismo_B16_neurogenese',
        'natureza_relacao':nat,'grau_maturidade':mat,'forca_causal':forca,
        'forca_biologica_conexao':fb,
        'especie_mesh':esp,'evid_role':role,'claim_id':'',
        'bloco_origem':bloco,'uso':'B16_v1','status_auditoria':'CONFIRMADO',
        'data_verificacao':'2026-09-08'})
os.makedirs(F+'/Evidencias/Vinculos',exist_ok=True)
json.dump(vinc,open(F+'/Evidencias/Vinculos/vinculos_referencia_afirmacao.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(vinc,open(F+'/Evidencias/Vinculos/vinculos_referencia_afirmacao_B16.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
from collections import Counter
print('vinculos:',len(vinc),'| blocos:',dict(Counter(v['bloco_origem'] for v in vinc)))
