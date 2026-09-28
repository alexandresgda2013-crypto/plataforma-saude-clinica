# BRIEFING — RODADA 0 — B9 — DISFUNÇÃO MITOCONDRIAL (ATUALIZAÇÃO)
### Dossiê de referências do GPM — PMIDs cravados, auditoria PubMed E-utilities, reconciliação com a triagem científica (matriz canônica) e insumo Consensus/DOIs

> **Status:** GPM atualizado (M00–M10, molde v2.0 com (Autor, Ano); substitui a versão em `2 ANTIGOS/2026-09-08/`) · 47 âncoras → 100% com PMID · corpo limpo (zero PMID/DOI) · trinca = GPM + este briefing + `CHECKLIST_SANIDADE_GPM_B9.md`
> **Fontes:** Artigos cientificos do mecanismo B9 disfunção mitocondrial 08.09.26 (152 refs) + Resumo do insumo B9 Chatgpt (7 submecanismos; camadas A–E) + briefing científico B9

## §1 — MÉTODO DE AUDITORIA
1. Insumo convertido em entradas (autor/ano/DOI) e auditado **DOI→PMID** no PubMed E-utilities (esearch individual + esumary em lote): resultados no `SUPORTE/pmid_map.json`/`meta_pmid.json`.
2. Âncoras citadas fora do insumo resolvidas por **buscas dirigidas** (título/autor/DOI) e confirmadas por esumary antes de entrar no anchormap.
3. Anchormap final: `SUPORTE/b9_anchormap.json` — 47 chaves, zero falhas.
4. Índice do GPM regenerado por script (bidirecional corpo↔índice); corpo validado com ZERO PMID/DOI.

## §2 — ESTATÍSTICAS DO GPM (atualizado)
| Métrica | Valor |
|---|---|
| Âncoras no anchormap | 47 |
| Chaves citadas no corpo | 47/47 |
| PMID/DOI no corpo | ZERO |
| Regras fundadoras (M00) | 12 (ROS-sinal; 4-fenômenos-mtDNA; MR-qualificador; camadas A–E) |
| Vias (M01) | 10 |
| Inventário negativo (M02) | 10 |
| Fenótipos (M07) | 7 (F1–F7) |
| Controvérsias (M08) | 10 |
| Submecanismos B9.1–B9.7 (M09) | 7/7 |
| EXTRAPOLAÇÃO POR ANALOGIA | 5 |
| [G1] | 17 |
| Autoauditorias | 11 blocos |

