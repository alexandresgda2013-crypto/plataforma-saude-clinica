# PARECER — Lote 7 (final) + síntese dos 36 scripts
10/09/2026

---

# 1. Quadro do lote

| # | Script | Veredito |
|---|---|---|
| 1 | `gera_mod9_BLOCO06` | 🔴 Mesmo `acha()` com fallback |
| 2 | `sintese()` BLOCO 07/11 | 🔴 Fallback + probe de 30 chars |
| 3 | `gera_mod9_BLOCO08` | 🔴 Idem |
| 4 | `build()` BLOCO 09/10 | 🔴 Idem |
| 5 | `monta_CHECKPOINT_02` | 🟢 **Bom** — e o melhor texto de todo o acervo |
| 6 | `reordena_subsecoes` | 🟠 Correto, mas reescreve a Canônica inteira |
| 7 | `preenche_trecho_literal_v2` | 🟢 **Corrigiu o que o gerador estragou** |

---

# 2. 🟢 Script 7 — explica os 93% do lote v2

No lote 4 mostrei que os 30 vínculos do v2 têm 93% de literalidade contra 33% do resto. **Este script é a razão.**

```python
trecho = frase_literal(sub, cita)
...
if trecho not in texto:
    falhas.append((rot, "trecho não é substring literal")); continue   # NÃO grava
v["trecho_ancora"] = trecho
```

Ele faz o que os geradores deveriam ter feito: **localiza a frase real no corpo, verifica que é substring literal, e pula se não for** — em vez de inventar `probe + "."`. Delimita a frase por pontuação a partir da citação, o que é a abordagem correta.

**Este é o padrão.** O `acha()` dos geradores deveria ter sido escrito assim desde o início.

## E revela a cadeia de escrita completa

Ele grava `status_auditoria = "G1_eutils + G2_elegibilidade + G3_abstract_lido"` — **fora do enum**. Mas o dado real hoje tem `CONFIRMADO` (26) e `PARCIALMENTE_CONFIRMADO` (4).

Logo: **outro script sobrescreveu depois** — o `aplica_vereditos` do lote 2. A ordem foi:

```
add_vinculos_b1v2 (lote 3)  → cria os 30 com claim_id vazio e natureza_relacao=forca_causal
preenche_trecho_literal (7) → conserta os trechos (93% literais), grava status fora do enum
aplica_vereditos (lote 2)   → sobrescreve status com o enum correto
```

**Três scripts escreveram nos mesmos 30 registros, em sequência, nenhum validando o resultado do anterior.** O `claim_id` vazio atravessou os três porque nenhum olhou para ele.

Uma ressalva no script 7: `re.search(r'(20\d\d)', ...).group(1)` estoura com `AttributeError` se a revista não tiver ano — e a lista `candidatos` é construída e nunca usada (usa só `cita`).

---

# 3. 🟢 Script 5 — o melhor texto do acervo

O bloco "Inventário negativo / honestidade do lote" é o artefato mais valioso que vi em 36 scripts:

> *"BLOCO02.006 (RLRs): busca não retornou literatura direta SNC/comportamental. Registrado `nao_estabelecido`. **Não forçado.**"*
> *"BLOCO02.012: apenas IL-6/5-HTTLPR tem vínculo humano forte. IL1B, TNF-308, TLR4, NLRP3, CRP: herança do GPM, sem PMID dedicado — **lote de genética humana, não inventado**."*
> *"miR-155 não retornou artigo SNC-comportamental — `nao_estabelecido`."*

Isto é **declaração explícita de ausência de evidência**, nomeando o que faltou e por quê. É exatamente a conduta que você exige ("se a regra bloqueia, reportar o bloqueio") e é o que a literatura de guidelines computáveis chama de *fidelidade*: nada omitido nem acrescentado sem explicação.

**Recomendação: torne esse bloco obrigatório em toda biblioteca.** Não como texto livre — como seção com formato fixo, e um item no checklist verificando que existe.

---

# 4. 🟠 Script 6 — correto, mas com risco desproporcional

Reordenar subseções é legítimo. O problema é o método: **reconstrói o arquivo inteiro linha a linha e o sobrescreve**, sem backup e sem dry-run. Verifica a ordem *depois* de gravar.

E há um efeito colateral não declarado: `re.sub(r"\n{3,}", "\n\n", new)` altera espaçamento em todo o documento — inclusive dentro de blocos de código e tabelas, se houver. Para um script cujo objetivo é "preservar 100% do conteúdo", isso é mais do que ele promete.

Mínimo: comparar `sorted(linhas_antes) == sorted(linhas_depois)` antes de gravar, e abortar se divergir.

---

# 5. Os quatro geradores restantes

Repetem exatamente o defeito do lote 6 — `t or probe + "."`, `prob` calculado e impresso, `write_text` logo abaixo. O script 2 e o 4 pioram: refatoraram o padrão em funções (`sintese()`, `build()`), o que **propaga o bug** para todos os blocos de uma vez, com probe reduzido para 30 caracteres.

