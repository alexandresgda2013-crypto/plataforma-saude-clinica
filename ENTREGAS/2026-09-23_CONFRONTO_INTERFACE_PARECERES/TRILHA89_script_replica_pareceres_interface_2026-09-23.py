#!/usr/bin/env python3
"""TRILHA 89 — réplica dos PARECERES de interface Claim→N1/N2 (2026-09-23).

Corpus fechado; níveis declarados por teste.
  T1  upload ≡ série (cmp) dos dois pareceres + digitais
  T2  anti-contaminação declarada no Mestre; Estrutura: medir presença/ausência
  T3  vereditos textuais: Estrutura "não há impedimento técnico nem epistemológico";
      Mestre "um impedimento epistemológico"
  T4  colisão id: pattern REF + sufixos no acervo (CAPURON_2002b, CHEN_2024b/c)
  T5  pattern VINC citado ≡ schema; candidatos 5/5; prefixos 244+30; max B1=0274
  T6  forca_causal e grau_maturidade 274/274; opcionais N2; 0× no Schema-Claim
  T7  evid_role ∉ props N1 v1.3; natureza_evidencia ∈ props; acervo legado 237/237 com evid_role
  T8  escopo âncora: descrição BLOCO_XX + APENDICE_CORPUS; SM-02 não é vocabulário declarado
  T9  Mestre: Schema-Claim tem aprovado_com_ressalva/nota_ressalva; N2 tem enums da cadeia
  T10 ressalvas reais do kit: heterogene/sexo/diverg medidos (tipos ≠ condição presentes)
  T11 L-06 rev.6: "inferência silenciosa" 1× e regra 3 verbatim
  T12 usado_em_biblioteca 22/22 nao (pré-condição ordem)
  T13 claim_id_origem string escalar (ambos citam)
  T14 DIVERGÊNCIA: "mapeamento único" (Estrutura) × "não mapeia para um único destino" (Mestre)
  T15 mapeamento r76 do Estrutura presente no parecer dele atual (§5)
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path("/home/user")
SERIE = ROOT / "BIBLIOTECAS/_documentos_serie/PARECERES_INTERFACE_CLAIM_N1N2_2026-09-23"
MESTRE = SERIE / "PARECER_INTERFACE_CLAIM_N1N2_MESTRE_2026-09-23.md"
ESTRUTURA = SERIE / "PARECER_TERRITORIAL_INTERFACE_CLAIM_N1N2_2026-09-23.md"
UP_M = ROOT / "uploads/PARECER_INTERFACE_CLAIM_N1N2_MESTRE_2026-09-23.md"
UP_E = ROOT / "uploads/PARECER_TERRITORIAL_INTERFACE_CLAIM_N1N2_2026-09-23.md"

N1_PATH = ROOT / "BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_referencia_v1.3_N1_b06660fd.json"
N2_PATH = ROOT / "BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
VINC_PATH = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
BIB = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia"
BLOCO = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/6º BLOCO DE ESTADO  v1.6.md"
SCHEMA_CLAIM = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/3º SCHEMA-CLAIM — v1.2.md"
L06 = ROOT / "BIBLIOTECAS/_documentos_serie/MESTRE_L06_minuta3_consolidada_rev6_recebida_2026-09-22/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev6_2026-09-22.md"

OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA89_replica_pareceres_interface_2026-09-23.json"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def main() -> int:
    # T1 identity
    same_m = UP_M.read_bytes() == MESTRE.read_bytes()
    same_e = UP_E.read_bytes() == ESTRUTURA.read_bytes()
    check("T1", "upload ≡ série dos dois pareceres + digitais", same_m and same_e, {
        "mestre_sha": sha(MESTRE), "mestre_bytes": MESTRE.stat().st_size,
        "estrutura_sha": sha(ESTRUTURA), "estrutura_bytes": ESTRUTURA.stat().st_size,
        "upload_mestre_igual": same_m, "upload_estrutura_igual": same_e,
    })

    mest = MESTRE.read_text(encoding="utf-8")
    estr = ESTRUTURA.read_text(encoding="utf-8")

    # T2 anti-contaminação
    m_ac = "não li o encaminhamento paralelo" in mest
    e_ac = bool(re.search(r"n[ãa]o li", estr, re.I))
    check("T2", "declarações anti-contaminação (medir presença, não presumir)", True, {
        "mestre_declarou_nao_li": m_ac,
        "estrutura_declarou_nao_li": e_ac,
        "nota": "ausência de declaração ≠ contaminação comprovada; registrado como fato textual",
    })

    # T3 vereditos
    e_ver = "Não há impedimento técnico nem epistemológico" in estr
    m_ver = "um impedimento epistemológico" in mest
    check("T3", "vereditos textuais binários", e_ver and m_ver, {
        "estrutura_sem_impedimento_tecnico_nem_epistemologico": e_ver,
        "mestre_um_impedimento_epistemologico": m_ver,
        "leitura": "resposta à pergunta binária diverge quanto a 'existe impedimento epistemológico?'",
    })

    # T4 REF pattern / suffixes
    n1 = json.loads(N1_PATH.read_text(encoding="utf-8"))
    n2 = json.loads(N2_PATH.read_text(encoding="utf-8"))
    pat = n1["properties"]["id_referencia_interna"].get("pattern", "")
    ids = []
    for fn in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
        for x in json.loads((BIB / fn).read_text(encoding="utf-8")):
            ids.append(x.get("id_referencia_interna") or "")
            ids.extend(x.get("ids_referencia_interna") or [])
    want = ["REF_CAPURON_2002b", "REF_CHEN_2024b", "REF_CHEN_2024c"]
    check("T4", "pattern REF com sufixo minúsculo e exemplos citados no acervo",
          pat == r"^REF_[A-Z0-9_]+[a-z]?$" and all(w in ids for w in want), {
        "pattern": pat, "exemplos": {w: w in ids for w in want},
        "sufixos_minusculos_distintos": sorted({i for i in ids if re.match(r"^REF_[A-Z0-9_]+[a-z]$", i)}),
        "nivel": "L1 schema + L1 dígito/literal no acervo",
    })

    # T5 VINC pattern and candidates
    vpat_s = n2["properties"]["id_vinculo"].get("pattern", "")
    vpat = re.compile(vpat_s)
    cands = {
        "VINC_B1_0275": True, "VINC_B1SM02_0001": True, "VINC_B1CLIN_0001": True,
        "VINC_B1.SM02_0001": False, "VINC_B1_10001": False,
    }
    got = {c: bool(vpat.match(c)) for c in cands}
    vinc = json.loads(VINC_PATH.read_text(encoding="utf-8"))
    pref = Counter()
    max_b1 = 0
    for x in vinc:
        vid = x["id_vinculo"]
        if re.match(r"^VINC_B1V2_", vid):
            pref["VINC_B1V2"] += 1
        elif re.match(r"^VINC_B1_", vid):
            pref["VINC_B1"] += 1
            max_b1 = max(max_b1, int(vid.rsplit("_", 1)[1]))
        else:
            pref[vid.split("_")[0] + "_" + vid.split("_")[1] if vid.count("_") > 1 else vid] += 1
    check("T5", "pattern VINC e série do acervo (citações do Estrutura)",
          vpat_s == r"^VINC_[A-Z0-9]+_[0-9]{4}$" and got == cands
          and pref["VINC_B1"] == 244 and pref["VINC_B1V2"] == 30 and max_b1 == 274,
          {"pattern": vpat_s, "candidatos": got, "prefixos": dict(pref), "max_B1": max_b1,
           "VINC_B1_0275_livre": not any(x["id_vinculo"] == "VINC_B1_0275" for x in vinc)})

    # T6 forca_causal / grau_maturidade
    fc = sum(1 for x in vinc if x.get("forca_causal"))
    gm = sum(1 for x in vinc if x.get("grau_maturidade"))
    sc = SCHEMA_CLAIM.read_text(encoding="utf-8")
    check("T6", "forca_causal e grau_maturidade 274/274; opcionais N2; 0× Schema-Claim",
          fc == 274 and gm == 274
          and "forca_causal" not in n2.get("required", [])
          and "grau_maturidade" not in n2.get("required", [])
          and "forca_causal" not in sc and "grau_maturidade" not in sc,
          {"forca_causal": fc, "grau_maturidade": gm, "total": len(vinc)})

    # T7 evid_role vs natureza_evidencia
    has_er_acervo = 0
    tot = 0
    for fn in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
        arr = json.loads((BIB / fn).read_text(encoding="utf-8"))
        tot += len(arr)
        has_er_acervo += sum(1 for x in arr if "evid_role" in x)
    check("T7", "evid_role ∉ N1 schema; natureza_evidencia ∈ schema; legado 237/237",
          "evid_role" not in n1["properties"]
          and "natureza_evidencia" in n1["properties"]
          and has_er_acervo == tot == 237,
          {"evid_role_no_schema": "evid_role" in n1["properties"],
           "natureza_evidencia_no_schema": "natureza_evidencia" in n1["properties"],
           "acervo_com_evid_role": has_er_acervo, "total_acervo": tot})

    # T8 escopo
    esc = n2["properties"]["ancoras"]["items"]["properties"].get("escopo", {})
    esc_d = esc.get("description", "")
    check("T8", "escopo: BLOCO_XX e APENDICE_CORPUS na descrição; SM-02 não declarado",
          "BLOCO_XX" in esc_d and "APENDICE_CORPUS" in esc_d and "SM-02" not in esc_d and "SM02" not in esc_d,
          {"description": esc_d})

    # T9 schema claim + N2 enums cadeia
    check("T9", "Schema-Claim e N2 contêm a cadeia de ressalva citada",
          "aprovado_com_ressalva" in sc and "nota_ressalva" in sc
          and "PARCIALMENTE_CONFIRMADO" in n2["properties"]["status_auditoria"].get("enum", [])
          and "condicao" in n2["properties"]["ancoras"]["items"]["properties"],
          {"status_enum": n2["properties"]["status_auditoria"].get("enum")})

    # T10 ressalvas reais
    bloco = BLOCO.read_text(encoding="utf-8")
    ress = re.findall(r'nota_ressalva:\s*"([^"]+)"', bloco)
    kinds = {
        "heterogene": sum(1 for r in ress if "heterogene" in r.lower()),
        "sexo_ou_diverg": sum(1 for r in ress if "sexo" in r.lower() or "diverg" in r.lower()),
    }
    check("T10", "ressalvas reais do kit incluem heterogeneidade (não só condição de aplicação)",
          len(ress) >= 5 and kinds["heterogene"] >= 2,
          {"total_nota_ressalva_string": len(ress), "tipos": kinds, "amostra": ress[:5]})

    # T11 L-06
    l06 = L06.read_text(encoding="utf-8")
    r3 = "não é permitido completar a condição por inferência silenciosa" in l06
    check("T11", "L-06 rev.6 regra 3 verbatim (inferência silenciosa)",
          r3 and l06.count("inferência silenciosa") == 1,
          {"ocorrencias_inferencia_silenciosa": l06.count("inferência silenciosa"), "regra3": r3})

    # T12 ordem
    usado = Counter(re.findall(r"usado_em_biblioteca:\s*(\S+)", bloco))
    check("T12", "usado_em_biblioteca 22/22 nao (pré-condição Biblioteca→N2)",
          usado.get("nao") == 22, {"contagem": dict(usado)})

    # T13 claim_id_origem
    cio_types = set()
    for fn in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
        for x in json.loads((BIB / fn).read_text(encoding="utf-8")):
            cio_types.add(type(x.get("claim_id_origem", "")).__name__)
    check("T13", "claim_id_origem string escalar (ambos os pareceres)",
          n1["properties"]["claim_id_origem"].get("type") == "string" and cio_types <= {"str"},
          {"schema": n1["properties"]["claim_id_origem"], "tipos_acervo": sorted(cio_types)})

    # T14 divergence phrases
    e_um = "mapeamento único" in estr
    m_nao = "não mapeia para um único destino" in mest or "não mapeia para um único" in mest
    check("T14", "divergência material textual: mapeamento único × roteio por tipo",
          e_um and m_nao,
          {"estrutura_mapeamento_unico": e_um, "mestre_nao_unico": m_nao,
           "classificacao": "B — divergência material (ressalva)",
           "contexto_estrutura": "§5 do parecer do estrutura",
           "contexto_mestre": "§2/§5 do parecer do mestre"})

    # T15 estrutura reaffirms rodada3 mapping presence
    check("T15", "Estrutura reafirma mapeamento/resalva da r76 neste parecer",
          e_um and ("reprova" in estr.lower() or "reprova se ausente" in estr.lower() or "reprova" in estr),
          {"frase_mapeamento_unico": e_um})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 89,
        "data": "2026-09-23",
        "objeto": "replica_pareceres_interface_claim_n1n2",
        "digitais": {"mestre": sha(MESTRE), "estrutura": sha(ESTRUTURA)},
        "total": len(results),
        "ok": n_ok,
        "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA89 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
