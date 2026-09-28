# ROTEIRO DE TRABALHO DA PLATAFORMA

**Documento operacional de acompanhamento do desenvolvimento da plataforma**

**Status:** documento de trabalho
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

O objetivo inicial **não é produzir imediatamente os 145 IDs restantes**.

O objetivo é construir e testar um **vertical slice completo da plataforma**, utilizando **B1 — Neuroinflamação** como primeiro conjunto integrado.

Somente depois que esse circuito estiver funcionando e auditado será feita a replicação para os demais IDs oficiais.

---

# 2. OS DOIS GRUPOS DE TRABALHO

O projeto possui dois grupos distintos.

Eles podem utilizar as mesmas tecnologias e até as mesmas IAs em momentos diferentes, mas possuem **objetos e responsabilidades diferentes**.

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
        (L-NT)      (L-05)
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
* coerência entre as diferentes camadas da plataforma.

A Arena–Casa é uma **bancada independente de verificação**. Ela recebe a análise produzida pelo Comentador, audita, mede e formaliza os achados e os encaminha aos responsáveis pelos contratos.

O Auditor-Mestre e o Auditor de Estrutura continuam sendo os responsáveis pelos seus respectivos domínios.

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

### Composição

```text
                 GRUPO 2
          VALIDAÇÃO DOS CLAIMS

       Outro ChatGPT
       (Validação inicial)
                │
                ▼
          Arena Claim
       (segunda análise)
                │
                ▼
          Claude Claim
       (terceira análise)
                │
                ▼
       retorno às IAs
                │
                ▼
      CONVERGÊNCIA FINAL
                │
          ┌─────┴─────┐
          ▼           ▼
       FECHADO     NÃO FECHADO
```

### Função

Este grupo trabalha especificamente na **validação científica dos claims clínicos**.

O processo utiliza:

* busca científica;
* PubMed;
* G1;
* G2;
* G3;
* análise da fonte primária;
* análise independente pelas IAs;
* registro das divergências;
* convergência final.

### Regra fundamental

O parecer da Claude Claim **não encerra sozinho o claim**.

A sequência é:

```text
ChatGPT Claim
      ↓
Arena Claim
      ↓
Claude Claim
      ↓
parecer da Claude
      ↓
retorno às IAs
      ↓
verificação final
      ↓
CONVERGÊNCIA
      ↓
CLAIM FECHADO
```

A concordância das IAs não constitui evidência científica.

A fonte científica permanece sendo a referência factual.

A convergência serve para verificar que o processo de análise não deixou divergência relevante aberta.

---

# 4. COMO OS DOIS GRUPOS SE RELACIONAM

Os grupos são separados, mas complementares.

```text
          GRUPO 2
     VALIDAÇÃO CIENTÍFICA
              │
              │
              ▼
       CLAIM FECHADO
              │
              ▼
     EVIDÊNCIAS /
      BIBLIOGRAFIA
              │
              ▼
          L-05 N1/N2
              │
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

O Grupo 2 determina **se o claim está cientificamente validado e fechado**.

O Grupo 1 determina **como esse conhecimento validado será formalizado, conectado, estruturado e disponibilizado para o restante da plataforma**.

---

# 5. COMO O PROJETO CHEGOU À ESTRUTURA ATUAL

O desenvolvimento ocorreu progressivamente.

Inicialmente, o foco estava na análise científica da **Biblioteca Canônica B1 — Neuroinflamação**.

Depois surgiu a necessidade de transformar o conhecimento canônico em unidades narrativas reutilizáveis.

Isso levou ao desenvolvimento das **Narrativas Transversais (NT)**.

Em seguida, tornou-se necessário estruturar as relações entre entidades, mecanismos e conhecimentos.

Isso levou à **Ontologia / Grafo**.

Depois surgiu a necessidade de representar essas estruturas de forma computável.

Isso levou aos **JSONs Modulares**.

Finalmente, percebeu-se que as narrativas e os JSONs precisavam ser produzidos já sabendo **como o Motor Clínico iria consumi-los**.

Por isso foi necessário desenvolver previamente o **Contrato do Motor Clínico**.

O percurso foi:

```text
B1 — ANÁLISE CIENTÍFICA
        ↓
BIBLIOTECA CANÔNICA
        ↓
necessidade de reutilização semântica
        ↓
NARRATIVAS TRANSVERSAIS
        ↓
necessidade de relações estruturadas
        ↓
ONTOLOGIA / GRAFO
        ↓
necessidade de representação computável
        ↓
JSONs MODULARES
        ↓
necessidade de definir o consumidor
        ↓
