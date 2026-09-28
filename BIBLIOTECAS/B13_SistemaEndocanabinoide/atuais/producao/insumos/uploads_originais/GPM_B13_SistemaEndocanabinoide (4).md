# GPM B13 — SISTEMA ENDOCANABINOIDE EM ANSIEDADE E DEPRESSÃO — MOLDE v2.0
### Módulo da arquitetura neuropsiquiátrica · Rodada 0 · 2026-09-09
> **Status:** GPM reconstruído sobre a triagem B13 (núcleo canônico humano ~21 + suporte experimental; em camadas) + insumo "Artigos cientificos do mecanismo B13 sistema endocanabinoide 08.09.26" (101 refs; 98 DOI→PMID auditados) + CSV Consensus de 07/set. 37 âncoras → 37 PMIDs verificados (b13_anchormap.json). Corpo limpo (zero PMID/DOI). **Reescrita** (o GPM antigo tinha 5 PMIDs vazando no corpo). Trinca: GPM + BRIEFING_B13_ENDOCANABINOIDE_RODADA0.md + CHECKLIST_SANIDADE_GPM_B13.md.

---

## MÓDULO 00 — METADADOS, REGRAS FUNDADORAS, ESCOPO E FRONTEIRAS
[REF_MODULO_00: Lutz, 2015; Yin, 2018; Rana, 2021; Yaseen, 2026; Gowatch, 2024]

**ID do mecanismo (B13):** o sistema endocanabinoide (AEA, 2-AG, PEA/OEA; enzimas FAAH/MAGL/NAPE-PLD/DAGL; receptores CB1/CB2) como **buffer/retorno resiliente do estresse**: estresse/CRH/glicocorticoides → alteração de síntese/degradação/disponibilidade de eCB → sinalização CB1/CB2 alterada → circuitos amígdala–mPFC–hipocampo (e septo–habênula) → extinção do medo/processamento de ameaça/coping/plasticidade → vulnerabilidade a fenótipos de ansiedade/depressão. **Não existe "deficiência global de eCB = doença":** a meta-análise mais recente mostra **desregulação seletiva** (AEA/PEA ↑ em MDD, 2-AG/OEA sem alteração consistente) (Yaseen, 2026).

**REGRAS FUNDADORAS:**
1. **ECS endógeno ≠ canabinoides exógenos:** THC/CBD/Cannabis/entourage ficam em camada translacional separada; nenhum claim do ECS endógeno deriva de exógenos (e vice-versa).
2. **Desregulação seletiva, não queda global** (Yaseen, 2026 — AEA/PEA ↑; 2-AG/OEA n.s.).
3. **eCB periféricos = biomarcadores mecanísticos/estratificadores potenciais — NÃO validados como diagnóstico** (heterogeneidade: sexo, estado clínico, medicação, método, matriz; Gowatch, 2024).
4. **PTSD é interface, não centro:** não infla a evidência de MDD/GAD.
5. **Animal "anxiety-like/depression-like" ≠ clínica humana** — camadas separadas; [EXTRAPOLAÇÃO POR ANALOGIA] nos causais animais.
6. **Reviews = arquitetura conceitual, não evidência primária adicional** (Lutz, 2015; Micale, 2018; Cota, 2008).
7. **A causalidade existente é experimental e regional** (amígdala/mPFC/hipocampo/septo-habênula) — não valida intervenção clínica.
8. **Exercício/PUFA = fatores moduladores interface** (Meyer, 2019 é CORE humano; os demais interface).
9. **Sandbox respeitado:** preprint de Biomed Pharmacother sem versão confirmada e abstract de congresso NÃO entram (ver briefing §5).
10. **Multi-tag permitida** (CORE humano + SUPPORT experimental).

**Dicionário mínimo:** AEA (anandamida); 2-AG; NAEs (PEA/OEA); FAAH/MAGL (hidrolases); NAPE-PLD/DAGL (sintases); CB1/CB2; "on-demand signaling"; extinção do medo; CRH; habenula lateral; escitalopram (sinal clínico em Marusak, 2025).

