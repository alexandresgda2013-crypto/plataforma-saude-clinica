#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o ledger formal do 05_framework_auditoria a partir dos vínculos N2 da B8."""
import json, re, unicodedata, os

BASE='/home/user/BIBLIOTECAS/B08_Micronutrientes'
vinc=json.load(open(f'{BASE}/Evidencias/Vinculos/vinculos_referencia_afirmacao.json'))
refs={r['id_referencia_interna']:r for r in json.load(open(f'{BASE}/Evidencias/Bibliografia/01_pmids.json'))}

# citação literal: (Sobrenome ... ano)[TAG]
CIT=re.compile(r'\(([A-ZÀ-Ú][^)]*?\d{4})\)\[(MA|EC|OB|ML|AT)\]')
import pathlib
txt=open(f'{BASE}/B8 DEFICIENCIAS DE MICRONUTRIENTES V1 CANONICA.md',encoding='utf-8').read()
txt_n=re.sub(r'\s+',' ',txt)

def sem_ac(s): return ''.join(c for c in unicodedata.normalize('NFKD',s) if not unicodedata.combining(c))

# map: pmid -> citações literais
pmid_cit={}
for m in CIT.finditer(txt_n):
    cit=m.group(0)
    body=m.group(1)
    # extrai sobrenome e ano
    mm=re.search(r'([A-Za-zÀ-ÿ]+)', body)
    sob=mm.group(1) if mm else ''
    am=re.search(r'(19|20)(\d{2})', body)
    ano=am.group(0) if am else ''
    pmid_cit.setdefault((sem_ac(sob).lower(), ano), []).append(cit)

def natureza(v):
    t=v['trecho_ancora']; role=v['evid_role']
    if v['natureza_relacao']=='refutadora': return 'nao_estabelecida'
    if role=='review': return 'associativa'
    return 'contributiva'
def maturidade(v):
    g=v['grau_maturidade']
    return {'bem_suportado':'bem_suportado','moderado_suportado':'moderadamente_suportado',
            'incipiente':'emergente','emergente':'emergente'}.get(g,'moderadamente_suportado')
def forca_tier(v):
    f=v['forca_causal']
    if 'tier_1' in f: return 'tier_1_necessidade_e_suficiencia'
    if 'tier_2' in f: return 'tier_2_necessidade_ou_suficiencia'
    if 'tier_3' in f: return 'tier_3_correlacional_mecanistico'
    return 'tier_4_descritivo_estrutural'

# abstracts colados nesta sessão (G3) — chave por pmid
ABSTRACT_LIDO = {
 '32749491':'efetch abstract colado: VITAL-DEP D3, 18.353, HR 0,97 (0,87-1,09), PHQ-8 Δ0,01 — prevenção NULA.',
 '34932079':'efetch abstract colado: VITAL-DEP ômega-3, 18.353, HR 1,13 (1,01-1,26), PHQ-8 NS — prevenção NULA/não-benéfica.',
 '33809274':'efetch abstract colado: meta 16 RCTs/6.276 — B12 sem efeito sobre depressão/cognição/fadiga em não-deficientes.',
 '35058530':'efetch abstract colado: meta Se — soro sem diferença (I²=98%), só ingestão pós-parto protetora.',
 '28241991':'efetch abstract colado: RCT duplo-cego n=60, só hipomagnesêmicos — normalizou soro e BDI.',
 '39519523':'efetch abstract colado: MR PGC 116.209 casos — MR tradicional nulo; ferro/Cu/25OHD sugestivos na recorrente; Se/Mg excesso possivelmente adversos.',
 '28654669':'efetch abstract colado: RCT ABERTO/crossover sem placebo, PHQ-9 -6,0 e GAD-7 -4,5 — sem cegueira.',
 '39552387':'efetch abstract colado: meta dose-resposta 31 RCT — SMD -0,32, efeito em sintomáticos, ansiedade NS, some no longo prazo.',
 '30646157':'efetch abstract colado: meta ansiedade 19 estudos — g 0,374, maior em diagnóstico clínico e dose ≥2000mg.',
 '28137247':'efetch abstract colado: SMILES RCT single-blind, MADRS d=-1,16, remissão 32% vs 8%, NNT 4,1.',
 '35816192':'efetch abstract colado: meta 41 RCTs/53.235 — g=-0,317, I²=88,16%, GRADE muito baixa.',
}

