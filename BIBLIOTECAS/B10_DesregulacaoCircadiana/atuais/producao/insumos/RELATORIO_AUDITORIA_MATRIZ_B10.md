# RELATÓRIO DE AUDITORIA DO INSUMO EXTERNO — B10 (rodada [AT] 2026-09-09, P-7)

**Escopo.** Reconciliação ref a ref do GPM oficial (molde v2.0, M00–M10) + dossiê RODADA0
(38 âncoras → PMID; 148 "não citadas") + matriz ChatGPT (58 claims RC.SM02.001–058) + anexo
(193 entradas parseadas por script) + briefing consolidado v1 (12 sementes) contra a V1 (39 refs).

**Método.** Todo PMID do dossiê revalidado por esummary (182/182 resolvidos); todo DOI do anexo
sem PMID no dossiê resolvido por esearch `DOI[aid]` (16 encontrados, 9 NAO-IDX confirmados);
abstracts efetch lidos nos 106 itens da fila final (directional claims verificados: Murray,
Nguyen, Burns, Song, Cox, Tofani, Zuo, Russell 2021).

## Divergências expostas (12)

| Insumo dizia | Auditoria constatou |
|---|---|
| Lyall 2018 = 30555405 | o PMID é **McGlashan 2018** (a pendência do dossiê!); Lyall real = 29776774 |
| Kinlein 2019 = 32750762 | o PMID é **Kırlıoğlu 2020** (ausente do dossiê); Kinlein real = 31863788 (print 2020) |
| "Serrano 2026" = 34640406 | o PMID é **Serrano-Serrano 2021** (outra pendência do dossiê!); Serrano 2026 eLife real = 42290481 |
| Rao 2021 = 37895351 | o PMID é **Robertson-Dixon 2023** (Life); Rao 2021 real = 34436424 (Metabolites) |
| Astiz 2019 = 40363695 | o PMID é **Başer 2025**; Astiz real = 30650649 |
| "Boon 2017" = 29223280 | mesmo paper: autor é **den Boon** FS (normalização) |
| Cao 2025 = 29054877 | o PMID é **Carmona-Alcocer 2018**; Cao 2025 (Theor. Nat. Sci.) é NAO-IDX → EXC |
| Goriki 2014 = 37761843 | o PMID é **Gršković 2023**; Goriki real = 24736997 |
| Lamont 2007 = 24043798 | o PMID é **Lande-Diner 2013**; Lamont real = 17969870 |
| Tonon 2024 = 19305510 | o PMID é **vanderLeest 2009**; Tonon real = 39210713 |
| "Welsh 2010" §6 = 38308964 | o PMID é **Wesarg-Menzel 2024** (confusão já flagada no §4 do dossiê) |
| Robertson-Dixon 2026 = 41389872 | **correto** (meta análise HPA×luz em animais não humanos) — e existe um irmão de 2023 |

## Sobre-correções/omissões do dossiê
- **Palagini 2022 É REAL** (Clin Neuropsychiatry, 35821870) — o dossiê "corrigiu" a âncora para
  Pandi-Perumal 2022; ambas entram (Palagini ENTRA clínica bipolar; Pandi-Perumal ENTRA revisão sono).
- **Spiga 2014 É indexada** (Compr Physiol, 24944037; o DOI do anexo era espúrio) — dossiê dizia NAO-IDX.
- **15 refs do anexo ausentes do dossiê** cobertas pela auditoria (Aydoğan/Gül 2025; Başer 2025;
  Carmona-Alcocer 2018; Gosztyła 2026; Gršković 2023; Kırlıoğlu 2020; Lande-Diner 2013;
  McCarthy 2021(2022); McGlashan 2018; Palagini 2022; Takahashi 2016 cap.; Van Beurden 2022;
  van Dalfsen 2018; vanderLeest 2009; Wesarg-Menzel 2024).

## Falso positivo estrutural descartado
- **Burns 2024 (âncora #33) = preprint medRxiv indexado no PubMed** (39314956) — elegível como
  registro mas NÃO como evidência canônica → **EXC** com a claim (sleep inertia media cronotipo
  vespertino→psiquiatria) sinalizada [G1] para rodada futura. Burns 2022/2023 e Mendoza 2024
  (Nature Mental Health) NAO-IDX confirmados → [G1].

## Anos canônicos (print) contra o insumo
McCarthy **2022** (ISBD; insumo 2021) · Dollish **2024** (2023) · Ketchesin **2020** (2018) ·
Kinlein & Karatsoreos **2020** (2019) · van Dalfsen & Markus **2018** (2017) · Kırlıoğlu **2020** (2019) ·
Tofani 2025 ✓ · Wescott 2025 ✓ · Mukherjee 2022 ✓.

## Matriz de decisão (209 itens)
**ENTRA 98** (TTFL/SCN/luz 33 · HPA 17 · clínica 9 · genética 4 · bipolar 14 · biomarcador 1 ·
cronoterapia 2 · causal experimental 5 · ponte B7 1 · sínteses 12) ·
**BAIXO 98** (SUP/CONTEXT/redundância/malha — registrados em matriz_b10_decisao.json) ·
**EXC 13** (preprint + NAO-IDX + não-fontes + duplicatas).

**Sobreposição com V1:** 0 (todo o material é aditivo; V1 GEOFFROY_2025 [luz bipolar] e o novo
Geoffroy & Maruani 2025 [cronobiologia do humor] são artigos distintos — id REF_GEOFFROYMARUANI_2025).

**Fecho.** Verificação externa independente executada ref a ref (P-7): 182 PMIDs do dossiê + 15
PMIDs resolvidos por DOI + efetch dos finalistas. Decisões em `matriz_b10_decisao.json`;
correções registradas em `decisoes_B10.md`, manifesto e trilha `04_AT_ciclo_2026-09-09.json`.
P-6 segue pendência honesta (2ª verificação cega ao fim da rodada 16/16).
