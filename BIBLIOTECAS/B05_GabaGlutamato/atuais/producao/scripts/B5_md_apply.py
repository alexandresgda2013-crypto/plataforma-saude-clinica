# -*- coding: utf-8 -*-
import json, re, unicodedata
F='/home/user/BIBLIOTECAS/B05_GabaGlutamato/B5 GABA GLUTAMATO V2 CANONICA.md'
doc=open(F).read()
AT=json.load(open('/home/user/BIBLIOTECAS/B05_GabaGlutamato/producao/insumos/matriz_b5_at_final.json'))
assert len(AT)==116
LAB={}
for r in AT: LAB.setdefault(r['grupo'],[]).append((r['label'],r['tag']))
def listra(g): return '*'+' | '.join(f"{l}[{t}]" for l,t in LAB[g])+'*'
def listra_up(itens): return '*'+' | '.join(f"{unicodedata.normalize('NFKD',l).encode('ascii','ignore').decode().upper()}[{t}]" for l,t in itens)+'*'

# 1) cabeçalho
old_hdr=("# B5 GABA GLUTAMATO V1 CANÔNICA\n## Biblioteca de Conhecimento Canônica (Mecanismo B5 — Ansiedade e Depressão)\n\n"
"**ID canônico:** mecanismo_B5_gaba_glutamato · **Prompt v4.2** · Corte: 2026-09-05.\n"
"**artefato_rotulo:** CANÔNICA v1 · G1 (41/41 PMIDs eutils) + G2 (espécie/desenho/elegibilidade) + G3 (suporte por vínculo; abstracts dos achados de alto risco lidos).")
new_hdr=("# B5 GABA GLUTAMATO V2 CANÔNICA\n## Biblioteca de Conhecimento Canônica (Mecanismo B5 — Ansiedade e Depressão)\n\n"
"**ID canônico:** mecanismo_B5_gaba_glutamato · **Prompt v4.2** · Corte: 2026-09-05.\n"
"**artefato_rotulo:** CANÔNICA v2 · G1/G2/G3 (44 refs) + rodada **[AT] 2026-09-08** (P-7): insumos externos (consolidação + anexo 190 + briefing) auditados ref a ref — **116 incorporadas**, 1 falso positivo exposto (Prosowski 2024, DOI trocado → `[G1]`), 3 correções de autoria (Carver 2013; Cavalleri 2018; Hollestein 2023), 14 EXC escopo, 53 baixo incremento, 2 não-resolvidos → **44→160 refs**; P-6 2ª verificação cega PENDENTE.")
assert doc.count(old_hdr)==1; doc=doc.replace(old_hdr,new_hdr)

# 2) MRS
mrs_txt=f"""
**Evidência MRS humana — camada medida, com disciplina de níveis [AT 2026-09-08].** A base humana
direta é metodologicamente forte e cientificamente **inconclusiva por desenho**: a meta-análise
de Godfrey (2018)[MA] encontrou GABA significativamente **reduzido** na TDM mas **nenhuma
diferença global de glutamato** — o primeiro grande negativo explícito do campo; e Kantrowitz
(2021)[EC] encontrou, em TDM não medicada, **Glx e glutamato elevados com GABA reduzido** no
vmPFC/ACC, com associação entre Glx e gravidade. As duas afirmações convivem: modelam
heterogeneidade (região, estado, medicação), não um veredito único (Regra B5.R01). A trava
metodológica é dupla: Steel (2020)[EC] mostrou correlação Glx×GABA+ que **colapsa** ao controlar
densidade neuronal/metabolismo, e Rideaux (2021)[EC]/Rideaux (2022)[EC] não encontraram essa
correlação em córtices visual e motor — logo, **GABA/Glx por MRS não é proxy do E/I
eletrofisiológico** (Regra B5.R02). A camada de doença adiciona: disfunção E/I em rede ampla na
TDM (Hu 2023)[EC]; alterações E/I do ACC dependentes de idade por MRS 7T (Yoshihara 2026)[EC];
modulação GABA/glutamato em RCT sham-controlado de iTBS (Steinholtz 2025)[EC]; efeitos do estresse
agudo em 7T (Houtepen 2017)[EC]; marcadores GABAérgicos pré-frontais sob modelo glicocorticoide
(Hu 2024)[ML]; e o ciclo glutamina–glutamato–GABA como eixo metabólico (Sarawagi 2021; Mamelak
2024; Lener 2017)[OB], com o elo translacional de ondas lentas/BDNF pós-cetamina (Duncan 2013)[EC].
**Regra B5.R02:** nenhuma frase da B5 pode saltar de \"concentração MRS\" para \"transmissão\" ou \"E/I
sináptico\" sem evidência do nível correspondente.

{listra('MRS')}
"""
anc="## BLOCO_02 (PROFUNDIDADE) — NEUROESTEROIDES EM GABA-A"
assert doc.count(anc)==1; doc=doc.replace(anc, mrs_txt.strip()+"\n\n"+anc, 1)

