# ROTEIRO DE TRABALHO DA PLATAFORMA - 27.09.2026

**Documento operacional de acompanhamento do desenvolvimento da plataforma**

**Status:** documento de trabalho
**Atualização:** 27-09-2026

**Objetivo:** organizar a sequência de desenvolvimento, validação, integração e teste da plataforma antes da replicação para os demais IDs oficiais.

---

# 1. OBJETIVO DO ROTEIRO

O objetivo deste roteiro é organizar a construção progressiva da plataforma, transformando o conhecimento científico estruturado em um sistema integrado capaz de:

* receber uma anamnese;
* consultar conhecimento estruturado;
* relacionar mecanismos, suplementos, intervenções, cenários e exames;
* realizar interpretação contextualizada;
* produzir sugestões compatíveis com os limites do sistema;
* explicar as relações utilizadas;
* produzir um Laudo Técnico de Apoio;
* preservar a rastreabilidade da origem das informações utilizadas.

A primeira finalidade do projeto é construir e testar um **vertical slice completo da plataforma**, utilizando a **Biblioteca Canônica B1 — Neuroinflamação** como eixo inicial.

Somente depois que esse circuito integrado estiver testado e auditado deverá ocorrer a replicação do modelo para os demais mecanismos e IDs oficiais.

O fluxo geral é:

```text
DESCOBERTA BIBLIOGRÁFICA
        ↓
CONSOLIDAÇÃO DO CORPUS
        ↓
VALIDAÇÃO CIENTÍFICA
        ↓
FECHAMENTO DO CLAIM
        ↓
EVIDÊNCIAS / BIBLIOGRAFIA
        ↓
N1 / N2
        ↓
INTEGRAÇÃO NAS CAMADAS POSTERIORES
```

A descoberta bibliográfica pode utilizar ferramentas diferentes.

A validação científica, entretanto, segue o protocolo específico vigente, tendo a **fonte primária como árbitro factual**.

---

# 2. DOIS GRUPOS DE TRABALHO

O projeto está organizado em dois grupos com funções diferentes.

## GRUPO 1 — ENGENHARIA, ARQUITETURA E CONTRATOS

Participantes:

* **Comentador — ChatGPT**
* **Arena-Casa**
* **Auditor-Mestre**
* **Auditor-Estrutura**

Este grupo trabalha sobre:

* arquitetura;
* contratos;
* schemas;
* ferramentas;
* estruturas de dados;
* materializadores;
* fluxos;
* integração;
* ontologia;
* JSONs;
* contrato do Motor;
* rastreabilidade;
* coerência estrutural.

### Funções

**Arena-Casa**

Atua como bancada de confronto, análise e verificação operacional.

**Auditor-Estrutura**

Atua sobre:

* estrutura;
* schemas;
* compatibilidade;
* materialização;
* coerência técnica.

**Auditor-Mestre**

Atua sobre:

* contratos;
* governança;
* processo;
* execução;
* auditoria;
* aderência ao rito.

**Comentador — ChatGPT**

Atua como apoio analítico, consolidação, comparação e organização das informações necessárias à execução.

A convergência do Grupo 1 não possui limite artificial de duas rodadas.

Análises, auditorias, contraposições, correções e novas verificações podem ser repetidas até que a solução esteja tecnicamente consistente e implementável.

---

# 3. GRUPO 2 — VALIDAÇÃO DOS CLAIMS CLÍNICOS

O Grupo 2 é responsável pela validação científica dos claims.

Participantes:

* **IA1 — ChatGPT dedicado**
* **IA2 — Arena dedicado**
* **IA3 — Claude dedicado**

As três IAs trabalham de forma independente na análise científica.

A IA3 produz parecer independente, mas não fecha o claim isoladamente.

Depois da comparação:

```text
IA1
IA2
IA3
   ↓
COMPARAÇÃO
   ↓
RETORNO ÀS IAs 1 E 2
   ↓
FECHAMENTO CONJUNTO
```

Quando houver divergência factual, a resolução deve ocorrer pela consulta à **fonte primária**, e não por votação ou contagem de opiniões.

As limitações, ressalvas e incertezas relevantes devem ser preservadas.

Este grupo atua sobre:

* descoberta e recuperação bibliográfica;
* consolidação do corpus;
* PubMed;
* G1;
* G2;
* G3;
* leitura de fonte primária;
* resolução de divergências;
* fechamento dos claims;
* produção do Claim Kit.

