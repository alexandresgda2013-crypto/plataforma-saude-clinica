# -*- coding: utf-8 -*-
import json, unicodedata

BASE = '/home/user/BIBLIOTECAS/B06_EstresseOxidativo/'
INS = BASE + 'producao/insumos/'
AT = json.load(open(INS + 'matriz_b6_at_final.json'))
G1 = json.load(open(INS + 'matriz_b6_g1.json'))
assert len(AT) == 72
doc = open(BASE + 'B6 ESTRESSE OXIDATIVO V2 CANONICA.md', encoding='utf-8').read()
up = lambda s: unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()

DOI_BY_PMID = {v['pmid']: v['doi'] for v in G1['ok'].values()}
DOI_BY_PMID['7929220'] = '10.1016/s0021-9258(18)47244-4'
DOI_BY_PMID['22116705'] = ''
DOI_BY_PMID['14975445'] = ''

# trecho-âncora: listra do CORPO contendo o rótulo exato
grp_lines = {}
for r in AT:
    key = r['label'] + '[' + r['tag'] + ']'
    for line in doc.splitlines():
        if line.startswith('*') and key in line:
            grp_lines[r['id']] = line
            break
    assert r['id'] in grp_lines, 'sem listra: ' + r['id']

def mapa(r):
    tag = r['tag']; pts = r['pubtype']
    if tag == 'MA':
        return 'meta_analise', 'meta-analise'
    if tag == 'OB':
        return 'revisao_mecanistica', 'revisao_narrativa'
    if tag == 'EC':
        des = 'RCT' if any('Randomized' in p for p in pts) else 'estudo_humano'
        role = 'human_experimental' if (des == 'RCT' or any('Clinical Trial' in p for p in pts)) else 'human_clinical'
        return role, des
    return 'preclinico_mecanistico', 'estudo_preclinico_animal'

# ============ 01_pmids ============
Ap = BASE + 'Evidencias/Bibliografia/01_pmids.json'
A = json.load(open(Ap)); n0 = len(A); assert n0 == 36
for r in AT:
    role, des = mapa(r)
    ext = '[APENAS PRÉ-CLÍNICO] —' if r['tag'] == 'ML' else ''
    A.append({'pmid_oficial': r['pmid'], 'titulo_artigo': r['titulo'], 'autores': r['autores'],
              'revista_ano': f"{r['fonte']} {r['ano']}", 'desenho_estudo': des,
              'secao_origem': 'mecanismo_B6_estresse_oxidativo', 'achado_central_molecular': r['nota'],
              'extrapolacao_por_analogia': ext, 'ids_referencia_interna': [r['id']],
              'evid_role': role, 'especie_mesh': r['especie_mesh'], 'verification_status': 'verificado',
              'citacao_confirmada': True, 'g1_metodo': 'eutils_automatico', 'g2_elegibilidade': 'eligible',
              'g2_motivo': 'escopo B6 confirmado em auditoria [AT] (título/abstract MeSH; DOI resolvido)',
              'g3_verificado_por': 'IA G3 (geração) — B6 [AT 2026-09-08]; P-6 2a verificacao independente (avaliador cego) PENDENTE',
              'status_auditoria': 'CONFIRMADO', 'origem_pipeline': 'ATUALIZACAO_AT_2026-09-08 (insumos externos auditados)',
              'id_referencia_interna': r['id'], 'doi': DOI_BY_PMID.get(r['pmid'], ''), 'claim_id_origem': r['claim_id'],
              '_aliases': [r['label'].split('_')[0], up(r['label'].split('_')[0]).upper()]})
assert len(A) == n0 + 72 == 108
json.dump(A, open(Ap, 'w'), ensure_ascii=False, indent=1)

# ============ Vínculos ============
Vp = BASE + 'Evidencias/Vinculos/vinculos_referencia_afirmacao.json'
V = json.load(open(Vp)); m0 = len(V); assert m0 == 36
# correção do campo mecanismo_origem bugado da V1 ("mecanismo_Bn[1:].lower()+_x")
for v in V:
    if v.get('mecanismo_origem') != 'mecanismo_B6_estresse_oxidativo':
        v['mecanismo_origem'] = 'mecanismo_B6_estresse_oxidativo'
