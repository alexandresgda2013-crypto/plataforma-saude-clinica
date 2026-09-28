#!/usr/bin/env python3
# B15 — tríade + manifesto + trilha (rodada [AT 2026-09-09])
import json, os, copy

HERE = os.path.dirname(os.path.abspath(__file__))
refs = json.load(open(f"{HERE}/b15_refs_data.json"))
anchors = json.load(open(f"{HERE}/b15_ancoras.json"))
doc = open(f"{HERE}/B15 AUTOFAGIA MTOR V2 CANONICA.md", encoding="utf-8").read()

PM = f"{HERE}/Evidencias/Bibliografia/01_pmids.json"
VI = f"{HERE}/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
LE = f"{HERE}/Auditoria_B15/ledger_auditoria_B15.json"
MF = f"{HERE}/Evidencias/Bibliografia/_manifesto_biblioteca.json"

pmids = json.load(open(PM)); vinc = json.load(open(VI)); led = json.load(open(LE))
tpl_ml = next(x for x in led if x["evid_role"] == "preclinical_mechanistic")
tpl_ec = next(x for x in led if x["evid_role"] == "human_clinical")
tpl_ob = next(x for x in led if x["evid_role"] == "review")
tpl_ml_v = next(x for x in vinc if x["evid_role"] == "preclinical_mechanistic")
tpl_ec_v = next(x for x in vinc if x["evid_role"] == "human_clinical")
tpl_ob_v = next(x for x in vinc if x["evid_role"] == "review")

n0 = len(pmids); today = "2026-09-09"
nomap = {"ML": tpl_ml, "EC": tpl_ec, "OB": tpl_ob}
nomap_v = {"ML": tpl_ml_v, "EC": tpl_ec_v, "OB": tpl_ob_v}

for i, r in enumerate(refs):
    rid = r["id_referencia_interna"]; tag = r["_tag"]
    pub = {k: v for k, v in r.items() if not k.startswith("_")}
    pmids.append(pub)
    idx = n0 + i + 1
    tpl = copy.deepcopy(nomap[tag])
    tpl.update({"id_auditoria": f"AUD_B15_{idx:04d}", "id_referencia_interna": rid,
        "pmid_oficial": r["pmid_oficial"], "secao_origem": "B15_CANONICA_V2",
        "trecho_ancora": anchors[rid], "citacao_literal": f"{rid.replace('REF_','')}[{tag}]",
        "natureza_da_relacao": r["_nat"], "grau_maturidade_cientifica": r["_mat"],
        "acao_correcao": r["_acao"], "origem_entrada": "GPM",
        "especie_mesh": r["especie_mesh"], "evid_role": r["evid_role"],
        "status_auditoria": "APROVADO", "destino": "FICA_MECANISMO", "reconciliado": True,
        "portao_G1_existencia": "VERIFIED_REFERENCE",
        "portao_G2_elegibilidade": "NAO_APLICAVEL" if tag == "ML" else "ELIGIBLE_SOURCE",
        "portao_G3_suporte": "APROVADO",
        "verificacao": {
            "verificador": "IA G3 Rodada [AT] GPM B15 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
            "data_verificacao": today,
            "g1_metodo": "eutils_automatico (esearch+esummary+efetch)",
            "abstract_ou_trecho": "abstract lido e conferido (autor/ano/tema/direção) antes de incorporar",
            "query_utilizada": "esearch PubMed por PMID do insumo; esummary confere autor+print",
            "g2_motivo": r["g2_motivo"],
            "g3_nota": "P-6 2a verificação independente (avaliador cego) PENDENTE — fecho rodada 16/16"}})
    led.append(tpl)
    tv = copy.deepcopy(nomap_v[tag])
    tv.update({"id_vinculo": f"VINC_B15_{idx:04d}", "id_referencia_interna": rid,
        "pmid_oficial": r["pmid_oficial"], "secao_origem": "B15_CANONICA_V2",
        "trecho_ancora": anchors[rid], "natureza_relacao": r["_nat"], "grau_maturidade": r["_mat"],
        "especie_mesh": r["especie_mesh"], "evid_role": r["evid_role"],
        "bloco_origem": "B15_CANONICA_V2", "uso": "B15_v2",
        "status_auditoria": "APROVADO",
        "segunda_verificacao": "P-6 pendente — 2ª verificação cega (Via 2) no fecho da rodada 16/16"})
    vinc.append(tv)

