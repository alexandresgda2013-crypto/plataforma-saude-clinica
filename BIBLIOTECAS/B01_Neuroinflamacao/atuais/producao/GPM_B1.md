# GERADOR DE PROFUNDIDADE MOLECULAR (GPM) — B1 NEUROINFLAMAÇÃO
# VERSÃO 3 (trilha mecanística)

> Escopo: levantamento de território científico (descoberta), não Biblioteca final.
> Padrão de citação neste documento: (Autor, Ano) — NÃO contém PMID/DOI. Os
> identificadores e o suporte por frase são resolvidos na Busca Sistemática por
> ferramenta (Ato 1 da Rodada 2 do Processo de Geração). Toda menção a espécie
> (humano/animal/in vitro) é declarada; extrapolação é sinalizada.

---

# MÓDULO 00 — METADADOS E ESCOPO

- **ID canônico:** mecanismo_B1_neuroinflamacao
- **Mecanismo:** B1 — Neuroinflamação
- **Biblioteca-alvo (Prompt 4.2):** BLOCO_01 (Fundamentos), BLOCO_07 (nós centrais)
- **Tipo de evidência dominante:** revisões humanas (epidemiologia/meta-análise) + mecanística animal/in vitro; sinalização obrigatória da fronteira.
- **Natureza do mecanismo:** associação robusta em humanos; contributiva causal demonstrada em animal; relação bidirecional com HPA, plasticidade, redox e intestino.

## Regra de escopo (R01/R02, P20)
- O documento descreve o MECANISMO B1. Achados de outros mecanismos (HPA=B2,
  plasticidade=B3, redox=B6, intestino=B7, mitocôndria=B9, etc.) são citados em
  fronteira, com referência cruzada; o aprofundamento pertence à Biblioteca do
  mecanismo correspondente.
- O sistema é de APOIO ao raciocínio (não diagnóstico, não prescrição). Sem
  doses, sem recomendação terapêutica direta dentro do corpo mecanístico.

## Cobertura conceitual (tradições que o MÓDULO 08 deve reconciliar)
"low-grade inflammation", "cytokine-induced depression" (incl. interferon-induced),
"sickness behavior", "microglial priming", "immunometabolism", "central vs
peripheral crosstalk", "neuroimmune interactions", "inflammaging".

---

## Corte de conhecimento e busca (declaração obrigatória)
Este GPM é um levantamento de TERRITÓRIO e usa o padrão de citação
(Autor, Ano); ele NÃO contém PMID/DOI verificados em tempo real nesta etapa.
Os identificadores, a confirmação de existência (G1) e o suporte por frase (G3)
são resolvidos na **Busca Sistemática por Ferramenta (PubMed eutils)** —
Ato 1 da Rodada 2 do Processo de Geração, que produz `corpus_pubmed.json` e
`log_de_busca`. Até lá, as referências aqui são CANDIDATAS; qualquer achado
contado como definitivo nesta fase deve ser tratado como não verificado e
confirmado pela ferramenta antes de uso.

---

# MÓDULO 01 — MAPA EXAUSTIVO DE VIAS MOLECULARES

## 1.1 — A resposta inflamatória: da ativação imune ao cérebro

A **sickness behavior** (comportamento de doença) é o elo conservado: ativação
imune periférica (infecção, dano tecidual, estresse crônico) induz um conjunto
coordenado — anedonia transitória, retraimento social, fadiga, hipersonia,
redução de apetite — mediado por citocinas pró-inflamatórias, que redireciona
energia para defesa/ reparo (Dantzer e Kelley, 2007; Miller e Raison, 2016;
Capuron e Miller, 2011 — revisões humanas/conceituais). Em indivíduos
vulneráveis, a resposta aguda resolve mal e transita para um estado crônico de
**baixo grau (low-grade)** associado a transtornos de humor e ansiedade — sem
ser idêntica à inflamação aguda.

Duas vias de sinalização periferia→cérebro estão documentadas:
1. **Via humoral:** citocinas circulantes acessam regiões com barreira
   permissiva (órgão subfornical, área postrema, plexo coroide, organo
   vasculoso da lâmina terminal) e sinalizam a células endoteliais/pericitos e
   macrófagos perivasculares (revisões: Banks, 2015 — BHE; Capuron e Miller,
   2011).
2. **Via neural:** sinalização vagal aferente. A inflamação periférica ativa
   fibras vagas via receptores de citocinas no tronco (Goehler et al., 2000;
   Dantzer e colaboradores — animal); a subdiafragmática modula, mas não é a
   única rota (a barreira humoral persiste).

[ATENÇÃO — a ação central de citocinas periféricas sobre neurotransmissão é
majoritariamente demonstrada em modelo animal e inferida em humanos; declarar
quando um elo é extrapolado.]

## 1.2 — PRRs e a detecção de perigo (receptores de reconhecimento padrão)

As células da imunidade inata (microglia, macrófagos perivasculares, monócitos
infiltrantes) expressam PRRs que detectam PAMPs (padrões patogênicos) e DAMPs
(padrões de dano celular).

- **Toll-like receptors (TLR):** TLR4 (reconhece LPS bacteriano e DAMPs como
  HMGB1, fibronectina degradada) e TLR2 são os mais ligados a fenótipos
  depressivos; TLR3/7/9 (sensores virais/nucleicos) participam de estresse
  crônico animal (revisão: Fiebich et al., 2018 — mecanística).
- **Inflamassomas (NLRP3 à frente):** complexos multiproteicos que, ao
  reconhecerem DAMPs/estresse celular, montam a maquinaria de clivagem de
  caspase-1.
- **RIG-I-like / NOD-like / C-type lectin:** modulam priming e respostas a
  vírus e dano (mecanística, menos estudada em humor).

Regra de espécie: a maioria dos dados de perda de função (KO/antagonismo) é
animal/in vitro; a base humana é genética-associativa e de marcadores.

