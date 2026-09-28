# TRILHA 63 — 2026-09-20 (rodada 46) — CARTA 19 ao Auditor-Mestre
# Objetivo: reexecutável. Mede tudo que a carta 19 referencia: V2.2 oficial,
# schemas correntes N1 v1.3 / N2 v1.4, zips de envio (2026-09-19), verbatim do
# mestre r45, varredura DELIBERACAO na base (=0), pacote ENTREGAS da carta
# (zip re-extraído == disco) e ciência B1 intocada (início e fim).
# Régua da casa: regex + escopo + chave + sha · open() em texto aplica
# universal newlines → contagens de CRLF feitas em BYTES. Camada: documental.
import hashlib, json, zipfile, re, os
from pathlib import Path

BASE = Path("/home/user")
S = BASE / "BIBLIOTECAS/_documentos_serie"
P = BASE / "ENTREGAS"
checks = []
def reg(nome, ok, det): checks.append({"check": nome, "ok": bool(ok), "detalhe": det})
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

V22_SERIE = S / "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
V22_ENTR  = P / "2026-09-19_V2.2_OFICIAL/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
DIST = P / "2026-09-19_SCHEMAS_L05_CORRENTES_DISTRIBUICAO"
N1 = DIST / "schema_referencia_v1.3__N1_CORRENTE.json"
N2 = DIST / "schema_vinculo_v1.4__N2_CORRENTE.json"
ESP = DIST / "L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4__ESPECIFICACAO.md"
LEIAME = DIST / "LEIAME.txt"
MESTRE_R45 = S / "MESTRE_resposta_carta18_V23_2026-09-19/RESPOSTA_MESTRE_a_carta18_V23_2026-09-19.md"
CARTA_SERIE = S / "CARTA19_MESTRE_2026-09-20/CARTA_19_AO_AUDITOR_MESTRE_2026-09-20.md"
PACOTE = P / "2026-09-20_CARTA19_MESTRE"
CARTA_ZIP = PACOTE / "CARTA_19_AO_AUDITOR_MESTRE_2026-09-20.zip"
ZIP_V22 = P / "2026-09-19_V2.2_OFICIAL/ARQUITETURA_V2.2_OFICIAL_2026-09-19.zip"
ZIP_SCH = DIST / "SCHEMAS_L05_CORRENTES_2026-09-19.zip"

CIENCIA = {
 "V7": ("BIBLIOTECAS/B01_Neuroinflamacao/atuais/B1 NEUROINFLAMAÇÃO V7 CANONICA.md",
        "6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238"),
 "manifesto": ("BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia/_manifesto_biblioteca.json",
        "79d1309a168922d0e8bf43736cd5b21c8b361bdf64e3b200eeeafd43806f3a9c"),
 "vinculos": ("BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json",
        "490675e63122a24baebd8890f4a7883a07f68916d90562e74adf309133501d1b"),
}
def ciencia_ok():
    return all(sha(BASE / p) == h for _, (p, h) in CIENCIA.items())

# C07 — ciência no INÍCIO
reg("C07 ciencia trio intacto (inicio)", ciencia_ok(),
    {k: sha(BASE / p)[:12] for k, (p, _) in CIENCIA.items()})

# C01 — V2.2 oficial (série)
b = V22_SERIE.read_bytes()
h = hashlib.sha256(b).hexdigest()
reg("C01 V2.2 oficial serie (sha, 52181 b, CRLF 1411)",
    h == "df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1"
    and len(b) == 52181 and b.count(b"\r\n") == 1411,
    f"sha={h} bytes={len(b)} crlf={b.count(b'\r\n')}")

# C02 — V2.2 entrega ≡ série
reg("C02 V2.2 entrega == serie (bytes identicos)",
    V22_ENTR.read_bytes() == b, f"sha_entrega={sha(V22_ENTR)}")

# C03 — schemas correntes
h1, h2 = sha(N1), sha(N2)
reg("C03 schemas correntes N1 v1.3 / N2 v1.4",
    h1 == "b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da"
    and h2 == "d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050",
    f"N1={h1} ({N1.stat().st_size} b) N2={h2} ({N2.stat().st_size} b)")

# C04 — verbatim mestre r45 (fonte das citações da carta)
hm = sha(MESTRE_R45)
reg("C04 verbatim mestre r45 == 1817615d...",
    hm == "1817615de2fbc8de529d8ab2339dc58459107595f63c0b2dbc7f33b7c6a8fb66", f"sha={hm}")

# C05 — varredura global DELIBERACAO em NOMES de arquivo = 0
# (lição C56-2: excluir artefatos da própria trilha 63)
proprios = {"TRILHA63"}
hits = []
for root, dirs, files in os.walk(BASE):
    for n in files:
        if "DELIBERACAO" in n.upper() and not any(t in n for t in proprios):
            hits.append(str(Path(root) / n).replace(str(BASE) + "/", ""))
reg("C05 glob DELIBERACAO na base == 0 ocorrencias (fora trilha 63)",
    len(hits) == 0, hits if hits else "0 ocorrencias — o pedido de bytes da carta-19 §3 procede")

