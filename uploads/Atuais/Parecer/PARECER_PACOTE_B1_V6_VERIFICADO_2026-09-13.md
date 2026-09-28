# PARECER SOBRE O PACOTE B1 V6 (VERIFICADO) E A RESPOSTA Nº 3

**Auditor-Mestre · 2026-09-13 · rodada 4**
**Objeto:** `pacote_auditoria_B1_V6_2026-09-13.zip` (19 arquivos, 18 com hash) + `README_PACOTE.md` + `RESPOSTA_3`.

---

## 1. O problema de entrega, antes de qualquer análise

**O pacote contém a V6. A carta descreve a V7.**

A Resposta nº 3 diz, em §0 e no rodapé: *"pacote-zip V7 anexo (sha da canônica V7 `6e2c2979…`)"*. O que chegou tem `canonica/B1 NEUROINFLAMAÇÃO V6 CANONICA.md`, sha256 **`e11dbd95…`** — a V6 final. Confirmei que a mudança central da carta não está no artefato: busquei os termos da nova regra C4 (`modificador de a priori`, `não critério de confirmação`, `rebaixa para`) na canônica entregue — **zero ocorrências** — e a tabela de classificação continua com **Critério C ≥1 presente como condição de linha** para "Compatibilidade alta".

Consequência prática, sem drama: **a decisão mais importante da rodada 3 — o fechamento do C4 no algoritmo — permanece não verificada.** Não a estou contestando; estou dizendo que não a auditei, porque o artefato correspondente não foi entregue. Ela segue como **aberta na minha contabilidade** até que a V7 chegue.

Registro de causa provável, sem atribuir culpa: o pacote foi montado para "o segundo auditor externo" antes da V7 existir, e foi encaminhado como se fosse o anexo da carta. É um erro de versionamento de entrega, não de conteúdo — mas é exatamente a classe de erro que o projeto inteiro existe para não cometer, e vale registrar como precedente.

## 2. Integridade do pacote — íntegra

| Verificação | Resultado |
|---|---|
| `sha256sum -c SHA256SUMS.txt` | **18/18 OK** |
| Contagens declaradas × reais | 200 + 34 + 3 = **237 refs** ✔ · **274 vínculos** ✔ · **237 ledger** ✔ |
| Diff V6-pré (`d8f41662`) × V6 final (`e11dbd95`) | **4 linhas**, todas de rótulo: o H1 dizia "V5" e foi corrigido; nota da errata acrescentada. **Zero toque científico** — confirmado |
| Autocontenção | reproduzi o layout do README e rodei tudo sem ajuste |

A errata do H1 merece nota: **o título interno dizia V5 enquanto o `artefato_rotulo` dizia V6, e nenhum portão pegou.** Quem pegou foi o operador, lendo. Isso é uma lacuna real de ferramenta — proponho **V-16**: o H1, o `artefato_rotulo`, o nome do arquivo e a versão do manifesto têm de concordar; divergência é ERRO.

## 3. Reprodução independente dos portões — bate exatamente

| Portão | Casa reportou | Eu medi |
|---|---|---|
| Gate P-5 | APROVADO | **APROVADO** |
| Framework | 0 ERRO / 236 AVISO | **0 ERRO / 236 AVISO** |
| P-8 | 0 ERRO / 25 AVISO | **0 ERRO / 25 AVISO** |
| V-02 (âncora em rodapé) | 0 | **0** |
| V-14 | 14/14 | **14/14** |

Primeira vez em quatro rodadas que **todos os números batem na primeira tentativa, dos dois lados, com a camada de evidência na mão.** Registro isso porque foi conquistado, não dado.

## 4. O que verifiquei além dos portões

**C1 persistiu.** As correções de Comai e Enache continuam nas fichas; as notas de `VINC_B1_0219` e `VINC_B1_0247` mantêm a versão corrigida. *(Meu primeiro teste marcou as duas como falha — era falso positivo meu: as notas citam o termo antigo dentro da própria frase de correção, "não é meta tri-compartimental". Prática correta da casa; teste grosseiro meu.)*

**C3 é a melhor ficha do acervo.** `REF_OSIMO_2019`: PMID 31258105, `desenho_estudo` "Meta-Analysis; Systematic Review", achado com os números e intervalos, `citacao_confirmada: true`; ledger `AUD_B1_0238` com **1.507 caracteres de abstract literal colado**; `VINC_B1_0274` ancorado na frase de prosa com `claim_id B1.MEC.BLOCO11.001`. É o padrão que o `achado_verbatim_fonte` (L-13) deve generalizar — vocês já provaram que sabem fazer.

**As 4 re-âncoras do C2 estão corretas.** `0261`, `0262`, `0265`, `0266` e `0175` em prosa, com `claim_id`. *(Suspeitei do `0261` porque o início da âncora cita Shirakawa; a âncora é um span de duas frases e Han está dentro dela. Alarme falso meu, registrado.)*

**A decisão do Mehta na V7 está cientificamente certa** — verifiquei na fonte: PMID 31951051 é revisão sistemática (486 estudos triados, 51 incluídos, N=10.633), sem meta-análise, implicando metilação em genes do eixo HPA e inflamatórios. Mover de `02_meta_analises` para `01_pmids` e MA→OB é correto. No pacote V6 a contradição ainda está viva: a ficha mora em `02_meta_analises` mas o próprio `desenho_estudo` diz "OB revisao sistematica".

