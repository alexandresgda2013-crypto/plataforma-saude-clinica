#!/usr/bin/env python3
# B7 — cruzamento definitivo: fila do anexo x V1 (85 pmids) x masters GPM(30)
import json, re

BASE='/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro'
d=json.load(open(f'{BASE}/producao/insumos/matriz_b7_g1.json'))
ok=d['ok']; ab=d['abstracts']; por=d['por_pmid']

pj=json.load(open(f'{BASE}/Evidencias/Bibliografia/01_pmids.json'))
pmids_v1=set()
refs_v1={}
def walk(o):
    if isinstance(o,dict):
        pm=None; rid=None
        for k,v in o.items():
            if k.lower()=='pmid' and isinstance(v,str): pm=v
            if k in ('id_referencia_interna','id','ref_id') and isinstance(v,str): rid=v
        if pm: pmids_v1.add(pm); refs_v1[pm]=rid
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for x in o: walk(x)
walk(pj)
print('V1 pmids:',len(pmids_v1))

MASTERS={  # 30 pmids master GPM (tabela-mestra + 3 fora do anexo)
 '38355758':'Aburto&Cryan 2024 LN Trp/KYN','29902437':'Agus 2021 permeabilidade','35229717':'Barki 2022 LPS barreiras',
 '32577079':'Bosi 2020 microbiota-imunidade','36797287':'Caetano-Silva 2023 probiotico 5-HT GF','25830558':'Carabotti 2015',
 '34127024':'Chen 2021 butirato TJP','38939042':'Chen 2024 ACSS2','38390241':'Cheng 2024 microglia SCFA','34731656':'Erny 2021 acetato microglia',
 '23201091':'Guo 2013 LPS occludin','26466961':'Guo 2015 TJP','31910709':'Kurita 2019 LPS BBB','36746244':'Li 2023 TJ','37049591':'Lin 2023 AHR microglia',
 '29157665':'Nighot 2017','30711488':'Nighot 2019','37070532':'Saikachain 2023 NAc KYN','38911967':'Sathyasaikumar 2024 IPrA',
 '38612489':'Schwarcz 2024 KYNA microbiota','34589808':'Spichak 2021 microglia SCFA','36776388':'Zhao 2023 L.reuteri KYN Treg','37386523':'Zhou 2023 mastocito-ENS',
 '25411471':'Braniste 2014 BBB GF (VIGENTE)','31460832':'Cryan 2019 (VIGENTE)','34450312':'Socala 2021 (VIGENTE)','36232548':'Goralczyk 2022 (VIGENTE)',
 '29467611':'Bonaz 2018 (fora anexo)','39940928':'Hwang 2025 (fora anexo)','33493503':'Margolis 2021 (fora anexo)'}

# extrair rotulos de autor da V1 para casar masters vigentes por nome
canon=open(f'{BASE}/B7 EIXO INTESTINO CEREBRO V1 CANONICA.md',encoding='utf-8').read()

linhas=[]
for k,v in ok.items():
    pm=v['pmid']
    linhas.append({'pmid':pm,'autor':v['real_a1'],'ano':v['real_ano'],'titulo':v['real_titulo'],'fonte':v['fonte'],'pubtype':v['pubtype'],'doi':v['doi'],'decl_autor':v['decl_autor'],'decl_ano':v['decl_ano']})
for kk,v in por.items():
    linhas.append({'pmid':v['pmid'],'autor':v['real_a1'],'ano':v['real_ano'],'titulo':v['real_titulo'],'fonte':v['fonte'],'pubtype':v['pubtype'],'doi':None,'decl_autor':kk.split(',')[0],'decl_ano':re.search(r'(\d{4})',kk).group(1)})
print('total anexo+por_pmid:',len(linhas))
# dedup por pmid
seen={}; 
for L in linhas: seen.setdefault(L['pmid'],L)
linhas=list(seen.values())
print('uniq pmid:',len(linhas))

vig=[L for L in linhas if L['pmid'] in pmids_v1]
print('JA VIGENTES (anexo∩V1):',len(vig))
for L in sorted(vig,key=lambda x:x['autor']):
    print('  VIG',L['pmid'],L['autor'],L['ano'],'|',L['titulo'][:70],'| master:',MASTERS.get(L['pmid'],'-'))

fila=[L for L in linhas if L['pmid'] not in pmids_v1]
print('FILA REAL (anexo - V1):',len(fila))
mast_fila=[L for L in fila if L['pmid'] in MASTERS]
print('masters na fila:',len(mast_fila))
for L in mast_fila: print('  MASTER-FILA',L['pmid'],L['autor'],L['ano'])
# masters fora do anexo: quais ja vigentes?
for pm,desc in MASTERS.items():
    st='VIGENTE' if pm in pmids_v1 else ('FILA' if pm in {L['pmid'] for L in fila} else 'AUSENTE-ANEXO')
    print('  MASTER',pm,desc[:46],'->',st)

json.dump({'vigentes':vig,'fila':fila}, open(f'{BASE}/producao/insumos/b7_cruzamento.json','w'), ensure_ascii=False, indent=1)
# pmids vigentes nao cobertos = a V1 inteira menos os vig -> quantos da V1 vieram deste anexo
print('V1 pmids vindos do anexo:',len(vig),'=> V1 tem mais',85-len(vig),'refs de origem anterior')