**Fronteiras:** neuroinflamação molecular → B1 (Morris/PUFA = interface); neuroplasticidade → B3 (ponte eCB–BDNF); HPA detalhado → B2; tireoide/HPA do insumo #38 → B11; Alzheimer (#91) → fora; trauma → B12 (Mazurka, 2024 ponte).

**Lacunas [G1] do M00:** (a) Bloemhof-Bris 2024 (ECT×eCB) não localizada; (b) Ibarra-Lecue 2018 (cérebro post-mortem) e McWhirter 2024 não resolvidas; (c) McLaughlin ×3 (pPFC/coping) não indexadas no lote; (d) Spohrs — RESOLVIDO na onda 09/09: versão publicada cravada (FAAH rs324420×recall de extinção, humanos; Via 2); (e) Zabik-RCT (THC×extinção em humanos) não localizado (o Zabik 2024 do insumo é review).

**Autoauditoria M00:** (i) separação endógeno×exógeno e camadas CORE/SUPORTE/INTERFACE/HOLD reproduzidas; (ii) desregulação seletiva no ID; (iii) regra do biomarcador (3) atua em todo M05.

---

## MÓDULO 01 — MAPA DAS VIAS MOLECULARES (10 camadas numeradas)
[REF_MODULO_01: Lutz, 2015; Gray, 2015; Marcus, 2020; Gunduz-Cinar, 2023; Yaseen, 2026]

**Via 1 — Arquitetura do ECS (base).** Guardião contra medo/ansiedade/estresse; revisões estruturais `[revisão; SUPORTE]` (Lutz, 2015; Ruehle, 2012; Cota, 2008; Yin, 2018; Rana, 2021).

**Via 2 — Estresse → CRH → FAAH → AEA ↓ → ansiedade.** CRH recruta hidrólise de AEA na amígdala; fluoxetina facilita extinção via eCB amigdalar `[animal; CAUSAL experimental; B]` + `[EXTRAPOLAÇÃO POR ANALOGIA]` (Gray, 2015; Gunduz-Cinar, 2013; Gunduz-Cinar, 2023 — substrato cortico-amigdalar da extinção); em humanos, o polimorfismo FAAH rs324420 modula o recall de extinção `[humano; B]` (Spohrs, 2022).

**Via 3 — Colapso/fortalecimento de sinalização eCB pelo estresse.** Estresse → colapso da sinalização eCB associado ao fortalecimento amigdalo-cortical `[animal; CAUSAL; A]` + `[EXTRAPOLAÇÃO POR ANALOGIA]` (Marcus, 2020); estresse agudo suprime inibição e ↑ANS na BLA (Di, 2016); sexo e modalidade de estressor modulam dinâmica corticolímbica (Vecchiarelli, 2022).

**Via 4 — CB1 e comportamento emocional.** BNST/CB1 e FAAH (Bedse, 2017); CB1 na aprendizagem/extinção do medo (Kuhnert, 2013); modulação direta/indireta (Kondev, 2023); redução de eCB → ansiedade/medo (Jenniches, 2016); estressor predatório (Lim, 2016); NAPE-PLD neuronal → fenótipo ansiogênico quando deletada (Tevosian, 2023).

**Via 5 — Circuitos estendidos.** Septo–habênula × ansiedade/depressão (Vickstrom, 2020); circuito amígdala–hipocampo × modulação eCB da ansiedade (Xue, 2025); memória/plasticidade hipocampo-amígdala (Segev, 2018 `[revisão]`); eCB–noradrenalina na extinção (Warren, 2021 `[revisão/integração]`).

**Via 6 — HPA ↔ ECS.** eCB como feedback fisiológico do eixo; estresse×HPA (Micale, 2018; Cota, 2008) — ponte B2, cadeia resumida no ID.

