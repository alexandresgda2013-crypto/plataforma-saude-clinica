#!/usr/bin/env python3
"""TRILHA 95 — RÉPLICA FINAL minuta rev.2 ↔ duas subscrições · encerramento de D1.

  T1  Mestre upload ≡ série + digital
  T2  Estrutura: "Subscrevo sem ressalva" (texto arquivado)
  T3  Mestre: "SUBSCREVO SEM RESSALVA" + formal P-K1..P-K6
  T4  rev.2 sha declarada 841532da… confere
  T5  rev.2: inverte não materializa; P-K6; granularidade; sem par inválido ativo
  T6  rev.2: P-K1..P-K6 na pergunta; P-K4 superada
  T7  N2 allOf: reprodução do que ambos assinaram (condicional⇒req; sustenta/refuta⇒null)
  T8  v3.1: sentido_do_achado OBRIGATÓRIO (Estrutura confirmou; Mestre recebeu)
  T9  mapeamento R-1 biunívoco no enum N2
  T10 retratação do Mestre presente (erro rev.1 declarado)
  T11 alcance vigente × travas registrado pelo Estrutura (contrato derivação; .001b espera)
  T12 estado formal: 2× sem ressalva ⇒ D1 PODE ENCERRAR (critério §19 Comentador)
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/user")
SERIE = ROOT / "BIBLIOTECAS/_documentos_serie/SUBSCRICOES_MINUTA_SAIDA_2026-09-24"
MESTRE = SERIE / "SUBSCRICAO_rev2_CLAIMKIT_MESTRE_2026-09-24.md"
UP_M = ROOT / "uploads/SUBSCRICAO_rev2_CLAIMKIT_MESTRE_2026-09-24.md"
ESTRUTURA = SERIE / "SUBSCRICAO_REV2_ESTRUTURA_2026-09-24.md"
MINUTA = ROOT / "ENTREGAS/2026-09-24_MINUTA_REV2_INVERTE_PENDENCIA/MINUTA_CONTRATO_SAIDA_CLAIMKIT_rev2_2026-09-24.md"
N2_PATH = ROOT / "BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
V31 = ROOT / "Ferramentas de geração e auditoria/02_fase1_gpm_profundidade/3º SCHEMA-CLAIM — MECANISMO v3.1.md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA95_replica_final_rev2_encerramento_2026-09-24.json"

EXPECTED_MINUTA = "841532dad13cd3fea1356c9e23e37067e78876685db52d3c1f2cd8b2a96e535c"
results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def main() -> int:
    same_m = UP_M.read_bytes() == MESTRE.read_bytes()
    check("T1", "Mestre rev.2 upload ≡ série", same_m, {
        "sha": sha(MESTRE), "bytes": MESTRE.stat().st_size, "upload_ok": same_m})

    mest = MESTRE.read_text(encoding="utf-8")
    estr = ESTRUTURA.read_text(encoding="utf-8")

    check("T2", "Estrutura: subscreve sem ressalva",
          "**Subscrevo sem ressalva.**" in estr and "D1 pode encerrar" in estr,
          {"frase": "**Subscrevo sem ressalva.**" in estr})

    check("T3", "Mestre: SUBSCREVO SEM RESSALVA formal com P-K1..P-K6",
          "SUBSCREVO SEM RESSALVA" in mest
          and "mantidas as pendências P-K1..P-K6" in mest, {})

    m = MINUTA.read_text(encoding="utf-8")
    check("T4", "rev.2 sha = 841532da… declarada nas subscrições",
          sha(MINUTA) == EXPECTED_MINUTA,
          {"sha": sha(MINUTA), "esperado": EXPECTED_MINUTA})

    check("T5", "rev.2: inverte não materializa + P-K6 + granularidade + sem par ativo",
          "**O `inverte` NÃO materializa em N2**" in m
          and "P-K6" in m
          and "fail-closed **por artefato**" in m
          and "Materializa como **duas relações N2 complementares**" not in m, {})

    check("T6", "rev.2: pergunta P-K1..P-K6; P-K4 superada",
          "P-K1..P-K6" in m and "superada pela P-K6" in m and "P-K1..P-K5" not in m, {})

    n2 = json.loads(N2_PATH.read_text(encoding="utf-8"))
    allOf = n2["properties"]["ancoras"]["items"].get("allOf", [])
    r_cond = any(
        r.get("if", {}).get("properties", {}).get("direcao_suporte", {}).get("const") == "condicional"
        and "condicao" in r.get("then", {}).get("required", []) for r in allOf)
    r_null = any(
        r.get("if", {}).get("properties", {}).get("direcao_suporte", {}).get("enum")
        == ["sustenta", "refuta", "inconclusivo"]
        and r.get("then", {}).get("properties", {}).get("condicao", {}).get("type") == "null"
        for r in allOf)
    check("T7", "N2 allOf (base do que ambos assinaram)",
          r_cond and r_null, {"condicional_req": r_cond, "null_quando_nao_condicional": r_null})

    v31 = V31.read_text(encoding="utf-8")
    check("T8", "v3.1 sentido_do_achado OBRIGATÓRIO (citado e confirmado)",
          "sentido_do_achado: suporta_relacao | refuta_relacao | inconclusivo" in v31
          and bool(re.search(r"sentido_do_achado[^\n]*\r?\n[^\n]*OBRIGAT[ÓO]RIO", v31)),
          {"sha": sha(V31)})

    ds = set(n2["properties"]["ancoras"]["items"]["properties"]["direcao_suporte"].get("enum", []))
    check("T9", "mapeamento R-1 no enum N2",
          {"sustenta", "refuta", "inconclusivo"} <= ds,
          {"enum": sorted(ds)})

    check("T10", "Mestre retrata erro da rev.1 (§1)",
          "retratação" in mest.lower() and "Estava errado" in mest, {})

    check("T11", "Estrutura registra alcance: vigente = derivação; .001b espera v1.5",
          "O que fica **vigente**" in estr and "espera até o v1.5" in estr.replace("até o", "até o"), {
          "vigente": "O que fica **vigente**" in estr,
          "001b": ".001b" in estr})

    check("T12", "2× sem ressalva ⇒ D1 pode encerrar (§19)",
          "**Subscrevo sem ressalva.**" in estr and "SUBSCREVO SEM RESSALVA" in mest,
          {"estrutura_sem": True, "mestre_sem": True,
           "proximo": "encerramento formal + registro na governança"})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 95, "data": "2026-09-24",
        "objeto": "replica_final_rev2_encerramento_D1",
        "digitais": {"mestre_rev2": sha(MESTRE), "estrutura_rev2": sha(ESTRUTURA),
                     "minuta_rev2": sha(MINUTA)},
        "D1": "ENCERRAVEL" if n_ok == len(results) else "ABERTA",
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA95 {n_ok}/{len(results)} D1={payload['D1']}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
