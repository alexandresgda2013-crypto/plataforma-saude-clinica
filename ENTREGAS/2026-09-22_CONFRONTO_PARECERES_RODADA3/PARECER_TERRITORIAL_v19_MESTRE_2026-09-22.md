# PARECER TERRITORIAL DO AUDITOR-MESTRE — COMO EXECUTAR v1.9
## Sobre o protocolo de validação, a bifurcação e a governança de auditoria

**Auditor-Mestre · 2026-09-22** · parecer, não aprovação
**Ancorado em:** COMO EXECUTAR v1.9 `1cd90b407facee81692d668919829c9d6d5a149b1309424c6f012e26cd81f586` (byte-idêntico ao que medi em 20/09) · L-06 rev.6 vigente `98e90bdc…` · Arquitetura V2.3 `498e7df9…` · minha Deliberação de 18/09 `fe5a18b3…` (declarada pela casa)

**Anti-contaminação:** não vi o encaminhamento ao Auditor-Estrutura. Este parecer é escrito só do meu território.

---

## Q1 — "G3 é parecer, não fechamento"

### O que medi no v1.9, antes de opinar

O texto confirma o diagnóstico da casa. Nos papéis (linhas 185–191): **IA 3 "emite parecer e redige o claim no schema"** — as duas coisas na mesma mão. No passo 8 (linha 462): **"Fecha o claim preenchendo Schema-Claim completo"** — o fechamento é ato da IA 3, sem retorno às IAs 1 e 2. A correção do consolidado B ("G3 é parecer, não fechamento") de fato **não está** no v1.9.

E há uma contradição interna, que é o ponto mais forte a favor da correção: o próprio v1.9 declara, na linha 201, o **corolário anti-ancoragem** — "o risco específico deste arranjo é ancoragem, assinar embaixo de uma extração plausível". Mas o desenho que ele especifica **produz** esse risco: a IA 2 inspeciona "sobre a análise da IA 1" (linha 189), e a IA 3 vê as duas análises antes de emitir a sua. Cada camada lê a anterior. O documento nomeia o risco e mantém a estrutura que o gera.

### (a) Endosso a formulação como correção da v1.10?

**Sim, com uma distinção que preciso marcar.** A proposta do Comentador faz **duas** coisas, e elas têm pesos epistemológicos diferentes:

1. **Separar parecer de fechamento** — a IA 3 emite parecer, o fechamento exige confirmação conjunta das IAs 1 e 2. Isso **corrige** a contradição interna: tira da IA 3 a autoridade de fechar sozinha o que ela mesma redigiu.

2. **Análise cega independente** — as três analisam o mesmo corpus sem ver o trabalho uma da outra, e só comparam depois. Isso vai **além** do consolidado B, como a casa mediu (9× "independent" na carta, 0× no consolidado).

Endosso as duas, mas **a nº 2 é a que de fato mata a ancoragem, não a nº 1.** Separar parecer de fechamento redistribui a autoridade; não impede que a IA 3 ancore, porque ela continua vendo as análises anteriores antes de escrever a sua. Só a independência cega remove o insumo que produz a ancoragem. Se for para escolher uma, a nº 2 é a substantiva.

### (b) A independência cega preserva o princípio de arbitragem?

**Preserva, e o reforça.** O princípio (linha 195) é: a fonte primária é o árbitro, concordância entre IAs não é evidência. A independência cega é a única estrutura **coerente** com esse princípio. No desenho atual há uma incoerência silenciosa: o texto diz "concordância não é evidência", mas o fluxo sequencial faz a concordância emergir por construção — a IA 3 que lê duas análises alinhadas tende a produzir a terceira alinhada, e três análises alinhadas *parecem* corroboração ainda que o texto negue que sejam. A independência cega quebra essa aparência: três análises que convergem **sem se verem** são um sinal mais forte que três que convergem em fila, porque a convergência não pôde ser fabricada por leitura mútua.

**Um risco que não vejo mencionado e que a v1.10 deve declarar:** independência cega **aumsenta a taxa de divergência aparente**. Três leituras cegas do mesmo artigo vão discordar mais que três leituras em cadeia — e isso é bom, porque grande parte dessa divergência é a heterogeneidade real da fonte aparecendo. Mas o protocolo precisa estar preparado para processar mais divergência, não menos. Se o custo de resolver divergência for alto, haverá pressão para afrouxar a cegueira. A v1.10 deve dizer explicitamente que **divergência cega é o funcionamento correto, não uma falha do método** — senão a regra será erodida pela primeira semana de uso.

