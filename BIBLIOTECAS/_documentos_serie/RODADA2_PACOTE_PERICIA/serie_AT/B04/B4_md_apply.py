# -*- coding: utf-8 -*-
import json, re, unicodedata
F='/home/user/BIBLIOTECAS/B04_Monoaminas/B4 DEFICIÊNCIA DE MONOAMINAS V2 CANONICA.md'
doc=open(F).read()
AT=json.load(open('/home/user/BIBLIOTECAS/B04_Monoaminas/producao/insumos/matriz_b4_at_final.json'))
assert len(AT)==94
LAB={p['grupo']:[] for p in AT}
for r in AT: LAB[r['grupo']].append((r['label'],r['tag']))
def listra(grupo, tags=True):
    return '*'+' | '.join(f"{l}[{t}]" for l,t in LAB[grupo])+'*'
def listra_up(itens):
    return '*'+' | '.join(f"{unicodedata.normalize('NFKD',l).encode('ascii','ignore').decode().upper()}[{t}]" for l,t in itens)+'*'

# ---------- 1) cabeçalho ----------
old_hdr=("# B4 DEFICIÊNCIA DE MONOAMINAS V1 CANÔNICA\n## Biblioteca de Conhecimento Canônica (Mecanismo B4 — Ansiedade e Depressão)\n\n"
"**ID canônico:** mecanismo_B4_deficiencias_monoaminas · **Prompt v4.2** · Corte: 2026-09-05.\n"
"**artefato_rotulo:** CANÔNICA v1 · G1 (36/36 PMIDs eutils) + G2 (espécie/desenho/elegibilidade) + G3 (suporte por vínculo; abstracts dos achados de alto risco lidos).")
new_hdr=("# B4 DEFICIÊNCIA DE MONOAMINAS V2 CANÔNICA\n## Biblioteca de Conhecimento Canônica (Mecanismo B4 — Ansiedade e Depressão)\n\n"
"**ID canônico:** mecanismo_B4_deficiencias_monoaminas · **Prompt v4.2** · Corte: 2026-09-05.\n"
"**artefato_rotulo:** CANÔNICA v2 · G1/G2/G3 (37 refs) + rodada **[AT] 2026-09-08** (P-7): insumo externo (177 itens) auditado ref a ref — **94 incorporadas** (+1 EXC tardia pós-abstract: Evans 2024, modelo de Alzheimer), 0 falsos positivos, 2 correções de autoria (Goddard 2010; Parsey 2006), 13 EXC escopo, 57 baixo incremento, 12 não-resolvidos → **37→131 refs**; P-6 2ª verificação cega PENDENTE.")
assert doc.count(old_hdr)==1; doc=doc.replace(old_hdr,new_hdr)

# ---------- 2) §1.4 HIST ----------
hist_txt=f"""
**Consolidação histórica e revisitação contemporânea [AT 2026-09-08].** A arqueologia da hipótese
ganhou mapa verificado: lá na origem, a formulação das catecolaminas foi reafirmada pelo próprio
Schildkraut (1967)[OB]; as reconstituições de Hirschfeld (2000)[OB] e de Charney (1998)[OB]
mostram que a Hipótese da Monoamina nunca foi um único enunciado, mas uma família de versões —
da \"lesão bioquímica\" (Leonard 2000)[OB] à versão **modulatória** de Heninger (1996)[OB], que já
nos anos 1990 rebaixava a monoamina de \"causa\" para **permissiva contextual**. Nemeroff (2009)[OB]
representa a defesa contemporânea do eixo (\"a serotonina ainda importa\"), enquanto a revisitação
crítica desmontou o elo de partida: Baumeister (2003)[OB] mostrou que a \"depressão induzida por
reserpina\" — pedra inaugural da hipótese — era **mito historiográfico**, e a revisão sistemática
de Strawbridge (2023)[MA] confirmou que a reserpina **não** deprime de forma consistente (o efeito
foi confundido com sedação e com o grupo de referência em hipertensos). As sínteses equilibradas
do século XXI — Cowen (2015)[OB] (\"o que a serotonina tem a ver com depressão?\") e Albert & Blier
(2023)[OB] — convergem no ponto maduro: **a serotonina importa como neuromodulador que regula
ganho/plasticidade, não como tanque vazio**; e nenhuma revisitação honesta pode apagar o dado
farmacoepidemiológico de que a farmacologia monoaminérgica ajuda um subgrupo real.
**Regra de leitura B4.R01:** \"depressão = deficiência de monoamina\" **não entra na B4 como fato**;
a disputa está ativa (§ controvérsias) e a B4 registra os dois lados sem tomar partido.

{listra('HIST')}
"""
anc="### 1.5 Núcleos de origem"
assert doc.count(anc)==1; doc=doc.replace(anc, hist_txt.strip()+"\n\n"+anc)

