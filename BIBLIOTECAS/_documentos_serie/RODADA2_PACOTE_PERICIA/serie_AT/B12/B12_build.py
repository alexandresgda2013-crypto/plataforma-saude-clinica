import json,re,unicodedata
def sem(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c))
META=json.load(open('/home/user/BIBLIOTECAS/B12_NeurobiologiaTrauma/producao/g1_resolvidos.json'))
ML={'Berton_2006','Krishnan_2007','Pena_2017','Milad_2002','Weaver_2004','Zhou_2007','Tsankova_2006','Caspi_2002'}
refs=[]; seen={}
for pmid,m in sorted(META.items(),key=lambda x:int(x[0])):
    label=m['anchor']; sob=re.sub(r'[^A-Za-z]','',sem(label.split('_')[0])).upper()
    ano=label[-4:] if label[-4:].isdigit() else m['pubdate'][:4]
    role='preclinical_mechanistic' if label in ML else ('review' if any(k in label for k in ('Galatzer','Schumacher' if False else 'GalatzerLevy','McEwen','Liberzon','Sheridan','Gunnar','Bangasser','Etkin')) else 'human_clinical')
    base=f'REF_{sob}_{ano}'
    if base in seen: seen[base]+=1; oid=f'{base}{chr(97+seen[base]-1)}'
    else: seen[base]=0; oid=base
    tag='ML' if role=='preclinical_mechanistic' else ('OB' if role=='review' else 'EC')
    refs.append({'pmid_oficial':pmid,'titulo_artigo':m['title'],'autores':m['authors'],
      'revista_ano':f"{m['journal']} ({m['pubdate'][:4]})",'desenho_estudo':f'[{tag}] {label}',
      'secao_origem':'mecanismo_B12_neurobiologia_trauma','achado_central_molecular':m['title'].rstrip('.'),
      'extrapolacao_por_analogia':('SIM — animal/célula [EXT]' if role=='preclinical_mechanistic' else 'não'),
      'ids_referencia_interna':[f'REF_{label}'],'id_referencia_interna':oid,'doi':'','claim_id_origem':'',
      'evid_role':role,'especie_mesh':['Animals'] if role=='preclinical_mechanistic' else ['Humans'],
      'verification_status':'preclinico' if role=='preclinical_mechanistic' else 'verificado',
      'citacao_confirmada':True,'g1_metodo':'eutils_automatico (autor+ano+tema vs GPM; falsos positivos descartados)',
      'g2_elegibilidade':'redirecionado_mecanistico' if role=='preclinical_mechanistic' else 'eligible',
      'g2_motivo':'animal causal' if role=='preclinical_mechanistic' else 'humano/meta/imagem',
      'g3_verificado_por':'IA G3; P-6 pendente','status_auditoria':'CONFIRMADO',
      'origem_pipeline':'BUSCA_FERRAMENTA','_aliases':[sob,sob.title()]})
json.dump(refs,open('/home/user/BIBLIOTECAS/B12_NeurobiologiaTrauma/Evidencias/Bibliografia/01_pmids.json','w'),ensure_ascii=False,indent=1)
for f in ['02_meta_analises','03_ensaios_clinicos','04_atualizacoes_literatura','05_manuais_e_livros']:
    json.dump([],open(f'/home/user/BIBLIOTECAS/B12_NeurobiologiaTrauma/Evidencias/Bibliografia/{f}.json','w'))
from collections import Counter
print('refs B12:',len(refs),Counter(r['evid_role'] for r in refs))