### (c) O que se perde ao abandonar a "inspeção sobre a análise anterior"?

Perde-se uma coisa real, e é honesto nomeá-la: **eficiência de detecção de erro grosseiro.** No desenho sequencial, se a IA 1 comete um erro óbvio, a IA 2 o pega imediatamente, porque está olhando para ele. Na cegueira, o erro da IA 1 só aparece na fase de comparação, depois das três análises prontas — mais tarde e com mais trabalho.

É uma perda aceitável, por uma razão: **o erro que a inspeção sequencial pega bem é o erro grosseiro, e esse é o menos perigoso** — números que não batem saltam à vista de qualquer revisor. O erro perigoso é o **plausível**: a extração que parece certa e não é, exatamente o que a ancoragem faz passar. A cegueira troca eficiência contra o erro fácil por proteção contra o erro difícil. É a troca certa para uma base científica canônica.

### (d) A acrescentar

**Um ponto de fronteira com a L-06.** O protocolo de três IAs resolve divergência entre **análises da mesma evidência**; a L-06 resolve divergência entre **relações no grafo**. São coisas diferentes e não devem usar o mesmo vocabulário. A "divergência factual → fonte primária" do v1.9 e a "divergência de medição → comando/escopo/camada" da R-BUSCA-1 são dois dos quatro tipos que discutimos; a v1.10 ganharia em precisão listando os quatro e dizendo qual instância resolve cada um — para o Comentador, casa e eu não reabrirmos a mesma taxonomia a cada peça.

---

## Q2 — A bifurcação (P2)

### (a) Confirmo e formalizo o parecer de 18/09 como resposta a P2

Mantenho **(i), com a bifurcação desenhada**: a afirmação do claim clínico vai à Biblioteca da entidade correspondente pelo rito normal (§5.5 da arquitetura); a evidência segue N1→N2 para rastreabilidade. Isso preserva a fonte única de conhecimento (§6 dever 1), não altera contrato nenhum, e resolve a insatisfazibilidade da NT-02 para claims clínicos. A medida do problema permanece: 39 dos 49 PMIDs do kit fora da V7, wiring claim→biblioteca zero.

### (b) Os eixos 4 e 6, que a Deliberação não cobriu

**Eixo 4 — coerência com "o sistema não transforma validação em evidência".** Aqui a bifurcação não é só compatível; ela é **necessária** para esse princípio. Se o claim clínico fosse direto para conhecimento sem passar pela Biblioteca, o *ato de ter sido validado* — o carimbo "aprovado em G3" — viraria, na prática, o passaporte da afirmação para o laudo. Isso é transformar validação em evidência: a afirmação valeria porque foi aprovada, não porque a Biblioteca a sustenta. A bifurcação impede isso ao exigir que a afirmação **entre na Biblioteca pelo mesmo rito de qualquer conhecimento** — o carimbo de validação fica na trilha de evidência (N1/N2), separado da via de conhecimento. Validação sustenta rastreabilidade; nunca é a razão pela qual algo é verdadeiro.

**Eixo 6 — a bifurcação altera o significado epistemológico do claim?** **Não altera, e é esse o ponto dela.** Um claim clínico afirma uma coisa (ex.: "citocina X elevada associa-se a depressão") com uma força (associação humana observacional). Se a afirmação entra na Biblioteca pelo rito e a evidência entra em N1/N2, o significado e a força são **preservados intactos** — a NT depois lê o significado da Biblioteca e a força dos eixos do vínculo, cada um da sua fonte. O risco de alteração de significado surge na hipótese **oposta** — (ii), claim como segunda fonte de conhecimento —, onde a afirmação entraria por uma porta que não é a da Biblioteca, com regras próprias, e poderia carregar consigo a força inflada pela aprovação. A bifurcação é a opção que **não** mexe no significado; a alternativa é que mexeria.

### (c) Por que a bifurcação é epistemologicamente necessária

