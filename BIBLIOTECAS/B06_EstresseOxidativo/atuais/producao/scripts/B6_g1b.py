import json, urllib.request, urllib.parse, time, re, sys

def get(u, tries=4):
    for i in range(tries):
        try:
            return urllib.request.urlopen(u, timeout=60).read().decode('utf-8', 'replace')
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))

ES = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
OUT = '/home/user/BIBLIOTECAS/B06_EstresseOxidativo/producao/insumos/matriz_b6_g1.json'
R = json.load(open(OUT))

def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', s.lower())

# 1) conferência de rótulos decl vs real
print('=== CONFERÊNCIA AUTOR/ANO (decl vs real) ===')
mism = 0
for k, v in R['ok'].items():
    da = norm(v['decl_autor']).split()[0] if v['decl_autor'] else ''
    ra = norm(v['real_a1']).split()[0] if v['real_a1'] else ''
    dy, ry = v['decl_ano'], v['real_ano']
    da_clean = re.sub(r'[^a-z]', '', da); ra_clean = re.sub(r'[^a-z]', '', ra)
    ok_a = da_clean[:6] == ra_clean[:6]
    ok_y = (dy == ry) or (ry and abs(int(dy) - int(ry)) <= 1)
    if not (ok_a and ok_y):
        mism += 1
        print(f"  AUTOR/ANO? decl={v['decl_autor']} {dy} | real={v['real_a1']} {ry} | pmid={v['pmid']} | {v['real_titulo'][:80]}")
print('divergencias autor/ano:', mism)
a1s = {v['pmid']: (v['real_a1'], v['real_ano'], v['real_titulo'][:90]) for v in R['ok'].values()}

# 2) tentativa de resgate dos NAO-IDX por título dirigido
print()
print('=== RESGATE NAO-IDX (title search) ===')
falhas = list(R['falha'].items())
resgatados = {}
for k, v in falhas:
    tit = v['decl_titulo']
    tit_clean = re.sub(r'[*\"\']', '', tit).strip()
    term = tit_clean[:120] + '[Title]'
    try:
        j = json.loads(get(ES + 'esearch.fcgi?db=pubmed&retmode=json&term=' + urllib.parse.quote(term)))
        ids = j['esearchresult'].get('idlist', [])
        if ids:
            pm = ids[0]
            s = json.loads(get(ES + 'esummary.fcgi?db=pubmed&retmode=json&id=' + pm))['result'][pm]
            rt = norm(s.get('title', ''))[:80]
            dt = norm(tit_clean)[:80]
            jac = len(set(rt.split()) & set(dt.split())) / max(1, len(set(dt.split())))
            print(f"  {v['decl_autor']} {v['decl_ano']} [{v['decl_titulo'][:60]}...] -> hits={ids[:3]} jaccard={jac:.2f} | real={s.get('title','')[:80]}")
            if jac > 0.6:
                resgatados[k] = {**v, 'pmid': pm, 'real_a1': (s.get('authors') or [{}])[0].get('name', ''),
                                 'real_ano': s.get('pubdate', '')[:4], 'real_titulo': s.get('title', ''),
                                 'fonte': s.get('source', ''), 'pubtype': s.get('pubtype', []),
                                 'resgate': 'title_search'}
        else:
            print(f"  {v['decl_autor']} {v['decl_ano']} [{v['decl_titulo'][:60]}...] -> SEM HIT (NAO-IDX confirmado)")
    except Exception as ex:
        print(f"  {v['decl_autor']} {v['decl_ano']} -> erro {str(ex)[:60]}")
    time.sleep(0.34)

# 3) Kéry 1994 / Hu 1995: busca dirigida por autores+tema
print()
print('=== BUSCA DIRIGIDA Kéry 1994 / Hu 1995 ===')
for q, tag in [('Kery V[Author] AND transsulfuration[Title]', 'Kery1994'),
               ('Hu ML[Author] AND antioxidant[Title] AND vitamin[Title]', 'Hu1995')]:
    try:
        j = json.loads(get(ES + 'esearch.fcgi?db=pubmed&retmode=json&term=' + urllib.parse.quote(q)))
        ids = j['esearchresult'].get('idlist', [])
        print(f'  {tag}: hits={ids[:5]}')
        for pm in ids[:3]:
            s = json.loads(get(ES + 'esummary.fcgi?db=pubmed&retmode=json&id=' + pm))['result'][pm]
            au = s.get('authors', [])
            print(f"     pmid={pm} {s.get('pubdate','')[:4]} | {(au[0]['name'] if au else '')} | {s.get('title','')[:90]}")
            resgatados.setdefault('dirigida:' + tag, []).append(
                {'pmid': pm, 'real_a1': (au[0]['name'] if au else ''), 'real_ano': s.get('pubdate', '')[:4],
                 'real_titulo': s.get('title', ''), 'fonte': s.get('source', ''), 'pubtype': s.get('pubtype', [])})
            time.sleep(0.34)
    except Exception as ex:
        print(f'  {tag}: erro {str(ex)[:60]}')

R['resgatados'] = resgatados
json.dump(R, open(OUT, 'w'), ensure_ascii=False)
print()
print('total ok:', len(R['ok']), '| falha pos-resgate:', len(R['falha']), '| resgatados:', len(resgatados))
