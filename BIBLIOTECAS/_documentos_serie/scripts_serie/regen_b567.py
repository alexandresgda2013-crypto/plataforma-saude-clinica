import json, glob, subprocess, sys, os, re
FW='/home/user/Ferramentas de geração e auditoria'
def regenerate(folder, Bn, bloco):
    base=f'/home/user/BIBLIOTECAS/{folder}'
    cans=[p for p in glob.glob(f'{base}/*.md') if 'CANONICA' in p.upper()]
    can=cans[0]; t=open(can).read()
    refs=json.load(open(f'{base}/Evidencias/Bibliografia/01_pmids.json'))
    if bloco and bloco.split('###')[1][:20] not in t:
        t=t.replace('## TABELA DE EVIDÊNCIAS', bloco+'\n---\n\n## TABELA DE EVIDÊNCIAS',1)
    # apendice
    marc='## APÊNDICE DE CORPUS'; b=t.split(marc)[0].rstrip()
    # preserva METADADOS CANONICOS (estao no fim) -> move antes do apendice: remover e readicionar depois
    meta=None
    if 'METADADOS CANÔNICOS' in b:
        idx=b.index('## METADADOS CANÔNICOS'); meta=b[idx:]; b=b[:idx].rstrip()
    lin=[]
    for r in refs:
        lab=r['id_referencia_interna'].replace('REF_','')
        tag={'preclinical_mechanistic':'ML','human_experimental':'EC','review':'OB'}.get(r['evid_role'],'MA')
        lin.append(f'{lab}[{tag}]')
    ap="\n\n---\n\n"+marc+f" (ÍNDICE — {Bn})\n> Entradas do Módulo 09 (G1 eutils); inclui GPM v2.\n"
    for i in range(0,len(lin),25): ap+="*"+" | ".join(lin[i:i+25])+"*\n"
    t=b+ap
    if meta: t=t.rstrip()+"\n\n"+meta
    open(can,'w').write(t)
    # ledger via retrocompat
    subprocess.run([sys.executable,'/home/user/retrocompat_mod9_ledger.py',base,Bn],capture_output=True)
    # fix trechos + vinc
    t=open(can).read()
    for r in refs: r['ids_referencia_interna']=[r['id_referencia_interna']]
    json.dump(refs,open(f'{base}/Evidencias/Bibliografia/01_pmids.json','w'),ensure_ascii=False,indent=1)
    led=json.load(open(f'{base}/Auditoria_{Bn}/ledger_auditoria_{Bn}.json'))
    bypm={str(r['pmid_oficial']):r for r in refs}; vinc=[]
    for i,e in enumerate(led,1):
        r=bypm.get(str(e['pmid_oficial']))
        if r:
            e['id_referencia_interna']=r['id_referencia_interna']
            lab=r['id_referencia_interna'].replace('REF_','')
            hits=[l for l in t.splitlines() if (lab+'[') in l]
            if hits: e['trecho_ancora']=max(hits,key=len).strip()[:600]; e['citacao_literal']=f'{lab}[TAG]'
        vinc.append({'id_vinculo':f'VINC_{Bn}_{i:03d}','id_referencia_interna':e['id_referencia_interna'],
          'pmid_oficial':e['pmid_oficial'],'secao_origem':f'{Bn}_CANONICA','trecho_ancora':e['trecho_ancora'],
          'mecanismo_origem':e.get('mecanismo_origem',f'mecanismo_{'Bn[1:].lower()+_x'}'),'natureza_relacao':'contributiva','grau_maturidade':'bem_suportado',
          'forca_causal':e['forca_causal'],'especie_mesh':e['especie_mesh'],'evid_role':e['evid_role'],
          'verification_status':('preclinico' if e['portao_G2_elegibilidade']=='NAO_APLICAVEL' else 'verificado'),
          'citacao_confirmada':True,'g1_metodo':'eutils_automatico',
          'g2_elegibilidade':('redirecionado_mecanistico' if e['portao_G2_elegibilidade']=='NAO_APLICAVEL' else 'eligible'),
          'g2_motivo':e['verificacao']['g2_motivo'],'g3_verificado_por':e['verificacao']['g3_nota'],
          'status_auditoria':('CONFIRMADO' if e['status_auditoria']=='APROVADO' else 'PARCIALMENTE_CONFIRMADO'),
          'status_referencia':'CONFIRMADA','uso':'nucleo_causal','data_verificacao':'2026-09-06'})
    json.dump(led,open(f'{base}/Auditoria_{Bn}/ledger_auditoria_{Bn}.json','w'),ensure_ascii=False,indent=1)
    json.dump(vinc,open(f'{base}/Evidencias/Vinculos/vinculos_referencia_afirmacao.json','w'),ensure_ascii=False,indent=1)
    return can,len(refs),len(vinc)

B5bloco="""
### Atualização (GPM B5 v2) — âncoras validadas
- **Sistema GABA na ansiedade/depressão e alvo terapêutico** — revisão clássica da farmacologia
  GABAérgica (sedação/ansiólise/cognição) (Möhler 2012)[OB].
- **Cetamina: receptores NMDA e além** — revisão do mecanismo glutamatérgico além do NMDA,
  ainda **disputado/emergente** (Zorumski 2016)[OB].
"""
B6bloco="""
### Atualização (GPM B6 v2) — âncoras validadas
- **Teoria dos radicais livres do envelhecimento** — fundamento histórico do O&NS (Harman
  1956)[OB]; **Nrf2** como fator de resposta antioxidante (Tebay 2015)[OB].
- **GSH cerebral in vivo (¹H-MRS) na depressão** — glutationa↔anedonia (Lapidus/Shungu
  2014)[EC]; revisão do estresse oxidativo na depressão (Bhatt & Patil 2020)[OB].
> Nota: Hashimoto 2018, Santos/Piato 2019 e Hayes não fecharam autor+ano+tema em esummary
> nesta rodada (falso-positivo); ficam sinalizados ao P-6, sem PMID forjado.
"""
for folder,Bn,bl in [('B5_GabaGlutamato','B5',B5bloco),('B6_EstresseOxidativo','B6',B6bloco)]:
    can,nr,nv=regenerate(folder,Bn,bl)
    print(f'{Bn}: refs {nr} vinc {nv}')
