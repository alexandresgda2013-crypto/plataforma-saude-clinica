# AUDITORIA CIENTÍFICA — CLAIM B1.SM02.014
## "MDD apresenta maior ligação de TSPO no cérebro que controles"

**Auditor-Mestre · 2026-09-25**
**Claim:** `B1.SM02.014` · status declarado `aprovado_com_ressalva`
**Método:** verificação contra fonte primária das referências decisivas — não aceito o achado como declarado.
**Escopo:** auditoria científica do claim (direção, magnitude, contra-evidência, força). Não é fechamento do claim nem execução do rito v1.10 — é o parecer do meu território sobre a ciência.

---

## VEREDITO: **`aprovado_com_ressalva` é o status correto.** A direção do claim está sustentada; a força é modesta e a ressalva é obrigatória. Duas correções de precisão no enunciado e uma exigência de escopo.

---

## 1. A direção — sustentada por fonte primária

Verifiquei os estudos-âncora contra a fonte, não contra a lista:

- **Setiawan 2015 (JAMA Psychiatry)** — primeira evidência compelível de TSPO VT elevado em MDE, medication-free, `18F-FEPPA`, com correlação regional entre TSPO e gravidade. Direção positiva confirmada.
- **Eggerstorfer 2022 (Front Mol Neurosci)** — a meta-análise: 8 estudos PET, **238 MDD × 164 controles**, elevação em múltiplas regiões corticais.
- **Holmes 2018, Richards 2018, Setiawan 2018** — todos na direção de elevação, com o eixo suicídio/gravidade.

A afirmação "MDD apresenta maior ligação de TSPO que controles" **é verdadeira na direção**, e é a leitura consolidada da área (Meyer 2020, Lancet Psychiatry: "os resultados mais compeliveis de TSPO foram em MDD, com aumentos consistentes").

## 2. A magnitude — modesta, e o enunciado não a carrega

Aqui está a primeira correção. A meta de Eggerstorfer mede efeitos **moderados, região-dependentes**, não um aumento uniforme:

| Região | Hedges' g | IC 95% |
|---|---|---|
| Cingulado anterior (ACC) | 0,60 | 0,36–0,84 |
| Hipocampo | 0,54 | 0,26–0,81 |
| Ínsula | 0,43 | 0,17–0,69 |
| Córtex pré-frontal | 0,36 | 0,14–0,59 |
| **Córtex temporal** | 0,39 | **−0,04–0,81** |

Duas consequências para o enunciado:

**(a) O efeito é regional, não "no cérebro" globalmente.** O claim diz "maior ligação de TSPO **no cérebro**". A evidência sustenta "maior em regiões corticais específicas, com o ACC como o achado mais robusto". "No cérebro" superdimensiona — sugere elevação global, quando o córtex temporal **não atinge significância** (IC cruza zero) e a magnitude varia por região. **Correção:** o statement deveria ler "em regiões corticais (mais robustamente no cingulado anterior)", não "no cérebro".

**(b) A magnitude é moderada (g 0,36–0,60), não forte.** Nenhum efeito chega a `g=0,8`. Isso não enfraquece a direção, mas fixa o teto: é associação moderada de grupo, não marcador de grande efeito. A força epistemológica do claim é **média**, e o `grau_maturidade` correspondente no N2 deve refletir isso — não "muito_estabelecido".

## 3. A contra-evidência — presente na própria lista, e é o que torna a ressalva obrigatória

A lista de fontes do claim **inclui os estudos negativos**, o que é correto e honesto:

- **Hannestad 2013** — "o marcador de neuroinflamação TSPO **não está elevado** em indivíduos com depressão leve-a-moderada" (`11C-PBR28`). É o contraponto direto, e a diferença provável é de gravidade: os positivos são MDE mais grave.
- **Schubert 2021** — "aumento **modesto** de TSPO, **não** associado a PCR nem IMC". Confirma direção mas rebaixa magnitude e desacopla dos marcadores periféricos.
- **Nettis 2020** — desafio com IFN-α **não** alterou TSPO cerebral. Relevante para causalidade (ver §5).
- **Li 2018** — TSPO **reduzido** durante TCC, e microglia associada a disfunção cognitiva.

A ressalva é **obrigatória e tem tipo definido**: pela taxonomia do Schema-Claim v1.3, isto é **heterogeneidade** (efeito depende de gravidade; estudos de depressão leve não replicam), não condição de aplicação nem maturidade. A materialização, portanto, mantém `direcao_suporte = sustenta` com `condicao = null`, e a ressalva de heterogeneidade fica registrada — exatamente o caso que a V-K6 e o P-K3 do schema foram desenhados para tratar sem fabricar condição.

## 4. Correção de escopo — o que é B1 e o que não é

