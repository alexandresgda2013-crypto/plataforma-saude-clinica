# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2    17.09.26

## Bibliotecas Canônicas, Evidências Bibliográficas/Vínculos, Narrativas Transversais, Ontologia/Grafo, JSONs Modulares, Pasta de Atualização e Motor Clínico
**Rev. V2.2 — 2026-09-17** · Correção arquitetural localizada do §2: nó "EVIDÊNCIAS / VÍNCULOS UNIFICADOS" removido — fluxos canônico × atualização segregados até o Motor (achado do Auditor-Mestre, sha 2841bc66…; parecer concorrente do comentador externo) · proveniência no item recuperado (origem_conhecimento = canonico | atualizacao) · base: V2.1 do operador (upload 5be36836…, instalada na rodada 24) · decisão do operador (rodada 26) · 0 ciência alterada

---

# 1. VISÃO GERAL

A arquitetura da plataforma não é formada apenas pelas Bibliotecas Canônicas dos mecanismos B1–B16.

O sistema deverá trabalhar com múltiplos domínios de conhecimento, incluindo, entre outros:

* mecanismos biológicos;
* suplementos;
* exames;
* intervenções;
* cenários;
* nutrição;
* fitoterapia;
* sono;
* exercício;
* e futuros domínios que venham a ser incorporados.

Atualmente existe um catálogo de **146 IDs oficiais**.

Esses IDs constituem o universo oficial de entidades da arquitetura atual.

Cada entidade poderá possuir sua própria cadeia:

**Biblioteca Canônica → Narrativa Transversal (NT) → JSON(s) Modular(es)**

Entretanto, essa cadeia não significa que cada entidade produzirá obrigatoriamente apenas um JSON.

Uma entidade poderá gerar múltiplos módulos JSON quando sua representação funcional exigir decomposição.

A arquitetura deve ser entendida como uma **rede multidomínio de conhecimento científico auditável**, e não como uma simples sequência de conversões de documentos.

---

# 2. VISÃO GERAL DA ARQUITETURA

```text

================================================================================
ARQUITETURA GERAL DA PLATAFORMA (MAPA EXECUTIVO)
================================================================================

      [ CIÊNCIA ]
           │
           ▼
  ┌─────────────────────────┐
  │  BIBLIOTECAS CANÔNICAS  │
  └────────────┬────────────┘
               │
         ┌─────┴──────────────────┐
         ▼                        ▼
  ┌──────────────┐        ┌──────────────┐
  │  EVIDÊNCIAS  │        │  NARRATIVAS  │
  │ BIBLIOGRAFIA │        │ TRANSVERSAIS │
  └──────┬───────┘        └──────┬───────┘
         │                       │
         └───────────┬───────────┘
                     │
                     ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │                    EVIDÊNCIAS / VÍNCULOS CANÔNICOS                     │
  └───────────────────────────────────┬────────────────────────────────────┘
                                      │
                                      ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │                     ONTOLOGIA / GRAFO MULTIDOMÍNIO                     │
  └───────────────────────────────────┬────────────────────────────────────┘
                                      │
                                      ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │                            JSONs MODULARES                             │
  └───────────────────────────────────┬────────────────────────────────────┘
                                      ▲
                                      │
                            [ CONEXÃO / CONSULTA ]
                                      │
                           O Motor busca ativamente
                              o conhecimento
                                      │
  ┌───────────────────────────────────┴────────────────────────────────────┐
  │                            MOTOR CLÍNICO                               │◄─── [ ANAMNESE ]
  │                     [ MÁQUINA DE PROCESSAMENTO ]                       │
  └───────────────────────────────────┬────────────────────────────────────┘
                                      │
                                      ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │                     INTERPRETAÇÃO CONTEXTUALIZADA                      │
  └────────┬──────────────────────────┬──────────────────────────┬─────────┘
           │                          │                          │
           ▼                          ▼                          ▼
  ┌─────────────────┐        ┌─────────────────┐        ┌─────────────────┐
  │   MECANÍSTICA   │        │    CLÍNICA      │        │  TERAPÊUTICA    │
  │    Sugestão     │        │    Sugestão     │        │    Sugestão     │
  └────────┬────────┘        └────────┬────────┘        └────────┬────────┘
           │                          │                          │
           └──────────────────────────┼──────────────────────────┘
                                      │
                                      ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │                          EXPLICAÇÃO NARRATIVA                          │
  └───────────────────────────────────┬────────────────────────────────────┘
                                      │
                                      ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │                                LAUDO                                   │
  └────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────┐
  │   PASTA DE ATUALIZAÇÃO  │
  │   (ciência recente;     │ ─────────────────►  MOTOR CLÍNICO
  │    fora do cânone)      │      consulta ativa do Motor — SEM
  └─────────────────────────┘      passar pela Ontologia/Grafo.
    Todo item recuperado pelo       Os dois fluxos só se encontram
    Motor carrega a origem:         no Motor (nunca a montante).
    origem_conhecimento =
    canonico | atualizacao


================================================================================
### Relação entre Conhecimento e Caso (Lógica da Máquina)
================================================================================

  ┌──────────────────────────────────────────────────┐
  │             CONHECIMENTO CIENTÍFICO              │
  │  (Bibliotecas, Narrativas, Atualizações, Grafo)  │
  └────────────────────────┬─────────────────────────┘
                           ▲
                           │
                    (Consulta Ativa)
                           │
            ┌──────────────┴──────────────┐
            │        MOTOR CLÍNICO        │◄============== [ ANAMNESE ]
            │ [ Processador Algorítmico ] │               (Dados do Caso)
            └──────────────┬──────────────┘
                           │
                           ▼
            ┌─────────────────────────────┐
            │INTERPRETAÇÃO CONTEXTUALIZADA│
            └──────────────┬──────────────┘
                           │
                           ▼
            ┌─────────────────────────────┐
            │          SUGESTÕES          │
            └──────────────┬──────────────┘
                           │
                           ▼
            ┌─────────────────────────────┐
            │            LAUDO             │
            └─────────────────────────────┘

--------------------------------------------------------------------------------
DEFINIÇÃO:
A anamnese constitui os dados clínicos do caso fornecidos como entrada
para o Motor Clínico (A Máquina). Ao receber este gatilho, o Motor executa
uma busca ativa e cruza esses dados com o conhecimento científico estruturado
(Bibliotecas Canônicas, Narrativas, Atualizações e relações mapeadas no
Grafo/JSONs) para gerar a interpretação contextualizada do caso.
--------------------------------------------------------------------------------
```

