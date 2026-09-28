#!/usr/bin/env python3
# B14 — V1 -> V2: rotação, BLOCO_14/BLOCO_15, apêndice [AT], metadados, asserts
import json, re, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
V1 = os.path.join(HERE, "B14 NEUROESTEROIDES V1 CANONICA.md")
V2 = os.path.join(HERE, "B14 NEUROESTEROIDES V2 CANONICA.md")
HIST = os.path.join(HERE, "producao", "historico", "v1_canonica_2026-09-09.md")

doc = open(V1, encoding="utf-8").read()
os.makedirs(os.path.dirname(HIST), exist_ok=True)
shutil.copyfile(V1, HIST)

# ---------- cabeçalho ----------
doc = doc.replace("# B14 NEUROESTEROIDES V1 CANÔNICA", "# B14 NEUROESTEROIDES V2 CANÔNICA", 1)
doc = doc.replace(
 "**ID canônico:** mecanismo_B14_neuroesteroides_hormonios_neuroativos · **Prompt v4.2** · Corte: 2026-09-07.",
 "**ID canônico:** mecanismo_B14_neuroesteroides_hormonios_neuroativos · **Prompt v4.2** · Corte: 2026-09-07; rodada [AT 2026-09-09], corte de literatura E-utilities 2026-09-09/10.", 1)
doc = doc.replace(
 "**artefato_rotulo:** CANÔNICA v1 · G1 (255/255 PMIDs do Briefing validados por eutils; 240 âncoras\nmecanísticas; 15 do bloco N = ruído de intervenção registrado à parte) + G2 + G3.",
 "**artefato_rotulo:** CANÔNICA v2 · G1 (255/255 PMIDs do Briefing originais validados por eutils; 240 âncoras\nmecanísticas; 15 do bloco N = ruído de intervenção registrado à parte) + G2 + G3 · **Rodada [AT 2026-09-09]**:\ninsumo externo (GPM B14 + RODADA0 + briefings + matriz ChatGPT) auditado ref a ref — 102 itens novos triados:\n50 ENTRA · 44 BAIXO (interface/conduta/redundância) · 7 EXC (malha) · 1 já vigente; total 290 referências.\nP-6 (2ª verificação cega) permanece pendente para a leva [AT].", 1)

