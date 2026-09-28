#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G1 da B11: valida autor+ano+tema no PubMed."""
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
ANC=[
('Brent_2012','Brent','2012','thyroid hormone synthesis mechanism review'),
('Zimmermann_2009','Zimmermann','2009','iodine deficiency review Lancet'),
('Bianco_2018','Bianco','2018','deiodinase thyroid hormone review'),
('Friesema_2005','Friesema','2005','MCT8 monocarboxylate thyroid transporter'),
('Groeneweg_2020','Groeneweg','2020','MCT8 Allan Herndon Dudley review'),
('Felmlee_2020','Felmlee','2020','MCT10 thyroid hormone transporter'),
('Cooke_2014','Cooke','2014','hypothyroidism hippocampus brain volume'),
('Silverman_2009','Silverman','2009','hypothyroidism brain PET glucose'),
('Duval_2021','Duval','2021','dopamine thyroid depression TSH'),
('Whybrow_2001','Bauer','2001','thyroid brain mood review Bauer Whybrow'),
('Sternbach_1983','Sternbach','1983','thyroid depression'),
('Joffe_na','Jackson','1998','thyroid psychological dysfunction review'),
('Dayan_2013','Panicker','2013','hypothyroidism symptoms Dayan Panicker'),
('Mason_1987','Mason','1987','thyroid adrenergic serotonin receptor brain'),
('Bunevicius_2010','Bunevicius','2010','thyroid mood psychiatric'),
('CooperKazaz_2009','Cooper-Kazaz','2009','T3 depression augmentation serotonin'),
('Siegmann_2018','Siegmann','2018','T3 depression meta-analysis augmentation'),
('Hochbaum_2024','Hochbaum','2024','thyroid hormone cortex metabolism behavior Cell'),
('Mayerl_2022','Mayerl','2022','MCT8 thyroid interneuron GABA'),
('SalasLucia_2025','Salas-Lucia','2025','thyroid neurogenesis'),
('Espina_2022','Espina','2022','thyroid glucocorticoid hippocampus gene'),
('Maddox_2025','Maddox','2025','thyroid fear memory amygdala Mol Psychiatry'),
('Sahin_2023','Sahin','2023','hyperthyroidism NMDA memory'),
('Valcarcel_2024','Valcarcel-Hernandez','2024','Mct8 Dio2 neurogliogenesis'),
('GuillenYunta_2024','Guillen-Yunta','2024','MCT8 astrocyte'),
('Sentis_2024','Sentis','2024','TRalpha1 hypothalamus temperature'),
('Pappa_2021','Pappa','2021','resistance thyroid hormone beta RTHbeta'),
('Toma_2026','Toma','2026','deiodinase cytokine low T3 NTIS'),
('Samuels_2018','Samuels','2018','thyroid function depression review'),
('Bode_2021','Bode','2021','T3 depression'),
('Sinko_2025','Sinko','2025','thyroid brain structure'),
('Kumar_2023','Kumar','2023','thyroid anxiety depression association'),
('Ates_2018','Ates','2018','subclinical thyroid psychiatric'),
('Watanave_2018','Watanave','2018','subclinical hypothyroidism depression'),
('Iosifescu_2001','Iosifescu','2001','T3 refractory depression'),
]
res={}; sem=[]
for label,sob,ano,tema in ANC:
    recs=su(es(f'{sob}[au] {ano}[dp] {tema}')) or su(es(f'{sob} {ano} {tema.split()[0]}'))
    pick=None
    for r in recs:
        auall=' '.join(a.get('name','') for a in r.get('authors',[])[:6])
        if sa(sob.split('-')[0]) in sa(auall) and str(ano)==r.get('pubdate','')[:4]: pick=r;break
    if pick:
        res[pick['uid']]={'pmid':pick['uid'],'title':pick['title'].rstrip('.'),'journal':pick.get('fulljournalname',pick.get('source','')),'pubdate':pick.get('pubdate',''),'authors':[a['name'] for a in pick.get('authors',[])][:6],'anchor':label}
        print('OK',label,pick['uid'],'|',pick['title'][:55])
    else:
        sem.append(label); print('??',label,'->',[(r['uid'],r.get('authors',[{}])[0].get('name'),r.get('pubdate','')[:4]) for r in recs[:2]])
json.dump(res,open('/home/user/BIBLIOTECAS/B11_DisfuncaoTireoidiana/producao/g1_resolvidos.json','w'),ensure_ascii=False,indent=1)
json.dump(sem,open('/home/user/BIBLIOTECAS/B11_DisfuncaoTireoidiana/producao/g1_sem_fonte.json','w'),ensure_ascii=False,indent=1)
print('\nRESOLVIDOS:',len(res),'| SEM:',len(sem),sem)
