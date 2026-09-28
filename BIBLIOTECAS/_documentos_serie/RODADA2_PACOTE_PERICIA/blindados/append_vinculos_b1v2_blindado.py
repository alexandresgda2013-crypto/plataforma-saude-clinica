#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# append_vinculos_b1v2_blindado.py — 2026-09-11 (agente, pacote Rodada 2 da perícia)
# Versão BLINDADA de append_vinculos_b1v2.py. O que muda (cada ponto = defeito observado):
#   D1  V() não alimenta dois campos com um parâmetro: natureza_relacao e forca_causal
#       são parâmetros EXPLÍCITOS (linha a linha), coerência conferida pelo contrato.
#   ti  "tier_2_intervencao" (fora do enum — origem do AT-11) não existe mais: só
#       valores do enum oficial de 4 tiers passam na validação pré-gravação.
#   status_auditoria "G1_G2_G3_B1v2" (fora do enum) → enum oficial de vínculo.
#   id  não é mais len(d)+1 (colide): próximo \d{4} livre por varredura do máximo.
#   D4  nada de json.dump direto: validar → abortar_se → gravar (backup + atômico).
#   D2  âncoras verificadas contra a Canônica ANTES de gravar (AUSENTE/VAZIO aborta).
# Uso:  python3 append_vinculos_b1v2_blindado.py <dir_atuais> [--aplicar]
#       sem --aplicar = dry-run (só valida e imprime o que faria)
import json, os, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))          # contrato.py do pacote
from contrato import Contrato, abortar_se, ENUM_VINCULO                    # noqa: E402

LINHAS = Path(os.environ.get("B1V2_LINHAS", Path(__file__).parent / "b1v2_linhas.json"))

TETO_POR_TIER = {    # mesma regra D3 da rodada de harmonização (teto de natureza pela força)
    "tier_1_necessidade_e_suficiencia": {"causal", "contributiva", "associativa", "compensatoria", "marcador", "nao_estabelecida"},
    "tier_2_necessidade_ou_suficiencia": {"causal", "contributiva", "associativa", "compensatoria", "marcador", "nao_estabelecida"},
    "tier_3_correlacional_mecanistico": {"contributiva", "associativa", "compensatoria", "marcador", "nao_estabelecida"},
    "tier_4_descritivo_estrutural": {"associativa", "marcador", "nao_estabelecida"},
}

def proximo_id(vinc, prefixo="VINC_B1V2_"):
    mx = 0
    for v in vinc:
        m = re.match(re.escape(prefixo) + r"(\d{4})$", str(v.get("id_vinculo", "")))
        if m: mx = max(mx, int(m.group(1)))
    return lambda i=iter(range(mx + 1, 9999)): f"{prefixo}{next(i):04d}"

def main():
    at = Path(sys.argv[1]); aplicar = "--aplicar" in sys.argv
    vp = at / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
    bib = at / "Evidencias/Bibliografia/01_pmids.json"
    md = sorted(at.glob("*.md"))
    if not (vp.exists() and bib.exists() and md):
        print("layout inválido:", at); sys.exit(2)
    corpo = md[0].read_text(encoding="utf-8")
    vinc = json.loads(vp.read_text(encoding="utf-8"))
    refs = json.loads(bib.read_text(encoding="utf-8"))
    rot2pmid = {}
    for it in refs if isinstance(refs, list) else refs.get("referencias", []):
        for full in it.get("ids_referencia_interna", [it.get("id_referencia_interna", "")]):
            rot2pmid[full.replace("REF_", "")] = it.get("pmid_oficial")
    linhas = json.loads(LINHAS.read_text(encoding="utf-8"))["linhas"]
    existe = {v.get("id_referencia_interna") for v in vinc}
    nid = proximo_id(vinc)
    novos = 0
    for L in linhas:
        iid = "REF_" + L["rotulo"]
        if iid in existe:
            continue
        forca, nat = L["forca"], L["natureza"]
        assert forca in ENUM_VINCULO["forca_causal"], f"forca fora do enum: {forca}"
        assert nat in ENUM_VINCULO["natureza_relacao"], f"natureza fora do enum: {nat}"
        assert nat in TETO_POR_TIER[forca], f"teto violado: natureza {nat} > tier {forca}"
        vinc.append({
            "id_vinculo": nid(), "id_referencia_interna": iid, "claim_id": "",
            "mecanismo_origem": "mecanismo_B1_neuroinflamacao",
            "secao_origem": "mecanismo_B1_neuroinflamacao/" + L["secao"],
            "trecho_ancora": L["ancora"], "achado_central_molecular": "",
            "natureza_relacao": nat, "grau_maturidade": L["grau"], "forca_causal": forca,
            "extrapolacao_por_analogia": "sim (animal/celula -> humano)" if L["verif"] in ("preclinico", "extrapolado") else "baixa (humano)",
            "evid_role": L["role"], "uso": "B1_v2",
            "status_referencia": "VALIDADO",  # D1-harmonização: oficial (era VALIDADO_G3_IA legado)
            "status_auditoria": "CONFIRMADO" if L["verif"] == "verificado" else "PARCIALMENTE_CONFIRMADO",
            "verification_status": L["verif"], "data_verificacao": "2026-09-04",
            "g2_elegibilidade": "eligible", "g2_motivo": "", "g1_metodo": "eutils_automatico",
            "g3_verificado_por": "IA G3 (B1 v2, 2026-09-04)",
            "pmid_oficial": rot2pmid.get(L["rotulo"], ""), "g3_notas": "",
            **({"desenho_evidencia": L["desenho"]} if L.get("desenho") else {})})
        novos += 1
    c = Contrato("vinculo", corpo_canonico=corpo)
    abortar_se(c.validar(vinc), "append_vinculos_b1v2_blindado")      # portão: exit 1 se bloqueante
    print(f"novos vínculos: {novos} | total: {len(vinc)} | examinados: {c.examinados}")
    if aplicar and novos:
        res = c.gravar(vp, vinc)                                       # backup + atômico
        print("gravado:", vp, "| backup:", res["backup"])
    else:
        print("dry-run: nada gravado (use --aplicar para gravar)")

if __name__ == "__main__":
    main()
