#!/usr/bin/env python3
"""TRILHA 103 — comunicação do ENSAIO PRÉ-PILOTO contra as 3 bases vigentes.

  T1  comunicação arquivada (digest/bytes)
  T2  3 bases citadas com dígitos corretos (841532da · 28cbc9c7 · 49514344)
       e digitais reais conferem
  T3  ensaio ≠ piloto oficial (não substitui; desenho do v1.10 preservado
      na execução oficial)
  T4  nenhuma base normativa alterada pelo ensaio (declaração + lista N1/N2)
  T5  classificação operacional × normativa (só normativa abre ciclo)
  T6  sem ajuste silencioso ("nenhum ajuste silenciosamente")
  T7  tríade dedicada do piloto oficial com pacotes sem acesso cruzado
  T8  atribuição transitória + retorno aos territórios
  T9  pergunta do ensaio é operacional (executar v1.10 ponta a ponta)
  T10 v1.10 vigente intacta (49514344)
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/home/user")
CARTA = ROOT / "BIBLIOTECAS/_documentos_serie/COMUNICACAO_ENSAIO_PRE_PILOTO_2026-09-25/COMUNICACAO_ENSAIO_PRE_PILOTO_2026-09-25.md"
V110 = ROOT / "BIBLIOTECAS/_documentos_serie/COMO_EXECUTAR_v1.10_vigente_2026-09-25/4º COMO EXECUTAR — v1.10.md"
CONTRATO = ROOT / "BIBLIOTECAS/_documentos_serie/CONTRATO_SAIDA_CLAIMKIT_rev2_vigente_2026-09-24/CONTRATO_SAIDA_CLAIMKIT_rev2_2026-09-24.md"
SCHEMA = ROOT / "BIBLIOTECAS/_documentos_serie/SCHEMA_CLAIM_v1.3_rev3_vigente_2026-09-25/3º SCHEMA-CLAIM — v1.3.md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA103_ensaio_prepiloto_2026-09-25.json"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def main() -> int:
    c = CARTA.read_text(encoding="utf-8")
    check("T1", "comunicação arquivada", CARTA.stat().st_size > 5000,
          {"sha256": sha(CARTA), "bytes": CARTA.stat().st_size})

    ok2 = (
        "`841532da`" in c and "`28cbc9c7`" in c and "`49514344`" in c
        and sha(CONTRATO) == "841532dad13cd3fea1356c9e23e37067e78876685db52d3c1f2cd8b2a96e535c"
        and sha(SCHEMA) == "28cbc9c76006f485f340da124aa1795833afa56d38e6572a9279d94a88f6b94c"
        and sha(V110) == "4951434417f24a329d41fc31f0ec13a5d6da5e1191edde1e72e6cbe2fee4038e"
    )
    check("T2", "3 bases citadas e digitais reais conferem", ok2, {
        "contrato": sha(CONTRATO)[:8], "schema": sha(SCHEMA)[:8], "v110": sha(V110)[:8]})

    check("T3", "ensaio ≠ piloto oficial; desenho v1.10 preservado no oficial",
          "O ensaio não substitui o piloto oficial" in c
          and "análises cegas independentes" in c
          and "não altera a regra do piloto oficial" in c, {})

    check("T4", "bases normativas intocadas pelo ensaio",
          "Nenhuma das três bases normativas vigentes será modificada" in c
          and "N1;" in c and "N2." in c, {})

    check("T5", "classificação operacional × normativa",
          "problema operacional de execução" in c
          and "problema real de norma/contrato" in c
          and "novo ciclo documental" in c, {})

    check("T6", "sem ajuste silencioso",
          "nenhum ajuste será feito silenciosamente" in c, {})

    check("T7", "tríade dedicada com pacotes sem acesso cruzado",
          "ChatGPT dedicado" in c and "Arena dedicado" in c
          and "Claude dedicado" in c and "sem acesso às análises produzidas pelas outras" in c, {})

    check("T8", "atribuição transitória + retorno aos territórios",
          "atribuição transitória" in c and "retorno" in c.lower()
          and "terrifícios" not in c, {"retorna ao seu território": "retorna ao seu território" in c})

    check("T9", "pergunta do ensaio operacional",
          "executar o COMO EXECUTAR v1.10 de ponta a ponta" in c, {})

    check("T10", "v1.10 vigente intacta",
          sha(V110) == "4951434417f24a329d41fc31f0ec13a5d6da5e1191edde1e72e6cbe2fee4038e",
          {"sha": sha(V110)})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 103, "data": "2026-09-25",
        "objeto": "comunicacao_ensaio_prepiloto",
        "carta_sha256": sha(CARTA),
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA103 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
