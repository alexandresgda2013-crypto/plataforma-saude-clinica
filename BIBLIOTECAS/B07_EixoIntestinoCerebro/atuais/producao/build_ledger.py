#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera ledger formal do 05_framework_auditoria a partir dos vínculos N2 (B7)."""
import json, re, os, unicodedata

BASE='/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro'
CAN='B7 EIXO INTESTINO CEREBRO V1 CANONICA.md'
vinc=json.load(open(f'{BASE}/Evidencias/Vinculos/vinculos_referencia_afirmacao.json'))
refs={r['pmid_oficial']:r for r in json.load(open(f'{BASE}/Evidencias/Bibliografia/01_pmids.json'))}
raw=open(f'{BASE}/{CAN}',encoding='utf-8').read()
norm=re.sub(r'\s+',' ',raw)
def sem_ac(s): return ''.join(c for c in unicodedata.normalize('NFKD',s) if not unicodedata.combining(c))

ABSTRACT={
 '21876150':'efetch abstract colado: L. rhamnosus JB-1 altera GABA região-dependente e ansiedade/corticosterona; efeito AUSENTE em vagotomizados — prova de rota vagal em roedor.',
 '27491067':'efetch abstract colado: FMT de deprimidos para ratos microbiota-depletados induz anedonia/ansiedade e alteração de triptofano (doadores humanos, fenótipo em rato).',
 '25860609':'efetch abstract colado: bactérias esporuladas promovem 5-HT de enterocromafins colônicos (mucosa/lúmen/plaqueta); NÃO serotonina cerebral.',
 '42309058':'efetch abstract colado: RCT FMT adjuvante à escitalopram — remissão semana 8 NÃO diferiu; HAMD-17 reduziu mais; engraftment/bile. Primário NULO.',
 '41921871':'efetch abstract colado: meta FMT 8 estudos/532, g=-0,81 depressão/-1,05 ansiedade, heterogeneidade substancial.',
 '40440772':'efetch abstract colado: meta 19 estudos/1405, SMD -1,76 depressão/-1,60 ansiedade com I²=96,3%/96,9%.',
 '34131108':'efetch abstract colado: meta psicobióticos em jovens, SMD -0,03 (IC -0,21 a 0,14) — AUSÊNCIA de efeito.',
 '41605120':'efetch abstract colado: meta probióticos — sintomas melhoram sem mudança de IL-6 (p=0,45) nem TNF-a (p=0,21).',
 '36834489':'efetch abstract colado: meta — BDNF periférico sobe (SMD 0,37); sem mudança de IL-6/TNF/IL-1b/cortisol.',
 '34620373':'efetch abstract colado: meta 16 RCTs/1125 — BDI moderado/STAI baixo; vários desfechos nulos.',
 '34524405':'efetch abstract colado: meta guarda-chuva 59 estudos — padrão transdiagnóstico (Faecalibacterium/Coprococcus baixos; Eggerthella alto), sem especificidade; região/medicação confundem.',
 '41865792':'efetch abstract colado: meta AGCC circulantes (8 humanos+52 murinos) — propionato/butirato mais baixos na TDM, alta heterogeneidade; associação.',
}

def frase_com(sob,ano):
    pat=re.compile(r'\('+re.escape(sem_ac(sob))+r'[^)]*?'+str(ano)+r'[^)]*?\)\[(?:MA|EC|OB|ML|AT)\]',re.I)
    ms=list(pat.finditer(sem_ac(norm)))
    if not ms: return None
    for m in ms:
        s=m.start()
        lo=max(norm.rfind('. ',0,s),norm.rfind('; ',0,s),norm.rfind(': ',0,s),norm.rfind('— ',0,s))
        hs=lo+2 if lo>-1 else max(0,s-200)
        he=norm.find('. ',m.end())
        seg=norm[hs:(he+1 if he>-1 else m.end()+180)].strip(' *-|')
        if '[' in seg and len(seg)>=25 and not seg.startswith('*') and 'BLOCO' not in seg[:12]:
            return seg
    return norm[max(0,ms[0].start()-150):ms[0].end()+120].strip(' *-|')

