# L-06 — PROTOCOLO DE RESOLUÇÃO DE RELAÇÕES CONCORRENTES
## Minuta 3 · consolidada · rev.1

*rev.1 (2026-09-21): altera apenas a seção de proveniência, após o operador confirmar o texto enviado à Arena. Conteúdo normativo idêntico ao da minuta 3 original (`a6a0027c…`).*

**Auditor-Mestre · 2026-09-21** · consolida a minuta 2 do Auditor-Mestre e a minuta 2 do Comentador
**Base normativa:** Arquitetura V2.3 `498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73`
**Schemas selados:** N1 v1.3 `b06660fd…` · N2 v1.4 `d96ad15b…`
**Acervo de medição:** vínculos B1 V7 `490675e63122a24baebd8890f4a7883a07f68916d90562e74adf309133501d1b` (274)

---

## PROVENIÊNCIA DAS ENTRADAS — LER ANTES DO RESTO

| Entrada | Forma recebida | Digital |
|---|---|---|
| Minuta 2 do Auditor-Mestre | arquivo | `eb54337c7f17c20fbd0ad1b926fd0d575b33462141537e837c4aff9fa13bbd13` · confere com a medição da casa |
| Minuta 2 do Comentador | **texto colado no chat pelo operador** | **nenhuma** — não recebi arquivo; não posso ecoar a sha `1a51d9b9…` que a casa mediu |
| Cruzamento da casa | arquivo | `560537f6…` · confere |

**Achado de proveniência.** O texto do Comentador que recebi **não corresponde, em vários pontos, ao texto que a casa cruzou.** Li o cruzamento contra o texto recebido, item a item:

| O cruzamento atribui ao Comentador | No texto que recebi |
|---|---|
| B1 — degrau 5 lê `ancoras[].direcao_suporte` | o degrau 5 **não nomeia campo algum** |
| B2 — matriz com célula `compensatoria × {causal, contributiva} = candidato` | **não há matriz de incompatibilidade**; o §1.2 é uma tabela de significados |
| Parte 1.3 — fronteira L-06 × D-02 em seção própria | não há Parte 1.3; D-02 aparece numa linha da Parte 9 |
| Parte 3 — "degraus 5/6 não são desempate", frase "direção de suporte não vira ranking" | a Parte 3 é a escada degradada; a frase não ocorre |
| Parte 4 — contrato do rastro enumerado (campo ausente, lista de degraus) | a Parte 4 é sobre `direcao_suporte`; o rastro é só `degrau_N_indisponivel` |
| Determinismo 6.3/6.7 — "atribuição por relação, nunca por posição" | 6.3 é a ordem dos degraus; não há 6.7; a frase não ocorre |
| Parte 8 — regra de não substituir por campo "parecido" | a Parte 8 é a tabela de dependências |
| Parte 10 — risco do gatilho estreito, revisão pós-piloto | a Parte 10 é o princípio de fecho; o risco residual trata de outra coisa |
| Saídas `disjuncao_de_contexto`, `niveis_distintos` | não ocorrem — **essas saídas são da minha minuta 1** |

**Causa identificada (rev.1).** O operador confirmou que o texto que recebi é **exatamente** o enviado à Arena — pela leitura, é idêntico palavra a palavra ao que consolidei. Isso exclui a hipótese de outra versão. Testei a segunda:

> **Os nove elementos listados acima estão todos na minha minuta 1 da L-06** (`3b6a15a0b311a7b73f8793e1187a353df92201a11d7746e9082d18c4f6c38595`, arquivada pela própria casa em 15/09): a célula `compensatoria × causal = candidato`, o degrau 5 lendo `direcao`, a fronteira com a D-02, a seção "degraus 5 e 6 não são desempate", a atribuição por relação, o risco do gatilho estreito, o rastro com o campo ausente e as saídas `disjuncao_de_contexto` e `niveis_distintos`.

