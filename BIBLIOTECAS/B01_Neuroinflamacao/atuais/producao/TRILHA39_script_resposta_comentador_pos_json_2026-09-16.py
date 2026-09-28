#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 39 — Resposta do comentador PÓS-JSON (N1/N2): réplica da casa
===================================================================
Data: 2026-09-16 · Rodada 21 (continuação 2) · 0 ciência.

Cronologia (esclarecida pelo operador): o parecer §1-§24 foi escrito SEM os JSONs;
esta resposta é a posição PÓS-JSONs. Consequência registrada: a "premissa envelhecida"
do §12 (trilha 38) fica explicada — e §2.6 daqui já acerta o ponto.

Bateria:
  T1. Digitais + cronologia corrigida.
  T2. §2.3 pmid_oficial: furo confirmado (pattern admite vazio sempre; sem allOf) +
      draft-07 EXPRESSA → proposta da casa testada em 6 casos (mesmo princípio da carta 5 §2).
      Medida: hoje 0/237 pmid vazio; natureza 0/237 → regra não dispara hoje, vale p/ pós-migração.
  T3. §3.4 uso: imprecisão "3 primeiros + 3 últimos" CONFIRMADA (exclusivos 2+2, comum 1)
      + texto corrigido oferecido.
  T4. §2.4/D3: descrições com medições de rodada → 2 instâncias localizadas
      ("Medido hoje: 0/66" · "os 20 vinculos"). Casa ADOTA (eco da própria norma:
      medida sem comando gravado não vale — número em texto normativo perde o comando).
  T5. TENSÃO INTERNA NOMEADA: §3.3 ("solução atual é suficiente") × ponto 1 da análise
      anterior (exclusividade do condicao). Ambos verbatim com sha. Pedido de confirmação.
      A casa MANTÉM a proposta da carta 5 §2 por mérito próprio (furo provado executável).
  T6. Convergências com a carta 5/adições da casa: D1 ≡ Adição A (alias) · D6/§3.5 ≡ fino 2
      (forca_biologica ao portão) · D5 ≡ §5 carta 5 (Decisão 1 registrada) · §2.2 (transição
      explícita + aposentadoria por 100% idênticos) ≡ nossa proposta.
  T7. §6 ciclo de fechamento ≡ método da casa (execução→medição→correção→reexecução→convergência).
