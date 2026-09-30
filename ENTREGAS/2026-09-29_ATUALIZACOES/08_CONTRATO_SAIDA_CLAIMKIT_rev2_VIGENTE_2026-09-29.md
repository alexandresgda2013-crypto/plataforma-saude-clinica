# CONTRATO DE SAÍDA DO CLAIM KIT
# ---------------------------------------------------------------------------
# ERRATA DE ETIQUETA — 2026-09-29 (decisão do operador · registrada via Arena)
# O título dizia "MINUTA FINAL" e o campo Status dizia "não vigente até dupla
# subscrição sem ressalva": era o estado na data da redação (24/09), antes das
# subscrições dos dois territoriais. A vigência foi declarada em ato próprio de
# 24/09/2026 (bilhete CONTRATO_SAIDA_CLAIMKIT_VIGENTE.txt, com a frase do
# operador) — o que não havia sido trocado era o título e o status.
# Correção de ETIQUETA e PROCEDÊNCIA: 0 (zero) mudança de conteúdo — nenhum
# eixo, campo, trava ou regra foi tocado. O parágrafo original de status foi
# preservado e marcado como "(na redação)". As passagens do corpo que falam em
# "esta minuta" pertencem ao relato do rito de subscrição (histórico) e foram
# preservadas de propósito.
# Texto aprovado em 24/09 = digital 841532da, preservado byte a byte em
#   "CONTRATO_SAIDA_CLAIMKIT_rev2_ASSINADO_841532da_2026-09-29.bak".
# ---------------------------------------------------------------------------
## Claim Clínico Aprovado → materialização N1/N2 (D1 + R-1 + R-2 integrados)

**Data:** 2026-09-24 · **Origem:** Arena Casa (redação da Rota A do Comentador)  
**Status (atualizado em 2026-09-29):** **VIGENTE — rev.2** · aprovado pelo operador em 24/09/2026 (frase de vigência no bilhete `CONTRATO_SAIDA_CLAIMKIT_VIGENTE.txt`) · digital do texto aprovado: `841532da…` (preservado byte a byte; ver nota de errata no topo).  
*Nota histórica — o parágrafo abaixo descreve o estado na data da redação (24/09/2026), antes das subscrições, e foi preservado sem alteração:*  
**Status (na redação):** MINUTA **rev.2** (2026-09-24) — §4.3 convertido em P-K6 após medição do Estrutura (TRILHA93) · **P-K6 ratificado pelo Comentador** (mesmo dia) com precisão de granularidade por claim (§6 da resposta); sem novo ajuste conceitual. Rascunho final **antes** da circularização aos auditores (rev.2 nunca havia saído às janelas). Para **última subscrição** dos dois territoriais — **não vigente** até dupla subscrição sem ressalva. A rev.1 perde vigência de candidatura; documento mudou ⇒ 2× novo.  
**Base:** Solução D1 (r79) · Pareceres R4 (r80) · Condução Rota A (§18)  
**Não altera:** N1 v1.3, N2 v1.4, Bibliografia, nem o Schema-Claim v1.2 **no texto** — as extensões de campo do kit são listadas como **pendências do ciclo do Claim Kit** (§7), com trava de materialização.

---

## 1. Objeto e princípio único

> **O materializador não decide ciência.** Ele transforma, no máximo, decisões já tomadas no fechamento do claim (rito das três IAs) para a estrutura N1/N2.

Quatro saídas científicas do claim fechado:

| # | Decisão | Vocabulário |
|---|---|---|
| 1 | **Estado** | `aprovado` \| `aprovado_com_ressalva` |
| 2 | **Direção por fonte/relação** | `suporta_relacao` \| `refuta_relacao` \| `inconclusivo` |
| 3 | **Tipo da ressalva** (quando houver) | `condicao_aplicacao` \| `heterogeneidade` \| `maturidade_evidencia` |
| 4 | **Modificações estruturadas** | `atenua` \| `amplifica` \| `inverte` \| `nulo` |

---

## 2. D1 — Dois eixos independentes (já subscrito no núcleo)

```text
status (claim)     → status_auditoria (N2)     — estado da validação
relação científica → direcao_suporte (N2)      — direção evidencial
```

- `aprovado` → `CONFIRMADO`
- `aprovado_com_ressalva` → `PARCIALMENTE_CONFIRMADO`
- **`aprovado_com_ressalva` NÃO implica `direcao_suporte = condicional`.**
- `condicional` + `condicao` **somente** quando houver condição científica real, decidida e registrada no fechamento.
- **Regra abolida (não reintroduzir):** `aprovado_com_ressalva → condicional` por derivação automática.

---

## 3. R-1 — Direção por fonte/relação

### 3.1 Vocabulário (importar, não inventar)

Do Schema-Claim v3.1 (`sentido_do_achado`, OBRIGATÓRIO):

```text
suporta_relacao | refuta_relacao | inconclusivo
```

Mapeamento mecânico único para o N2:

```text
suporta_relacao → sustenta
refuta_relacao  → refuta
inconclusivo    → inconclusivo
```

### 3.2 Granularidade

A direção acompanha a relação **fonte → afirmação** (por fonte/âncora), **não** uma direção única no claim.

### 3.3 Proibições (defaults)

O materializador **não pode** inferir direção de:

- `status` do claim (“aprovado → sustenta”);
- “fonte principal → sustenta”;
- `achado` positivo → sustenta;
- prosa do `statement` / `comparador`.

### 3.4 Falha dura

Claim fechado **sem** direção por fonte/relação → **falha de materialização** (“claim ainda não fechado”). **Nunca** preenchimento automático.

---

## 4. R-2 — Moderadores e fonte única de condição

### 4.1 Fonte única de `condicao`

> **Origem canônica de toda `condicao` do N2:** relação científica **condicional** explicitamente decidida e declarada no fechamento do claim.

Nem `nota_ressalva` isolada, nem `moderadores[]` isolado autorizam `condicao`.  
`ressalvas[]` **não** é fonte independente de direção nem de condição (só classifica).

### 4.2 `atenua` / `amplifica` / `nulo`

- Permanecem **no claim** (`moderadores[]`);
- **Não** viram `condicional`;
- Continuam acessíveis ao Motor via `N2.claim_id` → claim completo;
- **Não** precisam ser copiados para o N2.

### 4.3 `inverte` — PENDÊNCIA ESTRUTURAL NÃO RESOLVIDA (rev.2 · P-K6)

**Rev.2 (2026-09-24):** o §4.3 da rev.1 mandava materializar a inversão como

```text
condição A → sustenta
condição B → refuta
```

O Auditor-Estrutura **mediu** que essa linha é **inválida no N2 v1.4**: o `allOf` das âncoras exige `condicao: null` quando `direcao_suporte ∈ {sustenta, refuta, inconclusivo}`; `condicao` só existe com `condicional`. A casa **replicou** (TRILHA93): a violação é real, nos dois ramos.

Com os campos de hoje, `inverte` genuíno **não tem representação fiel no N2**: ou perde o sentido (dois `condicional`) ou perde a condição (`sustenta`/`refuta` sem texto). Forçar seria repetir a classe de erro de D1.

**Regra vigente nesta rev.2 (dependência estrutural, mesmo trato da maturidade):**

- A informação completa do `inverte` fica **no claim** (`moderadores[]` + ramificações decididas no fechamento), acessível por `N2.claim_id`;
- **O `inverte` NÃO materializa em N2** enquanto não existir campo de condição que coexista com `sustenta`/`refuta`;
- Exemplo canônico bloqueado: `B1.SM02.001b` — claim pode fechar; materialização **travada**;
- **Granularidade (precisão do Comentador §6, 2026-09-24):** P-K6 bloqueia **só claims afetados por `inverte`** — claim sem `inverte` segue os portões normalmente; fail-closed **por artefato**, não bloqueio global do corpus clínico (`B1.SM02.001b` = caso identificado hoje).
- **Não** colapsar em `condicional` único; **Não** descartar a condição.

**Caminho registrado (não altera esta minuta):** campo `condicao_modificadora` na âncora (distinto do `condicao` atrelado a `condicional`) + `allOf` correspondente — **ciclo editorial N2 v1.5**, matéria do Auditor-Estrutura; a minuta se declara **sem alteração de N2 v1.4** e não o adota aqui.

**1 PMID → 1 N1 → N ≥ 1 N2** permanece para os demais casos (múltiplos vínculos por referência são prática corrente do acervo).

### 4.4 Maturidade

```text
ressalva tipo maturidade_evidencia
  → decisão científica no claim
  → grau_maturidade no N2 (enum vigente)
```

**Nunca** `→ condicional`.

---

## 5. `ressalvas[]` (classificação; papel delimitado)

- Registra: `tipo` (+ `nota`; vínculo com a relação quando couber);
- Tipos mínimos: `condicao_aplicacao` | `heterogeneidade` | `maturidade_evidencia`;
- **Não** é segunda fonte de `direcao_suporte` nem de `condicao`.

---

## 6. Tabela de materialização (referência única)

| No claim fechado | → | No N2 v1.4 |
|---|---|---|
| `status: aprovado` | → | `status_auditoria: CONFIRMADO` |
| `status: aprovado_com_ressalva` | → | `status_auditoria: PARCIALMENTE_CONFIRMADO` |
| `sentido_do_achado: suporta_relacao` (por fonte) | → | `ancoras[].direcao_suporte: sustenta` + `condicao: null` |
| `sentido_do_achado: refuta_relacao` | → | `ancoras[].direcao_suporte: refuta` + `condicao: null` |
| `sentido_do_achado: inconclusivo` | → | `ancoras[].direcao_suporte: inconclusivo` + `condicao: null` |
| relação condicional decidida no fechamento | → | `direcao_suporte: condicional` + `condicao` (literal da decisão) |
| `ressalvas[tipo=condicao_aplicacao]` | → | só se (e onde) a relação condicional foi decidida — ver §4.1 |
| `ressalvas[tipo=heterogeneidade]` | → | sem `condicao`; nota permanece no claim |
| `ressalvas[tipo=maturidade_evidencia]` | → | `grau_maturidade` (enum) |
| `moderadores[efeito=atenua\|amplifica\|nulo]` | → | **não materializa em N2** (fica no claim) |
| `moderadores[efeito=inverte]` (direção troca) | → | **não materializa** — P-K6, informação no claim (§4.3 rev.2) |
| `nota_ressalva` (texto livre) | → | permanece no claim; N2.claim_id retorna |
| `claim_id` | → | `claim_id` no N2 |
| `fontes[].pmid` | → | lookup N1 (`pmid_oficial`) → `id_referencia_interna` |

