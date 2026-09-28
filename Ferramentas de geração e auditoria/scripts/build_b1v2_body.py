#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere as novas subseções da B1 v2 (ansiedade + profundidade molecular)
na cópia da v1, no lugar correto de cada bloco. Não altera a v1."""
from pathlib import Path
SRC=Path("/home/user/pipeline_auditoria_conteudo/OFICINA_geracao/_historico/versoes/Biblioteca_B1_v1_depressao_2026-09-04.md")
DST=Path("/home/user/pipeline_auditoria_conteudo/BIBLIOTECAS/B01_Neuroinflamacao/Biblioteca_B1_NEUROINFLAMACAO_CANONICA.md")
t=SRC.read_text(encoding="utf-8")

def inserir_antes(ancora, texto_novo):
    global t
    assert ancora in t, f"âncora não achada: {ancora}"
    t=t.replace(ancora, texto_novo.strip()+"\n\n"+ancora, 1)

# ---------- BLOCO 02: imunometabolismo, necroptose, hemicanais/AQP4 ----------
inserir_antes("### 2.24 — Proteínas S100 como DAMPs",
"""### 2.25 — Imunometabolismo da micróglia: succinato/HIF-1α, glicólise e itaconato (BLOCO02.025)

A resposta inflamatória é também uma **reprogramação bioenergética**. Ao ser ativada por LPS/estresse, a micróglia troca a fosforilação oxidativa e a β-oxidação por **glicólise aeróbica** (chaveamento tipo-Warburg), necessária à produção de citocinas (Cheng et al., 2021)[ML; camundongo/célula] [PRÉ-CLÍNICO]; o perfil glicolítico no hipocampo por neuroinflamação aguda é reproduzido em rato (Vizuete et al., 2022)[ML; rato] [PRÉ-CLÍNICO]. Na quebra do ciclo de Krebs, o acúmulo de **succinato** funciona como sinal inflamatório: estabiliza **HIF-1α** (ao inibir a prolil-hidroxilase), que induz IL-1β e sustenta o fenótipo pró-inflamatório (Tannahill et al., 2013)[ML; macrófago] [EXTRAPOLADO: animal/célula→humano][EXT]. Em contraponto, a ativação inflamatória induz a enzima mitocondrial **IRG1/ACOD1**, que produz **itaconato** — freio endógeno que inibe o NLRP3 e ativa o eixo Nrf2/antioxidante (Liu et al., 2023)[OB; revisão, célula/animal] [EXTRAPOLADO: animal/célula→humano]; o eixo glicolítico/IRG1-itaconato/Nrf2 é ativamente regulado em células expostas a LPS (Engskog-Vlachos et al., 2025)[ML; célula] [PRÉ-CLÍNICO]. Natureza: causal em animal/célula; a hipótese de que insuficiência de itaconato croniciza a depressão humana é **emergente** [humano por marcador].

---

*Glicolise_microglia_2021[ML] | Succinato_HIF_2013[ML] | Itaconato_Nrf2_2023[OB] | IRG1_itaconato_2025[ML]*

### 2.26 — Necroptose: morte lítica por RIPK1–RIPK3–MLKL paralela à piroptose (BLOCO02.026)

Além da piroptose (inflamassoma/gasdermina), o SNC tem uma via de morte programada **lítica e independente de caspase**: via TNFR1 (ou outros receptores de morte), quando as caspases estão inibidas, **RIPK1–RIPK3** fosforilam **MLKL**, que transloca à membrana, forma poros e rompe a célula, liberando DAMPs. Na depressão experimental, as quinases da necroptose estão envolvidas na redução de astrócitos e nas alterações gliais induzidas por estresse crônico (Zeb et al., 2022)[ML; camundongo] [PRÉ-CLÍNICO]. Natureza: mecanística em animal; a participação direta em TDM/ansiedade humana é emergente [EXT]. Diferencia-se da piroptose pelo gatilho (TNF/RIPK vs. inflamassoma/caspase), mas ambas amplificam a liberação de DAMPs.

