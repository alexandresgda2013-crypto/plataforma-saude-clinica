# TRILHA 64 — 2026-09-20 (rodada 47) — Réplica empírica da DELIBERAÇÃO do mestre
# (fluxo do claim clínico) + refação da CARTA 19 (v2) após chegada dos bytes.
# Política da casa: replicar ANTES de aceitar/comentar. Régua: regex + escopo +
# chave + sha, camada declarada. open() texto = universal newlines; CRLF em bytes.
import hashlib, json, re, os
from pathlib import Path

BASE = Path("/home/user")
S = BASE / "BIBLIOTECAS/_documentos_serie"
AT = BASE / "BIBLIOTECAS/B01_Neuroinflamacao/atuais"
KIT = S / "KIT_CLINICA_recebido_2026-09-15"
checks = []
def reg(nome, ok, det): checks.append({"check": nome, "ok": bool(ok), "detalhe": det})
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

UP_DELI = BASE / "uploads/DELIBERACAO_FLUXO_CLAIM_CLINICO_2026-09-18.md"
SR_DELI = S / "MESTRE_deliberacao_fluxo_claim_recebida_2026-09-20/DELIBERACAO_FLUXO_CLAIM_CLINICO_2026-09-18.md"
LISTA = KIT / "5º LISTA CANÔNICA — B1  SM-02 V1.3.md"
BLOCO = KIT / "6º BLOCO DE ESTADO  v1.6.md"
V22 = S / "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
MINUTA = S / "MESTRE_LNT_minuta1_recebido_2026-09-18/L-NT_CONTRATO_UNIDADES_NARRATIVAS_minuta1_294119b9_2026-09-18.md"
PROPOSTA = S / "OPERADOR_PROPOSTA_fluxo_claim_N1N2_recebido_2026-09-18/OPERADOR_PROPOSTA_FORMALIZACAO_FLUXO_CLAIMS_CLINICOS_2026-09-18.md"
CARTA_V2 = S / "CARTA19_MESTRE_2026-09-20/CARTA_19_AO_AUDITOR_MESTRE_2026-09-20_v2.md"
V1_SUPER = S / "CARTA19_MESTRE_2026-09-20/SUPERSEDED_CARTA_19_AO_AUDITOR_MESTRE_2026-09-20_v1.md"
PACOTE = BASE / "ENTREGAS/2026-09-20_CARTA19_MESTRE"
ZIP_CRT = PACOTE / "CARTA_19_AO_AUDITOR_MESTRE_2026-09-20_v2.zip"

