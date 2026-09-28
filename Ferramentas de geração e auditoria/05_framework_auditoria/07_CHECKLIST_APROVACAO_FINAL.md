# 07 — Checklist de Aprovação Final de Conteúdo (portão de integração)

**Uso:** após a mini-rodada C. É o último portão antes de a `Biblioteca_Bx.md` virar fonte canônica do mecanismo. Zero item `ERRO` em aberto.

---

## A. Fechamento do ciclo de evidência

- [ ] **A1.** Toda afirmação factual do corpo tem, no ledger, um trecho `APROVADO` ou `APROVADO_COM_RESSALVA` (com sinalizador aplicado).
- [ ] **A2.** Nenhum trecho permanece `PENDENTE`, `NAO_TRIADO`, `NAO_SUSTENTA`, `NAO_LOCALIZADO` ou `PMID_INCORRETO` sem ação de correção aplicada.
- [ ] **A3.** Toda `APROVADO_COM_RESSALVA` tem nota de ressalva na Lista/claim e sinalizador visível no texto.
- [ ] **A4.** Claims novos aprovados na auditoria estão na Lista Canônica (Schema-Claim v3.1 completo, com `mapa_exportacao_modulo09`).
- [ ] **A5.** `usado_em_biblioteca: sim` marcado nos claims efetivamente usados; claims aprovados mas não usados justificados ou registrados.

## B. Rastreabilidade ponta a ponta (teste por amostragem)

- [ ] **B1.** Sorteio mínimo de 5 frases por BLOCO: frase → trecho_ancora no ledger → entrada do Módulo 09 → PMID verificado (G1) → abstract/trecho colado (G3). Qualquer elo quebrado volta à mini-rodada C.
- [ ] **B2.** Toda entrada do Módulo 09 tem `ids_auditoria` (se o delta foi adotado) ou aparece no ledger; nenhuma referência órfã.
- [ ] **B3.** Toda citação `(Autor, Ano)[tipo]` do corpo resolve para uma entrada com `status_auditoria` agregado `VERIFICADA` (ou ressalvada), e as âncoras `[REF_BLOCO_XX]` batem.
- [ ] **B4.** Nenhum PMID/DOI no texto corrido.

## C. Linguagem e evidência

- [ ] **C1.** O nível de linguagem bate com a evidência, parágrafo a parágrafo: "demonstra/causa/confirmado" só onde G3 confirmou esse nível.
- [ ] **C2.** Evidência animal/in vitro de condição diferente tem `[APENAS PRÉ-CLÍNICO]`/`[EXTRAPOLAÇÃO POR ANALOGIA: ...]`; biologia básica sem doença não foi sinalizada indevidamente.
- [ ] **C3.** Sinalizadores do Prompt 4.0 aplicados onde necessário (`[CONTROVERSO]`, `[CORPO DE EVIDÊNCIA LIMITADO]`, etc.).
- [ ] **C4.** Sem conteúdo prescritivo (P20): doses/cortes/protocolos ficam nos módulos operacionais; entradas [EC] descrevem apenas o estudo.

## D. Disciplina do processo

- [ ] **D1.** O Checklist Estrutural foi rodado de novo após as correções e segue aprovado (forma não quebrou).
- [ ] **D2.** A mini-rodada C não introduziu fato/citação/claim novo — qualquer novidade foi para a Lista Canônica/filas, não para o texto.
- [ ] **D3.** Bloco de Estado do mecanismo atualizado: `claims_aprovados`, `fontes_rejeitadas`, `fila_realocacao`, `redirecionados_modulo_clinico`, `resultados_nao_triados`.
- [ ] **D4.** IDs oficiais validados contra `_ids_oficiais` (snake_case; sem IDs proibidos/removidos); fronteiras B1–B16 respeitadas (P16/P20).
- [ ] **D5.** `historico_correcoes`/corte_literatura atualizados conforme R06 (quando aplicável).

## E. Declaração de aprovação

- [ ] **E1.** Registrado: mecanismo, data, sessão, contagens do relatório (aprovados/ressalva/não sustenta/não localizado/redirecionados/realoções/rejeições), e a declaração:

> "A Biblioteca_Bx foi auditada quanto a conteúdo em AAAA-MM-DD: cada afirmação factual tem vínculo verificado por fonte (G1→G2→G3) ou está explicitamente sinalizada como evidência parcial/pré-clínica. Referências não sustentadas foram removidas/trocadas/rebaixadas na mini-rodada C. Ledger e decisões arquivados em /Auditoria_Bx."

- [ ] **E2.** Pendências (`NAO_TRIADO`, claims `em_busca`) arquivadas para próxima leva — não bloqueiam a integração, mas estão registradas.
- [ ] **E3.** GPM_Bx pode ser arquivado (ferramenta de produção, descartável após aprovação).

**Resultado:** `BIBLIOTECA APROVADA E INTEGRADA` ou `VOLTAR PARA MINI-RODADA C` com os itens específicos.
