#!/usr/bin/env python3
"""TRILHA 101 — minuta COMO EXECUTAR v1.10 contra as 3 bases vigentes + C-1..C-5.

  T1  minuta existe; declara MINUTA não vigente
  T2  C-1: fechamento conjunto (IA3 não fecha sozinha) — frase presente;
       "emite parecer e redige o claim no schema" = 0×
  T3  C-2: três análises INDEPENDENTES/CEGAS; "segunda inspeção sobre a
       análise da IA 1" = 0×
  T4  C-3: retorno do parecer + confirmo/altero/mantenho sem apagar
  T5  C-4: divergência factual à fonte primária (não votação)
  T6  C-5: ressalvas preservadas no fechamento
  T7  4 decisões do Contrato de Saída no fechamento (estado/direção/ressalva/moderadores)
  T8  referências: Schema-Claim v1.3 (vigente) · contrato 841532da citado
  T9  materialização separada + portões §8
  T10 bases: contrato 841532da · schema 28cbc9c7 · corpus Bloco 7db41d40 / Lista 20efa89f
  T11 v1.9 base intacta (1cd90b40) — não alteramos o recebido
  T12 X-1: divergência cega é funcionamento correto
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/user")
MINUTA = ROOT / "ENTREGAS/2026-09-25_COMO_EXECUTAR_V110_MINUTA/4º COMO EXECUTAR — v1.10 (MINUTA).md"
V19 = ROOT / "BIBLIOTECAS/_documentos_serie/COMO_EXECUTAR_v1.9_recebido_2026-09-20/4º_COMO_EXECUTAR___v1_9.md"
CONTRATO = ROOT / "BIBLIOTECAS/_documentos_serie/CONTRATO_SAIDA_CLAIMKIT_rev2_vigente_2026-09-24/CONTRATO_SAIDA_CLAIMKIT_rev2_2026-09-24.md"
SCHEMA = ROOT / "BIBLIOTECAS/_documentos_serie/SCHEMA_CLAIM_v1.3_rev3_vigente_2026-09-25/3º SCHEMA-CLAIM — v1.3.md"
BLOCO = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_ATUALIZADO_recebido_2026-09-25/6º_BLOCO_DE_ESTADO__v1_8.md"
LISTA = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_ATUALIZADO_recebido_2026-09-25/5º_LISTA_CANÔNICA___B1__SM-02_V1_5.md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA101_minuta_v110_2026-09-25.json"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def main() -> int:
    m = MINUTA.read_text(encoding="utf-8")

    check("T1", "minuta existe; não vigente", MINUTA.stat().st_size > 20000
          and "MINUTA — não vigente" in m, {"bytes": MINUTA.stat().st_size})

    check("T2", "C-1 fechamento conjunto; frase v1.9 morta",
          "FECHAMENTO CONJUNTO" in m
          and "emite parecer e redige o claim no schema" not in m
          and "**emite parecer**" in m, {})

    check("T3", "C-2 análises independentes; frase v1.9 morta",
          m.count("INDEPENDENTE") >= 3
          and "segunda inspeção sobre a análise da IA 1" not in m
          and "CEGAS" in m, {"indep": m.count("INDEPENDENTE")})

    check("T4", "C-3 retorno + confirmo/altero/mantenho",
          "RETORNA às IAs 1 e 2" in m and "confirmo / altero / mantenho" in m, {})

    check("T5", "C-4 factual à fonte primária",
          "FONTE PRIMÁRIA, nunca à contagem" in m
          and "Direto contra o artigo (C-4)" in m, {})

    check("T6", "C-5 ressalvas preservadas",
          "C-5" in m and "PRESERVADAS no fechamento" in m
          and "nada de \"fechar limpo\"" in m, {})

    ok7 = all(s in m for s in (
        "**Estado:**", "**Direção por fonte:**", "**Tipo da ressalva:**", "**Moderadores:**"))
    check("T7", "4 decisões do Contrato de Saída no fechamento", ok7, {})

    check("T8", "refs: Schema-Claim v1.3 + contrato 841532da",
          "Schema-Claim v1.3" in m and "841532da" in m and "28cbc9c7" in m, {})

    check("T9", "materialização separada + portões §8",
          "PASSO SEPARADO" in m and "portões do Contrato de Saída §8" in m, {})

    check("T10", "3 bases vigentes com digitais conferidas",
          sha(CONTRATO) == "841532dad13cd3fea1356c9e23e37067e78876685db52d3c1f2cd8b2a96e535c"
          and sha(SCHEMA) == "28cbc9c76006f485f340da124aa1795833afa56d38e6572a9279d94a88f6b94c"
          and sha(BLOCO) == "7db41d405cdeca181eef9ce3d294797f88c8e5e65fc800dac504f60fa9ed4563"
          and sha(LISTA) == "20efa89f9aed9837074a93f6aa92325a652b3c3fa250e398c98100f3d1ee28d3",
          {"contrato": sha(CONTRATO)[:8], "schema": sha(SCHEMA)[:8],
           "bloco": sha(BLOCO)[:8], "lista": sha(LISTA)[:8]})

    check("T11", "v1.9 recebida intacta",
          sha(V19) == "1cd90b407facee81692d668919829c9d6d5a149b1309424c6f012e26cd81f586",
          {"sha": sha(V19)})

    check("T12", "X-1 divergência cega = funcionamento correto",
          "funcionamento correto, não falha" in m, {})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 101, "data": "2026-09-25",
        "objeto": "minuta_como_executar_v110",
        "minuta_sha": sha(MINUTA),
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA101 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
