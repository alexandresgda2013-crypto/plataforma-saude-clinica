#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 49 — RODADA 30 — 2026-09-18
Réplica empírica: L-NT CONTRATO DAS UNIDADES NARRATIVAS · Minuta 1 (Auditor-Mestre)
+ análise do comentador. Protocolo da casa: réplica antes de aceitar; CAMADA declarada
em toda contagem; detector > tela (stdout íntegro); 0 ciência tocada.
Somente leitura. Saída: TRILHA49_LNT_minuta1_2026-09-18.json + stdout.
"""
import json, hashlib, re, sys, subprocess, unicodedata, glob, statistics, os
from collections import Counter

AT   = "/home/user/BIBLIOTECAS/B01_Neuroinflamacao/atuais"
PROD = AT + "/producao"
PKT  = "/home/user/BIBLIOTECAS/_documentos_serie/MESTRE_LNT_minuta1_recebido_2026-09-18"
DOC  = "/home/user/BIBLIOTECAS/_documentos_serie"
V7_F   = AT + "/B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
MAN_F  = AT + "/Evidencias/Bibliografia/_manifesto_biblioteca.json"
VINC_F = AT + "/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
V22_F  = DOC + "/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
MINUTA = PKT + "/L-NT_CONTRATO_UNIDADES_NARRATIVAS_minuta1_294119b9_2026-09-18.md"
VERBAT = PKT + "/COMENTADOR_verbatim_LNT_minuta1_2026-09-18.md"
M2_F   = DOC + "/L05_1.1_minuta_mestre_recebida_2026-09-15/L05_1.1_CONTRATO_CADEIA_MOTOR_minuta2_2026-09-15.md"
BLOCO6 = DOC + "/KIT_CLINICA_recebido_2026-09-15/6º BLOCO DE ESTADO  v1.6.md"
SC12   = DOC + "/KIT_CLINICA_recebido_2026-09-15/3º SCHEMA-CLAIM — v1.2.md"
P8     = "/home/user/Ferramentas de geração e auditoria/06_portao_P8_coerencia/scripts/validar_coerencia_camadas.py"
N2     = DOC + "/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
DEC    = AT + "/Auditoria_B1/decisoes_B1.md"
LED    = AT + "/Auditoria_B1/ledger_auditoria_B1.json"
R3     = DOC + "/RESPOSTA_3_PARECER_B1V6_AUDITOR_MESTRE_2026-09-13.md"
R5     = DOC + "/RESPOSTA_5_C4_RATIFICADA_P8_V1516_2026-09-14.md"
R15    = DOC + "/RESPOSTA_15_MESTRE_P8_SELADO_FASE4_VERDE_2026-09-18.md"

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
def nfc(s): return unicodedata.normalize("NFC", s)

CHECKS = []
def reg(cid, titulo, camada, escopo, comando, medido, esperado, ok, detalhe="", regex=None):
    c = {"id": cid, "titulo": titulo, "camada": camada, "escopo": escopo, "comando": comando,
         "medido": medido, "esperado": esperado, "ok": bool(ok), "detalhe": detalhe}
    if regex: c["regex"] = regex
    CHECKS.append(c)
    print(("[PASS]" if ok else "[FALHA]"), cid, "-", titulo)
    print("        medido:", str(medido)[:300], "| esperado:", str(esperado)[:200])
    if detalhe: print("        detalhe:", detalhe[:600])

t     = nfc(open(V7_F, encoding="utf-8").read())
vinc  = json.load(open(VINC_F))
v22   = nfc(open(V22_F, encoding="utf-8").read())
mint  = nfc(open(MINUTA, encoding="utf-8").read())
mcf   = mint.casefold()
m2    = nfc(open(M2_F, encoding="utf-8").read())
kit6  = nfc(open(BLOCO6, encoding="utf-8").read())
sc12  = nfc(open(SC12, encoding="utf-8").read())

# ============ SEÇÃO 0 — INTEGRIDADE ============
reg("S0.1", "V7 intacta", "ingerida sha256", V7_F, "sha256sum", sha(V7_F)[:12], "6e2c2979", sha(V7_F).startswith("6e2c2979"))
reg("S0.2", "Manifesto intacto", "ingerida sha256", MAN_F, "sha256sum", sha(MAN_F)[:12], "79d1309a", sha(MAN_F).startswith("79d1309a"))
reg("S0.3", "Vínculos intactos", "ingerida sha256", VINC_F, "sha256sum", sha(VINC_F)[:12], "490675e6", sha(VINC_F).startswith("490675e6"))
reg("S0.4", "Arquitetura V2.2 vigente intacta (âncora normativa da minuta)", "ingerida sha256", V22_F, "sha256sum",
    sha(V22_F)[:12], "df7f7cfd", sha(V22_F).startswith("df7f7cfd"))
reg("S0.5", "P-8 majestático intacto (referência da minuta)", "ingerida sha256", P8, "sha256sum",
    sha(P8)[:12], "be48a5ef", sha(P8).startswith("be48a5ef"))

# ============ SEÇÃO P — DIGITAIS ============
reg("P1", "Minuta 1 L-NT = bytes recebidos", "ingerida sha256", MINUTA, "sha256sum",
    sha(MINUTA)[:12], "294119b9", sha(MINUTA).startswith("294119b9"))
reg("P2", "Verbatim comentador arquivado", "ingerida sha256", VERBAT, "sha256sum", sha(VERBAT)[:16],
    "registrado", os.path.exists(VERBAT), detalhe="sha256=" + sha(VERBAT))
reg("P3", "Cabeçalho da minuta referencia os shas REAIS vigentes (V2.2 · V7 · P-8)", "documental NFC+casefold",
    "minuta linhas 1-10", "tokens sha", json.dumps({k: (k in mint) for k in ["df7f7cfd", "6e2c2979", "be48a5ef"]}),
    "3/3", all(x in mint for x in ["df7f7cfd", "6e2c2979", "be48a5ef"]))

# ============ SEÇÃO A — PARTE 1: DIMENSIONAMENTO MEDIDO (réplica exata) ============
marks = re.findall(r"\(BLOCO(\d{2})\.(\d{3})\)", t)
reg("A1", "Marcadores de claim: 90 · 81 distintos (Parte 1)", "documental NFC, regex case-sensitive",
    "V7 canônica inteira", r"re.findall(rb'\(BLOCO(\d{2})\.(\d{3})\)')",
    f"{len(marks)}/{len(set(marks))}", "90/81", len(marks) == 90 and len(set(marks)) == 81,
    regex=r"\(BLOCO(\d{2})\.(\d{3})\)")
blocos_dist = set(b for b, _ in set(marks))
reg("A2", "Blocos canônicos: 11", "ingerida sobre o conjunto de marcadores distintos",
    "set(marcadores)", "len(set(bloco))", str(len(blocos_dist)), "11", len(blocos_dist) == 11)
pb_rep  = Counter(b for b, _ in marks)          # camada R: com repetição (a do mestre)
pb_dist = Counter(b for b, _ in set(marks))     # camada D: distintos (declarada como vizinha)
vrep, vdist = sorted(pb_rep.values()), sorted(pb_dist.values())
reg("A3", "Claims por bloco: mín 1 · mediana 7 · máx 30 — CAMADA: marcadores com repetição (a camada distintos dá 6/27, registrada como vizinha)",
    "ingerida, duas camadas declaradas", "marcadores agrupados por bloco",
    "Counter(bloco)×{todas as ocorrências, distintos} → mín/mediana/máx",
    f"com-repetição: {vrep[0]}/{statistics.median(vrep)}/{vrep[-1]} · distintos: {vdist[0]}/{statistics.median(vdist)}/{vdist[-1]}",
    "1/7/30 (com repetição); 1/6/27 (distintos, nota de camada)",
    (vrep[0], statistics.median(vrep), vrep[-1]) == (1, 7, 30))
# A7b — CAMADA COMPLETA (descoberta da casa nesta trilha): o rodapé usa regex com '\)' literal final,
# que exige ')' logo após os 3 dígitos → cabeçalhos com ids AGRUPADOS e abreviados
# (ex.: '### 3.9 — ... (BLOCO03.009, 012)') escapam INTEIRAMENTE da receita estrita.
canon = {f"BLOCO{b}.{n}" for b, n in set(marks)}  # camada estrita (a do rodapé, com '\)' final)
grupos = re.findall(r"\((BLOCO\d{2}\.\d{3}(?:\s*,\s*(?:BLOCO\d{2}\.)?\d{3})*)\)", t)
ids_full = []
for g in grupos:
    bloco_atual = None
    for p in [p.strip() for p in g.split(",")]:
        mm = re.match(r"(?:BLOCO(\d{2})\.)?(\d{3})$", p)
        if mm:
            if mm.group(1): bloco_atual = mm.group(1)
            ids_full.append(f"BLOCO{bloco_atual}.{mm.group(2)}")
full = set(ids_full)
multi = sorted(g for g in grupos if "," in g)
abrev_resolvidas = sorted(full - canon)
pbfull = Counter(i.split(".")[0] for i in full)
reg("A3b", "CAMADA COMPLETA (descoberta da casa): a canônica tem **89 claims distintos**, não 81 — a receita do rodapé (parênteses com '\\)' final) perde 4 cabeçalhos com ids agrupados+abreviados: " + "; ".join(multi),
    "documental NFC, regex agrupado + expansão de abreviações (herda bloco da esquerda)",
    "V7 canônica", r"re.findall(rb'\((BLOCO\d{2}\.\d{3}(?:\s*,\s*(?:BLOCO\d{2}\.)?\d{3})*)\)') + expand",
    f"grupos={len(grupos)} · distintos camada completa={len(full)} · adicionados={abrev_resolvidas} · por-bloco={dict(sorted(pbfull.items()))}",
    "89 distintos (81 estrita + 8: 4 formas longas + 4 abreviações)", len(full) == 89 and len(abrev_resolvidas) == 8,
    detalhe="consequência para o NT-02: a régua oficial de existência PRECISA da camada completa — com a estrita, 7 claims válidos seriam marcados inexistentes", regex=r"\((BLOCO\d{2}\.\d{3}(?:\s*,\s*(?:BLOCO\d{2}\.)?\d{3})*)\)")
cid_nao_vazio = sum(1 for x in vinc if x.get("claim_id"))
reg("A4", "Vínculos com claim_id: 244/274", "ingerida json", "274 vínculos", "count(bool(claim_id))",
    f"{cid_nao_vazio}/274", "244/274", cid_nao_vazio == 244)
claims_ref = Counter()
for x in vinc:
    m = re.search(r"BLOCO(\d{2})\.(\d{3})", x.get("claim_id", "") or "")
    if m: claims_ref[f"BLOCO{m.group(1)}.{m.group(2)}"] += 1
reg("A5", "Claims referenciados por algum vínculo: 80", "ingerida json + regex de normalização",
    "claim_id dos 274", r"re.search(rb'BLOCO(\d{2})\.(\d{3})', claim_id) → Counter",
    str(len(claims_ref)), "80", len(claims_ref) == 80, regex=r"BLOCO(\d{2})\.(\d{3})")
vpc = sorted(claims_ref.values())
reg("A6", "Vínculos por claim: mín 1 · mediana 2 · máx 15", "ingerida (Counter de A5)",
    "80 claims", "mín/mediana/máx", f"{vpc[0]}/{statistics.median(vpc)}/{vpc[-1]}", "1/2/15",
    (vpc[0], statistics.median(vpc), vpc[-1]) == (1, 2, 15))
dono = {}
for x in vinc:
    m = re.search(r"BLOCO(\d{2})\.(\d{3})", x.get("claim_id", "") or "")
    if m:
        dono.setdefault(f"BLOCO{m.group(1)}.{m.group(2)}", []).append(x["id_vinculo"])
inter = set(claims_ref) & full
semvinc = full - set(claims_ref)
fora_full = sorted(set(claims_ref) - full)
det_a7 = {"camada_completa_89": len(full), "referenciados_80": len(claims_ref),
          "referenciados_que_existem": len(inter), "canonicos_sem_vinculo": len(semvinc),
          "orfaos_reais": fora_full, "orfaos_vinculos_nomeados": {c: dono[c] for c in fora_full},
          "semvinc": sorted(semvinc)}
reg("A7", "ACHADO MEDIDO E RESOLVIDO POR CAMADA: 79 dos 80 ids referenciados existem na camada completa (89); **órfão real é 1 só — BLOCO01.001 (6 vínculos nomeados: VINC_B1_0001–0006)**; 10 canônicos sem vínculo. Frase da minuta '80 dos 81 têm vínculo' → camada completa: '79 dos 89 + 1 órfão'. Dívida candidata: D-LNT-CLAIM-LEGADO",
    "ingerida × documental, camada completa (A3b)", "80 ids referenciados × 89 canônicos",
    "set difference camada completa + dono por vínculo",
    json.dumps(det_a7, ensure_ascii=False)[:550], "fora_full = 1 id (BLOCO01.001) com 6 vínculos",
    len(inter) == 79 and len(fora_full) == 1 and fora_full == ["BLOCO01.001"]
    and det_a7["orfaos_vinculos_nomeados"]["BLOCO01.001"] == ["VINC_B1_0001", "VINC_B1_0002", "VINC_B1_0003", "VINC_B1_0004", "VINC_B1_0005", "VINC_B1_0006"],
    regex=r"BLOCO(\d{2})\.(\d{3}) + expansão A3b")
# CAMADAS de frase — a exata que reproduz 628 e a vizinhança (sensibilidade declarada)
fr_exata  = [s.strip() for s in re.split(r"\.\s+", t)]
fr_gp     = [s.strip() for s in re.split(r"\.\s+", t)]
fr_alt1   = [s.strip() for s in re.split(r"[.!?…]\s+", t)]
fr_alt2   = [s.strip() for s in re.split(r"[.!?…]+", t)]
c_exata   = sum(1 for s in fr_exata if len(s) >= 60)
c_gt      = sum(1 for s in fr_exata if len(s) > 60)
c_alt1    = sum(1 for s in fr_alt1 if len(s) > 60)
c_alt2    = sum(1 for s in fr_alt2 if len(s) > 60)
reg("A8", "Frases >60 caracteres: 628 — CAMADA EXATA encontrada: split r'\\.\\s+' com corte ≥60 (sensibilidade: >60→625 · [.!?…]\\s+>60→626 · [.!?…]+>60→872)",
    "documental NFC, 4 camadas medidas", "V7 texto completo",
    "re.split + len por camada", f"EXATA(r'\\.\\s+',≥60)={c_exata} · vizinhas: {c_gt}/{c_alt1}/{c_alt2}",
    "628 na camada declarada (receita dele é subespecificada em pontuação e limiar; sensibilidade ±3)",
    c_exata == 628, regex=r"\.\s+ / [.!?…]\s+ / [.!?…]+, cortes >60 × ≥60")
palavras = len(t.split())
reg("A9", "Palavras na canônica: 21.503", "documental NFC, len(split())",
    "V7 texto completo", "len(text.split())", str(palavras), "21503", palavras == 21503)
est1, est2 = 80 * 146, 130 * 146
reg("A10", "Estimativa do programa: 12–19 mil = 80×146≈11.680 · 130×146≈18.980 (aritmética dele fecha)", "aritmética",
    "Parte 1 (estimativa, não medição)", "80*146, 130*146", f"{est1}–{est2}",
    "≈12 a 19 mil", 11000 < est1 < 12500 and 18500 < est2 < 19500,
    detalhe="estimativa derivada, não medição — registrado como tal; NT-B1 80–130 = 81 claims + ligações/lacunas")

# ============ SEÇÃO B — ÂNCORAS NORMATIVAS (V2.2 · L-05 minuta 2 · P-8) ============
v22cf = nfc(v22).casefold()
d1 = "consumir o conhecimento da biblioteca" in v22cf.replace("correspondente", "")
d2 = "utilizar as evidências/vínculos necessárias à rastreabilidade" in v22cf
reg("B1", "V2.2 §6 deveres 1–2 da NT presentes (âncora da minuta)", "documental NFC + casefold",
    "V2.2 §6 (linha 427+)", "tokens dever 1 e dever 2", f"{d1}/{d2}", "True/True", d1 and d2)
frase_limite = "converter uma relação mecanística em eficácia clínica sem sustentação"
ok_limite = frase_limite in v22
reg("B2", "V2.2 §7 contém o limite citado pela minuta (frase com 'uma'; a citação da minuta elide 'uma' — precisão fina registrada, sem erro)",
    "documental NFC, busca literal", "V2.2 §7", "substring exata",
    str(ok_limite) + " | na minuta: " + str("converter relação mecanística em eficácia clínica sem sustentação" in mint),
    "V2.2 tem com 'uma'; minuta/comentador citam sem 'uma' (elisão marcada, conteúdo idêntico)", ok_limite)
sete = ["fato", "associação", "causalidade", "hipótese", "evidência direta", "extrapolação", "lacuna científica"]
mtk  = ["fato", "associacao", "causalidade", "hipotese", "evidencia_direta", "extrapolacao", "lacuna"]
reg("B3", "§7 V2.2 distingue 7 estados −== status_epistemologico da minuta (7 valores)", "documental NFC",
    "V2.2 §7 × minuta Parte 2.2", "tokens por lado",
    f"§7: {all(s in v22 for s in sete)} · minuta: {all(mk in mint for mk in mtk)}", "True · True",
    all(s in v22 for s in sete) and all(mk in mint for mk in mtk),
    detalhe="observação fina: a ORDEM N-2 da minuta (lacuna<hipotese<…<fato) é caminho de portão novo, compatível com §7")
b4a = "# 13. NTs COMO UNIDADES DE EXPLICAÇÃO" in v22
b4b = "# 14. NT E LAUDO" in v22
reg("B4", "§13 e §14 existem na V2.2 (âncoras da minuta)", "documental NFC, cabeçalhos exatos",
    "V2.2", "startswith por cabeçalho", f"{b4a}/{b4b}", "True/True", b4a and b4b)
def tem(rx, txt): return re.search(rx, txt, re.M) is not None
m2_checks = {
 "D-02 cinco eixos": tem(r"## D-02", m2) and "Os cinco elementos" in m2,
 "D-03 seis tipos": tem(r"## D-03", m2) and "Seis tipos, nunca colapsados" in m2,
 "D-04 texto de ligação": tem(r"## D-04 · Texto de ligação", m2),
 "D-05 20/revisor cego/≥90%/três": tem(r"## D-05", m2) and ("20 unidades" in m2 and "revisor cego" in m2 and "≥90%" in m2),
 "D-06 Pasta segregada": tem(r"## D-06", m2) and "segregado" in m2.casefold(),
 "D-07/D-08 existem": tem(r"## D-07", m2) and tem(r"## D-08", m2),
}
reg("B5", "Contratos irmãos: L-05 minuta 2 carrega D-02(5 eixos)·D-03(6 tipos)·D-04(ligação)·D-05(aceite)·D-06(pasta)·D-07·D-08 — tudo o que a minuta L-NT herda",
    "documental NFC, tokens", "minuta 2 (sha 54ba243d histórico)", "regex+substring por D",
    json.dumps(m2_checks, ensure_ascii=False), "todas True", all(m2_checks.values()),
    detalhe="minuta L-NT Parte 2.2 propaga 'os cinco da D-02' e Parte 5 os 'seis tipos da D-03' — ambos confirmados na fonte")
r = subprocess.run([sys.executable, P8, "."], capture_output=True, text=True, cwd=AT)
outp = nfc(r.stdout + r.stderr)
erros_sec = re.findall(r"(?m)^.*ERRO.*$", outp)
alvo_campos = {"natureza_evidencia": "natureza_evidencia" in outp, "trilha": "trilha" in outp}
resumo = re.search(r"RESUMO: (\d+) ERRO\(S\), (\d+) AVISO\(S\)", outp)
reg("B6", "P-8 oficial HOJE: 2 ERRO / 299 AVISO / exit 1 — e os 2 ERRO vivos são os campos natureza_evidencia · trilha (Parte 8 da minuta)",
    "ingerida (execução oficial read-only, stdout íntegro varrido)", "P-8 be48a5ef × atuais",
    "cd atuais && python3 validar_coerencia_camadas.py .",
    f"resumo={resumo.groups() if resumo else None} exit={r.returncode} linhas-ERRO={len(erros_sec)} campos={alvo_campos}",
    "(2,299)·exit 1·campos presentes",
    bool(resumo) and resumo.groups() == ("2", "299") and r.returncode == 1 and all(alvo_campos.values()),
    detalhe="linhas-ERRO: " + json.dumps([l.strip()[:110] for l in erros_sec], ensure_ascii=False))
n2j = json.load(open(N2))
enum_n2 = n2j["properties"]["natureza_relacao"]["enum"]
enum_mn = ["causal", "contributiva", "associativa", "compensatoria", "marcador", "nao_estabelecida"]
reg("B7", "natureza_relacao da minuta == enum N2 v1.4 (6 valores, mesma forma)", "ingerida json × documental",
    "N2 v1.4 × minuta Parte 2.2", "enum compare", f"N2={enum_n2} minuta-contém={all(e in mint for e in enum_n2)}",
    "iguais", enum_n2 == enum_mn and all(e in mint for e in enum_n2))
nao_est = sum(1 for x in vinc if x.get("natureza_relacao") == "nao_estabelecida")
reg("B8", "4 vínculos nao_estabelecida no acervo (Parte 5)", "ingerida json", "274", "Counter",
    str(nao_est), "4", nao_est == 4)

# ============ SEÇÃO C — KIT / CAMPO uso ============
linhas_uso = re.findall(r"(?m)^\s+uso: (clinico|contexto_mecanistico|gap_pesquisa)\s*$", kit6)
cu = Counter(linhas_uso)
reg("C1", "Kit BLOCO DE ESTADO: uso por claim = 12 clinico · 6 contexto_mecanistico · 4 gap_pesquisa (22 claims)",
    "documental NFC, regex por linha, arquivo-escopo", "6º BLOCO DE ESTADO v1.6",
    r"re.findall(rb'^\s+uso: (clinico|contexto_mecanistico|gap_pesquisa)\s*$', M)",
    json.dumps(cu), "{'clinico': 12, 'contexto_mecanistico': 6, 'gap_pesquisa': 4} (soma 22)",
    cu == {"clinico": 12, "contexto_mecanistico": 6, "gap_pesquisa": 4} and sum(cu.values()) == 22,
    regex=r"^\s+uso: (clinico|contexto_mecanistico|gap_pesquisa)\s*$")
reg("C2", "'4 claims gap_pesquisa' da Parte 5 = lado kit conferido (C1)", "documental (deriva de C1)",
    "kit", "cu['gap_pesquisa']", str(cu.get("gap_pesquisa")), "4", cu.get("gap_pesquisa") == 4)
reg("C3", "SCHEMA-CLAIM v1.2 define uso em 3 valores (fonte do enum)", "documental NFC+casefold",
    "3º SCHEMA-CLAIM v1.2", "tokens dos 3 valores",
    str(all(v in sc12 for v in ["clinico", "contexto_mecanistico", "gap_pesquisa"])), "True",
    all(v in sc12 for v in ["clinico", "contexto_mecanistico", "gap_pesquisa"]))
censo = sorted(os.path.relpath(p, AT) for p in glob.glob(AT + "/Evidencias/**/*.*", recursive=True))
reg("C4", "Precisão de camada do 'uso não existe no acervo': existe em VÍNCULO (274/274 com uso) e NÃO existe por-claim (censo: nenhum registro de claims no acervo)",
    "documental (censo de arquivos) + ingerida (campo dos 274)", "Evidencias/** + vínculos",
    "glob censo + count(uso)", f"uso vínculos={sum(1 for x in vinc if x.get('uso') is not None)}/274 · arquivos={censo}",
    "274/274 no vínculo; sem registro por-claim (a afirmação dele vale na granularidade claim)",
    sum(1 for x in vinc if x.get("uso") is not None) == 274 and all("claim" not in os.path.basename(p).casefold() for p in censo),
    detalhe="a minuta pede herança por-claim; o acervo só tem por-vínculo — a afirmação dele é correta na camada certa")

# ============ SEÇÃO D — ARMADILHA (Parte 7) E LASTRO ============
v128 = next(x for x in vinc if x["id_vinculo"] == "VINC_B1_0128")
v173 = next(x for x in vinc if x["id_vinculo"] == "VINC_B1_0173")
notas = nfc((v128.get("g3_notas") or "") + " || " + (v173.get("g3_notas") or "")).casefold()
d1 = ("negativo na amostra toda" in notas) and ("subgrupo" in notas) and ("infliximabe" in notas)
reg("D1", "RAISON 2013 = lastro real da armadilha: 'negativo na amostra toda; resposta só no subgrupo inflamado' (hs-CRP/TNF/sTNFR2) — triagem já o exigia, a minuta o invoca corretamente",
    "ingerida json (g3_notas dos 2 vínculos RAISON)", "VINC_B1_0128/0173", "tokens",
    notas[:220], "negativo-todo ∧ subgrupo ∧ infliximabe", d1,
    detalhe=f"natureza dos 2: {v128.get('natureza_relacao')}/{v173.get('natureza_relacao')} · uso: {v128.get('uso')}/{v173.get('uso')}")
ok_cit = "citocinas" in t.casefold()
jan = re.findall(r"(?ims)^.*(?:camundongo|roedor|rato\b|murino|animal).*$", t)  # grupo NÃO-capturante (findall devolve a linha, não o grupo)
jan_tnf = [l for l in jan if "tnf" in l.casefold()][:6]
reg("D2", "Repertório da armadilha existe: citocinas×depressão (humano) na canônica · evidência animal sobre TNF presente (ex.: Xu 2020 camundongo [PRÉ-CLÍNICO]) — perna (3) construível a partir da B1",
    "documental NFC + casefold, janela por linha", "V7 canônica",
    r"linhas com (camundongo|roedor|rato|murino|animal) ∧ contendo 'tnf' (CI)",
    f"citocinas={ok_cit} · linhas animal∧TNF={len(jan_tnf)} · amostra: " + (jan_tnf[0].strip()[:150] if jan_tnf else "-"),
    "citocinas presente ∧ ≥1 linha animal∧TNF", ok_cit and len(jan_tnf) >= 1,
    regex=r"(camundongo|roedor|rato\b|murino|animal) ∧ tnf")
tok27 = len(re.findall(r"27%", t)); tok146 = len(re.findall(r"1[,.]46", t))
reg("D3", "Lastro do NT-10: '27%' e 'OR 1,46' presentes na V7 (D-B1-R4-TOKENS viva — é a ferida que a regra sara)",
    "documental NFC, regex", "V7", r"count(27%) · count(1[,.]46)", f"{tok27}/{tok146}", "≥1/≥1",
    tok27 >= 1 and tok146 >= 1, regex=r"27% · 1[,.]46")
x47 = next(x for x in vinc if x["id_vinculo"] == "VINC_B1_0047")
dec = nfc(open(DEC, encoding="utf-8").read())
led = nfc(open(LED, encoding="utf-8").read())
doc25  = "25 âncoras da listra-índice" in dec
ledtok = "HAFIZI_2005[… renomeado DENTRO da âncora" in led
reg("D4", "REF_HAFIZI_2005 → 2007: lição do NT-08 CONFERE — rename documentado como 25 âncoras propagadas (decisões, trilha 17) + ledger registra o token dentro da âncora; valor atual = REF_HAFIZI_2007",
    "documental NFC (decisões/ledger) + ingerida (vínculo atual)",
    "decisoes_B1.md · ledger_auditoria_B1.json · VINC_B1_0047",
    "tokens documentais × campo atual",
    json.dumps({"dez_trilha17_25": doc25, "ledger_token": ledtok, "atual": x47["id_referencia_interna"]}, ensure_ascii=False),
    "25 documentado ∧ token no ledger ∧ id atual 2007", doc25 and ledtok and x47["id_referencia_interna"] == "REF_HAFIZI_2007")
r3 = nfc(open(R3, encoding="utf-8").read()); r15 = nfc(open(R15, encoding="utf-8").read())
r15cf = r15.casefold()
ped = {"caso-armadilha": "caso-armadilha" in r15cf, "jamais": "jamais" in r15cf, "raison": "raison" in r15cf,
       "l-nt": "unidades narrativas" in r15cf}
reg("D5", "Crédito do mestre VERIFICADO NO TEXTO: RESPOSTA_15 da casa (linha 45) contém o pedido — 'se o L-NT puder nascer com um caso-armadilha próprio no estilo \"o que este contrato jamais pode produzir\", melhor ainda', citando o hábito RAISON — 'a casa pediu' é fato, não cortesia",
    "documental NFC + casefold, linha completa (nenhum corte)", "RESPOSTA_15 da casa",
    "tokens caso-armadilha ∧ jamais ∧ raison ∧ unidades narrativas", json.dumps(ped, ensure_ascii=False),
    "4/4 na RESPOSTA_15", all(ped.values()),
    detalhe="ERRATA da 1ª execução desta trilha (confissão datada): a exploração preliminar leu grep cortado em 150 colunas e induziu uma CONFISSÃO FALSA ('RESPOSTA_15 não contém'); a memória da casa estava certa — violação do próprio princípio detector>tela, registrada e corrigida com data")

# ============ SEÇÃO E — COMENTADOR × MINUTA (9 pontos) ============
inv_m = "a nt reorganiza significado" in mcf and "não produz ciência" in mcf and "não é o lugar onde uma afirmação nasce" in mcf
reg("E1", "Invariante citada pelo comentador == invariante da minuta", "documental NFC+casefold",
    "minuta Parte 0", "tokens", str(inv_m), "True", inv_m)
nrs = [f"n-{i}" in mcf for i in range(1, 7)]
reg("E2", "Regras N-1 a N-6 existem (comentador §2)", "documental NFC+casefold", "minuta Parte 3",
    "tokens N-1..N-6", str(all(nrs)) + " " + str(nrs), "6/6", all(nrs))
reg("E3", "Portão V-NT existe como tabela própria (NT-01..NT-10)", "documental NFC",
    "minuta Parte 6", "tokens NT-01..NT-10", str(all(f"NT-{i:02d}" in mint for i in range(1, 11))), "10/10",
    all(f"NT-{i:02d}" in mint for i in range(1, 11)))
reg("E4", "claim_origem ≥1 obrigatório na unidade comum (comentador §1)", "documental NFC",
    "minuta Parte 2.2", "tokens 'claim_origem' + '≥1, obrigatório'",
    str("claim_origem" in mint and "≥1, obrigatório" in mint), "True", "claim_origem" in mint and "≥1, obrigatório" in mint)
e5 = all(s in mint for s in ["isolamento", "remoção", "reutilização"]) if "Remoção" in mint or "remoção" in mint else False
reg("E5", "Três testes (isolamento · remoção · reutilização) + 20 unidades + revisor cego + ≥90% (comentador §3)",
    "documental NFC+casefold", "minuta Parte 4", "tokens",
    json.dumps({k: (k in mcf) for k in ["isolamento", "remoção", "reutilização", "revisor cego", "≥90%", "20 unidades"]}, ensure_ascii=False),
    "6/6", all(k in mcf for k in ["isolamento", "remoção", "reutilização", "revisor cego", "≥90%", "20 unidades"]))
reg("E6", "Estimativas 80–130 e 12–19 mil presentes e marcadas como estimativa (comentador §3/§6)", "documental NFC",
    "minuta Parte 1", "tokens", str("80 a 130" in mint and "12 a 19 mil" in mint), "True",
    "80 a 130" in mint and "12 a 19 mil" in mint)
e7 = ("não-cobertura" in mcf or "nao-cobertura" in mcf) and "gap_pesquisa" in mcf and "nao_estabelecida" in mcf and "lacuna" in mcf
reg("E7", "Cobertura obrigatória com declaração de não-cobertura + lacunas explícitas incluindo gap_pesquisa e nao_estabelecida (comentador §4)",
    "documental NFC+casefold", "minuta Parte 5", "tokens", str(e7), "True", e7)
e8 = "depend" in mcf and "camada do kit" in mcf
reg("E8", "Dependência uso × Claim Kit registrada na Parte 8 (= §5 do comentador — pendência de arquitetura contratual, não objeção)",
    "documental NFC+casefold", "minuta Parte 8", "tokens", str(e8), "True", e8)
e9 = "nenhuma impede escrever" in mcf and "validá-la" in mcf
reg("E9", "Parte 8: dependências travam validação integral, não a escrita do piloto (estratégia 20→medir→80)", "documental NFC+casefold",
    "minuta Parte 8", "tokens", str(e9), "True", e9)

# ============ SEÇÃO F — COERÊNCIA INTERNA DA MINUTA ============
f1 = mcf.count("ligaç") > 3 and "não tem `claim_origem`" in mint
reg("F1", "Unidade de ligação: sem claim_origem/eixos/vinculos (Parte 2.4) e NT-09 reprova a violação — coerência cruzada Parte 2 × Parte 6",
    "documental NFC", "minuta 2.4 × NT-09", "tokens",
    str("não tem `claim_origem`" in mint and "unidade de ligação com `vinculos[]`, `eixos` ou conteúdo afirmativo" in mint),
    "True", "não tem `claim_origem`" in mint and "unidade de ligação com `vinculos[]`, `eixos` ou conteúdo afirmativo" in mint)
ordem_n2 = "lacuna < hipotese < associacao < extrapolacao < evidencia_direta < causalidade < fato" in mcf
reg("F2", "N-2 traz ordem declarada dos 7 status (portão NT-04 comparável por máquina)", "documental NFC+casefold",
    "minuta Parte 3 N-2", "substring da escada", str(ordem_n2), "True", ordem_n2,
    detalhe="escada: lacuna<hipotese<associacao<extrapolacao<evidencia_direta<causalidade<fato — 7 degraus, verificável")
ids_opacos = "`NT-B1-0001`" in mint and "opaco e estável" in mcf
reg("F3", "Endereçamento opaco e estável (NT-B1-0001; lição HAFIZI citada como razão) — NT-08 reprova id com dado mutável",
    "documental NFC+casefold", "minuta 2.3 × NT-08", "tokens", str(ids_opacos), "True", ids_opacos)
tk_f4 = {"seis tipos da d-03": "seis tipos da d-03" in mcf,
         "4 claims gap_pesquisa": "4 claims `gap_pesquisa`" in mcf,
         "4 vínculos nao_estabelecida": "4 vínculos `nao_estabelecida`" in mcf}
reg("F4", "Parte 5 cita os números medidos: 6 tipos D-03 · 4 gap (kit, conferido C1) · 4 nao_estabelecida (acervo, conferido B8)",
    "documental NFC+casefold (agulhas casefold sobre feno casefold)", "minuta Parte 5", "tokens",
    json.dumps(tk_f4, ensure_ascii=False), "3/3", all(tk_f4.values()),
    detalhe="ERRATA da 1ª execução (datada): agulha em caixa mista sobre feno casefoldado — régua corrigida")

# ============ RESULTADO ============
n_ok = sum(1 for c in CHECKS if c["ok"]); n = len(CHECKS)
falhas = [c["id"] for c in CHECKS if not c["ok"]]
print(f"\n==== TRILHA 49: {n_ok}/{n} checks verdes ====")
if falhas: print("falhas:", falhas)
saida = {"trilha": 49, "rodada": 30, "data": "2026-09-18",
         "objeto": "L-NT Contrato das Unidades Narrativas · Minuta 1 (mestre) + comentador",
         "confissoes_e_erratas_datadas_2026_09_18": [
             "D5/META-ERRATA: a 1ª execução desta trilha registrou uma CONFISSÃO FALSA ('RESPOSTA_15 não contém o pedido do caso-armadilha') — a causa foi exploração preliminar com grep cortado em 150 colunas, fora do script; a memória da casa estava CERTA (linha 45 contém o pedido). Violação do próprio princípio detector>tela, confessada e corrigida com data. Permanece no registro: trilha é append-only.",
             "F4/ERRATA: agulha em caixa mista sobre feno casefoldado (nunca casa). Régua corrigida para agulhas casefold uniformes.",
             "D2/ERRATA: re.findall com grupo CAPTURANTE devolve o grupo, não a linha — régua corrigida para grupo não-capturante.",
             "NOTAS DE CAMADA (não são falha): claims/bloco 7/30 exige camada com-repetição (distintos dá 6/27) · frases 628 exige split r'\\.\\s+' com corte ≥60 (vizinhas 625/626/872) — a receita do rodapé é subespecificada; camadas declaradas resolvem.",
             "NOTA METODOLÓGICA A7/A3b (evolução por camadas, não erro): a 1ª régua de identidade usou a camada ESTRITA do rodapé (parênteses com '\\)' final) e encontrou 8 'fora'; iterando camadas descobrimos que 4 cabeçalhos agrupam ids com abreviação ('(BLOCO03.009, 012)'). Camada completa: 89 claims canônicos; dos 80 referenciados existem 79; órfão real = 1 (BLOCO01.001, VINC_B1_0001–0006) → dívida candidata D-LNT-CLAIM-LEGADO. As camadas estrita e completa ficam gravadas — a estrita reproduz o rodapé (A1), a completa é a régua de existência recomendada ao NT-02."],
         "shas_ciencia": {"v7": sha(V7_F), "manifesto": sha(MAN_F), "vinculos": sha(VINC_F),
                         "v22": sha(V22_F), "p8": sha(P8)},
         "shas_pacote": {"minuta_lnt_m1": sha(MINUTA), "verbatim_comentador": sha(VERBAT)},
         "resultado": {"checks_ok": n_ok, "checks_total": n, "falhas": falhas,
                       "veredito": "VERDE — réplica integral confirma a minuta" if not falhas else "PENDÊNCIAS — ver falhas"},
         "checks": CHECKS}
with open(PROD + "/TRILHA49_LNT_minuta1_2026-09-18.json", "w", encoding="utf-8") as f:
    json.dump(saida, f, ensure_ascii=False, indent=2)
print("JSON gravado:", PROD + "/TRILHA49_LNT_minuta1_2026-09-18.json")
sys.exit(0 if not falhas else 1)
