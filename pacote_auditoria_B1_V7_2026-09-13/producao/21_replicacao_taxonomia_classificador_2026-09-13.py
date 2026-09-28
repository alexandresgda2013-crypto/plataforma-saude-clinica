#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 21_replicacao_taxonomia_classificador_2026-09-13.py
# Réplica bilateral do §3 do PARECER_B1_V6_E_PLANO_TRIO_2026-09-13 (Auditor-Mestre).
# Mede, SÓ NA B1 V6: (a) citações (Autor, ANO[sufixo])[XX; ...] na prosa;
# (b) tokens AUTOR_ANO[XX] do apêndice; (c) balde da ficha (01/02/03) e desenho_estudo;
# e computa: refs divergentes prosa×apêndice, citações autodivergentes na prosa,
# concordância prosa×balde e apêndice×balde (hipótese: 01=OB, 02=MA, 03=EC).
# Hipótese declarada a priori (para comparação com os números dele: 71 divergentes,
# 7 autodivergentes, 37,1% (76/205), 21,3% (50/235)).
import json, re, glob, collections, unicodedata

AT = "/home/user/BIBLIOTECAS/B01_Neuroinflamacao/atuais/"
CAN = AT + "B1 NEUROINFLAMAÇÃO V6 CANONICA.md"
t = open(CAN, encoding="utf-8").read()

# ---------- (a) citações da prosa ----------
# formato B1: (Sobrenome et al., 2023)[XX; ...] ou (Sobrenome & Sobrenome, 2023)[XX...]
# e também "Sobrenome et al. (2023)[XX..." e menções com token só [XX] após ano em parêntese
cit = re.findall(r"\(([^()]*?,\s*(?:19|20)\d{2}[a-z]?)\)\[([A-Z]{2})", t)
# também formato "Sobrenome et al. (2023)[XX"
cit2 = re.findall(r"([A-ZÁÉÍÓÚÂÊÔÃÕÇ][\w\-]+(?:\s+et al\.|\s*&\s*[\w\-]+)?)\s*\(((?:19|20)\d{2}[a-z]?)\)\[([A-Z]{2})", t)
chaves_prosa = []
for base, xx in cit:
    ano = re.search(r"((?:19|20)\d{2}[a-z]?)", base).group(1)
    sob = base.split(",")[0].strip()
    chaves_prosa.append((sob, ano, xx))
for sob, ano, xx in cit2:
    chaves_prosa.append((sob, ano, xx))
unicas_prosa = sorted(set((s.lower(), a) for s, a, x in chaves_prosa))

# ---------- (b) tokens do apêndice ----------
# rev.1: a seção começa em "## APÊNDICE DE CORPUS" e vai até o próximo "## " (REGISTRO);
# usar rfind pegava a menção ao apêndice dentro do próprio REGISTRO (3 tokens fantasmas).
i0 = t.find("## APÊNDICE DE CORPUS")
i1 = t.find("## ", i0 + 5) if i0 >= 0 else -1
ap = t[i0:i1] if i0 >= 0 and i1 > i0 else ""
assert len(ap) > 1000, "seção de apêndice não isolada"
tok = re.findall(r"\b([A-ZÁÉÍÓÚÂÊÔÃÕÇ0-9_]+?_((?:19|20)\d{2}[a-z]?))\[([A-Z]{2})\]", ap)
tokens_apendice = sorted(set((tk.lower(), xx) for tk, ano, xx in tok))
# rev.2: ocorrências de TOKEN[XX] no documento INTEIRO (apêndice + listras de subseção) — comparável ao "317" dele
tok_doc = re.findall(r"\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ0-9_]+?_(?:19|20)\d{2}[a-z]?\[[A-Z]{2}\]", t)

