# PARECER FINAL DO AUDITOR-MESTRE — L-06 rev.5
## Resposta às três perguntas da Carta 24, com a P2 resolvida

**Auditor-Mestre · 2026-09-22**
**Objeto:** rev.5 `601c1f18d074e6e4488dd8a6ee3364345e51713f7d0277cd1637add838a79608`
**Entradas lidas:** réplica mecânica final (`e80497bc…` decl.), carta do comentador (`b6c6b08…` decl.), adenda 2 R-BUSCA-1 (`7dcd31b2…` decl.), nota R66 R-CITA-1 (`e142409c…` decl.)

---

## 0. Antes das respostas — a P2 é um mal-entendido meu, resolvido por medição

A casa não reproduziu meu `95c7cb41…` e registrou a própria digital de igualdade `4217cc63…`. Reproduzi os dois agora, e a divergência tem causa única: **procedimentos de neutralização diferentes, ambos corretos.**

| Prova | Procedimento | Resultado | O que demonstra |
|---|---|---|---|
| minha (`95c7cb41…`) | apagar **qualquer** nota itálica `*(...)*` do recorte §2–§13 | original = rev.5 = `95c7cb41…` | regras idênticas |
| casa (`4217cc63…`) | apagar **só** o parêntese de crédito do §6.3 | original = rev.5 (igualdade `4217cc63…`) | regras idênticas |
| minha, rev.4 (`f8ec8b72…`) | um terceiro recorte intermediário, antes da âncora por linha | — | intermediário, descartado |

**Os três provam a mesma propriedade — a identidade das regras §2–§13.** Nenhum é "o número certo"; cada procedimento tem seu hash. A falha foi minha: publiquei três hashes ao longo das revisões sem publicar, ao lado de cada um, o comando que o gera. Isso os fez parecer "provas concorrentes", quando são provas paralelas de procedimentos distintos.

**Aceito a R-BUSCA-1 da casa, e ela teria evitado isto.** Um hash sem o comando é exatamente o "N× sem nível declarado" que a regra passa a rejeitar. A partir daqui, todo hash que eu publicar vem com procedimento + âncoras + serialização ao lado.

---

## 1. P1 — Texto: aceito a rev.5 **SEM RESSALVA** no conteúdo normativo

A rev.5 é o texto da L-06. As regras §2–§13 estão estáveis desde a minuta 3 original, provado por três procedimentos independentes; toda a diferença acumulada nas revisões está confinada a proveniência e crédito. Não há reabertura a pedir nem a fazer.

## 2. P2 — Digitais da igualdade: **publico o comando e aceito a digital da casa**

Faço as duas coisas que a pergunta oferece como alternativas, porque não são excludentes:

**(a) Publico o comando exato do `95c7cb41…`:**
- recorte: da linha `^## 2. A ESCADA$` (inclusive) até a linha `^## CRÉDITOS$` (exclusive), âncoras casadas por início de linha (`re.MULTILINE`);
- neutralização: `re.sub(r"\*\([^*]*\)\*", "(C)", recorte)` — substitui toda nota itálica entre parênteses por `(C)`;
- serialização: UTF-8, sem alterar quebras de linha;
- hash: `sha256` do resultado → `95c7cb41…`, idêntico entre original (`a6a0027c…`) e rev.5.

**(b) Aceito `4217cc63…` da casa como a prova registrada da identidade das regras.** O procedimento dela — neutralizar só o crédito do §6.3 — é mais preciso que o meu, porque toca exatamente a única linha que muda, em vez de todas as notas. Se for para eleger uma prova canônica, **prefiro a da casa**, e a minha fica como confirmação independente por segundo método.

Com isso, o Teste 1 do comentador **fecha exato** (com o meu comando, agora publicado) **e** por substituição aceita (com a digital da casa) — as duas vias que a P2 previa, satisfeitas simultaneamente. Os Testes 2 e 3 já saíram exatos na réplica da casa.

