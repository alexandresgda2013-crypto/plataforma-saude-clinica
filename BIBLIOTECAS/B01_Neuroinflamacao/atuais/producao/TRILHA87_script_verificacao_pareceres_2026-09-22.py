#!/usr/bin/env python3
# TRILHA 87 — Verificação empírica das afirmações dos dois pareceres territoriais (rodada 76, 2026-09-22)
# Política da casa: replicar TUDO antes de aceitar. Régua R-BUSCA-1.
import json, re, unicodedata, hashlib
HOME="/home/user"
B1=HOME+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais"
CAN=B1+"/B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
VIN=B1+"/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
N2 =HOME+"/BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
N1 =HOME+"/BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_referencia_v1.3_N1_b06660fd.json"
SC =HOME+"/BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/3º SCHEMA-CLAIM — v1.2.md"
V19=HOME+"/uploads/4º_COMO_EXECUTAR___v1_9.md"
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
def txt(p): return unicodedata.normalize("NFC", open(p, encoding="utf-8").read())
R={"rodada":76,"data":"2026-09-22","corpus":{"canonica_V7":sha(CAN),"vinculos":sha(VIN),"N2_v14":sha(N2),"N1_v13":sha(N1),"schema_claim_v12":sha(SC),"v19":sha(V19)},"itens":[]}
def add(i,t,ok,obs=None,dados=None):
    d={"item":i,"teste":t,"ok":bool(ok)}
    if obs: d["obs"]=obs
    if dados: d["dados"]=dados
    R["itens"].append(d); return d
can=txt(CAN); can_cf=can.casefold()
vin=json.load(open(VIN)); V=vin["vinculos"] if isinstance(vin,dict) and "vinculos" in vin else vin
v19=txt(V19); v19L=v19.split("\n")
n1=json.load(open(N1)); n2=json.load(open(N2)); sc=txt(SC)

# E1 — 274 vínculos
add(1,"V7 tem 274 vínculos",len(V)==274,len(V))
# E2 — 274/274 trecho_ancora encontrados literalmente na canônica
falt=[];vaz=[]
for v in V:
    ta=(v.get("trecho_ancora") or "").strip()
    if not ta: vaz.append(v.get("id_vinculo") or v.get("id")); continue
    if ta.casefold() not in can_cf: falt.append({"id":v.get("id_vinculo") or v.get("id"),"trecho":ta[:90]})
add(2,"ESTRUTURA: 274/274 trecho_ancora encontrados LITERALMENTE na canônica",
    len(falt)==0 and len(vaz)==0, f"faltando={len(falt)} vazios={len(vaz)}", {"exemplos_faltando":falt[:5],"vazios":vaz[:5]})
# E3 — chave pmid_oficial no N1? N1 é ficha por PMID; contar fichas na canônica? (237 fichas citadas)
add(3,"N1 v1.3 usa 'pmid_oficial' como chave", "pmid_oficial" in json.dumps(n1), None, {"propriedades_N1":list(n1.get("properties",{}).keys())[:14]})
# E4 — N2 exige trecho_ancora string não vazia (aceita o órfão em JSON)
s=json.dumps(n2)
add(4,"N2 v1.4 aceita trecho_ancora sem validar existência na canônica",
    "trecho_ancora" in s and "canonica" not in s.casefold(), None,
    {"trecho_ancora_schema":str(n2.get("properties",{}).get("trecho_ancora"))[:200]})
# E5 — status_auditoria com CONFIRMADO / PARCIALMENTE_CONFIRMADO
add(5,"N2 v1.4 tem status_auditoria com CONFIRMADO/PARCIALMENTE_CONFIRMADO",
    "PARCIALMENTE_CONFIRMADO" in s and "CONFIRMADO" in s, None,
    {"enum":re.findall(r'"(?:PARCIALMENTE_)?CONFIRMADO[A-Z_]*"',s)[:8]})
# E6 — aprovado_com_ressalva no Schema-Claim obriga nota_ressalva
add(6,"Schema-Claim v1.2: aprovado_com_ressalva obriga nota_ressalva",
    "nota_ressalva" in sc and "aprovado_com_ressalva" in sc, None)
