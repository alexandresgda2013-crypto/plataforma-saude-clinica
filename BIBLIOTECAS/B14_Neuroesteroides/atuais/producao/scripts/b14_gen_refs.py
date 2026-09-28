#!/usr/bin/env python3
# B14 — gera refs_data.json para as 50 referências ENTRA da rodada [AT 2026-09-09]
# Fonte: eutils esummary (autor real + pubdate print) + efetch abstracts já lidos (b14_efetch_sel.json)
import json, re, urllib.request, time, os

HERE = os.path.dirname(os.path.abspath(__file__))
META = json.load(open(f"{HERE}/producao/insumos/insumos_b14_meta.json"))
ABS = json.load(open(f"{HERE}/b14_efetch_sel.json"))
V1 = json.load(open(f"{HERE}/Evidencias/Bibliografia/01_pmids.json"))
V1_IDS = {r["id_referencia_interna"] for r in V1}
V1_PMIDS = {str(r["pmid_oficial"]) for r in V1}

# pmid -> (id, tag, achado_central_molecular, evid_role, nat_mat, acao, tier, forca_bio, uso, aliases, extr)
R = [
 ("10557352","REF_GRIFFIN_1999","ML",
  "ISRS alteram diretamente a atividade de enzimas neuroesteroidogênicas e elevam a síntese de alopregnanolona por mecanismo dissociado da recaptação de serotonina",
  ["Griffin","Mellon","fluoxetina","SSRI"]),
 ("11720889","REF_STOFFELWAGNER_2001","OB",
  "Revisão do metabolismo de neuroesteroides no cérebro humano: enzimas esteroidogênicas presentes no SNC, localização regional e efeitos putativos",
  ["Stoffel-Wagner","Stoffel-Wagner 2001"]),
 ("14993041","REF_STOFFELWAGNER_2003","OB",
  "Biossíntese de neuroesteroides no cérebro humano (P450scc, aromatase, 5α-redutase, 3α-HSD) e suas implicações clínicas",
  ["Stefaniak 2023 (rótulo do insumo — autor real Stoffel-Wagner, print 2003)","Stoffel-Wagner 2003"]),
 ("18003893","REF_AGISBALBOA_2007","ML",
  "Isolamento social prolongado em camundongos reduz a biossíntese de alopregnanolona (5α-redutase tipo I) em circuitos corticolímbicos, paralelamente a alterações comportamentais",
  ["Agís-Balboa 2007","Agis-Balboa"]),
 ("23348009","REF_SRIPADA_2013","EC",
  "Administração de pregnenolona em humanos eleva a alopregnanolona e associa-se a redução da atividade da amígdala e da ínsula e a maior conectividade de regulação emocional (ensaio mecanístico com neuroimagem)",
  ["Sripada 2013b / pregnenolona","Sripada"]),
 ("24302681","REF_SRIPADA_2014","EC",
  "Em humanos, alopregnanolona e DHEA séricos modulam a conectividade funcional de repouso da amígdala — níveis maiores associados a menor acoplamento amígdala–hipocampo (padrão compatível com regulação afetiva)",
  ["Sripada 2013a / ALLO-DHEA","Sripada"]),
 ("24402140","REF_MACKENZIE_2014","OB",
  "Neuroesteroides derivados de hormônios ovarianos regulam os receptores GABA-A (plasticidade de subunidades) e a vulnerabilidade afetiva no período reprodutivo",
  ["MacKenzie & Maguire 2014","MacKenzie","Maguire"]),
 ("24781515","REF_AGISBALBOA_2014","EC",
  "Córtex pré-frontal (área de Brodmann 9) post-mortem de pacientes com depressão maior apresenta expressão reduzida de 5α-redutase tipo I — substrato molecular da deficiência de alopregnanolona",
  ["Agís-Balboa 2014","Agis-Balboa","5α-redutase PFC"]),
 ("25436563","REF_MACKENZIE_2013","OB",
  "Revisão integrativa de neuroesteroides e sinalização GABAérgica em saúde e doença: síntese local, flutuações fisiológicas e resposta ao estresse",
  ["Luscher 2023 (rótulo do insumo §3 — real: MacKenzie & Maguire 2013; Luscher 2023 = REF_LUSCHER_2023 já vigente)","MacKenzie & Maguire 2013"]),
 ("27306650","REF_ROSSETTI_2016","OB",
  "Estrógenos e progestágenos sintetizados de novo no tecido neural: enzimas, distribuição e funções (proteção hipocampal e cognição)",
  ["Rossetti","Rossetti 2016"]),
 ("28825678","REF_GUO_2017","ML",
  "Em ratos submetidos a estresse crônico imprevisível, a fórmula fitoterápica Xiaoyaosan reverteu comportamento tipo-depressivo normalizando neuroesteroides e a expressão de mRNAs das enzimas de síntese/metabolismo (valor: eixo neuroesteroide; não a fórmula)",
  ["Guo 2017","Xiaoyaosan"]),
 ("29199875","REF_ZSIDO_2017","OB",
  "Revisão: transições hormonais (ciclo, gestação→pós-parto, perimenopausa) como janelas de vulnerabilidade e contribuição da tomografia por emissão de pósitrons para mapear alterações neuroquímicas associadas",
  ["Zsido","Zsido 2017","PET hormônios"]),
 ("30321584","REF_HE_2019","OB",
  "17β-hidroxisteroides desidrogenases como etapas enzimáticas indispensáveis da neuroesteroidogênese no sistema nervoso central",
  ["He 2019","17β-HSD"]),
 ("31709278","REF_WALTON_2019","OB",
  "Perspectiva: a aprovação regulatória de tratamento à base de alopregnanolona (brexanolona) na depressão pós-parto como validação mecanística do eixo alopregnanolona–GABA-A — por que/como funciona",
  ["Walton & Maguire 2019","Walton","Maguire","brexanolona"]),
 ("32435663","REF_MELTZERBRODY_2020","OB",
  "Revisão: papel da alopregnanolona na fisiopatologia e no tratamento da depressão pós-parto",
  ["Matthew 2013 (rótulo do insumo — real: Meltzer-Brody & Kanes 2020, item §4 que constava 'não localizada')","Meltzer-Brody","Kanes"]),
 ("32435665","REF_PAUL_2020","OB",
  "Alopregnanolona: da fisiopatologia molecular (ações não-genômicas rápidas via GABA-A) à terapêutica — perspectiva histórica de três décadas",
  ["Paul","Pinna","Guidotti","Paul 2020"]),
 ("33404887","REF_NILLNI_2021","OB",
  "Revisão: efeitos da fase do ciclo menstrual e de seus hormônios em desfechos de ansiedade e TEPT, mecanismos neurobiológicos propostos e limitações metodológicas",
  ["Nillni","Nillni 2021","ciclo menstrual"]),
 ("33585496","REF_SCHWEIZERSCHUBERT_2021","OB",
  "Sensibilidade a hormônios esteroides (não os níveis absolutos) como base dos transtornos de humor reprodutivos — papel da sensibilidade do receptor GABA-A e do estresse",
  ["Schiller 2016 (rótulo do insumo — real: Schweizer-Schubert et al.; era [G1] da Via 7)","Schweizer-Schubert"]) ,
 ("35716803","REF_KUNDAKOVIC_2022","OB",
  "Flutuação de hormônios sexuais e risco feminino elevado de depressão e ansiedade: do nível etiológico ao mecanístico — revisão",
  ["Kundakovic & Rocks 2022","Kundakovic","Rocks"]),
 ("35809362","REF_LOZZAFIACCO_2022","EC",
  "Na transição menopausal, maior variabilidade do estradiol predisse fenótipos depressivos com ansiedade/anedonia; ensaio experimental mostra sensibilidade individual basal ao estradiol como preditor de resposta sintomática",
  ["Locci & Pinna 2017 (rótulo do insumo — real: Lozza-Fiacco 2022; Locci & Pinna 2017 = REF_LOCCI_2017 já vigente)","Lozza-Fiacco"]) ,
 ("35908135","REF_HERSON_2022","OB",
  "Revisão: agentes hormonais no tratamento da depressão associada à menopausa — camada intervenção-sinal, distinta do eixo endógeno",
  ["Herson & Kulkarni 2022","Herson","Kulkarni"]),
 ("36725341","REF_LU_2023","ML",
  "Alopregnanolona potencia a inibição GABAérgica em interneurônios parvalbumina do hipocampo — braço celular do efeito neuroesteroide",
  ["Lu 2023","interneurônios PV"]),
 ("36937732","REF_GAO_2023","OB",
  "TPM/PMDD conceituada como transtorno de sensibilidade subótima a neuroesteroides: mediação por sensibilidade do receptor GABA-A à alopregnanolona",
  ["Gao 2023","PMDD"]),
 ("37068417","REF_ZHANG_2023","EC",
  "Revisão sistemática com meta-análise de ensaios randomizados: estrogênio exógeno associado a melhora do humor depressivo em mulheres — evidência de intervenção (sinal), distinta do eixo endógeno",
  ["Zhang 2023","estrogênio exógeno","HRT sinal"]),
 ("38899227","REF_YAWATA_2024","ML",
  "Alopregnanolona e diazepamapresentam efeitos diferenciais sobre comportamento social por modulação distinta de oscilações (modelo murino) — farmacologia comparada pré-clínica",
  ["Yawata 2024","ALLO vs diazepam"]),
 ("40261706","REF_KOGANTI_2025","ML",
  "Mapa em resolução de célula única da neuroesteroidogênese no cérebro murino: etapas intermediárias de biossíntese distribuídas por populações celulares",
  ["Koganti & Selvaraj 2025","Koganti","single-cell"]),
 ("36961547","REF_ALBLOOSHI_2023","EC",
  "Revisão sistemática: a menopausa eleva o risco de desenvolver depressão e ansiedade diagnosticadas",
  ["Alblooshi 2023","menopausa risco"]),
 ("36433781","REF_ANTONELLI_2022","OB",
  "Revisão narrativa: transtornos de humor e estados de ansiedade em relação ao status hormonal ao longo da vida da mulher, da puberdade à menopausa",
  ["Antonelli 2022","Antonelli"]),
 ("24044974","REF_BALI_2014","OB",
  "Aspectos multifuncionais da alopregnanolona no estresse e em transtornos relacionados: síntese por 5α-redutase/3α-HSD e interação com o eixo do estresse",
  ["Bali & Jaggi 2014","Bali","Jaggi"]),
 ("34644812","REF_BELELLI_2022","OB",
  "Relacionar a modulação neuroesteroide da neurotransmissão inibitória ao comportamento: síntese mecanística dos PAMs endógenos do GABA-A (resolve [G1] 'Belelli 2021/2022' do GPM M00)",
  ["Belelli 2021 (rótulo do insumo — print 2022)","Belelli"]),
 ("31879693","REF_BOERO_2020","OB",
  "Ações pleiotrópicas da alopregnanolona subjacentes a benefícios terapêuticos em doenças relacionadas ao estresse, incluindo TEPT e depressão (perspectiva mecanística)",
  ["Boero 2020","Boero"]),
 ("39444825","REF_DUKIC_2024","EC",
  "Gestação→pós-parto: trajetórias longitudinais (classes latentes) de estradiol e progesterona associam-se diferencialmente a desfechos afetivos — heterogeneidade individual como achado central",
  ["Dukic 2024","Dukic"]),
 ("37423029","REF_ETYEMEZ_2023","EC",
  "Metabólitos da progesterona durante a gestação associam-se a ansiedade perinatal — coorte prospectiva",
  ["Etyemez 2023","Etyemez","ansiedade perinatal"]),
 ("40538358","REF_ETYEMEZ_2025","OB",
  "Revisão: biomarcadores em transtornos psiquiátricos reprodutivos — transições hormonais (ciclo, gestação, puerpério, menopausa) como janelas translacionais; sem ferramenta diagnóstica pronta",
  ["Etyemez 2025","biomarcadores reprodutivos"]),
 ("16373246","REF_EVANS_2005","EC",
  "Neuroesteroides 3α-reduzidos (alopregnanolona, pregnanolona) e precursores durante a gestação e o pós-parto: flutuações fisiológicas e relação com o humor",
  ["Evans 2005 (duplicata interna do insumo colapsada §4)","Gilbert Evans"]),
 ("39640510","REF_GROTSCH_2024b","EC",
  "Avaliação longitudinal em mulheres saudáveis: alopregnanolona e humor ao longo do periparto — relação sugerida em forma de U, com sensibilidade individual",
  ["Grötsch 2024 (longitudinal — distinto do REF_GROTSCH_2024 vigente, revisão sistemática)","Grötsch"]),
 ("42292154","REF_GUAN_2026","OB",
  "Revisão: moduladores do receptor GABA-A como agentes terapêuticos emergentes nos transtornos depressivos — camada terapêutica-sinal",
  ["Guan & Li 2026","Guan"]),
 ("24776841","REF_HELLGREN_2014","EC",
  "Alopregnanolona sérica baixa no final da gestação associa-se a sintomas depressivos (resolve [G1] 'Hellgren' do GPM/Via 6)",
  ["Hellgren 2014","Hellgren"]),
 ("31031589","REF_JARIC_2019","ML",
  "Modelo de desenvolvimento em dois insultos (roedor): efeitos de sexo e de ciclo estral sobre fenótipos de ansiedade e depressão — interação desenvolvimento × hormônio",
  ["Jain 2005 (rótulo do insumo §6 — real: Jarić et al. 2019, item §4 que constava 'não resolvida')","Jarić 2019","Jaric"]),
 ("27856395","REF_LI_2017","OB",
  "Revisão integrativa: vulnerabilidade aumentada das mulheres a transtornos de ansiedade, trauma e estresse — papel potencial dos hormônios sexuais (estradiol/progesterona)",
  ["Li & Graham 2017","Li 2016","Graham"]),
 ("41598293","REF_MARANO_2026","OB",
  "Neuroinflamação no cérebro feminino: mecanismos sexo-específicos em transtornos de humor e de estresse — interface com o eixo neuroesteroide (ponte B1↔B14)",
  ["Marano 2026","Marano"]),
 ("29290217","REF_MULHALL_2018","EC",
  "Amostra comunitária de mulheres de meia-idade: sintomas de depressão e ansiedade variam significativamente conforme o status menopausal",
  ["Mulhall 2018","Mulhall"]),
 ("38029039","REF_NAGDA_2023","EC",
  "Avaliação transversal: depressão, ansiedade e cognição em mulheres na transição peri/pós-menopausa",
  ["Nagda 2023","Nagda"]),
 ("26018188","REF_NEWHOUSE_2015","OB",
  "Comentário: modelo neurocognitivo integrando estrógeno, estresse e depressão",
  ["Newhouse & Albert 2015","Newhouse"]),
 ("41390123","REF_ROSS_2026","OB",
  "Revisão seletiva: mecanismos moleculares candidatos do risco de suicídio relacionado ao ciclo menstrual — flutuação ovariana cíclica como janela de vulnerabilidade",
  ["Ross 2025 (rótulo do insumo — print 2026)","Ross"]),
 ("34330326","REF_SANDER_2021","EC",
  "Coorte na transição menopausal tardia: examina a relação entre testosterona e sintomas depressivos",
  ["Sander 2021","Sander","testosterona"]),
 ("34714413","REF_STANDEVEN_2022","EC",
  "Estudo exploratório longitudinal: alopregnanolona e sintomas de depressão/ansiedade em múltiplos tempos ao longo do periparto",
  ["Standeven 2021","Standeven"]),
 ("16938407","REF_STROMBERG_2006","ML",
  "Modulação neurosteroide experimental da ação da alopregnanolona e do GABA sobre o receptor GABA-A",
  ["Strömberg 2006","Strömberg"]),
 ("32730861","REF_SUNDSTROMPOROMAA_2020","OB",
  "Revisão abrangente da progesterona e de seu metabólito alopregnanolona: propriedades biológicas, metabolismo e efeitos sobre humor e saúde mental feminina — 'progesterona, amiga ou adversa?'",
  ["Stumper 2026 (rótulo do insumo — real: Sundström-Poromaa 2020, item §4 'não resolvida')","Sundström-Poromaa"]),
 ("40211702","REF_YU_2025","OB",
  "Revisão: depressão perimenopausal sob a ótica de inflamação e estresse oxidativo — alvos e interface B1/B9",
  ["Yu 2025","Yu"]),
]

