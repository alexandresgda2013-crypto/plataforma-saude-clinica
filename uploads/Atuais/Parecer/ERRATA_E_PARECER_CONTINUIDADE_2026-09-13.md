# ERRATA DO AUDITOR-MESTRE + PARECER DE CONTINUIDADE

**2026-09-13 · resposta à carta da casa de produção**

---

## 1. ERRATA — as três críticas da casa aos meus scripts estão corretas

Verifiquei as três antes de responder. Errei nas três.

**E-01 · V-14 anunciada e não implementada.** Verdadeiro. A docstring do P-8 listava
"V-14 divergência entre docstring e implementação" e o código não continha uma
única linha dela. É literalmente o defeito F-08 que cobrei do `gate_script.py`, na
minha própria ferramenta, na mesma entrega.
**Corrigido:** V-14 implementada de verdade — compara as regras anunciadas na
docstring com as efetivamente executadas em runtime. Primeira versão ainda estava
errada (acusava V-03, V-07, V-11 e V-12 como inexistentes, quando apenas não tinham
violações a reportar); corrigi para distinguir *regra silenciosa* de *regra ausente*,
com registro explícito de execução. Testada com regra fantasma "V-99" plantada:
detecta e reprova.

**E-02 · Código morto no R-05.** Verdadeiro. O ramo de âncora multi-sentença tinha
`break` na primeira iteração e `alvo = None` incondicional depois — nunca reparou nada.
**Corrigido:** substituído por `fatia_literal()`, que recupera a fatia do texto original
por mapa de posições normalizada→original, com exigência de sítio único.

**E-03 · `corte_literatura` quebraria fora da B1.** Verdadeiro e pior do que a casa
relatou. Medi nas 16:

| Formato | Bibliotecas |
|---|---|
| objeto `{valor, tipo}` | **B01 apenas** |
| string de texto livre | B02–B15 (14) |
| `None` | B16 |

Meu V-07 chamaria `.get("valor")` sobre string → `AttributeError`. **Corrigido:** tolera
os três formatos, extrai a data por regex quando é texto livre, e emite AVISO pedindo
padronização — sem mascarar a divergência de schema, que é uma lacuna nova da série
(**L-17**: o manifesto não tem schema único nem portão que o valide).

**E-04 · Bug que eu mesmo encontrei ao rodar na série.** Em B02 o portão imprimia
`284/0 (100.0% de cobertura)` — denominador zero produzindo cobertura falsamente
perfeita. Exatamente o tipo de métrica mentirosa que estou aqui para caçar.
**Corrigido:** universo = `max(grosseiras, reconhecidas)`.

**E-05 · Os arquivos corrigidos de F-08/F-09 não foram entregues.** Procede. Eu os
corrigi e coloquei na pasta do pacote, mas apresentei apenas 5 arquivos e esses dois
ficaram de fora. Vão anexados agora, para a conferência bilateral que pediram.

---

## 2. RECONCILIAÇÃO 24 × 22 — o número certo é o da casa

Não foi estado intermediário dos arquivos deles. Foi bug meu, e tenho o log.

- **Execução 1 (matcher com defeito): 24 ERRO / 60 AVISO.** V-05 acusava 3 erros:
  `(Perry & Teeling, 2013)`, `(Serhan & Levy, 2018)`, `(Wang & Miller, 2018)` — os três
  **falsos positivos**, porque eu casava o nome completo contra fichas que usam só o
  primeiro sobrenome (`REF_PERRY_2013`).
- Ao mesmo tempo, o fallback por alias **não conferia o ano**, o que fazia
  `(Hafizi, 2007)` casar com `REF_HAFIZI_2005` e **não** ser reportado.
- **Execução 2 (matcher corrigido): 22 ERRO / 60 AVISO.** V-05 passa a 1 erro: Hafizi.

Aritmética: −3 falsos positivos +1 verdadeiro = **−2**. 24 → 22.

> **O 22 da casa está certo e o meu 24 estava errado.** Registro para a errata: o número
> que publiquei no relatório como "linha de base" era o da execução com o matcher
> defeituoso. A linha de base correta é 22.

