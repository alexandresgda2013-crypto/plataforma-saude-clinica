#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P-7 [AT] B1 — Etapa 1: resolve chaves do insumo (PMID/DOI) -> PMID real via eutils,
deduplica contra as 188 refs vigentes, baixa metadados+abstract e exporta matriz_b1_at_final.
Rejeitados ficam registrados com motivo (trilha de auditoria).
"""
import json, re, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
INSUMOS = "/home/user/BIBLIOTECAS/B01_Neuroinflamacao/producao/insumos"
OUT = INSUMOS + "/matriz_b1_at_final.json"

G1 = json.load(open(f"{INSUMOS}/matriz_b1_g1.json"))
BIB = "/home/user/BIBLIOTECAS/B01_Neuroinflamacao/Evidencias/Bibliografia/01_pmids.json"
PMIDS_VIGENTES = {r["pmid_oficial"] for r in json.load(open(BIB)) if r.get("pmid_oficial")}

# ---- listas de decisão (trilha auditável) ----
DROP_FALSO_POSITIVO = {"1110775", "25797247", "30156409", "30563872", "34864233"}
DROP_ESCOPO = {
    "10.3389/fncel.2022.915969": "TCE/TBI — fora de escopo permanente",
    "35669106": "TCE/TBI — fora de escopo permanente",
    "10.1007/s00401-022-02528-y": "Alzheimer — outra condição",
    "36481964": "Alzheimer — outra condição",
    "10.1073/pnas.1722041115": "esclerose múltipla — outra condição",
    "29895691": "esclerose múltipla — outra condição",
    "10.1016/j.bbi.2022.10.022": "minociclina = intervenção; incremento baixo (P20 cautela)",
    "36332817": "minociclina = intervenção; incremento baixo (P20 cautela)",
}
DROP_PODA_REDUNDANCIA = {
    "10.1515/revneuro-2022-0047": "revisão KP redundante (coberta por Savitz 2019/Stone 2023/Bertollo 2025)",
    "10.1038/s41423-021-00740-6": "revisão genérica inflamassoma+morte — corpus já cobre fundamentação",
    "10.1016/j.tibs.2022.10.002": "revisão genérica NLRP3 regulação — corpus já cobre fundamentação",
}
JA_COBERTOS = {"20015486", "28122130", "32113908", "31326932", "28939116", "28445690"}
DROP_DUP_BIBLIO = {"10.1038/s41380-019-0474-5": "duplicata bibliográfica de 31427752 (mesmo paper, Liu 2019 Mol Psychiatry)"}

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "arena-b1-audit/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def esearch_doi(doi):
    q = urllib.parse.quote(f"{doi}[aid]")
    xml = get(f"{BASE}esearch.fcgi?db=pubmed&term={q}&retmode=json")
    d = json.loads(xml)
    ids = d.get("esearchresult", {}).get("idlist", [])
    return ids[0] if ids else None

def efetch(pmids):
    xml = get(f"{BASE}efetch.fcgi?db=pubmed&id={','.join(pmids)}&retmode=xml")
    root = ET.fromstring(xml)
    out = {}
    for art in root.iter("PubmedArticle"):
        med = art.find("MedlineCitation")
        pmid = med.findtext("PMID")
        a = med.find("Article")
        title = "".join(a.find("ArticleTitle").itertext()) if a.find("ArticleTitle") is not None else ""
        jour_full = a.findtext("Journal/Title", "")
        autores = [f"{au.findtext('LastName','')} {au.findtext('Initials','')}".strip()
                   for au in a.iter("Author")][:8]
        autores = [x for x in autores if x]
        y = (a.findtext("Journal/JournalIssue/PubDate/Year")
             or a.findtext("Journal/JournalIssue/PubDate/MedlineDate", "")[:4])
        pubtypes = [pt.text for pt in a.iter("PublicationType")]
        species = [mh.findtext("DescriptorName") for mh in med.iter("MeshHeading")
                   if mh.findtext("DescriptorName") in ("Humans", "Animals")]
        abstr = " ".join("".join(x.itertext()) for x in a.findall("Abstract/AbstractText"))[:1500]
        ids = {aid.text: aid.get("IdType") for aid in art.iter("ArticleId")}
        doi = next((k for k, t in ids.items() if t == "doi"), "")
        out[pmid] = {"pmid": pmid, "titulo": title, "journal_full": jour_full, "ano": y,
                     "autores": autores, "pubtypes": pubtypes, "species": species,
                     "abstract": abstr, "doi": doi}
    return out

def main():
    keep, rejeit = [], []
    for key, rec in G1.items():
        if key in DROP_FALSO_POSITIVO:
            rejeit.append({"chave": key, "motivo": "FALSO POSITIVO — PMID não corresponde ao paper declarado"}); continue
        if key in DROP_ESCOPO:
            rejeit.append({"chave": key, "motivo": DROP_ESCOPO[key]}); continue
        if key in DROP_PODA_REDUNDANCIA:
            rejeit.append({"chave": key, "motivo": DROP_PODA_REDUNDANCIA[key]}); continue
        if key in JA_COBERTOS:
            rejeit.append({"chave": key, "motivo": "já presente na B1 vigente (mesmo PMID)"}); continue
        if key in DROP_DUP_BIBLIO:
            rejeit.append({"chave": key, "motivo": DROP_DUP_BIBLIO[key]}); continue
        keep.append((key, rec))

    print(f"KEEP candidatos: {len(keep)} | REJEITADOS: {len(rejeit)}")
    # resolve DOI->PMID
    resolved = []
    for key, rec in keep:
        if re.fullmatch(r"\d{6,9}", key):
            resolved.append({"chave": key, "pmid": key})
        else:
            pm = esearch_doi(key)
            time.sleep(0.4)
            if not pm:
                rejeit.append({"chave": key, "motivo": "DOI não resolveu no PubMed nesta etapa"}); continue
            resolved.append({"chave": key, "pmid": pm})

    # dedupe contra vigentes e internos
    vistos, final = set(), []
    for r in resolved:
        if r["pmid"] in PMIDS_VIGENTES:
            rejeit.append({"chave": r["chave"], "pmid": r["pmid"], "motivo": "resolveu para PMID já presente na B1 vigente"}); continue
        if r["pmid"] in vistos:
            rejeit.append({"chave": r["chave"], "pmid": r["pmid"], "motivo": "PMID duplicado dentro da própria leva [AT]"}); continue
        vistos.add(r["pmid"]); final.append(r)

    print(f"APÓS DEDUPE: {len(final)} entrantes")
    meta = efetch([r["pmid"] for r in final])
    for r in final:
        r.update(meta.get(r["pmid"], {}))
    json.dump({"entrantes": final, "rejeitados": rejeit}, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"gravado {OUT}")
    for r in final:
        a1 = r.get("autores", ["?"])[0]
        print(f'{r["chave"]:>36} -> {r["pmid"]:>9} | {a1:<22} {r.get("ano","?")} | {r.get("titulo","")[:80]}')

if __name__ == "__main__":
    main()
