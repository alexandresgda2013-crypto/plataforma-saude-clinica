# PARECER — Correções pós-auditoria, lote 5
**24 scripts periciados.** 10/09/2026

---

# 1. Quadro de veredito

| # | Script | Veredito |
|---|---|---|
| 1 | `check_troca_de_nome` | 🟢 **Excelente** — o melhor detector do acervo |
| 2 | `checklist_entrega.py` | ⏭️ **Já periciado** (v1). Ver `PARECER_CHECKLIST_ENTREGA.md` |
| 3 | `correcoes_finais` | 🟠 Boa intenção, mecânica insegura |
| 4 | `resolve_parenteses` | 🔴🔴 **PERIGOSO — troca autoria com zero evidência** |
| 5 | `correcoes_g3_b1v2` | 🟢 **O melhor script de escrita do acervo** |

---

# 2. 🔴🔴 Script 4 — pode trocar autoria com Jaccard ZERO

O casamento por similaridade tem um bônus que quebra o limiar:

```python
sc = len(ct & r["tok"]) / max(1, len(ct | r["tok"]))
if r["ano"] == ano: sc += 0.3
...
if best and bs >= 0.30:
    novo = f"({r['sob']} et al., {r['ano']}){tag}"   # REESCREVE A AUTORIA
```

Testei o pior caso:

```
jaccard puro (nenhuma palavra em comum) = 0.00
        + bônus de ano                  = 0.30
passa no limiar >= 0.30?                  True
```

> **Um título sem uma única palavra em comum com a referência, mas do mesmo ano, tem a autoria reescrita.** Basta a subseção ter uma referência daquele ano na listra.

E o limiar de 0.30 já é baixo por si: entre conjuntos de ~8 tokens, são ~4 palavras em comum. `inflammation`, `depression`, `brain`, `microglia` casam com dezenas de referências do corpus. Num acervo temático, onde quase tudo fala de neuroinflamação, isso é ruído puro.

O script **grava direto**, sem dry-run, sem diff, sem confirmação. E o comentário do cabeçalho diz *"Não inventa: sem casamento → marca [PENDENTE_VERIF]"* — a intenção é correta, a implementação não a cumpre.

**Correção mínima:** exigir jaccard **puro** ≥ 0.30 antes de qualquer bônus, e nunca deixar o bônus sozinho cruzar o limiar:

```python
jac = len(ct & r["tok"]) / max(1, len(ct | r["tok"]))
if jac < 0.30: continue           # piso duro
sc = jac + (0.3 if r["ano"] == ano else 0)
```

Mais `--apply` e diff obrigatório. **Enquanto isso, não rodar em nenhuma biblioteca.**

Um ponto positivo, registrado: o teste PT×EN funciona. Título em português contra registro em inglês dá jaccard ~0 e vira `[PENDENTE_VERIF]` — o comportamento honesto, e é o que impede o script de ser catastrófico em vez de só perigoso.

---

# 3. 🟢 Script 1 — o melhor detector do acervo, e não escreve nada

Este resolve um problema que nenhum outro script tenta: **verificar se o autor citado na frase corresponde à referência listada naquela subseção**. É a checagem que pegou as trocas Menard→Li e Sacta→Shirakawa.

O desenho está certo em três pontos:

- **Escopo por subseção** — compara a citação com a listra *daquela* seção, não com o banco inteiro. Precisão muito maior
- **Distingue dois erros diferentes**: "mesmo autor, ano diferente" (provável data online) de "autor ausente da listra" (provável troca). São diagnósticos distintos e ele não os mistura
- **Só lê.** Não tem `write_text`. Reporta e deixa a decisão com quem lê

Isso é exatamente o que eu recomendei nos pareceres anteriores, e alguém já tinha feito. **Promova-o a portão obrigatório.**

Duas ressalvas menores: o `sys.path.insert` para importar `_local_path` é frágil se o script mudar de pasta (o argumento explícito resolve, e ele suporta); e o `key=lambda` da ordenação por versão repete o padrão que estoura em arquivos sem `vN` — aqui está protegido por um `if`, corretamente.

---

# 4. 🟢 Script 5 — este é o padrão que os outros deveriam seguir

Por três motivos:

**(a) `assert c == 1` aborta antes de gravar.** Diferente da função `sub()` dos scripts 3 (deste lote e do lote 3), que avisa `[!]` e substitui assim mesmo. Testei: com 2 ocorrências ele levanta e o arquivo não é tocado.

**(b) As correções são no sentido certo — enfraquecem afirmações.** Todas as trocas ajustam a prosa para o que o abstract realmente diz:

| Antes | Depois |
|---|---|
| "Citocinas modulam circuitos da amígdala [VERIFICADO]" | "Em camundongo, IL-17A/IL-17C… [PRÉ-CLÍNICO]" |
| "meta-análises mostram associação" | "heterogênea, efeito pequeno, Hedge's g≈0,4" |
| TOC entre os confirmados | "**não diferiram significativamente** — achado nulo relevante" |
| "minociclina em humanos" | "em voluntários **saudáveis**, não em pacientes" |
| Wittenberg "em ansiedade" | "sintomas **depressivos**, não específica de ansiedade" |

