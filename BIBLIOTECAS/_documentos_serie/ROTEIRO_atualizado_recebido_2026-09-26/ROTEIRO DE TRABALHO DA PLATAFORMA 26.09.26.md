# ROTEIRO DE TRABALHO DA PLATAFORMA

**Documento operacional de acompanhamento do desenvolvimento da plataforma**

**Status:** documento de trabalho
**Atualização:** 2026-09-26
**Objetivo:** organizar a sequência de desenvolvimento, validação, integração e teste da plataforma antes da replicação para os demais IDs oficiais.

---

# 1. OBJETIVO DO ROTEIRO

Este documento estabelece o roteiro geral de trabalho para transformar o conhecimento científico da plataforma em um sistema integrado capaz de:

* receber uma anamnese;
* consultar conhecimento estruturado;
* relacionar mecanismos, suplementos, intervenções, cenários e exames;
* produzir interpretação contextualizada;
* gerar sugestões;
* explicar as relações encontradas;
* produzir um Laudo Técnico de Apoio para avaliação do profissional.

O objetivo inicial **não é produzir imediatamente os demais IDs oficiais em escala**.

O objetivo é construir e testar um **vertical slice completo da plataforma**, utilizando **B1 — Neuroinflamação** como primeiro conjunto integrado.

Somente depois que esse circuito estiver funcionando e auditado será feita a replicação para os demais IDs oficiais.

O roteiro também separa explicitamente:

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

A aquisição ampla de literatura pode utilizar diferentes ferramentas de descoberta. A validação científica, porém, segue o protocolo vigente e mantém a fonte primária como árbitro factual.

---

# 2. OS DOIS GRUPOS DE TRABALHO

O projeto possui dois grupos distintos.

Eles podem utilizar tecnologias semelhantes e, em situações específicas, as mesmas IAs, mas possuem **objetos e responsabilidades diferentes**.

---

## GRUPO 1 — ENGENHARIA, ARQUITETURA E CONTRATOS

### Composição

```text
                 GRUPO 1
       ARQUITETURA / CONTRATOS

       Comentador — ChatGPT
                │
                ▼
          Arena–Casa
           (Bancada)
          │          │
          ▼          ▼
      Auditor      Auditor
       Mestre     Estrutura
```

### Função

Este grupo trabalha sobre:

* arquitetura;
* contratos;
* schemas;
* ferramentas;
* estruturas de dados;
* fluxos;
* materializadores;
* integração;
* ontologia;
* JSONs;
* contrato do Motor;
* regras de rastreabilidade;
* coerência entre as diferentes camadas da plataforma;
* verificação operacional dos artefatos.

A **Arena–Casa** funciona como bancada de confronto, verificação e formalização de achados.

O **Auditor-Estrutura** atua sobre estrutura, schemas, materialização e compatibilidade estrutural.

O **Auditor-Mestre** atua sobre contrato, governança, execução do protocolo e auditoria do processo.

### Regra de convergência

O Grupo 1 trabalha como engenharia de software.

Portanto, **não existe limite artificial de duas rodadas**.

Quando houver divergência sobre arquitetura, schema, contrato ou ferramenta, podem ocorrer quantas rodadas forem necessárias para:

```text
ANÁLISE
   ↓
AUDITORIA
   ↓
CONTRAPOSIÇÃO
   ↓
CORREÇÃO
   ↓
NOVA VERIFICAÇÃO
   ↓
CONVERGÊNCIA
```

O objetivo é chegar a uma estrutura tecnicamente consistente, verificável e implementável.

---

# 3. GRUPO 2 — VALIDAÇÃO CIENTÍFICA DOS CLAIMS

Este grupo é separado do Grupo 1.

### Composição operacional oficial

```text
                 GRUPO 2
          VALIDAÇÃO DOS CLAIMS

       IA 1 — ChatGPT dedicado
                │
                │ análise independente
                ▼
       IA 2 — Arena dedicado
                │
                │ análise independente
                ▼
       IA 3 — Claude dedicado
                │
                │ análise independente
                │ + parecer
                ▼
          COMPARAÇÃO POSTERIOR
                │
                ▼
       retorno às IAs 1 e 2
                │
                ▼
        FECHAMENTO CONJUNTO
                │
         ┌──────┴──────┐
         ▼             ▼
      FECHADO      NÃO FECHADO
```

### Função

Este grupo trabalha especificamente na **validação científica dos claims clínicos**.

O processo vigente utiliza:

* descoberta e recuperação bibliográfica;
* PubMed;
* G1;
* G2;
* G3;
* análise da fonte primária;
* três análises independentes;
* registro das divergências;
* retorno às IAs 1 e 2;
* fechamento conjunto;
* registro das decisões do Claim Kit.

### Regra fundamental

A IA3 **não encerra sozinha o claim**.

A IA3 produz parecer.

O fechamento ocorre somente depois da comparação e do retorno às IAs 1 e 2.

A concordância entre as IAs não constitui evidência científica.

A fonte científica permanece sendo o artigo ou outra fonte primária adequada.

### Independência

Antes da comparação:

* IA1 não vê a análise da IA2 nem da IA3;
* IA2 não vê a análise da IA1 nem da IA3;
* IA3 não vê as análises anteriores antes de produzir a própria análise.

A divergência entre análises independentes é tratada como resultado possível do método, não como falha do método.

---

# 4. ENSAIO OPERACIONAL PRÉ-PILOTO

Antes do primeiro piloto oficial será realizado um **ensaio operacional do B1.SM02.014**.

O ensaio utiliza temporariamente os agentes que participaram da construção dos contratos, ferramentas e fluxos.

Essa etapa **não testa a independência epistemológica** da futura tríade, porque os participantes conhecem o histórico da construção.

Seu objetivo é testar a operação da máquina:

```text
PACOTES
   ↓
DOCUMENTOS
   ↓
ORDEM DE EXECUÇÃO
   ↓
FERRAMENTAS
   ↓
FLUXO
   ↓
REGISTROS
   ↓
FECHAMENTO OPERACIONAL
```

### O ensaio deve verificar

* integridade dos pacotes;
* leitura correta dos documentos;
* funcionamento das instruções;
* execução de G1/G2/G3;
* separação entre análise e fechamento;
* rastreabilidade;
* transição entre as etapas;
* compatibilidade dos resultados com o Schema vigente;
* separação entre execução e materialização;
* identificação de problemas puramente operacionais.

### Regras do ensaio

O ensaio:

* não altera as bases normativas;
* não fecha novamente o claim oficial;
* não altera o estado do B1.SM02.014 no Bloco;
* não transforma automaticamente seu corpus em corpus oficial;
* não encerra o piloto;
* não substitui a tríade independente do piloto oficial.

O resultado do ensaio é um **registro de execução operacional**.

Problema operacional permanece operacional.

Problema normativo somente pode resultar em novo ciclo formal.

---

# 5. COMO OS DOIS GRUPOS SE RELACIONAM

Os grupos são separados, mas complementares.

```text
          GRUPO 2
     VALIDAÇÃO CIENTÍFICA
              │
              ▼
       CLAIM FECHADO
              │
              ▼
     EVIDÊNCIAS /
      BIBLIOGRAFIA
              │
              ▼
           N1 / N2
              │
              ▼
     CAMADAS POSTERIORES
              │
              ▼
        GRUPO 1
 ESTRUTURA / INTEGRAÇÃO
              │
              ▼
       NT / ONTOLOGIA
              │
              ▼
       JSONs MODULARES
              │
              ▼
        MOTOR CLÍNICO
```

O Grupo 2 determina **se o claim foi cientificamente fechado**.

O Grupo 1 determina **como o conhecimento validado será formalizado, conectado, estruturado e disponibilizado para as camadas posteriores da plataforma**.

Claim, N1 e N2 não são a mesma coisa.

O Claim é o artefato do processo de validação científica.

O N1 representa a referência bibliográfica.

O N2 representa o vínculo estruturado.

---

# 6. DESCOBERTA BIBLIOGRÁFICA E VALIDAÇÃO

A plataforma diferencia explicitamente **descoberta de literatura** de **validação científica**.

A descoberta pode utilizar, conforme disponibilidade e objetivo:

* Consensus;
* PubMed;
* ferramentas de recuperação de texto completo;
* outras fontes de localização bibliográfica;
* agentes auxiliares de busca.

Essas ferramentas podem gerar conjuntos amplos de candidatos.

### Fluxo de descoberta

```text
CLAIM DA LISTA CANÔNICA
        ↓
DESCOBERTA AMPLA
        ↓
LISTAS DE ARTIGOS
        ↓
CONSOLIDAÇÃO
        ↓
DESDUPLICAÇÃO
        ↓
CORPUS DE TRABALHO
        ↓
CONGELAMENTO DO CORPUS DA RODADA
```

A lista consolidada é um **corpus de candidatos**.

