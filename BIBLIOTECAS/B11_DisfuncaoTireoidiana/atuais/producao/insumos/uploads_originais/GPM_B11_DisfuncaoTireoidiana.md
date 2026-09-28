# GPM B11 — DISFUNÇÃO TIREOIDIANA EM ANSIEDADE E DEPRESSÃO — MOLDE v2.0
### Módulo da arquitetura neuropsiquiátrica · Rodada 0 · 2026-09-09
> **Status:** GPM reconstruído sobre a Matriz Canônica B11 (10 claims B11.SM01–SM10; "APROVADO_COM_RESSALVAS") + insumo "Artigos cientificos do mecanismo B11 disfunção tireoidiana 08.09.26" (133 refs; 114 DOI→PMID auditados). 14 âncoras → 14 PMIDs verificados (b11_anchormap.json) — os 14 PMIDs da matriz foram revalidados 1 a 1 no PubMed, incluindo a **correção editorial** de Soheili-Nezhad (PMID no briefing §4) preservada como metadado. Corpo limpo (zero PMID/DOI). Trinca: GPM + BRIEFING_B11_DISFUNCAO_TIREOIDIANA_RODADA0.md + CHECKLIST_SANIDADE_GPM_B11.md.

---

## MÓDULO 00 — METADADOS, REGRAS FUNDADORAS, ESCOPO E FRONTEIRAS
[REF_MODULO_00: Roa Dueñas, 2024; Siegmann, 2018; Wildisen, 2020; Bode, 2022; Bauer, 2021]

**ID do mecanismo (B11):** alterações da função do eixo hipotálamo–hipófise–tireoide (HPT) e da autoimunidade tireoidiana associadas a sintomas/transtornos depressivos e ansiosos, com **magnitudes pequenas, direção variável por marcador (TSH/FT4/FT3), relações possivelmente não lineares e causalidade em geral não estabelecida**. A relação pode ser bidirecional (transtorno → tireoide) e envolver mecanismos autoimunes/genéticos além dos níveis hormonais.

**REGRAS FUNDADORAS:**
1. **Associação ≠ causalidade:** o estudo-âncora populacional explicitamente reconhece causalidade reversa possível e efeitos pequenos (Roa Dueñas, 2024).
2. **"Hipotireoidismo subclínico causa depressão" é NÃO registrável** — meta-análises compostas n.s. (Zhao, 2018; Tang, 2019) e grandes coortes/IPD negativas (Kim, 2018; Wildisen, 2020; Airaksinen, 2021) → claim canônico = inconsistência.
3. **Tireoidite autoimune (AIT):** associação robusta com depressão/ansiedade (OR elevados, heterogeneidade alta) — mecanismo possivelmente ALÉM dos hormônios circulantes; proibido escrever "Hashimoto causa depressão" (Siegmann, 2018).
4. **Genética compartilhada ≠ causalidade clínica individual** (Soheili-Nezhad, 2023; com correção editorial publicada, preservada como metadado bibliográfico no briefing §4).
5. **Não-linearidade ≠ faixa ótima de TSH:** pontos de inflexão observacionais não viram alvo terapêutico (Roa Dueñas, 2024; Ma, 2024).
6. **T3/T4 adjuvante ≠ tratar toda depressão como tireoidiana:** LT3 com evidência de aceleração de resposta/resistente é contexto específico (Bauer, 2021).
7. **Bidirecionalidade obrigatória no modelo:** depressão/ansiedade podem preceder doença tireoidiana (Fan, 2024).
8. **Evidência NEGATIVA é conteúdo canônico** (Wildisen, 2020; Airaksinen, 2021; Kim, 2018) — registrada com o mesmo status das positivas.
9. **Números de efeito (OR/HR/SMD) do insumo = alegação a confirmar em rodada de quantificação** — nenhum copiado.
10. **Multi-tag permitida** (CORE_ASSOCIATION + CLÍNICO; CONTROVERSIAL_CORE).

**Dicionário mínimo:** HPT; TSH/FT4/FT3; SCH (hipotireoidismo subclínico); AIT (tireoidite autoimune/Hashimoto); anti-TPO; IPD; MR; LT3/LT4 (liotironina/levotiroxina); relação em U (FT4×evento depressivo).