**Fluxo canônico × fluxo de atualização — regra arquitetural (Rev. V2.2, 2026-09-17):** os dois fluxos
permanecem segregados até o Motor Clínico. O canônico percorre Bibliotecas Canônicas → Evidências
Bibliográficas e Narrativas Transversais → Evidências/Vínculos Canônicos → Ontologia/Grafo → JSONs
Modulares → Motor; a Pasta de Atualização chega ao Motor por caminho próprio, por consulta ativa, sem
passar pela Ontologia/Grafo e sem se fundir aos vínculos canônicos. Todo item recuperado pelo Motor
carrega a proveniência no próprio item (origem_conhecimento = canonico | atualizacao), de modo que a
consulta conjunta preserva a rastreabilidade. A consulta à Pasta de Atualização não constitui incorporação
ao conhecimento canônico — esta só ocorre por processo formal de atualização/curadoria (§18–§20). Em
divergência de representação, a prosa deste documento prevalece sobre os desenhos.
*(Correção por achado do Auditor-Mestre de 2026-09-17; parecer concorrente do comentador externo;
decisão do operador, rodada 26.)*



---

# 3. CATÁLOGO DOS IDs OFICIAIS

Os IDs oficiais constituem o vocabulário controlado das entidades reconhecidas pelo sistema.

Atualmente:

**146 IDs oficiais**

Esses IDs podem pertencer a diferentes domínios.

Conceitualmente:

```text
                         146 IDs OFICIAIS
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
     MECANISMOS             SUPLEMENTOS             EXAMES
     B1 ... B16              S01 ...                 E01 ...
          │                     │                     │
          ├─────────────────────┼─────────────────────┤
          │                     │                     │
          ▼                     ▼                     ▼
    INTERVENÇÕES             CENÁRIOS             OUTROS
       I01 ...                C01 ...             DOMÍNIOS
```

O catálogo oficial permite que as diferentes camadas da arquitetura utilizem identificadores consistentes.

---

# 4. BIBLIOTECAS CANÔNICAS

A Biblioteca Canônica é a **fonte fechada e auditada do conhecimento científico de cada entidade/domínio**.

Ela deve representar o conhecimento que passou pelo processo de construção, triagem, validação e auditoria definido pela arquitetura da plataforma.

A NT não deverá reconstruir a Biblioteca.

A NT também não deverá complementar silenciosamente a Biblioteca por pesquisa externa durante sua construção.

Portanto:

```text
BIBLIOTECA CANÔNICA
        =
CONHECIMENTO CIENTÍFICO CANÔNICO
```

A Biblioteca responde essencialmente:

> **O que sabemos sobre esta entidade e quais afirmações científicas estão efetivamente sustentadas?**

---

# 5. EVIDÊNCIAS BIBLIOGRÁFICAS E VÍNCULOS

As camadas de Evidências/Vínculos constituem a infraestrutura de sustentação, rastreabilidade e procedência científica da arquitetura.

Elas **não constituem uma segunda Biblioteca Canônica** nem uma fonte de conhecimento científico independente.

A arquitetura já possui um repositório específico de referências científicas em:

`/Evidencias/Bibliograficas`

Esse repositório contém as referências científicas selecionadas e auditadas pelo pipeline, incluindo, conforme aplicável:

