#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# B9 — fusao V1(35) -> V2(111): insere 76 refs [AT 2026-09-09] na canonica (aprovada: completo 76).
# Asserts: cada ancora aparece exatamente 1x; varredura de 7-9 digitos = 0; citacoes novas presentes.
import json, re, shutil, os, sys
sys.path.insert(0, '/home/user')
from b9_refs import D, ROTULO

BASE = '/home/user/BIBLIOTECAS/B09_DisfuncaoMitocondrial'
V1 = f'{BASE}/B9 DISFUNCAO MITOCONDRIAL V1 CANONICA.md'
V2 = f'{BASE}/B9 DISFUNCAO MITOCONDRIAL V2 CANONICA.md'

doc = open(V1, encoding='utf-8').read()
trechos_ancora = {}
OPS = []
def rep(anc, new, key=None): OPS.append(('replace', anc, new, key))
def app(anc, ins, key=None): OPS.append(('after', anc, ins, key))

def rot(*rids, sep=' | '):
    return sep.join(ROTULO[r] for r in rids)

# ---------- 1) título / cabeçalho ----------
rep('# B9 DISFUNÇÃO MITOCONDRIAL V1 CANÔNICA',
    '# B9 DISFUNÇÃO MITOCONDRIAL V2 CANÔNICA', 'titulo')
rep('**ID canônico:** mecanismo_B9_disfuncao_mitocondrial · **Prompt v4.2** · Corte: 2026-09-06.',
    '**ID canônico:** mecanismo_B9_disfuncao_mitocondrial · **Prompt v4.2** · Corte: 2026-09-09.', 'corte_id')
rep('**artefato_rotulo:** CANÔNICA v1 · G1 (28 PMIDs eutils, tema validado contra o GPM) + G2 (espécie/desenho) + G3 (suporte; abstracts de alto risco lidos).',
    '**artefato_rotulo:** CANÔNICA v2 (rodada [AT] GPM 2026-09-09 — reconciliação de insumo externo, P-7; 35→111 refs: 76 ENTRA — 43 masters do GPM oficial + Lu 2024 resgatado + 32 extras auditados —; 69 BAIXO; 6 EXC pela malha de escopo: autismo, síndrome de fadiga crônica, diabetes, metanfetamina e demência ×2; 0 falso positivo; 4 não-indexados confirmados; 7 fragilidades do briefing externo revertidas e expostas) · G1 (111/111 PMIDs eutils) + G2 (espécie/desenho/elegibilidade) + G3 (suporte por vínculo; abstracts lidos ref a ref nesta rodada).', 'rotulo')

# ---------- 2) BLOCO_00 — nova tese 7 (MR nulo × arquitetura compartilhada) ----------
app('6. **Sem biomarcador validado para diagnóstico** — respirometria, mtDNAcn, cf-mtDNA e ³¹P-MRS são\n   de pesquisa/associação; sangue ≠ cérebro.',
    '\n7. **Associação do mtDNA ≠ causalidade genética ([[AT 2026-09-09]], regra fundadora 3)** — a\n   randomização mendeliana bidirecional não sustentou efeito causal do mtDNA-CN sobre TDM,\n   ansiedade, bipolar, esquizofrenia ou TOC (nem vias reversas) (Lu 2024)[EC]; a arquitetura\n   genética compartilhada entre mtDNA-CN e transtornos psiquiátricos existe (Xue 2026)[EC] —\n   qualificador interpretativo, não refutação do defeito funcional documentado.', 'REF_LU_2024')

# ---------- 3) §1.1 — células humanas alinham o defeito funcional ----------
app('(revisado em Khan\n2023)[OB].',
    '\n\n[[AT 2026-09-09]] A evidência em células humanas derivadas de pacientes alinhou-se ao mesmo\ndefeito funcional: fibroblastos dérmicos de adultos com TDM exibem função mitocondrial\nprejudicada — respiração basal e máxima reduzidas e alterações do\nsistema OXPHOS (Kuffner 2020)[EC]; em fibroblastos de bipolar em fase inicial há alterações de\nbiogênese/dinâmica e de\npotencial de membrana, com depleção de ATP na cadeia transportadora e estimulação compensatória\nda glicólise — o distúrbio aparece como evento precoce (Marques 2021)[EC]; e em progenitores\nneurais induzidos e neurônios iPS de pacientes com TDM, as diferenças funcionais dos fibroblastos\npersistem parcialmente após a reprogramação, com alteração da função neuronal associada\n(Triebelhorn 2024)[EC]. Em adultos jovens com TDM, a bioenergética de ATP medida no cérebro e no\nsangue revela uma assinatura associada à fadiga — com menor capacidade de produção de ATP em\nPBMC sob desacoplamento, lida como mecanismo compensatório em estágio inicial (Cullen 2026)[EC].\nEm modelo murino com função prejudicada do complexo I, a reatividade ao estresse e o metabolismo\ncerebral são reprogramados — motor candidato do substrato tipo-depressivo, não mero epifenômeno\n(Emmerzaal 2020)[ML]. Revisões integradoras enquadraram a disfunção mitocondrial como peça-chave\nda manifestação depressiva (Allen 2018)[OB]; os déficits do sistema OXPHOS descritos na\nesquizofrenia entram apenas como fronteira ilustrativa — patologia distinta sobre a mesma\norganela, sem seta causal para o humor (Bergman 2016)[OB].', 'REF_KUFFNER_2020')

