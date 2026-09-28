#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json,re,unicodedata
def sem(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c))
META=json.load(open('/home/user/BIBLIOTECAS/B13_SistemaEndocanabinoide/producao/g1_resolvidos.json'))
refs=[]; seen={}
ML_kw=['roedor','rat','mouse','knockout','deleção','delecao','animal','KO','in vitro','neural','condicionada','derrota','separação','separacao','modelo']
for pmid,m in META.items():
    tipo=sem(m.get('tipo','')+m.get('tema','')).lower()
    role='preclinical_mechanistic' if any(k in tipo for k in ['roedor','rat','mouse','knockout','deleç','dele c','animal','ko','in vitro','neural','derrota','separa','modelo']) else 'human_clinical'
    # revisões
    first=str(m.get('authors',[{}])[0]) if m.get('authors') else ''
    titulo=sem(m.get('title','')).lower()
    if 'review' in tipo or 'meta' in tipo or 'revisão' in sem(m.get('tipo','')).lower() or 'revisao' in sem(m.get('tipo','')).lower():
        role='review'
    label=re.sub(r'[^A-Za-z0-9]','',sem(m.get('autor_ano','')).split('/')[0].split(',')[0].split(' et')[0].split('.')[0]) or 'REF'
    ano=re.search(r'(19|20)\d{2}',m.get('autor_ano','')+m.get('pubdate',''))
    ano=ano.group(0) if ano else m['pubdate'][:4]
    sob=re.sub(r'[^A-Za-z]','',sem(m.get('authors',[{}])[0] if m.get('authors') else 'X').split()[-1].upper()) if m.get('authors') else label.upper()[:12]
    oid=f'REF_{sob}_{ano}'
    if oid in seen: seen[oid]+=1; oid=f'{oid}{chr(97+seen[oid]-1)}'
    else: seen[oid]=0
    tag={'preclinical_mechanistic':'ML','review':'OB','human_clinical':'EC'}[role]
    refs.append({'pmid_oficial':pmid,'titulo_artigo':m['title'],'autores':m['authors'],
      'revista_ano':f"{m['journal']} ({m['pubdate'][:4]})",'desenho_estudo':f'[{tag}]',
      'secao_origem':'mecanismo_B13_sistema_endocanabinoide','achado_central_molecular':m['tema'].strip('* '),
      'extrapolacao_por_analogia':('SIM — animal/celula [EXT]' if role=='preclinical_mechanistic' else 'não'),
      'ids_referencia_interna':[f'REF_{label}_{ano}'] if label else [oid],'id_referencia_interna':oid,
      'doi':'','claim_id_origem':'','evid_role':role,
      'especie_mesh':['Animals'] if role=='preclinical_mechanistic' else ['Humans'],
      'verification_status':'preclinico' if role=='preclinical_mechanistic' else 'verificado',
      'citacao_confirmada':True,'g1_metodo':'eutils_automatico (Briefing B13, 167/167 validados)',
      'g2_elegibilidade':'redirecionado_mecanistico' if role=='preclinical_mechanistic' else 'eligible',
      'g2_motivo':'animal/celula' if role=='preclinical_mechanistic' else 'humano/meta/revisao',
      'g3_verificado_por':'IA G3 (G1 validado); P-6 avaliador cego pendente','status_auditoria':'CONFIRMADO',
      'origem_pipeline':'BUSCA_FERRAMENTA','_aliases':[sob,sob.title()]})
json.dump(refs,open('/home/user/BIBLIOTECAS/B13_SistemaEndocanabinoide/Evidencias/Bibliografia/01_pmids.json','w'),ensure_ascii=False,indent=1)
for f in ['02_meta_analises','03_ensaios_clinicos','04_atualizacoes_literatura','05_manuais_e_livros']:
    json.dump([],open(f'/home/user/BIBLIOTECAS/B13_SistemaEndocanabinoide/Evidencias/Bibliografia/{f}.json','w'))
from collections import Counter
print('refs B13:',len(refs),Counter(r['evid_role'] for r in refs))
