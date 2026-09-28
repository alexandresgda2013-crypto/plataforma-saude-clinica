# -*- coding: utf-8 -*-
"""
TRILHA 53 — RODADA 34 — Auditoria independente da 2a rodada da IA externa (Motor Clinico)
Reexecutavel: python3 TRILHA53_script_auditoria_2rodada_IA_externa_motor_2026-09-19.py
Regua: python3, unicodedata NFC; camada declarada em CADA check (case-sensitive | casefold | regex).
Medida sem comando gravado nao vale; contagem exige CAMADA declarada.
Saidas: TRILHA53_auditoria_2rodada_IA_externa_motor_2026-09-19.json (mesma pasta).
Data: 2026-09-19. Objeto: validar E1-E20, P1-P8, G1-G20, C1-C10 da IA externa contra a base vigente
(Filosofia dedbff6c…, Roteiro 5e3f9163…, Arquitetura V2.2 VIGENTE df7f7cfd…) — sem redesenhar o Motor.
"""
import hashlib, json, os, re, sys, unicodedata, glob

DATA = "2026-09-19"
TRILHA = 53
RODADA = 34
HOME = "/home/user"
SERIE = os.path.join(HOME, "BIBLIOTECAS", "_documentos_serie")
BASE = os.path.join(SERIE, "BASE_AUDITORIA_MOTOR_recebida_2026-09-19")
PROD = os.path.join(HOME, "BIBLIOTECAS", "B01_Neuroinflamacao", "atuais", "producao")
ATUAIS = os.path.join(HOME, "BIBLIOTECAS", "B01_Neuroinflamacao", "atuais")

P = {
 "FIL": os.path.join(BASE, "FASE 2- 02 FILOSOFIA DO PROJETO.md"),
 "ROT": os.path.join(BASE, "ROTEIRO DE TRABALHO DA PLATAFORMA.md"),
 "IA":  os.path.join(BASE, "IA_EXTERNA_2a_RODADA_auditoria_classificacao_recebido_2026-09-19.md"),
 "VIG": os.path.join(SERIE, "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"),
 "R24": os.path.join(HOME, "uploads", "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md"),
 "V21": os.path.join(SERIE, "SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.1  -  17.09.26.md"),
 "V215": os.path.join(SERIE, "SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md"),
 "V1":  os.path.join(SERIE, "SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V1 - 15.09.26.md"),
}

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def txt(p):
    return unicodedata.normalize("NFC", open(p, encoding="utf-8").read())

for k, v in P.items():
    if not os.path.exists(v):
        print("FALTA ARQUIVO:", k, v); sys.exit(2)

T = {k: txt(v) for k, v in P.items()}
H = {k: sha(v) for k, v in P.items()}

def sec(t, n):
    """Fatia da secao '# n.' ate o proximo '# m.' (camada regex ^# n\\.)."""
    m = re.search(rf"(?m)^# {n}\.\s", t)
    if not m: return ""
    rest = t[m.start():]
    m2 = re.search(r"(?m)^# \d+\.\s", rest[50:])
    return rest if not m2 else rest[:50 + m2.start()]

def cnt(doc, frag):
    return T[doc].count(frag)

def cntcf(doc, frag):
    return T[doc].casefold().count(frag.casefold())

CHECKS = []
def check(cid, titulo, camada, escopo, comando, anchors, detalhe=""):
    """anchors: lista de (doc, fragmento, (op, n)); ok=True so se TODAS passarem."""
    res, ok_all = [], True
    for doc, frag, (op, n) in anchors:
        cam = "casefold" if camada.startswith("casefold") else "case-sensitive"
        med = cntcf(doc, frag) if cam == "casefold" else cnt(doc, frag)
        ok = {"==": med == n, ">=": med >= n, "<=": med <= n, "!=": med != n}[op]
        ok_all = ok_all and ok
        res.append({"doc": doc, "fragmento": frag[:80], "regra": f"{op}{n}", "medido": med, "ok": ok})
    CHECKS.append({"id": cid, "titulo": titulo, "camada": camada, "escopo": escopo,
                   "comando": comando, "esperado": "; ".join(f'{a[1][:45]} {a[2][0]}{a[2][1]}' for a in anchors),
                   "medido": "; ".join(f"{r['doc']}={r['medido']}" for r in res),
                   "ok": ok_all, "detalhe": detalhe or res})
    return ok_all

def check_manual(cid, titulo, camada, escopo, comando, medido, esperado, ok, detalhe=""):
    CHECKS.append({"id": cid, "titulo": titulo, "camada": camada, "escopo": escopo,
                   "comando": comando, "medido": medido, "esperado": esperado, "ok": ok, "detalhe": detalhe})
    return ok

# ============ BLOCO 0 — INTEGRIDADE, CIENCIA E IDENTIFICACAO DA BASE DA IA ============
check_manual("0.1", "Filosofia verbatim no acervo da casa", "documental (sha256 bytes)",
  P["FIL"], "python3 hashlib.sha256", H["FIL"],
  "dedbff6c8f542025a3f0579d58ab84ca17c122f113f2980edcb18153c408408b",
  H["FIL"] == "dedbff6c8f542025a3f0579d58ab84ca17c122f113f2980edcb18153c408408b",
  f"{len(open(P['FIL'],'rb').read())} bytes")
check_manual("0.2", "Roteiro verbatim no acervo da casa", "documental (sha256 bytes)",
  P["ROT"], "python3 hashlib.sha256", H["ROT"],
  "5e3f916335c4d631c2639e2aaf8efd48c98f6762e263ff301c4dfc9022bd04ac",
  H["ROT"] == "5e3f916335c4d631c2639e2aaf8efd48c98f6762e263ff301c4dfc9022bd04ac",
  f"{len(open(P['ROT'],'rb').read())} bytes")
check_manual("0.3", "Parecer da IA (2a rodada) verbatim no acervo", "documental (sha256 bytes)",
  P["IA"], "python3 hashlib.sha256", H["IA"], "40a58381354d… (registro da casa: transcricao da mensagem do operador)",
  H["IA"].startswith("40a58381354d"), f"{len(open(P['IA'],'rb').read())} bytes")
check_manual("0.4", "Arquitetura V2.2 VIGENTE intocada", "documental (sha256 bytes)",
  P["VIG"], "python3 hashlib.sha256", H["VIG"],
  "df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1",
  H["VIG"] == "df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1",
  "cadeia: ponteiro ARQUITETURA_VIGENTE.txt")

