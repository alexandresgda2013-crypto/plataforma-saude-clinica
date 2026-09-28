# PARECER — Geradores de prosa e checadores, lote 4 de 5
**20 scripts periciados até aqui.** 10/09/2026

---

# 1. Quadro de veredito

| # | Script | Veredito |
|---|---|---|
| 1 | `insere_subsecoes_v2` | 🟠 **Prosa boa, mecânica frágil** |
| 2 | `atualiza_cabecalho_v2` | 🟠 Mesmo padrão, um risco a mais |
| 3 | `check_fidelidade_b1` | 🟡 **O melhor checador do acervo** — com 3 furos |
| 4 | `check_fidelidade_canonica` | 🔴 **Aprova por não enxergar** |
| 5 | `check_gpm_completo` | 🟢 **Simples e correto** |

---

# 2. 🔴 Inversão importante: o lote v2 tem os MELHORES trechos-âncora

Testei literalidade normalizada dos 257 vínculos contra o corpo da Canônica:

```
lote v2 (script 4 do lote 3) ... 28/30 literais = 93%
resto (227) .................... 75/227 literais = 33%
```

**Os 30 vínculos que eu chamei de defeituosos têm o melhor casamento de trecho do acervo.** E a razão está no script 1 deste lote: a prosa e os vínculos foram escritos **na mesma rodada, um a partir do outro**. O texto que ele insere (`### 2.25`, `### 2.26`, `### 2.27`, `### 3.16`, `### 6.6`, `### 6.7`) contém exatamente as frases que viraram `trecho_ancora`.

Isso reforça e refina o adendo do laudo:

> **A rodada v2 produziu conteúdo científico e textual superior. O que falhou foi só a função `V()`, que preenche dois campos com um parâmetro.** Cinco linhas de código estragaram um trabalho que, no restante, é o melhor do acervo.

E acende um alerta sobre os **227**: apenas 33% de literalidade é ruim, e a causa mais provável é o `limp_pmid()` do script 3 do lote 2, que altera o `trecho_ancora` **depois** de extraído. Aquela suspeita agora tem número.

---

# 3. 🔴 Script 4 — o pior tipo de checador: o que aprova por cegueira

O regex de citação está errado:

```python
r'\(([A-ZÀ-Ú][A-Za-zÀ-ÿ\-]+)(?:,| et al)?,\s*((?:19|20)\d{2})\)\s*\[(ML|EC|OB|MA|AT)\]'
```

Exige `(Autor et al, 2020)` — mas a convenção real é `(Autor et al., 2020)`, **com ponto**. `(?:,| et al)?` não cobre `et al.`. Medi contra a B1:

| Regex | Citações encontradas |
|---|---|
| Script 4 | **7** |
| Script 3 | 267 |
| Real no documento | 270 |

**Ele verifica 2,6% das citações e reporta "Toda citação em prosa tem correspondência no Módulo 09".** Um checador que enxerga 7 de 270 e diz OK é pior que não ter checador: produz confiança falsa.

## Mais três defeitos

**(a) Extração de âncoras do GPM é lixo estatístico:**

```python
pats = re.findall(r'([A-ZÀ-Ú][A-Za-zÀ-ÿ\-]+)[^.]{0,6}?((?:19|20)\d{2})', gpm)
```

Testei num texto trivial: extraiu `('IL-', '2015')` e `('Modelo', '2020')` como se fossem autores. A "taxa de cobertura de âncoras" que ele imprime não mede nada.

**(b) Ordena por versão antes de filtrar canônicas** — se houver um `.md` sem `vN` na pasta, `int((re.search(...) or [0])[1])` estoura com `TypeError` sobre um arquivo que nem seria avaliado.

**(c) `if len(sys.argv)>3` para ler `sys.argv[2]`** — o GPM passado como 2º argumento **nunca é lido**, porque a condição pede 3 argumentos. Bug clássico de off-by-one: o docstring promete `[caminho_gpm.md]` e o código ignora.

**(d) `vias_gpm` é calculado e nunca usado.** O item 2/4 do docstring ("cobertura de vias") não existe no código.

---

# 4. 🟡 Script 3 — o melhor checador, e onde ele falha

Acertos reais, que faltam nos outros:

- Regex de citação **correto** (267/270)
- Detecta **órfãs nos dois sentidos** — registro sem listra e listra sem registro
- **Integridade referencial** vínculos ↔ Módulo 09
- Trata seções legitimamente sem referência (`Nota de escopo`, `Inventário NEGATIVO`) sem reprovar
- Detector de **título em inglês na prosa** — engenhoso, e é o que pegaria os 11 rótulos defasados da IMPL-46

Três furos:

| # | Problema |
|---|---|
| F1 | **Não valida enum de campo nenhum.** Confere que o vínculo existe, nunca o que há dentro. Passaria nos 30 do v2 — mesmo furo dos checklists em prosa |
| F2 | **Laço O(n³):** para cada rótulo de listra, relê **todos** os JSONs do disco. Com 237 refs e ~500 listras são milhares de leituras. E o resultado (`arq`, `esperado`) é calculado e **descartado** — a checagem de coerência de tag foi escrita pela metade |
| F3 | `BIB`/`BASE` indefinidos se não houver argumento → `NameError` no `print` da linha seguinte, antes da mensagem de ajuda |

