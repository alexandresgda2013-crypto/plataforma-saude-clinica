# -*- coding: utf-8 -*-
"""B10 rodada [AT] — tríade (pmids, vínculos, ledger) + manifesto + trilha. Espelha convenções B9."""
import json, re, unicodedata

ROOT = "/home/user/BIBLIOTECAS/B10_DesregulacaoCircadiana"
DOC  = f"{ROOT}/B10 DESREGULACAO CIRCADIANA V2 CANONICA.md"
doc = unicodedata.normalize('NFC', open(DOC, encoding='utf-8').read())
refs = json.load(open(f"{ROOT}/producao/insumos/b10_refs_data.json"))
assert len(refs)==98

P_PMIDS = f"{ROOT}/Evidencias/Bibliografia/01_pmids.json"
P_VINC  = f"{ROOT}/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
P_LED   = f"{ROOT}/Auditoria_B10/ledger_auditoria_B10.json"
P_MAN   = f"{ROOT}/Evidencias/Bibliografia/_manifesto_biblioteca.json"

pmids = json.load(open(P_PMIDS)); vincs = json.load(open(P_VINC)); led = json.load(open(P_LED))
assert len(pmids)==39 and len(vincs)==39 and len(led)==39

# ---------- 1) pmids ----------
aux = {"_prosa","_tag","_bloco","_natureza","_maturidade","_tier","_acao"}
novos_pmids=[]
for r in refs:
    e={k:v for k,v in r.items() if k not in aux}
    novos_pmids.append(e)
pmids += novos_pmids
ids=[r['id_referencia_interna'] for r in pmids]; pms=[r['pmid_oficial'] for r in pmids]
assert len(set(ids))==137==len(ids) and len(set(pms))==137
json.dump(pmids, open(P_PMIDS,'w'), ensure_ascii=False, indent=1)

# ---------- 2) trecho_ancora ----------
def trecho_para(prosa, tag):
    cit = unicodedata.normalize('NFC', f"({prosa})[{tag}]")
    i = doc.find(cit)
    assert i>=0, cit
    assert doc.count(cit)==1, (cit, doc.count(cit))
    ls = doc.rfind('\n', 0, i)+1
    le = doc.find('\n', i+len(cit))
    if le<0: le=len(doc)
    t = doc[ls:le]
    assert doc.count(t)==1
    return t

trechos={}
for r in refs:
    trechos[r['id_referencia_interna']]=trecho_para(r['_prosa'], r['_tag'])
json.dump(trechos, open(f"{ROOT}/producao/insumos/b10_trechos_ancora.json",'w'), ensure_ascii=False, indent=1)

# ---------- 3) vínculos ----------
USO={"BLOCO01":"nucleo_causal","BLOCO02":"nucleo_causal","BLOCO07":"nucleo_causal","BLOCO08":"nucleo_causal",
     "BLOCO03":"suporte","BLOCO05":"suporte","BLOCO06":"suporte","BLOCO11":"suporte","BLOCO12":"suporte"}
novos_vincs=[]
for n,r in enumerate(refs, start=40):
    v={
     "id_vinculo": f"VINC_B10_{n:03d}",
     "id_referencia_interna": r['id_referencia_interna'],
     "pmid_oficial": r['pmid_oficial'],
     "secao_origem": "B10_CANONICA_V2",
     "trecho_ancora": trechos[r['id_referencia_interna']],
     "mecanismo_origem": "mecanismo_B10_desregulacao_circadiana",
     "natureza_relacao": r['_natureza'],
     "grau_maturidade": r['_maturidade'],
     "forca_causal": r['_tier'],
     "extrapolacao_por_analogia": r['extrapolacao_por_analogia'],
     "especie_mesh": r['especie_mesh'],
     "evid_role": r['evid_role'],
     "verification_status": r['verification_status'],
     "status_referencia": "CONFIRMADA",
     "citacao_confirmada": True,
     "g1_metodo": "eutils_automatico",
     "g2_elegibilidade": r['g2_elegibilidade'],
     "g2_motivo": r['g2_motivo'],
     "g3_verificado_por": "IA G3 (Rodada [AT] GPM B10 2026-09-09): eutils esearch DOI[aid]/PMID + esummary + efetch; abstract lido; divergências do dossiê externo resolvidas por DOI",
     "g3_fulltext": "abstract lido; PMC full-text fica para 2a verificação independente (P-6, avaliador cego)",
     "status_auditoria": "CONFIRMADO",
     "uso": USO[r['_bloco']],
     "segunda_verificacao": "PENDENTE — 2a verificação independente (P-6, avaliador cego) registrada como pendência de fase; mitigação: selos honestos [ML]/[OB]/[EC], regras fundadoras B10 fixadas em CONTROVÉRSIAS, extrapolação por analogia explícita",
     "data_verificacao": "2026-09-09"
    }
    novos_vincs.append(v)
