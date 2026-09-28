#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# aplicar_rodada5_consolidado.py — Agente gerador, 2026-09-11 (regra AT-10: script
# versionado do reparo; NÃO edita o vivo — opera na bancada; o vivo recebe cópia
# ao final com trilha própria).
# Consolida sobre o produto do pipeline do perito (5 passadas, já aplicadas):
#   (a) correção canônica: rótulo defasado "— IL-6 predictor, 2015)" →
#       "; Virtanen et al., 2015)" (fonte: 01_pmids REF_VIRTANEN_2015 = Virtanen M
#       et al., 2015, Psychol Med, PMID 25697833 — vínculo VINC_B1_0130);
#   (b) AT-13: 3 âncoras apontando para frase alheia → frase da própria citação,
#       extraída manualmente com verificação de unicidade (fatiador markdown-aware
#       manual, 3 casos — perito recusou por ferramenta, decisão de conteúdo aqui);
#   (c) VINC_B1_0130: re-ancora à frase corrigida (sem prefixo de cabeçalho);
#   (d) AT-02c: remoção do prefixo "### …(BLOCOxx.yyy)" das 29−2 âncoras literais
#       que carregam cabeçalho (guardas: continua literal, não perde prosa);
#   (e) marca reancorado_em em todo registro alterado neste ciclo AT-02/AT-13.
import json, re, hashlib
from pathlib import Path

BANCADA = Path("/home/user/BIBLIOTECAS/_documentos_serie/bancada_at02")
VINC = BANCADA / "canonico/evidencias_b1/vinculos_referencia_afirmacao.json"
CANON = BANCADA / "uploads/B1 NEUROINFLAMAÇÃO V4 CANONICA.md"
TAG = "2026-09-11 AT-02 (5ª rodada perícia externa)"
NOTA13 = ("2026-09-11 AT-13 (decisão de conteúdo do agente): âncora apontava para frase de "
          "OUTRA referência (diagnóstico do perito, at13_trocas_de_ancora.json). Recolocada na "
          "frase única e não-ambígua que contém a citação nominal da própria referência "
          "(regra da 5ª passada; extração manual markdown-aware). Valor anterior preservado em "
          "producao/05_reparo_AT02_AT13_2026-09-11.json.")
NOTA130 = ("2026-09-11 reparo conjugado: rótulo defasado '— IL-6 predictor, 2015' corrigido NA "
           "CANÔNICA para '; Virtanen et al., 2015' (fonte: 01_pmids REF_VIRTANEN_2015, PMID "
           "25697833) e âncora re-extraída da frase corrigida, sem prefixo de cabeçalho.")

corpo = CANON.read_text(encoding="utf-8")
vinc = json.loads(VINC.read_text(encoding="utf-8"))
por_id = {v["id_vinculo"]: v for v in vinc}
log = {"data": "2026-09-11", "etapas": {}}
erros = []

# ── (a) correção canônica Virtanen ──────────────────────────────────────────
h_antes = hashlib.sha256(corpo.encode()).hexdigest()
VELHO = " — IL-6 predictor, 2015)"
NOVO = "; Virtanen et al., 2015)"
assert corpo.count(VELHO) == 1, f"esperado 1 ocorrência, achei {corpo.count(VELHO)}"
corpo2 = corpo.replace(VELHO, NOVO)
h_depois = hashlib.sha256(corpo2.encode()).hexdigest()
log["etapas"]["a_canonica_virtanen"] = {
    "sha256_antes": h_antes, "sha256_depois": h_depois,
    "mudanca": f"{VELHO!r} → {NOVO!r}", "ocorrencias": 1,
    "justificativa": "rótulo de estudo (título abreviado) no lugar de citação nominal; "
                     "fonte: 01_pmids.json REF_VIRTANEN_2015"}
corpo = corpo2

# ── (b) AT-13 ×3 + (c) 0130 ─────────────────────────────────────────────────
FR_ZHANG = ("A comunicação micróglia–neurônio por ATP tem mecanismo direto ligado a depressão: "
            "a crença padrão era que ATP extracelular → P2X7 → montagem do NLRP3; um achado mais "
            "fino mostra que o ATP e o estresse aumentam **contatos retículo-mitocôndria (MAMs)** "
            "na micróglia, e essa plataforma media o comportamento tipo-depressivo "
            "(Zhang et al., 2024)[ML; camundongo] [PRÉ-CLÍNICO].")
i = corpo.find("Arora et al., 2019")
jan = corpo[i - 800:i + 700]
m = re.search(r"(S100B sérico:[\s\S]*?\(Gulen et al\., 2016\)\[EC; humano\] \[VERIFICADO\]\.)", jan)
FR_S100B = m.group(1).strip()
import sys as _sys
_sys.path.insert(0, "/home/user/BIBLIOTECAS/_documentos_serie/bancada_at02/scripts")
from contrato import norm
alvos13 = {"VINC_B1_0095": ("REF_ZHANG_2024", FR_ZHANG, "Zhang et al., 2024"),
           "VINC_B1_0121": ("REF_ARORA_2019", FR_S100B, "Arora et al., 2019"),
           "VINC_B1_0122": ("REF_GULEN_2016", FR_S100B, "Gulen et al., 2016")}