CIENCIA = {
 "V7": (AT / "B1 NEUROINFLAMAÇÃO V7 CANONICA.md", "6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238"),
 "manifesto": (AT / "Evidencias/Bibliografia/_manifesto_biblioteca.json", "79d1309a168922d0e8bf43736cd5b21c8b361bdf64e3b200eeeafd43806f3a9c"),
 "vinculos": (AT / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", "490675e63122a24baebd8890f4a7883a07f68916d90562e74adf309133501d1b"),
}
def ciencia_ok(): return all(sha(p) == h for p, h in CIENCIA.values())

reg("C01 ciencia trio intacto (inicio)", ciencia_ok(), {k: sha(p)[:12] for k,(p,_) in CIENCIA.items()})

# C02 — arquivo da deliberação: série ≡ upload, digital e medidas
b = SR_DELI.read_bytes()
reg("C02 deliberacao arquivada: serie == upload · sha · 8141 b · 115 linhas",
    sha(UP_DELI) == sha(SR_DELI) == "fe5a18b3542305014147cf85d00676b4b92d483453c8d04fe331b8a5b5536543"
    and len(b) == 8141 and len(b.decode("utf-8").splitlines()) == 115,
    f"sha={sha(SR_DELI)} bytes={len(b)} linhas={len(b.decode('utf-8').splitlines())}")

txt = SR_DELI.read_text(encoding="utf-8")
# C03 — veredito e estrutura declarados no texto
reg("C03 veredicto B + 1 estrutural + 3 de precisao + 4 pedidos no texto",
    all(a in txt for a in [
        "VEREDITO: **B — concordância com ajustes**",
        "Um ajuste é estrutural e precisa ser resolvido antes do L-NT fechar. Os outros três são de precisão.",
        "Escrevo a minuta 2 assim que essa decisão for registrada"]),
    "marcadores de veredito/estrutura/fecho presentes")

# C04 — os arquivos-base citados pelo mestre são byte-idênticos ao acervo da casa
reg("C04 arquivos-base dele == acervo (LISTA 3252a920... / BLOCO 0a630dba...)",
    sha(LISTA) == "3252a920c6e972f21804f0488d6fd34df49ea59c6e23c8dd21e3ebf1239a37dd"
    and sha(BLOCO) == "0a630dba84f2f03d0d0aa727308a9b6eefef15cd7e0be0e7ae080b7f377756ae",
    f"LISTA={sha(LISTA)[:12]} BLOCO={sha(BLOCO)[:12]}")

# C05 — réplica §2: 41 / 22 / 21 / 8+14
lista = LISTA.read_text(encoding="utf-8"); bloco = BLOCO.read_text(encoding="utf-8")
ids = set(re.findall(r"^\s*-?\s*id:\s*(B1\.SM02\.\d+[a-z]?)\s*$", lista, re.M))
sec = bloco.split("claims_aprovados:", 1)[1].split("# LOG DE EXCLUSÃO", 1)[0].split("# ============================================")[0]
idsB = set(re.findall(r"\n\s*-?\s*[Cc]laim_id:\s*(B1\.SM02\.\d+[a-z]?)", sec))
n_entradas = len(idsB)
from collections import Counter
st = Counter(re.findall(r"status:\s*([a-z_]+)", sec))
fora_lista = sorted(idsB - ids)
sem = len(ids - idsB)
# C55-1 honrada: "sem entrada" é medida de CONJUNTO, não aritmética cega (41-22=19 ≠ 21).
# A interseção é 20 porque o BLOCO carrega dois subclaims não-listados (.012b/.012c)
# — convergente com a trilha 33, que já anotava o corpo da v1.6 com 22 entries incl. .012b/.012c.
reg("C05 replica secao 2: 41 alvos · 22 entradas · 21 sem (=|Lista-Bloco|, interseccao 20) · 8 aprovado + 14 com_ressalva",
    len(ids) == 41 and n_entradas == 22 and len(ids & idsB) == 20 and sem == 21
    and fora_lista == ["B1.SM02.012b", "B1.SM02.012c"]
    and st.get("aprovado") == 8 and st.get("aprovado_com_ressalva") == 14,
    f"alvos={len(ids)} entradas={n_entradas} interseccao={len(ids&idsB)} sem={sem} "
    f"no_bloco_fora_da_lista={fora_lista} status={dict(st)} "
    f"(regua: ids '^\\s*-?\\s*id:' LISTA x claim_id da secao claims_aprovados; 21=|41-20| por conjunto, nao 41-22)")

# C06 — réplica §3: 12 campos (régua: substring 'chave:' no BLOCO INTEIRO)
esp = {"pmid":158,"autor":37,"ano":41,"nivel":39,"especie":25,"comparador":48,
       "achado":52,"papel":36,"evidence_role":22,"uso":23,"moderadores":22,"statement":22}
med = {k: len(re.findall(rf"{k}:", bloco)) for k in esp}
uso_anc = len(re.findall(r"^\s*uso:", bloco, re.M))
reg("C06 replica secao 3: 12/12 campos iguais ao declarado (uso 23 = 22 ancoradas + 1 interna)",
    med == esp and uso_anc == 22,
    f"medido={med} uso_ancoradas={uso_anc} (regua: substring 'chave:' no BLOCO inteiro — "
    f"68? nao: na secao isolada pmid=66; a regua que casa as 12 medidas e' o arquivo inteiro)")

# C07 — réplica §1: 49 únicos · 39 ausentes · wiring zero (2 faces)
pm = set(re.findall(r"pmid:\s*\"?(\d{7,9})\"?", sec))
acervo = set(); sm02 = 0
for f in ("01_pmids.json","02_meta_analises.json","03_ensaios_clinicos.json"):
    for r in json.load(open(AT / "Evidencias/Bibliografia" / f)):
        p = str(r.get("pmid_oficial") or "").strip()
        if p and p.lower() not in ("none","null"): acervo.add(p)
        if str(r.get("claim_id_origem") or "").startswith("B1.SM02."): sm02 += 1
nao = Counter(re.findall(r"usado_em_biblioteca:\s*([a-z]+)", sec))
aus = len([p for p in pm if p not in acervo])
reg("C07 replica secao 1: 49 pmids unicos x 237 acervo -> 39 ausentes · wiring zero",
    len(pm) == 49 and len(acervo) == 237 and aus == 39
    and nao.get("nao") == 22 and sm02 == 0,
    f"unicos={len(pm)} acervo_com_pmid={len(acervo)} ausentes={aus} "
    f"usado_em_biblioteca_nao={nao.get('nao')} fichas_SM02_no_acervo={sm02} "
    f"(regua regex trilha33 r'pmid:\\s*\"?(\\d{{7,9}})\"?' na secao; claim_id_origem B1.SM02.*)")

# C08 — quotes na V2.2 oficial: §6 exato; §5.5 = paráfrase de sentido correto
v = V22.read_text(encoding="utf-8")
s6 = all(a in v for a in ["1. consumir o conhecimento da Biblioteca correspondente;",
                          "2. utilizar as Evidências/Vínculos necessárias à rastreabilidade;"])
s55_sent = ("A Biblioteca de origem explica a relação; a Biblioteca correspondente contém "
            "o aprofundamento específico do objeto científico.") in v
s55_dele = "a correspondente contém o aprofundamento do objeto" in v
reg("C08 quotes V2.2: §6 L446-447 exato · §5.5 L421 parafrase de sentido correto (literal registrado)",
    s6 and s55_sent and not s55_dele,
    f"sec6_exato={s6} · s55_literal_V22={s55_sent} · s55_forma_dele_ausente_na_V22={not s55_dele}")

# C09 — minuta L-NT: NT-02 / N-4 / herança uso (3 marcadores)
m = MINUTA.read_text(encoding="utf-8")
reg("C09 minuta L-NT 294119b9...: NT-02 (claim_origem inexistente na Biblioteca) · N-4 (uso=clinico exige origem humana) · 'uso herdado do kit'",
    sha(MINUTA).startswith("294119b9") and "NT-02" in m and "`claim_origem` inexistente na Biblioteca" in m
    and "N-4" in m and "`uso` herdado do kit" in m,
    f"sha={sha(MINUTA)[:12]} · 3 marcadores presentes")

# C10 — proposta no acervo: 35 · item13 · percurso sem Biblioteca Correspondente · papel L215
p = PROPOSTA.read_text(encoding="utf-8")
lins = p.splitlines()
s3 = "\n".join(lins[114:382]); s10 = "\n".join(lins[382:479])
ocorre_35 = p.count("os 35")
reg("C10 proposta 4ede1c81...: 'os 35' >= 2 · item 13 ressalva · §3/§10 sem 'Biblioteca Correspondente' · L215 papel do mestre",
    sha(PROPOSTA).startswith("4ede1c81") and ocorre_35 >= 2
    and "13. procedimento de auditoria para claims aprovados com ressalva" in p
    and s3.count("Correspondente") == 0 and s10.count("Correspondente") == 0
    and "coordena a transformação do resultado em N1/N2" in p,
    f"sha={sha(PROPOSTA)[:12]} ocorrencias_os35={ocorre_35} · 'Correspondente' no §3={s3.count('Correspondente')} · §10={s10.count('Correspondente')} "
    f"(paráfrase do mestre na forma verbal; literal L215 registrado)")

# C11 — carta 19 v2: digital + marcadores + 0 eco antecipado de aprovação
SHA_ESP_V2 = "74e1e1cbe415870dbe3b865c9fe6435ea864dd5db1e0e11bf0d6dabbf5d7e6f2"
c = CARTA_V2.read_text(encoding="utf-8")
ag = ["fe5a18b3542305014147cf85d00676b4b92d483453c8d04fe331b8a5b5536543",
      "1444ae441186565ac147fe02f5637c1f75f3147335d1d2252c3ff21e2e01e819",
      "72f8f2e5ea7ec0ad553fa25ee2976da53b0f896a1a6c3e3ed81279d2e58ba235",
      "b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da",
      "d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050",
      "309aa65f", "41 alvos", "39 ausentes", "VERIFICADA", ".012b"]
reg("C11 carta 19 v2: sha exato + 9 marcadores + 0 'APROVADO: V2.3'",
    sha(CARTA_V2) == SHA_ESP_V2 and all(a in c for a in ag) and "APROVADO: V2.3" not in c,
    f"sha={sha(CARTA_V2)} bytes={CARTA_V2.stat().st_size} marcadores={[a in c for a in ag]}")

# C12 — pacote ENTREGAS (R-DOWNLOAD-SEMPRE): zip re-extraído ≡ disco · v1 SUPERSEDED com sha conhecido
import zipfile
dig = (PACOTE / "DIGITAIS_2026-09-20.txt").read_text(encoding="utf-8")
with zipfile.ZipFile(ZIP_CRT) as z:
    re_md = z.read("CARTA_19_AO_AUDITOR_MESTRE_2026-09-20_v2.md")
    nomes = set(z.namelist())
reg("C12 pacote entrega: zip re-extraido == serie · DIGITAIS com 2 shas · v1 superseded arquivada (c2f799d6...)",
    re_md == CARTA_V2.read_bytes() and SHA_ESP_V2 in dig
    and "fe5a18b3542305014147cf85d00676b4b92d483453c8d04fe331b8a5b5536543" in dig
    and nomes == {"CARTA_19_AO_AUDITOR_MESTRE_2026-09-20_v2.md", "DIGITAIS_2026-09-20.txt"}
    and sha(V1_SUPER) == "c2f799d621b5b2e768f322471c69ed6925f6614f57270aed5ecd57de2d717a49",
    f"zip={sha(ZIP_CRT)} v1={sha(V1_SUPER)[:12]}")

# C13 — glob DELIBERACAO: exatamente o par upload+série, byte-idênticos (C56-2: exclui trilha)
hits = []
for root, dirs, files in os.walk(BASE):
    for n in files:
        if "DELIBERACAO" in n.upper() and "TRILHA64" not in n:
            hits.append(str(Path(root)/n).replace(str(BASE)+"/", ""))
esperado = {"uploads/DELIBERACAO_FLUXO_CLAIM_CLINICO_2026-09-18.md",
            "BIBLIOTECAS/_documentos_serie/MESTRE_deliberacao_fluxo_claim_recebida_2026-09-20/DELIBERACAO_FLUXO_CLAIM_CLINICO_2026-09-18.md"}
reg("C13 glob DELIBERACAO == par upload+serie, byte-identicos (a divida de bytes morreu)",
    set(hits) == esperado and UP_DELI.read_bytes() == SR_DELI.read_bytes(), hits)

reg("C14 ciencia trio intacto (fim)", ciencia_ok(), {k: sha(p)[:12] for k,(p,_) in CIENCIA.items()})

n_ok = sum(1 for x in checks if x["ok"])
out = {
 "trilha": 64, "data": "2026-09-20", "rodada": 47,
 "titulo": "Replica empirica da DELIBERACAO do mestre (fluxo claim clinico) + carta 19 v2",
 "veredito_da_replica": "VERIFICADO — todas as medidas do mestre replicaram EXATAS (41/22/21 · 8+14 · 12/12 campos · 49x237->39 · wiring zero 2 faces · quotes §6 exatas · NT-02/N-4/herança uso presentes · proposta: 35/item13/sem-Biblioteca/L215). 2 precisões de citação (§5.5 L421 · proposta L215): essência correta, literal registrado.",
 "checks": checks, "ok": n_ok, "total": len(checks),
 "confissoes": [
   "C64-1: C05 FALHOU na 1a corrida (13/14) por aritmetica cega da casa: testou 41-22==21 (falso, da 19). A regua certa e' conjunto: |Lista - Bloco| = 41 - 20 = 21, porque o Bloco guarda dois subclaims nao-listados (.012b/.012c) — com regua correta, a tabela do mestre fica INTEIRA EXATA. Mesma licenca da C55-1: contagem != classificacao.",
   "1a. sondagem exploratoria (fora do script) mediu pmid=66/achado=51 na SECAO claims_aprovados divergindo de 158/52; a regua que casa as 12 medidas do mestre e' substring 'chave:' no BLOCO INTEIRO — registrada em C06.",
   "Transito: a casa pediu os bytes na carta 19 v1 e eles ja estavam disponibilizados pela frente desde 18/09 — o elo que faltou foi o repasse do lado da casa/operador. v1 SUPERSEDED arquivada (c2f799d6...)."
 ]
}
js = AT / "producao/TRILHA64_replica_deliberacao_mestre_2026-09-20.json"
js.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"TRILHA 64: {n_ok}/{len(checks)} verdes · json={js.name}")
for x in checks: print(("OK " if x["ok"] else "FALHA ") + x["check"])
