# SOLUÇÃO DO COMENTADOR — D1

## Claim Clínico → Biblioteca → N1/N2

**Rodada de resolução da divergência D1**
**Data:** 2026-09-24
**Origem:** Comentador
**Base:** Pareceres territoriais de 2026-09-23 + Confronto da Rodada 78 + Trilha 89

---

# 1. OBJETO

A Rodada 78 identificou uma única divergência material entre os territórios:

> **Como materializar `aprovado_com_ressalva` no N2?**

O Auditor-Estrutura mantém o mapeamento:

```text
aprovado_com_ressalva
→ PARCIALMENTE_CONFIRMADO
→ direcao_suporte = condicional
→ condicao obrigatória
```

O Auditor-Mestre demonstra que esse mapeamento é epistemologicamente excessivo porque **ressalva e condição de aplicação não são conceitos equivalentes**.

Depois de analisar os dois pareceres junto ao funcionamento real do Claim Kit, proponho não escolher uma das duas estruturas de forma integral.

A solução é **separar os dois eixos semânticos**.

---

# 2. DIAGNÓSTICO

O problema nasce porque dois campos diferentes estão sendo usados para representar uma única informação composta.

### Eixo A — estado da validação

O Claim responde:

> “A afirmação foi considerada sustentada pelo processo de validação?”

O Claim Kit já possui:

```text
status:
  aprovado
  aprovado_com_ressalva
```

No N2, isso pode ser refletido por:

```text
CONFIRMADO
PARCIALMENTE_CONFIRMADO
```

### Eixo B — relação da evidência com a afirmação

O N2 responde outra pergunta:

> “Qual é a direção da relação entre esta evidência e esta afirmação?”

Porque existem:

```text
sustenta
refuta
inconclusivo
condicional
```

Esses dois eixos não devem ser colapsados.

---

# 3. DECISÃO DE MODELAGEM

A regra proposta pelo Comentador é:

> **`aprovado_com_ressalva` não determina automaticamente `direcao_suporte = condicional`.**

A ressalva deve ser classificada segundo seu significado científico.

A regra fica:

```text
STATUS DO CLAIM
        ↓
determina o estado de confirmação

RELAÇÃO EVIDENCIAL
        ↓
determina direcao_suporte
```

Em termos de engenharia:

> **estado de validação ≠ direção da evidência.**

Esta é a separação que resolve D1.

---

# 4. NOVA REGRA DE MATERIALIZAÇÃO

## 4.1 Claim sem ressalva

```text
status = aprovado
→ status_auditoria = CONFIRMADO
→ direcao_suporte = conforme a relação científica efetiva
→ condicao = null
```

A direção não é inventada a partir do status.

Ela é determinada pela relação real entre fonte e afirmação.

---

## 4.2 Claim com ressalva de condição de aplicação

Exemplo conceitual:

> “A associação ocorre em mulheres, mas não foi demonstrada em homens.”

Neste caso existe realmente uma condição.

```text
status = aprovado_com_ressalva
→ status_auditoria = PARCIALMENTE_CONFIRMADO
→ direcao_suporte = condicional
→ condicao = condição literal aprovada
```

Aqui a representação `condicional` é correta.

---

## 4.3 Claim com ressalva de heterogeneidade ou inconsistência

Exemplo real do kit:

> “Efeito por sexo diverge entre estudos.”

Isto **não constitui automaticamente uma condição de aplicação**.

Portanto:

```text
status = aprovado_com_ressalva
→ status_auditoria = PARCIALMENTE_CONFIRMADO
→ direcao_suporte = sustenta
  (ou refuta/inconclusivo, conforme a relação efetiva)
→ condicao = null
```

A ressalva completa permanece no Claim Kit, vinculada ao mesmo `claim_id`.

Nenhuma condição é fabricada.

---

## 4.4 Claim com ressalva de maturidade/limitação da evidência

Exemplo:

> “Achado preliminar, baseado em uma única coorte.”

A ressalva caracteriza maturidade/limitação da evidência, e não uma condição lógica de aplicação.

Portanto:

```text
status = aprovado_com_ressalva
→ status_auditoria = PARCIALMENTE_CONFIRMADO
→ direcao_suporte = relação efetiva da evidência
→ condicao = null
```

Quando houver eixo de maturidade aplicável no contrato N2, ele poderá representar a limitação segundo seu próprio significado.

Não se utiliza `condicional` apenas para evitar a perda da ressalva.

---

# 5. CONSEQUÊNCIA FUNDAMENTAL

A regra:

```text
aprovado_com_ressalva → condicional
```

fica abolida.

A regra passa a ser:

```text
aprovado_com_ressalva
        ↓
PARCIALMENTE_CONFIRMADO

e, independentemente:

tipo real da ressalva
        ↓
define se existe ou não condicao
```

Assim:

> **toda condição é uma ressalva, mas nem toda ressalva é uma condição.**

Esta é a relação lógica correta entre os dois conceitos.

---

# 6. O QUE DEVE SER ACRESCENTADO AO CLAIM KIT

O ponto em que a decisão científica precisa acontecer é **antes da materialização**.

O materializador não pode ler uma frase livre e decidir sozinho se ela representa heterogeneidade, maturidade ou condição.

Para tornar isso determinístico, proponho acrescentar ao contrato de saída do Claim Kit uma classificação estruturada da ressalva.

Em vez de utilizar apenas:

```text
nota_ressalva
```

o Claim aprovado deverá permitir registrar, quando houver ressalva, algo equivalente a:

```text
ressalvas:
  - tipo: heterogeneidade
    nota: "Efeito por sexo diverge entre estudos..."
```

ou

```text
ressalvas:
  - tipo: condicao_aplicacao
    nota: "Associação demonstrada em mulheres..."
    condicao: "sexo feminino"
```

ou

```text
ressalvas:
  - tipo: maturidade_evidencia
    nota: "Achado preliminar..."
```

O campo exato, o vocabulário definitivo e a possibilidade de múltiplas ressalvas devem ser definidos no contrato do Claim Kit antes da primeira materialização.

A proposta não pressupõe alteração imediata do N2.

---

# 7. POR QUE ESSA CLASSIFICAÇÃO DEVE SER FEITA NO PROCESSO DE CLAIM

A classificação da ressalva é uma decisão científica.

Ela não deve ser realizada pelo materializador como inferência.

Portanto, ela pertence ao fluxo que o operador já utiliza:

```text
artigos
   ↓
3 IAs independentes
   ↓
análise
   ↓
comparação
   ↓
aprovação do claim
   ↓
classificação da ressalva
   ↓
Claim fechado
   ↓
materialização
```

Isso é compatível com o fato de o operador já produzir e auditar os Claims Clínicos.

A materialização passa a ser mais mecânica porque recebe a classificação já decidida.

---

# 8. PAPEL DO AUDITOR CIENTÍFICO

A classificação da ressalva não deve ser aceita apenas porque foi escrita no Claim Kit.

Ela passa a fazer parte da fidelidade científica que precisa ser auditada:

> “A ressalva classificada como condição é realmente uma condição?”

> “A ressalva classificada como heterogeneidade realmente expressa heterogeneidade?”

> “A classificação preserva o que a fonte primária permite afirmar?”

Portanto, o Auditor científico/adversarial deve verificar a **classificação semântica da ressalva**.

Isso é diferente da checagem mecânica da cópia.

---

# 9. PAPEL DO AUDITOR-ESTRUTURA

O Auditor-Estrutura continua podendo executar os testes mecânicos já identificados:

### Se `direcao_suporte = condicional`

```text
condicao != null
```

### Se `direcao_suporte ∈ {sustenta, refuta, inconclusivo}`

```text
condicao = null
```

