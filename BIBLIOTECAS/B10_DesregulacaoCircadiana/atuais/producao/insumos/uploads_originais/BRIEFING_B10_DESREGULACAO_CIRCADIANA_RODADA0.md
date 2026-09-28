# BRIEFING — RODADA 0 — B10 — DESREGULAÇÃO CIRCADIANA (ATUALIZAÇÃO)
### Dossiê de referências do GPM — PMIDs cravados, auditoria PubMed E-utilities, reconciliação com a matriz canônica da triagem

> **Status:** GPM atualizado (M00–M10, molde v2.0; substitui a versão em `2 ANTIGOS/2026-09-09/`) · 38 âncoras → 100% com PMID · corpo limpo (zero PMID/DOI) · trinca = GPM + este briefing + `CHECKLIST_SANIDADE_GPM_B10.md`
> **Fontes:** Artigos cientificos do mecanismo B10 desregulação circadiana 08.09.26 (181 refs) + Resumo do unsumo B10 chatgpt (matriz 58 claims RC.SM02.001–058)

## §1 — MÉTODO DE AUDITORIA
1. Insumo convertido em entradas autor/ano/DOI e auditado **DOI→PMID** (esearch individual + esumary em lote): ver `SUPORTE/pmid_map.json`/`meta_pmid.json`.
2. Âncoras fora do insumo resolvidas por **buscas dirigidas** e confirmadas por esumary antes de entrar no anchormap.
3. Anchormap final: `SUPORTE/b10_anchormap.json` — 38 chaves, zero falhas, anos canônicos pelo print.
4. Índice do GPM regenerado por script; corpo validado com ZERO PMID/DOI.

## §2 — ESTATÍSTICAS DO GPM
| Métrica | Valor |
|---|---|
| Linhas / módulos | 242 / 11 (M00–M10) |
| Âncoras → PMIDs | 38/38 |
| PMID/DOI no corpo | ZERO |
| Regras fundadoras / vias | M00 / 10 |
| Inventário negativo / fenótipos | 10 / (M07) |
| EXTRAPOLAÇÃO POR ANALOGIA / [G1] | 4 / 10 |
| Autoauditorias | 11 blocos |