# ---------- 4) §1.2 — mecânica da dinâmica + evidência humana periférica ----------
app('OPA1 é proposto como "hub" comum (Papageorgiou 2024)[OB].',
    '\n\n[[AT 2026-09-09]] A mecânica molecular da fissão/fusão ganhou âncoras dedicadas: a função e a\nregulação da fissão dependente de DRP1 foram revistas em detalhe (Otera 2013)[OB];\n(Feng 2020)[OB]; as estruturas de MFN1 revelaram a dimerização dependente de nucleotídeo crítica para\na fusão (Cao 2017)[OB]; a estrutura, função e regulação de MFN2 foram consolidadas em revisão de\nreferência (Chandhok 2018)[OB]; e a dinâmica mitocondrial na saúde e na doença — com o\nequilíbrio MFN2–OPA1 como guarda da homeostase — foi revista duas vezes nesta rodada\n(Yapa 2021)[OB]; (Zanfardino 2025)[OB], com a advertência explícita de que o binário "fissão ruim /\nfusão boa" é falso: mutantes de MFN2 causadores de doença prejudicam a fissão por mecanismos\ndistintos de desregulação de DRP1 (Lagos 2026)[ML]. No sangue periférico de pacientes com TDM,\na via apoptótica e a dinâmica da rede mitocondrial estão perturbadas (Scaini 2017)[EC]; e, em\nroedor com síndrome tipo-depressiva, a acetilação elevada de MFN2 acompanha a disrupção do\nmetabolismo energético mitocondrial e da inflamação (Xie 2025)[ML]. Condições neurológicas\nentram só como fronteira ilustrativa de mecânica (CAMADA B/C — regra fundadora 4): a dinâmica\nperturbada nas doenças neurodegenerativas (Burté 2015)[OB]; o parkinsonismo sindrômico\ne a demência associados a mutações de OPA1 (Carelli 2015)[EC]; e a desregulação de OPA-1/DRP-1\nna apoptose induzida por manganês em astrócitos de rato (Alaimo 2014)[ML] demonstram a\ncentralidade da maquinaria sem autorizar nenhuma extrapolação ao humor.', 'REF_SCAINI_2017')

# ---------- 5) §1.5 — ROS é sinal; desregulação é o claim ----------
app('(a química fina é B6).',
    '\n\n[[AT 2026-09-09]] O status do ROS mitocondrial foi qualificado por revisões dedicadas — e o\nresultado é exatamente a regra fundadora 1 desta biblioteca: o ROS é, antes de tudo, **sinal\nfisiológico**, e a questão real é quando a produção deixa de ser função e vira disfunção (Palma\n2024)[OB]; o manejo mitocondrial das espécies reativas — fontes, alvos e defesas — está\nsistematizado (Napolitano 2021)[OB]; no cérebro, o mtROS participa da fisiologia antes de\nparticipar da neurodegeneração (Angelova 2018)[OB]; (Stefanatos 2018)[OB] — esta última no\ncérebro em envelhecimento, CAMADA C contextual. O estresse oxidativo mitocondrial como fator\ncausativo e alvo terapêutico (Kowalczyk 2021)[OB], a interação estresse oxidativo × falha\nbioenergética nas condições neuropsiquiátricas (Morris 2020)[OB] e o tripé mitocôndria–\nmetabolismo–redox nos transtornos psiquiátricos (Kim 2019)[OB] foram revistos. O eixo\nferroptose–mitocôndria na depressão — loop feedforward entre lipoperoxidação e disfunção da\norganela — é leitura recente e permanece emergente (Liu 2025)[OB]. O claim desta biblioteca\npermanece **desregulação da sinalização redox**, nunca "ROS ruim".', 'REF_PALMA_2024')

# ---------- 6) §1.6 — mecânica do controle de qualidade + UPRmt emergente ----------
app('sinapse. Interface com B15 (autofagia/mTOR).',
    '\n\n[[AT 2026-09-09]] A mecânica do controle de qualidade tem âncoras clássicas: a via PINK1/Parkin\nregula a morfologia mitocondrial (Poole 2008)[ML]; a perda de função de parkin ou PINK1 aumenta\na fragmentação dependente de DRP1 (Lutz 2009)[ML]; e, em neurônios de mamífero, a mesma via\nregula dinâmica e função (Yu 2011)[ML]. O elo direto com o estresse crônico aparece em modelo:\no estresse crônico leve disrompe a mitofagia e o status mitocondrial no córtex frontal de rato\n(Ulecia-Morón 2025)[ML]. E uma análise cross-espécies (separação materna em camundongo +\ntranscriptoma humano público de hipocampo) revelou assinatura compartilhada de **resposta de\nestresse mitocondrial**, com OXPHOS e dobramento proteico (UPRmt/ISR) como mecanismos centrais\n(Hofstra 2024)[ML] — sinal emergente: ainda não há âncora humana dedicada de UPRmt em\npsiquiatria `[G1]`.', 'REF_HOFSTRA_2024')

# ---------- 7) §1.7 — mito-inflamação em camadas ----------
app('(Casaril 2021)[OB]. Parceria principal com B1.',
    '\n\n[[AT 2026-09-09]] A ponte mitocôndria–inflamação foi revisada em camadas: o estresse oxidativo\nmitocondrial e a "mito-inflamação" como atores da doença (Patergnani 2021)[OB]; a resposta\ninflamatório-mitocondrial na depressão maior, com a evidência corrente (Visentin 2020)[OB]; e o\ntripé mitocôndria–micróglia–sistema imune nos transtornos afetivos (Culmsee 2018)[OB]. Do lado\nda dinâmica, a desregulação de DRP1 emerge como nó que alimenta a neuroinflamação — a interação\nfissão × imunidade foi revista nas doenças neurológicas, com leitura mecanística para os\nafetivos (Cai 2024)[OB].', 'REF_PATERGNANI_2021')

