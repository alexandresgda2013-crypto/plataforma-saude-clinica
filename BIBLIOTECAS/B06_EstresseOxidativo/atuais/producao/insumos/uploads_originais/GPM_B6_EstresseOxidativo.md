# GPM B6 — ESTRESSE OXIDATIVO (EIXO B6-VITAMINA → TRANSSULFURAÇÃO → GLUTATIONA → REDOX) — MOLDE v2.0
### Módulo da arquitetura neuropsiquiátrica (ansiedade & depressão) · Rodada 0 · 2026-09-08
> **Status:** GPM reconstruído sobre a Matriz Canônica B6 (13 claims, triagem científica validada) + insumo "Artigos cientificos do mecanismo B6 Stress oxidativo 08.09.26" (93 refs, 81→83 DOI→PMID auditados no PubMed). 45 âncoras → 45 PMIDs verificados (b6_anchormap.json). Corpo limpo (zero PMID/DOI). Trinca: GPM + BRIEFING_B6_STRESS_OXIDATIVO_RODADA0.md + CHECKLIST_SANIDADE_GPM_B6.md.

---

## MÓDULO 00 — METADADOS, REGRAS FUNDADORAS, ESCOPO E FRONTEIRAS
[REF_MODULO_00: Gregory, 2016; Dalto & Matte, 2017; Cabrini, 1998; Shen, 2010; Wondrak & Jacobson, 2012]

**ID do mecanismo (B6):** desregulação do sistema redox/O&NS com eixo canônico validado na coleção: **estado de B6/PLP → atividade da transulfuração (CBS/CGL) → disponibilidade de cisteína → dinâmica do sistema glutationa → carga oxidativa/peroxidação → biomarcador → dano celular/tecidual**. O módulo modela o eixo B6-dependente da defesa redox; não afirma "depressão = estresse oxidativo alto".

**REGRAS FUNDADORAS (não reversíveis sem nova auditoria):**
1. **REGRA B6-STRESS-OXIDATIVO-01 (matriz):** é PROIBIDO inferir "B6 → redução de estresse oxidativo humano" a partir de (a) atividade antioxidante in vitro, (b) alteração de GSH em animal, (c) PLP → atividade de CBS/CGL, ou (d) PLP baixo ↔ marcador oxidativo elevado. Cada seta da cadeia exige evidência própria; etapa sem demonstração = "hipótese", "inferência mecanística" ou "associação".
2. **"B6 aumenta GSH" é claim proibido.** O claim canônico é: o estado de B6/PLP modifica o metabolismo e a dinâmica do sistema glutationa, mas o efeito sobre GSH/GSSG **depende de tecido, estado nutricional, condição oxidativa e modelo** (Cabrini, 1998; Davis, 2006; Lamers, 2009; Lima, 2006; Hsu, 2015).
3. **Revisão nunca vira ensaio causal** (Dalto & Matte, 2017 `[revisão; CORE-B]`; Wondrak & Jacobson, 2012 `[revisão mecanística]`; Gregory, 2016 `[revisão bioquímica]`).
4. **Observacional nunca vira causalidade:** associação PLP↔inflamação/oxidação em humanos permanece `[humano; ASSOCIATIVO; C]` (Shen, 2010; Pusceddu, 2019).
5. **Nrf2/NADPH = hipótese emergente** `[G1]` — proposta mecanística recente, não mecanismo estabelecido de suplementação de B6 (Kato, 2026 `[revisão/hipótese; C]`).
6. **Literatura CONTEXT de glutationa** (Averill-Bates, 2023; Giustarini, 2023; Labarrere & Kassab, 2022; Lapenna, 2023; Nuhu, 2020; Valgimigli, 2023 `[básico; CONTEXT]`) sustenta a biologia geral do GSH, mas **não gera claim de B6**.
7. **NON-CANONICAL não gera claim clínico:** estudos em plantas, bactérias, cristalografia pura ou sistemas não-mamíferos ficam como suporte estrutural, sem transferência direta.
8. **Vitâmeros não são intercambiáveis:** piridoxina, piridoxal/PLP e piridoxamina têm propriedades redox distintas; não interpolar efeitos entre eles (Wondrak & Jacobson, 2012; Ramis, 2019).
9. **Ação antioxidante direta in vitro ≠ benefício psiquiátrico.** O desfecho psiquiátrico do eixo B6-GSH não está demonstrado nesta coleção; qualquer ligação a ansiedade/depressão passa pelas pontes do M06 com status explícito.
10. **Ponte com B1 só em cascata, nunca em salto:** B6/PLP → transulfuração/GSH → menor vulnerabilidade oxidativa → potencial modulação de sinalização inflamatória → (aí sim B1).
11. **[EXTRAPOLAÇÃO POR ANALOGIA] sempre etiquetada:** captura de radicais em química/célula → tecido → humano exige a etiqueta em cada salto.
12. **Multi-tag permitida:** um estudo pode ser CORE + HUMAN ou SUPPORT + NEURAL (matriz v1.0).

