#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
from pathlib import Path
BASE=Path(__file__).resolve().parent
abs_=json.loads((BASE/"corpus/abstracts_pubmed.json").read_text(encoding="utf-8"))
out=BASE/"ato2_pacote"

# ---- 02_meta_analises (schema 09.2: forca_evidencia_afirmacao, bloco_origem) ----
META=[
("REF_Dowlati_2010","20015486","alto","TNF-a e IL-6 significativamente elevados na TDM vs controles (meta seminal de citocinas)"),
("REF_Howren_2009","19188531","alto","depressao associada a PCR, IL-1 e IL-6 elevados (amostras comunitaria+clinica)"),
("REF_Goldsmith_2016","26903267","medio","rede de citocinas no sangue: padroes distintos entre esquizofrenia/bipolar/TDM e estado agudo/cronico"),
("REF_Osimo_2020","32113908","alto","meta de diferencas de media E de variabilidade: alteracoes heterogeneas, concentradas em subgrupo de pacientes"),
("REF_Quimio82_2017","28122130","alto","82 estudos: IL-6, TNF, IL-10, CCL2 e quimiocinas alterados na TDM (3212 TDM/2798 HC)"),
("REF_SexDiff_2024","39089535","medio","diferencas sexuais na ligacao inflamacao-depressao; efeito mais consistente em mulheres em alguns marcadores"),
]
n2meta=[]
for refid,pmid,forca,achado in META:
    r=abs_[pmid]
    n2meta.append({"id_referencia_interna":refid,"pmid_oficial":pmid,"doi":r["doi"],"titulo_artigo":r["titulo"],
      "autores":r["autores"][:6],"revista_ano":f"{r['revista']} ({r['ano']})","desenho_estudo":"Meta-analise (humano)",
      "forca_evidencia_afirmacao":forca,"bloco_origem":"mecanismo_B1_neuroinflamacao/BLOCO_05",
      "achado_central_molecular":achado,"extrapolacao_por_analogia":"baixa (humano direto)","status_auditoria":"",
      "claim_id_origem":"B1.MEC.BLOCO05.004","citacao_confirmada":True,"origem_pipeline":"BUSCA_FERRAMENTA",
      "g1_metodo":"eutils_automatico","g3_verificado_por":"","especie_mesh":r["especie_mesh"],
      "evid_role":"human_clinical","verification_status":"pendente"})

# ---- 01_pmids: estudos individuais (PET, LCR, soro, coorte) ----
PM=[
("REF_Setiawan_2015","25629589","EC humano (TSPO-PET, JAMA Psychiatry)","human_clinical","TSPO elevado em regioes cortico-limbicas na TDM; primeira demonstracao de neuroinflamacao central in vivo","baixa (humano; ressalva rs6971)"),
("REF_Holmes_2018","28939116","EC humano (TSPO-PET, Biol Psychiatry)","human_clinical","TSPO elevado no cingulado anterior na TDM e associado a ideacao suicida","baixa (humano)"),
("REF_Sublette_2011","21605657","EC humano (plasma)","human_clinical","quinurenina plasmatica elevada em tentadores de suicidio com TDM","baixa (humano)"),
("REF_Steiner_2011_QUIN","21831269","Pos-morte/tecidos humanos (J Neuroinflammation)","post_mortem","depressao grave associada a acido quinolínico microglial elevado em subregioes do cingulado anterior (amostra de suicidio)","baixa (humano pos-morte; qualificador suicidio)"),
("REF_S100B_dep_2019","30745657","Observacional humano (soro)","human_clinical","S100B serico elevado em depressao; marcador de BHE/dano glial, baixa especificidade","baixa (humano)"),
("REF_S100B_burnout_2016","27018399","EC humano (soro; burnout/depressao)","human_clinical","S100B serico como marcador substituto em burnout e depressao","baixa (humano)"),
("REF_YKL40_2024","39666148","Longitudinal humano (LCR; Parkinson)","human_clinical","marcadores gliais no LCR (sTREM2, YKL-40) associam-se longitudinalmente a depressao e disponibilidade de DAT","sim (Parkinson -> TDM)"),
("REF_KYNTRP_WM_2022","34847455","EC humano (soro + imagem)","human_clinical","citocinas e razao KYN/TRP associam-se seletivamente a alteracoes de substancia branca em bipolar/TDM","baixa (humano)"),
("REF_IL6resol_2015","25697833","Coorte humano (Psychol Med)","human_clinical","IL-6 baixa prediz melhor resolucao de sintomas em sofrimento psicologico","baixa (humano)"),
("REF_HippVol_ECT_2020","32114575","EC humano (ECT; neuroimagem)","human_clinical","marcadores inflamatorios (IL-6/TNF) relacionam-se a volume hipocampal e resposta a ECT","baixa (humano)"),
("REF_BrainIDO_2017","28631232","Experimental (camundongo)","preclinical_mechanistic","ativacao cerebral de IDO contribui para comportamento tipo-depressivo","sim (camundongo)"),
("REF_Obesidade_2025","41373743","Review (humano+animal)","human_clinical","obesidade como confundidor/mediador central da relacao inflamacao-depressao","baixa (revisao)"),
("REF_Mediadores_2024","38851764","Review (humano; TDM/bipolar)","human_clinical","revisao consolidada de mediadores inflamatorios em TDM e transtorno bipolar","baixa (revisao)"),
]
n1=[]
for refid,pmid,desenho,role,achado,ext in PM:
    r=abs_[pmid]
    n1.append({"id_referencia_interna":refid,"pmid_oficial":pmid,"doi":r["doi"],"titulo_artigo":r["titulo"],
      "autores":r["autores"][:6],"revista_ano":f"{r['revista']} ({r['ano']})","desenho_estudo":desenho,
      "secao_origem":"mecanismo_B1_neuroinflamacao/BLOCO_05","achado_central_molecular":achado,
      "extrapolacao_por_analogia":ext,"status_auditoria":"","claim_id_origem":"","citacao_confirmada":True,
      "origem_pipeline":"BUSCA_FERRAMENTA","g1_metodo":"eutils_automatico","g3_verificado_por":"",
      "especie_mesh":r["especie_mesh"],"evid_role":role,"verification_status":"pendente"})

