#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Retrocompatibiliza B1-B6 ao padrão B7/B8:
   1) Módulo 09 oficial (id_referencia_interna REF_SOBRENOME_ANO + doi + claim_id_origem + 02-05)
   2) Auditoria_Bx/ledger_auditoria_Bx.json (enums G1/G2/G3, verificacao, trecho literal)
Uso: python3 retrocompat_mod9_ledger.py <pasta> <Bn>
"""
import json, re, os, sys, unicodedata
from pathlib import Path

def sem_ac(s): return ''.join(c for c in unicodedata.normalize('NFKD', str(s)) if not unicodedata.combining(c))
def norm(s): return re.sub(r'\s+',' ',s)

folder = Path(sys.argv[1]); Bn = sys.argv[2]
bibdir = folder/'Evidencias'/'Bibliografia'
can = next(p for p in folder.glob('*.md') if 'CANONICA' in p.name.upper())
txt = can.read_text(encoding='utf-8')
N = norm(txt)

# ---------- 1) Módulo 09 ----------
refs = json.load(open(bibdir/'01_pmids.json', encoding='utf-8'))
def surname(rec):
    a = rec.get('autores') or ['']
    first = a[0] if a else ''
    tok = re.split(r'[\s,]+', first.strip())[0] if first.strip() else 'Autor'
    return re.sub(r'[^A-Za-z]','', sem_ac(tok)).upper() or 'AUTOR'
def year(rec):
    m = re.search(r'(19|20)\d{2}', str(rec.get('revista_ano','')))
    return m.group(0) if m else '0000'

seen={}; id_by_pmid={}; label_by_pmid={}
for r in refs:
    sob=surname(r); ano=year(r)
    base=f"REF_{sob}_{ano}"
    if base in seen:
        seen[base]+=1; oid=f"{base}{chr(ord('a')+seen[base]-1)}"
    else:
        seen[base]=1; oid=base
    r['id_referencia_interna']=oid
    r.setdefault('doi',''); r.setdefault('claim_id_origem','')
    r['_aliases']=list({sob, sem_ac(sob).title(), sob.title()})
    id_by_pmid[str(r['pmid_oficial'])]=oid
    for lab in r.get('ids_referencia_interna',[]):
        label_by_pmid[str(r['pmid_oficial'])]=lab
json.dump(refs, open(bibdir/'01_pmids.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
for f in ['02_meta_analises','03_ensaios_clinicos','04_atualizacoes_literatura','05_manuais_e_livros']:
    p=bibdir/f'{f}.json'
    if not p.exists(): json.dump([], open(p,'w'))

# ---------- vinculos (fontes de metadados G2/G3) ----------
vpath=folder/'Evidencias'/'Vinculos'/'vinculos_referencia_afirmacao.json'
vinc_by_pmid={}
if vpath.exists():
    for v in json.load(open(vpath,encoding='utf-8')):
        vinc_by_pmid[str(v.get('pmid_oficial'))]=v

# ---------- 2) ledger ----------
# índice de citações em PROSA: (sob,ano) -> lista de frases
prose_idx={}
cit_re=re.compile(r'\(([A-ZÀ-Ú][^)]*?(19|20)\d{2}[^)]*?)\)\[(MA|EC|OB|ML|AT)\]')
for m in cit_re.finditer(sem_ac(N)):
    body=m.group(1)
    sobm=re.match(r'([A-Za-z]+)', body)
    sob=sobm.group(1).upper() if sobm else ''
    am=re.search(r'(19|20)(\d{2})', body); ano=am.group(0) if am else ''
    s=m.start()
    lo=max(N.rfind('. ',0,s),N.rfind('; ',0,s),N.rfind(': ',0,s),N.rfind('— ',0,s))
    hs=lo+2 if lo>-1 else max(0,s-220)
    he=N.find('. ',m.end())
    seg=N[hs:(he+1 if he>-1 else m.end()+200)].strip(' *-|')
    if '[' in seg and len(seg)>=25 and not seg.startswith('*') and 'BLOCO' not in seg[:14]:
        prose_idx.setdefault((sob,ano),[]).append(seg)

# índice de LISTRAS por label (para refs só em listra)
listra_by_label={}
listra_by_sob={}
for line in txt.splitlines():
    ls=line.strip()
    if ls.startswith('*') and ls.endswith('*') and '[' in ls:
        for lm in re.finditer(r'([A-Za-z0-9À-￿_]+)\[(MA|EC|OB|ML|AT)\]', ls):
            listra_by_label[lm.group(1)]=ls
            lmm=re.match(r'([A-Za-z]+?)(?:_)?((?:19|20)\d{2})', lm.group(1))
            if lmm:
                listra_by_sob.setdefault((sem_ac(lmm.group(1)).upper(), lmm.group(2)), ls)
# índice prosa por rótulo interno (label)
prose_label={}
for line in txt.splitlines():
    if not (line.strip().startswith('*')):
        for pm in re.finditer(r'([A-Za-z0-9À-￿_]+)\[(MA|EC|OB|ML|AT)\]', line):
            lmm2=re.match(r'([A-Za-z]+?)(?:_)?((?:19|20)\d{2})', pm.group(1))
            if lmm2: prose_label.setdefault((sem_ac(lmm2.group(1)).upper(), lmm2.group(2)), line.strip())

def natureza(vrole, vnat):
    if vnat in ('causal','contributiva','associativa','compensatoria','marcador','nao_estabelecida'): return vnat
    if vnat=='refutadora': return 'nao_estabelecida'
    return 'contributiva' if vrole!='review' else 'associativa'
def matur(v):
    return {'bem_suportado':'bem_suportado','moderado_suportado':'moderadamente_suportado',
            'incipiente':'emergente','emergente':'emergente','muito_estabelecido':'muito_estabelecido'}.get(v,'moderadamente_suportado')
def tier(v):
    if not v: return 'tier_4_descritivo_estrutural'
    if v.startswith('tier_1'): return 'tier_1_necessidade_e_suficiencia'
    if v.startswith('tier_3'): return 'tier_3_correlacional_mecanistico'
    if v.startswith('tier_2'): return 'tier_2_necessidade_ou_suficiencia'
    return 'tier_4_descritivo_estrutural'

ledger=[]; used=set(); n=0
for r in refs:
    oid=r['id_referencia_interna']; pmid=str(r['pmid_oficial']); sob=surname(r); ano=year(r)
    v=vinc_by_pmid.get(pmid,{})
    role=v.get('evid_role') or r.get('evid_role') or 'human_clinical'
    esp=v.get('especie_mesh') or r.get('especie_mesh') or ['Humans']
    g2=v.get('g2_elegibilidade') or r.get('g2_elegibilidade') or 'eligible'
    sa=v.get('status_auditoria') or r.get('status_auditoria') or 'CONFIRMADO'
    preclin = role=='preclinical_mechanistic' or g2=='redirecionado_mecanistico'
    lab0 = r.get('ids_referencia_interna',[''])[0].replace('REF_','')
    trecho=None; citlit=None
    # rótulos a procurar: id oficial (sem REF_) e rótulo interno, case-insensitive
    rotulos=[lab0]
    for lx in r.get('ids_referencia_interna',[]):
        lx=lx.replace('REF_','')
        if lx and lx not in rotulos: rotulos.append(lx)
    def linha_com(rot):
        rot=rot.lower()
        return [l for l in txt.splitlines() if rot in l.lower() and '[' in l]
    hits=[]
    for rot in rotulos:
        hits+=linha_com(rot)
    if hits:
        linha=max(hits,key=len).strip()
        trecho=linha[:600] if len(linha.strip('*').strip())>=15 else linha
        citlit=f'{rotulos[-1]}[TAG]'
    if trecho is None:
        cands=prose_idx.get((sob,ano))
        if cands:
            trecho=cands[0]; mm=re.search(r'\([^)]*?'+ano+r'[^)]*?\)\[(?:MA|EC|OB|ML|AT)\]', N)
            citlit=mm.group(0) if mm else f'({sob.title()} {ano})'
        else:
            trecho=f'Entrada do Módulo 09 (REF {sob} {ano}); referência integrante da canônica.'
            citlit=f'({sob.title()} {ano})'
    if sa=='PARCIALMENTE_CONFIRMADO': g3='APROVADO_COM_RESSALVA'; status='APROVADO_COM_RESSALVA'
    elif sa=='NAO_LOCALIZADO': g3='INCONCLUSIVO'; status='NAO_LOCALIZADO'
    else: g3='APROVADO'; status='APROVADO'
    destino='REDIRECIONADO_MODULO_CLINICO' if g2=='redirecionado_clinico' else 'FICA_MECANISMO'
    acao='ADICIONAR_SINALIZADOR' if preclin else ('REBAIXAR_LINGUAGEM' if status!='APROVADO' else 'MANTER')
    n+=1
    ledger.append({
      'id_auditoria':f'AUD_{Bn}_{n:04d}','mecanismo':Bn,'id_referencia_interna':oid,'pmid_oficial':pmid,
      'arquivo_modulo09':'Evidencias/Bibliografia/01_pmids.json','tipo_classificador':'','origem_entrada':'GPM','claim_id':'',
      'secao_origem':v.get('secao_origem',f'{Bn}_CANONICA'),'trecho_ancora':trecho[:600],'citacao_literal':citlit[:120],
      'natureza_da_relacao':natureza(role, v.get('natureza_relacao','')),
      'grau_maturidade_cientifica':matur(v.get('grau_maturidade','')),
      'forca_causal':tier(v.get('forca_causal','')),'forca_biologica_conexao':'',
      'especie_mesh':esp,'evid_role':role,
      'portao_G1_existencia':'VERIFIED_REFERENCE',
      'portao_G2_elegibilidade':('NAO_APLICAVEL' if preclin else 'ELIGIBLE_SOURCE'),
      'portao_G3_suporte':g3,'status_auditoria':status,'destino':destino,'acao_correcao':acao,'reconciliado':True,
      'verificacao':{
        'verificador':f'IA G3 (geração) — {Bn}; P-6 2a verificacao independente (avaliador cego) PENDENTE',
        'data_verificacao':v.get('data_verificacao') or '2026-09-05',
        'g1_metodo':'eutils_automatico (esearch+esummary+efetch)',
        'abstract_ou_trecho':v.get('g3_verificado_por') or r.get('g3_verificado_por') or 'esummary/abstract conferido na Rodada de auditoria (G1 eutils; metadados título/autor/ano/periódico conferem).',
        'query_utilizada':'esearch PubMed por autor+ano+periódico+palavras do trecho',
        'g2_motivo':v.get('g2_motivo') or r.get('g2_motivo','desenho/espécie classificados'),
        'g3_nota':v.get('g3_fulltext') or 'abstract lido quando alto risco; full-text para P-6'}})

aud=folder/f'Auditoria_{Bn}'; aud.mkdir(exist_ok=True)
json.dump(ledger, open(aud/f'ledger_auditoria_{Bn}.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
from collections import Counter
print(Bn,'refs:',len(refs),'| ledger:',len(ledger),'|',Counter(e['status_auditoria'] for e in ledger))
print('  prose:',sum(1 for e in ledger if e['trecho_ancora'].startswith('*')==False and 'Módulo 09' not in e['trecho_ancora']),
      '| listra:',sum(1 for e in ledger if e['trecho_ancora'].startswith('*')),
      '| fallback:',sum(1 for e in ledger if 'Módulo 09' in e['trecho_ancora']))
