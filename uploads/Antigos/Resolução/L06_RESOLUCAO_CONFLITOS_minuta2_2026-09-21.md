# L-06 — PROTOCOLO DE RESOLUÇÃO DE RELAÇÕES CONCORRENTES
## Minuta 2

**Auditor-Mestre · 2026-09-21** · substitui a minuta 1
**Base normativa:** Arquitetura V2.3 `498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73` (vigente desde 2026-09-21)
**Schemas selados:** N1 v1.3 `b06660fd…` · N2 v1.4 `d96ad15b…` — lidos no projeto, digitais ecoadas
**Acervo de medição:** B1 V7 `6e2c2979…` (274 vínculos)

**Invariante, inalterado:**

> O Motor não fabrica precedência científica onde a ciência não estabeleceu precedência.

---

## 0. O QUE MUDA E POR QUÊ

A minuta 1 foi escrita antes dos schemas existirem. Com o N2 v1.4 selado na mão, verifiquei campo a campo o que cada degrau consome — e rodei a matriz de incompatibilidade, pela primeira vez, sobre o acervo real. Três coisas mudaram por medição, e uma delas é retratação minha.

### 0.1 Retratação: o degrau 5 não lê `direcao_suporte`

Na rodada anterior afirmei que *"o degrau 5 precisa ler `ancoras[].direcao_suporte`"*, e a casa replicou e me creditou. **A localização estava certa — o campo vive só em `ancoras[]` — mas a semântica estava errada.** O domínio selado de `direcao_suporte` é:

`{sustenta, refuta, inconclusivo, condicional}`

É a **direção epistêmica do suporte** — se a evidência sustenta ou refuta a afirmação. Não tem relação com "evidência direta × extrapolação", que é a pergunta do degrau 5. A casa verificou onde o campo mora; ninguém verificou o que ele significa, e a afirmação era minha. Corrijo aqui.

O degrau 5 passa a ler `verification_status` (`verificado` × `extrapolado`) e `extrapolacao_por_analogia`. E `direcao_suporte` vai para onde ele de fato serve — o gatilho (§1) e o degrau 3 (§2).

### 0.2 A primeira execução real da matriz: 4 de 4 falsos positivos

Rodei a matriz 1.2 da minuta 1 sobre os 274 vínculos, usando `claim_id` como aproximação de "mesmo par de entidades". **Ela disparou em 4 pares, em 2 claims. Os 4 são falsos positivos.**

| Claim | Par | O que realmente dizem |
|---|---|---|
| BLOCO02.011 | 0035 `causal` × 0036 `compensatoria` | necroptose via **TNFR1**/RIPK1 × efeito protetor via **TNFR2** — receptores diferentes |
| BLOCO02.011 | 0036 `compensatoria` × 0037 `causal` | idem — TNFR2 protetor × redução de TNF por arctigenina |
| BLOCO02.019 | 0052 `compensatoria` × 0261 `contributiva` | IL-10 contrarregulatória × entrega de IL-10 melhora desfecho — **mesma direção** |
| BLOCO02.019 | 0053 `compensatoria` × 0261 `contributiva` | idem |

Duas causas, as duas minhas:

**(a) A célula `compensatoria × {causal, contributiva}` estava errada.** `natureza_relacao` qualifica o **tipo** da relação, não o seu **sinal**. Uma relação compensatória pode apontar na mesma direção líquida de uma contributiva (o caso da IL-10) ou referir-se a outro sub-objeto (TNFR2 × TNFR1). Para chamar oposição é preciso saber o sinal, e o sinal não está em `natureza_relacao`.

**(b) `claim_id` não é aproximação aceitável de "mesmo objeto".** Um único claim do acervo agrupa TNFR1 e TNFR2. A coincidência de objeto exige `ancoras[].id_oficial` e `ancoras[].escopo`.

Na minuta 1 escrevi que o risco mais provável era o gatilho estar **estreito demais**. O dado mostrou o contrário: ele estava **errado numa célula**, e disparava em relações que concordam. É exatamente o alarme falso que treina a equipe a ignorar o portão.

### 0.3 Correções fáticas herdadas

- `condicao` está **ausente** no acervo (0/274), não esparsa — aceita da carta 10.
- `contexto`, `sentido_relacao` e `nivel_cadeia` **não existem** no N2 v1.4.
- `ancoras[]` está **vazio nos 274** vínculos do acervo — a migração para o N2 v1.4 ainda não ocorreu.

---

## 1. O GATILHO — QUANDO HÁ PAR CANDIDATO

Duas relações R₁ e R₂ formam par candidato quando, e somente quando, satisfazem simultaneamente:

1. **mesmo objeto** — coincidência de `ancoras[].id_oficial` **e** de `ancoras[].escopo`;
2. **oposição**, em pelo menos uma destas formas:
   - **oposição epistêmica** — uma âncora `direcao_suporte = sustenta` e a outra `refuta`, sobre o mesmo objeto;
   - **negação de existência** — uma relação afirma e a outra é `natureza_relacao = nao_estabelecida`;
   - **oposição de efeito** — `sentido_relacao` oposto (aumenta × reduz). *Dependente da Ontologia; hoje não executável.*

