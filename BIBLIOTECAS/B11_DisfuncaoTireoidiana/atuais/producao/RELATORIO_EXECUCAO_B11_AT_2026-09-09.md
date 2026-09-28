# RELATÓRIO DE EXECUÇÃO — B11 · Rodada [AT] 2026-09-09

**Resultado:** `B11 DISFUNCAO TIREOIDIANA V2 CANONICA.md` — **96 referências** (V1 40 → V2 96),
**9.700 palavras**, rodada 4, tríade 96/96/96.

## 1. Insumos e método
RODADA0 (14 âncoras + 121 não citadas + 19 NAO-IDX) · GPM oficial (M00–M10, 10 regras
fundadoras) · matriz ChatGPT B11 (SM01–SM10, APROVADO_COM_RESSALVAS). Auditoria **ref a ref
antes de qualquer fusão**: esearch/esummary/efetch (eutils); abstract lido antes de
incorporar; direção do resultado confirmada na fonte. Escopo da fusão: **completo**
(instrução permanente do operador).

## 2. Matriz de decisão
| Decisão | n | Conteúdo |
|---|---|---|
| **ENTRA** | **56** | 11 âncoras novas (Fischer, Kim2018, Zhao2018, Tang2019, Wildisen, Bauer2021, Airaksinen, Soheili, Roa Dueñas, Ma, Fan) + 45 clínicos (controvérsia SCH, AIT/eutireoidiano, ansiedade-específica, transitórios/NTI, marcadores, terapia-sinal, bidirecionalidade) |
| **BAIXO** | **41** | redundância (família 1º-episódio centro único representada por Zhao 2023; revisões narrativas Cureus), desfechos periféricos (psicóticos, suicídio, metabólicos, cognição), gestação, poluentes — todos com justificativa individual em `producao/insumos/matriz_b11_decisao.json` |
| **EXC** | **11 grupos** | esquizofrenia (2), câncer (Chen/Kornelius/Ao/Kirnap), álcool, anorexia, cardiopatia, diabetes tipo 1 + **19 revistas regionais sem indexação verificável** (declarados, não forjados) |

## 3. Exposições (transparência G1)
- **Roca 1990**: o PMID do dossiê era Romero-Gómez 2019. Roca real = Endocr Res 1990
  (hipertiroxinemia transitória; Roca RP, Blackman MR, Ackerley MB, Harman SM). Ambos entraram
  corrigidos.
- **"Zhang 2024" é correção editorial** de Soheili 2023 → metadado/_aliases, não referência.
- **Ao 2024** (rotulado "TDM jovens") = tumor ósseo primário → EXC.
- **Eckert 2020** = diabetes tipo 1 → EXC · **Kirnap 2020** = DTC iatrogênico → EXC.
- **Toma 2026**: tema corrigido (triagem hormonal rotineira, não "NTIS/desiodinase").
- **"Watanave 2018"** permanece sem resolução → [G1], não forjado.

## 4. Engenharia aplicada
- BLOCOS 14–15 [[AT 2026-09-09]]: camada clínica humana (100% [EC]/[OB]; zero [ML] novo) +
  10 regras fundadoras B11-REGRA-01..10 + exposições + [G1] mantidos.
- Anos canônicos = print (5 IDs ajustados: Forbes 2026, Wu 2021, Delitala 2016, Qiao 2022 + Roca).
- 27 citações legadas re-costuradas; 6 trechos novos re-fundidos após wrap; V1 arquivada em
  `producao/historico/` e removida da raiz (checklist seleciona cans[0] — aprendizado B10
  aplicado).
- Tríade atualizada por script único com asserts (IDs únicos; trechos literais count==1).

## 5. Portões
| Portão | Resultado |
|---|---|
| gate_script (P-5) | ✅ APROVADO (INFOs = ressalva de fase 1-operador; P-6) |
| validar_auditoria (framework) | ✅ **0 ERRO** (40 avisos — formato de listra legado, ressalva de fase) |
| checklist_entrega | ✅ **41/41** |

## 6. Pendências
- **P-6**: 2ª verificação cega (Via 2) — não autocertificável; cobrirá todo o pacote B1–B16
  incluindo levas [AT]; executar/documentar no fechamento da rodada (16/16).
- [G1] mantidos: FT3 prospectivo · rT3 cerebral (mecanismo celular) · iodo↔B8 âncora cruzada ·
  RM dedicada · ensaios LT4 em SCH×depressão · definição padronizada de SCH · B11×B2 · B11×B12
  (burnout) · confundimento por LT4 · "Watanave 2018".
