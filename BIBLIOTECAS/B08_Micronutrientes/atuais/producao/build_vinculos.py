#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera vinculos N2 da B8; trecho_ancora = sentença literal do texto canônico."""
import json, re

DATA = '2026-09-06'
TXT = open('/home/user/BIBLIOTECAS/B08_Micronutrientes/producao/historico/B8_PRE_CANONICA_rodada2.md', encoding='utf-8').read()
TXT_NORM = re.sub(r'\s+', ' ', TXT)

def sentencas(autor):
    pat = re.compile(r'\(' + re.escape(autor) + r'(?:[^)]*?(19|20)\d{2}[^)]*?|\s+(19|20)\d{2})\)\[(?:MA|EC|OB|ML|AT)\]')
    out = []
    for m in pat.finditer(TXT_NORM):
        s = m.start()
        fb = max(TXT_NORM.rfind('. ',0,s), TXT_NORM.rfind('; ',0,s), TXT_NORM.rfind('* ',0,s), TXT_NORM.rfind(': ',0,s))
        ss = fb+2 if fb>-1 else 0
        fe = TXT_NORM.find('. ', m.end())
        se = fe+1 if fe>-1 else min(len(TXT_NORM), m.end()+220)
        seg = TXT_NORM[ss:se].strip(' *-|')
        if 20 < len(seg) < 700: out.append(seg)
    return out

def ancora(autor, keys=None, sufixo=None, maxlen=300):
    autor = re.sub(r'\s+(19|20)\d{2}$', '', autor)  # strip ano colado
    cand = sentencas(autor)
    if not cand: return None
    if sufixo:
        f = [s for s in cand if sufixo.lower() in s.lower()]
        if f: cand = f
    if keys:
        cand = sorted(cand, key=lambda s: -sum(1 for k in keys if k.lower() in s.lower()))
    seg = cand[0]
    if len(seg) > maxlen: seg = seg[:maxlen].rsplit(' ',1)[0] + '…'
    return seg.strip()

