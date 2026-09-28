# -*- coding: utf-8 -*-
import json, unicodedata
BASE='/home/user/BIBLIOTECAS/B13_SistemaEndocanabinoide/'
doc=unicodedata.normalize('NFC', open(BASE+'B13 SISTEMA ENDOCANABINOIDE V2 CANONICA.md',encoding='utf-8').read())
R=json.load(open(BASE+'producao/insumos/b13_refs_data.json'))
P=json.load(open(BASE+'Evidencias/Bibliografia/01_pmids.json'))
V=json.load(open(BASE+'Evidencias/Vinculos/vinculos_referencia_afirmacao.json'))
L=json.load(open(BASE+'Auditoria_B13/ledger_auditoria_B13.json'))
M=json.load(open(BASE+'Evidencias/Bibliografia/_manifesto_biblioteca.json'))
n0=len(P); assert len(P)==len(V)==len(L)==167
ESP={"REF_GUNDUZCINAR_2016":"(Gunduz-Cinar 2016)","REF_DEMELOREIS_2021":"(de Melo Reis 2021)","REF_BORGESASSIS_2023":"(Borges-Assis 2023)","REF_MCWHIRTER_2024":"(McWhirter 2024)","REF_GOLDSTEINFERBER_2021":"(Goldstein Ferber 2021)","REF_ZARAZUAGUZMAN_2024":"(Zarazúa-Guzmán 2024)"}
HOJE="2026-09-09"; SCH=["_nat","_mat","_acao","_tier"]
for i,r in enumerate(R):
    rid=r['id_referencia_interna']; tag=r['desenho_estudo'][1:3]
    e=ESP.get(rid) or f"({rid[4:].rsplit('_',1)[0].capitalize()} {rid.rsplit('_',1)[1]})"
    alvo=f"{e}[{tag}]"
    linhas=[l for l in doc.split('\n') if alvo in l and not l.startswith('*')]
    esc=[l for l in linhas if doc.count(l)==1 and len(l)>30]
    assert esc, f"trecho p/ {rid}"
    trecho=esc[0]
    g2="eligible" if tag in("EC","OB") else "redirecionado_mecanistico"
    portao="ELIGIBLE_SOURCE" if tag in("EC","OB") else "NAO_APLICAVEL"
    p={k:v for k,v in r.items() if k not in SCH}
    P.append(p)
    V.append({"id_vinculo":f"VINC_B13_{168+i:03d}","id_referencia_interna":rid,"pmid_oficial":r['pmid_oficial'],
      "secao_origem":"B13_CANONICA_V2","trecho_ancora":trecho,"mecanismo_origem":"mecanismo_B13_sistema_endocanabinoide",
      "natureza_relacao":r['_nat'],"grau_maturidade":r['_mat'],"forca_causal":r['_tier'],
      "especie_mesh":r['especie_mesh'],"evid_role":r['evid_role'],"verification_status":r['verification_status'],
      "citacao_confirmada":True,"g1_metodo":"eutils_automatico","g2_elegibilidade":g2,"g2_motivo":p['g2_motivo'],
      "g3_verificado_por":"IA G3 Rodada [AT] GPM B13 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
      "status_auditoria":"CONFIRMADO","status_referencia":"CONFIRMADA",
      "uso":"nucleo_causal" if tag=="ML" else "suporte","data_verificacao":HOJE,
      "segunda_verificacao":"P-6 pendente — 2ª verificação cega (Via 2) a executar no fechamento da rodada 16/16"})
    L.append({"id_auditoria":f"AUD_B13_{168+i:04d}","mecanismo":"B13","id_referencia_interna":rid,
      "pmid_oficial":r['pmid_oficial'],"arquivo_modulo09":"Evidencias/Bibliografia/01_pmids.json","tipo_classificador":"",
      "origem_entrada":"GPM","claim_id":"B13.MEC.BLOCO14.001","secao_origem":"B13_CANONICA_V2","trecho_ancora":trecho,
      "citacao_literal":f"{e}[{tag}]","natureza_da_relacao":r['_nat'],"grau_maturidade_cientifica":r['_mat'],
      "forca_causal":r['_tier'],"forca_biologica_conexao":"","especie_mesh":r['especie_mesh'],"evid_role":r['evid_role'],
      "portao_G1_existencia":"VERIFIED_REFERENCE","portao_G2_elegibilidade":portao,"portao_G3_suporte":"APROVADO",
      "status_auditoria":"APROVADO","destino":"FICA_MECANISMO","acao_correcao":r['_acao'],"reconciliado":True,
      "verificacao":{"verificador":"IA G3 Rodada [AT] GPM B13 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
      "data_verificacao":HOJE,"g1_metodo":"eutils_automatico (esearch+esummary+efetch)",
      "abstract_ou_trecho":"abstract lido antes da incorporação (direção confirmada)" if r['pmid_oficial'] in json.load(open(BASE+'producao/insumos/b13_efetch_sel.json')) else "título/metadados confirmados via esummary",
      "query_utilizada":"esearch autor+tema quando divergente; esummary autor+ano+tema",
      "g2_motivo":p['g2_motivo'],
      "g3_nota":"rodada [AT] — insumo GPM+RODADA0+matriz ChatGPT auditado ref a ref"+(" | alias: "+"; ".join(r['_aliases']) if r['_aliases'] else "")}})
