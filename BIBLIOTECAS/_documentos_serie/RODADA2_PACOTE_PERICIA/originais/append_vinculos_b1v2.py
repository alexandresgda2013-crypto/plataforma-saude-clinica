#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Acrescenta vínculos Nível-2 (referência↔frase) das subseções novas da B1 v2,
alinhados ao schema já existente no vinculos_referencia_afirmacao.json."""
import json
from pathlib import Path
BIB=Path("/home/user/pipeline_auditoria_conteudo/BIBLIOTECAS/B01_Neuroinflamacao/Evidencias/Bibliografia/01_pmids.json")
F=Path("/home/user/pipeline_auditoria_conteudo/BIBLIOTECAS/B01_Neuroinflamacao/Evidencias/Vinculos/vinculos_referencia_afirmacao.json")
refs=json.load(open(BIB,encoding="utf-8"))
# rótulo -> pmid
rot2pmid={}
for it in refs:
    for full in it.get("ids_referencia_interna",[]):
        rot2pmid[full.replace("REF_","")]=it.get("pmid_oficial")

d=json.load(open(F,encoding="utf-8"))
n0=len(d)
existe={v.get("id_referencia_interna") for v in d}

def V(rot,secao,ancora,verif,role,forca):
    iid=f"REF_{rot}"
    if iid in existe:  # não duplicar
        return
    d.append({
      "id_vinculo":f"VINC_B1V2_{len(d)+1:04d}",
      "id_referencia_interna":iid,
      "claim_id":"",
      "mecanismo_origem":"mecanismo_B1_neuroinflamacao",
      "secao_origem":f"mecanismo_B1_neuroinflamacao/{secao}",
      "trecho_ancora":ancora,
      "achado_central_molecular":ancora,
      "natureza_relacao":forca,
      "grau_maturidade":("bem_suportado" if verif in ("verificado",) else ("emergente" if "extrapolado" in verif else "bem_suportado")),
      "forca_causal":forca,
      "extrapolacao_por_analogia":("sim (animal/celula -> humano)" if verif in ("preclinico","extrapolado") else "baixa (humano)"),
      "evid_role":role,
      "uso":"B1_v2",
      "status_referencia":"VALIDADO_G3_IA",
      "status_auditoria":"G1_G2_G3_B1v2",
      "verification_status":verif,
      "data_verificacao":"2026-09-04",
      "g2_elegibilidade":("eligible" if True else ""),
      "g2_motivo":"",
      "g1_metodo":"eutils_automatico",
      "g3_verificado_por":"IA_revisora (G3 B1 v2, 2026-09-04)",
      "pmid_oficial":rot2pmid.get(rot,""),
      "g3_notas":""})

P="preclinical_mechanistic"; H="human_clinical"; HE="human_experimental"
tc="tier_3_correlacional_mecanistico"; t4="tier_4_descritivo_estrutural"; ti="tier_2_intervencao"
V("Glicolise_microglia_2021","BLOCO02/2.25","glicolise aerobica controla ativacao inflamatoria microglial por LPS","preclinico",P,tc)
V("Glicolise_hipocampo_2022","BLOCO02/2.25","neuroinflamacao LPS induz chaveamento glicolitico no hipocampo de rato","preclinico",P,tc)
V("Succinato_HIF_2013","BLOCO02/2.25","succinato estabiliza HIF-1alfa e induz IL-1beta em macrofago","preclinico",P,tc)
V("Itaconato_Nrf2_2023","BLOCO02/2.25","itaconato/IRG1 inibe NLRP3 e ativa Nrf2 (revisao)","extrapolado",P,tc)
V("IRG1_itaconato_2025","BLOCO02/2.25","eixo glicolitico IRG1/itaconato/NRF2 regulado por LPS em microglia","preclinico",P,tc)
V("Necroptose_dep_2022","BLOCO02/2.26","RIPK1/RIPK3/MLKL na reducao de astrocitos sob estresse cronico (CUMS)","preclinico",P,tc)
V("Cx43_hemicanal_2015","BLOCO02/2.27","microglia ativada abre hemicanais Cx43 astrocitarios (IL-1beta/TNF; glutamato)","preclinico",P,tc)
V("Cx43_GJ_2011","BLOCO02/2.27","neuroinflamacao altera juncoes comunicantes de forma regiao-dependente","preclinico",P,tc)
V("Cx43_antidep_2023","BLOCO02/2.27","Cx43 astrocitario proposto como alvo antidepressivo (revisao)","extrapolado",P,tc)
V("AQP4_glinfatica_2024","BLOCO02/2.27","cetamina melhora glinfatica reduzindo piroptose astrocitaria/AQP4","preclinico",P,tc)
V("Glinfatica_RM_2025","BLOCO02/2.27","disfuncao glinfatica no comportamento tipo-depressivo (DCE-RM; AQP4)","preclinico",P,tc)
V("Amigdala_citocinas_2025","BLOCO03/3.16","IL-17A/C ansiogenico vs IL-10 ansiolitico em neuronios da BLA (camundongo)","preclinico",P,tc)
V("IL18_amigdala_2017","BLOCO03/3.16","IL-18 local na BLA regula suscetibilidade ao estresse cronico","preclinico",P,tc)
V("P2X7_NaK_ansiedade_2024","BLOCO03/3.16","ruptura NKAalfa1-P2X7 microglial promove comportamento tipo-ansiedade","preclinico",P,tc)
V("TET2_NLRP3_2023","BLOCO03/3.16","deficiencia de TET2 ativa NLRP3/IL-1beta e induz ansiedade (rinite alergica)","preclinico",P,tc)
V("NLRP3_def_ansiedade_2021","BLOCO03/3.16","deficiencia de NLRP3 tambem gera comportamento tipo-ansiedade (direcao nao monotonica)","preclinico",P,tc)
V("Renna_ansiedade_2018","BLOCO06/6.6","citocinas pro-inflamatorias elevadas em ansiedade/TEPT/TOC (efeito modesto; moderado por depressao)","verificado",H,t4)
V("Costello_ansiedade_2019","BLOCO06/6.6","citocinas perifericas no TAG: alteracoes com heterogeneidade (14 estudos)","verificado",H,t4)
V("TOC_imune_2019","BLOCO06/6.6","TOC: citocinas NAO diferiram significativamente dos controles (resultado nulo)","verificado",H,t4)
V("Panico_citocinas_2018","BLOCO06/6.6","panico: IL-6/IL-1beta elevados em parte dos estudos; resultados mistos (revisao narrativa)","verificado",H,t4)
V("PTSD_marc_2015","BLOCO06/6.6","marcadores inflamatorios elevados no TEPT (meta-analise)","verificado",H,t4)
V("PTSD_supressao_2020","BLOCO06/6.6","TEPT associado a supressao neuroimune (TSPO-PET + pos-morte)","verificado",H,t4)
V("TSPO_estresse_2022","BLOCO06/6.6","TSPO como alvo diagnostico/terapeutico em doencas relacionadas ao estresse (revisao)","verificado",H,t4)
V("Ansiedade_ped_2021","BLOCO06/6.6","inflamacao em ansiedade infantil/ADO: associacao proxima da significancia, inconsistente","verificado",H,t4)
V("Internalizante_ped_2022","BLOCO06/6.6","citocinas em internalizantes pediatricos (efeito dependente de moderadores)","verificado",H,t4)
V("Quinur_ansiedade_2018","BLOCO06/6.6","via imuno-quinurenina implicada na ansiedade (revisao)","verificado",H,t4)
V("Minociclina_medo_2024","BLOCO06/6.7","minociclina atenua retencao de memoria de medo em voluntarios saudaveis (RCT)","verificado",HE,ti)
V("Minociclina_extincao_2016","BLOCO06/6.7","minociclina reverte prejuizo de extincao do medo por IFN-alfa (rato)","preclinico",P,tc)
V("Mega_imunomod_2020","BLOCO06/6.7","imunomoduladores beneficiam sintomas depressivos no estrato com sintomas basais altos","verificado",HE,ti)
V("Omega3_ansiedade_2018","BLOCO06/6.7","omega-3 associado a reducao de sintomas de ansiedade (meta-analise)","verificado",HE,ti)

json.dump(d,open(F,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("vínculos antes:",n0,"| depois:",len(d),"| adicionados:",len(d)-n0)
