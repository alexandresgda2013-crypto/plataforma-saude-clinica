#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
from pathlib import Path
BASE=Path(__file__).resolve().parent
abs_=json.loads((BASE/"corpus/abstracts_pubmed.json").read_text(encoding="utf-8"))
out=BASE/"ato2_pacote"

M={"TREM2_APOE_2017":"28930663","snRNA_TREM2_2020":"31932797","AstroSwitch_2024":"38086421",
"A1block_2018":"29892066","IL6astro_2025":"39888279","MAMs_P2X7_2024":"38890305","PrimingPrinc_2018":"29902514",
"Pericitos_2010":"20944627","SocialStress_BBB_2017":"29184215","BBB_AD_2017":"27425887",
"Vago_2018":"29467611","taVNS_2020":"32050990","PVM_2025":"40391473","Treg_2024":"38016492",
"Bifido_2017":"28483500","Insula_2026":"40770435","MenLinf_2021":"33911285","Glinf_2025":"40324376",
"Plexo_2024":"39089253"}

N1=[
("REF_TREM2_APOE_2017","Experimental (Immunity; camundongo+humano)","preclinical_mechanistic","eixo TREM2-APOE define assinatura de microglia disfuncional (DAM) em ALS/EM/AD e placas Ab humanas","sim (neurodegener -> TDM)"),
("REF_snRNA_TREM2_2020","Experimental (Nat Med; snRNAseq humano+camundongo)","preclinical_mechanistic","populacoes DAM dependentes e independentes de TREM2 na patologia AD; heterogeneidade microglial","sim"),
("REF_AstroSwitch_2024","Experimental (Nature; camundongo)","preclinical_mechanistic","chave molecular separa astrocitos reativos C3+ (neurotoxico) de C3- (neuroprotetor), subdivisiveis; revisa binario A1/A2","sim (camundongo; TDM [EXT])"),
("REF_A1block_2018","Experimental (Nat Med; camundongo+humano)","preclinical_mechanistic","bloqueio da conversao A1 (induzida por mediadores microgliais) e neuroprotetor; agonistas GLP1R inibem A1","sim (Parkinson -> TDM)"),
("REF_IL6astro_2025","Experimental (Adv Sci; camundongo)","preclinical_mechanistic","IL-6 derivada de microglia induz apoptose de astrocitos hipocampais em modelo de depressao; atrofia/perda astrocitaria","sim (camundongo)"),
("REF_MAMs_P2X7_2024","Experimental (Nat Commun; camundongo)","preclinical_mechanistic","ATP/estresse aumentam contatos reticulo-mitocondria (MAMs) na microglia mediando comportamento tipo-depressivo; refinamento do eixo P2X7/NLRP3","sim (camundongo)"),
("REF_Pericitos_2010","Experimental (Nature; camundongo)","preclinical_mechanistic","pericitos regulam a BHE; necessarios para tight junctions e baixa vesiculacao endotelial","sim (camundongo)"),
("REF_SocialStress_BBB_2017","Experimental (Nat Neurosci; camundongo derrota social)","preclinical_mechanistic","estresse social cronico reduz claudina-5 (Cldn5), altera morfologia vascular e aumenta permeabilidade/passagem de sinais imunes -> depressao","sim (camundongo)"),
("REF_BBB_AD_2017","Review (humano+animal)","preclinical_mechanistic","disfuncao da BHE na doenca de Alzheimer por componentes celulares","sim"),
("REF_Vago_2018","Review (Front Neurosci)","preclinical_mechanistic","nervo vago (80% aferente) detecta metabolitos da microbiota e sinais inflamatorios; via periferia->SNC independente de BHE","parcial"),
("REF_taVNS_2020","Experimental humano (J Neuroinflammation; TDM)","human_clinical","taVNS aumenta conectividade amigdala-CPFdl e tem efeito anti-inflamatorio na TDM","baixa (humano)"),
("REF_PVM_2025","Experimental (Stroke; camundongo)","preclinical_mechanistic","macrofagos perivasculares/de borda promovem clearance glinfatico de Ab pos-AVE; interface SNC-periferia","sim (AVE)"),
("REF_Treg_2024","Observacional humano (prenatal)","human_clinical","fenotipos de Treg perifericas modificados em sofrimento psicologico pre-natal; imunidade de fronteira","baixa (humano)"),
("REF_Bifido_2017","RCT humano (Gastroenterology; SII)","human_clinical","Bifidobacterium longum NCC3001 (RCT duplo-cego) reduz depressao e altera ativacao cerebral limbica em humanos com SII","baixa (humano; SII)"),
("REF_Insula_2026","Experimental (camundongo)","preclinical_mechanistic","cortex insular anterior regula comportamento tipo-depressivo/ASD diferencialmente via microglia","sim (camundongo)"),
("REF_MenLinf_2021","Experimental (Nature; camundongo+humano)","preclinical_mechanistic","linfaticos meningeos afetam resposta microglial e imunoterapia anti-Ab; drenagem do SNC","sim"),
("REF_Glinf_2025","Review (Immunity; humano+animal)","preclinical_mechanistic","glinfatica e linfaticos meningeos formam o 'codigo imune' do cerebro; mobilizam residuos para bordas imunes","parcial"),
("REF_Plexo_2024","Experimental (Cell; camundongo)","preclinical_mechanistic","plexo coroide (barreira/fonte de LCR) sinergiza com neutrofilos/monocitos durante neuroinflamacao meningitica","sim (camundongo)"),
]
n1=[]
for refid,desenho,role,achado,ext in N1:
    key=refid[4:]; pmid=M[key]; r=abs_[pmid]
    n1.append({"id_referencia_interna":refid,"pmid_oficial":pmid,"doi":r["doi"],"titulo_artigo":r["titulo"],
      "autores":r["autores"][:6],"revista_ano":f"{r['revista']} ({r['ano']})","desenho_estudo":desenho,
      "secao_origem":"mecanismo_B1_neuroinflamacao/BLOCO_04","achado_central_molecular":achado,
      "extrapolacao_por_analogia":ext,"status_auditoria":"","claim_id_origem":"","citacao_confirmada":True,
      "origem_pipeline":"BUSCA_FERRAMENTA","g1_metodo":"eutils_automatico","g3_verificado_por":"",
      "especie_mesh":r["especie_mesh"],"evid_role":role,"verification_status":"pendente"})

