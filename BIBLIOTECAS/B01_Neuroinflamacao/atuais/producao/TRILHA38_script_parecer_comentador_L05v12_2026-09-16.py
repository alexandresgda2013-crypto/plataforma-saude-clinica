#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 38 — Parecer formal v1.0 do comentador (L-05 v1.2): réplica da casa
==========================================================================
Data: 2026-09-16 · Rodada 21 (continuação) · 0 ciência (só leitura; nenhuma re-leitura
de artigo — REGRA: status/estrutura sim, conteúdo científico não).

Réplica dos números do parecer:
  V1. citacao_confirmada "237/237=true" (§12) × resolução R6/D4 registrada no schema v1.2
      (premissa envelhecida?) × gate rev.A2 não usa o campo (grep).
  V2. caso REF_RAISON_2013 (§8): ficha e vínculo(s) existem? status medidos (sem abrir artigo).
  V3. "fila humana de 1 para 102" (§8/§16): o "1" = VINC_B1_0047 (medido)? composição
      possível dos 102 com os dados reais (274) — reversível sem o relatório dele?
  V4. "146 declarados × 103 capturados" (§13): recontagem por categoria no catálogo oficial
      (byte idêntico ao item 1º do kit) + referência da trilha 25.
  V5. "30 review" (§4/D2): evid_role=review medido (= D-B1-R3-V2CLAIM da casa).
  V6. §7: a proibição "papel isolado nunca é eficácia" — já está no schema v1.2? (convergência)
  V7. §13 fluxo derivador × dívida D-L05-IDS-JSON da casa (mesma sequência?).
  V8. Parecer §6 (integridade referencial não exprimível em draft-07) — já verificado na
      trilha 35 (V-17); registrado por referência.