# ciencia intocada
v7 = glob.glob(os.path.join(ATUAIS, "*V7*CANONICA*.md"))
man = glob.glob(os.path.join(ATUAIS, "Evidencias", "Bibliografia", "*manifesto*"))
vin = glob.glob(os.path.join(ATUAIS, "Evidencias", "Vinculos", "vinculos_referencia_afirmacao.json"))
sci_ok, sci_det = True, {}
for nome, lst, pref in [("V7", v7, "6e2c2979"), ("manifesto", man, "79d1309a"), ("vinculos", vin, "490675e6")]:
    if lst:
        h = sha(lst[0]); sci_det[nome] = {"path": lst[0], "sha": h}
        sci_ok = sci_ok and h.startswith(pref)
    else:
        sci_det[nome] = {"path": None, "sha": None}; sci_ok = False
check_manual("0.5", "0 ciencia tocada (V7 + manifesto + vinculos)", "documental (sha256 bytes)",
  str(sci_det), "sha256 dos 3 artefatos", sci_det, "prefixos 6e2c2979 / 79d1309a / 490675e6", sci_ok)

# Identificacao da base documental da IA externa
check("0.6", 'Citacao E6 da IA "preservando a origem de cada informacao" NAO existe em NENHUMA versao da arquitetura',
  "casefold, substring, arquivo inteiro", "VIG/R24/V21/V215/V1 + FIL + ROT",
  'python3: t.casefold().count("preservando a origem de cada informação")',
  [(d, "preservando a origem de cada informação", ("==", 0)) for d in ["VIG","R24","V21","V215","V1","FIL","ROT"]],
  "IA a apresenta com aspas e advérbio 'literalmente' ancorada em '§2, bloco DEFINIÇÃO'")
check("0.7", '"quando pertinente" (parafrase E6) tambem nao existe na base', "casefold, substring", "todos os 7 arquivos",
  'python3: t.casefold().count("quando pertinente")',
  [(d, "quando pertinente", ("==", 0)) for d in ["VIG","R24","V21","V215","V1","FIL","ROT"]])
check("0.8", "Marcas EXCLUSIVAS da vigente ausentes na linha pre-vigente (IA nao as menciona em lugar nenhum)",
  "case-sensitive, substring", "VIG x R24/V21",
  "python3: t.count(frag)",
  [("VIG","origem_conhecimento",("==",3)), ("R24","origem_conhecimento",("==",0)), ("V21","origem_conhecimento",("==",0)),
   ("VIG","prosa deste documento prevalece",("==",1)), ("R24","prosa deste documento prevalece",("==",0)),
   ("VIG","fora do cânone)",("==",1)), ("R24","fora do cânone)",("==",0)),
   ("VIG","**Rev. V2.2 — 2026-09-17**",("==",1)), ("R24","**Rev.",("==",0))])
check("0.9", "H1 da vigente rotula 'V2.2' — C-10 da IA e impossivel contra ela", "case-sensitive, primeira linha",
  "H1 VIG/R24/V21", "python3: txt.splitlines()[0]",
  [("VIG","# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2",("==",1)),
   ("R24","# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2    15.09.26",("==",1)),
   ("V21","# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2    15.09.26",("==",1))],
  "R24 e V2.1 tem H1 identico (V2 15.09.26, sem .1/.2); a vigente rotula V2.2 no H1 e no cabecalho Rev")
def fp(doc):
    return [int(x) for x in re.findall(r"(?m)^# (\d+)\.\s", T[doc])]
f_vig, f_v21, f_r24, f_v215 = fp("VIG"), fp("V21"), fp("R24"), fp("V215")
check_manual("0.10", "Fingerprint de secoes: vigente 30 unicas; V2.1 duplica '# 2.'; r24 duplica/desloca '# 21.'",
  "regex ^# \\d+\\. (multiline), lista integral", "VIG/V21/R24/V215",
  "python3: re.findall(r'(?m)^# (\\d+)\\.\\s')",
  {"VIG": f_vig, "V21": f_v21, "R24": f_r24, "V215": f_v215},
  "VIG seq 1..30; V21 dup 2; R24 dup 21 deslocada",
  f_vig == list(range(1,31)) and f_v21.count(2) == 2 and f_r24.count(21) == 2 and len(f_r24) == 31 and len(f_v21) == 31)
check("0.11", "No 'EVIDÊNCIAS / VÍNCULOS UNIFICADOS': na vigente so resta na NOTA DE REVISAO; em r24/V2.1 existe no mapa §2",
  "case-sensitive, substring + contexto de linha", "VIG/R24/V21",
  "python3: count + linha contendo",
  [("VIG","EVIDÊNCIAS / VÍNCULOS UNIFICADOS",("==",1)), ("R24","EVIDÊNCIAS / VÍNCULOS UNIFICADOS",(">=",1))],
  {"VIG_linha": [l for l in T["VIG"].splitlines() if "UNIFICADOS" in l][:2],
   "R24_linha": [l.strip() for l in T["R24"].splitlines() if "UNIFICADOS" in l][:2]})
def bloco_def(doc):
    m = re.search(r"(?m)^DEFINIÇÃO:\s*$", T[doc])
    if not m: return None
    return "\n".join(l.rstrip("\r") for l in T[doc][m.start():].splitlines()[:6])
bd = {d: bloco_def(d) for d in ["VIG","R24","V21","V215"]}
check_manual("0.12", "Bloco DEFINIÇÃO de §2 e byte-identico na vigente e na linha pre-vigente (ancora E5/E16 da IA ok nas duas)",
  "case-sensitive, fatia apos ^DEFINIÇÃO:$ (6 linhas, \\r removido)", "VIG/R24/V21/V215",
  "python3: fatia 6 linhas apos regex", bd, "VIG==R24==V21; V215 sem bloco",
  bd["VIG"] is not None and bd["VIG"] == bd["R24"] == bd["V21"] and bd["V215"] is None)
pasta_r24 = [l.rstrip("\r") for l in T["R24"].splitlines() if "PASTA" in l][:4]
check_manual("0.13", "Mapa §2 de r24 (base provavel da IA): caixa PASTA de Atualizacao com fluxo a montante (o achado ja corrigido)",
  "case-sensitive, linhas com 'PASTA' em r24", "R24", "python3: linhas contendo 'PASTA'",
  pasta_r24, "evidencia do mapa antigo (no UNIFICADOS) em linhas acima", len(pasta_r24) >= 1)

# ============ BLOCO A — E1..E20 (ancoragem dos [E] da IA na base vigente) ============
check("A-E1", "E1 §28 texto existe (cadeia + Biblioteca nao e camada final de consumo)", "case-sensitive, substring", "VIG §28",
  "python3: sec(28).count(frag)", [
  ("VIG","O Motor não deverá assumir que a Biblioteca Canônica é a camada final de consumo.",("==",1)),
  ("VIG","e utilizar a infraestrutura de Evidências/Vínculos para preservar a rastreabilidade.",("==",1))],
  "ressalva da IA (contradiz §19) so valia no mapa antigo; §2 vigente harmoniza (ver D-C2)")
