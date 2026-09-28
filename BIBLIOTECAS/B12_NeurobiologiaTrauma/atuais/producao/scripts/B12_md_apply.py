# -*- coding: utf-8 -*-
import re, shutil, unicodedata, json
BASE='/home/user/BIBLIOTECAS/B12_NeurobiologiaTrauma/'
V1=BASE+'B12 NEUROBIOLOGIA DO TRAUMA V1 CANONICA.md'
V2=BASE+'B12 NEUROBIOLOGIA DO TRAUMA V2 CANONICA.md'
doc=unicodedata.normalize('NFC', open(V1,encoding='utf-8').read())
shutil.copy(V1, BASE+'producao/historico/v1_canonica_2026-09-09.md')
a="# B12 NEUROBIOLOGIA DO TRAUMA V1 CANÔNICA"
assert doc.count(a)==1
doc=doc.replace(a,"# B12 NEUROBIOLOGIA DO TRAUMA V2 CANÔNICA")
anc="## TABELA DE EVIDÊNCIAS"
assert doc.count(anc)==1
B="""## BLOCO_14 — CAMADA TRANSVERSAL RODADA [AT] 2026-09-09 (insumo externo auditado ref a ref; P-7)

[[AT 2026-09-09]] Reconciliação do insumo (RODADA0 + GPM molde v2.0 + matriz ChatGPT B12,
`APROVADO_COM_RESSALVAS`, claims B12.SM01–SM10). Universo auditado: 36 âncoras (2 já vigentes:
Shin 2010, Logue 2018) + 146 não citadas + NAO-IDX declarados. Decisão: **ENTRA 74** (34
âncoras novas + 40 selecionados), **BAIXO ~55**, **EXC** (malha: TBI ×6, Alzheimer/
neurodegeneração ×5, psicose ×1, stroke ×1, substância ×1, NAO-IDX ×7-8). A camada nova é
predominantemente humana `[EC]/[OB]`; os quatro itens pré-clínicos entram com `[ML]` e
extrapolação explícita. Números de efeito do insumo = alegação não copiada (regra 10).

### 14.1 Fundamento: trauma como programador/sensibilizador (SM01)

O modelo canônico é programação/sensibilização, não causa única — consagrado pela revisão
fundacional de adversidade infantil na neurobiologia de humor e ansiedade (Heim & Nemeroff
2001)[OB].
A síntese dirigida trauma infantil×HPA×doença psiquiátrica confirma associação COM
heterogeneidade de direção e magnitude (Murphy 2022)[OB].
O estresse precoce foi revisado do lado dos receptores glicocorticoide e mineralocorticoide em
pacientes depressivos (Juruena 2015)[OB].
Os traços neuroestruturais de adversidades precoces mostram especificidade por IDADE e TIPO de
adversidade — a janela sensível é dado empírico, não metáfora (Pollok 2022)[OB].
Em crianças e jovens, a ativação neural de ansiedade e depressão difere do padrão adulto em
meta-análise dedicada — desenvolvimento muda o mapa (Ashworth 2021)[OB].

*HeimNemeroff2001_fundacao[OB] | Murphy2022_sintese[OB] | Juruena2015_GRGR[OB] | Pollok2022_janela[OB] | Ashworth2021_jovens[OB]*

### 14.2 HPA × trauma: heterogeneidade como conteúdo canônico (SM02)

Em depressão unipolar com trauma infantil, a atividade do HPA medida por teste combinado é
heterogênea — não existe "cortisol alto do trauma" (Lu 2016)[EC].
A depressão ansiosa dependente de trauma sensibilizou o HPA em amostra clínica com
dexametasona e genotipagem (Menke 2018)[EC].
Trauma infantil modula a resposta antidepressiva via atividade do HPA — exposição muda
trajetória, não determina desfecho (Nikkheslat 2020)[EC].
A posição cética também entra: se o fenótipo TEPT se associa a sensibilidade do HPA é questão
aberta de feedback e modelagem (Danan 2021)[OB].
A fisiopatologia do HPA no TEPT foi revista em separado — o recorte usado aqui é mecanístico;
a parte de intervenção permanece fora (P20) (Dunlop 2019)[OB].
Genes do eixo HPA interagem com maus-tratos infantis sobre o cortisol — G×E no eixo
(Gerritsen 2017)[EC].
Glicocorticoides de longo prazo em cabelo diferenciam depressão/ansiedade como marcador
crônico, nunca diagnóstico (Gerritsen 2019)[EC].
Trauma CUMULATIVO prediz cortisol em cabelo e sintomas — dose de exposição como variável
(Dobernecker 2023)[EC].
A revisão sistemática de respostas de cortisol e recuperação ao estresse agudo em sintomas
depressivos/ansiosos consolida a leitura não-linear (Fiksdal 2019)[OB].
A interface GR/MR do HPA na depressão foi avaliada em revisão dedicada (Von Werne Baes
2012)[OB], complementada pela maquinaria Hsp90 dos receptores de esteroides (Baker 2018)[OB],
pelo braço mineralocorticoide em humanos (Berardelli 2013)[OB], pela revisão conceitual do MR
em estresse e depressão (de Kloet 2016)[OB] e pelo MR cerebral como nó de RESILIÊNCIA
(ter Heegde 2015)[OB].
FKBP5 modula a RECUPERAÇÃO do estresse agudo em humanos saudáveis — interface, não causa
(Ising 2008)[EC]; a expressão periférica de mRNA de GR/FKBP5 é marcador associativo em
depressão/ansiedade (Hori 2024)[EC].
O eixo vasopressinérgico (receptor V1b) completa o mapa neuropeptídico da resposta ao estresse
na depressão (Kanes 2023)[OB].
A microglia e o HPA na depressão foram revistos como ponte, sem invasão do B1 (Cheiran
2022)[OB].

*Lu2016_heterogeneo[EC] | Menke2018_sensibiliza[EC] | Nikkheslat2020_resposta[EC] | Danan2021_cetico[OB] | Dunlop2019_fisio[OB] | Gerritsen2017_GxE[EC] | Gerritsen2019_cabelo[EC] | Dobernecker2023_cumulativo[EC] | Fiksdal2019_SR[OB] | VonWerneBaes2012_GRMR[OB] | Baker2018_Hsp90[OB] | Berardelli2013_MR[OB] | deKloet2016_MR[OB] | terHeegde2015_resiliencia[OB] | Ising2008_FKBP5[EC] | Hori2024_mRNA[EC] | Kanes2023_V1b[OB] | Cheiran2022_microglia[OB]*

### 14.3 Circuito da ameaça, memória e extinção (SM03/SM05/SM06)

As assinaturas neurais de condicionamento, extinção e reevocação da extinção foram medidas no
TEPT — a via 7 ganha ancoragem humana direta (Suarez-Jimenez 2020)[EC].
A memória traumática foi buscada em meta-análise de provocação de sintomas: padrão funcional
replicável, sem localização única (Sartory 2013)[OB].
As disrupções de circuitos emocionais são COMUNS entre transtornos — transdiagnóstico, não
específicas do trauma (McTeague 2020)[OB].
No maior consórcio de neuroimagem, a conectividade amígdala–hipocampo de repouso no TEPT foi
medida em escala multi-sítio (Hinojosa 2026)[EC].
O sexo modula exposição à violência e reatividade neural à ameaça — modulador obrigatório
(Dark 2022)[EC].

*SuarezJimenez2020_extincao[EC] | Sartory2013_memoria[OB] | McTeague2020_comum[OB] | Hinojosa2026_ENIGMA[EC] | Dark2022_sexo[EC]*

### 14.4 Neuroimagem transdiagnóstica — o regulador do módulo (SM04 — regra 7)

A parte compartilhada e a específica entre depressão, ansiedade e TEPT foi quantificada em
revisão com meta-análise (Serra-Blasco 2021)[OB]; a comparação estrutural direta TEPT×TDM já
estava consolidada na V1 (Bromis 2018), junto à meta-análise volumétrica em TEPT
(O'Doherty 2015)[OB].
O TEPT multimodal (função+estrutura) tem meta-análise própria (Xiao 2022)[OB], e a atividade
neural funcional, outra (Hayes 2012)[OB].
A especificidade por SUB-REGIÃO de hipocampo/amígdala no TEPT foi revisada em escopo
(Ben-Zion 2024)[OB], e a meta-análise ALE de massa cinzenta apontou lateralidade esquerda
(Del Casale 2022)[OB].
Medo patológico, ansiedade e afeto negativo têm assinaturas neuroestruturais DISTINTAS
(Liu 2022)[OB]; os fenótipos neurais compartilhados foram medidos em 226 estudos task-fMRI
(Janiri 2020)[OB].
A ansiedade INDUZIDA reproduz a PATOLÓGICA no fMRI — validação experimental do circuito
(Chavanne 2021)[OB].
Nos transtornos de ansiedade, ACC/PFC mostram traços comuns em VBM (Shang 2014)[OB], o
repouso tem meta-análise própria (Zugman 2023)[OB] e a amígdala, meta-análise de
conectividade por coordenadas (Lu 2026)[OB] e multimodal (Cao 2026)[OB].
Harm avoidance tem correlatos multimodais próprios (Zhong 2024)[OB].
A terminologia das redes é instável — 'PFC' e 'ACC' sobrepõem-se espacialmente em meta-análise
(Marusak 2016)[OB].
Mudanças comuns e específicas em larga escala entre depressão, ansiedade e dor crônica
completam o panorama transdiagnóstico (Brandl 2022)[OB], atualizado por meta-análise
recente de correlatos estruturais (Guo 2025)[OB].
A depressão COM ansiedade tem perfil volumétrico próprio revisado (Espinoza 2020)[OB].
Afeto negativo tem meta-análise comparativa (Schulze 2019)[OB].
Em deprimidos com história de trauma infantil, estrutura e METABOLISMO cerebrais foram medidos
em conjunto (Jones 2022)[EC].

*SerraBlasco2021_trans[OB] | ODoherty2015_vol[OB] | Xiao2022_multimodal[OB] | Hayes2012_funcional[OB] | BenZion2024_subregioes[OB] | DelCasale2022_ALE[OB] | Liu2022_distintos[OB] | Janiri2020_226[OB] | Chavanne2021_induzida[OB] | Shang2014_VBM[OB] | Zugman2023_repouso[OB] | Lu2026_ALE[OB] | Cao2026_conectividade[OB] | Zhong2024_harm[OB] | Marusak2016_terminologia[OB] | Brandl2022_larga[OB] | Guo2025_atualizacao[OB] | Espinoza2020_comorbida[OB] | Schulze2019_afeto[OB] | Jones2022_metabolismo[EC]*

### 14.5 BDNF/plasticidade: os dois braços e a fronteira epigenética (SM07/SM10)

A neurobiologia do BDNF na memória de medo e sensibilidade ao estresse permanece
primariamente animal (Notaras 2020)[ML]; a expressão serotoninérgica de BDNF melhora
resiliência em modelo (Leschik 2022)[ML].
O braço mesolímbico (VTA–NAcc) do BDNF sustenta a leitura recompensa/anedonia em modelo
(Koo 2019)[ML].
Do lado molecular geral, a sinalização BDNF foi revista em contexto (Wang 2022)[OB] e na
patogênese de transtornos por estresse (Numakawa 2023)[OB].
O modelo integrativo de neuroplasticidade em depressão (Price 2020)[OB] e a desregulação da
plasticidade hipocampal adulta na TDM (Tartt 2022)[OB] permanecem pontes declaradas a B3/B16
— a maquinaria não é reivindicada aqui (regra 5).
A interação Val66Met×trauma é bidirecional em evidência (Yu 2012)[EC] e plasticidade cerebral
(Tian 2021)[EC].
Fatores neurotróficos×trauma infantil têm revisão sistemática própria (Di Benedetto 2022)[OB]
e BDNF periférico no TEPT, estudo dedicado (Mojtabavi 2020)[EC] — nenhum com status
diagnóstico (M05).
A fronteira epigenética (regra 8): regulação epigenética do BDNF sob estresse (Miao 2020)[OB],
metilação multicamada do BDNF no TEPT (Wang 2026)[OB], metilação de NR3C1/SLC6A4 com cortisol
embotado na depressão (Bakusic 2020)[EC], metilação do gene GR relacionada a trauma infantil
(Farrell 2018)[EC] e metilação do BDNF em mães e recém-nascidos expostos a guerra — a
intergeracionalidade medida sem Lamarckismo (Kertes 2017)[EC].

*Notaras2020_medo[ML] | Leschik2022_resiliencia[ML] | Koo2019_mesolimbico[ML] | Wang2022_sinalizacao[OB] | Numakawa2023_estresse[OB] | Price2020_integrativo[OB] | Tartt2022_hipocampal[OB] | Yu2012_Val66Met[EC] | Tian2021_GxE[EC] | DiBenedetto2022_SR[OB] | Mojtabavi2020_periferico[EC] | Miao2020_epigenetica[OB] | Wang2026_metilacao[OB] | Bakusic2020_NR3C1[EC] | Farrell2018_GRmetilacao[EC] | Kertes2017_guerra[EC]*

### 14.6 Imunidade bidirecional e especificidade (SM08 — sem "inflamação universal")

Citocinas como alvos centrais sobre neurotransmissores e circuitos (Miller 2013)[OB]; a
bidirecionalidade é a formulação canônica (Rengasamy 2021)[OB].
Em evidência experimental, citocinas pró e anti-inflamatórias modulam bidirecionalmente
circuitos amigdalaros da ansiedade (Lee 2025)[ML].
Experiências adversas da infância associam-se a INFLAMAÇÃO em pacientes com depressão —
exposição, não universalidade (Gill 2020)[EC].
Citocinas INDIVIDUAIS mapeiam estrutura/função cerebral de forma diferencial — especificidade
contra a leitura "inflamação universal" (Cordero 2026)[OB].
A dinâmica de citocinas através da barreira hematoencefálica em humanos e primatas quantifica
o princípio sangue≠cérebro (Tyagi 2026)[EC].
O eixo HPA×alopregnanolona na depressão e no TEPT fixa a ponte canônica aos neuroesteroides
B14 (Almeida 2021)[OB].

*Miller2013_alvos[OB] | Rengasamy2021_bidirecional[OB] | Lee2025_neuromodulacao[ML] | Gill2020_ACEs[EC] | Cordero2026_especificidade[OB] | Tyagi2026_BBB[EC] | Almeida2021_alopreg[OB]*

### 14.7 Reversibilidade — piloto B12.11 [G1 ancorado parcialmente]

A pergunta "a psicoterapia focada em trauma muda o cérebro?" tem revisão sistemática: sinais
neurais de remodelação — PILOTO da reversibilidade (B12.11), mantido como emergente e sem
conduta (P20) (Manthey 2021)[OB].

*Manthey2021_piloto[OB]*

## BLOCO_15 — DEZ REGRAS FUNDADORAS FIXADAS (B12-REGRA-01..10) E EXPOSIÇÕES DA RODADA

[[AT 2026-09-09]] Regras do GPM oficial (M00), promovidas a canônicas:

- **B12-REGRA-01 (nada determinístico):** os dez bloqueios ("trauma causa depressão",
  "trauma reduz hipocampo", "trauma = cortisol alto", "FKBP5 causa doença", "BDNF baixo
  obrigatório", "amígdala hiperativa = biomarcador", "neuroinflamação universal",
  "alteração permanente", "trauma = causa da ansiedade") permanecem PROIBIDOS na prosa.
- **B12-REGRA-02 (alteração estrutural ≠ biomarcador diagnóstico):** a tríade
  amígdala↑/hipocampo↓/PFC↓ é heterogênea e transdiagnóstica (Serra-Blasco 2021; Janiri 2020).
- **B12-REGRA-03 (hipocampo com causalidade indeterminada):** vulnerabilidade prévia vs efeito
  do trauma não se separam na evidência estrutural (Logue 2018; Paquola 2016) — a
  indeterminação é o registro canônico.
- **B12-REGRA-04 (FKBP5/GR = interface molecular, não causa)** (Menke 2018; Ising 2008).
- **B12-REGRA-05 (não duplicar B1/B2/B3):** imunidade molecular → B1; maquinaria plástica →
  B3/B16; HPA fisiológico → B2; aqui apenas o braço trauma-dependente.
- **B12-REGRA-06 (TBI ≠ trauma psicológico):** seis itens do insumo excluídos pela malha
  (Bodnar 2018; Feiger 2022; Malik 2022; Malik 2023; Tapp 2019; Risbrough 2021).
- **B12-REGRA-07 (transdiagnóstico obrigatório):** TEPT não infla TDM/TAG; meta-análises
  comparativas regulam o módulo (Serra-Blasco 2021; Guo 2025; Cao 2026; Liu 2022).
- **B12-REGRA-08 (epigenética = fronteira promissora):** metilação é ASSOCIATIVA; causalidade
  humana não estabelecida (Miao 2020; Wang 2026; Kertes 2017).
- **B12-REGRA-09 (psicoterapia = piloto de reversibilidade):** B12.11 ancorado com status
  emergente (Manthey 2021) — demais âncoras de intervenção continuam fora do canônico.
- **B12-REGRA-10 (PMID do insumo sempre verificado; anos = print):** o PMID da triagem para
  Logue era INVÁLIDO (paper não-relacionado) → substituído pelo ENIGMA-PGC verificado; 12
  chaves do insumo divergiam do artigo real ao PMID e foram normalizadas com alias
  ("See 2025"→Serra-Blasco 2021; "Mayer 2020"→McTeague 2020; "Teo 2023"→ter Heegde 2015;
  "Oyarce 2020"→Espinoza 2020; "Deuter 2023"→Di Benedetto 2022; "Begni 2016"→Ben-Zion 2024;
  "Ferracuti 2022"→Del Casale 2022; "Pereira 2021"→Cheiran 2022; "Daskalakis 2022"→Dell'Oste
  2024 (BAIXO); "Fullana 2018"→Gędek 2025 (BAIXO); "Romeo 2024"→Sălcudean 2025 (BAIXO);
  "Cheng 2025"→Colucci-D'Amato 2020 (BAIXO); "Ashworth 2021"→Badowska-Szalewska 2021 no PMID
  do dossiê — o Ashworth real foi resolvido por DOI; 'Vogelzangs 2016' é duplicata da âncora
  Von Werne Baes 2012 exposta).

**[G1] mantidos:** GWAS FKBP5×trauma dedicado; réplica dos fenótipos de extinção em TDM/TAG
(hoje TEPT-centrados); medicação como moduladora (camada C); âncora B12×B7 no B7
(microbiota); e os sinalizados legados da V1 não localizados no insumo auditado (Peng 2023,
Zou 2024, Duran 2025, Gong 2026, Wingo PPM1F, Takahashi 2025, Mehta) — permanecem `[G1]`,
não forjados.

"""
doc=doc.replace(anc, B+anc)
linha="| Autonômico | VFC reduzida, FC elevada no TEPT | médio (marcador) |"
assert doc.count(linha)==1
doc=doc.replace(linha, linha+"""
| [AT] HPA×trauma | Heterogêneo (Lu; Danan); sensibilização no fenótipo ansioso-depressivo; cabelo = crônico | médio (direção não única) |
| [AT] Extinção/condicionamento | Assinaturas neurais TEPT medidas (condicionamento, extinção, reevocação) | alto (humano, transdiagnóstico) |
| [AT] Transdiagnóstico estrutural | Compartilhado > específico; TDM×ansiedade×TEPT parcialmente comuns | alto (metas convergentes) |
| [AT] BDNF×trauma | G×E (Val66Met); dois braços (medo [ML] + recompensa [ML]); periférico sem Dx | médio (interação); periférico baixo |
| [AT] Epigenética | NR3C1/FKBP5/BDNF metilação; intergeracional guerra | baixo-médio/emergente (fronteira) |
| [AT] Imunidade trauma | ACEs × inflamação; citocinas específicas × MRI; sangue≠cérebro | médio (especificidade) |
| [AT] Reversibilidade | Psicoterapia remodela circuitos (piloto) | emergente (B12.11) |""")
a3=doc[doc.index("> **Canônica v1 (Rodada 3).**"):]
fim=a3.index("avaliador cego) é pendência do avaliador externo.")+len("avaliador cego) é pendência do avaliador externo.")
trecho=doc[doc.index("> **Canônica v1 (Rodada 3).**"):doc.index("> **Canônica v1 (Rodada 3).**")+fim]
nova="""> **Canônica v2 (Rodada 4 — [AT] 2026-09-09).** Reconciliação de insumo externo auditado
> ref a ref (P-7): ENTRA 74 / BAIXO ~55 / EXC malha (TBI ×6, neurodegeneração, psicose,
> stroke, substância, NAO-IDX). Camada transversal adicionada nos BLOCOS 14–15; dez regras
> fundadoras fixadas; modelo multiplicativo preservado (nada determinístico). Sem PMID no
> texto; psicoterapia = piloto emergente, não conduta (P20). 2ª verificação independente
> (P-6, avaliador cego) permanece pendência do avaliador externo — cobrindo todas as levas
> [AT] de B1–B16."""
doc=doc.replace(trecho, nova)
assert doc.count("corte 2026-09-06")==1
doc=doc.replace("corte 2026-09-06","corte 2026-09-09 (rodada [AT])")
assert not re.search(r'\d{7,9}', doc)
open(V2,'w',encoding='utf-8').write(doc)
print("V2 gravada | palavras:", len(doc.split()))
# verificar as 74 citações
R=json.load(open(BASE+'producao/insumos/b12_refs_data.json'))
MAP={"REF_HEIM_2001a":"(Heim & Nemeroff 2001)","REF_VONWERNEBAES_2012":"(Von Werne Baes\n2012)","REF_DEKLOET_2016":"(de Kloet 2016)","REF_TERHEEGDE_2015":"(ter Heegde\n2015)"}
falt=[]
for r in R:
    rid=r['id_referencia_interna']; ano=rid.rsplit('_',1)[1]
    if rid in MAP: chave=MAP[rid]
    else:
        sob=rid[4:].rsplit('_',1)[0].capitalize()
        especiais={"Suarezjimenez":"Suarez-Jimenez","Odoherty":"O'Doherty","Rengasamy":"Rengasamy"}
        sob=especiais.get(sob,sob)
        chave=f"({sob} {ano})"
    found=any(chave.split('\n')[0] in l and '[' in l for l in doc.split('\n')) if '\n' not in chave else all(any(chave.split('\n')[i] in ll for ll in doc.split('\n')) for i in range(2))
    if not found: falt.append((rid,chave))
print("faltantes:", falt)
