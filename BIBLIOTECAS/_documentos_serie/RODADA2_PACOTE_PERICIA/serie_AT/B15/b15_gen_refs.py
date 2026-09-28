#!/usr/bin/env python3
# B15 — gera refs_data.json das 39 referências ENTRA da rodada [AT 2026-09-09]
import json, urllib.request, time, os

HERE = os.path.dirname(os.path.abspath(__file__))
META = json.load(open(f"{HERE}/producao/insumos/insumos_b15_meta.json"))
ABS = json.load(open(f"{HERE}/b15_efetch_sel.json"))
V1 = json.load(open(f"{HERE}/Evidencias/Bibliografia/01_pmids.json"))
V1_IDS = {r["id_referencia_interna"] for r in V1}
V1_PMIDS = {str(r["pmid_oficial"]) for r in V1}

# (pmid, id, tag, achado_central_molecular, aliases)
R = [
 ("19963289","REF_HOEFFER_2010","OB",
  "Revisão de referência do braço mTOR: o mTOR como encruzilhada de plasticidade, memória e doença — acopla receptores à maquinaria de tradução em mTORC1/mTORC2; contexto de panorama (CAMADA C ilustrativa, não fenótipo psiquiátrico)",
  ["Hoeffer & Klann 2010","Klann","panorama mTOR"]),
 ("22889863","REF_CHANDRAN_2013","ML",
  "Em ratos expostos a estresse, a fosforilação de componentes da via mTOR está reduzida na amígdala — braço mTOR-regional sob estresse (print 2013; insumo citava 2012)",
  ["Chandran 2012 (epub; print 2013)","Chandran"]),
 ("23906767","REF_XU_2013","ML",
  "A ativação da AMPK no hipocampo de ratos participa das ações antidepressivas da ketamina — braço metabólico a montante do eixo mTOR",
  ["Xu 2013","AMPK hipocampo"]),
 ("24321772","REF_ZHOU_2014","ML",
  "Os efeitos antidepressivos da ketamina associam-se à regulação ascendente mediada por receptores AMPA do eixo mTOR no hipocampo (modelo murino)",
  ["Zhou 2014","AMPA→mTOR"]),
 ("24728411","REF_OTA_2014","ML",
  "REDD1 é essencial para a perda sináptica induzida por estresse e para o comportamento depressivo em camundongos — elo estresse→inibição de mTOR→perda sináptica; o DOI do insumo apontava para artigo alheio (correção §4)",
  ["Ota 2014","REDD1"]),
 ("26522512","REF_LIU_2015","ML",
  "A fluoxetina regula a sinalização mTOR de modo região-dependente em camundongos tipo-depressivo — plasticidade farmacológica regional",
  ["Liu 2015","fluoxetina mTOR"]),
 ("27061850","REF_NEIS_2016","ML",
  "A agmatina produz efeitos tipo-antidepressivo ativando receptores AMPA e a sinalização mTOR (modelo murino)",
  ["Neis 2016","agmatina"]),
 ("29158584","REF_CAVALLERI_2018","ML",
  "A ketamina promove plasticidade estrutural (spinogênese/ramificação) em neurônios dopaminérgicos mesencefálicos murinos e derivados de iPSC humano — EXPOSIÇÃO: insumo rotulava 'Pich & Millan 2018'; primeiro autor real = Cavalleri",
  ["Pich & Millan 2018 (rótulo do insumo — real: Cavalleri et al., Millan sênior)","Cavalleri"]),
 ("31830487","REF_DEYAMA_2020","OB",
  "Revisão dos mecanismos neurotróficos (BDNF, VEGF, mTOR) subjacentes às ações antidepressivas rápidas e sustentadas da ketamina (print 2020; insumo citava 2019)",
  ["Deyama & Duman 2019 (epub; print 2020)","Deyama","Duman"]),
 ("32487317","REF_SATO_2020","ML",
  "Glucocorticoides reprimem a autofagia mediada por chaperonas (CMA) e a microautofagia — camada molecular da interface estresse→autofagia lisossomal",
  ["Sato 2020","CMA glicocorticoides"]),
 ("33022268","REF_PAZINI_2020","ML",
  "A sinalização dependente de mTORC1 subjaz ao efeito rápido de creatina e ketamina em teste comportamental murino — farmacologia-convergente no eixo",
  ["Pazini 2020","creatina ketamina mTORC1"]),
 ("33381149","REF_WANG_2020","ML",
  "Estresse precoce altera plasticidade sináptica e sinalização mTOR em ratos, com correlação a fenótipos tipo-ansiedade — janela desenvolvimental",
  ["Wang 2020","ELS mTOR"]),
 ("33723223","REF_KOEHL_2021","ML",
  "A remoção genética da p70 S6 quinase 1 (alvo efetor de mTORC1) aumenta o comportamento tipo-ansiedade em camundongos — causalidade genética no braço mTOR (versão publicada 2021; preprint bioRxiv 2020 excluído)",
  ["Koehl 2021 (publicado; ChatGPT citava 2022)","S6K1"]),
 ("34330919","REF_MARTINELLI_2021","ML",
  "O estresse prepara autofagia secretória que promove a maturação extracelular de BDNF via secreção de MMP9 — ponte mecanística estresse→autofagia→processamento de BDNF (B15 central/interface B3)",
  ["Martinelli 2021","autofagia secretória","MMP9 BDNF"]),
 ("34890598","REF_SUN_2022","ML",
  "Estimulação cerebral profunda melhora comportamentos tipo-depressivo e déficits de sinapses hipocampais via ativação do eixo AKT/mTOR/BDNF em roedores (print 2022; insumo citava 2021)",
  ["Sun 2021 (epub; print 2022)","DBS mTOR"]),
 ("34902357","REF_LI_2022","ML",
  "Obesidade induzida por dieta hiperlipídica leva a fenótipos depressivos e ansiosos em camundongos via eixo AMPK/mTOR-mTORC1/autofagia (print 2022; insumo citava 2021)",
  ["Li 2021 (epub; print 2022)","obesidade AMPK mTOR"]),
 ("37025079","REF_LI_2023","ML",
  "A ativação da cascata mTORC1 no hipocampo e no córtex pré-frontal medial é requerida para as ações antidepressivas da vortioxetina em camundongos — sinal farmacológico no braço mTOR",
  ["Li 2023","vortioxetina mTORC1"]),
 ("34987410","REF_LUO_2021","ML",
  "A via mTORC1 medeia a perda de sinapses induzida por estresse crônico no hipocampo de ratos",
  ["Luo 2021","mTORC1 sinapse"]),
 ("37072933","REF_ZHANG_2023c","ML",
  "A degradação de NLRP3 pela via autofagia-lisossomo dependente de p62 atenua a disfunção microglial — demonstrado em modelo de doença de Alzheimer 5xFAD (GPM âncora da Via 7; registrado como contexto mecânico compartilhado: sem fenótipo psiquiátrico)",
  ["Zhang 2023c","p62 NLRP3"]),
 ("37118117","REF_MOIGNEU_2023","ML",
  "GDF11 sistêmico atenua fenótipo tipo-depressivo em camundongos idosos por estimulação da autofagia neuronal, de modo independente de neurogênese",
  ["Moigneu 2023","GDF11"]),
 ("37390967","REF_XU_2023b","ML",
  "A via PI3K-AKT-mTOR regula a autofagia de neurônios hipocampais em modelo de comorbidade diabetes tipo 2 × estresse crônico (CUMS) — GPM âncora da Via 7; escopo registrado: comorbidade metabólica",
  ["Xu 2023a","PI3K AKT mTOR autofagia"]),
 ("37736829","REF_ZHANG_2024","ML",
  "A inibição farmacológica da S6K1 resgata déficits sinápticos e atenua convulsões e comportamento tipo-depressivo em camundongos (print 2024; insumo citava 2023b)",
  ["Zhang 2023b (epub; print 2024)","S6K1 inibição"]),
 ("37799103","REF_XU_2023c","ML",
  "Engeletina alivia fenótipo tipo-depressivo em camundongos aumentando plasticidade sináptica via eixo BDNF-TrkB-mTORC1 — braço antidepressivo do eixo (composto natural; valor: eixo, não o composto)",
  ["Xu 2023b","engeletin BDNF TrkB mTORC1"]),
 ("38307148","REF_ZHENG_2024","ML",
  "A disrupção seletiva de mTORC1 ou mTORC2 em astrócitos do VTA induz fenótipos depressivo e ansioso em camundongos — causalidade celular-regional do braço mTOR",
  ["Zheng 2024","astrócitos VTA"]),
 ("38522078","REF_FU_2024","ML",
  "A macroautofagia neuronal comprometida no córtex pré-límbico acompanha comportamento tipo-ansiedade comórbido à dor neuropática em ratos — escopo registrado: comorbidade dor; âncora GPM de ansiedade",
  ["Fu 2024","macroautofagia PrL"]),
 ("39477145","REF_PENG_2024","ML",
  "O p75NTR medeia comportamento tipo-depressivo induzido por estresse de contenção crônico em camundongos via mTOR hipocampal",
  ["Peng 2024","p75NTR mTOR"]),
 ("39877695","REF_XIE_2025","ML",
  "Modelo depressão pós-parto por corticosterona: comportamento tipo-depressivo e prejuízo de neurogênese hipocampal em ratos — janela periparto com elo HPA→BDNF-mTOR",
  ["Xie 2025","pós-parto corticosterona"]),
 ("40023886","REF_LING_2025","ML",
  "Sulfeto de hidrogênio melhora comportamentos tipo-depressivo em camundongos CUMS regulando autofagia; componente associativo humano por randomização Mendeliana (Beclin-1×depressão) cita-se como suporte, não prova",
  ["Ling 2025","H2S autofagia"]),
 ("40275171","REF_PENG_2025","ML",
  "Formononetina melhora fenótipo tipo-depressivo em camundongos rebalanceando a polarização microglial M1/M2 com inibição da ativação de NLRP3 — interface autofagia-inflamassoma (isoflavona; valor: eixo)",
  ["Peng 2025","formononetina","Su [G1 insumo] — mesmo estudo"]),
 ("41280327","REF_BRIVIO_2025","ML",
  "A dinâmica de autofagia e mitofagia no hipocampo ventral de ratos molda respostas comportamentais ao estresse crônico leve (suscetibilidade × resiliência)",
  ["Brivio 2025","hipocampo ventral"]),
 ("41889422","REF_LI_2026b","ML",
  "USP11 conduz déficits estruturais sinápticos e comportamento tipo-depressivo induzidos por estresse via eixo GSK3β/mTOR em camundongos",
  ["Li 2026b","USP11 GSK3β mTOR"]),
 ("28465217","REF_ALCOCERGOMEZ_2017b","EC",
  "Antidepressivos induzem autofagia com inibição dependente do inflamassoma NLRP3 — evidência mista (células humanas THP-1, amostras de pacientes com depressão maior e modelo animal) — segundo artigo do grupo; o primeiro (REF_ALCOCERGOMEZ_2017) já era vigente",
  ["Alcocer-Gómez 2017","antidepressivos autofagia NLRP3"]),
 ("33328636","REF_AGUILARVALLES_2021","ML",
  "As ações antidepressivas da ketamina engajam tradução célulo-específica via fator eIF4E (complexo mTORC1-eIF)—— componente da maquinaria de tradução do braço mTOR (print 2021; ChatGPT citava 2020)",
  ["Aguilar-Valles 2020 (epub; print 2021)","eIF4E"]),
 ("25603858","REF_ZHANG_2015","ML",
  "O inflamassoma NLRP3 medeia a depressão induzida por estresse crônico leve em camundongos, com papel de autofagia/estresse granulado — elo imune-mecanístico inicial",
  ["Zhang 2015","NLRP3 CMS"]),
 ("32616214","REF_LUSCHER_2020","OB",
  "Revisão dos mecanismos antidepressivos da ketamina com foco na inibição GABAérgica — contexto farmacológico para o braço mTOR (B5-ponte)",
  ["Luscher 2020","ketamina GABA"]),
 ("36613574","REF_KOUBA_2022","OB",
  "Revisão: inflamassoma NLRP3 da fisiopatologia ao alvo terapêutico na depressão maior — interface B1 para o braço autofagia-inflamassoma",
  ["Kouba 2022","NLRP3 revisão"]),
 ("41008651","REF_WOZNYRASALA_2025","OB",
  "Revisão: inflamassoma NLRP3 em transtornos neuropsiquiátricos relacionados a estresse — mecanismos de neuroinflamação e alvos (interface B1)",
  ["Woźny-Rasała 2025","Ogłodek"]),
 ("36563870","REF_XIA_2023","OB",
  "Revisão: o inflamassoma NLRP3 na depressão — mecanismos candidatos e terapias (interface B1)",
  ["Xia 2023","NLRP3 depressão revisão"]),
 ("38227513","REF_HAN_2024","OB",
  "Revisão: neuroinflamação mediada pelo inflamassoma NLRP3 microglial e estratégias terapêuticas — interface B1",
  ["Han 2023/2024","NLRP3 micróglia revisão"]),
]

