#!/usr/bin/env python3
# B8 — aplica rodada [AT] GPM 2026-09-09 na tríade (pmids/vínculos/ledger) + manifesto + trilha
import json

BASE='/home/user/BIBLIOTECAS/B08_Micronutrientes'
E=json.load(open(f'{BASE}/producao/insumos/b8_at_efetch.json'))
G1=json.load(open(f'{BASE}/producao/insumos/matriz_b8_g1.json'))
FONTE=lambda pm:(G1['ok'].get(pm) or G1['por_pmid'].get('Bourre, 2006') or {}).get('fonte','')
CANON=open(f'{BASE}/B8 DEFICIENCIAS DE MICRONUTRIENTES V2 CANONICA.md',encoding='utf-8').read()

# (rid, pmid, prosa, tag, bloco, n, evid_role, natureza, maturidade, desenho_curto, g2_motivo, achado, aliases_extra, especie_override, v_forca, v_verif, uso)
OB_,EC_,MA_='OB','EC','MA'
D=[
('REF_BOURRE_2006','17066209','Bourre 2006',OB_,'BLOCO01',1,'review','contributiva','bem_suportado',
 'revisão de referência (Parte 1: micronutrientes)','revisão histórica dos requisitos de micronutrientes para o cérebro; âncora do escopo',
 'Atualização clássica: vitaminas e minerais exercem funções específicas e insubstituíveis na estrutura e no funcionamento do sistema nervoso.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_EYLES_2013','22796576','Eyles 2013',OB_,'BLOCO01',12,'review','contributiva','bem_suportado',
 'revisão de neurobiologia','master GPM — vitamina D desenvolvimento/função cerebral',
 'A vitamina D atua no desenvolvimento cerebral e na função do cérebro adulto; níveis baixos ligam-se a doença neuropsiquiátrica (associação).',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_DU_2016','25365455','Du 2016',OB_,'BLOCO01',10,'review','contributiva','bem_suportado',
 'revisão','master GPM — nutrientes protegem mitocôndria/neurotransmissão; TEPT fora do escopo nominal',
 'Nutrientes protegem a função mitocondrial e a sinalização de neurotransmissores; implicações para depressão e comportamento suicida (revisão; o braço TEPT é externo ao escopo desta biblioteca).',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_KENNEDY_2016','26828517','Kennedy 2016',OB_,'BLOCO01',7,'review','contributiva','bem_suportado',
 'revisão de referência','master GPM — complexo B e cérebro: mecanismos',
 'Revisão de referência dos mecanismos, níveis de exposição e eficácia das vitaminas do complexo B no cérebro.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_FIRTH_SUPL_2017','28202095','Firth 2017',MA_,'BLOCO06',32,'human_experimental','contributiva','moderado_suportado',
 'revisão sistemática e meta-análise','master GPM — suplementação vit/mineral em esquizofrenia (fronteira ilustrativa)',
 'SR/MA: suplementação vitamínica/mineral como adjuvante em esquizofrenia mostra sinais modestos — janela de método (intervenção em psicose), não escopo causal B8.',[],None,'tier_2_meta_analise','verificado',''),
('REF_FIRTH_FEP_2018','29206972','Firth 2018',MA_,'BLOCO06',33,'human_clinical','contributiva','bem_suportado',
 'revisão sistemática e meta-análise','master GPM — deficiências no primeiro episódio psicótico (status)',
 'MA: deficiências nutricionais são prevalentes no primeiro episódio psicótico e associam-se a piores correlatos clínicos (status, não intervenção; fronteira ilustrativa).',[],None,'tier_2_meta_analise','verificado',''),
('REF_BARKS_2019','30341413','Barks 2019',OB_,'BLOCO02',25,'review','contributiva','bem_suportado',
 'revisão','master GPM — ferro como nutriente-modelo neuropsiquiátrico',
 'O ferro é o nutriente-modelo para estudar as origens nutricionais das doenças neuropsiquiátricas: a deficiência precoce reprograma o desenvolvimento cerebral.',['BARKS A','Barks A'],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_MATTEI_2019','30953290','Mattei 2019',OB_,'BLOCO02',29,'review','contributiva','bem_suportado',
 'revisão','resgate — briefing fundiu indevidamente com McWilliams 2022 (erro exposto)',
 'Micronutrientes são necessários ao desenvolvimento cerebral; deficiências na janela crítica comprometem trajetórias neurodesenvolvimentais.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_MOORE_2019','30692033','Moore 2019',EC_,'BLOCO01',5,'human_clinical','associativa','incipiente',
 'coorte transversal (TUDA)','idosos >60; associação status B×depressão (transversal)',
 'Na coorte TUDA, status bioquímico baixo de vitaminas do complexo B associou-se a maior risco de depressão em idosos — associação transversal, sem prova intervencional.',[],None,'tier_4_observacional_transversal','verificado',''),
('REF_WESSELINK_2019','30201141','Wesselink 2019',OB_,'BLOCO08',41,'review','contributiva','moderado_suportado',
 'revisão','master GPM — cofatores nutricionais mitocondriais (ponte B9)',
 'Componentes nutricionais podem nutrir a função mitocondrial na convalescença de doença crítica — "feeding mitochondria" (ponte B9).',[],['Humans','Animals'],'tier_4_descritivo_estrutural','verificado',''),
('REF_PLEVIN_2020','32552785','Plevin 2020',OB_,'BLOCO12',49,'review','refutadora','bem_suportado',
 'revisão sistemática','master GPM — bloco NEG vitamina C (associação sem prova intervencional)',
 'SR: a deficiência de vitamina C associa-se a efeitos neuropsiquiátricos, MAS não há estudos de desfecho adequados demonstrando efeito da reposição (lacuna intervencional explícita).',[],None,'tier_2_revisao_sistematica','verificado',''),
('REF_BARKS_2021','34836113','Barks 2021',OB_,'BLOCO02',26,'review','contributiva','moderado_suportado',
 'revisão (com evidência experimental animal)','master GPM — deficiência de ferro precoce programa epigenoma hipocampal',
 'A deficiência de ferro precoce programa a paisagem epigenômica do hipocampo, com efeitos que persistem apesar da correção posterior.',['BARKS AK','Barks AK'],['Humans','Animals'],'tier_4_descritivo_estrutural','verificado',''),
('REF_CUI_2021','33500553','Cui 2021',OB_,'BLOCO01',13,'review','contributiva','bem_suportado',
 'revisão/metasíntese 20 anos','master GPM — vitamina D×esquizofrenia (fronteira ilustrativa de método)',
 'Vitamina D e esquizofrenia, 20 anos de pesquisa: associação epidemiológica consolidada, intervenção sem prova — fronteira ilustrativa, não escopo causal B8.',[],['Humans','Animals'],'tier_4_descritivo_estrutural','verificado',''),
('REF_MUSCARITOLI_2021','33763446','Muscaritoli 2021',OB_,'BLOCO01',9,'review','contributiva','moderado_suportado',
 'revisão narrativa','master GPM — nutrientes e saúde mental (MeSH pendente de indexação)',
 'Revisão do impacto dos nutrientes na saúde mental e no bem-estar a partir da literatura.',[],['Humans'],'tier_4_descritivo_estrutural','verificado',''),
('REF_RUDZKI_2021','33428888','Rudzki 2021',OB_,'BLOCO08',39,'review','contributiva','moderado_suportado',
 'revisão','master GPM — vitaminas derivadas de microbiota (ponte B7)',
 'A microbiota intestinal produz vitaminas (K e complexo B) com papel subestimado na saúde psiquiátrica e na doença mental.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_BADAR_2022','35223256','Badar 2022',EC_,'BLOCO01',4,'human_clinical','associativa','incipiente',
 'relato de caso','master GPM — B12 neuropsiquiatria como POSSIBILIDADE clínica (MeSH pendente)',
 'Relato de caso autobiográfico de transtornos neuropsiquiátricos associados à deficiência de B12 — documenta possibilidade clínica, sem valor epidemiológico (formulação protegida).',[],['Humans'],'tier_4_observacional_transversal','verificado',''),
('REF_BARONE_2022','35294077','Barone 2022',OB_,'BLOCO08',40,'review','contributiva','moderado_suportado',
 'revisão','master GPM — interação microbioma-micronutriente (ponte B7)',
 'A interação microbioma–micronutriente é bidirecional no controle da saúde cerebral.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_FERRIANI_2022','34695501','Ferriani 2022',EC_,'BLOCO01',6,'human_clinical','associativa','incipiente',
 'coorte transversal (ELSA-Brasil)','ELSA-Brasil N≈14,7 mil; ingestão ≠ deficiência (B8-CAUSAL-05)',
 'No ELSA-Brasil, maior ingestão de antioxidantes e de vitaminas do complexo B associou-se a menor depressão — associação transversal de ingestão, não de status bioquímico.',[],None,'tier_4_observacional_transversal','verificado',''),
('REF_MCWILLIAMS_2022','36173945','McWilliams 2022',OB_,'BLOCO02',27,'review','contributiva','moderado_suportado',
 'revisão de escopo','fronteira neurodesenvolvimental ilustrativa (TDAH/TEA fora do escopo)',
 'Scoping review: a deficiência de ferro associa-se a transtornos comuns do neurodesenvolvimento — evidência de que a janela crítica do ferro existe (fronteira ilustrativa).',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_SAHU_2022','35337631','Sahu 2022',OB_,'BLOCO01',2,'review','contributiva','moderado_suportado',
 'revisão (Vitam Horm)','master GPM — manifestações neuropsiquiátricas da deficiência de B12',
 'Revisão das manifestações neuropsiquiátricas da deficiência de vitamina B12 — os sintomas podem preceder a anemia.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_SHAYGANFARD_2022','33904124','Shayganfard 2022',OB_,'BLOCO02',22,'review','contributiva','moderado_suportado',
 'revisão','master GPM — oligoelementos essenciais e transtornos mentais',
 'Revisão sobre o papel de oligoelementos essenciais (Zn, Mg, Se, Fe) na modulação de transtornos mentais.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_FIANI_2023','37147046','Fiani 2023',OB_,'BLOCO02',28,'review','contributiva','moderado_suportado',
 'revisão clínica','fronteira neurodesenvolvimental ilustrativa (TDAH/TEA fora do escopo)',
 'Revisão clínica: a deficiência de ferro no TDAH e em condições do neurodesenvolvimento — fronteira ilustrativa da janela crítica.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_LAHODABRODSKA_2023','37836413','Lahoda Brodska 2023',OB_,'BLOCO01',11,'review','contributiva','moderado_suportado',
 'revisão','fronteira ilustrativa (transtornos neurológicos; sem extrapolação de mecanismo)',
 'Revisão do papel dos micronutrientes em transtornos neurológicos — aproveitamento seletivo da mecânica de micronutrientes (fronteira ilustrativa).',['LAHODA','Lahoda','LAHODA BRODSKA','Lahoda Brodska','LAHODABRODSKA','Lahodabrodska'],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_NOGUEIRA_2023','36411563','Nogueira-de-Almeida 2023',OB_,'BLOCO01',8,'review','contributiva','moderado_suportado',
 'revisão sistemática','master GPM — neuronutrientes e SNC',
 'SR: neuronutrientes e o sistema nervoso central — catálogo ampliado de nutrientes com papel neural.',['NOGUEIRA','Nogueira','NOGUEIRA-DE-ALMEIDA','Nogueira-de-Almeida','NOGUEIRADEALMEIDA','Nogueiradealmeida'],None,'tier_2_revisao_sistematica','verificado',''),
('REF_ALJASSEM_2024','38630748','Al Jassem 2024',EC_,'BLOCO02',17,'human_clinical','associativa','incipiente',
 'estudo transversal','B12×sintomas neuropsiquiátricos (Líbano)',
 'Estudo transversal no Líbano: a deficiência de B12 associou-se a sintomas neuropsiquiátricos — associação, sem demonstrar precedência (B8-CAUSAL-02).',['AL JASSEM','Al Jassem','ALJASSEM','Aljassem','AlJassem'],None,'tier_4_observacional_transversal','verificado',''),
('REF_BERGER_2024','38462972','Berger 2024',OB_,'BLOCO11',47,'review','contributiva','moderado_suportado',
 'revisão de opinião','master GPM — deficiência e suplementos em escolares/adolescentes',
 'Revisão de opinião: deficiência de micronutrientes e suplementação em escolares e adolescentes.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_HUI_2024','38999789','Hui 2024',EC_,'BLOCO07',36,'human_clinical','associativa','incipiente',
 'revisão sistemática de associações genéticas (SNP)/MR','MR = associação instrumental genética; ≠ eficácia de suplementação (B8-CAUSAL-03)',
 'Polimorfismos de nucleotídeo único associados a micronutrientes mapeiam padrões distintos de relação com transtornos mentais, por par nutriente×transtorno.',[],None,'tier_4_observacional_transversal','emergente',''),
('REF_MATHEW_2024','38203763','Mathew 2024',OB_,'BLOCO01',3,'review','contributiva','moderado_suportado',
 'revisão','master GPM — B12 além da decomposição metabólica',
 'Revisão: a deficiência de B12 e o sistema nervoso além da decomposição metabólica.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_RAJASEKAR_2024','38605872','Rajasekar 2024',EC_,'BLOCO06',35,'human_clinical','associativa','incipiente',
 'estudo observacional','ingestão+suplementação combinadas × saúde mental',
 'Ingestão dietética combinada à suplementação de vitamina D, B6 e magnésio associou-se a melhor saúde mental (observacional).',[],None,'tier_4_observacional_transversal','emergente',''),
('REF_SCUTO_2024','39596221','Scuto 2024',OB_,'BLOCO08',43,'review','contributiva','moderado_suportado',
 'revisão','master GPM — nutrientes funcionais, resiliência redox e neuroesteroides (pontes B6/B3)',
 'Revisão: nutrientes funcionais, sinalização de resiliência redox e neuroesteroides na saúde cerebral.',[],['Humans','Animals'],'tier_4_descritivo_estrutural','verificado',''),
('REF_ANMELLA_2025','40100400','Anmella 2025',EC_,'BLOCO11',46,'human_clinical','associativa','incipiente',
 'série clínica transversal (N=729 internados jovens)','B12 insuficiente×transtorno depressivo em jovens',
 'Em 729 internados psiquiátricos crianças/adolescentes, folato insuficiente em 42,9% e B12 em 19,4%; B12 insuficiente associou-se a transtornos depressivos (e B12 baixa ao espectro da esquizofrenia — fronteira).',[],None,'tier_4_observacional_transversal','verificado',''),
('REF_ASTORINO_2025','40653891','Astorino 2025',OB_,'BLOCO02',23,'review','contributiva','moderado_suportado',
 'revisão','master GPM — etiologia multifacetada e elementos-traço',
 'Revisão: a etiologia multifacetada dos transtornos mentais, com foco em elementos-traço.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_DOMANSKI_2025','40289952','Domański 2025',EC_,'BLOCO05',30,'human_clinical','associativa','incipiente',
 'estudo clínico observacional','correlações hematológicas como preditores',
 'Correlações hematológicas avaliadas como preditores de manifestações em transtornos mentais (janela de mensuração, não biomarcador de humor).',['DOMANSKI','Domanski','DOMAŃSKI','Domański'],None,'tier_4_observacional_transversal','emergente',''),
('REF_FAA_2025','41303365','Faa 2025',OB_,'BLOCO02',24,'review','contributiva','moderado_suportado',
 'revisão','master GPM — homeostase do zinco e início de transtornos',
 'Revisão: perturbações da homeostase do zinco no início de transtornos neuropsiquiátricos.',[],['Humans','Animals'],'tier_4_descritivo_estrutural','verificado',''),
('REF_FAUGERE_2025','40218925','Faugere 2025',EC_,'BLOCO02',16,'human_clinical','associativa','incipiente',
 'estudo clínico transversal','D, B9, B12 × gravidade clínica psiquiátrica',
 'Deficiências combinadas de vitamina D, B9 e B12 associaram-se à gravidade clínica em pacientes psiquiátricos (associativo).',[],None,'tier_4_observacional_transversal','verificado',''),
('REF_HORSDAL_2025','40379361','Horsdal 2025',EC_,'BLOCO02',19,'human_clinical','associativa','moderado_suportado',
 'caso-coorte de base populacional (iPSYCH2012)','SIGNIFICATIVO p/ esquizofrenia/TEA/TDAH, NULO p/ TDM (n≈24 mil) — NEG no desfecho-âncora',
 '25(OH)D e DBP neonatais associaram-se inversamente a esquizofrenia, TEA e TDAH — sem associação significativa para a TDM (n≈24 mil casos); MR interno sugestivo apenas para TDAH. Fronteira ilustrativa com resultado nulo no desfecho-âncora desta biblioteca.',[],None,'tier_4_observacional_transversal','verificado',''),
('REF_ISLAM_2025','41228551','Islam 2025',OB_,'BLOCO11',45,'review','contributiva','moderado_suportado',
 'revisão sistemática','micronutrientes × depressão perinatal',
 'SR: correlações entre níveis de micronutrientes e depressão no período perinatal.',[],None,'tier_2_revisao_sistematica','verificado',''),
('REF_KOHL_2025','41515142','Kohl 2025',EC_,'BLOCO02',18,'human_clinical','associativa','incipiente',
 'estudo transversal (mulheres)','vitamina D × transtornos mentais comuns',
 'Em mulheres, deficiência/insuficiência de vitamina D associou-se a transtornos mentais comuns (transversal).',[],None,'tier_4_observacional_transversal','verificado',''),
('REF_LU_2025','40739033','Lu 2025',EC_,'BLOCO07',37,'human_clinical','associativa','incipiente',
 'randomização mendeliana','MR: efeitos de B12 sérica × transtornos psiquiátricos; ≠ eficácia (B8-CAUSAL-03) (MeSH pendente)',
 'MR: os efeitos estimados dos níveis séricos de B12 sobre transtornos psiquiátricos variam por desfecho — associação instrumental genética, não prova de suplementação.',[],['Humans'],'tier_4_observacional_transversal','emergente',''),
('REF_RADOEVA_2025','40329546','Radoeva 2025',EC_,'BLOCO05',31,'human_clinical','associativa','incipiente',
 'estudo observacional (coorte ABCD)','ingestão estimada × problemas psiquiátricos/sono em juventude com TEA (fronteira ilustrativa; B8-CAUSAL-05)',
 'Na juventude com TEA da coorte ABCD, a ingestão estimada de nutrientes associou-se a problemas psiquiátricos e de sono — ilustra que proxy de ingestão não é biomarcador de deficiência (fronteira ilustrativa; TEA fora do escopo).',[],None,'tier_4_observacional_transversal','emergente',''),
('REF_RAJEN_2025','39829265','Rajen 2025',EC_,'BLOCO02',15,'human_clinical','associativa','incipiente',
 'amostra clínica transversal','status de folato em transtornos mentais',
 'Status de folato prejudicado em pacientes com transtornos mentais (amostra clínica; associativo).',[],None,'tier_4_observacional_transversal','verificado',''),
('REF_RUCKLIDGE_2025','39703999','Rucklidge 2025',OB_,'BLOCO11',48,'review','contributiva','bem_suportado',
 'Annual Research Review','master GPM — micronutrientes no tratamento pediátrico',
 'Annual Research Review: o papel dos micronutrientes no tratamento das doenças mentais pediátricas.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_SKOCZEK_2025','40871684','Skoczek-Rubińska 2025',OB_,'BLOCO02',20,'review','contributiva','moderado_suportado',
 'revisão estruturada','master GPM — vitamina D status/suplementação × BDNF e humor-cognição',
 'Revisão estruturada: o impacto do status e da suplementação de vitamina D sobre BDNF e desfechos de humor-cognição é inconsistente.',['SKOCZEK','Skoczek','SKOCZEK-RUBIŃSKA','Skoczek-Rubińska','SKOCZEKRUBINSKA','Skoczekrubinska'],['Humans','Animals'],'tier_4_descritivo_estrutural','verificado',''),
('REF_YE_2025','39952338','Ye 2025',MA_,'BLOCO07',38,'human_clinical','contributiva','moderado_suportado',
 'revisão sistemática e meta-análise','master GPM — causalidade vitaminas B × neuropsiquiatria: distinta por par',
 'SR/MA: a relação causal entre vitaminas do complexo B e transtornos neuropsiquiátricos é distinta por par vitamina×transtorno — não há efeito geral do "complexo B".',[],None,'tier_2_meta_analise','verificado',''),
('REF_ALEXA_2026','42029584','Alexa 2026',OB_,'BLOCO11',44,'review','contributiva','moderado_suportado',
 'revisão narrativa','master GPM — paradoxo nutricional da obesidade',
 'Revisão: o paradoxo nutricional da obesidade — excesso calórico coexistindo com deficiências de micronutrientes, com implicações clínicas.',[],None,'tier_4_descritivo_estrutural','verificado',''),
('REF_MOROIANU_2026','42187879','Moroianu 2026',MA_,'BLOCO02',21,'human_clinical','refutadora','moderado_suportado',
 'revisão sistemática + meta-análise exploratória (PRISMA 2020)','master GPM — bloco NEG vitamina D (eficácia não demonstrada) (MeSH pendente)',
 'SR/MA exploratória de vitamina D e B12 em transtornos psiquiátricos: os sinais inversos iniciais colapsam ao nulo após correção de viés de publicação (trim-and-fill OR 0,88; IC95% 0,48–1,63 para suplementação de D); suplementação de B12 esparsa e nula — apoia avaliação direcionada de deficiência, não suplementação de rotina.',[],['Humans'],'tier_2_meta_analise','verificado',''),
('REF_SHAHINI_2026','42144425','Shahini 2026',EC_,'BLOCO08',42,'human_clinical','associativa','incipiente',
 'estudo caso-controle','master GPM — interações micronutriente-imunes (ponte B1)',
 'Caso-controle: interações micronutriente-imunes (vitamina C, ferro, zinco, magnésio e índices celulares periféricos) em transtornos de humor e psicóticos.',[],None,'tier_4_observacional_transversal','verificado',''),
('REF_TORTAJADA_2026','42253799','Tortajada 2026',OB_,'BLOCO06',34,'review','contributiva','moderado_suportado',
 'revisão sistemática','master GPM — suplementação pró-mitocondrial em psiquiatria (ponte B9) (MeSH pendente)',
 'SR: desfechos clínicos de suplementação com nutracêuticos voltados à função mitocondrial em transtornos psiquiátricos — campo heterogêneo, estudos pequenos.',[],['Humans'],'tier_2_revisao_sistematica','verificado',''),
('REF_YANG_2026','42044701','Yang 2026',OB_,'BLOCO01',14,'review','contributiva','emergente',
 'revisão mecanicista','hipótese complemento-sinapse/VDBP-megalin; sem lastro intervencional',
 'Revisão mecanicista: a deficiência de vitamina D tocaria a depressão por remodelamento sináptico mediado por complemento e sinalização VDBP-megalin — hipótese, sem lastro intervencional.',[],['Humans','Animals'],'tier_4_descritivo_estrutural','emergente',''),
]
assert len(D)==49 and len({d[0] for d in D})==49 and len({d[1] for d in D})==49