O cruzamento misturou a minuta 2 do Comentador com a minha minuta 1. Dois indícios de que houve reconstrução, e não leitura: a forma `ancoras[].direcao_suporte` no degrau 5 **não ocorre em nenhum dos dois textos** — é composição da troca de nome anunciada pelo Comentador (Parte 4) com o degrau 5 da minha minuta 1 —; e as numerações citadas (Parte 1.3, 6.7) **não existem em nenhum dos dois**.

**Mecanismo provável, a confirmar pela casa:** o operador informa que a cópia enviada à Arena trazia **"Auditor-Mestre" no cabeçalho de autoria**. Um texto chamado "L-06 minuta" assinado pelo Auditor-Mestre é facilmente lido junto com a minuta 1 que o Auditor-Mestre de fato escreveu. É o que a casa registrou como "anomalia de assinatura" — e é provavelmente a origem da mistura.

**Consequência para os créditos:** a minuta 3 já creditava ao Comentador apenas o que está no texto dele, e adotava os demais elementos "sob autoria própria quando já estavam nas minhas minutas". A medição confirma que essa separação estava certa. **O conteúdo desta minuta não muda.**

É o episódio da V2.2 em outra peça: um cabeçalho errado bastou para dois documentos se fundirem na leitura de terceiro.

---

## 0. INVARIANTE E FECHO

> **O Motor não fabrica precedência científica onde a ciência não estabeleceu precedência.**

Frase idêntica nas duas minutas de origem, escritas independentemente.

Quando a estrutura disponível não permitir resolver uma concorrência, o sistema **preserva as relações envolvidas e explicita a lacuna**. *(Comentador, §0.)*

---

## 1. O GATILHO

### 1.1 Quando há par candidato

Duas relações R₁ e R₂ formam par candidato quando, e somente quando:

1. **referem-se ao mesmo objeto** — na camada conceitual, mesmo par de extremos e mesmo objeto relacional (desfecho, marcador ou processo); na camada operacional, coincidência de `ancoras[].id_oficial` e de `ancoras[].escopo` (§7 declara a perda entre as duas camadas);
2. **e apresentam oposição**, em uma destas formas:
   - **epistêmica** — `ancoras[].direcao_suporte = sustenta` × `refuta`, sobre o mesmo objeto;
   - **negação de existência** — uma afirma a relação, a outra é `natureza_relacao = nao_estabelecida`;
   - **de efeito** — `sentido_relacao` oposto. *Depende da Ontologia; não executável.*

**Não disparam:** diferença de força, maturidade, desenho ou população *(Comentador, degrau 1)*; `sustenta × inconclusivo`; `sustenta × condicional` (vai ao degrau 3); **e diferença de natureza relacional por si só.**

**Proibido:** `claim_id` como aproximação de "mesmo objeto".

### 1.2 Por que "divergência de natureza" não é gatilho — medido

O §1.1 do texto do Comentador lista como gatilho *"divergência de sinal, natureza ou interpretação relacional"*. Executei essa regra sobre os 274 vínculos, com o mesmo proxy de `claim_id` que usei para medir a minha matriz antiga:

| Regra de gatilho | Pares no acervo | Claims afetados |
|---|---|---|
| "divergência de natureza" (Comentador §1.1) | **244** | 41 |
| matriz antiga do Mestre (célula `compensatoria`) | 4 | 2 |
| **matriz corrigida desta minuta** | **0** | 0 |

Os 244 decompõem-se em `causal × contributiva` (113), `associativa × contributiva` (96), `associativa × causal` (31) e os mesmos 4 da minha célula errada. **Nenhuma dessas combinações é contradição**: uma relação causal e uma contributiva sobre o mesmo processo dizem coisas compatíveis em forças diferentes — assunto da D-02.

`natureza_relacao` qualifica o **tipo** da relação, não o seu **sinal**. A única incompatibilidade real entre valores de natureza é afirmar a relação e declará-la não estabelecida. "Interpretação relacional" não é campo nem critério definido e sai do gatilho.

### 1.3 Matriz de natureza relacional

