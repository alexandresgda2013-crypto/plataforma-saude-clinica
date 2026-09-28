# GERADOR DE PROFUNDIDADE MOLECULAR (GPM)
## Mecanismo: B4 — Deficiência de Monoaminas (Serotonina/Noradrenalina/Dopamina) em Ansiedade e Depressão
### Módulos 00–10 (molde v2.0)

> Citações em (Autor, Ano); evidência/natureza/maturidade ao fim dos itens; âncora
> `[REF_MODULO_XX]` por módulo. PMIDs verificados no **Briefing B4** (31 âncoras, G1 por eutils);
> G1→G2→G3 na Rodada 2. **Sem medicamentos como conteúdo terapêutico** (proibição do molde): fármacos
> antidepressivos/IMAOs/etc. entram apenas como **sinal experimental/histórico** que revela o
> mecanismo (prova farmacológica, latência, viés de publicação); eficácia/prescrição é da Biblioteca.
> A hipótese clássica "baixa serotonina" entra como **história e controvérsia**, não como fato vigente.

---

## MÓDULO 00 — METADADOS E ESCOPO

- **ID:** B4 — Monoaminas (5-HT, noradrenalina/NA, dopamina/DA) como neuromoduladores.
- **Condições em escopo:** TDM, depressão resistente, distimia, TAG, pânico, ansiedade social, TEPT,
  TOC (quando no espectro ansioso). Bipolar entra rotulado.
- **Corte de conhecimento:** busca em tempo real **2026-09-05/06** via PubMed/eutils; consolidação
  Arena+Claude/Gemini + 3 eixos de fronteira (optogenética, scRNA-seq, outros moduladores); 31
  âncoras; a auditoria corrigiu 2 PMIDs trocados (Vetulani & Sulser e Blier & de Montigny),
  todos verificados no Briefing.
- **Observação de escopo:** a monoamina é **neuromodulador/gating**, não "estoque de conteúdo". A
  farmacologia de receptor (5-HT2A/mGlu2, GABA) tem interface com B5; o desfecho plástico
  (BDNF/sinapse) é B3; o MAO de membrana mitocondrial toca B9. 5-HT entérica/periférica (Yano) é
  B7/periferia, com ponte indireta ao SNC.

**Propósito (direção de atenção):** o levantamento genérico para em "baixa serotonina = depressão"
e no transportador SERT. Os pontos cegos: (i) a hipótese clássica é **histórica e derrubada**
(depleção não rebaixa humor de sadio; latência semanas vs bloqueio em horas); (ii) as monoaminas são
**três sistemas dissociáveis** (5-HT humor/ansiedade/compulsão; NA/locus coeruleus arousal/energia;
DA/mesolímbica recompensa/esforço/erro de predição); (iii) o **paradoxo temporal** (dessensibilização
de auto-receptor 5-HT1A; downregulation β-adrenérgica); (iv) a DA como **código temporal
fásico/tônico em microcircuitos**, não concentração (optogenética); (v) heterodímeros (5-HT2A–mGlu2),
**TAAR1**, farmacogenômica CYP, neuropeptídeos (NPY/galanina); (vi) a **controvérsia ativa**
(Moncrieff vs Jauhar) e a eficácia **real mas modesta/com viés** (Cipriani; Turner).

[REF_MODULO_00: Briefing_B4_2026 | Molde_GPM_v2.0 | Schildkraut_1965 | Ruhe_2007]

---

## MÓDULO 01 — MAPA EXAUSTIVO DE VIAS MOLECULARES

### Via 1 — Síntese, degradação e recaptada das três monoaminas
- **Sequência (5-HT):** triptofano → **TPH2 (neuronal; TPH1 periférica)** + AAAD → 5-HT →
  armazenado em vesícula; liberado; recaptado por **SERT/5-HTT (SLC6A4)**; degradado por
  **MAO-A** (membrana mitocondrial externa) e COMT. (DA): tirosina → **TH** → L-DOPA → AAAD → DA;
  recaptado por **DAT (SLC6A3)**; **DβH** converte DA→NA; NA recaptada por **NET (SLC6A2)**;
  degradação MAO-A/B + COMT (**Val158Met**).
