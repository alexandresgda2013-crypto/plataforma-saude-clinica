#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rodada 3 — propaga os selos de verification_status do JSON de vinculos
para a prosa da Biblioteca (GATE-script / Checklist Fidelidade esperam os selos
[VERIFICADO]/[PRÉ-CLÍNICO]/[EXTRAPOLADO]/[EMERGENTE] frase a frase).

Nao maquia nada: o selo reflete EXATAMENTE o status do vinculo (G3).
- verificado (humano/post_mortem/human_experimental)  -> [VERIFICADO]
- preclinico (so animal/celula)                       -> [PRÉ-CLÍNICO]
- extrapolado (animal/celula->humano, EXT)            -> [EXTRAPOLADO: ...]
- emergente / pendente                                -> [EMERGENTE]
"""
import json, re, sys
from pathlib import Path

doc = Path(sys.argv[1])
vinc = json.load(open(sys.argv[2], encoding="utf-8"))
t = doc.read_text(encoding="utf-8")

def selo(v):
    st = v.get("verification_status")
    role = v.get("evid_role", "")
    if st == "pendente":
        return "[EMERGENTE]"
    if st == "preclinico":
        return "[PRÉ-CLÍNICO]"
    if st == "extrapolado":
        return "[EXTRAPOLADO: animal/célula→humano]"
    if st == "verificado":
        return "[VERIFICADO]"
    return None

# normaliza texto para casar (remove ** e espacos duplos)
def norm(s):
    return re.sub(r"\s+", " ", s.replace("**", "").replace("`", "")).strip()

# Ordena os vinculos pelo trecho mais longo primeiro (para nao substituir
# um trecho curto contido num maior).
vs = sorted(vinc, key=lambda x: -len(norm(x["trecho_ancora"])))

inseridos = 0
sem_match = []
for v in vs:
    if v.get("status_auditoria") == "NAO_LOCALIZADO":
        continue
    s = selo(v)
    if not s:
        continue
    trecho = norm(v["trecho_ancora"])
    if len(trecho) < 20:
        continue
    # ja tem selo de verification nesta frase?
    if "[VERIFICADO]" in trecho or "[PRÉ-CLÍNICO]" in trecho or "[EXTRAPOLADO" in trecho:
        continue
    # procura o fim da frase-ancora no texto (normalizado) e insere o selo
    # antes da tag de geração [ML]/[EC]... ou antes do ponto final.
    # Usamos o final do trecho (ultima palavra) como ancora de insercao.
    # Pega a ultima parte distintiva do trecho (15-40 chars finais sem colchetes)
    fim = re.sub(r"\[[^\]]*\].*$", "", trecho).strip()
    # ignora trechos que terminam com tag
    if len(fim) < 15:
        fim = trecho
    # construa versao do final para localizar no texto original (que tem **)
    # procura o trecho quase literal no documento normalizado
    norm_doc = norm(t)
    idx = norm_doc.find(trecho)
    if idx == -1:
        # tenta so o final
        idx = norm_doc.find(fim[-60:])
        if idx == -1:
            sem_match.append(v["id_vinculo"])
            continue
        end = idx + len(fim[-60:])
    else:
        end = idx + len(trecho)
    # ponto de insercao: mapeia de volta eh complexo; em vez disso,
    # anexa o selo logo apos o ponto final da frase no texto ORIGINAL.
    # Abordagem segura: insere o selo antes do padrao de tag de geracao
    # que encerra a citacao daquele trecho ( (Autor...)[XX; ...] )
    inseridos += 1

print(f"selos a aplicar (por status): {inseridos}")
print(f"sem casar (revisar): {len(sem_match)} -> {sem_match[:10]}")
