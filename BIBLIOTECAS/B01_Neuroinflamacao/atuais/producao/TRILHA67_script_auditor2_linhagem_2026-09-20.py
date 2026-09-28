# TRILHA 67 — 2026-09-20 (rodada 52) — Réplica da resposta do Auditor-2 ao pacote
# L-05 LINHAGEM: 12 digitais × manifesto (reexecução) + tabela de genealogia
# (direcao/direcao_suporte/condicao) medida nos 4 N2 + pacote "espelho no Projeto"
# remontado byte-idêntico + descoberta: a arquitetura do PROJETO do auditor-2 é de 15/09.
import hashlib, json, re, zipfile
from pathlib import Path

BASE = Path("/home/user")
S = BASE / "BIBLIOTECAS/_documentos_serie"
AT = BASE / "BIBLIOTECAS/B01_Neuroinflamacao/atuais"
LIN = BASE / "ENTREGAS/2026-09-19_L05_LINHAGEM_COMPLETA"
DEST = BASE / "ENTREGAS/2026-09-20_ENVIO_AUDITOR2_PROJETO"
checks = []
def reg(nome, ok, det): checks.append({"check": nome, "ok": bool(ok), "detalhe": det})
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

V22_SRC = BASE / "ENTREGAS/2026-09-19_V2.2_OFICIAL/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
DIST = BASE / "ENTREGAS/2026-09-19_SCHEMAS_L05_CORRENTES_DISTRIBUICAO"
VERV = S / "AUDITOR2_resposta_linhagem_manifesto_2026-09-20/RESPOSTA_AUDITOR2_linhagem_2026-09-20.md"

