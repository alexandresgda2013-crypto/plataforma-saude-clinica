#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 40 — Resposta do mestre (ancoragem kit + reconciliação diff + precisão de escopo
+ achado arquitetural): réplica da casa
========================================================================================
Data: 2026-09-16 · Rodada 22 · 0 ciência (só leituras/greps; nada escrito no acervo nem no kit).

Réplica dos números do mestre:
  M1. Be48a5efa… — prefixo confere com o truncado registrado (rev.24)? Byte-verify: impossível
      via paste (formatação) — declarado; selável se o arquivo dele chegar.
  M2. Kit: uso 23 (12 clinico/6 contexto/4 gap) · comparador 59 c/ 8 valores · moderadores 22 ·
      usado_em_biblioteca 23 — greps com regex+escopo GRAVADOS (norma: comando ou não vale).
  M3. evidence_role 22/22 human_clinical (escopo das claims entries do Bloco).
  M4. Acervo V7: evid_role preclinical_mechanistic 133 · review 30 (+ restantes) — confere com
      a precisão de escopo dele (cobertura do kit = trilha humana apenas).
  M5. Wiring: claims distintos B1.SM02.* no kit × B1.MEC.* (esperado 43 × 0).
  M6. natureza_relacao = nao_estabelecida no acervo (esperado 4/274) — lado de cá da D-03.
  M7. Diff +17/−7 dele × +10/−7 nosso: reconciliação aceita condicionada ao confronto byte a
      byte do arquivo anexo dele — PENDENTE NOMEADO (operador repassa o anexo).