# ---------- 8) §1.8 — cadeia causal animal + ansiedade social ----------
app('ver B2). Carga alostática mitocondrial.',
    '\n\n[[AT 2026-09-09]] A cadeia causal em modelo ficou encadeada elo a elo (regra fundadora 6): o\nestresse crônico promove fissão mitocondrial no córtex pré-frontal medial via ativação de DRP1,\nimpondo ônus metabólico neuronal que aumenta a suscetibilidade ao estresse — e inibir DRP1\natenua o fenótipo (Dong 2023)[ML]; o corticosterona crônico induz comportamento tipo-depressivo\nacompanhado de disrupção do metabolismo energético mitocondrial em roedor (Xie 2020)[ML]. Os\nmodelos de **ansiedade social** completam a âncora (regra fundadora 9): a função mitocondrial no\nnúcleo accumbens liga a ansiedade-traço à subordinação social em ratos (Hollis 2015)[ML]; o\nisolamento social induz disfunção da succinato-desidrogenase em camundongos ansiosos (Watanabe\n2022)[ML]; e a diversidade e a organização de rede das mitocôndrias em escala cerebral ampla\npredizem o comportamento tipo-ansioso (Rosenberg 2023)[ML]. Leitura protegida: são evidências de\nroedor com [EXTRAPOLAÇÃO POR ANALOGIA] — âncoras do mecanismo, não demonstração humana.',
    'REF_DONG_2023')

# ---------- 9) §1.9 — MAO→respiração (ponte B4) ----------
app('ver B3); serotonina upstream da biogênese (Fanibunda 2019)[ML].',
    '\n\n[[AT 2026-09-09]] O acoplamento MAO→bioenergética foi medido diretamente: em mitocôndrias\nisoladas do córtex de camundongo, a inibição seletiva de MAO-A (não MAO-B) aumenta o consumo de\noxigênio acoplado ao complexo I — evidência de que a enzima monoaminérgica da membrana\nmitocondrial externa modula a respiração local (Kalimon 2023)[ML]. Ponte molecular adicional\ncom B4.', 'REF_KALIMON_2023')

# ---------- 10) §1.10 — transplante nomeado + sinais de fronteira + guarda-chuvas ----------
rep('Transplante mitocondrial melhora ansiedade/depressão em rato idoso\nestressado (2022, animal — hipótese inicial);',
    'Transplante mitocondrial melhora ansiedade/depressão em rato idoso\nestressado (Javani 2022)[ML] — animal; hipótese inicial;', 'REF_JAVANI_2022')
app('(Verbal 2026)[OB] — conceitual/emergente.',
    '\n\n[[AT 2026-09-09]] Os demais sinais de fronteira permanecem **sinais, não terapia** (regra\nfundadora 7): a administração intranasal de mitocôndrias aliviou fenótipos depressivos/ansiosos\ne marcadores inflamatório-oxidativos em camundongos sob estresse de contenção (Mafikandi\n2025)[ML]; e o astragalosídeo IV conferiu eficácia profilática em modelo de depressão via eixo\nredox–energia (ROS–Nrf2/Keap1) (Tian 2026)[ML] — ambos pré-clínicos, nenhum com lastro humano.\nO campo-guarda-chuva foi revisto em camadas: o papel das mitocôndrias nos transtornos de humor,\nda fisiologia à patofisiologia (Giménez-Palomo 2021)[OB]; a disfunção do metabolismo energético\nmitocondrial na depressão (Jiang 2024)[OB]; e os processos mitocondriais disfuncionais como\ncontribuintes das perturbações energéticas cerebrais e dos sintomas\nneuropsiquiátricos (Büttiker 2022)[OB]. Dois qualificadores fecham o mapa: o metabolismo energético cerebral em **modelos\nanimais** de depressão merece leitura própria — mini-revisão dedicada (Kolár 2021)[OB]; e a\nmedicação é confundidora de primeira ordem — os estabilizadores de humor exercem efeitos próprios\nsobre a função mitocondrial (Ľupták 2019)[OB]. Por fim, a bioenergética mitocondrial foi\nproposta como novo caminho na resposta à ECT e como biomarcador candidato em TDM, origem do\nconceito "Mito-Mood" — hipótese estruturante `[G1]`, não fato (Karabatsiakis 2020)[OB].',
    'REF_MAFIKANDI_2025')