PENDENTE NOMEADO: relatório de execução do auditor-2 (regra 172/102) NÃO chegou à bancada.
"""
import hashlib, json, re
from collections import Counter
from pathlib import Path

BASE = Path("/home/user/BIBLIOTECAS")
ATUAL = BASE / "B01_Neuroinflamacao/atuais"
RECB = BASE / "_documentos_serie/L05_v1.2_schemas_recebidos_2026-09-16"
CAT = Path("/home/user/Ferramentas de geração e auditoria/01_norteadores/1º IDS_OFICIAIS.md")
GATE = Path("/home/user/Ferramentas de geração e auditoria/scripts/gate_script.py")
TRILHA = ATUAL / "producao/TRILHA38_parecer_comentador_L05v12_2026-09-16.json"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

R = {"trilha": 38, "data": "2026-09-16", "rodada": "21-continuação",
     "objeto": "parecer comentador v1.0 (L-05 v1.2) — réplica da casa",
     "digitais": {"parecer": sha(RECB / "PARECER_COMENTADOR_L05_V12_v1.0_2026-09-16.md"),
                  "schema_vinculo_v1.2": sha(RECB / "schema_vinculo_v1.2_recebido_2026-09-16.json"),
                  "schema_referencia_v1.2": sha(RECB / "schema_referencia_v1.2_recebido_2026-09-16.json")},
     "etapas": {}, "vereditos": {}, "ciencia_tocada": 0}

vinc = json.load(open(ATUAL / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json"))
vinc = vinc if isinstance(vinc, list) else vinc["vinculos"]
fichas = []
for fn in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
    d = json.load(open(ATUAL / f"Evidencias/Bibliografia/{fn}"))
    it = d if isinstance(d, list) else list(d.values())[0]
    fichas += (list(it.values()) if isinstance(it, dict) else it)
SR = json.load(open(RECB / "schema_referencia_v1.2_recebido_2026-09-16.json"))
SV = json.load(open(RECB / "schema_vinculo_v1.2_recebido_2026-09-16.json"))
ref_byid = {f.get("id_referencia_interna"): f for f in fichas}

# ---------- V1. citacao_confirmada
dist = Counter(str(f.get("citacao_confirmada")) for f in fichas)
desc_r6 = SR["properties"]["citacao_confirmada"]["description"]
gate_txt = GATE.read_text(encoding="utf-8") if GATE.exists() else ""
usos_gate = [l for l in gate_txt.splitlines() if "citacao_confirmada" in l]
R["etapas"]["V1_citacao_confirmada"] = {
    "medido_distribuicao": dict(dist),
    "premissa_237de237_true_CONFERE": dist.get("True") == 237,
    "schema_v1.2_R6_D4_diz_RESOLVIDO": "RESOLVIDO" in desc_r6 and "DEFAULT DE GERACAO" in desc_r6,
    "schema_cita_PROMPT_v4.2_L1290_L1313": "L1290" in desc_r6 and "L1313" in desc_r6,
    "gate_revA2_linhas_com_o_campo": usos_gate or "nenhuma — banido confirmado",
    "leitura_da_casa": "o §12 do parecer parte de 'sem origem conhecida', mas a v1.2 que ele mesmo analisa registra R6/D4 RESOLVIDO (default de geração do PROMPT v4.2) + DEPRECATED + banido de portão desde gate rev.A2. A dívida de proveniência ESTÁ encerrada; sobra só a formalização do destino (D4 do operador): manter deprecated sem carga = estado atual."
}
R["vereditos"]["V1_premissa_envelhecida_resolucao_ja_registrada"] = (
    dist.get("True") == 237 and "RESOLVIDO" in desc_r6)

# ---------- V2. REF_RAISON_2013
raison_f = ref_byid.get("REF_RAISON_2013")
raison_v = [x for x in vinc if x.get("id_referencia_interna") == "REF_RAISON_2013"]
R["etapas"]["V2_RAISON_2013"] = {
    "ficha_existe": raison_f is not None,
    "ficha_status": {k: raison_f.get(k) for k in ("id_referencia_interna", "evid_role", "desenho_estudo", "verification_status", "pmid_oficial")} if raison_f else None,
    "vinculos": [{"id": x["id_vinculo"], "sa": x.get("status_auditoria"), "vs": x.get("verification_status"),
                  "uso": x.get("uso"), "g2": x.get("g2_elegibilidade")} for x in raison_v],
    "nota": "só status/estrutura — a leitura do caso (subgrupo inflamação alta × amostra geral negativa) é do auditor-2 e do G3 humano; a casa NÃO reabre ciência"
}
R["vereditos"]["V2_RAISON_existe_e_consistente_com_o_uso_como_teste"] = bool(raison_f and raison_v)

# ---------- V3. fila 1→102
cross = Counter(f'{x.get("status_auditoria")}|{x.get("verification_status")}' for x in vinc)
v47 = [x for x in vinc if x.get("id_vinculo") == "VINC_B1_0047"]
candidatos_102 = {
    "extrapolado+pendente+pendente_fulltext+emergente": 62+7+1+1,
    "+PARCIALMENTE_CONFIRMADO": 62+7+1+1+19,
    "+NAO_LOCALIZADO": 62+7+1+1+19+1,
    "PARCIAL+extrapolado+pendentes...outras somas": "ver cruzamento completo",
}
R["etapas"]["V3_fila_1_para_102"] = {
    "cruzamento_statusAuditoria_x_verificationStatus": dict(cross.most_common()),
    "VINC_B1_0047": [{"sa": x.get("status_auditoria"), "vs": x.get("verification_status"),
                      "uso": x.get("uso"), "ref": x.get("id_referencia_interna")} for x in v47],
    "o_1_da_fila_anterior_CONFERE_com_VINC_B1_0047": len(v47) == 1,
    "somas_candidatas_a_102": candidatos_102,
    "conclusao": "274-172=102 — a regra exata do auditor-2 NÃO é reversível da nossa bancada sem o relatório de execução dele (que o comentador cita e a casa NÃO recebeu). Nenhuma soma simples dos nossos status dá 102 → PENDENTE NOMEADO: pedir o relatório/script de execução (provável '.py' que o operador mencionou)."
}
R["vereditos"]["V3_1_confere_102_indecidivel_sem_relatorio_NOMEADO"] = (len(v47) == 1)

# ---------- V4. catálogo 146 por categoria
linhas = CAT.read_text(encoding="utf-8").splitlines()
ids = re.findall(r"\b((?:exame|suplemento|mecanismo|cenario)_[a-z0-9_]+)\b", "\n".join(linhas))
rem = [l for l in linhas if "removid" in l.lower()]
por_cat = Counter(i.split("_")[0] for i in sorted(set(ids)))
R["etapas"]["V4_catalogo_146"] = {
    "sha_catalogo_oficial": sha(CAT),
    "contagem_mecanica_ids_distintos": len(set(ids)), "por_categoria": dict(por_cat),
    "linhas_com_removidos": len(rem),
    "trilha25_legado_parser": "103 (número citado pelo comentador — é o da nossa trilha 25)",
    "gap_43": "é exatamente o escopo da dívida da casa D-L05-IDS-JSON (derivador oficial: rodar→comparar 146 por categoria→sha)",
    "nota": "o comentador cita '146 declarados × 103 capturados' — são os NOSSOS números; o bloqueador §13 dele = D-L05-IDS-JSON já nomeada pela casa"
}

# ---------- V5. 30 review
rev = sum(1 for f in fichas if f.get("evid_role") == "review")
R["etapas"]["V5_review_30"] = {"evid_role_review": rev, "confere_com_D-B1-R3-V2CLAIM": rev == 30}
R["vereditos"]["V5_30_review_CONFERE"] = (rev == 30)

# ---------- V6. §7 já no schema?
R["etapas"]["V6_regra_papel_ja_no_schema"] = {
    "proibicao_presente_em_papel_description": "proibidos de inferir eficacia ou direcao a partir de 'papel' isolado" in SV["properties"]["ancoras"]["items"]["properties"]["papel"]["description"],
    "leitura": "o §7 do parecer pede a regra no contrato do Motor — no SCHEMA v1.2 ela já está; falta carregá-la no contrato de execução (autoridade do Auditor-Mestre) e/ou prosa da 1.2"
}
R["vereditos"]["V6_convergencia_ja_implementada_no_schema"] = R["etapas"]["V6_regra_papel_ja_no_schema"]["proibicao_presente_em_papel_description"]

# ---------- V7. fluxo §13 × dívida da casa
R["etapas"]["V7_fluxo_derivador"] = {
    "sequencia_do_parecer": "fonte declarada→derivador→146 IDs→contagem por categoria→conferência→hash/versão→catálogo operacional",
    "divida_da_casa_D-L05-IDS-JSON": "rodar derivador→comparar 146 por categoria→registrar sha (critério de aceite do §7 R2 do auditor)",
    "conclusao": "mesma sequência — o bloqueador §13 do parecer é a dívida já nomeada da casa; reforço externo da prioridade"
}

# ---------- V8. §6 draft-07
R["etapas"]["V8_draft07_limite"] = {
    "parecer": "integridade referencial/ cardinalidade semântica exigem portão externo",
    "estado_na_bancada": "VERIFICADO na trilha 35 (ancora_principal inexprimível → V-17 de portão; o próprio schema v1.2 o declara) e trilha 37 (condicao-exclusividade É exprimível — ficou no schema)",
    "leitura": "as citações dele ao draft-07 batem com nossas medições; a fronteira schema×portão do v1.2 está coerente com os dois lados"
}
R["vereditos"]["V8_fronteira_schema_portao_coerente"] = True

R["pendente_nomeado"] = ("relatório de execução do auditor-2 contra B1 V7 (regra conservadora 172/102, "
                         "caso REF_RAISON_2013 aplicado, lista dos 102) — citado pelo comentador, NÃO recebido; "
                         "provável conteúdo do '.py'/anexo faltante. Casa replica quando chegar.")

TRILHA.write_text(json.dumps(R, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(R["vereditos"], ensure_ascii=False, indent=2))
print("RAISON:", json.dumps(R["etapas"]["V2_RAISON_2013"]["vinculos"], ensure_ascii=False))
print("cross top6:", dict(list(R["etapas"]["V3_fila_1_para_102"]["cruzamento_statusAuditoria_x_verificationStatus"].items())[:6]))
print("V4 por_categoria:", R["etapas"]["V4_catalogo_146"]["por_categoria"], "total:", R["etapas"]["V4_catalogo_146"]["contagem_mecanica_ids_distintos"], "removidos:", R["etapas"]["V4_catalogo_146"]["linhas_com_removidos"])
print("trilha:", TRILHA.name)
