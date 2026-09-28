# AT-02 — literalidade da B1: 40% → 88%
10/09/2026 · 4 passadas · 3 backups

---

# 1. Resultado

| Passada | Método | Reparos | Literalidade |
|---|---|---|---|
| — | estado inicial | — | **103/257 = 40%** |
| 1ª `reancorar.py` | busca de frase por prefixo | 80 | 183 = 71% |
| 2ª `reancorar2.py` | alinhamento de índices (selo com conteúdo) | 6 | 189 = 74% |
| 3ª `reancorar3.py` | âncora dupla (prefixo + sufixo) | 38 | **227 = 88%** |
| 4ª `reancorar4.py` | multi-âncora por segmentos | 0 | 227 = 88% |

**124 vínculos reancorados. Zero dados inventados. Zero bloqueantes novos.**

Restam **30** (20 PROSA + 10 ROTULO), todos com causa nomeada.

---

# 2. Por que parei em 88% e não forcei os 100%

Você pediu 100%. **Os 30 restantes não são reparáveis por máquina — e forçá-los seria falsificar.** Cada passada recusou mais do que aceitou, de propósito:

| Passada | Propôs | Aceitou | Recusou |
|---|---|---|---|
| 1ª | 99 | 80 | 19 |
| 3ª | 68 | 38 | 30 |
| 4ª | 1 | **0** | 30 |

Na 4ª passada, o único candidato produzia:

```
antes: «…mesma cascata (Punicalin LPS memory NF-κB, 2024)[ML; camundongo][EXT].»
novo : «…de memória induzido por LPS por supressão da mesma cascata»
```

Ele *aumentaria* a literalidade — cortando a frase no meio e jogando fora a citação. Acrescentei a guarda de fronteira (Prompt v4.2 L1450) e o reparo virou **0**.

**Um número de literalidade que sobe destruindo conteúdo é pior que um número honesto de 88%.**

---

# 3. 🔴 O que os 30 restantes revelam — e é achado de conteúdo

## 3.1 Nove casos de "ano divergente" — 3 são o mesmo defeito estrutural

A guarda do ano (todo ano citado no vínculo deve existir na fatia) recusou 9. Três deles são graves:

```
VINC_B1_0146 · ref=REF_SCHAFER_2012 · trecho fala de Schafer 2012  ✅ coerente
VINC_B1_0147 · ref=REF_HAO_2024     · trecho fala de Schafer 2012  ❌
VINC_B1_0148 · ref=REF_ZHAO_2025    · trecho fala de Schafer 2012  ❌
```

**Três vínculos, três referências diferentes, o mesmo `trecho_ancora`.** Dois deles (Hao 2024, Zhao 2025) estão ancorados numa frase que cita **outro artigo**. O G3 desses vínculos foi dado sobre uma frase que não é a deles.

Mesmo padrão em `VINC_B1_0121`/`0122` (Arora 2019 e Gulen 2016 no mesmo trecho) e `VINC_B1_0040`, `0050`, `0075`, `0118`.

**Isto não é dessincronização de etiqueta. É vínculo apontando para a frase errada** — e a re-extração automática *pioraria*, porque consolidaria a âncora errada como literal.

## 3.2 O problema é maior que os 30

Medi em todo o arquivo:

```
25 trechos são compartilhados por MAIS DE UMA referência
57 vínculos envolvidos
```

Só 5 desses estão entre os 30 não-literais — **os outros 52 já estão "literais" e passariam em qualquer checador**. São literais e mesmo assim não discriminam qual afirmação sustenta qual referência.

**É exatamente o furo F5** que apontei no `validar_auditoria.py` (trecho sem exigência de unicidade), agora com número: **57 vínculos na B1.** E é a mesma questão que levantei sobre a listra do ledger — só que aqui, no arquivo de vínculos, a arquitetura é claim-level e a unicidade deveria valer.

**Registro como AT-13**, para o outro agente: não é reparo de literalidade, é reauditoria de vínculo. Máquina nenhuma decide isso.

---

# 4. Os 30, classificados

| Causa | N | Reparável? |
|---|---|---|
| 1 parêntese defasado, sufixo também diverge | 16 | Talvez, com regra por posição — mas o risco de troca é alto |
| **Ano divergente = outra referência** | **9** | ❌ **Não. É AT-13** |
| Prosa realmente diferente | 2 | ❌ Inspeção humana |
| Vão incompatível | 2 | ❌ Inspeção humana |
| Truncaria a frase | 1 | ❌ Recusado por desenho |

Inventários: `canonico/at02_residuo_manual.json` · `canonico/at02_ano_divergente.json` (os 9, com o texto do vínculo e o texto da Canônica lado a lado).

---

# 5. As guardas que impediram falsificação

Cada uma nasceu de um erro real que o script quase cometeu:

| Guarda | Origem |
|---|---|
| Prefixo comum ≥50% do alvo | 1ª passada trocaria `VINC_B1_0001` por outra frase literal |
| Tamanho entre 0,6× e 1,6× | idem |
| Sufixo ≥25 chars (âncora dupla) | prefixo sozinho não prova ser a mesma frase |
| **Ano do vínculo presente na fatia** | resolvedor de parênteses do lote 5 trocou autoria Menard→Li |
| **Fronteira natural no fim** | 4ª passada truncaria a frase para "melhorar" o número |
| Validação diferencial | contrato travava reparo por causa de passivo alheio |

---

# 6. Resposta ao agente gerador (pontos dele)

- **AT-11 opção (b):** concordo integralmente. "Intervenção é tipo de desenho de prova, não nível da escala de força causal" é a formulação correta.
- **`desenho_evidencia` ortogonal:** endosso, sem contraproposta. Preserva a granularidade real dos 106 registros e fecha o enum por construção. É a opção (a) domesticada, como ele disse.
- **A família fantasma é maior:** ele achou **106 registros** em B7/B8 contra os 3 que eu vi. Ele tem os dados; eu tinha só a B1.
- **Fronteira 93-vs-77:** os anexos estão em `PARA_O_AGENTE/anexos_2026-09-10/`. Mas atenção: o `literalidade_b1.json` que gerei era **pré-reparo**. Estou regenerando o inventário no estado atual (88%) para não alinharmos definições sobre dados vencidos.
- **Ponto 3 do veredito dele (prefixo 85–99 como aviso nomeado):** aceito. Ele está certo — meu limiar de 40 era frouxo, o dele de 100 era rígido; "prefixo longo ≥85 = dessincronização, não inexistência" é o meio-termo correto, e o B2 é o contra-caso que prova (lá o AUSENTE é rascunho de campo, bloqueante correto).
- **Hash de proveniência (E5):** de acordo com hash do **bruto**, e com a observação dele de que a "liturgia" é virtude — hoje a edição silenciosa é gratuita.

---

# 7. Estado da B1

```
literalidade ....... 227/257 = 88%   (era 40%)
bloqueantes ........ 33 → 30          (AT-11 resolveu 3 no lado dele)
resíduo AT-02 ...... 30, com causa nomeada
achado novo ........ AT-13: 57 vínculos com trecho compartilhado
```

**Para chegar a 100% falta decisão humana, não código.** Os 16 de "sufixo divergente" talvez rendam mais 10–12 com uma 5ª passada por posição de parêntese, mas o risco de troca cresce e o ganho é pequeno. Os 9 do ano são reauditoria.

Minha recomendação: **fechar o AT-02 em 88%**, mandar os 30 para o P-6 junto com o AT-13, e voltar ao objetivo maior — provar o pipeline ponta a ponta. A B1 está utilizável agora; não estava em 40%.
