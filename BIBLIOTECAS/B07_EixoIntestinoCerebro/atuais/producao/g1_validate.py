#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G1: validacao de existencia via E-utilities esummary para B7."""
import json, time, urllib.request, urllib.parse, sys

IDS = [l.strip() for l in open('/tmp/b7_all_nums.txt') if l.strip()]
IDS = [i for i in IDS if i != '22814126']  # PMID trocado (lição de auditoria) — não é âncora

BASE = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

def esummary(ids):
    q = urllib.parse.urlencode({'db': 'pubmed', 'id': ','.join(ids), 'retmode': 'json'})
    url = BASE + 'esummary.fcgi?' + q
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)

out = {}
missing = []
# batch de 40
for k in range(0, len(IDS), 40):
    batch = IDS[k:k+40]
    data = esummary(batch)
    res = data.get('result', {})
    for pmid in batch:
        rec = res.get(pmid)
        if not rec:
            missing.append(pmid)
            continue
        out[pmid] = {
            'pmid': pmid,
            'title': rec.get('title', '').rstrip('.'),
            'journal': rec.get('fulljournalname', rec.get('source', '')),
            'pubdate': rec.get('pubdate', ''),
            'authors': [a.get('name', '') for a in rec.get('authors', [])][:6],
            'pubtype': rec.get('pubtype', []),
        }
    time.sleep(0.5)

print('TOTAL solicitados:', len(IDS))
print('RESOLVIDOS:', len(out))
print('NAO RESOLVIDOS:', missing)
json.dump(out, open('/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro/producao/g1_esummary.json', 'w'),
          ensure_ascii=False, indent=1)
for pmid in sorted(out, key=lambda x: int(x)):
    r = out[pmid]
    yr = r['pubdate'][:4]
    au = r['authors'][0] if r['authors'] else '?'
    print(f"{pmid} | {au} {yr} | {r['journal'][:45]} | {r['title'][:90]}")