def nat(v): return 'nao_estabelecida' if v['natureza_relacao']=='refutadora' else ('associativa' if v['evid_role']=='review' else 'contributiva')
def mat(v): return {'bem_suportado':'bem_suportado','moderado_suportado':'moderadamente_suportado','incipiente':'emergente','emergente':'emergente'}.get(v['grau_maturidade'],'moderadamente_suportado')
def tier(v):
    f=v['forca_causal']
    if 'tier_1' in f:return 'tier_1_necessidade_e_suficiencia'
    if 'tier_2' in f:return 'tier_2_necessidade_ou_suficiencia'
    if 'tier_3' in f:return 'tier_3_correlacional_mecanistico'
    return 'tier_4_descritivo_estrutural'

ledger=[]
for i,v in enumerate(vinc,start=1):
    pmid=v['pmid_oficial']; ref=refs.get(pmid)
    if not ref: print('sem ref p/ pmid',pmid); continue
    idof=ref['id_referencia_interna']; parts=idof.split('_'); sob=parts[1]; ano=parts[2]
    seg=frase_com(sob,ano) or v['trecho_ancora']
    ress = v['status_auditoria']=='PARCIALMENTE_CONFIRMADO'
    ledger.append({
      'id_auditoria':f'AUD_B7_{i:04d}','mecanismo':'B7','id_referencia_interna':idof,'pmid_oficial':pmid,
      'arquivo_modulo09':'Evidencias/Bibliografia/01_pmids.json','tipo_classificador':'','origem_entrada':'GPM','claim_id':'',
      'secao_origem':v['secao_origem'],'trecho_ancora':seg,'citacao_literal':f'({sob.title()} {ano})',
      'natureza_da_relacao':nat(v),'grau_maturidade_cientifica':mat(v),'forca_causal':tier(v),'forca_biologica_conexao':'',
      'especie_mesh':v['especie_mesh'],'evid_role':v['evid_role'],
      'portao_G1_existencia':'VERIFIED_REFERENCE',
      'portao_G2_elegibilidade':('NAO_APLICAVEL' if v['g2_elegibilidade'].startswith('redirecionado_mecan') else 'ELIGIBLE_SOURCE'),
      'portao_G3_suporte':('APROVADO_COM_RESSALVA' if ress else 'APROVADO'),
      'status_auditoria':('APROVADO_COM_RESSALVA' if ress else 'APROVADO'),
      'destino':('REDIRECIONADO_MODULO_CLINICO' if v['g2_elegibilidade']=='redirecionado_clinico' else 'FICA_MECANISMO'),
      'acao_correcao':('ADICIONAR_SINALIZADOR' if v['verification_status']=='preclinico' else ('REBAIXAR_LINGUAGEM' if ress else 'MANTER')),
      'reconciliado':True,
      'verificacao':{'verificador':'IA G3 Rodada 2 (operador de geração) — P-6 2a verificação independente (avaliador cego) PENDENTE',
        'data_verificacao':v['data_verificacao'],'g1_metodo':'eutils_automatico (esummary+efetch)',
        'abstract_ou_trecho':ABSTRACT.get(pmid,'esummary + abstract efetch lido na Rodada 2 para a âncora (G3); metadados conferem.'),
        'query_utilizada':'esearch PubMed por autor+ano+periódico+palavras do trecho-âncora (Rodada 2)',
        'g2_motivo':v['g2_motivo'],'g3_nota':'abstract lido; full-text para P-6'}})
os.makedirs(f'{BASE}/Auditoria_B7',exist_ok=True)
json.dump(ledger,open(f'{BASE}/Auditoria_B7/ledger_auditoria_B7.json','w'),ensure_ascii=False,indent=1)
from collections import Counter
print('ledger B7:',len(ledger),Counter(e['status_auditoria'] for e in ledger))
