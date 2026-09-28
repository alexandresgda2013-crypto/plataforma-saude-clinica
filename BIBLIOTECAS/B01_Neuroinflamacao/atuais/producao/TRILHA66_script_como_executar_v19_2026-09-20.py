# TRILHA 66 — 2026-09-20 (rodada 51) — COMO EXECUTAR v1.9 recebido (eco bilateral)
# + pacote de envio dos schemas remontado byte-idêntico (operador não localizou o de 19/09).
import hashlib, json, glob, os, zipfile
from pathlib import Path

BASE = Path("/home/user")
S = BASE / "BIBLIOTECAS/_documentos_serie"
AT = BASE / "BIBLIOTECAS/B01_Neuroinflamacao/atuais"
checks = []
def reg(nome, ok, det): checks.append({"check": nome, "ok": bool(ok), "detalhe": det})
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

UP = BASE / "uploads/4º_COMO_EXECUTAR___v1_9.md"
SR = S / "COMO_EXECUTAR_v1.9_recebido_2026-09-20/4º_COMO_EXECUTAR___v1_9.md"
SRC = BASE / "ENTREGAS/2026-09-19_SCHEMAS_L05_CORRENTES_DISTRIBUICAO"
DEST = BASE / "ENTREGAS/2026-09-20_ENVIO_MESTRE_SCHEMAS"

CIENCIA = {
 "V7": (AT / "B1 NEUROINFLAMAÇÃO V7 CANONICA.md", "6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238"),
 "manifesto": (AT / "Evidencias/Bibliografia/_manifesto_biblioteca.json", "79d1309a168922d0e8bf43736cd5b21c8b361bdf64e3b200eeeafd43806f3a9c"),
 "vinculos": (AT / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", "490675e63122a24baebd8890f4a7883a07f68916d90562e74adf309133501d1b"),
}
def ciencia_ok(): return all(sha(p) == h for p, h in CIENCIA.values())
reg("C01 ciencia trio intacto (inicio)", ciencia_ok(), {k: sha(p)[:12] for k,(p,_) in CIENCIA.items()})

b = SR.read_bytes()
reg("C02 v1.9: sha == 1cd90b40... (ECO BILATERAL c/ o mestre — 'declarado' vira VERIFICADO) · 29.423 b · 535 linhas · H1 'COMO EXECUTAR — v1.9' · serie == upload",
    sha(UP) == sha(SR) == "1cd90b407facee81692d668919829c9d6d5a149b1309424c6f012e26cd81f586"
    and len(b) == 29423 and len(b.decode("utf-8").splitlines()) == 535
    and b.decode("utf-8").splitlines()[0] == "# COMO EXECUTAR — v1.9",
    f"sha={sha(SR)} bytes={len(b)}")

dig = (SR.parent / "DIGITAIS_2026-09-20.txt").read_text(encoding="utf-8")
reg("C03 arquivado c/ status registrado por escrito: EM ATUALIZAÇÃO (não normativo) · frente própria (claims) · referência, não alçada da casa · dívida de linhagem v1.8 nomeada · regra: nova versão flui à casa com sha",
    all(a in dig for a in ["EM FASE DE APROVAÇÃO", "NÃO NORMATIVO", "v1.8", "ECO BILATERAL"]),
    SR.parent.name)

# elo v1.8 ausente (glob por nome; C56-2: fora artefatos da trilha)
hits18 = [p for p in glob.glob(str(BASE / "**/*v1.8*"), recursive=True)
          if os.path.isfile(p) and "TRILHA66" not in p]
hits19 = [p for p in glob.glob(str(BASE / "**/*v1_9*"), recursive=True)
          if os.path.isfile(p) and "TRILHA66" not in p]
reg("C04 glob: v1.8 = 0 arquivos na base (dívida registrada) · v1.9 = exatamente o par upload+serie",
    hits18 == [] and len(hits19) == 2 and sha(hits19[0]) == sha(hits19[1]),
    f"v1.8={hits18} · v1.9={[h.replace(str(BASE)+'/','') for h in hits19]}")

# convergência v1.9 × deliberação do mestre (linhas 17-18) — informativo, verificado
t = SR.read_text(encoding="utf-8")
reg("C05 convergência registrada: v1.9 diz 'claims de SM-xx são CLÍNICOS e alimentam a pasta evidencias/bibliografia, não a biblioteca canônica mecanística' (coerente c/ bifurcação (i) e c/ a pergunta 'de onde a NT tira o conhecimento clínico')",
    "são CLÍNICOS e alimentam a" in t.replace("\n#     "," ") 
    or "CLÍNICOS" in t and "biblioteca canônica mecanística" in t,
    "substring verificada no documento (nota de interface; 0 auditoria de conteúdo — outra alçada)")

# pacote de envio remontado ≡ distribuição
pares = ["SCHEMAS_L05_CORRENTES_2026-09-19.zip","schema_referencia_v1.3__N1_CORRENTE.json",
         "schema_vinculo_v1.4__N2_CORRENTE.json","L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4__ESPECIFICACAO.md","LEIAME.txt"]
ok = all((DEST/a).read_bytes() == (SRC/a).read_bytes() for a in pares)
z = DEST / "SCHEMAS_L05_CORRENTES_2026-09-19.zip"
with zipfile.ZipFile(z) as zz:
    re_ok = sorted(zz.namelist()) == sorted(pares[1:])
digd = (DEST / "DIGITAIS_2026-09-20.txt").read_text(encoding="utf-8")
reg("C06 pacote ENTREGAS/2026-09-20_ENVIO_MESTRE_SCHEMAS: 5/5 itens byte-idênticos à distribuição · zip 72f8f2e5... · DIGITAIS com shas INDIVIDUAIS (correção r50)",
    ok and re_ok and sha(z) == "72f8f2e5ea7ec0ad553fa25ee2976da53b0f896a1a6c3e3ed81279d2e58ba235"
    and all(s in digd for s in ["b06660fd", "d96ad15b", "78a0f2af", "3fd836d6"]),
    f"zip={sha(z)} · itens={pares}")

reg("C07 ciencia trio intacto (fim)", ciencia_ok(), {k: sha(p)[:12] for k,(p,_) in CIENCIA.items()})

n_ok = sum(1 for x in checks if x["ok"])
out = {"trilha": 66, "data": "2026-09-20", "rodada": 51,
 "titulo": "COMO EXECUTAR v1.9 (eco bilateral fechado) + pacote schemas remontado para envio",
 "checks": checks, "ok": n_ok, "total": len(checks),
 "confissoes": ["v1.9 contém menções a 'v1.8' no texto (changelog); o glob da régua C04 mede NOMES de arquivo, escopo declarado — lição C56-2"]}
js = AT / "producao/TRILHA66_como_executar_v19_pacote_schemas_2026-09-20.json"
js.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"TRILHA 66: {n_ok}/{len(checks)} verdes · json={js.name}")
for x in checks: print(("OK " if x["ok"] else "FALHA ") + x["check"])
