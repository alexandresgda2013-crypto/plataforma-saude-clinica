#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# contrato_censo_16.py — 2026-09-11 (5ª rodada): executa o contrato.py do perito sobre
# vínculos E ledgers das 16 bibliotecas. Vocabulário estendido de B7/B8 registrado em
# LEGADO_CONHECIDO como AVISO NOMEADO (pedido #1 da rodada; manifestos B07/B08 já o
# declaram desde 2026-09-10). NADA grava — instrumento de medição.
# rev.2 (2026-09-11, pós-Rodada de Harmonização): decisões nomeadas D7/D9/F1 do doc
# DECISOES_HARMONIZACAO_SCHEMA_2026-09-11.md passam a aparecer como AVISO NOMEADO
# (nunca silenciadas, nunca contadas como defeito novo):
#   D9 — id de vínculo legado com 3 dígitos (1541 registros, série histórica; novos
#        registros seguem \d{4}); ratificação vai ao SCHEMA v2/perícia (pacote Rodada 2).
#   D7 — g2_elegibilidade='nao_aplicavel' (B13, 49) é extensão declarada no manifesto
#        B13: sem equivalente fiel no enum oficial; proposta de estender o enum.
#   F1 — B14-B16 (geração nova) sem verification_status/g3/status_referencia/g2:
#        lacuna de arquitetura documentada; contrato conta como BLOQUEANTE de schema,
#        aqui separado em balde próprio "F1_schema" para não mascarar defeito de dado.
import json, glob, sys, collections, re
sys.path.insert(0, "/home/user/BIBLIOTECAS/_documentos_serie/bancada_at02/scripts")
import contrato
from contrato import Contrato

# AT-12 implementado em 2026-09-11 (D5): o vocabulário estendido B7/B8 foi decomposto
# em tier oficial + desenho_evidencia. Mantido vazio de propósito: se um valor estendido
# reaparecer, deve voltar a contar como BLOQUEANTE (regressão), não aviso.
EXT = {}
contrato.LEGADO_CONHECIDO["vinculo"]["forca_causal"] = {k: "enum oficial de 4 tiers + " + v for k, v in EXT.items()}
# D7: extensão declarada B13 (aviso nomeado)
contrato.LEGADO_CONHECIDO["vinculo"]["g2_elegibilidade"] = {
    "nao_aplicavel": "extensão declarada (D7, manifesto B13; enum oficial a estender no SCHEMA v2)",
}

ID_LEGADO = re.compile(r"^VINC_B\d{1,2}(V\d)?_\d{3}$")
GERACAO_NOVA = {"B14", "B15", "B16"}

def load_json(p):
    d = json.load(open(p, encoding="utf-8"))
    return d if isinstance(d, list) else d.get("vinculos", d.get("registros", d.get("entradas", [])))

linhas = []
for at in sorted(glob.glob("/home/user/BIBLIOTECAS/B*/atuais")):
    b = at.split("/")[-2]
    mds = sorted(glob.glob(at + "/*.md"))
    corpo = open(mds[0], encoding="utf-8").read() if mds else ""
    out = {"bib": b.split("_")[0]}

    vp = glob.glob(at + "/Evidencias/Vinculos/*.json")
    if vp:
        vinc = load_json(vp[0])
        c = Contrato("vinculo", corpo_canonico=corpo)
        probs = c.validar(vinc)
        bnum = b.split("_")[0]
        bloq = collections.Counter()
        for p in probs:
            if p.nivel != "BLOQUEANTE":
                continue
            # D9: id legado 3 dígitos → aviso nomeado, não bloqueante
            if p.campo == "id_vinculo" and ID_LEGADO.match(p.item):
                continue
            # F1: geração nova — lacuna de arquitetura, balde próprio
            if bnum in GERACAO_NOVA and p.campo in ("verification_status", "g3_verificado_por"):
                continue
            bloq[p.campo] += 1
        avisos = collections.Counter(
            "legado" if "LEGADO" in p.msg else ("literalidade" if p.campo == "trecho_ancora" else p.campo)
            for p in probs if p.nivel != "BLOQUEANTE")
        # contagem nomeada das decisões (visível, nunca silenciada)
        avisos["D9_id_legado3dig"] = sum(1 for p in probs if p.nivel == "BLOQUEANTE"
                                         and p.campo == "id_vinculo" and ID_LEGADO.match(p.item))
        if bnum in GERACAO_NOVA:
            avisos["F1_schema_geracao_nova"] = sum(1 for p in probs if p.nivel == "BLOQUEANTE"
                                                   and p.campo in ("verification_status", "g3_verificado_por"))
        out["vinculos"] = (len(vinc), dict(bloq), dict(avisos))
    lp = glob.glob(at + "/Auditoria_*/ledger_*.json")
    if lp:
        led = load_json(lp[0])
        c2 = Contrato("ledger", corpo_canonico=corpo)
        p2 = c2.validar(led)
        bloq2 = collections.Counter(p.campo for p in p2 if p.nivel == "BLOQUEANTE")
        av2 = collections.Counter(p.campo for p in p2 if p.nivel != "BLOQUEANTE")
        out["ledger"] = (len(led), dict(bloq2), dict(av2))
    linhas.append(out)

for o in linhas:
    print(f"### {o['bib']}")
    if "vinculos" in o:
        n, b, a = o["vinculos"]
        print(f"  vínculos: {n:4d} | BLOQ {sum(b.values()):3d} {b if b else ''}")
        print(f"             avisos {sum(a.values()):4d} {dict(sorted(a.items()))}")
    if "ledger" in o:
        n, b, a = o["ledger"]
        print(f"  ledger  : {n:4d} | BLOQ {sum(b.values()):3d} {b if b else ''}")
        print(f"             avisos {sum(a.values()):4d} {dict(sorted(a.items()))}")
