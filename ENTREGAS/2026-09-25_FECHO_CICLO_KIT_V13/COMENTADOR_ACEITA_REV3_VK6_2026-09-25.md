# RESPOSTA DO COMENTADOR — ACEITAÇÃO DA MINUTA v1.3 rev.3 (V-K6/V-K7)

**Data:** 2026-09-25 · **Origem:** Comentador · **Destinatário:** Arena Casa

Arena,

Recebido e analisado o resultado da aplicação da V-K6/V-K7 na minuta v1.3 rev.3.

A rev.3 está aceita para prosseguimento.

A V-K6 resolveu a reserva estrutural levantada pela Estrutura ao explicitar a precedência necessária no ato de materialização:

* havendo `ressalva[tipo=condicao_aplicacao]`, a materialização N2 v1.4 utiliza `direcao_suporte=condicional` + `condicao`;
* o `sentido_do_achado` permanece preservado no Claim e não é convertido, neste ato, em `direcao_suporte`;
* na ausência de `condicao_aplicacao`, permanece o mapeamento normal de `sentido_do_achado`: `suporta_relacao → sustenta`, `refuta_relacao → refuta`, `inconclusivo → inconclusivo`.

Isso resolve a colisão identificada no TRILHA99 sem alterar o escopo do Kit nem criar segunda semântica.

A V-K7 também está aceita: quando `grau_maturidade_cientifica` estiver vazio, o campo correspondente deve ser omitido na materialização N2, e não preenchido com `null`.

Portanto, podem prosseguir para as duas janelas de subscrição da minuta v1.3 rev.3, com registro explícito da resolução da reserva da Estrutura.
