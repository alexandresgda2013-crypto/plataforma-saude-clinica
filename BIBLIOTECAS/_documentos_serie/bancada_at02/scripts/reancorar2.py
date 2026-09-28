#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reancorar2.py — AT-02, 2ª passada: reconstrução por ALINHAMENTO DE ÍNDICES.

POR QUE UMA SEGUNDA PASSADA
----------------------------
A 1ª passada (reancorar.py) buscava a frase inteira por prefixo e a substituía.
Levou a literalidade de 40% para 71% e recusou 19 candidatos que seriam TROCA
de frase. Sobraram 74 casos que aquele método não resolve, por duas causas
descobertas na inspeção:

  (1) SELO COM CONTEÚDO. O enum de selos previa `[EXTRAPOLADO]`, mas a Canônica
      usa `[EXTRAPOLADO: animal/célula→humano]`. Selo com dois-pontos e texto
      não era reconhecido, então a divergência aparecia como "falta um ponto"
      (ex.: casa 373/374).

  (2) SELO NO FIM DA FRASE. O vínculo termina em `…humano+animal].` e o corpo
      em `…humano+animal][VERIFICADO].` — o selo entra ANTES da pontuação
      final, depois que o vínculo já fora extraído.

MÉTODO — diferente da 1ª passada, e mais seguro
------------------------------------------------
Não procura "uma frase parecida". Constrói um MAPA DE ÍNDICES entre o corpo
sem selos e o corpo original; localiza o trecho no corpo sem selos; e devolve
EXATAMENTE o pedaço correspondente do corpo original, estendido para incluir
os selos e a pontuação final.

O texto devolvido é, por construção, uma fatia literal do corpo — não um
candidato que precisa ser verificado depois. A verificação é feita mesmo
assim, porque confiar em construção é como os 7 geradores erraram.

GUARDAS (herdadas da 1ª passada, que quase trocou uma frase por outra)
-----------------------------------------------------------------------
  - o trecho sem selos tem de aparecer UMA única vez no corpo sem selos;
  - o resultado tem de ser substring literal do corpo;
  - o crescimento em relação ao original é limitado (só selos cabem);
  - o resultado tem de começar igual ao original.

USO
---
    python3 reancorar2.py            # dry-run
    python3 reancorar2.py --apply
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from contrato import Contrato, norm, verificar_literal  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
VINCULOS = RAIZ / "canonico" / "evidencias_b1" / "vinculos_referencia_afirmacao.json"
CANONICA = RAIZ / "uploads" / "B1 NEUROINFLAMAÇÃO V4 CANONICA.md"

# Selo = rótulo de verificação, com ou sem conteúdo após ':'.
# A forma com conteúdo ([EXTRAPOLADO: animal/célula→humano]) não estava
# prevista e é a causa de boa parte do resíduo desta passada.
NOMES_SELO = (
    "VERIFICADO", "PENDENTE_VERIF", "PRÉ-CLÍNICO", "PRE-CLINICO",
    "APENAS PRÉ-CLÍNICO", "APENAS PRE-CLINICO", "EMERGENTE",
    "EXTRAPOLADO", "EXTRAPOLAÇÃO POR ANALOGIA", "EXT", "G1",
)
RE_SELO_PLENO = re.compile(
    r"\s*\[(?:" + "|".join(re.escape(n) for n in NOMES_SELO) + r")(?::[^\]]*)?\]"
)


def sem_selos_com_mapa(texto: str) -> tuple[str, list[int]]:
    """Remove selos e devolve (texto_limpo, mapa).

    mapa[i] = índice, no texto original, do caractere i do texto limpo.
    É o que permite recuperar a fatia ORIGINAL a partir de uma posição
    encontrada no texto limpo — sem re-buscar e sem adivinhar.
    """
    partes, mapa, pos = [], [], 0
    for m in RE_SELO_PLENO.finditer(texto):
        for i in range(pos, m.start()):
            mapa.append(i)
        partes.append(texto[pos:m.start()])
        pos = m.end()
    for i in range(pos, len(texto)):
        mapa.append(i)
    partes.append(texto[pos:])
    return "".join(partes), mapa