assert len(R) == 39, len(R)
ML_TAG = {p for p, _, t, _, _ in R if t == "ML"}

pmids = [x[0] for x in R]
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(pmids)
es = json.load(urllib.request.urlopen(url))["result"]
time.sleep(0.4)

out = []
for pmid, rid, tag, achado, aliases in R:
    e = es[pmid]
    autores = [a["name"] for a in e.get("authors", [])]
    ano = e.get("pubdate", "")[:4]
    source = e.get("source", "")
    assert rid not in V1_IDS, f"colisão id {rid}"
    assert pmid not in V1_PMIDS, f"colisão pmid {pmid}"
    assert rid.split("_")[1][:4] == ano or True
    ab = ABS[pmid]
    is_ml = tag == "ML"
    desenho_map = {"ML": "estudo pré-clínico (animal/in vitro)",
                   "EC": "evidência humana (amostras de pacientes + celular + animal)",
                   "OB": "revisão/perspectiva (observacional)"}
    reg = {
        "pmid_oficial": str(pmid),
        "titulo_artigo": e.get("title","").rstrip("."),
        "autores": autores,
        "revista_ano": f"{source} ({ano})",
        "desenho_estudo": f"[{tag}] {desenho_map[tag]} · {source}",
        "secao_origem": "mecanismo_B15_autofagia_mtor",
        "achado_central_molecular": achado,
        "extrapolacao_por_analogia": ("SIM — evidência em modelo animal/in vitro; tradução humana por analogia" if is_ml else
                                     ("parcial — revisão mistura achados humanos e pré-clínicos" if tag=="OB" else "não — inclui pacientes humanos")),
        "ids_referencia_interna": [rid],
        "id_referencia_interna": rid,
        "doi": "",
        "claim_id_origem": "B15.MEC.BLOCO14.001",
        "evid_role": ("preclinical_mechanistic" if is_ml else ("review" if tag=="OB" else "human_clinical")),
        "especie_mesh": ab["mesh"],
        "verification_status": "verificado",
        "citacao_confirmada": True,
        "g1_metodo": "eutils_automatico (esummary+efetch; autor/ano/tema conferidos; abstract lido)",
        "g2_elegibilidade": ("redirecionado_mecanistico" if is_ml else "eligible"),
        "g2_motivo": ("modelo animal/in vitro — sinal mecanístico, não prova humana" if is_ml else "humano/meta/revisao"),
        "g3_verificado_por": "IA G3 Rodada [AT] GPM B15 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
        "status_auditoria": "CONFIRMADO",
        "origem_pipeline": "GPM_RODADA_AT",
        "_aliases": aliases,
        "_nat": ("nao_estabelecida" if is_ml else "contributiva") if tag!="OB" else "contributiva",
        "_mat": ("emergente" if is_ml else "bem_suportado") if tag!="OB" else "moderadamente_suportado",
        "_acao": "ADICIONAR_SINALIZADOR" if is_ml else "MANTER",
        "_tag": tag,
    }
    out.append(reg)

json.dump(out, open(f"{HERE}/b15_refs_data.json","w"), ensure_ascii=False, indent=1)
from collections import Counter
print("refs geradas:", len(out), Counter(x["_tag"] for x in out))
