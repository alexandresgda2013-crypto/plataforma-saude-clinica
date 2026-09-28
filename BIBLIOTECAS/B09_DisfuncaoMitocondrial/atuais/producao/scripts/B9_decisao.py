#!/usr/bin/env python3
# B9 — matriz de decisão da fila (151) → producao/insumos/matriz_b9_decisao.json
import json
BASE='/home/user/BIBLIOTECAS/B09_DisfuncaoMitocondrial'
cr=json.load(open(f'{BASE}/producao/insumos/b9_cruzamento.json'))
ef=json.load(open(f'{BASE}/producao/insumos/b9_efetch_all.json'))

# masters GPM (44 no fila; 4 das 47 âncoras já vigentes: Karabatsiakis2014/Fernström2021/Gebara2020/Scaini2021)
MASTERS={'24632637','29292494','25486875','26687620','38857809','28114303','25820230','38161720','29068134','25946463','30687139','37985735','32488052','31760107','41921723','26621716','35065970','32647150','34948180','32260327','42248856','29453441','19546216','39333279','34066918','34829696','23434681','38081963','33672477','18230723','37563104','29106705','41848740','35732695','40410878','32351669','36252817','32045672','40668505','41634133','33742459','21613270','40149969','39197553'}

# 32 ENTRA extras (motivos inline)
EXTRA={
'29928190':'ENTRA — Allen 2018 (Front Neurosci): revisão-âncora "Mitochondria and Mood" — arquitetura do campo (hipótese Mito-Mood)',
'40517524':'ENTRA — Beck 2025 (Psychoneuroendocrinology): ELS × condições psiquiátricas × mtDNAcn em jovens saudáveis (humano)',
'27412728':'ENTRA — Bergman 2016 (Can J Psychiatry): revisão OXPHOS em esquizofrenia — FRONTEIRA ILUSTRATIVA (não escopo causal)',
'36686690':'ENTRA — Büttiker 2022 (Front Pharmacol): revisão processos mitocondriais disfuncionais × sintomas neuropsiquiátricos (ausente do §3/§6 do briefing — cobertura exposta)',
'31639552':'ENTRA — Chung 2019: mtDNA-CN em pacientes com TDM (humano)',
'41776167':'ENTRA — Cullen 2026 (JA): ATP/bioenergética e fadiga em adultos jovens com e sem TDM (humano funcional)',
'31081430':'ENTRA — Czarny 2020: mtDNA — cópia, dano, reparo e degradação em depressão (humano)',
'37834200':'ENTRA — Czarny 2023: SNPs em genes de estabilidade do mtDNA em depressão (humano)',
'34295268':'ENTRA — Giménez-Palomo 2021 (Eur Neuropsychopharmacol): revisão papel da mitocôndria em transtornos do humor (distinta da vigente 2024)',
'37587338':'ENTRA — Gupta 2023: controle genético nuclear do mtDNA-CN/heteroplasmia em humanos (arquitetura M04)',
'38800537':'ENTRA — Hofstra 2024 (Neurobiol Stress): resposta de estresse mitocondrial cross-species em depressão/ELS/hipocampo — âncora UPRmt/ISR integrada (pendência §8 do briefing)',
'38334212':'ENTRA — Jiang 2024: mitocôndria na depressão — disfunção do metabolismo energético (revisão)',
'36841465':'ENTRA — Kalimon 2023 [ML]: MAO (membrana mitocondrial externa) — inibição de MAO-A aumenta respiração em mitocôndrias de córtex de camundongo (ponte B9↔B4)',
'29102411':'ENTRA — Kasahara 2018: revisão "o que a análise do mtDNA diz sobre transtornos do humor"',
'30585734':'ENTRA — Kim 2019: revisão mitocôndria, metabolismo e redox em transtornos psiquiátricos',
'34742335':'ENTRA — Klein 2021: caracterização de quantidade/qualidade do mtDNA no cérebro humano (referência anatômica; sangue≠SNC)',
'34098028':'ENTRA — Kolár 2021: mini-revisão do metabolismo energético cerebral em modelos animais de depressão',
'37344456':'ENTRA — Liu L 2023 (Transl Psychiatry): MiWAS UK Biobank — interação mtDNA×CRP × ansiedade (N=72 mil)/depressão (ponte B9×B1, humano)',
'40427494':'ENTRA — Liu X 2025 (Antioxidants): eixo ferroptose-mitocôndria na depressão (fronteira B6, emergente)',
'31755286':'ENTRA — Ľupták 2019: revisão mitocôndria e efeito dos estabilizadores de humor (âncora confundidor-medicação M08.9)',
'32564227':'ENTRA — Morris 2020: revisão interplay estresse oxidativo × falha bioenergética em vias neuroprogressivas',
'19290059':'ENTRA — Rollins 2009: variantes mitocondriais em esquizofrenia, bipolar e TDM (humano; inclui fronteira)',
'36216200':'ENTRA — Ryan 2023: mtDNA-CN em sangue total na depressão e resposta ao tratamento (humano)',
'28463235':'ENTRA — Scaini 2017 (Transl Psychiatry): via apoptótica e dinâmica da rede mitocondrial em cérebro PÓS-MORTEM (humano, CAMADA A forte)',
'26011537':'ENTRA — Sequeira 2015: mutações mitocondriais em indivíduos com transtornos psiquiátricos (humano)',
'29984425':'ENTRA — Tranah 2018: heteroplasmia m.13514G>A associada a depressão (humano)',
'29500956':'ENTRA — Tymofiyeva 2018: mtDNA alto associado a medidas de imagem cerebral em adolescentes (humano)',
'35085849':'ENTRA — Valiente-Pallejà 2022: SR abrangente de alterações de mtDNA em cérebro pós-mortem (humano)',
'28647451':'ENTRA — Wang X 2017: associação de mtDNA em sangue periférico com depressão (humano)',
'28153046':'ENTRA — Wei 2017: mutações pontuais e CN relativa do mtDNA em amostra depressão (humano)',
'40915505':'ENTRA — Yin 2026: análise completa da sequência do mtDNA em pacientes com TDM (humano)',
'41792945':'ENTRA — Zong 2026: variantes genéticas do mtDNA associadas a depressão (humano)',
}
EXC={
'39223276':'EXC — autismo (Khaliulin 2025; Mol Psychiatry — papel da mitocôndria no TEA); malha de escopo',
'29065167':'EXC — fadiga crônica/CFS (Tomas 2017); o GPM M10 declara CFS fora da cobertura',
'28131082':'EXC — diabetes tipo 2 (Rovira-Llopis 2017); CAMADA E contexto metabólico, fora do fenótipo',
'41344231':'EXC — transtorno por uso de metanfetamina (Aytaç 2025); fora do fenótipo ansiedade/depressão',
'39313624':'EXC — demência/risco cognitivo (Tian Q 2025; UK Biobank n=189 mil); malha de escopo',
'33774476':'EXC — Alzheimer (Park 2021; NOX4-ferroptose de astrócitos centrado em DA); malha de escopo',
}
OVERRIDE_BAIXO={}  # nenhum master rebaixado (regra: 44 masters entram)