* meta-análises;
* revisões sistemáticas;
* ensaios clínicos;
* estudos observacionais;
* estudos experimentais;
* estudos pré-clínicos;
* outras referências científicas aprovadas pelo processo de auditoria.

A classificação da referência não deverá ser duplicada por uma estrutura física de pastas baseada no desenho do estudo.

A natureza da evidência e o desenho do estudo são propriedades estruturadas nos registros das referências.

---

## 5.1. Schema de Referência — L-05 Nível 1

A caracterização estruturada das referências bibliográficas é realizada pelo:

`L05/schema_referencia_v1.1.json`

O Nível 1 representa a **própria referência científica**.

Ele registra, entre outros elementos:

* identificador interno da referência;
* PMID oficial;
* título;
* origem no pipeline;
* natureza da evidência;
* desenho do estudo;
* desenho do estudo bruto;
* status de auditoria;
* status de verificação;
* achados centrais;
* informações de proveniência;
* demais metadados definidos pelo schema.

O Nível 1 responde essencialmente:

> **O que é esta referência científica e que tipo de evidência ela representa?**

A referência científica deve existir uma única vez no repositório bibliográfico, ainda que possa ser relacionada a múltiplas entidades oficiais.

---

## 5.2. Evidências/Vínculos — L-05 Nível 2

A camada:

`/Evidencias/Vinculos`

é responsável por estabelecer a relação estruturada entre a referência científica, as afirmações e as entidades oficiais.

Seu schema é:

`L05/schema_vinculo_v1.1.json`

O Nível 2 representa:

```text
REFERÊNCIA
     ↕
   CLAIM
     ↕
ID(s) OFICIAL(is)
```

Um mesmo estudo pode possuir múltiplos vínculos e múltiplas âncoras oficiais quando sua evidência for cientificamente pertinente a mais de uma entidade.

Isso não significa duplicação da referência.

O vínculo preserva, conforme definido pelo schema:

* referência utilizada;
* trecho-âncora;
* claim relacionado;
* ID oficial;
* papel da âncora;
* escopo;
* direção da relação;
* condição, quando aplicável;
* natureza da relação;
* força da relação;
* grau de maturidade;
* trilha clínica ou mecanística;
* status de verificação;
* informações de auditoria;
* proveniência.

---

## 5.3. Relação entre Biblioteca, Evidência e Vínculo

A arquitetura distingue claramente três funções:

```text
EVIDÊNCIA BIBLIOGRÁFICA
        │
        │ fonte científica
        ▼
BIBLIOTECA CANÔNICA
        │
        │ conhecimento científico
        ▼
NARRATIVA TRANSVERSAL
        │
        │ organização semântica
        ▼
ONTOLOGIA / GRAFO
        │
        │ relações formalizadas
        ▼
JSONs MODULARES
        │
        ▼
MOTOR
```

Os vínculos funcionam transversalmente nessa cadeia:

```text
                    REFERÊNCIA
                         │
                         ▼
                       CLAIM
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
            B1           B3          S01
             │           │           │
             └───────────┼───────────┘
                         ▼
                  RASTREABILIDADE
```

Portanto, a evidência é armazenada uma vez e pode ser relacionada a diferentes entidades por meio de vínculos estruturados.

---

## 5.4. Regra de não duplicação

A arquitetura não deverá criar uma cópia da mesma evidência em cada Biblioteca.

Uma publicação pode ser relevante para:

* um mecanismo;
* um suplemento;
* um exame;
* uma intervenção;
* um cenário;
* ou múltiplas entidades simultaneamente.

Nesses casos, a referência permanece no repositório bibliográfico e recebe os vínculos correspondentes.

Assim:

> **A evidência existe uma vez; os vínculos permitem reutilizá-la em diferentes contextos científicos da arquitetura.**

Cada Biblioteca, entretanto, utiliza somente o conteúdo da referência pertinente ao seu próprio objeto científico.

---

## 5.5. Regra de localização do aprofundamento científico

O fato de uma evidência possuir relevância clínica não determina automaticamente que ela pertença a uma Biblioteca de Cenário Clínico.

A localização do aprofundamento é determinada pelo **objeto científico ao qual o conteúdo se refere**.

Portanto:

> **A Biblioteca de origem explica a relação; a Biblioteca correspondente contém o aprofundamento específico do objeto científico.**

Uma mesma publicação pode, portanto, ser relacionada por meio de vínculos a diferentes domínios, desde que cada vínculo represente uma relação cientificamente justificável e específica.

---

# 6. O QUE É A NARRATIVA TRANSVERSAL

A **Narrativa Transversal (NT)** é a camada semântica intermediária entre o conhecimento científico canônico e sua utilização pelo restante da arquitetura.

Ela não é:

* uma nova Biblioteca;
* um resumo simples da Biblioteca;
* a Ontologia/Grafo;
* o JSON;
* o Motor;
* o laudo final.

Sua função é:

> **interpretar semanticamente, organizar, relacionar, estruturar e explicar o conhecimento científico já fechado e auditado.**

A NT deverá:

1. consumir o conhecimento da Biblioteca correspondente;
2. utilizar as Evidências/Vínculos necessárias à rastreabilidade;
3. identificar conceitos, entidades e atributos;
4. identificar relações;
5. identificar condições e dependências;
6. identificar direção e natureza das relações;
7. estruturar semanticamente essas informações;
8. preparar essas relações para integração à Ontologia/Grafo;
9. estabelecer relações auditáveis com outras NTs;
10. produzir unidades narrativas reutilizáveis;
11. produzir explicações científicas fluidas;
12. fornecer a base semântica dos JSONs;
13. fornecer material narrativo reutilizável pelo Motor;
14. preservar a rastreabilidade até a afirmação e a evidência de origem.

---

# 7. LIMITES DA NT

A NT não deverá realizar nova busca científica durante sua construção.

Ela não poderá:

* criar PMID;
* criar DOI;
* inventar referências;
* criar claims científicos sem origem;
* aumentar o nível de evidência;
* transformar hipótese em fato;
* transformar associação em causalidade;
* converter uma relação mecanística em eficácia clínica sem sustentação.

A qualidade narrativa não poderá aumentar artificialmente a certeza científica.

A NT deverá preservar a distinção entre:

* fato;
* associação;
* causalidade;
* hipótese;
* evidência direta;
* extrapolação;
* lacuna científica.

---

# 8. AS NTs NÃO SÃO UMA ÚNICA FAMÍLIA

A arquitetura não deverá possuir somente NTs de mecanismos.

Haverá diferentes famílias de NTs.

Por exemplo:

```text
                         NARRATIVAS TRANSVERSAIS
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
        ▼                         ▼                         ▼
   NT MECANISMOS             NT SUPLEMENTOS              NT EXAMES
   B1 ... B16                S01 ...                    E01 ...
        │                         │                         │
        ├─────────────────────────┼─────────────────────────┤
        │                         │                         │
        ▼                         ▼                         ▼
 NT INTERVENÇÕES             NT CENÁRIOS               NT OUTROS
    I01 ...                    C01 ...                  ...
```

Cada NT mantém o seu próprio domínio.

Uma NT de suplemento não deve incorporar a Biblioteca de um mecanismo.

Uma NT de cenário não deve incorporar a Biblioteca de um exame.

Cada entidade permanece semanticamente independente.

A integração ocorre por meio das relações.

---

# 9. A NT NÃO É O GRAFO

Esta distinção é fundamental.

A NT não deve ser confundida com a Ontologia/Grafo.

A formulação correta é:

> **A NT constrói a representação semântica necessária para que o conhecimento possa ser formalizado e conectado por meio da Ontologia/Grafo.**

Por exemplo, uma NT mecanística pode identificar:

```text
Neuroinflamação
       │
       ├── envolve → NF-κB
       │
       ├── envolve → NLRP3
       │
       ├── relaciona-se → IDO
       │
       └── pode afetar → processos de neuroplasticidade
```

A NT organiza semanticamente essas relações.

A Ontologia/Grafo formaliza essas relações entre entidades.

---

# 10. A REDE MULTIDOMÍNIO

O grande objetivo da arquitetura transversal é permitir que os diferentes domínios sejam conectados.

Portanto, não teremos apenas:

```text
B1 ↔ B3
B1 ↔ B6
B1 ↔ B7
```

Teremos também:

```text
mecanismo ↔ suplemento

mecanismo ↔ exame

mecanismo ↔ intervenção

mecanismo ↔ cenário

cenário ↔ mecanismo

cenário ↔ exame

cenário ↔ intervenção

cenário ↔ suplemento
```

Conceitualmente:

```text
                         ┌─────────────────┐
                         │  NT MECANISMOS  │
                         │                 │
                         │ B1 ... B16      │
                         └────────┬────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
      ┌──────────────┐    ┌──────────────┐    ┌───────────────┐
      │NT SUPLEMENTOS│    │  NT EXAMES   │    │NT INTERVENÇÕES│
      └──────┬───────┘    └──────┬───────┘    └──────┬────────┘
             │                   │                   │
             └───────────────────┼───────────────────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │ NT CENÁRIOS   │
                         └───────┬───────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     ONTOLOGIA / GRAFO   │
                    │                         │
                    │     REDE MULTIDOMÍNIO   │
                    └─────────────────────────┘
```

---

# 11. EXEMPLO DE RELAÇÃO ENTRE DOMÍNIOS

Uma relação não deve ser simplesmente:

```text
B1 → Suplemento X
```

Isso é semanticamente insuficiente.

O modelo deve ser capaz de representar algo semelhante a:

```text
origem:
B1

destino:
S-X

tipo_relacao:
[relação definida pela ontologia]

direção:
B1 → S-X

condição:
[quando aplicável]

contexto:
[quando aplicável]

evidências:
[IDs das evidências]

claims:
[IDs das afirmações]

nivel_evidencia:
[metadado]

rastreabilidade:
[claim → evidência → biblioteca]
```

Assim, o sistema não interpreta automaticamente qualquer conexão como:

* indicação;
* eficácia;
* causalidade;
* tratamento;
* recomendação.

A semântica da relação deve determinar o que ela significa.

---

# 12. CENÁRIOS COMO CONTEXTUALIZADORES

As NTs de cenários poderão exercer uma função especialmente importante porque o cenário pode modificar a interpretação de outras relações.

Conceitualmente:

```text
                         CENÁRIO
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
         MECANISMO        EXAME       INTERVENÇÃO
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                        SUPLEMENTO
```

Isso não significa que o cenário cause o mecanismo ou que determinado suplemento seja automaticamente indicado.

Significa que o cenário pode fornecer **contexto semântico para a interpretação das relações existentes**.

---

# 13. NTs COMO UNIDADES DE EXPLICAÇÃO

A NT deverá produzir unidades narrativas reutilizáveis.

Essas unidades não devem ser simplesmente frases copiadas da Biblioteca e concatenadas.

Devem ser estruturas semanticamente completas.

Exemplo:

```text
UN_NARRATIVA_001

tema:
Neuroinflamação → Neuroplasticidade

origem:
B1

destino:
B3

tipo_relacao:
[relação]

condição:
[condição]

contexto:
[contexto]

evidências:
[IDs]

claims:
[IDs]

nivel_evidencia:
[metadado]

texto_explicativo:
[explicação científica]
```

A linguagem pode ser sofisticada, natural e didática.

Entretanto:

> **A qualidade da narrativa nunca poderá aumentar artificialmente a certeza científica.**

---

# 14. NT E LAUDO

A NT não deverá gerar diretamente o laudo.

Ela fornecerá unidades semânticas e narrativas para o Motor.

```text
                         NTs
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
          mecanismo     relação     condição
          explicado     explicada   contextual
              │           │           │
              └───────────┼───────────┘
                          ▼
                   MOTOR CLÍNICO
                          │
                          ▼
                       CONTEXTO
                          │
                          ▼
                  SELEÇÃO / COMBINAÇÃO
                          │
                          ▼
                        LAUDO
```

O objetivo é evitar que a IA precise "inventar" uma explicação científica do zero a cada laudo.

O Motor poderá selecionar e combinar estruturas previamente construídas, rastreáveis e semanticamente qualificadas.

---

# 15. ONTOLOGIA / GRAFO

A Ontologia/Grafo é a camada transversal responsável pela formalização das relações entre as diferentes entidades.

Ela deverá conectar:

```text
MECANISMOS
     ↕
SUPLEMENTOS
     ↕
EXAMES
     ↕
INTERVENÇÕES
     ↕
CENÁRIOS
     ↕
OUTROS DOMÍNIOS
```

A Ontologia/Grafo não substitui as Bibliotecas.

Também não substitui as Evidências.

E não substitui as NTs.

Ela formaliza as relações entre entidades que permanecem semanticamente independentes.

---

# 16. JSONs MODULARES

Os JSONs não deverão ser simples exportações textuais das NTs.

Eles constituem a representação computável dos elementos necessários ao Motor.

Portanto:

```text
BIBLIOTECA
     │
     ▼
 conhecimento canônico

NT
     │
     ▼
 semântica + relações + condições
 + unidades narrativas

ONTOLOGIA/GRAFO
     │
     ▼
 relações formais

JSON
     │
     ▼
 representação computável
```

Uma entidade poderá gerar:

```text
1 entidade
   │
   ├── JSON módulo A
   ├── JSON módulo B
   ├── JSON módulo C
   └── JSON módulo N
```

conforme a necessidade funcional.

---

# 17. CONTRATOS DO MOTOR CLÍNICO

Antes da geração definitiva dos JSONs, deverão ser definidos os contratos do Motor.

O contrato deverá especificar:

* entradas;
* IDs oficiais;
* estruturas JSON;
* relações;
* condições;
* evidências;
* metadados;
* regras de interpretação;
* estruturas de saída;
* rastreabilidade.

Conceitualmente:

```text
ENTRADAS
   │
   ├── IDs
   ├── contexto
   ├── relações
   ├── condições
   ├── evidências
   ├── metadados
   └── JSONs
        │
        ▼
   MOTOR CLÍNICO
        │
        ├── seleção
        ├── filtragem
        ├── combinação
        ├── contextualização
        └── rastreabilidade
        │
        ▼
      SAÍDAS
```

A definição prévia desses contratos evita reconstruções posteriores de centenas de módulos.

---

# 18. PASTA DE ATUALIZAÇÃO

A Pasta de Atualização representa uma camada diferente da Biblioteca Canônica.

Ela deverá receber conhecimento científico novo que ainda esteja no processo de avaliação, triagem, validação e eventual incorporação ao conhecimento canônico.