# ---------- BLOCO_14 ----------
B14 = """---

## BLOCO_14 — ATUALIZAÇÃO CANÔNICA [[AT 2026-09-09]] · INSUMO EXTERNO AUDITADO REF A REF (P-7)

> **Proveniência.** Rodada [AT] do GPM B14: 57 âncoras estruturantes (índice oficial), §6 com 107 não citadas e §4/§8 com correções e lacunas, reconciliados contra a V1 pelo pipeline oficial G1 (esummary + efetch; abstract lido antes de incorporar) e G2/G3. Das 57 âncoras, 26 não constavam da V1 e foram resolvidas e incorporadas aqui; das 107 itens da §6, 24 entraram por evidência direta e 83 foram triados (44 rebaixados = interface HPA/B2/B5, conduta menopausal ou redundância; 7 excluídos por malha: etanol×2, tiques, anestesia, depressão-Alzheimer, esquizofrenia e bibliometria — decisões individuais em `producao/insumos/matriz_b14_decisao.json`). Dez divergências entre o rótulo do insumo e a identidade real do artigo foram **expostas** (BLOCO_15, regra 08); nenhum identificador foi inventado e nenhum número do insumo entrou sem fonte.

### B14.1 — Neuroesteroidogênese: enzimas, regionalidade e resolução celular

A via biossintética cerebral — colesterol → pregnenolona → progesterona → redução 5α → 3α-HSD → alopregnanolona — está documentada no cérebro humano com enzimas esteroidogênicas identificadas regionalmente (Stoffel-Wagner, 2001)[OB].
A presença de P450scc, aromatase, 5α-redutase e 3α-HSD no SNC humano sustenta a autonomia parcial da síntese cerebral e suas implicações clínicas (Stoffel-Wagner, 2003)[OB].
Estrógenos e progestágenos também são sintetizados de novo no tecido neural, com distribuição e funções próprias, incluindo proteção hipocampal (Rossetti, 2016)[OB].
As 17β-hidroxisteroides desidrogenases completam o quadro enzimático como etapas indispensáveis do metabolismo neuroesteroide central (He, 2019)[OB].
A resolução de célula única no cérebro murino mostra a neuroesteroidogênese distribuída por populações celulares distintas, com biossíntese intermediária compartimentada (Koganti, 2025)[ML].

* STOFFELWAGNER_2001[OB] | STOFFELWAGNER_2003[OB] | ROSSETTI_2016[OB] | HE_2019[OB] | KOGANTI_2025[ML] *

### B14.2 — Neuroesteroides → GABA-A: alosterismo, plasticidade de subunidades e comportamento

A sinalização GABAérgica por neuroesteroides endógenos — alopregnanolona, THDOC, androstanodiol — integra síntese local, flutuações fisiológicas e resposta ao estresse em saúde e doença (MacKenzie & Maguire, 2013)[OB].
Neuroesteroides derivados de hormônios ovarianos regulam a expressão e a plasticidade de subunidades do GABA-A no período reprodutivo, com leitura direta para a vulnerabilidade afetiva (MacKenzie & Maguire, 2014)[OB].
A ponte entre a modulação alostérica positiva dos PAMs endógenos e o comportamento foi sistematizada de forma mecanística, fechando a cadeia molécula→circuito→fenótipo (Belelli, 2022)[OB].
Experimentalmente, a ação da alopregnanolona e do GABA sobre o receptor GABA-A é modulada por neuroesteroides de modo dependente de contexto (Strömberg, 2006)[ML].
No nível celular, a alopregnanolona potencia a inibição em interneurônios parvalbumina do hipocampo — um braço celular específico do efeito neuroesteroide (Lu, 2023)[ML].

* MACKENZIE_2013[OB] | MACKENZIE_2014[OB] | BELELLI_2022[OB] | STROMBERG_2006[ML] | LU_2023[ML] *

### B14.3 — SSRI → neuroesteroidogênese (ponte B4↔B14)

Inibidores seletivos da recaptação de serotonina alteram diretamente a atividade de enzimas neuroesteroidogênicas e elevam a síntese de alopregnanolona por mecanismo farmacodinâmico dissociado da recaptação de serotonina (Griffin & Mellon, 1999)[ML].

* GRIFFIN_1999[ML] *

### B14.4 — Estresse, circuitos e modelos animais causais (vias 4 e 10)

O isolamento social prolongado em camundongos reduz a biossíntese de alopregnanolona em circuitos corticolímbicos — com redução da 5α-redutase tipo I — associando-se a alterações comportamentais (Agís-Balboa, 2007)[ML].
A alopregnanolona é multifuncional no eixo do estresse: sintetizada por 5α-redutase/3α-HSD, interage bidirecionalmente com o HPA em transtornos relacionados ao estresse (Bali & Jaggi, 2014)[OB].
Em modelo de desenvolvimento em dois insultos, sexo e ciclo estral modulam fenótipos de ansiedade e depressão, evidenciando interação desenvolvimento×hormônio (Jarić, 2019)[ML].
Em ratos sob estresse crônico imprevisível, a reversão de comportamento tipo-depressivo por intervenção fitoterápica acompanhou normalização de neuroesteroides e das enzimas de síntese — evidência do eixo; o veículo herbário não é o conteúdo canônico (Guo, 2017)[ML].
A comparação direta alopregnanolona×diazepam em camundongos mostra efeitos diferenciais sobre comportamento social por modulação distinta de oscilações, distinguindo farmacologicamente o modulador neuroesteroide (Yawata, 2024)[ML].

* AGISBALBOA_2007[ML] | BALI_2014[OB] | JARIC_2019[ML] | GUO_2017[ML] | YAWATA_2024[ML] *

### B14.5 — Evidência humana transversal e circuitos (via 5)

No córtex pré-frontal post-mortem (área de Brodmann 9) de pacientes com depressão maior, a 5α-redutase tipo I está reduzida — substrato molecular humano da deficiência de alopregnanolona (Agís-Balboa, 2014)[EC].
Neuroesteroides 3α-reduzidos e precursores flutuam ao longo da gestação e do pós-parto em mulheres, com relação ao humor (Gilbert Evans, 2005)[EC].
A vulnerabilidade feminina aumentada a transtornos de ansiedade, trauma e estresse foi integrada em revisão com papel potencial dos hormônios sexuais (Li & Graham, 2017)[OB].
Os transtornos de humor e a ansiedade acompanham os estados hormonais ao longo da vida da mulher, da puberdade à menopausa, em revisão narrativa de escopo reprodutivo (Antonelli, 2022)[OB].
A revisão etiológico-mecanística de Kundakovic & Rocks disseca a flutuação hormonal como fator de risco feminino para depressão e ansiedade (Kundakovic & Rocks, 2022)[OB].
Em humanos, a administração de pregnenolona elevou a alopregnanolona e associou-se a redução da atividade da amígdala e da ínsula, com maior conectividade de regulação emocional (Sripada, 2013)[EC].
Alopregnanolona e DHEA séricos modulam a conectividade de repouso da amígdala em humanos — níveis maiores associados a menor acoplamento amígdala–hipocampo (Sripada, 2014)[EC].
A janela das transições hormonais foi mapeada por tomografia por emissão de pósitrons como caminho para ligar flutuação hormonal a alterações neuroquímicas (Zsido, 2017)[OB].
A interface inflamatória no cérebro feminino sistematiza mecanismos sexo-específicos em transtornos de humor e estresse, sem substituir o eixo neuroesteroide (Marano, 2026)[OB].

* AGISBALBOA_2014[EC] | EVANS_2005[EC] | LI_2017[OB] | ANTONELLI_2022[OB] | KUNDAKOVIC_2022[OB] | SRIPADA_2013[EC] | SRIPADA_2014[EC] | ZSIDO_2017[OB] | MARANO_2026[OB] *

### B14.6 — Janela gestação → pós-parto

Alopregnanolona sérica baixa no final da gestação associou-se a sintomas depressivos (Hellgren, 2014)[EC].
As trajetórias longitudinais de estradiol e progesterona da gestação ao pós-parto formam classes latentes que se associam diferencialmente a desfechos afetivos — a heterogeneidade individual é o achado central (Dukic, 2024)[EC].
Metabólitos da progesterona durante a gestação associaram-se a ansiedade perinatal em coorte prospectiva (Etyemez, 2023)[EC].
Os biomarcadores da psiquiatria reprodutiva foram revisados como oportunidade translacional das janelas hormonais, sem ferramenta diagnóstica pronta (Etyemez, 2025)[OB].
Em mulheres saudáveis acompanhadas longitudinalmente, a alopregnanolona e o humor no periparto sugerem relação em forma de U, reforçando o paradigma da sensibilidade individual (Grötsch, 2024)[EC].
Estudo exploratório em múltiplos tempos do periparto ligou a alopregnanolona a sintomas depressivos e ansiosos (Standeven, 2022)[EC].

* HELLGREN_2014[EC] | DUKIC_2024[EC] | ETYEMEZ_2023[EC] | ETYEMEZ_2025[OB] | GROTSCH_2024b[EC] | STANDEVEN_2022[EC] *

### B14.7 — Janela ciclo menstrual e PMDD: sensibilidade, não nível

Os efeitos da fase do ciclo menstrual em ansiedade e TEPT foram revisados com mecanismos e limitações metodológicas explícitas (Nillni, 2021)[OB].
A PMDD é conceituada como transtorno de sensibilidade subótima aos neuroesteroides, mediada pela sensibilidade do GABA-A à alopregnanolona (Gao, 2023)[OB].
A revisão abrangente da progesterona e da alopregnanolona — 'amiga ou adversa?' — organiza propriedades, metabolismo e efeitos no humor feminino (Sundström-Poromaa, 2020)[OB].
Nos transtornos de humor reprodutivos, o fator causal proposto é a sensibilidade a esteroides — não os níveis absolutos — com mediação do receptor GABA-A e do estresse (Schweizer-Schubert, 2021)[OB].
O risco de suicídio relacionado ao ciclo menstrual foi revisado na perspectiva molecular, com a flutuação ovariana cíclica como janela de vulnerabilidade (Ross, 2026)[OB].

* NILLNI_2021[OB] | GAO_2023[OB] | SUNDSTROMPOROMAA_2020[OB] | SCHWEIZERSCHUBERT_2021[OB] | ROSS_2026[OB] *

### B14.8 — Janela perimenopausa e menopausa

Revisão sistemática conclui que a menopausa eleva o risco de depressão e ansiedade diagnosticadas (Alblooshi, 2023)[EC].
Em amostra comunitária de mulheres de meia-idade, os sintomas depressivos e ansiosos variaram significativamente por status menopausal (Mulhall, 2018)[EC].
A avaliação transversal de mulheres na transição peri/pós-menopausa documentou depressão, ansiedade e cognição (Nagda, 2023)[EC].
Na transição menopausal tardia, a relação entre testosterona e sintomas depressivos foi examinada longitudinalmente (Sander, 2021)[EC].
O modelo neurocognitivo estrógeno–estresse–depressão organiza a interação em comentário conceitual (Newhouse & Albert, 2015)[OB].
A depressão perimenopausal foi revista sob a ótica da inflamação e do estresse oxidativo, como alvos e interface (Yu, 2025)[OB].
Na transição menopausal, maior variabilidade do estradiol predisse fenótipos depressivos com ansiedade e anedonia; a sensibilidade basal ao estradiol predisse a resposta sintomática em ensaio experimental (Lozza-Fiacco, 2022)[EC].

* ALBLOOSHI_2023[EC] | MULHALL_2018[EC] | NAGDA_2023[EC] | SANDER_2021[EC] | NEWHOUSE_2015[OB] | YU_2025[OB] | LOZZAFIACCO_2022[EC] *

### B14.9 — Camada terapêutica como validação mecanística (sinal — não protocolo; P20)

A revisão do papel da alopregnanolona na fisiopatologia e no tratamento da depressão pós-parto consolida a janela puerperal como prova de conceito do eixo (Meltzer-Brody & Kanes, 2020)[OB].
A leitura por que/como funcionam os tratamentos à base de alopregnanolona na depressão pós-parto explicita a validação mecanística do eixo alopregnanolona–GABA-A por via regulatória (Walton & Maguire, 2019)[OB].
A perspectiva histórica da alopregnanolona — da fisiopatologia molecular à terapêutica — sistematiza três décadas de ações não-genômicas via GABA-A (Paul, Pinna & Guidotti, 2020)[OB].
As ações pleiotrópicas da alopregnanolona foram propostas como base dos benefícios em TEPT e depressão, mantendo o estatuto de perspectiva mecanística (Boero, 2020)[OB].
Os moduladores do receptor GABA-A como agentes emergentes nos transtornos depressivos foram revisados como camada terapêutica—sinal (Guan & Li, 2026)[OB].
A meta-análise de ensaios randomizados com estrogênio exógeno mostrou melhora do humor depressivo em mulheres — evidência de intervenção, não do eixo endógeno (Zhang, 2023)[EC].
A revisão dos agentes hormonais na depressão associada à menopausa permanece no domínio exógeno—sinal, distinto da fisiologia endógena (Herson & Kulkarni, 2022)[OB].

* MELTZERBRODY_2020[OB] | WALTON_2019[OB] | PAUL_2020[OB] | BOERO_2020[OB] | GUAN_2026[OB] | ZHANG_2023[EC] | HERSON_2022[OB] *

---

## BLOCO_15 — REGRAS CANÔNICAS DA RODADA [AT] (B14-REGRA-01..10), EXPOSIÇÕES, MALHA E LACUNAS [G1]

**B14-REGRA-01 — Flutuação ≠ doença.** Mudanças hormonais reprodutivas são exposição; a vulnerabilidade canônica é a **sensibilidade individual ao fluxo hormonal** (Kundakovic & Rocks, 2022; Schweizer-Schubert, 2021; Lozza-Fiacco, 2022; Grötsch, 2024) — nunca "hormônio causa depressão".

**B14-REGRA-02 — Alopregnanolona↓ ≠ único mecanismo.** O subeixo ALLO/5α-redutase está bem ancorado (Agís-Balboa, 2014 post-mortem; Hellgren, 2014), mas é parte — não a totalidade — da fisiopatologia depressiva.

**B14-REGRA-03 — Terapêutica neuroesteroide = sinal.** Brexanolona/zuranolona/agentes hormonais aparecem como validação mecanística (Meltzer-Brody & Kanes, 2020; Walton & Maguire, 2019; Paul, 2020; Guan & Li, 2026) — proibido protocolo, dose ou conduta (P20).

**B14-REGRA-04 — HPA é interface.** Cortisol/GR/MR/FKBP5 entram como moduladores com âncoras cruzadas a B2/B12; 34 itens HPA-genéricos do insumo foram rebaixados por redundância ou deslocamento de território (não apagam a ponte B14.5).

**B14-REGRA-05 — Fenótipos reprodutivos = janelas naturais.** Ciclo/PMDD, gestação-pós-parto e perimenopausa são substrato do mecanismo (Hellgren, Dukic, Nillni, Gao, Alblooshi, Lozza-Fiacco), não subtipos diagnósticos fechados nem "doença hormonal".

**B14-REGRA-06 — Exógeno ≠ endógeno.** Estrogênio terapêutico, reposição hormonal e contracepção ficam na camada intervenção-sinal (Zhang, 2023; Herson, 2022); revisões de conduta (guidelines, THR em menopausa) foram rebaixadas.

**B14-REGRA-07 — Revisões = arquitetura.** Os 27 itens [OB] da leva compilam e organizam o mecanismo; não contam como prova causal isolada.

**B14-REGRA-08 — Chave do insumo ≠ identidade do artigo; exposições desta rodada.** Dez rótulos do insumo resolviam para artigos distintos e foram corrigidos com o autor real (esummary): (i) "Stefaniak 2023" = Stoffel-Wagner 2003 (biossíntese cerebral humana; a Stefaniak 2023 real permanece sem identificador — [G1]); (ii) "Luscher 2023" = MacKenzie & Maguire 2013 (o Luscher 2023 real já era vigente na V1); (iii) "Matthew 2013" = Meltzer-Brody & Kanes 2020 — o item que o §4 do briefing julgava "não localizado" estava vivo sob rótulo alheio; (iv) "Schiller 2016" = Schweizer-Schubert 2021 (era a lacuna [G1] da Via 7; Schiller 2016 real permanece [G1]); (v) "Locci & Pinna 2017" = Lozza-Fiacco 2022 (o Locci & Pinna 2017 real já era vigente — REF_LOCCI_2017); (vi) "Stumper 2026" = Sundström-Poromaa 2020 (o §4 a dava por não resolvida; Stumper 2026 permanece [G1]); (vii) "Jain 2005" = Jarić 2019 (item §4 "não resolvida"; Jain 2005 permanece [G1]); (viii) "Franco 2016" = Gądek-Michalska 2013 (rebaixada: HPA genérica); (ix) "Vaudry 2022" = Von Werne Baes 2012 (rebaixada; o Vaudry 2022 real já era vigente); (x) "Riebel 2024 / §8.3" = Rodríguez-Cerdeira 2026, **já vigente na V1** (REF_RODRIGUEZCERDEIRA_2026), e o Riebel real já era vigente (REF_RIEBEL_2025) — lacuna TSPO/5α-redutase triplamente coberta, sem nova inclusão.

**B14-REGRA-09 — Anos canônicos = ano de impressão.** "Sripada 2013a" é print 2014; "Belelli 2021" é print 2022; "Ross 2025" é print 2026 — os identificadores internos usam sempre o ano de impressão do PubMed.

**B14-REGRA-10 — Malha de exclusão registrada.** Excluídos por escopo (não por falta de qualidade): substrato de etanol (Hirani 2005; VanDoren 2000), exacerbação de tiques (Bortolato 2021 — hipótese ALLO×estresse em Tourette), anestesia geral (Tateiwa 2024), depressão associada a Alzheimer (Tidke 2025), HPA×esquizofrenia (Mikulska 2021) e bibliometria sem conteúdo mecanístico (Guo 2023). CORREÇÕES §4 JÁ EFETIVAS NA V1 (não requerem ação): "Trauger 2002" = van Broekhoven & Verkes 2003 (REF_VAN_2003 vigente); Antonoudiou preprint→publicado 2022 (REF_ANTONOUDIOU_2022); Evans 2005 e Hirani 2005 duplicatas internas colapsadas (Evans entra uma única vez; Hirani excluída por malha etanol).

**Lacunas [G1] que permanecem declaradas (sem fonte = não incorporar):** Stefaniak 2023 real; Schiller 2016 real; Stumper 2026; Jain 2005; Matthew & Samba 2013 real; ensaios de DHEA/pregnenolona em depressão unipolar com desfechos padronizados; testosterona em homens×humor (subcorpus pequeno); interações estrógeno×antidepressivo em humanos dedicadas; confundimento por contracepção hormonal nos estudos de ciclo; Parikh 2025 (não indexada — NAO-IDX).

---
"""