feitos13 = []
for vid, (ref, frase, cit) in alvos13.items():
    v = por_id[vid]
    assert v["id_referencia_interna"] == ref, (vid, v["id_referencia_interna"])
    ok = (corpo.count(frase) == 1 and re.search(r"[.!?\]]$", frase)
          and cit in frase and "###" not in frase)
    if not ok:
        erros.append((vid, "frase AT-13 falhou nas guardas")); continue
    ant = v["trecho_ancora"]
    v["trecho_ancora"] = frase
    v["nota_reparo"] = NOTA13
    v["reancorado_em"] = TAG + " · AT-13 (reancoragem por citação própria, manual)"
    feitos13.append({"id_vinculo": vid, "ref": ref, "antes": ant, "depois": frase})
log["etapas"]["b_at13"] = feitos13

# (c) VINC_B1_0130 — frase corrigida, sem cabeçalho
m130 = re.search(r"(Existe relação entre magnitude da ativação inflamatória[\s\S]*?"
                 r"Virtanen et al\., 2015\)\[EC; humano\] \[VERIFICADO\]\.)", corpo)
assert m130, "frase Virtanen corrigida não achada"
FR130 = m130.group(1)
v130 = por_id["VINC_B1_0130"]
ant130 = v130["trecho_ancora"]
assert corpo.count(FR130) == 1
v130["trecho_ancora"] = FR130
v130["nota_reparo"] = NOTA130
v130["reancorado_em"] = TAG + " · reancora pós-correção canônica (Virtanen)"
log["etapas"]["c_vinc0130"] = {"antes": ant130, "depois": FR130}

# ── (d) AT-02c: trim de prefixo "### …(BLOCO…)" em âncoras literais ─────────
RX_PREFIXO = re.compile(r"^#{1,6} .{0,120}?\(BLOCO[\d.,\s]+\)\s*-?\s*")
trims = []
for v in vinc:
    anc = v["trecho_ancora"]
    if "###" not in anc or v["id_vinculo"] in alvos13 or v["id_vinculo"] == "VINC_B1_0130":
        continue
    trim = RX_PREFIXO.sub("", anc).strip()
    # nota rev.2 2026-09-11: o domínio das âncoras é o da canônica NORMALIZADA
    # (norm(): "][", sem "**", aspas retas) — a rev.1 comparava com a canônica
    # crua e reprovava todos os trims por falso-negativo.
    if (trim and trim != anc and len(trim) >= 60 and trim in norm(corpo)
            and "###" not in trim and re.match(r"[A-ZÀ-Ü\"*\-•]", trim)):
        trims.append({"id_vinculo": v["id_vinculo"], "antes": anc[:120], "depois": trim[:120]})
        v["trecho_ancora"] = trim
        v["reancorado_em"] = TAG + " · AT-02c (prefixo de cabeçalho removido)"
    elif trim != anc:
        erros.append((v["id_vinculo"], "trim candidato reprovado nas guardas — mantido como está"))
log["etapas"]["d_at02c_trims"] = trims

# ── (e) marca reancorado_em nos registros alterados pelo pipeline (5 passadas)
VIVO = Path("/home/user/BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/"
            "Vinculos/vinculos_referencia_afirmacao.json")
vivo = {v["id_vinculo"]: v for v in json.loads(VIVO.read_text(encoding="utf-8"))}
n_tag = 0
for v in vinc:
    if v["trecho_ancora"] != vivo[v["id_vinculo"]]["trecho_ancora"] and "reancorado_em" not in v:
        v["reancorado_em"] = TAG
        n_tag += 1
log["etapas"]["e_tags_pipeline_151"] = n_tag

# ── verificação final ───────────────────────────────────────────────────────
import sys
sys.path.insert(0, str(BANCADA / "scripts"))
from contrato import verificar_literal
sts = {}
nao_lit = []
for v in vinc:
    s = verificar_literal(v["trecho_ancora"], corpo)["status"]
    sts[s] = sts.get(s, 0) + 1
    if s != "LITERAL":
        nao_lit.append(v["id_vinculo"])
log["verificacao_final"] = {"status": sts, "nao_literais": nao_lit,
                            "com_cabecalho": [v["id_vinculo"] for v in vinc if "###" in v["trecho_ancora"]]}
log["erros_guardas"] = erros

if not nao_lit and not erros:
    CANON.write_text(corpo, encoding="utf-8")
    VINC.write_text(json.dumps(vinc, ensure_ascii=False, indent=1), encoding="utf-8")
    print("✅ bancada atualizada (canônica + vínculos)")
else:
    print("⚠️ guardas reprovaram algo — NADA gravado")

print(json.dumps({"literalidade": sts, "nao_literais": nao_lit,
                  "trims": len(trims), "tags151": n_tag,
                  "com_###": log["verificacao_final"]["com_cabecalho"],
                  "erros": erros}, ensure_ascii=False, indent=1))
(Path(BANCADA / "canonico/log_reparo_consolidado_2026-09-11.json")).write_text(
    json.dumps(log, ensure_ascii=False, indent=1), encoding="utf-8")
print("log → bancada_at02/canonico/log_reparo_consolidado_2026-09-11.json")