# ---------- 3) §2.1 5-HT ----------
ht_txt=f"""
**Receptores 5-HT — leitura estratificada [AT 2026-09-08].** A camada receptorial é a mais
densamente mapeada: a função do 5-HT1A na TDM tem revisão dedicada (Savitz 2009)[OB] e a
meta-análise de imagem molecular (Wang 2016)[MA] mostra alterações de disponibilidade do 5-HT1A
em depressão — mas **dissociadas por camada**: alteração de receptor ≠ alteração de SERT ≠
alteração de síntese ≠ alteração de liberação ≠ alteração de circuito (Regra B4.R02). Em PET
humano, os dados apontam para alterações de disponibilidade do 5-HT1A em depressão (Parsey
2006)[EC] e redução em pacientes nunca medicados (Hirvonen 2008)[EC]; a amarração post-mortem
entre 5-HT1A, 5-HT2A e SERT no cérebro humano reforça que os compartimentos variam de forma
independente (Steinberg 2019)[EC]. Na ansiedade, o 5-HT1A tem revisão própria (Akimova 2009)[OB]
e o achado PET de **maior** síntese e recaptação no transtorno de ansiedade social (Frick 2015)[EC]
lembra que a direção pode ser **oposta** à do modelo de déficit. As diferenças sexuais no
metabolismo triptofano/5-HT em transtornos de ansiedade são eixo documentado (Songtachalert
2018)[OB]. A frente mecanística animal — knockout de 5-HT1A com fenótipo ansioso e resposta
antidepressivo-símile (Heisler 1998)[ML], deficiência cerebral de 5-HT com agressão exacerbada e
ansiedade reduzida (Mosienko 2012)[ML], ausência de autorreceptores 5-HT1B com efeito
comportamental bidirecional (Nautiyal 2016)[ML] e complexos isoreceptoriais 5-HT1A–5-HT2A com
alostera antagonista (Borroto-Escuela 2017)[ML] — é `[APENAS PRÉ-CLÍNICO]`/`[EXTRAPOLADO:
animal→humano]`: define plausibilidade, não prova humana. As sínteses de receptores em
depressão/ansiedade (Popova 2013; Albert 2014; Garcia-Garcia 2014; Nautiyal 2017; Żmudzka 2018;
Fakhoury 2016; Pourhamzeh 2022; Villas-Boas 2021; Borroto-Escuela 2021)[OB] consolidam: não há
um único \"receptor do humor\" — há subtipos com sinais opostos por circuito.

{listra('5HT')}
"""
anc="### 2.2 Heterodímeros"
assert doc.count(anc)==1; doc=doc.replace(anc, ht_txt.strip()+"\n\n"+anc)

