# POR QUE O SISTEMA DE PORTÕES DEIXOU PASSAR OS ERROS — ANÁLISE, CORREÇÃO E LACUNAS

**Auditor-Mestre · 2026-09-13**
**Escopo:** as 4 ferramentas de portão (`gate_script.py`, `validar_auditoria.py`, `checklist_entrega.py`, `check_fidelidade_canonica.py`), o Processo v2.1, o Prompt 4.2 e a Filosofia do Projeto — confrontados com os erros que efetivamente escaparam (AUD-026, 027, 029, 030, 031, 032, 035, 036, 037 e os novos AUD-049…063).

---

# PARTE I — DIAGNÓSTICO: POR QUE FALHOU

## A causa-raiz em uma frase

> Os portões foram construídos para provar que **as referências existem e que os identificadores casam**. Nenhum deles foi construído para provar que **a afirmação escrita corresponde ao que a referência diz**, nem que **as camadas dizem a mesma coisa entre si**. Como o pipeline mediu apenas o que sabia medir, todo indicador ficou verde enquanto a classe de erro mais perigosa passava livre.

Isso não é opinião: é mensurável. Abaixo, cada falha com o número que a comprova.

## F-01 · A checagem cruzada de citações enxergava 7,2% do texto

`validar_auditoria.py` usa esta regex para achar citações:

```
\(Autor(?: et al\.)?,?\s+(\d{4})[a-z]?\)\[([A-Z]{2})\]
```

Ela exige que o classificador tenha **exatamente duas letras maiúsculas e feche o colchete imediatamente**. O acervo real escreve `(Swanson et al., 2019)[OB; revisão, humano+animal]`.

| Medição na B1 V5 | Valor |
|---|---|
| Citações `(Autor, ANO)` presentes no texto | **280** |
| Citações que a regex oficial reconhece | **20** |
| **Cobertura efetiva da checagem cruzada** | **7,2%** |

Ou seja: 260 citações nunca foram confrontadas com o Módulo 09. O erro do Hafizi (ID `REF_HAFIZI_2005` para um artigo de 2007) sobreviveu a cinco rodadas porque estava nos 92,8% invisíveis.

## F-02 · O verificador de âncoras procurava um formato que não existe

O mesmo arquivo procura âncoras no padrão `[REF_BLOCO_XX: Autor_Ano[tipo] | …]`.

| Medição na B1 V5 | Valor |
|---|---|
| Âncoras `[REF_BLOCO_XX: …]` encontradas | **0** |
| Linhas-lote `*ZDILAR_2000[MA] \| …*` realmente usadas | **86** |

O ramo inteiro é código morto. Nunca executou uma verificação sequer no acervo.

## F-03 · O detector de referência órfã é logicamente inalcançável

A condição é `rid not in refs_citados AND rid not in ids_ledger`. Como o ledger cobre **236 de 236** referências, o segundo termo é sempre falso.

> **O AUD-032 (17 órfãs) foi encontrado por auditoria humana externa. O detector automático de órfãs jamais poderia tê-lo encontrado — a condição é insatisfazível por construção.**

## F-04 · O ledger inteiro está ancorado na granularidade errada

Esta é a descoberta mais grave desta análise.

| Medição no ledger da B1 | Valor |
|---|---|
| Entradas | 236 |
| Entradas cuja `trecho_ancora` é uma **linha-lote bibliográfica** | **236 (100%)** |
| Entradas cuja `citacao_literal` é um **token** (`ZDILAR_2000[TAG]`) e não uma citação | **221 (94%)** |
| Entradas cuja âncora contém uma citação `(Autor, ANO)` | **0** |

O framework validou "236/236 âncoras literais, 0 ERRO" — e estava tecnicamente **correto**: linhas-lote são texto literal do arquivo. Só que não são afirmações científicas. O ledger, que deveria registrar *por que cada afirmação entrou*, nunca apontou para nenhuma afirmação.

**Consequência:** o "0 ERRO" que sustentou a aprovação de todas as rodadas atesta que rodapés bibliográficos existem. Não atesta nada sobre o conteúdo científico.

## F-05 · Ninguém validava a âncora dos vínculos

`validar_auditoria.py` valida a âncora do **ledger**. `gate_script.py` verifica apenas que a âncora do **vínculo** é *não vazia*. Resultado: 159 âncoras de vínculo não literais existiram por rodadas sem detecção. A própria casa reconheceu isso no `decisoes_B1.md`: *"o framework valida âncora do LEDGER, não dos vínculos"*.

Foi essa lacuna que permitiu o fechamento aparente do R8 com 16 âncoras apontando para rodapé.

