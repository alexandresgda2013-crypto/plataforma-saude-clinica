# GPM B12 — NEUROBIOLOGIA DO TRAUMA EM ANSIEDADE E DEPRESSÃO — MOLDE v2.0
### Módulo da arquitetura neuropsiquiátrica · Rodada 0 · 2026-09-09
> **Status:** GPM reconstruído sobre a triagem B12 (10 claims B12.SM01–SM10; "APROVADO_COM_RESSALVAS") + insumo "Artigos cientificos do mecanismo B12 neurobiologia trauma 08.09.26" (178 refs; 171 DOI→PMID auditados) + 2 CSVs Consensus de 07/set (74 papers). 33 âncoras → 33 PMIDs verificados (b12_anchormap.json). Corpo limpo (zero PMID/DOI). Trinca: GPM + BRIEFING_B12_NEUROBIOLOGIA_TRAUMA_RODADA0.md + CHECKLIST_SANIDADE_GPM_B12.md.

---

## MÓDULO 00 — METADADOS, REGRAS FUNDADORAS, ESCOPO E FRONTEIRAS
[REF_MODULO_00: Heim & Nemeroff, 2001; Menke, 2018; Shin, 2011; Serra-Blasco, 2021; Miller, 2013]

**ID do mecanismo (B12):** o trauma psicológico (especialmente adversidade precoce) como **programador/sensibilizador de circuitos e sistemas de estresse**: trauma → HPA/GR/MR/FKBP5 → resposta ao estresse alterada → amígdala ↑ reatividade à ameaça + hipocampo ↓ contextualização + PFC/ACC ↓ regulação top-down → condicionamento/extinção do medo alterados → plasticidade/BDNF e imunidade moduladas → regulação emocional persistente alterada → fenótipos internalizantes. **Modelo multiplicativo, não linear:** trauma × genética × idade do trauma × tipo/intensidade × sexo × contexto posterior × resiliência. B12 é a camada de **origem/contexto** que modula os demais mecanismos (B1, B2, B3) — não os duplica.