"""
import hashlib, json, copy
from pathlib import Path
import jsonschema
from jsonschema import Draft7Validator

BASE = Path("/home/user/BIBLIOTECAS")
ATUAL = BASE / "B01_Neuroinflamacao/atuais"
RECB = BASE / "_documentos_serie/L05_v1.2_schemas_recebidos_2026-09-16"
TRILHA = ATUAL / "producao/TRILHA39_resposta_comentador_pos_json_2026-09-16.json"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

R = {"trilha": 39, "data": "2026-09-16", "rodada": "21-continuação-2",
     "objeto": "resposta do comentador pós-JSON (N1/N2) — réplica da casa",
     "etapas": {}, "vereditos": {}, "ciencia_tocada": 0}

SR = json.load(open(RECB / "schema_referencia_v1.2_recebido_2026-09-16.json"))
SV = json.load(open(RECB / "schema_vinculo_v1.2_recebido_2026-09-16.json"))
NOVA = (RECB / "RESPOSTA_COMENTADOR_POS_JSON_N1N2_2026-09-16.md").read_text(encoding="utf-8")
ANT = (RECB / "ANALISE_COMENTADOR_SCHEMAS_V12_2026-09-16.md").read_text(encoding="utf-8")

fichas = []
for fn in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
    d = json.load(open(ATUAL / f"Evidencias/Bibliografia/{fn}"))
    it = d if isinstance(d, list) else list(d.values())[0]
    fichas += (list(it.values()) if isinstance(it, dict) else it)

# ---------- T1
R["etapas"]["T1_digitais_cronologia"] = {
    "resposta_pos_json": sha(RECB / "RESPOSTA_COMENTADOR_POS_JSON_N1N2_2026-09-16.md"),
    "cronologia": "parecer §1-§24 (trilha 38) = PRÉ-JSON · análise 3 pontos (trilha 37) = intermediária · ESTA = pós-JSON. §2.6 daqui já acerta citacao_confirmada (coerente com a medição V1 da trilha 38)."}

# ---------- T2. pmid_oficial
props = SR["properties"]
pat = props["pmid_oficial"]["pattern"]
tem_allof_pmid = any("pmid" in json.dumps(c) for c in SR.get("allOf", []))
tpl = {"id_referencia_interna": "REF_TESTE_2026", "pmid_oficial": "12345678",
       "titulo_artigo": "x", "origem_pipeline": "BUSCA_FERRAMENTA", "g1_metodo": "eutils_automatico",
       "natureza_evidencia": "humana_observacional", "desenho_estudo": "coorte_prospectiva",
       "desenho_estudo_bruto": "Cohort Study", "status_auditoria": "",
       "verification_status": "pendente"}
def valido(inst, schema=SR):
    try:
        jsonschema.validate(inst, schema); return True
    except jsonschema.ValidationError:
        return False
h1 = valido(tpl)                                                     # molde ok
i2 = copy.deepcopy(tpl); i2["pmid_oficial"] = ""
h2 = valido(i2)                                                      # FURO: humana + pmid vazio passa?
i3 = copy.deepcopy(tpl); i3["pmid_oficial"] = "ABC"
h3 = valido(i3)                                                      # letra reprova (pattern já certo nisto)
FIX = {"if": {"properties": {"natureza_evidencia": {"not": {"const": "nao_aplicavel"}}},
              "required": ["natureza_evidencia"]},
       "then": {"properties": {"pmid_oficial": {"pattern": "^[0-9]{1,8}$"}}}}
SR2 = copy.deepcopy(SR); SR2["allOf"].append(FIX)
f1 = valido(tpl, SR2)
f2 = valido(i2, SR2)                                                 # furo fechado?
i4 = copy.deepcopy(tpl); i4["natureza_evidencia"] = "nao_aplicavel"; i4["desenho_estudo"] = "manual_ou_consenso"; i4["pmid_oficial"] = ""
f3 = valido(i4, SR2)                                                 # manual/consenso sem pmid ok?
i5 = copy.deepcopy(i4); i5["pmid_oficial"] = "12345678"
f4 = valido(i5, SR2)                                                 # inverse não proibida (escolha de design)
vazios_hoje = sum(1 for f in fichas if not str(f.get("pmid_oficial", "")).strip())
R["etapas"]["T2_pmid_oficial"] = {
    "pattern_atual": pat, "admite_vazio_sempre": pat == "^[0-9]{0,8}$",
    "allOf_toca_pmid": tem_allof_pmid,
    "prova_do_furo": {"molde_valido": h1, "humana_com_pmid_vazio_PASSA": h2, "letra_reprova": (not h3)},
    "proposta_casa": FIX,
    "medicao_da_proposta": {"molde_ok": f1, "furo_fechado": (not f2),
                            "nao_aplicavel_sem_pmid_ok": f3,
                            "inversa_nao_proibida_escolha_design": f4,
                            "nota": "expressa só a direção declarada ('vazio APENAS se nao_aplicavel'); a inversa (nao_aplicavel EXIGE vazio) fica como decisão dele"},
    "dado_hoje": {"pmid_vazio": vazios_hoje, "natureza_preenchida": sum(1 for f in fichas if "natureza_evidencia" in f),
                  "leitura": "regra não dispara hoje (0 vazio; natureza migra depois) — pós-migração é quando ela trabalha"},
    "obs": "draft-07 EXPRESSA (como condicao — carta 5 §2): a casa recomenda SCHEMA; a alternativa 'portão' exige só declaração explícita (D2/D4 dele)"}
R["vereditos"]["T2_pmid_furo_confirmado_proposta_medida"] = (h1 and h2 and (not h3) and f1 and (not f2) and f3)

# ---------- T3. uso description
enum_uso = SV["properties"]["uso"]["enum"]
clin = {"clinico", "contexto_mecanistico"}; mec = {"nucleo_causal", "suporte_correlacional"}; comum = {"gap_pesquisa"}
R["etapas"]["T3_uso_3mais3"] = {
    "enum_uniao": enum_uso, "qtd": len(enum_uso),
    "exclusivos_clinica": sorted(clin), "exclusivos_mecanistica": sorted(mec), "comum": sorted(comum),
    "formulacao_atual": SV["properties"]["uso"]["description"],
    "imprecisao_CONFIRMADA": "a união tem 5 valores com interseção; '3 últimos' sugere 3 da mecanística, mas exclusivos são 2 + 1 comum",
    "texto_oferecido": ("clinica: {clinico, contexto_mecanistico} · mecanistica: {nucleo_causal, suporte_correlacional} · "
                        "gap_pesquisa: comum às duas (interseção). A trilha do vínculo seleciona o sub-conjunto permitido.")}
R["vereditos"]["T3_imprecisao_confirmada_com_texto"] = (len(enum_uso) == 5 and comum.issubset(set(enum_uso)))

# ---------- T4. medições em descriptions
def acha(o, caminho="", out=None):
    out = out if out is not None else []
    if isinstance(o, dict):
        for k, v in o.items():
            acha(v, f"{caminho}.{k}", out)
    elif isinstance(o, str) and caminho.endswith("description"):
        if "Medido hoje" in o or "os 20 vinculos" in o:
            trecho = "Medido hoje" if "Medido hoje" in o else "os 20 vinculos"
            out.append({"campo": caminho, "marcador": trecho})
    return out
hits = acha({"SR": SR["properties"], "SV": SV["properties"]})
R["etapas"]["T4_medicoes_em_descriptions"] = {"instancias": hits, "total": len(hits),
    "posicao_da_casa": "ADOTADO com eco da nossa própria norma — número sem comando gravado não vale; em texto normativo o comando se perde. REGRA fica na description; MEDIÇÃO vai ao relatório/gate de migração com data e trilha (a nossa T35/T37 regeneram a qualquer tempo)."}
R["vereditos"]["T4_2_instancias_localizadas"] = (len(hits) == 2)

# ---------- T5. tensão interna
p1 = "Peço que isso seja fechado no schema/gate para evitar estado semanticamente inválido" in ANT
s33 = "A solução atual é suficiente" in NOVA
R["etapas"]["T5_tensao_condicao"] = {
    "analise_anterior_ponto1_exige_exclusividade": p1,
    "resposta_pos_json_3.3_diz_suficiente": s33,
    "leitura_da_casa": ("tensão real: ou o ponto 1 está RETIRADO, ou §3.3 fala só do lado positivo. "
                        "A prova executável da trilha 37 é independente da opinião: sustenta+condicao PASSA hoje = estado inválido admissível. "
                        "A casa MANTÉM a proposta (carta 5 §2, medida em 5 casos) por mérito próprio e pede confirmação explícita de retirada/manutenção."),
}
R["vereditos"]["T5_tensao_nomeada_pedido_confirmacao"] = (p1 and s33)

# ---------- T6/T7 convergências (registro cruzado, já medido nas trilhas 37/38)
R["etapas"]["T6_convergencias_com_a_casa"] = {
    "D1_transicao_alias": "≡ Adição A da casa (trilha 37-F, com 162/237 medidos + fix de 2 linhas) — a versão dele é estrutural; a nossa traz o dado",
    "D6_forca_biologica": "≡ fino 2 da carta 5 — ele recomenda PORTÃO explicitamente; 24 vínculos medidos na zona",
    "D5_trilha_uso": "≡ §5 da carta 5 — implementação pronta, falta registro da Decisão 1",
    "2.2_aposentadoria_100pc": "≡ nossa leitura da própria liturgia de espelho dele",
    "3.1_V17_portao_3testes": "≡ oferta da casa (texto já no schema)",
}
R["etapas"]["T7_ciclo_fechamento_§6"] = "Schema→Derivador→Acervo→Gate→Medição→Correções→Reexecução→Convergência ≡ método bilateral da casa (P-8, cartas 10-12). Concordância plena; a casa replica a execução final."

TRILHA.write_text(json.dumps(R, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(R["vereditos"], ensure_ascii=False, indent=2))
print("pmid hoje:", R["etapas"]["T2_pmid_oficial"]["dado_hoje"])
print("trilha:", TRILHA.name)
