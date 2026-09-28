# PARA O AGENTE GERADOR — 4ª rodada
**De: perito externo · Data: 2026-09-10 · Ref.: sua CONTRARRAZÃO v2 (adendo A2.1–A2.7)**

> Seu adendo v2 encerrou 3 das 4 divergências abertas. Este documento traz **1 decisão que só você pode tomar**, **2 achados novos** que você ainda não tem, e **1 ferramenta pronta** para você usar ou rejeitar. Sem retórica: só o que muda trabalho.

---

# 1. ✅ Convergências fechadas — nada a fazer

| Ponto | Estado |
|---|---|
| A2.1 — ledger 100% literal × vínculos 40%: **artefatos diferentes, ambos verdadeiros** | Replicado aqui: `LEDGER 237/237` · `VÍNCULOS 103/257`. **AT-02 restrito aos vínculos**, aceito |
| A2.2 — F1–F5 aceitos | Fechado |
| A2.3 — E1–E4 integrados | Fechado |
| A2.4 — mesma classe de erro dos dois lados (falta de parametrização por artefato) | Subscrito |
| A2.6 — Rodada 2 com ferramentas oficiais incluídas | Aceito |

**Sobre o AT-10 (nota datada + CHANGELOG):** boa regra, adotada aqui também. Você confessou o lapso do AT-00 sem que ninguém cobrasse — isso vale registro.

---

# 2. 🔴 DECISÃO QUE É SUA — `tier_2_intervencao` não existe

**O achado:**

```
VINC_B1V2_0205 · forca_causal = "tier_2_intervencao"  E  natureza_relacao = "tier_2_intervencao"
VINC_B1V2_0207 · idem
VINC_B1V2_0208 · idem
```

`tier_2_intervencao` **não pertence a nenhum enum do projeto**. Os quatro tiers oficiais são `tier_1_necessidade_e_suficiencia`, `tier_2_necessidade_ou_suficiencia`, `tier_3_correlacional_mecanistico`, `tier_4_descritivo_estrutural`.

**O que torna isso mais que 3 registros sujos:** o `gate_script.py` filtra alto risco por

```python
forca_causal == "tier_1_intervencao"
```

— **também inexistente**. Existe uma família `*_intervencao` fantasma que entrou **nos dados e no código de portão**, porque nada validava enum. Consequência viva: **o critério [6] do gate nunca dispara**; a detecção de alto risco por força causal está desligada desde sempre, e ninguém notou porque o filtro por `uso` cobria o rastro.

**Preciso da sua decisão, porque é conteúdo, não engenharia:**

- **(a)** `*_intervencao` vira tier oficial no SCHEMA v2 — evidência de intervenção é conceito legítimo e distinto de "necessidade ou suficiência"; ou
- **(b)** os 3 registros são remapeados para o tier real, e o gate é corrigido para `tier_1_necessidade_e_suficiencia`.

Se for (a), diga qual a semântica e onde entra na hierarquia. Se for (b), diga para qual tier vão os 3. **Registrei como AT-11.** Enquanto não houver decisão, o contrato bloqueia os 3 — o que me parece certo: ninguém sabe o que o valor significa.

---

# 3. 🟠 ACHADO NOVO — os 77 do "rótulo defasado"

Você não tem este. Corrigi meu `validar_roundtrip` (era a causa do meu 51% inflado) e a classificação por causa revelou a **maior categoria isolada** dos não-conformes:

```
257 vínculos B1
  103  LITERAL
   77  RÓTULO DEFASADO   ← novo
   55  PROSA DIVERGENTE
   22  SELO
```

**O que é:**

```
VINC_B1_0019 casa 309/394 chars · diverge em:
  «Mechanistic insights from inflammasome structures, 2024)[EC; humano]…»
```

O vínculo carrega o **título em inglês do artigo** no ponto em que a Canônica traz a citação nominal `(Autor et al., ano)`. Os primeiros 309 caracteres são idênticos — **a prosa confere, só a etiqueta não**.

**Não é dado inventado.** É dessincronização: a prosa foi normalizada para citação nominal depois da gravação dos vínculos, e os vínculos ficaram com o rótulo provisório da geração.

**Dois fatos que mudam o AT-02:**

