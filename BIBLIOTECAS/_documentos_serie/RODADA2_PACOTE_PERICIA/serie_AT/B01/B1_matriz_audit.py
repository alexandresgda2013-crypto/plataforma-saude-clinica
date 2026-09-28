#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auditoria ref-a-ref do INSUMO externo 'MATRIZ CANONICA B1' (neuroinflamacao).
Resolve cada identificador (PMID ou DOI) no PubMed (esearch+esummary) e
compara com os 188 ids ja cobertos pela B1 V3 CANONICA."""
import json,urllib.request,urllib.parse,time,re,sys
BASE='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def req(path,params):
    u=BASE+path+'?'+urllib.parse.urlencode(params)
    for _ in range(4):
        try:
            time.sleep(0.34); return json.load(urllib.request.urlopen(u,timeout=45))
        except Exception: time.sleep(1.5)
    return None
def esearch_doi(doi):
    d=req('esearch.fcgi',{'db':'pubmed','term':doi+'[aid]','retmode':'json'})
    return (d['esearchresult']['idlist'] or [None])[0] if d else None
def esum(ids):
    d=req('esummary.fcgi',{'db':'pubmed','id':','.join(ids),'retmode':'json'})
    if not d: return {}
    r=d['result']; return {i:r[i] for i in ids if i in r}

# (bloco, identificador, declarado_autor_ano)
ITENS=[
# 1 inflamacao periferica
('periferica','20015486','Dowlati 2010'),('periferica','28122130','Köhler 2017'),
('periferica','32113908','Osimo 2020'),('periferica','31427752','Liu 2019'),
('periferica','32807846','Ng'),('periferica','41226404','Gędek 2025'),
('periferica','41588410','Li 2026'),('periferica','1110775','Min 2023'),
('periferica','DOI:? 03946320231198828','Islam 2023'),
('periferica','10.1016/j.jad.2024.11.071','Jadhav 2024'),
('periferica','10.1111/ejn.15992','Elgellaie 2023'),
('periferica','10.3390/biomedicines12112501','Gavril 2024'),
('periferica','10.1089/cap.2019.0015',"D'Acunto 2019"),
('periferica','10.1136/bmjopen-2018-027925','Costello 2019'),
# 2 central
('central','31195092','Enache 2019'),('central','10.1093/schbul/sbx035','Wang & Miller 2018'),
('central','32917850','Böttcher 2020'),('central','32958675','Anderson 2020'),
('central','10.1038/s41593-020-0621-y','Nagy 2020'),
# 3 TSPO
('tspo','23850810','Hannestad 2013'),('tspo','28939116','Holmes 2018'),
('tspo','25797247','Setiawan 2015'),('tspo','30156409','Richards 2018'),
('tspo','30563872','Setiawan 2018'),('tspo','33515765','Schubert 2021'),
('tspo','36226319','Eggerstorfer 2022'),('tspo','37640701','Nutma 2023'),
('tspo','33433698','Nutma 2021'),('tspo','34848203','Guilarte 2022'),
('tspo','40036275','Wijesinghe 2025'),('tspo','31683271','Attwells 2020'),
('tspo','42034206','Barzon 2026'),('tspo','41957656','Barzon 2026'),
# 4 microglia extras
('microglia','10.1186/s12974-026-03614-3','Nussbaumer 2026'),
('microglia','10.1038/s12974-023-02769-y','Vicente-Rodríguez 2023'),
('microglia','10.1016/j.bbi.2022.10.022','Cheng 2022'),
# 5 kynurenine
('kyn','36231075','Almulla 2022'),('kyn','31940661','Haroon 2020'),
('kyn','27754481','Parrott 2016'),('kyn','10.1007/s12035-018-1096-7','Martín-Hernández 2018'),
('kyn','10.1186/s12974-026-03717-2',"O'Regan 2026"),
('kyn','10.1038/s41380-019-0414-4','Savitz 2019'),('kyn','10.1111/jnc.16015','Stone 2023'),
('kyn','10.5498/wjp.v13.i4.141','Badawy 2023'),('kyn','10.1515/revneuro-2022-0047','Gong 2023'),
('kyn','10.1515/revneuro-2024-0065','Bertollo 2025'),
('kyn','10.20944/preprints202201.0134.v1','Almulla & Maes preprint'),
('kyn','10.3390/jpm16020118','Murata 2026'),
# 6 NLRP3
('nlrp3','25603858','Zhang 2015'),('nlrp3','28263786','Kaufmann 2017'),
('nlrp3','34978026','Liu 2022 MCC950'),('nlrp3','41712983','McColgan 2026'),
('nlrp3','10.1016/j.phrs.2022.106625','Xia 2023'),('nlrp3','10.3390/ijms24010133','Kouba 2023'),
('nlrp3','10.1038/s41423-025-01275-w','Xu 2025'),('nlrp3','10.1038/s41423-021-00740-6','Huang 2021'),
('nlrp3','10.1016/j.tibs.2022.10.002','Xu & Núñez 2022'),
# 7 piroptose
('piroptose','34877938','Li 2021'),('piroptose','10.3389/fncel.2022.915969','Du 2022'),
('piroptose','10.1126/sciimmunol.abj3859','Wang 2021'),('piroptose','10.1073/pnas.1722041115','McKenzie 2018'),
('piroptose','10.1007/s00011-023-01790-4','Han 2023'),('piroptose','10.1007/s00401-022-02528-y','Moonen 2023'),
# 8 glutamato (declaradas so por autor/ano, sem id)
# 9 neurogenese
('ponte_b16','10.1172/jci.insight.146852','pyroptose glial'),
('ponte_b16','10.1038/s41401-026-01774-0','NLRP3 microglial IL-1β neurogenese'),
('ponte_b16','10.3389/fpsyt.2023.1242367','IL-33'),
# 12 antidepressivos
('antidepressivo','10.1016/j.psychres.2021.114317','fluoxetina'),
('antidepressivo','10.1007/s12035-017-0632-1','Köhler 2017 antidepressivo'),
('antidepressivo','10.1016/j.bbi.2019.02.021','Wang 2019 SSRI'),
('antidepressivo','10.1016/j.pnpbp.2017.04.026','Więdłocha 2018'),
('antidepressivo','10.1186/s12991-025-00596-4','Xie 2025 sertralina'),
('antidepressivo','10.1038/s41380-019-0474-5','Liu TNF resposta'),
]
# sem id, so autor/ano (nao auditaveis por identificador -> marcar G1)
SEM_ID=[
('glutamato','Dantzer & Walker 2014'),('glutamato','Bay-Richter 2014'),
('glutamato','Müller & Schwarz 2007'),('glutamato','Wu 2022'),
('bdnf','Erdem 2026'),('bdnf','Shen 2025'),
('bbb','Liang 2021'),('bbb','Turkheimer 2020'),
('suicidio','Bryleva & Brundin 2016'),('suicidio','Herzog 2024'),
('suicidio','Behera 2026'),('suicidio','Serafini 2017'),
('antidepressivo','? Liu (s41380-019-0474-5) ja listado'),
]
resolv={}; nao=[]
for bloco,ident,decl in ITENS:
    if ident.startswith('DOI:?'):
        nao.append((bloco,ident,decl,'identificador ilegivel/nao padrao')); continue
    if re.fullmatch(r'\d{6,9}',ident):
        pmid=ident
    else:
        pmid=esearch_doi(ident)
    if not pmid:
        nao.append((bloco,ident,decl,'nao localizado no PubMed')); continue
    m=esum([pmid]).get(pmid,{})
    resolv[ident]={'pmid':pmid,'bloco':bloco,'declarado':decl,
        'title':m.get('title','').rstrip('.'),'journal':m.get('fulljournalname',m.get('source','')),
        'pubdate':m.get('pubdate',''),'authors':[a['name'] for a in m.get('authors',[])[:4]]}
    print(f"[{len(resolv):3d}] {decl:32s} -> {pmid} | {m.get('pubdate','')[:11]:11s} | {(m.get('title') or '')[:60]}")
json.dump(resolv,open('/home/user/BIBLIOTECAS/B01_Neuroinflamacao/producao/insumos/matriz_b1_g1.json','w'),ensure_ascii=False,indent=1)
json.dump({'nao_localizados':nao,'sem_id':SEM_ID},open('/home/user/BIBLIOTECAS/B01_Neuroinflamacao/producao/insumos/matriz_b1_sem_id.json','w'),ensure_ascii=False,indent=1)
print()
print('RESOLVIDOS:',len(resolv),'| NAO LOCALIZADOS:',len(nao))
for x in nao: print('  -',x[1],'(',x[2],')',x[3])
print('SEM IDENTIFICADOR (so Autor,Ano no insumo):',len(SEM_ID))
for x in SEM_ID: print('  -',x[0],'|',x[1])
