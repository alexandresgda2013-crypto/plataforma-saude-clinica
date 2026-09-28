#!/usr/bin/env python3
# TRILHA 52 — rodada 33 — 2026-09-18
# Objeto: DIVERGÊNCIA DOCUMENTAL "duas V2.2" — o projeto do mestre tem
#         ARQUITETURA_CONSOLIDADA_DA_PLATAFORMA_V2__-__15_09_26.md sha 309aa65f…
#         (relato: ≠ V2.1 só em §§2/21, 28 seções idênticas, SEM origem_conhecimento,
#          prevalência-da-prosa, "fora do cânone"); a casa declarou vigente df7f7cfd…
# Método: inventário de bytes + marcas por elo + comparação por seções + cadeia documentada.
#         0 ciência. 309aa65f NÃO está no workspace — confronto byte-a-byte final pendente dos bytes.
import json, re, hashlib, os, glob, unicodedata as ud

BASE = "/home/user"
DOC  = BASE + "/BIBLIOTECAS/_documentos_serie"
AT   = BASE + "/BIBLIOTECAS/B01_Neuroinflamacao/atuais"
V7   = AT + "/B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
MAN  = AT + "/Evidencias/Bibliografia/_manifesto_biblioteca.json"
VINC = AT + "/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
P8   = BASE + "/Ferramentas de geração e auditoria/06_portao_P8_coerencia/scripts/validar_coerencia_camadas.py"
DEC  = AT + "/Auditoria_B1/decisoes_B1.md"
CHL  = BASE + "/BIBLIOTECAS/CHANGELOG_GERAL.md"
STS  = BASE + "/BIBLIOTECAS/STATUS_SIMPLES_2026-09-13.md"
V22  = DOC + "/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
V21  = DOC + "/SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.1  -  17.09.26.md"
V2O  = DOC + "/SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md"
UPL  = BASE + "/uploads/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md"
V1   = BASE + "/uploads/ARQUITETURA CONSOLIDADA DA PLATAFORMA.MD"
PONT = DOC + "/ARQUITETURA_VIGENTE.txt"
ACHD = DOC + "/MESTRE_achado_V21_no_unificado_recebido_2026-09-17/ACHADO_V21_NO_UNIFICADO_2026-09-17.md"
R14  = DOC + "/RESPOSTA_14_MESTRE_ACHADO_V21_NO_UNIFICADO_V22_INSTALADA_2026-09-17.md"
AD2  = DOC + "/ADENDO_2_RESPOSTA13_ARQUITETURA_V21_INSTALADA_2026-09-17.md"
T45  = AT + "/producao/TRILHA45_achado_mestre_V21_no_unificado_2026-09-17.json"
MNT  = DOC + "/MESTRE_LNT_minuta1_recebido_2026-09-18/L-NT_CONTRATO_UNIDADES_NARRATIVAS_minuta1_294119b9_2026-09-18.md"
REL  = DOC + "/RELATORIO_CASA_divergencia_dupla_V22_2026-09-18.md"

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def sha_b(b): return hashlib.sha256(b).hexdigest()
def rd(p):  return ud.normalize("NFC", open(p, encoding="utf-8").read())
def secs_of(p):
    raw = open(p, "rb").read().decode("utf-8")
    lines = raw.split("\r\n") if "\r\n" in raw else raw.split("\n")
    idx = [i for i, l in enumerate(lines) if re.match(r"^# \d+\.", l)]
    out = {}
    for k, i in enumerate(idx):
        end = idx[k + 1] if k + 1 < len(idx) else len(lines)
        num = re.match(r"^# (\d+)\.", lines[i]).group(1)
        out.setdefault(num, []).append("\n".join(lines[i:end]))
    return out
checks = []
def reg(cid, titulo, camada, escopo, comando, medido, esperado, ok, detalhe="", regex=None):
    checks.append({"id": cid, "titulo": titulo, "camada": camada, "escopo": escopo,
                   "comando": comando, "medido": medido, "esperado": esperado,
                   "ok": bool(ok), "detalhe": detalhe, **({"regex": regex} if regex else {})})