**Fronteiras:** iodo como micronutriente → B8 (B8.10) — ponte cruzada; HPA/cortisol → B2; neuroinflamação autoimune → B1; genética → M04; bipolar/esquizofrenia isoladas → EXC (B11.11).

**Lacunas [G1] do M00:** (a) revisões clínicas gerais do insumo sem papel de âncora (ver §6); (b) engenharia reverse-T3 sem âncora; (c) B11 × B8 (iodo) sem âncora cruzada; (d) estudos de desfecho de LT4 em SCH×depressão (TIRA/ThyroidRx) não no insumo.

**Autoauditoria M00:** (i) os 3 pontos de proteção contra overclaim da matriz (SCH conflitante; relações pequenas/não lineares; bidirecionalidade+autoimunidade) estão nas regras 2/5/7; (ii) NEG é conteúdo (regra 8); (iii) nenhuma direção única adotada.

---

## MÓDULO 01 — MAPA DAS VIAS MOLECULARES (10 camadas numeradas)
[REF_MODULO_01: Roa Dueñas, 2024; Bode, 2022; Siegmann, 2018; Fischer, 2018; Bauer, 2021]

**Via 1 — Eixo HPT: fisiologia e feedback.** TSH/FT4/FT3 e regulação central como base do módulo `[revisão sistemática; B]` (Fischer, 2018; Ma, 2024 — suporte transversal recente).

**Via 2 — Função tireoidiana ↔ depressão (coorte populacional).** Associação transversal + longitudinal pequena; relação em U entre FT4 e eventos depressivos incidentes; causalidade reversa possível `[humano; ASSOCIATIVO; B]` (Roa Dueñas, 2024).

**Via 3 — Hipotireoidismo subclínico: a controvérsia central.** Meta-análises sem resultado composto significativo (Zhao, 2018; Tang, 2019) × coorte incidente negativa em jovens/adultos (Kim, 2018) × IPD de 6 coortes sem diferença clinicamente relevante (Wildisen, 2020) × NHANES sem associação (Airaksinen, 2021) → **CONTROVERSIAL_CORE: inconsistente, causalidade não estabelecida**.

**Via 4 — Hipertireoidismo ↔ depressão clínica.** Meta-análise (15 estudos; ~240 mil) com associação consistente (heterogeneidade baixa), manifeste > subclínico; causalidade não demonstrada `[META; ASSOCIATIVO; A/B]` (Bode, 2022).

**Via 5 — Hipotireoidismo clínico e terapia tireoidiana.** Manifestações neuropsiquiátricas do hipotireoidismo manifesto; LT3/LT4 como adjuvante em contextos específicos (resistente/acceleração) — síntese, não prova causal primária `[revisão clínica; B]` (Bauer, 2021).

**Via 6 — Autoimunidade tireoidiana (AIT).** Associação com depressão e ansiedade com OR elevados e heterogeneidade muito alta; mecanismo além dos hormônios (inflamação/autoimunidade) `[SR+MA; ASSOCIATIVO; A]` (Siegmann, 2018).

**Via 7 — Genética compartilhada.** Comorbidade genética/autoimune entre tireoide e psiquiatria (amostra biobanco-scale); não equivale a causalidade individual `[genético; B]` + correção editorial preservada (Soheili-Nezhad, 2023).

**Via 8 — FT4 baixo-normal → risco futuro.** Grande coorte retrospectiva com HR pequeno; magnitude mínima; sem causalidade `[humano; PROSPECTIVO/ASSOCIATIVO; B]` (Odawara, 2023).

**Via 9 — Bidirecionalidade.** Depressão/ansiedade precedendo doença tireoidiana em coorte prospectiva de biobanco `[humano; PROSPECTIVO; B]` (Fan, 2024) — trava o modelo unidirecional.

**Via 10 — Não-linearidade emergente.** Relações U/limiar entre TSH/FT4 e sintomas; uso restrito a hipótese `[emergente; C/B; G1-parcial]` (Roa Dueñas, 2024; Ma, 2024).

**Autoauditoria M01:** (i) Via 3 carrega os dois lados da controvérsia com 5 âncoras; (ii) nenhuma via termina em "corrigir TSH cura"; (iii) bidirecionalidade (Via 9) impede modelo linear.

---

