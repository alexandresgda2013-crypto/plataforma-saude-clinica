#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 58 — Rodada 41 (2026-09-19): CANDIDATA V2.3 (renumerada no cabeçalho, histórico na Rev) + 3 cartas + regra de downloads.
Decisão do operador: "precisa mudar o número da versão" · cartas direcionadas · "qualquer mudança em documento → download".
Candidata e1 (rodada 40) SUPERSEDED antes de nascer — substituída por esta, por decisão de rótulo do operador.
"""
import json, hashlib, os, re, shutil, zipfile, unicodedata, difflib

RAIZ="/home/user"; SERIE=RAIZ+"/BIBLIOTECAS/_documentos_serie"
BASE =SERIE+"/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
PONT =SERIE+"/ARQUITETURA_VIGENTE.txt"
OUTD =SERIE+"/CARTAS_V23_2026-09-19"
CAND =OUTD+"/CANDIDATA_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.3 - 19.09.26.md"
ENT  =RAIZ+"/ENTREGAS/2026-09-19_V2.3_CANDIDATA_E_CARTAS"
V7   =RAIZ+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais/B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
MAN  =RAIZ+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia/_manifesto_biblioteca.json"
VINC =RAIZ+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
SHA_BASE="df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1"

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
raw=open(BASE,"rb").read()
C("B1","base oficial intacta","bytes",BASE,"sha256sum",(sha(BASE),len(raw)),(SHA_BASE,52181),"")
t=unicodedata.normalize("NFC",raw.decode("utf-8")); L=t.split("\r\n")
oc22=[i+1 for i,l in enumerate(L) if "V2.2" in l]
C("B2","'V2.2': 3× (L1 identidade · L4 Rev · L167 proveniência) · '17.09.26': só L1","documental{NFC,CS}",BASE,
  "linhas com V2.2 / 17.09.26",(oc22,[i+1 for i,l in enumerate(L) if "17.09.26" in l]),([1,4,167],[1]),
  "CRITÉRIO declarado: L1/L4 = identidade da vigente (MUDAM) · L167 = proveniência histórica correta (FICA)")

# --- construção V2.3 (bytes) ---
novo=raw.replace(b"# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2    17.09.26",
                 b"# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.3    19.09.26")
REV_VELHA=L[3]
REV_NOVA=("**Rev. V2.3 — 2026-09-19** · Correção editorial dos ponteiros de schema do §5.1/§5.2 "
 "(`L05/schema_referencia_v1.1.json` → `L05/schema_referencia_v1.3.json`; "
 "`L05/schema_vinculo_v1.1.json` → `L05/schema_vinculo_v1.4.json`) — dívida D-V22-SCHEMA-NOMES · "
 "renumeração de versão no cabeçalho decidida pelo operador (rastreabilidade da versão vigente; a emenda editorial "
 "virou mudança de versão) · base: V2.2 oficial (`df7f7cfd…`, aprovada em 2026-09-19) · decisão do operador (rodada 41) · "
 "0 conteúdo normativo alterado · histórico: " + REV_VELHA)
# ORDEM IMPORTA (confissão C58-1): primeiro os ponteiros, DEPOIS a cláusula Rev —
# senão o .replace global devora as citações históricas v1.1 dentro da própria cláusula.
novo=novo.replace(b"`L05/schema_referencia_v1.1.json`",b"`L05/schema_referencia_v1.3.json`") \
         .replace(b"`L05/schema_vinculo_v1.1.json`", b"`L05/schema_vinculo_v1.4.json`")
assert novo.count(REV_VELHA.encode("utf-8"))==1
novo=novo.replace(REV_VELHA.encode("utf-8"), REV_NOVA.encode("utf-8"))
C("C1","construção: CRLF 1411/1411 · 0 LF solto","bytes","candidata","count",
  (novo.count(b"\r\n"),novo.count(b"\n")-novo.count(b"\r\n")),(1411,0),"")
t2=unicodedata.normalize("NFC",novo.decode("utf-8")); L2=t2.split("\r\n")
D=list(difflib.unified_diff(L,L2,lineterm=""))
minus=[l for l in D if l.startswith("-") and not l.startswith("---")]; plus=[l for l in D if l.startswith("+") and not l.startswith("+++")]
alteradas=[i+1 for i,(x,y) in enumerate(zip(L,L2)) if x!=y]
C("C2","diff = exatas 4 linhas substituídas (1·4·269·306), 0 ins/rem","documental{NFC}","base×V2.3",
  "difflib",{"n_linhas":(len(L),len(L2)),"menos":len(minus),"mais":len(plus),"linhas":alteradas},
  {"n_linhas":(1412,1412),"menos":4,"mais":4,"linhas":[1,4,269,306]},"")
C("C3","L167 (proveniência 'Rev. V2.2') INALTERADA · Rev V2.2 preservada INTEIRA na linha histórico",
  "documental{NFC}","V2.3","L167 igual ∧ Rev_velha ⊆ L4_nova",
  (L2[166]==L[166], REV_VELHA in L2[3]),(True,True),"")
C("C3b","cláusula da Rev preserva as citações históricas 'v1.1 → v1.3' e 'v1.1 → v1.4'","documental{NFC}","V2.3",
  "agulhas literais na linha 4",
  ("`L05/schema_referencia_v1.1.json` → `L05/schema_referencia_v1.3.json`" in L2[3],
   "`L05/schema_vinculo_v1.1.json` → `L05/schema_vinculo_v1.4.json`" in L2[3]),(True,True),
  "guarda contra regressão da C58-1 (replace global comendo a citação histórica)")
C("C4","H1 = V2.3 19.09.26 · 'V2.2' restantes = só histórico (L4-histórico + L167) · 30 seções únicas",
  "documental{NFC}","V2.3","checks",
  (L2[0]=="# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.3    19.09.26",
   [i+1 for i,l in enumerate(L2) if "V2.2" in l],
   len(re.findall(r"^# (\d+)\.",t2,re.M))), (True,[4,167],30),"")
oc11=[i+1 for i,l in enumerate(L2) if "v1.1" in l]
C("C5","por-linha: 269→v1.3 (sem v1.1) · 306→v1.4 (sem v1.1) · 'v1.1' só na cláusula histórico da Rev(L4)",
  "documental{NFC,CS}","V2.3","por linha",
  {"l269":("v1.3" in L2[268],"v1.1" not in L2[268]),"l306":("v1.4" in L2[305],"v1.1" not in L2[305]),"linhas_v1.1":oc11},
  {"l269":(True,True),"l306":(True,True),"linhas_v1.1":[4]},"")

os.makedirs(OUTD,exist_ok=True)
open(CAND,"wb").write(novo); sha_cand=sha(CAND); tam=len(novo)
C("G1","candidata V2.3 gravada · ponteiro NÃO movido","bytes",CAND,"sha; ponteiro",
  (os.path.exists(CAND),"df7f7cfdfc01cf77" in open(PONT,encoding="utf-8").read()),(True,True),
  f"sha V2.3={sha_cand} · {tam} b · vigente oficial permanece V2.2 df7f7cfd… até aprovação do operador")

# --- CARTAS ---
CAB=lambda titulo: f"{titulo}\n{'='*len(titulo)}\nCasa (bancada de verificação) → via OPERADOR · 2026-09-19 · rodada 41\nEstado de governança: V2.3 é CANDIDATA — a oficial VIGENTE hoje é a V2.2 `df7f7cfd…` (aprovada 2026-09-19). Nada circula direto entre IAs: tudo flui pelo operador.\n\n"
DIGIT=(f"DIGITAIS (conferir com sha256sum):\n"
 f"· oficial vigente  V2.2 `df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1` (52.181 b · CRLF)\n"
 f"· candidata        V2.3 `{sha_cand}` ({tam} b)\n"
 f"· schema N1 corrente (referência) v1.3 `b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da`\n"
 f"· schema N2 corrente (vínculo)    v1.4 `d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050`\n\n"
 f"O QUE MUDA NA V2.3 (diff medido: exatas 4 linhas substituídas, 0 inseridas/removidas; CRLF 1411/1411; 30 seções únicas intactas):\n"
 f"1. cabeçalho: «…PLATAFORMA V2.2    17.09.26» → «…PLATAFORMA V2.3    19.09.26»  (renumeração pedida pelo operador: rastreabilidade da vigente — 'só mudar a data é pouco');\n"
 f"2. linha Rev: passa a «Rev. V2.3 — 2026-09-19» com o histórico INTEIRO da Rev. V2.2 preservado na mesma linha;\n"
 f"3. §5.1: ponteiro `L05/schema_referencia_v1.1.json` → `L05/schema_referencia_v1.3.json`;\n"
 f"4. §5.2: ponteiro `L05/schema_vinculo_v1.1.json`   → `L05/schema_vinculo_v1.4.json`.\n"
 f"Motivo: os ponteiros citavam 'v1.1' — nomes que nunca existiram como arquivos reais (dívida D-V22-SCHEMA-NOMES). 0 conteúdo normativo alterado.\n\n"
 f"O QUE NÃO MUDA: todo o restante, byte a byte — §2 completo (fluxos segregados até o Motor · origem_conhecimento · "
 f"prosa prevalece sobre desenhos · Pasta fora do cânone) · §§3–30 · a âncora interna «(Rev. V2.2, 2026-09-17)» do §2 FICA — "
 f"é proveniência histórica correta (a regra nasceu na V2.2). Citações por seção/feitas na auditoria da rodada 34 não quebram.\n\n")
cartas = {
"CARTA_18_AO_AUDITOR_MESTRE_V23_2026-09-19.md": CAB("CARTA 18 AO AUDITOR-MESTRE (projeto 1) — Atualização documental da arquitetura: V2.2 → V2.3") + DIGIT +
 ("PARA O SEU PROJETO:\n"
  "1) A oficial VIGENTE hoje é a V2.2 (`df7f7cfd…`). Se o projeto ainda detém o arquivo antigo (`309aa65f…`, upload r24 "
  "rotulado), substitua já pela oficial vigente e ecoe o sha — fecha a dívida D-V22-BYTES-PROJETO.\n"
  "2) Quando o operador repassar a V2.3 (após aprovar), substitua de novo e ecoe o sha da V2.3. A cadeia de versões fica: "
  "V2.1 `1a50645e…` → V2.2 `df7f7cfd…` → V2.3 (sha acima).\n"
  "3) NENHUM contrato do Motor / L-NT / L-06 muda. Os ponteiros §5.1/§5.2 agora citam os schemas que você já deve tratar "
  "como correntes (N1 v1.3 · N2 v1.4).\n"
  "PEDIDOS PENDENTES (inalterados, só referência): piloto de 20 unidades NT-B1 (revisor cego · ≥90% · 3 testes) · minuta 2 "
  "L-06 · resposta A/B/C/D + linha de herança `uso` (kit→N2.uso→NT.uso).\n"),
"CARTA_9_AO_AUDITOR_ESTRUTURA_V23_2026-09-19.md": CAB("CARTA 9 AO AUDITOR-ESTRUTURA (auditor-2) — Atualização documental da arquitetura: V2.2 → V2.3") + DIGIT +
 ("REGISTRO CRUZADO: o ponteiro defasado que você reportou em 19/09 é o mesmo que a casa nomeou D-V22-SCHEMA-NOMES na "
  "rodada 36 — convergência independente, agora corrigida na V2.3.\n"
  "PRECISÕES À SUA RÉPLICA (trilha 56 da casa, 26/26 verdes — disponível se quiser):\n"
  "(a) autoria: o aceite '…base de fechamento do L-05' (r29) é do comentador; a casa subscreveu após réplica integral — "
  "sem erro de mérito, só de atribuição;\n"
  "(b) genealogia (a única afirmação factual que não se sustentou na bancada): `direcao` e `condicao` existem DESDE a v1.1 "
  "(o rename para `direcao_suporte` ocorreu na v1.2) — logo a prosa do §5.2 não estava 'três versões à frente': foi escrita "
  "em 15/09, contra a própria v1.1. O defeito real era só o NOME do ponteiro — corrigido agora;\n"
  "(c) o 'parecer de ontem' citando `CLAIM_KIT_CLINICO` para o enum `origem_pipeline` do N1 NÃO chegou à casa (0 ocorrências "
  "na base arquivada · 0× na minuta v1.4). Por favor reenvie os bytes verbatim; a proposta fica registrada e subordinada à "
  "homologação do fluxo de claims e à cadeia formal de alteração do N1 (regra nova de versionamento — a mesma agora aplicada "
  "à arquitetura).\n"
  "ESTADO DOS SCHEMAS (alinhado à sua própria leitura de 19/09): N1 v1.3 / N2 v1.4 = correntes validados tecnicamente "
  "(ciclo r29; 52/52 + 26/26); selo formal do operador com sha/data ainda pendente — os nomes internos de arquivo e o "
  "rótulo 'PROPOSTA — não normativo' nas descriptions permanecem como dívida editorial (D-L05-NOME-X-ID).\n"),
"CARTA_AO_COMENTADOR_EXTERNO_V23_2026-09-19.md": CAB("CARTA AO COMENTADOR EXTERNO (ChatGPT) — Atualização documental da arquitetura: V2.2 → V2.3") + DIGIT +
 ("ESTADO DO SEU ACEITE DE 18/09 (rodada 29): 'N1 v1.3 + N2 v1.4 estruturalmente aprovados como base de fechamento do "
  "L-05' permanece INTEIRAMENTE de pé — a casa subscreve número a número (trilha 48: 52/52 · 26 casos sintéticos 26/26). "
  "Os ponteiros da arquitetura que citavam 'v1.1' agora apontam exatamente para esses dois — coerência restaurada.\n"
  "GOVERNANÇA (regra nova do operador, vigente): PROPOSTA → DOCUMENTO COMPLETO ENTREGUE → APROVAÇÃO → SHA/DATA → VIGENTE. "
  "A V2.2 cumpriu a cadeia em 19/09; a V2.3 aguarda a mesma aprovação; os schemas L-05 aguardam o selo formal do operador "
  "(sua base de fechamento foi o trampolim técnico — o carimbo final é dele).\n"
  "VERIFICAÇÃO: qualquer arquivo recebido deixa de ser oficial se o sha não bater com as digitais acima — favor ancorar "
  "comentários sempre por sha, como de costume. Pontos seus são lidos pela casa com réplica empírica antes de qualquer "
  "aceite (política permanente, a mesma aplicada ao seu parecer da rodada 29).\n"),
}
for nome, corpo in cartas.items():
    open(os.path.join(OUTD,nome),"w",encoding="utf-8").write(corpo)
ok_cartas=all(os.path.exists(os.path.join(OUTD,n)) for n in cartas) and \
         all(sha_cand in open(os.path.join(OUTD,n),encoding="utf-8").read() and SHA_BASE in open(os.path.join(OUTD,n),encoding="utf-8").read() for n in cartas)
C("C6","3 cartas geradas, cada uma cita sha vigente + sha candidata + instrução de verificação","documental",OUTD,
  "grep shas nas 3",ok_cartas,True,"mestre · auditor-estrutura · comentador — direcionadas, com especificidades por frente")

# --- pacote de entrega (regra nova de downloads: TODA mudança documental → download) ---
os.makedirs(ENT,exist_ok=True)
lei=(f"PACOTE — V2.3 CANDIDATA + CARTAS ÀS FRENTE · rodada 41 · 2026-09-19\n{'='*72}\n"
 f"1) CANDIDATA_ARQUITETURA_..._V2.3...md  sha {sha_cand} ({tam} b) — vira oficial SÓ após seu 'aprovado'.\n"
 f"2) CARTA_18_AO_AUDITOR_MESTRE...md · 3) CARTA_9_AO_AUDITOR_ESTRUTURA...md · 4) CARTA_AO_COMENTADOR...md\n"
 f"5) V2.2 oficial vigente segue df7f7cfd… (nada foi substituído no ponteiro).\n"
 f"REGRA PERMANENTE REGISTRADA (verbatim do operador, rev.48): 'qualquer conversa que gerou uma mudança no documento, "
 f"seja ele qual for, você tem que me disponibilizar para download' — esta pasta é a primeira aplicação; a partir de "
 f"agora, TODA mudança documental gera pacote ENTREGAS/ datado.\n")
open(os.path.join(ENT,"LEIAME.txt"),"w",encoding="utf-8").write(lei)
shutil.copyfile(CAND, os.path.join(ENT,"CANDIDATA_ARQUITETURA_V2.3_19.09.26.md"))
for n in cartas: shutil.copyfile(os.path.join(OUTD,n), os.path.join(ENT,n))
ZIP=os.path.join(ENT,"V2.3_CANDIDATA_E_CARTAS_2026-09-19.zip")
with zipfile.ZipFile(ZIP,"w",zipfile.ZIP_DEFLATED) as z:
    for fn in sorted(os.listdir(ENT)):
        if not fn.endswith(".zip"): z.write(os.path.join(ENT,fn),fn)
tmp=ENT+"/_v"; shutil.rmtree(tmp,ignore_errors=True)
with zipfile.ZipFile(ZIP) as z: z.extractall(tmp)
C("G2","pacote ENTREGAS + zip re-extraído confere (candidata byte-idêntica)","bytes",ZIP,"unzip→sha",
  sha(tmp+"/CANDIDATA_ARQUITETURA_V2.3_19.09.26.md")==sha_cand,True,f"zip {os.path.getsize(ZIP)} b · {len([f for f in os.listdir(ENT) if not f.endswith('.zip')])} arquivos")
shutil.rmtree(tmp)
ci_fim={os.path.basename(p):sha(p) for p in (V7,MAN,VINC)}
C("CI0","0 ciência intacta","bytes","acervo B1","sha início==fim",ci_ini==ci_fim,True,"")

res={"trilha":58,"rodada":41,"data":"2026-09-19",
 "tema":"V2.3 CANDIDATA (renumerada no cabeçalho, Histórico na Rev) + 3 cartas + regra permanente de downloads",
 "sha_v23_candidata":sha_cand,"bytes_v23":tam,"total":len(checks),"verdes":sum(c["ok"] for c in checks),
 "checks":checks,
 "veredito_casa":"V2.3 CANDIDATA medida: 4 linhas substituídas (H1·Rev·§5.1·§5.2), resto byte-idêntico, histórico da Rev V2.2 "
  "preservado integralmente, L167-proveniência mantida. Vigente oficial continua V2.2 df7f7cfd… até 'aprovado' do operador. "
  "Candidata e1 da rodada 40 = SUPERSEDED antes de nascer (decisão de rótulo). Cartas aos 3 frentes geradas com digitais."}
out=RAIZ+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA58_V23_candidata_e_cartas_2026-09-19.json"
json.dump(res,open(out,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print(f"{res['verdes']}/{res['total']} verdes · sha V2.3 {sha_cand[:16]}… · {tam} b")
for c in checks:
    if not c["ok"]: print("  FALHOU:",c["id"],str(c["medido"])[:240])