---

## 3. RESPOSTAS ÀS TRÊS PERGUNTAS

**(a) Log do P-8 ante-reparo — reconciliado acima.** Não precisam procurar divergência
nos arquivos de vocês: não há.

**(b) V-14 — implementar, não retirar.** Já implementada e testada. Retirar da docstring
seria resolver o sintoma; o valor da regra é justamente ser o único mecanismo que
policia o próprio ferramental. Recomendo que ela vire item obrigatório de todo portão
novo do projeto, inclusive dos que vocês escreverem.

**(c) Convenção de ano no ID — concordo com pubdate-ano NLM, com uma ressalva de fundo.**

Concordo com a recomendação de vocês para o caso imediato: `pubdate` NLM é coerente com
`revista_ano`, com a citação PubMed padrão e com o que o revisor humano vai ver na tela.
Adotem, e apliquem o rito da trilha 17.

A ressalva: isto está tratando o sintoma de **L-15**. Enquanto o ID codificar o ano, toda
divergência epub×print vira um rename de 25–43 âncoras. A demonstração de vocês na
trilha 17 — 1 token editado propagando para 25 âncoras — é o argumento mais forte que
existe a favor de IDs opacos, e foi produzida por vocês, contra o próprio conforto.
Mantenho a posição: **IDs opacos para todo ID novo**, sem migração retroativa em massa
(concordo com vocês nesse ponto), e a convenção pubdate-NLM como regra de desempate
enquanto os IDs legados existirem.

Sobre os 3 casos epub×print (`GEBARA_2020`, `SCAINI_2021`, `SCHWEIZERSHUBERT_2021`): a
decisão de **não renomear sem convenção da série** está correta. Não é timidez — é a
diferença entre corrigir um erro e propagar uma preferência por três bibliotecas.

---

## 4. O ACHADO QUE MUDA O PLANEJAMENTO: V-02 É DEFEITO DE SÉRIE

Vocês rodaram o P-8 na B13 e acharam 167 erros V-02. Rodei nas 16. É pior:

| Biblioteca | Vínculos | Âncoras em linha-lote (V-02) | % |
|---|---|---|---|
| B01 | 273 | **5** | 2% |
| B02 | 89 | 3 | 3% |
| B03 | 165 | **165** | **100%** |
| B04 | 131 | **131** | **100%** |
| B05 | 160 | **160** | **100%** |
| B06 | 108 | 68 | 63% |
| B07 | 71 | 2 | 3% |
| B08 | 83 | 0 | 0% |
| B09 | 111 | 35 | 32% |
| B10 | 137 | 39 | 28% |
| B11 | 96 | 40 | 42% |
| B12 | 111 | 35 | 32% |
| B13 | 207 | **167** | 81% |
| B14 | 290 | **240** | 83% |
| B15 | 173 | **134** | 77% |
| B16 | 290 | **290** | **100%** |
| **Série** | **2.495** | **≈1.514** | **61%** |

Quatro bibliotecas com **100%** dos vínculos ancorados em rodapé bibliográfico. Na média
da série, **61% das referências não estão ligadas a nenhuma afirmação científica** — estão
ligadas a uma lista de nomes.

E há mais, que vocês ainda não reportaram porque só rodaram V-02 na B13: a **B02 tem 126
fichas órfãs** (V-04) e **7 citações de prosa sem ficha** (V-05). A B01 tem 0 e 1. A B01 é
a única que passou por um ciclo de auditoria — e a diferença entre ela e as outras 15 é
essa. **O ciclo funciona. Ele simplesmente não foi aplicado ainda.**

Consequência para o roteiro: a etapa 5 da Parte IV deixa de ser "reancoragem eventual" e
passa a ser **pré-requisito de série**, com ~1.500 vínculos a reancorar. Pelo rendimento
da B1 (12 de 16 automatizáveis, 75%), estimo ~1.130 automáticos e ~380 para olho humano —
que se somam aos ~10 mil da P-6.

---

## 5. PARECER: CONTINUAR COM ESTE MÉTODO E COM ESTE AGENTE

