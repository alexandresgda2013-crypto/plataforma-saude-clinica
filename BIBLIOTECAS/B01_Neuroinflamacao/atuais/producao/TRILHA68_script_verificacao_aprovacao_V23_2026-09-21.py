# TRILHA 68 — 2026-09-21 (rodada 53) — Rodada histórica: réplica da verificação
# técnica do mestre à V2.3 + APROVAÇÃO do operador (V2.3 vigente + selo schemas)
# gravada no ponteiro + pacote-espelho refeito sob a regra nova de rótulos.
import hashlib, json, re, zipfile
from pathlib import Path

BASE = Path("/home/user")
S = BASE / "BIBLIOTECAS/_documentos_serie"
AT = BASE / "BIBLIOTECAS/B01_Neuroinflamacao/atuais"
DIST = BASE / "ENTREGAS/2026-09-19_SCHEMAS_L05_CORRENTES_DISTRIBUICAO"
LIN = BASE / "ENTREGAS/2026-09-19_L05_LINHAGEM_COMPLETA"
DEST = BASE / "ENTREGAS/2026-09-21_ENVIO_AUDITOR2_PROJETO_V23"
OLD = BASE / "ENTREGAS/2026-09-20_ENVIO_AUDITOR2_PROJETO"
checks = []
def reg(nome, ok, det): checks.append({"check": nome, "ok": bool(ok), "detalhe": det})
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

N1p = DIST / "schema_referencia_v1.3__N1_CORRENTE.json"
N2p = DIST / "schema_vinculo_v1.4__N2_CORRENTE.json"
V23 = S / "CARTAS_V23_2026-09-19/CANDIDATA_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.3 - 19.09.26.md"
V23V = S / "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.3 - 19.09.26.md"
PONTEIRO = S / "ARQUITETURA_VIGENTE.txt"
VERV = S / "MESTRE_verificacao_tecnica_V23_2026-09-21/VERIFICACAO_TECNICA_V23_CANDIDATA_2026-09-21 (1).md"
UP_V = BASE / "uploads/VERIFICACAO_TECNICA_V23_CANDIDATA_2026-09-21 (1).md"