### Se o contrato determinar que determinada classe de ressalva exige determinado destino

o teste de conformidade pode verificar a correspondência.

O Auditor-Estrutura não precisa decidir o significado científico da ressalva.

Ele verifica se a materialização respeitou o significado já decidido.

---

# 10. E-6 FICA RESOLVIDA EM DUAS CAMADAS

A discussão anterior sobre E-6 fica mais clara.

Existem duas operações diferentes:

### Operação A — classificação

> “Esta ressalva é uma condição de aplicação?”

**É decisão científica.**

### Operação B — preservação

> “A `condicao` materializada é idêntica à condição aprovada?”

**É comparação mecânica.**

Portanto:

```text
classificar → auditoria científica
preservar → teste mecânico
```

As duas podem coexistir sem conflito.

A objeção do Auditor-Estrutura contra autoauditoria continua válida.

---

# 11. O CLAIM CONTINUA SENDO A FONTE COMPLETA DA RESSALVA

Não proponho copiar toda `nota_ressalva` para o N2.

O Claim Kit continua contendo a informação completa do processo.

O N2 recebe somente os elementos que pertencem ao seu próprio contrato.

A ligação:

```text
N2.claim_id → Claim
```

permite retornar ao registro completo.

Isso evita criar duplicações desnecessárias.

Quando houver uma condição propriamente dita, a condição necessária ao N2 é materializada em `condicao`.

Quando não houver condição, `condicao` permanece `null`.

---

# 12. O EXEMPLO DO CLAIM B1.SM02.001

O Claim possui:

```text
status: aprovado_com_ressalva

nota_ressalva:
"Efeito por sexo diverge entre estudos — ver .001b"
```

Pela solução proposta:

```text
tipo_ressalva:
heterogeneidade
```

O N2 não recebe:

```text
direcao_suporte = condicional
```

simplesmente porque existe uma ressalva.

Ele recebe:

```text
status_auditoria = PARCIALMENTE_CONFIRMADO
```

e mantém a direção real da relação evidencial.

`condicao = null`.

A informação científica não é inventada.

---

# 13. O QUE ESTA SOLUÇÃO PRESERVA DOS DOIS PARECERES

### Do Auditor-Estrutura

Preserva:

* o N2 vigente;
* os enums existentes;
* a obrigatoriedade de `condicao` quando `condicional`;
* a proibição de `condicao` quando não condicional;
* a verificação mecânica;
* a segregação de auditoria;
* a menor alteração arquitetural.

### Do Auditor-Mestre

Preserva:

* a distinção entre ressalva e condição;
* a proibição de inferência silenciosa;
* a proteção contra fabricação de condição;
* a integridade da L-06;
* a exigência de auditoria científica da semântica;
* a não transformação de uma limitação em regra de aplicação.

Portanto, a solução não precisa “vencer” um parecer contra o outro.

Ela **separa o problema que os dois estavam tentando representar no mesmo campo**.

---

# 14. IMPACTO NO N2

A principal consequência é positiva:

> **Não é necessária uma nova arquitetura N2 para resolver D1.**

O N2 v1.4 já possui:

```text
status_auditoria
direcao_suporte
condicao
```

O que estava errado era a regra de derivação entre campos do Claim.

A mudança principal é no **contrato Claim Kit → N2**, não na estrutura básica do N2.

---

# 15. IMPACTO NA V1.10

D1 não exige reabrir toda a arquitetura do COMO EXECUTAR.

A v1.10 deverá apenas garantir que:

1. o claim com ressalva tenha a ressalva explicitamente registrada;
2. o tipo da ressalva seja definido durante o fechamento;
3. a classificação seja auditável;
4. o materializador não invente `condicao`;
5. o fechamento preserve a ressalva original.

As alterações específicas de N1, L-05, deduplicação e numeração dos vínculos continuam nos ciclos próprios já identificados.

---