A lista tem ~110 referências, e a **maioria não é sobre MDD**: há dezenas de estudos de Alzheimer, Parkinson, esquizofrenia, esclerose múltipla, fibromialgia, epilepsia, e um grande bloco de **metodologia de radioligante** (comparações PBR28/ER176/PK11195, cinética, polimorfismo rs6971). Isso é apropriado como **contexto de fundo** — a validade do TSPO como marcador depende dessa metodologia — mas exige uma regra clara na materialização:

**Só as fontes que medem TSPO em MDD × controle sustentam o claim.** As demais são contexto ou suporte metodológico, e **não podem** entrar como `sentido_do_achado = suporta_relacao` do claim de MDD — seria inflar o lastro com estudos de outra doença. Pelo protocolo de escopo B1, os estudos de Alzheimer/Parkinson/esquizofrenia com TSPO pertencem a **outros IDs** ou ao aprofundamento metodológico, não ao claim `.014`. As ~15 fontes de MDD (Setiawan 2015/2018, Holmes 2016/2018, Richards 2018, Hannestad 2013, Schubert 2021, Li 2018, Su 2016, Yrondi 2018, Joo 2021, Herzog 2024, Eggerstorfer 2022, Enache 2019, Gritti 2021) são as que materializam; o resto é fundo.

## 5. Fronteira epistemológica — o que o claim NÃO pode virar

Três limites que o meu território exige que fiquem escritos, porque o TSPO os convida a atravessar:

- **TSPO ≠ neuroinflamação comprovada.** O próprio corpo de evidência da lista (Nutma 2023: "TSPO é marcador de micróglia ativada em roedores, mas **não** em doenças neurodegenerativas humanas"; Notter 2018; Owen 2010 sobre polimorfismo) diz que TSPO é um **sinal**, não prova de ativação microglial em humano. O claim deve permanecer em "maior ligação de TSPO", que é o que se mede — **nunca** "maior neuroinflamação", que é interpretação. A NT, quando consumir este claim, não pode elevar de "sinal de TSPO" para "neuroinflamação".
- **Associação, não causalidade.** Nettis 2020 (IFN-α não elevou TSPO) e a natureza transversal dos estudos impedem "a neuroinflamação causa MDD". É `natureza_relacao = associativa`, não causal.
- **Periferia ≠ centro, e o desacoplamento é dado.** Schubert 2021 mostra que o TSPO cerebral elevado **não** se associa a PCR nem IMC — ou seja, este claim central não pode ser sustentado por, nem usado para sustentar, marcadores inflamatórios periféricos. São eixos separados.

## 6. Nota de método — o que não pude verificar

Verifiquei por fonte primária: Setiawan 2015, Eggerstorfer 2022 (magnitude e n), Hannestad 2013, Schubert 2021, Meyer 2020. **Não** reli os ~105 estudos restantes — a maioria é contexto e não sustenta o claim (§4), mas registro que a auditoria científica **completa** dos estudos de MDD exige releitura das ~15 fontes-âncora contra os números que cada uma reporta, e isso é trabalho do fechamento pelo rito das três IAs, não deste parecer. O que este parecer estabelece é que **a direção está certa, a magnitude é moderada, a ressalva é de heterogeneidade, e o escopo precisa ser filtrado**.

---

## Resumo para o fechamento

| Dimensão | Veredito |
|---|---|
| Direção ("maior TSPO em MDD") | **sustentada** |
| Magnitude | **moderada** (g 0,36–0,60), regional; não global, não forte |
| Enunciado "no cérebro" | **corrigir** para "em regiões corticais, mais robustamente ACC" |
| Status `aprovado_com_ressalva` | **correto** |
| Tipo da ressalva | **heterogeneidade** (depende de gravidade) — não condição |
| `natureza_relacao` | **associativa**, não causal |
| Escopo | **filtrar**: só ~15 fontes de MDD materializam; o resto é fundo |
| Limite a preservar na NT | TSPO = sinal, nunca "neuroinflamação comprovada" |

O claim é aproveitável e o status é o certo. As correções são de **precisão do enunciado e de escopo de fontes**, não de rejeição — a ciência sustenta o que o claim afirma, desde que o afirme na medida certa.

---

*Verificações: Setiawan 2015 (JAMA Psychiatry, direção +), Eggerstorfer 2022 (Front Mol Neurosci — g por região e n=238/164, ACC IC 0,36–0,84, temporal IC −0,04–0,81), Hannestad 2013 (negativo, leve-moderada), Schubert 2021 (modesto, desacoplado de PCR/IMC), Meyer 2020 (revisão), todos contra fonte primária nesta sessão. Contra-evidência confirmada presente na lista do claim. Os ~105 estudos de outras doenças e de metodologia não foram relidos — classificados como fundo/contexto por escopo.*