# ---------- 11) BLOCO_02 — §2.5 mtDNA sob quatro lentes ----------
app('É o autoalimentamento B9↔B1.',
    '\n\n### 2.5 [[AT 2026-09-09]] O genoma mitocondrial sob quatro lentes (regra fundadora 2)\n\nSão proibidos os genéricos do tipo "MDD aumenta mtDNA": o mtDNA tem **quatro fenômenos\ndistintos** — copy number, dano/oxidação, mutações/heteroplasmia e fração extracelular\n(ccf-mtDNA) —, cada um com direção e leitura próprias.\n\n**(A) Copy number.** Elevado em sangue periférico em várias coortes de TDM (Chung 2019)[EC];\n(Wang 2017)[EC]; (Ryan 2023)[EC] — valendo também para depressão/ansiedade de atenção primária,\ncom associação à gravidade basal e à resposta após oito semanas de tratamento (Wang 2017)[EC] —;\nem adolescentes, associa-se a sintomas ansiosos e à menor conectividade estrutural\nfronto-ocipital (Tymofiyeva 2018)[EC]. Mas as exceções são qualificantes: já houve coorte com CN\nleucocitário **menor** na TDM estável — com dano oxidativo maior, na mesma amostra (Chang\n2015)[EC]; o estresse precoce sem sintomatologia psiquiátrica não o eleva (Beck 2025)[EC]; e no\nestudo que mediu as duas frações, o CN leucocitário **não diferiu** entre TDM e controles — só a\nfração extracelular subiu (Lindqvist 2018)[EC]. O CN é em parte de controle genético nuclear —\nloci em TFAM e CDK6 (Cai 2015)[EC]; arquitetura nuclear que molda\ncopy number e heteroplasmia (Gupta 2023)[EC] — e permanece sem direção única (Calarco 2024)[EC].\n\n**(B) Dano e metilação.** O dano oxidativo do mtDNA aparece maior na TDM mesmo com CN menor\n(Chang 2015)[EC]; PBMCs de deprimidos reparam e degradam pior o mtDNA após insulto oxidativo ex\nvivo (Czarny 2020)[EC]; variantes nos genes que mantêm a estabilidade do mtDNA associam-se à\ndepressão e ao desfecho do tratamento (Czarny 2023)[EC]; e a metilação do D-loop diferencia TDM\nde bipolar e de controles — caindo na remissão (Ceylan 2023)[EC].\n\n**(C) Mutações e heteroplasmia.** Heteroplasmia aumentada em mulheres com TDM, com paradigma\nexperimental indicando o estresse como causa provável (Cai 2015)[EC]; heteroplasmia num sítio do\ncomplexo I (m.13514G>A) associada a sintomas depressivos em homens idosos (Tranah 2018)[EC];\nvariantes de sequência do mtDNA em tecido cerebral pós-morte através de esquizofrenia, bipolar e\nTDM (Rollins 2009)[EC]; mutações somáticas cerebrais mais frequentes em casos selecionados\n(Sequeira 2015)[EC]; e sequenciamento completo do mtDNA na TDM apontando mutações funcionais\nespecíficas e um haplótipo protetor candidato (Yin 2026)[EC]. Variantes do mtDNA também se\nassociam a depressão/ansiedade em pacientes com lúpus — comorbidade de doença sistêmica,\nfronteira contextual (Zong 2026)[EC]. Do lado negativo: grandes séries de cérebro envelhecido\n**não** sustentam papel maior das variantes puntiformes nas neurodegenerações — embora os níveis\nde mtDNA mereçam investigação (Wei 2017)[EC]; (Klein 2021)[EC]; fronteira CAMADA C, sem leitura\ndo humor.\n\n**(D) ccf-mtDNA (fração extracelular).** Elevado na TDM **sem** alteração do CN leucocitário no\nmesmo estudo (Lindqvist 2018)[EC]; a revisão sistemática confirma sinal mais consistente nos\ntranstornos depressivos (sobretudo sem medicação e na depressão tardia), heterogeneidade no\nbipolar e nulidade predominante na esquizofrenia — com advertência de heterogeneidade\nmetodológica, amostras pequenas e desenho transversal (Fernández-Pech 2026)[OB].\n\n**Genética, interações e causalidade.** No UK Biobank, SNPs do mtDNA e interações mtDNA×PCR\nsignificativas para ansiedade e depressão foram documentadas em dezenas de milhares de\nparticipantes (Liu 2023)[EC] — ponte direta com B1. A arquitetura genética compartilhada entre\nmtDNA-CN e condições psiquiátricas foi mapeada nas maiores GWAS disponíveis — sobreposição\nglobal, loci compartilhados e vias de ubiquitina/desenvolvimento (Xue 2026)[EC]. **Contra a\ncausalidade direta** (regra fundadora 3): a randomização mendeliana bidirecional **não\nsustentou** efeito causal do mtDNA-CN sobre TDM, ansiedade, bipolar, esquizofrenia ou TOC — nem\nefeito reverso —, sustentando associação causal potencial apenas para TEA, que permanece fora do\nescopo desta biblioteca (Lu 2024)[EC]. As revisões de método do próprio campo — o que a análise\ndo mtDNA pode dizer sobre os transtornos de humor (Kasahara 2018)[OB] e o sumário abrangente\ndas alterações do mtDNA em cérebro humano pós-morte (Valiente-Pallejà 2022)[OB] — fecham o\nmapa: a genética informa risco e arquitetura; não refuta nem substitui o defeito funcional\ndocumentado nas células.', 'REF_LINDQVIST_2018')

# ---------- 12) BLOCO_03 — mediadores + inventário negativo ----------
app('- **Neuroimagem:** ³¹P-MRS (ATP/fosfocreatina), ¹H-MRS (creatina) (Bansal 2016)[OB].',
    '\n- **[[AT]] mtDNA (quatro lentes — regra 2):** CN sob controle TFAM/CDK6 (Cai 2015)[EC]; dano e\n  metilação do D-loop (Chang 2015)[EC]; (Ceylan 2023)[EC]; heteroplasmia (Tranah 2018)[EC];\n  ccf-mtDNA (Lindqvist 2018)[EC]; (Fernández-Pech 2026)[OB].',
    'REF_TRANAH_2018')
app('- **Haplogrupos/POLG** sem associação robusta no humor (achado negativo, GPM); **GDF-15** é\n  emergente (parte em preprint).',
    '\n- **[[AT 2026-09-09]]:** (i) o MR bidirecional é **nulo** para mtDNA-CN→TDM/ansiedade/bipolar/\n  esquizofrenia/TOC e reversos (Lu 2024)[EC] — arquitetura compartilhada (Xue 2026)[EC] não é\n  causalidade; (ii) "ROS elevado = dano" é leitura proibida — ROS é sinal fisiológico até deixar\n  de ser (Palma 2024)[OB]; (iii) "fissão ruim / fusão boa" é binário falso — mutantes e revisões\n  mostram doença nos dois sentidos do equilíbrio (Lagos 2026)[ML]; (Zanfardino 2025)[OB]; (iv)\n  UPRmt/biogênese ainda não têm âncora humana dedicada em psiquiatria — o sinal cross-espécies é\n  emergente (Hofstra 2024)[ML] `[G1]`.', 'REF_LAGOS_2026')

# ---------- 13) BLOCO_05 — itens 2 e 3 ----------
app('2. **mtDNA copy number:** direção mista, confundido por idade/IMC/inflamação/medicação (Calarco\n   2024)[EC].',
    ' Série clínica compatível com a mistura: CN elevado na TDM (Chung 2019)[EC];\n   (Wang 2017)[EC]; (Ryan 2023)[EC], e menor numa coorte de pacientes estáveis (Chang 2015)[EC].',
    'REF_CHUNG_2019')
app('3. **cf-mtDNA/ccf-mtDNA:** marcador de **estado**, varia minuto-a-minuto, inespecífico (Trumpff\n   2021)[EC].',
    ' Elevado na fração **plasmática** da TDM — sem mudança no CN leucocitário do mesmo estudo\n   (Lindqvist 2018)[EC]; a SR de ccf-mtDNA em psiquiatria confirma sinal mais consistente em\n   transtornos depressivos, advertindo heterogeneidade e transversalidade (Fernández-Pech\n   2026)[OB].', 'REF_FERNANDEZPECH_2026')

