# -*- coding: utf-8 -*-
import json, unicodedata, re
BASE='/home/user/BIBLIOTECAS/B04_Monoaminas/'
AT=json.load(open(BASE+'producao/insumos/matriz_b4_at_final.json'))
assert len(AT)==94
doc=open(BASE+'B4 DEFICIÊNCIA DE MONOAMINAS V2 CANONICA.md').read()
up=lambda s: unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()
# listras anchor: body listra per grupo
grp_lines={}
for r in AT:
    key=r['label']+'['+r['tag']+']'
    for line in doc.splitlines():
        if line.startswith('*') and key in line: grp_lines[r['id']]=line; break
    assert r['id'] in grp_lines, 'sem listra: '+r['id']
# especies/desenho/roles
def mapa(r):
    tag=r['tag']; pts=r['pubtypes']
    if tag=='MA': return 'meta_analise','meta-analise'
    if tag=='OB': return 'revisao_mecanistica','revisao_narrativa'
    if tag=='EC':
        des='RCT' if any('Randomized' in p for p in pts) else 'estudo_humano'
        role='human_experimental' if des=='RCT' or 'Clinical Trial' in pts else 'human_clinical'
        return role,des
    return 'preclinico_mecanistico','estudo_preclinico_animal'
# 01_pmids
A=json.load(open(BASE+'Evidencias/Bibliografia/01_pmids.json')); n0=len(A); assert n0==37
for r in AT:
    role,des=mapa(r)
    ext='[APENAS PRÉ-CLÍNICO] —' if r['tag']=='ML' else ''
    A.append({'pmid_oficial':r['pmid'],'titulo_artigo':r['titulo'],'autores':r['autores'],
      'revista_ano':f"{r['revista']} {r['ano']}",'desenho_estudo':des,
      'secao_origem':'mecanismo_B4_monoaminas','achado_central_molecular':'',
      'extrapolacao_por_analogia':ext,'ids_referencia_interna':[r['id']],
      'evid_role':role,'especie_mesh':r['especie_mesh'],'verification_status':'verificado',
      'citacao_confirmada':True,'g1_metodo':'eutils_automatico','g2_elegibilidade':'eligible',
      'g2_motivo':'escopo B4 confirmado em auditoria [AT] (título/abstract MeSH; DOI resolvido)',
      'g3_verificado_por':'IA G3 (geração) — B4 [AT 2026-09-08]; P-6 2a verificacao independente (avaliador cego) PENDENTE',
      'status_auditoria':'CONFIRMADO','origem_pipeline':'ATUALIZACAO_AT_2026-09-08 (insumo externo auditado)',
      'id_referencia_interna':r['id'],'doi':r['doi'],'claim_id_origem':r['claim_id'],
      '_aliases':[r['label'].split('_')[0], up(r['label'].split('_')[0]).upper()]})
assert len(A)==n0+94==131
json.dump(A,open(BASE+'Evidencias/Bibliografia/01_pmids.json','w'),ensure_ascii=False,indent=1)
# vinculos
V=json.load(open(BASE+'Evidencias/Vinculos/vinculos_referencia_afirmacao.json')); m0=len(V); assert m0==37
MAT={'MA':'bem_suportado','EC':'moderadamente_suportado','OB':'moderadamente_suportado','ML':'moderadamente_suportado'}
for i,r in enumerate(AT,start=1):
    role,des=mapa(r)
    V.append({'id_vinculo':f'VINC_B4_{m0+i:03d}','id_referencia_interna':r['id'],'pmid_oficial':r['pmid'],
      'secao_origem':'B4_CANONICA','trecho_ancora':grp_lines[r['id']],
      'mecanismo_origem':'mecanismo_B4_deficiencias_monoaminas','natureza_relacao':'contributiva',
      'grau_maturidade':MAT[r['tag']],'forca_causal':('tier_3_associacao_humana' if r['tag'] in('EC','MA') else 'tier_4_descritivo_estrutural'),
      'especie_mesh':r['especie_mesh'],'evid_role':role,'verification_status':'verificado','citacao_confirmada':True,
      'g1_metodo':'eutils_automatico','g2_elegibilidade':'eligible',
      'g2_motivo':'escopo B4 confirmado em auditoria [AT] (título/abstract MeSH)',
      'g3_verificado_por':'IA G3 (geração) — B4 [AT 2026-09-08]; P-6 2a verificacao independente (avaliador cego) PENDENTE'})