- **Papel:** o nível na fenda não é a variável causal direta (ver Via 3/4); a degradação por **MAO-A
  está elevada no cérebro deprimido por PET** (Meyer et al., 2006) [humano imagem; associativo; bem
  suportado].
- [humano+animal+básica]; natureza: mecanística; maturidade: muito estabelecido (bioquímica).
- (Meyer, 2006)

### Via 2 — Receptores e auto-receptores (gating pré/pós-sináptico)
- **Sequência:** 5-HT atua em **5-HT1A** (auto-receptor somatodendrítico da rafe), 5-HT1B
  (terminal), 5-HT2A/2C, 5-HT3…5-HT7; NA em α1/**α2(auto)**/β; DA em D1-like e **D2/D3
  auto-receptores**. Os auto-receptores freiam a liberação.
- **Papel:** a **dessensibilização do 5-HT1A** somatodendrítico e a **downregulation β-adrenérgica**
  explicam o paradoxo temporal (bloqueio agudo da recaptação ≠ resposta clínica de semanas)
  (Blier & de Montigny, 1994; Vetulani & Sulser, 1975) [eletrofisiologia/animal; mecanístico;
  muito estabelecido]. **Heterodímero 5-HT2A–mGlu2** altera cascatas além da concentração
  (González-Maeso — `[G1]` a confirmar); **TAAR1** regula tom pré-sináptico de DA/5-HT
  (Revel — `[G1]`).
- [animal/eletrofisiologia]; natureza: mecanística/contributiva; maturidade: bem suportado
  (dessensibilização), emergente (heterodímero/TAAR).
- (Blier & de Montigny, 1994; Vetulani & Sulser, 1975)

### Via 3 — O paradoxo temporal e a "destrava" da plasticidade
- **Sequência:** bloqueio agudo do transportador → ↑ monoamina na fenda (horas) → adaptações
  lentas: dessensibilização de auto-receptores, sinalização **BDNF/TrkB**, neurogênese → resposta
  clínica (semanas). A monoamina **destrava a janela plástica**; a experiência/psicoterapia
  preenche (interface B3).
- **Papel:** depleção aguda de monoaminas **não rebaixa o humor de sadios**, só de vulneráveis/
  remitidos (Ruhé et al., 2007, meta; Homan & Neumeister, 2015; Harrison et al., 2004) [humano
  experimental; evidência contra o "estoque baixo"; bem suportado]. BDNF na via DA mesolímbica sob
  social defeat (Berton et al., 2006) [animal; causal/plasticidade].
- [humano experimental + animal]; natureza: contributiva/modulatória; maturidade: bem suportado.
- (Ruhé, 2007; Homan & Neumeister, 2015; Harrison, 2004; Berton, 2006)

### Via 4 — DA como código temporal: recompensa, esforço, erro de predição
- **Sequência:** neurônios DA da VTA disparam em **modo tônico** (tom basal) e **fásico (burst,
  ms)** diante de recompensas/erro de predição; o burst fásico é o sinal que direciona
  comportamento.
- **Papel:** DA é sinal de **erro de predição** (Schultz et al., 1997); o **disparo fásico é
  suficiente para condicionar** comportamento (Tsai et al., 2009, optogenética) [neurofisiologia/
  animal; causal; bem suportado]. Anedonia não é "baixa DA" mas alteração de esforço/erro de
  predição (Salamone — `[G1]`).
- [animal/neurofisiologia]; natureza: causal (código); maturidade: bem suportado.
- (Schultz, 1997; Tsai, 2009)

### Via 5 — NA/locus coeruleus: arousal, vigilância, estresse
- **Sequência:** o **locus coeruleus (LC)** emite NA em modo tônico vs burst; o burst muda o estado
  da rede (vigília, orientação, resposta de estresse).