Reduzo à frase mais curta que consigo defender: **conhecimento e evidência são coisas de tipos diferentes, e um sistema que não os separa deixa a evidência decidir o que é verdadeiro pela via errada.** A Biblioteca responde "o que sabemos e com que força"; a evidência responde "o que sustenta e é rastreável até onde". Se um claim entra pelos dois papéis ao mesmo tempo — afirmando conhecimento e trazendo sua própria evidência sem separá-los —, a fronteira entre "isto é sustentado" e "isto é verdadeiro" se apaga, e é nessa fronteira apagada que a força se infla. A bifurcação não é uma conveniência de engenharia; é a forma de manter os dois tipos em canais distintos. É a mesma disciplina que a não-elevação da D-02 impõe dentro do motor, aplicada uma camada antes, na entrada.

---

## Q3 — Quem audita os N1/N2 (P4)

**Proposta:** a produção dos N1/N2 a partir do claim clínico e a auditoria desses N1/N2 ficam em mãos separadas, e a auditoria é **adversarial de fidelidade**, não só de conformidade.

**Fundamento:** toda esta mesa funcionou por uma razão única — quem produz não é quem verifica. A casa mede a mim, eu meço a casa, e cada erro desta série (o "0×" da busca acentuada, meus três hashes sem comando, o "não há dois textos" da rev.3) foi pego pelo outro lado, nunca por quem o cometeu. Se a mesma mão que deriva o N1/N2 também atesta sua fidelidade ao claim, essa estrutura de detecção desaparece exatamente para o artefato mais novo e menos testado do pipeline.

**Território responsável:** a **conformidade de schema** (campos obrigatórios, enums, cardinalidade) é território do Auditor-Estrutura — é o que ele já faz com N1/N2. Mas a **fidelidade claim→N1→N2** — o N1 representa o artigo que o claim citou? o N2 preserva a força e a direção que o claim afirmou? — é território epistemológico, e não deve ficar com quem produziu nem só com quem checa schema. Duas leituras possíveis, e declaro minha preferência:

- **Opção A:** o Auditor-Estrutura assume o papel adversarial completo, como sugeri no §4 da Deliberação — schema **e** fidelidade. Vantagem: um só auditor. Risco: fidelidade claim→evidência é julgamento científico, e o território do Estrutura é estrutural; ele pode não ter o mandato para dizer "este N2 inflou a força do claim".
- **Opção B:** conformidade com o Estrutura, fidelidade comigo (ou com quem exerça o papel científico-adversarial). Vantagem: cada verificação na competência certa. Custo: dois auditores no caminho.

**Recomendo a Opção B**, com uma ressalva de honestidade: ela me coloca a auditar um artefato derivado de um claim que eu ajudei a definir o contrato. Isso é aceitável enquanto **eu não produzir o N1/N2** — auditar contra um contrato que ajudei a escrever é diferente de auditar o que eu mesmo gerei. Se algum dia a coordenação da produção dos N1/N2 recair sobre mim (como a proposta de fluxo chegou a sugerir), então a fidelidade tem de ir para outra mão, e a Opção B se inverte. **A regra invariante, acima das opções: a fidelidade de um N1/N2 nunca é atestada por quem o produziu.**

**Conflito de função a registrar:** o rito supremo do operador (os três sem ressalva) já é, ele mesmo, uma segregação de funções — nenhum artefato passa sem três olhos independentes. A governança dos N1/N2 deve herdar esse rito, não criar um paralelo mais frouxo. Se um N1/N2 pode ser aprovado por menos que os três, ele terá um padrão de prova inferior ao da L-06 — e seria estranho o dado científico ter barra mais baixa que o contrato que o processa.

---

## Fronteiras deste parecer

Não opino sobre P3 (destino da ressalva) nem sobre a parte estrutural de P2/P4 — território do Auditor-Estrutura, que não li. Sobre o piloto às cegas de B1.SM02.014 (P7): o desenho "mesmo corpus, mesma questão, três análises independentes, comparação depois" é o correto, e é a aplicação prática da minha resposta à Q1(b) — mas o desenho detalhado depende de registro do operador, e fica como adendo se solicitado.

Nenhuma destas respostas é aprovação do v1.9. São parecer territorial, sujeitos ao rito dos três sem ressalva e à palavra final do operador.

---

*Verificações desta rodada: papéis e passo 8 do v1.9 lidos nas linhas 185–201 e 458–466; corolário anti-ancoragem confirmado na linha 201; ausência da correção P1 confirmada no texto. Digitais das peças citadas pela casa não verificadas — recebidas como referência, marcadas "declaradas".*
