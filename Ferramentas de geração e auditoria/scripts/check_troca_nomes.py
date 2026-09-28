#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Checagem de TROCA DE NOME (rodada pós-auditoria externa Claude).
Para cada subseção com listra: cada citação (Sobrenome, Ano) do corpo daquela
subseção precisa bater com o 1o autor de ALGUM rótulo da listra da subseção.
Bate por (sobrenome, ano); aceita ano +/-0 se o rótulo do mesmo 1o autor existe.
Exclui: tabela-resumo final, blocos sem listra (cross-ref/escopo)."""
import json, re, glob, unicodedata, sys
from pathlib import Path
# helper LOCAL (ferramentas_geracao/_local_path.py): pasta do mecanismo resolvida
# relativa a este arquivo, sem caminho absoluto hard-coded.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # .../ferramentas_geracao/
import sys as _sys
MEC = _sys.argv[1] if len(_sys.argv)>1 else None
if MEC:
    from pathlib import Path as _P
    BASE=_P(MEC).resolve()
    import re as _re
    _cs=sorted([a for a in BASE.glob("*.md") if "CANONICA" in a.name.upper()],
               key=lambda a:int((_re.search(r"[Vv](\d+)",a.name) or [0])[1]) if _re.search(r"[Vv](\d+)",a.name) else 0)
    BIB=_cs[-1] if _cs else None
else:
    from _local_path import MEC_DIR as BASE, canonico_mais_novo as _cn
    BIB=_cn()
print(f"[versão ativa] {BIB.name if BIB else 'NENHUMA'} — {BASE.name}\n")
def sem_ac(s): return "".join(c for c in unicodedata.normalize("NFKD",s) if not unicodedata.combining(c))

reg={}
for f in glob.glob(str(BASE/"Evidencias/Bibliografia/*.json")):
    d=json.load(open(f,encoding="utf-8"))
    if not isinstance(d,list): continue
    for it in d:
        ids=it.get("ids_referencia_interna") or ([it["id_referencia_interna"]] if it.get("id_referencia_interna") else [])
        aut=it.get("autores") or ["?"]; p=aut[0]
        sob=(p.split(",")[0].strip() if "," in p else p.split()[0])
        a=re.search(r"(19|20)\d{2}",str(it.get("revista_ano","")))
        for full in ids:
            if full:
                rot=full[4:] if full.startswith("REF_") else full
                reg[rot]=(sem_ac(sob).lower(), a.group(0) if a else "????")

txt=BIB.read_text(encoding="utf-8")
# CORPO = antes da tabela-resumo / seção de referências finais
corte=txt.find("## TABELA DE EVIDÊNCIAS")
corpo=txt[:corte if corte>0 else len(txt)]
heads=[(m.start(),m.group(0)) for m in re.finditer(r"^### .*$",corpo,re.M)]
heads.append((len(corpo),""))
CITE=re.compile(r"\(([A-ZÀ-Ú][A-Za-zÀ-ÿ’'\-]+)(?:\s+(?:&|e)\s+[A-ZÀ-Ú][A-Za-zÀ-ÿ’'\-]+)?(?: et al\.?)?,?\s+((?:19|20)\d{2})[a-z]?\)")

problemas=[]; checadas=0; ok=0
for i in range(len(heads)-1):
    s,e=heads[i][0],heads[i+1][0]
    blk=corpo[s:e]; tit=heads[i][1][:58]
    labels=set()
    # considera SOMENTE linhas-listra que contêm rótulo[TAG] (MA/EC/OB/ML/AT);
    # ignora itálico de prosa que por acaso comece com *
    boas=[L for L in re.findall(r"^\*([^*\n]+)\*\s*$",blk,re.M)
          if re.search(r"\[(?:MA|EC|OB|ML|AT)\]",L)]
    for L in boas:
        for lab in re.findall(r"([A-Za-z0-9_À-￿]+)\[(?:MA|EC|OB|ML|AT)\]",L):
            labels.add(lab)
    if not labels:
        continue   # subseção sem listra (escopo/gap) -> não exige fecho
    # (sobrenome,ano)->rótulo  e  sobrenome->[(ano,rótulo)]
    por_chave={}; por_sob={}
    for lab in labels:
        if lab in reg:
            sob,ano=reg[lab]
            por_chave[(sob,ano)]=lab
            por_sob.setdefault(sob,[]).append((ano,lab))
    for m in CITE.finditer(blk):
        sob=sem_ac(m.group(1)).lower(); ano=m.group(2)
        checadas+=1
        if (sob,ano) in por_chave:
            ok+=1; continue
        if sob in por_sob:
            # mesmo 1o autor na listra, ano diferente -> pode ser data online/pub
            problemas.append((tit,sob,ano,"MESMO autor na listra, ano "+ano+" vs "+str(por_sob[sob])))
        else:
            # autor não está na listra -> TROCA DE NOME? ou cross-ref para outra seção
            onde=[l for l,(s2,a2) in reg.items() if s2==sob]
            problemas.append((tit,sob,ano,f"⚠ AUTOR NÃO ESTÁ NA LISTRA (possível troca). No banco: {onde[:3]}; listra: {sorted(labels)}"))

print(f"Citações checadas em subseções com listra: {checadas} | OK: {ok} | rever: {len(problemas)}\n")
for tit,sob,ano,msg in problemas:
    print(f"• ({sob} {ano}) — {tit}\n    {msg}\n")
