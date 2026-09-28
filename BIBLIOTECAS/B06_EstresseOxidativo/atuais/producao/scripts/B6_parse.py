import re, json

SRC = '/home/user/uploads/Artigos cientificos do mecanismo B6 Stress oxidativo.md'
OUT = '/home/user/BIBLIOTECAS/B06_EstresseOxidativo/producao/insumos/b6_anexo_entries.json'

t = open(SRC, encoding='utf-8').read().replace('\r\n', '\n')
blocks = [b.strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
entries = []
for b in blocks:
    if 'doi.org/' not in b:
        print('SKIP (sem doi):', b[:90].replace('\n', ' '))
        continue
    flat = re.sub(r'\s+', ' ', b)
    m = re.match(r'^(.*?)\s*\((\d{4})\)\.\s*(.*?)\s*(?:\*\*?)?https?://doi\.org/([^\s*]+)', flat)
    if not m:
        m = re.match(r'^(.*?)\s*\((\d{4})\)\.\s*(.*?)(?:https?://doi\.org/([^\s*]+))', flat)
    if not m:
        print('FAIL parse:', flat[:120])
        continue
    autores, ano, titulo, doi = m.group(1), m.group(2), m.group(3), m.group(4)
    doi = doi.rstrip('.* ').strip()
    titulo = re.sub(r'\*+$', '', titulo).strip()
    a1 = autores.split(',')[0].strip()
    entries.append({'doi': doi, 'decl_autor': a1, 'decl_autores_full': autores[:120],
                    'decl_ano': ano, 'decl_titulo': titulo[:200]})

print('ENTRADAS:', len(entries))
dois = [e['doi'] for e in entries]
dups = [d for d in set(dois) if dois.count(d) > 1]
print('DOIs duplicados:', dups)
json.dump(entries, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('salvo em', OUT)
