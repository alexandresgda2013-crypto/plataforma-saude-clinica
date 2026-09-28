# -*- coding: utf-8 -*-
import json
D='BIBLIOTECAS/B05_GabaGlutamato/producao/insumos/'
R=json.load(open(D+'matriz_b5_g1.json'))
rows={v['pmid']:v for v in R['ok'].values()}
rows.update(R.get('consolidacao_extra',{}))
UNI=set(rows); assert len(UNI)==190
VIG={'20724638','27144355','28697889','30914923','37543478','39368965'}
EXC={'34265291':'Alzheimer','39450669':'Alzheimer','33218044':'Alzheimer','38791587':'Alzheimer/PV-neurológico','34610314':'Alzheimer/β-amiloide','26922658':'autismo','32297709':'autismo','35587691':'autismo','36681677':'autismo (e ano corrigido 2021→2023)','37521710':'apneia do sono','35167940':'epilepsia','35250498':'epilepsia (borda: psiq-comorbidades)','40890771':'epilepsia','39524246':'Carta — redundância do original Xu 2020 (prioridade ao artigo)'}
FP={'42701922':('DOI do anexo ("Prosowski 2024 — Ketamine/Esketamine TRD") resolve para artigo NÃO correlato (Zhang L 2026, γ-butyrolactones — fisiologia não-psiquiátrica). '
 'Artigo pretendido NÃO localizado no PubMed (Prosowski[author] = 0) → [G1]')}
