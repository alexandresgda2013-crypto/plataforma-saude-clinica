# AUDITORIA INTEGRAL — B1 NEUROINFLAMAÇÃO · BIBLIOTECA CANÔNICA V4.1
## Veredito final único (integra a Fase 1 — GPM/Briefing/normativos)

**Papel:** Auditor-Mestre (sessão independente da geração)
**Data:** 2026-09-11
**Artefato auditado:** `B1 NEUROINFLAMAÇÃO V4.1 CANONICA.md` (1.303 linhas; BLOCO_00–12 + TABELA DE EVIDÊNCIAS + CONTROVÉRSIAS/LACUNAS + APÊNDICE DE CORPUS + METADADOS CANÔNICOS + REGISTRO DE AUDITORIA 2026-09-11)
**Lote de evidência:** Módulo 09 N1 (`01_pmids` 201 + `02_meta_analises` 33 + `03_ensaios_clinicos` 3 = **237 refs**), N2 `vinculos_referencia_afirmacao` (**257 vínculos**, 81 claims únicos, 220 refs ligadas), `_manifesto_biblioteca` (v2.5, pipeline v2.6), `corpus_pubmed.json` (78 chaves de claim + `_ANCORAS_GPM`, 792 artigos), `log_de_busca.txt` (77 claims, 622 PMIDs), `b1_anchormap.json` (160 chaves), `7º LISTA CANÔNICA — B1` (v1.1, 83 itens, 2026-08-27), `RECONCILIACAO_B1_INSUMO_CONSENSUS.md` (2026-09-08).
**Verificação externa independente nesta sessão:** PubMed E-utilities — esummary de **237/237 PMIDs distintos** (0 não localizados), comparação de título/ano de 237, **14 abstracts [AT] por efetch**, conferência do corpus/log de busca contra os 237, âncoras 257/257, reconciliação item a item (49 refs propostas).
**Relatório de fase anterior:** `RELATORIO_INTERMEDIO_B1_GPM_BRIEFING.md` (AUD-001…025). Este relatório dá continuidade ao registro (AUD-026 em diante) e emite o **veredito final único** sobre o artefato canônico.

---

## 1. VEREDITO FINAL ÚNICO

> ## **APROVADA COM RESSALVAS**
>
> A Biblioteca B1 CANÔNICA v4.1 **alcança status canônico** sob as condições de correção do §8. **Não é REPROVADA**: zero referências inventadas (237/237 re-verificadas independentemente), zero âncora ausente (257/257), zero hard-fail (sem PMID/DOI/grade A–D/[PENDENTE] no corpo), correções das duas falhas GRAVE da Fase 1 efetivas e sem resíduo, e disciplina anti-nivelamento confirmada. **Não é APROVADA limpa**: a re-verificação G3 independente **confirmou 2 novos erros de claim→referência (GRAVE)** em afirmações do lote [AT]/[VERIFICADO] (AUD-026, AUD-027), além de 11 desvios MODERADO de governança/traçabilidade e uma revisão cega humana de 59 vínculos de alto-risco ainda pendente (declaração do próprio pipeline).

**Resumo das severidades (fase 2, este relatório):**

| Severidade | N | IDs |
|---|---|---|
| GRAVE | 2 | AUD-026, AUD-027 |
| MODERADO | 11 | AUD-028…038 |
| MENOR | 8 | AUD-039…046 |
| OBSERVAÇÃO | 2 | AUD-047, AUD-048 |

**Números-chave da auditoria mecânica (re-execução independente):**

| Porte | Resultado |
|---|---|
| G1 — PMIDs inventados | **0** (237/237 resolvem na PubMed) |
| G1 — títulos N1↔PubMed | 213/237 idênticos; 24 diferenças por truncamento/glifos; **0 trocas de paper** |
| G1 — ano `revista_ano`↔pubdate | **0 divergências** |
| G2 — âncoras (257) | **257/257 presentes** (96 exatas, 161 divergência apenas de formato — consistente com o registro de 5ª rodada: 151 re-extrações + 4 re-âncoras + 26 prefixos `###` removidos) |
| G2 — `redirecionado_clinico` | 20 vínculos — **comportamento previsto** pelo processo (lin. 50/177); não é defeito (AUD-047) |
| G3 — lote [AT] (14 abstracts) | 10 afirmações CONFIRMADAS; **2 GRAVE** (AUD-026/027); 3 MODERADO (AUD-028/029/030) |
| Hard-fails no corpo | sem PMID/DOI · sem grade A–D · sem [PENDENTE] · [G1]=0 |
| Censo de tags (corpo) | [VERIFICADO]=72 · [OB]=117 · [MA]=80 · [EC]=145 · [ML]=269 · [AT 2026-09-08]=14 blocos · [APENAS PRÉ-CLÍNICO]=10 · [PRÉ-CLÍNICO]=46 · [EXTRAPOLADO]=64 · [EXT]=135 |
| Módulo 09 | N1=237 · vínculos=257 · claims=81 · refs ligadas=220 · **refs órfãs de vínculo=17** (AUD-032) |
| Busca | corpus 761 PMIDs · log 622 PMIDs · **42 refs BUSCA_FERRAMENTA sem trilha nos artefatos fornecidos** (AUD-033) |
| Reconciliação [AT] | 49 refs propostas para AGREGA → **36 incorporadas, 13 omcidas sem registro de decisão** (AUD-034) |
| Lista Canônica | 83/83 itens ainda `em_busca`; zero `usado_em_biblioteca` (AUD-035) |

