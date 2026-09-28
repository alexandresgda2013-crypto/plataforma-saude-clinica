#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G1 v2 da B9: valida autor+ano+TEMA (contexto do GPM), rejeita falso-positivo."""
import json, urllib.request, urllib.parse, time, unicodedata
BASE='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def sem_ac_(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c))
def es(term,n=8):
    for _ in range(3):
        try:
            u=BASE+'esearch.fcgi?'+urllib.parse.urlencode({'db':'pubmed','term':term,'retmode':'json','retmax':n,'sort':'relevance'})
            time.sleep(0.4); return json.load(urllib.request.urlopen(u,timeout=30))['esearchresult'].get('idlist',[])
        except Exception: time.sleep(1.5)
    return []
def su(ids):
    if not ids: return []
    for _ in range(3):
        try:
            u=BASE+'esummary.fcgi?'+urllib.parse.urlencode({'db':'pubmed','id':','.join(ids),'retmode':'json'})
            time.sleep(0.4); d=json.load(urllib.request.urlopen(u,timeout=40)).get('result',{}); return [d[i] for i in ids if i in d]
        except Exception: time.sleep(1.5)
    return []

# (rótulo, autor, ano, termos de título/tema que DEVEM aparecer em título/revista)
ANCH = [
 ('Konradi_2004','Konradi','2004',['mitochondrial','hippocampus','bipolar']),
 ('Ben-Shachar_2008','Ben-Shachar','2008',['mitochondrial complex I','brain','psychiatric']),
 ('Andreazza_2010','Andreazza','2010',['electron transport','mitochondrial','brain']),
 ('Holper_2019','Holper','2019',['complex I','mitochondrial','psychiatric']),
 ('Karabatsiakis_2014','Karabatsiakis','2014',['mitochondrial','depression','PBMC','respir']),
 ('Hroudova_2013','Hroudova','2013',['mitochondrial','oxidative phosphorylation','platelet','depression']),
 ('Fernstrom_2021','Fernstrom','2021',['mitochondrial','respiration','blood','depression']),
 ('Khan_2023','Khan','2023',['mitochondrial dysfunction','depression','review']),
 ('Scaini_2021','Scaini','2021',['mitochondrial dynamics','depression','Molecular Psychiatry']),
 ('Gebara_2020','Gebara','2020',['mitofusin','nucleus accumbens','anxiety','depression']),
 ('Papageorgiou_2024','Papageorgiou','2024',['mitochondrial dynamics','psychiatric']),
 ('Fanibunda_2019','Fanibunda','2019',['serotonin','mitochondrial biogenesis','PGC-1']),
 ('Deng_2024','Deng','2024',['PGC-1','dentate gyrus','depression','mitochondrial']),
 ('Ryan_2019','Ryan','2019',['PGC-1','depression','electroconvulsive']),
 ('Madrigal_2001','Madrigal','2001',['glutathione','lipid peroxidation','mitochondria','stress']),
 ('Casaril_2021','Casaril','2021',['mitochondrial','depression','bioenergetic','inflammat']),
 ('Picard_McEwen_2018','Picard','2018',['psychological stress','mitochondria','systematic']),
 ('Alcocer-Gomez_2014','Alcocer-Gomez','2014',['NLRP3','inflammasome','depression','mononuclear']),
 ('Ciubuc-Batcu_2024','Ciubuc-Batcu','2024',['mitochondrial nexus','major depressive']),
 ('Calarco_2024','Calarco','2024',['mitochondrial copy number','blood','depression']),
 ('Trumpff_2021','Trumpff','2021',['stress','mitochondrial DNA','cell-free']),
 ('Bansal_2016','Bansal','2016',['mitochondrial dysfunction','depression']),
 ('Filiou_2019','Filiou','2019',['mitochondria','anxiety','brain']),
 ('Ceylan_2024','Ceylan','2024',['mitoepigenetic','mood']),
 ('Verbal_2026','Verbal','2026',['circadian','mitochondria']),
 ('Torrell_2013','Torrell','2013',['mitochondrial DNA','brain','depression']),
 ('Picard_2021','Picard','2021',['social','mitochondria']),
 ('Turck_2025','Turck','2025',['mitochondri','mood','psychiatric']),
 ('Lobo_2024','Lobo','2024',['mitochondri','psychiatric','depression']),
]

out={}; sem=[]
for label,sob,ano,must in ANCH:
    recs = su(es(f'{sob}[au] {ano}[dp]'))
    if not recs:
        recs = su(es(f'{sob} {ano} mitochondr* depression'))
    cand=None
    for r in recs:
        if sem_ac_(sob).lower() not in sem_ac_(r.get('authors',[{}])[0].get('name','')).lower(): continue
        if str(ano)!=r.get('pubdate','')[:4]: continue
        tit=(r.get('title','')+' '+r.get('fulljournalname',r.get('source',''))).lower()
        score=sum(1 for m in must if sem_ac_(m).lower() in sem_ac_(tit))
        if score>=1:
            if cand is None or score>cand[1]: cand=(r,score)
    if cand:
        r=cand[0]
        out[r['uid']]={'pmid':r['uid'],'title':r['title'].rstrip('.'),'journal':r.get('fulljournalname',r.get('source','')),
          'pubdate':r.get('pubdate',''),'authors':[a['name'] for a in r.get('authors',[])][:6],'anchor':label}
        print(f"OK {label:22} {r['uid']} (score {cand[1]}) {r['title'][:55]}")
    else:
        sem.append(label); print(f"?? {label:22} SEM match com tema | cand: {[(x['uid'],x['title'][:40]) for x in recs[:2]]}")
json.dump(out, open('/home/user/BIBLIOTECAS/B09_DisfuncaoMitocondrial/producao/g1_resolvidos.json','w'), ensure_ascii=False, indent=1)
json.dump(sem, open('/home/user/BIBLIOTECAS/B09_DisfuncaoMitocondrial/producao/g1_sem_fonte.json','w'), ensure_ascii=False, indent=1)
print('\nRESOLVIDOS:',len(out),'| SEM:',len(sem),sem)
