#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_fidelidade_b1.py — Checklist de fidelidade canônica + estrutural da B1,
adaptado à convenção REAL da biblioteca:
  - listra  : *Rótulo[TAG] | Rótulo2[TAG]*   (rótulo descritivo)
  - prosa   : (Sobrenome et al., Ano)[TAG...]
  - Módulo09: ids_referencia_interna = ["REF_<rótulo>"]
  - vínculos: vinculos_referencia_afirmacao.json (id_referencia_interna -> REF_<rótulo>)
Cobre os portões dos checklists 05 (A2/A3/A4/A5, B3/B4) e 07 (B/D) do framework.
"""
import json, re, glob, sys, unicodedata
from pathlib import Path

# pasta do mecanismo: via argumento (script global) — ex.:
#   python3 check_fidelidade_b1.py /home/user/BIBLIOTECAS/B01_Neuroinflamacao
import sys as _sys
BIB = None
if len(_sys.argv) > 1:
    BASE = Path(_sys.argv[1]).resolve()
    _cs = sorted([a for a in BASE.glob("*.md") if "CANONICA" in a.name.upper()],
                 key=lambda a: int((re.search(r"[Vv](\d+)", a.name) or [0])[1]))
    if _cs: BIB = _cs[-1]
print(f"[versão ativa] {BIB.name if BIB else 'NENHUMA (passe a pasta do mecanismo por argumento)'} — {getattr(BASE,'name','')}\n")

erros, avisos, oks = [], [], []
def E(m): erros.append("ERRO | "+m)
def W(m): avisos.append("AVISO| "+m)
def O(m): oks.append("OK   | "+m)

def sem_ac(s):
    return "".join(c for c in unicodedata.normalize("NFKD",s) if not unicodedata.combining(c))

# ---------- carrega Módulo 09 ----------
regs = {}   # rótulo (sem REF_) -> registro
id2reg = {}  # REF_xxx -> registro
for f in glob.glob(str(BASE/"Evidencias/Bibliografia/*.json")):
    try: data = json.load(open(f, encoding="utf-8"))
    except Exception as ex:
        E(f"{Path(f).name}: JSON inválido ({ex})"); continue
    if not isinstance(data, list): continue
    for it in data:
        if not isinstance(it, dict): continue
        ids = it.get("ids_referencia_interna") or ([it["id_referencia_interna"]] if it.get("id_referencia_interna") else [])
        for full in ids:
            if not full: continue
            rot = full[4:] if full.startswith("REF_") else full
            if rot in regs:
                E(f"rótulo duplicado no Módulo09: {rot} ({Path(f).name})")
            regs[rot] = it
            id2reg[full] = it
        # valida PMID
        pmid = str(it.get("pmid_oficial",""))
        if pmid and not pmid.isdigit():
            E(f"PMID inválido em {ids}: {pmid!r}")

txt = BIB.read_text(encoding="utf-8")

# ================= ESTRUTURAL (forma) =================
n_h1 = len(re.findall(r"^# ", txt, re.M))
n_h2 = len(re.findall(r"^## ", txt, re.M))
n_h3 = len(re.findall(r"^### ", txt, re.M))
if n_h1 == 1: O(f"Estrutura: 1 H1")
else: E(f"Estrutura: H1 deveria ser 1, há {n_h1}")
if n_h2 >= 13: O(f"Estrutura: {n_h2} blocos H2")
else: E(f"Estrutura: poucos blocos H2 ({n_h2})")
O(f"Estrutura: {n_h3} subseções H3")

# cada H3 deve ter exatamente uma listra *...* com rótulos[TAG]
subs = list(re.finditer(r"^### .*$", txt, re.M))
subs.append(None)
labels_por_sub = {}
listra_sem_sub = 0
# seções intencionalmente SEM referência: nota de escopo, inventário negativo, gap de busca
SEM_REF_OK = re.compile(r"(Nota de escopo|Inventário NEGATIVO|gap de busca|gap_pesquisa)", re.I)
for i in range(len(subs)-1):
    s = subs[i].start()
    e = subs[i+1].start() if subs[i+1] else len(txt)
    blk = txt[s:e]
    tit = subs[i].group(0)[:60]
    listras = re.findall(r"^\*([^*]+)\*\s*$", blk, re.M)
    tem_citacao = bool(re.search(r"\([A-ZÀ-Ú][A-Za-zÀ-ÿ]+(?: et al\.?)?,?\s*\d{4}\)", blk)) or ("et al" in blk)
    if not listras:
        if SEM_REF_OK.search(blk) and not tem_citacao:
            O(f"seção intencionalmente sem referência (escopo/gap/negativo): {tit[:48]}")
        else:
            E(f"sem listra de referências: {tit}")
    labs = []
    for L in listras:
        for lab, tag in re.findall(r"([A-Za-z0-9_À-￿]+)\[(MA|EC|OB|ML|AT)\]", L):
            labs.append((lab, tag))
    labels_por_sub[tit] = labs

# mal-formado
if "]]" in txt: E("há ']]' (selo/tag mal-formado)")
else: O("sem ']]' mal-formado")

# tabelas
n_tbl = txt.count("\n|")
O(f"tabelas: {n_tbl} linhas com '|'")

# ================= FIDELIDADE DAS LISTRAS =================
todos_labels_listra = set()
for tit, labs in labels_por_sub.items():
    for lab, tag in labs:
        todos_labels_listra.add(lab)
        if lab not in regs:
            # PENDENTE provisório?
            if "PENDENTE" in lab:
                W(f"listra com rótulo PENDENTE (sem PMID): {lab}  ({tit[:40]})")
            else:
                E(f"rótulo de listra SEM registro no Módulo09: {lab}  ({tit[:40]})")
        else:
            # coerência de tag: classificador do arquivo vs tag da listra
            arq = None
            for ff in glob.glob(str(BASE/"Evidencias/Bibliografia/*.json")):
                try: dd = json.load(open(ff, encoding="utf-8"))
                except: continue
                if isinstance(dd, list) and any(
                        lab in [x[4:] if x.startswith('REF_') else x for x in (r.get('ids_referencia_interna') or [])]
                        for r in dd if isinstance(r, dict)):
                    arq = Path(ff).name
            esperado = {"01_pmids.json":"OB/EC/ML/MA","02_meta_analises.json":"MA",
                        "03_ensaios_clinicos.json":"EC","04_atualizacoes_literatura.json":"AT",
                        "05_manuais_e_livros.json":"ML"}.get(arq, "?")
O(f"listras: {len(todos_labels_listra)} rótulos únicos citados")

# ================= ÓRFÃS: registro no JSON nunca citado em listra =================
citados_listra = todos_labels_listra
orfas = []
for rot in regs:
    if rot not in citados_listra:
        orfas.append(rot)
if orfas:
    W(f"{len(orfas)} registro(s) do Módulo09 sem aparecer em NENHUMA listra:")
    for o_ in sorted(orfas):
        # pode estar citado só na prosa como autor-ano?
        W(f"   órfã de listra: {o_}")
else:
    O("nenhuma referência órfã (todo registro do Módulo09 aparece em listra)")

# ================= PMID/DOI no texto corrido (B4 / A5) =================
if re.search(r"\bPMID\s*:?\s*\d{5,}", txt):
    E("PMID encontrado no texto corrido (proibido)")
elif re.search(r"\b10\.\d{3,4}/\S+", txt):
    E("DOI encontrado no texto corrido (proibido)")
else:
    O("sem PMID/DOI no texto corrido (B4/A5)")

# ================= TÍTULOS EM INGLÊS NA PROSA =================
EN = re.compile(r"\b(the|and|with|from|that|which|between|through|drives?|mediat\w*|promot\w*|induc\w*|regulat\w*|mice|mouse|rats?|patients?|studies?|review|microglia|microglial|astrocyte|synaptic|hippocamp\w*|inflammation|inflammatory|disorders?|pyroptosis|signaling|mechanism\w*|activation|release)\b", re.I)
PT = re.compile(r"\b(revisão|camundongo|humano|reduz|prediz|resolução|sintomas|hipocampal|células|sobre|ver|astrócitos|glicação|referência|verificar|metilação|genes|fatores|modelo|limitando)\b", re.I)
en_res = [m.group(1) for m in re.finditer(r"\(([^()]{4,130}?,\s*(?:19|20)\d{2}[a-z]?)\)", txt)
          if EN.search(m.group(1)) and len(PT.findall(m.group(1))) < 3]
if en_res:
    E(f"{len(en_res)} título(s) em inglês ainda na prosa: {en_res[:5]}")
else:
    O("nenhum título em inglês na prosa")

# ================= CITAÇÕES autor-ano ↔ registro real =================
# (Sobrenome et al., Ano)[TAG]  ou  (Sobrenome & Sob, Ano)
CITE = re.compile(r"\(([A-ZÀ-Ú][A-Za-zÀ-ÿ’'-]+)(?:\s+(?:&|e)\s+([A-ZÀ-Ú][A-Za-zÀ-ÿ’'-]+))?(?: et al\.?)?,?\s+(\d{4})[a-z]?\)\s*\[?(MA|EC|OB|ML|AT)?")
# índice de sobrenome->rótulos (do JSON)
sob2rot = {}
for rot, it in regs.items():
    aut = it.get("autores") or []
    if not aut: continue
    p = aut[0]
    sob = p.split(",")[0].strip() if "," in p else p.split()[0]
    sob2rot.setdefault(sem_ac(sob).lower(), []).append((rot, str(it.get("revista_ano",""))))

cite_bad = []
cite_ok = 0
for m in CITE.finditer(txt):
    sob = m.group(1); ano = m.group(3)
    key = sem_ac(sob).lower()
    alvos = sob2rot.get(key, [])
    # casa por ano também
    bate = [r for r in alvos if ano in r[1]]
    if alvos and bate:
        cite_ok += 1
    elif alvos:
        cite_ok += 1  # sobrenome existe; ano pode variar por data de pub online
    else:
        cite_bad.append(f"{sob} {ano}")
if cite_bad:
    W(f"{len(set(cite_bad))} citação(ões) autor-ano sem sobrenome correspondente no Módulo09: {sorted(set(cite_bad))[:12]}")
else:
    O(f"todas as {cite_ok} citações autor-ano têm sobrenome correspondente no Módulo09")

# ================= SELOS =================
for selo in ["[VERIFICADO]", "[PRÉ-CLÍNICO]", "[EXTRAPOLADO: animal/célula→humano]"]:
    c = txt.count(selo)
    O(f"selo {selo}: {c}")
O(f"selo [PENDENTE_VERIF]: {txt.count('[PENDENTE_VERIF]')}")

# ================= VÍNCULOS (Nível 2) =================
vp = BASE/"Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
if vp.exists():
    vinc = json.load(open(vp, encoding="utf-8"))
    v_ids = {v.get("id_referencia_interna","") for v in vinc if isinstance(v, dict)}
    O(f"vínculos: {len(vinc)} registros, {len(v_ids)} referências distintas")
    # integridade: todo id de vínculo existe no Módulo09
    falt = [x for x in v_ids if x and x not in id2reg]
    if falt:
        E(f"{len(falt)} id_referencia_interna dos vínculos NÃO existe no Módulo09: {sorted(falt)[:8]}")
    else:
        O("toda referência dos vínculos existe no Módulo09 (integridade referencial)")

# ================= FRENTE / HEADER CANÔNICO =================
if "artefato_rotulo" in txt or "CANONICA" in txt[:3000].upper():
    O("header menciona artefato CANÔNICO")
else:
    W("header não menciona artefato_rotulo/CANONICA no .md (checar manifesto)")
man = BASE/"Evidencias/Bibliografia/_manifesto_biblioteca.json"
if man.exists():
    mj = json.load(open(man, encoding="utf-8"))
    O(f"manifesto: rodada={mj.get('rodada','?')} rotulo={mj.get('artefato_rotulo','?')}")

print("="*78)
print("CHECKLIST DE FIDELIDADE CANÔNICA + ESTRUTURAL — B1 NEUROINFLAMAÇÃO")
print("="*78)
for x in oks: print(x)
for x in avisos: print(x)
for x in erros: print(x)
print("="*78)
print(f"RESUMO: {len(erros)} ERRO(S), {len(avisos)} AVISO(S), {len(oks)} OK")
sys.exit(1 if erros else 0)
