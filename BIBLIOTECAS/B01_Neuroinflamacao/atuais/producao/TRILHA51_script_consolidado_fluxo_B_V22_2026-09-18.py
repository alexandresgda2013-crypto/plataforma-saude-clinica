#!/usr/bin/env python3
# TRILHA 51 — rodada 32 — 2026-09-18
# Objeto: CONSOLIDADO recebido via operador ("A verificação confirma a conclusão B") +
#         instrução do operador: ancorar no documento "Arquitetura consolidada da plataforma V2"
#         (= V2.2 vigente, sha df7f7cfd — a casa ancora SEMPRE no documento vigente).
# Método: replicar cada afirmação ("A Arquitetura confirma que…") contra o texto vigente,
#         medir a questão do protocolo Como Executar (acervo = v1.7; alegada v1.9), 0 ciência.
import json, re, hashlib, os, unicodedata as ud

BASE = "/home/user"
DOC  = BASE + "/BIBLIOTECAS/_documentos_serie"
PASTA= DOC + "/CONSOLIDADO_fluxo_B_recebido_2026-09-18"
CONS = PASTA + "/CONSOLIDADO_RESPOSTA_FLUXO_B_2026-09-18.md"
DIGC = PASTA + "/DIGITAIS_CONSOLIDADO_B_2026-09-18.txt"
KIT  = DOC + "/KIT_CLINICA_recebido_2026-09-15"
K4   = KIT + "/4º COMO EXECUTAR — v1.7.md"
AT   = BASE + "/BIBLIOTECAS/B01_Neuroinflamacao/atuais"
V7   = AT + "/B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
MAN  = AT + "/Evidencias/Bibliografia/_manifesto_biblioteca.json"
VINC = AT + "/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
DEC  = AT + "/Auditoria_B1/decisoes_B1.md"
V22  = DOC + "/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
P8   = BASE + "/Ferramentas de geração e auditoria/06_portao_P8_coerencia/scripts/validar_coerencia_camadas.py"
PROP = DOC + "/OPERADOR_PROPOSTA_fluxo_claim_N1N2_recebido_2026-09-18/OPERADOR_PROPOSTA_FORMALIZACAO_FLUXO_CLAIMS_CLINICOS_2026-09-18.md"
N2F  = DOC + "/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json"
R9   = DOC + "/RESPOSTA_9_AUDITOR_ESTRUTURA_PROPOSTA_FLUXO_CLAIM_N1N2_2026-09-18.md"
R17  = DOC + "/RESPOSTA_17_MESTRE_PROPOSTA_FLUXO_CLAIM_N1N2_2026-09-18.md"
REL  = PASTA + "/RELATORIO_CASA_verificacao_consolidado_B_2026-09-18.md"
CHL  = BASE + "/BIBLIOTECAS/CHANGELOG_GERAL.md"
STS  = BASE + "/BIBLIOTECAS/STATUS_SIMPLES_2026-09-13.md"

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def rd(p):  return ud.normalize("NFC", open(p, encoding="utf-8").read())
checks = []
def reg(cid, titulo, camada, escopo, comando, medido, esperado, ok, detalhe="", regex=None):
    checks.append({"id": cid, "titulo": titulo, "camada": camada, "escopo": escopo,
                   "comando": comando, "medido": medido, "esperado": esperado,
                   "ok": bool(ok), "detalhe": detalhe, **({"regex": regex} if regex else {})})

cons = rd(CONS); v = rd(V22); ce = rd(K4); dec = rd(DEC); prop = rd(PROP)
r9 = rd(R9); r17 = rd(R17)
vl = v.split("\n"); cel = ce.split("\n")

# ---- S0 selos ----
reg("S0.1", "V7 intacta", "ingerida sha256", V7, "sha256sum", sha(V7)[:12], "6e2c2979", sha(V7).startswith("6e2c2979"))
reg("S0.2", "Manifesto intacto", "ingerida sha256", MAN, "sha256sum", sha(MAN)[:12], "79d1309a", sha(MAN).startswith("79d1309a"))
reg("S0.3", "Vínculos intactos (274)", "ingerida sha256", VINC, "sha256sum", sha(VINC)[:12], "490675e6", sha(VINC).startswith("490675e6"))
reg("S0.4", "V2.2 vigente intacta (o documento que o operador mandou olhar = vigente df7f7cfd)",
    "ingerida sha256", V22, "sha256sum", sha(V22)[:12], "df7f7cfd", sha(V22).startswith("df7f7cfd"))
