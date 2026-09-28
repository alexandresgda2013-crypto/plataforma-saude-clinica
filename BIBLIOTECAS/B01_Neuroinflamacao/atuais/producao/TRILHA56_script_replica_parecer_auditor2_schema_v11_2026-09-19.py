#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 56 — Rodada 39 (2026-09-19): RÉPLICA do parecer do auditor-2 sobre "schema_vinculo_v1.1".
Parecer arquivado verbatim: AUDITOR2_resposta_schema_v11_2026-09-19/ (sha 82a8b5b4…).
Método: cada afirmação → 1+ checks com comando gravado. Régua python NFC trilateral; casefold declarado.
"""
import json, hashlib, os, re, shutil, unicodedata, glob

RAIZ = "/home/user"; SERIE = os.path.join(RAIZ, "BIBLIOTECAS/_documentos_serie")
PASTA = SERIE + "/AUDITOR2_resposta_schema_v11_2026-09-19"
V22  = SERIE + "/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
V2   = SERIE + "/SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md"
LOG  = os.path.join(RAIZ, "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Auditoria_B1/decisoes_B1.md")
VINC = os.path.join(RAIZ, "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json")
V7   = os.path.join(RAIZ, "BIBLIOTECAS/B01_Neuroinflamacao/atuais/B1 NEUROINFLAMAÇÃO V7 CANONICA.md")
MAN  = os.path.join(RAIZ, "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia/_manifesto_biblioteca.json")
N1   = SERIE + "/AUDITOR2_triagem_L05v13_recebido_2026-09-17/schema_referencia_recebido_2026-09-17.json"
N2   = SERIE + "/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
N2s = {"v1.1": SERIE+"/L05_v1.1_recebido_2026-09-15/schema_vinculo_v1.1.json",
       "v1.2": SERIE+"/L05_v1.2_schemas_recebidos_2026-09-16/schema_vinculo_v1.2_recebido_2026-09-16.json",
       "v1.3": SERIE+"/AUDITOR2_triagem_L05v13_recebido_2026-09-17/schema_vinculo_v1.3_recebido_2026-09-17.json",
       "v1.4": N2}
CARTA3 = SERIE + "/RESPOSTA_3_AUDITOR_ESTRUTURA_L05_V11_ARQUITETURA_V2_2026-09-15.md"
CARTA8 = SERIE + "/RESPOSTA_8_AUDITOR_ESTRUTURA_L05_N1V13_N2V14_VERIFICADOS_2026-09-18.md"
MINUTA = SERIE + "/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4_PROPOSTA_78a0f2af.md"

checks = []
def C(cid, titulo, camada, escopo, comando, medido, esperado, detalhe=""):
    checks.append({"id": cid,"titulo": titulo,"camada": camada,"escopo": escopo,"comando": comando,
                   "medido": medido,"esperado": esperado,"ok": medido==esperado,"detalhe": detalhe})
def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(65536),b""): h.update(b)
    return h.hexdigest()
def txt(p): return unicodedata.normalize("NFC", open(p,"rb").read().decode("utf-8"))
def props(p):
    s=set()
    def w(o):
        if isinstance(o,dict):
            if isinstance(o.get("properties"),dict): s.update(o["properties"].keys())
            for x in o.values(): w(x)
        elif isinstance(o,list):
            for x in o: w(x)
    w(json.loads(txt(p))); return s

ci_ini = {os.path.basename(p): sha(p) for p in (V7,MAN,VINC)}

# --- A. arquivamento ---
PAR = PASTA + "/PARECER_AUDITOR2_schema_v11_2026-09-19.md"
C("A1","parecer arquivado verbatim (sha do arquivo)","bytes",PAR,"sha256sum",sha(PAR),
  "82a8b5b4519522df87b6a26034bb2a49b7de5a2f08767397ba7dc5dbdab03e68","colado pelo operador neste chat")

# --- B. §1 dele: "o arquivo com esse nome nunca existiu" ---
ups = [os.path.basename(x) for x in glob.glob(os.path.join(RAIZ,"uploads/*"))]
C("B1","nenhum upload com 'v1.1' no nome","documental{CS}","uploads/","[n for n in ls if 'v1.1' in n]",
  [n for n in ups if "v1.1" in n], [],"nome v1.1 NUNCA foi nome de upload — VERDADE p/ artefatos recebidos")
c3 = txt(CARTA3)
C("B2","carta 3 prova o nome real do recebido","documental{NFC,CS}",CARTA3,
  "grep '`schema_vinculo_v1.json` (**v1.1**'", "`schema_vinculo_v1.json` (**v1.1**" in c3, True,
  "a casa registrou nome≠conteúdo na carta 3 — DE FATO (mas sem nomeá-lo defeito)")
C("B3","precisão da citação dele: 'conteúdo **v1.1**' pertence ao objeto referência","documental{NFC,CS}",CARTA3,
  "grep 'schema_referencia_v1.json` (conteúdo **v1.1**'",
  ("`schema_referencia_v1.json` (conteúdo **v1.1**;" in c3, "`schema_vinculo_v1.json` (conteúdo **v1.1**" in c3),
  (True, False),"citação dele desloca a palavra 'conteúdo' para o 2º objeto: sentido exato, forma não literal")
C("B4","nuance: o nome v1.1 EXISTE no acervo verbatim da casa (marca de arquivamento)","bytes",
  N2s["v1.1"],"os.path.exists ∧ ≡ upload",
  (os.path.exists(N2s["v1.1"]), sha(N2s["v1.1"])==sha(os.path.join(RAIZ,"uploads/schema_vinculo_v1.json"))),
  (True, True),"a casa renomeia ao arquivar; DIGITAIS da pasta registram a origem — 'nunca existiu' vale p/ artefato circulante, não p/ o arquivamento")
C("B5","0 diretórios 'L05' no workspace","bytes",RAIZ,"find -type d -name L05",
  [d for d,_,_ in os.walk(RAIZ) for _ in [0] if False] or [p for p in glob.glob(RAIZ+"/**/L05",recursive=True) if os.path.isdir(p)],
  [],"`L05/` = caminho declarado no $id, não diretório — VERDADE")
C("B6","carta 3 contém a nota L05/ literal","documental{NFC,CS}",CARTA3,
  "grep '`L05/` vira diretório canônico quando o 1.2 normatizar'",
  "`L05/` vira diretório canônico quando o 1.2 normatizar" in c3, True,
  "'1.2' = pacote L-05 1.2 (normatização), NÃO o schema v1.2 — precisão de leitura")

# --- C. §§2-3 dele: tabela + eco da cópia de trabalho ---
esp = {"v1.1":("b0934412b010b7e0801f372ae57769fe0daa42c046e757128788159ec9ff4130","15/09"),
       "v1.2":("19f4f29a8763aa635a09d16c1bd960af2687da62a5f79700b8dfd57081d73360","16/09"),
       "v1.3":("ec4f0de88fd0d845ad91f1d413132fa7d9a5c38d1f9f2f7abff1d3a27e7bf836","17/09"),
       "v1.4":("d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050","18/09")}
for v,(s5,d5) in esp.items():
    C(f"C-{v}",f"tabela dele: {v} sha exato","bytes",N2s[v],f"sha256sum ({v}, recebido {d5})",sha(N2s[v]),s5,"")
C("C-par","prefixos que ele citou batem com os oficiais","bytes","N1+N2",
  "sha[:16] == 'd96ad15b620fa373' ∧ shaN1[:16]=='b06660fd985a8186'",
  (sha(N2)[:16], sha(N1)[:16]), ("d96ad15b620fa373","b06660fd985a8186"),"eco da cópia de trabalho DELE: verificável só nos prefixos citados — batem")
c8 = txt(CARTA8)
C("C-c8","carta 8 da casa publica as duas digitais","documental{NFC,CS}",CARTA8,
  "grep b06660fd ∧ d96ad15b", ("b06660fd" in c8, "d96ad15b" in c8), (True,True),"")

# --- D. §4 dele: ponteiro errado + "prosa 3 versões à frente" ---
r22 = txt(V22)
C("D1","V2.2 oficial §5.1 cita v1.1 (1×) · §5.2 cita v1.1 (1×) · 0× v1.3/v1.4","documental{NFC,CS}",V22,
  "count()",
  (r22.count("L05/schema_referencia_v1.1.json"), r22.count("L05/schema_vinculo_v1.1.json"),
   r22.count("schema_vinculo_v1.4")+r22.count("schema_referencia_v1.3")),
  (1,1,0),"ponteiro defasado CONFERE — e é a dívida D-V22-SCHEMA-NOMES, nomeada pela casa na rodada 36 (redescoberta convergente dele)")
i=r22.find("## 5.2"); sec22=r22[i:r22.find("## 5.3",i)]
C("D2","§5.2 lista 'direção da relação' e 'condição, quando aplicável'","documental{NFC,CS}",V22,"grep §5.2",
  ("* direção da relação;" in sec22, "* condição, quando aplicável;" in sec22),(True,True),"")
r2 = txt(V2); i2=r2.find("## 5.2"); sec2=r2[i2:r2.find("## 5.3",i2)] if i2>=0 else "§5.2 AUSENTE"
C("D3","§5.2 é byte-idêntico entre a V2 (15/09) e a V2.2 oficial","documental{NFC,unicode-newlines}",
  "V2 × V2.2","extrair §5.2 de cada e comparar", sec2==sec22, True,
  "a prosa foi escrita em 15/09 — CONTEMPORÂNEA DA v1.1, não 'à frente' dela")
gene = {v: {"condicao":("condicao" in props(p)), "direcao":("direcao" in props(p)),
            "direcao_suporte":("direcao_suporte" in props(p))} for v,p in N2s.items()}
C("D4","GENEALOGIA dos campos citados por ele (o ponto que derruba a tese '3 versões à frente')",
  "documental{NFC,json}","4 versões","walk(properties) por versão",
  gene, {"v1.1":{"condicao":True,"direcao":True,"direcao_suporte":False},
         "v1.2":{"condicao":True,"direcao":False,"direcao_suporte":True},
         "v1.3":{"condicao":True,"direcao":False,"direcao_suporte":True},
         "v1.4":{"condicao":True,"direcao":False,"direcao_suporte":True}},
  "FALSO que 'direção e condição nasceram na v1.4': condicao+direcao existem desde a v1.1 (rename p/ direcao_suporte na v1.2). A prosa §5.2 é compatível com a PRÓPRIA v1.1 — o defeito real é só o NOME do ponteiro")
log = txt(LOG)
C("D5","dívida do ponteiro já estava nomeada pela casa (não é achado novo)","documental{NFC,CS}",LOG,
  "grep D-V22-SCHEMA-NOMES", "D-V22-SCHEMA-NOMES" in log, True,
  "registrada na rodada 36; confirmada no oficial na trilha 55 — convergência independente do auditor-2 = bom sinal")

# --- E. §5 dele: governança/dependências ---
C("E1","autoria do 'aprovado como base de fechamento': frase é do COMENTADOR, casa subscreve","documental{NFC,casefold}",LOG,
  "grep 'o aceite do comentador'",
  bool(re.search(r"o aceite do comentador \(.N1 v1\.3 \+ N2 v1\.4 estruturalmente aprovados", log, re.I)), True,
  "precisão de autoria: não foi 'a casa aprovou' — foi o comentador; a casa subscreveu após réplica (com ressalvas NÃO-estruturais nomeadas: D2 · adoção formal · homologação D4)")
ids = json.loads(txt(os.path.join(RAIZ,"Ferramentas de geração e auditoria/01_norteadores/_derivados_trilha46/_ids_oficiais.json")))
C("E2","catálogo candidato: sha + pendência de adoção + N2 exige validação","bytes + documental",
  "_ids_oficiais.json × N2 v1.4 × log",
  "sha256sum; txt(N2).count('id_oficial','catálogo'); grep log 'adoção formal'",
  (sha(os.path.join(RAIZ,"Ferramentas de geração e auditoria/01_norteadores/_derivados_trilha46/_ids_oficiais.json")),
   "adoção formal do `_ids_oficiais.json`" in log, txt(N2).count("id_oficial")>0),
  ("d0ff264735dc62565c9c102dcb3bd36d4a9960fcf536b636a64494d33d9c532c", True, True),
  "CONFERE: regra existe no schema; fonte não declarada/adotada — dependência crítica real")
d = json.loads(txt(VINC)); vs = d["vinculos"] if isinstance(d,dict) and "vinculos" in d else d
red = sum(1 for x in vs if x.get("g2_elegibilidade")=="redirecionado_clinico")
C("E3","'20 vínculos redirecionados não-conformes' — EXATO","json{unicode}",
  VINC,"sum(g2_elegibilidade=='redirecionado_clinico'); sum('ancoras' in x)",
  {"total":len(vs),"redirecionado_clinico":red,"com_ancoras":sum(1 for x in vs if "ancoras" in x)},
  {"total":274,"redirecionado_clinico":20,"com_ancoras":0},"efeito intencional do D3 — confere com rev.36")
C("E4","portão L-05 'ainda não nasceu' + regras fora do schema","documental{NFC,CS}",LOG,
  "grep 'portão L-05 a nascer' · '486 campos de avaliador'",
  ("portão L-05 a nascer" in log, "486 campos de avaliador" in log),(True,True),
  "V-17 (âncora principal) · condicao×BLOCO_07/08 · identidade do avaliador = padrão E2 (rev.A3-E2 da casa, a caminho do mestre) — os 3 mapeiam em dívidas existentes")
n1j = json.loads(txt(N1)); en=[]
def w2(o,c=""):
    if isinstance(o,dict):
        for k,x in o.items():
            if k=="enum": en.append((c,x))
            else: w2(x,c+"."+k if c else k)
    elif isinstance(o,list):
        for i,x in enumerate(o): w2(x,f"{c}[{i}]")
w2(n1j)
op = [e for c,e in en if "origem_pipeline" in c][0]
C("E5","enum origem_pipeline do N1 v1.3: 5 valores, CLAIM_KIT_CLINICO ausente","documental{NFC,json}",N1,
  "json.load → enum", sorted(op), sorted(["BUSCA_FERRAMENTA","GPM_BRIEFING","INSUMO_EXTERNO_AUDITADO","REANCORAGEM","AUDITORIA_EXTERNA"]),
  "fato: não consta no schema vigente")
AGU = b"CLAIM_KIT_CLINICO"  # agulha ASCII: busca em bytes ≡ busca textual p/ esta agulha (camada declarada)
hits = [p for p in glob.glob(RAIZ+"/BIBLIOTECAS/**/*",recursive=True) if os.path.isfile(p) and AGU in open(p,"rb").read()] 
hits_ex = [p for p in hits if "AUDITOR2_resposta_schema_v11" not in p and "TRILHA56" not in p]  # exclui a própria trilha (agulha procurando a si mesma — confissão C56-2)
C("E6","'consta no meu parecer de ontem' (CLAIM_KIT_CLINICO) — verificável na base arquivada?",
  "bytes{agulha ASCII} + documental{NFC}",RAIZ+"/BIBLIOTECAS","scan bytes CLAIM_KIT_CLINICO (excl. parecer de hoje) · count na minuta v1.4",
  {"arquivos":len(hits_ex),"na_minuta_v1.4":txt(MINUTA).count("CLAIM_KIT_CLINICO")}, {"arquivos":0,"na_minuta_v1.4":0},
  "régua: escopo exclui parecer de hoje E artefatos da própria trilha (self-match confessado). NÃO VERIFICÁVEL na base da casa: o 'parecer de ontem' dele não circulou até aqui → pedir os bytes ao operador. O PEDIDO em si é coerente com o fluxo de claims (subordinado à homologação B + regra nova)")

# --- F. sugestão (renomear) provada ---
tmp = os.path.join(RAIZ,"BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/_tmp_renomear_teste.json")
shutil.copyfile(N2, tmp); ok_rename = sha(tmp)==sha(N2); os.remove(tmp)
C("F1","'renomear não muda o sha' — verdade, medido","bytes",N2,"cp com outro nome → sha igual",
  ok_rename, True,"tecnicamente exato; MAS: renomear o artefato oficial de entrega = ato registrável do operador/casa; corrigir §5 da V2.2 = emenda ao OFICIAL → regra nova completa (proposta→documento→aprovação→sha/data)")

# --- 0 ciência ---
ci_fim = {os.path.basename(p): sha(p) for p in (V7,MAN,VINC)}
C("CI0","0 ciência: V7/manifesto/vínculos intactos","bytes","acervo B1","sha início==fim",ci_ini==ci_fim,True,"")

veredito = ("Parecer SUBSTANCIALMENTE correto e convergente (tabela de shas exata · ponteiro defasado real · 20 redirecionados exato · "
 "catálogo não adotado real · enum sem CLAIM_KIT_CLINICO real · 'não normativo' = posição da casa r38). "
 "3 CORREÇÕES DE PRECISÃO: P1 autoria ('a casa aprovou' → foi o comentador; casa subscreveu c/ ressalvas nomeadas) · "
 "P2 GENEALOGIA FALSA: 'direção e condição nasceram na v1.4' — medido: condicao+direcao existem desde a v1.1; a prosa do §5.2 é de 15/09 "
 "(contemporânea da v1.1) e compatível com ela; o defeito real é só o NOME do ponteiro (D-V22-SCHEMA-NOMES, que a casa JÁ nomeou na r36 — "
 "redescoberta convergente) · P3 'consta no meu parecer de ontem' (CLAIM_KIT_CLINICO) NÃO verificável na base arquivada (0 arquivos/0× na "
 "minuta) → pedir os bytes. NUANCE da casa: o nome v1.1 existe no ACERVO verbatim como marca de arquivamento desde 15/09 (carta 3 prova o "
 "recebido='schema_vinculo_v1.json'); a casa confessa: registrou a assimetria sem nomeá-la defeito — agora nomeada D-L05-NOME-X-ID. "
 "Sugestão dele (renomear+corrigir ponteiros): tecnicamente sha-invariante (medido), mas exige a regra nova para tocar a V2.2 oficial.")
res = {"trilha":56,"rodada":39,"data":"2026-09-19",
 "tema":"réplica do parecer do auditor-2 sobre schema_vinculo_v1.1 — nunca existiu como upload; vigente v1.4; 3 precisões",
 "total":len(checks),"verdes":sum(c["ok"] for c in checks),"checks":checks,"veredito_casa":veredito}
out = os.path.join(RAIZ,"BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA56_replica_parecer_auditor2_schema_v11_2026-09-19.json")
json.dump(res, open(out,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"{res['verdes']}/{res['total']} verdes")
for c in checks:
    if not c["ok"]: print("  FALHOU:",c["id"],"medido=",str(c["medido"])[:200])