vincs += novos_vincs
assert len(vincs)==137
json.dump(vincs, open(P_VINC,'w'), ensure_ascii=False, indent=1)

# ---------- 4) ledger ----------
PG2={"eligible":"ELIGIBLE_SOURCE","redirecionado_mecanistico":"NAO_APLICAVEL"}
novos_led=[]
for n,r in enumerate(refs, start=40):
    e={
     "id_auditoria": f"AUD_B10_{n:04d}",
     "mecanismo": "B10",
     "id_referencia_interna": r['id_referencia_interna'],
     "pmid_oficial": r['pmid_oficial'],
     "arquivo_modulo09": "Evidencias/Bibliografia/01_pmids.json",
     "tipo_classificador": "",
     "origem_entrada": "GPM",
     "claim_id": r['claim_id_origem'],
     "secao_origem": "B10_CANONICA_V2",
     "trecho_ancora": trechos[r['id_referencia_interna']],
     "citacao_literal": unicodedata.normalize('NFC', f"({r['_prosa']})[{r['_tag']}]"),
     "natureza_da_relacao": r['_natureza'],
     "grau_maturidade_cientifica": r['_maturidade'],
     "forca_causal": r['_tier'],
     "forca_biologica_conexao": "",
     "especie_mesh": r['especie_mesh'],
     "evid_role": r['evid_role'],
     "portao_G1_existencia": "VERIFIED_REFERENCE",
     "portao_G2_elegibilidade": PG2[r['g2_elegibilidade']],
     "portao_G3_suporte": "APROVADO",
     "status_auditoria": "APROVADO",
     "destino": "FICA_MECANISMO",
     "acao_correcao": r['_acao'],
     "reconciliado": True,
     "verificacao": {
      "verificador": "IA G3 Rodada [AT] GPM B10 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
      "data_verificacao": "2026-09-09",
      "g1_metodo": "eutils_automatico",
      "abstract_ou_trecho": "abstract efetch lido nesta rodada; trecho-âncora inserido na canônica V2",
      "query_utilizada": "esearch por PMID do dossiê e por DOI[aid] do anexo; esummary em lote; efetch completo",
      "g2_motivo": r['g2_motivo'],
      "g3_nota": "dossiê externo auditado: reatribuições corrigidas (Palagini 2022; Rao 2021; Spiga 2014; anos de print); preprint medRxiv (Burns 2024) excluído; P-6 pendente"
     }
    }
    novos_led.append(e)
led += novos_led
assert len(led)==137
json.dump(led, open(P_LED,'w'), ensure_ascii=False, indent=1)

# ---------- 5) verificação cruzada ----------
idp={r['id_referencia_interna'] for r in pmids} | set()
idv={v['id_referencia_interna'] for v in vincs}; idl={l['id_referencia_interna'] for l in led}
assert idp==idv==idl, "tríade fora de sincronia"
# novos vínculos: trecho literal 1×
for v in novos_vincs:
    assert doc.count(v['trecho_ancora'])==1, v['id_vinculo']
