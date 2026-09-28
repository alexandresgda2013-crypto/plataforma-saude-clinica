# RELATÓRIO DA CASA — AUDITORIA INDEPENDENTE DA 2ª RODADA DA IA EXTERNA (MOTOR CLÍNICO)
**Rodada 34 · 2026-09-19 · Trilha 53 reexecutável: 74/74 checks verdes · 0 ciência tocada**

**Objeto (pedido do operador):** verificar se as classificações da 2ª rodada da IA externa (E1–E20 · P1–P8 · G1–G20 · C1–C10) estão corretas à luz dos documentos-base vigentes — sem redesenhar o Motor, sem propor arquitetura, sem tratar proposta como regra.

**Base documental desta auditoria (verbatim no acervo da casa):**
| Documento | sha256 | Medida |
|---|---|---|
| FASE 2- 02 FILOSOFIA DO PROJETO.md | `dedbff6c8f542025a3f0579d58ab84ca17c122f113f2980edcb18153c408408b` | 5.264 b · 46 linhas |
| ROTEIRO DE TRABALHO DA PLATAFORMA.md | `5e3f916335c4d631c2639e2aaf8efd48c98f6762e263ff301c4dfc9022bd04ac` | 22.447 b · 780 linhas |
| ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2 – 17.09.26.md (**VIGENTE**) | `df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1` | 52.181 b · 30 seções únicas · H1 "V2.2" · Rev. V2.2 |
| Parecer da IA externa (2ª rodada, transcrito do chat do operador) | `40a58381354ddddd…` (completo nas DIGITAIS da pasta) | 16.964 b · 101 linhas |

**Trilha de verificação:** `producao/TRILHA53_script_auditoria_2rodada_IA_externa_motor_2026-09-19.py` + `TRILHA53…json` — cada check com regex/escopo/camada (case-sensitive × casefold × NFC)/sha registrados; confissões datadas de régua: 6 (todas nossas, corrigidas até verde).
**Ciência intocada (verificado início e fim):** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…` · P-8 `be48a5ef…`.

---

## 0. ACHADO DOCUMENTAL-RAIZ (anterior a qualquer item): **a IA auditou o documento SUPERSEDED**

A IA externa **não auditou a Arquitetura vigente** (`df7f7cfd…`). Auditou a linha pré-vigente (upload da rodada 24 `5be36836…` ou V2.1 `1a50645e…` — indistinguíveis pelas âncoras que ela cita; ambas SUPERSEDED). Provas medidas (checks 0.6–0.13):

1. **C-10 dela é impossível contra a vigente.** Ela registra "o arquivo se intitula 'Arquitetura Consolidada da Plataforma V2'; os diagramas internos e o Roteiro referem 'V2.2'". A vigente tem H1 **"...PLATAFORMA V2.2  17.09.26"**, cabeçalho **"Rev. V2.2 — 2026-09-17"** e 30 seções únicas. O Roteiro refere V2.2 ×2, coerente com ela.
2. **A citação "literal" do item E6 não existe em nenhuma versão da arquitetura.** `"preservando a origem de cada informação"` = **0×** (camada casefold) na vigente, no upload r24, na V2.1, na V2-15.09 e na V1 — e `"quando pertinente"` = 0× na inteira base. A IA a apresenta entre aspas, com "literalmente", ancorada em "§2, bloco DEFINIÇÃO". **Consequência de método registrada pela casa: toda citação dessa frente será tratada como paráfrase até verificação.** (A substância que o E6 quer ancorar existe — mas só na vigente, por outro texto: `origem_conhecimento = canonico | atualizacao` ×3 + "a consulta conjunta preserva a rastreabilidade".)
3. **Nenhuma menção às três marcas exclusivas da vigente** (`origem_conhecimento`, "a prosa deste documento prevalece sobre os desenhos", "fora do cânone") — marcas essas que resolveriam parte do que ela classifica como contradição. Quem leu a vigente não as omitiria.
4. Fingerprints de seção (camada regex `^# \d+\.`): vigente = 30 únicas; r24 = 31 com **§21 duplicada**; V2.1 = 31 com **§2 duplicada**. O relatório dela convive com §§2/21/30 sem notar anomalia — compatível com a linha antiga (e compatível com o arquivo do projeto do mestre, `309aa65f…`, já identificado na rodada 33 como upload r24 rotulado — dívida D-V22-BYTES-PROJETO viva).