**Via 7 — Humano: eCB periféricos em MDD/ansiedade.** Hill, 2008 (sérico alterado em mulheres com depressão); Yaseen, 2026 (MA: AEA/PEA ↑, 2-AG/OEA n.s.); Fuentes, 2024 (SR periféricos×MDD); Gowatch, 2024 (SR+MA estresse, heterogeneidade alta); Navarrete, 2020 (componentes do ECS como biomarcadores potenciais); Wang, 2025 (biomarcadores ECS×MDD); Obermanns, 2023 (CNR1×variantes serotonérgicas).

**Via 8 — Humano: trauma/ciclo de vida e intervenção-sinal.** Mazurka, 2024 (eCB×trauma infantil×volume hipocampal em mulheres); Marusak, 2025 (jovens: ansiedade×AEA↑/2-AG↓; escitalopram→↑2-AG associado à resposta — sinal, não protocolo); Meyer, 2019 (exercício×eCB×humor em MDD); Alcaraz-Silva, 2023 (ECS como biomarcador/alvo — revisão); Bright & Akirav, 2022 (pré-clínico+clínico); Garani, 2020 (transtornos do humor); Chadwick, 2019 (ansiedade/depressão/regulação emocional).

**Via 9 — Neuroinflamação (interface B1).** eCB↔imunidade nos desfechos MDD (Yaseen, 2026 — lipidoma neuroimune); PUFA→eCB→neuroinflamação `[interface]` — o molecular fica no B1.

**Via 10 — Exógenos/translacional (camada separada).** Zabik-RCT (THC×extinção em humanos) `[G1 não localizado]`; nenhum claim do núcleo deriva desta camada (regra 1).

**Autoauditoria M01:** (i) causais animais com EXTRAP; (ii) camada humana (vias 7–8) separada da experimental; (iii) via 10 isolada por regra.

---

## MÓDULO 02 — MEDIADORES COM POLARIDADE + INVENTÁRIO NEGATIVO
[REF_MODULO_02: Yaseen, 2026; Gowatch, 2024; Marusak, 2025; Mazurka, 2024; Marcus, 2020]

| Mediador | Papel | Efeito documentado |
|---|---|---|
| AEA | "buffer de estresse" | ↓ com CRH/estresse (animal); ↑ em MDD (humano — Yaseen) |
| 2-AG | sinalização sináptica | sem alteração consistente em MDD; ↓ associado à ansiedade em jovens (Marusak) |
| PEA/OEA | NAEs acompanham | ↑ em MDD (Yaseen) |
| FAAH | hidrólise de AEA | recrutada por CRH (Gray; Gunduz-Cinar); rs324420×extinção em humanos (Spohrs, 2022) |
| CB1 | receptor primário | modula extinção/ansiedade (Kuhnert; Bedse) |
| NAPE-PLD | síntese | deleção → ansiogênico (Tevosian) |
| Cortisol/CRH | gatilho upstream | cadeia estresse→eCB (Micale; Di) |

**INVENTÁRIO NEGATIVO:** 1. "deficiência de eCB = ansiedade/depressão" — falso (desregulação seletiva; Yaseen). 2. "AEA baixo em MDD" — o encontrado foi ↑ (Yaseen). 3. "eCB periférico = teste diagnóstico" (regra 3). 4. "THC/CBD provam o ECS endógeno" (regra 1). 5. "PTSD valida MDD/GAD" (regra 4). 6. "animal anxiety-like = clínico" (regra 5). 7. "reviews = evidência adicional" (regra 6). 8. "modulação eCB = tratamento validado" (regra 7; Kwee, 2023 é agregado pré-clínico+translacional). 9. "exercício = prescrição via eCB" (Meyer, 2019 é associação humana). 10. "eCB infantil×hipocampo = causal" (Mazurka é associativo).

**Autoauditoria M02:** (i) NEG 2 registra a direção oposta ao senso comum; (ii) intervenções como sinal; (iii) tabela com matriz (tecido×estado).

---

