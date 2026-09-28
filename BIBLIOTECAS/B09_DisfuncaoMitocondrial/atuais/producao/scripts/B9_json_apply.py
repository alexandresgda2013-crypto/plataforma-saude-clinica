#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# B9 — aplica rodada [AT] GPM 2026-09-09 na tríade (pmids/vínculos/ledger) + manifesto + trilha.
import json, sys
sys.path.insert(0, '/home/user')
from b9_refs import D

BASE = '/home/user/BIBLIOTECAS/B09_DisfuncaoMitocondrial'
E = json.load(open(f'{BASE}/producao/insumos/b9_efetch_all.json'))
CANON = open(f'{BASE}/B9 DISFUNCAO MITOCONDRIAL V2 CANONICA.md', encoding='utf-8').read()

VOCAB_NAT = {'', 'causal', 'contributiva', 'associativa', 'compensatoria', 'marcador', 'nao_estabelecida'}
VOCAB_MAT = {'', 'muito_estabelecido', 'bem_suportado', 'moderadamente_suportado', 'emergente', 'hipotese_inicial'}
VOCAB_ACAO = {'', 'MANTER', 'CORRIGIR_PMID', 'CORRIGIR_METADADOS', 'REBAIXAR_LINGUAGEM', 'REMOVER_TRECHO', 'ADICIONAR_SINALIZADOR', 'TROCAR_REFERENCIA'}
VOCAB_FC = {'tier_1_necessidade_e_suficiencia', 'tier_2_necessidade_ou_suficiencia', 'tier_3_correlacional_mecanistico', 'tier_4_descritivo_estrutural'}

def trecho_para(cit):
    idxs = []; start = 0
    while True:
        i = CANON.find(cit, start)
        if i < 0: break
        idxs.append(i); start = i + 1
    assert idxs, cit
    for i in idxs:
        l = CANON.rfind('\n', 0, i - 1); l2 = CANON.rfind('\n', 0, l - 1) if l > 0 else -1
        a = max(0, l2 + 1); b = CANON.find('\n', i + len(cit)); b = len(CANON) if b < 0 else b
        t = CANON[a:b].strip()
        assert cit in t
        if CANON.count(t) == 1: return t
    i = idxs[0]; a = CANON.rfind('\n\n', 0, i) + 2; b = CANON.find('\n\n', i)
    t = CANON[a:len(CANON) if b < 0 else b].strip()
    assert CANON.count(t) == 1, (cit, 'fallback')
    return t