dec=[]
for pm,a,y,t in cr['fila']:
    e=ef[pm]
    if pm in MASTERS:
        nota='MASTER GPM (âncora índice bidirecional)'
        if pm=='39197553': nota='ENTRA RESGATE — Lu 2024 MR bidirecional (J Affect Disord): âncora da regra 3 (MR nulo mtDNA-CN↔transtornos); o briefing §8 dizia "não resolvido" e o anexo o trazia (DOI 10.1016/j.jad.2024.08.162)'
        if pm=='35732695': nota='MASTER GPM — Triebelhorn (print **2024**, Mol Psychiatry): bioenergética+eletrofisiologia de iNPC/iPS-neurônios de MDD; resolve também a pendência "Triebelhorn 2024" do §8 (o briefing o chamava 2021 e procurava um 2024 inexistente — é o MESMO artigo, print 2024)'
        dec.append({'pmid':pm,'decisao':'ENTRA','motivo':nota})
    elif pm in EXTRA: dec.append({'pmid':pm,'decisao':'ENTRA','motivo':EXTRA[pm]})
    elif pm in EXC: dec.append({'pmid':pm,'decisao':'EXC','motivo':EXC[pm]})
    else:
        dec.append({'pmid':pm,'decisao':'BAIXO','motivo':'BAIXO — camada B/C mecânica redundante com os 44 masters (dinâmica/mitofagia/redox básicos), contexto não-psiquiátrico (envelhecimento, neurodegeneração mecânica, exposição), ou desenho preliminar/preprint; registrado sem descarte por contrariar tese'})

from collections import Counter
c=Counter(d['decisao'] for d in dec)
print('DECISÃO:',dict(c))
assert len(dec)==151
# infere autor/ano print
for d in dec:
    e=ef[d['pmid']]
    d['autor']=e['autores'][0]; d['ano']=e['ano_print']; d['fonte']=e['iso']; d['titulo']=e['titulo']; d['pubtype']=e['pubtypes'][:4]
json.dump({'totais':dict(c),'itens':dec}, open(f'{BASE}/producao/insumos/matriz_b9_decisao.json','w'), ensure_ascii=False, indent=1)
print('gravado matriz_b9_decisao.json')
print('ENTRA masters:',len([d for d in dec if d['decisao']=='ENTRA' and d['pmid'] in MASTERS]),'| extras:',len([d for d in dec if d['decisao']=='ENTRA' and d['pmid'] not in MASTERS]))
