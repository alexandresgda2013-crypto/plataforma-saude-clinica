# BRIEFING — RODADA 0 — B6 — ESTRESSE OXIDATIVO (EIXO B6-VITAMINA → TRANSSULFURAÇÃO → GSH) (ATUALIZAÇÃO)
### Dossiê de referências do GPM — PMIDs cravados, auditoria PubMed E-utilities, reconciliação com a triagem científica (matriz canônica) e insumo Consensus/DOIs

> **Status:** GPM atualizado (M00–M10, molde v2.0 com (Autor, Ano); substitui a versão em `2 ANTIGOS/2026-09-08/`) · 45 âncoras → 100% com PMID · corpo limpo (zero PMID/DOI) · trinca = GPM + este briefing + `CHECKLIST_SANIDADE_GPM_B6.md`
> **Fontes:** Artigos cientificos do mecanismo B6 Stress oxidativo 08.09.26 (93 refs) + Resumo do insumo B6 Chatgpt (matriz 13 claims)

## §1 — MÉTODO DE AUDITORIA
1. Insumo convertido em entradas (autor/ano/DOI) e auditado **DOI→PMID** no PubMed E-utilities (esearch individual + esumary em lote): resultados no `SUPORTE/pmid_map.json`/`meta_pmid.json`.
2. Âncoras citadas fora do insumo resolvidas por **buscas dirigidas** (título/autor/DOI) e confirmadas por esumary antes de entrar no anchormap.
3. Anchormap final: `SUPORTE/b6_anchormap.json` — 45 chaves, zero falhas.
4. Índice do GPM regenerado por script (bidirecional corpo↔índice); corpo validado com ZERO PMID/DOI.

## §2 — ESTATÍSTICAS DO GPM (atualizado)
| Métrica | Valor |
|---|---|
| Âncoras no anchormap | 45 |
| Chaves citadas no corpo | 45/45 |
| PMID/DOI no corpo | ZERO |
| Regras fundadoras (M00) | 12 (inclui REGRA B6-STRESS-OXIDATIVO-01) |
| Vias (M01) | 10 |
| Inventário negativo (M02) | 10 |
| Fenótipos (M07) | 6 (F1–F6) |
| Controvérsias (M08) | 10 |
| Submódulos B6.01–B6.13 (M09) | 13/13 |
| EXTRAPOLAÇÃO POR ANALOGIA | 3 |
| [G1] | 16 |
| Autoauditorias | 11 blocos |

