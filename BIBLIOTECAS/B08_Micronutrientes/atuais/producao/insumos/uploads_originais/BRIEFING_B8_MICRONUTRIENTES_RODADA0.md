# BRIEFING — RODADA 0 — B8 — DEFICIÊNCIAS DE MICRONUTRIENTES (ATUALIZAÇÃO)
### Dossiê de referências do GPM — PMIDs cravados, auditoria PubMed E-utilities, reconciliação com a matriz canônica da triagem

> **Status:** GPM atualizado (M00–M10, molde v2.0; substitui a versão em `2 ANTIGOS/2026-09-09/`) · 44 âncoras → 100% com PMID · corpo limpo (zero PMID/DOI) · trinca = GPM + este briefing + `CHECKLIST_SANIDADE_GPM_B8.md`
> **Fontes:** Artigos cientificos do mecanismo B8 deficiencia micronutrientes 08.09.26 (98 refs) + Resumo do insumo B8 Chatgpt (matriz 50 claims, 10 regras B8-Causal)

## §1 — MÉTODO DE AUDITORIA
1. Insumo convertido em entradas autor/ano/DOI e auditado **DOI→PMID** (esearch individual + esumary em lote): ver `SUPORTE/pmid_map.json`/`meta_pmid.json`.
2. Âncoras fora do insumo resolvidas por **buscas dirigidas** e confirmadas por esumary antes de entrar no anchormap.
3. Anchormap final: `SUPORTE/b8_anchormap.json` — 44 chaves, zero falhas, anos canônicos pelo print.
4. Índice do GPM regenerado por script; corpo validado com ZERO PMID/DOI.

## §2 — ESTATÍSTICAS DO GPM
| Métrica | Valor |
|---|---|
| Linhas / módulos | 257 / 11 (M00–M10) |
| Âncoras → PMIDs | 44/44 |
| PMID/DOI no corpo | ZERO |
| Regras fundadoras / vias | M00 / 10 |
| Inventário negativo / fenótipos | 10 / (M07) |
| EXTRAPOLAÇÃO POR ANALOGIA / [G1] | 0 / 7 |
| Autoauditorias | 11 blocos |

