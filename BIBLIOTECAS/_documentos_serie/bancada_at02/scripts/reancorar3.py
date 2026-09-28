#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reancorar3.py — AT-02, 3ª passada: RÓTULO DEFASADO (âncora dupla).

O PADRÃO
--------
Os 68 casos restantes são todos a mesma coisa. O vínculo traz o TÍTULO DO
ARTIGO no ponto em que a Canônica traz a CITAÇÃO NOMINAL:

  vínculo: «…em pacientes e modelos animais (Pathogenic NLRP3 mutants, 2024)[EC; …]»
  corpo  : «…em pacientes e modelos animais (Molina-López et al., 2024)[EC; …]»
                                            └── mesma posição, etiqueta diferente

Causa: a prosa foi normalizada para citação nominal DEPOIS que os vínculos
foram extraídos. O texto antes e depois do parêntese é idêntico; só o miolo
do parêntese mudou. Não é dado inventado — é dessincronização.

MÉTODO — ÂNCORA DUPLA
---------------------
Um único ponto de casamento (o prefixo) não basta: ele diz onde a frase
começa, mas não prova que o resto é a mesma frase. Foi assim que a 1ª passada
quase trocou VINC_B1_0001 por outra frase.

Aqui exige-se casamento nas DUAS pontas:

    [ prefixo comum ≥40 ]  (…parêntese divergente…)  [ sufixo comum ≥25 ]
             ↑                                                ↑
        localiza o início                          prova que é a mesma frase

O trecho devolvido é a fatia do corpo entre as duas âncoras — literal por
construção, e verificada mesmo assim.

GUARDA ADICIONAL — o ano tem de bater
--------------------------------------
Se o rótulo antigo cita um ano e a citação nova cita outro, NÃO é a mesma
referência: é troca de fonte disfarçada de reparo de formatação. Recusa.
Esta guarda existe por causa do resolvedor de parênteses do lote 5, que
trocou autoria (Menard→Li) por similaridade textual.

USO
---
    python3 reancorar3.py            # dry-run
    python3 reancorar3.py --apply
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from contrato import Contrato, norm, verificar_literal  # noqa: E402
from reancorar2 import RE_SELO_PLENO, sem_selos_com_mapa  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
VINCULOS = RAIZ / "canonico" / "evidencias_b1" / "vinculos_referencia_afirmacao.json"
CANONICA = RAIZ / "uploads" / "B1 NEUROINFLAMAÇÃO V4 CANONICA.md"

MIN_PREFIXO = 40
MIN_SUFIXO = 25


def prefixo_comum(a: str, b: str) -> int:
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def anos(s: str) -> set[str]:
    return set(re.findall(r"\b(19|20)\d{2}\b", s)) or set(
        re.findall(r"\b((?:19|20)\d{2})\b", s))


def anos_de(s: str) -> set[str]:
    return set(re.findall(r"\b(?:19|20)\d{2}\b", s))


def reparar(trecho: str, corpo_n: str) -> tuple[str | None, str]:
    """Devolve (fatia_literal, motivo) ou (None, motivo_da_recusa)."""
    alvo = norm(trecho)
    if len(alvo) < 60:
        return None, "trecho curto demais para âncora dupla"

    # -- âncora esquerda: maior prefixo do alvo presente no corpo
    lo, hi = 0, len(alvo)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if alvo[:mid] in corpo_n:
            lo = mid
        else:
            hi = mid - 1
    npre = lo
    if npre < MIN_PREFIXO:
        return None, f"prefixo insuficiente ({npre})"

    pre = alvo[:npre]
    if corpo_n.count(pre) != 1:
        return None, f"prefixo ambíguo ({corpo_n.count(pre)} ocorrências)"
    ini = corpo_n.find(pre)

    # -- âncora direita: maior sufixo do alvo presente logo adiante no corpo
    # -- âncora direita: maior sufixo do alvo presente logo adiante no corpo.
    # Busca-se na janela SEM SELOS: a cauda do vínculo termina em '.', e no
    # corpo o selo entra antes do ponto ("…humano][VERIFICADO]."), o que
    # zerava o sufixo e recusava reparos legítimos.
    janela = corpo_n[ini:ini + len(alvo) + 300]
    janela_lim, mapa_j = sem_selos_com_mapa(janela)
    alvo_lim = re.sub(r"\s+([.,;:!?])", r"\1",
                      RE_SELO_PLENO.sub("", alvo)).strip()
    alvo_lim = re.sub(r"\]\s+\[", "][", alvo_lim)

    melhor, pos_lim = 0, -1
    limite = max(len(alvo_lim) - MIN_PREFIXO, MIN_SUFIXO)
    for tam in range(min(limite, 200), MIN_SUFIXO - 1, -1):
        suf = alvo_lim[-tam:]
        p = janela_lim.find(suf, min(npre, len(janela_lim) - 1))
        if p >= 0:
            melhor, pos_lim = tam, p
            break
    if melhor < MIN_SUFIXO:
        return None, f"sufixo insuficiente ({melhor}) — não prova ser a mesma frase"

    fim_lim = pos_lim + melhor - 1
    fim = mapa_j[min(fim_lim, len(mapa_j) - 1)]
    # estende para abraçar selo e pontuação que sucedem a âncora direita
    j = fim + 1
    while j < len(janela):
        m = RE_SELO_PLENO.match(janela[j:j + 120])
        if m:
            j += m.end(); continue
        if janela[j] in ".;:!?":
            j += 1
        break
    fatia = janela[:j]

    # -- guarda do ano: mesma referência?
    a_alvo, a_fatia = anos_de(alvo), anos_de(fatia)
    if a_alvo and a_fatia and not (a_alvo & a_fatia):
        return None, f"ano divergente {sorted(a_alvo)} vs {sorted(a_fatia)} — outra fonte"

    return fatia.strip(), f"pre{npre}/suf{melhor}"


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
            falhas.append((v["id_vinculo"], motivo))
            continue
        atual = norm(v["trecho_ancora"])
        if novo not in corpo_n:
            falhas.append((v["id_vinculo"], "resultado não literal")); continue
        if not (0.6 <= len(novo) / max(len(atual), 1) <= 1.8):
            falhas.append((v["id_vinculo"],
                           f"tamanho incompatível {len(atual)}→{len(novo)}")); continue
        if novo == atual:
            falhas.append((v["id_vinculo"], "idêntico")); continue
        reparos.append((v, novo, motivo))

    print("═" * 74)
    print(f"  REANCORAR 3ª PASSADA (rótulo defasado) — "
          f"{'APLICAR' if args.apply else 'DRY-RUN'}")
    print("═" * 74)
    print(f"  EXAMINADOS ..... {len(vincs)}")
    print(f"  já literais .... {ja_ok}")
    print(f"  reparados ...... {len(reparos)}")
    print(f"  recusados ...... {len(falhas)}")
    print("─" * 74)
    for v, novo, motivo in reparos[:5]:
        a = norm(v["trecho_ancora"])
        print(f"  ✎ {v['id_vinculo']} [{motivo}]")
        print(f"      antes: «…{a[-62:]}»")
        print(f"      novo : «…{novo[-62:]}»")
    if len(reparos) > 5:
        print(f"  … mais {len(reparos) - 5}")
    if falhas:
        print("─" * 74)
        print(f"  ⚠️  {len(falhas)} recusado(s):")
        for vid, motivo in falhas[:10]:
            print(f"      {vid}: {motivo}")

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
        print(f"  ❌ ABORTADO — {len(novos)} bloqueante(s) novo(s). Nada gravado.")
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