A independência epistemológica é requisito do piloto oficial e não do ensaio operacional pré-piloto.

---

# 4. ENSAIO OPERACIONAL PRÉ-PILOTO

Antes do piloto oficial do **B1.SM02.014**, foi realizado um ensaio operacional com o grupo que participou da construção do sistema:

* ChatGPT / Comentador;
* Arena-Casa;
* Auditor-Estrutura;
* Auditor-Mestre.

O objetivo desse ensaio foi testar a **máquina operacional**, e não medir independência epistemológica.

O ensaio verificou, entre outros pontos:

* integridade do pacote;
* leitura dos documentos;
* compreensão das instruções;
* execução de G1;
* execução de G2;
* execução de G3;
* separação entre análise e fechamento;
* rastreabilidade;
* transições de etapa;
* compatibilidade com os schemas;
* distinção entre execução e materialização;
* identificação de problemas operacionais.

O ensaio do `.014` foi **realizado e encerrado**.

Ele possui registro operacional próprio e:

* não altera o corpus oficial;
* não altera o estado oficial do `.014`;
* não substitui o piloto oficial;
* não substitui a validação científica;
* não encerra o protocolo epistemológico do piloto;
* não transforma seus participantes em avaliadores epistemicamente independentes.

Problemas puramente operacionais permanecem registrados como problemas operacionais.

Problemas normativos devem retornar ao respectivo processo formal de alteração e aprovação.

---

# 5. RELAÇÃO ENTRE OS DOIS GRUPOS

A validação científica e a engenharia da plataforma permanecem separadas.

O fluxo conceitual é:

```text
GRUPO 2
VALIDAÇÃO DO CLAIM
        ↓
EVIDÊNCIAS / BIBLIOGRAFIA
        ↓
N1 / N2
        ↓
CAMADAS POSTERIORES
        ↓
GRUPO 1
ESTRUTURA / INTEGRAÇÃO
        ↓
NT
        ↓
ONTOLOGIA / GRAFO
        ↓
JSONs MODULARES
        ↓
MOTOR
```

O Grupo 1 não decide a verdade científica de um claim.

O Grupo 2 não substitui a engenharia, os contratos ou os schemas do sistema.

A distinção entre:

* Claim;
* N1;
* N2;

deve permanecer preservada em todas as camadas.

---

# 6. DESCOBERTA BIBLIOGRÁFICA E VALIDAÇÃO CIENTÍFICA

É necessário distinguir explicitamente **descoberta** de **validação**.

## Descoberta

A descoberta pode utilizar:

* Consensus;
* PubMed;
* ferramentas de recuperação de texto completo;
* mecanismos auxiliares de localização de fontes;
* agentes auxiliares de busca;
* outras ferramentas de descoberta bibliográfica.

Essas ferramentas podem produzir conjuntos amplos de candidatos.

O fluxo é:

```text
CLAIM CANÔNICO
      ↓
DESCOBERTA AMPLA
      ↓
LISTAS DE ARTIGOS
      ↓
CONSOLIDAÇÃO
      ↓
DEDUPLICAÇÃO
      ↓
CORPUS DE TRABALHO
      ↓
CONGELAMENTO DO CORPUS DA RODADA
```

A lista consolidada é um **corpus candidato**.

Ela não constitui, por si só, validação científica.

## Validação

Depois do corpus estar definido:

```text
CORPUS
   ↓
IA1
IA2
IA3
   ↓
FONTE PRIMÁRIA
   ↓
G1 / G2 / G3
   ↓
COMPARAÇÃO
   ↓
FECHAMENTO
```

A fonte primária continua sendo o árbitro factual.

### Execução do protocolo G1/G2/G3

A execução do protocolo ocorre de forma contínua dentro de cada estágio.

**G1** verifica cada referência, confirma a identificação do artigo e procura o PMID quando necessário.

A conclusão de G1 **não é um ponto de parada**.

A IA deve prosseguir imediatamente para G2.

**G2** avalia se cada artigo confirmado pode ser utilizado para analisar o claim, considerando, entre outros aspectos:

* relevância;
* população;
* doença;
* espécie;
* desenho;
* comparador;
* escopo;
* pertinência ao claim.

O primeiro ponto de parada ocorre somente depois de **G1 + G2**, com entrega da Lista G2.

As listas G2 são então submetidas ao confronto entre as IAs.

Após o congelamento da lista elegível, inicia-se G3.