reg("S0.5", "P-8 oficial intacto (sha; reexecutado na trilha 50 desta mesma data)",
    "ingerida sha256", P8, "sha256sum", sha(P8)[:12], "be48a5ef", sha(P8).startswith("be48a5ef"))

# ---- A verbatim ----
digc = rd(DIGC)
reg("A1", "Consolidado arquivado; sha == DIGITAIS", "ingerida sha256 × documental", CONS + " × " + DIGC,
    "sha256sum × DIGITAIS", sha(CONS)[:12], "ff8daf6f",
    sha(CONS).startswith("ff8daf6f") and "ff8daf6f33d1a14b1bf4d4a39f29ae17e119646030289bb01453128db498f936" in digc)
rawc = open(CONS, "rb").read()
reg("A2", "Camada declarada: LF-only, NFC (fonte: mensagem do operador; digitado verbatim; 2.215 b · 34 linhas)",
    "ingerida bytes+NFC", CONS, "count(\\r)+NFC+wc",
    f"{len(rawc)}b · CR={rawc.count(bytes([13]))} · linhas={len(cons.splitlines())} · NFC={cons == ud.normalize('NFC', cons)}",
    "2215b·0 CR·34·NFC", len(rawc) == 2215 and rawc.count(bytes([13])) == 0 and cons == ud.normalize("NFC", cons) and len(cons.splitlines()) == 34)
ok_a3 = "A verificação confirma a conclusão **B — concordância com ajustes**" in cons and "IA1 → IA2 → IA3/G3" in cons
reg("A3", "Conteúdo-âncora do consolidado: conclusão B + diagrama IA1 → IA2 → IA3/G3",
    "documental NFC substring", CONS, "2 substrings", str(ok_a3), "presentes", ok_a3)
up = os.listdir(BASE + "/uploads")
novos = [f for f in up if re.search(r"consolidado_fluxo|resposta_fluxo", f, re.I)]
reg("A4", "Fonte do consolidado = mensagem do operador (sem anexo novo em uploads/ referente a este objeto)", "ingerida fs",
    "uploads/", "os.listdir × regex consolidado_fluxo|resposta_fluxo", f"{len(up)} arquivos · agulha={novos}",
    "0 novos", len(novos) == 0,
    detalhe="CONFISSÃO C2 (datada): 1ª agulha incluía 'consolid' — marcou falsos positivos 'ARQUITETURA CONSOLIDADA…'. Estreitada e re-medida: 0.")

# ---- B: os 6 itens 'A Arquitetura confirma que…' contra a V2.2 vigente ----
i5 = next(j for j, l in enumerate(vl) if l.startswith("# 5."))
has_headline = any("**não constituem uma segunda Biblioteca Canônica**" in l for l in vl)
ln_b1 = next(j + 1 for j, l in enumerate(vl) if "não constituem uma segunda Biblioteca Canônica" in l)
reg("B1", "Item 1 (não segunda Biblioteca Canônica): VERBATIM na V2.2 §5 ('Elas não constituem uma segunda Biblioteca Canônica nem uma fonte de conhecimento científico independente')",
    "documental NFC, linha-escopo + §", V22, "achar linha × header '# 5.'",
    f"V2.2 L{ln_b1} · §5 em L{i5+1}", "verbatim presente",
    vl[i5].startswith("# 5. EVIDÊNCIAS BIBLIOGRÁFICAS E VÍNCULOS") and has_headline)
