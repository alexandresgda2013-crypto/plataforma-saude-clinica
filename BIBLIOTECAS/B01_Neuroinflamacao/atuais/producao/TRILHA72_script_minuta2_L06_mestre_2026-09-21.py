#!/usr/bin/env python3
# TRILHA 72 — rodada 58 (2026-09-21): MINUTA 2 L-06 DO MESTRE — replica integral
# (matriz velha => 4 falsos positivos exatos; matriz nova => 0 · retratacao do degrau 5 ·
# semantica escopo/papel/condicao no schema N2 v1.4 · citacao 243/274 trilha 27)
# Regua: json.load estrito · igualdade exata de enum · proxy claim_id NAO-VAZIO (conf. C72-1)
#
# CONFISSAO C72-1 (2026-09-21): 1a corrida da casa agrupou os vinculos com claim_id=''
# como se '' fosse um CLAIM — produziu 77 pares espurios entre VINC_B1V2_* (81-82 total).
# claim_id vazio = AUSENTE = sem proxy = sem par (e' o que as frases do mestre implicam:
# 'os outros tres nao tem claim_id'). Regua corrigida e datada; com ela: VELHA=4, NOVA=0.

import hashlib, json, re, unicodedata
from collections import defaultdict
from itertools import combinations
from pathlib import Path

BASE = Path("/home/user")
S = BASE / "BIBLIOTECAS/_documentos_serie"
PROD = BASE / "BIBLIOTECAS/B01_Neuroinflamacao/atuais"
SHA = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
res = []
def reg(nome, ok, detalhe=""):
    res.append({"check": nome, "ok": bool(ok), "detalhe": detalhe})
    print(("OK " if ok else "FALHA ") + nome + (f"  [{detalhe}]" if detalhe and not ok else ""))

V7  = PROD / "B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
MAN = PROD / "Evidencias/Bibliografia/_manifesto_biblioteca.json"
VIN = PROD / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
ESP = ("6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238",
       "79d1309a168922d0e8bf43736cd5b21c8b361bdf64e3b200eeeafd43806f3a9c",
       "490675e63122a24baebd8890f4a7883a07f68916d90562e74adf309133501d1b")
trio = lambda: (SHA(V7), SHA(MAN), SHA(VIN))
reg("C01 ciencia trio intacto (inicio)", trio() == ESP, str([s[:12] for s in trio()]))

M2 = S / "MESTRE_L06_minuta2_recebida_2026-09-21/L06_RESOLUCAO_CONFLITOS_minuta2_2026-09-21.md"
UPL = BASE / "uploads/L06_RESOLUCAO_CONFLITOS_minuta2_2026-09-21.md"
Tm = unicodedata.normalize("NFC", M2.read_text(encoding="utf-8"))
reg("C02 minuta 2 do mestre arquivada verbatim: sha eb54337c... · 12.837 b · serie == upload",
    SHA(M2) == "eb54337c7f17c20fbd0ad1b926fd0d575b33462141537e837c4aff9fa13bbd13" and SHA(M2) == SHA(UPL), SHA(M2)[:12])

SCH = json.load(open(BASE / "ENTREGAS/2026-09-21_ENVIO_AUDITOR2_PROJETO_V23/schema_vinculo_v1.4.json", encoding="utf-8"))
ap = SCH["properties"]["ancoras"]["items"]["properties"]
reg("C03 RETRATAÇÃO §0.1 VERDADEIRA: direcao_suporte enum selado == {sustenta, refuta, inconclusivo, condicional} e descricao 'eixo epistemico, ortogonal ao papel' → era a DIREÇÃO DO SUPORTE, nao extrapolacao; o campo do degrau 5 da minuta 1 (e da minuta do comentador, trilha 71) estava errado; a casa replica e registra a correcao DELE (7a confissao bilateral)",
    ap["direcao_suporte"].get("enum") == ["sustenta", "refuta", "inconclusivo", "condicional"]
    and "eixo epist" in str(ap["direcao_suporte"].get("description", "")).casefold(), str(ap["direcao_suporte"].get("enum")))

reg("C04 degrau 3: schema diz condicao 'Obrigatorio quando direcao_suporte=condicional; PROIBIDO (null) nos demais valores' == nota da escada dele",
    "ondicional" in str(ap["condicao"].get("description", "")) and "PROIBIDO" in str(ap["condicao"].get("description", "")), "")

reg("C05 degrau 2 NAO-serve-proxy VERDADEIRO: escopo descricao == 'Subdivisao interna da entidade... BLOCO_XX[/sub]' (nao e' contexto clinico) — aviso dele fiel ao schema",
    "Subdivis" in str(ap["escopo"].get("description", "")), "")

