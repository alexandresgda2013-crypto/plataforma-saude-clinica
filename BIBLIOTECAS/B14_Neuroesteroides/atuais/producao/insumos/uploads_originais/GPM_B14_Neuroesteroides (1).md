# GPM B14 — NEUROESTEROIDES/HORMÔNIOS EM ANSIEDADE E DEPRESSÃO — MOLDE v2.0
### Módulo da arquitetura neuropsiquiátrica · Rodada 0 · 2026-09-09
> **Status:** GPM reconstruído sobre a triagem B14 (arquitetura B14.1–B14.6; 30 âncoras estruturantes) + insumo "Artigos cientificos do mecanismo B14 neuroesteroides hormonios 08.09.26" (154 refs; 134 DOI→PMID auditados) + CSV de 07/set + mapa de âncoras da sessão anterior (aproveitado). 57 âncoras → 57 PMIDs verificados (b14_anchormap.json). Corpo limpo (zero PMID/DOI). Trinca: GPM + BRIEFING_B14_NEUROESTEROIDES_RODADA0.md + CHECKLIST_SANIDADE_GPM_B14.md.

---

## MÓDULO 00 — METADADOS, REGRAS FUNDADORAS, ESCOPO E FRONTEIRAS
[REF_MODULO_00: Paul, Pinna & Guidotti, 2020; Schüle, 2014; Chen, 2021; Porcu, 2016; Belelli, 2019]

**ID do mecanismo (B14):** eixo causal central `hormônios/esteroides (ovarianos, gestacionais, adrenais) → neuroesteroidogênese (pregnenolona→progesterona→5α-redução→3α-HSD→allopregnanolona/THDOC; DHEA; testosterona) → modulação alostérica GABA-A (sináptica/extrassináptica; subunidades δ; interneurônios PV) → circuitos amígdala–hipocampo–PFC e resposta ao estresse → fenótipos ansiosos/depressivos com janelas hormonais (ciclo, PMDD, gestação/pós-parto, perimenopausa)`. HPA/GR/MR/FKBP5 entra como **modulador/interface (B14.5)**, não como eixo concorrente.

**REGRAS FUNDADORAS:**
1. **Flutuação ≠ doença:** mudanças hormonais reprodutivas são exposição; a vulnerabilidade é **sensibilidade individual ao fluxo hormonal** (Kundakovic & Rocks, 2022; Schiller, 2016; Peters, 2024) — não "hormônio causa depressão".
2. **ALLO ↓ ≠ único mecanismo da depressão** — é um subeixo canônico bem ancorado (Schüle, 2014; Agís-Balboa, 2014; Locci & Pinna, 2017), não totalidade.
3. **Terapêutica neuroesteroide = sinal, não recomendação:** brexanolona/zuranolona aparecem como validação mecanística do eixo ALLO–GABA-A (Meltzer-Brody, 2018; Althaus, 2020; Epperson, 2023), nunca como protocolo.
4. **HPA é interface (B14.5):** GR/MR/cortisol/FKBP5 citados como moduladores, com âncora cruzada no B2/B12 (Gordon, 2015; Almeida, Pinna & Barros, 2021).
5. **Fenótipos reprodutivos são janelas naturais do mecanismo** (PMDD/pós-parto/perimenopausa), não subtipos diagnósticos fechados (Hantsoo & Epperson, 2020; Bixo, 2025; Gordon & Sander, 2021).
6. **Exógeno ≠ endógeno:** estrogênio terapêutico/HRT e contracepção ficam na camada intervenção-sinal (Zhang, 2023; Herson, 2022).
7. **Revisões = arquitetura** (Zorumski, 2019; Chen, 2021; Porcu, 2016; Pinna & Bortolato, 2025; Zorumski, 2025).
8. **Duplicatas eliminadas:** Evans 2005 ×2 e Hirani 2005 ×2 colapsadas (triagem); **"Trauger 2002" do insumo = van Broekhoven & Verkes 2003** (o DOI resolvia para o review de 2003) — correção registrada no briefing.
9. **Anos canônicos = print** (Stefaniak 1976→print 2023; Shivakumar? n/a; Antonoudiou = 2022 publicado, não preprint 2021; Sripada ×2 chaves).
10. **Multi-tag permitida** (ÂNCORA + JANELA REPRODUTIVA).