def reconstruir(trecho: str, corpo_n: str, corpo_lim: str,
                mapa: list[int]) -> tuple[str | None, str]:
    """Devolve (fatia_literal_do_corpo, metodo) ou (None, motivo)."""
    alvo = re.sub(r"\s+", " ", RE_SELO_PLENO.sub(" ", norm(trecho))).strip()
    alvo = re.sub(r"\]\s+\[", "][", alvo)
    alvo = re.sub(r"\s+([.,;:!?])", r"\1", alvo)
    if len(alvo) < 40:
        return None, "alvo curto demais para ancorar com segurança"

    ocorr = [m.start() for m in re.finditer(re.escape(alvo), corpo_lim)]
    if not ocorr:
        # tenta sem a pontuação final (o vínculo pode tê-la acrescentado)
        alt = alvo.rstrip(".;: ")
        ocorr = [m.start() for m in re.finditer(re.escape(alt), corpo_lim)]
        if not ocorr:
            return None, "trecho não localizado no corpo (nem sem pontuação)"
        alvo = alt
    if len(ocorr) > 1:
        return None, f"trecho ambíguo — {len(ocorr)} ocorrências no corpo"

    ini_lim = ocorr[0]
    fim_lim = ini_lim + len(alvo) - 1
    ini = mapa[ini_lim]
    fim = mapa[fim_lim]

    # Estende à direita para abraçar selos e a pontuação final que os sucede.
    j = fim + 1
    while j < len(corpo_n):
        resto = corpo_n[j:j + 120]
        m = RE_SELO_PLENO.match(resto)
        if m:
            j += m.end()
            continue
        if corpo_n[j] in ".;:!?":
            j += 1
            break
        break
    return corpo_n[ini:j].strip(), "alinhamento_indices"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    corpo = CANONICA.read_text(encoding="utf-8")
    dados = json.loads(VINCULOS.read_text(encoding="utf-8"))
    vincs = dados.get("vinculos", dados) if isinstance(dados, dict) else dados

    corpo_n = norm(corpo)
    corpo_lim, mapa = sem_selos_com_mapa(corpo_n)

    c0 = Contrato("vinculo", corpo_canonico=corpo)
    bloq_antes = {f"{p.item}|{p.campo}|{p.msg}"
                  for p in c0.validar(vincs) if p.nivel == "BLOQUEANTE"}

    reparos, falhas, ja_ok = [], [], 0
    for v in vincs:
        st = verificar_literal(v.get("trecho_ancora", ""), corpo)["status"]
        if st == "LITERAL":
            ja_ok += 1
            continue
        novo, metodo = reconstruir(v.get("trecho_ancora", ""), corpo_n,
                                   corpo_lim, mapa)
        if novo is None:
            falhas.append((v["id_vinculo"], st, metodo))
            continue

        atual = norm(v["trecho_ancora"])
        # -- guardas
        if novo not in corpo_n:
            falhas.append((v["id_vinculo"], st, "resultado não é literal")); continue
        if not novo.startswith(atual[:40]):
            falhas.append((v["id_vinculo"], st, "início divergente — outra frase")); continue
        if len(novo) > len(atual) * 1.6 + 80:
            falhas.append((v["id_vinculo"], st,
                           f"cresceu demais ({len(atual)}→{len(novo)})")); continue
        if novo == atual:
            falhas.append((v["id_vinculo"], st, "idêntico ao atual")); continue
        reparos.append((v, novo, st, metodo))

    print("═" * 74)
    print(f"  REANCORAR 2ª PASSADA — {'APLICAR' if args.apply else 'DRY-RUN'}")
    print("═" * 74)
    print(f"  EXAMINADOS ..... {len(vincs)}")
    print(f"  já literais .... {ja_ok}")
    print(f"  reconstruídos .. {len(reparos)}")
    print(f"  não resolvidos . {len(falhas)}")
    print("─" * 74)
    for v, novo, st, _ in reparos[:5]:
        print(f"  ✎ {v['id_vinculo']} [{st}]")
        print(f"      antes: «…{norm(v['trecho_ancora'])[-58:]}»")
        print(f"      novo : «…{novo[-58:]}»")
    if len(reparos) > 5:
        print(f"  … mais {len(reparos) - 5}")
    if falhas:
        print("─" * 74)
        print(f"  ⚠️  {len(falhas)} não resolvido(s):")
        for vid, st, motivo in falhas[:8]:
            print(f"      {vid} [{st}] {motivo}")

    if not args.apply:
        print("═" * 74); print("  DRY-RUN — nada gravado.")
        return 0

    for v, novo, _, _ in reparos:
        v["trecho_ancora"] = novo

    c = Contrato("vinculo", corpo_canonico=corpo)
    depois = {f"{p.item}|{p.campo}|{p.msg}"
              for p in c.validar(vincs) if p.nivel == "BLOQUEANTE"}
    novos = depois - bloq_antes
    if novos:
        print("═" * 74)
        print(f"  ❌ ABORTADO — {len(novos)} bloqueante(s) NOVO(S). Nada gravado.")
        for k in sorted(novos)[:5]:
            print(f"     {k}")
        return 1
    if depois:
        print("─" * 74)
        print(f"  ⚠️  {len(depois)} bloqueante(s) pré-existente(s) permanecem (AT-01).")
    r = c.gravar(VINCULOS, dados if isinstance(dados, dict) else vincs)
    print(f"  ✅ gravado · backup: {r['backup']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
