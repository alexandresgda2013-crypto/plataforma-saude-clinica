#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# replica_tabela_v02_serie_2026-09-13.py — réplica bilateral da tabela §4 do
# ERRATA_E_PARECER_CONTINUIDADE_2026-09-13 do Auditor-Mestre.
# Roda o P-8 OFICIAL (validar_coerencia_camadas.py --json) nas 16 bibliotecas e
# extrai: vínculos totais, ERROS por regra (V-02, V-04, V-05...), avisos.
# NADA grava nas bibliotecas — só lê e escreve o relatório agregado.
import glob, json, subprocess, sys, collections, os

P8 = "/home/user/Ferramentas de geração e auditoria/06_portao_P8_coerencia/scripts/validar_coerencia_camadas.py"
OUTDIR = "/tmp/p8_serie_2026-09-13"
os.makedirs(OUTDIR, exist_ok=True)

linhas = []
tot_vinc = 0; tot_v02 = 0
for at in sorted(glob.glob("/home/user/BIBLIOTECAS/B*/atuais")):
    b = at.split("/")[-2].split("_")[0]
    sj = f"{OUTDIR}/{b}.json"
    r = subprocess.run([sys.executable, P8, at, "--json", sj], capture_output=True, text=True, timeout=600)
    try:
        d = json.load(open(sj, encoding="utf-8"))
    except Exception as e:
        linhas.append((b, None, None, None, f"FALHA JSON: {e} | stderr: {r.stderr[-200:]}"))
        continue
    # estruturas possíveis do relatório
    erros = collections.Counter()
    avisos = collections.Counter()
    for item in d.get("problemas", d.get("achados", [])):
        regra = item.get("regra", item.get("id_regra", "?"))
        nivel = item.get("nivel", item.get("severidade", "?"))
        if nivel.upper().startswith("ERRO"):
            erros[regra] += 1
        else:
            avisos[regra] += 1
    nv = d.get("vinculos", d.get("totais", {}).get("vinculos"))
    if nv is None:
        # tenta contar do arquivo de vínculos
        vp = glob.glob(at + "/Evidencias/Vinculos/*.json")
        if vp:
            dd = json.load(open(vp[0], encoding="utf-8"))
            nv = len(dd if isinstance(dd, list) else dd.get("vinculos", []))
    linhas.append((b, nv, erros.get("V-02", 0), dict(erros), r.returncode))
    tot_vinc += nv or 0
    tot_v02 += erros.get("V-02", 0)

print(f"{'bib':5} {'vinc':>5} {'V-02':>5}  todos_erros / retcode")
for b, nv, v02, e, rc in linhas:
    print(f"{b:5} {nv!s:>5} {v02!s:>5}  {e} rc={rc}")
print(f"TOTAL {'':1} {tot_vinc:>5} {tot_v02:>5}")
json.dump({"gerado_em": "2026-09-13", "linhas": [
    {"bib": b, "vinculos": nv, "V-02_erros": v02, "erros_por_regra": e} for b, nv, v02, e, rc in linhas],
    "total_vinculos": tot_vinc, "total_V02": tot_v02},
    open("/tmp/p8_serie_2026-09-13/AGREGADO.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("agregado em /tmp/p8_serie_2026-09-13/AGREGADO.json")
