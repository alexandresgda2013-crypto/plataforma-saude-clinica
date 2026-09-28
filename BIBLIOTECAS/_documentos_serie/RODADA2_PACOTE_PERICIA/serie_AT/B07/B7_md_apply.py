#!/usr/bin/env python3
# B7 — aplica rodada [AT] GPM 2026-09-09 na canônica V1 -> V2 (31 refs ENTRA)
import re, sys

BASE='/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro'
SRC=f'{BASE}/B7 EIXO INTESTINO CEREBRO V1 CANONICA.md'
DST=f'{BASE}/B7 EIXO INTESTINO CEREBRO V2 CANONICA.md'
doc=open(SRC,encoding='utf-8').read()
trechos={}  # rid -> trecho_ancora literal (para json_apply)

def rep(anc, new, label, n=1):
    global doc
    c=doc.count(anc)
    assert c==n, f'âncora "{label}" encontrada {c}x (esperado {n})'
    doc=doc.replace(anc,new,1)

# ---------- 1) cabeçalho ----------
rep('# B7 EIXO INTESTINO–CÉREBRO / MICROBIOTA V1 CANÔNICA',
    '# B7 EIXO INTESTINO–CÉREBRO / MICROBIOTA V2 CANÔNICA','titulo')
rep('**ID canônico:** mecanismo_B7_eixo_intestino_cerebro_microbiota · **Prompt v4.2** · Corte: 2026-09-05.\n**artefato_rotulo:** CANÔNICA v1 · G1 (85/85 PMIDs eutils) + G2 (espécie/desenho/elegibilidade) + G3 (suporte por vínculo; abstracts de alto risco lidos: metas 2026, FMT-RCT, Bravo/Kelly/Yano).',
    '**ID canônico:** mecanismo_B7_eixo_intestino_cerebro_microbiota · **Prompt v4.2** · Corte: 2026-09-09.\n**artefato_rotulo:** CANÔNICA v2 · G1 (116/116 PMIDs eutils) + G2 (espécie/desenho/elegibilidade) + G3 (suporte por vínculo; abstracts de alto risco lidos) · rodada [AT] GPM B7 2026-09-09: +31 referências auditadas ref a ref sobre a V1 (0 falsos positivos; 4 não-indexados mantidos fora).','cab2')

# ---------- 2) §1.1 arquitetura: Aburto & Cryan 2024 + Carabotti 2015 ----------
trecho='A interface entre **barreiras gastrointestinal e cerebral**\ncomo portas de comunicação ganhou revisão dedicada (Aburto & Cryan 2024)[OB], e a sistematização\ntripartite microbiota entérica–SNC–SNE foi fixada por (Carabotti 2015)[OB].'
rep('(Socała 2021)[OB]; (Góralczyk-Bińkowska 2022)[OB].',
    '(Socała 2021)[OB]; (Góralczyk-Bińkowska 2022)[OB]. '+trecho,'s1.1')
trechos['REF_ABURTOCRYAN_2024']='como portas de comunicação ganhou revisão dedicada (Aburto & Cryan 2024)[OB]'
trechos['REF_CARABOTTI_2015']='sistematização\ntripartite microbiota entérica–SNC–SNE foi fixada por (Carabotti 2015)[OB]'

# ---------- 3) listra BLOCO_01 ----------
rep('Jia2024_bile[EC] | Yano2015_5HT[ML] | Strandwitz2019_GABA[EC]*',
    'Jia2024_bile[EC] | Yano2015_5HT[ML] | Strandwitz2019_GABA[EC] | AburtoCryan2024_barreiras[OB] | Carabotti2015_SNC_SNE[OB]*','listra1')

