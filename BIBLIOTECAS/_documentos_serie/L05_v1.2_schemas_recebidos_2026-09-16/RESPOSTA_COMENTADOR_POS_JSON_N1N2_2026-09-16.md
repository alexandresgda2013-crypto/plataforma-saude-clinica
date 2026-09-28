Deixo explicar ,o chatgpt não tinha visto os dois jsons da resposta do auditor estrutura, depois que ele viu , ele emitiu uma nova resposta.

```
# RESPOSTA AO AUDITOR DE ESTRUTURA

## L-05 v1.2 — Schemas N1 e N2

**Origem:** Comentador Externo
**Destinatário:** Auditor de Estrutura
**Data:** 16/09/2026
**Status:** Parecer técnico externo — não normativo

Após análise conjunta dos dois schemas apresentados:

* `L05/schema_referencia_v1.2.json` — Nível 1;
* `L05/schema_vinculo_v1.2.json` — Nível 2;

considero que a proposta v1.2 apresenta **coerência arquitetural suficiente para seguir para a etapa de fechamento das decisões pendentes**, sem necessidade de nova reengenharia estrutural.

## 1. Decisão geral

A arquitetura N1/N2 está tecnicamente consistente.

A separação entre:

* referência bibliográfica;
* natureza da evidência;
* desenho do estudo;
* procedência;
* estado de validação da referência;
* vínculo com a afirmação;
* entidade ancorada;
* papel temático;
* direção do suporte;
* natureza da relação;
* força causal;

está adequada.

Não identifico, nos dois schemas, uma incompatibilidade estrutural que justifique retornar à concepção anterior.

**Conclusão: seguir para fechamento, não para reestruturação.**

---

## 2. N1 — `schema_referencia_v1.2.json`

### 2.1 `natureza_evidencia` × `desenho_estudo`

A separação está aprovada.

A regra:

> natureza = QUEM/O QUE foi estudado
> desenho = COMO foi estudado

deve permanecer como princípio normativo.

Também está correta a guarda que impede migração automática para `humana_observacional` quando o `desenho_estudo_bruto` contém marcadores intervencionais.

A regra deve permanecer conservadora:

**quando o dado de origem não garante a classificação, não preencher automaticamente.**

---

### 2.2 `status_validacao` × `status_auditoria`

A distinção entre os níveis está adequada:

* N1 → `status_validacao`: estado do processo de validação da ficha;
* N2 → `status_auditoria`: estado do vínculo/veredito da relação.

Não considero necessário uniformizar os nomes apenas por uniformidade nominal.

A separação semântica é justificável.

Entretanto, a migração do N1 precisa ser explicitada:

atualmente `status_auditoria` permanece no `required`, enquanto `status_validacao` é o campo novo.

Portanto, a v1.2 deve declarar formalmente se está em **regime transitório** e qual será a condição objetiva para:

```text
status_validacao → obrigatório
status_auditoria → aposentado
```

O gate de identidade em 100% dos registros deve permanecer como critério de aposentadoria.

---

### 2.3 `pmid_oficial`

A intenção declarada é correta:

`pmid_oficial` vazio somente quando:

```text
natureza_evidencia = nao_aplicavel
```

Porém, atualmente essa restrição está apenas na descrição e não é integralmente expressa pelo schema.

É necessário escolher e declarar uma das duas opções:

1. a regra pertence ao JSON Schema; ou
2. a regra pertence ao portão L-05.

Não é necessário aumentar a complexidade do schema se a decisão for manter essa validação no portão, mas isso deve ficar explícito.

---

### 2.4 Medições atuais dentro das descrições

Trechos como:

> "Medido hoje: 0/66 mordem..."

devem ser tratados como **estado da execução/migração**, e não como regra normativa permanente.

A regra deve permanecer.

A medição atual deve permanecer no relatório/gate de migração.

Isso evita que números de uma rodada específica sejam confundidos com invariantes do schema.

---

### 2.5 `origem_pipeline` × `origem_detalhe`

A separação está aprovada.

`origem_pipeline` deve permanecer categórico.

`origem_detalhe` deve receber data, lote e observações.

Não recomendo retornar ao campo composto anterior.

---

### 2.6 `citacao_confirmada`

A solução adotada está adequada.

O campo pode permanecer como `deprecated` durante a transição, mas não deve ser utilizado como via de portão ou como prova de verificação.

A distinção entre:

```text
default de geração
```

e

```text
estado de verificação
```

deve permanecer.

---

# 3. N2 — `schema_vinculo_v1.2.json`

## 3.1 Multi-âncora

A solução está aprovada.

A combinação:

```text
ancora_principal
+
ancoras[]
```

é tecnicamente mais adequada que um booleano `principal` em cada âncora.

A regra V-17 deve permanecer no portão:

1. `ancora_principal` não vazio;
2. pertence a `ancoras[*].id_oficial`;
3. não há `id_oficial` duplicado em `ancoras`.

---

## 3.2 `papel` × `direcao_suporte`

A separação está aprovada e deve ser preservada.

`papel` representa relação temática.

`direcao_suporte` representa direção epistemológica.

O Motor e os consumidores não podem inferir eficácia, causalidade ou direção apenas a partir de `papel`.

A regra deve permanecer explícita.

---

## 3.3 `condicional` → `condicao`

A implementação está correta.

Quando:

```text
direcao_suporte = condicional
```

`condicao` deve existir e ser não vazia.

A solução atual é suficiente.

---

## 3.4 `trilha` × `uso`

A estrutura está adequada:

```text
trilha = clinica | mecanistica
```

com `uso` restrito condicionalmente à trilha.

Entretanto, esta continua sendo a **Decisão D-L05-1** e não deve ser considerada encerrada apenas porque o mecanismo foi implementado no schema.

A decisão normativa precisa ser registrada antes do congelamento.

Também recomendo ajustar a descrição de `uso` para evitar a formulação "3 primeiros + 3 últimos", já que `gap_pesquisa` é compartilhado pelas duas trilhas.

---

## 3.5 `forca_biologica_conexao`

A descrição estabelece obrigatoriedade para âncora principal em `BLOCO_07` ou `BLOCO_08`, mas o JSON Schema não implementa essa obrigatoriedade.

Isso não é necessariamente um problema.

A decisão necessária é apenas declarar se a regra é:

```text
Schema
```

ou:

```text
Portão L-05
```

Minha recomendação é manter essa regra no **portão**, evitando tornar o Draft-07 excessivamente dependente de relações entre objetos internos de `ancoras`.

Nesse caso, a descrição deve dizer explicitamente que a obrigatoriedade é aplicada pelo portão.

---

# 4. Compatibilidade N1 ↔ N2

A análise conjunta dos dois schemas mostra compatibilidade estrutural.

O fluxo está corretamente separado:

```text
N1
REFERÊNCIA
   │
   │ id_referencia_interna
   ▼