**Consequência para a auditoria:** tudo o que a IA ancorou **fora de §2** permanece materialmente válido (o sufixo §3→fim é byte-idêntico entre a linha antiga e a vigente). Os itens que dependem de **§2, do §19 em contraste com o §2 antigo, e dos pontos de versão/prosa** exigem re-ancoragem — e é onde suas conclusões mudam (ver B C-2, C-10 e tabela A G1).

---

## A. G1–G20 — TABELA DE VALIDAÇÃO DA CASA

Legenda de veredito sobre a IA: **CONFIRMADA** (pendência existe e está bem classificada) · **REDUZIDA confirmada** (a redução da própria IA está correta) · **REFORMULADA** (existe, mas o enquadramento está errado) · **NÃO DETERMINÁVEL NESTA BASE** (marcação correta por regra do operador).

| ID | Classe da casa | Veredito sobre a IA | Âncora medida (trilha 53) |
|---|---|---|---|
| **G1** | PENDENTE real | **CONFIRMADA em essência, REFORMULADO o agravante**: a "superfície de runtime" é pendência genuína (4 representações textuais coexistem: §2 DEFINIÇÃO lista Bibliotecas/Narrativas/Grafo/JSONs; §6 item 13 e §14 mandam material narrativo ao Motor; §19 desenha Bib/NT/JSONs→Motor; §5.3/§16/§17 descrevem JSONs→Motor). **MAS o agravante "documentos se contradizem" não subsiste na vigente**: há regra interna de arbitragem ("a prosa deste documento prevalece sobre os desenhos") + prosa normativa do §2 (fluxos segregados até o Motor; Pasta por caminho próprio). Pendente real: interfaces, formato dos JSONs, consulta a N1/N2 por referência para rastreabilidade — sem redesenho aqui. | D-G1, E-C2 |
| G2 | NÃO DETERMINÁVEL NESTA BASE | **CONFIRMADA** — a base só informa que os arquivos existem (Roteiro §9; checklist item 23 "ARQUIVOS EXISTENTES"); "contrato de entrada" 0× nos três documentos. | D-G2 |
| G3 | parcialmente ESTABELECIDO + PENDENTE residual | **REDUZIDA confirmada** — a ancoragem dos dados do paciente aos 146 IDs é exigida pela Filosofia; "sintomas"/"escalas" = 0× em toda a Arquitetura (§1/§3 não listam essas classes). | C-G3red |
| G4 | PENDENTE | **CONFIRMADA** — `condição` existe como nome (§5.2, §11, §13 = placeholders); nenhuma linguagem formal na base (WHERE/expressão booleana/DSL = 0×). | D-G4 |
| G5 | NÃO DETERMINÁVEL NESTA BASE | **CONFIRMADA a marcação** — os nomes dos campos estão na base (§5.1/§5.2); os domínios de valor, não (0× "valores permitidos"/"enum"). *(Nota de acervo, sem resolver: fora desta base existem os schemas L-05 N1 v1.3/N2 v1.4 aprovados na rodada 29.)* | D-G5 |
| G6 | ESTABELECIDO (conteúdo) + PENDENTE (formato) | **REDUZIDA confirmada** — conteúdo do laudo: §23 ×1 verbatim + Filosofia ("linguagem clara e didática", razão de cada hipótese, improváveis, fundamentação, rastreabilidade); "schema do laudo" 0× nos três. | C-G6red |
| G7 | PENDENTE | **CONFIRMADA** — os três nomes de trilha existem; "definição operacional" 0×. | D-G7 |
| G8 | PENDENTE | **CONFIRMADA — a casa endossa "maior lacuna substantiva"**: a Filosofia **exige** estimar relevância relativa e descartar mecanismos (×1 cada); "relevância relativa" 0× na Arquitetura e no Roteiro; "critério de descarte" 0× nos três. | D-G8 |
| G9 | PENDENTE **declarada** | **CONFIRMADA** — §19 literal: modalidade (alerta/atualização/comparação/enriquecimento/outra) "deverá ser definida posteriormente no contrato do Motor". | C-G9 |
| G10 | PENDENTE (fronteira) c/ piso ESTABELECIDO | **REDUZIDA confirmada** — piso: proibido improviso/especulação (Filosofia) e dependência de geração espontânea (§14/§28 ×1); "componente generativo" 0× nos três. | C-G10red |
| G11 | PENDENTE | **CONFIRMADA** — Filosofia exige "sinergias, interações, contraindicações" ×1; na Arquitetura "sinergia" 0× e "contraindicação" 0×; §11 tem `tipo_relacao: [relação definida pela ontologia]` (placeholder). | D-G11 |
| G12 | PENDENTE nesta base | **CONFIRMADA** — "conflito" 0× nos três documentos para relações. *(Solução: não determinável nesta base; nota de acervo: existe minuta L-06 fora dela.)* | D-G12 |
| G13 | PENDENTE | **CONFIRMADA** — checklist item 30 prevê reexecução; "versão do laudo" 0× nos três. *(Imprecisão da IA: a âncora é §13 checklist, não §12 — conteúdo existe igual.)* | D-G13 |
| **G14** | PENDENTE | **CONFIRMADA** — §22 coloca a Biblioteca na cadeia de autoridade (ordem medida EVIDÊNCIA→…→BIBLIOTECA); Roteiro §7 desvia os claims ("não entram na Biblioteca Canônica de mecanismos" ×1). Registro da casa: a direção substantiva já consta de documento oficial da própria base (Roteiro §7) e da governança (rev.38, proposta da rodada 31) — o nó remanescente é formal: diverge da Filosofia literal → depende de **G19**. | D-G14 |
| G15 | PENDENTE (operacionalização) | **REDUZIDA confirmada** — §10 tem exatos 15 itens numerados; §12 tem exatos 9 bullets (medido por regex nas fatias). | C-G15red |
| **G16** | PENDENTE — raiz real | **CONFIRMADA como raiz** — tensão textual nas duas direções medida à letra: Filosofia atribui a integração aos 146 IDs **à anamnese** ("anamnese estruturada e inteligente integra informações clínicas…"); a Arquitetura atribui **ao Motor** o cruzamento ("Ao receber este gatilho, o Motor executa uma busca ativa e cruza esses dados…", §2 DEFINIÇÃO) e trata a anamnese como fornecedora de contexto (§23). | D-G16 |
| G17 | PENDENTE (não bloqueante) | **CONFIRMADA** — escopo "ansiedade e depressão" só na Filosofia (0× "ansiedade" em Arquitetura e Roteiro); "fora do escopo" 0× nos três. | D-G17 |
| G18 | PENDENTE | **CONFIRMADA** (= C-6) — "trilha clínica ou mecanística" ×1 (dois valores, §5.2) × três trilhas de saída (§2/§21); "trilha terapêutica" 0×; "mapeamento" 0×. | D-G18 |
| **G19** | PENDENTE — raiz máxima | **CONFIRMADA** — Roteiro §16 subordina **apenas** o próprio Roteiro ("Nenhum documento deste roteiro substitui os contratos normativos…"); "Filosofia" 0× na Arquitetura e no Roteiro; "Arquitetura Consolidada" 0× na Filosofia. Nenhum documento declara precedência Filosofia × Arquitetura. | D-G19 |
| G20 | PENDENTE, **não autônomo** | **REFORMULADA** — a tensão existe (âncoras medidas), mas G20 é a **projeção de C-3/C-4 sob G19**; listá-lo como vigésima decisão independente infla a matriz. Trata-se da mesma decisão de admissibilidade/proveniência com dois exemplos (Pasta; claims). | D-G20 |

