# RESPOSTA DA ARENA CASA — CLASSIFICAÇÃO DE INTERFACE Claim Clínico → Biblioteca → N1/N2

**Rodada 77 · 2026-09-23** · Arena Casa  
**Em resposta a:** CARTA DO COMENTADOR À ARENA CASA — “Proposta de solução de engenharia após a Rodada 3” (2026-09-23)  
**Anexo medido:** `ESTRUTURAS DE JSONS VÍNCULOS,PMIDS, BLOCO DE ESTADO.md` (27.518 b, CRLF)  
**Status desta peça:** classificação + proposta de interface para avaliação dos territoriais — **não é aprovação** do COMO EXECUTAR v1.9 nem alteração de schema.

---

## Digitais (corpus fechado)

| Artefato | sha256 |
|---|---|
| Carta arquivada | `6c8042da5430d6ccf5f6c9f7ddf3a3ccdf47c07dca26e514ebb7de441133680c` |
| Anexo upload ≡ série (T2) | `c58617a976362428b0dc91d7c7a77551578e3a590e44bda6fa5bb23954a58886` |
| TRILHA88 script | `a05e979cf9204bc5554337f92ddefe9427f8a4c581eaae5a734826fc51f0a52f` |
| TRILHA88 JSON (16/16) | `18dc89d54720c27805c869c34a171ac47a145929eea925fb5f74ce9873fc94dd` |
| N1 v1.3 | `b06660fd…` |
| N2 v1.4 | `d96ad15b…` |
| Vínculos V7 | 274 registros |
| Bibliografia V7 | 237 fichas (201+33+3) |
| Bloco kit 15/09 | `0a630dba…` |
| Schema-Claim v1.2 | `56dc0e94…` |

**Confissão C88-1:** primeira régua da T13 exigiu `status:` na coluna 0 e acusou 0/0; corrigida para indentação opcional **antes** de publicar. Contagem final: **8** `aprovado` + **14** `aprovado_com_ressalva` = 22 entradas.

**Níveis:** T1–T16 todas em L1 (byte/JSON/schema), exceto T5/T15 (L1 dígito exato em campo), declarados no JSON.

---

## 0. Posição da casa (sem muro)

**Aceito o núcleo da hipótese de engenharia**, com uma correção de ordem e uma condição.

1. **Aceito:** Claim Clínico não cria sistema paralelo. N1 = bibliografia única; N2/Vínculo = relação; multiplica-se o vínculo, nunca o N1 do mesmo PMID. Medido: Bibliografia V7 **0 duplicidade** de `pmid_oficial` em 237 fichas; V7 já opera com 81 `claim_id` distintos e 30 vínculos sem claim mecanístico — o padrão “1 N : N V” já vive no acervo.
2. **Aceito:** o Claim não é N1 nem N2 — é registro do processo de validação. Os dois acervos coexistem e se encaixam por materialização, não por fusão.
3. **Correção de ordem (não discordância — é a mesma assimetria da Rodada 3):** o diagrama da carta pinta `CLAIM → materialização → {Biblioteca, N1} → N2` como se Biblioteca e N2 pudessem nascer no mesmo passo. Medido: `usado_em_biblioteca: nao` em **22/22** claims do kit; `trecho_ancora` do N2 é “cópia LITERAL da frase sustentada” e a frase só existe na canônica se a **afirmação entrar na Biblioteca pelo rito** (bifurcação “(i), com a bifurcação desenhada”). **Precondição:** frase na Biblioteca → então N2. Isso é E-1/Estrutura, não invenção nova.
4. **Condição:** segregação de auditoria herdada da Rodada 3 — quem materializa (produção N1/N2 do kit) não atesta a própria fidelidade.

**Menor alteração suficiente** (preferência do próprio comentador): o que **falta de fato no Claim Kit** é pouco; o que falta é **contrato de saída** + **1 enum no ciclo N1 v1.5** + **passo de entrada na Biblioteca**. Não há arquitetura nova a inventar.

---

## 1. Quadro A–I (pedido §14)

### A. Claim → N1

| Do Claim aprovado | Campo N1 | Como |
|---|---|---|
| `fontes[].pmid` | `pmid_oficial` | **chave de busca**: se já existe → reutiliza N1; se não → cria N1 novo |
| `evidence_role` (ex.: `human_clinical`) | `natureza_evidencia` / `evid_role` do acervo | **não é 1:1 no schema**: N1 v1.3 exige `natureza_evidencia` (enum de 7) e **não possui** `evid_role` como propriedade schema (o acervo legado tem o campo; o schema vigente não). Mapeamento preciso = decisão de contrato, não cópia cega |
| `claim_id` (quando o N1 nasce do kit) | `claim_id_origem` | **proveniência escalar** — ver F |
| (novo) valor de origem | `origem_pipeline = CLAIM_KIT_CLINICO` | **não existe no enum v1.3** — ver §F/§11 da carta |
| `statement`, `nota_ressalva`, `comparador`, `achado`, `moderadores`, `usado_em_biblioteca`, `status` | — | **não alimentam N1** (campos de processo/relação, não bibliográficos) |