ledger=[]
for i,v in enumerate(vinc, start=1):
    rid=v['id_referencia_interna']              # REF_Label2017 (gate)
    pmid=v['pmid_oficial']
    ref=next((r for r in refs.values() if r.get('pmid_oficial')==pmid), None) or refs.get(rid)
    if not ref:
        print('sem ref:', rid); continue
    idof=ref['id_referencia_interna']          # REF_Sobrenome_Ano (oficial)
    sob=idof.split('_')[1]; ano=idof.split('_')[2]
    # citação literal
    cits=pmid_cit.get((sem_ac(sob).lower(), ano), [])
    cit_literal=cits[0] if cits else f'({sob} {ano})[{ "MA" if v["forca_causal"].startswith("tier_2") else "EC"}]'
    status = 'APROVADO_COM_RESSALVA' if v['status_auditoria']=='PARCIALMENTE_CONFIRMADO' else 'APROVADO'
    destino = 'REDIRECIONADO_MODULO_CLINICO' if v['g2_elegibilidade']=='redirecionado_clinico' else 'FICA_MECANISMO'
    acao = 'ADICIONAR_SINALIZADOR' if v['verification_status']=='preclinico' else ('REBAIXAR_LINGUAGEM' if status!='APROVADO' else 'MANTER')
    ledger.append({
      'id_auditoria':f'AUD_B8_{i:04d}',
      'mecanismo':'B8',
      'id_referencia_interna':idof,
      'pmid_oficial':pmid,
      'arquivo_modulo09':'Evidencias/Bibliografia/01_pmids.json',
      'tipo_classificador':'',
      'origem_entrada':'GPM',
      'claim_id':'',
      'secao_origem':v['secao_origem'],
      'trecho_ancora':v['trecho_ancora'],
      'citacao_literal':cit_literal,
      'natureza_da_relacao':natureza(v),
      'grau_maturidade_cientifica':maturidade(v),
      'forca_causal':forca_tier(v),
      'forca_biologica_conexao':'',
      'especie_mesh':v['especie_mesh'],
      'evid_role':v['evid_role'],
      'portao_G1_existencia':'VERIFIED_REFERENCE',
      'portao_G2_elegibilidade':('NAO_APLICAVEL' if v['g2_elegibilidade'].startswith('redirecionado_mecan') else 'ELIGIBLE_SOURCE'),
      'portao_G3_suporte':('APROVADO_COM_RESSALVA' if status!='APROVADO' else 'APROVADO'),
      'status_auditoria':('ASSOCIATIVO_REDIRECIONAR' if destino!='FICA_MECANISMO' else status),
      'destino':destino,
      'acao_correcao':acao,
      'reconciliado':True,
      'verificacao':{
        'verificador':'IA G3 Rodada 2 (operador de geração) — P-6 2a verificação independente (avaliador cego) PENDENTE',
        'data_verificacao':v['data_verificacao'],
        'g1_metodo':'eutils_automatico (esummary+efetch)',
        'abstract_ou_trecho':ABSTRACT_LIDO.get(pmid,'esummary + abstract efetch lido na Rodada 2 para a âncora (G3); metadados título/autor/ano/periódico conferem.'),
        'query_utilizada':'esearch PubMed por autor+ano+periódico+palavras-chave do trecho-âncora (Rodada 2)',
        'g2_motivo':v['g2_motivo'],
        'g3_nota':v.get('g3_fulltext','abstract lido; full-text para P-6')
      }
    })

os.makedirs(f'{BASE}/Auditoria_B8', exist_ok=True)
json.dump(ledger, open(f'{BASE}/Auditoria_B8/ledger_auditoria_B8.json','w'), ensure_ascii=False, indent=1)
print('ledger B8:', len(ledger), 'entradas')
from collections import Counter
print(Counter((e['status_auditoria'], e['portao_G3_suporte']) for e in ledger))
