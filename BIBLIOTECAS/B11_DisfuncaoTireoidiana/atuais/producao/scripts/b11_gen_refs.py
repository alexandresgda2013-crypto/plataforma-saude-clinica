# -*- coding: utf-8 -*-
"""Gera b11_refs_data.json (57 ENTRA novos) + matriz_b11_decisao.json para a V2 da B11."""
import json, re, unicodedata
BASE='/home/user/BIBLIOTECAS/B11_DisfuncaoTireoidiana/'
M=json.load(open(BASE+'producao/insumos/matriz_b11_g1.json'))
META=M['meta']; ABS=json.load(open(BASE+'producao/insumos/b11_efetch_sel.json'))
def norm(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()
    return re.sub(r'[^A-Z]','',s.upper())
def mk_ref(pmid, id_, tag, desenho, sec, achado, extr, role, mesh, g2, g2mot, tier_nat, mat, acao, doi=''):
    m=META.get(pmid,{})
    return {"pmid_oficial":pmid,"titulo_artigo":m.get('title',''),"autores":m.get('authors',[]),
      "revista_ano":f"{m.get('source','')} ({m.get('pubdate','')[:4]})","desenho_estudo":f"[{tag}] {desenho} · {m.get('source','')}",
      "secao_origem":f"mecanismo_B11_{sec}","achado_central_molecular":(achado or ABS.get(pmid,'')[:220] or m.get('title','')),
      "extrapolacao_por_analogia":extr,"ids_referencia_interna":[id_],"id_referencia_interna":id_,"doi":doi,
      "claim_id_origem":"B11.MEC.BLOCO14.001","evid_role":role,"especie_mesh":mesh,"verification_status":"humano_clinico" if tag in("EC","OB") else "preclinico",
      "citacao_confirmada":True,"g1_metodo":"eutils_automatico","g2_elegibilidade":g2,"g2_motivo":g2mot,
      "g3_verificado_por":"IA G3 Rodada [AT] GPM B11 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
      "status_auditoria":"CONFIRMADO","origem_pipeline":"GPM_RODADA_AT","_aliases":[],
      "_nat":tier_nat,"_mat":mat,"_acao":acao,"_tier":"tier_4_descritivo_estrutural" if tag in("EC","OB") else "tier_3_correlacional_mecanistico"}
N="não — avaliado por título/abstract (MeSH pendente de indexação)"
H=["Humans"]
R=[]
def E(pmid, autor, ano, tag, desenho, sec, achado, role="human_clinical", g2="eligible", g2mot="ELIGIBLE_SOURCE", nat="associativa", mat="moderadamente_suportado", extr=N, mesh=H):
    id_=f"REF_{norm(autor)}_{ano}"
    R.append(mk_ref(pmid,id_,tag,desenho,sec,achado,extr,role,mesh,g2,g2mot,nat,mat,"MANTER"))
    return id_
# ============ ÂNCORAS (11) ============
E("29064607","Fischer",2018,"OB","revisão sistemática","eixo_hpt_ansiedade","Revisão sistemática do eixo HPT nos transtornos de ansiedade: alterações modestas e heterogêneas; contraste com a literatura de depressão; ansiedade permanece menos mapeada que depressão.",role="review",nat="contributiva",mat="bem_suportado")
E("29408972","Kim",2018,"EC","coorte prospectiva (adultos jovens e de meia-idade)","sch_incidente_neg","SCH não se associou a depressão incidente em adultos jovens/de meia-idade em coorte prospectiva — evidência NEGATIVA canônica.")
E("30375372","Zhao",2018,"OB","meta-análise","sch_meta","Meta-análise SCH×depressão: associação fraca/inerentemente inconsistente contra coortes negativas.",role="review",nat="contributiva",mat="bem_suportado")
E("31214119","Tang",2019,"OB","revisão sistemática e meta-análise","sch_meta","SR/MA SCH×depressão: sinal de associação em estudos transversais, sem estabelecer causalidade.",role="review",nat="contributiva",mat="bem_suportado")
E("33154486","Wildisen",2020,"EC","análise individual de dados de participantes (IPD) de coortes prospectivas (~23 mil)","sch_ipd_neg","IPD de coortes prospectivas: SCH não se associou a sintomas depressivos de forma robusta — evidência NEGATIVA de maior hierarquia.",mat="bem_suportado")
E("34129186","Bauer",2021,"OB","revisão terapêutica","terapia_sinal","Revisão do papel dos hormônios tireoidianos como adjuvantes em depressão: sinal terapêutico histórico (T3/T4) que não autoriza tratar toda depressão como tireoidiana (P20, sem doses).",role="review",nat="contributiva",mat="bem_suportado")
E("34147730","Airaksinen",2021,"EC","coorte populacional (NHANES)","sch_nhanes_neg","NHANES: SCH sem associação clara a sintomas depressivos no geral; análise sintoma-específica — evidência NEGATIVA canônica.")
E("36463425","Soheili",2023,"EC","estudo genético (ligações genéticas/compartilhadas)","genetica_compartilhada","Variações de hormônio tireoidiano dentro da faixa normal associam-se a risco de transtornos psiquiátricos comuns via ligação genética compartilhada — não estabelece causalidade individual (correção editorial Zhang 2024, PMID 37155921, registrada como metadado).",mat="emergente")
E("37855318","Roa Dueñas",2024,"EC","coorte populacional transversal e longitudinal","funcao_tireoidiana_depressao","Associação transversal e longitudinal entre função tireoidiana e depressão em coorte populacional; causalidade reversa não excluída — regra bidirecional.",mat="bem_suportado")
E("39280013","Ma",2024,"EC","estudo observacional (transversal)","depressao_funcao_tireoidiana","Associação entre depressão e função tireoidiana em análise transversal; FT3 como marcador associativo — sem FT3 prospectivo [G1].")
E("40226662","Fan",2024,"EC","coorte prospectiva UK Biobank","bidirecional_ukbiobank","UK Biobank prospectivo: depressão e ansiedade associam-se a risco subsequente de doença tireoidiana — direção reversa documentada; bidirecionalidade obrigatória.",mat="bem_suportado")
# ============ CONTROVÉRSIA SCH / COORTES ============
E("25777685","Ittermann",2015,"EC","coorte populacional (SHIP) com diagnósticos por entrevista","diagnosticos_gold","Transtornos tireoidianos diagnosticados associaram-se a depressão e ansiedade definidas por entrevista padrão — desfecho por gold-standard, não só escala.",mat="bem_suportado")
E("25580957","Bensenor",2016,"EC","coorte transversal populacional (ELSA-Brasil)","elsa_brasil","ELSA-Brasil: disfunção tireoidiana subclínica e transtornos psiquiátricos em coorte brasileira de base populacional — sinal associativo latino-americano.")
E("12100345","Engum",2002,"EC","coorte populacional (HUNT)","hunt_funcao","HUNT: associação entre depressão/ansiedade e função tireoidiana questionada como possível artefato — contribuição escéptica clássica.",nat="nao_estabelecida",mat="bem_suportado")
E("16253615","Engum",2005,"EC","coorte populacional (HUNT)","hunt_autoimunidade","HUNT: autoimunidade tireoidiana (anti-TPO) e depressão/ansiedade em amostra populacional ampla — associação fraca/ausente na base populacional.",nat="nao_estabelecida",mat="bem_suportado")
E("30106989","Hong",2018,"EC","inquérito populacional (KNHANES)","knanhnes_sch","KNHANES: disfunção tireoidiana subclínica e sintomas depressivos em adultos coreanos sem doença tireoidiana franca.")
E("25973566","Kim",2015,"EC","coorte retrospectiva","tsh_faixa_bdi","Níveis de TSH dentro da faixa de referência e risco de sintomas depressivos (BDI) — variação intra-faixa sem corte clínico (regra não-linearidade≠faixa ótima).")
E("30772742","Lee",2019,"EC","estudo transversal populacional","tsh_sexo_depressao","Diferenças de sexo na associação entre TSH (dentro da faixa) e sintomas depressivos — heterogeneidade por sexo como moderador.")
E("37419569","Kumar",2023,"EC","coorte histórica populacional (Mayo)","mayo_tsh_phq9","Coorte histórica Mayo: TSH e depressão clinicamente relevante (PHQ-9) em amostra ampla — sinal populacional contemporâneo.",mat="bem_suportado")
E("40163571","Liu",2025,"EC","coorte histórica","coorte_historica_tsh","Coorte histórica independente: função tireoidiana e depressão — convergência com sinais de coortes maiores.",mat="emergente")
E("41825352","Baweja",2026,"EC","coorte clínica retrospectiva real-world","realworld_tireoide_depressao","Coorte real-world retrospectiva: tireoide e depressão na prática clínica — sinal de mundo real, suscetível a confusão por indicação.",mat="emergente")
E("40133129","Forbes",2025,"EC","estudo transversal e longitudinal em idosos","idosos_tsh_depressao","TSH e depressão em idosos, transversal e longitudinal — complementa a evidência negativa geriátrica.",mat="emergente")
E("17043339","Roberts",2006,"EC","estudo longitudinal em idosos","idosos_disfuncao_leve","Disfunção tireoidiana leve em idosos: associações com depressão/cognição NÃO confirmadas — evidência NEGATIVA geriátrica clássica.")
E("21890841","Bould",2012,"EC","coorte prospectiva (DEPTH)","depth_angustia","Investigação de disfunção tireoidiana é mais provável em pacientes com alta morbidade psicológica — sinal de triagem, não de caso.",mat="emergente")
E("34427900","Karakatsoulis",2021,"OB","revisão","sch_tdm_autoimunidade","Revisão SCH×TDM: hipótese de mediação autoimune entre disfunção subclínica e depressão maior — mecanismo candidato, não demonstrado.",role="review",nat="contributiva",mat="emergente")
E("30621645","Loh",2019,"OB","revisão sistemática e meta-análise","sch_meta_lt4","MA atualizada SCH×depressão incluindo desfecho de melhora sintomática com LT4 — sinal terapêutico populacional fraco e heterogêneo.",role="review",nat="contributiva",mat="bem_suportado")
E("35946076","Hirtz",2022,"EC","coorte prospectiva nacional em adolescentes e adultos jovens","sch_incidente_jovens","SCH e depressão incidente em adolescentes/adultos jovens (coorte nationwide) — janela etária pouco coberta.",mat="bem_suportado")
# ============ AIT / HASHIMOTO EUTIREOIDIANO ============
E("24211158","Ayhan",2014,"EC","estudo caso-controle com entrevista diagnóstica","hashimoto_eutireoideo","Hashimoto eutireoidiano: prevalência aumentada de depressão e ansiedade correntes vs controles — suporte fenomenológico direto do eixo AIT.")
E("16314199","Gulseren",2006,"EC","estudo transversal comparativo","hashimoto_qv","Tireoidite de Hashimoto (inclusive eutireoidiana): depressão, ansiedade, qualidade de vida e incapacidade — AIT além do status hormonal.")
E("26655116","Delitala",2015,"EC","coorte populacional (SardiNIA)","sardinia_autoimunidade","SardiNIA: sintomas depressivos, hormônio tireoidiano e autoimunidade (anti-TPO) sem medicação — dissociação entre autoimunidade e humor na população.",mat="moderadamente_suportado")
E("39717384","Wang",2024,"OB","revisão sistemática e meta-análise","hashimoto_eutireoideo_meta","SR/MA: depressão e ansiedade em Hashimoto EUTIREOIDIANO — associação presente sem hipotireoidismo; não resolve se AIT causa ou co-ocorre.",role="review",nat="contributiva",mat="bem_suportado")
# ============ ANSIEDADE-ESPECÍFICA ============
E("15256776","Gonen",2004,"EC","estudo transversal ambulatorial","sch_ansiedade","Avaliação de ansiedade em distúrbios tireoidianos subclínicos — sinal ansiedade-específico (vs depressão) em amostra clínica.")
E("37706034","Zhao",2023,"EC","estudo transversal em TDM jovem de primeiro episódio","genero_ansiedade_tdm","Diferenças de gênero na associação entre ansiedade e hormônios tireoidianos em TDM jovem drug-naïve — moderador de gênero, desenho transversal [representante único da família de coortes de primeiro episódio].")
E("41966231","Qiu",2026,"EC","estudo transversal em TDM drug-naïve de primeiro episódio","padrao_nao_linear_tsh","Padrão não-linear ('aumenta-diminui-aumenta') entre TSH e sintomas ansiosos em TDM — reforça não-linearidade; não define faixa ótima.",mat="emergente")
E("33210405","Wu",2020,"EC","estudo caso-controle","autoimune_hormonios","Hormônios tireoidianos desregulados correlacionam-se com risco de ansiedade e depressão em doença autoimune — elo autoimune-humor extraclasse TPO.")
E("33210626","Gorkhali",2020,"EC","estudo transversal","disturbios_tireoidianos_ansiedade","Ansiedade e depressão entre pacientes com distúrbios da função tireoidiana — sinal clínico transcultural (Nepal).",mat="emergente")
E("39833737","Dehesh",2025,"EC","estudo transversal","hipotireoidismo_ansiedade","Prevalência e fatores associados de ansiedade e depressão em hipotireoidismo — população endócrina direta.",mat="emergente")
E("24937789","Aslan",2005,"EC","estudo transversal com entrevista","sintomas_psiq_tireoide","Sintomas e diagnósticos psiquiátricos em distúrbios tireoidianos (transversal) — fenótipo psiquiátrico da doença tireoidiana franca.")
# ============ TRANSIENTES / NTI / MARCADORES ============
E("2129342","Roca",1990,"EC","série clínica com medidas seriadas","transitorio_hiperT4","Elevações TRANSITÓRIAS de hormônios tireoidianos em doença psiquiátrica aguda — distinção de hipertireoidismo verdadeiro; antiartefato clássico.",mat="bem_suportado")
E("2336036","Chopra",1990,"EC","série clínica em internados psiquiátricos","transitorio_tsh","Hipertireotropinemia transitória em internados psiquiátricos agudos — TSH/T4 elevados iniciais revertem; reforça reavaliação, não rótulo.")
E("22318794","Dickerman",2012,"OB","revisão clínica","red_herring","'Red herring': testes tireoidianos anormais em psiquiátricos frequentemente refletem doença não-tireoidiana/transitoriedade — cautela interpretativa central.",role="review",nat="contributiva",mat="bem_suportado")
E("2198197","Hein",1990,"OB","revisão","revisao_funcao_psiq","Revisão clássica da função tireoidiana na doença psiquiátrica — síndrome da doença não-tireoidiana, variabilidade de testes e limites da triagem.",role="review",nat="contributiva",mat="bem_suportado")
E("16840838","Premachandra",2006,"EC","estudo transversal psiquiátrico","lowT3_depressao","Síndrome do T3 baixo em depressão psiquiátrica — T3 reduzido com TSH/T4 preservados; marcador de gravidade transversal, não FT3 prospectivo [G1].")
E("16804044","Saravanan",2006,"EC","estudo transversal em reposição tireoidiana","bemestar_ft4_nao_ft3","Bem-estar psicológico correlaciona-se com FT4, NÃO com FT3, em pacientes sob reposição — achado nulo de FT3 canônico.")
E("40489725","Wilson",2025,"EC","estudo transversal","rT3_reposicao","rT3 (produto de desiodinação periférica D1/D3) em hipotireoidismo sob diferentes esquemas de reposição — âncora periférica de rT3; sinalização CEREBRAL de rT3 permanece [G1].",mat="emergente")
E("19751298","Panicker",2009,"EC","estudo transversal populacional (área de captação)","paradoxo_ansiedade_depressao","Diferença paradoxal: relação TSH×ansiedade em direção distinta de TSH×depressão (em usuários de T4 vs população) — não-linearidade documentada.",mat="emergente")
E("8936670","Woolf",1996,"EC","série prospectiva hospitalar","triagem_tsh_hospitalar","Triagem com TSH em internados psiquiátricos: rendimento e limites — referência histórica do debate 'triar ou não'.")
E("42346303","Toma",2026,"EC","estudo transversal em internados","triagem_internados","Desregulação do eixo HPT em transtornos de humor e ansiedade internados: utilidade clínica da avaliação hormonal rotineira — triagem, não diagnóstico de humor (P20).",mat="emergente")
E("31390496","Luft",2019,"EC","série clínica pediátrica","triagem_jovens","Triagem da função tireoidiana em crianças/adolescentes com transtornos de humor e ansiedade — rendimento baixo mas não nulo.",mat="emergente")
E("34856305","Qiao",2021,"EC","coorte clínica","hormonios_predicao_resposta","Hormônios tireoidianos como preditores candidatos de melhora clínica em deprimidos tratados — biomarcador de resposta emergente, não validado.",mat="emergente")
E("31795239","Romero-Gomez",2019,"EC","estudo transversal comparativo","humor_residual_lt4","Mulheres hipotireoideas EM TRATAMENTO com levotiroxina mantêm carga residual de ansiedade/depressão — normalizar TSH não garante eutimia (confusão por indicação).")
E("17639255","Almeida",2007,"EC","estudo transversal com entrevista (SCID)","sch_prevalencia_brasil","SCH: prevalência de transtornos e sintomas psiquiátricos avaliados por SCID — sinal brasileiro com diagnóstico estruturado.")
E("21152840","Andrade",2010,"EC","estudo caso-controle","hipotireoidismo_sintomas","Sintomas de depressão e ansiedade em mulheres hipotireoideas vs controles — espelho fenomenológico clássico do fenótipo endócrino.")
E("32874682","Costache",2020,"EC","coorte clínica de deprimidos","tsh_t4_deprimidos","TSH e T4 em coorte de pacientes depressivos — perfil hormonal na depressão como janela associativa.",mat="emergente")
E("23449617","Kamble",2013,"EC","estudo caso-controle drug-naïve","t4_t3_gravidade","T4/T3/TSH em deprimidos drug-naïve vs controles, por gravidade (HAM-D) — gradiente dimensional associativo.",mat="emergente")
# ============ TERAPIA-SINAL ============
E("42074695","Hilmon",2026,"EC","estudo observacional em jovens","lt4_jovens_intervencoes","LT4 em hipotireoidismo (inclusive subclínico) de crianças/adolescentes e risco de intervenções psiquiátricas — terapia-sinal, não conduta (P20).",mat="emergente")
# ============ decisões BAIXO/EXC ============
BAIXO = {
"Bathla 2016 (27366712)":"BAIXO — redundância (prevalência clínica coberta por Dehesh/Gorkhali com desenhos equivalentes)",
"Baumgartner 1988 (3136485)":"BAIXO — série 1988 coberta pela revisão clássica Hein 1990",
"Beydoun 2013 (23690311)":"BAIXO — desfecho primário cognitivo (moderação por sintomas depressivos apenas)",
"Bjorklund 2025 (39799523)":"BAIXO — eixo exposição ambiental/poluentes (Cazaquistão), população nominalmente saudável",
"Hakoshima 2025 (41354432)":"BAIXO — mania/episódios bipolares → registrado ao eixo B1",
"Hallab 2024 (39833340)":"BAIXO — ansiedade informada por terceiros em contexto de envelhecimento/cognição",
"Konstantakou 2021 (34421508)":"BAIXO — população gestante/pós-parto (fisiologia hormonal não-equivalente)",
"Lang 2019 (31759671)":"BAIXO — família 1º episódio drug-naïve (mesmo centro), representada por Zhao 2023",
"Lei 2025 (40933156)":"BAIXO — internados heterogêneos por duração de doença; psicopatologia ampla",
"Liu 2025 (40270696)":"BAIXO — família SCH 1º episódio, redundância de centro único",
"Luo 2023 (37201896)":"BAIXO — desfecho sobrepeso/obesidade em TDM",
"Nuguru 2022 (36003348)":"BAIXO — revisão narrativa (Cureus) redundante com SR/MA incluídas",
"Peng 2023 (36645990)":"BAIXO — desfecho sintomas psicóticos em TDM",
"Qaderi 2026 (41732642)":"BAIXO — revisão abrangente (Cureus) redundante",
"Rao 1989 (2497474)":"BAIXO — série pequena 1989, coberta por Fischer 2018/Hein 1990",
"Rehman 2025 (40108945)":"BAIXO — revisão narrativa redundante (adolescentes cobertos por Hirtz/Luft)",
"Sabeen 2010 (19616322)":"BAIXO — long-term care geriátrico; prevalência sem desfecho mecanístico",
"Shangguan 2022 (35728676)":"BAIXO — desfecho tentativa de suicídio (coberto por âncora Odawara; família centro único)",
"Shen 2019 (31446378)":"BAIXO — idem (suicídio em 1º episódio)",
"Song 2026 (41601507)":"BAIXO — idosos com dislipidemia, família centro único",
"Sun 2023 (37437726)":"BAIXO — mediação para sintomas psicóticos",
"Suwal 2026 (42021447)":"BAIXO — perfil lipídico como desfecho central",
"Vedal 2018 (30292780)":"BAIXO — foco em antipsicóticos (efeito iatrogênico)",
"Wang Q 2024 (38281598)":"BAIXO — mediação para sintomas psicóticos",
"Wang T 2025 (40225726)":"BAIXO — comorbidade glicêmica como estratificador central",
"Wang 2023 (36806659)":"BAIXO — sobrepeso/obesidade como estratificador central",
"Yang 2022a (35851661)":"BAIXO — família 1º episódio centro único (representada por Zhao 2023)",
"Yang 2022b (35815037)":"BAIXO — idem",
"Yang 2023 (37303557)":"BAIXO — desfecho psicótico em adolescentes",
"Yang 2024 (38699891)":"BAIXO — desfecho psicótico",
"Ye 2023 (37608074)":"BAIXO — desfecho suicídio (família centro único)",
"Zhan 2023 (37920820)":"BAIXO — TDM com dislipidemia (família centro único)",
"Zhan 2026 (41485512)":"BAIXO — desfecho NSSI adolescente",
"Zhang 2024 (38773550)":"BAIXO — risco de síndrome metabólica como desfecho",
"Zhang 2020 (32901909)":"BAIXO — efeito de antipsicóticos de 2ª geração",
"Zhu 2023 (37633524)":"BAIXO — TDM com síndrome metabólica (família centro único)",
"Aung 2024 (39046130)":"BAIXO — SCH×síndrome metabólica em psiquiátricos (desfecho metabólico)",
"Erensoy 2019 (31872808)":"BAIXO — foco primário 25(OH)D (vitamina D) com TSH covariável",
"Cui 2025 (39838463)":"BAIXO — família SCH 1º episódio (família centro único)",
"Grigorova":"BAIXO — não resolvida via eutils no insumo; candidata declarada sem PMID confirmado [G1]",
"Fountoulakis 2004 (3378493)":"BAIXO — registrada como referência primária do eixo B1 (bipolar); não âncora clínica B11",
}
EXC = {
"Telo 2016 (28358451)":"EXC — esquizofrenia (malha de escopo)",
"Jiang 2025 (39831013)":"EXC — esquizofrenia",
"Chen 2024 (39391263)":"EXC — câncer de tireoide (DTC pós-operatório)",
"Kornelius 2025 (40235655)":"EXC — nódulos/câncer de tireoide",
"Ao 2024 (37937562)":"EXC — pacientes com tumor ósseo primário (dossiê rotulava como 'TDM jovens'; divergência exposta via abstract)",
"Yu 2025 (41215684)":"EXC — transtorno por uso de álcool",
"Mattar 2025 (40641314)":"EXC — anorexia nervosa",
"Meng 2024 (39537660)":"EXC — cardiopatia coronariana (não-psiquiátrico clínico)",
"Eckert 2020 (33325120)":"EXC — população com diabetes tipo 1 (malha)",
"Kirnap 2020 (32490648)":"EXC — hipertireoidismo subclínico iatrogênico em seguimento de carcinoma diferenciado de tireoide (oncologia; divergência exposta via abstract)",
"19 revistas regionais NAO-IDX (Alanazi, Bali, Bernardes, Challa, Cieplak, Exley, Gupta, Hermann 2004, Kale, Kassaee, Mani, Moini, Morley 1982, Peng 2023-NAOIDX, Radhakrishnan, Rehman 2026, Santos, Shrestha, Swigar 1979)":"EXC — sem indexação PubMed verificável (G1 impossível); declarados, não forjados",
}
matriz={"entra":[r['id_referencia_interna']+" = "+r['pmid_oficial'] for r in R],"baixo":BAIXO,"exc":EXC,
 "exposicoes":[
  "Roca 1990 do dossiê estava mapeado ao PMID 31795239 (que é Romero-Gómez 2019) — Roca 1990 real = 2129342 (elevações transitórias); ambos ENTRAM com identidades corrigidas.",
  "'Zhang 2024' (37155921) é CORREÇÃO EDITORIAL de Soheili-Nezhad 2023 — registrada como metadado/_aliases, não como referência.",
  "Ao 2024 (37937562): dossiê rotulava 'TDM jovens'; o artigo real é em tumor ósseo primário → EXC (câncer).",
  "Eckert 2020 (33325120): população com diabetes tipo 1 → EXC pela malha.",
  "Kirnap 2020 (32490648): SCHiper iatrogênico em seguimento oncológico (DTC) → EXC pela malha.",
  "Toma 2026: a V1 sinalizava como pendente 'NTIS/desiodinase'; o artigo real (42346303) versa sobre utilidade da triagem hormonal em internados — tema corrigido na V2.",
  "'Watanave 2018' (V1) permanece SEM resolução via eutils → mantido [G1], não forjado.",
  "Grigorova e 'Roca'(PMID errado) — falsos positivos do pré-mapeamento expostos e corrigidos.",
 ]}
json.dump(R, open(BASE+'producao/insumos/b11_refs_data.json','w'), indent=1, ensure_ascii=False)
json.dump(matriz, open(BASE+'producao/insumos/matriz_b11_decisao.json','w'), indent=1, ensure_ascii=False)
print("ENTRA:",len(R),"| BAIXO len:",len(BAIXO),"| EXC grupos:",len(EXC))
ids=[r['id_referencia_interna'] for r in R]
assert len(ids)==len(set(ids)), "ids duplicados!"
print("ids ok, únicos:",len(ids))
