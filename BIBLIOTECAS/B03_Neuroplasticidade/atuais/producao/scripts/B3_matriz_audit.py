#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auditoria G1 do insumo 'matriz canônica B3' (Consolidação + anexo Consensus 193 refs).
1) Resolve os 193 DOIs do anexo via eutils esearch -> PMID; confere rótulo (autor1/ano).
2) Resolve os PMIDs declarados na Consolidação colada (texto da mensagem).
3) Cruza tudo com as 53 refs vigentes da B3.
Saída: producao/insumos/matriz_b3_g1.json + resumo stdout.
"""
import json, re, time, urllib.parse, urllib.request
from pathlib import Path

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
B3 = Path("/home/user/BIBLIOTECAS/B03_Neuroplasticidade")
OUT = B3 / "producao" / "insumos"
OUT.mkdir(parents=True, exist_ok=True)

ENTRIES = json.load(open("/tmp/b3_insumo_entries.json"))  # 193 blocos do anexo

# PMIDs declarados na CONSOLIDAÇÃO colada (rótulo autor/ano conforme o insumo)
MATRIX_PMIDS = [
 ("20655508","Nissen 2010"),("29387021","Kishi 2018"),("33643008","Arosio 2021"),
 ("34053675","Castrén & Monteggia 2021"),("35810199","Appelbaum 2023"),
 ("35354926","Tartt 2022"),("29432620","Youssef 2018"),("19153574","Gatt 2009"),
 ("22442074","Yu 2012"),("33053385","Tian 2020"),("31900428","Notaras 2020"),
 ("34298123","Robinson 2021"),("35995236","Lu 2022"),("34819637","Yao 2022"),
 ("39116252","Chen 2024"),("39558048","Liao 2025"),("41620807","O'Donnell 2026"),
 ("35601905","Rygvold 2022"),("33795646","Höflich 2021"),("26687096","Kailainathan"),
 ("24048383","Anastasia"),("35722560","Pagliusi"),("36194941","meta TRD BDNF"),
 ("39613915","meta psicoplastógenos BDNF"),("21677641","Autry 2011"),
 ("20724638","Li 2010"),("23534055","Kavalali & Monteggia"),("21907221","Duman"),
 ("30894661","Duman 2019"),("35546951","Kang 2022"),("37124348","He"),
 ("35074585","Wang"),("38278430","Elmeseiny"),("34407417","Lin"),
 ("34731624","Suzuki"),("33637303","Wu"),("37358072","Zaytseva"),
 ("29532791","Zanos & Gould"),("27144355","Zanos"),("39562042","Storey"),
 ("37793581","Bottemanne"),("40097740","Brown 2025"),("41633835","Brown 2026"),
 ("42066082","TrkB/mGluR5 cross-talk"),("42287566","Ketamine Evolving Neuroplasticity"),
 ("41526004","25 anos cetamina"),("18037014","Bremner"),("17851537","Pittenger & Duman"),
 ("26076834","McEwen"),("21807003","McEwen 2011/12"),("29545546","Forrest"),
 ("31037646","Treccani"),("29691465","Pryazhnikov"),("39864644","Algaidi"),
 ("34601342","Parrott"),("40339008","Ma ZZ 2025"),("34880451","Yao erratum"),
 ("35364073","Robinson corrigendum"),
]

def get(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent":"arena-b3-audit/1.0"})
            with urllib.request.urlopen(req, timeout=30) as r: return r.read()
        except Exception as e:
            if i==tries-1: raise
            time.sleep(1.5*(i+1))

def esearch_doi(doi):
    q = urllib.parse.quote(f'"{doi}"[aid]')
    d = json.loads(get(f"{BASE}esearch.fcgi?db=pubmed&term={q}&retmode=json"))
    ids = d.get("esearchresult",{}).get("idlist",[])
    return ids[0] if ids else None

def esummary_batch(pmids):
    if not pmids: return {}
    d = json.loads(get(f"{BASE}esummary.fcgi?db=pubmed&id={','.join(pmids)}&retmode=json"))
    out={}
    for pm in pmids:
        r = d.get("result",{}).get(pm,{})
        aut = r.get("authors",[])
        out[pm] = {"pmid": pm, "titulo": r.get("title",""),
                   "autor1": (aut[0]["name"] if aut else ""),
                   "autores_todos": [a["name"] for a in aut[:6]],
                   "journal": r.get("fulljournalname",""),
                   "pubdate": r.get("pubdate",""), "pubtypes": r.get("pubtype",[])}
    return out

def first_declared_author(block):
    # formato: 'Sobrenome, I., ...' ; pode ser '(2017). ...' sem autor
    b = block.lstrip()
    if b.startswith("("): return ""
    return b.split(",")[0].strip()

def norm(s):
    return re.sub(r"[^a-zà-ÿ]","", s.lower())

def main():
    vigentes = {str(r["pmid_oficial"]): r for r in json.load(open(B3/"Evidencias"/"Bibliografia"/"01_pmids.json"))}
    doi_map, falhas = {}, []
    # 1) resolve 193 DOIs -> PMID
    for i,e in enumerate(ENTRIES):
        doi = e["doi"]
        try: pm = esearch_doi(doi)
        except Exception as ex:
            falhas.append({"doi":doi,"declarado":e["block"][:80],"motivo":f"erro esearch: {ex}"}); continue
        if not pm:
            falhas.append({"doi":doi,"declarado":e["block"][:80],"motivo":"DOI não resolveu no PubMed"})
        else:
            doi_map[doi] = pm
        if (i+1)%20==0: print(f"esearch {i+1}/193", flush=True)
        time.sleep(0.36)
    print("resolvidos:", len(doi_map), "falhas:", len(falhas))
    # 2) esummary de tudo (anexo + matriz)
    all_pm = list(dict.fromkeys(list(doi_map.values()) + [p for p,_ in MATRIX_PMIDS]))
    meta={}
    for i in range(0, len(all_pm), 40):
        meta.update(esummary_batch(all_pm[i:i+40])); time.sleep(0.4)
    pmid_nao_existe = [p for p,_ in MATRIX_PMIDS if not meta.get(p,{}).get("titulo")]
    # 3) reúne registros do anexo
    registros=[]
    for e in ENTRIES:
        doi=e["doi"]; pm = doi_map.get(doi)
        if not pm: continue
        m = meta.get(pm,{})
        ano_real = (m.get("pubdate","")[:4])
        decl_aut = first_declared_author(e["block"])
        aut_ok = norm(decl_aut)[:5] and norm(decl_aut)[:5] in norm(m.get("autor1",""))
        ano_ok = (e["year"] and ano_real.startswith(e["year"][:4]))
        registros.append({"doi":doi,"pmid":pm,"declarado":decl_aut,"ano_decl":e["year"],
            "autor1_real":m.get("autor1",""),"ano_real":ano_real,"titulo":m.get("titulo",""),
            "journal":m.get("journal",""),"pubtypes":m.get("pubtypes",[]),
            "rotulo_ok":bool(aut_ok and ano_ok),"ja_na_b3": pm in vigentes,
            "block": e["block"][:220]})
    # 4) matriz (PMIDs diretos)
    pmids_do_anexo = set(doi_map.values())
    matriz=[]
    for p,label in MATRIX_PMIDS:
        m=meta.get(p,{})
        matriz.append({"pmid":p,"declarado":label,"autor1_real":m.get("autor1",""),
            "ano_real":m.get("pubdate","")[:4] if m else "",
            "titulo":m.get("titulo","") if m else "",
            "tambem_no_anexo": p in pmids_do_anexo, "ja_na_b3": p in vigentes})
    extras_matriz = [r for r in matriz if not r["tambem_no_anexo"]]
    json.dump({"registros_anexo":registros,"falhas":falhas,"matriz":matriz,
               "extras_matriz":extras_matriz,"pmid_nao_existe":pmid_nao_existe,
               "vigentes_qtd":len(vigentes)},
              open(OUT/"matriz_b3_g1.json","w"), ensure_ascii=False, indent=1)
    print("\n== RESUMO ==")
    print("anexo 193 -> resolvidos:", len(registros), "| já na B3:", sum(1 for r in registros if r['ja_na_b3']))
    print("rótulo divergente (autor ou ano):", sum(1 for r in registros if not r['rotulo_ok']))
    for r in registros:
        if not r['rotulo_ok']:
            print(f"  [DIF] doi={r['doi']} decl={r['declarado']}({r['ano_decl']}) real={r['autor1_real']}({r['ano_real']}) :: {r['titulo'][:70]}")
    print("falhas:", len(falhas))
    for f in falhas: print("  [FALHA]", f["doi"], "::", f["declarado"][:60], "::", f["motivo"])
    print("matriz: PMIDs não existentes:", pmid_nao_existe)
    print("matriz extras (não constam no anexo):", len(extras_matriz))
    for r in extras_matriz: print("  [EXTRA]", r["pmid"], r["declarado"], "->", r["autor1_real"], r["ano_real"], "::", r["titulo"][:60])

if __name__=="__main__":
    main()
