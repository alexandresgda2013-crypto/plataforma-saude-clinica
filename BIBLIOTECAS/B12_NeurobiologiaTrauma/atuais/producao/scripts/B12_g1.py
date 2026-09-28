#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G1 da B12: valida autor+ano+tema no PubMed."""
import json,urllib.request,urllib.parse,time,unicodedata
def sa(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c)).lower()
BASE='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def es(term,n=8):
    for _ in range(3):
        try:
            u=BASE+'esearch.fcgi?'+urllib.parse.urlencode({'db':'pubmed','term':term,'retmode':'json','retmax':n,'sort':'relevance'})
            time.sleep(0.4); return json.load(urllib.request.urlopen(u,timeout=30))['esearchresult'].get('idlist',[])
        except Exception: time.sleep(1.5)
    return []
def su(ids):
    if not ids: return []
    u=BASE+'esummary.fcgi?'+urllib.parse.urlencode({'db':'pubmed','id':','.join(ids),'retmode':'json'})
    time.sleep(0.5); d=json.load(urllib.request.urlopen(u,timeout=40)).get('result',{}); return [d[i] for i in ids if i in d]
ANC=[
('Heim_2000','Heim','2000','Heim abuse women ACTH cortisol hyperresponsiveness JAMA'),
('Heim_2001','Heim','2001','Heim child abuse pituitary adrenal depression Am J Psychiatry'),
('Yehuda_1990','Yehuda','1990','Yehuda PTSD low urinary cortisol'),
('Yehuda_2016','Yehuda','2016','Yehuda holocaust FKBP5 offspring methylation'),
('Schumacher_2019','Schumacher','2019','Schumacher cortisol PTSD meta-analysis'),
('Klengel_2013','Klengel','2013','Klengel FKBP5 allele-specific demethylation trauma'),
('McGowan_2009','McGowan','2009','McGowan NR3C1 methylation suicide abuse brain'),
('Weaver_2004','Weaver','2004','Weaver maternal care GR methylation rat'),
('Caspi_2003','Caspi','2003','Caspi 5-HTTLPR stress depression gene environment'),
('Karg_2011','Karg','2011','Karg serotonin transporter stress depression meta-analysis'),
('Ressler_2011','Ressler','2011','Ressler PACAP PAC1 PTSD sex Nature'),
('Polanczyk_2009','Polanczyk','2009','Polanczyk CRHR1 abuse protective'),
('Berton_2006','Berton','2006','Berton BDNF social defeat mesolimbic Science'),
('Krishnan_2007','Krishnan','2007','Krishnan susceptibility resilience social defeat Cell'),
('Pena_2017','Peña','2017','Pena OTX2 VTA early life stress Science'),
('Milad_2002','Milad','2002','Milad Quirk fear extinction vmPFC Nature'),
('Rauch_2006','Rauch','2006','Rauch Shin Phelps amygdala fear neurocircuitry'),
('Shin_2006','Shin','2006','Shin amygdala medial prefrontal PTSD'),
('Liberzon_2010','Liberzon','2010','Liberzon stress neurocircuits'),
('Etkin_Wager','Wager','2007','Etkin Wager emotional regulation fMRI meta-analysis'),
('Patel_2012','Patel','2012','Patel anxiety amygdala fMRI meta-analysis'),
('Lissek_2014','Lissek','2014','Lissek fear generalization anxiety PTSD'),
('McCall_2015','McCall','2015','McCall CRH locus coeruleus arousal anxiety Neuron'),
('Pole_2007','Pole','2007','Pole heart rate variability PTSD meta-analysis'),
('Gilbertson_2002','Gilbertson','2002','Gilbertson hippocampus PTSD twins'),
('Ozer_2003','Ozer','2003','Ozer PTSD predictors meta-analysis'),
('Brewin_Brewin','Brewin','2000','Brewin PTSD review'),
('McEwen_2007','McEwen','2007','McEwen allostatic load stress'),
('Mehta_2024','Mehta','2024','Mehta trauma epigenetics'),
('Wingo_2018','Wingo','2018','Wingo PPM1F stress resilience methylation'),
('Bromis_2018','Bromis','2018','Bromis hippocampus trauma meta-analysis'),
('Logue_2018','Logue','2018','Logue PTSD genetics meta-analysis'),
('GalatzerLevy_2018','Galatzer-Levy','2018','Galatzer-Levy trauma trajectories'),
('Humphreys_2020','Humphreys','2020','Humphreys childhood adversity brain'),
('Liston_2009','Liston','2009','Liston chronic stress prefrontal connectivity'),
('Eckstrand_2019','Eckstrand','2019','Eckstrand trauma reward cingulate'),
('Sheridan_2014','Sheridan','2014','Sheridan McLaughlin threat deprivation'),
('Gunnar_2007','Gunnar','2007','Gunnar Quevedo stress neurobiology developing'),
('Cross_2017','Cross','2017','Cross sensitive period stress'),
('VanAssche_2020','Van Assche','2020','Van Assche attachment trauma anxiety depression'),
('Bangasser_2021','Bangasser','2021','Bangasser CRH arousal stress sex'),
('Binder_2008','Binder','2008','Binder FKBP5 PTSD risk'),
('Zhou_2007','Zhou','2007','Zhou epigenetic BDNF social defeat'),
('Tsankova_2006','Tsankova','2006','Tsankova epigenetic stress depression'),
('Caspi_2002','Caspi','2002','Caspi MAOA maltreatment violence'),
]
res={}; sem=[]
for label,sob,ano,tema in ANC:
    recs=su(es(f'{sob}[au] {ano}[dp] {tema}')) or su(es(f'{sob} {ano} {tema.split()[0]}'))
    pick=None
    for r in recs:
        auall=' '.join(a.get('name','') for a in r.get('authors',[])[:6])
        if sa(sob.split()[0]) in sa(auall) and str(ano)==r.get('pubdate','')[:4]: pick=r;break
    if pick:
        res[pick['uid']]={'pmid':pick['uid'],'title':pick['title'].rstrip('.'),'journal':pick.get('fulljournalname',pick.get('source','')),'pubdate':pick.get('pubdate',''),'authors':[a['name'] for a in pick.get('authors',[])][:6],'anchor':label}
        print('OK',label,pick['uid'],'|',pick['title'][:50])
    else:
        sem.append(label); print('??',label,'->',[(r['uid'],r.get('authors',[{}])[0].get('name')) for r in recs[:2]])
json.dump(res,open('/home/user/BIBLIOTECAS/B12_NeurobiologiaTrauma/producao/g1_resolvidos.json','w'),ensure_ascii=False,indent=1)
json.dump(sem,open('/home/user/BIBLIOTECAS/B12_NeurobiologiaTrauma/producao/g1_sem_fonte.json','w'),ensure_ascii=False,indent=1)
print('\nRESOLVIDOS:',len(res),'| SEM:',len(sem),sem)
