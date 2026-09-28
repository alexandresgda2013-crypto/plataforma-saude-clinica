# RELATÓRIO DA CASA — Verificação do consolidado (B confirmada) contra a Arquitetura V2.2 vigente
**Rodada 32 · 2026-09-18 · Trilha 51 (28/28 VERDE, reexecutável) · decisoes rev.39**

Operador, seguindo sua instrução ("de uma olhada também no documento Arquitetura consolidada da plataforma V2"), a casa ancorou cada afirmação no documento **vigente** (V2.2, sha `df7f7cfd…`, conferido intacto) e no kit **arquivado** (COMO EXECUTAR **v1.7**). Consolidado arquivado verbatim: sha `ff8daf6f…` (2.215 b · 34 linhas), pasta `CONSOLIDADO_fluxo_B_recebido_2026-09-18/`.

---

## 1. Os 6 pontos atribuídos à Arquitetura — verificados linha a linha

| # | Afirmação do consolidado | Veredito medido | Âncora exata na V2.2 |
|---|---|---|---|
| 1 | Evidências não constituem uma segunda Biblioteca Canônica | **VERBATIM ✔** | §5 (L239) — L243: *"Elas **não constituem uma segunda Biblioteca Canônica** nem uma fonte de conhecimento científico independente."* |
| 2 | Uma referência científica existe uma única vez | **VERBATIM ✔** | §5.1 "Schema de Referência — L-05 Nível 1" — L292: *"A referência científica deve existir uma única vez no repositório bibliográfico, ainda que possa ser relacionada a múltiplas entidades oficiais."* (é a âncora normativa do dedupe por `pmid_oficial` medido na trilha 50: 10 refs do kit já existem → não duplicar) |
| 3 | Vínculos permitem uso transversal por entidades | **VERBATIM + diagrama ✔** | L369 *"Os vínculos funcionam transversalmente nessa cadeia:"* + desenho REFERÊNCIA → CLAIM → {B1, B3, S01} |
| 4 | **"o Claim Kit pode atuar como produtor controlado de N1/N2"** | **A ARQUITETURA NÃO DIZ ISSO** — 0× "kit" e 0× "produtor" em toda a V2.2 (medido) | — |
| 5 | NT, Ontologia/Grafo e JSONs permanecem em suas camadas | **✔** | §1 L31 (cadeia canônica) + mapa (fence L353s): NT → ONTOLOGIA/GRAFO → JSONs MODULARES → MOTOR + §6 dedicado à NT |
| 6 | Nenhuma camada posterior aumenta a autoridade científica | **VERBATIM-PRÓXIMO ✔** | §22 (L1115) — L1214: *"Nenhuma camada posterior deverá possuir autoridade para aumentar artificialmente a certeza científica estabelecida pelas camadas anteriores."* (+ L1184 e L1350) |

**Precisão da casa sobre o item 4 (a única correção de redação da rodada):** a afirmação é **verdadeira como compatibilidade** — provada na rodada 31: `N2.claim_id` já cita `B{n}.SM{nn}.{nnn}` na description, ids genéricos, `uso` superset, e a arquitetura não impede nada. Mas é **falsa como citação da arquitetura**: a V2.2 é silente sobre o kit (registro desde a rev.29: "Kit: 0 ocorrências na V2 — INALTERADO em qualquer opção"). Sugestão de redação para a homologação: **"compatível com a arquitetura por via dos contratos L-05"** — não "a arquitetura confirma que o kit pode…". Não é furo de ninguém; é a precisão que a casa existe para dar.

## 2. A correção do G3 (IA1 → IA2 → IA3/G3 → retorno → confirmação conjunta → fechamento)

Medida contra o texto ancorado:

1. **O acervo da casa tem `COMO EXECUTAR — v1.7`** (sha bate as DIGITAIS do kit; cabeçalho medido: "# COMO EXECUTAR — v1.7"). **`v1.8`/`v1.9` não existem em nenhum arquivo do acervo** (busca global em `BIBLIOTECAS/`: única ocorrência de "v1.9" é dentro do próprio consolidado).
2. **O que a v1.7 diz sobre G3** (quotes com linha): portão de suporte ao claim (L111) · **"Conhecimento nasce em G3"** (L114) · "G3 não é binário" — 3 saídas (L120) · ressalva exige `nota_ressalva` (L131s) · G3 exige "abstract colado nesta sessão" (L136). Executado por "a IA" **no singular** — **o arranjo multi-IA não consta do texto** (0× IA1/IA2/IA3 · 0× votação · 0× consenso · 0× fonte primária; nenhum dos 8 documentos do kit traz regra multi-IA ou mecanismo de resolução — as ocorrências de "múltipl/diverg" são contexto científico).
3. **Conclusão medida:** a correção do consolidado **é aditiva ao texto arquivado — não contradiz nada**; e toca um ponto real: a "auditoria por múltiplas IAs" (declarada na sua proposta, §1) é prática do projeto que **não está normatizada em nenhum texto do kit**. A exigência (retorno do G3 às demais, confirmação conjunta, divergência → mecanismo de resolução) merece entrar em versão normativa — **na versão certa: a casa ancora o "v1.9" quando você enviar os bytes**. Se "v1.9" foi lapso de número e o texto corrente é a v1.7, a correção se escreve como adendo sobre a v1.7.
4. O princípio de guarda que o consolidado crava — *"não é votação; fonte primária continua sendo o árbitro; consenso das IAs não cria evidência"* — é **harmônico com o §22 da V2.2** (autoridade permanece nas fontes canônicas e evidências, L1184) e com a guarda humana P-6 do projeto. A casa subscreve integralmente e propõe um complemento operacional: o fechamento por confirmação conjunta deve **ser carregável no dado** (quem confirmou → `g3_verificado_por`; divergência resolvida + razão → nota de auditoria do vínculo), caso contrário a regra fica fora da trilha.

## 3. Convergências medidas

1. **Letra B == B da casa** (RESPOSTA_17/RESPOSTA_9, rev.38) — os ajustes do consolidado (âncoras · taxonomia natureza/desenho · status/verification · derivação de trilha · entidades na NT) são **exatamente os 5 que a casa nomeou e mediu**.
2. **A sequência sugerida** (corrigir lacunas → fechar poucos claims → materializar → L-05 → validar → ampliar) **é o §7/§11 da sua própria proposta** — frentes e comentador convergiram com o piloto controlado.
3. **Camada registrada:** a casa verificou o consolidado, mas **não viu os pareceres originais de cada frente**. A homologação A/B/C/D deve se dar sobre os bytes das respostas deles (política da casa: nada vale sem o artefato ancorado).

## 4. Pedidos da casa (para destravar a homologação)

1. Envie **os pareceres originais das duas frentes** (a resposta A/B/C/D de cada um) → arquivei consolidado; agora preciso dos bytes de origem para ancorar e conferir.
2. Envie o **`COMO EXECUTAR` na versão corrente** (se existe v1.8/v1.9 fora da casa) → a casa arquiva verbatim e mede onde a correção do G3 deve entrar; se não existe, escrevo o **adendo sobre a v1.7** com o mesmo conteúdo aprovado.
3. **Confirme o remetente do consolidado** (o texto não é assinado; a voz sugere o comentador) — fecho a digitais com autoria certa.
4. Homologação é sua, como sempre: a casa recomenda avançar — **a formalização B do fluxo está convergente das três frentes + casa**, e a produção (piloto NT-B1 · portão L-05) retoma intacta.

**0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…` · V2.2 `df7f7cfd…` · P-8 `be48a5ef…` intactos. Confissões datadas da sessão: 4 (fs C1 · agulhas C2/C3 · parse C4) — nenhuma tocou dado.
— A casa (bancada de verificação)
