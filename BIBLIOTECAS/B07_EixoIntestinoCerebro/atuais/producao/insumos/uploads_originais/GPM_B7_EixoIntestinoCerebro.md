# GPM B7 — EIXO INTESTINO–CÉREBRO / MICROBIOTA — MOLDE v2.0
### Módulo da arquitetura neuropsiquiátrica (ansiedade & depressão) · Rodada 0 · 2026-09-08
> **Status:** GPM reconstruído sobre a Matriz Canônica B7 (34 claims, triagem científica com causalidade explícita) + insumo "Artigos cientificos do mecanismo B7 eixo intestino cérebro 08.09.26" (178 refs; 173 DOI→PMID auditados) + 5 PDFs de fase anterior incorporados como revisões de arquitetura. 31 âncoras → 31 PMIDs verificados (b7_anchormap.json). Corpo limpo (zero PMID/DOI). Trinca: GPM + BRIEFING_B7_EIXO_INTESTINO_CEREBRO_RODADA0.md + CHECKLIST_SANIDADE_GPM_B7.md.

---

## MÓDULO 00 — METADADOS, REGRAS FUNDADORAS, ESCOPO E FRONTEIRAS
[REF_MODULO_00: Cryan, 2019; Carabotti, 2015; Margolis & Cryan, 2021; Braniste, 2014; Barki, 2022]

**ID do mecanismo (B7):** comunicação bidirecional microbiota–intestino–cérebro por **quatro pontes funcionais** (metabólica/SCFAs e indóis; imune/barreira; neural/vagal; endócrina/HPA), em que **cada seta da cadeia-mãe é uma unidade independente de evidência**: microbiota → função/metabólito → alvo molecular/celular → barreira/imunidade/neural → circulação/BBB → SNC → microglia/neurônio → neurotransmissão/plasticidade → comportamento → desfecho clínico.

**REGRAS FUNDADORAS:**
1. **REGRA B7-CAUSAL-01:** nenhuma alteração de composição da microbiota é promovida a mecanismo causal cerebral sem demonstração independente de **pelo menos uma ponte funcional** (metabólito, receptor, barreira, sinalização imune, sinalização neural, intervenção experimental).
2. **REGRA B7-CAUSAL-02:** metabólito administrado exogenamente com efeito cerebral sustenta apenas **metabólito → cérebro**; não converte automaticamente em **microbiota → cérebro** (Sathyasaikumar, 2024 é o guarda-case).
3. **REGRA B7-CAUSAL-03:** associações microbiota ↔ depressão/ansiedade permanecem `[ASSOCIATIVO]` mesmo com plausibilidade mecânica (Zhou, 2023; Lin, 2023).
4. **Causalidade graduada obrigatória:** cada claim carrega selo ESTABLISHED experimental / PROBABLE / SUGGESTIVE / ASSOCIATIVE (matriz v1.0) — nunca colapsados em "comprovado".
5. **Formulação específica > genérica:** "acetato → maturação metabólica de microglia" (Erny, 2021) substitui "SCFA é anti-inflamatório".
6. **Arquitetura causal preservada intacta:** SCFA cerebral → ACSS2 → PPARγ → TPH2 → serotonina → comportamento (Chen, 2024) não pode ser resumida a "SCFA melhora depressão".
7. **Revisões = arquitetura, não prova** (Cryan, 2019; Carabotti, 2015; Margolis & Cryan, 2021; Socała, 2021; Góralczyk-Bińkowska, 2022; Bonaz, 2018; Hwang, 2025).
8. **GF/germ-free ≠ humana:** extrapolação de camundongos GF para humano exige `[EXTRAPOLAÇÃO POR ANALOGIA]` (Braniste, 2014; Erny, 2021).
9. **Multi-tag permitida** (CORE + clínico + suporte, como na matriz).
10. **Desfecho psiquiátrico humano** só entra como associação/intervenção-ponte; nenhum claim causal humano fechado nesta rodada.

