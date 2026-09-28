# L-06 — PROTOCOLO DE RESOLUÇÃO DE RELAÇÕES CONCORRENTES
## Minuta 1 · especificação executável da escada D-01

**Auditor-Mestre · 2026-09-15** · Fase 3 da ordem do operador
**Normativa:** Arquitetura V2 (sha `09692e18…`) · L-05 1.1 minuta 2 (D-01, D-02, D-03)
**Acervo de referência:** B1 V7 (sha `6e2c2979…`)

**Invariante que governa todo este documento:**

> O Motor não fabrica precedência científica onde a ciência não estabeleceu precedência.

O L-06 **não** é uma hierarquia entre entidades. É um protocolo que, diante de duas relações aparentemente conflitantes, decide **se há conflito** e, havendo, **se a estrutura de conhecimento permite resolvê-lo**. Quando não permite, o resultado correto é preservar as duas e sinalizar — nunca escolher.

---

# PARTE 1 — O QUE A D-01 NÃO DEFINIU: O GATILHO

A D-01 diz o que fazer quando há conflito. Não diz **como o Motor decide que há um conflito candidato**. Sem isso o protocolo não é executável: ou nunca dispara, ou dispara em tudo.

## 1.1 Definição de par candidato

Duas relações R₁ e R₂ formam **par candidato** quando, e somente quando, satisfazem simultaneamente:

1. **coincidência de extremos** — mesmo par de entidades `(origem, destino)`, em qualquer ordem;
2. **coincidência de objeto** — referem-se ao mesmo desfecho, marcador ou processo;
3. **divergência de sinal ou de natureza** — ao menos uma destas:
   - `sentido_relacao` oposto (aumenta × reduz),
   - `natureza_relacao` incompatível segundo a matriz 1.2,
   - uma afirma a relação e a outra a marca `nao_estabelecida`.

Fora disso **não há par candidato** e o protocolo não dispara. Duas relações que dizem coisas diferentes sobre coisas diferentes não são conflito — são conhecimento.

## 1.2 Matriz de incompatibilidade de `natureza_relacao`

Valores reais do acervo: `causal` (109), `contributiva` (100), `associativa` (56), `nao_estabelecida` (4), `compensatoria` (4), `marcador` (1).

| | causal | contributiva | associativa | compensatoria | marcador | nao_estabelecida |
|---|---|---|---|---|---|---|
| **causal** | — | compatível | compatível | **candidato** | compatível | **candidato** |
| **contributiva** | | — | compatível | **candidato** | compatível | **candidato** |
| **associativa** | | | — | compatível | compatível | **candidato** |
| **compensatoria** | | | | — | compatível | **candidato** |
| **marcador** | | | | | — | compatível |
| **nao_estabelecida** | | | | | | — |

Leitura: uma relação `causal` e uma `associativa` sobre o mesmo par **não conflitam** — diferem em força, e isso é assunto da D-02, não da D-01. Já `compensatoria` contra `causal` no mesmo sentido é candidato real, porque descrevem efeitos líquidos opostos.

**Fronteira explícita com a D-02:** diferença de força, maturidade ou desenho **nunca** cria par candidato. Se o Motor tratasse força divergente como conflito, resolveria por autoridade epistêmica — que é exatamente a precedência fabricada que o invariante proíbe.

---

# PARTE 2 — A ESCADA, DEGRAU A DEGRAU

Ordem fixa. Para no primeiro degrau que resolve. Cada degrau declara o campo que consome e o que acontece se o campo não existir.

