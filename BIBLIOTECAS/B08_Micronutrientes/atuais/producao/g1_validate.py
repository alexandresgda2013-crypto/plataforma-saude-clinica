#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G1: validacao de existencia via E-utilities esummary para B8."""
import json, time, urllib.request, urllib.parse

IDS = [l.strip() for l in open('/tmp/b8_all.txt') if l.strip()]
# 28137334 = carta de controle de infeccao (descartado como ancora; mantido fora do Módulo 09)
DESCARTADOS = {'28137334'}
IDS = [i for i in IDS if i not in DESCARTADOS]

BASE = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def esummary(ids):
    q = urllib.parse.urlencode({'db':'pubmed','id':','.join(ids),'retmode':'json'})
    with urllib.request.urlopen(BASE+'esummary.fcgi?'+q, timeout=60) as r:
        return json.load(r)

out, missing = {}, []
for k in range(0, len(IDS), 40):
    batch = IDS[k:k+40]
    data = esummary(batch)
    res = data.get('result', {})
    for pmid in batch:
        rec = res.get(pmid)
        if not rec:
            missing.append(pmid); continue
        out[pmid] = {'pmid':pmid,
            'title':rec.get('title','').rstrip('.'),
            'journal':rec.get('fulljournalname',rec.get('source','')),
            'pubdate':rec.get('pubdate',''),
            'authors':[a.get('name','') for a in rec.get('authors',[])][:6],
            'pubtype':rec.get('pubtype',[])}
    time.sleep(0.5)

print('TOTAL:', len(IDS), '| RESOLVIDOS:', len(out), '| NAO RESOLVIDOS:', missing)
json.dump(out, open('/home/user/BIBLIOTECAS/B08_Micronutrientes/producao/g1_esummary.json','w'), ensure_ascii=False, indent=1)
for pmid in sorted(out, key=int):
    r = out[pmid]
    au = r['authors'][0] if r['authors'] else '?'
    print(f"{pmid} | {au} {r['pubdate'][:4]} | {r['journal'][:42]} | {r['title'][:88]}")
