# GERADOR DE PROFUNDIDADE MOLECULAR (GPM) — PARTE 1
## Mecanismo: B10 — Desregulação Circadiana (Ritmos / Sono / Luz) em Ansiedade e Depressão
### (Módulos 00–05 · Parte 2 = Módulos 06–10, a gerar após liberação)

> Geração conforme **Molde GPM v2.0**. Citações no corpo em **(Autor, Ano)**; ao fim de cada
> item, origem da evidência **+ natureza da relação + maturidade**; ao fim de cada módulo, âncora
> `[REF_MODULO_XX: Autor_Ano | ...]`. Os **PMIDs verificados** permanecem no **Briefing B10
> consolidado** (15 blocos A–O, 177 âncoras, G1 por eutils/PubMed + auditoria de insumos +
> Consensus + varredura OpenAlex) e são a chave de rastreabilidade para o G1→G2→G3 da Rodada 2 —
> o GPM **aponta território**, não substitui a verificação. **Sem medicamentos/suplementos/
> intervenções como conteúdo** (proibição do molde): luz, melatonina, *wake therapy*, IPSRT,
> agomelatina, exercício-cronoterapia entram apenas como **sinal interventivo/experimental**,
> nunca como prescrição; vivem no Briefing e entram na Biblioteca via Prompt 4.2.
>
> **Regra fundadora deste mecanismo: *timing* ≠ *estado*.** O sistema circadiano é uma **rede
> temporal** (fase, amplitude, período, estabilidade, sincronização); o **sono é um *output* dessa
> rede, não o mecanismo**. Insônia, dormir pouco/tarde, sonolência e *jet lag* podem refletir
> desregulação circadiana, mas não são sinônimos dela. O GPM separa **distúrbio do *timing***
> (fase/amplitude/estabilidade/desacoplamento) de **distúrbio do *estado* do sono (insônia)**.

---

## MÓDULO 00 — METADADOS E ESCOPO

- **ID do mecanismo:** B10 — Desregulação Circadiana e Sono (ritmos biológicos, sincronização
  fótica e não-fótica, arquitetura temporal do humor).
- **Condições em escopo:** Transtorno Depressivo Maior (TDM), Depressão Resistente ao Tratamento,
  Distimia, Transtorno de Ansiedade Generalizada, Transtorno do Pânico, Transtorno de Ansiedade
  Social, TEPT (quando tratado no espectro trauma/ansiedade). O **transtorno bipolar** entra como
  condição-irmã com evidência mecanística **mais forte** (é a "doença-relógio" paradigmática) —
  sempre sinalizado como bipolar, **nunca fundido** à TDM; a sazonalidade/SAD e os transtornos do
  ritmo sono-vigília (DSWPD/ASWPD) entram como fenótipos circadianos nucleares.
- **Corte de conhecimento:** busca em tempo real **executada em 2026-09-06** via PubMed/eutils
  (esearch/esummary, com backoff), leitura da análise do Consensus.app (20 artigos lidos pelo
  agente; 3 queries exatas do motor extraídas do `agent_trace`), reprodução dessas queries no
  PubMed (bloco M) e no **OpenAlex** (bloco O, corpus aberto), e quatro insumos auditados
  (pré-caça + insumo A de 37 âncoras + insumo B de 11 + Consensus). O GPM reflete literatura até
  essa data.
- **Observação de escopo:** a regra de delimitação por doença foi aplicada item a item. A **biologia
  circadiana fundamental** (TTFL, SCN, melanopsina, melatonina) entra como base universal, sem
  exigir contexto de doença. Achados em **outra condição** (esquizofrenia, câncer/turno, obesidade,
  Alzheimer, autismo, TDAH) entram no corpo só quando há estudo-ponte para humor/ansiedade,
  sinalizados `[EXTRAPOLAÇÃO POR ANALOGIA]`; os sem ponte vão para o Módulo 10. Dados de **tecido
  periférico/sanguíneo** (PBMC, fibroblastos, actigrafia de punho) entram com rótulo explícito de
  **periférico/marcador (≠ relógio neuronal)**.

**Propósito deste GPM (nota de direção de atenção):** o tema "circadiano" seduz o levantamento
genérico a parar no óbvio — "dormir mal deprime", "melatonina dá sono", "luz faz bem" — e a
colapsar *ritmo* em *sono*. Os pontos cegos que este documento deve trazer à tona são: (i) a
**maquinaria molecular do relógio** como laço transcricional (TTFL) com genes/quinases específicos
(BMAL1/CLOCK/NPAS2, PER1–3/CRY1/2, REV-ERBα/β–ROR, CK1δ/ε, FBXL3, TIMELESS, DEC1/2) e sua
integração metabólica (NAD⁺/SIRT1, AMPK, mTOR, GSK3β, PPARs, nocturnina); (ii) a **hierarquia
SCN → relógios locais**, com os relógios de PFC/hipocampo/amígdala/VNAc/estriado podendo
**desacoplar** sob estresse (mPFC ≠ SCN); (iii) a **entrada fótica** por ipRGC/melanopsina (Opn4)
distinta da visão e a **curva de resposta de fase à luz** (o efeito depende do *horário*, não da
"dose"); (iv) os **quatro parâmetros** fase/DLMO, amplitude/MESOR, estabilidade (IS/IV) e período —
e a **heterogeneidade de fase** (não existe "depressão = relógio atrasado"; há avanço, atraso e
desalinhamento fase↔sono); (v) a **assimetria de evidência**: prova causal limpa em animal
(mutante *Clock* tipo-mania bloqueado por lítio; KD de *Bmal1* no SCN) versus evidência humana
majoritariamente **associativa/preditiva**, com a randomização Mendeliana de cronotipo como a
exceção causal; (vi) **ansiedade com lastro próprio** (não só "via insônia"); e (vii) o
**inventário negativo** — não há biomarcador circadiano único validado para diagnóstico, e os
estudos de associação de genes-relógio em humano são fracos/heterogêneos. O GPM cobre
**mecanismo**; **não cobre terapia** (luz/melatonina/*wake therapy*/IPSRT/agomelatina são sinal,
não conduta).

[REF_MODULO_00: Briefing_B10_2026 | Molde_GPM_v2.0 | Roenneberg_2003 | Takahashi_2017 | Geoffroy_2025]

---

## MÓDULO 01 — MAPA EXAUSTIVO DE VIAS MOLECULARES

### Via 1 — Laço transcricional-traducional (TTFL): o relógio molecular núcleo
- **Sequência:** os heterodímeros **BMAL1 (ARNTL)/CLOCK** (ou **BMAL1/NPAS2** em tecido neural)
  ligam-se a **E-box** (CACGTG) e ativam a transcrição de **PER1/2/3** e **CRY1/2**; as proteínas
  PER/CRY acumulam-se, heterodimerizam, translocam ao núcleo e **inibem o próprio complexo
  BMAL1/CLOCK** (laço de retroalimentação negativa, ~24 h). A degradação de PER/CRY por
  **CK1δ/ε (CSNK1D/E)** (fosforilação) e pelo complexo **FBXL3/FBXL2** (ubiquitinação) alivia a
  inibição e reinicia o ciclo. Laço de revisão: **REV-ERBα/β (NR1D1/2)** reprimem e **RORα/β/γ
  (RORA/B/G)** ativam *BMAL1* via **RORE**. Saídas rítmicas: **DBP/TEF/HLF** (PAR-bZIP), **DEC1/2
  (BHLHE40/41)** e **TIMELESS**; **AANAT** (síntese de melatonina) é saída pineal rítmica.
- **Papel em ansiedade/depressão:** é a base universal do relógio. O KD estereotáxico de **Bmal1
  no SCN** (neurônios intactos) produz desamparo aprendido, desespero comportamental e ansiedade,
  com padrão anormal de corticosterona (Landgraf et al., 2016) [animal; **causal**; muito
  estabelecido como prova de conceito]. A disfunção do SCN induz fenótipo ansioso/depressivo via
  **ativação do eixo BDNF–TrkB no estriado**, reversível por bloqueio (Liang et al., 2025)
  [animal; causal/mediacional; emergente-maduro — ponte com B3]. O mutante **ClockΔ19** exibe
  comportamento tipo-mania (hiperatividade, sono reduzido, recompensa) (Roybal et al., 2007)
  [animal; causal; bem suportado]. Deficiência de **Rev-erbα** induz comportamento tipo-humor
  (Otsuka et al., 2022) e alvejamento farmacológico do relógio altera sono/emoção (Banerjee et al.,
  2014) [animal; causal; moderadamente suportado]. Revisões da arquitetura: Takahashi 2017; Mohawk,
  Green & Takahashi 2012; Lowrey & Takahashi 2011 [biologia básica; fundamento; muito
  estabelecido].
- **Convergência/divergência:** é o nó que recebe os demais laços (luz Via 2, melatonina Via 3,
  metabolismo Via 6). Diverge da noção de "um relógio central único": o TTFL roda em **quase todas
  as células**, e o SCN é o **maestro/sincronizador**, não o único relógio.

