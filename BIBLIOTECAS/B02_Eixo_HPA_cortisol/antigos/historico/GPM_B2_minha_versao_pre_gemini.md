# GPM_B2 — GERADOR DE PROFUNDIDADE MOLECULAR
## Mecanismo: B2 — EIXO HPA / CORTISOL CRÔNICO (ansiedade e depressão)

> Ferramenta de Rodada 1 (inventário científico, NÃO é a biblioteca). Gera a partir do molde GPM
> v2.0 e do Briefing_B2 (+ FASE1-02 com seções 14–17). Os PMIDs abaixo são âncoras de G1
> (existência via eutils); espécie/direção/força serão auditadas em G2/G3 na Rodada 2/3.

---

## MÓDULO 00 — METADADOS E ESCOPO

ID do mecanismo: B2 — Eixo HPA (hipotálamo–pituitária–adrenal) / cortisol
Condições em escopo: Transtorno Depressivo Maior, Depressão Melancólica/Psicótica, Depressão
Resistente, Depressão Pós-Parto, Transtorno de Ansiedade Generalizada (TAG), Transtorno do
Pânico, Ansiedade Social, TEPT (espectro trauma/ansiedade), TOC, Transtorno de Personalidade
Borderline, Burnout/fadiga crônica.
Corte de conhecimento: busca em tempo real (PubMed/eutils) usada no Briefing (Rodada 0) e a usar
na Rodada 2. Data da busca-base: 2026-09-04/05.
Observação de escopo: regra de delimitação por doença aplicada — biologia básica do eixo entra
(controle de estresse, feedback); achados de outras condições entram só quando há ponte publicada
com ansiedade/depressão, sinalizada.

**Propósito / pontos cegos que este GPM deve trazer à tona (não convergir para o óbvio):**
1. **Bipolaridade do sinal**: hipercortisolismo (melancolia/psicótico) **E** hipocortisolismo
   (TEPT crônico, fadiga, burnout) — não reduzir a "cortisol alto".
2. **Resistência ao receptor de glicocorticoide (GR)** é mais informativa que o nível do ligante.
3. **MR ≠ GR** (alta vs. baixa afinidade; setpoint/resiliência vs. pico/feedback) — razão MR/GR.
4. **Dinâmica temporal** (CAR, slope diurno, cortisol no cabelo, DST/CRH) como lentes distintas.
5. O **freio endocanabinoide** (feedback rápido não-genômico no PVN) e a **circuitaria aferente
   glutamato/GABA** que dispara o eixo antes do CRH.
6. O elo **neuroesteroides/GABA** (alopregnanolona) na depressão pós-parto/ansiedade feminina.
7. A interface **sono REM ↔ HPA noturno** e a **programação precoce × epigenética** (FKBP5/NR3C1).

[REF_MODULO_00: McEwen_2007 | Herman_2016 | Holsboer_2000 | StetlerMiller_2011 | Heim_2000]

---

## MÓDULO 01 — MAPA EXAUSTIVO DE VIAS MOLECULARES

### Via 1 — Eixo neuroendócrino clássico (eixo de estresse)
- Sequência: estímulo → **PVN hipotalâmico** libera **CRH** (e **AVP/vasopressina** co-secretada)
  → hipófise anterior (corticótrofo, receptor CRHR1/MCR2) → **ACTH** → córtex adrenal (zona
  fasciculada) → **cortisol** (corticosterona em roedores) → atua em **GR** e **MR** em todo o
  organismo e no cérebro.
- Feedback negativo: cortisol → GR (e MR) no hipocampo/PVN/hipófise → suprime CRH/ACTH (dois
  modos: **rápido/não-genômico** e **lento/genômico**).
- Papel em ansiedade/depressão: hiperatividade sustentada na melancolia; hiporreatividade/
  hipocortisolismo no TEPT crônico.