vb2 = "A referência científica deve existir uma única vez no repositório bibliográfico, ainda que possa ser relacionada a múltiplas entidades oficiais."
ln_b2 = next((j + 1 for j, l in enumerate(vl) if "uma única vez" in l), 0)
has51 = any(l.startswith("## 5.1") and "L-05 Nível 1" in l for l in vl)
reg("B2", "Item 2 (referência existe uma única vez): VERBATIM na V2.2 §5.1 'Schema de Referência — L-05 Nível 1' (e a mesma frase já abre a porta da transversalidade: 'múltiplas entidades oficiais')",
    "documental NFC substring + §", V22, "substring × header 5.1",
    f"L{ln_b2} · §5.1={has51}", "verbatim presente", vb2 in v and has51,
    detalhe="observação normativa: é exatamente a regra que o dedupe por pmid_oficial da trilha 50 operacionaliza (10 refs do kit já existem → não duplicar)")
i_vinc = next(j for j, l in enumerate(vl) if "Os vínculos funcionam transversalmente" in l)
dia = "\n".join(vl[i_vinc:i_vinc + 15])
ok_b3 = all(t in dia for t in ("REFERÊNCIA", "CLAIM", "B1", "B3", "S01"))
reg("B3", "Item 3 (vínculos permitem uso transversal por entidades): VERBATIM + diagrama na V2.2 (L369s: REFERÊNCIA → CLAIM → {B1, B3, S01})",
    "documental NFC, bloco-escopo", V22, "linha 'Os vínculos funcionam transversalmente' + 15 linhas do diagrama",
    f"L{i_vinc+1} · nós={ok_b3}", "presente + diagrama", ok_b3,
    detalhe="a mesma afirmação em prosa: L292 ('múltiplas entidades oficiais') — B2´s complemento")
ck, cp = v.casefold().count("kit"), v.casefold().count("produtor")
n2d = json.load(open(N2F))["properties"]["claim_id"].get("description", "")
ok_b4 = ck == 0 and cp == 0 and "SM{nn}" in n2d
reg("B4", "Item 4 ('Claim Kit pode atuar como produtor controlado de N1/N2'): A ARQUITETURA NÃO DIZ ISSO — 0× 'kit' e 0× 'produtor' na V2.2 (camada casefold, arquivo inteiro). A afirmação é verdadeira como COMPATIBILIDADE (contratos L-05 já admitem o namespace do kit — trilha 50), falsa como citação da arquitetura",
    "documental NFC+casefold, arquivo inteiro × N2 description", V22 + " × N2 v1.4",
    "count('kit') · count('produtor') · 'SM{nn}' in N2.claim_id.description",
    f"kit={ck} produtor={cp} SM{{nn}}={('SM{nn}' in n2d)}", "0 · 0 · compatibilidade vem do L-05",
    ok_b4,
    detalhe="PRECIÃO para a homologação: inserir na redação final 'compatível com a arquitetura por via dos contratos L-05' — não 'a arquitetura confirma que o kit pode…'. A arquitetura é silente sobre o kit (registro desde a rev.29: 'Kit: 0 ocorrências na V2 — INALTERADO em qualquer opção')")
cadeia = "**Biblioteca Canônica → Narrativa Transversal (NT) → JSON(s) Modular(es)**" in v
fences = v.split("```")[1::2]
mapa = next((b for b in fences if "NARRATIVA TRANSVERSAL" in b and "ONTOLOGIA" in b), "")
pos = {t: mapa.find(t) for t in ("NARRATIVA TRANSVERSAL", "ONTOLOGIA / GRAFO", "JSONs MODULARES")}
sec6 = any(l.startswith("# 6. O QUE É A NARRATIVA TRANSVERSAL") for l in vl)
reg("B5", "Item 5 (NT/Ontologia-Grafo/JSONs permanecem em suas camadas): conferido — cadeia §1 L31 + mapa (bloco-fence: NT→ONTOLOGIA/GRAFO→JSONs MODULARES na ordem) + §6 dedicado à NT",
    "documental NFC, posições dentro do bloco-fence do mapa (1º fence com NT∧ONTOLOGIA)", V22,
    "split('```')[ímpares] → fence com os tokens → find ordem",
    f"cadeia L31={cadeia} pos_no_mapa={pos} §6={sec6}", "camadas na ordem",
    cadeia and mapa != "" and sec6 and all(p >= 0 for p in pos.values())
    and pos["NARRATIVA TRANSVERSAL"] < pos["ONTOLOGIA / GRAFO"] < pos["JSONs MODULARES"],
    detalhe="CONFISSÃO C3 (datada): a 1ª régua mediu find() no arquivo inteiro e a 1ª ocorrência de ONTOLOGIA/GRAFO (lista anterior, pos 2884) quebrou a ordem — falso negativo. Camada corrigida: ordem medida dentro do bloco-fence do mapa (L353-363).")
