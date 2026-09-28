# -*- coding: utf-8 -*-
"""Gera b10_refs_data.json: 98 refs novas (rodada [AT] GPM B10) campos completos."""
import json

EF = json.load(open('/home/user/BIBLIOTECAS/B10_DesregulacaoCircadiana/producao/insumos/b10_efetch_all.json'))

# id, pmid, prosa (citação), tag, bloco, achado (uma linha honesta)
D = [
# ---- TTFL (BLOCO01.001-016) ----
("SATO_2006","16474406","Sato 2006","ML","BLOCO01","A repressão por retroalimentação é obrigatória para a função do relógio circadiano de mamíferos."),
("KUME_1999","10428031","Kume 1999","ML","BLOCO01","CRY1 e CRY2 são componentes essenciais do braço negativo do laço transcricional (TTFL)."),
("YE_2011","21613214","Ye 2011","ML","BLOCO01","Reconstituição bioquímica do modelo canônico de feedback negativo do relógio de mamíferos."),
("YE_2014","25228643","Ye 2014","ML","BLOCO01","CRY e PER inibem CLOCK:BMAL1 por dois modos distintos no TTFL de mamíferos."),
("DUONG_2011","21680841","Duong 2011","ML","BLOCO01","Mecanismo molecular do feedback negativo do relógio via complexos repressivos macromoleculares."),
("NANGLE_2014","25127877","Nangle 2014","ML","BLOCO01","Montagem molecular do complexo repressor transcricional PER–criptocromo."),
("XU_2015","25961797","Xu 2015","ML","BLOCO01","CRY1 regula o relógio por interações dinâmicas com o C-terminal de BMAL1."),
("MICHAEL_2017","28143926","Michael 2017","ML","BLOCO01","A formação do complexo repressor do relógio é mediada pelo bolso secundário de CRY1."),
("LANDEDINER_2013","24043798","Lande-Diner 2013","ML","BLOCO01","Um laço de feedback positivo conecta CLOCK–BMAL1 ao maquinário basal de transcrição."),
("ABE_2022","35999195","Abe 2022","ML","BLOCO01","A transcrição rítmica de Bmal1 estabiliza o sistema de marcação temporal em mamíferos."),
("GORIKI_2014","24736997","Goriki 2014","ML","BLOCO01","A proteína CHRONO funciona como componente de núcleo do relógio circadiano de mamíferos."),
("OTOBE_2026","41108717","Otobe 2026","OB","BLOCO01","Revisão: a fosforilação de CLOCK e BMAL1 é mecanismo regulatório chave do relógio de mamíferos."),
("SERRANO_2026","42290481","Serrano 2026","ML","BLOCO01","CK1δ nuclear é determinante crítico da dinâmica do complexo PER:CRY e do período circadiano."),
("ARYAL_2017","28886335","Aryal 2017","OB","BLOCO01","Revisão das assembleias macromoleculares do relógio circadiano de mamíferos."),
("OISHI_2003","12865428","Oishi 2003","ML","BLOCO01","Análise genômica de expressão hepática revela genes de saída circadianos regulados por CLOCK."),
("TAKAHASHI_2015","26332962","Takahashi 2015","OB","BLOCO01","Revisão dos componentes moleculares do relógio circadiano em mamíferos."),
# ---- SCN/fótica (BLOCO01.017-033) ----
("MOHAWK_2011","21665298","Mohawk 2011","OB","BLOCO01","Revisão: autonomia celular e sincronia dos osciladores circadianos do núcleo supraquiasmático."),
("WELSH_2010","20148688","Welsh 2010","OB","BLOCO01","Revisão anual: SCN — autonomia celular e propriedades de rede."),
("SHAN_2020","32768389","Shan 2020","ML","BLOCO01","Imagem dual em célula única revela papel circadiano na sincronia da rede do SCN."),
("ONO_2024","38366616","Ono 2024","OB","BLOCO01","O núcleo supraquiasmático aos 50 anos: retrospectiva e prospectiva (revisão)."),
("JONES_2018","30082421","Jones 2018","ML","BLOCO01","Neurônios VIP do SCN são essenciais para o reajuste normal do relógio pela luz."),
("HAMNETT_2019","30710088","Hamnett 2019","ML","BLOCO01","VIP controla a rede do relógio do SCN via sinalização ERK1/2 e DUSP4."),
("XU_2021","34416169","Xu 2021","ML","BLOCO01","NPAS4 regula a resposta transcricional do SCN à luz e o comportamento circadiano."),
("VONGALL_1998","9852576","Von Gall 1998","ML","BLOCO01","CREB no SCN como interface molecular dos estímulos de fase (luz, glutamato, PACAP, melatonina)."),
("FERNANDEZ_2016","27162356","Fernandez 2016","ML","BLOCO01","Arquitetura das projeções retinianas ao marcapasso circadiano central."),
("GOLOMBEK_2010","20664079","Golombek 2010","OB","BLOCO01","Revisão de referência da fisiologia do entrançamento circadiano."),
("RAMKISOENSING_2015","26097465","Ramkisoensing 2015","OB","BLOCO01","Sincronização de neurônios-relógio por luz e feedback periférico promove ritmos e saúde (revisão)."),
("MCGLASHAN_2018","30555405","McGlashan 2018","EC","BLOCO01","A resposta da área supraquiasmática humana à luz (fMRI) apresenta variabilidade individual mapeável."),
("PETT_2018","30456356","Pett 2018","ML","BLOCO01","Laços de feedback coexistentes geram ritmos circadianos tecido-específicos."),
("SCHIBLER_2015","26683231","Schibler 2015","OB","BLOCO01","Revisão do diálogo entre osciladores circadianos centrais e periféricos em mamíferos."),
("KIESSLING_2014","24658072","Kiessling 2014","ML","BLOCO01","A luz estimula a adrenal de camundongo por via retino-hipotalâmica independente do relógio do SCN."),
("ROBERTSONDIXON_2023","37895351","Robertson-Dixon 2023","OB","BLOCO01","Revisão sistemática: o comprimento de onda da luz influencia os ritmos do eixo HPA humano."),
("ROBERTSONDIXON_2026","41389872","Robertson-Dixon 2026","OB","BLOCO01","Meta-análise em animais não humanos: o comprimento de onda da luz influencia a função do eixo HPA."),
# ---- HPA (BLOCO02.001-017) ----
("NICOLAIDES_2014","24890877","Nicolaides 2014","OB","BLOCO02","Ritmos endócrinos circadianos: o eixo HPA e suas ações (revisão)."),
("NADER_2010","20106676","Nader 2010","OB","BLOCO02","Interações do sistema CLOCK circadiano com o eixo HPA (revisão)."),
("RUSSELL_2015","25494867","Russell 2015","OB","BLOCO02","Osciladores biológicos coordenam atividade do HPA, resposta glicocorticoide tecidual e adaptação neurocomportamental (revisão)."),
("KALSBEEK_2012","21782883","Kalsbeek 2012","OB","BLOCO02","Ritmos circadianos no eixo HPA (revisão)."),
("SPIGA_2014","24944037","Spiga 2014","OB","BLOCO02","Ritmos do eixo HPA (revisão de fisiologia abrangente)."),
("RAOANDROULAKIS_2019A","30862458","Rao & Androulakis 2019a","OB","BLOCO02","Significado fisiológico da dinâmica circadiana do HPA: ritmos, alostase e resiliência (revisão)."),
("RAOANDROULAKIS_2019B","31371802","Rao & Androulakis 2019b","OB","BLOCO02","Adaptação alostática e trocas fisiológicas personalizadas na regulação circadiana do HPA (modelagem matemática)."),
("RAO_2021","34436424","Rao 2021","OB","BLOCO02","Modelagem da influência da restrição crônica de sono sobre os ritmos circadianos de cortisol."),
("KINLEIN_2020","31863788","Kinlein & Karatsoreos 2020","OB","BLOCO02","O eixo HPA como substrato de resiliência ao estresse: interações com o relógio circadiano (revisão)."),
("VANDALFSEN_2018","29126903","van Dalfsen & Markus 2018","OB","BLOCO02","Revisão sistemática: o sono influencia a reatividade do eixo HPA humano."),
("BUCKLEY_2005","15728214","Buckley 2005","OB","BLOCO02","Revisão clássica das interações entre o eixo HPA e o sono (atividade normal e distúrbios exemplares)."),
("YAMANAKA_2019","30480877","Yamanaka 2019","EC","BLOCO02","A resposta aguda do eixo HPA ao estresse psicológico difere entre manhã e noite em humanos."),
("WESARGMENZEL_2024","38308964","Wesarg-Menzel 2024","OB","BLOCO02","Parâmetros diurnos de cortisol se associam à reatividade e recuperação ao estresse (revisão sistemática/meta-análise)."),
("LIGHTMAN_2020","32060528","Lightman 2020","OB","BLOCO02","Dinâmica da secreção de ACTH e cortisol e implicações para doença (revisão de referência)."),
("DENBOON_2017","29223280","den Boon & Sarabdjitsingh 2017","OB","BLOCO02","Padrões circadianos e ultradianos da atividade do HPA em roedores: significado para a função cerebral (revisão)."),
("CHELLAPPA_2020","33122670","Chellappa 2020","EC","BLOCO02","O desalinhamento circadiano aumenta a vulnerabilidade de humor em trabalho por turnos simulado (crossover humano)."),
("CHRISTIANSEN_2012","22217141","Christiansen 2012","ML","BLOCO02","Atividade circadiana do eixo HPA é diferencialmente afetada no modelo de estresse leve crônico (rato) nos animais que desenvolvem fenótipo depressivo."),
# ---- genética (BLOCO03.001-004) ----
("SORIA_2010","20072116","Soria 2010","EC","BLOCO03","Associação genética diferencial de genes circadianos: CRY1/NPAS2 com depressão unipolar; CLOCK/VIP com bipolar."),
("VONSCHANTZ_2021","33641746","von Schantz 2021","OB","BLOCO03","Perspectivas genômicas da hipótese do relógio circadiano nos transtornos psiquiátricos (revisão)."),
("LIBERMAN_2018","29614896","Liberman 2018","OB","BLOCO03","Modelagem fortalece o elo molecular entre polimorfismos circadianos e transtornos do humor."),
("MCCARTHY_2011","21781277","McCarthy 2011","EC","BLOCO03","Variação funcional na via REV-ERBα associada à resposta ao lítio no transtorno bipolar."),
# ---- clínica geral (BLOCO02.018-026) ----
("ROBILLARD_2018","30301878","Robillard 2018","EC","BLOCO02","Subgrupos fisiopatológicos definidos por marcadores circadianos em jovens com depressão unipolar ligam-se a perfis psiquiátricos distintos."),
("NGUYEN_2019","30878655","Nguyen 2019","EC","BLOCO02","Cronotipagem molecular in vivo: desalinhamento circadiano e altas taxas de depressão em jovens adultos."),
("PILZ_2018","30061722","Pilz 2018","EC","BLOCO02","Ritmicidade dos sintomas de humor em indivíduos com risco aumentado para transtornos psiquiátricos."),
("EMENS_2020","32777620","Emens 2020","EC","BLOCO02","Ritmo circadiano do afeto negativo com pico na noite circadiana — implicações para transtornos de humor."),
("MURRAY_2017","28364473","Murray 2017","EC","BLOCO02","No DSPD clínico, o subtipo circadiano (DLMO desalinhado) carrega mais sintomas depressivos; quase metade dos casos não mostra desalinhamento."),
("LYALL_2018","29776774","Lyall 2018","EC","BLOCO02","Ritmicidade circadiana disruptiva associada a transtornos de humor, bem-estar subjetivo e cognição em coorte populacional."),
("SONG_2024","38579366","Song 2024","EC","BLOCO02","Dinâmica causal diária entre sono, fase circadiana estimada e sintomas de humor modelada com dados de wearables."),
("COXOLATUNJI_2019","31302521","Cox & Olatunji 2019","EC","BLOCO02","A relação cronotipo–ansiedade persiste controlando distúrbio de sono e afeto negativo."),
("CARPENTER_2025","40662977","Carpenter 2025","EC","BLOCO02","Evidência de desalinhamento interno entre marcadores de fase (DLMO vs pico de cortisol) em jovens com transtornos de humor emergentes."),
# ---- bipolar (BLOCO11.001-014) ----
("MELO_2017","27524206","Melo 2017","OB","BLOCO11","Cronotipo e ritmo circadiano no transtorno bipolar (revisão sistemática)."),
("TAKAESU_2018","29869403","Takaesu 2018","OB","BLOCO11","Ritmo circadiano no transtorno bipolar (revisão da literatura)."),
("ALLOY_2017","28321642","Alloy 2017","OB","BLOCO11","Desregulação do ritmo circadiano nos transtornos do espectro bipolar (revisão)."),
("MOON_2016","27543154","Moon 2016","EC","BLOCO11","Fase circadiana avançada na mania e atrasada na depressão bipolar/mista, com normalização após tratamento."),
("VIDAFAR_2021","34468894","Vidafar 2021","EC","BLOCO11","Cronotipo tardio prediz mais sintomas depressivos no transtorno bipolar em seguimento de cinco anos."),
("ESAKI_2021","34645802","Esaki 2021","EC","BLOCO11","Ritmos circadianos de atividade associados à recaída de episódios de humor no bipolar (coorte prospectiva)."),
("MUKHERJEE_2022","34320487","Mukherjee 2022","EC","BLOCO11","Padrão diurno de cortisol desregulado e cortisol noturno elevado no transtorno bipolar."),
("LEI_2024","38800632","Lei 2024","EC","BLOCO11","Disfunção do ritmo circadiano e psicopatologia em descendentes de pais com bipolar (estudo de alto risco)."),
("SCOTT_2022","35182537","Scott 2022","OB","BLOCO11","Distúrbios de sono e ritmo circadiano em indivíduos de alto risco ou com início precoce de transtorno bipolar (revisão sistemática/meta-análise)."),
("PALAGINI_2022","35821870","Palagini 2022","EC","BLOCO11","Alterações circadianas relacionadas a resiliência prejudicada, desregulação emocional e gravidade afetiva no bipolar I/II."),
("TONON_2024","39210713","Tonon 2024","OB","BLOCO11","Sono e disrupção circadiana no transtorno bipolar: da psicopatologia à fenotipagem digital (revisão)."),
("GEOFFROY_2025B","40381827","Geoffroy & Maruani 2025","OB","BLOCO11","Cronobiologia dos transtornos do humor: o papel do relógio biológico na depressão e no bipolar (revisão de referência)."),
("MCCARTHY_2022","34850507","McCarthy 2022","OB","BLOCO11","Mecanismos neurobiológicos e comportamentais da disrupção circadiana no bipolar — consenso multidisciplinar da task force ISBD de cronobiologia."),
("CHAKRABORTY_2026","41913359","Chakraborty 2026","OB","BLOCO11","Anormalidades circadianas, genes-relógio moleculares e tratamento cronobiológico nos transtornos psiquiátricos (revisão)."),
# ---- biomarcadores/exposição (BLOCO05.001) ----
("DEPRATO_2025","40154089","Deprato 2025","OB","BLOCO05","Luz à noite e saúde mental: associação consistente, com avaliação de exposição em evolução (revisão sistemática/meta-análise)."),
# ---- cronoterapia (BLOCO06.001-002) ----
("WESCOTT_2025","39608218","Wescott 2025","OB","BLOCO06","Realinhamento circadiano pode melhorar a depressão em subgrupos; a mediação pela fase fisiológica não está demonstrada (revisão sistemática)."),
("CAMPBELL_2017","31528147","Campbell 2017","OB","BLOCO06","Fototerapia: transtorno afetivo sazonal e além (revisão)."),
# ---- causal experimental (BLOCO07.001-005) ----
("RUSSELL_2021","33509094","Russell 2021","ML","BLOCO07","Knockout de Per2 desorganiza a secreção de corticosterona e gera comportamento tipo-depressivo e déficit de startle."),
("ZUO_2024","38241675","Zuo 2024","ML","BLOCO07","Desalinhamento circadiano prejudica a mielinização oligodendroglial via Bmal1 (inibição AKT/mTOR), gerando fenótipo tipo ansiedade/depressão."),
("TOFANI_2025","39504963","Tofani 2025","ML","BLOCO07","A microbiota intestinal regula a responsividade ao estresse através do sistema circadiano (ritmicidade do HPA)."),
("FRANCIS_2023","37441675","Francis 2023","ML","BLOCO07","Regulação tipo-celular específica de humor e ansiedade pelo sistema relógio circadiano no cérebro (revisão pré-clínica)."),
("KANDALEPAS_2016","27362940","Kandalepas 2016","ML","BLOCO07","A melatonina reajusta o relógio do SCN ao entardecer requerendo transcrição mediada por E-box de Per1/Per2."),
# ---- pontes (BLOCO08.001) ----
("BAUTISTA_2025","41244880","Bautista 2025","OB","BLOCO08","Eixo intestino–cérebro–circadiano em ansiedade e depressão (revisão crítica)."),
# ---- revisões gerais (BLOCO12.001-012) ----
("HYNDYCH_2025","41662130","Hyndych 2025","OB","BLOCO12","Interações bidirecionais entre sono e transtornos psiquiátricos e mecanismos neurobiológicos compartilhados (revisão)."),
("ZOU_2022","36033630","Zou 2022","OB","BLOCO12","Cronotipo, ritmo circadiano e transtornos psiquiátricos: evidências recentes e mecanismos potenciais (revisão)."),
("MEYER_2024","38394243","Meyer 2024","OB","BLOCO12","A interface sono–circadiano como janela para os transtornos mentais (revisão)."),
("WALKER_2020","32066704","Walker 2020","OB","BLOCO12","Disrupção do ritmo circadiano e saúde mental (revisão)."),
("DOLLISH_2024","37858331","Dollish 2024","OB","BLOCO12","Ritmos circadianos e transtornos de humor: hora de ver a luz (revisão de referência)."),
("KIRLIOGLU_2020","32750762","Kırlıoğlu 2020","OB","BLOCO12","Cronobiologia revisitada nos transtornos psiquiátricos: perspectiva translacional (revisão)."),
("LAMONT_2007","17969870","Lamont 2007","OB","BLOCO12","O papel dos genes do relógio circadiano nos transtornos mentais (revisão)."),
("MCCLUNG_2007","17395264","McClung 2007","OB","BLOCO12","Genes e ritmos circadianos na biologia dos transtornos de humor (revisão)."),
("MCCLUNG_2013","23558300","McClung 2013","OB","BLOCO12","Como os ritmos circadianos poderiam controlar o humor (revisão mecanística)."),
("KETCHESIN_2020","30402924","Ketchesin 2020","OB","BLOCO12","Relógios centrais e periféricos relacionados ao humor (revisão)."),
("SMITH_2024","39308240","Smith 2024","OB","BLOCO12","Cronopsiquiatria como campo articulado (artigo temático de referência)."),
("PANDIPERUMAL_2022","35033557","Pandi-Perumal 2022","OB","BLOCO12","O timing é tudo: ritmos circadianos e seu papel no controle do sono (revisão)."),
]