**Síntese A:** 20 itens — **15 pendências reais confirmadas** (G1, G4, G7–G14, G16–G19) · **2 corretamente marcadas como indetermináveis nesta base** (G2, G5) · **3 reduções da própria IA confirmadas** (G3, G6, G15; mais G10 como redução parcial) · **1 reformulada por dupla contagem** (G20). **Pendências criadas indevidamente: nenhuma inventada do zero; 1 agregada indevidamente (G20) e 1 agravante invalidado (o "agravado" do G1).** A ordenação da IA (G1, G16, G19 antes dos demais) é **substancialmente correta** — a casa inverte para **G19 → G16 → G1** (ver seção E) e registra: os rótulos "M1…M9/T1…T3" na coluna "Módulo afetado" são **propostas da própria IA** (0× na base — check B-P1), não estrutura vigente.

---

## B. C1–C10 — TABELA DE VALIDAÇÃO DA CASA

| ID | Classe da casa | Veredito detalhado | Âncora |
|---|---|---|---|
| **C-1** (Filosofia × Arq: NT "conecta domínios" × NTs por domínio/Grafo) | **FALSA CONTRADIÇÃO** | A casa **diverge da IA** com prova de reconciliação **interna aos documentos**: Filosofia = nível macro ("representação integrada… conectar os diferentes domínios"); Arquitetura detalha o mecanismo — cada NT mantém seu domínio (§8 ×1), "a integração ocorre por meio das relações" (§8 ×1 literal), a NT identifica/estrutura relações e as prepara para a Ontologia (§6 itens 4–9, incl. "estabelecer relações auditáveis com outras NTs" ×1), e "a Ontologia/Grafo formaliza essas relações entre entidades" (§9 ×1). "Conectar" (Filosofia) ≡ "relações identificadas na NT e formalizadas no Grafo" (Arquitetura): **DERIVÁVEL, sem decisão arquitetural.** O que resta é dívida de glossário (harmonizar o verbo). O enquadramento da IA ("decide se M3 percorre o Grafo ou lê NT integrada") usa módulo que só existe na proposta dela. | E-C1 |
| **C-2** (o que o Motor lê) | **FOI CONTRADITÓRIO — JÁ RESOLVIDO na vigente** | **Na base que a IA leu (pré-vigente): VERDADEIRO** — o nó "EVIDÊNCIAS / VÍNCULOS UNIFICADOS" e o fluxo da Pasta a montante contradiziam §19/§28. É exatamente **o ACHADO do mestre de 17/09** (`2841bc66…`), já corrigido por decisão do operador (rodada 26) na V2.2 vigente: nó removido, fluxos segregados até o Motor (prosa: "permanecem segregados até o Motor Clínico" · "caminho próprio, por consulta ativa" · "sem se fundir aos vínculos canônicos" — 3× medidas), proveniência no item e regra "prosa prevalece sobre desenhos". **Residual real e menor:** os desenhos frios §21 e §30 ainda mostram a Pasta se juntando a montante/JSONs (medido) — dívida já registrada como D-V2-DIAGRAMA-DUPLO, arbitrada pela regra de prevalência. **Não é mais contradição; G1 segue pendente sem agravante.** | E-C2 |
| **C-3** (Filosofia "derivar exclusivamente das Bibliotecas" × §19 Pasta) | **CONTRADITÓRIO real interdocumental** | **CONFIRMADA.** A Filosofia veda conteúdo ao usuário fora das Bibliotecas (×1 literal); §19 manda o Motor consultar a Pasta (×1). A vigente **mitiga sem resolver formalmente**: proveniência obrigatória no item (`origem_conhecimento` ×3) + "fora do cânone" ×1 + modalidade pendente (G9). A divergência formal **exige G19** (qual documento rege) — não é resolvível dentro do contrato do Motor. Único ajuste fino à IA: a consequência binária ("ou viola a Filosofia, ou §19 inerte") tem terceira via já prefigurada na vigente (uso marcado como atualização/alerta — G9), o que reclassifica a consequência, não a pendência. | E-C3 |
| **C-4** (Filosofia "ingresso obrigatório" × Roteiro §7 "não entram na Biblioteca") | **CONTRADITÓRIO real formal** | **CONFIRMADA** à letra (duas âncoras ×1). Nuance registrada: a direção substantiva **já é documento oficial desta própria base** (Roteiro §7) e está registrada na governança (rev.38 — proposta do operador homologada por ninguém ainda). O que falta: homologação + regra de hierarquia (G19) ou emenda de uma linha na Filosofia. **Resolção não pertence ao contrato do Motor — ponto da IA correto.** | E-C4 |
| **C-5** (tríade da Filosofia omite Evidências/Vínculos e Ontologia/Grafo) | **DIVERGÊNCIA real de cobertura** | **CONFIRMADA** — na Filosofia: "ontologia" 0×, "grafo" 0×, "vínculo" 0×, "evidências/vínculos" 0× (só a tríade Biblioteca/NT/JSON). São dois mapas da mesma cadeia em granularidades distintas; fecha-se **junto de G19** (e da dívida de glossário de C-1). | E-C5 |
| **C-6** (2 trilhas no vínculo × 3 na saída) | **DIVERGÊNCIA real de taxonomia** | **CONFIRMADA** (âncoras em D-G18). Sem mapa vínculo→sugestão declarado; é **pendência de decisão (G18)**, não contradição lógica (um valor a mais na saída não contradiz o domínio do vínculo — falta é a regra de correspondência). | E-C6 |
| **C-7** (Biblioteca antes × depois das Evidências) | **DIVERGÊNCIA DE REPRESENTAÇÃO — REBAIXADA pela casa** | Textos confirmados nas duas direções (ordens medidas: §5.3 e §22 e §20 colocam Evidência antes; §2, §21, §30 colocam Biblioteca antes). A casa **rebaixa de "contradição" para divergência resolvível com decisão de registro mínima**: §5.3/§22 descrevem o **fluxo de constituição/autoridade** (a evidência sustenta a afirmação que compõe a Biblioteca); §2/§21/§30 descrevem o **fluxo de consumo** (a Biblioteca, já constituída, disponibiliza seus conteúdos e evidências ao Motor). A distinção não está declarada — precisa de **uma linha normativa** (glossário), não de redesenho; a trilha de rastreabilidade §11 (`claim → evidência → biblioteca`) está estabelecida e não depende dessa leitura. **Não bloqueia o contrato do Motor** (contra a IA). | E-C7 |
| **C-8** (status B1: §26 × checklist) | **DIVERGÊNCIA DE REGISTRO real** | **CONFIRMADA** — §26 "já possui sua Biblioteca Canônica e passou pelo processo de auditoria" ×1 × checklist item 9 "🔄 EM CONSOLIDAÇÃO" e item 8 "🔄 EM VALIDAÇÃO" (medidas). Mitigação **no próprio §26**: "a validação estrutural e a validação científica são dimensões distintas" ×1 (e §29 mantém a auditoria ativa). Divergência de **status reportado** entre documentos, não de arquitetura: corrigir um dos dois registros (correção menor, dono: governança). Impacto prático a IA apontou corretamente (leitura do piloto). | E-C8 |
| **C-9** (Roteiro §17 "já consolidado" × checklist item 2 "PENDENTE DE REGISTRO") | **FALSA CONTRADIÇÃO** | Textos confirmados — mas **"pendente de registro" ≠ "não feito"**: o checklist cobra o **registro formal** do que §17 declara consolidado conceitualmente. É divergência de rótulo de controle de progresso, no máximo débito documental menor. Descartável como contradição (a própria IA a classificou "menor"). | E-C9 |
| **C-10** (título "V2" × referências "V2.2") | **FALSO — artefato da base superseded** | Contra a vigente é **impossível**: H1 V2.2, cabeçalho Rev. V2.2, Roteiro ×2 coerentes. É a prova-fumaça do achado da seção 0: **a IA leu o documento errado.** Nada a decidir aqui; a ação é o saneamento da base (seção E, passo 0). | E-C10 |

