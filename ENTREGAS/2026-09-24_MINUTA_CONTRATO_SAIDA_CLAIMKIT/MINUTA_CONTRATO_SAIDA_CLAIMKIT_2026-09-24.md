# MINUTA FINAL — CONTRATO DE SAÍDA DO CLAIM KIT
## Claim Clínico Aprovado → materialização N1/N2 (D1 + R-1 + R-2 integrados)

**Data:** 2026-09-24 · **Origem:** Arena Casa (redação da Rota A do Comentador)  
**Status:** MINUTA para **última subscrição** dos dois territoriais — **não vigente** até dupla subscrição sem ressalva (critério §19 do Comentador).  
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

### 4.3 `inverte` (quando houver efetiva troca de direção)

- **Não** colapsa em um único N2 condicional;
- Materializa como **duas relações N2 complementares** (mesmo PMID → mesmo N1; dois N2), cada uma com sua `condicao` decidida no fechamento:

```text
condição A → sustenta
condição B → refuta   (par que a L-06 resolve por disjunção de condição)
```

- Exemplo canônico do kit: `B1.SM02.001b` (`classe_antidepressivo`, `efeito: inverte`, `aprovado_com_ressalva`);
- **1 PMID → 1 N1 → N ≥ 1 N2** permanece.

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
| `moderadores[efeito=inverte]` (direção troca) | → | **dois N2 complementares** (§4.3) |
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
| P-K4 | Regra de `inverte` → dois N2 (com exemplo `.001b`) | Nova (§4.3) |
| P-K5 | Importar `grau_maturidade` (vocabulário v3.1) ao fechamento clínico quando houver ressalva de maturidade | v1.2 sem o campo; N2 tem o destino |

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

## 11. Pergunta única de subscrição (para os dois territoriais)

> **“Subscrevem, sem ressalva, a minuta do contrato de saída do Claim Kit que integra D1 + R-1 + R-2 conforme a Rota A (§18 da condução), com as pendências P-K1..P-K5 travando a primeira materialização até o ciclo do kit as fechar?”**

Resposta esperada: **subscrevo sem ressalva** · **subscrevo com ressalva(s): listar** · **não subscrevo: impedimento**.

---

*Minuta da casa · Rodada 81 · 2026-09-24 · não vigente até dupla subscrição limpa.*