assert len(pmids) == len(vinc) == len(led) == 173
ids = [{x["id_referencia_interna"] for x in c} for c in (pmids, vinc, led)]
assert ids[0] == ids[1] == ids[2]
for rid, anc in anchors.items(): assert doc.count(anc) == 1
json.dump(pmids, open(PM, "w"), ensure_ascii=False, indent=1)
json.dump(vinc, open(VI, "w"), ensure_ascii=False, indent=1)
json.dump(led, open(LE, "w"), ensure_ascii=False, indent=1)

mf = json.load(open(MF))
mf["artefato_rotulo"] = "CANONICA v2"; mf["rodada"] = 4; mf["pmids_total"] = 173
mf["g2"] = {"eligible": 68, "redirecionado": 105}; mf["g3"] = {"vinculos_n2": 173}
mf["corte_literatura"] = "E-utilities/PubMed 2026-09-07 (rodada 0) + rodada [AT] 2026-09-09/10 (insumo externo GPM B15 auditado ref a ref)"
mf["historico_correcoes"].append({
  "data": "2026-09-09",
  "campo": "rodada [AT] GPM B15 — reconciliacao de insumo externo (P-7)",
  "correcao": "156 itens novos: 39 ENTRA (31 ancoras GPM + 8 secao 6 nucleo) · 87 BAIXO (leva N: ketamina/BDNF-suporte, HPA-B2, mito-B8, reviews NLRP3/contexto, metodologicos) · 28 EXC (CAMADA C: Alzheimer/Parkinson/autismo/fragil-X/dor) · 2 NAO-IDX mantidos",
  "acao_downstream": "V2 BLOCO_14/15; triade 173/173/173; matriz producao/insumos/matriz_b15_decisao.json"})
mf["historico_correcoes"].append({
  "data": "2026-09-09",
  "campo": "identidade de referencias",
  "correcao": "10 exposicoes: Pich&Millan=Cavalleri 2018 · Deyama print 2020 · Li-obesidade 2022 · Sun 2022 · Zhang-S6K1 2024 · Aguilar-Valles 2021 · Chandran 2013 · segundo Alcocer-Gomez 2017 (REF_ALCOCERGOMEZ_2017b) · Xu-2023a=T2DMxCUMS · aliases GPM<->V1 (Zhang-d=ZHANG_2023b; Li-2026a=LI_2026; Li-2025=LI_2025b)",
  "acao_downstream": "alias documentados; [G1] mantidos (TFEB humano, fluxo periferico, mTORC2, dorxdepressao, envelhecimento/sexo humano, pos-parto humano, Pich&Millan real, Choe/Liu-BNIP3L)"})
mf["pendencias_fase"] = ["P-6 avaliador cego (Fase 3 Fidelidade Canonica A/B/C/E) — AMPLIADA a toda a leva [AT] B15 2026-09-09 (39 refs novas; fecho rodada 16/16)"]
json.dump(mf, open(MF, "w"), ensure_ascii=False, indent=1)

json.dump({"mecanismo": "B15", "rodada": "[AT] 2026-09-09",
 "insumos": ["uploads/GPM_B15_Autofagia_mTOR (1).md", "uploads/BRIEFING_B15_AUTOFAGIA_MTOR_RODADA0 (1).md",
             "uploads/BRIEFING_B15_AUTOFAGIA_MTOR_RODADA0.md", "uploads/BRIENFING CONSOLIDADO _B15_v1.md",
             "uploads/Resumo do insumo para B15 chatgpt.md",
             "uploads/Artigos cientificos do mecanismo B15 autofagia mtor.md"],
 "triagem": {"universo_novos": 156, "ENTRA": 39, "BAIXO": 87, "EXC": 28, "nao_idx": 2,
             "matriz": "producao/insumos/matriz_b15_decisao.json"},
 "entra_por_grupo": {"ancoras_GPM_49": 31, "sec6_nucleo": 8},
 "exposicoes": 10,
 "totais_v2": {"refs": 173, "vinculos": 173, "auditorias": 173, "palavras": 9974},
 "arquivos_gerados": ["b15_gen_refs.py", "b15_refs_data.json", "b15_efetch_sel.json", "B15_md_apply.py",
                      "b15_ancoras.json", "B15_json_apply.py", "producao/historico/v1_canonica_2026-09-09.md",
                      "B15 AUTOFAGIA MTOR V2 CANONICA.md"],
 "data_fecho": "2026-09-10 (America/Sao_Paulo)"},
 open(f"{HERE}/producao/04_AT_ciclo_2026-09-09.json", "w"), ensure_ascii=False, indent=1)
print("tríade 173/173/173 + manifesto + trilha gravados")
