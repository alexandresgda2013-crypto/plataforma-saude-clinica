# -*- coding: utf-8 -*-
import json, unicodedata
BASE='/home/user/BIBLIOTECAS/B12_NeurobiologiaTrauma/'
doc=unicodedata.normalize('NFC', open(BASE+'B12 NEUROBIOLOGIA DO TRAUMA V2 CANONICA.md',encoding='utf-8').read())
R=json.load(open(BASE+'producao/insumos/b12_refs_data.json'))
P=json.load(open(BASE+'Evidencias/Bibliografia/01_pmids.json'))
V=json.load(open(BASE+'Evidencias/Vinculos/vinculos_referencia_afirmacao.json'))
L=json.load(open(BASE+'Auditoria_B12/ledger_auditoria_B12.json'))
M=json.load(open(BASE+'Evidencias/Bibliografia/_manifesto_biblioteca.json'))
assert len(P)==len(V)==len(L)==37
ESP={"REF_HEIM_2001a":"(Heim & Nemeroff 2001)","REF_VONWERNEBAES_2012":"(Von Werne Baes 2012)","REF_WINGENFELD_2015":"(Wingenfeld 2015)","REF_PAQUOLA_2016":"(Paquola 2016)","REF_MCTEAGUE_2020":"(McTeague 2020)","REF_CHEIRAN_2022":"(Cheiran 2022)","REF_SERRABLASCO_2021":"(Serra-Blasco 2021)","REF_BENZION_2024":"(Ben-Zion 2024)","REF_DELCASALE_2022":"(Del Casale 2022)","REF_DIBENEDETTO_2022":"(Di Benedetto 2022)","REF_DEKLOET_2016":"(de Kloet 2016)","REF_TERHEEGDE_2015":"(ter Heegde 2015)","REF_SUAREZJIMENEZ_2020":"(Suarez-Jimenez 2020)","REF_ODOHERTY_2015":"(O'Doherty 2015)","REF_RENGASAMY_2021":"(Rengasamy 2021)","REF_NIKKHESLAT_2020":"(Nikkheslat 2020)","REF_JANIRI_2020":"(Janiri 2020)"}
HOJE="2026-09-09"; SCH=["_nat","_mat","_acao","_tier"]
for i,r in enumerate(R):
    rid=r['id_referencia_interna']; tag=r['desenho_estudo'][1:3]
    e=ESP.get(rid) or f"({rid[4:].rsplit('_',1)[0].capitalize()} {rid.rsplit('_',1)[1]})"
    alvo=f"{e}[{tag}]"
    linhas=[l for l in doc.split('\n') if alvo in l and not l.startswith('*')]
    escolhidas=[l for l in linhas if doc.count(l)==1]
    assert escolhidas, f"sem trecho único p/ {rid}"
    trecho=escolhidas[0]
    g2="eligible" if tag in("EC","OB") else "redirecionado_mecanistico"
    portao="ELIGIBLE_SOURCE" if tag in("EC","OB") else "NAO_APLICAVEL"
    p={k:v for k,v in r.items() if k not in SCH}
    p['g2_elegibilidade']=g2; p['g2_motivo']="humano clínico/síntese — elegível" if tag in("EC","OB") else "animal/modelo causal — redirecionado"
    P.append(p)
    V.append({"id_vinculo":f"VINC_B12_{38+i:03d}","id_referencia_interna":rid,"pmid_oficial":r['pmid_oficial'],
      "secao_origem":"B12_CANONICA_V2","trecho_ancora":trecho,"mecanismo_origem":"mecanismo_B12_neurobiologia_trauma",
      "natureza_relacao":r['_nat'],"grau_maturidade":r['_mat'],"forca_causal":r['_tier'],
      "especie_mesh":r['especie_mesh'],"evid_role":r['evid_role'],"verification_status":r['verification_status'],
      "citacao_confirmada":True,"g1_metodo":"eutils_automatico","g2_elegibilidade":g2,"g2_motivo":p['g2_motivo'],
      "g3_verificado_por":"IA G3 Rodada [AT] GPM B12 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
      "status_auditoria":"CONFIRMADO","status_referencia":"CONFIRMADA",
      "uso":"nucleo_causal" if tag=="ML" else "suporte","data_verificacao":HOJE,
      "segunda_verificacao":"P-6 pendente — 2ª verificação cega (Via 2) a executar no fechamento da rodada 16/16"})
    L.append({"id_auditoria":f"AUD_B12_{38+i:04d}","mecanismo":"B12","id_referencia_interna":rid,
      "pmid_oficial":r['pmid_oficial'],"arquivo_modulo09":"Evidencias/Bibliografia/01_pmids.json","tipo_classificador":"",
      "origem_entrada":"GPM","claim_id":"B12.MEC.BLOCO14.001","secao_origem":"B12_CANONICA_V2","trecho_ancora":trecho,
      "citacao_literal":f"{e}[{tag}]","natureza_da_relacao":r['_nat'],"grau_maturidade_cientifica":r['_mat'],
      "forca_causal":r['_tier'],"forca_biologica_conexao":"","especie_mesh":r['especie_mesh'],"evid_role":r['evid_role'],
      "portao_G1_existencia":"VERIFIED_REFERENCE","portao_G2_elegibilidade":portao,"portao_G3_suporte":"APROVADO",
      "status_auditoria":"APROVADO","destino":"FICA_MECANISMO","acao_correcao":r['_acao'],"reconciliado":True,
      "verificacao":{"verificador":"IA G3 Rodada [AT] GPM B12 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
      "data_verificacao":HOJE,"g1_metodo":"eutils_automatico (esearch+esummary+efetch)",
      "abstract_ou_trecho":"abstract lido antes da incorporação (direção do resultado confirmada)" if r['pmid_oficial'] in json.load(open(BASE+'producao/insumos/b12_efetch_sel.json')) else "título/metadados confirmados via esummary",
      "query_utilizada":"esearch DOI[aid] quando divergente; esummary autor+ano+tema",
      "g2_motivo":p['g2_motivo'],
      "g3_nota":"rodada [AT] — insumo GPM+RODADA0+matriz ChatGPT auditado ref a ref"+(" | alias: "+"; ".join(r['_aliases']) if r['_aliases'] else "")}})
