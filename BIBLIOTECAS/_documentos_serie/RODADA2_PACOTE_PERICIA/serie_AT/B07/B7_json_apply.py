#!/usr/bin/env python3
# B7 — aplica rodada [AT] GPM 2026-09-09 na tríade (pmids/vínculos/ledger) + manifesto + trilha
import json

BASE='/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro'
E=json.load(open(f'{BASE}/producao/insumos/b7_at_efetch.json'))
T=json.load(open(f'{BASE}/producao/insumos/b7_trechos_ancora.json'))
if 'REF_ABURTOCRYAN_2024' in T: T['REF_ABURTO_2024']=T.pop('REF_ABURTOCRYAN_2024')
CANON=open(f'{BASE}/B7 EIXO INTESTINO CEREBRO V2 CANONICA.md',encoding='utf-8').read()

# rid: (pmid, prosa, tag, bloco_claim, evid_role, natureza, maturidade, uso, desenho, g2_eleg, g2_motivo, achado, aliases_extra, especie_override)
D=[
('REF_GUO_2013','23201091','Guo 2013','ML','BLOCO02',1,'preclinical_mechanistic','contributiva','bem_suportado','nucleo_causal',
 '[ML] LPS→TLR4/CD14 no enterócito→↑permeabilidade TJ — in vitro + in vivo (rato) · Am J Pathol','redirecionado_mecanistico','evidência pré-clínica (rato/célula); uso mecanístico; tradução humana indireta [EXT]',
 'LPS induz expressão/localização de TLR4-CD14 na membrana do enterócito e aumenta a permeabilidade de tight junction intestinal, in vitro e in vivo.',[],None),
('REF_GUO_2015','26466961','Guo 2015','ML','BLOCO02',2,'preclinical_mechanistic','contributiva','bem_suportado','nucleo_causal',
 '[ML] LPS→TLR4→FAK/MyD88→TJ (am J Pathol… J Immunol)','redirecionado_mecanistico','mesmo desenho da série Guo: primário mecanístico não-humano',
 'A regulação da permeabilidade de tight junction intestinal por LPS é mediada pela via TLR4 com ativação de FAK e MyD88.',[],None),
('REF_NIGHOT_2017','29157665','Nighot 2017','ML','BLOCO02',3,'preclinical_mechanistic','contributiva','bem_suportado','nucleo_causal',
 '[ML] LPS→TLR4/MyD88→↑MLCK (enterócito, in vitro/in vivo) · Am J Pathol','redirecionado_mecanistico','primário mecanístico in vitro/in vivo; tradução indireta [EXT]',
 'O aumento de permeabilidade epitelial intestinal por LPS é mediado por TLR4/MyD88 com ativação da expressão da MLCK.',[],None),
('REF_NIGHOT_2019','30711488','Nighot 2019','ML','BLOCO02',4,'preclinical_mechanistic','contributiva','bem_suportado','nucleo_causal',
 '[ML] LPS→TAK-1→IKK→MLCK/MYLK · Am J Pathol','redirecionado_mecanistico','primário mecanístico; tradução indireta [EXT]',
 'O efeito de LPS sobre a permeabilidade intestinal é mediado por TAK-1, com ativação de IKK e do gene MLCK/MYLK.',[],None),
('REF_KURITA_2020','31910709','Kurita 2020','ML','BLOCO02',5,'preclinical_mechanistic','contributiva','bem_suportado','nucleo_causal',
 '[ML] endotoxemia metabólica→neuroinflamação (camundongo; contexto isquemia experimental) · J Cereb Blood Flow Metab','redirecionado_mecanistico','modelo isquêmico: a lição transportável é a endotoxemia; AVC não é escopo',
 'Endotoxemia metabólica crônica promove neuroinflamação em roedor (modelo em contexto isquêmico — a seta transportável é endotoxemia→SNC).',[],None),
('REF_TULKENS_2020','30518529','Tulkens 2020','EC','BLOCO02',6,'human_clinical','associativa','emergente','associativo_observacional',
 '[EC] carta ao Gut: EVs bacterianas LPS+ sistêmicas ↑ em pacientes com disfunção de barreira · Gut','redirecionado_clinico','estudo humano observacional de barreira/translocação; sem desfecho psiquiátrico (B7-CAUSAL-03)',
 'Pacientes com disfunção de barreira intestinal apresentam níveis sistêmicos aumentados de vesículas extracelulares bacterianas LPS-positivas — janela humana de translocação; SEM ABSTRACT no PubMed (validação G3 por título/periódico/autores).',[],None),
('REF_KUO_2021','34478742','Kuo 2021','ML','BLOCO02',7,'preclinical_mechanistic','contributiva','bem_suportado','nucleo_causal',
 '[ML] ZO-1 cKO: dispensável p/ barreira, crítico p/ reparo (camundongo/organoides) · Gastroenterology','redirecionado_mecanistico','primário mecanístico; refina o uso de ZO-1 como marcador',
 'A proteína de junção ZO-1 é dispensável para a função de barreira intestinal, mas crítica para o reparo mucoso — freio de precisão contra leituras de ZO-1 como "marcador de permeabilidade".',[],None),
('REF_ERNY_2021','34731656','Erny 2021','ML','BLOCO02',8,'preclinical_mechanistic','contributiva','bem_suportado','nucleo_causal',
 '[ML] acetato microbiano→aptidão metabólica/maturação microglial (camundongo) · Cell Metab','redirecionado_mecanistico','marco pré-clínico; formulação específica protegida (não "AGCC anti-inflamatório")',
 'O acetato derivado de microbiota sustenta a aptidão metabólica e a maturação da microglia — imunidade inata cerebral — em saúde e doença (roedor).',[],None),
('REF_SPICHAK_2021','34589808','Spichak 2021','ML','BLOCO02',9,'preclinical_mechanistic','contributiva','moderadamente_suportado','nucleo_causal',
 '[ML] AGCC microbianos→expressão gênica astrocitária sexo-específica (roedor/célula) · Brain Behav Immun Health','redirecionado_mecanistico','primário mecanístico único; astrócitos',
 'AGCC derivados de microbiota modulam a expressão gênica de astrócitos de modo sexo-específico.',[],['Animals']),
('REF_CAETANOSILVA_2023','36797287','Caetano-Silva 2023','ML','BLOCO02',10,'preclinical_mechanistic','contributiva','moderadamente_suportado','nucleo_causal',
 '[ML] fibra/AGCC inibem microglia inflamatória (murino/in vitro) · Sci Rep','redirecionado_mecanistico','primário mecanístico; microglia',
 'Fibra alimentar e AGCC inibem a ativação inflamatória da microglia em modelo murino/in vitro.',['CaetanoSilva','CAETANOSILVA','Caetanosilva','Caetano-Silva','CAETANO-SILVA'],None),
('REF_BARKI_2022','35229717','Barki 2022','ML','BLOCO02',11,'preclinical_mechanistic','contributiva','bem_suportado','nucleo_causal',
 '[ML] quimiogenética define eixo receptor-AGCC intestino→cérebro (camundongo) · eLife','redirecionado_mecanistico','primário mecanístico (quimiogenética); tradução indireta [EXT]',
 'A quimiogenética define um eixo receptor-de-AGCC intestino→cérebro em camundongo.',[],None),
('REF_CHENG_2024','38390241','Cheng 2024','OB','BLOCO02',12,'review','contributiva','bem_suportado','arquitetura_mecanistica',
 '[OB] revisão: AGCC derivados de microbiota e depressão · Gen Psychiatr','eligible','revisão mecanística dedicada (AGCC×depressão)',
 'Revisão mecanística dos AGCC derivados de microbiota na depressão: mecanismos e aplicações potenciais.',[],None),
('REF_CHEN_2024','38939042','Chen 2024','ML','BLOCO02',13,'preclinical_mechanistic','contributiva','bem_suportado','nucleo_causal',
 '[ML] AGCC cerebral→ACSS2→PPARγ→TPH2→comportamento (camundongo; knockdown ACSS2 abole) · Research (Wash DC)','redirecionado_mecanistico','cadeia circuital completa em ROEDOR — vedado transcrever à clínica',
 'AGCC cerebrais induzem ACSS2 neuronal e melhoram o comportamento tipo-depressivo via eixo PPARγ-TPH2 (serotonina); knockdown neuronal de ACSS2 abole o efeito.',[],['Animals']),
('REF_CHENGHAN_2025','39998158','Chenghan 2025','ML','BLOCO02',14,'preclinical_mechanistic','contributiva','moderadamente_suportado','nucleo_causal',
 '[ML] antibióticos orais perturbam BBB; AGCC restauram — macaco rhesus + camundongo · Ann N Y Acad Sci','redirecionado_mecanistico','primário translacional (rhesus) único; BBB×AGCC',
 'Antibióticos orais perturbam a barreira hematoencefálica e AGCC restauram sua integridade, em macaco rhesus e camundongo.',[],None),
('REF_NOHR_2013','23885020','Nøhr 2013','ML','BLOCO02',15,'preclinical_mechanistic','contributiva','moderadamente_suportado','nucleo_causal',
 '[ML] mapa FFAR3/GPR41 e FFAR2/GPR43 em EEC e SNE (camundongo repórter) · Endocrinology','redirecionado_mecanistico','mapeamento de receptores (repórter murino); elo metabólito→receptor',
 'FFAR3 (GPR41) e FFAR2 (GPR43) expressam-se em subconjuntos de células enteroendócrinas (GLP-1/PYY/CCK/GIP/secretina/grelina) e em neurônios entéricos/leucócitos, definindo o sensor intestinal de AGCC.',['NOHR','Nohr','NØHR'],None),
('REF_SAIKACHAIN_2023','37070532','Saikachain 2023','ML','BLOCO02',16,'preclinical_mechanistic','contributiva','emergente','nucleo_causal',
 '[ML] AGCC neuroprotetores via GPR43 — SH-SY5Y in vitro · J Neurochem','redirecionado_mecanistico','prova celular (linhagem humana SH-SY5Y); in vitro apenas',
 'AGCC protegem células SH-SY5Y da injúria por estresse oxidativo via via dependente de GPR43 (in vitro).',[],None),
('REF_AGUS_2018','29902437','Agus 2018','OB','BLOCO02',17,'review','contributiva','bem_suportado','arquitetura_mecanistica',
 '[OB] revisão Cell Host Microbe: microbiota regula o metabolismo do triptofano','eligible','revisão de arquitetura do substrato Trp',
 'A microbiota intestinal regula o metabolismo do triptofano em saúde e doença (colheita/partição do substrato).',[],None),
('REF_BOSI_2020','32577079','Bosi 2020','OB','BLOCO02',18,'review','contributiva','bem_suportado','arquitetura_mecanistica',
 '[OB] revisão: metabólitos do triptofano como comunicação inter-reinos no eixo · Int J Tryptophan Res','eligible','revisão de arquitetura',
 'Os metabólitos do triptofano operam como sistema de comunicação inter-reinos ao longo do eixo microbiota-intestino-cérebro.',[],None),
('REF_CHEN_2021','34127024','Chen 2021','OB','BLOCO02',19,'review','contributiva','bem_suportado','arquitetura_mecanistica',
 '[OB] revisão: elo triptofano-quinurenina intestino-cérebro na depressão/DII · J Neuroinflammation','eligible','revisão com desfecho psiquiátrico explícito',
 'O metabolismo triptofano-quinurenina é um elo intestino-cérebro para a depressão na doença inflamatória intestinal.',[],None),
('REF_SCHWARCZ_2024','38612489','Schwarcz 2024','ML','BLOCO02',20,'preclinical_mechanistic','contributiva','moderadamente_suportado','guarda_B7_CAUSAL_02',
 '[ML] L. reuteri sintetiza KYNA de KYN — in vitro · Int J Mol Sci','redirecionado_mecanistico','produção bacteriana in vitro ≠ produção cerebral (B7-CAUSAL-02)',
 'O probiótico Lactobacillus reuteri sintetiza preferencialmente ácido quinurênico (KYNA) a partir de quinurenina, in vitro.',[],None),
('REF_SATHYASAIKUMAR_2024','38911967','Sathyasaikumar 2024','ML','BLOCO02',21,'preclinical_mechanistic','contributiva','moderadamente_suportado','guarda_B7_CAUSAL_02',
 '[ML] IPrA (metabólito isolado) eleva KYNA no cérebro — rato in vivo · Int J Tryptophan Res','redirecionado_mecanistico','claim metabólito→cérebro; não microbiota→cérebro (B7-CAUSAL-02)',
 'O metabólito indol-3-propionato (IPrA) eleva os níveis de ácido quinurênico no cérebro de rato in vivo.',[],['Animals']),
('REF_ZHAO_2022','36776388','Zhao 2022','ML','BLOCO02',22,'preclinical_mechanistic','contributiva','moderadamente_suportado','nucleo_causal',
 '[ML] colite DSS→IDO-1→KYN soro+cérebro, dependente de microbiota (camundongo) · Front Immunol','redirecionado_mecanistico','primário mecanístico; inflamação intestinal→KYN cerebral',
 'A colite DSS ativa a via da quinurenina no soro e no cérebro via IDO-1, em dependência da microbiota intestinal.',[],None),
('REF_LI_2023','36746244','Li 2023','ML','BLOCO02',23,'preclinical_mechanistic','contributiva','moderadamente_suportado','nucleo_causal',
 '[ML] perfil Trp-KYN intestino+cérebro em ratos com fenótipo depressivo (CRS) · J Affect Disord','redirecionado_mecanistico','primário com fenótipo tipo-depressivo em roedor [APENAS PRÉ-CLÍNICO]',
 'Ratos com fenótipo depressivo por estresse crônico de contenção exibem perfil triptofano-quinurenina alterado simultaneamente no intestino e no cérebro.',[],None),
('REF_STANIMIROV_2025','41465592','Stanimirov 2025','OB','BLOCO02',24,'review','contributiva','moderadamente_suportado','arquitetura_mecanistica',
 '[OB] revisão: sinalização por sais biliares no eixo (FXR/TGR5) · Int J Mol Sci','eligible','única revisão dedicada bile↔cérebro da rodada',
 'A microbiota modifica o pool de sais biliares, que sinalizam via FXR/TGR5 com ação direta no SNC e indireta por mediadores endócrinos e imunes.',[],None),
('REF_BAJ_2019','30934533','Baj 2019','OB','BLOCO02',25,'review','contributiva','moderadamente_suportado','arquitetura_mecanistica',
 '[OB] revisão: sinalização glutamatérgica no eixo microbiota-intestino-cérebro · Int J Mol Sci','eligible','elo glutamato (B5) no eixo',
 'A sinalização glutamatérgica transita no eixo microbiota-intestino-cérebro (revisão dedicada).',[],None),
('REF_OHARA_2025','39743581','Ohara 2025','OB','BLOCO04',1,'review','contributiva','bem_suportado','arquitetura_mecanistica',
 '[OB] revisão Nat Rev Microbiol: sinalização neuroepitelial no eixo','eligible','janela neuroepitélio/neuropods ausente na V1',
 'Sinalização neuroepitelial no eixo intestino-cérebro: neuropods e células EEC como transdutores do lúmen ao sistema nervoso.',[],None),
('REF_ABURTO_2024','38355758','Aburto & Cryan 2024','OB','BLOCO01',1,'review','contributiva','bem_suportado','arquitetura_mecanistica',
 '[OB] revisão Nat Rev Gastroenterol Hepatol: barreiras GI e cerebral como portas de comunicação do eixo','eligible','revisão-teto de barreiras (2024)',
 'As barreiras gastrointestinal e cerebral funcionam como portas de comunicação através do eixo microbiota-intestino-cérebro.',['AburtoCryan','ABURTOCRYAN','Aburtocryan'],None),
('REF_CARABOTTI_2015','25830558','Carabotti 2015','OB','BLOCO01',2,'review','contributiva','bem_suportado','arquitetura_mecanistica',
 '[OB] revisão Ann Gastroenterol: interações microbiota entérica–SNC–SNE','eligible','sistematização clássica; sem DOI no anexo (resgatada por busca dirigida)',
 'Sistematização das interações entre microbiota entérica, sistema nervoso central e sistema nervoso entérico (eixo intestino-cérebro).',[],None),
('REF_LIN_2023','37049591','Lin 2023','EC','BLOCO05',1,'human_clinical','associativa','emergente','associativo_observacional',
 '[EC] disbiose+via KYN como biomarcadores potenciais na TDM · Nutrients','redirecionado_clinico','observacional humano; ASSOCIATIVO (B7-CAUSAL-03)',
 'Disbiose da microbiota intestinal e atividade da via da quinurenina como biomarcadores potenciais em pacientes com transtorno depressivo maior.',[],None),
('REF_ZHOU_2023','37386523','Zhou 2023','EC','BLOCO05',2,'human_clinical','associativa','emergente','associativo_observacional',
 '[EC] metabolômica Trp + microbiota em adolescentes com depressão (humano) com validação em camundongo · Microbiome','redirecionado_clinico','humano associativo + braço mecanístico animal (validação); ler clínica como ASSOCIATIVA',
 'Em adolescentes com depressão, a metabolômica do triptofano integra microbiota e neurotransmissores; validação em camundongo aponta a microbiota regulando neurotransmissores derivados de triptofano e comportamento.',[],None),
('REF_ZHANG_2025','39716675','Zhang Q 2025','EC','BLOCO05',3,'human_clinical','associativa','emergente','associativo_observacional',
 '[EC] multiômica microbiota+imunidade+Trp-KYN × cognição na TDM · J Affect Disord','redirecionado_clinico','observacional humano (N=86×120); ASSOCIATIVO (B7-CAUSAL-03)',
 'Análise multi-ômica associa microbiota intestinal, imunidade e metabolismo triptofano-quinurenina ao desempenho cognitivo no transtorno depressivo maior.',['ZHANG Q','Zhang Q'],None),
]
assert len(D)==31
assert len({d[0] for d in D})==31 and len({d[1] for d in D})==31