**Dicionário mínimo:** GF/PF (germ-free/antibiótico); SCFAs (ácidos graxos de cadeia curta: acetato, propionato, butirato); FFAR2/GPR43 e FFAR3/GPR41; TJP/tight junctions; TLR4/MyD88/MLCK; Hcy–KYN (triptofano→quinurenina); KYNA/QUIN; indóis/IPrA (indole-3-propionic acid); ACSS2 (acetil-CoA sintetase de cadeia curta); FMT (transplante de microbiota).

**Fronteiras:** quinurenina central profunda → B1 (inflamação/IDO) e B5 (NMDAR/QUIN); HPA/cortisol → B2; estresse como modulador → B12 (trauma); dieta/micronutrientes → B8; ROS periférico → B6; mitocondria-microglia → B9; serotonina/TPH2 → B4.

**Lacunas [G1] do M00:** (a) ácidos biliares como ponte neuroativa — estrutura B7-07 sem âncora própria nesta coleção; (b) ponte neural direta (vago→núcleo do trato solitário→…) com fisiologia humana; (c) HPA-microbiota com âncora experimental do eixo completo.

**Autoauditoria M00:** (i) as 3 regras causais da matriz estão reproduzidas verbatim em espírito (01/02/03); (ii) nenhuma revisão foi usada como prova; (iii) a cadeia-mãe está no ID e cada via do M01 corresponde a um trecho dela.

---

## MÓDULO 01 — MAPA DAS VIAS MOLECULARES (10 camadas numeradas)
[REF_MODULO_01: Barki, 2022; Erny, 2021; Caetano-Silva, 2023; Chen, 2024; Braniste, 2014]

**Via 1 — Microbiota → SCFAs (produção metabólica).** Fermentação de fibras → acetato/propionato/butirato; fibra/inulina eleva SCFAs e reduz resposta microglial a LPS `[animal+celular; PROBABLE]` (Caetano-Silva, 2023).

**Via 2 — SCFAs → FFAR2/FFAR3 → comunicação neural gut–brain.** Ativação funcional dos receptores em componentes neurais; FFAR3 intestinal regula aferentes sensoriais `[animal; ESTABLISHED experimental; A]` — chemogenética (Barki, 2022).

**Via 3 — Acetato → microglia (maturação metabólica).** Microbiota→acetato habilita a fitness metabólica da microglia; funções como fagocitose dependem do estado metabólico `[animal GF/PF; ESTABLISHED+PROBABLE; A/A-B]` (Erny, 2021).

**Via 4 — SCFAs → HDAC↓/NF-κB nuclear↓ em microglia.** Mecanismo epigenético/transcricional da modulação inflamatória `[microglia primária; ESTABLISHED; B]` (Caetano-Silva, 2023). Nuance preservada: o efeito não depende necessariamente de FFAR2/3 na microglia (mesmo estudo).

**Via 5 — SCFA cerebral → ACSS2 → PPARγ → TPH2 → serotonina → comportamento.** Cadeia completa com knockdown neuronal abolindo o efeito comportamental `[animal+célula; ESTABLISHED/PROBABLE; B]` (Chen, 2024). Extrapolação para humano: proibida sem ponte (regras 6/8).

**Via 6 — Barreira intestinal: LPS → TLR4/MyD88/MLCK → permeabilidade ↑.** MLC fosforilação e redistribuição de TJP `[celular+animal; ESTABLISHED; A]` (Guo, 2013; Guo, 2015; Nighot, 2017; Nighot, 2019).

**Via 7 — Endotoxemia → circulação → cérebro (neuroinflamação).** Endotoxemia metabólica amplifica neuroinflamação pós-isquemia — cadeia intestino→circulação→cérebro `[animal; PROBABLE; B]` (Kurita, 2020).

**Via 8 — Barreira hematoencefálica: microbiota → TJP cerebrais.** GF ↑ permeabilidade da BBB; restauração da microbiota normaliza occludina/claudina-5 `[animal GF; PROBABLE/ESTABLISHED; A]` + arquitetura das barreiras `[revisão]` (Braniste, 2014; Aburto & Cryan, 2024).

**Via 9 — Triptofano → KYN (periferia e cérebro).** Inflamação intestinal ativa via KYN em sangue/cérebro (colite experimental) `[animal; PROBABLE; B]` (Zhao, 2023); estresse crônico altera KYN nos dois compartimentos (Li, 2023); caracterização geral `[revisão]` (Agus, 2018; Chen, 2021; Bosi, 2020).

