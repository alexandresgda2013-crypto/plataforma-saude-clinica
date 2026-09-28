#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# motor_harmoniza.py — 2026-09-11 (Rodada de Harmonização, Fila A/B do ROTEIRO).
# Aplica as decisões D1–D8 de DECISOES_HARMONIZACAO_SCHEMA_2026-09-11.md sobre os
# vínculos das bibliotecas. REGRAS:
#   * lossless — todo valor original fica em nota_reparo (registro) + trilha (producao/)
#   * idempotente — re-rodar não duplica nem altera o que já está oficial
#   * dry-run por padrão; escrita só com --apply Bxx (uma biblioteca por vez)
#   * backup datado + escrita atômica via contrato.gravar do perito
#   * auto-verificação: bloqueantes do contrato antes/depois, impressos e na trilha
import json, glob, sys, collections
sys.path.insert(0, "/home/user/BIBLIOTECAS/_documentos_serie/bancada_at02/scripts")
from contrato import Contrato

DATA = "2026-09-11"
# ── mapas oficiais de tradução (D1, D2, D4, D6) ─────────────────────────────
MAP_STATUS_REF = {"CONFIRMADA": "VALIDADO", "PARCIAL": "TRIADO",
                  "VALIDADO_G3_IA": "VALIDADO", "PENDENTE_FULLTEXT": "TRIADO"}
MAP_EVID_ROLE = {"revisao_mecanistica": "review", "preclinico_mecanistico": "preclinical_mechanistic",
                 "meta_analise": "human_clinical"}
MAP_GRAU = {"moderado_suportado": "moderadamente_suportado", "incipiente": "emergente"}
MAP_VERIF = {"humano_clinico": "verificado"}
MAP_G2 = {"eligible_source": "eligible"}   # 'nao_aplicavel' fica como extensão declarada (D7)

# ── D5: forca_causal estendido → (tier oficial, desenho_evidencia) ──────────
MAP_FORCA = {
 "tier_2_intervencao_humana":  ("tier_2_necessidade_ou_suficiencia", "intervencao_humana"),
 "tier_2_meta_analise":        ("tier_2_necessidade_ou_suficiencia", "meta_analise"),
 "tier_2_revisao_sistematica": ("tier_2_necessidade_ou_suficiencia", "revisao_sistematica"),
 "tier_3_mecanistico_animal":  ("tier_3_correlacional_mecanistico",  "mecanistico_animal"),
 "tier_3_mecanistico_invitro": ("tier_3_correlacional_mecanistico",  "mecanistico_invitro"),
 "tier_4_observacional_transversal": ("tier_4_descritivo_estrutural","observacional_transversal"),
}

# ── D3: natureza por conteúdo — tabela id-a-id (revisada um a um; trilha explica) ──
NAT_B01 = {**{f"VINC_B1V2_{n}": "contributiva" for n in
              ["0179","0180","0181","0182","0183","0184","0185","0186","0187","0188","0189",
               "0190","0191","0192","0193","0194","0206"]},
           "VINC_B1V2_0197": "nao_estabelecida", "VINC_B1V2_0198": "nao_estabelecida",
           "VINC_B1V2_0202": "nao_estabelecida", "VINC_B1V2_0201": "marcador",
           **{f"VINC_B1V2_{n}": "associativa" for n in ["0195","0196","0199","0200","0203","0204"]}}
NAT_B07 = {"VINC_B7_016": "associativa", "VINC_B7_022": "nao_estabelecida",
           "VINC_B7_023": "nao_estabelecida", "VINC_B7_025": "marcador",
           "VINC_B7_032": "contributiva", "VINC_B7_033": "contributiva",
           "VINC_B7_034": "contributiva",
           "VINC_B7_018": "nao_estabelecida", "VINC_B7_019": "nao_estabelecida",
           "VINC_B7_028": "nao_estabelecida", "VINC_B7_038": "nao_estabelecida"}
