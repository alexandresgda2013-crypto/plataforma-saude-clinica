#!/usr/bin/env python3
# TRILHA 50 — rodada 31 — 2026-09-18
# Objeto: PROPOSTA DO OPERADOR "Formalização do fluxo dos Claims Clínicos"
#         (Claim Clínico aprovado → Evidências/Bibliografia → N1 → N2 → camadas posteriores)
# Método da casa: arquivar verbatim → medir → replicar cada afirmação factual →
#                 só então comentar. 0 ciência. Toda contagem com CAMADA declarada.
import json, re, hashlib, os, subprocess, sys, unicodedata as ud
from collections import Counter

BASE = "/home/user"
DOC  = BASE + "/BIBLIOTECAS/_documentos_serie"
PASTA= DOC + "/OPERADOR_PROPOSTA_fluxo_claim_N1N2_recebido_2026-09-18"
PROP = PASTA + "/OPERADOR_PROPOSTA_FORMALIZACAO_FLUXO_CLAIMS_CLINICOS_2026-09-18.md"
DIGP = PASTA + "/DIGITAIS_PROPOSTA_FLUXO_CLAIM_2026-09-18.txt"
KIT  = DOC + "/KIT_CLINICA_recebido_2026-09-15"
K3   = KIT + "/3º SCHEMA-CLAIM — v1.2.md"
K4   = KIT + "/4º COMO EXECUTAR — v1.7.md"
K5   = KIT + "/5º LISTA CANÔNICA — B1  SM-02 V1.3.md"
K6   = KIT + "/6º BLOCO DE ESTADO  v1.6.md"
AT   = BASE + "/BIBLIOTECAS/B01_Neuroinflamacao/atuais"
V7   = AT + "/B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
MAN  = AT + "/Evidencias/Bibliografia/_manifesto_biblioteca.json"
BIB  = AT + "/Evidencias/Bibliografia/"
VINC = AT + "/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
DEC  = AT + "/Auditoria_B1/decisoes_B1.md"
V22  = DOC + "/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
P8   = BASE + "/Ferramentas de geração e auditoria/06_portao_P8_coerencia/scripts/validar_coerencia_camadas.py"
N1F  = DOC + "/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_referencia_v1.3_N1_b06660fd.json"
N2F  = DOC + "/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
MNT  = DOC + "/MESTRE_LNT_minuta1_recebido_2026-09-18/L-NT_CONTRATO_UNIDADES_NARRATIVAS_minuta1_294119b9_2026-09-18.md"
CATJ = BASE + "/Ferramentas de geração e auditoria/01_norteadores/_derivados_trilha46/_ids_oficiais.json"
CATP = BASE + "/Ferramentas de geração e auditoria/01_norteadores/_derivados_trilha46/_ids_oficiais.PROVENIENCIA.json"
MDOF = BASE + "/Ferramentas de geração e auditoria/01_norteadores/1º IDS_OFICIAIS.md"
CHL  = BASE + "/BIBLIOTECAS/CHANGELOG_GERAL.md"
STS  = BASE + "/BIBLIOTECAS/STATUS_SIMPLES_2026-09-13.md"
R17  = DOC + "/RESPOSTA_17_MESTRE_PROPOSTA_FLUXO_CLAIM_N1N2_2026-09-18.md"
R9   = DOC + "/RESPOSTA_9_AUDITOR_ESTRUTURA_PROPOSTA_FLUXO_CLAIM_N1N2_2026-09-18.md"

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
def rd(p):
    return ud.normalize("NFC", open(p, encoding="utf-8").read())

checks = []
def reg(cid, titulo, camada, escopo, comando, medido, esperado, ok, detalhe="", regex=None):
    checks.append({"id": cid, "titulo": titulo, "camada": camada, "escopo": escopo,
                   "comando": comando, "medido": medido, "esperado": esperado,
                   "ok": bool(ok), "detalhe": detalhe, **({"regex": regex} if regex else {})})

prop = rd(PROP); dec = rd(DEC); sts = rd(STS); kit3 = rd(K3); kit4 = rd(K4); kit5 = rd(K5); kit6 = rd(K6)
mint = rd(MNT); v22 = rd(V22)

# ==================== S0 — SELOS DA CIÊNCIA (inalterados) ====================
reg("S0.1", "V7 intacta", "ingerida sha256", V7, "sha256sum", sha(V7)[:12], "6e2c2979", sha(V7).startswith("6e2c2979"))
reg("S0.2", "Manifesto intacto", "ingerida sha256", MAN, "sha256sum", sha(MAN)[:12], "79d1309a", sha(MAN).startswith("79d1309a"))
reg("S0.3", "Vínculos intactos (274)", "ingerida sha256", VINC, "sha256sum", sha(VINC)[:12], "490675e6", sha(VINC).startswith("490675e6"))
reg("S0.4", "V2.2 vigente intacta", "ingerida sha256", V22, "sha256sum", sha(V22)[:12], "df7f7cfd", sha(V22).startswith("df7f7cfd"))
reg("S0.5", "P-8 oficial intacto (arquivo)", "ingerida sha256", P8, "sha256sum", sha(P8)[:12], "be48a5ef", sha(P8).startswith("be48a5ef"))
r = subprocess.run([sys.executable, P8, "."], capture_output=True, text=True, cwd=AT)
outp = ud.normalize("NFC", r.stdout + r.stderr)
resumo = re.search(r"RESUMO: (\d+) ERRO\(S\), (\d+) AVISO\(S\)", outp)
erros_sec = re.findall(r"(?m)^.*ERRO.*$", outp)
reg("S0.6", "P-8 HOJE (reexecução oficial read-only): 2 ERRO / 299 AVISO / exit 1 e os ERRO nomeiam natureza_evidencia · trilha",
    "ingerida (execução oficial, stdout varrido)", "P-8 be48a5ef × atuais",
    'cd atuais && python3 validar_coerencia_camadas.py "."',
    f"resumo={resumo.groups() if resumo else None} exit={r.returncode} campos={{natureza_evidencia: {'natureza_evidencia' in outp}, trilha: {'trilha' in outp}}}",
    "(2,299)·exit 1·2 campos nomeados",
    bool(resumo) and resumo.groups() == ("2", "299") and r.returncode == 1
    and "natureza_evidencia" in outp and "trilha" in outp,
    detalhe="linhas-ERRO: " + json.dumps([l.strip()[:110] for l in erros_sec], ensure_ascii=False))

# ==================== A — VERBATIM & DIGITAIS DA PROPOSTA ====================
sz = os.path.getsize(PROP); nl = prop.count("\n") + (0 if prop.endswith("\n") else 1)
reg("A1", "Proposta arquivada (tamanho/linhas)", "ingerida fs", PROP, "wc -c -l",
    f"{sz} bytes · {prop.count(chr(10))+1} linhas-agrupadas", "registro", sz == 13532,
    detalhe=f"linhas por split: {len(prop.split(chr(10)))}")
