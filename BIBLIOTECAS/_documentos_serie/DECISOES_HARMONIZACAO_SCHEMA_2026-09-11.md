# DECISÕES DE HARMONIZAÇÃO DE VOCABULÁRIO E CONTRATO — 2026-09-11
**Registro normativo da rodada de harmonização (Fila A/B do ROTEIRO_PROJETO.md).**
Princípios: (1) ciência primeiro — nenhum valor é "adivinhado"; toda conversão é
*lossless* (o valor original fica gravado em `nota_reparo` no próprio registro e na
trilha `producao/`); (2) conversão nunca silenciosa — cada mapa abaixo é decisão
registrada, submetida à ratificação da perícia externa no pacote da Rodada 2;
(3) regra do operador 2026-09-11: mudança de metadado = versão de ponto; conteúdo
científico = versão principal; nota datada em tudo.

Fontes oficiais usadas: `contrato.py` da perícia (enums + tabela LEGADO
`VALIDADO_G3_IA→VALIDADO`, `PENDENTE_FULLTEXT→TRIADO`, que aqui é APLICADA como
conversão registrada — a própria lei manda que sair da lista exige decisão
registrada), PROMPT v4.2 L1438/L1441 (eixos ortogonais), SCHEMA-CLAIM v3.1.

---

## D1 — status_referencia (G1-G3 de referência; enum: CANDIDATO, TRIADO, VALIDADO, REJEITADO)

| Valor observado (contagem) | Decisão | Justificativa |
|---|---|---|
| `CONFIRMADA` (1218: B02 61, B03 165, B04 37, B05 44, B06 108, B07 66, B08 75, B09 111, B10 137, B11 96, B12 111, B13 207) | **VALIDADO** | Variante pt do estado decidido/confirmado; os registros carregam assinatura G3 própria. |
| `PARCIAL` (13: B07 5, B08 8) | **TRIADO** | "Parcial" = verificado em abstract, fulltext pendente — mesma posição epistêmica do precedente oficial `PENDENTE_FULLTEXT→TRIADO`. Nunca para cima (VALIDADO inflaria). |
| `VALIDADO_G3_IA` (264: B01 236, B02 28) | **VALIDADO** | Tabela LEGADO oficial da própria perícia, agora aplicada como decisão registrada. |
| `PENDENTE_FULLTEXT` (1: B01) | **TRIADO** | Idem. |

## D2 — evid_role (enum: preclinical_mechanistic, human_clinical, human_experimental, post_mortem, review)

| Valor observado (contagem) | Decisão |
|---|---|
| `revisao_mecanistica` (206: B03 54, B04 59, B05 50, B06 43) | **review** (revisão mecanística continua sendo síntese secundária; flavor preservado em nota_reparo) |
| `preclinico_mecanistico` (125: B03 42, B04 14, B05 49, B06 20) | **preclinical_mechanistic** (tradução direta) |
| `meta_analise` (15: B03 2, B04 6, B05 7) | **human_clinical** (MA neste acervo pooling de estudos humanos clínicos; valor original preservado; linha marcada REVISAVEL na trilha) |

## D3 — natureza_relacao (enum: causal, contributiva, associativa, compensatoria, marcador, nao_estabelecida)

Regra de teto coerente com a força causal registrada (eixo ortogonal, PROMPT v4.2 L1438):
tier_3 (=correlacional/mecanístico de modelo) não sustenta etiqueta `causal`; tier_4 (=descritivo/estrutural) sustenta no máximo associação/marcador.

| Valor observado | Decisão | Regra de conteúdo |
|---|---|---|
| `tier_3_correlacional_mecanistico` em natureza (B01: 17) | **contributiva** | Achados mecanísticos em modelo (micróglia/LPS, succinato→HIF-1α, itaconato/IRG1, Cx43, glinfático, IL-17A/BLA…) — mecanismo demonstrado opera como contribuição, sem demonstração de necessidade/suficiência. Tabela id-a-id na trilha. |
| `tier_4_descritivo_estrutural` em natureza (B01: 10) | **associativa** / **marcador** / **nao_estabelecida** por conteúdo | Linguagem de nulo ("não diferiu", "resultado nulo") → nao_estabelecida; linguagem de biomarcador-alvo ("alvo diagnóstico", "marcador") → marcador; demais (associações descritivas em humano, heterogêneas) → associativa. Tabela id-a-id na trilha. |
| `descritiva` (B07: 7, B08: 7) | por conteúdo | Ausência/invalidação ("não há", "não validado") → **nao_estabelecida**; descrição de mecanismo ("é cofator", "atua como", "produzem", vias, ecologia) → **contributiva**; evidência preliminar/quadro descritivo de associação → **associativa**. |
| `refutadora` (B07: 4, B08: 9) | **nao_estabelecida** | Evidência que REFUTA a relação ⇒ por aquela referência a relação não está estabelecida. Sinal de refutação preservado em `nota_reparo`; SCHEMA v2 propõe extensão oficial `refutadora` (ver F2). |

## D4 — grau_maturidade (enum: muito_estabelecido, bem_suportado, moderadamente_suportado, emergente, hipotese_inicial)

| Valor observado | Decisão |
|---|---|
| `moderado_suportado` (43: B07 10, B08 33) | **moderadamente_suportado** (variante/typo direto) |
| `incipiente` (27: B07 7, B08 20) | **emergente** (os registros citam dados humanos diretos, ainda que mistos — hipotese_inicial reservado a ausência de dado direto; linha marcada REVISAVEL na trilha) |

