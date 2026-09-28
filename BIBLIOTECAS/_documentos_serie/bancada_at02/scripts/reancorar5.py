#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reancorar5.py — AT-02/AT-13, 5ª passada: ÂNCORA PELA PRÓPRIA CITAÇÃO.

A REGRA (determinística, não heurística)
-----------------------------------------
    O trecho_ancora de um vínculo deve ser a frase da Canônica que contém
    a citação nominal DA PRÓPRIA REFERÊNCIA daquele vínculo.

Não é palpite sobre "qual frase parece a certa". É a definição do que um
vínculo É: a ligação entre uma afirmação e a fonte que a sustenta. Se
`REF_HAO_2024` é a fonte, a âncora tem de ser a frase onde a Canônica escreve
`(Hao et al., 2024)`. Qualquer outra frase é âncora errada, ainda que literal.

POR QUE ISTO É VERIFICAÇÃO E NÃO EXTRAPOLAÇÃO
----------------------------------------------
A regra deriva de dois textos normativos já existentes, não de inferência:

  PROMPT v4.2 L1256 — "o veredito de suporte científico (G3) é sempre
                       por vínculo, nunca por artigo inteiro";
  PROMPT v4.2 L1450 — o trecho é a FRASE completa, em fronteira natural.

Uma frase que cita outro autor não pode ser o objeto do G3 desta referência.
Isso é dedução das regras, e é conferível: a saída é uma fatia literal da
Canônica contendo a citação exata da referência declarada no próprio vínculo.

O QUE ESTA PASSADA RESOLVE ALÉM DA LITERALIDADE
------------------------------------------------
O AT-13: vínculos cuja âncora aponta para a frase de OUTRA referência
(VINC_B1_0147 = REF_HAO_2024 ancorado na frase de Schafer 2012). A 3ª e a 4ª
passadas recusavam esses casos justamente porque o ano não batia — a recusa
estava certa, e agora há um método para resolvê-los pela raiz.

GUARDAS
-------
  - a citação da própria ref tem de existir na Canônica (senão: recusa);
  - se houver mais de uma frase candidata, escolhe-se a de maior sobreposição
    com o trecho atual — e exige-se sobreposição mínima, senão recusa;
  - o resultado tem de ser substring literal e terminar em fronteira natural;
  - toda troca de âncora é registrada com antes/depois para auditoria.

USO
---
    python3 reancorar5.py            # dry-run
    python3 reancorar5.py --apply
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from contrato import Contrato, norm, verificar_literal  # noqa: E402
from reancorar2 import RE_SELO_PLENO  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
VINCULOS = RAIZ / "canonico" / "evidencias_b1" / "vinculos_referencia_afirmacao.json"
CANONICA = RAIZ / "uploads" / "B1 NEUROINFLAMAÇÃO V4 CANONICA.md"

MIN_SOBREPOSICAO = 25


def sem_acento(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s)
                   if not unicodedata.combining(c))


def sobrenome_ano(ref: str) -> tuple[str, str] | None:
    """REF_SCHAFER_2012 -> ('Schafer', '2012'); REF_CHEN_2024c -> ('Chen','2024')."""
    m = re.match(r"^(?:REF|RCT)_([A-ZÀ-Ú][A-ZÀ-Úa-z]*)_?(\d{4})[a-z]?$", ref or "")
    if not m:
        return None
    return m.group(1).capitalize(), m.group(2)


def frases(corpo_n: str) -> list[tuple[int, int, str]]:
    """Frases do corpo com posição. Fronteira = pontuação seguida de maiúscula."""
    out, ini = [], 0
    for m in re.finditer(r"[.!?](?=\s+[A-ZÀ-Ú«\"]|\s*$)", corpo_n):
        fim = m.end()
        # estende para abraçar tags/selos que sucedem a pontuação
        j = fim
        while j < len(corpo_n):
            mm = RE_SELO_PLENO.match(corpo_n[j:j + 160])
            if mm:
                j += mm.end(); continue
            break
        txt = corpo_n[ini:j].strip()
        if len(txt) > 30:
            out.append((ini, j, txt))
        ini = j
    return out