# ---- vinculos N2 ----
V=[
("REF_Dowlati_2010","B1.MEC.BLOCO05.004","BLOCO_05/5.1","A meta-análise seminal de citocinas na depressão maior demonstrou concentrações significativamente elevadas de TNF-α e IL-6 em deprimidos versus controles","associativa","muito_estabelecido","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico","meta"),
("REF_Howren_2009","B1.MEC.BLOCO05.004","BLOCO_05/5.1","A meta-análise de PCR, IL-1 e IL-6 confirmou associação positiva entre depressão e PCR/IL-6 em amostras comunitárias e clínicas","associativa","muito_estabelecido","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico","meta"),
("REF_Goldsmith_2016","B1.MEC.BLOCO05.004","BLOCO_05/5.1","A meta-análise da rede de citocinas no sangue comparou esquizofrenia, bipolar e TDM e mostrou padrões distintos de alteração conforme estado clínico","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico","meta"),
("REF_Osimo_2020","B1.MEC.BLOCO05.004","BLOCO_05/5.1","A meta-análise mais recente quantificou tanto diferenças de média quanto variabilidade, testando se só um subgrupo de pacientes tem elevação — Osimo et al. (2020/2021)[MA; humano] consolidam que as alterações são heterogêneas e concentram-se num subgrupo.","associativa","muito_estabelecido","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico","meta"),
("REF_Quimio82_2017","B1.MEC.BLOCO05.004","BLOCO_05/5.1","A meta-análise de 82 estudos confirmou IL-6, TNF-α, CCL2 e outras citocinas elevadas na TDM","associativa","muito_estabelecido","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico","meta"),
("REF_SexDiff_2024","B1.MEC.BLOCO05.004","BLOCO_05/5.1","Diferenças sexuais na ligação inflamação-depressão são meta-analisadas, com efeito mais consistente em mulheres em alguns marcadores","associativa","moderadamente_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico","meta"),
("REF_IL6resol_2015","B1.MEC.BLOCO05.004","BLOCO_05/5.1","IL-6 também prediz pior resolução de sintomas em sofrimento psicológico","associativa","moderadamente_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico","pm"),
("REF_KYNTRP_WM_2022","B1.MEC.BLOCO05.001","BLOCO_05/5.2","Em pacientes bipolares e deprimidos, níveis de citocinas e a razão KYN/TRP associam-se seletivamente a alterações de substância branca","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico","pm"),
("REF_Sublette_2011","B1.MEC.BLOCO05.001","BLOCO_05/5.2","Em tentadores de suicídio com TDM, quinurenina plasmática está elevada","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano; suicidio)","human_clinical","clinico","pm"),
("REF_BrainIDO_2017","B1.MEC.BLOCO05.001","BLOCO_05/5.2","A ativação cerebral de IDO contribui para comportamento tipo-depressivo em modelo animal","causal","moderadamente_suportado","tier_2_necessidade_ou_suficiencia","sim (camundongo)","preclinical_mechanistic","contexto_mecanistico","pm"),
("REF_Setiawan_2015","B1.MEC.BLOCO05.002","BLOCO_05/5.4","Em TDM, a densidade de TSPO está elevada em regiões cortico-límbicas (Setiawan et al., 2015)[EC; humano, PET] — primeira demonstração de neuroinflamação central em pacientes vivos.","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano; rs6971)","human_clinical","clinico","pm"),
("REF_Holmes_2018","B1.MEC.BLOCO05.002","BLOCO_05/5.4","O TSPO no córtex cingulado anterior está elevado na depressão maior e relacionado a ideação suicida","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico","pm"),
("REF_S100B_dep_2019","B1.MEC.BLOCO05.005","BLOCO_05/5.5","S100B sérico: níveis séricos elevados são relatados em depressão","associativa","moderadamente_suportado","tier_3_correlacional_mecanistico","baixa (humano; baixa especificidade)","human_clinical","clinico","pm"),
("REF_S100B_burnout_2016","B1.MEC.BLOCO05.005","BLOCO_05/5.5","propostos como marcador substituto em burnout/depressão","associativa","emergente","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","gap_pesquisa","pm"),
("REF_Steiner_2011_QUIN","B1.MEC.BLOCO05.006","BLOCO_05/5.6","depressão grave associa-se a QUIN elevado em subregiões do córtex cingulado anterior (Steiner et al., 2011)[EC; pós-morte/tecidos humanos] — popular de suicídio com alta inflamação","associativa","bem_suportado","tier_3_correlacional_mecanistico","baixa (humano pos-morte; suicidio)","post_mortem","clinico","pm"),
("REF_YKL40_2024","B1.MEC.BLOCO05.006","BLOCO_05/5.6","Marcadores gliais no LCR (sTREM2, YKL-40) têm associação longitudinal com depressão e disponibilidade de transportador de dopamina em Parkinson","associativa","emergente","tier_3_correlacional_mecanistico","sim (Parkinson)","human_clinical","gap_pesquisa","pm"),
("REF_HippVol_ECT_2020","B1.MEC.BLOCO05.007","BLOCO_05/5.7","após ECT, marcadores inflamatórios (IL-6/TNF) relacionam-se a volume hipocampal e resposta","associativa","moderadamente_suportado","tier_3_correlacional_mecanistico","baixa (humano)","human_clinical","clinico","pm"),
("REF_Obesidade_2025","B1.MEC.BLOCO05.003","BLOCO_05/5.3","A obesidade é um confundidor/mediador central da relação inflamação-depressão","contributiva","bem_suportado","","baixa (revisao)","human_clinical","contexto_mecanistico","pm"),
]
corpo=(out/"CHECKPOINT_05_BLOCO05_corpo.md").read_text(encoding="utf-8").replace("**","")
cflat=re.sub(r"\s+"," ",corpo); frases=re.findall(r"[^.].*?\.\s",cflat+" ")
def acha(p):
    c=[f.strip() for f in frases if p[:34] in f]
    return c[0] if c else None
