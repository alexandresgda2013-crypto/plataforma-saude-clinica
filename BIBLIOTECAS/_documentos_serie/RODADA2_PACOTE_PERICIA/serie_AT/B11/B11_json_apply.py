# -*- coding: utf-8 -*-
import json, unicodedata, datetime
BASE='/home/user/BIBLIOTECAS/B11_DisfuncaoTireoidiana/'
V2=BASE+'B11 DISFUNCAO TIREOIDIANA V2 CANONICA.md'
doc=unicodedata.normalize('NFC', open(V2,encoding='utf-8').read())
R=json.load(open(BASE+'producao/insumos/b11_refs_data.json'))
P=json.load(open(BASE+'Evidencias/Bibliografia/01_pmids.json'))
V=json.load(open(BASE+'Evidencias/Vinculos/vinculos_referencia_afirmacao.json'))
L=json.load(open(BASE+'Auditoria_B11/ledger_auditoria_B11.json'))
M=json.load(open(BASE+'Evidencias/Bibliografia/_manifesto_biblioteca.json'))
assert len(P)==len(V)==len(L)==40
MAP={"REF_ROADUENAS_2024":"(Roa Dueñas 2024)","REF_ROMEROGOMEZ_2019":"(Romero-Gómez 2019)"}
HOJE="2026-09-09"
SCH_KEYS=["_nat","_mat","_acao","_tier"]
novos_p, novos_v, novos_l = [], [], []
for i,r in enumerate(R):
    rid=r['id_referencia_interna']; tag=r['desenho_estudo'][1:3]
    sob=rid[4:].rsplit('_',1)[0]; ano=rid.rsplit('_',1)[1]
    cit=MAP.get(rid, f"({sob.capitalize()} {ano})")
    alvo=cit.split(')')[0]+f")[{tag}]"
    linhas=[l for l in doc.split('\n') if alvo in l]
    assert len(linhas)>=1, f"sem linha p/ {rid}"
    trecho=None
    for l in linhas:
        if doc.count(l)==1 and not l.startswith('*'): trecho=l; break
    assert trecho, f"trecho não único p/ {rid}"
    g2 = "eligible" if tag in ("EC","OB") else r['g2_elegibilidade']
    portao = "ELIGIBLE_SOURCE" if tag in ("EC","OB") else "NAO_APLICAVEL"
    p={k:v for k,v in r.items() if k not in SCH_KEYS}
    p['g2_elegibilidade']=g2; p['g2_motivo']="humano clínico observacional/síntese — elegível" if tag in("EC","OB") else r['g2_motivo']
    p['verification_status']="humano_clinico"
    novos_p.append(p)
    nv={"id_vinculo":f"VINC_B11_{41+i:03d}","id_referencia_interna":rid,"pmid_oficial":r['pmid_oficial'],
        "secao_origem":"B11_CANONICA_V2","trecho_ancora":trecho,"mecanismo_origem":"mecanismo_B11_disfuncao_tireoidiana",
        "natureza_relacao":r['_nat'],"grau_maturidade":r['_mat'],"forca_causal":r['_tier'],
        "especie_mesh":["Humans"],"evid_role":r['evid_role'],"verification_status":"humano_clinico",
        "citacao_confirmada":True,"g1_metodo":"eutils_automatico","g2_elegibilidade":g2,
        "g2_motivo":p['g2_motivo'],"g3_verificado_por":"IA G3 Rodada [AT] GPM B11 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
        "status_auditoria":"CONFIRMADO","status_referencia":"CONFIRMADA","uso":"suporte",
        "data_verificacao":HOJE,"segunda_verificacao":"P-6 pendente — 2ª verificação cega (Via 2) a executar no fechamento da rodada 16/16"}
    novos_v.append(nv)
    nl={"id_auditoria":f"AUD_B11_{41+i:04d}","mecanismo":"B11","id_referencia_interna":rid,
        "pmid_oficial":r['pmid_oficial'],"arquivo_modulo09":"Evidencias/Bibliografia/01_pmids.json",
        "tipo_classificador":"","origem_entrada":"GPM","claim_id":"B11.MEC.BLOCO14.001",
        "secao_origem":"B11_CANONICA_V2","trecho_ancora":trecho,"citacao_literal":cit+f"[{tag}]",
        "natureza_da_relacao":r['_nat'],"grau_maturidade_cientifica":r['_mat'],"forca_causal":r['_tier'],
        "forca_biologica_conexao":"","especie_mesh":["Humans"],"evid_role":r['evid_role'],
        "portao_G1_existencia":"VERIFIED_REFERENCE","portao_G2_elegibilidade":portao,"portao_G3_suporte":"APROVADO",
        "status_auditoria":"APROVADO","destino":"FICA_MECANISMO","acao_correcao":"MANTER","reconciliado":True,
        "verificacao":{"verificador":"IA G3 Rodada [AT] GPM B11 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
        "data_verificacao":HOJE,"g1_metodo":"eutils_automatico (esearch+esummary+efetch)",
        "abstract_ou_trecho":"abstract lido antes da incorporação (direção do resultado confirmada)",
        "query_utilizada":"esearch DOI[aid]/autor+ano quando divergente; esummary autor+ano+tema; efetch abstract",
        "g2_motivo":p['g2_motivo'],"g3_nota":"rodada [AT] — insumo GPM+RODADA0+matriz ChatGPT auditado ref a ref"}}
    if rid=="REF_SOHEILI_2023":
        nl['verificacao']['g3_nota']+=" | correção editorial Zhang 2024 (registrada como metadado/_aliases, não referência)"
    novos_l.append(nl)
