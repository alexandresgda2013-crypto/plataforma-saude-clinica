# COMENTADOR — Minuta 2 CANÔNICA da L-06 (recebida via operador em 2026-09-21, rodada 63)
# NOTA DA CASA: verbatim do bloco colado na ponte. É o artefato que a dívida D-TEXTO-M pedia.
# Verbatim:

# L-06 — PROTOCOLO DE RESOLUÇÃO DE RELAÇÕES CONCORRENTES

**Comentador · 2026-09-21**

**Fase 3 da ordem de desenvolvimento**

**Para auditoria do Auditor-Mestre**

**Normativa:** Arquitetura Consolidada da Plataforma V2.3 · L-05 vigente · N1 v1.3 · N2 v1.4 selados

---

## 0. OBJETO E ESTADO DA MINUTA

Esta Minuta 2 atualiza a L-06 para o estado vigente dos contratos estruturais do pacote V2.3.

A L-06 é a especificação operacional da **D-01 — Relações concorrentes**.

Seu objetivo é definir como o Motor identifica, testa e trata relações potencialmente concorrentes sem fabricar precedência científica.

A atualização principal desta minuta é a adaptação aos schemas vigentes, especialmente ao campo:

`ancoras[].direcao_suporte`

A presente minuta **não altera a arquitetura**, não redefine a D-01, não cria hierarquia científica entre entidades e não autoriza descarte de relações.

### Invariante central

> **O Motor não fabrica precedência científica onde a ciência não estabeleceu precedência.**

Quando a estrutura disponível não permitir resolver uma concorrência, o sistema deve preservar as relações envolvidas e explicitar a lacuna.

---

# PARTE 1 — GATILHO DE RELAÇÕES CONCORRENTES

## 1.1 Critério de formação do par

Duas relações entram no espaço de resolução quando:

- possuem o mesmo par `(origem, destino)`, em qualquer ordem;
- referem-se ao mesmo objeto relacional;
- apresentam divergência de sinal, natureza ou interpretação relacional;
- ou uma delas apresenta `natureza_relacao = nao_estabelecida`.

A simples diferença de força, maturidade ou desenho do estudo **não constitui, por si só, conflito**.

Essas diferenças alimentam a qualificação epistemológica da relação, mas não autorizam a classificação automática como concorrência.

## 1.2 Matriz de natureza relacional

A avaliação considera, quando disponíveis, as seguintes naturezas:

| NaturezaSignificado operacional |                                                                       |
| ------------------------------- | --------------------------------------------------------------------- |
| `causal`                        | relação causal explicitamente estabelecida                            |
| `contributiva`                  | contribuição para o fenômeno sem equivalência a causalidade exclusiva |
| `associativa`                   | associação observada sem implicação causal suficiente                 |
| `nao_estabelecida`              | ausência de relação estabelecida                                      |
| `compensatoria`                 | relação interpretada como compensação/modulação de outra condição     |
| `marcador`                      | relação de marcação, indicação ou proxy sem equivalência causal       |

A natureza relacional não é convertida automaticamente em hierarquia de autoridade.

---

# PARTE 2 — ESCADA FIXA DE RESOLUÇÃO

A resolução obedece a uma ordem normativa única.

Nenhum degrau pode ser pulado para produzir uma solução mais conveniente.

## Degrau 1 — Existe contradição real?

Verificar se as relações afirmam efetivamente proposições incompatíveis.

Diferença de formulação, força, desenho, população ou nível de análise não constitui contradição por si só.

Se não houver contradição real, não existe conflito a resolver.

## Degrau 2 — Mesmo contexto clínico?

Verificar se as relações estão descrevendo o mesmo contexto clínico.

Ausência de `contexto` estruturado impede uma resolução afirmativa neste degrau.

Nesse caso:

`degrau_2_indisponivel`

Não é permitido inferir equivalência de contexto por ausência do campo.

## Degrau 3 — Condições de aplicação diferentes?

Verificar se as relações divergentes dependem de condições diferentes de aplicação.

A análise utiliza `condicao` quando disponível.

Quando o campo for inexistente ou insuficiente:

`degrau_3_indisponivel`

Também aqui, não é permitido completar a condição por inferência silenciosa.

## Degrau 4 — Níveis diferentes da cadeia causal?

Verificar se as duas relações se encontram em níveis diferentes da cadeia causal.

Diferença de nível pode eliminar a aparência de contradição sem estabelecer precedência geral entre as relações.