# rid | autor_prosa | sufixo | keys | natureza | maturidade | forca | especie | role | vstatus | auditoria | g2 | motivo | uso
V = [
 ('Jacka2017_SMILES','Jacka 2017','', ['SMILES','d=−1,16','dieta','MADRS'],'contributiva','bem_suportado','tier_2_intervencao_humana',['Humans'],'human_experimental','verificado','CONFIRMADO','eligible','RCT single-blind de modificação dietética na TDM','clinico'),
 ('Lassale2019_dieta_meta','Lassale 2019','', ['dose-gradiente','Mediterr','padrão'],'contributiva','bem_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','meta observacional; confundimento residual do usuário saudável','nucleo_causal'),
 ('Okereke2020_VITAL_D3','Okereke 2020','', ['VITAL','D3','não preveniu','HR'],'refutadora','bem_suportado','tier_2_intervencao_humana',['Humans'],'human_experimental','verificado','CONFIRMADO','eligible','RCT ~18 mil prevenção; NULO (HR 0,97)','nucleo_causal'),
 ('Okereke2021_VITAL_n3','Okereke 2021','', ['ômega-3','VITAL','não preveniu'],'refutadora','bem_suportado','tier_2_intervencao_humana',['Humans'],'human_experimental','verificado','CONFIRMADO','eligible','RCT ~18 mil prevenção; ômega-3 nulo/não-benéfico (HR 1,13)','nucleo_causal'),
 ('Markun2021_B12_nulo','Markun 2021','', ['B12','não-deficientes','nula','16 RCT'],'refutadora','bem_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','16 RCTs/6276; B12 sem efeito em não-deficientes','nucleo_causal'),
 ('Mikola2023_D_meta','Mikola 2023','', ['I²','88','GRADE','g≈−0,32','g=−0,317'],'contributiva','bem_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','41 RCTs; g=−0,317, I²=88%, GRADE muito baixa','clinico'),
 ('Ghaemi2024_D_dose','Ghaemi 2024','', ['ansiedade','curto prazo','deficientes'],'contributiva','moderado_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','31 RCTs; efeito em sintomáticos; ansiedade SEM efeito; some no longo prazo',''),
 ('Sajjadi2022_Se_meta','Sajjadi 2022','', ['selênio','I²','98','sem diferença'],'refutadora','bem_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','soro sem diferença (I²=98%); sinal só pós-parto por ingestão',''),
 ('Rajizadeh2017_Mg_RCT','Rajizadeh 2017','', ['hipomagnesemia','duplo-cego','BDI','deficiência'],'contributiva','moderado_suportado','tier_2_intervencao_humana',['Humans'],'human_experimental','verificado','CONFIRMADO','eligible','RCT cego pequeno (n=60) SÓ em deficientes; prova de conceito','clinico'),
 ('Tarleton2017_Mg_RCT_aberto','Tarleton 2017','', ['aberto','GAD-7','PHQ-9'],'contributiva','incipiente','tier_2_intervencao_humana',['Humans'],'human_experimental','extrapolado','PARCIALMENTE_CONFIRMADO','eligible','RCT ABERTO/não-cego; GAD-7 secundário; ressalva de cegueira',''),
 ('Sartori2012_Mg_ansiedade','Sartori 2012','', ['ansiedade','HPA','camundongo','dieta pobre'],'contributiva','bem_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','prova pré-clínica direta; Mg/HPA/ansiedade em roedor','nucleo_causal'),
 ('Kemp2024_Fe_n3_dev','Kemp 2024','', ['ferro','n-3','monoaminas','desenvolvimento'],'contributiva','moderado_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','carência materna ferro/n-3; prole; janela desenvolvimental',''),
 ('Kim2014_ferro','Kim 2014','', ['ferro','tirosina','triptofano','hidroxilase','BH4'],'descritiva','bem_suportado','tier_4_descritivo_estrutural',['Humans','Animals'],'review','verificado','CONFIRMADO','eligible','revisão mecanística; ferro cofator de TH/TPH; deficiência sem anemia',''),
 ('Bottiglieri2000_homocisteina','Bottiglieri 2000','', ['homocisteína','SAM','monoaminas','folato'],'contributiva','moderado_suportado','tier_4_observacional_transversal',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','estudo humano transversal de marcadores na depressão','nucleo_causal'),
 ('Gaysina2008_MTHFR_nulo','Gaysina 2008','', ['MTHFR','SEM','nula','DeCC'],'refutadora','bem_suportado','tier_4_observacional_transversal',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','DeCC + meta SEM associação; conflita com Wu/Rai','nucleo_causal'),
 ('Wu2013_MTHFR_pos','Wu 2013','', ['MTHFR','C677T','associação'],'contributiva','incipiente','tier_2_meta_analise',['Humans'],'human_clinical','extrapolado','PARCIALMENTE_CONFIRMADO','eligible','meta positiva; conflita com Gaysina; heterogênea',''),
 ('Papakostas2012_LMethylfol','Papakostas 2012','', ['L-metilfolato','ISRS','adjuvante','resistente'],'contributiva','moderado_suportado','tier_2_intervencao_humana',['Humans'],'human_experimental','verificado','CONFIRMADO','eligible','L-metilfolato adjuvante em respondedores inadequados a ISRS','clinico'),
 ('Carnegie2024_MR_TDM','Carnegie 2024','', ['Mendelian','MR','nulo','ferro','cobre'],'contributiva','emergente','tier_4_descritivo_estrutural',['Humans'],'human_clinical','emergente','PARCIALMENTE_CONFIRMADO','eligible','MR tradicional NULO; ferro/cobre/25OHD sugestivos na recorrente; MR≠RCT; excesso pode fazer mal','nucleo_causal'),
 ('Fang2025_MR_ansiedade','Fang 2025','', ['ansiedade','MR','colocalização'],'contributiva','emergente','tier_4_descritivo_estrutural',['Humans'],'human_clinical','emergente','PARCIALMENTE_CONFIRMADO','eligible','MR + colocalização bayesiana para ansiedade; causalidade potencial',''),
 ('Anglin2013_D_meta','Anglin 2013','', ['vitamina D','deficiência','associação'],'contributiva','bem_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','meta de associação deficiência-D ↔ depressão',''),
 ('Kouba2022_D_mecanismo','Kouba 2022','', ['VDR','BDNF','esteroide nuclear'],'descritiva','bem_suportado','tier_4_descritivo_estrutural',['Humans','Animals'],'review','verificado','CONFIRMADO','eligible','revisão mecanística do VDR/vitamina D',''),
 ('Swardfager2013_Zn_review','Swardfager 2013','', ['zinco','NMDA','plasticidade'],'descritiva','bem_suportado','tier_4_descritivo_estrutural',['Humans','Animals'],'review','verificado','CONFIRMADO','eligible','revisão do zinco (NMDA extracelular, GABA, plasticidade)',''),
 ('Johnson2013_Se_agua','Johnson 2013','', ['selênio','água','GPX1','ambiental'],'contributiva','incipiente','tier_4_observacional_transversal',['Humans'],'human_clinical','extrapolado','PARCIALMENTE_CONFIRMADO','eligible','exposição AMBIENTAL (água) × GPX1; não é suplemento',''),
 ('Su2018_n3_ansiedade','Su 2018','', ['ômega-3','ansiedade','g≈0,37','0,374'],'contributiva','moderado_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','meta de ansiedade; efeito maior em diagnóstico clínico/dose alta',''),
 ('Young2019_Bvit_meta','Young 2019','', ['B-vitaminas','ansiedade NS','p=0,07'],'refutadora','bem_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','estresse +, depressão p=0,07, ANSIEDADE NS',''),
 ('Galizia2016_SAMe_cochrane','Galizia 2016','', ['SAMe','Cochrane','limitado'],'contributiva','incipiente','tier_2_revisao_sistematica',['Humans'],'human_clinical','extrapolado','PARCIALMENTE_CONFIRMADO','eligible','Cochrane; evidência limitada/heterogênea',''),
 ('Johnstone2020_multinutri_meta','Johnstone 2020','', ['multinutrientes','microfórmula','heterogêneo'],'contributiva','incipiente','tier_2_meta_analise',['Humans'],'human_clinical','extrapolado','PARCIALMENTE_CONFIRMADO','eligible','sinal modesto, não atribuível a um nutriente',''),
 ('Varga2025_Mg_review','Varga 2025','', ['magnésio','enxaqueca','cognição'],'descritiva','bem_suportado','tier_4_descritivo_estrutural',['Humans'],'review','verificado','CONFIRMADO','eligible','revisão ampla de Mg',''),
 ('Phelan2018_Mg_inconclusivo','Phelan 2018','', ['inconclusivo','magnésio','soro'],'refutadora','moderado_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','revisão/meta inconclusiva para Mg e humor',''),
 ('Gupta2025_anemia','Gupta 2025','', ['anemia','inespecífica'],'descritiva','moderado_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','anemia×depressão é inespecífica (vários tipos, não só ferro)',''),
 ('Han2025_complexoB','Han 2025','', ['Wernicke','pelagra','complexo B','neuropsiquiátricas'],'descritiva','bem_suportado','tier_4_descritivo_estrutural',['Humans'],'review','verificado','CONFIRMADO','eligible','manifestações neuropsiquiátricas das deficiências do complexo B',''),
 ('Parletta2019_HELFIMED','Parletta 2019','', ['Mediterr','peixe','HELFIMED'],'contributiva','moderado_suportado','tier_2_intervencao_humana',['Humans'],'human_experimental','verificado','CONFIRMADO','eligible','RCT Mediterrâneo+óleo de peixe (réplica de SMILES)',''),
 ('Sarris2022_WFSBP_diretriz','Sarris 2022','', ['diretriz','WFSBP','CANMAT','hierarquia'],'descritiva','bem_suportado','tier_4_descritivo_estrutural',['Humans'],'review','verificado','CONFIRMADO','eligible','diretriz clínica; hierarquia de evidência de nutracêuticos',''),
 ('Davarinejad2026_elementos','Davarinejad 2026','', ['Zn','Fe','Cu','cobre alto'],'contributiva','incipiente','tier_4_observacional_transversal',['Humans'],'human_clinical','extrapolado','PARCIALMENTE_CONFIRMADO','eligible','elementos séricos; Cu alto = redistribuição inflamatória; 2026',''),
]

refs = {r['ids_referencia_interna'][0]: r for r in
        json.load(open('/home/user/BIBLIOTECAS/B08_Micronutrientes/Evidencias/Bibliografia/01_pmids.json'))}

out=[]
for i,(rid,autor,sufixo,keys,nat,mat,forca,esp,role,vstat,aud,g2,motivo,uso) in enumerate(V, start=1):
    refid=f'REF_{rid}'
    ref=refs.get(refid)
    if not ref: print('REF AUSENTE:',refid); continue
    trecho=ancora(autor, keys, sufixo or None)
    if not trecho: print('ANCORA NAO ENCONTRADA:',autor,sufixo); continue
    out.append({
      'id_vinculo':f'VINC_B8_{i:03d}','id_referencia_interna':refid,'secao_origem':'B8_CANONICA_V1',
      'trecho_ancora':trecho,'mecanismo_origem':'mecanismo_B8_deficiencias_micronutrientes',
      'natureza_relacao':nat,'grau_maturidade':mat,'forca_causal':forca,
      'extrapolacao_por_analogia':('SIM — evidência em roedor/modelo; tradução humana por analogia [EXT]' if role=='preclinical_mechanistic' else 'não'),
      'especie_mesh':esp,'evid_role':role,'verification_status':vstat,
      'status_referencia':'CONFIRMADA' if aud=='CONFIRMADO' else 'PARCIAL',
      'citacao_confirmada':True,'g1_metodo':'eutils_automatico','g2_elegibilidade':g2,'g2_motivo':motivo,
      'g3_verificado_por':'IA G3 (Rodada 2): esummary + abstract efetch lido para âncoras de alto risco (VITAL D3/n3, B12 Markun, selênio Sajjadi, Mg Rajizadeh/Tarleton, MR Carnegie, SMILES, Ghaemi/Mikola)',
      'g3_fulltext':'abstract lido; PMC full-text fica para 2a verificação independente (P-6, avaliador cego)',
      'status_auditoria':aud,'uso':uso,
      'segunda_verificacao':'PENDENTE — 2a verificação independente (P-6, avaliador cego) registrada como pendência de fase; mitigação: tier/espécie explícitos, nulo dos grandes RCTs destacado, claim animal nunca afirmado como humano',
      'data_verificacao':DATA,'pmid_oficial':ref['pmid_oficial']})

json.dump(out, open('/home/user/BIBLIOTECAS/B08_Micronutrientes/Evidencias/Vinculos/vinculos_referencia_afirmacao.json','w'),
          ensure_ascii=False, indent=1)
print('vinculos escritos:', len(out))
EOF_DUMMY = None
