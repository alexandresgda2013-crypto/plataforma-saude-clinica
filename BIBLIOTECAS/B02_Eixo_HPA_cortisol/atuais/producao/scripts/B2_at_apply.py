#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P-7 [AT] B2 — Etapa 3: grava os 28 entrantes (01_pmids, vínculos N2, ledger, manifesto)."""
import json, re, unicodedata
from pathlib import Path

B2 = Path("/home/user/BIBLIOTECAS/B02_Eixo_HPA_cortisol")
BIBDIR = B2 / "Evidencias" / "Bibliografia"
FINAL = json.load(open(B2 / "producao" / "insumos" / "matriz_b2_at_final.json"))["entrantes"]
V2 = (B2 / "B2 EIXO HPA CORTISOL V2 CANONICA.md").read_text(encoding="utf-8")

def asc(s): return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))

# pmid -> (ID, label, tag, role, secao, claim, achado, g3, g2)
CFG = {
 "15996533": ("REF_SWAAB_2005","SWAAB_2005","OB","review","BLOCO_06/6.17","B2.MEC.BLOCO06.017","Sistema de estresse cerebral humano em depressão/neurodegeneração: alterações focais CRH/PVN, não hiperatividade uniforme","Revisão Swaab Nature Rev Neurosci; sustenta heterogeneidade central.","revisão; elegível"),
 "28183380": ("REF_VONWERNEBAES_2012","VONWERNEBAES_2012","OB","review","BLOCO_06/6.17","B2.MEC.BLOCO06.017","Avaliação da atividade HPA (grandezas GR/MR) e estresse precoce — revisão","Revisão de métodos de avaliação HPA.","revisão; elegível"),
 "32203965": ("REF_CERUSO_2020","CERUSO_2020","OB","review","BLOCO_06/6.17","B2.MEC.BLOCO06.017","Alterações HPA em TDM com/sem estresse precoce (revisão sistemática)","Rev sist; subgrupos por adversidade.","revisão sistemática; elegível"),
 "36458076": ("REF_SAHU_2022","SAHU_2022","OB","review","BLOCO_06/6.17","B2.MEC.BLOCO06.017","Cortisol sérico/plasmático no TDM: revisão/meta — heterogeneidade","Cortisol periférico com alta variância.","revisão/meta; elegível"),
 "41270487": ("REF_MACHAHARY_2025","MACHAHARY_2025","MA","review","BLOCO_06/6.17","B2.MEC.BLOCO06.017","Hormônios endógenos x fenótipos do TDM (meta)","Meta; associações fenótipo-específicas.","meta-análise; elegível"),
 "23410758": ("REF_JARCHO_2013","JARCHO_2013","EC","human_clinical","BLOCO_06/6.17","B2.MEC.BLOCO06.017","Ritmo diurno desregulado associado a resistência glicocorticoide","Humano; elo ritmo->resistência GR.","humano; elegível"),
 "40040865": ("REF_VANDENNOORGATE_2025","VANDENNOORGATE_2025","OB","review","BLOCO_08/8.1","B2.MEC.BLOCO08.001","Meta crosstalk imune-neuroendócrino em transtornos do humor/psicóticos","Bidirecionalidade meta-analisada; trava B1<->B2.","revisão/meta; elegível ponte B1"),
 "20047716": ("REF_ZOBEL_2010","ZOBEL_2010","EC","human_clinical","BLOCO_04/4.3","B2.MEC.BLOCO04.003","Variantes FKBP5 associadas a depressão unipolar","Associação genética humana.","humano caso-controle; elegível"),
 "20393453": ("REF_XIE_2010","XIE_2010","EC","human_clinical","BLOCO_04/4.3","B2.MEC.BLOCO04.003","FKBP5 x adversidade infantil -> risco de TEPT","G x E humano.","humano; elegível"),
 "21865530": ("REF_ZIMMERMANN_2011","ZIMMERMANN_2011","EC","human_clinical","BLOCO_04/4.3","B2.MEC.BLOCO04.003","Coorte 10 anos (n=884): FKBP5 x eventos traumáticos -> incidência TDM","Prospectiva; lastro temporal G x E.","humano prospectivo; elegível"),
 "29182159": ("REF_TOZZI_2018","TOZZI_2018","EC","human_clinical","BLOCO_04/4.4","B2.MEC.BLOCO04.004","Epigenética FKBP5 liga risco genético+ambiental a alterações cerebrais no TDM","Metilação+imagem humano.","humano; elegível"),
 "28850857": ("REF_WANG_2018","WANG_2018","MA","review","BLOCO_04/4.3","B2.MEC.BLOCO04.003","Meta 14 estudos/15.109: FKBP5 x trauma precoce -> TDM/TEPT","Meta com ressalvas de heterogeneidade.","meta-análise; elegível"),
 "41849885": ("REF_KAUL_2026","KAUL_2026","EC","human_clinical","BLOCO_04/4.4","B2.MEC.BLOCO04.004","Variantes de splicing FKBP5 alteradas no córtex humano em transtornos psiquiátricos","[fronteira 2026] tecido humano.","humano pós-morte; elegível fronteira"),
 "40578604": ("REF_ZHANG_2025","ZHANG_2025","ML","preclinical_mechanistic","BLOCO_04/4.3","B2.MEC.BLOCO04.003","FKBP5 KO prejudica LTD-NMDAR via calcineurina: mecanismo de resiliência","[APENAS PRÉ-CLÍNICO] camundongo.","modelo animal; elegível mecanismo"),
 "37078436": ("REF_STANTON_2023","STANTON_2023","OB","review","BLOCO_02/2.12","B2.MEC.BLOCO02.012","Neurônios PVN-CRH: contribuições sinápticas à psicopatologia do estresse","Reavaliação da função sináptica PVN-CRH.","revisão; elegível"),
 "41935803": ("REF_ZHENG_2026","ZHENG_2026","OB","review","BLOCO_02/2.12","B2.MEC.BLOCO02.012","Circuitos sinápticos PVN(CRH) além do HPA: defesa/recompensa/sono/autonomia","[fronteira 2026] mapa de circuitos.","revisão; elegível fronteira"),
 "34901719": ("REF_SUKHAREVA_2021","SUKHAREVA_2021","OB","review","BLOCO_02/2.12","B2.MEC.BLOCO02.012","CRH e receptores na regulação da resposta ao estresse (revisão)","Base CRH/receptores.","revisão; elegível"),
 "19008333": ("REF_SPIGA_2009","SPIGA_2009","ML","preclinical_mechanistic","BLOCO_06/6.14","B2.MEC.BLOCO06.014","Bloqueio V1B reduz ACTH ao estresse sem alterar basal; corticosterona não reduz","[APENAS PRÉ-CLÍNICO] roedor; alvo investigacional.","animal; elegível mecanismo"),
 "34566653": ("REF_DING_2021","DING_2021","MA","review","BLOCO_06/6.15","B2.MEC.BLOCO06.015","Meta de tratamentos HPA no TDM: sinal favorável, efeito global pequeno","Meta Ding 2021 (rótulo do insumo sem autor, corrigido).","meta-análise; elegível sonda P20"),
 "26563991": ("REF_STALDER_2016","STALDER_2016","OB","review","BLOCO_05/CAR","B2.MEC.BLOCO05.001","Guideline consensual do CAR: protocolo e variáveis","Consenso internacional CAR.","consenso; elegível metrologia"),
 "38308964": ("REF_WESARGMENZEL_2024","WESARGMENZEL_2024","MA","review","BLOCO_05/CAR","B2.MEC.BLOCO05.001","Meta 12 estudos: diurno (AUC/slope/CAR) SEM associação global com reatividade aguda","[NEG] prova de não-intercambiabilidade.","meta-análise; elegível calibrador"),
 "32276241": ("REF_SUGAYA_2020","SUGAYA_2020","EC","human_clinical","BLOCO_05/cabelo","B2.MEC.BLOCO05.002","Validação 30 dias: cabelo x cortisol salivar integrado; não x CAR/slope","Estudo de validação n=24.","humano validação; elegível metrologia"),
 "42009273": ("REF_BALFOUR_2026","BALFOUR_2026","MA","review","BLOCO_04/4.4","B2.MEC.BLOCO04.004","Meta 39 estudos metilação x resposta de cortisol: misto; só lactentes; certeza baixa","[downgrade] anti-entusiasmo epigenético.","meta-análise; elegível calibrador"),
 "36624454": ("REF_SUN_2023","SUN_2023","ML","preclinical_mechanistic","BLOCO_06/6.14","B2.MEC.BLOCO06.014","Antagonista CRHR1 alivia depressão-tipo em modelo LPS (camundongo)","[APENAS PRÉ-CLÍNICO] elo imune->CRH.","animal; elegível mecanismo"),
 "19545546": ("REF_TATRO_2009","TATRO_2009","ML","preclinical_mechanistic","BLOCO_02/2.3","B2.MEC.BLOCO02.003","FKBP51/FKBP52 modulam translocação nuclear do GR em neurônios","[APENAS PRÉ-CLÍNICO] célula neuronal.","célula; elegível mecanismo"),
 "34920399": ("REF_ZAJKOWSKA_2022","ZAJKOWSKA_2022","MA","review","BLOCO_06/6.17","B2.MEC.BLOCO06.017","Meta: cortisol e desenvolvimento de depressão em adolescência/adulto jovem","Meta prognóstica juvenil.","meta-análise; elegível desenvolvimento"),
 "31499391": ("REF_LOMBARDO_2019","LOMBARDO_2019","MA","review","BLOCO_06/6.15","B2.MEC.BLOCO06.015","Cortisol basal x eficácia antiglicocorticoide: só prediz resposta em inibidores de síntese","Meta; precisão fenotípica.","meta-análise; elegível sonda P20"),
 "11089561": ("REF_MULLER_2000","MULLER_2000","ML","preclinical_mechanistic","BLOCO_06/6.14","B2.MEC.BLOCO06.014","CRHR1-deficiente: ativação seletiva do sistema vasopressinérgico (camundongo)","[APENAS PRÉ-CLÍNICO] duplicata Ller/Müller mesclada a 1 entrada.","animal; elegível mecanismo"),
}
assert len(CFG) == 28
E = {v["pmid_final"]: v for v in FINAL.values()}
assert all(pm in E for pm in CFG), [pm for pm in CFG if pm not in E]