## 1.3 — O inflamassoma NLRP3 e a piroptose

O **NLRP3** é o inflamassoma mais documentado em neuroinflamação ligada a humor
e ansiedade. Duas etapas:
1. **Priming (sinal 1):** TLR4/IL-1R/NF-κB induzem transcrição de NLRP3,
   pró-IL-1β e pró-IL-18.
2. **Ativação (sinal 2):** sinais de dano (K+ efflux, mtROS/DNA mitocondrial
   oxidado, ATP extracelular → P2X7, cristais, lysosomal damage) promovem
   montagem NLRP3 + ASC + pro-caspase-1.

Saídas:
- caspase-1 ativa cliva pró-IL-1β e pró-IL-18 → IL-1β e IL-18 maduros;
- cliva **gasdermina-D (GSDMD)**: o fragmento N-terminal forma poros na
  membrana → **piroptose** (morte celular inflamatória) e liberação do
  conteúdo. [PRÉ-CLÍNICO para o efeito comportamental em ansiedade/depressão;
  humano = associação de marcadores/genética].

Reguladores negativos documentados (mecanística): **autofagia** degrada
componentes do inflamassoma; **SIGIRR/TIR8** limita sinalização TLR/IL-1R.

## 1.4 — Gasderminas (efetoras de piroptose)

Além de GSDMD (o canônico piroptótico), GSDME/DFNA5 responde a caspase-3 e
expande a morte celular inflamatória para estímulos classicamente
"apoptóticos". Em ansiedade/depressão, o papel comportamental é **pré-clínico
emergente** (Li et al., 2021/2022, estudos NLRP3/GSDMD em estresse em
camundongo); não há validação humana direta. [EXTRAPOLAÇÃO animal→humano].

## 1.5 — DAMPs relevantes ao B1

Moléculas de dano que ativam PRRs/inflamassomas:
- **HMGB1** (alarina nuclear liberada por morte celular; agonista de TLR2/4 e
  RAGE) — elevado em estudos de TDM/estresse;
- **ATP extracelular** (via P2X7, gatilho clássico de NLRP3);
- **mtDNA e mtROS** (dano mitocondrial; liga B1↔B9 mitocôndria);
- **DNA livre, S100/cristais**;
- **LPS translocado** (ver eixo intestino 1.10).

## 1.6 — NF-κB e o eixo glicocorticoide

**NF-κB** é o nó transcricional central da resposta pró-inflamatória:
ativa TLR/IL-1R/TNFR → IKK → degradação de IκB → translocação de p65/p50 →
transcrição de citocinas, quimiocinas, COX-2, iNOS.
- **Feedback glicocorticoide (B1↔B2):** o cortisol/GR normalmente reprime
  NF-κB (trans-repressão). No estresse crônico surge **resistência
  glicocorticoide em células imunes** (GR não suprime NF-κB de forma eficiente)
  → inflamação persiste apesar de cortisol (revisão: Raison e Miller, 2003;
  Bierhaus et al. — mecanística/animal + humano em queimadura/metabólico).
- Sensibilidade reduzida à retroalimentação reforça priming microglial.

## 1.7 — Via da quinurenina (B1↔B4/B12)

Ativada por citocinas (IFN-γ, IL-1β, TNF), a **indoleamina 2,3-dioxigenase
(IDO)** desvia triptofano da serotonina para a via da quinurenina (KYN).
Bifurcação chave:
- **Ramo neuroprotetor/antioxidante:** KYN → **ácido quinolínico? não** —
  KYN → ácido quinurênico (KYNA), agonista de receptores NMDA/α7 nicotínicos
  (em astrócitos);
- **Ramo neurotóxico:** KYN → **3-HK** e **ácido quinolínico (QUIN)**
  (em microglia/monócitos infiltrantes) — QUIN é agonista NMDA e gerador de
  ROS; 3-HK é pró-oxidante.
O balanço **QUIN/KYNA** deslocado para o lado neurotóxico é o elo molecular
entre inflamação e disfunção glutamatérgica/dopaminérgica (revisões:
Dantzer et al., 2008; Schwarcz e colaboradores; Steiner et al., 2011 —
pós-morte/ LCR humano para QUIN, em contexto de suicídio/neuroinflamação).

[CUIDADO: Steiner et al., 2011 é de VÍTIMAS DE SUICÍDIO/pós-morte e LCR —
popular de suicídio, não "depressão geral" na fonte; essa distinção precisa
estar na evidência final.]

## 1.8 — Sistema complemento e poda sináptica (B1↔B3/B13)

C1q e C3 marcam sinapses para eliminação microglial via CR3 (Stevens et al.,
2007 — desenvolvimento; Sekar et al., 2016 — genética humana em esquizofrenia,
**outra condição → EXTRAPOLAÇÃO** para depressão). C4 variantes modulam poda.
Em humor, a participação do complemento na plasticidade é mecanisticamente
plausível mas majoritariamente inferida de outra condição.

## 1.9 — Lipídios pró-resolutivos especializados (SPMs)

A inflamação NÃO é só "ligar": a **resolução** é um programa ativo.
- **Resolvinas (RvD/E), protectinas (PD/NPD), maresinas (MaR), lipoxinas**
  derivados de ômega-3/6 (Serhan et al.) limitam recrutamento neutrofílico,
  promovem fagocitose de restos por microglia e encerram o estado pró-
  inflamatório.
- A ausência/insuficiência de SPMs é hipótese para inflamação persistente
  (FRED-PROTECT; subexplorada — gap, ver MÓDULO 08). [Efeito comportamental e
  metabolismo SPM: PRÉ-CLÍNICO].

## 1.10 — Eixo intestino–micróbio–neuroinflamação (B1↔B7)

- **LPS (lipopolissacarídeo)** translocado por permeabilidade aumentada ativa
  TLR4 na interface. Estudos animais (Sohail et al., 2012 — depressão-like por
  administração; **modelo animal, não demonstra translocação em deprimidos
  humanos**);