# 3) GABA
gaba_txt=f"""
**Fundamentos GABAérgicos e neuroesteroides — consolidação [AT 2026-09-08].** A camada molecular
do eixo inibitório fica completa: criticidade do GABA na TDM (Pehrson 2015)[OB]; a anatomia
quantitativa dos tipos de interneurônios na amígdala lateral/basal (Vereczki 2021)[ML, corrigida
do preprint]; a taxonomia que organiza tudo (Rudy 2011)[OB]; a diversidade funcional de
interneurônios SST (Riedemann 2019)[OB]; o papel da α5 na localização sináptica e função
(Magnin 2019)[ML]; inibição tônica e sua variância por tipo celular (Lee & Maguire 2014;
Bryson 2020)[ML]; descoplamento funcional de SST por GABA-B pré-sináptico e efeitos
perissomáticos vs dendríticos (Booker 2020; Booker 2013)[ML]; contribuições PV/SST às oscilações
gama hipocampais (Antonoudiou 2020)[ML]; e o crosstalk homeostático glutamato↔GABA-A
(Du 2023; Wen 2022)[ML]. No comportamento: silenciar SST-GABA induz déficits resgatados por
potenciação de α5-GABA-A (Fee 2021)[ML]; inibir interneurônios GABA do mPFC é **suficiente e
necessário** para resposta antidepressivo rápida em modelo (Fogaça 2021)[ML]; e os déficits
pré-frontais GABAérgicos estruturam a patofisiologia (Ghosal 2017)[OB] sendo revertidos pela
cetamina (Ghosal 2020)[ML]. Nos neuroesteroides como son da de alvo (P20): interações sinápticas
vs extrassinápticas em GABA-A (Carver 2013)[OB, autoria corrigida do insumo], alopregnanolona
sobre PV hipocampais (Lu 2023)[ML], moduladores GABA-A em psiquiatria (Thompson 2024)[OB] e
regulação pré-frontal de aferentes de longa distância (Yang 2021)[ML]. Tudo `[ML]` permanece
`[APENAS PRÉ-CLÍNICO]` (R04) — fundamento mecanístico, não evidência clínica.

{listra('GABA')}
"""
anc="## BLOCO_02 (DETALHE) — GLUTAMATO: NMDA, AMPA E A FRONTEIRA MECANÍSTICA"
assert doc.count(anc)==1; doc=doc.replace(anc, gaba_txt.strip()+"\n\n"+anc, 1)