**G3** avalia se cada artigo elegível sustenta o claim clínico.

Quando necessário, deve ser consultado o texto completo.

A leitura deve ser registrada segundo o nível efetivamente realizado:

```text
texto_completo
abstract
nao_lido
```

`nao_lido` deve permanecer explicitamente identificado e não pode ser tratado como artigo efetivamente analisado.

O segundo ponto de parada ocorre depois da conclusão de G3 e entrega do respectivo parecer/tabela.

Somente depois do confronto entre os resultados de G3 ocorre o fechamento.

---

# 6.1. VALIDAÇÃO DOS DOCUMENTOS E FERRAMENTAS

Além da validação dos claims científicos, o projeto adota uma regra transversal para os documentos utilizados na operação da plataforma.

**Cada documento envolvido na execução do sistema — inclusive ferramentas de geração e documentos operacionais — deve passar pelo crivo das três IAs antes de ser considerado vigente e utilizável na operação correspondente.**

O processo ocorre documento por documento.

De forma geral:

```text
DOCUMENTO / FERRAMENTA
        ↓
IA1
        ↓
IA2
        ↓
IA3
        ↓
COMPARAÇÃO
        ↓
RESOLUÇÃO DAS DIVERGÊNCIAS
        ↓
FECHAMENTO
        ↓
VIGÊNCIA / USO OPERACIONAL
```

A existência física de um arquivo não equivale à sua vigência operacional.

Um documento pode existir no projeto e ainda assim permanecer:

```text
EXISTENTE
≠
VALIDADO
≠
VIGENTE
≠
AUTORIZADO PARA USO
```

Antes de um teste integrado, deve ser verificado se as ferramentas e os documentos necessários:

* são os documentos corretos;
* estão na versão correta;
* possuem vigência;
* foram aprovados pelo rito aplicável;
* não foram substituídos por versão posterior.

Essa regra aplica-se especialmente aos documentos que participam diretamente da execução, incluindo ferramentas de geração, instrumentos operacionais e documentação utilizada pelo Motor ou pela preparação dos dados.

---

# 7. COMO O PROJETO CHEGOU À ESTRUTURA ATUAL

O desenvolvimento ocorreu progressivamente.

Inicialmente, o foco estava na análise científica da **Biblioteca Canônica B1 — Neuroinflamação**.

Depois surgiu a necessidade de transformar o conhecimento canônico em unidades narrativas reutilizáveis.

Isso levou ao desenvolvimento das **Narrativas Transversais (NT)**.

Em seguida, tornou-se necessário estruturar as relações entre entidades, mecanismos e conhecimentos.

Isso levou à **Ontologia / Grafo**.

Depois surgiu a necessidade de representar essas estruturas de forma computável.

Isso levou aos **JSONs Modulares**.

Paralelamente, surgiu a necessidade de separar o pipeline de validação científica dos mecanismos de representação e consumo.

Isso levou à consolidação do:

* Claim Kit;
* L-05 N1/N2;
* Contrato de Saída;
* Schema-Claim;
* COMO EXECUTAR.

Finalmente, tornou-se necessário definir previamente como o Motor Clínico consumirá as estruturas.

Isso levou ao desenvolvimento do **Contrato do Motor Clínico**.

O percurso passou a ser:

```text
B1 — ANÁLISE CIENTÍFICA
        ↓
BIBLIOTECA / CONHECIMENTO
        ↓
CLAIMS CLÍNICOS
        ↓
CLAIM KIT
        ↓
EVIDÊNCIAS / BIBLIOGRAFIA
        ↓
N1 / N2
        ↓
NARRATIVAS TRANSVERSAIS
        ↓
ONTOLOGIA / GRAFO
        ↓
JSONs MODULARES
        ↓
CONTRATO DO MOTOR
        ↓
MOTOR CLÍNICO
```

Essa sequência representa a descoberta progressiva dos requisitos necessários para manter o sistema coerente.

---

# 8. ESTRATÉGIA PRINCIPAL: VERTICAL SLICE

O projeto não deve produzir todos os demais IDs oficiais em escala antes de testar o funcionamento integrado.

Primeiro será construído um **vertical slice completo**, utilizando B1 como eixo.

O objetivo é provar que todas as camadas necessárias conseguem trabalhar juntas.

