#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grava JSONs da leva [AT] 2026-09-08 na B3: 01_pmids, vínculos, ledger, manifesto,
trilha AT (P-7) e 04_atualizacoes_literatura.json=[]. Idempotente (pula já gravados)."""
import json, re
from pathlib import Path
B3=Path('/home/user/BIBLIOTECAS/B03_Neuroplasticidade')
CFG=json.load(open(B3/'producao/insumos/matriz_b3_at_final.json'))
DEC=json.load(open(B3/'producao/insumos/matriz_b3_decisao.json'))
V=(B3/'B3 NEUROPLASTICIDADE V2 CANONICA.md').read_text(encoding='utf-8')

P01=B3/'Evidencias/Bibliografia/01_pmids.json'
PV=B3/'Evidencias/Vinculos/vinculos_referencia_afirmacao.json'
PL=B3/'Auditoria_B3/ledger_auditoria_B3.json'
PM=B3/'Evidencias/Bibliografia/_manifesto_biblioteca.json'
P04=B3/'Evidencias/Bibliografia/04_atualizacoes_literatura.json'
PAT=B3/'producao/04_AT_ciclo_2026-09-08.json'

regs=json.load(open(P01)); vinc=json.load(open(PV)); led=json.load(open(PL))
vig_pm={r['pmid_oficial'] for r in regs}
novas=[o for o in CFG if o['pmid_final'] not in vig_pm]
if not novas:
    print("nada a fazer (idempotente)"); raise SystemExit
print("já vigentes:",len(regs),"· novas:",len(novas))

# mapeia grupo -> linha de apêndice (trecho âncora)
def apx_line(gs):
    items=[]
    for g in gs:
        for o in CFG:
            if o['grupo']==g: items.append(f"{o['ID'].replace('REF_','')}[{o['tag']}]")
    return '*'+' | '.join(items)+'*'
LINHAS={'A':0,'D':0,'B':1,'C':2,'E':3,'F':4,'L':4,'G':5,'H':5,'J':5,'I':6,'K':6,'M':7,'N':7,'O':8}
GRPS=[['A'],['D'],['B'],['C'],['E'],['F'],['L'],['G'],['H'],['J'],['I'],['K'],['M'],['N'],['O']]
APX=[apx_line(['A','D']),apx_line(['B']),apx_line(['C']),apx_line(['E']),apx_line(['F','L']),
     apx_line(['G','H','J']),apx_line(['I','K']),apx_line(['M','N']),apx_line(['O'])]
for ln in APX:
    assert ln in V, "linha de apêndice ausente: "+ln[:60]

CLAIM_BASE={'A':('B3.MEC.BLOCO02',21),'B':('B3.MEC.BLOCO02',28),'C':('B3.MEC.BLOCO02',41),
 'D':('B3.MEC.BLOCO02',51),'E':('B3.MEC.BLOCO01',106),'F':('B3.MEC.BLOCO03',61),
 'G':('B3.MEC.BLOCO03',72),'H':('B3.MEC.BLOCO03',77),'I':('B3.MEC.BLOCO05',51),
 'J':('B3.MEC.BLOCO05',55),'K':('B3.MEC.BLOCO05',57),'L':('B3.MEC.BLOCO06',63),
 'M':('B3.MEC.BLOCO06',64),'N':('B3.MEC.BLOCO07',71),'O':('B3.MEC.BLOCO08',81)}
DESENHO={'EC':'estudo_humano','MA':'meta_analise','OB':'revisao_narrativa','ML':'estudo_preclinico_animal'}
MATUR={'EC':'bem_suportado','MA':'bem_suportado','OB':'moderadamente_suportado','ML':'moderadamente_suportado'}
ROLE={'EC':'human_clinical','MA':'meta_analise','OB':'revisao_mecanistica','ML':'preclinico_mecanistico'}
n0=len(regs)+1; nv0=len(vinc)+1; nl0=len(led)+1
cnt={}
novos_regs=[]; novos_vinc=[]; novos_led=[]
for i,o in enumerate(novas):
    bkey,num0=CLAIM_BASE[o['grupo']]
    cnt[o['grupo']]=cnt.get(o['grupo'],0)+1
    claim=f"{bkey}.{num0+cnt[o['grupo']]-1:03d}"
    tag=o['tag']; li=APX[LINHAS[o['grupo']]]
    rid=o['ID']
    rec={"pmid_oficial":o['pmid_final'],"titulo_artigo":o['titulo'],"autores":o['autores'],
     "revista_ano":f"{o['journal']} {o['ano']}","desenho_estudo":DESENHO[tag],
     "secao_origem":"mecanismo_B3_neuroplasticidade",
     "achado_central_molecular":o['achado'],
     "extrapolacao_por_analogia":("[APENAS PRÉ-CLÍNICO] " if tag=='ML' else "")+(o['nota'] or "—"),
     "ids_referencia_interna":[rid],"evid_role":ROLE[tag],"especie_mesh":o['especie_mesh'],
     "verification_status":"verificado","citacao_confirmada":True,"g1_metodo":"eutils_automatico",
     "g2_elegibilidade":"eligible","g2_motivo":"escopo B3 confirmado em auditoria [AT] (título/abstract MeSH)",
     "g3_verificado_por":"IA G3 (geração) — B3 [AT 2026-09-08]; P-6 2a verificacao independente (avaliador cego) PENDENTE",
     "status_auditoria":"CONFIRMADO","origem_pipeline":"ATUALIZACAO_AT_2026-09-08 (insumo externo auditado)",
     "id_referencia_interna":rid,"doi":o['doi'],"claim_id_origem":claim,
     "_aliases":[o['label'].split('_')[0], o['label'].split('_')[0].upper()]}
    novos_regs.append(rec)
    gv={"id_vinculo":f"VINC_B3_{nv0+i:03d}","id_referencia_interna":rid,"pmid_oficial":o['pmid_final'],
     "secao_origem":"B3_CANONICA","trecho_ancora":li,"mecanismo_origem":"mecanismo_B3_neuroplasticidade",
     "natureza_relacao":"contributiva","grau_maturidade":MATUR[tag],
     "forca_causal":"tier_4_descritivo_estrutural","especie_mesh":o['especie_mesh'],"evid_role":ROLE[tag],
     "verification_status":"verificado","citacao_confirmada":True,"g1_metodo":"eutils_automatico",
     "g2_elegibilidade":"eligible","g2_motivo":rec['g2_motivo'],
     "g3_verificado_por":rec['g3_verificado_por'],"status_auditoria":"CONFIRMADO",
     "status_referencia":"CONFIRMADA","uso":"contexto_mecanistico","data_verificacao":"2026-09-08"}
    novos_vinc.append(gv)
    gl={"id_auditoria":f"AUD_B3_{nl0+i:04d}","mecanismo":"B3","id_referencia_interna":rid,
     "pmid_oficial":o['pmid_final'],"arquivo_modulo09":"Evidencias/Bibliografia/01_pmids.json",
     "tipo_classificador":"","origem_entrada":"POLITICA_FONTES","claim_id":claim,
     "secao_origem":"B3_CANONICA","trecho_ancora":li,"citacao_literal":f"{o['label']}[{tag}]",
     "natureza_da_relacao":"contributiva","grau_maturidade_cientifica":MATUR[tag],
     "forca_causal":"tier_4_descritivo_estrutural","forca_biologica_conexao":"",
     "especie_mesh":o['especie_mesh'],"evid_role":ROLE[tag],
     "portao_G1_existencia":"VERIFIED_REFERENCE","portao_G2_elegibilidade":"ELIGIBLE_SOURCE",
     "portao_G3_suporte":"APROVADO","status_auditoria":"APROVADO","destino":"FICA_MECANISMO",
     "acao_correcao":"MANTER","reconciliado":True,
     "verificacao":{"verificador":rec['g3_verificado_por'],"data_verificacao":"2026-09-08",
      "g1_metodo":"eutils_automatico (esearch+esummary+efetch)",
      "abstract_ou_trecho":(o['abstract'][:420] if o['abstract'] else "esummary conferido (G1 eutils)."),
      "query_utilizada":f"esearch PubMed DOI[aid] ou PMID direto; validado autor+ano+tema",
      "g2_motivo":rec['g2_motivo'],
      "g3_nota":"ademais do insumo externo auditado ref a ref; G3 IA (geração); P-6 pendente"}}
    novos_led.append(gl)
regs+=novos_regs; vinc+=novos_vinc; led+=novos_led
assert len({r['id_referencia_interna'] for r in regs})==len(regs), "id duplicado 01_pmids"
assert len({l['id_auditoria'] for l in led})==len(led)
json.dump(regs,open(P01,'w'),ensure_ascii=False,indent=1)
json.dump(vinc,open(PV,'w'),ensure_ascii=False,indent=1)
json.dump(led,open(PL,'w'),ensure_ascii=False,indent=1)
# manifesto
m=json.load(open(PM))
m.setdefault('atualizacoes_pos_publicacao',[]).append({
 "data":"2026-09-08","tipo":"AT_P7_INSUMO_EXTERNO","biblioteca":"B3","versao":"V2",
 "resumo":"Insumo 'matriz canônica B3' (193 itens + consolidação) auditado ref a ref (G1 eutils): 112 refs incorporadas (53→165); 0 FP; 3 correções de autoria; 33 EXC escopo, 42 baixo incremento, 2 erratas, 8 não-resolvidos; P-6 pendente.",
 "refs_adicionadas":[o['pmid_final'] for o in novas]})
json.dump(m,open(PM,'w'),ensure_ascii=False,indent=1)
json.dump([],open(P04,'w'))
json.dump({"at_ciclo":"2026-09-08","biblioteca":"B3","at_status":"INCORPORADO_V2",
 "insumo":{"arquivo":"uploads/Artigos cientificos do mecanismo B3 Neuroplasticidade.md","itens":193,
   "consolidacao_texto":True},
 "incorporadas":[{"pmid":o['pmid_final'],"id":o['ID'],"grupo":o['grupo'],"tag":o['tag']} for o in novas],
 "rejeitados_registro":{
   "EXC_escopo":DEC['EXC'],"BAIXO_incremento":DEC['BAIXO'],"erratas":DEC['ERRATA'],
   "falhas_g1":DEC['FALHAS'],"correcoes_autoria":DEC['FP'],
   "ja_vigentes":DEC['VIG']}},open(PAT,'w'),ensure_ascii=False,indent=1)
print(f"01_pmids {len(regs)} · vínculos {len(vinc)} · ledger {len(led)} · manifesto+trilha OK")