## Degrau 5 — Relação direta versus extrapolação

Verificar se uma relação possui suporte direto e outra decorre de extrapolação.

Quando houver indicação correspondente na estrutura de evidência, considerar também o rastro de extrapolação.

A distinção direta/extrapolada deve ser registrada sem transformar extrapolação em inexistência da relação.

## Degrau 6 — Estabelecida versus emergente

Verificar o grau de maturidade epistemológica da relação.

`grau_maturidade` pode distinguir relações estabelecidas de relações emergentes.

Esse campo serve à caracterização epistemológica e **não autoriza, isoladamente, eliminar a relação concorrente**.

## Degrau 7 — Coexistência multifatorial

Quando as diferenças anteriores não eliminarem a concorrência aparente e houver estrutura suficiente para sustentar coexistência, reconhecer a possibilidade de múltiplos fatores atuarem simultaneamente.

A coexistência multifatorial não pode ser usada como saída automática para qualquer conflito.

Se os degraus anteriores necessários não estiverem disponíveis, aplica-se a regra da escada degradada.

## Resultado residual

Se nenhuma etapa resolver legitimamente a concorrência:

```text
lacuna_tipo = conflito_nao_resolvido

```

As duas relações permanecem preservadas, com suas respectivas origens e qualificações.

**O Motor não escolhe uma delas.**

---

# PARTE 3 — ESCADA DEGRADADA

A ausência de campos estruturais não pode produzir uma falsa aparência de resolução.

Quando um degrau depender de informação ausente ou insuficiente:

```text
degrau_N_indisponivel

```

A escada continua apenas até onde houver informação legítima.

### Regra crítica

Se a conclusão depender de um degrau posterior, mas algum degrau anterior obrigatório estiver indisponível, não se pode atribuir ao resultado posterior a mesma força que teria sob informação completa.

Em particular:

> Se o resultado pretendido seria `coexistencia_multifatorial`, mas algum degrau anterior necessário não pôde ser executado por ausência estrutural, o resultado deve ser rebaixado para:

```text
conflito_nao_resolvido

```

com:

```text
motivo = escada_degradada

```

Assim, ausência de estrutura gera **incerteza explícita**, nunca preenchimento implícito.

---

# PARTE 4 — PAPEL DE `ancoras[].direcao_suporte`

O campo vigente do N2 é:

```text
ancoras[].direcao_suporte

```

Ele substitui a referência anterior a um campo genérico `direcao` utilizado nas versões preliminares.

Seu conteúdo pode ser utilizado como elemento de interpretação do suporte da evidência à relação.

Entretanto:

> `direcao_suporte` não é critério autônomo de precedência.

Ele não pode, isoladamente:

- transformar uma relação em dominante;
- eliminar uma relação concorrente;
- gerar uma ordem de autoridade;
- substituir natureza relacional;
- substituir força causal;
- substituir maturidade epistemológica;
- produzir uma decisão clínica.

A interpretação deve permanecer vinculada ao conjunto estrutural aprovado.

---

# PARTE 5 — REQUISITOS DE CONSUMO

A L-06 deve consumir somente relações e registros disponibilizados pelo fluxo vigente de evidência e estrutura.

Para relações derivadas de evidência, devem ser respeitados, quando presentes:

- `trecho_ancora`;
- `natureza_relacao`;
- `forca_causal`;
- `ancoras[].direcao_suporte`;
- `grau_maturidade`;
- `verification_status`;
- demais campos normativos pertinentes do N1/N2 vigentes.

Campos depreciados ou pertencentes a versões de transição não podem ser reintroduzidos como se fossem vigentes.

A L-06 não cria campos ausentes.

Se uma representação necessária não existir, isso constitui dependência estrutural a ser resolvida no nível apropriado.

---

# PARTE 6 — DETERMINISMO

A resolução deve ser determinística.

## 6.1 Ordem dos pares

Quando houver múltiplas relações concorrentes, o conjunto de pares é normalizado em ordem lexicográfica determinística.

## 6.2 Simetria

A inversão da ordem de apresentação das duas relações não pode produzir resultado diferente.

Se:

```text
A × B

```

e

```text
B × A

```

representam o mesmo par lógico, ambos devem produzir a mesma classificação.

## 6.3 Ordem normativa dos testes

Os degraus são sempre avaliados nesta sequência:

1. contradição real;
2. mesmo contexto;
3. condições de aplicação;
4. nível da cadeia causal;
5. direta × extrapolação;
6. estabelecida × emergente;
7. coexistência multifatorial.