P.extend(novos_p); V.extend(novos_v); L.extend(novos_l)
ids=[x['id_referencia_interna'] for x in P]
assert len(ids)==len(set(ids)) and len(P)==len(V)==len(L)==96
json.dump(P, open(BASE+'Evidencias/Bibliografia/01_pmids.json','w'), indent=1, ensure_ascii=False)
json.dump(V, open(BASE+'Evidencias/Vinculos/vinculos_referencia_afirmacao.json','w'), indent=1, ensure_ascii=False)
json.dump(L, open(BASE+'Auditoria_B11/ledger_auditoria_B11.json','w'), indent=1, ensure_ascii=False)
# manifesto
M['artefato_rotulo']="CANONICA v2"; M['rodada']=4; M['data_corte']=HOJE
M['pmids_total']=96
M['g2']={"eligible": 20+len([r for r in novos_p if r['g2_elegibilidade']=='eligible']), "redirecionado_mecanistico":10}
M['g3']={"vinculos_n2":96}
M['versao']="2.6"; M['corte_literatura']="E-utilities/PubMed 2026-09-09 (rodada [AT])"
M.setdefault('historico_correcoes',[]).append({"data":HOJE,"campo":"rodada [AT] GPM B11","correcao":"Reconciliação de insumo externo (RODADA0+GPM+matriz ChatGPT) auditada ref a ref: ENTRA 56 / BAIXO 41 / EXC 11 grupos. Roca 1990 real localizado (era mapeado a Romero-Gómez 2019); correção editorial de Soheili 2023 como metadado; Ao/Eckert/Kirnap fora da malha expostos; Toma 2026 tema corrigido; 'Watanave 2018' mantido [G1]. 27 citações legadas re-costuradas (higiene).","acao_downstream":"P-6 ampliado p/ cobrir levas [AT] B1–B16"})
M['pendencias_fase']=["P-6 (2ª verificação cega, Via 2) pendente — cobre B1–B16 incluindo todas as levas [AT]","ressalva de fase: listras legadas com citacao_literal no formato listra — avisos não bloqueantes do framework"]
json.dump(M, open(BASE+'Evidencias/Bibliografia/_manifesto_biblioteca.json','w'), indent=1, ensure_ascii=False)
# trilha
json.dump({"ciclo":"AT","data":HOJE,"biblioteca":"B11","versao_resultante":"V2","rodada_resultante":4,
 "insumos":["RODADA0 (dossiê)","GPM oficial","matriz ChatGPT B11 (APROVADO_COM_RESSALVAS)","anexo de artigos","briefing consolidado v1"],
 "universo_auditado":"14 âncoras + 121 não citadas + 19 NAO-IDX + correção editorial",
 "decisao":{"ENTRA":56,"BAIXO":41,"EXC_grupos":11},
 "refs_total":96,"palavras_v2":len(doc.split()),
 "exposicoes":["Roca 1990 real = artigo de elevações transitórias (Endocr Res 1990); o PMID do dossiê era Romero-Gómez 2019","Zhang 2024 = correção editorial de Soheili 2023 (metadado)","Ao = tumor ósseo primário (EXC)","Eckert = diabetes tipo 1 (EXC)","Kirnap = DTC iatrogênico (EXC)","Toma 2026 tema corrigido (triagem, não NTIS)","Watanave 2018 [G1]"],
 "portoes":{"gate_P5":"pendente nesta etapa","framework":"pendente","checklist":"pendente"}},
 open(BASE+'producao/04_AT_ciclo_2026-09-09.json','w'), indent=1, ensure_ascii=False)
print("tríade pós-apply:", len(P), len(V), len(L))