# ---------- 4) §2.2 parágrafo LPS→TJ mecânica ----------
p22=('[...] via imune [[AT 2026-09-09]] a mecânica molecular foi dissecada em série: LPS induz expressão/\n'
'localização de **TLR4-CD14** na membrana do enterócito e aumenta a permeabilidade paracelular in vitro e\n'
'in vivo (Guo 2013)[ML]; a sinalização desce por TLR4→FAK/MyD88 (Guo 2015)[ML] e pela ativação de\n'
'MyD88 com aumento da quinase da cadeia leve de miosina — **MLCK** (Nighot 2017)[ML], mediada a montante por\n'
'**TAK-1→IKK→gene MYLK** (Nighot 2019)[ML]: cadeia LPS→TLR4→MyD88→MLCK→abertura de tight junction. No plano\n'
'cerebral, endotoxemia metabólica crônica promove neuroinflamação em roedor (modelo em contexto isquêmico — a\n'
'lição transportável é a endotoxemia; isquemia/AVC não é escopo desta biblioteca) (Kurita 2020)[ML]. Leitura\n'
'**humana** do braço de translocação: pacientes com disfunção de barreira intestinal exibem níveis sistêmicos\n'
'aumentados de **vesículas extracelulares bacterianas LPS-positivas** (Tulkens 2020)[EC] — evidência\n'
'**ASSOCIATIVA** (REGRA B7-CAUSAL-03), e não prova de que o cérebro seja atingido. Freio de precisão molecular:\n'
'a proteína de junção **ZO-1 é dispensável para a função de barreira** (mas crítica para o reparo mucoso),\n'
'avisando contra leituras ingênuas de ZO-1 como "marcador de permeabilidade" (Kuo 2021)[ML]. **[APENAS\n'
'PRÉ-CLÍNICO]** a cadeia LPS→TJ→MLCK é roedor/célula; o elo endotoxemia→humor humano segue extrapolado [EXT].')
rep('estresse crônico em roedor adolescente (Li 2021)[ML].',
    'estresse crônico em roedor adolescente (Li 2021)[ML].\n\n'+p22,'s2.2')
trechos['REF_GUO_2013']='TLR4-CD14** na membrana do enterócito e aumenta a permeabilidade paracelular in vitro e\nin vivo (Guo 2013)[ML]'
trechos['REF_GUO_2015']='a sinalização desce por TLR4→FAK/MyD88 (Guo 2015)[ML]'
trechos['REF_NIGHOT_2017']='**MLCK** (Nighot 2017)[ML]'
trechos['REF_NIGHOT_2019']='**TAK-1→IKK→gene MYLK** (Nighot 2019)[ML]'
trechos['REF_KURITA_2020']='lição transportável é a endotoxemia; isquemia/AVC não é escopo desta biblioteca) (Kurita 2020)[ML]'
trechos['REF_TULKENS_2020']='aumentados de **vesículas extracelulares bacterianas LPS-positivas** (Tulkens 2020)[EC]'
trechos['REF_KUO_2021']='ZO-1 é dispensável para a função de barreira** (mas crítica para o reparo mucoso),\n\'avisando\'?[0:0]'

# ---------- 5) §2.4 parágrafo AGCC mecanístico ----------
p24=('[...] via metabólica AGCC [[AT 2026-09-09]] o andar mecanístico foi fixado com formulações específicas:\n'
'em roedor, o **acetato** derivado de microbiota sustenta a aptidão metabólica e a maturação da **microglia**\n'
'(Erny 2021)[ML] — lê-se "acetato→fitness/maturação microglial", não "AGCC é anti-inflamatório"; AGCC\n'
'microbianos remodelam a expressão gênica de **astrócitos** de modo sexo-dependente (Spichak 2021)[ML];\n'
'fibra alimentar e AGCC inibem a microglia inflamatória (Caetano-Silva 2023)[ML]; e a **quimiogenética**\n'
'definiu um eixo receptor-de-AGCC intestino→cérebro (Barki 2022)[ML]. A síntese dedicada conecta AGCC\n'
'derivados de microbiota à depressão, com mecanismos e aplicações potenciais (Cheng 2024)[OB]. Uma cadeia\n'
'circuital completa foi demonstrada **em roedor**: AGCC cerebral → indução neuronal de **ACSS2** → **PPARγ** →\n'
'**TPH2** → serotonina → comportamento tipo-depressivo, abolida por knockdown neuronal de ACSS2\n'
'(Chen 2024)[ML] — **[APENAS PRÉ-CLÍNICO]**; é vedado transcrever a cadeia para a clínica humana. No andar da\n'
'barreira: antibióticos orais perturbam a BBB e AGCC restauram a integridade, em **macaco rhesus e camundongo**\n'
'(Chenghan 2025)[ML]. No andar do sensor: os receptores **FFAR3/GPR41 e FFAR2/GPR43** mapeiam-se em\n'
'subconjuntos de células enteroendócrinas (GLP-1, PYY, CCK, GIP, secretina) e em neurônios entéricos\n'
'(Nøhr 2013)[ML]. In vitro, AGCC protegem neurônios SH-SY5Y do estresse oxidativo via GPR43\n'
'(Saikachain 2023)[ML] — prova mecanística celular, não clínica.')
rep('É **assinatura\nassociativa**, não RCT de butirato com desfecho de humor; AGCC fecal ≠ luminal ≠ sistêmico.',
    'É **assinatura\nassociativa**, não RCT de butirato com desfecho de humor; AGCC fecal ≠ luminal ≠ sistêmico.\n\n'+p24,'s2.4')
