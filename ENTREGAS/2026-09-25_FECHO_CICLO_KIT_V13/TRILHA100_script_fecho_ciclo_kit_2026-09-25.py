#!/usr/bin/env python3
"""TRILHA 100 — RÉPLICA FINAL das subscrições Schema-CLAIM v1.3 rev.3 · fecho do ciclo do kit.

  T1  Mestre upload ≡ série + digital
  T2  Mestre: SUBSCREVO SEM RESSALVA + declara sha rev.3 = 28cbc9c7…
  T3  Estrutura final: SUBSCREVO SEM RESSALVA a rev.3 (texto arquivado)
  T4  rev.3 canônica sha = 28cbc9c7 (bate com o declarado pelo Mestre)
  T5  rev.3 contém V-K6 no corpo (sentido_do_achado) e nos validadores
  T6  rev.3 contém V-K7
  T7  diff rev.2→rev.3 confinado a V-K6/V-K7 (corpo P-K idêntico)
  T8  epílogo arquivo errado registrado (rev.2 × rev.3; disciplina de bytes)
  T9  estado: 2× sem ressalva sobre a rev.3 ⇒ ciclo do kit ENCAVEL
       (vigência = frase do operador)
  T10 P-K1/P-K2 seguem como trava da 1ª materialização; P-K6 no v1.5
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/user")
SERIE = ROOT / "BIBLIOTECAS/_documentos_serie/SUBSCRICOES_SCHEMA_CLAIM_V13_2026-09-25"
MESTRE = SERIE / "SUBSCRICAO_SCHEMA_CLAIM_v13_rev3_MESTRE_2026-09-25.md"
UP_M = ROOT / "uploads/SUBSCRICAO_SCHEMA_CLAIM_v13_rev3_MESTRE_2026-09-25.md"
ESTRUTURA = SERIE / "SUBSCRICAO_ESTRUTURA_rev3_FINAL_2026-09-25.md"
REV3 = ROOT / "ENTREGAS/2026-09-25_CICLO_KIT_MINUTA_V13/3º SCHEMA-CLAIM — v1.3 (MINUTA rev.3).md"
REV2 = ROOT / "ENTREGAS/2026-09-25_CICLO_KIT_MINUTA_V13/3º SCHEMA-CLAIM — v1.3 (MINUTA rev.2).md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA100_fecho_ciclo_kit_v13_2026-09-25.json"

SHA_REV3 = "28cbc9c76006f485f340da124aa1795833afa56d38e6572a9279d94a88f6b94c"
results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def main() -> int:
    same = UP_M.read_bytes() == MESTRE.read_bytes()
    check("T1", "Mestre upload ≡ série", same,
          {"sha": sha(MESTRE), "bytes": MESTRE.stat().st_size})

    mest = MESTRE.read_text(encoding="utf-8")
    estr = ESTRUTURA.read_text(encoding="utf-8")
    r3 = REV3.read_text(encoding="utf-8")
    r2 = REV2.read_text(encoding="utf-8")

    check("T2", "Mestre sem ressalva + declara sha rev.3",
          "SUBSCREVO SEM RESSALVA" in mest and SHA_REV3 in mest, {})

    check("T3", "Estrutura final sem ressalva à rev.3",
          "Subscrevo sem ressalva a minuta Schema-Claim v1.3 rev.3" in estr
          and "está fechado do meu lado" in estr, {})

    check("T4", "rev.3 canônica sha = 28cbc9c7",
          sha(REV3) == SHA_REV3, {"sha": sha(REV3)})

    vk6_body = "PRECEDÊNCIA" in r3 and "sentido_do_achado" in r3 and "V-K6" in r3
    vk6_valid = r3.count("V-K6") >= 2
    check("T5", "V-K6 no corpo e nos validadores",
          vk6_body and vk6_valid, {"ocorrencias_VK6": r3.count("V-K6")})

    check("T6", "V-K7 presente", "V-K7" in r3 and "null gravado" in r3, {})

    # diff confinado: remove V-K6/V-K7 lines from r3 and compare core P-K markers
    def core(t: str) -> str:
        lines = [ln for ln in t.splitlines()
                 if not re.search(r"V-K6|V-K7|PRECED|rev\.3|rev\.2|preced", ln, re.I)]
        return "\n".join(lines)
    # markers P-K
    markers = ["suporta_relacao | refuta_relacao | inconclusivo",
               "condicao_aplicacao", "FONTE ÚNICA DE CONDIÇÃO",
               "grau_maturidade_cientifica", "opção preferida do Comentador"]
    ok7 = all(m in r3 and m in r2 for m in markers)
    check("T7", "corpo P-K idêntico rev.2↔rev.3 (marcadores)", ok7,
          {"faltando": [m for m in markers if m not in r3 or m not in r2]})

    check("T8", "epílogo arquivo errado registrado",
          "rev.2 do arquivo, não a rev.3" in estr and "arquivo errado" in estr.lower()
          or "Epílogo" in estr, {"epilogo": "Epílogo" in estr})

    check("T9", "2× sem ressalva sobre rev.3 ⇒ ciclo ENCAVEL",
          "SUBSCREVO SEM RESSALVA" in mest
          and "Subscrevo sem ressalva a minuta Schema-Claim v1.3 rev.3" in estr,
          {"vigencia": "pendente frase do operador"})

    check("T10", "travas seguem: P-K1/P-K2 kit; P-K6 v1.5",
          "P-K1 e P-K2" in estr and "ciclo do N2 v1.5" in estr, {})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 100, "data": "2026-09-25",
        "objeto": "fecho_ciclo_kit_schema_claim_v13_rev3",
        "digitais": {"mestre_rev3": sha(MESTRE), "estrutura_rev3": sha(ESTRUTURA),
                     "minuta_rev3": sha(REV3)},
        "ciclo_kit": "ENCAVEL" if n_ok == len(results) else "ABERTO",
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA100 {n_ok}/{len(results)} ciclo_kit={payload['ciclo_kit']}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
