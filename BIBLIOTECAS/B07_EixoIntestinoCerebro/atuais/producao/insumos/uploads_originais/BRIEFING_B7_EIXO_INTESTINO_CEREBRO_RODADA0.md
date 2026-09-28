# BRIEFING — RODADA 0 — B7 — EIXO INTESTINO–CÉREBRO / MICROBIOTA (ATUALIZAÇÃO)
### Dossiê de referências do GPM — PMIDs cravados, auditoria PubMed E-utilities, reconciliação com a triagem científica (matriz canônica) e insumo Consensus/DOIs

> **Status:** GPM atualizado (M00–M10, molde v2.0 com (Autor, Ano); substitui a versão em `2 ANTIGOS/2026-09-08/`) · 31 âncoras → 100% com PMID · corpo limpo (zero PMID/DOI) · trinca = GPM + este briefing + `CHECKLIST_SANIDADE_GPM_B7.md`
> **Fontes:** Artigos cientificos do mecanismo B7 eixo intestino cérebro 08.09.26 (178 refs) + Resumo do insumo B7 Chatgpt (matriz 34 claims) + 5 PDFs de fase anterior

## §1 — MÉTODO DE AUDITORIA
1. Insumo convertido em entradas (autor/ano/DOI) e auditado **DOI→PMID** no PubMed E-utilities (esearch individual + esumary em lote): resultados no `SUPORTE/pmid_map.json`/`meta_pmid.json`.
2. Âncoras citadas fora do insumo resolvidas por **buscas dirigidas** (título/autor/DOI) e confirmadas por esumary antes de entrar no anchormap.
3. Anchormap final: `SUPORTE/b7_anchormap.json` — 31 chaves, zero falhas.
4. Índice do GPM regenerado por script (bidirecional corpo↔índice); corpo validado com ZERO PMID/DOI.

## §2 — ESTATÍSTICAS DO GPM (atualizado)
| Métrica | Valor |
|---|---|
| Âncoras no anchormap | 31 |
| Chaves citadas no corpo | 30/30 |
| PMID/DOI no corpo | ZERO |
| Regras fundadoras (M00) | 10 (inclui B7-CAUSAL-01/02/03 verbatim) |
| Vias (M01) | 10 (cadeia-mãe por trecho) |
| Inventário negativo (M02) | 10 |
| Fenótipos (M07) | 4 (F1–F4) |
| Controvérsias (M08) | 10 |
| Submódulos B7-01–B7-12 (M09) | 12/12 (B7-07 e B7-09 marcados [G1]) |
| EXTRAPOLAÇÃO POR ANALOGIA | 2 |
| [G1] | 16 |
| Autoauditorias | 11 blocos |

