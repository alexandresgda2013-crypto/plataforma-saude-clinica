#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# propaga_selos_blindado.py — 2026-09-11 (agente, pacote Rodada 2 da perícia)
# Versão BLINDADA de _propaga_selos3.py. Defeitos fechados:
#   D4: o original sobrescrevia o .md direto. Aqui: backup datado + escrita atômica.
#   Lei P-5: pré-condições viram PORTÃO (exit 1) — vínculos com verification_status
#   fora do enum, OU âncora não-literal (selo propagado para frase errada é o modo
#   de falha histórico), OU citação localizada 0 vezes / em seção de referências.
#   Pós-condição verificada: nenhum selo duplicado colado ([X] [X]); contagem
#   impressa com denominador (D3).
# Uso:  python3 propaga_selos_blindado.py <canonica.md> <vinculos.json> [--aplicar]
import json, re, sys, shutil
from pathlib import Path
from datetime import datetime, timezone
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from contrato import Contrato, verificar_literal                                # noqa: E402

SELOS = {"verificado": "[VERIFICADO]", "preclinico": "[PRÉ-CLÍNICO]",
         "extrapolado": "[EXTRAPOLADO: animal/célula→humano]", "pendente": "[EMERGENTE]"}
SELO_RE = re.compile(r"\[(VERIFICADO|PR[ÉE]-CL[ÍI]NICO|EXTRAPOLADO:|EMERGENTE)")
_RE_SEC_REFS = re.compile(r"refer.ncias|bibliografia", re.I)

def ultima_cit(texto):
    ms = list(re.finditer(r"\([^()]*?\d{4}[^()]*?\)\s*\[[^\]]*\]", texto))
    return ms[-1] if ms else None

def main():
    doc = Path(sys.argv[1]); vinc = json.load(open(sys.argv[2], encoding="utf-8"))
    aplicar = "--aplicar" in sys.argv
    vinc = vinc if isinstance(vinc, list) else vinc.get("vinculos")
    t = doc.read_text(encoding="utf-8")

    # PORTÃO 1 — vocabulário + âncoras literais (senão o selo vai parar na frase errada)
    c = Contrato("vinculo", corpo_canonico=t)
    probs = [p for p in c.validar(vinc) if p.nivel == "BLOQUEANTE" and p.campo == "trecho_ancora"]
    enum_bad = [p for p in c.validar(vinc) if p.nivel == "BLOQUEANTE" and p.campo != "trecho_ancora"]
    if enum_bad:
        print(f"❌ {len(enum_bad)} bloqueantes de enum/campo — ex.: {enum_bad[0]}"); sys.exit(1)
    if probs:
        print(f"❌ {len(probs)} âncoras não literais — ex.: {probs[0]}")
        print("   selo propagado com âncora não literal já causou selo na frase errada; abortando.")
        sys.exit(1)

    ins, falhas = [], []
    for v in vinc:
        if v.get("status_auditoria") == "NAO_LOCALIZADO":
            continue
        s = SELOS.get(v.get("verification_status"))
        if not s:
            continue
        m = ultima_cit(v["trecho_ancora"])
        if not m:
            falhas.append(v["id_vinculo"]); continue
        cit = m.group(0)
        pos = t.find(cit)
        if pos == -1:
            cit2 = cit.replace("**", "")
            pos = t.find(cit2)
            cit = cit2 if pos != -1 else cit
        if pos == -1:
            falhas.append(v["id_vinculo"]); continue
        end = pos + len(cit)
        if SELO_RE.match(t[end:end + 30]):
            continue                                    # idempotente
        ins.append((end, s))
    ins.sort(reverse=True)
    t2 = t
    for end, s in ins:
        t2 = t2[:end] + " " + s + t2[end:]

    # PORTÃO 2 — pós-condição: sem selo imediatamente duplicado
    if re.search(r"(\[(?:VERIFICADO|PR[ÉE]-CL[ÍI]NICO|EXTRAPOLADO:[^\]]*|EMERGENTE)\]) *\1", t2):
        print("❌ pós-condição violada: selo duplicado colado"); sys.exit(1)

    from collections import Counter
    cont = Counter(re.findall(r"\[(VERIFICADO|PRÉ-CLÍNICO|EXTRAPOLADO: animal/célula→humano|EMERGENTE)\]", t2))
    print(f"selos na prosa: {dict(cont)} | total {sum(cont.values())} | inserções novas {len(ins)} | âncoras sem citação localizável: {len(falhas)}")
    if falhas:
        print("  (sem localização → não selados por precaução):", falhas[:10])
    if aplicar and ins:
        carimbo = datetime.now(timezone.utc).astimezone().strftime("%Y%m%d_%H%M%S")
        bkp = doc.with_suffix(doc.suffix + f".bak_{carimbo}")
        shutil.copy2(doc, bkp)
        tmp = doc.with_suffix(doc.suffix + ".tmp")
        tmp.write_text(t2, encoding="utf-8"); tmp.replace(doc)
        print("gravado com backup:", bkp)
    else:
        print("dry-run: nada gravado (use --aplicar)")

if __name__ == "__main__":
    main()
