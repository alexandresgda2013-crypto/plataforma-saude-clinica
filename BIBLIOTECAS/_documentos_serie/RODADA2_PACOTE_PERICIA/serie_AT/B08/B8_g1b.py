#!/usr/bin/env python3
# B8 — falhas + busca dirigida (Bourre/sem-DOI) + validação tabela-mestra 44 + cruzamento V1
import json, time, urllib.request, urllib.parse, xml.etree.ElementTree as ET, re

BASE='/home/user/BIBLIOTECAS/B08_Micronutrientes'
G=json.load(open(f'{BASE}/producao/insumos/matriz_b8_g1.json'))
print('=== FALHAS (10) ===')
for k,v in G['falha'].items():
    print(' ',k,'|',v.get('motivo'),'|',v.get('decl',''))

UA={'User-Agent':'arena-b8-audit/1.0'}
def get(url, data=None):
    req=urllib.request.Request(url, data=data, headers=UA)
    return urllib.request.urlopen(req, timeout=60).read()
def esearch(q):
    x=ET.fromstring(get(f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(q)}&retmode=xml'))
    return [i.text for i in x.iter('Id')]
def esummary(ids):
    if not ids: return {}
    raw=get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi', data=f'db=pubmed&id={",".join(ids)}&retmode=json'.encode())
    return json.loads(raw)['result']

# busca dirigida Bourre 2006
print('=== DIRIGIDA Bourre 2006 ===')
hits=esearch('Bourre JM[Author] AND 2006[dp] AND nutrients brain')
print('hits:',hits)
por={}
if hits:
    r=esummary(hits[:5])
    for pid in hits[:5]:
        d=r[pid]; print(pid, d['authors'][0]['name'], d.get('pubdate'), d.get('title','')[:110], '|', d.get('fulljournalname'))
        if 'Effects of nutrients' in d.get('title','') and d['authors'][0]['name'].startswith('Bourre'):
            por['Bourre, 2006']={'pmid':pid,'via':'busca dirigida (sem DOI no anexo; briefing §5 dizia NAO-IDX — REVISAR)',
              'real_a1':d['authors'][0]['name'],'real_ano':d.get('pubdate','')[:4],'real_titulo':d.get('title','').rstrip('.'),
              'fonte':d.get('fulljournalname'),'pubtype':d.get('pubtype',[])}

# tabela-mestra 44
MASTERS={'22796576':'Eyles 2013','25365455':'Du 2016','26828517':'Kennedy 2016','28202095':'Firth supl 2017','29206972':'Firth FEP 2017',
'30201141':'Wesselink 2019','30341413':'Barks 2019','32552785':'Plevin 2020','33428888':'Rudzki 2021','33500553':'Cui 2021',
'33763446':'Muscaritoli 2021','33904124':'Shayganfard 2022','34836113':'Barks 2021','35223256':'Badar 2022','35294077':'Barone 2022',
'35337631':'Sahu 2022','36173945':'McWilliams 2022','36411563':'Nogueira-de-Almeida 2023','37147046':'Fiani 2023','37299394':'Zielinska 2023',
'37836413':'Lahoda Brodska 2023','38203763':'Mathew 2024','38462972':'Berger 2024','38605872':'Rajasekar 2024','38630748':'Al Jassem 2024',
'38999789':'Hui 2024','39519523':'Carnegie 2024','39596221':'Scuto 2024','39703999':'Rucklidge 2025','39829265':'Rajen 2025',
'39952338':'Ye 2025','40100400':'Anmella 2025','40218925':'Faugere 2025','40289952':'Domanski 2025','40329546':'Radoeva 2025',
'40653891':'Astorino 2025','40739033':'Lu & Paterson 2025','40871684':'Skoczek-Rubinska 2025','41211168':'Fang 2025','41303365':'Faa 2025',
'42029584':'Alexa 2026','42144425':'Shahini 2026','42187879':'Moroianu 2026','42253799':'Tortajada 2026'}
ok_pm={e['pmid'] for e in [v for k,v in G['ok'].items()]}
print('=== MASTERS 44 ===')
falt=[]
r=esummary([p for p in MASTERS if p not in ok_pm])
for p,nm in MASTERS.items():
    if p in ok_pm: st='no anexo ✓'
    elif p in por: st='dirigida ✓'
    elif p in r:
        d=r[p]; st=f"fora do anexo — esummary: {d['authors'][0]['name']} {d.get('pubdate','')[:4]} ✓"
        por[f'{nm} (master fora-anexo)']={'pmid':p,'via':'esummary direto (master GPM fora do anexo)',
          'real_a1':d['authors'][0]['name'],'real_ano':d.get('pubdate','')[:4],'real_titulo':d.get('title','').rstrip('.'),
          'fonte':d.get('fulljournalname'),'pubtype':d.get('pubtype',[])}
    else: st='FALTA'; falt.append((p,nm))
    print(f'  {p} {nm:28s} {st}')
print('masters OK:',44-len(falt),'/44; faltando:',falt)

# cruzamento com V1 (96)
pj=json.load(open(f'{BASE}/Evidencias/Bibliografia/01_pmids.json'))
pmids_v1={e['pmid_oficial']:e['id_referencia_interna'] for e in pj}
G['por_pmid']=por
json.dump(G, open(f'{BASE}/producao/insumos/matriz_b8_g1.json','w'), ensure_ascii=False, indent=1)
anexo_pm=ok_pm|{v['pmid'] for v in por.values()}
overlap=[(pm,pmids_v1[pm]) for pm in anexo_pm if pm in pmids_v1]
print('=== CRUZAMENTO ===')
print('anexo total único:',len(anexo_pm),'| overlap V1:',len(overlap))
for pm,rid in sorted(overlap): print('  VIG',pm,rid)
fila=sorted(anexo_pm-set(pmids_v1))
print('FILA:',len(fila))
json.dump({'fila':fila,'overlap':overlap}, open(f'{BASE}/producao/insumos/b8_cruzamento.json','w'), ensure_ascii=False, indent=1)