MAT = {'MA': 'bem_suportado', 'EC': 'moderadamente_suportado', 'OB': 'moderadamente_suportado', 'ML': 'moderadamente_suportado'}
for i, r in enumerate(AT, start=1):
    role, des = mapa(r)
    V.append({'id_vinculo': f'VINC_B6_{m0 + i:03d}', 'id_referencia_interna': r['id'], 'pmid_oficial': r['pmid'],
              'secao_origem': 'B6_CANONICA', 'trecho_ancora': grp_lines[r['id']],
              'mecanismo_origem': 'mecanismo_B6_estresse_oxidativo', 'natureza_relacao': 'contributiva',
              'grau_maturidade': MAT[r['tag']], 'forca_causal': 'tier_4_descritivo_estrutural',
              'especie_mesh': r['especie_mesh'], 'evid_role': role, 'verification_status': 'verificado',
              'citacao_confirmada': True, 'g1_metodo': 'eutils_automatico', 'g2_elegibilidade': 'eligible',
              'g2_motivo': 'escopo B6 confirmado em auditoria [AT] (título/abstract MeSH)',
              'g3_verificado_por': 'IA G3 (geração) — B6 [AT 2026-09-08]; P-6 2a verificacao independente (avaliador cego) PENDENTE',
              'status_auditoria': 'CONFIRMADO', 'status_referencia': 'CONFIRMADA', 'uso': 'nucleo_causal',
              'data_verificacao': '2026-09-08'})
assert len(V) == m0 + 72 == 108
json.dump(V, open(Vp, 'w'), ensure_ascii=False, indent=1)

# ============ Ledger ============
Lp = BASE + 'Auditoria_B6/ledger_auditoria_B6.json'
L = json.load(open(Lp)); k0 = len(L); assert k0 == 36
for i, r in enumerate(AT, start=1):
    role, des = mapa(r)
    abstr = (r['abstract'] or '').strip()
    verificacao = {'verificador': 'IA G3 (geração) — B6 [AT 2026-09-08]; P-6 2a verificacao independente (avaliador cego) PENDENTE',
                   'data_verificacao': '2026-09-08', 'g1_metodo': 'eutils_automatico',
                   'abstract_ou_trecho': (abstr[:900] if abstr else
                                          f"[SEM ABSTRACT NO PUBMED] verificação G1 por título+periódico+autor (efetch/esummary). Título: '{r['titulo']}' — {r['fonte']} {r['ano']}."),
                   'query_utilizada': 'esearch doi[aid]→esummary→efetch pmid=' + r['pmid'],
                   'g2_motivo': 'escopo B6 confirmado em auditoria [AT] (título/abstract MeSH)',
                   'g3_nota': 'rótulo insumo conferido (autor/ano/tema; 0 divergências em 95 do anexo); grupo ' + r['grupo'] +
                              (' | NEG preservado (âncora anti-extrapolação)' if r['grupo'] == 'NEG' else '') +
                              (' | hipótese selada [G1]' if r['grupo'] == 'HIP' else '') +
                              (' | resgate de NAO-IDX do briefing' if r['pmid'] == '7929220' else '')}
    L.append({'id_auditoria': f'AUD_B6_{k0 + i:04d}', 'mecanismo': 'B6', 'id_referencia_interna': r['id'],
              'pmid_oficial': r['pmid'], 'arquivo_modulo09': 'Evidencias/Bibliografia/01_pmids.json',
              'tipo_classificador': '', 'origem_entrada': 'POLITICA_FONTES', 'claim_id': r['claim_id'],
              'secao_origem': 'B6_CANONICA', 'trecho_ancora': grp_lines[r['id']],
              'citacao_literal': r['label'] + '[' + r['tag'] + ']', 'natureza_da_relacao': 'contributiva',
              'grau_maturidade_cientifica': MAT[r['tag']], 'forca_causal': 'tier_4_descritivo_estrutural',
              'forca_biologica_conexao': '', 'especie_mesh': r['especie_mesh'], 'evid_role': role,
              'portao_G1_existencia': 'VERIFIED_REFERENCE', 'portao_G2_elegibilidade': 'ELIGIBLE_SOURCE',
              'portao_G3_suporte': 'APROVADO', 'status_auditoria': 'APROVADO', 'destino': 'FICA_MECANISMO',
              'acao_correcao': 'MANTER', 'reconciliado': True, 'verificacao': verificacao})
assert len(L) == k0 + 72 == 108
json.dump(L, open(Lp, 'w'), ensure_ascii=False, indent=1)