**Dicionário mínimo:** PLP (piridoxal-5'-fosfato, forma ativa da B6); vitâmeros (piridoxina, piridoxal, piridoxamina e fosfatos); transulfuração (Hcy → cistationina → cisteína, via CBS e CGL/CSE); GSH/GSSG (glutationa reduzida/oxidada); GPx/GR (glutationa peroxidase/redutase); TBARS (peroxidação lipídica medida como substâncias reativas ao TBA); RCS/AGEs (espécies carbonílicas reativas/produtos finais de glicação).

**Fronteiras (o que NÃO é deste módulo):** origem mitocondrial do ROS → B9; neuroinflamação como consumidora → B1; eixo HPA/cortisol → B2; LPS/barreira intestinal como gatilho → B7; Se/Zn/Cu/Mg como cofatores redox → B8; plasticidade redox-sensível → B3; trauma → B12.

**Lacunas [G1] do M00:** (a) âncora neuronal-celular do claim B6.SM02.011 (candidato de 2024 não indexado no PubMed — ver briefing §5); (b) Nrf2 (regra 5); (c) polimorfismos CBS/CGL associados a fenótipo psiquiátrico — nada na coleção.

**Autoauditoria M00:** (i) a regra 1 está decomposta em todas as vias do M01 (cada seta com fonte própria ou status); (ii) nenhum claim da matriz foi promovido de nível (SUPORTE não virou NÚCLEO); (iii) o renome conceitual do ID preserva a matriz (13 claims) sem direção única "B6 = antioxidante = antidepressivo".

---

## MÓDULO 01 — MAPA DAS VIAS MOLECULARES (10 camadas numeradas)
[REF_MODULO_01: Gregory, 2016; Stipanuk, 2004; Stipanuk, 2020; Aitken, 2011; Banerjee, 2004; Meier, 2001; Taoka, 1999; Sbodio, 2018; Pajares, 2025]

**Via 1 — PLP como cofator das enzimas sulfuradas.** PLP é cofator de CBS e CGL/CSE; caracterização estrutural e cinética do sítio ativo estabelece a base `[básico; estrutural; ESTABELECIDO]` (Aitken, 2011; Banerjee, 2004; Meier, 2001; Taoka, 1999; Kabil, 1999; Yadav, 2012). CBS tem domínio hemérico regulador e comunicação allostérica PLP–heme (Yadav, 2012).

**Via 2 — Fluxo da transulfuração: Hcy → cistationina → cisteína.** Regulação pós-traduzional e integração com metabolismo de enxofre `[básico; revisão+experimental; ESTABELECIDO]` (Stipanuk, 2004; Stipanuk, 2020; Sbodio, 2018; Pajares, 2025).

**Via 3 — Cisteína → GSH.** A transulfuração fornece o aminoácido limitante para a síntese de glutationa `[básico; revisão+bioquímica; ESTABELECIDO com nuance]` (Dalto & Matte, 2017; Mosharov, 2000; Gould & Pazdro, 2019). Nuance: a conexão B6→GSH é B, não A (regra 2).

**Via 4 — Ciclo GSH/GSSG (GPx/GR/GRx, NADPH).** Biologia geral da defesa redox — camada CONTEXT sem claim de B6 `[básico; CONTEXT]` (Averill-Bates, 2023; Giustarini, 2023; Labarrere & Kassab, 2022; Lapenna, 2023; Nuhu, 2020; Valgimigli, 2023).

**Via 5 — Restrição/estado de B6 → fluxo transulfuration em humanos.** Restrição dietética controlada altera cisteína, cistationina e taxa de síntese de GSH eritrocitária, com respostas **não unidirecionais** (cistationina plasmática pode ELEVAR) `[humano; experimental de dieta; A/B]` (Davis, 2006; Lamers, 2009; Lima, 2006).

**Via 6 — Deficiência de B6 → peroxidação + resposta compensatória (animal).** `[animal; causal; B]` (Cabrini, 1998; Choi, 2009; Hsu, 2015). Detalhe crítico de Cabrini 1998: TBARS ↑ e razão GSH/GSSG ↓ com GPx/GR ↑ compensatórias e **GSH total sem diferença** — heterogeneidade preservada por regra.

**Via 7 — Atividade antioxidante direta dos vitâmeros (química/celular).** Captura de radicais (·OH, superóxido), proteção de peroxidação e potencial mitocondrial em modelos celulares `[celular/química; B]` (Kannan & Jain, 2004; Jain, 2001; Mahfouz, 2009; Mahfouz, 2004; Matxain, 2009; Matxain, 2006; Natera, 2012).

**Via 8 — Piridoxamina → RCS/AGEs e sequestro carbonílico.** Inibição da formação de produtos de glicação; propriedade quelante discutida `[celular/revisão; B; SUPPORT]` (Wondrak & Jacobson, 2012; Ramis, 2019).

**Via 9 — Humano observacional: PLP ↔ inflamação/estresse oxidativo.** Associação de status de B6 com CRP/marcadores de oxidação em coortes `[humano; ASSOCIATIVO; C]` (Shen, 2010; Pusceddu, 2019). Intervenção como sinal, sem causalidade: (Cheng, 2016; Lai, 2020).

**Via 10 — Hipótese Nrf2/NADPH + ponte B1.** Cadeia proposta B6/PLP → metabólitos antioxidantes/NADPH/GSH → sinalização Nrf2 `[hipótese; C; G1]` (Kato, 2026); e cascata para B1: menor vulnerabilidade oxidativa → modulação potencial de sinalização inflamatória (regra 10 — nunca em um passo).

**Autoauditoria M01:** (i) nenhuma via conecta B6 a desfecho psiquiátrico direto; (ii) Vias 5–6 preservam as duas direções da evidência (alteração × compensação); (iii) Via 10 está marcada como hipótese [G1], não como via estabelecida.

---

## MÓDULO 02 — MEDIADORES COM POLARIDADE + INVENTÁRIO NEGATIVO
[REF_MODULO_02: Cabrini, 1998; Davis, 2006; Lamers, 2009; Kannan & Jain, 2004; Ramis, 2019]

| Mediador | Papel no módulo | Polaridade esperada no eixo |
|---|---|---|
| PLP | cofator CBS/CGL | PLP ↓ → atividade transulfuração ↓ (contexto-dependente) |
| Homocisteína | substrato upstream | Hcy ↑ quando transulfuração ↓ |
| Cistationina | intermediário | pode ↑ na restrição de B6 (paradoxo Davis) |
| Cisteína | produto limitante do GSH | ↓ com fluxo ↓ (tecido-dependente) |
| GSH / GSSG | buffer redox principal | razão ↓ na deficiência; GSH total variável |
| GPx / GR | enzimas do ciclo | ↑ compensatórias (Cabrini) |
| TBARS/MDA | peroxidação | ↑ na deficiência animal |
| RCS/AGEs | alvo da piridoxamina | ↓ com captura carbonílica |
| CRP | inflamação associada | ↔ PLP (observacional) |
| NADPH | poder redutor | hipótese Nrf2 [G1] |

**INVENTÁRIO NEGATIVO (o que a evidência NÃO sustenta):**
1. **"B6 aumenta GSH"** — proibido (regra 2); evidência dividida (Lamers, 2009 vs Cabrini, 1998).
2. **"B6 → redução de estresse oxidativo humano"** — sem demonstração causal (regra 1; Shen, 2010 é associativo).
3. **"Antioxidant in vitro → benefício em tecido/órgão"** — não demonstrado (salto exige [EXTRAPOLAÇÃO POR ANALOGIA]).
4. **"Nrf2 é mecanismo comprovado da B6"** — é hipótese [G1] (Kato, 2026).
5. **"Literatura geral de GSH valida claim de B6"** — CONTEXT não gera claim (regra 6).
6. **"Deficiência de B6 reduz sempre o GSH total"** — Cabrini 1998: GSH total sem diferença com GPx/GR ↑ (fenótipo compensatório).
7. **"Vitâmeros são equivalentes"** — propriedades distintas (piridoxamina ≠ piridoxina) (regra 8).
8. **"PLP baixo causa inflamação"** — associação bidirecional possível; causalidade não estabelecida (Shen, 2010).
9. **"Suplementar B6 melhora ansiedade/depressão via redox"** — nenhum ensaio na coleção sustenta; fármacos/suplementos aparecem só como sinal.
10. **"Transulfuração = única fonte de cisteína"** — via dietética e de salvamento existem; o módulo cobre apenas a contribuição B6-dependente.

**Autoauditoria M02:** (i) os 10 itens negativos mapeiam 1:1 as tentações de simplificação da matriz; (ii) a tabela mantém polaridade com modificadores "contexto-dependente/variável"; (iii) nenhum mediador recebe status clínico.

---

## MÓDULO 03 — TIPOS CELULARES E ESTRUTURAS
[REF_MODULO_03: Cabrini, 1998; Hsu, 2015; Lamers, 2009; Gregory, 2016]
- **Hepatócito:** local principal da transulfuração; fígado como tecido-eixo da deficiência (Cabrini, 1998; Lima, 2006).
- **Miocárdio:** coração afetado na deficiência experimental (Cabrini, 1998).
- **Eritrócito:** taxa de síntese de GSH mensurável em humanos (Lamers, 2009).
- **Neurônio (modelo celular):** vulnerabilidade a H2O2 dependente de PLP/GSH — âncora pendente [G1] (candidato não indexado; briefing §5).
- **Plasma:** compartimento dos marcadores humanos (Davis, 2006; Shen, 2010).
- **CBS/CGL por tecido:** expressão hepática/renal/neural discutida nas revisões (Gregory, 2016; Sbodio, 2018).
**Autoauditoria M03:** (i) nenhum tipo celular recebeu fenótipo psiquiátrico; (ii) a ausência de âncora neuronal primária está declarada como lacuna, não camuflada.

---

## MÓDULO 04 — GENÉTICA E EPIGENÉTICA (ESTRUTURAL)
[REF_MODULO_04: Casique, 2013; Conter, 2025; Conter, 2020; Zhu, 2008; Yadav, 2012; Kabil, 1999; Singh, 2011]
- **CBS mutante/homocistinúria:** mutações patogênicas alteram comunicação estrutural e função (Casique, 2013; Conter, 2025; Zhu, 2008).
- **CBS em outros organismos:** biossíntese de cisteína e H2S em levedura (Conter, 2020) — NON-CANONICAL, sem claim humano.
- **Alostery PLP–heme:** base estrutural da regulação (Yadav, 2012; Kabil, 1999; Singh, 2011).
- **Polimorfismos comuns ↔ fenótipo psiquiátrico:** NADA na coleção `[G1]`.
- **Epigenética da transulfuração:** NADA na coleção `[G1]`.
**Autoauditoria M04:** (i) mutações monogênicas raras não são extrapoladas para variação comum; (ii) os dois [G1] do módulo estão no briefing §8.

---

## MÓDULO 05 — BIOMARCADORES À BEIRA DO LEITO (SEM PROTOCOLO/CORTE)
[REF_MODULO_05: Shen, 2010; Lamers, 2009; Davis, 2006; Pusceddu, 2019; Nuhu, 2020]
- **Exposição/estado:** PLP plasmático; Hcy total; cistationina; cisteína.
- **Sistema glutationa:** GSH/GSSG plasmático; taxa de síntese eritrocitária (Lamers, 2009); atividade GPx/GR.
- **Dano:** TBARS/MDA; produtos de peroxidação (Valgimigli, 2023 para contexto de medida; Nuhu, 2020 para methodologia).
- **Inflamação associada:** CRP (Shen, 2010; Pusceddu, 2019).
- **Regras:** nenhum marcador define diagnóstico; sangue ≠ SNC; direções dependentes de tecido (regra 2); marcadores CONTEXT valem para padronização de medida, não para claim de B6.
**Autoauditoria M05:** (i) nenhum corte numérico; (ii) hierarquia exposição→dano explícita; (iii) "associação" rotulada em todos os itens humanos.

---

## MÓDULO 06 — CONEXÕES CAUSAIS COM OUTROS BLOCOS (FÁRMACOS SÓ COMO SINAL)
[REF_MODULO_06: Shen, 2010; Dalto & Matte, 2017; Valgimigli, 2023; Kato, 2026]
- **B6 ↔ B1 (neuroinflamação):** cascata declarada (regra 10) — ROS/dano redox modulam sinalização inflamatória; **salto direto proibido**. Âncora inflamatória humana: CRP (Shen, 2010).
- **B6 ↔ B9 (mitocôndria):** ROS de origem mitocondrial é território do B9; aqui entra como consumidor/limitador (Kannan & Jain, 2004 mediu potencial mitocondrial em célula — sinal celular, não causalidade in vivo).
- **B6 ↔ B8 (micronutrientes):** Se (GPx), Zn/Cu (SOD), Mg — cofatores do sistema redox vivem no B8 `[G1: âncora cruzada pendente]`.
- **B6 ↔ B7 (intestino):** LPS/endotoxemia como gatilho exógeno de carga oxidativa — ponte declarada, âncora no B7.
- **B6 ↔ B2 (HPA):** cortisol→redox pontual `[G1]`.
- **B6 ↔ B3 (plasticidade):** proteínas/redox-sensíveis da sinapse `[G1: ponte a construir]`.
- **Terapia como sinal:** intervenções com vitâmeros em doença hepática/renal aparecem como janelas experimentais (Lai, 2020) — jamais como tratamento psiquiátrico.
**Autoauditoria M06:** (i) toda conexão tem status (declarada/âncora-no-outro-bloco/G1); (ii) nenhuma terapia é recomendada; (iii) as fronteiras do M00 foram respeitadas.

---

## MÓDULO 07 — SUBTIPOS / FENÓTIPOS CLÍNICOS (SEM INTERVENÇÃO)
[REF_MODULO_07: Cabrini, 1998; Lamers, 2009; Shen, 2010; Pusceddu, 2019; Davis, 2006]
- **F1 — Deficiência severa experimental (animal):** peroxidação ↑, GSH/GSSG ↓, compensação enzimática (Cabrini, 1998; Choi, 2009).
- **F2 — Restrição controlada em humano saudável:** fluxo alterado sem colapso do GSH total (Davis, 2006; Lamers, 2009; Lima, 2006).
- **F3 — Inflamação crônica/comorbidade (humano):** PLP baixo associado a CRP/marcadores oxidativos (Shen, 2010; Pusceddu, 2019).
- **F4 — Fenótipo compensatório:** GPx/GR ↑ sem ΔGSH total — assinatura de adaptação, não de simples "defesa menor" (Cabrini, 1998).
- **F5 — Hiperoxocisteinemia estrutural (rara):** CBS mutante — janela mecanística, não fenótipo psiquiátrico (Casique, 2013; Conter, 2025).
- **F6 — Neurônio sob carga H2O2:** dependência de PLP/GSH `[G1 — âncora pendente]`.
**Autoauditoria M07:** (i) fenótipos sem protocolo; (ii) F1–F2 mostram que "deficiência" tem gradientes; (iii) nenhum fenótipo vira subtipo diagnóstico de ansiedade/depressão.

---

## MÓDULO 08 — CONTROVÉRSIAS, INCERTEZAS, LIMITES DE ESCOPO
[REF_MODULO_08: Davis, 2006; Kato, 2026; Matxain, 2009; Shen, 2010; Lai, 2020]
1. **Direcionalidade** do eixo PLP↔inflamação (quem puxa quem? — Pusceddu, 2019 discute morbilidade).
2. **Paradoxo da cistationina** na restrição de B6 (Davis, 2006).
3. **Dose-resposta:** gradiente restrição × deficiência × suplementação não mapeado em humanos.
4. **Vitâmeros:** efeitos redox distintos — qual vitâmero em qual contexto?
5. **Relevância da captura in vitro** (Matxain, 2009; Mahfouz, 2009) em concentrações fisiológicas.
6. **Nrf2:** proposta recente (Kato, 2026) — risco de sobreinterpretação `[G1]`.
7. **Marcadores de peroxidação:** TBARS vs F2-isoprostanos vs HNE — discordâncias metodológicas (Valgimigli, 2023; Nuhu, 2020).
8. **RCTs de vitâmeros em doença sistêmica** (Lai, 2020) — transferir para psiquiatria é extrapolação indevida.
9. **Interpolação animal→humano** — sempre com [EXTRAPOLAÇÃO POR ANALOGIA].
10. **Ausência total de âncora psiquiátrica primária** nesta coleção — o módulo é um fornecedor de mecanismo, não de desfecho.
**Autoauditoria M08:** (i) as 10 controvérsias têm fonte ou status; (ii) nenhuma foi "resolvida" por conveniência.

---

## MÓDULO 09 — TABELA DE MAPEAMENTO × PROMPT 4.0 (MATRIZ CANÔNICA)
[REF_MODULO_09: ver M01–M08]
| Submódulo | Claim canônico (matriz B6 v1.0) | Onde está no GPM |
|---|---|---|
| B6.01 | PLP → cofator CBS/CGL | Via 1 |
| B6.02 | Transulfuração → cisteína | Via 2–3 |
| B6.03 | PLP → funcionamento do fluxo | Via 5 |
| B6.04 | Transulfuração → substratos do GSH | Via 3 |
| B6.05 | B6/PLP → dinâmica do sistema GSH (heterogênea) | Via 5–6 + regra 2 |
| B6.06 | Deficiência → estresse oxidativo experimental | Via 6 |
| B6.07 | Deficiência → resposta compensatória GPx/GR | Via 6 + F4 |
| B6.08 | Vitâmeros → ação antioxidante direta | Via 7 |
| B6.09 | Vitâmeros → ↓ROS/peroxidação celular | Via 7 |
| B6.10 | Piridoxamina → RCS/AGEs | Via 8 |
| B6.11 | PLP → GSH → vulnerabilidade neuronal | F6 `[G1]` |
| B6.12 | PLP ↔ inflamação/oxidação humana (associativo) | Via 9 + F3 |
| B6.13 | B6 → NADPH/GSH → Nrf2 [HIPÓTESE] | Via 10 `[G1]` |
**Autoauditoria M09:** 13/13 submódulos mapeados; nenhum claim reordenado em força (NÚCLEO permanece NÚCLEO; HIPÓTESE permanece HIPÓTESE).

---

## MÓDULO 10 — OUTRAS DOENÇAS ONDE O MECANISMO É PERTURBADO (AMOSTRA ILUSTRATIVA — FORA DA COBERTURA)
[REF_MODULO_10: Casique, 2013; Conter, 2025; Ramis, 2019; Lai, 2020]
- **Homocistinúria clássica** (CBS): arquetipo da transulfuração rompida (Casique, 2013; Conter, 2025).
- **Diabetes/complicações:** RCS/AGEs como alvo da piridoxamina (Ramis, 2019).
- **Doença hepática avançada:** janela experimental de vitâmeros (Lai, 2020).
- **[EXC — exclusões de escopo:** estudos em plantas/insetos/levedura sem gancho mamífero; cristalografia pura sem função; e o estudo neuronal 2024 não indexado (briefing §5).]
**Autoauditoria M10:** (i) amostra ilustrativa, não exaustiva; (ii) nenhuma doença foi usada para "comprovar" o eixo em psiquiatria.

---

## FECHAMENTO
Trinca B6: este GPM + BRIEFING_B6_STRESS_OXIDATIVO_RODADA0.md (tabela-mestra 45 PMIDs, NAO-IDX §5, pendências §8) + CHECKLIST_SANIDADE_GPM_B6.md (veredito). Âncoras: `SUPORTE/b6_anchormap.json` (45 chaves → 45 PMIDs). Rodada 2: transportadores/cofatores cruzados com B8; Nrf2; âncora neuronal; polimorfismos.

## ÍNDICE AUTOR ↔ MÓDULO (bidirecional)
| Chave (Autor, Ano) | PMID | Módulos onde aparece |
|---|---|---|
| Aitken, 2011 | 21435402 | MÓDULO 01 |
| Averill-Bates, 2023 | 36707132 | MÓDULO 00; MÓDULO 01 |
| Banerjee, 2004 | 15581573 | MÓDULO 01 |
| Cabrini, 1998 | 9844729 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 07 |
| Casique, 2013 | 23981774 | MÓDULO 04; MÓDULO 07; MÓDULO 10 |
| Cheng, 2016 | 27051670 | MÓDULO 01 |
| Choi, 2009 | 20090886 | MÓDULO 01; MÓDULO 07 |
| Conter, 2020 | 32887901 | MÓDULO 04 |
| Conter, 2025 | 40327797 | MÓDULO 04; MÓDULO 07; MÓDULO 10 |
| Dalto & Matte, 2017 | 28245568 | MÓDULO 00; MÓDULO 01; MÓDULO 06 |
| Davis, 2006 | 16424114 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 05; MÓDULO 07; MÓDULO 08 |
| Giustarini, 2023 | 37237960 | MÓDULO 00; MÓDULO 01 |
| Gould & Pazdro, 2019 | 31083508 | MÓDULO 01 |
| Gregory, 2016 | 26765812 | MÓDULO 00; MÓDULO 01; MÓDULO 03 |
| Hsu, 2015 | 25933612 | MÓDULO 00; MÓDULO 01; MÓDULO 03 |
| Jain, 2001 | 11165869 | MÓDULO 01 |
| Kabil, 1999 | 10531322 | MÓDULO 01; MÓDULO 04 |
| Kannan & Jain, 2004 | 14975445 | MÓDULO 01; MÓDULO 02; MÓDULO 06 |
| Kato, 2026 | 42196957 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 06; MÓDULO 08 |
| Labarrere & Kassab, 2022 | 36386929 | MÓDULO 00; MÓDULO 01 |
| Lai, 2020 | 32635181 | MÓDULO 01; MÓDULO 06; MÓDULO 08; MÓDULO 10 |
| Lamers, 2009 | 19515736 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 05; MÓDULO 07 |
| Lapenna, 2023 | 37683986 | MÓDULO 00; MÓDULO 01 |
| Lima, 2006 | 16857832 | MÓDULO 00; MÓDULO 01; MÓDULO 03; MÓDULO 07 |
| Mahfouz, 2004 | 15203107 | MÓDULO 01 |
| Mahfouz, 2009 | 20209473 | MÓDULO 01; MÓDULO 08 |
| Matxain, 2006 | 17134167 | MÓDULO 01 |
| Matxain, 2009 | 19558175 | MÓDULO 01; MÓDULO 08 |
| Meier, 2001 | 11483494 | MÓDULO 01 |
| Mosharov, 2000 | 11041866 | MÓDULO 01 |
| Natera, 2012 | 22231514 | MÓDULO 01 |
| Nuhu, 2020 | 32933160 | MÓDULO 00; MÓDULO 01; MÓDULO 05; MÓDULO 08 |
| Pajares, 2025 | 40141131 | MÓDULO 01 |
| Pusceddu, 2019 | 31129702 | MÓDULO 00; MÓDULO 01; MÓDULO 05; MÓDULO 07; MÓDULO 08 |
| Ramis, 2019 | 31480509 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 10 |
| Sbodio, 2018 | 30007014 | MÓDULO 01; MÓDULO 03 |
| Shen, 2010 | 19955400 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 05; MÓDULO 06; MÓDULO 07; MÓDULO 08 |
| Singh, 2011 | 21315854 | MÓDULO 04 |
| Stipanuk, 2004 | 15189131 | MÓDULO 01 |
| Stipanuk, 2020 | 33000151 | MÓDULO 01 |
| Taoka, 1999 | 10052944 | MÓDULO 01 |
| Valgimigli, 2023 | 37759691 | MÓDULO 00; MÓDULO 01; MÓDULO 05; MÓDULO 06; MÓDULO 08 |
| Wondrak & Jacobson, 2012 | 22116705 | MÓDULO 00; MÓDULO 01 |
| Yadav, 2012 | 22977242 | MÓDULO 01; MÓDULO 04 |
| Zhu, 2008 | 18476726 | MÓDULO 04 |
