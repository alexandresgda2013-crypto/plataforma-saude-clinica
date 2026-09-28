#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reancorar4.py — AT-02, 4ª passada: MÚLTIPLOS rótulos defasados (multi-âncora).

O PADRÃO QUE SOBROU
-------------------
A 3ª passada resolveu trechos com UM parêntese defasado (âncora dupla:
prefixo + sufixo). Os 30 restantes têm DOIS OU MAIS:

  vínculo: «…alvo terapêutico (Pain-resolving immune mechanisms, 2023)[OB],
            e a maresina MaR2 … no frio (Brown adipose MaR2 resolution, 2022)[ML]»
  corpo  : «…alvo terapêutico (Fiore et al., 2023)[OB],
            e a maresina MaR2 … no frio (Serhan et al., 2022)[ML]»

O sufixo também diverge, então a âncora direita da 3ª passada zerava.

MÉTODO — ALINHAMENTO POR SEGMENTOS DE PROSA
--------------------------------------------
A prosa entre os parênteses é idêntica; só o miolo dos parênteses mudou.
Então: fatia-se o alvo nos parênteses de citação, e casam-se os segmentos de
prosa EM ORDEM no corpo. O resultado é a fatia do corpo do primeiro ao último
segmento.

    [prosa A] (cit1 divergente) [prosa B] (cit2 divergente) [prosa C]
        ↓                            ↓                          ↓
     casa em ordem, com avanço monotônico da posição no corpo

Exige-se ≥2 segmentos com ≥25 chars, casando em ordem crescente e dentro de
uma janela proporcional ao tamanho do alvo. Isso é mais forte que a âncora
dupla: são N pontos de concordância, não 2.

GUARDA DO ANO — herdada e obrigatória
--------------------------------------
Se os anos citados no alvo não estiverem TODOS presentes na fatia recuperada,
recusa. Um rótulo pode ser reescrito; o ano da fonte, não. Foi assim que
VINC_B1_0047 foi corretamente recusado: alvo cita 2007, corpo cita 2005 —
não é dessincronização de etiqueta, é referência diferente, e isso é
decisão de conteúdo, não de formatação.

USO
---
    python3 reancorar4.py            # dry-run
    python3 reancorar4.py --apply
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from contrato import Contrato, norm, verificar_literal  # noqa: E402
from reancorar2 import RE_SELO_PLENO  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
VINCULOS = RAIZ / "canonico" / "evidencias_b1" / "vinculos_referencia_afirmacao.json"
CANONICA = RAIZ / "uploads" / "B1 NEUROINFLAMAÇÃO V4 CANONICA.md"

# Parêntese de citação: contém um ano de 4 dígitos.
RE_CITACAO = re.compile(r"\((?=[^()]*\b(?:19|20)\d{2}\b)[^()]*\)")
MIN_SEG = 25


def segmentos(alvo: str) -> list[str]:
    """Prosa entre parênteses de citação, sem selos, com ≥MIN_SEG chars."""
    bruto = RE_CITACAO.sub("\x00", alvo)
    bruto = RE_SELO_PLENO.sub("\x00", bruto)
    return [s.strip() for s in bruto.split("\x00") if len(s.strip()) >= MIN_SEG]


def anos_de(s: str) -> list[str]:
    return re.findall(r"\b(?:19|20)\d{2}\b", s)