DESENHO = {
"ML":"modelo animal/celular/molecular (pré-clínico)",
"EC":"estudo humano (observacional/experimental)",
"OB":"revisão/síntese narrativa ou sistemática",
}
NATUREZA = {"ML":"nao_estabelecida","EC":"associativa","OB":"contributiva"}
MATUR   = {"ML":"emergente","EC":"emergente","OB":"bem_suportado"}
TIER    = {"ML":"tier_3_correlacional_mecanistico","EC":"tier_4_descritivo_estrutural","OB":"tier_4_descritivo_estrutural"}
ROLE    = {"ML":"preclinical_mechanistic","EC":"human_clinical","OB":"review"}
G2      = {"ML":"redirecionado_mecanistico","EC":"eligible","OB":"eligible"}
VERIF   = {"ML":"preclinico","EC":"emergente","OB":"emergente"}
ACAO    = {"ML":"ADICIONAR_SINALIZADOR","EC":"MANTER","OB":"MANTER"}

def split_aliases(prosa):
    # "Rao & Androulakis 2019a" -> sobrenomes sem ano
    base = prosa.rsplit(' ',1)[0]
    als=[base.upper(), base]
    parts = [p.strip() for p in base.replace('&','|').split('|')]
    for p in parts:
        if p and p not in als: als.append(p)
    # diacríticos preservados; adiciona forma sem acento quando houver
    import unicodedata
    for p in list(als):
        s=unicodedata.normalize('NFKD',p).encode('ascii','ignore').decode()
        if s and s not in als: als.append(s)
    return als