Um detalhe do script 2: nos vínculos do BLOCO_07 os trechos contêm `"(CAPS, PMID 38321014)"` e `"(PMID 40602264)"`. **PMID dentro do `trecho_ancora`** — que é copiado do corpo. Se estiver no corpo, viola a regra "zero PMID no texto corrido". Vale conferir.

---

# 6. SÍNTESE FINAL — 36 scripts

## Distribuição

| Categoria | Qtd | % |
|---|---|---|
| Escrevem sem validar | 13 | 36% |
| **Detectam e não bloqueiam** | 10 | 28% |
| Checam corretamente | 4 | 11% |
| Só leem / utilitários | 6 | 17% |
| Mortos ou redundantes | 3 | 8% |

## O diagnóstico em uma frase

> **O acervo não tem falta de verificação — tem verificação que não bloqueia.**

Dez scripts calculam a lista de problemas, imprimem, e gravam mesmo assim. O código já existe. Falta `sys.exit(1)`.

## Os defeitos, em ordem de dano

| # | Defeito | Onde | Dano medido |
|---|---|---|---|
| 1 | `natureza_relacao = forca_causal` (mesmo parâmetro) | lote 3 #4 | 30 vínculos, motor perde 30 de 136 |
| 2 | `trecho_ancora = probe + "."` (fallback) | 7 geradores | ~127 trechos não-literais |
| 3 | Selo inserido depois quebra literalidade | lote 1 #4/#5 | 27 trechos + meu validador errado |
| 4 | Guarda anti-duplicação com `.match()` | lote 1 #5 | +109 selos por execução |
| 5 | Jaccard 0 + bônus de ano troca autoria | lote 5 #4 | risco não medido |
| 6 | Regex sem `et al.` vê 7 de 270 citações | lote 4 #4 | checador cego |

## O que já está certo e deve ser preservado

| Prática | Script modelo |
|---|---|
| Verifica literal e **pula** se falhar | lote 7 #7 |
| `assert` antes de gravar | lote 5 #5 |
| Exit 1 conteúdo / exit 2 infra | lote 6 #1 (`gate_script`) |
| Só lê, reporta, não decide | lote 5 #1 |
| Inventário negativo declarado | lote 7 #5 |
| Caminho relativo sem hard-code | lote 1 #2 |
| Log de proveniência com data/hora | lote 2 #1 |
| Correção que **enfraquece** alegação | lote 5 #5 |

**Nenhum script tem mais de duas destas oito.** Reunidas num módulo comum, resolvem os seis defeitos.

---

# 7. Proposta de correção — três arquivos, não trinta e seis

Não proponho reescrever o acervo. Proponho **um módulo** que os escritores importem:

```python
# ferramentas/contrato.py
def validar_vinculos(vinc, schema)      # enum por campo + troca entre campos
def verificar_literal(trecho, corpo)    # normaliza selos/negrito antes de comparar
def gravar_seguro(path, dados, backup=True)   # backup + escrita atômica
def abortar_se(problemas)               # sys.exit(1) com relatório
```

Depois, uma linha em cada escritor:

```python
from contrato import validar_vinculos, abortar_se
abortar_se(validar_vinculos(n2, SCHEMA))
```

E dois níveis de pasta: `ferramentas/` (vigentes, quem escreve valida) e `_analises/` (descartáveis, só leem).

---

# 8. Ordem sugerida de execução

| # | Ação | Por quê |
|---|---|---|
| 1 | Corrigir meu `validar_roundtrip.py` (normalizar selos) | Sem isso, todo número que eu reportar está errado |
| 2 | Escrever `contrato.py` | Base dos demais |
| 3 | Blindar os 3 escritores ativos (`aplica_vereditos`, `add_vinculos`, selos) | Impede novo dano |
| 4 | Rodar `checklist_entrega_v2.py` nas 16 | Mapa real de conformidade |
| 5 | Reauditar os 30 (claim_id + natureza_relacao) | IMPL-45 |
| 6 | Re-extrair os ~127 trechos com o método do script 7 | IMPL nova |

**Sugiro parar a perícia aqui e começar pelo item 1.** Já tenho o que precisava: os 36 scripts confirmaram o mesmo padrão, e os próximos confirmariam de novo.

---

# 9. Nota final

Vale dizer com clareza, porque as sete rodadas foram duras com o código: **o problema deste projeto nunca foi a ciência.** O inventário negativo do script 5, o contra-padrão do TEPT, a correção que rebaixa `[VERIFICADO]` para `[PRÉ-CLÍNICO]`, a tabela de confundidores com o rs6971 — isso é trabalho de qualidade rara, e apareceu em todos os lotes.

O que falhou foi a camada de transporte: 36 scripts, cada um com seu conceito do que é um dado válido, escrevendo nos mesmos arquivos sem se falarem. É um problema conhecido, tem solução conhecida, e é o mais barato de consertar de todos os que você tem pela frente.
