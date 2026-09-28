# PARECER — Scripts de geração/normalização, lote 1 de 5
**Perícia por execução, não por leitura.** 10/09/2026

---

# 1. Quadro de veredito

| # | Script | O que faz | Veredito |
|---|---|---|---|
| 1 | `normaliza_markdown` | Repõe `#` em títulos | 🟡 **Usável**, com 3 ressalvas |
| 2 | `helper_local` (paths relativos) | Acha pasta do mecanismo | 🟢 **Bom** — o melhor dos cinco |
| 3 | `propaga_selos` (v1) | Conta selos | 🔴 **CÓDIGO MORTO — deletar** |
| 4 | `propaga_selos` (v2) | Insere selos | 🔴 **Quebrado e perigoso — deletar** |
| 5 | `propaga_selos` (v3) | Insere selos | 🔴 **NÃO IDEMPOTENTE — corromper arquivo** |

**Coerência entre eles: 🔴 ruim.** Três scripts (3, 4, 5) são tentativas sucessivas do mesmo problema. Nenhum foi apagado. Não há como saber, olhando a pasta, qual é o vigente — exatamente a patologia que gerou o lote v2.

---

# 2. 🔴 O achado grave: o script 5 destrói a Canônica

Não deduzi — **rodei três vezes contra a B1 real**:

```
selos [VERIFICADO] antes ......  72
rodada 1 ....... total 288  | inserções: 109
rodada 2 ....... total 397  | inserções: 109   ← deveria ser 0
rodada 3 ....... total 506  | inserções: 109   ← deveria ser 0

ocorrências de "[VERIFICADO] [VERIFICADO]" no arquivo: 106
```

**Cada execução acrescenta 109 selos, para sempre.** O arquivo cresce e apodrece a cada rodada.

## A causa exata

O script tem uma guarda anti-duplicação. Ela não funciona:

```python
end = pos + len(cit)
if SELO_RE.match(t[end:end+30]): continue
```

Depois de inserir, o texto fica `...[OB] [VERIFICADO].` — com **um espaço** antes do selo. Mas a inserção é feita com `t[:end] + " " + s`, e a verificação usa `.match()`, que ancora no **caractere 0**. O caractere 0 é o espaço, não o `[`. Provei isolado:

```
t = "Frase (Banks, 2005)[OB] [VERIFICADO]. fim"
SELO_RE.match(t[end:end+30])  ->  False
fatia examinada: ' [VERIFICADO]. fim'   ← o espaço mata o match
```

**Correção de uma linha:**

```python
if SELO_RE.match(t[end:end+30].lstrip()): continue
```

Ou, melhor, inserir sem espaço à esquerda e casar com `search` numa janela curta.

## Consequência prática

Se este script rodou mais de uma vez em alguma das 16 bibliotecas, **aquela Canônica tem selos duplicados**. E selo duplicado não é cosmético: o `trecho_ancora` do vínculo deixa de casar literalmente com o corpo — quebra a rastreabilidade que o `validar_roundtrip.py` verifica.

> **Ação imediata sugerida:** rodar `grep -c '\[VERIFICADO\] \[VERIFICADO\]'` nas 16. Onde der >0, restaurar do backup.

---

# 3. 🔴 Script 3 — nunca escreveu nada

O laço inteiro termina em:

```python
inseridos += 1
```

Incrementa um contador e segue. **Não há `doc.write_text` no arquivo.** Todo o cálculo de `idx`, `end`, `fim[-60:]` é descartado. Ele imprime "selos a aplicar: N" e sai.

O risco não é o script — é o relatório dele. Alguém lê *"selos a aplicar: 109"* e conclui que foram aplicados. **Foram zero.**

---

# 4. 🔴 Script 4 — incoerente consigo mesmo

Faz duas passagens que se contradizem:

1. Calcula posições sobre `t_norm` (texto normalizado, sem `**`) e guarda em `v["_ins"]`.
2. Monta a lista `ins = sorted(...)` — **e nunca a usa.**
3. Depois refaz tudo com `t2.find(cit)` no texto original.

Os offsets da passagem 1 são inúteis: posição em texto normalizado não corresponde a posição no original. O próprio comentário admite a confusão (*"mapear de volta eh complexo; em vez disso..."*). Além disso, **muta o dicionário de entrada** (`v["_ins"] = ...`) — se alguém salvar `vinc` depois, grava lixo no JSON de vínculos.

Tem a mesma falha de idempotência do script 5, pelo mesmo motivo.

---

# 5. 🟡 Script 1 — usável, com ressalvas

**Testei a idempotência: passa.** Rodadas 2 e 3 são estáveis, o `re.sub` de `---` duplicado segura. E confirmei que na B1 atual há **zero** linhas `BLOCO` sem `#` — ele não teria o que fazer, o que é bom sinal.