## F-06 · Nenhum portão compara camadas entre si

Não existe, em nenhuma ferramenta, uma verificação de que `achado_central_molecular` (ficha), `g3_notas` (vínculo), `citacao_literal` (ledger) e a prosa canônica **dizem a mesma coisa**. Por isso a correção do GRAVE AUD-027 pôde ser aplicada na prosa e não na ficha, deixando o erro vivo na camada que o motor lê — e nenhum indicador piscou.

## F-07 · O G3 é declarativo no vínculo

O ledger exige `verificacao.abstract_ou_trecho` para decidir. O **vínculo** — que é o que o motor consome — aceita `status_auditoria: CONFIRMADO` sem nenhum campo que carregue o texto da fonte. AUD-026 e AUD-027 eram exatamente isto: `[VERIFICADO]` na prosa, `CONFIRMADO` no vínculo, e nenhum campo em lugar nenhum contendo a frase do abstract que teria exposto a inversão de direção.

> **Regra estrutural violada:** um selo de verificação sem o material que o justifica é uma opinião com aparência de dado.

## F-08 · Docstring divergente da implementação

A docstring do `gate_script.py` prometia verificar *"100% das frases declarativas da Canônica com verification_status"* e *"zero citação sem vínculo"*. O código não faz nenhuma das duas. Quem lê a documentação acredita ter cobertura que não existe — e para de procurar.

## F-09 · Portão não reproduzível fora da máquina do autor

`checklist_entrega.py` linhas 43–44 apontavam para `/home/user/…` em caminho absoluto. Em qualquer outra máquina o checklist reporta 2 falhas espúrias. Um portão que só roda em uma máquina não é auditável por terceiro — o que é a razão de existir do portão.

## F-10 · Ausências puras (nunca houve regra)

| O que não existe | Erro real que passou |
|---|---|
| Sincronia manifesto × canônica | AUD-037, AUD-056 (4 campos divergentes) |
| Claim quantitativo exige referência | AUD-031, AUD-051 ("27% / OR 1,46" sem ficha) |
| Cobertura de `claim_id` | AUD-036 (46/273 sem claim_id) |
| Âncora deve estar em prosa, não em rodapé | AUD-032/050 |
| Âncora deve ser sítio único | risco latente (hoje 0 ocorrências) |
| Bloco de classificação exige declaração de não-validação | AUD-052 |
| Hash da canônica registrado | edição fora de trilha indetectável |
| Separar deriva tipográfica de deriva de palavra | AUD-058 (35 itens mandados a humano sem necessidade) |

---

# PARTE II — O QUE FOI CORRIGIDO

## 1. Portão novo: `validar_coerencia_camadas.py` (P-8)

Criado para cobrir exatamente a classe de erro que escapava. Quatorze regras:

| Regra | O que impede | Erro histórico que teria pego |
|---|---|---|
| **V-01** | âncora de vínculo não literal, separando deriva **tipográfica** de **lexical** | AT-02/13, AUD-058 |
| **V-02** | âncora apontando para linha-lote, tabela ou título | AUD-032, AUD-050 |
| **V-03** | âncora ambígua (mais de um sítio) | latente |
| **V-04** | integridade referencial **nos dois sentidos** | AUD-032 |
| **V-05** | citação de prosa sem ficha, **com a cobertura medida e impressa** | AUD-038, AUD-059 |
| **V-06** | correção aplicada na prosa e não propagada às camadas | AUD-027/049, AUD-029, AUD-030 |
| **V-07** | manifesto dessincronizado da canônica | AUD-037, AUD-056, AUD-057 |
| **V-08** | claim quantitativo sem âncora de vínculo | AUD-031, AUD-051 |
| **V-09** | cobertura de `claim_id` abaixo do limite | AUD-036 |
| **V-10** | `citacao_literal` degradada a token | F-04 |
| **V-11** | corte numérico / posologia no corpo (P20) | AUD-031 |
| **V-12** | bloco de classificação sem declaração de não-validação | AUD-052 (parcial) |
| **V-13** | hash da canônica × registrado no manifesto | edição fora de trilha |
| **V-14** | divergência docstring × implementação | F-08 |

**Princípio de projeto:** o P-8 não julga verdade científica — isso é do G3 e da revisão humana. Ele garante que, uma vez decidido, a decisão esteja escrita **de forma idêntica em todas as camadas que o motor lê**, e que nenhuma afirmação chegue ao motor sem lastro localizável. Erro de ciência ele não pega; erro de propagação, de deriva e de lastro ausente, pega todos.

