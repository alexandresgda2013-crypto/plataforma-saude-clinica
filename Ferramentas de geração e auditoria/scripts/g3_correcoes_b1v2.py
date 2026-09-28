#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Correções G3 da B1 v2: ajustar a linguagem ao que o abstract realmente diz."""
from pathlib import Path
P=Path("/home/user/pipeline_auditoria_conteudo/BIBLIOTECAS/B01_Neuroinflamacao/Biblioteca_B1_NEUROINFLAMACAO_CANONICA.md")
t=P.read_text(encoding="utf-8")
def sub(velho,novo):
    global t
    c=t.count(velho)
    assert c==1, f"{c}x: {velho[:70]}"
    t=t.replace(velho,novo)

# 3.16 — Lee 2025: é IL-17A/C ansiogênico vs IL-10 ansiolítico em camundongo (não "citocinas" genérico; não VERIFICADO humano)
sub("Citocinas pró e anti-inflamatórias modulam bidirecionalmente os circuitos da amígdala reguladores do medo/ansiedade (Lee et al., 2025)[OB/ML; revisão+experimento] [VERIFICADO].",
    "Em camundongo, **IL-17A/IL-17C** na amígdala basolateral aumentam a excitabilidade neuronal e induzem comportamento ansiogênico, ao passo que a citocina anti-inflamatória **IL-10**, sobre a mesma população neuronal, tem efeito oposto — modulação bidirecional do circuito do medo/ansiedade por citocinas (Lee et al., 2025)[ML; camundongo] [PRÉ-CLÍNICO].")

# 6.6 — reescrever para refletir direção/força reais
sub("A tradução clínica da neuroinflamação **não é exclusiva da depressão**. Meta-análises específicas mostram associação transdiagnóstica de marcadores inflamatórios periféricos com ansiedade, estresse traumático e TOC (Renna et al., 2018)[MA; humano] [VERIFICADO]; a meta-análise de citocinas periféricas em transtornos de ansiedade confirma elevações em subgrupos (Costello et al., 2019)[MA; humano] [VERIFICADO]. Por transtorno: TOC (Cosco et al., 2019)[MA; humano] [VERIFICADO], transtorno de pânico (Quagliato et al., 2018)[OB; revisão sistemática] [VERIFICADO], e TEPT (Passos et al., 2015)[MA; humano] [VERIFICADO].",
    "A tradução clínica da neuroinflamação **não é exclusiva da depressão**, mas a evidência por transtorno de ansiedade é **heterogênea e de tamanho de efeito pequeno**. Uma meta-análise transdiagnóstica encontra diferença significativa (porém modesta, Hedge's g≈0,4) nas citocinas pró-inflamatórias entre indivíduos com ansiedade/TEPT/TOC e controles, com o efeito moderado por comorbidade depressiva (Renna et al., 2018)[MA; humano] [VERIFICADO]; a meta-análise dedicada ao transtorno de ansiedade generalizada (14 estudos) encontra alterações periféricas com heterogeneidade (Costello et al., 2019)[MA; humano] [VERIFICADO]. Por transtorno, o quadro é **misto, não universal**: no **TOC**, as citocinas (TNF-α, IL-6, IL-1β, IL-4, IL-10, IFN-γ) **não diferiram significativamente** dos controles na meta-análise, que reporta resultados inconsistentes (Cosco et al., 2019)[MA; humano] [VERIFICADO] — um achado nulo relevante; no **pânico**, uma revisão sistemática narrativa (não meta-análise) relata elevação de IL-6/IL-1β em parte dos estudos, com conflitos para outras citocinas (Quagliato et al., 2018)[OB; revisão sistemática]; no **TEPT**, a meta-análise confirma marcadores periféricos elevados (Passos et al., 2015)[MA; humano] [VERIFICADO].")

sub("Em crianças/adolescentes, transtornos internalizantes de base ansiosa também apresentam alterações inflamatórias (Parsons et al., 2021)[OB; revisão sistemática] e citocinas alteradas (Howe et al., 2022)[MA; humano] [VERIFICADO].",
    "Em crianças/adolescentes, a revisão sistemática de transtornos de base ansiosa encontra uma associação combinada que **se aproxima da significância** mas permanece inconsistente entre estudos (Parsons et al., 2021)[OB; revisão sistemática], e a meta-análise exploratória de internalizantes pediátricos reporta alterações de citocinas dependentes de moderadores (Howe et al., 2022)[MA; humano] [VERIFICADO].")

# 6.7 — minociclina em saudáveis; Wittenberg mede sintomas depressivos
sub("Há tradução terapêutica mensurável na ansiedade. **Minociclina atenua a retenção de memória de medo em humanos** em ensaio randomizado placebo-controlado (Xia et al., 2024)[EC; humano, RCT] [VERIFICADO] — e reverte o prejuízo de extinção do medo induzido por IFN-α em rato (Bi et al., 2016)[ML; rato] [PRÉ-CLÍNICO]. A mega-análise de fármacos imunomoduladores em sintomas psiquiátricos (incluindo ansiedade) mostra efeito pequeno mas significativo (Wittenberg et al., 2020)[MA; mega-análise de RCT] [VERIFICADO].",
    "Há tradução experimental em mecanismo de medo/ansiedade. **Minociclina atenua a retenção de memória de medo em voluntários saudáveis** em ensaio randomizado placebo-controlado (N=105, condicionamento de medo) (Xia et al., 2024)[EC; humano, RCT em saudáveis] [VERIFICADO] — evidência de modulabilidade farmacológica da memória do medo, **não** teste do fármaco em pacientes com transtorno de ansiedade; em rato, reverte o prejuízo de extinção do medo induzido por IFN-α (Bi et al., 2016)[ML; rato] [PRÉ-CLÍNICO]. Uma mega-análise de 18 RCTs de fármacos imunomoduladores (N=10.743, nove doenças) mostra benefício para **sintomas depressivos/psicológicos** (SF-36/HADS), restrito ao estrato com sintomas basais altos — prova de conceito imunomodulador, não específica de ansiedade (Wittenberg et al., 2020)[MA; mega-análise de RCT] [VERIFICADO].")

P.write_text(t,encoding="utf-8")
print("correções G3 aplicadas à prosa")

# Ajustar JSON: itaconato é mecanístico pré-clínico (não human_clinical)
import json
F=Path("/home/user/pipeline_auditoria_conteudo/BIBLIOTECAS/B01_Neuroinflamacao/Evidencias/Bibliografia/01_pmids.json")
d=json.load(open(F,encoding="utf-8"))
for it in d:
    if it.get("ids_referencia_interna")==["REF_Itaconato_Nrf2_2023"]:
        it["evid_role"]="preclinical_mechanistic"
        it["extrapolacao_por_analogia"]="sim (revisao de mecanistica/discovery em celula/animal -> humano)"
json.dump(d,open(F,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("JSON: itaconato reclassificado")