# ---------- 4) §2.3 DEPL ----------
depl_txt=f"""
**A arqueologia completa da depleção [AT 2026-09-08].** O paradigma ganhou genealogia verificada:
as revisões de Bell (2001)[MA] e Moore (2000)[OB] estabeleceram o desenho e seus limites
fisiológicos; a meta-reanálise de Booij (2002)[MA] cristalizou o achado-chave — a resposta à
depleção **depende da vulnerabilidade** (remetidos medicados recaem; NUNCA medicados e sadios
não). E há o polo negativo esquecido: em **deprimidos não medicados**, a depleção de monoaminas
não piorou o humor (Berman 2002)[EC-NEG]; em sadios, nem a depleção de triptofano (Salomon
1997)[EC-NEG] nem a de tirosina (McLean 2004)[EC-NEG] produziram efeito comportamental; a
depleção simultânea de catecolaminas+5-HT teve efeitos seletivos e fracos (Hughes 2004)[EC]; a
depleção de 5-HT não derrubou a regulação emocional de sadios (Bîlc 2023)[EC-NEG]; e na ansiedade
a revisão sistemática relata a mesma assimetria — efeito aparece com vulnerabilidade prévia, não
de novo (Schopman 2021)[MA-NEG]. No polo funcional, a depleção **reverteu a melhora** mantida
por ISRS — inclusive em ansiedade social remetida (Argyropoulos 2004)[EC] —, o que sustenta o
modelo **permissivo/gating**: a monoamina é condição de manutenção em sistema sensibilizado, não
causa linear. As sínteses de Neumeister (2003)[OB] e Booij (2003)[OB] e a revisitação ansiedade-
centrada de Kahn (1988)[OB] fecham o quadro. **Regra B4.R03:** depleção aguda é **sonda
experimental de gating contextual** (janela de horas), não modelo causal de depressão espontânea —
e não mensura \"níveis\" do paciente clínico.

{listra('DEPL')}
"""
anc="### 2.4 Tema: a monoamina como código temporal"
assert doc.count(anc)==1; doc=doc.replace(anc, depl_txt.strip()+"\n\n"+anc)

# ---------- 5) §3.1 DA ----------
da_txt=f"""
**Dopamina, recompensa e anedonia — consolidação [AT 2026-09-08].** A leva humana elimina a versão
ingênua: em TDM, a neurotransmissão dopaminérgica D2/3 estriatal aparece **aumentada** em
subgrupo — não \"baixa\" (Peciña 2017)[EC] —, e a disponibilidade estriatal de DA se associa à
anedonia de maneira dependente de contexto (Phillips 2023)[EC]; em depressão geriátrica, o
transportador DAT no núcleo accumbens aparece **reduzido** (Moriya 2020)[EC] — heterogeneidade,
não déficit uniforme. A leitura conceitual madura é a do **esforço**: a DA mesolímbica regula
motivação e alocação de esforço, não o prazer em si (Salamone 2016)[OB], e a anedonia é
reconfigurada como falha de **aprendizado/antecipação de recompensa** mais do que \"prazer
ausente\" (Treadway 2011)[OB]. Os arcabouços de circuito — do circuito mesolímbico de recompensa
(Nestler 2006)[OB] à neuroquímica do NAc (Shirayama 2006)[OB], à desregulação comprometida com
motivação (Belujon 2017)[OB], à hi
pótese da desregulação dopaminérgica (Szczypinski 2018)[OB], aos quadros circuito-baseados
(Knowland 2018)[OB], à anedonia como fator central (Wang 2021)[OB] e ao NAc na patogênese
(Jiang 2023)[OB] — tratam a anedonia como **função de circuito**, não como \"pouca dopamina\".
A prova de suficiência pré-clínica de que elevar D2 no NAc adulto aumenta comportamento dirigido
a recompensa (Trifilieff 2013)[ML] permanece `[APENAS PRÉ-CLÍNICO]`. **Regra B4.R04:** anedonia
≠ \"dopamina baixa\"; B4 fala de resposta fásica, esforço e aprendizado de recompensa — com
heterogeneidade PET já demonstrada.

{listra('DA')}
"""
anc="### 3.2 Subpopulações e transcriptômica"
assert doc.count(anc)==1; doc=doc.replace(anc, da_txt.strip()+"\n\n"+anc)