**Resultado na B1 V5, antes de qualquer reparo:**

```
Portões antigos:  GATE APROVADO · 0 ERRO · checklist 41/41
Portão P-8     :  24 ERRO(S), 60 AVISO(S)
```

Cuidado tomado: os 3 primeiros erros de V-05 eram **falso positivo meu** (citações de dois autores, "Perry & Teeling", cuja ficha usa só o primeiro sobrenome). Corrigi o matcher antes de prosseguir. Um portão que grita em vão treina a equipe a ignorá-lo — é pior que portão nenhum. Após a correção, V-05 aponta **exatamente um** item, que é o erro real do Hafizi.

## 2. Reparos aplicados: `reparo_coerencia_2026-09-13.py`

Executado com backup datado, trilha JSON (`producao/15_reparo_coerencia_2026-09-13.json`) e **zero linha da canônica alterada** (sha256 conferido antes e depois: `3c6dda4d…` idêntico).

| Reparo | Condição | Resultado |
|---|---|---|
| **R-01** | C1 / AUD-049 | 4 campos propagados: `REF_COMAI_2022` e `REF_ENACHE_2019` (fichas), `VINC_B1_0219` e `VINC_B1_0247` (notas g3) |
| **R-02** | C2 / AUD-050 | **12 de 16** vínculos re-ancorados da linha-lote para a frase de prosa, com `claim_id` derivado do marcador `(BLOCOxx.yyy)` da subseção |
| **R-05** | C6 / AUD-058 | **34 de 35** âncoras tipográficas reparadas deterministicamente |
| **R-06** | C5 / AUD-056/057 | manifesto sincronizado: corte 2026-09-03→**2026-09-04**, `related_entities` 12→**15**, `clinical_domains` alinhado, placeholders resolvidos, **sha256 da canônica registrado** |
| **R-07** | AUD-053 | 0 de 236 — impossível derivar: a âncora do ledger não contém citação (ver F-04) |

**Resultado depois dos reparos:**

```
Portão P-8 :  24 ERRO → 6 ERRO   ·   60 AVISO → 24 AVISO
Portões antigos: continuam verdes (gate APROVADO · 0 ERRO · 41/41)
```

Os 6 erros que sobram são, deliberadamente, os que **não podem ser resolvidos por máquina sem inventar**:
- 4 vínculos (`0261` Han, `0262` Huang, `0265` Li, `0266` Mehta) têm 2–3 frases de prosa candidatas — sobrenome comum. O script recusou-se a escolher e mandou para fila humana. **Esse é o comportamento correto.**
- `VINC_B1_0175` (Steiner) ancorado em rodapé desde antes do R8.
- `(Hafizi, 2007)` sem ficha — o ID diz 2005.

## 3. Correções nas ferramentas antigas

- **`checklist_entrega.py`** — caminho absoluto substituído por resolução a partir do próprio script. Confirmado: **41/41 sem o atalho `/home/user`**.
- **`gate_script.py`** — docstring reescrita para descrever o que o código faz, com uma seção explícita **"COBERTURA QUE ESTE PORTÃO NÃO TEM"** apontando para o P-8.

## 4. Causa-raiz do erro do Hafizi, corrigida na origem

O campo era `revista_ano: "British journal of hospital medicine (London, England : 2005) (2007)"`. O parser extraiu **2005 do nome do periódico**. Não é um erro de digitação: é um bug de extração que pode ter contaminado B2–B16. **Ação recomendada:** varredura de `revista_ano` com `(` … `: ANO)` no título em todas as 16 bibliotecas antes do próximo ciclo.

## 5. O que ficou fora, e por quê

| Pendência | Por que não foi feito por script |
|---|---|
| **C3 / AUD-051** — catalogar Osimo 2019 (PMID 31258105) | Entrada de referência nova exige rito **[AT]** (regra zero-citação-nova na consolidação). Deixei a ficha pronta e verificada em `PROPOSTA_AT_OSIMO_2019.json`, com a correção de prosa proposta e as 6 ações obrigatórias do [AT]. Verifiquei os números na fonte: 27% (IC 21–34%, 30 estudos) e OR 1,46 (IC 1,22–1,75, 17 estudos). |
| **C4 / AUD-052** — BLOCO_11.4 | Declarar não-validação e desfazer a circularidade do Critério C é **decisão do autor científico**, não de auditor nem de script. |
| **F-04** — reancoragem do ledger | Reancorar 236 entradas na frase correta é uma migração de esquema. Precisa de decisão sobre o modelo-alvo (ver Lacuna L-03). |

---