- **Papel:** o LC molda o hipocampo sob estresse (Privitera et al., 2024, eLife); o modo tônico vs
  burst do LC reconfigura redes (Grimm et al., 2024, *Nat Neurosci*); LC na ansiedade patológica
  (Morris et al., 2020) [animal opto/quimiogenético + revisão; causal/emergente].
- [animal + revisão]; natureza: mecanística; maturidade: bem suportado/emergente.
- (Privitera, 2024; Grimm, 2024; Morris, 2020)

### Via 6 — Modulação transcricional e identidade celular sob estresse (scRNA-seq)
- **Sequência:** estresse severo altera o transcriptoma de neurônios da rafe/LC/VTA e de glia;
  habituação transcricional ao estresse (Waag et al., 2025, *Nat Commun*) [single-cell animal;
  emergente]; identidade de subtipos da rafe (Okaty — `[G1]`).
- **Natureza:** mecanística/emergente; liga estado de estresse a subtipos monoaminérgicos.
- (Waag, 2025)

### Via 7 — Outros moduladores em tempo real que interagem com monoaminas
- **Endocanabinoides (CB1, 2-AG/AEA):** modulam recompensa/liberação (Parsons & Hurd, 2015) —
  B13. **Opioides endógenos:** neurônios μ-opioide na rafe dorsal (interface 5-HT; Welsch et al.,
  2023); **dinorfina/κ-opioide** e estresse (Wang et al., 2023) — B13/anedonia. **Neuroesteroides**
  (alopregnanolona/GABA-A) no estresse reprodutivo (Maguire & Mody, 2007; brexanolone na depressão
  pós-parto, Meltzer-Brody, 2018) — B14. **Neuropeptídeos NPY/galanina** modulam liberação sob
  estresse crônico (`[G1]`).
- [animal + humano (brexanolone RCT)]; natureza: modulatória; maturidade: emergente.
- (Parsons & Hurd, 2015; Welsch, 2023; Wang, 2023; Maguire & Mody, 2007; Meltzer-Brody, 2018)

**Autoauditoria M01:** o mecanismo é apresentado como gating/modulação, não déficit de estoque; a
hipótese clássica e sua queda estão explícitas; três monoaminas dissociadas; código temporal da DA
coberto por optogenética. Fármacos só como prova experimental.

[REF_MODULO_01: Meyer_2006 | Blier_deMontigny_1994 | Vetulani_Sulser_1975 | Ruhe_2007 |
Homan_Neumeister_2015 | Harrison_2004 | Berton_2006 | Schultz_1997 | Tsai_2009 | Privitera_2024 |
Grimm_2024 | Morris_2020 | Waag_2025 | Parsons_Hurd_2015 | Welsch_2023 | Wang_dinorfina_2023 |
Maguire_Mody_2007 | Meltzer-Brody_2018]

---

## MÓDULO 02 — MAPA EXAUSTIVO DE MEDIADORES MOLECULARES

**Categorias:** Enzimas de síntese/degradação · Transportadores · Receptores · Moduladores.

- **Síntese:** TPH2 (neuronal) vs TPH1 (periferia), TH, AAAD, DβH.
- **Degradação:** **MAO-A** (elevada por PET na TDM, Meyer 2006), MAO-B, **COMT (Val158Met)**.
- **Transportadores:** **SERT/SLC6A4 (5-HTTLPR)**, **NET/SLC6A2**, **DAT/SLC6A3**.
- **Receptores 5-HT:** 5-HT1A (auto somatodendrítico), 5-HT1B (auto terminal), 5-HT2A, 5-HT2C,
  5-HT3…5-HT7.
- **Receptores NA/DA:** α1, **α2(auto)**, β; **D1-like (D1/D5)**, **D2-like (D2/D3/D4; auto
  D2/D3)**.
