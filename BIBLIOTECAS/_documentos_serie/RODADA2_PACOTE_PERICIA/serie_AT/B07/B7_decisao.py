#!/usr/bin/env python3
# B7 — matriz de decisão ref a ref (188 itens da fila real)
import json
BASE='/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro'
f=json.load(open(f'{BASE}/producao/insumos/b7_fila_real.json'))
fila=sorted(f['fila'], key=lambda v:(v['real_ano'],v['real_a1']))

EMAST = {  # 23 masters GPM na fila (7 masters ja vigentes, 8 overlaps no total)
 '38355758':'MASTER GPM — Aburto & Cryan 2024, barreiras GI↔cérebro (arquitetura)',
 '29902437':'MASTER GPM — Agus 2018, microbiota regula metabolismo do triptofano',
 '35229717':'MASTER GPM — Barki 2022, quimiogenética define eixo receptor-AGCC intestino-cérebro',
 '32577079':'MASTER GPM — Bosi 2020, metabólitos do triptofano no eixo (comunicação inter-reinos)',
 '36797287':'MASTER GPM — Caetano-Silva 2023, fibra/AGCC inibem microglia inflamatória',
 '25830558':'MASTER GPM — Carabotti 2015, eixo intestino-cérebro (SNC/SNE)',
 '34127024':'MASTER GPM — Chen LM 2021, Trp-KYN intestino-cérebro na depressão/DII',
 '38939042':'MASTER GPM — Chen N 2024, AGCC cerebral→ACSS2→PPARγ→TPH2 (guarda: sem cadeia clínica completa)',
 '38390241':'MASTER GPM — Cheng 2024, AGCC derivados de microbiota e depressão',
 '34731656':'MASTER GPM — Erny 2021, acetato→aptidão metabólica microglial (formulação específica)',
 '23201091':'MASTER GPM — Guo 2013, LPS→TLR4/CD14→permeabilidade de TJ intestinal',
 '26466961':'MASTER GPM — Guo 2015, LPS→TLR4→FAK/MyD88→TJ',
 '31910709':'MASTER GPM — Kurita 2020, endotoxemia metabólica→neuroinflamação (contexto isquemia experimental)',
 '36746244':'MASTER GPM — Li CC 2023, Trp-KYN intestino+cérebro em ratos com fenótipo depressivo (CRS)',
 '37049591':'MASTER GPM — Lin 2023, disbiose+via KYN como biomarcadores na TDM (ASSOCIATIVE)',
 '29157665':'MASTER GPM — Nighot 2017, LPS→TLR4/MyD88→MLCK→TJ',
 '30711488':'MASTER GPM — Nighot 2019, LPS→TAK-1→IKK→MLCK/MYLK→TJ',
 '37070532':'MASTER GPM — Saikachain 2023, AGCC neuroprotetor via GPR43 (SH-SY5Y, in vitro)',
 '38911967':'MASTER GPM — Sathyasaikumar 2024, IPrA→↑KYNA no cérebro (guarda B7-CAUSAL-02)',
 '38612489':'MASTER GPM — Schwarcz 2024, L. reuteri sintetiza KYNA de KYN (in vitro)',
 '34589808':'MASTER GPM — Spichak 2021, AGCC microbianos→expressão gênica astrocitária sexo-específica',
 '36776388':'MASTER GPM — Zhao 2022, colite DSS→IDO-1→KYN soro+cérebro via microbiota',
 '37386523':'MASTER GPM — Zhou 2023, depressão adolescente humano+camundongo: microbiota regula neurotransmissores derivados de Trp',
}
ENTRA_EXTRA = {
 '30518529':'ENTRA — humano: vesículas extracelulares bacterianas LPS+ sistêmicas aumentadas em disfunção de barreira (janela humana de translocação; SEM ABSTRACT no PubMed → validação G3 título/Gut/autor; claim ASSOCIATIVO)',
 '23885020':'ENTRA — mapa FFAR3/FFAR2 em células EEC (GLP-1/PYY/CCK/GIP/secretina) e neurônios entéricos (sensor intestinal de AGCC; elo metabólito→receptor→via neural)',
 '39998158':'ENTRA — antibióticos orais perturbam BBB e AGCC restauram integridade, em macaco rhesus e camundongo (janela translacional BBB×AGCC; [APENAS PRÉ-CLÍNICO])',
 '34478742':'ENTRA — ZO-1 dispensável para função de barreira mas crítico para reparo mucoso (Gastroenterology; afia o ceticismo da V1 sobre ZO-1 como marcador)',
 '41465592':'ENTRA — única revisão dedicada sais biliares↔eixo gut-brain (FXR/TGR5); ancora mecanisticamente a seção 2.6',
 '39743581':'ENTRA — Nat Rev Microbiol 2025: sinalização neuroepitelial no eixo (janela ausente na V1: neuropods/EEC)',
 '30934533':'ENTRA — única revisão dedicada ao glutamato no eixo intestino-cérebro (elo B5/GABA-glutamato)',
 '39716675':'ENTRA — humano TDM (N=86×120): multiômica microbiota+KYN+inflamação×cognição (claim ASSOCIATIVO por B7-CAUSAL-03)',
}
EXC = {  # malha dura (escopo excluído da série) — expostos
 '35367310':'EXC — pecuária (galinhas DON/C. jejuni)',
 '25888437':'EXC — pecuária (IPEC-J2/porcos neonatos)',
 '29705796':'EXC — pecuária (IPEC-J2)',
 '35736894':'EXC — pecuária (porcino) + fitoterápico (ginsenosídeo)',
 '32131830':'EXC — veterinária (BMC Vet Res, betaina)',
 '32829453':'EXC malha — Alzheimer (revisão disbiose)',
 '32583667':'EXC malha — Alzheimer (acetato GPR41)',
 '35855330':'EXC malha — Alzheimer (AGCC)',
 '36757399':'EXC malha — Alzheimer (AhR)',
 '39833898':'EXC malha — Alzheimer (Akkermansia GPR41/43)',
 '42245509':'EXC malha — neurodegenerativos (eixo microbiota-Trp-cérebro)',
 '41798063':'EXC malha — neurodegenerativos (AGCC epigenéticos)',
 '37960284':'EXC malha — neurodegenerativos (revisão eixo gut-brain)',
 '38360862':'EXC malha — neurodegenerativos (Loh 2024)',
 '33905875':'EXC malha — Parkinson (MPTP, AGCC)',
 '38377788':'EXC malha — Parkinson (α-sinucleína/SCFA)',
 '39904963':'EXC malha — Parkinson (GPR43-NLRP3)',
 '38542172':'EXC malha — esclerose múltipla (SCFA imunomodulação)',
 '31222050':'EXC malha — neuroinflamação autoimune/EAE (SCFA×GPCR)',
 '37264394':'EXC malha — autoimunidade/EAE (GPR43 linfócitos T)',
 '34707612':'EXC malha — epilepsia',
 '33893636':'EXC malha — TCE + epilepsia pós-traumática',
 '41010510':'EXC malha — autismo',
 '35420913':'EXC malha — AVC (envelhecimento, risco/desfecho)',
 '41155363':'EXC malha — AVC (mecanismos microbiota-gut-brain)',
 '40723792':'EXC malha — AVC isquêmico (neuroinflamação)',
}
decisoes=[]
for i,v in enumerate(fila,1):
    pm=v['pmid']
    if pm in EMAST: dec,mo='ENTRA',EMAST[pm]
    elif pm in ENTRA_EXTRA: dec,mo='ENTRA',ENTRA_EXTRA[pm]
    elif pm in EXC: dec,mo='EXC',EXC[pm]
    else: dec,mo='BAIXO',None
    decisoes.append({'n':i,'pmid':pm,'autor':v['real_a1'],'ano':v['real_ano'],'fonte':v['fonte'],'titulo':v['real_titulo'],'pubtype':v['pubtype'],'decisao':dec,'motivo':mo,'doi':v.get('doi'),'decl_autor':v.get('decl_autor'),'decl_ano':v.get('decl_ano')})
tot={'ENTRA':0,'EXC':0,'BAIXO':0}
for x in decisoes: tot[x['decisao']]+=1
assert len(decisoes)==188, len(decisoes)
print('TOTAIS:',tot)
print('ENTRA:',[x['autor']+' '+x['ano'] for x in decisoes if x['decisao']=='ENTRA'])
print()
print('EXC:',len([x for x in decisoes if x['decisao']=='EXC']))
# gravar rascunho (BAIXO sem motivo ainda)
json.dump({'totais':tot,'itens':decisoes}, open(f'{BASE}/producao/insumos/matriz_b7_decisao_draft.json','w'), ensure_ascii=False, indent=1)
# conferir especificos
for pm in ['39408347','36758839','40137174','38102897']:
    x=[d for d in decisoes if d['pmid']==pm]
    print(pm,'->',x[0]['decisao'] if x else 'AUSENTE', (x[0]['titulo'][:70] if x else ''))
