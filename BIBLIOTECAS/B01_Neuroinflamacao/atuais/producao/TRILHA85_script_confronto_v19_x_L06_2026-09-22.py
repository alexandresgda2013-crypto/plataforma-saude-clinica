#!/usr/bin/env python3
# TRILHA 85 — Confronto COMO EXECUTAR v1.9 x L-06 vigente (rodada 74, 2026-09-22)
# Régua: R-BUSCA-1 (corpus fechado com digitais + padrão exato + trinca + nível declarado)
# Níveis: L1 forma exata (casefold) · L2 prosa (substring casefold) · +declarado
import unicodedata, hashlib, json, re

HOME = "/home/user"
V19  = HOME + "/uploads/4º_COMO_EXECUTAR___v1_9.md"
V19S = HOME + "/BIBLIOTECAS/_documentos_serie/COMO_EXECUTAR_v1.9_recebido_2026-09-20/4º_COMO_EXECUTAR___v1_9.md"
L06  = HOME + "/BIBLIOTECAS/_documentos_serie/MESTRE_L06_minuta3_consolidada_rev6_recebida_2026-09-22/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev6_2026-09-22.md"
LISTA= HOME + "/BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/5º LISTA CANÔNICA — B1  SM-02 V1.3.md"
BLOCO= HOME + "/BIBLIOTECAS/_documentos_serie/KIT_CLINICA_recebido_2026-09-15/6º BLOCO DE ESTADO  v1.6.md"
CONS = HOME + "/BIBLIOTECAS/_documentos_serie/CONSOLIDADO_fluxo_B_recebido_2026-09-18/CONSOLIDADO_RESPOSTA_FLUXO_B_2026-09-18.md"

def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
def txt(p): return unicodedata.normalize("NFC", open(p, encoding="utf-8").read())

def busca(texto, padrao, corpus_nome):
    """L1/L2: substring casefold, com trinca de cada ocorrência."""
    cf, pat = texto.casefold(), padrao.casefold()
    hits, i = [], 0
    while True:
        j = cf.find(pat, i)
        if j < 0: break
        ln = texto[:j].count("\n") + 1
        trecho = texto[max(0,j-70):j+len(padrao)+70].replace("\n", " ")
        hits.append({"linha": ln, "trinca": "...%s..." % trecho})
        i = j + 1
    return {"corpus": corpus_nome, "padrao": padrao, "n": len(hits), "hits": hits[:6]}

R = {"rodada": 74, "data": "2026-09-22", "itens": []}
digitais = {k: sha(v) for k, v in [("v19",V19),("v19_serie",V19S),("L06",L06),("lista",LISTA),("bloco",BLOCO),("consolidado",CONS)]}
R["corpus_digitais"] = digitais
R["itens"].append({"item": 1, "teste": "identidade v1.9 upload ≡ série",
    "ok": digitais["v19"] == digitais["v19_serie"] == "1cd90b407facee81692d668919829c9d6d5a149b1309424c6f012e26cd81f586",
    "nivel": "L1-preciso (sha256)"})
R["itens"].append({"item": 2, "teste": "identidade L-06 artefato vigente",
    "ok": digitais["L06"] == "98e90bdc755162b28fd16817d65692cebe81f939c466ef1d29c7a0a1124f2b41",
    "nivel": "L1-preciso (sha256)"})

v19, l06, cons = txt(V19), txt(L06), txt(CONS)

# 3. A correção do consolidado B chegou ao v1.9? ("G3 é parecer... retorno... confirmação conjunta")
alvos_consolidado = [
    ("retorn", "v1.9"), ("confirmação conjunta", "v1.9"), ("G3 é parecer", "v1.9"),
    ("não fechamento", "v1.9"), ("fechamento", "v1.9"), ("confirmad", "v1.9"),
    ("retorn", "consolidado"), ("confirmação conjunta", "consolidado"),
]
res3 = {}
for pat, corpus in alvos_consolidado:
    res3[f"{corpus}::{pat}"] = busca(v19 if corpus=="v1.9" else cons, pat, corpus)
R["itens"].append({"item": 3, "teste": "correção 'G3 é parecer, não fechamento' presente no v1.9?",
    "medicoes": {k: {"n": v["n"], "hits": v["hits"][:3]} for k, v in res3.items()},
    "ok": res3["v1.9::retorn"]["n"] == 0 and res3["v1.9::confirmação conjunta"]["n"] == 0 and res3["v1.9::G3 é parecer"]["n"] == 0,
    "ok_significado": "AUSENTE no v1.9 (0× nos 3 padrões exatos) = correção NÃO incorporada",
    "nivel": "L1 (0× de forma exata) — 'ausente' apenas nestes 3 padrões"})