| # | Pergunta | Campo consumido | Resolve quando | Saída |
|---|---|---|---|---|
| 1 | Há contradição real? | `natureza_relacao`, `sentido_relacao`, objeto | os predicados não se negam | `sem_conflito` — ambas seguem |
| 2 | Mesmo contexto clínico? | `contexto` | contextos disjuntos | `disjuncao_de_contexto` — ambas seguem, cada uma no seu contexto |
| 3 | Condições de aplicação diferentes? | `condicao` | condições mutuamente exclusivas | `disjuncao_de_condicao` — ambas seguem, condicionadas |
| 4 | Níveis diferentes da cadeia causal? | `nivel_cadeia` ou posição no grafo | níveis distintos | `niveis_distintos` — ambas seguem, encadeadas |
| 5 | Direta × extrapolação? | `direcao` / marcação `[EXTRAPOLADO]` | uma é direta, a outra extrapolada | **não escolhe** — ambas seguem, a extrapolada rotulada |
| 6 | Estabelecida × emergente? | `grau_maturidade` | graus distintos | **não escolhe** — ambas seguem, a emergente rotulada |
| 7 | Coexistem como explicação multifatorial? | estrutura do grafo | ambas contribuem sem se negar | `multifatorial` — ambas seguem, apresentadas juntas |
| — | nenhum resolveu | — | — | `conflito_nao_resolvido` — ambas preservadas + lacuna com os dois IDs |

**Nota de desenho, que quero explícita:** nenhum degrau elimina uma relação. Os degraus 1 a 4 descobrem que o conflito era aparente; os degraus 5 a 7 qualificam relações que coexistem. **A escada nunca produz descarte.** Se alguma implementação futura fizer um degrau descartar, terá violado o invariante, mesmo cumprindo a tabela.

## 2.1 Degraus 5 e 6 não são desempate

Registro porque é o erro mais provável de implementação: "direta × extrapolação" e "estabelecida × emergente" **parecem** critérios de desempate e não são. Eles **rotulam**, não escolhem. A alternativa — preferir a direta sobre a extrapolada — seria razoável cientificamente e ainda assim proibida aqui, porque converteria uma diferença de força numa decisão de exclusão, atravessando a fronteira da Parte 1.2.

---

# PARTE 3 — DEGRAU INDISPONÍVEL: A CLÁUSULA QUE FALTAVA

Esta é a contribuição principal desta minuta, e nasce de um achado do acervo.

Hoje `contexto` **não existe** no dado e `condicao` é esparso. Logo os degraus 2 e 3 não executam. Sem cláusula específica, um conflito de contexto **desce silenciosamente a escada** e sai como `multifatorial` no degrau 7 — isto é, **falta de dado vira afirmação de coexistência**. É a mesma classe de erro da D-03: ausência de recuperação virando afirmação científica.

**Regra.** Quando um degrau não pode executar por ausência do campo:

1. o degrau **não** resolve e **não** é contado como "testado";
2. registra-se `degrau_N_indisponivel` com o nome do campo ausente;
3. o rastro do resultado final carrega a lista de degraus indisponíveis;
4. se o resultado final for `multifatorial` (degrau 7) **e** houver algum degrau indisponível, o resultado é **rebaixado** para `conflito_nao_resolvido` com `motivo = escada_degradada`.

**Justificativa.** `multifatorial` é uma afirmação positiva sobre a biologia: diz que os dois mecanismos operam juntos. Uma escada degradada não tem autoridade para afirmá-la. `conflito_nao_resolvido` é honesto — diz que o sistema não sabe, e nomeia por quê.

**Efeito prático hoje:** enquanto `contexto` e `condicao` não existirem, **o degrau 7 está desabilitado na B1** e todo par candidato não resolvido nos degraus 1, 4, 5 e 6 sai como conflito não resolvido, com a causa nomeada. É mais ruidoso e é correto. O ruído é a medida da dívida de schema, e desaparece quando os campos existirem — sem ninguém tocar no protocolo.

---

# PARTE 4 — DETERMINISMO

