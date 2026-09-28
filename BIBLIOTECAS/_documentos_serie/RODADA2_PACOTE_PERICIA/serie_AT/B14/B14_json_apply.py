#!/usr/bin/env python3
# B14 — aplica tríade + manifesto + trilha (rodada [AT 2026-09-09])
import json, os, copy, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
refs = json.load(open(f"{HERE}/b14_refs_data.json"))
anchors = json.load(open(f"{HERE}/b14_ancoras.json"))
doc = open(f"{HERE}/B14 NEUROESTEROIDES V2 CANONICA.md", encoding="utf-8").read()

PM = f"{HERE}/Evidencias/Bibliografia/01_pmids.json"
VI = f"{HERE}/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
LE = f"{HERE}/Auditoria_B14/ledger_auditoria_B14.json"
MF = f"{HERE}/Evidencias/Bibliografia/_manifesto_biblioteca.json"

pmids = json.load(open(PM))
vinc = json.load(open(VI))
led = json.load(open(LE))

# templates por tag a partir de itens CONFIRMADOS da V1
tpl_ml = next(x for x in le if x["evid_role"] == "preclinical_mechanistic")
tpl_ec = next(x for x in le if x["evid_role"] == "human_clinical")
tpl_ob = next(x for x in le if x["evid_role"] == "review")
tpl_ml_v = next(x for x in vinc if x["evid_role"] == "preclinical_mechanistic")
tpl_ec_v = next(x for x in vinc if x["evid_role"] == "human_clinical")
tpl_ob_v = next(x for x in vinc if x["evid_role"] == "review")

n0 = len(pmids)
today = "2026-09-09"

new_ids, new_led, new_vin = [], [], []
for i, r in enumerate(refs):
    rid = r["id_referencia_interna"]
    tag = r["_tag"]; ml = r["evid_role"] == "preclinical_mechanistic"
    # ---- pmids.json (remove privados) ----
    pub = {k: v for k, v in r.items() if not k.startswith("_")}
    pub["id_referencia_interna"] = rid
    pub["g3_verificado_por"] = "IA G3 Rodada [AT] GPM B14 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente"
    new_ids.append(rid); pmids.append(pub)
    # ---- ledger ----
    tpl = copy.deepcopy(tpl_ml if ml else (tpl_ec if tag == "EC" else tpl_ob))
    idx = n0 + i + 1
    tpl.update({
        "id_auditoria": f"AUD_B14_{idx:04d}",
        "mecanismo": "B14",
        "id_referencia_interna": rid,
        "pmid_oficial": r["pmid_oficial"],
        "secao_origem": "B14_CANONICA_V2",
        "trecho_ancora": anchors[rid],
        "citacao_literal": f"{rid.replace('REF_','')}[{tag}]",
        "natureza_da_relacao": r["_nat"],
        "grau_maturidade_cientifica": r["_mat"],
        "forca_causal": r["_tier"],
        "forca_biologica_conexao": r["_forca"],
        "especie_mesh": r["especie_mesh"],
        "evid_role": r["evid_role"],
        "acao_correcao": r["_acao"],
        "origem_entrada": "GPM",
        "data_verificacao": today,
        "verificador": "IA G3 Rodada [AT] GPM B14 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
        "segunda_verificacao": "P-6 pendente — 2ª verificação cega (Via 2) a executar no fechamento da rodada 16/16",
        "status_auditoria": "CONFIRMADO",
    })
    new_led.append(tpl); led.append(tpl)
    # ---- vínculo ----
    tv = copy.deepcopy(tpl_ml_v if ml else (tpl_ec_v if tag == "EC" else tpl_ob_v))
    tv.update({
        "id_vinculo": f"VINC_B14_{idx:04d}",
        "id_referencia_interna": rid,
        "pmid_oficial": r["pmid_oficial"],
        "secao_origem": "B14_CANONICA_V2",
        "trecho_ancora": anchors[rid],
        "natureza_relacao": r["_nat"],
        "grau_maturidade": r["_mat"],
        "forca_causal": r["_tier"],
        "forca_biologica_conexao": r["_forca"],
        "especie_mesh": r["especie_mesh"],
        "evid_role": r["evid_role"],
        "bloco_origem": "B14_CANONICA_V2",
        "uso": "B14_v2",
        "status_auditoria": "CONFIRMADO",
        "data_verificacao": today,
        "segunda_verificacao": "P-6 pendente — 2ª verificação cega (Via 2) a executar no fechamento da rodada 16/16",
    })
    new_vin.append(tv); vinc.append(tv)

# ---- verificações cruzadas ----
assert len(pmids) == len(vinc) == len(led) == 290, (len(pmids), len(vinc), len(led))
ids_p = {x["id_referencia_interna"] for x in pmids}
ids_v = {x["id_referencia_interna"] for x in vinc}
ids_l = {x["id_referencia_interna"] for x in led}
assert ids_p == ids_v == ids_l, "tríade divergente"
for rid, anc in anchors.items():
    assert doc.count(anc) == 1, f"âncora fora da V2: {rid}"