for F,d in [('Evidencias/Bibliografia/01_pmids.json',P),('Evidencias/Vinculos/vinculos_referencia_afirmacao.json',V),('Auditoria_B13/ledger_auditoria_B13.json',L)]:
    json.dump(d, open(BASE+F,'w'), indent=1, ensure_ascii=False)
ids=[x['id_referencia_interna'] for x in P]
assert len(ids)==len(set(ids)) and len(P)==len(V)==len(L)==207
M['artefato_rotulo']="CANONICA v2"; M['rodada']=4; M['data_corte']=HOJE; M['pmids_total']=207
M.setdefault('historico_correcoes',[]).append({"data":HOJE,"campo":"rodada [AT] GPM B13","correcao":"ENTRA 40 (18 âncoras+22 selecionados) / BAIXO 19 / EXC 4. 6 chaves divergentes com alias; falso mapeamento Spohrs2021→vídeo neurocirúrgico EXC; Segev real localizado (falso par Șerban); [G1] McWhirter/Zabik-RCT/Spohrs-publicado RESOLVIDOS; Ibarra-Lecue já vigente; anos=print (Garani 2021, Warren 2022, Morena 2019, GoldsteinFerber 2021, Lu 2021, Ribeiro 2021, Uzuneser 2023).","acao_downstream":"P-6 ampliado p/ levas [AT] B1–B16"})
M['g3']={"vinculos_n2":207}; M['versao']="2.6"; M['corte_literatura']="E-utilities/PubMed 2026-09-09 (rodada [AT])"
g2e=M.get('g2',{})
M['g2']={"eligible": g2e.get('eligible',0)+24, "redirecionado_mecanistico": g2e.get('redirecionado_mecanistico',0)+16}
M['pendencias_fase']=["P-6 (2ª verificação cega, Via 2) pendente — cobre B1–B16 incluindo levas [AT]"]
json.dump(M, open(BASE+'Evidencias/Bibliografia/_manifesto_biblioteca.json','w'), indent=1, ensure_ascii=False)
json.dump({"ciclo":"AT","data":HOJE,"biblioteca":"B13","versao_resultante":"V2","rodada_resultante":4,
 "decisao":{"ENTRA":40,"BAIXO":19,"EXC":4},"refs_total":207,"palavras_v2":len(doc.split()),
 "g1_resolvidos":["McWhirter (sexo feminino)","Zabik-RCT (→via 10 exógena)","Spohrs versão publicada","Ibarra-Lecue (já vigente)"],
 "exposicoes":["6 chaves divergentes normalizadas com alias","'Spohrs 2021' = vídeo neurocirúrgico (EXC, exposto)","'Segev 2018' do dossiê = Șerban 2025 (BAIXO); Segev real localizado"]},
 open(BASE+'producao/04_AT_ciclo_2026-09-09.json','w'), indent=1, ensure_ascii=False)
print("tríade:", len(P), len(V), len(L))