```text
                 B1
                  │
        ┌─────────┴─────────┐
        │ VERTICAL SLICE    │
        │ COMPLETO TESTADO  │
        └─────────┬─────────┘
                  │
        ┌─────────▼─────────┐
        │ MODELO REPLICÁVEL │
        └─────────┬─────────┘
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
      B2         B3         B4 ...
       │          │          │
       ▼          ▼          ▼
    mesmo      mesmo       mesmo
    contrato   contrato    contrato
```

B1 será, portanto, o **primeiro mecanismo utilizado para testar o circuito completo da plataforma**.

---

# 9. PRIMEIRO CONJUNTO INTEGRADO

Para testar o circuito completo, B1 não será trabalhado isoladamente.

Será necessário construir o conjunto de conhecimentos relacionados à neuroinflamação.

### Bibliotecas

* Biblioteca Canônica B1 — Neuroinflamação;
* Biblioteca de Suplementos relacionados a B1;
* Biblioteca de Intervenções relacionadas a B1;
* Biblioteca de Cenários relacionados a B1;
* Biblioteca de Exames relacionados a B1.

### Narrativas

* NT-B1;
* narrativas dos suplementos relacionados;
* narrativas das intervenções relacionadas;
* narrativas dos cenários relacionados;
* narrativas dos exames relacionados.

### Estrutura

* Ontologia/Grafo correspondente;
* JSONs Modulares correspondentes;
* vínculos entre mecanismos, suplementos, intervenções, cenários e exames.

### Claims clínicos

Os claims clínicos validados pelo Grupo 2 entram no fluxo:

```text
CLAIM FECHADO
      ↓
EVIDÊNCIAS / BIBLIOGRAFIA
      ↓
N1
      ↓
N2
```

Eles **não entram na Biblioteca Canônica de mecanismos como se fossem afirmações mecanísticas do mesmo tipo**.

Sua utilização nas camadas posteriores depende dos respectivos contratos e da arquitetura vigente.

---

# 10. O CIRCUITO COMPLETO A SER TESTADO

Quando o conjunto B1 estiver preparado **e os documentos e ferramentas necessários estiverem previamente validados e vigentes**, o circuito será:

```text
                         ANAMNESE
                            │
                            ▼
                     ┌─────────────┐
                     │   MOTOR     │
                     │   CLÍNICO   │
                     └──────┬──────┘
                            │
                            ▼
                  CONSULTA AO CONHECIMENTO
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
       FLUXO CANÔNICO              PASTA DE ATUALIZAÇÃO
              │                           │
              ▼                           │
     Bibliotecas / Evidências             │
     / NT / Vínculos /                    │
     Ontologia / Grafo / JSONs            │
              │                           │
              └─────────────┬─────────────┘
                            │
                            ▼
                     MOTOR CLÍNICO
                            │
                            ▼
                  INTERPRETAÇÃO
                  CONTEXTUALIZADA
                            │
                            ▼
                       SUGESTÕES
                            │
                            ▼
                  EXPLICAÇÃO NARRATIVA
                            │
                            ▼
                  LAUDO TÉCNICO DE APOIO
```

O fluxo canônico e a Pasta de Atualização permanecem segregados até o Motor.

Todo item recuperado deve preservar sua proveniência.

---

# 11. ENTRADA DO SISTEMA

A entrada inicial do teste será a **anamnese**.

Os arquivos de anamnese já existentes constituem o acervo disponível, porém **não serão automaticamente considerados aptos para uso no teste integrado**.

Cada documento necessário da Anamnese deverá passar pelo crivo das três IAs, individualmente, antes de receber vigência para uso operacional.

Assim:

```text
ANAMNESE EXISTENTE
        ↓
VALIDAÇÃO DOCUMENTAL
        ↓
FECHAMENTO
        ↓
VIGÊNCIA
        ↓
USO NO TESTE INTEGRADO
```

Enquanto esse processo não for concluído, o documento permanece disponível como material existente, mas não como instrumento operacional vigente.

Também poderão ser criados **casos clínicos simulados controlados**, especificamente para testar diferentes caminhos do Motor.

Os casos simulados não terão finalidade de estabelecer eficácia clínica.

Sua função será testar:

* comportamento;
* recuperação;
* integração;
* rastreabilidade;
* regras;
* segurança;
* consistência das saídas.

---

# 12. O QUE O TESTE B1 DEVE RESPONDER

O teste não deve perguntar somente se cada arquivo está correto isoladamente.

Deve verificar se:

1. a anamnese é corretamente interpretada;
2. o Motor identifica os conhecimentos pertinentes;
3. as relações ontológicas funcionam;
4. os JSONs são recuperados corretamente;
5. as NTs preservam o significado científico;
6. os claims permanecem rastreáveis;
7. as evidências permanecem vinculadas às afirmações;
8. as sugestões respeitam as regras do sistema;
9. não ocorre elevação epistemológica;
10. as relações entre mecanismo, suplemento, intervenção, cenário e exame funcionam;
11. o Motor consegue combinar informações de diferentes domínios;
12. a explicação narrativa corresponde ao raciocínio estruturado;
13. o Laudo Técnico de Apoio é produzido corretamente;
14. a origem das informações pode ser rastreada;
15. a distinção `origem_conhecimento = canonico | atualizacao` é preservada quando aplicável;
16. as regras de segurança e limites do sistema são respeitadas;
17. nenhuma camada inventa informação ausente da camada de origem;
18. divergências entre fontes e relações permanecem explicitamente tratáveis.

---

# 13. TESTE DE PONTA A PONTA

O verdadeiro teste da plataforma será:

```text
CASO SIMULADO
      ↓
ANAMNESE VALIDADA
      ↓
MOTOR
      ↓
RECUPERAÇÃO DO CONHECIMENTO
      ↓
B1 + SUPLEMENTOS + INTERVENÇÕES
+ CENÁRIOS + EXAMES
      ↓
ONTOLOGIA / GRAFO
      ↓
JSONs
      ↓
INTERPRETAÇÃO CONTEXTUALIZADA
      ↓
SUGESTÕES
      ↓
EXPLICAÇÃO NARRATIVA
      ↓
LAUDO TÉCNICO DE APOIO
      ↓
AUDITORIA DO RESULTADO
```

Somente depois desse teste será possível avaliar se a arquitetura funciona como uma **plataforma integrada**, e não apenas como um conjunto de documentos tecnicamente corretos.

---

# 14. CRITÉRIO PARA A REPLICAÇÃO

A produção dos demais mecanismos e IDs oficiais somente deverá entrar em escala depois que o vertical slice B1 demonstrar:

* funcionamento;
* integração;
* rastreabilidade;
* coerência semântica;
* recuperação correta;
* ausência de falhas estruturais críticas;
* comportamento adequado do Motor;
* capacidade de produzir o resultado esperado;
* possibilidade de reprodução do processo;
* capacidade de auditoria do circuito.

O objetivo é transformar o conjunto B1 em um **modelo replicável**.

Depois:

```text
B1 — VALIDADO COMO VERTICAL SLICE
              ↓
       MODELO REPLICÁVEL
              ↓
      B2 → B3 → B4 → ... → B16
              ↓
      demais domínios
              ↓
       demais IDs oficiais
```

---

# 15. CHECKLIST MESTRE DO PROJETO

