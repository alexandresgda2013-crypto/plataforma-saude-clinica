# MOTOR_CLINICO — visão consolidada da série (data de geração: 2026-09-11)

## O que é esta pasta
Visão "todos juntos" das evidências de maior peso clínico da série B1–B16,
gerada para consumo do motor clínico, **depois** da distribuição oficial do
Módulo 09 (`[MA]`→02, `[EC]`→03) ser finalmente executada dentro de cada
biblioteca (ver `CHANGELOG_GERAL.md`, entrada 2026-09-11).

## Arquivos
| Arquivo | Conteúdo | N |
|---|---|---|
| `evidencias_pmids_serie.json` | **TODAS as referências da série juntas (todos os PMIDs)** (5 arquivos Bibliografia × 16 mecanismos), dedup por PMID, `classe_serie` por registro | 2.577 |
| `evidencias_ma_serie.json` | Meta-análises e revisões sistemáticas (schema 09.2) — subconjunto | 268 |
| `evidencias_ec_serie.json` | Ensaios clínicos randomizados — subconjunto | 58 |

> **rev. 2026-09-11:** renomeado `evidencias_todas_serie.json` → **`evidencias_pmids_serie.json`**
> (sugestão do operador — padroniza com `01_pmids.json` e com `ma`/`ec`: o arquivo
> contém exatamente "todos os PMIDs" da série).

**Composição do consolidado geral** (`evidencias_todas_serie.json`, rev.1):
**268** meta-análise/revisão sistemática · **58** ensaio clínico randomizado ·
**2.251** nível base · dos quais **102** aparecem em mais de uma biblioteca
(listados uma vez, com todas as casas em `bibliotecas[]`).
Conflito de classe resolvido por prioridade MA>EC>base — 1 caso nomeado na
trilha (PMID 30646157, ficha MA da B8 prevaleceu sobre gêmea base de outra bib).

- **Dedup por `pmid_oficial`**: o mesmo estudo citado em mais de uma biblioteca
  aparece UMA vez aqui, com `bibliotecas: ["B01_...", "B03_", ...]`.
- Cada registro preserva a ficha integral da biblioteca de origem
  (`titulo_artigo`, `achado_central_molecular`, `g1|g2|g3*`…), mais
  `classe_serie` e `bibliotecas[]`.
- Fonte da verdade **continua sendo a pasta de cada mecanismo**
  (`Bxx/atuais/Evidencias/Bibliografia/02_…|03_…`): este consolidado é derivado,
  regenerado pela mesma regra mecânica (script
  `_documentos_serie/scripts_serie/separa_ma_ec_09.py`, trilha
  `trilha_09_distribuicao_MA_EC_serie_2026-09-11.json`).

## Regra de classificação (mecânica, replicável — zero invenção)
- **MA**: etiqueta `[MA...]` declarada na canônica (`desenho_estudo`) OU título
  contendo *meta-anal\** / *systematic review* (sinal objetivo PubMed).
- **EC**: título/desenho contendo *randomized|double-blind|placebo-controlled|
  crossover|duplo-cego*. Prioridade **MA > EC** quando ambos disparam.
- **Não migraram (dívida nomeada, decisão com ratificação externa):** 390
  registros etiquetados `[EC]` em sentido amplo (evidência clínica humana sem
  sinal objetivo de RCT — o schema 09.3 é reservado a RCT estrito). Todos
  nomeados id-a-id nas trilhas `producao/09_distribuicao_MA_EC_<Bn>_…`.

## Dívidas nomeadas (não silenciadas)
- `forca_evidencia_afirmacao` (obrigatório no schema 09.2): preenchido só onde
  a ficha já trazia (4 fichas); nos demais fica `""` — preenchimento exige
  avaliação evidência-por-evidência; **nunca fabricado**.
- 27 conflitos etiqueta×título resolvidos por prioridade MA e listados
  `[REVISAVEL]` nas trilhas.
- Mapeamento doc `[ML]`→`05_manuais_e_livros.json` permanece **não executado**
  (ambíguo; fora do pedido).
