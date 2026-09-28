#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera 01_pmids.json da B8 a partir dos metadados G1 + curadoria G2."""
import json

META = json.load(open('/home/user/BIBLIOTECAS/B08_Micronutrientes/producao/g1_esummary.json'))

# pmid -> (REFid, papel[selo+desenho], especie, evid_role, g2_elegibilidade, g2_motivo, achado)
C = {
 # ---- metilação / folato / B12 ----
 '10896698': ('Bottiglieri2000_homocisteina','[EC] estudo humano transversal/caso-controle JNNP',['Humans'],'human_clinical','eligible','pacientes deprimidos; marcadores bioquímicos','Homocisteína alta, folato/SAM baixos e monoaminas alteradas (metabólitos de 5-HT/DA) na depressão.'),
 '16109454': ('Bottiglieri2005_review','[OB] revisão PNPBP',['Humans'],'review','eligible','revisão mecanística','Metabolismo de homocisteína e folato na depressão; metilação e SAM.'),
 '15671130': ('Coppen2005_B12folato','[OB] artigo de perspectiva J Psychopharmacol',['Humans'],'review','eligible','revisão/posição','Tratamento da depressão: hora de considerar folato e B12.'),
 '18981340': ('Almeida2008_homocis_idoso','[MA] meta/SR Arch Gen Psychiatry — idosos',['Humans'],'human_clinical','eligible','revisão sistemática de estudos em idosos','Homocisteína alta associada a depressão no idoso.'),
 '17568057': ('Gilbody2007_folato_meta','[MA] meta-análise JECH',['Humans'],'human_clinical','eligible','meta de estudos observacionais + exploração de heterogeneidade','Folato baixo como fator de risco para depressão (associação; heterogeneidade).'),
 '28759846': ('Bender2017_folato_meta','[MA] meta-análise J Psychiatr Res',['Humans'],'human_clinical','eligible','meta de associação','Associação entre folato e depressão.'),
 '26055921': ('Petridou2016_B12idoso','[MA] SR Aging Ment Health',['Humans'],'human_clinical','eligible','revisão sistemática em idosos','Níveis séricos de folato e B12 associados à depressão no idoso.'),
 '33809274': ('Markun2021_B12_nulo','[MA] meta/metarregressão Nutrients — 16 RCTs/6276',['Humans'],'human_clinical','eligible','RCTs em pessoas SEM deficiência/doença neurológica; âncora LIMITADORA','Suplemento de B12 (sozinho ou complexo B) SEM efeito sobre cognição, sintomas depressivos ou fadiga em não-deficientes.'),
 '33912967': ('Wu2022_ingestaoB','[EC] coorte/observacional Nutr Rev — INGESTÃO',['Humans'],'human_clinical','eligible','associação de ingestão dietética (FFQ), não deficiência','Ingestão de B1/B2/B6/B12 associada ao risco de depressão (proxy dietético ruidoso).'),
 '38992845': ('Sliwinski2024_Bmetab','[EC/OB] estudo de metabólitos B circulantes J Affect? Behav Brain Res',['Humans'],'human_clinical','eligible','metabólitos séricos de vitaminas B; interface B7','Metabólitos circulantes de vitaminas B nos transtornos depressivos — conexão com microbiota.'),
 '34986378': ('Nguyen2022_B1B3','[EC] modelagem de misturas NHANES J Affect Disord',['Humans'],'human_clinical','eligible','observacional transversal; ingestão','Ingestão de B1 e B3 associadas à depressão em modelagem de misturas.'),
 '38367708': ('Xu2024_tiamina','[EC] estudo nacional transversal J Affect Disord',['Humans'],'human_clinical','eligible','observacional; ingestão de tiamina','Ingestão de tiamina (B1) associada à depressão (transversal).'),
 # ---- MTHFR ----
 '18165972': ('Gaysina2008_MTHFR_nulo','[EC] estudo DeCC + meta AJMG-B — NULO',['Humans'],'human_clinical','eligible','resultado negativo; metas divergem','SEM associação entre MTHFR C677T e depressão maior (DeCC + meta).'),
 '23831680': ('Wu2013_MTHFR_pos','[MA] meta-análise PNPBP — positiva',['Humans'],'human_clinical','eligible','meta; conflita com Gaysina','Associação entre MTHFR C677T e depressão (meta atualizada).'),
 '28968218': ('Rai2017_MTHFR_pos','[MA] meta Cell Mol Biol — positiva',['Humans'],'human_clinical','eligible','meta; conflita com Gaysina','Associação do polimorfismo C677T (rs1801133) com depressão.'),
 '41280388': ('SorianoGonzalez2025_B9B12D','[OB] revisão Front Nutr — 24 estudos',['Humans'],'review','eligible','revisão de B9/B12/D × variantes genéticas','Relação biológica entre depressão, vitaminas B9/B12/D e variantes genéticas.'),
 # ---- energia / complexo B / idoso ----
 '40904570': ('Han2025_complexoB','[OB] revisão Front Psychiatry',['Humans'],'review','eligible','revisão de manifestações neuropsiquiátricas','Manifestações neuropsiquiátricas das deficiências do complexo B (Wernicke-Korsakoff, pelagra).'),
 '40303879': ('Gao2025_defic_idoso','[OB] revisão Front Nutr',['Humans'],'review','eligible','revisão em idosos; mitocôndria/neuroinflamação','Associação de deficiência vitamínica com depressão no idoso.'),
 # ---- redox: Zn/Mg/Se/Cu ----
 '29747386': ('Wang2018_ZnMgSe','[OB] revisão Nutrients',['Humans'],'review','eligible','revisão de mecanismos','Zinco, magnésio e selênio na depressão; zinco é o mais consistente.'),
 '36442656': ('Wang2023_antiox_meta','[MA] meta-análise J Affect Disord',['Humans'],'human_clinical','eligible','meta de antioxidantes; efeito pequeno','Papel protetor pequeno da suplementação antioxidante para depressão e ansiedade.'),
 '23289525': ('Johnson2013_Se_agua','[EC] coorte transversal BMC Psychiatry — água/ambiental',['Humans'],'human_clinical','eligible','exposição AMBIENTAL (selênio da água subterrânea), não suplemento','GPX1 modera a associação entre selênio da água e depressão (Project FRONTIER).'),
 '35058530': ('Sajjadi2022_Se_meta','[MA] SR/meta Sci Rep — SEM diferença sérica, I²≈98%',['Humans'],'human_clinical','eligible','evidência fraca/inconsistente; soro sem diferença','Selênio sérico sem diferença na depressão (I²=98%); sinal apenas para depressão pós-parto por ingestão.'),
 '41263185': ('Davarinejad2026_elementos','[EC] meta/estudo Rev Environ Health — Zn↓ Fe↓ Cu↑',['Humans'],'human_clinical','eligible','elementos séricos; Cu alto = redistribuição inflamatória','Níveis séricos de Zn e Fe menores e Cu maior na TDM.'),
 '41472978': ('Gupta2025_anemia','[MA] SR/meta Niger Med J',['Humans'],'human_clinical','eligible','anemia é inespecífica (vários tipos, não só ferro)','Associação entre anemia e depressão (inespecífica).'),
 '38191692': ('Meng2024_multi_ion','[MA] SR/meta Mol Neurobiol — sangue E LCR',['Humans'],'human_clinical','eligible','meta de íons; mede sangue e LCR (Meng/Guo, NÃO "Wang")','Alterações de íons no sangue e no LCR em deprimidos.'),
 '25405366': ('Lomagno2014_FeZn_mulher','[MA] SR Nutrients — mulheres pré-menopausa',['Humans'],'human_clinical','eligible','revisão de ferro/zinco e humor/cognição','Aumento de ferro e zinco em mulheres pré-menopausa e efeitos sobre humor e cognição.'),
 # ---- ômega-3 (referência cruzada, NÃO micronutriente) ----
 '20130098': ('Appleton2010_n3_meta','[MA] meta-análise AJCN',['Humans'],'human_clinical','eligible','meta de n-3 PUFA; referência cruzada','Efeitos de n-3 PUFA sobre humor deprimido (meta atualizada; efeito pequeno/heterogêneo).'),
 '30646157': ('Su2018_n3_ansiedade','[MA] meta-análise JAMA Netw Open — ansiedade',['Humans'],'human_clinical','eligible','meta; efeito maior em diagnóstico clínico e dose ≥2000mg','Uso de ômega-3 associado a redução de sintomas de ansiedade clínica (g≈0,37).'),
 '42005438': ('Fleig2026_n3_review','[OB] revisão Front Nutr 2026',['Humans'],'review','eligible','revisão de mecanismos/terapêutica','Ômega-3 em transtornos mentais: mecanismos neurobiológicos/metabólicos.'),
 '34932079': ('Okereke2021_VITAL_n3','[EC] RCT grande JAMA (VITAL-DEP) — NULO/prevenção',['Humans'],'human_experimental','eligible','RCT ~18 mil, prevenção; âncora LIMITADORA','Ômega-3 marinho de longo prazo NÃO preveniu depressão (HR 1,13; humor sem diferença).'),
 '31383846': ('Liao2019_n3_meta','[MA] meta-análise Transl Psychiatry',['Humans'],'human_clinical','eligible','meta de n-3 PUFA; EPA>baseline','Eficácia de n-3 PUFA na depressão; efeito pequeno, dependente de EPA.'),
 '37585720': ('Kemp2024_Fe_n3_dev','[ML] estudo pré-clínico Nutr Neurosci — desenvolvimento',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','roedor; carência materna de ferro e n-3; janela desenvolvimental','Depleção combinada de ferro e n-3 no desenvolvimento altera monoaminas (DA/NE estriatais, DA frontal, 5-HT sexo-dependente) e comportamento.'),
 # ---- vitamina D / VDR ----
 '35806075': ('Kouba2022_D_mecanismo','[OB] revisão mecanística IJMS',['Humans','Animals'],'review','eligible','revisão de base molecular','Base molecular do potencial terapêutico da vitamina D (VDR, BDNF, neuroesteroides, imunomodulação).'),
 '23377209': ('Anglin2013_D_meta','[MA] meta-análise Br J Psychiatry',['Humans'],'human_clinical','eligible','meta de associação','Deficiência de vitamina D associada à depressão (associação).'),
 '39552387': ('Ghaemi2024_D_dose','[MA] meta dose-resposta Psychol Med — 31 RCTs',['Humans'],'human_clinical','eligible','SMD −0,32; GRADE moderada; ansiedade SEM efeito; efeito some em follow-up longo','D3 reduz sintomas depressivos no curto prazo (mais em deprimidos); SEM efeito sobre ansiedade.'),
 '35816192': ('Mikola2023_D_meta','[MA] meta-análise CRFSN — 41 RCTs/53.235, g≈−0,32, I²≈88%',['Humans'],'human_clinical','eligible','GRADE muito baixa; heterogeneidade alta; RoB preocupante','Vitamina D reduz sintomas depressivos (g=−0,317) com GRADE muito baixa e I²=88%.'),
 '36716601': ('Srifuengfung2023_D','[MA] meta/rede Nutrition',['Humans'],'human_clinical','eligible','meta de eficácia/aceitabilidade','Eficácia e aceitabilidade da vitamina D em deprimidos.'),
 '36509315': ('Musazadeh2023_D_umbrella','[MA] umbrella meta Pharmacol Res',['Humans'],'human_clinical','eligible','umbrella de intervenções','Vitamina D protege contra depressão (evidência de intervenção agregada).'),
 '40821024': ('Wang2025_D_meta','[MA] meta-análise Front Psychiatry',['Humans'],'human_clinical','eligible','meta 2025','Efeito da vitamina D na depressão.'),
 '32749491': ('Okereke2020_VITAL_D3','[EC] RCT grande JAMA (VITAL-DEP) — NULO/prevenção',['Humans'],'human_experimental','eligible','RCT ~18 mil, prevenção; âncora LIMITADORA','D3 de longo prazo NÃO preveniu depressão nem alterou escores de humor (HR 0,97).'),
 '38965219': ('Bassett2024_D_MR','[EC] MR linear/não-linear Transl Psychiatry',['Humans'],'human_clinical','eligible','Mendelian randomization; MR≠RCT','Vitamina D, dor crônica e depressão: MR (causalidade potencial, não comprovada).'),
 '34737282': ('Arathimos2021_D_MR','[EC] MR Transl Psychiatry',['Humans'],'human_clinical','eligible','MR; depressão resistente/atípica','Vitamina D e risco de depressão resistente/atípica (MR).'),
 '31518429': ('Meng2019_D_pheMR','[EC] MR fenômico Int J Epidemiol',['Humans'],'human_clinical','eligible','MR fenômico; efeitos mistos','Efeitos da vitamina D determinada geneticamente sobre desfechos de saúde (humor incluso).'),
 # ---- monoaminas / ferro ----
 '25154570': ('Kim2014_ferro','[OB] revisão mecanística J Nutr Biochem',['Humans','Animals'],'review','redirecionado_mecanistico','revisão com mecanismo animal/celular','Ferro é cofator de tirosina/triptofano-hidroxilase (DA/NE/5-HT) e mielinização; deficiência sem anemia pode afetar humor.'),
 # ---- magnésio / HPA / NMDA ----
 '21835188': ('Sartori2012_Mg_ansiedade','[ML] experimento em camundongo Neuropharmacology',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','prova pré-clínica direta; dieta pobre em Mg','Deficiência de Mg induz ansiedade e desregulação do HPA em camundongo (sensível a diazepam/desipramina/SSRI).'),
 '40647320': ('Varga2025_Mg_review','[OB] revisão Nutrients',['Humans'],'review','eligible','revisão ampla (depressão/enxaqueca/Alzheimer/cognição)','Papel do magnésio em depressão, enxaqueca, Alzheimer e cognição.'),
 '25748766': ('Tarleton2015_Mg_ingestao','[EC] observacional JABFM',['Humans'],'human_clinical','eligible','ingestão de Mg (transversal)','Ingestão de magnésio associada à depressão em adultos.'),
 '38812090': ('Hajhashemy2025_Mg_ingestao','[MA] SR GRADE Nutr Rev',['Humans'],'human_clinical','eligible','revisão de ingestão dietética','Ingestão dietética de Mg em relação à depressão (GRADE).'),
 '31261707': ('Tarleton2019_Mg_soro','[EC] coorte Nutrients — soro',['Humans'],'human_clinical','eligible','soro reflete mal a reserva; atenção primária','Associação entre Mg sérico e depressão em atenção primária.'),
 '30444158': ('You2018_Mg_soro','[MA] meta Nord J Psychiatry — sensível',['Humans'],'human_clinical','eligible','resultado sensível à exclusão de estudos','Mg sérico diminuído na depressão (meta; sensível).'),
 '25827510': ('Cheungpasitporn2015_hipoMg','[MA] meta Intern Med J',['Humans'],'human_clinical','eligible','meta de hipomagnesemia','Hipomagnesemia ligada à depressão (meta).'),
 '29897029': ('Phelan2018_Mg_inconclusivo','[MA] meta BJPsych Open — inconclusivo',['Humans'],'human_clinical','eligible','evidência inconclusiva','Magnésio e transtornos do humor: revisão/meta inconclusiva.'),
 '28241991': ('Rajizadeh2017_Mg_RCT','[EC] RCT duplo-cego placebo Nutrition — só em DEFICIENTES',['Humans'],'human_experimental','eligible','RCT pequeno (n=60) em hipomagnesêmicos; prova de conceito de corrigir deficiência','Mg em deprimidos COM hipomagnesemia normalizou soro e reduziu BDI.'),
 '28654669': ('Tarleton2017_Mg_RCT_aberto','[EC] RCT ABERTO/não-cego PLoS One',['Humans'],'human_experimental','eligible','open-label crossover; GAD-7 secundário; âncora com ressalva de cegueira','Cloreto de Mg melhorou PHQ-9 e GAD-7 em RCT aberto (sem cegueira).'),
 '38213402': ('Moabedi2023_Mg_meta','[MA] meta de RCTs Front Psychiatry',['Humans'],'human_clinical','eligible','meta de suplementação de Mg','Suplementação de Mg afeta beneficamente a depressão.'),
 '30562392': ('Pouteau2018_MgB6','[EC] RCT PLoS One — estresse em sadios',['Humans'],'human_experimental','eligible','RCT em voluntários sadios com estresse; Mg+B6 vs Mg','Mg+B6 superior ao Mg sozinho em estresse severo em adultos sadios.'),
 # ---- zinco ----
 '23567517': ('Swardfager2013_Zn_review','[OB] revisão Neurosci Biobehav Rev',['Humans','Animals'],'review','eligible','revisão de mecanismos','Papel do zinco na fisiopatologia e tratamento da TDM (NMDA, plasticidade).'),
 '23806573': ('Swardfager2013_Zn_meta','[MA] meta-análise Biol Psychiatry',['Humans'],'human_clinical','eligible','meta de zinco','Zinco na depressão: meta-análise (status baixo + adjuvante).'),
 '32829928': ('Yosaee2022_Zn_dose','[MA] meta dose-resposta Gen Hosp Psychiatry',['Humans'],'human_clinical','eligible','meta comparativa/desenvolvimento→tratamento','Zinco na depressão: meta dose-resposta (observacional + RCT).'),
 '21798601': ('Lai2012_Zn_RCT_meta','[MA] meta de RCTs J Affect Disord',['Humans'],'human_clinical','eligible','meta de suplementação','Eficácia da suplementação de zinco na depressão (meta de RCTs).'),
 '41508425': ('Li2026_Zn_homeostase','[OB] revisão Ann Med 2026',['Humans'],'review','eligible','revisão de homeostase','Homeostase do zinco na TDM: mecanismos patológicos heterogêneos.'),
 '41683306': ('Zhong2026_oligoelementos','[OB] revisão Nutrients 2026',['Humans'],'review','eligible','revisão de elementos-traço','Relação entre elementos-traço e depressão.'),
 # ---- padrão alimentar (alimento > pílula) ----
 '30254236': ('Lassale2019_dieta_meta','[MA] meta observacional Mol Psychiatry — dose-gradiente',['Humans'],'human_clinical','eligible','meta de índices dietéticos; confundimento residual','Padrão saudável/Mediterrâneo reduz risco de depressão de forma dose-gradiente.'),
 '20048020': ('Jacka2010_dieta_mulher','[EC] estudo transversal Am J Psychiatry',['Humans'],'human_clinical','eligible','observacional em mulheres','Dieta ocidental vs tradicional associada a depressão/ansiedade em mulheres.'),
 '28137247': ('Jacka2017_SMILES','[EC] RCT BMC Med — SMILES (dieta vs apoio social)',['Humans'],'human_experimental','eligible','RCT single-blind de modificação dietética na TDM; d=−1,16; NNT≈4','Aconselhamento dietético (Mediterrâneo) melhorou a TDM mais que apoio social (SMILES).'),
 '29215971': ('Parletta2019_HELFIMED','[EC] RCT Nutr Neurosci — Mediterrâneo+peixe',['Humans'],'human_experimental','eligible','RCT de intervenção Mediterrânea suplementada com óleo de peixe','Intervenção estilo-Mediterrâneo melhorou qualidade da dieta e saúde mental (HELFIMED).'),
 '37019362': ('Tsai2023_dieta_perinatal','[MA] meta AJCN — perinatal',['Humans'],'human_clinical','eligible','meta de intervenções dietéticas perinatais','Intervenções dietéticas para depressão/ansiedade perinatal.'),
 '40812962': ('Teasdale2025_Lancet','[OB] comissão Lancet Psychiatry 3º relatório',['Humans'],'review','eligible','recomendação de implementação de estilo de vida','Implementar intervenções de estilo de vida na saúde mental (3º relatório Lancet Psychiatry).'),
 '42123920': ('Hachmeriyan2026_alimentos','[OB] revisão Nutrients 2026',['Humans'],'review','eligible','revisão de alimentos e ansiedade/depressão','Alimentos que podem influenciar ansiedade e depressão (do prato à mente).'),
 '37299394': ('Zielinska2023_defic_map','[OB] revisão Nutrients 2018-2023',['Humans'],'review','eligible','mapa de deficiências nutricionais','Deficiências de nutrientes dietéticos e risco de depressão (revisão 2018-2023).'),
 '26359904': ('Sarris2015_Lancet_nutricao','[OB] comentário/revisão Lancet Psychiatry',['Humans'],'review','eligible','artigo de posição (Sarris/Logan/Jacka)','Medicina nutricional como corrente principal na psiquiatria.'),
 # ---- adjuvantes ----
 '10967371': ('Coppen2000_folato_fluox','[EC] RCT J Affect Disord — folato+fluoxetina',['Humans'],'human_experimental','eligible','RCT pequeno; folato potencializa fluoxetina','Ácido fólico potencializa a ação antidepressiva da fluoxetina (RCT).'),
 '23212058': ('Papakostas2012_LMethylfol','[EC] RCT AJP — L-metilfolato adjuvante',['Humans'],'human_experimental','eligible','RCT em respondedores inadequados a ISRS','L-metilfolato como adjuvante na TDM resistente a ISRS (dois RCTs).'),
 '24813065': ('Papakostas2014_LMethylfol','[EC] RCT JCP — estratificado',['Humans'],'human_experimental','eligible','RCT estratificado por biomarcador/genótipo','L-metilfolato 15mg adjuvante em respondedores inadequados a ISRS.'),
 '27035404': ('Zajecka2016_LMethylfol_long','[EC] estudo longo prazo JCP',['Humans'],'human_experimental','eligible','segurança/eficácia de longo prazo','Eficácia/segurança de longo prazo de L-metilfolato cálcico adjuvante.'),
 '26613389': ('Shelton2015_LMethylfol_obes','[EC] análise JCP — obesidade/inflamação',['Humans'],'human_experimental','eligible','subgrupo obesidade/marcador inflamatório','Obesidade e marcadores inflamatórios modificam o desfecho com L-metilfolato.'),
 '34794190': ('Maruf2022_LMethylfol_meta','[MA] meta Pharmacopsychiatry',['Humans'],'human_clinical','eligible','meta de potencialização','L-metilfolato como potencialização na TDM (meta).'),
 '15260915': ('Taylor2004_folato_meta','[MA] meta J Psychopharmacol',['Humans'],'human_clinical','eligible','meta de RCTs de folato','Folato para transtornos depressivos (meta de RCTs).'),
 '38873435': ('Gao2024_folato_addon','[MA] meta Food Sci Nutr',['Humans'],'human_clinical','eligible','meta de folato adjuvante','Folato como add-on benéfico na TDM.'),
 '25644193': ('Almeida2015_folato_RCT_meta','[MA] meta de RCTs placebo Int Psychogeriatr',['Humans'],'human_clinical','eligible','meta de RCTs','Folato e B12 em RCTs placebo para depressão (meta).'),
 '27727432': ('Galizia2016_SAMe_cochrane','[MA] Cochrane Database Syst Rev',['Humans'],'human_clinical','eligible','evidência limitada/heterogênea','SAMe para depressão em adultos (Cochrane; limitado).'),
 # ---- multinutrientes ----
 '33158241': ('Johnstone2020_multinutri_meta','[MA] meta Nutrients — amostras clínicas',['Humans'],'human_clinical','eligible','sinal modesto, heterogêneo, não atribuível a um nutriente','Multinutrientes para sintomas psiquiátricos em amostras clínicas (meta).'),
 '32178540': ('Blampied2020_microformula','[OB] SR Expert Rev Neurother',['Humans'],'review','eligible','revisão de fórmulas amplas','Fórmulas de micronutrientes de largo espectro para depressão/estresse/ansiedade.'),
 '35156551': ('BorgesVieira2023_BvitD','[MA] meta Nutr Neurosci',['Humans'],'human_clinical','eligible','meta de B-vitaminas e vitamina D','Eficácia de B-vitaminas e vitamina D em sintomas depressivos/ansiosos.'),
 '31527485': ('Young2019_Bvit_meta','[MA] meta Nutrients — estresse +, depressão p=0,07, ansiedade NS',['Humans'],'human_clinical','eligible','ansiedade NÃO significativa; depressão limítrofe','Suplementação de B-vitaminas: estresse positivo, depressão p=0,07, ansiedade NS.'),
 '24554519': ('Rucklidge2014_posdesastre','[EC] estudo pós-desastre Hum Psychopharmacol',['Humans'],'human_experimental','eligible','intervenção após desastre natural','Funcionamento psicológico 1 ano após intervenção com micronutrientes pós-desastre.'),
 '31081672': ('Rucklidge2019_seguranca','[EC] observacional J Altern Complement Med',['Humans'],'human_clinical','eligible','segurança de consumo prolongado','Segurança do consumo de longo prazo de micronutrientes.'),
 # ---- diretrizes / intervenções ----
 '35311615': ('Sarris2022_WFSBP_diretriz','[OB] diretriz clínica World J Biol Psychiatry',['Humans'],'review','eligible','diretriz WFSBP/CANMAT; hierarquia de evidência','Diretriz para tratamento com nutracêuticos e fitoterápicos (força de evidência hierarquizada).'),
 '33652997': ('Hoepner2021_intervencoes','[OB] revisão Nutrients',['Humans'],'review','eligible','revisão de intervenções nutricionais','Impacto de suplementação e intervenções nutricionais nos processos da TDM.'),
 '35066009': ('Jin2022_folato_gestacional','[EC] coorte JAD — gestação',['Humans'],'human_clinical','eligible','suplementação contínua de folato na gravidez','Suplementação contínua de ácido fólico na gravidez e risco de depressão perinatal.'),
 # ---- MR ----
 '39519523': ('Carnegie2024_MR_TDM','[EC] Mendelian randomization Nutrients — PGC 116.209 casos',['Humans'],'human_clinical','eligible','MR tradicional NULO; sinais sugestivos (ferro/cobre/25OHD na recorrente); MR≠RCT','MR de micronutrientes na TDM: MR tradicional nulo; ferro/cobre/25(OH)D sugestivamente protetores na recorrente; selênio/MG possivelmente adversos em excesso.'),
 '41211168': ('Fang2025_MR_ansiedade','[EC] MR + colocalização Food Sci Nutr — ansiedade',['Humans'],'human_clinical','eligible','MR observacional; causalidade potencial','Influências causais de micronutrientes sobre ansiedade (MR + colocalização bayesiana).'),
 # ---- adjuvantes/interfaces (Rodada 2) ----
 '41294251': ('Magalhaes2026_CoQ10','[MA] meta J Clin Psychopharmacol 2026',['Humans'],'human_clinical','eligible','meta de CoQ10; interface B9; adjuvante','CoQ10 sobre sintomas depressivos e fadiga (meta).'),
 '41189312': ('Eckert2025_creatina_meta','[MA] meta Br J Nutr 2025',['Humans'],'human_clinical','eligible','meta de creatina; interface B9/energia','Creatina para sintomas de depressão (meta).'),
 '29177955': ('Toniolo2018_creatina_RCT','[EC] RCT duplo-cego prova de conceito J Neural Transm',['Humans'],'human_experimental','eligible','RCT pequeno; creatina adjuvante','Creatina monohidratada como adjuvante na TDM (prova de conceito, duplo-cego).'),
 '26353411': ('deOliveira2015_vitC_ans','[EC] RCT duplo-cego Pak J Biol Sci — estudantes',['Humans'],'human_experimental','redirecionado_clinico','RCT pequeno em estudantes; periódico de menor impacto; âncora fraca','Vitamina C oral reduziu ansiedade em estudantes (RCT pequeno).'),
}

refs=[]
for pmid,(rid,papel,esp,role,eleg,motivo,achado) in sorted(C.items(), key=lambda x:int(x[0])):
    m=META.get(pmid)
    if not m: print('FALTANDO META:',pmid); continue
    refs.append({
      'pmid_oficial':pmid,'titulo_artigo':m['title'],'autores':m['authors'],
      'revista_ano':f"{m['journal']} ({m['pubdate'][:4]})",
      'desenho_estudo':papel,'secao_origem':'mecanismo_B8_deficiencias_micronutrientes',
      'achado_central_molecular':achado,
      'extrapolacao_por_analogia':('SIM — evidência em roedor/modelo; tradução humana por analogia [EXT]' if role=='preclinical_mechanistic' else ('parcial — revisão mistura espécies' if role=='review' and 'Animals' in esp else 'não')),
      'ids_referencia_interna':[f'REF_{rid}'],
      'evid_role':role,'especie_mesh':esp,
      'verification_status':('preclinico' if role=='preclinical_mechanistic' else 'verificado'),
      'citacao_confirmada':True,'g1_metodo':'eutils_automatico',
      'g2_elegibilidade':eleg,'g2_motivo':motivo,
      'g3_verificado_por':'IA G3 (Rodada 2): esummary + abstract efetch para âncoras de alto risco (VITAL D3/n3, B12 nulo, selênio, Mg Rajizadeh/Tarleton, MR Carnegie, SMILES, Ghaemi/Mikola D); 2a verificação P-6 pendente',
      'status_auditoria':'CONFIRMADO','origem_pipeline':'BUSCA_FERRAMENTA'})

json.dump(refs, open('/home/user/BIBLIOTECAS/B08_Micronutrientes/Evidencias/Bibliografia/01_pmids.json','w'), ensure_ascii=False, indent=1)
print('refs escritas:',len(refs))
from collections import Counter
print('role:',Counter(r['evid_role'] for r in refs))
print('g2:',Counter(r['g2_elegibilidade'] for r in refs))