**Proibido na tabela acima:** qualquer linha que derive `direcao_suporte` de `status`, ou `condicao` de `nota_ressalva`/`moderador` sem decisão explícita.

---

## 7. Pendências do ciclo do Claim Kit (trava de materialização)

Estes itens **não** alteram N1/N2; alteram o **kit** e seguem o ciclo próprio (palavra do operador):

| ID | Item | Estado hoje |
|---|---|---|
| P-K1 | Campo de **direção por fonte** no claim (usando vocabulário `sentido_do_achado`) | Ausente no v1.2; vocabulário existe na v3.1 |
| P-K2 | `ressalvas[]` com `tipo` | Ausente no v1.2 |
| P-K3 | Regra de **fonte única** `condicao` escrita no contrato do kit | Nova (§4.1) |
| P-K4 | ~~Regra de `inverte` → dois N2~~ — **superada pela P-K6** (rev.1; o N2 reprova o par — TRILHA93) | Histórico |
| P-K5 | Importar `grau_maturidade` (vocabulário v3.1) ao fechamento clínico quando houver ressalva de maturidade | v1.2 sem o campo; N2 tem o destino |
| P-K6 | Representação fiel de `inverte` no N2: campo de condição coexistente com `sustenta`/`refuta` (ex.: `condicao_modificadora` + `allOf`) — **ciclo editorial v1.5** | N2 v1.4 reprova o par da rev.1; `inverte` não materializa (§4.3 rev.2) |

**Trava:** a **primeira materialização clínica** não começa enquanto P-K1 e P-K2 não existirem no contrato do kit (sem elas, R-1 e o tipo de ressalva não têm onde ser registrados).

---

## 8. Portões da primeira materialização (herdados da Rota A §16)

1. **Científico** — claim fechado com direção por fonte, ressalva classificada, condicionais decididas, moderadores tratados;  
2. **Biblioteca** — afirmação incorporada à canônica;  
3. **N1** — reuso por PMID ou criação correta;  
4. **N2** — trecho, âncoras, direção, condição, estado materializados;  
5. **Mecânico** — schema, cardinalidade, dedup, ancoragem textual;  
6. **Adversarial** — produtor não atesta a própria fidelidade.

---

## 9. O que esta minuta NÃO altera

- N1 v1.3 · N2 v1.4 · deduplicação por `pmid_oficial` · ordem Biblioteca → N2 · `claim_id_origem` (proveniência) · `claim_id` (uso) · segregação produtor × auditor · Biblioteca como fonte única de conhecimento · enum `CLAIM_KIT_CLINICO` (ciclo v1.5) · numeração de vínculos clínicos (ciclo próprio).

---

## 10. Critério de encerramento da Rodada 4 / D1 (§19 do Comentador)

1. ✕ Auditor-Estrutura subscreve esta minuta **sem ressalva**;  
2. ✕ Auditor-Mestre subscreve esta minuta **sem ressalva**;  
3. Arena verifica mecanicamente que a minuta corresponde aos pareceres (trilha);  
4. Operador recebe o pacote final sem divergência residual.  

**Só então:** D1 deixa de ser pendência → preparar piloto `.014` com o rito já corrigido (cego + retorno G3 + estas regras congeladas).

---

## 11. Pergunta única de subscrição (para os dois territoriais — valendo para a **rev.2**)

> **“Subscrevem, sem ressalva, a minuta do contrato de saída do Claim Kit que integra D1 + R-1 + R-2 conforme a Rota A (§18 da condução), com as pendências P-K1..P-K6 travando a primeira materialização até o ciclo do kit as fechar?”**

Resposta esperada: **subscrevo sem ressalva** · **subscrevo com ressalva(s): listar** · **não subscrevo: impedimento**.

---

*Contrato da casa **rev.2** · Rodada 82 · 2026-09-24 · **VIGENTE** desde 24/09/2026 (dupla subscrição limpa cumprida — ver bilhete `CONTRATO_SAIDA_CLAIMKIT_VIGENTE.txt`) · texto aprovado = digital `841532da`, preservado byte a byte em `CONTRATO_SAIDA_CLAIMKIT_rev2_ASSINADO_841532da_2026-09-29.bak`.*