| Etapa | Item                                                              | Status                  |
| ----- | ----------------------------------------------------------------- | ----------------------- |
| 1     | Arquitetura Consolidada V2.2                                      | ✅ REALIZADO             |
| 2     | Definição dos dois grupos de trabalho                             | ✅ REALIZADO             |
| 3     | Contratos L-05 / N1 / N2                                          | ✅ BASE VIGENTE          |
| 4     | Contrato L-NT                                                     | 🔄 EM CONSOLIDAÇÃO      |
| 5     | Contrato do Motor Clínico                                         | ⬜ A DESENVOLVER         |
| 6     | Contrato de Saída do Claim Kit rev.2                              | ✅ VIGENTE               |
| 7     | Schema-Claim v1.3 rev.3                                           | ✅ VIGENTE               |
| 8     | COMO EXECUTAR v1.11 rev.2                                         | ✅ VIGENTE               |
| 9     | Protocolo científico dos claims                                   | ✅ INCORPORADO AO v1.11  |
| 10    | Ensaio operacional B1.SM02.014                                    | ✅ REALIZADO E ENCERRADO |
| 11    | Piloto oficial B1.SM02.014                                        | ⬜ PENDENTE              |
| 12    | Claims clínicos B1                                                | 🔄 EM VALIDAÇÃO         |
| 13    | Biblioteca Canônica B1                                            | 🔄 EM CONSOLIDAÇÃO      |
| 14    | Biblioteca de Suplementos — B1                                    | ⬜ PENDENTE              |
| 15    | Biblioteca de Intervenções — B1                                   | ⬜ PENDENTE              |
| 16    | Biblioteca de Cenários — B1                                       | ⬜ PENDENTE              |
| 17    | Biblioteca de Exames — B1                                         | ⬜ PENDENTE              |
| 18    | NT-B1                                                             | ⬜ PENDENTE              |
| 19    | NT dos Suplementos — B1                                           | ⬜ PENDENTE              |
| 20    | NT das Intervenções — B1                                          | ⬜ PENDENTE              |
| 21    | NT dos Cenários — B1                                              | ⬜ PENDENTE              |
| 22    | NT dos Exames — B1                                                | ⬜ PENDENTE              |
| 23    | Ontologia/Grafo — B1                                              | ⬜ PENDENTE              |
| 24    | JSONs Modulares — B1                                              | ⬜ PENDENTE              |
| 25    | Integração dos claims clínicos em Evidências/Bibliografia         | 🔄 EM PREPARAÇÃO        |
| 26    | Primeira materialização N1/N2 do fluxo novo                       | ⬜ PENDENTE              |
| 27    | Acervo de Anamnese existente                                      | ✅ DISPONÍVEL            |
| 28    | Validação documental da Anamnese pelas 3 IAs                      | ⬜ PENDENTE              |
| 29    | Verificação de vigência das ferramentas e documentos operacionais | 🔄 EM EXECUÇÃO CONTÍNUA |
| 30    | Casos simulados de teste                                          | ⬜ PENDENTE              |
| 31    | Integração completa B1                                            | ⬜ PENDENTE              |
| 32    | Teste do Motor Clínico                                            | ⬜ PENDENTE              |
| 33    | Teste ponta a ponta                                               | ⬜ PENDENTE              |
| 34    | Auditoria do circuito completo                                    | ⬜ PENDENTE              |
| 35    | Correção das falhas encontradas                                   | ⬜ PENDENTE              |
| 36    | Reexecução do circuito após correções                             | ⬜ PENDENTE              |
| 37    | Aprovação do vertical slice B1                                    | ⬜ PENDENTE              |
| 38    | Definição do procedimento de replicação                           | ⬜ PENDENTE              |
| 39    | Início da expansão para demais IDs                                | ⬜ PENDENTE              |

---

# 16. MARCOS DE TRABALHO

## MARCO 1 — ENGENHARIA BASE

```text
Arquitetura
   ↓
L-05
   ↓
L-NT
   ↓
Contrato do Motor
   ↓
estruturas prontas para produção
```

**Objetivo:** saber exatamente como o conteúdo deverá nascer e como será consumido.

---

## MARCO 2 — VALIDAÇÃO DOS CLAIMS B1

```text
Claim
 ↓
IA 1 — ChatGPT dedicado
 ↓
IA 2 — Arena dedicado
 ↓
IA 3 — Claude dedicado
 ↓
comparação posterior
 ↓
retorno às IAs 1 e 2
 ↓
fechamento conjunto
 ↓
claim fechado
```

**Objetivo:** produzir claims clínicos cientificamente validados e rastreáveis.

---

## MARCO 3 — ENSAIO OPERACIONAL PRÉ-PILOTO

```text
B1.SM02.014
      ↓
pacote de trabalho
      ↓
ensaio com o grupo que construiu o sistema
      ↓
identificação de problemas operacionais
      ↓
registro
      ↓
ajustes de pacote/instrução, quando aplicável
      ↓
ensaio encerrado
```

**Objetivo:** testar a máquina antes de entregar o piloto oficial à tríade dedicada.

O ensaio não substitui o piloto oficial e não mede independência epistemológica.

O ensaio já foi executado e encerrado.

---

## MARCO 4 — PILOTO OFICIAL DO `.014`

```text
CORPUS CONGELADO
      ↓
IA 1 — ChatGPT dedicado
IA 2 — Arena dedicado
IA 3 — Claude dedicado
      ↓
três análises independentes
      ↓
comparação
      ↓
retorno às IAs 1 e 2
      ↓
fechamento conjunto
```

**Objetivo:** executar o **COMO EXECUTAR v1.11 rev.2** em condições de independência operacional e epistemológica adequadas ao piloto oficial.

---

## MARCO 5 — PRODUÇÃO DO CONJUNTO B1

```text
B1
+
Suplementos
+
Intervenções
+
Cenários
+
Exames
        ↓
Narrativas
        ↓
Ontologia
        ↓
JSONs
```