- Sinais via LPS/TLR4, peptidoglicano/NOD e metabolitos (ver Biblioteca B7):
  SCFAs/butirato, indóis, peptídeos antimicrobianos.
- **Distinguição exigida (Briefing):** LPS em modelo animal (animal, causalidade
  inferida) vs estudos de LCR/sangue em pacientes (humano, associativo).

## 1.11 — Imunometabolism e senescência (B1↔B9/B12/inflammaging)

- **Priming microglial:** sensibilização por idade/estresse prévio baixa o
  limiar de resposta (Norden et al., 2015; revisão de envelhecimento).
- **SASP (senescence-associated secretory phenotype):** astrócitos/microglia
  senescentes secretam citocinas/proteases em baixo grau contínuo; senolíticos
  em estudo (mecanístico/animal).
- **mtROS/glicólise de microglia/M1-like** sustentam o fenótipo pró-
  inflamatório; há interseção com disfunção mitocondrial (B9).

## 1.12 — Rede de sinalização resumida (ordem causal da ativação)

```
estresse / patógeno / dano
   │  (PAMPs·DAMPs)
   ▼
PRR (TLR2/4, NLRP3) ──priming NF-κB──> transcrição pró-IL1β, TNF, IL-6
   │ sinal 2 (ATP/P2X7, mtROS, K+)              ▲
   ▼                                              │ resistência GR (B2)
INFLAMASSOMA NLRP3 + ASC + caspase-1
   ├─> IL-1β / IL-18 maduros
   └─> GSDMD -> PIROPTOSE + liberação
              │
              ▼
   microglia/macrófago ativados (+ astro A1)
   ├─> QUIN/3HK (quinurenina neurotóxica) -> NMDA/ROS
   ├─> TNF/IL-1 -> supressão BDNF/CREB (B3), HPA (B2)
   ├─> complemento C1q/C3 -> poda sináptica
   └─> [falta SPMs] -> resolução incompleta / priming (B9, idade)
```
> [Toda essa cascata é causal em modelo animal/in vitro; em humanos, o elo é
> demonstrado por marcadores, genética e intervenção de prova (vacinas/anti-
> citocina em subgrupo). Essa fronteira deve permanecer no texto final.]

[REF_MODULO_01: Dantzer_2008 | Miller_Raison_2016 | Capuron_Miller_2011 |
Banks_2015 | Fiebich_2018 | Heneka_2017_NLRP3 | Kelley_2019 | Swanson_2019 |
Sekar_2016 | Stevens_2007 | Serhan_SPM | Schwarcz_quinurenina |
Steiner_2011 | Norden_2015 | Sohail_2012 | Raison_Miller_2003]

---

# MÓDULO 02 — MAPA EXAUSTIVO DE MEDIADORES MOLECULARES

*Mediadores já detalhados como componente de via no MÓDULO 01 (NLRP3, NLRP1,
GSDMD, TLR2/3/4, componentes da quinurenina, C1q/C3/CR3, RvD/RvE, claudina-5)
não são redescritos integralmente — aqui entra o que é específico do mediador
isolado: função, direção, fonte, receptor e nível de evidência.*

## 2.1 — Citocinas pró-inflamatórias

Para CADA citocina, padrão: identidade / função / fonte celular / receptor /
direção em TDM·TAG·TEPT (humano) / evidência animal (manipulação) / natureza /
maturidade.

- **IL-1β** — citocina madura via inflamassoma (caspase-1). Fonte: monócitos,
  macrófagos, microglia, células da barreira. Receptores IL-1R1 (tipo I,
  sinalizante) e IL-1RA (antagonista endógeno). Direção: elevada em TDM
  (meta-análises em sangue/LCR; Howren et al., 2009; meta-análise Goldsmith,
  2016) e em subgrupos de ansiedade/TEPT. Animal: IL-1R1 KO e antagonismo
  reduzem fenótipos depressivos/anedônicos (contributivo). Associativo forte
  em humano; causal em animal. Maduro.
- **IL-6** — a mais replicada nas meta-análises de TDM (Dowlati et al., 2010;
  Haapakoski et al., 2015; Osimo et al., 2020/2021). Fonte: monócitos,
  macrófagos, linfócitos T, adipócitos, microglia/astrócitos. Receptor:
  **IL-6R de membrana (sinalização clássica, anti-regenerativa) vs.
  trans-sinalização via IL-6R solúvel + gp130 (perfil pró-inflamatório
  amplo)** — distinção que poucos estudos clínicos separam (medem "IL-6 total"
  no sangue). Direção: elevada; trans-sinalização é o ramo implicado em
  doença (revisões: Rose-John). Animal: KO/anti-IL-6 altera resposta ao
  estresse (contributivo). Muito estabelecido.
- **TNF-α** — Fonte: microglia, macrófagos, linfócitos, adipócitos.
  Receptores: TNFR1 (p55, pró-apoptótico/pró-inflamatório) e TNFR2 (p75,
  homeostático/neuroprotetor). Direção: elevada em TDM (meta-análises); a
  razão TNF/TNFR2 e a resposta de antagonistas (etanercepte/infliximabe em
  subgrupo inflamado — Raison et al., 2013, RCT) é a evidência clínica
  [mecanística com ressalva P20: achado clínico, não recomendação]. Animal:
  TNF media supressão de BDNF/LTP e comportamento de adoecimento (B1↔B3).
  Maduro.
- **IFN-γ** — principal indutor de IDO. Elevado em subgrupos; a depressão
  induzida por IFN-α (hepatite C — Capuron et al., 2002/2003; Bull et al.,
  2009 em genética/5-HTTLPR) é o modelo "proof-of-concept" humano de que
  citocina → comportamento depressivo. [Humano, intervenção — evidência
  causal mais forte do conjunto, em contexto terapêutico específico].

