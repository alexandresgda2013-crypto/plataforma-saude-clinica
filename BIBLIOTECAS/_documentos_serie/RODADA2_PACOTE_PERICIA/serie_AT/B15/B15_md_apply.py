#!/usr/bin/env python3
# B15 — V1 -> V2: rotação, BLOCO_14/15, apêndice [AT], cabeçalho, asserts
import json, re, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
V1P = os.path.join(HERE, "B15 AUTOFAGIA MTOR V1 CANONICA.md")
V2P = os.path.join(HERE, "B15 AUTOFAGIA MTOR V2 CANONICA.md")
HIST = os.path.join(HERE, "producao", "historico", "v1_canonica_2026-09-09.md")

doc = open(V1P, encoding="utf-8").read()
os.makedirs(os.path.dirname(HIST), exist_ok=True)
shutil.copyfile(V1P, HIST)

doc = doc.replace("# B15 AUTOFAGIA / mTOR V1 CANÔNICA", "# B15 AUTOFAGIA / mTOR V2 CANÔNICA", 1)
doc = doc.replace(
 "**ID canônico:** mecanismo_B15_autofagia_mtor · **Prompt v4.2** · Corte: 2026-09-07.",
 "**ID canônico:** mecanismo_B15_autofagia_mtor · **Prompt v4.2** · Corte: 2026-09-07; rodada [AT 2026-09-09], corte E-utilities 2026-09-09/10.", 1)