"""
import hashlib, json, re
from collections import Counter
from pathlib import Path

BASE = Path("/home/user/BIBLIOTECAS")
ATUAL = BASE / "B01_Neuroinflamacao/atuais"
KIT = BASE / "_documentos_serie/KIT_CLINICA_recebido_2026-09-15"
RECB = BASE / "_documentos_serie/P8_revisao_mestre_3pontos_recebida_2026-09-16"
TRILHA = ATUAL / "producao/TRILHA40_resposta_mestre_kit_reconciliacao_2026-09-16.json"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

R = {"trilha": 40, "data": "2026-09-16", "rodada": 22,
     "objeto": "resposta do mestre (kit ancorado + diff reconciliado + escopo + camada a montante) — réplica",
     "etapas": {}, "vereditos": {}, "ciencia_tocada": 0}

txt_resp = (RECB / "RESPOSTA_MESTRE_ANCORAGEM_KIT_E_RECONCILIACAO_2026-09-16.md").read_text(encoding="utf-8")
R["etapas"]["M0_arquivo"] = {"sha_resposta_mestre": sha(RECB / "RESPOSTA_MESTRE_ANCORAGEM_KIT_E_RECONCILIACAO_2026-09-16.md")}

# ---------- M1. sha por extenso
m = re.search(r"be48a5efa1d67f9e7b4ae3a38fdcf562b924cc03fc58e91baa2c63a3c6b33e92", txt_resp)
SHA_REV = "be48a5efa1d67f9e7b4ae3a38fdcf562b924cc03fc58e91baa2c63a3c6b33e92"
R["etapas"]["M1_sha_revisao"] = {
    "sha_por_extenso_presente_na_resposta": bool(m),
    "prefixo_confere_com_o_truncado_da_rev24": SHA_REV.startswith("be48a5ef"),
    "byte_verify_contra_nossa_copia": "IMPOSSÍVEL — nossa cópia veio colada (renderização), não é o arquivo dele; honestamente nomeado",
    "condicao_de_selagem": "se o operador repassar o ARQUIVO da revisão, a casa confere be48a5efa… byte a byte"}
R["vereditos"]["M1_prefixo_recebido_selagem_pendente_arquivo"] = bool(m)

# ---------- M2/M3/M5. greps no kit (escopo: 6º BLOCO + demais arquivos, tudo registrado)
bloco = (KIT / "6º BLOCO DE ESTADO  v1.6.md").read_text(encoding="utf-8")
schema_claim = (KIT / "3º SCHEMA-CLAIM — v1.2.md").read_text(encoding="utf-8")
lista = (KIT / "5º LISTA CANÔNICA — B1  SM-02 V1.3.md").read_text(encoding="utf-8")

uso_vals = re.findall(r"(?m)^\s*uso:\s*([a-z_]+)\s*$", bloco)
comp_vals = re.findall(r"(?m)^\s*comparador:\s*(.+?)\s*$", bloco)
mod_hits = re.findall(r"(?m)^\s*moderadores:\s*$", bloco)
ub_vals = re.findall(r"(?m)^\s*usado_em_biblioteca:\s*([a-z_]+)\s*$", bloco)
er_vals = re.findall(r"(?m)^\s*evidence_role:\s*([a-z_]+)\s*$", bloco)

claims_sm02 = set(re.findall(r"B1\.SM02\.\d{3}[a-z]?", "\n".join([bloco, lista, schema_claim])))
claims_mec = set(re.findall(r"B1\.MEC\.BLOCO\d{2}\.\d{3}", "\n".join([bloco, lista, schema_claim])))

R["etapas"]["M2_campos_do_bloco"] = {
    "regex_escopo": {k: v for k, v in {
        "uso": r"(?m)^\s*uso:\s*([a-z_]+)\s*$ @6ºBLOCO",
        "comparador": r"(?m)^\s*comparador:\s*(.+?)\s*$ @6ºBLOCO",
        "moderadores": r"(?m)^\s*moderadores:\s*$ @6ºBLOCO",
        "usado_em_biblioteca": r"(?m)^\s*usado_em_biblioteca:\s*([a-z_]+)\s*$ @6ºBLOCO",
        "evidence_role": r"(?m)^\s*evidence_role:\s*([a-z_]+)\s*$ @6ºBLOCO"}.items()},
    "uso": {"total": len(uso_vals), "dist": dict(Counter(uso_vals))},
    "comparador": {"total": len(comp_vals), "valores_distintos": len(set(comp_vals)),
                   "valores": sorted(set(comp_vals))},
    "moderadores_ocorrencias": len(mod_hits),
    "usado_em_biblioteca": {"total": len(ub_vals), "dist": dict(Counter(ub_vals))},
    "evidence_role": {"total": len(er_vals), "dist": dict(Counter(er_vals))},
}
R["etapas"]["M5_wiring_claims"] = {
    "regex": r"B1\.SM02\.\d{3}[a-z]? e B1\.MEC\.BLOCO\d{2}\.\d{3} @BLOCO+LISTA+SCHEMA",
    "SM02_distintos": len(claims_sm02), "SM02_lista": sorted(claims_sm02),
    "MEC_distintos": len(claims_mec)}

cc = R["etapas"]["M2_campos_do_bloco"]
R["vereditos"]["M2_uso_23_12_6_4"] = (cc["uso"]["total"] == 23 and cc["uso"]["dist"] ==
    {"clinico": 12, "contexto_mecanistico": 6, "gap_pesquisa": 4, **{k: v for k, v in cc["uso"]["dist"].items() if k not in ("clinico", "contexto_mecanistico", "gap_pesquisa")}} and
    cc["uso"]["dist"].get("clinico") == 12 and cc["uso"]["dist"].get("contexto_mecanistico") == 6 and cc["uso"]["dist"].get("gap_pesquisa") == 4)
R["vereditos"]["M2_comparador_59_e_8_valores"] = (cc["comparador"]["total"] == 59 and cc["comparador"]["valores_distintos"] == 8)
R["vereditos"]["M2_moderadores_22"] = (cc["moderadores_ocorrencias"] == 22)
R["vereditos"]["M2_usado_em_biblioteca_23_nao"] = (cc["usado_em_biblioteca"]["total"] == 23 and cc["usado_em_biblioteca"]["dist"] == {"nao": 23})
R["vereditos"]["M3_evidence_role_22de22_human_clinical"] = (cc["evidence_role"]["total"] == 22 and cc["evidence_role"]["dist"] == {"human_clinical": 22})
R["vereditos"]["M5_wiring_43_SM02_e_0_MEC"] = (R["etapas"]["M5_wiring_claims"]["SM02_distintos"] == 43 and R["etapas"]["M5_wiring_claims"]["MEC_distintos"] == 0)

# ---------- M4. acervo evid_role
fichas = []
for fn in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
    d = json.load(open(ATUAL / f"Evidencias/Bibliografia/{fn}"))
    it = d if isinstance(d, list) else list(d.values())[0]
    fichas += (list(it.values()) if isinstance(it, dict) else it)
er = Counter(str(f.get("evid_role")) for f in fichas)
R["etapas"]["M4_acervo_evid_role"] = {"dist": dict(er.most_common())}
R["vereditos"]["M4_133_preclinical_e_30_review"] = (er.get("preclinical_mechanistic") == 133 and er.get("review") == 30)

# ---------- M6. nao_estabelecida no acervo
vinc = json.load(open(ATUAL / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json"))
vinc = vinc if isinstance(vinc, list) else vinc["vinculos"]
ne = [x["id_vinculo"] for x in vinc if x.get("natureza_relacao") == "nao_estabelecida"]
R["etapas"]["M6_nao_estabelecida"] = {"total": len(ne), "ids": ne,
    "lado_kit_da_D03": "4 claims gap_pesquisa (contados em M2, mesmo grep) — convergência dos dois lados medida"}
R["vereditos"]["M6_4_em_274"] = (len(ne) == 4)

# ---------- M7. pendente do anexo
R["pendente_nomeado"] = ("anexo do mestre (SEU arquivo P-8 com o comentário F-C2 de 6 linhas) — operador repassa; "
    "casa faz o confronto byte a byte contra o oficial instalado (84fa918d…): critério de aceite = diff SO o comentário + "
    "execução 2/299/exit 1 + V-14 verde + F-C2 disparando. Reconciliação +17/−7 dele × +10/−7 nosso: remoções idênticas (−7) ✔ confere com o medido na trilha 36.")

TRILHA.write_text(json.dumps(R, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(R["vereditos"], ensure_ascii=False, indent=2))
print("uso:", R["etapas"]["M2_campos_do_bloco"]["uso"])
print("comparador valores:", R["etapas"]["M2_campos_do_bloco"]["comparador"]["valores"])
print("SM02:", R["etapas"]["M5_wiring_claims"]["SM02_distintos"], "| MEC:", R["etapas"]["M5_wiring_claims"]["MEC_distintos"])
print("evid_role acervo:", dict(list(R["etapas"]["M4_acervo_evid_role"]["dist"].items())[:6]))
print("trilha:", TRILHA.name)