**A recusa em criar o vínculo do L717 está certa.** O escopo "eixo HPA e genes inflamatórios" torna FKBP5 plausível, mas plausibilidade não é trecho literal. Não criar o N2 e mandar ao P-6 é a decisão correta — e a confissão da margem ("a identificação é por desenho↔pedido↔escopo, não por trecho literal") é o tipo de transparência que dispensa auditoria adversarial.

## 5. Taxonomia: reconciliação do 71 × 84

Medi no pacote real: **71 divergências prosa×apêndice** — idêntico ao que medi na V6-pré, o que confirma que a errata do H1 não mexeu em nada. O 84 de vocês vem de um matcher que casa sufixos e cobre mais chaves; **os dois números descrevem o mesmo defeito e o de vocês é mais completo.** Adoto 84 como a contagem de referência.

Achado adicional meu nesta medição: **12 tokens de apêndice carregam dois classificadores diferentes ao mesmo tempo** — `Bull_2009`, `Klengel_2013`, `Steiner_2011`, `Sublette_2011`, `Setiawan_2015`, `Holmes_2018`, `Mehta_2020`, `Levy_2018`, `Teeling_2013` e três tokens sintéticos (`Epi_2019`, `Primingprinc_2018`, `Psoriase_2025`). Os três últimos merecem atenção à parte: **são tokens de apêndice que não correspondem a nenhum autor** — parecem rótulos temáticos misturados ao espaço de nomes das referências. Isso é ruído no namespace que o motor vai indexar.

A posição normativa que vocês declararam — *"a semântica vigente de fato do `[XX]` é ambígua; não há declaração normativa preservada que os distingua"* — é a resposta que eu pedi, e é a correta. Confessar a ausência de norma é melhor que inventar uma retroativamente. **Não classifico as 84 como erro científico**; classifico como **dívida arquitetural bloqueante do motor**, a ser resolvida no L-05/1.2 com um campo autoritativo único. V-15 e V-16 entram no meu lado da fila de portões.

## 6. Contabilidade dos impedimentos

| # | Impedimento | Estado |
|---|---|---|
| 1 | **P-6** — revisão humana | Aberto por decisão do operador (instância do fim). Único número agora: **108 vínculos / 91 refs**, derivado de artefato — AUD-066 **encerrado** |
| 2 | **C4** — circularidade no algoritmo | **Aberto na minha contabilidade** — a correção descrita é a alternativa certa e bem fundamentada, mas está na V7, que não recebi |
| 3 | **Taxonomia de classificador** | Aberto, no pacote L-05/1.2 · 84 divergências + 7 autodivergências + 12 tokens ambíguos + 3 tokens sem autor |
| 4 | **Camada de evidência** | **Encerrado** — entregue, íntegra, reproduzida |

## 7. Veredito

### **B1 V6: APROVADA COM RESSALVAS — confirmada como base piloto do trio**

Mantenho o veredito da rodada anterior, agora com a camada de evidência efetivamente auditada em vez de presumida. A biblioteca está apta a servir de fonte para a NT e o JSON modular. O selo definitivo continua barrado pelo P-6, e agora também pelo C4 até que a V7 chegue.

**Uma condição nova e única para a rodada 5:** enviar o pacote da **V7** no mesmo formato deste (que foi excelente — canônica + `01/02/03` + manifesto + vínculos + ledger + ferramentas + saídas + `SHA256SUMS.txt`). Com ele fecho o C4 e o item 2 da tabela acima.

## 8. Sobre o próximo passo

O Bloco 1 está aceito dos dois lados e a ordem não muda: **Contrato do Motor (L-05) → taxonomia única (1.2) → precedência (L-06) → `achado_verbatim_fonte` (L-13)**. O achado da §5 reforça que 1.2 não é higiene, é pré-requisito: um motor determinístico não consegue ponderar evidência quando o mesmo campo tem três significados e 12 tokens têm dois valores simultâneos.

Sobre a proposta de **B13 como a "mais uma"** do critério de replicação: aceito. É a escolha certa — 167 erros V-02 já diagnosticados, perfil idêntico ao da B1 pré-ciclo, e serve de teste honesto para o reancorador de série. Sugiro apenas que o reancorador seja escrito **antes** de tocar a B13, e que a B13 seja a primeira execução dele e não um piloto manual — senão repetimos o artesanato que a §7 do parecer anterior pediu para não repetir.

---

*Verificações desta rodada: 18/18 hashes; contagens 237/274/237 conferidas nos JSONs; diff V6-pré×V6-final (4 linhas, zero científicas); gate, framework e P-8 re-executados de forma independente; persistência das correções C1; ficha e ledger do Osimo 2019; 5 re-âncoras C2; 71 divergências de classificador e 12 tokens ambíguos re-medidos; Mehta 2020 (PMID 31951051) verificado em fonte primária. Dois falsos positivos meus (notas C1 e âncora 0261) registrados no corpo. A V7 não foi auditada porque não foi entregue.*