- Fase temporal: ativação aguda (minutos, adaptativa) → manutenção crônica (semanas/anos,
  patológica) → resolução com retirada do estressor.
- Origem: revisões-seminais. Natureza: causal (eixo endócrino) / associativa na psicopatologia.
- (McEwen 2007 [17615391]; Herman 2016 [27065163]; Holsboer 2000 [11027914])

### Via 2 — Feedback rápido não-genômico via endocanabinoide (o "freio" do PVN)
- Sequência: estresse → pico de glicocorticoide → ativação não-genômica rápida de GR em
  neurônios do PVN/área → produção retrógrada de **endocanabinoide (2-AG/AEA)** → ativa CB1 em
  terminações glutamatérgicas aferentes → **suprime a liberação de glutamato/CRH** em segundos.
- Papel: é a mecanística do **feedback curto prazo**, distinto do feedback genômico lento do GR.
  Déficit do tônus eCB proposto na ansiedade/TEPT (hiperexcitabilidade amigdalar).
- Natureza: causal em animal/célula (mecanismo); humano associativo/emergente.
- (Hill 2012 [22214537]; Evanson/Tasker 2010 [20702575]; Lutz 2015 [26585799];
  Morena 2016 [26068727])
- **Fronteira:** biologia CB1/CB2 completa é B13; aqui fica o elo HPA.

### Via 3 — Resistência ao glicocorticoide (desacoplamento sinal–resposta)
- Sequência: cortisol elevado + falha do GR em trans-reprimir NF-κB e suprimir CRH →
  inflamação sem freio (ponte B1) e feedback insuficiente.
- Mecanismos: razão **GRα (ativo)/GRβ (dominante-negativo)** reduzida; FKBP5 elevada
  (co-chaperona que reduz translocação/afinidade do GR); fosforilação; metilação NR3C1.
- Papel: glicocorticoide não consegue "desligar" resposta → crônica. Ponte com inflamação
  (Th17, citocinas reduzem sensibilidade do GR).
- (Perrin 2019 [31316402]; Rodriguez 2016 [27643454]; Carvalho 2014 [24424390];
  Khantakova 2023 [38067176]; Kokkinopoulou 2021 [34681832])

### Via 4 — Circuitaria aferente do PVN (glutamato excita / GABA inibe) — B2 puro
- Estresse excita o PVN via **glutamato** (amígdala medial/BNST, núcleo do trato solitário);
  é freado por tônus **GABAérgico** (peri-PVN, hipocampo via MR/GR). A hiperatividade amigdalar
  (ansiedade/TEPT) liga o eixo **por cima** do feedback hormonal.
- O **BNST** (núcleo leito da estria terminal) diferencia excitação/inibição do PVN por subnúcleo.
- (Jamieson 2017 [28872712]; Kakizawa 2016 [27540587]; Choi 2008 [18039788];
  Bains 2015 [26087679]; Herman 1997 [9023876])

### Via 5 — Metabolismo tecidual: 11β-HSD
- **11β-HSD1** ativa cortisona→cortisol em tecidos (fígado, cérebro); **11β-HSD2** inativa.
  Amplificação local de sinal independente do nível sérico.
- (Gallezot 2019 [30877174] PET; Wheelan 2018 [29306773])

### Via 6 — Programação precoce × epigenética
- Adversidade infantil → metilação/desmetilação de NR3C1 e **FKBP5** (alelo-específica,
  trauma-dependente) → reajuste do setpoint do eixo no adulto.
- (Klengel 2013 [23201972]; Binder 2009 [19560279]; Mendonça 2023 [36933666];
  Logue 2020 [32171335])

[REF_MODULO_01: McEwen_2007 | Herman_2016 | Holsboer_2000 | Hill_2012 | Evanson_2010 |
Lutz_2015 | Perrin_2019 | Carvalho_2014 | Jamieson_2017 | Choi_2008 | Bains_2015 |
Gallezot_2019 | Klengel_2013]

