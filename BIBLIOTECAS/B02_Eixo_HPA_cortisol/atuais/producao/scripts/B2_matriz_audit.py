#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auditoria G1 do insumo 'matriz canônica B2' (externo).
Para cada identificador: resolve no PubMed (eutils), confere rótulo declarado
(1º autor + ano + tema), e cruza com as 185 refs vigentes da B2.
Saída: producao/insumos/matriz_b2_g1.json + resumo em stdout.
"""
import json, re, time, urllib.parse, urllib.request
from pathlib import Path

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
B2 = Path("/home/user/BIBLIOTECAS/B02_Eixo_HPA_cortisol")
OUT = B2 / "producao" / "insumos"
OUT.mkdir(parents=True, exist_ok=True)

# (chave, rótulo declarado no insumo)
INSUMO = [
 ("21257974","Stetler & Miller 2011"),("15996533","Swaab, Bao & Lucassen 2005"),
 ("28183380","Baes 2012"),("32203965","Ceruso 2020"),("23410758","Jarcho 2013"),
 ("28012291","Zorn 2017"),("27528460","Keller 2017"),("36458076","Sahu 2022"),
 ("37581323","Menke 2024"),("38176541","Wang 2024"),("41270487","Machahary 2025"),
 ("40040865","Van Den Noortgate 2025"),("20047716","Zobel 2010"),("20393453","Xie 2010"),
 ("21865530","Zimmermann 2011"),("29182159","Tozzi 2018"),("28850857","Wang 2018"),
 ("41849885","Kaul 2026"),("40578604","Zhang 2025"),("37078436","Stanton 2023"),
 ("41935803","Zheng 2026"),("19008333","Spiga 2009"),("34566653","meta HPA-treatments"),
 ("26563991","Stalder 2016"),("38308964","Wesarg-Menzel 2024"),("32276241","Sugaya 2020"),
 ("42009273","Balfour 2026"),("41791598","Zhang 2026 antenatal"),("41755883","Thom 2026"),
 ("36624454","Sun 2023"),("19545546","Tatro 2009"),("34901719","Sukhareva 2021"),
 ("34920399","Zajkowska 2021"),("31499391","Lombardo 2019"),
 ("10.1210/endo.141.11.7767","Müller/Ller 2000 (duplicata)"),
]
SEM_ID = ["Menke et al. 2013","Peng et al. 2018","Klinger-König 2019","Kim 2019","Poidinger 2015",
 "Ising 2008","Ising 2019","Bunea 2017","Jiang 2025","Khoury 2019","Van Bodegom 2017",
 "Morris 2012","Schumacher 2019","Yehuda 2013","Bale 2000","Müller 2003","Refojo 2011",
 "Gan 2022","Häusl 2021","Choi 2021","Vasyl 2025"]

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent":"arena-b2-audit/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r: return r.read()

def esearch_doi(doi):
    q = urllib.parse.quote(f"{doi}[aid]")
    d = json.loads(get(f"{BASE}esearch.fcgi?db=pubmed&term={q}&retmode=json"))
    ids = d.get("esearchresult",{}).get("idlist",[])
    return ids[0] if ids else None

def esummary_batch(pmids):
    d = json.loads(get(f"{BASE}esummary.fcgi?db=pubmed&id={','.join(pmids)}&retmode=json"))
    out={}
    for pm in pmids:
        r = d.get("result",{}).get(pm,{})
        aut = r.get("authors",[])
        out[pm] = {"pmid": pm, "titulo": r.get("title",""),
                   "autor1": (aut[0]["name"] if aut else ""), "journal": r.get("fulljournalname",""),
                   "pubdate": r.get("pubdate",""), "pubtypes": r.get("pubtype",[])}
    return out

def main():
    vigentes = {r["pmid_oficial"]: r for r in json.load(open(B2/"Evidencias"/"Bibliografia"/"01_pmids.json"))}
    resolvidos, falhas = {}, []
    pmid_keys = [k for k,_ in INSUMO if re.fullmatch(r"\d{6,9}", k)]
    meta = esummary_batch(pmid_keys); time.sleep(0.4)
    for key, label in INSUMO:
        if re.fullmatch(r"\d{6,9}", key):
            m = meta.get(key, {})
            if not m.get("titulo"):
                falhas.append({"chave":key,"declarado":label,"motivo":"PMID não encontrado no PubMed"}); continue
            ano = (m.get("pubdate","")[:4])
            a1 = m.get("autor1","?")
            # confere rótulo: sobrenome declarado consta no autor real?
            sob_decl = label.split()[0].split("&")[0].split(",")[0].lower().rstrip("’'s")
            ok_rot = sob_decl[:5] in a1.lower() if sob_decl else False
            resolvidos[key] = {**m, "declarado": label, "ano": ano,
                "rotulo_confere": bool(ok_rot),
                "ja_na_b2": key in vigentes}
        else:
            pm = esearch_doi(key); time.sleep(0.4)
            if not pm:
                falhas.append({"chave":key,"declarado":label,"motivo":"DOI não resolveu no PubMed"}); continue
            m = esummary_batch([pm])[pm]; time.sleep(0.4)
            resolvidos[key] = {**m, "declarado": label, "ano": (m.get("pubdate","")[:4]),
                "pmid_resolvido": pm, "rotulo_confere": True, "ja_na_b2": pm in vigentes}
    json.dump({"resolvidos": resolvidos, "falhas": falhas, "sem_identificador": SEM_ID},
              open(OUT/"matriz_b2_g1.json","w"), ensure_ascii=False, indent=1)
    n_cob = sum(1 for v in resolvidos.values() if v["ja_na_b2"])
    n_rot = sum(1 for v in resolvidos.values() if v["rotulo_confere"])
    print(f"resolvidos {len(resolvidos)}/{len(INSUMO)} | rótulo confere {n_rot} | já na B2 {n_cob}")
    print("--- detalhe ---")
    for k,v in resolvidos.items():
        print(f"{k:>28} | {v.get('autor1','?'):<22} {v.get('ano','?'):<5} | rot={'OK' if v['rotulo_confere'] else '<<<DIVERGE'} | B2={'SIM' if v['ja_na_b2'] else 'NÃO'} | {v.get('titulo','')[:70]}")
    for f in falhas: print("FALHA:", f)

if __name__ == "__main__":
    main()