# ---------- inserir B14/B15 antes de TABELA DE EVIDÊNCIAS ----------
mk = "## TABELA DE EVIDÊNCIAS"
assert mk in doc
doc = doc.replace(mk, B14 + mk, 1)

# ---------- nota de fecho + apêndice ----------
APPEND = """---

### Nota de fecho v1 → v2 (rodada [AT 2026-09-09])
A versão anterior (v1, 240 âncoras mecanísticas sobre os 255 PMIDs validados do briefing original) foi integralmente preservada em `producao/historico/v1_canonica_2026-09-09.md`. A rodada [AT] auditou ref a ref o insumo externo completo do GPM B14 (índice de 57 âncoras; §6 com 107 itens; correções §4; lacunas §8), incorporou 50 referências novas com verificação G1 (autor/ano/tema/abstract), rebaixou 44 por escopo e excluiu 7 pela malha, expôs 10 divergências de identidade entre rótulo do insumo e artigo real e consolidou as 10 regras canônicas da biblioteca no BLOCO_15. Totais da v2: **290 referências · 290 vínculos · 290 registros de auditoria**. P-6 (segunda verificação independente, avaliador cego) permanece pendente para toda a leva [AT].

---

## APÊNDICE DE REFERÊNCIAS (MÓDULO 09) — ATUALIZAÇÃO [AT 2026-09-09]

* STOFFELWAGNER_2001[OB] | STOFFELWAGNER_2003[OB] | ROSSETTI_2016[OB] | HE_2019[OB] | KOGANTI_2025[ML] | MACKENZIE_2013[OB] | MACKENZIE_2014[OB] | BELELLI_2022[OB] | STROMBERG_2006[ML] | LU_2023[ML] | GRIFFIN_1999[ML] | AGISBALBOA_2007[ML] | BALI_2014[OB] | JARIC_2019[ML] | GUO_2017[ML] | YAWATA_2024[ML] *
* AGISBALBOA_2014[EC] | EVANS_2005[EC] | LI_2017[OB] | ANTONELLI_2022[OB] | KUNDAKOVIC_2022[OB] | SRIPADA_2013[EC] | SRIPADA_2014[EC] | ZSIDO_2017[OB] | MARANO_2026[OB] | HELLGREN_2014[EC] | DUKIC_2024[EC] | ETYEMEZ_2023[EC] | ETYEMEZ_2025[OB] | GROTSCH_2024b[EC] | STANDEVEN_2022[EC] | NILLNI_2021[OB] | GAO_2023[OB] | SUNDSTROMPOROMAA_2020[OB] | SCHWEIZERSCHUBERT_2021[OB] | ROSS_2026[OB] *
* ALBLOOSHI_2023[EC] | MULHALL_2018[EC] | NAGDA_2023[EC] | SANDER_2021[EC] | NEWHOUSE_2015[OB] | YU_2025[OB] | LOZZAFIACCO_2022[EC] | MELTZERBRODY_2020[OB] | WALTON_2019[OB] | PAUL_2020[OB] | BOERO_2020[OB] | GUAN_2026[OB] | ZHANG_2023[EC] | HERSON_2022[OB] *
"""

