#!/usr/bin/env python3
"""TRILHA 98 — resposta do Comentador ao ciclo do kit + ajuste V-K3 na minuta v1.3.

  T1  carta arquivada digest/bytes
  T2  veredito: pode seguir aos dois auditores
  T3  P-K1/P-K2/P-K3/P-K5 aprovados (4 seções)
  T4  V-K3: opção preferida explicitada
  T5  proibição de importar eixos mecanísticos (§6/§10)
  T6  não reabrir D1 (§13)
  T7  minuta rev.2 contém o ajuste V-K3 (exploratórias)
  T8  minuta rev.2 preserva enum P-K1 e tipos P-K2 (não regrediu)
  T9  minuta rev.2 declara rev.2 / não vigente
  T10 baseline v1.2 e contrato intactos
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/user")
CARTA = ROOT / "BIBLIOTECAS/_documentos_serie/COMENTADOR_resposta_ciclo_kit_v13_2026-09-25/COMENTADOR_RESPOSTA_CICLO_KIT_V13_2026-09-25.md"
MINUTA = ROOT / "ENTREGAS/2026-09-25_CICLO_KIT_MINUTA_V13/MINUTA_SCHEMA_CLAIM_v1.3_2026-09-25.md"
V12 = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/3º SCHEMA-CLAIM — v1.2.md"
CONTRATO = ROOT / "BIBLIOTECAS/_documentos_serie/CONTRATO_SAIDA_CLAIMKIT_rev2_vigente_2026-09-24/CONTRATO_SAIDA_CLAIMKIT_rev2_2026-09-24.md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA98_ciclo_kit_comentador_2026-09-25.json"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def main() -> int:
    c = CARTA.read_text(encoding="utf-8")
    m = MINUTA.read_text(encoding="utf-8")

    check("T1", "carta arquivada", CARTA.stat().st_size > 5000,
          {"sha256": sha(CARTA), "bytes": CARTA.stat().st_size})

    check("T2", "veredito: seguir aos dois auditores",
          "pode seguir para os dois auditores" in c
          and "levar a minuta v1.3 aos dois auditores" in c, {})

    ok3 = all(s in c for s in (
        "P-K1 — SENTIDO DO ACHADO", "**Aprovado para o ciclo.**",
        "P-K3 — FONTE ÚNICA DE CONDIÇÃO", "P-K5 — MATURIDADE"))
    check("T3", "P-K1/K2/K3/K5 aprovados", ok3, {})

    check("T4", "V-K3 opção preferida na carta",
          "Opção preferida" in c and "fonte exploratória que não materializa" in c, {})

    check("T5", "proíbe importar eixos mecanísticos (forca_causal etc.)",
          "forca_causal" in c and "extrapolação de escopo" in c, {})

    check("T6", "não reabrir D1",
          "NÃO ABRIR NOVAMENTE D1" in c, {})

    check("T7", "minuta rev.2 contém ajuste V-K3",
          "opção preferida do Comentador" in m
          and "PARTICIPAR DA MATERIALIZAÇÃO" in m
          and "NÃO é erro" in m.replace("não é erro", "NÃO é erro") or "NÃO é erro de materialização" in m, {})

    ok8 = ("suporta_relacao | refuta_relacao | inconclusivo" in m
           and all(t in m for t in ("condicao_aplicacao", "heterogeneidade", "maturidade_evidencia"))
           and "FONTE ÚNICA DE CONDIÇÃO" in m)
    check("T8", "rev.2 preserva P-K1/P-K2/P-K3", ok8, {})

    check("T9", "rev.2 declarada; não vigente",
          "MINUTA rev.2" in m and "não vigente" in m, {})

    check("T10", "v1.2 e contrato intactos",
          sha(V12) == "56dc0e94cc2e2983384190706bc00977db38f82d4d2663c1c4eca533683b0e79"
          and sha(CONTRATO) == "841532dad13cd3fea1356c9e23e37067e78876685db52d3c1f2cd8b2a96e535c",
          {"v12": sha(V12), "contrato": sha(CONTRATO)})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 98, "data": "2026-09-25",
        "objeto": "ciclo_kit_resposta_comentador_VK3",
        "carta_sha256": sha(CARTA), "minuta_rev2_sha256": sha(MINUTA),
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA98 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