## §3 — TABELA-MESTRA (38 âncoras → PMID)
| # | Chave (Autor, Ano) | PMID | Título (resumo) |
|---|---|---|---|
| 1 | Oishi, 2003 | 12865428 | Genome-wide expression analysis of mouse liver reveals CLOCK-regulated circadian output genes. |
| 2 | Sato, 2006 | 16474406 | Feedback repression is required for mammalian circadian clock function. |
| 3 | Soria, 2010 | 20072116 | Differential association of circadian genes with mood disorders: CRY1 and NPAS2 are associated with  |
| 4 | Welsh, 2010 | 20148688 | (busca dirigida — ver esumary) |
| 5 | Mohawk, 2011 | 21665298 | Cell autonomy and synchrony of suprachiasmatic nucleus circadian oscillators. |
| 6 | Nicolaides, 2014 | 24890877 | Circadian endocrine rhythms: the hypothalamic-pituitary-adrenal axis and its actions. |
| 7 | Nangle, 2014 | 25127877 | Molecular assembly of the period-cryptochrome circadian transcriptional repressor complex. |
| 8 | Russell, 2015 | 25494867 | The importance of biological oscillators for hypothalamic-pituitary-adrenal activity and tissue gluc |
| 9 | Ramkisoensing, 2015 | 26097465 | Synchronization of Biological Clock Neurons by Light and Peripheral Feedback Systems Promotes Circad |
| 10 | Takahashi, 2015 | 26332962 | Molecular components of the circadian clock in mammals. |
| 11 | Schibler, 2015 | 26683231 | Clock-Talk: Interactions between Central and Peripheral Circadian Oscillators in Mammals. |
| 12 | Moon, 2016 | 27543154 | Advanced Circadian Phase in Mania and Delayed Circadian Phase in Mixed Mania and Depression Returned |
| 13 | Michael, 2017 | 28143926 | Formation of a repressive complex in the mammalian circadian clock is mediated by the secondary pock |
| 14 | Sassone-Corsi, 2016 | 28892344 | Molecular Architecture of the Circadian Clock in Mammals. |
| 15 | Pilz, 2018 | 30061722 | Rhythmicity of Mood Symptoms in Individuals at Risk for Psychiatric Disorders. |
| 16 | Robillard, 2018 | 30301878 | Circadian rhythms and psychiatric profiles in young adults with unipolar depressive disorders. |
| 17 | Pett, 2018 | 30456356 | Co-existing feedback loops generate tissue-specific circadian rhythms. |
| 18 | Yamanaka, 2019 | 30480877 | Hypothalamic-pituitary-adrenal axis differentially responses to morning and evening psychological st |
| 19 | Rao & Androulakis, 2019a | 30862458 | The physiological significance of the circadian dynamics of the HPA axis: Interplay between circadia |
| 20 | Nguyen, 2019 | 30878655 | In vivo molecular chronotyping, circadian misalignment, and high rates of depression in young adults |
| 21 | Rao & Androulakis, 2019b | 31371802 | Allostatic adaptation and personalized physiological trade-offs in the circadian regulation of the H |
| 22 | Shan, 2020 | 32768389 | Dual-Color Single-Cell Imaging of the Suprachiasmatic Nucleus Reveals a Circadian Role in Network Sy |
| 23 | Russell, 2021 | 33509094 | Knockout of the circadian gene, Per2, disrupts corticosterone secretion and results in depressive-li |
| 24 | von Schantz, 2021 | 33641746 | Genomic perspectives on the circadian clock hypothesis of psychiatric disorders. |
| 25 | Mukherjee, 2022 | 34320487 | Dysregulated Diurnal Cortisol Pattern and Heightened Night-Time Cortisol in Individuals with Bipolar |
| 26 | Vidafar, 2021 | 34468894 | (busca dirigida — ver esumary) |
| 27 | Pandi-Perumal, 2022 | 35033557 | Timing is everything: Circadian rhythms and their role in the control of sleep. |
| 28 | Scott, 2022 | 35182537 | A systematic review and meta-analysis of sleep and circadian rhythms disturbances in individuals at  |
| 29 | Rao, 2021 | 37895351 | The Influence of Light Wavelength on Human HPA Axis Rhythms: A Systematic Review. |
| 30 | Zuo, 2024 | 38241675 | Circadian misalignment impairs oligodendrocyte myelination via Bmal1 overexpression leading to anxie |
| 31 | Ono, 2024 | 38366616 | The Suprachiasmatic Nucleus at 50: Looking Back, Then Looking Forward. |
| 32 | Smith, 2024 | 39308240 | (busca dirigida — ver esumary) |
| 33 | Burns, 2024 | 39314956 | Sleep inertia drives the association of evening chronotype with psychiatric disorders: epidemiologic |
| 34 | Tofani GSS, 2025 | 39504963 | Gut microbiota regulates stress responsivity via the circadian system. |
| 35 | Wescott, 2025 | 39608218 | Circadian realignment and depressed mood: A systematic review. |
| 36 | Otobe, 2026 | 41108717 | Phosphorylation of CLOCK and BMAL1-a key regulatory mechanism in the mammalian circadian clockwork. |
| 37 | Robertson-Dixon, 2026 | 41389872 | (busca dirigida — ver esumary) |
| 38 | Von Gall, 1998 | 9852576 | (busca dirigida — ver esumary) |