def aut_entry(auth):
    a1=auth[0].split()[0]; return a1

AL=lambda sob:[sob.upper(),sob]
pmids_new=[]; vincs_new=[]; leds_new=[]
for i,d in enumerate(D):
    (rid,pmid,prosa,tag,bloco,nc,erole,nat,mat,uso,desenho,g2e,g2m,achado,alx,esp_ov)=d
    e=E[pmid]
    ano=e['ano_print']; iso=e['iso']
    esp=e['especie_mesh'] or (esp_ov or []) or (['Humans'] if erole in('human_clinical','human_experimental') else [])
    claim=f'B7.MEC.{bloco}.{nc:03d}'
    autores=e['autores'] if e['autores'] else ['?']
    a1=autores[0].split()[0]
    aliases=AL(a1)+alx
    extrap = 'SIM — evidência em roedor/modelo; tradução humana por analogia' if tag=='ML' else ('não' if tag=='EC' else 'parcial — revisão mistura espécies')
    verif = 'preclinico' if tag=='ML' else 'emergente'
    trecho=T[rid].rstrip('\n')
    assert CANON.count(trecho)==1, ('trecho',rid)
    cit=f'({prosa})[{tag}]'
    assert CANON.count(cit)>=1, ('cit',cit)
    ensaio_sem_abs = pmid=='30518529'
    pmids_new.append({
     'pmid_oficial':pmid,'titulo_artigo':e['titulo'],'autores':autores,
     'revista_ano':f'{iso} ({ano})','desenho_estudo':desenho,
     'secao_origem':'mecanismo_B7_eixo_intestino_cerebro_microbiota',
     'achado_central_molecular':achado,
     'extrapolacao_por_analogia':extrap,
     'ids_referencia_interna':[rid],'evid_role':erole,'especie_mesh':esp,
     'verification_status':verif,'citacao_confirmada':True,'g1_metodo':'eutils_automatico',
     'g2_elegibilidade':g2e,'g2_motivo':g2m,
     'g3_verificado_por':'IA G3 (Rodada [AT] GPM B7 2026-09-09): esearch DOI[aid]/busca dirigida + esummary + efetch; abstract lido' + (' — SEM ABSTRACT no PubMed; G3 por título/periódico/autores' if ensaio_sem_abs else '') + '; 2a verificação independente (P-6) pendente',
     'status_auditoria':'CONFIRMADO','origem_pipeline':'GPM_RODADA_AT','id_referencia_interna':rid,
     'doi':e['doi'],'claim_id_origem':claim,'_aliases':aliases})
    vfc = 'tier_3_mecanistico_animal' if tag=='ML' else ('tier_4_observacional_transversal' if tag=='EC' else 'tier_4_descritivo_estrutural')
    lfc = 'tier_3_correlacional_mecanistico' if tag=='ML' else 'tier_4_descritivo_estrutural'
    vincs_new.append({
     'id_vinculo':f'VINC_B7_{40+len(vincs_new)+1:03d}','id_referencia_interna':rid,'secao_origem':'B7_CANONICA_V2',
     'trecho_ancora':trecho,'mecanismo_origem':'mecanismo_B7_eixo_intestino_cerebro_microbiota',
     'natureza_relacao':nat,'grau_maturidade':mat,'forca_causal':vfc,
     'extrapolacao_por_analogia': extrap + (' [EXT]' if tag=='ML' else ''),
     'especie_mesh':esp,'evid_role':erole,'verification_status':verif,'status_referencia':'CONFIRMADA',
     'citacao_confirmada':True,'g1_metodo':'eutils_automatico','g2_elegibilidade':g2e,'g2_motivo':g2m,
     'g3_verificado_por':'IA G3 (Rodada [AT] GPM B7 2026-09-09): eutils esearch DOI[aid] + esummary + efetch abstract lido ref a ref; P-6 pendente',
     'g3_fulltext':'abstract lido; PMC full-text fica para 2a verificação independente (P-6, avaliador cego)' if not ensaio_sem_abs else 'SEM ABSTRACT no PubMed (carta ao Gut, letter+research); validação G3 por título/periódico (Gut)/autores; P-6 pendente',
     'status_auditoria':'CONFIRMADO','uso':uso,'segunda_verificacao':'PENDENTE — 2a verificação independente (P-6, avaliador cego)'})
    leds_new.append({
     'id_auditoria':f'AUD_B7_{47+len(leds_new)+1:04d}','mecanismo':'B7','id_referencia_interna':rid,'pmid_oficial':pmid,
     'arquivo_modulo09':'Evidencias/Bibliografia/01_pmids.json','tipo_classificador':'','origem_entrada':'GPM [AT] 2026-09-09',
     'claim_id':claim,'secao_origem':'B7_CANONICA_V2','trecho_ancora':trecho + ('' if CANON.count(trecho+cit) else ''),
     'citacao_literal':cit,'natureza_da_relacao':nat,'grau_maturidade_cientifica':mat,'forca_causal':lfc,
     'forca_biologica_conexao':'','especie_mesh':esp,'evid_role':erole,
     'portao_G1_existencia':'VERIFIED_REFERENCE','portao_G2_elegibilidade':'NAO_APLICAVEL' if tag=='ML' else 'ELIGIBLE_SOURCE',
     'portao_G3_suporte':'APROVADO','status_auditoria':'APROVADO','destino':'FICA_MECANISMO','acao_correcao':'ACRESCENTAR',
     'reconciliado':True,
     'verificacao':{'verificador':'IA G3 Rodada [AT] GPM B7 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente',
      'data_verificacao':'2026-09-09','g1_metodo':'eutils_automatico',
      'abstract_ou_trecho':('carta ao Gut SEM ABSTRACT indexado; validação por título/periódico/autores (G3)' if ensaio_sem_abs else 'abstract efetch lido nesta rodada; trecho-âncora inserido na canônica V2'),
      'query_utilizada':'esearch PubMed DOI[aid]' + (' / busca dirigida autor+ano (sem DOI no anexo)' if pmid=='25830558' else ''),
      'g2_motivo':g2m,'g3_nota':'integridade referencial + formulação protegida (regras B7-CAUSAL) quando aplicável.'}})