**Via 10 — Indóis/IPrA → cérebro (KYNA) e probiótico→KYN.** L. reuteri capta quinurenina e gera KYNA in vitro `[in vitro; B]` (Schwarcz, 2024); IPrA oral ↑ IPrA e KYNA cerebrais `[ratos; ESTABLISHED; B]` — com regra 2 limitando o claim (Sathyasaikumar, 2024).

**Autoauditoria M01:** (i) cada via corresponde a um trecho da cadeia-mãe com selo causal próprio; (ii) nenhuma via termina em desfecho clínico humano causal; (iii) as revisões de arquitetura (Via 0 implícita) ficaram no M00/M02, não como prova.

---

## MÓDULO 02 — MEDIADORES COM POLARIDADE + INVENTÁRIO NEGATIVO
[REF_MODULO_02: Erny, 2021; Caetano-Silva, 2023; Chen, 2024; Sathyasaikumar, 2024; Zhou, 2023]

| Mediador/ponte | Alvo principal | Efeito documentado |
|---|---|---|
| Acetato | microglia | maturação metabólica/função (Erny, 2021) |
| Butirato/acetato | microglia LPS | citocinas ↓ (Caetano-Silva, 2023) |
| SCFAs | FFAR2/3 neural | atividade aferente ↑ (Barki, 2022) |
| SCFAs | HDAC/NF-κB | epigenômico anti-inflamatório (Caetano-Silva, 2023) |
| SCFA cerebral | ACSS2→PPARγ→TPH2 | transcrição TPH2/serotonina (Chen, 2024) |
| LPS | TJP intestinal | permeabilidade ↑ (Guo, 2013) |
| Endotoxemia | neuroinflamação | amplificação pós-lesão (Kurita, 2020) |
| KYN/IPrA | KYNA cerebral | disponibilidade ↑ (Sathyasaikumar, 2024) |
| Roseburia | serotonina/KYN/glia | modificação experimental (Zhou, 2023) |
| Microbiota | BBB TJP | permeabilidade ↓ na colonização (Braniste, 2014) |

**INVENTÁRIO NEGATIVO:**
1. "Disbiose causa depressão" — não demonstrado; associação permanece (regra 3).
2. "SCFA é anti-inflamatório" genérico — substituir pela formulação específica (regra 5).
3. "IPrA provou microbiota→cérebro" — provou metabólito→cérebro (regra 2).
4. "Probiótico = tratamento psiquiátrico" — nenhum claim terapêutico fechado; intervenções como sinal.
5. "Microglia humana = microglia de camundongo GF" — [EXTRAPOLAÇÃO POR ANALOGIA] obrigatória.
6. "FFAR2/3 explicam tudo" — efeitos independentes de FFAR documentados (Caetano-Silva, 2023).
7. "Via KYN intestinal = via KYN central" — compartimentos distintos; pontes parciais (Zhao, 2023; Li, 2023).
8. "FMT de saudável = terapia" — fenótipo animal melhorado; tradução indefinida (Zhou, 2023).
9. "Ácidos biliares/neuroativação" — lacuna sem âncora `[G1]`, não afirmar.
10. "Vago = única rota neural" — rota importante, não exclusiva (Bonaz, 2018; Hwang, 2025).

**Autoauditoria M02:** (i) NEG 1–3 protegem exatamente as três regras causais; (ii) tabela sem polaridade binária (efeitos descritos, não "bom/ruim"); (iii) lacunas viram [G1] e não afirmações.

---