N2
VÍNCULO
   │
   ├── claim_id
   ├── trecho_ancora
   ├── âncoras
   ├── papel
   ├── direção_suporte
   ├── natureza_relacao
   ├── força_causal
   └── estados de validação
```

Não identifico necessidade de criar um terceiro nível apenas para resolver essas relações.

---

# 5. Pendências que considero necessárias antes do congelamento

Solicito que o fechamento normativo trate objetivamente destes pontos:

### D1

Formalizar a transição:

```text
N1:
status_auditoria
→ status_validacao
```

incluindo condição de aposentadoria do alias.

### D2

Definir se:

```text
pmid_oficial vazio
```

é validado pelo schema ou pelo portão.

### D3

Retirar das descrições normativas as medições específicas da rodada atual, mantendo-as no relatório de execução/migração.

### D4

Definir explicitamente quais regras são:

```text
JSON Schema
```

e quais são:

```text
Gate/Portão L-05
```

especialmente as invariantes que dependem de mais de um objeto.

### D5

Registrar a decisão final de:

```text
trilha × uso
```

antes do congelamento.

### D6

Registrar a regra de obrigatoriedade de:

```text
forca_biologica_conexao
```

para BLOCO_07/BLOCO_08.

---

# 6. Critério de fechamento

Depois dessas decisões, considero adequado executar novamente o derivador contra o acervo real.

O fechamento deve demonstrar:

```text
Schema
   ↓
Derivador
   ↓
Acervo real
   ↓
Gate
   ↓
Medição
   ↓
Correções
   ↓
Nova execução
   ↓
Convergência
```

Somente depois dessa execução final a proposta deve ser elevada de:

```text
PROPOSTA v1.2 — não normativa
```

para o estado normativo correspondente.

---

# 7. Parecer final

**Parecer favorável ao fechamento estrutural da proposta L-05 v1.2.**

Não recomendo nova reengenharia dos schemas N1 e N2.

As pendências identificadas são predominantemente de:

* decisão normativa;
* regra de migração;
* delimitação Schema × Gate;
* validação contra o acervo real.

A arquitetura central deve ser preservada.

Em especial, considero consolidadas as seguintes decisões estruturais:

```text
natureza_evidencia ≠ desenho_estudo

status_validacao N1 ≠ status_auditoria N2

papel ≠ direcao_suporte

ancora_principal ≠ precedência epistemológica

verification_status ≠ força da evidência

proveniência ≠ força causal

schema ≠ portão

referência N1 ≠ vínculo N2
```

A partir daqui, o trabalho deve ser de **fechamento, migração, execução e verificação**, e não de retorno à concepção estrutural.

**Este parecer é externo e não incorpora automaticamente qualquer alteração ao contrato L-05. A autoridade de fechamento permanece com o fluxo formal do projeto e com a verificação da Casa.**
```
