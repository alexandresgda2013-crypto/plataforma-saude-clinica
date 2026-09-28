#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# censo_valores.py — 2026-09-11: despeja TODOS os valores reais fora do enum por
# campo/biblioteca (com contagens e ids de exemplo) + presença de campos.
# Instrumento de medição: NADA grava.
import json, glob, sys, collections
sys.path.insert(0, "/home/user/BIBLIOTECAS/_documentos_serie/bancada_at02/scripts")
from contrato import Contrato, ENUM_VINCULO, ID_PAT, STATUS_DECIDIDOS

def load_json(p):
    d = json.load(open(p, encoding="utf-8"))
    return d if isinstance(d, list) else d.get("vinculos", d.get("registros", d.get("entradas", [])))

CAMPOS = ["natureza_relacao","forca_causal","grau_maturidade","status_referencia",
          "verification_status","evid_role","g2_elegibilidade","status_auditoria"]
res = {}
for at in sorted(glob.glob("/home/user/BIBLIOTECAS/B*/atuais")):
    b = at.split("/")[-2].split("_")[0]
    vp = glob.glob(at + "/Evidencias/Vinculos/*.json")
    if not vp: continue
    vinc = load_json(vp[0])
    out = {"n": len(vinc), "fora_enum": {}, "ausentes": collections.Counter(),
           "id_fora_padrao": [], "g3_assinaturas": collections.Counter(),
           "tem_verificacao_dict": 0, "path": vp[0]}
    for r in vinc:
        rid = str(r.get("id_vinculo","?"))
        if not ID_PAT["vinculo"].match(rid): out["id_fora_padrao"].append(rid)
        if isinstance(r.get("verificacao"), dict): out["tem_verificacao_dict"] += 1
        for c in CAMPOS:
            if c not in r:
                out["ausentes"][c] += 1; continue
            v = r[c]
            if v in (None,""): continue
            if v not in ENUM_VINCULO[c]:
                fc = out["fora_enum"].setdefault(c, collections.Counter())
                fc[str(v)] += 1
                ex = out["fora_enum"].setdefault(c+"__ex", {})
                ex.setdefault(str(v), rid)
        q = (r.get("g3_verificado_por") or "").strip()
        st = r.get("status_auditoria","")
        if st in STATUS_DECIDIDOS["vinculo"]:
            import re as _re
            if _re.search(r"eutils|script|automatico", q, _re.I):
                out["g3_assinaturas"][q[:120]] += 1
    out["ausentes"] = dict(out["ausentes"])
    out["g3_assinaturas"] = dict(out["g3_assinaturas"])
    for c in list(out["fora_enum"].keys()):
        if isinstance(out["fora_enum"][c], collections.Counter):
            out["fora_enum"][c] = dict(out["fora_enum"][c])
    if out["id_fora_padrao"]:
        out["id_fora_padrao"] = [len(out["id_fora_padrao"]), out["id_fora_padrao"][:3]]
    res[b] = out
json.dump(res, open("/home/user/BIBLIOTECAS/_documentos_serie/scripts_serie/censo_valores_2026-09-11.json","w"),
          ensure_ascii=False, indent=1)
for b,o in res.items():
    print("###", b, "n=",o["n"])
    if o["fora_enum"]:
        for c in CAMPOS:
            if c in o["fora_enum"] and not c.endswith("__ex"):
                print("   ",c, o["fora_enum"][c])
    if o["ausentes"]: print("    AUSENTES:", o["ausentes"])
    if o["id_fora_padrao"]: print("    ID fora padrão:", o["id_fora_padrao"][0], "ex:", o["id_fora_padrao"][1])
    if o["g3_assinaturas"]: print("    G3 mistas:", json.dumps(o["g3_assinaturas"], ensure_ascii=False)[:400])
    print("    verificacao{} em", o["tem_verificacao_dict"])