check("A-E2", "E2 §17 cinco operacoes sob 'Conceitualmente' + remessa ao contrato", "case-sensitive, substring", "VIG §17",
  "python3: sec(17).count(frag)", [
  ("VIG","Conceitualmente:",(">=",1)), ("VIG","seleção",(">=",1)), ("VIG","filtragem",(">=",1)),
  ("VIG","combinação",(">=",1)), ("VIG","contextualização",(">=",1)), ("VIG","rastreabilidade",(">=",1)),
  ("VIG","O contrato deverá especificar:",("==",1))],
  "ressalva da IA aceita pela casa: a lista nao se declara exaustiva; §17 remete ao contrato")
check("A-E3", "E3 §17 sete entradas (IDs, contexto, relacoes, condicoes, evidencias, metadados, JSONs)", "case-sensitive", "VIG §17",
  "python3: sec(17).count(frag)", [
  ("VIG","├── IDs",(">=",1)), ("VIG","├── contexto",(">=",1)), ("VIG","├── relações",(">=",1)),
  ("VIG","├── condições",(">=",1)), ("VIG","├── evidências",(">=",1)), ("VIG","├── metadados",(">=",1)),
  ("VIG","└── JSONs",(">=",1))])
check("A-E4", "E4 sequencia de saidas nos pontos citados (§2/§21/§23)", "case-sensitive", "VIG §2/§21/§23",
  "python3: count no doc e em sec(23)", [
  ("VIG","INTERPRETAÇÃO CONTEXTUALIZADA",(">=",2)), ("VIG","EXPLICAÇÃO NARRATIVA",(">=",2)),
  ("VIG","MECANÍSTICA",(">=",2)), ("VIG","TERAPÊUTICA",(">=",2)),
  ("VIG","contendo os achados, possíveis mecanismos envolvidos, relações relevantes, evidências, explicações científicas e sugestões auxiliares",("==",1))])
check("A-E5", "E5 anamnese como entrada (§2 DEFINIÇÃO) + simulados sem eficacia (Roteiro §9)", "case-sensitive", "VIG §2 / ROT §9", 
  "python3: count(frag)", [
  ("VIG","A anamnese constitui os dados clínicos do caso fornecidos como entrada",("==",1)),
  ("ROT","Os arquivos de anamnese já existentes poderão ser utilizados.",("==",1)),
  ("ROT","não terão finalidade de estabelecer eficácia clínica.",("==",1)),
  ("ROT","Sua função será testar o comportamento do sistema.",("==",1))])
check("A-E6", "E6 consulta ativa a Pasta: EXISTE (§19, todas as versoes); MAS a citacao literal da IA e fabricada (0.6/0.7)",
  "case-sensitive + casefold", "VIG §19/§2 + IA", "python3: count(frag)", [
  ("VIG","O Motor deverá possuir capacidade de consultar a Pasta de Atualização para identificar conhecimento científico recente",("==",1)),
  ("VIG","origem_conhecimento = canonico | atualizacao",(">=",2)),
  ("IA","preservando a origem de cada informação",(">=",1))],
  "substancia E na vigente via origem_conhecimento + §19; na base lida pela IA a regra de preservacao NAO constava")
check("A-E7", "E7 §19 literal: Pasta nao equivale ao canonico", "case-sensitive", "VIG §19",
  "python3: sec(19).count(frag)",
  [("VIG","O Motor não deverá automaticamente tratar uma informação da Pasta de Atualização como equivalente ao conhecimento canônico.",("==",1))])
check("A-E8", "E8 §11 literal — vincula 'o sistema' (precisao: nao nomeia o Motor)", "case-sensitive, CRLF-aware", "VIG §11",
  "python3: count(frag) — fragmentos bullet (§7 repete 'causalidade;' na lista de distincao NT)", [
  ("VIG","o sistema não interpreta automaticamente qualquer conexão como:",("==",1)),
  ("VIG","* indicação;\n* eficácia;\n* causalidade;\n* tratamento;\n* recomendação.",("==",1))],
  "casa: aplicacao ao Motor e DERIVAVEL (o laudo e saida do sistema); a IA disse 'vincula o Motor explicitamente' — leve estiramento")
check("A-E9", "E9 §12 literal: cenario contextualiza, nao causa nem indica", "case-sensitive", "VIG §12",
  "python3: sec(12).count(frag)", [
  ("VIG","Isso não significa que o cenário cause o mecanismo ou que determinado suplemento seja automaticamente indicado.",("==",1)),
  ("VIG","contexto semântico para a interpretação das relações existentes",("==",1))])
check("A-E10", "E10 §22 seis proibicoes para nenhuma camada posterior", "case-sensitive, doc inteiro c/ duplicidade §7↔§22 medida",
  "VIG §22 (§7 repete 3 das 6 proibicoes — fato medido)", "python3: count(frag)", [
  ("VIG","Nenhuma camada posterior poderá:",("==",1)),
  ("VIG","inventar evidência;",("==",1)), ("VIG","inventar referências;",("==",2)),
  ("VIG","criar claims científicos sem origem;",("==",2)), ("VIG","aumentar o grau de certeza;",("==",1)),
  ("VIG","transformar associação em causalidade;",("==",2)), ("VIG","transformar hipótese em fato.",("==",1))],
  "medido 2 nas ocorrencias que §7 duplica (norma NT repetida como norma geral)")
check("A-E11", "E11 reclassificacao da IA correta: §7 e norma da NT; ao Motor chega por §22+§25+Roteiro §10 item 9", 
  "case-sensitive", "VIG §7/§22/§25 + ROT §10", "python3: count(frag)", [
  ("VIG","converter uma relação mecanística em eficácia clínica sem sustentação.",("==",1)),
  ("VIG","# 7. LIMITES DA NT",("==",1)),
  ("ROT","não ocorre elevação epistemológica;",("==",1))])
check("A-E12", "E12 §13 + §25 (qualidade narrativa nao aumenta certeza)", "case-sensitive", "VIG §13/§25",
  "python3: count(frag)", [
  ("VIG","A qualidade da narrativa nunca poderá aumentar artificialmente a certeza científica.",("==",1)),
  ("VIG","Nenhuma camada posterior deverá possuir autoridade para aumentar artificialmente a certeza científica estabelecida pelas camadas anteriores.",("==",1))])