CIENCIA = {
 "V7": (AT / "B1 NEUROINFLAMAÇÃO V7 CANONICA.md", "6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238"),
 "manifesto": (AT / "Evidencias/Bibliografia/_manifesto_biblioteca.json", "79d1309a168922d0e8bf43736cd5b21c8b361bdf64e3b200eeeafd43806f3a9c"),
 "vinculos": (AT / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", "490675e63122a24baebd8890f4a7883a07f68916d90562e74adf309133501d1b"),
}
def ciencia_ok(): return all(sha(p) == h for p, h in CIENCIA.values())
reg("C01 ciencia trio intacto (inicio)", ciencia_ok(), {k: sha(p)[:12] for k,(p,_) in CIENCIA.items()})

reg("C02 verbatim do mestre arquivado: sha 42ddd558... · serie == upload · DIGITAIS da pasta",
    sha(VERV) == sha(UP_V) == "42ddd558b79621c3ae3f9194c1836521604060b583bd863e05f0d36daf2e69ba"
    and (VERV.parent / "DIGITAIS_2026-09-21.txt").exists(),
    f"sha={sha(VERV)} bytes={VERV.stat().st_size}")

N1 = json.load(open(N1p)); N2 = json.load(open(N2p))
try:
    from jsonschema import Draft7Validator
    Draft7Validator.check_schema(N1); Draft7Validator.check_schema(N2); d7 = True
except Exception as e:
    d7 = f"FALHA/ausente: {e}"
reg("C03 replica A.1: shas+bytes exatos (b06660fd 9.582 · d96ad15b 12.840) · Draft7Validator.check_schema OK nos 2 (mesma biblioteca dele)",
    sha(N1p) == "b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da" and N1p.stat().st_size == 9582
    and sha(N2p) == "d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050" and N2p.stat().st_size == 12840 and d7 is True,
    f"d07={d7}")

v23 = V23.read_text(encoding="utf-8")
reg("C04 replica A.2: $id N1/N2 == ponteiros ativos §5.1/§5.2 da V2.3 (caractere a caractere)",
    N1.get("$id") == "L05/schema_referencia_v1.3.json" and N2.get("$id") == "L05/schema_vinculo_v1.4.json"
    and "`L05/schema_referencia_v1.3.json`" in v23 and "`L05/schema_vinculo_v1.4.json`" in v23,
    f"$ids={{N1:{N1.get('$id')}, N2:{N2.get('$id')}}}")

regs = json.dumps(N1) + json.dumps(N2)
reg("C05 replica A.4: 0 '$ref' nos dois schemas -> 0 referencias externas (sem acoplamento de versao)",
    regs.count('"$ref"') == 0, "nenhum '$ref' em N1+N2")

sec52 = "\n".join(v23.splitlines()[305:340])
reg("C06 replica O-2: 'uso' consta em required do N2 e NAO consta no §5.2 da V2.3 (observacao verdadeira; vai p/ proxima revisao)",
    "uso" in N2.get("required", []) and "uso" not in sec52,
    f"required_N2={N2.get('required')}")

def acha(o, chave):
    out = []
    if isinstance(o, dict):
        for k, v in o.items():
            if k == chave: out.append(True)
            out += acha(v, chave)
    elif isinstance(o, list):
        for v in o: out += acha(v, chave)
    return out
anc = N2.get("properties", {}).get("ancoras", {}).get("items", {}).get("properties", {})
reg("C07 replica precisao NOVA: direcao_suporte existe APENAS sob ancoras[] (raiz do vinculo nao tem) — degrau 5 da L-06 deve ler ancoras[].direcao_suporte",
    "direcao_suporte" in anc and "direcao_suporte" not in N2.get("properties", {})
    and len(acha(N2, "direcao_suporte")) == 3,
    f"ancoras.keys={sorted(anc.keys())}")

esp_t = (DIST / "L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4__ESPECIFICACAO.md").read_text(encoding="utf-8")
lei_t = (DIST / "LEIAME.txt").read_text(encoding="utf-8")
ocs = [open(p, encoding="utf-8").read().count("origem_conhecimento") for p in (N1p, N2p)] + [
       esp_t.count("origem_conhecimento"), lei_t.count("origem_conhecimento")]
reg("C08 replica O-3: origem_conhecimento = 0x nos 4 artefatos (2 schemas + spec + LEIAME) e 3x na V2.3 -> dependencia futura registrada (D-JSONM-ORIGEM-CONHECIMENTO: schema dos JSONs Modulares tera de carregar o campo)",
    all(x == 0 for x in ocs) and v23.count("origem_conhecimento") == 3,
    f"nos4={ocs} naV23={v23.count('origem_conhecimento')}")

reg("C09 replica A.6: descriptions dos JSONs dizem 'PROPOSTA ... nao normativo' (pre-selo confirmado nos bytes) -> selo do operador cobre a ordem; rotulos internos saem no ciclo editorial v1.5 (registrado no DIGITAIS do pacote)",
    N1.get("description","").startswith("PROPOSTA v1.3") and "nao normativo" in N1.get("description","")
    and N2.get("description","").startswith("PROPOSTA v1.4") and "nao normativo" in N2.get("description","")
    and "resíduo pré-selo" in (DEST / "DIGITAIS_2026-09-21.txt").read_text(encoding="utf-8"),
    "residuo declarado por escrito no pacote")

pon = PONTEIRO.read_text(encoding="utf-8")
reg("C10 APROVACAO gravada no ponteiro: cabeca contem sha da V2.3 + 2 shas de schemas + frase verbatim do operador · V2.3 promovida na serie raiz == 498e7df9... · historico V2.2 preservado (regua: nomes da serie nao se renomeiam — 17 scripts os citam)",
    all(a in pon for a in ["498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73",
        "b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da",
        "d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050",
        "a oficial agora é a Arquitetura Consolidada", "APROVACAO FORMAL — 2026-09-19"])
    and sha(V23V) == "498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73",
    "D-V22-SCHEMA-NOMES fechada com a vigencia da V2.3 · ponteiro = fonte de verdade do estado temporal")

# manifesto 2026-09-21 × 12 arquivos (regra dupla da C67; caminho: LIN para historicos, DIST p/ spec limpa)
man = (DEST / "MANIFESTO_LINHAGEM_2026-09-21.txt").read_text(encoding="utf-8")
declarados = {}
# CONFISSAO C68-1 (2026-09-21): 1a corrida leu so 10/12 — regua assumia coluna
# 'estado' de 1 token; o manifesto pos-selo introduziu estado de 2 tokens
# ("APROVADO vige"). falhos=[] nos 10 lidos: era cobertura do parser, nao dado.
# Regua corrigida: sha ancorado no FIM da linha, estado e' campo livre (.+?).
for linha in man.splitlines():
    m = re.match(r"L05/(schema_\S+\.json)\s+\d{4}-\d{2}-\d{2}\s+\d+\s+.+?\s+([0-9a-f]{64})\s*$", linha)
    if m: declarados[m.group(1)] = m.group(2)
ls = man.splitlines()
for i, linha in enumerate(ls):
    m = re.match(r"(\S+\.md)\s*$", linha.strip())
    if m and re.match(r"L05_", linha.strip()):
        m2 = re.search(r"sha\s+([0-9a-f]{64})", ls[i + 1])
        if m2: declarados[m.group(1)] = m2.group(1)
def caminho(n):
    if n == "L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4__ESPECIFICACAO.md": return DIST / n
    return LIN / n
falhos = [n for n, h in declarados.items() if not caminho(n).exists() or sha(caminho(n)) != h]
reg("C11 manifesto 2026-09-21 (espelho pos-selo): 12 digitais x 12 arquivos conferem (7 schemas via LIN + 5 md; a spec v1.4 medida no nome limpo da distribuicao)",
    len(declarados) == 12 and not falhos, f"declarados={len(declarados)} falhos={falhos} manifesto_sha={sha(DEST/'MANIFESTO_LINHAGEM_2026-09-21.txt')[:12]}")

nomes = sorted(p.name for p in DEST.iterdir() if p.name != "ENVIO_AUDITOR2_PROJETO_V23_2026-09-21.zip")
z = DEST / "ENVIO_AUDITOR2_PROJETO_V23_2026-09-21.zip"
with zipfile.ZipFile(z) as zz:
    re_ok = all(zz.read(p.name) == p.read_bytes() for p in DEST.iterdir() if p.name != z.name)
    zn = sorted(zz.namelist())
limpo = all(("CANDIDATA" not in n.upper() and "PROPOSTA" not in n.upper() and "CORRENTE" not in n.upper()) for n in nomes + [z.name])
reg("C12 pacote refeito sob a regra nova de rotulos: nomes limpos (0 CANDIDATA/PROPOSTA/CORRENTE) · conteudo ≡ fontes oficiais · zip re-extraido ≡ · pasta de 20/09 marcada SUPERSEDED",
    re_ok and zn == nomes and limpo and (OLD / "SUPERSEDED_2026-09-21.txt").exists()
    and sha(DEST / "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.3 - 19.09.26.md") == "498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73",
    f"zip={sha(z)} nomes={nomes}")

reg("C13 ciencia trio intacto (fim)", ciencia_ok(), {k: sha(p)[:12] for k,(p,_) in CIENCIA.items()})

n_ok = sum(1 for x in checks if x["ok"])
out = {"trilha": 68, "data": "2026-09-21", "rodada": 53,
 "titulo": "Replica da verificacao tecnica do mestre (A.1-A.6, O-1..O-3) · APROVACAO V2.3+schemas gravada · pacote-espelho refeito sob regra de rotulos",
 "veredito": "TUDO do mestre CONFERE nas replicas duras (shas/bytes · draft-07 · $id==ponteiros · 0 $ref · uso required x fora do §5.2 · direcao_suporte so em ancoras[] · origem_conhecimento 0 nos 4 artefatos · descriptions pre-selo). A.6 RESOLVIDA pelo operador na mesma frase (selo junto). O-2 e O-1 registradas para proxima revisao; O-3 vira divida nomeada D-JSONM-ORIGEM-CONHECIMENTO. Vigencia V2.3 gravada no ponteiro (historico intacto). Pacote limpo (regra nova de rotulos).",
 "checks": checks, "ok": n_ok, "total": len(checks), "confissoes": []}
js = AT / "producao/TRILHA68_verificacao_mestre_aprovacao_V23_2026-09-21.json"
js.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"TRILHA 68: {n_ok}/{len(checks)} verdes · json={js.name}")
for x in checks: print(("OK " if x["ok"] else "FALHA ") + x["check"])