V=[
("REF_TREM2_APOE_2017","B1.MEC.BLOCO04.001","BLOCO_04/4.1","O estado DAM (microglia associada a doença) depende do eixo TREM2–APOE: uma assinatura transcricional APOE-dependente identifica micróglia disfuncional","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (neurodegener -> TDM)","preclinical_mechanistic","contexto_mecanistico"),
("REF_snRNA_TREM2_2020","B1.MEC.BLOCO04.001","BLOCO_04/4.1","O sequenciamento mononuclear em camundongo e humano confirma populações DAM dependentes e independentes de TREM2 associadas à patologia","contributiva","bem_suportado","tier_3_correlacional_mecanistico","sim","preclinical_mechanistic","contexto_mecanistico"),
("REF_AstroSwitch_2024","B1.MEC.BLOCO04.002","BLOCO_04/4.2","Um trabalho de 2024 identificou uma chave molecular que separa reatividade neuroprotetora de neurotóxica: astrócitos de substância branca lesada diferenciam-se em populações C3+ e C3−","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico"),
("REF_A1block_2018","B1.MEC.BLOCO04.002","BLOCO_04/4.2","O bloqueio da conversão ao fenótipo A1 neurotóxico (induzido por mediadores microgliais) é neuroprotetor em modelos de Parkinson, e agonistas GLP1R inibem essa conversão","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (Parkinson -> TDM)","preclinical_mechanistic","contexto_mecanistico"),
("REF_IL6astro_2025","B1.MEC.BLOCO04.002","BLOCO_04/4.2","Em depressão, IL-6 derivada de micróglia pode induzir apoptose de astrócitos hipocampais","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","gap_pesquisa"),
("REF_MAMs_P2X7_2024","B1.MEC.BLOCO04.003","BLOCO_04/4.3","um achado mais fino mostra que o ATP e o estresse aumentam contatos retículo-mitocôndria (MAMs) na micróglia, e essa plataforma media o comportamento tipo-depressivo","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico"),
("REF_Pericitos_2010","B1.MEC.BLOCO04.004","BLOCO_04/4.4","Os pericitos regulam a BHE: sua integridade é necessária para manter as junções e a baixa vesiculação endotelial","causal","muito_estabelecido","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico"),
("REF_SocialStress_BBB_2017","B1.MEC.BLOCO04.004","BLOCO_04/4.4","estresse social crônico (derrota social em camundongo) induz patologia neurovascular promotora de depressão — reduz a tight junction claudina-5 (Cldn5), altera morfologia vascular e aumenta permeabilidade","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico"),
("REF_Vago_2018","B1.MEC.BLOCO04.005","BLOCO_04/4.5","O nervo vago (80% fibras aferentes) detecta metabólitos da microbiota e sinais inflamatórios periféricos e os conduz ao SNC independentemente da BHE","contributiva","bem_suportado","","parcial","preclinical_mechanistic","contexto_mecanistico"),
("REF_taVNS_2020","B1.MEC.BLOCO04.005","BLOCO_04/4.5","Em humanos, a estimulação vagal auricular transcutânea (taVNS) aumenta conectividade amígdala–córtex pré-frontal dorsolateral e tem efeito anti-inflamatório na TDM","causal","moderadamente_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
("REF_PVM_2025","B1.MEC.BLOCO04.006","BLOCO_04/4.6","Macrófagos perivasculares promovem clearance glinfático de Aβ pós-AVE por mecanismo próprio","contributiva","emergente","","sim (AVE)","preclinical_mechanistic","gap_pesquisa"),
("REF_Treg_2024","B1.MEC.BLOCO04.006","BLOCO_04/4.6","Tregs periféricas têm fenótipos modificados em sofrimento psicológico pré-natal","associativa","emergente","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","contexto_mecanistico"),
("REF_taVNS_2020","B1.MEC.BLOCO04.009","BLOCO_04/4.7","A taVNS modula conectividade amígdala–CPFdl","causal","moderadamente_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
("REF_Bifido_2017","B1.MEC.BLOCO04.009","BLOCO_04/4.7","Probiótico (Bifidobacterium longum NCC3001, RCT) reduz escores de depressão e altera ativação cerebral em áreas límbicas em humanos com SII","causal","moderadamente_suportado","tier_2_necessidade_ou_suficiencia","baixa (humano RCT; SII)","human_experimental","clinico"),
("REF_Insula_2026","B1.MEC.BLOCO04.009","BLOCO_04/4.7","A ínsula/anterior é modulada por microglia em comportamento tipo-depressivo/ASD em camundongo","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","gap_pesquisa"),
("REF_MenLinf_2021","B1.MEC.BLOCO04.010","BLOCO_04/4.8","O SNC drena pela glinfática e por vasos linfáticos meníngeos, que afetam a resposta microglial e a imunoterapia","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim","preclinical_mechanistic","contexto_mecanistico"),
("REF_Glinf_2025","B1.MEC.BLOCO04.010","BLOCO_04/4.8","a revisão de 2025 consolida como o \"código imune\" do cérebro","contributiva","bem_suportado","","parcial","preclinical_mechanistic","contexto_mecanistico"),
("REF_Plexo_2024","B1.MEC.BLOCO04.010","BLOCO_04/4.8","O plexo coroide funciona como barreira e fonte de LCR e sinergiza com células imunes durante neuroinflamação","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico"),
]
corpo=(out/"CHECKPOINT_04_BLOCO04_corpo.md").read_text(encoding="utf-8").replace("**","")
cflat=re.sub(r"\s+"," ",corpo); frases=re.findall(r"[^.].*?\.\s",cflat+" ")
def acha(p):
    c=[f.strip() for f in frases if p[:36] in f]
    return c[0] if c else None
n2=[]
for i,(refid,claim,secao,probe,nat,mat,forca,ext,role,uso) in enumerate(V,1):
    t=acha(probe)
    n2.append({"id_vinculo":f"VINC_B1_{3000+i:04d}","id_referencia_interna":refid,"claim_id":claim,
      "mecanismo_origem":"B1","secao_origem":secao,"trecho_ancora":t or probe+".",
      "achado_central_molecular":next(r["achado_central_molecular"] for r in n1 if r["id_referencia_interna"]==refid),
      "natureza_relacao":nat,"grau_maturidade":mat,"forca_causal":forca,"extrapolacao_por_analogia":ext,
      "evid_role":role,"uso":uso,"status_referencia":"CANDIDATO","status_auditoria":"",
      "verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"",
      "g1_metodo":"eutils_automatico","g3_verificado_por":""})
ids1={r["id_referencia_interna"] for r in n1}; prob=[]
for v in n2:
    t=re.sub(r"\s+"," ",v["trecho_ancora"]).strip()
    if t[-1] not in '.!?]': prob.append(("PONT",v["id_vinculo"]))
    if t not in cflat: prob.append(("LIT",v["id_vinculo"],t[:35]))
    if v["id_referencia_interna"] not in ids1: prob.append(("REF",v["id_vinculo"]))
for r in n1:
    if r["pmid_oficial"] not in abs_: prob.append(("PMID",r["pmid_oficial"]))
claims=sorted({v["claim_id"] for v in n2})
sem=[f"B1.MEC.BLOCO04.{i:03d}" for i in range(1,11) if f"B1.MEC.BLOCO04.{i:03d}" not in claims]
print("N1:",len(n1),"N2:",len(n2),"| problemas:",prob if prob else "NENHUM")
print("claims sem vinculo:",sem)
(out/"mod9_BLOCO04_N1_01_pmids.json").write_text(json.dumps(n1,ensure_ascii=False,indent=1),encoding="utf-8")
(out/"mod9_BLOCO04_N2_vinculos.json").write_text(json.dumps(n2,ensure_ascii=False,indent=1),encoding="utf-8")
