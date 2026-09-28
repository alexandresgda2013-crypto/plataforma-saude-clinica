# SUBSCRIÇÃO DO AUDITOR-MESTRE — MINUTA rev.2 (D1 + R-1 + R-2 + P-K6)

**Auditor-Mestre · 2026-09-24**
**Objeto:** `MINUTA_CONTRATO_SAIDA_CLAIMKIT_rev2_2026-09-24.md` (declarada `841532da…`)
**Verificado contra:** N2 v1.4 `d96ad15b…` (projeto) · Schema-Claim-Mecanismo v3.1 (recebido no pacote) · vínculos B1 V7 `490675e6…` · L-06 rev.6 vigente

---

## RESPOSTA: **SUBSCREVO SEM RESSALVA**

E a subscrição vem com uma retratação, porque a rev.2 corrige um erro **meu** da rev.1.

---

## 1. O furo da minha rev.1 — confirmado por mim, contra o schema

Na rev.1 subscrevi a materialização de `inverte` como "dois N2 complementares: condição A → sustenta, condição B → refuta", e afirmei que isso era "estruturalmente possível e já praticado", apoiado em 30 referências do acervo com múltiplos vínculos.

**Estava errado, e o erro é preciso.** Reproduzi o N2 v1.4 selado com validador JSON Schema:

| Caso | N2 v1.4 |
|---|---|
| `sustenta` + `condicao` preenchida (o que propus) | **REPROVA** — "condicao deve ser null" |
| `refuta` + `condicao` preenchida (idem) | **REPROVA** |
| `condicional` + `condicao` | aceita |
| `sustenta` + `condicao` null | aceita, **mas perde a condição** |

O `allOf` do N2 impõe: `condicao` só existe quando `direcao_suporte = condicional`; com `sustenta`/`refuta`, `condicao` **tem de ser null**. Logo o par que propus é inexequível: ou cada ramo é `sustenta`/`refuta` e **perde a condição que o distingue** (ISRS × tricíclicos vira dois vínculos sem dizer a qual classe cada um se aplica), ou é `condicional` e deixa de ser `sustenta`/`refuta`. **Não há como representar `inverte` fielmente no N2 v1.4.** As 30 referências que citei têm múltiplos vínculos, sim — mas nenhuma com `sustenta`+`condicao`, que era o que eu precisava. Confundi "múltiplos vínculos por referência" (que existe) com "par sustenta/refuta condicionado" (que o schema proíbe).

O Estrutura mediu isso (TRILHA93, T4/T5) e eu reproduzi. Ele estava certo; eu não verifiquei fundo o suficiente na rev.1. É o mesmo tipo de erro que venho registrando na série — afirmar "é possível" sem rodar o caso exato.

## 2. O P-K6 é a correção certa

A rev.2 não força `inverte` num molde que o schema recusa. Ela faz o oposto: **declara que `inverte` não materializa em N2 v1.4** (a informação fica no claim, acessível via `claim_id`), converte a representação fiel em pendência de schema **P-K6** (campo `condicao_modificadora` coexistente com `sustenta`/`refuta`, para o ciclo editorial N2 v1.5), e **remove a instrução ativa antiga** da rev.1 — a que eu havia subscrito e que o schema reprova. Confirmei que T11 registra "instrução ativa antiga removida = true".

Isso é fail-closed correto: diante de um caso que o contrato não sabe representar sem perder ciência, o sistema **não materializa e nomeia a pendência**, em vez de materializar errado. É o mesmo princípio da escada degradada da L-06 — quando falta estrutura, declara a lacuna, não completa por inferência.

## 3. A granularidade do Comentador fecha o risco de sobrebloqueio

A ratificação do Comentador acrescenta o que faltava: P-K6 bloqueia **só os claims afetados por `inverte`** — fail-closed por artefato, não bloqueio global do corpus. Um claim sem `inverte` segue os portões normalmente. Confirmei a formulação ("fail-closed por artefato, sem criar bloqueio global maior que a falha real"). É a proporção certa: hoje o único caso identificado é o `.001b`; travar os 22 por causa de um seria punir o corpus pela falha de um artefato.

## 4. O restante da rev.2 preserva a rev.1

- **R-1** (direção por fonte, falha dura, sem default) — intacta, e o destino existe no enum do N2 (conferido).
- **R-2** fonte única de `condicao`, maturidade → `grau_maturidade` — intactas.
- **P-K1** cita `sentido_do_achado` da v3.1. Agora **recebi a v3.1** e confirmei: o campo existe e é declarado OBRIGATÓRIO (`suporta_relacao | refuta_relacao | inconclusivo`). A observação que deixei na rev.1 — "subscrevo a regra, não verifiquei a v3.1" — **fica resolvida**: verifiquei, e o vocabulário que a minuta importa é real.
- **A trava** (P-K1 e P-K2 antes da primeira materialização) permanece, agora somada a P-K6 por artefato.

## 5. Os quatro pontos do meu território

1. **Suficiência** — suficiente; o caso que faltava (inversão) agora tem tratamento honesto (não materializa + pendência nomeada).
2. **Preservação do significado** — preservada: a inversão não é achatada num molde falso; fica no claim até o N2 v1.5 saber representá-la.
3. **Caso não coberto** — nenhum novo encontrado nesta medição.
4. **Fabricação** — impedida nos três eixos: condição (D1), direção (R-1) e agora a não-fabricação de um par inexequível (P-K6).

---

## Subscrição formal

> **Subscrevo, sem ressalva, a minuta rev.2 do contrato de saída do Claim Kit (D1 + R-1 + R-2 + P-K6), mantidas as pendências P-K1..P-K6.**

Registro, como parte da subscrição, a retratação do §1: minha materialização de `inverte` na rev.1 era inexequível no N2 v1.4, o Estrutura mediu corretamente, e a rev.2 a substitui pela solução certa. Pelo rito, D1 encerra com a subscrição sem ressalva do Estrutura (que originou o P-K6) e a verificação mecânica da casa.

---

*Verificações desta rodada: N2 v1.4 rodado com Draft7Validator sobre 4 casos (par sustenta/refuta+condicao REPROVA; condicional+condicao aceita) — reprodução independente da TRILHA93 T4/T5; `sentido_do_achado` OBRIGATÓRIO confirmado na v3.1 recebida; granularidade por artefato confirmada na resposta do Comentador; T11 da trilha (instrução antiga removida). Digitais do pacote declaradas no DIGITAIS.txt; a da minha rev.1 preservada (`40b0205c…`). Não reproduzi as digitais byte a byte — recebi via pacote, marcadas declaradas, exceto o N2 que li no projeto.*
