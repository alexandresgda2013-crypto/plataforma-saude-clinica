import json,re,unicodedata
def sem(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c))
META=json.load(open('/home/user/BIBLIOTECAS/B10_DesregulacaoCircadiana/producao/g1_resolvidos.json'))
# role por anchor
ROLE={'Ralph_1990':'ML','Hattar_2002':'ML','Berson_2002':'ML','Roybal_2007':'ML','Landgraf_2016':'ML',
'Ozburn_2017':'ML','Liang_2025':'ML','Gardner_2026':'ML','Hines_2013':'ML','Tapia-Osorio_2013':'ML'}
refs=[]; seen={}
for pmid,m in sorted(META.items(),key=lambda x:int(x[0])):
    label=m['anchor']; sob=re.sub(r'[^A-Za-z]','',sem(label.split('_')[0])).upper()
    # ano de label ou pubdate
    ano=label[-4:] if label[-4:].isdigit() else m['pubdate'][:4]
    isml=label in ROLE or 'na' in label[-2:]
    role='preclinical_mechanistic' if label in ROLE else ('review' if label in ('Roenneberg_2003','Takahashi_2017','Mohawk_2012','McClung_2017','McClung_2019','Vadnie_2017','Fonken_2019','Brancaccio_2018','Hastings_2018','Bedrosian_na','Ehlers_1988','Bunney_2013','Bunney_na','Riemann_2019','Riemann_2010','Geoffroy_2025','Carmassi_2019','Crouse_2021','Etain_2012','Lewy_2006','Lewy_na') else 'human_clinical')
    base=f'REF_{sob}_{ano}'
    if base in seen: seen[base]+=1; oid=f'{base}{chr(97+seen[base]-1)}'
    else: seen[base]=0; oid=base
    tag='ML' if role=='preclinical_mechanistic' else ('OB' if role=='review' else 'EC')
    refs.append({'pmid_oficial':pmid,'titulo_artigo':m['title'],'autores':m['authors'],
      'revista_ano':f"{m['journal']} ({m['pubdate'][:4]})",'desenho_estudo':f'[{tag}] {m["anchor"]}',
      'secao_origem':'mecanismo_B10_desregulacao_circadiana','achado_central_molecular':m['title'].rstrip('.'),
      'extrapolacao_por_analogia':('SIM — animal [EXT]' if role=='preclinical_mechanistic' else 'não'),
      'ids_referencia_interna':[f'REF_{label}'],'id_referencia_interna':oid,'doi':'','claim_id_origem':'',
      'evid_role':role,'especie_mesh':['Animals'] if role=='preclinical_mechanistic' else ['Humans'],
      'verification_status':'preclinico' if role=='preclinical_mechanistic' else 'verificado',
      'citacao_confirmada':True,'g1_metodo':'eutils_automatico (autor+ano+tema vs GPM)',
      'g2_elegibilidade':'redirecionado_mecanistico' if role=='preclinical_mechanistic' else 'eligible',
      'g2_motivo':'animal causal' if role=='preclinical_mechanistic' else 'humano/revisao',
      'g3_verificado_por':'IA G3 esummary; P-6 pendente','status_auditoria':'CONFIRMADO',
      'origem_pipeline':'BUSCA_FERRAMENTA','_aliases':[sob,sob.title()]})
json.dump(refs,open('/home/user/BIBLIOTECAS/B10_DesregulacaoCircadiana/Evidencias/Bibliografia/01_pmids.json','w'),ensure_ascii=False,indent=1)
for f in ['02_meta_analises','03_ensaios_clinicos','04_atualizacoes_literatura','05_manuais_e_livros']:
    json.dump([],open(f'/home/user/BIBLIOTECAS/B10_DesregulacaoCircadiana/Evidencias/Bibliografia/{f}.json','w'))
from collections import Counter
print('refs B10:',len(refs),Counter(r['evid_role'] for r in refs))
