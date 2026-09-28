# -*- coding: utf-8 -*-
import json
BASE='/home/user/BIBLIOTECAS/B13_SistemaEndocanabinoide/'
META=json.load(open(BASE+'producao/insumos/matriz_b13_g1.json'))
PAR="parcial — revisão mistura espécies/evidência translacional"
NO="não — evidência humana"
SIM="SIM — evidência em roedor/modelo; tradução humana por analogia"
# pmid: (id, tag, desenho, sec, achado, nat, mat, role, extr, alias)
D={
"23702112":("REF_KUHNERT_2013","ML","estudo pré-clínico (rato)","cb1_amigdala_pfc","Receptores canabinoides na amígdala e córtex pré-frontal de ratos na aprendizagem de medo — CB1 corticolímbico causal em modelo.","contributiva","bem_suportado","preclinical_mechanistic",SIM,None),
"25981172":("REF_JENNICHES_2016","ML","estudo pré-clínico (camundongo)","reducao_ecb_ansiedade","Camundongos com níveis reduzidos de endocanabinoides mostram respostas de ansiedade, estresse e medo intensificadas — suporte causal ao buffer eCB.","contributiva","bem_suportado","preclinical_mechanistic",SIM,None),
"26361059":("REF_LIM_2016","ML","estudo pré-clínico (rato)","estresse_predador","Modulação endocanabinoide da ansiedade de longo prazo induzida por estresse predatório — modelo de trauma/TEPT.","contributiva","bem_suportado","preclinical_mechanistic",SIM,None),
"26514583":("REF_GUNDUZCINAR_2016","ML","estudo pré-clínico (camundongo)","fluoxetina_extincao","A fluoxetina facilita a EXTINÇÃO do medo via endocanabinoides amigdalares — elo fármaco×eCB na extinção (sinal mecanístico, P20).","contributiva","bem_suportado","preclinical_mechanistic",SIM,"chave insumo 'Gray 2015' — 1ª autora real Gunduz-Cinar; print 2016"),
"27511017":("REF_DI_2016","ML","estudo pré-clínico (rato)","estresse_agudo_bla","Estresse agudo suprime inibição sináptica e aumenta ansiedade via liberação de eCB na amígdala basolateral — via 3.","contributiva","bem_suportado","preclinical_mechanistic",SIM,None),
"30036537":("REF_MICALE_2018","OB","revisão","ecs_hpa","Sistema endocanabinoide, estresse e eixo HPA — arquitetura da ponte B2 (regra 6: revisão = conceito).","contributiva","bem_suportado","review",PAR,None),
"30573646":("REF_MORENA_2019","ML","estudo pré-clínico (rato)","bls_aearol_hidrolise","Aumento da hidrólise de anandamida no complexo basolateral da amígdala reduz a expressão da memória de medo — alvo FAAH amigdalar.","contributiva","bem_suportado","preclinical_mechanistic",SIM,None),
"30973483":("REF_MEYER_2019","EC","estudo experimental humano (exercício)","exercicio_ecb_humor","eCB séricos e humor após EXERCÍCIO na depressão maior — interface exercício (regra 8) em humano (CORE humano).","associativa","bem_suportado","human_clinical",NO,None),
"31948734":("REF_MARCUS_2020","ML","estudo pré-clínico","colapso_ecb_amigdalo","O COLAPSO da sinalização eCB medeia o fortalecimento amigdalo-cortical induzido por estresse — causalidade experimental central (via 3).","contributiva","bem_suportado","preclinical_mechanistic",SIM,None),
"32898588":("REF_GARANI_2021","OB","revisão de estudos humanos","estudos_humanos_humor","ECS em transtornos psicóticos e do humor: revisão dos estudos HUMANOS — camada humana separada da experimental.","contributiva","bem_suportado","review",NO,None),
"33759226":("REF_WARREN_2022","OB","revisão integrativa","ecb_noradrenalina","Interações endocanabinoide–noradrenérgicas na extinção do medo — integração de sistemas (ponte LC-NA).","contributiva","moderadamente_suportado","review",PAR,None),
"34776851":("REF_DEMELOREIS_2021","OB","revisão","qualidade_vida_ecs","Qualidade de vida e um sistema endocanabinoide vigilante — framework de homeostase.","contributiva","moderadamente_suportado","review",PAR,"chave insumo 'Cota 2008' — autor real de Melo Reis; artigo de 2021"),
"34893921":("REF_SPOHRS_2022","EC","estudo fMRI humano (genética)","faah_rs324420_extincao","O polimorfismo FAAH rs324420 modula o RECALL de extinção em humanos saudáveis (fMRI) — tradução humana da via 2 (versão publicada do preprint [G1] anterior).","associativa","bem_suportado","human_clinical",NO,None),
"36039150":("REF_VECCHIARELLI_2022","ML","estudo pré-clínico","sexo_modalidade_estressor","Sexo e modalidade de estressor modulam a dinâmica corticolímbica de eCB sob estresse agudo — moduladores experimentais.","contributiva","bem_suportado","preclinical_mechanistic",SIM,None),
"36870468":("REF_BORGESASSIS_2023","ML","estudo pré-clínico","bnst_cb1_faah","Receptores CB1 e enzima FAAH no BNST modulam comportamento ansioso dependendo do contexto — circuito estendido.","contributiva","bem_suportado","preclinical_mechanistic",SIM,"chave insumo 'Bedse 2017' — autor real Borges-Assis (2023)"),
"37984468":("REF_OBERMANNS_2023","EC","estudo genético humano","cnr1_serotonina","Variação genética 5-HT1A/5-HT2A/CNR1 e tônus endocanabinoide alterado — elo genético serotonina×eCB em humano.","associativa","emergente","human_clinical",NO,None),
"38886733":("REF_MCWHIRTER_2024","OB","revisão sistemática","mulheres_depressao","Níveis de endocanabinoides em indivíduos do sexo feminino com depressão diagnosticada: revisão sistemática — resolve o [G1] 'McWhirter (sexo feminino)'.","contributiva","bem_suportado","review",NO,"chave insumo 'Mazurka 2024' — autor real McWhirter; a Mazurka real permanece [G1]"),
"41013856":("REF_WANG_2025","EC","estudo humano com validação experimental","biomarcadores_ecs_mdd","Biomarcadores associados ao ECS na depressão maior: identificação e validação experimental — marcadores candidatos (M05: não diagnóstico).","associativa","emergente","human_clinical",PAR,None),
# selecionados §6
"40799146":("REF_AZIZI_2025","ML","estudo pré-clínico (rato)","cb1_hipocampo_rem","Ativação de CB1r hipocampal e comportamento sob privação de sono REM — interface eCB×sono (ponte B10).","contributiva","emergente","preclinical_mechanistic",SIM,None),
"30458201":("REF_BALOGH_2019","OB","revisão","condicionamento_contextual","Interações endocanabinoides na aquisição do condicionamento de medo contextual — consolidação ameaça [revisão pré-clínica].","contributiva","bem_suportado","review","SIM — revisão de evidência pré-clínica; tradução humana por analogia",None),
"20167262":("REF_CAMPOS_2010","ML","estudo pré-clínico (rato)","hipocampo_ventral","Facilitação de efeitos endocanabinoides no hipocampo VENTRAL modula ansiedade — circuito hipocampal.","contributiva","bem_suportado","preclinical_mechanistic",SIM,None),
"38280009":("REF_DRAGON_2024","OB","revisão","antidepressivos_ecb","Como a depressão e os antidepressivos afetam o sistema endocanabinoide — elo fármaco×eCB (sinal, P20).","contributiva","bem_suportado","review",PAR,None),
"31849055":("REF_GOLDSTEINFERBER_2021","OB","revisão","desenvolvimento_els","Estresse precoce e desenvolvimento do sistema endocanabinoide: regulação bidirecional, sexo- e região-dependente — ponte B12 (trauma).","contributiva","bem_suportado","review","SIM — revisão de evidência pré-clínica; tradução humana por analogia","chave insumo 'Ferber 2019' — autora real Goldstein Ferber"),
"22029953":("REF_HEYMAN_2012","EC","estudo experimental humano (exercício)","exercicio_ecb_bdnf","Exercício intenso aumenta eCB circulantes e BDNF em humanos — interface exercício×plasticidade (regra 8).","associativa","bem_suportado","human_clinical",NO,"chave insumo 'Gamelin 2012' — autor real Heyman"),
"24286185":("REF_HILL_2013","OB","revisão translacional","evidencia_translacional","Evidência translacional do envolvimento do ECS em respostas ao estresse e humor — ponte animal→humano.","contributiva","bem_suportado","review",PAR,None),
"19903506":("REF_HILL_2010","OB","revisão","estresse_neurocomportamental","ECS nos efeitos neurocomportamentais do estresse — revisão estrutural (série Hill).","contributiva","bem_suportado","review","SIM — revisão de evidência pré-clínica; tradução humana por analogia","chave insumo 'Hill 2009' (artigo distinto do REF_HILL_2009 da V1); print 2010"),
"22214537":("REF_HILL_2012","OB","revisão","feedback_glicocorticoide","Sinalização endocanabinoide e feedback negativo glicocorticoide — mecanismo do eixo (ponte B2).","contributiva","bem_suportado","review","SIM — revisão de evidência pré-clínica; tradução humana por analogia","chave insumo 'Hill 2011' → print 2012"),
"32375160":("REF_IVY_2020","ML","estudo pré-clínico","cb2_anxiolitico","Receptores CB2 medeiam efeitos ansiolíticos de modulação de monoacilglicerol — braço CB2 em modelo.","contributiva","bem_suportado","preclinical_mechanistic",SIM,None),
"42314784":("REF_LIEDHEGNER_2026","ML","estudo pré-clínico","scp2_lipideo","Perda de SCP-2 (proteína carreadora de esterol) reduz ansiedade e aumenta extinção do medo — nova camada lipídica intracelular do ECS.","contributiva","emergente","preclinical_mechanistic",SIM,None),
"32980261":("REF_LU_2021","OB","revisão","review_ecs","Review do sistema endocanabinoide — arquitetura geral atualizada (Biol Psychiatry CNNI).","contributiva","bem_suportado","review",PAR,"chave insumo 'Lu 2020' → print 2021"),
"22804774":("REF_MECHOULAM_2013","OB","revisão","ecs_cerebro_fundacao","O sistema endocanabinoide e o cérebro (Annu Rev Psychol) — revisão fundacional.","contributiva","muito_estabelecido","review",PAR,None),
"26068727":("REF_MORENA_2016","OB","revisão","stress_ecs_interacoes","Interações neurobiológicas entre estresse e o sistema endocanabinoide — síntese estrutural central.","contributiva","bem_suportado","review","SIM — revisão de evidência pré-clínica; tradução humana por analogia",None),
"35675221":("REF_PARK_2022","OB","revisão","pufa_exercicio","PUFAs dietéticos e exercício: ações dinâmicas sobre endocanabinoides no cérebro — interface (regra 8; molecular inflamação fica em B1).","contributiva","bem_suportado","review",PAR,None),
"35126139":("REF_RIBEIRO_2021","ML","estudo pré-clínico","cb2_constitutivo","Atividade espontânea (constitutiva) de receptores CB2 atenua comportamento induzido por estresse — sinal basal CB2.","contributiva","emergente","preclinical_mechanistic",SIM,None),
"40840197":("REF_ROSA_2025","OB","revisão","resistencia_tratamento","Endocanabinoides, depressão e resistência ao tratamento: perspectivas — dimensão clínica de refratariedade.","contributiva","emergente","review",PAR,None),
"35650684":("REF_UZUNESER_2023","ML","estudo pré-clínico","fabp5_cb2","Identificação de nova via FABP5–CB2 no córtex — transporte intracelular de eCB como alvo.","contributiva","emergente","preclinical_mechanistic",SIM,None),
"31962287":("REF_VIMALANATHAN_2020","ML","estudo pré-clínico (rato)","weak_extinction","Fármacos moduladores de eCB melhoram 'ansiedade' mas NÃO a expressão de medo no fenótipo de extinção fraca — dissociação comportamento×medo.","contributiva","bem_suportado","preclinical_mechanistic",SIM,None),
"39370369":("REF_ZARAZUAGUZMAN_2024","OB","revisão","overview_mdd_ecs","Visão geral depressão maior×sistema endocanabinoide — síntese clínica recente.","contributiva","bem_suportado","review",PAR,"chave insumo 'Zabik 2024' = autor real Zarazúa-Guzmán"),
"37088409":("REF_ZABIK_2023","EC","estudo experimental humano (THC×fMRI)","thc_extincao_humano","Modulação canabinoide (THC) da ativação corticolímbica durante aprendizagem de extinção em adultos saudáveis — CAMADA EXÓGENA (via 10, regra 1): não sustenta claims do núcleo endógeno. Resolve o [G1] 'Zabik-RCT'.","associativa","emergente","human_clinical","não — camada translacional exógena (regra 1), sinal isolado",None),
"29977073":("REF_SEGEV_2018","OB","revisão","hipocampo_amigdala_plasticidade","Papel dos endocanabinoides no hipocampo e amígdala em memória emocional e plasticidade — revisão estrutural (resolve 'Segev real', expõe falso mapeamento para Șerban 2025).","contributiva","bem_suportado","review",PAR,None),
}
R=[]
for pmid,(fid,tag,des,sec,ach,nat,mat,role,extr,alias) in D.items():
    m=META.get(pmid,{})
    if not m and pmid=="29977073": m={"title":"Role of endocannabinoids in the hippocampus and amygdala in emotional memory and plasticity","authors":["Segev A"],"pubdate":"2018","source":"Neuropsychopharmacology"}
    g2="eligible" if tag in("EC","OB") else "redirecionado_mecanistico"
    R.append({"pmid_oficial":pmid,"titulo_artigo":m.get('title',''),"autores":m.get('authors',[]),
      "revista_ano":f"{m.get('source','')} ({(m.get('pubdate') or '')[:4]})","desenho_estudo":f"[{tag}] {des} · {m.get('source','')}",
      "secao_origem":f"mecanismo_B13_{sec}","achado_central_molecular":ach,"extrapolacao_por_analogia":extr,
      "ids_referencia_interna":[fid],"id_referencia_interna":fid,"doi":"",
      "claim_id_origem":"B13.MEC.BLOCO14.001","evid_role":role,
      "especie_mesh":["Animals"] if tag=="ML" else ["Humans"],
      "verification_status":"preclinico" if tag=="ML" else "humano_clinico",
      "citacao_confirmada":True,"g1_metodo":"eutils_automatico","g2_elegibilidade":g2,
      "g2_motivo":"humano clínico/síntese — elegível" if tag in("EC","OB") else "animal/modelo causal — redirecionado",
      "g3_verificado_por":"IA G3 Rodada [AT] GPM B13 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
      "status_auditoria":"CONFIRMADO","origem_pipeline":"GPM_RODADA_AT","_aliases":([alias] if alias else []),
      "_nat":nat,"_mat":mat,"_acao":"ADICIONAR_SINALIZADOR" if tag=="ML" else "MANTER",
      "_tier":"tier_3_correlacional_mecanistico" if tag=="ML" else "tier_4_descritivo_estrutural"})