B14 = """---

## BLOCO_14 — ATUALIZAÇÃO CANÔNICA [[AT 2026-09-09]] · INSUMO EXTERNO AUDITADO REF A REF (P-7)

> **Proveniência.** Rodada [AT] do GPM B15: índice de 49 âncoras com PMIDs cravados, §6 com 129 itens do insumo não citados, correções §4 (Ulecia-Morón; Ota; Koehl publicada; famílias Li/Zhang desambiguadas; Fukumoto-lixo; onda 09/09 com vortioxetina) e lacunas §8, reconciliados contra a V1 pelo pipeline G1 (esummary + efetch; abstract lido antes de incorporar). Das 49 âncoras, 31 não constavam da V1 e entraram; das 129 da §6, 8 entraram por evidência mecanística direta no eixo autofagia/mTOR; ~76 compõem a **leva N de suporte** (mTOR-plasticidade B3, BDNF-ketamina, HPA, mitocôndria B8, reviews e contexto) registrada com decisões individuais em `producao/insumos/matriz_b15_decisao.json`; ~28 excluídos por malha (Alzheimer/Parkinson/autismo/fragil-X/dor-entorrinal — CAMADA C) e 2 NAO-IDX. Cinco divergências de identidade entre rótulo do insumo e artigo real foram **expostas** (BLOCO_15, regra 08). Nenhum identificador foi inventado; nenhum número do insumo entrou sem fonte.

### B14.1 — Braço mTOR: regionalidade, astrócitos e causalidade pré-clínica

A disrupção seletiva de mTORC1 ou mTORC2 em astrócitos do VTA induz fenótipos depressivo e ansioso em camundongos — causalidade celular-regional do braço mTOR (Zheng, 2024)[ML].
A via mTORC1 medeia a perda de sinapses induzida por estresse crônico no hipocampo de ratos (Luo, 2021)[ML].
A ativação da cascata mTORC1 no hipocampo e no córtex pré-frontal medial é requerida para as ações antidepressivas da vortioxetina em camundongos (Li, 2023)[ML].
Engeletina alivia fenótipo tipo-depressivo em camundongos aumentando plasticidade sináptica via eixo BDNF-TrkB-mTORC1 (Xu, 2023)[ML].
O p75NTR medeia comportamento tipo-depressivo induzido por estresse crônico em camundongos via mTOR hipocampal (Peng, 2024)[ML].
USP11 conduz déficits estruturais sinápticos e comportamento tipo-depressivo induzidos por estresse via eixo GSK3β/mTOR em camundongos (Li, 2026)[ML].
As ações antidepressivas da ketamina engajam tradução célulo-específica via fator eIF4E (Aguilar-Valles, 2021)[ML].
Os efeitos antidepressivos da ketamina associam-se à regulação ascendente mediada por receptores AMPA do eixo mTOR no hipocampo (Zhou, 2014)[ML].
A agmatina produz efeitos tipo-antidepressivo ativando receptores AMPA e a sinalização mTOR (Neis, 2016)[ML].
A ativação da AMPK no hipocampo de ratos participa das ações antidepressivas da ketamina (Xu, 2013)[ML].
A fluoxetina regula a sinalização mTOR de modo região-dependente em camundongos tipo-depressivo (Liu, 2015)[ML].
A ketamina promove plasticidade estrutural em neurônios dopaminérgicos murinos e derivados de iPSC humano (Cavalleri, 2018)[ML].
A remoção genética da p70 S6 quinase 1, efetor de mTORC1, aumenta o comportamento tipo-ansiedade em camundongos (Koehl, 2021)[ML].
Os mecanismos neurotróficos das ações antidepressivas rápidas e sustentadas da ketamina foram revistos (BDNF, VEGF, mTOR) (Deyama & Duman, 2020)[OB].
A revisão com foco GABAérgico dos mecanismos da ketamina dá o contexto farmacológico do braço (Luscher, 2020)[OB].

* ZHENG_2024[ML] | LUO_2021[ML] | LI_2023[ML] | XU_2023c[ML] | PENG_2024[ML] | LI_2026b[ML] | AGUILARVALLES_2021[ML] | ZHOU_2014[ML] | NEIS_2016[ML] | XU_2013[ML] | LIU_2015[ML] | CAVALLERI_2018[ML] | KOEHL_2021[ML] | DEYAMA_2020[OB] | LUSCHER_2020[OB] *

### B14.2 — Estresse e HPA × mTOR/autofagia: exposições e janelas

Em ratos expostos a estresse, a fosforilação de componentes da via mTOR está reduzida na amígdala (Chandran, 2013)[ML].
REDD1 é essencial para a perda sináptica induzida por estresse e o comportamento depressivo em camundongos (Ota, 2014)[ML].
Estresse precoce altera plasticidade sináptica e sinalização mTOR em ratos, com correlação a fenótipos tipo-ansiedade (Wang, 2020)[ML].
Estimulação cerebral profunda melhora comportamentos tipo-depressivo e déficits de sinapses hipocampais via eixo AKT/mTOR/BDNF (Sun, 2022)[ML].
Glucocorticoides reprimem a autofagia mediada por chaperonas e a microautofagia (Sato, 2020)[ML].
Modelo depressão pós-parto por corticosterona: comportamento tipo-depressivo e prejuízo de neurogênese hipocampal em ratos (Xie, 2025)[ML].
A macroautofagia neuronal comprometida no córtex pré-límbico acompanha comportamento tipo-ansiedade comórbido à dor neuropática em ratos (Fu, 2024)[ML].

* CHANDRAN_2013[ML] | OTA_2014[ML] | WANG_2020[ML] | SUN_2022[ML] | SATO_2020[ML] | XIE_2025[ML] | FU_2024[ML] *

### B14.3 — Fluxo autofágico: insuficiente, excessivo e adaptativo (sem dualidade simplista)

A dinâmica de autofagia e mitofagia no hipocampo ventral de ratos molda respostas comportamentais ao estresse crônico leve (Brivio, 2025)[ML].
GDF11 sistêmico atenua fenótipo tipo-depressivo em camundongos idosos por estimulação da autofagia neuronal, independentemente de neurogênese (Moigneu, 2023)[ML].
Sulfeto de hidrogênio melhora comportamentos tipo-depressivo em camundongos CUMS regulando autofagia; a associação humana por randomização Mendeliana (Beclin-1×depressão) é suporte, não prova (Ling, 2025)[ML].
A inibição farmacológica da S6K1 resgata déficits sinápticos e atenua comportamento tipo-depressivo em camundongos (Zhang, 2024)[ML].
Obesidade induzida por dieta leva a fenótipos depressivos e ansiosos em camundongos via eixo AMPK/mTOR/autofagia (Li, 2022)[ML].
A via PI3K-AKT-mTOR regula a autofagia de neurônios hipocampais em modelo de comorbidade diabetes tipo 2 × estresse crônico (Xu, 2023)[ML].
O estresse prepara autofagia secretória que promove a maturação extracelular de BDNF via secreção de MMP9 (Martinelli, 2021)[ML].

* BRIVIO_2025[ML] | MOIGNEU_2023[ML] | LING_2025[ML] | ZHANG_2024[ML] | LI_2022[ML] | XU_2023b[ML] | MARTINELLI_2021[ML] *

### B14.4 — Interface autofagia → inflamassoma (ponte B1)

O inflamassoma NLRP3 medeia a depressão induzida por estresse crônico leve em camundongos (Zhang, 2015)[ML].
Antidepressivos induzem autofagia com inibição dependente do inflamassoma NLRP3 — evidência mista em células humanas THP-1, amostras de pacientes e modelo animal (Alcocer-Gómez, 2017)[EC].
A degradação de NLRP3 pela via autofagia-lisossomo dependente de p62 atenua a disfunção microglial em modelo de doença de Alzheimer (Zhang, 2023)[ML].
Formononetina melhora fenótipo tipo-depressivo em camundongos rebalanceando a polarização microglial M1/M2 com inibição de NLRP3 (Peng, 2025)[ML].
O inflamassoma NLRP3 foi revisto da fisiopatologia ao alvo terapêutico na depressão maior (Kouba, 2022)[OB].
O inflamassoma NLRP3 na depressão foi revisto com mecanismos candidatos e terapias (Xia, 2023)[OB].
O NLRP3 em transtornos neuropsiquiátricos relacionados a estresse foi revisto com foco nos mecanismos de neuroinflamação (Woźny-Rasała & Ogłodek, 2025)[OB].
A neuroinflamação mediada por inflamassomas NLRP3 microgliais e suas estratégias terapêuticas foi revista (Han, 2024)[OB].

* ZHANG_2015[ML] | ALCOCERGOMEZ_2017b[EC] | ZHANG_2023c[ML] | PENG_2025[ML] | KOUBA_2022[OB] | XIA_2023[OB] | WOZNYRASALA_2025[OB] | HAN_2024[OB] *

### B14.5 — Panorama e convergência farmacológica (contexto)

O braço mTOR como encruzilhada de plasticidade, memória e doença — panorama de referência (Hoeffer & Klann, 2010)[OB].
A sinalização dependente de mTORC1 subjaz ao efeito rápido de creatina e ketamina em teste comportamental murino (Pazini, 2020)[ML].

* HOEFFER_2010[OB] | PAZINI_2020[ML] *

---

## BLOCO_15 — REGRAS CANÔNICAS DA RODADA [AT] (B15-REGRA-01..10), EXPOSIÇÕES, MALHA E LACUNAS [G1]

**B15-REGRA-01 — Regra do fluxo autofágico (obrigatória).** É proibido inferir "autofagia ativada/inibida" a partir de LC3-II, Beclin-1 ou p62 em uma única condição; distinguir expressão × autofagossomo × degradação lisossomal × fluxo efetivo, e basal × induzida × excessiva × insuficiente.

**B15-REGRA-02 — "Depressão = baixa autofagia" é proibido.** A hiperautofagia consome BDNF (Zhang âncora vigente REF_ZHANG_2023) e a direção depende da temporalidade do estresse (Yang âncora vigente REF_YANG_2025); insuficiente, excessiva e adaptativa coexistem na biblioteca.

**B15-REGRA-03 — mTOR é bifásico e regional.** mTORC1 sináptico-plástico ≠ mTORC1 lisossomal-autofágico; astrócitos do VTA (Zheng, 2024) e córtex infralímbico (âncora vigente Garro-Martínez) dão causalidade regional; não extrapolar para o cérebro inteiro.

**B15-REGRA-04 — Ketamina = interface, não núcleo.** Li-2010 e congêneres entram como fundação do braço mTOR-plasticidade; ketamina como intervenção pertence a B3/B1 — a leva ketamina-mecanismo da §6 ficou como suporte (BAIXO), não âncora.

**B15-REGRA-05 — Interfaces sem duplicação.** Autofagia×NLRP3: B15 guarda o mecanismo autofágico, B1 o inflamassoma (Alcocer-Gómez×2, Zhang-2015, Kouba, Xia); mitofagia → B15+B8 (Brivio; Ulecia-Morón vigente); HPA → B2 (Sato, Ota, Xie como interfaces); plasticidade pura → B3; neurogênese adulta é elo condicional (B16; P16); neuroesteroides → B14.

**B15-REGRA-06 — Neurodegeneração fora do núcleo (CAMADA C).** Alzheimer/Parkinson/autismo/fragil-X como fenótipo foram EXCLUIDOS da malha (28 itens); quando a âncora do GPM usa modelo de doença neurodegenerativa (Zhang, 2023 — p62/NLRP3 em 5xFAD), o registro é de contexto mecânico compartilhado, nunca fenótipo.

**B15-REGRA-07 — Reviews e comentários = contexto.** Reviews da §6 não foram promovidas a âncora; Corona 2025 (News & Views) e revisões HPA/metabolic-interface ficaram rebaixadas.

**B15-REGRA-08 — Chave do insumo ≠ identidade do artigo; exposições desta rodada.** (i) "Pich & Millan 2018" = Cavalleri et al. 2018 (Millan sênior); (ii) "Deyama & Duman 2019" é print 2020; (iii) "Li 2021" (obesidade) é print 2022; (iv) "Sun 2021" é print 2022; (v) "Zhang 2023b" (S6K1) é print 2024; (vi) "Aguilar-Valles 2020" é print 2021; (vii) "Chandran 2012" é print 2013; (viii) o grupo Alcocer-Gómez tem DOIS artigos de 2017 — o da V1 (REF_ALCOCERGOMEZ_2017) e o agora incorporado (REF_ALCOCERGOMEZ_2017b); (ix) "Xu 2023a" é modelo de comorbidade diabetes×CUMS; (x) aliases V1↔GPM: "Zhang 2023d" (GPM) = REF_ZHANG_2023b vigente · "Li 2026a" (FKBP51) = REF_LI_2026 vigente · "Li 2025" (ApoE-complemento) = REF_LI_2025b vigente.

**B15-REGRA-09 — Anos canônicos = ano de impressão**, com sufixo de colisão por sobrenome (REF_LI_2022 vs. REF_LI_2010/2023/2025/2026; REF_ZHANG_2023c vs. REF_ZHANG_2023/2023b; REF_XU_2023b/c vs. REF_XU_2013).

**B15-REGRA-10 — Malha e lacunas [G1] declaradas.** NAO-IDX mantidos fora: Fukumoto-2020 (revista predatória), Koehl-2020 bioRxiv (substituída pela publicada), Pannu-2026 (Bentham não indexado). Lacunas [G1] que permanecem: TFEB/lisossomal em psiquiatria humana; marcador periférico de fluxo autofágico validado; mTORC2 além de astrócitos-VTA; dor×depressão como interface dedicada; envelhecimento×depressão tardia em humano (Moigneu é animal); sexo como variável; autofagia no pós-parto humano (Xie é animal); "Pich & Millan 2018" real com identificador próprio; "Choe" e "Liu-BNIP3L/NIX" do insumo sem resolução confiável.

---
"""

