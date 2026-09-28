#!/usr/bin/env python3
# B8 — parse do anexo APA (DOI) -> entries json
import json, re
raw=open('/home/user/uploads/Artigos cientificos do mecanismo B8 deficiencia micronutrientes.md',encoding='utf-8').read()
blocks=[b.strip() for b in raw.split('\n\n') if b.strip()]
entries=[]
for b in blocks[1:]:  # pular título
    m=re.search(r'\(\s*(\d{4})[a-z]?\s*\)', b)
    ano=m.group(1) if m else '?'
    autores=b[:m.start()].rstrip(' .,') if m else b[:80]
    a1=autores.split(',')[0].strip()
    d=re.search(r'https://doi\.org/(\S+)', b)
    doi=d.group(1).rstrip('.').rstrip(',') if d else None
    t=re.search(r'\)\.?\s+(.+?)\.\s*\*', b, re.S)
    tit=(t.group(1).replace('\n',' ') if t else '')
    entries.append({'decl_autor':a1,'decl_autores_full':autores,'decl_ano':ano,'decl_ano_raw':b[m.start():m.end()] if m else '',
                    'doi':doi,'decl_titulo':tit.strip(),'raw':b})
print('entries:',len(entries))
sem_doi=[e for e in entries if not e['doi']]
print('sem DOI:',len(sem_doi))
for e in sem_doi: print('  -',e['decl_autor'],e['decl_ano'],e['decl_titulo'][:70])
anos={}
for e in entries: anos[e['decl_ano']]=anos.get(e['decl_ano'],0)+1
print('dist anos:',dict(sorted(anos.items())))
json.dump(entries, open('/home/user/BIBLIOTECAS/B08_Micronutrientes/producao/insumos/b8_anexo_entries.json','w'), ensure_ascii=False, indent=1)
print('gravado b8_anexo_entries.json')