**Dicionário mínimo:** ALLO (allopregnanolona); THDOC; 5α-redutase; 3α-HSD/AKR1C; DHEA/S; PMDD; PPD (depressão pós-parto); GABA-A δ/α subunidades; PV (parvalbumina); brexanolona/zuranolona (moduladores GABA-A neuroesteroides); TSPO.

**Fronteiras:** HPA/GR detalhado → B2 (e FKBP5 → B12); neuroinflamação → B1; plasticidade → B3; B5 (GABA/glutamato) recebe a interface ALLO×GABA-A como ponte (regra da série: B14 realoca o braço allopregnanolona); sono/menopausa vasomotora → B10-ponte `[G1]`.

**Lacunas [G1] do M00:** (a) Stumper 2026 (sensibilidade afetiva ao fluxo) — insumo DOI apontava para review de 2020; (b) Lozza-Fiacco 2022 e Jarić 2019 não localizadas; (c) Belelli 2022/2021 (Curr Opin/J Neuroendocrin) não indexadas — Belelli 2019 cobre; (d) Rodríguez-Cerdeira 2026 (5αR neuro) — busca retornou outra paper do mesmo nome; Braccagni 2026 cobre o eixo 5αR; (e) Sundström-Poromaa 2020.

**Autoauditoria M00:** (i) eixo central verbatim da triagem no ID; (ii) HPA como interface (regra 4); (iii) fenótipos-reprodutivos como janelas (regra 5).

---

## MÓDULO 01 — MAPA DAS VIAS MOLECULARES (10 camadas numeradas)
[REF_MODULO_01: Liang & Rasmusson, 2018; Porcu, 2016; Belelli, 2019; Legesse, 2023; Griffin & Mellon, 1999]

**Via 1 — Neuroesteroidogênese.** Pregnenolona→progesterona→5α-redução→3α-HSD→ALLO; biossíntese, cinética e via da pregnenolona (Liang & Rasmusson, 2018; Tomaselli & Vallée, 2019; Stoffel-Wagner, 2001; He, 2019; Rossetti, 2016; Porcu, 2016; Koganti, 2025 — single-cell; Braccagni, 2026 — 5αR cerebrais; Riebel, 2024 — 5αR/TSPO).

**Via 2 — Neuroesteroides → GABA-A.** Modulação alostérica positiva; sináptico/extrassináptico; subunidade δ (Belelli, 2019; Legesse, 2023 — estrutura de ações opostas; Matthew, 2013; MacKenzie & Maguire, 2014; Lu, 2023 — PV hipocampais; Luscher, 2023; Lüscher & Möhler, 2019 — déficit GABAérgico).

**Via 3 — SSRI → neuroesteroidogênese.** Fluoxetina induz ALLO via 3α-HSD, dissociando serotonina de neuroesteroide (Griffin & Mellon, 1999) — ponte B4/B14.

**Via 4 — ALLO × estresse/HPA.** Estresse eleva/reduz ALLO conforme fase; HPA×ALLO integrados (Almeida, Pinna & Barros, 2021 — HPA+ALLO em MDD/PTSD; Gordon, 2015 — hormônios ovarianos+neuroesteroides+HPA; Sripada, 2013a/b — ALLO/DHEA e pregnenolona em circuitos emocionais/PTSD; Rasmusson, 2018 — LCR neuroesteroides GABAérgicos em PTSD).

**Via 5 — ALLO na depressão/ansiedade (translacional humana).** Níveis baixos em MDD/PPD/PMDD; correlação com sintomas (Schüle, 2014; Schüle, 2011; Chen, 2021; Paul, Pinna & Guidotti, 2020; Locci & Pinna, 2017; Agís-Balboa, 2014 — ↓5αR em PFC de deprimidos; Agís-Balboa, 2007 — ↓neuroesteroidogênese×isolamento; van Broekhoven & Verkes, 2003 — revisão; Bixo, 2025 — PMDD; Gao, 2023 — ALLO/GABA-A/PMDD; Hantsoo & Epperson, 2020).

