# -*- coding: utf-8 -*-
import json, unicodedata
BASE='/home/user/BIBLIOTECAS/B05_GabaGlutamato/'
AT=json.load(open(BASE+'producao/insumos/matriz_b5_at_final.json'))
assert len(AT)==116
doc=open(BASE+'B5 GABA GLUTAMATO V2 CANONICA.md').read()
up=lambda s: unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()
grp_lines={}
for r in AT:
    key=r['label']+'['+r['tag']+']'
    for line in doc.splitlines():
        if line.startswith('*') and key in line: grp_lines[r['id']]=line; break
    assert r['id'] in grp_lines, 'sem listra: '+r['id']
def mapa(r):
    tag=r['tag']; pts=r['pubtype']
    if tag=='MA': return 'meta_analise','meta-analise'
    if tag=='OB': return 'revisao_mecanistica','revisao_narrativa'
    if tag=='EC':
        des='RCT' if any('Randomized' in p for p in pts) else 'estudo_humano'
        role='human_experimental' if des=='RCT' or 'Clinical Trial' in pts else 'human_clinical'
        return role,des
    return 'preclinico_mecanistico','estudo_preclinico_animal'
A=json.load(open(BASE+'Evidencias/Bibliografia/01_pmids.json')); n0=len(A); assert n0==44
for r in AT:
    role,des=mapa(r)
    ext='[APENAS PRÉ-CLÍNICO] —' if r['tag']=='ML' else ''
    A.append({'pmid_oficial':r['pmid'],'titulo_artigo':r['titulo'],'autores':r['autores'],
      'revista_ano':f"{r['fonte']} {r['ano']}",'desenho_estudo':des,
      'secao_origem':'mecanismo_B5_gaba_glutamato','achado_central_molecular':'',
      'extrapolacao_por_analogia':ext,'ids_referencia_interna':[r['id']],
      'evid_role':role,'especie_mesh':r['especie_mesh'],'verification_status':'verificado',
      'citacao_confirmada':True,'g1_metodo':'eutils_automatico','g2_elegibilidade':'eligible',
      'g2_motivo':'escopo B5 confirmado em auditoria [AT] (título/abstract MeSH; DOI resolvido)',
      'g3_verificado_por':'IA G3 (geração) — B5 [AT 2026-09-08]; P-6 2a verificacao independente (avaliador cego) PENDENTE',
      'status_auditoria':'CONFIRMADO','origem_pipeline':'ATUALIZACAO_AT_2026-09-08 (insumos externos auditados)',
      'id_referencia_interna':r['id'],'doi':'','claim_id_origem':r['claim_id'],
      '_aliases':[r['label'].split('_')[0], up(r['label'].split('_')[0]).upper()]})
assert len(A)==n0+116==160
json.dump(A,open(BASE+'Evidencias/Bibliografia/01_pmids.json','w'),ensure_ascii=False,indent=1)
V=json.load(open(BASE+'Evidencias/Vinculos/vinculos_referencia_afirmacao.json')); m0=len(V); assert m0==44
MAT={'MA':'bem_suportado','EC':'moderadamente_suportado','OB':'moderadamente_suportado','ML':'moderadamente_suportado'}
for i,r in enumerate(AT,start=1):
    role,des=mapa(r)
    V.append({'id_vinculo':f'VINC_B5_{m0+i:03d}','id_referencia_interna':r['id'],'pmid_oficial':r['pmid'],
      'secao_origem':'B5_CANONICA','trecho_ancora':grp_lines[r['id']],
      'mecanismo_origem':'mecanismo_B5_gaba_glutamato','natureza_relacao':'contributiva',
      'grau_maturidade':MAT[r['tag']],'forca_causal':'tier_4_descritivo_estrutural',
      'especie_mesh':r['especie_mesh'],'evid_role':role,'verification_status':'verificado','citacao_confirmada':True,
      'g1_metodo':'eutils_automatico','g2_elegibilidade':'eligible',
      'g2_motivo':'escopo B5 confirmado em auditoria [AT] (título/abstract MeSH)',
      'g3_verificado_por':'IA G3 (geração) — B5 [AT 2026-09-08]; P-6 2a verificacao independente (avaliador cego) PENDENTE',
      'status_auditoria':'CONFIRMADO'})