---

## MÓDULO 02 — MAPA DE MEDIADORES / RECEPTORES

- **CRH (CRF)** e receptor **CRHR1** (pituitária/SNC; alvo farmacológico — ver Módulo 09);
  CRHR2 com papéis distintos.
- **AVP/vasopressina** (V1b na hipófise): co-secretada, amplifica ACTH sob estresse crônico.
- **ACTH**: hormônio trófico da adrenal.
- **Cortisol** (corticosterona roedor): ligante final.
- **GR (NR3C1)**: isoformas **GRα** (ativo) e **GRβ** (dominante-negativo); translocação nuclear;
  trans-repressão de NF-κB.
- **MR (NR3C2)**: alta afinidade, ocupa a [cortisol] basal; setpoint/resiliência; razão MR/GR.
- **FKBP5 (FKBP51)** e chaperonas (HSP90): regulam afinidade/traffic do GR.
- **CBG (globulina ligadora de corticosteroides)**: fração livre ativa.
- **DHEA(S)**: antagonista neuroativo do cortisol; razão DHEA:cortisol como marcador.
- **Neuroesteroides**: **alopregnanolona** (metabólito da progesterona → modulador GABA-A);
  pregnanolona; elo com humor feminino/pós-parto.
- **11β-HSD1/2**: ativação/inativação tecidual.
- **Endocanabinoides AEA/2-AG** (ver Via 2; CB1).
- Direção em ansiedade/depressão: cortisol elevado na melancolia/agudo; reduzido/achatado no TEPT
  crônico; GR resistente; FKBP5↑ com trauma; alopregnanolona↓ associada a ansiedade/pós-parto.
- (ter Heegde 2015 [25459896]; de Kloet 2016 [26970338]; Wingenfeld 2019 [30243757];
  Schüle 2014 [24215796]; Belelli 2005 [15959466]; Maguire 2019 [30906252])

**Inventário negativo:** marcadores de cortisol isolado (uma medida) **não** definem o
mecanismo — a dinâmica e a sensibilidade do receptor superam o nível pontual; registrado para não
sustentar afirmação binária a partir de uma coleta única.

[REF_MODULO_02: deKloet_2016 | terHeegde_2015 | Wingenfeld_2019 | Schüle_2014 | Belelli_2005]

---

## MÓDULO 03 — MAPA DE CÉLULAS / CIRCUITOS / ESTRUTURAS

- **PVN hipotalâmico**: núcleo paraventricular, neurônios CRH (núcleo de saída do eixo).
- **Hipófise anterior** (corticótrofos) e **córtex adrenal** (fasciculada/reticular).
- **Hipocampo**: rico em GR/MR; feedback negativo; vulnerável a cortisol crônico (atrofia).
- **Amígdala** (BLA/medial): excita o eixo; central na ansiedade/TEPT; modular por eCB e IL-17/IL-18.
- **BNST (núcleo leito da estria terminal)**: excitação difusa/ansiedade antecipatória; controla PVN.
- **Córtex pré-frontal (CPFdl/Cg)**: regulação superior (feedback cognitivo); atrofiado/hipoativo.
- **Hipotálamo supraquiasmático (SCN)**: acoplamento circadiano (interface B10).
- Periferia: adipócitos, hepatócitos (11β-HSD), imunócitos (GR).
- (Sapolsky 2000 [11015810]; Uno 1994 [7729802]; Brown 1999 [10481830]; Choi 2008 [18039788])

[REF_MODULO_03: Sapolsky_2000 | Uno_1994 | Brown_1999 | Choi_2008]

---

## MÓDULO 04 — GENÉTICA / EPIGENÉTICA / POLIMORFISMOS

- **FKBP5 (rs1360780 e outros)**: interação alelo × abuso infantil → desmetilação dependente de
  trauma → risco psiquiátrico/TEPT (Klengel 2013, Nat Neurosci).