# ---------- 13b) BLOCO_05 (DETALHE) — marcadores um a um ----------
app('- **mtDNA copy number:** direção mista, sem assinatura única (Calarco 2024)[EC].',
    ' Estudos direcionais da leva [AT]: acima do controle\n  (Chung 2019)[EC]; (Wang 2017)[EC]; (Ryan 2023)[EC]; abaixo (Chang 2015)[EC]; leucócitos sem\n  diferença com ccf-mtDNA elevado (Lindqvist 2018)[EC].', 'REF_WANG_2017')
app('- **cf-mtDNA/ccf-mtDNA:** marcador de estado/lesão inespecífico, varia em minutos (Trumpff\n  2021)[EC].',
    ' Na TDM, a fração plasmática se eleva sem mudança leucocitária (Lindqvist 2018)[EC];\n  SR: sinal mais consistente em transtornos depressivos que em bipolar/esquizofrenia\n  (Fernández-Pech 2026)[OB].', 'REF_CEYLAN_2023_B05')

# ---------- 14) BLOCO_07 — item 7 (genética ≠ causalidade) ----------
app('6. **Regra anti-prescrição:** mecanismo robusto ≠ alvo medicamentoso; causalidade forte é [ML].',
    '\n7. **[[AT 2026-09-09]] Genética: associação ≠ causalidade (regra fundadora 3)** — a\n   arquitetura compartilhada mtDNA-CN × transtornos psiquiátricos foi mapeada (Xue 2026)[EC];\n   mas o MR bidirecional é **nulo** para os desfechos-âncora desta biblioteca (Lu 2024)[EC] —\n   qualificador interpretativo, não refutação do defeito; a tensão resolve-se por camadas (regra\n   fundadora 4).', 'REF_XUE_2026')

# ---------- 15) BLOCO_08 — itens 1, 6 e 10 ----------
app('empurram glicólise (Alcocer-Gómez 2014)[EC]; (Ciubuc-Batcu 2024)[OB]; (Casaril 2021)[OB].',
    ' Interações mtDNA×PCR\n   para ansiedade/depressão foram documentadas no UK Biobank (Liu 2023)[EC]; e a\n   fissão/DRP1 atua como nó da neuroinflamação (Cai 2024)[OB].', 'REF_LIU_2023')
app('5-HT→5-HT2A→biogênese (Fanibunda 2019)[ML].',
    ' Inibição seletiva de MAO-A aumenta a\n   respiração em mitocôndria cortical isolada (Kalimon 2023)[ML].', 'REF_B08_KAL')
app('10. **B9↔B10 (ritmo/sono) — MEDIUM/emergente:** Mito-Mood/ritmo (Verbal 2026)[OB].',
    ' O conceito "Mito-Mood" permanece\n   hipótese estruturante `[G1]`, não fato (regra fundadora 11).', 'REF_B08_MITOMOOD')

# ---------- 16) BLOCO_11 — item 6 (fenótipos operacionais) ----------
app('5. **Sexo:** fissão neuronal documentada em machos — não generalizar entre sexos (GPM, emergente).',
    '\n6. **[[AT 2026-09-09]] Fenótipos B9 (operacionais, não diagnósticos):** bioenergético\n   periférico (reserva ↓ — Karabatsiakis 2014)[EC]; multi-tecido (PBMC + fibroblasto +\n   iPSC-neurônio — Kuffner 2020)[EC]; (Triebelhorn 2024)[EC]; **ccf-mtDNA alto** (Lindqvist\n   2018)[EC]; (Fernández-Pech 2026)[OB]; **fenótipo de dano do mtDNA** (Ceylan 2023)[EC];\n   **suscetibilidade ao estresse** (fissão no mPFC — Dong 2023)[ML]; **social/ansioso** (Hollis\n   2015)[ML]; (Rosenberg 2023)[ML]; e **bipolar como fronteira**, com sobreposição parcial\n   (Marques 2021)[EC]; (Chang 2015)[EC].', 'REF_TYMOFIYEVA_2018_B11')

# ---------- 17) BLOCO_12 — três cenários novos ----------
app('  estudo-ponte, sinalizados `[EXTRAPOLADO]`; não são o miolo ansiedade/depressão.',
    '\n- **"ROS alto = mitocôndria doente?"** não — ROS é sinal fisiológico; o defeito é a\n  **desregulação da sinalização redox**, não o ROS em si (Palma 2024)[OB]; (Napolitano 2021)[OB]\n  (regra fundadora 1).\n- **"Parkinson/OPA1 comprovam o eixo na depressão?"** não — são CAMADA B/C: mecânica\n  compartilhada da organela, sem seta causal para o humor (Burté 2015)[OB]; (Carelli 2015)[EC]\n  (regra fundadora 4).\n- **"Transplante ou mitocôndria intranasal é tratamento?"** não — é sinal experimental em animal:\n  Javani 2022 já vigente acima; a via intranasal foi replicada como sinal (Mafikandi 2025)[ML]\n  (regra fundadora 7).', 'REF_NAPOLITANO_2021_B12')

# ---------- 18) TABELA DE EVIDÊNCIAS — linhas novas ----------
app('| Intervenção humana | Sem evidência causal robusta de terapia mitocondrial para humor | baixo/emergente |',
    '\n| Células derivadas de pacientes | Fibroblastos TDM/bipolar e iNPC/iPS-neurônios com bioenergética prejudicada (Kuffner; Marques; Triebelhorn); assinatura ATP×fadiga em jovens (Cullen) | médio-alto (humano, multi-tecido) |\n| mtDNA — quatro fenômenos | CN: ↑ (Chung; Wang; Ryan; Tymofiyeva; Beck) vs ↓ (Chang) vs leucócitos = (Lindqvist); dano/D-loop (Czarny; Ceylan); heteroplasmia/mutações (Cai; Tranah; Sequeira; Rollins; Yin); ccf-mtDNA ↑ (Lindqvist; SR Fernández-Pech) | médio (heterogêneo — regra 2) |\n| Causalidade genética | MR bidirecional NULO para mtDNA-CN × TDM/ansiedade/bipolar/esq/TOC e reversos (Lu); arquitetura compartilhada existe (Xue) | médio-alto (qualificador, não refutação) |\n| Cadeia causal animal do estresse | Estresse → DRP1 → fissão no mPFC → comportamento; inibir DRP1 atenua (Dong); ansiedade social NAc/rede (Hollis; Rosenberg; Watanabe) | alto em modelo; [ML]/[EXT] em humano |\n| UPRmt/ISR | Sinal cross-espécies no hipocampo (ELS em camundongo + transcriptoma humano) (Hofstra) | emergente; `[G1]` em psiquiatria |\n| Terapias experimentais | Transplante, via intranasal, fitoterápico (Javani; Mafikandi; Tian) | sinal pré-clínico apenas |',
    'REF_TABELA')