**Via 6 — Janela gestação/pós-parto.** ALLO plasmático ↓ + depressão gestacional (Hellgren `[G1 insumo]`); perfil GABA periparto (Deligiannidis, 2016); brexanolona validando o eixo (Meltzer-Brody, 2018; Epperson, 2023; Walton & Maguire, 2019; Matthew, 2013); zuranolona (Althaus, 2020; Cutler, 2023; Marecki, 2023); PPD×ansiedade (Herson, 2022; Barbu `[G1]`).

**Via 7 — Janela ciclo menstrual/PMDD.** Sensibilidade ao metabólito da progesterona (Bixo, 2025; Gao, 2023; Hantsoo & Epperson, 2020; Nillni, 2021 — ciclo×ansiedade/PTSD; Stefaniak, 2023; Schweizer-Schubert `[G1]`; Zsido, 2017 — PET hormônio×circuito).

**Via 8 — Janela perimenopausa/menopausa.** Flutuação de estradiol × depressão (Gordon & Sander, 2021; Joffe `[G1]`; Maki `[G1]`; Mulhall `[G1]`; Nagda `[G1]`; Newhouse `[G1]`; Sander `[G1]`; Herson, 2022; Parikh `[G1 insumo]`); estrógeno exógeno×depressão — RCT meta (Zhang, 2023) como intervenção-sinal.

**Via 9 — Testosterona/DHEA e aging.** DHEA/pregnenolona como janelas (Sripada, 2013b; Reddy, 2010 — terapêutica neuroesteroide geral); Wolkowitz `[G1 — âncora antiga DHEA]`.

**Via 10 — Modelos animais causais.** ALLO×comportamento e oscilações (Takasu, 2024; Yawata, 2024 — ALLO vs diazepam); Xiaoyaosan/estresse (Guo, 2017); Antonoudiou, 2022 — ALLO media affective switching via oscilações; Walton `[G1 insumo]`.

**Autoauditoria M01:** (i) vias 5–8 = janelas reprodutivas separadas; (ii) via 3 dissocia SSRI-serotonina de ALLO; (iii) terapêutica (vias 6/8/9) rotulada sinal.

---

## MÓDULO 02 — MEDIADORES COM POLARIDADE + INVENTÁRIO NEGATIVO
[REF_MODULO_02: Schüle, 2014; Kundakovic & Rocks, 2022; Belelli, 2019; Agís-Balboa, 2014; Meltzer-Brody, 2018]

| Mediador | Papel | Direção documentada |
|---|---|---|
| ALLO | neuroesteroide GABA-A-agonista | ↓ em MDD/PPD/PMDD (Schüle, 2014; Agís-Balboa, 2014) |
| 5α-redutase | enzima-limitante | ↓ em PFC de deprimidos (Agís-Balboa, 2014); isoformas (Braccagni, 2026) |
| Estradiol | modulador cerebro-afetivo | flutuação → janela de vulnerabilidade (Gordon & Sander, 2021) |
| Progesterona/metabólitos | via ALLO | sensibilidade anormal em PMDD (Bixo, 2025) |
| DHEA(S)/pregnenolona | janela adaptativa | associação com circuitos emocionais (Sripada, 2013b) |
| GABA-A δ | alvo extrassináptico | modulação neuroesteroide (Belelli, 2019; Legesse, 2023) |
| BDNF | ponte plástica | fator neurotrófico associado (Almeida, 2021 — camada B3) |