**Síntese B:** 10 itens — **4 divergências reais que exigem decisão fora do contrato** (C-3, C-4 → G19; C-8 registro; C-5 fecha com G19) · **1 real de taxonomia→pendência** (C-6→G18) · **2 rebaixadas/descartadas como "contradição" com solução derivável ou já resolvida** (C-7 registro mínimo; C-2 resolvida na vigente com residual de desenhos) · **2 falsas contradições** (C-1, C-9) · **1 falso item por artefato de base** (C-10). Contra a contagem da IA ("quatro — C-2, C-3, C-4, C-7 — impedem a especificação"): na vigente restam **C-3 e C-4**.

**Nota sobre Parte A/B/C da IA (E/P/[?]):** casa confirma 16/16 confirmações substantivas de E1–E20 (com E6 re-ancorado e E8 com precisão de escopo — a regra do §11 vincula "o sistema"; sua aplicação ao Motor é derivável, não "explícita"); valida integralmente as autocorreções E11/E15/E18/P6 e a correção estrutural (módulos = proposta: **0× tokens M1–M9/T1–T3 na base**); valida as resoluções/reduções da Parte C, com duas emendas: a "Preservação de procedência" só é [E] **na vigente** (âncora válida: `origem_conhecimento`), não na base lida; e a "agravamento" do G1 cai (ver A-G1). Regra da casa daqui em diante: **nenhuma aspa dessa frente vale como literal sem verificação** (E6).

