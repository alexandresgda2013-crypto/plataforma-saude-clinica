#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adiciona os PMIDs novos da B1 v2 (imunometabolismo/necroptose/Cx43/AQP4 + ansiedade)
ao Módulo 9, com rótulos casados com as listras da biblioteca."""
import json
from pathlib import Path
F=Path("/home/user/pipeline_auditoria_conteudo/BIBLIOTECAS/B01_Neuroinflamacao/Evidencias/Bibliografia/01_pmids.json")
d=json.load(open(F,encoding="utf-8"))
exist={r.get("pmid_oficial") for r in d}

# (pmid, rotulo, titulo, 1oautor, revista_ano, desenho, especie_mesh, role, verif)
rows=[
 ("34107997","Glicolise_microglia_2021","Early glycolytic reprogramming controls microglial inflammatory activation.","Cheng J","Journal of neuroinflammation (2021)","ML celula/camundongo (glicolise microglia)",["Animals","Cells"],"preclinical_mechanistic","preclinico"),
 ("23535595","Succinato_HIF_2013","Succinate is an inflammatory signal that induces IL-1beta through HIF-1alpha.","Tannahill GM","Nature (2013)","ML macrofago (succinato/HIF-1alfa/IL-1beta)",["Cells","Animals"],"preclinical_mechanistic","preclinico"),
 ("37717531","Itaconato_Nrf2_2023","Itaconate: A promising precursor for treatment of neuroinflammation associated depression.","Liu R","Biomedicine & pharmacotherapy (2023)","OB revisao (itaconato/IRG1/NLRP3/Nrf2)",["Humans","Animals"],"human_clinical","extrapolado"),
 ("40913317","IRG1_itaconato_2025","Metabolic profiling reveals a glycolytic shift and an IRG1/Itaconate/NFE2L2 axis regulated by LPS.","Engskog-Vlachos P","Journal of neurochemistry (2025)","ML celula (metabolomica, IRG1/itaconato/Nrf2)",["Cells"],"preclinical_mechanistic","preclinico"),
 ("36221097","Glicolise_hipocampo_2022","Early effects of LPS-induced neuroinflammation on the rat hippocampal glycolytic pathway.","Vizuete AFK","Journal of neuroinflammation (2022)","ML rato (glicolise hipocampo)",["Animals","Rats"],"preclinical_mechanistic","preclinico"),
 ("36686688","Necroptose_dep_2022","Necroptotic kinases are involved in the reduction of depression-induced astrocytes.","Zeb S","Frontiers in pharmacology (2022)","ML camundongo (RIPK1/RIPK3/MLKL, estresse cronico)",["Animals"],"preclinical_mechanistic","preclinico"),
 ("25643695","Cx43_hemicanal_2015","Activated microglia impairs neuroglial interaction by opening Cx43 hemichannels in hippocampal astrocytes.","Abudara V","Glia (2015)","ML camundongo/celula (Cx43 hemicanais)",["Animals","Cells"],"preclinical_mechanistic","preclinico"),
 ("21228152","Cx43_GJ_2011","Neuroinflammation leads to region-dependent alterations in astrocyte gap junction communication.","Karpuk N","Journal of neuroscience (2011)","ML camundongo (gap junctions astrocitarias)",["Animals"],"preclinical_mechanistic","preclinico"),
 ("37875763","Cx43_antidep_2023","Astroglial connexin 43-mediated gap junctions and hemichannels: potential antidepressant targets.","Lei L","Cellular and molecular neurobiology (2023)","OB revisao (Cx43; alvo antidepressivo)",["Humans","Animals"],"human_clinical","extrapolado"),
 ("37840071","AQP4_glinfatica_2024","Ketamine improves the glymphatic pathway by reducing pyroptosis of hippocampal astrocytes.","Wen G","Molecular neurobiology (2024)","ML camundongo (glinfatica/AQP4; cetamina)",["Animals"],"preclinical_mechanistic","preclinico"),
 ("41205656","Glinfatica_RM_2025","Dynamic contrast-enhanced MRI reveals glymphatic dysfunction in mice with depressive-like behavior.","Lyu C","Neurobiology of disease (2025)","ML camundongo (RM, glinfatica)",["Animals"],"preclinical_mechanistic","preclinico"),
 ("40199321","Amigdala_citocinas_2025","Inflammatory and anti-inflammatory cytokines bidirectionally modulate amygdala circuits.","Lee B","Cell (2025)","OB/ML revisao+experimento (citocinas e circuitos da amigdala)",["Animals"],"preclinical_mechanistic","extrapolado"),
 ("27590137","IL18_amigdala_2017","Local interleukin-18 system in the basolateral amygdala regulates susceptibility to chronic stress.","Kim TK","Molecular neurobiology (2017)","ML camundongo (IL-18 na BLA)",["Animals"],"preclinical_mechanistic","preclinico"),
 ("38395698","P2X7_NaK_ansiedade_2024","Disruption of the Na(+)/K(+)-ATPase-purinergic P2X7 receptor complex in microglia promotes anxiety.","Huang S","Immunity (2024)","ML camundongo (Na/K-ATPase/P2X7 microglial)",["Animals"],"preclinical_mechanistic","preclinico"),
 ("38012545","TET2_NLRP3_2023","TET2 deficiency promotes anxiety and depression-like behaviors by activating NLRP3/IL-1beta.","Gao Z","Molecular medicine (2023)","ML camundongo (TET2/NLRP3)",["Animals"],"preclinical_mechanistic","preclinico"),
 ("33358726","NLRP3_def_ansiedade_2021","NLRP3 deficiency-induced hippocampal dysfunction and anxiety-like behavior in mice.","Komleva YK","Brain research (2021)","ML camundongo (deficiencia de NLRP3; direcao nao monotonica)",["Animals"],"preclinical_mechanistic","preclinico"),
 ("30199144","Renna_ansiedade_2018","The association between anxiety, traumatic stress, and obsessive-compulsive disorders and inflammatory markers.","Renna ME","Depression and anxiety (2018)","MA/revisao sistematica (inflamacao em ansiedade/TEPT/TOC)",["Humans"],"human_clinical","verificado"),
 ("31326932","Costello_ansiedade_2019","Systematic review and meta-analysis of the association between peripheral inflammatory cytokines and anxiety disorders.","Costello H","BMJ open (2019)","MA (citocinas perifericas em ansiedade)",["Humans"],"human_clinical","verificado"),
 ("32398677","PTSD_supressao_2020","PTSD is associated with neuroimmune suppression: evidence from PET imaging and postmortem.","Bhatt S","Nature communications (2020)","EC humano (PET TSPO + pos-morte; supressao neuroimune)",["Humans"],"human_clinical","verificado"),
 ("30382535","TOC_imune_2019","Immune aberrations in obsessive-compulsive disorder: a systematic review and meta-analysis.","Cosco TD","Molecular neurobiology (2019)","MA (marcadores imunes no TOC)",["Humans"],"human_clinical","verificado"),
 ("29241050","Panico_citocinas_2018","Cytokine alterations in panic disorder: A systematic review.","Quagliato LA","Journal of affective disorders (2018)","OB revisao sistematica (citocinas no panico)",["Humans"],"human_clinical","verificado"),
 ("26544749","PTSD_marc_2015","Inflammatory markers in post-traumatic stress disorder: systematic review, meta-analysis.","Passos IC","Lancet psychiatry (2015)","MA (marcadores inflamatorios no TEPT)",["Humans"],"human_clinical","verificado"),
 ("35444254","TSPO_estresse_2022","Translocator protein (18kDa) TSPO: a new diagnostic or therapeutic target for stress-related disorders.","Rupprecht R","Molecular psychiatry (2022)","OB revisao (TSPO/estresse)",["Humans","Animals"],"human_clinical","verificado"),
 ("33200498","Ansiedade_ped_2021","Review: Inflammation and anxiety-based disorders in children and adolescents - a systematic review.","Parsons C","Child and adolescent mental health (2021)","OB revisao sistematica (ansiedade infantil/ADO)",["Humans"],"human_clinical","verificado"),
 ("35880170","Internalizante_ped_2022","Cytokine alterations in pediatric internalizing disorders: systematic review and exploratory meta-analysis.","Howe AS","Brain behavior & immunity - health (2022)","MA (citocinas em internalizantes pediatricos)",["Humans"],"human_clinical","verificado"),
 ("28901278","Quinur_ansiedade_2018","Neuroinflammation and the immune-kynurenine pathway in anxiety disorders.","Kim YK","Current neuropharmacology (2018)","OB revisao (quinurenina-imune na ansiedade)",["Humans","Animals"],"human_clinical","verificado"),
 ("38233395","Minociclina_medo_2024","Attenuating human fear memory retention with minocycline: a randomized placebo-controlled trial.","Xia Y","Translational psychiatry (2024)","EC humano RCT (minociclina/memoria de medo)",["Humans"],"human_experimental","verificado"),
 ("27357391","Minociclina_extincao_2016","Minocycline attenuates interferon-alpha-induced impairments in rat fear extinction.","Bi Q","Journal of neuroinflammation (2016)","ML rato (minociclina/extincao do medo/IFN)",["Animals","Rats"],"preclinical_mechanistic","preclinico"),
 ("31427751","Mega_imunomod_2020","Effects of immunomodulatory drugs on depressive symptoms: a mega-analysis of randomized placebo-controlled trials.","Wittenberg GM","Molecular psychiatry (2020)","MA mega-analise de RCT (farmacos imunomoduladores)",["Humans"],"human_experimental","verificado"),
 ("30646157","Omega3_ansiedade_2018","Association of use of omega-3 polyunsaturated fatty acids with changes in severity of anxiety symptoms.","Su KP","JAMA network open (2018)","MA (omega-3 e sintomas de ansiedade)",["Humans"],"human_experimental","verificado"),
]
add=0
for pmid,rot,tit,aut,rev,des,sp,role,ver in rows:
    if pmid in exist: continue
    d.append({
      "pmid_oficial":pmid,"doi":"","titulo_artigo":tit,"autores":[aut],"revista_ano":rev,
      "desenho_estudo":des,"secao_origem":"mecanismo_B1_neuroinflamacao/v2",
      "achado_central_molecular":tit[:120],"extrapolacao_por_analogia":("sim (animal/celula -> humano)" if role=="preclinical_mechanistic" else "baixa (humano)"),
      "status_auditoria":"VALIDADO_G3_IA (B1 v2, 2026-09-04)","claim_id_origem":"",
      "citacao_confirmada":True,"origem_pipeline":"BUSCA_FERRAMENTA","g1_metodo":"eutils_automatico",
      "g3_verificado_por":"IA_revisora (v2)","especie_mesh":sp,"evid_role":role,
      "verification_status":ver,"ids_referencia_interna":["REF_"+rot]})
    add+=1
json.dump(d,open(F,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("adicionados:",add,"| total:",len(d))