## 2.2 — Anti-inflamatórios e reguladores
- **IL-10** — principal citocina anti-inflamatória; limita NF-κB e
  inflamassoma. Pré-clínico: rIL-10 reverte ansiedade/depressão em modelos
  (Voorhees et al., 2013). Humano: baixos níveis/razão pró:anti deslocada
  (associativo).
- **TGF-β** — papel duplo (imunorregulação/fibrose); em neuroinflamação
  tende a anti-inflamatório/neuroprotetor na microglia (revisão).
- **IL-4 / IL-13** — polarização microglial/astroglial protetora (M2/A2);
  animais (pré-clínico).
- **IL-1RA** — antagonista endógeno de IL-1; marcador de contra-regulação.

## 2.3 — Quimiocinas
- **CCL2 (MCP-1)**, **CXCL8 (IL-8)**, **CXCL12 (SDF-1)**, **CCL5 (RANTES)**
  — modulam migração monocítica, permeabilidade e sinalização neural.
  Meta-análises (Leighton et al., 2018; revisões Eyre et al.) associam
  quimiocinas a TDM; natureza associativa, menos específica.
- **CX3CL1 (fractalquina)/CX3CR1** — eixo neurônio–microglia; regula poda e
  comunicação (mecanística, animal; relevância para B3/B12).

## 2.4 — Mediadores da via do quinurenato (detalhe)
- **Triptofano → 5-HT** vs. **desvio para KYN**: razão KYN/TRP como índice
  de ativação de IDO (Sublette et al., 2011; meta-análise de quinurenina).
- **KYNA** (astrócito): antagonista NMDA glicina + agonista α7nACh;
  neuroprotetor em concentração adequada.
- **QUIN** (microglia/macrófago): agonista NMDA no sítio glicina/NR1+NR2,
  gerador de ROS, pró-apoptótico; elevado em condições inflamadas;
  [Steiner et al., 2011 — LCR/tecidos de **suicídio/pós-morte**, não é
  "TDM geral": popular de suicídio com alta inflamação — aplicar qualificador].
- **3-HK / 3-HAA** — pró-oxidantes.

## 2.5 — Espécies reativas (B1↔B6)
- **ROS/RNS** (superóxido, ONOO−) amplificam NF-κB e inflamassoma; o oxida
  reverso (redox) reforça o loop inflamatório. Detalhe de enzimas está em B6.

## 2.6 — Mediadores lipidados (B1↔B7/B13, SPMs)
- **Prostaglandinas (PGE2 via COX-2)** — sinalizam febre/sick behavior,
  modulam febre/supressão; PGE2 central medeia parte do adoecimento.
- **SPMs (RvD1/D2/E1, PD1/NPD1, MaR1, LXA4)** — ver MÓDULO 01 (1.9);
  resolução ativa.
- **Endocanabinoides/neuroesteroides** — modulação anti-inflamatória cruzada
  com B13/B14 (revisões; pré-clínico).

[REF_MODULO_02: Dowlati_2010 | Haapakoski_2015 | Osimo_2020 | Goldsmith_2016 |
Howren_2009 | Raison_2013 | Capuron_2002 | Bull_2009 | Voorhees_2013 |
RoseJohn_IL6 | Sublette_2011 | Leighton_2018 | Schwarcz_quinurenina |
Steiner_2011 | Serhan_SPM]

---


## 2.7 — Inventário NEGATIVO (mediadores/desfechos sem associação consistente)
Registro honesto do que foi investigado mas NÃO mostrou associação robusta em
neuroinflamação de ansiedade/depressão (revisões e meta-análises negativas ou
heterogêneas) — não confundir com lacuna (MÓDULO 08):
- **Marcadores centrais traduzidos para sangue de forma não confiável**:
  nenhum marcador sanguíneo isolado (PCR, IL-6, BDNF sérico) tem especificidade
  diagnóstica; achados negativos/inconsistentes em coortes menores (ênfase na
  inespecificidade, não na ausência de mecanismo).
- **Anti-inflamatórios clássicos como intervenção generalizada**: sem benefício
  consistente fora do subgrupo citocina-alto (Raison et al., 2013 foi positivo
  apenas no subgrupo inflamado) — não há base para efeito global (achado clínico
  negativo para uso amplo).
- **GSDME/DFNA5 e gásderminas não-D** em comportamento: investigadas, sem
  evidência em ansiedade/depressão (apenas mecanístico emergente).
- **Neutrófilos e marcadores adaptativos (imunidade T/B)** no sangue periférico:
  associação fraca/inconsistente com TDM na maioria das meta-análises.
- **TSPO como marcador exclusivo de microglia**: a hipótese de "microglia=ativa
  medida por TSPO" teve resultados contraditórios (sinal também em astrócito/
  endotélio) — tratar a leitura unívoca como não sustentada.
[REGRA: itens aqui não "provaram o contrário" — não têm associação CONSISTENTE
no estágio atual; podem ser reclassificados com evidência nova.]

---

# MÓDULO 03 — MAPA EXAUSTIVO DE TIPOS CELULARES E ESTRUTURAS

## 3.1 — Microglia (NÃO é categoria única)
- **Estados** — nomenclatura M1-like (pró-inflamatória: iNOS/CD86,
  ROS/IL-1β/TNF/IL-6, fagocitose aumentada) vs M2-like (anti/regenerativa:
  CD206/Arginase-1/IL-10/TGFβ, fagocitose de resto). [ATENÇÃO: M1/M2 é
  SIMPLIFICAÇÃO DIDÁTICA — o estado real é um espectro/transcriptoma
  (Paolicelli et al.; revisões de imunologia single-cell); usar como
  polarização, não identidade fixa.]
- **Priming/treinamento imune** — sensibilização por idade (Norden et al.),
  por insulto prévio; baixa o limiar de reação.
