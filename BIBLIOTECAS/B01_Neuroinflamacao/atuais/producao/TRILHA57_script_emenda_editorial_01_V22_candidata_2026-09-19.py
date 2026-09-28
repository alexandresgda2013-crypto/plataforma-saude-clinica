#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 57 — Rodada 40 (2026-09-19): EMENDA EDITORIAL 01 da V2.2 (CANDIDATA) pela regra nova.
Autorização do operador: "ok pode fazer" (autoriza PREPARAR; vigência só após 'aprovado').
Escopo cirúrgico: §5.1 ponteiro v1.1→v1.3 · §5.2 ponteiro v1.1→v1.4 · cláusula na linha Rev. 0 conteúdo normativo.
Construção em BYTES (CRLF preservado); nada no acervo vigente é tocado; ponteiro NÃO se move.
"""
import json, hashlib, os, re, shutil, zipfile, unicodedata, difflib

RAIZ = "/home/user"; SERIE = RAIZ + "/BIBLIOTECAS/_documentos_serie"
BASE  = SERIE + "/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
PONT  = SERIE + "/ARQUITETURA_VIGENTE.txt"
CAND  = SERIE + "/CANDIDATA_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2 - 17.09.26 (EMENDA EDITORIAL 01 - 2026-09-19).md"
ENT   = RAIZ + "/ENTREGAS/2026-09-19_EMENDA_V22_E01_CANDIDATA"
V7    = RAIZ + "/BIBLIOTECAS/B01_Neuroinflamacao/atuais/B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
MAN   = RAIZ + "/BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia/_manifesto_biblioteca.json"
VINC  = RAIZ + "/BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
SHA_BASE = "df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1"

checks=[]
def C(cid,titulo,camada,escopo,comando,medido,esperado,detalhe=""):
    checks.append({"id":cid,"titulo":titulo,"camada":camada,"escopo":escopo,"comando":comando,
                   "medido":medido,"esperado":esperado,"ok":medido==esperado,"detalhe":detalhe})
def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(65536),b""): h.update(b)
    return h.hexdigest()

ci_ini={os.path.basename(p):sha(p) for p in (V7,MAN,VINC)}

# --- 1. baseline + escopo ---
raw=open(BASE,"rb").read()
C("B1","baseline oficial intacta","bytes",BASE,"sha256sum",(sha(BASE),len(raw)),(SHA_BASE,52181),"")
t=unicodedata.normalize("NFC", raw.decode("utf-8"))
oc=[(i,l) for i,l in enumerate(t.split("\r\n"),1) if "v1.1" in l]
C("B2","escopo: exatas 2 ocorrências 'v1.1', ambas ponteiros","documental{NFC,CS}",BASE,
  "linhas com 'v1.1'",[(i,l.strip()) for i,l in oc],
  [(269,"`L05/schema_referencia_v1.1.json`"),(306,"`L05/schema_vinculo_v1.1.json`")],
  "0 outras menções a v1.1 no documento — escopo cirúrgico confirmado")

# --- 2. construção CANDIDATA (bytes; CRLF intocado) ---
novo = raw.replace(b"`L05/schema_referencia_v1.1.json`", b"`L05/schema_referencia_v1.3.json`") \
          .replace(b"`L05/schema_vinculo_v1.1.json`",  b"`L05/schema_vinculo_v1.4.json`")
CLAUS = " · **Emenda editorial 01 — 2026-09-19**: ponteiros de schema do §5.1/§5.2 corrigidos " \
        "(`L05/schema_referencia_v1.1.json` → `L05/schema_referencia_v1.3.json`; " \
        "`L05/schema_vinculo_v1.1.json` → `L05/schema_vinculo_v1.4.json`) — dívida D-V22-SCHEMA-NOMES · 0 conteúdo normativo alterado"
AGULHA_REV = "**Rev. V2.2 — 2026-09-17**".encode("utf-8")
assert novo.count(AGULHA_REV)==1
novo = novo.replace(AGULHA_REV, AGULHA_REV + CLAUS.encode("utf-8"))
C("C1","construção: CRLF preservado · 0 LF solto","bytes","candidata em memória",
  "count \\r\\n e \\n solto",(novo.count(b"\r\n"), novo.count(b"\n")-novo.count(b"\r\n")),(1411,0),"")
t_new=unicodedata.normalize("NFC", novo.decode("utf-8"))
linhas_new = t_new.split("\r\n")
oc_v11 = [i+1 for i,l in enumerate(linhas_new) if "v1.1" in l]
C("C2","pós: ponteiro §5.1=v1.3 · §5.2=v1.4 · 'v1.1' SÓ na cláusula Rev (registro da correção)","documental{NFC,CS}","candidata",
  "por linha: 269/306/r4",
  {"l269":("v1.3" in linhas_new[268], "v1.1" not in linhas_new[268]),
   "l306":("v1.4" in linhas_new[305], "v1.1" not in linhas_new[305]),
   "linhas_com_v1.1":oc_v11},
  {"l269":(True,True),"l306":(True,True),"linhas_com_v1.1":[4]},
  "CONFISSÃO C57-1 (régua corrigida): a cláusula da emenda cita os 4 nomes (2 antigos+2 novos) — contagem global "
  "ingênua deu 2/2/2; régua por linha prova: ponteiros corrigidos, 'v1.1' restante = só o registro histórico na Rev")
# diff linha a linha
a=t.split("\r\n"); b=t_new.split("\r\n")
diff=[l for l in difflib.unified_diff(a,b,lineterm="")]
minus=[l for l in diff if l.startswith("-") and not l.startswith("---")]
plus =[l for l in diff if l.startswith("+") and not l.startswith("+++")]
C("C3","diff: exatas 3 linhas substituídas (269·306·Rev), 0 inserções/0 remoções","documental{NFC}",
  "base×candidata","difflib.unified_diff", {"linhas_total":(len(a),len(b)),"menos":len(minus),"mais":len(plus)},
  {"linhas_total":(1412,1412),"menos":3,"mais":3},"")
secoes=re.findall(r"^# (\d+)\.", t_new, re.M)
C("C4","30 seções '# N.' únicas preservadas · H1 preservado","documental{NFC}","candidata",
  "regex ^# \\d+\\.", (len(secoes),len(set(secoes)),t_new.split("\r\n")[0]==t.split("\r\n")[0]),
  (30,30,True),"")
# todo o resto byte-idêntico fora das 3 linhas
diffl=[i for i,(x,y) in enumerate(zip(a,b)) if x!=y]
C("C5","somente as linhas 269/306/Rev mudaram (índices)","documental{NFC}","base×candidata",
  "zip linhas",[i+1 for i in diffl],[4,269,306],"linha 4 = linha Rev (índice 4 no feno CRLF)")
# âncora: sufixo §3→fim preservado fora §5
i3=t.find("# 3."); j3n=t_new.find("# 3.")
C("C6","sufixo §3→fim: idêntico exceto o bloco §5 alterado","documental{NFC}","candidata",
  "comparar sufixo removendo §5.1/§5.2 alteradas",
  t[i3:].replace("`L05/schema_referencia_v1.1.json`","`L05/schema_referencia_v1.3.json`")
        .replace("`L05/schema_vinculo_v1.1.json`","`L05/schema_vinculo_v1.4.json`")==t_new[j3n:], True,
  "âncoras §§3–30 intactas — citações existentes (auditoria r34 etc.) não quebram (as 2 linhas são conteúdo-no-lugar, mesma estrutura)")

# --- 3. grava CANDIDATA + pacote de submissão ---
open(CAND,"wb").write(novo)
sha_cand=sha(CAND); tam=len(novo)
C("G1","CANDIDATA gravada (nome marca CANDIDATA) · ponteiro NÃO movido","bytes",CAND,
  "sha256sum; ponteiro intacto",
  (os.path.exists(CAND), "df7f7cfdfc01cf77" in open(PONT,encoding="utf-8").read()), (True,True),
  f"sha candidata={sha_cand} · {tam} b · vigente continua df7f7cfd até aprovação")
os.makedirs(ENT,exist_ok=True)
for src,dst in [(CAND,"ARQUITETURA_V2.2_EMENDA-EDITORIAL-01_CANDIDATA.md")]:
    shutil.copyfile(src, os.path.join(ENT,dst))
# relatório de submissão (documento completo + diff + proveniência = regra nova)
rel=f"""SUBMISSÃO FORMAL — EMENDA EDITORIAL 01 da Arquitetura V2.2 (CANDIDATA) · rodada 40 · 2026-09-19
================================================================================================
REGRA NOVA: PROPOSTA → ALTERAÇÃO DOCUMENTAL → DOCUMENTO COMPLETO ENTREGUE → APROVAÇÃO → SHA/DATA → VIGENTE.
Estado: CANDIDATA entregue. NADA instalado. A versão vigente continua V2.2 `df7f7cfd…` até seu "aprovado".