out=[]
counters={}
for (rid,pmid,prosa,tag,bloco,achado) in D:
    m=EF[pmid]
    counters[bloco]=counters.get(bloco,0)+1
    claim=f"B10.MEC.{bloco}.{counters[bloco]:03d}"
    mesh=m.get('mesh') or []
    species=[s for s in mesh if s in ('Humans','Animals')]
    pts=m.get('pubtypes') or []
    isrev=any('Review' in p or 'Meta-Analysis' in p for p in pts)
    if tag=="ML":
        extr="SIM — evidência em roedor/célula/modelo; tradução humana por analogia"
        if isrev: extr="SIM — revisão de evidência pré-clínica (roedor/célula); tradução humana por analogia"
    elif tag=="OB":
        if 'Animals' in species and 'Humans' not in species: extr="parcial — revisão mistura espécies"
        else: extr="não — avaliado por título/abstract (MeSH pendente de indexação)" if not species else "não"
    else:
        extr="não"
    ano=m.get('ano_print') or (m.get('ano_epub') or '')[:4] or ''
    rev=f"{m.get('revista_iso') or m.get('revista_full') or ''} ({ano})"
    des=f"[{tag}] {DESENHO[tag]} · {m.get('revista_iso') or m.get('revista_full')}"
    out.append({
      "pmid_oficial": pmid,
      "titulo_artigo": m['titulo'],
      "autores": m['autores'],
      "revista_ano": rev,
      "desenho_estudo": des,
      "secao_origem": "mecanismo_B10_desregulacao_circadiana",
      "achado_central_molecular": achado,
      "extrapolacao_por_analogia": extr,
      "ids_referencia_interna": [f"REF_{rid}"],
      "id_referencia_interna": f"REF_{rid}",
      "doi": m.get('doi') or '',
      "claim_id_origem": claim,
      "evid_role": ROLE[tag],
      "especie_mesh": species,
      "verification_status": VERIF[tag],
      "citacao_confirmada": True,
      "g1_metodo": "eutils_automatico",
      "g2_elegibilidade": G2[tag],
      "g2_motivo": f"rodada [AT] GPM B10 {bloco} — insumo externo auditado ref a ref (P-7)",
      "g3_verificado_por": "IA G3 (Rodada [AT] GPM B10 2026-09-09, insumo externo auditado ref a ref; P-7): esearch DOI[aid]/PMID + esummary + efetch; abstract lido; 2a verificação independente (P-6) pendente",
      "status_auditoria": "CONFIRMADO",
      "origem_pipeline": "GPM_RODADA_AT",
      "_aliases": split_aliases(prosa),
      "_prosa": prosa, "_tag": tag, "_bloco": bloco,
      "_natureza": NATUREZA[tag], "_maturidade": MATUR[tag], "_tier": TIER[tag], "_acao": ACAO[tag],
    })
json.dump(out, open('/home/user/BIBLIOTECAS/B10_DesregulacaoCircadiana/producao/insumos/b10_refs_data.json','w'), ensure_ascii=False, indent=1)
print('refs novas:', len(out))
from collections import Counter
print(Counter(x['_bloco'] for x in out))
print(Counter(x['_tag'] for x in out))
# ids únicos + pmids únicos + sem colisão com V1
v1=json.load(open('/home/user/BIBLIOTECAS/B10_DesregulacaoCircadiana/Evidencias/Bibliografia/01_pmids.json'))
idsv1={r['id_referencia_interna'] for r in v1}; pmv1={r['pmid_oficial'] for r in v1}
idsn=[x['id_referencia_interna'] for x in out]; pmn=[x['pmid_oficial'] for x in out]
assert len(set(idsn))==len(idsn), 'id dup'
assert len(set(pmn))==len(pmn), 'pmid dup'
assert not (set(idsn)&idsv1), 'colisão id: %s'%(set(idsn)&idsv1)
assert not (set(pmn)&pmv1), 'colisão pmid: %s'%(set(pmn)&pmv1)
print('OK sem colisões; total projetado:', len(idsv1)+len(idsn))
