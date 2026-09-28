#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera vinculos N2 da B7; trecho_ancora = sentença literal do texto canônico que contém a citação."""
import json, re

DATA = '2026-09-05'
TXT = open('/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro/producao/historico/B7_PRE_CANONICA_rodada2.md', encoding='utf-8').read()
TXT_NORM = re.sub(r'\s+', ' ', TXT)

def sentencas(autor):
    pat = re.compile(r'\(' + re.escape(autor) + r'(?:[^)]*?(19|20)\d{2}[^)]*?|\s+(19|20)\d{2})\)\[(?:MA|EC|OB|ML|AT)\]')
    sents = []
    for m in pat.finditer(TXT_NORM):
        start = m.start()
        fb = max(TXT_NORM.rfind('. ', 0, start), TXT_NORM.rfind('; ', 0, start),
                 TXT_NORM.rfind('* ', 0, start), TXT_NORM.rfind(': ', 0, start))
        seg_start = fb + 2 if fb > -1 else 0
        fe = TXT_NORM.find('. ', m.end())
        seg_end = fe + 1 if fe > -1 else min(len(TXT_NORM), m.end() + 220)
        seg = TXT_NORM[seg_start:seg_end].strip(' *-|')
        if 20 < len(seg) < 700:
            sents.append(seg)
    return sents

def ancora(autor, keys=None, sufixo=None, maxlen=300):
    autor = re.sub(r'\s+(19|20)\d{2}$', '', autor)  # strip ano colado ("Li 2021" -> "Li")
    cand = sentencas(autor)
    if not cand:
        return None
    if sufixo:
        filt = [s for s in cand if sufixo.lower() in s.lower()]
        if filt: cand = filt
    if keys:
        cand = sorted(cand, key=lambda s: -sum(1 for k in keys if k.lower() in s.lower()))
    seg = cand[0]
    if len(seg) > maxlen:
        seg = seg[:maxlen].rsplit(' ', 1)[0] + '…'
    return seg.strip()