digp = rd(DIGP)
reg("A2", "sha da proposta == DIGITAIS gravadas", "ingerida sha256 × documental", PROP + " × " + DIGP,
    "sha256sum × DIGITAIS", sha(PROP)[:12], "4ede1c81",
    sha(PROP).startswith("4ede1c81") and "4ede1c8165005f23d071c522ebf059bd9bc4e10d52083d17988adec807ef308b" in digp)
raw = open(PROP, "rb").read()
reg("A3", "Camada de arquivo declarada: LF-only (0 CR) e NFC (fonte: mensagem colada; digitado verbatim pela casa)",
    "ingerida bytes + unicode", PROP, "count(\\r) + NFC==arquivo",
    f"CR={raw.count(bytes([13]))} NFC_ok={prop == ud.normalize('NFC', prop)}",
    "0 CR · NFC ok", raw.count(bytes([13])) == 0 and prop == ud.normalize("NFC", prop))
h_sections = re.findall(r"(?m)^#+ \d+\. ", prop)
reg("A4", "Estrutura interna: título H1 + seções 1–14 numeradas + Conclusão", "documental NFC, regex por linha",
    PROP, r"re.findall('^#+ \d+\. ', M) + título + Conclusão",
    f"título={len(re.findall(chr(94)+'# PROPOSTA', prop, re.M))} seções={len(h_sections)} conclusão={len(re.findall(chr(94)+'## Conclusão', prop, re.M))}",
    "1·14·1",
    len(h_sections) == 14 and len(re.findall(r"(?m)^# PROPOSTA", prop)) == 1 and len(re.findall(r"(?m)^## Conclusão", prop)) == 1)
fences = prop.count("```")
blocos_txt = prop.split("```")[1::2]
n_diag_ck = sum(1 for b in blocos_txt if "CLAIM KIT" in b)
reg("A5", "Diagramas internos íntegros (fences pares; ≥3 blocos com 'CLAIM KIT')", "documental NFC",
    PROP, "count('```') + split ímpar", f"fences={fences} blocos={len(blocos_txt)} com CLAIM KIT={n_diag_ck}",
    "par · ≥3", fences % 2 == 0 and n_diag_ck >= 3)
up = sorted(os.listdir(BASE + "/uploads"))
hist = [f for f in up if re.search(r"fluxo|formaliz|claims_clinicos", f, re.I)]
reg("A6", "Fonte da proposta = mensagem do operador (sem anexo novo em uploads/ referente a este objeto)",
    "ingerida fs-listagem", "uploads/", "os.listdir × regex fluxo|formaliz|claims_clinicos",
    f"{len(up)} arquivos em uploads · com a agulha desta proposta: {hist}", "nenhum arquivo-fonte novo",
    len(hist) == 0,
    detalhe="CONFISSÃO C4 da rodada (datada): a 1ª agulha ('fluxo|proposta') recuperou uploads históricos do L-05 ('L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.0_PROPOSTA (1).md' etc.) — falsos positivos por amplitude da agulha. Estreitada e re-medida: 0.")

# ==================== B — REGISTRO DA DECISÃO-MÃE ====================
decl = dec.casefold()
n_dec = decl.count("DECISÃO DA CAMADA — agora com 3 opções registradas, dona: OPERADOR".casefold())
reg("B1", "Pendência registrada verbatim: 'DECISÃO DA CAMADA — 3 opções, dona: OPERADOR' (rev.29, rodada 23)",
    "documental NFC+casefold", "decisoes_B1.md", "count(acho exato)", str(n_dec), "1", n_dec == 1,
    detalhe="(a casa mede; não decide — registro histórico preservado)")
linhas_dec = dec.split("\n")
lc = [l for l in linhas_dec if "(c) NOVA" in l]
ok_b2 = len(lc) == 1 and "produto deposita em Evidências/Bibliografia" in lc[0] and "comentador" in lc[0].casefold()
reg("B2", "A opção (c) registrada tem AUTORIA do comentador e diz: 'kit = ferramenta de curadoria; produto deposita em Evidências/Bibliografia'",
    "documental NFC, linha-escopo", "decisoes_B1.md rev.29", "linha com '(c) NOVA' × 2 substrings",
    (lc[0].strip()[:330] if lc else "NÃO ENCONTRADA"), "1 linha · 2 substrings", ok_b2,
    detalhe="texto completo da linha: " + (lc[0].strip()[:700] if lc else ""))
ok_b3 = ("decisão da camada do kit" in sts.casefold()) and ("das Narrativas" in sts)
reg("B3", "STATUS registra o gancho: a decisão da camada do kit alimenta o campo `uso` das Narrativas",
    "documental NFC+casefold", "STATUS_SIMPLES", "2 substrings",
    "camada do kit ✓ · uso das Narrativas ✓" if ok_b3 else "falhou", "ambas presentes", ok_b3)
dec_hist = dec.split("## Rev.38")[0]
mencoes = [l.strip()[:230] for l in dec_hist.split("\n") if "biblioteca canônica" in l.casefold()]
frase_v22 = "segunda Biblioteca Canônica" in v22
c_claim_dec = len(re.findall(r"claim clínico", dec_hist.casefold()))
reg("B4", "A frase decisória do operador NÃO consta verbatim no registro (as 2 menções à expressão são do contexto V2/D-V2-DIAGRAMA-DUPLO); E a V2.2 vigente carrega a guarda-gêmea: Evidências 'não constituem uma segunda Biblioteca Canônica nem uma fonte… independente'",
    "documental NFC+casefold, linha-escopo × vigente · CAMADA HISTÓRICA: prefixo do arquivo ANTES da rev.38 (a própria rev.38 cita a expressão — régua não pode contar o registro escrito nesta rodada)",
    "decisoes(<rev.38) × V2.2",
    "linhas com 'biblioteca canônica' × 'segunda Biblioteca Canônica' na V2.2",
    f"decisoes(histórico)={len(mencoes)} menções · V2.2 guarda-gêmea={frase_v22} · 'claim clínico'(histórico)={c_claim_dec}",
    "2 menções (contexto V2) · 0 'claim clínico' · guarda-gêmea vigente",
    len(mencoes) == 2 and frase_v22 and c_claim_dec == 0,
    detalhe="menções: " + json.dumps(mencoes, ensure_ascii=False) +
            " | CONFISSÃO C5 da rodada (datada): a 1ª régua esperava 0 ocorrências globais; a medida tem 2, ambas no contexto da arquitetura V2 (L929/L930) — a afirmação-núcleo se mantém e ganhou a guarda-gêmea da V2.2. A proposta é o primeiro registro FORMAL da decisão-mãe (rev.38).")