Corrigido F1, este vira o checador oficial. É o único com a estrutura certa.

---

# 5. 🟠 Scripts 1 e 2 — a prosa é boa, a mecânica não

O conteúdo científico inserido é de qualidade: distingue causal em animal de emergente em humano, marca `[PRÉ-CLÍNICO]`/`[EXTRAPOLADO]` corretamente, e a subseção 6.6 preserva o **contra-padrão** do TEPT com supressão neuroimune — resultado negativo, difícil de manter, e ele manteve.

Mas:

**(a) `assert` como controle de fluxo.** `assert ancora in t, f"âncora não achada"` — com `python3 -O` os asserts somem e o script grava sem verificar nada.

**(b) Ancoragem em títulos literais.** `inserir_antes("### 2.24 — Proteínas S100 como DAMPs", ...)`. Se o título mudar uma vírgula, quebra. Pior: o script 1 do lote 1 (`normaliza_markdown`) **reescreve títulos** — os dois brigam pelo mesmo texto.

**(c) Não é idempotente.** Rodar duas vezes insere as subseções duas vezes. Nenhum dos dois verifica se `### 2.25` já existe.

**(d) Script 1 lê de `_historico/versoes/` e escreve na canônica ativa.** Reconstrói a v2 a partir de uma v1 congelada — qualquer correção feita na canônica **entre** a v1 e a execução é silenciosamente descartada. Este é o mecanismo clássico de perda de trabalho.

**(e) Script 2 grava selos `[VERIFICADO]` dentro do texto inserido** (ex.: `(Lee et al., 2025)[OB/ML] [VERIFICADO]`). Selo é saída de auditoria, não de geração — mesma inversão do script 3 do lote 3. E `[OB/ML]` é tag composta, que nenhum dos checadores reconhece.

---

# 6. 🟢 Script 5 — correto

Faz uma coisa, faz certo, sai com código apropriado. `re.findall(r'^##\s+MÓDULO\s+(\d{2})\b', t, re.M)`, compara com 00–10, reprova com a lista do que falta.

Só uma incoerência: calcula `ultima = linhas[-1]` para detectar truncamento e **nunca usa**. Ou implemente (verificar se o Módulo 10 tem conteúdo depois do título), ou remova.

---

# 7. Síntese dos 20 scripts

| Categoria | Qtd | Situação |
|---|---|---|
| **Escrevem em canônico sem validar** | 8 | 🔴 causa de todos os defeitos achados |
| **Checam** | 4 | 🟡 nenhum valida enum; um enxerga 2,6% |
| **Só leem / utilitários** | 5 | 🟢 sem problema |
| **Mortos ou redundantes** | 3 | ⚪ deletar |

**O desequilíbrio é a doença:** 8 escritores contra 4 checadores, e nenhum dos 8 chama nenhum dos 4. Escrita e verificação são universos separados — por isso o defeito v2 sobreviveu 6 dias.

A correção é estrutural e é uma linha por script:

```python
from validar_vinculo import validar   # importa o SCHEMA_VINCULO_v1.json
erros = validar(registros)
if erros: sys.exit(f'ABORTADO: {erros}')
```

Um módulo `validar_vinculo.py`, importado pelos 8. Quem escreve, valida — antes de gravar.

---

# 8. Ações consolidadas

| # | Ação | Urgência |
|---|---|---|
| 1 | Investigar os **227 com 33% de literalidade** — provável dano do `limp_pmid()` | 🔴 **novo, e maior que os 30** |
| 2 | Aposentar o script 4 deste lote (checador cego) | 🔴 |
| 3 | Promover o script 3 a checador oficial + validação de enum | 🟠 |
| 4 | Criar `validar_vinculo.py` e importá-lo nos 8 escritores | 🟠 |
| 5 | Tornar 1 e 2 idempotentes; trocar `assert` por `sys.exit` | 🟠 |
| 6 | Rodar o `conta_selos.sh` (lote 3) nas 16 | 🟠 pendente desde o lote 1 |

**A ação 1 mudou de prioridade.** Se 152 dos 227 vínculos não casam literalmente, o problema é 5× maior que os 30 do lote v2 — e é o alicerce da rastreabilidade que a plataforma inteira pressupõe.

---

# 9. Nota sobre o que isto revela do método

Vale registrar: **o conteúdo científico deste projeto é consistentemente bom.** A subseção 2.25 sobre imunometabolismo, o contra-padrão do TEPT, a tabela de confundidores com o genótipo rs6971 no TSPO-PET — isso é trabalho de qualidade, e apareceu em todos os lotes.

O que falha é sempre a mesma coisa, e nunca é a ciência: **é a camada de transporte.** Scripts que gravam sem validar, âncoras de texto frágeis, checadores com regex quebrado. A boa notícia é que essa camada é a mais fácil de consertar — schema, validação na escrita e um checador que enxergue.

Mande os últimos 5.