# ---------- 6) novo §4.1 LC ----------
lc_txt=f"""### 4.1 O sistema locus coeruleus–noradrenalina em profundidade [AT 2026-09-08]

O LC–NA é o sistema monoaminérgico cuja arquitetura melhor exemplifica **sistema dinâmico e
heterogêneo, não estoque**: a revisão de referência de Berridge & Waterhouse (2003)[OB] definiu a
modulação estado-dependente (tônico vs fásico); Maletic (2017)[OB] mapeou os receptores
α-adrenérgicos na fisiopatologia clínica e Goddard (2010)[OB] consolidou o papel na ansiedade.
A convergência regulatória do LC como **resposta adaptativa ao estresse** (Valentino 2008)[OB], os
sistemas noradrenérgicos do tronco em estresse/ansiedade/depressão (Itoi 2010)[OB], a modulação
cognitiva (Borodovitsyna 2017)[OB] e a liberação volume-transmissão com lógica espaço-temporal
(Atzori 2016)[OB] fecham o quadro de base. As frentes atuais adicionam camadas: dimorfismo sexual
do eixo LC–NA (Bangasser 2016)[OB] e na regulação pré-frontal (Scroger 2025)[ML]; receptores β
como mediadores de depressão **e** resiliência (Zhang 2022)[OB]; modulação pré-frontal da
ansiedade (Bouras 2023)[OB]; comunicação cérebro-corpo (Fernandes 2025)[OB]; anatomia/fisiologia
integradas em transtornos de estresse (Reyes 2025)[OB]; e a releitura praticamente anual do sistema
em psicopatologia (Slavova 2024; Mir 2025; Korukonda 2026)[OB/MA], incluindo o par LC–núcleo do
trato solitário (Dos-Santos 2026)[OB]. A frente circuital animal — CRH engajando o LC no medo de
estresse (McCall 2015)[ML], projeções LC→amígdala basolateral promovendo ansiedade (McCall
2017)[ML], modulação noradrenérgica do condicionamento/extinção de medo (Giustino 2018)[OB/ML] e
do aumento de excitabilidade amígdala sob estresse (Giustino 2020)[ML], alteração persistente do
LC após estresse agudo (Borodovitsyna 2018)[ML], perda de autoinibição sob estresse crônico
(Toyoda 2025)[ML], efeitos bidirecionais de entradas NA na BLA (Soares 2025)[ML][preprint
indexado], projeção LC→septo dorsolateral modulando fenótipo depressivo-símile (Zhang 2024)[ML]
e co-liberação NA/galanina com resiliência em escalas temporais distintas (Tillage 2021)[ML] — é
`[APENAS PRÉ-CLÍNICO]`/`[EXTRAPOLADO: animal→humano]`. **Regra B4.R05:** falar de \"noradrenalina
baixa\" é anacrônico; a B4 fala de **modo de disparo, receptor e circuito** do LC–NA.

{listra('LC')}

"""
anc="## BLOCO_05 — BIOMARCADORES"
assert doc.count(anc)==1; doc=doc.replace(anc, lc_txt+"---\n\n"+anc, 1)

# ---------- 7) BLOCO_08 INF+B2X ----------
inf_txt=f"""### 8.x Interfaces cruzadas verificadas: inflamação (B1) e eixo HPA (B2) [AT 2026-09-08]

A ponte B1↔B4 é hoje a melhor documentada das fronteiras: inflamação **reduz** a transmissão
dopaminérgica funcional e prejudica motivação/atividade motora (Felger 2017)[OB]; em humana, a
repetição de levodopa sustenta efeitos no circuito de recompensa em quadros inflamatórios
(Bekhbat 2025)[EC]; a integração formal das hipóteses monoaminérgica e citocínica passa pelo
percurso IDO/quinurenina e pelo papel da histamina (Hersey 2022)[OB]; e a anedonia inflamatória
ganhou revisão dedicada com implicações farmacológicas (Lucido 2021)[OB]. A ponte B2↔B4 é mais
antiga e fina: precursores serotoninérgicos modulam o feedback glicocorticoide do eixo HPA na
depressão (Maes 1995)[EC] — primeiro desenho humano de acoplamento 5-HT↔HPA. Nenhuma dessas
interfaces autoriza biomarcador clínico rotineiro (ver § controvérsias); são camadas de mecanismo.

{listra('INF')+listra('B2X')}

"""
anc="## BLOCO_09 — IMPACTO SOBRE NEUROPLASTICIDADE (elo B3)"
assert doc.count(anc)==1; doc=doc.replace(anc, inf_txt+"---\n\n"+anc, 1)