---

## 2. MODO

1. **Nunca aceitei conformidade declarada.** Todo gate foi re-executado sobre os artefatos do lote, com ferramenta (PubMed E-utilities) ou script, desta sessão — nunca pelo registro do manifesto.
2. **G1 100% dos PMIDs** (237 únicos, esummary): existência, título, periódico, data.
3. **Fidelidade canônica** (autor↔referência): comparação normalizada de todos os 237 títulos N1↔PubMed + leitura de 14 abstracts [AT] (efetch) + amostragem cruzada Fase 1 (13 abstracts) — **0 troca de nomes detectada** nos 41 aprofundamentos.
4. **G2/G3 estruturais**: 257 âncoras contra o corpo; 257 vínculos contra N1 (claim_id, refs, status); 81 claims contra corpus (78 chaves de claim + `_ANCORAS_GPM`); 83 itens da Lista Canônica; 49 refs da reconciliação item a item.
5. **Normativos aplicados**: Prompt 4.2 / Molde GPM / Processo v2.1 (com a nota de que o processo declarado do lote é v2.6 — AUD-037), Contrato (P12/P19/P20/R04/R06), Auditor-Mestre (20 regras absolutas).
6. **Distinção exigida**: cada item é classificado como *confirmado por evidência*, *não conformidade* ou **não verificável com os materiais fornecidos** (§7).

---

## 3. CONDIÇÕES BLOQUEANTES DA FASE 1 — SITUAÇÃO NO ARTEFATO CANÔNICO

| # | Condição (Fase 1) | Situação | Evidência |
|---|---|---|---|
| 1 | Corrigir AUD-001 (Hannestad+LPS) e AUD-002 (Parrott+espécie), com log, nunca silencioso | **ATENDIDA no corpo canônico** | 0 ocorrência de "Hannestad" com desafio LPS: a citação vigente é "não se eleva em depressão leve–moderada (Hannestad et al., 2013)[EC; humano, evidência negativa]" — enquadramento correto do PET transversal. 0 ocorrência de "Parrott" com enquadramento humano/pós-morte: citação única "no território pré-clínico…(Parrott et al., 2016)[ML; camundongo] [APENAS PRÉ-CLÍNICO]". **Propagação ao Briefing: NÃO VERIFICÁVEL** — o Briefing no lote é a versão pré-correção (AUD-048). |
| 2 | Ratificar por escrito a exceção de ordem invertida (AUD-003) | **NÃO ATENDIDA / NÃO ENCONTRADA** | Nenhum documento do lote registra a ratificação. O Briefing mantém o cabeçalho "ordem invertida a pedido". Ausência de registro = a exceção segue informal. |
| 3 | G1 oficial em sessão separada, com artefatos próprios do Ato 1 (AUD-004/016) | **SUBSTANTIVAMENTE ATENDIDA** | `corpus_pubmed.json` + `log_de_busca.txt` + `b1_anchormap.json` agora fornecidos; manifesto declara "G1 por ferramenta (eutils)"; N1 traz `g1_metodo: eutils_automatico`; REGISTRO DE AUDITORIA 2026-09-11 (5ª rodada perícia externa) documenta re-ancoragem independente. Ressalva: não há declaração explícita "sessão separada da geração" — a independência é inferida da trilha, não declarada. |
| 4 | Tratamento da herança v3.1 (Lista Canônica formal ou "V"=candidata comum) + versionamento (AUD-005) | **SUBSTANTIVAMENTE ATENDIDA** | Lista Canônica v1.1 (83 itens, 2026-08-27) fornecida e auditada contra o GPM; [AT] 2026-09-08 registrado como atualização P-7 (versão N+1, histórico preservado no manifesto); v4 preservada em `antigos/historico/` (referenciado; arquivo não fornecido). |
| 5 | Fornecer o lote completo para auditoria integral + veredito final único | **ATENDIDA** | Este relatório. |

---

## 4. PORTÕES (re-execução independente)

### 4.1 G1 — integridade de referências: **PASSOU**
- **237/237 PMIDs resolvem na PubMed** (esummary, 2026-09-11, sessão do auditor). **Zero referência inventada** — o requisito mais duro do canonicado.
- Títulos: 24/237 diferem do PubMed — todos por truncamento no campo N1, glifos (α/alpha, ¹¹C), itálicos ou subtítulo abreviado; **0 caso de paper errado para o autor/ano citado**. (AUD-039, MENOR.)
- Ano: 0 divergência entre o ano do campo `revista_ano` e o pubdate do PubMed (incluindo os pares ambíguos Köhler 2017/2018, Attwells 2019/2020 — consistentes).
- A reconciliação do insumo [AT] (2026-09-08) é, por si, um excelente gate G1: detectou 5 PMIDs falsos do insumo Consensus (incl. o exemplar 1110775→Waldron 1975), 2 trocas de autoria/direção (o "Ng et al." = Mac Giollabhui 2021 tratado como âncora **NEG**, o "Herzog 2024"=2025) e 5 refs não localizadas → `[G1]`. Nenhum dos 5 PMIDs falsos ou 2 erros de direção migrou para a v4.1 (verificado por PMID contra N1).

