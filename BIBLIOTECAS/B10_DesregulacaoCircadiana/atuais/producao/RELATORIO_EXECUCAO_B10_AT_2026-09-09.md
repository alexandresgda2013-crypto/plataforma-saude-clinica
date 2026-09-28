# RELATÓRIO DE EXECUÇÃO — B10 rodada [AT] 2026-09-09

**Resultado:** CANÔNICA **V2** entregue — de **39 → 137 referências** (+98), todas G1 eutils
(autor+ano+tema+DOI validado) + G2 + G3. Tríade sincronizada 137/137/137. Portões: **gate P-5 ✅,
framework 0 ERRO, checklist 41/41 ✅**.

## Pipeline executado
1. Leitura integral: GPM molde v2.0 (M00–M10), dossiê RODADA0, matriz RC.SM02 (58 claims),
   anexo (193 entradas parseadas), briefing consolidado v1, V1 (39 refs).
2. **Verificação externa (P-7):** 182 PMIDs-candidatos via esummary (autor+ano+tema); 16 resoluções
   por DOI[aid]; efetch (abstract+MeSH+print) dos 106 finalistas; varreduras de direção (Murray,
   Nguyen, Burns*, Song, Cox).
3. **Matriz de decisão:** 209 itens → **ENTRA 98 / BAIXO 98 / EXC 13** (`insumos/matriz_b10_decisao.json`).
4. Fusão completa (pré-aprovada): 13 blocos [[AT 2026-09-09]] na canônica (TTFL camada 1, SCN/luz
   camada 2, HPA camada 3, clínica camada 4, genética, biomarcador-exposição, cronoterapia-sinal,
   causal experimental, pontes, bipolar, sínteses, CONTROVÉRSIAS reforçadas, TABELA +7 linhas,
   APÊNDICE +98 listras) — 39 citações legadas quebradas reunidas (reparo documentado).
5. JSONs: pmids 137 · vínculos 137 (98 novos + 39 legados reanclados — ressalva documentada) ·
   ledger 137 (AUD_B10_0040–0137) · manifesto v2 (rodada 4) · trilha `04_AT_ciclo_2026-09-09.json`.

## Principais achados de auditoria (expostos)
- **Falso positivo:** âncora #33 (Burns 2024) é **preprint medRxiv** indexado — EXC.
- **Pendências do dossiê resolvidas:** McGlashan 2018 = 30555405; Serrano-Serrano 2021 = 34640406.
- **Sobre-correções revertidas:** Palagini 2022 real (35821870); Spiga 2014 indexada (24944037).
- **11 divergências autor/ano/PMID** do dossiê resolvidas por DOI (matriz completa no relatório
  de auditoria); **15 refs do anexo fora do dossiê** cobertas.
- **Anos canônicos = print** (6 renomeações documentadas).

## Ciência incorporada (por bloco)
| Bloco | n | Núcleo |
|---|---|---|
| BLOCO01 TTFL/SCN/luz | 33 | química do laço (Sato/Kume/Ye×2/Duong/Nangle/Xu/Michael/Lande-Diner/Abe/Goriki/Otobe/Serrano/Oishi), rede SCN (Shan/Ono/Welsh/Mohawk), entrada fótica (Jones/Hamnett/Xu 2021/Von Gall/Fernandez/Golombek/McGlashan), luz×HPA (Kiessling; Robertson-Dixon ×2) |
| BLOCO02 HPA+clínica | 26 | HPA circadiano (Nicolaides/Nader/Russell/Kalsbeek/Spiga/Rao&Androulakis×2/Rao/Kinlein/van Dalfsen/Buckley/Wesarg-Menzel/Lightman/den Boon) + fase/cronotipo humano (Robillard/Nguyen/Pilz/Emens/Murray/Lyall/Song/Cox/Carpenter; Yamanaka; Chellappa; Christiansen) |
| BLOCO03 genética | 4 | Soria; von Schantz; Liberman; McCarthy 2011 (REV-ERBα×lítio) |
| BLOCO05–06 | 3 | Deprato (LAN); Wescott (realinhamento); Campbell (fototerapia sinal) |
| BLOCO07–08 causal/pontes | 6 | Russell 2021 (Per2-KO); Zuo (Bmal1→AKT/mTOR→mielina); Tofani (microbiota→HPA); Francis (tipo-celular); Kandalepas (melatonina→E-box); Bautista (eixo intestino-cérebro-circadiano) |
| BLOCO11–12 | 26 | bipolar (Melo/Takaesu/Alloy/Moon/Vidafar/Esaki/Mukherjee/Lei/Scott/Palagini/Tonon/Geoffroy&Maruani/McCarthy ISBD/Chakraborty) + sínteses (Meyer/Hyndych/Zou/Walker/Dollish/Kırıloğlu/Lamont/McClung×2/Ketchesin/Smith/Pandi-Perumal) |

## Pendências honestas
- **P-6 (2ª verificação cega, Via 2):** pendente ao fim da rodada 16/16 — **ampliada** para cobrir
  todas as levas [AT] de B1–B16.
- **[G1]:** Satyanarayanan 2020 (agomelatina); Mendoza 2024; Burns 2023 (NMH).
- **Metodológicas:** DLMO/fase fisiológica como desfecho em ensaios; GRADE formal.

## Artefatos
`producao/insumos/{b10_anexo_entries, matriz_b10_g1, b10_doi_resolution, b10_efetch_all,
b10_refs_data, b10_trechos_ancora, matriz_b10_decisao}.json` · `insumos/RELATORIO_AUDITORIA_MATRIZ_B10.md`
· `producao/historico/v1_canonica_2026-09-09.md` · scripts `/home/user/{b10_gen_refs,B10_md_apply,B10_json_apply}.py`.
