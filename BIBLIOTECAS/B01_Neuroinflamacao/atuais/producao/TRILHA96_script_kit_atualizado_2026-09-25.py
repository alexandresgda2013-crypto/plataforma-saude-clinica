#!/usr/bin/env python3
"""TRILHA 96 — kit ATUALIZADO recebido 2026-09-25 (corpus 17/09).

  T1  uploads ≡ série (todos os arquivos novos)
  T2  Schema-Claim ≡ kit 15/09 (56dc0e94) — inalterado
  T3  COMO EXECUTAR ≡ v1.9 recebido 20/09 (1cd90b40) — inalterado
  T4  Bloco v1.8: cabeçalho data 2026-09-17; sha 7db41d40
  T5  Lista v1.5: cabeçalho data 2026-09-17; sha 20efa89f
  T6  Bloco: 27 claims (8 aprovado + 15 aprovado_com_ressalva + 4 em_busca); 0 sem status
  T7  6 claims novos vs 15/09: .014 .015 .017 .023 .028 .032; 0 removidos
  T8  .014 presente: aprovado_com_ressalva; pmids 39938607, 34864233
  T9  Lista 43 ids; .012b/.012c agora são alvos (fecha lacuna C85)
  T10 bloco ⊆ lista (todo claim tem entrada na lista); lista − bloco = próximos alvos (16)
  T11 usado_em_biblioteca 23× nao (nenhum claim clínico na canônica ainda)
  T12 P-K1/P-K2 AUSENTES (sentido_do_achado 0×, ressalvas[] 0×) — esperado: ciclo do kit pendente
  T13 ESTRUTURA MESTRE mudou → v2.2 (sha novo)
  T14 IDS/ESCOPO/CANDIDATOS ≡ 15/09
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path("/home/user")
SERIE = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_ATUALIZADO_recebido_2026-09-25"
OLD = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15"
UP = ROOT / "uploads"
V19 = ROOT / "BIBLIOTECAS/_documentos_serie/COMO_EXECUTAR_v1.9_recebido_2026-09-20/4º_COMO_EXECUTAR___v1_9.md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA96_kit_atualizado_2026-09-25.json"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def claims_of(text: str) -> list[str]:
    ids = []
    for p in re.split(r"(?=- claim_id:)", text):
        m = re.match(r"- claim_id:\s*(\S+)", p)
        if m and m.group(1).startswith("B1."):
            ids.append(m.group(1))
    return ids


def main() -> int:
    files = [
        "1º IDS_OFICIAIS.md",
        "2º PROTOCOLO DE ESCOPO — B1 (v1.3).md",
        "3º SCHEMA-CLAIM — v1.2.md",
        "4º_COMO_EXECUTAR___v1_9.md",
        "5º_LISTA_CANÔNICA___B1__SM-02_V1_5.md",
        "6º_BLOCO_DE_ESTADO__v1_8.md",
        "CANDIDATOS_IDS_OFICIAIS — v1.0.md",
        "ESTRUTURA_MESTRE_v2_2.md",
    ]
    same = all((UP / f).read_bytes() == (SERIE / f).read_bytes() for f in files)
    check("T1", "uploads ≡ série (8 arquivos)", same, {
        "sha_bloco": sha(SERIE / files[5]), "sha_lista": sha(SERIE / files[4])})

    sc_new = sha(SERIE / "3º SCHEMA-CLAIM — v1.2.md")
    sc_old = sha(OLD / "3º SCHEMA-CLAIM — v1.2.md")
    check("T2", "Schema-Claim ≡ 15/09", sc_new == sc_old == "56dc0e94cc2e2983384190706bc00977db38f82d4d2663c1c4eca533683b0e79",
          {"sha": sc_new})

    v19_new = sha(SERIE / "4º_COMO_EXECUTAR___v1_9.md")
    v19_old = sha(V19.read_bytes() and str(V19)) if False else sha(V19)
    check("T3", "COMO EXECUTAR ≡ v1.9 de 20/09",
          v19_new == v19_old == "1cd90b407facee81692d668919829c9d6d5a149b1309424c6f012e26cd81f586",
          {"sha": v19_new})

    b = (SERIE / files[5]).read_text(encoding="utf-8")
    l = (SERIE / files[4]).read_text(encoding="utf-8")
    check("T4", "Bloco v1.8 datado 2026-09-17", "ESTADO v1.8 — 2026-09-17" in b,
          {"sha": sha(SERIE / files[5]), "bytes": (SERIE / files[5]).stat().st_size})
    check("T5", "Lista v1.5 datada 2026-09-17", "v1.5 — 2026-09-17" in l,
          {"sha": sha(SERIE / files[4]), "bytes": (SERIE / files[4]).stat().st_size})

    ids = claims_of(b)
    stats = Counter()
    for p in re.split(r"(?=- claim_id:)", b):
        m = re.match(r"- claim_id:\s*(\S+)", p)
        if not m or not m.group(1).startswith("B1."):
            continue
        st = re.search(r"^[ \t]*status:\s*(\S+)", p, re.M)
        stats[st.group(1) if st else "SEM_STATUS"] += 1
    ok6 = len(ids) == 27 and stats.get("aprovado") == 8 and stats.get("aprovado_com_ressalva") == 15 \
        and stats.get("em_busca") == 4 and stats.get("SEM_STATUS", 0) == 0
    check("T6", "Bloco: 27 claims · 8/15/4 · 0 sem status", ok6,
          {"total": len(ids), "status": dict(stats)})

    b_old = (OLD / "6º BLOCO DE ESTADO  v1.6.md").read_text(encoding="utf-8")
    ids_old = claims_of(b_old)
    novos = sorted(set(ids) - set(ids_old))
    removidos = sorted(set(ids_old) - set(ids))
    check("T7", "6 novos vs 15/09; 0 removidos",
          novos == ["B1.SM02.014", "B1.SM02.015", "B1.SM02.017", "B1.SM02.023", "B1.SM02.028", "B1.SM02.032"]
          and not removidos and len(ids_old) == 21,
          {"novos": novos, "removidos": removidos, "old": len(ids_old)})

    m014 = re.search(r"- claim_id:\s*B1\.SM02\.014\b(.*?)(?=- claim_id:)", b, re.S)
    ok8 = bool(m014) and "aprovado_com_ressalva" in m014.group(1) and set(re.findall(r"pmid:\s*(\d+)", m014.group(1))) == {"39938607", "34864233"}
    check("T8", ".014: aprovado_com_ressalva; pmids 39938607+34864233", ok8, {})

    alvos = set(re.findall(r"B1\.SM02\.\d+[a-z]*", l))
    ok9 = "B1.SM02.012b" in alvos and "B1.SM02.012c" in alvos and len(alvos) == 43
    check("T9", "Lista 43 ids; .012b/.012c agora alvos", ok9,
          {"n": len(alvos), "header": l.splitlines()[2] if len(l.splitlines()) > 2 else ""})

    fora_bloco = sorted(alvos - set(ids))
    check("T10", "bloco ⊆ lista; lista−bloco = 16 próximos alvos",
          not (set(ids) - alvos) and len(fora_bloco) == 16,
          {"bloco_sem_lista": sorted(set(ids) - alvos), "proximos": fora_bloco})

    usado = Counter(re.findall(r"usado_em_biblioteca:\s*(\S+)", b))
    check("T11", "usado_em_biblioteca 23× nao", usado.get("nao") == 23 and len(usado) == 1,
          dict(usado))

    check("T12", "P-K1/P-K2 ainda ausentes (ciclo do kit pendente)",
          "sentido_do_achado" not in b and not re.search(r"^ressalvas:", b, re.M),
          {"sentido": b.count("sentido_do_achado")})

    check("T13", "ESTRUTURA MESTRE → v2.2 (mudou)",
          sha(SERIE / "ESTRUTURA_MESTRE_v2_2.md") != sha(OLD / "ESTRUTURA MESTRE.md"),
          {"sha_novo": sha(SERIE / "ESTRUTURA_MESTRE_v2_2.md")})

    ok14 = (
        sha(SERIE / files[0]) == sha(OLD / files[0])
        and sha(SERIE / files[1]) == sha(OLD / files[1])
        and sha(SERIE / files[6]) == sha(OLD / files[6])
    )
    check("T14", "IDS / ESCOPO / CANDIDATOS ≡ 15/09", ok14, {})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 96, "data": "2026-09-25",
        "objeto": "kit_atualizado_corpus_17_09",
        "corpus": "Bloco v1.8 + Lista v1.5 (ambos 2026-09-17)",
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA96 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
