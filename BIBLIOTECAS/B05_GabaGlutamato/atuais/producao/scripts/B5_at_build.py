# -*- coding: utf-8 -*-
import json, re, unicodedata
D='BIBLIOTECAS/B05_GabaGlutamato/producao/insumos/'
DEC=json.load(open(D+'matriz_b5_decisao.json'))
R=json.load(open(D+'matriz_b5_g1.json'))
AB=R['abstracts']
norm=lambda s: re.sub(r'[^A-Za-z0-9]','',unicodedata.normalize('NFKD',s or '').encode('ascii','ignore').decode())
NEG={'30144668','34023450','32619710','35526748'}           # Godfrey(glutamato sem dif.), Rideaux×2, Steel(atenuada)
CONT={'33059355','34354048','32017978','41607072','36596696'} # Pothula, Kantrowitz, Sial, Lu-opioide, Zanos2023
def tag_of(pt,mesh,titulo):
    t=titulo.lower()
    if 'Meta-Analysis' in pt or 'Systematic Review' in pt: return 'MA'
    if 'Review' in pt: return 'OB'
    m=[x.lower() for x in mesh]
    humany=any(x=='humans' for x in m); anim=any(x=='animals' for x in m)
    if humany and not anim: return 'EC'
    return 'EC' if humany and any('Trial' in p for p in pt) else 'ML'
out=[]; used={}
ORDER=['KET','GABA','NMDA','AMPA','PLAST','MRS','ANX','STR','IFACE']
for g in ORDER:
    seq=0
    for e in [x for x in DEC['ENTRA'] if x['grupo']==g]:
        p=e['pmid']; seq+=1
        tit=e['titulo'] or ''
        a1=e['a1'] or 'X'
        sob=a1.split()[0]
        sob2=''.join(w.capitalize() for w in re.split(r"[-' ]",sob) if w)
        lab=norm(sob2)+'_'+(e['ano'] or '')
        if lab in used:
            lab=re.sub(r'_(\d{4})$',lambda m:'_B'+m.group(1),lab)
        used[lab]=1
        mesh=AB.get(p,{}).get('mesh',[])
        tag=tag_of(e.get('pubtype',[]),mesh,tit)
        esp=['Humans'] if tag in('MA','EC') else (['Animals'] if tag=='ML' else ['Humans'])
        if tag=='OB':
            m=[x.lower() for x in mesh]
            esp=['Animals'] if (any(x=='animals' for x in m) and not any(x=='humans' for x in m)) else ['Humans']
        papel='NEG' if p in NEG else ('CONT' if p in CONT else ('MEC' if tag=='ML' else ('SUP' if tag in('EC','MA') else 'REF')))
        cid='B5.MEC.'+g+'.%03d'%seq
        out.append({'pmid':p,'grupo':g,'label':lab,'id':'REF_'+lab.upper(),'tag':tag,'evid_role':papel,'claim_id':cid,
          'titulo':tit,'fonte':e['fonte'],'ano':e['ano'],'autores':[e['a1']],'pubtype':e.get('pubtype',[]),
          'especie_mesh':esp,'abstract':AB.get(p,{}).get('abstract','')[:1200]})
dup=[k for k,v in used.items() if list(used).count(k)>1]
assert (len(out),len({r['id'] for r in out}),len({r['label'] for r in out}))==(116,116,116), (len(out),len({r['id'] for r in out}),len({r['label'] for r in out}))
from collections import Counter
print('por grupo:',dict(Counter(r['grupo'] for r in out)),'| tags:',dict(Counter(r['tag'] for r in out)))
json.dump(out,open(D+'matriz_b5_at_final.json','w'),ensure_ascii=False,indent=1)
print('ok; amostras:',[(r['label'],r['tag'],r['evid_role']) for r in out[:5]])