- **NR3C1**: metilação do promotor por cuidados/estresse precoce; resistência a GR.
- **CRHR1/CRHBP**: variantes no sistema CRH; resposta a antidepressivo.
- **NR3C2 (MR)**: variantes e setpoint; resiliência.
- EWAS de TEPT (Logue 2020); metilação sexo-específica FKBP5 (Lee 2018 [30036794]).
- Natureza: interação gene×ambiente (não risco genético puro).
- (Klengel 2013 [23201972]; Szczepankiewicz 2014 [24856550]; Licinio 2004 [15365580];
  Binder 2009 [19560279]; Logue 2020 [32171335]; Zennaro 2017 [28348114])

[REF_MODULO_04: Klengel_2013 | Binder_2009 | Szczepankiewicz_2014 | Logue_2020 | Lee_2018]

---

## MÓDULO 05 — BIOMARCADORES (dinâmica > mancha única)

- **Cortisol matinal/serum/salivar** (`exame_cortisol_matinal`).
- **CAR — cortisol awakening response** (4 pontos, `exame_cortisol_salivar_4pts`).
- **Slope diurno** (declínio ao longo do dia).
- **Cortisol no cabelo** (acumulado mensal; Stalder 2017 meta [28135674]; Psarraki 2021 [33310696]).
- **Cortisol urinário 24h** (`exame_cortisol_urinario_24h`).
- **DST** (dexametasona; meta Ribeiro 1993 [8214170]) e **DST/CRH combinado** (Ising 2005
  [15950349], prediz recaída/resposta).
- **ACTH** (`exame_acth`); **DHEA(S)** (`exame_dhea_s`) e razão DHEA:cortisol.
- **DUTCH test** (`exame_dutch_test`) e ensaio de sensibilidade do GR (Baes 2012 [28183380]).
- Marcadores indiretos: **PCR/IL-6** (resistência a GR co-ocorre com inflamação).
- Confundidores: horário de coleta, sono, medicação, índice 11β-HSD, CBG.
- (Ribeiro 1993 [8214170]; Ising 2005 [15950349]; Stalder 2017 [28135674];
  Jopling 2023 [40654374]; Staufenbiel 2013 [23253896])

[REF_MODULO_05: Ribeiro_1993 | Ising_2005 | Stalder_2017 | Jopling_2023 | Staufenbiel_2013]

---

## MÓDULO 06 — INTERCONEXÕES (CROSSTALK B1–B16)

> Só entram conexões com publicação específica em ansiedade/depressão (ou ponte). Conexões
> apenas biologicamente plausíveis vão ao Módulo 10.

### B2 ↔ B1 (Neuroinflamação) — DUAL e forte
- Citocinas (IL-1β, IL-6, TNF) induzem resistência a GR (falta de feedback → cortisol não
  desliga NF-κB); IFN-α reduz o feedback do HPA em humanos.
- (Perrin 2019 [31316402]; Khantakova 2023 [38067176]; Felger/IFN-HPA [26703263];
  Hage 2024 [39333855])

### B2 ↔ B3 (Neuroplasticidade)
- Cortisol crônico → supressão de BDNF, retração dendrítica hipocampal/CPF; atrofia.
- (Sapolsky 2000 [11015810]; Brown 1999 [10481830]; McEwen 2001 [12000027])

### B2 ↔ B4 (Monoaminas)
- GR modula expressão de SERT/MAO; CRH altera seratonina/dopamina; resistência a GR
  associa-se a não resposta antidepressiva.
- (Holsboer 2000 [11027914])

### B2 ↔ B5 (GABA/Glutamato)
- Alopregnanolona (GABA-A+) e tônus GABAérgico do PVN controlam CRH; glutamato (amígdala/BNST)
  excita. (Choi 2008 [18039788]; Belelli 2005 [15959466]; Schüle 2014 [24215796])

