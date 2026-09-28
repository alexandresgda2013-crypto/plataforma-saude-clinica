import re, json
txt=open('uploads/Artigos cientificos do mecanismo B5 Gaba Glutamato.md',encoding='utf-8',errors='replace').read().replace('\r\n','\n')
blocks=re.split(r'\n\s*\n', txt)
ent=[]
for b in blocks:
    b=b.strip()
    if not b or 'doi.org/' not in b.lower(): continue
    m=re.search(r'doi\.org/([^\s]+)', b, re.I)
    doi=m.group(1).rstrip('.,;').strip() if m else ''
    my=re.search(r'\((\d{4})[a-z]?\)', b)
    ano=my.group(1) if my else ''
    aut=b.split('(')[0].strip().rstrip(',.')[:120]
    t=re.search(r'\(\d{4}[a-z]?\)\.\s*(.+?)\.\s*\*', b, re.S)
    tit=(t.group(1).replace('\n',' ').strip() if t else '')[:240]
    ent.append({'doi':doi.lower(),'decl_autor':aut,'decl_ano':ano,'decl_titulo':tit})
print('entradas anexo:',len(ent))
seen={}; dups=[]
for e in ent:
    if e['doi'] in seen: dups.append(e['doi'])
    seen[e['doi']]=e
print('dups doi:',dups)
json.dump(ent,open('BIBLIOTECAS/B05_GabaGlutamato/producao/insumos/b5_anexo_entries.json','w'),ensure_ascii=False,indent=1)
json.dump({'consolidacao_pmids':['30144668','34354048','32619710','34023450','25340958','33059355','28234212','37358072','41781722','38865810','42362547','42278495','37419688','39562042','33837051','36681677','32158215','41577431','41475562','42250487','40581655','40199850'],
'consolidacao_dois':['10.1016/j.neuron.2019.03.013'],
'briefing_sementes':['8122957','9092613','10686270','16894061','17959792','17141740','21827775','10565505','20004363','28697889','30914923','22465203','27067130','28619476','30177236','34190962','37491938','21963369','16919524']},open('BIBLIOTECAS/B05_GabaGlutamato/producao/insumos/b5_consolidacao_ids.json','w'),ensure_ascii=False,indent=1)