assert len(V)==m0+94==131
json.dump(V,open(BASE+'Evidencias/Vinculos/vinculos_referencia_afirmacao.json','w'),ensure_ascii=False,indent=1)
# ledger
L=json.load(open(BASE+'Auditoria_B4/ledger_auditoria_B4.json')); k0=len(L); assert k0==37
for i,r in enumerate(AT,start=1):
    role,des=mapa(r)
    L.append({'id_auditoria':f'AUD_B4_{k0+i:04d}','mecanismo':'B4','id_referencia_interna':r['id'],
      'pmid_oficial':r['pmid'],'arquivo_modulo09':'Evidencias/Bibliografia/01_pmids.json','tipo_classificador':'',
      'origem_entrada':'POLITICA_FONTES','claim_id':r['claim_id'],'secao_origem':'B4_CANONICA',
      'trecho_ancora':grp_lines[r['id']],'citacao_literal':r['label']+'['+r['tag']+']',
      'natureza_da_relacao':'contributiva','grau_maturidade_cientifica':MAT[r['tag']],
      'forca_causal':('tier_3_associacao_humana' if r['tag'] in('EC','MA') else 'tier_4_descritivo_estrutural'),
      'forca_biologica_conexao':'','especie_mesh':r['especie_mesh'],'evid_role':role,
      'portao_G1_existencia':'VERIFIED_REFERENCE','portao_G2_elegibilidade':'ELIGIBLE_SOURCE',
      'portao_G3_suporte':'APROVADO','status_auditoria':'APROVADO','destino':'FICA_MECANISMO',
      'acao_correcao':'MANTER','reconciliado':True,
      'verificacao':{'verificador':'IA G3 (geração) — B4 [AT 2026-09-08]; P-6 2a verificacao independente (avaliador cego) PENDENTE',
        'data_verificacao':'2026-09-08','g1_metodo':'eutils_automatico',
        'abstract_ou_trecho':r['abstract'][:900],'query_utilizada':'efetch pmid='+r['pmid'],
        'g2_motivo':'escopo B4 confirmado em auditoria [AT] (título/abstract MeSH; resgates DOI-PII quando aplicável)',
        'g3_nota':'rótulo insumo conferido (autor/ano/tema); falsos positivos=0 na leva; grupo '+r['grupo']}})
assert len(L)==k0+94==131
json.dump(L,open(BASE+'Auditoria_B4/ledger_auditoria_B4.json','w'),ensure_ascii=False,indent=1)
# manifesto
M=json.load(open(BASE+'Evidencias/Bibliografia/_manifesto_biblioteca.json'))
M['artefato_rotulo']='CANONICA v2'
M['pmids_total']=131
M['g1']={'metodo':'eutils_automatico','resolvidos':131}
M['g2']={'eligible':131}
M['g3']={'vinculos_n2':131,'CONFIRMADO':131}
M['corte_literatura']='E-utilities/PubMed 2026-09; GPM B4 v2 + insumo externo [AT] 2026-09-08'
M.setdefault('historico_correcoes',[]).append({'data':'2026-09-08','campo':'insumo externo B4 (P-7)',
 'erro_anterior':'37 refs (V1)','correcao':'+94 refs auditadas ref a ref (0 FP; 2 correções de autoria do insumo; 1 EXC tardia pós-abstract Evans_2024 Alzheimer)',
 'acao_downstream':'canônica V2 + 01_pmids/vínculos/ledger/manifesto atualizados; decisoes/P-4 com adendo V2'})
M.setdefault('atualizacoes_pos_publicacao',[]).append({'data':'2026-09-08','tipo':'AT_P7_INSUMO_EXTERNO','biblioteca':'B4','versao':'V2',
 'resumo':"Insumo 'matriz canônica B4' (177 itens + consolidação + briefing) auditado ref a ref (G1 eutils): 94 refs incorporadas (37→131); 0 FP; 2 correções de autoria; 1 EXC tardia pós-abstract (Alzheimer); 13 EXC escopo; 57 baixo incremento; 12 não-resolvidos; P-6 pendente.",
 'refs_adicionadas':[r['pmid'] for r in AT]})
json.dump(M,open(BASE+'Evidencias/Bibliografia/_manifesto_biblioteca.json','w'),ensure_ascii=False,indent=1)
# trilha
T={'at_ciclo':'2026-09-08','biblioteca':'B4','at_status':'INCORPORADO_V2',
 'insumo':{'arquivo':'uploads/Artigos cientificos do mecanismo B4 Deficiencias monoaminas.md','itens':177,'consolidacao_texto':True,'briefing_sementes':14},
 'incorporadas':[{'pmid':r['pmid'],'id':r['id'],'grupo':r['grupo'],'tag':r['tag']} for r in AT],
 'exc_tardia_pos_abstract':[{'pmid':'39696597','rotulo_insumo':'Evans 2024','motivo':'modelo 5XFAD de doença de Alzheimer — fora de escopo permanente; corte no abstract'}],
 'excluidas_escopo':13,'baixo_incremento':57,'falhas_nao_resolvidas':12,
 'correcoes_autoria':[{'insumo':'Martinez 2010','real':'Goddard AW 2010 (PMID 19960531)'},{'insumo':'Ogden 2006','real':'Parsey RV 2006 (PMID 16154547)'}],
 'falsos_positivos':0,'p6':'PENDENTE (2a verificacao cega, Via 2)'}
json.dump(T,open(BASE+'producao/04_AT_ciclo_2026-09-08.json','w'),ensure_ascii=False,indent=1)
print('JSON OK: pmids',len(A),'vinculos',len(V),'ledger',len(L))