CONTRATO DO MOTOR CLÍNICO
```

Essa sequência não representa desvio de planejamento.

Representa a descoberta progressiva dos requisitos necessários para que o sistema inteiro seja coerente.

---

# 6. ESTRATÉGIA PRINCIPAL: VERTICAL SLICE

O projeto não deve produzir os 145 IDs em escala antes de testar o funcionamento integrado.

Primeiro será construído um **vertical slice completo**, utilizando B1 como eixo.

O objetivo é provar que todas as camadas conseguem trabalhar juntas.

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

# 7. PRIMEIRO CONJUNTO INTEGRADO

Para testar o circuito completo, B1 não será trabalhado isoladamente.

Será necessário construir o conjunto de conhecimentos relacionados à neuroinflamação:

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

Os claims clínicos validados pelo **Grupo 2** serão incorporados ao fluxo de:

```text
CLAIM FECHADO
      ↓
EVIDÊNCIAS / BIBLIOGRAFIA
      ↓
N1
      ↓
N2
      ↓
NT / ONTOLOGIA / GRAFO
```

Eles **não entram na Biblioteca Canônica de mecanismos**.

---

# 8. O CIRCUITO COMPLETO A SER TESTADO

Quando o conjunto B1 estiver preparado:

```text
                 ANAMNESE
                    │
                    ▼
             ┌─────────────┐
             │ MOTOR       │
             │ CLÍNICO     │
             └──────┬──────┘
                    │
                    ▼
          CONSULTA AO CONHECIMENTO
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
   CANÔNICO      EVIDÊNCIAS   ATUALIZAÇÕES
       │
       ▼
   NARRATIVAS
   TRANSVERSAIS
       │
       ▼
   ONTOLOGIA /
      GRAFO
       │
       ▼
   JSONs
   MODULARES
       │
       └──────────────► MOTOR
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

---

# 9. ENTRADA DO SISTEMA

A entrada inicial do teste será a **anamnese**.

Os arquivos de anamnese já existentes poderão ser utilizados.

Também poderão ser criados **casos clínicos simulados controlados**, especificamente para testar diferentes caminhos do Motor.

Os casos simulados não terão finalidade de estabelecer eficácia clínica.

Sua função será testar o comportamento do sistema.

---

# 10. O QUE O TESTE B1 DEVE RESPONDER

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
15. as regras de segurança e limites do sistema são respeitadas.

---

# 11. TESTE DE PONTA A PONTA

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

# 12. CRITÉRIO PARA A REPLICAÇÃO

A produção dos demais mecanismos e IDs oficiais somente deverá entrar em escala depois que o vertical slice B1 demonstrar:

* funcionamento;
* integração;
* rastreabilidade;
* coerência semântica;
* recuperação correta;
* ausência de falhas estruturais críticas;
* comportamento adequado do Motor;
* capacidade de produzir o resultado esperado;
* possibilidade de reprodução do processo.

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

# 13. CHECKLIST MESTRE DO PROJETO

| Etapa | Item                                                      | Status                 |
| ----- | --------------------------------------------------------- | ---------------------- |
| 1     | Arquitetura Consolidada V2.2                              | ✅ REALIZADO            |
| 2     | Definição dos dois grupos de trabalho                     | ⬜ PENDENTE DE REGISTRO |
| 3     | Contratos L-05 / N1 / N2                                  | 🔄 EM CONSOLIDAÇÃO     |
| 4     | Contrato L-NT                                             | 🔄 EM CONSOLIDAÇÃO     |
| 5     | Contrato do Motor Clínico                                 | 🔄 EM CONSOLIDAÇÃO     |
| 6     | Claim Kit                                                 | 🔄 EM TESTE            |
| 7     | Protocolo científico dos claims                           | 🔄 EM TESTE            |
| 8     | Claims clínicos B1                                        | 🔄 EM VALIDAÇÃO        |
| 9     | Biblioteca Canônica B1                                    | 🔄 EM CONSOLIDAÇÃO     |
| 10    | Biblioteca de Suplementos — B1                            | ⬜ PENDENTE             |
| 11    | Biblioteca de Intervenções — B1                           | ⬜ PENDENTE             |
| 12    | Biblioteca de Cenários — B1                               | ⬜ PENDENTE             |
| 13    | Biblioteca de Exames — B1                                 | ⬜ PENDENTE             |
| 14    | NT-B1                                                     | ⬜ PENDENTE             |
| 15    | NT dos Suplementos — B1                                   | ⬜ PENDENTE             |
| 16    | NT das Intervenções — B1                                  | ⬜ PENDENTE             |
| 17    | NT dos Cenários — B1                                      | ⬜ PENDENTE             |
| 18    | NT dos Exames — B1                                        | ⬜ PENDENTE             |
| 19    | Ontologia/Grafo — B1                                      | ⬜ PENDENTE             |
| 20    | JSONs Modulares — B1                                      | ⬜ PENDENTE             |
| 21    | Integração dos claims clínicos em Evidências/Bibliografia | ⬜ PENDENTE             |
| 22    | Integração N1/N2                                          | ⬜ PENDENTE             |
| 23    | Anamnese para teste                                       | ✅ ARQUIVOS EXISTENTES  |
| 24    | Casos simulados de teste                                  | ⬜ PENDENTE             |
| 25    | Integração completa B1                                    | ⬜ PENDENTE             |
| 26    | Teste do Motor Clínico                                    | ⬜ PENDENTE             |
| 27    | Teste ponta a ponta                                       | ⬜ PENDENTE             |
| 28    | Auditoria do circuito completo                            | ⬜ PENDENTE             |
| 29    | Correção das falhas encontradas                           | ⬜ PENDENTE             |
| 30    | Reexecução do circuito após correções                     | ⬜ PENDENTE             |
| 31    | Aprovação do vertical slice B1                            | ⬜ PENDENTE             |
| 32    | Definição do procedimento de replicação                   | ⬜ PENDENTE             |
| 33    | Início da expansão para demais IDs                        | ⬜ PENDENTE             |