**Campos N1 required que o Claim não tem:** `titulo_artigo`, `autores`, `revista_ano`, `doi`, `desenho_estudo(_bruto)`, `g1_metodo`, `id_referencia_interna`. Origem legítima: N1 já existente **ou** metadados da fonte primária no ato da criação — **nunca invenção pelo materializador**.

### B. Claim → N2

| Do Claim aprovado | Campo N2 v1.4 | Como |
|---|---|---|
| `claim_id` | `claim_id` | direto |
| `uso` (ex.: `clinico`) | `uso` + `trilha` | `trilha: clinica` (enum existe; Opção A registrada no schema) |
| `status: aprovado` | `status_auditoria: CONFIRMADO` | mapeamento do Estrutura (Rodada 3), **já verificado campo a campo na trilha 87** |
| `status: aprovado_com_ressalva` | `status_auditoria: PARCIALMENTE_CONFIRMADO` + `ancoras[].direcao_suporte: condicional` + `condicao` | idem; `condicao` obrigatório por `if/then` no N2 v1.4 |
| `nota_ressalva` | `ancoras[].condicao` (e espelho em `claim.nota_ressalva` na materialização) | identidade obrigatória; divergência reprova (regra do Estrutura) |
| `fontes[].pmid` | `ancoras[].id_oficial` **via** `id_referencia_interna` do N1 correspondente | PMID não é `id_oficial`; resolve pelo N1 |
| `fontes[].achado` / `nivel` / `papel` | `achado_central_molecular` / papel da âncora | deriváveis com rótulo; `papel` por âncora está no kit em outro formato (`nivel: principal`) — mapear no contrato |
| `statement` | **não é** `trecho_ancora` | `trecho_ancora` = frase **literal da Biblioteca** (ver H) |
| (geração) | `id_vinculo`, `id_referencia_interna`, `ancora_principal`, `trilha`, `verification_status` | derivados / rito (ver C) |

**N2 required sem fonte direta no kit:** `trecho_ancora` (precisa da frase na canônica), `ancora_principal` (decisão de curadoria da entidade — vazio só se a afirmação ainda não entrou), `trilha` (derivável: claims SM-02 → `clinica`).

### C. Campos derivados (sem nova decisão científica)

- Lookup/reuso N1 por `pmid_oficial`.
- Geração de `id_vinculo` (próximo da série; nunca sobrescrever V7).
- `id_referencia_interna` a partir do N1 resolvido.
- `status_auditoria` e `direcao_suporte`/`condicao` a partir de `status` + `nota_ressalva` (tabela do Estrutura).
- `trilha = "clinica"` para este kit.
- `origem_detalhe` (N1) pode carregar data/proveniência detalhada se o enum for estendido — o schema já separa `origem_pipeline` (categoria pura) de `origem_detalhe`.
- Deduplicação: um N1 por PMID; N ≠ 1 vínculos.

### D. Campos que **realmente** faltam no Claim Kit

Medido (T12): kit **0×** em `trecho_ancora`, `ancora_principal`, `ancoras`, `condicao`.

| Falta? | O quê | Veredicto |
|---|---|---|
| **Não copiar para o kit por antecipação** | `trecho_ancora`, `ancoras[]`, `condicao` como campos novos do Bloco | O comentário §8 da carta está certo: **não acrescentar agora**. Eles nascem na **materialização N2**, não no Claim |
| **Falta de fato no kit** | (1) identificador/ritmo de **entrada da afirmação na Biblioteca** (`usado_em_biblioteca` hoje só marca `nao`); (2) garantia de que cada `fonte.pmid` tenha caminho a `id_referencia_interna`; (3) explicitar `papel`/`nivel` por fonte de forma estável para virar âncora | extensão **mínima** de contrato de saída |
| **Falta no schema N1 (ciclo v1.5)** | enum `CLAIM_KIT_CLINICO` em `origem_pipeline` | alteração pontual, ciclo próprio (como já classificado na r76) |
| **Não é gap do kit** | `titulo` de artigo novo, `desenho_estudo` N1 | preenchidos no N1 a partir da fonte primária no ato de criação |

### E. Reutilização / anti-duplicação

