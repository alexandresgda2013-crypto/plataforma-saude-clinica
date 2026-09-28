#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera matriz_b3_at_final.json (CFG): id, label, tag, grupo, claim por ref [AT].
Fonte única de verdade para os scripts de md e JSONs."""
import json, re, unicodedata
from pathlib import Path
B3=Path('/home/user/BIBLIOTECAS/B03_Neuroplasticidade')
g1=json.load(open(B3/'producao/insumos/matriz_b3_g1.json'))
dec=json.load(open(B3/'producao/insumos/matriz_b3_decisao.json'))
regs={r['pmid']:r for r in g1['registros_anexo']}
matriz={m['pmid']:m for m in g1['matriz']}
ABS=json.load(open('/tmp/b3_abstracts.json'))
DOI_EXTRA={'39613915':'10.1038/s41380-024-02830-z','39562042':'10.1523/JNEUROSCI.0823-24.2024',
 '42066082':'10.1126/sciadv.aec1444','42287566':'10.1007/s40261-026-01565-9','41526004':'10.1152/jn.00516.2025'}

# grupo: A..O conforme plano
GRUPO={
 '17949819':'A','34053675':'A','29507199':'A','36826992':'A','38338875':'A','37761014':'A','30737641':'A',
 '35546951':'B','37488280':'B','21907221':'B','30894661':'B','39343821':'B','34407417':'B','33637303':'B',
 '37358072':'B','34731624':'B','29532791':'B','37793581':'B','35508195':'B','38687826':'B',
 '34968492':'C','36907686':'C','29158578':'C','28640258':'C','36596696':'C','40097740':'C','41633835':'C',
 '34016377':'C','33963284':'C','40339008':'C',
 '38177353':'D','42066082':'D','38278430':'D',
 '39562042':'E','23100425':'E','26938443':'E','29440558':'E','25451194':'E','30359599':'E','23946413':'E',
 '19489005':'E','32895399':'E','36866246':'E','22993436':'E','32071234':'E',
 '24048383':'F','26687096':'F','26015580':'F','29432620':'F','29387021':'F','22442074':'F','33053385':'F',
 '19153574':'F','31900428':'F','28926000':'F','35722560':'F',
 '37124348':'G','35074585':'G','39770460':'G','25340958':'G','32616214':'G',
 '35995236':'H','34819637':'H','34601342':'H','26786147':'H',
 '33643008':'I','37038358':'I','20686454':'I','39613915':'I',
 '27634355':'J','36050137':'J',
 '20655508':'K','35601905':'K','33795646':'K','29353879':'K','35354926':'K','35810199':'K','39116252':'K',
 '27066532':'K','31037646':'K','29691465':'K','29158584':'K',
 '34565579':'L',
 '37435365':'M','32353004':'M',
 '37047730':'N','39457754':'N',
 '17851537':'O','26076834':'O','21807003':'O','26404711':'O','26844236':'O','27240534':'O','22522470':'O',
 '31022420':'O','39864644':'O','40545507':'O','39368530':'O','31801966':'O','21967517':'O','23268191':'O',
 '28246558':'O','29545546':'O','34707481':'O','34298123':'O','35145379':'O','41659277':'O',
 '41620807':'O','39558048':'O','41526004':'O','42287566':'O','41594739':'O',
}
TAG_OVR={'20686454':'ML','28926000':'ML','22442074':'ML','34016377':'OB',
 '26687096':'ML','24048383':'ML','26015580':'ML','40339008':'ML','29158584':'ML',
 '22993436':'OB','23946413':'OB','39613915':'MA'}
NOTA={'35601905':'[dado negativo — associação inversa com sintomas depressivos]',
 '39613915':'[MA — sem efeito significativo cetamina→BDNF periférico; NEG/CONT]',
 '20686454':'[EXTRAPOLADO: roedor→humano]'}

def ascii_(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c)!='Mn')
def surname(a1):
    s=ascii_(a1.split()[0])
    s=re.sub(r"[^A-Za-z]","",s)
    return s
def tc_label(a1,ano,suf=''):
    return f"{surname(a1).capitalize()}_{ano}{suf}"

pmids = list(dict.fromkeys(dec['ENTRA_NUC']+dec['ENTRA_MET']+dec['ENTRA_ADD']))
vig = json.load(open(B3/'Evidencias/Bibliografia/01_pmids.json'))
ids_usados={r['id_referencia_interna'] for r in vig}
for pm in pmids: assert pm in GRUPO, pm
assert len(pmids)==len(GRUPO)==112, (len(pmids),len(GRUPO))
SUFIXO={'21907221':'c','27634355':'b','34016377':'b'}  # DUMAN_2012c / LIU_2017b / WU_2021b
NOME_FIX={'37038358':('NIKOLACPERKOVIC','NikolacPerkovic'),'36826992':('MOYAALVARADO','MoyaAlvarado'),
 '41659277':('AGUILARVALLES','AguilarValles'),'22993436':('FERNANDEZMONREAL','FernandezMonreal'),
 '41620807':('ODONNELL','ODonnell'),'39368530':('LUGENBUHL','Lugenbuhl')}
out=[]; vistos={}
for pm in pmids:
    src = regs.get(pm) or matriz.get(pm)
    a1 = src.get('autor1_real') or src.get('autor1') or '?'
    ano = (src.get('ano_real') or src.get('pubdate',''))[:4]
    sobre=surname(a1)
    suf = SUFIXO.get(pm,'')
    if pm in NOME_FIX:
        idr=f"REF_{NOME_FIX[pm][0]}_{ano}{suf}"
    else:
        idr=f"REF_{sobre.upper()}_{ano}{suf}"
    while idr in vistos or idr in ids_usados:
        suf = suf+'b' if suf else 'b'
        idr=f"REF_{sobre.upper()}_{ano}{suf}"
    vistos[idr]=pm
    mesh = ABS.get(pm,{}).get('mesh',[])
    sp = 'Humans' if 'Humans' in mesh else ('Animals' if 'Animals' in mesh else 'celular/in vitro')
    especie = 'humano' if 'Humans' in mesh else ('animal' if 'Animals' in mesh else 'celular')
    pts = src.get('pubtypes') or []
    tag = TAG_OVR.get(pm)
    if not tag:
        if 'Meta-Analysis' in pts or 'Systematic Review' in pts: tag='MA'
        elif 'Review' in pts: tag='OB'
        elif especie=='humano': tag='EC'
        else: tag='ML'
    if pm in NOME_FIX:
        label=f"{NOME_FIX[pm][1]}_{ano}{suf}"
    else:
        label=tc_label(a1,ano,suf)
    titulo = src.get('titulo','')
    doi = src.get('doi') or DOI_EXTRA.get(pm,'')
    abstract = ABS.get(pm,{}).get('abstract','').strip()
    achado = abstract[:340].rsplit(' ',1)[0]+'…' if len(abstract)>340 else abstract
    out.append({'pmid_final':pm,'titulo':titulo,'journal':src.get('journal',''),'ano':ano,
        'autores':src.get('autores_todos',[a1]),'pubtypes':pts,'species':especie,'especie_mesh':[sp],
        'abstract':abstract,'doi':doi,'ID':idr,'label':label,'tag':tag,'grupo':GRUPO[pm],
        'nota':NOTA.get(pm,''),'achado':achado})
extra_doi=[o for o in out if not o['doi']]
print('sem DOI:',[(o['pmid_final'],o['label']) for o in extra_doi])
json.dump(out,open(B3/'producao/insumos/matriz_b3_at_final.json','w'),ensure_ascii=False,indent=1)
from collections import Counter
print('total:',len(out),'| grupos:',dict(Counter(o['grupo'] for o in out)))
print('tags:',dict(Counter(o['tag'] for o in out)))
EOF = None
