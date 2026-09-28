# CONFRONTO DOS PARECERES DE INTERFACE — Claim Clínico → Biblioteca → N1/N2

**Rodada 78 · 2026-09-23** · Arena Casa  
**Objeto:** confronto mecânico e documentado dos dois pareceres territoriais de 2026-09-23, sobre a pergunta da carta §16 (redação da Arena §3).  
**Status:** medir e organizar o estado dos pareceres — **não é aprovação** da interface, nem do COMO EXECUTAR v1.9.

---

## Digitais

| Artefato | sha256 | bytes |
|---|---|---|
| Parecer Mestre (upload ≡ série) | `cbc0ab796b59f577f9faac94f23cd0c89817f2ee0184ffd215a0fc926d262c99` | 8.654 |
| Parecer Estrutura (upload ≡ série) | `86d09995eb7a09070e0020feb0f19875b294c4fd0420fbf3ed40266348d46fd3` | 8.632 |
| TRILHA89 script | `2aceadd6789555560d204e5f39c3d7309cec5fad06c130a4901b6bdd9fee10c7` | — |
| TRILHA89 JSON **15/15** | `a3ac74283d91be83021218a29bf60cdb36b9a1ca08cd69749ef39d479f82cf60` | — |
| Classificação da casa (r77) | `9770fe6a128b6a72…` | — |
| N1 v1.3 / N2 v1.4 / L-06 rev.6 | `b06660fd…` / `d96ad15b…` / `98e90bdc…` | — |

**Anti-contaminação (medida, não presumida):** Mestre declara verbatim “não li o encaminhamento paralelo ao Auditor-Estrutura”. Estrutura **não** trouxe linha equivalente neste parecer (0× “não li”). Ausência de declaração ≠ contaminação comprovada — registrado como fato textual (T2).

---

## 1. Quadro dos itens

### P1 — Núcleo da arquitetura (claim ≠ N1 ≠ N2; 1 PMID → 1 N1 → N V2; reuso; proveniência)

| | |
|---|---|
| **Classificação** | **A — convergência material** |
| Estrutura | “A solução é compatível. Não há impedimento técnico nem epistemológico.” Seis itens da minuta compatíveis com N1/N2 como estão. |
| Mestre | “Compatível, sim — a arquitetura da interface é correta e é a menor alteração suficiente.” Confirma campo a campo. |
| Réplica (T9/T13) | Cadeia de ressalva existe nos enums; `claim_id_origem` string escalar nos dois lados. |

### P2 — Resposta à pergunta binária “existe impedimento epistemológico?”

| | |
|---|---|
| **Classificação** | **B — divergência material** (aparente na forma; substância concentrada em P3) |
| Estrutura | **Não** — “Não há impedimento técnico **nem epistemológico**.” |
| Mestre | **Sim** — “há **um impedimento epistemológico**… antes da primeira materialização” (§9 da carta / roteio de ressalva). |
| Leitura da casa | A discordância real de conteúdo está em **P3**. Formulada assim, as respostas binárias são opostas e **não** se reduz a silêncio territorial. |

### P3 — Destino de `aprovado_com_ressalva` / `nota_ressalva` no N2

| | |
|---|---|
| **Classificação** | **B — divergência material** (única divergência substantiva da rodada) |
| Estrutura | §5: “a ressalva tem **mapeamento único** e reprova se ausente” (reafirma a tabela da r76: ressalva → `PARCIALMENTE_CONFIRMADO` + `condicional` + `condicao`). |
| Mestre | §2: a ressalva “**não mapeia para um único destino**”; forçar todo `aprovado_com_ressalva` em `condicional` **fabrica condição** onde a ciência não afirmou; a L-06 degrau 3 (“não é permitido completar a condição por inferência silenciosa”, medido 1× verbatim) usará essa condição fabricada. Propõe **roteio por tipo** (condição de aplicação → `condicao`; heterogeneidade → nota sem `condicao`; maturidade → `grau_maturidade`) e move a ressalva da classe C (derivável) para I (exige auditoria). |
| Réplica (T10/T11/T14) | Ressalvas reais do kit: **4× heterogeneidade**, 1× sexo/divergente (7 strings `nota_ressalva` no Bloco) — tipos que **não** são condição de aplicação existem de fato. Regra 3 da L-06 confirmada. Frases de divergência confirmadas nos dois arquivos. |
| Por que é material | Altera o contrato Claim→N2, a classe da matriz da r77 e o que a auditoria de fidelidade deve checar. Não é detalhe de implementação. |

### P4 — Ordem Biblioteca antes de N2

