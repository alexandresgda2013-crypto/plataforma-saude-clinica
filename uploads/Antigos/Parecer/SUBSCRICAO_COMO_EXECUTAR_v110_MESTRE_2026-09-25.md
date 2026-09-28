# SUBSCRIÇÃO TERRITORIAL — COMO EXECUTAR v1.10

**Auditor-Mestre · 2026-09-25**
**Objeto:** minuta `COMO EXECUTAR v1.10` — sha `4951434417f24a329d41fc31f0ec13a5d6da5e1191edde1e72e6cbe2fee4038e` (confere com T1 da TRILHA101)
**Verificado contra:** v1.9 `1cd90b40…` · meu Parecer Territorial de 22/09 (Q1) · Schema-Claim v1.3 rev.3 `28cbc9c7…` (subscrito) · Contrato de Saída rev.2 `841532da…`

---

## RESPOSTA: **SUBSCREVO SEM RESSALVA**

A v1.10 implementa, verbatim, as três correções que pedi na Q1 territorial de 22/09 — e o único risco que eu havia sinalizado ali (a erosão da cegueira por parecer "ineficiente") está escrito como regra no documento. É a rara vez em que um parecer meu retorna inteiro no artefato.

## 1. O protocolo implementa C-1..C-5 e não enfraquece a arbitragem

**A contradição do v1.9 está resolvida.** O v1.9 tinha a IA 3 emitindo parecer **e** fechando o claim no mesmo ato (linha 191 + passo 8) — eu apontei isso como a estrutura que *produzia* a ancoragem que o próprio v1.9 condenava. A v1.10 separa: a IA 3 **emite parecer, não fecha** (linhas 221–222), e o fechamento é **ato conjunto** com retorno às IAs 1 e 2 (passo 7, linha 235; passo 8 do fluxo operacional, linha 517). C-1 cumprido.

**A cegueira está escrita como sequência executável** (linhas 224–235): cada IA analisa sozinha antes de ver as outras; a IA 2 explicitamente **não** é "inspeção sobre a análise da IA 1"; a IA 3 não vê 1 nem 2; a comparação só ocorre no passo 5. Isso é C-2, e é a mudança substantiva — na minha Q1 eu disse que **só a independência cega remove o insumo da ancoragem**, e é ela que está implementada, não apenas a separação parecer/fechamento. O corolário "concordância não é evidência" permanece (linha 246), e agora é **coerente com a estrutura**, porque a convergência não pode mais ser fabricada por leitura em cadeia.

C-3 (retorno + confirmo/altero/mantenho sem apagar as análises originais), C-4 (divergência factual → fonte primária, nunca votação) e C-5 (ressalvas preservadas no fechamento) estão presentes e escritos. A arbitragem pela fonte primária não é enfraquecida — é reforçada, pela mesma razão que dei em 22/09: três leituras que convergem sem se verem são sinal mais forte que três em fila.

## 2. Cegueira destravada na prática

Sim. A sequência das linhas 224–235 é operacional, não conceitual: sete passos numerados, com o ponto de comparação isolado no passo 5 e o fechamento conjunto no 7. O papel de cada IA está fixado (1 busca/triagem, 2 leitura independente, 3 independente + verificação contra fonte), e só o operador roda PubMed. É executável como está.

## 3. As 4 decisões preservam o significado científico

Confirmei a seção de fechamento (linhas 286–300) contra o que subscrevi no Schema-Claim v1.3 rev.3:

- **Direção sem default** — `sentido_do_achado` por fonte, "decidido com leitura da fonte, sem default (R-1)", com a falha dura escrita: ausência = claim não fechado. É a R-1 que eu pedi, e a v1.10 a repete no lugar certo.
- **Ressalva classificada** — `ressalvas[]` com tipo (P-K2/P-K3), a classificação como decisão do fechamento.
- **Moderadores / `inverte`** — `inverte` materializa só no N2 v1.5 (P-K6 travado), coerente com o que subscrevi.
- **"O materializador NÃO decide nenhum dos quatro"** (linha 300) — é o princípio que amarra tudo: a ciência é decidida no fechamento, o materializador copia. C-5 aparece de novo na linha 183 e 268, ligando a preservação da ressalva à heterogeneidade real da literatura.

## 4. A IA 3 não fecha sozinha

Verificado em três lugares independentes do documento: cabeçalho C-1 (linhas 3–4, "a IA 3 não fecha sozinha"), papéis (linha 221–222, "emite parecer, não fecha o claim"), e passo operacional 8 (linha 517, "a IA 3 propõe o preenchimento; IAs 1 e 2 respondem; operador aprova"). Não há caminho no documento em que a IA 3 feche isolada.

## O X-1 — meu aviso virou regra

Na Q1 eu disse: "cegueira aumenta a divergência aparente, e a v1.10 deve dizer que isso é o funcionamento correto, senão a regra será erodida na primeira semana por parecer ineficiente". Está escrito, nas linhas 240–241 e 268: *"Divergência cega entre as três é funcionamento correto, não falha (X-1)… divergência preservada é heterogeneidade real da literatura aparecendo."* É a proteção contra a própria erosão do método, e agradeço que tenha sido incorporada como norma e não como nota.

## Escopo — não ampliado

Confirmei por medição: **zero** menções a alterar N2, redefinir arquitetura ou tocar `schema_vinculo`/`schema_referencia`. A v1.10 não reabre D1, não altera N1/N2 e não amplia o COMO EXECUTAR — as três fronteiras do encaminhamento. E a verificação ao vivo do v1.8 permanece com as cinco condições intactas.

---

## Subscrição formal

> **Subscrevo, sem ressalva, a minuta COMO EXECUTAR v1.10 (C-1..C-5, X-1, protocolo de três IAs cegas com fechamento conjunto), como implementação das correções da rodada territorial de 22/09.**

Uma observação que **não é ressalva**, para o registro: a v1.10 é a norma de *processo* (como o claim é produzido e fechado); ela vale na prática quando o Schema-Claim v1.3 e o Contrato de Saída rev.2 fecharem seus ritos, porque é o fechamento das quatro decisões que a v1.10 pressupõe. Os três documentos são coerentes entre si — verifiquei o Schema-Claim v1.3 rev.3 e o Contrato rev.2 nas rodadas anteriores, e a v1.10 referencia ambos corretamente.

---

*Verificações: sha da minuta conferido contra TRILHA101 T1; contradição parecer/fechamento do v1.9 (linhas 191/passo 8) confirmada resolvida na v1.10 (C-1 em 3 lugares); sequência cega lida (linhas 224–235); 4 decisões do fechamento contra o Schema-Claim v1.3 rev.3; X-1 e C-5 localizados; zero menção a alteração de N1/N2. v1.9 lido no upload; bases referenciadas por digital.*