| | causal | contributiva | associativa | compensatoria | marcador | nao_estabelecida |
|---|---|---|---|---|---|---|
| **causal** | — | compat. | compat. | compat. | compat. | **candidato** |
| **contributiva** | | — | compat. | compat. | compat. | **candidato** |
| **associativa** | | | — | compat. | compat. | **candidato** |
| **compensatoria** | | | | — | compat. | **candidato** |
| **marcador** | | | | | — | **candidato** |

`marcador × nao_estabelecida` como candidato é mudança por coerência lógica, sem caso no acervo — a revisar no piloto (E2).

Significado operacional de cada natureza, conforme a tabela do Comentador (§1.2): `causal` — relação causal explicitamente estabelecida; `contributiva` — contribuição sem equivalência a causalidade exclusiva; `associativa` — associação sem implicação causal suficiente; `nao_estabelecida` — ausência de relação estabelecida; `compensatoria` — compensação ou modulação de outra condição; `marcador` — marcação ou proxy sem equivalência causal. **A natureza não é convertida em hierarquia de autoridade.**

---

## 2. A ESCADA

Ordem normativa única. Nenhum degrau pode ser pulado para produzir solução mais conveniente *(Comentador)*. **Nenhum degrau elimina relação.**

| # | Pergunta | Campo (N2 v1.4) | Saída |
|---|---|---|---|
| 1 | Há contradição real? | `ancoras[].direcao_suporte`, `natureza_relacao` | `sem_conflito` |
| 2 | Mesmo contexto clínico? | `contexto` — **inexistente** | `degrau_2_indisponivel` |
| 3 | Condições de aplicação diferentes? | `ancoras[].condicao` | `disjuncao_de_condicao` ou `degrau_3_indisponivel` |
| 4 | Níveis diferentes da cadeia causal? | `nivel_cadeia` — **inexistente** | `degrau_4_indisponivel` |
| 5 | Direta × extrapolação? | `verification_status`, `extrapolacao_por_analogia` | `rotulo_extrapolacao` — ambas seguem |
| 6 | Estabelecida × emergente? | `grau_maturidade` | `rotulo_emergente` — ambas seguem |
| 7 | Coexistência multifatorial? | estrutura do grafo | `multifatorial` — só se 1 a 4 estiverem disponíveis |
| — | nada resolve | — | `conflito_nao_resolvido` + lacuna com os dois IDs |

**Salvaguardas por degrau** — todas do texto do Comentador, adotadas:

- **1** — diferença de formulação, força, desenho, população ou nível de análise não é contradição por si só.
- **2** — *não é permitido inferir equivalência de contexto pela ausência do campo.* E, do lado do Mestre: `ancoras[].escopo` **não é contexto clínico** — é subdivisão da entidade.
- **3** — *não é permitido completar a condição por inferência silenciosa.*
- **5** — a distinção é registrada *sem transformar extrapolação em inexistência da relação.*
- **6** — maturidade *não autoriza, isoladamente, eliminar a relação concorrente.*
- **7** — multifatorial *não pode ser usado como saída automática para qualquer conflito.*

**Degraus 5 e 6 rotulam, não desempatam.** Preferir a direta sobre a extrapolada seria cientificamente razoável e continua proibido, porque converteria diferença de força em exclusão.

**Degrau 4 — `papel` não é adotado como proxy.** O schema declara que `ancoras[].papel` expressa a relação temática, *nunca o veredito*. Decisão aberta, a revisitar com a Ontologia (E3).

---

## 3. ESCADA DEGRADADA

Degrau indisponível não resolve, não conta como testado e é registrado no rastro como `degrau_N_indisponivel`, com o nome do campo ausente.

> **O degrau 7 é barrado se qualquer degrau resolutivo — 1, 2, 3 ou 4 — estiver indisponível.** Nesse caso, o que seria `multifatorial` sai como `conflito_nao_resolvido` com `motivo = escada_degradada`.
>
> **A indisponibilidade dos degraus 5 ou 6 não barra o 7**, porque eles só rotulam: sua ausência não deixa aberta a hipótese de o conflito ser aparente.