pj=f'{BASE}/Evidencias/Bibliografia/01_pmids.json'
vj=f'{BASE}/Evidencias/Vinculos/vinculos_referencia_afirmacao.json'
lj=f'{BASE}/Auditoria_B7/ledger_auditoria_B7.json'
pjx=json.load(open(pj)); vjx=json.load(open(vj)); ljx=json.load(open(lj))
old_p,old_v,old_l=len(pjx),len(vjx),len(ljx)
pjx+=pmids_new; vjx+=vincs_new; ljx+=leds_new
assert len(pjx)==116 and len(vjx)==71 and len(ljx)==78
ids=[e['id_referencia_interna'] for e in pjx]
assert len(set(ids))==116, 'id duplicado'
# trechos dos NOVOS vínculos estão na V2
for v in vincs_new: assert CANON.count(v['trecho_ancora'])==1, v['id_vinculo']
json.dump(pjx, open(pj,'w'), ensure_ascii=False, indent=1)
json.dump(vjx, open(vj,'w'), ensure_ascii=False, indent=1)
json.dump(ljx, open(lj,'w'), ensure_ascii=False, indent=1)

# manifesto
mj=f'{BASE}/Evidencias/Bibliografia/_manifesto_biblioteca.json'
man=json.load(open(mj))
man['artefato_rotulo']='CANONICA v2'
man['rodada']=4
man['data_corte']='2026-09-09'
man['pmids_total']=116
man['g1']={'metodo':'eutils_automatico (esearch+esummary+efetch)','resolvidos':116,'nao_resolvidos':0,
 'descartados_auditoria':['22814126 (PMID trocado em vídeo externo: Yang 2012 Fitoterapia, não Cryan)',
  'rodada [AT] GPM 2026-09-09: 4 NÃO-INDEXADOS mantidos fora (Thomas 2021 bioRxiv; Towriss 2026 preprint; Xia 2025; Zhang 2026) — sem fonte forjada']}