pmids_new, vincs_new, leds_new = [], [], []
for (rid, pmid, prosa, tag, bloco, nn, erole, mat, desenho, g2m, achado, alx) in D:
    e = E[pmid]; ano = e['ano_print']; fonte = e['iso']
    esp = e['especie_mesh'] or []
    claim = f'B9.MEC.{bloco}.{nn:03d}'
    autores = e['autores'] if e['autores'] else ['?']
    a1 = autores[0].split()[0].replace('-', '').replace('ü', 'u').replace('Ľ', 'L').replace('ľ', 'l')
    aliases = [a1.upper(), a1] + alx
    ML = tag == 'ML'
    # extrapolação
    if rid == 'REF_HOFSTRA_2024':
        extrap = 'parcial — desenho cross-espécies (camundongo ELS + transcriptoma humano público); validação humana direta pendente'
    elif esp == ['Animals'] or (ML and 'Animals' in esp):
        extrap = 'SIM — evidência em roedor/célula/modelo; tradução humana por analogia'
    elif 'Animals' in esp:
        extrap = 'parcial — revisão mistura espécies'
    elif not esp:
        extrap = 'não — avaliado por título/abstract (MeSH pendente de indexação)'
    else:
        extrap = 'não'
    cit = f'({prosa})[{tag}]'
    assert CANON.count(cit) >= 1, ('cit ausente', cit)
    trecho = trecho_para(cit)
    mesh_note = '; MeSH pendente de indexação (espécie inferida por título/abstract)' if not e.get('mesh') else ''
    g2e = 'redirecionado_mecanistico' if ML else 'eligible'
    erole_final = erole
    if rid in ('REF_TRIEBELHORN_2024', 'REF_KUFFNER_2020', 'REF_MARQUES_2021'):
        erole_final = 'human_experimental'
    natureza = 'nao_estabelecida' if ML else 'associativa' if tag == 'EC' else 'contributiva'
    acao = 'ADICIONAR_SINALIZADOR' if ML or rid == 'REF_LU_2024' else 'MANTER'
    if rid == 'REF_LU_2024':
        natureza = 'nao_estabelecida'
    pG2 = 'NAO_APLICAVEL' if ML else 'ELIGIBLE_SOURCE'
    fc_led = 'tier_3_correlacional_mecanistico' if ML else 'tier_4_descritivo_estrutural'
    vstat = 'preclinico' if ML else 'emergente'
    assert natureza in VOCAB_NAT and mat in VOCAB_MAT and acao in VOCAB_ACAO and fc_led in VOCAB_FC

    pmids_new.append({
     'pmid_oficial': pmid, 'titulo_artigo': e['titulo'], 'autores': autores,
     'revista_ano': f'{fonte} ({ano})', 'desenho_estudo': f'[{tag}] {desenho} · {fonte}',
     'secao_origem': 'mecanismo_B9_disfuncao_mitocondrial',
     'achado_central_molecular': achado,
     'extrapolacao_por_analogia': extrap,
     'ids_referencia_interna': [rid], 'id_referencia_interna': rid, 'doi': e.get('doi', ''),
     'claim_id_origem': claim, 'evid_role': erole_final, 'especie_mesh': esp,
     'verification_status': vstat,
     'citacao_confirmada': True, 'g1_metodo': 'eutils_automatico',
     'g2_elegibilidade': g2e, 'g2_motivo': g2m,
     'g3_verificado_por': f'IA G3 (Rodada [AT] GPM B9 2026-09-09, insumo externo auditado ref a ref; P-7): esearch DOI[aid] + esummary + efetch; abstract lido{mesh_note}; 2a verificação independente (P-6) pendente',
     'status_auditoria': 'CONFIRMADO', 'origem_pipeline': 'GPM_RODADA_AT', '_aliases': aliases})

    vincs_new.append({
     'id_vinculo': f'VINC_B9_{36 + len(vincs_new):03d}', 'id_referencia_interna': rid,
     'pmid_oficial': pmid, 'secao_origem': 'B9_CANONICA_V2',
     'trecho_ancora': trecho, 'mecanismo_origem': 'mecanismo_B9_disfuncao_mitocondrial',
     'natureza_relacao': natureza if natureza != 'nao_estabelecida' or not ML else 'contributiva',
     'grau_maturidade': mat, 'forca_causal': fc_led,
     'extrapolacao_por_analogia': extrap, 'especie_mesh': esp, 'evid_role': erole_final,
     'verification_status': vstat, 'status_referencia': 'CONFIRMADA',
     'citacao_confirmada': True, 'g1_metodo': 'eutils_automatico', 'g2_elegibilidade': g2e,
     'g2_motivo': g2m,
     'g3_verificado_por': f'IA G3 (Rodada [AT] GPM B9 2026-09-09): eutils esearch DOI[aid] + esummary + efetch; abstract lido{mesh_note}',
     'g3_fulltext': 'abstract lido; PMC full-text fica para 2a verificação independente (P-6, avaliador cego)',
     'status_auditoria': 'CONFIRMADO', 'uso': 'nucleo_causal',
     'segunda_verificacao': 'PENDENTE — 2a verificação independente (P-6, avaliador cego) registrada como pendência de fase; mitigação: selos honestos [ML]/[OB]/[EC], regras fundadoras B9-01..12 fixadas, extrapolação por analogia explícita',
     'data_verificacao': '2026-09-09'})

    leds_new.append({
     'id_auditoria': f'AUD_B9_{36 + len(leds_new):04d}', 'mecanismo': 'B9',
     'id_referencia_interna': rid, 'pmid_oficial': pmid,
     'arquivo_modulo09': 'Evidencias/Bibliografia/01_pmids.json', 'tipo_classificador': '',
     'origem_entrada': 'GPM', 'claim_id': claim, 'secao_origem': 'B9_CANONICA_V2',
     'trecho_ancora': trecho, 'citacao_literal': cit,
     'natureza_da_relacao': natureza, 'grau_maturidade_cientifica': mat,
     'forca_causal': fc_led, 'forca_biologica_conexao': '', 'especie_mesh': esp,
     'evid_role': erole_final,
     'portao_G1_existencia': 'VERIFIED_REFERENCE', 'portao_G2_elegibilidade': pG2,
     'portao_G3_suporte': 'APROVADO', 'status_auditoria': 'APROVADO',
     'destino': 'FICA_MECANISMO', 'acao_correcao': acao, 'reconciliado': True,
     'verificacao': {
      'verificador': 'IA G3 Rodada [AT] GPM B9 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente',
      'data_verificacao': '2026-09-09', 'g1_metodo': 'eutils_automatico',
      'abstract_ou_trecho': f'abstract efetch lido nesta rodada; trecho-âncora inserido na canônica V2{mesh_note}',
      'query_utilizada': 'esearch PubMed DOI[aid]' + (' / busca dirigida autor+ano (sem resolução por DOI)' if pmid in ('39197553',) else ''),
      'g2_motivo': g2m,
      'g3_nota': 'integridade referencial + formulação protegida (regras fundadoras B9-01..12; fronteiras ilustrativas e camadas A–E sinalizadas).'}})

