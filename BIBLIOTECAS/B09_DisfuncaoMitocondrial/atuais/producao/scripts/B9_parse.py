#!/usr/bin/env python3
# B9 — parse do anexo (citações APA com DOI) → entradas
import re, json

RAW=open('/home/user/uploads/Artigos cientificos do mecanismo B9 disfunção mitocondrial.md',encoding='utf-8').read()
# blocos separados por linha em branco
blocks=[b.strip() for b in re.split(r'\n\s*\n', RAW) if b.strip()]
entries=[]
for b in blocks[1:]:  # primeiro bloco = título
    flat=' '.join(b.split())
    m=re.match(r'^(.+?)\s*\((\d{4})\)\.\s*(.+?)\.\s*\*([^*]+)\*\.?\s*(.*)$', flat)
    doi=''
    md=re.search(r'(?:https?://doi\.org/|doi:\s*)(10\.\d{4,9}/[^\s,;]+)', flat)
    if md: doi=md.group(1).rstrip('.').lower()
    if not m:
        entries.append({'raw':flat[:200],'parse':'FALHOU'})
        continue
    autores,ano,titulo,fonte,resto=m.groups()
    a1=autores.split(',')[0].strip()
    entries.append({'raw':flat,'decl_autor':a1,'decl_autores_full':autores,'decl_ano':ano,
                    'decl_titulo':titulo.strip(),'fonte_decl':fonte.strip(),'doi':doi,'parse':'OK'})

ok=[e for e in entries if e['parse']=='OK']
fal=[e for e in entries if e['parse']!='OK']
com_doi=[e for e in ok if e['doi']]
print('entradas:',len(entries),'| parse ok:',len(ok),'| com DOI:',len(com_doi),'| falhas:',len(fal))
for f in fal: print(' FALHA:',f['raw'])
sem=[e['decl_autor']+' '+e['decl_ano'] for e in ok if not e['doi']]
print('sem DOI:',sem)
json.dump(entries, open('/home/user/BIBLIOTECAS/B09_DisfuncaoMitocondrial/producao/insumos/b9_anexo_entries.json','w'), ensure_ascii=False, indent=1)
print('gravado b9_anexo_entries.json')