Portanto, não deverá ser tratada como uma segunda Biblioteca.

A arquitetura será:

```text
                      NOVA CIÊNCIA
                           │
                           ▼
                  ┌─────────────────┐
                  │ PASTA DE        │
                  │ ATUALIZAÇÃO     │
                  └────────┬────────┘
                           │
                 triagem / validação
                           │
                           ▼
                 incorporação formal
                           │
                           ▼
                 BIBLIOTECA CANÔNICA
                           │
                           ▼
                           NT
```

A existência de uma publicação na Pasta de Atualização não significa automaticamente que seu conteúdo já tenha se tornado conhecimento canônico.

---

# 19. O MOTOR TAMBÉM DEVERÁ CONSULTAR A PASTA DE ATUALIZAÇÃO

Essa é uma função distinta da incorporação canônica.

O Motor deverá possuir capacidade de consultar a Pasta de Atualização para identificar conhecimento científico recente que possa ser relevante para determinado contexto.

Assim:

```text
                         ┌────────────────────┐
                         │ BIBLIOTECA / NT /  │
                         │ JSONs CANÔNICOS    │
                         └─────────┬──────────┘
                                   │
                                   ▼
                              ┌─────────┐
                              │ MOTOR   │
                              └────┬────┘
                                   ▲
                                   │
                         ┌─────────┴─────────┐
                         │ PASTA DE          │
                         │ ATUALIZAÇÃO       │
                         │                   │
                         │ ciência recente   │
                         └───────────────────┘
```

As duas fontes possuem papéis diferentes:

```text
CANÔNICO
   =
conhecimento incorporado,
auditado e estruturado

ATUALIZAÇÃO
   =
conhecimento recente,
em acompanhamento/avaliação
```

O Motor não deverá automaticamente tratar uma informação da Pasta de Atualização como equivalente ao conhecimento canônico.

A forma como essa informação será utilizada — por exemplo, alerta, atualização, comparação, enriquecimento ou outra modalidade — deverá ser definida posteriormente no contrato do Motor.

---

# 20. DUPLO FLUXO DE CONHECIMENTO

A arquitetura completa possui dois fluxos complementares.

## FLUXO CANÔNICO

```text
CIÊNCIA
   ↓
SELEÇÃO / ANÁLISE
   ↓
EVIDÊNCIA
   ↓
BIBLIOTECA CANÔNICA
   ↓
NT
   ↓
ONTOLOGIA / GRAFO
   ↓
JSONs
   ↓
MOTOR
```

## FLUXO DE ATUALIZAÇÃO

```text
NOVA CIÊNCIA
   ↓
PASTA DE ATUALIZAÇÃO
   ↓
ANÁLISE / TRIAGEM / VALIDAÇÃO
   │
   ├──────────────► incorporação futura
   │                      │
   │                      ▼
   │                BIBLIOTECA
   │
   └──────────────► consulta pelo MOTOR
                          │
                          ▼
                   conhecimento recente
```

Os dois fluxos coexistem, mas não possuem o mesmo status epistemológico.

---

# 21. ARQUITETURA MULTIDOMÍNIO COMPLETA

```text

							  CIÊNCIA
                                  │
                   ┌──────────────┴──────────────┐
                   │                             │
                   ▼                             ▼
        ┌────────────────────┐         ┌────────────────────┐
        │ BIBLIOTECAS        │         │ PASTA DE           │
        │ CANÔNICAS          │         │ ATUALIZAÇÃO        │
        └─────────┬──────────┘         └─────────┬──────────┘
                  │                              │
                  ├──────────────┐               │
                  │              │               │
                  ▼              ▼               │
        ┌────────────────┐  ┌────────────────┐   │
        │ EVIDÊNCIAS     │  │ NARRATIVAS     │   │
        │ BIBLIOGRÁFICAS │  │ TRANSVERSAIS   │   │
        └───────┬────────┘  └───────┬────────┘   │
                │                   │             │
                ▼                   │             │
        ┌────────────────┐          │             │
        │ EVIDÊNCIAS /   │◄─────────┘             │
        │ VÍNCULOS       │                        │
        └───────┬────────┘                        │
                │                                 │
                └────────────────┬────────────────┘
                                 ▼
                    ┌────────────────────────┐
                    │    ONTOLOGIA / GRAFO   │
                    │                        │
                    │ relações multidomínio  │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │     JSONs MODULARES     │
                    └───────────┬────────────┘
                                │
                                ▼
                         ┌─────────────┐
                         │    MOTOR    │
                         │   CLÍNICO   │
                         └──────┬──────┘
                                ▲
                                │
                     ┌──────────┴──────────┐
                     │      ANAMNESE       │
                     │   CONTEXTO DO CASO  │
                     └─────────────────────┘
                                │
                                ▼
                       INTERPRETAÇÃO
                       CONTEXTUALIZADA
                                │
                  ┌─────────────┼─────────────┐
                  ▼             ▼             ▼
             MECANÍSTICA     CLÍNICA      TERAPÊUTICA
             SUGESTÃO        SUGESTÃO      SUGESTÃO
                  │             │             │
                  └─────────────┼─────────────┘
                                ▼
                       EXPLICAÇÃO NARRATIVA
                                │
                                ▼
                              LAUDO
```