Esta regra resolve a divergência F2 entre as versões de origem. A do Mestre barrava só 2 ou 4 (restrita demais — B5); a do Comentador barrava *"algum degrau anterior necessário"* sem definir quais são necessários. "Necessário" passa a significar **resolutivo**.

*Ausência de estrutura gera incerteza explícita, nunca preenchimento implícito.* (Comentador)

---

## 4. `ancoras[].direcao_suporte`

Campo do N2 v1.4, domínio `{sustenta, refuta, inconclusivo, condicional}`. Substitui a referência preliminar a um campo genérico `direcao`.

**Onde é usado:** no gatilho (`sustenta × refuta` é oposição epistêmica), no degrau 1, e no degrau 3 (`condicional` exige `ancoras[].condicao`).

**Onde não é usado:** no degrau 5. É a direção epistêmica do suporte, não a distinção direta × extrapolação — retratação do Mestre registrada na minuta 2.

**O que ele não pode fazer, isoladamente** *(Comentador, Parte 4, adotada integralmente)*: tornar uma relação dominante; eliminar uma concorrente; gerar ordem de autoridade; substituir natureza relacional, força causal ou maturidade; produzir decisão clínica.

---

## 5. REQUISITOS DE CONSUMO

*(Comentador, Parte 5, adotada.)* A L-06 consome apenas relações e registros disponibilizados pelo fluxo vigente de evidência e estrutura. Campos depreciados ou de versões de transição **não podem ser reintroduzidos como vigentes**. A L-06 não cria campos ausentes: representação inexistente é dependência estrutural, a resolver no nível apropriado.

**Gate de consumo:** relações fora do estado de aprovação ou validação não entram silenciosamente no processamento. **Pendência E1:** falta definir quem declara uma relação "aprovada para consumo" e por qual campo — sem isso o teste correspondente (T-18) não tem oráculo.

---

## 6. DETERMINISMO

1. Pares em ordem lexicográfica determinística.
2. **Simetria:** A × B e B × A produzem o mesmo resultado.
3. **Atribuição por relação, nunca por posição:** rótulos dos degraus 5 e 6 pertencem à relação, não à ordem em que o par foi apresentado. *(Minuta 1 do Mestre, §4.)*
4. Ordem normativa dos degraus; nenhum algoritmo local a altera.
5. **Idempotência sem memória oculta:** executar duas vezes produz o mesmo resultado; nenhum par influencia outro. *(Comentador, 6.4.)*
6. Sem precedência emergente: proibido propagar decisão entre pares.

---

## 7. GRANULARIDADE DO OBJETO — A PERDA ENTRE AS DUAS CAMADAS

A ponte entre o "mesmo objeto" conceitual e o operacional **não existe sem perda**.

O schema define `escopo` como subdivisão da entidade por bloco ou sub-bloco. No caso TNFR1 × TNFR2, os três vínculos estão no mesmo claim (BLOCO02.011), e nenhum dos dois receptores tem ID oficial. **Nenhum campo do N2 v1.4 separa os dois.** O objeto conceitual é mais fino do que o schema consegue expressar.

Consequência: na granularidade do schema, "mesmo objeto" **super-associa**, e quem filtra é a condição de oposição. Se duas relações sobre sub-objetos distintos carregarem `sustenta × refuta`, o gatilho dispara, a escada encontra 2, 3 e 4 indisponíveis, e o resultado é `conflito_nao_resolvido` com `escada_degradada`. **É a falha segura** — o protocolo diz "não sei", nunca afirma nem descarta — mas é um conflito falso apresentado ao profissional.

**Correção registrada:** os 4 falsos positivos da matriz antiga são eliminados **pela correção da matriz**, não pela definição operacional de objeto. A minuta 2 do Mestre e o cruzamento da casa creditavam indevidamente essa definição.

**Dívida: D-L05-GRANULARIDADE-OBJETO** — falta granularidade de sub-objeto abaixo do claim, a resolver no N2 ou na Ontologia.

---

## 8. EXECUTABILIDADE — SCHEMA × ACERVO