# 4) NMDA
nmda_txt=f"""
**NMDAR e AMPAR em profundidade [AT 2026-09-08].** O núcleo glutamatérgico ganha camadas: GluN2B
como regulador de comportamento depressivo-símile e crítico para a ação rápida da cetamina
(Miller 2014)[ML]; a contra-prova de unidirecionalidade — potenciação alostérica positiva do
NMDAR **também** produz efeito antidepressivo-símile (Pothula 2021)[ML-CONT]; evidência
post-mortem humana de subunidades NR2A/NR2B e PSD-95 reduzidas no PFC na depressão (Feyissa
2009)[EC]; revisão translacional do receptor na neurobiologia e tratamento da TDM (Amidfar
2019; Comai 2024)[OB]; o elo inflamação→depressão abolido pela disrupção de GluN2A
(Francija 2019)[ML, ponte B1]; LTD NMDAR-dependente na habenula lateral ligada a comportamento
depressivo-símile (Kang 2020)[ML]; alterações de subunidades no desamparo aprendido
(Bieler 2021)[ML]; o modelo Flinders como leitura de subunidades pós-sinápticas (Treccani
2016)[ML]; e a contra-face da disputa — efeitos dependentes de **ativação** do NMDAR
(Zanos 2023)[ML-CONT]. Fundamentos estruturantes (todos `[ML]`/SUP, R04): LTP/LTD NMDAR
(Lüscher & Malenka 2012)[OB]; papéis diferenciais NR2A/NR2B (Massey 2004)[ML]; equilíbrio
GluN2A/GluN2B na plasticidade (Shipton 2014; Baez 2018)[OB/ML]; internalização atividade-
dependente de GluN2B com incorporação de GluN2A (Storey 2025)[ML, corrigida do preprint]; perda
de GluN2B em CA1/córtex com redução de densidade espinhosa (Brigman 2010)[ML]; papel de
GluN2C/2D no ACC (Chen 2021)[OB]; desacoblar DAPK1 de GluN2B com efeito antidepressivo-símile
(Li 2018)[ML]; modulação por estresse crônico e cetamina dos iGlu/mGlu (Elhussiny 2021)[ML]; e
GluN2A como alvo de desenho (Wang 2024)[OB]. **Regra B5.R03:** NMDAR não é mecanismo patológico
unidirecional — e falamos de **subunidade, localização e estado**, não de \"NMDA\" genérico.

{listra('NMDA')}
"""
amp_txt=f"""
**AMPAR — do mecanismo à evidência humana [AT 2026-09-08].** A frente AMPAR fecha com o elo mais
importante da leva: a dinâmica de AMPAR medida por **PET em pacientes com TRD** acompanha
gravidade, diferencia TRD de controles, muda após cetamina e se associa à resposta
(Nakajima 2026)[EC] — a primeira ponte AMPAR→humano direta. Do lado pré-clínico `[ML]`/R04:
AMPAR permeáveis a Ca²⁺ medeiam a resposta rápida à cetamina (Zaytseva 2023)[ML]; o envolvimento
de AMPAR e mecanismos **além do antagonismo NMDA** (Aleksandrova 2017)[OB]; a disfunção de
transmissão glutamatérgica focada em AMPAR na depressão (He 2023)[OB]; e a desregulação
bidirecional da sinalização AMPAR em modelos (Zhang 2020)[OB].

{listra('AMPA')}
"""
anc="## BLOCO_02 (DETALHE) — A QUÍMICA DA ANSIEDADE E DA EXTINÇÃO"
assert doc.count(anc)==1; doc=doc.replace(anc, nmda_txt.strip()+"\n\n"+amp_txt.strip()+"\n\n"+anc, 1)