## D5 — forca_causal com desenho embutido (AT-12; B07: 57, B08: 49 = 106 registros)

Decomposição lossless já endossada pela perícia (qualificador ortogonal, proposta SCHEMA v2 implementada à frente, sem deixar vácuo):

| Valor observado | forca_causal (enum oficial de 4 tiers) | desenho_evidencia (NOVO campo) |
|---|---|---|
| `tier_2_intervencao_humana` (10) | tier_2_necessidade_ou_suficiencia | `intervencao_humana` |
| `tier_2_meta_analise` (24) | tier_2_necessidade_ou_suficiencia | `meta_analise` |
| `tier_2_revisao_sistematica` (7) | tier_2_necessidade_ou_suficiencia | `revisao_sistematica` |
| `tier_3_mecanistico_animal` (33) | tier_3_correlacional_mecanistico | `mecanistico_animal` |
| `tier_3_mecanistico_invitro` (1) | tier_3_correlacional_mecanistico | `mecanistico_invitro` |
| `tier_4_observacional_transversal` (31) | tier_4_descritivo_estrutural | `observacional_transversal` |

Prefixo de tier (juízo causal do registrador) é preservado 1:1; o sufixo de desenho
nunca portou força causal — vira qualificador. Nenhuma perda, nenhuma amplificação.

## D6 — verification_status com valor de outro campo (B11: 56, B12: 70, B13: 24)

`humano_clinico` é valor de *evid_role* gravado em *verification_status* (confusão
de campo na origem; evid_role correto já existe no registro). Decisão: **verificado**,
pois status_auditoria=CONFIRMADO + assinatura G3 própria existem nos mesmos registros.
Original preservado em nota_reparo.

## D7 — g2_elegibilidade (B13: 167)

| Valor | Decisão |
|---|---|
| `eligible_source` (118) | **eligible** (vocabulário de LEDGER gravado em vínculo — furo F2 da família B14; tradução registrada) |
| `nao_aplicavel` (49) | **MANTER como extensão declarada** — `nao_avaliado` ≠ `nao_aplicavel` (seria mentira semântica). Vira item de SCHEMA v2: acrescentar `nao_aplicavel` ao enum. Declarado no manifesto B13 e no instrumento (aviso nomeado, nunca silenciado). |

## D8 — assinatura G3 mista "IA G3 … eutils …" (AT-03/AT-04 + B09/B10; 254 registros)

A guarda do contrato ("G1 por ferramenta não assina G3 — suporte") dispara nos
sufrágios que misturam VERIFICADOR com MÉTODO G1. Reparo *data-side* endossado:
- `g3_verificado_por` := `IA G3 (Rodada [AT] GPM <Bn> 2026-09-09)` — fica o QUEM + contexto da rodada.
- O método (eutils esearch/esummary/efetch; abstract lido ref a ref) NÃO é apagado:
  permanece registrado — a string original integral vai para `nota_reparo` e para a
  trilha; `g1_metodo` dos registros já documenta eutils (verificado).
- Nada é escondido: a mudança separa QUEM verificou (IA) de COMO a fonte foi obtida
  (eutils), que é exatamente a fronteira que a guarda protege.

## D9 — IDs de vínculo com 3 dígitos (1541 registros em 12 bibliotecas)

**Decisão de schema, NÃO de dado:** reformatar 1541 ids quebraria referências
externas (relatórios periciais citam ids) sem ganho científico. A série legada
`\d{3}` é legitimada retroativamente; `\d{4}` segue obrigatório para registros
NOVOS. Instrumento do agente passa a aceitar `\d{3,4}` com AVISO NOMEADO
("id legado 3 dígitos — decisão D9"); a ratificação formal vai ao perito no
pacote da Rodada 2 (SCHEMA v2 item ID_PAT).

## F1 — B14/B15/B16 (arquitetura "geração nova")

Registros carregam `status_auditoria` + `data_verificacao` mas não carregam
`verification_status`/`g3_verificado_por`/`status_referencia`/`g2_elegibilidade`
(753 registros). Preencher esses campos seria INVENTAR dado de verificação
(quem verificou? com que método?) — vedado. Decisão: **lacuna de arquitetura a
resolver no SCHEMA v2** (E4: contrato deve reconhecer a arquitetura da geração
nova OU a geração nova deve ser reprocessada com o contrato — decisão a tomar
com a perícia; recomendação do agente: reprocessamento assistido dos metadados de
verificação, pois hoje não há como provar QUEM verificou o quê). Bibliotecas
permanecem com gates verdes; a dívida fica nomeada, não silenciada.

## F2 — propostas SCHEMA v2 consolidadas (a formalizar na Fila C)

`desenho_evidencia` ortogonal (implementado hoje em D5) · extensão `refutadora`
em natureza_relacao · extensão `nao_aplicavel` em g2_elegibilidade · ID_PAT `\d{3,4}`
legado · variantes pt→oficiais de enum (tabela D1–D4 ratificação) · arquitetura de
verificação da geração nova (F1) · status_referencia como obrigatório no contrato
(lacuna: B04/B05 têm 94/116 registros sem o campo e hoje isso não dispara nada).

---

**Nota de auditoria:** documento gerado na rodada de harmonização 2026-09-11; cada
decisão aqui vira `nota_reparo` por registro + trilha em `producao/` + entrada no
CHANGELOG_GERAL.md. REVISAVEL = linha que a revisão humana deve conferir primeiro.