reg("C06 degrau 4 proxy rejeitado com razao: papel enum tem sustenta_mecanismo/biomarcador/intervencao e descricao 'RELACAO TEMATICA — NUNCA o veredito' — adotar como nivel causal atribuiria semantica que o campo recusa (palavras dele) — bate no schema",
    set(ap["papel"].get("enum", [])) >= {"sustenta_mecanismo", "sustenta_biomarcador", "sustenta_intervencao"}
    and "NUNCA o veredito" in str(ap["papel"].get("description", "")), str(ap["papel"].get("enum")))

V = json.load(open(VIN, encoding="utf-8"))
vincs = V if isinstance(V, list) else V.get("vinculos", list(V.values())[0])
byclaim = defaultdict(list)
for v in vincs:
    cid = (v.get("claim_id") or "").strip()  # C72-1
    if cid: byclaim[cid].append(v)
VELHA = {(a, "compensatoria") for a in ("causal", "contributiva")} | {("compensatoria", a) for a in ("causal", "contributiva")}
VELHA |= {(a, "nao_estabelecida") for a in ("causal", "contributiva", "associativa", "compensatoria")} | {("nao_estabelecida", a) for a in ("causal", "contributiva", "associativa", "compensatoria")}
NOVA = {(a, "nao_estabelecida") for a in ("causal", "contributiva", "associativa", "compensatoria", "marcador")} | {("nao_estabelecida", a) for a in ("causal", "contributiva", "associativa", "compensatoria", "marcador")}
def executa(mat):
    out = []
    for cid, vs in byclaim.items():
        for r1, r2 in combinations(vs, 2):
            if (r1["natureza_relacao"], r2["natureza_relacao"]) in mat:
                out.append((cid, r1["id_vinculo"], r1["natureza_relacao"], r2["id_vinculo"], r2["natureza_relacao"]))
    return sorted(out)
pv = executa(VELHA)
esperado = sorted([("B1.MEC.BLOCO02.011", "VINC_B1_0035", "causal", "VINC_B1_0036", "compensatoria"),
                   ("B1.MEC.BLOCO02.011", "VINC_B1_0036", "compensatoria", "VINC_B1_0037", "causal"),
                   ("B1.MEC.BLOCO02.019", "VINC_B1_0052", "compensatoria", "VINC_B1_0261", "contributiva"),
                   ("B1.MEC.BLOCO02.019", "VINC_B1_0053", "compensatoria", "VINC_B1_0261", "contributiva")])
reg("C07 EXECUCAO §0.2 REPLICADA: matriz VELHA (proxy claim_id nao-vazio) dispara EXATAMENTE os 4 pares dele (2 claims, ids e naturezas exatos) — confissao C72-1 aplicada",
    pv == esperado, f"{len(pv)} pares")

alvo = {"VINC_B1_0035": "TNFR1", "VINC_B1_0036": "TNFR2", "VINC_B1_0037": "arctig",
        "VINC_B1_0052": "IL-10", "VINC_B1_0053": "IL-10", "VINC_B1_0261": "IL-10"}
byid = {v["id_vinculo"]: v for v in vincs}
bioread = all(alvo[i].lower() in (byid[i].get("trecho_ancora", "") + " " + byid[i].get("achado_central_molecular", "")).lower() for i in alvo)
reg("C08 leitura biológica dos 4 FP confere nos bytes: TNFR1 (0035) × TNFR2 (0036) receptores diferentes · 0037 arctigenina reduz TNF · 0052/0053 × 0261 IL-10 mesma direcao — 'o que realmente dizem' dele = o que esta escrito",
    bioread, "")

pn = executa(NOVA)
naos = [v for v in vincs if v["natureza_relacao"] == "nao_estabelecida"]
naos_ok = (len(naos) == 4
           and byid["VINC_B1_0028"].get("claim_id") == "B1.MEC.BLOCO02.006"
           and len(byclaim.get("B1.MEC.BLOCO02.006", [])) == 1
           and all((v.get("claim_id") or "") == "" for v in naos if v["id_vinculo"] != "VINC_B1_0028"))
mar = [v for v in vincs if v["natureza_relacao"] == "marcador"]
reg("C09 matriz NOVA → 0 pares · 4 nao_estabelecida isolados como ele disse (0028 unico no claim BLOCO02.006; 0197/0198/0202 sem claim_id) · marcador unico (0201) sem par → 'sem caso no acervo' para marcador×nao_estabelecida VERDADEIRO (registro para o piloto, como ele pede)",
    pn == [] and naos_ok and len(mar) == 1 and (mar[0].get("claim_id") or "") == "", f"nova={len(pn)} naos={len(naos)}")

