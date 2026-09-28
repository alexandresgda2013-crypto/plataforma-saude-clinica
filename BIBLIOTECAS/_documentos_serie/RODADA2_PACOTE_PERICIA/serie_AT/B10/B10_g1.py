#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G1 da B10: valida autor+ano+tema no PubMed para as âncoras centrais do GPM."""
import json,urllib.request,urllib.parse,time,unicodedata
def sa(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c)).lower()
BASE='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def es(term,n=8):
    for _ in range(3):
        try:
            u=BASE+'esearch.fcgi?'+urllib.parse.urlencode({'db':'pubmed','term':term,'retmode':'json','retmax':n,'sort':'relevance'})
            time.sleep(0.45); return json.load(urllib.request.urlopen(u,timeout=30))['esearchresult'].get('idlist',[])
        except Exception: time.sleep(1.5)
    return []
def su(ids):
    if not ids: return []
    u=BASE+'esummary.fcgi?'+urllib.parse.urlencode({'db':'pubmed','id':','.join(ids),'retmode':'json'})
    time.sleep(0.5); d=json.load(urllib.request.urlopen(u,timeout=40)).get('result',{}); return [d[i] for i in ids if i in d]

# (label, autor, ano, tema)
ANC=[
('Roenneberg_2003','Roenneberg','2003','chronotype Munich chronotype'),
('Takahashi_2017','Takahashi','2017','molecular architecture circadian clock review'),
('Mohawk_2012','Mohawk','2012','circadian clock mammalian'),
('Ralph_1990','Ralph','1990','suprachiasmatic nucleus tau mutant hamster'),
('Berson_2002','Berson','2002','melanopsin retinal ganglion'),
('Hattar_2002','Hattar','2002','melanopsin ipRGC retina brain'),
('Khalsa_2003','Khalsa','2003','melatonin dim light onset phase response'),
('Rosenwasser_na','Rosenthal','1984','seasonal affective disorder light therapy'),
('Lewy_2006','Lewy','2006','melatonin circadian phase'),
('Benedetti_2007','Benedetti','2007','sleep deprivation light bipolar'),
('Wu_na','Kupfer','1988','sleep EEG depression REM latency'),
('Landgraf_2016','Landgraf','2016','Bmal1 suprachiasmatic anxiety'),
('Roybal_2007','Roybal','2007','Clock mutant mania lithium mouse'),
('Ozburn_2017','Ozburn','2017','clock gene mood bipolar'),
('McClung_2017','McClung','2017','circadian rhythms mood disorders'),
('McClung_2019','McClung','2019','circadian rhythms psychiatry'),
('Coleman_2019','Coleman','2019','DLMO melatonin sleep depression young women'),
('Hasler_2010','Hasler','2010','circadian phase sleep depression'),
('Buckley_2010','Buckley','2010','circadian temperature melatonin depression'),
('Liang_2025','Liang','2025','SCN BDNF TrkB striatum mood'),
('Meyer_2024','Meyer','2024','nucleus accumbens clock Per1 Per2 anxiety'),
('Gardner_2026','Gardner','2026','mPFC molecular clock sleep deprivation antidepressant'),
('Hines_2013','Hines','2013','adenosine astrocyte sleep deprivation'),
('Fernandez_2018','Fernandez','2018','light retina non-image forming mood'),
('Tapia-Osorio_2013','Tapia-Osorio','2013','constant light anxiety HPA rat'),
('Vadnie_2017','Vadnie','2017','circadian stress mood review'),
('Fonken_2019','Fonken','2019','light at night circadian behavior'),
('Bedrosian_na','Nelson','2017','timing light mood Bedrosian'),
('Satyanarayanan_2020','Satyanarayanan','2020','agomelatine melatonin cytokine clock depression'),
('Etain_2012','Etain','2012','melatonin receptor bipolar genetic'),
('Schuch_2018','Schuch','2018','exercise depression meta-analysis'),
('Riemann_2019','Riemann','2019','insomnia depression bidirectional review'),
('Riemann_2010','Riemann','2010','insomnia depression'),
('Irwin_na','Walker','2020','sleep stress inflammation'),
('Geoffroy_2025','Geoffroy','2025','circadian bipolar'),
('Stalder_2022','Stalder','2022','sleep circadian cortisol? meta'),
('Brancaccio_2018','Brancaccio','2018','astrocyte circadian SCN'),
('Hastings_2018','Hastings','2018','SCN circadian networks'),
('Mendoza_2024','Mendoza','2024','circadian food reward'),
('Pires_2016','Pires','2016','sleep deprivation bipolar systematic'),
('Crouse_2021','Crouse','2021','circadian rhythm bipolar young'),
('Carmassi_2019','Carmassi','2019','sleep bipolar review'),
('Bunney_2013','Bunney','2013','circadian bipolar depression'),
('Belgium_na','Benedetti','2005','sleep wake therapy bipolar'),
('Souetre_1989','Souetre','1989','circadian rhythms depression temperature cortisol'),
('Ehlers_1988','Ehlers','1988','social zeitgeber'),
('Ehlers_na','Ehlers','1988','social rhythms zeitgeber'),
('Bunney_na','Bunney','2013','circadian antipsychotic bipolar'),
('Lewy_na','Lewy','2006','light phase'),
('Cain_na','Hasler','2010','circadian'),
]
res={}; sem=[]
for label,sob,ano,tema in ANC:
    recs=su(es(f'{sob}[au] {ano}[dp] {tema}')) or su(es(f'{sob} {ano} {tema.split()[0]}'))
    pick=None
    for r in recs:
        auall=' '.join(a.get('name','') for a in r.get('authors',[])[:6])
        if sa(sob) in sa(auall) and str(ano)==r.get('pubdate','')[:4]: pick=r; break
    if pick:
        res[pick['uid']]={'pmid':pick['uid'],'title':pick['title'].rstrip('.'),'journal':pick.get('fulljournalname',pick.get('source','')),'pubdate':pick.get('pubdate',''),'authors':[a['name'] for a in pick.get('authors',[])][:6],'anchor':label}
        print('OK',label,pick['uid'],'|',pick['title'][:55])
    else:
        sem.append(label); print('??',label,'->',[(r['uid'],r.get('authors',[{}])[0].get('name'),r.get('pubdate','')[:4]) for r in recs[:2]])
json.dump(res,open('/home/user/BIBLIOTECAS/B10_DesregulacaoCircadiana/producao/g1_resolvidos.json','w'),ensure_ascii=False,indent=1)
json.dump(sem,open('/home/user/BIBLIOTECAS/B10_DesregulacaoCircadiana/producao/g1_sem_fonte.json','w'),ensure_ascii=False,indent=1)
print('\nRESOLVIDOS:',len(res),'| SEM:',len(sem))
