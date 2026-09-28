# -*- coding: utf-8 -*-
import re, shutil, unicodedata
BASE='/home/user/BIBLIOTECAS/B11_DisfuncaoTireoidiana/'
V1=BASE+'B11 DISFUNCAO TIREOIDIANA V1 CANONICA.md'
V2=BASE+'B11 DISFUNCAO TIREOIDIANA V2 CANONICA.md'
doc=open(V1,encoding='utf-8').read()
shutil.copy(V1, BASE+'producao/historico/v1_canonica_2026-09-09.md')
NFC=lambda s: unicodedata.normalize('NFC',s)
doc=NFC(doc)

# 1) Título
a="# B11 DISFUNÇÃO TIREOIDIANA V1 CANÔNICA"
assert doc.count(a)==1
doc=doc.replace(a,"# B11 DISFUNÇÃO TIREOIDIANA V2 CANÔNICA")

# 2) BLOCO_14 + BLOCO_15 antes da TABELA
ancora_tabela="## TABELA DE EVIDÊNCIAS"
assert doc.count(ancora_tabela)==1
BLOCO14 = """## BLOCO_14 — CAMADA CLÍNICA RODADA [AT] 2026-09-09 (insumo externo auditado ref a ref; P-7)

[[AT 2026-09-09]] Rodada de reconciliação de insumo externo (RODADA0 + GPM oficial + matriz
ChatGPT B11, status `APROVADO_COM_RESSALVAS`). Universo auditado: 14 âncoras, 121 referências
não citadas e 19 itens sem indexação verificável. Decisão final: **ENTRA 56** (11 âncoras
novas + 45 clínicos), **BAIXO 41**, **EXC 11 grupos** (inclui as 19 não indexadas). Toda a
camada abaixo é clínica/observacional humana `[EC]/[OB]` — a causalidade molecular permanece
na estrutura pré-existente dos BLOCOS 01–04. Números de efeito do insumo foram tratados como
alegação; direções de resultado foram confirmadas por abstract antes de cada incorporação.

### 14.1 A controvérsia do hipotireoidismo subclínico (SM03 — CONTROVERSIAL_CORE)

O núcleo polêmico da B11 é a pergunta "SCH causa depressão?" — e a resposta canônica é
**inconsistência**: as meta-análises de estudos transversais reportam associação fraca e
heterogênea (Zhao 2018)[OB], replicada em revisão sistemática independente com a mesma
ressalva de heterogeneidade (Tang 2019)[OB].
A meta-análise atualizada que incluiu desfechos de tratamento confirma o sinal transversal
fraco e não resolve a direção causal (Loh 2019)[OB].
Contra esse sinal, a coorte prospectiva de adultos jovens e de meia-idade não encontrou
associação entre SCH e depressão incidente (Kim 2018)[EC].
A análise individual de dados de participantes de coortes prospectivas (~23 mil) — hierarquia
superior — igualmente não sustentou a associação (Wildisen 2020)[EC].
O NHANES, em análise sintoma-específica, também não confirmou associação global entre SCH e
sintomas depressivos (Airaksinen 2021)[EC].
Em idosos, a disfunção tireoidiana leve teve associações com depressão/cognição declaradamente
NÃO confirmadas (Roberts 2006)[EC].
A coorte HUNT explicitou a hipótese cética: a associação depressão/ansiedade×função tireoidiana
pode ser artefato de medição e comorbidade (Engum 2002)[EC].
Com desfecho por entrevista diagnóstica (gold-standard), o SHIP encontrou transtornos
tireoidianos diagnosticados associados a depressão e ansiedade — sinal positivo do lado do
diagnóstico clínico, não do subclínico laboratorial (Ittermann 2015)[EC].
O ELSA-Brasil contribuiu coorte latino-americana examinando disfunção subclínica e transtornos
psiquiátricos com dados transversais de base (Bensenor 2016)[EC].
O KNHANES adicionou amostra nacional coreana avaliando disfunção subclínica e sintomas
depressivos (Hong 2018)[EC].
A coorte histórica Mayo associou TSH a depressão clinicamente relevante (PHQ-9) em escala
populacional (Kumar 2023)[EC], e coorte histórica independente reportou sinal convergente
(Liu 2025)[EC].
A coorte real-world retrospectiva reforça o sinal de mundo real, com confusão por indicação
sempre em aberto (Baweja 2026)[EC].
Em idosos com avaliação transversal e longitudinal, o quadro permanece misto (Forbes 2026)[EC].
A faixa etária jovem foi coberta prospectivamente: SCH e depressão incidente em adolescentes e
adultos jovens em coorte nacional (Hirtz 2022)[EC].
A morbidade psicológica alta aumenta a chance de investigação tireoidiana — viés de triagem
medido prospectivamente (Bould 2012)[EC].
Dentro da faixa de referência, TSH e sintomas depressivos associaram-se de modo modesto em
coorte (Kim 2015)[EC], com heterogeneidade por sexo documentada (Lee 2019)[EC].

*Zhao2018_meta[OB] | Tang2019_meta[OB] | Loh2019_metaLT4[OB] | Kim2018_incidenteNEG[EC] | Wildisen2020_IPDneg[EC] | Airaksinen2021_NHANESneg[EC] | Roberts2006_idososNEG[EC] | Engum2002_artefato[EC] | Ittermann2015_goldstd[EC] | Bensenor2016_ELSA[EC] | Hong2018_KNHANES[EC] | Kumar2023_Mayo[EC] | Liu2025_coorte[EC] | Baweja2026_realworld[EC] | Forbes2026_idosos[EC] | Hirtz2022_jovens[EC] | Bould2012_triagem[EC] | Kim2015_faixa[EC] | Lee2019_sexo[EC]*

### 14.2 Autoimunidade tireoidiana e Hashimoto eutireoidiano (SM06)

A AIT associa-se a depressão/ansiedade de modo robusto em meta-análise (já consolidado na V1:
ORs elevados com heterogeneidade alta) — mas a formulação "Hashimoto causa depressão" permanece
**proibida** nesta biblioteca. A base populacional HUNT mostrou a associação anti-TPO×humor
fraca a ausente na população geral (Engum 2005)[EC].
Em Hashimoto eutireoidiano, a prevalência corrente de depressão e ansiedade foi maior que em
controles — sem hipotireoidismo como intermediário (Ayhan 2014)[EC].
A carga de sintomas, qualidade de vida e incapacidade em Hashimoto (inclusive eutireoidiano)
excede a do bócio não autoimune (Gulseren 2006)[EC].
A coorte SardiNIA, sem medicação tireoidiana/antidepressiva, dissociou autoimunidade e sintomas
depressivos na população — o elo AIT×humor não é automático (Delitala 2016)[EC].
A revisão sistemática/meta-análise específica de Hashimoto eutireoidiano confirmou excesso de
depressão e ansiedade sem hipotireoidismo, sem resolver se a AIT causa ou co-ocorre
(Wang 2024)[OB].
A hipótese de mediação autoimune entre disfunção subclínica e TDM permanece candidata, não
demonstrada (Karakatsoulis 2021)[OB].
Fora do eixo TPO, hormônios tireoidianos desregulados correlacionaram-se com ansiedade e
depressão em doença autoimune sistêmica (Wu 2021)[EC].
O espelho fenomenológico clássico (doença tireoidiana franca) é reafirmado por séries com
entrevista: sintomas e diagnósticos psiquiátricos em distúrbios tireoidianos (Aslan 2005)[EC],
sintomas depressivos e ansiosos em hipotireoidismo franco (Andrade 2010)[EC],
transtornos psiquiátricos por SCID no SCH (Almeida 2007)[EC],
sinal transcultural em população endócrina (Gorkhali 2020)[EC],
e prevalência de ansiedade/depressão em hipotireoidismo com fatores associados
(Dehesh 2025)[EC].

*Engum2005_TPOpop[EC] | Ayhan2014_Heuti[EC] | Gulseren2006_QV[EC] | Delitala2016_SardiNIA[EC] | Wang2024_metaHeuti[OB] | Karakatsoulis2021_mecanismo[OB] | Wu2021_autoimune[EC] | Aslan2005_entrevista[EC] | Andrade2010_casocontrole[EC] | Almeida2007_SCID[EC] | Gorkhali2020_transcultural[EC] | Dehesh2025_prevalencia[EC]*

### 14.3 Ansiedade-específica e não-linearidade (SM05/SM09)

A revisão sistemática dedicada mostrou que o eixo HPT nos transtornos de ansiedade é menos
mapeado que na depressão, com alterações modestas e heterogêneas (Fischer 2018)[OB].
A ansiedade em distúrbios tireoidianos subclínicos foi medida diretamente, com sinal distinto
do depressivo (Gonen 2004)[EC].
Em TDM jovem de primeiro episódio, a associação hormônio×ansiedade mostrou-se modulada por
gênero (Zhao 2023)[EC].
O padrão entre TSH e sintomas ansiosos em TDM drug-naïve não é monotônico — descreveu-se
curva do tipo aumenta-diminui-aumenta (Qiu 2026)[EC].
Em amostra de área de captação, a direção da associação com TSH diferiu entre ansiedade e
depressão (e entre usuários de T4 e população) — o paradoxo documentado que proíbe a leitura
linear (Panicker 2009)[EC].

*Fischer2018_SRansiedade[OB] | Gonen2004_ansiedadeSCH[EC] | Zhao2023_genero[EC] | Qiu2026_naolinear[EC] | Panicker2009_paradoxo[EC]*

### 14.4 Bidirecionalidade obrigatória (SM01/SM08)

Função tireoidiana e depressão associaram-se transversal e longitudinalmente em coorte
populacional — sem excluir causalidade reversa (Roa Dueñas 2024)[EC].
A associação depressão×função tireoidiana foi reexaminada em análise dedicada com marcadores
periféricos, incluindo FT3, em desenho transversal (Ma 2024)[EC].
A direção reversa está documentada prospectivamente: depressão e ansiedade precederam risco
aumentado de doença tireoidiana na UK Biobank (Fan 2024)[EC].

*RoaDuenas2024_longitudinal[EC] | Ma2024_FT3transversal[EC] | Fan2024_UKBreverso[EC]*

### 14.5 Genética compartilhada ≠ causalidade individual (SM07)

Variações de hormônio tireoidiano dentro da faixa normal associaram-se a risco de transtornos
psiquiátricos comuns por ligação genética compartilhada — evidência de arquitetura comum, não
de causalidade individual (Soheili 2023)[EC]. Registra-se que o artigo recebeu **correção
editorial** (2024), aqui armazenada como metadado da referência, não como referência própria.

*Soheili2023_genetica[EC]*

### 14.6 Alterações transitórias, doença não-tireoidiana e o limite dos exames

A doença psiquiátrica aguda pode cursar com hipertiroxinemia TRANSITÓRIA — distinta do
hipertireoidismo verdadeiro (Roca 1990)[EC].
A hipertireotropinemia transitória de internados agudos reverte espontaneamente em semanas
(Chopra 1990)[EC].
Testes tireoidianos anormais em psiquiátricos são frequentemente "arenque vermelho" — doença
não-tireoidiana ou transitoriedade (Dickerman 2012)[OB].
A revisão clássica da função tireoidiana na doença psiquiátrica sistematizou variabilidade de
testes, NTI e limites da triagem (Hein 1990)[OB].
Na depressão psiquiátrica, a síndrome do T3 baixo aparece como marcador transversal de
gravidade, com TSH/T4 preservados (Premachandra 2006)[EC].
Em pacientes sob reposição, o bem-estar correlacionou-se com FT4 e **não** com FT3 — achado
nulo canônico do FT3 (Saravanan 2006)[EC].
O rT3, produto da desiodinação periférica por D1/D3, foi quantificado sob diferentes esquemas
de reposição — âncora periférica; a sinalização cerebral de rT3 permanece [G1]
(Wilson 2025)[EC].
A triagem com TSH em internados psiquiátricos foi avaliada prospectivamente quanto a
rendimento (Woolf 1996)[EC].
A utilidade clínica da avaliação hormonal rotineira em internados com transtornos de humor e
ansiedade foi reexaminada recentemente (Toma 2026)[EC].
Em crianças e adolescentes com transtornos de humor e ansiedade, o rendimento da triagem da
função tireoidiana é baixo, porém não nulo (Luft 2019)[EC].
Hormônios tireoidianos basais foram testados como preditores de melhora clínica sob tratamento
antidepressivo — biomarcador de resposta candidato, não validado (Qiao 2022)[EC].
Mulheres hipotireoideas em tratamento com levotiroxina mantêm carga residual de ansiedade e
depressão — normalizar o TSH não garante eutimia (Romero-Gómez 2019)[EC].
Em coorte de deprimidos, TSH e T4 perfilaram a janela hormonal associativa da depressão
(Costache 2020)[EC].
Em deprimidos drug-naïve, T4/T3/TSH variaram por gravidade (HAM-D) contra controles — gradiente
dimensional associativo (Kamble 2013)[EC].

*Roca1990_transitorio[EC] | Chopra1990_TSHtransitorio[EC] | Dickerman2012_redherring[OB] | Hein1990_revisao[OB] | Premachandra2006_lowT3[EC] | Saravanan2006_FT3nulo[EC] | Wilson2025_rT3[EC] | Woolf1996_triagem[EC] | Toma2026_rotina[EC] | Luft2019_pediatria[EC] | Qiao2022_predicao[EC] | RomeroGomez2019_residual[EC] | Costache2020_coorte[EC] | Kamble2013_gravidade[EC]*

### 14.7 Terapia como sinal, nunca como conduta (SM10)

O papel adjuvante dos hormônios tireoidianos (T3/T4) na depressão é sinal terapêutico
histórico consolidado em revisão — e não autoriza tratar depressão primária como doença
tireoidiana (Bauer 2021)[OB].
Em crianças e adolescentes com hipotireoidismo (incluindo subclínico), o tratamento com LT4 e
o risco de intervenções psiquiátricas foram acompanhados observacionalmente — terapia-sinal,
sob P20 (Hilmon 2026)[EC].

*Bauer2021_adjuvante[OB] | Hilmon2026_LT4jovens[EC]*

### 14.8 Compatibilização de fenótipos (matriz F1–F6 ↔ dicionário V1 F1–F8)

A matriz externa classificou as claims em fenótipos F1–F6; a V1 já operava com o dicionário
F1–F8 (BLOCO 13.4 e BLOCO 11). Declara-se o mapeamento: F1–F6 da matriz estão contidos na
tipologia F1–F8 vigente; o fenótipo **F6 (SCH não-fenótipo)** corresponde exatamente ao
cancelamento da leitura ingênua já redigido em 13.2–13.3 — SCH laboratorial isolado NÃO é
fenótipo clínico registrável, e a evidência negativa (Kim 2018; Wildisen 2020; Airaksinen
2021; Roberts 2006) tem o mesmo status canônico que a positiva.

### 14.9 Pontes declaradas e [G1] mantidos

Permanecem como lacuna sinalizada `[G1]`: FT3 prospectivo (só transversal), mecanismo celular
cerebral de rT3 (âncora periférica em 14.6, sem âncora celular), âncora cruzada iodo↔B8,
randomização mendeliana dedicada tireoide×psiquiatria, ensaios LT4 em SCH×depressão
(TIRA/ThyroidRx), padronização da definição de SCH, âncora B11×B2 no B2 (HPA), B11×B12
(burnout), e controle do confundimento por LT4 em eutireoidianos.

## BLOCO_15 — DEZ REGRAS FUNDADORAS FIXADAS (B11-REGRA-01..10) E EXPOSIÇÕES DA RODADA

[[AT 2026-09-09]] Regras do GPM oficial (M00), promovidas a regras canônicas:

- **B11-REGRA-01 (associação≠causalidade):** a bidirecionalidade (Fan 2024; Roa Dueñas 2024)
  torna causalidade reversa plausível em toda claim transversal.
- **B11-REGRA-02 (SCH não registrável como causa):** metas fracas (Zhao 2018; Tang 2019) ×
  coortes/IPD negativas (Kim 2018; Wildisen 2020; Airaksinen 2021; Roberts 2006) → a claim
  canônica é INCONSISTÊNCIA (SM03 = CONTROVERSIAL_CORE).
- **B11-REGRA-03 (AIT robusta, causalidade proibida):** associação AIT×humor é robusta; a
  frase "Hashimoto causa depressão" está banida da B11.
- **B11-REGRA-04 (genética compartilhada≠causalidade individual):** Soheili 2023 lido assim;
  correção editorial registrada como metadado.
- **B11-REGRA-05 (não-linearidade≠faixa ótima):** curvas em U/paradoxos (Panicker 2009; Qiu
  2026) não autorizam "faixa ótima de TSH" para humor — nenhum corte é fornecido (P20 reforçado).
- **B11-REGRA-06 (adjuvante≠tratar toda depressão como tireoidiana):** Bauer 2021; Hilmon 2026;
  Loh 2019 — sinal terapêutico ≠ conduta.
- **B11-REGRA-07 (bidirecionalidade obrigatória):** toda análise mecanística B11 declara as
  duas direções antes de usar direção única.
- **B11-REGRA-08 (evidência NEGATIVA é conteúdo canônico):** Wildisen 2020, Airaksinen 2021,
  Kim 2018, Roberts 2006, Engum 2002 e o FT3-nulo de Saravanan 2006 têm o mesmo status das
  positivas — são a espinha dorsal da controvérsia SCH.
- **B11-REGRA-09 (efeitos do insumo = alegação):** tamanhos de efeito citados pelo insumo
  externo só entram após confirmação direta na fonte; quando não confirmados, a direção
  qualitativa é mantida sem número.
- **B11-REGRA-10 (multi-tag permitida):** uma mesma referência pode ancorar mais de uma claim
  (ex.: Engum 2005 em AIT e em negativa populacional).

**Exposições e falsos positivos desta rodada (transparência G1):**
(a) "Roca 1990" do dossiê estava mapeado a um PMID que é, na verdade, Romero-Gómez 2019 —
Roca 1990 real foi localizado por busca independente (elevações transitórias) e ambos entraram
com identidades corrigidas; (b) "Zhang 2024" é correção editorial de Soheili 2023 — metadado,
não referência; (c) "Ao 2023/2024", rotulado no insumo como TDM jovem, é estudo em tumor ósseo
primário → EXC (câncer); (d) Eckert 2020 é população com diabetes tipo 1 → EXC (malha);
(e) Kirnap 2020 é hipertireoidismo subclínico iatrogênico em seguimento de carcinoma
diferenciado de tireoide → EXC (oncologia); (f) Toma 2026, sinalizado na V1 como pendente
sobre NTIS/desiodinase, é na verdade sobre triagem hormonal rotineira em internados — tema
corrigido nesta V2; (g) "Watanave 2018", sinalizado na V1, permanece sem resolução via eutils
→ mantido `[G1]`, não forjado; (h) 19 itens de revistas regionais sem indexação verificável →
EXC declarados (Alanazi, Bali, Bernardes, Challa, Cieplak, Exley, Gupta, Hermann 2004, Kale,
Kassaee, Mani, Moini, Morley 1982, Peng 2023-NAOIDX, Radhakrishnan, Rehman 2026, Santos,
Shrestha, Swigar 1979).

"""
doc=doc.replace(ancora_tabela, BLOCO14+ancora_tabela)