- **Fagocitose/poda sináptica** — C1q/C3/CR3 (Stevens 2007; Sekar 2016,
  extrapolado de esquizofrenia).
- **Monitoração sináptica e de BHE**, CX3CR1.

## 3.2 — Astrócitos
- **A1 (neurotóxico/reativo)** vs **A2 (protetor/cicatricial)** — notação de
  Liddelow et al., 2017. A1 induzido por IL-1/TNF/C1q da microglia; perde
  função trófica, é pró-inflamatório. [Hipótese forte em cultura/animal;
  a extrapolação direta ao cérebro deprimido humano é parcial — marcar].
- Astrócito é a fonte de **glutamina** (ciclo glutamato-glutamina), de
  **KYNA**, mantém o meio sináptico e BHE.
- Reatividade astrócitária (GFAP) em pós-morte de depressão/suicídio.

## 3.3 — Células da barreira e infiltrantes
- **Células endoteliais** e **pericitos** da BHE: respondem a citocinas,
  regulam permeabilidade (claudina-5/ocludina/ZO-1); transporte de citocina.
- **Macrófagos perivasculares** e do plexo coroide; diferenciar de microglia
  (origens distintas).
- **Monócitos/macrófagos infiltrantes** (Ly6Chi em animal; em humano
  depende de permeabilidade) — a infiltração em TDM é associativa/discutida;
  o recrutamento é robusto em modelo animal.
- **Neutrófilos** — evidência mais fraca, marginal.
- **Linfócitos T/B** — regulação (Treg, Th17, B/IgA) em interface com B7.

## 3.4 — Neurônios como alvo (não produtor primário)
- Neurônios expressam receptores de citocina (IL-1R1, TNFR, IL-6R), receptores
  para PGE2, NMDA (QUIN) — são a parte efetora do fenótipo (neurotransmissor,
  BDNF/LTP, ritmo — B3/B2/B4).
- Podem produzir sinais de DAMP/alarinas (CX3CL1).

## 3.5 — Estruturas neuroanatômicas relevantes
- **BHE e interface sangüínea** — ver 1.1 / BHE:
  - BHE como filtro ativo: zonas permissivas (órgão circunventricular,
    plexo coroide).
  - Transporte de citocina, perda da junção apertada (claudina-5) —
    demonstrada em modelo (Menard et al., 2017, estresse; **camundongo**).
- **Glia do núcleo** (NAc, hipocampo, amígdala, ACC, córtex pré-frontal):
  - Hipocampo (BDNF/neurogênese), NAc (recompensa/anedonia), amígdala
    (ansiedade/medo) e córtex (ruminação/função executiva) recebem os efeitos.
- **Nervo vago** (afferente do tronco; tronco cerebral/NTS) — via neural.
- **Plexo coroide** e entrada de citocina/leptina.
- **Regiões doentes em LCR** — produção ventricular/leptomeníngea.

## 3.6 — Tecidos/órgãos periféricos da imunidade
- Monócitos circulantes (PBMCs), tecido adiposo (fonte de IL-6/TNF),
  intestino (B7), fígado (proteínas de fase aguda, CRP, SAA) — ver 4.

[REF_MODULO_03: Paolicelli_microglia | Norden_2015 | Liddelow_2017 |
Stevens_2007 | Sekar_2016 | Menard_2017 | Capuron_citocina |
Goshen_IL1 | Banks_2015 | Ransohoff_perivascular]

---

# MÓDULO 04 — VARIABILIDADE GENÉTICA E EPIGENÉTICA EXAUSTIVA

*Escopo: variabilidade humana relevante ao B1. Para cada marcador: gene/variante,
função, direção do achado (risco/resiliência/interação), evidência (humana
associativa GWAS/candidato; animal quando causal), natureza e maturidade.
Não confundir genética de resposta a tratamento com mecanismo central.*

## 4.1 — Genes de citocinas e seus receptores
- **IL-6 / IL-6R** (e promotor de IL6, rs1800795) — associações candidatas
  com depressão/fadiga em contexto inflamatório; Bull et al., 2009 é
  especificamente depressão **induzida por IFN-α em hepatite C** (amostra
  caucasiana) — não evidência de estresse precoce nem de heterogeneidade
  étnica. [Humano, intervenção/candidata; heterogêneo].
- **TNF / TNFR** — variantes (promotor -308) estudadas em depressão/insônia;
  associação fraca e inconsistente.
- **IL1B / IL1RN (IL-1RA)** — polimorfismos de resposta inflamatória;
  candidatos, replicados de forma variável.
- **IFNG / IL10 / TGFB1** — equilíbrio pró/anti; achados associativos em
  subgrupos inflamados.

## 4.2 — Receptores e sinalização
- **TLR4/TLR2 (CD284/CD282)** — variantes em resposta a LPS/estresse;
  associação a depressão em candidata (Hung et al., estudos de
  estresse/animal para mecanismo). Animal: TLR4 KO/KD reduz resposta
  depressiva (causal no modelo, não no humano).
- **NLRP3 / P2RX7** — variantes modulam inflamassoma; P2RX7 é canal de
  K+/ATP; estudos candidatos em depressão (Backlund et al., 2011/2012 —
  **transtorno bipolar/teor**, não TDM puro: aplicar a extrapolação de
  condição).
- **CRP (genética)** — variantes associadas a níveis de PCR e,
  indiretamente, a depressão (estudos de aleatorização mendeliana
  suportam componente inflamatório, sem provar causalidade direta em
  todos os transtornos).

## 4.3 — Genes de modulação trans-critica (intersecção B1/B4)
- **5-HTTLPR/SLC6A4** e **BDNF Val66Met** — clássicos de depressão/plasticidade;
  interagem com o eixo de citocina (interferon-alpha em hepatite — Bull;
  BDNF suprimido por IL-1/TNF). São genes de B4/B3 que MODULAM o impacto da
  inflamação, não "genes da neuroinflamação".