assert len(R) == 50, len(R)
ML = {"10557352","18003893","36725341","38899227","28825678","31031589","40261706","16938407"}

# buscar autores completos + pubdate exato (batch único)
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
    ab = ABS[pmid]
    especie = ab["mesh"]
    is_ml = pmid in ML
    humano = any("Humans" == m for m in especie) or not is_ml
    desenho_map = {
        "ML": "estudo pré-clínico (animal/in vitro)",
        "EC": "evidência humana (clínico/coorte/ensaio/meta-análise)",
        "OB": "revisão/perspectiva (observacional)"}
    reg = {
        "pmid_oficial": str(pmid),
        "titulo_artigo": e.get("title","").rstrip("."),
        "autores": autores,
        "revista_ano": f"{source} ({ano})",
        "desenho_estudo": f"[{tag}] {desenho_map[tag]} · {source}",
        "secao_origem": "mecanismo_B14_neuroesteroides_hormonios_neuroativos",
        "achado_central_molecular": achado,
        "extrapolacao_por_analogia": ("SIM — evidência em modelo animal/in vitro; tradução humana por analogia" if is_ml else
                                       ("parcial — revisão mistura achados humanos e pré-clínicos" if tag=="OB" else "não — evidência humana")),
        "ids_referencia_interna": [rid],
        "id_referencia_interna": rid,
        "doi": "",
        "claim_id_origem": "B14.MEC.BLOCO14.001",
        "evid_role": ("preclinical_mechanistic" if is_ml else ("review" if tag=="OB" else "human_clinical")),
        "especie_mesh": especie,
        "verification_status": "verificado",
        "citacao_confirmada": True,
        "g1_metodo": "eutils_automatico (esummary+efetch; autor/ano/tema conferidos; abstract lido)",
        "g2_elegibilidade": ("redirecionado_mecanistico" if is_ml else "eligible"),
        "g2_motivo": ("modelo animal/in vitro — sinal mecanístico, não prova humana" if is_ml else "humano/meta/revisao"),
        "g3_verificado_por": "IA G3 Rodada [AT] GPM B14 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
        "status_auditoria": "CONFIRMADO",
        "origem_pipeline": "GPM_RODADA_AT",
        "_aliases": aliases,
        # campos privados para o json_apply (removidos do pmids.json final)
        "_nat": ("nao_estabelecida" if is_ml else "associativa") if tag!="OB" else "contributiva",
        "_mat": ("emergente" if is_ml else "bem_suportado") if tag!="OB" else "moderadamente_suportado",
        "_acao": "ADICIONAR_SINALIZADOR" if is_ml else "MANTER",
        "_tier": "tier_3_mecanistico_extrapolado" if is_ml else "tier_4_descritivo_estrutural",
        "_forca": "media(preclinico)" if is_ml else ("media-alta(revisao)" if tag=="OB" else "alta(humano)"),
        "_uso": "nucleo_causal" if is_ml else "suporte",
        "_tag": tag,
        "_ptypes": ab["ptypes"],
    }
    out.append(reg)

json.dump(out, open(f"{HERE}/b14_refs_data.json","w"), ensure_ascii=False, indent=1)
from collections import Counter
print("refs geradas:", len(out), Counter(x["_tag"] for x in out))
print("anos print:", sorted({x['id_referencia_interna'] for x in out})[:6], "...")
