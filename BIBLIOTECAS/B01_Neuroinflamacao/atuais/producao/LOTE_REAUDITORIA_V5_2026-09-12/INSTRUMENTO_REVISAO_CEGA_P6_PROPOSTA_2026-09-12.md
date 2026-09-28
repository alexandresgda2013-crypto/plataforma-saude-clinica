# INSTRUMENTO DE REVISÃO CEGA (P-6) — **PROPOSTA v0.1 para ratificação do Auditor-Mestre**
**Data:** 2026-09-12 · **Escopo:** fila `FILA_REVISAO_CEGA_ALTO_RISCO_B1_2026-09-12.json` (108 vínculos / 91 referências; critério operacional declarado no próprio arquivo).

**Natureza deste documento (declaração honesta):** não existia instrumento formal preservado para a P-6
(2ª verificação independente por avaliador cego humano/externo) — as menções ao P-6 no projeto são de
disciplina, não de formulário. Esta é uma **proposta construída a partir do que o pipeline já registra**
(portões G1/G2/G3 e as 3 perguntas usadas na rodada de auditoria científica), para ser ratificada ou
emendada pelo Auditor-Mestre antes do uso. Não é apresentada como instrumento oficial preexistente.

---

## 1. Princípio de cegueira
- O avaliador recebe **somente**: id_vinculo, trecho_ancora (a frase da canônica) e o abstract/full-text
  da referência (via PubMed/PMC). **Não recebe**: vereditos anteriores, g3_notas, status_auditoria,
  natureza_relacao, forca_causal nem qualquer campo do pipeline interno.
- O avaliador não sabe quais itens são de refs [AT] novas nem quais já têm rodada full-text (22).
- Envio sugerido: CSV/JSON com as 3 colunas mínimas por item + PMID/PMC para busca própria do avaliador.

## 2. As 3 perguntas G3 (por vínculo), com gabarito de resposta fechado
1. **PERTENCIMENTO** — o artigo pertence ao mecanismo em questão na frase?
   `pertence | tangencia | não pertence | não decido pelo abstract`
2. **SUPORTE** — o artigo sustenta a afirmação *na forma e força* em que está escrita (direção, espécie,
   desenho, números)? `sustenta integralmente | sustenta com ressalva (descrever) | não sustenta | contradiz`
3. **ROBUSTEZ** — a fonte é suficiente para o peso dado na frase?
   `adequada | frágil (descrever) | precisa rebaixar linguagem`

## 3. Campos adicionais por item
- `direcao_efeto_confere`: sim/não/na (para achados com direção — ex.: ↑/↓ metabólito)
- `especie_confere`: humano/animal/in vitro — conforme o abstract lido
- `desenho_confere`: o desenho real (pubtype) × o rótulo usado na canônica (OB/MA/EC/ML)
- `discrepancia_numerica`: descrever (n, efeito, ano, etc.) ou vazio
- `veredito_final_item`: CONFIRMADO | PARCIALMENTE_CONFIRMADO | NAO_SUSTENTA | NAO_DECIDO (com motivo livre obrigatório se ≠ CONFIRMADO)
- `confianca_avaliador`: alta/média/baixa
- `tempo_gasto_min` (opcional; para estimar viabilidade de cobrir os 108)

## 4. Regras de decisão sugeridas
- Qualquer `não sustenta`/`contradiz` ⇒ item volta à reconciliação com prioridade GRAVE (mesmo rito das
  condições R*: prova eutils/efetch anexada à resposta).
- `sustenta com ressalva` ⇒ vira MODERADO e entra na trilha da próxima manutenção.
- `não decido pelo abstract` ⇒ promovido automaticamente à sub-fila **full-text (PMC)** antes do veredito
  (precedente interno: rodada G3 full-text 2026-09-04, 22 claims).
- Itens CONFIRMADOS por ambos (pipeline + cego) ⇒ retiram o vínculo da fila de alto-risco e atualizam
  `verificacao.verificador` removendo "P-6 PENDENTE".

## 5. Amostragem e carga
- Fila completa: 108 vínculos (recomendado — a réplica condiciona a retirada do status PROVISÓRIO à
  revisão da fila; o nominal histórico era 59 antes da leva [AT]).
- Se recursos limitarem: estratos mínimos obrigatórios = **todos** os 22 da rodada full-text (revisão
  confirmatória) + todos os refs [AT] (leva 2026-09-08) da fila + todos com status PARCIALMENTE_CONFIRMADO.

## 6. Material de apoio entregue neste lote
- `FILA_REVISAO_CEGA_ALTO_RISCO_B1_2026-09-12.json` — 108 itens com âncora literal e PMID.
- `RELATORIO_G3_FULLTEXT` (histórico, em antigos/historico/ — metodologia dos 22).
- Canônica V5 (contexto das âncoras) e Lista Canônica v1.2 (claims-alvo).

**Ratificação solicitada:** o Auditor-Mestre pode alterar 2–5 à vontade; a casa executará a fila sob o
instrumento ratificado e registrará a versão em `decisoes_B1.md` e no CHANGELOG.
