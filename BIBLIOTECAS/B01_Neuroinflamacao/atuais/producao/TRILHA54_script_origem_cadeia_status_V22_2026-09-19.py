# -*- coding: utf-8 -*-
"""
TRILHA 54 — RODADA 35 — Origem, cadeia e status documental de df7f7cfd… ("V2.2")
Reexecutavel: python3 TRILHA54_script_origem_cadeia_status_V22_2026-09-19.py
Regua: python3 NFC; camada declarada por check; sha256 sha em todo registro.
Pergunta do operador (2026-09-19): origem/cadeia/entrega/aprovacao da "V2.2 vigente" + suspensao
ate esclarecimento + regra nova PROPOSTA→ALTERACAO→ENTREGA COMPLETA→APROVACAO→SHA/DATA→VIGENTE.
"""
import hashlib, json, os, re, sys, unicodedata, difflib, glob

HOME = "/home/user"
SERIE = os.path.join(HOME, "BIBLIOTECAS", "_documentos_serie")
PROD = os.path.join(HOME, "BIBLIOTECAS", "B01_Neuroinflamacao", "atuais", "producao")
ATUAIS = os.path.join(HOME, "BIBLIOTECAS", "B01_Neuroinflamacao", "atuais")

R24 = os.path.join(HOME, "uploads", "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md")
V21 = os.path.join(SERIE, "SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.1  -  17.09.26.md")
V22 = os.path.join(SERIE, "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md")
PONT = os.path.join(SERIE, "ARQUITETURA_VIGENTE.txt")
DEC = os.path.join(ATUAIS, "Auditoria_B1", "decisoes_B1.md")
CHL = os.path.join(HOME, "BIBLIOTECAS", "CHANGELOG_GERAL.md")

sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
T = lambda p: unicodedata.normalize("NFC", open(p, encoding="utf-8").read())
tr, t1, t2 = T(R24), T(V21), T(V22)
td, tl = T(DEC), T(CHL)

CHECKS = []
def cm(cid, titulo, camada, escopo, comando, medido, esperado, ok, detalhe=""):
    CHECKS.append({"id": cid, "titulo": titulo, "camada": camada, "escopo": escopo,
                   "comando": comando, "medido": medido, "esperado": esperado, "ok": bool(ok), "detalhe": detalhe})
    return ok

# --- Elos (cadeia documental medida) ---
cm("1.1", "Elo recebido do operador: upload r24 (V2 - 15.09.26, 50.964 b)", "documental sha256",
   R24, "hashlib.sha256(bytes)", sha(R24),
   "5be36836610d26832506b73dac45baa09e7041bc9ce22e6557f2be59b258e06a",
   sha(R24) == "5be36836610d26832506b73dac45baa09e7041bc9ce22e6557f2be59b258e06a",
   f"{os.path.getsize(R24)} b; ULTIMO DOCUMENTO COMPLETO RECEBIDO DO OPERADOR")
cm("1.2", "Elo instalado rodada 24: V2.1 (= upload + 4 linhas de formato; opção A)", "documental sha256",
   V21, "hashlib.sha256(bytes)", sha(V21),
   "1a50645e260984ab7b78b95abc177bdb171203f55f22990c195e5cefa0a94b60",
   sha(V21) == "1a50645e260984ab7b78b95abc177bdb171203f55f22990c195e5cefa0a94b60",
   f"{os.path.getsize(V21)} b; SUPERSEDED")
cm("1.3", "Elo questionado: df7f7cfd… ('V2.2', construido PELA CASA na rodada 26)", "documental sha256",
   V22, "hashlib.sha256(bytes)", sha(V22),
   "df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1",
   sha(V22) == "df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1",
   f"{os.path.getsize(V22)} b; NUNCA saiu de _documentos_serie (ver 3.1)")

# --- Diffs medidos ---
def diff(a, b):
    d = list(difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm=""))
    pl = [l for l in d if l.startswith("+") and not l.startswith("+++")]
    mi = [l for l in d if l.startswith("-") and not l.startswith("---")]
    return len(pl), len(mi), pl, mi
p1, m1, pl1, mi1 = diff(tr, t1)
cm("2.1", "r24 → V2.1 = +4/−2 linhas (Rev V2.1 · rótulo '# 21.'→'# 2. (MAPA EXECUTIVO)' · fence §21 ×2)",
   "difflib unified NFC", "r24 vs V2.1", "difflib.unified_diff(splitlines())", f"+{p1}/−{m1}", "+4/−2",
   p1 == 4 and m1 == 2, {"removidas": [l[:90] for l in mi1], "adicionadas": [l[:90] for l in pl1]})