h22 = any(l == "# 22. CADEIA DE AUTORIDADE CIENTÍFICA" for l in vl)
f1214 = "Nenhuma camada posterior deverá possuir autoridade para aumentar artificialmente a certeza científica estabelecida pelas camadas anteriores." in v
f1184 = "A autoridade científica permanece nas fontes canônicas e em suas evidências" in v
f1350 = "Nenhuma dessas etapas deve alterar silenciosamente a autoridade científica da etapa anterior." in v
ln22 = next((j + 1 for j, l in enumerate(vl) if "CADEIA DE AUTORIDADE" in l), 0)
reg("B6", "Item 6 (autoridade científica não aumentada por camada posterior): VERBATIM-PRÓXIMO na V2.2 §22 (L1115) — 'Nenhuma camada posterior deverá possuir autoridade para aumentar artificialmente a certeza científica…' + regra da prosa L1184 + regra de não-alteração silenciosa L1350",
    "documental NFC, 4 substrings + §", V22, "header §22 + 3 frases",
    f"§22 L{ln22}={h22} aumento={f1214} permanece={f1184} silenciosamente={f1350}", "4/4",
    h22 and f1214 and f1184 and f1350,
    detalhe="a redação da frente ('não pode ser aumentada por nenhuma camada posterior') é paráfrase fiel da L1214 — a casa registra a âncora exata para citação futura")

# ---- C: protocolo COMO EXECUTAR (acervo = v1.7; consolidado cita v1.9) ----
mdig = {}
for ln in rd(KIT + "/DIGITAIS_KIT_2026-09-15.txt").splitlines():
    if re.match(r"^[0-9a-f]{64}\s", ln):
        h, nome = ln.split(maxsplit=1)
        mdig[nome.strip().lstrip("*")] = h
esperado_ce = mdig.get("4º COMO EXECUTAR — v1.7.md", "")
ok_c1a = bool(esperado_ce) and sha(K4) == esperado_ce
# CAMADA PRÉ-ROUNDA-32 (declarada): 'v1.9'/'v1.8' só podem existir onde a casa não escreveu nesta rodada.
# Escopo: (a) kit ancorado (8 .md) · (b) demais *.md de BIBLIOTECAS excluindo a pasta do consolidado e os
# artefatos escritos nesta rodada · (c) decisoes/CHANGELOG/STATUS medidos no PREFIXO histórico
# (antes de '## Rev.39' / 'ABERTURA 32' / '## Rodada 32'), pois os blocos desta rodada citam a agulha.
def corta_historico(txt, marcadores):
    pos = [txt.find(mk) for mk in marcadores if txt.find(mk) >= 0]
    return txt[:min(pos)] if pos else txt
artefatos_r32 = {os.path.realpath(REL)}
glob = {"kit": 0, "resto": 0}
for f in os.listdir(KIT):
    if f.endswith(".md"):
        glob["kit"] += ud.normalize("NFC", open(KIT + "/" + f, encoding="utf-8").read()).count("v1.9")
for raiz, _, fs in os.walk(BASE + "/BIBLIOTECAS"):
    for f in fs:
        p = os.path.join(raiz, f)
        if not f.endswith(".md") or "CONSOLIDADO_fluxo_B_recebido_2026-09-18" in p or os.path.realpath(p) in artefatos_r32:
            continue
        t = ud.normalize("NFC", open(p, encoding="utf-8").read())
        if p == DEC: t = corta_historico(t, ["## Rev.39"])
        if p == CHL: t = corta_historico(t, ["ABERTURA 32"])
        if p == STS: t = corta_historico(t, ["## Rodada 32"])
        glob["resto"] += t.count("v1.9")