**INVENTÁRIO NEGATIVO:** 1. "hormônio causa depressão" (regra 1). 2. "ALLO baixo = toda depressão" (regra 2). 3. "brexanolona/zuranolona = protocolo" (regra 3). 4. "HPA substitui o eixo neuroesteroide" (regra 4). 5. "PMDD/PPD/perimenopausa = diagnósticos fechados por hormônio" (regra 5). 6. "HRT = tratamento psiquiátrico" (regra 6). 7. "reviews = evidência causal" (regra 7). 8. "Trauger 2002 existe como âncora" (corrigido → van Broekhoven & Verkes, 2003). 9. "preprint Antonoudiou 2021" (usar publicado 2022). 10. "interneurônios PV = explicação completa" (Lu, 2023 é um braço).

**Autoauditoria M02:** (i) NEG 8–9 registram as correções de auditoria; (ii) direção por janela reprodutiva (não universal); (iii) tabela com pontes.

---

## MÓDULO 03 — TIPOS CELULARES E ESTRUTURAS
[REF_MODULO_03: Belelli, 2019; Lu, 2023; Agís-Balboa, 2014; Legesse, 2023; Antonoudiou, 2022]
- **Interneurônios PV do hipocampo** (ALLO×inibição) — Lu, 2023.
- **Sinapses GABA-A sinápticas/extrassinápticas (δ)** — Belelli, 2019; Legesse, 2023; Matthew, 2013.
- **PFC** (5αR ↓ nos deprimidos — humano post-mortem) — Agís-Balboa, 2014.
- **Amígdala/oscilações (affective switching)** — Antonoudiou, 2022.
- **Neuroesteroidogênese cerebral (célula-a-célula)** — Koganti, 2025; Braccagni, 2026.
**Autoauditoria M03:** (i) camada celular com âncoras; (ii) nenhum circuito humano in vivo novo além de PET (Zsido, 2017).

---

## MÓDULO 04 — GENÉTICA E EPIGENÉTICA
[REF_MODULO_04: Kundakovic & Rocks, 2022; Obermanns `[B13-ponte]`; Herson, 2022]
- **Vulnerabilidade feminina por flutuação hormonal** — revisão integrativa (Kundakovic & Rocks, 2022).
- **Polimorfismos GR/HPA×PPD** — `[G1 — Bechu 2022 não indexada]`.
- **Epigenética da neuroesteroidogênese** — `[G1]`.
**Autoauditoria M04:** (i) interação≠determinismo; (ii) [G1] registradas.

---

## MÓDULO 05 — BIOMARCADORES À BEIRA DO LEITO (SEM PROTOCOLO/CORTE)
[REF_MODULO_05: Schüle, 2014; Deligiannidis, 2016; Bixo, 2025; Rasmusson, 2018; Cutler, 2023]
- **Plasma/soro/LCR:** ALLO (fase do ciclo/gestação; LCR em PTSD — Rasmusson, 2018); metabólitos de progesterona; DHEA.
- **Janelas:** PMDD (fase lútea), PPD (3º trimestre/puerpério), perimenopausa (flutuação estradiol) — com heterogeneidade individual como achado central (Peters, 2024).
- **Regras:** nenhuma "dosagem ALLO" diagnóstica; sensibilidade ao fluxo ≠ nível hormonal absoluto (Peters, 2024; Schiller, 2016); sangue≠SNC.
**Autoauditoria M05:** (i) marcador contínuo por janela; (ii) sensibilidade individual como conceito.

---

## MÓDULO 06 — CONEXÕES CAUSAIS COM OUTROS BLOCOS (FÁRMACOS SÓ COMO SINAL)
[REF_MODULO_06: Almeida, Pinna & Barros, 2021; Griffin & Mellon, 1999; Meltzer-Brody, 2018; Zhang, 2023; Lu, 2023]
- **B14 ↔ B2 (HPA):** ALLO×HPA bidirecional (Almeida, 2021; Gordon, 2015) — interface B14.5.
- **B14 ↔ B5 (GABA/glutamato):** ALLO→GABA-A é a ponte estrutural (Belelli, 2019; Lüscher & Möhler, 2019) — recepção no B5.
- **B14 ↔ B4 (monoaminas):** SSRI induz neuroesteroidogênese (Griffin & Mellon, 1999) — mecanismo dissociado.
- **B14 ↔ B3 (plasticidade):** fatores neurotróficos×ALLO (Almeida, 2021; Lu, 2023) — ponte.
- **B14 ↔ B12 (trauma):** PTSD com LCR-ALLO ↓ (Rasmusson, 2018; Sripada, 2013a) — ponte.
- **B14 ↔ B1:** neuroinflamação periparto `[G1 âncora]`.
- **Terapias como sinal:** brexanolona/zuranolona (Meltzer-Brody, 2018; Althaus, 2020; Cutler, 2023; Epperson, 2023), HRT/estrógeno (Zhang, 2023; Herson, 2022), DHEA `[G1]`.
**Autoauditoria M06:** (i) pontes sem invasão de B5/B2; (ii) terapias = validação mecanística, não protocolo.

