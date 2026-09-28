#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# aplicar_vereditos_blindado.py — 2026-09-11 (agente, pacote Rodada 2 da perícia)
# Versão BLINDADA de 07_aplicar_vereditos.py. Defeitos fechados:
#   D3/lei P-5: o original imprimia a validação e gravava mesmo assim. Aqui a
#   validação É o portão (abortar_se, exit 1) — nenhum veredito com valor fora do
#   enum, de artefato errado (F2) ou âncora AUSENTE passa.
#   D4: gravação só via contrato.gravar (backup datado + escrita atômica).
#   D1-legado: status_referencia sobe para o oficial "VALIDADO" (a tabela LEGADO
#   VALIDADO_G3_IA→VALIDADO da perícia foi aplicada ao vivo em 2026-09-11; gerar o
#   valor legado de novo reintroduziria a dívida).
# Uso:  python3 aplicar_vereditos_blindado.py <dir_atuais> <dir_vereditos> [--aplicar]
import json, glob, sys, collections
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from contrato import Contrato, abortar_se                                   # noqa: E402

AUDITOR = "IA G3 (rodada de auditoria; aguarda revisão de pares humana)"

def main():
    at = Path(sys.argv[1]); dver = Path(sys.argv[2]); aplicar = "--aplicar" in sys.argv
    ev = at / "Evidencias"
    vp = ev / "Vinculos/vinculos_referencia_afirmacao.json"
    md = sorted(at.glob("*.md"))
    corpo = md[0].read_text(encoding="utf-8")
    vinc = json.loads(vp.read_text(encoding="utf-8"))
    ver = {}
    for f in glob.glob(str(dver / "vereditos_*.json")):
        ver.update(json.load(open(f, encoding="utf-8")))
    print("vereditos carregados:", len(ver))
    if not ver:
        print("nenhum veredito — nada a fazer"); sys.exit(0)
    aplicados, faltando = 0, []
    for v in vinc:
        vid = v["id_vinculo"]
        if vid not in ver:
            faltando.append(vid); continue
        d = ver[vid]
        v["g2_elegibilidade"] = d["g2"]; v["g2_motivo"] = d["g2_motivo"]
        v["status_auditoria"] = d["status"]
        v["forca_causal"] = d.get("forca") or v.get("forca_causal", "")
        if d.get("natureza"):
            v["natureza_relacao"] = d["natureza"]
        v["verification_status"] = d.get("vs", "pendente")
        v["g3_verificado_por"] = AUDITOR if d["status"] != "NAO_LOCALIZADO" else ""
        v["data_verificacao"] = d.get("data", "") if d["status"] != "NAO_LOCALIZADO" else ""
        v["g3_notas"] = d.get("nota", "")
        if d["status"] in ("CONFIRMADO", "PARCIALMENTE_CONFIRMADO") and d["g2"] == "eligible":
            v["status_referencia"] = "VALIDADO"
        aplicados += 1
    c = Contrato("vinculo", corpo_canonico=corpo)
    abortar_se(c.validar(vinc), "aplicar_vereditos_blindado", examinados=c.examinados)
    print(f"vínculos aplicados: {aplicados}/{len(vinc)} | sem veredito: {len(faltando)}")
    print("distribuição G3:", dict(collections.Counter(v['status_auditoria'] for v in vinc)))
    if aplicar and aplicados:
        res = c.gravar(vp, vinc)
        print("gravado com backup:", res["backup"])
    else:
        print("dry-run: nada gravado (use --aplicar)")

if __name__ == "__main__":
    main()
