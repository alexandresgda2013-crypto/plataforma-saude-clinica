# -*- coding: utf-8 -*-
import json, re, unicodedata

D = '/home/user/BIBLIOTECAS/B06_EstresseOxidativo/producao/insumos/'
M = json.load(open(D + 'matriz_b6_decisao.json'))
R = json.load(open(D + 'matriz_b6_g1.json'))
AB = R['abstracts']
inv = {i['pmid']: i for i in R['inventario']}
inv['14975445'] = {'pmid': '14975445', 'label': 'Kannan & Jain 2004', 'real_a1': 'Kannan K', 'real_ano': '2004',
                   'titulo': 'Effect of vitamin B6 on oxygen radicals, mitochondrial membrane potential, and lipid peroxidation in H2O2-treated U937 monocytes.',
                   'fonte': 'Free Radic Biol Med', 'pubtype': ['Journal Article'], 'doi': ''}

dec = {p: v for p, v in M['decisao'].items() if v[0] == 'ENTRA'}
assert len(dec) == 72

# overrides ref a ref pós-leitura de abstract (tag decidida na auditoria, não por heurística)
TAG_FIX = {'16531614': 'EC'}  # Bønaa NORVIT = RCT multicêntrico (não meta); lição NEG
ORDER = ['ENZ', 'B6DEF', 'ANTIOX', 'GSH', 'HUM', 'NEG', 'HIP']
BLOCO = {'ENZ': 'BLOCO01', 'B6DEF': 'BLOCO02', 'ANTIOX': 'BLOCO03', 'GSH': 'BLOCO03',
         'HUM': 'BLOCO05', 'NEG': 'BLOCO06', 'HIP': 'BLOCO08'}

norm = lambda s: re.sub(r'[^A-Za-z0-9]', '', unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode())

def sobrenome(a1_full, decl_label):
    # usa o 1º autor real do esummary quando existe; senão o declarado
    base = (a1_full or '').split(',')[0].split()[0] if a1_full else decl_label.split()[0].replace('&', '')
    w = re.split(r"[-' ]", base)
    return ''.join(x.capitalize() for x in w if x)

out = []
used = {}
# autores completos por pmid via R['ok']
autores_by_pmid = {}
tit_by_pmid = {}
fonte_by_pmid = {}
ano_by_pmid = {}
pts_by_pmid = {}
for k, v in R['ok'].items():
    pm = v['pmid']
    tit_by_pmid[pm] = v.get('real_titulo') or v.get('decl_titulo') or ''
    fonte_by_pmid[pm] = v.get('fonte') or ''
    ano_by_pmid[pm] = v.get('real_ano') or v.get('decl_ano') or ''
    pts_by_pmid[pm] = v.get('pubtype') or []
    sob = sobrenome(v.get('real_a1'), v.get('decl_autor'))
    ano = v.get('real_ano') or v.get('decl_ano')
    autores_by_pmid[pm] = {'sob': sob, 'a1': v.get('real_a1') or v.get('decl_autor')}
autores_by_pmid['7929220'] = {'sob': 'Kery', 'a1': 'Kery V'}
tit_by_pmid['7929220'] = "Transsulfuration depends on heme in addition to pyridoxal 5'-phosphate. Cystathionine beta-synthase is a heme protein."
fonte_by_pmid['7929220'] = 'J Biol Chem'
ano_by_pmid['7929220'] = '1994'
pts_by_pmid['7929220'] = ['Journal Article']
autores_by_pmid['22116705'] = {'sob': 'Wondrak', 'a1': 'Wondrak GT'}
tit_by_pmid['22116705'] = 'Vitamin B6: beyond coenzyme functions.'
fonte_by_pmid['22116705'] = 'Subcell Biochem'
ano_by_pmid['22116705'] = '2012'
pts_by_pmid['22116705'] = ['Journal Article', 'Review']
autores_by_pmid['14975445'] = {'sob': 'Kannan', 'a1': 'Kannan K'}
tit_by_pmid['14975445'] = inv['14975445']['titulo']
fonte_by_pmid['14975445'] = 'Free Radic Biol Med'
ano_by_pmid['14975445'] = '2004'
pts_by_pmid['14975445'] = ['Journal Article']

seq_bloco = {}
for g in ORDER:
    pmg = [p for p, v in dec.items() if v[1] == g]
    # ordenar por ano
    pmg.sort(key=lambda p: (ano_by_pmid.get(p, '9999'), autores_by_pmid[p]['sob']))
    for p in pmg:
        dest, grupo, tag, nota = dec[p]
        tag = TAG_FIX.get(p, tag)
        sob = autores_by_pmid[p]['sob']
        ano = ano_by_pmid[p]
        lab = norm(sob) + '_' + ano
        if lab in used:
            lab = lab + 'b'  # colisão Taoka_1999 -> Taoka_1999b (padrão B3/B5: b minúsculo após o ano)
        used[lab] = used.get(lab, 0) + 1
        bl = BLOCO[g]
        seq_bloco[bl] = seq_bloco.get(bl, 0) + 1
        cid = f'B6.MEC.{bl}.{seq_bloco[bl]:03d}'
        mesh = AB.get(p, {}).get('mesh', [])
        ml = [x.lower() for x in mesh]
        if tag == 'ML':
            esp = ['Animals']
        elif tag in ('MA', 'EC'):
            esp = ['Humans']
        else:
            esp = ['Animals'] if (any(x == 'animals' for x in ml) and not any(x == 'humans' for x in ml)) else ['Humans']
        # celular/in vitro para química/DFT/células humanas in vitro
        if p in ('17134167', '19558175', '22231514', '35390394', '11165869', '20209473', '14975445'):
            esp = ['celular/in vitro']
        papel = 'NEG' if g == 'NEG' else ('HIP' if g == 'HIP' else ('MEC' if tag == 'ML' else ('SUP' if tag in ('EC', 'MA') else 'REF')))
        out.append({'pmid': p, 'grupo': g, 'label': lab, 'id': 'REF_' + lab.upper()[:-2] + lab[-2:] if lab[-1] == 'b' else 'REF_' + lab.upper(),
                    'tag': tag, 'evid_role': papel, 'claim_id': cid,
                    'titulo': tit_by_pmid.get(p, ''), 'fonte': fonte_by_pmid.get(p, ''),
                    'ano': ano, 'autores': [autores_by_pmid[p]['a1']], 'pubtype': pts_by_pmid.get(p, []),
                    'especie_mesh': esp, 'abstract': AB.get(p, {}).get('abstract', '')[:1200], 'nota': nota})

# correção do ID misto para colisão: REF_TAOKA_1999b (b minúsculo no fim; padrão série)
for r in out:
    if r['label'].endswith('b') and 'taoka_1999b' in r['label'].lower():
        r['id'] = 'REF_TAOKA_1999b'

ids = [r['id'] for r in out]
labs = [r['label'] for r in out]
assert len(out) == 72 and len(set(ids)) == 72 and len(set(labs)) == 72, (len(set(ids)), len(set(labs)))
from collections import Counter
print('por grupo:', dict(Counter(r['grupo'] for r in out)))
print('tags:', dict(Counter(r['tag'] for r in out)))
print('amostras:', [(r['label'], r['id'], r['tag'], r['claim_id']) for r in out[:4]])
print('colisao:', [(r['label'], r['id']) for r in out if 'Taoka' in r['label']])
json.dump(out, open(D + 'matriz_b6_at_final.json', 'w'), ensure_ascii=False, indent=1)
print('ok ->', D + 'matriz_b6_at_final.json')