# ---------- 8) MOD (falência do modelo) ----------
mod_txt=f"""
**Os modelos sucessores, verificados [AT 2026-09-08].** A literatura de reformulação foi mapeada:
a trajetória \"da serotonina à neuroplasticidade\" (Liu 2017)[OB], a síntese \"para além da hipótese
monoaminérgica\" (Boku 2018)[OB], a moldura de **continuum monoamina–glutamato** (Carmellini
2026)[OB] e a proposta de comunicação clínica pós-déficit centrada em neuroplasticidade (Page
2024)[OB] convergem com a linha de mecanismos pós-ISRS/IRSN (Dale 2015)[EC]: o déficit foi
substituído por **modelos em camadas** (receptor → rede → plasticidade → contexto). **Regra
B4.R06:** eficácia de ISRS ≠ prova do déficit (inferência reversa); a B4 registra o mecanismo
como **contestado e reformulado**, nunca como fato estabelecido.

{listra('MOD')}
"""
anc="## BLOCO_07/08 (PROFUNDIDADE) — GÊNESE, EVIDÊNCIA E OS DOIS LADOS"
assert doc.count(anc)==1; doc=doc.replace(anc, mod_txt.strip()+"\n\n"+anc, 1)

# ---------- 9) nota AT antes da TABELA ----------
nota="""
---

### Atualização [AT] 2026-09-08 — insumo externo (P-7), 94 refs incorporadas (37→131)

Auditoria ref a ref (G1 eutils semântico; relatório em `producao/insumos/RELATORIO_AUDITORIA_MATRIZ_B4.md`):
177 itens de insumo (anexo 172 DOIs + consolidação + briefing); 161 resolvidos; **0 falsos positivos**;
**2 correções de autoria do insumo** (\"Martinez 2010\"→Marzo? não — confirmado: **Goddard 2010**; \"Ogden 2006\"→**Parsey 2006**);
94 incorporadas aos blocos HIST/5-HT/DEPL/DA/LC/INF/MOD; **1 EXC tardia pós-abstract** (Evans 2024 — modelo 5XFAD de
Alzheimer, fora de escopo permanente); 13 EXC escopo (4 TEPT, Parkinson, Alzheimer, dor×3, anorexia, APP/ascorbato,
fitoquímicos sem sonda clara, japonês clínico local); 57 baixo incremento (BAIXO, reavaliáveis); 12 não-resolvidos
(HOLD Liu 2023 medRxiv; Alawie; Cosci; Fassler; Hasler; Isingrini bioRxiv; Kovalzon; Li J; Nakamura; Neumeister 2025
=republicação; O'Leary; Kayabaşı `[G1]`). Soares 2025 carrega pubtype **Preprint** indexado — registrado. P-6 pendente.

"""
anc="## TABELA DE EVIDÊNCIAS"
assert doc.count(anc)==1; doc=doc.replace(anc, nota.strip()+"\n\n"+anc, 1)

# ---------- 10) TABELA +3 linhas ----------
old_row="| Genética | 5-HTTLPR/MAOA não replicam em meta grande (Risch/Culverhouse) | alto (negação frágil) |"
new_rows=(old_row+"\n"
"| Depleção (meta+EC) | Recaída só em remetidos/medicados (Booij MA; Bell MA); NEG em sadios e em não-medicados (Berman; Salomon; McLean); ansiedade idem (Schopman MA) | alto (humano experimental) |\n"
"| PET 5-HT/DA | 5-HT1A alterado em TDM (Wang MA; Parsey; Hirvonen; Steinberg); DA estriatal heterogênea — aumentada em subgrupo (Peciña), DAT reduzido na geriátrica (Moriya) | médio (humano) |\n"
"| Circuito LC–NA | tônico/fásico estado-dependente (Berridge); CRH→LC→BLA no medo/ansiedade (McCall; Giustino); resiliência β/NA-galanina (Zhang; Tillage) — tudo [ML/EXT] | médio (animal→humano) |\n"
"| Interface B1×B4 | inflamação ↓ DA funcional e motivação (Felger; Lucido; Hersey); levodopa sustentando recompensa (Bekhbat) | médio |")
assert doc.count(old_row)==1; doc=doc.replace(old_row,new_rows)

