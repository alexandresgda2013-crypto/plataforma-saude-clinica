#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reancorar.py — AT-02: re-extração literal de `trecho_ancora` (dry-run por padrão).

O QUE FAZ
---------
Para cada vínculo cujo trecho não é literal na Canônica, tenta recuperar a
FRASE REAL do corpo e propõe a substituição. Não grava sem `--apply`.

MÉTODO (herdado do melhor script do acervo — lote 7 #7)
-------------------------------------------------------
    trecho = localizar_no_corpo(...)
    if trecho is None:
        registrar_falha(); continue        # NUNCA inventa
    if trecho not in corpo:
        registrar_falha(); continue        # verifica antes de aceitar

É o oposto do fallback `probe + "."` dos 7 geradores, que gravava o texto
digitado à mão como se fosse literal do corpo.

ESCOPO (decidido em 2026-09-10, CONTRARRAZÃO A2.1)
---------------------------------------------------
Só o arquivo de VÍNCULOS. O ledger da B1 tem 237/237 âncoras literais
(arquitetura de listra) e está FORA deste reparo.

CATEGORIAS TRATADAS
-------------------
  SELO    (22) — selo inserido na prosa após a extração. Auto-reparável.
  ROTULO  (77) — vínculo traz título em inglês; Canônica traz (Autor, ano).
                 Auto-reparável: o prefixo longo localiza a frase.
  PROSA   (55) — Canônica editada após a extração. NÃO auto-reparável:
                 sai em relatório para inspeção humana.
  AUSENTE      — candidato a fabricação. NUNCA reparado automaticamente.

USO
---
    python3 reancorar.py                      # dry-run, relatório
    python3 reancorar.py --apply              # grava (backup automático)
    python3 reancorar.py --only ROTULO        # limita a uma categoria
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from contrato import (Contrato, norm, norm_selos, verificar_literal,  # noqa: E402
                      abortar_se)

RAIZ = Path(__file__).resolve().parent.parent
VINCULOS = RAIZ / "canonico" / "evidencias_b1" / "vinculos_referencia_afirmacao.json"
CANONICA = RAIZ / "uploads" / "B1 NEUROINFLAMAÇÃO V4 CANONICA.md"

AUTO_REPARAVEL = {"SELO", "ROTULO"}


def frases_do_corpo(corpo: str) -> list[str]:
    """Fatia o corpo em frases completas.

    Fronteira natural = pontuação final OU fechamento de tag ']', conforme
    PROMPT v4.2 L1450. Ignora linhas de título (#) — cabeçalho markdown como
    âncora foi um defeito real (VINC_B1_0019).
    """
    linhas = [l for l in corpo.split("\n") if not l.lstrip().startswith("#")]
    plano = norm("\n".join(linhas))
    # separa após '.', '!' ou '?' que estejam fora de parênteses/colchetes
    partes = re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ú])", plano)
    return [p.strip() for p in partes if len(p.strip()) > 30]


def recuperar(trecho: str, corpo: str, frases: list[str]) -> tuple[str | None, str]:
    """Devolve (frase_literal, metodo) ou (None, motivo_da_falha).

    Só devolve texto que É substring literal do corpo. Verificado aqui, não
    presumido — é a diferença entre este script e os 7 geradores.
    """
    corpo_n = norm(corpo)
    alvo = norm_selos(trecho)
    if not alvo:
        return None, "trecho vazio"

    # 1) O prefixo que já casa localiza a frase no corpo.
    for tam in (200, 150, 120, 100, 80, 60, 40):
        if len(alvo) < tam:
            continue
        chave = alvo[:tam]
        if chave not in norm_selos(corpo):
            continue
        cands = [f for f in frases if chave[:min(tam, 60)] in norm_selos(f)]
        if len(cands) == 1:
            if norm(cands[0]) in corpo_n:
                return norm(cands[0]), f"prefixo_{tam}"
        elif len(cands) > 1:
            # desempata pela maior sobreposição com o alvo
            melhor = max(cands, key=lambda f: _sobrepos(alvo, norm_selos(f)))
            if _sobrepos(alvo, norm_selos(melhor)) >= 40 and norm(melhor) in corpo_n:
                return norm(melhor), f"prefixo_{tam}_desempate"

    # 2) O trecho pode abranger mais de uma frase: tenta janela contígua.
    n = norm_selos(corpo)
    if alvo[:60] in n:
        i = n.find(alvo[:60])
        janela = n[i:i + len(alvo) + 120]
        m = re.match(r"^.{%d,}?[.!?\]](?=\s|$)" % max(len(alvo) - 60, 40), janela)
        if m:
            cand = m.group(0).strip()
            # reconstrói a forma COM selos, que é a que existe no corpo
            bruto = _com_selos(cand, corpo)
            if bruto and norm(bruto) in corpo_n:
                return norm(bruto), "janela"

    return None, "frase não localizada no corpo"


