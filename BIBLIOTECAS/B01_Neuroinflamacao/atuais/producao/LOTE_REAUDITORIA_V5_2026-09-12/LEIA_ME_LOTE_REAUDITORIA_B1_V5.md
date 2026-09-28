# LOTE DE RE-AUDITORIA — B1 V5 (resposta ao §6 da réplica do Auditor-Mestre, 2026-09-11)
**Montado em:** 2026-09-12 · **Casa:** execução IA com trilha completa · **Estado dos portões no fechamento:** gate APROVADO · checklist 41/41 · framework 0 ERRO (236 avisos [TAG] não-bloqueantes, padrão) · censo da série 32/32 BLOQ 0.

Reconhecimento das 3 **erratas do próprio auditor** incorporadas: AUD-040 retirado integral (Sublette 2011 — nada a corrigir; o texto é espelho do título PubMed 21605657); AUD-038 reduzido ao ano (Hafizi **2007**; PubMed 17639827 sem abstract — efetch replicado pela casa); AUD-034 13→12 (37070103 era typo por 37070163, já presente em N1).

## Mapa item a item do §6 da réplica
| # | Exigência da réplica | Arquivo(s) neste lote |
|---|---|---|
| 1 | Canônica **V5** + v4.1 preservada (hash) | `canonica_B1_V5.md` (sha `3c6dda4d2f319dd6…`) · `canonica_B1_v4.1_preservada_pos_auditoria.md` (sha `43b7673bd2f9d65f…`, bit a bit) |
| 2 | Manifesto sincronizado (status provisório) | `manifesto_biblioteca.json` — pmids_total **236**, meta_análises **33**, ensaios_clínicos **3**, `status_canonico: PROVISÓRIO` + motivo (R9–R10) |
| 3 | Vínculos: 19 g3_nota + 30 V2 claim_id **ou dívida nomeada** | `vinculos_referencia_afirmacao.json` (273) + `trilha_12_R3_parciais_v2.json` — 15/19 já tinham nota com motivo; 4 reconstruídas do ledger + `reavaliacao_g3_pendente`; 30 claim_id: 0/30 elegíveis à herança → **dívida D-B1-R3-V2CLAIM** (opção aceita na réplica) |
| 4 | Lista Canônica **v1.2** | `LISTA_CANONICA_B1_v1.2.md` — 78/83 `usado_em_biblioteca`; 2 claim_ids sem item = dívida D-B1-R4-2CLAIMS |
| 5 | `decisoes_B1.md` com R5, R12, R8 | `decisoes_B1.md` rev.3 — R5 item a item dos 12 PMIDs (10 incorporar no próximo [AT] / 2 não-incorporar motivado; rastro factual: 11/12 nunca entraram no funil da casa), R12 **ratificada** (matriz presente), R8 (ANNETT removida + 16 vínculos VINC_B1_0258–0273) |
| 6 | `matriz_b1_at_final.json` | incluída — 49 entrantes (todos no Módulo 09) + 19 rejeitados com motivo; + `RELATORIO_AUDITORIA_MATRIZ_B1.md` (auditoria ref-a-ref do insumo) |
| 7 | Log de busca **completo** | `DECLARACAO_LOG_BUSCA_D-B1-R13-LOG.md` + `log_de_busca_top10/` — dívida honesta **D-B1-R13-LOG** (o pipeline só preservou o top-10, 622 linhas; log completo será artefato obrigatório no próximo [AT]) |
| 8 | Trilha [AT] + artefatos | `trilha_10…14_*.json`, `censo_pos_R1_R13_2026-09-12.txt`, `MANIFESTO_LOTE.json` (hashes) — CHANGELOG_GERAL.md 2026-09-11/12 no repositório (entradas ABERTURA + RESULTADO) |
| 9 | Lista dos **59** + instrumento da revisão cega | `FILA_REVISAO_CEGA_ALTO_RISCO_B1_2026-09-12.json` — **108 vínculos / 91 refs** (critério operacional declarado; ver nota abaixo) · `INSTRUMENTO_REVISAO_CEGA_P6_PROPOSTA_2026-09-12.md` (**proposta**, não instrumento oficial preexistente — a ratificar) |

## Nota de reconciliação do "59" (transparência exigida pelo método da casa)
O "59 vínculos de alto-risco" do relatório de fidelidade (V3, 2026-09-04) era **contagem qualitativa por classes**
(metas, RCT, TSPO-PET, pós-morte, genética humana) **sem lista preservada**; não foi bit-reproduzível em bancada
(tentativas registradas: 65 na V3 por união de rótulos, 91 refs/108 vínculos na V5 pelo critério atual). A casa
entrega a **fila operacional v2026-09-12** — superconjunto conservador das mesmas classes, incluindo a leva [AT]
2026-09-08 — com cobertura **completa** dos 22 claims já revistos em full-text (rodada G3 PMC 2026-09-04). Se o
Auditor-Mestre tiver a lista nominal dos 59 do seu lado, a casa reconcilia id-a-id em uma manutenção.

## Registro do veredito sobre a execução (o que a casa considera encerrado vs. aberto)
- **Encerradas com prova:** R1, R2 (GRAVE — eutils replicado pelos dois lados), R7, R11, R3(a), R4, R6, R8, R12; AUD-038/040 por errata do auditor.
- **Entregues em forma de dívida nomeada (aceita na réplica):** R3(b) claim_ids V2 · R13 log completo · orfandade de claim_id dos 16 novos vínculos (D-B1-R8-CLAIM) · 2 claims sem item na Lista (D-B1-R4-2CLAIMS) · 4 notas G3 reconstruídas (D-B1-R3-G3NOTA).
- **Descoberta da casa não pedida na ata:** 159 âncoras de vínculo não literais por espaçamento/pontuação — **124 reparadas mecanicamente** (sítio único, sim ≥0,985; trilha 13 com a rev do método); **35 com deriva lexical viraram dívida D-B1-ANCORA-DERIVA** (a casa não reescreve âncora com troca de palavras).
- **Status canônico:** **PROVISÓRIO** — declarado no cabeçalho da V5, do manifesto e aqui; a retirada depende da revisão cega da fila (R9–R10).

**Como verificar este lote:** cada arquivo tem sha256 em `MANIFESTO_LOTE.json`; as fontes vivas estão nos caminhos
`origem` (o lote é cópia congelada de 2026-09-12). Divergência de hash entre lote e origem = alteração posterior a
esta data, rastreável no CHANGELOG.
