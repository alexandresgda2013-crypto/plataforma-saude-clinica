#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consolida os checkpoints na Biblioteca PRE-CANONICA unica, com as secoes
exigidas pelo Checklist Estrutural (TABELA DE EVIDENCIAS, CONTROVERSIAS,
ELEMENTOS MOLECULARES CRITICOS, MARCADORES_PARA_JSON, ancoras [REF_BLOCO_XX],
BLOCO_12 N/A) e reconstrói o Modulo 9 consolidado."""
import re, json, glob
from pathlib import Path
BASE=Path(__file__).resolve().parent
out=BASE/"ato2_pacote"

def limp_pmid(t):
    t=re.sub(r',?\s*PMID\s*\d+','',t)
    t=re.sub(r'\(BLOCO\d+[.\d]*,\s*\)','',t)
    return re.sub(r'[ \t]{2,}',' ',t)

# ---- reconstroi N1/N2 consolidados a partir dos mod9_BLOCO ----
pmap={}
for f in sorted(glob.glob(str(out/"mod9_BLOCO*_N1_01_pmids.json"))):
    for r in json.load(open(f)):
        r=dict(r); p=r['pmid_oficial']
        iid=r.pop('id_referencia_interna')
        if p not in pmap:
            r['ids_referencia_interna']=[iid]; pmap[p]=r
        else:
            if iid not in pmap[p]['ids_referencia_interna']:
                pmap[p]['ids_referencia_interna'].append(iid)
refs=sorted(pmap.values(), key=lambda x:x['pmid_oficial'])
meta=json.load(open(out/"mod9_BLOCO05_02_meta_analises.json"))
n2=[]
for f in sorted(glob.glob(str(out/"mod9_BLOCO*_N2_vinculos.json"))):
    for v in json.load(open(f)):
        v['trecho_ancora']=limp_pmid(v['trecho_ancora']).strip()
        n2.append(v)
for i,v in enumerate(n2,1): v['id_vinculo']=f'VINC_B1_{i:04d}'
id2pmid={}
for r in refs:
    for i in r['ids_referencia_interna']: id2pmid[i]=r['pmid_oficial']
for r in meta: id2pmid[r['id_referencia_interna']]=r['pmid_oficial']
for v in n2: v['pmid_oficial']=id2pmid.get(v['id_referencia_interna'])

ev=out/'Evidencias'
json.dump(refs, open(ev/'Bibliografia/01_pmids.json','w'), ensure_ascii=False, indent=1)
json.dump(meta, open(ev/'Bibliografia/02_meta_analises.json','w'), ensure_ascii=False, indent=1)
json.dump(n2, open(ev/'Vinculos/vinculos_referencia_afirmacao.json','w'), ensure_ascii=False, indent=1)

# ---- ancora [REF_BLOCO_XX] por bloco (chaves unicas de refs citadas) ----
import collections
refs_por_bloco=collections.defaultdict(set)
for v in n2:
    m=re.search(r'BLOCO_?(\d+)', v['secao_origem']) or re.search(r'BLOCO(\d+)', v['claim_id'])
    if m:
        b=int(m.group(1))
        refs_por_bloco[b].add(v['id_referencia_interna'])
def ancora(b):
    ids=sorted(refs_por_bloco.get(b,set()))
    # blocos 01 e 08 usam secao_origem com formato proprio; garante suas refs
    extras={1:['REF_Swanson_2019','REF_Serhan_2014','REF_Serhan_Levy_2018','REF_Perry_Teeling_2013','REF_Barrientos_2015','REF_Norden_2015','REF_Dantzer_2001','REF_Dantzer_2006','REF_Harden_2015','REF_OConnor_2009'],
            8:['REF_GR_repress_2018','REF_Poda_2012','REF_GutLPS_2024','REF_D2_LPS_2004','REF_Klengel_2013','REF_VitD_2024','REF_SleepInflam_2023']}
    ids=sorted(set(ids)|set(extras.get(b,[])))
    role_tipo={'human_clinical':'EC','human_experimental':'EC','post_mortem':'EC','preclinical_mechanistic':'ML'}
    partes=[]
    for i in ids:
        r=next((x for x in refs if i in x['ids_referencia_interna']), None) or next((x for x in meta if x['id_referencia_interna']==i),None)
        if not r: continue
        tipo='MA' if 'meta' in str(r.get('desenho_estudo','')).lower() else role_tipo.get(r.get('evid_role',''),'OB')
        nome=i.replace('REF_','')
        partes.append(f"{nome}[{tipo}]")
    return f"[REF_BLOCO_{b:02d}: " + " | ".join(partes) + "]"

# ---- corpo dos blocos ----
bloco00 = (out/'_bloco00.md').read_text(encoding='utf-8') if (out/'_bloco00.md').exists() else None
ordem=[1,2,3,4,5,6,7,8,9,10,11]
fix={3:("## BLOCO_03 — BIOLOGIA CELULAR: MICRÓGLIA, ASTRÓCITOS, BARREIRA E COMUNICAÇÃO IMUNE-CÉREBRO",
        "## BLOCO_03 — MEDIADORES ESPECÍFICOS (CITOCINAS, QUIMIOCINAS)")}
partes=[]
for n in ordem:
    cp=(out/f'CHECKPOINT_{n:02d}_BLOCO{n:02d}.md').read_text(encoding='utf-8')
    i=cp.find('## BLOCO'); j=cp.find('# MODULO 9')
    corpo=limp_pmid(cp[i:j].strip() if j>0 else cp[i:].strip())
    if n in fix: corpo=corpo.replace(fix[n][0],fix[n][1])
    corpo += "\n\n" + ancora(n)
    partes.append(corpo)

# BLOCO_12 (N/A explicito)
bloco12 = """## BLOCO_12 — CENÁRIOS CLÍNICOS ILUSTRATIVOS

