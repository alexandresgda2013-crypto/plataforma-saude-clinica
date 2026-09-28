#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adiciona as 7 referências resgatadas no PubMed (Rodada 4) ao Módulo 9 e às listras."""
import json, re
from pathlib import Path
BASE=Path("/home/user/pipeline_auditoria_conteudo/BIBLIOTECAS/B01_Neuroinflamacao")
P=BASE/"Biblioteca_B1_NEUROINFLAMACAO_CANONICA.md"

# ------------ 1) registros novos no 01_pmids.json ------------
novos=[
 dict(pmid="28882317", tit="Persistent Increase in Microglial RAGE Contributes to Chronic Stress-Induced Priming of Depressive-like Behavior.",
   aut=["Franklin TC","et al."], rev="Biological psychiatry (2018)", des="ML camundongo (estresse cronico; microglial RAGE)",
   sec="BLOCO_02/2.7", ach="RAGE microglial elevado persistentemente contribui para priming induzido por estresse cronico de comportamento tipo-depressivo",
   ext="sim (camundongo -> humano)", role="preclinical_mechanistic", ver="preclinico",
   ids=["REF_RAGE_stress_2018"]),
 dict(pmid="41160920", tit="Trans-cinnamaldehyde alleviates IFN-alpha-induced depressive-like behaviors by restoring astrocytic function.",
   aut=["Zhou R","et al."], rev="International immunopharmacology (2025)", des="ML camundongo (IFN-alfa; trans-cinamaldeido; astrocito)",
   sec="BLOCO_02/2.16", ach="trans-cinamaldeido alivia comportamento tipo-depressivo induzido por IFN-alfa restaurando funcao astrocitaria",
   ext="sim (camundongo -> humano)", role="preclinical_mechanistic", ver="preclinico",
   ids=["REF_Cinnam_2025"]),
 dict(pmid="39220869", tit="Mitophagy and cGAS-STING crosstalk in neuroinflammation.",
   aut=["Zhou X","et al."], rev="Acta pharmaceutica Sinica B (2024)", des="OB revisao",
   sec="BLOCO_02/2.18", ach="crosstalk mitofagia-cGAS-STING na neuroinflamacao (mtDNA/mitofagia regula STING)",
   ext="sim (revisao mecanistica; extrapolado para TDM)", role="preclinical_mechanistic", ver="extrapolado",
   ids=["REF_Mitophagy_cGAS_2024"]),
 dict(pmid="41094684", tit="cGAS-STING signaling in brain aging and neurodegeneration: molecular links and therapeutic perspectives.",
   aut=["Li H","et al."], rev="Journal of neuroinflammation (2025)", des="OB revisao",
   sec="BLOCO_02/2.18", ach="sinalizacao cGAS-STING no envelhecimento cerebral/neurodegeneracao; vazamento de mtDNA como alvo terapeutico",
   ext="sim (revisao; extrapolado para TDM)", role="preclinical_mechanistic", ver="extrapolado",
   ids=["REF_cGAS_aging_2025"]),
 dict(pmid="37597297", tit="Improving outcomes in intracerebral hemorrhage through microglia/macrophage-targeted IL-10 delivery with phosphatidylserine liposomes.",
   aut=["Han R","et al."], rev="Biomaterials (2023)", des="ML camundongo (HIC; IL-10 direcionada a microglia/macrofago)",
   sec="BLOCO_02/2.19", ach="entrega de IL-10 direcionada a microglia/macrofago (lipossomos fosfatidilserina) melhora desfecho em hemorragia intracerebral",
   ext="sim (camundongo -> humano)", role="preclinical_mechanistic", ver="preclinico",
   ids=["REF_IL10_ICH_2023"]),
 dict(pmid="31951051", tit="A Systematic Review of DNA Methylation and Gene Expression Studies in Posttraumatic Stress Disorder.",
   aut=["Mehta D","et al."], rev="Journal of traumatic stress (2020)", des="OB revisao sistematica (humano; metilacao/expressao em TEPT)",
   sec="BLOCO_02/2.21", ach="revisao sistematica de metilacao de DNA e expressao genica (genes imunes/inflamatorios) em TEPT/fatores psicologicos",
   ext="baixa (humano; revisao)", role="human_clinical", ver="verificado",
   ids=["REF_MetilPTSD_2020"]),
 dict(pmid="34218905", tit="Preoperative inflammatory mediators and postoperative delirium: systematic review and meta-analysis.",
   aut=["Noah AM","et al."], rev="British journal of anaesthesia (2021)", des="MA revisao sistematica+meta-analise (humano; mediadores pre-operatorios incl. neopterina/IL-6)",
   sec="BLOCO_05/5.5", ach="mediadores inflamatorios pre-operatorios (neopterina, IL-6 etc.) associam-se a delirium pos-operatorio",
   ext="baixa (humano; contexto cirurgico)", role="human_clinical", ver="verificado",
   ids=["REF_Neopterin_surg_2021"]),
]
f=BASE/"Evidencias/Bibliografia/01_pmids.json"
d=json.load(open(f,encoding="utf-8"))
exist={r.get("pmid_oficial") for r in d}
for n in novos:
    if n["pmid"] in exist:
        print("já existe:",n["pmid"]); continue
    d.append({
      "pmid_oficial":n["pmid"],"doi":"","titulo_artigo":n["tit"],"autores":n["aut"],
      "revista_ano":n["rev"],"desenho_estudo":n["des"],"secao_origem":"mecanismo_B1_neuroinflamacao/"+n["sec"],
      "achado_central_molecular":n["ach"],"extrapolacao_por_analogia":n["ext"],
      "status_auditoria":"VALIDADO_G3_IA (resgate Rodada 4, 2026-09-04)","claim_id_origem":"",
      "citacao_confirmada":True,"origem_pipeline":"BUSCA_FERRAMENTA","g1_metodo":"eutils_automatico",
      "g3_verificado_por":"IA_revisora (resgate pos-auditoria externa)","especie_mesh":["Humans"] if n["role"]=="human_clinical" else ["Animals"],
      "evid_role":n["role"],"verification_status":n["ver"],
      "ids_referencia_interna":n["ids"]})
