#!/usr/bin/env python3
# B16 — rodada [AT 2026-09-09]: tríade +2, manifesto, trilha, matriz de decisão
import json, copy, re, os

BASE = "/home/user/BIBLIOTECAS/B16_Neurogenese"
V2 = open(os.path.join(BASE, "B16 NEUROGENESE V2 CANONICA.md"), encoding="utf-8").read()

def italica(tag):
    hits = [ln for ln in V2.splitlines() if ln.startswith("*") and ln.endswith("*") and tag in ln]
    assert len(hits) == 1, (tag, hits)
    return hits[0]

LISTRA_12 = italica("DOLUDDA_2026[OB]")
LISTRA_112 = italica("ZHOU_2025[ML]")
assert LISTRA_12.startswith("*ERIKSSON_1998") and LISTRA_112.startswith("*KUHN_1996"), (LISTRA_12[:40], LISTRA_112[:40])

# ---------- 1. pmids.json ----------
P = os.path.join(BASE, "Evidencias/Bibliografia/01_pmids.json")
refs = json.load(open(P))
isdict = isinstance(refs, dict)
lst = refs.get("referencias", refs) if isdict else refs
tk = [r for r in lst if r["id_referencia_interna"] == "REF_KEMPERMANN_2018"][0]
tx = [r for r in lst if r["id_referencia_interna"] == "REF_XIE_2025"][0]
assert all(r["pmid_oficial"] not in ("41795427", "40681842") for r in lst)

dol = copy.deepcopy(tk)
dol.update({
 "pmid_oficial": "41795427",
 "titulo_artigo": "Adult neurogenesis: New neurons, new opportunities",
 "autores": ["Doludda B","Barde W","D'Egidio F","Fitzsimons CP","Frisén J","Gage FH","Jessberger S","Lazarov O","Lie DC","Lucassen PJ","de Lucia C","Salta E","Song H","Song J","Thuret S","Toda T","Kempermann G"],
 "revista_ano": "Cell stem cell (2026)",
 "achado_central_molecular": "CONSENSO de 17 líderes do campo (2026): NG adulta como processo estabelecido na função hipocampal em saúde e doença; perguntas de fronteira abertas (identidade das células-tronco, nicho, NG sem célula-tronco, função além do hipocampo); dezenas de ensaios com a palavra-chave = sinal de interesse, não validação [consenso/revisão-teto (2026)]",
 "ids_referencia_interna": ["REF_DOLUDDA_2026"],
 "id_referencia_interna": "REF_DOLUDDA_2026",
 "doi": "10.1016/j.stem.2026.01.014",
 "g1_resumo": "eutils (rodada [AT 2026-09-09]; anexo DOI + matriz externa Tier; 2026; abstract lido)",
 "g3_verificado_por": "IA G3 (esummary + abstract efetch lido 2026-09-09; autor+ano+periódico+tema conferidos); P-6 avaliador cego pendente",
 "origem_pipeline": "RODADA_AT_2026-09-09",
 "_aliases": ["Doludda", "DOLUDDA", "consenso 2026"],
})
zho = copy.deepcopy(tx)
zho.update({
 "pmid_oficial": "40681842",
 "titulo_artigo": "Adult hippocampal neurogenesis-mediated cognitive behavior participates in stress resilience to anxiety and depression-like behaviors in postpartum dams",
 "autores": ["Zhou L","Wu Z","Li Y","Xie Y","Sun L","Lin S","Xiao L","Wang H","Wang G"],
 "revista_ano": "Molecular psychiatry (2025)",
 "achado_central_molecular": "Separação breve de filhotes → resiliência pós-parto ao estresse crônico em fêmeas lactantes (↑NG, ↓microglia/NLRP3-IL-1β); comportamento COGNITIVO mediado por AHN participa da resiliência a ansiedade/depressão pós-parto [animal/pós-parto (2025)]",
 "ids_referencia_interna": ["REF_ZHOU_2025"],
 "id_referencia_interna": "REF_ZHOU_2025",
 "doi": "10.1038/s41380-025-03082-1",
 "g1_resumo": "eutils (rodada [AT 2026-09-09]; anexo DOI + matriz externa Tier; 2025; abstract lido)",
 "g3_verificado_por": "IA G3 (esummary + abstract efetch lido 2026-09-09; autor+ano+periódico+tema conferidos); P-6 avaliador cego pendente",
 "origem_pipeline": "RODADA_AT_2026-09-09",
 "_aliases": ["Zhou", "ZHOU", "Zhou pós-parto 2025"],
})
lst.extend([dol, zho])
json.dump(refs, open(P, "w"), ensure_ascii=False, indent=1)
print("pmids.json:", len(lst))