---

*Necroptose_dep_2022[ML]*

### 2.27 — Hemicanais astrocitários (conexina-43/panexina) e aquaporina-4 no sistema glinfático (BLOCO02.027)

A neuroinflamação também corrompe a fisiologia astrocitária de suporte. Citocinas como IL-6/IFN induzem fosforilação aberrante da **conexina-43 (Cx43)**: fecham-se as *gap junctions* que distribuem energia/glicose pela rede astrocitária e abrem-se **hemicanais**, com vazamento de ATP e glutamato para o espaço extracelular — excitotoxicidade e amplificação do sinal purinérgico. A abertura de hemicanais Cx43 em hipocampo por micróglia ativada prejudica a interação neuro-glial (Abudara et al., 2015)[ML; camundongo/célula] [PRÉ-CLÍNICO]; neuroinflamação altera as junções comunicantes de forma região-dependente (Karpuk et al., 2011)[ML; camundongo] [PRÉ-CLÍNICO]; o Cx43 astrocitário é proposto como alvo antidepressivo (Lei et al., 2023)[OB; revisão, célula/animal] [EXTRAPOLADO: animal/célula→humano]. Paralelamente, a despolarização da **aquaporina-4 (AQP4)** nos pés astrocitários desorganiza o fluxo glinfático, com acúmulo de citocinas e detritos; a disfunção glinfática no comportamento tipo-depressivo é documentada por imagem dinâmica e revertida por cetamina (Wen et al., 2024)[ML; camundongo] [PRÉ-CLÍNICO], (Lyu et al., 2025)[ML; camundongo] [PRÉ-CLÍNICO]. Natureza: mecanística em animal; humano por marcador [EXT].

---

*Cx43_hemicanal_2015[ML] | Cx43_GJ_2011[ML] | Cx43_antidep_2023[OB] | AQP4_glinfatica_2024[ML] | Glinfatica_RM_2025[ML]*""")

# ---------- BLOCO 03/04: amígdala/medo/ansiedade ----------
inserir_antes("### 3.15 — Inventário NEGATIVO de mediadores",
"""### 3.16 — Neuroimunologia da ansiedade: amígdala, IL-18 local, P2X7/Na⁺-K⁺-ATPase e NLRP3 (BLOCO03.016)

A ansiedade tem nós moleculares próprios, centrados na **amígdala basolateral (BLA)** e na extinção do medo. Citocinas pró e anti-inflamatórias modulam bidirecionalmente os circuitos da amígdala reguladores do medo/ansiedade (Lee et al., 2025)[OB/ML; revisão+experimento] [VERIFICADO]. Um sistema local de **IL-18 na BLA** regula a suscetibilidade ao estresse crônico (Kim TK et al., 2017)[ML; camundongo] [PRÉ-CLÍNICO]. Na micróglia, a ruptura do complexo **Na⁺/K⁺-ATPase–P2X7** promove o comportamento tipo-ansiedade (Huang S et al., 2024)[ML; camundongo] [PRÉ-CLÍNICO]. O inflamassoma na ansiedade tem direção **não monotônica**: a deficiência de **TET2** (que desreprime metilação) ativa NLRP3/IL-1β e induz ansiedade/depressão (Gao et al., 2023)[ML; camundongo] [PRÉ-CLÍNICO], mas a própria **deficiência de NLRP3** também provoca disfunção hipocampal e comportamento tipo-ansiedade (Komleva et al., 2021)[ML; camundongo] [PRÉ-CLÍNICO] — aviso contra leituras unidirecionais do inflamassoma. Natureza: causal em animal; humano por marcador/imagem [EXT].

---

*Amigdala_citocinas_2025[OB] | IL18_amigdala_2017[ML] | P2X7_NaK_ansiedade_2024[ML] | TET2_NLRP3_2023[ML] | NLRP3_def_ansiedade_2021[ML]*""")

# ---------- BLOCO 06: tradução clínica da ansiedade (antes do BLOCO_07) ----------
inserir_antes("## BLOCO_07 — NÓS MOLECULARES CENTRAIS",
"""### 6.6 — Ansiedade e estresse traumático: meta-evidência e o subtipo TEPT neuroimune suprimido (BLOCO06.006)

