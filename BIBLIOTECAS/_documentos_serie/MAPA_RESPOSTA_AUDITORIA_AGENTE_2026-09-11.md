# MAPA DE RESPOSTA ANTECIPADA — Agente Auditor externo (2026-09-11)

**Propósito:** o operador montou um agente auditor externo para auditar as
bibliotecas; o veredito chega em seguida. Este mapa registra, **computado de
arquivo hoje**, o status de cada insumo que o agente perguntou — para a réplica
sair imediata, com caminho e número. Nada aqui altera artefato de ciência.

> **rev.1 (mesma data):** este documento já corrige um erro de rastreio do
> assistente em resposta anterior — o `find` com padrão `*canon*` não casou
> "CANÔNICA" (caractere Ô). A Lista Canônica **EXISTE** (item 1 abaixo).

---

## 1. "Lista Canônica de B1" — **EXISTE** ✅
- Arquivo: `Ferramentas de geração e auditoria/02_fase1_gpm_profundidade/
  7º LISTA CANÔNICA — B1 TRILHA MECANÍSTICA GPM_B1 ARENA.md`
- 736 linhas, formato YAML, **v1.1 auditada contra o GPM_B1** (cabeçalho
  documenta a auditoria item a item: 42→83 itens; fila_realocacao com 1ª
  entrada real — PMID 33361152 realocado BLOCO08.015/B15).
- É o **Documento 5 / 7º** do conjunto processual da trilha mecanística
  (cf. `01_norteadores/ESTRUTURA MESTRE — TRILHA MECANÍSTICA v1.1.md`:
  `lista_canonica_ativa: "Lista Canônica — B1/MEC (Documento 5)"`).
- Consumo rastreado no ledger B1: `origem_entrada` = GPM 188 / POLITICA_FONTES 49.

**Do conjunto "Documentos 1–7"** (citados pela Estrutura Mestre), existem no
workspace: **2º** (Schema-Claim v3.1), **3º/5º/6º/7º** (pasta
`02_fase1_gpm_profundidade/`), **1º IDS_OFICIAIS**. **Não localizados como
arquivo:** "Protocolo de Escopo B1 (Documento 1)", "Como Executar — B1
(Documento 3)", "Bloco de Estado (Documento 6)",
`CANDIDATOS_IDS_OFICIAIS.yaml` (Documento 7) ← **lacuna real nomeada**
(insumos da trilha, não artefatos canônicos; conteúdo-efeito está nos
GPMs/BRIEFINGs preservados).

## 2. "Artefatos de reconciliação A1–A8 da v3.1" — **não existem com esse nome** ⚠️ provável falso positivo do auditor
- Varredura hermética: **zero** ocorrências de "A1–A8" em todo o workspace.
- O que existe de próximo: o **CHECKLIST FIDELIDADE CANÔNICA (FASE 3)** tem
  seção A com **A1–A4** (não A8): A1 frase tem lastro; A2 nada rejeitado
  residual; A3 zero citação nova na Rodada 3; A4 log de reconciliação aplicado.
- Evidências da reconciliação de B1 (o "artefato" que esses itens pedem):
  `B01_Neuroinflamacao/atuais/Auditoria_B1/fidelidade_canonica_P4_B1.md`,
  `…/Auditoria_B1/decisoes_B1.md`, `…/Auditoria_B1/ledger_auditoria_B1.json`,
  `B01_Neuroinflamacao/antigos/historico/RELATORIO_FIDELIDADE_CANONICA_B1.md`,
  trilhas `atuais/producao/05_reparo_*`.
- Se o veredito cobrar "A5–A8": pedir à fonte o documento que define esses
  itens — **na literatura processual desta plataforma só há A1–A4**.

## 3. "Registros de G1–G3 em sessão separada" — existem, por camada
| Portão | Sessão separada | Registros |
|---|---|---|
| G1 (referência existe; DOI→PMID eutils) | **SIM** (script+saída por biblioteca) | `producao/insumos/matriz_bX_g1.json` B1–B13; `B5_g1.py`, `B7_g1.py`, `g1_validate.py`, `g1_esummary.json` (B7) |
| G2 (elegibilidade) | vereditos incorporados | `g2_elegibilidade` + `g2_motivo` em cada vínculo (sem arquivo solto — por design) |
| G3 (suporte frase-a-frase) | rodadas [AT]/GPM | `RELATORIO_G3_FULLTEXT_alto_risco_2026-09-04.md` (B1, `antigos/historico/`); `status_auditoria`/`g3_verificado_por`/`g1_metodo` nos vínculos; `04_AT_ciclo_*.json`; `rodada1_gpm/`; `RELATORIO_EXECUCAO_B16_AT_…` |

## 4. `bX_anchormap.json` — **nenhum existe** (confirmado)
- Arquivos `*anchormap*` no disco: **zero**. Pasta `SUPORTE/`: **zero**.
- B6–B15: mencionado nos BRIEFINGs/GPMs de Rodada 0 (`SUPORTE/bX_anchormap.json`)
  — insumo de preparação **não preservado** no workspace. B1–B5 e B16: nem mencionado.
- Papel hoje exercido oficialmente por `vinculos_referencia_afirmacao.json`
  (referência ↔ frase, PMID, veredito G3) + Bibliografia 01–05.

## Lacunas reais (prováveis achados legítimos do agente)
1. Insumos SUPORTE/anchormap de B6–B15 não preservados (declarados nos briefings).
2. Documentos 1/3/6/7 da trilha mecanística citados pela Estrutura Mestre sem arquivo.
3. G2 sem relatório próprio por biblioteca (derivável dos vínculos sob demanda).
4. F1 (B14–B16): 753 fichas sem campos de verificação — já nomeada antes
   (manifestos + SCHEMA_V2_PROPOSTA P1–P10); reprocessamento assistido recomendado.

## Falsos positivos prováveis (resposta pronta se aparecerem no veredito)
- "Falta Lista Canônica B1" → **existe**: 7º LISTA CANÔNICA… (item 1).
- "Faltam A5–A8" → não há A5–A8 definidos na plataforma; evidências de A1–A4 listadas no item 2.
- "Sem meta-análise/RCT" → 272+64 fichas distribuídas 02/03 nas 16 + consolidado
  `MOTOR_CLINICO/` (268+58 dedup) — CHANGELOG 2026-09-11.
- "Vínculos duplicados em 4 arquivos" → só há 1 vigente; demais são `.bak_*` de
  segurança e cópias legadas `_B1X.json` (B13–16), não lidos por nenhum portão.