## MÓDULO 02 — MEDIADORES COM POLARIDADE + INVENTÁRIO NEGATIVO
[REF_MODULO_02: Roa Dueñas, 2024; Siegmann, 2018; Wildisen, 2020; Bode, 2022; Fan, 2024]

| Marcador/fator | Papel | Status |
|---|---|---|
| TSH | eixo HPT | relações pequenas/não lineares; sem alvo terapêutico psiquiátrico |
| FT4 | hormônio periférico | U-shape com eventos depressivos (Roa Dueñas, 2024); baixo-normal HR pequeno (Odawara, 2023) |
| FT3 | hormônio ativo | transversal (Ma, 2024) `[G1 prospectivo]` |
| SCH | condição | associação inconsistente (regra 2) |
| Hipertireoidismo | condição | associação consistente (Bode, 2022) |
| AIT/anti-TPO | autoimunidade | associação robusta heterogênea (Siegmann, 2018) |
| Autoimunidade/genética compartilhada | mecanismo | suporte genético (Soheili-Nezhad, 2023) |
| LT3/LT4 | intervenção | adjuvante em contexto específico (Bauer, 2021) — só sinal |

**INVENTÁRIO NEGATIVO:**
1. "SCH causa depressão" — rejeitado (regra 2; Wildisen, 2020; Airaksinen, 2021).
2. "Hashimoto causa depressão" — rejeitado; associação com mecanismo indefinido (regra 3).
3. "Faixa ótima de TSH para psiquiatria" — proibida (regra 5).
4. "Todo deprimido é hipotireoideo" — falso (regra 6).
5. "Genética = causalidade individual" — proibido (regra 4).
6. "Tireoide → humor unidirecional" — bidirecional (Fan, 2024).
7. "Efeito hormonal isolado explica AIT×humor" — heterogeneidade alta (Siegmann, 2018).
8. "HR/OR pequenos = irrelevantes" — e "grandes = causais": ambos proibidos (regra 9).
9. "LT3 de uso amplo" — contexto restrito (Bauer, 2021).
10. "FT3 transversal = causa" — desfecho transversal `[G1]`.

**Autoauditoria M02:** (i) NEG 1–3 são as regras 2–5 espelhadas; (ii) marcadores sem polaridade binária; (iii) intervenção como dimensão.

---

## MÓDULO 03 — TIPOS CELULARES E ESTRUTURAS
[REF_MODULO_03: Siegmann, 2018; Bauer, 2021; Roa Dueñas, 2024]
- **Tireóide/eixo central** (hipotálamo/hipófise) — fisiologia HPT (Fischer, 2018).
- **Sinalização cerebral de T4/T3** (transportadores/desiodases) — descrita em revisão clínica sem âncora experimental própria no insumo `[G1]` (Bauer, 2021).
- **Sistema imune/autoimune** (linfócitos/anti-TPO) — Siegmann, 2018 (mecanismo hipotetizado).
- **Circuitos de humor:** NENHUMA âncora celular/circuito específica no insumo `[G1]`.
**Autoauditoria M03:** (i) ausência de camada celular é declarada (limitação do campo); (ii) nada inventado para preencher.

---

## MÓDULO 04 — GENÉTICA E EPIGENÉTICA
[REF_MODULO_04: Soheili-Nezhad, 2023; Fan, 2024]
- **Compartilhamento genético tireoide×psiquiatria:** (~497 mil; mecanismo específico-hormonal vs comorbidade autoimune geral) + correção editorial como metadado (Soheili-Nezhad, 2023).
- **Predisposição psiquiátrica → doença tireoidiana:** teste prospectivo de bidirecionalidade genética/fenotípica (Fan, 2024).
- **MR dedicada B11:** `[G1 — nenhuma no insumo]`.
**Autoauditoria M04:** (i) genética nunca vira causalidade clínica (regra 4); (ii) correção editorial registrada sem substituir o original.

---