- **Moduladores:** TAAR1; heterodímero 5-HT2A–mGlu2; NPY, galanina; endocanabinoides;
  μ/κ-opioides; neuroesteroides; enzimas de metabolismo de fármaco **CYP2D6/CYP2C19**
  (farmacogenômica da biodisponibilidade — não é mediador neural, mas explica pseudorrefratariedade).
- **Marcadores periféricos:** 5-HIAA (LCR), 5-HT plaquetária/entérica (~95% é periférica).

### Inventário negativo (mediadores/hipóteses SEM associação causal consistente)
- **"Baixa serotonina medida = depressão":** sem evidência de 5-HT baixa causal in vivo; depleção
  não rebaixa sadio (Ruhé, 2007); a revisão guarda-chuva (Moncrieff et al., 2022) não encontra
  suporte à hipótese — **disputa ativa** com a réplica metodológica (Jauhar et al., 2023); entra
  como controvérsia, não veredito.
- **5-HTTLPR × estresse → depressão:** achado inicial (Caspi et al., 2003) **não replicou** em
  meta (Risch et al., 2009; Culverhouse et al., 2018). O mesmo polimorfismo/MAOA-uVNTR para
  ansiedade (Lesch et al., 1996; Caspi 2002) é terreno frágil/efeito pequeno — lição de cautela.
- **5-HT periférica/plaquetária = 5-HT cerebral:** ~95% da 5-HT é entérica/plaquetária; Yano
  (2015) é 5-HT **entérica** (cólon), ponte ao SNC indireta.
- **"Anedonia = baixa dopamina":** é alteração de esforço/erro de predição/código fásico, não
  concentração (Schultz, 1997; Tsai, 2009).
- **5-HTP/triptofano/SAM-e "recompõem serotonina":** biodisponibilidade no SNC e efeito
  transitório; não é repor estoque.
- **MAOA-PET sem ajuste de tabaco:** tabagismo reduz MAO-A fortemente (confundidor).

[REF_MODULO_02: Meyer_2006 | Ruhe_2007 | Moncrieff_2022 | Jauhar_2023 | Caspi_2003 | Risch_2009 |
Culverhouse_2018 | Lesch_1996 | Yano_2015 | Schultz_1997 | Tsai_2009]

---

## MÓDULO 03 — MAPA EXAUSTIVO DE TIPOS CELULARES E ESTRUTURAS

### 3.1 Tipos celulares
- **Neurônios serotoninérgicos da rafe (dorsal/mediana):** subtipos moleculares distintos
  (scRNA, Okaty `[G1]`); alvo de μ-opioide (Welsch, 2023); auto-receptor 5-HT1A.
- **Neurônios noradrenérgicos do locus coeruleus:** modos tônico/burst (Grimm, 2024;
  Privitera, 2024); arousal/estresse (Morris, 2020).
- **Neurônios dopaminérgicos da VTA/substância negra:** vias mesolímbica (recompensa) e
  mesocortical (cognição/ânimo); código fásico (Tsai, 2009).
- **Neurônios-alvo pós-sinápticos (CPF, NAc, amígdala, hipocampo):** expressam os receptores e
  executam plasticidade (B3).
- **Células enterocromafins/plaquetas:** 5-HT periférica (Yano, 2015) — não neuronais centrais.

### 3.2 Estruturas/circuitos
- **Rafe, locus coeruleus, VTA/SN:** núcleos de origem.
- **Vias mesolímbica/mesocortical e coeruleo-cortical:** projeções de DA/NA.
- **NAc (recompensa/anedonia; D1/D2), CPFvm (humor/extinção), amígdala (medo/ansiedade),
  hipocampo (cognição/estresse):** alvos da modulação.
- **Estrutura legível em humano:** PET de **MAO-A** (Meyer, 2006) e PET de SERT/NET/DAT
  (ocupação); neuroimagem de rede.

[REF_MODULO_03: Welsch_2023 | Grimm_2024 | Privitera_2024 | Morris_2020 | Tsai_2009 | Yano_2015 |
Meyer_2006]