# ---- S0 selos ----
reg("S0.1", "V7 intacta", "ingerida sha256", V7, "sha256sum", sha(V7)[:12], "6e2c2979", sha(V7).startswith("6e2c2979"))
reg("S0.2", "Manifesto intacto", "ingerida sha256", MAN, "sha256sum", sha(MAN)[:12], "79d1309a", sha(MAN).startswith("79d1309a"))
reg("S0.3", "Vínculos intactos (274)", "ingerida sha256", VINC, "sha256sum", sha(VINC)[:12], "490675e6", sha(VINC).startswith("490675e6"))
reg("S0.4", "P-8 oficial intacto", "ingerida sha256", P8, "sha256sum", sha(P8)[:12], "be48a5ef", sha(P8).startswith("be48a5ef"))
reg("S0.5", "V2.2 instalada intacta e = o ponteiro oficial", "ingerida sha256 × documental", V22 + " × " + PONT,
    "sha × grep ponteiro",
    sha(V22)[:12] + " · ponteiro cita df7f7cfdfc01=" + str("df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1" in rd(PONT)),
    "df7f7cfd nos dois", sha(V22).startswith("df7f7cfd") and "df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1" in rd(PONT))

# ---- A inventário: 309aa65f não está aqui ----
achou = []
for raiz, _, fs in os.walk(BASE):
    if "node_modules" in raiz: continue
    for f in fs:
        if f.endswith((".md", ".MD")):
            p = os.path.join(raiz, f)
            try:
                if sha(p).startswith("309aa65f"): achou.append(p)
            except Exception: pass
reg("A1", "O artefato do mestre (sha 309aa65f…) NÃO existe no workspace da casa → (b)-fina exige os bytes; (b)-documental já está medida por conteúdo/seções",
    "ingerida sha256 global, camada: todos *.md sob /home/user", "/home/user (varredura .md)",
    "find + sha256sum por arquivo", json.dumps(achou), "[] (ausente)", len(achou) == 0,
    detalhe="PEDIDO (obrigatório para selar a identidade): operador envia o arquivo ARQUITETURA_CONSOLIDADA_DA_PLATAFORMA_V2__-__15_09_26.md do projeto do mestre → a casa arquiva verbatim e executa o diff byte-a-byte")

# ---- B marcas e forma por elo ----
elos = {"V1-upload": V1, "V2-15.09(09692e18)": V2O, "upload-r24(5be36836)": UPL, "V2.1(1a50645e)": V21, "V2.2-inst(df7f7cfd)": V22}
marcas = {}
for nome, p in elos.items():
    t = rd(p); raw = open(p, "rb").read()
    s = secs_of(p)
    dup = {n: len(v) for n, v in s.items() if len(v) > 1}
    h1 = [l[:70] for l in t.split("\n") if l.startswith("# ")][:1]
    marcas[nome] = {
        "oc": t.casefold().count("origem_conhecimento"),
        "prev": len(re.findall(r"prevalece[^.\n]*desenho|prosa[^.\n]*prevalece", t.casefold())),
        "fora": t.casefold().count("fora do cânone"),
        "secoes": len([1 for v in s.values() for _ in v]), "dup": dup, "crlf": b"\r\n" in raw,
        "h1": h1, "bytes": len(raw)}
reg("B1", "As 3 marcas do relato do mestre (origem_conhecimento · prevalência-da-prosa · 'fora do cânone') existem SOMENTE na df7f7cfd (3·1·1); em TODOS os outros elos da cadeia: 0·0·0 — logo o arquivo do projeto dele NÃO é a V2.2 instalada; é um elo anterior rotulado",
    "documental NFC+casefold por elo, arquivo inteiro", "5 elos da cadeia",
    "count 3 agulhas por elo",
    json.dumps({k: (v["oc"], v["prev"], v["fora"]) for k, v in marcas.items()}),
    "só df7f7cfd: (3,1,1); resto 0",
    marcas["V2.2-inst(df7f7cfd)"]["oc"] == 3 and marcas["V2.2-inst(df7f7cfd)"]["prev"] == 1 and marcas["V2.2-inst(df7f7cfd)"]["fora"] == 1
    and all(v["oc"] == 0 and v["prev"] == 0 and v["fora"] == 0 for k, v in marcas.items() if k != "V2.2-inst(df7f7cfd)"),
    detalhe="linhas âncora na df7f7cfd: L4 (Rev. V2.2) · L117 ('fora do cânone', bloco Pasta) · L121 (desenho origem_conhecimento=) · L172 (prosa origem_conhecimento = canonico | atualizacao) · L175 ('a prosa deste documento prevalece sobre os desenhos')")