1. **Ordem dos pares.** Pares candidatos são processados em ordem lexicográfica de `(id_relacao_menor, id_relacao_maior)`. Nenhuma dependência de ordem de iteração.
2. **Simetria.** O resultado de (R₁, R₂) é idêntico ao de (R₂, R₁). Os degraus 5 e 6, que distinguem papéis, produzem rótulos **atribuídos por relação**, não por posição.
3. **Ordem dos degraus é normativa**, não heurística. Trocar a ordem muda o resultado e exige errata datada.
4. **Idempotência.** Reexecutar o protocolo sobre um resultado já produzido devolve o mesmo resultado.
5. **Sem estado.** A resolução de um par não influencia a de outro par. Proibido propagar decisão entre pares — seria precedência emergente, que é precedência fabricada por outro caminho.

---

# PARTE 5 — VALIDAÇÃO POR TESTE

| Teste | Construção | Critério de aprovação |
|---|---|---|
| T-1 a T-7 | um par sintético desenhado para resolver em cada degrau | o degrau acionado é o esperado; nenhuma relação descartada |
| T-8 | par irresolúvel por construção | `conflito_nao_resolvido` com os dois IDs |
| T-9 **(escada degradada)** | par que resolveria no degrau 2, com `contexto` removido | **não** sai `multifatorial`; sai `conflito_nao_resolvido` + `motivo = escada_degradada` + `degrau_2_indisponivel` |
| T-10 **(não-gatilho)** | duas relações de forças diferentes sobre o mesmo par | protocolo **não dispara** |
| T-11 **(simetria)** | T-1 a T-8 com os argumentos invertidos | resultado idêntico |
| T-12 **(sem descarte)** | toda a suíte | nenhuma execução remove relação do conjunto de saída |
| T-13 **(sem estado)** | mesma suíte em ordens diferentes | resultados idênticos par a par |

T-9, T-10 e T-12 são os testes que protegem o invariante. Os demais protegem a mecânica.

---

# PARTE 6 — DEPENDÊNCIAS, COM O QUE CADA UMA TRAVA

| Dependência | Trava | Estado no acervo |
|---|---|---|
| `contexto` estruturado | degrau 2 e, por consequência, o degrau 7 | **ausente** |
| `condicao` estruturado | degrau 3 | esparso, só dentro de `ancoras[]` |
| `sentido_relacao` | gatilho 1.1(3) e degrau 1 | **não existe como campo** |
| `nivel_cadeia` ou posição no grafo | degrau 4 | depende da Ontologia (Fase 5) |
| `direcao` (nome a decidir — D-L05-NOMES-DIRECAO) | degrau 5 | existe no schema v1.1, ausente no dado |
| `grau_maturidade` | degrau 6 | **274/274 presente** ✔ |
| `natureza_relacao` | gatilho 1.2 | **274/274 presente** ✔ |

**Executável hoje na B1: o gatilho (1.2) e os degraus 1 e 6.** Tudo o mais depende de campos que a Fase 5 precisa criar. Isso não impede fechar o protocolo — impede executá-lo por inteiro, e a Parte 3 garante que a execução parcial seja honesta em vez de otimista.

---

# PARTE 7 — O QUE ESTE PROTOCOLO NÃO FAZ

- Não escolhe entre relações, em nenhum degrau, em nenhuma circunstância.
- Não usa força, desenho ou maturidade como critério de exclusão — só como rótulo.
- Não resolve conflito entre **bibliotecas**; resolve entre **relações**. Duas relações da mesma biblioteca podem ser par candidato.
- Não decide o que aparece no laudo: isso é a D-08.
- Não cria `contexto`, `condicao` nem `sentido_relacao`. Declara que precisa deles.

---

*Risco residual assumido: o gatilho da Parte 1 pode ser estreito demais e deixar passar conflitos reais que não coincidem em extremos — por exemplo, dois caminhos distintos para o mesmo desfecho clínico. Preferi o gatilho estreito porque o largo produziria conflitos falsos em massa e treinaria a equipe a ignorá-los. Recomendo revisitar o gatilho depois do piloto B1, com pares reais em mãos, e registro que esta é a decisão mais provável de precisar de revisão neste documento.*