### 4.2 G2 — elegibilidade e âncoras: **PASSOU (com governança pendente)**
- 257/257 `trecho_ancora` presentes no corpo; 161 com divergência apenas de formato (espaços/cabeçalhos) — aderente ao registro da 5ª rodada (100% literalidade após re-ancoragem).
- `redirecionado_clinico` (20 vínculos: Köhler×4, Osimo×3, Virtanen×2, Dowlati, Howren, Goldsmith, Jarkas, Comai, Sublette, Arora, Gulen, Belge, Więdłocha, Tobinick): **conforme o desenho do processo** — "PMID puramente associativo/epidemiológico…nunca é rejeitado…vai para `redirecionados_modulo_clinico`" (Processo, lin. 177; enumeração de status lin. 50). As afirmações correspondentes no corpo mantêm enquadramento mecanístico (descrição da associação, nunca conduta) e o BLOCO_11 carrega a ressalva obrigatória de que a decisão pertence às bibliotecas operacionais. **Sem achado** (AUD-047, OBSERVAÇÃO — a trilha clínica precisa existir como destino: o claim B1.SM02.007, §5).
- Desvios de schema (AUD-036): `forca_evidencia` vazio em 233/237; `status_auditoria` no lugar de `g3_sustenta`; **30 vínculos VINC_B1V2_* (Rodada 4) sem `claim_id` e sem `achado_referencia`** — G3 registrado só em nível de lote (`g3_por`); 19 vínculos `PARCIALMENTE_CONFIRMADO` **sem `g3_nota`** — o "parcial" não é documentado.

### 4.3 G3 — suporte das afirmações (re-verificação independente do lote [AT])
Abstracts recuperados nesta sessão (efetch): 42034206, 41957656, 36226319, 41588410, 36231075, 31195092, 40036275, 31427752, 30797959, 34877938, 39595067, 39089535, 28263786, 34847455.

**CONFIRMADO pelo abstract:**
- Eggerstorfer 2022: "∼18% increase" (8 estudos PET, 238 TDM/164 HC) = número do corpo, exato ✓.
- Li 2026: case-control 63+63 TNF-α plasma em 1º episódio drug-naïve + meta-análise ✓ (tags de desenho corretas).
- Wang 2019 e Liu 2020b: meta-análises ✓ (tag [MA] correta).
- Barzon 2026a (42034206): título direto — inflamação periférica reduz influxo do traçador TSPO ✓ (claim de confundidor transportado).
- Barzon 2026b (41957656): fingerprinting de rede ✓ (tag "fronteira" honesta).
- Li 2021: modelo de depressão em camundongo, piroptose NLRP3 ✓.
- Jarkas 2024: meta-análise de diferenças sexuais ✓.
- Enache 2019: "Abnormalities in CSF and PET inflammatory markers were not correlated with their counterparts in peripheral blood" — a claim central ("parcialmente independentes dos periféricos") é **diretamente suportada** ✓ (com ressalva de escopo — AUD-030).
- Böttcher 2020 / Nagy 2020 / Mac Giollabhui 2021: tratamento **NEG** preservado no corpo ("não exibe fenótipo pró-inflamatório clássico"; "weakening" longitudinal, não confirmação temporal) — o anti-nivelamento exigido pela reconciliação foi cumprido ✓.
- Holmes 2018 (28939116): título PubMed = "Elevated Translocator Protein in Anterior Cingulate in Major Depression and a Role for Inflammation in Suicidal Thinking" — claim do corpo 5.3 [VERIFICADO] exato ✓.
- Osimo 2020 / Dowlati 2010: títulos confirmados ✓; "elevação é de um SUBGRUPO e não universal" coerente com o próprio título do Osimo 2020 ("mean differences and **variability**") ✓.
- Kaufmann 2017 (28263786, Brain Behav Immun 2017): abstract confirma revisão clínico–pré-clínica ligando montagem do NLRP3/IL-1β a modelos de estresse crônico e pacientes TDM ✓ (o detalhe "pós-morte" específico não é verificável pelo abstract — revisão; sem achado).

**ERROS CONFIRMADOS (GRAVE) — ver §5, AUD-026/027.**

### 4.4 Hard-fails terminológicos/estruturais: **LIMPOS**
- 0 PMID/DOI no corpo (a única menção à palavra "PMID" é na nota metodológica do cabeçalho, sem valor identificado).
- 0 "grade" A–D (o único hit é "low-grade inflammation" — termo científico legítimo).
- 0 `[PENDENTE]`; 0 `[G1]` residual (as lacunas são declaradas em CONTROVÉRSIAS/LACUNAS e BLOCO_10/11/12, sem cravar âncora fictícia).
- P16 (neurogênese): presente apenas como efeito indireto/cross-ref a B16 ✓.
- BLOCO_12: nota de fechamento correta — "arquétipos didáticos…não categorias mutuamente exclusivas nem rótulos diagnósticos…qualquer decisão pertence às bibliotecas operacionais" ✓.
- P20 no corpo: sem doses/protocolos/algoritmos; **uma exceção** — a TABELA DE EVIDÊNCIAS traz o corte numérico "PCR>3" (AUD-031).

---

## 5. ACHADOS (registro contínuo — fase 2)

