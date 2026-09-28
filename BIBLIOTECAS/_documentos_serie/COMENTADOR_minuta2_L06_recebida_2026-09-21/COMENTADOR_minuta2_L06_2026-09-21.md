# COMENTADOR — Minuta 2 da L-06 (recebida via operador em 2026-09-21, rodada 57)
# NOTA DA CASA: o operador identificou a autoria como "comentador"; o documento se assina
# "Auditor-Mestre · 2026-09-21" e fecha com "Status: pronta para auditoria do Auditor-Mestre".
# Anomalia de autoria registrada (ver decisoes rev.64). Verbatim do bloco recebido na ponte:

# L-06 — PROTOCOLO DE RESOLUÇÃO DE RELAÇÕES CONCORRENTES

## Minuta 2 · especificação executável da escada D-01

**Auditor-Mestre · 2026-09-21** · Fase 3 da ordem do operador
**Normativa:** Arquitetura Consolidada da Plataforma V2.3 · L-05 vigente · N1 v1.3 · N2 v1.4 selados
**Acervo de referência:** B1 V7

### Estado desta minuta

Esta Minuta 2 incorpora as correções decorrentes do fechamento de N1 v1.3 e N2 v1.4, especialmente a utilização de `ancoras[].direcao_suporte` no lugar do campo transitório `direcao`.

O L-06 permanece subordinado à Arquitetura Consolidada e aos contratos vigentes. Não cria nova fonte de conhecimento, não altera a hierarquia arquitetural e não estabelece precedência científica onde a estrutura de conhecimento não a estabeleça.

---

# INVARIANTE

> **O Motor não fabrica precedência científica onde a ciência não estabeleceu precedência.**

O L-06 não é uma hierarquia entre entidades, evidências ou relações.

É um protocolo que, diante de duas relações aparentemente conflitantes, determina:

1. se existe efetivamente um conflito;
2. se a estrutura disponível permite caracterizá-lo;
3. se há uma forma estrutural de explicar a aparente incompatibilidade.

Quando a estrutura não permite resolver a relação concorrente, o resultado correto é **preservar ambas e sinalizar a lacuna**.

Nenhum degrau do protocolo autoriza descarte de relação.

---

# PARTE 1 — GATILHO: QUANDO EXISTE UM PAR CANDIDATO

A D-01 define o comportamento diante de relações concorrentes, mas o protocolo precisa estabelecer previamente quando duas relações podem ser submetidas à escada.

## 1.1 Definição de par candidato

Duas relações R₁ e R₂ formam **par candidato** quando, e somente quando, satisfazem simultaneamente:

1. **coincidência de extremos** — mesmo par de entidades `(origem, destino)`, em qualquer ordem;
2. **coincidência de objeto** — referem-se ao mesmo desfecho, marcador ou processo;
3. **divergência de sinal ou de natureza** — ao menos uma destas condições:

   * `sentido_relacao` oposto;
   * `natureza_relacao` incompatível segundo a matriz desta especificação;
   * uma relação afirma a relação e a outra a classifica como `nao_estabelecida`.

Diferenças de força, maturidade ou desenho do estudo **não constituem, por si mesmas, gatilho de conflito**.

Fora dessas condições, não há par candidato e o L-06 não dispara.

---

## 1.2 Matriz de incompatibilidade de `natureza_relacao`

Valores observados no acervo de referência:

* `causal`
* `contributiva`
* `associativa`
* `nao_estabelecida`
* `compensatoria`
* `marcador`

|                      | causal | contributiva | associativa | compensatoria | marcador   | nao_estabelecida |
| -------------------- | ------ | ------------ | ----------- | ------------- | ---------- | ---------------- |
| **causal**           | —      | compatível   | compatível  | candidato     | compatível | candidato        |
| **contributiva**     |        | —            | compatível  | candidato     | compatível | candidato        |
| **associativa**      |        |              | —           | compatível    | compatível | candidato        |
| **compensatoria**    |        |              |             | —             | compatível | candidato        |
| **marcador**         |        |              |             |               | —          | compatível       |
| **nao_estabelecida** |        |              |             |               |            | —                |