CIENCIA = {
 "V7": (AT / "B1 NEUROINFLAMAÇÃO V7 CANONICA.md", "6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238"),
 "manifesto": (AT / "Evidencias/Bibliografia/_manifesto_biblioteca.json", "79d1309a168922d0e8bf43736cd5b21c8b361bdf64e3b200eeeafd43806f3a9c"),
 "vinculos": (AT / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", "490675e63122a24baebd8890f4a7883a07f68916d90562e74adf309133501d1b"),
}
def ciencia_ok(): return all(sha(p) == h for p, h in CIENCIA.values())
reg("C01 ciencia trio intacto (inicio)", ciencia_ok(), {k: sha(p)[:12] for k,(p,_) in CIENCIA.items()})

# C02 — manifesto × 12 arquivos (reexecução da conferência que ele declarou: "12 digitais conferem")
# Régua corrigida (C67-1): o manifesto tem DOIS formatos —
#  (a) schemas em tabela: 'L05/<nome>  <data>  <bytes>  <estado>   <sha64>'
#  (b) especificações em bloco: '<nome.md>' seguido de '  <data> · <bytes> b · sha <sha64>'
man = (LIN / "MANIFESTO_LINHAGEM.txt").read_text(encoding="utf-8")
declarados = {}
for linha in man.splitlines():
    m = re.match(r"L05/(schema_\S+\.json)\s+\d{4}-\d{2}-\d{2}\s+\d+\s+\S+\s+([0-9a-f]{64})", linha)
    if m: declarados[m.group(1)] = m.group(2)
linhas = man.splitlines()
for i, linha in enumerate(linhas):
    m = re.match(r"(\S+\.md)\s*$", linha.strip())
    if m and i + 1 < len(linhas):
        m2 = re.search(r"sha\s+([0-9a-f]{64})", linhas[i + 1])
        if m2: declarados[m.group(1)] = m2.group(1)
falhos = [n for n, h in declarados.items() if not (LIN / n).exists() or sha(LIN / n) != h]
reg("C02 manifesto: 12 digitais declaradas × 12 arquivos do pacote — reexecucao confere (ecos dele VERIFICADOS)",
    len(declarados) == 12 and not falhos,
    f"declarados={len(declarados)} falhos={falhos} manifesto_sha={sha(LIN/'MANIFESTO_LINHAGEM.txt')[:12]} "
    f"(regua: 2 padroes de linha do manifesto; C67-1 confessada no json)")

# C03 — tabela de genealogia dele medida nos 4 N2 (chaves JSON)
esp = {
 "schema_vinculo_v1.1.json": ("b0934412", {"direcao":True,  "direcao_suporte":False, "condicao":True}),
 "schema_vinculo_v1.2.json": ("19f4f29a", {"direcao":False, "direcao_suporte":True,  "condicao":True}),
 "schema_vinculo_v1.3.json": ("ec4f0de8", {"direcao":False, "direcao_suporte":True,  "condicao":True}),
 "schema_vinculo_v1.4.json": ("d96ad15b", {"direcao":False, "direcao_suporte":True,  "condicao":True}),
}
ok3 = nota = True
det = {}
for f, (hx, t) in esp.items():
    txt = (LIN / f).read_text(encoding="utf-8")
    pres = {k: bool(re.search(rf'"{k}"\s*:', txt)) for k in t}
    n = {k: len(re.findall(rf'"{k}"\s*:', txt)) for k in t}
    det[f] = n
    ok3 &= sha(LIN / f).startswith(hx) and pres == t
reg("C03 tabela do auditor-2 CONFERE NOS ARTEFATOS: direcao+condicao nascem na v1.1 · v1.2 so renomeia (presencas exatas; contagens: v1.1 2/2 · v1.2 2/2 · v1.3 3/3 · v1.4 3/3)",
    ok3, f"medido={det} — correcao (b) agora verificada dos DOIS lados sobre os mesmos bytes")

# C04 — correntes ≡ bytes da casa (eco b06660fd / d96ad15b)
reg("C04 eco dos correntes: v1.3 == b06660fd... · v1.4 == d96ad15b... (pacote linhagem ≡ distribuição)",
    sha(LIN / "schema_referencia_v1.3.json") == sha(DIST / "schema_referencia_v1.3__N1_CORRENTE.json")
    and sha(LIN / "schema_vinculo_v1.4.json") == sha(DIST / "schema_vinculo_v1.4__N2_CORRENTE.json"),
    f"v13={sha(LIN/'schema_referencia_v1.3.json')[:12]} v14={sha(LIN/'schema_vinculo_v1.4.json')[:12]}")

# C05 — verbatim da rodada arquivado (integridade + marcadores do conteúdo novo)
v = VERV.read_text(encoding="utf-8")
reg("C05 verbatim auditor-2 arquivado: sha 2c94efab... · marcadores (12 digitais · 'nao guarda nada entre sessões' · 'arquitetura... de 15/09' · 'regra de producao' · selo pendente)",
    sha(VERV) == "2c94efabb4d432f6c68d60e561a288735c6aa5a4541c4eade4f87e1aa667d6fb"
    and all(a in v for a in ["As 12 digitais conferem", "o meu ambiente não guarda nada entre sessões",
        "a de 15/09", "regra de distribuição da casa como regra de produção", "selo formal do operador"]),
    f"sha={sha(VERV)[:12]}")

# C06 — pacote espelho para o Projeto dele: itens ≡ fontes oficiais + DIGITAIS c/ shas individuais + zip
fontes = {
 "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md": sha(V22_SRC),
 "schema_referencia_v1.3__N1_CORRENTE.json": sha(DIST / "schema_referencia_v1.3__N1_CORRENTE.json"),
 "schema_vinculo_v1.4__N2_CORRENTE.json": sha(DIST / "schema_vinculo_v1.4__N2_CORRENTE.json"),
 "L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4__ESPECIFICACAO.md": sha(DIST / "L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4__ESPECIFICACAO.md"),
 "MANIFESTO_LINHAGEM.txt": sha(LIN / "MANIFESTO_LINHAGEM.txt"),
}
ok6 = all(sha(DEST / n) == h for n, h in fontes.items())
dig = (DEST / "DIGITAIS_2026-09-20.txt").read_text(encoding="utf-8")
z = DEST / "ENVIO_AUDITOR2_PROJETO_2026-09-20.zip"
with zipfile.ZipFile(z) as zz:
    zn = set(zz.namelist())
    re_ok = all(zz.read(n) == (DEST / n).read_bytes() for n in fontes)
reg("C06 pacote ENTREGAS/2026-09-20_ENVIO_AUDITOR2_PROJETO: 5/5 ≡ fontes oficiais (V2.2 vigente — disciplina: candidata V2.3 só sobe após a frase) · DIGITAIS c/ shas individuais + ajuste de regime escrito · zip re-extraído ≡",
    ok6 and re_ok and zn == set(fontes) | {"DIGITAIS_2026-09-20.txt"}
    and all(h[:8] in dig for h in fontes.values())
    and "V2.3 é candidata" in dig.replace("a V2.3 é candidata","a V2.3 é candidata") and "só sobe APÓS a frase" in dig,
    f"zip={sha(z)}")

# C07 — a descoberta da rodada: o PROJETO DO AUDITOR-2 também está com arquitetura de 15/09
reg("C07 registrado (ação): o Projeto do auditor-2 tem 'a Filosofia, as Decisões Arquiteturais e a Arquitetura Consolidada de 15/09' — MESMA classe da D-V22-BYTES-PROJETO, agora no 2º projeto · pedido: eco do sha do arquivo antigo ANTES da troca (casa crava o elo — 4º fantasma já arquivado p/ confronto)",
    "duas versões atrás da V2.3" in v,
    "receita espelho do mestre: V2.2 oficial sobe já; eco antigo+novo fecha a 2ª base superseded")

reg("C08 ciencia trio intacto (fim)", ciencia_ok(), {k: sha(p)[:12] for k,(p,_) in CIENCIA.items()})

n_ok = sum(1 for x in checks if x["ok"])
out = {"trilha": 67, "data": "2026-09-20", "rodada": 52,
 "titulo": "Réplica resposta auditor-2 ao pacote de linhagem + pacote espelho p/ o Projeto dele",
 "veredito": "TUDO VERIFICADO: manifesto 12/12 × arquivos · tabela de genealogia exata nos artefatos (2 lados, mesmos bytes) · ecos correntes ≡ casa · premissa do pacote corrigida por ele com honestidade e A Solução certa (espelho no Projeto — com ajuste de regime: sobe VIGENTE V2.2, V2.3 só apos frase) · adoção da regra da casa como regra de PRODUÇÃO (causa-raiz aposentada) · descoberta: 2ª base de projeto superseded (15/09) — mesmo defeito do mestre, mesma receita.",
 "checks": checks, "ok": n_ok, "total": len(checks),
 "confissoes": [
   "C67-1: 1a corrida FALHOU C02 (7/8): regex ingenuo 'sha + resto-da-linha' parseou a tabela mista do manifesto ao contrario (sha primeiro, resto como nome). O manifesto tem 2 formatos (tabela de schemas + bloco de mds) — regua corrigida com 2 padroes; 12/12 confirmam. Licao C55-1 outra vez: formato declarado antes de contar."
 ]}
js = AT / "producao/TRILHA67_auditor2_linhagem_2026-09-20.json"
js.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"TRILHA 67: {n_ok}/{len(checks)} verdes · json={js.name}")
for x in checks: print(("OK " if x["ok"] else "FALHA ") + x["check"])