# 5) KET
ket_txt=f"""
**Cetamina/esketamina — arquitetura mecanística sem narrativa única [AT 2026-09-08].** A síntese
integrada de Duman, Sanacora & Krystal (2019)[OB] e o enquadramento de \"nova era\" (Duman
2018)[OB] organizam o campo; Abdallah (2016)[OB] mapeia o caminho ao antidepressivo rápido.
A leva impõe **estratificação por camada** (Regra B5.R03): não basta \"bloqueio NMDA\" — há
metabólitos com ação independente (Zanos 2016, vigente), correntes tônicas de NMDAR como alvo
diferenciado entre cetamina/esketamina/dextrometorfano (Le 2026a)[OB], LTP e synaptic scaling
induzidos por cetamina/esketamina em revisão sistemática (Le 2026b)[MA], keto-enantiômeros em
perspectiva ((R)-ketamina, Scotton 2022)[OB], mecanismo clínico-translacional da esketamina
intranasal (van Hoogdalem 2026; Śledzikowska 2026)[OB], moduladores NMDA e GABAérgicos rápidos
no humor numa síntese (Serretti 2025)[OB], e a moldura \"todos os caminhos levam ao glutamato\"
(Freudenberg 2025)[OB]. Os mecanismos celulares aprofundam: ações de arketamina além do NMDAR
(Wei 2022)[OB]; vias convergentes de ação rápida (Zanos 2018; Hess 2022; Kang 2022)[OB];
neurotrofismo BDNF/TrkB no rápido e sustentado (Deyama 2020)[OB]; variações de BDNF no efeito
(Pardossi 2024)[OB]; e o estado da arte de Krystal (2024)[OB] sobre sinalização sináptica nova.
A crítica interna permanece visível: \"fronteira final ou fim deprimente?\" (Sial 2020)[OB-CONT] e
a hipótese de mediação **opioide** (Lu 2026)[OB-CONT]. Wohleb (2017)[OB] conecta cetamina e
escopolamina como rápidos não-monoaminérgicos; correlatos neurais de resposta em TRD (Yun 2024)[EC]
completam o elo humano. **Regra B5.R03 corolário:** \"antagonismo NMDAR\" é o evento farmacológico
inicial importante, não a explicação suficiente do efeito antidepressivo.

{listra('KET')}
"""
anc="## BLOCO_03 (PROFUNDIDADE) — MEDIADORES DO E/I, UM A UM"
assert doc.count(anc)==1; doc=doc.replace(anc, ket_txt.strip()+"\n\n"+anc, 1)

# 6) PLAST
plast_txt=f"""
**Plasticidade sináptica — o elo B5↔B3, estratificado [AT 2026-09-08].** O elo canônico continua
sendo B3 (dono da plasticidade), e a B5 registra **os gatilhos receptoriais**: sinalização TrkB
como lócus sináptico da ação rápida da cetamina (Lin 2021)[ML]; metaplasticidade como alvo de
ações sustentadas (Brown & Gould 2024)[OB]; efeitos metaplásticos de cetamina/MK-801 sobre
receptores (Piva 2021)[ML]; plasticidade estrutural em neurônios mesencefálicos humanos iPSC
(Cavalleri 2018)[ML/EC, autoria corrigida do insumo]; convergência cetamina×psicodélicos na
neuroplasticidade (Aleksandrova 2021)[OB]; NMDAR espontâneo como gatilho da cascata (Kavalali
2012)[OB]; ponte rápido→sustentado (Kim 2023)[OB]; ubiquitinação de GluA1 como requisito à
plasticidade/memória/flexibilidade (Guntupalli 2023)[ML, corrigida do preprint]; o código AMPAR
da plasticidade (Diering 2018)[OB]; regulação fosforilação-dependente de CP-AMPAR (Purkey
2020)[ML]; incorporação transitória de CP-AMPAR na LTD (Sanderson 2016)[ML]; e LTP/NMDAR como
referência disciplinar (Volianskis 2015)[OB]. **Regra B5.R05:** toda essa camada é
`[APENAS PRÉ-CLÍNICO]`/revisão conceitual — B5 não transforma LTP de fatia em prognóstico clínico;
a tradução humana passa por B3.

{listra('PLAST')}
"""
anc="## BLOCO_06 (RESUMO) — POR QUE O E/I SEPARA ANSIEDADE E DEPRESSÃO"
assert doc.count(anc)==1; doc=doc.replace(anc, plast_txt.strip()+"\n\n"+anc, 1)