---

# 22. CADEIA DE AUTORIDADE CIENTÍFICA

A autoridade científica deverá permanecer:

```text
EVIDÊNCIA
   ↓
AFIRMAÇÃO VALIDADA
   ↓
BIBLIOTECA CANÔNICA
   ↓
NT
   ↓
ESTRUTURA SEMÂNTICA
   ↓
JSON
   ↓
MOTOR
   ↓
SAÍDA
```

A Pasta de Atualização constitui uma rota paralela de conhecimento recente e não altera automaticamente essa cadeia.

Nenhuma camada posterior poderá:

* inventar evidência;
* inventar referências;
* criar claims científicos sem origem;
* aumentar o grau de certeza;
* transformar associação em causalidade;
* transformar hipótese em fato.

---

# 23. FLUXO CLÍNICO DA PLATAFORMA

Após a construção e integração do conhecimento científico pelas Bibliotecas Canônicas, Evidências/Vínculos, Narrativas Transversais, Ontologia/Grafo e JSONs Modulares, esse conhecimento é disponibilizado ao Motor Clínico.

Durante a utilização da plataforma, a anamnese estruturada, juntamente com os demais dados clínicos disponíveis, fornece o contexto necessário para que o Motor Clínico analise o caso à luz do conhecimento científico estruturado.

O Motor realiza a análise e a inferência computacional das relações pertinentes ao contexto apresentado, preservando a rastreabilidade das informações utilizadas.

Como resultado, a plataforma produz um laudo/relatório técnico de apoio ao raciocínio clínico integrativo, contendo os achados, possíveis mecanismos envolvidos, relações relevantes, evidências, explicações científicas e sugestões auxiliares compatíveis com os dados analisados.

O laudo constitui suporte à avaliação profissional.

Cabe ao profissional responsável analisar criticamente os resultados apresentados, considerando o contexto clínico completo, e tomar a decisão clínica final.

Assim, a plataforma não realiza diagnóstico nem substitui o julgamento clínico profissional.

Sua função é apoiar o raciocínio clínico integrativo por meio de conhecimento científico estruturado, rastreável e contextualizado.

---

# 24. DEFINIÇÃO CONSOLIDADA DA PLATAFORMA

A plataforma deve ser compreendida como uma:

> **Plataforma de apoio ao raciocínio clínico integrativo, baseada em conhecimento científico estruturado, auditado e rastreável, capaz de contextualizar informações clínicas individuais, relacioná-las ao conhecimento científico da arquitetura e produzir análises, explicações e sugestões auxiliares para avaliação do profissional responsável.**

Sua arquitetura integra:

**Bibliotecas Canônicas → Evidências/Vínculos → Narrativas Transversais → Ontologia/Grafo → JSONs Modulares → Motor Clínico**

e, durante sua utilização:

**Anamnese e dados clínicos → Motor Clínico → análise contextualizada → laudo/relatório → avaliação profissional → decisão clínica final.**

A autoridade científica permanece nas fontes canônicas e em suas evidências, enquanto o Motor realiza a aplicação contextual desse conhecimento ao caso apresentado.

A plataforma, portanto, não substitui o profissional nem toma a decisão clínica final; ela fornece suporte estruturado para que o profissional possa exercer seu próprio raciocínio clínico integrativo com maior organização, rastreabilidade e fundamentação científica.

---

# 25. PRINCÍPIO FUNDAMENTAL

A arquitetura deve obedecer ao seguinte princípio:

> **A ciência não deve se encaixar no claim; o claim é que deve se encaixar na ciência.**

Consequentemente:

**Biblioteca preserva a ciência.**

**Evidências preservam a sustentação.**

**Vínculos preservam a relação entre evidência, claim e entidade.**

**NT preserva o significado, as relações e a capacidade de explicação.**

**Ontologia/Grafo preserva a estrutura transversal das relações.**

**JSON preserva a representação computável.**

**Motor preserva a aplicação contextual.**

**Pasta de Atualização preserva o fluxo de acompanhamento da ciência recente.**

Nenhuma camada posterior deverá possuir autoridade para aumentar artificialmente a certeza científica estabelecida pelas camadas anteriores.

---

# 26. PRIMEIRO PILOTO DE INTEGRAÇÃO

A arquitetura será inicialmente validada por meio de um **piloto vertical**, utilizando a B1 — Neuroinflamação como primeira entidade.

A B1 já possui sua Biblioteca Canônica e passou pelo processo de auditoria.

O objetivo agora não é esperar a conclusão de todas as demais bibliotecas para testar a engenharia.