- **FKBP5 (HSP90 co-chaperona do GR) — Klengel et al., 2013** — interação
  trauma × alelo de risco, desmetilação dependente de contexto e falha de
  feedback glicocorticoide; liga B12 (trauma) a B2 (HPA). [Humano,
  mecanismo robusto].
- **NR3C1/GR** — metilação associada a adversidade precoce (revisões de
  Meaney/Szyf; contexto do B12).

## 4.4 — Epigenética
- **Metilação de DNA / marcação de histonas** em promotores de TLR, IL6, TNF,
  NLRP3; mudanças associadas a estresse crônico e inflamação (animal e
  pós-morte/ sangue em humano).
- **MicroRNAs** regulando TLR/NF-kB e citocina (ex.: miR-146a, miR-155) —
  mecanístico, pré-clínico.
- **Efeito da idade/inflammaging** no padrão epigenético (B1↔B12).

[ATENÇÃO de espécie/desenho: genética de risco em humano é majoritariamente
associativa (candidata/GWAS); a causalidade é demonstrada em animal (KO/KD);
a inferência causal em humano apoia-se em MR e em intervenções (anti-TNF em
subgrupo inflamado). Heterogeneidade étnica e tamanho amostral devem limitar
a força da alegação.]

[REF_MODULO_04: Bull_2009 | Backlund_2011 | Klengel_2013 | Hung_TLR4 |
MR_CRP | Capuron_2003 | Meaney_epigenetica]

---

# MÓDULO 05 — BIOMARCADORES EXAUSTIVOS

*Organizados por camada/coleta. Para cada: direção, onde medido, força da
associação, especificidade (sempre baixa para marcadores inespecíficos),
natureza (humano). Regra: marcador periférico não equivale a marcador
cerebral; registrar a lacuna periferia↔SNC.*

## 5.1 — Marcadores inflamatórios SÉRICOS/PLASMÁTICOS (periferia)
- **PCR-us (CRP) / VHS / fibrinogênio** — proteínas de fase aguda. Meta-
  análises: elevação em TDM (estudos da PCR; Haapakoski/Osimo); inespecíficos
  (sobe em qualquer inflamação, aguda/crônica). Usar para estratificação de
  subgrupo inflamado, não diagnóstico.
- **IL-6, TNF-α, IL-1β** — citocinas periféricas; meta-análises associam
  TDM; IL-6 a mais replicada. Interleucina sérica não prova produção central.
- **IL-10, razão pró:anti** — estado contra-regulatório.
- **Quimiocinas (MCP-1/CCL2, IL-8/CXCL8)** — meta-análise Leighton;
  inespecíficas.

## 5.2 — Marcadores do eixo quinurenina
- **Razão KYN/TRP (sangue)** — índice de ativação de IDO por citocina;
  elevada em TDM/ansiedade/inflamado (Sublette et al.; meta-análise).
- **Quinurenina e ácido quinolínico (LCR, microdiálise) — [ Steiner, 2011 e
  similares são de VÍTIMAS DE SUICÍDIO/pós-morte, popular suicídio; não
  "TDM geral" — registrar]. QUIN no LCR é o mais diretamente ligado a
  neurotoxidade mas menos acessível.
- **KYNA** (protetor) — medir em paralelo (balanço QUIN/KYNA).

## 5.3 — Marcadores centrais e de imagem
- **TSPO-PET (ligante de translocador mitocondrial)** — sinaliza glia/
  mieloide ativa (Setiawan et al., 2015/2018; Holmes et al., 2018 — este
  último com ideação suicida: popular suicídio). A interpretação de TSPO
  como "microglia ativada" é debatida (TSPO também em astrócito/endotélio).
- **Volumetria/RMf** — redução de substância cinzenta em contexto
  inflamado; conectividade (não é marcador químico, é desfecho).
- **Pós-morte** — microgliose, astroglio GFAP, TLR/NF-κB em regiões límbicas
  (contexto de depressão/suicídio — qualificar).

## 5.4 — Marcadores de BHE/permeabilidade
- **Razão albuminorraquia/LCR-sangue**, **S100B**, **claudina-5** (marcador
  direto em estudo, não disponível rotineiramente); microvesículas.
  Evidência: permeabilidade aumentada em estresse/animal (Menard — camundongo);
  humano associativo e indireto.

## 5.5 — Marcadores da interface imune-endócrina e neurotrófica (B1 cruzado)
- **Cortisol e resistência glicocorticoide** (supressão à dexametasona,
  feedback — B2): inflamação crônica associa-se a falha de supressão.
- **BDNF (sérico/central)**: suprimido por IL-1/TNF (mecanismo de B3);
  BDNF sérico é inespecífico e parcialmente periférico.

## 5.6 — Marcadores intestinais/metabólicos da interface B1↔B7
- **LPS sérico/LBP (LPS-binding protein)**, **Zonulina**, **calprotectina
  fecal** — marcadores de translocação/permeabilidade (evidência humana
  associativa, com variação; calprotectina fecal é intestinal, não
  neural).
- **16S/metabólitos** (SCFAs, indóis) — ver B7.

## 5.7 — O que NÃO constitui marcador diagnóstico
- Nenhum marcador isolado tem especificidade/sensibilidade para
  diagnóstico (PCR/IL-6/quinurenina sobem em dezenas de condições e em
  estresse agudo do saudável). Os marcadores servem para ESTRATIFICAÇÃO
  (subgrupo inflamado) e pesquisa, não para "exame de depressão".
- [Manter o princípio P20/P21: inespecificidade e ausência de corte
  diagnóstico devem estar explícitos no uso clínico].

[REF_MODULO_05: Osimo_2020 | Haapakoski_2015 | Sublette_2011 | Steiner_2011 |
Setiawan_2015 | Holmes_2018 | Menard_2017 | Leighton_2018 | CRP_meta]

---