A tradução clínica da neuroinflamação **não é exclusiva da depressão**. Meta-análises específicas mostram associação transdiagnóstica de marcadores inflamatórios periféricos com ansiedade, estresse traumático e TOC (Renna et al., 2018)[MA; humano] [VERIFICADO]; a meta-análise de citocinas periféricas em transtornos de ansiedade confirma elevações em subgrupos (Costello et al., 2019)[MA; humano] [VERIFICADO]. Por transtorno: TOC (Cosco et al., 2019)[MA; humano] [VERIFICADO], transtorno de pânico (Quagliato et al., 2018)[OB; revisão sistemática] [VERIFICADO], e TEPT (Passos et al., 2015)[MA; humano] [VERIFICADO].

**Contra-padrão decisivo:** o TEPT não é uniformemente "inflamação alta". Estudo combinando **PET de TSPO e tecido pós-morte** encontra **supressão neuroimune** (sinal glial reduzido) em subgrupo de TEPT (Bhatt et al., 2020)[EC; humano, PET+pós-morte] [VERIFICADO] — paralelo ao hipocortisolismo da B2; o TSPO como alvo em doenças relacionadas ao estresse é revisado (Rupprecht et al., 2022)[OB; revisão] [VERIFICADO]. Em crianças/adolescentes, transtornos internalizantes de base ansiosa também apresentam alterações inflamatórias (Parsons et al., 2021)[OB; revisão sistemática] e citocinas alteradas (Howe et al., 2022)[MA; humano] [VERIFICADO]. A via imuno-quinurenina está implicada nos transtornos de ansiedade (Kim YK et al., 2018)[OB; revisão, humano] [VERIFICADO]. Natureza: associativo em humano; o subtipo suprimido exige não tratar "inflamação alta" como universal.

---

*Renna_ansiedade_2018[MA] | Costello_ansiedade_2019[MA] | TOC_imune_2019[MA] | Panico_citocinas_2018[OB] | PTSD_marc_2015[MA] | PTSD_supressao_2020[EC] | TSPO_estresse_2022[OB] | Ansiedade_ped_2021[OB] | Internalizante_ped_2022[MA] | Quinur_ansiedade_2018[OB]*

### 6.7 — Tradução anti-inflamatória na ansiedade: medo/extinção e ensaios (descrever o estudo; P20) (BLOCO06.007)

Há tradução terapêutica mensurável na ansiedade. **Minociclina atenua a retenção de memória de medo em humanos** em ensaio randomizado placebo-controlado (Xia et al., 2024)[EC; humano, RCT] [VERIFICADO] — e reverte o prejuízo de extinção do medo induzido por IFN-α em rato (Bi et al., 2016)[ML; rato] [PRÉ-CLÍNICO]. A mega-análise de fármacos imunomoduladores em sintomas psiquiátricos (incluindo ansiedade) mostra efeito pequeno mas significativo (Wittenberg et al., 2020)[MA; mega-análise de RCT] [VERIFICADO]. Ômega-3 (LCPUFA) associa-se a redução de sintomas de ansiedade (Su et al., 2018)[MA; humano, JAMA Netw Open] [VERIFICADO]. Estes são achados de **estudo**, não recomendação de conduta (doses/posologia pertencem ao módulo operacional, não a esta biblioteca). Natureza: intervencionista em humano (minociclina/ômega/imunomoduladores) com heterogeneidade; a qualidade da evidência é variável.

---

*Minociclina_medo_2024[EC] | Minociclina_extincao_2016[ML] | Mega_imunomod_2020[MA] | Omega3_ansiedade_2018[MA]*""")

DST.write_text(t, encoding="utf-8")
print("inserções aplicadas. Novo total de linhas:", t.count(chr(10))+1)
print("H3 agora:", t.count("### "))
