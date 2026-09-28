# TRÍPLICA — resposta à Contrarrazão + perícia do `validar_auditoria.py`
10/09/2026

---

# 0. Antes de tudo: três retratações minhas

A contrarrazão é séria, mede o que afirma e me corrige em pontos reais. Começo pelo que eu errei.

## 🔴 Retratação 1 — a mais grave. Eu acusei o ledger errado.

Eu escrevi que os 237 `trecho_ancora` do ledger "não são âncoras, são dumps de rótulos", e que "pela regra do projeto não tinham permissão de receber G3".

**Rodei a verificação de literalidade do próprio framework contra a V4:**

```
trecho_ancora LITERAL na canônica: ok=237  aviso=0  ERRO=0  (de 237)
```

**Os 237 são substring literal da Canônica.** As listras `*ZDILAR_2000[MA] | CAPURON_2002[EC] | ...*` **existem no corpo do documento** — são o formato de âncora `[REF_BLOCO_XX: ...]` previsto no Prompt v4.2 e reconhecido pelo `ANCHOR_RE` do framework. Não são lixo do extrator. É uma **arquitetura de listra**, deliberada, e o framework a valida.

Eu julguei um formato que não conhecia usando a régua de outro formato. Foi exatamente o erro que eu mesmo tinha catalogado como dead end: *"antes de acusar dado alheio, provar que o comparador não é a causa"*. Reincidi.

**O que permanece de pé, e só isso:** o G3 varia dentro de um mesmo trecho compartilhado (21 APROVADO / 3 RESSALVA / 1 INCONCLUSIVO em 25 registros que citam a mesma listra). O trecho é literal, mas **não é discriminante** — dele não se recupera qual afirmação foi julgada. É uma limitação de rastreabilidade fina, **não uma violação**. Rebaixo de 🔴 para 🟡.

## ✅ Retratação 2 — "dois vocabulários": eu estava certo pelo motivo errado

Ontem eu disse "os vínculos estão certos, o ledger violou o `MAPEAR_VOCABULARIO`". **Errado.** O `validar_auditoria.py` prova que são dois enums **diferentes e ambos oficiais**:

| Enum | Vocabulário |
|---|---|
| `ENUM_STATUS_AUD` (**ledger**) | APROVADO · APROVADO_COM_RESSALVA · NAO_SUSTENTA · PMID_INCORRETO · REALOCAR… |
| `MAPEAR_VOCABULARIO` (**vínculo**) | CONFIRMADO · PARCIALMENTE_CONFIRMADO · NAO_SUSTENTA_CLAIM · CITACAO_INCORRETA |

Interseção: **apenas `NAO_LOCALIZADO`**.

O ledger usa `APROVADO` **corretamente** — é o enum do ledger. Cada artefato tem o seu, por desenho.

**Mas o problema real é maior do que o que eu tinha apontado:** dois vocabulários quase-disjuntos para o mesmo conceito, distinguidos só pelo arquivo em que moram. Um `APROVADO` num arquivo de vínculos é erro; num ledger é certo. **Nenhuma ferramenta valida essa fronteira** — e foi exatamente aí que a B14 quebrou (o agente achou sozinho: `B14_json_apply` copiou template de ledger para vínculos). O defeito não é de quem escreveu; é do desenho de ter dois enums que só diferem por contexto.

## ✅ Retratação 3 — literalidade: o agente está mais certo que eu

Replicação independente, mesma base:

```
cru : 86/257 = 33%   ← idêntico ao número dele
norm: 125/257 = 49%  (ele: 96=37% · eu ontem: 130=51%)
```

**Convergimos no número cru.** A divergência é só a força do normalizador de selos — e o meu é agressivo demais, o que **infla** a literalidade aparente. Confirma que minha prioridade nº1 (corrigir o `validar_roundtrip.py`) é a certa, e que meu 51% de ontem era otimista.

---

# 1. Perícia do `validar_auditoria.py` — 🟢 o melhor script do acervo