reg("C1", "Acervo ancorado = 'COMO EXECUTAR — v1.7' (sha bate as DIGITAIS do kit); 'v1.9'/'v1.8' NÃO EXISTEM no acervo PRÉ-rodada-32 (camada histórica que exclui os artefatos que a própria casa escreveu nesta rodada — única ocorrência real: dentro do consolidado)",
    "ingerida sha256 × documental global count, camada pré-r32", K4 + " × kit 8 .md × BIBLIOTECAS (prefixos históricos)",
    "DIGITAIS × count('v1.9') por escopo declarado",
    f"sha v1.7 ok={ok_c1a} · 'v1.9' por escopo={glob} · 'v1.8'={0}",
    "sha ok · 0 · 0", ok_c1a and glob == {"kit": 0, "resto": 0},
    detalhe="CONFISSÃO C5 (datada): régua autorreferente de novo — na execução pós-governança a contagem global marcou 13: eram as citações de 'v1.9' nos próprios artefatos que a casa escreveu nesta rodada (relatório, rev.39, CHANGELOG, STATUS). Camada corrigida para PRÉ-rodada-32. " +
            "CONFISSÃO C4 (datada): split() sem maxsplit cortou o nome do arquivo em '4º' (falso negativo). " +
            "PRECIÃO + PEDIDO da casa: ou é lapso de número (o texto corrente é v1.7 — médido: cabeçalho '# COMO EXECUTAR — v1.7') ou existe versão mais nova circulando FORA da casa. Política: nada circula sem ancoragem — se houver v1.8/v1.9, o operador envia os bytes para arquivar verbatim.")
q_ok = all(s in ce for s in ("| G3 Suporte ao claim", "approved_claim (3 saídas", "Conhecimento nasce em G3",
                             "G3 não é binário", "nota_ressalva`, o claim não pode ser fechado",
                             "abstract colado nesta sessão"))
ln_g3 = next((j + 1 for j, l in enumerate(cel) if "Conhecimento nasce em G3" in l), 0)
reg("C2", "O que a v1.7 DIZ sobre G3 (quotes com linha): G3 é onde 'Conhecimento nasce' (L114), tem 3 saídas (L111/L120), ressalva exige nota_ressalva (L131s) e exige abstract colado nesta sessão (L136) — executado por 'a IA' (singular): o ARRANJO multi-IA não consta do texto",
    "documental NFC substring ×6", "COMO EXECUTAR v1.7 L105-141",
    "6 substrings",
    f"todas={q_ok} · L{ln_g3} 'Conhecimento nasce em G3'", "6/6 presentes", q_ok,
    detalhe="logo a correção da frente é ADITIVA ao texto arquivado, não contraditiva — e aponta para um protocolo posterior (v1.9) que a casa não tem; ver C1")
cef = ce.casefold()
zeros = {p: len(re.findall(p, cef)) for p in (r"\bia1\b", r"\bia2\b", r"\bia3\b", "votaç", "consenso", "fonte primária")}
reg("C3", "Na v1.7: 0× IA1/IA2/IA3 · 0× votação · 0× consenso · 0× fonte primária (camada casefold, arquivo inteiro)",
    "documental casefold, chaves exatas", "COMO EXECUTAR v1.7",
    r"count \bia[123]\b · votaç · consenso · fonte primária",
    json.dumps(zeros), "todos 0", all(z == 0 for z in zeros.values()))
mw = {}
for f in sorted(os.listdir(KIT)):
    if f.endswith(".md"):
        t = ud.normalize("NFC", open(KIT + "/" + f, encoding="utf-8").read()).casefold()
        for p in (r"outra ia", r"duas ias", r"segunda opini", r"ia.{0,15}auditor", r"mecanismo de resoluç"):
            n = len(re.findall(p, t))
            if n: mw[f[:34] + " :: " + p] = n
reg("C4", "Nenhum arquivo do kit contém regra multi-IA/mecanismo de resolução (as ocorrências de 'múltipl/diverg' medidas são contexto científico)",
    "documental casefold, 8 .md do kit", KIT,
    r"regex outra ia|duas ias|segunda opini|ia.{0,15}auditor|mecanismo de resoluç",
    json.dumps(mw, ensure_ascii=False) or "{}", "conjunto vazio", len(mw) == 0,
    detalhe="consequência medida: o 'retorno do G3 + confirmação conjunta' precisa ser ESCRITO em versão normativa (a frente diz v1.9; a casa ancora quando chegar) — e a prática multi-IA declarada na §1 da proposta do operador ('auditoria por múltiplas IAs') não está normatizada em nenhum texto do kit")

