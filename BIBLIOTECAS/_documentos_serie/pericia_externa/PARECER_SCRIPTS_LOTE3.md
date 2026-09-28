# PARECER — Scripts de resgate/v2, lote 3 de 5
**Encontrei a arma do crime.** 10/09/2026

---

# 1. Quadro de veredito

| # | Script | Veredito |
|---|---|---|
| 1 | `add_7_refs_rodada4` | 🟠 **Arriscado** — grava JSON antes de poder falhar |
| 2 | `add_pmids_b1v2` | 🟠 **Funciona, mas fabrica campo** |
| 3 | `aplica_correcoes_fidelidade` | 🔴 **O mais perigoso do conjunto** |
| 4 | `add_vinculos_b1v2` | 🔴🔴 **É ESTE. Criou os 30 vínculos defeituosos** |
| 5 | `conta_selos.sh` | 🟢 **Bom** — e resolve a ação urgente do lote 1 |

---

# 2. 🔴🔴 CASO ENCERRADO: o script 4 é a origem do lote v2

Não é mais hipótese. O código diz, literalmente:

```python
tc = "tier_3_correlacional_mecanistico"
t4 = "tier_4_descritivo_estrutural"
ti = "tier_2_intervencao"

def V(rot, secao, ancora, verif, role, forca):
    d.append({
      "claim_id": "",                    # ← vazio POR DESENHO
      "natureza_relacao": forca,         # ← recebe o MESMO argumento
      "forca_causal": forca,             # ← que forca_causal
      "g2_motivo": "",                   # ← vazio POR DESENHO
      "g3_notas": "",                    # ← vazio POR DESENHO
      "uso": "B1_v2",                    # ← rótulo de lote no campo errado
    })
```

Confere com os dados, campo a campo:

| Achado do laudo | Linha do script |
|---|---|
| `natureza_relacao == forca_causal` em 30/30 | mesmo parâmetro `forca` nos dois |
| `claim_id` vazio em 30/30 | `"claim_id": ""` literal |
| `g2_motivo`/`g3_notas` vazios em 30/30 | `""` literais |
| `tier_2_intervencao` (termo inexistente) | `ti = "tier_2_intervencao"` declarado no script |
| `uso = "B1_v2"` | `"uso": "B1_v2"` literal |
| IDs `VINC_B1V2_0179–0208` | `f"VINC_B1V2_{len(d)+1:04d}"` |

**Retratação necessária.** Meu `LAUDO_LOTE_V2.md` concluiu "assinatura de schema diferente — segundo agente com dialeto próprio". **Estava errado.** Não houve segundo agente nem dialeto: houve **um script que preenche `natureza_relacao` com o valor de `forca_causal` porque a função tem um parâmetro só para os dois campos**. Vou corrigir o laudo.

E isso explica o `VINC_B1_0030` correto no meio da rodada: ele **não passou por este script**.

## Mais três bugs no mesmo script

**(a) A deduplicação não funciona.** `existe` é calculado uma vez e nunca atualizado:

```python
existe = {v.get("id_referencia_interna") for v in d}
def V(rot, ...):
    if f"REF_{rot}" in existe: return     # 'existe' nunca recebe o novo
    d.append(...)
```

Testei: chamar `V("B")` três vezes insere **três** vínculos. Rodar o script duas vezes duplica os 30. *(Hoje o arquivo está limpo — 0 IDs duplicados — então rodou uma vez só.)*

**(b) Ternário morto:** `"g2_elegibilidade": ("eligible" if True else "")`. Sempre `eligible`. **Isto é grave**: o script declara elegibilidade G2 por padrão, sem avaliação. O G2 dos 30 é ficção.

**(c) `id_vinculo` por `len(d)+1`** — depende do tamanho atual do arquivo. Concorrência ou ordem diferente gera colisão.

**(d) `status_auditoria: "G1_G2_G3_B1v2"`** — não é valor de enum, é rótulo de rodada. Nos dados hoje aparece `CONFIRMADO`/`PARCIALMENTE_CONFIRMADO`, então **algum script posterior sobrescreveu** — provavelmente o `aplica_vereditos` do lote 2.

---

# 3. 🔴 Script 3 — o mais perigoso, e o motivo não é técnico

Ele reescreve **afirmações científicas** por `str.replace`, e a guarda é só um aviso:

```python
def troca(velho, novo, esperado=1):
    n = t.count(velho)
    if n != esperado:
        print(f"  [!] {esperado} esperado, {n} achado")   # avisa
    t = t.replace(velho, novo)                            # e troca assim mesmo
```

Se o texto não casar, imprime `[!]` e **continua**. Se casar 3 vezes, troca as 3. Sem `exit`, sem backup, sem diff.

O conteúdo das trocas é o que preocupa:

- `(Menard et al., 2017)` → `(Li et al., 2017)` — **troca de autoria de um claim**
- `(Sacta et al., 2018)` → `(Shirakawa et al., 2018)` — idem
- `(meta-análise de quimiocinas — a verificar)` → `(Köhler et al., 2017)[MA; humano] [VERIFICADO]` — **promove um pendente a VERIFICADO por substituição de texto**

A última é a mais séria: o selo `[VERIFICADO]` passa a existir na prosa **sem que nenhum vínculo tenha sido auditado**. É exatamente o tipo de operação que a sua regra "proibido inventar dado para passar" veda.

Um comentário do próprio script admite o improviso: *"S100B-ECT específico não existe"* — e mesmo assim substitui a frase por outra, com outra referência e selo `[VERIFICADO]`.