Sem disputa. Faz o que nenhum dos 36 fazia:

| Prática | Presente |
|---|---|
| **Valida 12 campos contra enum fechado** | ✅ único |
| **Integridade referencial** ledger→Módulo 09 | ✅ |
| **Coerência cruzada** `tipo_classificador` × arquivo de origem | ✅ |
| **Literalidade com fuzzy** — distingue "não literal" (ERRO) de "próximo, texto editado?" (AVISO ≥0.85) | ✅ **exatamente o que faltava no meu** |
| **"Decisão exige verificação"** — status decidido sem abstract/data/verificador = ERRO | ✅ anti-autocertificação real |
| **Proíbe PMID/DOI no corpo** | ✅ |
| **Órfãs nos dois sentidos** | ✅ |
| ERRO vs AVISO separados, exit code correto | ✅ |

O bloco `decidido → exige verificacao{abstract, data, verificador}` é a implementação literal de *"o LLM não tem permissão de escrever os campos de verificação"*. É a peça mais madura do projeto.

## Furos que encontrei (5)

| # | Furo | Efeito |
|---|---|---|
| **F1** | **Não valida `citacao_literal` contra o `trecho_ancora`.** Confere que cada um está no texto, nunca que a citação está *dentro* da âncora | Um par (âncora, citação) pode ser de frases distintas e passar |
| **F2** | **Não valida a fronteira de enum entre artefatos.** Não sabe que `CONFIRMADO` é ilegal no ledger e `APROVADO` ilegal em vínculos | **É o buraco por onde a B14 caiu** |
| **F3** | **Não valida o arquivo de vínculos.** Valida Módulo 09 + ledger + corpo. Os 30 `natureza_relacao=tier_*` são invisíveis para ele | O "0 ERRO" nunca olhou os vínculos |
| **F4** | Casamento por substring: `sob.upper() in rid.upper()` — `"LI"` casa com `REF_LI_2021` e `REF_QUALQUERCOISALI_2021` | Falso negativo silencioso |
| **F5** | `trecho_ancora` não precisa ser **único**; nada impede 25 registros compartilharem um | O item 0 desta tríplica |

**Consequência para o item 4 do meu parecer anterior:** o "0 ERRO / 237 avisos" é honesto **dentro do escopo do script**. O que eu não sabia é que **os vínculos não estão nesse escopo**. Reformulo: não é que o checador seja cego — é que o P-4 apresentou "framework 0 ERRO" como se cobrisse artefatos que ele nunca leu.

---

# 2. Onde mantenho a posição

## 2.1 Ordem de prioridade (contra a seção 3.5)

Ele reordena: órfãos B7 → campos B1 → literalidade. **Aceito integralmente para os dados.** Mantenho meu item 1 apenas porque é *meu* instrumento de medição, roda em minutos e não compete com nada. As duas trilhas correm em paralelo, como ele mesmo diz. **Sem divergência real.**

## 2.2 `uso: "B1_v2"` (contra a seção 3.2)

Ele diz: convenção nativa, não corrupção. **Aceito o fato** — se B16 v1 já nascia assim, é convenção. **Mantenho a objeção de desenho:** um campo chamado `uso`, cujo enum semântico é `clinico|contexto_mecanistico|gap_pesquisa`, carregando marca de versão é sobrecarga de campo — a mesma classe de erro da `V()` que pôs `forca_causal` em `natureza_relacao`. A ação dele (documentar no SCHEMA v2) resolve; eu preferiria depreciar para `lote_origem`.

## 2.3 `g1_metodo` (seção 3.3)

Concordância total, inclusive na solução dele — **checksum do arquivo de efetch no manifesto** é melhor que a minha proposta. *"A exigência do checklist é fraca (string, não prova)"* é a formulação exata.

---

# 3. O que ele achou e eu não achei

Isto merece registro explícito, porque é a parte mais valiosa do documento:

| Achado dele | Por que eu não achei |
|---|---|
| **B7: 31 vínculos órfãos** | Só recebi dados da B1 |
| B2: 126 refs sem vínculo · 61 trechos com "PMID" embutido | idem |
| B8: 62 sem vínculo · 58 sem ledger | idem |
| **B14: regressão viva, achada e reparada hoje** (50 vínculos com vocabulário de ledger) | idem — **e é a prova empírica do F2** |
| Falso-positivo do checklist: `B01_` → `B01` vs. `Auditoria_B1` | Nunca rodei o checklist oficial |
| B1: 17 refs sem vínculo, 37 coberturas duplicadas | Não cruzei refs↔vínculos nos dois sentidos |

**A B7 com 31 órfãos é o pior defeito vivo do projeto, e é dele o achado.** Ele aplicou meu método a um escopo que eu não tinha e encontrou mais do que eu. É o resultado que se espera de uma auditoria bem-sucedida.

E a conclusão que ele soma é a que eu não tinha condições de tirar:

> *"o defeito 'detecta e não bloqueia' também existe **nas ferramentas oficiais**"*

Está certo. O F3 acima é a prova: o framework oficial não lê o arquivo onde vivem os 30 defeitos conhecidos.

---

# 4. Plano consolidado

Adoto o plano dele (AT-00..AT-09) como **plano único**, com quatro emendas:

| Emenda | Conteúdo |
|---|---|
| **E1 → AT-06** | Acrescentar item duro: **enum válido por artefato** (ledger ≠ vínculo). É o F2, causa da regressão B14 |
| **E2 → AT-06** | O framework deve **ler o arquivo de vínculos** (F3). Hoje "0 ERRO" não cobre onde estão os defeitos |
| **E3 → AT-02** | Antes de re-extrair: **decidir se arquitetura de listra é válida como âncora de G3**. Se sim, o G3 precisa apontar para a *frase*, não só para a listra — senão o veredito não é recuperável (meu único achado sobrevivente do ledger) |
| **E4 → AT-09** | Formalizar as **duas arquiteturas** (claim-level × listra-level) no SCHEMA v2 e **declará-la no manifesto de cada biblioteca**, para o checador se parametrizar. É a proposta dele em 3.1, que subscrevo |

**Rodada 2 da perícia: aceito.** Os 8+ scripts `[AT]` (B3→B16), com foco em (i) `B14_json_apply` e outras classes de vocabulário cruzado, (ii) idempotência real dos `md_apply`, (iii) cobertura das asserções. É onde a plataforma vive hoje — e é onde o F2 pode ter deixado mais filhos.

---

# 5. Sobre sua pergunta: o `MAPEAR_VOCABULARIO` foi usado na B1?

**Foi, e corretamente.** Prova nos dados:

- Vínculos da B1: `CONFIRMADO` (237) / `PARCIALMENTE_CONFIRMADO` (19) / `NAO_LOCALIZADO` (1) — **é o enum do MAPEAR**
- Ledger da B1: `APROVADO` / `APROVADO_COM_RESSALVA` / `NAO_LOCALIZADO` — **é o enum do framework**

Cada artefato com o seu vocabulário oficial. A tradução foi aplicada. **O que não existe é uma ferramenta que impeça a troca** — e por isso a B14 quebrou. A resposta à sua dúvida é: o mapa foi usado, mas ele é um documento, não um portão.

---

# 6. Fecho

Ele tem razão em três pontos contra mim, um deles grave (acusei um formato válido de ser lixo). Eu tenho razão nos furos F1–F5 do framework, e o F2 já se provou sozinho na regressão da B14.

Nenhum de nós dois encontrou **um único dado científico inventado** em 36 scripts, 16 bibliotecas e 237 referências. Os defeitos são todos de transporte e de contrato — e agora estão mapeados, com dono e número.

**Sigo com o item 1 (corrigir meu `validar_roundtrip.py` com a lógica de fuzzy do framework), depois `contrato.py`.** Peça a ele o pacote da Rodada 2 quando quiser.
