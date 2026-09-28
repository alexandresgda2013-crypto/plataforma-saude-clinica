#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
from pathlib import Path
BASE=Path(__file__).resolve().parent
abs_=json.loads((BASE/"corpus/abstracts_pubmed.json").read_text(encoding="utf-8"))
out=BASE/"ato2_pacote"

def sintese(n, refs, vincs, prefix, cab_claims):
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
    return cab_claims

# BLOCO 07 — nos centrais (refs ja validadas)
refs07=[
("REF_Gastrodin_2024","38552431","Experimental (camundongo; TLR4/TRAF6/NF-kB)","preclinical_mechanistic","sequencia receptor->IRAK/TRAF6->IKK->IkBa->NF-kB nuclear; inibicao reduz neuroinflamacao","sim (camundongo)"),
("REF_GR_repress_2018","29424686","Experimental (eLife; macrófago)","preclinical_mechanistic","GR reprime genes pro-inflamatorios gene-especificamente; resistencia a GR desinibe NF-kB","sim"),
("REF_CAPS_2024","38321014","Genetica humana (Nat Commun)","human_clinical","variantes gain-of-function NLRP3 -> inflamassoma constitutivo; GSDMD/IL-18 basais","baixa (doenca rara)"),
("REF_NEK7_2025","40602264","Experimental (Int Immunopharmacol; rato)","preclinical_mechanistic","NEK7 regula NLRP3; alvo modula piroptose e alivia comportamento depressivo","sim (rato)"),
("REF_Swanson_2019","31036962","Review (Nat Rev Immunol)","preclinical_mechanistic","dois sinais do NLRP3; NF-kB da priming; sinal 2 monta ASC/caspase-1","sim"),
("REF_cGAS_POCD_2024","38481801","Experimental (camundongo)","preclinical_mechanistic","eixo mtDNA-cGAS-STING ativa NLRP3 microglial; loop amplificador mitocondrial","sim"),
]
vincs07=[
("REF_Gastrodin_2024","B1.MEC.BLOCO07.001","BLOCO_07/7.1","via IRAK/TRAF6→IKK→degradação de IκBα→translocação nuclear — dirigindo a transcrição de IL1B, IL6, TNF, do próprio NLRP3 (priming), PTGS2/COX-2 e NOS2/iNOS","causal","muito_estabelecido","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico"),
("REF_GR_repress_2018","B1.MEC.BLOCO07.001","BLOCO_07/7.1","resistência a glicocorticoide desinibe NF-κB (BLOCO08.001, GR reprime genes inflamatórios gene-especificamente)","causal","bem_suportado","tier_2_necessidade_ou_suficiencia","sim","preclinical_mechanistic","contexto_mecanistico"),
("REF_CAPS_2024","B1.MEC.BLOCO07.001","BLOCO_07/7.2","Prova causal forte: variantes humanas ganho-de-função geram inflamassoma constitutivo (CAPS, PMID 38321014)","causal","bem_suportado","tier_1_necessidade_e_suficiencia","baixa (humano doenca rara)","human_clinical","contexto_mecanistico"),
("REF_NEK7_2025","B1.MEC.BLOCO07.001","BLOCO_07/7.2","NEK7 modula o complexo e alivia comportamento depressivo em rato (PMID 40602264)","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (rato)","preclinical_mechanistic","gap_pesquisa"),
("REF_Swanson_2019","B1.MEC.BLOCO07.001","BLOCO_07/7.3","Se NF-κB é o nó transcricional, o inflamassoma NLRP3 é o nó executor a jusante: recebe o priming de NF-κB e o \"sinal 2\"","causal","bem_suportado","","sim","preclinical_mechanistic","contexto_mecanistico"),
("REF_cGAS_POCD_2024","B1.MEC.BLOCO07.001","BLOCO_07/7.3","amplificado por loops (B6/ROS, B9/mitocôndria, B2/resistência a glicocorticoide)","causal","emergente","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico"),
]
sintese(7,refs07,vincs07,7000,"")

# BLOCO 11 — estratificacao
refs11=[
("REF_Osimo_2020","32113908","Meta-analise (BBI; humano)","human_clinical","elevacao de marcadores heterogenea e concentrada em subgrupo; variabilidade","baixa (humano)"),
("REF_RCT_infliximab","22945416","RCT (JAMA Psychiatry; N=60)","human_clinical","infliximabe nao supera placebo na amostra toda; so beneficia subgrupo com marcador basal alto (PCR/TNF/sTNFR2)","baixa (humano RCT)"),
("REF_Setiawan_2015","25629589","EC humano (TSPO-PET)","human_clinical","TSPO elevado em regioes cortico-limbicas na TDM","baixa (humano)"),
("REF_Steiner_2011_QUIN","21831269","Pos-morte humano","post_mortem","acido quinolínico microglial elevado em cingulado em depressao grave (amostra suicidio)","baixa (pos-morte)"),
("REF_Reward_2022","35927580","EC humano (fMRI)","human_clinical","inflamacao baixa conectividade cortico-estriatal de recompensa -> anedonia","baixa (humano)"),
("REF_Bull_2009","18458677","Genetica humana (Mol Psychiatry)","human_clinical","IL-6 rs1800795 e 5-HTTLPR modificam depressao por IFN-a; genotipo x inflamacao","baixa (humano)"),
("REF_Treg_2024","38016492","Observacional humano (prenatal)","human_clinical","fenotipos de Treg perifericas modificados em sofrimento psicologico pre-natal (subtipo perinatal)","baixa (humano)"),
]
vincs11=[
("REF_Osimo_2020","B1.MEC.BLOCO11.001","BLOCO_11/11.1","a meta de Osimo 2020 confirma que a elevação é de um SUBGRUPO e não universal — ver BLOCO05","associativa","muito_estabelecido","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
("REF_RCT_infliximab","B1.MEC.BLOCO11.001","BLOCO_11/11.1","(d) modificabilidade por intervenção anti-TNF exclusivamente quando o marcador basal está alto (RCT infliximabe: negativo na amostra toda, positivo no subgrupo inflamado","causal","bem_suportado","tier_1_necessidade_e_suficiencia","baixa (humano RCT)","human_clinical","clinico"),
("REF_Setiawan_2015","B1.MEC.BLOCO11.001","BLOCO_11/11.1","(b) sinal central (TSPO-PET elevado em córtex cingulado/ínsula","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
("REF_Steiner_2011_QUIN","B1.MEC.BLOCO11.001","BLOCO_11/11.1","QUIN pós-morte em subregião cingulada — BLOCO05.002/006","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (pos-morte suicidio)","post_mortem","contexto_mecanistico"),
("REF_Reward_2022","B1.MEC.BLOCO11.001","BLOCO_11/11.1","(c) assinatura neural de anedonia (baixa conectividade córtico-estriatal ventral; BLOCO06.004)","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico"),
("REF_Bull_2009","B1.MEC.BLOCO11.001","BLOCO_11/11.1","genética (Bull IL-6, FKBP5)","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","contexto_mecanistico"),
("REF_Treg_2024","B1.MEC.BLOCO11.001","BLOCO_11/11.2","Depressão perinatal: disfunção do ajuste imunológico gestacional; Treg/Th17 (BLOCO04.006, PMID 38016492)","associativa","emergente","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","gap_pesquisa"),
]
sintese(11,refs11,vincs11,11000,"")
