# RELATÓRIO DE AUDITORIA — Insumos externos B8 (Deficiências de Micronutrientes)
**Data:** 2026-09-09 · **Alvo:** B8 V1 (96 refs vigentes) → proposta V2
**Insumos (5):** `GPM_B8_Micronutrientes (2).md` (oficial, molde v2.0, M00–M10) + `BRIEFING_B8_MICRONUTRIENTES_RODADA0.md` + `BRIEFING_CONSOLIDADO_B8_v1.md` + anexo APA (`Artigos ... B8 deficiencia micronutrientes.md`) + `Resumo do insumo para B8 Chatgpt.md` (matriz 50 claims B8.SM02.001–050 + 10 regras B8-Causal + estrutura B8.01–21)
**Regra:** auditoria ref a ref ANTES de qualquer fusão; nada entra sem resolver no PubMed.

## 1. Números reais vs. briefing (incongruências expostas)
| Item | Briefing/GPM dizia | Auditado | Veredito |
|---|---|---|---|
| Refs do insumo | "98 refs; 88 DOI→PMID auditados" | **106 entradas únicas parseadas** (matriz ChatGPT diz 106 ✓) | subcontagem do briefing |
| Tabela-mestra | 44 âncoras → 44 PMIDs | **44/44 confirmadas no anexo**, rótulo autor/ano/tema correto (anos-canónicos = print, conforme §4.4) | ✅ |
| NAO-IDX (§5) | 9 DOI sem hit + Bourre sem DOI | **10/10 confirmados NAO-IDX** (Barakat, Chambers, Fedulova, Jayashree, Júnior, Kim, Lubis, Medford, Wróblewska + Bourre-sem-DOI) — **MAS Bourre foi resgatado por busca dirigida** | ✅ com 1 ressalva |
| §4.1 "Mattei 2019 = McWilliams 2022" | reatribuição | **FALSO** — Mattei D 2019 real existe no anexo (PMID 30953290, Curr Nutr Rep, *Micronutrients and Brain Development*); as duas refs são distintas (McWilliams é master #17 ✓) | ❌ exposição |
| §4.2 "Yoon 2026 = Zielińska 2023" | reatribuição | **FALSO** — Yoon Y 2026 real existe (PMID 42514375, *Dynamic Coenzyme Network of B Vitamins…*); Zielińska já era vigente na V1; a claim .015 fica coberta pelo master Kennedy 2016 | ❌ exposição |
| §4.3 "Dehesh 2026 = Domański 2025" | reatribuição | **FALSO** — Dehesh T 2026 real existe (PMID 42605394, Iran J Psychiatry) | ❌ exposição |
| §8 "Cortés-Albornoz 2021 não localizada" | pendência [G1] | **Existe** (PMID 34684531) | ❌ exposição |
| §8 "Das 2025 não localizada" | pendência [G1] | **Existe** (PMID 41064635) | ❌ exposição |
| §5 "Bourre 2006 revista francesa não localizada" | NAO-IDX | **Existe**: Bourre JM 2006, J Nutr Health Aging, *Effects of nutrients… Part 1: micronutrients* (PMID 17066209) — âncora exata das claims .001–.002 | ❌ exposição (resgate) |
| §4.7 "Wang 2018 sem PMID → [G1]" | pendência | **Resolvido**: 29747386 — e **já era vigente na V1** (REF_WANG_2018) | ✅ resolvido por evidência |

> **Síntese:** as 44 âncoras do GPM estão 100% corretas; mas o aparato de "correções/pendências" do briefing §4–§8 continha **7 erros factuais** que a auditoria ref a ref desta rodada reverteu com evidência PubMed. Nenhuma ref foi forjada ou inventada em nenhuma direção.

## 2. Sobreposição com a V1 (96 refs)
**6 refs** já vigentes: Wang 2018 (29747386), Zielińska 2023, Carnegie 2024, Han 2025, Fang 2025, Hachmeriyan 2026.
→ Masters novas na fila = **41** (44 − 3 vigentes: Zielińska/Carnegie/Fang). **Fila de decisão = 91** (96 resolvidos + Bourre − 6 overlap).

## 3. Matriz ChatGPT B8 (50 claims + 10 regras) — papel na fusão
- As **10 regras B8-Causal** entrarão fixadas na canônica (CONTROVÉRSIAS/regras): 01 deficiência ≠ causa automática; 02 associação ≠ precedência; 03 **MR ≠ eficácia de suplementação**; 04 suplementar é pergunta causal distinta; 05 **ingestão ≠ deficiência bioquímica**; 06 **sérico ≠ deficiência funcional**; 07 animal/célula ≠ linguagem clínica; 08 **heterogeneidade obrigatória por micronutriente×desfecho**; 09 revisão ≠ ensaio causal; 10 B8→B6/B9/B3 = conexão, não duplicação.
- **Bloco NEG canônico:** vitamina C — associação deficiência↔humor SEM prova intervencional de reposição (Plevin 2020); vitamina D — associação robusta SEM eficácia antidepressiva (Moroianu 2026).
- Correções epistemológicas da triagem preservadas: Carnegie 2024 e Lu & Paterson 2025 são **MR** (não meta-análise); Badar 2022 = relato de caso (possibilidade, não população).

## 4. Decisão ref a ref (91)
### 4.1 ENTRA — 49 (41 masters GPM + 8 adicionais)
Masters (41): listadas em `matriz_b8_decisao.json` com papel por via (M01).
Adicionais (8):
1. **Bourre 2006** (RESGATE) — âncora bioquímica ESTABLISHED das claims .001–.002.
2. **Mattei 2019** (RESGATE) — micronutrientes×desenvolvimento cerebral (claims .001–.003; fecha pendência do GPM).
3. **Moore 2019** — coorte TUDA: vitaminas B com status bioquímico × depressão em idosos (humano ASSOCIATIVO; janela ausente na V1).
4. **Ferriani 2022** — ELSA-Brasil N≈14,7 mil: ingestão Se/Zn/B6/B12 inversamente associada a depressão (humano ASSOCIATIVO; ingestão≠status, regra 05).
5. **Kohl 2025** — vit D def/insuf × transtornos mentais comuns em mulheres trabalhadoras (humano ASSOCIATIVO, fora de população psiquiátrica).
6. **Islam 2025** — SR micronutrientes × **depressão perinatal** (ASSOCIATIVO; janela de desfecho direto).
7. **Yang 2026** — vit D×depressão: **complemento-remodelamento sináptico + VDBP-megalin** (janela molecular nova; OB).
8. **Horsdal 2025** — Lancet Psychiatry, caso-coorte nacional dinamarquesa: **vit D neonatal × 6 transtornos incluindo TDM** (humano ASSOCIATIVO de alto peso; desenvolvimento).

### 4.2 BAIXO — 30 (justificados individualmente)
Resgates com conteúdo tangencial: Yoon 2026 (redundante c/ Kennedy), Dehesh 2026 (ingestão estudantes — regra 05), Cortés-Albornoz 2021 (maternal, redundante c/ Mattei), Das 2025 (review genérica).
Demais famílias: desenvolvimento/pediatria tangencial (Fuglestad, Heland, Freedman, Mohammadzadeh-protocolo, Upadhyaya, Saidi, Singh, Panzeri, Pancheva), redundância vit D (Rihal, Wassif, Ye X, Ducki, Ciobanu), cognição-energia (Tardy, Mustafa Khalid), metodológico (Walsh), dieta-vegana (Clemente-Suárez), MR redundantes (Li C, Wu J), minerais×depressão redundante (Majewska), B12-gut-brain redundante (Xu C), sono-B10 (Khosropanah), autoimune (Triggianese), piloto pequeno (Khan), genérica (López-Sebastiani).

### 4.3 EXC — 12 (malha exposta)
Autismo (5): Altamimi 2018, Guo 2020, Indika 2023, Avram 2025, Daniel 2025.
Neurodegenerativos/Alzheimer (2): Kumar 2022, Miteva 2026.
Demência/AVC (1): **Navale 2022** (resgatada do apagamento do briefing §4.3, mas o conteúdo real é vit D×demência/AVC UK Biobank — fica fora com honestidade; a citação .019–.021 dela na matriz era imprópria).
Anorexia nervosa (1): Hanachi 2019.
Epilepsia (1): Chen H 2024.
Delirium (1): Ceolin 2023.
Botânica (1): Gupta 2024 (oxstress em plantas).

## 5. Pendências e selos
- NAO-IDX confirmados (9 com DOI + 0 após resgate): Barakat, Chambers, Fedulova, Jayashree, Júnior, Kim, Lubis, Medford, Wróblewska → monitorar próxima rodada; claims dependentes ficam [G1].
- Lacunas mantidas como [G1] honestas: vitaminas B1/B2/B3/B5 sem âncora própria; iodo↔B11 e HPA↔B2 âncoras cruzadas pendentes; MR por micronutriente individual.
- Toda evidência animal (Barks 2021, Walsh) = [APENAS PRÉ-CLÍNICO]; MRs rotulados MR (não intervenção); humanos observacionais = ASSOCIATIVO.
- **P-6 Via 2** (2ª verificação cega B1–B16): PENDENTE ao fim da rodada — será redeclarada.

## 6. Artefatos
`b8_anexo_entries.json` (106) · `matriz_b8_g1.json` (96 ok + 10 NAO-IDX + resgates) · `b8_cruzamento.json` (overlap 6; fila 91) · `matriz_b8_decisao.json` (49/30/12, motivos individuais).