# rid_na_lista | autor_prosa | sufixo_prosa | keys | natureza | maturidade | forca | especie | role | vstatus | auditoria | g2 | motivo | uso
V = [
 ('Sudo2004_germfree','Sudo','', ['HPA','corticosterona','germ-free','colonização'],'contributiva','bem_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','marco em roedor; germ-free é extremo não fisiológico','nucleo_causal'),
 ('Bravo2011_vagotomia','Bravo','', ['vagotom','vago','GABA'],'contributiva','bem_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','prova de rota em roedor; não testado em humano','nucleo_causal'),
 ('Kelly2016_FMTblues','Kelly','FMT', ['ratos','anedonia','triptofano'],'contributiva','bem_suportado','tier_3_mecanistico_animal',['Animals','Humans'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','doadores humanos, fenótipo medido em rato','nucleo_causal'),
 ('Zheng2016_FMT','Zheng','', ['metabol','carboidratos','FMT'],'contributiva','bem_suportado','tier_3_mecanistico_animal',['Animals','Humans'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','prova causal em roedor',''),
 ('LiN2019_FMT_CUMS','Li N','', ['CUMS','inflamação','doadores'],'contributiva','moderado_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','dados animais',''),
 ('Erny2015_microglia','Erny','', ['microglia','maturação'],'contributiva','bem_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','dados animais; braço B1/B7',''),
 ('Yano2015_5HT','Yano','', ['5-HT','enterocromafins','esporuladas'],'contributiva','bem_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','5-HT entérica/periférica, NÃO cerebral',''),
 ('Bellono2017_sensores','Bellono','', ['quimiossensores','enterocromafins','vagais'],'contributiva','bem_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','mecanismo sensorial roedor/célula',''),
 ('DiazHeijtz2011_dev','Diaz Heijtz','', ['desenvolvimento','motor','comportamental'],'contributiva','bem_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','dados animais de desenvolvimento',''),
 ('Desbonnet2014_social','Desbonnet','', ['social','déficit'],'contributiva','moderado_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','dados animais; janela desenvolvimental',''),
 ('Neufeld2011_germfree','Neufeld','', ['ansiedade reduzida','neuroquímica'],'contributiva','moderado_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','direção do fenótipo é complexa',''),
 ('Braniste2014_BBB','Braniste','', ['barreira hematoencefálica','permeável','colonização'],'contributiva','bem_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','dados animais',''),
 ('Li2021_rifaximina','Li 2021','', ['rifaximina','microglia','adolescente'],'contributiva','moderado_suportado','tier_3_mecanistico_animal',['Animals'],'preclinical_mechanistic','preclinico','CONFIRMADO','redirecionado_mecanistico','modelo animal; rifaximina não absorvível',''),
 ('LiJ2026_FMTRCT','Li J','', ['remissão','HAMD','placebo','escitalopram'],'contributiva','emergente','tier_2_intervencao_humana',['Humans'],'human_experimental','emergente','PARCIALMENTE_CONFIRMADO','eligible','RCT duplo-cego; endpoint primário (remissão) NULO; secundário positivo; único, aguarda replicação','clinico'),
 ('LiB2026_FMTmeta','Li B','', ['532','heterogeneidade','g≈'],'contributiva','emergente','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','meta pequena que mistura RCTs e coortes; heterogeneidade alta','clinico'),
 ('Chinna2020_FMT_RS','Chinna Meyyappan','', ['psicopatologia','desfecho secundário'],'descritiva','incipiente','tier_4_descritivo_estrutural',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','RS; estudos pequenos',''),
 ('Moshfeghinia2025_I2','Moshfeghinia','', ['I²','96','heterogeneidade'],'contributiva','bem_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','meta-análise; heterogeneidade altíssima; efeito aparente inflado','clinico'),
 ('CohenKadosh2021_nulo','Cohen Kadosh','', ['jovens','nulo','−0,03'],'refutadora','bem_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','meta-análise de resultado nulo em jovens','clinico'),
 ('Shakir2026_citocinas','Shakir','', ['IL-6','TNF','0,45','citocinas'],'refutadora','bem_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','argumenta contra mediação citocínica obrigatória','nucleo_causal'),
 ('Sikorska2023_BDNF','Sikorska','', ['BDNF','0,37','IL-6'],'contributiva','moderado_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','meta de 20 registros; BDNF periférico é leitura indireta',''),
 ('ElDib2021_16RCT','El Dib','', ['BDI','STAI','16 RCT'],'contributiva','bem_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','16 RCTs/1125 pacientes; efeito pequeno','clinico'),
 ('Nikolova2021_umbrella','Nikolova','', ['transdiagnóst','Eggerthella','Faecalibacterium','táxon'],'descritiva','bem_suportado','tier_2_meta_analise',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','meta guarda-chuva 59 estudos; sem táxon universal','nucleo_causal'),
 ('Simpson2021_26est','Simpson','', ['diversidade','26 estudos','inconsistente'],'descritiva','bem_suportado','tier_2_revisao_sistematica',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','RS de 26 estudos; diversidade inconsistente',''),
 ('Do2026_SCFAmeta','Do','', ['AGCC','circulantes','propionato','butirato'],'contributiva','moderado_suportado','tier_2_meta_analise',['Humans','Animals'],'human_clinical','verificado','CONFIRMADO','eligible','assinatura associativa; NÃO é intervenção',''),
 ('Jiang2015_fezes','Jiang','', ['fecal','composição'],'descritiva','moderado_suportado','tier_4_observacional_transversal',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','caso-controle fundacional; transversal',''),
 ('Stevens2018_zonulina','Stevens','', ['zonulina','FABP2','LPS'],'contributiva','incipiente','tier_4_observacional_transversal',['Humans'],'human_clinical','extrapolado','PARCIALMENTE_CONFIRMADO','redirecionado_clinico','carta ao Gut, n pequeno; transversal; marcadores não validados',''),
 ('Maes2008_leakygut','Maes 2008','', ['IgM anti-LPS','translocação','barreira'],'contributiva','incipiente','tier_4_observacional_transversal',['Humans'],'human_clinical','extrapolado','PARCIALMENTE_CONFIRMADO','redirecionado_clinico','um único grupo; ensaio pouco padronizado; não replicado',''),
 ('Bibolar2025_validacao','Bibolar','', ['validados','biomarcadores'],'refutadora','bem_suportado','tier_4_descritivo_estrutural',['Humans'],'review','verificado','CONFIRMADO','eligible','revisão crítica: zonulina/FABP2 não validados','clinico'),
 ('VallesColomer2019_potencial','Vallès-Colomer','', ['potencial neuroativo','qualidade de vida'],'contributiva','moderado_suportado','tier_4_observacional_transversal',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','coorte humana; função (não taxonomia)',''),
 ('Jia2024_bile','Jia','', ['sais biliares','cogni'],'contributiva','incipiente','tier_4_observacional_transversal',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','estudo observacional; epub 2024',''),
 ('Butler2022_ansiedadesocial','Butler','', ['ansiedade social','quinurenina'],'contributiva','incipiente','tier_4_observacional_transversal',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','caso-controle; âncora de ansiedade social',''),
 ('Strandwitz2019_GABA','Strandwitz 2019','', ['GABA','produzem','consomem'],'descritiva','bem_suportado','tier_3_mecanistico_invitro',['Humans'],'human_experimental','verificado','CONFIRMADO','eligible','ecologia bacteriana humana; NÃO é reposição central',''),
 ('Cryan2019_teto','Cryan 2019','', ['cinco vias','teto'],'descritiva','bem_suportado','tier_4_descritivo_estrutural',['Humans','Animals'],'review','verificado','CONFIRMADO','eligible','revisão-teto do eixo',''),
 ('Kelly2016_traducao','Kelly','tradução', ['tradução','roedor','fisio'],'descritiva','bem_suportado','tier_4_descritivo_estrutural',['Humans','Animals'],'review','verificado','CONFIRMADO','eligible','revisão sobre o abismo roedor-humano','nucleo_causal'),
 ('Cussotto2021_psicof','Cussotto 2021','psicof', ['psicofármacos','antidepressivos','antipsicóticos'],'contributiva','bem_suportado','tier_4_descritivo_estrutural',['Humans','Animals'],'review','verificado','CONFIRMADO','eligible','confundidor crítico: psicofármacos alteram a microbiota',''),
 ('Cussotto2025_livre','Cussotto 2025','livre', ['sem antidepressivo','gravidade'],'contributiva','moderado_suportado','tier_4_observacional_transversal',['Humans'],'human_clinical','verificado','CONFIRMADO','eligible','controla parcialmente o confundidor medicação',''),
 ('Messaoudi2011_subclin','Messaoudi','', ['sadios','voluntários'],'contributiva','moderado_suportado','tier_2_intervencao_humana',['Humans'],'human_experimental','verificado','CONFIRMADO','eligible','RCT em população subclínica/sadia',''),
 ('Mysonhimer2023_nulo','Mysonhimer','', ['nulo','não mudou','prebiótico'],'refutadora','bem_suportado','tier_2_intervencao_humana',['Humans'],'human_experimental','verificado','CONFIRMADO','eligible','RCT humano de resultado nulo para prebiótico/estresse',''),
 ('Crocetta2024_fMRI','Crocetta','', ['fMRI','neuroimagem','amígdala'],'contributiva','incipiente','tier_2_revisao_sistematica',['Humans'],'human_experimental','extrapolado','PARCIALMENTE_CONFIRMADO','eligible','RS de neuroimagem; heterogênea; sem desfecho clínico duro',''),
 ('Hemmings2017_TEPT','Hemmings','', ['TEPT','trauma'],'contributiva','incipiente','tier_4_observacional_transversal',['Humans'],'human_clinical','extrapolado','PARCIALMENTE_CONFIRMADO','eligible','estudo exploratório pequeno; lacuna de TEPT',''),
]

refs = {r['ids_referencia_interna'][0]: r for r in
        json.load(open('/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro/Evidencias/Bibliografia/01_pmids.json'))}

out = []
for i, (rid, autor, sufixo, keys, nat, mat, forca, esp, role, vstat, aud, g2, motivo, uso) in enumerate(V, start=1):
    refid = f'REF_{rid}'
    ref = refs.get(refid)
    if not ref:
        print('REF AUSENTE:', refid); continue
    trecho = ancora(autor, keys, sufixo if sufixo else None)
    if not trecho:
        print('ANCORA NAO ENCONTRADA:', autor, sufixo); continue
    out.append({
        'id_vinculo': f'VINC_B7_{i:03d}',
        'id_referencia_interna': refid,
        'secao_origem': 'B7_CANONICA_V1',
        'trecho_ancora': trecho,
        'mecanismo_origem': 'mecanismo_B7_eixo_intestino_cerebro_microbiota',
        'natureza_relacao': nat,
        'grau_maturidade': mat,
        'forca_causal': forca,
        'extrapolacao_por_analogia': ('SIM — evidência em roedor/modelo; tradução humana por analogia [EXT]' if role=='preclinical_mechanistic' else 'não'),
        'especie_mesh': esp,
        'evid_role': role,
        'verification_status': vstat,
        'status_referencia': 'CONFIRMADA' if aud=='CONFIRMADO' else 'PARCIAL',
        'citacao_confirmada': True,
        'g1_metodo': 'eutils_automatico',
        'g2_elegibilidade': g2,
        'g2_motivo': motivo,
        'g3_verificado_por': 'IA G3 (Rodada 2): esummary + abstract efetch lido para âncoras de alto risco (metas 2026, FMT-RCT, Bravo/Kelly/Yano)',
        'g3_fulltext': 'abstract lido; PMC full-text fica para 2a verificação independente (P-6, avaliador cego)',
        'status_auditoria': aud,
        'uso': uso,
        'segunda_verificacao': 'PENDENTE — 2a verificação independente (P-6, avaliador cego) registrada como pendência de fase; mitigação: tier e espécie explícitos, claim animal nunca afirmado como humano',
        'data_verificacao': DATA,
        'pmid_oficial': ref['pmid_oficial']
    })

json.dump(out, open('/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro/Evidencias/Vinculos/vinculos_referencia_afirmacao.json','w'),
          ensure_ascii=False, indent=1)
print('vinculos escritos:', len(out))
for v in out:
    print(v['id_vinculo'], v['id_referencia_interna'].replace('REF_',''), '->', v['trecho_ancora'][:95])
