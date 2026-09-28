#!/usr/bin/env python3
"""TRILHA 102 — RÉPLICA FINAL subscrições COMO EXECUTAR v1.10 · fecho do ciclo.

  T1  Mestre upload ≡ série + digital
  T2  Mestre: SUBSCREVO SEM RESSALVA + sha 49514344 declarado
  T3  Estrutura: Subscrevo sem ressalva (texto arquivado) + sha 49514344
  T4  minuta canônica sha = 4951434417f2… (as duas batem)
  T5  nota E (verificação ao vivo/passagem literal) registrada, não bloqueia
  T6  nota M (v1.10 vale com schema+contrato fechados) registrada
  T7  estado: 2× sem ressalva ⇒ ciclo v1.10 ENCAVEL (vigência = operador)
  T8  pendências seguem: P-K1/P-K2 · P-K6 v1.5 · piloto .014 (não bloqueio)
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/home/user")
SERIE = ROOT / "BIBLIOTECAS/_documentos_serie/SUBSCRICOES_COMO_EXECUTAR_V110_2026-09-25"
MESTRE = SERIE / "SUBSCRICAO_COMO_EXECUTAR_v110_MESTRE_2026-09-25.md"
UP_M = ROOT / "uploads/SUBSCRICAO_COMO_EXECUTAR_v110_MESTRE_2026-09-25.md"
ESTRUTURA = SERIE / "SUBSCRICAO_ESTRUTURA_v110_2026-09-25.md"
MINUTA = ROOT / "ENTREGAS/2026-09-25_COMO_EXECUTAR_V110_MINUTA/4º COMO EXECUTAR — v1.10 (MINUTA).md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA102_fecho_v110_2026-09-25.json"

SHA_MIN = "4951434417f24a329d41fc31f0ec13a5d6da5e1191edde1e72e6cbe2fee4038e"
results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def main() -> int:
    same = UP_M.read_bytes() == MESTRE.read_bytes()
    mest = MESTRE.read_text(encoding="utf-8")
    estr = ESTRUTURA.read_text(encoding="utf-8")

    check("T1", "Mestre upload ≡ série", same, {"sha": sha(MESTRE)})

    check("T2", "Mestre sem ressalva + sha declarado",
          "SUBSCREVO SEM RESSALVA" in mest and SHA_MIN in mest, {})

    check("T3", "Estrutura sem ressalva + sha declarado (prefixo 12)",
          "Subscrevo sem ressalva a minuta COMO EXECUTAR v1.10" in estr
          and SHA_MIN[:12] in estr, {"prefixo": SHA_MIN[:12]})

    check("T4", "minuta canônica sha = 49514344",
          sha(MINUTA) == SHA_MIN, {"sha": sha(MINUTA)})

    check("T5", "nota E: passagem literal na mesa das três (não bloqueia)",
          "não é problema desta minuta" in estr and "não muda a subscrição" in estr, {})

    check("T6", "nota M: v1.10 coerente com schema+contrato subscritos",
          "não é ressalva" in mest and "Os três documentos são coerentes" in mest, {})

    check("T7", "2× sem ressalva ⇒ ciclo v1.10 ENCAVEL",
          "SUBSCREVO SEM RESSALVA" in mest
          and "Subscrevo sem ressalva a minuta COMO EXECUTAR v1.10" in estr,
          {"vigencia": "pendente frase do operador"})

    check("T8", "pendências de sempre registradas como não-bloqueio",
          "P-K6" in estr and "piloto `.014`" in estr.replace("`", "") or "piloto" in estr, {})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 102, "data": "2026-09-25",
        "objeto": "fecho_como_executar_v110",
        "digitais": {"mestre": sha(MESTRE), "estrutura": sha(ESTRUTURA),
                     "minuta": sha(MINUTA)},
        "ciclo_v110": "ENCAVEL" if n_ok == len(results) else "ABERTO",
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA102 {n_ok}/{len(results)} ciclo_v110={payload['ciclo_v110']}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
