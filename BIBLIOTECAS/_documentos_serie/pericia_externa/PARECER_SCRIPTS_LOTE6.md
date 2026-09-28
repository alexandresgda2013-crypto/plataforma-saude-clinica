# PARECER — Gate e geradores de bloco, lote 6
**29 scripts periciados. Achei a causa da baixa literalidade.** 10/09/2026

---

# 1. Quadro de veredito

| # | Script | Veredito |
|---|---|---|
| 1 | `gate_script.py` (P-5) | 🟢 **O melhor portão do acervo** — 2 furos |
| 2 | `gera_mod9_BLOCO02` | 🟠 Trecho copiado à mão, sem verificação |
| 3 | `gera_mod9_BLOCO03` | 🔴 **`acha()` com fallback silencioso** |
| 4 | `gera_mod9_BLOCO04` | 🔴 Mesmo defeito, pior (probe de 36 chars) |
| 5 | `gera_mod9_BLOCO05` | 🔴 Mesmo defeito |

---

# 2. 🔴 CAUSA ENCONTRADA: por que só 40% dos trechos são literais

No parecer anterior reportei 33% de literalidade e culpei o `limp_pmid()`. **Estava parcialmente errado.** Fiz a perícia por busca binária de prefixo:

```
VINC_B1_0001: casa 445/446 chars
  TRECHO : 'isão, humano+animal].'
  CORPO  : 'isão, humano+animal] [VERIFICADO]. Essa ativação aguda...'

VINC_B1_0002: casa 445/450 chars
  TRECHO : 'Serhan & Levy, 2018][OB].'
  CORPO  : 'Serhan & Levy, 2018] [VERIFICADO][OB]. A micróglia...'
```

**O trecho está correto. O corpo é que mudou depois.** Os propagadores de selo (lote 1) inseriram `[VERIFICADO]` **dentro** das frases que já eram `trecho_ancora`, quebrando a literalidade retroativamente.

Normalizando os selos dos dois lados:

| Comparação | Literalidade |
|---|---|
| Crua | 103/257 = **40%** |
| Normalizando selos | 130/257 = **51%** |

**Duas conclusões:**

1. **Meu `validar_roundtrip.py` está medindo errado.** Precisa remover selos antes de comparar — senão acusa de não-literal um trecho que é literal. Vou corrigir.
2. **Ainda restam 127 que não casam nem assim** — e a causa desses é o script 3/4/5 deste lote.

---

# 3. 🔴 O `acha()` dos scripts 3, 4 e 5 — fallback que inventa trecho

Os três compartilham o mesmo padrão:

```python
def acha(probe):
    cand = [f.strip() for f in frases if probe[:40] in f]
    if cand: return cand[0]
    ...
    return None

trecho = acha(probe)
...
"trecho_ancora": trecho or probe + ".",   # ← FALLBACK SILENCIOSO
```

Quando a busca falha, ele grava **o probe digitado à mão, com um ponto no fim**, como se fosse trecho literal do corpo. Sem aviso, sem marca, sem distinção. O campo passa a conter texto que **nunca esteve na Canônica**.

Pior: no script 4 o probe é de apenas 36 caracteres, e `frases` vem de um `re.findall` grosseiro que pode capturar títulos. Encontrei a prova nos dados:

```
VINC_B1_0019 trecho_ancora = '### 2.2 — Outros inflamassomas no SNC: NLRP1, AIM2, NLRC4 (BLOCO02.002...'
```

**Um cabeçalho markdown virou trecho-âncora de evidência.**

Os scripts *têm* um validador de literalidade no fim (`if t not in cflat: prob.append(("LIT",...))`) — mas ele só **imprime** a lista de problemas. Os arquivos são gravados de qualquer jeito, nas linhas seguintes. Mesmo padrão de todos os lotes: detecta e não bloqueia.

**Correção:**

```python
t = acha(probe)
if t is None:
    faltas.append((claim, probe[:50])); continue     # não inventa
...
if prob:
    sys.exit(f'ABORTADO: {len(prob)} problemas de literalidade')
# só então gravar
```

---

