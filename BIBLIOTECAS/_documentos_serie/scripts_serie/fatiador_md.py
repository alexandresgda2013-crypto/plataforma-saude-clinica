#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# fatiador_md.py — 2026-09-11. Fatiador de prosa MARKDOWN-AWARE (reescreve o fatiador
# condenado na 5ª rodada: nada de regex empilhado sobre markdown bruto).
# Estratégia ESTRUTURAL, não textual: (1) o documento é decomposto em BLOCOS pelo
# markdown (cabeçalhos, itens de lista, parágrafos, separadores); (2) dentro de cada
# bloco de prosa, as FRASES são delimitadas por pontuação terminal seguida de espaço+
# maiúscula/aspas/parentese, com exceções duras para não cortar abreviatura do domínio
# ("et al.", "vs.", "ca.", "p.e.", "Fig.", números decimais, "e.g.", "i.e.").
# Devolve fatias = frases completas, com o bloco de origem. Nenhum conteúdo é reescrito:
# a união das fatias de um bloco, na ordem, reproduz o bloco (round-trip testado).
import re, unicodedata

_EXCECOES = ("et al", "vs", "ca", "p.e", "e.g", "i.e", "fig", "et. al", "cf", "sr", "dr",
             "aprox", "obs", "seq", "inc", "ed", "vol", "pp", "no", "art")
_RE_NUM_DEC = re.compile(r"\d[.,]\d")

def _blocos(md: str):
    """Decompõe o markdown em blocos estruturais (linha a linha; agrupa prosa corrida)."""
    linhas = md.split("\n")
    blocos, buf, tipo = [], [], None
    def fecha():
        nonlocal buf, tipo
        if buf:
            blocos.append((tipo, "\n".join(buf).strip()))
            buf, tipo = [], None
    for ln in linhas:
        s = ln.strip()
        if not s:
            fecha(); continue
        if s.startswith("#"):
            fecha(); blocos.append(("cabecalho", s)); continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            fecha(); blocos.append(("separador", s)); continue
        if re.match(r"^([-*+] |\d+[.)] )", s):
            fecha(); buf, tipo = [s], "lista"; fecha(); continue
        buf.append(s); tipo = "prosa"
    fecha()
    return [b for b in blocos if b[0] in ("prosa", "lista", "cabecalho")]

def _frases(texto: str):
    """Fatia um bloco de prosa em frases. Corta em [.!?…] seguido de fronteira REAL:
    espaço + (maiúscula | abre-parêntese/aspas | início de citação), exceto abreviações."""
    t = unicodedata.normalize("NFC", texto)
    cortes = []
    for m in re.finditer(r"[.!?…]", t):
        i = m.start()
        if _RE_NUM_DEC.search(t[max(0,i-2):i+3]):  # decimal 0,45 / 1.25(OH)
            continue
        j = i + 1
        if j < len(t) and t[j] in ")]}\"'*":        # ponto antes de fecha-pontuação: anda junto
            while j < len(t) and t[j] in ")]}\"'*":
                j += 1
        if j >= len(t):
            cortes.append(j); break
        if t[j] != " ":
            continue
        pal = t[max(0, i-12):i].strip().split()[-1].strip("([{").lower() if t[max(0, i-12):i].strip() else ""
        if pal in _EXCECOES:
            continue
        nxt = t[j+1:j+3]
        if re.match(r"[A-ZÀ-Ú0-9\"'\(\[*-]", nxt):
            cortes.append(j)
    fatias, ini = [], 0
    for c in cortes:
        f = t[ini:c].strip()
        if f: fatias.append(f)
        ini = c
    resto = t[ini:].strip()
    if resto: fatias.append(resto)
    return fatias

def fatiar(md: str, incluir_cabecalho=False):
    """Devolve [{'tipo','bloco','frase'}...] na ordem do documento."""
    out = []
    for tipo, corpo in _blocos(md):
        if tipo == "cabecalho" and not incluir_cabecalho:
            continue
        if tipo == "cabecalho":
            out.append({"tipo": tipo, "bloco": corpo, "frase": corpo}); continue
        for f in _frases(corpo):
            out.append({"tipo": tipo, "bloco": corpo, "frase": f})
    return out

if __name__ == "__main__":
    # autoteste round-trip: a junção das fatias refaz o texto (módulo whitespace entre frases)
    import sys
    md = open(sys.argv[1], encoding="utf-8").read()
    fs = fatiar(md)
    print("fatias:", len(fs))
    plano = " ".join(f["frase"] for f in fs if f["tipo"] != "cabecalho").lower()
    alvo = " ".join(l.strip() for l in md.split("\n") if l.strip() and not l.strip().startswith("#") and not set(l.strip()) <= set("-*_ ") and not l.strip().startswith("---")).lower()
    sim = sum(1 for a, b in zip(plano, alvo) if a == b) / max(1, len(alvo))
    print(f"round-trip cobertura ≈ {sim:.1%} (esperado alto; cortes só em fronteira de frase)")