json.dump(pmids, open(PM, "w"), ensure_ascii=False, indent=1)
json.dump(vinc, open(VI, "w"), ensure_ascii=False, indent=1)
json.dump(led, open(LE, "w"), ensure_ascii=False, indent=1)

# ---- manifesto ----
mf = json.load(open(MF))
mf["artefato_rotulo"] = "CANONICA v2"
mf["rodada"] = 4
mf["pmids_total"] = 290
mf["g2"] = {"eligible": 248, "redirecionado": 42}
mf["g3"] = {"vinculos_n2": 290}
mf["corte_literatura"] = "E-utilities/PubMed 2026-09-07 (rodada 0) + rodada [AT] 2026-09-09/10 (insumo externo GPM B14 auditado ref a ref)"
mf["historico_correcoes"].append({
    "data": "2026-09-09",
    "campo": "rodada [AT] GPM B14 — reconciliacao de insumo externo (P-7)",
    "correcao": "102 itens novos triados ref a ref: 50 ENTRA (26 das 57 ancoras do GPM + 24 da secao 6) · 44 BAIXO (34 HPA-genericos/B2, 7 conduta menopausal/THR-guidelines, 3 redundancia/GABA-B5/substancia) · 7 EXC (etanol x2, tiques, anestesia, Alzheimer-depressao, esquizofrenia, bibliometria) · 1 ja vigente (van Broekhoven 2003)",
    "acao_downstream": "V2 com BLOCO_14/15; triade 290/290/290; decisoes em producao/insumos/matriz_b14_decisao.json"})
mf["historico_correcoes"].append({
    "data": "2026-09-09",
    "campo": "identidade de referencias rotuladas pelo insumo",
    "correcao": "10 exposicoes: 'Stefaniak 2023'=Stoffel-Wagner 2003 · 'Luscher 2023'=MacKenzie & Maguire 2013 · 'Matthew 2013'=Meltzer-Brody & Kanes 2020 (era 'nao localizada' no sec.4) · 'Schiller 2016'=Schweizer-Schubert 2021 · 'Locci & Pinna 2017'=Lozza-Fiacco 2022 · 'Stumper 2026'=Sundstrom-Poromaa 2020 · 'Jain 2005'=Jaric 2019 · 'Franco 2016'=Gadek-Michalska 2013 · 'Vaudry 2022'=Von Werne Baes 2012 · 'Riebel 2024'=Rodriguez-Cerdeira 2026 (ja vigente; Riebel real=REF_RIEBEL_2025 vigente)",
    "acao_downstream": "aliases documentados; [G1] honestos mantidos (Stefaniak/Schiller/Stumper/Jain/Matthew-Samba reais, DHEA-homens, estrogenioxAD, contracepcao, Parikh NAO-IDX)"})
mf["pendencias_fase"] = ["P-6 avaliador cego (Fase 3 Fidelidade Canonica A/B/C/E) — AMPLIADA a toda a leva [AT] B14 2026-09-09 (50 refs novas; rodada 16/16)"]
json.dump(mf, open(MF, "w"), ensure_ascii=False, indent=1)

# ---- trilha ----
trilha = {
 "mecanismo": "B14",
 "rodada": "[AT] 2026-09-09",
 "insumos": ["uploads/GPM_B14_Neuroesteroides (1).md",
             "uploads/BRIEFING_B14_NEUROESTEROIDES_RODADA0 (1).md",
             "uploads/BRIEFING_B14_NEUROESTEROIDES_RODADA0.md",
             "uploads/BRIEFING_CONSOLIDADO_B14_v1.md",
             "uploads/Resumo do insumo para B14 chatgpt.md",
             "uploads/Artigos cientificos do mecanismo B14 neuroesteroides hormonios.md"],
 "triagem": {"universo_novos": 102, "ENTRA": 50, "BAIXO": 44, "EXC": 7, "ja_vigente": 1,
             "matriz": "producao/insumos/matriz_b14_decisao.json"},
 "entra_por_grupo": {"ancoras_GPM_57": 26, "sec6_107": 24},
 "exposicoes": 10,
 "totais_v2": {"refs": 290, "vinculos": 290, "auditorias": 290, "palavras": 11979},
 "arquivos_gerados": ["b14_gen_refs.py", "b14_refs_data.json", "b14_efetch_sel.json",
                      "B14_md_apply.py", "b14_ancoras.json", "B14_json_apply.py",
                      "producao/historico/v1_canonica_2026-09-09.md",
                      "B14 NEUROESTEROIDES V2 CANONICA.md"],
 "data_fecho": "2026-09-10 (America/Sao_Paulo)",
}
json.dump(trilha, open(f"{HERE}/producao/04_AT_ciclo_2026-09-09.json", "w"), ensure_ascii=False, indent=1)
print("tríade 290/290/290 gravada | manifesto v2 rodada 4 | trilha OK")
print("novos:", len(new_ids), "| exemplos:", new_ids[:3], "…", new_ids[-2:])