A matriz não constitui hierarquia epistemológica.

Exemplo: `causal` × `associativa` não constitui, por si só, conflito. A diferença diz respeito à natureza da relação e não autoriza o Motor a eliminar a relação associativa.

Já `compensatoria` × `causal`, quando aplicadas ao mesmo objeto e nas condições definidas pelo gatilho, constitui par candidato para a escada.

---

## 1.3 Fronteira explícita com a D-02

Diferença de:

* força;
* maturidade;
* desenho de estudo;
* ou qualquer outro atributo de qualificação epistemológica

**não cria, isoladamente, par candidato.**

O L-06 não converte diferença de força ou maturidade em conflito e não utiliza esses atributos para fabricar precedência.

---

# PARTE 2 — A ESCADA D-01

A ordem dos degraus é normativa.

O protocolo interrompe a avaliação quando encontra uma condição que explique a aparente incompatibilidade sem exigir descarte de nenhuma relação.

| # | Pergunta                                 | Campo/estrutura consumida                              | Resolve quando                             | Saída                                                                 |
| - | ---------------------------------------- | ------------------------------------------------------ | ------------------------------------------ | --------------------------------------------------------------------- |
| 1 | Há contradição real?                     | `natureza_relacao`, sinal/objeto da relação            | os predicados não se negam                 | `sem_conflito` — ambas seguem                                         |
| 2 | Mesmo contexto clínico?                  | `contexto`                                             | contextos disjuntos                        | `disjuncao_de_contexto` — ambas seguem no respectivo contexto         |
| 3 | Condições de aplicação diferentes?       | `condicao`                                             | condições mutuamente exclusivas            | `disjuncao_de_condicao` — ambas seguem condicionadas                  |
| 4 | Níveis diferentes da cadeia causal?      | `nivel_cadeia` ou posição equivalente no grafo         | níveis distintos                           | `niveis_distintos` — ambas seguem encadeadas                          |
| 5 | Direta × extrapolação?                   | `ancoras[].direcao_suporte` + marcação de extrapolação | uma relação é direta e a outra extrapolada | **não escolhe** — ambas seguem; a extrapolada é rotulada              |
| 6 | Estabelecida × emergente?                | `grau_maturidade`                                      | graus distintos                            | **não escolhe** — ambas seguem; a emergente é rotulada                |
| 7 | Coexistem como explicação multifatorial? | estrutura do grafo                                     | ambas contribuem sem se negar              | `multifatorial` — ambas seguem apresentadas em conjunto               |
| — | nenhum degrau resolve                    | —                                                      | conflito permanece                         | `conflito_nao_resolvido` — ambas preservadas + lacuna com os dois IDs |

### Regra fundamental

Nenhum degrau elimina uma relação.

Os degraus 1–4 identificam situações em que o conflito era aparente.

Os degraus 5–7 qualificam relações que podem coexistir.

A escada nunca produz descarte.

Se uma implementação futura eliminar uma relação em qualquer degrau, a implementação estará em desacordo com este protocolo, ainda que os demais critérios sejam satisfeitos.

---

# PARTE 3 — DEGRAUS 5 E 6 NÃO SÃO DESEMPATE

`ancoras[].direcao_suporte` e `grau_maturidade` não constituem critérios autônomos de precedência.

No degrau 5, a distinção entre relação direta e extrapolada produz **rotulagem**, não eliminação.

No degrau 6, a distinção entre relação estabelecida e emergente produz **rotulagem**, não eliminação.

Em particular:

> `direcao_suporte` não deve ser interpretada isoladamente como decisão de prevalência.

A leitura do suporte deve permanecer vinculada ao registro de evidência aprovado e aos demais elementos necessários à caracterização da relação.

A L-06 não transforma a direção de suporte em ranking.

---