# ---------- 2. vínculos ----------
V = os.path.join(BASE, "Evidencias/Vinculos/vinculos_referencia_afirmacao.json")
v = json.load(open(V))
vidmax = max(int(x["id_vinculo"].rsplit("_", 1)[1]) for x in v)
vk = [x for x in v if x["id_referencia_interna"] == "REF_KEMPERMANN_2018"][0]
vx = [x for x in v if x["id_referencia_interna"] == "REF_XIE_2025"][0]
vd = copy.deepcopy(vk); vd.update({
 "id_vinculo": f"VINC_B16_{vidmax+1:04d}", "id_referencia_interna": "REF_DOLUDDA_2026",
 "pmid_oficial": "41795427", "trecho_ancora": LISTRA_12, "bloco_origem": "BLOCO_01",
 "uso": "B16_v2", "data_verificacao": "2026-09-09",
 "segunda_verificacao": "P-6 pendente — 2ª verificação cega (Via 2) no fecho da rodada 16/16"})
vz = copy.deepcopy(vx); vz.update({
 "id_vinculo": f"VINC_B16_{vidmax+2:04d}", "id_referencia_interna": "REF_ZHOU_2025",
 "pmid_oficial": "40681842", "trecho_ancora": LISTRA_112, "bloco_origem": "BLOCO_11",
 "uso": "B16_v2", "data_verificacao": "2026-09-09",
 "segunda_verificacao": "P-6 pendente — 2ª verificação cega (Via 2) no fecho da rodada 16/16"})
v.extend([vd, vz])
json.dump(v, open(V, "w"), ensure_ascii=False, indent=1)
print("vinculos:", len(v))

# ---------- 3. ledger ----------
L = os.path.join(BASE, "Auditoria_B16/ledger_auditoria_B16.json")
Lg = json.load(open(L))
amax = max(int(x["id_auditoria"].rsplit("_", 1)[1]) for x in Lg)
lk = [x for x in Lg if x["id_referencia_interna"] == "REF_KEMPERMANN_2018"][0]
lx = [x for x in Lg if x["id_referencia_interna"] == "REF_XIE_2025"][0]
ld = copy.deepcopy(lk); ld.update({
 "id_auditoria": f"AUD_B16_{amax+1:04d}", "id_referencia_interna": "REF_DOLUDDA_2026",
 "pmid_oficial": "41795427", "origem_entrada": "RODADA_AT",
 "trecho_ancora": LISTRA_12, "citacao_literal": "DOLUDDA_2026[TAG]",
 "verificacao": {
   "verificador": "IA G3 (rodada AT 2026-09-09) — B16; P-6 2a verificacao independente (avaliador cego) PENDENTE",
   "data_verificacao": "2026-09-09",
   "g1_metodo": "eutils_automatico (esearch+esummary+efetch)",
   "abstract_ou_trecho": "Abstract efetch lido na íntegra (2026-09-09): consenso de 17 líderes do campo; autor+ano+periódico conferidos via esummary",
   "query_utilizada": "esearch por DOI 10.1016/j.stem.2026.01.014[doi] + esummary + efetch",
   "g2_motivo": "humano/meta/revisao",
   "g3_nota": "abstract lido; consenso registrado como revisão-teto; 'nº de ensaios com a palavra-chave' tratado como sinal de interesse, não validação de alvo"}})