pj = f'{BASE}/Evidencias/Bibliografia/01_pmids.json'
vj = f'{BASE}/Evidencias/Vinculos/vinculos_referencia_afirmacao.json'
lj = f'{BASE}/Auditoria_B9/ledger_auditoria_B9.json'
pjx = json.load(open(pj)); vjx = json.load(open(vj)); ljx = json.load(open(lj))
old_p, old_v, old_l = len(pjx), len(vjx), len(ljx)
pjx += pmids_new; vjx += vincs_new; ljx += leds_new
assert (len(pjx), len(vjx), len(ljx)) == (111, 111, 111), (len(pjx), len(vjx), len(ljx))
assert old_v == 35 and vincs_new[0]['id_vinculo'] == 'VINC_B9_036' and vincs_new[-1]['id_vinculo'] == 'VINC_B9_111'
assert leds_new[0]['id_auditoria'] == 'AUD_B9_0036' and leds_new[-1]['id_auditoria'] == 'AUD_B9_0111'
ids = [x['id_referencia_interna'] for x in pjx]
assert len(set(ids)) == 111, 'id duplicado'
for v in vincs_new:
    assert CANON.count(v['trecho_ancora']) == 1, v['id_vinculo']
for l in leds_new:
    assert l['natureza_da_relacao'] in VOCAB_NAT
    assert l['grau_maturidade_cientifica'] in VOCAB_MAT
    assert l['acao_correcao'] in VOCAB_ACAO
    assert l['forca_causal'] in VOCAB_FC
    assert l['portao_G2_elegibilidade'] in ('ELIGIBLE_SOURCE', 'NAO_APLICAVEL')
json.dump(pjx, open(pj, 'w'), ensure_ascii=False, indent=1)
json.dump(vjx, open(vj, 'w'), ensure_ascii=False, indent=1)
json.dump(ljx, open(lj, 'w'), ensure_ascii=False, indent=1)