# legados: relatório (não bloqueante — ressalva de fase documentada)
leg_ok=sum(1 for v in vincs[:40] if False) # placeholder
leg_ok=sum(1 for v in vincs[:39] if v['trecho_ancora'] in doc)
print(f"tríade OK 137/137/137; vínculos novos com trecho 1×: {len(novos_vincs)}; legados com trecho ainda literal: {leg_ok}/39 (ressalva de fase legada, não bloqueante)")

# ---------- 6) manifesto ----------
man=json.load(open(P_MAN))
from collections import Counter
g2c=Counter(r['g2_elegibilidade'] for r in pmids)
man['artefato_rotulo']="CANONICA v2"
man['rodada']=4
man['pmids_total']=137
man['g1']={"metodo":"eutils_automatico","resolvidos":137}
man['g2']={"eligible":g2c.get('eligible',0),"redirecionado_mecanistico":g2c.get('redirecionado_mecanistico',0)}
man['g3']={"vinculos_n2":137}
man['versao']="2.6"
man['corte_literatura']="E-utilities/PubMed 2026-09-06 (v1) + rodada [AT] GPM 2026-09-09 (reconciliação P-7)"
man['historico_correcoes'].append({
 "data":"2026-09-09",
 "campo":"fusão [AT] GPM B10 (+98 refs; 39→137)",
 "correcao":"rodada externa (GPM molde v2.0 + dossiê RODADA0 + matriz RC.SM02) auditada ref a ref: reatribuições resolvidas (McGlashan 30555405; Kırlıoğlu 32750762; Serrano-Serrano 34640406; Spiga 24944037; Palagini 2022 35821870; Rao 2021 34436424; Robertson-Dixon 2023 37895351); preprint Burns 2024 (medRxiv indexado) excluído; anos de print canônicos (McCarthy 2022; Dollish 2024; Ketchesin 2020; Kinlein 2020; van Dalfsen 2018; Kırlıoğlu 2020); NAO-IDX declarados",
 "acao_downstream":"P-6 (ampliado para todas as levas [AT]) ao fim da rodada 16/16"
})
man['pendencias_fase']=[
 "P-6 avaliador cego — ampliado: cobre levas [AT] de B1–B16 ao fim da rodada",
 "Satyanarayanan 2020 (agomelatina) sem resolução [G1]",
 "Mendoza 2024 / Burns 2023 (Nature Mental Health) NAO-IDX [G1]",
 "DLMO/fase fisiológica como desfecho em ensaios de realinhamento (regra metodológica Wescott)",
 "GRADE formal pendente para ativação do pipeline"
]
json.dump(man, open(P_MAN,'w'), ensure_ascii=False, indent=1)

