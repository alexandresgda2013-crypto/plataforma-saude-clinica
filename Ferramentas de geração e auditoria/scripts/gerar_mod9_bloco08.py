#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
from pathlib import Path
BASE=Path(__file__).resolve().parent
abs_=json.loads((BASE/"corpus/abstracts_pubmed.json").read_text(encoding="utf-8"))
out=BASE/"ato2_pacote"
M={"GR_repress_2018":"29424686","FKBP_inflam_2020":"32622856","IFN_HPA_2016":"26703235",
"IL1b_BDNF_1993":"8492907","Poda_2012":"22632727","GutC3_2024":"38378622","PDE4_2025":"39947489",
"MAMs_2024":"38890305","GutLPS_2024":"38491103","TLR4brain_2011":"22053929","Reward_2022":"35927580",
"VitD_2024":"38303529","SleepInflam_2023":"36608535","SleepIL6_2026":"42174628","D2_LPS_2004":"14684601",
"dio2_NFkB_2006":"16728495","Klengel_2013":"23201972","Holocausto_2016":"26410355","Estrogen_2022":"36552208"}
N1=[
("REF_GR_repress_2018","Experimental (eLife; macrófago/camundongo)","preclinical_mechanistic","GR reprime genes pro-inflamatorios por mecanismos gene-especificos (NELF/Pol2); base da repressao NF-kB pelo cortisol","sim (celula)"),
("REF_FKBP_inflam_2020","Review (humano+animal)","preclinical_mechanistic","FKBP e sinalizacao inflamatoria; FKBP5 modula sensibilidade do GR","parcial"),
("REF_IFN_HPA_2016","EC humano (Physiol Behav; hepatite C)","human_experimental","inflamacao por IFN-alfa reduz feedback negativo de glicocorticoide (resistencia HPA)","baixa (humano)"),
("REF_IL1b_BDNF_1993","Experimental (Neuroscience; rato)","preclinical_mechanistic","IL-1b sistemica reduz mRNA de BDNF no hipocampo","sim (rato)"),
("REF_Poda_2012","Experimental (Neuron; camundongo)","preclinical_mechanistic","microglia esculpe circuitos pos-natais de modo atividade- e complemento-dependentes (C1q/C3)","sim (desenvolvimento)"),
("REF_GutC3_2024","Experimental (Microbiome; camundongo)","preclinical_mechanistic","disbiose intestinal induz comportamento tipo-depressivo via poda anormal dependente de complemento C3","sim (camundongo)"),
("REF_PDE4_2025","Experimental (Brain Behav Immun; camundongo)","preclinical_mechanistic","inibicao de PDE4 alivia poda fagocitica excessiva microglial mediada por HMGB1/C1q/C3 na depressao","sim (camundongo)"),
("REF_MAMs_2024","Experimental (Nat Commun; camundongo)","preclinical_mechanistic","contatos reticulo-mitocondria (MAMs) na microglia mediam comportamento tipo-depressivo; loop inflamacao-mitocondria","sim (camundongo)"),
("REF_GutLPS_2024","Experimental (Sci Rep; camundongo)","preclinical_mechanistic","LPS derivado do intestino e TLR4 periferico medeiam inflamacao no estresse (translocacao bacteriana)","sim (camundongo)"),
("REF_TLR4brain_2011","Experimental (J Neuroinflammation; rato)","preclinical_mechanistic","estresse compromete barreira intestinal; estimulacao da via TLR4 cerebral relevante para depressao","sim (rato)"),
("REF_Reward_2022","EC humano (Mol Psychiatry; fMRI)","human_clinical","inflamacao reduz conectividade cortico-estriatal de recompensa e dopamina -> anedonia","baixa (humano)"),
("REF_VitD_2024","Review (Curr Pharm Des; humano+animal)","preclinical_mechanistic","vitamina D/VDR modula ativacao microglial e neuroinflamacao","parcial"),
("REF_SleepInflam_2023","Experimental (Microbiol Res; camundongo)","preclinical_mechanistic","privacao aguda de sono exacerba inflamacao sistemica e disturbios psiquiatricos","sim (camundongo)"),
("REF_SleepIL6_2026","Experimental (J Neuroinflammation; camundongo)","preclinical_mechanistic","privacao de sono induz ansiedade via IL-6 e eixo astrocito-GABA no PAG","sim (camundongo)"),
("REF_D2_LPS_2004","Experimental (Endocrinology; rato)","preclinical_mechanistic","LPS induz desiodase tipo 2 (D2) em tanicitos do hipotálamo mediobasal; converte T4->T3 no SNC","sim (rato)"),
("REF_dio2_NFkB_2006","Experimental (Endocrinology; rato/humano)","preclinical_mechanistic","gene dio2 humano tem elemento responsivo a NF-kB; LPS ativa D2 central","sim"),
("REF_Klengel_2013","Genetica/epigenetica humana (Nat Neurosci)","human_clinical","desmetilacao alelo-especifica de FKBP5 dependente de trauma infantil; resistencia a GR","baixa (humano)"),
("REF_Holocausto_2016","EC humano (Biol Psychiatry)","human_clinical","efeitos intergeracionais da exposicao ao Holocausto na metilacao de FKBP5 (sobreviventes e filhos)","baixa (humano)"),
("REF_Estrogen_2022","Review (Biology)","preclinical_mechanistic","17beta-estradiol derivado do cerebro (BDE2) modula ativacao glial; diferencas entre sexos","parcial"),
]
n1=[]
for refid,desenho,role,achado,ext in N1:
    pmid=M[refid[4:]]; r=abs_[pmid]
    n1.append({"id_referencia_interna":refid,"pmid_oficial":pmid,"doi":r["doi"],"titulo_artigo":r["titulo"],
      "autores":r["autores"][:6],"revista_ano":f"{r['revista']} ({r['ano']})","desenho_estudo":desenho,
      "secao_origem":"mecanismo_B1_neuroinflamacao/BLOCO_08","achado_central_molecular":achado,
      "extrapolacao_por_analogia":ext,"status_auditoria":"","claim_id_origem":"","citacao_confirmada":True,
      "origem_pipeline":"BUSCA_FERRAMENTA","g1_metodo":"eutils_automatico","g3_verificado_por":"",
      "especie_mesh":r["especie_mesh"],"evid_role":role,"verification_status":"pendente"})