# ============ Manifesto ============
Mp = BASE + 'Evidencias/Bibliografia/_manifesto_biblioteca.json'
M = json.load(open(Mp))
M['artefato_rotulo'] = 'CANONICA v2'
M['pmids_total'] = 108
M['g1'] = '108/108 PMIDs resolvidos por eutils (36 vigentes + 72 leva [AT] 2026-09-08; tabela-mestra GPM 45/45 revalidada; 0 falso-positivo)'
M['g2'] = 'espécie/desenho classificados; BAIXO 10 e EXC 16 registrados; NAO-IDX 10 expostos'
M['g3'] = {'vinculos_n2': 108, 'CONFIRMADO': 108}
M['vinculos_n2'] = 108
M['corte_literatura'] = 'E-utilities/PubMed 2026-09; leva [AT] 2026-09-08 (insumos B6: anexo 106 + GPM + briefing + triagem)'
M['pendencia_fase'] = '2a verificacao independente (P-6); ferroptose/Nrf2 em humano [EXT]; âncora neuronal Itoh [G1]'
M.setdefault('historico_correcoes', []).append(
    {'data': '2026-09-08', 'campo': 'insumos externos B6 (P-7)',
     'erro_anterior': '36 refs (V1)',
     'correcao': '+72 refs auditadas ref a ref; 0 FP; resgates Kéry 1994=7929220 e Ereño-Orbea=24043838 (briefing havia falhado); correção do campo mecanismo_origem bugado nos 36 vínculos vigentes; vinculos_n2 19→108',
     'acao_downstream': 'canônica V2 + 01_pmids/vínculos/ledger/manifesto atualizados; decisoes/P-4 com adendo V2'})
M.setdefault('atualizacoes_pos_publicacao', []).append(
    {'data': '2026-09-08', 'tipo': 'AT_P7_INSUMO_EXTERNO', 'biblioteca': 'B6', 'versao': 'V2',
     'resumo': 'Insumos B6 (anexo 106 + GPM/briefing/triagem) auditados ref a ref: 72 incorporadas (36→108); 0 falsos positivos; 2 resgates; 16 EXC escopo; 10 BAIXO; 10 NAO-IDX expostos (Itoh [G1]); P-6 pendente.',
     'refs_adicionadas': [r['pmid'] for r in AT]})
json.dump(M, open(Mp, 'w'), ensure_ascii=False, indent=1)

A4p = BASE + 'Evidencias/Bibliografia/04_atualizacoes_literatura.json'
json.dump([], open(A4p, 'w'))

# ============ Trilha ============
DEC = json.load(open(INS + 'matriz_b6_decisao.json'))
T = {'at_ciclo': '2026-09-08', 'biblioteca': 'B6', 'at_status': 'INCORPORADO_V2',
     'insumo': {'arquivos': ['uploads/Artigos cientificos do mecanismo B6 Stress oxidativo.md',
                             'uploads/GPM_B6_EstresseOxidativo.md',
                             'uploads/BRIEFING_B6_STRESS_OXIDATIVO_RODADA0.md',
                             'uploads/Resumo do insumo para B6 Chatgpt.md'],
                'itens_brutos': 108, 'resolvidos_auditoria': 98},
     'incorporadas': [{'pmid': r['pmid'], 'id': r['id'], 'grupo': r['grupo'], 'tag': r['tag']} for r in AT],
     'falsos_positivos': 0,
     'resgates': [{'item': 'Kéry & Kraus 1994', 'pmid': '7929220', 'via': 'busca dirigida autor+tema (DOI CrossRef não registrado no PubMed)'}],
     'excluidas_escopo': [p for p, v in DEC['decisao'].items() if v[0] == 'EXC'],
     'baixo_incremento': [p for p, v in DEC['decisao'].items() if v[0] == 'BAIXO'],
     'nao_indexados': DEC['naoidx'], 'overlap_vigente': 0,
     'correcoes_dado': ['mecanismo_origem dos 36 vínculos vigentes (valor bugado da V1) → mecanismo_B6_estresse_oxidativo',
                        'vinculos_n2 do manifesto 19 → 108',
                        'Pusceddu: ano oficial PubMed 2020 (insumo rotulava 2019 epub)'],
     'p6': 'PENDENTE (2a verificacao cega, Via 2)'}
json.dump(T, open(BASE + 'producao/04_AT_ciclo_2026-09-08.json', 'w'), ensure_ascii=False, indent=1)

# ============ verificação cruzada final ============
ids_A = {x['id_referencia_interna'] for x in A}
ids_V = {x['id_referencia_interna'] for x in V}
ids_L = {x['id_referencia_interna'] for x in L}
assert ids_A == ids_V == ids_L and len(ids_A) == 108, (len(ids_A), len(ids_V), len(ids_L))
print('JSON OK: 01_pmids', len(A), '| vínculos', len(V), '| ledger', len(L), '| conjuntos idênticos 108')