### Via 2 — Entrada fótica: ipRGC/melanopsina → trato retino-hipotalâmico (RHT) → SCN
- **Sequência:** células ganglionares retinianas **intrinsecamente fotossensíveis (ipRGC)**
  expressam **melanopsina (OPN4)** e respondem à luz mesmo sem bastonetes/cones; projetam via
  **trato retino-hipotalâmico (RHT)** ao SCN (glutamato + PACAP), sincronizando o relógio-mestre.
  A via da luz que afeta humor/aprendizado **diverge da via da imagem** (Fernandez et al., 2018).
- **Papel em ansiedade/depressão:** a luz no **horário biológico** determina a resposta — a
  **curva de resposta de fase (PRC)** mostra que luz matinal **avança** e luz noturna **atrasa** a
  fase, e luz noturna **suprime melatonina** (Khalsa et al., 2003; St Hilaire et al., 2012; Gooley
  et al., 2011) [humano/fisiologia; mecanístico; muito estabelecido]. O *timing* da luz modula
  humor e circuitos límbicos (Bedrosian & Nelson, 2017). Em animal, **luz constante crônica**
  (Tapia-Osorio et al., 2013) e **luz no meio da noite** (Ikeno et al., 2016) induzem
  ansiedade/depressão; **menor iluminação diurna** produz ansiedade com alteração do HPA (dado
  animal, 2016 — autor a confirmar no G2) e **luz fraca noturna no pós-parto** induz fenótipo
  depressivo (dado animal, 2025 — autor a confirmar no G2) [animal; causal/ambiental; bem
  suportado]. **O efeito da luz = intensidade × duração × espectro × horário circadiano ×
  sensibilidade individual** — "mais luz" não é "melhor".
- **Fase temporal:** atua na **sincronização** (arrasto) continuamente; o desalinhamento crônico
  (turno, *jet lag*, luz noturna) é a exposição patológica.

### Via 3 — Saída endócrina temporal: melatonina pineal e o marcador DLMO
- **Sequência:** noite biológica → SCN via paraventricular/simpática → pineal → **AANAT** →
  **melatonina** (sinal químico de noite). O **início da melatonina em luz fraca (DLMO)** é o
  marcador canônico de **fase**. A melatonina sinaliza de volta via receptores **MT1/MT2
  (MTNR1A/B)** no SCN e alhures; a **agomelatina** (MT1/MT2 + 5-HT2C) é fármaco, não
  suplemento.
- **Papel em ansiedade/depressão:** o **DLMO** é usado para definir fase; achado-chave — **DLMO
  avançado em relação ao sono** em mulheres jovens com TDM não medicado, i.e., **desalinhamento
  fase↔sono**, não atraso simples (Coleman et al., 2019) [humano; marcador/mecanístico; bem
  suportado]. As relações de fase temperatura/melatonina/sono associam-se à gravidade (Hasler et
  al., 2010; Buckley et al., 2010). Variantes da via da melatonina no bipolar (Etain et al., 2012)
  [humano/genética; associativo; moderadamente suportado]. Em intervenção translacional (sinal, não
  prescrição), agonista melatonérgico normaliza genes clock + citocinas + neurotrofinas em
  deprimidos/ansiosos com insônia (Satyanarayanan et al., 2020) [humano/intervenção; contributivo;
  emergente].
- **Natureza:** melatonina é **marcador de fase e saída** rítmica; tratá-la como "hormônio do
  sono" ou antidepressivo é extrapolação (ver Módulo 08).

### Via 4 — Relógios locais extra-SCN e o desacoplamento sob estresse
- **Sequência:** o TTFL opera em **neurônios e glia de todo o cérebro** (PFC/mPFC, hipocampo,
  amígdala, estriado, VTA, núcleo accumbens/NAc, hipotálamo) e em periferia (fígado, músculo,
  adiposo, intestino, imune). O SCN os **arrasta**; sob estresse, alimentação ou luz errante,
  relógios locais podem **dessincronizar** do SCN e entre si.
- **Papel em ansiedade/depressão:** os relógios do **NAc** regulam ansiedade de forma
  gene-dependente e **oposta**: KD de **Per1/Per2** no NAc **aumenta** ansiedade, enquanto KD de
  **Npas2** a **reduz** (Meyer et al., 2024) [animal; causal/manipulativo; emergente-maduro]. O
  **relógio molecular do mPFC** (não do SCN) medeia o efeito antidepressivo da privação de sono
  (Gardner et al., 2026) e esse efeito requer **sinalização de adenosina dependente de astrócito**
  (Hines et al., 2013) [animal; causal/mediacional; emergente — mPFC ≠ SCN]. Estresse crônico
  altera ritmos moleculares regionais (Logan et al., 2015); a relação relógio↔neurotransmissão é
  **bidirecional** e os relógios límbicos desacoplam sob estresse (Wang et al., 2026; revisões
  Francis & Porcu, 2023; Dollish et al., 2023; Vadnie & McClung, 2017; Ketchesin et al., 2020)
  [animal + revisão; contributivo/associativo; bem suportado e emergente].
- **Divergência:** esta via **revoga** o modelo "SCN-ditador": a patologia pode residir no
  **desacoplamento de relógios locais** com SCN intacto (subtipo F do Módulo 07).

### Via 5 — Saídas rítmicas que modulam humor: HPA, monoaminas, temperatura, imunidade, plasticidade
- **Sequência:** o relógio "gativa" ritmos fisiológicos — pulso de **cortisol** matinal e
  **resposta ao despertar (CAR)** e slope diurno; ritmos de **dopamina/serotonina/norepinefrina**;
  **temperatura corporal central**; **imunidade** (citocinas rítmicas); e **plasticidade**
  (BDNF/CREB/GSK3β/mTOR/MAPK rítmicos).
- **Papel em ansiedade/depressão:** na TDM o sinal objetivo mais replicado é **amplitude
  reduzida** — achatamento de temperatura, cortisol, NE, TSH e melatonina (Souêtre et al., 1989)
  [humano/clássico; marcador; bem suportado] e, em meta de actigrafia (53 estudos/~11 mil), menor
  MESOR/amplitude/estabilidade e atividade diurna (Ho et al., 2024) [meta/humano; marcador; bem
  suportado]. O **ritmo de IL-6 diurno achatado** associa-se à regulação emocional da amígdala
  (dado humano, 2023 — autor a confirmar no G2) e a depressão major eleva IL-6 plasmático
  diurno (Alesci et al., 2005) [humano; associativo/marcador; moderadamente suportado — B1]. O
  **5-HT é elo comum** relógio–estresse–humor (Daut & Fonken, 2019) e a dopamina/recompensa é
  ritmicamente regulada (Kim et al., 2017) [revisão/animal; contributivo; bem suportado — B4].
  **NPAS2 regula ansiedade e receptores GABA-A** (Ozburn et al., 2017) [animal; causal; bem
  suportado — B5]. O BDNF/TrkB estriatal rítmico media o fenótipo da disfunção do SCN (Liang et
  al., 2025) [animal; causal/mediacional; emergente — B3].
- **Natureza:** majoritariamente **saídas/marcadores** rítmicos; a direção causal (relógio→saída
  vs. doença→achatamento) é bidirecional (Módulo 08).

### Via 6 — Integração metabólica do relógio e relógios periféricos
- **Sequência:** o TTFL conversa com **NAD⁺/SIRT1**, **AMPK**, **mTOR**, **GSK3β**, **PPARs** e
  **nocturnina**; relógios de fígado/adiposo/intestino são arrastados por **alimentação** e
  **glicocorticoides** (Pezük et al., 2012); o horário da refeição é um *zeitgeber* não-fótico.
- **Papel em ansiedade/depressão:** o **GSK3β** é nó que liga relógio e resposta ao **lítio** no
  bipolar (SNP do promotor de GSK3β; Benedetti et al., 2004) e a via **REV-ERBα/NR1D1** liga
  relógio e lítio (McCarthy et al., 2011) [humano/genética bipolar; associativo; bem suportado].
  A desregulação circadiana, clock genes e metabolismo convergem (Schrader et al., 2024) e o
  **horário da ingestão energética (crononutrição)** associa-se a sintomas depressivos (dado
  humano, 2025 — autor a confirmar no G2) [revisão/humano; contributivo/associativo; emergente —
  B8/B9]. Antidepressivos de ação rápida (cetamina) e cronoterapia compartilham clock genes/
  GSK3β/mTOR/MAPK/plasticidade (Sato et al., 2022) [revisão; mecanístico; moderadamente
  suportado].
- **Fase temporal:** arrasto **metabólico** contínuo; o desalinhamento alimentar (comer à noite)
  desacopla relógios periféricos do SCN.

### Via 7 — Hierarquia social/comportamental e zeitgebers não-fóticos
- **Sequência:** além da luz, **refeição, atividade física, temperatura e ritmos sociais**
  sincronizam o sistema. A teoria dos **zeitgebers sociais** (Ehlers, Frank & Kupfer, 1988)
  sustenta que a desestabilização dos hábitos sociais desorganiza os ritmos biológicos; base da
  **IPSRT** (sinal psicoterápico ancorado em Frank et al., 2005, não prescrição farmacológica).