# ---------- 19) CONTROVÉRSIAS — regras fundadoras + inventário negativo + fragilidades ----------
app('  sinalizadas `[ML]/[EMERGENTE]/P-6`, nunca como recomendação.',
    '\n- **REGRAS FUNDADORAS B9 FIXADAS (rodada [AT] 2026-09-09 — insumo externo auditado, P-7):** as\n  doze regras do GPM oficial foram incorporadas ao contrato desta biblioteca:\n  (01) B9 ≠ "ROS elevado" — ROS é sinal/hormese/adaptação; o claim é "desregulação da\n  sinalização redox", nunca "ROS ruim" (Palma 2024)[OB];\n  (02) o mtDNA tem quatro fenômenos distintos — copy number, dano/oxidação,\n  mutações/heteroplasmia, ccf-mtDNA — proibido o genérico "MDD aumenta mtDNA" (Lindqvist\n  2018)[EC];\n  (03) associação ≠ causalidade genética — MR bidirecional nulo para os desfechos-âncora (Lu\n  2024)[EC]; a arquitetura compartilhada existe (Xue 2026)[EC] — qualificador, não refutação;\n  (04) camadas A–E: canônica psiquiátrica (A), mecanística (B) e contextual (Parkinson/Alzheimer/\n  diabetes/envelhecimento; C) não se cruzam — proibida a seta "Parkinson → comprova depressão"\n  (Burté 2015)[OB]; (Carelli 2015)[EC];\n  (05) humanos multi-compartimento — PBMC (Karabatsiakis 2014)[EC], fibroblasto (Kuffner\n  2020)[EC], iPSC-neurônio (Triebelhorn 2024)[EC] — e PBMC ≠ neurônio;\n  (06) causalidade experimental é âncora — estresse crônico → DRP1 → fissão no mPFC →\n  comportamento; inibir DRP1 atenua (Dong 2023)[ML] — [EXTRAPOLAÇÃO POR ANALOGIA];\n  (07) terapias só como sinal — transplante (Javani 2022)[ML], intranasal (Mafikandi 2025)[ML],\n  fitoterápico (Tian 2026)[ML] — nunca recomendação;\n  (08) B9 não rouba território — mito↔inflamação fica aqui; inflamação→neurônio é B1; ROS\n  citosólico/GSH é B6;\n  (09) modelos de ansiedade social são âncora legítima (Hollis 2015)[ML]; (Watanabe 2022)[ML];\n  (Rosenberg 2023)[ML] — com [EXTRAPOLAÇÃO];\n  (10) anos canônicos = ano de impressão (Scaini 2021 tem impressão 2022 — ID vigente mantido;\n  Ulecia-Morón 2025; Triebelhorn 2024);\n  (11) "Mito-Mood" é hipótese estruturante `[G1]`, não fato (Karabatsiakis 2020)[OB];\n  (12) multi-tag permitida — uma mesma referência pode ancorar mais de um bloco.\n- **INVENTÁRIO NEGATIVO B9 (GPM, auditado):** (i) "MDD aumenta mtDNA" — proibido; especificar o\n  fenômeno (regra 2); (ii) "mtDNA-CN causa MDD" — o MR não sustenta (regra 3); (iii) "ROS\n  mitocondrial é patológico por definição" — falso (regra 1); (iv) "DRP1 ruim / fusão boa" —\n  binário falso (Lagos 2026)[ML]; (Zanfardino 2025)[OB]; (v) "Parkinson/OPA1 comprovam o eixo na\n  depressão" — CAMADA C; (vi) "PBMC = neurônio" — a bioenergética periférica não mede cérebro;\n  (vii) "transplante / mitocôndria nasal = tratamento" — sinal experimental apenas; (viii)\n  "Mito-Mood comprovada" — `[G1]`; (ix) "bipolar = mesma disfunção que TDM" — fenótipos\n  parcialmente sobrepostos, entidades distintas (Marques 2021)[EC]; (Chang 2015)[EC]; (x)\n  "UPRmt/biogênese resolvidos em psiquiatria" — sem âncora `[G1]`.\n- **Fragilidades do briefing externo expostas (P-7):** "Lu 2024 MR não resolvido" — resolvido\n  nesta rodada (J Affect Disord; MR bidirecional, já citado acima); "Triebelhorn 2024 não\n  localizado" — é o mesmo registro que o próprio briefing citaria como pendente (Mol Psychiatry,\n  impressão 2024; o GPM o trata como "2021"); "Mańczak 2010" — o estudo real é Reddy 2011\n  (Mańczak é coautora; coberto na auditoria); "Li 2018" — o estudo real é Wang 2018 em bipolar\n  (ficou BAIXO na matriz); o Scaini vigente tem impressão 2022 (ID REF_SCAINI_2021 mantido);\n  anos de impressão corrigidos (Burté 2015; Chandhok 2018; Culmsee 2018; Feng 2020; Lagos 2026;\n  Mafikandi 2025; Palma 2024); o anexo real tinha 165 entradas, não 152; quatro itens\n  não-indexados foram confirmados e ficaram fora (Heyat 2024; Nunes 2025; Niu 2024 em preprint;\n  Giménez-Palomo 2023) — nenhuma fonte forjada.', 'REF_CONTROVERSIAS')