## MÓDULO 05 — BIOMARCADORES À BEIRA DO LEITO (SEM PROTOCOLO/CORTE)
[REF_MODULO_05: Roa Dueñas, 2024; Odawara, 2023; Wildisen, 2020; Ma, 2024]
- **Painel HPT:** TSH/FT4/FT3 — interpretar como contínuos, não binários; relações pequenas/não lineares (Roa Dueñas, 2024; Ma, 2024).
- **Autoimunidade:** anti-TPO/AIT como marcador de associação (Siegmann, 2018).
- **Prospecção:** FT4 baixo-normal × risco futuro pequeno (Odawara, 2023) — sinal, não teste.
- **Regras:** nenhum corte; nenhuma "faixa ótima"; rastreio psiquiátrico universal de tireoide não é suportado pelo insumo; SCH sem valor preditivo clínico demonstrado (Wildisen, 2020).
**Autoauditoria M05:** (i) marcadores contínuos; (ii) nenhuma recomendação de rastreio; (iii) NEG integrado.

---

## MÓDULO 06 — CONEXÕES CAUSAIS COM OUTROS BLOCOS (FÁRMACOS SÓ COMO SINAL)
[REF_MODULO_06: Siegmann, 2018; Bauer, 2021; Fan, 2024; Soheili-Nezhad, 2023]
- **B11 ↔ B1 (neuroinflamação):** autoimunidade/inflamação como mecanismo além dos hormônios (Siegmann, 2018) — ponte declarada.
- **B11 ↔ B2 (HPA):** interação HPT×HPA no estresse `[G1 âncora no B2]`.
- **B11 ↔ B8 (iodo/micronutrientes):** iodo como insumo da síntese hormonal `[G1 âncora cruzada]`.
- **B11 ↔ B12 (trauma):** burnout/estresse crônico × tireoide `[G1]`.
- **Terapia como sinal:** LT3/LT4 adjuvante (Bauer, 2021) — contexto restrito; nunca prescrição via B11.
**Autoauditoria M06:** (i) pontes com status; (ii) nenhuma invasão de B1/B2; (iii) fármacos como janela.

---

## MÓDULO 07 — SUBTIPOS / FENÓTIPOS CLÍNICOS (SEM INTERVENÇÃO)
[REF_MODULO_07: Bode, 2022; Siegmann, 2018; Roa Dueñas, 2024; Odawara, 2023; Fan, 2024]
- **F1 — Hipertireoidismo + depressão clínica:** associação consistente (Bode, 2022).
- **F2 — AIT + depressão/ansiedade:** dupla associação com heterogeneidade (Siegmann, 2018).
- **F3 — Eutireoidiano com FT4 em U:** eventos depressivos nos extremos (Roa Dueñas, 2024).
- **F4 — FT4 baixo-normal prospectivo:** HR pequeno (Odawara, 2023).
- **F5 — Psiquiátrico prévio → doença tireoidiana:** direção reversa (Fan, 2024).
- **F6 — SCH:** SEM fenótipo depressivo clinicamente relevante estabelecido (regra 2; Wildisen, 2020) — "não-fenótipo" registrado.
**Autoauditoria M07:** (i) F6 como não-fenótipo é honestidade canônica; (ii) nenhum vira indicação terapêutica.

---

## MÓDULO 08 — CONTROVÉRSIAS, INCERTEZAS, LIMITES DE ESCOPO
[REF_MODULO_08: Zhao, 2018; Wildisen, 2020; Roa Dueñas, 2024; Siegmann, 2018; Bauer, 2021]
1. **SCH×depressão:** meta-análises positivas-fracas vs IPD/coortes negativas (regra 2).
2. **Não-linearidade:** pontos de inflexão estáveis? (Via 10 `[G1]`).
3. **AIT:** hormônios vs autoimunidade vs inflamação (Siegmann, 2018).
4. **Causalidade reversa** (Roa Dueñas, 2024; Fan, 2024).
5. **FT3 pouco estudado prospectivamente** `[G1]`.
6. **Reverse-T3:** sem âncora `[G1]`.
7. **LT3 adjuvante:** população certa, desfecho certo? (Bauer, 2021).
8. **Genética: hormonal vs autoimune geral** (Soheili-Nezhad, 2023).
9. **Heterogeneidade de definição de SCH** entre coortes `[G1]`.
10. **Confundimento por medicação** (levotiroxina em eutireoidianos) `[G1]`.
**Autoauditoria M08:** (i) controvérsias com os dois lados citados; (ii) [G1] explícitas.

---