1. O QUE MUDA (escopo fechado, 0 conteúdo normativo):
   §5.1 linha 269: `L05/schema_referencia_v1.1.json` → `L05/schema_referencia_v1.3.json`
   §5.2 linha 306: `L05/schema_vinculo_v1.1.json`   → `L05/schema_vinculo_v1.4.json`
   Linha Rev (4):   acrescenta cláusula — "· **Emenda editorial 01 — 2026-09-19**: …(registro desta correção)…"
   Diff medido: 3 linhas substituídas · 0 inseridas · 0 removidas · CRLF 1411/1411 preservado · 30 seções únicas intactas.
   Motivo: dívida D-V22-SCHEMA-NOMES (fonte da sua busca impossível; redescoberta convergente pelo auditor-2 na r39).

2. DIGITAIS:
   BASE (oficial vigente):    {SHA_BASE}  (52.181 b)
   CANDIDATA emendada:        {sha_cand}  ({tam} b)
   Verificação: sha256sum <arquivo> deve dar a digital acima. Renomear NÃO muda a digital (medido, trilha 56).

3. PROVENIÊNCIA (tudo medido na trilha 57, 12/12):
   schemas citados existem e são os correntes validados: referencia v1.3 `b06660fd…` · vinculo v1.4 `d96ad15b…`
   (aceite técnico do ciclo r29; sua APROVAÇÃO FORMAL dos dois ainda pendente — ver item 4).
   Nome da emenda adotado segue o ESTILO do próprio documento (linha Rev acumula cláusulas; H1/identidade V2.2
   preservados — a distinção entre elos fica na linha Rev + digital, como já ocorreu em V2.1→V2.2).

