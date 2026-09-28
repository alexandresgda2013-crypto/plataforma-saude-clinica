#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
varredura_familia_hafizi.py — 2026-09-13 (rodada re-auditoria 2026-09-13 do Auditor-Mestre).

VARREDURA DA FAMÍLIA "HAFIZI" (causa-raiz AUD-038/V-05):
o ano usado no ID interno (REF_SOBRENOME_ANO) foi extraído do NOME do periódico
(padrão NLM: "Revista (Cidade, País : ANO_INICIO) (ANO_PUBLICACAO)") em vez do ano
de publicação. Este script percorre as 16 bibliotecas (B01–B16, pasta atuais/) e
registra, por ficha do Módulo 09 (01_pmids, 02_meta_analises, 03_ensaios_clinicos,
04_atualizacoes_literatura):

  (a) FICHA COM ANO NO NOME DA REVISTA — revista_ano contém ": AAAA" dentro de
      parênteses (marca o periódico com ano de início no nome; risco estrutural);
  (b) DIVERGÊNCIA ano-do-ID × ano-de-publicação — o ano final do ID não bate com o
      ano de publicação (último parêntese do revista_ano, ou o único ano presente);
  (c) NOMINAL família-Hafizi — divergência em que o ano-do-ID bate com o ANO DO NOME
      da revista (mesmo padrão do caso Hafizi: ID contaminado pelo nome do periódico).

Este script é READ-ONLY: gera apenas relatório. Correções seguem o rito documentado
(backups + trilha datada + nota no artefato + CHANGELOG antes/depois) — como na
trilha 17 da B1 (producao/17_rename_hafizi_2005_2007_2026-09-13.json).