def revista_ano(v): return f"{v.get('journal','').strip()} {v.get('ano','')}".strip()
def surname(v): return (v.get("autores") or ["?"])[0].split()[0]

p01 = json.load(open(BIBDIR/"01_pmids.json"))
p01 = [r for r in p01 if r.get("pmid_oficial") not in CFG]
novos = []
for pm,(rid,label,tag,role,sec,claim,achado,g3,g2) in CFG.items():
    v = E[pm]
    novos.append({
      "pmid_oficial": pm, "titulo_artigo": v.get("titulo",""), "autores": v.get("autores",[])[:8],
      "revista_ano": revista_ano(v), "desenho_estudo": "; ".join(v.get("pubtypes",[])[:3]),
      "secao_origem": f"mecanismo_B2_EixoHPA/{sec.split('/')[0]}", "achado_central_molecular": achado,
      "extrapolacao_por_analogia": ("sim (animal/célula; humano indireto)" if tag=="ML" else "nao"),
      "ids_referencia_interna": [rid], "evid_role": role,
      "especie_mesh": v.get("species",[]), "verification_status": "verificado",
      "citacao_confirmada": True, "g1_metodo": "eutils_automatico",
      "g3_verificado_por": "IA_revisora_G3 (mini-rodada [AT] 2026-09-08; aguarda revisao de pares humana — P-6 pendente)",
      "status_auditoria": "", "origem_pipeline": "ATUALIZACAO_AT_2026-09-08 (insumo externo auditado)",
      "g2_elegibilidade": "eligible", "g2_motivo": g2,
      "id_referencia_interna": rid, "doi": v.get("doi",""), "claim_id_origem": claim,
      "_aliases": [surname(v), asc(surname(v)).upper(), asc(surname(v))],
    })