def trecho_para(cit):
    """retorna trecho único da V2 contendo a citação literal"""
    idxs=[]; start=0
    while True:
        i=CANON.find(cit,start)
        if i<0: break
        idxs.append(i); start=i+1
    assert idxs, cit
    for i in idxs:
        l=CANON.rfind('\n',0,i-1); l2=CANON.rfind('\n',0,l-1) if l>0 else -1
        a=max(0,l2+1); b=CANON.find('\n',i+len(cit)); b=len(CANON) if b<0 else b
        trecho=CANON[a:b].strip()
        assert cit in trecho
        if CANON.count(trecho)==1: return trecho
    # fallback: parágrafo inteiro da 1a ocorrência
    i=idxs[0]; a=CANON.rfind('\n\n',0,i)+2; b=CANON.find('\n\n',i)
    trecho=CANON[a:len(CANON) if b<0 else b].strip()
    assert CANON.count(trecho)==1,(cit,'fallback')
    return trecho

G2_STATUS='eligible'
pmids_new=[]; vincs_new=[]; leds_new=[]
for (rid,pmid,prosa,tag,bloco,nn,erole,nat,mat,desenho,g2m,achado,alx,esp_ov,vfc,vverif,uso) in D:
    e=E[pmid]; ano=e['ano_print']; fonte=FONTE(pmid) or e['iso']
    esp=e['especie_mesh'] or esp_ov or []
    claim=f'B8.MEC.{bloco}.{nn:03d}'
    autores=e['autores'] if e['autores'] else ['?']
    a1=autores[0].split()[0].replace('-','').replace('ü','u')
    aliases=[a1.upper(),a1]+alx
    if e['especie_mesh']==['Humans'] or erole in ('human_clinical','human_experimental') and 'Animals' not in esp:
        extrap='não'
    elif 'Animals' in esp:
        extrap='parcial — revisão mistura espécies'
    else:
        extrap='não'
    cit=f'({prosa})[{tag}]'
    assert CANON.count(cit)>=1,('cit ausente',cit)
    trecho=trecho_para(cit)
    mesh_note='; MeSH pendente de indexação (espécie inferida por título/abstract)' if not e['mesh'] else ''
    desenho_full=f'[{tag}] {desenho} · {fonte}'
    pmids_new.append({
     'pmid_oficial':pmid,'titulo_artigo':e['titulo'],'autores':autores,
     'revista_ano':f'{fonte} ({ano})','desenho_estudo':desenho_full,
     'secao_origem':'mecanismo_B8_deficiencias_micronutrientes',
     'achado_central_molecular':achado,
     'extrapolacao_por_analogia':extrap,
     'ids_referencia_interna':[rid],'evid_role':erole,'especie_mesh':esp,
     'verification_status':vverif if vverif!='verificado' else 'emergente' if mat in('incipiente','emergente') else 'emergente',
     'citacao_confirmada':True,'g1_metodo':'eutils_automatico',
     'g2_elegibilidade':G2_STATUS,'g2_motivo':g2m,
     'g3_verificado_por':f'IA G3 (Rodada [AT] GPM B8 2026-09-09): esearch DOI[aid] + esummary + efetch; abstract lido ref a ref{mesh_note}; 2a verificação independente (P-6) pendente',
     'status_auditoria':'CONFIRMADO','origem_pipeline':'GPM_RODADA_AT',
     'id_referencia_interna':rid,'doi':e['doi'],'claim_id_origem':claim,'_aliases':aliases})
    lfc='tier_2_necessidade_ou_suficiencia' if False else 'tier_4_descritivo_estrutural'
    vincs_new.append({
     'id_vinculo':f'VINC_B8_{34+len(vincs_new)+1:03d}','id_referencia_interna':rid,'secao_origem':'B8_CANONICA_V2',
     'trecho_ancora':trecho,'mecanismo_origem':'mecanismo_B8_deficiencias_micronutrientes',
     'natureza_relacao':nat,'grau_maturidade':mat,'forca_causal':vfc,
     'extrapolacao_por_analogia':extrap,'especie_mesh':esp,'evid_role':erole,
     'verification_status':vverif,'status_referencia':'CONFIRMADA',
     'citacao_confirmada':True,'g1_metodo':'eutils_automatico','g2_elegibilidade':G2_STATUS,'g2_motivo':g2m,
     'g3_verificado_por':f'IA G3 (Rodada [AT] GPM B8 2026-09-09): eutils esearch DOI[aid] + esummary + efetch; abstract lido ref a ref{mesh_note}',
     'g3_fulltext':'abstract lido; PMC full-text fica para 2a verificação independente (P-6, avaliador cego)',
     'status_auditoria':'CONFIRMADO','uso':uso,
     'segunda_verificacao':'PENDENTE — 2a verificação independente (P-6, avaliador cego) registrada como pendência de fase; mitigação: tier/espécie explícitos, selos honestos [OB]/[EC]/[MA], fronteiras ilustrativas sinalizadas, regras B8-CAUSAL fixadas',
     'data_verificacao':'2026-09-09','pmid_oficial':pmid})
    leds_new.append({
     'id_auditoria':f'AUD_B8_{38+len(leds_new)+1:04d}','mecanismo':'B8','id_referencia_interna':rid,'pmid_oficial':pmid,
     'arquivo_modulo09':'Evidencias/Bibliografia/01_pmids.json','tipo_classificador':'','origem_entrada':'GPM',
     'claim_id':claim,'secao_origem':'B8_CANONICA_V2','trecho_ancora':trecho,
     'citacao_literal':cit,'natureza_da_relacao':nat,'grau_maturidade_cientifica':mat,'forca_causal':lfc,
     'forca_biologica_conexao':'','especie_mesh':esp,'evid_role':erole,
     'portao_G1_existencia':'VERIFIED_REFERENCE','portao_G2_elegibilidade':'ELIGIBLE_SOURCE',
     'portao_G3_suporte':'APROVADO','status_auditoria':'APROVADO','destino':'FICA_MECANISMO','acao_correcao':'ACRESCENTAR',
     'reconciliado':True,
     'verificacao':{'verificador':'IA G3 Rodada [AT] GPM B8 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente',
      'data_verificacao':'2026-09-09','g1_metodo':'eutils_automatico',
      'abstract_ou_trecho':'abstract efetch lido nesta rodada; trecho-âncora inserido na canônica V2',
      'query_utilizada':'esearch PubMed DOI[aid]' + (' / busca dirigida autor+ano (sem DOI no anexo)' if pmid=='17066209' else ''),
      'g2_motivo':g2m,'g3_nota':'integridade referencial + formulação protegida (regras B8-CAUSAL; fronteiras ilustrativas sinalizadas).'}})