## MÓDULO 03 — TIPOS CELULARES E ESTRUTURAS
[REF_MODULO_03: Erny, 2021; Caetano-Silva, 2023; Braniste, 2014; Aburto & Cryan, 2024; Spichak, 2021]
- **Microglia** (metabolismo acetato-dependente; resposta a LPS) — Erny, 2021; Caetano-Silva, 2023.
- **Enterócito/barreira intestinal** (TJP, MLCK) — Guo, 2013; Nighot, 2019.
- **Endotélio/BBB** (occludina, claudina-5) — Braniste, 2014; Aburto & Cryan, 2024.
- **Neurônios aferentes/enteroendócrinos** (FFAR3) — Barki, 2022.
- **Astrócitos** (expressão gênica sex-dependente sob SCFAs) — Spichak, 2021 `[celular; PROBABLE; B]`.
- **Neurônio serotoninérgico (TPH2/raphe)** — Chen, 2024 (modelo).
- **Vago** (interface neural) — Bonaz, 2018; Hwang, 2025.
**Autoauditoria M03:** (i) tipos com evidência própria citada; (ii) nenhum circuito central específico (PFC/hipocampo) recebeu âncora nesta coleção `[G1]`.

---

## MÓDULO 04 — VARIABILIDADE: ECOSSISTEMA E HOSPEDEIRO (não polimorfismo clássico)
[REF_MODULO_04: Zhou, 2023; Lin, 2023; Caetano-Silva, 2023]
- **Interindividualidade da microbiota:** resposta dependente do ecossistema basal (Zhou, 2023 — doador adolescente saudável; Lin, 2023).
- **Dieta como variável causal de ponte** (fibra/inulina → SCFAs) — Caetano-Silva, 2023.
- **Sexo:** efeitos sex-dependentes em astrócitos (Spichak, 2021) — sinal, não sistema.
- **Genética do hospedeiro/microbioma de base ↔ psiquiatria:** NADA direto na coleção `[G1]`.
**Autoauditoria M04:** (i) variabilidade tratada como modulador, não como ruído; (ii) [G1] registrada.

---

## MÓDULO 05 — BIOMARCADORES À BEIRA DO LEITO (SEM PROTOCOLO/CORTE)
[REF_MODULO_05: Zhou, 2023; Lin, 2023; Kurita, 2020]
- **Composição microbiota** (gêneros: Roseburia etc. — Zhou, 2023) — descritiva, associativa.
- **Metabolômica fecal/sérica:** SCFAs, triptofano, KYN/KYNA/QUIN, indóis/IPrA; painéis SCFA↔depressão em revisão dedicada (Cheng, 2024).
- **Permeabilidade:** marcadores de translocação (LPS/endotoxemia — Kurita, 2020, contexto experimental).
- **Inflamação:** citocinas periféricas.
- **Regras:** sangue/fezes ≠ cérebro; nenhum corte; nenhuma assinatura diagnóstica estabelecida.
**Autoauditoria M05:** (i) nenhum marcador virou "teste"; (ii) camada metabolômica ligada às vias 1/9/10.

---

## MÓDULO 06 — CONEXÕES CAUSAIS COM OUTROS BLOCOS (FÁRMACOS/INTERVENÇÕES SÓ COMO SINAL)
[REF_MODULO_06: Zhao, 2023; Li, 2023; Schwarcz, 2024; Kurita, 2020; Chen, 2024]
- **B7 → B1:** endotoxemia/barreira → neuroinflamação (Kurita, 2020); microglia (Erny, 2021) — ponte imune declarada.
- **B7 → B5/B1 (KYN):** triptofano→quinurenina compartimentada (Zhao, 2023; Li, 2023; Schwarcz, 2024) — QUIN/KYNA pertencem a B5 (glutamato) e B1 (IDO); aqui só a ponte periférica.
- **B7 → B4 (serotonina):** TPH2 via ACSS2 (Chen, 2024) — ponte declarada, cadeia no B7, neurotransmissor no B4.
- **B7 ↔ B2 (HPA):** estresse→microbiota→KYN (Li, 2023) `[G1: âncora HPA completa pendente]`.
- **B7 ↔ B8 (dieta):** fibra/SCFAs = interface dietética; alimentos como exposição, não terapia.
- **B7 ↔ B6 (redox):** Saikachain, 2023 (neuroproteção oxidativa celular via GPR43) — sinal `[G1]`.
- **B7 ↔ B10 (ritmo):** microbiota-gut-circadian `[G1 — âncora no B10]`.
**Autoauditoria M06:** (i) nenhuma ponte invade território (KYN central fica em B5/B1); (ii) intervenções (probiótico/FMT/dieta) apenas como janelas experimentais.

---

