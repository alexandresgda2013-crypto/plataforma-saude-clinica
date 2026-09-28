import json, urllib.request, urllib.parse, time, sys

def get(u, tries=4):
    for i in range(tries):
        try:
            return urllib.request.urlopen(u, timeout=60).read().decode('utf-8', 'replace')
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))

ES = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
ENT = '/home/user/BIBLIOTECAS/B06_EstresseOxidativo/producao/insumos/b6_anexo_entries.json'
OUT = '/home/user/BIBLIOTECAS/B06_EstresseOxidativo/producao/insumos/matriz_b6_g1.json'

ent = json.load(open(ENT))
# acréscimos do GPM citados mas não presentes no anexo (buscar por PMID direto)
PMS_DIR = {'Wondrak & Jacobson, 2012': '22116705'}
try:
    R = json.load(open(OUT))
except Exception:
    R = {'ok': {}, 'falha': {}, 'por_pmid': {}}

n = 0
for e in ent:
    d = e['doi']
    key = 'doi:' + d
    if key in R['ok'] or key in R['falha']:
        continue
    try:
        u = ES + 'esearch.fcgi?db=pubmed&retmode=json&term=' + urllib.parse.quote(d + '[aid]')
        j = json.loads(get(u))
        ids = j['esearchresult'].get('idlist', [])
        if ids:
            pm = ids[0]
            s = json.loads(get(ES + 'esummary.fcgi?db=pubmed&retmode=json&id=' + pm))['result'][pm]
            au = s.get('authors', [])
            a1 = (au[0]['name'] if au else '')
            R['ok'][key] = {**e, 'pmid': pm, 'real_a1': a1,
                            'real_ano': (s.get('pubdate', '')[:4]),
                            'real_titulo': s.get('title', ''), 'fonte': s.get('source', ''),
                            'pubtype': s.get('pubtype', [])}
        else:
            R['falha'][key] = {**e, 'motivo': 'doi nao resolveu no pubmed (NAO-IDX)'}
    except Exception as ex:
        R['falha'][key] = {**e, 'motivo': 'erro: ' + str(ex)[:80]}
    n += 1
    if n % 20 == 0:
        json.dump(R, open(OUT, 'w'), ensure_ascii=False)
        print(n, 'processados | ok', len(R['ok']), 'falha', len(R['falha']))
        sys.stdout.flush()
    time.sleep(0.34)

for nome, pm in PMS_DIR.items():
    if nome in R['por_pmid']:
        continue
    s = json.loads(get(ES + 'esummary.fcgi?db=pubmed&retmode=json&id=' + pm))['result'][pm]
    au = s.get('authors', [])
    a1 = (au[0]['name'] if au else '')
    R['por_pmid'][nome] = {'pmid': pm, 'real_a1': a1, 'real_ano': s.get('pubdate', '')[:4],
                           'real_titulo': s.get('title', ''), 'fonte': s.get('source', ''),
                           'pubtype': s.get('pubtype', [])}
    time.sleep(0.34)

json.dump(R, open(OUT, 'w'), ensure_ascii=False)
print('FIM ok', len(R['ok']), 'falha', len(R['falha']), 'por_pmid', len(R['por_pmid']))