pj=f'{BASE}/Evidencias/Bibliografia/01_pmids.json'
vj=f'{BASE}/Evidencias/Vinculos/vinculos_referencia_afirmacao.json'
lj=f'{BASE}/Auditoria_B8/ledger_auditoria_B8.json'
pjx=json.load(open(pj)); vjx=json.load(open(vj)); ljx=json.load(open(lj))
old_p,old_v,old_l=len(pjx),len(vjx),len(ljx)
pjx+=pmids_new; vjx+=vincs_new; ljx+=leds_new
assert (len(pjx),len(vjx),len(ljx))==(145,83,87), (len(pjx),len(vjx),len(ljx))
ids=[e['id_referencia_interna'] for e in pjx]
assert len(set(ids))==145,'id duplicado'
for v in vincs_new: assert CANON.count(v['trecho_ancora'])==1, v['id_vinculo']
json.dump(pjx,open(pj,'w'),ensure_ascii=False,indent=1)
json.dump(vjx,open(vj,'w'),ensure_ascii=False,indent=1)
json.dump(ljx,open(lj,'w'),ensure_ascii=False,indent=1)

# manifesto
mj=f'{BASE}/Evidencias/Bibliografia/_manifesto_biblioteca.json'
man=json.load(open(mj))
man['artefato_rotulo']='CANONICA v2'
man['rodada']=4
man['data_corte']='2026-09-09'
man['pmids_total']=145
man['g1']['resolvidos']=145
man['g1']['descartados_auditoria'].append('rodada [AT] GPM 2026-09-09: 9 NÃO-INDEXADOS confirmados fora (Barakat; Chambers; Fedulova; Jayashree; Júnior; Kim; Lubis; Medford; Wróblewska) + 12 EXC por malha de escopo (autismo ×5, neurodegeneração ×2, anorexia, epilepsia, delirium, botânica, demência/AVC) — sem fonte forjada; 7 erros factuais do briefing externo revertidos (ver decisoes_B8.md)')
g2=man['g2']
g2['eligible']=g2['eligible']+49
er=g2['evid_role']
er['human_clinical']=er.get('human_clinical',0)+24
er['review']=er.get('review',0)+24
er['human_experimental']=er.get('human_experimental',0)+1
man['g3']['vinculos_n2']=83
man['g3']['CONFIRMADO']=26+49
man['g3']['abstracts_lidos_alto_risco']=man['g3'].get('abstracts_lidos_alto_risco',11)+49
man['vinculos_n2']=83
man['palavras_canonica']=10007
man['versao']='2.6'
man['corte_literatura']='busca ativa com ferramenta externa E-utilities/PubMed; corte 2026-09-09'
man['pendencias_fase']=[
 'P-6: 2a verificação independente (avaliador cego) dos claims de alto risco (VITAL, MR Carnegie/Hui/Lu/Ye, metas D/Mg/Se, Moroianu, Horsdal) — AMPLIADA na rodada [AT] 2026-09-09: incluir as levas [AT] de TODAS as bibliotecas B1–B16 ao fim da rodada (16/16)']