---

## C. PONTOS-RAIZ QUE PRECISAM REALMENTE DE DECISÃO ARQUITETURAL

1. **G19 — hierarquia normativa (Filosofia × Arquitetura V2.2 × Roteiro).** Raiz máxima, confirmada. Sem ela, C-3/C-4/C-5 oscilam e G14/G20 não fecham. *(Nenhuma solução aqui — apenas a ordem.)*
2. **G16 — fronteira Anamnese ↔ Motor.** Raiz real: dois documentos atribuem a ancoragem aos 146 IDs a componentes distintos. Antecede o contrato de entrada (G2) e o residual de G3.
3. **G1 reformulado — superfície de dados em runtime.** Pendente real sem agravante de contradição. Puxa consigo G9 (modalidade da Pasta) e G13 (superfície+versionamento).
4. **C-3/C-4 + G14/G20 — admissibilidade e origem rastreável do conteúdo não-canônico (Pasta; claims).** Decisão formal após G19; a direção substantiva já existe no Roteiro §7 e na governança (rev.38) — falta homologação.
5. **G18/G7 (+G11) — taxonomia e conteúdo operacional das trilhas** (casamento 2×3 verificado; tipos de relação exigidos pela Filosofia sem enumeração na Arquitetura).
6. **G8 — relevância relativa e descarte** (maior lacuna substantiva; a casa endossa a gradação da IA).
7. **Demais pendências técnicas confirmadas:** G4, G5 (após abrir os schemas L-05), G6 (só o formato), G10, G12, G13, G15, G17.
8. **Correções de registro (não são decisões arquiteturais):** C-8 (status B1), C-1/C-5 (glossário/cobertura), C-7 (uma linha declarando constituição × consumo), C-9 (rótulo), desenhos frios §21/§30 (residual C-2), C-10/E6 (saneamento da base da IA).

