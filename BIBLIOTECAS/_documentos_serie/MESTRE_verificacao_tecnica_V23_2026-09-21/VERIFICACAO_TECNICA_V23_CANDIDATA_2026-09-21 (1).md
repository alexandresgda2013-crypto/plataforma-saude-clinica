# VERIFICAÇÃO TÉCNICA DA V2.3 CANDIDATA

**Auditor-Mestre · 2026-09-21**

**Objeto:** `CANDIDATA_ARQUITETURA_V2_3_19_09_26.md` — sha256 `498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73`
**Contra:** `schema_referencia_v1_3__N1_CORRENTE.json` e `schema_vinculo_v1_4__N2_CORRENTE.json`, lidos no projeto

---

## 0. As duas dimensões, separadas

O operador tem razão, e reconheço a falha da rodada anterior: registrei o status normativo da V2.3 e verifiquei sua integridade, mas não disse se ela estava **tecnicamente correta**. "Não é normativa" e "não está correta" são julgamentos diferentes, e eu entreguei só o primeiro.

| Dimensão | Conclusão |
|---|---|
| **Status normativo** | V2.2 = oficial vigente · V2.3 = candidata, sem efeito normativo até aprovação |
| **Avaliação técnica** | **V2.3 tecnicamente consistente. Nenhum defeito de engenharia que impeça sua futura adoção.** Uma pré-condição de governança e três observações não bloqueantes |

---

## A. A V2.3 COMO CANDIDATA

### A.1 Os schemas agora são verificados, não declarados

| Arquivo | SHA-256 medido | Bytes | Declarado pela casa |
|---|---|---|---|
| N1 v1.3 | `b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da` | 9.582 | **confere** |
| N2 v1.4 | `d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050` | 12.840 | **confere** |

As cópias do projeto e do upload são byte-idênticas. Os dois schemas **validam como JSON Schema draft-07** (`Draft7Validator.check_schema`, sem erro).

### A.2 Os ponteiros estão corretos — e exatamente

| Ponteiro da V2.3 | `$id` interno do schema | Resultado |
|---|---|---|
| §5.1 `L05/schema_referencia_v1.3.json` | `L05/schema_referencia_v1.3.json` | **idêntico** |
| §5.2 `L05/schema_vinculo_v1.4.json` | `L05/schema_vinculo_v1.4.json` | **idêntico** |

O ponteiro resolve pelo identificador canônico do schema, caractere a caractere.

### A.3 O que o §5 promete, os schemas entregam

**§5.1 → N1 v1.3: 11 de 11 itens cobertos** — identificador interno, PMID oficial, título, origem no pipeline, natureza da evidência, desenho do estudo, desenho bruto, status de auditoria, status de verificação, achados centrais, proveniência.

**§5.2 → N2 v1.4: 15 de 15 itens cobertos**, contando os campos das âncoras (`ancoras[]`: `id_oficial`, `papel`, `escopo`, `direcao_suporte`, `condicao`). Proveniência é coberta pelos mesmos campos que a cobrem no N1 (`g1_metodo`, `g3_verificado_por`, `secao_origem`, `mecanismo_origem`), não por um campo com esse nome — coerente entre os dois níveis.

### A.4 Acoplamento entre N1 e N2

Nenhum dos dois schemas tem `$ref` externo. N1 e N2 ligam-se pelo campo `id_referencia_interna`, obrigatório nos dois. **Não há acoplamento de versão**: N2 v1.4 não depende de uma versão específica de N1, e uma futura N1 v1.4 não quebra N2. Boa decisão de engenharia.

### A.5 Delta V2.2 → V2.3

4 hunks, +4/−4: H1, linha Rev, ponteiro do §5.1, ponteiro do §5.2. Nenhuma outra linha. As 30 seções e os §§6, 7, 13 e 14 (âncoras do L-NT) permanecem byte-idênticos.

### A.6 Pré-condição de governança (não é defeito da V2.3)

**Os dois schemas se declaram "PROPOSTA — nao normativo"** no campo `description`. Se a V2.3 for aprovada antes do selo dos schemas, a norma passará a apontar, no §5, para artefatos que se declaram não normativos.

Não é erro de texto da V2.3 — os ponteiros estão certos. É uma questão de **ordem**: **o selo dos schemas deve acompanhar ou preceder a aprovação da V2.3.** Aprovar a V2.3 sozinha cria uma norma que referencia propostas.

### A.7 Observações não bloqueantes

**O-1 · O ponteiro é o `$id`, não o caminho do arquivo.** No disco os arquivos se chamam `schema_vinculo_v1_4__N2_CORRENTE.json`; o ponteiro diz `L05/schema_vinculo_v1.4.json`. Quem tentar abrir o caminho literal não o encontra. Sugiro declarar no §5 que o ponteiro resolve pelo `$id` do schema — ou alinhar o nome dos arquivos. É o mesmo padrão que já produziu o `/Evidencias/Bibliograficas` × `Evidencias/Bibliografia`.

