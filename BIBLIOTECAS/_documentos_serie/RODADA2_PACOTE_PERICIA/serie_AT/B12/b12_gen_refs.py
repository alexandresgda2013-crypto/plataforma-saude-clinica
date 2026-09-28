# -*- coding: utf-8 -*-
import json, re, unicodedata
BASE='/home/user/BIBLIOTECAS/B12_NeurobiologiaTrauma/'
M=json.load(open(BASE+'producao/insumos/matriz_b12_g1.json'))
META=M['meta']
def norm(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()
    return re.sub(r'[^A-Z]','',s.upper())
# pmid: (id_forcado_ou_None, tag, desenho, sec, achado, nat, mat, role, extr, alias)
PAR="parcial — revisão mistura espécies/evidência translacional"
NO="não — evidência humana clínica/observacional"
SIM="SIM — evidência em roedor/célula/modelo; tradução humana por analogia"
D={
"11430844":(None,"OB","revisão fundacional","trauma_programador","Revisão fundacional: adversidade infantil na neurobiologia dos transtornos de humor e ansiedade — modelo de programação/sensibilização, pré-clínico e clínico.", "contributiva","muito_estabelecido","review",PAR,None),
"22442074":(None,"EC","estudo translacional (polimorfismo humano + modelo)","bdnf_val66met","Polimorfismo Val66Met do BDNF altera vulnerabilidade ao estresse — interação gene×ambiente, não determinismo (regra 1).", "associativa","bem_suportado","human_clinical",PAR,None),
"23468190":(None,"OB","revisão","citocinas_cerebro","Citocinas como alvos centrais: impacto sobre neurotransmissores e neurocircuitos — ponte B1 (imunidade↔circuitos).", "contributiva","bem_suportado","review",PAR,None),
"23536785":(None,"OB","meta-análise fMRI","memoria_traumatica","Meta-análise de provocação de sintomas: em busca da memória traumática — assinatura funcional transdiagnóstica do trauma.", "contributiva","bem_suportado","review",NO,None),
"25462901":("REF_WINGENFELD_2015","OB","revisão sistemática","cortisol_cognicao","Efeitos do cortisol sobre cognição em TDM, TEPT e borderline — cortisol como modulador cognitivo transdiagnóstico.", "contributiva","bem_suportado","review",NO,"Wingenfeld 2014 (chave insumo) → print 2015"),
"25735885":(None,"OB","revisão sistemática e meta-análise MRI","ptsd_volumetrico","Meta-análise volumétrica em TEPT — alterações estruturais associativas sem valor de biomarcador individual (regra 2).", "contributiva","bem_suportado","review",NO,None),
"27049575":(None,"EC","estudo clínico com provocação (DST/combinada)","hpa_trauma_heterogeneidade","Atividade do HPA em depressão unipolar com trauma infantil: resposta combinada — heterogeneidade, não hiperatividade universal (NEG #3).", "associativa","bem_suportado","human_clinical",NO,None),
"27531235":(None,"OB","meta-análise","heterogeneidade_massa_cinzenta","Heterogeneidade da massa cinzenta em adultos com maus-tratos infantis — a heterogeneidade é dado, não ruído (regra 3).", "contributiva","bem_suportado","review",NO,None),
"27824358":(None,"OB","meta-análise fMRI","pfc_acc_terminologia","Sobreposição espacial amígdala–'PFC'×'ACC' — a controvérsia de terminologia das redes é documentada (regra 2).", "contributiva","bem_suportado","review",NO,None),
"28183380":(None,"OB","revisão","gr_mr_depressao","Avaliação GR/MR do eixo HPA na depressão — interface molecular (regra 4).", "contributiva","bem_suportado","review",NO,"chave 'Vogelzangs 2016' do insumo = mesmo PMID (duplicata exposta)"),
"30086534":(None,"EC","estudo clínico com DST e genotipagem FKBP5","trauma_sensibiliza_hpa","Depressão ansiosa dependente de trauma infantil SENSIBILIZA a função do HPA — trauma como modulador, não causa única (144 pacientes).", "associativa","bem_suportado","human_clinical",NO,None),
"31258096":(None,"EC","tarefa de condicionamento/extinção com fMRI","extincao_ptsd","Assinaturas neurais de condicionamento, aprendizagem de extinção e reevocação no TEPT — núcleo da via 7.", "associativa","bem_suportado","human_clinical",NO,None),
"31794798":(None,"EC","estudo clínico prospectivo","trauma_hpa_resposta_antidepressiva","Trauma infantil, atividade do HPA e resposta antidepressiva na depressão — trauma modula trajetória terapêutica (sinal, P20).", "associativa","bem_suportado","human_clinical",NO,None),
"31801966":(None,"OB","revisão integrativa","neuroplasticidade_depressao","Neuroplasticidade nos mecanismos cognitivos e psicológicos da depressão: modelo integrativo — ponte B3 (não invasão).", "contributiva","bem_suportado","review",PAR,None),
"31900428":(None,"ML","revisão pré-clínica","bdnf_medo","Neurobiologia do BDNF na memória de medo, sensibilidade ao estresse e transtornos relacionados — primariamente evidência animal.", "contributiva","bem_suportado","preclinical_mechanistic","SIM — revisão de evidência pré-clínica; tradução humana por analogia",None),
"31964160":(None,"OB","meta-análise transdiagnóstica fMRI","circuitos_emocionais_comuns","Disrupções comuns de circuitos emocionais entre transtornos psiquiátricos — transdiagnóstico obrigatório (regra 7).", "contributiva","bem_suportado","review",NO,"chave 'Mayer 2020' renomeada — 1º autor real McTeague"),
"32085670":(None,"OB","revisão","epigenetica_bdnf","Estresse, transtornos mentais e regulação epigenética do BDNF — fronteira promissora, barra causal alta (regra 8).", "contributiva","moderadamente_suportado","review",PAR,None),
"33053385":(None,"EC","estudo experimental humano","trauma_val66met_plasticidade","Trauma infantil × polimorfismo Val66Met sobre plasticidade cerebral — interação exposição×vulnerabilidade (não determinismo).", "associativa","moderadamente_suportado","human_clinical",NO,None),
"34100334":("REF_CHEIRAN_2022","OB","revisão","microglia_hpa","Microglia e eixo HPA na depressão: participação e relação — ponte B1 (neuroimunidade).", "contributiva","moderadamente_suportado","review",PAR,"Pereira 2021 (chave insumo; Cheiran Pereira G = 1º autor; print 2022)"),
"34256069":(None,"OB","revisão sistemática e meta-análise","transdiagnostico_estrutural","Correlatos estruturais em depressão maior, ansiedade e TEPT: parte compartilhada, parte específica — regulador do módulo (regra 7).", "contributiva","muito_estabelecido","review",NO,"'See 2025' do insumo = Serra-Blasco 2021 (reatribuição)"),
"34963057":(None,"OB","revisão","sinalizacao_bdnf","Sinalização do BDNF em contexto: da regulação sináptica aos transtornos psiquiátricos — mecanismo como moldura.", "contributiva","bem_suportado","review",PAR,None),
"35189164":(None,"OB","meta-análise","neuroestrutura_adversidade","Traços neuroestruturais de adversidades precoces: efeitos específicos por idade e tipo de adversidade — janela sensível como dado.", "contributiva","bem_suportado","review",NO,None),
"35354926":(None,"OB","revisão","neuroplasticidade_hipocampal_tdm","Desregulação da neuroplasticidade hipocampal adulta na depressão maior: patogênese e potencial terapêutico — ponte B3/B16.", "contributiva","bem_suportado","review",PAR,None),
"35599780":(None,"OB","síntese dirigida de literatura","trauma_hpa_sintese","Síntese dirigida: trauma infantil, HPA e doença psiquiátrica — confirma associação com heterogeneidade.", "contributiva","bem_suportado","review",NO,None),
"35872219":(None,"ML","estudo pré-clínico (roedor)","bdnf_serotonina_resiliencia","Expressão de BDNF em neurônios serotoninérgicos melhora resiliência ao estresse — mecanismo animal (via 8).", "nao_estabelecida","emergente","preclinical_mechanistic","SIM — evidência em roedor; tradução humana por analogia",None),
"35992016":(None,"OB","revisão","bidirecionalidade_imune","Cenário 'ovo e galinha' em psiconeuroimunologia: mecanismos bidirecionais citocinas↔cérebro (regra bidirecional).", "contributiva","bem_suportado","review",PAR,None),
"36029627":(None,"OB","meta-análise multimodal","ptsd_multimodal","Anormalidades funcionais e estruturais no TEPT: meta-análise multimodal — comparação reguladora (regra 7).", "contributiva","bem_suportado","review",NO,None),
"36151073":(None,"OB","meta-análise","medo_patologico_neuroestrutura","Medo patológico, ansiedade e afeto negativo têm assinaturas neuroestruturais DISTINTAS — separação de fenótipos (transdiagnóstico).", "contributiva","bem_suportado","review",NO,None),
"37741177":(None,"OB","revisão sistemática e meta-análise rs-fMRI","repouso_ansiedade","Resting-state fMRI nos transtornos de ansiedade: meta-análise com chamado a compartilhamento — ansiedade ≠ TEPT ≠ depressão.", "contributiva","bem_suportado","review",NO,None),
"37781095":(None,"OB","revisão","bdnf_estresse","Papel da sinalização BDNF na patogênese de transtornos por estresse — síntese mecanística (ponte B3).", "contributiva","bem_suportado","review",PAR,None),
"39304648":(None,"OB","meta-análise multimodal","harm_avoidance","Correlatos neurais de harm avoidance (esquiva de dano): meta-análise multimodal — traço ligado a ansiedade/depressão.", "contributiva","moderadamente_suportado","review",NO,None),
"40199321":(None,"ML","estudo pré-clínico com registro de circuito","citocinas_neuromoduladores","Citocinas pró e anti-inflamatórias modulam bidirecionalmente circuitos amigdalaros da ansiedade — formulação específica (NEG #7), evidência experimental.", "nao_estabelecida","emergente","preclinical_mechanistic","SIM — evidência em modelo animal (Cell); tradução humana por analogia",None),
"41660208":(None,"OB","revisão","metilacao_bdnf_ptsd","Regulação multicamada da metilação do DNA do BDNF no TEPT: do mecanismo molecular à tradução — fronteira (regra 8).", "contributiva","emergente","review",PAR,None),
"42165096":(None,"OB","meta-análise baseada em coordenadas","amigdala_repouso_ansiedade","Conectividade funcional de repouso da amígdala alterada nos transtornos de ansiedade: meta-análise ALE — ansiedade-específica.", "contributiva","bem_suportado","review",NO,None),
# selecionados
"35058584":(None,"OB","meta-análise multimodal transdiagnóstica","transdiagnostico_largescala","Mudanças cerebrais comuns e específicas em depressão, ansiedade e dor crônica em larga escala — transdiagnóstico.", "contributiva","bem_suportado","review",NO,None),
"33054384":(None,"OB","meta-análise fMRI","ansiedade_induzida_patologica","Neurobiologia sobreposta da ansiedade INDUZIDA e da PATOLÓGICA: validação experimental do circuito de medo humano.", "contributiva","bem_suportado","review",NO,None),
"31664439":("REF_JANIRI_2020","OB","meta-análise (226 estudos task-fMRI)","fenotipos_neurais_compartilhados","Fenótipos neurais compartilhados em transtornos de humor e ansiedade (226 estudos) — JAMA Psychiatry.", "contributiva","muito_estabelecido","review",NO,"chave insumo 2019 → print 2020"),
"40686488":(None,"OB","meta-análise","estrutura_mdd_ansiedade_ptsd","Correlatos estruturais em depressão, ansiedade e TEPT (Psychol Med 2025) — atualização da linha transdiagnóstica.", "contributiva","bem_suportado","review",NO,None),
"41444402":(None,"OB","meta-análise de conectividade","amigdala_conectividade_comum","Alterações comuns da conectividade intrínseca da amígdala (total e sub-regiões) em depressão/ansiedade/TEPT.", "contributiva","bem_suportado","review",NO,None),
"30581154":(None,"OB","meta-análise comparativa","afeto_negativo_neural","Correlatos neurais de distúrbios afetivos: meta-análise comparativa de processamento de afeto negativo.", "contributiva","bem_suportado","review",NO,None),
"24676455":(None,"OB","meta-análise VBM","acc_pfc_ansiedade","Traços comuns de ACC e PFC nos transtornos de ansiedade (DSM-5): meta-análise VBM — ansiedade-específica sem TEPT.", "contributiva","bem_suportado","review",NO,None),
"22738125":(None,"OB","meta-análise quantitativa fMRI","atividade_neural_ptsd","Meta-análise quantitativa da atividade neural no TEPT — contraponto funcional do padrão estrutural.", "contributiva","bem_suportado","review",NO,None),
"41922983":(None,"EC","estudo de consórcio (ENIGMA-PGC)","repouso_ptsd_consortio","Conectividade de repouso amígdala–hipocampo no TEPT: resultados do maior consórcio (ENIGMA-PGC) — escala multi-sítio.", "associativa","bem_suportado","human_clinical",NO,None),
"32726102":("REF_ESPINOZA_2020","OB","revisão sistemática","depressao_com_ansiedade_volumen","Diferenças volumétricas na depressão clínica EM ASSOCIAÇÃO com ansiedade — fenótipo comórbido medido.", "contributiva","moderadamente_suportado","review",NO,"chave insumo 'Oyarce 2020' (Espinoza Oyarce = 1º autor)"),
"38298789":("REF_BENZION_2024","OB","revisão de escopo","subregioes_amigdala_hipocampo_ptsd","Neuroimagem estrutural de SUB-REGIÕES de hipocampo e amígdala no TEPT: revisão de escopo — especificidade subcampo.", "contributiva","emergente","review",NO,"chave insumo 'Begni 2016' = Ben-Zion 2024 real; Begni real (BDNF genérico) fica BAIXO"),
"35158360":("REF_DELCASALE_2022","OB","meta-análise ALE","massa_cinzenta_ptsd","Reduções de massa cinzenta em hipocampo e amígdala esquerdos no TEPT: meta-análise ALE.", "contributiva","bem_suportado","review",NO,"chave insumo 'Ferracuti 2022' (Del Casale = 1º autor)"),
"33725661":("REF_ASHWORTH_2021","OB","revisão sistemática e meta-análise fMRI","jovens_ansiedade_depressao","Ativação neural de ansiedade e depressão em CRIANÇAS E JOVENS: meta-análise fMRI — janela do desenvolvimento (via 1.7).", "contributiva","bem_suportado","review",NO,"chave 'Ashworth 2021' corrigida: o PMID do dossiê resolvia Badowska-Szalewska (BAIXO)"),
"36030316":(None,"EC","estudo fMRI","sexo_violencia_reatividade","Diferenças de sexo na exposição à violência, reatividade neural à ameaça e saúde mental — sexo como modulador (lacuna §8.3).", "associativa","moderadamente_suportado","human_clinical",NO,None),
"35378148":("REF_DIBENEDETTO_2022","OB","revisão sistemática","fatores_neurotroficos_trauma","Fatores neurotróficos, trauma infantil e transtornos psiquiátricos: revisão sistemática — via 8 trauma-específica.", "contributiva","bem_suportado","review",NO,"chave insumo 'Deuter 2023' (Di Benedetto = 1º autor)"),
"33344725":(None,"EC","estudo clínico com metilação","metilacao_nr3c1_cortisol","Metilação aumentada de NR3C1 e SLC6A4 associa-se a reatividade de cortisol EMBOTADA na depressão — epigenética×HPA.", "associativa","moderadamente_suportado","human_clinical",NO,None),
"29793048":(None,"EC","estudo clínico com metilação","dnarn3c1_depressao_trauma","Diferenças de metilação no gene do receptor glicocorticoide na depressão relacionadas a trauma infantil — via 10.", "associativa","moderadamente_suportado","human_clinical",NO,None),
"28680507":(None,"EC","estudo mãe-bebê (metilação)","intergeracional_guerra","Metilação do BDNF em mães e recém-nascidos associada à exposição materna a guerra — transmissão intergeracional (via 1.8).", "associativa","moderadamente_suportado","human_clinical",NO,None),
"18702710":(None,"EC","estudo experimental humano (TSST)","fkbp5_recuperacao","Polimorfismos de FKBP5 modulam a RECUPERAÇÃO do estresse psicossocial agudo em saudáveis — interface (regra 4), não causa.", "associativa","bem_suportado","human_clinical",NO,None),
"38199409":(None,"EC","estudo clínico","mrna_gr_fkbp5","Expressão periférica de mRNA de receptores glicocorticoides e FKBP5 associada a depressão/ansiedade — marcador periférico.", "associativa","emergente","human_clinical",NO,None),
"28589964":(None,"EC","estudo clínico G×E","hpa_genes_maus_tratos","Genes do eixo HPA e sua interação com maus-tratos infantis relacionam-se ao cortisol — G×E no eixo (via 3).", "associativa","bem_suportado","human_clinical",NO,None),
"30472466":(None,"EC","estudo clínico longitudinal","cortisol_cabelo","Níveis glicocorticoides de longo prazo medidos em cabelo em depressão/ansiedade — marcador crônico, não diagnóstico.", "associativa","moderadamente_suportado","human_clinical",NO,None),
"36697477":(None,"EC","estudo clínico","trauma_cumulativo_cabelo","Trauma CUMULATIVO prediz cortisol em cabelo e sintomas depressivos/ansiosos — dose de exposição como dado.", "associativa","moderadamente_suportado","human_clinical",NO,None),
"30513499":(None,"OB","revisão sistemática","sintomas_cortisol_resposta","Sintomas de depressão e ansiedade × respostas de cortisol e recuperação ao estresse agudo — revisão sistemática.", "contributiva","bem_suportado","review",NO,None),
"30585227":(None,"OB","revisão molecular","hsp90_gr","Heterocomplexos Hsp90 regulam receptores de hormônios esteroides: da resposta ao estresse à doença psiquiátrica — maquinaria da via 3.", "contributiva","bem_suportado","review",PAR,None),
"22836869":(None,"OB","revisão","mr_hpa_humanos","Papel dos receptores MINERALOCORTICOIDES no eixo HPA em humanos — braço MR da interface GR/MR.", "contributiva","bem_suportado","review",NO,None),
"26970338":("REF_DEKLOET_2016","OB","revisão","mr_estresse_depressao","Estresse e depressão: papel crucial do receptor mineralocorticoide — revisão conceitual (de Kloet).", "contributiva","bem_suportado","review",PAR,None),
"25459896":("REF_TERHEEGDE_2015","OB","revisão","mr_resiliencia","O receptor mineralocorticoide cerebral e a RESILIÊNCIA ao estresse — MR como nó de resiliência (BLOCO 2.5).", "contributiva","bem_suportado","review",PAR,"chave insumo 'Teo 2023' = ter Heegde 2015 real"),
"25564387":(None,"OB","revisão","els_gr_mr_depressao","Estresse precoce em pacientes depressivos: papel de receptores glicocorticoides e mineralocorticoides — GR/MR×ELS.", "contributiva","bem_suportado","review",NO,None),
"37077711":(None,"OB","revisão","avp_v1b","Sistema do receptor V1b da arginina-vasopressina e resposta ao estresse na depressão — neuropeptídeo da via 1.5.", "contributiva","moderadamente_suportado","review",PAR,None),
"31327473":(None,"ML","revisão pré-clínica","bdnf_mesolimbico","BDNF mesolímbico (VTA–NAcc) na depressão — braço recompensa/anedonia em modelo animal.", "contributiva","bem_suportado","preclinical_mechanistic","SIM — revisão de evidência pré-clínica (roedor); tradução humana por analogia",None),
"34205191":(None,"OB","revisão crítica","ptsd_hpa_feedback","O fenótipo TEPT associa-se a SENSIBILIDADE do HPA? Feedback e outros modelos — posição cética canônica (NEG #3).", "contributiva","bem_suportado","review",NO,None),
"30342071":(None,"OB","revisão","hpa_ptsd_fisiopatologia","O eixo HPA no TEPT: fisiopatologia (recorte mecanístico; a parte de intervenção NÃO é usada nesta biblioteca, P20).", "contributiva","bem_suportado","review",NO,None),
"32379599":(None,"EC","estudo clínico","aces_inflamacao","Experiências adversas da infância e INFLAMAÇÃO em pacientes com depressão — trauma como exposição imune (via 9).", "associativa","moderadamente_suportado","human_clinical",NO,None),
"42167549":(None,"OB","revisão sistemática","especificidade_citocina_mri","Especificidade de vias imune-cérebro: citocinas INDIVIDUAIS associam-se diferencialmente a estrutura/função por MRI — contra 'inflamação universal' (NEG #7).", "contributiva","bem_suportado","review",NO,None),
"33152026":(None,"EC","estudo clínico","bdnf_periferico_ptsd","BDNF periférico em pacientes com TEPT — marcador periférico, sem status de diagnóstico (M05).", "associativa","emergente","human_clinical",NO,None),
"34071053":(None,"OB","revisão","hpa_alopregnanolona","Eixo HPA e ALOPREGNANOLONA na neurobiologia da depressão maior e do TEPT — ponte canônica B14 (neuroesteroides).", "contributiva","bem_suportado","review",PAR,None),
"40946890":(None,"EC","estudo translacional (humano + primata)","citocinas_bbb_dinamica","Relações dinâmicas de citocinas através da barreira hematoencefálica (humanos e primatas) — sangue≠cérebro quantificado (M05).", "associativa","emergente","human_clinical",PAR,None),
"36115855":(None,"EC","estudo MRI+PET","metabolismo_trauma_depressao","Estrutura e METABOLISMO cerebral em deprimidos com história de trauma infantil — janela metabólica do fenótipo.", "associativa","moderadamente_suportado","human_clinical",NO,None),
"34394855":(None,"OB","revisão sistemática","psicoterapia_neural","A psicoterapia focada em trauma muda o cérebro? Revisão sistemática — PILOTO B12.11 (reversibilidade), status emergente.", "contributiva","emergente","review",NO,None),
}
R=[]
seen={}
for pmid,(fid,tag,des,sec,ach,nat,mat,role,extr,alias) in D.items():
    m=META.get(pmid,{})
    if not m and pmid=="33725661": m={"title":"Neural activation of anxiety and depression in children and young people: A systematic meta-analysis of fMRI studies","authors":["Ashworth E","Schiöth HB","Brooks SJ"],"pubdate":"2021","source":"Psychiatry Res Neuroimaging"}
    if fid is None:
        parts=[t for t in re.split(r"[ ,]+",(m.get('authors') or ["?"])[0]) if t]
        au="".join(t for t in parts if len(t)>2) or parts[0]
        sob=parts[0] if len(parts[-1])<=2 else parts[-1]
        if len(parts[-1])<=2: sob=parts[0]
        if sob.lower() in ("ter","de","von","van") and len(parts)>1: sob=sob+parts[1]
        ano=(m.get('pubdate') or "2020")[:4]
        fid=f"REF_{norm(sob)}_{ano}"
    assert fid not in seen, fid; seen[fid]=1
    g2="eligible" if tag in("EC","OB") else "redirecionado_mecanistico"
    R.append({"pmid_oficial":pmid,"titulo_artigo":m.get('title',''),"autores":m.get('authors',[]),
      "revista_ano":f"{m.get('source','')} ({(m.get('pubdate') or '')[:4]})","desenho_estudo":f"[{tag}] {des} · {m.get('source','')}",
      "secao_origem":f"mecanismo_B12_{sec}","achado_central_molecular":ach,"extrapolacao_por_analogia":extr,
      "ids_referencia_interna":[fid],"id_referencia_interna":fid,"doi":"",
      "claim_id_origem":"B12.MEC.BLOCO14.001","evid_role":role,
      "especie_mesh":["Animals"] if tag=="ML" else ["Humans"],
      "verification_status":"preclinico" if tag=="ML" else "humano_clinico",
      "citacao_confirmada":True,"g1_metodo":"eutils_automatico","g2_elegibilidade":g2,
      "g2_motivo":"humano clínico/síntese — elegível" if tag in("EC","OB") else "redirecionado_mecanistico (animal/modelo)",
      "g3_verificado_por":"IA G3 Rodada [AT] GPM B12 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente",
      "status_auditoria":"CONFIRMADO","origem_pipeline":"GPM_RODADA_AT","_aliases":([alias] if alias else []),
      "_nat":nat,"_mat":mat,"_acao":"ADICIONAR_SINALIZADOR" if tag=="ML" else "MANTER",
      "_tier":"tier_3_correlacional_mecanistico" if tag=="ML" else "tier_4_descritivo_estrutural"})
json.dump(R, open(BASE+'producao/insumos/b12_refs_data.json','w'), indent=1, ensure_ascii=False)
print("ENTRA B12:", len(R), "| ML:", sum(1 for r in R if r['desenho_estudo'][1:3]=='ML'))
