#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ato 1b: busca dirigida por ferramenta para as ancoras [REF_MODULO_xx] do GPM v3.

Para cada rotulo (Autor_Ano) citado nas ancoras do GPM:
  esearch PubMed: sobrenome[au] + ano[dp] + topico, sort=relevance, top 3
Depois efetch (xml) dos PMIDs novos (mesmo parser do 03_).
Saidas:
  corpus_ancoras_pubmed.json  — {rotulo: {query, candidatos:[registro+abstract]}}
  log_de_busca_ancoras.json   — rotulo -> query -> pmids
  abstracts_pubmed.json       — ATUALIZADO com os registros novos
G1 = ferramenta (data/hora no log). Os 3 candidatos sao para o avaliador (G3),
nao sao escolha automatica.
"""
import json, time, urllib.request, urllib.parse, sys
from pathlib import Path
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent))
import importlib.util
spec = importlib.util.spec_from_file_location("ef", Path(__file__).resolve().parent / "03_efetch_abstracts.py")
ef = importlib.util.module_from_spec(spec); spec.loader.exec_module(ef)

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
BASE = Path(__file__).resolve().parent
CORPUS_DIR = BASE / "corpus"

# rotulo -> (termo de busca). Sobrenome[au] AND ano[dp] AND (topico)
ALVOS = [
    ("Dantzer_2008",        "Dantzer[au] AND 2008[dp] AND (inflammation AND (sickness OR depression OR behavior) AND brain)"),
    ("Miller_Raison_2016",  "Miller[au] AND Raison[au] AND 2016[dp] AND (inflammation AND depression AND (evolutionary OR treatment target))"),
    ("Capuron_Miller_2011", "Capuron[au] AND Miller[au] AND 2011[dp] AND (immune AND brain AND (neuropsychopharmacology OR signaling OR behavior))"),
    ("Banks_2015",          "Banks[au] AND 2015[dp] AND (cytokine AND (blood-brain barrier OR brain) AND neuroimmune)"),
    ("Fiebich_2018",        "Fiebich[au] AND 2018[dp] AND (microglia OR cytokine OR neuroinflammation)"),
    ("Heneka_2017_NLRP3",   "Heneka[au] AND 2017[dp] AND (NLRP3 OR inflammasome OR innate immunity)"),
    ("Kelley_2019",         "Kelley[au] AND 2019[dp] AND (inflammation AND (behavior OR sickness OR depression) AND cytokine)"),
    ("Swanson_2019",        "Swanson[au] AND 2019[dp] AND (NLRP3 AND inflammasome AND (review OR regulation OR activation))"),
    ("Sekar_2016",          "Sekar[au] AND 2016[dp] AND (complement C4 AND schizophrenia)"),
    ("Stevens_2007",        "Stevens[au] AND 2007[dp] AND (complement C1q AND synapse AND (elimination OR pruning))"),
    ("Serhan_SPM",          "Serhan[au] AND (2014[dp] OR 2017[dp] OR 2018[dp]) AND (resolvins OR pro-resolving OR specialized pro-resolving mediators)"),
    ("Schwarcz_quinurenina","Schwarcz[au] AND (kynurenine OR kynurenic acid OR quinolinic acid) AND (brain OR CNS)"),
    ("Dowlati_2010",        "Dowlati[au] AND 2010[dp] AND (meta-analysis AND cytokines AND depression)"),
    ("Haapakoski_2015",     "Haapakoski[au] AND 2015[dp] AND ((meta-analysis OR inflammation OR cytokines) AND depression)"),
    ("Osimo_2020",          "Osimo[au] AND 2020[dp] AND (inflammatory markers AND depression AND meta-analysis)"),
    ("Goldsmith_2016",      "Goldsmith[au] AND 2016[dp] AND (cytokine AND meta-analysis AND (depression OR psychiatric))"),
    ("Howren_2009",         "Howren[au] AND 2009[dp] AND (C-reactive protein OR IL-6 OR inflammation AND depression)"),
    ("Raison_2013",         "Raison[au] AND 2013[dp] AND (infliximab OR TNF AND depression AND (randomized OR treatment-resistant))"),
    ("Capuron_2002",        "Capuron[au] AND 2002[dp] AND (cytokine AND (interferon) AND (depression OR mood OR HPA))"),
    ("Bull_2009",           "Bull[au] AND (2008[dp] OR 2009[dp]) AND (IL-6 OR interleukin-6 OR polymorphism OR depression)"),
    ("Voorhees_2013",       "Voorhees[au] AND 2013[dp] AND (stress AND immune AND (chronic OR glucocorticoid))"),
    ("RoseJohn_IL6",        "Rose-John[au] AND (IL-6 OR interleukin-6) AND (trans-signaling OR review)"),
    ("Sublette_2011",       "Sublette[au] AND 2011[dp] AND (kynurenine OR tryptophan OR omega-3) AND (suicide OR depression)"),
    ("Leighton_2018",       "Leighton[au] AND 2018[dp] AND (neuroinflammation OR microglia OR cytokine) AND (depression OR mood)"),
    ("Paolicelli_microglia","Paolicelli[au] AND (synaptic pruning OR microglia AND brain development)"),
    ("Norden_2015",         "Norden[au] AND 2015[dp] AND (microglia AND (priming OR aging OR stress))"),
    ("Liddelow_2017",       "Liddelow[au] AND 2017[dp] AND (reactive astrocytes OR A1 astrocytes)"),
    ("Menard_2017",         "Menard[au] AND 2017[dp] AND (social stress AND (neurovascular OR blood-brain barrier OR depression))"),
    ("Capuron_citocina",    "Capuron[au] AND (cytokine AND (brain OR behavior OR depression)) AND (review[pt] OR 2000:2005[dp])"),
    ("Goshen_IL1",          "Goshen[au] AND (interleukin-1 OR IL-1) AND (hippocampus OR memory OR depression)"),
    ("Ransohoff_perivascular","Ransohoff[au] AND (perivascular macrophages OR innate immune cells CNS OR neuroinflammation)"),
    ("Backlund_2011",       "Backlund[au] AND 2011[dp] AND (C-reactive protein OR CRP OR inflammation) AND (bipolar OR depression)"),
    ("Klengel_2013",        "Klengel[au] AND 2013[dp] AND (FKBP5 AND (trauma OR methylation OR demethylation))"),
    ("Hung_TLR4",           "Hung[au] AND (TLR4 OR toll-like receptor 4) AND (depression OR stress OR microglia)"),
    ("MR_CRP",              "(mendelian randomization[tiab]) AND (C-reactive protein OR CRP) AND (depression OR depressive)"),
    ("Capuron_2003",        "Capuron[au] AND 2003[dp] AND (cytokine OR interferon) AND (depression OR mood)"),
    ("Meaney_epigenetica",  "(Meaney[au] OR Szyf[au] OR McGowan[au]) AND (epigenetic OR methylation OR maternal care) AND (glucocorticoid receptor OR hippocampus OR stress)"),
    ("Raison_Miller_HPA",   "(Raison[au] AND Miller[au]) AND (HPA OR glucocorticoid OR cortisol) AND (inflammation OR cytokine)"),
    ("Dantzer_quinurenina", "Dantzer[au] AND (kynurenine OR indoleamine 2,3-dioxygenase OR IDO) AND (depression OR inflammation)"),
    ("Serhan_resolucao",    "Serhan[au] AND (resolution of inflammation OR pro-resolving mediators) AND (review[pt])"),
    ("Steiner_2011",        "Steiner[au] AND 2011[dp] AND (microglia OR neuroinflammation) AND (depression OR schizophrenia OR postmortem)"),
    ("Setiawan_2015",       "Setiawan[au] AND 2015[dp] AND (TSPO OR translocator protein OR PET) AND depression"),
    ("Holmes_2018",         "Holmes[au] AND 2018[dp] AND (TSPO OR translocator protein OR neuroinflammation) AND (depression OR PET)"),
    ("CRP_meta",            "(meta-analysis[pt]) AND (C-reactive protein OR CRP) AND (depression OR depressive disorder)"),
    ("CRP_subgroup",        "(infliximab OR anti-TNF OR anti-inflammatory) AND (CRP OR C-reactive protein) AND (subgroup OR responders) AND depression"),
    ("meta_ansiedade_2026", "(anxiety[ti] OR anxiety disorders[mesh]) AND (meta-analysis[pt]) AND (inflammation OR cytokine OR CRP)"),
    ("Enache_meta_2019",    "Enache[au] AND (inflammation OR cytokine) AND (depression OR aging)"),
    ("setola_TSPO",         "(TSPO OR translocator protein) AND (PET OR imaging) AND (polymorphism OR rs6971 OR neuroinflammation) AND (review[pt] OR method*)"),
    ("Haythornthwaite_confunding","(inflammation OR cytokine) AND (depression) AND (confounding OR confounders)"),
]


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "biblioteca_canonica_b1/1.0"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.load(r)


def main():
    abstracts = json.loads((CORPUS_DIR / "abstracts_pubmed.json").read_text(encoding="utf-8"))
    resultado, log = {}, []
    todos_pmids_novos = []

    for rotulo, termo in ALVOS:
        url = (f"{EUTILS}/esearch.fcgi?db=pubmed&retmode=json&retmax=3&sort=relevance&tool=biblioteca_canonica_b1&term="
               + urllib.parse.quote(termo))
        try:
            ids = get_json(url)["esearchresult"].get("idlist", [])
        except Exception as e:
            ids = []
            print(f"{rotulo}: ERRO {e}")
        print(f"{rotulo:24s} -> {ids}")
        resultado[rotulo] = {"query": termo, "pmids": ids}
        log.append({"ancora": rotulo, "query": termo, "pmids": ids})
        for p in ids:
            if p not in abstracts and p not in todos_pmids_novos:
                todos_pmids_novos.append(p)
        time.sleep(0.4)

    print(f"\nPMIDs novos para efetch: {len(todos_pmids_novos)}")
    for i in range(0, len(todos_pmids_novos), 100):
        lote = todos_pmids_novos[i:i + 100]
        raw = ef.buscar(f"{EUTILS}/efetch.fcgi?db=pubmed&retmode=xml&tool=biblioteca_canonica_b1&id=" + ",".join(lote))
        root = ET.fromstring(raw)
        for rec in root.iter():
            if rec.tag in ("PubmedArticle", "PubmedBookArticle"):
                reg = ef.parse_registro(rec)
                if reg["pmid"]:
                    abstracts[reg["pmid"]] = reg
        time.sleep(0.5)

    # monta corpus de ancoras com registros completos
    for rotulo, blk in resultado.items():
        cands = []
        for p in blk["pmids"]:
            r = abstracts.get(p)
            if r:
                cands.append({k: r[k] for k in ("pmid", "titulo", "revista", "ano", "doi", "autores",
                                                 "idioma", "pubtypes", "especie_mesh", "abstract", "tem_abstract")})
        blk["candidatos"] = cands

    (CORPUS_DIR / "corpus_ancoras_pubmed.json").write_text(
        json.dumps(resultado, ensure_ascii=False, indent=1), encoding="utf-8")
    (CORPUS_DIR / "abstracts_pubmed.json").write_text(
        json.dumps(abstracts, ensure_ascii=False, indent=1), encoding="utf-8")
    logdoc = {
        "etapa": "busca_dirigida_ancoras_gpm",
        "ferramenta": "NCBI eutils esearch (sort=relevance, retmax=3) + efetch",
        "g1_metodo": "eutils_automatico",
        "data_hora": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "n_rotulos": len(ALVOS),
        "pmids_novos_baixados": len(todos_pmids_novos),
        "buscas": log,
        "observacao": "3 candidatos por ancora sao sugestoes da ferramenta; G3 (avaliador) confirma leitura. "
                      "Rotulos sem volta ou sem o artigo certo devem ser recasados a mao com mais termos.",
    }
    (CORPUS_DIR / "log_de_busca_ancoras.json").write_text(
        json.dumps(logdoc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nTotal registros no abstracts_pubmed.json: {len(abstracts)}")


if __name__ == "__main__":
    main()