Isto é o oposto do script 3 do lote 3, que promovia pendentes a `[VERIFICADO]`. Aqui um `[VERIFICADO]` humano vira `[PRÉ-CLÍNICO]` em camundongo. **Correção que reduz o alcance da alegação é sinal de auditoria honesta.**

**(c) Corrige o JSON junto com a prosa** — reclassifica o itaconato de `human_clinical` para `preclinical_mechanistic`. Mantém os dois níveis coerentes, coisa que quase nenhum outro faz.

Uma ressalva: também não faz backup, e o `assert` some com `python3 -O`.

---

# 5. 🟠 Script 3 — o problema é a função `sub()`, de novo

```python
def sub(velho, novo, n=1, ok=True):
    c = t.count(velho)
    if c != n: log.append(f"[!] esperado {n}, achado {c}")
    t = t.replace(velho, novo)      # troca mesmo assim
```

Mesma falha do lote 3: registra a divergência e prossegue. O parâmetro `ok=True` é declarado e nunca usado.

O **conteúdo**, porém, é bom: as três primeiras correções fazem exatamente o que a sua regra manda — em vez de forçar um nome, marcam `[PENDENTE_VERIF]`. O comentário *"não achar nome à força"* é a conduta certa. E as 11 listras completadas resolvem a parte de "autor correto, listra incompleta".

Basta trocar `sub()` por versão que aborta:

```python
def sub(velho, novo, n=1):
    c = t.count(velho)
    if c != n:
        sys.exit(f'ABORTADO: esperado {n}, achado {c}: {velho[:70]}')
    return t.replace(velho, novo)
```

---

# 6. Observação sobre o conjunto: existe um bom padrão, mas ninguém o segue

Depois de 24 scripts, o achado é este:

**As boas práticas já existem no acervo — estão espalhadas, uma em cada script.**

| Prática | Onde já existe |
|---|---|
| Aborta antes de gravar | Script 5 deste lote (`assert c == 1`) |
| Só lê, reporta e não decide | Script 1 deste lote |
| Caminho relativo sem hard-code | Script 2 do lote 1 |
| Log de proveniência com data/hora | Script 1 do lote 2 |
| Regex de citação correto | Script 3 do lote 4 |
| Escopo por subseção | Script 1 deste lote |
| Corrige prosa e JSON juntos | Script 5 deste lote |

Nenhum script tem mais de duas delas. **Não falta conhecimento — falta um lugar comum onde essas práticas morem.** Um módulo importado por todos resolveria, e nenhuma das sete precisa ser inventada: é copiar de onde já funciona.

---

# 7. Sobre a multiplicação: o número agora tem significado

Você disse que ele gera mais scripts a cada pedido. Com 24 periciados, dá para medir o custo:

- **4 fazem a mesma coisa** (propagar selos: 3 do lote 1; resolver citações: script 4 deste lote)
- **2 checadores de fidelidade** concorrentes, um deles enxergando 2,6% das citações
- **2 versões** do `checklist_entrega.py` circulando (você me mandou a v1 duas vezes — sinal de que também não está claro qual é qual do seu lado)

O custo real não é o disco. É que **ninguém consegue dizer qual script produziu qual campo** — e foi por isso que precisei de três lotes de perícia para achar a função `V()` que causou o defeito v2.

Minha sugestão continua a mesma e é modesta: separar `ferramentas/` (vigentes, um por trabalho, quem escreve valida) de `_analises/` (descartáveis, só leem). Não precisa reescrever nada agora — basta mover.

---

# 8. Ações deste lote

| # | Ação | Urgência |
|---|---|---|
| 1 | **Não rodar o script 4** até o piso de jaccard puro | 🔴 |
| 2 | Verificar se ele já rodou: procurar autorias trocadas sem `[PENDENTE_VERIF]` | 🔴 |
| 3 | Promover o script 1 a portão obrigatório | 🟠 |
| 4 | Trocar `sub()` por versão que aborta (scripts 3 dos lotes 3 e 5) | 🟠 |
| 5 | Usar o script 5 como modelo dos escritores | 🟡 |

A **ação 2** é a que me preocupa. O script 1 deste lote é justamente a ferramenta para isso: ele detecta autor citado que não está na listra da subseção. **Rode-o antes de qualquer coisa** — ele responde se o script 4 deixou dano.

---

# 9. Continue mandando

Pode seguir com os próximos. Não estou acumulando cópias no workspace — os pareceres ficam, os scripts não. E o `checklist_entrega.py` repetido eu reconheci e pulei.

Se em algum momento quiser interromper a perícia e partir para a correção, diga: já tenho material suficiente para escrever o `validar_vinculo.py` compartilhado e a reorganização das duas pastas. Os lotes seguintes tendem a confirmar o mesmo padrão, não a mudá-lo.
