# RESPOSTA DA ARENA CASA — SOLUÇÃO D1 (COMENTADOR) + RODADA 4 PRONTA

**Rodada 79 · 2026-09-24** · Arena Casa  
**Em resposta a:** “SOLUÇÃO DO COMENTADOR — D1” (2026-09-24)  
**Status:** posição da casa + pacote para Rodada 4 · **D1 ainda não encerrada** (falta os dois territoriais subscreverem sem ressalva, pelo rito do operador).

---

## 0. Envio da digital da casa (pedido do operador)

Esta resposta **inteira** deve acompanhar a Rodada 4 **nas duas janelas** (Estrutura e Mestre), junto com `COMENTADOR_SOLUCAO_D1_2026-09-24.md`. Assim cada territorial vê que a casa **subscreveu a tese com ressalvas nomeadas (H-1..H-3)** antes do parecer dele — digital da casa no processo, sem muro e sem surpresa.

- O que **cada um cola** continua sendo só o bloco dele (§3.A ou §3.B).
- A digital desta peça é o sha256 do próprio arquivo, publicado no `DIGITAIS.txt` do pacote e no CHANGELOG da rodada 79 (zip). Trocar uma letra invalida a digital — em caso de alteração, nova versão datada.

---

## Digitais

| Artefato | sha256 |
|---|---|
| Carta D1 arquivada | `b83bcc9457846fe2010976f3ba202e53446a38c2eea002d1cf19ce57c03b57dc` (15.072 b) |
| TRILHA90 script | `5fbd1e1425a6745f5d26d58a8dc2414f31c2e3d96cf91cb5e6ec747cf652011e` |
| TRILHA90 JSON **11/11** | `04b81e21fd915fffe946657a3887a17db326b38be7c56cb7c2031d5303c13230` |
| Base r78 confronto | `7d0b53f06928b50bcad8e0ded98a66e45d4fd5b6d2c588c59300d01e4613846d` |
| N2 v1.4 | `d96ad15b…` |

**Trilha 90 (11/11):** enums e if/then do N2 batem · `B1.SM02.001` verbatim do §12 ✓ · Schema-Claim **não** tem `ressalvas[]` estruturadas (lacuna real que a carta quer preencher) · kit com heterogeneidade de verdade · L-06 “inferência silenciosa” 1× · a **minuta r77 da casa** continha a cadeia `aprovado_com_ressalva → condicional` (é o alvo da abolição) · eixos do N2 vivem em camadas distintas (status no vínculo; direção na âncora) — o colapso era **derivação Claim→N2**, não colisão de schema.

---

## 1. Posição da casa (sem muro) — **ACEITO**

A solução de **dois eixos** resolve D1 de forma melhor do que as opções (a) e (b) puras:

1. **Diagnóstico correto:** `status_auditoria` (estado da validação) e `direcao_suporte` (relação evidencial) respondem perguntas diferentes. Colapsar `aprovado_com_ressalva → condicional` era **erro de derivação**, não falta de campo no N2.
2. **Preserva os dois pareceres:**  
   - Estrutura: N2 v1.4 intacto; if/then de `condicao` permanecem; testes mecânicos intactos; menor alteração.  
   - Mestre: proibição de fabricar condição; L-06 degrau 3 protegida; classificação semântica = auditoria científica.
3. **E-6 em duas camadas** (classificar × preservar) fecha a fronteira sem contradição com o invariante “quem produz não atesta”.
4. **Exemplo real:** `.001` com “Efeito por sexo diverge…” **não** pode virar `condicional` — medido no kit (T5/T7).
5. **A casa corrige a si mesma:** a Tabela G da r77 (“aprovado_com_ressalva → condicional” universal) fica **SUPERADA** por esta carta, sujeita à subscrição dos dois territoriais. Nada vigente de schema foi alterado.

**Ressalvas honestas da casa (não são objeções à tese):**

| # | Ressalva |
|---|---|
| H-1 | `ressalvas[]` com `tipo` é **extensão do contrato do Claim Kit** — vocabulário e cardinalidade entram no ciclo do kit / palavra do operador; não vira vigente por carta do Comentador. |
| H-2 | Direção efetiva (`sustenta/refuta/inconclusivo`) quando **não** há condicional: em claims clínicos, de onde ela sai hoje? O kit tem `achado`/`nivel`, não `direcao_suporte`. Materializador precisa de fonte determinística (fonte principal / relação declarada) — **item de contrato** na Rodada 4 ao Estrutura. |
| H-3 | D1 só encerra com **2× subscrever sem ressalva** (mais você já com a rota dos 3). Até lá: proposta, não vigência. |

---