O primeiro fluxo será:

```text
B1
Biblioteca Canônica auditada
        │
        ▼
NT B1
        │
        ▼
Ontologia / Grafo B1
        │
        ▼
JSONs B1
        │
        ▼
Motor Clínico
        │
        ▼
Teste de raciocínio
```

A utilização da B1 nesse piloto serve para validar:

* contratos;
* estruturas;
* integração;
* rastreabilidade;
* geração da NT;
* formalização ontológica;
* geração dos JSONs;
* consumo pelo Motor;
* comportamento do raciocínio computacional.

A utilização da B1 como piloto de engenharia não significa que qualquer conteúdo ainda não homologado cientificamente deva ser tratado como conhecimento final do sistema.

A validação estrutural e a validação científica são dimensões distintas.

---

# 27. EXPANSÃO MULTIDOMÍNIO DO PILOTO

Após a validação do fluxo B1, o piloto deverá incorporar entidades de outros domínios.

Conceitualmente:

```text
B1
 │
 ├──── Suplemento
 │
 ├──── Exame / Biomarcador
 │
 ├──── Cenário
 │
 └──── Intervenção
```

Cada entidade deverá preservar sua própria:

**Biblioteca → NT → JSON(s)**

e sua própria identidade oficial.

A integração ocorrerá por meio da:

**Ontologia/Grafo + Evidências/Vínculos**

O objetivo dessa etapa é testar as relações multidomínio antes da replicação da arquitetura para os demais IDs oficiais.

---

# 28. REGRA PARA O DESENVOLVIMENTO DO MOTOR

O Motor Clínico poderá ser desenvolvido em paralelo à construção das NTs, desde que seja construído contra os contratos da arquitetura consolidada.

O Motor não deverá assumir que a Biblioteca Canônica é a camada final de consumo.

Ele deverá respeitar a cadeia:

```text
Biblioteca
    ↓
NT
    ↓
Ontologia / Grafo
    ↓
JSONs
    ↓
Motor
```

e utilizar a infraestrutura de Evidências/Vínculos para preservar a rastreabilidade.

Como a NT é uma camada semântica intermediária, o Motor deverá ser projetado para consumir estruturas semânticas e computáveis já qualificadas, em vez de depender da geração espontânea de explicações científicas a cada caso.

---

# 29. DIVISÃO DE RESPONSABILIDADES NO PILOTO

A arquitetura permite que diferentes etapas sejam desenvolvidas por ferramentas ou agentes diferentes, desde que todos respeitem os mesmos contratos.

No piloto atual:

### Auditoria científica B1

Responsável por garantir a qualidade, consistência e conformidade da Biblioteca Canônica B1.

### Construção da NT

Responsável por transformar o conhecimento canônico auditado em estrutura semântica narrativa, sem criar ciência nova.

### Ontologia/Grafo

Responsável por formalizar as relações identificadas e sustentadas.

### JSONs Modulares

Responsáveis pela representação computável dos elementos necessários ao Motor.

### Motor Clínico

Responsável pela seleção, filtragem, combinação e contextualização computacional das informações diante dos dados clínicos apresentados.

Nenhuma dessas etapas deve alterar silenciosamente a autoridade científica da etapa anterior.

---

# 30. SÍNTESE FINAL

A plataforma deve ser compreendida como uma:

> **rede multidomínio de conhecimento científico estruturado, auditado, rastreável e computável, destinada a apoiar o raciocínio clínico integrativo do profissional de saúde.**

Sua arquitetura fundamental é:

```text
                         CONHECIMENTO CIENTÍFICO
                                  │
                  ┌───────────────┴───────────────┐
                  │                               │
                  ▼                               ▼
              CANÔNICO                       ATUALIZAÇÃO
                  │                               │
                  ▼                               │
             BIBLIOTECA                           │
                  │                               │
          ┌───────┴────────┐                      │
          ▼                ▼                      │
     EVIDÊNCIAS          NTs                      │
     BIBLIOGRÁFICAS       │                       │
          │                ▼                       │
          ▼         ONTOLOGIA / GRAFO             │
       VÍNCULOS            │                       │
          │                ▼                       │
          └───────────►  JSONs ◄─────────────────┘
                           │
                           ▼
                         MOTOR
                           │
                           ▼
                        CONTEXTO
                           │
                           ▼
                  ANÁLISE CONTEXTUALIZADA
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           sugestão    explicação    narrativa
           científica  contextual   contextual
              │            │            │
              └────────────┼────────────┘
                           ▼
                         LAUDO
                           │
                           ▼
                AVALIAÇÃO PROFISSIONAL
                           │
                           ▼
                  DECISÃO FINAL DO
                    PROFISSIONAL
```

A arquitetura preserva simultaneamente:

**ciência → evidência → rastreabilidade → semântica → relações → computabilidade → atualização → contextualização → apoio ao raciocínio clínico.**