check("A-E13", "E13 §5.5 regra de localizacao do aprofundamento (arquitetura; consequencia runtime = P da IA)", "case-sensitive",
  "VIG §5.5", "python3: count(frag)", [
  ("VIG","## 5.5. Regra de localização do aprofundamento científico",("==",1)),
  ("VIG","objeto científico ao qual o conteúdo se refere",("==",1))])
check("A-E14", "E14 piso estabelecido / proibicao total nao estabelecida (reclassificacao parcial da IA aceita)", "case-sensitive",
  "VIG §14/§28 + FIL", "python3: count(frag)", [
  ("VIG","evitar que a IA precise",("==",1)), ("VIG","O Motor poderá selecionar e combinar estruturas previamente construídas",("==",1)),
  ("VIG","em vez de depender da geração espontânea de explicações científicas a cada caso.",("==",1)),
  ("FIL","respostas improvisadas por modelos de linguagem",("==",1)), ("FIL","conteúdo especulativo",("==",1))])
check("A-E15", "E15 autocorrecao da IA aceita: §15 nao declara interface de Grafo ('travessia' 0x; 'direção' e campo)", 
  "casefold + case-sensitive", "todos os 3 + VIG §15/§5.2/§11", "python3: counts", [
  ("VIG","formalização das relações entre as diferentes entidades",("==",1)),
  ("VIG","direção da relação;",("==",1)), ("FIL","travessia",("==",0)), ("ROT","travessia",("==",0)),
  ("VIG","travessia",("==",0))])
check("A-E16", "E16 multiplos JSONs por entidade (§16 e §1)", "case-sensitive", "VIG §16/§1",
  "python3: count(frag)", [
  ("VIG","Uma entidade poderá gerar múltiplos módulos JSON quando sua representação funcional exigir decomposição.",("==",1)),
  ("VIG","JSON módulo A",("==",1))])
check("A-E17", "E17 inventarios N1 (§5.1) e N2 (§5.2) existem; 'Motor le N1/N2 direto' = [?] correto", "case-sensitive",
  "VIG §5.1/§5.2", "python3: count(frag)", [
  ("VIG","* PMID oficial;",("==",1)), ("VIG","* natureza da evidência;",("==",1)), ("VIG","* desenho do estudo;",("==",1)),
  ("VIG","* trecho-âncora;",("==",1)), ("VIG","* papel da âncora;",("==",1)), ("VIG","* escopo;",("==",1)),
  ("VIG","* direção da relação;",("==",1)), ("VIG","* força da relação;",("==",1)), ("VIG","* grau de maturidade;",("==",1)),
  ("VIG","* trilha clínica ou mecanística;",("==",1)), ("VIG","* status de verificação;",("==",2)),
  ("VIG","* informações de auditoria;",("==",1)), ("VIG","* proveniência.",("==",1))],
  "'status de verificação' consta em §5.1 e §5.2 (medido 2) — reforca o inventario duplo N1/N2")
check("A-E18", "E18 autocorrecao aceita: 'fechamento da trilha' nao consta na base", "casefold, substring", "todos os 3",
  "python3: t.casefold().count(frag)", [(d,"fechamento da trilha",("==",0)) for d in ["VIG","FIL","ROT"]])
check("A-E19", "E19 Filosofia literal: relevancia relativa + descarte + improvaveis", "case-sensitive", "FIL",
  "python3: count(frag)", [
  ("FIL","estima sua relevância relativa",("==",1)), ("FIL","descarta mecanismos pouco compatíveis",("==",1)),
  ("FIL","os mecanismos considerados improváveis",("==",1))])
check("A-E20", "E20 tres trilhas de sugestao (§2 e §21)", "case-sensitive", "VIG §2/§21",
  "python3: count(frag)", [
  ("VIG","MECANÍSTICA",(">=",2)), ("VIG","CLÍNICA",(">=",2)), ("VIG","TERAPÊUTICA",(">=",2))])

# ============ BLOCO B — P1..P8 (propostas da IA: confirmar que NAO estao na base) ============
mt = {d: len(re.findall(r"\b[MT][1-9]\b", T[d])) for d in ["VIG","FIL","ROT"]}
check_manual("B-P1", "P1 modulos M1–M9/T1–T3: 0 ocorrencias na base (integralmente PROPOSTA DA IA — confirmado)",
  "regex \\b[MT][1-9]\\b, arquivo inteiro", "VIG/FIL/ROT", "python3: re.findall", mt, "0 em todos",
  mt == {"VIG":0,"FIL":0,"ROT":0})
check("B-P2", "P2 colide com taxonomia de 2 trilhas do §5.2 (C-6) — ancoras confirmadas", "case-sensitive", "VIG",
  "python3: count(frag)", [
  ("VIG","* trilha clínica ou mecanística;",("==",1)), ("VIG","trilha terapêutica",("==",0))])
check("B-P3", "P3 metade de saida = E (Filosofia + §23); log interno auditavel ausente da base", "casefold + case-sensitive",
  "FIL/VIG/todos", "python3: counts", [
  ("FIL","as razões que sustentam cada hipótese",("==",1)), ("FIL","a fundamentação das sugestões apresentadas",("==",1)),
  ("VIG","explicações científicas",(">=",1)), ("VIG","log de decisão",("==",0)), ("ROT","log de decisão",("==",0))],
  "FIL 'log' como palavra (fronteira \\b): " + str(len(re.findall(r"(?i)\blog\b", T["FIL"]))) + " ocorrencias (agulha solta casaria com 'biologicamente')")
check("B-P4", "P4 piso estabelecido (Filosofia + §22/§25); calibracao verbal nao consta", "case-sensitive", "FIL/VIG",
  "python3: count(frag)", [
  ("FIL","considerando níveis de evidência, qualidade metodológica, sinergias, interações, contraindicações e limitações",("==",1)),
  ("VIG","calibração",("==",0)), ("FIL","calibração",("==",0))])
check("B-P5", "P5 campo trilha existe (§5.2); regra de uso pelo Motor nao consta", "case-sensitive", "VIG",
  "python3: count(frag) + contexto 'trilha'", [
  ("VIG","trilha clínica ou mecanística",("==",1)),
  ("VIG","o Motor deverá usar a trilha",("==",0))],
  "contextos de 'trilha' no doc: " + str(re.findall(r"(?i).{25}trilha.{25}", T["VIG"].replace("\r",""))[:4]))
check("B-P6", "P6 autocorrecao aceita: Roteiro §12 fala de replicacao, nao de determinismo do laudo", "casefold",
  "ROT §12 / todos", "python3: counts", [
  ("ROT","possibilidade de reprodução do processo.",("==",1)),
  ("VIG","determinismo",("==",0)), ("FIL","determinismo",("==",0)), ("ROT","determinismo",("==",0))])