## §3 — TABELA-MESTRA (47 âncoras → PMID)
| # | Chave (Autor, Ano) | PMID | Título (resumo) |
|---|---|---|---|
| 1 | Alaimo, 2014 | 24632637 | Deregulation of mitochondria-shaping proteins Opa-1 and Drp-1 in manganese-induced apoptosis. |
| 2 | Angelova, 2018 | 29292494 | Role of mitochondrial ROS in the brain: from physiology to neurodegeneration. |
| 3 | Burté, 2014 | 25486875 | Disturbed mitochondrial dynamics and neurodegenerative disorders. |
| 4 | Cai, 2015 | 26687620 | Genetic Control over mtDNA and Its Relationship to Major Depressive Disorder. |
| 5 | Cai, 2024 | 38857809 | Drp1 and neuroinflammation: Deciphering the interplay between mitochondrial dynamics imbalance and i |
| 6 | Cao, 2017 | 28114303 | MFN1 structures reveal nucleotide-triggered dimerization critical for mitochondrial fusion. |
| 7 | Carelli, 2015 | 25820230 | Syndromic parkinsonism and dementia associated with OPA1 missense mutations. |
| 8 | Ceylan, 2023 | 38161720 | Mitochondrial DNA oxidation, methylation, and copy number alterations in major and bipolar depressio |
| 9 | Chandhok, 2017 | 29068134 | Structure, function, and regulation of mitofusin-2 in health and disease. |
| 10 | Chang, 2015 | 25946463 | Mitochondria DNA change and oxidative damage in clinically stable patients with major depressive dis |
| 11 | Culmsee, 2019 | 30687139 | Mitochondria, Microglia, and the Immune System-How Are They Linked in Affective Disorders? |
| 12 | Dong, 2023 | 37985735 | Mitochondrial fission drives neuronal metabolic burden to promote stress susceptibility in male mice |
| 13 | Emmerzaal, 2020 | 32488052 | Impaired mitochondrial complex I function as a candidate driver in the biological stress response an |
| 14 | Feng, 2019 | 31760107 | Dynamin-related protein 1: A protein critical for mitochondrial fission, mitophagy, and neuronal dea |
| 15 | Fernström, 2021 | 34789750 | Blood-based mitochondrial respiratory chain function in major depression. |
| 16 | Fernández-Pech, 2026 | 41921723 | Mitochondrial signals in the bloodstream: Peripheral signature of mitochondrial dysfunction in menta |
| 17 | Gebara, 2020 | 33583561 | Mitofusin-2 in the Nucleus Accumbens Regulates Anxiety and Depression-like Behaviors Through Mitocho |
| 18 | Hollis, 2015 | 26621716 | Mitochondrial function in the brain links anxiety with social subordination. |
| 19 | Javani, 2022 | 35065970 | Mitochondrial transplantation improves anxiety- and depression-like behaviors in aged stress-exposed |
| 20 | Karabatsiakis, 2014 | 26126180 | Mitochondrial respiration in peripheral blood mononuclear cells correlates with depressive subsympto |
| 21 | Karabatsiakis, 2020 | 32647150 | Depression, mitochondrial bioenergetics, and electroconvulsive therapy: a new approach towards perso |
| 22 | Kowalczyk, 2021 | 34948180 | Mitochondrial Oxidative Stress-A Causative Factor and Therapeutic Target in Many Diseases. |
| 23 | Kuffner, 2020 | 32260327 | Major Depressive Disorder is Associated with Impaired Mitochondrial Function in Skin Fibroblasts. |
| 24 | Lagos, 2025 | 42248856 | Disease-causing MFN2 mutants impair mitochondrial fission dynamics by distinct DRP1 dysregulation. |
| 25 | Lindqvist, 2018 | 29453441 | Circulating cell-free mitochondrial DNA, but not leukocyte mitochondrial DNA copy number, is elevate |
| 26 | Lutz, 2009 | 19546216 | Loss of parkin or PINK1 function increases Drp1-dependent mitochondrial fragmentation. |
| 27 | Mafikandi, 2024 | 39333279 | Nasal administration of mitochondria relieves depressive- and anxiety-like behaviors in male mice ex |
| 28 | Marques, 2021 | 34066918 | Mitochondrial Alterations in Fibroblasts of Early Stage Bipolar Disorder Patients. |
| 29 | Napolitano, 2021 | 34829696 | Mitochondrial Management of Reactive Oxygen Species. |
| 30 | Otera, 2013 | 23434681 | New insights into the function and regulation of mitochondrial fission. |
| 31 | Palma, 2023 | 38081963 | ROS production by mitochondria: function or dysfunction? |
| 32 | Patergnani, 2021 | 33672477 | Mitochondrial Oxidative Stress and "Mito-Inflammation": Actors in the Diseases. |
| 33 | Poole, 2008 | 18230723 | The PINK1/Parkin pathway regulates mitochondrial morphology. |
| 34 | Rosenberg, 2023 | 37563104 | Brain mitochondrial diversity and network organization predict anxiety-like behavior in male mice. |
| 35 | Scaini, 2021 | 34650203 | Dysregulation of mitochondrial dynamics, mitophagy and apoptosis in major depressive disorder: Does  |
| 36 | Stefanatos, 2018 | 29106705 | The role of mitochondrial ROS in the aging brain. |
| 37 | Tian, 2026 | 41848740 | Astragaloside IV Confers Prophylactic Efficacy Against Depression Associated with the ROS/Nrf2/Keap1 |
| 38 | Triebelhorn, 2021 | 35732695 | Induced neural progenitor cells and iPS-neurons from major depressive disorder patients show altered |
| 39 | Ulecia-Morón, 2025 | 40410878 | Chronic mild stress disrupts mitophagy and mitochondrial status in rat frontal cortex |
| 40 | Visentin, 2020 | 32351669 | Targeting Inflammatory-Mitochondrial Response in Major Depression: Current Evidence and Further Chal |
| 41 | Watanabe, 2022 | 36252817 | Social isolation induces succinate dehydrogenase dysfunction in anxious mice. |
| 42 | Xie, 2020 | 32045672 | Depression-like behaviors are accompanied by disrupted mitochondrial energy metabolism in chronic co |
| 43 | Xie, 2025 | 40668505 | Elevated Acetylation of MFN2 is Accompanied by the Disruption of Mitochondrial Energy Metabolism and |
| 44 | Xue, 2026 | 41634133 | Powering the mind: deciphering the shared genetic architecture between mitochondrial DNA copy number |
| 45 | Yapa, 2021 | 33742459 | Mitochondrial dynamics in health and disease. |
| 46 | Yu, 2011 | 21613270 | The PINK1/Parkin pathway regulates mitochondrial dynamics and function in mammalian hippocampal and  |
| 47 | Zanfardino, 2025 | 40149969 | The Balance of MFN2 and OPA1 in Mitochondrial Dynamics, Cellular Homeostasis, and Disease. |

