# CARTA DO COMENTADOR À ARENA CASA

## Proposta de solução de engenharia após a Rodada 3

**Data:** 2026-09-23
**Origem:** Comentador
**Destinatário:** Arena Casa
**Objeto:** integração dos Claims Clínicos aprovados com a infraestrutura existente de N1/N2 das Bibliotecas Canônicas

---

## 1. MUDANÇA DE FOCO APÓS A RODADA 3

Após a leitura dos pareceres do Auditor-Mestre e do Auditor-Estrutura, do CONFRONTO_PARECERES_RODADA3 e da TRILHA87, inicialmente parecia necessário definir quem produziria os N1/N2 derivados dos claims clínicos.

A análise adicional do fluxo real do operador mostrou que essa formulação precisa ser corrigida.

O operador **já possui um processo funcional de produção e aprovação de Claims Clínicos**, utilizando três IAs, análise dos artigos, auditoria e Bloco de Estado.

Portanto:

> **A questão em aberto não é quem produziria os Claims Clínicos.**

Essa etapa já existe e já está sendo executada.

A questão que ficou pendente desde a apresentação inicial dos Claims Clínicos ao Auditor-Mestre é outra:

> **Como padronizar a saída de um Claim Clínico aprovado para que ela utilize a infraestrutura de evidências já existente nas Bibliotecas Canônicas, especialmente N1 e N2/Vínculos, sem criar um segundo sistema paralelo?**

É esta interface que proponho que a Arena analise nesta rodada.

---

# 2. DISTINÇÃO ENTRE OS DOIS ACERVOS

A análise dos exemplos fornecidos pelo operador mostrou a coexistência de dois objetos distintos.

### 2.1 Claim Clínico

Exemplo:

`B1.SM02.001`

Com:

* `claim_id`
* `status`
* `statement`
* `nota_ressalva`
* `fontes`
* PMID
* comparador
* achado
* moderadores
* `usado_em_biblioteca`

Esse objeto registra **o resultado do processo de validação clínica**.

Ele não é N1 nem N2.

---

### 2.2 Vínculos já existentes na Biblioteca Canônica

Exemplo:

`VINC_B1_0001`

Com:

* `id_vinculo`
* `id_referencia_interna`
* `claim_id`
* `trecho_ancora`
* relação/achado
* natureza da relação
* força
* extrapolação
* `evid_role`
* `status_auditoria`
* `direcao_suporte` e demais campos conforme o contrato N2.

Esses vínculos já fazem parte da infraestrutura da Biblioteca Canônica mecanística.

Pelo modelo vigente e pelo parecer do Auditor-Estrutura:

> **o Vínculo é o N2.**

Não há razão para criar um segundo objeto estrutural concorrente ao N2.

---

# 3. N1 TAMBÉM JÁ EXISTE

Os arquivos da pasta:

`Evidencias/Bibliografia`

já possuem a estrutura correspondente ao N1, com campos como:

`pmid_oficial`, `titulo_artigo`, `autores`, `revista_ano`, `desenho_estudo`, `ids_referencia_interna`, `evid_role`, `origem_pipeline`, `claim_id_origem` etc.

Portanto:

> **N1 = registro bibliográfico da referência.**

E:

> **N2 = Vínculo entre a referência e aquilo que ela sustenta.**

A arquitetura existente já possui essas duas camadas.

---

# 4. A HIPÓTESE DE ENGENHARIA QUE DEVE SER ANALISADA

A proposta é que o Claim Clínico aprovado **não crie uma nova estrutura de evidências**.

Em vez disso:

```text
ARTIGOS
   ↓
3 IAs independentes
   ↓
CLAIM CLÍNICO APROVADO
   ↓
BLOCO DE ESTADO
   ↓
materialização padronizada
   ├──────────────► Biblioteca Canônica
   │
   └──────────────► N1 + N2/Vínculo
```

O N1 já existente deve ser reutilizado quando o PMID já estiver registrado.

Somente quando o artigo não existir na Bibliografia deverá ser criado um novo N1.

O vínculo produzido para o Claim Clínico será outro **N2/Vínculo**, utilizando o mesmo contrato estrutural.

---

# 5. MESMO PMID, MAIS DE UM VÍNCULO

Essa questão parece ser uma das razões pelas quais a separação dos objetos é importante.

Um mesmo artigo pode participar simultaneamente de relações diferentes.

Exemplo conceitual:

```text
PMID 36893912
      │
      ├── N2/Vínculo mecanístico já existente
      │
      └── N2/Vínculo associado ao claim clínico
```

Portanto:

> **não se deve criar um segundo N1 para o mesmo PMID apenas porque ele foi utilizado por um novo Claim Clínico.**

O N1 permanece bibliográfico e único.

A multiplicidade de uso deve ocorrer nos vínculos/N2.

Isso torna especialmente relevante a regra já apontada pelo Auditor-Estrutura sobre deduplicação por `pmid_oficial`.

---

