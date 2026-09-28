#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
from pathlib import Path
BASE=Path(__file__).resolve().parent
abs_=json.loads((BASE/"corpus/abstracts_pubmed.json").read_text(encoding="utf-8"))
out=BASE/"ato2_pacote"

def build(n, refs, vincs, prefix):
    n1=[]
    for refid,pmid,desenho,role,achado,ext in refs:
        r=abs_[pmid]
        n1.append({"id_referencia_interna":refid,"pmid_oficial":pmid,"doi":r["doi"],"titulo_artigo":r["titulo"],
          "autores":r["autores"][:6],"revista_ano":f"{r['revista']} ({r['ano']})","desenho_estudo":desenho,
          "secao_origem":f"mecanismo_B1_neuroinflamacao/BLOCO_{n:02d}","achado_central_molecular":achado,
          "extrapolacao_por_analogia":ext,"status_auditoria":"","claim_id_origem":"","citacao_confirmada":True,
          "origem_pipeline":"BUSCA_FERRAMENTA","g1_metodo":"eutils_automatico","g3_verificado_por":"",
          "especie_mesh":r["especie_mesh"],"evid_role":role,"verification_status":"pendente"})
    corpo=(out/f"CHECKPOINT_{n:02d}_BLOCO{n:02d}_corpo.md").read_text(encoding="utf-8").replace("**","")
    cflat=re.sub(r"\s+"," ",corpo); frases=re.findall(r"[^.].*?\.\s",cflat+" ")
    def acha(p):
        c=[f.strip() for f in frases if p[:30] in f]
        return c[0] if c else None
    n2=[]
    for i,(refid,claim,secao,probe,nat,mat,forca,ext,role,uso) in enumerate(vincs,1):
        t=acha(probe); achado=next(x["achado_central_molecular"] for x in n1 if x["id_referencia_interna"]==refid)
        n2.append({"id_vinculo":f"VINC_B1_{prefix+i:04d}","id_referencia_interna":refid,"claim_id":claim,
          "mecanismo_origem":"B1","secao_origem":secao,"trecho_ancora":(t or probe+"."),
          "achado_central_molecular":achado,"natureza_relacao":nat,"grau_maturidade":mat,"forca_causal":forca,
          "extrapolacao_por_analogia":ext,"evid_role":role,"uso":uso,"status_referencia":"CANDIDATO",
          "status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado",
          "g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""})
    ids1={x["id_referencia_interna"] for x in n1}; prob=[]
    for v in n2:
        t=re.sub(r"\s+"," ",v["trecho_ancora"]).strip()
        if t[-1] not in '.!?]': prob.append(("PONT",v["id_vinculo"]))
        if t not in cflat: prob.append(("LIT",v["id_vinculo"],t[:30]))
        if v["id_referencia_interna"] not in ids1: prob.append(("REF",v["id_vinculo"]))
    for x in n1:
        if x["pmid_oficial"] not in abs_: prob.append(("PMID",x["pmid_oficial"]))
    print(f"BLOCO{n:02d}: N1 {len(n1)} N2 {len(n2)} | problemas:", prob if prob else "NENHUM")
    (out/f"mod9_BLOCO{n:02d}_N1_01_pmids.json").write_text(json.dumps(n1,ensure_ascii=False,indent=1),encoding="utf-8")
    (out/f"mod9_BLOCO{n:02d}_N2_vinculos.json").write_text(json.dumps(n2,ensure_ascii=False,indent=1),encoding="utf-8")

# ---- BLOCO 09 ----
refs09=[
("REF_IL1_stress_2009","19017533","Review (Front Neuroendocrinol; humano+animal)","preclinical_mechanistic","IL-1 cerebral e elo central da resposta de estresse; modula plasticidade/LTP e neuroendocrino","parcial"),
("REF_GliaMental_2020","38377429","Review (BBI Health)","preclinical_mechanistic","ativacao glial/citocinas interferem com plasticidade sinaptica e memoria em transtornos mentais","parcial"),
("REF_IL1b_BDNF_1993","8492907","Experimental (Neuroscience; rato)","preclinical_mechanistic","IL-1b sistemica reduz mRNA de BDNF hipocampal","sim (rato)"),
("REF_MicrogliaGlut_2022","34661306","Experimental (Glia; camundongo, PLX5622)","preclinical_mechanistic","deplecao de microglia altera transmissao CA3-CA1; microglia controla sinapses glutamatergicas no hipocampo adulto","sim (camundongo)"),
("REF_HIVdend_2019","31465771","Experimental/humano (Brain Res)","preclinical_mechanistic","dano sinaptodendritico cortical regulado por opioides/quimiocinas sem morte neuronal; reversivel por modulacao imune","sim (HIV)"),
("REF_TNFscaling_2006","16547515","Experimental (Nature; camundongo/rato)","preclinical_mechanistic","TNF-alpha glial medeia scaling sinaptico homeostatico (ajuste de AMPA), fisiologico","sim (camundongo/rato)"),
]
vincs09=[
("REF_IL1_stress_2009","B1.MEC.BLOCO09.001","BLOCO_09/9.1","IL-1 é regulador central da resposta de estresse e a produção cerebral de IL-1 liga o desafio imunológico/psicológico à ativação neuroendócrina e à plasticidade","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","parcial","preclinical_mechanistic","contexto_mecanistico"),
("REF_GliaMental_2020","B1.MEC.BLOCO09.001","BLOCO_09/9.1","A revisão de ativação glial em transtornos mentais consolida que citocinas interferem com plasticidade sináptica e memória","contributiva","moderadamente_suportado","","parcial","preclinical_mechanistic","contexto_mecanistico"),
("REF_IL1b_BDNF_1993","B1.MEC.BLOCO09.001","BLOCO_09/9.1","O mecanismo molecular é a supressão de BDNF/CREB (BLOCO03.001: IL-1β reduz mRNA de BDNF hipocampal, 1993)","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (rato)","preclinical_mechanistic","contexto_mecanistico"),
("REF_MicrogliaGlut_2022","B1.MEC.BLOCO09.002","BLOCO_09/9.2","Microglia controla sinapses glutamatérgicas no hipocampo adulto: a depleção farmacológica de microglia altera a transmissão CA3-CA1","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico"),
("REF_HIVdend_2019","B1.MEC.BLOCO09.002","BLOCO_09/9.2","Em HIV, dano sinaptodendrítico cortical é regulado por opioides e quimiocinas mesmo sem morte neuronal","associativa","emergente","tier_3_correlacional_mecanistico","sim (HIV)","preclinical_mechanistic","gap_pesquisa"),
("REF_TNFscaling_2006","B1.MEC.BLOCO09.003","BLOCO_09/9.3","Esse scaling é mediado por TNF-α glial: o TNF derivado da glia ajusta a força de receptores AMPA na membrana para estabilizar a atividade da rede","causal","muito_estabelecido","tier_2_necessidade_ou_suficiencia","sim (camundongo/rato; relevancia TDM [EXT])","preclinical_mechanistic","contexto_mecanistico"),
]
build(9,refs09,vincs09,9000)

# ---- BLOCO 10 ----
refs10=[
("REF_IFN_NSC_2014","25068123","Experimental/Review (celula NSC)","preclinical_mechanistic","maquinaria IFN-a/IL-6 em celulas-tronco neurais; ambiente inflamatorio altera destino de NSC","sim (celula)"),
("REF_IL1_stress_2009b","19017533","Review (Front Neuroendocrinol; humano+animal)","preclinical_mechanistic","IL-1 como regulador central da resposta de estresse; suprime neurogenese via NF-kB nas NSC","parcial"),
("REF_M2ves_2025","40270025","Experimental (J Nanobiotechnol; camundongo)","preclinical_mechanistic","vesiculas extracelulares de microglia M2 modulam destino de NSC pos-isquemia promovendo neurogenese","sim (camundongo)"),
("REF_TREM2_2025","41261263","Experimental (Mol Neurobiol; camundongo)","preclinical_mechanistic","TREM2 polariza microglia para M2 e melhora neurogenese (liberando BDNF)","sim (camundongo)"),
("REF_IL4_STAT6_2024","37933553","Experimental humano (Clin Exp Pharmacol Physiol)","human_clinical","eixo IL-4/STAT6 reverte defeito proliferativo em celulas-tronco neurais humanas","baixa (humano; SCA3)"),
]
vincs10=[
("REF_IFN_NSC_2014","B1.MEC.BLOCO10.001","BLOCO_10/10.1","a maquinaria de IFN-α/IL-6 em células-tronco neurais está documentada na depressão induzida por citocinas (Mechanisms for IFN-α-induced depression and neural stem cell dysfunction, 2014)","causal","moderadamente_suportado","tier_2_necessidade_ou_suficiencia","sim (celula)","preclinical_mechanistic","contexto_mecanistico"),
("REF_IL1_stress_2009b","B1.MEC.BLOCO10.002","BLOCO_10/10.2","IL-1β e TNF ativam NF-κB nas NSC e reduzem proliferação/sobrevivência de novos neurônios do giro denteado — elo causal distinto e complementar ao do IL-6.","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (animal; humano [EXT])","preclinical_mechanistic","contexto_mecanistico"),
("REF_M2ves_2025","B1.MEC.BLOCO10.003","BLOCO_10/10.3","Vesículas extracelulares derivadas de microglia M2 modulam o destino das NSC após isquemia, promovendo neurogênese","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","gap_pesquisa"),
("REF_TREM2_2025","B1.MEC.BLOCO10.003","BLOCO_10/10.3","TREM2 polariza microglia para M2 e melhora neurogênese","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","gap_pesquisa"),
("REF_IL4_STAT6_2024","B1.MEC.BLOCO10.003","BLOCO_10/10.3","o eixo IL-4/STAT6 reverte defeito proliferativo em células-tronco neurais humanas","causal","emergente","tier_2_necessidade_ou_suficiencia","baixa (humano; doenca neurodegenerativa)","human_clinical","gap_pesquisa"),
]
build(10,refs10,vincs10,10000)