1. Para cada `fontes[].pmid`: **seleção** em `Evidencias/Bibliografia` por `pmid_oficial`.
2. Hit → reusa `id_referencia_interna`; **nunca** segundo N1.
3. Miss → cria N1 novo (metadados da fonte primária) + `origem_pipeline=CLAIM_KIT_CLINICO` (após v1.5) + `claim_id_origem` = claim de origem.
4. Colisão de `id_referencia_interna` (PMID novo × mesmo id legado) → falha dura da materialização, não silêncio.
5. **Reconciliação técnica prévia** (carta §12, aceita): no kit 15/09, **21** PMIDs distintos no Bloco; **7** já na Bibliografia; **14 fora** (`18391129`, `22832816`, `26065825`, `32696276`, `35442429`, `36517638`, `36893912`, `37931509`, `38802507`, `39615605`, `39938607`, `40345445`, `40856326`, `41481888`) — **12 claims** tocam PMID fora. Isso **não** é reabertura científica: é fila de criação de N1 + checagem de existência, antes da primeira materialização.

### F. Proveniência — leitura §10 **confirmada**

- No N1 v1.3, `claim_id_origem` é **`type: string`** (T7) — não pode ser catálogo.
- No acervo: **54/237** preenchidos; valores são **um** `claim_id` mecanístico cada (ex.: `B1.MEC.BLOCO05.002`), sem listas (T16).
- Uso múltiplo de um PMID em vários claims **já** vive nos N2 via `claim_id` (81 claims distintos no V7).
- **Regra proposta (para os auditores avaliarem):** `claim_id_origem` = proveniência do **nascimento** do N1; multipropriedade de uso = só N2/`claim_id`. Se um N1 legado nasceu da busca e só depois foi usado por claim clínico, **não se reescreve** `claim_id_origem` para “fazer bater”; a origem fica `BUSCA_FERRAMENTA` e o uso aparece no vínculo.
- `origem_pipeline` legado no acervo já foge ao enum v1.3 (valores compostos históricos) — medido; não abrir parentesco agora; o ponto do kit é só o valor novo.

### G. Ressalvas — formalização Claim Kit → N2

```text
claim.status = aprovado
  → N2.status_auditoria = CONFIRMADO
  → direcao_suporte ∈ {sustenta, refuta, inconclusivo}  (sem condicao)

claim.status = aprovado_com_ressalva
  → N2.status_auditoria = PARCIALMENTE_CONFIRMADO
  → anchors[].direcao_suporte = condicional
  → anchors[].condicao  OBRIGATÓRIO
  → claim.nota_ressalva ≡ toda condicao derivada  (identidade; divergência reprova)

claim.status aprovado_com_ressalva  SEM nota_ressalva  → reprova na materialização
(condicao) sem direcao_suporte=condicional → reprova (já é regra do schema N2)
```

Segunda semântica: **não**. Uma só tabela; contrato de saída nomeia as setas.

### H. Biblioteca — de onde sai o `trecho_ancora`

1. `statement` do claim aprovado **entra** na Biblioteca da entidade (rito normal da canônica; bifurcação desenhada).
2. Só então o N2 copia **literalmente** a frase canônica para `trecho_ancora`.
3. `usado_em_biblioteca` passa de `nao` → `sim` **no ato** da entrada (hoje: 22/22 `nao` — nenhum claim clínico ancorou ainda; nenhum N2 de kit existe).
4. Portão de ancoragem textual (L-05, já classificado como ciclo próprio) confere depois: `trecho_ancora` ∈ canônica da entidade da âncora principal.

Sem (1), (2) gera vínculo órfão — é exatamente o defeito que o Estrutura descreveu na r76.

### I. Auditoria — quem fica com o quê

| Verificação | Mão |
|---|---|
| Conformidade de schema (N1/N2 JSON válido) | Auditor-Estrutura (mecânica) |
| Ancoragem textual (`trecho_ancora` na canônica) | instrumento do Estrutura; execução pode ser ferramenta |
| Deduplicação por `pmid_oficial` | instrumento do Estrutura |
| Fidelidade ressalva (`nota_ressalva` ≡ `condicao`) | instrumento **se** quem executa não escreveu as duas pontas — senão cai no invariante da r76 (**E-6**, mantida em aberto) |
| Fidelidade claim → N1 → N2 (leitura da fonte primária) | mão **adversarial científica** (Mestre / papel designado) — **nunca** o produtor da materialização |
| Réplica empírica de tudo | bancada (casa) antes de aceitar |

---

## 2. Matriz §15 — classificação pedida