## §3 — TABELA-MESTRA (45 âncoras → PMID)
| # | Chave (Autor, Ano) | PMID | Título (resumo) |
|---|---|---|---|
| 1 | Aitken, 2011 | 21435402 | The enzymes of the transsulfuration pathways: active-site characterizations. |
| 2 | Averill-Bates, 2023 | 36707132 | The antioxidant glutathione. |
| 3 | Banerjee, 2004 | 15581573 | Redox regulation and reaction mechanism of human cystathionine-beta-synthase: a PLP-dependent hemese |
| 4 | Cabrini, 1998 | 9844729 | Vitamin B6 deficiency affects antioxidant defences in rat liver and heart. |
| 5 | Casique, 2013 | 23981774 | Characterization of two pathogenic mutations in cystathionine beta-synthase: different intracellular |
| 6 | Cheng, 2016 | 27051670 | Vitamin B-6 Supplementation Could Mediate Antioxidant Capacity by Reducing Plasma Homocysteine Conce |
| 7 | Choi, 2009 | 20090886 | Effect of vitamin B(6) deficiency on antioxidative status in rats with exercise-induced oxidative st |
| 8 | Conter, 2020 | 32887901 | Cystathionine β-synthase is involved in cysteine biosynthesis and H(2)S generation in Toxoplasma gon |
| 9 | Conter, 2025 | 40327797 | The disease-linked R336C mutation in cystathionine β-synthase disrupts communication with the PLP co |
| 10 | Dalto & Matte, 2017 | 28245568 | Pyridoxine (Vitamin B₆) and the Glutathione Peroxidase System; a Link between One-Carbon Metabolism  |
| 11 | Davis, 2006 | 16424114 | Plasma glutathione and cystathionine concentrations are elevated but cysteine flux is unchanged by d |
| 12 | Giustarini, 2023 | 37237960 | How to Increase Cellular Glutathione. |
| 13 | Gould & Pazdro, 2019 | 31083508 | Impact of Supplementary Amino Acids, Micronutrients, and Overall Diet on Glutathione Homeostasis. |
| 14 | Gregory, 2016 | 26765812 | Vitamin B6 nutritional status and cellular availability of pyridoxal 5'-phosphate govern the functio |
| 15 | Hsu, 2015 | 25933612 | Role of vitamin B6 status on antioxidant defenses, glutathione, and related enzyme activities in mic |
| 16 | Jain, 2001 | 11165869 | (ver esumary) |
| 17 | Kabil, 1999 | 10531322 | Deletion of the regulatory domain in the pyridoxal phosphate-dependent heme protein cystathionine be |
| 18 | Kannan & Jain, 2004 | 14975445 | Effect of vitamin B6 on oxygen radicals, mitochondrial membrane potential, and lipid peroxidation in |
| 19 | Kato, 2026 | 42196957 | Potential Role of Vitamin B6 as an Antioxidant via Pyridoxal-5'-Phosphate-Dependent Metabolic Pathwa |
| 20 | Labarrere & Kassab, 2022 | 36386929 | Glutathione: A Samsonian life-sustaining small molecule that protects against oxidative stress, agei |
| 21 | Lai, 2020 | 32635181 | Impact of Glutathione and Vitamin B-6 in Cirrhosis Patients: A Randomized Controlled Trial and Follo |
| 22 | Lamers, 2009 | 19515736 | Vitamin B-6 restriction tends to reduce the red blood cell glutathione synthesis rate without affect |
| 23 | Lapenna, 2023 | 37683986 | Glutathione and glutathione-dependent enzymes: From biochemistry to gerontology and successful aging |
| 24 | Lima, 2006 | 16857832 | Vitamin B-6 deficiency suppresses the hepatic transsulfuration pathway but increases glutathione con |
| 25 | Mahfouz, 2004 | 15203107 | Vitamin C or Vitamin B6 supplementation prevent the oxidative stress and decrease of prostacyclin ge |
| 26 | Mahfouz, 2009 | 20209473 | Vitamin B6 compounds are capable of reducing the superoxide radical and lipid peroxide levels induce |
| 27 | Matxain, 2006 | 17134167 | Theoretical study of the antioxidant properties of pyridoxine. |
| 28 | Matxain, 2009 | 19558175 | Evidence of high *OH radical quenching efficiency by vitamin B6. |
| 29 | Meier, 2001 | 11483494 | Structure of human cystathionine beta-synthase: a unique pyridoxal 5'-phosphate-dependent heme prote |
| 30 | Mosharov, 2000 | 11041866 | The quantitatively important relationship between homocysteine metabolism and glutathione synthesis  |
| 31 | Natera, 2012 | 22231514 | The role of vitamin B6 as an antioxidant in the presence of vitamin B2-photogenerated reactive oxyge |
| 32 | Nuhu, 2020 | 32933160 | Measurement of Glutathione as a Tool for Oxidative Stress Studies by High Performance Liquid Chromat |
| 33 | Pajares, 2025 | 40141131 | Posttranslational Regulation of Mammalian Sulfur Amino Acid Metabolism. |
| 34 | Pusceddu, 2019 | 31129702 | Subclinical inflammation, telomere shortening, homocysteine, vitamin B6, and mortality: the Ludwigsh |
| 35 | Ramis, 2019 | 31480509 | How Does Pyridoxamine Inhibit the Formation of Advanced Glycation End Products? The Role of Its Prim |
| 36 | Sbodio, 2018 | 30007014 | Regulators of the transsulfuration pathway. |
| 37 | Shen, 2010 | 19955400 | Association of vitamin B-6 status with inflammation, oxidative stress, and chronic inflammatory cond |
| 38 | Singh, 2011 | 21315854 | PLP-dependent H(2)S biogenesis. |
| 39 | Stipanuk, 2004 | 15189131 | Sulfur amino acid metabolism: pathways for production and removal of homocysteine and cysteine. |
| 40 | Stipanuk, 2020 | 33000151 | Metabolism of Sulfur-Containing Amino Acids: How the Body Copes with Excess Methionine, Cysteine, an |
| 41 | Taoka, 1999 | 10052944 | Characterization of the heme and pyridoxal phosphate cofactors of human cystathionine beta-synthase  |
| 42 | Valgimigli, 2023 | 37759691 | Lipid Peroxidation and Antioxidant Protection. |
| 43 | Wondrak & Jacobson, 2012 | 22116705 | Vitamin B6: beyond coenzyme functions. |
| 44 | Yadav, 2012 | 22977242 | Allosteric communication between the pyridoxal 5'-phosphate (PLP) and heme sites in the H2S generato |
| 45 | Zhu, 2008 | 18476726 | Kinetic properties of polymorphic variants and pathogenic mutants in human cystathionine gamma-lyase |

## §4 — CORREÇÕES DE AUDITORIA APLICADAS (não reverter)
1. **Kannan & Jain, 2004** (14975445): 1º autor é Kannan K — a triagem citava "Jain/Kannan 2004"; chave canônica corrigida.
2. **Itoh, 2024** (claim B6.SM02.011): periódico NÃO indexado no PubMed → entrou como [G1] com candidato registrado no §5; chave NÃO carregada no índice.
3. **Wondrak & Jacobson, 2012** (22116705) e **Ereño-Orbea**: Wondrak NÃO estava nos 93 DOIs do insumo → adicionado por busca dirigida (confere com a triagem); Ereño-Orbea não localizada → fora.
4. **Taoka, 1999** = 2 registros JBC (10052944/10529187) → citado apenas o 1º; **Singh 2011 ≠ Singh 2007** (chave única 2011).
5. Não localizadas e fora: Chen X 2006, Smith 2012, Tu 2018, Lu 2023 (não no insumo/sem match seguro).

