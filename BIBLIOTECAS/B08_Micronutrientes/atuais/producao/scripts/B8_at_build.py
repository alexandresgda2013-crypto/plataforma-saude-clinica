#!/usr/bin/env python3
# B8 — build do pacote [AT] das 49 refs ENTRA (rodada GPM 2026-09-09)
import json, urllib.request, xml.etree.ElementTree as ET

BASE='/home/user/BIBLIOTECAS/B08_Micronutrientes'
M=json.load(open(f'{BASE}/producao/insumos/matriz_b8_decisao.json'))
entra=[x for x in M['itens'] if x['decisao']=='ENTRA']
assert len(entra)==49, len(entra)
pmids=[x['pmid'] for x in entra]

def efetch(ids):
    url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    data=('db=pubmed&id='+','.join(ids)+'&rettype=abstract&retmode=xml').encode()
    req=urllib.request.Request(url,data=data,headers={'User-Agent':'arena-audit/1.0'})
    return urllib.request.urlopen(req,timeout=90).read()

# efetch em 2 lotes (robustez)
raw=b''
for i in range(0,len(pmids),25):
    raw+=efetch(pmids[i:i+25])

arts={}
for chunk in raw.split(b'<?xml version="1.0" ?>'):
    if not chunk.strip(): continue
    if not chunk.lstrip().startswith(b'<'): chunk=b'<?xml version="1.0" ?>'+chunk
    try:
        root=ET.fromstring(b'<?xml version="1.0" ?>'+chunk if not chunk.startswith(b'<?xml') else chunk)
    except ET.ParseError:
        continue
    for a in root.iter('PubmedArticle'):
        pm=a.findtext('.//PMID')
        arts[pm]=ET.tostring(a)

assert len(arts)==49, (len(arts), set(pmids)-set(arts))

def info(pm):
    a=ET.fromstring(arts[pm])
    auths=[]
    for au in a.findall('.//Article/AuthorList/Author'):
        ln=au.findtext('LastName'); ini=au.findtext('Initials')
        if ln: auths.append(f'{ln} {ini}' if ini else ln)
        else:
            cn=au.findtext('CollectiveName')
            if cn: auths.append(cn)
    te=a.find('.//Article/ArticleTitle')
    ttl=''.join(te.itertext()) if te is not None else ''
    iso=a.findtext('.//Article/Journal/ISOAbbreviation') or a.findtext('.//Article/Journal/Title')
    epub=None
    for h in a.findall('.//PubmedData/History/PubMedPubDate'):
        if h.get('PubStatus')=='epub': epub=h.findtext('Year')
    pd=a.find('.//Article/Journal/JournalIssue/PubDate')
    pyr=pd.findtext('Year') if pd is not None else None
    if not pyr and pd is not None: pyr=(pd.findtext('MedlineDate') or '')[:4]
    doi=''
    for aid in a.findall('.//PubmedData/ArticleIdList/ArticleId'):
        if aid.get('IdType')=='doi': doi=aid.text or ''
    mesh=[]
    for m in a.findall('.//MeshHeadingList/MeshHeading/DescriptorName'):
        mesh.append(m.text)
    especie=[]
    if 'Humans' in mesh: especie.append('Humans')
    if 'Animals' in mesh: especie.append('Animals')
    abst=' '.join(''.join(x.itertext()) for x in a.findall('.//Abstract/AbstractText')).strip()
    ptypes=[p.text for p in a.findall('.//PublicationTypeList/PublicationType')]
    return {'pmid':pm,'autores':auths,'titulo':ttl,'iso':iso,'ano_print':pyr,'ano_epub':epub,
            'doi':doi,'mesh':mesh,'especie_mesh':especie,'abstract':abst,'pubtypes':ptypes}

out={}
for pm in pmids:
    out[pm]=info(pm)
    t=out[pm]
    print(pm, t['autores'][0] if t['autores'] else '?', '| print',t['ano_print'],'epub',t['ano_epub'],'|',t['iso'],'| esp',t['especie_mesh'],'| abs',len(t['abstract']),'| mesh',len(t['mesh']))

json.dump(out, open(f'{BASE}/producao/insumos/b8_at_efetch.json','w'), ensure_ascii=False, indent=1)
print('\nGRAVADO producao/insumos/b8_at_efetch.json n=', len(out))