# PARTE 4 — DEGRAU INDISPONÍVEL E ESCADA DEGRADADA

A ausência de um campo necessário para executar determinado degrau não pode ser convertida em uma afirmação positiva sobre a biologia.

Quando um degrau não pode executar por ausência do campo ou estrutura necessária:

1. o degrau **não resolve**;
2. o degrau **não é contabilizado como testado**;
3. registra-se `degrau_N_indisponivel`;
4. registra-se o campo ou estrutura ausente;
5. o rastro do resultado final carrega a lista de degraus indisponíveis.

### Regra especial para `multifatorial`

Se:

* o resultado somente poderia ser obtido no degrau 7; e
* existir pelo menos um degrau anterior indisponível;

o resultado **não poderá ser `multifatorial`**.

Nesse caso, o resultado será:

`conflito_nao_resolvido`

com:

`motivo = escada_degradada`

e identificação dos degraus indisponíveis.

### Justificativa

`multifatorial` é uma afirmação positiva de coexistência biológica.

Uma escada degradada não possui autoridade estrutural para fazer essa afirmação.

`conflito_nao_resolvido` preserva as duas relações e explicita a dívida estrutural responsável pela impossibilidade de resolução.

### Estado operacional na B1

Enquanto `contexto` e `condicao` não estiverem disponíveis de forma estruturada, os respectivos degraus permanecem indisponíveis.

Consequentemente, o degrau 7 não pode ser utilizado para converter uma escada incompleta em uma afirmação de multifatorialidade.

---

# PARTE 5 — REQUISITOS DE CONSUMO

O L-06 deve consumir somente relações e registros aprovados para consumo pelo fluxo vigente.

A existência de um registro no acervo não implica, por si só, autorização para o Motor utilizá-lo como relação resolvível.

Para relações derivadas de evidências, a interpretação deve respeitar os elementos estruturais já definidos nos contratos vigentes, incluindo, quando aplicáveis:

* `trecho_ancora`;
* `natureza_relacao`;
* `forca_causal`;
* `ancoras[].direcao_suporte`;
* `verification_status`.

Nenhum desses campos, isoladamente, cria precedência.

O L-06 não deve consumir campos de transição ou campos explicitamente depreciados pelos contratos vigentes.

---

# PARTE 6 — DETERMINISMO

1. **Ordem dos pares.**
   Pares candidatos são processados em ordem lexicográfica de `(id_relacao_menor, id_relacao_maior)`.

2. **Simetria.**
   O resultado de `(R₁,R₂)` deve ser idêntico ao de `(R₂,R₁)`.

3. **Atribuição por relação.**
   Quando os degraus 5 ou 6 produzirem rótulos, estes serão atribuídos à relação correspondente, nunca à posição ocupada no par.

4. **Ordem dos degraus.**
   A ordem da escada é normativa. Sua alteração exige revisão formal e errata datada.

5. **Idempotência.**
   Reexecutar o protocolo sobre o mesmo conjunto de relações deve produzir o mesmo resultado.

6. **Sem estado entre pares.**
   A resolução de um par não pode alterar a resolução de outro par.

7. **Sem precedência emergente.**
   É proibido propagar uma resolução entre pares para fabricar uma hierarquia que não exista na estrutura de conhecimento.

---

# PARTE 7 — VALIDAÇÃO POR TESTE

