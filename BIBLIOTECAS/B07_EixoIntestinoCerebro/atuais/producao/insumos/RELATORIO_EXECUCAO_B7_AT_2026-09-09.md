# RELATÓRIO DE EXECUÇÃO — B7 V2 (Rodada [AT] GPM 2026-09-09)

**Resultado:** `B7 EIXO INTESTINO CEREBRO V2 CANONICA.md` — **116 referências** (85 vigentes + 31 [AT]),
9.356 palavras. V1 arquivada em `producao/historico/v1_canonica_2026-09-09.md`.

## Pipeline executado (P-7, ponta a ponta)
1. Parse do anexo: 196 DOIs + Carabotti 2015 (sem DOI → busca dirigida, PMID 25830558 ✓).
2. G1 eutils ref a ref: 192/196 ok; 4 NAO-IDX (Thomas/Towriss preprints, Xia, Zhang) fora; **0 falsos positivos**
   (8 alertas de forma). Briefing dizia "178 refs" vs 197 reais — incongruência exposta.
3. Tabela-mestra GPM 30/30 ("31" no texto = menor); 7 já vigentes → 23 masters novas; overlap total 8.
4. Matriz de decisão (188 itens): **31 ENTRA · 131 BAIXO · 26 EXC** — motivos individuais em
   `matriz_b7_decisao.json`; relatório em `RELATORIO_AUDITORIA_MATRIZ_B7.md`.
5. Aprovação do usuário ("ok" → aplicação completa, padrão B5/B6).
6. Fusão: 16 inserções com âncoras únicas + asserts; varredura `\d{7,9}` = 0; 31 trechos-âncora
   literais gravados para a tríade.
7. Tríade: pmids 85→116 · vínculos 40→71 (CONFIRMADO; trechos literais na V2) · ledger 47→78 ·
   manifesto v2 (rodada 4, versão 2.6) · trilha `producao/04_AT_ciclo_2026-09-09.json`.
8. Ajuste ao vocabulário controlado do framework (origem_entrada/acao_correcao) — rodada [AT]
   preservada em `verificacao.verificador` de cada registro novo.

## As 31 incorporadas (selo de evidência)
- **OB (9):** Aburto & Cryan 2024 (barreiras) · Carabotti 2015 · Agus 2018 · Bosi 2020 · Chen 2021
  (Trp-KYN/DII-depressão) · Cheng 2024 (AGCC-depressão) · Ohara 2025 (neuroepitélio) ·
  Stanimirov 2025 (bile FXR/TGR5) · Baj 2019 (glutamato).
- **ML (18) [APENAS PRÉ-CLÍNICO]:** Guo 2013/2015 · Nighot 2017/2019 (LPS→TLR4→MyD88→MLCK→TJ) ·
  Kurita 2020 (endotoxemia→neuroinflamação; isquemia só como modelo) · Erny 2021
  (acetato→microglia, formulação protegida) · Spichak 2021 (astrócitos) · Caetano-Silva 2023
  (fibra→microglia) · Barki 2022 (quimiogenética) · Chen N 2024 (ACSS2→PPARγ→TPH2, ROEDOR) ·
  Chenghan 2025 (BBB×AGCC, rhesus) · Nøhr 2013 (FFAR3/FFAR2 em EEC/SNE) · Saikachain 2023
  (GPR43, SH-SY5Y) · Schwarcz 2024 (KYNA in vitro) e Sathyasaikumar 2024 (IPrA→KYNA) — ambos sob
  guarda B7-CAUSAL-02 · Zhao 2022 (DSS→IDO-1→KYN) · Li 2023 (Trp-KYN em CRS) · Kuo 2021
  (ZO-1 dispensável — freio ao biomarcador).
- **EC associativa (4):** Tulkens 2020 (EVs LPS+; SEM ABSTRACT → G3) · Lin 2023 (KYN/disbiose
  marcadores TDM) · Zhou 2023 (adolescentes; validação camundongo) · Zhang Q 2025 (multiômica
  cognição TDM) — todas ASSOCIATIVAS (B7-CAUSAL-03).

## Portões oficiais
- ✅ gate_script.py (P-5): **APROVADO**
- ✅ validar_auditoria.py (framework): **0 ERRO · 0 AVISO**
- ✅ checklist_entrega.py: **41/41 OK · 0 FALHA**
- ✅ P-4 ADENDO V2 (15 itens revalidados) + decisoes_B7.md (bloco completo)

## Pendências
- **P-6 (2ª verificação cega, Via 2)** — PENDENTE ao fim da rodada 16/16 (declarada em ledger,
  decisões, P-4, manifesto e fecho da canônica).
- 4 NAO-IDX monitorados ([G1] se a ciência amadurecer).

**Série atualizada:** B1 ✅ (237) · B2 ✅ (213) · B3 ✅ (165) · B4 ✅ (131) · B5 ✅ (160) ·
B6 ✅ (108) · **B7 ✅ (116)** — 7/16 da rodada de insumos externos.