## MÓDULO 03 — TIPOS CELULARES E ESTRUTURAS
[REF_MODULO_03: Marcus, 2020; Xue, 2025; Di, 2016; Bedse, 2017; Tevosian, 2023]
- **Amígdala BLA/CeA** (FAAH/AEA; extinção) — Gray, 2015; Morena, 2018; Gunduz-Cinar, 2013/2023.
- **mPFC** (colapso de sinalização; top-down) — Marcus, 2020.
- **Hipocampo** (redundância funcional; memória) — Bedse, 2017; Kuhnert, 2013; Segev, 2018.
- **BNST** — Bedse, 2017.
- **Septo–habênula** — Vickstrom, 2020.
- **Neurônios TRAPed/NAPE-PLD** — Tevosian, 2023.
**Autoauditoria M03:** (i) circuitos com evidência causal própria; (ii) nenhum circuito humano in vivo ancorado `[G1]`.

---

## MÓDULO 04 — GENÉTICA E EPIGENÉTICA
[REF_MODULO_04: Obermanns, 2023; Navarrete, 2020]
- **CNR1 × variantes 5-HT** (Obermanns, 2023) — associativo.
- **Componentes do ECS como biomarcadores genéticos/exprimíveis** (Navarrete, 2020).
- **GWAS eCB×psiquiatria:** `[G1 — nada no insumo]`.
**Autoauditoria M04:** (i) associativo rotulado; (ii) [G1].

---

## MÓDULO 05 — BIOMARCADORES À BEIRA DO LEITO (SEM PROTOCOLO/CORTE)
[REF_MODULO_05: Yaseen, 2026; Gowatch, 2024; Hill, 2008; Mazurka, 2024; Marusak, 2025]
- **Lipidoma plasmático/sérico (AEA, 2-AG, PEA, OEA):** alterações seletivas em MDD (Yaseen, 2026); heterogeneidade alta (Gowatch, 2024).
- **Moduladores do valor do biomarcador:** sexo, estado, medicação, método, matriz (regra 3).
- **Neuroimagem/fisiologia:** sem marcador ECS-validado em clínica.
- **Regras:** nenhum corte; nenhuma "dosagem de eCB" diagnóstica; mudança com tratamento = sinal (Marusak, 2025), não teste preditivo.
**Autoauditoria M05:** (i) biomarcador potencial rotulado; (ii) nada validado.

---

## MÓDULO 06 — CONEXÕES CAUSAIS COM OUTROS BLOCOS (FÁRMACOS SÓ COMO SINAL)
[REF_MODULO_06: Gray, 2015; Meyer, 2019; Yaseen, 2026; Mazurka, 2024; Vickstrom, 2020]
- **B13 ↔ B2 (HPA):** cadeia CRH→eCB (Gray, 2015; Micale, 2018) — detalhe do eixo no B2.
- **B13 ↔ B3 (plasticidade):** eCB↔BDNF/extinção/plasticidade sináptica (Gunduz-Cinar, 2023; Segev, 2018) — ponte.
- **B13 ↔ B1 (inflamação):** lipidoma neuroimune (Yaseen, 2026); PUFA (interface).
- **B13 ↔ B12 (trauma):** eCB×trauma infantil×hipocampo (Mazurka, 2024) — associativo.
- **B13 ↔ B4 (serotonina):** SSRI×eCB (Gray, 2015 animal; Marusak, 2025 humano) — sinal.
- **Exógenos (THC/CBD):** camada translacional separada — nunca validam o núcleo (regra 1).
**Autoauditoria M06:** (i) pontes com status; (ii) exógenos isolados; (iii) [G1] para HPA completo.

---