### B2 ↔ B6/B9 (Estresse oxidativo/Mitocôndria)
- Cortisol crônico aumenta ROS; dano mitocondrial na fisiopatologia (estudos celulares).

### B2 ↔ B7 (Eixo intestino–cérebro)
- Microbiota modula desenvolvimento/reatividade do HPA; probióticos reduzem cortisol (meta
  dose-resposta). (Rusch 2023 [37404311]; Gandomkar 2026 [42032711]; Misiak 2020 [32335265])

### B2 ↔ B10 (Circadiano/Sono)
- Relógio/SCN acopla ritmo do cortisol; **fragmentação do sono REM ↔ hiperativação noturna
  do HPA** (bidirecional). (Steiger 2002 [12531148]; Buckley 2005 [15728214];
  Palagini 2013 [23391633]; Sgoifo 2006 [16154708])

### B2 ↔ B11 (Tireoide)
- Eixo de resposta compartilhado; disfunção tireoideana em estresse (rT3/eutireoide-adoentado).
  (Rupprecht 1989 [2912508])

### B2 ↔ B12 (Neurobiologia do trauma)
- Trauma precoce reajusta o setpoint via FKBP5/NR3C1; hipocortisolismo TEPT.
  (Klengel 2013 [23201972]; Heim 2000 [10633533]; Meewisse 2007 [17978317])

### B2 ↔ B13 (Sistema endocanabinoide)
- eCB = freio rápido do PVN (feedback não-genômico); déficit na ansiedade/TEPT.
  (Lutz 2015 [26585799]; Morena 2016 [26068727]; Gunduz-Cinar 2021 [32976951];
  Hill 2012 [22214537])

### B2 ↔ B14 (Neuroesteroides/Hormônios)
- Alopregnanolona (progesterona→GABA-A) e DHEA; depressão pós-parto, diferenças sexuais.
  (Schüle 2014 [24215796]; Meltzer-Brody 2018 [30177236]; Hantsoo 2023 [38149098];
  Hodes 2024 [37855285]; Maguire 2019 [30906252])

### B2 ↔ B15 (Autofagia/mTOR)
- glicocorticoide modula mTOR/autofagia em contexto neuroplástico (área a aprofundar).

### B2 ↔ B16 (Neurogênese)
- cortisol crônico suprime neurogênese hipocampal (indireto via B3) [gap].

[REF_MODULO_06: Perrin_2019 | Khantakova_2023 | Sapolsky_2000 | Choi_2008 | Belelli_2005 |
Rusch_2023 | Gandomkar_2026 | Steiger_2002 | Buckley_2005 | Palagini_2013 | Klengel_2013 |
Heim_2000 | Lutz_2015 | Schüle_2014 | MeltzerBrody_2018 | Hantsoo_2023]

---

## MÓDULO 07 — SUBTIPOS E DIFERENÇAS TRANSIDIAGNÓSTICAS (HETEROGENEIDADE)

Padrões HPA por transtorno (meta reatividade: Zorn 2017 [28012291]):
- **Depressão melancólica/psicótica**: hiper- (Cushing-like, DST não-suprimível).
- **Depressão atípica/crônica**: variável; predomínio de reatividade achatada.
- **TEPT crônico**: hipocortisolismo/hiporreatividade (Heim 2000; Meewisse 2007 [17978317];
  Vythilingam 2010 [19766403]).
- **TOC**: padrão HPA distinto (meta Sousa-Lima 2019 [31540796]).
- **Borderline**: hiporreatividade semelhante ao TEPT (Drews 2019 [30500331]; Thomas 2019 [30557762]).
- **Burnout/fadiga crônica**: "fadiga adrenal" é mito (Cadegiani 2016 [27557747] desmente);
  o real é exaustão/achatamento dinâmico.
- **Ansiedade (TAG/pânico/social)**: reatividade aumentada mas heterogênea (Zorn 2017;
  Vreeburg 2010 [20190128]).