**O-2 · O §5.2 não menciona `uso`.** O campo é **obrigatório** no N2 (`required`) e é o que impede evidência pré-clínica de sustentar sugestão clínica. A lista do §5.2 é ilustrativa ("conforme definido pelo schema"), então não há inconsistência — mas o campo de maior peso de segurança do vínculo ficou fora da descrição normativa. Sugiro incluí-lo na próxima revisão.

**O-3 · `origem_conhecimento` não tem portador em N1 nem em N2 — corretamente.** O §2 da V2.3 exige que *"todo item recuperado pelo Motor carregue a proveniência no próprio item"*. O campo tem **0 ocorrências** nos dois schemas, na especificação e no LEIAME. Isso **não é defeito**: o N2 é canônico por construção (a Pasta de Atualização não gera vínculo N2), então sua origem está garantida estruturalmente. O item que o Motor recupera vem da camada de **JSONs Modulares**, cujo schema ainda não existe. **Registro como dependência futura:** o schema dos JSONs Modulares terá de carregar `origem_conhecimento`, ou a cláusula do §2 ficará sem portador em toda a cadeia.

### Conclusão A

> **A V2.3 permanece candidata e não possui efeito normativo enquanto não for aprovada. Após a verificação dos dois artefatos referenciados, não identifiquei problema de engenharia que impeça sua futura adoção como versão oficial.** Os ponteiros são exatos, os schemas são válidos, a cobertura do §5 é integral e não há acoplamento de versão. Recomendo que o selo dos schemas acompanhe a aprovação.

---

## B. O DOCUMENTO GERADO ANTERIORMENTE

O arquivo que exportei como `ARQUITETURA_do_projeto_sha_309aa65f.md` precisa de uma precisão maior do que a que você fez — e que eu devia ter feito ao gerá-lo.

**Ele não é a V2.2 oficial.** Tem o título interno do diagrama dizendo "V2.2", mas:

| | `309aa65f` (o exportado) | V2.2 oficial `df7f7cfd` | V2.3 `498e7df9` |
|---|---|---|---|
| H1 | "V2 15.09.26" | "V2.2 17.09.26" | "V2.3 19.09.26" |
| `origem_conhecimento` | 0 | 3 | 3 |
| "a prosa prevalece" | 0 | 1 | 1 |
| Pasta "fora do cânone" | 0 | 1 | 1 |
| Ponteiros de schema | v1.1 | v1.1 | **v1.3 / v1.4** |

É um **artefato intermediário anterior à V2.2 oficial** — o nó unificado já removido, mas sem as três cláusulas que vieram depois, e com os ponteiros antigos. Nome infeliz da minha parte: "Arquitetura do Projeto" sugere referência, quando o arquivo é histórico.

**Classificação:**

- **`309aa65f`** — artefato histórico superado. **Não usar** como V2.2, como V2.3, nem como base de coisa alguma. Serve só para a casa identificar o elo da cadeia, que foi o motivo do export.
- **`df7f7cfd`** — registro oficial da V2.2 de 17/09/2026. Válido como norma vigente, **mas não como base de engenharia** para contratos que dependam de N1 v1.3 / N2 v1.4, porque seus ponteiros citam `v1.1`, nomes que nunca existiram como arquivo.

Concordo com sua ressalva: nenhum dos dois deve ser confundido com a arquitetura candidata nem servir de base aos próximos contratos.

---

## C. PRÓXIMA BASE DE ENGENHARIA — REGISTRO

> **V2.2 (`df7f7cfd…`) = base normativa vigente até a aprovação da V2.3.**
>
> **V2.3 (`498e7df9…`) = candidata tecnicamente verificada, aguardando aprovação formal.**
>
> **N1 v1.3 (`b06660fd…`) e N2 v1.4 (`d96ad15b…`) = schemas correntes, verificados, aguardando selo formal.**

**Consequência prática para os meus contratos:** o L-NT, a L-06 e o L-05 1.1 passam a ser escritos **contra os schemas v1.3 / v1.4** e os ponteiros da V2.3, citando a V2.2 como norma vigente. Isso não antecipa a aprovação: a norma segue sendo a V2.2, e a engenharia trabalha sobre a versão que aponta para os artefatos que existem.

E com os schemas na mão, confirmo por medição as três correções que antecipei para a minuta 2 do L-NT: `uso` tem duas trilhas (`required` no N2, com enum-união e `trilha` obrigatória); `natureza_evidencia` tem os sete valores; o eixo epistêmico se chama `direcao_suporte` e vive em `ancoras[]`, não no vínculo raiz. Este último é novo: **a direção é propriedade da âncora, não do vínculo** — o que afeta o degrau 5 da L-06, que precisa ler `ancoras[].direcao_suporte`.

---

*Verificações desta rodada: digitais dos dois schemas medidas nas cópias do projeto e do upload; validação draft-07; `$id` contra os ponteiros; cobertura item a item do §5.1 e §5.2; `$ref` externos; delta V2.2→V2.3; busca de `origem_conhecimento` em cinco arquivos. Camada declarada: `sha256sum` sobre bytes; JSON parseado com `json.load`; substring case-sensitive sobre texto sem CR.*