trechos['REF_ERNY_2021']='o **acetato** derivado de microbiota sustenta a aptidão metabólica e a maturação da **microglia**\n(Erny 2021)[ML]'
trechos['REF_SPICHAK_2021']='expressão gênica de **astrócitos** de modo sexo-dependente (Spichak 2021)[ML]'
trechos['REF_CAETANOSILVA_2023']='fibra alimentar e AGCC inibem a microglia inflamatória (Caetano-Silva 2023)[ML]'
trechos['REF_BARKI_2022']='a **quimiogenética**\ndefiniu um eixo receptor-de-AGCC intestino→cérebro (Barki 2022)[ML]'
trechos['REF_CHENG_2024']='conecta AGCC\nderivados de microbiota à depressão, com mecanismos e aplicações potenciais (Cheng 2024)[OB]'
trechos['REF_CHEN_2024']='**TPH2** → serotonina → comportamento tipo-depressivo, abolida por knockdown neuronal de ACSS2\n(Chen 2024)[ML]'
trechos['REF_CHENGHAN_2025']='perturbam a BBB e AGCC restauram a integridade, em **macaco rhesus e camundongo**\n(Chenghan 2025)[ML]'
trechos['REF_NOHR_2013']='em neurônios entéricos\n(Nøhr 2013)[ML]'
trechos['REF_SAIKACHAIN_2023']='AGCC protegem neurônios SH-SY5Y do estresse oxidativo via GPR43\n(Saikachain 2023)[ML]'

# ---------- 6) §2.5 parágrafo Trp/KYN ----------
p25=('[...] via metabólica triptofano/quinurenina [[AT 2026-09-09]] a arquitetura do substrato ganhou revisões\n'
'próprias: a microbiota regula o metabolismo do triptofano em saúde e doença (Agus 2018)[OB]; os metabólitos\n'
'do triptofano operam como sistema de comunicação **inter-reinos** (Bosi 2020)[OB]; e a ponte\n'
'triptofano→quinurenina foi traçada explicitamente para a depressão na doença inflamatória intestinal\n'
'(Chen 2021)[OB]. Guardas da REGRA B7-CAUSAL-02: *L. reuteri* sintetiza preferencialmente **ácido quinurênico\n'
'(KYNA)** a partir de quinurenina **in vitro** (Schwarcz 2024)[ML] — produção bacteriana em placa ≠ produção\n'
'cerebral; e o **indol-3-propionato (IPrA)**, metabólito investigado isoladamente, eleva KYNA no cérebro de\n'
'rato — claim permitido: **metabólito→cérebro**, não microbiota→cérebro (Sathyasaikumar 2024)[ML]. Em modelo\n'
'inflamatório intestinal, a colite DSS ativa a via da quinurenina no soro **e no cérebro** via IDO-1, em\n'
'dependência da microbiota (Zhao 2022)[ML]; e ratos com fenótipo depressivo por estresse crônico de contenção\n'
'exibem perfil Trp-KYN alterado simultaneamente no intestino e no cérebro (Li 2023)[ML]. **[APENAS\n'
'PRÉ-CLÍNICO]** as duas últimas setas são roedor; a leitura humana desta via é associativa (ver BLOCO_05).')
rep('bactérias modulam o substrato, não "produzem neurotoxina".',
    'bactérias modulam o substrato, não "produzem neurotoxina".\n\n'+p25,'s2.5')
trechos['REF_AGUS_2018']='a microbiota regula o metabolismo do triptofano em saúde e doença (Agus 2018)[OB]'
trechos['REF_BOSI_2020']='do triptofano operam como sistema de comunicação **inter-reinos** (Bosi 2020)[OB]'
trechos['REF_CHEN_2021']='triptofano→quinurenina foi traçada explicitamente para a depressão na doença inflamatória intestinal\n(Chen 2021)[OB]'
trechos['REF_SCHWARCZ_2024']='(KYNA)** a partir de quinurenina **in vitro** (Schwarcz 2024)[ML]'
trechos['REF_SATHYASAIKUMAR_2024']='não microbiota→cérebro (Sathyasaikumar 2024)[ML]'
trechos['REF_ZHAO_2022']='dependência da microbiota (Zhao 2022)[ML]'
trechos['REF_LI_2023']='Trp-KYN alterado simultaneamente no intestino e no cérebro (Li 2023)[ML]'