# 4. Convergências verbatim de filosofia v1.9 x L-06
conv = [
    ("não fabrica precedência", "L06"), ("fonte primária", "v1.9"), ("consenso", "v1.9"),
    ("preservar as duas", "L06"), ("registrar a lacuna", "L06"), ("não se força consenso", "v1.9"),
    ("preenchimento implícito", "L06"), ("nunca se estima", "v1.9"),
    ("conhecimento nasce em G3", "v1.9"), ("heterogeneidade", "v1.9"),
    ("aprovado_com_ressalva", "v1.9"), ("aprovado_com_ressalva", "L06"),
    ("nota_ressalva", "v1.9"), ("nota_ressalva", "L06"),
    ("divergência", "v1.9"), ("concordância entre IAs não é evidência", "v1.9"),
]
res4 = {}
for pat, corpus in conv:
    res4[f"{corpus}::{pat}"] = busca(l06 if corpus=="L06" else v19, pat, corpus)
R["itens"].append({"item": 4, "teste": "mapa de convergência verbatim v1.9 x L-06",
    "medicoes": {k: {"n": v["n"], "hits": v["hits"][:2]} for k, v in res4.items()},
    "ok": True, "nivel": "L1/L2 conforme padrão; trincas gravadas"})

# 5. Acoplamento de camadas: o v1.9 cita L-05/L-06/L-NT/Motor? A L-06 cita o v1.9?
acop = [("L-05","v1.9"),("L-06","v1.9"),("L-NT","v1.9"),("Motor","v1.9"),("N1","v1.9"),("N2","v1.9"),
        ("Como Executar","L06"),("claim clínico","L06"),("G3","L06")]
res5 = {}
for pat, corpus in acop:
    res5[f"{corpus}::{pat}"] = busca(l06 if corpus=="L06" else v19, pat, corpus)
R["itens"].append({"item": 5, "teste": "acoplamento nominal entre os documentos",
    "medicoes": {k: {"n": v["n"], "hits": v["hits"][:2]} for k, v in res5.items()},
    "ok": True, "nivel": "L1 (forma exata casefold)"})

# 6. Réplica das contagens do kit (mestre: 41 alvos / 22 com entrada / 8+14)
lista, bloco = txt(LISTA), txt(BLOCO)
alvos = re.findall(r"B1\.SM02\.\d{3}[a-z]?", lista)
bloco_ids = set(re.findall(r"B1\.SM02\.\d{3}[a-z]?", bloco))
n_aprov      = len(re.findall(r"status:\s*aprovado(?!_com)", bloco, re.I))
n_ressalva   = len(re.findall(r"status:\s*aprovado_com_ressalva", bloco, re.I))
R["itens"].append({"item": 6, "teste": "réplica contagens do kit (mestre: 41/22/21/8/14)",
    "medicao": {"alvos_lista": len(alvos), "alvos_distintos": len(set(alvos)),
                "ids_no_bloco": len(bloco_ids),
                "status_aprovado_no_bloco": n_aprov, "status_aprovado_com_ressalva_no_bloco": n_ressalva,
                "padrao": "regex B1\\.SM02\\.\\d{3}[a-z]?; status:\\s*aprovado(_com_ressalva)? (casefold, neg lookahead no 1º)"},
    "ok": len(alvos) == 41 and len(bloco_ids) == 22 and n_aprov == 8 and n_ressalva == 14,
    "nivel": "L1-exato sobre corpus declarado (Lista 3252a920-era / Bloco 0a630dba-era — digitais medidas agora acima)"})

# 7. Piloto do Protocolo de três IAs: B1.SM02.014 tem resolução registrada na base?
import subprocess
g = subprocess.run(["grep","-rl","SM02.014", HOME+"/BIBLIOTECAS/B01_Neuroinflamacao"], capture_output=True, text=True)
arqs = [a for a in g.stdout.strip().split("\n") if a and "TRILHA85" not in a]
R["itens"].append({"item": 7, "teste": "rastro do piloto B1.SM02.014 na base",
    "arquivos_com_mencao": arqs[:20], "n_arquivos": len(arqs),
    "ok": True, "nivel": "busca global por nome; leitura de conteúdo fica para o documento",
    "comando": "grep -rl 'SM02.014' BIBLIOTECAS/B01_Neuroinflamacao"})

out = HOME + "/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA85_confronto_v19_x_L06_2026-09-22.json"
json.dump(R, open(out,"w"), ensure_ascii=False, indent=2)
verdes = sum(1 for x in R["itens"] if x["ok"])
print(f"TRILHA 85 gravada: {out}")
print(f"verdes {verdes}/{len(R['itens'])}")
for x in R["itens"]:
    print(f"  item {x['item']}: {'VERDE' if x['ok'] else 'VERMELHO'} — {x['teste']}")
print("item3 n(retorn/conf conj/G3 é parecer no v1.9):",
      res3["v1.9::retorn"]["n"], res3["v1.9::confirmação conjunta"]["n"], res3["v1.9::G3 é parecer"]["n"])
print("item6:", R["itens"][5]["medicao"])
print("item7:", R["itens"][6]["n_arquivos"], "arquivos")