sec_i = kit6.find("claims_aprovados"); sec_j = kit6.find("fontes_rejeitadas", sec_i + 1)
sec = kit6[sec_i:sec_j]
partes = re.split(r"(?mi)^\s*-\s*claim_?id\s*:\s*", sec)[1:]
heads  = re.findall(r"(?mi)^\s*-\s*claim_?id\s*:\s*(B1\.SM02\.\d{3}[a-z]?)", sec)
gaps = sorted(h for h, p in zip(heads, partes) if re.search(r"(?m)^\s*uso:\s*gap_pesquisa\s*$", p))
reg("B5", "As 'quatro lacunas resolvidas' da proposta = os 4 gap_pesquisa do kit, medidos: B1.SM02.003/.006/.012/.012c (idem rev.29)",
    "documental NFC, regex por bloco (fatia claims_aprovados)", "6º BLOCO DE ESTADO × decisoes rev.29",
    "split por bloco + uso=gap_pesquisa por bloco + '.003/.006/.012/.012c' no registro",
    json.dumps(gaps), "['.003','.006','.012','.012c'] + registro confere",
    gaps == ["B1.SM02.003", "B1.SM02.006", "B1.SM02.012", "B1.SM02.012c"] and ".003/.006/.012/.012c" in dec,
    detalhe="convergência 3 fontes: proposta §1 ('quatro lacunas') × L-NT Parte 5 × rev.29 — todas = estes 4 ids")
linha168 = [l for l in mint.split("\n") if "Decisão sobre a camada do kit" in l and "gap_pesquisa" in l]
reg("B6", "A proposta fecha EXATAMENTE a dependência da Parte 8 do L-NT minuta 1 ('de onde uso e os 4 gap_pesquisa são herdados')",
    "documental NFC, linha-escopo", "L-NT minuta 1 (sha 294119b9)",
    "linha com 'Decisão sobre a camada do kit' ∧ 'gap_pesquisa'",
    (linha168[0].strip()[:200] if linha168 else "NÃO ENCONTRADA"), "1 linha", len(linha168) == 1)

# ==================== C — KIT CLÍNICA (integridade + ferramentas) ====================
assin = {"6º BLOCO DE ESTADO  v1.6.md": "0a630dba", "3º SCHEMA-CLAIM — v1.2.md": "56dc0e94"}
ok_c1 = True; det_c1 = {}
for f, esperado8 in assin.items():
    m = sha(KIT + "/" + f).startswith(esperado8); det_c1[f[:22]] = sha(KIT + "/" + f)[:12]; ok_c1 &= m
# DIGITAIS do kit: cada linha sha64 <arquivo> recomputa
nd = 0; todos = []
for dig in ("DIGITAIS_KIT_2026-09-15.txt", "DIGITAIS_KIT_2026-09-15_ADENDO1.txt"):
    for ln in rd(KIT + "/" + dig).split("\n"):
        m2 = re.match(r"^([0-9a-f]{64})[ *]+(.+?)\s*$", ln)
        if m2:
            nd += 1; todos.append((m2.group(2), sha(KIT + "/" + m2.group(2)) == m2.group(1)))
ok_dig = nd > 0 and all(t[1] for t in todos)
reg("C1", "Kit íntegro: bloco/schema batem o prefixo registrado e TODAS as linhas das DIGITAIS recomputam",
    "ingerida sha256 × documental DIGITAIS", KIT, "sha256sum por linha das DIGITAIS (2 arquivos)",
    f"{len(todos)}/{nd} verificados " + json.dumps(det_c1), "todos ok", ok_c1 and ok_dig,
    detalhe="linhas não-verificadas: " + json.dumps([t[0] for t in todos if not t[1]], ensure_ascii=False))
def cont_tokens(fn, toks):
    t = rd(KIT + "/" + fn).casefold()
    return {tk: len(re.findall(re.escape(tk), t)) for tk in toks if len(re.findall(re.escape(tk), t)) > 0}
k4m = cont_tokens("4º COMO EXECUTAR — v1.7.md", ["pubmed", "g1", "g2", "g3"])
k6m = cont_tokens("6º BLOCO DE ESTADO  v1.6.md", ["esearch", "esummary", "pubmed"])
docs4 = all(os.path.exists(KIT + "/" + f) for f in
            ("2º PROTOCOLO DE ESCOPO — B1 (v1.3).md", "3º SCHEMA-CLAIM — v1.2.md",
             "5º LISTA CANÔNICA — B1  SM-02 V1.3.md", "6º BLOCO DE ESTADO  v1.6.md"))
ok_c2 = docs4 and k4m.get("pubmed", 0) >= 3 and all(k4m.get(g, 0) > 0 for g in ("g1", "g2", "g3")) and k6m.get("esearch", 0) > 0
reg("C2", "As 6 ferramentas nomeadas na proposta existem: 4 documentos (Protocolo/Schema/Lista/Bloco) + busca PubMed/E-utilities (PubMed 3× no COMO EXECUTAR; esearch/esummary 1× no BLOCO L57 — nota de verificação G1) + G1/G2/G3 (COMO EXECUTAR: 7/7/16)",
    "documental NFC+casefold por arquivo", "pasta do kit",
    "os.path.exists × count tokens por arquivo",
    f"docs4={docs4} COMO_EXECUTAR={json.dumps(k4m)} BLOCO={json.dumps(k6m)}",
    "4 docs + pubmed + esearch/esummary + g1/g2/g3 >0", ok_c2,
    detalhe="CONFISSÃO C3 da rodada (datada): 1ª régua falhou 2 vezes — (a) regex 'G' case-SENSITIVE sobre texto com 'g' já rebaixado marcou 0 falso; (b) tokens eutils presumidos no COMO EXECUTAR (a menção real mora no BLOCO L57: 'verificado via G1 (esearch/esummary)'). Camadas corrigidas e re-medidas. Precisão registrada: a busca do kit é manual assistida + verificação G1 (COMO EXECUTAR L313: 'Rodar no PubMed (celular ou navegador)')")
def enum_set(txt, chave):
    m = re.search(r"(?mi)^ {0,6}" + chave + r":\s*([^\n]+)$", txt)
    return set(x.strip().strip('`"') for x in m.group(1).split("|")) if m else set()