# 7) ANX
anx_txt=f"""
**Ansiedade por circuito E/I [AT 2026-09-08].** O eixo GABA–ansiedade ganha base própria:
modulação GABAérgica perturbada nos transtornos de ansiedade (Nuss 2015)[OB]; implicações
GABAérgicas com foco em subunidades e inibição (Arora 2024)[OB]; GluN2D no BNST influenciando
comportamentos de ansiedade e depressão (Salimando 2020)[ML]; separação materna alterando PV
amigdalares e ansiedade desenvolvimental (Abraham 2023)[ML]; **desinibição de SST-GABA com efeito
ansioli tico-símile** — direção oposta à da depressão, prova de regionalidade (Fuchs 2017)[ML];
PV do hipocampo ventral durante ansiedade (Volitaki 2024)[ML]; a projeção BNST-SST→NAc-PV como
circuito ansiolítico (Xiao 2021)[ML]; ansiedade induzida por estresse via excitabilidade
amigdalar aumentada (Mitten 2024)[ML]; circuitos inibitórios da memória de medo e transtornos
relacionados (Singh 2023)[OB, medo transdiagnóstico — não TEPT-específico]; e reequilíbrio E/I
amigdalar com efeito ansiolítico via sinalização LXRβ (Yu 2020)[ML]. **Regra de leitura:**
ansiedade e depressão **compartilham o eixo mas não o sinal** — em vários circuitos, ansiedade
pede **mais** inibição funcional e depressão, recuperação da rede (Regra B5.R01).

{listra('ANX')}
"""
anc="## BLOCO_00 (FECHO) — A ASSINATURA DO B5"
assert doc.count(anc)==1; doc=doc.replace(anc, anx_txt.strip()+"\n\n"+anc, 1)

# 8) STR
str_txt=f"""
**Estresse como modulador sistêmico do E/I [AT 2026-09-08].** A prova mais elegante da leva: o
desequilíbrio E/I mensurável em circuito definido prediz **suscetibilidade** — aumento
coordenado de projeção glutamatérgica dmPFC→LHb com redução da projeção GABAérgica em animais
suscetíveis ao estresse, e sua restauração produzindo resiliência (Wu 2026)[ML]; PV amigdalares
comportando excitabilidade e resposta ao estresse crônico via inibição tônica GABA-B dirigida por
cainato (Ryazantseva 2025)[ML]; desequilíbrio E/I hipotalâmico (área pré-óptica mediana) sob
estresse crônico (Tao 2024)[ML]; alterações de PV em transtornos de humor estresse-relacionados
sistematizadas (Perlman 2021)[MA]; balanço E/I pré-frontal em estresse e transtornos emocionais
(Page 2019)[OB]; e a perturbação do ciclo glutamina–glutamato–GABA no estriado/hipocampo/cerebelo
no modelo murino de depressão (Xu 2020)[ML] — artigo original priorizado sobre a carta que o
comentava (regra de precedência documental). Tudo `[ML]`/revisão: R04 integral.

{listra('STR')}
"""
anc="## BLOCO_01 (PROFUNDIDADE) — FASES TEMPORAIS"
assert doc.count(anc)==1; doc=doc.replace(anc, str_txt.strip()+"\n\n"+anc, 1)