### GRAVE

**AUD-026 — GRAVE — Alma de claim→referência invertida: quinurenina (Almulla 2022, [AT])**
- **Local:** §2.10 [AT 2026-09-08], BLOCO02.010.
- **Texto do corpo:** "meta-análise de catabolitos do triptofano no episódio depressivo atual documenta alterações de TRYCATs — **redução de quinurenina** e das razões neuroprotetoras/neurotóxicas — sobretudo nos subtipos melancólico, psicótico e na ideação suicida (Almulla et al., 2022)[MA; humano]".
- **Evidência (abstract, 36231075):** "Severe patients showed significant lower (p < 0.0001) TRP (SMD = -0.517)… **Kynurenine (KYN) levels were unaltered** in severe MDD/BD phenotypes, while the KYN/TRP ratio showed a significant increase only in patients with psychotic features (SMD = 0.224). Quinolinic acid (QA) was significantly increased (SMD = 0.358) and kynurenic acid (KA) significantly decreased (SMD = -0.260)".
- **Problema:** a direção do metabólito nomeado está invertida/errada: a quinurenina **não se alterou**; o que se reduziu foi o TRP e o ácido quinurênico (KA), e a razão KYN/TRP **aumentou** no subtipo psicótico. A quinurenina é exatamente o marcador central da biblioteca (BLOCO_05.001, KYN/TRP). O resto da frase (TRYCATs alterados; subtipos melancólico/psicótico/suicida; desequilíbrio neuroprotetor/neurotóxico) é suportado.
- **Por que GRAVE:** erro de direção em biomarcador, confirmado por abstract, numa afirmação do lote [AT] — o ponto exato em que o risco de "atualização mal re-verificada" é máximo; RAG downstream afirmaria "quinurenina reduzida no episódio depressivo (meta 2022)" — falso.
- **Correção:** reformular para "TRP e ácido quinurênico reduzidos, ácido quinolínico aumentado, quinurenina inalterada; razão KYN/TRP aumentada apenas no subtipo psicótico" — ou re-âncorar. Nunca correção silenciosa (log de substituição).
- **Efeito colateral a conferir:** o §5.2 descreve KYN/TRP como índice de "inflamação desvia triptofano para quinurenina e eleva a razão"; com a direção real desta meta (TRP↓), a explicação mecanística da elevação da razão deve ser lida como "denominador rebaixado" ao menos neste conjunto.

**AUD-027 — GRAVE — Seletividade do achado apagada (Comai 2022, [VERIFICADO])**
- **Local:** §5.2 (BLOCO05.001).
- **Texto do corpo:** "Em pacientes **bipolares e depressivos**, níveis de citocinas e a razão KYN/TRP associam-se seletivamente a alterações de substância branca (Comai et al., 2022)[EC; humano] [VERIFICADO]".
- **Evidência (título PubMed, 34847455):** "Selective association of cytokine levels and kynurenine/tryptophan ratio with white matter microstructure in **bipolar but not unipolar** depression".
- **Problema:** a seletividade (bipolar **e não** unipolar) é a própria claim do paper; a frase como redigida afirma associação em ambos os grupos — o "seletivamente" do texto vira ornamentação em vez de conteúdo. A afirmação carrega selo [VERIFICADO] — o G3 da pipeline não detectou.
- **Por que GRAVE:** um RAG downstream concluiria que o biomarcador KYN/TRP associa-se a substância branca na depressão unipolar — contradiz o paper-âncora.
- **Correção:** "…associam-se a alterações de substância branca **em depressão bipolar (e não em unipolar)** (Comai et al., 2022)"; revisar o status G3 do vínculo (VINC correspondente a Comai) para registrar a limitação.

### MODERADO

**AUD-028 — Gavril 2024 [AT]: rotulagem de desenho errada.**
§5.1: "(Gavril et al., 2024)[OB; **revisão**]". O 39595067 é **estudo original** case-control (92 TDM vs 76 controles; IL-1α/IL-6/TNF-α elevados; correlações HAM-D, ex.: log IL-1α em homens r=0,355). O N1 mesmo lista `desenho_estudo: Journal Article` — a tag do corpo contradiz o próprio N1. A claim ("valor preditivo isolado permanece baixo") é defensável pelos tamanhos de efeito modestos do abstract, mas a origem do erro está no insumo: a reconciliação também a classifica como "revisão" (AUD-043). **Correção:** trocar por `[OB; estudo original, humano]`.

**AUD-029 — Wijesinghe 2025 [AT]: resultado positivo lido como "questão aberta".**
§5.4: "a validação pós-morte do PET como biomarcador microglial **permanece questão aberta** mesmo em condição demonstradora neurodegenerativa (Wijesinghe et al., 2025)[EC; humano, PSP como demonstradora] [EXTRAPOLADO: PSP→TDM]". O paper demonstrou **correlação positiva** (n=8 PSP) entre o BP do ¹¹C-PK11195 in vivo e a carga de micróglia CD68+/TSPO pós-morte. A formulação do corpo omite a direção encontrada; o enquadramento conservador e a tag [EXTRAPOLADO: PSP→TDM] são honestos, mas a afirmação como lida descreve o oposto do resultado do paper (positivo, pequena amostra). **Correção:** "na única validação pós-morte até agora (n=8, PSP), o traçador in vivo correlacionou-se com carga microglial pós-morte — evidência positiva de pequena amostra, extrapolação para TDM pendente".