## MÓDULO 09 — TABELA DE MAPEAMENTO × PROMPT 4.0 (B11.01–B11.11)
[REF_MODULO_09: ver M01–M08]
| Submódulo | Conteúdo | Onde |
|---|---|---|
| B11.01 Eixo HPT | TSH/FT4/FT3/feedback | Via 1 |
| B11.02 Hipotireoidismo | clínico + subclínico | Vias 3/5 |
| B11.03 Hipertireoidismo | clínico + subclínico | Via 4 |
| B11.04 Ansiedade | HPT↔ansiedade | Via 1 (Fischer) |
| B11.05 Depressão | HPT↔depressão | Vias 2/8 |
| B11.06 Autoimunidade | AIT/anti-TPO | Via 6 |
| B11.07 Genética | suscetibilidade compartilhada | Via 7; M04 |
| B11.08 T4/T3 e SNC | sinalização cerebral | M03 `[G1]` |
| B11.09 Tratamento | LT4/LT3 adjuvância | Via 5 (sinal) |
| B11.10 Causalidade e lacunas | reversa/não-linear/heterogeneidade | Vias 9–10; M08 |
| B11.11 Evidência excluída/periférica | esquizofrenia/bipolar isolados etc. | M10 |
**Autoauditoria M09:** 11/11 blocos mapeados; 10 claims SM01–SM10 distribuídos sem promoção de nível.

---

## MÓDULO 10 — OUTRAS DOENÇAS/CONTEXTOS ONDE O MECANISMO É PERTURBADO (ILUSTRATIVO — FORA DA COBERTURA)
[REF_MODULO_10: Soheili-Nezhad, 2023; Fan, 2024; Fischer, 2018]
- **Doença tireoidiana em geral (hipo/hiper/AIT):** epidemiologia bidirecional com psiquiatria (Fan, 2024).
- **Comorbidade genética ampla** (Soheili-Nezhad, 2023).
- **Ansiedade como transtorno-alvo próprio** (Fischer, 2018).
- **[EXC — exclusões de escopo:** esquizofrenia/bipolaridade isoladas, anorexia, câncer de tireoide, diabetes, gravidez/puerpério sem desfecho psiquiátrico, e as revistas regionais NAO-IDX do insumo (briefing §5).]
**Autoauditoria M10:** (i) ilustrativo; (ii) exclusões nomeadas conforme a matriz B11.11.

---

## FECHAMENTO
Trinca B11: este GPM + BRIEFING_B11_DISFUNCAO_TIREOIDIANA_RODADA0.md (tabela-mestra 14 PMIDs + correção editorial; NAO-IDX §5: 19; pendências §8) + CHECKLIST_SANIDADE_GPM_B11.md. Âncoras: `SUPORTE/b11_anchormap.json` (14 → 14 PMIDs). Rodada 2: FT3 prospectivo; reverse-T3; iodo↔B8; MR dedicada; ensaios LT4/SCH×depressão; padronização de definição de SCH.

## ÍNDICE AUTOR ↔ MÓDULO (bidirecional)
| Chave (Autor, Ano) | PMID | Módulos onde aparece |
|---|---|---|
| Airaksinen, 2021 | 34147730 | MÓDULO 00; MÓDULO 01; MÓDULO 02 |
| Bauer, 2021 | 34129186 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 06; MÓDULO 08 |
| Bode, 2022 | 36064836 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 07 |
| Fan, 2024 | 40226662 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 04; MÓDULO 06; MÓDULO 07; MÓDULO 08; MÓDULO 10 |
| Fischer, 2018 | 29064607 | MÓDULO 01; MÓDULO 03; MÓDULO 10 |
| Kim, 2018 | 29408972 | MÓDULO 00; MÓDULO 01 |
| Ma, 2024 | 39280013 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 05 |
| Odawara, 2023 | 37528949 | MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 07 |
| Roa Dueñas, 2024 | 37855318 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 05; MÓDULO 07; MÓDULO 08 |
| Siegmann, 2018 | 29800939 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 05; MÓDULO 06; MÓDULO 07; MÓDULO 08 |
| Soheili-Nezhad, 2023 | 36463425 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 04; MÓDULO 06; MÓDULO 08; MÓDULO 10 |
| Tang, 2019 | 31214119 | MÓDULO 00; MÓDULO 01 |
| Wildisen, 2020 | 33154486 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 07; MÓDULO 08 |
| Zhao, 2018 | 30375372 | MÓDULO 00; MÓDULO 01; MÓDULO 08 |