## §3 — TABELA-MESTRA (30 âncoras → PMID)
| # | Chave (Autor, Ano) | PMID | Título (resumo) |
|---|---|---|---|
| 1 | Aburto & Cryan, 2024 | 38355758 | Gastrointestinal and brain barriers: unlocking gates of communication across the microbiota-gut-brai |
| 2 | Agus, 2018 | 29902437 | Gut Microbiota Regulation of Tryptophan Metabolism in Health and Disease. |
| 3 | Barki, 2022 | 35229717 | Chemogenetics defines a short-chain fatty acid receptor gut-brain axis. |
| 4 | Bonaz, 2018 | 29467611 | The Vagus Nerve at the Interface of the Microbiota-Gut-Brain Axis. |
| 5 | Bosi, 2020 | 32577079 | Tryptophan Metabolites Along the Microbiota-Gut-Brain Axis: An Interkingdom Communication System Inf |
| 6 | Braniste, 2014 | 25411471 | The gut microbiota influences blood-brain barrier permeability in mice. |
| 7 | Caetano-Silva, 2023 | 36797287 | Inhibition of inflammatory microglia by dietary fiber and short-chain fatty acids. |
| 8 | Carabotti, 2015 | 25830558 | The gut-brain axis: interactions between enteric microbiota, central and enteric nervous systems. |
| 9 | Chen, 2021 | 34127024 | Tryptophan-kynurenine metabolism: a link between the gut and brain for depression in inflammatory bo |
| 10 | Chen, 2024 | 38939042 | Brain Short-Chain Fatty Acids Induce ACSS2 to Ameliorate Depressive-Like Behavior via PPARγ-TPH2 Axi |
| 11 | Cheng, 2024 | 38390241 | Gut microbiota-derived short-chain fatty acids and depression: deep insight into biological mechanis |
| 12 | Cryan, 2019 | 31460832 | The Microbiota-Gut-Brain Axis. |
| 13 | Erny, 2021 | 34731656 | Microbiota-derived acetate enables the metabolic fitness of the brain innate immune system during he |
| 14 | Guo, 2013 | 23201091 | Lipopolysaccharide causes an increase in intestinal tight junction permeability in vitro and in vivo |
| 15 | Guo, 2015 | 26466961 | Lipopolysaccharide Regulation of Intestinal Tight Junction Permeability Is Mediated by TLR4 Signal T |
| 16 | Góralczyk-Bińkowska, 2022 | 36232548 | The Microbiota-Gut-Brain Axis in Psychiatric Disorders. |
| 17 | Hwang, 2025 | 39940928 | Interaction of the Vagus Nerve and Serotonin in the Gut-Brain Axis. |
| 18 | Kurita, 2020 | 31910709 | Metabolic endotoxemia promotes neuroinflammation after focal cerebral ischemia. |
| 19 | Li, 2023 | 36746244 | Tryptophan-kynurenine metabolic characterization in the gut and brain of depressive-like rats induce |
| 20 | Lin, 2023 | 37049591 | Dysbiosis of the Gut Microbiota and Kynurenine (Kyn) Pathway Activity as Potential Biomarkers in Pat |
| 21 | Margolis & Cryan, 2021 | 33493503 | The Microbiota-Gut-Brain Axis: From Motility to Mood. |
| 22 | Nighot, 2017 | 29157665 | Lipopolysaccharide-Induced Increase in Intestinal Epithelial Tight Permeability Is Mediated by Toll- |
| 23 | Nighot, 2019 | 30711488 | Lipopolysaccharide-Induced Increase in Intestinal Permeability Is Mediated by TAK-1 Activation of IK |
| 24 | Saikachain, 2023 | 37070532 | Neuroprotective effect of short-chain fatty acids against oxidative stress-induced SH-SY5Y injury vi |
| 25 | Sathyasaikumar, 2024 | 38911967 | The Tryptophan Metabolite Indole-3-Propionic Acid Raises Kynurenic Acid Levels in the Rat Brain In V |
| 26 | Schwarcz, 2024 | 38612489 | The Probiotic Lactobacillus reuteri Preferentially Synthesizes Kynurenic Acid from Kynurenine. |
| 27 | Socała, 2021 | 34450312 | The role of microbiota-gut-brain axis in neuropsychiatric and neurological disorders. |
| 28 | Spichak, 2021 | 34589808 | Microbially-derived short-chain fatty acids impact astrocyte gene expression in a sex-specific manne |
| 29 | Zhao, 2023 | 36776388 | DSS-induced colitis activates the kynurenine pathway in serum and brain by affecting IDO-1 and gut m |
| 30 | Zhou, 2023 | 37386523 | Microbiome and tryptophan metabolomics analysis in adolescent depression: roles of the gut microbiot |

## §4 — CORREÇÕES DE AUDITORIA APLICADAS (não reverter)
1. **PMIDs da matriz da triagem 100% confirmados** pela auditoria própria: Braniste 25411471; Barki 35229717; Erny 34731656; Caetano-Silva 36797287; Chen 38939042; Kurita 31910709; Zhao 36776388; Li 36746244; Agus 29902437; Bosi 32577079; Schwarcz 38612489; Sathyasaikumar 38911967; Zhou 37386523; Lin 37049591; Saikachain 37070532; Spichak 34589808; Guo 23201091/26466961; Nighot 29157665/30711488.
2. **Chen 2024 = 2 papers** (ACSS2/TPH2 = 38939042; metaboloma do triptofano = 39408347) → apenas o ACSS2 citado, chave única.
3. **Zhao 2023 = 2 papers** (36776388 KYN sérico+cerebral; 36758839 colite aguda) → citado apenas 36776388 (o da matriz).
4. **Carabotti, 2015 = 25830558** resolvido por busca dirigida (entrada do insumo sem DOI).
5. **Socała, 2021 = 34450312** resolvido por DOI (PDF de fase anterior incorporado como revisão de arquitetura).
6. Guo/Nighot: os claims .016/.017 da matriz pediam "validar registro" → validados e ancorados (Guo 2013/2015; Nighot 2017/2019).