| | |
|---|---|
| **Classificação** | **A — convergência material** |
| Estrutura | §3.1 e §5: escopo da âncora pelo **destino** da frase; ordem precondição estrutural. |
| Mestre | §3: “Biblioteca primeiro, N2 depois, nunca simultâneos”; diagrama em série. |
| Réplica (T12) | `usado_em_biblioteca: nao` **22/22**. |

### P5 — `claim_id_origem` = proveniência escalar (§10 da carta)

| | |
|---|---|
| **Classificação** | **A — convergência material** |
| Ambos | Confirmam string escalar; uso múltiplo nos N2; **não reescrever** origem legado. T13 verde. |

### P6 — Pontos técnicos só do Estrutura (colisão de id; escopo; numeração `id_vinculo`; eixos mecanísticos vazios)

| | |
|---|---|
| **Classificação** | **C + D — complementaridade / fora do outro território** |
| Estrutura | 4 itens: (1) colisão `REF_*` → sufixo, não falha dura; (2) escopo = BLOCO de destino, não `SM-02`; (3) série `VINC_` com prefixo próprio clínico (não misturar 0275+ na trilha mecanística); (4) ausência de `forca_causal`/`grau_maturidade` em `trilha: clinica` = não-aplicável, nunca fraqueza. |
| Mestre | Não trata estes quatro (silêncio — **não** é consenso nem divergência). |
| Réplica (T4–T8) | Pattern REF ✓ · sufixos `CAPURON_2002b`/`CHEN_2024b`/`CHEN_2024c` ✓ · pattern VINC idêntico ao citado ✓ · 5 candidatos ✓ · prefixos **244+30** ✓ · max B1 **0274** ✓ · `forca_causal`/`grau_maturidade` **274/274** ✓ · 0× no Schema-Claim ✓ · `evid_role` ∉ schema N1 e 237/237 no legado ✓ · escopo `BLOCO_XX`/`APENDICE_CORPUS` sem SM-02 ✓. **Todos os pontos técnicos dele CONFEREM.** |

### P7 — E-6 (portão de fidelidade da ressalva × invariante r76)

| | |
|---|---|
| **Classificação** | **C — complementaridade** (com ressalva de fronteira) |
| Estrutura | Fecha E-6: comparar `nota_ressalva` ≡ `condicao` é comparação de duas cópias (instrumento mecânico), desde quem executa não escreva o materializador. |
| Mestre | Não nomeia E-6; diz que o **roteio** (classificação do tipo da ressalva) é decisão científica / classe I — fica a montante da comparação de cópias. |
| Fronteira a não confundir | Comparar cópias ≠ classificar tipo. As duas falas **podem** conviver; não foram postas em conflito pelos autores. |

---

## 2. Convergências (material)

1. Interface **compatível** no núcleo arquitetônico; menor alteração suficiente; sem sistema paralelo.  
2. Ordem **Biblioteca → N2** obrigatória.  
3. `claim_id_origem` proveniência; dedup por `pmid_oficial`.  
4. `CLAIM_KIT_CLINICO` via ciclo editorial do N1 (não unilateral).  
5. Fidelidade claim→N1→N2 **não** com o produtor (Mestre §4; Estrutura §5).

---

## 3. Divergências materiais

| # | Ponto | Estrutura | Mestre | Impacto |
|---|---|---|---|---|
| **D1** | Destino da ressalva | **mapeamento único** → `condicional`+`condicao` | **roteio por tipo**; `condicional` universal **fabrica condição** e envenena L-06 §regra 3 | Contrato Claim→N2 · matriz r77 (C vs I) · auditoria de fidelidade · motor L-06 |
| **D2** (forma de D1) | “Existe impedimento epistemológico?” | **não** | **sim** (é D1) | Resposta binária da carta §16 |

**Nenhuma outra divergência material** foi encontrada.

---

## 4. Complementaridades

- Estrutura: correções de contrato e padrões (P6) + fecho proposto de E-6 (P7).  
- Mestre: roteio epistemológico da ressalva (P3) + classificação C→I na matriz.  
- Escopo/destino da frase (Estrutura) encaixa no passo H da r77 (Mestre endossa a ordem).

---

## 5. Fora de território / silêncios registrados

- Mestre não avalia patterns/numeração/sufixos (território Estrutura).  
- Estrutura não avalia tipos de ressalva/L-06 (declara escopo: não delibera filosofia) — mas **afirma** “não há impedimento epistemológico”, o que o traz à frente de P2/P3; a casa não absolve a frase por escopo automático: **conta como posição oposta em D1/D2**.  
- Silêncio ≠ consenso (regra da r76 mantida).