# ---------- (c) fichas ----------
balde = {}
desenho = {}
refs = {}
for f, b in [("01_pmids.json", "OB"), ("02_meta_analises.json", "MA"), ("03_ensaios_clinicos.json", "EC")]:
    d = json.load(open(AT + "Evidencias/Bibliografia/" + f, encoding="utf-8"))
    d = d if isinstance(d, list) else d.get("referencias", d.get("registros", []))
    for r in d:
        rid = r["id_referencia_interna"]  # REF_SOBRENOME_ANO
        balde[rid.lower()] = b
        desenho[rid.lower()] = r.get("desenho_estudo", "")
        refs[rid.lower()] = rid

def rid_da_chave(sob, ano):
    # rev.2: sobrenome puro — corta "et al.", "& Parceiro", normaliza acento e hífen
    s = sob.split(" et al")[0].split(" & ")[0].strip()
    s = s.split(",")[0].strip()
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9]", "", s).upper()
    for cand in ("REF_" + s + "_" + ano, "REF_" + s + "_" + ano.replace("b", "").replace("c", "")):
        if cand.lower() in refs:
            return cand.lower()
    return None

# ---------- (1) refs divergentes prosa × apêndice ----------
prosa_xx = collections.defaultdict(set)
for sob, ano, xx in chaves_prosa:
    rid = rid_da_chave(sob, ano)
    if rid:
        prosa_xx[rid].add(xx)
ap_xx = collections.defaultdict(set)
for tk, xx in tokens_apendice:
    rid = ("ref_" + tk).lower()
    if rid in refs:
        ap_xx[rid].add(xx)
div_pa = sorted(rid for rid in prosa_xx if rid in ap_xx and prosa_xx[rid] != ap_xx[rid])

# ---------- (2) autodivergentes na prosa ----------
auto = sorted(rid for rid in prosa_xx if len(prosa_xx[rid]) > 1)

# ---------- (3) concordância com o balde ----------
def concordancia(mapa_xx):
    tot = ok = 0
    for rid, s in mapa_xx.items():
        if rid in balde:
            tot += 1
            if balde[rid] in s:
                ok += 1
    return ok, tot
ok_p, tot_p = concordancia(prosa_xx)
ok_a, tot_a = concordancia(ap_xx)

out = {
 "data": "2026-09-13",
 "objeto": "réplica do §3 do parecer (3 taxonomias de classificador)",
 "canonica_sha_parcial": "ver manifesto vigente",
 "contagens": {
   "mencoes_prosa_brutas": len(chaves_prosa),
   "chaves_unicas_prosa": len(unicas_prosa),
   "tokens_apendice_unicos": len(tokens_apendice),
   "ocorrencias_token_documento": len(tok_doc),
   "refs_com_xx_na_prosa": len(prosa_xx),
   "refs_com_token_no_apendice": len(ap_xx),
 },
 "refs_divergentes_prosa_x_apendice": {"n": len(div_pa), "lista": [refs[r] for r in div_pa]},
 "autodivergentes_na_prosa": {"n": len(auto), "lista": {refs[r]: sorted(prosa_xx[r]) for r in auto}},
 "concordancia_prosa_x_balde": {"ok": ok_p, "tot": tot_p, "pct": round(100*ok_p/max(tot_p,1),1)},
 "concordancia_apendice_x_balde": {"ok": ok_a, "tot": tot_a, "pct": round(100*ok_a/max(tot_a,1),1)},
 "hipoteses": "balde 01_pmids=OB, 02_meta_analises=MA, 03_ensaios=EC; parser regex declarado no script",
 "numeros_do_auditor": {"refs_divergentes": 71, "autodivergentes": 7,
   "prosa_x_balde": "76/205 (37,1%)", "apendice_x_balde": "50/235 (21,3%)",
   "chaves_prosa": 217, "tokens_apendice": 317},
}
print(json.dumps(out, ensure_ascii=False, indent=2))
json.dump(out, open(AT + "producao/21_replicacao_taxonomia_classificador_2026-09-13.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