reg("B2", "Forma dos elos (H1 · seções '# N.' · duplicatas · CRLF): upload-r24 tem H1 'V2 … 15.09.26' + duplicata §21×2; V2.1 tem H1 idem + duplicata §2×2; APENAS a df7f7cfd tem H1 'V2.2 … 17.09.26' + 30 seções únicas",
    "documental NFC+regex '^# \\d+\\.' por linha", "upload r24 × V2.1 × V2.2",
    r"re.findall('^# (\d+)\.') + H1 + CRLF",
    json.dumps({k: {"h1": marcas[k]["h1"], "n": marcas[k]["secoes"], "dup": marcas[k]["dup"], "crlf": marcas[k]["crlf"]} for k in ("upload-r24(5be36836)", "V2.1(1a50645e)", "V2.2-inst(df7f7cfd)") }),
    "assinaturas registradas",
    marcas["upload-r24(5be36836)"]["dup"] == {"21": 2} and marcas["V2.1(1a50645e)"]["dup"] == {"2": 2}
    and marcas["V2.2-inst(df7f7cfd)"]["dup"] == {} and "V2.2" in (marcas["V2.2-inst(df7f7cfd)"]["h1"][0] if marcas["V2.2-inst(df7f7cfd)"]["h1"] else ""),
    regex=r"^# (\d+)\.")

# ---- C comparação por seções (a assinatura do relato do mestre) ----
su, sa, sb = secs_of(UPL), secs_of(V21), secs_of(V22)
def diff_secs(s1, s2):
    nums = sorted(set(s1) | set(s2), key=int)
    dif = [n for n in nums if s1.get(n) != s2.get(n)]
    same = [n for n in nums if len(s1.get(n, [])) == 1 and s1.get(n) == s2.get(n)]
    return dif, same
d_ua, s_ua = diff_secs(su, sa)
reg("C1", "A ASSINATURA DO RELATO BATE EXATA: upload-r24 × V2.1-instalada = 28 seções idênticas; DIFEREM exatamente §2 e §21 (§§6·7·13·14 entre as 28) — a V2.2 do projeto do mestre é, em conteúdo, o upload da rodada 24 (pré-achado) com rótulo 'V2.2'",
    "documental por-fatias (# N.) sobre bytes, NFC", "upload r24 × V2.1 instalada",
    "secs_of × compare por seção",
    f"idênticas={len(s_ua)} dif={d_ua}", "28 · ['2','21']",
    d_ua == ["2", "21"] and len(s_ua) == 28 and all(n in s_ua for n in ("6", "7", "13", "14")),
    detalhe="o relato do mestre ('28 idênticas · só §§2/21 · §§6/7/13/14 byte a byte') é EXATAMENTE esta assinatura — identificação por conteúdo fechada; identidade byte-a-byte só quando os bytes chegarem")
d_ab, s_ab = diff_secs(sa, sb)
reg("C2", "O que a casa (por decisão do operador) acrescentou: V2.1 → V2.2-instalada difere SOMENTE no §2 (29 idênticas) — é o ACHADO do próprio mestre (2841bc66) + parecer concorrente do comentador",
    "documental por-fatias", "V2.1 × V2.2 instalada", "secs_of × compare",
    f"idênticas={len(s_ab)} dif={d_ab}", "29 · ['2']",
    d_ab == ["2"] and len(s_ab) == 29)
d_ub, s_ub = diff_secs(su, sb)
reg("C3", "E portanto: upload-r24 (≈ conteúdo do arquivo do mestre) × V2.2-instalada diferem em §2 e §21 (28 idênticas) — (b) documental congelada",
    "documental por-fatias", "upload r24 × V2.2 instalada", "secs_of × compare",
    f"idênticas={len(s_ub)} dif={d_ub}", "28 · ['2','21']",
    d_ub == ["2", "21"] and len(s_ub) == 28)
ra, rb = open(V21, "rb").read(), open(V22, "rb").read()
ia, ib = ra.find(b"# 3."), rb.find(b"# 3.")
reg("C4", "Prova byte-a-byte (re-verificada): sufixo §3→fim de V2.1 e V2.2-instalada é IDÊNTICO (39.165 bytes) — o conteúdo normativo usado pelo L-NT (§§6·7·13·14) é o mesmo nos dois lados; a afirmação do mestre sobre suficiência de conteúdo está CORRETA",
    "ingerida bytes, fatia posicional", "V2.1 × V2.2", "raw.find('# 3.') × == sufixos",
    f"A={ia} B={ib} iguais={ra[ia:] == rb[ib:]} len={len(ra[ia:])}", "True · 39165",
    ra[ia:] == rb[ib:] and len(ra[ia:]) == 39165)

