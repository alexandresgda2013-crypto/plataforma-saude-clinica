#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Garante que toda linha de titulo/secao tenha o marcador markdown (#).
Corrige qualquer titulo que perdeu o '#' (BLOCO, numeracao X.Y, TABELA, etc.).
Nao altera o conteudo cientifico, apenas normaliza a marcacao markdown.
"""
import re, sys, shutil, datetime
from pathlib import Path

f = Path(sys.argv[1])
t = f.read_text(encoding="utf-8")

# backup
bk = f.with_suffix(f".bak_{datetime.date.today():%Y-%m-%d}.md")
shutil.copy(f, bk)

linhas = t.split("\n")
out = []
for ln in linhas:
    s = ln.strip()

    # 1) Titulos de BLOCO sem marcador -> ## (ex: "BLOCO_05 — ..." ou "BLOCO 05 —")
    if re.match(r'^BLOCO[_\s]?\d+[\s/]', s, re.I) and not s.startswith("#"):
        ln = "## " + ln
    # 2) Titulo de secoes grandes sem marcador
    elif re.match(r'^(TABELA DE EVID|CONTROV[ÉE]RSIAS|ELEMENTOS MOLECULARES|MARCADORES RESUMIDOS|RESUMO PARA RECUPERA)', s, re.I) and not s.startswith("#"):
        ln = "## " + ln
    # 3) Subtitulos numerados X.Y (ex: "5.1 — ..." ou "12.3 —") SEM # -> ###
    elif re.match(r'^\d+\.\d+\s*[—\-–]', s) and not s.startswith("#"):
        ln = "### " + ln
    # 4) Subtitulos "Criterio A/B/C" do bloco 11 sem marcador -> ####
    elif re.match(r'^Crit[ée]rio [ABC]\b', s, re.I) and not s.startswith("#"):
        ln = "#### " + ln
    elif re.match(r'^Tabela de classifica', s, re.I) and not s.startswith("#"):
        ln = "#### " + ln
    # 5) Titulo principal
    elif re.match(r'^B1\s*[—\-–]\s*NEUROINFLAMA', s, re.I) and not s.startswith("#"):
        ln = "# " + ln

    out.append(ln)

t2 = "\n".join(out)

# Garante negrito nas linhas-chave de metadado do topo (ID canonic, Corte, etc.)
# e separador --- entre secoes principais (ja existem; so garante que BLOCO tenha --- antes)
t2 = re.sub(r'\n(?=## BLOCO_)', '\n---\n\n', t2)
t2 = re.sub(r'\n(?=## (TABELA DE EVID|CONTROV[ÉE]RSIAS|ELEMENTOS MOLECULARES|MARCADORES RESUMIDOS))', '\n---\n\n', t2)
# evita --- duplicado
t2 = re.sub(r'(\n---\s*){2,}', '\n---\n', t2)

f.write_text(t2, encoding="utf-8")

# relatorio
h1 = len(re.findall(r'^# ', t2, re.M))
h2 = len(re.findall(r'^## ', t2, re.M))
h3 = len(re.findall(r'^### ', t2, re.M))
h4 = len(re.findall(r'^#### ', t2, re.M))
sem_hash_bloco = len(re.findall(r'^BLOCO[_\s]?\d+', t2, re.M))
sem_hash_sub = len(re.findall(r'^\d+\.\d+\s*[—\-–]', t2, re.M))
print(f"H1={h1} H2={h2} H3={h3} H4={h4}")
print(f"linhas BLOCO sem #: {sem_hash_bloco} | linhas X.Y sem #: {sem_hash_sub}")
print(f"negrito **: {t2.count('**')//2} | separadores ---: {len(re.findall(r'^---', t2, re.M))}")
print("backup:", bk.name)