# ---------- 7) §2.6 Stanimirov ----------
rep('(Jia 2024)[EC]. É também o ramo',
    '(Jia 2024)[EC]. A sinalização por sais biliares foi revista como eixo próprio: modificação microbiana do\npool biliar → FXR/TGR5, com ação direta no SNC e indireta por mediadores endócrinos e imunes\n(Stanimirov 2025)[OB]. É também o ramo','s2.6')
trechos['REF_STANIMIROV_2025']='pool biliar → FXR/TGR5, com ação direta no SNC e indireta por mediadores endócrinos e imunes\n(Stanimirov 2025)[OB]'

# ---------- 8) §2.7 Baj glutamato ----------
rep('Peptídeos intestinais (GLP-1, PYY, CCK, grelina, leptina, NPY) fazem a',
    'O **glutamato** também transita no eixo — revisão dedicada mapeia a sinalização glutamatérgica\nmicrobiota–intestino–cérebro, elo direto com a B5 (Baj 2019)[OB]. Peptídeos intestinais (GLP-1, PYY, CCK, grelina, leptina, NPY) fazem a','s2.7')
trechos['REF_BAJ_2019']='revisão dedicada mapeia a sinalização glutamatérgica\nmicrobiota–intestino–cérebro, elo direto com a B5 (Baj 2019)[OB]'

# ---------- 9) listra BLOCO_02 ----------
nova02=' | '.join(['Guo2013_LPS_TLR4CD14_TJ[ML]','Guo2015_TLR4_FAK_MyD88[ML]','Nighot2017_TLR4_MLCK[ML]','Nighot2019_TAK1_IKK_MLCK[ML]','Kurita2020_endotoxemia_neuroinfl[ML]','Tulkens2020_EVs_LPS_humano[EC]','Kuo2021_ZO1_reparo[ML]','Erny2021_acetato_microglia[ML]','Spichak2021_astrocitos_SCFA[ML]','CaetanoSilva2023_fibra_microglia[ML]','Barki2022_quimiogenetico_SCFAr[ML]','Cheng2024_SCFA_depressao[OB]','Chen2024_ACSS2_PPARg_TPH2[ML]','Chenghan2025_BBB_SCFA_rhesus[ML]','Nohr2013_FFAR_EEC[ML]','Saikachain2023_GPR43_SHSY5Y[ML]','Agus2018_Trp_microbiota[OB]','Bosi2020_Trp_interreinos[OB]','Chen2021_TrpKYN_DII[OB]','Schwarcz2024_KYNA_Lreuteri[ML]','Sathyasaikumar2024_IPrA_KYNA[ML]','Zhao2022_DSS_IDO1_KYN[ML]','Li2023_TrpKYN_CRS[ML]','Stanimirov2025_bile_FXR_TGR5[OB]','Baj2019_glutamato_eixo[OB]'])
rep('Lach2018_peptideos[OB] | Braniste2014_BBB[ML]*',
    'Lach2018_peptideos[OB] | Braniste2014_BBB[ML] | '+nova02+'*','listra2')

# ---------- 10) §4.1 Ohara neuroepitélio ----------
rep('- **Células enteroendócrinas:** enterocromafins (5-HT; Yano 2015)[ML], células L (GLP-1/PYY),\n  células tuft (quimiossensoriais) — liberam sinal em sentido basal para aferentes vagais\n  (Bellono 2017)[ML]; (Hwang 2025)[OB].',
    '- **Células enteroendócrinas:** enterocromafins (5-HT; Yano 2015)[ML], células L (GLP-1/PYY),\n  células tuft (quimiossensoriais) — liberam sinal em sentido basal para aferentes vagais\n  (Bellono 2017)[ML]; (Hwang 2025)[OB]. A arquitetura dessa conversa epitelial foi sintetizada como\n  **sinalização neuroepitelial** — neuropods e células EEC como transdutores do lúmen ao nervo\n  (Ohara 2025)[OB].','s4.1')
trechos['REF_OHARA_2025']='**sinalização neuroepitelial** — neuropods e células EEC como transdutores do lúmen ao nervo\n  (Ohara 2025)[OB]'

# ---------- 11) listra BLOCO_04 ----------
rep('Erny2015_microglia[ML] | Li2021_rifaximina[ML] | Braniste2014_BBB[ML]*',
    'Erny2015_microglia[ML] | Li2021_rifaximina[ML] | Braniste2014_BBB[ML] | Ohara2025_neuroepitelio[OB]*','listra4')