p2, m2, pl2, mi2 = diff(t1, t2)
cm("2.2", "V2.1 → V2.2 = +40/−18 (§2 reescrito + Rev V2.2 + duplicata eliminada); sufixo §3→fim idêntico",
   "difflib unified NFC + fatias por seção", "V2.1 vs V2.2", "difflib.unified_diff(splitlines())",
   f"+{p2}/−{m2}", "+40/−18",
   p2 == 40 and m2 == 18,
   "sufixo §3→fim: " + str(t1[t1.find("# 3. CATÁLOGO"):] == t2[t2.find("# 3. CATÁLOGO"):]))
p3, m3, pl3, mi3 = diff(tr, t2)
cm("2.3", "r24 → V2.2 (direto) = +42/−18: 3 blocos de alteracao", "difflib unified NFC", "r24 vs V2.2",
   "difflib.unified_diff(splitlines())", f"+{p3}/−{m3}", "+42/−18", p3 == 42 and m3 == 18,
   "(i) duplicata mapa 114 linhas removida (ii) §2 novo (mapa + prosa) (iii) H1/Rev V2.2")
idxs = [m.start() for m in re.finditer(r"(?m)^# 2\.\s", t1)]
dup = t1[idxs[1]:t1.find("\n# 3.", idxs[1])] if len(idxs) == 2 else ""
cm("2.4", "Duplicata '# 2.' na V2.1 (o '# 21.' extraviado do r24, re-rotulado na instalação) = 6.144 chars/114 linhas; ELIMINADA na V2.2",
   "regex ^# 2\\. + fatia", "V2.1/V2.2", "re.finditer + slice",
   {"V2.1_ocorrencias": len(idxs), "chars": len(dup), "linhas": dup.count("\n"), "presente_na_V2.2": dup in t2},
   "len 2 · 6.144 chars · 114 linhas · ausente na V2.2",
   len(idxs) == 2 and len(dup) == 6144 and dup.count("\n") == 114 and dup not in t2,
   "era o bloco com o nó UNIFICADOS (achado do mestre)")
fp = {n: [int(x) for x in re.findall(r"(?m)^# (\d+)\.\s", t)] for n, t in [("r24", tr), ("V2.1", t1), ("V2.2", t2)]}
cm("2.5", "Fingerprints de secoes: r24=[1,2,21,3…30] (dup 21) · V2.1=[1,2,2,3…30] (dup 2) · V2.2=[1…30] únicas",
   "regex ^# \\d+\\.", "3 elos", "re.findall", fp, "assinaturas acima",
   fp["r24"].count(21) == 2 and fp["V2.1"].count(2) == 2 and fp["V2.2"] == list(range(1, 31)))

# --- Prova de NAO-ENTREGA (pergunta 4) ---
alvo = sha(V22)
copias = []
for p in glob.glob("/home/user/**/*.md", recursive=True):
    if "_documentos_serie" in p: continue
    try:
        if sha(p) == alvo: copias.append(p)
    except Exception:
        pass
cm("3.1", "Zero copias de df7f7cfd… fora de _documentos_serie (varredura sha global .md)",
   "documental sha256, varredura recursiva", "/home/user/**/*.md exclui _documentos_serie",
   "glob + sha256 por arquivo", copias, "[] (nenhuma) — documento completo nunca circulou, nem ao mestre",
   copias == [])
ent = [f for f in os.listdir(SERIE) if "ENTREGA" in f.upper()]
cm("3.2", "Zero artefatos de entrega formal ('ENTREGA*') relativos à V2.2 em _documentos_serie",
   "documental (listdir + filtro nome)", SERIE, "os.listdir + 'ENTREGA' in nome", ent, "[] (nenhum)", ent == [])
cm("3.3", "Registro que CONSTA: decisão de DIREÇÃO 'opção A' (rev.31/rev.33/CHANGELOG)", "documental substring NFC",
   "decisoes/CHANGELOG", "count de strings exatas", {
     "rev31_decisao_formato_V21": td.count("Decisão do operador (2026-09-17):** instalar com as 2 micro-correções de formato (opção A)"),
     "rev33_instalada_opcaoA": td.count("V2.2 INSTALADA (decisão do operador, opção A)"),
     "changelog26": tl.count("V2.2 INSTALADA por decisão do operador (opção A)")}, "≥1 cada",
   td.count("Decisão do operador (2026-09-17):** instalar com as 2 micro-correções de formato (opção A)") >= 1
   and td.count("V2.2 INSTALADA (decisão do operador, opção A)") >= 1
   and tl.count("V2.2 INSTALADA por decisão do operador (opção A)") >= 1,
   "o que foi aprovado: APLICAR a candidata (direção); não consta entrega do documento final")