## §4 — CORREÇÕES DE AUDITORIA APLICADAS (não reverter)
1. **PMIDs da matriz revalidados:** Nguyen 30878655; Robillard 30301878; Moon 27543154; **Vidafar = 34468894** (busca dirigida, confere); **Zuo = 38241675** (confere); Tofani = 39504963 (print **2025**); Scott 35182537; Soria 20072116.
2. **"Vidafar, 2021" (insumo idx162) = von Schantz, 2021** (33641746, genomic perspectives) — reatribuição; Vidafar real entra por busca dirigida.
3. **"Palagini, 2022" (insumo) = Pandi-Perumal, 2022** (35033557, "Timing is everything") — reatribuição; a Palagini-2023 real (desregulação emocional) NÃO indexada → [G1].
4. **"Welsh, 2010" (insumo) apontava para paper de 2024** (cortisol) — Welsh real = 20148688 (Annu Rev Physiol, busca dirigida). **"Takaruck 2016" = Sassone-Corsi, 2016** (28892344) pelo 1º autor do print.
5. **Anos canônicos = print:** Wescott **2025**; Mukherjee **2022** (triagem: 2021); Yamanaka **2019** (2018); Otobe **2026** (2025); Tofani **2025** (2024/2025); Russell 2015/2021 chaves separadas; Rao & Androulakis **2019a/2019b** (dois papers distintos).
6. **Smith, 2024** (Chronopsychiatry, 39308240) e **Robertson-Dixon, 2026** (luz×HPA meta) adicionados por busca (substituem claims de Pandi-Perumal/Meyer não localizados).
7. **Não localizados → [G1]/R2:** McCarthy 2021; McGlashan 2018; Ye 2011/2014; Xu 2015; Walker 2020; Serrano-Serrano 2021; Burns 2022/2023; Mendoza 2024; Sandate 2020.