| Peça | Schema N2 v1.4 | Acervo B1 V7 |
|---|---|---|
| Gatilho — mesmo objeto | ✔ (com a perda do §7) | ✘ `ancoras[]` 0/274 |
| Gatilho — oposição epistêmica | ✔ | ✘ |
| Gatilho — negação de existência | ✔ | ✔ `natureza_relacao` 274/274 |
| Gatilho — oposição de efeito | ✘ | ✘ |
| Degrau 1 | ✔ | parcial |
| Degrau 2 | ✘ | ✘ |
| Degrau 3 | ✔ | ✘ `condicao` ausente (0/274) |
| Degrau 4 | ✘ | ✘ |
| Degrau 5 | ✔ | ✔ 274/274 |
| Degrau 6 | ✔ | ✔ 274/274 |
| Degrau 7 | — | barrado (1–4 indisponíveis) |

`condicao` está **ausente**, não "insuficiente/esparsa" como diz a Parte 8 do texto do Comentador — é a mesma correção que a casa aplicou à minuta 1 do Mestre (`RESPOSTA_10_L06_MINUTA1_E_P8_HARMONIZADO_2026-09-15.md`, §2, tabela da Parte 6).

**A L-06 só roda sobre a B1 depois da migração dos vínculos para o N2 v1.4** (243 de 274 migráveis por máquina, trilha 27 da casa). *A ausência de suporte estrutural não é falha científica da relação* (Comentador, Parte 8).

---

## 9. TESTES — LISTA UNIFICADA

As duas minutas de origem numeravam de T-1 a T-15 com **conteúdos diferentes para o mesmo número** — a colisão F1 era mais ampla do que os T-14/T-15 apontados. A consolidada adota numeração nova, com correspondência:

| ID | Critério | Origem |
|---|---|---|
| T-01 | degrau 1 resolve: sem contradição real → `sem_conflito` | M T-1 · C T-1 |
| T-02 | força, maturidade, desenho ou população diferentes não disparam | M T-10 · C T-2 |
| T-03 | degrau 2 resolve por contexto — **bloqueado**: campo inexistente | M T-2 · C T-3 |
| T-04 | contexto ausente → `degrau_2_indisponivel` | C T-4 |
| T-05 | degrau 3 resolve por `ancoras[].condicao` | M T-3 · C T-5 |
| T-06 | condição ausente → `degrau_3_indisponivel` | C T-6 |
| T-07 | degrau 4 resolve por nível — **bloqueado**: campo inexistente | M T-4 · C T-7 |
| T-08 | degrau 5 rotula extrapolação, não descarta | M T-5 · C T-8 |
| T-09 | degrau 6 rotula maturidade, sem precedência | M T-6 · C T-9 |
| T-10 | `multifatorial` só com 1–4 disponíveis | M T-7 · C T-10 |
| T-11 | irresolvível → `conflito_nao_resolvido`, ambas preservadas | M T-8 · C T-11 |
| T-12 | escada degradada: 2 ausente → não sai `multifatorial` | M T-9 |
| T-13 | 5 ou 6 ausentes **não** barram o 7 | novo — B5 refinado |
| T-14 | simetria A×B = B×A | M T-11 · C T-12 |
| T-15 | nenhuma relação removida, nem por maior autoridade aparente | M T-12 · C "não descarte" |
| T-16 | sem estado entre pares | M T-13 · C T-13 |
| T-17 | `direcao_suporte` não é critério autônomo de precedência | C T-14 |
| T-18 | gate de consumo — **oráculo pendente (E1)** | C T-15 |
| T-19 | **os 4 pares reais da matriz antiga não disparam** | M T-14 (novo) |
| T-20 | `claim_id` igual e `escopo` diferente → não dispara | M T-15 (novo) |
| T-21 | `sustenta × inconclusivo` → não dispara | M T-16 (novo) |
| T-22 | mesmo `escopo`, sub-objetos distintos, `sustenta × refuta` → `conflito_nao_resolvido` + `escada_degradada` | novo — §7 |
| T-23 | **os 244 pares por "divergência de natureza" não disparam** | novo — §1.2 |

