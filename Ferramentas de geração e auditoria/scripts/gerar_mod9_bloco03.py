#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
from pathlib import Path
BASE = Path(__file__).resolve().parent
abs_ = json.loads((BASE/"corpus/abstracts_pubmed.json").read_text(encoding="utf-8"))
out = BASE/"ato2_pacote"

# refid -> pmid
M = {
 "IL1b_BDNF_1993":"8492907","IL1b_NT3_2011":"22200088","Plasticity_2018":"29861718",
 "Etanercept_2009":"19027875","RepopIL6_2020":"32142677","Quimio_meta82_2017":"28122130",
 "TGFb_2025":"40946904","Antidep_meta_2018":"28445690","IFNg_PRIMING_2024":"39392762",
 "PrimingPrinc_2018":"29902514","NEK7_2025":"40602264","Antidep_microglia_2022":"35098788",
 "Psoriase_2025":"39960105","CCL2_2008":"18289346","CCR2_2005":"15781755",
 "Poda_2011":"21778362","CX3CL1_2026":"41192110","ICAM_2020":"32782234","Microvasc_2023":"36852396",
 "GutInfl_2020":"33362788","PSD_gut_2025":"41052746","Prob_2020":"32140393",
}

# (refid, desenho, role, achado, extrapol)
N1 = [
 ("REF_IL1b_BDNF_1993","Experimental (Neuroscience; rato, IL-1b sistemico)","preclinical_mechanistic","IL-1b sistemica reduz mRNA de BDNF no hipocampo; ligacao sinal imune periferico -> trofismo central","sim (rato)"),
 ("REF_IL1b_NT3_2011","Experimental (J Neuroinflammation; cultura/camundongo)","preclinical_mechanistic","IL-1b suprime sobrevivencia neuronal por neurotrofinas; interage com crescimento neuritico","sim (celula)"),
 ("REF_Plasticity_2018","Review (Neural Plast)","preclinical_mechanistic","citocinas residentes mantem plasticidade; elevadas (IL-1b/TNF) interferem com aprendizagem/cognicao, excitotoxicidade","parcial"),
 ("REF_Etanercept_2009","Review (humano; perispinal etanercepte)","human_clinical","bloqueio periferico de TNF (etanercepte perispinhal) explorado em disturbios neuroinflamatorios; efeito central sem cruzar BHE","baixa (humano, off-label)"),
 ("REF_RepopIL6_2020","Experimental (Cell; camundongo+humano)","preclinical_mechanistic","renovacao da microglia gera fenotipo neuroprotetor dependente de trans-sinalizacao IL-6 via sIL-6R/gp130; duplo papel do IL-6","sim (camundongo)"),
 ("REF_Quimio_meta82_2017","Meta-analise (Acta Psychiatr Scand; 82 estudos, humano)","human_clinical","IL-6, TNF, IL-10, CCL2 e quimiocinas alteradas em TDM vs controles (3212 TDM/2798 HC)","baixa (humano)"),
 ("REF_TGFb_2025","Review (Neuroscience; humano+animal)","preclinical_mechanistic","TGF-b1 reduzido em AD e TDM; via proposta como elo restaurativo compartilhado","sim"),
 ("REF_Antidep_meta_2018","Meta-analise (Prog Neuropsychopharmacol; humano)","human_clinical","antidepressivos deslocam balanco pro/anti-inflamatorio de marcadores perifericos","baixa (humano)"),
 ("REF_IFNg_PRIMING_2024","Experimental (CNS Neurosci Ther; cultura+camundongo)","preclinical_mechanistic","IFN-g induz priming microglial via STAT1 -> ativacao do NLRP3 (CD86/CD11b, morfologia hedgehog)","sim (celula/camundongo)"),
 ("REF_PrimingPrinc_2018","Review (Brain Behav Immun; humano+animal)","preclinical_mechanistic","principios de priming e inibicao do inflamassoma; P2X7 como sinal 2; implicacoes psiquiatricas","sim"),
 ("REF_NEK7_2025","Experimental (Int Immunopharmacol; rato)","preclinical_mechanistic","NEK7 (regulador de NLRP3) elevado em hipocampo (MS+CUMS); alvo modula piroptose e microbiota e alivia comportamento depressivo","sim (rato)"),
 ("REF_Antidep_microglia_2022","Review (J Psychopharmacol; humano+animal)","preclinical_mechanistic","antidepressivos (ISRS/IRSN) modulam ativacao microglial, morfologia, citocinas e stress oxidativo","parcial"),
 ("REF_Psoriase_2025","Review (Acta Physiol; humano+animal)","human_clinical","citocinas pro-inflamatorias e neuropeptideos conectam inflamacao sistemica/estresse/psoriase a depressao e ansiedade","baixa (humano, comorbidade)"),
 ("REF_CCL2_2008","Experimental (J Neurochem; cultura BMEC)","preclinical_mechanistic","CCL2 parenquimal atravessa endotelio microvascular cerebral por transcitose, formando gradiente para recrutar leucocitos","sim (celula BHE)"),
 ("REF_CCR2_2005","Experimental (Circulation; celula/humano/animal)","preclinical_mechanistic","CCR2 e receptor dominante de quimiotaxia de monocitos; estatina reduz CCR2 e recrutamento","sim"),
 ("REF_Poda_2011","Experimental (Science; camundongo)","preclinical_mechanistic","microglia fagocita material sinaptico e a poda e necessaria para o desenvolvimento normal pos-natal","sim (camundongo; desenvolvimento)"),
 ("REF_CX3CL1_2026","Experimental (Int Immunopharmacol; camundongo+celula humana)","preclinical_mechanistic","CX3CL1 atenua deficit neurologico e neuroinflamacao via CX3CR1/p38 MAPK/ERK1/2; eixo neuronio-microglia","sim (TBI/celula)"),
 ("REF_ICAM_2020","Experimental (Biomol Ther; astrocito)","preclinical_mechanistic","telmisartana inibe adesao leucocitaria induzida por TNF bloqueando ICAM-1 em astroglia; melhora depressao/memoria","sim (celula)"),
 ("REF_Microvasc_2023","Experimental (Mediators Inflamm; camundongo CRS)","preclinical_mechanistic","estresse cronico de restricao induz marcadores inflamatorios/oxidativos na microvasculatura cerebral","sim (camundongo)"),
 ("REF_GutInfl_2020","Review (humano+animal)","preclinical_mechanistic","eixo intestino-cerebro: microbiota e inflamassoma do hospedeiro influenciam fisiologia cerebral","sim"),
 ("REF_PSD_gut_2025","Experimental (Exp Neurol; rato)","preclinical_mechanistic","disbiose intestinal agrava depressao pos-AVE via inflamassoma NLRP3 microglial","sim (rato)"),
 ("REF_Prob_2020","Experimental (Acta Pharm Sin B; camundongo SAMP8)","preclinical_mechanistic","probióticos melhoram memoria e reduzem ativacao glial modulando eixo intestino-cerebro","sim (camundongo)"),
]