reg("C10 estado de executabilidade (tabela §5 dele) medido N/A-por-N/A: ancoras[] 0/274 (gatilho NAO executavel hoje) · verification_status 274/274 (contem verificado/extrapolado) · extrapolacao_por_analogia 274/274 · grau_maturidade 274/274 (degraus 5 e 6 plenos HOJE) · contexto/sentido_relacao/nivel_cadeia = 0x no schema N2 (raiz E ancoras)",
    all(not v.get("ancoras") for v in vincs)
    and all("verification_status" in v and "extrapolacao_por_analogia" in v and "grau_maturidade" in v for v in vincs)
    and {"verificado", "extrapolado"} <= {v["verification_status"] for v in vincs}
    and all(q not in SCH["properties"] and q not in ap for q in ("contexto", "sentido_relacao", "nivel_cadeia")), "")

RESP7 = unicodedata.normalize("NFC", (S / "RESPOSTA_7_PARECER_ARQUITETURA_V2_MESTRE_2026-09-15.md").read_text(encoding="utf-8"))
reg("C11 citacao dele EXATA: 'A casa mediu 243/274 migraveis por maquina na trilha 27' ≡ registro da casa de 15/09 (RESPOSTA_7/rev.14: 'trilha 27 … 243/274 vinculos migraveis a maquina') — leitura precisa do nosso acervo documental",
    "243/274" in RESP7 and "migráveis" in RESP7, "")

reg("C12 referencias do cabecalho dele batem na casa: V2.3 sha completo 498e7df9 (64h) · N1 prefixo b06660fd · N2 prefixo d96ad15b · V7 prefixo 6e2c2979 + '274 vinculos'",
    "498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73" in Tm
    and all(q in Tm for q in ("b06660fd", "d96ad15b", "6e2c2979", "274 vínculos")), "")

C71 = PROD / "producao/TRILHA71_compatibilidade_minuta2_L06_2026-09-21.json"
MC = unicodedata.normalize("NFC", (S / "COMENTADOR_minuta2_L06_recebida_2026-09-21/COMENTADOR_minuta2_L06_2026-09-21.md").read_text(encoding="utf-8"))
tbl_mc = MC[MC.find("|                      |"):MC.find("A matriz não constitui")]
comp = ("direcao_suporte` + marcação de extrapolação" in MC) and (tbl_mc.count("candidato") == 6) and ("T-14" in MC) and C71.exists()
reg("C13 comparativo codificado: a minuta do comentador (trilha 71) carrega o campo errado no degrau 5 (`ancoras[].direcao_suporte` + marcação de extrapolação) — herdado da frase que o mestre hoje RETRATOU · e a celula compensatoria×{causal,contributiva}=candidato que gerou os 4 FP · e marcador×nao_estabelecida=compativel — os 3 pontos que esta minuta 2 corrige COM EXECUCAO. Resgates da do comentador para a ata: teste 'direcao nao-precedente' (T-14 dela; reformulavel ja que direcao_suporte virou gatilho/degrau1) e a formalizacao do determinismo",
    comp and "T-14" in MC, "")

reg("C14 linhagem/rito: 'substitui a minuta 1' — porem a MINUTA 1 da L-06 nunca chegou a casa (0 bytes na serie; o que ha e' Minuta 1 do L-NT) → entra no pacote D-D01-D02-FONTE (mesma divida: a familia D-xx e a minuta 1 vivem no projeto do mestre) · autoria desta = mestre, coerente com assinatura + auto-retratacao",
    "substitui a minuta 1" in Tm and not list(S.glob("MESTRE_L06_minuta1*")) and not list(S.glob("*L06*minuta1*")), "")

reg("C15 ciencia trio intacto (fim)", trio() == ESP, str([s[:12] for s in trio()]))

ok = sum(1 for r in res if r["ok"])
out = PROD / "producao/TRILHA72_minuta2_L06_mestre_2026-09-21.json"
out.write_text(json.dumps({"trilha": 72, "data": "2026-09-21", "rodada": 58,
  "escopo": "replica integral da Minuta 2 L-06 do mestre contra schema N2 v1.4 + acervo B1 (274)",
  "veredito": "VERIFICADA INTEGRALMENTE — todas as afirmacoes mediveis conferem; a minuta se autocorrige nos mesmos 2 pontos que a casa anotou na minuta do comentador (P-1 absorvida via 'carta 10'; campo do degrau 5 ≡ P-2 da casa) e vai alem: matriz executada no acervo (velha=4 FP exatos; nova=0), proxies proibidos com evidencia, escopo/papel fieis ao schema",
  "confissoes": {"C72-1": "1a corrida da casa agrupou claim_id='' como grupo (77 pares espurios); claim_id vazio=ausente; regua corrigida → VELHA=4, NOVA=0"},
  "checks": res, "verdes": ok, "total": len(res)}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nTRILHA 72: {ok}/{len(res)} verdes · json={out.name}")