- **Papel em ansiedade/depressão:** a desruptura de ritmo social precede episódios bipolar/
  unipolar (Malkoff-Schwartz et al., 2000); ritmo social perturbado na depressão (Szuba et al.,
  1992) e na ansiedade (Shear et al., 1994); ritmos sociais regulares ligam-se a sono/humor/
  ansiedade (Sabet et al., 2021) [humano/observacional; associativo/preditivo; bem suportado]. O
  **jet lag social** (diferença entre dia de trabalho e dia livre; Roenneberg et al., 2012)
  associa-se a depressão/ansiedade, inclusive em adolescentes (Gao et al., 2025; Sun et al., 2025;
  Lu et al., 2026; Ravenhall et al., 2026) [meta/RS; associativo; bem suportado]. O **exercício**
  atua como *zeitgeber* comportamental (He et al., 2025; dado animal 2015) [animal; interventivo-
  experimental; emergente].

> **Autoauditoria do Módulo 01:** as vias 1–3 e 5 têm lastro muito estabelecido (TTFL, luz/PRC,
> melatonina/DLMO, achatamento de amplitude). As vias 4 (desacoplamento de relógios locais, NAc
> Per1/2 vs Npas2, mPFC) e 6 (integração metabólica/crononutrição) são as camadas **emergentes**
> que um levantamento genérico perderia — estão marcadas como tal. Três alegações animais
> (iluminação diurna 2016; luz fraca pós-parto 2025) e duas humanas (IL-6/amígdala 2023;
> crononutrição 2025) têm o **primeiro autor a confirmar no G2** (PMID no Briefing); o fato e o
> periódico estão pinados, não se inventou nome. Nenhuma via de intervenção (luz/melatonina/wake
> therapy/IPSRT/agomelatina) é apresentada como conduta — apenas como sinal experimental.

[REF_MODULO_01: Takahashi_2017 | Mohawk_2012 | Landgraf_2016 | Liang_2025 | Roybal_2007 |
Hattar_2002 | Khalsa_2003 | Fernandez_2018 | Tapia-Osorio_2013 | Coleman_2019 | Meyer_2024 |
Gardner_2026 | Hines_2013 | Wang_2026 | Souêtre_1989 | Ho_2024 | Daut_Fonken_2019 | Ozburn_2017 |
Pezük_2012 | Schrader_2024 | Ehlers_1988 | Roenneberg_2012]

---

## MÓDULO 02 — MAPA EXAUSTIVO DE MEDIADORES MOLECULARES

*Categorias adaptadas à natureza temporal do mecanismo (não são as categorias imunológicas do
molde).*

### 2.1 Componentes do relógio molecular (proteínas/genes do TTFL)
- **BMAL1/ARNTL** — braço ativador; KD no SCN → fenótipo depressivo/ansioso (Landgraf et al.,
  2016) [animal; causal; bem suportado]. **CLOCK** e **NPAS2** — parceiros de BMAL1; NPAS2 neural
  regula ansiedade/GABA-A (Ozburn et al., 2017) e no NAc reduz ansiedade (Meyer et al., 2024)
  [animal; causal; moderadamente suportado]. **PER1–3 / CRY1/2** — braço repressor; no NAc,
  Per1/Per2 ↑ansiedade (Meyer et al., 2024) [animal; causal; emergente]. **REV-ERBα/β (NR1D1/2)**
  e **RORα/β/γ (RORA)** — laço de revisão de BMAL1; Rev-erbα liga-se ao lítio/bipolar (McCarthy
  et al., 2011; Otsuka et al., 2022) [humano+animal; associativo/causal; moderadamente
  suportado]. **CK1δ/ε (CSNK1D/E)** — fosforila/degrada PER; alvo de fármacos cronobióticos
  (sinal) [básico; mecanístico; muito estabelecido]. **FBXL3/FBXL2** — ubiquitinação de CRY;
  **TIMELESS**, **DEC1/2 (BHLHE40/41)** — saídas/moduladores; **DBP/TEF/HLF** — PAR-bZIP de saída
  [básico; mecanístico; bem estabelecido].
- Natureza: componentes de **maquinaria** (causal em animal; variantes humanas de efeito pequeno
  — ver Módulo 04).

### 2.2 Sinais hormonais temporais (saídas endócrinas)
- **Melatonina / AANAT** — sinal de noite; DLMO = marcador de fase (não "hormônio do sono")
  [humano; marcador; muito estabelecido]. **Cortisol, CAR e slope diurno** — saída HPA rítmica;
  slope diurno mais plano associa-se a pior saúde mental (Adam et al., 2017; consenso de método
  Stalder et al., 2022/2025) [meta/consenso; marcador; bem suportado]. **Temperatura corporal
  central** — saída rítmica achatada na depressão (Souêtre et al., 1989) [humano; marcador; bem
  suportado]. **TSH** — ritmo achatado (Souêtre) [humano; marcador; moderadamente suportado].

### 2.3 Neurotransmissão e neuropeptídeos rítmicos
- **Dopamina** (recompensa/VTA-NAc; Kim et al., 2017), **serotonina/5-HT** (elo relógio–estresse;
  Daut & Fonken, 2019), **norepinefrina** (ritmo achatado; Souêtre), **glutamato/GABA**
  (NPAS2→GABA-A; Ozburn et al., 2017; Wang et al., 2026) [animal+revisão; contributivo; bem
  suportado]. **Orexina/hypocretina** — neuromodulador de vigília/arousal com implicações
  cronopatológicas em sono/psiquiatria, **inclusive TEPT** (revisão, 2018 — autor a confirmar no
  G2) [revisão; hipótese mecanística/emergente; fronteira — B13/B12]. **Adenosina** — marcador da
  pressão homeostática do sono (Processo S de Borbély); media o efeito da privação de sono via
  astrócito (Hines et al., 2013) [animal; causal/mediacional; emergente].

### 2.4 Plasticidade e sinalização intracelular rítmicas
- **BDNF/TrkB** (mediação estriatal do fenótipo SCN; Liang et al., 2025), **CREB**, **GSK3β**
  (nó do lítio; Benedetti et al., 2004), **mTOR/MAPK** (antidepressivos rápidos × relógio; Sato et
  al., 2022) [animal+humano; mediacional/associativo; emergente a bem suportado — B3].

### 2.5 Mediadores imunes/metabólicos rítmicos (periféricos e centrais)
- **IL-6** (ritmo diurno achatado ↔ amígdala; 2023; e elevação diurna na TDM; Alesci et al.,
  2005), **TNF/IL-1β** rítmicos (revisões de imunidade circadiana; Zeng et al., 2024) [humano+
  revisão; associativo/marcador; moderadamente suportado — B1]. **NAD⁺/SIRT1, AMPK, PPARs,
  nocturnina** — integração relógio–metabolismo (Schrader et al., 2024) [revisão; mecanístico;
  emergente — B9/B8]. **Microbiota rítmica** e eixo intestino–cérebro–circadiano (Bautista et al.,
  2025; Li et al., 2018) [revisão; hipótese/contributivo; emergente — B7].

### 2.6 INVENTÁRIO NEGATIVO (subseção obrigatória)
Mediadores/parâmetros **repetidamente investigados sem associação consistente** ou **sem
validação** em ansiedade/depressão:
- **Nenhum biomarcador circadiano único** (gene, hormônio ou medida actigráfica) tem
  sensibilidade/especificidade diagnóstica validada para TDM/ansiedade (Geoffroy et al., 2025)
  [revisão de autoridade; **inventário negativo**; bem suportado].
- **Estudos de associação de genes-relógio** (polimorfismos de CLOCK/PER/CRY/REV-ERB etc.) na TDM
  são **heterogêneos e sem gene consistentemente replicado** em revisão sistemática (Melhuish
  Beaupre et al., 2020); meta-análise de genes circadianos na TDM sem associação robusta (revisão
  sistemática, 2018) [RS/humano; **achado nulo**; bem suportado].
- **Amplitude de transcrição de genes-relógio** em tecido humano: a revisão de etiologia documenta
  tanto atenuação quanto **achados nulos** (de Leeuw et al., 2023) [revisão; **inconsistência**;
  moderadamente suportado].
- **MTNR1A/MTNR1B** em GWAS de humor: sem associação robusta estabelecida (permanece `[G1]` para
  a Rodada 2) [lacuna].
- **Fase como "teste"**: não há fase única (toda atrasada ou toda avançada) que defina depressão
  — a direção é heterogênea (avanço, atraso e desalinhamento; Coleman et al., 2019) [humano;
  **negação de marcador único**; bem suportado].