**AUD-030 — Enache 2019 [AT]: escopo da meta-análise sobreafirmado.**
§5.6 [AT]: "meta-análise **conjunta de líquor, PET e pós-morte** mostra que os marcadores centrais…são parcialmente independentes dos periféricos". A meta do Enache 2019 cobriu **apenas LCR + PET** (69 estudos); o pós-morte foi tratado como narrativa (2 estudos com marcadores microgliais ↑ / 4 sem mudança). A claim central (independência parcial) é suportada; o escopo metodológico não. **Correção:** "meta-análise de marcadores em LCR e PET (com revisão do pós-morte)".

**AUD-031 — "27% / OR 1,46 / PCR>3": dependência inter-artefato + corte numérico (P20).**
§11.1 (BLOCO11.001) e TABELA DE EVIDÊNCIAS: "Aproximadamente **27%** dos pacientes com depressão apresentam PCR-us elevada…razão de chances **~1,46**…(achado epidemiológico da **trilha SM**…)". A Lista Canônica formaliza: claim B1.MEC.BLOCO11.001 → `claim_id_clinico_relacionado: B1.SM02.007`, `referencia_cruzada_obrigatoria: true`. O artefato da trilha SM (âncora primária do 27%/OR) **não está no lote** → **não verificável com os materiais fornecidos** (a origem está declarada no corpo e na Lista — boa prática). Além disso, a TABELA DE EVIDÊNCIAS traz o **corte numérico "PCR>3"** — violação de P20 (valores de corte residem em C-LAB; o próprio §11.1 faz o deferimento correto, a tabela não). **Correção:** (a) remover "PCR>3" da tabela → "acima do limiar de baixo grau (módulo C-LAB)"; (b) registrar a dependência B1.SM02.007 no manifesto como referência cruzada obrigatória pendente.

**AUD-032 — 17 refs N1 sem vínculo; 1 delas nunca citada no corpo.**
16 refs citadas no corpo (linha de âncora + prosa) **sem nenhum vínculo N2**: BIANCHI_2007, BOATO_2011, FRANKLIN_2018, HAN_2023, HUANG_2024, LAWRENCE_2023, LI_2017, LI_2025b, MEHTA_2020b, NOAH_2021, POLETTI_2024, SUGIMOTO_2022, ZDILAR_2000, ZENARO_2017, ZHOU_2024, ZHOU_2025 — as frases do corpo que as citam ficaram **sem registro de G3 em nível de claim**. E **ANNETT_2020** (FKBP/sinalização inflamatória) não aparece em nenhum lugar do corpo (só no apêndice): referência catalogada e **jamais usada** — hard-fail "referência isolada" do Prompt 4.2. **Correção:** criar vínculos (claim_id) para as 16 ou declará-las referências de contexto; ANNETT_2020: citar com vínculo ou remover de N1.

**AUD-033 — Proveniência de busca incompleta (42 refs originais sem trilha).**
Dos 237 PMIDs de N1, **89 não aparecem em nenhum artefato de busca fornecido**: 47 são [AT] (trilha própria no artefato de auditoria da matriz [AT], não fornecido — aceitável por desenho, AUD-048) e **42 são BUSCA_FERRAMENTA** (origem Ato 1 original) ausentes tanto do corpus por claim (761 PMIDs) quanto do log (622 PMIDs, top-10/claim). Para essas 42, a query que as recuperou, a data e a posição no ranking **não são auditáveis com os materiais fornecidos**. Existência e título conferidos (G1 ✓) — a falha é de trilha, não de integridade. **Correção:** fornecer o log de busca completo (não o resumo top-10) ou o registro das buscas complementares.

**AUD-034 — Integração [AT] incompleta vs. a própria reconciliação aprovada.**
A reconciliação (2026-09-08, status "veredito para aprovação") propõe 49 refs para AGREGA; **36 foram incorporadas e 13 não entraram sem registro de decisão de rejeição**:
- **sub-bloco suicidalidade (BLOCO_06) inteiro ausente**: Bryleva & Brundin 2017 (26820800), Bryleva 2017 (27221623, "opcional"), Behera 2026 (42525506), Herzog 2025 (39504032);
- **fundamentos**: Müller & Schwarz 2007 (17457312 — "paper FUNDADOR…a v3.1 usa o argumento sem citar a origem"), Dantzer & Walker 2014 (24633997 — "contraponto cético canônico…evita leitura só-pro"), Bay-Richter 2015 (25124710);
- **TSPO**: Richards 2018 (29971587, ↑TSPO em TDM **não medicado** — "controla o confundidor farmacológico"), Setiawan 2018 (29496589, duração);
- **ponte BDNF↔NLRP3 (BLOCO_09)**: Erdem Ş 2026 (41752782), Erdem M 2025 (40638969);
- McKenzie 2018 (29895691) — marcado "opcional" na reconciliação (aceitável).
O manifesto declara "[AT]…+ 37 novas refs"; verificado: 36. Nenhuma das 13 omissões consta na lista "NÃO AGREGA" (§4) da reconciliação. **Correção:** decisão documentada por item (incorporar agora / rejeitar com motivo / declarar lacuna) — especialmente o sub-bloco suicidalidade, que o corpo cita hoje apenas por Sublette 2011 e Holmes 2018.