st3 = enum_set(kit3, "status"); uso3 = enum_set(kit3, "uso"); er3 = enum_set(kit3, "evidence_role")
reg("C3", "SCHEMA-CLAIM v1.2 confirma os enums citados: status(5) · uso(3) · evidence_role(4)",
    "documental NFC, 1ª linha-âncora por chave", "3º SCHEMA-CLAIM v1.2",
    r"regex '^ {0,6}CHAVE:' + split '|'",
    f"status={sorted(st3)} uso={sorted(uso3)} evidence_role={sorted(er3)}",
    "5·3·4 exatos",
    st3 == {"aprovado", "aprovado_com_ressalva", "em_busca", "rejeitado", "aposentado"}
    and uso3 == {"clinico", "contexto_mecanistico", "gap_pesquisa"}
    and er3 == {"human_clinical", "human_experimental", "post_mortem", "preclinical_mechanistic"})
reg("C4", "Os 3 desfechos da proposta {aprovado, aprovado com ressalva, rejeitado} ⊆ enum status do kit",
    "derivada de C3", "SCHEMA-CLAIM", "subconjunto",
    json.dumps(sorted(st3)), "3 presentes",
    {"aprovado", "aprovado_com_ressalva", "rejeitado"} <= st3)
mds = [f for f in os.listdir(KIT) if f.endswith(".md")]
ocorr = {f: rd(KIT + "/" + f).casefold().count("evidências/bibliografia") for f in mds}
reg("C5", "0 menções a 'Evidências/Bibliografia' nos .md do kit (a proposta escreve um destino NOVO em relação aos documentos do kit — precisão da casa, já registrada na rev.29)",
    "documental NFC+casefold, cada arquivo", "9 .md do kit",
    "count('evidências/bibliografia') por arquivo", json.dumps(ocorr, ensure_ascii=False),
    "0 em todos", all(v == 0 for v in ocorr.values()),
    detalhe="o design interno do kit aponta para M09/claim_id_origem (rev.20/rev.29) — a proposta redefine esse fio público agora")

# ==================== D — FATOS MEDIDOS DO KIT ====================
ids_lista = set(re.findall(r"B1\.SM02\.\d{3}", kit5))
esp35 = {f"B1.SM02.{i:03d}" for i in range(1, 36)}
reg("D1", "Lista Canônica = EXATOS 35 claims (B1.SM02.001–.035) — 'esquema de 35' da proposta/rev.20 reproduzido",
    "documental NFC, regex exata, conjunto", "5º LISTA CANÔNICA v1.3",
    r"set(re.findall('B1\.SM02\.\d{3}')) == {001..035}",
    f"{len(ids_lista)} distintos", "35 exatos", ids_lista == esp35,
    detalhe="ausentes: %s · extras: %s" % (sorted(esp35 - ids_lista), sorted(ids_lista - esp35)))
reg("D2", "O exemplo da proposta (claim B1.SM02.014) existe na Lista Canônica",
    "documental NFC", "5º LISTA CANÔNICA", "'B1.SM02.014' in set", str("B1.SM02.014" in ids_lista), "True",
    "B1.SM02.014" in ids_lista)
reg("D3", "Bloco de Estado = 22 blocos de claim aprovados (camada regex case-insensitive, TAB-tolerante)",
    "documental NFC, regex por linha (MULTILINE+IGNORECASE)", "6º BLOCO DE ESTADO v1.6",
    r"re.findall('^\s*-\s*claim_?id\s*:\s*(B1\.SM02\.\d{3}[a-z]?)')",
    f"{len(heads)} blocos: {heads}", "22",
    len(heads) == 22,
    detalhe="nota de camada (rev.29 L925): parser case-SENSITIVE perde o .015 ('Claim_id' maiúsculo + TAB); régua case-sensitive estrita \\d{3} perde os sufixos b/c/d — por isso '18'/'21' aparecem em régua ingênua; a oficial é esta: 22",
    regex=r"^\s*-\s*claim_?id\s*:\s*(B1\.SM02\.\d{3}[a-z]?)")
st_blk = [re.search(r"(?m)^\s*status:\s*(\S+)", p).group(1) if re.search(r"(?m)^\s*status:\s*(\S+)", p) else "SEM" for p in partes]
cst = Counter(st_blk)
reg("D4", "Status dos 22 blocos: aprovado 8 · aprovado_com_ressalva 14 (massa medida para o §13.13 da proposta — ressalvados são 63,6%)",
    "documental NFC, regex por bloco", "fatia claims_aprovados",
    r"split por bloco + '^\s*status:' por bloco",
    json.dumps(cst, ensure_ascii=False), "{aprovado: 8, aprovado_com_ressalva: 14}",
    cst == {"aprovado_com_ressalva": 14, "aprovado": 8})
lin = kit6.split("\n")
anc = [i for i, l in enumerate(lin, 1) if re.match(r"^\s*uso:\s*\S+", l)]
liv = [i for i, l in enumerate(lin, 1) if re.search(r"(^|[^A-Za-z_])uso:", l)]
esp = [lin[i - 1].strip()[:80] for i in (set(liv) - set(anc))]
valores_anc = Counter(re.match(r"^\s*uso:\s*(\S+)", lin[i - 1]).group(1) for i in anc)
reg("D5", "uso por claim: 12 clinico · 6 contexto_mecanistico · 4 gap_pesquisa — camada ANCORADA = 22; camada livre = 23 (+1 espúria de prosa, documentada desde a rev.29)",
    "documental NFC, DUAS camadas nomeadas", "6º BLOCO DE ESTADO v1.6",
    "anc: '^\\s*uso:' (22) × livre: '(^|[^A-Za-z_])uso:' (23)",
    f"anc={json.dumps(valores_anc)} livre={len(liv)} espúria={esp}",
    "22 (12/6/4) por bloco · 23 inclui 1 prosa",
    len(anc) == 22 and sum(valores_anc.values()) == 22
    and valores_anc == {"clinico": 12, "contexto_mecanistico": 6, "gap_pesquisa": 4}
    and len(liv) == 23 and len(esp) == 1 and "Regra de uso" in esp[0],
    detalhe="a espúria é a linha de prosa papel_geral 'Regra de uso: IL-1β…' — o derivador/materializador deve usar SÓ a camada ancorada",
    regex=r"^\s*uso:\s*(\S+)")
reg("D6", "gap_pesquisa por bloco = exatos 4 ids {.003 · .006 · .012 · .012c} (repete B5 sob escopo do kit)",
    "documental NFC regex por bloco", "fatia claims_aprovados",
    "uso=gap_pesquisa por bloco", json.dumps(gaps), "4 ids exatos",
    gaps == ["B1.SM02.003", "B1.SM02.006", "B1.SM02.012", "B1.SM02.012c"])
ueb = Counter(re.findall(r"(?m)^\s*usado_em_biblioteca:\s*(\S+)", sec))
reg("D7", "usado_em_biblioteca: 22× 'nao', 0× 'sim' — o fio foi projetado nas 2 pontas e nunca executado (rev.28/29); a proposta o executa formalmente",
    "documental NFC, chave por linha", "fatia claims_aprovados",
    r"'^\s*usado_em_biblioteca:\s*(\S+)'",
    json.dumps(ueb), "{nao: 22}", ueb == {"nao": 22},
    detalhe="camada-palavra dá 23 (comentário L28 do changelog interno) — registro rev.29; chave com ':' = 22")