## §4 — CORREÇÕES DE AUDITORIA APLICADAS (não reverter)
1. **Scaini = 2021** (34650203, print) — triagem dizia 2022; ano canônico corrigido.
2. **Ulecia-Morón = 2025** (40410878, J Transl Med — estresse crônico×mitofagia/status mitocondrial no córtex frontal; DOI do insumo 10.1186/s12967-025-06604-1). **CORREÇÃO 09/09 (com ordem do usuário):** a rodada havia ancorado o homônimo de 2026 (42606669, Molecular Biomedicine — outro artigo); trocado pelo paper do insumo, verificado por esumary.
3. **Yu, 2011 = 21613270** resolvido (PINK1/Parkin dinâmica/função em neurônios mamários).
4. **Fernández-Pech, 2026 = 41921723** (SR ccf-mtDNA em psiquiatria) — NÃO estava nos 152 DOIs; adicionada por busca dirigida (título confere).
5. **Lu, 2024 (MR bidirecional)** NÃO resolvido no PubMed nesta rodada → claim qualificador permanece com [G1] e registro no §8 (link ScienceDirect da triagem arquivado no briefing).
6. **Triebelhorn, 2024** (eletrofisiologia iPSC) não localizado → [G1]; mantido Triebelhorn, 2021 (35732695).
7. **Kannan & Jain analogia do B6 não se aplica aqui — bônus do insumo**: Karabatsiakis, 2020 (ECT × bioenergética) e Xie, 2025 (acetilação de MFN2) incorporados como âncoras adicionais.
8. Marques, 2021 e Chang, 2015 = **bipolar** → rotulados F7/fronteira, sem colapsar em MDD.

## §5 — NÃO-INDEXADOS / NAO-IDX
| Item | Motivo/destino |
|---|---|
| Heyat, 2024 — 10.1007/s40747-024-01346-x | registro sem match PubMed (revisão de ML/saúde) |
| Niu, 2024 — 10.1101/2024.04.25.24306401 | preprint medRxiv |
| Nunes, 2025 — 10.3390/clinbioenerg1010006 | periódico novo não indexado |
| Lu, 2024 — J Affect Disord (S016503272401396X) | DOI não resolvido nesta rodada → [G1] §8 |

## §6 — NÃO CITADAS NO GPM (107 do insumo) — registro para Rodada 2

**dinâmica/fissão-fusão (básico) (17):** Bertholet 2016 (26494254); Chang 2010 (20649536); Chen 2009 (19808793); Colpman 2023 (37508561); Dagda 2009 (19279012); Deng 2008 (18799731); Grel 2023 (37685840); Han 2020 (32484300); Hu 2017 (28098754); Ko 2021 (33805672); Li 2025 (41169572); Ojaimi 2022 (36135912); Oliver 2019 (31450774); Portz 2021 (33924585); Tang 2024 (39191736); Xi 2025 (39976201); Yang 2008 (18443288).

**humana MDD/ansiedade (19):** Allen 2018 (29928190); Bansal 2016 (26923778); Bhatt 2020 (32404275); Correia 2023 (36830028); Cullen 2026 (41776167); Ding 2020 (33237755); Filiou 2019 (31362874); Jiang 2024 (38334212); Khan 2023 (37189442); Kim 2019 (30585734); Lee 2025 (41009813); Liu 2025 (40427494); Morris 2020 (32564227); Olsen 2013 (23383735); Papageorgiou 2024 (39089419); Rollins 2009 (19290059); Sequeira 2015 (26011537); Villa 2017 (28431972); Wang 2022 (35855329).