# C06 — re-extração dos zips de envio (2026-09-19) e conferência de conteúdo
exp_v22 = {"ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md": sha(V22_SERIE)}
with zipfile.ZipFile(ZIP_V22) as z:
    ok1 = all(hashlib.sha256(z.read(n)).hexdigest() == v for n, v in exp_v22.items()) and len(z.namelist()) == 1
exp_sch = {p.name: sha(p) for p in (N1, N2, ESP, LEIAME)}
with zipfile.ZipFile(ZIP_SCH) as z:
    ok2 = set(z.namelist()) == set(exp_sch) and all(
        hashlib.sha256(z.read(n)).hexdigest() == v for n, v in exp_sch.items())
reg("C06 zips de envio re-extraidos: V2.2 sha + schemas 4/4",
    ok1 and ok2, f"zipV22={sha(ZIP_V22)} zipSCH={sha(ZIP_SCH)}")

# C08 — carta 19: digital exata + marcadores obrigatórios (norma trilateral: python NFC)
SHA_CARTA_ESP = "c2f799d621b5b2e768f322471c69ed6925f6614f57270aed5ecd57de2d717a49"
txt = CARTA_SERIE.read_text(encoding="utf-8")  # universal newlines (camada declarada)
h_c = sha(CARTA_SERIE)
agulhas = {
 "sha V2.2 oficial": "df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1",
 "sha N1 v1.3": "b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da",
 "sha N2 v1.4": "d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050",
 "sha zip V2.2": "1444ae441186565ac147fe02f5637c1f75f3147335d1d2252c3ff21e2e01e819",
 "sha zip schemas": "72f8f2e5ea7ec0ad553fa25ee2976da53b0f896a1a6c3e3ed81279d2e58ba235",
 "alvo do pedido (nome do arquivo)": "DELIBERACAO_FLUXO_CLAIM_CLINICO_2026-09-18.md",
 "pedido secundario 309aa65f": "309aa65f",
 "verbatim mestre r45 arquivado": "1817615de2fbc8de529d8ab2339dc58459107595f63c0b2dbc7f33b7c6a8fb66",
 "eco impraticado antecipadamente (nao deve constar)": "APROVADO: V2.3",
}
pres = {k: (ag in txt) for k, ag in agulhas.items()}
ok_marc = all(pres[k] for k in list(agulhas)[:-1]) and not pres[list(agulhas)[-1]]
reg("C08 carta 19: sha exato + 8 marcadores presentes + 0 eco antecipado de aprovacao",
    h_c == SHA_CARTA_ESP and ok_marc, f"sha={h_c} bytes={CARTA_SERIE.stat().st_size} presenca={pres}")

# C09 — pacote ENTREGAS: zip re-extraído ≡ disco; DIGITAIS contém o sha da carta
dig = (PACOTE / "DIGITAIS_2026-09-20.txt").read_text(encoding="utf-8")
with zipfile.ZipFile(CARTA_ZIP) as z:
    re_carta = z.read("CARTA_19_AO_AUDITOR_MESTRE_2026-09-20.md")
    nomes = z.namelist()
reg("C09 pacote datado (R-DOWNLOAD-SEMPRE): re-extracao == disco + DIGITAIS consistente",
    re_carta == CARTA_SERIE.read_bytes() and SHA_CARTA_ESP in dig and len(nomes) == 2,
    f"zip={sha(CARTA_ZIP)} itens={nomes}")

# C10 — ciência no FIM
reg("C10 ciencia trio intacto (fim)", ciencia_ok(),
    {k: sha(BASE / p)[:12] for k, (p, _) in CIENCIA.items()})

n_ok = sum(1 for c in checks if c["ok"])
out = {
 "trilha": 63, "data": "2026-09-20", "rodada": 46,
 "titulo": "CARTA 19 ao Auditor-Mestre — pedido da deliberacao do fluxo claim + envio V2.2 oficial e schemas L-05",
 "camada": "documental (0 ciencia tocada)",
 "checks": checks, "ok": n_ok, "total": len(checks),
 "artefatos": {
   "carta_serie": str(CARTA_SERIE).replace(str(BASE) + "/", ""),
   "carta_sha": h_c,
   "pacote_entrega": str(PACOTE).replace(str(BASE) + "/", ""),
   "zip_carta_sha": sha(CARTA_ZIP),
 },
 "confissoes": [
   "C63-1: 1a execucao falhou por desempacotamento de tupla no dicionario CIENCIA "
   "(items() devolve (chave,(caminho,sha)); o codigo lia (caminho,sha)) — FileNotFoundError "
   "imediato, nenhuma medida fabricada; corrigido e reexecutado. Mesma classe da C62-1."
 ]
}
js = BASE / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA63_carta19_mestre_2026-09-20.json"
js.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"TRILHA 63: {n_ok}/{len(checks)} verdes · json={js.name}")
for c in checks:
    print(("OK " if c["ok"] else "FALHA ") + c["check"])
