# SUBSCRIÇÃO — SCHEMA-CLAIM v1.3 rev.3 (V-K1..V-K7)

**Auditor-Mestre · 2026-09-25**
**Objeto:** `SCHEMA-CLAIM v1.3 rev.3` — sha `28cbc9c76006f485f340da124aa1795833afa56d38e6572a9279d94a88f6b94c`
**Verificado contra:** rev.2 `bd9360e0…` (subscrita) · N2 v1.4 `d96ad15b…` (projeto)

---

## RESPOSTA: **SUBSCREVO SEM RESSALVA**

Agora com o arquivo certo em mãos. Verifiquei os três pontos que eu tinha condicionado na rodada anterior, e os três passam.

## 1. O arquivo é a rev.3, e o diff é limpo

Confirmei: a rev.3 contém V-K6 (4 ocorrências) e V-K7. O diff rev.2→rev.3 no **corpo do schema** é de quatro linhas, todas a nota de precedência V-K6 dentro de `sentido_do_achado`; o resto do acréscimo está nos comentários de migração (V-K6 e V-K7 como validadores). **Nada do corpo P-K1/P-K2/P-K3/P-K5 que subscrevi na rev.2 mudou** — o que eu já havia auditado permanece intacto, e só as duas regras novas foram somadas.

## 2. A V-K6 preserva o sentido e evita o par que reprova — provado no schema

Era a minha reserva: a V-K6 podia estar escrita de modo a perder o `sentido_do_achado` ao materializar `condicional`. Não está. Simulei os dois casos contra o N2 v1.4 selado:

| Materialização | N2 v1.4 |
|---|---|
| copiar sentido **e** condição → `sustenta` + `condicao` | **REPROVA** ("condicao deve ser null") |
| V-K6, precedência → `condicional` + `condicao` | **ACEITA** |

A V-K6 troca exatamente o caso reprovado pelo aceito. E o texto da regra é o correto nos dois lados: quando há `condicao_aplicacao` aplicável, materializa `condicional` + `condicao`, **e o `sentido_do_achado` fica registrado no claim, não é copiado como `direcao_suporte` neste ato**. O sentido não se perde — permanece recuperável via `claim_id`. É a mesma correção de D1 e do P-K6, aplicada ao ponto que faltava: quando os dois campos coincidem na mesma fonte.

É também a resposta certa à colisão que o Estrutura levantou (TRILHA99): sem a precedência, uma fonte com sentido próprio **e** condição geraria `sustenta`+`condicao`, que o N2 rejeita — "o mesmo colapso de D1 na saída", como a própria nota diz. A V-K6 é contrato de materialização, não altera o N2 — conferido: nenhuma mudança no schema N2.

## 3. A V-K7 está correta e a distinção importa

A V-K7 diz: `grau_maturidade_cientifica` vazio → **campo omitido** no N2, nunca `null` gravado. Verifiquei por que a distinção não é cosmética: o enum do N2 v1.4 **aceita `null`** (`[…, hipotese_inicial, null]`). Se a materialização gravasse `null`, seria formalmente válido — mas afirmaria positivamente "maturidade avaliada e indeterminada", quando o correto é "maturidade não avaliada". Omitir o campo diz a segunda coisa; gravar `null` diz a primeira. A V-K7 escolhe a omissão, que é semanticamente honesta: ausência de avaliação ≠ avaliação com resultado nulo. É a mesma disciplina do resto do contrato — não afirmar o que não foi decidido.

## Os cinco pontos do meu território, revisitados na rev.3

Os quatro que subscrevi na rev.2 continuam valendo (corpo idêntico). O quinto — "a saída ao materializador é suficiente para preservar o significado" — **melhora** na rev.3: o caso `sentido + condição na mesma fonte`, que na rev.2 dependeria de o materializador escolher certo, agora tem regra explícita (V-K6) que o impede de gerar o par inválido e preserva o sentido. Menos espaço para o materializador errar é exatamente o que o meu território pede.

---

## Subscrição formal

> **Subscrevo, sem ressalva, a minuta Schema-Claim v1.3 rev.3 (V-K1 a V-K7, com V-K6 e V-K7 resolvendo a reserva do Estrutura).**

Registro que a rev.2 que eu subscrevi não substitui esta — o documento mudou, e reauditei o delta. A V-K6/V-K7 não reabrem D1, não alteram N1/N2 e não importam eixos mecanísticos. Pelo rito, o ciclo do kit fecha com a subscrição sem ressalva do Estrutura e a verificação da casa.

---

*Verificações desta rodada: sha da rev.3 conferido; diff rev.2→rev.3 confinado a V-K6/V-K7; corpo P-K1/P-K2/P-K3/P-K5 idêntico entre rev.2 e rev.3; V-K6 simulada contra o N2 v1.4 (par sustenta+condicao REPROVA, condicional+condicao ACEITA); enum `grau_maturidade` do N2 aceita null, o que torna a escolha de omissão da V-K7 uma decisão semântica real. N2 lido no projeto; minuta recebida no upload.*