g2=man['g2']
g2['eligible']=g2['eligible']+9   # OB: Aburto, Carabotti, Agus, Bosi, Chen2021, Cheng, Ohara, Stanimirov, Baj
g2['redirecionado_mecanistico']=g2['redirecionado_mecanistico']+18
g2['redirecionado_clinico']=g2['redirecionado_clinico']+4  # EC: Tulkens, Lin, Zhou, ZhangQ
er=g2['evid_role']
er['preclinical_mechanistic']=er.get('preclinical_mechanistic',0)+18
er['human_clinical']=er.get('human_clinical',0)+4
er['review']=er.get('review',0)+9
man['g3']['vinculos_n2']=71; man['g3']['CONFIRMADO']=66
man['g3']['abstracts_lidos_alto_risco']=man['g3'].get('abstracts_lidos_alto_risco',13)+30
man['vinculos_n2']=71
man['palavras_canonica']=9356
man['versao']='2.6'
man['corte_literatura']='busca ativa com ferramenta externa E-utilities/PubMed; corte 2026-09-09'
man['pendencias_fase']=[
 'P-6: 2a verificacao independente (avaliador cego) dos claims de alto risco (FMT 42309058/41921871, metas 2026, Bravo vagotomia) — AMPLIADA na rodada [AT] 2026-09-09: incluir as levas [AT] de TODAS as bibliotecas B1–B16 ao fim da rodada']
