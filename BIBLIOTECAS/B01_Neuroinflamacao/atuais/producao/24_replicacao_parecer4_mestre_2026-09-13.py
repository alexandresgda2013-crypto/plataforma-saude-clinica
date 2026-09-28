#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 24 — Réplica do parecer nº 4 do Auditor-Mestre (2026-09-13)
Objeto: PARECER_PACOTE_B1_V6_VERIFICADO_2026-09-13.md
Mede na CANÔNICA V7 (não na V6 que ele recebeu):
  A) §5 dele: tokens com DOIS classificadores [XX] simultâneos (lista dele tinha 12 na V6)
  B) §5 dele: 3 tokens temáticos "sem autor" (Epi_2019, Primingprinc_2018, Psoriase_2025)
  C) V-16 proposta por ele: H1 × artefato_rotulo(L5) × nome do arquivo × rótulo no manifesto
Camadas medidas separadamente:
  - prosa        : (Autor et al., ANO)[XX]  — só [XX] adjacente a citação
  - indice_inline: linhas itálicas *Token[XX] | ...* dentro dos blocos (TitleCase)
  - apendice     : linhas após '## APÊNDICE DE CORPUS' (CAIXA_ALTA)
Saída: JSON na mesma pasta. Sem escrita em nenhum artefato canônico (trilha read-only).
"""
import re, json, hashlib, os, unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
ATUAIS = os.path.dirname(BASE)
CAN = os.path.join(ATUAIS, "B1 NEUROINFLAMAÇÃO V7 CANONICA.md")
MAN = os.path.join(ATUAIS, "Evidencias", "Bibliografia", "_manifesto_biblioteca.json")

txt = open(CAN, encoding="utf-8").read()
lines = txt.splitlines()

# ---------- localizar início do apêndice e seu FIM (rev.1: corta no próximo cabeçalho '## ') ----------
# rev.0 mediu tudo após o cabeçalho do apêndice — incluindo o REGISTRO narrativo (cita tokens antigos
# como 'MEHTA_2020[MA]' em texto histórico) e os METADADOS. Falso positivo meu em MEHTA: corrigido.
idx_ap = next((i for i, l in enumerate(lines) if "APÊNDICE DE CORPUS" in l.upper()), None)
idx_ap_fim = len(lines)
if idx_ap is not None:
    for j in range(idx_ap + 1, len(lines)):
        if lines[j].startswith("## "):
            idx_ap_fim = j
            break

# ---------- extratores ----------
TOK = re.compile(r"([A-Za-zÀ-ÿ0-9][A-Za-zÀ-ÿ0-9_\-]*?)\[(EC|ML|OB|MA)\]")
CIT = re.compile(r"\(([A-ZÀ-Þ][^()]*?et al\.[^()]*?\d{4}[a-z]?(?:\s*&[^()]*)?)\)\s*(?:\[(EC|ML|OB|MA)\])?")

def norm(tok):
    t = tok.upper()
    return t

prosa, indice, apendice = {}, {}, {}
prosa_raw = []

for i, l in enumerate(lines):
    in_ap = idx_ap is not None and idx_ap < i < idx_ap_fim
    if in_ap:
        for m in TOK.finditer(l):
            apendice.setdefault(norm(m.group(1)), set()).add(m.group(2))
    else:
        # linha índice inline: itálica com |
        if l.strip().startswith("*") and "|" in l and TOK.search(l):
            for m in TOK.finditer(l):
                indice.setdefault(norm(m.group(1)), set()).add(m.group(2))
        # prosa: varre a linha procurando citação seguida de [XX]
        for m in TOK.finditer(l):
            ini = m.start()
            janela = l[max(0, ini-120):ini]
            if re.search(r"\)\s*$", janela) and re.search(r"\([^()]*\d{4}[a-z]?\s*\)\s*$", janela):
                prosa.setdefault(norm(m.group(1)), set()).add(m.group(2))
                prosa_raw.append((i+1, m.group(1), m.group(2)))

def ambiguos(d):
    out = {}
    for k, v in d.items():
        vv = set(v)
        if len(vv) > 1:
            out[k] = sorted(vv)
    return dict(sorted(out.items()))

# globais (caixa-insensível), por camada e união
glob = {}
for d in (prosa, indice, apendice):
    for k, v in d.items():
        glob.setdefault(k, set()).update(v)

lista_mestre_v6 = ["BULL_2009","KLENGEL_2013","STEINER_2011","SUBLETTE_2011","SETIAWAN_2015",
                   "HOLMES_2018","MEHTA_2020","LEVY_2018","TEELING_2013",
                   "EPI_2019","PRIMINGPRINC_2018","PSORIASE_2025"]

# mapeamento dos tokens dele para a V7 (nomes reais encontrados)
aliases_v7 = {
    "STEINER_2011": ["STEINER_2011_QUIN", "STEINER_2011"],
    "LEVY_2018": ["SERHAN_LEVY_2018", "LEVY_2018"],
    "TEELING_2013": ["PERRY_TEELING_2013", "TEELING_2013"],
    "EPI_2019": ["STRESS_EPI_2019", "EPI_2019"],
    "PRIMINGPRINC_2018": ["PRIMINGPRINC_2018"],
}
def lookup(tok):
    cands = aliases_v7.get(tok, [tok])
    ach = {}
    for c in cands:
        if c in glob:
            ach[c] = sorted(glob[c])
    return ach

res_mestre = {t: lookup(t) for t in lista_mestre_v6}

# ---------- V-16 ----------
h1 = lines[0].strip()
rotulo_linha = next((l for l in lines[:10] if "artefato_rotulo" in l), "")
m = re.search(r"artefato_rotulo:\**\s*(CAN[ÔO]NICA\s+V\d+)", rotulo_linha, re.I)
rotulo_l5 = m.group(1).upper().replace("Ô","O") if m else None
h1_tok = re.search(r"V(\d+)", h1)
arq = os.path.basename(CAN)
arq_tok = re.search(r"V(\d+)", arq)
man = json.load(open(MAN, encoding="utf-8"))
man_bib = man.get("biblioteca") or man.get("artefato_rotulo") or ""
man_tok = re.search(r"V(\d+)", man_bib)
v16 = {
    "H1_linha1": h1[:70],
    "H1_versao": "V"+h1_tok.group(1) if h1_tok else None,
    "artefato_rotulo_L5": (rotulo_l5 or "")[:40],
    "rotulo_versao": re.search(r"V(\d+)", rotulo_l5 or ""),
    "nome_arquivo": arq,
    "arquivo_versao": "V"+arq_tok.group(1) if arq_tok else None,
    "manifesto_biblioteca": man_bib,
    "manifesto_versao": ("V"+man_tok.group(1)) if man_tok else None,
    "versao_manifesto_campo": man.get("versao_manifesto") or man.get("versao"),
}
v16["rotulo_versao"] = "V"+v16["rotulo_versao"].group(1) if v16["rotulo_versao"] else None
vers = {v16["H1_versao"], v16["rotulo_versao"], v16["arquivo_versao"], v16["manifesto_versao"]}
v16["V16_resultado"] = "OK — 4 superficies concordam" if len(vers) == 1 and None not in vers else f"DIVERGENCIA: {sorted(x for x in vers if x)}"

# ---------- tokens temáticos (sem sobrenome de autor) ----------
tematicos = {}
for t in ["STRESS_EPI_2019", "PRIMINGPRINC_2018", "PSORIASE_2025"]:
    ocorr = [(i+1, lines[i].strip()[:100], ("apendice" if (idx_ap is not None and idx_ap < i < idx_ap_fim) else ("indice_inline" if idx_ap is not None and i < idx_ap else "metadados"))) for i, l in enumerate(lines) if t.lower() in l.lower()]
    tematicos[t] = {"classificadores_global": sorted(glob.get(t, [])), "ocorrencias": ocorr}

# fichas correspondentes na evidência (rev.1: a chave de ID é id_referencia_interna / ids_referencia_interna)
refs_ids = set()
def coleta_ids(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ("id_referencia_interna", "ref_id", "id") and isinstance(v, str):
                refs_ids.add(v.upper())
            elif k == "ids_referencia_interna" and isinstance(v, list):
                for x in v:
                    if isinstance(x, str): refs_ids.add(x.upper())
            coleta_ids(v)
    elif isinstance(o, list):
        for x in o: coleta_ids(x)
for f in ["01_pmids.json","02_meta_analises.json","03_ensaios_clinicos.json"]:
    try:
        coleta_ids(json.load(open(os.path.join(ATUAIS,"Evidencias","Bibliografia",f), encoding="utf-8")))
    except Exception as e:
        pass

tematicos_ficha = {}
for t in ["STRESS_EPI_2019","PRIMINGPRINC_2018","PSORIASE_2025"]:
    cand = [r for r in refs_ids if t.split("_")[0] in r or t in r]
    tematicos_ficha[t] = cand
# rev.1 — fichas por AUTOR/TÍTULO (prosa L346 cita "(Herman et al., 2018)"; L354 "(Keenan et al., 2025)")
def fichas_por_sobrenome(sob):
    hits = []
    for f in ["01_pmids.json","02_meta_analises.json","03_ensaios_clinicos.json"]:
        try:
            d = json.load(open(os.path.join(ATUAIS,"Evidencias","Bibliografia",f), encoding="utf-8"))
        except Exception:
            continue
        for it in (d if isinstance(d, list) else []):
            aut = str(it.get("autores","")).upper()
            tit = str(it.get("titulo_artigo","")).upper()
            rid = it.get("id_referencia_interna") or (it.get("ids_referencia_interna") or [None])[0]
            if sob in aut or sob in tit:
                hits.append((f, rid, str(it.get("autores",""))[:70], str(it.get("pmid_oficial","")), str(it.get("desenho_estudo",""))[:50]))
    return hits
cand_keenan = fichas_por_sobrenome("KEENAN")
cand_herman = fichas_por_sobrenome("HERMAN")
cand_mehta  = fichas_por_sobrenome("MEHTA")

out = {
  "trilha": "24_replicacao_parecer4_mestre_2026-09-13",
  "rev": "rev.1 — apêndice cortado no próximo cabeçalho '## ' (rev.0 varria REGISTRO narrativo e METADADOS: falso positivo MEHTA_2020{EC,MA,OB} confessado e corrigido); fichas buscadas por id_referencia_interna e por autor/título",
  "canonica_sha256": hashlib.sha256(open(CAN,'rb').read()).hexdigest(),
  "alvo": "B1 NEUROINFLAMAÇÃO V7 CANONICA.md",
  "A_tokens_dois_classificadores": {
     "na_V7_por_camada": {
        "prosa": ambiguos(prosa),
        "indice_inline": ambiguos(indice),
        "apendice": ambiguos(apendice),
        "global_uniao": ambiguos(glob),
     },
     "lista_mestre_V6_x_estado_V7": res_mestre,
  },
  "B_tokens_tematicos": {"classificadores": tematicos, "fichas_candidatas_por_token": tematicos_ficha,
                          "fichas_por_autor_titulo": {"KEENAN": cand_keenan, "HERMAN": cand_herman, "MEHTA": cand_mehta}},
  "C_V16_4_superficies": v16,
  "contagens": {"tokens_indice_inline": len(indice), "tokens_apendice": len(apendice),
                "tokens_prosa_com_classe": len(prosa)},
}
p = os.path.join(BASE, "24_replicacao_parecer4_mestre_2026-09-13.json")
json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(out["C_V16_4_superficies"], ensure_ascii=False, indent=1))
print("=== ambiguos por camada (V7) ===")
for k, v in out["A_tokens_dois_classificadores"]["na_V7_por_camada"].items():
    print(k, "->", len(v), v)
print("=== lista mestre (nomes V6) x estado na V7 ===")
for k, v in res_mestre.items():
    print(k, "->", v if v else "NAO ENCONTRADO")
print("=== temáticos ===")
print(json.dumps(out["B_tokens_tematicos"]["fichas_por_autor_titulo"], ensure_ascii=False))
print("sha:", out["canonica_sha256"][:16])
print("gravado:", p)