## D. PONTOS DESCARTÁVEIS (falsa pendência/contradição ou já resolvidos)

- **C-10** — artefato da base errada (vigente é V2.2 no título).
- **C-9** — "pendente de registro" ≠ "não feito" (rótulo de controle).
- **C-1** — reconciliação interna derivável; é dívida de glossário, não decisão.
- **C-2 como contradição vigente** — já resolvida na rodada 26 (V2.2); resta residual de desenhos (D-V2-DIAGRAMA-DUPLO).
- **O "agravamento" de G1** — cai com a prevalência da prosa; G1 permanece como pendência limpa.
- **G20 como 20ª decisão autônoma** — agregado de C-3/C-4 sob G19 (dupla contagem).
- **C-7 como "contradição que impede o contrato"** — rebaixada a divergência de representação (1 linha de glossário); não bloqueia.
- **E6 como "reforço literal"** — citação fabricada (0× em toda a linha documental); a substância vale só pela vigente.
- **M1–M9/T1–T3, "travessia", "fechamento da trilha"** — vocábulos da própria IA; ela mesma os reclassificou (correto); não pertencem à base (0×).
- **P1–P8 como "regras do documento"** — a IA já os mantém [P]; a casa confirma: 100% proposição. Nenhum [P] foi indevidamente promovido a [E] na 2ª rodada — ponto de método dela, correto.