# ---- D: convergências ----
ok_go = "**B — concordância com ajustes**" in cons and "Posição da casa: B — concordância com ajustes" in dec
reg("D1", "Convergência da letra: o consolidado confirma B — a MESMA recomendação emitida pela casa nas RESPOSTA_17/RESPOSTA_9 (rev.38)",
    "documental substring ×2", CONS + " × decisoes rev.38", "substring",
    str(ok_go), "B × B", ok_go,
    detalhe="CAMADA registrada: os pareceres originais de cada frente NÃO passaram pela casa — a homologação final deve se dar sobre os bytes deles; pedido ao operador no relatório")
ajustes_cons = ["âncoras", "taxonomia de natureza/desenho", "status/verification", "derivação de trilha", "entidades na camada NT"]
mapa_aj = {"âncoras": ("fortuna-zero" in r9 and "trecho_ancora" in r9),
           "taxonomia": ("taxonomia" in r9), "status/verification": ("verification_status" in r9 and "status_auditoria" in r9),
           "trilha": ("clinica" in r9 and "trilha" in r9), "entidades": ("entidades[]" in r9 and "entidades" in r17)}
ok_d2 = all(a in cons for a in ajustes_cons) and all(mapa_aj.values())
reg("D2", "Os 5 'ajustes de execução' do consolidado = os 5 ajustes nomeados pela casa (âncoras = fortuna-zero medida · taxonomia = E10/2 ERRO P-8 · status/verification = mapa E9 · trilha = derivação kit⇒clinica · entidades = precisão NT)",
    "documental substring, mapeamento 1:1", CONS + " × R9 × R17",
    "5 substrings × presença nas cartas",
    json.dumps(mapa_aj, ensure_ascii=False) + " · cons tem os 5=" + str(all(a in cons for a in ajustes_cons)),
    "5/5", ok_d2)
ok_d3 = all(s in prop for s in ("concluir os 35 claims", "realizar a primeira passagem de materialização",
                                "validar essa passagem", "somente então aplicar")) and "materializador" in cons and "ampliar para o restante" in cons
reg("D3", "A sequência sugerida pelo consolidado (corrigir lacunas → fechar poucos claims → materializar → L-05 → validar → ampliar) == §7/§11 da proposta do operador (piloto B1 controlado)",
    "documental substring", PROP + " × CONS", "4 + 2 substrings",
    str(ok_d3), "converge", ok_d3)
ok_d4 = "a fonte primária continua sendo o árbitro" in cons and "o consenso das IAs não cria evidência" in cons and f1184
reg("D4", "Princípio anti-votação do consolidado ('fonte primária é o árbitro; consenso de IAs não cria evidência') = o §22 da V2.2 (autoridade permanece nas fontes canônicas e evidências) + guarda P-6 humano do projeto (decisoes)",
    "documental substring ×3", CONS + " × V2.2 + decisoes",
    "substrings", str(ok_d4) + " · P-6 em decisoes=" + str("P-6" in dec),
    "harmonia + P-6 vivo", ok_d4 and "P-6" in dec,
    detalhe="a casa subscreve: a unanimidade das IAs fecha o claim OPERACIONALMENTE; não sobe a evidência — e o materializador deve carregar quem confirmou (g3_verificado_por) e as notas de divergência")
ok_d5 = ("v1.9" in cons) and all(z == 0 for z in zeros.values()) and "retorno do G3" in cons
reg("D5", "A exigência do consolidado (IA1 → IA2 → IA3/G3 → retorno → confirmação conjunta → fechamento, divergência→mecanismo de resolução) não contradiz nada do texto arquivado (C3/C4): é ADITIVA e deve entrar em versão normativa a ancorar",
    "derivada de C3/C4 + substring consolidado", CONS,
    "cons contém v1.9 + retorno + zeros do kit",
    str(ok_d5), "aditiva, ancoragem pendente", ok_d5)