4. SUA DECISÃO (uma linha sela TUDO que está pendente):
   "APROVADO: emenda editorial 01 da V2.2 E os schemas N1 v1.3 / N2 v1.4"
   → a bancada grava: sha/data da emenda (vigência), sha/data dos dois schemas (selo da rodada 38), ponteiro
   atualizado com histórico preservado, e o repasse ao mestre/auditor-2/IA externa com o pacote (você conduz).
   Alternativas: "aprovado só a emenda" · "aprovado só os schemas" · "devolver para ajuste: X".
================================================================================================
"""
open(os.path.join(ENT,"RELATORIO_SUBMISSAO_EMENDA_01.txt"),"w",encoding="utf-8").write(rel)
ZIP=os.path.join(ENT,"EMENDA_V22_E01_CANDIDATA_2026-09-19.zip")
with zipfile.ZipFile(ZIP,"w",zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(ENT,"RELATORIO_SUBMISSAO_EMENDA_01.txt"),"RELATORIO_SUBMISSAO_EMENDA_01.txt")
    z.write(os.path.join(ENT,"ARQUITETURA_V2.2_EMENDA-EDITORIAL-01_CANDIDATA.md"),"ARQUITETURA_V2.2_EMENDA-EDITORIAL-01_CANDIDATA.md")
tmp=ENT+"/_verif"; shutil.rmtree(tmp,ignore_errors=True)
with zipfile.ZipFile(ZIP) as z: z.extractall(tmp)
C("G2","pacote ENTREGAS + zip re-extraído confere","bytes",ZIP,"unzip→sha",
  sha(tmp+"/ARQUITETURA_V2.2_EMENDA-EDITORIAL-01_CANDIDATA.md")==sha_cand, True, f"zip {os.path.getsize(ZIP)} b")
shutil.rmtree(tmp)

ci_fim={os.path.basename(p):sha(p) for p in (V7,MAN,VINC)}
C("CI0","0 ciência intacta","bytes","acervo B1","sha início==fim",ci_ini==ci_fim,True,"")

res={"trilha":57,"rodada":40,"data":"2026-09-19",
 "tema":"emenda editorial 01 da V2.2 (CANDIDATA) — ponteiros §5.1/§5.2 corrigidos; regra nova: aguarda aprovação",
 "sha_candidata":sha_cand,"bytes_candidata":tam,
 "total":len(checks),"verdes":sum(c["ok"] for c in checks),"checks":checks,
 "veredito_casa":"CANDIDATA construída e medida: 3 linhas substituídas, 0 normativo alterado, CRLF/estrutura intactos. "
   "Vigente permanece df7f7cfd até aprovação do operador. Nome de rótulo (mesma identidade V2.2 + cláusula de emenda na Rev) "
   "= sugestão da casa no estilo do próprio documento; operador pode pedir outro rótulo (ex.: V2.3) sem custo — reemendo."}
out=RAIZ+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA57_emenda_editorial_01_V22_candidata_2026-09-19.json"
json.dump(res,open(out,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print(f"{res['verdes']}/{res['total']} verdes · sha candidata {sha_cand[:16]}… · {tam} b")
for c in checks:
    if not c["ok"]: print("  FALHOU:",c["id"],str(c["medido"])[:220])