---

## 6. Questões ainda sem dados / decisões que não são desta rodada

- Qual texto final do roteio (se prevalecer Mestre) — desenho fino após resolução de D1.  
- Prefixo exato da série clínica de `id_vinculo` — “decisão de quem mantém a série” (Estrutura não propõe valor; casa não inventa).  
- `human_clinical → humana_observacional` com guarda de `desenho_estudo_bruto` — contrato na materialização.  
- Bytes ≥17/09 e piloto .014 — **operador** (herdadas).  
- Ciclos já oficiais fora da interface: enum v1.5, portões L-05, dedup formal.

---

## 7. Consequências já suficientemente demonstradas para a interface (podem seguir como minuta, salvo D1)

- Núcleo arquitetônico A (P1).  
- Ordem em série Biblioteca → N2 (P4).  
- Proveniência `claim_id_origem` (P5).  
- Reuso N1 por PMID; reconciliação técnica dos 14 PMIDs fora (r77).  
- Correção de colisão REF por sufixo (P6.1) — **contra** a falha dura da minuta r77 §E.4; a minuta da casa **deve ser corrigida** quando a interface for reemitida.  
- Escopo da âncora pelo destino da frase (P6.2).  
- Aviso de eixos vazios = não-aplicável (P6.4).  
- Anti-ressalva fabricada **só existe se D1 se mantiver** — ver §8.

## 8. Consequência que **não** pode entrar em contrato antes de resolver D1

- Qualquer texto que diga “`aprovado_com_ressalva` → **sempre** `condicional`+`condicao`” **ou** que adote o roteio de três destinos **antes** de os três lados (Comentador, Mestre, Estrutura — na forma do rito do operador) ciclarem D1.  
- Mover a ressalva na matriz r77 de C para I (pedido do Mestre) — **pendente de D1**.

---

## 9. Estado do rito da interface

| Etapa | Estado |
|---|---|
| Classificação da casa (r77) | ✔ |
| Pareceres independentes (r78) | ✔ · janelas com declaração anti-contaminação no Mestre; sem linha equivalente no Estrutura (registrado) |
| Confronto (esta peça) | ✔ · **1 divergência material (D1/D2)** |
| Rodada 4 (ciclo da divergência pelos 3) | **ACIONAR** — pela regra subscrita do operador: toda ressalva passa por Comentador, Arena e Mestre/Estrutura |
| Consolidação de contrato / v1.10 | **não iniciada** |

---

## 10. Posição da casa (sem muro)

1. **D1 é real.** Não é ruído nem território trocado: são duas regras de materialização incompatíveis sobre o mesmo campo. A casa **não** escolhe sozinha o vencedor.  
2. **O lado empírico do Mestre pesa:** o kit já tem ressalvas de heterogeneidade (4/7 strings medida); a cadeia universal geraria `condicao` sem ciência que a sustente, e a L-06 consome `condicao` no degrau 3 (1× verbatim).  
3. **O lado técnico do Estrutura também:** a tabela da r76 era o mapeamento que ele **especificou** e que a trilha 87 validou campo a campo; ele a reafirma como “mapeamento único”. Não é ignorância — é tese.  
4. **Os quatro pontos técnicos dele conferem 100%** (T4–T8) e podem ser adotados como correções de contrato **independentemente** de D1.  
5. **A minuta r77 da casa tem um erro conhecido** (falha dura de id) — corrigir na reemissão, com crédito à correção dele.  
6. **Próximo passo do rito:** devolver **apenas D1/D2** aos dois territoriais para Rodada 4 (ver o parecer um do outro **só neste ponto**, conforme o ciclo do operador), e levar o confronto ao Comentador como condutor do fechamento.

---

## 11. Pergunta única para a Rodada 4 (redação sugerida aos dois)

> **D1 — Qual é o destino correto de `aprovado_com_ressalva` na materialização Claim → N2?**  
> (a) mapeamento único em `PARCIALMENTE_CONFIRMADO` + `direcao_suporte=condicional` + `condicao` obrigatória;  
> (b) roteio por tipo de ressalva (condição / heterogeneidade / maturidade), com classificação humana/científica antes da escrita do N2;  
> (c) outra formulação que os dois subscritem **sem ressalva**.  
> Exigência do rito do operador: **só fecha quando os três (Comentador + os dois territórios neste ponto) concordarem 100% sem ressalva.**

---

*Trilha 89: 15/15 · upload ≡ série · 0 ciência alterada · confronto não é aprovação.*