p01 += novos
json.dump(p01, open(BIBDIR/"01_pmids.json","w"), ensure_ascii=False, indent=1)

# trilha P-7 em producao/ (Módulo 09 mantém identidade única)
at = [{"at_ciclo":"AT-2026-09-08-B2","at_fluxo":"P-7: CANDIDATO->G1/G2/G3->APROVADO->V2",
       "at_status":"INCORPORADO_V2","at_data":"2026-09-08","pmid_oficial":r["pmid_oficial"],
       "id_referencia_interna":r["id_referencia_interna"],"titulo_artigo":r["titulo_artigo"],
       "revista_ano":r["revista_ano"],"g1_metodo":"eutils_automatico","citacao_confirmada":True} for r in novos]
at.append({"at_ciclo":"AT-2026-09-08-B2","at_status":"REJEITADOS_REGISTRO","at_data":"2026-09-08",
  "itens":[{"item":"21 itens só (Autor, Ano)","motivo":"[G1: a cravar] — sem identificador verificável (inclui Peng 2018 incompleto; Klinger-König/Ising/Khoury/Klengel já tinham equivalente na B2)"},
           {"item":"Müller/Ller 2000 duplicata","motivo":"mesmo DOI — mantida 1 entrada (PMID 11089561)"},
           {"item":"34566653 sem autor no rótulo","motivo":"corrigido: Ding Y 2021"}]})
