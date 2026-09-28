# EXECUÇÃO DO ENSAIO — B1.SM02.014 · janela do Auditor-Mestre (IA 3/Claude)
## G1 / G2 / G3 executados, com registro operacional

**Auditor-Mestre · 2026-09-25**
**Natureza:** registro de teste (ensaio pré-piloto). Não muda o status do `.014`, que permanece `aprovado_com_ressalva` no Bloco. Cego: entreguei meu filtro e meu veredito **antes** de ver os das outras IAs — este é o meu trabalho isolado.

---

## G1 — existência (fontes-âncora de MDD)

Executei G1 ao vivo sobre as fontes que sustentam o claim, contra o PubMed. Todas as âncoras de MDD existem e conferem: Setiawan 2015 (JAMA Psychiatry, PMID 25671328), Setiawan 2018 (Lancet Psychiatry, 29496589), Hannestad 2013 (23884183), Richards 2018 (EJNMMI Res), Schubert 2021, Eggerstorfer 2022 (Front Mol Neurosci), Holmes 2018. Nenhuma referência inventada nas âncoras — o que verifiquei na auditoria científica de ontem, confirmado aqui.

**Registro operacional G1:** a lista chegou com **DOI, não PMID**. G1 pede confirmação por PMID; o materializador terá de resolver DOI→PMID por busca, e isso **é** o G1 executando, como a instrução diz. Anoto a data da busca: 2026-09-25.

## G2 — escopo (o filtro, e é onde está o achado)

Executei o G2 sobre as **107 referências**. Classificação:

| Classe | Qtd | Materializa o claim? |
|---|---|---|
| MDD — PET humano (candidata forte) | **~13** | **Sim** |
| MDD — PET multimodal/correlato | 4 | Sim, com cautela (correlato, não medida direta de grupo) |
| MDD — revisão/meta | 3 | Sim, como síntese (Eggerstorfer, Enache, Gritti) |
| MDD — modelo animal | 2 | **Não** — pré-clínica, `uso = contexto_mecanistico`, nunca sustenta claim clínico |
| MDD — post-mortem/single-cell | 1 | **Contra-evidência**, outro compartimento (ver abaixo) |
| MDD — mecanismo básico (esteroidogênese) | 1 | Não — fundo |
| **Outro alvo, não-TSPO** (HDAC6) | 1 | **Não** — nem é TSPO |
| Outras doenças (AD, PD, esquizofrenia, MS, fibromialgia, Gulf War, epilepsia…) | **~66** | **Não** — fundo/contexto |
| Metodologia de radioligante | ~11 | Não — suporte metodológico |

**O achado central do G2, que confirma a auditoria de ontem: das 107, cerca de 66 são de outras doenças e ~11 são método.** Só ~20 tocam MDD, e destas apenas ~13 são TSPO-PET humano que materializam o claim. **A lista é ~80% fundo.** Isso não é defeito da busca — é o G2 fazendo o trabalho para o qual existe. Mas exige que o fechamento **não** deixe nenhuma das ~66 entrar como `sentido_do_achado = suporta_relacao`: seria sustentar um claim de depressão com estudo de Alzheimer.

**Três itens que o G2 precisa resolver antes de congelar a lista:**

1. **`Zhou 2026` (HDAC6) não é TSPO** — mede outro alvo. Sai do lote que materializa o claim de ligação de TSPO. É o tipo de intruso que passa despercebido porque o título tem "neuroinflammation" e "depression".
2. **`Li 2018` aparece duplicado** — são **dois artigos distintos** do mesmo autor/ano (um em Prog Neuropsychopharmacol Biol Psychiatry sobre TSPO reduzido em TCC; outro em J Affect Disord sobre marcadores microgliais e cognição). Não é duplicata a remover — são duas fontes que precisam de PMIDs distintos. A consolidação tem de separá-las, não deduplica-las.
3. **Böttcher 2020 é contra-evidência de compartimento, não fonte de suporte.** Single-cell de micróglia em MDD achou fenótipo **não-inflamatório**. Não é TSPO-PET; entra como **contra-evidência** (reforça a ressalva de heterogeneidade), com `sentido_do_achado = refuta_relacao` ou `inconclusivo` — nunca como suporte.

## G3 — veredito (direção por fonte)

Executei G3 sobre as âncoras de MDD, com o texto na mesa (verifiquei os abstracts na auditoria de ontem). Direção por fonte (`sentido_do_achado`):