# MÓDULO 06 — INTERCONEXÕES EXAUSTIVAS COM B2–B16

Para cada conexão: classe (causal|moduladora|associativa|compensatória),
direção, evidência e FORÇA BIOLÓGICA (HIGH/MEDIUM/LOW), com o mecanismo
molecular específico do B1. Detalhe profundo fica na Biblioteca do mecanismo
alvo.

- **B1 ↔ B2 (Eixo HPA / cortisol).** Bidirecional. Cortisol crônico +
  resistência glicocorticoide em monócitos/microglia → falha da trans-repressão
  de NF-κB → citocinas persistem; em paralelo, IL-1/TNF estimulam CRH e
  ativação do eixo (feed-forward). Força: HIGH (humano associativo robusto +
  animal). FKBP5 (Klengel et al., 2013) liga trauma×genética a essa
  resistência.
- **B1 ↔ B3 (Neuroplasticidade/neurogênese).** IL-1β e TNF-α suprimem BDNF/
  CREB e LTP; neuroinflamação reduz neurogênese hipocampal e favorece poda
  por complemento (C1q/C3). Força: HIGH em mecanismo (animal); em humano por
  marcadores/imagem. Complemento: Sekar/Smith (extrapolado de
  esquizofrenia → marcar).
- **B1 ↔ B4 (Monoaminas).** IDO1 desvia triptofano (menos 5-HT) e gera
  QUIN (agonista NMDA); citocinas alteram transporte/reciclagem de dopamina
  e noradrenalina. Força: HIGH (humano quinurenina + animal).
- **B1 ↔ B5 (GABA/glutamato).** QUIN estimula NMDA/ROS; IL-1 modula
  glutamato/astroglia (excitotoxicidade); microglia regula reciclagem de
  glutamato. Força: MEDIUM-HIGH (animal forte; humano indireto).
- **B1 ↔ B6 (Estresse oxidativo).** Bidirecional. ROS/RNS ativam
  NLRP3/NF-κB; inflamassoma gera mais ROS (mtROS). Amplificador chave.
  Força: HIGH (mecânico).
- **B1 ↔ B7 (Eixo intestino-cérebro).** LPS/bactérias translocadas→TLR4;
  SCFAs (butirato) e indóis têm efeito anti-inflamatório/barreira;
  psicobióticos moduladores (pré-clínico). Força: MEDIUM (associativo em
  humano; causal em animal).
- **B1 ↔ B8 (Micronutrientes).** Deficiências (vitD, Zn, Mg, ômega-3)
  sensibilizam vias pró-inflamatórias; nutrientes apoiam resolução (SPMs de
  ômega-3). Força: MEDIUM (ensaios/associação; contextual).
- **B1 ↔ B9 (Mitocôndria).** mtDNA/DAMPs e disfunção mitocondrial ativam
  NLRP3 (imunometabolismo M1); glicólise microglial. Força: HIGH
  (mecânico, pré-clínico).
- **B1 ↔ B10 (Ritmo circadiano/sono).** BMAL1/CLOCK modulam NF-κB e
  produção citocínica; privação de sono e LPS diurno alteram resposta
  inflamatória. Força: MEDIUM (humano associativo + animal).
- **B1 ↔ B11 (Tireoide).** Substrato inflamatório em tireoidites e
  hipotireoidismo; citocinas alteram conversão periférica de hormônios
  tireoidianos (síndrome T3 baixo). Força: MEDIUM.
- **B1 ↔ B12 (Trauma).** Adversidade precoce/TEPT programa priming
  microglial, metilação FKBP5/GR (Meaney/Klengel) e reatividade HPA;
  neuroinflamação como elo duradouro. Força: MEDIUM-HIGH (epigenética
  robusta; marcadores inflamatórios heterogêneos).
- **B1 ↔ B13 (Endocanabinoides).** sinalização endocanabinoide (CB2 em
  glia) é majoritariamente anti-inflamatória/neuroprotetora; modula BHE.
  Força: MEDIUM (pré-clínico forte).
- **B1 ↔ B14 (Neuroesteroides/hormônios).** Estrogênio/DHEA modulam
  inflamassoma e microglia (sex-dimorfismo); glicocorticoide compartilha
  B2. Força: MEDIUM.
- **B1 ↔ B15 (Autofagia/mTOR).** Autofagia degrada NLRP3/pró-IL1β;
  senescência/SASP sustenta inflamação de baixo grau. Força: MEDIUM
  (pré-clínico/geriátrica).
- **B1 ↔ B16 (Neurogênese).** Compartilha B3: inflamassoma/citocina
  deprimem nicho neurogênico hipocampal. Força: MEDIUM (animal).

[REF_MODULO_06: Klengel_2013 | Raison_Miller_HPA | Sekar_2016 |
Dantzer_quinurenina | Meaney_epigenetica | Serhan_resolucao]

---

# MÓDULO 07 — SUBTIPOS E FENÓTIPOS CLÍNICOS DOCUMENTADOS

*Subtipos baseados em mecanismo, com evidência do próprio B1. Não é diagnóstico
e exige ressalva (especificidade baixa).*

- **Fenótipo "inflamado" / citocina-alto (high-CRP/IL-6).** Subgrupo de
  pacientes deprimidos com marcadores periféricos elevados e performance de
  resposta diferenciada (anti-TNF em subgrupo inflamado — Raison et al.,
  2013; meta-análises de estratificação). [Evidência clínica de intervenção
  com ressalva P20].
- **Depressão resistente ao tratamento.** Em média, maior carga
  inflamatória/quinurenina (meta-análises; associação, não causal).
- **Depressão/ansiedade com comorbidade médica inflamatória** (doença autoimune,
  cardíaca, metabólica) — onde o mecanismo é mais convergente.
- **Depressão induzida por IFN-α** — modelo humano de prova de conceito de
  citocina→comportamento (Capuron; Bull — hepatite C).