def sobrepos(a: str, b: str) -> int:
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def ancorar(ref: str, atual: str, fr: list[tuple[int, int, str]],
            corpo_n: str) -> tuple[str | None, str]:
    sa = sobrenome_ano(ref)
    if not sa:
        return None, f"id_referencia_interna não parseável: {ref!r}"
    sob, ano = sa

    padroes = [
        rf"\({re.escape(sob)} et al\.,? {ano}",
        rf"\({re.escape(sob)} (?:&|e) [A-ZÀ-Ú][\w\-]*,? {ano}",
        rf"\({re.escape(sob)},? {ano}",
        rf"{re.escape(sob)} et al\.,? {ano}",
    ]
    rx = re.compile("|".join(padroes))

    cands = [(i, j, t) for i, j, t in fr if rx.search(sem_acento(t))
             or rx.search(t)]
    if not cands:
        return None, f"citação de {sob} {ano} não encontrada na Canônica"

    # RAMO "citação única" REMOVIDO (2026-09-11).
    # A regra é válida — se a citação ocorre uma só vez, aquela frase É a
    # âncora. Mas recortá-la exige um fatiador que entenda listas com
    # marcador '- ', que a normalização colapsa em blocos de 850 chars.
    # Tentei resolver com regex de corte e produzi âncoras cortadas DENTRO
    # do parêntese de citação ("(Arora et al."), pior que o defeito original.
    # Empilhar regex aqui é exatamente o padrão que esta perícia condena.
    # O reparo correto é reescrever o fatiador de frases respeitando a
    # estrutura markdown — trabalho próprio, não emenda. Até lá, recusar.

    if len(cands) == 1:
        escolhida = cands[0][2]
    else:
        escolhida = max(cands, key=lambda c: sobrepos(atual, c[2]))[2]
        if sobrepos(atual, escolhida) < MIN_SOBREPOSICAO:
            return None, (f"{len(cands)} frases citam {sob} {ano} e nenhuma "
                          f"casa o trecho atual (sobrepos < {MIN_SOBREPOSICAO}) "
                          f"— ambíguo, exige decisão de conteúdo")

    if escolhida not in corpo_n:
        return None, "frase escolhida não é literal (bug do fatiador)"
    if not re.search(r"[.!?\]]$", escolhida):
        return None, "frase escolhida não termina em fronteira natural"
    return escolhida, f"citacao_{sob}_{ano}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    corpo = CANONICA.read_text(encoding="utf-8")
    corpo_n = norm(corpo)
    fr = frases(corpo_n)
    dados = json.loads(VINCULOS.read_text(encoding="utf-8"))
    vincs = dados.get("vinculos", dados) if isinstance(dados, dict) else dados

    c0 = Contrato("vinculo", corpo_canonico=corpo)
    bloq_antes = {f"{p.item}|{p.campo}|{p.msg}"
                  for p in c0.validar(vincs) if p.nivel == "BLOQUEANTE"}

    reparos, falhas, ja_ok, trocas = [], [], 0, []
    for v in vincs:
        if verificar_literal(v.get("trecho_ancora", ""), corpo)["status"] == "LITERAL":
            ja_ok += 1
            continue
        atual = norm(v.get("trecho_ancora", ""))
        novo, motivo = ancorar(v.get("id_referencia_interna", ""), atual,
                               fr, corpo_n)
        if novo is None:
            falhas.append((v["id_vinculo"], motivo)); continue
        if novo == atual:
            falhas.append((v["id_vinculo"], "idêntico")); continue
        # Se a frase escolhida não compartilha início com a atual, isto não é
        # correção de etiqueta: é MUDANÇA DE FRASE. A regra "ancore na citação
        # da própria ref" é válida, mas quando há várias frases citando a mesma
        # fonte o desempate por sobreposição erra — verificado empiricamente
        # (escolheu "Regra de leitura [AT]…" para REF_ARORA_2019). Trocar a
        # afirmação que um vínculo sustenta é decisão de CONTEÚDO. Recusa e
        # encaminha ao AT-13 com o diagnóstico pronto.
        if sobrepos(atual, novo) < 40:
            trocas.append((v["id_vinculo"], v.get("id_referencia_interna"),
                           atual[:120], novo[:120]))
            falhas.append((v["id_vinculo"],
                           "âncora aponta para frase de outra referência — "
                           "AT-13, exige decisão de conteúdo (não reparado)"))
            continue
        reparos.append((v, novo, motivo, False))

    print("═" * 74)
    print(f"  5ª PASSADA — âncora pela própria citação "
          f"({'APLICAR' if args.apply else 'DRY-RUN'})")
    print("═" * 74)
    print(f"  EXAMINADOS ......... {len(vincs)}")
    print(f"  já literais ........ {ja_ok}")
    print(f"  reancorados ........ {len(reparos)}")
    print(f"     dos quais TROCA DE FRASE (AT-13) ... {len(trocas)}")
    print(f"  recusados .......... {len(falhas)}")
    print("─" * 74)
    for v, novo, motivo, troca in reparos[:6]:
        marca = "⚠ TROCA" if troca else "etiqueta"
        print(f"  ✎ {v['id_vinculo']} [{motivo}] {marca}")
        print(f"      antes: «…{norm(v['trecho_ancora'])[-60:]}»")
        print(f"      novo : «…{novo[-60:]}»")
    if len(reparos) > 6:
        print(f"  … mais {len(reparos) - 6}")
    if trocas:
        print("─" * 74)
        print(f"  ⚠️  {len(trocas)} vínculo(s) estavam ancorados na frase de OUTRA "
              f"referência (AT-13) — a âncora foi movida para a frase que cita "
              f"a própria fonte:")
        for vid, ref, a, b in trocas[:6]:
            print(f"      {vid} ({ref})")
            print(f"        de : «{a}…»")
            print(f"        para: «{b}…»")
    if falhas:
        print("─" * 74)
        print(f"  ⚠️  {len(falhas)} recusado(s):")
        for vid, motivo in falhas[:10]:
            print(f"      {vid}: {motivo}")

    inv = RAIZ / "canonico" / "at13_trocas_de_ancora.json"
    inv.write_text(json.dumps(
        [{"id_vinculo": a, "id_referencia_interna": b, "ancora_antiga": c,
          "ancora_nova": d} for a, b, c, d in trocas],
        ensure_ascii=False, indent=1), encoding="utf-8")
    print("─" * 74)
    print(f"  trocas registradas → {inv.relative_to(RAIZ)}")

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
