import json, re

R = json.load(open('/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro/producao/insumos/matriz_b7_g1.json'))
vig = json.load(open('/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro/Evidencias/Bibliografia/01_pmids.json'))
vig_pmids = {str(r.get('pmid_oficial')) for r in (vig if isinstance(vig, list) else vig.get('referencias', []))}

inv = []
for k, v in R['ok'].items():
    inv.append({'pmid': v['pmid'], 'label': f"{v['decl_autor']} {v['decl_ano']}",
                'real_a1': v['real_a1'], 'real_ano': v['real_ano'], 'titulo': v['real_titulo'],
                'fonte': v['fonte'], 'pubtype': v.get('pubtype', []), 'doi': v['doi']})
for nome, v in R.get('por_pmid', {}).items():
    inv.append({'pmid': v['pmid'], 'label': nome, 'real_a1': v.get('real_a1', ''),
                'real_ano': v.get('real_ano', ''), 'titulo': v.get('real_titulo', ''),
                'fonte': v.get('fonte', ''), 'pubtype': v.get('pubtype', []), 'doi': '(sem doi no anexo)' if 'Carabotti' in nome else ''})
inv = [i for i in inv if i['pmid'] not in vig_pmids]
MASTERS = {'38355758','29902437','35229717','29467611','32577079','36797287','25830558','34127024','38939042','38390241','34731656','23201091','26466961','39940928','31910709','36746244','37049591','33493503','29157665','30711488','37070532','38911967','38612489','34589808','36776388','37386523'}
print('itens a decidir (menos 5 vigentes):', len(inv), '| masters esperadas novas:', len(MASTERS - vig_pmids))
n = 0
for i in sorted(inv, key=lambda x: (x['real_ano'], x['real_a1'])):
    n += 1
    ab = R['abstracts'].get(i['pmid'], {})
    a = ab.get('abstract', '')
    mestre = ' ★MASTER' if i['pmid'] in MASTERS else ''
    print(f"[{n:03d}]{mestre} {i['label']} pmid={i['pmid']} ({i['fonte']})")
    print('  TIT:', i['titulo'][:105])
    print('  MESH:', ' | '.join(ab.get('mesh', [])[:12])[:150])
    print('  PT:', ' | '.join(i['pubtype'])[:65])
    print('  ABS:', (a[:330] + ('…' if len(a) > 330 else '')) or '(SEM ABSTRACT)')
    print('-' * 100)