# 9) IFACE
iface_txt=f"""### Interfaces verificadas da B5 com a série (B1, B2, B4, B7) [AT 2026-09-08]

- **B5×B2 (estresse/HPA):** neurônios **glutamatérgicos** (não GABAérgicos) do prosencéfalo
  medeiam efeitos ansiogênicos do CRHR1 (Hartmann 2017)[ML] — desce o estresse ao nível de tipo
  celular.
- **B5×B1 (inflamação):** LPS reduz marcadores GABAérgicos e BDNF (Rezaei 2024)[ML]; inflamação
  neonatal com TGF-β1 persistentemente rebaixada diminui GABA-A em circuitos do medo
  (Zhong 2022)[ML] — ponte neurodesenvolvimento-inflamatório (R04).
- **Nó de circuito:** co-liberação GABA/glutamato controlando a saída habenular e modificada pelo
  estado de humor (Shabel 2014)[ML].
- **B5.03 transporte:** influência do transporte de glutamato/GABA sobre o balanço E/I
  (Sears 2021)[OB].
- **B5×B4:** serotonina e glutamato na ação rápida (Pham 2019)[OB] — ponte às monoaminas.
- **B5×B7:** bactérias produtoras de GABA como **psicobióticos potenciais** no eixo intestino-
  cérebro (Zielińska 2026)[OB] — **ponte, não prova**: GABA bacteriano ≠ GABA cerebral (Regra
  B5.R07).

{listra('IFACE')}

"""
anc="## BLOCO_09 — IMPACTO SOBRE NEUROPLASTICIDADE (elo B3)"
assert doc.count(anc)==1; doc=doc.replace(anc, iface_txt+"---\n\n"+anc, 1)

# 10) nota AT
nota="""
---

### Atualização [AT] 2026-09-08 — insumos externos (P-7), 116 refs incorporadas (44→160)

Auditoria ref a ref (G1 eutils semântico; relatório em `producao/insumos/RELATORIO_AUDITORIA_MATRIZ_B5.md`):
192 itens colados/anexados; 190 resolvidos com identidade verificada; **1 falso positivo exposto**
(\"Prosowski 2024\": DOI do anexo resolve para artigo não correlato; artigo pretendido inexistente no
PubMed → `[G1]`, não entrou); **3 correções de autoria** (\"Matthew & Samba 2013\"→Carver 2013;
\"Pich & Millan 2018\"→Cavalleri 2018; Hollestein 2021→2023); correções de metadados da consolidação
**confirmadas corretas** (Guntupalli=JNeurosci 2023; Storey=2025; Vereczki=2021; prioridade Xu 2020
sobre a carta Babber & Sharma; Duman Neuron 2019). Grupos: KET 21 · GABA 20 · NMDA 19 · PLAST 14 ·
MRS 14 · ANX 10 · STR 6 · IFACE 7. 14 EXC escopo (Alzheimer×5, autismo×4, epilepsia×3, apneia, carta
redundante), 53 baixo incremento, 2 não-resolvidos, 6 já vigentes. P-6 pendente.

"""
anc="## TABELA DE EVIDÊNCIAS"
assert doc.count(anc)==1; doc=doc.replace(anc, nota.strip()+"\n\n"+anc, 1)

# 11) tabela +3 linhas
old_row="| Em disputa | HNK independente de NMDAR (Zanos) vs NMDA; midazolam | [EMERGENTE] |"
new_rows=(old_row+"\n"
"| MRS meta/EC | GABA↓ TDM, glutamato global sem dif. (Godfrey, NEG) × Glx↑+GABA↓ (Kantrowitz); Glx×GABA+ depende de coorte (Steel×Rideaux) | alto humano, confundidores MRS |\n"
"| PET TRD | Dinâmica AMPAR acompanha gravidade/resposta à cetamina (Nakajima); correlatos de resposta (Yun) | médio (humano, fronteira) |\n"
"| Circuito E/I | dmPFC→LHb dual-pathway na suscetibilidade (Wu); PV amígdala/kainato-GABA-B (Ryazantseva); BNST→NAc ansiolítico (Xiao) — [ML/EXT] | médio (animal→humano) |\n"
"| CONT par | Potenciação NMDAR antidepressivo-símile (Pothula; Zanos-2023) vs antagonismo; hipótese opioide (Lu) | [EMERGENTE] |")
assert doc.count(old_row)==1; doc=doc.replace(old_row,new_rows)