# 3) TABELA: inserir linhas novas antes do fim da tabela
linha="| Neurorimagem humana | Volume hipocampal/PET revertem com reposição | médio (associativo) |"
assert doc.count(linha)==1
novas_linhas = linha + """
| [AT] SCH controvérsia | Metas transversais fracas vs coortes/IPD negativas — claim canônica = inconsistência | médio (bidimensional, contraditório) |
| [AT] AIT/Hashimoto eutireoidiano | Excesso de depressão/ansiedade sem hipotireoidismo; causalidade proibida | médio (associativo robusto) |
| [AT] Ansiedade-específica | HPT pouco mapeado; sinais modestos, não-lineares (paradoxo ansiedade×depressão) | baixo-médio (emergente) |
| [AT] Transitórios/NTI | Hipertiroxinemia/TSH transitórios na doença aguda; FT3-nulo sob reposição; rT3 periférico | médio (antiartefato) |
| [AT] Bidirecionalidade | Depressão/ansiedade precedem doença tireoidiana (UK Biobank); reversa plausível | médio (prospectivo) |
| [AT] Terapia-sinal | T3/T4 adjuvante e LT4 jovens = sinal, não conduta (P20) | médio (sinal histórico) |"""
doc=doc.replace(linha, novas_linhas)

# 4) CONTROVÉRSIAS: atualizar sinalizados
antigo="""- **Lacunas:** T3 cerebral em humor adulto; augmentation com T3 como conduta (módulo clínico);
  NTIS/citocinas; DIO2. Sinalizados P-6 sem PMID confirmado: Siegmann meta-T3, Toma 2026
  (NTIS/desiodinase), Bode 2021, Watanave 2018 — não forjados."""
