#!/usr/bin/env python3
"""TRILHA 105 — minuta COMO EXECUTAR v1.11 (paradas E-04) vs v1.10 vigente.

  T1  v1.10 vigente intacta (49514344)
  T2  v1.11 declara MINUTA e a correção E-04
  T3  paradas na sequência (ENTREGA → PÁRA)
  T4  comando do operador explícito
  T5  quem avança sozinho = fora do rito
  T6  corpo fora do cabeçalho/sequência é idêntico ao v1.10
  T7  portões/G3/4 decisões intactos
  T8  frases mortas da v1.9 não voltaram
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/home/user")
V10 = ROOT / "BIBLIOTECAS/_documentos_serie/COMO_EXECUTAR_v1.10_vigente_2026-09-25/4º COMO EXECUTAR — v1.10.md"
V11 = ROOT / "ENTREGAS/2026-09-25_V110_PARADAS_MINUTA/4º COMO EXECUTAR — v1.11 (MINUTA).md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA105_minuta_v111_2026-09-25.json"
SHA10 = "4951434417f24a329d41fc31f0ec13a5d6da5e1191edde1e72e6cbe2fee4038e"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def strip_header(t: str) -> str:
    return t[t.find("## Destino dos claims"):]


def strip_seq(t: str) -> str:
    a = t.find("### Sequência obrigatória")
    b = t.find("**Divergência cega entre as três")
    assert a > 0 and b > a
    return t[:a] + t[b:]


def main() -> int:
    t10 = V10.read_text(encoding="utf-8")
    t11 = V11.read_text(encoding="utf-8")

    check("T1", "v1.10 vigente intacta", sha(V10) == SHA10, {"sha": sha(V10)})
    check("T2", "v1.11 declara MINUTA e correção E-04",
          "v1.11 (MINUTA" in t11 and "E-04" in t11, {})
    # T3 (reforço do Comentador 25/09): verificar ORDEM operacional,
    # não só contagem: ENTREGA → PÁRA → COMANDO → próxima etapa
    seq = t11[t11.find("### Sequência obrigatória"):t11.find("### Paradas obrigatórias")]
    order_marks = [
        "ENTREGA análise 1 → ⛔ PÁRA",
        "ENTREGA análise 2 → ⛔ PÁRA",
        "ENTREGA análise 3 + PARECER → ⛔ PÁRA",
        "COM COMANDO DO OPERADOR: comparação",
        "COM COMANDO DO OPERADOR: FECHAMENTO CONJUNTO",
    ]
    positions = [seq.find(m) for m in order_marks]
    ordered = all(pos >= 0 for pos in positions) and positions == sorted(positions)
    check("T3", "paradas na sequência: ORDEM ENTREGA→PÁRA→COMANDO por transição",
          ordered and "Paradas obrigatórias (E-04" in t11,
          {"marcas": dict(zip(order_marks, positions)), "ordem_ok": ordered,
           "count_PARA": t11.count("PÁRA")})
    check("T4", "comando do operador explícito",
          "COM COMANDO DO OPERADOR" in t11, {})
    check("T5", "fora do rito para quem avança",
          "fora do rito" in t11, {})
    b10, b11 = strip_seq(strip_header(t10)), strip_seq(strip_header(t11))
    check("T6", "corpo fora do cabeçalho/sequência idêntico", b10 == b11,
          {"len10": len(b10), "len11": len(b11)})
    check("T7", "portões/G3/4 decisões intactos",
          all(x in t11 for x in ("G3 detalhado", "4 decisões",
                                 "portões do Contrato de Saída §8",
                                 "Paradas obrigatórias")), {})
    check("T8", "frases mortas v1.9 não voltaram",
          "segunda inspeção sobre a análise da IA 1" not in t11, {})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 105, "data": "2026-09-25",
        "objeto": "minuta_v111_paradas",
        "v11_sha": sha(V11),
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA105 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
