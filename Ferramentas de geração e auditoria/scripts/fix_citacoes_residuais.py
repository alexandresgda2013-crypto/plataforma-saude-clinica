#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Passada garantida: resolve QUALQUER parêntese (...,ANO) que não seja autor-ano
contra os rótulos da listra da própria subseção. Não inventa: sem casamento -> marca [PENDENTE_VERIF]."""
import json, re, glob, unicodedata
from pathlib import Path

BASE = Path("/home/user/pipeline_auditoria_conteudo/BIBLIOTECAS/B01_Neuroinflamacao")
P = BASE / "Biblioteca_B1_NEUROINFLAMACAO_CANONICA.md"

def sem_ac(s): return "".join(c for c in unicodedata.normalize("NFKD",s) if not unicodedata.combining(c))
def toks(s):
    s=sem_ac(s.lower()); s=re.sub(r"[^a-z0-9]+"," ",s)
    return set(s.split())-{"and","the","of","in","a","via"}

# registros por rótulo
regs={}
for f in glob.glob(str(BASE/"Evidencias/Bibliografia/*.json")):
    data=json.load(open(f,encoding="utf-8"))
    if not isinstance(data,list): continue
    for it in data:
        if not isinstance(it,dict): continue
        ids=it.get("ids_referencia_interna") or ([it["id_referencia_interna"]] if it.get("id_referencia_interna") else [])
        aut=it.get("autores") or ["?"]
        p=aut[0]; sob=p.split(",")[0].strip() if "," in p else p.split()[0]
        for full in ids:
            if not full: continue
            rot=full[4:] if full.startswith("REF_") else full
            ano=re.search(r"(19|20)\d{2}",str(it.get("revista_ano","")))
            regs[rot]=dict(tok=toks(it.get("titulo_artigo","")), sob=sob,
                           ano=ano.group(0) if ano else "????")

txt=P.read_text(encoding="utf-8")
# subseções
heads=[(m.start(),m.end()) for m in re.finditer(r"^### .*$",txt,re.M)]
heads.append((len(txt),len(txt)))
secoes=[]
for i in range(len(heads)-1):
    s,e=heads[i][0],heads[i+1][0]
    blk=txt[s:e]
    labs=set()
    for L in re.findall(r"^\*([^*]+)\*\s*$",blk,re.M):
        for lab in re.findall(r"([A-Za-z0-9_À-￿]+)\[(?:MA|EC|OB|ML|AT)\]",L):
            labs.add(lab)
    secoes.append((s,e,labs))
def secao(pos):
    for s,e,l in secoes:
        if s<=pos<e: return l
    return set()

# parêntese com ano
PAREN=re.compile(r"\(([^()]{3,130}?,\s*((?:19|20)\d{2})[a-z]?)\)(\s*\[(?:MA|EC|OB|ML|AT)[^\]]*\])?")
AUTOR=re.compile(r"^[A-ZÀ-Ú][A-Za-zÀ-ÿ’'\-.]+(?:\s+(?:&|e)\s+[A-ZÀ-Ú][A-Za-zÀ-ÿ’'\-.]+| et al\.?)?,?$")

repl=[]; pend=[]
for m in PAREN.finditer(txt):
    inner=m.group(1); ano=m.group(2)
    cabeça=inner.rsplit(",",1)[0].strip()
    # já é autor-ano? (1-3 palavras capitalizadas, sem palavra-título minúscula inglesa)
    palavras=cabeça.split()
    he_autor = bool(AUTOR.match(cabeça)) and len(palavras)<=4
    # nota explicativa em português?
    eh_pt = len(re.findall(r"\b(revisão|revisao|camundongo|humano|reduz|prediz|melhor|resolução|resolucao|sofrimento|psicológico|sintomas|hipocampal|células|celular|sobre|entre|assim|como|ver|derivada|frio|astrócitos|astrocitos|glicação|avançada|produtos|finais|questão|humor|literatura|referência|verificar|metilação|genes|fatores|modelo|limitando|composto|natural|alivia)\b",inner,re.I))>=2
    if he_autor or eh_pt:
        continue
    # é título (em qualquer língua) a resolver
    ct=toks(cabeça); labs=secao(m.start())
    best=None;bs=-1
    for rot in labs:
        r=regs.get(rot)
        if not r: continue
        sc=len(ct & r["tok"])/max(1,len(ct | r["tok"]))
        if r["ano"]==ano: sc+=0.3
        if sc>bs: bs=sc;best=rot
    tag=m.group(3) or ""
    if best and bs>=0.30:
        r=regs[best]
        novo=f"({r['sob']} et al., {r['ano']}){tag}"
        repl.append((m.start(),m.end(),novo,f"{best} ({bs:.2f})"))
    else:
        novo=f"({cabeça} — referência a verificar na Rodada 4){tag} [PENDENTE_VERIF]"
        repl.append((m.start(),m.end(),novo,f"PENDENTE bs={bs:.2f} labs={sorted(labs)}"))
        pend.append(cabeça[:60])

for s,e,novo,info in sorted(repl,reverse=True):
    txt=txt[:s]+novo+txt[e:]
P.write_text(txt,encoding="utf-8")
print("resolvidos:",len(repl))
for s,e,novo,info in sorted(repl,key=lambda x:x[0]):
    print("  ",info)
print("PENDENTES:",pend)
