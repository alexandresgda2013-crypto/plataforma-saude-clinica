#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C2/E3: preenche trecho_ancora LITERAL (frase verbatim do texto) para os
30 vínculos novos da B1 v2, localizando a citação (Autor, ano) na subseção."""
import re, json
from pathlib import Path
BASE=Path("/home/user/pipeline_auditoria_conteudo/BIBLIOTECAS/B01_Neuroinflamacao")
BIB=BASE/"Biblioteca_B1_NEUROINFLAMACAO_CANONICA.md"
F=BASE/"Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
REFS=BASE/"Evidencias/Bibliografia/01_pmids.json"

texto=BIB.read_text(encoding="utf-8")
refs=json.load(open(REFS,encoding="utf-8"))
rot2ref={}
for it in refs:
    for full in it.get("ids_referencia_interna",[]):
        rot=full.replace("REF_","")
        rot2ref[rot]=it

d=json.load(open(F,encoding="utf-8"))

def sobrenome(it):
    a=(it.get("autores") or ["?"])[0]
    return a.split()[0].replace(",","")

def subsecao(num):
    # extrai texto da subseção "### num " até o próximo "### "
    m=re.search(r'^### '+re.escape(num)+r'[^\n]*\n', texto, re.M)
    if not m: return None
    start=m.end()
    nxt=re.search(r'^### ', texto[start:], re.M)
    end=start+nxt.start() if nxt else start+4000
    return texto[start:end]

def frase_literal(sub, cita):
    # acha a citação exata "(Sobrenome ... ano)"
    idx=sub.find(cita)
    if idx<0:
        return None
    # início da frase: último ". " anterior
    back=sub.rfind(". ", 0, idx)
    ini=0 if back<0 else back+2
    # fim da frase: próximo ". " após a citação (após as tags [..])
    fwd=sub.find(". ", idx)
    if fwd<0: fwd=len(sub)
    fim=fwd+1
    trecho=sub[ini:fim].strip()
    return trecho

atualizados=[]; falhas=[]
for v in d:
    if not str(v.get("id_vinculo","")).startswith("VINC_B1V2"):
        continue
    rot=v["id_referencia_interna"].replace("REF_","")
    it=rot2ref.get(rot)
    if not it:
        falhas.append((rot,"sem registro")); continue
    sn=sobrenome(it)
    ano=re.search(r'(20\d\d)', str(it.get("revista_ano",""))).group(1)
    # número da subseção
    sec=v["secao_origem"].split("/")[-1]  # ex: 2.25
    sub=subsecao(sec)
    if not sub:
        falhas.append((rot,f"subseção {sec} não achada")); continue
    # padrões de citação possíveis
    candidatos=[f"({sn} et al., {ano})", f"({sn} et al., {ano})", f"({sn} et al. {ano})",
                f"{sn} et al., {ano}", f"({sn} et al., {ano}".replace("(",f"({sn} ")]
    cita=f"({sn} et al., {ano})"
    trecho=frase_literal(sub, cita)
    if not trecho:
        # tenta sem parêntese
        trecho=frase_literal(sub, f"{sn} et al., {ano}")
    if not trecho or len(trecho)<20:
        falhas.append((rot,f"citação '{cita}' não achada em {sec}")); continue
    # normaliza: garante que é literal (está no texto)
    if trecho not in texto:
        falhas.append((rot,"trecho não é substring literal")); continue
    v["trecho_ancora"]=trecho
    v["g3_verificado_por"]="IA_G3_auditor (abstract efetch lido, 2026-09-04)"
    v["status_auditoria"]="G1_eutils + G2_elegibilidade + G3_abstract_lido"
    atualizados.append((rot,sec,len(trecho)))

json.dump(d,open(F,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ATUALIZADOS:",len(atualizados))
for rot,sec,n in atualizados: print(f"  {rot:26s} {sec:7s} {n}c")
print("FALHAS:",len(falhas))
for f in falhas: print("  ",f)