**REGRAS FUNDADORAS:**
1. **Nada determinístico (10 bloqueios da triagem):** "trauma causa depressão", "trauma causa redução do hipocampo", "trauma causa cortisol alto", "trauma causa hiperatividade do HPA", "FKBP5 causa depressão", "BDNF baixo é consequência obrigatória do trauma", "amígdala hiperativa é biomarcador de trauma", "trauma produz neuroinflamação em todos", "trauma altera permanentemente o cérebro", "trauma é a causa da ansiedade" — TODOS proibidos.
2. **Alteração estrutural ≠ biomarcador diagnóstico:** a narrativa "amígdala↑+hipocampo↓+PFC↓" não é o registro canônico; a evidência é heterogênea e transdiagnóstica (Serra-Blasco, 2021 — MDD×ansiedade×PTSD compartilham parte, não tudo).
3. **Hipocampo: causalidade parcialmente indeterminada** (vulnerabilidade prévia vs efeito do trauma) — claim canônico preserva a indeterminação (Logue, 2018 — consórcio ENIGMA; Paquola, 2016 — heterogeneidade de massa cinzenta em adultos com maus-tratos infantis; o PMID da triagem para Logue era inválido e foi substituído pelo verificado — briefing §4).
4. **FKBP5/GR = interface molecular, não causa** (Menke, 2018).
5. **B12 não duplica B1 (inflamação), B3 (plasticidade/BDNF), B2 (HPA):** registra apenas o vínculo com o trauma como variável expositiva (Miller, 2013; Pereira, 2021; Price & Duman, 2019 citados como ponte).
6. **TBI (traumatismo craniano) ≠ trauma psicológico** — TBI excluído (blocos Malik/Risbrough/Tapp → fora do canônico).
7. **Transdiagnóstico obrigatório:** PTSD não infla MDD/GAD; meta-análises comparativas regulam o módulo (Serra-Blasco, 2021; Zugman, 2023).
8. **Epigenética = promissora/fronteira, não causalidade humana estabelecida** (Miao, 2020; Wang, 2026); "transgeracional" exige barra causal alta.
9. **Psicoterapia = submódulo de reversibilidade/plasticidade terapêutica (B12.11), não mecanismo primário** `[G1 — âncoras de intervenção fora do canônico]`.
10. **Anos canônicos = print** (Suarez-Jimenez 2020; O'Doherty 2015); **PMID da triagem nunca entra sem verificação** (caso Logue: o PMID da triagem apontava para paper não-relacionado → resolvido por busca dirigida).

**Dicionário mínimo:** HPA/CRH/ACTH/cortisol; GR/MR; FKBP5; dexametasona (teste de feedback); Val66Met (polimorfismo do BDNF); extinção/recuperação da extinção; reconsolidação; ENIGMA (consórcio neuroimagem); VBM; conectividade funcional repouso.

**Fronteiras:** inflamação molecular → B1; maquinaria plástica → B3; eixo HPA fisiológico → B2; microbiota→estresse → B7; resiliência social → fenótipos; TBI → fora.

**Lacunas [G1] do M00:** (a) piloto psicoterapia (Manthey) — B12.11. [(a)–(d) originais — Logue-ENIGMA, McTeague 2020, Von Werne Baes 2012, Paquola 2016 — foram CRAVADOS na onda de catches de 09/09; ver briefing §4, item 7.]

**Autoauditoria M00:** (i) os 10 bloqueios deterministas estão reproduzidos; (ii) modelo multiplicativo no ID; (iii) fronteira B12-origem × B1/B2/B3-maquinaria explícita.

---

## MÓDULO 01 — MAPA DAS VIAS MOLECULARES (10 camadas numeradas)
[REF_MODULO_01: Menke, 2018; Shin, 2011; Notaras, 2020; Tian, 2020; Lee, 2025]

**Via 1 — Trauma como estressor neurobiológico (porta de entrada).** Trauma/adversidade precoce ↔ risco e fenótipo internalizante, com modelo programação/sensibilização `[humano; ASSOCIATIVO/PROBABLE; A/B]` (Heim & Nemeroff, 2001 — revisão fundacional; Murphy, 2022 — SR HPA×trauma).

**Via 2 — HPA agudo/crônico × trauma.** HPA em depressão unipolar com heterogeneidade (Lu, 2016); trauma infantil sensitiza resposta ansioso-depressiva do eixo (Menke, 2018 — 144 pacientes, dexametasona+FKBP5); resposta antidepressiva modulada por trauma×HPA (Nikkheslat, 2019); cortisol×cognição (Wingenfeld, 2014).

**Via 3 — GR/MR/FKBP5.** Interface molecular exposição→regulação do estresse `[humano; B]` (Menke, 2018; Murphy, 2022; Von Werne Baes, 2012 — avaliação GR/MR do HPA na depressão) — sem causalidade FKBP5→doença (regra 4).

**Via 4 — Amígdala: processamento de ameaça.** Neurocircuito medo/estresse/ansiedade (Shin, 2011); conectividade amígdala alterada em ansiedade (Lu, 2026); dano/aferência emocional (McTeague, 2020 — disrupções comuns de circuitos emocionais; primeiro autor real do paper — ex-chave "Mayer, 2020").

**Via 5 — Hipocampo: contextualização e estrutura.** Memória contextual/discriminação segurança×ameaça; estrutura associativa (indeterminada — regra 3): Liu, 2022 (medo patológico); Xiao, 2022 (PTSD estrutural+funcional); O'Doherty, 2015 (meta MRI PTSD); Pollok, 2022 (traços neuroestruturais de adversidade precoce); Sartory, 2013 (memória traumática).

**Via 6 — PFC/ACC: regulação top-down.** ACC×PFC na regulação (Marusak, 2016); controvérsia de terminologia/rede (o próprio Marusak 2016); transdiagnóstico (Serra-Blasco, 2021; Zugman, 2023 — resting-state ansiedade; Zhong, 2024 — harm avoidance multimodal).

**Via 7 — Condicionamento/extinção do medo.** Trauma → aprendizagem de ameaça → generalização → extinção prejudicada (Suarez-Jimenez, 2020 — assinaturas neurais de condicionamento/extinção/recuperação em PTSD; Sartory, 2013).

**Via 8 — BDNF/plasticidade/neurogênese.** BDNF no medo/estresse (Notaras, 2020); BDNF serotoninérgico (Leschik, 2022); sinalização BDNF em contexto psiquiátrico (Wang, 2021; Numakawa, 2023); plasticidade hippocampal em MDD (Tartt, 2022); mecanismos plásticos da depressão (Price & Duman, 2019 — ponte B3); Val66Met×trauma (Tian, 2020; Yu, 2012) — interação exposição×vulnerabilidade, não determinismo.

**Via 9 — Imunidade/neuroinflamação (ponte B1).** Citocinas↔transmissores (Miller, 2013); bidirecionalidade imune-cérebro (Rengasamy, 2021); microglia×HPA (Pereira, 2021); **citocinas modulam circuitos amigdalaros bidirecionalmente** (Lee, 2025) — formulação específica, não "inflamação=ansiedade".

**Via 10 — Epigenética/programação.** Estresse×transtornos×epigenômica (Miao, 2020); metilação do BDNF em PTSD (Wang, 2026) — fronteira promissora, barra causal alta (regra 8).

**Autoauditoria M01:** (i) nenhuma via fecha causalidade determinística; (ii) vias 2–3 (HPA) e 8 (BDNF) citam ponte, não invasão de B2/B3; (iii) via 9 formula bidirecionalidade (Lee, 2025).

---

## MÓDULO 02 — MEDIADORES COM POLARIDADE + INVENTÁRIO NEGATIVO
[REF_MODULO_02: Menke, 2018; Serra-Blasco, 2021; Tian, 2020; Lee, 2025; Murphy, 2022]

| Mediador/eixo | Papel | Status |
|---|---|---|
| Cortisol/HPA | eixo de resposta | alterado com heterogeneidade (Lu, 2016; Murphy, 2022) |
| GR/FKBP5 | interface molecular | sensitização associada (Menke, 2018) |
| Amígdala | ameaça | reatividade/conectividade alteradas (Shin, 2011; Lu, 2026) |
| Hipocampo | contexto/memória | alterações associativas, causalidade indeterminada (regra 3) |
| PFC/ACC | top-down | regulação alterada (Marusak, 2016) |
| Extinção do medo | aprendizagem | prejudicada em trauma/PTSD (Suarez-Jimenez, 2020) |
| BDNF/Val66Met | plasticidade | interação gen×ambiente (Tian, 2020; Yu, 2012) |
| Citocinas | modulação bidirecional | pró E anti-inflamatórias modulam circuitos (Lee, 2025) |
| Metilação (BDNF) | epigenética | fronteira (Wang, 2026) |

**INVENTÁRIO NEGATIVO:** 1. "trauma causa depressão/ansiedade" (regra 1). 2. "trauma reduz o hipocampo" como fato (regra 3). 3. "trauma = cortisol alto/HPA hiperativo" (heterogeneidade; Lu, 2016). 4. "FKBP5 causa doença" (regra 4). 5. "BDNF baixo obrigatório" (regra 1; Tian, 2020 é interação). 6. "amígdala hiperativa = biomarcador" (regra 2). 7. "neuroinflamação universal pós-trauma" (Lee, 2025 é bidirecional). 8. "alterações permanentes" (plasticidade/reversibilidade existe — B12.11 [G1]). 9. "TBI = trauma psicológico" (regra 6). 10. "PTSD infla MDD/GAD" (regra 7; Serra-Blasco, 2021).

**Autoauditoria M02:** (i) NEG 1–10 = os 10 bloqueios; (ii) tabela sem polaridade binária; (iii) nada diagnóstico.

---

## MÓDULO 03 — TIPOS CELULARES E ESTRUTURAS
[REF_MODULO_03: Shin, 2011; Marusak, 2016; Notaras, 2020; Pereira, 2021]
- **Amígdala (BLA/CeA), hipocampo (dentado/CA), PFC (dl/vl/medial), ACC** — circuitos de ameaça/regulação (Shin, 2011; Marusak, 2016).
- **Redes em repouso** (default/salience — Zugman, 2023; Lu, 2026).
- **Microglia** (ponte B1) — Pereira, 2021.
- **Interneuronios serotoninérgicos/BDNF** — Leschik, 2022 `[animal]`.
**Autoauditoria M03:** (i) estruturas com evidência citada; (ii) nenhum circuito vira "biomarcador de trauma".

---

## MÓDULO 04 — GENÉTICA E EPIGENÉTICA
[REF_MODULO_04: Tian, 2020; Yu, 2012; Miao, 2020; Wang, 2026]
- **BDNF Val66Met × trauma × regulação emocional** — interação (Tian, 2020; Yu, 2012).
- **Epigenômica do estresse** (revisão; Miao, 2020).
- **Metilação mult_camada do BDNF em PTSD** (Wang, 2026) — fronteira.
- **FKBP5 genético × HPA** — dentro da interface GR (regra 4) `[G1 — GWAS dedicado ausente]`.
**Autoauditoria M04:** (i) interação ≠ destino; (ii) epigenética sem causalidade humana.

---

## MÓDULO 05 — BIOMARCADORES À BEIRA DO LEITO (SEM PROTOCOLO/CORTE)
[REF_MODULO_05: Menke, 2018; Lu, 2016; Serra-Blasco, 2021; Wang, 2026]
- **Neuroendócrino:** cortisol basal/DST; resposta GR/FKBP5 (Menke, 2018) — pesquisa.
- **Neuroimagem:** volumes/cortical (Serra-Blasco, 2021; Xiao, 2022; Pollok, 2022); conectividade repouso (Zugman, 2023; Lu, 2026); assinaturas de extinção (Suarez-Jimenez, 2020).
- **Moleculares:** BDNF/citocinas periféricas — heterogêneos, sem valor diagnóstico isolado.
- **Regras:** nenhuma medida define diagnóstico; alteração estrutural ≠ marcador individual (regra 2); sangue ≠ cérebro.
**Autoauditoria M05:** (i) sem cortes; (ii) transdiagnóstico (Serra-Blasco, 2021).

---

## MÓDULO 06 — CONEXÕES CAUSAIS COM OUTROS BLOCOS (TERAPIAS SÓ COMO SINAL)
[REF_MODULO_06: Miller, 2013; Price & Duman, 2019; Pereira, 2021; Lee, 2025]
- **B12 → B1:** trauma→estresse→imunidade (Miller, 2013; Rengasamy, 2021; Pereira, 2021) — o molecular fica no B1.
- **B12 → B3:** trauma altera condições de plasticidade (Price & Duman, 2019; Tartt, 2022; Notaras, 2020) — a maquinaria é B3.
- **B12 ↔ B2:** HPA detalhado é B2; aqui só o braço trauma-dependente (Menke, 2018; Murphy, 2022).
- **B12 ↔ B7:** trauma e o eixo microbiota-intestino `[G1 âncora no B7]`.
- **B12.11 Reversibilidade:** psicoterapia remodela circuitos `[G1 — âncora de intervenção fora do canônico]`.
- **TBI → fora** (regra 6).
**Autoauditoria M06:** (i) pontes sem duplicação; (ii) nenhuma terapia recomendada; (iii) [G1] registradas.

---

## MÓDULO 07 — SUBTIPOS / FENÓTIPOS CLÍNICOS (SEM INTERVENÇÃO)
[REF_MODULO_07: Menke, 2018; Serra-Blasco, 2021; Suarez-Jimenez, 2020; Tian, 2020; Zhong, 2024]
- **F1 — Depressão ansiosa pós-trauma com sensitização HPA/GR** (Menke, 2018).
- **F2 — PTSD com perfil de extinção prejudicada** (Suarez-Jimenez, 2020).
- **F3 — Fenótipo transdiagnóstico compartilhado** (Serra-Blasco, 2021; McTeague, 2020).
- **F4 — Portadores Val66Met expostos** (Tian, 2020; Yu, 2012).
- **F5 — Ansiedade com perfil harm-avoidance/harm-OCD-like** (Zhong, 2024).
- **F6 — Resiliência:** expo≠fenótipo; moduladores contextuais (regra do modelo multiplicativo) `[G1 âncora]`.
**Autoauditoria M07:** (i) fenótipos sem corte; (ii) F6 registra a não-universalidade.

---

## MÓDULO 08 — CONTROVÉRSIAS, INCERTEZAS, LIMITES DE ESCOPO
[REF_MODULO_08: Serra-Blasco, 2021; Murphy, 2022; Tian, 2020; Lee, 2025; Miao, 2020]
1. **Causalidade reversa/vulnerabilidade prévia** (estrutura hipocampal — regra 3).
2. **Heterogeneidade HPA** (hipo×hiper; Lu, 2016; Murphy, 2022).
3. **Especificidade vs transdiagnóstico** (Serra-Blasco, 2021; Zugman, 2023).
4. **Gen×ambiente: replicação limitada** (Tian, 2020; Yu, 2012) `[G1]`.
5. **Epigenética: causalidade e transgeracionalidade** (Miao, 2020; Wang, 2026).
6. **Bidirecionalidade imune** (Lee, 2025).
7. **Medição do trauma** (autorrelato×objetivo) `[G1]`.
8. **Medicação como confundidor** (Nikkheslat, 2019) `[G1]`.
9. **Sexo como modulador** `[G1]`.
10. **Neuroimagem: sensibilidade/especificidade nula para uso clínico** (regra 2).
**Autoauditoria M08:** (i) controvérsias com fonte; (ii) nenhuma resolvida por retórica.

---

## MÓDULO 09 — TABELA DE MAPEAMENTO × PROMPT 4.0 (B12.1–B12.11)
[REF_MODULO_09: ver M01–M08]
| Submódulo | Conteúdo (claims) | Onde |
|---|---|---|
| B12.1 Trauma como estressor | SM01 | Via 1 |
| B12.2 HPA/glicocorticoides | SM02 | Vias 2 |
| B12.3 GR–FKBP5 | SM03 | Via 3 |
| B12.4 Amígdala | SM04 | Via 4 |
| B12.5 Hipocampo/contexto | (parte SM04/SM06) | Via 5 |
| B12.6 PFC/ACC top-down | SM04 | Via 6 |
| B12.7 Condicionamento/extinção | SM05 | Via 7 |
| B12.8 Estrutura hipocampal (indeterminada) | SM06 | Via 5 + regra 3 |
| B12.9 BDNF/plasticidade | SM07 | Via 8 |
| B12.10 Epigenética/Gen×amb | SM08 | Via 10; M04 |
| B12.9-inflamação | SM09 | Via 9 |
| B12.10 heterogeneidade | SM10 | M00-ID; M07 |
| B12.11 Reversibilidade terapêutica | — | M06 `[G1]` |
**Autoauditoria M09:** 11/11 blocos mapeados; 10 claims SM01–SM10 distribuídos sem promoção de nível.

---

## MÓDULO 10 — OUTRAS DOENÇAS/CONTEXTOS ONDE O MECANISMO É PERTURBADO (ILUSTRATIVO — FORA DA COBERTURA)
[REF_MODULO_10: Murphy, 2022; Xiao, 2022; Zugman, 2023]
- **PTSD como protótipo do eixo medo/extinção** (Suarez-Jimenez, 2020; Xiao, 2022) — interface, não centro exclusivo.
- **Transtornos de ansiedade** (Zugman, 2023; Lu, 2026).
- **[EXC — exclusões de escopo:** TBI/trauma físico (regra 6); AVC/Alzheimer (periferia da triagem); MDMA/farmacologia de adjuntos (fora do mecanismo); NAO-IDX do insumo (briefing §5).]
**Autoauditoria M10:** (i) ilustrativo; (ii) exclusões nomeadas.

---

## FECHAMENTO
Trinca B12: este GPM + BRIEFING_B12_NEUROBIOLOGIA_TRAUMA_RODADA0.md (tabela-mestra 36 PMIDs; NAO-IDX §5; pendências §8) + CHECKLIST_SANIDADE_GPM_B12.md. Âncoras: `SUPORTE/b12_anchormap.json` (36 → 36 PMIDs). Rodada 2: piloto psicoterapia (B12.11); sexo/medicação como moduladores; GWAS FKBP5×trauma; réplicas dos fenótipos de extinção em MDD/GAD.

## ÍNDICE AUTOR ↔ MÓDULO (bidirecional)
| Chave (Autor, Ano) | PMID | Módulos onde aparece |
|---|---|---|
| Heim & Nemeroff, 2001 | 11430844 | MÓDULO 00; MÓDULO 01 |
| Lee, 2025 | 40199321 | MÓDULO 01; MÓDULO 02; MÓDULO 06; MÓDULO 08 |
| Leschik, 2022 | 35872219 | MÓDULO 01; MÓDULO 03 |
| Liu, 2022 | 36151073 | MÓDULO 01 |
| Logue, 2018 | 29217296 | MÓDULO 00 |
| Lu, 2016 | 27049575 | MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 08 |
| Lu, 2026 | 42165096 | MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 05; MÓDULO 10 |
| Marusak, 2016 | 27824358 | MÓDULO 01; MÓDULO 02; MÓDULO 03 |
| McTeague, 2020 | 31964160 | MÓDULO 01; MÓDULO 07 |
| Menke, 2018 | 30086534 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 06; MÓDULO 07 |
| Miao, 2020 | 32085670 | MÓDULO 00; MÓDULO 01; MÓDULO 04; MÓDULO 08 |
| Miller, 2013 | 23468190 | MÓDULO 00; MÓDULO 01; MÓDULO 06 |
| Murphy, 2022 | 35599780 | MÓDULO 01; MÓDULO 02; MÓDULO 06; MÓDULO 08; MÓDULO 10 |
| Nikkheslat, 2019 | 31794798 | MÓDULO 01; MÓDULO 08 |
| Notaras, 2020 | 31900428 | MÓDULO 01; MÓDULO 03; MÓDULO 06 |
| Numakawa, 2023 | 37781095 | MÓDULO 01 |
| O'Doherty, 2015 | 25735885 | MÓDULO 01 |
| Paquola, 2016 | 27531235 | MÓDULO 00 |
| Pereira, 2021 | 34100334 | MÓDULO 00; MÓDULO 01; MÓDULO 03; MÓDULO 06 |
| Pollok, 2022 | 35189164 | MÓDULO 01; MÓDULO 05 |
| Price & Duman, 2019 | 31801966 | MÓDULO 00; MÓDULO 01; MÓDULO 06 |
| Rengasamy, 2021 | 35992016 | MÓDULO 01; MÓDULO 06 |
| Sartory, 2013 | 23536785 | MÓDULO 01 |
| Serra-Blasco, 2021 | 34256069 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 07; MÓDULO 08 |
| Shin, 2011 | 19625997 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03 |
| Suarez-Jimenez, 2020 | 31258096 | MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 07; MÓDULO 10 |
| Tartt, 2022 | 35354926 | MÓDULO 01; MÓDULO 06 |
| Tian, 2020 | 33053385 | MÓDULO 01; MÓDULO 02; MÓDULO 04; MÓDULO 07; MÓDULO 08 |
| Von Werne Baes, 2012 | 28183380 | MÓDULO 01 |
| Wang, 2021 | 34963057 | MÓDULO 01 |
| Wang, 2026 | 41660208 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 04; MÓDULO 05; MÓDULO 08 |
| Wingenfeld, 2014 | 25462901 | MÓDULO 01 |
| Xiao, 2022 | 36029627 | MÓDULO 01; MÓDULO 05; MÓDULO 10 |
| Yu, 2012 | 22442074 | MÓDULO 01; MÓDULO 02; MÓDULO 04; MÓDULO 07; MÓDULO 08 |
| Zhong, 2024 | 39304648 | MÓDULO 01; MÓDULO 07 |
| Zugman, 2023 | 37741177 | MÓDULO 00; MÓDULO 01; MÓDULO 03; MÓDULO 05; MÓDULO 08; MÓDULO 10 |