- Sexo/fase hormonal: padrões diferentes (Hantsoo 2023 [38149098]).

[REF_MODULO_07: Zorn_2017 | Heim_2000 | Meewisse_2007 | SousaLima_2019 | Drews_2019 |
Thomas_2019 | Cadegiani_2016 | Vreeburg_2010 | Hantsoo_2023]

---

## MÓDULO 08 — TRADUÇÃO FARMACOLÓGICA (LIÇÕES)

- **Antagonistas CRF1**: bem-sucedidos em animal, **falharam em grandes ensaios humanos** para
  depressão/ansiedade — caso-documentado de fracasso translacional (Spierling 2017 [28265716];
  Ising 2007 [18179304]; Kehne 2002 [12769601]).
- **Anti-glicocorticoides**: **mifepristona (RU-486)** com sinal na depressão psicótica
  (Blasey 2009 [19318138], DeBattista 2006 [16889757], Cochrane Kruizinga 2021 [34875106]);
  metirapona/ketoconazol históricos (Wolkowitz 1999 [10511017]).
- **Brexanolona (alopregnanolona IV)**: RCT positivo na depressão pós-parto severa
  (Meltzer-Brody 2018 [30177236], *Lancet*); zuranolona oral.
- Normalização do HPA com recuperação/antidepressivo; hidrocortisona precoce pode reduzir
  risco de TEPT (Sijbrandij 2015 [26360285]; Kothgassner 2021 [33626392]) — evidência em construção.

[REF_MODULO_08: Spierling_2017 | Blasey_2009 | DeBattista_2006 | Kruizinga_2021 |
MeltzerBrody_2018 | Sijbrandij_2015 | Wolkowitz_1999]

---

## MÓDULO 09 — CONTROVÉRSIAS / LACUNAS / INVENTÁRIO NEGATIVO

- **"Fadiga adrenal" NÃO existe** como entidade clínica (Cadegiani 2016): desmentir como
  diagnóstico; o fenômeno real é exaustão/dinâmica do eixo.
- **Hipocortisolismo vs. hipercortisolismo** aparentemente paradoxais: dependem de
  fase (aguda=alta; crônica/TEPT=baixa), tipo de medida e reatividade — não um valor fixo.
- Um único cortisol NÃO decide: a dinâmica (CAR/slope/DST) e a resistência do GR superam o nível.
- CRF1-anagonista: alvo promissor em animal que fracassou em humano — cautela na tradução.
- **Em construção/fracas**: correlação BDNF-Val66Met x HPA (Shalev 2009 [18990498]);
  11β-HSD1 como alvo na depressão (PET viável, ensaios limitados).
- Correções de PMID necessárias (as referências vão ser re-validadas no G1 da Rodada 2):
  buscar pelo nome do autor/título, NÃO copiar PMID de listas (verificar Cullinan/Herman PVN,
  Flak BNST, Meerlo sono com fonte real).

[REF_MODULO_09: Cadegiani_2016 | Shalev_2009 | Gallezot_2019 | Spierling_2017]

---

## MÓDULO 10 — ACHADOS RELEVANTES FORA DO ESCOPO DE DOENÇA

> **Nota de natureza do Módulo 10:** os itens abaixo são **amostra ilustrativa** do que fica
> fora do corpo principal — não é uma triagem exaustiva. Achados robustos em outra condição sem
> ponte publicada com ansiedade/depressão são registrados aqui e não entram na contagem de cobertura.


- Biologia básica de corticosteroides sem contexto direto de ansiedade/depressão (fisiologia de
  outras glândulas, adrenal em doenças não-psiquiátricas) — registra-se aqui, não entra no corpo
  principal nem na contagem de cobertura do mecanismo.
- Achados em Cushing/Addison orgânicos: usados como prova de conceito hormonal (relevantes para
  a interface), mas são endocrinopatias, não o transtorno psiquiátrico.