| Fonte | `sentido_do_achado` | Base |
|---|---|---|
| Setiawan 2015 | `suporta_relacao` | TSPO VT elevado em MDE, g regional |
| Setiawan 2018 | `suporta_relacao` | VT associado a duração não-tratada |
| Holmes 2018 | `suporta_relacao` | TSPO elevado no ACC, eixo suicídio |
| Richards 2018 | `suporta_relacao` | TSPO aumentado em deprimidos não-medicados |
| Eggerstorfer 2022 | `suporta_relacao` | meta, g 0,36–0,60 por região |
| Schubert 2021 | `suporta_relacao` (modesto) | aumento modesto, desacoplado de PCR/IMC |
| **Hannestad 2013** | **`refuta_relacao`** | **não elevado em depressão leve-moderada** |
| **Li 2018 (TCC)** | **`refuta_relacao`/`inconclusivo`** | **TSPO reduzido durante TCC** |
| **Böttcher 2020** | **`refuta_relacao`** | micróglia não-inflamatória (outro compartimento) |

**Divergência entre fontes é real e é o dado, não erro** — como a própria instrução (X-1) diz. Ela não se resolve por votação: pela §regra, cada fonte carrega seu sentido, e a divergência vira `ressalva[tipo=heterogeneidade]`, com o padrão de que os positivos são MDE grave e os negativos são depressão leve. O artigo manda; a contagem de concordâncias não.

## As 4 decisões do fechamento (minha proposta, sujeita ao cruzamento)

1. **Estado:** `aprovado_com_ressalva` — mantido (é o do Bloco; o ensaio não o altera).
2. **Direção por fonte:** conforme a tabela G3 acima — maioria `suporta_relacao`, três `refuta_relacao`. **Não** há direção única do claim; há direção por fonte.
3. **Tipo da ressalva:** `heterogeneidade` (efeito depende de gravidade; leve não replica) — **não** condição de aplicação, **não** maturidade.
4. **Moderadores:** gravidade da depressão como modificador (`atenua` em depressão leve); permanece no claim, não materializa condição.

## Registro operacional do ensaio (formato S-4)

**O que funcionou:** G1/G2/G3 são executáveis de ponta a ponta sobre este claim; a taxonomia do Schema v1.3 (`sentido_do_achado` por fonte + `ressalva[heterogeneidade]`) representou o caso real sem forçar nada; a regra "sinal ≠ neuroinflamação" e o filtro de escopo funcionaram como travas.

**O que apresentou dificuldade:**
- **Lista com DOI, sem PMID** — G1 precisa resolver DOI→PMID; some com custo, mas anota-se.
- **~80% da lista é fundo** — o G2 filtra, mas o volume torna o cruzamento das três IAs pesado; sugiro que a lista já chegue pré-marcada por tema (não pré-filtrada — marcada), para o cruzamento comparar filtros sobre o mesmo universo anotado.
- **Intruso de alvo (HDAC6) e duplicata aparente (Li 2018)** — dois defeitos de lista que o G2 pega, mas que deveriam ser saneados na consolidação **antes** do congelamento, como a própria instrução já prevê ("3 nomes de autor corrigidos").
- **Nomes truncados** — `De Picker, *.` e `Kim, *.-H.` têm o primeiro nome corrompido no arquivo; corrigir antes de congelar.

**Problema de pacote/instrução, não de norma:** todos os itens acima são operacionais. Nenhum exige tocar Contrato, Schema ou COMO EXECUTAR.

**O que exigiria ciclo normativo:** nada encontrado neste claim. As três bases sustentaram a execução sem lacuna que peça alteração.

**Condições a congelar para o piloto:** lista saneada (HDAC6 fora do lote-TSPO, dois Li separados, nomes corrigidos), com data de busca, DOI→PMID resolvido, e as ~66 de outras doenças marcadas como fundo — não apagadas, marcadas.

---

## Fronteira do meu papel

Executei como IA participante do ensaio, transitoriamente. **Não é o piloto oficial** e **não testa cegueira** (conheço o histórico — S-5). O que este registro prova é que **o mecanismo operacional roda**: o rito produz as 4 decisões, a taxonomia comporta o caso, e os defeitos encontrados são de lista, não de norma. Ao fim, volto à bancada; o piloto oficial fica com a tríade dedicada.

*Registro para arquivamento com digital, conforme S-4. Verificações de conteúdo herdadas da auditoria científica de 2026-09-25 (Setiawan/Eggerstorfer/Hannestad/Schubert/Meyer contra fonte primária); classificação G2 executada sobre as 107 referências do arquivo do claim nesta sessão.*