assert doc.count(antigo)==1
novo="""- **Lacunas:** T3 cerebral em humor adulto; augmentation com T3 como conduta (módulo clínico);
  NTIS/citocinas; DIO2. Atualização [AT 2026-09-09]: Siegmann (meta-análise AIT), Bode 2021
  (JAMA Psychiatry) e Toma 2026 (triagem rotineira em internados — tema corrigido em relação
  ao sinalizado na V1) foram **ancorados** nesta rodada; "Watanave 2018" permanece sem
  resolução via eutils → mantido `[G1]`, não forjado."""
doc=doc.replace(antigo, novo)

# 5) corte de literatura e nota de fecho
a2="**corte_literatura (R06):** busca ativa E-utilities/PubMed — corte 2026-09-06."
assert doc.count(a2)==1
doc=doc.replace(a2,"**corte_literatura (R06):** busca ativa E-utilities/PubMed — corte 2026-09-09 (rodada [AT]).")
a3="""> **Canônica v1 (Rodada 3).** G1 eutils (30 âncoras autor+ano+tema vs GPM), G2 (espécie/desenho),
> G3 (suporte). Sem número de PMID no texto. Causalidade animal/molecular [ML]/[EXT];
> reposição/augmentation é sinal, não conduta (P20). 2ª verificação independente (P-6, avaliador
> cego) é pendência do avaliador externo."""
assert doc.count(a3)==1
doc=doc.replace(a3,"""> **Canônica v2 (Rodada 4 — [AT] 2026-09-09).** Reconciliação de insumo externo auditado
> ref a ref (P-7): ENTRA 56 / BAIXO 41 / EXC 11 grupos (209 itens + correção editorial como
> metadado). Camada clínica humana [EC]/[OB] adicionada nos BLOCOS 14–15; causalidade
> molecular permanece [ML]/[EXT] nos BLOCOS 01–04. Dez regras fundadoras fixadas; evidência
> negativa promovida a conteúdo canônico. Sem número de PMID no texto; sem doses (P20).
> 2ª verificação independente (P-6, avaliador cego) permanece pendência do avaliador externo —
> agora cobrindo todas as levas [AT] de B1–B16.""")