---

# 14. MARCOS DE TRABALHO

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
ChatGPT Claim
 ↓
Arena Claim
 ↓
Claude Claim
 ↓
retorno às IAs
 ↓
convergência
 ↓
claim fechado
```

**Objetivo:** produzir claims clínicos cientificamente validados e rastreáveis.

---

## MARCO 3 — PRODUÇÃO DO CONJUNTO B1

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

## MARCO 4 — INTEGRAÇÃO

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

## MARCO 5 — TESTE COMPLETO

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

## MARCO 6 — AUDITORIA E CORREÇÃO

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

## MARCO 7 — REPLICAÇÃO

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

# 15. PRINCÍPIO CENTRAL DO PROJETO

A plataforma não será considerada pronta porque cada componente individual funciona.

Ela será considerada pronta para expansão quando o **circuito integrado** funcionar.

O objetivo desta primeira fase é, portanto:

> **Construir, integrar, testar e auditar um circuito completo da plataforma utilizando B1 — Neuroinflamação como vertical slice, incluindo claims clínicos validados, Bibliotecas, Narrativas Transversais, Ontologia/Grafo, JSONs Modulares, Motor Clínico e Anamnese, antes de replicar o modelo para os demais IDs oficiais.**

---

# 16. REGRA DE GOVERNANÇA

Nenhum documento deste roteiro substitui os contratos normativos, schemas ou protocolos específicos.

Este documento serve para:

* orientar a sequência de trabalho;
* registrar o estado do projeto;
* mostrar dependências;
* evitar produção fora de ordem;
* permitir que os dois grupos saibam em que etapa o projeto se encontra;
* identificar o próximo trabalho necessário.

As decisões específicas continuam pertencendo ao documento/contrato correspondente.

---

# 17. ESTADO ATUAL

### Já consolidado

* Arquitetura Consolidada V2.2;
* separação conceitual entre os dois grupos;
* direção Claim Kit → Evidências/Bibliografia → L-05;
* distinção entre Claim, N1 e N2;
* necessidade de contrato do Motor antes da produção massiva das NTs;
* estrutura geral do L-NT;
* estrutura L-05 N1/N2 em consolidação;
* B1 como primeiro vertical slice;
* anamnese já disponível para os testes.

### Próximo objetivo operacional

**Finalizar as estruturas e contratos necessários para que o conteúdo possa começar a ser produzido já no formato adequado ao circuito completo.**

Depois:

**Claim clínico → Evidências/Bibliografia → N1/N2 → NT → Ontologia → JSON → Motor → Anamnese → Teste.**

---

# 18. CONTROLE DE PROGRESSO

Este quadro deverá ser atualizado ao longo do projeto.

| Marco                       | Início | Em andamento | Concluído | Auditoria | Observação |
| --------------------------- | -----: | -----------: | --------: | --------: | ---------- |
| Engenharia base             |      ⬜ |            ⬜ |         ⬜ |         ⬜ |            |
| Claims B1                   |      ⬜ |            ⬜ |         ⬜ |         ⬜ |            |
| Bibliotecas B1              |      ⬜ |            ⬜ |         ⬜ |         ⬜ |            |
| Narrativas B1               |      ⬜ |            ⬜ |         ⬜ |         ⬜ |            |
| Ontologia/Grafo             |      ⬜ |            ⬜ |         ⬜ |         ⬜ |            |
| JSONs B1                    |      ⬜ |            ⬜ |         ⬜ |         ⬜ |            |
| Integração Motor            |      ⬜ |            ⬜ |         ⬜ |         ⬜ |            |
| Anamnese/Casos              |      ⬜ |            ⬜ |         ⬜ |         ⬜ |            |
| Teste ponta a ponta         |      ⬜ |            ⬜ |         ⬜ |         ⬜ |            |
| Auditoria final B1          |      ⬜ |            ⬜ |         ⬜ |         ⬜ |            |
| Aprovação do vertical slice |      ⬜ |            ⬜ |         ⬜ |         ⬜ |            |
| Replicação                  |      ⬜ |            ⬜ |         ⬜ |         ⬜ |            |

**Legenda:**
⬜ Pendente
🔄 Em andamento
✅ Concluído
⚠️ Requer correção
