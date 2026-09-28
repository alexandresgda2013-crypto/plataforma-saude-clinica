# ITEM 1 CONCLUÍDO — `validar_roundtrip.py` corrigido
10/09/2026 · backup em `validar_roundtrip.py.bak`

---

# 1. O que estava errado no meu validador

Três defeitos, todos meus:

| # | Defeito | Efeito |
|---|---|---|
| D1 | `norm()` removia **selos** junto com a formatação | Um trecho não-literal era declarado conforme. Inflava 33% → 51% |
| D2 | Aceitava **prefixo de 80 chars** como "possível truncamento" e seguia | Um trecho que casava 111 de 581 chars passava calado |
| D3 | Reportava **quantos falharam**, nunca **quantos examinou** | Exatamente o defeito que eu acusei no `check_fidelidade_canonica` |

D1 é o mais grave: eu misturava normalização de **apresentação** (legítima: `**negrito**`, hífens unicode) com remoção de **conteúdo** (ilegítima: selos). São coisas diferentes e agora são duas funções.

---

# 2. O que fiz

**`norm()`** — só apresentação. Markdown, variantes unicode, espaço entre tags adjacentes (`] [` → `][`). Preserva todo o resto.

**`norm_selos()`** — nova, com **enum fechado** de 11 selos. Usada *apenas para diagnosticar causa*, nunca para aprovar. O docstring registra o motivo:

> *"Um trecho que só casa aqui é uma PENDÊNCIA DE RE-EXTRAÇÃO, não um trecho válido."*

Isso responde à advertência do outro agente sobre normalizador agressivo: qualquer colchete fora do enum (tags `[OB]`, `[ML]`, `[EC; humano]`, listras) é **conteúdo e nunca é removido**.

**CHECK 1 reescrito** — classifica por **causa** via busca binária de prefixo comum, e reporta onde divergiu, não só que divergiu.

---

# 3. Resultado — os 257 vínculos da B1

```
C1  EXAMINADOS: 257 vínculos · LITERAIS: 103 (40%)

❌  22 só casam ignorando SELOS   — prosa selada após a extração
❌  77 com RÓTULO DEFASADO        — título em inglês onde a Canônica tem (Autor, ano)
❌  55 com PROSA DIVERGENTE       — Canônica editada após a extração
   103 LITERAIS
```

| Antes | Agora |
|---|---|
| "140 casaram só por prefixo" (sem causa) | 4 categorias, cada uma com reparo próprio |
| 51% literal (inflado) | **40% literal**, medido |
| Não dizia quantos examinou | `EXAMINADOS: 257` |

**Sobre a divergência de números com o outro agente:** ele mediu 33% cru; eu meço 40%. A diferença são 18 trechos que só diferem por `**negrito**` e espaço entre tags — normalização de **apresentação**, que é legítima. Nossos números convergem quando a régua é a mesma; o dele estava certo contra o meu 51% de ontem, e o 40% de hoje é o número defensável.

---

# 4. A descoberta: os 77 do "rótulo defasado"

Esta é a **maior categoria isolada**, e eu não a tinha visto:

```
VINC_B1_0019 casa 309/394 · diverge em:
  «Mechanistic insights from inflammasome structures, 2024)[EC; humano]…»
```

O vínculo carrega o **título em inglês do artigo** dentro do trecho; a Canônica, no mesmo ponto, traz a citação nominal `(Autor et al., ano)`. Os primeiros 309 caracteres são idênticos — a prosa confere.

**Isto não é dado inventado, é dessincronização.** A prosa foi normalizada para citação nominal em algum momento posterior à gravação dos vínculos, e os vínculos ficaram com o rótulo provisório da geração.

**Consequência prática para o AT-02:** dos 154 não-conformes, **99 (22 selo + 77 rótulo) casam por prefixo longo** — a frase está lá, só a cauda mudou. São reparáveis por re-extração automática com alta confiança. Os **55 de prosa divergente** exigem inspeção. A fila deixou de ser "127 trechos ruins" e virou dois problemas de tamanho e risco diferentes.

---

# 5. Artefato gerado

**`canonico/literalidade_b1.json`** — 257 registros, um por vínculo:

```json
{"id_vinculo": "VINC_B1_0019", "claim_id": "...", "secao": "...",
 "status_literalidade": "ROTULO", "chars_casados": 309, "chars_total": 394}
```

É a **fila de trabalho do AT-02**, ordenável por esforço (`chars_casados / chars_total`).

---

# 6. Estado dos demais checks

Passando: C2 (PMIDs resolvem) · C3 (formato) · C4 (enum) · C5 (sem GRADE) · C6 (P12) · C7 (43 claim_id da NT resolvem) · C8 (8 IDs de exame) · C9 (hash declarado).

Avisos que continuam de pé: 30 sem `claim_id` · 30 com `natureza_relacao=tier_*` · 1 `pendente_fulltext`. São AT-01.

---

# 7. Próximo: `contrato.py`

Com fonte normativa agora conhecida — implementa o P-5 e o `MAPEAR_VOCABULARIO`, mais os furos F1–F5 que achei no `validar_auditoria.py`:

```python
validar_vinculos(regs, artefato)   # enum POR ARTEFATO (F2 — causa da regressão B14)
verificar_literal(trecho, corpo)   # devolve (status, chars_casados) — nunca booleano
gravar_seguro(path, dados)         # backup + escrita atômica
abortar_se(problemas)              # sys.exit(1) — o que falta em 10 dos 36 scripts
```

E a regra que aprendi hoje na própria pele: **todo checador reporta quantos itens examinou.**
