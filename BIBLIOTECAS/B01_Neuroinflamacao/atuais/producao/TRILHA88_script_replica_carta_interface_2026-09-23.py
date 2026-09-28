#!/usr/bin/env python3
"""TRILHA 88 — réplica da CARTA DO COMENTADOR 2026-09-23 (interface Claim→N1/N2).

Mede, com corpus fechado e níveis declarados:
  T1  identidade da carta arquivada × digest esperado (após gravação)
  T2  anexo upload ≡ série (cmp byte)
  T3  anexo exemplos VINC_B1_0001..0006 existem na V7
  T4  trecho_ancora do anexo (VINC_B1_0001) ≡ trecho real
  T5  PMIDs do anexo na Bibliografia V7 (lista explícita)
  T6  claims do anexo existem no Bloco de Estado kit 15/09
  T7  N1 v1.3: claim_id_origem é string (não array); preenchidos/total
  T8  N1 v1.3: CLAIM_KIT_CLINICO ausente de origem_pipeline enum
  T9  Bibliografia V7: 0 duplicidade de pmid_oficial (dedup por pmid)
  T10 N2 v1.4: required inclui trecho_ancora, ancora_principal, ancoras
  T11 N2 v1.4: anchors item required = id_oficial, papel, direcao_suporte;
               condicao presente
  T12 Kit 15/09: 0× trecho_ancora/ancora_principal/ancoras/condicao
  T13 Kit: status aprovado / aprovado_com_ressalva contagens no Bloco
  T14 Bloco: nota_ressalva, usado_em_biblioteca presentes; schema-claim também
  T15 PMIDs distintos do Bloco fora da Bibliografia (reconciliação técnica)
  T16 claim_id_origem preenchidos: valores são claim_ids mecanísticos (proveniência),
       não listas — regra do comentador §10
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/user")
SERIE = ROOT / "BIBLIOTECAS/_documentos_serie/COMENTADOR_carta_interface_claim_N1N2_2026-09-23"
CARTA = SERIE / "CARTA_COMENTADOR_interface_claim_N1N2_2026-09-23.md"
ANEXO_SERIE = SERIE / "ESTRUTURAS_DE_JSONS_VINCULOS_PMIDS_BLOCO_2026-09-23.md"
ANEXO_UPLOAD = ROOT / "uploads/ESTRUTURAS DE JSONS VÍNCULOS,PMIDS, BLOCO DE ESTADO.md"

N1_PATH = ROOT / "BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_referencia_v1.3_N1_b06660fd.json"
N2_PATH = ROOT / "BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
VINC_PATH = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
BIB_DIR = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia"
BLOCO = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/6º BLOCO DE ESTADO  v1.6.md"
LISTA = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/5º LISTA CANÔNICA — B1  SM-02 V1.3.md"
SCHEMA_CLAIM = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/3º SCHEMA-CLAIM — v1.2.md"

OUT_JSON = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA88_replica_carta_interface_2026-09-23.json"

# digest da carta será preenchido na primeira execução de gravação; aqui medimos o arquivo como gravado.
EXPECTED_ANEXO_SHA = "c58617a976362428b0dc91d7c7a77551578e3a590e44bda6fa5bb23954a58886"

results = []


def check(tid: str, desc: str, ok: bool, detail: dict) -> None:
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def main() -> int:
    # T1 carta existe e tem digest estável
    carta_sha = sha256(CARTA)
    carta_bytes = CARTA.stat().st_size
    check("T1", "carta arquivada existe com digest mensurável", carta_bytes > 1000, {
        "sha256": carta_sha, "bytes": carta_bytes, "caminho": str(CARTA),
    })

    # T2 anexo upload ≡ série
    same = ANEXO_UPLOAD.read_bytes() == ANEXO_SERIE.read_bytes()
    check("T2", "anexo upload ≡ série (byte a byte)", same and sha256(ANEXO_SERIE) == EXPECTED_ANEXO_SHA, {
        "sha_upload": sha256(ANEXO_UPLOAD), "sha_serie": sha256(ANEXO_SERIE),
        "esperado": EXPECTED_ANEXO_SHA, "bytes": ANEXO_SERIE.stat().st_size,
    })

    # corpus load
    vinc = json.loads(VINC_PATH.read_text(encoding="utf-8"))
    by_id = {x["id_vinculo"]: x for x in vinc}
    biblio = {}
    biblio_files = {}
    for fn in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
        arr = json.loads((BIB_DIR / fn).read_text(encoding="utf-8"))
        biblio_files[fn] = len(arr)
        for x in arr:
            biblio[str(x["pmid_oficial"])] = x
    n1 = json.loads(N1_PATH.read_text(encoding="utf-8"))
    n2 = json.loads(N2_PATH.read_text(encoding="utf-8"))
    bloco = BLOCO.read_text(encoding="utf-8")
    schema_claim = SCHEMA_CLAIM.read_text(encoding="utf-8")
    lista = LISTA.read_text(encoding="utf-8")
    anexo = ANEXO_SERIE.read_text(encoding="utf-8")

    # T3 vínculos do anexo
    want_v = [f"VINC_B1_000{i}" for i in range(1, 7)]
    missing_v = [v for v in want_v if v not in by_id]
    check("T3", "VINC_B1_0001..0006 do anexo existem na V7", not missing_v, {
        "presentes": 6 - len(missing_v), "ausentes": missing_v, "total_v7": len(vinc),
    })

    # T4 trecho VINC_B1_0001 anexo ≡ real
    m = re.search(
        r'"id_vinculo": "VINC_B1_0001",.*?"trecho_ancora": "(.*?)",\n',
        anexo.replace("\r\n", "\n"),
        re.S,
    )
    trecho_ok = False
    anexo_trecho_len = 0
    if m:
        t = m.group(1).replace('\\"', '"')
        anexo_trecho_len = len(t)
        trecho_ok = t == by_id["VINC_B1_0001"]["trecho_ancora"]
    check("T4", "trecho_ancora VINC_B1_0001 do anexo ≡ arquivo real", trecho_ok, {
        "len_anexo": anexo_trecho_len,
        "len_real": len(by_id["VINC_B1_0001"]["trecho_ancora"]),
    })

    # T5 PMIDs citados no anexo
    anexo_pmids = ["10827143", "11927189", "28122130", "31005627", "22945416",
                   "38233395", "31427751", "36893912", "39089535", "31258105", "22832816"]
    in_bib = [p for p in anexo_pmids if p in biblio]
    out_bib = [p for p in anexo_pmids if p not in biblio]
    # 36893912 é o exemplo hipotético do comentador §5 — não precisa existir; mas medimos
    check("T5", "PMIDs do anexo medidos contra Bibliografia V7", True, {
        "citados": anexo_pmids, "em_biblio": in_bib, "fora_biblio": out_bib,
        "nota": "36893912 aparece na carta como exemplo conceitual de PMID; 22832816 é fonte de claim SM02.001b",
    })

    # T6 claims do anexo no Bloco
    want_c = ["B1.SM02.001", "B1.SM02.001b", "B1.SM02.001c", "B1.SM02.001d", "B1.SM02.002"]
    missing_c = [c for c in want_c if c not in bloco]
    check("T6", "claims de exemplo do anexo existem no Bloco kit 15/09", not missing_c, {
        "ausentes": missing_c, "arquivo": str(BLOCO),
    })

    # T7 claim_id_origem type
    cio_types = set()
    cio_filled = 0
    cio_values = []
    n1_total = 0
    for fn in biblio_files:
        arr = json.loads((BIB_DIR / fn).read_text(encoding="utf-8"))
        for x in arr:
            n1_total += 1
            v = x.get("claim_id_origem", None)
            cio_types.add(type(v).__name__)
            if isinstance(v, str) and v.strip():
                cio_filled += 1
                cio_values.append(v)
    schema_cio = n1["properties"].get("claim_id_origem", {})
    check("T7", "N1 claim_id_origem é string escalar (não lista)", 
          schema_cio.get("type") == "string" and cio_types <= {"str"}, {
        "schema_type": schema_cio.get("type"),
        "tipos_acervo": sorted(cio_types),
        "preenchidos": cio_filled, "total_n1": n1_total,
        "exemplos_valores": sorted(set(cio_values))[:5],
    })

    # T8 CLAIM_KIT_CLINICO no enum
    enum = n1["properties"].get("origem_pipeline", {}).get("enum", [])
    check("T8", "CLAIM_KIT_CLINICO ausente do enum origem_pipeline N1 v1.3",
          "CLAIM_KIT_CLINICO" not in enum, {
        "enum": enum, "legados_no_acervo_fora_do_enum": sorted({
            str(json.loads((BIB_DIR / fn).read_text(encoding="utf-8"))[i].get("origem_pipeline", ""))
            for fn in biblio_files
            for i in range(len(json.loads((BIB_DIR / fn).read_text(encoding="utf-8"))))
            if json.loads((BIB_DIR / fn).read_text(encoding="utf-8"))[i].get("origem_pipeline", "") not in enum
        }),
    })

    # T9 dedup pmid
    pmids = []
    for fn in biblio_files:
        for x in json.loads((BIB_DIR / fn).read_text(encoding="utf-8")):
            pmids.append(str(x["pmid_oficial"]))
    dups = sorted({p for p in pmids if pmids.count(p) > 1})
    check("T9", "Bibliografia V7 sem duplicidade de pmid_oficial", not dups, {
        "total_fichas": len(pmids), "pmids_distintos": len(set(pmids)),
        "duplicados": dups, "por_arquivo": biblio_files,
    })

    # T10 N2 required
    req = n2.get("required", [])
    need = ["trecho_ancora", "ancora_principal", "ancoras"]
    check("T10", "N2 v1.4 required inclui trecho_ancora, ancora_principal, ancoras",
          all(x in req for x in need), {"required": req})

    # T11 anchors
    anch = n2["properties"]["ancoras"]
    item = anch.get("items", {})
    item_req = item.get("required", [])
    props = sorted(item.get("properties", {}).keys())
    check("T11", "ancoras[] item required = id_oficial, papel, direcao_suporte; condicao existe",
          all(x in item_req for x in ("id_oficial", "papel", "direcao_suporte")) and "condicao" in props,
          {"required_item": item_req, "props_item": props})

    # T12 kit 0× chaves âncora
    probes = {}
    for term in ("trecho_ancora", "ancora_principal", "ancoras", "condicao"):
        probes[term] = {
            "bloco": len(re.findall(re.escape(term), bloco)),
            "lista": len(re.findall(re.escape(term), lista)),
            "schema_claim": len(re.findall(re.escape(term), schema_claim)),
        }
    check("T12", "Kit 15/09 sem chaves-âncora do N2 (0× em Bloco/Lista/Schema-Claim)",
          all(v["bloco"] == 0 and v["lista"] == 0 and v["schema_claim"] == 0 for v in probes.values()),
          probes)

    # T13 status counts
    # padrão exato com indentação opcional (C88-1: primeira régua exigiu coluna 0 e deu 0/0)
    aprov = len(re.findall(r"^[ \t]*status: aprovado[ \t]*$", bloco, re.M))
    ress = len(re.findall(r"^[ \t]*status: aprovado_com_ressalva[ \t]*$", bloco, re.M))
    check("T13", "Bloco: contagem de status aprovado / aprovado_com_ressalva",
          aprov == 8 and ress == 14, {"aprovado": aprov, "aprovado_com_ressalva": ress,
          "confissao": "C88-1: régua inicial sem indentação → 0/0; corrigida antes de publicar",
          "nota": "kit 15/09; se mudar, é corpus novo (pergunta de bytes ≥17/09 permanece)"})

    # T14 ressalva + usado_em_biblioteca
    check("T14", "Bloco e Schema-Claim carregam nota_ressalva e usado_em_biblioteca",
          ("nota_ressalva" in bloco and "usado_em_biblioteca" in bloco
           and "nota_ressalva" in schema_claim and "usado_em_biblioteca" in schema_claim),
          {
              "nota_ressalva_bloco": bloco.count("nota_ressalva"),
              "usado_em_biblioteca_bloco": bloco.count("usado_em_biblioteca"),
              "nota_ressalva_schema": schema_claim.count("nota_ressalva"),
              "usado_em_biblioteca_schema": schema_claim.count("usado_em_biblioteca"),
              "status_auditoria_bloco": bloco.count("status_auditoria"),
              "direcao_suporte_bloco": bloco.count("direcao_suporte"),
          })

    # T15 PMIDs do Bloco fora da Bibliografia
    bloco_pmids = sorted(set(re.findall(r"pmid:\s*(\d+)", bloco)))
    outside = sorted(set(bloco_pmids) - set(biblio))
    inside = sorted(set(bloco_pmids) & set(biblio))
    check("T15", "PMIDs distintos do Bloco medidos contra Bibliografia (reconciliação técnica)",
          True, {
              "bloco_pmids_distintos": len(bloco_pmids),
              "em_biblio": len(inside), "fora_biblio": len(outside),
              "lista_fora": outside,
              "nivel": "L1 — dígito exato em campo pmid: × pmid_oficial",
          })

    # T16 claim_id_origem values look like single claim ids (no lists/commas)
    bad = [v for v in cio_values if ("," in v or v.startswith("["))]
    check("T16", "claim_id_origem preenchido = um claim_id escalar (proveniência; não catálogo)",
          not bad and cio_filled > 0, {
              "preenchidos": cio_filled, "valores_com_virgula_ou_lista": bad,
              "exemplos": sorted(set(cio_values))[:8],
              "leitura_comentador_§10": "confirmada no acervo: um N1 → um claim de origem; uso múltiplo fica nos N2 via claim_id",
          })

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 88,
        "data": "2026-09-23",
        "objeto": "replica_carta_interface_comentador_claim_N1N2",
        "carta_sha256": carta_sha,
        "anexo_sha256": sha256(ANEXO_SERIE),
        "corpus": {
            "n1": str(N1_PATH),
            "n2": str(N2_PATH),
            "vinculos": str(VINC_PATH),
            "bibliografia": str(BIB_DIR),
            "bloco": str(BLOCO),
            "lista": str(LISTA),
            "schema_claim": str(SCHEMA_CLAIM),
        },
        "total": len(results),
        "ok": n_ok,
        "resultado": results,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA88 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