Nenhum algoritmo local pode alterar essa ordem.

## 6.4 Idempotência

Executar a resolução duas vezes sobre o mesmo estado deve produzir o mesmo resultado.

Não pode existir memória oculta de pares anteriores influenciando pares posteriores.

Cada resolução deve ser independente das anteriores.

---

# PARTE 7 — TESTES NORMATIVOS

| TesteRequisito |                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------ |
| T-1            | contradição real detectada corretamente                                                    |
| T-2            | diferença sem conflito não dispara resolução                                               |
| T-3            | contexto suficiente resolve corretamente quando aplicável                                  |
| T-4            | contexto ausente gera `degrau_2_indisponivel`                                              |
| T-5            | condição suficiente permite avaliação do degrau 3                                          |
| T-6            | condição insuficiente gera `degrau_3_indisponivel`                                         |
| T-7            | nível causal corretamente identificado                                                     |
| T-8            | direta × extrapolação corretamente diferenciada                                            |
| T-9            | maturidade corretamente considerada sem criar precedência                                  |
| T-10           | coexistência multifatorial somente quando legitimamente suportada                          |
| T-11           | conflito não resolvido preserva ambas as relações                                          |
| T-12           | inversão A/B produz resultado idêntico                                                     |
| T-13           | não existe estado residual entre pares                                                     |
| T-14           | `ancoras[].direcao_suporte` não funciona como critério autônomo de precedência             |
| T-15           | relações fora do estado de aprovação/validação não entram silenciosamente no processamento |

### Teste de não descarte

Em nenhum teste de resolução uma relação pode ser eliminada apenas porque a outra apresenta maior força, maior maturidade ou maior autoridade aparente.

A saída deve preservar o rastro das relações envolvidas.

---

# PARTE 8 — DEPENDÊNCIAS E ESTADO ATUAL

A implementação completa de todos os degraus depende da disponibilidade dos campos correspondentes.

Estado conhecido:

| ElementoSituação            |                                                |
| --------------------------- | ---------------------------------------------- |
| `natureza_relacao`          | disponível                                     |
| `grau_maturidade`           | disponível                                     |
| `condicao`                  | estrutura insuficiente/esparsa                 |
| `contexto`                  | não disponível de forma estruturada            |
| `sentido_relacao`           | não estabelecido como campo vigente            |
| `ancoras[].direcao_suporte` | campo vigente do N2 v1.4                       |
| nível da cadeia causal      | dependente da ontologia e estrutura relacional |

Assim, a L-06 permanece executável somente nos degraus para os quais existe suporte estrutural correspondente.

Não se deve tratar a ausência de suporte estrutural como falha científica da relação.

---

# PARTE 9 — LIMITES DO CONTRATO

A L-06:

- não estabelece hierarquia entre entidades;
- não define qual mecanismo é cientificamente superior;
- não produz decisão clínica;
- não altera a fonte canônica de conhecimento;
- não cria evidência;
- não realiza pesquisa bibliográfica independente;
- não incorpora conhecimento externo;
- não altera schemas;
- não cria campos ausentes;
- não transforma diferenças epistemológicas em precedência científica;
- não redefine D-02.

A D-02 permanece uma decisão independente referente ao teto epistemológico por eixo na combinação.

---

# PARTE 10 — PRINCÍPIO DE FECHO

Quando o Motor encontrar duas relações concorrentes e a estrutura disponível não permitir resolver legitimamente a diferença:

> **preservar as duas, registrar a lacuna e não escolher.**

Quando a estrutura permitir resolução:

> **resolver somente pelo primeiro degrau normativo que efetivamente discrimine o caso.**

Quando a estrutura necessária estiver ausente:

> **declarar a indisponibilidade e degradar o resultado, nunca completar por inferência.**

---

## RISCO RESIDUAL

O principal risco residual continua sendo a possibilidade de uma classificação multifatorial absorver um conflito que, com contexto ou condição mais bem estruturados, poderia ser discriminado anteriormente.

Esse risco é reconhecido como consequência da cobertura estrutural atual e não deve ser mascarado pela lógica do contrato.

---

## STATUS

**Minuta 2 — preparada pelo Comentador para auditoria independente do Auditor-Mestre.**

A próxima etapa metodológica é a elaboração da versão do **Auditor-Mestre sem utilizar esta minuta como resposta pré-formatada**, seguida de cruzamento sistemático entre as duas versões.