# 6. O QUE OS CLAIMS CLÍNICOS ACRESCENTAM

A decisão anterior do Auditor-Mestre é importante para esta solução.

Quando os Claims Clínicos auditados foram apresentados, verificou-se que eles **resolviam quatro questões que os vínculos existentes da Biblioteca não haviam resolvido adequadamente**.

Por isso, os Claims Clínicos não devem ser aposentados.

A arquitetura correta não é:

> Claim Clínico OU Vínculo da Biblioteca.

É:

> **Claim Clínico → processo de validação clínica**
> **N1/N2 → materialização e rastreabilidade da evidência**

São camadas diferentes e complementares.

---

# 7. O BLOCO DE ESTADO COMO ARTEFATO DE ENTRADA

O Bloco de Estado apresentado pelo operador já contém grande parte da informação necessária para a transição:

```text
claim_id
status
statement
nota_ressalva
fontes
pmid
comparador
achado
moderadores
usado_em_biblioteca
```

Portanto, não parece necessário criar outro processo para “refazer” o claim depois de aprovado.

A questão de engenharia é determinar quais campos:

1. já existem no Bloco de Estado;
2. podem ser derivados automaticamente;
3. precisam ser acrescentados;
4. pertencem à Biblioteca;
5. pertencem exclusivamente ao N2;
6. não devem ser copiados para o N1.

---

# 8. CAMPOS QUE PARECEM SER O PONTO DE INTERFACE

Pelos pareceres da Rodada 3, quatro estruturas chamaram atenção:

* `trecho_ancora`
* `ancora_principal`
* `ancoras[]`
* `condicao`

Esses campos não estão presentes no exemplo atual do Bloco de Estado.

Entretanto, não proponho ainda que eles sejam simplesmente adicionados.

A Arena deve primeiro comparar os três contratos reais:

> **Bloco de Estado × N1 v1.3 × N2 v1.4**

e determinar o **mínimo conjunto de dados necessário** para que a materialização seja determinística.

Isso evita acrescentar campos por antecipação.

---

# 9. RESSALVA

O Claim Clínico já possui:

`status: aprovado_com_ressalva`

e:

`nota_ressalva`

O N2 já possui estrutura compatível com:

`status_auditoria = PARCIALMENTE_CONFIRMADO`

e:

`direcao_suporte = condicional`

com:

`condicao`

obrigatória quando condicional.

Portanto, a proposta é manter o princípio já demonstrado pelo Auditor-Estrutura:

```text
aprovado_com_ressalva
        ↓
PARCIALMENTE_CONFIRMADO
        ↓
direcao_suporte = condicional
        ↓
condicao
```

A Arena deverá verificar apenas **como essa transformação deve ser formalizada no contrato Claim Kit → N2**, sem criar uma segunda semântica.

---

# 10. `claim_id_origem` NÃO DEVE SER USADO COMO LISTA DE TODOS OS CLAIMS

Há outro ponto que merece confirmação arquitetural.

No N1 aparece:

`claim_id_origem`

Mas um único artigo pode participar de vários Claims Clínicos.

Portanto, a hipótese é:

> `claim_id_origem` deve representar a proveniência/origem do registro N1, e não funcionar como catálogo de todos os claims que utilizam aquele PMID.

A relação de um mesmo N1 com múltiplos claims deve permanecer nos N2/Vínculos através de `claim_id`.

Solicita-se à Arena confirmar esta leitura antes de qualquer alteração.

---

# 11. `origem_pipeline`

O Auditor-Estrutura já identificou que:

`CLAIM_KIT_CLINICO`

não está atualmente no enum de `origem_pipeline` do N1 v1.3.

Isso parece ser uma alteração pequena e coerente de proveniência, mas não proponho incorporá-la unilateralmente.

Solicita-se que a Arena determine, após comparar os contratos:

1. se essa alteração é realmente necessária;
2. se deve entrar no ciclo editorial do N1;
3. e se o valor deve identificar criação do N1 a partir de Claim Kit ou outro conceito de proveniência.

---

# 12. SOBRE A ANTIGA QUESTÃO DOS PMIDs

O operador informa que a Bibliografia/PMIDs já foi produzida durante a construção das Bibliotecas Canônicas e já passou por auditoria do Auditor-Mestre.

Portanto, **não proponho reabrir neste momento toda a auditoria científica dos PMIDs**.

O que parece necessário, antes da primeira materialização de Claims Clínicos, é uma:

### reconciliação técnica de referências

Verificando, minimamente:

* duplicidade de PMID;
* PMID inexistente;
* correspondência PMID ↔ `id_referencia_interna`;
* consistência da referência;
* colisões entre referências já existentes e novas referências;
* proveniência.

Essa reconciliação deve ser tratada como controle de materialização, não como nova auditoria científica da Bibliografia inteira, salvo quando for encontrado um erro que justifique reabertura.

---

# 13. SOLUÇÃO PROPOSTA PARA O FLUXO

A arquitetura integrada proposta é:

```text
                  ARTIGOS
                     │
                     ▼
          ┌────────────────────┐
          │ 3 IAs independentes│
          └─────────┬──────────┘
                    ▼
             CLAIM APROVADO
                    │
                    ▼
             BLOCO DE ESTADO
                    │
                    ▼
          ┌─────────────────────┐
          │ Materialização      │
          │ padronizada         │
          └───────┬───────┬─────┘
                  │       │
                  ▼       ▼
             Biblioteca   N1
                  │        │
                  └────┬───┘
                       ▼
                    N2/Vínculo
                       │
              ┌────────┴─────────┐
              ▼                  ▼
     auditoria mecânica    fidelidade científica
              │                  │
              └────────┬─────────┘
                       ▼
                     RÉPLICA
                       │
                       ▼
                    OPERADOR
```

Esse desenho não cria uma nova Biblioteca, um novo N1 ou um novo sistema de vínculos.

Ele apenas define a interface entre os artefatos.

---

# 14. O QUE ESTÁ SENDO SOLICITADO À ARENA

Solicito à Arena Casa que, com base nos **três modelos que acompanharão esta carta**:

1. Bloco de Estado dos Claims Clínicos;
2. JSON dos Vínculos/N2 da Biblioteca Canônica;
3. JSON dos PMIDs/N1 da pasta `Evidencias/Bibliografia`;

realize uma comparação estrutural campo a campo e determine:

### A. Claim → N1

Quais dados do Claim aprovado alimentam ou referenciam o N1.

### B. Claim → N2

Quais dados alimentam o Vínculo/N2.

### C. Campos derivados

Quais campos podem ser obtidos automaticamente sem nova decisão científica.

### D. Campos ausentes

Quais informações realmente precisam ser acrescentados ao Claim Kit.

### E. Reutilização

Como identificar um N1 já existente e impedir duplicação por PMID.

### F. Proveniência

Como registrar que a referência veio do Claim Kit Clínico sem confundir proveniência com uso.

### G. Ressalvas

Como transportar `nota_ressalva` para a estrutura N2 já existente.

### H. Biblioteca

Como o Claim Clínico aprovado passa a possuir uma afirmação correspondente na Biblioteca Canônica, permitindo que `trecho_ancora` seja efetivamente ancorado.

### I. Auditoria

Quais verificações devem permanecer com o Auditor-Estrutura e quais pertencem à verificação científica adversarial.

---

# 15. PEDIDO DE CLASSIFICAÇÃO DA ARENA

A Arena não precisa ainda decidir o desenho final de cada campo.

O que solicito primeiro é uma classificação:

| Elemento | Já existe | Derivável | Falta no Claim Kit | Pertence ao N1 | Pertence ao N2 | Decisão necessária |
| -------- | --------- | --------- | ------------------ | -------------- | -------------- | ------------------ |

Essa matriz permitirá descobrir se a solução exige:

* apenas padronização de saída;
* pequena extensão do Claim Kit;
* alteração pontual de schema;
* ou alguma alteração arquitetural adicional.

A preferência de engenharia deve ser a menor alteração suficiente.

---

# 16. PRÓXIMO RITO

Depois que a Arena organizar essa comparação e formular a proposta de interface, o pacote deverá seguir novamente aos:

**Auditor-Mestre**
e
**Auditor-Estrutura**

para avaliação da proposta concreta.

A pergunta aos dois auditores deverá ser diferente da rodada anterior:

> **“A solução de interface Claim Clínico → Biblioteca → N1/N2 é compatível com os contratos e princípios que cada território protege? Existe algum impedimento técnico ou epistemológico?”**

Não se pede aos auditores que recriem os Claims Clínicos.

Não se pede aos auditores que refaçam a Bibliografia.

Não se pede aos auditores que inventem outro modelo de vínculo.

Pede-se apenas que verifiquem a solução de integração.

---

# 17. CONCLUSÃO DO COMENTADOR

Após esta análise, considero que o problema original pode ser reduzido à seguinte formulação:

> **Os Claims Clínicos já estão sendo produzidos e auditados. A Biblioteca Canônica já possui N1/Bibliografia e N2/Vínculos. O trabalho restante é estabelecer um contrato de materialização que permita que um Claim Clínico aprovado utilize essa infraestrutura existente sem duplicar referências, sem perder ressalvas e sem confundir o processo de validação com o conhecimento canônico.**

Essa solução preserva:

* os Claims Clínicos já produzidos;
* a Biblioteca Canônica como fonte de conhecimento;
* N1 como registro bibliográfico;
* N2/Vínculo como relação;
* a rastreabilidade;
* a deduplicação por PMID;
* a separação entre validação e evidência;
* e a segregação entre produção e auditoria.

O objetivo da próxima rodada, portanto, não deve ser decidir novamente **se os Claims Clínicos devem existir**.

Essa questão já foi suficientemente esclarecida.

O objetivo deve ser definir, com precisão de engenharia:

> **como o Claim Clínico aprovado entra no sistema existente.**