Três ressalvas:

| # | Problema | Correção |
|---|---|---|
| R1 | **Backup sobrescreve no mesmo dia.** `f.with_suffix(f".bak_{hoje}.md")` — rodar duas vezes no mesmo dia perde o backup original, que é justamente quando você mais precisa dele | acrescentar `%H%M%S`, ou não sobrescrever se existir |
| R2 | **Hard-code do mecanismo.** A regra 5 é `^B1\s*[—-]\s*NEUROINFLAMA` — só funciona na B1. Nas outras 15 o título principal não vira `#` | derivar do nome da pasta, como faz o script 2 |
| R3 | **Silencioso demais.** Reescreve o arquivo sempre, mesmo sem mudança | só gravar se `t2 != t`, e reportar quantas linhas mudaram |

O relatório final também engana um pouco: `sem_hash_bloco` conta `^BLOCO`, mas depois da correção esses viraram `## BLOCO`, então o número **sempre** dá 0 — não prova nada.

---

# 6. 🟢 Script 2 — este é o padrão a seguir

É o único bem projetado do lote:

- **Zero hard-code** — sobe a árvore procurando `Evidencias/`
- Funciona em qualquer profundidade e se o workspace mudar de lugar
- Escolhe o canônico por **maior `_vN`**, não por nome fixo
- Tem `if __name__ == "__main__"` para inspeção sem efeito colateral

Duas melhorias pequenas:

- `versao()` devolve 0 quando não há `_vN`. Se dois arquivos não tiverem versão, `sorted` escolhe por ordem instável — desempatar por `mtime`.
- `MEC_PREFIXO = MEC_DIR.name.split("_")[0]` é calculado e nunca usado.

> **Recomendação:** os outros scripts deveriam importar este em vez de repetir descoberta de caminho. É o antídoto contra o problema `/home/user/Ferramentas de geração e auditoria/` hard-coded que apontei no `checklist_entrega.py`.

---

# 7. O padrão que os cinco revelam

Não é falta de competência — é **falta de contrato**, a mesma raiz do lote v2:

| Sintoma | Evidência no lote |
|---|---|
| **Versões sucessivas convivendo** | 3 scripts para o mesmo trabalho, nenhum apagado |
| **Nenhum é idempotente por desenho** | 4 e 5 corrompem se rodarem 2× |
| **Nenhum tem teste** | o bug do `.match()` some com 3 linhas de teste |
| **Nenhum declara pré/pós-condição** | o script 3 "reporta" trabalho que não fez |
| **Nenhum grava log do que alterou** | impossível saber se rodou, e quantas vezes |

Um script que **escreve** na Canônica é mais perigoso que um checklist errado: o checklist erra o veredito, o script erra o dado.

## Regra que sugiro adotar para todo script que escreve

1. **Idempotente** — rodar N vezes = rodar 1 vez. Testado, não presumido.
2. **Dry-run por padrão** — só altera com `--apply`.
3. **Diff no stdout** — o que vai mudar, antes de mudar.
4. **Log em JSON** — arquivo, sha256 antes/depois, contagem por tipo.
5. **Um script por trabalho** — versão antiga vai para `_deprecated/`.

O item 2 sozinho teria evitado o dano do script 5.

---

# 8. Ações

| # | Ação | Urgência |
|---|---|---|
| 1 | `grep -c '\[VERIFICADO\] \[VERIFICADO\]'` nas 16 Canônicas | 🔴 **agora** |
| 2 | Onde >0: restaurar backup ou desduplicar com regex | 🔴 |
| 3 | Deletar scripts 3 e 4 (ou mover para `_deprecated/`) | 🟠 |
| 4 | Corrigir o `.lstrip()` no script 5 e adicionar `--apply` | 🟠 |
| 5 | Generalizar script 1 (R1, R2, R3) | 🟡 |
| 6 | Fazer os demais importarem o script 2 | 🟡 |
| 7 | Acrescentar ao `checklist_entrega`: item "sem selo duplicado na prosa" | 🟡 |

O item 7 vale destacar: **o defeito do script 5 é detectável automaticamente.** Já sei o regex. Quando você mandar o próximo lote eu acrescento.

---

# 9. Mande os próximos 5

Este lote respondeu à sua pergunta — **não, não foram coerentes**. Mas o problema é sistêmico, não pontual, e vale ver os 10 antes de eu propor a reorganização da pasta de ferramentas.

Um pedido: se souber **quais desses rodaram nas 16 bibliotecas e quantas vezes**, me diga. Muda a ação 1 de precaução para reparo dirigido.
