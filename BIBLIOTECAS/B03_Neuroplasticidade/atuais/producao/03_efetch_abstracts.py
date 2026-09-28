#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ato 1 (complemento): efetch dos abstracts dos PMIDs do corpus_pubmed.json.

- Le corpus_pubmed.json (saida do esearch+esummary por relevancia)
- Coleta PMIDs unicos
- Busca em lotes de 100 via efetch retmode=xml (com retry e pausa NCBI)
- Extrai por PMID: titulo, abstract (com rotulos de abstract estruturado),
  revista, ano, doi, autores, idioma, pubtypes, mesh terms (inclui especie:
  Humans/Mice/Rats/Cells, Cultured etc. — util para G2)
- Grava:
    abstracts_pubmed.json         — {pmid: registro completo}
    corpus_pubmed_completo.json   — corpus original + abstract/doi/autores/idioma/mesh
    log_efetch.json               — estatisticas e pendencias (sem abstract / nao retornado)

NAO decide nada: apenas traz o conteudo. G1 = ferramenta (este fetch com data/hora).
A leitura/veredito G3 e do avaliador, nunca deste script.
"""
import json, time, urllib.request, urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL = "biblioteca_canonica_b1"
LOTE = 100
ESPERA = 0.5          # segundos entre requisicoes (limite NCBI sem API key = 3/s)
TENTATIVAS = 4

BASE = Path(__file__).resolve().parent
CORPUS = BASE / "corpus" / "corpus_pubmed.json"
OUT_ABS = BASE / "corpus" / "abstracts_pubmed.json"
OUT_CORPUS = BASE / "corpus" / "corpus_pubmed_completo.json"
OUT_LOG = BASE / "corpus" / "log_efetch.json"


def buscar(url):
    for tent in range(1, TENTATIVAS + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": f"{TOOL}/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            print(f"  tentativa {tent} falhou: {e}")
            time.sleep(2 * tent)
    raise RuntimeError(f"falha apos {TENTATIVAS} tentativas: {url[:120]}")


def texto_abstract(art):
    partes = []
    for ab in art.findall(".//Abstract/AbstractText"):
        label = ab.get("Label")
        txt = "".join(ab.itertext()).strip()
        if not txt:
            continue
        partes.append(f"{label}: {txt}" if label else txt)
    return "\n".join(partes)


def parse_registro(rec):
    """rec = elemento PubmedArticle/BookArticle -> dict normalizado."""
    art = rec.find(".//MedlineCitation/Article")
    pmid_el = rec.find(".//MedlineCitation/PMID")
    if pmid_el is None or not pmid_el.text:
        pmid_el = rec.find(".//BookDocument/PMID")
    pmid = pmid_el.text.strip() if pmid_el is not None and pmid_el.text else None

    def txt(path, root=rec):
        el = root.find(path)
        return "".join(el.itertext()).strip() if el is not None else ""

    titulo = txt(".//Article/ArticleTitle", rec) or txt(".//BookDocument/Book/BookTitle", rec)
    revista = txt(".//Article/Journal/Title", rec) or txt(".//BookDocument/Book/BookTitle", rec)
    ano = txt(".//Article/Journal/JournalIssue/PubDate/Year", rec)
    if not ano:
        md = txt(".//Article/Journal/JournalIssue/PubDate/MedlineDate", rec)
        ano = md[:4] if md else ""

    abstract = texto_abstract(rec) if art is not None else ""

    autores = []
    for au in rec.findall(".//AuthorList/Author"):
        ln = au.find("LastName")
        ini = au.find("Initials")
        cn = au.find("CollectiveName")
        if ln is not None and ln.text:
            autores.append(f"{ln.text} {ini.text if ini is not None and ini.text else ''}".strip())
        elif cn is not None and cn.text:
            autores.append(cn.text.strip())

    idioma = txt(".//Article/Language", rec)

    pubtypes = [pt.text.strip() for pt in rec.findall(".//PublicationTypeList/PublicationType") if pt.text]

    doi = ""
    for eid in rec.findall(".//ELocationID"):
        if eid.get("EIdType") == "doi" and eid.text:
            doi = eid.text.strip()
    if not doi:
        for aid in rec.findall(".//PubmedData/ArticleIdList/ArticleId"):
            if aid.get("IdType") == "doi" and aid.text:
                doi = aid.text.strip()

    mesh = []
    for d in rec.findall(".//MeshHeadingList/MeshHeading/DescriptorName"):
        if d.text:
            mesh.append(d.text.strip())

    especie = []
    for m in mesh:
        ml = m.lower()
        if m in ("Humans", "Mice", "Rats", "Animals", "Swine", "Zebrafish", "Drosophila melanogaster",
                 "Caenorhabditis elegans", "Rabbits", "Dogs", "Cattle", "Sheep", "Chickens", "Guinea Pigs"):
            especie.append(m)
        elif "cells, cultured" in ml:
            especie.append("Cells, Cultured")

    return {
        "pmid": pmid,
        "titulo": titulo,
        "revista": revista,
        "ano": ano,
        "doi": doi,
        "autores": autores,
        "idioma": idioma,
        "pubtypes": pubtypes,
        "mesh": mesh,
        "especie_mesh": sorted(set(especie)),
        "abstract": abstract,
        "tem_abstract": bool(abstract),
    }


def main():
    corpus = json.loads(CORPUS.read_text(encoding="utf-8"))

    pmids = []
    for cid, blk in corpus.items():
        for a in blk.get("artigos", []):
            if a.get("pmid") and a["pmid"] not in pmids:
                pmids.append(a["pmid"])
    print(f"PMIDs unicos para efetch: {len(pmids)}")

    registros = {}
    for i in range(0, len(pmids), LOTE):
        lote = pmids[i:i + LOTE]
        url = (f"{EUTILS}/efetch.fcgi?db=pubmed&retmode=xml&tool={TOOL}"
               f"&id=" + ",".join(lote))
        print(f"lote {i//LOTE + 1}/{(len(pmids)-1)//LOTE + 1} ({len(lote)} pmids)...")
        raw = buscar(url)
        root = ET.fromstring(raw)
        for rec in root.iter():
            if rec.tag in ("PubmedArticle", "PubmedBookArticle"):
                reg = parse_registro(rec)
                if reg["pmid"]:
                    registros[reg["pmid"]] = reg
        time.sleep(ESPERA)

    sem_abstract, nao_retornados = [], []
    for p in pmids:
        if p not in registros:
            nao_retornados.append(p)
        elif not registros[p]["tem_abstract"]:
            sem_abstract.append(p)

    # corpus enriquecido (estrutura original intacta; adiciona campos)
    corpus_full = {}
    for cid, blk in corpus.items():
        novos = []
        for a in blk.get("artigos", []):
            reg = registros.get(a["pmid"])
            item = dict(a)
            if reg:
                item.update({
                    "doi": reg["doi"],
                    "autores": reg["autores"],
                    "idioma": reg["idioma"],
                    "pubtypes_full": reg["pubtypes"],
                    "mesh": reg["mesh"],
                    "especie_mesh": reg["especie_mesh"],
                    "abstract": reg["abstract"],
                    "tem_abstract": reg["tem_abstract"],
                })
            else:
                item.update({"abstract": "", "tem_abstract": False, "efetch": "NAO_RETORNA_DO"})
            novos.append(item)
        corpus_full[cid] = {"query": blk.get("query", ""), "artigos": novos}

    OUT_ABS.write_text(json.dumps(registros, ensure_ascii=False, indent=1), encoding="utf-8")
    OUT_CORPUS.write_text(json.dumps(corpus_full, ensure_ascii=False, indent=1), encoding="utf-8")

    log = {
        "etapa": "efetch_abstracts",
        "ferramenta": "NCBI eutils efetch retmode=xml",
        "g1_metodo": "eutils_automatico",
        "data_hora": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "pmids_solicitados": len(pmids),
        "registros_retornados": len(registros),
        "com_abstract": sum(1 for r in registros.values() if r["tem_abstract"]),
        "sem_abstract": sem_abstract,
        "nao_retornados_pelo_pubmed": nao_retornados,
        "observacao": "Sem abstract geralmente = editorial/carta/erratum/artigo antigo ou registro sem resumo. "
                      "Nao impede G1 (PMID existe); G3 e que exige leitura — usar full text ou marcar NAO_LOCALIZADO.",
    }
    OUT_LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nretornados: {len(registros)}/{len(pmids)}")
    print(f"com abstract: {log['com_abstract']}")
    print(f"sem abstract: {len(sem_abstract)} -> {sem_abstract[:15]}")
    print(f"nao retornados: {len(nao_retornados)} -> {nao_retornados[:15]}")


if __name__ == "__main__":
    main()