## 2. O que muda no nosso material da r77

- Tabela G / §G da classificação: cadeia universal **abolida** (se D1 fechar como (c)).
- Classe da ressalva na matriz §15: de “derivável” → **decisão científica + auditável** (endossa Mestre; casa alinha).
- Minuta §E.4 (falha dura de id) já corrigida pelo Estrutura na r78 — manter na próxima reemissão do contrato.

---

## 3. RODADA 4 — textos prontos (janelas separadas)

> **Anti-contaminação:** cada auditor recebe **esta carta do Comentador + o trecho de comando abaixo**. Não colar o outro parecer inteiro nem a resposta do outro território.

### 3.A → AUDITOR-ESTRUTURA (cola isto)

```text
# RODADA 4 — D1 — AO AUDITOR-ESTRUTURA

Data: 2026-09-24
Origem: operador (ciclo da Arena)

O Comentador propôs fechar D1 pelo modelo de dois eixos (anexo: SOLUÇÃO DO COMENTADOR — D1).

Pergunta única (redação do Comentador §17):

“Os dois territórios subscrevem que a separação entre estado de validação e direção de suporte resolve D1 sem alterar indevidamente N1/N2?”

No seu território, verifique especificamente:
1. compatibilidade da solução com N2 v1.4;
2. possibilidade de manter os if/then existentes;
3. necessidade ou não de alteração de schema;
4. testes mecânicos possíveis;
5. (complemento da casa — H-2) quando direcao_suporte não for condicional, qual campo/derivação do Claim→N2 fornece a direção efetiva de forma determinística.

Responda: subscreve sem ressalva, subscreve com ressalva (listar), ou não subscreve (impedimento).
Não é pedido: recriar claims, refazer bibliografia, novo modelo de vínculo.

Ressalvas da casa no rito (valem para as duas janelas):
- H-1: o vocabulário/campo `ressalvas[]` do Claim Kit é contrato do kit (ciclo próprio); não precisa ser fechado neste parecer — só não pode ser pressuposto como vigente.
- H-3: D1 só se encerra com os DOIS territórios subscrevendo SEM ressalva (rito do operador). Uma ressalva aberta mantém D1 em aberto.
```

### 3.B → AUDITOR-MESTRE (cola isto)

```text
# RODADA 4 — D1 — AO AUDITOR-MESTRE

Data: 2026-09-24
Origem: operador (ciclo da Arena)

O Comentador propôs fechar D1 pelo modelo de dois eixos (anexo: SOLUÇÃO DO COMENTADOR — D1).

Pergunta única (redação do Comentador §17):

“Os dois territórios subscrevem que a separação entre estado de validação e direção de suporte resolve D1 sem alterar indevidamente N1/N2?”

No seu território, verifique especificamente:
1. suficiência epistemológica da classificação;
2. se os tipos de ressalva preservam o significado científico;
3. se existe algum caso relevante ainda não coberto;
4. se a solução impede fabricação de condição.

Responda: subscreve sem ressalva, subscreve com ressalva (listar), ou não subscreve (impedimento).
Não é pedido: recriar claims, refazer bibliografia, novo modelo de vínculo.

Ressalvas da casa no rito (valem para as duas janelas):
- H-1: o vocabulário/campo `ressalvas[]` do Claim Kit é contrato do kit (ciclo próprio); não precisa ser fechado neste parecer — só não pode ser pressuposto como vigente.
- H-3: D1 só se encerra com os DOIS territórios subscrevendo SEM ressalva (rito do operador). Uma ressalva aberta mantém D1 em aberto.
```

**Anexo comum às duas janelas:** `COMENTADOR_SOLUCAO_D1_2026-09-24.md`.

---

## 4. Estado do rito

| Etapa | Estado |
|---|---|
| D1 identificada (r78) | ✔ |
| Solução do Comentador (r79) | ✔ · casa **aceita** a tese (com H-1..H-3) |
| Rodada 4 — 2 subscrições | ** sua ação** |
| Encerramento D1 / contrato Claim→N2 final | após 2× sem ressalva |
| v1.10 / bytes / piloto | fluxos paralelos intactos |

---

*Trilha 90: 11/11 · 0 ciência · nada N1/N2/kit/L-06 alterado · proposta não é vigência.*

---

## Assinatura da casa neste ato

**Arena Casa — Rodada 79 — 2026-09-24**  
Posição: **subscreve a solução de dois eixos do Comentador, com ressalvas H-1, H-2 e H-3 nomeadas.**  
Digital: sha256 deste arquivo, registrado em `DIGITAIS.txt` (pacote) e CHANGELOG r79 (rev.3+envio).