mk = "## TABELA DE EVIDÊNCIAS"
assert mk in doc
doc = doc.replace(mk, B14 + mk, 1)

APPEND = """---

### Nota de fecho v1 → v2 (rodada [AT 2026-09-09])
A versão anterior (v1, 134 âncoras mecanísticas sobre os 140 PMIDs validados do briefing original) foi integralmente preservada em `producao/historico/v1_canonica_2026-09-09.md`. A rodada [AT] auditou ref a ref o insumo externo do GPM B15 (49 âncoras com PMIDs; §6 com 129 itens; correções §4; lacunas §8): incorporou 39 referências novas (31 âncoras + 8 da §6) com verificação G1 completa (autor/ano/tema/abstract), registrou a leva N de suporte com decisão individual (~76 itens) e excluiu ~28 por malha CAMADA C + 2 NAO-IDX; expôs 10 divergências de identidade/ano entre rótulo do insumo e artigo real e consolidou as 10 regras canônicas no BLOCO_15. Totais da v2: **173 referências · 173 vínculos · 173 registros de auditoria**. P-6 (segunda verificação independente, avaliador cego) permanece pendente para toda a leva [AT].

---

## APÊNDICE DE REFERÊNCIAS (MÓDULO 09) — ATUALIZAÇÃO [AT 2026-09-09]

* ZHENG_2024[ML] | LUO_2021[ML] | LI_2023[ML] | XU_2023c[ML] | PENG_2024[ML] | LI_2026b[ML] | AGUILARVALLES_2021[ML] | ZHOU_2014[ML] | NEIS_2016[ML] | XU_2013[ML] | LIU_2015[ML] | CAVALLERI_2018[ML] | KOEHL_2021[ML] | DEYAMA_2020[OB] | LUSCHER_2020[OB] | CHANDRAN_2013[ML] | OTA_2014[ML] | WANG_2020[ML] | SUN_2022[ML] *
* SATO_2020[ML] | XIE_2025[ML] | FU_2024[ML] | BRIVIO_2025[ML] | MOIGNEU_2023[ML] | LING_2025[ML] | ZHANG_2024[ML] | LI_2022[ML] | XU_2023b[ML] | MARTINELLI_2021[ML] | ZHANG_2015[ML] | ALCOCERGOMEZ_2017b[EC] | ZHANG_2023c[ML] | PENG_2025[ML] | KOUBA_2022[OB] | XIA_2023[OB] | WOZNYRASALA_2025[OB] | HAN_2024[OB] | HOEFFER_2010[OB] | PAZINI_2020[ML] *
"""