> **Trocar autoria de claim não pode ser feito por `replace` cego.** Tem que ser: localizar → mostrar o antes/depois → exigir confirmação → registrar no ledger. Cada uma dessas trocas deveria ser uma entrada de auditoria, não uma linha de script.

---

# 4. 🟠 Scripts 1 e 2 — metadados fabricados

Os dois inserem registros no `01_pmids.json` com PMIDs reais (bom) mas com campos preenchidos por decisão do script:

```python
"citacao_confirmada": True,          # afirmado, não verificado
"g1_metodo": "eutils_automatico",    # mas nada foi buscado aqui
"status_auditoria": "VALIDADO_G3_IA (resgate Rodada 4)",
"doi": "",                           # vazio, embora o efetch traga DOI
```

`g1_metodo: "eutils_automatico"` é **falso**: os dados foram digitados na lista `novos`/`rows`, não vieram de eutils. O script 1 do lote 2 (`03_efetch_abstracts`) é que faz eutils de verdade — e grava o mesmo rótulo. Depois disso, é impossível distinguir o que veio da ferramenta do que veio da mão.

No script 2 há ainda:

```python
"achado_central_molecular": tit[:120],   # o título truncado vira o "achado"
"autores": [aut],                        # só o primeiro autor
```

O achado central não é o título. Isso enche um campo semântico com outra coisa — mesma classe de erro do `uso: "B1_v2"`.

**Script 1, risco adicional:** grava o `01_pmids.json` e **só depois** mexe nas listras, onde há `assert i>=0, sec`. Se a seção não existir, o processo morre **com o JSON já gravado e o `.md` intacto** — estado inconsistente, sem rollback.

---

# 5. 🟢 Script 5 — o único sem ressalvas

```bash
f=$(ls "$DIR"/Biblioteca_*_CANONICA.md | sort -t_ -k2 -V | tail -1)
```

Caminho relativo, escolhe a versão mais nova, `grep -F -c` (literal, correto para strings com `[]`), só lê. **Bom.**

E é a ferramenta da ação urgente do lote 1: rode-o nas 16 e compare `[VERIFICADO]` com o número de vínculos `verificado`. Onde a prosa tiver mais selos que vínculos, houve duplicação.

Duas melhorias: acrescentar a contagem de duplicados (`grep -c '\[VERIFICADO\] \[VERIFICADO\]'`) e `[PENDENTE_VERIF]`, que o script 3 cria e este não conta.

---

# 6. O padrão dos três lotes, agora claro

Quinze scripts vistos. O defeito é sempre o mesmo:

> **Scripts que escrevem em artefato canônico gravam o que lhes mandam, sem validar contra nada.**

| Lote | Script | O que gravou sem validar |
|---|---|---|
| 1 | propagador de selos | selo duplicado, +109 por execução |
| 2 | `aplica_vereditos` | `g2_motivo`/`g3_notas` vazios |
| 3 | **`add_vinculos_b1v2`** | **`natureza_relacao` = `forca_causal`, `claim_id` vazio, G2 fictício** |
| 3 | `aplica_correcoes` | autoria trocada, `[VERIFICADO]` sem auditoria |

Nenhum deles é incompetente isoladamente. Somados, produzem um acervo onde não se sabe qual campo foi auditado e qual foi preenchido por um valor-padrão de função.

**A causa comum: cada script tem seu próprio conceito do que é um vínculo válido.** É exatamente o que o `SCHEMA_VINCULO_v1.json` elimina — se os quatro tivessem importado o schema e validado antes de gravar, **nenhum dos quatro defeitos teria entrado**.

---

# 7. Ações revisadas

| # | Ação | Mudança |
|---|---|---|
| 1 | ~~Procurar os `vereditos_*.json`~~ | ❌ **cancelada.** O defeito não está no veredito, está no script 4. Não perca tempo |
| 2 | **Os 30 exigem reauditoria de verdade** | 🔴 `claim_id`, `natureza_relacao`, `g2_motivo`, `g3_notas` nunca foram avaliados — nasceram vazios ou copiados |
| 3 | Rodar o script 5 nas 16 | 🔴 fecha o mapa de dano dos selos |
| 4 | Congelar os scripts 3 e 4 | 🔴 não rodar de novo em nenhuma biblioteca |
| 5 | Verificar se o script 4 rodou em B2–B16 | 🔴 procurar `uso: "B1_v2"` ou IDs `VINC_*V2_*` nas outras |
| 6 | Corrigir a IMPL-45 | 🟠 escopo confirmado: reauditar, não remapear |

**A ação 5 é a que mais me preocupa.** Se o padrão `add_vinculos_bXv2` foi replicado nas outras 15 bibliotecas, existem mais lotes com `natureza_relacao == forca_causal`. Um comando resolve:

```bash
grep -l '"natureza_relacao": "tier_' */Evidencias/Vinculos/*.json
```

---

# 8. Retratação registrada

Meu `LAUDO_LOTE_V2.md` afirmou: *"prova do segundo agente com dialeto próprio"*. **Falso.** A causa é uma função com um parâmetro servindo dois campos. Vou emendar o laudo com esta correção — o diagnóstico errado levaria a cobrar disciplina de um agente, quando o conserto é de cinco linhas de código.

O que **permanece válido** do laudo: a auditoria científica dos 30 foi de fato superior (27% de full-text), os trechos são literais, os PMIDs conferem, e os resultados negativos foram preservados. **O conteúdo é bom; o transporte é que corrompeu.**

Mande os próximos 5.
