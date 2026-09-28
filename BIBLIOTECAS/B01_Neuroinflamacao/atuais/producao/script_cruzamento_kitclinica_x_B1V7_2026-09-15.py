#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TRILHA 33 — cruzamento KIT CLÍNICA (BLOCO DE ESTADO v1.6 + LISTA CANÔNICA SM-02 v1.3)
# × acervo B1 V7 (237 fichas) — 2026-09-15
# Escopo: uploads/ (kit) × BIBLIOTECAS/B01_Neuroinflamacao/atuais (acervo)
# Chaves: pmid extraído por regex das linhas 'pmid:'/pmid: <n> das seções claims_aprovados
#         (BLOCO) e 'fontes:'/'fontes_exploratorias:' (LISTA); acervo por campo pmid_oficial.
import json, re, hashlib, sys

UP = "/home/user/uploads/"
AT = "/home/user/BIBLIOTECAS/B01_Neuroinflamacao/atuais/"
bloco = open(UP + "6º BLOCO DE ESTADO  v1.6.md", encoding="utf-8").read()
lista = open(UP + "5º LISTA CANÔNICA — B1  SM-02 V1.3.md", encoding="utf-8").read()

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]
print("sha bloco:", sha(UP + "6º BLOCO DE ESTADO  v1.6.md"))
print("sha lista:", sha(UP + "5º LISTA CANÔNICA — B1  SM-02 V1.3.md"))

# --- acervo V7 por pmid_oficial ---
acervo_pmid = {}   # pmid -> id_referencia_interna
acervo_sem_pmid = []
for f in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
    d = json.load(open(AT + "Evidencias/Bibliografia/" + f))
    for r in d:
        p = str(r.get("pmid_oficial") or "").strip()
        if p and p.lower() not in ("none", "null", ""):
            acervo_pmid[p] = r["id_referencia_interna"]
        else:
            acervo_sem_pmid.append(r["id_referencia_interna"])
print(f"acervo V7: {len(acervo_pmid)} fichas COM pmid_oficial · {len(acervo_sem_pmid)} sem pmid_oficial")

# --- claim_id_origem no acervo ---
cids = set()
for f in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
    for r in json.load(open(AT + "Evidencias/Bibliografia/" + f)):
        v = r.get("claim_id_origem")
        if v: cids.add(str(v))
print("claim_id_origem distintos no acervo:", len(cids), "| padrão B1.SM02.*:", sum(1 for c in cids if c.startswith("B1.SM0")))
print("  exemplos:", sorted(cids)[:10])

# --- PMIDs do BLOCO por claim (seção claims_aprovados apenas) ---
sec = bloco.split("claims_aprovados:", 1)[1].split("# LOG DE EXCLUSÃO", 1)[0]
# também cortar no cabeçalho da linha '# ============================================' que precede o log
sec = sec.split("# ============================================")[0]
claims = re.split(r"\n\s*-?\s*[Cc]laim_id:\s*", sec)
res = {}   # claim -> {fontes:[(pmid,em_v7ref)], total, em_v7}
for ped in claims[1:]:
    cid = ped.split("\n", 1)[0].strip()
    pmids = re.findall(r"pmid:\s*\"?(\d{7,9})\"?", ped)
    emv7 = {p: (p in acervo_pmid) for p in pmids}
    res[cid] = emv7

print("\n=== COBERTURA POR CLAIM (fontes+exploratórias+moderadores do BLOCO) ===")
tot_p = tot_em = 0
ausentes_total = {}
for cid in res:
    em = res[cid]
    n, k = len(em), sum(em.values())
    tot_p += n; tot_em += k
    faltam = [p for p, ok in em.items() if not ok]
    if faltam: ausentes_total[cid] = faltam
    marca = "OK " if k == n else ("PARCIAL" if k else "ZERO")
    print(f"  {cid:16} {n:2} pmids · {k:2} em V7  [{marca}]" + (f"  ausentes: {faltam}" if faltam else ""))
print(f"\nTOTAL: {tot_p} pmid-citações · {tot_em} presentes em V7 ({tot_em/tot_p*100:.1f}%) · {tot_p-tot_em} ausentes")

# --- PMIDs da LISTA (fontes declaradas nas entradas aprovadas) ---
pm_lista = set(re.findall(r"fontes:\s*\[([\d, ]+)\]", lista.replace('"', '')))
conj_lista = set()
for grp in pm_lista:
    conj_lista |= set(re.findall(r"\d{7,9}", grp))
print(f"\nLISTA — PMIDs únicos em 'fontes:' das entradas: {len(conj_lista)} · em V7: {sum(p in acervo_pmid for p in conj_lista)}")
print("  ausentes de V7:", sorted(p for p in conj_lista if p not in acervo_pmid))

# --- filas da LISTA (futura/realocacao/redirecionados) ---
for nome in ("fila_futura_outros_submodulos", "fila_realocacao", "redirecionados"):
    bloco2 = lista.split(nome + ":", 1)[1]
    fim = re.split(r"\n# =", bloco2, 1)
    pm = set(re.findall(r"pmid:\s*\"?(\d{7,9})", fim[0]))
    emv = sum(p in acervo_pmid for p in pm)
    print(f"LISTA {nome}: {len(pm)} pmids · em V7: {emv} · ausentes: {sorted(p for p in pm if p not in acervo_pmid)}")

# --- fontes_rejeitadas do BLOCO: quantas existem no acervo V7? (rejeitada lá não deveria estar aqui?) ---
rej = bloco.split("fontes_rejeitadas:", 1)[1]
pm_rej = set(re.findall(r"pmid:\s*\"?(\d{7,9})", rej))
emv = {p: acervo_pmid.get(p) for p in pm_rej if p in acervo_pmid}
print(f"\nBLOCO fontes_rejeitadas: {len(pm_rej)} pmids únicos · presentes no acervo V7: {len(emv)} -> {sorted(emv.items())}")

# --- o inverso: fichas V7 ligadas a claims SM-02 (claim_id_origem) ---
vinculadas = {}
for f in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
    for r in json.load(open(AT + "Evidencias/Bibliografia/" + f)):
        v = str(r.get("claim_id_origem") or "")
        if v.startswith("B1.SM02."):
            vinculadas[v] = vinculadas.get(v, 0) + 1
print("\nfichas V7 com claim_id_origem B1.SM02.*:", sum(vinculadas.values()), "em", len(vinculadas), "claims:", dict(sorted(vinculadas.items())))