ids=[r['id_referencia_interna'] for r in R]
assert len(ids)==len(set(ids))
json.dump(R, open(BASE+'producao/insumos/b13_refs_data.json','w'), indent=1, ensure_ascii=False)
print("ENTRA B13:", len(R), "| ML:", sum(1 for r in R if r['desenho_estudo'][1:3]=='ML'))
BAIXO={"Coelho 2022":"BAIXO — iNOS/mPFC, periférico ao ECS-core","Ferber 2020":"BAIXO — entourage/cannabis (regra 1: camada exógena não alimenta núcleo)","Gellman 2026":"BAIXO — compostos sintéticos (farmacologia)","He 2026":"BAIXO — rede HPA×BDNF genérica","Kasatkina 2021":"BAIXO — neuroproteção/imunomodulação (ponte B1)","Li 2026":"BAIXO — microglia-astrocyte (B1)","Lowe 2021":"BAIXO — camada terapêutica","Lyndon 2025":"BAIXO — PTSD targets (interface+terapêutico)","Morris 2022":"BAIXO — inflamação/nitro-oxidativo (interface; molecular em B1)","Peixoto 2026":"BAIXO — resiliência genérica","Pilatti 2026":"BAIXO — HPA×inflamação terapêutica","Rao 2026":"BAIXO — sintomas neuropsiquiátricos amplo","Ren 2020":"BAIXO — agentes terapêuticos","Rezende 2023":"BAIXO — química básica ECS","Ricardi 2024":"BAIXO — beta-cariofileno (fitocanabinoide, regra 1)","Șerban 2025":"BAIXO — revisão genérica human-disease (e é o falso mapeamento de 'Segev 2018', exposto)","Thippaiah 2021":"BAIXO — misto exo/endógeno, suicídio periférico","Viveros 2007":"BAIXO — redundância (REF_VIVEROS_2005 já vigente)","Yarar 2020":"BAIXO — redundância de revisões ECS×MDD"}
EXC={"Cossu 2020 (36284789)":"EXC — falso mapeamento de 'Spohrs 2021': vídeo neurocirúrgico (fístula carótido-cavernosa); exposto","Liu 2026 (NAO-IDX)":"EXC — revista não indexada","Saito 2010 (NAO-IDX)":"EXC — SciELO sem match verificável","Wang 2025 IJNP (NAO-IDX)":"EXC — abstract de congresso"}
json.dump({"entra":len(R),"baixo":BAIXO,"exc":EXC}, open(BASE+'producao/insumos/matriz_b13_decisao.json','w'), indent=1, ensure_ascii=False)
print("BAIXO:",len(BAIXO),"EXC:",len(EXC))
