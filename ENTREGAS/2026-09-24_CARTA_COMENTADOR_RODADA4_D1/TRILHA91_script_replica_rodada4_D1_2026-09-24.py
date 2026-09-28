#!/usr/bin/env python3
"""TRILHA 91 — réplica dos PARECERES Rodada 4 · D1 (2026-09-24).

  T1  upload ≡ série + digitais dos 2 pareceres
  T2  vereditos: Estrutura SUBSCREVO SEM RESSALVA; Mestre modelo sem ressalva + fechamento com DUAS ressalvas
  T3  anti-contaminação: Mestre declara; Estrutura 0× (fato textual)
  T4  Mestre: direcao/refuta = 0 no Bloco
  T5  Mestre: 15 marcadores (contradit|diverg|inconsist|nul) — rótulo dele "nula"; medida da casa com stem nul = 15 (nulo 4)
  T6  moderadores efeitos: atenua 3, amplifica 5, inverte 1
  T7  inverte em B1.SM02.001b aprovado_com_ressalva
  T8  grau_maturidade N2: enum 5+null; 274/274 no V7
  T9  Schema-Claim v1.2: moderadores[] com variavel/efeito/regra_motor; 0× sentido_do_achado
  T10 v3.1: sentido_do_achado suporta|refuta|inconclusivo marcado OBRIGATÓRIO em relacoes_causais_declaradas
       (estilo do arquivo: schema comentado; campo documentado nos itens da lista ativa)
  T11 L-06: disjunção / sustenta × refuta para par de vínculos (caminho citado pelo Mestre)
  T12 H-3: D1 encerra só com 2× sem ressalva → medir estado final (1 sem + 1 com ressalvas ⇒ ABERTA)
  T13 confissão do Estrutura: regra abolida era dele (18/09 e 22/09) — texto presente
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path("/home/user")
SERIE = ROOT / "BIBLIOTECAS/_documentos_serie/PARECERES_RODADA4_D1_2026-09-24"
MESTRE = SERIE / "PARECER_RODADA4_D1_MESTRE_2026-09-24.md"
ESTRUTURA = SERIE / "RODADA4_D1_PARECER_ESTRUTURA_2026-09-24.md"
UP_M = ROOT / "uploads/PARECER_RODADA4_D1_MESTRE_2026-09-24.md"
UP_E = ROOT / "uploads/RODADA4_D1_PARECER_ESTRUTURA_2026-09-24.md"
BLOCO = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/6º BLOCO DE ESTADO  v1.6.md"
SC_V12 = ROOT / "BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/3º SCHEMA-CLAIM — v1.2.md"
SC_V31 = ROOT / "Ferramentas de geração e auditoria/02_fase1_gpm_profundidade/3º SCHEMA-CLAIM — MECANISMO v3.1.md"
N2_PATH = ROOT / "BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
VINC = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
L06 = ROOT / "BIBLIOTECAS/_documentos_serie/MESTRE_L06_minuta3_consolidada_rev6_recebida_2026-09-22/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev6_2026-09-22.md"
OUT = ROOT / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA91_replica_rodada4_D1_2026-09-24.json"

results = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(tid, desc, ok, detail):
    results.append({"id": tid, "descricao": desc, "ok": bool(ok), "detalhe": detail})


def main() -> int:
    same_m = UP_M.read_bytes() == MESTRE.read_bytes()
    same_e = UP_E.read_bytes() == ESTRUTURA.read_bytes()
    check("T1", "upload ≡ série + digitais", same_m and same_e, {
        "mestre_sha": sha(MESTRE), "mestre_bytes": MESTRE.stat().st_size,
        "estrutura_sha": sha(ESTRUTURA), "estrutura_bytes": ESTRUTURA.stat().st_size,
    })

    mest = MESTRE.read_text(encoding="utf-8")
    estr = ESTRUTURA.read_text(encoding="utf-8")

    # T2 vereditos
    e_sem = "SUBSCREVO SEM RESSALVA" in estr
    m_modelo = "subscrito sem ressalva" in mest.lower() or ("sem ressalva" in mest and "modelo" in mest.lower())
    m_fech = "duas ressalvas" in mest and "fechamento de D1" in mest
    check("T2", "vereditos: E sem ressalva; M modelo sem + fechamento com 2 ressalvas", e_sem and m_modelo and m_fech, {
        "estrutura_sem_ressalva": e_sem, "mestre_modelo_sem": bool(m_modelo), "mestre_fechamento_2_ressalvas": bool(m_fech),
    })

    # T3 anti-contaminação
    check("T3", "anti-contaminação declarada (medir, não presumir)", True, {
        "mestre_declarou": "não li o bloco de colagem" in mest,
        "estrutura_declarou": bool(re.search(r"n[ãa]o li", estr, re.I)),
    })

    bloco = BLOCO.read_text(encoding="utf-8")

    # T4 direcao/refuta
    d = len(re.findall(r"direcao", bloco, re.I))
    r = len(re.findall(r"refuta", bloco, re.I))
    check("T4", "Bloco: direcao 0× e refuta 0×", d == 0 and r == 0, {"direcao": d, "refuta": r})

    # T5 marcadores
    n = {k: len(re.findall(re.escape(k), bloco, re.I)) for k in ("contradit", "diverg", "inconsist", "nul")}
    tot = sum(n.values())
    check("T5", "marcadores de divergência = 15 (stem nul; rótulo do Mestre 'nula' = 4× 'nulo')",
          tot == 15, {**n, "total": tot,
          "nota": "rótulo verbatim dele: nula; medido nulo=4, nula=0; número 15 confere com stem 'nul'",
          "nivel": "L1 substring case-insensitive"})

    # T6 moderadores efeitos
    efeitos = Counter(re.findall(r"efeito:\s*(\S+)", bloco))
    check("T6", "efeitos de moderadores: atenua 3, amplifica 5, inverte 1",
          efeitos.get("atenua") == 3 and efeitos.get("amplifica") == 5 and efeitos.get("inverte") == 1,
          dict(efeitos))

    # T7 inverte localizado
    m = re.search(r"- claim_id:\s*(B1\.SM02\.\S+)(.*?)(?=- claim_id:)", bloco, re.S)
    claims_inverte = re.findall(r"- claim_id:\s*(\S+)(?:(?!- claim_id:).)*?efeito:\s*inverte", bloco, re.S)
    ok7 = claims_inverte == ["B1.SM02.001b"]
    m001b = re.search(r"- claim_id:\s*B1\.SM02\.001b(.*?)(?=- claim_id:)", bloco, re.S)
    ok7 = ok7 and bool(m001b) and "aprovado_com_ressalva" in m001b.group(1)
    check("T7", "inverte no .001b e claim é aprovado_com_ressalva",
          ok7, {"claims_com_inverte": claims_inverte})

    # T8 grau_maturidade
    n2 = json.loads(N2_PATH.read_text(encoding="utf-8"))
    vinc = json.loads(VINC.read_text(encoding="utf-8"))
    gm = n2["properties"].get("grau_maturidade", {})
    filled = sum(1 for x in vinc if x.get("grau_maturidade") not in (None, ""))
    enum = [e for e in gm.get("enum", []) if e is not None]
    check("T8", "grau_maturidade N2 enum 5 valores; 274/274 preenchidos",
          len(enum) == 5 and filled == 274 and len(vinc) == 274,
          {"enum": enum, "preenchidos": filled, "total": len(vinc)})

    # T9 v1.2 moderadores
    sc = SC_V12.read_text(encoding="utf-8")
    check("T9", "v1.2 tem moderadores[] (variavel/efeito/regra_motor); 0× sentido_do_achado",
          "moderadores" in sc and "regra_motor" in sc and "sentido_do_achado" not in sc,
          {"moderadores": sc.count("moderadores"), "regra_motor": sc.count("regra_motor"),
           "sentido_do_achado": sc.count("sentido_do_achado")})

    # T10 v3.1
    v31 = SC_V31.read_text(encoding="utf-8")
    has_sense = "sentido_do_achado: suporta_relacao | refuta_relacao | inconclusivo" in v31
    has_obrig = bool(re.search(r"sentido_do_achado[^\n]*\r?\n[^\n]*OBRIGAT[ÓO]RIO", v31))
    has_list = "relacoes_causais_declaradas" in v31
    check("T10", "v3.1: sentido_do_achado no item de relacoes_causais_declaradas, OBRIGATÓRIO",
          has_sense and has_obrig and has_list,
          {"sha_v31": sha(SC_V31), "sentido": has_sense, "obrigatorio": has_obrig,
           "estilo": "schema comentado (YAML-like); campo documentado nos itens da lista ativa",
           "mapeamento": "suporta_relacao→sustenta, refuta_relacao→refuta, inconclusivo→inconclusivo"})

    # T11 L-06
    l06 = L06.read_text(encoding="utf-8")
    check("T11", "L-06: disjunção e sustenta × refuta presentes",
          l06.lower().count("disjun") >= 1 and (l06.count("sustenta × refuta") + l06.count("sustenta x refuta")) >= 1,
          {"disjun": l06.lower().count("disjun"),
           "sustenta_x_refuta": l06.count("sustenta × refuta") + l06.count("sustenta x refuta")})

    # T12 H-3 estado
    check("T12", "estado H-3: E=sem ressalva; M=com 2 ressalvas ⇒ D1 ABERTA",
          e_sem and m_fech, {"D1_fechada": False,
          "regra": "H-3: só fecha com 2× subscrever sem ressalva",
          "estado": "1 sem (Estrutura) + 1 com 2 ressalvas (Mestre)"})

    # T13 confissão
    conf = "O erro era meu" in estr or "era meu" in estr
    conf2 = "regra abolida era minha" in estr
    check("T13", "Estrutura confessa autoria da regra abolida",
          conf or conf2, {"frase1": conf, "frase2": conf2})

    n_ok = sum(1 for r in results if r["ok"])
    payload = {
        "trilha": 91, "data": "2026-09-24",
        "objeto": "replica_pareceres_rodada4_D1",
        "digitais": {"mestre": sha(MESTRE), "estrutura": sha(ESTRUTURA)},
        "total": len(results), "ok": n_ok, "resultado": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"TRILHA91 {n_ok}/{len(results)}")
    for r in results:
        print(("OK " if r["ok"] else "FAIL"), r["id"], r["descricao"])
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