NAT_B08 = {**{f"VINC_B8_{n}": "contributiva" for n in ["013","021","022","031","033"]},
           "VINC_B8_028": "associativa", "VINC_B8_030": "associativa",
           **{f"VINC_B8_{n}": "nao_estabelecida" for n in
              ["003","004","005","008","015","025","029","045","080"]}}
REVISAVEL_NATUREZA = {"VINC_B7_034", "VINC_B8_033"}
REVISAVEL_CAMPOS = {("meta_analise","evid_role"), ("incipiente","grau_maturidade"),
                    ("PARCIAL","status_referencia"), ("refutadora","natureza_relacao")}

def nota(r, campo, old, new, regra, rev=False):
    tag = f"{DATA} HARMONIZA {regra}: {campo} {old!r}→{new!r}" + (" [REVISAVEL]" if rev else "")
    r["nota_reparo"] = (r["nota_reparo"] + " || " if (r.get("nota_reparo") or "").strip() else "") + tag
    return tag

def harmoniza(vinc, bib):
    log = []
    for r in vinc:
        rid = str(r.get("id_vinculo", "?"))
        # D3 natureza por tabela (B01/B07/B08)
        nat = r.get("natureza_relacao")
        mapa = {"B01": NAT_B01, "B07": NAT_B07, "B08": NAT_B08}.get(bib, {})
        if nat in ("descritiva", "refutadora") or (isinstance(nat, str) and nat.startswith("tier_")):
            if rid in mapa and r.get("natureza_relacao") != mapa[rid]:
                old = nat
                r["natureza_relacao"] = mapa[rid]
                tag = nota(r, "natureza_relacao", old, mapa[rid], "D3",
                           rev=(rid in REVISAVEL_NATUREZA) or ((old, "natureza_relacao") in REVISAVEL_CAMPOS))
                log.append((rid, "natureza_relacao", old, mapa[rid], "D3"))
        # D1 status_referencia
        v = r.get("status_referencia")
        if v in MAP_STATUS_REF:
            new = MAP_STATUS_REF[v]; r["status_referencia"] = new
            nota(r, "status_referencia", v, new, "D1", rev=(v, "status_referencia") in REVISAVEL_CAMPOS)
            log.append((rid, "status_referencia", v, new, "D1"))
        # D2 evid_role
        v = r.get("evid_role")
        if v in MAP_EVID_ROLE:
            new = MAP_EVID_ROLE[v]; r["evid_role"] = new
            nota(r, "evid_role", v, new, "D2", rev=(v, "evid_role") in REVISAVEL_CAMPOS)
            log.append((rid, "evid_role", v, new, "D2"))
        # D4 grau
        v = r.get("grau_maturidade")
        if v in MAP_GRAU:
            new = MAP_GRAU[v]; r["grau_maturidade"] = new
            nota(r, "grau_maturidade", v, new, "D4", rev=(v, "grau_maturidade") in REVISAVEL_CAMPOS)
            log.append((rid, "grau_maturidade", v, new, "D4"))
        # D5 forca estendido → tier + desenho
        v = r.get("forca_causal")
        if v in MAP_FORCA:
            tier, des = MAP_FORCA[v]
            r["forca_causal"] = tier
            if not (r.get("desenho_evidencia") or "").strip():
                r["desenho_evidencia"] = des
            nota(r, "forca_causal", v, f"{tier} + desenho_evidencia={des}", "D5-AT12")
            log.append((rid, "forca_causal", v, tier, "D5-AT12"))
        # D6 verification_status campo trocado
        v = r.get("verification_status")
        if v in MAP_VERIF:
            new = MAP_VERIF[v]; r["verification_status"] = new
            nota(r, "verification_status", v, new, "D6")
            log.append((rid, "verification_status", v, new, "D6"))
        # D7 g2
        v = r.get("g2_elegibilidade")
        if v in MAP_G2:
            new = MAP_G2[v]; r["g2_elegibilidade"] = new
            nota(r, "g2_elegibilidade", v, new, "D7")
            log.append((rid, "g2_elegibilidade", v, new, "D7"))
        # D8 assinatura G3 mista (B07/B08/B09/B10)
        q = (r.get("g3_verificado_por") or "")
        if "eutils" in q.lower():
            import re as _re
            m = _re.match(r"\s*(IA G3 \(Rodada \[AT\] GPM B\d+ 2026-09-09\))", q)
            if m:
                r["g3_verificado_por"] = m.group(1)
                nota(r, "g3_verificado_por", q[:90] + "…", m.group(1) + " (método eutils preservado em nota/trilha)", "D8")
                log.append((rid, "g3_verificado_por", "mista→assinatura", "", "D8"))
    return log