## §5 — NÃO-INDEXADOS / NAO-IDX
| Item | Motivo/destino |
|---|---|
| Itoh, 2024 — 10.1016/j.nutos.2024.03.011 | periódico não indexado (claim B6.11 virou [G1]) |
| Dawood, 2024 — 10.32947/ajps.v24i1.1030 | revista não indexada (planta) |
| Kéry, 1994 / Hu, 1995 | JBC/Chem-Biol Interact clássicos sem resolução por DOI — não eram âncoras do corpo |
| Lee, 2019 (crystallography) / Mendes, 2017 / Serhiyenko, 2025 / Shrayner, 2025 / Velásquez, 2019 / Li, 2026 | revistas regionais/cristalografia/fora de escopo |

## §6 — NÃO CITADAS NO GPM (51 do insumo) — registro para Rodada 2

**B6-vitamina/estado (19):** An 2019 (31601260); Ankisettypalli 2016 (26823273); Bajic 2022 (35454125); Balakina 2021 (34573083); Chen 2003 (14642387); Christen 2018 (29776960); Ciapaite 2023 (37451483); Danielyan 2017 (28024289); Ford 2018 (30513795); Havaux 2009 (19903353); Li 2025 (40218880); Lindschinger 2019 (31915511); Lu 2023 (36717385); Ngo 2022 (35390394); Pilesi 2024 (38830901); Rivero 2024 (38542149); Song 2009 (19491213); Wilson 2019 (30671974); Yin 2025 (41393929).

**estrutura/cinética CBS-CGL (11):** Chen 2006 (16619244); Devi 2019 (31132312); Ishii 2010 (20566639); Lee 2025 (40044138); Matoba 2020 (32913258); Petrosino 2022 (35864237); Prudova 2006 (16614071); Singh 2007 (17534535); Smith 2012 (22738154); Taoka 1999 (10529187); Tu 2018 (29630349).

**glutationa/redox geral (CONTEXT) (4):** Chen 2024 (38279310); Giustarini 2017 (28807817); Hacham 2024 (39441545); Schmitt 2015 (26262996).

**outros (17):** Bønaa 2006 (16531614); Chen 2021 (33414386); Dawood 2024 (NAO-IDX); Hu 1995 (NAO-IDX); Itoh 2024 (NAO-IDX); Kéry 1994 (NAO-IDX); Lee 2019 (NAO-IDX); Li 2026 (NAO-IDX); Liu 2025 (39960689); Lizzo 2022 (35821844); Mendes 2017 (NAO-IDX); Neugart 2020 (31961357); Serhiyenko 2025 (NAO-IDX); Shrayner 2025 (NAO-IDX); Velásquez 2019 (NAO-IDX); Xi 2025 (39762627); Zhou 1991 (1653565).

> **Motivo geral:** SUP estrutural, desdobramentos temáticos e CAMADA C/E (outras doenças) que a triagem separou da camada canônica. Nenhum descarte por contrariar tese.

## §7 — RECONCILIAÇÃO ESTRUTURAL (triagem → GPM)
- Matriz canônica incorporada como espinha: claims mapeados 1:1 no M09; regras causais da triagem reproduzidas no M00.
- Números de efeito/grandezas da triagem NÃO foram copiados (alegação a confirmar em rodada de quantificação).
- Camadas A/B/C e níveis de evidência preservados como tags; dupla classificação permitida.
- Cadeia causal-mãe representada no ID do mecanismo com cada seta como unidade de evidência.

## §8 — PENDÊNCIAS [G1] PARA A RODADA 2

1. PMID do estudo neuronal 2024 (Itoh) ou âncora substituta indexada (claim B6.11).
2. Nrf2/NADPH: revisões adicionais e eventual estudo experimental (hoje [G1] via Kato, 2026).
3. Polimorfismos CBS/CGL comuns ↔ fenótipo psiquiátrico (zero na coleção).
4. Âncoras cruzadas: Se/GPx e Zn/Cu-SOD no B8; cortisol→redox no B2; plasticidade redox-sensível no B3.
5. Dose-resposta humana de vitâmeros (gradiente restrição/deficiência/suplementação).
6. Marcadores de peroxidação padronizados (TBARS vs isoprostanos vs HNE) para rodadas seguintes.

---

**Fecho:** B6 entra na Rodada 2 com biblioteca 100% verificável (45 chaves → 45 PMIDs, zero falhas), zero PMID/DOI no corpo, NAO-IDX registrados e regras causais da triagem como espinha do módulo.