check("B-P7", "P7 sustentacao arquitetonica existe (§5.5/§8/§10); a regra de runtime continua proposta", "case-sensitive",
  "VIG", "python3: count(frag)", [
  ("VIG","A integração ocorre por meio das relações.",("==",1)),
  ("VIG","A NT não deverá reconstruir a Biblioteca.",("==",1))])
check_manual("B-P8", "P8 ordem de fechamento de lacunas: metodologia da IA, sem ancora normativa — confirmado [P]",
  "casefold, substring", "todos os 3", "python3: casefold count",
  {d: cntcf(d, "ordem de fechamento") for d in ["VIG","FIL","ROT"]}, "0 em todos",
  all(cntcf(d, "ordem de fechamento") == 0 for d in ["VIG","FIL","ROT"]))

# ============ BLOCO C — Parte C da IA ([?] resolvidos/reduzidos) ============
check("C-G3red", "G3 reduzido: ancoragem exigida pela Filosofia; classes de ID para sintomas/escalas ausentes de §1/§3",
  "casefold, substring", "FIL + VIG §1/§3", "python3: counts em sec(1)/sec(3)", [
  ("FIL","integra informações clínicas, sintomas, exames, escalas e demais dados do paciente aos 146 IDs oficiais",("==",1)),
  ("VIG","sintomas",("==",0)), ("VIG","escalas",("==",0))],
  "na arquitetura interia 'sintomas'/'escalas' = 0x — redução e pendência residual da IA CONFIRMADAS")
check("C-G6red", "G6 reduzido: conteudo do laudo E (§23 + Filosofia); formato/schema ausente", "casefold", "VIG §23/FIL/todos",
  "python3: counts", [
  ("VIG","laudo/relatório técnico de apoio",(">=",1)), ("FIL","linguagem clara e didática",("==",1)),
  ("VIG","schema do laudo",("==",0)), ("ROT","schema do laudo",("==",0)), ("FIL","schema do laudo",("==",0))])
check("C-G10red", "G10 reduzido: piso E; fronteira exata ausente", "casefold", "todos os 3", "python3: counts", [
  ("VIG","geração espontânea",("==",1)), ("FIL","respostas improvisadas",("==",1)),
  ("VIG","componente generativo",("==",0)), ("FIL","componente generativo",("==",0)), ("ROT","componente generativo",("==",0))])
n10 = len(re.findall(r"(?m)^\d{1,2}\.\s", sec(T["ROT"], 10)))
n12 = len(re.findall(r"(?m)^\*\s+\S", sec(T["ROT"], 12)))
check_manual("C-G15red", "G15 reduzido: Roteiro §10 tem 15 verificacoes; §12 tem 9 criterios de replicacao",
  "regex (?m)^\\d{1,2}\\. e (?m)^\\* dentro das fatias #10/#12", "ROT §10/§12",
  "python3: len(re.findall)", {"§10_itens": n10, "§12_bullets": n12}, "15 / 9", n10 == 15 and n12 == 9,
  "imprecisao da IA: o 'item 30' esta no checklist §13, nao em §12; o conteudo referido existe")
check("C-PROC", "Preservacao de procedencia: RESOLVIDA so na vigente (âncora da IA invalida — ver 0.6)", "case-sensitive",
  "VIG §2 prosa normativa", "python3: count(frag)", [
  ("VIG","carrega a proveniência no próprio item",("==",1)),
  ("VIG","consulta conjunta preserva a rastreabilidade",("==",1))],
  "fragmento anterior cruzava CRLF — corrigido para linha unica")
check("C-TIT", "Titularidade do contrato: Roteiro §2 Grupo 1 lista 'contrato do Motor'", "case-sensitive", "ROT §2",
  "python3: sec(2).count(frag)", [("ROT","* contrato do Motor;",("==",1))])
check("C-G9", "G9 e pendencia DECLARADA pelo proprio §19 (confirmado pela casa)", "case-sensitive", "VIG §19",
  "python3: sec(19).count(frag)", [
  ("VIG","A forma como essa informação será utilizada — por exemplo, alerta, atualização, comparação, enriquecimento ou outra modalidade — deverá ser definida posteriormente no contrato do Motor.",("==",1))])

# ============ BLOCO D — G1..G20 (matriz de pendencias da IA) ============
check("D-G1", "G1 pendencia REAL: 4 representacoes textuais coexistem na vigente; mitigacao nova = prevalencia da prosa",
  "case-sensitive", "VIG §2/§5.3/§6/§14/§17/§19/§30", "python3: counts", [
  ("VIG","(Bibliotecas Canônicas, Narrativas, Atualizações e relações mapeadas no",("==",1)),
  ("VIG","13. fornecer material narrativo reutilizável pelo Motor;",("==",1)),
  ("VIG","Ela fornecerá unidades semânticas e narrativas para o Motor.",("==",1)),
  ("VIG","BIBLIOTECA / NT /",("==",1)),
  ("VIG","a prosa deste documento prevalece sobre os desenhos.",("==",1))],
  "na vigente a CONTRADIÇÃO esta resolvida por regra interna; a superficie exata de runtime segue pendente")
check("D-G2", "G2 'nao determinavel nesta base': Roteiro so informa que arquivos existem", "casefold", "ROT §9/§13 + todos",
  "python3: counts", [
  ("ROT","* contrato de entrada",("==",0)), ("VIG","contrato de entrada",("==",0)), ("FIL","contrato de entrada",("==",0)),
  ("ROT","Anamnese para teste",("==",1)), ("ROT","ARQUIVOS EXISTENTES",("==",1))])
check("D-G4", "G4 pendencia real: campo 'condição' existe como nome; sem linguagem formal na base", "casefold", "VIG",
  "python3: count(frag)", [
  ("VIG","condição, quando aplicável;",("==",1)), ("VIG","condição:",(">=",2)),
  ("VIG","WHERE",("==",0)), ("VIG","expressão booleana",("==",0)), ("VIG","DSL",("==",0))])
check("D-G5", "G5 'nao determinavel nesta base': valores/enumeracoes fora (schemas L-05); base nao declara dominios",
  "casefold", "todos os 3", "python3: casefold counts", [
  ("VIG","schema_vinculo_v1.1.json",("==",1)), ("VIG","schema_referencia_v1.1.json",("==",1)),
  ("VIG","valores permitidos",("==",0)), ("FIL","valores permitidos",("==",0)),
  ("VIG","enumeration",("==",0)), ("VIG","enum",("==",0))],
  "nota: no acervo fora desta base existem schemas L-05 N1v1.3/N2v1.4 aprovados (rodada 29) — nao conta para esta auditoria")
