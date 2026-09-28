#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
from pathlib import Path
BASE=Path(__file__).resolve().parent
abs_=json.loads((BASE/"corpus/abstracts_pubmed.json").read_text(encoding="utf-8"))
out=BASE/"ato2_pacote"
M={"LCL_biom_2021":"32327735","RCT_infliximab":"22945416","PlastDep_2016":"26937618",
"IL6resol_2015":"25697833","Osimo_meta":"32113908","IFNcancer_2002":"11927189",
"Trp_2002":"12082564","IFN_HPA_2016":"26703235","HepC_2000":"10827143",
"Reward_2022":"35927580","RewardTrauma_2020":"32291455","Capuron2003":"12615197"}
N1=[
("REF_LCL_biom_2021","EC humano (Mol Psychiatry; linfoblastos)","human_clinical","linhagens de linfoblastos de deprimidos: biomarcadores distinguem remitters de nao-remitters; resposta ao farmaco depende do estado imune/transcricional basal","baixa (humano; celular)"),
("REF_RCT_infliximab","RCT (JAMA Psychiatry; N=60)","human_clinical","inflamacao alta prediz nao-resposta a antidepressivo e resposta ao anti-TNF; citocina sabotam mecanismo de acao do antidepressivo","baixa (humano)"),
("REF_PlastDep_2016","Review (humano)","human_clinical","plasticidade sinaptica e antidepressivos de acao rapida na interface estresse/BDNF/CREB","baixa (revisao)"),
("REF_IL6resol_2015","Coorte humano (Psychol Med)","human_clinical","IL-6 baixa prediz melhor resolucao de sintomas; gradiente dose-resposta marcador->sintoma","baixa (humano)"),
("REF_IFNcancer_2002","EC humano (Neuropsychopharmacology; melanoma N=40)","human_experimental","IFN-alfa induz clusters neuropsiquiatricos especificos ao longo de 3 meses; previne/reverte com paroxetina; cronologia e fenomenologia","baixa (humano; intervencao)"),
("REF_Trp_2002","EC humano (Mol Psychiatry)","human_experimental","queda de triptofano serico durante terapia com citocinas associada a sintomas depressivos (consistente com IDO/quinurenina)","baixa (humano)"),
("REF_IFN_HPA_2016","EC humano (Physiol Behav; hepatite C)","human_experimental","inflamacao por IFN-alfa reduz feedback negativo de glicocorticoide (resistencia HPA)","baixa (humano)"),
("REF_HepC_2000","Review clinico (Hepatology; SEM abstract)","human_clinical","hepatite C/IFN-alfa e depressao; revisao clinica do paradigma (requer full text no G3)","baixa (humano; sem abstract)"),
("REF_Reward_2022","EC humano (Mol Psychiatry; fMRI)","human_clinical","inflamacao elevada na TDM associada a baixa conectividade funcional cortico-estriatal de recompensa e anedonia; impacto sobre dopamina","baixa (humano)"),
("REF_RewardTrauma_2020","EC humano (Soc Cogn Affect Neurosci; fMRI; N=56)","human_clinical","em mulheres expostas a trauma, PCR/citocinas elevadas associam-se a alteracao do circuito de recompensa e anedonia/TEPT","baixa (humano)"),
]
n1=[]
for refid,desenho,role,achado,ext in N1:
    pmid=M[refid[4:]]; r=abs_[pmid]
    n1.append({"id_referencia_interna":refid,"pmid_oficial":pmid,"doi":r["doi"],"titulo_artigo":r["titulo"],
      "autores":r["autores"][:6],"revista_ano":f"{r['revista']} ({r['ano']})","desenho_estudo":desenho,
      "secao_origem":"mecanismo_B1_neuroinflamacao/BLOCO_06","achado_central_molecular":achado,
      "extrapolacao_por_analogia":ext,"status_auditoria":"","claim_id_origem":"","citacao_confirmada":True,
      "origem_pipeline":"BUSCA_FERRAMENTA","g1_metodo":"eutils_automatico","g3_verificado_por":"",
      "especie_mesh":r["especie_mesh"],"evid_role":role,"verification_status":"pendente"})