# ---------- 7) trilha ----------
trilha={
 "ciclo":"[AT] GPM B10 — Desregulação Circadiana",
 "data":"2026-09-09",
 "artefato":"CANONICA v2 (137 refs; de 39)",
 "insumos":[
  "GPM_B10_DesregulacaoCircadiana.md (oficial, molde v2.0 — M00–M10; regra fundadora timing≠estado)",
  "BRIEFING_B10_DESREGULACAO_CIRCADIANA_RODADA0.md (dossiê: 38 âncoras→PMID + 148 não citadas)",
  "BRIEFING_CONSOLIDADO_B10_v1.md (geração original; 12 sementes reconciliadas)",
  "Artigos cientificos do mecanismo B10 desregulação circadiana.md (193 entradas parseadas)",
  "Resumo do insumo para B10 chatgpt.md (matriz 58 claims RC.SM02.001–058)"
 ],
 "auditoria":{
  "anexo_itens":193,
  "candidatos_com_pmid_verificados":182,
  "doi_resolvidos_extras":15,
  "sobreposicao_com_V1":0,
  "masters_gpm":{"total_ancoras":38,"validas":37,"redesenho":"Rao 2021 (PMID do dossiê era Robertson-Dixon 2023; ambos entraram)"},
  "entra":98,"baixo":None,"exc":None,
  "anexo_fora_das_38_148_coberto":["Aydoğan/Gül 2025","Başer 2025","Carmona-Alcocer 2018","Gosztyła 2026","Gršković 2023","Kırlıoğlu 2020","Lande-Diner 2013","McCarthy 2021(2022)","McGlashan 2018","Palagini 2022","Takahashi 2016 cap.","Van Beurden 2022","van Dalfsen 2018","vanderLeest 2009","Wesarg-Menzel 2024"]
 },
 "decisao":{"entra":98,"baixo":"resto do corpus (SUP/CONTEXT/redundante/malha) documentado em matriz_b10_decisao.json","exc":"Burns 2024 (preprint medRxiv) + NAO-IDX (Burns 2022/2023; Mendoza 2024; Sandate 2020; Palagini 2023; Cao 2025; Gosztyła 2026; Noweta 2026; You 2024; Feng 2025) + não-fontes (Rumanova; Albrecht) + duplicatas (Murray 2016; Takahashi 2016 cap.)"},
 "fragilidades_dossie_revertidas":[
  "Palagini 2022 real existe (Clin Neuropsychiatry 35821870) — o dossiê o 'corrigira' para Pandi-Perumal",
  "Spiga 2014 é indexada (24944037; DOI do anexo era falso) — dossiê dizia NAO-IDX",
  "tabela-mestra #29 (Rao 2021) apontava para Robertson-Dixon 2023 — Rao real = 34436424",
  "Burns 2024 (âncora #33) é preprint medRxiv — excluído apesar da indexação",
  "pendências do dossiê resolvidas: McGlashan 2018=30555405 (estava rotulado 'Lyall'); Serrano-Serrano 2021=34640406 (rotulado 'Serrano 2026'); Walker 2020 e McCarthy ISBD confirmados",
  "15 refs do anexo ausentes do dossiê cobertas pela auditoria",
  "anos canônicos pelo print (McCarthy 2022; Dollish 2024; Ketchesin 2020; Kinlein 2020; van Dalfsen 2018; Kırlıoğlu 2020)"
 ],
 "regras_fixadas":[
  "B10-REGRA-01 timing≠estado (sono é output; insônia é distúrbio de estado; DSPD circadiano vs não-circadiano)",
  "B10-REGRA-02 sem biomarcador circadiano único validado para diagnóstico",
  "B10-REGRA-03 causalidade assimétrica (animal causal; humana associativa; genética inconsistente)",
  "B10-REGRA-04 intervenção≠mediador demonstrado (fase fisiológica como mediadora não provada)",
  "B10-REGRA-05 melatonina≠antidepressivo (marcador de fase; agomelatina é fármaco)",
  "B10-REGRA-06 [ML] é roedor/modelo (extrapolação por analogia; tradução pendente)",
  "B10-REGRA-07 anos canônicos pelo print",
  "B10-REGRA-08 bipolar sinalizado, nunca fundido à TDM"
 ],
 "artefatos":[
  "producao/insumos/b10_anexo_entries.json","producao/insumos/matriz_b10_g1.json","producao/insumos/b10_doi_resolution.json","producao/insumos/b10_efetch_all.json","producao/insumos/b10_refs_data.json","producao/insumos/b10_trechos_ancora.json","producao/insumos/matriz_b10_decisao.json","producao/insumos/RELATORIO_AUDITORIA_MATRIZ_B10.md","producao/historico/v1_canonica_2026-09-09.md"
 ],
 "pendencias":[
  "P-6 (2ª verificação cega, Via 2) — PENDENTE ao fim da rodada 16/16, cobrindo todas as levas [AT]",
  "Satyanarayanan 2020 (agomelatina) [G1]; Mendoza 2024 / Burns 2023 (NMH) [G1]"
 ]
}
json.dump(trilha, open(f"{ROOT}/producao/04_AT_ciclo_2026-09-08.json",'w'), ensure_ascii=False, indent=1)
import os
os.replace(f"{ROOT}/producao/04_AT_ciclo_2026-09-08.json", f"{ROOT}/producao/04_AT_ciclo_2026-09-09.json")
print("OK json: pmids/vínculos/ledger/manifesto/trilha aplicados")