| Teste                         | Construção                                              | Critério de aprovação                                                                                       |
| ----------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| T-1 a T-7                     | um par sintético desenhado para cada degrau             | degrau acionado é o esperado; nenhuma relação descartada                                                    |
| T-8                           | par irresolúvel por construção                          | `conflito_nao_resolvido` com os dois IDs                                                                    |
| T-9 — escada degradada        | par que dependeria do degrau 2, com `contexto` removido | não sai `multifatorial`; sai `conflito_nao_resolvido` + `motivo=escada_degradada` + `degrau_2_indisponivel` |
| T-10 — não-gatilho            | duas relações com forças diferentes sobre o mesmo par   | protocolo não dispara                                                                                       |
| T-11 — simetria               | T-1 a T-8 com argumentos invertidos                     | resultado idêntico                                                                                          |
| T-12 — sem descarte           | toda a suíte                                            | nenhuma execução remove relação do conjunto de saída                                                        |
| T-13 — sem estado             | mesma suíte em ordens diferentes                        | resultados idênticos par a par                                                                              |
| T-14 — direção não-precedente | relações com `ancoras[].direcao_suporte` divergente     | divergência não produz descarte nem ranking                                                                 |
| T-15 — gate                   | relação não aprovada para consumo                       | relação não entra na resolução                                                                              |

T-9, T-10, T-12, T-14 e T-15 protegem diretamente as fronteiras de segurança do protocolo.

---

# PARTE 8 — DEPENDÊNCIAS

| Dependência                                    | Trava                            | Estado conhecido                               |
| ---------------------------------------------- | -------------------------------- | ---------------------------------------------- |
| `contexto` estruturado                         | degrau 2 e uso pleno do degrau 7 | ausente                                        |
| `condicao` estruturada                         | degrau 3                         | atualmente esparsa / dependente de `ancoras[]` |
| representação de sentido da relação            | gatilho e degrau 1               | requer mapeamento contratual                   |
| `nivel_cadeia` ou posição equivalente no grafo | degrau 4                         | depende da Ontologia/Grafo                     |
| `ancoras[].direcao_suporte`                    | degrau 5                         | campo vigente do N2 v1.4                       |
| `grau_maturidade`                              | degrau 6                         | presente no acervo de referência               |
| `natureza_relacao`                             | gatilho                          | presente no acervo de referência               |

### Regra de implementação

A ausência de uma dependência não autoriza substituição silenciosa por outro campo semanticamente parecido.

Quando o campo necessário não estiver disponível, aplica-se a regra de **degrau indisponível** da Parte 4.

---

# PARTE 9 — O QUE ESTE PROTOCOLO NÃO FAZ

O L-06:

* não escolhe entre relações;
* não descarta relações;
* não cria hierarquia científica;
* não usa força, desenho ou maturidade como critério de exclusão;
* não transforma `ancoras[].direcao_suporte` em ranking;
* não resolve conflito entre Bibliotecas;
* resolve relações concorrentes submetidas ao protocolo;
* não decide o que aparece no laudo — isso pertence à D-08;
* não cria `contexto`, `condicao`, sentido de relação ou estruturas da Ontologia;
* não realiza nova pesquisa bibliográfica;
* não introduz conhecimento externo;
* não altera a fonte canônica de conhecimento definida pela arquitetura.

---

# PARTE 10 — RISCO RESIDUAL

O gatilho da Parte 1 pode ser estreito demais e deixar passar conflitos reais que não coincidam nos extremos, por exemplo, dois caminhos distintos para o mesmo desfecho clínico.

O gatilho permanece deliberadamente restrito nesta versão para evitar a criação de falsos conflitos em massa.

Esse ponto deve ser reavaliado após o piloto B1 com pares reais.

A eventual ampliação do gatilho deverá ocorrer por revisão formal do L-06, acompanhada de testes correspondentes, e não por comportamento heurístico do Motor.

---

## ESTADO DA MINUTA 2

Esta Minuta 2:

* atualiza a referência normativa para **V2.3**;
* assume **N1 v1.3 e N2 v1.4 como selados**;
* corrige o campo do degrau 5 para **`ancoras[].direcao_suporte`**;
* preserva a regra de não descarte;
* explicita que direção de suporte não constitui precedência;
* exige consumo de registros aprovados;
* preserva a escada degradada;
* não cria nova decisão arquitetural;
* não altera a fonte canônica de conhecimento;
* permanece dependente de campos que ainda não existem ou estão incompletos, sem mascarar essa dependência.

**Status:** pronta para auditoria do Auditor-Mestre.
