import json, urllib.request, urllib.parse, time, sys
def get(u, tries=4):
    for i in range(tries):
        try: return urllib.request.urlopen(u, timeout=60).read().decode('utf-8','replace')
        except Exception as ex:
            if i==tries-1: raise
            time.sleep(2*(i+1))
ES='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
ent=json.load(open('BIBLIOTECAS/B05_GabaGlutamato/producao/insumos/b5_anexo_entries.json'))
ent.append({'doi':'10.1016/j.neuron.2019.03.013','decl_autor':'Duman, Sanacora & Krystal','decl_ano':'2019','decl_titulo':'Altered connectivity in depression: GABA and glutamate neurotransmitter deficits'})
OUT='BIBLIOTECAS/B05_GabaGlutamato/producao/insumos/matriz_b5_g1.json'
try: R=json.load(open(OUT))
except Exception: R={'ok':{},'falha':{}}
n=0
for e in ent:
    d=e['doi']
    if d in R['ok'] or d in R['falha']: continue
    try:
        u=ES+'esearch.fcgi?db=pubmed&retmode=json&term='+urllib.parse.quote(d+'[aid]')
        j=json.loads(get(u)); ids=j['esearchresult'].get('idlist',[])
        if ids:
            pm=ids[0]
            s=json.loads(get(ES+'esummary.fcgi?db=pubmed&retmode=json&id='+pm))['result'][pm]
            au=s.get('authors',[]); a1=(au[0]['name'] if au else '')
            R['ok'][d]={**e,'pmid':pm,'real_a1':a1,'real_ano':(s.get('pubdate','')[:4]),'real_titulo':s.get('title',''),'fonte':s.get('source',''),'pubtype':s.get('pubtype',[])}
        else:
            R['falha'][d]={**e,'motivo':'doi nao resolveu no pubmed'}
    except Exception as ex:
        R['falha'][d]={**e,'motivo':'erro: '+str(ex)[:80]}
    n+=1
    if n%20==0: json.dump(R,open(OUT,'w'),ensure_ascii=False); print(n,'processados | ok',len(R['ok']),'falha',len(R['falha'])); sys.stdout.flush()
    time.sleep(0.34)
json.dump(R,open(OUT,'w'),ensure_ascii=False)
print('FIM ok',len(R['ok']),'falha',len(R['falha']))
