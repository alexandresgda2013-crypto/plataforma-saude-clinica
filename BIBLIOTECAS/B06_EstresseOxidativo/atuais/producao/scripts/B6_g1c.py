import json, urllib.request, urllib.parse, time, re, sys

def get(u, tries=5):
    for i in range(tries):
        try:
            return urllib.request.urlopen(u, timeout=90).read().decode('utf-8', 'replace')
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))

ES = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
OUT = '/home/user/BIBLIOTECAS/B06_EstresseOxidativo/producao/insumos/matriz_b6_g1.json'
R = json.load(open(OUT))

# injeta os resgates confirmados de Kéry e Hu como 'ok' adicionais
KERY = {'doi': '10.1016/s0021-9258(18)47244-4', 'decl_autor': 'Kéry', 'decl_ano': '1994',
        'decl_titulo': "Transsulfuration depends on heme in addition to pyridoxal 5'-phosphate. Cystathionine beta-synthase is a heme protein.",
        'pmid': '7929220', 'resgate': 'busca_dirigida_autor_tema (auditoria assistente; briefing havia falhado)'}
resgate_kery = False

if 'abstracts' not in R:
    R['abstracts'] = {}

pmids = []
label_by_pmid = {}
for k, v in R['ok'].items():
    pmids.append(v['pmid'])
    label_by_pmid[v['pmid']] = f"{v['decl_autor']} {v['decl_ano']}"
# Kéry via resgate
pmids.append('7929220')
label_by_pmid['7929220'] = 'Kéry & Kraus 1994'
# Wondrak (por_pmid)
for nome, v in R.get('por_pmid', {}).items():
    pmids.append(v['pmid'])
    label_by_pmid[v['pmid']] = nome

pmids = sorted(set(pmids), key=lambda x: int(x))
print('total de PMIDs a efetch:', len(pmids))

todo = [p for p in pmids if p not in R['abstracts']]
print('faltam:', len(todo))
B = 40
for i in range(0, len(todo), B):
    chunk = todo[i:i + B]
    try:
        xml = get(ES + 'efetch.fcgi?db=pubmed&retmode=xml&id=' + ','.join(chunk))
    except Exception as ex:
        print('ERRO chunk', i, str(ex)[:60]); continue
    arts = re.findall(r'<PubmedArticle>.*?</PubmedArticle>', xml, re.S)
    for art in arts:
        mpm = re.search(r'<PMID[^>]*>(\d+)</PMID>', art)
        if not mpm:
            continue
        pm = mpm.group(1)
        abs_parts = re.findall(r'<AbstractText[^>]*>(.*?)</AbstractText>', art, re.S)
        abstr = ' '.join(re.sub(r'<[^>]+>', ' ', p) for p in abs_parts)
        abstr = re.sub(r'\s+', ' ', abstr).strip()
        mesh = re.findall(r'<DescriptorName[^>]*>(.*?)</DescriptorName>', art)
        ptypes = re.findall(r'<PublicationType[^>]*>(.*?)</PublicationType>', art)
        R['abstracts'][pm] = {'abstract': abstr[:3500], 'mesh': mesh, 'pubtypes': ptypes}
    print(f'chunk {i}: +{len(arts)} abstracts (total {len(R["abstracts"])})')
    sys.stdout.flush()
    time.sleep(0.4)

R['label_by_pmid'] = label_by_pmid
if True:
    R['resgate_kery'] = KERY
json.dump(R, open(OUT, 'w'), ensure_ascii=False)
sem_abs = [p for p in pmids if not R['abstracts'].get(p, {}).get('abstract')]
print('FIM; sem abstract:', [(p, label_by_pmid.get(p)) for p in sem_abs])