**Proibido como aproximação:** `claim_id` no lugar de `ancoras[].id_oficial` + `escopo`. A primeira execução mostrou que ele confunde sub-objetos distintos dentro de um mesmo claim.

**Não disparam:** `sustenta × inconclusivo` (incerteza, não contradição), `sustenta × condicional` (vai direto ao degrau 3), e **qualquer diferença de força, maturidade ou desenho** — isso é D-02, e usá-lo aqui seria resolver conflito por autoridade epistêmica.

## 1.2 Matriz de `natureza_relacao`, corrigida

Só existe uma incompatibilidade lógica real entre valores de natureza: **afirmar uma relação e declará-la não estabelecida**.

| | causal | contributiva | associativa | compensatoria | marcador | nao_estabelecida |
|---|---|---|---|---|---|---|
| **causal** | — | compat. | compat. | compat. | compat. | **candidato** |
| **contributiva** | | — | compat. | compat. | compat. | **candidato** |
| **associativa** | | | — | compat. | compat. | **candidato** |
| **compensatoria** | | | | — | compat. | **candidato** |
| **marcador** | | | | | — | **candidato** |
| **nao_estabelecida** | | | | | | — |

Duas mudanças. `compensatoria × {causal, contributiva}` passa a compatível, pelo motivo de §0.2. E `marcador × nao_estabelecida` passa a candidato, por coerência: a minuta 1 o tratava como compatível sem razão declarada, e declarar algo marcador de uma relação não estabelecida é a mesma negação que nas demais linhas. *Esta segunda mudança é por consistência lógica, sem caso no acervo — registro para revisão no piloto.*

Com a matriz corrigida, a mesma execução sobre o acervo dá **0 pares**. Os quatro vínculos `nao_estabelecida` estão isolados: `VINC_B1_0028` é o único em seu claim, e os outros três não têm `claim_id`.

---

## 2. A ESCADA

Ordem fixa. Para no primeiro degrau que resolve. **Nenhum degrau elimina relação.**

| # | Pergunta | Campo no N2 v1.4 | Saída |
|---|---|---|---|
| 1 | Há contradição real? | `ancoras[].direcao_suporte`, `natureza_relacao` | `sem_conflito` — ambas seguem |
| 2 | Mesmo contexto clínico? | `contexto` — **não existe** | indisponível |
| 3 | Condições de aplicação diferentes? | `ancoras[].condicao` (obrigatória quando `direcao_suporte = condicional`) | `disjuncao_de_condicao` — ambas seguem, condicionadas |
| 4 | Níveis diferentes da cadeia causal? | `nivel_cadeia` — **não existe**; depende da Ontologia | indisponível |
| 5 | Direta × extrapolação? | **`verification_status`** (`verificado` × `extrapolado`) · `extrapolacao_por_analogia` | ambas seguem, a extrapolada rotulada |
| 6 | Estabelecida × emergente? | `grau_maturidade` | ambas seguem, a emergente rotulada |
| 7 | Coexistem como explicação multifatorial? | estrutura do grafo | `multifatorial` — **desabilitado enquanto 2 ou 4 estiverem indisponíveis** |
| — | nenhum resolveu | — | `conflito_nao_resolvido` — ambas preservadas + lacuna com os dois IDs |

**Sobre o escopo, para não confundir:** `ancoras[].escopo` existe e é tentador usá-lo no degrau 2. Não serve. O schema o define como *subdivisão interna da entidade* (`BLOCO_XX/sub`), não como contexto clínico do paciente. Usá-lo no degrau 2 seria descobrir "contextos diferentes" onde há apenas blocos diferentes da mesma biblioteca.

**Candidato a proxy do degrau 4, não adotado:** `ancoras[].papel` distingue `sustenta_mecanismo` de `sustenta_biomarcador` de `sustenta_intervencao`, o que se aproxima de "níveis diferentes da cadeia". Mas o schema declara que `papel` expressa a relação temática, **nunca o veredito**. Adotá-lo como nível causal seria atribuir-lhe semântica que ele recusa. Fica como decisão aberta, a revisitar com a Ontologia.

**Degraus 5 e 6 rotulam, não desempatam** — inalterado da minuta 1, e continua sendo o erro mais provável de implementação.

---

## 3. ESCADA DEGRADADA

Inalterada da minuta 1: degrau indisponível não resolve, não conta como testado, é registrado no rastro; `multifatorial` com qualquer degrau indisponível é rebaixado para `conflito_nao_resolvido` com `motivo = escada_degradada`.