## MÓDULO 07 — SUBTIPOS / FENÓTIPOS CLÍNICOS (SEM INTERVENÇÃO)
[REF_MODULO_07: Zhou, 2023; Lin, 2023]
- **F1 — Depressão adolescente com assinatura microbiota-triptofano:** associação + causalidade experimental em cascata (FMT de doador saudável → comportamento ↑ e metabólitos; Roseburia preditiva) — dois níveis separados por selo (Zhou, 2023).
- **F2 — MDD com atividade KYN alterada:** associação periférica (Lin, 2023).
- **F3 — Fenótipo barreira-leak:** translocação/endotoxemia como assinatura candidate `[G1: âncora clínica psiquiátrica pendente]`.
- **F4 — Resposta microglial hiperinflamatória:** derivada do estado acetato-dependente (Erny, 2021) — fenótipo celular, não diagnóstico.
**Autoauditoria M07:** (i) F1 mantém associação e experimento separados (regra 3); (ii) sem "subtipos de depressão por disbiose".

---

## MÓDULO 08 — CONTROVÉRSIAS, INCERTEZAS, LIMITES DE ESCOPO
[REF_MODULO_08: Erny, 2021; Chen, 2024; Sathyasaikumar, 2024; Caetano-Silva, 2023]
1. **Translacionalidade GF→humano** (regra 8) — o maior fosso do campo.
2. **Dose/espécie de SCFA** — efeitos não interpoláveis entre acetato/propionato/butirato.
3. **Causalidade reversa** (depressão→dieta→microbiota) raramente excluída nos estudos associativos.
4. **FFAR-dependência** parcial (Caetano-Silva, 2023).
5. **Rotas neurais dominantes** (vago vs metabólica vs imune) por contexto.
6. **Kyurenina compartimentada** — medir periferia não informa cérebro.
7. **Probióticos cepa-específicos** (Schwarcz, 2024) — generalização indevida entre cepas.
8. **Heterogeneidade de "disbiose"** — nenhuma assinatura universal.
9. **Ácidos biliares:** bloco estrutural sem âncora `[G1]`.
10. **HPA completo:** peças espalhadas, cadeia não fechada `[G1]`.
**Autoauditoria M08:** (i) controvérsias com fonte; (ii) [G1] ≠ conteúdo inventado.

---

## MÓDULO 09 — TABELA DE MAPEAMENTO × PROMPT 4.0 (ARQUITETURA B7-01–B7-12)
[REF_MODULO_09: ver M01–M08]
| Submódulo | Conteúdo | Onde |
|---|---|---|
| B7-01 | Microbiota (composição/disorbia) | M00 ID; M05; M07 |
| B7-02 | Barreira intestinal (TJP/TLR4/MLCK/LPS) | Via 6; M03 |
| B7-03 | Imunidade intestinal (TLR/citocinas/Treg/Th17/NLRP3) | Via 6–7; M06 `[G1 parcial]` |
| B7-04 | SCFAs (FFAR2/3, HDAC, acetato/propionato/butirato) | Vias 1–5 |
| B7-05 | Triptofano (serotonina, IDO/TDO, KYN/KYNA/QUIN) | Via 9 |
| B7-06 | Metabólitos neuroativos (indóis/IPrA, GABA bacteriano) | Via 10 + NEG |
| B7-07 | Ácidos biliares | `[G1 sem âncora]` |
| B7-08 | Vago/aferências neurais | M03; M08-5 |
| B7-09 | HPA | M06 `[G1]` |
| B7-10 | BBB | Via 8 |
| B7-11 | Microglia/neuroinflamação | Via 3–4; M06 |
| B7-12 | Desfechos (depressão/ansiedade/estresse/cognição) | M07 (selos) |
**Autoauditoria M09:** 12/12 blocos mapeados; B7-07/B7-09 marcados como lacuna, não preenchidos por analogia.

---