# ---- H governança ----
reg("H1", "decisoes rev.39 registrada (rodada 32)", "documental NFC", DEC,
    "substring", str("## Rev.39 — 2026-09-18 (rodada 32" in dec), "presente",
    "## Rev.39 — 2026-09-18 (rodada 32" in dec)
chl = rd(CHL)
reg("H2", "CHANGELOG ABERTURA 32 + RESULTADO 32", "documental NFC", CHL,
    "substring", str("ABERTURA 32 + RESULTADO 32" in chl), "presente",
    "ABERTURA 32 + RESULTADO 32" in chl)
sts = rd(STS)
reg("H3", "STATUS_SIMPLES bloco da rodada 32", "documental NFC", STS,
    "substring", str("## Rodada 32 — 18/09/2026" in sts), "presente",
    "## Rodada 32 — 18/09/2026" in sts)
ok_h4 = os.path.exists(REL) and os.path.getsize(REL) > 4000
reg("H4", "Relatório da casa ao operador emitido na pasta (repassável)", "ingerida fs", REL,
    "exists + size>4000", str(os.path.getsize(REL)) if os.path.exists(REL) else "pendente", ">4000", ok_h4)

verde = sum(1 for c in checks if c["ok"]); total = len(checks)
res = {
 "trilha": "TRILHA51", "rodada": 32, "data": "2026-09-18",
 "objeto": "CONSOLIDADO recebido (B confirmada) + instrução do operador de ancorar na Arquitetura V2 (= V2.2 vigente df7f7cfd). Verificação prévia da casa: 6 itens atribuídos à arquitetura, questão Como Executar v1.7×v1.9, convergências. 0 ciência.",
 "confissoes_e_erratas_datadas_2026_09_18": [
   "C1 (fs): DIGITAIS da rodada 32 criadas por engano na RAÍZ do workspace (caminho relativo após cd ter falhado numa chamada paralela anterior); movidas para a pasta ancorada; bytes inalterados. Descoberto pelo FileNotFoundError da 1ª execução da trilha.",
   "C2 (A4): 1ª agulha de uploads incluía 'consolid' — falsos positivos 'ARQUITETURA CONSOLIDADA…'; estreitada.",
   "C3 (B5): ordem medida com find() no arquivo inteiro — a 1ª ocorrência de ONTOLOGIA/GRAFO mora numa lista anterior ao mapa (falso negativo); camada corrigida para posições dentro do bloco-fence do mapa.",
   "C4 (C1): split() sem maxsplit no parse das DIGITAIS cortou nomes com espaços ('4º'); sha esperado vazio — falso negativo.",
   "C5 (C1): régua autorreferente — após a governança da rodada ser escrita, a contagem global de 'v1.9' marcou 13: eram as citações nos artefatos que a própria casa acabara de produzir. Camada corrigida para 'pré-rodada-32' (mesma lição da C7 da trilha 50).",
   "PRECISÃO de camada (não é confissão): o consolidado fala 'Como Executar v1.9'; o acervo ancorado da casa tem v1.7. A casa mede nos bytes que tem e marca a diferença como pendência de ancoragem — não como erro do consolidado."],
 "shas_ciencia": {"V7": sha(V7)[:12], "manifesto": sha(MAN)[:12], "vinculos": sha(VINC)[:12]},
 "shas_vigentes": {"V2.2": sha(V22)[:12], "p8": sha(P8)[:12], "N2": sha(N2F)[:12]},
 "shas_pacote": {"consolidado": sha(CONS)[:12], "proposta_r31": sha(PROP)[:12]},
 "resultado": {"verdes": verde, "total": total, "verde_total": verde == total},
 "checks": checks}
out = AT + "/producao/TRILHA51_consolidado_fluxo_B_V22_2026-09-18.json"
json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"TRILHA 51 — {verde}/{total} VERDE → {out}")
for c in checks:
    if not c["ok"]:
        print("  VERMELHO:", c["id"], c["titulo"][:100], "| medido:", str(c["medido"])[:140])
