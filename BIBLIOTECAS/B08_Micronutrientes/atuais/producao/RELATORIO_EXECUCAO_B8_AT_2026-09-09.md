# RELATÓRIO DE EXECUÇÃO — B8 Micronutrientes · Rodada [AT] 2026-09-09 (P-7) → CANÔNICA V2

## Resultado
**V1 (96 refs, 7.414 palavras) → V2 (145 refs, 10.007 palavras).** Fusão completa aprovada pelo usuário ("completo (49)", padrão B5/B6/B7). V1 rotacionada para `producao/historico/v1_canonica_2026-09-09.md`.

## Insumos auditados (ref a ref, antes de qualquer fusão)
| Insumo | Conteúdo | Veredito |
|---|---|---|
| GPM_B8_Micronutrientes (2).md | oficial, molde v2.0, M00–M10, 44 âncoras, 12 regras, inventário negativo, estrutura B8.01–21 | adotado como molde |
| BRIEFING RODADA0 | tabela-mestra 44 PMIDs (§3), correções (§4), NAO-IDX (§5), "não citadas" (§6) | **7 erros factuais revertidos e expostos** |
| BRIEFING CONSOLIDADO v1 | consolidação | coerente |
| Anexo de artigos | **106 entradas reais** (briefing dizia "98"); 105 DOI + Bourre sem DOI | auditado 100% |
| Matriz ChatGPT | 50 claims B8.SM02 + 10 regras B8-Causal + bloco NEG (vit C/vit D) + cadeia-mãe + quatro-pontos | regras 01–10 fixadas verbatim |

## G1 (eutils — esearch/esummary/efetch)
96/105 DOIs ok · **0 falso positivo** · 9 NAO-IDX confirmados (Barakat; Chambers; Fedulova; Jayashree; Júnior; Kim; Lubis; Medford; Wróblewska) · **Bourre 2006 resgatado por busca dirigida** (17066209, J Nutr Health Aging — o briefing o dava como não indexado) · 34 alertas = forma/ano **epub-vs-print** normalizados pelo print.

## Matriz de decisão — 49 ENTRA / 30 BAIXO / 12 EXC
| Bloco da V2 | Referências [AT] incorporadas |
|---|---|
| §1.1 (§1.2/1.3/1.6 fundamentos) | Bourre 2006 · Sahu 2022 · Mathew 2024 · Badar 2022 (relato de caso) · Moore 2019 (TUDA) · Ferriani 2022 (ELSA-Brasil) · Kennedy 2016 · Nogueira-de-Almeida 2023 · Muscaritoli 2021 · Du 2016 (TEPT excluído do escopo) · Lahoda Brodska 2023 (fronteira neuro) · Eyles 2013 · Cui 2021 (fronteira psicose) · Yang 2026 (hipótese complemento/VDBP-megalin) |
| §2.1–2.4 (vias) | Rajen 2025 · Faugere 2025 · Al Jassem 2024 · Kohl 2025 · **Horsdal 2025 (NULO p/ TDM)** · Skoczek-Rubińska 2025 · **Moroianu 2026 (NEG)** · Shayganfard 2022 · Astorino 2025 · Faa 2025 · Barks 2019 · Barks 2021 · McWilliams 2022 · Fiani 2023 · Mattei 2019 (resgatada) |
| BLOCO_05 | Domański 2025 · Radoeva 2025 (ingestão ≠ status) |
| BLOCO_06 | Firth 2018 (FEP status) · Firth 2017 (supl em esquizofrenia) · Tortajada 2026 (ponte B9) · Rajasekar 2024 |
| §7.5 (MR) | Hui 2024 · Lu 2025 · Ye 2025 — cláusula MR ≠ eficácia (B8-CAUSAL-03) |
| BLOCO_08 (pontes) | Rudzki 2021 · Barone 2022 (B7) · Wesselink 2019 (B9) · Shahini 2026 (B1) · Scuto 2024 (B6/B3) |
| BLOCO_11 / 12 | Alexa 2026 · Islam 2025 · Anmella 2025 (N=729) · Berger 2024 · Rucklidge 2025 · **Plevin 2020 (NEG vitamina C)** |

EXC (12) por malha de escopo: autismo ×5 · neurodegeneração ×2 · anorexia · epilepsia · delirium · botânica · demência/AVC (Navale).

## Regras fixadas
**B8-CAUSAL-01..10** (CONTROVÉRSIAS da V2) + blocos NEG (vitamina C — Plevin 2020; vitamina D — Moroianu 2026) + formulações protegidas (Badar relato de caso; fronteiras ilustrativas psicose/TDAH/TEA/TEPT/neurológico; Horsdal nulo p/ TDM; MR ≠ RCT).

## Tríade (mesmo conjunto de IDs em tudo)
01_pmids.json **96→145** (claim_id `B8.MEC.BLOCOxx.nnn`) · Vínculos **34→83** (trechos-âncora únicos, assert 1× na V2) · ledger **38→87** (vocabulário controlado: `origem_entrada=GPM`, `acao_correcao=MANTER`; verificador "IA G3 Rodada [AT] GPM B8 2026-09-09 — P-6 pendente") · manifesto (rodada 4, versão 2.6, P-6 AMPLIADA) · trilha `producao/04_AT_ciclo_2026-09-09.json`.

## Portões oficiais (pós-fusão)
| Portão | Resultado |
|---|---|
| gate_script.py (P-5) | ✅ APROVADO (conteúdo) — 145 refs, 83 vínculos |
| validar_auditoria.py (framework) | ✅ **0 ERRO / 0 AVISO** — 87 trechos, 145 refs únicas |
| checklist_entrega.py B8 | ✅ **41/41 OK — 0 FALHA** |
| decisoes_B8.md | ✅ append "Rodada [AT] 2026-09-09 — reconciliação (P-7) → V2" |
| P-4 (fidelidade) | ✅ ADENDO V2 — 15 itens revalidados |

## Pendências honestas
- **P-6 (2ª verificação cega, Via 2): PENDENTE** — ao fim da rodada 16/16, cobrindo todas as levas [AT] de B1–B16; inclui os 49 novos claims da B8 (alto risco: MRs Hui/Lu/Ye; Moroianu; Horsdal; masters GPM). Não autocertificável — registrado em ledger, decisões, P-4, manifesto e fecho da canônica.
- Legado editorial V1 (não-bloqueante): 5 refs do Módulo 09 sem espelho em listra-resumo (Bottiglieri 2000/2005; Coppen 2000/2005; Taylor 2004) — saneamento futuro.

## Próximo
Aguardar insumo **B9 (Disfunção Mitocondrial)**; ao fim da rodada (16/16), fechar P-6 Via 2.
