#!/usr/bin/env python3
"""TRILHA 90 — réplica da SOLUÇÃO DO COMENTADOR D1 (2026-09-24).

  T1  carta arquivada digest + bytes
  T2  N2 v1.4: status_auditoria, direcao_suporte, condicao existem com enums citados
  T3  N2 v1.4: if/then de condicao (condicional exige; não-condicional proíbe)
  T4  direcao_suporte enum = sustenta|refuta|inconclusivo|condicional
  T5  claim B1.SM02.001 no Bloco: aprovado_com_ressalva + nota verbatim do §12
  T6  Schema-Claim: NÃO tem ressalvas[] estruturadas / tipo_ressalva (lacuna que a carta propõe preencher)
  T7  kit: 7 nota_ressalva; ao menos 1 heterogeneidade (exemplo §12/§4.3)
  T8  L-06: inferência silenciosa 1× (§8/§13 da carta)
  T9  r77 casa tinha a cadeia aprovado_com_ressalva→condicional (objeto da abolição §5/§16)
  T10 confronto r78 existia D1 com mapeamento único × roteio (base declarada)
  T11 dois eixos: status_auditoria e direcao_suporte são propriedades distintas no N2
       (status no vínculo, direcao_suporte em ancoras[]) — colapso era de derivação, não de schema
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/user")
CARTA = ROOT / "BIBLIOTECAS/_documentos_serie/COMENTADOR_resolucao_D1_2026-09-24/COMENTADOR_SOLUCAO_D1_2026-09-24.md"
N2_PATH = ROOT / "BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
BLOCO = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/6º BLOCO DE ESTADO  v1.6.md"
SCHEMA_CLAIM = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/3º SCHEMA-CLAIM — v1.2.md"
L06 = ROOT / "BIBLIOTECAS/_documentos_serie/MESTRE_L06_minuta3_consolidada_rev6_recebida_2026-09-22/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev6_2026-09-22.md"
R77 = ROOT / "ENTREGAS/2026-09-23_CLASSIFICACAO_INTERFACE_CLAIM_N1N2/CLASSIFICACAO_INTERFACE_CLAIM_N1N2_2026-09-23.md"
R78 = ROOT / "ENTREGAS/2026-09-23_CONFRONTO_INTERFACE_PARECERES/CONFRONTO_INTERFACE_PARECERES_2026-09-23.md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA90_replica_solucao_D1_2026-09-24.json"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def main() -> int:
    carta = CARTA.read_text(encoding="utf-8")
    check("T1", "carta D1 arquivada", CARTA.stat().st_size > 5000, {
        "sha256": sha(CARTA), "bytes": CARTA.stat().st_size,
    })

    n2 = json.loads(N2_PATH.read_text(encoding="utf-8"))
    check("T2", "N2: status_auditoria + direcao_suporte + condicao com enums citados", (
        "PARCIALMENTE_CONFIRMADO" in n2["properties"]["status_auditoria"].get("enum", [])
        and set(n2["properties"]["ancoras"]["items"]["properties"]["direcao_suporte"].get("enum", []))
        == {"sustenta", "refuta", "inconclusivo", "condicional"}
        and "condicao" in n2["properties"]["ancoras"]["items"]["properties"]
    ), {
        "status_enum": n2["properties"]["status_auditoria"].get("enum"),
        "direcao_enum": n2["properties"]["ancoras"]["items"]["properties"]["direcao_suporte"].get("enum"),
    })

    # if/then: condicional → condicao required; sustenta etc → condicao null
    blob = json.dumps(n2)
    # specs in allOf of anchors
    anchor_allof = n2["properties"]["ancoras"]["items"].get("allOf", [])
    has_cond_if = any(
        "condicional" in json.dumps(x) and "condicao" in json.dumps(x)
        for x in anchor_allof
    )
    check("T3", "N2 if/then liga condicional ↔ condicao (mínimo textual no allOf das âncoras)",
          has_cond_if and len(anchor_allof) >= 2,
          {"allOf_anchors_count": len(anchor_allof), "contem_condicional_condicao": has_cond_if})

    ds = n2["properties"]["ancoras"]["items"]["properties"]["direcao_suporte"]
    check("T4", "enum direcao_suporte exatamente os 4 valores",
          set(ds.get("enum", [])) == {"sustenta", "refuta", "inconclusivo", "condicional"},
          {"enum": ds.get("enum")})

    bloco = BLOCO.read_text(encoding="utf-8")
    m = re.search(
        r"- claim_id:\s*B1\.SM02\.001\b.*?status:\s*(\S+).*?nota_ressalva:\s*\"([^\"]+)\"",
        bloco, re.S,
    )
    ok5 = bool(m) and m.group(1) == "aprovado_com_ressalva" and m.group(2) == "Efeito por sexo diverge entre estudos — ver .001b"
    check("T5", "B1.SM02.001: status e nota_ressalva verbatim do §12",
          ok5, {"status": m.group(1) if m else None, "nota": m.group(2) if m else None})

    sc = SCHEMA_CLAIM.read_text(encoding="utf-8")
    has_struct = bool(re.search(r"^ressalvas:", sc, re.M)) or "tipo_ressalva" in sc
    check("T6", "Schema-Claim v1.2 SEM lista estruturada de ressalvas (lacuna proposta no §6)",
          not has_struct and "nota_ressalva" in sc and "aprovado_com_ressalva" in sc,
          {"ressalvas_linha": bool(re.search(r"^ressalvas:", sc, re.M)),
           "tipo_ressalva": "tipo_ressalva" in sc, "nota_ressalva": "nota_ressalva" in sc})

    ress = re.findall(r'nota_ressalva:\s*"([^"]+)"', bloco)
    het = [r for r in ress if "heterogene" in r.lower() or "diverg" in r.lower() or "sexo" in r.lower()]
    check("T7", "kit tem ressalvas não-condicionais (heterogeneidade/divergência)",
          len(ress) >= 5 and len(het) >= 2,
          {"total": len(ress), "heterogene_ou_diverg": len(het), "amostra": het[:3]})

    l06 = L06.read_text(encoding="utf-8")
    check("T8", "L-06: inferência silenciosa 1×",
          l06.count("inferência silenciosa") == 1,
          {"ocorrencias": l06.count("inferência silenciosa")})

    r77 = R77.read_text(encoding="utf-8")
    chain = "direcao_suporte = condicional" in r77 or "direcao_suporte=condicional" in r77
    check("T9", "minuta r77 da casa continha a cadeia status→condicional (objeto da abolição)",
          chain and "aprovado_com_ressalva" in r77,
          {"cadeia_presente": chain})

    r78 = R78.read_text(encoding="utf-8")
    check("T10", "base r78: D1 documentada (mapeamento único × roteio)",
          "mapeamento único" in r78 and ("roteio" in r78 or "roteio por tipo" in r78) and "D1" in r78,
          {"mapeamento_unico": "mapeamento único" in r78, "D1": "D1" in r78})

    # two axes live in different places of N2
    status_on_vinculo = "status_auditoria" in n2["properties"]
    dir_na_ancora = "direcao_suporte" in n2["properties"]["ancoras"]["items"]["properties"]
    status_na_ancora = "status_auditoria" in n2["properties"]["ancoras"]["items"]["properties"]
    check("T11", "eixos em camadas distintas do N2 (status no vínculo; direção na âncora)",
          status_on_vinculo and dir_na_ancora and not status_na_ancora,
          {"status_no_vinculo": status_on_vinculo, "direcao_na_ancora": dir_na_ancora,
           "status_na_ancora": status_na_ancora,
           "nota": "colapso era regra de derivação Claim→N2, não colisão de propriedades no schema"})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 90, "data": "2026-09-24",
        "objeto": "replica_solucao_D1_comentador",
        "carta_sha256": sha(CARTA),
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA90 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