Ela não representa, por si só, validação científica.

### Validação

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

Essa sequência representa descoberta progressiva dos requisitos necessários para manter o sistema coerente.

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

Quando o conjunto B1 estiver preparado:

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

Os arquivos de anamnese já existentes poderão ser utilizados.

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
ANAMNESE
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

| Etapa | Item                                                      | Status                 |
| ----- | --------------------------------------------------------- | ---------------------- |
| 1     | Arquitetura Consolidada V2.2                              | ✅ REALIZADO            |
| 2     | Definição dos dois grupos de trabalho                     | ✅ REALIZADO            |
| 3     | Contratos L-05 / N1 / N2                                  | ✅ BASE VIGENTE         |
| 4     | Contrato L-NT                                             | 🔄 EM CONSOLIDAÇÃO     |
| 5     | Contrato do Motor Clínico                                 | ⬜ A DESENVOLVER        |
| 6     | Contrato de Saída do Claim Kit rev.2                      | ✅ VIGENTE              |
| 7     | Schema-Claim v1.3 rev.3                                   | ✅ VIGENTE              |
| 8     | COMO EXECUTAR v1.10                                       | ✅ VIGENTE              |
| 9     | Protocolo científico dos claims                           | ✅ INCORPORADO AO v1.10 |
| 10    | Ensaio operacional B1.SM02.014                            | 🔄 A INICIAR           |
| 11    | Piloto oficial B1.SM02.014                                | ⬜ PENDENTE             |
| 12    | Claims clínicos B1                                        | 🔄 EM VALIDAÇÃO        |
| 13    | Biblioteca Canônica B1                                    | 🔄 EM CONSOLIDAÇÃO     |
| 14    | Biblioteca de Suplementos — B1                            | ⬜ PENDENTE             |
| 15    | Biblioteca de Intervenções — B1                           | ⬜ PENDENTE             |
| 16    | Biblioteca de Cenários — B1                               | ⬜ PENDENTE             |
| 17    | Biblioteca de Exames — B1                                 | ⬜ PENDENTE             |
| 18    | NT-B1                                                     | ⬜ PENDENTE             |
| 19    | NT dos Suplementos — B1                                   | ⬜ PENDENTE             |
| 20    | NT das Intervenções — B1                                  | ⬜ PENDENTE             |
| 21    | NT dos Cenários — B1                                      | ⬜ PENDENTE             |
| 22    | NT dos Exames — B1                                        | ⬜ PENDENTE             |
| 23    | Ontologia/Grafo — B1                                      | ⬜ PENDENTE             |
| 24    | JSONs Modulares — B1                                      | ⬜ PENDENTE             |
| 25    | Integração dos claims clínicos em Evidências/Bibliografia | 🔄 EM PREPARAÇÃO       |
| 26    | Primeira materialização N1/N2 do fluxo novo               | ⬜ PENDENTE             |
| 27    | Anamnese para teste                                       | ✅ ARQUIVOS EXISTENTES  |
| 28    | Casos simulados de teste                                  | ⬜ PENDENTE             |
| 29    | Integração completa B1                                    | ⬜ PENDENTE             |
| 30    | Teste do Motor Clínico                                    | ⬜ PENDENTE             |
| 31    | Teste ponta a ponta                                       | ⬜ PENDENTE             |
| 32    | Auditoria do circuito completo                            | ⬜ PENDENTE             |
| 33    | Correção das falhas encontradas                           | ⬜ PENDENTE             |
| 34    | Reexecução do circuito após correções                     | ⬜ PENDENTE             |
| 35    | Aprovação do vertical slice B1                            | ⬜ PENDENTE             |
| 36    | Definição do procedimento de replicação                   | ⬜ PENDENTE             |
| 37    | Início da expansão para demais IDs                        | ⬜ PENDENTE             |

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
```

**Objetivo:** testar a máquina antes de entregar o piloto oficial à tríade dedicada.

O ensaio não substitui o piloto oficial e não mede independência epistemológica.

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

**Objetivo:** testar o COMO EXECUTAR v1.10 em condições reais de independência operacional.

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
Anamnese
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

> **Construir, integrar, testar e auditar um circuito completo da plataforma utilizando B1 — Neuroinflamação como vertical slice, incluindo claims clínicos validados, Bibliotecas, Narrativas Transversais, Ontologia/Grafo, JSONs Modulares, Motor Clínico e Anamnese, antes de replicar o modelo para os demais IDs oficiais.**

O processo de validação científica dos claims e o processo de engenharia da plataforma permanecem separados.

O primeiro não deve substituir o segundo.

O segundo não deve decidir a verdade científica do primeiro.

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
* separar ensaio operacional, piloto oficial e produção.

As decisões específicas continuam pertencendo ao documento/contrato correspondente.

### Bases normativas vigentes relacionadas ao processo

```text
Contrato de Saída do Claim Kit rev.2
        ↓
