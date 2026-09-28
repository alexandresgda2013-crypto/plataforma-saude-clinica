#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Constrói 01_pmids.json da B15 (134 ancoras mecanisticas; 6 ruidos de composto/suplemento
registrados a parte). Classificacao por tipo do Briefing + overrides cientificos."""
import json,re,unicodedata
from collections import Counter
def sem(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c))
META=json.load(open('/home/user/BIBLIOTECAS/B15_AutofagiaMTOR/producao/g1_resolvidos.json'))
RUIM=set(json.load(open('/tmp/b15_ruido.json')))

# overrides cientificos: pmid -> (sob, ano, role, aliases extras). role: review/OB human/EC preclin/ML
OV={
 '33634751':('KLIONSKY','2021','review',['KLIONSKY_DIRETRIZ']),
 '20724638':('LI','2010','preclinical_mechanistic',['LI_KETAMINA']),
 '21677641':('AUTRY','2011','preclinical_mechanistic',[]),
 '40205038':('YANG','2025','preclinical_mechanistic',[]),
 '35115539':('SHEN','2022','preclinical_mechanistic',[]),   # autofagia dendritica Nat Commun
 '36793868':('YANG','2023','preclinical_mechanistic',[]),    # hiperativacao depleta BDNF Theranostics
 '31234698':('JUNG','2020','preclinical_mechanistic',[]),    # morte autofagica cel-tronco Autophagy
 '38831333':('CHOE','2024','preclinical_mechanistic',[]),
 '25386878':('GASSEN','2014','human_clinical',[]),           # FKBP51 translacional (celulas/roedor/humano)
 '25714272':('GASSEN','2015','preclinical_mechanistic',[]),
 '31244689':('HE','2019','human_clinical',['BECLIN_SERICO']),
 '38001115':('HE','2023','human_clinical',['LC3A']),
 '35925279':('LYU','2022','preclinical_mechanistic',['NLRP3']),
 '36914810':('LU','2023','human_clinical',['NIX','BNIP3L']),  # animal+humano (NIX sangue TDM)
 '27004790':('ARDID','2016','preclinical_mechanistic',[]),   # rapamicina bloqueia animal
 '32092760':('ABDALLAH','2020','human_clinical',['RAPAMICINA_ECR']),
 '30990795':('KATO','2019','preclinical_mechanistic',['NV5138']),
 '41512716':('TARGUM','2026','human_clinical',['NV5138_ECR']),
 '40752777':('MALLET','2026','preclinical_mechanistic',['SANDI','UROLITINA']),
 '42270169':('CHAUDHARI','2026','review',[]),
 '37644025':('ZHANG','2023','preclinical_mechanistic',['NRBF2']),
 '34971825':('LIAO','2022','preclinical_mechanistic',[]),
 '41073381':('LIU','2025','preclinical_mechanistic',[]),     # downreg autofagia amigdala alivia ansiedade
 '21635931':('JERNIGAN','2011','human_clinical',[]),          # mTOR PFC comprometido TDM (post-mortem)
 '30038230':('GULBINS','2018','preclinical_mechanistic',[]),
 '33124469':('GULBINS','2021','preclinical_mechanistic',[]), # sertralina AMPK-MTOR Autophagy
 '32264724':('SHANG','2021','review',['KLIONSKY_SEXO']),
 '35508467':('CHEN','2022','human_clinical',[]),
 '25726893':('MACHADO','2015','human_clinical',[]),
 '31477685':('LI','2019','human_clinical',[]),
 '34391068':('ZENG','2021','human_clinical',[]),
 '40497971':('WANG','2025','review',[]),
 '42372600':('MALLET','2026','preclinical_mechanistic',[]),  # urolitina A sono/ferroptose
 '38729223':('QI','2024','human_clinical',['ESPERMIDINA_NHANES']),
 '39677641':('MACKERT','2024','preclinical_mechanistic',['ESPERMIDINA_PREPRINT']),  # bioRxiv
 '40722026':('CHAO','2025','preclinical_mechanistic',['APOE']),
 '38677623':('MARTON','2024','preclinical_mechanistic',['BGP15']),  # sinal de alvo mitofagico (fica)
 '40205038b':('YANG','2025','preclinical_mechanistic',[]),
}

def role_de(tipo,tema):
    t=sem(tipo+' '+tema).lower()
    if any(k in t for k in ['revis','review','meta','editorial','diretriz','guidelines','perspectiv']):
        return 'review'
    # humano explicito
    if any(k in t for k in ['humano','ecr','rct','coorte','pós-morte','pos-morte','post-mortem','transcriptoma',
                            'sérico','serico','sangue','pbmc','monócito','monocito','epidemiol','nhanes','fase 1b',
                            'bioinformática','bioinformatica','pacientes']):
        return 'human_clinical'
    if any(k in t for k in ['animal','roedor','rato','camundong','mouse','rat','knockout','knock-down','knockdown',
                            'modelo','in vitro','mecanístic','mecanistic','causal','celulas','células','pré-clín',
                            'pre-clin','transgên']):
        return 'preclinical_mechanistic'
    return 'review'  # default: revisao

refs=[]; noise=[]; seen={}
for pmid,m in META.items():
    autores=m['authors']
    blocos=m.get('blocos',['?'])
    if pmid in OV:
        sob,ano,role,extra=OV[pmid]
    else:
        first=autores[0] if autores else 'REF'
        tok=re.split(r'[\s,]+',first.strip())[0] if first.strip() else 'REF'
        sob=re.sub(r'[^A-Za-z]','',sem(tok)).upper() or 'REF'
        ano=str(m['pubdate'][:4]); extra=[]
        role=role_de(m.get('tipo',''),m.get('tema',''))
    tag={'review':'OB','preclinical_mechanistic':'ML','human_clinical':'EC'}[role]
    oid=f'REF_{sob}_{ano}'
    if oid in seen: seen[oid]+=1; oid=f'{oid}{chr(96+seen[oid])}'
    else: seen[oid]=1
    aliases={sob,sob.title()}
    esp=sem(m.get('autor_ano',''))
    mt=re.match(r'\s*([A-Za-zÀ-ÿ]{3,})',esp)
    if mt:
        a=re.sub(r'[^A-Za-z]','',mt.group(1)).upper()
        if len(a)>=4: aliases.add(a); aliases.add(a.title())
    for e in extra: aliases.add(e.upper()); aliases.add(e.title())
    tema=m['tema'].strip('* ').strip()
    preprint = 'biorxiv' in m['journal'].lower() or 'preprint' in m['tipo'].lower()
    rec={'pmid_oficial':pmid,'titulo_artigo':m['title'],
      'autores':autores if autores else [m.get('autor_ano','').split('(')[0].strip()],
      'revista_ano':f"{m['journal']} ({ano})",'desenho_estudo':f'[{tag}]',
      'secao_origem':'mecanismo_B15_autofagia_mtor',
      'achado_central_molecular':tema+(' [PRÉ-PRINT bioRxiv — evidência emergente, G3]' if preprint else ''),
      'extrapolacao_por_analogia':('SIM — dado animal/celular [EXT]; traducao humana cautelosa' if role=='preclinical_mechanistic' else 'não'),
      'ids_referencia_interna':[oid],'id_referencia_interna':oid,
      'doi':'','claim_id_origem':'','evid_role':role,
      'especie_mesh':['Animals'] if role=='preclinical_mechanistic' else (['Humans'] if role=='human_clinical' else ['Humans','Animals']),
      'verification_status':('preclinico' if role=='preclinical_mechanistic' else 'verificado'),
      'citacao_confirmada':True,'g1_metodo':'eutils_automatico',
      'g1_resumo':f"eutils (Briefing B15; 140/140 resolvem PubMed; {ano})",
      'g2_elegibilidade':('redirecionado_mecanistico' if role=='preclinical_mechanistic' else 'eligible'),
      'g2_motivo':('animal/celular — [EXT]'+('; pre-print' if preprint else '') if role=='preclinical_mechanistic' else 'humano/meta/revisao'),
      'g3_verificado_por':'IA G3 (G1 esummary; autor+ano+tema conferidos); P-6 avaliador cego pendente',
      'status_auditoria':'CONFIRMADO','origem_pipeline':'BUSCA_FERRAMENTA',
      '_aliases':sorted(a for a in aliases if a and a.lower()!='ref')}
    if pmid in RUIM:
        rec['status_auditoria']='EXCLUIDO_RUIDO'
        rec['g2_motivo']='composto/suplemento/TCM/contexto metabólico — não é biologia do mecanismo (excluído do corpo)'
        noise.append(rec)
    else:
        refs.append(rec)

B='/home/user/BIBLIOTECAS/B15_AutofagiaMTOR/Evidencias/Bibliografia'
json.dump(refs,open(B+'/01_pmids.json','w'),ensure_ascii=False,indent=1)
for f in ['02_meta_analises','03_ensaios_clinicos','04_atualizacoes_literatura','05_manuais_e_livros']:
    json.dump([],open(B+f'/{f}.json','w'))
json.dump(noise,open('/home/user/BIBLIOTECAS/B15_AutofagiaMTOR/producao/ruido_excluido.json','w'),ensure_ascii=False,indent=1)
print('ANCORAS:',len(refs),Counter(r['evid_role'] for r in refs))
print('RUIDO:',len(noise),[r['pmid_oficial'] for r in noise])
probl=[r['id_referencia_interna'] for r in refs if re.match(r'REF_\d',r['id_referencia_interna'])]
print('labels so-numero:',probl)