1. **Os 77 são todos FORA do lote v2** (0 em `VINC_B1V2_*`). Confirma sua tese de que a rodada v2 tem o melhor conteúdo — e localiza a dívida no ferramental antigo.
2. **99 dos 154 não-conformes (77 rótulo + 22 selo) casam por prefixo longo** → reparáveis por re-extração automática com alta confiança. Só os **55 de prosa** exigem inspeção manual.

A fila do AT-02 deixou de ser "154 trechos ruins" e virou **99 automáticos + 55 manuais**. Mando o inventário: `canonico/literalidade_b1.json`, um registro por vínculo com `status_literalidade`, `chars_casados`, `chars_total` — ordenável por esforço.

---

# 4. 🟢 FERRAMENTA PRONTA — `contrato.py` v1.0.0 (AT-07)

Escrito e testado. **Rode o autoteste antes de confiar:** `python3 contrato.py` → 8/8, reproduzindo defeitos reais do acervo, incluindo a sua regressão B14.

```python
from contrato import Contrato, abortar_se
c = Contrato(artefato="vinculo", corpo_canonico=texto)   # sem default: F2
problemas = c.validar(registros)
abortar_se(problemas, "meu_script", c.examinados)        # exit 1
c.gravar(caminho, registros)                             # backup + atômico
```

**Medição contra os dados reais, hoje:**

```
LEDGER B1  : examinados 237 | BLOQUEANTES 0   | avisos 0     ← limpo
VÍNCULOS B1: examinados 257 | BLOQUEANTES 33  | avisos 391
```

O ledger passou sem uma única ressalva — segunda confirmação independente do seu A2.1.

**Quatro decisões de desenho que você deve auditar (e rejeitar se discordar):**

| Decisão | Por quê |
|---|---|
| `artefato=` obrigatório, sem default | Impossível validar sem declarar o vocabulário. É o F2 fechado por construção |
| `verificar_literal()` devolve `{status, casados, total, divergencia}`, nunca booleano | Um booleano não diz a causa; cada causa tem reparo diferente |
| `SELO`/`ROTULO`/`PROSA` = **aviso**; `AUSENTE`/`VAZIO` = **bloqueante** | Se o prefixo longo casa, a frase existe: é dessincronização. Se nada casa, pode nunca ter existido |
| `LEGADO_CONHECIDO` — `VALIDADO_G3_IA` e `PENDENTE_FULLTEXT` viram aviso **nomeado, com tradução** | São a ressalva que o seu P-4 já declarou. Não podem ser silenciados nem confundidos com defeito novo |

Se a 3ª ou a 4ª estiverem erradas, diga: são julgamento, não fato.

---

# 5. O que peço nesta rodada

| # | Pedido | Tipo |
|---|---|---|
| 1 | **Decisão AT-11** (`*_intervencao`: tier oficial ou remapeamento) | 🔴 bloqueia 3 registros e o critério [6] do gate |
| 2 | Corrigir no `gate_script.py`: `tier_1_intervencao` → tier real | 🔴 o filtro está desligado hoje |
| 3 | Veredito sobre o `contrato.py` — adotar, emendar ou rejeitar | 🟠 |
| 4 | Rodar o contrato nas **B2, B7, B8** e me mandar só a contagem por categoria | 🟠 valida se os 33 são exclusivos da B1 |
| 5 | **Pacote da Rodada 2** quando estiver pronto: scripts `[AT]` B3→B16 **+ ferramentas oficiais** | 🟡 |

---

# 6. Uma pergunta de método, para você pensar sem pressa

Os 77 do rótulo defasado, os 22 do selo e a sua regressão B14 têm a mesma raiz: **um artefato foi editado depois que outro artefato derivou dele, e nada detectou a defasagem.**

O `contrato.py` pega isso na hora da escrita. Mas não impede que alguém edite a Canônica amanhã e desatualize 257 vínculos em silêncio.

A defesa usual é **hash de proveniência**: cada vínculo grava o `sha256` da Canônica de onde foi extraído; qualquer divergência de hash marca o vínculo como `dessincronizado` até re-extração. Meu `validar_roundtrip` já calcula e declara esse hash (`C9`), mas nenhum vínculo o armazena.

Não estou propondo como IMPL ainda — quero seu parecer se cabe no SCHEMA v2 ou se é peso demais para o ganho. **Você conhece o custo de escrita da série melhor que eu.**

---

**Anexos:** `contrato.py` · `canonico/literalidade_b1.json` · `RELATORIO_ITEM1_ROUNDTRIP.md` · `RELATORIO_ITEM2_CONTRATO.md`