n1=[]
for refid, desenho, role, achado, extrapol in N1:
    key = refid[4:] if refid.startswith("REF_") else refid
    pmid=M[key]
    r=abs_[pmid]
    n1.append({"id_referencia_interna":refid,"pmid_oficial":pmid,"doi":r["doi"],
      "titulo_artigo":r["titulo"],"autores":r["autores"][:6],"revista_ano":f"{r['revista']} ({r['ano']})",
      "desenho_estudo":desenho,"secao_origem":"mecanismo_B1_neuroinflamacao/BLOCO_03",
      "achado_central_molecular":achado,"extrapolacao_por_analogia":extrapol,"status_auditoria":"",
      "claim_id_origem":"","citacao_confirmada":True,"origem_pipeline":"BUSCA_FERRAMENTA",
      "g1_metodo":"eutils_automatico","g3_verificado_por":"","especie_mesh":r["especie_mesh"],
      "evid_role":role,"verification_status":"pendente"})

# cada tupla: (refid, claim, secao, [chaves de busca da frase no corpo], natureza, maturidade, forca, extrapol, role, uso)
V = [
 ("REF_IL1b_BDNF_1993","B1.MEC.BLOCO03.001","BLOCO_03/3.1","O achado clássico: IL-1β sistêmica reduz a expressão de mRNA de BDNF no hipocampo de rato","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (rato)","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_Plasticity_2018","B1.MEC.BLOCO03.001","BLOCO_03/3.1","Em condições fisiológicas, citocinas residentes mantêm plasticidade; quando elevadas na neuroinflamação, IL-1β e TNF interferem com circuitos de aprendizado/cognição","contributiva","bem_suportado","","parcial","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_Plasticity_2018","B1.MEC.BLOCO03.002","BLOCO_03/3.2","O TNF tem papel fisiológico na plasticidade hebbiana e homeostática","associativa","bem_suportado","","parcial","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_Etanercept_2009","B1.MEC.BLOCO03.002","BLOCO_03/3.2","O bloqueio periférico de TNF com etanercepte por via perispinhal é explorado em distúrbios neuroinflamatórios","associativa","emergente","","baixa (humano off-label)","human_clinical","gap_pesquisa"),
 ("REF_RepopIL6_2020","B1.MEC.BLOCO03.003","BLOCO_03/3.3","mas induzir a renovação da população gera um fenótipo microglial neuroprotetor que auxilia a recuperação — e esse efeito benéfico depende criticamente da trans-sinalização de IL-6 via IL-6R solúvel + gp130","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_Quimio_meta82_2017","B1.MEC.BLOCO03.003","BLOCO_03/3.3","Na periferia, a meta-análise de 82 estudos confirma IL-6 elevada na TDM","associativa","muito_estabelecido","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
 ("REF_TGFb_2025","B1.MEC.BLOCO03.004","BLOCO_03/3.4","TGF-β1 é citocina imunorreguladora; níveis reduzidos são relatados tanto em Alzheimer quanto em depressão","associativa","moderadamente_suportado","","sim","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_Antidep_meta_2018","B1.MEC.BLOCO03.004","BLOCO_03/3.4","A meta-análise do efeito de antidepressivos sobre marcadores periféricos mostra deslocamento do balanço pró/anti-inflamatório","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
 ("REF_IFNg_PRIMING_2024","B1.MEC.BLOCO03.005","BLOCO_03/3.5","IFN-γ induz priming em micróglia por ativação STAT1-mediada do inflamassoma NLRP3","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (celula/camundongo)","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_PrimingPrinc_2018","B1.MEC.BLOCO03.005","BLOCO_03/3.5","Os princípios de priming e inibição do inflamassoma são revisados com implicações psiquiátricas","contributiva","bem_suportado","","sim","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_NEK7_2025","B1.MEC.BLOCO03.005","BLOCO_03/3.5","Em modelo de depressão, o alvo NEK7 (regulador a montante do NLRP3) modula piroptose e microbiota e alivia comportamento tipo-depressivo","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (rato)","preclinical_mechanistic","gap_pesquisa"),
 ("REF_Antidep_microglia_2022","B1.MEC.BLOCO03.006","BLOCO_03/3.6","Antidepressivos modulam a ativação microglial, deslocando o fenótipo para menos pró-inflamatório","contributiva","moderadamente_suportado","","parcial","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_Psoriase_2025","B1.MEC.BLOCO03.006","BLOCO_03/3.6","Citocinas pró-inflamatórias e neuropeptídeos conectam inflamação sistêmica, estresse e pele (psoríase) a depressão/ansiedade","associativa","moderadamente_suportado","","baixa (humano comorbidade)","human_clinical","contexto_mecanistico"),
 ("REF_Antidep_microglia_2022","B1.MEC.BLOCO03.007","BLOCO_03/3.7","Em camundongo, IFN-γ também priming astrocitário e a modulação por antidepressivos/anti-inflamatórios desloca o balanço","contributiva","emergente","","sim [EXT A1/A2 em TDM]","preclinical_mechanistic","gap_pesquisa"),
 ("REF_PrimingPrinc_2018","B1.MEC.BLOCO03.008","BLOCO_03/3.8","P2X7 é receptor de ATP extracelular em alta concentração que funciona como \"sinal 2\" do NLRP3","causal","bem_suportado","tier_3_correlacional_mecanistico","sim (celula/animal; comportamento [EXT])","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_CCL2_2008","B1.MEC.BLOCO03.009","BLOCO_03/3.9","A quimiocina CCL2 (MCP-1) produzida no parênquima atravessa o endotélio microvascular cerebral por transporte transcelular, formando um gradiente que recruta monócitos","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (celula BHE)","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_CCR2_2005","B1.MEC.BLOCO03.009","BLOCO_03/3.9","O receptor CCR2 é o receptor dominante de quimiotaxia de monócitos Ly6C^high; inibição de HMG-CoA redutase reduz expressão de CCR2 e recrutamento","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_ICAM_2020","B1.MEC.BLOCO03.012","BLOCO_03/3.9","telmisartana inibe adesão leucocitária induzida por TNF bloqueando ICAM-1 em astrócitos, com melhora de depressão/memória e redução de inflamação cerebral","causal","moderadamente_suportado","tier_2_necessidade_ou_suficiencia","sim (celula)","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_Microvasc_2023","B1.MEC.BLOCO03.012","BLOCO_03/3.9","Estresse crônico de restrição induz marcadores inflamatórios e oxidativos na microvasculatura cerebral","causal","emergente","tier_3_correlacional_mecanistico","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_CX3CL1_2026","B1.MEC.BLOCO03.010","BLOCO_03/3.10","Em lesão cerebral, CX3CL1 atenua déficit neurológico e neuroinflamação via CX3CR1/p38 MAPK/ERK1/2","causal","moderadamente_suportado","tier_2_necessidade_ou_suficiencia","sim (TBI/celula)","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_Poda_2011","B1.MEC.BLOCO03.010","BLOCO_03/3.10","Durante o desenvolvimento, a poda sináptica pela micróglia é necessária para a maturação normal do cérebro","causal","muito_estabelecido","tier_2_necessidade_ou_suficiencia","sim (desenvolvimento; poda adulta na TDM e [EXT])","preclinical_mechanistic","contexto_mecanistico"),
 ("REF_Quimio_meta82_2017","B1.MEC.BLOCO03.011","BLOCO_03/3.11","A meta-análise de 82 estudos confirma alterações periféricas de quimiocinas na TDM, incluindo CCL2 e quimiocinas correlacionadas a sintomas somáticos/fadiga","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
 ("REF_PSD_gut_2025","B1.MEC.BLOCO03.006","BLOCO_03/3.12","A disbiose intestinal agrava depressão pós-AVE via inflamassoma NLRP3 microglial","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (rato; cross-ref B7)","preclinical_mechanistic","gap_pesquisa"),
 ("REF_Prob_2020","B1.MEC.BLOCO03.006","BLOCO_03/3.12","probióticos melhoram déficit de memória modulando glia/eixo intestino-cérebro","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","gap_pesquisa"),
 ("REF_GutInfl_2020","B1.MEC.BLOCO03.006","BLOCO_03/3.12","A revisão de eixo intestino-cérebro e inflamassoma consolida como microbiota hospedeira influencia fisiologia cerebral","contributiva","bem_suportado","","sim","preclinical_mechanistic","contexto_mecanistico"),
]

corpo = (out/"CHECKPOINT_03_BLOCO03_corpo.md").read_text(encoding="utf-8").replace("**","")
cflat = re.sub(r"\s+"," ",corpo)
frases = re.findall(r"[^.].*?\.\s", cflat+" ")
def acha(probe):
    cand=[f.strip() for f in frases if probe[:40] in f]
    if cand: return cand[0]
    cand=[f.strip() for f in frases if probe[-40:] in f]
    return cand[0] if cand else None

n2=[]
for i,(refid,claim,secao,probe,nat,mat,forca,ext,role,uso) in enumerate(V,1):
    trecho=acha(probe)
    n2.append({"id_vinculo":f"VINC_B1_{2000+i:04d}","id_referencia_interna":refid,"claim_id":claim,
      "mecanismo_origem":"B1","secao_origem":secao,"trecho_ancora":trecho or probe+".",
      "achado_central_molecular":next(r["achado_central_molecular"] for r in n1 if r["id_referencia_interna"]==refid),
      "natureza_relacao":nat,"grau_maturidade":mat,"forca_causal":forca,"extrapolacao_por_analogia":ext,
      "evid_role":role,"uso":uso,"status_referencia":"CANDIDATO","status_auditoria":"",
      "verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"",
      "g1_metodo":"eutils_automatico","g3_verificado_por":""})

ids1={r["id_referencia_interna"] for r in n1}
prob=[]
for v in n2:
    t=re.sub(r"\s+"," ",v["trecho_ancora"]).strip()
    if t[-1] not in '.!?]': prob.append(("PONT",v["id_vinculo"],t[-20:]))
    if t not in cflat: prob.append(("LIT",v["id_vinculo"],t[:40]))
    if v["id_referencia_interna"] not in ids1: prob.append(("REF",v["id_vinculo"]))
    if v["g3_verificado_por"]!="": prob.append(("G3",v["id_vinculo"]))
for r in n1:
    if r["pmid_oficial"] not in abs_: prob.append(("PMID",r["pmid_oficial"]))
claims=sorted({v["claim_id"] for v in n2})
sem=[f"B1.MEC.BLOCO03.{i:03d}" for i in range(1,13) if f"B1.MEC.BLOCO03.{i:03d}" not in claims]
print("N1:",len(n1),"N2:",len(n2))
print("problemas:", prob if prob else "NENHUM")
print("claims sem vinculo direto:", sem)
(out/"mod9_BLOCO03_N1_01_pmids.json").write_text(json.dumps(n1,ensure_ascii=False,indent=1),encoding="utf-8")
(out/"mod9_BLOCO03_N2_vinculos.json").write_text(json.dumps(n2,ensure_ascii=False,indent=1),encoding="utf-8")
