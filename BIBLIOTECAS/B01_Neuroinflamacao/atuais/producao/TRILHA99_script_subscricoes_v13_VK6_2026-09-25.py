#!/usr/bin/env python3
"""TRILHA 99 — subscrições Schema-Claim v1.3 rev.2 · ressalva V-K6 · minuta rev.3.

  T1  Mestre upload ≡ série + digital
  T2  Mestre: SUBSCREVO SEM RESSALVA formal
  T3  Estrutura: "subscrevo com a ressalva" + V-K6 nomeado
  T4  armadilha: sustenta+condicao VIOLA N2 (reprodutível)
  T5  caminhos OK: condicional+condicao aceito; sustenta+null aceito
  T6  minuta rev.3 contém V-K6 com precedência (condicional+condicao;
      sentido fica no claim e não vira direcao_suporte)
  T7  minuta rev.3 contém V-K7 (grau_maturidade vazio ⇒ ausência no N2)
  T8  rev.3 preserva rev.2 (V-K3 preferida + P-K1/K2/K3)
  T9  estado: 1 sem ressalva (M) + 1 com ressalva sanada na rev.3 (E)
       ⇒ documento mudou ⇒ 2× novo sobre a rev.3; ressalva cicla pelos 3
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/user")
SERIE = ROOT / "BIBLIOTECAS/_documentos_serie/SUBSCRICOES_SCHEMA_CLAIM_V13_2026-09-25"
MESTRE = SERIE / "SUBSCRICAO_SCHEMA_CLAIM_v13_MESTRE_2026-09-25.md"
UP_M = ROOT / "uploads/SUBSCRICAO_SCHEMA_CLAIM_v13_MESTRE_2026-09-25.md"
ESTRUTURA = SERIE / "SUBSCRICAO_ESTRUTURA_V13_VK6_2026-09-25.md"
REV3 = ROOT / "ENTREGAS/2026-09-25_CICLO_KIT_MINUTA_V13/3º SCHEMA-CLAIM — v1.3 (MINUTA rev.3).md"
REV2 = ROOT / "ENTREGAS/2026-09-25_CICLO_KIT_MINUTA_V13/3º SCHEMA-CLAIM — v1.3 (MINUTA rev.2).md"
N2_PATH = ROOT / "BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA99_subscricoes_v13_VK6_2026-09-25.json"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def violates(n2, direcao, cond):
    allOf = n2["properties"]["ancoras"]["items"]["allOf"]
    anc = {"direcao_suporte": direcao, "condicao": cond}
    for rule in allOf:
        ifc, then = rule.get("if", {}), rule.get("then", {})
        props = ifc.get("properties", {})
        matched = True
        for k, spec in props.items():
            if k not in anc:
                matched = False
                continue
            if "const" in spec and anc[k] != spec["const"]:
                matched = False
            if "enum" in spec and anc[k] not in spec["enum"]:
                matched = False
        if "required" in ifc and not all(k in anc for k in ifc["required"]):
            matched = False
        if not matched:
            continue
        tp = then.get("properties", {})
        if "condicao" in tp:
            if tp["condicao"].get("type") == "null" and anc.get("condicao") is not None:
                return True
            if "required" in then and "condicao" in then["required"] and anc.get("condicao") is None:
                return True
    return False


def main() -> int:
    same = UP_M.read_bytes() == MESTRE.read_bytes()
    check("T1", "Mestre upload ≡ série", same,
          {"sha": sha(MESTRE), "bytes": MESTRE.stat().st_size})

    mest = MESTRE.read_text(encoding="utf-8")
    estr = ESTRUTURA.read_text(encoding="utf-8")
    r3 = REV3.read_text(encoding="utf-8")
    r2 = REV2.read_text(encoding="utf-8")
    n2 = json.loads(N2_PATH.read_text(encoding="utf-8"))

    check("T2", "Mestre: SUBSCREVO SEM RESSALVA",
          "SUBSCREVO SEM RESSALVA" in mest, {})

    check("T3", "Estrutura: subscreve com ressalva V-K6",
          "subscrevo com a ressalva" in estr.lower() or "Subscrevo com uma ressalva" in estr
          and "V-K6" in estr, {"vk6": "V-K6" in estr})

    check("T4", "armadilha: sustenta+condicao VIOLA N2",
          violates(n2, "sustenta", "sexo feminino") and violates(n2, "refuta", "x"),
          {"sustenta_cond": violates(n2, "sustenta", "sexo feminino")})

    check("T5", "condicional+condicao aceito; sustenta+null aceito",
          not violates(n2, "condicional", "sexo feminino")
          and not violates(n2, "sustenta", None), {})

    check("T6", "rev.3: V-K6 precedência escrita",
          "V-K6" in r3 and "PRECEDÊNCIA" in r3
          and "condicional" in r3 and "não vira direcao_suporte" in r3
          or "NÃO vira direcao_suporte" in r3, {})

    check("T7", "rev.3: V-K7 grau_maturidade ausência ≠ null gravado",
          "V-K7" in r3 and "nunca null gravado" in r3, {})

    ok8 = ("opção preferida do Comentador" in r3
           and all(x in r3 for x in ("condicao_aplicacao", "heterogeneidade", "maturidade_evidencia",
                                     "suporta_relacao | refuta_relacao | inconclusivo",
                                     "FONTE ÚNICA DE CONDIÇÃO"))
           and r3 != r2)
    check("T8", "rev.3 preserva conteúdo da rev.2 e é distinta", ok8,
          {"sha_r2": sha(REV2), "sha_r3": sha(REV3)})

    check("T9", "estado: M sem + E ressalva sanada em rev.3 ⇒ 2× novo sobre rev.3",
          "SUBSCREVO SEM RESSALVA" in mest and "V-K6" in estr and "V-K6" in r3,
          {"proximo": "Comentador (ciclo da ressalva) → janelas rev.3"})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 99, "data": "2026-09-25",
        "objeto": "subscricoes_v13_ressalva_VK6_minuta_rev3",
        "digitais": {"mestre": sha(MESTRE), "estrutura": sha(ESTRUTURA),
                     "rev2": sha(REV2), "rev3": sha(REV3)},
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA99 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