**mitofagia (3):** Li 2021 (34362731); Li 2022 (36503124); Xian 2019 (30894073).

**mtDNA (27):** Aytaç 2025 (41344231); Beck 2025 (40517524); Burr 2026 (41922875); Chang 2014 (24447331); Chung 2019 (31639552); Czarny 2020 (31081430); Czarny 2023 (37834200); Filograna 2020 (33314045); Filograna 2019 (30949583); Franczak 2026 (41907442); Glynos 2023 (37878704); Gupta 2023 (37587338); Hummel 2022 (36462294); Kasahara 2017 (29102411); Klein 2021 (34742335); Li 2018 (29801445); Lu 2024 (39197553); Nissanka 2018 (29281123); Ryan 2022 (36216200); Tian 2024 (39313624); Tranah 2018 (29984425); Tymofiyeva 2018 (29500956); Wang 2017 (28647451); Wei 2017 (28153046); Yin 2025 (40915505); Zhang 2017 (29157198); Zong 2026 (41792945).

**redox/inflamação/outros (41):** Barnett 2026 (42497856); Bergman 2016 (27412728); Brown 2025 (40436283); Chan 2020 (31585519); Charidemou 2026 (42352333); Choi 2024 (39063194); Gao 2017 (28379197); Glancy 2020 (32358865); Gore 2021 (34605675); Heyat 2024 (NAO-IDX); Hofstra 2024 (38800537); Jomová 2023 (37597078); Juhász 2025 (40317489); Kageyama 2025 (40149919); Kalimon 2023 (36841465); Khaliulin 2024 (39223276); Kleinauskas 2026 (42352055); Liu 2023 (37344456); Liu 2021 (33655635); Liu 2026 (42282151); Lu 2022 (36531636); Morcillo 2024 (38858390); Niu 2024 (NAO-IDX); Nunes 2025 (NAO-IDX); Park 2021 (33774476); Picca 2020 (32707949); Pijuan 2022 (35177962); Scaini 2017 (28463235); Shi 2026 (42238570); Smullen 2023 (37369829); Sukhorukov 2024 (39684566); Tábara 2024 (39420231); Teranishi 2024 (39457098); Tilokani 2018 (30030364); Tomas 2017 (29065167); Trofin 2025 (40227270); Verbal 2026 (41836028); Wolf 2019 (31609012); Yu 2020 (32595603); Zhang 2022 (35213291); Zhao 2023 (37774988).

> **Motivo geral:** SUP estrutural, desdobramentos temáticos e CAMADA C/E (outras doenças) que a triagem separou da camada canônica. Nenhum descarte por contrariar tese.

## §7 — RECONCILIAÇÃO ESTRUTURAL (triagem → GPM)
- Matriz canônica incorporada como espinha: claims mapeados 1:1 no M09; regras causais da triagem reproduzidas no M00.
- Números de efeito/grandezas da triagem NÃO foram copiados (alegação a confirmar em rodada de quantificação).
- Camadas A/B/C e níveis de evidência preservados como tags; dupla classificação permitida.
- Cadeia causal-mãe representada no ID do mecanismo com cada seta como unidade de evidência.

## §8 — PENDÊNCIAS [G1] PARA A RODADA 2

1. PMID de Lu, 2024 (MR) — reprocessar quando indexar; até lá [G1].
2. Triebelhorn, 2024 (iPSC eletrofisiologia) — localizar/substituir.
3. UPRmt e biogênese (PGC-1α) com âncoras próprias.
4. Ferroptose × B9 (fronteira com B8) e medição humana direta (imagem/mito-PET).
5. Sexo e medicação antidepressiva como confundidores das medidas humanas.
6. Replicação do fenótipo ccf-mtDNA em coortes longitudinais (hoje SR sinaliza heterogeneidade).

---

**Fecho:** B9 entra na Rodada 2 com biblioteca 100% verificável (47 chaves → 47 PMIDs, zero falhas), zero PMID/DOI no corpo, NAO-IDX registrados e regras causais da triagem como espinha do módulo.