# 4. 🟠 Script 2 — trechos digitados à mão

Diferente dos outros três, este **não busca no corpo**: o `trecho_ancora` está escrito literalmente na tupla `N2`, com 200–400 caracteres de prosa copiados manualmente.

Funciona enquanto a cópia estiver exata, e a validação final só checa pontuação final (`t[-1] not in '.!?]'`) — **nunca se o texto existe no corpo**. Qualquer edição posterior na Canônica dessincroniza sem ninguém notar.

Um detalhe que confirma o risco: no vínculo de `REF_CAPS_2024`, o trecho cita *"(Heneka/Swanson linhas; Pathogenic NLRP3 mutants, 2024)"* — uma anotação de rascunho, não uma citação formatada. Isso está gravado como âncora de evidência.

---

# 5. 🟢 Script 1 — o melhor portão, e deveria ser o padrão

Acertos que **nenhum outro script tem**:

- **Distingue falha de conteúdo (exit 1) de falha de infraestrutura (exit 2)** — o docstring diz: *"nunca confunde 'não consegui consultar' com 'citação inválida'"*. Isso é maturidade de engenharia
- **Valida enum de `status_auditoria`** — é o único do acervo que faz isso antes do meu `SCHEMA_VINCULO_v1.json`
- Separa `REPROVA` de `INFO` — o item [6] (alto risco sem 2ª verificação) é ressalva declarada, não bloqueio
- Trata pré-canônica com exit 0 e mensagem clara, em vez de reprovar

Dois furos:

| # | Problema |
|---|---|
| G1 | **Não valida `natureza_relacao`.** Valida só `status_auditoria`. Os 30 do lote v2 passariam |
| G2 | **`tier_1_intervencao` não existe.** O item [6] filtra alto risco por `forca_causal == "tier_1_intervencao"` — termo inexistente no acervo (o real é `tier_1_necessidade_e_suficiencia`). Esse critério nunca casa; sobra só o filtro por `uso` |

Corrigidos os dois, este é o portão oficial. Ele já tem a arquitetura certa.

---

# 6. Ação corretiva que assumo

Meu `validar_roundtrip.py` reportou "140 casaram só por prefixo" e eu tratei como defeito dos dados. **Parte é defeito do meu comparador** — ele não normaliza selos. Vou corrigir e reportar o número real. A regra que você me deu vale para mim também: *antes de acusar dado alheio, provar que o comparador não é a causa*.

---

# 7. Ações

| # | Ação | Urgência |
|---|---|---|
| 1 | Corrigir `validar_roundtrip.py` para normalizar selos | 🔴 meu |
| 2 | Auditar os 127 trechos que não casam nem normalizado — quantos são fallback `probe + "."` | 🔴 |
| 3 | Corrigir `acha()` nos 3 geradores: falhar em vez de inventar | 🔴 |
| 4 | Corrigir `VINC_B1_0019` (cabeçalho `###` como âncora) | 🟠 |
| 5 | Gate: acrescentar enum de `natureza_relacao`; corrigir `tier_1_intervencao` | 🟠 |
| 6 | Ordem de execução: selos **antes** dos vínculos, ou re-extrair após selar | 🟠 |

A **ação 6** é a lição estrutural: os selos são inseridos na prosa *depois* que os vínculos foram criados a partir dela. Enquanto essa ordem existir, toda rodada de selagem quebra a literalidade de novo. Ou os selos entram antes, ou o `trecho_ancora` é re-extraído após selar.

---

# 8. Padrão dos 29 scripts, consolidado

| Categoria | Qtd |
|---|---|
| Escrevem sem validar | 11 |
| Detectam e não bloqueiam | 6 |
| Checam corretamente | 3 |
| Só leem | 6 |
| Mortos/redundantes | 3 |

A categoria "detectam e não bloqueiam" é a mais frustrante: **o código de verificação já foi escrito, roda, acha o problema — e o script grava assim mesmo.** Nos três geradores deste lote, o `prob` é calculado e impresso 4 linhas antes do `write_text`. Faltou um `if prob: sys.exit(1)`.

Mande os 7 restantes.