**AUD-035 — Lista Canônica não atualizada após a incorporação.**
Os 83 itens seguem todos `status: em_busca`; **zero** marcas `usado_em_biblioteca: sim` (Passo 13 do processo: "Marcar, na Lista Canônica correspondente, os claims incorporados"). A trilha seed→biblioteca está romuida: não se pode saber pela Lista quais das 81 claims da biblioteca derivam de cada item. **Correção:** atualizar statuses + `usado_em_biblioteca`.

**AUD-036 — Status G3 "parcial" sem justificação + bloco V2 sem mapeamento de claim.**
19 vínculos `PARCIALMENTE_CONFIRMADO` (Dantzer 2006, Rajesh 2022, Chiu 2013, Picca 2017, Fiore 2023, Shirakawa 2018, Tobinick 2009, Mariani 2022, Chen 2025, Menard 2017, Souza 2017, Arora 2019, Cho 2024, Brann 2022, Goshen 2009 + 4 do bloco V2: Lee 2025, Cosco 2019, Quagliato 2018, Parsons 2021) têm **`g3_nota` vazio e `achado_referencia` vazio** — o que foi confirmado e o que ficou parcial está irrecuperável. Adicionalmente, os **30 vínculos VINC_B1V2_* (Rodada 4)** têm `claim_id` e `achado_referencia` vazios; o G3 consta apenas em lote (`g3_por: IA_G3_rodada_auditoria_cientifica (abstract efetch relido, 3 perguntas G3)`). O trabalho pode ter sido feito — o registro, não. **Correção:** preencher `g3_nota` (o que está parcial e por quê) ou reclassificar para CONFIRMADO/NAO_SUSTENTA; mapear claim_id nos 30 vínculos V2.

**AUD-037 — Manifesto dessincronizado pós-[AT] e artefatos referenciados ausentes.**
`pmids_total: 184` (real: 237) e `meta_analises: 6` (real: 33) — valores do estado pré-[AT]; manifesto v2.5 com `pipeline_versao_geracao: 2.6` (o kit normativo é v2.1 — o salto de versão não está documentado no lote); referências a `producao/…`, `decisoes_B1.md`, `antigos/historico/…`, `CHANGELOG_GERAL.md` — **nenhum fornecido**. O manifesto é a fonte de verdade declarada do lote; com dois campos numéricos obsoletos, a fonte dupla com o corpo (237) fica ambígua. **Correção:** sincronizar manifesto (237/33), documentar o salto v2.1→v2.6 (ou declarar a norma aplicada), e incluir ou excluir explicitamente os artefatos de trilha.

**AUD-038 — Hafizi: ano de citação errado + afirmação falsa sobre o abstract (mitigada por disclaimer).**
§2.16: "(Hafizi et al., 2005)[OB; revisão, SEM abstract no corpus — PENDENTE DE FULL-TEXT, não serve de lastro próprio]". PubMed: 17639827 = "Interferon-induced depression: mechanisms and management", *BJ Hosp Med*, **2007 Jun** — o ID N1 (`REF_HAFIZI_2005`) e o ano da citação (2005) estão errados (2005→2007), e o "SEM abstract no corpus" é falso (o abstract existe e resolve por efetch — o NAO_LOCALIZADO/TRIADO foi artefato de triagem). Mitigação real: o corpo já declara "não serve de lastro próprio", então a citação não carrega claim. **Correção:** corrigir ano (2007), remover o falso "SEM abstract" (o registro N1 TRIADO/NLO deve ser atualizado).

### MENOR