## MÓDULO 10 — OUTRAS DOENÇAS ONDE O MECANISMO É PERTURBADO (AMOSTRA ILUSTRATIVA — FORA DA COBERTURA)
[REF_MODULO_10: Kurita, 2020; Zhao, 2023; Góralczyk-Bińkowska, 2022; Socała, 2021]
- **Isquemia cerebral:** endotoxemia amplifica neuroinflamação (Kurita, 2020).
- **Colite/DII:** ativação KYN sérica+cerebral (Zhao, 2023).
- **Espectro neuropsiquiátrico amplo:** revisões de arquitetura (Socała, 2021; Góralczyk-Bińkowska, 2022).
- **[EXC — exclusões de escopo:** doenças puramente gastrointestinais sem desfecho neural; estudos de produção alimentar/pecuária; preprints da coleção (briefing §5).]
**Autoauditoria M10:** (i) ilustrativo; (ii) nenhuma doença emprestada como "prova" de depressão.

---

## FECHAMENTO
Trinca B7: este GPM + BRIEFING_B7_EIXO_INTESTINO_CEREBRO_RODADA0.md (tabela-mestra 31 PMIDs; NAO-IDX §5: 1 sem DOI + 4 não indexados/preprints; pendências §8) + CHECKLIST_SANIDADE_GPM_B7.md. Âncoras: `SUPORTE/b7_anchormap.json` (31 → 31 PMIDs). Rodada 2: ácidos biliares; HPA completo; FFAR humanos; ensaios probióticos com desfecho psiquiátrico registrado.

## ÍNDICE AUTOR ↔ MÓDULO (bidirecional)
| Chave (Autor, Ano) | PMID | Módulos onde aparece |
|---|---|---|
| Aburto & Cryan, 2024 | 38355758 | MÓDULO 01; MÓDULO 03 |
| Agus, 2018 | 29902437 | MÓDULO 01 |
| Barki, 2022 | 35229717 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03 |
| Bonaz, 2018 | 29467611 | MÓDULO 00; MÓDULO 02; MÓDULO 03 |
| Bosi, 2020 | 32577079 | MÓDULO 01 |
| Braniste, 2014 | 25411471 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03 |
| Caetano-Silva, 2023 | 36797287 | MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 04; MÓDULO 08 |
| Carabotti, 2015 | 25830558 | MÓDULO 00 |
| Chen, 2021 | 34127024 | MÓDULO 01 |
| Chen, 2024 | 38939042 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 06; MÓDULO 08 |
| Cheng, 2024 | 38390241 | MÓDULO 05 |
| Cryan, 2019 | 31460832 | MÓDULO 00 |
| Erny, 2021 | 34731656 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 06; MÓDULO 07; MÓDULO 08 |
| Guo, 2013 | 23201091 | MÓDULO 01; MÓDULO 02; MÓDULO 03 |
| Guo, 2015 | 26466961 | MÓDULO 01 |
| Góralczyk-Bińkowska, 2022 | 36232548 | MÓDULO 00; MÓDULO 10 |
| Hwang, 2025 | 39940928 | MÓDULO 00; MÓDULO 02; MÓDULO 03 |
| Kurita, 2020 | 31910709 | MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 06; MÓDULO 10 |
| Li, 2023 | 36746244 | MÓDULO 01; MÓDULO 02; MÓDULO 06 |
| Lin, 2023 | 37049591 | MÓDULO 00; MÓDULO 04; MÓDULO 05; MÓDULO 07 |
| Margolis & Cryan, 2021 | 33493503 | MÓDULO 00 |
| Nighot, 2017 | 29157665 | MÓDULO 01 |
| Nighot, 2019 | 30711488 | MÓDULO 01; MÓDULO 03 |
| Saikachain, 2023 | 37070532 | MÓDULO 06 |
| Sathyasaikumar, 2024 | 38911967 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 08 |
| Schwarcz, 2024 | 38612489 | MÓDULO 01; MÓDULO 06; MÓDULO 08 |
| Socała, 2021 | 34450312 | MÓDULO 00; MÓDULO 10 |
| Spichak, 2021 | 34589808 | MÓDULO 03; MÓDULO 04 |
| Zhao, 2023 | 36776388 | MÓDULO 01; MÓDULO 02; MÓDULO 06; MÓDULO 10 |
| Zhou, 2023 | 37386523 | MÓDULO 00; MÓDULO 02; MÓDULO 04; MÓDULO 05; MÓDULO 07 |