Uso:  python3 varredura_familia_hafizi.py
Saída: relatório markdown em ../VARREDURA_FAMILIA_HAFIZI_B1_B16_2026-09-13.md
"""
import json, re, sys
from pathlib import Path

RAIZ = Path("/home/user/BIBLIOTECAS")
DATA = "2026-09-13"
SAIDA = RAIZ / "_documentos_serie" / f"VARREDURA_FAMILIA_HAFIZI_B1_B16_{DATA}.md"

RE_ANO_ID = re.compile(r"_(\d{4})[a-z]?$")
RE_ANO_NOME = re.compile(r":\s*(\d{4})\s*\)")
RE_PAREN = re.compile(r"\((\d{4})\)")

def registros_de(path: Path):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception:
        return []
    if isinstance(d, list):
        return [x for x in d if isinstance(x, dict)]
    return []

def ano_do_id(rid: str):
    m = RE_ANO_ID.search(rid or "")
    return int(m.group(1)) if m else None

RE_PAREN_NU = re.compile(r"\((\d{4})\)\s+(\d{4})")   # "Rev (2020) 2023" — título NLM de periódico novo + ano-pub solto
RE_ANO_SOLTO_FINAL = re.compile(r"(?<!\()\b(19|20)\d{2}\b\s*\.?\s*$")  # "Rev Abrev 2003" — geração antiga

def analisar_registro(r):
    rid = r.get("id_referencia_interna") or ""
    ra = r.get("revista_ano") or ""
    if not rid or not ra:
        return None
    ano_id = ano_do_id(rid)
    anos_nome = [int(a) for a in RE_ANO_NOME.findall(ra)]
    # 2026-09-13 rev.2 do parser: três formatos conviventes na série —
    #   (i)  "Rev (Local : ANO_NOME) (ANO_PUB)"     → pub = último parêntese (Hafizi: (2005) vs (2007))
    #   (ii) "Rev (ANO_NLM) ANO_PUB"                → título NLM de periódico novo; pub = ano solto (Du B05: "(2020) 2023")
    #   (iii)"Rev Abrev ANO_PUB"                    → geração antiga sem parênteses ("Mol Psychiatry 2017")
    m2 = RE_PAREN_NU.search(ra)
    if m2:
        anos_nome = anos_nome + [int(m2.group(1))]
        pub = int(m2.group(2))
    else:
        pub = None
        for m in RE_PAREN.finditer(ra):
            # parêntese precedido de ":" = ano do NOME NLM do periódico; senão = ano de publicação
            if ra[:m.start()].rstrip()[-1:] != ":":
                pub = int(m.group(1))
        if pub is None:
            ms = RE_ANO_SOLTO_FINAL.search(ra)
            if ms:
                pub = int(ms.group(0).strip().rstrip("."))
    return {"id": rid, "revista_ao": None, "revista_ano": ra, "ano_id": ano_id,
            "anos_nome": anos_nome, "ano_pub": pub,
            "pmid": r.get("pmid_oficial") or r.get("pmid") or ""}

def main():
    linhas = []
    tot = {"fichas": 0, "com_ano_nome": 0, "divergentes": 0, "nominal_hafizi": 0,
           "sem_ano_id": 0, "sem_ano_pub": 0}
    por_bib = []
    for b in sorted(RAIZ.glob("B??_*")):
        pasta = b / "atuais" / "Evidencias" / "Bibliografia"
        if not pasta.exists():
            continue
        casos_a, casos_b, casos_c, nf, sem_id, sem_pub = [], [], [], 0, 0, 0
        for arq in sorted(pasta.glob("*.json")):
            if arq.name.startswith("_") or ".bak" in arq.name:
                continue
            for r in registros_de(arq):
                a = analisar_registro(r)
                if not a:
                    continue
                nf += 1
                if a["ano_id"] is None:
                    sem_id += 1
                    continue
                if a["ano_pub"] is None:
                    sem_pub += 1
                if a["anos_nome"]:
                    casos_a.append((arq.name, a))
                if a["ano_pub"] is not None and a["ano_id"] != a["ano_pub"]:
                    casos_b.append((arq.name, a))
                    if a["ano_id"] in a["anos_nome"]:
                        casos_c.append((arq.name, a))
        tot["fichas"] += nf; tot["sem_ano_id"] += sem_id; tot["sem_ano_pub"] += sem_pub
        tot["com_ano_nome"] += len(casos_a); tot["divergentes"] += len(casos_b)
        tot["nominal_hafizi"] += len(casos_c)
        por_bib.append((b.name, nf, casos_a, casos_b, casos_c, sem_id, sem_pub))

    L = []
    L.append(f"# VARREDURA FAMÍLIA HAFIZI — B01–B16 ({DATA})")
    L.append("")
    L.append("Causa-raiz AUD-038/V-05: ano extraído do NOME NLM do periódico `Revista (Local : AAAA) (AAAA)`")
    L.append("contaminando o ano do ID interno. Script read-only; correções exigem rito (backup+trilha+nota+CHANGELOG).")
    L.append("")
    L.append("## Placar agregado")
    L.append("")
    L.append(f"- fichas analisadas (Módulo 09, 16 bibliotecas): **{tot['fichas']}**")
    L.append(f"- (a) com ano no nome da revista: **{tot['com_ano_nome']}**")
    L.append(f"- (b) ano-do-ID ≠ ano-de-publicação: **{tot['divergentes']}**")
    L.append(f"- (c) família-Hafizi nominal (ID bate com o ano do NOME): **{tot['nominal_hafizi']}**")
    L.append(f"- sem ano parseável no ID: {tot['sem_ano_id']} · sem ano de publicação detectável: {tot['sem_ano_pub']}")
    L.append("")
    for nome, nf, ca, cb, cc, si, sp in por_bib:
        L.append(f"## {nome} — {nf} fichas | (a) {len(ca)} · (b) {len(cb)} · (c) {len(cc)}"
                 + (f" · s/ano-ID {si} · s/ano-pub {sp}" if si or sp else ""))
        L.append("")
        for tag, casos in (("(c) FAMÍLIA-HAFIZI NOMINAL", cc), ("(b) divergentes", cb),
                           ("(a) ano-no-nome (só referência)", ca if not cc else [])):
            if not casos:
                continue
            if tag.startswith("(a)") and len(casos) > 12:
                L.append(f"- {tag}: {len(casos)} ocorrências (listadas as 12 primeiras; padrão benigno quando (b)=0)")
                mostra = casos[:12]
            else:
                mostra = casos
            for arq, a in mostra:
                L.append(f"  - `{a['id']}` ({arq}) id={a['ano_id']} pub={a['ano_pub']}"
                         + (f" nome={a['anos_nome']}" if a['anos_nome'] else "")
                         + (f" PMID {a['pmid']}" if a['pmid'] else "")
                         + f" — «{a['revista_ano'][:110]}»")
        L.append("")
    SAIDA.write_text("\n".join(L), encoding="utf-8")
    print(json.dumps(tot, ensure_ascii=False))
    print("relatório:", SAIDA)

if __name__ == "__main__":
    main()