json.dump(d,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("banco agora com",len(d),"PMIDs")

# ------------ 2) listras (com quebra de linha segura) ------------
t=P.read_text(encoding="utf-8")
def add(sec, addlabel):
    global t
    i=t.find(sec); assert i>=0,sec
    j=t.find("### ",i+5)
    blk=t[i:j]
    ms=[m for m in re.finditer(r"^\*([^*\n]+)\*\s*$",blk,re.M) if re.search(r"\[(?:MA|EC|OB|ML|AT)\]",m.group(0))]
    m=ms[-1]; linha=m.group(0).rstrip()
    if addlabel.split("[")[0] in linha: print(sec,"já tem"); return
    nova=linha[:-1].rstrip()+" | "+addlabel+"*"
    t=t[:i]+blk[:m.start()]+nova+"\n"+blk[m.end():]+t[j:]
    print(sec,"->",nova[:90])

add("### 2.7","RAGE_stress_2018[ML]")
add("### 2.16","Cinnam_2025[ML]")
add("### 2.18","Mitophagy_cGAS_2024[OB] | cGAS_aging_2025[OB]")
add("### 2.19","IL10_ICH_2023[ML]")
add("### 2.21","MetilPTSD_2020[OB]")
add("### 5.5","Neopterin_surg_2021[MA]")
# separa qualquer listra colada em cabeçalho
t=re.sub(r"(\*[^\n*]*\[(?:MA|EC|OB|ML|AT)\][^\n*]*\*)(#{1,3} )", r"\1\n\n\2", t)
P.write_text(t,encoding="utf-8")
print("coladas:", len(re.findall(r"\*[^\n*]*\[(?:MA|EC|OB|ML|AT)\][^\n*]*\*(?=#{1,3} )", t)))