# 12) regras de leitura
regras="""
### Regras de leitura B5 (fixadas na rodada [AT] 2026-09-08)

- **B5.R01** — Não existe \"glutamato alto + GABA baixo\" como estado universal de depressão ou ansiedade:
  a própria base MRS discorda (Godfrey × Kantrowitz); a biblioteca modela **heterogeneidade por região,
  tipo celular, estado temporal e contexto** — e o sinal pode ser oposto entre ansiedade e depressão.
- **B5.R02** — Níveis de evidência separados: concentração (MRS) ≠ neurotransmissão ≠ receptor ≠
  transportador ≠ sinalização ≠ circuito ≠ comportamento. **GABA/Glx por MRS ≠ E/I sináptico**
  (controle Steel; contradição Rideaux).
- **B5.R03** — NMDAR ≠ mecanismo unidirecional \"ruim\" (potenciação também é antidepressivo-símile);
  **antagonismo NMDAR ≠ descrição suficiente da cetamina** (metabólitos, AMPAR, correntes tônicas,
  enantiômeros, plasticidade a jusante).
- **B5.R04** — glutamato↑ ≠ excitotoxicidade: exige evidência adicional de sobrecarga de Ca²⁺, estresse
  oxidativo e dano neuronal (elo B6), que a B5 não reivindica.
- **B5.R05** — Fundamentos (LTP/LTD, subunidades, inibição tônica/fásica, interneurônios PV/SST, ciclo
  glutamina) entram como **SUP mecanístico `[ML]`/`[EXT]`** (R04), não como evidência clínica de MDD/
  ansiedade; a tradução humana da plasticidade é B3.
- **B5.R06** — Negativos e contraditórios preservados com o mesmo peso: Godfrey-NEG, Rideaux-NEG,
  Steel-contexto, Pothula-CONT, Sial/Lu-opioide críticas.
- **B5.R07** — Psicobióticos GABA = **ponte B5↔B7**, não prova de aumento de GABA cerebral.
- **B5.R08** — Fármacos citados como **sonda experimental de alvo** (P20): nenhum dado de dose, via,
  posologia ou indicação entra na B5 (neuroesteroides → B14 para a camada clínica).
- **B5.R09** — A leva [AT] (116 refs) aguarda P-6 (2ª verificação independente cega).
"""
anc="## ELEMENTOS MOLECULARES CRÍTICOS (UniProt/HGNC)"
assert doc.count(anc)==1; doc=doc.replace(anc, regras.strip()+"\n\n---\n\n"+anc, 1)

# 13) apêndice
ap=("> Bloco [AT] 2026-09-08 — insumos externos auditados (116 refs; relatório em producao/insumos/):\n"
    +listra_up(LAB['GABA']+LAB['NMDA'])+"\n"
    +listra_up(LAB['AMPA']+LAB['KET'])+"\n"
    +listra_up(LAB['PLAST']+LAB['MRS'])+"\n"
    +listra_up(LAB['ANX']+LAB['STR']+LAB['IFACE']))
anc="## METADADOS CANÔNICOS (Contrato de Geração — P12 / R06 / P17)"
assert doc.count(anc)==1; doc=doc.replace(anc, "\n"+ap+"\n\n---\n\n"+anc, 1)

for r in AT:
    up=unicodedata.normalize('NFKD',r['label']).encode('ascii','ignore').decode().upper()
    assert f"{up}[{r['tag']}]" in doc, r['label']
    assert f"{r['label']}[{r['tag']}]" in doc, 'body '+r['label']
assert not re.search(r'\b\d{7,9}\b', doc), 'numero longo no texto!'
open(F,'w').write(doc)
print('palavras:',len(doc.split()))
print('refs novas no corpus:',sum(doc.count(unicodedata.normalize('NFKD',r['label']).encode('ascii','ignore').decode().upper()+'['+r['tag']+']') for r in AT))
print('MD APLICADO OK')
