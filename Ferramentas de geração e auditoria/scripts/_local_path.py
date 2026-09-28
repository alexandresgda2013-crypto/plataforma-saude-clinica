#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Helper LOCAL do mecanismo (vai em processo_de_producao_e_ferramentas/ferramentas_scripts/).
Localiza, com caminho RELATIVO (sem hard-code), a pasta do mecanismo e o arquivo
canônico mais novo (maior _vN). A pasta do mecanismo é identificada por conter 'Evidencias/'.
Funciona em qualquer profundidade e se o workspace mudar de lugar."""
import re, sys
from pathlib import Path

def _acha_mec_dir(inicio: Path) -> Path:
    p = inicio.resolve()
    for cand in [p] + list(p.parents):
        if (cand / "Evidencias").exists():
            return cand
    return inicio  # fallback

MEC_DIR = _acha_mec_dir(Path(__file__))
RAIZ_BIBLIOTECAS = MEC_DIR.parent
MEC_PREFIXO = MEC_DIR.name.split("_")[0]

def versao(p: Path) -> int:
    m = re.search(r"_v(\d+)", p.name)
    return int(m.group(1)) if m else 0

def canonico_mais_novo():
    arqs = [a for a in MEC_DIR.glob("*.md") if "CANONICA" in a.name.upper()]
    arqs = sorted(arqs, key=versao)
    return arqs[-1] if arqs else None

def pasta_evidencias():
    return MEC_DIR / "Evidencias"

if __name__ == "__main__":
    print("Mecanismo :", MEC_DIR.name)
    print("Pasta     :", MEC_DIR)
    c = canonico_mais_novo()
    print("Canônico  :", c.name if c else "NENHUM")
    print("Evidências:", pasta_evidencias())