# ---- D cadeia documentada (resposta 'd') ----
dec = rd(DEC)
ok_d1 = "## Rev.33" in dec and "df7f7cfd" in dec and "1a50645e" in dec and "2841bc66" in dec
reg("D1", "decisoes rev.33 documenta a instalação da df7f7cfd (achado 2841bc66 · V2.1 1a50645e → SUPERSEDED · decisão opção A do operador)",
    "documental NFC, 4 substrings", DEC, "grep", str(ok_d1), "presentes", ok_d1)
pont = rd(PONT)
ok_d2 = ("correcao arquitetural LOCALIZADA" in pont) and ("opção A" in pont or "opcao A" in pont) and ("prosa prevalece" in pont.casefold()) and ("SUPERSEDED" in pont)
reg("D2", "ARQUITETURA_VIGENTE.txt registra escopo cirúrgico, origem (decisão opção A) e a cadeia SUPERSEDED",
    "documental NFC+casefold", PONT, "4 substrings", str(ok_d2), "presentes", ok_d2)
ok_d3 = os.path.exists(ACHD) and sha(ACHD).startswith("2841bc66")
reg("D3", "O ACHADO que gerou a V2.2 (2841bc66) está arquivado verbatim e íntegro", "ingerida sha256 + fs",
    ACHD, "sha256sum", str(ok_d3), "presente", ok_d3)
ok_d4 = os.path.exists(R14) and os.path.exists(AD2)
reg("D4", "As cartas de instalação (RESPOSTA_14, V2.2) e de anúncio (ADENDO_2_RESPOSTA_13, V2.1) existem — a rota oficial de repasse ao mestre consta",
    "ingerida fs", DOC, "os.path.exists ×2", str(ok_d4), "2/2", ok_d4,
    detalhe="NOTA-DÍVIDA da casa (nova, nomeada D-V22-BYTES-PROJETO): os BYTES da V2.2 instalada seguem não confirmados no projeto do mestre — a divergência de hoje é a prova; o repasse do ARQUIVO (não só a carta) é o passo que fecha a identidade")
ok_d5 = os.path.exists(T45)
t45_info = None
if ok_d5:
    j = json.load(open(T45, encoding="utf-8"))
    ch = j.get("checks", [])
    ok_all = isinstance(ch, list) and len(ch) > 0 and all(c.get("ok") for c in ch if isinstance(c, dict) and "ok" in c) if ch else None
    t45_info = {"checks": len(ch) if isinstance(ch, list) else None, "todos_ok": ok_all,
                "resultado_tem_PROCEDENTE": "PROCEDENTE" in str(j.get("resultado", ""))}
reg("D5", "Trilha 45 reexecutável arquivada e verde (checks todos ok + 'PROCEDENTE') — a mesma prova do sufixo byte-a-byte reexecutada hoje em C4",
    "ingerida json (schema legado: resultado é string descritiva + checks[])", T45,
    "json.load × len(checks) × all(ok) × 'PROCEDENTE'",
    json.dumps(t45_info, ensure_ascii=False), "todos ok · PROCEDENTE",
    ok_d5 and t45_info.get("todos_ok") and t45_info.get("resultado_tem_PROCEDENTE"),
    detalhe="CONFISSÃO C6 (datada): o script lia 'resultado.verde_total' — o schema legado da trilha 45 guarda 'resultado' como STRING; leitura corrigida para checks[]+marcador. Nenhum dado histórico afetado; o arquivo da trilha 45 estava e está íntegro.")

# ---- E o L-NT não precisa mudar; a citação correta já é df7f7cfd ----
mnt = rd(MNT)
ok_e1 = "df7f7cfd" in mnt and "309aa65f" not in mnt
reg("E1", "Resposta objetiva ao ponto do mestre: a Minuta 1 JÁ cita o sha correto (df7f7cfd) no cabeçalho e NÃO cita 309aa65f — logo NÃO se corrige a minuta para 309aa65f; a correção é trocar o ARQUIVO no projeto dele (309aa65f → df7f7cfd)",
    "documental substring ×2", MNT, "grep shas", f"cita df7f7cfd={'df7f7cfd' in mnt} cita 309aa65f={'309aa65f' in mnt}",
    "Sim · Não", ok_e1,
    detalhe="PEDIDO ao mestre (via operador): substituir o arquivo do projeto pelos bytes da df7f7cfd (52.181 b, CRLF) e re-verificar sha; após isso a identidade fecha e NADA muda no conteúdo normativo dele")

# ---- H governança ----
reg("H1", "decisoes rev.40 registrada (rodada 33)", "documental NFC", DEC,
    "substring", str("## Rev.40 — 2026-09-18 (rodada 33" in dec), "presente",
    "## Rev.40 — 2026-09-18 (rodada 33" in dec)