# PARTE III — LACUNAS DAS FERRAMENTAS FRENTE À FILOSOFIA DO PROJETO

Confrontei a Filosofia com o ferramental existente. A Filosofia promete: **tríade (Biblioteca + Narrativa Transversal + JSON Modular) para 146 IDs oficiais**, **ontologia**, **motor clínico automático**, **sem IA interna em tempo de execução**, com **toda afirmação rastreável**.

O ferramental atual cobre **um terço de um dos três artefatos, para 16 dos 146 IDs**. Segue o que falta, em ordem de bloqueio.

## Bloqueiam o piloto (precisam existir antes do trio B1)

**L-01 · Não existe especificação da Narrativa Transversal.**
Nenhum arquivo do workspace define o que é uma NT: schema, campos, regras de derivação, o que pode e não pode acrescentar. A Filosofia diz que ela "conecta domínios de forma biologicamente coerente" — isso não é especificação executável. Falta: `SCHEMA-NT v1.0` + `PROMPT DE GERAÇÃO DE NT` + **portão de não-elevação epistemológica** (a NT não pode transformar "pré-clínico" em "clínico"; hoje nada impede).

**L-02 · Não existe especificação do JSON Modular.**
Os JSONs que existem (`Evidencias/`, ledger, vínculos) são *artefatos de auditoria da biblioteca*, não a representação computável que o motor consome. Falta: `SCHEMA-JSON-MODULAR v1.0`, o gerador determinístico Biblioteca→JSON, e o **portão de round-trip** (o JSON tem de reproduzir a semântica da biblioteca sem perder incerteza).

**L-03 · O modelo de ancoragem precisa de decisão antes de escalar.**
Hoje há três granularidades convivendo: âncora de prosa (vínculos), âncora de linha-lote (ledger, 100%) e claim_id (46/273 vazios). Para 146 IDs isso multiplica por nove. Falta: **um contrato único de ancoragem** — a unidade atômica é a frase; toda camada aponta para a mesma frase pelo mesmo identificador estável.

**L-04 · Não existe a pasta de ontologia nem qualquer arquivo dela.**
A Filosofia e o motor dependem dela; o workspace tem `1º IDS_OFICIAIS.md` (uma lista) e nada mais. Falta: vocabulário controlado versionado, relações entre entidades (mecanismo↔biomarcador↔exame↔intervenção), cardinalidade, e o **registro dos 146 IDs como dado**, não como prosa em markdown.

**L-05 · Não existe contrato do Motor Clínico.**
"A plataforma não terá IA interna, será automático" é a decisão arquitetural mais importante do projeto — e não há um documento que diga: quais campos o motor lê, com que precedência, como resolve conflito entre mecanismos, como combina evidência de força diferente, e o que ele faz quando falta dado. Sem isso, cada biblioteca é escrita para um consumidor imaginário. **Este é o maior risco do projeto hoje.**

**L-06 · Não existe regra de precedência entre bibliotecas.**
A Filosofia manda integrar 16 mecanismos e ainda intervenções, exames, nutrição, psicoterapia. Quando B1 e B9 apontam direções opostas, quem vence? Sem regra declarada, o motor produzirá saída não determinística — o que contraria "automático" e "rastreável".

**L-07 · Não existe portão de segurança para a saída do motor.**
Todos os portões atuais olham para o *insumo* (a biblioteca). Nenhum olha para o *produto* (o relatório ao profissional). A hierarquia que o próprio projeto declara — risco vital → restrição legal → contraindicação → interação → eficácia → sugestão — não está implementada em lugar nenhum.

## Bloqueiam a escala para 146 IDs

**L-08 · Os scripts são por biblioteca, não por série.**
Existem 275 scripts, muitos duplicados por biblioteca (`B4_json_apply.py`, `B5_json_apply.py`, `B6_json_apply.py`…). Isso é insustentável em 146. Falta: **uma biblioteca de funções única, parametrizada por ID**, com os scripts por biblioteca reduzidos a configuração.

**L-09 · Não há CI: os portões são invocados à mão.**
Daí o `/home/user` hardcoded ter sobrevivido, e daí "rodei os portões" ser uma afirmação sem prova. Falta: execução automática dos 4 portões a cada alteração, com relatório versionado e **bloqueio de merge**.

**L-10 · Não há teste de regressão dos próprios portões.**
Nenhuma ferramenta tem teste. Foi por isso que uma regex de 7% de cobertura passou despercebida. Falta: um conjunto de **artefatos-armadilha** (com erro conhecido plantado) que todo portão precisa detectar; se um portão deixa de pegar a armadilha, o próprio portão reprova. **Sugiro usar AUD-026/027/032 como as três primeiras armadilhas** — são erros reais, com correção conhecida.