def reparar(trecho: str, corpo_n: str) -> tuple[str | None, str]:
    alvo = norm(trecho)
    segs = segmentos(alvo)
    if len(segs) < 2:
        return None, f"apenas {len(segs)} segmento(s) de prosa — multi-âncora exige 2+"

    # casa os segmentos em ordem, com avanço monotônico
    pos, marcas = 0, []
    for s in segs:
        p = corpo_n.find(s, pos)
        if p < 0:
            return None, f"segmento não encontrado: «{s[:38]}…»"
        marcas.append((p, p + len(s)))
        pos = p + len(s)

    ini, fim = marcas[0][0], marcas[-1][1]
    span = fim - ini
    if not (0.7 <= span / max(len(alvo), 1) <= 1.6):
        return None, f"vão incompatível ({span} vs alvo {len(alvo)})"

    # estende à direita para abraçar citação/selo/pontuação finais
    j = fim
    while j < len(corpo_n):
        r = corpo_n[j:j + 160]
        m = RE_CITACAO.match(r) or RE_SELO_PLENO.match(r)
        if m:
            j += m.end(); continue
        if corpo_n[j] in ".;:!?":
            j += 1
        break
    fatia = corpo_n[ini:j].strip()

    # guarda do ano: todo ano do alvo tem de existir na fatia
    fa = anos_de(fatia)
    faltando = [a for a in set(anos_de(alvo)) if a not in fa]
    if faltando:
        return None, (f"ano(s) {faltando} do vínculo ausente(s) na fatia — "
                      f"referência diferente, não dessincronização")
    return fatia, f"{len(segs)}segs"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    corpo = CANONICA.read_text(encoding="utf-8")
    corpo_n = norm(corpo)
    dados = json.loads(VINCULOS.read_text(encoding="utf-8"))
    vincs = dados.get("vinculos", dados) if isinstance(dados, dict) else dados

    c0 = Contrato("vinculo", corpo_canonico=corpo)
    bloq_antes = {f"{p.item}|{p.campo}|{p.msg}"
                  for p in c0.validar(vincs) if p.nivel == "BLOQUEANTE"}

    reparos, falhas, ja_ok = [], [], 0
    for v in vincs:
        if verificar_literal(v.get("trecho_ancora", ""), corpo)["status"] == "LITERAL":
            ja_ok += 1
            continue
        novo, motivo = reparar(v.get("trecho_ancora", ""), corpo_n)
        if novo is None:
            falhas.append((v["id_vinculo"], motivo)); continue
        atual = norm(v["trecho_ancora"])
        if novo not in corpo_n:
            falhas.append((v["id_vinculo"], "resultado não literal")); continue
        if novo == atual:
            falhas.append((v["id_vinculo"], "idêntico")); continue
        # Guarda de FRONTEIRA (PROMPT v4.2 L1450): trecho tem de terminar em
        # pontuação, tag ou selo. Sem isto o multi-âncora pode devolver uma
        # fatia que corta no meio da frase — pior que o original, porque
        # "conserta" a literalidade destruindo a unidade de sentido.
        if not re.search(r"[.!?\]]$", novo):
            falhas.append((v["id_vinculo"],
                           "fatia terminaria fora de fronteira natural "
                           "(truncaria a frase) — recusado")); continue
        reparos.append((v, novo, motivo))

    print("═" * 74)
    print(f"  REANCORAR 4ª PASSADA (multi-âncora) — "
          f"{'APLICAR' if args.apply else 'DRY-RUN'}")
    print("═" * 74)
    print(f"  EXAMINADOS ..... {len(vincs)}")
    print(f"  já literais .... {ja_ok}")
    print(f"  reparados ...... {len(reparos)}")
    print(f"  recusados ...... {len(falhas)}")
    print("─" * 74)
    for v, novo, motivo in reparos[:5]:
        print(f"  ✎ {v['id_vinculo']} [{motivo}]")
        print(f"      antes: «…{norm(v['trecho_ancora'])[-62:]}»")
        print(f"      novo : «…{novo[-62:]}»")
    if len(reparos) > 5:
        print(f"  … mais {len(reparos) - 5}")
    if falhas:
        print("─" * 74)
        print(f"  ⚠️  {len(falhas)} recusado(s) — vão para inspeção humana:")
        for vid, motivo in falhas[:12]:
            print(f"      {vid}: {motivo}")

    inv = RAIZ / "canonico" / "at02_residuo_manual.json"
    inv.write_text(json.dumps(
        [{"id_vinculo": a, "motivo": b} for a, b in falhas],
        ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  resíduo → {inv.relative_to(RAIZ)}")

    if not args.apply:
        print("═" * 74); print("  DRY-RUN — nada gravado.")
        return 0

    for v, novo, _ in reparos:
        v["trecho_ancora"] = novo
    c = Contrato("vinculo", corpo_canonico=corpo)
    depois = {f"{p.item}|{p.campo}|{p.msg}"
              for p in c.validar(vincs) if p.nivel == "BLOQUEANTE"}
    novos = depois - bloq_antes
    if novos:
        print(f"  ❌ ABORTADO — {len(novos)} bloqueante(s) novo(s).")
        for k in sorted(novos)[:5]:
            print(f"     {k}")
        return 1
    if depois:
        print(f"  ⚠️  {len(depois)} bloqueante(s) pré-existente(s) permanecem (AT-01).")
    r = c.gravar(VINCULOS, dados if isinstance(dados, dict) else vincs)
    print(f"  ✅ gravado · backup: {r['backup']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