lz = copy.deepcopy(lx); lz.update({
 "id_auditoria": f"AUD_B16_{amax+2:04d}", "id_referencia_interna": "REF_ZHOU_2025",
 "pmid_oficial": "40681842", "origem_entrada": "RODADA_AT",
 "trecho_ancora": LISTRA_112, "citacao_literal": "ZHOU_2025[TAG]",
 "verificacao": {
   "verificador": "IA G3 (rodada AT 2026-09-09) — B16; P-6 2a verificacao independente (avaliador cego) PENDENTE",
   "data_verificacao": "2026-09-09",
   "g1_metodo": "eutils_automatico (esearch+esummary+efetch)",
   "abstract_ou_trecho": "Abstract efetch lido na íntegra (2026-09-09): PS15×CRS em fêmeas lactantes; modulação viral da AHN; eixo NLRP3/microglia",
   "query_utilizada": "esearch por DOI 10.1038/s41380-025-03082-1[doi] + esummary + efetch",
   "g2_motivo": "animal/mecanístico",
   "g3_nota": "abstract lido; nuance registrada — desfecho emocional via comportamento cognitivo mediado por AHN (não direto); [APENAS PRÉ-CLÍNICO] na prosa"}})
Lg.extend([ld, lz])
json.dump(Lg, open(L, "w"), ensure_ascii=False, indent=1)
print("ledger:", len(Lg))

# ---------- 4. manifesto ----------
M = os.path.join(BASE, "Evidencias/Bibliografia/_manifesto_biblioteca.json")
man = json.load(open(M))
man["versao"] = "v2"
man["artefato_rotulo"] = "B16 NEUROGENESE V2 CANONICA.md"
man["pmids_pos_rodada_at_2026_09_09"] = 290
man["rodada_at_2026_09_09"] = {
 "tipo": "auditoria ref a ref de todos os insumos com fusão dirigida",
 "universo_numerico_8d": 285, "vigentes": 283,
 "entra": 2, "entra_refs": ["REF_DOLUDDA_2026", "REF_ZHOU_2025"],
 "entra_motivo": "falha silenciosa da fusão da rodada 0 — demandadas por anexo+matriz; G1 eutils + abstracts lidos",
 "off_scope_oficial": {"Siopi 2016 (J Neurosci)": "26758842 — decisão explícita do próprio insumo (ZSV/bulbo olfatório); mantido fora"},
 "corte_literatura": "2026-09-07 (inalterado — a rodada não rebuscou literatura nova além das 2 âncoras demandadas)",
 "total_final": 290}
man["identificadores_falsos_expostos_at"] = {
 "fragmentos_doi": {"20001002": "Palmer 2000 (J Comp Neurol) — obra real; contexto fora da canônica",
                    "00207454": "Fares 2018 (Int J Neurosci) — obra real; fora por redundância (rodada 0)"},
 "nao_resolvem_pubmed": {"40727497": "\"Allen 2025\" (matriz externa) — esummary inexistente",
                         "39024461": "\"Zhou 2024\" (matriz externa) — esummary inexistente"}}
man["exclusoes_matriz_ratificadas_at"] = [
 "Zhang 2017 APP/PS1 (malha EXC/Alzheimer — contexto apenas)",
 "Nejad 2024 (morfina — fora do arco ansiedade/depressão)",
 "Li 2024 (plasticidade geral — domínio B3)",
 "W. 2025 (venue baixa relevância; duplicidade B15/B16)",
 "Yang 2025 / Wang 2025 (anais não indexados — nota sem citação formal)"]