---

## MÓDULO 07 — SUBTIPOS / FENÓTIPOS CLÍNICOS (SEM INTERVENÇÃO)
[REF_MODULO_07: Bixo, 2025; Hantsoo & Epperson, 2020; Gordon & Sander, 2021; Schüle, 2014; Rasmusson, 2018]
- **F1 — PMDD:** sensibilidade anormal ao metabólito da progesterona (Bixo, 2025; Gao, 2023; Hantsoo & Epperson, 2020).
- **F2 — PPD:** ALLO/GABA periparto alterados (Deligiannidis, 2016; Walton & Maguire, 2019; Matthew, 2013).
- **F3 — Depressão perimenopausal:** janela de flutuação estradiol (Gordon & Sander, 2021; Herson, 2022).
- **F4 — MDD com ALLO/5αR ↓** (Schüle, 2014; Agís-Balboa, 2014; Locci & Pinna, 2017).
- **F5 — PTSD com neuroesteroides GABAérgicos ↓ (LCR)** (Rasmusson, 2018; Sripada, 2013a).
- **F6 — Fenótipo de alta sensibilidade hormonal sem doença hormonal:** Peters, 2024; Schiller, 2016 (dimensão, não categoria).
**Autoauditoria M07:** (i) janelas reprodutivas como substrato, não diagnóstico; (ii) F6 dimensional.

---

## MÓDULO 08 — CONTROVÉRSIAS, INCERTEZAS, LIMITES DE ESCOPO
[REF_MODULO_08: Peters, 2024; Kundakovic & Rocks, 2022; Zorumski, 2019; Chen, 2021; Legesse, 2023]
1. **Nível hormonal × sensibilidade ao fluxo** (Peters, 2024) — paradigma em disputa.
2. **Por que só uma subpopulação desenvolve sintomas** nas mesmas flutuações (Kundakovic & Rocks, 2022).
3. **ALLO ↓: causa ou marcador?** (Schüle, 2014; Chen, 2021).
4. **Ações opostas em GABA-A (concentração/subunidade/fase)** (Legesse, 2023).
5. **Tradução brexanolona→zuranolona** (via oral, sedação, contexto) (Cutler, 2023; Marecki, 2023) — sinal.
6. **DHEA/pregnenolona:** evidência mista `[G1]`.
7. **Testosterona em homens×humor** `[G1 — subcorpus pequeno]`.
8. **Interações estrogênio×antidepressivo** (Lozza-Fiacco `[G1]`).
9. **TSPO como alvo** (Riebel, 2024) — emergente.
10. **Confundimento contraceptivo/estrogênio exógeno** `[G1]`.
**Autoauditoria M08:** (i) controvérsias com fonte; (ii) [G1] explícitas.

---