V=[
("REF_LCL_biom_2021","B1.MEC.BLOCO06.001","BLOCO_06/6.1","Em linhagens celulares humanas (linfoblastos) de pacientes deprimidos, biomarcadores de resposta a antidepressivo distinguem remitters de não-remitters, sugerindo que a resposta ao fármaco depende do estado imune/transcricional basal","causal","moderadamente_suportado","tier_3_correlacional_mecanistico","baixa (humano celular)","human_clinical","contexto_mecanistico"),
("REF_RCT_infliximab","B1.MEC.BLOCO06.001","BLOCO_06/6.1","Isso explica por que, no subgrupo inflamado, a falha ao SSRI é mais comum (a inflamação \"sabota\" os mecanismos de ação do antidepressivo, como o próprio RCT do infliximabe enquadra — Raison et al., 2013)","causal","bem_suportado","tier_1_necessidade_e_suficiencia","baixa (humano RCT)","human_clinical","clinico"),
("REF_PlastDep_2016","B1.MEC.BLOCO06.001","BLOCO_06/6.1","Plasticidade sináptica e antidepressivos de ação rápida são revista nesta interface","contributiva","moderadamente_suportado","","baixa (revisao)","human_clinical","contexto_mecanistico"),
("REF_IL6resol_2015","B1.MEC.BLOCO06.002","BLOCO_06/6.2","níveis mais altos de marcadores associam-se a sintomas mais graves e a pior resolução (IL-6 baixa prediz melhor resolução de sintomas em sofrimento psicológico","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
("REF_Osimo_meta","B1.MEC.BLOCO06.002","BLOCO_06/6.2","A meta-análise de variabilidade (Osimo et al., 2020)[MA; humano] mostra que não há \"deprimido inflamado\" binário — a elevação é contínua e concentrada num subgrupo","associativa","muito_estabelecido","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
("REF_IFNcancer_2002","B1.MEC.BLOCO06.003","BLOCO_06/6.3","Análise dimensional dos sintomas em pacientes com melanoma mostra clusters neuropsiquiátricos específicos que emergem ao longo dos primeiros três meses e são prevenidos/revertidos por paroxetina","causal","bem_suportado","tier_1_necessidade_e_suficiencia","baixa (humano intervencao)","human_experimental","clinico"),
("REF_Trp_2002","B1.MEC.BLOCO06.003","BLOCO_06/6.3","O mecanismo bioquímico inclui queda de triptofano sérico associada aos sintomas depressivos","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","baixa (humano)","human_experimental","contexto_mecanistico"),
("REF_IFN_HPA_2016","B1.MEC.BLOCO06.003","BLOCO_06/6.3","A inflamação por IFN-α também reduz o feedback negativo de glicocorticoide (resistência ao eixo HPA), ligando inflamação à disfunção do estresse","causal","moderadamente_suportado","tier_2_necessidade_ou_suficiencia","baixa (humano)","human_experimental","contexto_mecanistico"),
("REF_Reward_2022","B1.MEC.BLOCO06.004","BLOCO_06/6.4","Em TDM, inflamação elevada associa-se a baixa conectividade funcional nos circuitos cortico-estriatais de recompensa e a sintomas de anedonia — relação que envolve impacto da inflamação sobre síntese/liberação de dopamina","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
("REF_RewardTrauma_2020","B1.MEC.BLOCO06.004","BLOCO_06/6.4","Em mulheres expostas a trauma, PCR/citocinas elevadas associam-se a alteração do circuito de recompensa e a anedonia/sintomas de TEPT","associativa","moderadamente_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
]
corpo=(out/"CHECKPOINT_06_BLOCO06_corpo.md").read_text(encoding="utf-8").replace("**","")
cflat=re.sub(r"\s+"," ",corpo); frases=re.findall(r"[^.].*?\.\s",cflat+" ")
def acha(p):
    c=[f.strip() for f in frases if p[:34] in f]
    return c[0] if c else None
# Osimo meta ref: usar do n1 do bloco05? nao — referenciar como meta ja existente; incluir ref local
r=abs_["32113908"]
n1.append({"id_referencia_interna":"REF_Osimo_meta","pmid_oficial":"32113908","doi":r["doi"],"titulo_artigo":r["titulo"],
  "autores":r["autores"][:6],"revista_ano":f"{r['revista']} ({r['ano']})","desenho_estudo":"Meta-analise (humano)",
  "secao_origem":"mecanismo_B1_neuroinflamacao/BLOCO_06","achado_central_molecular":"meta de variabilidade: elevacao continua concentrada em subgrupo (gradiente)",
  "extrapolacao_por_analogia":"baixa (humano)","status_auditoria":"","claim_id_origem":"","citacao_confirmada":True,
  "origem_pipeline":"BUSCA_FERRAMENTA","g1_metodo":"eutils_automatico","g3_verificado_por":"",
  "especie_mesh":r["especie_mesh"],"evid_role":"human_clinical","verification_status":"pendente"})
n2=[]
for i,(refid,claim,secao,probe,nat,mat,forca,ext,role,uso) in enumerate(V,1):
    t=acha(probe)
    achado=next((x["achado_central_molecular"] for x in n1 if x["id_referencia_interna"]==refid),"")
    n2.append({"id_vinculo":f"VINC_B1_{6000+i:04d}","id_referencia_interna":refid,"claim_id":claim,
      "mecanismo_origem":"B1","secao_origem":secao,"trecho_ancora":(t or probe+"."),"achado_central_molecular":achado,
      "natureza_relacao":nat,"grau_maturidade":mat,"forca_causal":forca,"extrapolacao_por_analogia":ext,
      "evid_role":role,"uso":uso,"status_referencia":"CANDIDATO","status_auditoria":"",
      "verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"",
      "g1_metodo":"eutils_automatico","g3_verificado_por":""})
ids1={x["id_referencia_interna"] for x in n1}; prob=[]
for v in n2:
    t=re.sub(r"\s+"," ",v["trecho_ancora"]).strip()
    if t[-1] not in '.!?]': prob.append(("PONT",v["id_vinculo"]))
    if t not in cflat: prob.append(("LIT",v["id_vinculo"],t[:30]))
    if v["id_referencia_interna"] not in ids1: prob.append(("REF",v["id_vinculo"]))
for x in n1:
    if x["pmid_oficial"] not in abs_: prob.append(("PMID",x["pmid_oficial"]))
print("N1:",len(n1),"N2:",len(n2),"| problemas:",prob if prob else "NENHUM")
(out/"mod9_BLOCO06_N1_01_pmids.json").write_text(json.dumps(n1,ensure_ascii=False,indent=1),encoding="utf-8")
(out/"mod9_BLOCO06_N2_vinculos.json").write_text(json.dumps(n2,ensure_ascii=False,indent=1),encoding="utf-8")
