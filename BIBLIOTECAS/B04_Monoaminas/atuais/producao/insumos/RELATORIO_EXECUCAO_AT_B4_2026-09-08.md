# RELATÓRIO DE EXECUÇÃO [AT] — B4 → V2 (2026-09-08)

**Decisão do usuário:** aplicar agora ("agora_completo", 95 aprovadas na auditoria).
**Executado:** 94 incorporadas (1 EXC tardia pós-abstract: Evans 2024 = 5XFAD Alzheimer, fora de escopo
permanente — corte no abstract, apesar do título citar depressão). Corpus final: **37 → 131 refs**.

## Alocação efetiva (após re-rotulação por autoria real PubMed)
| Grupo | n | Destino | Leitura |
|---|---|---|---|
| HIST | 10 | §1.4 | desmontagem/montagem histórica; reserpina mitigada (Baumeister OB; Strawbridge MA) |
| 5-HT | 21 | §2.1 | receptor≠SERT≠síntese≠liberação≠circuito (Wang MA; Parsey/Hirvonen/Steinberg PET) |
| DEPL | 13 | §2.3 | gating contextual; NEGs em sadios/não-medicados com peso igual (Berman/Salomon/McLean/Schopman) |
| DA | 14 | §3.1 | anedonia ≠ "pouca dopamina" (Peciña ↑; Moriya ↓ DAT; Salamone esforço) |
| LC–NA | 26 | novo §4.1 | tônico/fásico, receptor, circuito (Berridge; McCall; Giustino; Tillage) — ML marcado R04 |
| B1↔B4 | 4 | novo §8.x | inflamação↓DA funcional (Felger; Lucido; Hersey; Bekhbat EC) |
| B2↔B4 | 1 | novo §8.x | Maes 1995: 5-HT↔feedback HPA (EC) |
| MOD | 5 | BLOCO_06-PROF | modelos pós-monoamínicos (Liu; Boku; Page; Carmellini; Dale) |

## Portões (rodados após aplicação)
- gate_script.py (P-5): **APROVADO (131|131)**.
- validar_auditoria.py (framework): **0 ERRO** — 37 avisos não-bloqueantes (padrão listra descritiva).
- checklist_entrega.py: **41/41 OK | 0 FALHA**.
- Varredura `\b\d{7,9}\b` no corpus: 0 (sem PMID no texto corrido).

## Registros/formalizações
- Regras de leitura **B4.R01–R08** fixadas no bloco "Regras de leitura B4" (CONTROVÉRSIAS).
- decisoes_B4.md: bloco [AT] com contagens, correções e 4 incidentes de engenharia corrigidos.
- fidelidade_canonica_P4_B4.md: ADENDO V2 — 15/15 itens revalidados.
- Trilha: `producao/04_AT_ciclo_2026-09-08.json`; V1 arquivada em `producao/historico/v1_canonica_2026-09-08.md`.
- **P-6 PENDENTE** (2ª verificação cega — pacote alto-risco incluirá a leva [AT] da B4).