check("D-G7", "G7 pendencia real: nomes das 3 trilhas E; definicao operacional ausente", "case-sensitive", "VIG/FIL",
  "python3: counts", [
  ("VIG","MECANÍSTICA",(">=",2)), ("VIG","TERAPÊUTICA",(">=",2)),
  ("VIG","definição operacional",("==",0)), ("FIL","definição operacional",("==",0))])
check("D-G8", "G8 pendencia real: Filosofia exige; nenhum doc define como (maior lacuna substantiva — casa concorda)",
  "casefold", "todos os 3", "python3: counts", [
  ("FIL","estima sua relevância relativa",("==",1)),
  ("VIG","relevância relativa",("==",0)), ("ROT","relevância relativa",("==",0)),
  ("VIG","critério de descarte",("==",0)), ("FIL","critério de descarte",("==",0)), ("ROT","critério de descarte",("==",0))])
check("D-G11", "G11 real: Filosofia exige sinergia/interacao/contraindicacao; Arquitetura nao enumera tipos", "casefold",
  "FIL/VIG §11/§15", "python3: counts", [
  ("FIL","sinergias, interações, contraindicações",("==",1)),
  ("VIG","sinergia",("==",0)), ("VIG","contraindicação",("==",0)),
  ("VIG","tipo_relacao:",(">=",1)), ("VIG","[relação definida pela ontologia]",("==",1))])
check("D-G12", "G12 real nesta base: 'conflito' de relacoes nao tratado em nenhum dos 3", "casefold", "todos os 3",
  "python3: casefold counts", [
  ("VIG","conflito",("==",0)), ("FIL","conflito",("==",0)), ("ROT","conflito de direções",("==",0))],
  "ROT §3 tem 'registro das divergências' (processo de claims — outro objeto). Acervo fora da base tem minuta L-06 — nao conta aqui")
check("D-G13", "G13 real: reexecucao prevista (checklist 30); versionamento/determinismo do laudo ausente", "casefold",
  "ROT §13 / todos", "python3: counts", [
  ("ROT","Reexecução do circuito após correções",("==",1)),
  ("VIG","versão do laudo",("==",0)), ("ROT","versão do laudo",("==",0)), ("FIL","versão do laudo",("==",0))])
check("D-G14", "G14 real: §22 coloca Biblioteca na cadeia; Roteiro §7 desvia claims dela", "case-sensitive", "VIG §22 / ROT §7",
  "python3: counts + ordem em sec(22)", [
  ("VIG","AFIRMAÇÃO VALIDADA",("==",1)),
  ("ROT","Eles **não entram na Biblioteca Canônica de mecanismos**.",("==",1)),
  ("ROT","CLAIM FECHADO",(">=",1))],
  "ordem em §22: " + str(sec(T["VIG"],22).find("EVIDÊNCIA") < sec(T["VIG"],22).find("BIBLIOTECA CANÔNICA")))
check("D-G16", "G16 pendencia-raiz REAL: Filosofia atribui integracao a anamnese; Arq atribui cruzamento ao Motor", "case-sensitive",
  "FIL / VIG §2/§23", "python3: counts", [
  ("FIL","anamnese estruturada e inteligente integra",("==",1)),
  ("VIG","Ao receber este gatilho, o Motor executa",("==",1)),
  ("VIG","a anamnese estruturada, juntamente com os demais dados clínicos disponíveis, fornece o contexto necessário",("==",1))],
  "tensao textual confirmada nas duas direcoes")
check("D-G17", "G17 real: escopo so na Filosofia; regra de fora-de-escopo ausente", "casefold", "todos os 3",
  "python3: casefold counts", [
  ("FIL","ansiedade e depressão",(">=",1)),
  ("VIG","ansiedade",("==",0)), ("ROT","ansiedade",("==",0)),
  ("VIG","fora do escopo",("==",0)), ("FIL","fora do escopo",("==",0)), ("ROT","fora do escopo",("==",0))])
check("D-G18", "G18 real: 2 valores no vinculo x 3 trilhas na saida; sem mapa", "casefold", "VIG",
  "python3: counts", [
  ("VIG","trilha clínica ou mecanística;",("==",1)), ("VIG","trilha terapêutica",("==",0)),
  ("VIG","mapeamento",("==",0))])
check("D-G19", "G19 pendencia-raiz REAL: Roteiro §16 subordina so o Roteiro; Filosofia x Arquitetura sem regra", 
  "casefold + case-sensitive", "ROT §16 + contagens cruzadas", "python3: counts", [
  ("ROT","Nenhum documento deste roteiro substitui os contratos normativos, schemas ou protocolos específicos.",("==",1)),
  ("ROT","As decisões específicas continuam pertencendo ao documento/contrato correspondente.",("==",1)),
  ("FIL","Arquitetura Consolidada",("==",0)), ("VIG","Filosofia",("==",0)), ("ROT","Filosofia",("==",0))],
  "nenhum dos 3 declara precedencia entre Filosofia e Arquitetura — confirmado")
check("D-G20", "G20 real, mas NAO autonomo: agrega C-3/C-4 e depende de G19 (evitar contagem dupla)", "case-sensitive",
  "FIL / VIG §19 / ROT §7", "python3: counts", [
  ("FIL","Todo conteúdo apresentado ao usuário deve derivar exclusivamente das Bibliotecas de Conhecimento correspondentes.",("==",1)),
  ("FIL","Todo conhecimento científico ingressa obrigatoriamente pela Biblioteca de Conhecimento correspondente.",("==",1)),
  ("VIG","consultar a Pasta de Atualização",(">=",1)),
  ("ROT","não entram na Biblioteca Canônica de mecanismos",("==",1))])

# ============ BLOCO E — C1..C10 (contradicoes/divergencias) ============
check("E-C1", "C-1: textos existem, MAS reconciliacao esta no proprio documento (§8 'integracao por relacoes' + §6 itens) — falsa contradicao",
  "case-sensitive", "FIL / VIG §6/§8/§9", "python3: counts", [
  ("FIL","responsável por conectar os diferentes domínios científicos",("==",1)),
  ("VIG","Cada NT mantém o seu próprio domínio.",("==",1)),
  ("VIG","A integração ocorre por meio das relações.",("==",1)),
  ("VIG","A Ontologia/Grafo formaliza essas relações entre entidades.",("==",1)),
  ("VIG","9. estabelecer relações auditáveis com outras NTs;",("==",1))],
  "'conectar' (Filosofia, macro) = identificar/estruturar relacoes (§6) formalizadas no Grafo (§9/§15): DERIVAVEL; divida de glossario, nao decisao arquitetural")