---

## MÓDULO 04 — VARIABILIDADE GENÉTICA E EPIGENÉTICA EXAUSTIVA

*Teste de escopo aplicado.*

**Genética:**
- **5-HTTLPR (SLC6A4):** Caspi et al. (2003) → interação com estresse; **não replicado** (Risch,
  2009; Culverhouse, 2018). [humano; associação frágil].
- **MAOA-uVNTR:** Caspi et al. (2002) × maus-tratos; Lesch et al. (1996) traços de ansiedade —
  efeito pequeno, cautela.
- **COMT Val158Met:** modula degradação de DA/NA; variante de risco, não marcador de estado.
- **TPH2 loss-of-function:** variantes raras associadas (Zhang — `[G1]`); **TAAR1**, CANLI/Lesch
  (`[G1]`).
- **CYP2D6/CYP2C19:** metabolizador lento/rápido altera exposição ao fármaco (farmacogenômica).

**Epigenética:**
- Metilação de SERT/genes monoaminérgicos por estresse precoce; regulação transcricional por
  estresse (Waag, 2025 scRNA). Lastro epigenético humano direto em humor: `[emergente]`.

[REF_MODULO_04: Caspi_2003 | Risch_2009 | Culverhouse_2018 | Caspi_2002 | Lesch_1996 | Waag_2025]

---

## MÓDULO 05 — BIOMARCADORES EXAUSTIVOS
*(catálogo — sem protocolo/valor de corte)*

### 5.1 Periféricos
- **5-HIAA no LCR / 5-HT plaquetária:** marcadores clássicos; periféricos, confundidos por dieta/
  ritmo/ativação plaquetária; especificidade baixa.
- **Metabolitos/transportadores em sangue:** NET/DAT/SERT em células; inespecíficos.
- **Genótipo 5-HTTLPR/MAOA/COMT/CYP:** covariáveis de risco/metabolização, **não** marcadores de
  estado/diagnóstico.

### 5.2 Centrais/liquor
- **5-HIAA liquórico:** histórico; baixa especificidade.

### 5.3 Neuroimagem (o canal humano mais forte)
- **PET de MAO-A:** elevado na TDM (Meyer, 2006) — **ajustar tabagismo** (reduz MAO-A).
- **PET de SERT/NET/DAT (ocupação/ligante):** ocupação por fármaco; genótipo basal; DAT
  confundido por tabaco.
- **Princípio:** não há biomarcador monoaminérgico validado para diagnóstico; PET é pesquisa;
  depleção é teste de vulnerabilidade, não de diagnóstico.

[REF_MODULO_05: Meyer_2006 | Yano_2015]

---

## MÓDULO 06 — INTERCONEXÕES EXAUSTIVAS COM B1–B16

- **B4↔B3 (plasticidade/BDNF) — HIGH.** monoamina dessensibiliza auto-receptor → BDNF/TrkB →
  neurogênese/sinapse; a monoamina **destrava a janela plástica**. (Blier, 1994; Berton, 2006).
- **B4↔B5 (GABA/glutamato/receptor) — HIGH.** heterodímero 5-HT2A–mGlu2; NMDAR e glutamato na
  resposta rápida; receptor é B5, gating é B4. (`[G1]` González-Maeso).
- **B4↔B2 (HPA/estresse) — HIGH.** LC/NA e rafe/5-HT respondem a cortisol/estresse; estresse
  crônico altera liberação (Morris, 2020; Caspi×estresse).
- **B4↔B13 (endocanabinoide/opioide) — MEDIUM-HIGH.** CB1 modula liberação; μ na rafe;
  dinorfina/κ na anedonia por estresse (Parsons & Hurd, 2015; Welsch, 2023; Wang, 2023).
- **B4↔B1 (neuroinflamação) — MEDIUM.** citocinas modulam transportadores/síntese; interface
  doença-do-comportamento.
