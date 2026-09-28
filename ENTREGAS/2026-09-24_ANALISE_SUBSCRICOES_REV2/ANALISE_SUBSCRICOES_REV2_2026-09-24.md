# ANÁLISE DA ARENA — SUBSCRIÇÕES DA MINUTA · PONTO DO `inverte` · V3.1 AO MESTRE

**Data:** 2026-09-24 · **Origem:** Arena Casa · **Rodada 82**  
**Objeto:** (1) veredito sobre a objeção do Estrutura ao §4.3; (2) resposta à pergunta do operador sobre a v3.1 e o parecer do Mestre; (3) minuta rev.2 pronta; (4) rota de fecho.  
**Status:** análise + rev.2 para nova subscrição — **não é encerramento** de D1.

---

## 0. Respostas diretas

### Pergunta 1 — A objeção do Estrutura está certa?

**SIM. Medida e replicada.** O `allOf` do N2 v1.4 (âncoras) determina:

| Se `direcao_suporte` = | Então `condicao` |
|---|---|
| `condicional` | **obrigatória** (string minLength 1) |
| `sustenta` \| `refuta` \| `inconclusivo` | **`type: null`** (preenchida = inválida) |

O §4.3 da rev.1 pedia `condição A → sustenta` com condição preenchida ⇒ **violação exata** (TRILHA93 T4/T5). As duas saídas alternativas que o Estrutura enumerou (perder sentido ou perder condição) também conferem. **A rev.1 tinha um erro real.**

### Pergunta 2 — O parecer do Mestre precisa da v3.1 para estar completo?

**Resposta matizada (medida):**

| O que ele verificou | Precisa de v3.1? |
|---|---|
| Regras de materialização (R-1, defaults, falha dura, mapeamento → enum N2) | **Não** — alvo é o N2, que ele leu |
| Os 4 pontos epistemológicos (suficiência, significado, casos, fabricação) | **Não** — v1.2 + Bloco + N2 bastam |
| Fato de a minuta citar “Schema-Claim v3.1, `sentido_do_achado`, OBRIGATÓRIO” (§3.1) | **Sim** — ele **assinou um texto que afirma um fato** sobre um arquivo que **declarou não receber** |

Ele foi **honesto**: “subscrevo a regra de materialização; não verifiquei a v3.1”. Ou seja: **a análise das regras está completa; a subscrição do documento, não** — falta-lhe conferir a citação de origem do vocabulário (P-K1).

**Recomendação da casa: enviar a v3.1 ao Mestre** na próxima rodada (arquivo existe, digital `f7e664d73e2dad603f7c4316df09286f0da9313a28779d2a67eb5f5fd225624e`). Custo zero; fecha a única lacuna declarada dele. Junto com a **rev.2**, porque o documento mudou.

---

## 1. Confronto das duas respostas

| Ponto | Mestre | Estrutura | Casa |
|---|---|---|---|
| Núcleo D1 (dois eixos) | sem ressalva | sem ressalva | **A — fechado** |
| R-1 (direção/defaults/falha dura) | sem ressalva | sem ressalva (“resolve a H-2 como recomendei”) | **A — fechado** |
| R-2 fonte única / atenua/amplifica/nulo | sem ressalva | sem ressalva | **A — fechado** |
| **§4.3 `inverte` → dois N2** | **sem ressalva** (“estruturalmente possível”; validação fina **delegada ao Estrutura**) | **impedimento medido** (schema reprova) | **B — divergência… mas não simétrica** |
| Maturidade → `grau_maturidade` | sem ressalva | (fora do ponto) | **A** |

**Classificação honesta de §4.3:** o Mestre **não contradiz** a medição do Estrutura — ele **declarou** não opinar sobre “if/then de schema; território do Auditor-Estrutura” e assinou com essa fronteira. Quem testou o schema foi o Estrutura. **A casa mediu: o Estrutura está certo.** Não há briga de interpretação; há um **erro da minuta** que só um dos dois testou.

**Consequência (rito):** documento mudou (rev.1 → rev.2) ⇒ **as duas assinaturas da rev.1 não valem para a rev.2** ⇒ **2× subscrição nova** sobre a rev.2.

---

## 2. O que a rev.2 faz (pronta no pacote)

1. **§4.3 → P-K6:** `inverte` **não materializa** em N2 até existir campo de condição coexistente com `sustenta`/`refuta` (caminho `condicao_modificadora` registrado, **ciclo editorial v1.5**, não adotado aqui);
2. Informação completa **fica no claim** (via `claim_id`) — mesmo trato da maturidade;
3. `.001b` nomeado como **materialização travada**;
4. Tabela **P-K1..P-K6** com trava da 1ª materialização;
5. Declaração **sem alteração de N2 v1.4** mantida;
6. Instrução ativa antiga removida (citação histórica do erro permanece com rótulo).

Com P-K6, **o próprio Estrutura declarou**: “subscrevo a minuta inteira sem ressalva”.

---

## 3. Rota de fecho (§19 do Comentador, mais uma passada)

1. Operador manda a **rev.2 + esta análise + as duas respostas + v3.1** às **duas janelas** (mesmo pacote);
2. Cada um responde **sobre a rev.2** (subscrevo sem ressalva / com ressalva / não subscrevo);
3. Casa roda a trilha de correspondência final;
4. Dupla subscrição limpa ⇒ **D1 encerra** ⇒ prepara piloto `.014`.

**Cola pronta** no pacote (`COLA_REV2_...md`).

---

## 4. Digitais

| Artefato | sha256 |
|---|---|
| Subscrição Mestre (upload ≡ série) | `40b0205c11c042e081b3706161b75e2f7883a6b19a37016cc69c1ebc15d65953` |
| Subscrição Estrutura (arquivada) | `63e23c2af34e9b08020a7d148d6c8b20f891750a5b29a4ef38d12714fa4aed9e` |
| Minuta rev.1 (base) | `fe27012a2055b2c7e4cd0590e74c070031041ec2de878aba324cd0460abe7abd` |
| **Minuta rev.2** | `c44066f6e9f864bd9f0c6571860526065ae578fee9b5b32d6e9a473834be467a` |
| TRILHA93 JSON **12/12** | `6162e7a803ee707f15e3685021418a777f91734f32592fce85e74fa530300d85` |
| Schema-Claim v3.1 (a enviar ao Mestre) | `f7e664d73e2dad603f7c4316df09286f0da9313a28779d2a67eb5f5fd225624e` |
| N2 v1.4 | `d96ad15b…` |

---

## 5. Posição da casa (sem muro)

- O **Erro da rev.1 é nosso** (aceitamos o §4.3 do Comentador sem rodar o `allOf` na redação — a trilha 92 checou cobertura textual, não validade do par). **Confissão C92-2:** medir “a minuta cita os blocos §18” ≠ medir “o que a minuta manda é válido no schema”. A lição entra no método: **toda regra de materialização nova passa por simulação de schema antes de sair.**
- O **Estrutura fez o trabalho dele** (mediu, apontou o caminho, não criou campo por conta própria).
- O **Mestre assinou dentro da fronteira declarada** (não testou schema — e disse).
- A **v3.1 vai ao Mestre** — não por ressalva dele, mas para a assinatura cobrir o texto inteiro.

**0 ciência alterada. D1 aberta até 2× na rev.2.**

---

*Assinatura da casa — Arena · Rodada 82 · sha256 publicado no DIGITAIS do pacote.*