patterns = {
 "REF_ZHENG_2024": "(Zheng, 2024)", "REF_LUO_2021": "(Luo, 2021)", "REF_LI_2023": "(Li, 2023)",
 "REF_XU_2023c": "(Xu, 2023)[ML].\nO p75NTR", "REF_PENG_2024": "(Peng, 2024)", "REF_LI_2026b": "(Li, 2026)",
 "REF_AGUILARVALLES_2021": "(Aguilar-Valles, 2021)", "REF_ZHOU_2014": "(Zhou, 2014)",
 "REF_NEIS_2016": "(Neis, 2016)", "REF_XU_2013": "(Xu, 2013)", "REF_LIU_2015": "(Liu, 2015)",
 "REF_CAVALLERI_2018": "(Cavalleri, 2018)", "REF_KOEHL_2021": "(Koehl, 2021)",
 "REF_DEYAMA_2020": "(Deyama & Duman, 2020)", "REF_LUSCHER_2020": "(Luscher, 2020)",
 "REF_CHANDRAN_2013": "(Chandran, 2013)", "REF_OTA_2014": "(Ota, 2014)", "REF_WANG_2020": "(Wang, 2020)",
 "REF_SUN_2022": "(Sun, 2022)", "REF_SATO_2020": "(Sato, 2020)", "REF_XIE_2025": "(Xie, 2025)",
 "REF_FU_2024": "(Fu, 2024)", "REF_BRIVIO_2025": "(Brivio, 2025)", "REF_MOIGNEU_2023": "(Moigneu, 2023)",
 "REF_LING_2025": "(Ling, 2025)", "REF_ZHANG_2024": "(Zhang, 2024)", "REF_LI_2022": "(Li, 2022)",
 "REF_XU_2023b": "(Xu, 2023)[ML].\nO estresse prepara", "REF_MARTINELLI_2021": "(Martinelli, 2021)",
 "REF_ZHANG_2015": "(Zhang, 2015)", "REF_ALCOCERGOMEZ_2017b": "(Alcocer-Gómez, 2017)",
 "REF_ZHANG_2023c": "(Zhang, 2023)[ML].\nFormononetina", "REF_PENG_2025": "(Peng, 2025)",
 "REF_KOUBA_2022": "(Kouba, 2022)", "REF_XIA_2023": "(Xia, 2023)",
 "REF_WOZNYRASALA_2025": "(Woźny-Rasała & Ogłodek, 2025)", "REF_HAN_2024": "(Han, 2024)",
 "REF_HOEFFER_2010": "(Hoeffer & Klann, 2010)", "REF_PAZINI_2020": "(Pazini, 2020)",
}
anchor_map = {}
for rid, pat in patterns.items():
    hit = None
    for line in B14.splitlines():
        if pat.split("\n")[0] in line and line.strip() and not line.strip().startswith("*"):
            hit = line.strip(); break
    assert hit, f"sem linha p/ {rid}"
    anchor_map[rid] = hit
for rid, anc in anchor_map.items():
    assert doc.count(anc) == 1, f"{rid} x{doc.count(anc)}"

mk2 = "## APÊNDICE DE REFERÊNCIAS (MÓDULO 09)"
assert mk2 in doc
doc = doc.replace(mk2, APPEND.strip() + "\n\n" + mk2.replace("## ", "## ") if False else APPEND.strip() + "\n", 1)

hits = [m.group(0) for m in re.finditer(r'\d{7,9}', doc)]
assert len(hits) == 0, f"dígitos: {hits[:5]}"

open(V2P, "w", encoding="utf-8").write(doc)
os.remove(V1P)
json.dump(anchor_map, open(os.path.join(HERE, "b15_ancoras.json"), "w"), ensure_ascii=False, indent=1)
print("V2 gravada:", V2P)
print("palavras:", len(doc.split()), "| âncoras:", len(anchor_map))