# ---------- mapa de âncoras (id -> trecho literal da prosa) ----------
REFS = json.load(open(os.path.join(HERE, "b14_refs_data.json")))
anchor_map = {}
patterns = {
 "REF_STOFFELWAGNER_2001": "(Stoffel-Wagner, 2001)[OB]",
 "REF_STOFFELWAGNER_2003": "(Stoffel-Wagner, 2003)[OB]",
 "REF_ROSSETTI_2016": "(Rossetti, 2016)[OB]",
 "REF_HE_2019": "(He, 2019)[OB]",
 "REF_KOGANTI_2025": "(Koganti, 2025)[ML]",
 "REF_MACKENZIE_2013": "(MacKenzie & Maguire, 2013)[OB]",
 "REF_MACKENZIE_2014": "(MacKenzie & Maguire, 2014)[OB]",
 "REF_BELELLI_2022": "(Belelli, 2022)[OB]",
 "REF_STROMBERG_2006": "(Strömberg, 2006)[ML]",
 "REF_LU_2023": "(Lu, 2023)[ML]",
 "REF_GRIFFIN_1999": "(Griffin & Mellon, 1999)[ML]",
 "REF_AGISBALBOA_2007": "(Agís-Balboa, 2007)[ML]",
 "REF_BALI_2014": "(Bali & Jaggi, 2014)[OB]",
 "REF_JARIC_2019": "(Jarić, 2019)[ML]",
 "REF_GUO_2017": "(Guo, 2017)[ML]",
 "REF_YAWATA_2024": "(Yawata, 2024)[ML]",
 "REF_AGISBALBOA_2014": "(Agís-Balboa, 2014)[EC]",
 "REF_EVANS_2005": "(Gilbert Evans, 2005)[EC]",
 "REF_LI_2017": "(Li & Graham, 2017)[OB]",
 "REF_ANTONELLI_2022": "(Antonelli, 2022)[OB]",
 "REF_KUNDAKOVIC_2022": "(Kundakovic & Rocks, 2022)[OB]",
 "REF_SRIPADA_2013": "(Sripada, 2013)[EC]",
 "REF_SRIPADA_2014": "(Sripada, 2014)[EC]",
 "REF_ZSIDO_2017": "(Zsido, 2017)[OB]",
 "REF_MARANO_2026": "(Marano, 2026)[OB]",
 "REF_HELLGREN_2014": "(Hellgren, 2014)[EC]",
 "REF_DUKIC_2024": "(Dukic, 2024)[EC]",
 "REF_ETYEMEZ_2023": "(Etyemez, 2023)[EC]",
 "REF_ETYEMEZ_2025": "(Etyemez, 2025)[OB]",
 "REF_GROTSCH_2024b": "(Grötsch, 2024)[EC]",
 "REF_STANDEVEN_2022": "(Standeven, 2022)[EC]",
 "REF_NILLNI_2021": "(Nillni, 2021)[OB]",
 "REF_GAO_2023": "(Gao, 2023)[OB]",
 "REF_SUNDSTROMPOROMAA_2020": "(Sundström-Poromaa, 2020)[OB]",
 "REF_SCHWEIZERSCHUBERT_2021": "(Schweizer-Schubert, 2021)[OB]",
 "REF_ROSS_2026": "(Ross, 2026)[OB]",
 "REF_ALBLOOSHI_2023": "(Alblooshi, 2023)[EC]",
 "REF_MULHALL_2018": "(Mulhall, 2018)[EC]",
 "REF_NAGDA_2023": "(Nagda, 2023)[EC]",
 "REF_SANDER_2021": "(Sander, 2021)[EC]",
 "REF_NEWHOUSE_2015": "(Newhouse & Albert, 2015)[OB]",
 "REF_YU_2025": "(Yu, 2025)[OB]",
 "REF_LOZZAFIACCO_2022": "(Lozza-Fiacco, 2022)[EC]",
 "REF_MELTZERBRODY_2020": "(Meltzer-Brody & Kanes, 2020)[OB]",
 "REF_WALTON_2019": "(Walton & Maguire, 2019)[OB]",
 "REF_PAUL_2020": "(Paul, Pinna & Guidotti, 2020)[OB]",
 "REF_BOERO_2020": "(Boero, 2020)[OB]",
 "REF_GUAN_2026": "(Guan & Li, 2026)[OB]",
 "REF_ZHANG_2023": "(Zhang, 2023)[EC]",
 "REF_HERSON_2022": "(Herson & Kulkarni, 2022)[OB]",
}
# trecho = a linha inteira da prosa que contém a citação
for rid, pat in patterns.items():
    hit = None
    for line in B14.splitlines():
        if pat in line and line.strip() and not line.strip().startswith("*"):
            hit = line.strip()
            break
    assert hit, f"sem linha para {rid}"
    anchor_map[rid] = hit

for rid, anc in anchor_map.items():
    n = doc.count(anc)
    assert n == 1, f"âncora {rid} x{n}"

# inserir nota+apêndice logo antes do APÊNDICE original
mk2 = "## APÊNDICE DE REFERÊNCIAS (MÓDULO 09)"
assert mk2 in doc
doc = doc.replace(mk2, APPEND.strip() + "\n", 1)

# varredura de dígitos longos (exclui listras de ids e rs-ids/códigos)
body = doc
hits = [m.group(0) for m in re.finditer(r'\d{7,9}', body)]
assert len(hits) == 0, f"vazamento de dígitos: {hits[:5]}"

open(V2, "w", encoding="utf-8").write(doc)
os.remove(V1)
json.dump(anchor_map, open(os.path.join(HERE, "b14_ancoras.json"), "w"), ensure_ascii=False, indent=1)
print("V2 gravada:", V2)
print("palavras:", len(doc.split()), "| refs novas ancoradas:", len(anchor_map))