man["duplicata_anexo_resolvida_at"] = "Jones/Zhou/Jhaveri 2022 ×2 consecutivas → REF_JONES_2022 única (35842419)"
man["aliases_ano_resolvidos_doi_at"] = {
 "Gage '2024'": "REF_GAGE_2025 (39648699)", "Zhang IL-4 '2020'": "REF_ZHANG_2021 (33731342)",
 "Elliott '2024'": "REF_ELLIOTT_2025 (39558003)", "Simard '2023'": "pré-print bioRxiv de REF_SIMARD_2024 (39414359)"}
man["historico_rodadas"] = man.get("historico_rodadas", []) + [{
 "data": "2026-09-09", "rodada": "[AT] auditoria externa",
 "placar": "288 → 290", "entra": 2, "falsos_expostos": 4, "off_scope_oficial": 1,
 "portoes": "gate/framework/checklist reexecutados (ver RELATORIO_EXECUCAO_B16_AT_2026-09-09.md)"}]
man["pendencias_fase"] = ["P-6 Via 2 — 2ª verificação cega atravessando todas as levas [AT] B1–B16 no fecho 16/16 (inclui REF_DOLUDDA_2026 e REF_ZHOU_2025)"]
json.dump(man, open(M, "w"), ensure_ascii=False, indent=1)
print("manifesto atualizado")

# ---------- 5. trilha ----------
T = os.path.join(BASE, "producao/04_AT_ciclo_2026-09-09.json")
json.dump({
 "biblioteca": "B16", "rodada": "[AT] 2026-09-09", "tipo": "auditoria_externa_com_fusao_dirigida",
 "insumos": ["GPM_B16 (298 âncoras; M00–M10)", "RODADA0 (283 identificadores 8d)", "briefing consolidado (14)",
             "matriz externa 17 seções", "anexo bibliográfico por DOI", "síntese cruzada"],
 "placar": {"antes": 288, "depois": 290, "entra": 2, "baixo": 0, "exc_novos": 0,
            "vigentes_confirmados": 283, "falsos_ids_expostos": 4, "off_scope_oficial": 1, "duplicata_colapsada": 1},
 "entra": [{"ref": "REF_DOLUDDA_2026", "pmid": "41795427", "papel": "consenso 2026 — revisão-teto [OB]",
            "g1": "esearch DOI→41795427; esummary; efetch abstract lido"},
           {"ref": "REF_ZHOU_2025", "pmid": "40681842", "papel": "resiliência pós-parto [ML]",
            "g1": "esearch DOI→40681842; esummary; efetch abstract lido"}],
 "exposicoes": ["fragmentos DOI 20001002/00207454 lidos como PMID", "40727497/39024461 não resolvem (matriz externa)"],
 "portoes": "reexecutados pós-fusão (gate, framework, checklist)",
 "pendencias": ["P-6 Via 2 no fecho 16/16"]},
 open(T, "w"), ensure_ascii=False, indent=1)
print("trilha gravada")

# ---------- 6. matriz de decisão ----------
os.makedirs(os.path.join(BASE, "producao/insumos"), exist_ok=True)
json.dump({
 "biblioteca": "B16", "data": "2026-09-09",
 "universo": {"numerico_8d": 285, "doi_only_detectados_na_checagem_autor_ano": 2},
 "decisao": {"ENTRA": 2, "VIGENTE": 283, "OFF_SCOPE_OFICIAL": 1, "FALSO_ID": 4, "DUPLICATA": 1,
             "EXC_RATIFICADAS_MATRIZ": 6, "NAO_INDEXADOS_G1_NOTA": 2},
 "entra": {"REF_DOLUDDA_2026": "41795427", "REF_ZHOU_2025": "40681842"},
 "falsos": {"20001002": "fragmento DOI Palmer 2000", "00207454": "fragmento DOI Fares 2018",
            "40727497": "N/A PubMed (\"Allen 2025\")", "39024461": "N/A PubMed (\"Zhou 2024\")"},
 "numeros_computados": True},
 open(os.path.join(BASE, "producao/insumos/matriz_b16_decisao.json"), "w"), ensure_ascii=False, indent=1)
print("matriz gravada")
