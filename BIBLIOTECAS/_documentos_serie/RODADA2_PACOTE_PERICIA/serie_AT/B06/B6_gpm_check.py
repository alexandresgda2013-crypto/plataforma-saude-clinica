import json, re

R = json.load(open('/home/user/BIBLIOTECAS/B06_EstresseOxidativo/producao/insumos/matriz_b6_g1.json'))

# Tabela-mestra do briefing §3 (chave, PMID declarado)
GPM = """Aitken, 2011|21435402
Averill-Bates, 2023|36707132
Banerjee, 2004|15581573
Cabrini, 1998|9844729
Casique, 2013|23981774
Cheng, 2016|27051670
Choi, 2009|20090886
Conter, 2020|32887901
Conter, 2025|40327797
Dalto & Matte, 2017|28245568
Davis, 2006|16424114
Giustarini, 2023|37237960
Gould & Pazdro, 2019|31083508
Gregory, 2016|26765812
Hsu, 2015|25933612
Jain, 2001|11165869
Kabil, 1999|10531322
Kannan & Jain, 2004|14975445
Kato, 2026|42196957
Labarrere & Kassab, 2022|36386929
Lai, 2020|32635181
Lamers, 2009|19515736
Lapenna, 2023|37683986
Lima, 2006|16857832
Mahfouz, 2004|15203107
Mahfouz, 2009|20209473
Matxain, 2006|17134167
Matxain, 2009|19558175
Meier, 2001|11483494
Mosharov, 2000|11041866
Natera, 2012|22231514
Nuhu, 2020|32933160
Pajares, 2025|40141131
Pusceddu, 2019|31129702
Ramis, 2019|31480509
Sbodio, 2018|30007014
Shen, 2010|19955400
Singh, 2011|21315854
Stipanuk, 2004|15189131
Stipanuk, 2020|33000151
Taoka, 1999|10052944
Valgimigli, 2023|37759691
Wondrak & Jacobson, 2012|22116705
Yadav, 2012|22977242
Zhu, 2008|18476726"""

gpm = {}
for ln in GPM.strip().split('\n'):
    chave, pm = ln.split('|')
    gpm[chave.strip()] = pm.strip()

def norm_s(s):
    return re.sub(r'[^a-z]', '', s.lower())

print('=== VALIDAÇÃO TABELA-MESTRA GPM (45) vs minha resolução eutils ===')
ok = 0
usados = set()
for chave, pm_decl in gpm.items():
    sob = norm_s(chave.split(',')[0].split('&')[0].strip())
    ano = chave.strip()[-4:]
    hit = R['ok'].get('pmid:' + pm_decl) or None
    rec = None
    for k, v in R['ok'].items():
        if v['pmid'] == pm_decl:
            rec = v; break
    if not rec:
        for nome, v in R.get('por_pmid', {}).items():
            if v['pmid'] == pm_decl:
                rec = v; break
    if not rec:
        print(f'  FALHOU: {chave} pmid_decl={pm_decl} não consta na minha resolução')
        continue
    ra = norm_s((rec.get('real_a1') or '').split()[0] if rec.get('real_a1') else '')
    if sob[:6] == ra[:6] or sob[:5] in ra or ra[:5] in sob:
        ok += 1
        usados.add(pm_decl)
    else:
        print(f'  AUTOR DIVERGE: {chave} decl-pmid={pm_decl} | real={rec.get("real_a1")} ({rec.get("pmid")}) | {rec.get("real_titulo","")[:70]}')
print(f'confirmadas {ok}/45 (autor bate com PMID declarado)')

print()
print('=== CRUZAMENTO COM A CANÔNICA VIGENTE (36 PMIDs) ===')
vig = json.load(open('/home/user/BIBLIOTECAS/B06_EstresseOxidativo/Evidencias/Bibliografia/01_pmids.json'))
vig_refs = vig if isinstance(vig, list) else vig.get('referencias', [])
vig_pmids = {str(r.get('pmid_oficial')) for r in vig_refs}
novos = {v['pmid'] for v in R['ok'].values()} | {'7929220', '22116705'}
inter = vig_pmids & novos
print('vigentes:', len(vig_pmids), '| novas resolvidas:', len(novos), '| overdup:', inter)

print()
print('=== INVENTÁRIO COMPLETO DAS NOVAS (para matriz de decisão) ===')
inv = []
for k, v in sorted(R['ok'].items(), key=lambda x: (x[1]['real_ano'], x[1]['real_a1'])):
    inv.append({'pmid': v['pmid'], 'label': f"{v['decl_autor']} {v['decl_ano']}",
                'real_a1': v['real_a1'], 'real_ano': v['real_ano'],
                'titulo': v['real_titulo'], 'fonte': v['fonte'], 'pubtype': v.get('pubtype', []),
                'doi': v['doi']})
inv.append({'pmid': '7929220', 'label': 'Kéry & Kraus 1994', 'real_a1': 'Kery V', 'real_ano': '1994',
            'titulo': "Transsulfuration depends on heme in addition to pyridoxal 5'-phosphate. Cystathionine beta-synthase is a heme protein.",
            'fonte': 'J Biol Chem', 'pubtype': ['Journal Article'], 'doi': R['resgate_kery']['doi']})
inv.append({'pmid': '22116705', 'label': 'Wondrak & Jacobson 2012', **{kk: R['por_pmid']['Wondrak & Jacobson, 2012'].get({'real_a1':'real_a1','real_ano':'real_ano','real_titulo':'titulo','fonte':'fonte','pubtype':'pubtype'}[kk], '') for kk in ['real_a1','real_ano','real_titulo','fonte','pubtype']}})
inv[-1]['titulo'] = inv[-1].pop('real_titulo')
inv[-1]['doi'] = ''
R['inventario'] = inv
json.dump(R, open('/home/user/BIBLIOTECAS/B06_EstresseOxidativo/producao/insumos/matriz_b6_g1.json', 'w'), ensure_ascii=False)
print('inventario salvo:', len(inv), 'itens')