# contagens para o manifesto
from collections import Counter
cg2 = Counter(x['g2_elegibilidade'] for x in pjx)
crole = Counter(x['evid_role'] for x in pjx)
mj = f'{BASE}/Evidencias/Bibliografia/_manifesto_biblioteca.json'
man = json.load(open(mj))
man['artefato_rotulo'] = 'CANONICA v2'
man['rodada'] = 4
man['data_corte'] = '2026-09-09'
man['pmids_total'] = 111
man['g1']['resolvidos'] = 111
man['g1']['nao_resolvidos'] = 0
man['g1']['descartados_auditoria'] = ['rodada [AT] GPM 2026-09-09: anexo real 165 itens (o briefing dizia 152); 161 resolvidos por DOI/eutils nesta rodada; 4 NÃO-INDEXADOS confirmados fora (Heyat 2024; Nunes 2025; Niu 2024 preprint medRxiv; Giménez-Palomo 2023); 6 EXC por malha de escopo (Khaliulin — autismo; Tomas — fadiga crônica; Rovira — diabetes; Aytaç — metanfetamina; Tian Q e Park — demência/Alzheimer); 69 BAIXO (camada B/C redundante); 7 fragilidades do briefing externo revertidas (ver decisoes_B9.md)']
man['g2'] = {
 'eligible': cg2.get('eligible', 0),
 'redirecionado_mecanistico': cg2.get('redirecionado_mecanistico', 0),
 'evid_role': {k: crole.get(k, 0) for k in ('review', 'human_clinical', 'human_experimental', 'preclinical_mechanistic')}}
man['g3']['vinculos_n2'] = 111
man['g3']['CONFIRMADO'] = 111
man['g3']['achado'] = 'defeito mitocondrial (reserva/dinâmica/DAMP/mtDNA sob quatro lentes) bem estabelecido; causalidade forte animal [ML]; MR nulo × arquitetura compartilhada; terapia humana emergente/sinal'
man['vinculos_n2'] = 111
man['palavras_canonica'] = len(CANON.split())
man['versao'] = '2.6'
man['pipeline_versao_geracao'] = '2.6'
man['corte_literatura'] = 'busca ativa E-utilities/PubMed; corte 2026-09-09 (rodada [AT] GPM, P-7)'
man['pendencias_fase'] = [
 'P-6: 2a verificação independente (avaliador cego) — AMPLIADA na rodada [AT] 2026-09-09: incluir as levas [AT] de TODAS as bibliotecas B1–B16 ao fim da rodada (16/16)']
man['historico_correcoes'].append({
 'data': '2026-09-09', 'campo': 'rodada_AT_GPM_B9',
 'erro_anterior': 'V1 (35 refs) sem a leva auditada do insumo externo GPM B9 (anexo 165 entradas reais — o briefing dizia 152; 47 âncoras GPM)',
 'correcao': 'auditoria ref a ref (G1 eutils 161/161; 0 falso positivo; 4 não-indexados confirmados — Heyat, Nunes, Niu preprint, Giménez-Palomo 2023; sobreposição com a V1 = 10); matriz de decisão 76 ENTRA/69 BAIXO/6 EXC; 7 fragilidades do briefing revertidas ("Lu 2024 MR não resolvido" — resolvido [Lu 2024: MR bidirecional NULO para mtDNA-CN × TDM/ansiedade/bipolar/esquizofrenia/TOC e reversos; sinal potencial apenas para TEA, fora do escopo]; "Triebelhorn 2024 não localizado" — mesmo registro, impressão 2024; "Mańczak 2010" — Reddy 2011 real; "Li 2018" — Wang 2018 real; Scaini vigente impressão 2022 — ID mantido; anos de impressão corrigidos; 10 itens do anexo fora do §3∪§6 cobertos pela auditoria); fusão V2 com 111 refs; 12 regras fundadoras B9 + inventário negativo ×10 fixados em CONTROVÉRSIAS; mtDNA lido sob quatro lentes (CN/dano/mutações/ccf-mtDNA); tríade sincronizada (pmids 111, vínculos 111, ledger 111)',
 'acao_downstream': 'portões oficiais revalidados (gate P-5, framework auditoria, checklist); P-4 adendo V2; P-6 mantido pendente'})
json.dump(man, open(mj, 'w'), ensure_ascii=False, indent=1)