T-19 e T-23 são os de maior valor: não são sintéticos. São pares do acervo que regras de gatilho anteriores acusavam e que a biologia diz serem compatíveis. Uma regressão futura aparece na primeira execução.

T-03 e T-07 existem nas duas minutas de origem e nenhuma das duas tinha como executá-los. Ficam na lista como bloqueados, e não como aprovados por omissão.

---

## 10. LIMITES

A L-06 não estabelece hierarquia entre entidades; não define mecanismo cientificamente superior; não produz decisão clínica nem decide o que aparece no laudo (D-08); não altera a fonte canônica de conhecimento; não cria evidência nem faz pesquisa bibliográfica; não incorpora conhecimento externo; não altera schemas nem cria campos; não transforma diferença epistemológica em precedência; **não redefine a D-02** — a resolução de concorrência não é autoridade epistemológica, e o teto por eixo segue decisão independente.

---

## 11. DEPENDÊNCIAS

| Dependência | Trava |
|---|---|
| Migração dos vínculos para N2 v1.4 | gatilho inteiro, degraus 1 e 3 |
| `contexto` clínico | degrau 2 → degrau 7 |
| `nivel_cadeia` | degrau 4 → degrau 7 |
| `sentido_relacao` | oposição de efeito |
| Granularidade de sub-objeto (D-L05-GRANULARIDADE-OBJETO) | falsos conflitos do §7 |
| Oráculo do gate de consumo (E1) | T-18 |

---

## 12. RISCOS RESIDUAIS

1. **Multifatorial absorvendo conflito discriminável** *(Comentador)* — mitigado pela regra do §3, que barra o 7 enquanto 1–4 estiverem indisponíveis.
2. **O gatilho** — o risco previsto na minuta 1 era estar estreito demais; o dado mostrou duas regras largas demais (4 e 244 falsos positivos). A matriz corrigida dá zero. Ampliação futura só por revisão formal, com testes, depois do piloto.
3. **Granularidade** — conflitos falsos entre sub-objetos do mesmo claim (§7). Falha segura, declarada.

---

## 13. PRINCÍPIO DE FECHO

*(Comentador, Parte 10, verbatim.)*

> Quando a estrutura disponível não permitir resolver legitimamente a diferença: **preservar as duas, registrar a lacuna e não escolher.**
>
> Quando a estrutura permitir resolução: **resolver somente pelo primeiro degrau normativo que efetivamente discrimine o caso.**
>
> Quando a estrutura necessária estiver ausente: **declarar a indisponibilidade e degradar o resultado, nunca completar por inferência.**

---

## CRÉDITOS

**Do Comentador, verificado no texto recebido:** salvaguardas por degrau (§2), frase de fecho da escada degradada (§3), limites de `direcao_suporte` (§4), requisitos de consumo e gate (§5), idempotência sem memória oculta (§6.5), "ausência de suporte não é falha científica" (§8), T-14/T-15 de origem, risco residual 1, princípio de fecho.

**Do Mestre:** matriz corrigida e sua execução (4→0), proibição do proxy, gatilho em três formas de oposição, campo correto do degrau 5, alerta sobre `escopo` e `papel`, mapa de executabilidade, perda de granularidade (§7), T-19 a T-22.

**Desta consolidação:** regra do §3 por degraus resolutivos, medição do gatilho do Comentador (244→0), T-13 e T-23, lista de testes unificada.

**Da casa:** as correções B3, B5, B6, B7 e o levantamento F1–F5.

---

*Rito: esta minuta segue para réplica da casa e, depois, aprovação do operador. Medições desta rodada: gatilho "divergência de natureza" executado sobre os 274 vínculos com proxy `claim_id` declarado (244 pares, 41 claims); comparação item a item do texto recebido do Comentador com o cruzamento `560537f6…`. O texto do Comentador foi lido como recebido no chat — sem arquivo e sem digital verificável.*
