#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reordena fisicamente as subseções (### X.Y) dentro de cada bloco (##),
em ordem numérica crescente, preservando 100% do conteúdo. Não altera
blocos H2, cabeçalho nem tabelas finais que não sejam ###."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _local_path import MEC_DIR, canonico_mais_novo

src = canonico_mais_novo()
txt = src.read_text(encoding="utf-8")

def num(headline):
    m = re.match(r"^###\s+(\d+)\.(\d+)", headline)
    return (int(m.group(1)), int(m.group(2))) if m else (999, 999)

lines = txt.split("\n")
out = []
i = 0
n = len(lines)
def is_h2(s): return s.startswith("## ") and not s.startswith("### ")
def is_h3(s): return s.startswith("### ")

while i < n:
    line = lines[i]
    # quando entra num H2, junta tudo até o próximo H2 e ordena os H3
    if is_h2(line):
        bloco = [line]
        i += 1
        # préambulo do H2 (texto antes do primeiro H3) + subseções
        pre = []
        subsecs = []   # lista de (numero, lista_de_linhas)
        atual = None
        while i < n and not is_h2(lines[i]):
            if is_h3(lines[i]):
                atual = [lines[i]]
                subsecs.append(atual)
            else:
                if atual is None:
                    pre.append(lines[i])
                else:
                    atual.append(lines[i])
            i += 1
        bloco.extend(pre)
        subsecs.sort(key=lambda s: num(s[0]))
        for s in subsecs:
            bloco.append("")      # linha em branco antes de cada subseção
            bloco.extend(s)
        out.extend(bloco)
    else:
        out.append(line)
        i += 1

new = "\n".join(out)
# consolida 3+ quebras de linha em 2
new = re.sub(r"\n{3,}", "\n\n", new)
src.write_text(new, encoding="utf-8")

# verifica ordem
ordem = [re.match(r"^###\s+(\d+\.\d+)", l).group(1) for l in new.split("\n") if l.startswith("### ")]
print("Ordem após reordenação:", ordem)
ok = ordem == sorted(ordem, key=lambda x: tuple(map(int, x.split("."))))
print("Crescente:", ok)