cm("3.4", "Registro do que a decisão A aprovava: trilha 45 declara 'candidata em STAGING… APLICAÇÃO aguarda decisão'",
   "documental substring NFC", "TRILHA45 json", "count de string", 
   T(os.path.join(PROD, "TRILHA45_achado_mestre_V21_no_unificado_2026-09-17.json")).count("APLICAÇÃO aguarda decisão do operador"),
   ">=1",
   T(os.path.join(PROD, "TRILHA45_achado_mestre_V21_no_unificado_2026-09-17.json")).count("APLICAÇÃO aguarda decisão do operador") >= 1)
cm("3.5", "Registro de ENTREGA DO DOCUMENTO COMPLETO p/ aprovação c/ sha: NÃO CONSTA (busca nos 2 registros)",
   "documental substring NFC (negativo)", "decisoes/CHANGELOG blocos 17/09",
   "count de strings candidatas a entrega", {
     "entregue+V22.2": len(re.findall(r"entregue.{0,60}V2\.2|V2\.2.{0,60}entregue", td + tl)),
     "aprovacao+c sha": len(re.findall(r"aprovação.{0,80}sha|sha.{0,40}aprovação", td + tl))},
   "0 / 0 — real: não consta",
   len(re.findall(r"entregue.{0,60}V2\.2|V2\.2.{0,60}entregue", td + tl)) == 0 and
   len(re.findall(r"aprovação.{0,80}sha|sha.{0,40}aprovação", td + tl)) == 0,
   "busca lexical na integra dos dois registros; comunicação às frentes (RESPOSTA_14) não é entrega-aprovação")

# --- Conteúdo distintivo re-verificado ---
cm("4.1", "Marcas só na V2.2 (origem_conhecimento ×3 · prevalência ×1 · 'fora do cânone' ×1); r24/V2.1 = 0",
   "case-sensitive NFC", "3 elos", "t.count(frag)",
   {n: [t.count("origem_conhecimento"), t.count("prosa deste documento prevalece"), t.count("fora do cânone)")]
    for n, t in [("r24", tr), ("V2.1", t1), ("V2.2", t2)]}, "0/0/0 · 0/0/0 · 3/1/1",
   tr.count("origem_conhecimento") == 0 and t1.count("origem_conhecimento") == 0
   and t2.count("origem_conhecimento") == 3 and t2.count("prosa deste documento prevalece") == 1
   and t2.count("fora do cânone)") == 1)

# --- Ciência intacta ---
import glob as _g
sci_ok, sci = True, {}
for nome, pat, pref in [("V7", os.path.join(ATUAIS, "*V7*CANONICA*.md"), "6e2c2979"),
                        ("manifesto", os.path.join(ATUAIS, "Evidencias", "Bibliografia", "*manifesto*"), "79d1309a"),
                        ("vinculos", os.path.join(ATUAIS, "Evidencias", "Vinculos", "vinculos_referencia_afirmacao.json"), "490675e6")]:
    g = _g.glob(pat)
    h = sha(g[0]) if g else ""
    sci[nome] = h; sci_ok = sci_ok and h.startswith(pref)
cm("5.1", "0 ciência tocada (V7 · manifesto · vínculos)", "documental sha256", str(sci), "sha256",
   sci, "prefixos 6e2c2979/79d1309a/490675e6", sci_ok)

out = {"trilha": 54, "rodada": 35, "data": "2026-09-19",
 "objeto": "origem/cadeia/entrega/aprovacao de df7f7cfd… + suspensao determinada pelo operador + regra nova de versionamento",
 "conclusao_da_trilha": "df7f7cfd…: construido PELA CASA (rodada 26, 17/09) sobre o upload do operador 5be36836… + ACHADO mestre 2841bc66… + parecer comentador dfbd9ab7… · aplicação aprovada em DIREÇÃO ('opção A') · marca de vigência registrada pela casa · ENTREGA DO DOCUMENTO COMPLETO AO OPERADOR PARA APROVAÇÃO NÃO CONSTA (prova 3.1/3.2/3.5) ⇒ pela regra do operador: NÃO é versão oficial; SUSPENSO como referência normativa até decisão do operador sobre a submissão desta rodada",
 "confissoes": "CASA: converteu aprovação de direção (opção A) em marca de vigência sem a etapa entrega-completa→aprovação-com-sha do documento final; a frente do mestre foi orientada a trocar para um arquivo nunca formalmente entregue (rodada 33) — orientação suspensa nesta rodada",
 "resultado": {"verdes": sum(1 for c in CHECKS if c["ok"]), "total": len(CHECKS),
               "verde_total": all(c["ok"] for c in CHECKS)}, "checks": CHECKS}
dst = os.path.join(PROD, "TRILHA54_origem_cadeia_status_V22_2026-09-19.json")
json.dump(out, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(out["resultado"]); print("FALHOS:", [c["id"] for c in CHECKS if not c["ok"]] or "nenhum"); print(dst)
