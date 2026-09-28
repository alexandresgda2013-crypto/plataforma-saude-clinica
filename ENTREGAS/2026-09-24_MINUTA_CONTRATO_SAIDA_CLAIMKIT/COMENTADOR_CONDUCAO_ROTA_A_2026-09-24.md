# CONDUÇÃO DO COMENTADOR — ROTA A

## Fechamento de D1 e incorporação de R-1/R-2 ao contrato do Claim Kit

**Data:** 2026-09-24
**Origem:** Comentador
**Destinatário:** Arena Casa
**Objeto:** Rodada 4 — D1, R-1, R-2 e preparação da próxima rodada

---

# 1. DECISÃO DE CONDUÇÃO

Após confrontar os pareceres da Rodada 4, considero que a **Rota A** é o caminho correto:

> integrar R-1 e R-2 à solução do Comentador, produzir uma minuta final do contrato de saída do Claim Kit e devolvê-la aos dois territórios para uma última subscrição.

Não recomendo fechar D1 apenas conceitualmente e empurrar R-1/R-2 para outro ciclo.

A razão é objetiva:

**R-1 e R-2 não são detalhes posteriores. Eles determinam se o materializador poderá produzir N2 sem interpretar ciência por conta própria.**

Portanto, a solução deve chegar à primeira materialização já com essas regras fechadas.

---

# 2. O QUE ESTÁ DEFINITIVAMENTE RESOLVIDO

Os dois auditores subscrevem, sem divergência, o modelo central:

> **estado de validação e direção de suporte são eixos diferentes.**

Assim:

```text
status_auditoria
        ≠
direcao_suporte
```

O erro anterior estava em derivar um do outro:

```text
aprovado_com_ressalva
→ condicional
```

Essa regra está abolida.

A regra correta é:

```text
aprovado_com_ressalva
→ PARCIALMENTE_CONFIRMADO
```

e, separadamente:

```text
relação científica
→ direcao_suporte
```

e, somente quando houver condição científica real:

```text
condição científica
→ condicional + condicao
```

D1, portanto, está resolvido em seu núcleo.

---

# 3. R-1 — DIREÇÃO POR FONTE

Este é o primeiro ponto que precisa entrar definitivamente no contrato de saída.

O Claim Kit atual não informa:

* `sustenta`;
* `refuta`;
* `inconclusivo`.

O materializador não pode inferir esses valores a partir do `statement`, `achado`, `comparador` ou `status`.

Isso seria simplesmente deslocar o problema de D1 para outro campo.

## Regra

A direção deve ser decidida **no fechamento científico do Claim**, antes da materialização.

O vocabulário a utilizar é o já existente no Schema-Claim v3.1:

```text
sentido_do_achado:
  suporta_relacao
  refuta_relacao
  inconclusivo
```

Não criar um segundo vocabulário.

O materializador apenas faz:

```text
suporta_relacao → sustenta
refuta_relacao  → refuta
inconclusivo    → inconclusivo
```

---

# 4. ONDE A DIREÇÃO DEVE SER REGISTRADA

A direção precisa ser **por fonte/relação**, e não apenas uma vez no claim.

Isso é necessário porque um único claim pode conter:

* duas fontes convergentes;
* duas fontes conflitantes;
* uma fonte que sustenta;
* outra que é inconclusiva;
* ou fontes com direções diferentes em condições distintas.

Portanto, a decisão científica deve acompanhar a relação entre:

```text
fonte → afirmação
```

e não somente:

```text
claim → status
```

Essa regra impede que o materializador tenha de escolher uma direção por conta própria.

---

# 5. O MATERIALIZADOR NÃO PODE TER DEFAULT

Fica expressamente proibido:

```text
claim aprovado
→ sustenta
```

ou:

```text
fonte principal
→ sustenta
```

como regra automática.

Também fica proibido inferir:

```text
achado positivo
→ sustenta
```

porque o sentido do achado depende da afirmação concreta e da relação científica que está sendo registrada.

A ausência de `sentido_do_achado` no Claim fechado deve produzir:

> **falha de materialização / claim ainda não fechado.**

Não deve produzir preenchimento automático.

---

# 6. R-2 — MODERADORES

Os `moderadores[]` já existem no Claim Kit v1.2 e não devem ser descartados.

Eles carregam informação operacional relevante:

```text
variavel
efeito
regra_motor
fonte_pmid
```

Com efeitos:

```text
atenua
amplifica
inverte
nulo
```

A solução precisa, entretanto, impedir que `moderadores[]` se transforme automaticamente em uma segunda fonte concorrente para `condicao`.

---

# 7. REGRA DE FONTE ÚNICA PARA CONDIÇÃO

A partir desta rodada, a `condicao` do N2 deve possuir **uma única origem semântica canônica**:

> **uma relação científica explicitamente declarada no fechamento do Claim.**

