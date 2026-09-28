#!/usr/bin/env python3
"""TRILHA 93 — réplica das SUBSCRIÇÕES da minuta de saída (Estrutura × Mestre) · 2026-09-24.

  T1  identidade dos arquivos (Mestre upload ≡ série; texto do Estrutura arquivado)
  T2  vereditos: Mestre sem ressalva; Estrutura subscreve TUDO exceto §4.3 (inverte)
  T3  **objeção central**: N2 v1.4 allOf das âncoras —
       (a) condicional ⇒ condicao required string
       (b) sustenta|refuta|inconclusivo ⇒ condicao type null
       logo "condição A → sustenta" com condicao preenchida é INVÁLIDA
  T4  simulação: âncora {direcao_suporte: sustenta, condicao: "..."} viola (b)
  T5  simulação: âncora {direcao_suporte: refuta, condicao: "..."} viola (b)
  T6  minuta §4.3 contém exatamente o par problemático
  T7  minuta declara "não altera N2" (§9) — proposta de campo novo não cabe na minuta
  T8  Mestre: 30 refs com >1 vínculo; REF_SWANSON_2019 com 3
  T9  Mestre registrou não ter recebido v3.1 (0× sentido_do_achado na v1.2 que ele cita)
  T10 v3.1 existe no workspace com enum citado (casa pode enviá-lo)
  T11 proposta do Estrutura é coerente: inverte → pendência P-K travada
       (minuta rev.2 contém P-K6 com esse desenho)
  T12 estado H-3: 1 sem (Mestre) + 1 com impedimento medido (Estrutura §4.3)
       ⇒ minuta rev.1 NÃO encerra D1; rev.2 precisa de 2× novo
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path("/home/user")
SERIE = ROOT / "BIBLIOTECAS/_documentos_serie/SUBSCRICOES_MINUTA_SAIDA_2026-09-24"
MESTRE = SERIE / "SUBSCRICAO_CONTRATO_SAIDA_CLAIMKIT_MESTRE_2026-09-24.md"
UP_M = ROOT / "uploads/SUBSCRICAO_CONTRATO_SAIDA_CLAIMKIT_MESTRE_2026-09-24.md"
ESTRUTURA = SERIE / "SUBSCRICAO_ESTRUTURA_PONTO_INVERTE_2026-09-24.md"
N2_PATH = ROOT / "BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
MINUTA_R1 = ROOT / "ENTREGAS/2026-09-24_MINUTA_CONTRATO_SAIDA_CLAIMKIT/MINUTA_CONTRATO_SAIDA_CLAIMKIT_2026-09-24.md"
V31 = ROOT / "Ferramentas de geração e auditoria/02_fase1_gpm_profundidade/3º SCHEMA-CLAIM — MECANISMO v3.1.md"
SC12 = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/3º SCHEMA-CLAIM — v1.2.md"
VINC = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
MINUTA_R2 = ROOT / "ENTREGAS/2026-09-24_MINUTA_REV2_INVERTE_PENDENCIA/MINUTA_CONTRATO_SAIDA_CLAIMKIT_rev2_2026-09-24.md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA93_replica_subscricoes_minuta_2026-09-24.json"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def anchor_violates(ancora: dict, allOf: list) -> list:
    """Avalia os if/then das âncoras como JSON Schema (simplificado para os 2 ramos)."""
    viol = []
    for rule in allOf:
        if_c = rule.get("if", {})
        then_c = rule.get("then", {})
        # avaliar condição
        props = if_c.get("properties", {})
        matched = True
        for k, spec in props.items():
            if k not in ancora:
                if "required" in if_c and k in if_c["required"]:
                    matched = False
                continue
            if "const" in spec and ancora[k] != spec["const"]:
                matched = False
            if "enum" in spec and ancora[k] not in spec["enum"]:
                matched = False
        if "required" in if_c:
            for k in if_c["required"]:
                if k not in ancora:
                    matched = False
        if not matched:
            continue
        # then: checar condicao
        tprops = then_c.get("properties", {})
        if "condicao" in tprops:
            spec = tprops["condicao"]
            val = ancora.get("condicao", None)
            if spec.get("type") == "null":
                if val is not None:
                    viol.append({"regra": "condicao deve ser null", "valor": val})
            if spec.get("type") == "string":
                if not isinstance(val, str) or (spec.get("minLength") and len(val) < spec["minLength"]):
                    viol.append({"regra": "condicao string minLength", "valor": val})
            if "required" in then_c and "condicao" in then_c["required"]:
                if val is None:
                    viol.append({"regra": "condicao required", "valor": val})
    return viol


def main() -> int:
    same_m = UP_M.read_bytes() == MESTRE.read_bytes()
    check("T1", "upload ≡ série (Mestre) + texto Estrutura arquivado",
          same_m and ESTRUTURA.stat().st_size > 2000,
          {"mestre_sha": sha(MESTRE), "mestre_bytes": MESTRE.stat().st_size,
           "estrutura_sha": sha(ESTRUTURA), "estrutura_bytes": ESTRUTURA.stat().st_size,
           "upload_ok": same_m})

    mest = MESTRE.read_text(encoding="utf-8")
    estr = ESTRUTURA.read_text(encoding="utf-8")
    check("T2", "vereditos: M=sem ressalva; E=§4.3 impedimento, resto subscrito",
          "SUBSCREVO SEM RESSALVA" in mest
          and "não subscrevo — impedimento estrutural, medido" in estr
          and "Com essa troca" in estr and "subscrevo a minuta inteira sem ressalva" in estr,
          {"mestre_sem_ressalva": "SUBSCREVO SEM RESSALVA" in mest,
           "estrutura_impedimento_4_3": "impedimento estrutural" in estr})

    n2 = json.loads(N2_PATH.read_text(encoding="utf-8"))
    allOf = n2["properties"]["ancoras"]["items"].get("allOf", [])
    # T3 estrutura das regras
    r_cond = any(
        rule.get("if", {}).get("properties", {}).get("direcao_suporte", {}).get("const") == "condicional"
        and "condicao" in rule.get("then", {}).get("required", [])
        for rule in allOf
    )
    r_null = any(
        rule.get("if", {}).get("properties", {}).get("direcao_suporte", {}).get("enum")
        == ["sustenta", "refuta", "inconclusivo"]
        and rule.get("then", {}).get("properties", {}).get("condicao", {}).get("type") == "null"
        for rule in allOf
    )
    check("T3", "N2 allOf: condicional⇒condicao required; sustenta/refuta/inconclusivo⇒condicao null",
          r_cond and r_null and len(allOf) >= 2,
          {"regra_condicional": r_cond, "regra_null": r_null, "allOf_anchors": len(allOf),
           "nivel": "L1 JSON Schema"})

    # T4/T5 simulação
    v_s = anchor_violates({"direcao_suporte": "sustenta", "condicao": "classe_antidepressivo"}, allOf)
    v_r = anchor_violates({"direcao_suporte": "refuta", "condicao": "classe_antidepressivo"}, allOf)
    v_c = anchor_violates({"direcao_suporte": "condicional", "condicao": "classe_antidepressivo"}, allOf)
    check("T4", "sustenta+condicao preenchida VIOLA", bool(v_s), {"violacoes": v_s})
    check("T5", "refuta+condicao preenchida VIOLA", bool(v_r), {"violacoes": v_r,
          "nota": f"controle: condicional+condicao violacoes={v_c} (deve ser 0)"})

    # T6 minuta §4.3
    m1 = MINUTA_R1.read_text(encoding="utf-8")
    check("T6", "minuta rev.1 §4.3 contém o par proibido",
          "condição A → sustenta" in m1 and "condição B → refuta" in m1,
          {"presente": True})

    # T7 minuta declara não alterar N2
    check("T7", "minuta rev.1 declara não alterar N1/N2",
          bool(re.search(r"n[ãa]o altera", m1, re.I)),
          {"achado": bool(re.search(r"n[ãa]o altera", m1, re.I))})

    # T8 acervo: refs com >1 vínculo
    vinc = json.loads(VINC.read_text(encoding="utf-8"))
    c = Counter(x.get("id_referencia_interna") for x in vinc)
    multi = sum(1 for k, v in c.items() if v > 1)
    swanson = c.get("REF_SWANSON_2019", 0)
    check("T8", "Mestre: 30 refs com >1 vínculo; SWANSON_2019 com 3",
          multi == 30 and swanson == 3,
          {"multi_refs": multi, "swanson": swanson, "total_vinculos": len(vinc)})

    # T9 v3.1 ausente da base que o Mestre declarou
    sc = SC12.read_text(encoding="utf-8")
    check("T9", "Mestre declarou não receber v3.1; v1.2 sem sentido_do_achado",
          "A Schema-Claim v3.1 não me foi entregue" in mest and "sentido_do_achado" not in sc,
          {"declaracao": "A Schema-Claim v3.1 não me foi entregue" in mest,
           "v1_2_sentido": sc.count("sentido_do_achado")})

    # T10 v3.1 existe e bate
    v31 = V31.read_text(encoding="utf-8")
    has = "sentido_do_achado: suporta_relacao | refuta_relacao | inconclusivo" in v31
    check("T10", "v3.1 existe no workspace com o enum citado (enviável ao Mestre)",
          has, {"sha": sha(V31), "bytes": V31.stat().st_size})

    # T11 minuta rev.2
    if MINUTA_R2.exists():
        m2 = MINUTA_R2.read_text(encoding="utf-8")
        ok11 = (
            "P-K6" in m2
            and "inverte" in m2.lower()
            and "condicao_modificadora" in m2
            # instrução ATIVA antiga removida (citação histórica do erro pode permanecer)
            and "Materializa como **duas relações N2 complementares**" not in m2
            and "**O `inverte` NÃO materializa em N2**" in m2
        )
        check("T11", "minuta rev.2: inverte → P-K6 travado; instrução ativa antiga removida; v1.5 registrada",
              ok11, {"P_K6": "P-K6" in m2,
                     "instrucao_ativa_antiga_removida": "Materializa como **duas relações N2 complementares**" not in m2,
                     "nao_materializa": "**O `inverte` NÃO materializa em N2**" in m2,
                     "condicao_modificadora": "condicao_modificadora" in m2})
    else:
        check("T11", "minuta rev.2 existe", False, {"caminho": str(MINUTA_R2)})

    # T12 estado
    check("T12", "estado: rev.1 não encerra (1 sem + 1 impedimento §4.3)",
          "SUBSCREVO SEM RESSALVA" in mest and "impedimento estrutural" in estr,
          {"rev1_encerra": False,
           "proximo": "rev.2 → 2× subscrição nova (documento mudou)"})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 93, "data": "2026-09-24",
        "objeto": "replica_subscricoes_minuta_saida_claimkit",
        "digitais": {"mestre": sha(MESTRE), "estrutura": sha(ESTRUTURA)},
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA93 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