# ---------- 20) MARCADORES RESUMIDOS ----------
app('baixo (marcadores de estado e intervenção\nhumana).',
    ' Rodada [AT] 2026-09-09: +76 refs (76 ENTRA / 69 BAIXO / 6 EXC);\n12 regras fundadoras B9 fixadas (ver CONTROVÉRSIAS); mtDNA lido sob quatro lentes\n(CN/dano/mutações/ccf-mtDNA — Chung; Wang; Chang; Czarny; Ceylan; Tranah; Sequeira; Rollins;\nYin; Lindqvist; Cai; Gupta); MR bidirecional nulo (Lu 2024) × arquitetura compartilhada (Xue\n2026); ccf-mtDNA elevado na TDM com SR de heterogeneidade (Lindqvist 2018; Fernández-Pech 2026);\ninteração mtDNA×PCR no UK Biobank (Liu 2023); UPRmt/ISR emergente (Hofstra 2024); causalidade\nanimal DRP1-mPFC (Dong 2023) e ansiedade social (Hollis; Watanabe; Rosenberg); terapias\nexperimentais só como sinal (Javani; Mafikandi; Tian); fronteiras ilustrativas sinalizadas\n(Parkinson/OPA1 — Burté, Carelli; manganês — Alaimo; esquizofrenia — Bergman; lúpus — Zong);\nTEA permanece fora do escopo.', 'REF_MARCADORES')

# ---------- 21) METADADOS (corte + hint) ----------
rep('**corte_literatura (R06):** busca ativa E-utilities/PubMed — corte 2026-09-06.',
    '**corte_literatura (R06):** busca ativa E-utilities/PubMed — corte 2026-09-09 (rodada [AT] GPM, P-7).', 'corte_lit')
rep('mtDNA-DAMP/cf-mtDNA, ³¹P-MRS, ou para contrapor defeito bioquímico (robusto) a terapia humana (modesta).',
    'mtDNA-DAMP/cf-mtDNA, ³¹P-MRS, os quatro fenômenos do mtDNA (CN/dano/mutações/ccf — regra 2), o MR\nnulo do mtDNA (regra 3), UPRmt/ISR cross-espécies, ou para contrapor defeito bioquímico (robusto) a\nterapia humana (modesta).', 'rag_hint')

# ---------- 22) fecho ----------
old_fecho = '''> **Canônica v1 (Consolidação, Rodada 3).** Portões: G1 (eutils, 28 âncoras com tema validado
> contra o GPM), G2 (espécie/desenho), G3 (suporte; abstracts de alto risco lidos). Prosa em
> (Autor, ano)[tag], sem número de PMID no texto. Causalidade animal é [ML]/[EXT]; intervenção
> humana é emergente e não gera prescrição (P20). 2ª verificação independente (P-6, avaliador
> cego) é pendência do avaliador externo.'''
new_fecho = '''> **Canônica v2 (Rodada [AT] 2026-09-09 — reconciliação de insumo externo, P-7).** 35→111
> referências (76 ENTRA — 43 masters do GPM oficial, Lu 2024 resgatado do "não resolvido" do
> briefing e 32 extras auditados; 69 BAIXO; 6 EXC pela malha de escopo: autismo, síndrome de
> fadiga crônica, diabetes, metanfetamina e demência ×2). Sete fragilidades do briefing externo
> foram revertidas e expostas ("Lu 2024 não resolvido" — resolvido; "Triebelhorn 2024 não
> localizado" — mesmo registro, impressão 2024; "Mańczak 2010" — Reddy 2011 real; "Li 2018" —
> Wang 2018 real; impressão do Scaini vigente é 2022 — ID mantido; anos de impressão corrigidos;
> anexo com 165 entradas reais, não 152). Portões: G1 (eutils, 161/161 auditados nesta rodada; 0
> falso positivo; 4 não-indexados confirmados — Heyat 2024, Nunes 2025, Niu 2024 preprint,
> Giménez-Palomo 2023 — nenhum forjado), G2 (espécie/desenho/elegibilidade), G3 (suporte por
> vínculo; abstracts lidos ref a ref). Prosa em (Autor, ano)[tag], sem número de PMID/DOI no
> texto. As 12 regras fundadoras B9 e o inventário negativo ×10 estão fixados em CONTROVÉRSIAS:
> mtDNA sob quatro lentes; MR de Lu 2024 nulo para os desfechos-âncora (arquitetura compartilhada
> de Xue 2026 ≠ causalidade); "Mito-Mood" hipótese `[G1]`; UPRmt/ISR emergente (Hofstra 2024);
> transplante/intranasal/fitoterápico só sinal pré-clínico (Javani 2022; Mafikandi 2025; Tian
> 2026); fronteiras ilustrativas sem seta causal (Parkinson/OPA1, manganês, esquizofrenia,
> lúpus); TEA permanece fora do escopo. Causalidade animal permanece [ML]/[EXT] (Dong 2023;
> Gebara 2020; Hollis 2015; Rosenberg 2023; Watanabe 2022; Xie 2020). 2ª verificação
> independente (P-6, avaliador cego) permanece pendência do avaliador externo.'''
rep(old_fecho, new_fecho, 'fecho')

# ---------- 23) listras-resumo ----------
ALL76 = [d[0] for d in D]
B01_IDS = [d[0] for d in D if d[4] == 'BLOCO01']
B02_IDS = [d[0] for d in D if d[4] == 'BLOCO02']
rep(' | Turck2025_proteomica[ML]*',
    ' | Turck2025_proteomica[ML] | ' + rot(*ALL76) + '*', 'listra00')
rep('| Picard2018_estresse[OB] | Verbal2026_mitomood[OB]*',
    '| Picard2018_estresse[OB] | Verbal2026_mitomood[OB] | ' + rot(*B01_IDS) + '*', 'listra01')