**Objetivo:** produzir o primeiro conjunto completo de conhecimento relacionado a um mecanismo.

---

## MARCO 6 — INTEGRAÇÃO

```text
Conhecimento
      ↓
NT
      ↓
Ontologia
      ↓
JSON
      ↓
Motor
      ↑
Anamnese validada
```

**Objetivo:** fazer todas as camadas funcionarem juntas.

---

## MARCO 7 — TESTE COMPLETO

```text
CASO
 ↓
ANAMNESE
 ↓
MOTOR
 ↓
CONHECIMENTO
 ↓
INTERPRETAÇÃO
 ↓
SUGESTÕES
 ↓
EXPLICAÇÃO
 ↓
LAUDO
```

**Objetivo:** testar a plataforma como sistema.

---

## MARCO 8 — AUDITORIA E CORREÇÃO

Identificar:

* falhas;
* perdas de informação;
* erros de vínculo;
* problemas de recuperação;
* problemas semânticos;
* problemas nos JSONs;
* problemas do Motor;
* problemas narrativos;
* problemas de rastreabilidade.

Corrigir e repetir o teste.

---

## MARCO 9 — REPLICAÇÃO

Somente após aprovação do vertical slice:

```text
B1
 ↓
MODELO VALIDADO
 ↓
REPLICAÇÃO
 ↓
B2
B3
B4
...
B16
...
demais IDs oficiais
```

---

# 17. PRINCÍPIO CENTRAL DO PROJETO

A plataforma não será considerada pronta porque cada componente individual funciona.

Ela será considerada pronta para expansão quando o **circuito integrado** funcionar.

O objetivo desta primeira fase é, portanto:

> **Construir, integrar, testar e auditar um circuito completo da plataforma utilizando B1 — Neuroinflamação como vertical slice, incluindo claims clínicos validados, Bibliotecas, Narrativas Transversais, Ontologia/Grafo, JSONs Modulares, Motor Clínico e Anamnese previamente validada, antes de replicar o modelo para os demais IDs oficiais.**

O processo de validação científica dos claims e o processo de engenharia da plataforma permanecem separados.

O primeiro não deve substituir o segundo.

O segundo não deve decidir a verdade científica do primeiro.

Da mesma forma, a existência de um documento ou ferramenta não implica automaticamente sua vigência operacional. Documentos e ferramentas envolvidos na execução devem cumprir o crivo de validação aplicável antes de seu uso.

---

# 18. REGRA DE GOVERNANÇA

Nenhum documento deste roteiro substitui os contratos normativos, schemas ou protocolos específicos.

Este documento serve para:

* orientar a sequência de trabalho;
* registrar o estado do projeto;
* mostrar dependências;
* evitar produção fora de ordem;
* permitir que os dois grupos saibam em que etapa o projeto se encontra;
* identificar o próximo trabalho necessário;
* separar ensaio operacional, piloto oficial e produção;
* registrar a dependência entre validação documental, vigência e uso operacional.

As decisões específicas continuam pertencendo ao documento/contrato correspondente.

### Bases normativas vigentes relacionadas ao processo

```text
Contrato de Saída do Claim Kit rev.2
SHA:
841532dad13cd3fea1356c9e23e37067e78876685db52d3c1f2cd8b2a96e535c
        ↓
Schema-Claim v1.3 rev.3
SHA:
28cbc9c76006f485f340da124aa1795833afa56d38e6572a9279d94a88f6b94c
        ↓
COMO EXECUTAR v1.11 rev.2
SHA prefix:
2efc0edd
```

O **COMO EXECUTAR v1.10** é histórico e não é a versão vigente.

O Roteiro apenas organiza a execução do projeto em torno dessas bases.

Nenhuma etapa deste roteiro autoriza alteração silenciosa de contrato, schema, N1 ou N2.

---

# 19. ESTADO ATUAL

## Já consolidado

* Arquitetura Consolidada V2.2;
* separação entre os dois grupos;
* distinção entre Claim, N1 e N2;
* Contrato de Saída do Claim Kit rev.2 vigente;
* Schema-Claim v1.3 rev.3 vigente;
* COMO EXECUTAR v1.11 rev.2 vigente;
* direção Claim Kit → Evidências/Bibliografia → N1/N2;
* distinção entre descoberta bibliográfica e validação científica;
* B1 como primeiro vertical slice;
* acervo de Anamnese existente;
* regra de validação documental pelas três IAs antes da vigência/uso;
* ensaio operacional pré-piloto B1.SM02.014 realizado e encerrado.

