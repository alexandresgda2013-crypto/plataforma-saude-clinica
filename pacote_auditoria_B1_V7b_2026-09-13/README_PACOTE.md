# PACOTE DE AUDITORIA — B1 Neuroinflamação · CANÔNICA V7 · 2026-09-13 (pós-rodada 3 do ciclo bilateral)

**Destinatários:** Auditor-Mestre (pacote mínimo pedido no §0 do parecer rodada 3) e segundo auditor
externo. **Conteúdo:** camada de evidência completa da B1 V7 + os programas de portão + saídas frescas +
as trilhas da rodada que gerou a V7. Tudo medido hoje, direto dos arquivos.

## Estado medido (V7, sha 6e2c2979…)

| Item | Valor medido |
|---|---|
| Canônica | `canonica/B1 NEUROINFLAMAÇÃO V7 CANONICA.md` — sha256 **6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238** |
| Referências Módulo 09 | **237** (01_pmids: 201 · 02_meta_analises: **33** · 03_ensaios: 3 · 04/05: 0) |
| Meta-análises | **33** (AUD-067: REF_MEHTA_2020b é Revisão Sistemática — eutils — e deixou o balde 02) |
| Vínculos N2 | **274** |
| Ledger N3 | **237** |
| Portões (saídas em `saidas/`) | gate **APROVADO** · checklist **41/41** · framework **0 ERRO/236 AVISO** · P-8 **0 ERRO/26 AVISO** (V-02=0; V-05 96,9%; V-13 confere o sha; V-14 14/14) · censo série 32/32 |
| Novidades da V7 | C4 decidida no algoritmo (Critério C = modificador; regra de rebaixamento) · AUD-066 (PROVISÓRIO ← fila 108/91) · AUD-067 (Mehta) · L717→2020b · §3-taxonomia replicada (trilha 21) |

## Layout para re-rodar

```
mkdir atuais && cd atuais
cp ../pacote/canonica/*.md . ; cp -r ../pacote/Evidencias . ; cp -r ../pacote/Auditoria_B1 .
python3 ../pacote/ferramentas/gate_script.py .
python3 ../pacote/ferramentas/validar_auditoria.py . --biblioteca "B1 NEUROINFLAMAÇÃO V7 CANONICA.md" \
  --ledger Auditoria_B1/ledger_auditoria_B1.json
```

## Avisos conhecidos (nada escondido)

- Framework 236 avisos: 235 = `citacao_literal` por TOKEN (dívida L-13, prioridade máxima no Bloco 1 do
  parecer) + 1 informativo.
- P-8: 26 avisos — 18 × V-06 (qualificador não propagado; dívida D-B1-R3-G3NOTA), 6 × V-08 (números em
  prosa editorial dos REGISTROs/rótulo), V-09 (30 vínculos sem claim_id — nomeado), V-10 (tokens do
  ledger — L-13).
- **Taxonomia [XX] (achado §3 do Auditor-Mestre, confirmado por réplica na trilha 21):** classificadores
  divergem entre prosa, apêndice, balde e `desenho_estudo`; correção material vai ao pacote L-05/1.2 com
  V-15 — as listas completas (84 divergentes; 7 autodivergentes — 1 já zerada, Mehta) estão em
  `producao/21_….json`.
- Fila P-6 (revisão humana, instância do fim): `FILA_REVISAO_CEGA_ALTO_RISCO_B1_2026-09-12.json` = 108
  vínculos/91 refs (na casa; declarado), + formalização do vínculo N2 da L717 + revisão da regra C4.
- A V6 final (sha e11dbd95) e todas as anteriores estão preservadas bit a bit na casa
  (`antigos/historico/`), com linhagem no `_manifesto_biblioteca.json` (`historico_sha_v6`).

— Gerado pela IA da casa em 2026-09-13 · hashes de cada arquivo em `SHA256SUMS.txt`.


---

## ADDENDUM V7b (2026-09-13, rodada 4 — revisão do CÓDIGO do portão pelo auditor de estrutura)

- **`ferramentas/gate_script.py` passa a ser a rev.A2** (os 4 critérios do Bloco H implementados com
  contadores por critério · E1/E2 como FALHA · E3 INFO · selo por frase [11]/[11b] · INFO permanente do
  campo `uso` fora do enum v3.1 · `citacao_confirmada` banido como via: dependência=FALHA, campo
  preenchido=INFO). Backup da versão oficial na casa (`gate_script.py.bak_gateOficial_pre_revA2_2026-09-13`).
- `saidas/gate_P5_revA2_2026-09-13.txt` — saída completa com os INFOs nomeados (237 fichas com
  `citacao_confirmada` preenchido; 51/38 alto-risco; VINC_B1_0047; 7 do índice; 2 âncoras E3).
- `producao/23_replicacao_auditor_estrutura_2026-09-13.json` — réplica achado-a-achado (6/6
  confirmados) + desenho da implementação + portões pós-patch.
- Checklist re-rodado: **41/41**; framework e P-8 inalterados por construção (0 ERRO / 236 / 26) e
  re-medidos na trilha 23.