for F,data in [('Evidencias/Bibliografia/01_pmids.json',P),('Evidencias/Vinculos/vinculos_referencia_afirmacao.json',V),('Auditoria_B12/ledger_auditoria_B12.json',L)]:
    json.dump(data, open(BASE+F,'w'), indent=1, ensure_ascii=False)
ids=[x['id_referencia_interna'] for x in P]
assert len(ids)==len(set(ids)) and len(P)==len(V)==len(L)==111
M['artefato_rotulo']="CANONICA v2"; M['rodada']=4; M['data_corte']=HOJE; M['pmids_total']=111
M['g2']={"eligible": M.get('g2',{}).get('eligible',0)+len([r for r in R if r['desenho_estudo'][1:3] in('EC','OB')]), "redirecionado_mecanistico": M.get('g2',{}).get('redirecionado_mecanistico',0)+4}
M['g3']={"vinculos_n2":111}; M['versao']="2.6"; M['corte_literatura']="E-utilities/PubMed 2026-09-09 (rodada [AT])"
M.setdefault('historico_correcoes',[]).append({"data":HOJE,"campo":"rodada [AT] GPM B12","correcao":"Reconciliação de insumo (36 âncoras+146) auditada ref a ref: ENTRA 74 / BAIXO ~55 / EXC malha. 12 chaves divergentes normalizadas com alias; PMIDs inválidos do insumo (Logue) documentados; TBI fora (regra 6); V1->V2; 46 citações re-costuradas; anos=print (Wingenfeld 2015, Janiri 2020, Nikkheslat 2020, Price 2020, Tian 2021, Wang 2022, Chavanne 2021, Fiksdal 2019, Tyagi 2026, Cheiran 2022).","acao_downstream":"P-6 ampliado p/ levas [AT] B1–B16"})
M['pendencias_fase']=["P-6 (2ª verificação cega, Via 2) pendente — cobre B1–B16 incluindo levas [AT]","ressalva de fase: citacao_literal de listras legadas — avisos não bloqueantes do framework"]
json.dump(M, open(BASE+'Evidencias/Bibliografia/_manifesto_biblioteca.json','w'), indent=1, ensure_ascii=False)
json.dump({"ciclo":"AT","data":HOJE,"biblioteca":"B12","versao_resultante":"V2","rodada_resultante":4,
 "universo_auditado":"36 âncoras (2 já vigentes) + 146 não citadas + NAO-IDX",
 "decisao":{"ENTRA":74,"BAIXO_aprox":55,"EXC":"TBI×6, Alzheimer/neurodegeneração×5, psicose, stroke, substância, NAO-IDX×7"},
 "refs_total":111,"palavras_v2":len(doc.split()),
 "exposicoes":["12 chaves divergentes normalizadas com alias (See→Serra-Blanco; Mayer→McTeague; Teo→terHeegde; Oyarce→Espinoza; Deuter→DiBenedetto; Begni→BenZion; Ferracuti→DelCasale; Pereira→Cheiran; Daskalakis→Dell'Oste; Fullana→Gędek; Romeo→Sălcudean; Cheng→Colucci-D'Amato; Ashworth-dossiê→Badowska; Vogelzangs=duplicata Von Werne Baes)","PMID inválido de Logue já corrigido pelo insumo (documentado)","sinalizados V1 não localizados no insumo permanecem [G1]"]},
 open(BASE+'producao/04_AT_ciclo_2026-09-09.json','w'), indent=1, ensure_ascii=False)
print("tríade:", len(P), len(V), len(L))