man['historico_correcoes'].append({
 'data':'2026-09-09','campo':'rodada_AT_GPM_B7',
 'erro_anterior':'V1 (85 refs) sem a leva auditada do insumo externo GPM B7 (anexo 196 refs + Carabotti 2015)',
 'correcao':'auditoria ref a ref (G1 eutils 192/196; 0 falsos positivos; 4 não-indexados fora; 8 sobreposições); matriz de decisão 31 ENTRA/131 BAIXO/26 EXC; fusão V2 com 116 refs, regras B7-CAUSAL-01/02/03 fixadas em CONTROVÉRSIAS; tríade sincronizada (pmids 116, vínculos 71, ledger 78)',
 'acao_downstream':'portões oficiais revalidados (gate P-5, framework auditoria, checklist); P-4 adendo V2'})
json.dump(man, open(mj,'w'), ensure_ascii=False, indent=1)

# trilha AT
trilha={'ciclo':'[AT] GPM B7 — Eixo Intestino-Cérebro','data':'2026-09-09','artefato':'CANONICA v2 (116 refs; de 85)',
 'insumos':['GPM_B7_EixoIntestinoCerebro.md (oficial)','BRIEFING_B7_EIXO_INTESTINO_CEREBRO_RODADA0.md','BRIEFING_CONSOLIDADO_B7_v1.md','Artigos cientificos do mecanismo B7 (anexo 196 DOIs + Carabotti sem DOI)','Resumo do insumo para B7 Chatgpt.md (34 claims B7.SM02 + 3 regras de ouro)'],
 'auditoria':{'anexo_itens':197,'g1_resolvidos':192,'nao_indexados':['Thomas 2021 (bioRxiv)','Towriss 2026 (preprint)','Xia 2025','Zhang 2026'],
  'falsos_positivos':0,'sobreposicao_com_V1':8,'masters_gpm':{'total':30,'ja_vigentes':7,'novas':23},
  'fila_decisao':188,'entra':31,'baixo':131,'exc':26},
 'regras_fixadas':['B7-CAUSAL-01','B7-CAUSAL-02','B7-CAUSAL-03'],
 'artefatos':['producao/insumos/RELATORIO_AUDITORIA_MATRIZ_B7.md','producao/insumos/matriz_b7_decisao.json','producao/insumos/matriz_b7_g1.json','producao/insumos/b7_fila_real.json','producao/insumos/b7_at_efetch.json','producao/insumos/b7_trechos_ancora.json'],
 'pendencias':['P-6 (2ª verificação cega, Via 2) — PENDENTE ao fim da rodada 16/16, cobrindo todas as levas [AT]']}
json.dump(trilha, open(f'{BASE}/producao/04_AT_ciclo_2026-09-09.json','w'), ensure_ascii=False, indent=1)
print('TRÍADE OK: pmids',old_p,'→',len(pjx),'| vínculos',old_v,'→',len(vjx),'| ledger',old_l,'→',len(ljx))
print('manifesto v2 gravado; trilha at gravada')