## MÓDULO 09 — TABELA DE MAPEAMENTO × PROMPT 4.0 (B14.1–B14.6)
[REF_MODULO_09: ver M01–M08]
| Subeixo | Conteúdo | Onde |
|---|---|---|
| B14.1 Flutuação hormonal×vulnerabilidade | janelas ciclo/pós-parto/perimenopausa | Vias 5–8; M07 |
| B14.2 Neuroesteroidogênese | pregnenolona→ALLO; 5αR/3α-HSD | Via 1 |
| B14.3 Neuroesteroides→GABA-A | alosterismo/δ/PV | Via 2 |
| B14.4 Circuitos ansiedade/depressão | amígdala/hipocampo/PFC; switching | Via 10; M03 |
| B14.5 HPA/GR/MR (interface) | ALLO×HPA; PTSD-LCR | Via 4; M06 |
| B14.6 Evidência terapêutica (sinal) | brexanolona/zuranolona/estrógeno/SSRI→ALLO | Vias 3,6,8; M06 |
**Autoauditoria M09:** 6/6 subeixos mapeados; 30 âncoras estruturantes da triagem cobertas.

---

## MÓDULO 10 — OUTRAS DOENÇAS/CONTEXTOS ONDE O MECANISMO É PERTURBADO (ILUSTRATIVO — FORA DA COBERTURA)
[REF_MODULO_10: Reddy, 2010; Zorumski, 2025; Pinna & Bortolato, 2025]
- **Epilepsia/catamenial, anestesia neuroesteroide** — contexto (Reddy, 2010) `[G1 âncora]`.
- **Neuropsiquiatria do envelhecimento** (Zorumski, 2025; Pinna & Bortolato, 2025) — panorama.
- **[EXC — exclusões de escopo:** Alzheimer-ALLO (Tidke — SUPORTE), oncologia hormonal, esporte/doping, anestesia como especialidade; NAO-IDX do insumo (briefing §5).]
**Autoauditoria M10:** (i) ilustrativo; (ii) nada emprestado como prova psiquiátrica.

---

## FECHAMENTO
Trinca B14: este GPM + BRIEFING_B14_NEUROESTEROIDES_RODADA0.md (tabela-mestra 57 PMIDs; correções §4; pendências §8) + CHECKLIST_SANIDADE_GPM_B14.md. Âncoras: `SUPORTE/b14_anchormap.json` (57 → 57 PMIDs). Rodada 2: Stumper/Lozza-Fiacco/Jarić/Sundström-Poromaa relocalização; Belelli 2022; DHEA consolidada; TSPO; interações estrógeno×AD; homens/testosterona.

