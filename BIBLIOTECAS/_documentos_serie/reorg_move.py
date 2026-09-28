#!/usr/bin/env python3
# REORG 2026-09-10 — B01..B16: cria atuais/ e antigos/ e move material
# Unidade de portão (canônica+Evidencias+Auditoria) move-se JUNTA para atuais/.
# Registro prévio: BIBLIOTECAS/CHANGELOG_GERAL.md (entrada 2026-09-10) — IMPL-AT-10.
import os, shutil, sys

BASE = "/home/user/BIBLIOTECAS"
LOG = []

def mv(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.move(src, dst)
    LOG.append(f"{src.replace(BASE+'/','')}  ->  {dst.replace(BASE+'/','')}")

libs = sorted(d for d in os.listdir(BASE) if d.startswith("B") and os.path.isdir(os.path.join(BASE, d)))
report = []
for lib in libs:
    p = os.path.join(BASE, lib)
    os.chdir(p)  # facilita paths relativos
    at, an = os.path.join(p, "atuais"), os.path.join(p, "antigos")
    if os.path.isdir(at):
        report.append(f"{lib}: JÁ REORGANIZADO — pulo"); continue
    os.makedirs(at); os.makedirs(an)

    # 0) antigos/: conteúdo de producao/historico (se existir)
    hist = os.path.join(p, "producao", "historico")
    if os.path.isdir(hist):
        mv(hist, os.path.join(an, "historico"))

    # 1) unidade de portão + producao
    md = [f for f in os.listdir(p) if f.endswith(".md") and "CANONICA" in f.upper() and not f.startswith("~")]
    assert len(md) >= 1, f"{lib}: canônica não achada na raiz"
    md.sort(key=lambda f: int(__import__("re").search(r"[Vv](\d+)", f).group(1)))
    can = md[-1]
    if len(md) > 1:  # versões antigas soltas na raiz -> antigos
        for old in md[:-1]:
            mv(os.path.join(p, old), os.path.join(an, old))
    mv(os.path.join(p, can), os.path.join(at, can))
    for d in os.listdir(p):
        fp = os.path.join(p, d)
        if d.startswith("Evidencias") or d.startswith("Auditoria_"):
            mv(fp, os.path.join(at, d))
    if os.path.isdir(os.path.join(p, "producao")):
        mv(os.path.join(p, "producao"), os.path.join(at, "producao"))

    # 2) demais soltos na raiz: scripts/artefatos da versão vigente -> atuais/
    for f in sorted(os.listdir(p)):
        fp = os.path.join(p, f)
        if os.path.isfile(fp) and f not in ("README_ORGANIZACAO.md",) and not f.startswith("."):
            mv(fp, os.path.join(at, f))

    # 3) verificação estrutural pós-mudança
    assert os.path.isfile(os.path.join(at, can))
    assert os.path.isdir(os.path.join(at, "Evidencias"))
    assert [d for d in os.listdir(at) if d.startswith("Auditoria_")]
    assert os.path.isdir(os.path.join(at, "producao"))
    n_at = sum(len(fs) for _, _, fs in os.walk(at)); n_an = sum(len(fs) for _, _, fs in os.walk(an))
    report.append(f"{lib}: atuais={n_at} arqs | antigos={n_an} arqs")

with open(os.path.join(BASE, "reorg_move_log_2026-09-10.txt"), "w") as f:
    f.write("\n".join(LOG))
print("\n".join(report))
print("\nlog de movimentos:", os.path.join(BASE, "reorg_move_log_2026-09-10.txt"), f"({len(LOG)} movimentos)")