## §3 — TABELA-MESTRA (44 âncoras → PMID)
| # | Chave (Autor, Ano) | PMID | Título (resumo) |
|---|---|---|---|
| 1 | Eyles, 2013 | 22796576 | Vitamin D, effects on brain development, adult brain function and the links between low levels of vi |
| 2 | Du, 2016 | 25365455 | The Role of Nutrients in Protecting Mitochondrial Function and Neurotransmitter Signaling: Implicati |
| 3 | Kennedy, 2016 | 26828517 | B Vitamins and the Brain: Mechanisms, Dose and Efficacy--A Review. |
| 4 | Firth, 2017, suplementação | 28202095 | The effects of vitamin and mineral supplementation on symptoms of schizophrenia: a systematic review |
| 5 | Firth, 2017, FEP | 29206972 | Nutritional Deficiencies and Clinical Correlates in First-Episode Psychosis: A Systematic Review and |
| 6 | Wesselink, 2019 | 30201141 | Feeding mitochondria: Potential role of nutritional components to improve critical illness convalesc |
| 7 | Barks, 2019 | 30341413 | Iron as a model nutrient for understanding the nutritional origins of neuropsychiatric disease. |
| 8 | Plevin, 2020 | 32552785 | The neuropsychiatric effects of vitamin C deficiency: a systematic review. |
| 9 | Rudzki, 2021 | 33428888 | Gut microbiota-derived vitamins - underrated powers of a multipotent ally in psychiatric health and  |
| 10 | Cui, 2021 | 33500553 | Vitamin D and schizophrenia: 20 years on. |
| 11 | Muscaritoli, 2021 | 33763446 | The Impact of Nutrients on Mental Health and Well-Being: Insights From the Literature. |
| 12 | Shayganfard, 2022 | 33904124 | Are Essential Trace Elements Effective in Modulation of Mental Disorders? Update and Perspectives. |
| 13 | Barks, 2021 | 34836113 | Early-Life Iron Deficiency Anemia Programs the Hippocampal Epigenomic Landscape. |
| 14 | Badar, 2022 | 35223256 | Neuropsychiatric Disorders Associated With Vitamin B12 Deficiency: An Autobiographical Case Report. |
| 15 | Barone, 2022 | 35294077 | Gut microbiome-micronutrient interaction: The key to controlling the bioavailability of minerals and |
| 16 | Sahu, 2022 | 35337631 | Neuropsychiatric manifestations in vitamin B12 deficiency. |
| 17 | McWilliams, 2022 | 36173945 | Iron deficiency and common neurodevelopmental disorders-A scoping review. |
| 18 | Nogueira-de-Almeida, 2023 | 36411563 | Neuronutrients and Central Nervous System: A Systematic Review. |
| 19 | Fiani, 2023 | 37147046 | Iron Deficiency in Attention-Deficit Hyperactivity Disorder, Autism Spectrum Disorder, Internalizing |
| 20 | Zielińska, 2023 | 37299394 | Dietary Nutrient Deficiencies and Risk of Depression (Review Article 2018-2023). |
| 21 | Lahoda Brodska, 2023 | 37836413 | The Role of Micronutrients in Neurological Disorders. |
| 22 | Mathew, 2024 | 38203763 | Vitamin B12 Deficiency and the Nervous System: Beyond Metabolic Decompensation-Comparing Biological  |
| 23 | Berger, 2024 | 38462972 | Micronutrient deficiency and supplements in schoolchildren and teenagers. |
| 24 | Rajasekar, 2024 | 38605872 | Dietary intake with supplementation of vitamin D, vitamin B6, and magnesium on depressive symptoms:  |
| 25 | Al Jassem, 2024 | 38630748 | Vitamin B12 deficiency and neuropsychiatric symptoms in Lebanon: A cross-sectional study of vegans,  |
| 26 | Hui, 2024 | 38999789 | Micronutrient-Associated Single Nucleotide Polymorphism and Mental Health: A Mendelian Randomization |
| 27 | Carnegie, 2024 | 39519523 | Micronutrients and Major Depression: A Mendelian Randomisation Study. |
| 28 | Scuto, 2024 | 39596221 | Functional Food Nutrients, Redox Resilience Signaling and Neurosteroids for Brain Health. |
| 29 | Rucklidge, 2025 | 39703999 | Annual Research Review: Micronutrients and their role in the treatment of paediatric mental illness. |
| 30 | Rajen, 2025 | 39829265 | Impaired folate status in patients with mental disorders. |
| 31 | Ye, 2025 | 39952338 | Causal relationship between B vitamins and neuropsychiatric disorders: A systematic review and meta- |
| 32 | Anmella, 2025 | 40100400 | Association of low vitamin B(12) levels with depressive and schizophrenia spectrum disorders in chil |
| 33 | Faugere, 2025 | 40218925 | Vitamin D, B9, and B12 Deficiencies as Key Drivers of Clinical Severity and Metabolic Comorbidities  |
| 34 | Domański, 2025 | 40289952 | Hematological Correlations as Predictors of Disease Manifestations in Psychiatric Inpatients. |
| 35 | Radoeva, 2025 | 40329546 | Estimated Nutrient Intake and Association With Psychiatric and Sleep Problems in Autistic Youth in t |
| 36 | Astorino, 2025 | 40653891 | The Multifaceted Etiology of Mental Disorders With a Focus on Trace Elements, a Review of Recent Lit |
| 37 | Lu & Paterson, 2025 | 40739033 | Estimating effects of serum vitamin B12 levels on psychiatric disorders and cognitive impairment: a  |
| 38 | Skoczek-Rubińska, 2025 | 40871684 | Impact of Vitamin D Status and Supplementation on Brain-Derived Neurotrophic Factor and Mood-Cogniti |
| 39 | Fang, 2025 | 41211168 | Causal Influences of Micronutrients on Anxiety: Insights From an Observational and Mendelian Randomi |
| 40 | Faa, 2025 | 41303365 | Perturbations of Zinc Homeostasis and Onset of Neuropsychiatric Disorders. |
| 41 | Alexa, 2026 | 42029584 | The Nutritional Paradox of Obesity: Mechanisms and Clinical Implications of Micronutrient Deficienci |
| 42 | Shahini, 2026 | 42144425 | Micronutrient-immune interactions in mood and psychotic disorders: a case-control study of vitamin C |
| 43 | Moroianu, 2026 | 42187879 | Vitamin D and Vitamin B(12) in Psychiatric Disorders: An Exploratory Systematic Review and Meta-Anal |
| 44 | Tortajada, 2026 | 42253799 | Clinical outcomes of mitochondrial-enhancing nutraceutical supplementation in psychiatric disorders: |

## §4 — CORREÇÕES DE AUDITORIA APLICADAS (não reverter)
1. **"Mattei, 2019" (insumo) = McWilliams, 2022** (36173945, scoping review de ferro×neurodesenvolvimento) — a reatribuição resolveu exatamente o "McWilliams 2022" citado pela matriz; o Mattei real (desenvolvimento) NÃO localizado → [G1].
2. **"Yoon, 2026" (insumo) = Zielińska, 2023** (37299394, revisão 2018–2023 de deficiências nutricionais×depressão) — autor/ano canônicos pelo print.
3. **"Dehesh, 2026" (insumo) = Domański, 2025** (40289952) — reatribuído; o Dehesh real não localizado → [G1]. **"Navale, 2022" (insumo) = Nogueira-de-Almeida, 2023** (36411563, SR neuronutrientes) — reatribuído.
4. **Anos canônicos = print:** Barks **2019** (triagem/insumo: 2018); Eyles **2013** (2012); Rucklidge **2025**; Shayganfard **2022**; Al Jassem 2024; Lahoda Brodska 2023 (sobrenome composto).
5. **Firth 2017 = DOIS papers** (FEP meta 29206972; suplementação em esquizofrenia 28202095) → chaves separadas.
6. **MR confirmados:** Carnegie 39519523 e Fang 41211168 conferem com os PMIDs da matriz; **Lu & Paterson = 40739033** (esumary Lu T, 2025); **Ye = 39952338** (Ye M, SR+MA+MR); Hui = 38999789; Skoczek-Rubińska = 40871684 (dirigidas).
7. **Wang 2018 (Zn-Mg-Se, PDF de fase anterior) sem PMID confirmado** → [G1], não inventado.