chl = rd(CHL)
reg("H2", "CHANGELOG ABERTURA 33 + RESULTADO 33", "documental NFC", CHL,
    "substring", str("ABERTURA 33 + RESULTADO 33" in chl), "presente",
    "ABERTURA 33 + RESULTADO 33" in chl)
sts = rd(STS)
reg("H3", "STATUS_SIMPLES bloco da rodada 33", "documental NFC", STS,
    "substring", str("## Rodada 33 — 18/09/2026" in sts), "presente",
    "## Rodada 33 — 18/09/2026" in sts)
ok_h4 = os.path.exists(REL) and os.path.getsize(REL) > 5000
reg("H4", "Relatório da casa ao operador (divergência dupla V2.2) emitido", "ingerida fs", REL,
    "exists + size>5000", str(os.path.getsize(REL)) if os.path.exists(REL) else "pendente", ">5000", ok_h4)

verde = sum(1 for c in checks if c["ok"]); total = len(checks)
res = {
 "trilha": "TRILHA52", "rodada": 33, "data": "2026-09-18",
 "objeto": "Divergência documental dupla-V2.2 (mestre: 'V2.2' sha 309aa65f no projeto dele, sem as 3 guardas × casa: vigente df7f7cfd). Resposta a (a)-(d) do operador, medida. 0 ciência.",
 "resposta_abcd_medida": {
   "a": "SIM — df7f7cfd é posterior e editada SOB DECISÃO REGISTRADA (rodada 26, opção A do operador), aplicando o ACHADO do próprio mestre (2841bc66); não é edição espúria — é a instalação oficial.",
   "b": "Documental medida: upload-r24 (≈ conteúdo do arquivo do mestre, assinatura C1 exata) × df7f7cfd diferem em §2 (nó UNIFICADOS removido · fluxos segregados até o Motor · bloco Pasta com 'fora do cânone' · origem_conhecimento desenho+prosa · regra 'prosa prevalece sobre desenhos' · H1 V2→V2.2-17.09 · 30 seções únicas) e §21 consolidada. (b)-fina byte-a-byte: pendente dos bytes do 309aa65f.",
   "c": "VIGENTE RECOMENDADA: df7f7cfd — única com as 3 guardas (exigidas pelo achado do próprio mestre), rastreabilidade completa e conteúdo §§6/7/13/14 idênticos nos dois lados.",
   "d": "Documentação: decisoes rev.33 · ARQUITETURA_VIGENTE.txt · trilhas 45/45b · ACHADO 2841bc66 · RESPOSTA_14 + ADENDO_2_RESPOSTA_13 · CHANGELOG rodada 26."},
 "confissoes_e_erratas_datadas_2026_09_18": [
   "C0 (script): faltou o argumento posicional 'escopo' no reg A1 (TypeError antes de qualquer medida) e o caminho da trilha 45 presumiu um nome abreviado; corrigidos com o nome real medido em produção ('TRILHA45_achado_mestre_V21_no_unificado_2026-09-17.json'). Nenhuma medida afetada.",
   "C6 (D5): leitura do JSON legado da trilha 45 esperava 'resultado.verde_total'; o schema legado guarda 'resultado' como string. Corrigido para checks[]+'PROCEDENTE'.",
   "NOTA-DÍVIDA NOVA (não é confissão): D-V22-BYTES-PROJETO — os bytes da V2.2 instalada seguem não confirmados no projeto do mestre; a divergência de hoje é a prova. Repasse do arquivo fecha a identidade."],
 "shas_ciencia": {"V7": sha(V7)[:12], "manifesto": sha(MAN)[:12], "vinculos": sha(VINC)[:12]},
 "shas_vigentes": {"V2.2": sha(V22)[:12], "p8": sha(P8)[:12]},
 "cadeia_shas": {"V1_upload": sha(V1)[:12], "V2_1509": sha(V2O)[:12], "upload_r24": sha(UPL)[:12],
                  "V2.1": sha(V21)[:12], "V2.2": sha(V22)[:12], "alvo_mestre_309aa65f": "AUSENTE do workspace"},
 "resultado": {"verdes": verde, "total": total, "verde_total": verde == total},
 "checks": checks}
out = AT + "/producao/TRILHA52_divergencia_dupla_V22_2026-09-18.json"
json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"TRILHA 52 — {verde}/{total} VERDE → {out}")
for c in checks:
    if not c["ok"]:
        print("  VERMELHO:", c["id"], c["titulo"][:100], "| medido:", str(c["medido"])[:140])