def main():
    apply_mode = len(sys.argv) > 2 and sys.argv[1] == "--apply"
    alvo = sys.argv[-1].upper() if len(sys.argv) > 1 else None
    resumo = {}
    for at in sorted(glob.glob("/home/user/BIBLIOTECAS/B*/atuais")):
        bib = at.split("/")[-2].split("_")[0]
        if alvo and bib != alvo: continue
        vp = glob.glob(at + "/Evidencias/Vinculos/*.json")[0]
        mds = sorted(glob.glob(at + "/*.md"))
        corpo = open(mds[0], encoding="utf-8").read()
        vinc = json.load(open(vp, encoding="utf-8"))
        vinc = vinc if isinstance(vinc, list) else vinc.get("vinculos")
        pre = sum(1 for p in Contrato("vinculo", corpo_canonico=corpo).validar(vinc) if p.nivel == "BLOQUEANTE")
        log = harmoniza(vinc, bib)
        pos = sum(1 for p in Contrato("vinculo", corpo_canonico=corpo).validar(vinc) if p.nivel == "BLOQUEANTE")
        por = collections.Counter(x[1] for x in log)
        resumo[bib] = (pre, pos, dict(por), len(vinc))
        print(f"{bib}: vínculos={len(vinc)} BLOQ {pre}→{pos} | alterações={len(log)} {dict(por)}")
        if apply_mode and log:
            c = Contrato("vinculo", corpo_canonico=corpo)
            rest = [p for p in c.validar(vinc) if p.nivel == "BLOQUEANTE"]
            # grava mesmo com bloqueantes residuais SÓ se forem as classes já decididas como
            # "decisão de schema" (id 3 dígitos / g2 nao_aplicavel / AT-05-B2 âncoras pendentes)
            aceit = {"id_vinculo", "g2_elegibilidade", "trecho_ancora"}
            duros = [p for p in rest if p.campo not in aceit]
            if duros:
                print(f"  !! ABORT: {len(duros)} bloqueantes fora das classes decididas, ex.: {duros[0]}")
                sys.exit(2)
            res = c.gravar(vp, vinc)
            trilha = {"data": DATA, "bib": bib, "arquivo": vp, "backup": res["backup"],
                      "bloq_pre": pre, "bloq_pos": pos, "residual_schema": len(rest),
                      "decisoes": "DECISOES_HARMONIZACAO_SCHEMA_2026-09-11.md",
                      "alteracoes": [{"id_vinculo": a, "campo": b, "de": str(c)[:120], "para": d, "regra": e}
                                     for a, b, c, d, e in log]}
            tp = at + f"/producao/06_harmoniza_{bib}_2026-09-11.json"
            json.dump(trilha, open(tp, "w"), ensure_ascii=False, indent=1)
            print(f"  gravado (backup {res['backup'].split('/')[-1]}); trilha {tp.split('/')[-1]}; residual-schema={len(rest)}")
    json.dump(resumo, open("/tmp/resumo_harmoniza.json", "w"))

if __name__ == "__main__":
    main()