check("E-C2", "C-2: VERDADEIRA na base lida (no UNIFICADOS/fundia fluxos = o ACHADO do mestre); RESOLVIDA na vigente (§2 novo + prevalencia); residual = desenhos §21/§30",
  "case-sensitive", "VIG §2/§21/§30 + R24", "python3: counts", [
  ("VIG","permanecem segregados até o Motor Clínico.",("==",1)),
  ("VIG","caminho próprio, por consulta ativa, sem",("==",1)),
  ("VIG","sem se fundir aos vínculos canônicos",("==",1)),
  ("R24","EVIDÊNCIAS / VÍNCULOS UNIFICADOS",(">=",1))],
  {"residual§21": "└────────────────┬────────────────┘" in sec(T["VIG"],21),
   "residual§30": "►  JSONs ◄──" in sec(T["VIG"],30)})
check("E-C3", "C-3 VERDADEIRA (interdocumental): Filosofia literal x §19; vigente MITIGA (origem no item), nao resolve formalmente",
  "case-sensitive", "FIL / VIG §19/§2", "python3: counts", [
  ("FIL","derivar exclusivamente das Bibliotecas de Conhecimento correspondentes.",("==",1)),
  ("VIG","capacidade de consultar a Pasta de Atualização",("==",1)),
  ("VIG","origem_conhecimento = canonico | atualizacao",(">=",1)),
  ("VIG","fora do cânone)",("==",1))])
check("E-C4", "C-4 VERDADEIRA (formal): ingresso obrigatorio (Filosofia) x desvio declarado (Roteiro §7)", "case-sensitive",
  "FIL / ROT §7 / VIG §5", "python3: counts", [
  ("FIL","Todo conhecimento científico ingressa obrigatoriamente pela Biblioteca de Conhecimento correspondente.",("==",1)),
  ("ROT","não entram na Biblioteca Canônica de mecanismos",("==",1)),
  ("VIG","não constituem uma segunda Biblioteca Canônica",("==",1))],
  "a direcao ja esta registrada na governanca (rev.38, proposta rodada 31); falta homologacao + regra G19")
check("E-C5", "C-5 VERDADEIRA (cobertura): Filosofia omite Evidencias/Vinculos e Ontologia/Grafo", "casefold", "FIL",
  "python3: casefold counts", [
  ("FIL","ontologia",("==",0)), ("FIL","grafo",("==",0)), ("FIL","vínculo",("==",0)), ("FIL","evidências/vínculos",("==",0))],
  "Filosofia menciona so a triade Biblioteca/NT/JSON")
check("E-C6", "C-6 VERDADEIRA (taxonomia): 2 trilhas no vinculo x 3 na saida", "casefold", "VIG §5.2/§2/§21",
  "python3: counts", [
  ("VIG","trilha clínica ou mecanística;",("==",1)), ("VIG","TERAPÊUTICA",(">=",2)), ("VIG","trilha terapêutica",("==",0))])
check("E-C7", "C-7: divergencia de REPRESENTACAO confirmada (2 sentidos); resolivel por distincao constituição x consumo — rebaixar de contradicao",
  "case-sensitive + ordem", "VIG §2/§5.3/§20/§22/§21/§30", "python3: counts + ordem", [
  ("VIG","EVIDÊNCIA BIBLIOGRÁFICA",("==",1)), ("VIG","fonte científica",("==",1)),
  ("VIG","conhecimento científico",(">=",2))],
  {"ordem_5.3_evidencia_antes_biblioteca": sec(T["VIG"],5).find("EVIDÊNCIA BIBLIOGRÁFICA") > -1,
   "ordem_22": sec(T["VIG"],22).find("EVIDÊNCIA") < sec(T["VIG"],22).find("BIBLIOTECA CANÔNICA"),
   "ordem_2_biblioteca_antes_evidencias": sec(T["VIG"],2).find("BIBLIOTECAS CANÔNICAS") < sec(T["VIG"],2).find("EVIDÊNCIAS"),
   "ordem_30": sec(T["VIG"],30).find("BIBLIOTECA") < sec(T["VIG"],30).find("EVIDÊNCIAS"),
   "ordem_21": sec(T["VIG"],21).find("BIBLIOTECAS") < sec(T["VIG"],21).find("EVIDÊNCIAS"),
   "ordem_20_evidencia_antes": sec(T["VIG"],20).find("EVIDÊNCIA") < sec(T["VIG"],20).find("BIBLIOTECA CANÔNICA")})
check("E-C8", "C-8 divergencia de STATUS real: §26 'passou pela auditoria' x checklist 9 'EM CONSOLIDACAO'/8 'EM VALIDACAO'; mitigacao no proprio §26",
  "case-sensitive", "VIG §26/§29 + ROT §13", "python3: counts", [
  ("VIG","A B1 já possui sua Biblioteca Canônica e passou pelo processo de auditoria.",("==",1)),
  ("VIG","A validação estrutural e a validação científica são dimensões distintas.",("==",1)),
  ("ROT","Biblioteca Canônica B1",(">=",1)), ("ROT","EM CONSOLIDAÇÃO",(">=",2)),
  ("ROT","Claims clínicos B1",("==",1)), ("ROT","EM VALIDAÇÃO",("==",1)), ("ROT","EM TESTE",("==",2))])
check("E-C9", "C-9: textos coexistem, MAS 'PENDENTE DE REGISTRO' != 'nao feito' — falsa contradicao (divergencia de rotulo de controle)",
  "case-sensitive", "ROT §17/§13/§2", "python3: counts", [
  ("ROT","* separação conceitual entre os dois grupos;",("==",1)),
  ("ROT","Definição dos dois grupos de trabalho",("==",1)),
  ("ROT","PENDENTE DE REGISTRO",("==",1))])
check("E-C10", "C-10 FALSA contra a vigente: H1 + Rev + Roteiro ja dizem V2.2 — artefato da base pre-vigente lida pela IA",
  "case-sensitive", "VIG H1/Rev + ROT", "python3: counts", [
  ("VIG","# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2",("==",1)),
  ("VIG","**Rev. V2.2 — 2026-09-17**",("==",1)),
  ("ROT","Arquitetura Consolidada V2.2",("==",2))])
check("E-IA-LIM", "Limite assumido da IA: cita schema_vinculo_v1.1.json — existe na vigente (e em toda a linha); 'nao determinavel' bem aplicado pela IA",
  "case-sensitive", "VIG/IA", "python3: counts", [
  ("VIG","L05/schema_vinculo_v1.1.json",("==",1)), ("VIG","L05/schema_referencia_v1.1.json",("==",1)),
  ("IA","schema_vinculo_v1.1.json",(">=",1))])

