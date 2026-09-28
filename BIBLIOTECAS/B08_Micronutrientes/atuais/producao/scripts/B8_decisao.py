#!/usr/bin/env python3
# B8 — matriz de decisão ref a ref (91 itens da fila)
import json
BASE='/home/user/BIBLIOTECAS/B08_Micronutrientes'
G=json.load(open(f'{BASE}/producao/insumos/matriz_b8_g1.json'))
C=json.load(open(f'{BASE}/producao/insumos/b8_cruzamento.json'))
fila=set(C['fila'])
MAST={'22796576':'Eyles 2013 — vit D neurobiologia/desenvolvimento (master)',
'25365455':'Du 2016 — nutrientes protegem mitocôndria/neurotransmissão; depressão/TEPT/suicídio (master)',
'26828517':'Kennedy 2016 — complexo B e cérebro: mecanismos (master-teto)',
'28202095':'Firth 2017 supl — SR/MA suplementação vit/mineral em esquizofrenia (master; janela-sinal adjuvante)',
'29206972':'Firth 2017 FEP — MA deficiências no 1º episódio psicótico = STATUS (master)',
'30201141':'Wesselink 2019 — cofatores nutricionais mitocondriais (master; ponte B9)',
'30341413':'Barks 2019 — ferro como modelo de origem nutricional neuropsiquiátrica (master)',
'32552785':'Plevin 2020 — SR vit C neuropsiquiatria: associação SEM prova intervencional (master; bloco NEG)',
'33428888':'Rudzki 2021 — vitaminas derivadas de microbiota (master; ponte B7)',
'33500553':'Cui 2021 — vit D e esquizofrenia 20 anos (master)',
'33763446':'Muscaritoli 2021 — nutrientes e saúde mental (master)',
'33904124':'Shayganfard 2022 — oligoelementos essenciais × transtornos mentais (master)',
'34836113':'Barks 2021 — deficiência de ferro precoce programa epigenoma do hipocampo (master; animal)',
'35223256':'Badar 2022 — B12 neuropsiquiatria, relato de caso = possibilidade clínica (master)',
'35294077':'Barone 2022 — microbioma×biodisponibilidade de minerais/vitaminas (master; ponte B7)',
'35337631':'Sahu 2022 — manifestações neuropsiquiátricas da deficiência de B12 (master)',
'36173945':'McWilliams 2022 — scoping ferro×neurodesenvolvimento (master)',
'36411563':'Nogueira-de-Almeida 2023 — SR neuronutrientes×SNC (master)',
'37147046':'Fiani 2023 — ferro em ADHD/TEA/internalizantes/movimento (master; associativo)',
'37836413':'Lahoda Brodska 2023 — micronutrientes em transtornos neurológicos (master)',
'38203763':'Mathew 2024 — B12 e sistema nervoso além da decompensação metabólica (master-teto B12)',
'38462972':'Berger 2024 — deficiências e suplementos em escolares (master; método/regra 11)',
'38605872':'Rajasekar 2024 — dieta+suplementação vit D/B6/Mg e sintomas depressivos, saúde pública (master)',
'38630748':'Al Jassem 2024 — B12×sintomas neuropsiquiátricos (Líbano, veg/omn) (master)',
'38999789':'Hui 2024 — SNP-micronutriente×saúde mental, MR (master)',
'39596221':'Scuto 2024 — nutrientes funcionais, sinalização redox e neuroesteroides (master; pontes B6/B14)',
'39703999':'Rucklidge 2025 — Annual Research Review micronutrientes×saúde mental pediátrica (master)',
'39829265':'Rajen 2025 — status de folato prejudicado em transtornos mentais (master)',
'39952338':'Ye 2025 — SR+MA(+MR) vitaminas B×neuropsiquiatria: relações distintas por vit×transtorno (master)',
'40100400':'Anmella 2025 — B12 baixa×depressão/espectro em internados infantojuvenis (master; associativo)',
'40218925':'Faugere 2025 — vit D/B9/B12 como drivers de severidade/comorbidade (master; associativo)',
'40289952':'Domański 2025 — correlações hematológicas predizem manifestações em internados psiquiátricos (master)',
'40329546':'Radoeva 2025 — ingestão estimada×problemas psiquiátricos/sono em jovens autistas ABCD (master; regra 5; TEA=fronteira ilustrativa)',
'40653891':'Astorino 2025 — etiologia multifacetada com foco em oligoelementos (master)',
'40739033':'Lu & Paterson 2025 — MR B12 sérica×transtornos/cognição: efeito NÃO uniforme (master)',
'40871684':'Skoczek-Rubińska 2025 — vit D status/suplementação×BDNF e humor-cognição (master)',
'41303365':'Faa 2025 — perturbações da homeostase do zinco e transtornos neuropsiquiátricos (master)',
'42029584':'Alexa 2026 — paradoxo nutricional da obesidade: deficiências com excesso (master)',
'42144425':'Shahini 2026 — micronutriente-imune em humor e psicose (vit C, ferro, Zn, Mg, índices celulares) (master; caso-controle)',
'42187879':'Moroianu 2026 — SR+MA exploratória vit D/B12 status e suplementação em psiquiatria (master; NEG eficácia)',
'42253799':'Tortajada 2026 — SR desfechos clínicos de suplementação pró-mitocondrial em psiquiatria (master; ponte B9)'}
ENTRA_EXTRA={
 '17066210':'ENTRA RESGATE — Bourre 2006 (J Nutr Health Aging, Part 1 micronutrientes): âncora bioquímica das claims .001–.002; briefing dava NAO-IDX, existe (17066210)',
 '30953290':'ENTRA RESGATE — Mattei 2019 (Curr Nutr Rep: Micronutrients and Brain Development): âncora das claims .001–.003; briefing a "fundiu" com McWilliams por engano — são distintas',
 '34695501':'ENTRA — Ferriani 2022 ELSA-Brasil (N≈14,7 mil): ingestão de Se/Zn/B6/B12 inversamente associada a depressão (humano ASSOCIATIVO; ingestão≠status — B8-Causal-05)',
 '30692033':'ENTRA — Moore 2019 coorte TUDA: vitaminas B (incl. status bioquímico)×depressão em idosos >60 (humano ASSOCIATIVO)',
 '41515142':'ENTRA — Kohl 2025: vit D def/insuf×transtornos mentais comuns em mulheres trabalhadoras (humano ASSOCIATIVO, população não psiquiátrica)',
 '41228551':'ENTRA — Islam 2025 SR: níveis de micronutrientes×depressão perinatal (ASSOCIATIVO; janela desfecho direto ausente nas masters)',
 '42044701':'ENTRA — Yang 2026: vit D×depressão — remodelamento sináptico por complemento e sinalização VDBP-megalin (janela molecular nova; OB)',
 '40379361':'ENTRA — Horsdal 2025 Lancet Psychiatry: caso-coorte nacional dinamarquesa; vit D NEONATAL×6 transtornos incl. TDM (humano ASSOCIATIVO de alto peso; desenvolvimento)'}