## §5 — NÃO-INDEXADOS / NAO-IDX
| Item | Motivo/destino |
|---|---|
| Carabotti, 2015 — sem DOI no insumo | RESOLVIDO por busca dirigida (25830558) |
| Thomas, 2021 — 10.1101/2021.07.21.453192 | preprint bioRxiv |
| Towriss, 2026 — 10.64898/2026.06.30.735602 | preprint |
| Xia, 2025 — 10.1016/j.jfutfo.2024.09.006 / Zhang, 2026 — 10.1007/s42399-026-02275-1 | periódicos não indexados/ainda sem registro PubMed |

## §6 — NÃO CITADAS NO GPM (155 do insumo) — registro para Rodada 2

**barreira/permeabilidade (38):** Akiba 2021 (33403482); Arumugam 2024 (39321109); Assimakopoulos 2012 (22023490); Bein 2017 (27191060); Chelakkot 2018 (30115904); Chen 2017 (28935573); Condette 2014 (25019507); Erikson 2020 (32600371); Feng 2018 (30227623); Georgopoulou 2024 (38397970); Ghosh 2020 (32099951); He 2019 (30747184); Horowitz 2023 (37186118); Kang 2022 (35736894); Koufou 2024 (38255265); Kuo 2021 (34478742); Li 2023 (37009158); Li 2009 (19235836); Ling 2016 (27551722); Liu 2021 (33434620); Mazarati 2021 (33893636); Paradis 2021 (33801524); Qin 2015 (26290681); Reinhold 2016 (27957611); Scalise 2021 (34152937); Shu 2023 (37274298); Tulkens 2018 (30518529); Tunisi 2019 (31024456); Wang 2024 (38855764); Wang 2015 (25970544); Wu 2019 (32131830); Xiao 2018 (29705796); Yan 2017 (28654658); Yang 2015 (25888437); Yoseph 2016 (27299587); Yumoto 2024 (39637366); Zhang 2022 (36558058); Zheng 2022 (36232464).

**outros (35):** Carabotti 2015 (NAO-IDX); Dong 2022 (35596843); Dong 2024 (38336171); Du 2024 (39000498); Facchin 2025 (40801563); He 2020 (32887215); Hou 2021 (33905875); Kalyan 2022 (36552802); Kalyanaraman 2024 (38377788); Kibbie 2021 (34365090); Li 2018 (29875665); Li 2018 (29750914); Lin 2012 (22506074); Liu 2020 (32583667); Luo 2022 (35688319); Mann 2024 (38565643); Martin 2018 (30023410); Nøhr 2013 (23885020); Park 2025 (40804450); Park 2019 (31222050); Porbahaie 2023 (38661366); Prado 2023 (37264394); Qu 2025 (39904963); Sasso 2023 (37156006); Song 2022 (35819092); Thomas 2021 (NAO-IDX); Towriss 2026 (NAO-IDX); Wang 2025 (39833898); Wang 2025 (41201037); Wenzel 2020 (32333962); Xia 2025 (NAO-IDX); Yang 2019 (31784978); Zhang 2026 (NAO-IDX); Zhang 2023 (37596634); Zou 2022 (36199030).