- **Dimensão ansiedade/TEPT e neuroinflamação** — marcadores
  heterogêneos; TSPO/citocina em subgrupos (Holmes — ideação suicida,
  qualificar).
- **Sickness behavior vs. depressão** — distinção conceitual obrigatória:
  a resposta aguda é adaptativa; a depressão é uma possível transição
  patológica em vulneráveis.

[ATENÇÃO: os marcadores não definem diagnóstico; agrupam perfis para
pesquisa/estratificação. Ver BLOCO_11/12 da Biblioteca].

[REF_MODULO_07: Raison_2013 | Capuron_2003 | CRP_subgroup | Holmes_2018]

---

# MÓDULO 08 — CONTROVÉRSIAS, HETEROGENEIDADE E LACUNAS

## 8.1 — Controvérsias abertas (apresentar ambos os lados)
- **Neuroinflamação central vs periférica em TDM.** Muitos marcadores são
  periféricos (sangue) — a extrapolação ao cérebro é inferencial.
- **Microglia "ativada" vs TSPO.** TSPO-PET não é específico de microglia
  (astrócito/endotélio) e sua densidade cai/ sobe dependendo do ligante.
- **M1/M2 e A1/A2 são simplificações.** Estados reais são contínuos e
  dependentes de contexto (single-cell); não usar como identidades fixas.
- **Causalidade.** Associação robusta; causalidade em humanos depende de
  intervenções (anti-citocina em subgrupo) e MR — ainda não prova que
  inflamação "causa" depressão idiopática.
- **Resolução (SPMs)** — campo emergente, poucos dados humanos.
- **Anti-inflamatório como terapia** — não é recomendação (P20); efeito em
  subgrupo inflamado, sem base para uso geral.

## 8.2 — Heterogeneidade dos estudos (especificar efeitos de confundimento)
Espécie (humano vs roedor), sexo/dimorfismo, idade/inflammaging, medicação
psiquiátrica (os próprios fármacos alteram citocinas), IMC/comorbidade
metabólica, trauma, raça/etnia, estágio de doença e estado agudo vs crônico.

## 8.3 — Lacunas (honestas)
- Falta marcador central específico e tradutável.
- Ausência de prova de resolução/SNM em humanos.
- Desigualdade de cobertura: mais dados de depressão que de ansiedade (TAG/pânico
  mais frouxos — meta-análises de citocina em ansiedade ainda incipientes).
- BHE e translocação em pacientes: evidência indireta.
- Ausência de ensino causal para a maioria dos alvos não-TNF.
- Gásdermina/piroptose em comportamento: pré-clínico apenas.

## 8.4 — O que NÃO extrapolar
Não afirmar que o conjunto de evidências prova diagnóstico ou recomenda
terapêutica; não tratar animal como equivalente humano; não apresentar TSPO
como "microglia ativada" sem ressalva.

[REF_MODULO_08: meta_ansiedade_2026 | Enache_meta_2019 | setola_TSPO |
Haythornthwaite_confunding]

---

# MÓDULO 09 — CHECKLIST DE VERIFICAÇÃO CRUZADA COM O PROMPT 4.2
- [ ] Vias com intermediário/enzima/receptor nomeados (NLRP3→caspase-1→GSDMD→IL-1β).
- [ ] Cascata fisiopatológica com "por quê" em cada passo.
- [ ] Cada mediador (MÓD. 02) está em via no MÓD. 01.
- [ ] Células (MÓD. 03) com subtipo e não agrupadas (microglia/astrócito).
- [ ] Genética marca G (gene)/R (receptor); confundimento de tratamento registrado.
- [ ] Biomarcadores (MÓD. 05) com direção, coleta e especificidade (sem diagnóstico).
- [ ] Conexões B2–B16 com classe/direção/força e mecanismo.
- [ ] Controvérsias (8.1) apresentam os dois lados.
- [ ] Toda evidência tem espécie declarada; extrapolação sinalizada; [EXTRAPOLAÇÃO]/[PRÉ-CLÍNICO].
- [ ] Fonte (Autor, Ano) por item; NENHUM PMID/DOI neste documento (a Busca
      Sistemática por ferramenta resolve os identificadores).
- [ ] Nenhum conteúdo terapêutico prescritivo dentro do corpo mecanístico.

[REF_MODULO_09: —]

---

# MÓDULO 10 — OBSERVAÇÕES EM OUTRAS CONDIÇÕES
Achados do B1 documentados fora de ansiedade/depressão (contexto/extrapolação,
NÃO contam para a cobertura central):
- **Esquizofrenia** — complemento C4 (Sekar); microglia/TSPO; citocinas.
- **Doença de Alzheimer** — inflammaging, A1 (Liddelow), TSPO; extrapolado.
- **Bipolar** — inflamassoma/P2RX7 (Backlund; condição separada).
- **TEPT/trauma** — priming, FKBP5; popular de trauma, parte compartilhada.
- **Autoimune/metabólica/oncológica (IFN)** — inflamação com transtornos de
  humor (prova de conceito).
- **Parkinson/neurodegeneração** — NLRP3/α-sinucleína.
*(Regra: registrar, sem aprofundar no núcleo; o aprofundamento pertence à
Biblioteca do transtorno correspondente)*.

[REF_MODULO_10: Sekar_2016 | Backlund_2011 | Liddelow_2017]

---
# FIM DO GPM_B1 NEUROINFLAMAÇÃO v3

---
> **STATUS DE GERAÇÃO:** Documento auditado e aprovado na **Rodada 1 (geração do GPM)**, conforme o Processo de Geração de Bibliotecas de Conhecimento (mini-rodada: Checklist de Sanidade do GPM, com o Briefing original e o presente GPM). **APROVADO PARA A RODADA 2.** Veredito estrutural (não científico): 11/11 módulos, cobertura total do Briefing, âncoras 10/10, inventário negativo e declaração de busca presentes.