**AUD-039 — Fidelidade de título N1 (24/237).** Truncamentos ("Cyclooxygenase-2 in synaptic signaling." etc.), glifos (α→alpha, "11C"), subtítulos abreviados; 0 troca de paper. O campo N1 não é fonte canônica de fidelidade — o título PubMed é.
**AUD-040 — Sublette 2011 sobreafirmado.** §5.2: "a razão KYN/TRP é o biomarcador com a **melhor especificidade** para ideação suicida (Sublette et al., 2011)". O paper (21605657): "Plasma **kynurenine** levels are elevated in suicide attempters with MDD". A direção (KYN↑ em tentadores) é suportada; o enquadramento "razão KYN/TRP" + "melhor especificidade" não é verificável na âncora.
**AUD-041 — Citação com parênteses vazios.** §7.2: "alivia comportamento depressivo em rato **()**[ML]" — autor/ano ausente (recuperável pela âncora NEK7_2025). Defeito de formato.
**AUD-042 — Bloco METADADOS (rodapé) obsoleto.** `corte_literatura: 2026-05` (vs. cabeçalho: corte 2026-09-04 + [AT] 2026-09-08 + alterações 09-10/11); `clinical_domains` inclui `decisao_terapeutica`; `semantic_keywords` inclui "**NAC, cetamina** inflamatória" — conteúdo farmacológico em bibliotecas de mecanismo (P20) e um segundo conjunto de palavras-chave de RAG divergente do do cabeçalho (linha 17). Fonte única violada dentro do próprio arquivo.
**AUD-043 — Erros internos da reconciliação (insumo, não do artefato canônico).** "Kaufmann 2016" (ano canônico 2017, BBI); "Elgellaie 2023 — 37070103" (typo: 37070103 resolve para corrigendum em EClinicalMedicine; o PMID correto 37070163 está em N1 ✓); "Gavril 2024 · revisão" (origem do AUD-028). Relevantes para a qualidade do insumo [AT] e para auditorias futuras.
**AUD-044 — Checagem de fidelidade registrada cobre 184 citações (pré-[AT]).** Cabeçalho: "checagem de troca de nomes (autor↔referência, 184 citações) sem erros encontrados nesta rodada" (Rodada 4). Após o [AT] (237 refs), a 5ª rodada re-extraiu as 257 âncoras (literalidade 100%) — o que compensa parcialmente — mas não há registro explícito de re-fidelidade autor↔referência sobre as 53 refs novas. Nesta auditoria: 0 troca detectada em 41 aprofundamentos (Fase 1 + 14 [AT] + 13 reconciliação).
**AUD-045 — TABELA DE EVIDÊNCIAS, linha agregada.** "Dowlati; Howren; Goldsmith; Osimo; 82 estudos" — a agregação dos 4 estudos (n total) não é itemizada; o "~27% com PCR>3 (OR~1,46)" aparece na coluna de achados dessa linha, ofuscando a origem (trilha SM — ver AUD-031).
**AUD-046 — Kaufmann 2017 (título/jornal).** N1/áncora consistentes (BBI 2017); a reconciliação escreveu "2016" (ver AUD-043). Sem impacto no canônico.
**AUD-047 — (OBSERVAÇÃO) 20 `redirecionado_clinico`.** Conforme desenho (Processo lin. 50/177). Ressalva administrativa: o destino (módulo clínico B1.SM) não está no lote — os redirecionamentos dependem de uma trilha viva (o claim B1.SM02.007 na Lista Canônica sugere que existe).
**AUD-048 — (OBSERVAÇÃO) Artefatos externos não fornecidos (afeta escopo, não mérito).** Briefing/GPM pós-correção (propagação da cond. 1); registro de ratificação da ordem invertida (cond. 2); trilha de auditoria [AT] (`RELATORIO_AUDITORIA_MATRIZ_B1.md`, 4 falsos positivos rejeitados, 19 exclusões de escopo); `producao/05_reparo_AT02_AT13_2026-09-11.json`; `antigos/historico/v4_…` (preservação bit a bit declarada); `CHANGELOG_GERAL.md`; `decisoes_B1.md`; lista dos 59 vínculos de alto-risco; full-texts (a auditoria G3 opera em abstract — escopo formal do gate).

---

## 6. PONTOS FORTES CONFIRMADOS (o que sustenta o canonicado)

1. **Zero referência inventada** — 237/237 re-verificados independentemente; o lote [AT] chegou após uma reconciliação que já havia expurgado 5 PMIDs falsos e 2 trocas de autoria/direção do insumo, e nenhum deles migrou.
2. **Correções da Fase 1 efetivas e completas**: 0 resíduo de "Hannestad+LPS" e de "Parrott+humano"; as duas regras fundadoras (LPS-negativo como evidência negativa transversal; animal marcado [APENAS PRÉ-CLÍNICO]) estão aplicadas.
3. **Anti-nivelamento de qualidade rara**: blocos negativos bem ancorados (Hannestad, Böttcher, Nagy, Mac Giollabhui longitudinal NEG, Schubert "modesto", Eggerstorfer ~18%), regra "periferia ≠ centro" reafirmada com âncora meta-analítica, M1/M2 declarado falso com contra-evidência humana, BLOCO_12 como "arquétipos didáticos" com veto explícito a rótulo diagnóstico, causalidade escrita como NÃO fechada.
4. **Sinalizadores disciplinares**: 72 [VERIFICADO], 117 [OB], 64 [EXTRAPOLADO] + 135 [EXT], 10 [APENAS PRÉ-CLÍNICO] + 46 [PRÉ-CLÍNICO] — a separação humano/animal/extrapolação está efetivamente operante; 0 [G1] e 0 [PENDENTE] residual.
5. **G2 íntegro**: 257/257 âncoras; o registro de 5ª rodada (re-ancoragem, 100% literalidade) é aderente ao que esta auditoria mediu.
6. **Honestidade governamental do manifesto**: natureza do sistema declarada (G1 ferramenta; G2/G3 por IA revisora; **revisão cega humana pendente — fila de 59 vínculos de alto-risco**); [AT] registrado como P-7 com versão N+1 e histórico.
7. **Fidelidade de fase 1**: 148/161 âncoras do GPM sem divergência + 13 abstracts; das 7 correções materiais do insumo, todas confirmadas na v4.1.

---

## 7. NÃO VERIFICÁVEL COM OS MATERIAIS FORNECIDOS (declaração explícita)