- Alegações quantitativas fortes de revisões de baixo peso (ex.: "25–40% de risco", "CAR
  hiperativo na ansiedade", "luz em suicidas") **não lastreadas em fonte indexada** — entram como
  `[G1]`/a confirmar, não como fato (ver Briefing, descarte de fonte predatória).

> **Autoauditoria do Módulo 02:** os mediadores foram distribuídos entre maquinaria (2.1), saídas
> endócrinas (2.2), neurotransmissão (2.3), plasticidade (2.4) e imune/metabólico (2.5), evitando
> concentração apenas em melatonina/cortisol (o "óbvio"). O **inventário negativo** está explícito
> e é uma marca deste mecanismo (Geoffroy 2025: sem biomarcador único). Ore xina/TEPT (2.3), IL-6/
> amígdala e crononutrição (2.5) têm autor a confirmar no G2 (PMID no Briefing) — não se inventou.

[REF_MODULO_02: Landgraf_2016 | Ozburn_2017 | Meyer_2024 | McCarthy_2011 | Coleman_2019 |
Souêtre_1989 | Adam_2017 | Stalder_2022 | Kim_2017 | Daut_Fonken_2019 | Hines_2013 | Liang_2025 |
Benedetti_2004 | Sato_2022 | Alesci_2005 | Schrader_2024 | Bautista_2025 | Geoffroy_2025 |
Melhuish_Beaupre_2020 | deLeeuw_2023]

---

## MÓDULO 03 — MAPA EXAUSTIVO DE TIPOS CELULARES E ESTRUTURAS

### 3.1 Tipos celulares
- **Neurônios do SCN (rede GABAérgica, ~20 mil neurônios)** — marcapasso mestre; geram ritmo de
  ~24 h em rede e sincronizam o organismo; transplante impõe o período do doador (Ralph et al.,
  1990); o SCN é uma rede acoplada (Hastings, Maywood & Brancaccio, 2018) [básico/animal;
  causal/marco; muito estabelecido]. A **ablação de Sox2** no SCN perturba o comportamento
  ansioso/depressivo (dado animal, 2021 — autor a confirmar no G2) [animal; causal; emergente].
- **ipRGC (células ganglionares retinianas intrinsecamente fotossensíveis, melanopsina/OPN4)** —
  fotorreceptores do relógio, distintos de bastonetes/cones (Hattar et al., 2002; Berson et al.,
  2002) [básico/marco; mecanístico; muito estabelecido].
- **Neurônios monoaminérgicos rítmicos** (dopaminérgicos VTA/área tegmental; serotoninérgicos
  dos núcleos da rafe; noradrenérgicos do locus coeruleus) — disparo e síntese modulados pelo
  relógio (Kim et al., 2017; Daut & Fonken, 2019) [revisão/animal; contributivo; bem suportado].
- **Astrócitos** — participam do relógio (sinalização de adenosina na privação de sono; Hines et
  al., 2013) e da regulação rítmica glutamatérgica [animal; causal/mediacional; emergente].
- **Células pinealócitos** — síntese noturna de melatonina/AANAT [básico; mecanístico; muito
  estabelecido].
- **Neurônios de núcleos límbicos com relógio próprio** (mPFC/CPF, hipocampo, amígdala, NAc,
  estriado) — relógios locais que desacoplam sob estresse (Meyer et al., 2024; Logan et al.,
  2015; Gardner et al., 2026) [animal; causal/associativo; emergente a bem suportado].
- **Células imunes rítmicas** (monócitos/linfócitos com relógio periférico; citocinas rítmicas;
  Zeng et al., 2024; Alesci et al., 2005) [humano+revisão; associativo; moderadamente suportado].
- **Micróbiota intestinal rítmica** — comunidade com oscilação diária que alimenta o eixo
  intestino–cérebro–circadiano (Bautista et al., 2025) [revisão; hipótese/contributivo; emergente].

### 3.2 Estruturas anatômicas e circuitos
- **Núcleo supraquiasmático (SCN)** do hipotálamo — relógio-mestre; entrada fótica via RHT;
  disfunção causa fenótipo depressivo/ansioso (Landgraf et al., 2016; Liang et al., 2025; Vadnie
  et al., 2021) [animal; causal; muito estabelecido].
- **Trato retino-hipotalâmico (RHT)** e **ipRGC** — via de arrasto fótico (Hattar; Berson;
  Fernandez) [básico; mecanístico; muito estabelecido].
- **Glândula pineal** — saída melatoninérgica [básico; muito estabelecido].
- **Eixo HPA (hipotálamo–hipófise–adrenal)** — cortisol rítmico sob controle do SCN; interação
  ritmo×estresse (Koch et al., 2017) [revisão; contributivo; bem suportado — B2].
- **Córtex pré-frontal (mPFC/CPF)** — relógio local que medeia a privação de sono (Gardner et al.,
  2026); [18F]-FDG e metabolismo regional predizem resposta à privação de sono (Wu et al., 1999)
  [animal+humano; causal/neuroimagem; emergente].
- **Núcleo accumbens (NAc)** — relógio local com efeitos opostos de Per1/2 vs Npas2 sobre
  ansiedade (Meyer et al., 2024) [animal; causal; emergente-maduro].
- **Amígdala** — regulação emocional associada ao ritmo de IL-6 (dado humano, 2023) e à
  modulação fótica do humor (Bedrosian & Nelson, 2017) [humano+revisão; associativo; emergente].
- **Hipocampo** — neurogênese e plasticidade rítmicas; vulnerável ao desalinhamento (revisões
  Logan & McClung, 2019; Dollish et al., 2023) [revisão/animal; contributivo; moderadamente
  suportado].
- **VTA/estriado** — dopamina/recompensa rítmica; BDNF–TrkB estriatal na disfunção do SCN (Liang
  et al., 2025; Kim et al., 2017) [animal; causal/mediacional; emergente].
- **Relógios periféricos** (fígado, músculo, adiposo, intestino, adrenal) — arrastados por
  alimentação/glicocorticoides; podem dessincronizar do SCN (Pezük et al., 2012; Mohawk et al.,
  2012) [básico/animal; mecanístico; bem suportado].
- **Métodos de avaliação na literatura:** actigrafia de punho (atividade-repouso), DLMO salivar/
  plasmático, cortisol salivar, temperatura, polissonografia, e neuroimagem rítmica — ver Módulo
  05.

> **Autoauditoria do Módulo 03:** cobriu-se o eixo retina→SCN→pineal (ó bvio) **e** as estruturas
> límbicas com relógio local (NAc, mPFC, amígdala, VTA/estriado) e os componentes celulares
> menos lembrados (astrócito/adenosina, Sox2-SCN, microbiota rítmica). O ablação-Sox2 (2021) tem
> autor a confirmar no G2. Nenhuma estrutura foi inventada.

[REF_MODULO_03: Ralph_1990 | Hastings_2018 | Hattar_2002 | Berson_2002 | Landgraf_2016 |
Liang_2025 | Vadnie_2021 | Meyer_2024 | Hines_2013 | Gardner_2026 | Pezük_2012 | Kim_2017 |
Bedrosian_Nelson_2017 | Koch_2017 | Bautista_2025 | Mohawk_2012]

---

## MÓDULO 04 — VARIABILIDADE GENÉTICA E EPIGENÉTICA EXAUSTIVA

**Teste de escopo aplicado a cada item:** variantes de genes-relógio só entram quando há estudo
em ansiedade/depressão/bipolar (humano) ou manipulação em modelo de humor (animal). O que é só de
outra doença (esquizofrenia/Alzheimer/câncer) sem ponte vai para o Módulo 10.

### 4.1 Variantes de genes-relógio em transtornos de humor (humano)
- **CLOCK (3111 T/C; rs1801260 e relacionados):** influencia sono/atividade por actimetria e
  resposta de longo prazo ao lítio no bipolar (Benedetti et al., 2007; Benedetti et al., 2005);
  revisão do papel de CLOCK nos transtornos psiquiátricos (Schuch et al., 2018) [humano/genética;
  associativo; moderadamente suportado].
- **GSK3β (SNP do promotor):** associado a início/resposta à privação de sono no bipolar
  (Benedetti et al., 2004) [humano/genética; associativo; moderadamente suportado].
- **REV-ERBα/NR1D1:** variação funcional associada à resposta ao lítio no bipolar (McCarthy et
  al., 2011) [humano/genética; associativo; moderadamente suportado].
- **PER3 (rs17031614) e CRY1 (rs2287161):** em estudo de ML/expressão em população profundamente
  fenotipada, o genótipo **PER3-AG/CRY1-CG** é o preditor mais forte de risco de ansiedade **em
  homens**, com fase avançada+desalinhamento associada a ansiedade grave (Zafar et al., 2022)
  [humano/ML; **associativo/preditivo, exploratório**; emergente — nota: os genes ABCC2/APP/HK2/
  RORA citados em prosa em outro insumo não aparecem no abstract deste paper; confirmar no G3].
- **Variantes Per3 e início pós-parto do bipolar** (Dallaspezia et al., 2011); **via da
  melatonina MTNR no bipolar** (Etain et al., 2012) [humano/genética; associativo;
  moderadamente/fracamente suportado].

### 4.2 Genética humana: o achado nulo e a exceção causal
- **Revisão sistemática de genes circadianos na TDM: sem associação consistente** (Melhuish
  Beaupre et al., 2020); RS de clock genes na etiologia da TDM com resultados heterogêneos (RS,
  2018); modelagem molecular de polimorfismos circadianos×humor (2018) [RS/modelagem; **achado
  nulo/heterogêneo**; bem suportado].
- **GWAS/PheWAS** de fenótipos circadianos×humor: fracos (conforme revisões Consensus/Zafar);
  **MTNR1A/MTNR1B** sem associação robusta (`[G1]`) [lacuna].
- **Randomização Mendeliana (MR):** a **preferência diurna (cronotipo matutino)** é
  causalmente protetora contra depressão/ansiedade (O'Loughlin et al., 2021, *Mol Psychiatry*)
  [MR/humano; **causal (sobre cronotipo, não sobre gene isolado)**; bem suportado]. Associações
  sexo-específicas de genes do relógio no UK Biobank (Minbay et al., 2024) [genética/humano;
  associativo; emergente].

### 4.3 Prova causal animal (manipulação de gene-relógio → comportamento de humor)
- **ClockΔ19 → comportamento tipo-mania, bloqueado por lítio** (Roybal et al., 2007; Andrabi et
  al., 2020) [animal; **causal**; bem suportado].
- **Bmal1 KD no SCN → desamparo/desespero/ansiedade** (Landgraf et al., 2016); **Bmal1 cKO/lesão
  SCN → BDNF–TrkB estriatal** (Liang et al., 2025) [animal; causal; bem suportado/emergente].
- **NPAS2** regula ansiedade/GABA-A (Ozburn et al., 2017); **Per1/2 vs Npas2 no NAc** (Meyer et
  al., 2024); **Rev-erbα** (Otsuka et al., 2022); **Vadnie** (SCN↔ansiedade, 2021) [animal;
  causal; moderadamente a bem suportado].
- **Viés de sexo a registrar:** a pré-clínica circadiana foi historicamente dominada por machos;
  estudos fêmeas/perinatais (luz fraca pós-parto, 2025) são mais raros (lacuna de tradução).

### 4.4 Epigenética e expressão
- Metilação/expressão rítmica de genes-relógio em tecido periférico e em modelos de estresse;
  transcriptômica circadiana como biomarcador **exploratório** (Shi et al., 2024, ML/4 genes —
  bioinformática, a validar) [bioinformática; **hipótese inicial**; emergente].
- Modificação epigenética de genes-relógio induzida por estresse/turno e sua reversibilidade:
  literatura ainda incipiente — **"literatura insuficiente para maior resolução nesta camada"**
  para epigenética específica em humor (sinalizado como lacuna, não preenchido).

> **Autoauditoria do Módulo 04:** cada variante humana passou pelo teste de escopo (há estudo em
> humor/bipolar). O contraste **causal animal forte × genética humana fraca/heterogênea** está
> explícito, e a MR de cronotipo é apresentada como exceção causal (sobre cronotipo, não sobre um
> gene). Não se afirmou gene único causal em humano. ML/4 genes (Shi 2024) e os genes do estudo
> Zafar estão marcados como exploratórios; ABCC2/APP/HK2/RORA vão para confirmação no G3.

[REF_MODULO_04: Benedetti_2004 | Benedetti_2005 | Benedetti_2007 | McCarthy_2011 | Schuch_2018 |
Zafar_2022 | Dallaspezia_2011 | Etain_2012 | Melhuish_Beaupre_2020 | O'Loughlin_2021 |
Minbay_2024 | Roybal_2007 | Andrabi_2020 | Landgraf_2016 | Liang_2025 | Ozburn_2017 | Meyer_2024 |
Shi_2024]

---

## MÓDULO 05 — BIOMARCADORES EXAUSTIVOS
*(catálogo apenas — **sem protocolo de coleta, sem valor de corte**; regra do BLOCO_05 do Prompt
4.0. A identidade e o papel biológico são listados; a operação fica para a clínica/Prompt 4.2.)*

Organizados nos **quatro níveis** adotados no Briefing, mais a divisão periférico/central/
neuroimagem do molde.

### 5.1 Nível comportamental (periférico, autorrelato)
- **Cronotipo (morningness/eveningness; MCTQ/MEQ)** — vespertinidade associada a depressão/
  ansiedade (Au & Reece, 2017; Norbury, 2021; meta global Dong et al., 2026; jovens Cheung et al.,
  2023) [meta/humano; **marcador/associativo**; bem suportado]. **Especificidade baixa** (é
  traço, não fase fisiológica nem diagnóstico).
- **Social jetlag (MCTQ)** — diferença trabalho/livre associada a humor (Gao et al., 2025;
  Ravenhall et al., 2026) [meta/RS; marcador/associativo; bem suportado]. Especificidade baixa.
- **Ritmos sociais/sintomas (BRIAN/SRRS)** e horário de sono-despertar (Szuba, 1992; Shear, 1994;
  Sabet, 2021) [humano; marcador; moderadamente suportado].
- **Insônia/sintomas de sono (autorrelato)** — prediz depressão/ansiedade bidirecionalmente (Li
  et al., 2016; Alvaro et al., 2013/2017) [meta/preditivo; marcador; bem suportado]. **Atenção:**
  é marcador de **estado de sono**, não de *timing*.

### 5.2 Nível actigráfico (periférico, objetivo)
- **MESOR, amplitude e acrofase** da atividade motora — **amplitude/MESOR reduzidos** na TDM
  (Ho et al., 2024, meta; Souêtre clássico) [meta/humano; **marcador objetivo**; bem suportado].
- **Interdaily Stability (IS) e Intradaily Variability (IV)** e fragmentação — menor
  estabilidade/maior variabilidade na TDM/ansiedade (Ho et al., 2024; Tazawa et al., 2019;
  coorte NESDA/Difrancesco et al., 2019) [meta/coorte; marcador; bem suportado].
- **Sleep Regularity Index** — regularidade como preditora (sinal de larga escala; wearables/UKB
  permanecem `[G1]` para confirmação) [emergente].
- Actigrafia validada por diretriz (Smith/AASM, 2018) [diretriz; método; muito estabelecido].
  **Especificidade moderada-baixa** (reflete atividade-repouso, não o relógio molecular
  diretamente; confundida por turno, doença médica, medicação).

### 5.3 Nível fisiológico (periférico/central)
- **DLMO (início da melatonina em luz fraca)** — marcador canônico de **fase**; DLMO avançado
  relativo ao sono em TDM jovem (Coleman et al., 2019) [humano; **marcador de fase**; bem
  suportado]. Especificidade moderada para fase; **não é teste de doença**.
- **Cortisol/CAR/slope diurno** — slope mais plano e ritmo alterado associados a humor (Adam et
  al., 2017; Stalder consenso 2022/2025) [meta/consenso; marcador; bem suportado].
- **Temperatura corporal central/MESOR** — achatada na depressão (Souêtre et al., 1989) [humano;
  marcador; moderadamente suportado].
- **Phase angle (relação de fase cortisol↔melatonina; temperatura↔sono)** — medida de
  **desalinhamento interno**, associada à gravidade (Buckley et al., 2010; Hasler et al., 2010);
  ainda experimental [humano/piloto; marcador; emergente].
- **Ritmo de citocinas (IL-6 diurno)** — achatado ↔ amígdala/humor (dado humano 2023; Alesci et
  al., 2005) [humano; marcador; emergente/moderado — B1].

### 5.4 Nível molecular (periférico/central; hoje de pesquisa)
- **Expressão de genes-relógio (CLOCK/BMAL1/PER/CRY/REV-ERB)** em PBMC/fibroblasto/sangue —
  sinal de amplitude/fase periférica (de Leeuw et al., 2023; Shi et al., 2024) [humanos;
  **marcador exploratório**; emergente]. **Especificidade baixa** (periférico ≠ neuronal).
- **Transcriptômica/epigenética/metabolômica circadiana** — painéis de ML (Shi 2024; Zafar 2022)
  [bioinformática; **hipótese inicial**; emergente].
- **BDNF e neurotrofinas séricos** com ritmo normalizado por cronobiótico (Satyanarayanan et al.,
  2020) [humano/intervenção; marcador; emergente].

### 5.5 Neuroimagem (central)
- **Metabolismo regional ([18F]-FDG)** prediz resposta à privação de sono no bipolar (Wu et al.,
  1999) [humano/neuroimagem; preditivo; moderadamente suportado].
- **Reatividade da amígdala** associada ao ritmo de IL-6 e à modulação fótica (dado humano 2023;
  Bedrosian & Nelson, 2017) [humano; marcador/associativo; emergente].
- Neuroimagem do relógio molecular/funcional em humor: campo ainda em consolidação — **piso de 3
  itens atingido** (FDG, amígdala, e estudos de fase/DLMO), mas a resolução molecular direta em
  cérebro humano é limitada.

> **Especificidade global (a levar ao Módulo 08):** nenhum desses marcadores é específico de
> ansiedade/depressão — todos são marcadores de **fase/amplitude/estabilidade do timing** ou do
> **estado de sono**, compartilhados por outras condições. Geoffroy et al. (2025) sintetizam:
> **não há biomarcador circadiano único validado para diagnóstico**. Os confundidores (luz
> ambiental suprimindo melatonina, hora da coleta, causalidade reversa, medicação, turno, idade,
> sexo, apneia) estão catalogados no Briefing §7.

> **Autoauditoria do Módulo 05:** catálogo em quatro níveis (comportamental/actigráfico/
> fisiológico/molecular) + neuroimagem, **sem protocolo nem valor de corte**. Indicou-se direção
> da alteração e especificidade (toda baixa/moderada, nenhuma alta). Não se apresentou nenhum
> marcador como "teste de depressão". IL-6/amígdala (2023) tem autor a confirmar no G2.

[REF_MODULO_05: Cole man_2019 | Ho_2024 | Tazawa_2019 | Difrancesco_2019 | Smith_2018 |
Souêtre_1989 | Adam_2017 | Stalder_2022 | Buckley_2010 | Hasler_2010 | Au_Reece_2017 |
Ravenhall_2026 | Li_2016 | Alvaro_2013 | deLeeuw_2023 | Wu_1999 | Satyanarayanan_2020 |
Geoffroy_2025]

---

*Fim da PARTE 1 (Módulos 00–05).*

---

# GERADOR DE PROFUNDIDADE MOLECULAR (GPM) — PARTE 2
## Mecanismo: B10 — Desregulação Circadiana (Ritmos / Sono / Luz) em Ansiedade e Depressão
### (Módulos 06–10)

## MÓDULO 06 — INTERCONEXÕES EXAUSTIVAS COM B1–B16

**Teste de escopo aplicado a cada conexão:** só se apresenta como *documentada* a ponte com
estudo em ansiedade/depressão/bipolar ou em modelo de humor; o que é apenas plausível por biologia
geral é sinalizado como **hipótese/emergente** ou vai para o Módulo 10. Força (HIGH/MEDIUM/LOW) é
estimativa preliminar para o Prompt 4.2 priorizar.

- **B2 — Eixo HPA / cortisol crônico (HIGH):** o SCN controla o ritmo do cortisol e o pulso
  matinal/CAR; o estresse (e o cortisol) por sua vez realimentam o relógio e arrastam relógios
  periféricos. Interação ritmo×estresse revisada (Koch et al., 2017); slope diurno de cortisol
  mais plano associado a pior saúde mental (Adam et al., 2017); *phase angle* cortisol↔melatonina
  na TDM (Buckley et al., 2010); achatamento rítmico clássico inclui cortisol (Souêtre et al.,
  1989) [humano+revisão; **bidirecional/contributiva**; bem suportado]. O subtipo H (Módulo 07) é
  a face clínica desta ponte.
- **B3 — Neuroplasticidade / BDNF (HIGH):** a disfunção do SCN produz fenótipo depressivo/ansioso
  via **ativação de BDNF–TrkB no estriado**, reversível por bloqueio (Liang et al., 2025) — ponte
  mecanisticamente demonstrada; GSK3β/mTOR/MAPK rítmicos ligam relógio e plasticidade e são
  compartilhados por antidepressivos rápidos (Sato et al., 2022); o relógio do mPFC medeia a
  privação de sono (Gardner et al., 2026) [animal+revisão; **causal/mediacional**; emergente-maduro].
- **B4 — Deficiência de monoaminas (MEDIUM-HIGH):** dopamina/recompensa ritmicamente regulada
  (Kim et al., 2017); 5-HT como elo comum relógio–estresse–humor (Daut & Fonken, 2019); NE com
  ritmo achatado (Souêtre et al., 1989); em animal, antidepressivo serotonérgico normaliza o
  arrasto à luz e o ritmo ultradiano (dado animal, 2016 — autor a confirmar no G2)
  [revisão+animal; **contributiva/bidirecional**; bem suportado]. A agomelatina (MT1/MT2 +
  5-HT2C) é fármaco-ponte, citada apenas como sinal.
- **B5 — Desregulação GABA/glutamato (MEDIUM):** o SCN é uma rede **GABAérgica** (Hastings et al.,
  2018); **NPAS2 regula ansiedade e receptores GABA-A** (Ozburn et al., 2017); a relação
  relógio↔neurotransmissão é bidirecional com desacoplamento sob estresse (Wang et al., 2026)
  [animal+revisão; **causal/contributiva**; bem suportado].
- **B1 — Neuroinflamação/imunidade (MEDIUM, emergente):** o relógio regula células imunes e a
  inflamação tem ritmo (revisão, Zeng et al., 2024); o **ritmo de IL-6 diurno achatado**
  associa-se à regulação emocional da amígdala (dado humano, 2023 — autor a confirmar no G2) e a
  TDM eleva IL-6 plasmático diurno (Alesci et al., 2005); agonista melatonérgico normaliza
  citocinas + genes clock em humano (Satyanarayanan et al., 2020) [humano+revisão; **associativa/
  contributiva**; moderadamente suportado].
- **B9/B6 — Disfunção mitocondrial / estresse oxidativo (MEDIUM, emergente):** o relógio orquestra
  metabolismo energético e redox; desarranjo circadiano, clock genes e saúde metabólica/mitocondrial
  convergem (Schrader et al., 2024) [revisão; **hipótese mecanística/contributiva**; emergente]. A
  ligação direta mitocôndria-rítmica **em humor com PMID próprio** permanece `[G1]` para a Rodada 2.
- **B7 — Disbiose / eixo intestino-cérebro (MEDIUM, emergente):** a microbiota tem ritmo diário e
  alimenta o eixo intestino–cérebro–circadiano em ansiedade/depressão (Bautista et al., 2025);
  microbioma na insônia/dessincronia/depressão (Li et al., 2018) [revisão; **hipótese/
  contributiva**; emergente].
- **B8 — Deficiências de micronutrientes / nutrição (LOW-MEDIUM, emergente):** o **horário** da
  ingestão (crononutrição), mais que o nutriente isolado, associa-se a sintomas depressivos (dado
  humano, 2025 — autor a confirmar no G2); a alimentação é *zeitgeber* de relógios periféricos
  (Schrader et al., 2024) [humano+revisão; **associativa**; emergente].
- **B13 — Sistema endocanabinoide / orexina (LOW, emergente):** a **orexina/hypocretina**
  (vigília/arousal) tem implicações cronopatológicas em sono/psiquiatria (revisão, 2018 — autor a
  confirmar no G2) [revisão; **hipótese mecanística**; fronteira].
- **B12 — Neurobiologia do trauma / TEPT (LOW, emergente):** a orexina é o neuropeptídeo de
  interface com o TEPT/sono (revisão, 2018); falta âncora humana circadiana **por transtorno**
  (TEPT/pânico/TAG/fobia) — permanece `[G1]` [revisão; **associativa/emergente**; hipótese inicial].
- **B14 — Neuroesteroides/hormônios (LOW-MEDIUM):** glicocorticoides arrastam relógios
  periféricos (Pezük et al., 2012); diferenças de ritmo/genética por sexo (Minbay et al., 2024);
  vulnerabilidade perinatal à luz noturna (dado animal, 2025) [básico+humano+animal;
  **contributiva**; moderadamente/emergente].
- **B15 — Autofagia/mTOR/clearance (LOW, emergente):** mTOR é nó rítmico compartilhado por
  antidepressivos rápidos e relógio (Sato et al., 2022); a privação de sono intersecta *clearance*/
  glicinfático (sem inversão da reconciliação B1) [revisão; **hipótese**; fronteira — `[G1]` para
  ponte específica em humor].
- **B16 — Neurogênese (LOW, emergente):** neurogênese e plasticidade hipocampal são rítmicas e
  sensíveis ao desalinhamento (Logan & McClung, 2019; Dollish et al., 2023); o exercício
  (*zeitgeber*) favorece marcadores tróficos (He et al., 2025) [revisão+animal; **contributiva**;
  emergente].
- **B11 — Disfunção tireoidiana (LOW):** o TSH tem ritmo que se achata na depressão (Souêtre et
  al., 1989) [humano; **marcador/associativa**; fraco].

> **Autoauditoria do Módulo 06:** B10 é um mecanismo **transversal de sincronização** — por isso
> toca quase todos os blocos, mas com força distinta: HIGH para B2 (HPA) e B3 (BDNF, ponte
> causal demonstrada), MEDIUM para B4/B5/B1 e B9/B7 (emergentes), LOW para B8/B13/B12/B15/B16/B11.
> As pontes sem estudo-ponte em humor (mitocôndria-rítmica, glicinfática, TEPT circadiano) foram
> sinalizadas como hipótese/`[G1]`, não apresentadas como documentadas. Citações animais/humanas
> com autor a confirmar no G2 estão marcadas.

[REF_MODULO_06: Koch_2017 | Adam_2017 | Buckley_2010 | Souêtre_1989 | Liang_2025 | Sato_2022 |
Gardner_2026 | Kim_2017 | Daut_Fonken_2019 | Ozburn_2017 | Hastings_2018 | Wang_2026 | Zeng_2024 |
Alesci_2005 | Satyanarayanan_2020 | Schrader_2024 | Bautista_2025 | Li_2018 | Pezük_2012 |
Minbay_2024 | Logan_McClung_2019 | Dollish_2023 | He_2025]

---

## MÓDULO 07 — SUBTIPOS E FENÓTIPOS CLÍNICOS DOCUMENTADOS

> **Natureza desta seção:** os "subtipos circadianos" abaixo são uma **heurística de
> fenotipagem** (sobreponíveis, não classes mutuamente exclusivas nem taxonomia validada) — útil
> para a curadoria, não um diagnóstico. Documentam-se os perfis biológicos distintivos e o lastro.

**Subtipos circadianos da depressão (A–H; sobreponíveis):**
- **Tipo A — fase atrasada + vespertinidade:** DLMO/sono tardios, eveningness; associado a
  depressão/ansiedade e a jovens (Au & Reece, 2017; Norbury, 2021; Cheung et al., 2023; Crouse et
  al., 2021) [meta/humano; **associativo/marcador**; bem suportado].
- **Tipo B — fase avançada + despertar precoce:** fase adiantada, típica de despertares
  matutinos na melancolia/idosos; fase avançada também na **mania** (Moon et al., 2016) [humano;
  **associativo/marcador**; moderadamente suportado].
- **Tipo C — amplitude reduzida (achatamento):** MESOR/amplitude/estabilidade baixos — o sinal
  objetivo mais replicado na TDM (Souêtre et al., 1989; Ho et al., 2024) [meta/humano;
  **marcador**; bem suportado].
- **Tipo D — alta variabilidade / baixa estabilidade diária:** IS baixo/IV alto/fragmentação;
  prediz humor (Ho et al., 2024; Tazawa et al., 2019; Sabet et al., 2021) [meta/coorte;
  **marcador/preditivo**; bem suportado].
- **Tipo E — *social jetlag*:** descompasso trabalho/livre associado a depressão/ansiedade,
  inclusive em adolescentes (Roenneberg et al., 2012; Gao et al., 2025; Ravenhall et al., 2026)
  [meta/RS; **associativo**; bem suportado].
- **Tipo F — SCN relativamente intacto com relógios periféricos/metabólicos desalinhados:**
  dessincronização interna (alimentação/metabolismo fora de fase com o SCN); lastro emergente
  (Pezük et al., 2012; Schrader et al., 2024; desacoplamento de relógios locais, Wang et al.,
  2026) [básico+revisão; **hipótese de subtipo**; emergente].
- **Tipo G — alteração melatoninérgica:** fase/amplitude de melatonina/DLMO alterada; variantes
  MTNR no bipolar (Coleman et al., 2019; Etain et al., 2012) [humano; **marcador**; moderadamente
  suportado].
- **Tipo H — alteração conjunta HPA + circadiana:** *phase angle* cortisol↔melatonina e CAR
  alterados (Buckley et al., 2010; Adam et al., 2017) [humano; **marcador**; emergente/moderado].

**Fenótipos clínicos transversais:**
- **Transtorno bipolar — o fenótipo-relógio paradigmático:** disrupção de ritmo social precede
  episódios (Malkoff-Schwartz et al., 2000); mutante *Clock* tipo-mania **bloqueado por lítio**
  (Roybal et al., 2007); cronotipo/ritmo no bipolar (Melo et al., 2017; Meyrel et al., 2022);
  **fase avançada na mania vs atrasada na depressão/mania mista** (Moon et al., 2016) [humano+
  animal; **mais forte que na unipolar**; bem suportado].
- **Transtorno afetivo sazonal (SAD)/sazonalidade:** descrição fundadora (Rosenthal et al.,
  1984); hipótese de fase (Lewy et al., 2006); a **hora circadiana da luz matinal** determina a
  resposta no SAD (Terman et al., 2001 — sinal de cronoterapia fótica, não prescrição); modelos
  roedores diurnos de SAD (dado animal, 2021) [humano+animal; **mecanístico/fenotípico**; bem
  suportado].
- **Fenótipo de ansiedade (lastro próprio, não só via insônia):** SCN regula ansiedade (Vadnie et
  al., 2021); luz constante/noturna induz ansiedade (Tapia-Osorio et al., 2013; Ikeno et al.,
  2016); privação aguda de sono **aumenta ansiedade-estado** (Pires et al., 2016, meta
  experimental); cronotipo associado a ansiedade **independente de insônia** (Cox & Olatunji,
  2019); transtornos de ansiedade com sono alterado (Cox & Olatunji, 2020) [humano+animal;
  **bidirecional/causal-experimental**; bem suportado]. **Falta âncora humana por transtorno
  específico** (TAG/pânico/TEPT/fobia) — `[G1]`.
- **Fenótipo desenvolvimental:** adolescente = atraso de fase/vespertino (Cheung et al., 2023;
  Crouse et al., 2021; Shanahan et al., 2014) vs idoso = avanço/achatamento (Souêtre; revisões de
  sono no idoso) [humano; **marcador**; bem suportado].
- **Fenótipo ocupacional/ambiental:** trabalhador de turno e exposto a luz noturna (Torquati et
  al., 2019; Obayashi et al., 2018; Cyr et al., 2022) — população de risco, não subtipo de doença.

> **Autoauditoria do Módulo 07:** os subtipos são apresentados como **heurística sobreponível**,
> não como taxonomia validada (Geoffroy et al., 2025: não há biomarcador único). O bipolar e o SAD
> têm lastro mais forte; o Tipo F (periférico) é explicitamente emergente. Nenhuma intervenção
> (luz/melatonina/IPSRT) é apresentada como tratamento de subtipo — só o fenótipo biológico.

[REF_MODULO_07: Au_Reece_2017 | Cheung_2023 | Crouse_2021 | Moon_2016 | Souêtre_1989 | Ho_2024 |
Tazawa_2019 | Sabet_2021 | Roenneberg_2012 | Ravenhall_2026 | Pezük_2012 | Schrader_2024 |
Wang_2026 | Coleman_2019 | Etain_2012 | Buckley_2010 | Malkoff-Schwartz_2000 | Roybal_2007 |
Melo_2017 | Meyrel_2022 | Rosenthal_1984 | Lewy_2006 | Vadnie_2021 | Tapia-Osorio_2013 |
Pires_2016 | Cox_Olatunji_2019 | Torquati_2019 | Geoffroy_2025]

---

## MÓDULO 08 — CONTROVÉRSIAS, HETEROGENEIDADE E LACUNAS

- **Ritmo (*timing*) vs estado de sono (insônia):** a confusão mais perigosa. Insônia é
  hiper-rouseamento/distúrbio do estado (Riemann et al., 2010; Riemann et al., 2019); o
  mecanismo B10 é a **rede temporal**. Privação de sono e desalinhamento circadiano são
  perturbadores diferentes (modelo de dois processos de Borbély: Processo S homeostático vs
  Processo C circadiano). *Resolveria*: estudos que meçam fase (DLMO) **e** sono separadamente.
- **Causa vs consequência (bidirecionalidade):** a depressão altera sono/ritmo/atividade/luz/
  social tanto quanto o ritmo perturbado prediz depressão (Walker et al., 2020 — ressalva causal
  explícita; revisões de bidirecionalidade, Alvaro et al., 2013; Zhang et al., 2022). A evidência
  humana é majoritariamente **associativa/preditiva**; as exceções causais são o animal
  (mutantes) e a **MR de cronotipo** (O'Loughlin et al., 2021). *Resolveria*: MR de variáveis de
  **fase** (não só de cronotipo) e ensaios naturais (turno/horário de verão).
- **Fase heterogênea — não existe "depressão = relógio atrasado":** há atraso, avanço
  (Coleman et al., 2019 — DLMO avançado relativo ao sono) e fases normais; na mania a fase é
  avançada e na depressão/mista atrasada (Moon et al., 2016). A síntese forçada de "um relógio
  atrasado" é incorreta.
- **Melatonina não é antidepressivo comprovado:** a melatonina exógena tem efeito
  limitado/heterogêneo (meta, Hansen et al., 2014); é cronobiótico de fase, não "pílula do sono/
  humor"; a agomelatina é **fármaco** (revisão/cochrane), não suplemento.
- **Luz: *timing* vs dose:** o efeito depende do horário circadiano (PRC; Khalsa et al., 2003;
  St Hilaire et al., 2012), não de "mais luz"; resposta heterogênea e revisões críticas das metas
  de luz não-sazonal (Dong et al., 2022). A *wake therapy* é rápida mas **transitória e com risco
  de virada maníaca** (Bunney et al., 2013).
- **Turno/luz noturna são ecológicos/observacionais**, não causa experimental (Torquati et al.,
  2019; Deprato et al., 2025 — números de efeito a confirmar no G3).
- **Genética humana fraca vs causalidade animal forte:** RS de genes-relógio sem gene consistente
  (Melhuish Beaupre et al., 2020); variantes comuns de efeito pequeno; o causal forte é o mutante
  animal (Roybal; Landgraf). Não se deve dizer "gene do relógio causa depressão em humano".
- **Vespertinidade não é doença:** associação pequena, traço normal em distribuição (Roenneberg);
  não transformar cronotipo em diagnóstico.
- **Viés de sexo na pré-clínica:** modelos historicamente dominados por machos; fêmeas/perinatal
  mais raros (luz fraca pós-parto, 2025) — limita tradução.
- **Alegações quantitativas fortes sem lastro indexado:** "25–40% de risco", "CAR hiperativo na
  ansiedade", "luz em suicidas", "neuroinflamação como driver" vieram de fonte predatória
  (descartada) — **não canônicas**; buscar fonte primária na Rodada 2 (`[G1]`).
- **Fonte real não-indexada:** Mendoza et al., 2024 (*Nature Mental Health*) é legítima mas sem
  PMID (ainda não no MEDLINE) — citar sem chave PMID.
- **Lacunas explícitas:** âncora humana circadiana **por transtorno de ansiedade** (TEPT/pânico/
  TAG/fobia); MTNR1A/B em GWAS; wearables/SRI em larga escala (UKB); cronofarmacologia dos
  psicofármacos; pontes BDNF/redox/mitocôndria/microbiota com PMID próprio; epigenética específica
  de humor; confirmação dos genes de ML (ABCC2/APP/HK2/RORA vs PER3/CRY1 do abstract real).

> **Nota sobre viés de publicação:** ver também o Inventário Negativo do Módulo 02 (genes-relógio
> sem associação, amplitude de transcrição com achados nulos, sem biomarcador único) — são parte
> da controvérsia, não ausência de pesquisa.

> **Autoauditoria do Módulo 08:** as controvérsias centrais (*timing*≠*estado*, bidirecionalidade,
> fase heterogênea, melatonina≠antidepressivo, luz por *timing*, genética humana fraca, viés de
> sexo) estão documentadas com (Autor, Ano). As alegações quantitativas fortes sem fonte
> indexada (RR/OR/"25–40%"/CAR/luz-em-suicidas) foram **excluídas ou marcadas `[G1]`**, não
> afirmadas como fato. A fonte predatória e a não-indexada (Mendoza 2024) têm tratamento
> distinto e explícito. As lacunas (ansiedade por transtorno, MTNR-GWAS, wearables, pontes
> BDNF/redox/mitocôndria) estão listadas para a Rodada 2 — nenhuma foi preenchida com
> extrapolação.

[REF_MODULO_08: Riemann_2010 | Riemann_2019 | Walker_2020 | Alvaro_2013 | O'Loughlin_2021 |
Coleman_2019 | Moon_2016 | Hansen_2014 | Khalsa_2003 | Dong_2022 | Bunney_2013 | Torquati_2019 |
Melhuish_Beaupre_2020 | Roybal_2007 | Landgraf_2016 | Roenneberg_2003 | Mendoza_2024 |
Geoffroy_2025 | Zafar_2022]

---

## MÓDULO 09 — CHECKLIST DE VERIFICAÇÃO CRUZADA COM O PROMPT 4.0

| Categoria deste GPM (B10) | Bloco correspondente no Prompt 4.0 | Conteúdo de partida | Status |
|---|---|---|---|
| Módulo 01 (vias) | BLOCO_02.1–2.3 (vias/sinalização) | TTFL; ipRGC/RHT/SCN; melatonina/DLMO; relógios locais/desacoplamento; saídas rítmicas; integração metabólica; zeitgebers sociais | [ ] preencher no 4.0 |
| Módulo 02 (mediadores) | BLOCO_03 (mediadores) | BMAL1/CLOCK/NPAS2/PER/CRY/REV-ERB/ROR/CK1δ/ε; melatonina/AANAT; cortisol/CAR; monoaminas; orexina; adenosina; BDNF; IL-6; NAD/SIRT1 + inventário negativo | [ ] |
| Módulo 03 (células/estruturas) | BLOCO_04 (células/estruturas) | Neurônios SCN; ipRGC; monoaminérgicos; astrócitos; pinealócitos; relógios límbicos; imunes; microbiota; SCN/RHT/pineal/HPA/mPFC/NAc/amígdala/VTA/periféricos | [ ] |
| Módulo 04 (genética/epigenética) | BLOCO_02.4 (genética/epigenética) | CLOCK/GSK3β/Rev-Erbα/PER3/CRY1/Per3/MTNR; RS nulos; MR de cronotipo; mutantes animais; epigenética incipiente | [ ] |
| Módulo 05 (biomarcadores) | BLOCO_05 (biomarcadores; sem protocolo/corte) | 4 níveis: comportamental/actigráfico/fisiológico/molecular + neuroimagem; DLMO/MESOR/IS/IV/CAR/phase angle; todos baixa/moderada especificidade | [ ] |
| Módulo 06 (interconexões) | BLOCO_08 (crosstalk B1–B16) | HIGH: B2 HPA, B3 BDNF; MEDIUM: B4/B5/B1, B9/B7; LOW: B8/B13/B12/B15/B16/B11 | [ ] |
| Módulo 07 (subtipos) | BLOCO_12 (subtipos/fenótipos) | Subtipos circadianos A–H; bipolar; SAD; ansiedade; desenvolvimental; ocupacional | [ ] |
| Módulo 08 (controvérsias) | Seção CONTROVÉRSIAS E LACUNAS | timing≠estado; bidirecionalidade; fase heterogênea; melatonina≠antidepressivo; luz timing; genética fraca; viés de sexo; `[G1]` | [ ] |

*Este checklist é preenchido pelo Prompt 4.0 durante a geração da Biblioteca; aqui está o
mapeamento de conteúdo de partida.*

[REF_MODULO_09: mapeamento estrutural Molde_GPM_v2.0 × Prompt_4.2 | Briefing_B10_2026]

---

## MÓDULO 10 — OBSERVAÇÕES EM OUTRAS CONDIÇÕES
*(amostra **ilustrativa**, não triagem sistemática — sinalização para revisão futura; ver regra de
escopo. Itens aqui não entram na contagem de cobertura do mecanismo.)*

- **Transtornos do ritmo sono-vigília (DSWPD/ASWPD etc.):** síndromes primárias de fase do
  sono, fortemente circadianas e comórbidas com humor (revisão, *Sleep Med Rev*, 2026) — são o
  espelho clínico do *timing*; incluir na fronteira, não confundir com insônia.
- **Trabalho de turno / *jet lag* de fuso:** dessincronização crônica ocupacional/ambiental
  (Torquati et al., 2019; revisão de vulnerabilidade no turno, 2020); eixo amplo de saúde
  (metabólico, cardiovascular), não só psiquiátrico.
- **Transtorno do espectro autista / TDAH (neurodesenvolvimento):** distúrbios de sono/
  dessincronização circadiana frequentes (RS no autismo, Carmassi et al., 2019); ponte com humor
  indireta [EXTRAPOLAÇÃO POR ANALOGIA: neurodesenvolvimento — validação direta em ansiedade/
  depressão limitada].
- **Neurodegeneração (Alzheimer):** degeneração do SCN e desorganização rítmica como parte da
  doença; biologia do relógio no envelhecimento — ponte com humor indireta [EXTRAPOLAÇÃO POR
  ANALOGIA].
- **Esquizofrenia/psicose:** desarranjo de sono e ritmo documentado (revisão, 2011) e
  vespertinidade em risco de psicose (2021) — condição psiquiátrica vizinha, fora do escopo
  ansiedade/depressão.
- **Apneia obstrutiva do sono:** distúrbio de **estado** de sono que confunde actigrafia/ritmo;
  confundidor, não mecanismo B10 primário.
- **Câncer / turno (IARC):** trabalho de turnos como provável carcinógeno e relógios na
  oncologia — corpo de evidência não-psiquiátrico.
- **Obesidade/síndrome metabólica:** "síndrome circadiana" e alimentação fora de hora (crononutrição)
  — domínio metabólico; toca B8/B9.
- **Fronteira técnica (não doença):** *wearables*/actigrafia de consumo, Sleep Regularity Index
  em larga escala (UKB), cronofarmacologia, multi-ômica e medicina circadiana de precisão,
  fotoperíodo/estação — ferramentas/campos a monitorar (`[G1]` para dados duros).

[REF_MODULO_10: DSWPD_SleepMedRev_2026 | Torquati_2019 | Carmassi_2019 | Walker_2020 |
Schrader_2024 | Briefing_B10_2026]

---

*Fim da PARTE 2 (Módulos 06–10). GPM B10 completo (Módulos 00–10). Os PMIDs verificados e a chave
frase↔referência vivem no **Briefing B10 consolidado** (blocos A–O); este GPM aponta território
para o Prompt 4.2. Segue-se o **Checklist de Sanidade do GPM** no molde oficial.*