- **B4↔B9 (mitocôndria) — MEDIUM.** MAO é enzima de membrana mitocondrial externa (gera H₂O₂);
  serotonina regula biogênese via 5-HT2A/SIRT1-PGC-1α (cross B9).
- **B4↔B14 (neuroesteroides) — MEDIUM.** alopregnanolona/GABA e estresse reprodutivo
  (Maguire & Mody, 2007; brexanolone).
- **B4↔B7 (microbiota) — MEDIUM/emergente.** microbiota regula 5-HT **entérica** (Yano, 2015);
  ponte ao SNC indireta.
- **B4↔B12 (trauma/TEPT), B10 (sono/ritmo), B6 (redox), B8 (micronutrientes — cofatores
  BH4/B12/folato/triptofano) — MEDIUM/LOW:** plausíveis; conexão específica no humor parcialmente
  documentada, em parte `[emergente]`.

[REF_MODULO_06: Blier_1994 | Berton_2006 | Morris_2020 | Caspi_2003 | Parsons_Hurd_2015 |
Welsch_2023 | Wang_dinorfina_2023 | Maguire_Mody_2007 | Yano_2015]

---

## MÓDULO 07 — SUBTIPOS E FENÓTIPOS CLÍNICOS DOCUMENTADOS

- **Fenótipo "depleção-sensível/vulnerável":** depleção rebaixa humor só em remitidos/vulneráveis
  (Ruhé, 2007) — traço de dependência monoaminérgica.
- **Subtipo respondedor vs não-respondedor:** eficácia real mas modesta; a base é o subconjunto
  respondedor (Cipriani, 2018); CYP2D6/2C19 explica pseudorrefratariedade.
- **Fenótipo de anedonia/recompensa (DA):** alteração de esforço/erro de predição (Schultz,
  1997); distinto do fenótipo ansioso.
- **Fenótipo ansioso/hipervigilante (NA/LC):** arousal/burst do LC (Morris, 2020; Grimm, 2024).
- **Fenótipo compulsivo/ruminativo (5-HT):** TOC/ruminação (ISRS em dose alta — uso clínico na
  Biblioteca).
- **Fenótipo genético de vulnerabilidade (5-HTTLPR/MAOA):** pequeno e dependente de estresse
  (não replicado para depressão).
- **Depressão pós-parto/reprodutiva (neuroesteroide):** brexanolone/Maguire & Mody — interface
  B14.

[REF_MODULO_07: Ruhe_2007 | Cipriani_2018 | Schultz_1997 | Morris_2020 | Grimm_2024 |
Caspi_2003 | Maguire_Mody_2007 | Meltzer-Brody_2018]

---

## MÓDULO 08 — CONTROVÉRSIAS, HETEROGENEIDADE E LACUNAS

**Controvérsia central (viva, entra como disputa):**
- *Hipótese da serotonina baixa causal* — revisão guarda-chuva não encontra evidência (Moncrieff
  et al., 2022) vs réplica metodológica que questiona a revisão (Jauhar et al., 2023). O campo
  não trata "baixa 5-HT" como fato; a modulação monoaminérgica segue clinicamente útil, mas por
  gating/plasticidade, não por reposição. [humano; controvérsia ativa].
- **Eficácia real mas modesta e com viés:** rede de 21 antidepressivos mostra efeito agudo real,
  porém pequeno (Cipriani et al., 2018); o viés de publicação inflou a eficácia aparente (Turner
  et al., 2008). [meta; bem documentado].
- **Genética candidata que não replica:** 5-HTTLPR×estresse (Caspi 2003 → Risch 2009/
  Culverhouse 2018); MAOA/Lesch ansiedade efeito pequeno.

**Heterogeneidade:** três monoaminas dissociáveis; espécie (código temporal/optogenética é
animal); periferia vs SNC (5-HT entérica); tabaco (MAO-A/DAT); genótipo/CYP; estado vs traço.

