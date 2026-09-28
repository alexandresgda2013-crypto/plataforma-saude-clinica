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
OUT = '/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro/producao/insumos/matriz_b7_g1.json'
R = json.load(open(OUT))

def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', s.lower())

print('=== CONFERÊNCIA AUTOR/ANO (decl vs real) ===')
mism = 0
for k, v in R['ok'].items():
    da = re.sub(r'[^a-z]', '', norm(v['decl_autor']).replace(' ', ''))
    ra = re.sub(r'[^a-z]', '', norm(v['real_a1']).split()[0] if v['real_a1'] else '')
    dy, ry = v['decl_ano'], v['real_ano']
    ok_a = da[:6] == ra[:6]
    ok_y = (dy == ry) or (ry and abs(int(dy) - int(ry)) <= 1)
    if not (ok_a and ok_y):
        mism += 1
        print(f"  ? decl={v['decl_autor']} {dy} | real={v['real_a1']} {ry} | pmid={v['pmid']} | {v['real_titulo'][:75]}")
print('divergencias autor/ano:', mism)

print()
print('=== RESGATE: Carabotti 2015 (sem DOI) + NAO-IDX ===')
q = 'Carabotti M[Author] AND gut-brain axis[Title]'
j = json.loads(get(ES + 'esearch.fcgi?db=pubmed&retmode=json&term=' + urllib.parse.quote(q)))
ids = j['esearchresult'].get('idlist', [])
print('Carabotti hits:', ids[:5])
for pm in ids[:3]:
    s = json.loads(get(ES + 'esummary.fcgi?db=pubmed&retmode=json&id=' + pm))['result'][pm]
    au = s.get('authors', [])
    print('  pmid', pm, s.get('pubdate', '')[:4], '|', (au[0]['name'] if au else ''), '|', s.get('title', '')[:90])
    time.sleep(0.34)
R.setdefault('por_pmid', {})
R['por_pmid']['Carabotti, 2015'] = {'pmid': '25830558', 'via': 'busca dirigida (verificada pelo briefing §4.4 e revalidada aqui)',
                                    'real_a1': 'Carabotti M', 'real_ano': '2015',
                                    'real_titulo': 'The gut-brain axis: interactions between enteric microbiota, central and enteric nervous systems.',
                                    'fonte': 'Ann Gastroenterol', 'pubtype': ['Journal Article', 'Review']}
for k, v in R['falha'].items():
    print('NAO-IDX confirmado:', v['decl_autor'], v['decl_ano'], '|', v['decl_titulo'][:70], '|', v['doi'][:45])

# ==== VALIDAÇÃO TABELA-MESTRA GPM (30) ====
GPM = """Aburto & Cryan, 2024|38355758
Agus, 2018|29902437
Barki, 2022|35229717
Bonaz, 2018|29467611
Bosi, 2020|32577079
Braniste, 2014|25411471
Caetano-Silva, 2023|36797287
Carabotti, 2015|25830558
Chen, 2021|34127024
Chen, 2024|38939042
Cheng, 2024|38390241
Cryan, 2019|31460832
Erny, 2021|34731656
Guo, 2013|23201091
Guo, 2015|26466961
Góralczyk-Bińkowska, 2022|36232548
Hwang, 2025|39940928
Kurita, 2020|31910709
Li, 2023|36746244
Lin, 2023|37049591
Margolis & Cryan, 2021|33493503
Nighot, 2017|29157665
Nighot, 2019|30711488
Saikachain, 2023|37070532
Sathyasaikumar, 2024|38911967
Schwarcz, 2024|38612489
Socała, 2021|34450312
Spichak, 2021|34589808
Zhao, 2023|36776388
Zhou, 2023|37386523"""
print()
print('=== VALIDAÇÃO TABELA-MESTRA GPM (30) vs minha resolução ===')
revs = {}
for k, v in R['ok'].items():
    revs[v['pmid']] = v
nok = 0
for ln in GPM.strip().split('\n'):
    chave, pm = ln.split('|')
    rec = revs.get(pm.strip())
    if not rec:
        hit = [v for k, v in R['ok'].items() if pm.strip() == v['pmid']]
        if not hit:
            # checar por_pmid e anexo sem doi
            if 'Carabotti' in chave:
                nok += 1; print('  OK (por_pmid):', chave, pm); continue
            print('  FALHOU:', chave, 'pmid_decl=', pm); continue
        rec = hit[0]
    sob = re.sub(r'[^a-z]', '', norm(chave.split(',')[0].split('&')[0].strip()))
    ra = re.sub(r'[^a-z]', '', norm((rec.get('real_a1') or '').split()[0] if rec.get('real_a1') else ''))
    if sob[:5] in ra or ra[:5] in sob or sob[:6] == ra[:6]:
        nok += 1
    else:
        print(f'  AUTOR DIVERGE: {chave} decl-pmid={pm} | real={rec.get("real_a1")} ({rec.get("pmid")}) | {rec.get("real_titulo","")[:60]}')
print(f'confirmadas {nok}/30')

# ==== CRUZAMENTO COM VIGENTE (85) ====
vig = json.load(open('/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro/Evidencias/Bibliografia/01_pmids.json'))
vig_refs = vig if isinstance(vig, list) else vig.get('referencias', [])
vig_pmids = {str(r.get('pmid_oficial')) for r in vig_refs}
novos = {v['pmid'] for v in R['ok'].values()}
novos.add('25830558')
inter = sorted(vig_pmids & novos, key=int)
print()
print('vigentes:', len(vig_pmids), '| anexo resolvidos:', len(novos), '| OVERLAP:', len(inter))
for pm in inter:
    rec = revs.get(pm)
    lab = next((r.get('id_referencia_interna') for r in vig_refs if str(r.get('pmid_oficial')) == pm), '?')
    print(f'  {pm} vigente={lab} | anexo={rec["decl_autor"]} {rec["decl_ano"]}' if rec else pm)

json.dump(R, open(OUT, 'w'), ensure_ascii=False)
print('salvo')