# ---------- 12) §5.2 biomarcadores funcionais humanos ----------
rep('o princípio "espécie ≠ função"\nempurra o campo da taxonomia para o metaboloma/multi-ômica (Caspani 2019)[OB].',
    'o princípio "espécie ≠ função"\nempurra o campo da taxonomia para o metaboloma/multi-ômica (Caspani 2019)[OB]. [[AT 2026-09-09]] Leituras\nhumanas diretas desse andar: disbiose com atividade da **via da quinurenina** como biomarcadores potenciais\nna TDM (Lin 2023)[EC]; metabolômica do triptofano integrando microbiota e neurotransmissores em\n**adolescentes com depressão**, com validação mecanística em camundongo (Zhou 2023)[EC]; e análise\nmulti-ômica ligando microbiota, imunidade e via Trp-KYN ao **desempenho cognitivo** na TDM\n(Zhang Q 2025)[EC] — todas **ASSOCIATIVAS** (REGRA B7-CAUSAL-03), marcadores de pesquisa, não diagnóstico.','s5.2')
trechos['REF_LIN_2023']='disbiose com atividade da **via da quinurenina** como biomarcadores potenciais\nna TDM (Lin 2023)[EC]'
trechos['REF_ZHOU_2023']='**adolescentes com depressão**, com validação mecanística em camundongo (Zhou 2023)[EC]'
trechos['REF_ZHANG_2025']='via Trp-KYN ao **desempenho cognitivo** na TDM\n(Zhang Q 2025)[EC]'

# ---------- 13) listra BLOCO_05 ----------
rep('Crocetta2024_fMRI[MA] | Sikorska2023_BDNF[MA] | Shakir2026_citocinas[MA] | Cussotto2021_psicof[OB]*',
    'Crocetta2024_fMRI[MA] | Sikorska2023_BDNF[MA] | Shakir2026_citocinas[MA] | Cussotto2021_psicof[OB] | Lin2023_KYN_biomarc_TDM[EC] | Zhou2023_Trp_adolescente[EC] | Zhang2025_multiomica_cognicao[EC]*','listra5')

# ---------- 14) TABELA DE EVIDÊNCIAS: 3 linhas ----------
trev=('| Revisão mecanística (rodada GPM B7, 2026-09) | Barreiras GI↔cérebro (Aburto & Cryan); arquitetura SNC/SNE (Carabotti); triptofano microbiano (Agus; Bosi; Chen 2021); AGCC↔depressão (Cheng); neuroepitélio (Ohara); sais biliares (Stanimirov); glutamato no eixo (Baj) | médio (arquitetura, não prova primária) |\n'
'| Experimento animal/celular mecanístico (rodada GPM B7) | LPS→TLR4→MyD88→MLCK→TJ (Guo 2013/2015; Nighot 2017/2019); endotoxemia→neuroinflamação (Kurita); acetato→microglia (Erny); AGCC→astrócitos (Spichak); fibra→microglia (Caetano-Silva); quimiogenética receptor-AGCC (Barki); ACSS2→PPARγ→TPH2 (Chen 2024); antibiótico/BBB+AGCC (Chenghan); Trp-KYN em estresse crônico (Li 2023); DSS→IDO-1→KYN (Zhao 2022); GPR43 em SH-SY5Y (Saikachain); IPrA→KYNA (Sathyasaikumar); KYNA bacteriana in vitro (Schwarcz); ZO-1 dispensável/reparo (Kuo); FFAR3/FFAR2 em EEC (Nøhr) | alto em roedor/célula; [APENAS PRÉ-CLÍNICO] |\n'
'| Estudo humano (rodada GPM B7) | EVs bacterianas LPS+ sistêmicas × barreira intestinal (Tulkens); disbiose+via KYN como biomarcadores na TDM (Lin); metabolômica do triptofano em adolescentes com depressão (Zhou); multiômica Trp-KYN × cognição na TDM (Zhang Q) | baixo — ASSOCIATIVO (B7-CAUSAL-03) |')
rep('| Neuroimagem | fMRI regional heterogênea em RCTs de probiótico (Crocetta) | baixo-médio |',
    '| Neuroimagem | fMRI regional heterogênea em RCTs de probiótico (Crocetta) | baixo-médio |\n'+trev,'tabela')

