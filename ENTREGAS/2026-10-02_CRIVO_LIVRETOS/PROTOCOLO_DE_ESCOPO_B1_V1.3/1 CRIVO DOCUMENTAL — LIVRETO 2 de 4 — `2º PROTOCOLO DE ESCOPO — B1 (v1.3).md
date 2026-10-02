# 📘 CRIVO DOCUMENTAL — LIVRETO 2 de 4 — `2º PROTOCOLO DE ESCOPO — B1 (v1.3).md`

**Atualização do rito:** 02/10/2026
**Objeto:** `2º PROTOCOLO DE ESCOPO — B1 (v1.3).md`
**Aplicação:** crivo documental para o piloto oficial `B1.SM02.014`
**Natureza:** **0 ciência** — não se analisa conteúdo científico.

O rito geral é definido pelo:

> **FLUXO DO CRIVO DOCUMENTAL — versão final — 02/10/2026**

Os prompts executáveis são **documentos separados** e não fazem parte deste Livreto.

---

# 1️⃣ O que este crivo avalia

**Objeto:** declarar (ou não) apto a seguir ao fechamento do crivo, para posterior decisão de vigência pelo operador, o **Protocolo de Escopo — B1 (v1.3)**.

### Régua

> **EXISTENTE ≠ VALIDADO ≠ VIGENTE ≠ AUTORIZADO PARA USO**

### Natureza

Crivo **documental**.

**0 ciência:** não julgar conteúdo científico.

### Regra

Divergência é resolvida **lendo o documento**, nunca por votação.

O documento sob crivo permanece intacto durante o rito.

---

# 2️⃣ Papel do documento

É o **2º item do pacote mínimo obrigatório** do `COMO EXECUTAR v1.11 rev.2` — *“fronteiras do mecanismo em trabalho”*.

O documento define, para o mecanismo **B1 (neuroinflamação)**:

| Bloco                                       | Função documental                            |
| ------------------------------------------- | -------------------------------------------- |
| `scope_in` / `scope_out`                    | delimitação de entrada e saída de B1         |
| `nota_regra_fronteira_B1_B4_B5`             | regra da dupla fronteira do quinolinato      |
| `cross_ref_allowed_shorthand`               | atalhos permitidos                           |
| `cross_ref_ids_oficiais`                    | correspondência dos atalhos aos IDs oficiais |
| `relacoes_cruzadas_semanticas`              | natureza das relações entre mecanismos       |
| `biomarcadores_referenciados`               | presença no catálogo ou em candidatos        |
| `inclusion_criteria` / `exclusion_criteria` | critérios documentais de inclusão e exclusão |

---

# 3️⃣ Identidade, cópias e digitais

Medições registradas em 2026-09-30:

| Peça                          | Caminho                                                                      | Digital (sha256, início) | Observação                        |
| ----------------------------- | ---------------------------------------------------------------------------- | ------------------------ | --------------------------------- |
| **Objeto — kit atual**        | `uploads/Atuais/Documentos/2º PROTOCOLO DE ESCOPO — B1 (v1.3).md`            | `943425cd…`              | 161 linhas · 8.150 bytes · LF     |
| Cópia idêntica                | `BIBLIOTECAS/_documentos_serie/KIT_CLINICA_ATUALIZADO_recebido_2026-09-25/…` | `943425cd…`              | idêntica                          |
| Cópia idêntica — proveniência | `BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/…`            | `943425cd…`              | idêntica · origem do kit de 15/09 |

### Estado

* uma só versão documental identificada;
* três cópias com a mesma digital;
* não há bilhete próprio de vigência;
* a vigência do objeto é matéria deste crivo e da posterior decisão do operador.

---

# 4️⃣ Dependência do Livreto 1

O Livreto 1 (`1º IDS_OFICIAIS`) é dependência documental para as conferências de IDs.

As conferências registradas neste Livreto usam o catálogo **como existe hoje**, digital `3c0eccac…`.

Se o resultado do Livreto 1 alterar o catálogo:

> **refazer a conferência de IDs deste Livreto.**

Não repetir essa conferência sem alteração relevante do catálogo.

---

# 5️⃣ O que a Casa já mediu

Estas conferências são **histórico mecânico** e não substituem o crivo.

| Conferência                                | Resultado                                                                                            |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| IDs oficiais citados no protocolo          | **14 citados · 14 presentes** no `1º IDS_OFICIAIS` · 0 ausentes                                      |
| `cross_ref_ids_oficiais`                   | **10 pares** · todos existem em `mecanismos` do `_ids_oficiais.json`                                 |
| Campos documentais citados no Schema-Claim | `evidence_role`, `uso` e `referencia_cruzada` existem                                                |
| Regra de trilha pré-clínica × Schema       | protocolo exige `preclinical_mechanistic`; o Schema vincula esse valor a `uso: contexto_mecanistico` |
| NLR e S100B                                | não estão no catálogo; estão em `CANDIDATOS_IDS_OFICIAIS — v1.0.md`, conforme descrito no protocolo  |

---

# 6️⃣ Pontos de verificação

Os pontos abaixo são **fatos a verificar**.

Não são correções prévias.

## V1 — Referência a “Schema-Claim v1.2”

**Onde:** `nota_v1.1` do Protocolo.

**Fato medido:** o texto manda verificar:

> “Schema-Claim v1.2, evidence_role”

O Schema-Claim vigente é **v1.3 rev.3** (`e9f9e5d8…`).

No Schema vigente, `evidence_role` está registrado como idêntico ao v1.2.

---

## V2 — Referência a `CANDIDATOS_IDS_OFICIAIS.yaml`

**Onde:** `nota_v1.2` do Protocolo.

**Fato medido:** o arquivo é citado com extensão `.yaml`.

No kit atual, o arquivo é:

`CANDIDATOS_IDS_OFICIAIS — v1.0.md`

Digital:

`a069de5f…`

O `COMO EXECUTAR v1.11 rev.2` vigente também contém referências a `.yaml`.

---

## V3 — Data interna `last_updated: 2026-08-04`

**Fato medido:** o objeto declara:

* `version: 1.3`
* `status: ativo`
* `last_updated: 2026-08-04`

A cópia de proveniência pertence ao kit recebido em 15/09.

O arquivo não contém digital própria nem referência a bilhete próprio de vigência.

---

## V4 — Claim `.011` e regra de fronteira

**Fato medido:** o Protocolo estabelece que, quando aprovado em G3, o `.011` deve incluir `[B4, B5]` em `referencia_cruzada`.

Na Lista Canônica v1.5, o `.011` aparece como:

`aprovado_com_ressalva`

e possui:

* `mecanismo_B4…`
* `mecanismo_B5…`
* `cenario_E99_urgencias_psiquiatricas`

O ID do cenário existe no catálogo.

Este ponto é documental e cruza com o Livreto 3.

---

## V5 — Atalhos permitidos × mapa de IDs

**Fato medido:**

`cross_ref_allowed_shorthand` lista **8 atalhos**:

B2, B3, B5, B6, B7, B9, B10 e B16.

`cross_ref_ids_oficiais` contém **10 pares**:

os 8 anteriores + B4 e B12.

Os dois adicionais possuem comentários de uso relacionados à regra da quinurenina e ao `.007b`.

---

# 7️⃣ Perguntas do crivo

As três IAs, a Casa e os auditores trabalham segundo o Fluxo-mãe.

As cinco perguntas documentais são:

1. **É o documento correto?**
2. **Está na versão correta?**
3. **Possui vigência?**
4. **Foi aprovado pelo rito aplicável?**
5. **Não foi substituído por versão posterior?**

A pergunta de vigência significa verificar a **situação documental da vigência**; não autoriza a IA ou o auditor a declarar vigência.

---

# 8️⃣ Território das três IAs

As três IAs verificam:

* coerência interna documental;
* os 14 IDs citados contra o catálogo;
* coerência documental com Schema-Claim v1.3 rev.3;
* coerência documental com `COMO EXECUTAR v1.11 rev.2`;
* pontos V1–V5;
* demais contradições documentais que encontrarem.

**Não analisam ciência clínica.**

---

# 9️⃣ Território do Auditor-Estrutura

### Pontos

**V1 · V2 · V4 · V5**

### Função

* estrutura;
* schemas;
* compatibilidade;
* materialização;
* coerência técnica.

O auditor trabalha primeiro sobre o documento, sem Folha.

Depois recebe a Folha e confronta com sua análise própria.

Usa o arquivo externo:

> `PROMPT_AUDITOR_ESTRUTURA.txt`

---

# 🔟 Território do Auditor-Mestre

### Ponto

**V3**

Além de V3, verifica as questões de:

* rito;
* governança;
* aderência normativa;
* identidade e cadeia documental;
* situação documental de vigência.

O auditor trabalha primeiro sobre o documento, sem Folha.

Depois recebe a Folha e confronta com sua análise própria.

Usa o arquivo externo:

> `PROMPT_AUDITOR_MESTRE.txt`

---

# 1️⃣1️⃣ Pacote fechado das três IAs

As três IAs recebem **exatamente o mesmo pacote**.

O operador carrega os arquivos e confere as digitais antes do início.

| # | Arquivo                                        | Papel                             | Digital (início) |
| - | ---------------------------------------------- | --------------------------------- | ---------------- |
| 1 | `LIVRETO_02_PROTOCOLO_ESCOPO_B1_2026-09-30.md` | instrução do crivo                | `36ed0fa5…`      |
| 2 | `2º PROTOCOLO DE ESCOPO — B1 (v1.3).md`        | **objeto sob crivo**              | `943425cd…`      |
| 3 | `ROTEIRO DE TRABALHO DA PLATAFORMA.md`         | régua e rito                      | `507eaefa…`      |
| 4 | `4º COMO EXECUTAR — v1.11 rev.2.md`            | documento normativo de referência | `1ea6d354…`      |
| 5 | `3º SCHEMA-CLAIM — v1.3.md`                    | schema vigente                    | `e9f9e5d8…`      |
| 6 | `1º IDS_OFICIAIS.md`                           | catálogo de IDs                   | `3c0eccac…`      |
| 7 | `CANDIDATOS_IDS_OFICIAIS — v1.0.md`            | complemento do catálogo           | `a069de5f…`      |

### Prompt

O operador envia, separadamente:

> `PROMPT_IA_CRIVO_LIVRETO_02.txt`

Esse prompt **não faz parte deste Livreto**.

Nenhuma IA recebe prompts destinados aos auditores ou ao Comentador.

---

# 1️⃣2️⃣ Regras do pacote das três IAs

As três IAs:

* recebem exatamente os mesmos 7 arquivos;
* trabalham em janelas próprias;
* não veem os pareceres das outras;
* não acessam o repositório;
* não acrescentam nem retiram arquivos;
* não alteram o objeto;
* não executam produção.

Se faltar arquivo ou alguma digital não bater:

> **PARAR E AVISAR.**

Não ajustar por tentativa.

Modelos diferentes devem ser usados quando a plataforma permitir.

---

# 1️⃣3️⃣ Pacote inicial do Auditor-Estrutura

Na FASE 1, recebe somente o necessário ao seu território:

| # | Arquivo                                 | Papel                 | Digital     |
| - | --------------------------------------- | --------------------- | ----------- |
| 1 | Livreto 2                               | pontos V1, V2, V4, V5 | `36ed0fa5…` |
| 2 | `2º PROTOCOLO DE ESCOPO — B1 (v1.3).md` | objeto                | `943425cd…` |
| 3 | `3º SCHEMA-CLAIM — v1.3.md`             | schema                | `e9f9e5d8…` |
| 4 | `1º IDS_OFICIAIS.md`                    | catálogo              | `3c0eccac…` |
| 5 | `CANDIDATOS_IDS_OFICIAIS — v1.0.md`     | V2                    | `a069de5f…` |

Quando necessário para uma verificação específica, a Casa pode fornecer somente o material adicional correspondente ao ponto.

O operador envia separadamente:

> `PROMPT_AUDITOR_ESTRUTURA.txt`

A Folha não é entregue na FASE 1.

---

# 1️⃣4️⃣ Pacote inicial do Auditor-Mestre

Na FASE 1, recebe somente o necessário ao seu território:

| # | Arquivo                                 | Papel                          | Digital     |
| - | --------------------------------------- | ------------------------------ | ----------- |
| 1 | Livreto 2                               | ponto V3 e contexto documental | `36ed0fa5…` |
| 2 | `2º PROTOCOLO DE ESCOPO — B1 (v1.3).md` | objeto                         | `943425cd…` |
| 3 | `ROTEIRO DE TRABALHO DA PLATAFORMA.md`  | régua/rito                     | `507eaefa…` |
| 4 | `4º COMO EXECUTAR — v1.11 rev.2.md`     | rito aplicável                 | `1ea6d354…` |
| 5 | `3º SCHEMA-CLAIM — v1.3.md`             | V1 e referência normativa      | `e9f9e5d8…` |
| 6 | `CANDIDATOS_IDS_OFICIAIS — v1.0.md`     | V2                             | `a069de5f…` |

Bilhetes de vigência ou outros materiais entram somente quando necessários para concluir um ponto.

O operador envia separadamente:

> `PROMPT_AUDITOR_MESTRE.txt`

A Folha não é entregue na FASE 1.

---

# 1️⃣5️⃣ Ordem da auditoria

A auditoria segue o Fluxo-mãe.

### FASE 1

**Documento → análise independente**

O auditor não vê a Folha.

### FASE 2

**Folha → confronto com a análise própria → parecer**

A Folha é material de confronto, não veredito.

O auditor não corrige o documento e não declara vigência.

---

# 1️⃣6️⃣ Folha da Casa

Depois dos três pareceres, a Casa monta a Folha.

| Ponto | IA1     | IA2     | IA3     | Território | Gravidade             |
| ----- | ------- | ------- | ------- | ---------- | --------------------- |
| V1    | sim/não | sim/não | sim/não | EST        | BLOQUEIA/RESSALVA/OBS |
| V2    | sim/não | sim/não | sim/não | EST        | BLOQUEIA/RESSALVA/OBS |
| V3    | sim/não | sim/não | sim/não | GOV        | BLOQUEIA/RESSALVA/OBS |
| V4    | sim/não | sim/não | sim/não | EST        | BLOQUEIA/RESSALVA/OBS |
| V5    | sim/não | sim/não | sim/não | EST        | BLOQUEIA/RESSALVA/OBS |

Acima da tabela:

* resultado das três IAs;
* pontos exclusivos;
* divergências;
* eventual ponto novo.

A Casa não vota.

---

# 1️⃣7️⃣ Comentador

O Comentador recebe **somente a Folha**.

Usa:

> `PROMPT_COMENTADOR.txt`

Não recebe nem solicita o documento.

Produz recomendação, não decisão de vigência.

---

# 1️⃣8️⃣ Ponto novo

Se surgir ponto novo durante o crivo:

1. registrar o fato;
2. registrar onde está;
3. atribuir território;
4. se tocar GOVERNANÇA e ESTRUTURA, acionar os dois;
5. incluir somente na rodada necessária.

---

# 1️⃣9️⃣ Ressalvas e novas rodadas

Se houver ressalva:

> **nova rodada somente dos pontos afetados.**

Somente quem precisa revisar o ponto retorna a ele.

Não se refaz o crivo inteiro sem necessidade.

O objeto permanece intacto.

Se o objeto for alterado:

> **nova digital → novo objeto → novo crivo.**

---

# 2️⃣0️⃣ Fechamento

A Casa reúne:

* os três pareceres;
* a Folha;
* a recomendação do Comentador;
* o parecer do Auditor-Estrutura;
* o parecer do Auditor-Mestre.

Faz o fechamento **sem votação**.

A Casa lê o documento quando houver divergência relevante.

O fechamento não declara vigência.

---

# 2️⃣1️⃣ Vigência

Nenhum destes fatos declara o Protocolo vigente:

* estar no `main`;
* existir;
* possuir digital;
* receber parecer favorável;
* receber recomendação favorável;
* receber parecer favorável dos auditores;
* receber fechamento favorável.

A sequência é:

**3 pareceres → Folha → Comentador → auditorias → fechamento da Casa → frase do operador → VIGÊNCIA**

A frase final é ato exclusivo do operador.

---

# 2️⃣2️⃣ Regras permanentes

1. **0 ciência.**
2. Três IAs em janelas próprias e sem ciência entre si.
3. Modelos diferentes quando a plataforma permitir.
4. As três IAs recebem exatamente o mesmo pacote.
5. Prompts são documentos separados.
6. Nenhum agente recebe prompt destinado a outro papel.
7. Digital divergente ou arquivo faltante → parar e avisar.
8. Divergência → leitura do documento, nunca votação.
9. Comentador → somente a Folha.
10. Auditor → documento primeiro, Folha depois.
11. Auditor → somente seu território, salvo nível completo por ordem do operador.
12. Ponto novo → atribuição territorial.
13. Ressalva → somente pontos afetados.
14. Alteração do objeto → nova digital e novo crivo.
15. Documentos históricos → somente por necessidade concreta.
16. Livreto 1 antecede este Livreto.
17. Se o Livreto 1 alterar o catálogo, repetir as conferências de IDs deste documento.
18. O documento sob crivo permanece intacto durante o rito.
19. O auditor emite parecer e não declara vigência.
20. O operador é a única autoridade para declarar vigência.

---

# 2️⃣3️⃣ Pergunta final do crivo

### Para as três IAs

> **O `2º PROTOCOLO DE ESCOPO — B1 (v1.3).md` (`943425cd…`) pode seguir ao fechamento do crivo para decisão de vigência pelo operador?**

Resposta:

`de acordo` · `com ressalva(s)` · `em desacordo`

### Para os auditores

Cada auditor responde em seu território:

`de acordo` · `de acordo com ressalva` · `em desacordo`

Nenhum parecer declara vigência.