**Estendida:** o degrau 7 fica desabilitado se o **2 ou o 4** estiver indisponível (a minuta 1 só previa o 2). Ambos são perguntas que, sem resposta, deixam aberta a hipótese de o conflito ser aparente — e `multifatorial` é afirmação positiva sobre a biologia que uma escada com esses buracos não tem autoridade para fazer.

---

## 4. DETERMINISMO

Inalterado: ordem lexicográfica dos pares, simetria por relação, ordem normativa dos degraus, idempotência, sem propagação entre pares.

---

## 5. EXECUTABILIDADE — SCHEMA × ACERVO

| Peça | No schema N2 v1.4 | No acervo B1 V7 hoje |
|---|---|---|
| Gatilho — mesmo objeto | ✔ `ancoras[].id_oficial` + `escopo` | ✘ `ancoras[]` 0/274 |
| Gatilho — oposição epistêmica | ✔ `direcao_suporte` sustenta × refuta | ✘ 0/274 |
| Gatilho — negação de existência | ✔ | ✔ `natureza_relacao` 274/274 |
| Gatilho — oposição de efeito | ✘ Ontologia | ✘ |
| Degrau 1 | ✔ | parcial (natureza sim, direção não) |
| Degrau 2 | ✘ | ✘ |
| Degrau 3 | ✔ | ✘ |
| Degrau 4 | ✘ | ✘ |
| **Degrau 5** | ✔ | **✔ `verification_status` 274/274 · `extrapolacao_por_analogia` 274/274** |
| Degrau 6 | ✔ | ✔ `grau_maturidade` 274/274 |
| Degrau 7 | — | desabilitado (2 e 4 indisponíveis) |

**Leitura honesta:** o protocolo está **completo no schema**, exceto degraus 2 e 4 e a oposição de efeito, que dependem de campos que o N2 não tem e que só a Ontologia trará. **No acervo, o gatilho não é executável** — não há como determinar "mesmo objeto" sem `ancoras[]`. O que já funciona hoje, com dado real, são os degraus 5 e 6 — e o 5 ficou melhor do que a minuta 1 previa, de "meia perna" para pleno, justamente por ter saído do campo errado.

**A L-06 só roda sobre a B1 depois da migração dos vínculos para o N2 v1.4.** A casa mediu 243 dos 274 como migráveis por máquina na trilha 27.

---

## 6. TESTES

| Teste | Construção | Critério |
|---|---|---|
| T-1 a T-7 | par sintético por degrau | degrau correto; nenhuma relação descartada |
| T-8 | par irresolúvel | `conflito_nao_resolvido` com os dois IDs |
| T-9 | escada degradada (degrau 2 ausente) | não sai `multifatorial`; sai `escada_degradada` |
| T-10 | forças diferentes, mesmo objeto | gatilho **não dispara** |
| T-11 | argumentos invertidos | resultado idêntico |
| T-12 | toda a suíte | nenhuma relação removida |
| T-13 | ordens diferentes | resultados idênticos par a par |
| **T-14 (novo)** | **os 4 pares reais de §0.2** | **gatilho não dispara em nenhum** |
| **T-15 (novo)** | `claim_id` igual, `ancoras[].escopo` diferente | gatilho **não dispara** — proxy proibido |
| **T-16 (novo)** | `sustenta × inconclusivo`, mesmo objeto | gatilho **não dispara** |

**T-14 é o teste mais valioso desta minuta**, porque não é sintético. São quatro pares do acervo que a matriz antiga acusava e que a biologia diz que concordam. Se uma versão futura do protocolo voltar a dispará-los, a regressão fica visível na primeira execução.

---

## 7. O QUE ESTE PROTOCOLO NÃO FAZ

Inalterado: não escolhe entre relações; não usa força, desenho ou maturidade como critério de exclusão; resolve conflito entre **relações**, não entre bibliotecas; não decide o que aparece no laudo (D-08); não cria os campos que declara precisar.

---

## 8. DEPENDÊNCIAS

| Dependência | Trava | Onde se resolve |
|---|---|---|
| Migração dos vínculos para N2 v1.4 (`ancoras[]`) | gatilho inteiro, degraus 1 e 3 | casa · 243/274 migráveis |
| `contexto` clínico | degrau 2 → degrau 7 | schema futuro |
| `nivel_cadeia` / posição no grafo | degrau 4 → degrau 7 | Ontologia |
| `sentido_relacao` | oposição de efeito no gatilho | Ontologia |
| Decisão sobre `papel` como proxy do degrau 4 | — | aberta |

---

*Medições desta rodada: campos e enums lidos em `schema_vinculo_v1_4.json` (`d96ad15b…`); `ancoras[]`, `verification_status`, `extrapolacao_por_analogia` e `grau_maturidade` contados nos 274 vínculos da B1 V7; matriz antiga e corrigida executadas sobre o acervo com proxy declarado (`claim_id`), os 4 disparos lidos âncora a âncora. Camada declarada: `json.load` sobre os arquivos, igualdade exata de valor de enum.*
