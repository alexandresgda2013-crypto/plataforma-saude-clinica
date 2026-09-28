#!/usr/bin/env python3
"""TRILHA 97 — ciclo do kit: minuta Schema-Claim v1.3 (P-K1/P-K2/P-K3/P-K5).

  T1  minuta existe e declara escopo somente-v1.2
  T2  baseline v1.2 = 56dc0e94 (inalterado)
  T3  contrato de saída vigente = 841532da (base normativa)
  T4  P-K1: sentido_do_achado enum EXATO do v3.1 (3 valores, sem renomear)
  T5  P-K2: tipos exatos do contrato (condicao_aplicacao|heterogeneidade|maturidade_evidencia)
  T6  P-K3: fonte única escrita (só ressalvas[tipo=condicao_aplicacao]; nota/moderadores/sentido proibidos)
  T7  P-K5: enum grau_maturidade idêntico ao N2 v1.4 (sem renomear)
  T8  proibições R-1 presentes (default de status/nivel/achado/prosa)
  T9  inverte não materializa (P-K6) registrado no kit
  T10 moderadores v1.2 preservados (efeitos 4)
  T11 validadores V-K1..V-K5 declarados
  T12 migração: sem reescrita retroativa; falha dura sem sentido_do_achado
  T13 campos v1.2 preservados (claim_id, status, evidence_role, uso,
       especificidade, nota_ressalva, fontes base, usado_em, fila)
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/user")
MINUTA = ROOT / "ENTREGAS/2026-09-25_CICLO_KIT_MINUTA_V13/MINUTA_SCHEMA_CLAIM_v1.3_2026-09-25.md"
V12 = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/3º SCHEMA-CLAIM — v1.2.md"
V31 = ROOT / "Ferramentas de geração e auditoria/02_fase1_gpm_profundidade/3º SCHEMA-CLAIM — MECANISMO v3.1.md"
N2 = ROOT / "BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
CONTRATO = ROOT / "BIBLIOTECAS/_documentos_serie/CONTRATO_SAIDA_CLAIMKIT_rev2_vigente_2026-09-24/CONTRATO_SAIDA_CLAIMKIT_rev2_2026-09-24.md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA97_ciclo_kit_minuta_v13_2026-09-25.json"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def main() -> int:
    m = MINUTA.read_text(encoding="utf-8")
    check("T1", "minuta existe; declara escopo somente-v1.2",
          "MINUTA — não vigente" in m and "somente isto" in m, {"bytes": MINUTA.stat().st_size})

    check("T2", "baseline v1.2 inalterada", sha(V12) == "56dc0e94cc2e2983384190706bc00977db38f82d4d2663c1c4eca533683b0e79",
          {"sha": sha(V12)})

    check("T3", "contrato vigente é a base normativa da minuta",
          sha(CONTRATO) == "841532dad13cd3fea1356c9e23e37067e78876685db52d3c1f2cd8b2a96e535c"
          and "841532da" in m, {"sha_contrato": sha(CONTRATO)})

    v31 = V31.read_text(encoding="utf-8")
    check("T4", "P-K1 enum exato do v3.1 (3 valores)",
          "sentido_do_achado: suporta_relacao | refuta_relacao | inconclusivo" in v31
          and "sentido_do_achado: suporta_relacao | refuta_relacao | inconclusivo" in m, {})

    ok5 = all(t in m for t in ("condicao_aplicacao", "heterogeneidade", "maturidade_evidencia"))
    check("T5", "P-K2 tipos exatos do contrato", ok5, {})

    ok6 = (
        "FONTE ÚNICA DE CONDIÇÃO" in m
        and "NUNCA autoriza condicao" in m
        and m.count("NUNCA autoriza condicao") >= 3
    )
    check("T6", "P-K3 fonte única: nota/moderadores/sentido proibidos",
          ok6, {"proibicoes": m.count("NUNCA autoriza condicao")})

    n2 = json.loads(N2.read_text(encoding="utf-8"))
    gm_enum = [e for e in n2["properties"]["grau_maturidade"].get("enum", []) if e]
    ok7 = all(e in m for e in gm_enum) and "v3.1" in m
    check("T7", "P-K5 enum idêntico ao N2 (5 valores)", ok7, {"n2_enum": gm_enum})

    ok8 = all(s in m for s in (
        'inferir de status ("aprovado → suporta_relacao")',
        "inferir de nivel", "inferir de achado positivo", "inferir de prosa"))
    check("T8", "proibições R-1 (4 defaults) presentes", ok8, {})

    check("T9", "inverte não materializa (P-K6) no kit",
          "NÃO materializa em N2 v1.4" in m and "P-K6" in m, {})

    ok10 = "moderadores: [ ]" in m and all(e in m for e in ("atenua", "inverte", "amplifica", "nulo"))
    check("T10", "moderadores v1.2 preservados", ok10, {})

    ok11 = all(f"V-K{i}" in m for i in range(1, 6))
    check("T11", "validadores V-K1..V-K5 declarados", ok11, {})

    check("T12", "migração sem reescrita retroativa + falha dura",
          "NÃO são reescritos retroativamente" in m and "FALHA DE MATERIALIZAÇÃO" in m, {})

    campos_v12 = ["claim_id", "status:", "evidence_role", "uso:", "especificidade",
                  "nota_ressalva", "fontes:", "usado_em_biblioteca", "fila_realocacao"]
    check("T13", "campos v1.2 preservados", all(c in m for c in campos_v12),
          {"faltando": [c for c in campos_v12 if c not in m]})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 97, "data": "2026-09-25",
        "objeto": "ciclo_kit_minuta_schema_claim_v13",
        "minuta_sha": sha(MINUTA),
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA97 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