FALHAS={'10.1002/alz70855_102267':'Imiruaye 2025 — abstract de congresso (Alzheimer Association); não indexado como artigo; também fora de escopo (Alzheimer)','Prosowski 2024':'rótulo do anexo sem correspondente no PubMed → [G1]'}
BAIXO={'39769420':'narrativa derivada (além do conjunto CORE KET)','31215725':'história/revisão derivada','25954495':'revisão derivada era-2015','33569971':'perspective derivada','33155503':'perspective derivada','35312993':'revisão genérica','32440333':'revisão genérica','35267893':'panorama neuropsiquiátrico amplo (não-alvo)','29736744':'eficácia/tolerabilidade clínica — guia, não mecanismo','41858652':'bipolar-específico','30034974':'revisão genérica','35872836':'revisão genérica','31699965':'revisão genérica','27523302':'eletrofisiologia básica nicho','34678377':'eletrofisiologia básica nicho','29593052':'LTP/LTD básico sem elo','26830140':'MIA neurodesenvolvimental sem fenótipo-alvo direto (borda)','38391931':'álcool×TDM misto, incremento baixo','37900589':'fisiologia nicho (VIP/SST somatossensorial)','39901494':'fisiologia nicho (BK/GABAb VIP)','39141819':'fisiologia nicho (subículo)','35088731':'AMPAR para praticante de estimulação (educacional)','40161576':'crosstalk pleiotrópico amplo','33766086':'GluN2C/2D nicho','41637458':'ubiquitinação GluN2A nicho','34637787':'GluN2D eletrofisiologia nicho','35105656':'cinética PV/SST nicho','26041915':'tráfego AMPAR nicho','40436282':'Grin2a global nicho','37545878':'δ/α6 cerebellar nicho','37258641':'SST-GABAb neocórtex nicho','40445322':'SST camada-4 aprendizado nicho','33303963':'SST entorrinal nicho','38813758':'domínios GluN2 nicho','35484243':'GluN2A-enhancer nicho','40239379':'PAMs GluN2A (química medicinal)','32832654':'GABA pré-frontal LTP nicho','40013665':'δ-GABA(A) PV nicho','31873798':'SSTR1-5 córtex-barril nicho','29311610':'SST-signaling nicho','28965758':'PV/SST codificação espacial nicho','38616956':'PV fisiologia nicho','33972691':'cadherina-13 stem-cell nicho','36309210':'E/I desenvolvimento sem doença','26586374':'BLA GABA saúde/doença amplo','39841263':'AMPAR plasticidade/doenças review amplo','35601529':'PV plasticidade sensorial nicho','35775994':'SST-astrócito nicho','40029461':'PTM NMDAR nicho','38516040':'crosstalk neuromodulador amplo','37448697':'inibição tônica bidirecional nicho','33007389':'sevoflurano pré-natal nicho','42038294':'editorial (veículo de opinião)'}
GRP={'27449797':'MRS','30144668':'MRS','34354048':'MRS','32619710':'MRS','34023450':'MRS','35526748':'MRS','37495889':'MRS','42250487':'MRS','40199850':'MRS','28180078':'MRS','39483976':'MRS','33986699':'MRS','39150032':'MRS','22676966':'MRS',
'42362547':'STR','40581655':'STR','39362860':'STR','34557569':'STR','31377218':'STR','32158215':'STR',
'37294327':'ANX','27821870':'ANX','38796850':'ANX','32555286':'ANX','39086371':'ANX','37035504':'ANX','32297184':'ANX','25653526':'ANX','38865810':'ANX','32277042':'ANX',
'34407417':'PLAST','38177353':'PLAST','29158584':'PLAST','34565579':'PLAST','33723767':'PLAST','39684808':'PLAST','36907686':'PLAST','23534055':'PLAST','37419688':'PLAST','30359599':'PLAST','32292336':'PLAST','26938443':'PLAST','22510460':'PLAST','25619552':'PLAST',
'25340958':'NMDA','33059355':'NMDA','18992785':'NMDA','31207274':'NMDA','28439098':'NMDA','30296532':'NMDA','33087756':'NMDA','33843051':'NMDA','27262028':'NMDA','36596696':'NMDA','39562042':'NMDA','20357110':'NMDA','24298164':'NMDA','15356193':'NMDA','39185814':'NMDA','32640261':'NMDA','34364898':'NMDA','29706992':'NMDA','39770460':'NMDA',
'28234212':'AMPA','37358072':'AMPA','41781722':'AMPA','37124348':'AMPA','32754026':'AMPA',
'33438026':'GABA','33070149':'GABA','27812532':'GABA','31707118':'GABA','36725341':'GABA','24071826':'GABA','21154909':'GABA','30523065':'GABA','24550784':'GABA','32073397':'GABA','23637187':'GABA','32859716':'GABA','31974304':'GABA','31212931':'GABA','33837051':'GABA','37101797':'GABA','36184627':'GABA','37709943':'GABA','25653499':'GABA','34322002':'GABA',
'30946828':'KET','29899972':'KET','27062302':'KET','41475562':'KET','41577431':'KET','41607072':'KET','35182519':'KET','41923438':'KET','42515873':'KET','41139588':'KET','40840695':'KET','29532791':'KET','29516301':'KET','31830487':'KET','35546951':'KET','34968492':'KET','37488280':'KET','33963284':'KET','26955968':'KET','32017978':'KET','39116687':'KET',
'27240530':'IFACE','38586282':'IFACE','35513229':'IFACE','25237099':'IFACE','33554649':'IFACE','42278495':'IFACE','30851296':'IFACE'}
for k in list(BAIXO)+list(VIG):
    assert k in UNI, ('fora do universo:',k)
ENTRA=sorted(UNI-VIG-set(EXC)-set(FP)-set(BAIXO))
sem=[p for p in ENTRA if p not in GRP]
assert not sem, ('sem grupo:',[(p,rows[p]['real_titulo']) for p in sem])
assert len(ENTRA)+len(BAIXO)+len(EXC)+len(FP)+len(VIG & UNI)==190
cnt={}
OUT={'VIG':sorted(VIG & UNI),'EXC':EXC,'FP':FP,'FALHAS':FALHAS,'BAIXO_MOTIVOS':BAIXO,'ENTRA':[]}
for p in ENTRA:
    r=rows[p]; g=GRP[p]; cnt[g]=cnt.get(g,0)+1
    OUT['ENTRA'].append({'pmid':p,'grupo':g,'a1':r.get('real_a1'),'ano':r.get('real_ano'),'titulo':r.get('real_titulo'),'fonte':r.get('fonte'),'pubtype':r.get('pubtype',[])})
print('grupos:',cnt,'| total ENTRA',len(OUT['ENTRA']),'| BAIXO',len(BAIXO),'| EXC',len(EXC),'| FP 1 | VIG',len(VIG))
json.dump(OUT,open(D+'matriz_b5_decisao.json','w'),ensure_ascii=False,indent=1)
print('somatorio = 190 OK')