**Tradução animal→humano:** burst de DA, modos do LC e gating são prova causal em roedor/
neurofisiologia; humano oferece PET, depleção, genética e resposta clínica.

**Lacunas `[G1]`:** STAR*D/Trivedi; heterodímero 5-HT2A–mGlu2 (González-Maeso); TAAR1 (Revel);
TPH2 LoF (Zhang); Canli & Lesch; 5-HT optogenético na amígdala (Marcinkiewcz); scRNA rafe (Okaty)
e astroglia (von Ziegler); NPY/galanina; Salamone (DA/esforço); mais dinorfina/κ; CYP e resposta;
TOC/ISRS; pânico/sistema de alerta; agomelatina MT/5-HT2C.

**Viés de publicação:** ver inventário negativo (baixa 5-HT, 5-HTTLPR, 5-HT periférica,
anedonia=baixa DA).

[REF_MODULO_08: Moncrieff_2022 | Jauhar_2023 | Cipriani_2018 | Turner_2008 | Caspi_2003 |
Risch_2009 | Culverhouse_2018 | Lesch_1996]

---

## MÓDULO 09 — CHECKLIST DE VERIFICAÇÃO CRUZADA COM O PROMPT 4.0

| Categoria | Bloco Prompt 4.0 | Status |
|---|---|---|
| M01 vias | BLOCO_02.1-2.3 | [7 vias: síntese, receptores, latência, DA-código, NA/LC, scRNA, outros moduladores] |
| M02 mediadores | BLOCO_03 | [enzimas/transportadores/receptores/moduladores + inventário negativo] |
| M03 células/estruturas | BLOCO_04 | [rafe/LC/VTA, subtipos, vias, PET] |
| M04 genética/epigenética | BLOCO_02.4 | [5-HTTLPR/MAOA/COMT/TPH2/CYP; não-replicação explícita] |
| M05 biomarcadores | BLOCO_05 | [periférico/liquor/PET MAO-A/SERT; sem valor de corte] |
| M06 interconexões | BLOCO_08 | [B3/B5/B2 HIGH; B13/B1/B9/B14/B7; outras] |
| M07 subtipos | BLOCO_12 | [7 fenótipos descritivos] |
| M08 controvérsias | CONTROVÉRSIAS | [Moncrieff×Jauhar; Cipriani/Turner; não-replicação gênica; `[G1]`] |

*Antidepressivos/fármacos aparecem apenas como prova farmacológica/histórica e de eficácia
populacional (modesta/viés), não como prescrição — reservado à Biblioteca.*

[REF_MODULO_09: mapeamento Molde_GPM_v2.0 × Prompt_4.2]

---

## MÓDULO 10 — OBSERVAÇÕES EM OUTRAS CONDIÇÕES
*(amostra ilustrativa — não triagem sistemática; fora da contagem de cobertura)*

- **Hipótese histórica (reserpina/IMAOs, Schildkraut 1965; Coppen 1967; Lacasse & Leo 2005):**
  origem acidental da hipótese das catecolaminas/serotonina — entra como marco historiográfico.
- **Doença de Parkinson (DA/substância negra):** depleção dopaminérgica definida e depressão
  comórbida — contraste que mostra o que é um déficit monoaminérgico "real" vs sutil no humor.
- **TDAH (DAT/NET), narcolepsia, dor crônica:** modulação por transportadores/DA/NA fora do humor.
- **Síndrome serotoninérgica/toxicidade farmacológica:** farmacologia, não mecanismo de doença.
- **Dependência/recompensa:** código fásico de DA e endocanabinoides (Parsons & Hurd, 2015) —
  vizinho de recompensa.

[REF_MODULO_10: Schildkraut_1965 | Coppen_1967 | Lacasse_Leo_2005 | Parsons_Hurd_2015]

---

*Fim do GPM_B4. PMIDs verificados no Briefing B4 (31 âncoras); G1→G2→G3 na Rodada 2.*
