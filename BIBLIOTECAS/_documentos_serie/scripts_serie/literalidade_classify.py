#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# literalidade_classify.py — v2 (2026-09-10, pós-depuração da 4ª rodada da perícia)
# Classificador INDEPENDENTE de literalidade de trechos-âncora de vínculos contra a canônica.
# HISTÓRICO (regra AT-10): v1 sub-contava a classe ROTULO por (i) não remover ênfases
#   markdown (**negrito**) das sementes, (ii) semear só no offset 0 (âncoras com cabeçalho
#   "### 2.2 —" falhavam), (iii) exigir "(" no início da divergência (divergência ocorre
#   DENTRO do parêntese de citação). Caso-guia: VINC_B1_0019 (309/366 chars casados).
# Definições operacionais v2:
#   LITERAL      : trecho normalizado (espaços + ênfases markdown) ocorre na canônica.
#   LITERAL_APROX: melhor janela cobre >=97% do trecho com divergência residual <=8 chars
#                  que não seja citação (pontuação/acento isolado).
#   SELO         : só casa após remover selos [ML/EC/OB/...] de AMBOS os lados.
#   ROTULO       : prefixo longo casado (>=100); o grupo "(…, ano)" que contém o 1º ponto de
#                  divergência é TÍTULO no vínculo (sem "et al") e citação NOMINAL na canônica.
#   PROSA        : prefixo longo casado; divergência real de prosa.
#   AUSENTE      : nenhum prefixo >= 100 chars (pode nunca ter existido na vigente).
# Uso: python3 literalidade_classify.py <B0X> [--amostras N] [--ids] ; saída em contagens.
import json, re, glob, sys, collections

SELO_RE = re.compile(
    r"\[(?:ML|EC|OB|MA|SR|RI|G1|G2|G3|RCT|VERIFICADO(?:_PARCIAL)?|PENDENTE\w*|REF|LISTRA|V[ÍI]NCULO)"
    r"(?:[\s;:][^\]\[]{0,90})?\]"
)
WS = re.compile(r"\s+")
MD = re.compile(r"[*`]+")
CIT_NOMINAL = re.compile(r"\([A-ZÀ-Þ][-\w]*(?:[ -][A-ZÀ-Þ][-\w]*){0,2} et al\., (?:19|20)\d{2}[a-z]?")
ANO_GRUPO = re.compile(r"(?:19|20)\d{2}[a-z]?")

def norm(s):
    s = MD.sub("", s or "")
    return WS.sub(" ", s).strip()

def de_seal(s): return norm(SELO_RE.sub("", s))

def grupo_paren(texto, pos):
    """Retorna o grupo '(…)' que contém pos (até 400 chars para trás)."""
    ini = texto.rfind("(", max(0, pos - 400), pos + 1)
    fim = texto.find(")", pos)
    if ini < 0 or fim < 0 or fim - ini > 420: return ""
    return texto[ini:fim + 1]

def melhor_alinhamento(t2, c2):
    """Multi-offset: a maior extensão de prefixo a partir de qualquer semente de 40 chars."""
    best = (0, 0, 0)  # (L, off_t, pos_c)
    for off in range(0, max(len(t2) - 39, 1), 25):
        seed = t2[off:off + 40]
        if len(seed) < 40: break
        start = 0
        while True:
            j = c2.find(seed, start)
            if j < 0: break
            L = off + 40
            lim = min(len(t2), j - off + len(t2))
            k = j + 40
            while L - off + off < len(t2) and k < len(c2) and t2[off + (k - j)] == c2[k]:
                L += 1; k += 1
            if L - off > best[0]: best = (L - off, off, j)
            start = j + 1
    return best  # comprimento do prefixo casado a partir de off_t

def classify(T, c, c2):
    t = norm(T); t2 = de_seal(t)
    if not t: return ("VAZIO", 0, 0, "")
    if t in c: return ("LITERAL", len(t), len(t), "")
    if t2 and t2 in c2: return ("SELO", len(t2), len(t2), "")
    L, off, jc = melhor_alinhamento(t2, c2)
    if L >= 100:
        pos_t = off + L; pos_c = jc + L
        gt = grupo_paren(t2, pos_t); gc = grupo_paren(c2, min(pos_c, len(c2) - 1))
        if gt and ANO_GRUPO.search(gt) and "et al" not in gt and CIT_NOMINAL.match(gc):
            return ("ROTULO", L, len(t2), f"V:{gt[:70]!r} | C:{gc[:70]!r}")
        resto = t2[pos_t:]
        if (len(t2) - off - L) <= 8 and off <= 8:
            return ("LITERAL_APROX", L, len(t2), resto[:40])
        return ("PROSA", L, len(t2), t2[pos_t:pos_t + 90])
    return ("AUSENTE", L, len(t2), t2[:90])

def load_bib(bxx):
    atuais = glob.glob(f"/home/user/BIBLIOTECAS/{bxx}_*/atuais")
    if not atuais: raise SystemExit(f"pasta não achada: {bxx}")
    md = sorted(glob.glob(atuais[0] + "/*.md"))
    canon = open(md[0], encoding="utf-8").read()
    vinc = glob.glob(atuais[0] + "/Evidencias/Vinculos/*.json")
    d = json.load(open(vinc[0], encoding="utf-8"))
    recs = d if isinstance(d, list) else d.get("vinculos", d.get("registros", []))
    return canon, recs, vinc[0]

if __name__ == "__main__":
    bxx = sys.argv[1]
    n_am = int(sys.argv[sys.argv.index("--amostras") + 1]) if "--amostras" in sys.argv else 2
    canon, recs, arq = load_bib(bxx)
    c, c2 = norm(canon), de_seal(norm(canon))
    por = collections.defaultdict(list)
    for r in recs:
        cat, cas, tot, div = classify(r.get("trecho_ancora", ""), c, c2)
        por[cat].append((str(r.get("id_vinculo")), cas, tot, div))
    total = sum(len(v) for v in por.values())
    print(f"### {bxx} — {total} vínculos ({arq.split('BIBLIOTECAS/')[-1]})")
    for cat in ("LITERAL", "LITERAL_APROX", "SELO", "ROTULO", "PROSA", "AUSENTE", "VAZIO"):
        v = por.get(cat, [])
        if v: print(f"  {cat:13s}: {len(v):4d}")
    nc_v2 = sum(1 for cat in por for rec in por[cat]
                if "V2" in rec[0].upper() and cat not in ("LITERAL", "LITERAL_APROX"))
    rot_v2 = sum(1 for rec in por.get("ROTULO", []) if "V2" in rec[0].upper())
    print(f"  não-conformes na leva V2: {nc_v2} | ROTULO na leva V2: {rot_v2}")
    repara = len(por.get("SELO", [])) + len(por.get("ROTULO", []))
    print(f"  auto-reparáveis por prefixo (SELO+ROTULO): {repara} | manuais (PROSA+AUSENTE): "
          f"{len(por.get('PROSA', [])) + len(por.get('AUSENTE', []))}")
    for cat in ("SELO", "ROTULO", "PROSA", "AUSENTE", "LITERAL_APROX"):
        for idv, cas, tot, div in por.get(cat, [])[:n_am]:
            print(f"    · [{cat}] {idv} {cas}/{tot} :: {div}")