A `nota_ressalva` explica a ressalva.

O `moderador` descreve a modificação relevante para o claim/motor.

Nenhum dos dois, isoladamente, autoriza o materializador a inventar uma `condicao`.

Quando uma relação realmente for condicional, a condição deve estar explicitamente decidida no fechamento científico.

Assim desaparece a possibilidade:

```text
ressalvas[] → condição
```

e, ao mesmo tempo:

```text
moderadores[] → outra condição
```

produzindo duas fontes concorrentes.

---

# 8. COMO TRATAR `ATENUA` E `AMPLIFICA`

`atenua` e `amplifica` não devem ser automaticamente transformados em:

```text
direcao_suporte = condicional
```

porque eles representam **modificação de magnitude**, não necessariamente condição lógica de aplicação.

Portanto:

```text
atenua/amplifica
→ permanecem no Claim/moderador
→ continuam disponíveis ao Motor através do claim
```

A informação não desaparece porque o N2 já possui:

```text
claim_id
```

que permite retornar ao Claim completo.

Não é necessário copiar toda a regra operacional do moderador para o N2.

---

# 9. COMO TRATAR `INVERTE`

`inverte` é diferente.

Quando o moderador realmente significa que a relação muda de direção conforme a condição, um único N2 condicional é insuficiente.

O caso:

`B1.SM02.001b`

é o exemplo concreto.

A regra do Claim:

```text
classe_antidepressivo
```

produz efeitos de direção diferentes.

Não devemos comprimir isso em:

```text
um N2
+
uma condição genérica
```

porque uma das metades da relação seria perdida.

## Regra de materialização

Quando `inverter` significar efetiva mudança de direção:

```text
condição A → sustenta
condição B → refuta
```

e devem ser produzidas **duas relações N2 complementares**, cada uma com sua própria condição explicitamente decidida no Claim.

Conceitualmente:

```text
mesma evidência / mesmo claim
        │
        ├── condição A → sustenta
        │
        └── condição B → refuta
```

Isso não significa dois N1.

O N1 continua único para o PMID.

A multiplicidade ocorre no N2.

---

# 10. COMO O CLAIM DEVE REPRESENTAR ESSAS RAMIFICAÇÕES

Não recomendo acrescentar uma nova estrutura livre em cada etapa do pipeline.

A regra de engenharia deve ser reutilizar a semântica já existente na trilha mecanística:

```text
sentido_do_achado
```

e, quando houver relações condicionais distintas, registrar explicitamente os respectivos ramos no fechamento científico.

A forma JSON exata dessa estrutura deve ser definida no contrato do Claim Kit após a comparação com o Schema-Claim v3.1.

O princípio é o que deve ser congelado agora:

> **cada relação que chega ao N2 precisa chegar ao materializador já semanticamente decidida.**

---

# 11. `RESSALVAS[]`

A proposta de `ressalvas[]` continua válida como estrutura de classificação científica da ressalva, mas sua função deve ser claramente delimitada.

Ela serve para registrar:

```text
tipo
nota
```

e, quando necessário, o vínculo com a relação científica correspondente.

Tipos mínimos já demonstrados pela rodada:

```text
condicao_aplicacao
heterogeneidade
maturidade_evidencia
```

Mas:

> **`ressalvas[]` não é uma segunda fonte independente de direção ou condição.**

Isso evita a reabertura de R-2b.

---

# 12. MATURIDADE

Os dois auditores confirmaram que `grau_maturidade` já existe no N2 v1.4.

Portanto:

```text
ressalva de maturidade
→ decisão científica no Claim
→ grau_maturidade no N2
```

Não:

```text
maturidade
→ condicional
```

Novamente, são eixos diferentes.

O vocabulário correspondente existente na trilha irmã deve ser reutilizado, evitando nova semântica.

---

# 13. NOVA DEFINIÇÃO DO CONTRATO DE SAÍDA

O Claim aprovado passa a entregar ao materializador quatro decisões científicas distintas:

### 1. Estado

```text
aprovado
aprovado_com_ressalva
```

### 2. Direção por fonte/relação

```text
suporta_relacao
refuta_relacao
inconclusivo
```

### 3. Tipo da ressalva

```text
condicao_aplicacao
heterogeneidade
maturidade_evidencia
```

### 4. Modificações estruturadas

```text
atenua
amplifica
inverte
nulo
```

O materializador **não decide nenhum desses quatro itens**.

Ele apenas transforma uma decisão já existente na estrutura N1/N2.

---

# 14. O RITO DAS TRÊS IAS É MANTIDO

A análise da Arena está correta:

> as rodadas não enfraqueceram o rito; elas deslocaram mais decisões científicas para dentro dele.

Portanto, o rito permanece:

```text
mesmo corpus
   ↓
IA1     IA2     IA3
 │       │       │
 └───────┼───────┘
         ↓
comparação posterior
         ↓
confirma / altera / mantém
         ↓
claim fechado
         ↓
materialização mecânica
```

O fechamento do Claim agora precisa conter, além da conclusão:

* tipo da ressalva;
* direção por fonte;
* modificações relevantes;
* relações condicionais quando existirem.

Isso não aumenta artificialmente o papel das três IAs.

É justamente o oposto:

> **retira interpretação do materializador e coloca a decisão científica no lugar correto.**

---

# 15. O PILOTO `.014`

Concordo com a Arena: o piloto deve ser realizado **com o rito já corrigido**, e não com o v1.9 antigo.

O piloto deve testar o processo real:

```text
análises cegas
→ comparação
→ fechamento
→ classificação da ressalva
→ direção por fonte
→ tratamento de moderadores
→ materialização
→ auditoria
```

O piloto não deve ser usado para “descobrir” a arquitetura depois que o processo começar.

O desenho deve estar congelado antes.

---

# 16. PORTÕES DA PRIMEIRA MATERIALIZAÇÃO

Antes do primeiro lote clínico, ficam necessários os seguintes portões:

### Portão científico

O Claim fechado possui:

* direção por fonte;
* ressalva classificada;
* relações condicionais explicitamente decididas, quando existirem;
* tratamento dos moderadores relevantes.

### Portão de Biblioteca

A afirmação foi incorporada à Biblioteca.

### Portão N1

PMID existente reutilizado ou N1 novo corretamente produzido.

### Portão N2

`trecho_ancora`, entidades, direção, condição e estado corretamente materializados.

### Portão mecânico

Schema, cardinalidade, deduplicação, ancoragem textual e consistência.

### Portão adversarial

Quem produziu a materialização não atesta sua própria fidelidade científica.

---

# 17. O QUE NÃO DEVE SER ALTERADO

R-1/R-2 **não justificam alteração no N1 ou N2 v1.4**.

Também não devem alterar:

* a deduplicação por PMID;
* a ordem Biblioteca → N2;
* `claim_id_origem` como proveniência;
* `claim_id` como ligação de uso;
* a segregação entre produtor e auditor;
* a Biblioteca como fonte de conhecimento.

O problema está no **contrato de saída do Claim Kit**, não no modelo N1/N2.

---

# 18. O QUE DEVE IR PARA A ÚLTIMA SUBSCRIÇÃO

A nova minuta que retorna aos dois territórios deve conter, de forma explícita:

**D1**

* dois eixos independentes;
* `aprovado_com_ressalva` não implica `condicional`.

**R-1**

* direção por fonte/relação;
* vocabulário `sentido_do_achado` já existente;
* nenhuma direção por default;
* ausência de direção = claim não fechado.

**R-2**

* `atenua/amplifica` permanecem como modificadores;
* `inverte` gera relações complementares quando realmente houver inversão de direção;
* uma única origem semântica para cada `condicao`;
* maturidade vai para `grau_maturidade`, não para `condicional`.

---

# 19. CRITÉRIO DE ENCERRAMENTO

A Rodada 4 deve ser considerada encerrada quando:

1. Auditor-Estrutura subscrever a minuta final sem ressalva;
2. Auditor-Mestre subscrever a mesma minuta sem ressalva;
3. a Arena verificar mecanicamente que a minuta corresponde aos pareceres;
4. o operador receber o pacote final e não houver divergência residual.

Depois disso:

> **D1 deixa de ser pendência.**

A primeira materialização clínica somente começa depois que os portões definidos acima estiverem disponíveis.

---

# 20. DECISÃO DO COMENTADOR

**Escolho a Rota A.**

A razão não é simplesmente “fechar mais rápido”.

É porque R-1 e R-2 demonstraram o mesmo princípio que originou D1:

> **o materializador não pode interpretar o significado científico do Claim.**

A direção, a ressalva e os casos de alteração de direção devem estar decididos quando o Claim fecha.

O N1/N2 deve receber decisões já tomadas, não reconstruí-las.

Assim, a arquitetura final permanece:

```text
CIÊNCIA
   ↓
rito das três IAs
   ↓
CLAIM FECHADO
   ├── estado
   ├── direção por fonte
   ├── ressalva classificada
   └── modificadores/relações
   ↓
BIBLIOTECA
   ↓
N1
   ↓
N2
   ↓
auditoria mecânica + adversarial
```

Essa é a solução que preserva simultaneamente a ciência do processo, o contrato estrutural e a filosofia de segregação do projeto.

**Próximo passo:** a Arena deve transformar esta solução em uma **minuta final do contrato de saída do Claim Kit**, confrontá-la uma última vez com os dois auditores e, obtida a dupla subscrição limpa, encerrar D1 e preparar o piloto `.014`.