man['historico_correcoes'].append({
 'data':'2026-09-09','campo':'rodada_AT_GPM_B8',
 'erro_anterior':'V1 (96 refs) sem a leva auditada do insumo externo GPM B8 (anexo 106 refs reais — o briefing dizia "98")',
 'correcao':'auditoria ref a ref (G1 eutils 96/105 DOIs + Bourre sem DOI resgatado por busca dirigida; 0 falso positivo; 9 não-indexados confirmados; 6 sobreposições com a V1); matriz de decisão 49 ENTRA/30 BAIXO/12 EXC; 7 erros factuais do briefing revertidos (Mattei≠McWilliams; Yoon; Dehesh; Cortés-Albornoz; Das; Bourre NAO-IDX refutado; Wang 2018 já vigente); fusão V2 com 145 refs; regras B8-CAUSAL-01..10 fixadas em CONTROVÉRSIAS; blocos NEG (vit C — Plevin; vit D — Moroianu); Horsdal 2025 nulo para TDM; tríade sincronizada (pmids 145, vínculos 83, ledger 87)',
 'acao_downstream':'portões oficiais revalidados (gate P-5, framework auditoria, checklist); P-4 adendo V2; P-6 mantido pendente'})
json.dump(man,open(mj,'w'),ensure_ascii=False,indent=1)