| Elemento | Já existe | Derivável | Falta no Claim Kit | Pertence ao N1 | Pertence ao N2 | Decisão necessária |
|---|---|---|---|---|---|---|
| `claim_id` | sim | — | — | — | sim (`claim_id`) | não (cópia) |
| `status` / `nota_ressalva` | sim | → `status_auditoria`, `condicao`, `direcao_suporte` | não | não | sim (efeitos) | formalizar tabela única (G) |
| `statement` | sim | — | não | não | **não vai para `trecho_ancora`** | rito de entrada na Biblioteca (H) |
| `fontes[].pmid` | sim | lookup N1; `id_oficial` da âncora | caminho garantido a `id_referencia_interna` | chave (`pmid_oficial`) | via âncora | reconciliação dos 14 PMIDs fora (E) |
| `fontes[].achado` / `nivel` / `papel` | sim | mapear para âncora (`papel`, nota) | talvez padronizar vocabulário de papel | não | sim | definir mapeamento no contrato |
| `usado_em_biblioteca` | sim (bool, 22×`nao`) | flip no ato da entrada | **símbolo/ritmo do ato de publicar afirmação** | não | não (é estado do claim) | desenho do passo H |
| `trecho_ancora` | não no kit; obrigatório no N2 | cópia literal após H | **não** (não copiar para o kit) | não | **sim** | ordem: Biblioteca → N2 (E-1) |
| `ancora_principal` / `ancoras[]` | não no kit; obrigatório no N2 | montagem na materialização | **não** | não | **sim** | quem escolhe a principal (curadoria) |
| `id_referencia_interna` | só nos dois lados | sim, via N1×pmid | não | sim | sim | colisão = erro duro |
| `id_vinculo` | só N2 | gerador de série | não | não | sim | política de numeração (fora da série V7 existente) |
| `origem_pipeline=CLAIM_KIT_CLINICO` | **não** no enum | — | não é campo do kit | **sim** | não | **ciclo N1 v1.5** (não unilateral) |
| `claim_id_origem` | sim (string, 54 preenchidos) | gravar no nascimento do N1 novo | não | **sim** | não | ratificar leitura F (§10) |
| `natureza_evidencia` / `desenho_estudo` (N1 novo) | só no N1 | da fonte primária no ato de criação | não exigir no kit | **sim** | não | mapeamento `evidence_role`→enum N1 |
| `trilha: clinica` | no N2 | sim (kit SM-02) | não | não | sim | nenhum — derivável |
| segregação produtor × fidelidade | princípio já convergente (r76) | — | — | — | — | **E-2**: quem produz o N1/N2 do kit |

**Leitura da matriz:** a solução pede **(1) padronização de saída** (contrato Claim → N1/N2), **(2) pequena extensão do Claim Kit** só no passo de entrada na Biblioteca + resolução pmid→referência, **(3) alteração pontual de schema** = enum no ciclo v1.5. **Não** pede arquitetural novo.

---

## 3. Proposta de interface (texto que irá aos dois auditores)

> **Contrato de materialização Claim Clínico → sistema existente (minuta da casa, para parecer — não vigente)**  
> 1. Claim aprovado **não** substitui N1/N2 e **não** cria objeto concorrente.  
> 2. Entrada na Biblioteca pelo rito da entidade **antes** de qualquer N2 novo do kit.  
> 3. N1: lookup por `pmid_oficial`; reuso; criação só na ausência; metadados da fonte primária; `claim_id_origem` = origem escalar; `origem_pipeline` = `CLAIM_KIT_CLINICO` **após** v1.5.  
> 4. N2: contrato único de status/ressalva (tabela G); âncoras resolvidas por N1; `trecho_ancora` literal da canônica; `trilha=clinica`.  
> 5. Reconciliação técnica pré-materialização (E-5 do kit: 14 PMIDs fora) sem reabrir auditoria científica da Bibliografia.  
> 6. Auditoria segregada (quadro I); invariante r76 intacto: **quem produz N1/N2 não atesta a própria fidelidade**.

**Pergunta aos territoriais (redação da carta §16, mantida):**

> “A solução de interface Claim Clínico → Biblioteca → N1/N2 é compatível com os contratos e princípios que cada território protege? Existe algum impedimento técnico ou epistemológico?”

---

## 4. O que **não** decidimos aqui

- Aprovação do COMO EXECUTAR v1.9 / redação da v1.10 (fica no rito em curso).
- Alteração de schema N1/N2 (ciclos próprios: enum v1.5; portões L-05; dedup formal).
- Quem senta na cadeira de fidelidade (E-2) — depende de quem produzirá o N1/N2 do kit.
- E-6 (portão de fidelidade da ressalva × invariante).
- Bytes ≥17/09 e piloto .014 — seguem perguntas **ao operador**, não ao Comentador.

---

## 5. Próximo passo do rito

1. Operador leva **esta peça** ao **Auditor-Mestre** e ao **Auditor-Estrutura**, em **janelas separadas**, com a pergunta do §3 e os anexos (carta + anexo de estruturas + trilha 88).  
2. Respostas territoriais voltam à casa → confronto (mesmo método da Rodada 3).  
3. Só então Comentador consolida interface +, se for o caso, textos para a v1.10.

**A casa não envia nada direto a nenhuma IA.**

---

*Trilha 88: 16/16 · C88-1 declarada · 0 ciência alterada · nada vigente foi editado nesta rodada.*
