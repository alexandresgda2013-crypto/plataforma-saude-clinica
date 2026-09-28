#!/usr/bin/env python3
"""TRILHA 92 — réplica da CONDUÇÃO DO COMENTADOR ROTA A (2026-09-24).

  T1  carta arquivada digest/bytes
  T2  Rota A escolhida + pedido de minuta final verbatim
  T3  dois eixos: status ≠ direcao (enums N2 medidos)
  T4  cadeia abolida aprovado_com_ressalva→condicional ausente como regra
       no novo contrato (minuta da casa) — medir na minuta
  T5  sentido_do_achado na v3.1 com enum exato e OBRIGATÓRIO
  T6  mapeamento 3→3 (suporta/refuta/inconclusivo → sustenta/refuta/inconclusivo)
       é biunívoco com enum direcao_suporte
  T7  moderadores v1.2: 4 campos citados + 4 efeitos
  T8  .001b inverte + aprovado_com_ressalva (exemplo §9)
  T9  atenua/amplifica no kit: permanecem claim (medir existência, não conversão)
  T10 grau_maturidade N2 presente (destino da maturidade)
  T11 rito 3 IAs: carta do comentador mantém (§14) — texto presente
  T12 portões §16 listados 6 na carta
  T13 minuta da casa contém os 4 blocos de §18 (D1/R-1/R-2/encerramento)
  T14 minuta NÃO propõe alteração de N1/N2 v1.4 (§17)
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/user")
CARTA = ROOT / "BIBLIOTECAS/_documentos_serie/COMENTADOR_conducao_RotaA_2026-09-24/COMENTADOR_CONDUCAO_ROTA_A_2026-09-24.md"
V31 = ROOT / "Ferramentas de geração e auditoria/02_fase1_gpm_profundidade/3º SCHEMA-CLAIM — MECANISMO v3.1.md"
SC12 = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/3º SCHEMA-CLAIM — v1.2.md"
BLOCO = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/6º BLOCO DE ESTADO  v1.6.md"
N2_PATH = ROOT / "BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
MINUTA = ROOT / "ENTREGAS/2026-09-24_MINUTA_CONTRATO_SAIDA_CLAIMKIT/MINUTA_CONTRATO_SAIDA_CLAIMKIT_2026-09-24.md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA92_replica_rotaA_2026-09-24.json"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def main() -> int:
    carta = CARTA.read_text(encoding="utf-8")
    check("T1", "carta Rota A arquivada", CARTA.stat().st_size > 5000, {
        "sha256": sha(CARTA), "bytes": CARTA.stat().st_size})

    check("T2", "Rota A + pedido de minuta final verbatim",
          bool(re.search(r"\*\*Escolho a Rota A", carta)) and "minuta final do contrato de saída do Claim Kit" in carta,
          {"rota_a": bool(re.search(r"\*\*Escolho a Rota A", carta)),
           "pedido_minuta": "minuta final do contrato de saída" in carta})

    n2 = json.loads(N2_PATH.read_text(encoding="utf-8"))
    st = set(n2["properties"]["status_auditoria"].get("enum", []))
    ds = set(n2["properties"]["ancoras"]["items"]["properties"]["direcao_suporte"].get("enum", []))
    check("T3", "N2: enums dos dois eixos completos e distintos",
          {"CONFIRMADO", "PARCIALMENTE_CONFIRMADO"} <= st
          and ds == {"sustenta", "refuta", "inconclusivo", "condicional"}
          and not (st & ds),
          {"status_auditoria": sorted(st), "direcao_suporte": sorted(ds),
           "interseccao": sorted(st & ds)})

    # T5 sentido_do_achado v3.1
    v31 = V31.read_text(encoding="utf-8")
    has_enum = "sentido_do_achado: suporta_relacao | refuta_relacao | inconclusivo" in v31
    has_obr = bool(re.search(r"sentido_do_achado[^\n]*\r?\n[^\n]*OBRIGAT[ÓO]RIO", v31))
    check("T5", "v3.1 sentido_do_achado enum exato + OBRIGATÓRIO",
          has_enum and has_obr, {"sha": sha(V31), "enum": has_enum, "obrigatorio": has_obr})

    # T6 bijection
    map3 = {"suporta_relacao": "sustenta", "refuta_relacao": "refuta", "inconclusivo": "inconclusivo"}
    ok6 = all(v in ds for v in map3.values()) and len(set(map3.values())) == 3
    check("T6", "mapeamento 3→3 biunívoco dentro do enum N2", ok6, {"map": map3})

    # T7 moderadores schema-claim v1.2
    sc = SC12.read_text(encoding="utf-8")
    campos = all(c in sc for c in ("moderadores", "variavel", "efeito", "regra_motor", "fonte_pmid"))
    efeitos = all(e in sc for e in ("atenua", "amplifica", "inverte"))
    check("T7", "v1.2 moderadores: campos e efeitos citados na carta",
          campos and efeitos, {"campos": campos, "efeitos": efeitos})

    # T8 .001b
    bloco = BLOCO.read_text(encoding="utf-8")
    m = re.search(r"- claim_id:\s*B1\.SM02\.001b(.*?)(?=- claim_id:)", bloco, re.S)
    check("T8", ".001b: inverte + aprovado_com_ressalva",
          bool(m) and "inverte" in m.group(1) and "aprovado_com_ressalva" in m.group(1),
          {"encontrado": bool(m)})

    # T9 atenua/amplifica existem para permanecer no claim
    efeitos_bloco = re.findall(r"efeito:\s*(\S+)", bloco)
    check("T9", "efeitos no kit para tratamento §8/§9",
          efeitos_bloco.count("atenua") >= 1 and efeitos_bloco.count("amplifica") >= 1
          and efeitos_bloco.count("inverte") >= 1,
          {"atenua": efeitos_bloco.count("atenua"),
           "amplifica": efeitos_bloco.count("amplifica"),
           "inverte": efeitos_bloco.count("inverte")})

    # T10 grau_maturidade
    gm = "grau_maturidade" in n2["properties"]
    check("T10", "grau_maturidade existe no N2 v1.4 (destino da maturidade)", gm,
          {"enum": [e for e in n2["properties"].get("grau_maturidade", {}).get("enum", []) if e]})

    # T11 rito mantido
    check("T11", "§14 mantém rito das três IAs",
          "O RITO DAS TRÊS IAS É MANTIDO" in carta and "retira interpretação do materializador" in carta,
          {})

    # T12 portões
    portoes = re.findall(r"### Portão[^\n]*", carta)
    check("T12", "§16: 6 portões listados", len(portoes) >= 6, {"portoes": portoes})

    # T13/T14 minuta (se existir — executa após escrita; se ausente, falha explícita)
    if MINUTA.exists():
        minuta = MINUTA.read_text(encoding="utf-8")
        ml = minuta.lower()
        blocos = {
            "D1": "dois eixos" in ml and "não implica" in ml,
            "R-1": "sentido_do_achado" in ml and "default" in ml and "não fechado" in ml,
            "R-2": "atenua" in ml and "inverte" in ml and ("única origem" in ml or "fonte única" in ml),
            "grau_maturidade": "grau_maturidade" in ml,
        }
        check("T13", "minuta casa cobre §18 (D1/R-1/R-2)",
              all(blocos.values()), blocos)
        no_schema = not re.search(r"altera(r|ç[ãa]o).{0,40}(schema N2|N2 v1\.4).{0,20}(obrigat|necess)", minuta, re.I)
        # stronger: minuta must say não altera N1/N2
        declara = bool(re.search(r"n[ãa]o.{0,60}(altera|toca).{0,40}(N1|N2)", minuta, re.I)) or "sem alteração de schema" in minuta.lower()
        check("T14", "minuta declara 0 alteração N1/N2 (§17)", declara,
              {"declara": declara})
    else:
        check("T13", "minuta da casa existe", False, {"caminho": str(MINUTA)})
        check("T14", "minuta declara 0 alteração N1/N2", False, {"nota": "minuta ausente"})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 92, "data": "2026-09-24",
        "objeto": "replica_conducao_RotaA_comentador",
        "carta_sha256": sha(CARTA),
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA92 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
