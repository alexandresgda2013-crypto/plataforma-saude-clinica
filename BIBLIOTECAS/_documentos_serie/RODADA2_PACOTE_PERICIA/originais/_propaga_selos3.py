#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Propaga selos de verification na prosa (texto original, sem destruir formatacao).

Para cada vinculo, pega a ultima citacao (Autor, ano)[tags...] do trecho ancora
e, no texto ORIGINAL, localiza essa mesma citacao e insere o selo de Rodada 3
logo apos o ] de fechamento da tag (antes do ponto final).

Selo = status G3 do vinculo (nao maquia):
  verificado  -> [VERIFICADO]
  preclinico  -> [PRÉ-CLÍNICO]
  extrapolado -> [EXTRAPOLADO: animal/célula→humano]
  pendente    -> [EMERGENTE]
"""
import json, re, sys
from pathlib import Path

doc = Path(sys.argv[1])
vinc = json.load(open(sys.argv[2], encoding="utf-8"))
t = doc.read_text(encoding="utf-8")

SELO_RE = re.compile(r"\[(VERIFICADO|PR[ÉE]-CL[ÍI]NICO|EXTRAPOLADO:|EMERGENTE)")

def selo(v):
    st = v.get("verification_status")
    if st == "pendente":
        return "[EMERGENTE]"
    if st == "preclinico":
        return "[PRÉ-CLÍNICO]"
    if st == "extrapolado":
        return "[EXTRAPOLADO: animal/célula→humano]"
    if st == "verificado":
        return "[VERIFICADO]"
    return None

def ultima_cit(texto):
    # acha a ultima ocorrencia de ( ...ano... )[ ... ] no trecho
    ms = list(re.finditer(r"\([^()]*?\d{4}[^()]*?\)\s*\[[^\]]*\]", texto))
    return ms[-1] if ms else None

# Aplica de tras pra frente no texto por posicao real do texto original.
ins = []
for v in vinc:
    if v.get("status_auditoria") == "NAO_LOCALIZADO":
        continue
    s = selo(v)
    if not s:
        continue
    m = ultima_cit(v["trecho_ancora"])
    if not m:
        continue
    cit = m.group(0)
    # localiza no texto original (pode diferir por **; tenta exata, depois flex)
    pos = t.find(cit)
    if pos == -1:
        # tenta removendo marcadores ** do proprio cit
        cit_flex = cit.replace("**", "")
        pos = t.find(cit_flex)
        if pos != -1:
            cit = cit_flex
    if pos == -1:
        continue
    end = pos + len(cit)
    if SELO_RE.match(t[end:end+30]):
        continue
    ins.append((end, s))

ins.sort(reverse=True)
for end, s in ins:
    t = t[:end] + " " + s + t[end:]

doc.write_text(t, encoding="utf-8")

# contagem
from collections import Counter
c = Counter(re.findall(r"\[(VERIFICADO|PRÉ-CLÍNICO|EXTRAPOLADO: animal/célula→humano|EMERGENTE)\]", t))
print("Selos na prosa:")
for k, n in c.items():
    print(f"  {k}: {n}")
print("total:", sum(c.values()), "| insercoes:", len(ins))