**reviews arquitetura gut-brain (67):** Ahmed 2022 (35903003); Baj 2019 (30934533); Batagianni 2025 (40673654); Cao 2025 (40400035); Chen 2025 (40952592); Costa 2024 (38812976); Deng 2021 (33535879); Ding 2021 (34707612); Doenyas 2025 (39870727); Feng 2019 (31211803); Fock 2023 (36831324); Gao 2019 (31825083); Gao 2018 (29468141); Gheorghe 2019 (31610413); Guo 2025 (40723792); Gupta 2023 (37898179); Hays 2024 (39284033); Honarpisheh 2022 (35420913); Hou 2023 (37999261); Hyland 2022 (35038025); Ikeda 2022 (36057320); Jiang 2026 (42305614); Kandpal 2022 (36355147); Kennedy 2016 (27392632); Kim 2018 (28925886); Leclercq 2021 (34599147); Liaqat 2022 (36014776); Liu 2020 (32829453); Liu 2025 (40903950); Loh 2024 (38360862); Lukic 2022 (36172468); Majumdar 2023 (36868874); Mei 2025 (39998158); Miao 2025 (40765836); Morais 2020 (33093662); Nakhal 2024 (39459534); Ohara 2025 (39743581); Olasunkanmi 2026 (41630697); Osadchiy 2018 (30292888); Palma 2014 (24756641); Petropoulos 2025 (41010510); Qian 2022 (35855330); Roth 2021 (33804088); Schächtle 2021 (34335190); Shekarabi 2024 (38824840); Shen 2026 (41971333); Silva 2020 (32082260); Singh 2024 (38776563); Sittipo 2022 (35706008); Stanimirov 2025 (41465592); Su 2022 (35892593); Suganya 2020 (33066156); Sun 2016 (27448578); Tanaka 2025 (40868271); Tiwari 2025 (39875781); Wang 2026 (42245509); Wang 2016 (27647198); Xu 2026 (41798063); Xu 2025 (40584038); Yassin 2025 (41104042); You 2024 (39036341); Zhang 2026 (41814325); Zhang 2025 (40937571); Zhang 2024 (39716675); Zhao 2023 (36758839); Zheng 2023 (37960284); Zhuang 2024 (39182226).

**triptofano/KYN/indóis (15):** Ala 2021 (34289794); Bertollo 2024 (39245854); Chen 2019 (30977499); Chen 2024 (39408347); Dehhaghi 2019 (31258331); Haq 2021 (34473368); Hestad 2022 (35883554); Höglund 2019 (31024440); Huang 2023 (37191427); Li 2023 (37521424); Salminen 2023 (36757399); Shaw 2023 (37512997); Stone 2023 (38102897); Wang 2025 (40137174); Xu 2025 (40072112).

> **Motivo geral:** SUP estrutural, desdobramentos temáticos e CAMADA C/E (outras doenças) que a triagem separou da camada canônica. Nenhum descarte por contrariar tese.

## §7 — RECONCILIAÇÃO ESTRUTURAL (triagem → GPM)
- Matriz canônica incorporada como espinha: claims mapeados 1:1 no M09; regras causais da triagem reproduzidas no M00.
- Números de efeito/grandezas da triagem NÃO foram copiados (alegação a confirmar em rodada de quantificação).
- Camadas A/B/C e níveis de evidência preservados como tags; dupla classificação permitida.
- Cadeia causal-mãe representada no ID do mecanismo com cada seta como unidade de evidência.

## §8 — PENDÊNCIAS [G1] PARA A RODADA 2

1. Ácidos biliares como ponte neuroativa (B7-07) — sem âncora.
2. HPA-microbiota com cadeia completa (B7-09).
3. FFAR2/3 em humanos; fisiologia vagal humana do eixo.
4. Ensaios probióticos/FMT com desfecho psiquiátrico registrado (hoje só sinal).
5. GABA produzido por microbiota com âncora própria (NEG atual sem âncora B7).
6. Monitorar publicação dos preprints (Thomas; Towriss) e dos periódicos não indexados (Xia; Zhang).

---

**Fecho:** B7 entra na Rodada 2 com biblioteca 100% verificável (30 chaves → 30 PMIDs, zero falhas), zero PMID/DOI no corpo, NAO-IDX registrados e regras causais da triagem como espinha do módulo.