def _sobrepos(a: str, b: str) -> int:
    """Maior prefixo comum entre duas strings."""
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def _com_selos(sem_selo: str, corpo: str) -> str | None:
    """Dado um texto sem selos, encontra a forma original no corpo."""
    corpo_n = norm(corpo)
    chave = sem_selo[:50]
    idx = norm_selos(corpo).find(chave)
    if idx < 0:
        return None
    # busca por prefixo crescente na forma normal
    aprox = corpo_n.find(sem_selo[:40])
    if aprox < 0:
        return None
    fim = aprox + len(sem_selo) + 60
    janela = corpo_n[aprox:fim]
    m = re.match(r"^.*?[.!?](?=\s|$)", janela)
    return m.group(0).strip() if m else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="grava as correções (padrão: dry-run)")
    ap.add_argument("--only", default=None,
                    help="limita a uma categoria (SELO/ROTULO/PROSA)")
    args = ap.parse_args()

    if not VINCULOS.exists() or not CANONICA.exists():
        print(f"❌ fonte ausente: {VINCULOS if not VINCULOS.exists() else CANONICA}")
        return 2

    corpo = CANONICA.read_text(encoding="utf-8")
    dados = json.loads(VINCULOS.read_text(encoding="utf-8"))
    vincs = dados.get("vinculos", dados) if isinstance(dados, dict) else dados
    frases = frases_do_corpo(corpo)

    # Fotografa os bloqueantes ANTES de qualquer alteração, para a validação
    # diferencial no fim (só responder pelo que este script muda).
    _c0 = Contrato("vinculo", corpo_canonico=corpo)
    bloq_antes = {f"{p.item}|{p.campo}|{p.msg}"
                  for p in _c0.validar(vincs) if p.nivel == "BLOQUEANTE"}

    reparados, falhas, manuais, ja_ok = [], [], [], 0

    for v in vincs:
        res = verificar_literal(v.get("trecho_ancora", ""), corpo)
        st = res["status"]
        if st == "LITERAL":
            ja_ok += 1
            continue
        if args.only and st != args.only:
            continue
        if st not in AUTO_REPARAVEL:
            manuais.append((v["id_vinculo"], st, res["casados"], res["total"],
                            res["divergencia"][:50]))
            continue

        novo, metodo = recuperar(v["trecho_ancora"], corpo, frases)
        if novo is None:
            falhas.append((v["id_vinculo"], st, metodo))
            continue
        # ---- guarda 1: tem de ser literal no corpo (inegociável)
        if norm(novo) not in norm(corpo):
            falhas.append((v["id_vinculo"], st, "candidato não é literal — descartado"))
            continue
        # ---- guarda 2: tem de ser A MESMA FRASE, não outra frase literal.
        # Sem isto o script "conserta" trocando a âncora por um trecho
        # verdadeiro porém alheio — a mesma classe do resolvedor de parênteses
        # que trocou autoria (lote 5 #4). Exige-se prefixo comum longo com o
        # alvo original E tamanho compatível.
        alvo, cand = norm_selos(v["trecho_ancora"]), norm_selos(novo)
        pref = _sobrepos(alvo, cand)
        if pref < max(60, int(0.5 * len(alvo))):
            falhas.append((v["id_vinculo"], st,
                           f"candidato diverge cedo (prefixo comum {pref}/{len(alvo)}) "
                           f"— seria troca de frase, não reparo"))
            continue
        if not (0.6 <= len(cand) / max(len(alvo), 1) <= 1.6):
            falhas.append((v["id_vinculo"], st,
                           f"tamanho incompatível ({len(cand)} vs {len(alvo)})"))
            continue
        # ---- guarda 3: reparo que não muda nada não é reparo
        if norm(novo) == norm(v["trecho_ancora"]):
            falhas.append((v["id_vinculo"], st, "candidato idêntico ao atual"))
            continue
        reparados.append((v, novo, metodo, st, pref))

    # ---------------------------------------------------------------- relatório
    print("═" * 74)
    print(f"  REANCORAR (AT-02) — {'APLICAR' if args.apply else 'DRY-RUN'}")
    print("═" * 74)
    print(f"  EXAMINADOS ......... {len(vincs)}")
    print(f"  já literais ........ {ja_ok}")
    print(f"  reparáveis ......... {len(reparados)}")
    print(f"  falhas de recuperação {len(falhas)}")
    print(f"  para inspeção manual  {len(manuais)}")
    print("─" * 74)

    for v, novo, metodo, st, pref in reparados[:6]:
        print(f"  ✎ {v['id_vinculo']} [{st}·{metodo}·pref{pref}]")
        print(f"      antes: «…{norm_selos(v['trecho_ancora'])[-55:]}»")
        print(f"      novo : «…{norm(novo)[-55:]}»")
    if len(reparados) > 6:
        print(f"  … mais {len(reparados) - 6} reparo(s)")

    if falhas:
        print("─" * 74)
        print(f"  ⚠️  {len(falhas)} não recuperado(s) — permanecem como estão:")
        for vid, st, motivo in falhas[:5]:
            print(f"      {vid} [{st}] {motivo}")

    if manuais:
        print("─" * 74)
        print(f"  📋 {len(manuais)} exigem inspeção humana (prosa divergente):")
        for vid, st, c, t, div in manuais[:5]:
            print(f"      {vid} casa {c}/{t} · diverge «{div}…»")

    # inventário sempre gravado — é a fila de trabalho
    inv = RAIZ / "canonico" / "reancoragem_b1.json"
    inv.write_text(json.dumps({
        "examinados": len(vincs), "ja_literais": ja_ok,
        "reparaveis": [{"id_vinculo": v["id_vinculo"], "metodo": m,
                        "categoria": s, "antes": v["trecho_ancora"], "depois": n, "prefixo_comum": p}
                       for v, n, m, s, p in reparados],
        "nao_recuperados": [{"id_vinculo": a, "categoria": b, "motivo": c}
                            for a, b, c in falhas],
        "inspecao_manual": [{"id_vinculo": a, "categoria": b, "casados": c,
                             "total": d, "divergencia": e}
                            for a, b, c, d, e in manuais],
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print("─" * 74)
    print(f"  inventário → {inv.relative_to(RAIZ)}")

    if not args.apply:
        print("═" * 74)
        print("  DRY-RUN — nada gravado. Use --apply para efetivar.")
        return 0

    # ---------------------------------------------------------------- aplicar
    for v, novo, _, _, _ in reparados:
        v["trecho_ancora"] = novo

    # Validação diferencial: este script só responde pelo que ELE muda.
    # Bloqueantes pré-existentes (os 30 de AT-01 e os 3 de AT-11) não podem
    # travar um reparo que não os toca — mas também não podem ser ignorados:
    # são recontados e exibidos, e qualquer bloqueante NOVO aborta.
    c = Contrato("vinculo", corpo_canonico=corpo)
    depois = {f"{p.item}|{p.campo}|{p.msg}"
              for p in c.validar(vincs) if p.nivel == "BLOQUEANTE"}
    novos = depois - bloq_antes
    if novos:
        print("═" * 74)
        print(f"  ❌ ABORTADO: o reparo INTRODUZIU {len(novos)} bloqueante(s). Nada gravado.")
        for k in sorted(novos)[:5]:
            print(f"     {k}")
        return 1
    if depois:
        print("─" * 74)
        print(f"  ⚠️  {len(depois)} bloqueante(s) PRÉ-EXISTENTE(S) permanecem "
              f"(AT-01: campos trocados · AT-11: tier_2_intervencao). "
              f"Fora do escopo deste reparo.")

    r = c.gravar(VINCULOS, dados if isinstance(dados, dict) else vincs)
    print(f"  ✅ gravado · backup: {r['backup']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
