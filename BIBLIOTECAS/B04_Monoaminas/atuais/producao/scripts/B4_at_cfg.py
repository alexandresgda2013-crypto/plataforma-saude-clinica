import json, re, html
D=json.load(open('/home/user/BIBLIOTECAS/B04_Monoaminas/producao/insumos/matriz_b4_decisao.json'))
FULL=json.load(open('/home/user/BIBLIOTECAS/B04_Monoaminas/producao/insumos/matriz_b4_g1_full.json'))
ABS={}
for e in FULL:
    if e.get('resolved'):
        ABS[e['pmid']]=e.get('abstract','') or ''
VIG=set(D['VIG'])
ENTRA=D['ENTRA_ESQ']+D['ENTRA_CRA']+D['ENTRA_C1']+D['ENTRA_C2']+D['ENTRA_C3']+D['ENTRA_C4']+D['ENTRA_C5']
# ---- mapa: pmid -> (key1, key2, key3, label, tag, nivel, evid_role, bloco, secao) ----
M = {
 # HIST (BLOCO_01 / 1.4)
 '12953623':('Baumeister','AA','2003','Baumeister_2003','OB','CORE','REF','BLOCO_01','1.4'),
 '36000248':('Strawbridge','R','2019','Strawbridge_2019','OB','CORE','REF','BLOCO_01','1.4'),
 '26043325':('Cowen','PJ','2015','Cowen_2015','OB','CORE','REF','BLOCO_01','1.4'),
 '37857415':('Albert','PR','2023','Albert_Blier_2023','OB','CORE','REF','BLOCO_01','1.4'),
 '19428959':('Savitz','JB','2009','Savitz_2009','OB','SUPPORT','REF','BLOCO_01','1.4'),
 '38816586':('Fakhoury','MA','2024','Fakhoury_2024','OB','CORE','REF','BLOCO_01','1.4'),
 '4863731':('Schildkraut','JJ','1967','Schildkraut_1967','OB','CORE','REF','BLOCO_01','1.4'),
 '8852528':('Heninger','GR','1996','Heninger_1996','OB','CORE','REF','BLOCO_01','1.4'),
 '9818625':('Charney','DS','1998','Charney_1998','OB','CORE','REF','BLOCO_01','1.4'),
 '10775017':('Hirschfeld','RM','2000','Hirschfeld_2000','OB','CORE','REF','BLOCO_01','1.4'),
 '10775019':('Leonard','BE','2000','Leonard_2000','OB','CORE','REF','BLOCO_01','1.4'),
 '7899535':('Meltzer','HY','1995','Meltzer_1995','OB','SUPPORT','REF','BLOCO_01','1.4'),
 '19498050':('Owens','MJ','2009','Owens_Nemeroff_2009','OB','SUPPORT','REF','BLOCO_01','1.4'),
 # 5HT (BLOCO_02 / 2.1)
 '16154547':('Parsey','RV','2006','Parsey_2006','EC','CORE','SUP','BLOCO_02','2.1'),
 '17971260':('Kaufman','J','2006','Kaufman_2006','EC','CORE','SUP','BLOCO_02','2.1'),
 '24936175':('Zhang','K','2014','Zhang_2014','EC','SUPPORT','SUP','BLOCO_02','2.1'),
 '24337875':('Andrews','PW','2015','Andrews_2015','OB','CORE','MEC','BLOCO_02','2.1'),
 '19423077':('Erritzoe','D','2009','Erritzoe_2009','EC','CORE','SUP','BLOCO_02','2.1'),
 '23492554':('Eshel','N','2013','Eshel_2013','ML','SUPPORT','MEC','BLOCO_02','2.1'),
 '28232871':('Phillips','JL','2017','PhillipsL_2017','OB','SUPPORT','REF','BLOCO_02','2.1'),
 '27353308':('Takano','A','2014','Takano_2014','EC','SUPPORT','SUP','BLOCO_02','2.1'),
 '33651238':('Ruf','BM','2021','Ruf_2021','ML','SUPPORT','MEC','BLOCO_02','2.1'),
 '33673205':('Gjerris','A','2021','Gjerris_2021','ML','SUPPORT','MEC','BLOCO_02','2.1'),
 '33672070':('Mariani','N','2021','Mariani_2021','MA','CORE','SUP','BLOCO_02','2.1'),
 '9844013':('Miller','HL','1998','Miller_1998','OB','SUPPORT','REF','BLOCO_02','2.1'),
 '31120232':('Vicens','J','2019','Vicens_2019','ML','SUPPORT','MEC','BLOCO_02','2.1'),
 '30144453':('Meyer','JH','2018','MeyerJ_2018','MA','CORE','SUP','BLOCO_02','2.1'),
 '22832966':('Nogami','S','2012','Nogami_2012','EC','SUPPORT','SUP','BLOCO_02','2.1'),
 '26083190':('Katrinli','S','2015','Katrinli_2015','OB','SUPPORT','REF','BLOCO_02','2.1'),
 '28920103':('Karalic','AS','2017','Karalic_2017','OB','SUPPORT','REF','BLOCO_02','2.1'),
 '25823514':('Beltz','AM','2015','Beltz_2015','EC','SUPPORT','SUP','BLOCO_02','2.1'),
 '27623971':('Wang','L','2016','Wang_2016','MA','CORE','SUP','BLOCO_02','2.1'),
 # DEPL (BLOCO_02 / 2.3)
 '11331552':('Bell','C','2001','Bell_2001','OB','CORE','REF','BLOCO_02','2.3'),
 '11063917':('Moore','P','2000','Moore_2000','OB','CORE','REF','BLOCO_02','2.3'),
 '12431859':('Booij','L','2002','Booij_2002','MA','CORE','SUP','BLOCO_02','2.3'),
 '11922881':('Berman','RM','2002','Berman_2002','EC','CORE','NEG','BLOCO_02','2.3'),
 '15450786':('Argyropoulos','SV','2004','Argyropoulos_2004','EC','CORE','SUP','BLOCO_02','2.3'),
 '33574223':('Schopman','JE','2021','Schopman_2021','EC','CORE','NEG','BLOCO_02','2.3'),
 '37430145':('Bilc','M','2023','Bilc_2023','ML','SUPPORT','NEG','BLOCO_02','2.3'),
 '15131521':('Neumeister','A','2004','Neumeister_2004','EC','CORE','SUP','BLOCO_02','2.3'),
 '3275471':('Kahn','RS','1988','Kahn_1988','ML','SUPPORT','SUP','BLOCO_02','2.3'),
 '8988796':('Salomon','RM','1997','Salomon_1997','EC','CORE','NEG','BLOCO_02','2.3'),
 '14647394':('Booij','L','2003','Booij_2003','EC','SUPPORT','SUP','BLOCO_02','2.3'),
 '14731308':('Leyton','M','2003','Leyton_2003','EC','SUPPORT','SUP','BLOCO_02','2.3'),
 '12955284':('Harrison','BJ','2001','Harrison_2001','EC','SUPPORT','SUP','BLOCO_02','2.3'),
 # DA (BLOCO_03 / 3.1)
 '29573379':('Moriya','T','2018','Moriya_2018','EC','SUPPORT','SUP','BLOCO_03','3.1'),
 '28870407':('Pecina','M','2017','Pecina_2017','EC','CORE','SUP','BLOCO_03','3.1'),
 '37301129':('Phillips','JL','2023','PhillipsJ_2023','OB','CORE','REF','BLOCO_03','3.1'),
 '26525751':('Lucido','MJ','2015','Lucido_2015','OB','SUPPORT','REF','BLOCO_08','B1xB4'),
 '26323245':('Young','CB','2015','Young_2015','OB','CORE','REF','BLOCO_03','3.1'),
 '18654637':('Dunlop','BW','2008','Dunlop_2008','OB','SUPPORT','REF','BLOCO_03','3.1'),
 '33631251':('Moriya-VanRooij','T','2021','MoriyaVanRooij_2021','EC','SUPPORT','SUP','BLOCO_03','3.1'),
 '36889362':('Hersey','M','2023','Hersey_2023','ML','SUPPORT','MEC','BLOCO_08','B1xB4'),
 '29106542':('Silvetti','M','2017','Silvetti_2017','ML','SUPPORT','MEC','BLOCO_03','3.1'),
 '29309799':('Whitton','AE','2018','Whitton_2018','MA','CORE','SUP','BLOCO_03','3.1'),
 '23711983':('AitOumeziane','B','2013','AitOumeziane_2013','ML','SUPPORT','SUP','BLOCO_03','3.1'),
 # LC (BLOCO_04)
 '12668290':('Berridge','CW','1993','Berridge_1993','ML','CORE','MEC','BLOCO_04','LC'),
 '18255055':('Jacobs','BL','2008','Jacobs_2008','OB','SUPPORT','REF','BLOCO_04','LC'),
 '20210846':('Sara','SJ','2009','Sara_2009','OB','CORE','MEC','BLOCO_04','LC'),
 '28596922':('Bouret','S','2017','Bouret_2017','OB','SUPPORT','REF','BLOCO_04','LC'),
 '29341884':('AstonJones','G','2018','AstonJones_2018','OB','CORE','REF','BLOCO_04','LC'),
 '26607253':('Poe','GR','2015','Poe_2015','OB','SUPPORT','MEC','BLOCO_04','LC'),
 '27616990':('McCall','JG','2015','McCallJ_2015','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '26212712':('Yu','AJ','2015','Yu_2015','OB','SUPPORT','MEC','BLOCO_04','LC'),
 '28708061':('Ross','JA','2017','Ross_2017','OB','SUPPORT','SUP','BLOCO_04','LC'),
 '28367128':('Black','SW','2017','Black_2017','OB','SUPPORT','REF','BLOCO_04','LC'),
 '36289638':('Mutschler','I','2022','Mutschler_2022','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '30430940':('Arnsten','AFT','2018','Arnsten_2018','OB','CORE','REF','BLOCO_04','LC'),
 '37139472':('Schmidt','K','2023','Schmidt_2023','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '40442382':('Hake','HS','2025','Hake_2025','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '40219735':('Tang','A','2025','Tang_2025','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '41225565':('Lei','Y','2025','Lei_2025','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '41066175':('Kim','SG','2025','Kim_2025','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '41000807':('Borsini','F','2025','Borsini_2025','OB','SUPPORT','REF','BLOCO_04','LC'),
 '38155473':('Bari','BA','2022','Bari_2022','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '41938091':('Pandey','R','2026','Pandey_2026','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '19960531':('Goddard','AW','1996','Goddard_1996','EC','CORE','SUP','BLOCO_04','LC'),
 '29593511':('Heneka','MT','2018','Heneka_2018','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '31801809':('Terra','M','2019','Terra_2019','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '16566899':('Tillage','RP','2021','Tillage_2021','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '33911187':('Tillage','RP','2021','TillageR_2021','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '39427811':('Slavova','Y','2024','Slavova_2024','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '41167443':('Mir','F','2025','Mir_2025','ML','SUPPORT','MEC','BLOCO_04','LC'),
 '42332025':('Korukonda','S','2026','Korukonda_2026','ML','SUPPORT','MEC','BLOCO_04','LC'),
 # INF (BLOCO_08 conexão B1↔B4)
 '27480574':('Felger','JC','2016','Felger_2016','OB','CORE','REF','BLOCO_08','B1xB4'),
 '39694342':('Bekhbat','M','2024','Bekhbat_2024','EC','CORE','SUP','BLOCO_08','B1xB4'),
 # MOD (BLOCO_00 fronteira)
 '32363761':('Moriya','T','2019','Moriya_2019','OB','SUPPORT','REF','BLOCO_00','modelo'),
 '28926161':('Nestler','EJ','2017','Nestler_2017','OB','CORE','REF','BLOCO_00','modelo'),
 '39696597':('Dale','E','2024','Dale_2024','OB','CORE','REF','BLOCO_00','modelo'),
 '42198336':('Carmellini','CR','2025','Carmellini_2025','OB','SUPPORT','REF','BLOCO_00','modelo'),
 '34285088':('Page','CE','2021','Page_2021','OB','SUPPORT','REF','BLOCO_00','modelo'),
 '34265868':('Salomon','RM','1993','Salomon_1993','EC','SUPPORT','NEG','BLOCO_02','2.3'),
 '29033793':('Mandrioli','J','2017','Mandrioli_2017','OB','SUPPORT','REF','BLOCO_00','modelo'),
 '25813654':('Kang','HJ','2015','Kang_2015','EC','SUPPORT','SUP','BLOCO_00','modelo'),
}
# sanidade
busy=set()
for p,(k1,k2,k3,lbl,tag,niv,role,bk,sec) in list(M.items()):
    k=(k1,k3,lbl)
    if k in busy: print('DUP-LABEL',k,lbl)
    busy.add(k)
missing=[p for p in ENTRA if p not in M]
extra=[p for p in M if p not in ENTRA and p not in VIG]
print('ENTRA total:',len(ENTRA),'| mapeados:',len([p for p in ENTRA if p in M]))
print('SEM MAPA:',missing)
# sobrescrever rótulos com autoria real do PubMed: usar 1º autor real
def real_first_author(p):
    for e in FULL:
        if e.get('resolved') and e['pmid']==p:
            b=e.get('biblio',{})
            aus=b.get('authors') or []
            if aus: return re.sub(r'[^A-Za-z-]','',aus[0].split()[0])
    return None
fix=0
for p in list(M.keys()):
    ra=real_first_author(p)
    if not ra: continue
    k1=M[p][0]
    if re.sub(r'[^A-Za-z]','',k1).lower() not in re.sub(r'[^A-Za-z]','',ra).lower() and re.sub(r'[^A-Za-z]','',ra).lower() not in re.sub(r'[^A-Za-z]','',k1).lower():
        print(f'AUTOR-DIVERGE pmid={p} cfg={k1} pubmed={ra}'); fix+=1
print('divergencias:',fix)
json.dump({'ABS_KEYS':list(ABS.keys())[:0],'mapa':M}, open('/tmp/b4_at_cfg_mapa.json','w'))