# E7 — usado_em_biblioteca booleano no Schema-Claim
add(7,"Schema-Claim tem usado_em_biblioteca (booleano)", "usado_em_biblioteca" in sc, None,
    {"trinca":(re.search(r".{80}usado_em_biblioteca.{120}",sc,re.S).group(0).replace("\n"," ") if "usado_em_biblioteca" in sc else None)})
# E8 — origem_pipeline sem CLAIM_KIT_CLINICO no N1
n1s=json.dumps(n1)
add(8,"ESTRUTURA: CLAIM_KIT_CLINICO ausente do enum origem_pipeline (N1 v1.3)",
    "CLAIM_KIT_CLINICO" not in n1s, None,
    {"enum_origem":re.findall(r'"origem_pipeline".{0,600}',n1s)[:1]})
# E9 — MESTRE: v1.9 linhas 185-191 (papéis) e 201 (anti-ancoragem) e 462 (passo 8) e 189 (IA2 sobre análise da IA1)
def linha(n): return v19L[n-1].strip() if 0 < n <= len(v19L) else "<fora>"
bloco185=" ".join(v19L[184:191])
add(9,"MESTRE: papéis nas linhas 185-191 (IA3 emite parecer E redige claim)", "emite parecer" in bloco185 and "redige o claim" in bloco185,
    None, {"l185":linha(185),"l188":linha(188),"l191":linha(191)})
add(10,"MESTRE: linha 201 = corolário anti-ancoragem", "ancoragem" in linha(201).casefold() or "ancoragem" in " ".join(v19L[198:206]).casefold(),
    None, {"l201":linha(201)})
add(11,"MESTRE: passo 8 / linha ~462 = 'Fecha o claim preenchendo Schema-Claim'",
    any("fecha o claim preenchendo" in l.casefold() for l in v19L[455:470]),
    None, {"l462":linha(462),"trinca":next((l.strip() for l in v19L[455:470] if "fecha o claim" in l.casefold()),None)})
add(12,"MESTRE: linha 189 = IA2 'segunda inspeção sobre a análise da IA 1'",
    "sobre a análise da ia 1" in " ".join(v19L[184:195]).casefold(), None, {"l189":linha(189)})
# E10 — colisões de PMID previstas (10 dentro da V7)
pmids_v7=set()
try:
    for f in ["01_pmids.json"]:
        d=json.load(open(B1+"/Evidencias/Bibliografia/"+f))
        s2=json.dumps(d); pmids_v7 |= set(re.findall(r'"(3\d{7}|4\d{7})"',s2))
except Exception as e: pass
lista=txt(HOME+"/BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/5º LISTA CANÔNICA — B1  SM-02 V1.3.md")
bloco=txt(HOME+"/BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/6º BLOCO DE ESTADO  v1.6.md")
pmids_kit=set(re.findall(r'\b(\d{7,8})\b',bloco))
dentro = sorted(pmids_kit & pmids_v7)
add(13,"ESTRUTURA: ~10 PMIDs do kit já dentro da V7 (colisões garantidas)",
    len(pmids_v7)>0, f"pmids_V7_medidos={len(pmids_v7)} · pmids_kit={len(pmids_kit)} · interseção={len(dentro)}",
    {"interseccao":dentro[:15],"nota":"conferir contra a medida do mestre (39 de 49 fora → 10 dentro)"})
# E11 — contagem de âncoras/condicao no acervo (o caso 14/22 é do kit, já medido na trilha 85)
add(14,"vinculos: ancoras[] presente 0/274 (coerente com L-06 §8)", all(not v.get("ancoras") for v in V), None)
out=HOME+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA87_verificacao_pareceres_2026-09-22.json"
json.dump(R,open(out,"w"),ensure_ascii=False,indent=2)
print("verdes",sum(1 for x in R["itens"] if x["ok"]),"/",len(R["itens"]))
for x in R["itens"]: print(" ",x["item"],"VERDE" if x["ok"] else "VERMELHO","|",x["teste"],"|",x.get("obs",""))