**L-11 · Não existe versionamento semântico nem contrato de compatibilidade.**
"V4.1 → V5" é convenção informal. Com 146 IDs × 3 artefatos + motor, é preciso declarar o que é mudança compatível e o que quebra o consumidor.

**L-12 · Não existe orçamento de revisão humana.**
O P-6 (segunda verificação cega) é a única barreira real contra erro científico, e está declarado como pendente. Na B1 são 108 vínculos de alto risco. Em 146 IDs, na mesma proporção, são cerca de **10 mil**. Sem uma política de amostragem estratificada e um critério de suficiência, o P-6 nunca fechará e **toda a plataforma permanecerá PROVISÓRIA para sempre**.

## Melhorias de qualidade (não bloqueiam, mas evitam retrabalho)

**L-13 · Falta campo de citação verbatim da fonte.** Se cada vínculo carregasse `achado_verbatim_fonte` (a frase do abstract, entre aspas, com o PMID), AUD-026 e AUD-027 teriam sido detectáveis por máquina — bastaria comparar a direção declarada na prosa com a frase da fonte. **É a mudança de esquema de maior retorno do projeto inteiro.**

**L-14 · Falta declarar população/pooling no vínculo.** O §2.10 usa uma meta que agrupa unipolares e bipolares sem sinalizar; o §5.2 ao lado distingue os dois. Um campo `populacao_agrupada` resolveria por portão.

**L-15 · Falta política de aliases.** `REF_HAFIZI_2005` para artigo de 2007 mostra que o ID codifica um dado mutável (o ano). IDs devem ser opacos e estáveis, com autor/ano em campos.

**L-16 · Falta o registro de decisões arquiteturais como dado.** O `CONTRATO DE GERAÇÃO` é prosa; os portões implementam algumas regras (P12/P20) de forma dispersa. Deveria ser uma tabela legível por máquina, com cada regra ligada ao portão que a verifica — e regra sem portão deveria ser um erro declarado.

---

# PARTE IV — PLANO PARA O TRIO PILOTO

A estratégia de validar um trio antes de replicar está certa. Ajuste que recomendo: **a ordem que você propôs constrói o motor por último, e é justamente o motor que define o que os três artefatos precisam conter.** Sem o contrato do motor (L-05), a NT e o JSON da B1 serão escritos no escuro e provavelmente refeitos.

Sequência sugerida:

| Etapa | Entrega | Por que nesta ordem |
|---|---|---|
| **0** | Fechar as 4 condições bloqueantes da B1 (C1–C4) | Não se valida arquitetura sobre base com GRAVE aberto |
| **1** | **Contrato do Motor Clínico** (L-05) + regra de precedência (L-06) | Define o consumidor. Tudo depois é derivado dele |
| **2** | Ontologia mínima: 146 IDs como dado + relações (L-04) | NT e JSON referenciam a ontologia |
| **3** | `SCHEMA-NT` e `SCHEMA-JSON-MODULAR` (L-01, L-02) + contrato de ancoragem (L-03) | Especificação antes de geração |
| **4** | Gerar **NT-B1** e **JSON-B1** a partir da B1 V5 corrigida | O trio piloto de verdade |
| **5** | Portão de round-trip + portão de não-elevação epistemológica | Provar que a derivação não cria ciência nova |
| **6** | Bibliotecas mínimas de Exames, Intervenções e Suplementos (recorte só do necessário para B1) | Menor superfície possível para testar o motor |
| **7** | **Teste do motor com caso clínico sintético**, saída auditada frase a frase | O teste real da arquitetura |
| **8** | CI + armadilhas de regressão (L-09, L-10) + refatoração dos scripts para série (L-08) | Só então replicar para os 145 restantes |

**Marco de decisão (gate de replicação):** só replicar quando um caso sintético atravessar anamnese → mecanismos → sugestões → relatório com **100% das frases do relatório rastreáveis até uma frase de biblioteca canônica**, e com os portões P-5, P-8 e o de saída verdes.

---

## Nota de método

Nada neste documento foi aceito por declaração. Cada número foi medido nos arquivos: 280 citações, 7,2% de cobertura, 0 âncoras no formato esperado, 236/236 do ledger em linha-lote, 24→6 erros no P-8, sha256 idêntico antes e depois. Onde não pude verificar, está escrito. Onde errei durante a análise — os 3 falsos positivos do matcher de citação — corrigi a ferramenta antes de seguir, e o registro fica aqui.