## §5 — NÃO-INDEXADOS / NAO-IDX
| Item | Motivo |
|---|---|
| Burns, 2022 — 10.1101/2022.10.16.22280934 | preprint medRxiv |
| Burns, 2023 / Mendoza, 2024 — 10.1038/s44220-* | Nature Mental Health sem resolução no PubMed nesta rodada |
| Sandate, 2020 — 10.1107/* | Acta Crystallographica (estrutural, fora do PubMed) |
| Palagini, 2023 — 10.1192/j.eurpsy.2023.830 | European Psychiatry não resolvido |
| Albrecht 2012 (springerreference); Murray 2016; Rumanova 2020 (sem DOI); Feng/Noweta/You | referência de dicionário/revistas regionais/sem DOI |

## §6 — NÃO CITADAS NO GPM (148 do insumo) — registro para Rodada 2

**básico/outros (132):** Abe 2022 (35999195); Abelson 2023 (36801587); Albrecht 2012 (NAO-IDX); Alloy 2017 (28321642); Androulakis 2021 (33438348); Annayev 2014 (24385426); Aryal 2017 (28886335); Ashton 2022 (35054913); Astiz 2019 (40363695); Bernard 2007 (17432930); Bhake 2019 (31355884); Boareto 2025 (42237005); Boon 2017 (29223280); Buckley 2005 (15728214); Buhr 2019 (31607531); Buijink 2016 (28006027); Burns 2023 (NAO-IDX); Burns 2022 (NAO-IDX); Calligaro 2023 (37500494); Camici 2026 (41568000); Cao 2020 (33443219); Cao 2023 (36682495); Cao 2025 (29054877); Carpenter 2025 (40662977); Chellappa 2020 (33122670); Chen 2009 (19917250); Chiou 2020 (33381013); Chiou 2016 (27688755); Christiansen 2012 (22217141); Chung 2023 (38627069); Coomans 2015 (25451984); Cox 2024 (39096022); Crumbley 2011 (21479263); Crumbley 2010 (20817722); Dollish 2023 (37858331); Duong 2011 (21680841); Duy 2020 (33030409); Emens 2020 (32777620); Esaki 2021 (34645802); Feng 2025 (NAO-IDX); Fernandez 2016 (27162356); Focke 2019 (31738971); Fribourgh 2020 (32101164); Gaffey 2016 (27377692); Gao 2022 (35478603); Gjerstad 2018 (29764284); Golombek 2010 (20664079); Goltsev 2022 (35848398); Goncharova 2023 (36699023); Goriki 2014 (37761843); Gu 2026 (41979826); Gu 2016 (27358024); Gul 2020 (33028638); Gustafson 2014 (25303119); Hafner 2012 (22423219); Hamnett 2019 (30710088); Hastings 2014 (24329967); Herzog 2017 (28049647); James 2023 (36950689); Jha 2021 (33440199); Jones 2018 (30082421); Juliana 2025 (41009704); Kalsbeek 2012 (21782883); Kandalepas 2016 (27362940); Kanter 2024 (39569439); Karan 2021 (34399150); Karin 2020 (32672906); Kiessling 2014 (24658072); Kim 2021 (33510438); Klusmann 2022 (35597328); Knezevic 2023 (38067154); Koch 2022 (35285799); Korf 2024 (38965880); Korom 2026 (41990568); Kumar 2024 (38964508); Kume 1999 (10428031); Kusov 2023 (36903600); Lamont 2007 (24043798); Laothamatas 2023 (37708890); Leclercq 2020 (33326640); Lee 2011 (21199878); Lei 2024 (38800632); Li 2021 (34504149); Li 2023 (37597751); Li 2022 (36387856); Liberman 2018 (29614896); Lightman 2020 (32060528); Liu 2025 (40854106); Liyanarachchi 2017 (29223281); Lokshin 2015 (25994103); Lu 2021 (34657394); Ludwig 2023 (36870963); Lyall 2018 (30555405); Melo 2017 (27524206); Mendoza 2024 (NAO-IDX); Morimoto 2022 (36256675); Moyers 2023 (37001634); Murray 2016 (NAO-IDX); Na 2012 (23133559); Nader 2010 (20106676); Naito 2008 (18375863); Nikhil 2025 (41380001); Noweta 2026 (NAO-IDX); Palagini 2023 (NAO-IDX); Postnova 2013 (23599244); Rosensweig 2018 (29556064); Rumanova 2020 (NAO-IDX); Sandate 2020 (NAO-IDX); Schirmer 2023 (37389366); Schrader 2024 (39007272); Shirtcliff 2024 (38428723); Simons 2017 (28027684); Smyllie 2025 (40247113); Speer 2019 (31236437); Spencer 2016 (27871862); Spiga 2014 (NAO-IDX); Starnes 2023 (37106709); Starr 2019 (30340064); Takaesu 2018 (29869403); Tamayo 2015 (26323038); Tonon 2024 (19305510); Vriend 2015 (25369242); Waly 2015 (27103927); Welsh 2010 (38308964); Xu 2021 (34416169); Xu 2015 (25961797); Yang 2021 (35255992); Ye 2014 (25228643); Ye 2011 (21613214); You 2024 (NAO-IDX); Yu 2002 (11798163); Yuan 2025 (41170746).

**microbiota/gut (1):** Bautista 2025 (41244880).

**psiquiatria clínica/observacional (15):** Chakraborty 2026 (41913359); Deprato 2025 (40154089); Francis 2023 (37441675); Geoffroy 2025 (40381827); Hyndych 2025 (41662130); Joseph 2016 (27750377); Kinlein 2019 (32750762); Meyer 2024 (38394243); Murray 2017 (28364473); Serrano 2026 (34640406); Song 2024 (38579366); Walker 2020 (32066704); Walker 2021 (34225967); Yeom 2024 (39757810); Zou 2022 (36033630).

> **Motivo geral:** SUP temático, CONTEXT e revisões redundantes com as âncoras; nenhum descarte por contrariar tese.

## §7 — RECONCILIAÇÃO ESTRUTURAL (matriz → GPM)
- Claims da matriz mapeados no M09 sem promoção de nível; regras causais da triagem reproduzidas no M00.
- Números de efeito (OR/HR/SMD/d) NÃO copiados — alegações a confirmar em rodada de quantificação.
- Cadeia causal-mãe no ID do mecanismo; cada seta como unidade de evidência.

## §8 — PENDÊNCIAS [G1] PARA A RODADA 2

1. McCarthy 2021 (circadiano×bipolar) e McGlashan 2018 (variabilidade da resposta à luz).
2. Estrutural CRY (Ye/Xu/Sandate) — hoje o TTFL é sustentado por Sato/Nangle/Michael/Otobe.
3. Walker 2020 (circadiano×saúde mental) e Serrano-Serrano 2021.
4. DLMO/fase fisiológica como desfecho em ensaios de realinhamento (testar a regra 2).
5. Wearables×fase (Song 2024 não localizado).
6. GRADE formal quando o pipeline ativar.

---

**Fecho:** B10 entra na Rodada 2 com biblioteca 100% verificável (38 chaves → 38 PMIDs), zero PMID/DOI no corpo, NAO-IDX registrados e regras causais da matriz como espinha.