V=[
("REF_GR_repress_2018","B1.MEC.BLOCO08.001","BLOCO_08/8.1","O glicocorticoide ativado (GR) reprime potemente a inflamação de macrófagos; análise genômica mostra que o GR reprime genes pró-inflamatórios por mecanismos gene-específicos","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (celula)","preclinical_mechanistic","contexto_mecanistico"),
("REF_IFN_HPA_2016","B1.MEC.BLOCO08.001","BLOCO_08/8.1","A inflamação por IFN-α reduz o feedback negativo do HPA em humanos","causal","moderadamente_suportado","tier_2_necessidade_ou_suficiencia","baixa (humano)","human_experimental","contexto_mecanistico"),
("REF_IL1b_BDNF_1993","B1.MEC.BLOCO08.002","BLOCO_08/8.2","IL-1β/TNF suprimem BDNF/TrkB/CREB (ver BLOCO03.001/002; IL-1β reduz mRNA de BDNF hipocampal, 1993)","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (rato)","preclinical_mechanistic","contexto_mecanistico"),
("REF_Poda_2012","B1.MEC.BLOCO08.003","BLOCO_08/8.2","a poda sináptica mediada por complemento C1q/C3 pela micróglia é necessária ao desenvolvimento","causal","muito_estabelecido","tier_2_necessidade_ou_suficiencia","sim (desenvolvimento; excesso adulto e [EXT])","preclinical_mechanistic","contexto_mecanistico"),
("REF_GutC3_2024","B1.MEC.BLOCO08.003","BLOCO_08/8.2","quando excessiva no adulto é candidata a perda sináptica na depressão: a disbiose intestinal induz comportamento tipo-depressivo via poda anormal dependente de complemento","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","gap_pesquisa"),
("REF_PDE4_2025","B1.MEC.BLOCO08.003","BLOCO_08/8.2","e a inibição de PDE4 alivia poda fagocítica excessiva mediada por HMGB1/C1q/C3","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","gap_pesquisa"),
("REF_MAMs_2024","B1.MEC.BLOCO08.006","BLOCO_08/8.3","Os contatos retículo-mitocôndria (MAMs) na micróglia medeiam comportamento tipo-depressivo","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","gap_pesquisa"),
("REF_GutLPS_2024","B1.MEC.BLOCO08.005","BLOCO_08/8.4","LPS derivado do intestino e TLR4 periférico medeiam inflamação no estresse","causal","moderadamente_suportado","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico"),
("REF_TLR4brain_2011","B1.MEC.BLOCO08.005","BLOCO_08/8.4","e a estimulação da via TLR4 cerebral no estresse crônico é relevante para depressão","causal","moderadamente_suportado","tier_2_necessidade_ou_suficiencia","sim (rato)","preclinical_mechanistic","contexto_mecanistico"),
("REF_Reward_2022","B1.MEC.BLOCO08.007","BLOCO_08/8.5","Em paralelo, IFN-α/inflamação reduzem disponibilidade de dopamina em circuitos de recompensa, produzindo anedonia (ver BLOCO06.004: conectividade córtico-estriatal e anedonia, PMID 35927580)","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
("REF_VitD_2024","B1.MEC.BLOCO08.009","BLOCO_08/8.7","Micronutrientes modulam a ativação imune: vitamina D/VDR modula ativação microglial","contributiva","moderadamente_suportado","","parcial","preclinical_mechanistic","contexto_mecanistico"),
("REF_SleepInflam_2023","B1.MEC.BLOCO08.010","BLOCO_08/8.8","Privação de sono eleva IL-6/TNF/PCR: privação aguda de sono exacerba inflamação sistêmica e distúrbios psiquiátricos","causal","moderadamente_suportado","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico"),
("REF_SleepIL6_2026","B1.MEC.BLOCO08.010","BLOCO_08/8.8","e sono perdido induz ansiedade via IL-6 (IL-6 astrocyte PAG, 2026)","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","gap_pesquisa"),
("REF_D2_LPS_2004","B1.MEC.BLOCO08.011","BLOCO_08/8.9","LPS induz a desiodase tipo 2 (D2) em tanicitos do hipotálamo mediobasal — a principal enzima que converte T4 em T3 ativo no SNC","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (rato)","preclinical_mechanistic","contexto_mecanistico"),
("REF_dio2_NFkB_2006","B1.MEC.BLOCO08.011","BLOCO_08/8.9","e o gene dio2 humano tem elemento responsivo a NF-κB","causal","moderadamente_suportado","tier_2_necessidade_ou_suficiencia","sim","preclinical_mechanistic","contexto_mecanistico"),
("REF_Klengel_2013","B1.MEC.BLOCO08.012","BLOCO_08/8.10","desmetilação alelo-específica dependente de trauma (Klengel 2013, BLOCO02.20)","causal","muito_estabelecido","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
("REF_Holocausto_2016","B1.MEC.BLOCO08.012","BLOCO_08/8.10","e efeitos intergeracionais na metilação de FKBP5 em sobreviventes do Holocausto e seus filhos","associativa","moderadamente_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","contexto_mecanistico"),
("REF_Estrogen_2022","B1.MEC.BLOCO08.014","BLOCO_08/8.12","estrogênio/17β-estradiol derivado do cérebro (BDE2) modula ativação glial com diferenças entre sexos","contributiva","emergente","","parcial","preclinical_mechanistic","gap_pesquisa"),
]
corpo=(out/"CHECKPOINT_08_BLOCO08_corpo.md").read_text(encoding="utf-8").replace("**","")
cflat=re.sub(r"\s+"," ",corpo); frases=re.findall(r"[^.].*?\.\s",cflat+" ")
def acha(p):
    c=[f.strip() for f in frases if p[:32] in f]
    return c[0] if c else None
n2=[]
for i,(refid,claim,secao,probe,nat,mat,forca,ext,role,uso) in enumerate(V,1):
    t=acha(probe); achado=next(x["achado_central_molecular"] for x in n1 if x["id_referencia_interna"]==refid)
    n2.append({"id_vinculo":f"VINC_B1_{8000+i:04d}","id_referencia_interna":refid,"claim_id":claim,
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
(out/"mod9_BLOCO08_N1_01_pmids.json").write_text(json.dumps(n1,ensure_ascii=False,indent=1),encoding="utf-8")
(out/"mod9_BLOCO08_N2_vinculos.json").write_text(json.dumps(n2,ensure_ascii=False,indent=1),encoding="utf-8")