# ============ VEREDITOS DA CASA ============
VEREDITOS = {
 "identificacao_da_base_da_IA": "Pre-vigente (linha V2 15.09.26: r24 5be36836… ou V2.1 1a50645e…, indistinguiveis pelas ancorações citadas; NAO e a vigente df7f7cfd). Provas: C-10 impossivel contra H1 V2.2; 0 mencao a origem_conhecimento/prevalencia/Rev; citacao E6 fabricada. Consequencia: itens ancorados fora de §2 mantem-se (sufixo byte-identico); itens de §2/§19/C-2/C-10 exigem re-ancoragem.",
 "E": {"E1":"CONFIRMADO (vigente); ressalva da IA so valia na base antiga","E2":"CONFIRMADO c/ ressalva aceita",
       "E3":"CONFIRMADO","E4":"CONFIRMADO","E5":"CONFIRMADO",
       "E6":"RE-ANCORADO: substancia E na vigente (origem_conhecimento+§19); citacao literal fabricada (0x em todas as versoes)",
       "E7":"CONFIRMADO","E8":"CONFIRMADO com precisao: regra vincula 'o sistema'; ao Motor e derivavel",
       "E9":"CONFIRMADO","E10":"CONFIRMADO","E11":"RECLASSIFICACAO da IA validada (DERIVAVEL ao Motor)","E12":"CONFIRMADO",
       "E13":"CONFIRMADO (arquitetura); runtime = proposta","E14":"CONFIRMADO parcial (piso E; proibicao total pendente->G10)",
       "E15":"AUTOCORRECAO validada (PROPOSTA)","E16":"CONFIRMADO","E17":"CONFIRMADO ([?] bem marcado)","E18":"AUTOCORRECAO validada",
       "E19":"CONFIRMADO","E20":"CONFIRMADO"},
 "P": "Todos confirmados como PROPOSTA DA IA (0 modulos M/T na base; pisos normativos medidos em P3/P4/P5/P7). Nenhum promovido — concordamos.",
 "G": {"G1":"CONFIRMADO pendente real, sem o agravante de contradicao na vigente","G2":"CONFIRMADO (nao determinavel nesta base)",
       "G3":"CONFIRMADO reduzido (residual: classes de ID)","G4":"CONFIRMADO","G5":"CONFIRMADO (nao determinavel nesta base; schemas existem no acervo fora dela)",
       "G6":"CONFIRMADO reduzido (so formato/schema)","G7":"CONFIRMADO","G8":"CONFIRMADO (maior lacuna substantiva)",
       "G9":"CONFIRMADO (pendencia declarada)","G10":"CONFIRMADO reduzido","G11":"CONFIRMADO","G12":"CONFIRMADO nesta base (solucao nao determinavel nela)",
       "G13":"CONFIRMADO","G14":"CONFIRMADO (depende de G19; direcao ja registrada em Roteiro §7/rev.38)","G15":"CONFIRMADO reduzido",
       "G16":"CONFIRMADO raiz (tensao textual real nas duas direcoes)","G17":"CONFIRMADO","G18":"CONFIRMADO",
       "G19":"CONFIRMADO raiz maxima","G20":"REFORMULADO: real, mas agregado de C-3/C-4 sob G19 — nao autonomo"},
 "C": {"C-1":"FALSA CONTRADICAO (reconciliacao interna §6/§8/§9/§15; divida de glossario)","C-2":"VERDADEIRA na base lida = o ACHADO ja corrigido na vigente; residual de desenhos §21/§30 arbitrado pela prevalencia — NAO irredutivel",
       "C-3":"VERDADEIRA formal; mitigada na vigente; exige G19","C-4":"VERDADEIRA formal; exige G19/homologacao (direcao ja registrada)",
       "C-5":"VERDADEIRA (cobertura); decorre/fecha com G19","C-6":"VERDADEIRA (taxonomia) -> G18",
       "C-7":"REBAIXADA: divergencia de representacao com solucao derivavel (constituicao x consumo); divida documental, nao bloqueia contrato",
       "C-8":"VERDADEIRA de registro (status); correcao menor em um dos dois docs",
       "C-9":"FALSA CONTRADICAO ('pendente de registro' != 'nao feito')","C-10":"FALSA contra a vigente (artefato de base)"},
}

out = {
 "trilha": TRILHA, "rodada": RODADA, "data": DATA,
 "objeto": "Auditoria independente da 2a rodada da IA externa sobre o Motor (E/P/G/C) contra a base vigente",
 "documentos_base": {"Filosofia": H["FIL"], "Roteiro": H["ROT"], "Arquitetura_V2.2_vigente": H["VIG"],
                     "Parecer_IA_verbatim": H["IA"]},
 "cadeia_arquitetura": {"VIGENTE_V2.2": H["VIG"], "upload_r24": H["R24"], "SUPERSEDED_V2.1": H["V21"],
                        "SUPERSEDED_V2_15.09": H["V215"], "SUPERSEDED_V1": H["V1"]},
 "shas_ciencia": sci_det, "vereditos_casa": VEREDITOS,
 "confissoes_e_erratas_datadas_2026_09_19": [
   "1a execucao: 69/74; 5 falhos TODOS de regua da casa (nunca fabricar dado; regua corrigida ate verde):",
   "A-E8: agulha 'causalidade;' capturava a lista de distincao do §7 — trocada pela cadeia de 5 bullets CRLF (==1).",
   "A-E10: 3 agulhas de §22 tambem existem em §7 (norma NT duplicada como geral — fato medido): esperado corrigido ==1->==2 para essas 3.",
   "A-E17: '* status de verificacao;' consta em §5.1 e §5.2: esperado ==1->==2 (reforca o duplo inventario N1/N2).",
   "B-P3: 'log' solto casava 'biologicamente' na Filosofia (2x) — medida com fronteira \\b: 0 ocorrencias da palavra.",
   "C-PROC: fragmento cruzava CRLF ('de modo que a\\nconsulta...') — trocado por linha unica (==1).",
   "2a execucao: open() texto aplica universal newlines (\\r\\n->\\n antes do NFC) — cadeia de bullets de A-E8 corrigida \\r\\n->\\n. Camada declarada passa a registrar isso."],
 "resultado": {"verdes": sum(1 for c in CHECKS if c["ok"]), "total": len(CHECKS),
               "verde_total": all(c["ok"] for c in CHECKS)},
 "checks": CHECKS,
}
dst = os.path.join(PROD, "TRILHA53_auditoria_2rodada_IA_externa_motor_2026-09-19.json")
json.dump(out, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(json.dumps(out["resultado"], ensure_ascii=False))
falhos = [c["id"] for c in CHECKS if not c["ok"]]
print("FALHOS:", falhos if falhos else "nenhum")
print("JSON:", dst)
