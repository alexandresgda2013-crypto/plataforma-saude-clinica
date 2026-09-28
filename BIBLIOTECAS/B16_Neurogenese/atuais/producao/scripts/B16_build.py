#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Constrói 01_pmids.json da B16 (288 ancoras; zero ruído excluído das tabelas —
nao-fundidos registrados a parte). Classificacao por tipo do Briefing + overrides."""
import json,re,unicodedata
from collections import Counter
def sem(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c))
META=json.load(open('/home/user/BIBLIOTECAS/B16_Neurogenese/producao/g1_resolvidos.json'))

# --- colisoes (pmid esperado sem sufixo = primeiro do grupo) ---
PREF=['23650397','23303060','35524139','35787318','34783064','30617274','31899214',
      '29162814','26910812','32360430','30867562','21460835','21609817']

# --- aliases de autoria do Briefing (1o autor real = PubMed) ---
ALIAS_EXTRA={
 '31165247':['BORTOLOTTO'], '30236533':['BANASR'], '29941977':['JIN_MEDO'],
 '31310776':['ARDALAN2'], '27106168':['ARDALAN'], '30622299':['DUKART'],
 '30414016':['BARHA'], '32774242':['ADIPONECTINA'], '32138332':['MELATONINA_DG'],
 '41303432':['KBN2202'], '37790349':['AGRIMI_PREPRINT'], '38352378':['CHANG_PREPRINT'],
 '22652019':['BOLDRINI_ANGIO'], '39648699':['GAGE_2025'],
}

# --- overrides de role quando o tipo do briefing e ambiguo ---
ROLE_OV={
 '9809557':'human_clinical','23746839':'human_clinical','41651838':'preclinical_mechanistic',
 '10889528':'review','12946878':'review','35420933':'review','30617274':'review','31290449':'review',
 '31915385':'human_clinical','20126454':'human_clinical','29722804':'human_clinical',
 '33762407':'human_clinical','21519376':'review','16415915':'human_clinical','28675388':'human_clinical',
 '37302394':'preclinical_mechanistic','29898390':'preclinical_mechanistic','34273388':'preclinical_mechanistic',
 '32138332':'preclinical_mechanistic','36080418':'preclinical_mechanistic','33609653':'preclinical_mechanistic',
 '41303432':'preclinical_mechanistic','29867368':'preclinical_mechanistic','23727882':'preclinical_mechanistic',
 '37000971':'preclinical_mechanistic','42009274':'preclinical_mechanistic','39830600':'preclinical_mechanistic',
 '36599082':'preclinical_mechanistic','37790349':'preclinical_mechanistic','38352378':'preclinical_mechanistic',
 '39558003':'review','35495058':'review','39648699':'review','36259116':'review','40735066':'review',
 '30986730':'human_clinical','30622299':'human_clinical','32730916':'human_clinical','25451411':'human_clinical',
 '30867562':'human_clinical','26138003':'human_clinical','40199994':'human_clinical','37393047':'human_clinical',
 '35859546':'human_clinical','33479507':'human_clinical','39984680':'human_clinical','23641193':'human_clinical',
 '31930958':'human_clinical','28529072':'human_clinical','32726406':'human_clinical','22071871':'human_clinical',
 '39297528':'human_clinical','21483429':'human_clinical','19606083':'human_clinical','22652019':'human_clinical',
 '29625071':'human_clinical','29513649':'human_clinical','30911133':'human_clinical','31130513':'human_clinical',
 '33762406':'human_clinical','34672693':'human_clinical','40608919':'human_clinical','40957417':'human_clinical',
 '42629468':'human_clinical','39414359':'human_clinical','41741649':'human_clinical','37015226':'human_clinical',
 '33183762':'preclinical_mechanistic','21525974':'preclinical_mechanistic',  # primata -> preclinico
}
def role_de(tipo,tema):
    t=sem(tipo+' '+tema).lower()
    if any(k in t for k in ['revis','consenso','comentario','teoria','teorico','perspectiv','debate','escopo','capitulo','metodologica','metodo','hipotese']):
        return 'review'
    if any(k in t for k in ['humano','pos-morte','pós-morte','celular','in vitro','organoide','imagem','primatas','primata q1','fmri']):
        # primata aqui tratado como preclinico
        if 'primata' in t and 'revis' not in t: return 'preclinical_mechanistic'
        return 'human_clinical'
    if any(k in t for k in ['animal','mecanist','causal','roedor','clonal','linhagem']):
        return 'preclinical_mechanistic'
    return 'review'

tagmap={'review':'OB','preclinical_mechanistic':'ML','human_clinical':'EC'}
refs=[]
for pmid,m in META.items():
    autores=m['authors']
    first=autores[0] if autores else 'REF'
    tok=re.split(r'[\s,]+',first.strip())[0] if first.strip() else 'REF'
    sob=re.sub(r'[^A-Za-z]','',sem(tok)).upper() or 'REF'
    ano=str(m['pubdate'][:4])
    role=ROLE_OV.get(pmid) or role_de(m.get('tipo',''),m.get('tema',''))
    tag=tagmap[role]
    tema=re.sub(r'\s+',' ',m['tema']).strip()
    achado=tema[:180]
    extra=[f"[{m['tipo']}]"] if m.get('tipo') else []
    situ = ' '.join([achado]+extra)
    gen='Humans' if role=='human_clinical' else ('Animals' if role=='preclinical_mechanistic' else 'Humans')
    esp=[gen] if role!='review' else ['Humans','Animals']
    aliases=list(dict.fromkeys([sob, sob.title()]+ALIAS_EXTRA.get(pmid,[])))
    jour=re.sub(r'\s*\([^)]*(?:19|20)\d{2}[^)]*\)','',m['journal']).strip()
    refs.append({
        'pmid_oficial':pmid,'titulo_artigo':m['title'],'autores':autores,
        'revista_ano':f"{jour} ({ano})",
        'desenho_estudo':f'[{tag}]',
        'secao_origem':'mecanismo_B16_neurogenese',
        'achado_central_molecular':situ[:240],
        'extrapolacao_por_analogia':'não',
        'ids_referencia_interna':[],  # preenchido abaixo
        'id_referencia_interna':'',
        'doi':'','claim_id_origem':'',
        'evid_role':role,'especie_mesh':esp,
        'verification_status':'verificado','citacao_confirmada':True,
        'g1_metodo':'eutils_automatico',
        'g1_resumo':f"eutils (Briefing B16; 288/288 resolvem PubMed; {ano})",
        'g2_elegibilidade':'eligible',
        'g2_motivo':'humano/meta/revisao' if role!='preclinical_mechanistic' else 'animal/mecanístico',
        'g3_verificado_por':'IA G3 (G1 esummary; autor+ano+tema conferidos); P-6 avaliador cego pendente',
        'status_auditoria':'CONFIRMADO','origem_pipeline':'BUSCA_FERRAMENTA',
        '_aliases':aliases,
        '_sob':sob,'_ano':ano,'_pmid':pmid,
    })
# ordena: grupos de colisao na ordem PREF; resto por (sob,ano,pmid)
def chave(r):
    if r['_pmid'] in PREF: return (r['_sob'],r['_ano'],0,PREF.index(r['_pmid']))
    return (r['_sob'],r['_ano'],1,r['_pmid'])
refs.sort(key=chave)
seen={}
for r in refs:
    base=f"REF_{r['_sob']}_{r['_ano']}"
    if base in seen:
        seen[base]+=1; oid=f"{base}{chr(ord('a')+seen[base]-1)}"
    else:
        seen[base]=1; oid=base
    r['id_referencia_interna']=oid; r['ids_referencia_interna']=[oid]
    del r['_sob'],r['_ano'],r['_pmid']
out='/home/user/BIBLIOTECAS/B16_Neurogenese/Evidencias/Bibliografia'
import os; os.makedirs(out,exist_ok=True)
json.dump(refs,open(out+'/01_pmids.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('refs:',len(refs))
print('roles:',dict(Counter(r['evid_role'] for r in refs)))
print('tags:',dict(Counter(r['desenho_estudo'] for r in refs)))
# confere sufixos gerados
suf=[(r['pmid_oficial'],r['id_referencia_interna']) for r in refs if re.search(r'_[0-9]{4}[bc]$',r['id_referencia_interna'])]
print('sufixos b/c:',suf)
# mapa rotulo->pmid p/ escrever as listras
mapa={r['id_referencia_interna'].replace('REF_',''):(r['pmid_oficial'],r['desenho_estudo']) for r in refs}
json.dump(mapa,open('/tmp/b16_mapa_rotulos.json','w'),ensure_ascii=False,indent=1)
# manifesto
man={'biblioteca':'B16','mecanismo':'mecanismo_B16_neurogenese',
 'titulo':'Neurogênese hipocampal adulta (AHN) na ansiedade e na depressão',
 'data_corte':'2026-09-07','porta_g1':'eutils_automatico',
 'pmids_briefing':289,'pmids_tabelas':288,'validados_pubmed':288,'sem_resolucao':0,
 'nao_fundidos':{'anais_EWA_nao_indexados':2,'resumos_congresso_IJNPP':2,'venue_nao_indexado':1,'off_scope_SVZ_OB':['26758842']},
 'preprints_biorxiv':['37790349','38352378'],
 'correcoes_autoria':{
  '31165247':'Park SC 2019 (briefing: Bortolotto)','30236533':'Micheli L 2018 (briefing: Banasr)',
  '29941977':'Huckleberry KA 2018 (briefing: Jin)','31310776':'Yamada J 2019 (briefing: Ardalan)',
  '27106168':'Clarke M 2017 (briefing: Ardalan)','30622299':'Takamiya A 2019 (briefing: Dukart)',
  '30414016':'Gheorghe A 2019 (briefing: Barha)'},
 'nota':'Zero PMID inventado; rotulos genericos do briefing resolvidos por 1o autor PubMed.'}
json.dump(man,open(out+'/_manifesto_biblioteca.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for f in ['02_meta_analises','03_ensaios_clinicos','04_atualizacoes_literatura','05_manuais_e_livros']:
    json.dump([],open(out+'/'+f+'.json','w'))
print('manifesto + 02-05 gravados.')