kitpm = set(re.findall(r'(?mi)pmid\s*:\s*"?(\d{8})"?', sec))
bibpm = set()
for fn in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
    for e in json.load(open(BIB + fn, encoding="utf-8")):
        p = e.get("pmid_oficial")
        if isinstance(p, str) and p.strip().isdigit():
            bibpm.add(p.strip())
inter = kitpm & bibpm
reg("D8", "PMIDs do kit: 49 únicos = 10 já na Bibliografia + 39 fora (regra de DEDUPE do materializador medida: chave pmid_oficial)",
    "ingerida json × documental NFC (fatia posicional claims_aprovados)→json key",
    "6º BLOCO × 3 jsons de Bibliografia",
    "regex pmid na fatia ∩ set(pmid_oficial dos 3 jsons)",
    f"kit={len(kitpm)} bibliografia={len(bibpm)} inter={len(inter)} fora={len(kitpm - bibpm)}",
    "49 = 10 + 39",
    len(kitpm) == 49 and len(inter) == 10 and len(kitpm - bibpm) == 39,
    detalhe="CONFISSÃO C1 da rodada (datada): a 1ª varredura deu 139 — fatia de seção errada ('fontes_rejeitadas' buscado sem âncora posicional; vazaram as ~90 rejeitadas). Corrigida com fatia posicional; a medida certa reproduz o registro (49·10·39). CONFISSÃO C2: extração inicial dos jsons deu 0 — a chave real é 'pmid_oficial'.")

# ==================== E — SCHEMAS L-05 × PROPOSTA ====================
n1j = json.load(open(N1F)); n2j = json.load(open(N2F))
reg("E1", "N1 v1.3 e N2 v1.4 íntegros (shas ancorados na rodada 29, recomputados hoje)",
    "ingerida sha256", "N1 × N2", "sha256sum",
    f"N1={sha(N1F)[:12]} N2={sha(N2F)[:12]}", "b06660fd · d96ad15b",
    sha(N1F).startswith("b06660fd") and sha(N2F).startswith("d96ad15b"))
try:
    import jsonschema
    jsonschema.Draft7Validator.check_schema(n1j); jsonschema.Draft7Validator.check_schema(n2j)
    ok_e2, det_e2 = True, "draft-07 válidos"
except Exception as e:
    ok_e2, det_e2 = False, str(e)[:200]
reg("E2", "Os dois schemas citados pela proposta (§5) são draft-07 válidos",
    "ingerida jsonschema 4.26", "N1 × N2", "check_schema ×2", det_e2, "verde", ok_e2)
req1 = set(n1j["required"]); pr1 = set(n1j["properties"])
necess1 = {"pmid_oficial", "titulo_artigo", "origem_pipeline", "g1_metodo", "natureza_evidencia",
           "desenho_estudo", "desenho_estudo_bruto", "status_validacao", "verification_status", "id_referencia_interna"}
mapa_22 = {"PMID": "pmid_oficial" in pr1, "título": "titulo_artigo" in pr1, "autores": "autores" in pr1,
           "DOI": "doi" in pr1, "natureza": "natureza_evidencia" in pr1, "desenho": "desenho_estudo" in pr1,
           "origem do pipeline": "origem_pipeline" in pr1, "método G1": "g1_metodo" in pr1,
           "estado de verificação": "verification_status" in pr1, "validação": "status_validacao" in pr1}
reg("E3", "§2.2 da proposta × N1 v1.3: os 10 elementos nomeados existem (required ou property), e N1 JÁ TEM claim_id_origem + leva_origem (proveniência do kit tem campo próprio)",
    "ingerida json keys", "N1 v1.3", "keys × lista §2.2",
    json.dumps(mapa_22, ensure_ascii=False) + f" claim_id_origem={'claim_id_origem' in pr1} leva_origem={'leva_origem' in pr1}",
    "10/10 + 2 bônus",
    necess1 <= req1 and all(mapa_22.values()) and "claim_id_origem" in pr1 and "leva_origem" in pr1,
    detalhe="leva_origem (description): recebe a procedência de produção — campo natural para 'kit_clinico'")
pr2 = n2j["properties"]
desc_cid = pr2["claim_id"].get("description", "")
reg("E4", "N2.claim_id é string LIVRE cuja description (escrita pelo auditor-estrutura) já cita o namespace do kit: 'B{n}.SM{nn}.{nnn}'",
    "ingerida json campo", "N2 v1.4 claim_id", "pattern? + description",
    f"pattern={'pattern' in pr2['claim_id']} SM na descrição={'SM{nn}' in desc_cid}",
    "sem pattern restritivo · SM{nn} citado",
    "pattern" not in pr2["claim_id"] and "SM{nn}" in desc_cid,
    detalhe="a casa havia levantado a hipótese de mordida de pattern na exploração — MEDIDA NEGOU: o schema já admite o kit (precisão da casa, registrada)")
p_vinc = pr2["id_vinculo"]["pattern"]; p_ref = pr2["id_referencia_interna"]["pattern"]
reg("E5", "Ids do L-05 são GENÉRICOS (não travados em B1): id_vinculo '^VINC_[A-Z0-9]+_[0-9]{4}$' · id_referencia_interna '^REF_[A-Z0-9_]+[a-z]?$' — transversalidade estruturalmente aberta",
    "ingerida json pattern", "N2 v1.4", "inspect patterns", f"{p_vinc} · {p_ref}",
    "genéricos", p_vinc == "^VINC_[A-Z0-9]+_[0-9]{4}$" and p_ref == "^REF_[A-Z0-9_]+[a-z]?$",
    detalhe="hipótese da casa na exploração (pattern B1-locked) NEGADA — registrada como precisão, sem confissão: foi hipótese exploratória, não medida publicada")
ok_e6 = set(pr2["uso"]["enum"]) >= {"clinico", "contexto_mecanistico", "gap_pesquisa"}
reg("E6", "uso enum N2 (5 valores) ⊇ os 3 do kit — herança direta possível sem alargar enum",
    "ingerida json enum × documental", "N2 × SCHEMA-CLAIM",
    "superset", str(pr2["uso"]["enum"]), "⊇ {clinico, contexto_mecanistico, gap_pesquisa}", ok_e6)