## Estado transitório atual

O ensaio operacional do **B1.SM02.014 já foi executado e encerrado**.

O próximo conjunto de trabalhos envolve a preparação das condições para o piloto oficial e, posteriormente, para a integração completa do vertical slice.

Antes do uso da Anamnese e dos demais documentos operacionais no teste integrado, deve ser concluída sua validação documental e verificada sua vigência.

O `.014` não deve ser tratado como se ainda estivesse na etapa de ensaio operacional.

O registro do pré-piloto permanece como registro de execução e aprendizado operacional, sem alterar o estado oficial previamente estabelecido para o `.014`.

## Próximo objetivo operacional

A sequência operacional passa a ser:

```text
VALIDAÇÃO DOS DOCUMENTOS E FERRAMENTAS NECESSÁRIOS
        ↓
VIGÊNCIA OPERACIONAL
        ↓
PACOTES FINAIS
        ↓
PILOTO OFICIAL .014
        ↓
CLAIM FECHADO
        ↓
EVIDÊNCIAS / BIBLIOGRAFIA
        ↓
N1 / N2
        ↓
PRODUÇÃO DO CONJUNTO B1
        ↓
INTEGRAÇÃO
        ↓
VERTICAL SLICE B1
        ↓
TESTE PONTA A PONTA
        ↓
AUDITORIA
        ↓
CORREÇÕES
        ↓
REEXECUÇÃO
        ↓
APROVAÇÃO DO VERTICAL SLICE
        ↓
REPLICAÇÃO
```

A Anamnese já existente **não será utilizada automaticamente apenas por estar disponível**.

Ela entra no teste integrado somente depois de passar pelo processo de validação documental e obter vigência para uso.

---

# 20. CONTROLE DE PROGRESSO

Este quadro deverá ser atualizado ao longo do projeto.

| Marco                                          | Início | Em andamento | Concluído | Auditoria   | Observação                                           |
| ---------------------------------------------- | :----: | :----------: | :-------: | :-------:   | ---------------------------------------------------- |
| Engenharia base                                |    ⬜   |      🔄      |     ⬜     |     ⬜     | contratos e estruturas em evolução                   |
| Claims B1                                      |    ⬜   |      🔄      |     ⬜     |     ⬜     | validação em curso                                   |
| Ensaio operacional `.014`                      |    ✅  |       ⬜      |     ✅    |     ✅    | ensaio realizado e encerrado                         |
| Piloto oficial `.014`                          |    ⬜   |       ⬜      |     ⬜     |     ⬜     | depende das condições de execução e corpus congelado |
| Bibliotecas B1                                 |    ⬜   |      🔄      |     ⬜     |     ⬜     | consolidação                                         |
| Narrativas B1                                  |    ⬜   |       ⬜      |     ⬜     |     ⬜     | depende da base                                      |
| Ontologia/Grafo                                |    ⬜   |       ⬜      |     ⬜     |     ⬜     |                                                      |
| JSONs B1                                       |    ⬜   |       ⬜      |     ⬜     |     ⬜     |                                                      |
| Integração Motor                               |    ⬜   |       ⬜      |     ⬜     |     ⬜     |                                                      |
| Anamnese — acervo                              |    ✅  |       ⬜      |     ✅    |     ⬜     | arquivos existentes                                  |
| Anamnese — validação documental                |    ⬜   |       ⬜      |     ⬜     |     ⬜     | requer crivo das 3 IAs                               |
| Ferramentas/documentos operacionais — vigência |    ⬜   |      🔄      |     ⬜     |     ⬜     | verificação contínua                                 |
| Casos simulados                                |    ⬜   |       ⬜      |     ⬜     |     ⬜     |                                                      |
| Teste ponta a ponta                            |    ⬜   |       ⬜      |     ⬜     |     ⬜     | depende da integração                                |
| Auditoria final B1                             |    ⬜   |       ⬜      |     ⬜     |     ⬜     |                                                      |
| Aprovação do vertical slice                    |    ⬜   |       ⬜      |     ⬜     |     ⬜     |                                                      |
| Replicação                                     |    ⬜   |       ⬜      |     ⬜     |     ⬜     | somente após vertical slice                          |

### Legenda

⬜ Pendente
🔄 Em andamento
✅ Concluído
⚠️ Requer correção
