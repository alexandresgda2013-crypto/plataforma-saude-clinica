# SCHEMA-CLAIM v2 — PROPOSTA FORMAL PARA RATIFICAÇÃO (perícia externa)
**Data: 2026-09-11 · Origem: agente (Rodada de Harmonização) · Status: PROPOSTA — nada aqui é unilateral; cada item já traz o estado atual e o impacto.**

Contexto: a rodada de harmonização executada hoje aplicou reparos *lossless* e
registrou decisões (D1–D9, F1–F2) em `DECISOES_HARMONIZACAO_SCHEMA_2026-09-11.md`.
Os pontos abaixo NÃO cabem em reparo de dado — são decisões de schema/contrato que
pedem ratificação da perícia.

---

## P1 — `desenho_evidencia` (qualificador ortogonal novo) — IMPLEMENTADO, pede-se adoção
Força causal (4 tiers) e desenho do estudo são eixos ortogonais que a série B7/B8
havia fundido num valor só (`tier_2_meta_analise`). Implementação aplicada: 106
registros decompostos lossless — `forca_causal` (enum oficial de 4 tiers) +
`desenho_evidencia ∈ {intervencao_humana, meta_analise, revisao_sistematica,
mecanistico_animal, mecanistico_invitro, observacional_transversal}` (extensível).
Pedido: consagrar o campo no schema (opcional, não-enum fechado a princípio).

## P2 — Extensão de `natureza_relacao`: `refutadora`
Hoje: 13 vínculos B7/B8 cuja referência REFUTA a relação foram mapeados para
`nao_estabelecida` (fiel, mas perde o sinal "há evidência contrária" — que é
informação científica valiosa, distinta de "faltam dados"). Valores originais
preservados em `nota_reparo`. Pedido: acrescentar `refutadora` ao enum; se aprovado,
re-aplicamos nos 13 (trilha já os identifica id-a-id).

## P3 — Extensão de `g2_elegibilidade` (vínculo): `nao_aplicavel`
B13: 49 registros usam `nao_aplicavel` (G2 não se aplica àquela fonte) — sem
equivalente fiel no enum (`nao_avaliado` ≠ `nao_aplicavel`). Mantidos como extensão
declarada no manifesto B13 (aviso nomeado no instrumento). Pedido: acrescentar ao
enum, ou indicar o destino oficial.

## P4 — `ID_PAT` de vínculo: `\d{3,4}` para série legada; `\d{4}` obrigatório para novos
1.541 vínculos em 12 bibliotecas usam `VINC_B<n>_NNN` (3 dígitos). Renumerar
quebraria referências externas (relatórios periciais citam ids) sem ganho científico.
Instrumento do agente já os reporta como aviso nomeado `D9_id_legado3dig`. Pedido:
ratificar (ou ordenar renumeração com tabela de mapeamento publicada).

## P5 — Variantes pt→oficiais de enum (tabela de tradução a ratificar)
Aplicadas hoje com nota_reparo por registro; reversíveis. Pedir ratificação formal
(MAPEAR_VOCABULARIO.md não está neste workspace — trabalhamos com a tabela LEGADO
embutida no contrato.py + decisões documentadas):
`CONFIRMADA→VALIDADO` (1218) · `PARCIAL→TRIADO` (13) · `VALIDADO_G3_IA→VALIDADO` /
`PENDENTE_FULLTEXT→TRIADO` (tabela oficial da perícia, 265) ·
`revisao_mecanistica→review` (206) · `preclinico_mecanistico→preclinical_mechanistic` (125) ·
`meta_analise→human_clinical` (15, REVISAVEL) · `moderado_suportado→moderadamente_suportado` (43) ·
`incipiente→emergente` (27, REVISAVEL) · `humano_clinico→verificado` em verification_status (150) ·
`eligible_source→eligible` (118).

## P6 — Arquitetura de verificação da "geração nova" (B14–B16) — F1
753 registros carregam `status_auditoria` + `data_verificacao` mas NÃO carregam
`verification_status`, `g3_verificado_por` (ou `verificacao{}`), `status_referencia`,
`g2_elegibilidade`. Nada foi preenchido: inventar "quem verificou o quê" é vedado.
Opções: (a) contrato reconhece a arquitetura alternativa (exige documentá-la); ou
(b) **recomendação do agente: reprocessamento assistido dos metadados de
verificação das três bibliotecas** (a ausência de assinante G3 é lacuna real de
auditoria, não só de formato). Pedido: decisão.

## P7 — `status_referencia` deve ser obrigatório no contrato de vínculo
Hoje o campo não é obrigatório → B04/B05 têm 94/116 registros sem ele sem que nada
dispare (silêncio). Pedido: promover a obrigatório (com exceção nomeada enquanto a
geração nova não é reprocessada).

## P8 — Ancoragem por linha-lote (`*A|B|C*`)
B14–B16 (e resíduos em B6/B12) ancoram vínculos em linhas-lote de referências, que
não são frases-claim. A regra 5ª-rodada (âncora = frase com citação nominal da
própria ref) já foi aplicada onde havia candidata única. Pedido: o SCHEMA v2 deve
vedar linha-lote como `trecho_ancora` (claimer frase-claim obrigatória), o que
formaliza o fim do padrão D2.

## P9 — `canonica_sha256` + `data_extracao` nos artefatos de evidência
Vínculos/ledgers devem registrar o hash da Canônica contra a qual foram extraídos
(E5 da rodada 4) — prova de proveniência e detector de deriva. Pedido: incluir no
schema (o agente já computa sha256 nos registros de auditoria das Canônicas).

## P10 — Contrato: lacunas admitidas a completar
- prefixo de literalidade 85–99% hoje passa silentemente → reportar como aviso;
- reconciliação 1:1 ledger↔vínculos↔refs (B7: 78≠71≠116; B8: 87≠83≠145) → o
  contrato deve exigir ou nomear a política de cardinalidade;
- `verificacao{}` (dict) vs campos planos: unificar ou formalizar os dois perfis.

---
**Nota de auditoria:** proposta elaborada 2026-09-11 a partir de dados medidos nos
arquivos (censo pós-harmonização). Nenhuma alteração de schema foi feita
unilateralmente — implementações prévias (P1) estão revertíveis e trilhadas.