# trilha
trilha = {'ciclo': '[AT] GPM B9 — Disfunção Mitocondrial', 'data': '2026-09-09',
 'artefato': 'CANONICA v2 (111 refs; de 35)',
 'insumos': ['GPM_B9_DisfuncaoMitocondrial (3).md (oficial, molde v2.0 — 47 âncoras com PMIDs; 12 regras fundadoras; inventário negativo ×10; fenótipos F1–F7; submecanismos B9.1–B9.7)',
  'BRIEFING_B9_DISFUNCAO_MITOCONDRIAL_RODADA0.md',
  'B9_Disfuncao_Mitocondrial_Briefing_Cientifico (1).md',
  'Artigos cientificos do mecanismo B9 disfunção mitocondrial.md (anexo real: 165 entradas — briefing dizia 152)',
  'Resumo do insumo para B9 Chatgpt.md (matriz 7 submecanismos; defesa do MR negativo)'],
 'auditoria': {'anexo_itens': 165, 'g1_resolvidos': 161, 'falsos_positivos': 0,
  'nao_indexados': ['Heyat 2024 (s40747)', 'Nunes 2025 (clinbioenerg)', 'Niu 2024 (preprint medRxiv)', 'Giménez-Palomo 2023 (Eur Psychiatry)'],
  'sobreposicao_com_V1': 10, 'masters_gpm': {'total': 47, 'ja_vigentes': 4, 'novas': 43},
  'fila_decisao': 151, 'entra': 76, 'baixo': 69, 'exc': 6,
  'exc_itens': ['Khaliulin 2025 (autismo)', 'Tomas 2017 (fadiga crônica — GPM M10 exclui)', 'Rovira 2017 (diabetes)', 'Aytaç 2025 (metanfetamina)', 'Tian Q 2025 (demência)', 'Park 2021 (Alzheimer)'],
  'fragilidades_briefing_revertidas': ['"Lu 2024 não resolvido" → resolvido (MR bidirecional, J Affect Disord)', '"Triebelhorn 2024 não localizado" → mesmo registro, impressão 2024 (Mol Psychiatry)', '"Mańczak 2010" → Reddy 2011 real (Mańczak coautora)', '"Li 2018" → Wang 2018 real (BAIXO)', 'Scaini vigente impressão 2022 — ID mantido', 'anos de impressão corrigidos (Burté 2015; Chandhok 2018; Culmsee 2018; Feng 2020; Lagos 2026; Mafikandi 2025; Palma 2024; Triebelhorn 2024)', '10 itens do anexo fora de §3∪§6 cobertos pela auditoria']},
 'regras_fixadas': ['B9-REGRA-01 ROS≠elevado (sinalização redox)', 'B9-REGRA-02 mtDNA quatro fenômenos', 'B9-REGRA-03 associação≠causalidade genética (MR Lu nulo; Xue compartilhada)', 'B9-REGRA-04 camadas A–E', 'B9-REGRA-05 multi-compartimento (PBMC≠neurônio)', 'B9-REGRA-06 causalidade animal Dong 2023', 'B9-REGRA-07 terapias só sinal (Javani/Mafikandi/Tian)', 'B9-REGRA-08 fronteiras B1/B6', 'B9-REGRA-09 ansiedade social âncora legítima', 'B9-REGRA-10 anos = impressão', 'B9-REGRA-11 Mito-Mood [G1]', 'B9-REGRA-12 multi-tag'],
 'blocos_neg': ['inventário negativo B9 ×10 fixado em CONTROVÉRSIAS'],
 'artefatos': ['producao/insumos/RELATORIO_AUDITORIA_MATRIZ_B9.md', 'producao/insumos/matriz_b9_decisao.json', 'producao/insumos/matriz_b9_g1.json', 'producao/insumos/b9_anexo_entries.json', 'producao/insumos/b9_cruzamento.json', 'producao/insumos/b9_efetch_all.json', 'producao/insumos/b9_trechos_ancora.json', 'producao/historico/v1_canonica_2026-09-09.md'],
 'pendencias': ['P-6 (2ª verificação cega, Via 2) — PENDENTE ao fim da rodada 16/16, cobrindo todas as levas [AT]']}
json.dump(trilha, open(f'{BASE}/producao/04_AT_ciclo_2026-09-09.json', 'w'), ensure_ascii=False, indent=1)
print('TRÍADE OK: pmids', old_p, '→', len(pjx), '| vínculos', old_v, '→', len(vjx), '| ledger', old_l, '→', len(ljx))
print('manifesto v2 gravado; trilha gravada; palavras =', man['palavras_canonica'])