# trilha
trilha={'ciclo':'[AT] GPM B8 — Deficiências de Micronutrientes','data':'2026-09-09','artefato':'CANONICA v2 (145 refs; de 96)',
 'insumos':['GPM_B8_Micronutrientes (2).md (oficial, molde v2.0)','BRIEFING_B8_MICRONUTRIENTES_RODADA0.md','BRIEFING_CONSOLIDADO_B8_v1.md','Artigos cientificos do mecanismo B8 (anexo: 106 entradas reais — briefing dizia 98)','Resumo do insumo para B8 Chatgpt.md (50 claims B8.SM02 + 10 regras B8-Causal + bloco NEG)'],
 'auditoria':{'anexo_itens':106,'dois_lotes_g1':105,'g1_resolvidos':96,'sem_doi_resgatados':['Bourre 2006 (17066209 — busca dirigida; briefing dizia NAO-IDX)'],
  'nao_indexados':['Barakat','Chambers','Fedulova','Jayashree','Júnior','Kim','Lubis','Medford','Wróblewska'],
  'falsos_positivos':0,'sobreposicao_com_V1':6,'masters_gpm':{'total':41,'ja_vigentes':0,'novas':41},
  'fila_decisao':91,'entra':49,'baixo':30,'exc':12,
  'erros_briefing_revertidos':['"Mattei 2019 = McWilliams 2022" (Mattei real = 30953290)','"Yoon 2026 = Zielińska 2023" (Yoon real = 42514375)','"Dehesh 2026 = Domański 2025" (Dehesh real = 42605394)','"Cortés-Albornoz 2021 não localizada" (= 34684531)','"Das 2025 não localizada" (= 41064635)','"Bourre 2006 NAO-IDX" (= 17066209, artigo-âncora Parte 1)','"Wang 2018 sem PMID" (já vigente REF_WANG_2018 = 29747386)']},
 'regras_fixadas':['B8-CAUSAL-01','B8-CAUSAL-02','B8-CAUSAL-03','B8-CAUSAL-04','B8-CAUSAL-05','B8-CAUSAL-06','B8-CAUSAL-07','B8-CAUSAL-08','B8-CAUSAL-09','B8-CAUSAL-10'],
 'blocos_neg':['vitamina C — associação sem prova intervencional (Plevin 2020)','vitamina D — eficácia antidepressiva não demonstrada (Moroianu 2026); avaliação direcionada, não universal','Horsdal 2025 — nulo para TDM'],
 'artefatos':['producao/insumos/RELATORIO_AUDITORIA_MATRIZ_B8.md','producao/insumos/matriz_b8_decisao.json','producao/insumos/matriz_b8_g1.json','producao/insumos/b8_anexo_entries.json','producao/insumos/b8_cruzamento.json','producao/insumos/b8_at_efetch.json','producao/insumos/b8_trechos_ancora.json'],
 'pendencias':['P-6 (2ª verificação cega, Via 2) — PENDENTE ao fim da rodada 16/16, cobrindo todas as levas [AT]']}
json.dump(trilha,open(f'{BASE}/producao/04_AT_ciclo_2026-09-09.json','w'),ensure_ascii=False,indent=1)
print('TRÍADE OK: pmids',old_p,'→',len(pjx),'| vínculos',old_v,'→',len(vjx),'| ledger',old_l,'→',len(ljx))
print('manifesto v2 gravado; trilha gravada')