allrefs={r["id_referencia_interna"] for r in n1}|{r["id_referencia_interna"] for r in n2meta}
n2=[]
for i,(refid,claim,secao,probe,nat,mat,forca,ext,role,uso,tipo) in enumerate(V,1):
    t=acha(probe)
    achado=next((r["achado_central_molecular"] for r in (n1+n2meta) if r["id_referencia_interna"]==refid),"")
    n2.append({"id_vinculo":f"VINC_B1_{5000+i:04d}","id_referencia_interna":refid,"claim_id":claim,
      "mecanismo_origem":"B1","secao_origem":secao,"trecho_ancora":(t or probe+"."),
      "achado_central_molecular":achado,"natureza_relacao":nat,"grau_maturidade":mat,"forca_causal":forca,
      "extrapolacao_por_analogia":ext,"evid_role":role,"uso":uso,"status_referencia":"CANDIDATO",
      "status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado",
      "g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""})
prob=[]
for v in n2:
    t=re.sub(r"\s+"," ",v["trecho_ancora"]).strip()
    if t[-1] not in '.!?]': prob.append(("PONT",v["id_vinculo"]))
    if t not in cflat: prob.append(("LIT",v["id_vinculo"],t[:30]))
    if v["id_referencia_interna"] not in allrefs: prob.append(("REF",v["id_vinculo"]))
for coll in (n1,n2meta):
    for r in coll:
        if r["pmid_oficial"] not in abs_: prob.append(("PMID",r["pmid_oficial"]))
print("01_pmids:",len(n1),"| 02_meta:",len(n2meta),"| N2 vinculos:",len(n2))
print("problemas:",prob if prob else "NENHUM")
(out/"mod9_BLOCO05_N1_01_pmids.json").write_text(json.dumps(n1,ensure_ascii=False,indent=1),encoding="utf-8")
(out/"mod9_BLOCO05_02_meta_analises.json").write_text(json.dumps(n2meta,ensure_ascii=False,indent=1),encoding="utf-8")
(out/"mod9_BLOCO05_N2_vinculos.json").write_text(json.dumps(n2,ensure_ascii=False,indent=1),encoding="utf-8")