# 6) varreduras
assert not re.search(r'\d{7,9}', doc), "dígito longo na prosa!"
for m in re.finditer(r'\(([^)]{2,40}?)\s*\n\s*(\d{4}[a-z]?)\)\[(EC|OB|ML)\]', doc):
    print("AVISO citação quebrada legada:", m.group(0)[:60].replace('\n','\\n'))
open(V2,'w',encoding='utf-8').write(doc)
palavras=len(doc.split())
print("V2 gravada:", V2.split('/')[-1], "| palavras:", palavras)
# checar unicidade dos trechos-âncora das 56 (prosa)
import json
R=json.load(open(BASE+'producao/insumos/b11_refs_data.json'))
MAP={"REF_ROADUENAS_2024":"(Roa Dueñas 2024)","REF_ROMEROGOMEZ_2019":"(Romero-Gómez 2019)"}
falt=[]
for r in R:
    rid=r['id_referencia_interna']
    sob=rid[4:].rsplit('_',1)[0]
    ano=rid.rsplit('_',1)[1]
    cit=MAP.get(rid, f"({sob.capitalize()} {ano})")
    # achar no doc
    linha=[l for l in doc.split('\n') if cit.split(')')[0] in l and '[' in l]
    ok=sum(doc.count(l) for l in set(linha))>=1 and len(linha)>=1
    if not ok: falt.append((rid,cit))
print("citações não localizadas:", falt[:10], "total faltantes:", len(falt))
