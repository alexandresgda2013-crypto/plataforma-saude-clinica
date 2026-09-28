#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auditoria G1 do insumo B4 (Consolidação + anexo Consensus 177 refs + briefing v1 semente).
1) Resolve os 172 DOIs do anexo -> PMID (esearch), confere rótulo (autor1/ano).
2) Confere os PMIDs declarados na Consolidação + tabela-semente do briefing.
3) Cruza com as 37 refs vigentes da B4.
Saída: producao/insumos/matriz_b4_g1.json + resumo stdout."""
import json, re, time, urllib.parse, urllib.request
from pathlib import Path

BASE="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
B4=Path("/home/user/BIBLIOTECAS/B04_Monoaminas")
OUT=B4/"producao"/"insumos"; OUT.mkdir(parents=True, exist_ok=True)
ENTRIES=json.load(open("/tmp/b4_insumo_entries.json"))

MATRIX_PMIDS=[
 ("5319766","Schildkraut 1965 FUND"),("12953623","Baumeister 2003"),("11922881","Berman 2002"),
 ("11331552","Bell 2001"),("11063917","Moore 2000"),("12431859","Booij 2002"),
 ("35854107","Moncrieff 2022/23"),("26043325","Cowen 2015"),("37857415","Albert & Blier 2023"),
 ("38816586","Page 2024"),("15450786","Argyropoulos 2004"),("33574223","Schopman 2021"),
 ("37430145","Bîlc 2023"),("36000248","Strawbridge 2023"),("27623971","Wang 2016"),
 ("19428959","Savitz 2009"),("32363761","Moriya 2020"),("28870407","Peciña 2017"),
 ("37301129","Phillips 2023"),("27480574","Felger & Treadway 2017"),("39694342","Bekhbat 2025"),
 ("16566899","Nestler & Carlezon 2006"),("29100627","Naegeli 2018"),("32954002","Morris 2020"),
 ("34650410","Nwokafor 2021"),("39427811","Slavova 2024"),("41167443","Mir 2025"),
 ("42332025","Korukonda & Weinshenker 2026"),("40243512","Naoi 2025"),("33911187","Tillage 2021"),
 ("15131521","Neumeister 2003"),("4863731","Schildkraut 1967"),
 # briefing tabela-semente
 ("4169954","Coppen 1967"),("12869766","Caspi 2003"),("19531786","Risch 2009"),
 ("17389902","Ruhé 2007"),("17088501","Meyer 2006"),("20603146","Treadway & Zald 2011"),
 ("25860609","Yano 2015"),("8929413","Lesch 1996"),("37322065","Jauhar 2023"),
]
# buscas autor/tema para pendentes declarados sem PMID
ESCRAVAR=[("Vetulani J[Author] AND Sulser F[Author] AND 1975[pdat]","Vetulani & Sulser 1975 Nature"),
 ("Heninger GR[Author] AND Delgado PL[Author] AND monoamine depletion[Title] AND 1996[pdat]","Heninger 1996 modulatory"),
 ("Charney DS[Author] AND Monoamine dysfunction and the pathophysiology and treatment of depression[Title]","Charney 1998 (anexo s/DOI)"),
 ("Hirschfeld RM[Author] AND History and evolution of the monoamine hypothesis[Title]","Hirschfeld 2000 (anexo s/DOI)"),
 ("Leonard BE[Author] AND Evidence for a biochemical lesion in depression[Title]","Leonard 2000 (anexo s/DOI)"),
 ("Kayabasi[Author] AND Serotonin Receptors and Depression[Title]","Kayabaşı 2021 (anexo s/DOI)")]

def get(url,tries=4):
    for i in range(tries):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"arena-b4-audit/1.0"})
            with urllib.request.urlopen(req,timeout=30) as r: return r.read()
        except Exception:
            if i==tries-1: raise
            time.sleep(1.5*(i+1))
def esearch_q(q):
    d=json.loads(get(f"{BASE}esearch.fcgi?db=pubmed&term={urllib.parse.quote(q)}&retmode=json"))
    ids=d.get("esearchresult",{}).get("idlist",[])
    return ids[0] if ids else None
def esummary_batch(pmids):
    if not pmids: return {}
    d=json.loads(get(f"{BASE}esummary.fcgi?db=pubmed&id={','.join(pmids)}&retmode=json"))
    out={}
    for pm in pmids:
        r=d.get("result",{}).get(pm,{})
        aut=r.get("authors",[])
        out[pm]={"pmid":pm,"titulo":r.get("title",""),"autor1":(aut[0]["name"] if aut else ""),
            "autores_todos":[a["name"] for a in aut[:6]],"journal":r.get("fulljournalname",""),
            "pubdate":r.get("pubdate",""),"pubtypes":r.get("pubtype",[])}
    return out
def norm(s): return re.sub(r"[^a-zà-ÿ]","",s.lower())
def first_decl(b):
    b=b.lstrip()
    return "" if b.startswith("(") else b.split(",")[0].strip()

def main():
    vigentes=set(open('/tmp/b4_vigentes.txt').read().split())
    doi_map,falhas={},[]
    for i,e in enumerate(ENTRIES):
        doi=e["doi"]
        if not doi: continue
        try: pm=esearch_q(f'"{doi}"[aid]')
        except Exception as ex:
            falhas.append({"doi":doi,"declarado":e["block"][:80],"motivo":f"erro esearch: {ex}"}); continue
        if not pm: falhas.append({"doi":doi,"declarado":e["block"][:80],"motivo":"DOI não resolveu no PubMed"})
        else: doi_map[doi]=pm
        if (i+1)%25==0: print(f"esearch {i+1}", flush=True)
        time.sleep(0.36)
    print("resolvidos:",len(doi_map),"falhas:",len(falhas))
    cravar={}
    for q,label in ESCRAVAR:
        pm=esearch_q(q); cravar[label]=pm
        print("cravar:",label,"->",pm); time.sleep(0.4)
    all_pm=list(dict.fromkeys(list(doi_map.values())+[p for p,_ in MATRIX_PMIDS]+[p for p in cravar.values() if p]))
    meta={}
    for i in range(0,len(all_pm),40):
        meta.update(esummary_batch(all_pm[i:i+40])); time.sleep(0.4)
    pmid_nao_existe=[p for p,_ in MATRIX_PMIDS if not meta.get(p,{}).get("titulo")]
    registros=[]
    for e in ENTRIES:
        if not e["doi"]: continue
        pm=doi_map.get(e["doi"])
        if not pm: continue
        m=meta.get(pm,{})
        ano_real=(m.get("pubdate","")[:4])
        decl=first_decl(e["block"])
        aut_ok=norm(decl)[:5] and norm(decl)[:5] in norm(m.get("autor1",""))
        ano_ok=(e["year"] and ano_real.startswith(e["year"][:4]))
        registros.append({"doi":e["doi"],"pmid":pm,"declarado":decl,"ano_decl":e["year"],
          "autor1_real":m.get("autor1",""),"ano_real":ano_real,"titulo":m.get("titulo",""),
          "journal":m.get("journal",""),"pubtypes":m.get("pubtypes",[]),
          "rotulo_ok":bool(aut_ok and ano_ok),"ja_na_b4":pm in vigentes,"block":e["block"][:220]})
    pmids_anexo=set(doi_map.values())
    matriz=[]
    for p,label in MATRIX_PMIDS:
        m=meta.get(p,{})
        matriz.append({"pmid":p,"declarado":label,"autor1_real":m.get("autor1",""),
          "ano_real":m.get("pubdate","")[:4] if m else "","titulo":m.get("titulo","") if m else "",
          "tambem_no_anexo":p in pmids_anexo,"ja_na_b4":p in vigentes})
    cravar_meta=[{"declarado":l,"pmid":p,"titulo":meta.get(p,{}).get("titulo","") if p else "",
        "autor1_real":meta.get(p,{}).get("autor1","") if p else "",
        "ja_na_b4": p in vigentes if p else False} for l,p in cravar.items()]
    json.dump({"registros_anexo":registros,"falhas":falhas,"matriz":matriz,"cravar":cravar_meta,
      "pmid_nao_existe":pmid_nao_existe},
      open(OUT/"matriz_b4_g1.json","w"),ensure_ascii=False,indent=1)
    print("\n== RESUMO ==")
    print("anexo resolvidos:",len(registros),"| já na B4:",sum(1 for r in registros if r['ja_na_b4']))
    print("rótulo divergente:",sum(1 for r in registros if not r['rotulo_ok']))
    for r in registros:
        if not r['rotulo_ok']:
            print(f"  [DIF] doi={r['doi']} decl={r['declarado']}({r['ano_decl']}) real={r['autor1_real']}({r['ano_real']}) :: {r['titulo'][:60]}")
    print("falhas:",len(falhas))
    for f in falhas: print("  [FALHA]",(f.get('doi') or '')[:45],"::",f['declarado'][:55],"::",f['motivo'][:40])
    print("matriz não existentes:",pmid_nao_existe)
    print("matriz extras (fora do anexo):")
    for m2 in matriz:
        if not m2['tambem_no_anexo']: print("  [EXTRA]",m2['pmid'],m2['declarado'],"->",m2['autor1_real'],m2['ano_real'],"| vigente" if m2['ja_na_b4'] else "")
if __name__=="__main__": main()
