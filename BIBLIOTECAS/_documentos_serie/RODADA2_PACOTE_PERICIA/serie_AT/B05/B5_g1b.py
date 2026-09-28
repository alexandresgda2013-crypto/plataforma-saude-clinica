import json, urllib.request, urllib.parse, time, xml.etree.ElementTree as ET
def get(u,tries=4):
    for i in range(tries):
        try: return urllib.request.urlopen(u,timeout=90).read()
        except Exception:
            if i==tries-1: raise
            time.sleep(3)
ES='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
D='BIBLIOTECAS/B05_GabaGlutamato/producao/insumos/'
R=json.load(open(D+'matriz_b5_g1.json'))
C=json.load(open(D+'b5_consolidacao_ids.json'))
# pmids universo
pmids={v['pmid'] for v in R['ok'].values()}
cons=set(C['consolidacao_pmids'])
faltam=cons-pmids
print('consolidacao pmids a resolver extra:',faltam)
# esummary dos extras
for pm in list(faltam):
    try:
        s=json.loads(get(ES+'esummary.fcgi?db=pubmed&retmode=json&id='+pm).decode())['result'][pm]
        au=s.get('authors',[])
        R.setdefault('consolidacao_extra',{})[pm]={'pmid':pm,'decl_autor':'consolidacao','decl_ano':'','decl_titulo':'',
          'real_a1':(au[0]['name'] if au else ''),'real_ano':s.get('pubdate','')[:4],'real_titulo':s.get('title',''),
          'fonte':s.get('source',''),'pubtype':s.get('pubtype',[])}
        time.sleep(0.34)
    except Exception as ex: R.setdefault('consolidacao_falha',{})[pm]=str(ex)[:100]
print('extras ok:',len(R.get('consolidacao_extra',{})),'falha:',R.get('consolidacao_falha',{}))
# efetch abstracts para TODOS
todos=sorted({v['pmid'] for v in R['ok'].values()} | set(R.get('consolidacao_extra',{})))
AB={}
for i in range(0,len(todos),50):
    chunk=todos[i:i+50]
    x=get(ES+'efetch.fcgi?db=pubmed&retmode=xml&id='+','.join(chunk))
    root=ET.fromstring(x)
    for art in root.findall('.//PubmedArticle'):
        pm=art.findtext('.//PMID')
        ab=' '.join(''.join(e.itertext()) for e in art.findall('.//Abstract/AbstractText')).strip()
        mesh=[mh.findtext('DescriptorName') for mh in art.findall('.//MeshHeading') if mh.findtext('DescriptorName')]
        AB[pm]={'abstract':ab,'mesh':mesh}
    time.sleep(0.34)
R['abstracts']=AB
json.dump(R,open(D+'matriz_b5_g1.json','w'),ensure_ascii=False)
print('abstracts:',len(AB),'de',len(todos))