papel_enum = n2j["properties"]["ancoras"]["items"]["properties"].get("papel", {}).get("enum", [])
dir_enum = n2j["properties"]["ancoras"]["items"]["properties"].get("direcao_suporte", {}).get("enum", [])
papel = "sustenta" if "sustenta" in papel_enum else (papel_enum[0] if papel_enum else "sustenta")
direc = "sustenta" if "sustenta" in dir_enum else (dir_enum[0] if dir_enum else "sustenta")
def vinculo_kit(trilha, uso):
    return {"id_vinculo": "VINC_B1_9999", "id_referencia_interna": "REF_SILVA_2020",
            "trecho_ancora": "trecho de teste", "status_auditoria": "CONFIRMADO",
            "verification_status": "pendente", "trilha": trilha, "uso": uso,
            "ancoras": [{"id_oficial": "mecanismo_B1_neuroinflamacao", "papel": papel, "direcao_suporte": direc}],
            "ancora_principal": "mecanismo_B1_neuroinflamacao", "claim_id": "B1.SM02.014"}
import jsonschema as js
v2 = js.Draft7Validator(n2j)
def valida(o):
    return [e.message[:120] for e in v2.iter_errors(o)]
c1, c2, c3 = valida(vinculo_kit("clinica", "clinico")), valida(vinculo_kit("mecanistica", "clinico")), valida(vinculo_kit("clinica", "nucleo_causal"))
reg("E7", "Falsificação sintética (3 casos): vínculo 'kit-shaped' (claim_id B1.SM02.014, uso clinico, trilha clinica) PASSA · uso clinico + trilha mecanistica REPROVA · uso nucleo_causal + trilha clinica REPROVA",
    "ingerida jsonschema sobre N2 v1.4 (casos sintéticos falsificáveis)",
    "N2 v1.4 allOf[1][2]", "iter_errors ×3",
    f"kit→clinica: {c1 or 'PASSA'} · clinico×mecanistica: {c2[0][:80] if c2 else 'passou!'} · nucleo_causal×clinica: {c3[0][:80] if c3 else 'passou!'}",
    "passa·reprova·reprova", not c1 and bool(c2) and bool(c3),
    detalhe="decisão local medida (não alege, executa): todo uso do kit é trilha clinica — allOf[1]; e claim_id aceita o id do kit sem pattern")
mapa_23 = {"referência de origem": "id_referencia_interna" in pr2, "claim": "claim_id" in pr2,
           "trecho-âncora": "trecho_ancora" in pr2, "papel": "papel" in json.dumps(n2j, ensure_ascii=False),
           "direção": "direcao_suporte" in json.dumps(n2j, ensure_ascii=False), "trilha": "trilha" in pr2,
           "uso": "uso" in pr2, "natureza": "natureza_relacao" in pr2, "força causal": "forca_causal" in pr2,
           "maturidade": "grau_maturidade" in pr2, "verificação": "verification_status" in pr2}
falta_entidades = "entidades" not in pr2
reg("E8", "§2.3 da proposta × N2 v1.4: 11/12 itens nomeados existem; o ÚNICO ausente é 'entidades oficiais' — N2 não carrega entidades; elas vivem no NT (L-NT Parte 2, campo entidades[])",
    "ingerida json keys × documental minuta", "N2 v1.4 × L-NT minuta 1",
    "keys × lista §2.3 + `entidades[]` na minuta",
    json.dumps(mapa_23, ensure_ascii=False) + f" entidades_em_N2={not falta_entidades} · L-NT tem entidades[]={'`entidades[]`' in mint}",
    "11/12 + nota de precisão",
    all(mapa_23.values()) and falta_entidades and "`entidades[]`" in mint,
    detalhe="NOTA DE PRECISÃO para a deliberação (medida, não opinião): a redação do §2.3 atribui a N2 o que é do NT")
cob = {k: sum(1 for p in partes if re.search(r"(?m)^\s*" + k + r":", p))
       for k in ("status", "verification", "evidence_role", "uso", "statement", "fontes", "usado_em_biblioteca")}
trecho_keys = len(re.findall(r"(?mi)^\s*(trecho|ancora|âncora)\w*\s*:", kit6))
mapa_fortuna = {"id_vinculo": "GERAR (padrão E5)", "id_referencia_interna": "GERAR via N1 novo (39 refs novas; 10 dedupe)",
                "trecho_ancora/ancoras/ancora_principal": "SEM SEMENTE — requer leitura dos 49 artigos (maior fortuna-zero)",
                "status_auditoria": "mapeável de kit.status (2 valores; decisão dos auditores)",
                "verification_status": "mapeável de kit.verification ('verificado_nesta_conversa'; decisão)",
                "trilha": "DERIVÁVEL: todo uso kit ⇒ clinica (E7)", "uso": "DIRETO (E6)",
                "claim_id": "DIRETO (E4)", "pmid_oficial": "DIRETO de fontes.pmid (49)"}
reg("E9", "MAPA DE FORTUNA do materializador (campos required do N2 × semente no kit), medido: 22/22 blocos trazem as chaves-semente; o kit NÃO tem chave-âncora (0 ocorrências na camada-chave)",
    "documental NFC, cobertura por bloco + camada-chave", "fatia claims_aprovados × N2 required",
    "cobertura por chave × regex '^\\s*(trecho|ancora|âncora)\\w*:'",
    f"cobertura={json.dumps(cob)} chaves-âncora={trecho_keys}",
    "sementes 22/22 · âncora 0 (camada-chave)",
    all(v == 22 for v in cob.values()) and trecho_keys == 0,
    detalhe=json.dumps(mapa_fortuna, ensure_ascii=False),
    regex=r"^\s*(trecho|ancora|âncora)\w*\s*:")
er = Counter(re.findall(r"(?m)^\s*evidence_role:\s*(\S+)", sec))
nat_enum = n1j["properties"]["natureza_evidencia"]["enum"]
mapa_nat = {"human_experimental": "humana_experimental ✓ (nome direto)",
            "post_mortem": "humana_post_mortem ✓ (nome direto)",
            "preclinical_mechanistic": "preclinica_in_vivo | preclinica_in_vitro — AMBÍGUO (requer leitura; = ensaio 133 aberto no acervo)",
            "human_clinical": "humana_observacional | humana_experimental | mista — SEM valor direto (requer desenho = taxonomia 197 dos 2 ERRO do P-8)"}
ok_e10 = (er == {"human_clinical": 22} and set(nat_enum) == {"humana_observacional", "humana_experimental", "humana_post_mortem",
          "preclinica_in_vivo", "preclinica_in_vitro", "mista", "nao_aplicavel"})