A pergunta era se o ferramental insuficiente justifica trocar de agente. **Não justifica,
e a própria carta é a prova.** Separo as duas coisas, porque estão sendo confundidas.

### O que a carta demonstra sobre o agente

Seis comportamentos que não se obtêm trocando de fornecedor:

1. **Confessou o C1 sem ser obrigada.** "As correções R2/R11 da nossa V5 não propagaram
   à ficha/g3/ledger — falha nossa, não sua." Nenhum portão os obrigaria a isso.
2. **Não aceitou meu número.** Replicou, achou 22 contra meus 24, e **pediu o log em vez
   de adotar o meu** — que é exatamente a regra que impus e que quase ninguém segue
   quando o número vem da autoridade.
3. **Auditou o auditor.** Achou três defeitos reais nos meus scripts, incluindo eu
   cometendo o pecado que acabara de cobrar deles. Um fornecedor que só executa não faz isso.
4. **Recusou-se a decidir o que não lhe cabe.** C4 ao autor científico; 3 renames
   epub×print barrados por falta de convenção. Saber onde parar é mais raro que saber executar.
5. **Confessou falso positivo próprio** (B05 `REF_DU_2023`) e consertou o parser.
6. **Rodou o P-8 na B13 e reportou 167 erros contra si mesma.** Sem isso, eu levaria
   mais uma rodada para descobrir que o defeito é de série.

### O que é insuficiente de verdade

Não é o agente. São três coisas, e nenhuma se resolve trocando quem executa:

- **Arquitetura ausente** (L-01…L-06): não existe contrato do Motor Clínico, nem schema
  de NT, nem de JSON modular, nem ontologia. Qualquer agente, do melhor ao pior, produz
  no escuro sem isso. **Trocar de agente agora só troca quem produz no escuro.**
- **Escala** (~1.500 reancoragens + ~10 mil revisões P-6): é problema de throughput e de
  orçamento humano, não de competência.
- **Revisão científica humana**: o P-6 é a única barreira real contra erro de ciência, e
  **nenhum agente pode ser essa barreira** — nem eu, nem eles. Este é o limite estrutural
  do arranjo atual, e é o único que eu chamaria de risco de método.

### O risco que eu apontaria no arranjo, já que a pergunta é franca

O ciclo bilateral casa↔auditor está funcionando bem demais em uma dimensão — verificação
mecânica — e nada em outra: **nenhum dos dois lados lê os artigos**. Eu li três abstracts
nesta rodada e encontrei que a correção R1 estava fiel; não li os outros 233. Vocês
verificaram existência por eutils. Se o mesmo erro de direção do Almulla estiver em
outras 20 fichas, **este arranjo não o encontra** — e o P-8, que acabei de escrever, também
não, porque ele confere propagação, não verdade.

Por isso mantenho **L-13 (`achado_verbatim_fonte`) como a mudança de maior retorno do
projeto inteiro** e subo sua prioridade: com a frase do abstract entre aspas dentro do
vínculo, a checagem de direção vira mecânica e os dois GRAVES teriam sido pegos por script.
Sem ela, o gargalo científico permanece humano e o projeto continuará PROVISÓRIO
independentemente de quem produza.

### Recomendação

**Manter casa e método. Trocar a ordem do trabalho.** Antes de qualquer nova biblioteca:
etapa 0 (C3 no [AT], C4 ao autor), depois **L-05 contrato do Motor + L-06 precedência**, e
**L-13 no mesmo pacote de schema**. A reancoragem de série (etapa 5) roda em paralelo,
porque é mecânica e já tem ferramenta.

O critério de replicação que vocês adotaram verbatim continua valendo, e eu acrescentaria
um segundo: **só replicar quando o P-8 fechar 0 ERRO V-02 na biblioteca-piloto e em pelo
menos mais uma** — porque uma biblioteca limpa pode ser sorte, duas é processo.

---

*Nada aqui foi aceito por declaração, incluindo o que a casa disse a meu favor. Os números
da tabela da §4 foram computados rodando o portão nas 16 bibliotecas nesta sessão. As
quatro correções da §1 estão nos scripts anexos, com teste negativo no caso da V-14.*
