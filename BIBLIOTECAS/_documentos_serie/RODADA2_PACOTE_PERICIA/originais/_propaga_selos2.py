#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Propaga selos de verification na prosa: para cada vinculo, localiza a
citacao-final do trecho ancora (padrao (Autor, ano)[..]) e insere o selo de
Rodada 3 logo DEPOIS da tag de geracao, antes do ponto final.

Regra (nao maquia): selo = status G3 do proprio vinculo.
[VERIFICADO]/[PRÉ-CLÍNICO]/[EXTRAPOLADO: ...]/[EMERGENTE]
"""
import json, re, sys
from pathlib import Path

doc = Path(sys.argv[1])
vinc = json.load(open(sys.argv[2], encoding="utf-8"))
t = doc.read_text(encoding="utf-8")

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

SELO_EXIST = ("[VERIFICADO]", "[PRÉ-CLÍNICO]", "[EXTRAPOLADO:", "[EMERGENTE]")

# extrai a ultima citacao do trecho (Autor, ano)[tags] -> usamos como ancora
def ultima_cit(trecho):
    # acha todos (.....)[....] no final do trecho
    ms = list(re.finditer(r"\(([^()]*?\d{4}[^()]*?)\)\s*\[[^\]]*\]", trecho))
    if ms:
        m = ms[-1]
        return m.group(0)  # o texto (Autor, ano)[OB; ...]
    return None

# normaliza igualar (tira ** e espacos)
def norm(s):
    return re.sub(r"\s+", " ", s.replace("**", "")).strip()

t_norm = norm(t)
aplicados = {}
falhas = []

for v in vinc:
    if v.get("status_auditoria") == "NAO_LOCALIZADO":
        continue
    s = selo(v)
    if not s:
        continue
    cit = ultima_cit(norm(v["trecho_ancora"]))
    if not cit:
        falhas.append((v["id_vinculo"], "sem citacao final"))
        continue
    if any(e.replace("[","").rstrip(":") in cit for e in SELO_EXIST):
        continue
    # localiza a citacao no texto normalizado
    pos = t_norm.find(cit)
    if pos == -1:
        falhas.append((v["id_vinculo"], "citacao nao achada: " + cit[:40]))
        continue
    # nao reinsere se ja existe selo logo depois
    fim = pos + len(cit)
    if any(t_norm[fim:fim+22].startswith(e) for e in SELO_EXIST):
        continue
    aplicados[s] = aplicados.get(s, 0) + 1
    # registra insercao a fazer no texto ORIGINAL: marca a posicao (em texto norm)
    # vamos fazer as insercoes depois, de tras pra frente.
    v["_ins"] = (pos, fim, s)

# aplica insercoes no texto NORMALIZADO de tras pra frente
ins = sorted([(v["_ins"][1], v["_ins"][2]) for v in vinc if "_ins" in v], reverse=True)
# reconstruir: como norm() remove **, trabalhamos sobre copia normalizada e
# salvamos como novo texto (os ** ja sao quase todos em negrito de rotulos;
# a prosa cientifica permanece integra). Para nao perder formatacao, em vez
# disso inserimos no ORIGINAL casando a string exata da citacao.
t2 = t
for v in sorted(vinc, key=lambda x: -len(x["trecho_ancora"])):
    if "_ins" not in v:
        continue
    cit = ultima_cit(norm(v["trecho_ancora"]))
    s = v["_ins"][2]
    # a citacao no original pode ter ** ; procura variante simples:
    # insere o selo apos o ']' final da ocorrencia exata
    idx = t2.find(cit)
    if idx == -1:
        continue
    end = idx + len(cit)
    if s in t2[end:end+30]:
        continue
    # se ja tem selo logo apos, pula
    if any(t2[end:end+24].startswith(e) for e in SELO_EXIST):
        continue
    t2 = t2[:end] + " " + s + t2[end:]

doc.write_text(t2, encoding="utf-8")
print("selos aplicados por tipo:", aplicados)
print("total inserido:", sum(aplicados.values()))
print("falhas:", len(falhas))
for f in falhas[:15]:
    print("  ", f)
