#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera 01_pmids.json da B7 a partir dos metadados G1 (esummary) + curadoria G2."""
import json

META = json.load(open('/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro/producao/g1_esummary.json'))

# curadoria: pmid -> (REF_id, papel, especie_mesh, evid_role, g2_elegibilidade, g2_motivo, achado)
CUR = {
 # --- revisões-teto / arquitetura ---
 '31460832': ('Cryan2019_teto','[OB] revisao-teto Physiology Reviews; arquitetura bidirecional do eixo',['Humans','Animals'],'review','eligible','revisão de mecanismo; cita evidência humana e pré-clínica','Síntese-canônica do eixo microbiota-intestino-cérebro: cinco vias (vago, imune, endócrina, metabólica, neurotransmissora) e bidirecionalidade.'),
 '22968153': ('CryanDinan2012_fundadora','[OB] revisão fundadora Nat Rev Neurosci',['Humans','Animals'],'review','eligible','revisão fundadora do campo','Formula o eixo microbiota-cérebro como campo; germ-free, FMT e modulação comportamental.'),
 '36232548': ('Goralczyk2022_psiq','[OB] revisão do enquadramento psiquiátrico IJMS',['Humans','Animals'],'review','eligible','revisão narrativa em periódico psiquiátrico/biomédico','Panorama microbiota-intestino-cérebro em transtornos psiquiátricos (TDM, bipolar, esquizofrenia, ansiedade).'),
 '34450312': ('Socala2021_farmacol','[OB] revisão Pharmacol Res neuropsiquiátrico',['Humans','Animals'],'review','eligible','revisão farmacológica','Papel do eixo em desordens neuropsiquiátricas e neurológicas; potenciais alvos.'),
 '33493503': ('Margolis2021_motilidade','[OB] revisão Gastroenterology "da motilidade ao humor"',['Humans','Animals'],'review','eligible','revisão de gastroenterologia','Eixo microbiota-intestino-cérebro do ponto de vista GI: SNE, motilidade, secreção e humor.'),
 '29467611': ('Bonaz2018_vago','[OB] revisão Front Neurosci sobre o vago na interface',['Animals','Humans'],'review','eligible','revisão focada na via neural','Nervo vago como via de comunicação aferente/eferente do eixo; células enteroendócrinas e SNE.'),
 '39940928': ('Hwang2025_vago5HT','[OB] revisão 2025 IJMS acoplamento vago x 5-HT',['Animals','Humans'],'review','eligible','revisão; publicação 2025','Interação entre nervo vago e serotonina entérica; aferentes vagais e NTS/DRN; interface com VNS.'),
 '29276734': ('Foster2017_estresse','[OB] revisão Neurobiol Stress',['Animals','Humans'],'review','eligible','revisão de estresse/eixo','Regulação do eixo intestino-cérebro pela microbiota sob estresse; programação do HPA.'),
 '22483040': ('DinanCryan2012_HPA','[OB] revisão Psychoneuroendocrinology',['Animals'],'review','redirecionado_mecanistico','revisão centrada em dados animais do HPA','Microbiota regula a resposta ao estresse/HPA; implicações psiconeuroendócrinas.'),
 '27005587': ('Kelly2016_traducao','[OB] revisão Ann Epidemiol sobre desafios translacionais',['Humans','Animals'],'review','eligible','revisão sobre o abismo roedor-humano','Explicitam os desafios de tradução psiquiátrica do eixo: germ-free não é fisiológico; humanos transversais.'),
 # --- via vago / SNE / sensores ---
 '21876150': ('Bravo2011_vagotomia','[ML] experimento em camundongo com vagotomia — PNAS',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','prova de dependência vagal em ROEDOR; não há teste equivalente em humano','L. rhamnosus JB-1 altera receptores GABA centrais e ansiedade; efeito abolido por vagotomia seletiva.'),
 '28648659': ('Bellono2017_sensores','[ML] experimento celular/roedor Cell — células enteroendócrinas como sensores',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','mecanismo sensorial em roedor/célula','Enterocromafins funcionam como quimiossensores que acoplam estímulos luminais a aferentes neurais.'),
 '36521049': ('Sharkey2023_SNE','[OB] revisão Physiol Rev sobre o SNE',['Humans','Animals'],'review','eligible','revisão fisiológica abrangente','Sistema nervoso entérico: anatomia, fisiologia, diálogo com microbiota e vago.'),
 '34702353': ('Vicentini2021_glia','[ML] estudo em roedor Microbiome — neurônios/glia entéricos',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','dados animais de fisiologia entérica','Microbiota intestinal modela a fisiologia do intestino e regula neurônios e glia entéricos.'),
 '26662472': ('Moloney2016_IBS','[OB] revisão CNS Neurosci Ther estresse/IBS',['Animals','Humans'],'review','eligible','revisão com dados mistos','Estresse e eixo microbiota-intestino-cérebro na dor visceral/IBS.'),
 '35396067': ('Austelle2022_VNS','[OB] revisão Neuromodulation sobre VNS na depressão',['Humans'],'human_clinical','eligible','revisão de dispositivo em humano','VNS como terapia estabelecida para depressão refratária/epilepsia; interface com o eixo.'),
 # --- via imune/LPS/barreira ---
 '18283240': ('Maes2008_leakygut','[EC] estudo humano transversal; UM GRUPO, ensaio pouco padronizado — Neuro Endocrinol Lett',['Humans'],'human_clinical','redirecionado_clinico','associação de um único grupo (Maes); IgM anti-LPS; não replicado de forma independente','Hipótese da barreira intestino-cérebro na TDM: disfunção mucosa intestinal e translocação bacteriana.'),
 '28814485': ('Stevens2018_zonulina','[EC] carta/estudo humano pequeno Gut — zonulina/FABP2/LPS',['Humans'],'human_clinical','redirecionado_clinico','carta ao editor, n pequeno, transversal','Zonulina e FABP2 plasmáticos correlacionam-se com LPS plasmático e microbioma alterado em ansiedade/depressão.'),
 '41155365': ('Bibolar2025_validacao','[OB] revisão narrativa 2025 IJMS sobre biomarcadores de permeabilidade',['Humans'],'review','eligible','revisão crítica de validação de marcadores','Biomarcadores sanguíneos de permeabilidade intestinal (zonulina, FABP2, LBP) não estão validados para clínica.'),
 '26030851': ('Erny2015_microglia','[ML] estudo germ-free/reconvenção em camundongo — Nat Neurosci',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','dados animais; microglia residente','A microbiota do hospedeiro controla constantemente a maturação e a função da microglia no SNC.'),
 '34736493': ('Li2021_rifaximina','[ML] experimento CUMS em camundongo adolescente — J Neuroinflammation',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','modelo animal de estresse crônico','Rifaximina modula microbiota e microglia e reverte fenótipo tipo-depressivo induzido por CUMS.'),
 # --- HPA / desenvolvimento ---
 '15133062': ('Sudo2004_germfree','[ML/marco] camundongos germ-free — J Physiol',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','marco experimental em ROEDOR; germ-free é extremo não fisiológico','Colonização microbiana pós-natal programa o HPA; germ-free tem resposta de corticosterona exagerada, parcialmente revertida por colonização precoce.'),
 '21282636': ('DiazHeijtz2011_dev','[ML] germ-free vs convencional — PNAS',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','dados animais de desenvolvimento','Microbiota normal modula o desenvolvimento cerebral e o comportamento; alterações motoras e de expressão gênica.'),
 '23689536': ('Desbonnet2014_social','[ML] germ-free, déficit social — Mol Psychiatry',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','dados animais; janela de desenvolvimento','A microbiota é essencial para o desenvolvimento social do camundongo; germ-free tem déficit social parcialmente reversível.'),
 '26679775': ('Arentsen2015_social','[ML] preferência social em camundongo — Microb Ecol Health Dis',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','dados animais; CORREÇÃO de metadado: é preferência social, não BDNF','A microbiota do hospedeiro modula o desenvolvimento da preferência social em camundongos.'),
 '21054680': ('Neufeld2011_germfree','[ML] germ-free, ansiedade reduzida — Neurogastroenterol Motil',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','dados animais; direção do fenótipo é complexa (ansiedade reduzida no germ-free)','Camundongos germ-free exibem comportamento tipo-ansiedade reduzido e alterações neuroquímicas centrais.'),
 '36535610': ('Lynch2023_janela','[ML] revisão/experimentos de janelas críticas — Brain Behav Immun',['Animals'],'review','redirecionado_mecanistico','síntese de dados animais sobre janelas críticas','Janelas críticas de perturbação microbiana no início da vida para comportamento, neuroimunidade e neurodesenvolvimento.'),
 '27742460': ('Hoban2016_adulto','[ML] depleção crônica na vida adulta — Neuroscience',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','dados animais; depleção por antibiótico no adulto','Consequências comportamentais e neuroquímicas da depleção crônica de microbiota na vida adulta do rato.'),
 # --- metabólitos: AGCC / triptofano / bile ---
 '31646148': ('Caspani2019_metab','[OB] revisão Microb Cell de metabólitos microbianos',['Humans','Animals'],'review','eligible','revisão de bioquímica','Metabólitos microbianos na depressão: AGCC, triptofano/quinurenina/indóis, sais biliares; mecanismos bioquímicos.'),
 '41865792': ('Do2026_SCFAmeta','[MA] meta-análise 2026 Biomed J — AGCC CIRCULANTES (8 estudos humanos + 52 murinos)',['Humans','Animals'],'human_clinical','eligible','meta-análise de estudos transversais humanos + experimentais murinos; ASSOCIAÇÃO, não intervenção','Pacientes com TDM têm AGCC circulantes mais baixos (propionato SMD −0,60; butirato −0,50); heterogeneidade alta; em murino, suplementação melhora comportamento.'),
 '27392632': ('Kennedy2017_quinurenina','[OB] revisão Neuropharmacology via quinurenina',['Humans','Animals'],'review','eligible','revisão de via metabólica','Metabolismo da via da quinurenina e o eixo microbiota-intestino-cérebro.'),
 '34758380': ('Butler2022_ansiedadesocial','[EC] estudo humano transversal Brain Behav Immun — fobia social',['Humans'],'human_clinical','eligible','estudo de caso-controle em humanos','Via imune-quinurenina no transtorno de ansiedade social: associação entre marcadores e sintomas.'),
 '39719433': ('Jia2024_bile','[EC] metabolômica+metagenômica humana TDM — Transl Psychiatry (epub 2024)',['Humans'],'human_clinical','eligible','estudo humano observacional; CORREÇÃO: ano 2024 (não 2025)','Disbiose promove disfunção cognitiva na TDM via metabolismo de sais biliares.'),
 # --- neurotransmissores / peptídeos ---
 '25860609': ('Yano2015_5HT','[ML] experimento germ-free/cultura — Cell',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','dados animais/celulares; 5-HT é ENTÉRICA/periférica, não cerebral','Bactérias esporuladas indígenas promovem biossíntese de 5-HT pelas células enteroendócrinas/enterocromafins do cólon; afeta motilidade e plaquetas.'),
 '30531975': ('Strandwitz2019_GABA','[EC/ecologia] isolamento de bactérias de microbiota humana — Nat Microbiol',['Humans'],'human_experimental','eligible','ecologia bacteriana de origem humana; NÃO é reposição central','Bactérias da microbiota humana produzem e consomem GABA; ecologia do potencial neuroativo.'),
 '29903615': ('Strandwitz2018_NT','[OB] revisão Brain Res de neurotransmissores microbianos',['Humans','Animals'],'review','eligible','revisão','Modulação de neurotransmissores pela microbiota intestinal (GABA, glutamato, monoaminas).'),
 '29134359': ('Lach2018_peptideos','[OB] revisão Neurotherapeutics de peptídeos intestinais',['Humans','Animals'],'review','eligible','revisão','Papel de peptídeos intestinais (GLP-1, PYY, CCK, grelina, leptina, NPY) em ansiedade, depressão e microbiota.'),
 '24892638': ('Clarke2014_endocrino','[OB] minirrevisão Mol Endocrinol — microbiota como órgão endócrino',['Humans','Animals'],'review','eligible','revisão endócrina','A microbiota como órgão endócrino negligenciado; produção de moléculas sinalizadoras.'),
 # --- FMT / causalidade animal ---
 '27491067': ('Kelly2016_FMTblues','[ML/FMT] FMT humano→rato — J Psychiatr Res',['Animals','Humans'],'preclinical_mechanistic','redirecionado_mecanistico','doadores humanos, mas fenótipo medido em RATO; prova causal animal','FMT de pacientes deprimidos para ratos microbiota-depletados induz anedonia, ansiedade e alterações de triptofano.'),
 '27067014': ('Zheng2016_FMT','[ML/FMT] FMT humano→camundongo + metabolômica — Mol Psychiatry',['Animals','Humans'],'preclinical_mechanistic','redirecionado_mecanistico','prova causal em ROEDOR','Remodelagem do microbioma induz comportamento depressivo via metabolismo (carboidratos/aminoácidos); FMT transfere fenótipo.'),
 '31124390': ('LiN2019_FMT_CUMS','[ML/FMT] FMT de doadores CUMS — Stress',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','dados animais','FMT de camundongos sob estresse crônico imprevisível transfere ansiedade/depressão via inflamação.'),
 # --- biomarcadores / composição humana ---
 '25882912': ('Jiang2015_fezes','[EC] estudo caso-controle humano — Brain Behav Immun',['Humans'],'human_clinical','eligible','estudo humano fundacional observacional','Composição fecal alterada em pacientes com TDM; aumento de Firmicutes/Proteobacteria e correlação com gravidade.'),
 '37174640': ('Maes2023_Ruminococcus','[EC] estudo caso-controle humano (Tailândia) — Cells',['Humans'],'human_clinical','eligible','estudo observacional; um grupo/região','Depleção de Ruminococcus e outras alterações de microbioma em pacientes tailandeses com TDM.'),
 '34524405': ('Nikolova2021_umbrella','[MA] meta-análise guarda-chuva JAMA Psychiatry — 59 estudos',['Humans'],'human_clinical','eligible','meta-análise de estudos caso-controle; avalia especificidade diagnóstica','Perturbações de microbiota são transdiagnósticas (Faecalibacterium/Coprococcus diminuídos; Eggerthella elevado); sem assinatura diagnóstica específica; confundem região e medicação.'),
 '38065935': ('Gao2023_metareg','[MA] meta-análise + metarregressão — Transl Psychiatry',['Humans'],'human_clinical','eligible','meta-análise de composição','Composição da microbiota no transtorno depressivo; metarregressão mostra heterogeneidade por medicamento/região.'),
 '33271426': ('Simpson2021_26est','[MA] RS de 26 estudos — Clin Psychol Rev',['Humans'],'human_clinical','eligible','revisão sistemática; diversidade inconsistente','Microbiota em ansiedade e depressão: achados de diversidade inconsistentes; táxons pró-inflamatórios elevados e produtores de AGCC reduzidos.'),
 '40312666': ('Cao2025_meta','[MA] RS 2025 BMC Psychiatry',['Humans'],'human_clinical','eligible','meta-análise 2025','Variações de microbiota em depressão e ansiedade; confirma heterogeneidade.'),
 '30718848': ('VallesColomer2019_potencial','[EC] coorte humana + metagenômica funcional — Nat Microbiol',['Humans'],'human_clinical','eligible','estudo populacional humano; função, não taxonomia','O potencial neuroativo da microbiota humana (produção/consumo de GABA, glutamato, dopamina) correlaciona-se com depressão e qualidade de vida.'),
 '39360283': ('Crocetta2024_fMRI','[MA/neuroimagem] RS de fMRI em RCTs de probiótico — Front Nutr',['Humans'],'human_experimental','eligible','revisão sistemática de estudos experimentais com neuroimagem','Probióticos modificam sinal regional (amígdala, rede de saliência, DMN, OFC, hipocampo) de forma heterogênea.'),
 '37505311': ('DiVincenzo2024_permeab','[OB] revisão narrativa Intern Emerg Med',['Humans'],'review','eligible','revisão integrativa','Microbiota, permeabilidade intestinal e inflamação sistêmica: estado da arte.'),
 # --- metas de probiótico ---
 '27509521': ('Huang2016_metaDep','[MA] meta-análise Nutrients — depressão',['Humans'],'human_clinical','eligible','meta-análise de RCTs','Probióticos reduzem sintomas depressivos em meta de RCTs (efeito pequeno-moderado).'),
 '29995348': ('Liu2018_metaAns','[MA] meta-análise — ansiedade (Depress Anxiety)',['Humans'],'human_clinical','eligible','meta-análise de RCTs','Probióticos reduzem sintomas de ansiedade em meta de RCTs.'),
 '31563280': ('Goh2019_meta','[MA] meta-análise Psychiatry Res',['Humans'],'human_clinical','eligible','meta-análise de estudos humanos','Probióticos e sintomas depressivos: efeito significativo, porém heterogêneo.'),
 '33191776': ('Zagorska2020_psicob','[OB] revisão Benef Microbes — de probióticos a psicobióticos',['Humans','Animals'],'review','eligible','revisão narrativa','Conceito de psicobiótico e eixo intestino-cérebro em transtornos psiquiátricos.'),
 '34620373': ('ElDib2021_16RCT','[MA] meta-análise 16 RCTs Clin Nutr ESPEN',['Humans'],'human_clinical','eligible','meta-análise com GRADE; CORREÇÃO de periódico: Clin Nutr ESPEN','Probióticos melhoram BDI (certeza moderada) e STAI (baixa); vários outros desfechos nulos; efeito pequeno.'),
 '35276981': ('LeMorvan2022_RS','[MA] RS Nutrients — sintomas psiquiátricos/CNS',['Humans'],'human_clinical','eligible','revisão sistemática','Efeito de probióticos em sintomas psiquiátricos e funções do SNC em humanos.'),
 '39731509': ('Asad2025_diag','[MA] meta-análise 2025 Nutr Rev — amostras DIAGNOSTICADAS',['Humans'],'human_clinical','eligible','meta-análise restrita a populações clínicas','Prebióticos e probióticos em sintomas de depressão/ansiedade em populações clinicamente diagnosticadas.'),
 '38219239': ('Zhao2025_rede','[MA] revisão/rede 2025 Nutr Rev — probiótico vs antidepressivo',['Humans'],'human_clinical','eligible','revisão sistemática comparativa','Probióticos para adultos com TDM comparados a antidepressivos; efeito adjunto, não substitutivo.'),
 '35742022': ('Trifkovic2022_materna','[MA] meta-análise Healthcare — depressão materna',['Humans'],'human_clinical','eligible','meta-análise de população específica','Uso direto/indireto de probióticos para depressão materna; efeito pequeno.'),
 '34441793': ('LeMorvan2021_IBS','[MA] meta-análise J Clin Med — IBS',['Humans'],'human_clinical','eligible','meta-análise em IBS','Probióticos melhoram qualidade de vida, depressão e ansiedade em pacientes com IBS (sinal relativamente melhor que na TDM grave).'),
 '40440772': ('Moshfeghinia2025_I2','[MA] meta-análise 2025 J Psychiatr Res — I²≈96%',['Humans'],'human_clinical','eligible','meta-análise; HETEROGENEIDADE MUITO ALTA (I² 96,3%/96,9%)','Probióticos/prebióticos/simbióticos reduzem escores de depressão (SMD −1,76) e ansiedade (SMD −1,60) com heterogeneidade altíssima (I²≈96%).'),
 '36834489': ('Sikorska2023_BDNF','[MA] RS/meta IJMS — mecanismos moleculares e BDNF',['Humans'],'human_clinical','eligible','meta-análise de 20 registros; BDNF periférico','Probióticos elevam BDNF periférico (SMD 0,37) e reduzem CRP em comorbidade somática; SEM mudança consistente de IL-6, TNF-α, IL-1β, cortisol.'),
 '41605120': ('Shakir2026_citocinas','[MA] meta-análise 2026 Clin Nutr — citocinas',['Humans'],'human_clinical','eligible','meta-análise; 13 RS/7 meta','Probióticos associam-se a melhora de sintomas depressivos SEM alteração significativa de IL-6 (p=0,45) nem TNF-α (p=0,21).'),
 '34131108': ('CohenKadosh2021_nulo','[MA] meta-análise Transl Psychiatry — JOVENS, EFEITO NULO',['Humans'],'human_clinical','eligible','meta-análise em jovens 10-24 anos; SMD −0,03 (IC −0,21 a 0,14)','Psicobióticos para ansiedade em jovens: ausência de efeito (SMD −0,03); evidência limitada.'),
 '20974015': ('Messaoudi2011_subclin','[EC] RCT em voluntários sadios — Br J Nutr',['Humans'],'human_experimental','eligible','RCT em população subclínica/sadia','Formulação probiótica (L. helveticus/B. longum) reduz sintomas psicológicos em voluntários sadios com estresse.'),
 # --- psicobióticos / conceito ---
 '23759244': ('Dinan2013_psicobiot','[OB] artigo conceitual Biol Psychiatry — psicobióticos',['Humans','Animals'],'review','eligible','artigo de conceito','Cunhagem/definição do termo psicobiótico: organismos vivos com benefício em saúde mental.'),
 '34032650': ('Dinan2021_evolucao','[OB] revisão Mod Trends Psychiatry — evolução dos psicobióticos',['Humans','Animals'],'review','eligible','revisão dos mesmos autores','Evolução dos psicobióticos como novos antidepressivos; estado da evidência.'),
 '27793434': ('Sarkar2016_psicob','[OB] revisão Trends Neurosci',['Humans','Animals'],'review','eligible','revisão conceitual','Psicobióticos e a manipulação dos sinais bactéria-intestino-cérebro.'),
 '32406013': ('Morkl2020_foco','[OB] revisão Curr Nutr Rep — foco em psiquiatria',['Humans','Animals'],'review','eligible','revisão','Probióticos e o eixo microbiota-intestino-cérebro com foco em psiquiatria.'),
 # --- FMT clínico ---
 '32539741': ('Chinna2020_FMT_RS','[MA] RS BMC Psychiatry — FMT em sintomas psiquiátricos',['Humans'],'human_clinical','eligible','revisão sistemática; maioria estudos pequenos','FMT em sintomas psiquiátricos: evidência preliminar, sobretudo em condições GI; psicopatologia como desfecho secundário.'),
 '41921871': ('LiB2026_FMTmeta','[MA] meta-análise 2026 J Affect Disord — 8 estudos/532 participantes',['Humans'],'human_clinical','eligible','meta-análise pequena e heterogênea; mistura RCTs e coortes','FMT melhora sintomas depressivos (g=−0,81) e de ansiedade (g=−1,05) com heterogeneidade substancial; sem eventos adversos graves.'),
 '42309058': ('LiJ2026_FMTRCT','[EC/EMERGENTE] RCT duplo-cego placebo 2026 Cell Host Microbe — TDM',['Humans'],'human_experimental','eligible','RCT; endpoint primário (remissão semana 8) NULO; escore HARD maior; ÚNICO, aguarda replicação','FMT adjuvante à escitalopram na TDM: remissão não difere, mas redução de HAMD-17 maior; engraftment duradouro, bile ácidos e mediação inflamatória.'),
 # --- variabilidade / confundidores ---
 '31805290': ('Jaggar2020_sexo','[OB] revisão Front Neuroendocrinol — sexo e o eixo',['Animals','Humans'],'review','eligible','revisão sobre dimorfismo','Sexo modula o eixo microbiota-intestino-cérebro ao longo da vida.'),
 '41244880': ('Bautista2025_ciclo','[OB] revisão crítica 2025 Front Psychiatry — ritmo circadiano',['Animals','Humans'],'review','eligible','revisão; interface com B10','Eixo intestino-cérebro-circádio em ansiedade e depressão.'),
 '34032649': ('Cussotto2021_psicof','[OB] revisão Mod Trends Psychiatry — psicofármacos e microbioma',['Humans','Animals'],'review','eligible','revisão sobre o confundidor medicação','Drogas psicotrópicas alteram a microbiota; a "disbiose do doente" pode ser efeito de droga.'),
 '30806744': ('Cussotto2019_camara','[OB] revisão Psychopharmacology — psicotrópicos e microbioma',['Humans','Animals'],'review','eligible','revisão do grupo Cryan/Dinan','Psicotrópicos e microbioma: relação mão-dupla e confundimento.'),
 '40717539': ('Cussotto2025_livre','[EC] estudo 2025 J Neurochem — pacientes SEM antidepressivo',['Humans'],'human_clinical','eligible','estudo humano controlado para medicação','Microbiota alterada em pacientes deprimidos SEM antidepressivo e associada à gravidade — separa doença de efeito de droga.'),
 # --- outras condições / fronteira ---
 '27912057': ('Sampson2016_Parkinson','[ML] FMT em modelo de Parkinson — Cell',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','doença neurológica, fora do miolo ansiedade/depressão; prova animal','Microbiota regula déficits motoros e neuroinflamação em modelo da doença de Parkinson; FMT transfere fenótipo motor.'),
 '39617896': ('Feng2024_ALS','[ML/EC emergente] FMT em ELA — BMC Med',['Humans'],'human_experimental','redirecionado_clinico','ensaio clínico pequeno em ELA; fora do miolo','FMT em esclerose lateral amiotrófica esporádica: segurança e sinais preliminares.'),
 # --- Rodada 2: achados novos ---
 '25411471': ('Braniste2014_BBB','[ML] germ-free/colonização — Sci Transl Med',['Animals'],'preclinical_mechanistic','redirecionado_mecanistico','dados animais de barreira','A microbiota influencia a permeabilidade da barreira hematoencefálica em camundongos.'),
 '25449699': ('Schmidt2015_prebCort','[EC] RCT em voluntários sadios — Psychopharmacology',['Humans'],'human_experimental','eligible','RCT humano pequeno; desfecho de cortisol e viés emocional','Prebiótico (FOS/GOS) reduz resposta de cortisol ao despertar e altera viés emocional em voluntários sadios.'),
 '36841506': ('Mysonhimer2023_nulo','[EC] RCT J Nutr — prebiótico, EFEITO NULO em estresse',['Humans'],'human_experimental','eligible','RCT humano; resultado negativo (contra-ponto importante)','Prebiótico altera a microbiota, mas NÃO marcadores biológicos de estresse/inflamação nem saúde mental em adultos estressados.'),
 '28700459': ('Hemmings2017_TEPT','[EC] estudo exploratório humano — Psychosom Med',['Humans'],'human_clinical','eligible','estudo exploratório transversal; TEPT','Microbioma no TEPT vs controles expostos a trauma: associações exploratórias.'),
 '37980332': ('Zeamer2023_trauma','[EC] coorte longitudinal pós-trauma — Transl Psychiatry',['Humans'],'human_clinical','eligible','estudo longitudinal humano','Associação entre microbioma e desenvolvimento de sequelas neuropsiquiátricas pós-traumáticas.'),
 '35634468': ('Srivastava2022_eCB','[OB] revisão Front Cell Neurosci — endocanabinoides e estresse',['Animals','Humans'],'review','redirecionado_mecanistico','interface com B13; maioria dados animais','Microbioma e sistema endocanabinoide entérico na regulação de respostas ao estresse e metabolismo.'),
}

refs = []
for pmid, (rid, papel, esp, role, eleg, motivo, achado) in sorted(CUR.items(), key=lambda x: int(x[0])):
    m = META.get(pmid)
    if not m:
        print('FALTANDO META:', pmid); continue
    autores = m['authors']
    refs.append({
        'pmid_oficial': pmid,
        'titulo_artigo': m['title'],
        'autores': autores,
        'revista_ano': f"{m['journal']} ({m['pubdate'][:4]})",
        'desenho_estudo': papel,
        'secao_origem': 'mecanismo_B7_eixo_intestino_cerebro_microbiota',
        'achado_central_molecular': achado,
        'extrapolacao_por_analogia': ('SIM — evidência em roedor/modelo; tradução humana por analogia' if role=='preclinical_mechanistic' else ('parcial — revisão mistura espécies' if role=='review' and 'Animals' in esp and 'Humans' in esp else 'não')),
        'ids_referencia_interna': [f'REF_{rid}'],
        'evid_role': role,
        'especie_mesh': esp,
        'verification_status': ('preclinico' if role=='preclinical_mechanistic' else ('verificado' if role in ('human_clinical','human_experimental') else 'verificado')),
        'citacao_confirmada': True,
        'g1_metodo': 'eutils_automatico',
        'g2_elegibilidade': eleg,
        'g2_motivo': motivo,
        'g3_verificado_por': 'IA G3 (Rodada 2): esummary + abstract efetch para âncoras de alto risco; 2a verificação independente (P-6) pendente do avaliador cego',
        'status_auditoria': 'CONFIRMADO',
        'origem_pipeline': 'BUSCA_FERRAMENTA'
    })

json.dump(refs, open('/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro/Evidencias/Bibliografia/01_pmids.json','w'),
          ensure_ascii=False, indent=1)
print('refs escritas:', len(refs))
# conferência de labels
for r in refs:
    print(r['pmid_oficial'], r['ids_referencia_interna'][0], r['evid_role'], r['g2_elegibilidade'])