## MÓDULO 07 — SUBTIPOS / FENÓTIPOS CLÍNICOS (SEM INTERVENÇÃO)
[REF_MODULO_07: Yaseen, 2026; Marusak, 2025; Mazurka, 2024; Meyer, 2019; Hill, 2008]
- **F1 — MDD com lipidoma eCB desregulado (AEA/PEA ↑)** (Yaseen, 2026; Hill, 2008).
- **F2 — Jovens ansiosos com AEA↑/2-AG↓** (Marusak, 2025).
- **F3 — Mulheres com trauma infantil: eCB×hipocampo** (Mazurka, 2024).
- **F4 — MDD em exercício: mudança de eCB×humor** (Meyer, 2019) — associativo.
- **F5 — Sexo feminino: perfis próprios de eCB** (Hill, 2008; McWhirter `[G1]`; Gowatch heterogeneidade).
**Autoauditoria M07:** (i) fenótipos associativos; (ii) F5 registra a estratificação por sexo.

---

## MÓDULO 08 — CONTROVÉRSIAS, INCERTEZAS, LIMITES DE ESCOPO
[REF_MODULO_08: Yaseen, 2026; Gowatch, 2024; Marcus, 2020; Bedse, 2017]
1. **Direção dos NAEs em MDD** (↑ contraintuitivo; Yaseen, 2026).
2. **Heterogeneidade metodológica das medidas periféricas** (Gowatch, 2024).
3. **Tradução animal→humano** (regra 5).
4. **Redundância funcional CB1** por região (Bedse, 2017).
5. **Colapso vs adaptação** da sinalização (Marcus, 2020) — temporalidade.
6. **Sexo** (Vecchiarelli, 2022) `[G1]`.
7. **Exógenos×endógenos** na narrativa pública (regra 1).
8. **PTSD como motor do campo** (regra 4).
9. **Habênula/ circuitos estendidos** pouco replicados `[G1]`.
10. **Faltas de âncora humana** (Bloemhof/Ibarra-Lecue/McWhirter → [G1]; Spohrs cravado em 09/09).
**Autoauditoria M08:** (i) controvérsias vivas; (ii) [G1] explícitas.

---

## MÓDULO 09 — TABELA DE MAPEAMENTO × PROMPT 4.0 (CAMADAS DA TRIAGEM)
[REF_MODULO_09: ver M01–M08]
| Bloco | Conteúdo | Onde |
|---|---|---|
| B13-01 ECS endógeno (AEA/2-AG/FAAH/MAGL/CB1/CB2) | arquitetura | Via 1; M02 |
| B13-02 Estresse→eCB (CRH/HPA) | cadeia central | Vias 2–3; 6 |
| B13-03 Circuitos (amígdala/mPFC/hipocampo/BNST/habênula) | causais | Vias 3–5 |
| B13-04 Humano: MDD (lipidoma) | núcleo clínico | Via 7 |
| B13-05 Humano: ansiedade/jovens | núcleo clínico | Via 8 |
| B13-06 Trauma/PTSD (interface) | ponte B12 | M06; F3 |
| B13-07 Exógenos/translacional (THC/CBD) | camada isolada | Via 10 |
| B13-08 Genética/biomarcadores | associativo | M04–M05 |
| B13-09 Neuroinflamação (interface B1) | ponte | Via 9; M06 |
| B13-10 Moduladores (exercício/PUFA/sexo) | interface | Via 8; F4–F5 |
**Autoauditoria M09:** 10/10 blocos; núcleo humano (~21 refs da triagem) coberto pelas vias 7–8.

---

