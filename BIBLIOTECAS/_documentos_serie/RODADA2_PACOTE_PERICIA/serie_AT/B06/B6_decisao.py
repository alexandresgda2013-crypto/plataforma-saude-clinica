import json, re

R = json.load(open('/home/user/BIBLIOTECAS/B06_EstresseOxidativo/producao/insumos/matriz_b6_g1.json'))
inv = R['inventario']
# insere Kannan no inventario
inv_k = {'pmid': '14975445', 'label': 'Kannan & Jain 2004', 'real_a1': 'Kannan K', 'real_ano': '2004',
         'titulo': 'Effect of vitamin B6 on oxygen radicals, mitochondrial membrane potential, and lipid peroxidation in H2O2-treated U937 monocytes.',
         'fonte': 'Free Radic Biol Med', 'pubtype': ['Journal Article'], 'doi': '(fora do anexo; busca dirigida do GPM — verificado)'}
inv.append(inv_k)

def gole(i):
    pm = i['pmid']
    ab = R['abstracts'].get(pm, {})
    return ab.get('abstract', ''), ' | '.join(ab.get('mesh', [])[:14]), ' | '.join(ab.get('pubtypes', []))

NAOIDX = {e['doi'] for e in R['falha'].values()}
print('NAO-IDX definitivas (11 falhas - Kéry resgatada = 10):')
for k, v in R['falha'].items():
    print('  ', v['decl_autor'], v['decl_ano'], '|', v['decl_titulo'][:75], '|', v['doi'][:45])
print()
print('=' * 100)
n = 0
for i in sorted(inv, key=lambda x: (x['real_ano'], x['real_a1'])):
    a, m, p = gole(i)
    n += 1
    print(f"[{n:02d}] {i['label']}  pmid={i['pmid']}  ({i['fonte']})")
    print('  TIT:', i['titulo'][:110])
    print('  MESH:', m[:130])
    print('  PT:', p[:60])
    print('  ABS:', (a[:380] + ('…' if len(a) > 380 else '')) or '(SEM ABSTRACT)')
    print('-' * 100)
