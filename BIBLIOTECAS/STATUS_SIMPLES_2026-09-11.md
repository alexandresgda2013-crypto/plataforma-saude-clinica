# STATUS SIMPLES DO PROJETO — 2026-09-11 (verificado agora, direto dos arquivos)

> **Atualização 2 (mesmo dia, fim do dia):** rodada de harmonização executada —
> 2.619 reparos de METADADO em 13 bibliotecas (fichas de rastreabilidade:
> vocabulário, âncoras, assinaturas G3). **Ciência: zero linhas tocadas nas 16
> Canônicas.** Contrato: 14/16 com 0 bloqueantes; B2=48 e B12=1 apenas na fila
> de confirmação humana (com candidatas prontas). Gates 16/16 verdes. Versão
> completa em `ROTEIRO_PROJETO.md`.

> **Atualização (mesmo dia):** a Canônica B1 foi **renomeada para
> `B1 NEUROINFLAMAÇÃO V4.1 CANONICA.md`** — agora a mudança aparece no número da
> versão, não só na nota interna. A v4 original está intacta em
> `B01_Neuroinflamacao/antigos/historico/`. Portões re-rodados no novo nome:
> gate aprovado, checklist 41/41, framework 0 erro.

## 1) O que foi alterado DE FATO nas Canônicas (a ciência)

Medido por diff contra o backup de 11/set/2026 (pré-rodada 5):

- **B1 (Neuroinflamação):** 17 linhas diferentes no total. Dessas:
  - **1 linha de ciência de verdade:** no §6.2, a etiqueta de fonte
    `— IL-6 predictor, 2015)` virou `; Virtanen et al., 2015)`.
    A frase, o mecanismo e o achado científico são **idênticos** — só a
    etiqueta da referência estava fora do padrão do resto do documento.
  - **16 linhas = a nota de auditoria anexada no fim do arquivo**, que
    registra essa própria mudança (regra AT-10: nada muda sem nota datada).
- **B2–B16: ZERO alterações** nos documentos canônicos desde a entrega.
  O que aconteceu com elas foi só leitura de diagnóstico (censo) e, em
  B7/B8, uma declaração no manifesto (arquivo administrativo, não a ciência).

**Resumo: nenhum mecanismo foi criado, removido ou reescrito. Nenhuma
afirmação científica mudou de conteúdo.**

## 2) Os checklists foram rodados depois das mudanças? Precisa?

Precisa sim — toda vez que algo muda. Re-rodados AGORA (11/set):

| Portão                        | Resultado hoje                    |
|-------------------------------|-----------------------------------|
| Gate de estrutura/conteúdo    | **16/16 bibliotecas APROVADAS**   |
| Checklist de entrega B1       | **41/41 OK, 0 falhas**            |
| Fidelidade (framework, B1)    | **0 ERRO** (237 avisos não-bloqueantes) |

## 3) "Foram feitas análises de todos os mecanismos?"

O trabalho das rodadas 4 e 5 **não foi refazer ciência** — foi conferir
rastreabilidade, ou seja: cada ficha de referência científica aponta para
a frase EXATA da Canônica que aquela referência sustenta?

- B1 tem **257 vínculos** (referência ↔ frase). Hoje: **257/257 (100%)
  batem palavra por palavra** com o texto canônico.
- B1 tem **237 decisões** registradas no ledger de auditoria (a ficha de
  "por que esta afirmação entrou"). Framework: **0 erro bloqueante** —
  não existe afirmação na Canônica sem lastro registrado.

## 4) O que são os AT-xx (sem jargão)

Pense assim: a Canônica é o **conteúdo científico** (o "código-fonte").
Os vínculos são **metadados de rastreabilidade** (etiquetas: que frase,
que tipo de evidência, força causal, quem verificou).

Os AT-xx são **dívidas de metadado**, não erros de ciência:

| Item     | Biblioteca | O que é, em uma frase                                             | Estado   |
|----------|------------|--------------------------------------------------------------------|----------|
| AT-02/13 | B1         | Âncoras que não batiam literalmente com o texto                   | **FECHADO** (100%) |
| AT-01    | B1         | 27 fichas com etiqueta de um campo no lugar de outro (tier × natureza) | Fila     |
| AT-13b   | B1         | 12 fichas onde 2 referências dividem a mesma frase — decidir co-citação | Máquina propõe, humano confirma |
| AT-03    | B7         | Ficha de auditoria assinada com convenção antiga ("IA+eutils")    | Fila     |
| AT-04    | B8         | Idem B7                                                            | Fila     |
| AT-05    | B2         | 61 fichas em estado "rascunho" + 62 âncoras vazias — **a única dívida que toca evidência diretamente** | Próxima da fila |
| AT-12    | B7/B8      | 106 etiquetas fora do vocabulário oficial — harmonizar com o schema | Fila     |

## 5) Uma linha por biblioteca

- **Todas as 16:** gate de estrutura/conteúdo APROVADO hoje.
- **B1:** a mais auditada de todas (5 rodadas de perícia em cima).
  Rastreabilidade 100% literal. Prosa alterada: 1 etiqueta de citação.
- **B2:** ciência verde no gate, mas é a que tem a maior dívida de
  metadado (AT-05) — por isso lidera a fila.
- **B7 e B8:** ciência verde; as fichas de auditoria usam convenção
  antiga (AT-03/04/12).
- **B3–B6, B9–B16:** ciência verde; dívidas de metadado já catalogadas
  com contagens exatas no censo do contrato, aguardando a fila P-6.

## 6) Rastreabilidade (sua regra: "não sei o que mudou")

Toda mudança das rodadas 4 e 5 tem TRÊSS registros:
1. Entrada datada em `BIBLIOTECAS/CHANGELOG_GERAL.md` (antes e depois);
2. Nota datada dentro do próprio arquivo alterado;
3. Trilha de máquina em `producao/05_reparo_*.json` + backup datado.

Nada foi editado em silêncio.

---

## 7) Atualização 2026-09-12 — EXECUÇÃO R1–R13 (auditoria integral do agente externo sobre a B1) CONCLUÍDA

- **B1 V5 vigente** (status canônico **PROVISÓRIO** declarado — revisão cega humana dos 59 vínculos pendente, exigência do auditor). A v4.1 auditada está preservada bit a bit em `antigos/historico/` (sha 43b7673bd2f9d65f); `atuais/` tem só a V5.
- **Corrigidos 2 GRAVE** (Almulla: direção dos TRYCATs invertida na prosa → reformulada; Comai: seletividade "bipolar, não unipolar" restituída) **+ todos os 11 MODERADOS decidíveis** (Gavril, Wijesinghe, Enache, Hafizi-2007, citação vazia → Lang 2025, tabela sem corte de PCR, manifesto sincronizado, Lista v1.2, g3_notas, órfãs).
- **Tríade B1 final:** Módulo 09 = **236** (base 200 · MA 33 · EC 3) · ledger **236** · vínculos **273** (+16 da reconciliação de órfãs; ANNETT_2020 removida por isolamento — auditável na trilha).
- **Manutenção bônus da sessão:** 124 âncoras de vínculo re-escritas na forma literal da V5 (deriva de espaçamento pré-existente; 35 casos com deriva lexical ficaram como dívida nomeada para olho humano).
- **Portões:** gate APROVADO · checklist 41/41 · framework 0 ERRO · censo **32/32 BLOQ 0**.
- **Pendente do lado de cá:** envio do lote de re-auditoria ao Auditor-Mestre (está tudo em `producao/10…14_*` + `decisoes_B1.md` rev.3 + CHANGELOG). Dívidas nomeadas: 6 (com contagens exatas) — nada fabricado.
