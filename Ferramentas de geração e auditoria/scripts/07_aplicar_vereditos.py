#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica os vereditos G2/G3 (lidos por IA-revisora) ao Modulo 9 consolidado.
Atualiza vinculos (g2, status_auditoria, forca_causal, verification_status,
g3_verificado_por, data, notas) e o status das referencias."""
import json, glob
from datetime import date
from pathlib import Path
BASE=Path(__file__).resolve().parent
pac=BASE/"ato2_pacote"
ev=pac/"Evidencias"
AUDITOR="IA_revisora_G3 (rodada de auditoria 2026-09-03; aguarda revisao de pares humana)"
DATA="2026-09-03"

# carrega todos os vereditos
ver={}
for f in glob.glob(str(BASE/"auditoria_G2G3/vereditos/vereditos_*.json")):
    ver.update(json.load(open(f,encoding="utf-8")))
print("vereditos carregados:", len(ver))

vinc=json.load(open(ev/"Vinculos/vinculos_referencia_afirmacao.json",encoding="utf-8"))
refs=json.load(open(ev/"Bibliografia/01_pmids.json",encoding="utf-8"))
meta=json.load(open(ev/"Bibliografia/02_meta_analises.json",encoding="utf-8"))

aplicados=0; faltando=[]
contagem={"CONFIRMADO":0,"PARCIALMENTE_CONFIRMADO":0,"NAO_LOCALIZADO":0,"NAO_SUSTENTA_CLAIM":0,"CITACAO_INCORRETA":0}
for v in vinc:
    vid=v["id_vinculo"]
    if vid not in ver:
        faltando.append(vid); continue
    d=ver[vid]
    v["g2_elegibilidade"]=d["g2"]
    v["g2_motivo"]=d["g2_motivo"]
    v["status_auditoria"]=d["status"]
    v["forca_causal"]=d.get("forca","") or v.get("forca_causal","")
    # verification_status
    vs=d.get("vs","pendente")
    v["verification_status"]=vs
    v["g3_verificado_por"]=AUDITOR if d["status"]!="NAO_LOCALIZADO" else ""
    v["data_verificacao"]=DATA if d["status"]!="NAO_LOCALIZADO" else ""
    v["g3_notas"]=d.get("nota","")
    # status_referencia sobe para VALIDADO se ha vinculo confirmado
    if d["status"] in ("CONFIRMADO","PARCIALMENTE_CONFIRMADO") and d["g2"]=="eligible":
        v["status_referencia"]="VALIDADO_G3_IA"
    contagem[d["status"]]=contagem.get(d["status"],0)+1
    aplicados+=1

# atualiza status das referencias N1/meta com base nos vinculos
id2status={}
for v in vinc:
    rid=v["id_referencia_interna"]
    st=v.get("status_referencia","CANDIDATO")
    if st=="VALIDADO_G3_IA": id2status[rid]="VALIDADO_G3_IA"
for coll in (refs,meta):
    for r in coll:
        ids=r.get("ids_referencia_interna",[r.get("id_referencia_interna")])
        if any(i in id2status for i in ids):
            r["status_auditoria"]="VALIDADO_G3_IA (revisao de pares pendente)"
            r["g3_verificado_por"]=AUDITOR
            r["data_verificacao"]=DATA

json.dump(vinc, open(ev/"Vinculos/vinculos_referencia_afirmacao.json","w"), ensure_ascii=False, indent=1)
json.dump(refs, open(ev/"Bibliografia/01_pmids.json","w"), ensure_ascii=False, indent=1)
json.dump(meta, open(ev/"Bibliografia/02_meta_analises.json","w"), ensure_ascii=False, indent=1)

print("vinculos aplicados:", aplicados, "/", len(vinc))
print("faltando veredito:", faltando or "nenhum")
print("distribuicao G3:", contagem)
# g2
import collections
print("distribuicao G2:", dict(collections.Counter(v["g2_elegibilidade"] for v in vinc)))
print("verification_status:", dict(collections.Counter(v["verification_status"] for v in vinc)))