json.dump(at, open(B2/"producao"/"04_AT_ciclo_2026-09-08.json","w"), ensure_ascii=False, indent=1)

# ---------------- vínculos ----------------
vinc = [v for v in json.load(open(B2/"Evidencias"/"Vinculos"/"vinculos_referencia_afirmacao.json"))]
IDS = {c[0] for c in CFG.values()}
vinc = [v for v in vinc if v.get("id_referencia_interna") not in IDS]
n0 = len(vinc)
TRECHO = {
 "15996533":"(Swaab 2005)[OB]",
 "28183380":"(Von Werne Baes 2012)[OB]",
 "32203965":"(Ceruso 2020)[OB]",
 "36458076":"(Sahu 2022)[OB]",
 "41270487":"(Machahary 2025)[MA]",
 "23410758":"associa-se à **resistência ao glicocorticoide** (Jarcho 2013)[EC]",
 "40040865":"(Van Den Noortgate 2025)[OB]",
 "20047716":"(Zobel 2010)[EC]; a adversidade infantil modula o",
 "20393453":"a adversidade infantil modula o\n  risco de TEPT (Xie 2010)[EC]",
 "21865530":"(Zimmermann 2011)[EC]",
 "29182159":"(Tozzi 2018)[EC]",
 "28850857":"ressalvas de heterogeneidade (Wang 2018)[MA]. Leitura canônica:",
 "41849885":"(Kaul 2026)[EC; fronteira]",
 "40578604":"(Zhang S 2025)[ML] [APENAS PRÉ-CLÍNICO]",
 "37078436":"(Stanton 2023)[OB]",
 "41935803":"(Zheng 2026)[OB; fronteira]",
 "34901719":"(Sukhareva 2021)[OB]",
 "19008333":"(Spiga 2009)[ML; roedor] [APENAS PRÉ-CLÍNICO]",
 "34566653":"(Ding 2021)[MA]",
 "26563991":"(Stalder 2016)[OB; consenso de especialistas]",
 "38308964":"medida diurna **não** substitui desafio (Wesarg-Menzel 2024)[MA] [NEG]",
 "32276241":"(Sugaya 2020)[EC; validação]",
 "42009273":"gene-candidato (Balfour 2026)[MA]",
 "36624454":"(Sun 2023)[ML; camundongo] [APENAS PRÉ-CLÍNICO]",
 "19545546":"(Tatro 2009)[ML; neurônios] [APENAS PRÉ-CLÍNICO]",
 "34920399":"(Zajkowska 2022)[MA]",
 "31499391":"(Lombardo 2019)[MA]",
 "11089561":None,  # Müller sem menção de prosa (trilha apêndice/vínculo index)
}
falt=[]
for pm,t in TRECHO.items():
    if t is not None and t not in V2: falt.append(pm)
if falt: print("TRECHOS NÃO ENCONTRADOS:",falt); raise SystemExit(1)

for i,(pm,(rid,label,tag,role,sec,claim,achado,g3,g2)) in enumerate(CFG.items(),1):
    v = E[pm]
    trecho = TRECHO[pm] or f"Entrada índice [AT] 2026-09-08: {label}[{tag}] — registra a duplicata Ller/Müller mesclada (mesmo DOI), verificada por eutils; sem menção de prosa adicional."
    vinc.append({
      "id_vinculo": f"VINC_B2_{n0+i:04d}", "id_referencia_interna": rid, "claim_id": claim,
      "mecanismo_origem": "B2", "secao_origem": sec, "trecho_ancora": trecho,
      "achado_central_molecular": achado,
      "natureza_relacao": "causal" if role=="preclinical_mechanistic" else "contributiva",
      "grau_maturidade": "bem_suportado" if tag in ("MA","ML") else "moderadamente_suportado",
      "forca_causal": "tier_4_descritivo_estrutural",
      "extrapolacao_por_analogia": ("sim (animal/célula; humano indireto)" if tag=="ML" else "nao"),
      "evid_role": role, "uso": "contexto_mecanistico",
      "status_referencia": "VALIDADO_G3_IA", "status_auditoria": "CONFIRMADO",
      "verification_status": "verificado", "data_verificacao": "2026-09-08",
      "g2_elegibilidade": "eligible", "g2_motivo": g2, "g1_metodo": "eutils_automatico",
      "g3_verificado_por": "IA_revisora_G3 (mini-rodada [AT] 2026-09-08; aguarda revisao de pares humana — P-6 pendente)",
      "pmid_oficial": pm, "g3_notas": g3,
    })