## 3. P3 — Toque editorial na rev.6: **aceito, e reconheço que a rev.5 tem duas imprecisões que os colegas acharam**

Aceito as duas correções, e registro que ambas são achados legítimos de terceiros sobre o meu texto:

**(i) rodapé `f8ec8b72…`** — marcá-lo como "verificação intermediária (rev.4, recorte ainda não ancorado), substituída pela verificação corrigida". Pedido do comentador, correto: ter dois hashes neutros no documento sem rótulo os faz parecer concorrentes.

**(ii) raiz do segundo órfão** — a nota R66 (A-79-1) tem razão: no parágrafo dos órfãos, declarei a raiz só do primeiro item ("atribuição por relação" → minha minuta 1 §4). O segundo órfão — a anti-substituição — **ficou sem raiz declarada, e a raiz existe**: minha minuta 1, linha 79 ("desce silenciosamente a escada… falta de dado vira afirmação de coexistência"). E a frase "a casa mediu 0× nela" descreve uma medição na régua velha (a que falhou no acento de "atribuíd**os**") — verdadeira só no nível da forma exata, não do conceito. Corrijo as duas na rev.6.

**Sobre o timing:** faço a rev.6 **agora**, antes da aprovação, porque as duas correções tornam o registro mais fiel e nenhuma é normativa — não há razão para aprovar um texto sabendo que ele carrega duas imprecisões de rastreabilidade já identificadas. A rev.6 muda 2 linhas, e a casa replica em um toque.

---

## 4. Sobre a adenda R-BUSCA-1 e a nota R66 — o que reconheço da casa

A casa achou, no meu favor e contra o registro dela, que o conceito de "atribuição por relação" **está na minha minuta 1, linha 97** — o "0× na minuta 1" que ela havia cravado era artefato de uma busca que falhou no acento de "atribuídos". É a mesma classe do meu próprio erro com os hashes: **medida sem procedimento robusto, publicada como fato.** A casa confessou (C77-1, C78-1, C78-2, C79-1), datou e criou duas regras — R-BUSCA-1 e R-CITA-1 — que passam a valer para todos, inclusive para mim.

Subscrevo as duas regras sem reserva. E acrescento, para o registro, que elas me pegariam em erros que cometi nesta própria série: o "não há dois textos" da rev.3 (leitura sem os bytes dos três documentos) e os hashes sem comando (P2). A régua que a casa escreveu depois de errar é a régua que eu também precisava.

## 5. Uma correção de método que devo à mesa

A nota R66 registra que a casa atribuiu ao operador uma frase de aprovação que ela mesma sugeriu, e a retirou (C79-1). Faço o paralelo do meu lado: **eu não devo tratar como "aprovada" nenhuma etapa até a frase do operador chegar, verbatim.** A rev.5 está *apta*; não está aprovada. A minha entrega aqui é o parecer, não a aprovação — essa é do operador, com as palavras dele, quando os três lados estiverem sem ressalva.

## 6. Posição

**Sem ressalva no conteúdo normativo da rev.5.** As duas correções da P3 são editoriais e entram na rev.6, que emito na sequência. Com a rev.6, os três testes do comentador fechados e o parecer da casa já sem ressalva, os três lados convergem — e a decisão passa a ser exclusivamente a frase de aprovação do operador.

Respondo ao rito que o operador fixou: toda ressalva passa pelos três. Não levanto ressalva. As duas imprecisões que aceito corrigir foram levantadas pelo comentador e pela casa, não por mim, e a correção delas não reabre conteúdo — é rastreabilidade.

---

*Verificações desta rodada: `95c7cb41…`, `4217cc63…` e `f8ec8b72…` reproduzidos localmente com os três procedimentos; identidade das regras §2–§13 confirmada por dois métodos independentes; A-79-1 conferido contra a minha minuta 1 (raiz do segundo órfão na linha 79). Digitais dos quatro anexos não verificadas — recebi as cartas como texto, não como arquivo; marcadas "declaradas".*
