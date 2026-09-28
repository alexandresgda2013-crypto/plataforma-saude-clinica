# ITEM 3 — bloqueio reportado + AT-02 executado
10/09/2026

---

# 1. 🔴 BLOQUEIO: os 3 escritores não existem no meu workspace

O item 3 era blindar `aplica_vereditos.py`, `add_vinculos_b1v2.py` e o propagador de selos. **Procurei os três: não estão aqui.** Eu os periciei a partir do código colado no chat; os arquivos vivem no ambiente do outro agente.

**Não vou recriá-los de memória.** Uma cópia minha seria um quarto dialeto do mesmo script — exatamente o defeito que estamos consertando —, e eu blindaria um arquivo que ninguém executa enquanto o original continua rodando sem contrato.

**O que preciso, quando for conveniente:** os três arquivos, ou a confirmação de que o outro agente os blinda com o `contrato.py` no lado dele. Prefiro a segunda: são os scripts dele, na bancada dele.

Enquanto isso, executei o item da fila que **é** possível aqui e que estava logo atrás.

---

# 2. ✅ AT-02 EXECUTADO — literalidade de 40% para 71%

```
ANTES                          DEPOIS
LITERAL   103 (40%)            LITERAL   183 (71%)
ROTULO     77                  ROTULO     18
PROSA      55                  PROSA      55
SELO       22                  SELO        1
```

**80 vínculos reancorados.** Backup em `vinculos_referencia_afirmacao.json.bak_20260911_003043`.

Ferramenta: **`ferramentas/reancorar.py`**, dry-run por padrão, `--apply` para gravar.

---

# 3. O método — e o erro que ele quase cometeu

O script usa a lógica do melhor script do acervo (lote 7 #7): localizar a frase real, **verificar que é substring literal, pular se não for**. Nunca inventa.

**Na primeira execução ele recuperou 99 trechos — e um deles estava errado:**

```
VINC_B1_0001
  antes: «…e-1 (Swanson et al., 2019)[OB; revisão, humano+animal].»
  novo : «… reconhecem motivos moleculares conservados (PAMPs, ex.»
```

O candidato **era literal no corpo** — passava na verificação — mas era **outra frase**. Isto é a mesma classe do resolvedor de parênteses do lote 5, que trocou autoria Menard→Li: um reparo que substitui dado verdadeiro por outro dado verdadeiro porém alheio.

Acrescentei três guardas:

| Guarda | Regra |
|---|---|
| **É a mesma frase?** | prefixo comum ≥ 60 chars **e** ≥ 50% do alvo |
| **Tamanho compatível?** | entre 0,6× e 1,6× do original |
| **Muda alguma coisa?** | candidato idêntico ao atual não é reparo |

Resultado: **99 → 80 reparos, 19 recusados**, com motivo nomeado:

```
VINC_B1_0001 [SELO]   candidato diverge cedo (prefixo comum 162/446) — seria troca de frase
VINC_B1_0040 [ROTULO] candidato diverge cedo (prefixo comum 90/299)  — seria troca de frase
```

**Os 19 recusados são um bom resultado, não uma falha.** São exatamente os casos em que a recuperação automática erraria. Ficam na fila manual.

---

# 4. Validação diferencial — o contrato funcionou contra mim

Na primeira tentativa de `--apply`, o contrato **abortou**:

```
❌ ABORTADO: o resultado tem 33 bloqueante(s). Nada gravado.
   [VINC_B1V2_0179] natureza_relacao: valor 'tier_3_...' é do enum de 'forca_causal'
```

Estava certo em bloquear, mas o critério era errado: aqueles 33 são **pré-existentes** (AT-01 e AT-11) e não têm relação com a reancoragem. Do jeito que estava, nenhum reparo poderia ser aplicado à B1 até que *todos* os defeitos históricos fossem resolvidos.

Mudei para **validação diferencial**: fotografa os bloqueantes antes, compara depois.

```python
novos = depois - bloq_antes
if novos: abortar()          # só respondo pelo que EU mudo
if depois: avisar(...)        # pré-existentes: recontados e exibidos, nunca silenciados
```

Saída final:

```
⚠️  33 bloqueante(s) PRÉ-EXISTENTE(S) permanecem (AT-01 · AT-11). Fora do escopo.
✅ gravado · backup: …bak_20260911_003043
```

Este é um princípio que vale para todo o plano: **um script responde pelo delta que introduz, não pelo passivo que herdou** — desde que o passivo continue visível a cada execução.

---

# 5. O que sobrou — a fila real do AT-02

| Categoria | Qtd | Natureza |
|---|---|---|
| **PROSA divergente** | 55 | A Canônica foi editada após a extração. Exige leitura humana |
| **ROTULO não recuperado** | 18 | Divergem cedo demais; recuperar seria trocar de frase |
| **SELO não recuperado** | 1 | idem |

**74 casos para inspeção**, inventariados em `canonico/reancoragem_b1.json` com `id_vinculo`, categoria, `chars_casados/total` e o ponto exato da divergência.

Detalhe dos 55 PROSA: muitos divergem só no caractere final (`casa 373/374 · diverge «.»`). São quase certamente reparáveis, mas com uma regra diferente — a frase da Canônica termina com selo *após* o ponto, e o corte da frase precisa considerar isso. Não forcei: prefiro uma segunda passada com regra própria a alargar a guarda e arriscar trocas.

---

# 6. Estado da fila

| # | Item | Estado |
|---|---|---|
| 1 | `validar_roundtrip.py` corrigido | ✅ |
| 2 | `contrato.py` v1.0.0 | ✅ |
| 3 | Blindar 3 escritores | 🔴 **bloqueado — arquivos não estão aqui** |
| — | **AT-02 reancoragem (antecipado)** | ✅ **40% → 71%** |
| 4 | `checklist_entrega_v2.py` nas 16 | ⏳ depende das outras bibliotecas |
| 5 | AT-01 — reauditar os 30 | ⏳ |
| 6 | AT-11 — `tier_2_intervencao` | ⏳ **decisão do outro agente** |

**Próximo passo que eu consigo fazer sozinho:** a segunda passada nos 55 PROSA, com regra de fronteira de selo. Ganho estimado: até 71% → ~92%.

Quer que eu siga por aí, ou prefere que eu pare a correção e volte ao objetivo maior — provar o pipeline ponta a ponta em B1 (biblioteca → narrativa → JSONs → motor)?