# ---------- 15) CONTROVÉRSIAS: regras B7-CAUSAL ----------
regras=('- **REGRAS B7-CAUSAL (fixação GPM 2026-09-09):**\n'
'  - **B7-CAUSAL-01:** sem ponte funcional fechada (função microbiana → metabólito → alvo →\n'
'    barreira/imunidade/neural → circulação/BBB → SNC → neurotransmissão/plasticidade → comportamento),\n'
'    correlação de **composição** microbiana não constitui mecanismo causal — cada seta é unidade\n'
'    independente de evidência.\n'
'  - **B7-CAUSAL-02:** quando o metabólito é investigado isoladamente (administrado/rastreado), o claim\n'
'    permitido é **metabólito → cérebro**, nunca "microbiota → cérebro" — guarda-case: IPrA\n'
'    (Sathyasaikumar 2024)[ML]; KYNA bacteriana in vitro (Schwarcz 2024)[ML].\n'
'  - **B7-CAUSAL-03:** microbiota ↔ depressão em humano permanece **ASSOCIATIVA** até mediação/intervenção\n'
'    fecharem a cadeia (Lin 2023)[EC]; (Zhou 2023)[EC]; (Zhang Q 2025)[EC].\n'
'  - **Formulações protegidas:** Erny 2021 lê-se "acetato microbiano → aptidão metabólica/maturação\n'
'    microglial → função", não "AGCC é anti-inflamatório"; a cadeia AGCC cerebral→ACSS2→PPARγ→TPH2 é\n'
'    **roedor** (Chen 2024)[ML], proibida a transcrição clínica completa; germ-free segue [APENAS\n'
'    PRÉ-CLÍNICO]/[EXT].')
rep('- **Hype:** campo mais "vendido além da prova" da série.',
    regras+'\n- **Hype:** campo mais "vendido além da prova" da série.','regras')

# ---------- 16) fecho: blockquote v2 ----------
rep('> causalidade animal é [ML]/[EXT]; probiótico tem evidência pequena/heterogênea (sem prescrição,\n> P20). 2ª verificação independente (P-6) é pendência do avaliador cego.',
    '> causalidade animal é [ML]/[EXT]; probiótico tem evidência pequena/heterogênea (sem prescrição,\n> P20). 2ª verificação independente (P-6) é pendência do avaliador cego.\n\n> **Canônica v2 (Rodada [AT] GPM B7, 2026-09-09).** Reconciliação de insumo externo (P-7): anexo com 196\n> referências + Carabotti 2015 (sem DOI, resgatada por busca dirigida); G1 eutils resolveu 192/196 (4\n> não-indexados — Thomas 2021, Towriss 2026, Xia 2025, Zhang 2026 — mantidos fora, sem fonte forjada);\n> 0 falsos positivos; 8 sobreposições com a V1; decisão ref a ref: **31 ENTRA / 131 BAIXO / 26 EXC**\n> (malha de escopo, exposta no relatório de auditoria). **V2 = 116 referências canônicas (85+31).**\n> Regras B7-CAUSAL-01/02/03 fixadas em CONTROVÉRSIAS. 2ª verificação independente (P-6) permanece\n> PENDENTE do avaliador cego, incluindo as levas [AT] B1–B16.','fecho')

# ---------- saneamentos ----------
bad=re.findall(r'\b\d{7,9}\b', doc)
assert not bad, f'dígitos longos na prosa: {bad[:5]}'
for rid in ['REF_GUO_2013']:
    pass
# valida trechos literalmente presentes (contra órfãos)
falt=[k for k,v in trechos.items() if v and doc.count(v)!=1]
# KUO teve trecho placeholder -> definir agora
trechos['REF_KUO_2021']='a proteína de junção **ZO-1 é dispensável para a função de barreira** (mas crítica para o reparo mucoso),\n'
assert trechos['REF_KUO_2021'] in doc
falt=[k for k,v in trechos.items() if doc.count(v)!=1]
assert not falt, f'trechos âncora não únicos/ausentes: {falt}'

open(DST,'w',encoding='utf-8').write(doc)
import json
json.dump(trechos, open(f'{BASE}/producao/insumos/b7_trechos_ancora.json','w'), ensure_ascii=False, indent=1)
print('V2 gravada:', DST)
print('palavras:', len(doc.split()))
print('trechos ok:', len(trechos))
# check listras
for lbl in ['AburtoCryan2024_barreiras[OB]','Guo2013_LPS_TLR4CD14_TJ[ML]','Ohara2025_neuroepitelio[OB]','Zhang2025_multiomica_cognicao[EC]']:
    assert doc.count(lbl)==1, lbl
print('listras ok')