**Status: N/A nesta Rodada 2.**
O BLOCO_12 depende de subtipos clínicos biologicamente documentados no BLOCO_11. O BLOCO_11 descreve o substrato mecanístico do subtipo "depressão inflamatória" e lista candidatos futuros (TRD, perinatal, TEPT, geriátrica), mas estes ainda não foram convertidos em subtipos formais com cenário próprio — decisão registrada na Lista Canônica (nota de candidatos futuros). Portanto, em conformidade com a regra de dependência arquitetural, o BLOCO_12 é declarado **N/A — a desenvolver quando os subtipos do BLOCO_11 forem formalizados**. Nenhum conteúdo terapêutico (fármaco/protocolo/conduta) é inserido aqui, por design.

[REF_BLOCO_12: —]
"""

secoes_fim = (out/'_secoes_fim.md').read_text(encoding='utf-8') if (out/'_secoes_fim.md').exists() else ""

cab=(f"# B1 — NEUROINFLAMAÇÃO\n## Biblioteca de Conhecimento Científico — Clinical Dominion\n"
 f"### Versão PRÉ-CANÔNICA · Rodada 2 (Prompt PMID v4.2 + GPM v3)\n\n"
 f"**Mecanismo:** mecanismo_B1_neuroinflamacao · **Data:** 2026-09-03\n"
 f"**Fonte primária:** GPM_B1_NEUROINFLAMACAO_v3 · 7ª Lista Canônica (trilha mecanística)\n"
 f"**G1 (ferramenta):** NCBI eutils (esearch+efetch) · {len(refs)} referências com PMID real e abstract baixado.\n"
 f"**Status:** PRÉ-CANÔNICA — toda referência `CANDIDATO`, `verification_status=pending`, `g3_verificado_por=\"\"`. "
 f"G2/G3 são da auditoria, não desta geração.\n\n"
 f"**Módulo 9 (arquivos separados, mesma Rodada 2):**\n"
 f"- N1 `/Evidencias/Bibliografia/01_pmids.json` ({len(refs)} refs, schema 09.1)\n"
 f"- N1 `/Evidencias/Bibliografia/02_meta_analises.json` ({len(meta)} metas, schema 09.2)\n"
 f"- N1 `/Evidencias/Bibliografia/03_ensaios_clinicos.md` (1 RCT, template 09.3)\n"
 f"- N2 `/Evidencias/Vinculos/vinculos_referencia_afirmacao.json` ({len(n2)} vínculos, trecho_ancora literal por sentença — E3)\n\n"
 f"> Espécie declarada em cada vínculo (`especie_mesh`,`evid_role`); extrapolação marcada (`extrapolacao_por_analogia`, [ML]/[OB]/[EXT]). TOC fora do escopo central.\n\n---\n\n")

documento=cab+(bloco00+"\n\n---\n\n" if bloco00 else "")+("\n\n---\n\n".join(partes))+"\n\n---\n\n"+bloco12+"\n\n---\n\n"+secoes_fim
(out/'BIBLIOTECA_B1_NEUROINFLAMACAO_PRE_CANONICA.md').write_text(documento,encoding='utf-8')
print("Biblioteca unica:", len(documento),"chars,",len(documento.split()),"palavras")
print("refs:",len(refs),"| metas:",len(meta),"| vinculos:",len(n2))