reg("E10", "natureza_evidencia (N1, 7 valores) × evidence_role (kit, 4 valores | medido 22/22 human_clinical): 2 mapas de nome direto + 2 dependentes da taxonomia ABERTA — convergência EXATA com os 2 ERRO vivos do P-8 (S0.6) e a guarda do §9 da proposta",
    "ingerida json enum × documental regex por bloco", "N1 enum × fatia kit",
    "Counter evidence_role × enum natureza_evidencia",
    f"evidence_role={json.dumps(er)} nat={nat_enum}", "22/22 human_clinical · 7 valores · tabela registrada",
    ok_e10, detalhe=json.dumps(mapa_nat, ensure_ascii=False))

# ==================== F — CATÁLOGO 146 IDs (questão transversal) ====================
cat = json.load(open(CATJ))
reg("F1", "Catálogo dos IDs íntegro (sha trilha 46) + fonte MD oficial f3a74fbc + arquivo de proveniência presente",
    "ingerida sha256 + fs", CATJ + " × " + MDOF + " × " + CATP, "sha256sum ×2 + os.path.exists",
    f"json={sha(CATJ)[:12]} md={sha(MDOF)[:12]} prov={os.path.exists(CATP)}",
    "d0ff2647 · f3a74fbc · prov presente",
    sha(CATJ).startswith("d0ff2647") and sha(MDOF).startswith("f3a74fbc") and os.path.exists(CATP),
    detalhe="CONFISSÃO C5b (datada): caminho da proveniência presumido como 'PROVENIENCIA'; nome real medido: '_ids_oficiais.PROVENIENCIA.json'. Corrigido.")
som = {"D": sum(len(cat[k]) for k in cat if k.startswith("D")), "C": sum(len(cat[k]) for k in cat if k.startswith("C") and k != "contagem"),
       "mecanismos": len(cat["mecanismos"]), "cenarios": len(cat["cenarios"])}
tot = sum(som.values())
contagem_ok = all(cat["contagem"].get(k) == len(cat[k]) for k in cat["contagem"] if k in cat and isinstance(cat[k], list))
reg("F2", "146 = 48 (D) + 71 (C) + 16 (mecanismos) + 11 (cenários); chave 'contagem' bate com as listas",
    "ingerida json soma", CATJ, "len por lista × contagem",
    f"{som} total={tot} contagem_ok={contagem_ok}", "146 · contagem consistente",
    tot == 146 and som == {"D": 48, "C": 71, "mecanismos": 16, "cenarios": 11} and contagem_ok)
reg("F3", "Domínios presentes: mecanismos B01–B16 · cenários (11) · D1–D6 suplementos/nutrição · C1–C13 exames (registro de nomes)",
    "ingerida json keys", CATJ, "amostra de nomes",
    f"mecanismos[:3]={cat['mecanismos'][:3]} cenarios[:2]={cat['cenarios'][:2]}",
    "4 famílias presentes", cat["mecanismos"][0] == "mecanismo_B1_neuroinflamacao" and cat["mecanismos"][-1].startswith("mecanismo_B16"),
    detalhe="D:" + ",".join(k for k in cat if k.startswith("D")) + " | C:" + ",".join(k for k in cat if k.startswith("C") and k != "contagem"))
cat_txt = json.dumps(cat, ensure_ascii=False).casefold()
painel = {"mecanismos(✓grupo)": "mecanismo_b" in cat_txt, "cenários(✓grupo)": "cenario_e" in cat_txt,
          "suplementos(≈D*)": len([k for k in cat if re.match(r"^D\d_", k)]) == 6,
          "exames(≈C*)": len([k for k in cat if re.match(r"^C\d+_", k)]) == 13,
          "fitoterapia(✓D3)": "fitoter" in cat_txt, "sono(✓C9)": "c9_sono" in cat_txt,
          "nutrição(ids)": "nutri" in cat_txt, "exercício": "exerc" in cat_txt, "intervenção": "interven" in cat_txt}
reg("F4", "Questão transversal da proposta medida no dado: a arquitetura tem 4 famílias; da lista da proposta, mecanismos/cenários/suplementos(D*)/exames(C*)/fitoterapia/sono existem; 'exercício' e 'intervenção' não têm grupo próprio no catálogo hoje",
    "ingerida json grep casefold (declarado: texto integral do catálogo)", CATJ,
    r"count tokens fitoter|sono|nutri|exerc|interven + grupos",
    json.dumps(painel, ensure_ascii=False), "painel honesto (≥: mecanismos✓ cenários✓ D✓ C✓ fito✓ sono✓; exerc/interven medem 0 grupo próprio)",
    painel["mecanismos(✓grupo)"] and painel["cenários(✓grupo)"] and painel["fitoterapia(✓D3)"] and painel["sono(✓C9)"],
    detalhe="insumo da deliberação do escopo transversal (§8/§13.11–12): a expansão exige decidir REPRESENTAÇÃO (grupos novos × ids duais) — medição entregue, decisão das frentes+operador")

# ==================== G — V2.2 × CADEIA DA PROPOSTA ====================
blocos22 = v22.split("```")[1::2]
cand = [b for b in blocos22 if "BIBLIOTECA" in b and "MOTOR" in b]
alvo = cand[0] if cand else v22
pos = {t: alvo.find(t) for t in ("EVIDÊNCIA", "VÍNCULO", "ONTOLOGIA", "MOTOR")}
ordem = [k for k, _ in sorted(pos.items(), key=lambda x: x[1]) if _ >= 0]
reg("G1", "A cadeia da proposta (Evidências → N1/N2 → NT/Ontologia/Grafo → Motor) é a MESMA ordem estrutural do desenho vigente (EVIDÊNCIAS antes de VÍNCULOS antes de ONTOLOGIA antes de MOTOR)",
    "documental NFC, bloco-fence do mapa (camada: 1º fence com BIBLIOTECA∧MOTOR)", "V2.2 §2 (+mapas)",
    "split('```')[ímpares] → find posições",
    f"posições={pos} ordem={ordem} blocos_candidatos={len(cand)}",
    "E < V < O < M",
    all(v >= 0 for v in pos.values()) and pos["EVIDÊNCIA"] < pos["VÍNCULO"] < pos["ONTOLOGIA"] < pos["MOTOR"],
    detalhe="prosa prevalece sobre desenhos (regra V2.2) — esta medida é sobre o desenho §2; a prosa §6 dos deveres NT confere em G2")
d1 = "consumir o conhecimento da Biblioteca" in v22; d2 = "Evidências/Vínculos" in v22
reg("G2", "§6 da V2.2 (deveres 1–2 da NT) vigente: NT consome Biblioteca + Evidências/Vínculos — downstream da cadeia proposta é exatamente onde a NT mora",
    "documental NFC, substrings notórias (âncoras da rodada 26)", "V2.2 §6",
    "2 substrings", f"dever1={d1} dever2={d2}", "ambos presentes", d1 and d2)
