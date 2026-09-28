# PROPOSTA DE FORMALIZAÇÃO DO FLUXO DOS CLAIMS CLÍNICOS

**Documento para análise conjunta — Auditor-Mestre e Auditor de Estrutura**

**Status:** proposta para validação
**Finalidade:** formalizar o papel do Claim Clínico e seu fluxo até Evidências/Bibliografia, eliminando ambiguidades antes da consolidação do Contrato das Unidades Narrativas.

---

## 1. Contexto

Em rodada anterior, foi estabelecida uma decisão arquitetural importante:

> **O Claim Clínico não integra a Biblioteca Canônica como entidade de conhecimento.**

Após sua aprovação, o Claim Clínico deve alimentar diretamente a camada de **Evidências/Bibliografia**.

Essa decisão permanece como premissa desta proposta.

O ponto que permaneceu sem formalização suficiente é:

> **Como ocorre operacionalmente a entrada de um Claim Clínico aprovado em Evidências/Bibliografia?**

Durante o desenvolvimento do projeto, o Claim Kit Clínico passou a possuir ferramentas próprias para:

* protocolo de escopo;
* Schema-Claim;
* Lista Canônica;
* Bloco de Estado;
* busca científica com PubMed/E-utilities;
* G1;
* G2;
* G3;
* auditoria por múltiplas IAs;
* fechamento do claim como aprovado, aprovado com ressalva ou rejeitado.

Além disso, a aplicação prática do Claim Kit identificou e resolveu lacunas que não haviam sido solucionadas adequadamente pelo fluxo geral de busca mecanística/clínica.

Por isso, antes de sua eventual aposentadoria ou incorporação parcial, propõe-se formalizar seu papel e testar sua integração com a arquitetura já desenvolvida.

---

# 2. Distinção fundamental

Devem ser mantidos separados três objetos:

### 2.1 Claim Clínico

É uma **afirmação científica que está sendo submetida a validação**.

Exemplo:

```text
B1.SM02.014
```

O Claim Kit trabalha principalmente neste nível.

---

### 2.2 N1 — Registro da Referência

Depois que uma evidência é aceita para determinado claim, o artigo é registrado segundo o contrato L-05 N1:

`L05/schema_referencia_v1.3.json`

N1 representa a referência bibliográfica.

Em termos simples:

> **N1 = “Que artigo é este?”**

Contém, entre outros elementos:

* PMID;
* título;
* autores;
* DOI;
* natureza da evidência;
* desenho do estudo;
* origem do pipeline;
* método G1;
* estado de verificação;
* demais metadados exigidos pelo schema.

---

### 2.3 N2 — Vínculo da Evidência

Depois é registrada a relação entre a referência, o claim e as entidades envolvidas, segundo:

`L05/schema_vinculo_v1.4.json`

Em termos simples:

> **N2 = “O que exatamente este artigo sustenta em relação a este claim e a quais entidades?”**

N2 registra, entre outros elementos:

* referência de origem;
* claim;
* trecho-âncora;
* entidades oficiais;
* papel da âncora;
* direção do suporte;
* trilha;
* uso;
* natureza da relação;
* força causal quando aplicável;
* grau de maturidade;
* estado de verificação.

---

# 3. Fluxo formal proposto

O fluxo passa a ser entendido da seguinte forma:

```text
CLAIM CLÍNICO
      │
      ▼
CLAIM KIT
      │
      ├── Protocolo de Escopo
      ├── Schema-Claim
      ├── Lista Canônica
      ├── Bloco de Estado
      ├── Busca PubMed / E-utilities
      └── G1 → G2 → G3
                  │
                  ▼
           Auditorias do Claim
                  │
                  ▼
       ┌─────────────────────────┐
       │ APROVADO                │
       │ APROVADO COM RESSALVA   │
       │ REJEITADO               │
       └────────────┬────────────┘
                    │
                    ▼
             EVIDÊNCIAS/
             BIBLIOGRAFIA
                    │
                    ▼
             N1 — REFERÊNCIA
                    │
                    ▼
             N2 — VÍNCULO
                    │
                    ▼
        NT / ONTOLOGIA / GRAFO
                    │
                    ▼
             JSONs MODULARES
                    │
                    ▼
                 MOTOR
```

Assim, a expressão:

> “o claim aprovado vai para Evidências/Bibliografia”

passa a ter significado operacional preciso.

Ela **não significa que o objeto Claim simplesmente seja copiado para uma pasta**.

Significa que:

1. o claim permanece como objeto de origem/auditoria;
2. as referências aceitas são materializadas em registros N1;
3. os vínculos entre referência, claim e entidades são materializados em N2;
4. esses registros passam a integrar a camada estruturada de Evidências/Bibliografia.

---

# 4. Papel do Claim Kit

O Claim Kit não deve ser confundido com L-05.

### Claim Kit

Responsável pela etapa anterior:

> **descobrir, selecionar, analisar e fechar claims clínicos e suas evidências.**

### L-05

Responsável pela etapa posterior:

> **formalizar e validar estruturalmente referências e vínculos de evidência.**

Portanto:

```text
CLAIM KIT
= validação e fechamento do claim

L-05 N1/N2
= formalização da evidência e do vínculo
```

Um não precisa substituir o outro.

---

# 5. Papel do Auditor-Mestre e do Auditor de Estrutura

Propõe-se manter a separação de responsabilidades.

## Auditor-Mestre

Recebe o material clínico já fechado e coordena a transformação do resultado em N1/N2 conforme os contratos vigentes.

Seu papel não é simplesmente repetir a auditoria científica dos 35 claims.

Ele deve garantir que a transição:

```text
Claim aprovado
      ↓
Evidência
      ↓
N1
      ↓
N2
```

seja compatível com a arquitetura e com os contratos existentes.

---

## Auditor de Estrutura

Recebe os N1/N2 produzidos e verifica sua conformidade estrutural com:

* `schema_referencia_v1.3.json`;
* `schema_vinculo_v1.4.json`;
* gates;
* enums;
* campos obrigatórios;
* relações entre campos;
* regras L-05.

Portanto, a sequência proposta é:

```text
CLAIM KIT
   ↓
AUDITOR-MESTRE
   ↓
AUDITOR DE ESTRUTURA
```

e não os dois realizando simultaneamente a mesma tarefa.

---

# 6. O que acontece com o Claim Kit após a aprovação?

O Claim Kit não precisa entrar no Motor.

Também não precisa produzir diretamente os JSONs que o Motor utilizará.

Sua posição proposta é:

```text
                  CLAIM KIT
                      │
                      ▼
               CLAIM APROVADO
                      │
                      ▼
             EVIDÊNCIAS/BIBLIOGRAFIA
                      │
                 ┌────┴────┐
                 ▼         ▼
                N1        N2
                 └────┬────┘
                      ▼
              camadas posteriores
```

Assim, o Claim Kit permanece como **camada upstream de curadoria clínica**, e não como uma segunda camada do Motor.

---

# 7. Relação com os 35 claims B1

Os 35 claims clínicos de B1 constituem um primeiro conjunto adequado para testar o fluxo.

A proposta é:

1. concluir os 35 claims;
2. fechar suas respectivas auditorias;
3. consolidar seus resultados;
4. interromper a expansão temporariamente;
5. realizar a primeira passagem de materialização para N1/N2;
6. validar essa passagem;
7. avaliar se o fluxo funciona como esperado;
8. somente então aplicar o mesmo processo aos demais mecanismos.

Isso permite que B1 funcione como piloto controlado.

---

# 8. O Claim Clínico pertence somente aos mecanismos B1–B16?

Não se propõe essa restrição.

Os mecanismos B1–B16 constituem um domínio importante, mas a arquitetura possui aproximadamente 146 entidades oficiais distribuídas em diferentes domínios.

Há, por exemplo:

* mecanismos;
* intervenções;
* suplementos;
* exames;
* cenários;
* nutrição;
* fitoterapia;
* sono;
* exercício;
* outros domínios oficiais.

O Claim Clínico deve ser entendido como **uma ferramenta transversal para afirmações clínicas que necessitem de validação científica estruturada**, e não como uma ferramenta exclusiva dos mecanismos.

Portanto:

```text
                 CLAIM CLÍNICO
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      MECANISMO    INTERVENÇÃO   SUPLEMENTO
          │            │            │
          ▼            ▼            ▼
       evidência    evidência    evidência
          │            │            │
          └────────────┼────────────┘
                       ▼
                EVIDÊNCIAS/N1/N2
```

O fato de um claim ter como origem um mecanismo não impede que suas âncoras N2 também envolvam outras entidades oficiais.

Por exemplo, uma afirmação clínica pode envolver simultaneamente:

```text
Mecanismo
    ↕
Biomarcador
    ↕
Intervenção
    ↕
Suplemento
    ↕
Cenário clínico
```

O N2 é justamente uma das camadas que permite registrar essas relações de maneira estruturada.

---

# 9. O que não deve acontecer

O Claim Kit não deve:

* transformar automaticamente um claim aprovado em conhecimento canônico;
* substituir a Biblioteca Canônica;
* gerar diretamente uma recomendação do Motor;
* elevar uma evidência apenas porque o claim foi aprovado;
* transformar evidência pré-clínica em evidência clínica;
* substituir os contratos L-05;
* ser incorporado ao Motor como uma segunda base paralela.

Da mesma forma, N1/N2 não devem ser utilizados para recriar o Claim Kit.

---

# 10. Questão específica para deliberação

Solicita-se aos Auditores-Mestre e de Estrutura avaliar se o fluxo abaixo deve ser formalizado como fluxo oficial:

```text
Claim Kit
   ↓
Claim clínico fechado
   ↓
Evidências/Bibliografia
   ↓
N1 — Registro da Referência
   ↓
N2 — Vínculo Evidência ↔ Claim ↔ Entidades
   ↓
NT / Ontologia / Grafo
   ↓
JSONs Modulares
   ↓
Motor
```

Também deve ser definida a forma de entrada do Claim Kit no estágio N1/N2:

* quais campos do Claim Kit serão preservados;
* quais campos serão transformados;
* quais informações serão utilizadas para gerar N1;
* quais informações serão utilizadas para gerar N2;
* quais campos precisarão ser preenchidos posteriormente;
* quais tarefas poderão ser automatizadas por script;
* quais tarefas exigirão análise/auditoria.

---

# 11. Proposta de ferramenta de transição

Não se propõe neste momento alterar as seis ferramentas do Claim Kit.

Após o fechamento dos 35 claims, deverá ser avaliada a criação de um **derivador/materializador** que receba a saída consolidada do Claim Kit e produza:

```text
Claim Kit
   ↓
dados consolidados
   ↓
Gerador N1
   ↓
Gerador N2
   ↓
Validador L-05
```

Essa ferramenta poderá utilizar Python, PubMed/E-utilities e validação JSON Schema, mas sua especificação deve ser definida somente após a confirmação do fluxo pelos auditores.

---

# 12. Sequência proposta para os mecanismos

Após o piloto B1:

```text
B1
 ↓
piloto completo
 ↓
validação do fluxo
 ↓
B2
 ↓
B3
 ↓
...
 ↓
B16
```

O objetivo é evitar que cada mecanismo desenvolva uma interpretação própria do processo.

O fluxo aprovado para B1 deve tornar-se o padrão reutilizável para os demais mecanismos.

Posteriormente, deverá ser avaliada a aplicação do mesmo modelo aos demais domínios dos 146 IDs oficiais.

---

# 13. Decisões que devem ser registradas

Para evitar reabertura futura da mesma questão, recomenda-se registrar formalmente:

1. posição do Claim Clínico na arquitetura;
2. relação Claim Kit → Evidências/Bibliografia;
3. definição operacional de N1;
4. definição operacional de N2;
5. responsabilidade do Auditor-Mestre;
6. responsabilidade do Auditor de Estrutura;
7. formato de entrada do Claim Kit;
8. formato de saída N1/N2;
9. ferramentas/scripts responsáveis pela materialização;
10. momento em que o Claim Kit deixa de atuar;
11. relação entre claims e os 146 IDs;
12. critérios para decidir quando um novo domínio necessita de claims clínicos;
13. procedimento de auditoria para claims aprovados com ressalva;
14. procedimento de versionamento e rastreabilidade.

---

# 14. Proposta de decisão

A presente documentação não pretende alterar unilateralmente os contratos já estabelecidos.

Propõe-se que os dois Auditores analisem o fluxo e indiquem:

**A — concordância integral;**

**B — concordância com ajustes;**

**C — necessidade de alteração arquitetural;**

**D — necessidade de manutenção do Claim Kit apenas como ferramenta auxiliar.**

Após essa deliberação, a decisão deverá ser registrada antes da continuidade das etapas dependentes.

---

## Conclusão

A questão central não é decidir se o Claim Kit substitui L-05.

A proposta é estabelecer uma separação clara:

> **Claim Kit valida o claim e seleciona/fecha sua evidência.**

> **L-05 formaliza a referência e o vínculo dessa evidência.**

> **Os contratos posteriores utilizam essa informação estruturada.**

O Claim Clínico, portanto, não precisa entrar na Biblioteca Canônica para ser útil à arquitetura. Ele pode funcionar como uma camada especializada de curadoria científica que alimenta a camada de Evidências/Bibliografia, mantendo rastreabilidade entre:

**claim → artigo → vínculo → entidade → camadas posteriores → Motor.**