rep('| Ciubuc-Batcu2024_nexus[OB] | Casaril2021_bioenergetica[OB]*',
    '| Ciubuc-Batcu2024_nexus[OB] | Casaril2021_bioenergetica[OB] | Scaini2017_rede_mitocondrial[EC] | ' + rot(*B02_IDS) + '*', 'listra02')
rep('| Ben-Shachar2008_complexoI[EC] | Andreazza2010_ETC[EC]*',
    '| Ben-Shachar2008_complexoI[EC] | Andreazza2010_ETC[EC] | ' + rot('REF_CAI_2015','REF_CHANG_2015','REF_CEYLAN_2023','REF_TRANAH_2018','REF_LINDQVIST_2018','REF_FERNANDEZPECH_2026','REF_LU_2024','REF_XUE_2026','REF_PALMA_2024','REF_LAGOS_2026','REF_ZANFARDINO_2025','REF_HOFSTRA_2024') + '*', 'listra03')
rep('| Torrell2013_mtDNAcerebro[EC] | Bansal2016_revisao[OB] | Picard2018_estresse[OB]*',
    '| Torrell2013_mtDNAcerebro[EC] | Bansal2016_revisao[OB] | Picard2018_estresse[OB] | ' + rot('REF_LINDQVIST_2018','REF_FERNANDEZPECH_2026','REF_CHUNG_2019','REF_WANG_2017','REF_RYAN_2023','REF_CHANG_2015','REF_CEYLAN_2023') + '*', 'listra05')
rep('| Ciubuc-Batcu2024_nexus[OB] | Casaril2021_bioenergetica[OB] | Picard2018_estresse[OB]*',
    '| Ciubuc-Batcu2024_nexus[OB] | Casaril2021_bioenergetica[OB] | Picard2018_estresse[OB] | ' + rot('REF_XUE_2026','REF_LU_2024') + '*', 'listra07')
rep('| Trumpff2021_cfmtDNA[EC]*',
    '| Trumpff2021_cfmtDNA[EC] | ' + rot('REF_LIU_2023','REF_CAI_2024','REF_KALIMON_2023') + '*', 'listra08')
rep('| Filiou2019_ansiedade[OB] | Ryan2019_PGC1a[EC]*',
    '| Filiou2019_ansiedade[OB] | Ryan2019_PGC1a[EC] | ' + rot('REF_KUFFNER_2020','REF_TRIEBELHORN_2024','REF_LINDQVIST_2018','REF_FERNANDEZPECH_2026','REF_CEYLAN_2023','REF_DONG_2023','REF_HOLLIS_2015','REF_ROSENBERG_2023','REF_MARQUES_2021','REF_CHANG_2015') + '*', 'listra11')
rep('*Karabatsiakis2014_PBMC[EC] | Calarco2024_mtDNAcn[EC] | Picard2018_estresse[OB]*',
    '*Karabatsiakis2014_PBMC[EC] | Calarco2024_mtDNAcn[EC] | Picard2018_estresse[OB] | ' + rot('REF_PALMA_2024','REF_NAPOLITANO_2021','REF_BURTE_2015','REF_CARELLI_2015','REF_MAFIKANDI_2025') + '*', 'listra12')

# ---------- 24) APÊNDICE DE CORPUS ----------
APX = ' | '.join(f"{d[0].replace('REF_','')}[{d[3]}]" for d in D)
rep('*PAPAGEORGIOU_2024[OB] | FILIPOVIC_2025[ML] | VERBAL_2026[OB] | BODENSTEIN_2019[MA] | CLAY_2011[OB] | GIMENEZPALOMO_2024[MA] | KUANG_2018[MA] | KATO_2000[MA] | MISIEWICZ_2019[ML] | EINAT_2005[ML]*',
    '*PAPAGEORGIOU_2024[OB] | FILIPOVIC_2025[ML] | VERBAL_2026[OB] | BODENSTEIN_2019[MA] | CLAY_2011[OB] | GIMENEZPALOMO_2024[MA] | KUANG_2018[MA] | KATO_2000[MA] | MISIEWICZ_2019[ML] | EINAT_2005[ML]*\n*' + APX + '*\n> Leva [AT 2026-09-09]: 76 refs ENTRA (auditadas ref a ref; 69 BAIXO; 6 EXC malha de escopo; 4 não-indexados confirmados fora).', 'apendice')

# ================= aplica =================
erros = []
for modo, anc, new, key in OPS:
    c = doc.count(anc)
    if c != 1:
        erros.append((key, anc[:90], c))
if erros:
    for e in erros: print('FALHA ANCORA', e)
    raise SystemExit(2)

for modo, anc, new, key in OPS:
    doc = doc.replace(anc, new, 1) if modo == 'replace' else doc.replace(anc, anc + new, 1)
    if key:
        trechos_ancora[key] = new if len(new) < 1500 else new[:1500]

# citações novas presentes (e contagem mínima)
falt = []
for d in D:
    cit = f'({d[2]})[{d[3]}]'
    if cit not in doc:
        falt.append(cit)
assert not falt, falt

# varredura: 7-9 dígitos (PMID no texto)
hits = re.findall(r'(?<![\w./])\d{7,9}(?![\w.])', doc)
assert not hits, ('PMID/DIGITOS NO TEXTO', hits[:10])

nAT = doc.count('[[AT 2026-09-09]]')
assert nAT == 13, nAT
for tag in ('[[AT]]',):
    pass

# rotação V1 -> histórico
os.makedirs(f'{BASE}/producao/historico', exist_ok=True)
shutil.copy2(V1, f'{BASE}/producao/historico/v1_canonica_2026-09-09.md')
open(V2, 'w', encoding='utf-8').write(doc)
os.remove(V1)

json.dump(trechos_ancora, open(f'{BASE}/producao/insumos/b9_trechos_ancora.json', 'w'), ensure_ascii=False, indent=1)

print('OK — V2 gravada:', len(doc), 'chars; ~', len(doc.split()), 'palavras')
print('rótulos AT:', nAT)