# 16. DECISÃO SOBRE D1

Minha posição como Comentador é:

> **D1 deve ser resolvida pelo modelo de dois eixos: `status_auditoria` representa o estado de confirmação; `direcao_suporte` representa a relação evidencial. `aprovado_com_ressalva` não implica `condicional`.**

Portanto, entre as opções apresentadas na Rodada 78:

* **(a) não deve ser adotada como regra universal**;
* **(b) é conceitualmente a direção correta**, mas deve ser refinada para não transformar toda ressalva em um dos três destinos de forma mecânica;
* proponho uma **(c) formulação integrada**, com classificação semântica da ressalva no Claim Kit e materialização determinística no N2.

---

# 17. PROPOSTA PARA O ENCERRAMENTO DA RODADA 4

A questão que deve retornar aos dois territórios não precisa mais ser:

> “Qual dos dois está certo?”

Deve ser:

> **“Os dois territórios subscrevem que a separação entre estado de validação e direção de suporte resolve D1 sem alterar indevidamente N1/N2?”**

E, especificamente:

### Auditor-Estrutura

Verificar:

* compatibilidade da solução com N2 v1.4;
* possibilidade de manter os `if/then` existentes;
* necessidade ou não de alteração de schema;
* testes mecânicos possíveis.

### Auditor-Mestre

Verificar:

* suficiência epistemológica da classificação;
* se os tipos de ressalva preservam o significado científico;
* se existe algum caso relevante ainda não coberto;
* se a solução impede fabricação de condição.

Se ambos confirmarem, D1 pode ser encerrada sem nova discussão territorial sobre a arquitetura inteira.

---

# 18. ESTADO PROPOSTO APÓS D1

Com a resolução acima, os seguintes pontos podem ser tratados como consolidados:

* arquitetura Claim → Biblioteca → N1/N2;
* Claim ≠ N1 ≠ N2;
* um PMID → um N1 → múltiplos N2;
* `claim_id_origem` como proveniência;
* Biblioteca antes de N2;
* deduplicação por PMID;
* segregação produção × fidelidade;
* classificação científica da ressalva antes da materialização;
* `condicional` somente quando houver condição científica real.

Restam para seus ciclos próprios:

* enum `CLAIM_KIT_CLINICO`;
* política de numeração dos vínculos clínicos;
* portões L-05;
* reconciliação técnica dos PMIDs fora da Bibliografia;
* definição final do contrato de saída do Claim Kit;
* piloto e bytes ainda pendentes do fluxo geral.

---

# CONCLUSÃO

A divergência D1 não exige escolher entre “mapeamento único” e “roteamento universal”.

Ela revela que **o modelo estava tentando representar duas dimensões diferentes com uma única transformação**.

A solução de engenharia é separar essas dimensões:

```text
CLAIM
  │
  ├── status de validação
  │      ├── aprovado
  │      └── aprovado_com_ressalva
  │
  └── ressalva classificada
         │
         ├── condição de aplicação
         ├── heterogeneidade/inconsistência
         └── maturidade/limitação
                     │
                     ▼
                 N2
           ┌─────────┴──────────┐
           ▼                    ▼
   status_auditoria       direcao_suporte
   CONFIRMADO /           sustenta /
   PARCIALMENTE           refuta /
   CONFIRMADO              inconclusivo /
                           condicional
                                  │
                                  ▼
                         condicao somente
                         quando existir
                         condição real
```

**A regra que deve ficar proibida é:**

> `aprovado_com_ressalva → condicional` por simples derivação.

**A regra que deve permanecer é:**

> `condicional` somente quando a ciência realmente afirma uma condição.

Com isso, a materialização deixa de interpretar livremente a ressalva e passa a reproduzir uma decisão científica já registrada no Claim Kit.

Essa, em minha avaliação, é a solução que permite avançar sem sacrificar nem o contrato estrutural do N2 nem a integridade epistemológica do projeto.
