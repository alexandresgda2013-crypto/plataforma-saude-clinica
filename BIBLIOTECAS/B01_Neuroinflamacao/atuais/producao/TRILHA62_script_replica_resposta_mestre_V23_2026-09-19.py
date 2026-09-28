#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TRILHA 62 — Rodada 45 (2026-09-19): réplica da resposta do MESTRE à carta 18 + V2.3.
Veredicto-resumo: eco V2.3 exato · âncoras L-NT idênticas · N-4/herança uso confere · conflito do arquivo do
projeto: conclusão prática VERDADEIRA (com prova cruzada) MAS o marcador §2.82 prova que 309aa65f ≠ upload r24
exato → confissão de caracterização da casa + pedido dos bytes do arquivo do projeto."""
import hashlib, unicodedata, re, json, glob, os
RAIZ="/home/user"; S=RAIZ+"/BIBLIOTECAS/_documentos_serie/"
V22=S+"ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
V23=S+"CARTAS_V23_2026-09-19/CANDIDATA_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.3 - 19.09.26.md"
R24=RAIZ+"/uploads/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md"
LNT=S+"MESTRE_LNT_minuta1_recebido_2026-09-18/L-NT_CONTRATO_UNIDADES_NARRATIVAS_minuta1_294119b9_2026-09-18.md"
V7=RAIZ+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais/B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
MAN=RAIZ+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia/_manifesto_biblioteca.json"
VINC=RAIZ+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
checks=[]
def C(cid,tit,camada,escopo,cmd,med,esp,det=""):
    checks.append({"id":cid,"titulo":tit,"camada":camada,"escopo":escopo,"comando":cmd,"medido":med,"esperado":esp,"ok":med==esp,"detalhe":det})
def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(65536),b""): h.update(b)
    return h.hexdigest()
def T(p): return unicodedata.normalize("NFC", open(p,"rb").read().decode("utf-8"))
ci={os.path.basename(p):sha(p) for p in (V7,MAN,VINC)}
AG=["origem_conhecimento","a prosa deste documento prevalece sobre os desenhos","fora do cânone","O Motor busca ativamente","UNIFICADOS"]
def med(p):
    t=T(p); L=t.split("\r\n")
    return {a:(t.count(a)) for a in AG}, {"v1.1":(t.count("v1.1"),[i+1 for i,l in enumerate(L) if "v1.1" in l])}
m22,e22=med(V22); m23,e23=med(V23); m24,e24=med(R24)
C("M1","eco V2.3 do mestre: marcadores 3/1/1/1 · UNIFICADOS só L4 · v1.1 só L4","documental{NFC,CS}",V23,
  "count por agulha + linhas",
  {"V2.3":m23,"UNIFICADOS_L4":m23["UNIFICADOS"]==1,"v1.1":e23["v1.1"]},
  {"V2.3":{"origem_conhecimento":3,"a prosa deste documento prevalece sobre os desenhos":1,"fora do cânone":1,
           "O Motor busca ativamente":1,"UNIFICADOS":1},"UNIFICADOS_L4":True,"v1.1":(2,[4])},
  "confere com a alegação dele; precisão: 'v1.1' = 2 substrings (os 2 nomes) em 1 linha. "
  "C62-1 (régua): 1ª execução aninhou o dict v1.1 no empacotamento — corrigido; medida inalterada")
C("M2","V2.2 oficial contém os 4 marcadores (a 'V2.2 oficial contém origem_conhecimento' — correção dele ✔)",
  "documental{NFC,CS}",V22,"count", {k:v for k,v in m22.items()},
  {"origem_conhecimento":3,"a prosa deste documento prevalece sobre os desenhos":1,"fora do cânone":1,
   "O Motor busca ativamente":1,"UNIFICADOS":1},"")
# ÂNCORAS — implementação limpa
def sec_sha(p,sec):
    t=T(p); i=t.find(sec)
    j=re.search(r"\r\n# \d+\.", t[i+3:])
    trecho=t[i: i+3+j.start()] if j else t[i:]
    return hashlib.sha256(trecho.encode("utf-8")).hexdigest()[:12]
anc={sec:(sec_sha(V22,sec),sec_sha(V23,sec)) for sec in ["# 6.","# 7.","# 13.","# 14."]}
C("M3","ÂNCORAS L-NT: §§6/7/13/14 V2.2 ≡ V2.3 (sha por seção)","documental{NFC}","V2.2×V2.3",
  "extrair seção até próximo '# N.'; sha256[:12]",
  {k:(a==b,a) for k,(a,b) in anc.items()}, {k:(True,v[0]) for k,v in anc.items()},
  "afirmação do mestre verificada: idênticas")
C("M4","CONFLITO do arquivo do projeto (a peça que muda a caracterização) — teste cruzado no upload r24 que TEMOS",
  "documental{NFC,CS}",R24,"count nos bytes do r24",
  {"origem_conhecimento":m24["origem_conhecimento"],"prosa_prevalece":m24["a prosa deste documento prevalece sobre os desenhos"],
   "fora_do_canone":m24["fora do cânone"],"motor_busca_ativamente_L82":m24["O Motor busca ativamente"],"UNIFICADOS_L66":m24["UNIFICADOS"]},
  {"origem_conhecimento":0,"prosa_prevalece":0,"fora_do_canone":0,"motor_busca_ativamente_L82":1,"UNIFICADOS_L66":1},
  "r24: 3 primeiros = 0 (bate com o 0 do projeto) MAS 'O Motor busca ativamente' = 1× na L82 do r24 × 0 no projeto (declarado pelo mestre) "
  "→ 309aa65f NÃO é byte-idêntico ao upload r24. CONFISSÃO da casa: a caracterização 'r24 rotulado' estava imprecisa; "
  "verdade sustentada: 309aa65f é SUPERSEDED e NÃO é a V2.2 oficial. Identidade exata: só com os bytes do projeto (pedido ao operador)")
t=T(LNT)
C("M5","N-4 / herança uso na minuta L-NT (alegação 'coberta no L-NT, regra N-4')","documental{NFC,casefold}",LNT,
  "grep 'N-4' e 'uso` herdado do kit'",
  {"N-4":t.count("N-4")>0,"uso herdado do kit":"`uso` herdado do kit" in t,"NT-05 referencia N-4":"NT-05 | `uso = clinico` com origem pré-clínica (N-4)" in t},
  {"N-4":True,"uso herdado do kit":True,"NT-05 referencia N-4":True},"")
hits=glob.glob(RAIZ+"/BIBLIOTECAS/**/*DELIBERACAO*",recursive=True)+glob.glob(RAIZ+"/uploads/*DELIBERACAO*")
C("M6","DELIBERACAO_FLUXO_CLAIM_CLINICO_2026-09-18.md na base?","bytes",RAIZ,"glob",[os.path.basename(h) for h in hits],[],
  "confirmado: não temos; posição B dele coerente com consolidado ff8daf6f (r32) e com a posição da casa — pedir os bytes verbatim")
ci2={os.path.basename(p):sha(p) for p in (V7,MAN,VINC)}
C("CI0","0 ciência","bytes","acervo","sha início==fim",ci==ci2,True,"")
res={"trilha":62,"rodada":45,"data":"2026-09-19",
 "tema":"réplica resposta do MESTRE à carta 18 (V2.3) — 6 checks + confissão de caracterização 309aa65f",
 "checks":[c for c in checks],"verdes":sum(c["ok"] for c in checks),"total":len(checks),
 "veredito":"Mestre: eco V2.3 exato · âncoras idênticas · N-4/herança confere · correções dele honradas. "
 "Conflito: conclusão prática (projeto ≠ V2.2 oficial; base sem endurecimento de proveniência) VERDADEIRA e agora provada dos dois lados; "
 "MAS 'O Motor busca ativamente' (1× r24 × 0 projeto) → 309aa65f ≠ r24 exato: confissão de precisão da casa, pedido dos bytes do arquivo do projeto."}
out=RAIZ+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA62_replica_resposta_mestre_V23_2026-09-19.json"
json.dump(res,open(out,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print(f"{res['verdes']}/{res['total']} verdes")
for c in checks:
    if not c["ok"]: print("  FALHOU:",c["id"],str(c["medido"])[:250])
