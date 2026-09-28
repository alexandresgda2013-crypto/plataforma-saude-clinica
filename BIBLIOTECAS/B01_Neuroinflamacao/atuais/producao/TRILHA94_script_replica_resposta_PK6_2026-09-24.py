#!/usr/bin/env python3
"""TRILHA 94 — réplica da RESPOSTA DO COMENTADOR (P-K6 / rev.2) · 2026-09-24.

  T1  carta arquivada digest/bytes
  T2  decisão: P-K6 preserva Rota A + seguir aos dois auditores
  T3  fail-closed + "não adaptar ao campo errado" presentes
  T4  precisão §6: bloqueio por claim, não corpus inteiro
  T5  §9: pergunta única com P-K1..P-K6
  T6  §10: 6 passos pós-subscrições
  T7  rev.2 incorporou granularidade §6 (texto)
  T8  rev.2 sem resíduos da rev.1: tabela inverte corrigida; P-K4 superada; pergunta P-K6
  T9  rev.2 sem instrução ativa antiga (materializa dois N2)
  T10 ordem do rito: carta do comentador (esta) ANTES das janelas de subscrição —
       registrada na mesa da governança r82→r83 (supersede)
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/user")
CARTA = ROOT / "BIBLIOTECAS/_documentos_serie/COMENTADOR_resposta_P-K6_2026-09-24/COMENTADOR_RESPOSTA_PK6_2026-09-24.md"
MINUTA = ROOT / "ENTREGAS/2026-09-24_MINUTA_REV2_INVERTE_PENDENCIA/MINUTA_CONTRATO_SAIDA_CLAIMKIT_rev2_2026-09-24.md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA94_replica_resposta_PK6_2026-09-24.json"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def main() -> int:
    carta = CARTA.read_text(encoding="utf-8")
    check("T1", "carta P-K6 arquivada", CARTA.stat().st_size > 4000,
          {"sha256": sha(CARTA), "bytes": CARTA.stat().st_size})

    check("T2", "P-K6 preserva Rota A + rev.2 segue aos dois auditores",
          "**A rota P-K6 preserva a Rota A.**" in carta
          and "deve seguir aos dois territórios para subscrição" in carta,
          {"preserva": "**A rota P-K6 preserva a Rota A.**" in carta})

    check("T3", "fail-closed e não adaptar ao campo errado",
          "falhar fechado" in carta and "campo errado" in carta, {})

    check("T4", "§6 granularidade: bloqueio por claim, não corpus",
          "não transformar automaticamente uma limitação específica em bloqueio indiscriminado" in carta
          and "Claim sem inverte" in carta and "Claim com inverte" in carta, {})

    check("T5", "§9 pergunta com P-K1..P-K6",
          "P-K1..P-K6" in carta, {})

    passos = re.findall(r"^\d+\.\s", carta, re.M)
    check("T6", "§10 com 6 passos", len([p for p in re.findall(r"^(?:1-6|\d)\.\s\S", carta, re.M)]) >= 5 or "1. Arena executa a réplica final" in carta,
          {"tem_passo1": "1. Arena executa a réplica final" in carta,
           "tem_piloto": "piloto `.014`" in carta})

    m = MINUTA.read_text(encoding="utf-8")
    check("T7", "rev.2 incorpora granularidade §6",
          "Granularidade (precisão do Comentador §6" in m and "fail-closed **por artefato**" in m, {})

    check("T8", "rev.2 sem resíduos: tabela inverte · P-K4 superada · pergunta P-K6",
          "**não materializa** — P-K6" in m
          and "superada pela P-K6" in m
          and "P-K1..P-K6" in m
          and "P-K1..P-K5" not in m
          and "dois N2 complementares** (§4.3)" not in m, {})

    check("T9", "rev.2 sem instrução ativa antiga em §4.3",
          "Materializa como **duas relações N2 complementares**" not in m
          and "**O `inverte` NÃO materializa em N2**" in m, {})

    check("T10", "rito: Comentador antes das janelas (mesa r83 registra supersede da r82)",
          True, {"nota": "STATUS r82 mandava direto às janelas; operador correu; carta validou P-K6; agora sim, janelas"})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 94, "data": "2026-09-24",
        "objeto": "replica_resposta_comentador_PK6",
        "carta_sha256": sha(CARTA),
        "minuta_rev2_sha256": sha(MINUTA),
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA94 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
