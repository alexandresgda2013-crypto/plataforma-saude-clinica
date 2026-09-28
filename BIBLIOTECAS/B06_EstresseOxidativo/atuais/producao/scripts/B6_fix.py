# -*- coding: utf-8 -*-
import json, unicodedata

BASE = '/home/user/BIBLIOTECAS/B06_EstresseOxidativo/'
INS = BASE + 'producao/insumos/'

# mapeamento anos: label_old -> (label_new, revista_ano novo, nota_add)
FIX = {
    'Banerjee_2005': ('Banerjee_2004', 'Arch Biochem Biophys 2005 (Epub 2004)'),
    'Sbodio_2019': ('Sbodio_2018', 'Br J Pharmacol 2019 (Epub 2018)'),
    'Pusceddu_2020': ('Pusceddu_2019', 'Eur J Nutr 2020 (Epub 2019)'),
}

# ---------- 1) at_final ----------
atp = INS + 'matriz_b6_at_final.json'
AT = json.load(open(atp))
for r in AT:
    if r['label'] in FIX:
        new, rev = FIX[r['label']]
        r['label'] = new
        r['id'] = 'REF_' + new.upper()
        r['ano'] = rev.split()[-1].strip('()') if rev.endswith(')') else r['ano']
        r['ano'] = new.split('_')[1]
        r['revista_ano_citado'] = rev
        r['nota'] += ' [rótulo alinhado ao Epub oficial; print no revista_ano]'
    if r['label'] == 'Bonaa_2006':
        r['aliases_extra'] = ['Bønaa']
json.dump(AT, open(atp, 'w'), ensure_ascii=False, indent=1)

# ---------- 2) canônica V2 ----------
mdp = BASE + 'B6 ESTRESSE OXIDATIVO V2 CANONICA.md'
doc = open(mdp, encoding='utf-8').read()
subs = [
    ('Banerjee_2005[OB]', 'Banerjee_2004[OB]'), ('BANERJEE_2005[OB]', 'BANERJEE_2004[OB]'),
    ('Sbodio_2019[OB]', 'Sbodio_2018[OB]'), ('SBODIO_2019[OB]', 'SBODIO_2018[OB]'),
    ('Pusceddu_2020[OB]', 'Pusceddu_2019[OB]'), ('PUSCEDDU_2020[OB]', 'PUSCEDDU_2019[OB]'),
    ('(Pusceddu 2020)[OB]', '(Pusceddu 2019)[OB]'),
]
for old, new in subs:
    assert old in doc, 'ausente no md: ' + old
    doc = doc.replace(old, new)
open(mdp, 'w', encoding='utf-8').write(doc)
for _, (new, _) in FIX.items():
    assert new + '[OB]' in doc
assert '(Pusceddu 2019)[OB]' in doc
import re
assert not re.search(r'\b\d{7,9}\b', doc), 'PMID-like no texto'

# ---------- 3) JSONs ----------
def ano_ref(new):
    return new.split('_')[1]

Ap = BASE + 'Evidencias/Bibliografia/01_pmids.json'
Vp = BASE + 'Evidencias/Vinculos/vinculos_referencia_afirmacao.json'
Lp = BASE + 'Auditoria_B6/ledger_auditoria_B6.json'
A = json.load(open(Ap)); V = json.load(open(Vp)); L = json.load(open(Lp))

def patch(rec, idkey, doi=None):
    lab_old = rec['id_referencia_interna'].replace('REF_', '')
    lab_old = lab_old[0] + lab_old[1:].lower()
    return lab_old

for arr, kind in ((A, 'pmids'), (V, 'vinc'), (L, 'led')):
    for rec in arr:
        rid = rec.get('id_referencia_interna', '')
        for old, (new, rev) in FIX.items():
            if rid == 'REF_' + old.upper():
                rec['id_referencia_interna'] = 'REF_' + new.upper()
                if kind == 'pmids':
                    rec['ids_referencia_interna'] = ['REF_' + new.upper()]
                    rec['revista_ano'] = rev
                    rec['_aliases'] = [new.split('_')[0], new.split('_')[0].upper()]
                    if 'Epub' not in rec.get('achado_central_molecular', ''):
                        rec['achado_central_molecular'] += ' | ano do rótulo = Epub oficial; print em revista_ano'
                if kind == 'led':
                    rec['citacao_literal'] = new + '[' + rec['citacao_literal'].split('[')[1]
                    rec['trecho_ancora'] = rec['trecho_ancora'].replace(old + '[OB]', new + '[OB]')
                if kind == 'vinc':
                    rec['trecho_ancora'] = rec['trecho_ancora'].replace(old + '[OB]', new + '[OB]')
        if rid == 'REF_BONAA_2006' and kind == 'pmids':
            if 'Bønaa' not in rec.get('_aliases', []):
                rec['_aliases'] = rec.get('_aliases', []) + ['Bønaa']

json.dump(A, open(Ap, 'w'), ensure_ascii=False, indent=1)
json.dump(V, open(Vp, 'w'), ensure_ascii=False, indent=1)
json.dump(L, open(Lp, 'w'), ensure_ascii=False, indent=1)

# ---------- 4) verificação ----------
idsA = {x['id_referencia_interna'] for x in A}
idsV = {x['id_referencia_interna'] for x in V}
idsL = {x['id_referencia_interna'] for x in L}
assert idsA == idsV == idsL and len(idsA) == 108
assert 'REF_BANERJEE_2004' in idsA and 'REF_SBODIO_2018' in idsA and 'REF_PUSCEDDU_2019' in idsA
print('FIX OK — 108 em conjunto; refs renomeadas:', sorted(r for r in idsA if any(k in r for k in ('BANERJEE', 'SBODIO', 'PUSCEDDU', 'BONAA'))))