Schema-Claim v1.3 rev.3
        ↓
COMO EXECUTAR v1.10
```

Os documentos acima têm função normativa própria.

O Roteiro apenas organiza a execução do projeto em torno deles.

Nenhuma etapa deste roteiro autoriza alteração silenciosa de contrato, schema, N1 ou N2.

---

# 19. ESTADO ATUAL

### Já consolidado

* Arquitetura Consolidada V2.2;
* separação entre os dois grupos;
* distinção entre Claim, N1 e N2;
* Contrato de Saída do Claim Kit rev.2 vigente;
* Schema-Claim v1.3 rev.3 vigente;
* COMO EXECUTAR v1.10 vigente;
* direção Claim Kit → Evidências/Bibliografia → N1/N2;
* distinção entre descoberta bibliográfica e validação científica;
* B1 como primeiro vertical slice;
* anamnese já disponível para os testes;
* desenho do ensaio operacional pré-piloto do B1.SM02.014.

### Estado transitório atual

O próximo passo é executar o **ensaio operacional pré-piloto do B1.SM02.014**.

Esse ensaio deverá:

* testar as ferramentas;
* testar os pacotes;
* testar a ordem do processo;
* registrar dificuldades;
* não alterar o estado oficial do `.014`;
* não encerrar E-4;
* não substituir o piloto oficial.

### Próximo objetivo operacional

**Executar o ensaio operacional do B1.SM02.014, consolidar os aprendizados operacionais e então congelar os pacotes da tríade dedicada para o piloto oficial.**

Depois:

```text
Ensaio operacional
        ↓
Pacotes finais
        ↓
Piloto oficial .014
        ↓
Claim fechado
        ↓
Evidências / Bibliografia
        ↓
N1 / N2
        ↓
Integração posterior
        ↓
Vertical slice B1
        ↓
Teste ponta a ponta
        ↓
Auditoria
        ↓
Replicação
```

---

# 20. CONTROLE DE PROGRESSO

Este quadro deverá ser atualizado ao longo do projeto.

| Marco                       | Início | Em andamento | Concluído | Auditoria | Observação                                       |
| --------------------------- | :----: | :----------: | :-------: | :-------: | ------------------------------------------------ |
| Engenharia base             |    ⬜   |      🔄      |     ⬜     |     ⬜     | contratos e estruturas em evolução               |
| Claims B1                   |    ⬜   |      🔄      |     ⬜     |     ⬜     | piloto `.014` em preparação                      |
| Ensaio operacional `.014`   |    ⬜   |      🔄      |     ⬜     |     ⬜     | etapa atual                                      |
| Piloto oficial `.014`       |    ⬜   |       ⬜      |     ⬜     |     ⬜     | depende do ensaio                                |
| Bibliotecas B1              |    ⬜   |      🔄      |     ⬜     |     ⬜     | consolidação                                     |
| Narrativas B1               |    ⬜   |       ⬜      |     ⬜     |     ⬜     | depende da base                                  |
| Ontologia/Grafo             |    ⬜   |       ⬜      |     ⬜     |     ⬜     |                                                  |
| JSONs B1                    |    ⬜   |       ⬜      |     ⬜     |     ⬜     |                                                  |
| Integração Motor            |    ⬜   |       ⬜      |     ⬜     |     ⬜     |                                                  |
| Anamnese/Casos              |    ✅   |      🔄      |     ⬜     |     ⬜     | anamnese existente; casos ainda serão preparados |
| Teste ponta a ponta         |    ⬜   |       ⬜      |     ⬜     |     ⬜     |                                                  |
| Auditoria final B1          |    ⬜   |       ⬜      |     ⬜     |     ⬜     |                                                  |
| Aprovação do vertical slice |    ⬜   |       ⬜      |     ⬜     |     ⬜     |                                                  |
| Replicação                  |    ⬜   |       ⬜      |     ⬜     |     ⬜     | somente após vertical slice                      |

### Legenda

⬜ Pendente
🔄 Em andamento
✅ Concluído
⚠️ Requer correção
