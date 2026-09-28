# Processo de produção e ferramentas

## ⭐ LEIA PRIMEIRO: `00_PROCESSO_DE_GERACAO_LEIA_PRIMEIRO.md`
É o documento-mestre (**Processo de Geração v2.1**). Ele define o pipeline inteiro e
deve ser lido antes de tudo, pois explica a sequência:

- **RODADA 1** — Briefing → **GPM** (miolo molecular). Gate: Checklist de Sanidade do GPM.
- **RODADA 2** (3 atos) — busca por ferramenta (PubMed/eutils) → geração com o **Prompt v4.2**
  → rótulo **Pré-Canônica**. Gate: Checklist de Auditoria Estrutural.
- **PORTÃO G1→G2→G3** — auditoria científica em sessão separada (existência → elegibilidade → suporte).
- **RODADA 3** — Consolidação Canônica (proibido introduzir citação nova). Gate: Checklist de Fidelidade Canônica.

Os arquivos abaixo são exatamente os documentos que esse mestre manda usar em cada etapa.

---

## Mapa de documentos ATUAIS (sem duplicatas — versões antigas em `_arquivo_morto/`)

### RODADA 1 — GPM / briefing / schema
`02_fase1_gpm_profundidade/`
- `5º GERADOR DE PROFUNDIDADE MOLECULAR (GPM).md` — **molde GPM** (fixo, reusado 16×).
- `6º BRIEFING COMPLETO B1 — NEUROINFLAMAÇÃO.md` — **modelo de briefing** (exemplo de profundidade mínima; cada Bx terá o seu).
- `FASE 1- 03 CHECKLIST DE SANIDADE DO GPM.md` — gate da Rodada 1.
- `3º SCHEMA-CLAIM — MECANISMO v3.1.md` — schema oficial de claim.
- `7º LISTA CANÔNICA — B1 TRILHA MECANÍSTICA GPM_B1 ARENA.md` — lista canônica de claims aprovados (exemplo B1; opcional).

### RODADA 2 — Prompt de geração da biblioteca
`03_fase2_geracao_biblioteca/`
- `PROMPT FINAL — BIBLIOTECA ... PMID v4.2.md` — **Prompt 4.2 VIGENTE** ("Mecanismos de Ansiedade e Depressão"; autoridade final sobre estrutura/qualidade/seleção).

### RODADA 3 / PORTÕES — auditoria (forma + verdade)
`04_fase3_auditoria_fidelidade/`
- `CHECKLIST DE AUDITORIA ESTRUTURAL DA BIBLIOTECA.md` — **estrutural v1.1** (forma; gate pós-Rodada 2).
- `FASE 3- CHECKLIST FIDELIDADE CANONICA.md` — **fidelidade canônica** (gate de fechamento; regra anti-autocertificação E1–E3).

`05_framework_auditoria/`
- Documentos 00–08 do framework de auditoria G1→G2→G3 (protocolo, ledger, delta do Módulo 09,
  checklist de conteúdo, mini-rodada C, aprovação final, guia de execução) + `scripts/validar_auditoria.py`.

### Norteadores (regras-base que valem para todo mecanismo)
`01_norteadores/`
- `FASE 2- 02 FILOSOFIA DO PROJETO.md` — princípios e fronteiras (P20, P16…).
- `CONTRATO DE GERAÇÃO DECISÕES ARQUITETURAIS.md` — decisões de design.
- `ESTRUTURA MESTRE — TRILHA MECANÍSTICA v1.1.md` — macro-estrutura B1–B16.
- `1º IDS_OFICIAIS.md` — IDs oficiais de exames/mecanismos/cenários.

---

## Onde ficam as ferramentas e o material de cada mecanismo
Os **scripts** (.py) de geração/auditoria e o material de rodadas (briefings, GPM, relatórios,
versões antigas) **não estão aqui** — ficam dentro de cada mecanismo, pois são atrelados àquele
arquivo/Módulo 9:
- Produto: `BIBLIOTECAS/<Bx_Nome>/Biblioteca_Bx_vN_..._CANONICA.md` + `Evidencias/`
- Scripts: `BIBLIOTECAS/<Bx_Nome>/ferramentas_geracao/`
- Rodadas/relatórios/histórico: `BIBLIOTECAS/<Bx_Nome>/processo_rodadas/` e `historico_versoes/`

## Duplicatas/versões substituídas
Cópias antigas (Prompt 4.0, schema v1.2, Processo v2.0, estruturas-mestre base, checklists
duplicados, etc.) foram movidas para `_arquivo_morto/` — não usar para geração; ficam só de rastro.