json.dump(vinc, open(B2/"Evidencias"/"Vinculos"/"vinculos_referencia_afirmacao.json","w"), ensure_ascii=False, indent=1)

# ---------------- ledger ----------------
led = [e for e in json.load(open(B2/"Auditoria_B2"/"ledger_auditoria_B2.json")) if e.get("id_referencia_interna") not in IDS]
l0 = len(led)
linhas = [l for l in V2.splitlines() if l.startswith("*") and l.endswith("*")]
novas = [l for l in linhas if "SWAAB_2005" in l or "STANTON_2023" in l]
assert len(novas)==2, (len(novas))
linhaA, linhaB = novas
for i,(pm,(rid,label,tag,role,sec,claim,achado,g3,g2)) in enumerate(CFG.items(),1):
    v = E[pm]
    led.append({
      "id_auditoria": f"AUD_B2_{l0+i:04d}", "mecanismo": "B2", "id_referencia_interna": rid,
      "pmid_oficial": pm, "arquivo_modulo09": "Evidencias/Bibliografia/01_pmids.json",
      "tipo_classificador": "", "origem_entrada": "POLITICA_FONTES", "claim_id": claim,
      "secao_origem": sec,
      "trecho_ancora": linhaA if f"| {label}[" in linhaA else linhaB,
      "citacao_literal": f"{label}[TAG]", "natureza_da_relacao": "causal" if role=="preclinical_mechanistic" else "contributiva",
      "grau_maturidade_cientifica": "bem_suportado" if tag in ("MA","ML") else "moderadamente_suportado",
      "forca_causal": "tier_4_descritivo_estrutural", "forca_biologica_conexao": "",
      "especie_mesh": v.get("species",[]), "evid_role": role,
      "portao_G1_existencia": "VERIFIED_REFERENCE", "portao_G2_elegibilidade": "ELIGIBLE_SOURCE",
      "portao_G3_suporte": "APROVADO", "status_auditoria": "APROVADO",
      "destino": "FICA_MECANISMO", "acao_correcao": "MANTER", "reconciliado": True,
      "verificacao": {
        "verificador": "IA G3 (geração) — B2 [AT 2026-09-08]; P-6 2a verificacao independente (avaliador cego) PENDENTE",
        "data_verificacao": "2026-09-08",
        "g1_metodo": "eutils_automatico (esearch+esummary+efetch)",
        "abstract_ou_trecho": (v.get("abstract") or v.get("titulo",""))[:400],
        "query_utilizada": "verificação direta de PMID do insumo externo via eutils",
        "g2_motivo": g2, "g3_nota": g3,
      },
    })
json.dump(led, open(B2/"Auditoria_B2"/"ledger_auditoria_B2.json","w"), ensure_ascii=False, indent=1)

man = json.load(open(BIBDIR/"_manifesto_biblioteca.json"))
man.setdefault("atualizacoes_pos_publicacao", []).append({
  "tipo":"[AT] P-7","data":"2026-09-08","versao_gerada":"CANÔNICA v2",
  "descricao":"Insumo externo 'matriz canônica B2' auditado ref-a-ref (35/35 resolvidos; 0 falsos positivos; 7 já cobertos; 21 sem identificador [G1: a cravar]); 28 referências verificadas incorporadas (185 -> 213).",
  "origem_insumo":"producao/insumos/RELATORIO_AUDITORIA_MATRIZ_B2.md",
  "refs_adicionadas":28,"refs_totais":len(p01),
  "pendencias":"P-6 (2a verificação cega) permanece pendente, incluindo a leva [AT]."})
json.dump(man, open(BIBDIR/"_manifesto_biblioteca.json","w"), ensure_ascii=False, indent=1)
print(f"OK: 01_pmids {len(p01)} | vínculos {len(vinc)} (+{len(vinc)-n0}) | ledger {len(led)} (+{len(led)-l0})")