EXC={
 '29773950':'EXC — autismo (status nutricional Palestina)','30570388':'EXC — autismo (Hainan)','30959831':'EXC — anorexia nervosa (malha de escopo permanente)',
 '34802410':'EXC — neurodegenerativos (Kumar 2022)','37754219':'EXC — delirium (condição aguda neurocognitiva hospitalar, fora do miolo)',
 '36836486':'EXC — autismo (medicina de precisão)','39076846':'EXC — epilepsia (MR)','39133336':'EXC — botânica (oxstress em plantas)',
 '40362647':'EXC — autismo (SR/MA biomarcadores)','40290005':'EXC — autismo (prevalência EUA)','41769656':'EXC — Alzheimer (Miteva 2026)',
 '35451454':'EXC — demência/AVC/neuroimagem (Navale 2022, UK Biobank): conteúdo real na malha excluída; resgatada do apagamento do briefing, mas fica fora com honestidade'}
decisoes=[]
itens=[]
for k,e in G['ok'].items():
    if e['pmid'] in fila:
        itens.append({'pmid':e['pmid'],'autor':e['real_a1'],'ano':e['real_ano'],'titulo':e['real_titulo'],'fonte':e['fonte'],'pubtype':e['pubtype'],'doi':e['doi']})
b=G['por_pmid']['Bourre, 2006']
itens.append({'pmid':b['pmid'],'autor':b['real_a1'],'ano':b['real_ano'],'titulo':b['real_titulo'],'fonte':b['fonte'],'pubtype':b['pubtype'],'doi':None})
itens.sort(key=lambda x:(x['ano'],x['autor']))
for i,x in enumerate(itens,1):
    pm=x['pmid']
    if pm in MAST: dec,mo='ENTRA','MASTER GPM — '+MAST[pm]
    elif pm in ENTRA_EXTRA: dec,mo='ENTRA',ENTRA_EXTRA[pm]
    elif pm in EXC: dec,mo='EXC',EXC[pm]
    else: dec,mo='BAIXO',None
    decisoes.append({'n':i,'pmid':pm,'autor':x['autor'],'ano':x['ano'],'fonte':x['fonte'],'titulo':x['titulo'],'pubtype':x['pubtype'],'decisao':dec,'motivo':mo,'doi':x['doi']})
tot={}
for x in decisoes: tot[x['decisao']]=tot.get(x['decisao'],0)+1
print('TOTAIS:',tot,'| soma',sum(tot.values()))
assert sum(tot.values())==91
json.dump({'totais':tot,'itens':decisoes}, open(f'{BASE}/producao/insumos/matriz_b8_decisao_draft.json','w'), ensure_ascii=False, indent=1)
b=[x for x in decisoes if x['decisao']=='BAIXO']
print('BAIXO:',len(b))
for x in b: print('  -',x['pmid'],x['autor'],x['ano'],'|',x['titulo'][:64])
