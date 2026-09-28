#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construi 01_pmids.json da B14 (240 ancoras mecanisticas; 15 ruidos bloco N a parte).
Refinamento: classificacao por tipo do Briefing + overrides cientificos; sobrenome canonico."""
import json,re,unicodedata
from collections import Counter
def sem(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c))
META=json.load(open('/home/user/BIBLIOTECAS/B14_Neuroesteroides/producao/g1_resolvidos.json'))
RUIM=set(json.load(open('/tmp/b14_ruido.json')))

# ---- overrides cientificos: pmid -> (sobrenome canonico, ano, role, aliases extras) ----
# role: review=OB / human_clinical=EC / preclinical_mechanistic=ML
OV={
 '2422758':('MAJEWSKA','1986','preclinical_mechanistic',[]),           # Science classico (bifasic PAM discovery; celula/animal)
 '1852011':('PURDY','1991','preclinical_mechanistic',[]),              # Purdy PNAS estresse->ALLO (rato)
 '7482994':('LAMBERT','1995','review',[]),
 '15959466':('BELELLI','2005','review',[]),                            # Belelli/Lambert Nat Rev Neurosci teto
 '18667149':('MAGUIRE','2008','review',['MODY']),                       # Maguire & Mody Neuron
 '34561029':('ANTONOUDIOU','2022','preclinical_mechanistic',['MAGUIRE']), # BLA theta transespecies
 '28991263':('MILLER','2017','preclinical_mechanistic',[]),            # cristalografia Nat Struct Mol Biol
 '37607940':('LEGESSE','2023','preclinical_mechanistic',[]),           # cryo-EM Nat Commun
 '37730991':('SUN','2023','preclinical_mechanistic',['GOUAUX']),       # cryo-EM Nature
 '39843743':('ZHOU','2025','preclinical_mechanistic',[]),              # estruturas humanas Nature
 '9501247':('UZUNOVA','1998','human_clinical',[]),                     # ISRS elevam NS no liquor (humano CSF)
 '16934764':('RASMUSSON','2006','human_clinical',[]),                  # ALLO baixa liquor TEPT mulheres
 '29727810':('PINELES','2018','human_clinical',[]),                    # bloqueio conversao plasma TEPT
 '12578433':('STROHLE','2003','human_clinical',[]),                    # panico Arch Gen Psychiatry
 '12798975':('BRAMBILLA','2003','human_clinical',[]),                  # panico Psychiatry Res
 '30529908':('RASMUSSON','2019','human_clinical',[]),                  # CSF TEPT homens
 '28619476':('KANES','2017','human_clinical',[]),                      # brexanolone fase2 Lancet
 '30177236':('MELTZERBRODY','2018','human_clinical',['MELTZER']),       # brexanolone fase3 Lancet
 '34190962':('DELIGIANNIDIS','2021','human_clinical',[]),              # zuranolona DPP JAMA
 '37132201':('CLAYTON','2023','human_clinical',[]),                    # zuranolona TDM MOUNTAIN AJP
 '36811520':('CLAYTON','2023','human_clinical',[]),
 '40562419':('WILSON','2025','review',[]),                             # Cochrane DPP
 '10200751':('WOLKOWITZ','1999','human_clinical',[]),                  # DHEA RCT Am J Psychiatry
 '30427999':('WALTHER','2019','review',[]),                            # testosterona/depressao meta JAMA Psych
 '11386980':('SOARES','2001','human_clinical',[]),                     # estradiol perimenopausa RCT
 '29322164':('GORDON','2018','human_clinical',[]),                     # estradiol transdermico RCT JAMA
 '26018333':('SCHMIDT','2015','human_clinical',[]),                    # retirada estradiol RCT
 '31693131':('JOFFE','2020','human_clinical',[]),                      # variabilidade estradiol JCEM
 '34097071':('GUERRIERI','2021','human_clinical',[]),                  # Dex/CRH perimenopausa
 '39841836':('CADEDDU','2025','preclinical_mechanistic',[]),           # 5a-redutase tipo2 PFC macho Sci Adv
 '29544191':('MOSHER','2018','human_clinical',[]),                     # deficiencia SRD5A2 humano
 '24011224':('MODOL','2014','preclinical_mechanistic',[]),             # finasterida neonatal animal
 '27784541':('IRWIG','2014','review',[]),                              # finasterida seguranca
 '25871957':('IRWIG','2015','review',[]),
 '33515765':('SCHUBERT','2021','human_clinical',[]),                   # PET TSPO TDM Biol Psych Cogn
 '35444254':('RUPPRECHT','2022','review',[]),                          # TSPO Mol Psychiatry
 '24756763':('CROWLEY','2014','review',['SCHULE']),                    # Crowley & Girdler (briefing: Schule)
 '17159334':('ESER','2006','review',[]),                              # pub 2006
 '34506047':('REDDY','2022','review',[]),                             # pub 2022
 '32435660':('BELELLI','2020','review',[]),                           # pub 2020
 '37715106':('PATTERSON','2024','review',['MORROW']),                 # pub 2024
 '24385629':('VALLEE','2014','preclinical_mechanistic',['PIOMELLI','PIAZZA']),  # pregnenolona CB1-SSi Science
 '39716883':('BELELLI','2025','review',[]),                           # microbiota GABA Brain
 '40782954':('KENNEY','2025','preclinical_mechanistic',[]),           # puberdade sexo Brain Res
 '24917198':('BROWN','2014','human_clinical',[]),                     # pregnenolona bipolar RCT
 '11152391':('BICIKOVA','2000','human_clinical',[]),                  # PS alto soro
 '28319848':('BIXO','2017','human_clinical',[]),                      # sepranolona TDPM ECR
 '34597899':('BACKSTROM','2021','human_clinical',[]),                 # sepranolona ECR
 '26272051':('MARTINEZ','2016','human_clinical',[]),                  # inibicao 5a-redutase TDPM
 '11331087':('GIRDLER','2001','human_clinical',[]),                  # ALLO/reatividade PMDD Biol Psych
 '32435664':('HANTSOO','2020','review',[]),                          # PMDD sensibilidade
 '37059403':('HANTSOO','2023','review',[]),                          # PMDD genes->GABA teto
 '39511449':('SCHORETSANITIS','2025','human_clinical',[]),           # meta periparto Mol Psych
 '28278440':('OSBORNE','2017','human_clinical',[]),                  # ALLO gestacao prediz DPP
 '39885361':('OSBORNE','2025','human_clinical',[]),
 '37524978':('TAO','2023','preclinical_mechanistic',[]),             # mPOA retirada Nat Neurosci
 '28619359':('YANG','2017','preclinical_mechanistic',[]),            # retirada estrogenio amigdala
 '12574407':('KOKSMA','2003','preclinical_mechanistic',[]),          # oxitocina SON J Neurosci
 '12367609':('VICINI','2002','preclinical_mechanistic',[]),          # delecao delta Neuropharmacol
 '10804198':('SHEN','2000','preclinical_mechanistic',[]),            # PS modula transmissao J Neurosci
 '36449311':('DELIGIANNIDIS','2023','human_clinical',['ERRATA']),    # errata zuranolona JAMA
 '38244954':('MORROW','2024','review',[]),                          # TLR4/imune Neurosci Biobehav
 '38792602':('BALAN','2024','review',[]),                          # pregnanos TLR Life
 '41620430':('BALAN','2026','human_clinical',['OBUCKLEY']),         # brexanolona efeito sustentado
 '32435667':('ALMEIDA','2020','review',[]),                        # BDNF/neurotrofico Neurobiol Stress
 '34071053':('ALMEIDA','2021','review',[]),
 '33578758':('ALMEIDA','2021','review',[]),
 '28456011':('LOCCI','2017','review',['PINNA']),                   # Locci & Pinna TSPO/endocanabinoide
 '25309317':('PINNA','2014','preclinical_mechanistic',['RASMUSSON']), # ganaxolona modelo TEPT
 '40320133':('CASTANHEIRA','2025','review',[]),                    # antidepressivos rapidos
 '36168047':('LAMBERT','2023','preclinical_mechanistic',[]),        # EEG GABAkines
 '37499891':('WALTON','2023','review',['MAGUIRE']),                # tom afetivo
 '31649968':('ZORUMSKI','2019','review',[]),
 '40127877':('ZORUMSKI','2025','review',[]),
 '12510009':('RUPPRECHT','2003','review',[]),                      # revisao fundadora
 '37369775':('MAGUIRE','2024','review',[]),                        # teto 2024 Neuropsychopharmacology
 '34019980':('CHEN','2021','review',[]),                           # alopreg transtornos humor Pharmacol Res
 '32440589':('LIANG','2018','review',[]),                          # esteroidogenese StAR Chronic Stress
 '26681259':('PORCU','2016','review',[]),                          # alvos neuroesteroidogenese
 '21094889':('REDDY','2010','review',[]),
 '40732235':('FEDOTCHEVA','2025','review',[]),
 '25585035':('GORDON','2015','review',['SCHMIDT']),                # heuristica perimenopausa AmJPsych
 '38664491':('HAMIDOVIC','2024','human_clinical',[]),              # PHASE trajetorias TDPM
 '39601877':('KIMBALL','2025','human_clinical',[]),
 '31780185':('KIMBALL','2020','human_clinical',[]),
 '28786978':('NGUYEN','2017','review',[]),
 '12715262':('SUNDSTROM','2003','review',['BACKSTROM']),
 '23978486':('BACKSTROM','2014','review',[]),
 '24215796':('SCHULE','2014','review',[]),
 '23085210':('ZORUMSKI','2013','review',[]),
 '37543478':('LUSCHER','2023','review',[]),
 '30906252':('MAGUIRE','2019','review',[]),
 '30633900':('MODY','2019','review',[]),
 '31275559':('LUSCHER','2019','review',[]),
 '30204559':('POISBEAU','2018','review',[]),
 '25620535':('STEIN','2015','human_clinical',[]),                  # etifoxina vs alprazolam
 '33009629':('VICENTE','2020','human_clinical',[]),                # etifoxina vs clonazepam
 '39725124':('FISCHER','2025','preclinical_mechanistic',[]),       # etifoxina animal
 '32930419':('PEIXOTO','2020','review',[]),                        # DHEA meta
 '30124161':('PEIXOTO','2018','review',[]),
 '26036454':('MOCKING','2015','human_clinical',[]),
 '34375211':('CHRONISTER','2021','human_clinical',[]),
 '27108164':('KIMMEL','2016','human_clinical',[]),
 '42492846':('BRACCAGNI','2026','review',[]),
 '41718149':('RODRIGUEZCERDEIRA','2026','review',[]),
 '34171352':('AMIEL','2021','review',[]),
 '16554740':('WALF','2006','review',[]),
 '39448569':('KACZMARCZYK','2024','human_clinical',[]),
 '34517034':('HSU','2021','review',[]),
}

def role_de(tipo,tema):
    t=sem(tipo+' '+tema).lower()
    if any(k in t for k in ['revis','review','meta','editorial','perspectiv','posiçao','posicao','capitulo',
                            'cocrane','cochrane','sistematica','histórica','historica','narrativ','rs ','rs/']):
        return 'review'
    if any(k in t for k in ['roedor','rat','rato','camundong','mouse','knockout','knock-in','knock in','deleç',
                            'delecao','animal','ko ','in vitro','cryo-em','cryo em','cristalogr','estrutural',
                            'eletrofisiolog','modelo','ovariectom','optogen','transesp','sprague','wistar',
                            'mecanismo','mecanística','mecanistica','básico','basico']):
        return 'preclinical_mechanistic'
    return 'human_clinical'

refs=[]; noise=[]; seen={}
for pmid,m in META.items():
    autores=m['authors']
    blocos=m.get('blocos',['?'])
    if pmid in OV:
        sob,ano,role,extra=OV[pmid]
    else:
        # sobrenome do 1o autor real
        first=autores[0] if autores else 'REF'
        tok=re.split(r'[\s,]+', first.strip())[0] if first.strip() else 'REF'
        sob=re.sub(r'[^A-Za-z]','',sem(tok)).upper() or 'REF'
        ano=str(m['pubdate'][:4]); extra=[]
        role=role_de(m.get('tipo',''),m.get('tema',''))
    tag={'review':'OB','preclinical_mechanistic':'ML','human_clinical':'EC'}[role]
    oid=f'REF_{sob}_{ano}'
    if oid in seen: seen[oid]+=1; oid=f'{oid}{chr(96+seen[oid])}'
    else: seen[oid]=1
    aliases={sob,sob.title()}
    esp=sem(m.get('autor_ano',''))
    mt=re.match(r'\s*([A-Za-zÀ-ÿ]{3,})', esp)
    if mt:
        a=re.sub(r'[^A-Za-z]','',mt.group(1)).upper()
        if len(a)>=4: aliases.add(a); aliases.add(a.title())
    for e in extra:
        aliases.add(e.upper()); aliases.add(e.title())
    tema=m['tema'].strip('* ').strip()
    rec={'pmid_oficial':pmid,'titulo_artigo':m['title'],
      'autores':autores if autores else [m.get('autor_ano','').split('(')[0].strip()],
      'revista_ano':f"{m['journal']} ({ano})",'desenho_estudo':f'[{tag}]',
      'secao_origem':'mecanismo_B14_neuroesteroides_hormonios_neuroativos',
      'achado_central_molecular':tema,
      'extrapolacao_por_analogia':('SIM — dado animal/estrutural [EXT]; traducao humana cautelosa' if role=='preclinical_mechanistic' else 'não'),
      'ids_referencia_interna':[oid],'id_referencia_interna':oid,
      'doi':'','claim_id_origem':'','evid_role':role,
      'especie_mesh':['Animals'] if role=='preclinical_mechanistic' else (['Humans'] if role=='human_clinical' else ['Humans','Animals']),
      'verification_status':('preclinico' if role=='preclinical_mechanistic' else 'verificado'),
      'citacao_confirmada':True,
      'g1_metodo':'eutils_automatico (Briefing B14; 255/255 resolvem PubMed; 240 ancoras mecanisticas)',
      'g2_elegibilidade':('redirecionado_mecanistico' if role=='preclinical_mechanistic' else 'eligible'),
      'g2_motivo':('animal/estrutural/celula — [EXT]' if role=='preclinical_mechanistic' else 'humano/meta/revisao'),
      'g3_verificado_por':'IA G3 (G1 esummary; autor+ano+tema conferidos); P-6 avaliador cego pendente',
      'status_auditoria':'CONFIRMADO','origem_pipeline':'BUSCA_FERRAMENTA',
      '_aliases':sorted(a for a in aliases if a and a.lower()!='ref')}
    if pmid in RUIM:
        rec['status_auditoria']='EXCLUIDO_RUIDO'
        rec['g2_motivo']='bloco N: intervencao nao-mecanismo (acupuntura/TCM/fitoterapico) — excluido do corpo'
        noise.append(rec)
    else:
        refs.append(rec)

B='/home/user/BIBLIOTECAS/B14_Neuroesteroides/Evidencias/Bibliografia'
json.dump(refs,open(B+'/01_pmids.json','w'),ensure_ascii=False,indent=1)
for f in ['02_meta_analises','03_ensaios_clinicos','04_atualizacoes_literatura','05_manuais_e_livros']:
    json.dump([],open(B+f'/{f}.json','w'))
json.dump(noise,open('/home/user/BIBLIOTECAS/B14_Neuroesteroides/producao/ruido_excluido_blocoN.json','w'),ensure_ascii=False,indent=1)
print('ANCORAS:',len(refs),Counter(r['evid_role'] for r in refs))
print('RUIDO:',len(noise))
# checa labels problematicos
probl=[r['id_referencia_interna'] for r in refs if re.match(r'REF_\d',r['id_referencia_interna'])]
print('labels so-numero:',probl)
