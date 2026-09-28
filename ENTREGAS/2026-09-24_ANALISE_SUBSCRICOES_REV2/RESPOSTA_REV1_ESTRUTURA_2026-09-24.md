# SUBSCRIÇÃO COM PONTO — AUDITOR-ESTRUTURA — CONTRATO DE SAÍDA DO CLAIM KIT

**Auditor-Estrutura · 2026-09-24** (texto enviado ao operador; arquivado verbatim pela casa)

Terminei. E preciso segurar a subscrição por um ponto — não é ressalva de redação, é uma contradição que o schema real reprova.

O núcleo de D1 eu subscrevo sem reserva: dois eixos, `aprovado_com_ressalva` não implica `condicional`, e a proibição de default do R-1. Está tudo certo, e o R-1 resolve a H-2 do jeito que eu tinha recomendado, importando `sentido_do_achado` da v3.1 em vez de inventar vocabulário.

O problema é o §4.3, o tratamento do `inverte`, e o caso é o `.001b` que a própria minuta escolheu como exemplo canônico.

O §4.3 manda materializar a inversão como dois N2 complementares, e escreve literalmente:

```
condição A → sustenta
condição B → refuta
```

Rodei isso contra o N2 v1.4. **As duas linhas são inválidas no schema.** O `allOf` que fechamos na v1.3 proíbe `condicao` preenchida quando `direcao_suporte` é `sustenta` ou `refuta` — `condicao` só é permitida com `condicional`. Então "condição A → sustenta" com a condição preenchida é exatamente o que o schema recusa.

A minuta pede, no §14, que a Arena verifique mecanicamente que ela corresponde aos contratos. Corresponde em tudo, menos aqui: o §4.3 descreve um par que o N2 vigente não aceita.

E não é conserto de sintaxe, porque as duas saídas possíveis pioram coisas que este ciclo protegeu:

- Se reescrever os dois ramos como `condicional` + condição — que é o que o schema aceita — perde-se a informação de que um ramo sustenta e o outro refuta. `condicional` não carrega o sentido; some justamente a inversão que o §4.3 existe para preservar.
- Se deixar `sustenta`/`refuta` e jogar a condição fora, perde-se a condição que separa os dois ramos.

Ou seja, com os campos de hoje, o caso `inverte` não tem representação fiel: ou perde o sentido, ou perde a condição. É a mesma classe de problema do D1 original — informação composta sem campo para as duas partes — só que agora entre `direcao_suporte` e `condicao`.

Minha resposta à pergunta única, então: **subscrevo D1 e R-1 sem ressalva; no R-2, subscrevo** `atenua`**/**`amplifica`**/**`nulo` **e a fonte única de condição; no** `inverte` **do §4.3, não subscrevo — impedimento estrutural, medido.**

E aponto o caminho, porque acho que ele fecha limpo. O `inverte` genuíno precisa de um campo de condição que coexista com `sustenta`/`refuta` — algo como `condicao_modificadora` na âncora, distinto do `condicao` atual que é atrelado a `condicional`. Aí o ramo A vira `sustenta` + `condicao_modificadora: classe A`, o ramo B vira `refuta` + `condicao_modificadora: classe B`, e os dois eixos ficam de novo separados: `direcao_suporte` diz o sentido, o novo campo diz sob qual condição, e `condicional`/`condicao` continuam reservados para o caso em que a evidência apoia sob restrição sem inverter.

Isso é alteração do N2 — pequena, um campo e um `allOf` — e portanto **não cabe fechar por esta minuta, que se declara "não altera N2 v1.4."** É material para o ciclo editorial v1.5 que já estava na mesa. Enquanto não existir, sugiro que a minuta faça no `inverte` o mesmo que fez com maturidade e moderadores: **declarar o caso como dependência estrutural não resolvida** — a informação completa fica no claim, acessível por `claim_id`, e o `inverte` não materializa em N2 até o campo existir. Isso é coerente com a própria regra da L-06 §5 que a minuta cita: representação inexistente é dependência estrutural, não coisa para forçar no campo errado.

Com essa troca — `inverte` vira pendência P-K travada, como P-K1 e P-K2 já são — eu subscrevo a minuta inteira sem ressalva. Do jeito que está no §4.3, a assinatura afirmaria correspondência com o N2 que a medição nega.