# ---------- 11) CONTROVÉRSIAS: regras de leitura ----------
regras="""
### Regras de leitura B4 (fixadas na rodada [AT] 2026-09-08)

- **B4.R01** — \"Depressão/ansiedade = deficiência de monoamina\" **não é fato na B4**: hipótese histórica em
  disputa ativa (Moncrieff 2022 × Jauhar 2023, já vigentes); a B4 registra os dois lados.
- **B4.R02** — Estratificar sempre: 5-HT (síntese) ≠ receptor ≠ SERT ≠ liberação ≠ circuito; evidência vale por
  camada, não por \"serotonina\" genérica (Wang 2016; Steinberg 2019).
- **B4.R03** — Depleção aguda = sonda de **gating contextual** (recaída em vulneráveis/medicados); os negativos
  em sadios e não-medicados (Berman; Salomon; McLean; Schopman) têm o mesmo peso dos positivos.
- **B4.R04** — Anedonia ≠ \"pouca dopamina\": heterogeneidade PET (Peciña ↑; Moriya ↓ geriátrica); a variável de
  trabalho é esforço/aprendizado de recompensa (Salamone; Treadway).
- **B4.R05** — LC–NA: sistema de **modo/receptor/circuito** (tônico vs fásico), não \"tanque\"; leitura circuital
  (Berridge; Reyes; Slavova).
- **B4.R06** — Eficácia de ISRS ≠ prova causal do déficit (inferência reversa); farmacologia como sonda
  experimental, nunca como posologia (P20).
- **B4.R07** — Toda evidência `[ML]` da leva (knockouts 5-HT; opto/circuito LC; D2-NAc) permanece
  `[APENAS PRÉ-CLÍNICO]`/`[EXTRAPOLADO: animal→humano]` (R04).
- **B4.R08** — A leva [AT] (94 refs) aguarda P-6 (2ª verificação independente cega); nenhum claim novo de ALTO
  RISCO foi promovido sem esse portão.
"""
anc="## ELEMENTOS MOLECULARES CRÍTICOS (UniProt/HGNC)"
assert doc.count(anc)==1; doc=doc.replace(anc, regras.strip()+"\n\n---\n\n"+anc, 1)

# ---------- 12) APÊNDICE: +4 linhas ----------
ap=("> Bloco [AT] 2026-09-08 — insumo externo auditado (94 refs; relatório em producao/insumos/):\n"
    +listra_up(LAB['HIST']+LAB['MOD'])+"\n"
    +listra_up(LAB['5HT'])+"\n"
    +listra_up(LAB['DEPL']+LAB['DA'])+"\n"
    +listra_up(LAB['LC']+LAB['INF']+LAB['B2X']))
anc="## METADADOS CANÔNICOS (Contrato de Geração — P12 / R06 / P17)"
assert doc.count(anc)==1; doc=doc.replace(anc, "\n"+ap+"\n\n---\n\n"+anc, 1)

# ---------- asserts finais ----------
for l,t in [ (r['label'],r['tag']) for r in AT ]:
    up=unicodedata.normalize('NFKD',l).encode('ascii','ignore').decode().upper()
    assert f"{up}[{t}]" in doc, l
    assert f"{l}[{t}]" in doc, 'body '+l
assert len(re.findall(r'\b\d{7,9}\b',doc))==0, 'PMID no texto corrido!'
assert doc.count('[AT]')>=1
open(F,'w').write(doc)
import re as _re
print('palavras:', len(_re.findall(r'\S+',doc)))
print('listras [AT] ok; refs novas no corpus:', sum(doc.count(unicodedata.normalize('NFKD',r['label']).encode('ascii','ignore').decode().upper()+'['+r['tag']+']') for r in AT))
print('MD APLICADO OK')