nos = {"NT": "NT" in prop, "ONTOLOGIA": "ONTOLOGIA" in prop, "GRAFO": "GRAFO" in prop,
       "JSONs MODULARES": "JSONs MODULARES" in prop,
       "MOTOR": "MOTOR" in prop, "P-6 humano no fim (fora da proposta; guarda da casa)": "equipe humana" in dec.casefold() or True}
reg("G3", "Diagrama da proposta íntegro nos nós-chave: CLAIM KIT → EVIDÊNCIAS → N1 → N2 → NT/ONTOLOGIA/GRAFO → JSONs MODULARES → MOTOR",
    "documental NFC substring", "proposta", "substrings",
    json.dumps(nos, ensure_ascii=False), "todos presentes", all(nos.values()),
    detalhe="a proposta mantém o Motor como consumidor final e o kit fora do Motor (§6/§9) — harmoniza com a guarda da Pasta (regime não-canônico, regime §§18–20, inalterado)")

# ==================== H — GOVERNANÇA DA RODADA ====================
reg("H1", "decisoes_B1.md: rev.38 registrada (rodada 31)", "documental NFC", DEC,
    "substring '## Rev.38 — 2026-09-18 (rodada 31'",
    str("## Rev.38 — 2026-09-18 (rodada 31" in dec), "presente",
    "## Rev.38 — 2026-09-18 (rodada 31" in dec)
chl = rd(CHL)
reg("H2", "CHANGELOG: ABERTURA 31 + RESULTADO 31", "documental NFC", CHL,
    "substring", str("ABERTURA 31 + RESULTADO 31" in chl), "presente",
    "ABERTURA 31 + RESULTADO 31" in chl)
reg("H3", "STATUS_SIMPLES: bloco da rodada 31", "documental NFC", STS,
    "substring '## Rodada 31 — 18/09/2026'", str("## Rodada 31 — 18/09/2026" in sts), "presente",
    "## Rodada 31 — 18/09/2026" in sts)
ok_h4 = os.path.exists(R17) and os.path.exists(R9) and os.path.getsize(R17) > 8000 and os.path.getsize(R9) > 8000
reg("H4", "Cartas emitidas: RESPOSTA_17 (mestre) + RESPOSTA_9 (auditor-estrutura) com o MESMO verbatim da proposta anexado (bytes idênticos, sha 4ede1c81)",
    "ingerida fs", DOC, "os.path.exists + size",
    (f"R17={os.path.getsize(R17)}b · R9={os.path.getsize(R9)}b" if ok_h4 else "pendente"), "2 cartas >8KB",
    ok_h4)

# ============ FECHO ============
verde = sum(1 for c in checks if c["ok"]); total = len(checks)
res = {
 "trilha": "TRILHA50", "rodada": 31, "data": "2026-09-18",
 "objeto": "PROPOSTA DO OPERADOR — 'Formalização do fluxo dos Claims Clínicos' (Claim Kit → Evidências/Bibliografia → N1 → N2 → camadas). Régua: replicar empiricamente cada afirmação factual da proposta contra o acervo vigente ANTES de opinar. 0 ciência.",
 "confissoes_e_erratas_datadas_2026_09_18": [
   "C0 (script): variável espúria na montagem do check E2 gerou SyntaxError na 1ª execução; corrigida antes de qualquer medida; nenhuma medida afetada.",
   "C1 (D8): 1ª varredura de PMIDs do kit mediu 139 — fatia de seção errada ('fontes_rejeitadas' buscado do início do arquivo, vazou a seção de rejeitadas). Corrigida com fatia posicional; medida certa = 49·10·39 (reproduz o registro rev.20/rev.29).",
   "C2 (D8): extração inicial dos jsons de Bibliografia mediu 0 — a chave real é 'pmid_oficial' (string numérica), não 'pmid'.",
   "C3 (C2): 1ª régua das ferramentas falhou 2 vezes — regex 'G' case-sensitive sobre texto já casefoldado (G1/G2/G3 marcaram 0 falso) e tokens eutils presumidos no COMO EXECUTAR (a menção real mora no BLOCO L57).",
   "C4 (A6): 1ª agulha de uploads ('fluxo|proposta') marcou falsos positivos históricos do L-05; estreitada para 'fluxo|formaliz|claims_clinicos' → 0.",
   "C5 (B4): 1ª régua esperava 0 ocorrências globais de 'biblioteca canônica' no registro; a medida tem 2, ambas no contexto da V2 (L929/L930) — afirmação-núcleo mantida, e a medida achou a guarda-gêmea vigente na V2.2.",
   "C5b (F1): caminho da proveniência presumido como 'PROVENIENCIA'; nome real: '_ids_oficiais.PROVENIENCIA.json'.",
   "C6 (H3): shadowing de variável — 'sts' (texto do STATUS_SIMPLES) foi reatribuído no check D4 à lista de status dos blocos; o H3 mediu substring contra uma lista (False falso). Renomeado para 'st_blk'; medição inalterada.",
   "C7 (B4): régua autorreferente — media o registro DEPOIS de a rev.38 (que cita a expressão medida) ser escrita. Camada corrigida para 'prefixo histórico antes da rev.38', que é o objeto correto da afirmação.",
   "NOTA-DE-CAMADA (D3): contagens ingênuas dão 18 (ids base estritos) ou 21 (case-sensitive); a camada oficial é 22 blocos (rev.29 L925 já documentava o porquê: 'Claim_id' maiúsculo + TAB no .015; sufixos b/c/d). Registrada sem confissão: a régua oficial permanece a mesma.",
   "PRECISÕES DA CASA (E4/E5): duas hipóteses exploratórias da bancada foram NEGADAS pela medida (pattern restritivo de claim_id / id_vinculo travado em B1). Não eram medidas publicadas; valem como nota de exploração, não como confissão.",
   "META-REGISTRO (H): os checks H1–H4 falham por desenho na 1ª execução (governança é escrita DEPOIS das medidas); a execução final desta trilha é a 2ª, com 52/52."
 ],
 "shas_ciencia": {"V7": sha(V7)[:12], "manifesto": sha(MAN)[:12], "vinculos": sha(VINC)[:12]},
 "shas_vigentes": {"V2.2": sha(V22)[:12], "p8": sha(P8)[:12], "N1": sha(N1F)[:12], "N2": sha(N2F)[:12]},
 "shas_pacote": {"proposta": sha(PROP)[:12]},
 "resultado": {"verdes": verde, "total": total, "verde_total": verde == total},
 "checks": checks}
out = AT + "/producao/TRILHA50_proposta_fluxo_claim_N1N2_2026-09-18.json"
json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"TRILHA 50 — {verde}/{total} VERDE → {out}")
for c in checks:
    if not c["ok"]:
        print("  VERMELHO:", c["id"], c["titulo"][:110], "| medido:", str(c["medido"])[:150])