assert len(V)==m0+116==160
json.dump(V,open(BASE+'Evidencias/Vinculos/vinculos_referencia_afirmacao.json','w'),ensure_ascii=False,indent=1)
L=json.load(open(BASE+'Auditoria_B5/ledger_auditoria_B5.json')); k0=len(L); assert k0==44
for i,r in enumerate(AT,start=1):
    role,des=mapa(r)
    abstr=r['abstract'].strip()
    verificacao={'verificador':'IA G3 (geração) — B5 [AT 2026-09-08]; P-6 2a verificacao independente (avaliador cego) PENDENTE',
      'data_verificacao':'2026-09-08','g1_metodo':'eutils_automatico',
      'abstract_ou_trecho':(abstr[:900] if abstr else f"[SEM ABSTRACT NO PUBMED] verificação G1 por título+periódico+autor (efetch/esummary). Título: '{r['titulo']}' — {r['fonte']} {r['ano']}."),
      'query_utilizada':'esearch doi[aid]→esummary→efetch pmid='+r['pmid'],
      'g2_motivo':'escopo B5 confirmado em auditoria [AT] (título/abstract MeSH)',
      'g3_nota':'rótulo insumo conferido (autor/ano/tema); grupo '+r['grupo']+(' | NEG/CONT preservado' if r['evid_role'] in ('NEG','CONT') else '')}
    L.append({'id_auditoria':f'AUD_B5_{k0+i:04d}','mecanismo':'B5','id_referencia_interna':r['id'],
      'pmid_oficial':r['pmid'],'arquivo_modulo09':'Evidencias/Bibliografia/01_pmids.json','tipo_classificador':'',
      'origem_entrada':'POLITICA_FONTES','claim_id':r['claim_id'],'secao_origem':'B5_CANONICA',
      'trecho_ancora':grp_lines[r['id']],'citacao_literal':r['label']+'['+r['tag']+']',
      'natureza_da_relacao':'contributiva','grau_maturidade_cientifica':MAT[r['tag']],
      'forca_causal':'tier_4_descritivo_estrutural','forca_biologica_conexao':'',
      'especie_mesh':r['especie_mesh'],'evid_role':role,
      'portao_G1_existencia':'VERIFIED_REFERENCE','portao_G2_elegibilidade':'ELIGIBLE_SOURCE',
      'portao_G3_suporte':'APROVADO','status_auditoria':'APROVADO','destino':'FICA_MECANISMO',
      'acao_correcao':'MANTER','reconciliado':True,'verificacao':verificacao})
assert len(L)==k0+116==160
json.dump(L,open(BASE+'Auditoria_B5/ledger_auditoria_B5.json','w'),ensure_ascii=False,indent=1)
M=json.load(open(BASE+'Evidencias/Bibliografia/_manifesto_biblioteca.json'))
M['artefato_rotulo']='CANONICA v2'; M['pmids_total']=160
if isinstance(M.get('g1'),dict): M['g1']={'metodo':'eutils_automatico','resolvidos':160}
if isinstance(M.get('g2'),dict): M['g2']={'eligible':160}
if isinstance(M.get('g3'),dict): M['g3']={'vinculos_n2':160,'CONFIRMADO':160}
M['corte_literatura']='E-utilities/PubMed 2026-09; GPM B5 v2 + insumos externos [AT] 2026-09-08'
M.setdefault('historico_correcoes',[]).append({'data':'2026-09-08','campo':'insumos externos B5 (P-7)','erro_anterior':'44 refs (V1)','correcao':'+116 refs auditadas ref a ref; 1 FP exposto (Prosowski [G1]); 3 correções de autoria; 5 correções de metadados do insumo confirmadas','acao_downstream':'canônica V2 + 01_pmids/vínculos/ledger/manifesto atualizados; decisoes/P-4 com adendo V2'})
M.setdefault('atualizacoes_pos_publicacao',[]).append({'data':'2026-09-08','tipo':'AT_P7_INSUMO_EXTERNO','biblioteca':'B5','versao':'V2','resumo':"Insumos B5 (consolidação + anexo 190 + briefing) auditados ref a ref: 116 incorporadas (44→160); 1 FP exposto; 3 correções autoria; 14 EXC escopo; 53 baixo incremento; 2 não-resolvidos; P-6 pendente.",'refs_adicionadas':[r['pmid'] for r in AT]})
json.dump(M,open(BASE+'Evidencias/Bibliografia/_manifesto_biblioteca.json','w'),ensure_ascii=False,indent=1)
A4p=BASE+'Evidencias/Bibliografia/04_atualizacoes_literatura.json'
A4=json.load(open(A4p)); assert A4==[] or isinstance(A4,list)
json.dump([],open(A4p,'w'))
T={'at_ciclo':'2026-09-08','biblioteca':'B5','at_status':'INCORPORADO_V2',
 'insumo':{'arquivos':['uploads/Artigos cientificos do mecanismo B5 Gaba Glutamato.md','uploads/BRIEFING_CONSOLIDADO_B5_v1.md','consolidação colada na conversa'],'itens':192,'resolvidos':190},
 'incorporadas':[{'pmid':r['pmid'],'id':r['id'],'grupo':r['grupo'],'tag':r['tag']} for r in AT],
 'falso_positivo':[{'rotulo_insumo':'Prosowski 2024 — Ketamine/Esketamine TRD','doi_apontava_para':'Zhang L 2026 (γ-butyrolactones)','destino':'NÃO ENTRA — artigo pretendido inexistente no PubMed [G1]'}],
 'correcoes_autoria':[{'insumo':'Matthew & Samba 2013','real':'Carver CM 2013 (PMID 24071826)'},{'insumo':'Pich & Millan 2018','real':'Cavalleri L 2018 (PMID 29158584)'},{'insumo':'Hollestein 2021','real':'Hollestein V 2023 (PMID 36681677; EXC autismo)'}],
 'excluidas_escopo':14,'baixo_incremento':53,'falhas':2,'ja_vigentes':6,'p6':'PENDENTE (2a verificacao cega, Via 2)'}
json.dump(T,open(BASE+'producao/04_AT_ciclo_2026-09-08.json','w'),ensure_ascii=False,indent=1)
print('JSON OK:',len(A),len(V),len(L))