## E. ORDEM RECOMENDADA PARA RESOLVER AS DECISÕES (sem definir soluções)

0. **Saneamento documental (pré-condição, não é decisão):** alinhar a IA externa (e o projeto do mestre) aos bytes da vigente `df7f7cfd…` — é a dívida D-V22-BYTES-PROJETO já aberta; e adotar a regra "citação ≠ literal até verificação" para esta frente.
1. **G19** — qual documento rege em conflito (Filosofia × Arquitetura × Roteiro).
2. **G16** (fronteira Anamnese↔Motor) → destrava **G2** (contrato de entrada — abrindo os arquivos de anamnese existentes) e **G3-residual** (classes de ID para sintomas/escalas).
3. **G1** (superfície de runtime: JSONs + Pasta; papel de N1/N2 por referência na rastreabilidade) → com **G9** (modalidade da Pasta) e **G13** (versionamento) na mesma sessão de decisão.
4. **C-3/C-4 homologadas sob G19** → fecha **G14/G20** e harmoniza **C-5** (+emenda de cobertura/glossário na Filosofia, se aplicável).
5. **G18/G7** (taxonomia e definições das trilhas) → com **G11** (tipos de relação ontológicos) na sequência, pois C-6 toca os contratos L-05 a jusante.
6. **G8** (relevância/descarte) → com **G12** (precedência em conflito de vínculos).
7. **G4/G5/G6/G10** (condição formal; domínios L-05; schema do laudo; fronteira do componente generativo).
8. **G15/G17** (operacionalização executável dos critérios; regra de fora-de-escopo).
9. **Correções de registro** (C-8, C-1/C-5 glossário, C-7 UMA linha, C-9 rótulo, desenhos §21/§30) — em qualquer janela, sem dependência.

---

## ANEXO — PENDÊNCIAS POR DONO (rodada 34)

- **Operador:** (a) repassar o relatório à frente externa; (b) **identificar a frente/remetente** da auditoria (casa não recebeu a 1ª rodada — pedir os bytes); (c) providenciar que ela receba a V2.2 vigente (`df7f7cfd…`, 52.181 b) — fecha este caso junto de D-V22-BYTES-PROJETO; (d) homologações que seguem na sua mesa (decisão B do fluxo dos claims; pareceres originais das frentes; COMO EXECUTAR corrente; demais antigos).
- **Frente externa:** re-ancorar na vigente os itens dependentes de §2/§19 (E6, C-2, C-10, agravante do G1); aceitar D como descartáveis; prosseguir para G19→G16→G1.
- **Casa (dívidas próprias novas):** nenhuma de conteúdo; regime novo adotado — citações desta frente sem valor literal até verificação. Mantidas: rev.A3-E2, taxonomia (197 desenhos), reancorador B13, órfão BLOCO01.001.

**Casa — bancada de verificação · 2026-09-19 · rodada 34 · trilha 53 (74/74) · nada redesenhado, nada decidido além dos documentos.**
