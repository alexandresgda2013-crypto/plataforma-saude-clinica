#!/usr/bin/env python3
# B7 — build do pacote [AT] das 31 refs ENTRA (rodada GPM 2026-09-09)
import json, time, urllib.request, xml.etree.ElementTree as ET

BASE='/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro'
M=json.load(open(f'{BASE}/producao/insumos/matriz_b7_decisao.json'))
entra=[x for x in M['itens'] if x['decisao']=='ENTRA']
assert len(entra)==31
pmids=[x['pmid'] for x in entra]

def efetch(ids):
    url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    data=('db=pubmed&id='+','.join(ids)+'&rettype=abstract&retmode=xml').encode()
    req=urllib.request.Request(url,data=data,headers={'User-Agent':'arena-audit/1.0'})
    return urllib.request.urlopen(req,timeout=60).read()

xml=efetch(pmids)
root=ET.fromstring(xml)
art={}
for a in root.iter('PubmedArticle'):
    pm=a.findtext('.//PMID')
    art[pm]=a
assert len(art)==31, (len(art), set(pmids)-set(art))

def info(pm):
    a=art[pm]
    auths=[]
    for au in a.findall('.//Article/AuthorList/Author'):
        ln=au.findtext('LastName'); ini=au.findtext('Initials')
        if ln: auths.append(f'{ln} {ini}' if ini else ln)
        else:
            cn=au.findtext('CollectiveName')
            if cn: auths.append(cn)
    ttl=''.join(a.find('.//Article/ArticleTitle').itertext()) if a.find('.//Article/ArticleTitle') is not None else ''
    iso=a.findtext('.//Article/Journal/ISOAbbreviation') or a.findtext('.//Article/Journal/Title')
    # anos
    dep=a.findtext('.//PubmedData/History/PubMedPubDate[@PubStatus="entrez"]/..')
    epub=None
    for h in a.findall('.//PubmedData/History/PubMedPubDate'):
        if h.get('PubStatus')=='epub': epub=h.findtext('Year')
    pd=a.find('.//Article/Journal/JournalIssue/PubDate')
    pyr=pd.findtext('Year') if pd is not None else None
    if not pyr and pd is not None: pyr=(pd.findtext('MedlineDate') or '')[:4]
    doi=''
    for aid in a.findall('.//PubmedData/ArticleIdList/ArticleId'):
        if aid.get('IdType')=='doi': doi=aid.text or ''
    mesh=set()
    for m in a.findall('.//MeshHeadingList/MeshHeading/DescriptorName'):
        mesh.add(m.text)
    especie=[]
    if 'Humans' in mesh: especie.append('Humans')
    if 'Animals' in mesh: especie.append('Animals')
    abst=' '.join(''.join(x.itertext()) for x in a.findall('.//Abstract/AbstractText')).strip()
    ptypes=[p.text for p in a.findall('.//PublicationTypeList/PublicationType')]
    return {'pmid':pm,'autores':auths,'titulo':ttl,'iso':iso,'ano_print':pyr,'ano_epub':epub,'doi':doi,'especie_mesh':especie,'abstract':abst,'pubtypes':ptypes}

out={}
for pm in pmids:
    out[pm]=info(pm)
    t=out[pm]
    print(pm,t['autores'][0] if t['autores'] else '?', '| print',t['ano_print'],'epub',t['ano_epub'],'|',t['iso'],'| doi',t['doi'][:40],'| esp',t['especie_mesh'],'| abs',len(t['abstract']))
json.dump(out, open(f'{BASE}/producao/insumos/b7_at_efetch.json','w'), ensure_ascii=False, indent=1)