## §5 — NÃO-INDEXADOS / NAO-IDX
| Item | Motivo |
|---|---|
| Bourre, 2006 — sem DOI | revista francesa não localizada no PubMed |
| Chambers, 2023 — 10.33140/mcr.08.10.04 | revista não indexada |
| Barakat, 2026 — 10.1016/j.nutos.2026.100646 | periódico não indexado (claims B8.SM18-19 viraram [G1] nele) |
| Fedulova/Jayashree/Júnior/Kim-2026/Lubis/Medford/Wróblewska | revistas regionais/capítulo de livro/fora de escopo |

## §6 — NÃO CITADAS NO GPM (54 do insumo) — registro para Rodada 2

**básico/outros (23):** Altamimi 2018 (29773950); Barakat 2026 (NAO-IDX); Bourre 2006 (NAO-IDX); Ceolin 2023 (37754219); Chambers 2023 (NAO-IDX); Chen 2024 (39076846); Ciobanu 2023 (34684531); Daniel 2025 (40290005); Das 2025 (41064635); Fedulova 2026 (NAO-IDX); Fuglestad 2016 (26439893); Hanachi 2019 (30959831); Jayashree 2026 (NAO-IDX); Júnior 2026 (NAO-IDX); Khalid 2022 (36497797); Khan 2026 (42005161); Kim 2026 (NAO-IDX); Li 2025 (41994411); Lubis 2026 (NAO-IDX); Medford 2020 (NAO-IDX); Mohammadzadeh 2022 (35105560); Panzeri 2024 (38512555); Wróblewska 2025 (NAO-IDX).

**minerais/oligoelementos (2):** Majewska 2025 (40724885); Wang 2018 (29747386).

**psiquiatria clínica/observacional (4):** Hachmeriyan 2026 (42123920); Heland 2022 (36483929); Islam 2025 (41228551); Wu 2024 (39393463).

**redox/mitocôndria (1):** Gupta 2024 (39133336).

**vitaminas/um-carbono (24):** Avram 2025 (40362647); Ducki 2026 (42356264); Ferriani 2021 (34695501); Freedman 2021 (33838984); Guo 2020 (30570388); Han 2025 (40904570); Horsdal 2025 (40379361); Indika 2023 (36836486); Khosropanah 2026 (41992896); Kohl 2025 (41515142); Kumar 2021 (34802410); Miteva 2026 (41769656); Moore 2019 (30692033); Pancheva 2026 (41978148); Rihal 2022 (36049434); Saidi 2023 (37350315); Tardy 2020 (31963141); Triggianese 2026 (41754076); Upadhyaya 2022 (36613505); Walsh 2024 (38560530); Wassif 2023 (38022259); Xu 2025 (41523970); Yang 2026 (42044701); Ye 2023 (37424961).

> **Motivo geral:** SUP temático, CONTEXT e revisões redundantes com as âncoras; nenhum descarte por contrariar tese.

## §7 — RECONCILIAÇÃO ESTRUTURAL (matriz → GPM)
- Claims da matriz mapeados no M09 sem promoção de nível; regras causais da triagem reproduzidas no M00.
- Números de efeito (OR/HR/SMD/d) NÃO copiados — alegações a confirmar em rodada de quantificação.
- Cadeia causal-mãe no ID do mecanismo; cada seta como unidade de evidência.

## §8 — PENDÊNCIAS [G1] PARA A RODADA 2

1. Mattei 2019; Dehesh 2026; Wang 2018 Zn-Mg-Se; Das 2025; Cortés-Albornoz 2021 (âncoras do desenvolvimento/observacional).
2. Iodo ↔ B11 (B8.10) e HPA ↔ B2 (B8.19) com âncoras cruzadas.
3. Vitaminas B1/B2/B3/B5/B7 sem âncora própria.
4. MR por micronutriente individual consolidado (hoje espalhado em 5 estudos).
5. Interações multi-nutriente (Rucklidge) com desfecho psiquiátrico registrado.
6. GRADE formal quando o pipeline ativar.

---

**Fecho:** B8 entra na Rodada 2 com biblioteca 100% verificável (44 chaves → 44 PMIDs), zero PMID/DOI no corpo, NAO-IDX registrados e regras causais da matriz como espinha.