| Item | Por quê |
|---|---|
| Âncora primária do "27%/OR 1,46" (claim B1.SM02.007) | Artefato da trilha clínica (B1.SM) não está no lote |
| Trilha de auditoria da matriz [AT] (rejeições de falsos positivos; 19 exclusões de escopo) | `RELATORIO_AUDITORIA_MATRIZ_B1.md` / `producao/…` referenciados, não fornecidos |
| Proveniência das 42 refs BUSCA_FERRAMENTA fora do corpus/log (AUD-033) | Log fornecido é resumo top-10/claim; buscas complementares não registradas no lote |
| Preservação bit a bit da v4 (`antigos/historico/…`) e `CHANGELOG_GERAL.md` | Referenciados, não fornecidos |
| Lista dos 59 vínculos de alto-risco pendentes de revisão cega | Declaração do manifesto; lista em artefato externo |
| Propagação das correções ao Briefing/GPM (cond. 1) | Lote contém a versão pré-correção do Briefing |
| Ratificação por escrito da ordem invertida (cond. 2) | Nenhum registro no lote |
| Resultados por subtipo do Almulla 2022 (full-text) | A auditoria G3 opera em abstract; o achado AUD-026 assenta-se no abstract (escopo formal) |

---

## 8. CONDIÇÕES DE CORREÇÃO (obrigatórias — antes da próxima rodada [AT] ou nova publicação)

**Imediatas (GRAVE — bloqueiam a próxima [AT]):**
1. **R1 (AUD-026):** reformular a frase do Almulla 2022 no §2.10 com a direção real (KYN inalterado; TRP e KA reduzidos; QA aumentado; KYN/TRP↑ só no psicótico) — com log de substituição.
2. **R2 (AUD-027):** reformular a frase do Comai 2022 no §5.2 ("bipolar, **não** unipolar") e atualizar o vínculo G3 correspondente.

**Na mesma manutenção (MODERADO):**
3. **R3 (AUD-036):** justificar ou reclassificar os 19 `PARCIALMENTE_CONFIRMADO` (preencher `g3_nota`); mapear `claim_id`/`achado` nos 30 vínculos V2.
4. **R4 (AUD-035):** atualizar a Lista Canônica (statuses + `usado_em_biblioteca: sim`).
5. **R5 (AUD-034):** registro de decisão item a item para as 13 refs omcidas — com decisão expressa sobre o sub-bloco suicidalidade (incorporar / declarar lacuna).
6. **R6 (AUD-037/AUD-042):** sincronizar o manifesto (237/33) e alinhar o bloco METADADOS do rodapé (corte, `clinical_domains` sem `decisao_terapeutica`, keywords sem fármaco) — fonte única.
7. **R7 (AUD-031):** remover o corte "PCR>3" da TABELA DE EVIDÊNCIAS (deferir ao C-LAB); registrar a referência cruzada B1.SM02.007.
8. **R8 (AUD-032):** ANNETT_2020 — citar com vínculo ou remover de N1; criar vínculos (ou declarar contexto) para as 16 refs órfãs.
9. **R10:** concluir a revisão cega humana da fila de 59 vínculos (ou declarar o status canônico como **provisório** até o fechamento — esta é a própria ressalva do pipeline).

**Recomendadas (MENOR — mesma rodada, sem bloqueio):**
10. **R11:** Gavril→`[OB; estudo original]`; Wijesinghe→enunciar o resultado positivo (n=8, PSP); Enache→"meta LCR+PET (+revisão do pós-morte)"; Hafizi→2007 e remover "SEM abstract"; §7.2→preencher a citação vazia; Sublette 2011→"quinurenina plasmática elevada em tentadores" (sem "melhor especificidade").
11. **R12:** ratificação por escrito da ordem invertida (cond. 2 da Fase 1) e documentação do salto Processo v2.1→v2.6.
12. **R13:** fornecer o log de busca completo (não-top-10) e a trilha [AT] para fechamento do AUD-033/048.

---

## 9. VEREDITO FINAL (reiterado e assinado)

**APROVADA COM RESSALVAS.**

O artefato `B1 NEUROINFLAMAÇÃO V4.1 CANONICA` atinge o status canônico **condicional**: a integridade referencial (0 falsas/237), a integridade estrutural (257/257 âncoras; 0 hard-fails), a disciplina de sinalização (espécie/extrapolação/pré-clínico) e o anti-nivelamento estão confirmados por re-execução independente; as duas falhas GRAVE da Fase 1 foram corrigidas sem resíduo. As ressalvas que impedem o veredito limpo são: **(i)** dois novos erros de claim→referência confirmados por abstract (AUD-026 quinurenina/Almulla; AUD-027 seletividade/Comai) — localizados, exatos e corrigíveis por reformulação, não regeneração; **(ii)** lacunas de governança/traçabilidade (status G3 parciais sem justificação, Lista Canônica desatualizada, manifesto dessincronizado, 13 omissões [AT] sem registro, 17 refs sem vínculo, 42 refs sem trilha de busca); **(iii)** a revisão cega humana de 59 vínculos de alto-risco pendente — ressalva declarada pelo próprio pipeline, que permanece em aberto.

Nenhum achado deste relatório exige regeneração da biblioteca: todas as correções são pontuais, com log de substituição, no padrão MAPEAR_VOCABULARIO. A aplicação das R1–R2 antes de qualquer nova rodada [AT] e das R3–R10 na próxima manutenção são as condições de manutenção do status canônico.

---
*Auditor-Mestre — sessão independente da geração. Verificação externa: PubMed E-utilities (237 esummary + 14 efetch de abstracts + esummary pontuais), 2026-09-11. Esta auditoria não substitui o Portão G1→G2→G3 oficial nem a revisão cega humana pendente; constitui evidência de auditoria integral do lote canônico e emite o veredito final único solicitado.*
