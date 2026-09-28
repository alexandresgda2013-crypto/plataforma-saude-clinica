# 05 — Checklist da Auditoria Científica de Conteúdo

**Uso:** colar, em mini-rodada separada, junto com a `Biblioteca_Bx.md`, o Módulo 09 (5 arquivos) e o ledger. A IA reporta; o operador decide nos portões. Não corrige o documento — só reporta (a correção é a mini-rodada C, doc 06).

---

## A. Integridade do ledger

- [ ] **A1.** Existe um objeto no ledger para cada par (entrada do Módulo 09 × trecho onde ela é citada). Contagem: ___ trechos no corpo / ___ objetos no ledger.
- [ ] **A2.** Todo `id_referencia_interna` do ledger existe exatamente uma vez no Módulo 09 e o `arquivo_modulo09` bate com o classificador `[MA][EC][OB][ML][AT]`.
- [ ] **A3.** Todo `trecho_ancora` é encontrado literalmente na Biblioteca (diferença substancial = ERRO; pequena diferença de pontuação = AVISO).
- [ ] **A4.** Toda citação `(Autor, Ano)[tipo]` no corpo tem objeto correspondente no ledger; nenhuma referência do Módulo 09 está sem trecho (órfã).
- [ ] **A5.** Nenhum PMID/DOI aparece no texto corrido (regra do Prompt 4.0).

## B. G1 — Existência (por trecho)

- [ ] **B1.** Para cada trecho com `pmid_oficial` preenchido: o identificador resolve e os metadados (título/autor/ano/revista) conferem via busca nesta sessão.
- [ ] **B2.** `NAO_LOCALIZADO` e `PMID_INCORRETO` têm query registrada e passaram pelo resgate único.
- [ ] **B3.** Nenhum PMID foi aceito "de memória": todo `VERIFIED_REFERENCE` tem fonte/abstract colado na sessão ou esearch/esummary registrado.
- [ ] **B4.** Entradas `citacao_confirmada: false` / "referência a confirmar" foram 100% verificadas (não podem permanecer pendentes).

## C. G2 — Elegibilidade (por trecho)

- [ ] **C1.** Desenho aceito (tiers de força causal / tipos de modelo) e espécie declarada.
- [ ] **C2.** BLOCO_02–05 sem contaminação por desfecho de tratamento (salvo BLOCO_06.7/09.6).
- [ ] **C3.** Sem `exclusion_criteria`: off-target sem controle, preprint, retratado, in silico sem validação, anedótico — cada um registrado em `fontes_rejeitadas` com motivo.
- [ ] **C4.** Achado puramente associativo/clínico-epidemiológico foi para `redirecionados_modulo_clinico` (não para rejeitado), com `destino_sugerido`.
- [ ] **C5.** Elo causal de outro BLOCO/mecanismo foi para `fila_realocacao` com destino (ID oficial).

## D. G3 — Suporte ao trecho (o núcleo científico)

- [ ] **D1.** Toda decisão de G3 tem **abstract/trecho colado nesta sessão** (`verificacao.abstract_ou_trecho` não vazio).
- [ ] **D2.** O trecho respeita o **sistema experimental**: frase redigida como fato em humanos não está sustentada só por animal/in vitro — caso contrário `APROVADO_COM_RESSALVA` + sinalizador/`[EXTRAPOLAÇÃO POR ANALOGIA]`.
- [ ] **D3.** A **direção e a força** do trecho batem com a fonte (aumento/diminuição; causal/associativo; "demonstra" vs. "sugere"). Efeito clínico não é usado para afirmar mecanismo causal.
- [ ] **D4.** Aresta causal (`no_origem → no_destino`) é demonstrada pelo desenho, não inferida; abstract que só sugere = `INCONCLUSIVO`.
- [ ] **D5.** `dominios_grade_observados` preenchidos (não antes do G3); `risco_de_vies` só com texto completo, senão `nao_avaliado`.
- [ ] **D6.** Toda `APROVADO_COM_RESSALVA` tem `nota_ressalva` redigida e a ação de correção definida (sinalizador/rebaixamento).
- [ ] **D7.** Todo `NAO_SUSTENTA` tem cotação da fonte demonstrando a divergência e passou por resgate.

## E. Coerência com a Lista Canônica e IDs

- [ ] **E1.** Toda entrada `origem_entrada: LISTA_CANONICA` usa exatamente o PMID/autor/ano/achado do claim aprovado (conferência de integridade; G3 não é re-julgado).
- [ ] **E2.** `referencia_cruzada`/IDs oficiais citados validam contra `_ids_oficiais` (snake_case; nenhum ID proibido/removido).
- [ ] **E3.** Claims novos aprovados na auditoria foram registrados no Schema-Claim v3.1 (com `mapa_exportacao_modulo09`) e entram na Lista Canônica do BLOCO.
- [ ] **E4.** Fronteiras de mecanismo respeitadas (ex.: IDO/JAK-STAT = B1.MEC.BLOCO08; cinética da quinurenina = B4; neurogênese aprofundada = B16 — P16/P20).

## F. Escopo e filosofia (P20 / R04 / P12)

- [ ] **F1.** Sem valor de corte, protocolo de coleta, dose/posologia como recomendação na Biblioteca de mecanismo (P20). Entradas [EC] descrevem apenas o estudo.
- [ ] **F2.** Sem fonte proibida (blog, wiki, comercial, cinzenta, opinião) — Política de Fontes.
- [ ] **F3.** Todo conteúdo de outra condição clínica tem `[EXTRAPOLAÇÃO POR ANALOGIA: ...]` no corpo e no Módulo 09/ledger.
- [ ] **F4.** Biologia básica sem contexto de doença não foi sinalizada como extrapolação (exceção correta).

## G. Saída do relatório (formato obrigatório)

```
AUDITORIA DE CONTEÚDO — BIBLIOTECA [mecanismo]
Trechos auditados: [n] | APROVADO: [n] | COM_RESSALVA: [n] |
NAO_SUSTENTA: [n] | NAO_LOCALIZADO: [n] | PMID_INCORRETO: [n] |
ASSOCIATIVO_REDIRECIONAR: [n] | REALOCAR: [n] | ELEGIBILIDADE_FALHOU: [n] |
NAO_TRIADO/PENDENTE: [n]

A. Ledger: [conforme/não conforme] — divergências: [...]
B. G1: falhas de existência: [...]
C. G2: redirecionamentos/realoções/rejeições por desenho: [...]
D. G3: trechos não sustentados / linguagem acima da evidência: [...]
E. Lista Canônica/IDs: divergências: [...]
F. Escopo/filosofia: violações: [...]

VEREDITO: [APROVADO PARA INTEGRAÇÃO] ou [REQUER MINI-RODADA C — correções: ...]
```

**Critério de veredito:** `REQUER MINI-RODADA C` se houver qualquer trecho `NAO_SUSTENTA`, `NAO_LOCALIZADO`/`PMID_INCORRETO` não resolvido, violação de escopo (F), ou divergência com Lista Canônica/IDs (E). Caso contrário, `APROVADO PARA INTEGRAÇÃO`.

Este veredito é sobre **suporte factual das afirmações** — complementa, não substitui, o Checklist Estrutural (forma) e o Checklist de Sanidade do GPM (insumo).