## MÓDULO 10 — OUTRAS DOENÇAS/CONTEXTOS ONDE O MECANISMO É PERTURBADO (ILUSTRATIVO — FORA DA COBERTURA)
[REF_MODULO_10: Garani, 2020; Cota, 2008]
- **Transtornos do humor além de MDD (psicóticos):** (Garani, 2020) — contexto.
- **Qualidade de vida/vigilância metabólica do ECS** (Cota, 2008).
- **[EXC — exclusões de escopo:** Alzheimer (#91); psilocibina×HPA×BDNF (abstract — sandbox); doenças gastrointestinais; dor crônica como doença-âncora; NAO-IDX do insumo (briefing §5).]
**Autoauditoria M10:** (i) ilustrativo; (ii) sandbox respeitado.

---

## FECHAMENTO
Trinca B13: este GPM + BRIEFING_B13_ENDOCANABINOIDE_RODADA0.md (tabela-mestra 38 PMIDs; NAO-IDX §5; pendências §8) + CHECKLIST_SANIDADE_GPM_B13.md. Âncoras: `SUPORTE/b13_anchormap.json` (38 → 38 PMIDs). Rodada 2: Bloemhof-Bris (ECT); Ibarra-Lecue (post-mortem); McWhirter; McLaughlin pPFC ×3; Zabik-RCT; GWAS eCB.

## ÍNDICE AUTOR ↔ MÓDULO (bidirecional)
| Chave (Autor, Ano) | PMID | Módulos onde aparece |
|---|---|---|
| Alcaraz-Silva, 2023 | 35382720 | MÓDULO 01 |
| Bedse, 2017 | 36870468 | MÓDULO 01; MÓDULO 03; MÓDULO 08 |
| Bright & Akirav, 2022 | 35628337 | MÓDULO 01 |
| Chadwick, 2019 | 31714262 | MÓDULO 01 |
| Cota, 2008 | 34776851 | MÓDULO 00; MÓDULO 01; MÓDULO 10 |
| Di, 2016 | 27511017 | MÓDULO 01; MÓDULO 03 |
| Fuentes, 2024 | 39118031 | MÓDULO 01 |
| Garani, 2020 | 32898588 | MÓDULO 01; MÓDULO 10 |
| Gowatch, 2024 | 38683635 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 08 |
| Gray, 2015 | 26514583 | MÓDULO 01; MÓDULO 03; MÓDULO 06 |
| Gunduz-Cinar, 2013 | 24325918 | MÓDULO 01; MÓDULO 03 |
| Gunduz-Cinar, 2023 | 37480845 | MÓDULO 01; MÓDULO 06 |
| Hill, 2008 | 18311684 | MÓDULO 01; MÓDULO 05; MÓDULO 07 |
| Jenniches, 2016 | 25981172 | MÓDULO 01 |
| Kondev, 2023 | 40005177 | MÓDULO 01 |
| Kuhnert, 2013 | 23702112 | MÓDULO 01; MÓDULO 03 |
| Kwee, 2023 | 37094409 | MÓDULO 02 |
| Lim, 2016 | 26361059 | MÓDULO 01 |
| Lutz, 2015 | 26585799 | MÓDULO 00; MÓDULO 01 |
| Marcus, 2020 | 31948734 | MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 08 |
| Marusak, 2025 | 40579470 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 06; MÓDULO 07 |
| Mazurka, 2024 | 38886733 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 06; MÓDULO 07 |
| Meyer, 2019 | 30973483 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 06; MÓDULO 07 |
| Micale, 2018 | 30036537 | MÓDULO 00; MÓDULO 01; MÓDULO 06 |
| Morena, 2018 | 30573646 | MÓDULO 03 |
| Navarrete, 2020 | 32395111 | MÓDULO 01; MÓDULO 04 |
| Obermanns, 2023 | 37984468 | MÓDULO 01; MÓDULO 04 |
| Rana, 2021 | 33471311 | MÓDULO 00; MÓDULO 01 |
| Ruehle, 2012 | 21768162 | MÓDULO 01 |
| Spohrs, 2022 | 34893921 | MÓDULO 01; MÓDULO 02 |
| Tevosian, 2023 | 37149657 | MÓDULO 01; MÓDULO 03 |
| Vecchiarelli, 2022 | 36039150 | MÓDULO 01; MÓDULO 08 |
| Vickstrom, 2020 | 33093652 | MÓDULO 01; MÓDULO 03; MÓDULO 06 |
| Wang, 2025 | 41013856 | MÓDULO 01 |
| Warren, 2021 | 33759226 | MÓDULO 01 |
| Xue, 2025 | 40522172 | MÓDULO 01; MÓDULO 03 |
| Yaseen, 2026 | 42431383 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 06; MÓDULO 07; MÓDULO 08 |
| Yin, 2018 | 30002489 | MÓDULO 00; MÓDULO 01 |
