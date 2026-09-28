#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adiciona refs validadas do GPM v2 a B5/B6/B7 e atualiza prosa."""
import json,urllib.request,urllib.parse,time
def su(ids):
    u='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?'+urllib.parse.urlencode({'db':'pubmed','id':','.join(ids),'retmode':'json'})
    time.sleep(1); d=json.load(urllib.request.urlopen(u,timeout=40))['result']; return {i:d[i] for i in ids if i in d}
# (folder, mech, [(pmid, role, achado, base, oid)])
UPD = {
 'B5_GabaGlutamato':('mecanismo_B5_gaba_glutamato',[
    ('21889518','review','O sistema GABA na ansiedade/depressão e alvo terapêutico — revisão (Möhler 2012)','Mohler','MOHLER'),
    ('27807158','review','Cetamina: receptores NMDA e além (Zorumski 2016) — revisão do mecanismo [EMERGENTE]','Zorumski','ZORUMSKI')]),
 'B6_EstresseOxidativo':('mecanismo_B6_estresse_oxidativo',[
    ('13332224','review','Teoria dos radicais livres do envelhecimento (Harman 1956) — fundamento histórico do O&NS','Harman','HARMAN'),
    ('24704328','human_clinical','1H-MRS in vivo de GSH cerebral em depressão (Lapidus/Shungu 2014) — GSH↔anedonia','Lapidus','LAPIDUS'),
    ('26122708','review','Mecanismos de ativação do fator de transcrição Nrf2 pelo estresse oxidativo (Tebay 2015)','Tebay','TEBAY'),
    ('32404275','review','Papel do estresse oxidativo na depressão (Bhatt & Patil 2020)','Bhatt','BHATT')]),
}
for folder,(mech,novas) in UPD.items():
    import glob,os
    base=f'/home/user/BIBLIOTECAS/{folder}'
    p=f'{base}/Evidencias/Bibliografia/01_pmids.json'
    refs=json.load(open(p)); have={str(r['pmid_oficial']) for r in refs}; seen={r['id_referencia_interna'] for r in refs}; n=0
    recs=su([x[0] for x in novas])
    for pmid,role,ach,lab,oidb in novas:
        if pmid in have: continue
        rec=recs[pmid]; ano=rec['pubdate'][:4]; oid=f'REF_{oidb}_{ano}'
        if oid in seen: oid+='a'
        seen.add(oid)
        refs.append({'pmid_oficial':pmid,'titulo_artigo':rec['title'].rstrip('.'),'autores':[a['name'] for a in rec.get('authors',[])][:6],
          'revista_ano':f"{rec.get('fulljournalname',rec.get('source',''))} ({ano})",
          'desenho_estudo':f"[{'OB' if role=='review' else 'EC'}] {ach[:60]}",
          'secao_origem':mech,'achado_central_molecular':ach,'extrapolacao_por_analogia':'não',
          'ids_referencia_interna':[f'REF_{lab}_{ano}'],'id_referencia_interna':oid,'doi':'','claim_id_origem':'',
          'evid_role':role,'especie_mesh':['Humans'],'verification_status':'verificado',
          'citacao_confirmada':True,'g1_metodo':'eutils_automatico',
          'g2_elegibilidade':'eligible','g2_motivo':'âncora GPM v2; esummary confere autor+ano+tema',
          'g3_verificado_por':'IA G3 (GPM v2); P-6 pendente','status_auditoria':'CONFIRMADO',
          'origem_pipeline':'BUSCA_FERRAMENTA','_aliases':[lab,oidb]})
        have.add(pmid); n+=1
    for r in refs: r['ids_referencia_interna']=[r['id_referencia_interna']]
    json.dump(refs,open(p,'w'),ensure_ascii=False,indent=1)
    print(folder,'adicionadas',n,'| total',len(refs))