## ÍNDICE AUTOR ↔ MÓDULO (bidirecional)
| Chave (Autor, Ano) | PMID | Módulos onde aparece |
|---|---|---|
| Agís-Balboa, 2007 | 18003893 | MÓDULO 01 |
| Agís-Balboa, 2014 | 24781515 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 07 |
| Almeida, Pinna & Barros, 2021 | 34071053 | MÓDULO 00; MÓDULO 01; MÓDULO 06 |
| Althaus, 2020 | 32976892 | MÓDULO 00; MÓDULO 01; MÓDULO 06 |
| Antonoudiou, 2022 | 34561029 | MÓDULO 01; MÓDULO 03 |
| Belelli, 2019 | 32435660 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 06 |
| Bixo, 2025 | 40518728 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 07 |
| Braccagni, 2026 | 42492846 | MÓDULO 01; MÓDULO 02; MÓDULO 03 |
| Chen, 2021 | 34019980 | MÓDULO 00; MÓDULO 01; MÓDULO 08 |
| Cutler, 2023 | 37365161 | MÓDULO 01; MÓDULO 05; MÓDULO 06; MÓDULO 08 |
| Deligiannidis, 2016 | 27209438 | MÓDULO 01; MÓDULO 05; MÓDULO 07 |
| Epperson, 2023 | 36191643 | MÓDULO 00; MÓDULO 01; MÓDULO 06 |
| Gao, 2023 | 36937732 | MÓDULO 01; MÓDULO 07 |
| Gordon & Sander, 2021 | 34607269 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 07 |
| Gordon, 2015 | 25585035 | MÓDULO 00; MÓDULO 01; MÓDULO 06 |
| Griffin & Mellon, 1999 | 10557352 | MÓDULO 01; MÓDULO 06 |
| Guo, 2017 | 28825678 | MÓDULO 01 |
| Hantsoo & Epperson, 2020 | 32435664 | MÓDULO 00; MÓDULO 01; MÓDULO 07 |
| He, 2019 | 30321584 | MÓDULO 01 |
| Herson, 2022 | 35908135 | MÓDULO 00; MÓDULO 01; MÓDULO 04; MÓDULO 06; MÓDULO 07 |
| Koganti, 2025 | 40261706 | MÓDULO 01; MÓDULO 03 |
| Kundakovic & Rocks, 2022 | 35716803 | MÓDULO 00; MÓDULO 02; MÓDULO 04; MÓDULO 08 |
| Legesse, 2023 | 37607940 | MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 08 |
| Liang & Rasmusson, 2018 | 32440589 | MÓDULO 01 |
| Locci & Pinna, 2017 | 35809362 | MÓDULO 00; MÓDULO 01; MÓDULO 07 |
| Lu, 2023 | 36725341 | MÓDULO 01; MÓDULO 02; MÓDULO 03; MÓDULO 06 |
| Luscher, 2023 | 25436563 | MÓDULO 01 |
| Lüscher & Möhler, 2019 | 31275559 | MÓDULO 01; MÓDULO 06 |
| MacKenzie & Maguire, 2014 | 24402140 | MÓDULO 01 |
| Marecki, 2023 | 38116383 | MÓDULO 01; MÓDULO 08 |
| Matthew, 2013 | 32435663 | MÓDULO 01; MÓDULO 03; MÓDULO 07 |
| Meltzer-Brody, 2018 | 30177236 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 06 |
| Nillni, 2021 | 33404887 | MÓDULO 01 |
| Paul, Pinna & Guidotti, 2020 | 32435665 | MÓDULO 00; MÓDULO 01 |
| Peters, 2024 | 39143323 | MÓDULO 00; MÓDULO 05; MÓDULO 07; MÓDULO 08 |
| Pinna & Bortolato, 2025 | 41777158 | MÓDULO 00; MÓDULO 10 |
| Porcu, 2016 | 26681259 | MÓDULO 00; MÓDULO 01 |
| Rasmusson, 2018 | 30529908 | MÓDULO 01; MÓDULO 05; MÓDULO 06; MÓDULO 07 |
| Reddy, 2010 | 21094889 | MÓDULO 01; MÓDULO 10 |
| Riebel, 2024 | 41718149 | MÓDULO 01; MÓDULO 08 |
| Rossetti, 2016 | 27306650 | MÓDULO 01 |
| Schiller, 2016 | 33585496 | MÓDULO 00; MÓDULO 05; MÓDULO 07 |
| Schüle, 2011 | 21439354 | MÓDULO 01 |
| Schüle, 2014 | 24215796 | MÓDULO 00; MÓDULO 01; MÓDULO 02; MÓDULO 05; MÓDULO 07; MÓDULO 08 |
| Sripada, 2013a | 24302681 | MÓDULO 01; MÓDULO 06; MÓDULO 07 |
| Sripada, 2013b | 23348009 | MÓDULO 01; MÓDULO 02 |
| Stefaniak, 2023 | 14993041 | MÓDULO 01 |
| Stoffel-Wagner, 2001 | 11720889 | MÓDULO 01 |
| Takasu, 2024 | 38259500 | MÓDULO 01 |
| Tomaselli & Vallée, 2019 | 31525393 | MÓDULO 01 |
| Walton & Maguire, 2019 | 31709278 | MÓDULO 01; MÓDULO 07 |
| Yawata, 2024 | 38899227 | MÓDULO 01 |
| Zhang, 2023 | 37068417 | MÓDULO 00; MÓDULO 01; MÓDULO 06 |
| Zorumski, 2019 | 31649968 | MÓDULO 00; MÓDULO 08 |
| Zorumski, 2025 | 40127877 | MÓDULO 00; MÓDULO 10 |
| Zsido, 2017 | 29199875 | MÓDULO 01; MÓDULO 03 |
| van Broekhoven & Verkes, 2003 | 12420152 | MÓDULO 01; MÓDULO 02 |
