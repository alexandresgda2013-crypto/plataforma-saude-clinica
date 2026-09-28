#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere a prosa + listras + apêndice + controvérsias + tabela da leva [AT] 2026-09-08
na B3 V2. Uma passada, asserts estritos (âncora única + listra presente)."""
import json
from pathlib import Path
B3=Path('/home/user/BIBLIOTECAS/B03_Neuroplasticidade')
V=B3/'B3 NEUROPLASTICIDADE V2 CANONICA.md'
txt=V.read_text(encoding='utf-8')
CFG=json.load(open(B3/'producao/insumos/matriz_b3_at_final.json'))
by={}
for o in CFG: by.setdefault(o['grupo'],[]).append(o)
def listra(g):
    return '*'+ ' | '.join(f"{o['label']}[{o['tag']}]" for o in by[g]) +'*'

INS={}
INS['A']=("### 2.2 Via rápida AMPA→mTORC1","""[AT 2026-09-08] O eixo BDNF→TrkB foi reforçado em três frentes. **(i) Arquitetura da sinalização:** o
receptor TrkB e suas cascatas (Ras-MAPK, PI3K-Akt, PLCγ) já dispõem de mapa consolidado (Kozisek 2008)[OB];
endossomas de sinalização BDNF/TrkB trafegam do axônio ao núcleo e coordenam CREB/mTOR à distância
(Moya-Alvarado 2023)[ML]; o efeito tipo-antidepressivo exige acoplamento do receptor a **Gαi1/3** (Marshall
2018)[ML]; e a isoforma truncada **TrkB.T1** modula comportamento tipo-depressivo geneticamente determinado
(Alsalloum 2023)[ML] — todas [APENAS PRÉ-CLÍNICO] no nível molecular. **(ii) Interface com estresse:** revisões
convergentes ligam BDNF/TrkB à desregulação pelo estresse (Castrén 2021)[OB]; (Numakawa 2024)[OB].
**(iii) ERK como nó:** a via ERK liga sinalização trófica ao fenótipo depressivo (Wang 2019)[OB].
**Regra [AT]:** TrkB não é interruptor único — importa a célula, o compartimento e o parceiro de sinalização.

"""+listra('A')+"\n\n")
INS['B']=("### 2.3 Ressalvas da via rápida","""[AT 2026-09-08] A via rápida ganhou leitura sistemática: revisão de **139 publicações** (humano, animal
e cultura) sobre ação antidepressiva rápida da cetamina encontrou convergência em glutamato, AMPAR, mTOR,
BDNF/TrkB, eEF2K, GSK-3 e ERK — e não uma via única (Kang 2022)[MA]. Autores de referência alinham o
mesmo quadro multiescalar (Krystal 2024)[OB]; (Kavalali 2025)[OB]; (Duman 2012)[OB]; (Duman 2019)[OB];
(Zanos & Gould 2018)[OB]; sob lente computacional, o efeito é reenquadrado como \"tempestade\" no cérebro
preditivo (Bottemanne 2023)[OB]; e transições de estado de humor dependem de mecanismos sinápticos
distintos (Parekh 2022)[OB]. No plano experimental, o locus sináptico de TrkB é exigido para o efeito
rápido (Lin 2021)[ML]; espinhaturas novas em mPFC surgem em horas (Wu 2021)[ML]; a resposta rápida usa
AMPAR permeável a Ca²⁺ (Zaytseva 2023)[ML]; a convergência de vias sobre **scaling sináptico** dispara o
efeito (Suzuki 2021)[ML]; e o andaime **PSD-95** amplifica sinalização trófica (Shi 2024)[ML] — todos
[APENAS PRÉ-CLÍNICO]. **Regra [AT]:** convergência molecular ≠ mecanismo clínico comprovado; cada elo é
SUPPORT, não causa validada no paciente (B3.C15/C16).

"""+listra('B')+"\n\n")
INS['C']=("### 2.4 Metaplasticidade e GSK-3β/Wnt","""[AT 2026-09-08] A dissociação temporal rápido↔sustentado ficou mais fina. O metabólito
(2R,6R)-hidroxinorketamina produz alterações duradouras com assinatura própria (Yao 2018)[ML] e modula
a função de NMDAR sináptico (Suzuki 2017)[ML]; comportamentos antidepressivo-relevantes podem depender
de **ativação** — não bloqueio — de NMDAR (Zanos 2023)[ML]. A potenciação inicial e a plasticidade que
perdura distinguem cetamina de seu metabólito (Brown 2025)[ML], e uma **plasticidade tempo-sensível**
separa as ações rápidas das sustentadas (Brown 2026)[ML]; a duração do efeito pode ser estendida
reforçando ERK/DUSP6 na sinapse CA3-CA1 (Ma 2025)[ML] — todos [APENAS PRÉ-CLÍNICO]. A pergunta \"quando\"
importa tanto quanto o \"como\" (Wu 2021b)[OB]; a ponte rápido↔sustentado segue a questão aberta central
(Kim 2023)[OB]; arketamina sinaliza **além** de NMDAR (Wei 2022)[OB]; e os metabólitos foram
sistematizados (Hess 2022)[OB]. **Regra [AT]:** efeito molecular imediato ≠ remodelamento sináptico
sustentado ≠ efeito clínico sustentado (B3.C15).

"""+listra('C')+"\n\n")
INS['D']=("### 2.5 Energia da plasticidade (B6/B9)","""[AT 2026-09-08] A metaplasticidade virou alvo explícito de sustentação do efeito antidepressivo
(Brown 2024)[OB]. Mecanismo de fronteira: **cross-talk TrkB–mGluR5** como metaplasticidade sináptica da
cetamina, com reforço da sinalização BDNF/TrkB (Arefin 2026)[ML]; [APENAS PRÉ-CLÍNICO]. A regulação
pós-sináptica de mGluR5 sustenta a leitura glutamatérgica complementar (Elmeseiny 2024)[OB].
**Regra [AT]:** a resposta a um estímulo plástico depende da história plástica prévia do circuito (B3.C09).

"""+listra('D')+"\n\n")
INS['E']=("\n### 2.6 Detalhe da via rápida (por dentro)","""
### 1.6 Caixa de ferramentas LTP/LTD — fundamentos SUPPORT/METH [AT 2026-09-08]
Os trabalhos fundamentais da plasticidade entram nesta biblioteca como **SUPPORT/METH**, não como
evidência clínica direta: a internalização dependente de atividade de NMDAR-GluN2B é necessária para a
incorporação de GluN2A e a plasticidade sináptica (Storey 2025)[ML]; calcineurina ancorada em AKAP150
limita CP-AMPAR (Sanderson 2012)[ML]; o LTD dependente de NMDAR exige incorporação transitória de
CP-AMPAR (Sanderson 2016)[ML]; a homeostase é controlada por quinases/fosfatases ancoradas
(Sanderson 2018)[ML]; o acoplamento PKA–GluA1 via AKAP5 regula a fosforilação de AMPAR (Diering
2014)[ML]; o \"código\" do receptor AMPA organiza subunidades na plasticidade (Diering & Huganir
2018)[OB]; o direcionamento subcelular de subunidades define a plasticidade sináptica (Soares 2013)[OB];
LTP e LTD de NMDAR usam mecanismos de tráfego distintos (Peng 2010)[ML]; a competição entre AMPAR
permeáveis e impermeáveis a Ca²⁺ regula LTP (Sumi 2020)[ML] e o LTD muscarínico/NMDAR-dependente
(Sumi 2023)[ML]; o balanço reciclagem↔lisossomo define o destino dos receptores (Fernández-Monreal
2012)[OB]; e a fosforilação de GluA2 \"porta\" a plasticidade homeostática (Yong 2020)[ML].
**Regra [AT]:** nenhum desses estudos mostra, por si, \"alteração X em paciente deprimido\" — eles
sustentam a gramática mecanística sobre a qual os achados clínicos são interpretados (B3.C08).

"""+listra('E')+"\n\n")
INS['F']=("### 3.2 NMDA sináptico vs. extrassináptico","""[AT 2026-09-08] O polimorfismo **Val66Met (rs6265)** e o domínio pró-BDNF ganharam corpo mecanístico:
o produto Val66 altera a estrutura do pró-domínio e induz retração do cone de crescimento (Anastasia
2013)[ML]; a variante humana Val66 — mas não Met66 — ativa via de enfraquecimento sináptico
(Kailainathan 2016)[ML]; e ações da pró-peptídeo facilitam LTD hipocampal, alteradas pelo polimorfismo
(Mizui 2015)[ML] — todos [APENAS PRÉ-CLÍNICO]. No humano, Val66Met associa-se a níveis cerebrais de
BDNF e a depressão/suicídio (Youssef 2018)[EC]; a evidência BDNF×TDM foi revista criticamente
(Kishi 2017)[OB]; a variante altera vulnerabilidade a estresse e resposta a antidepressivos em modelo
knock-in (Yu 2012)[ML]; trauma infantil × Val66Met modula plasticidade cerebral (Tian 2021)[EC];
estresse precoce interage com o polimorfismo (Gatt 2009)[EC]; e o polimorfismo regula efeitos
corticolímbicos de glicocorticoides (Notaras 2017)[ML]. Memória de medo e sensibilidade a estresse
completam o quadro (Notaras 2020)[OB], e a susceptibilidade passa por neurônios **D2 do NAc** via
BDNF-TrkB (Pagliusi 2022)[ML] — valência regional do BDNF já prevista nesta biblioteca.

"""+listra('F')+"\n\n")
INS['G']=("### 3.3 Poda por complemento e microglia","""[AT 2026-09-08] O braço glutamatérgico/NMDAR foi detalhado: a disfunção da transmissão glutamatérgica
na depressão tem leitura molecular integrada (He 2023)[OB]; receptores NMDA ligam psicofarmacologia a
plasticidade (Comai 2024)[OB]; receptores glutamatérgicos e neuroplasticidade na depressão implicam
diretamente cetamina e rapastinel (Wang 2022)[OB]; receptores **GluN2B** regulam comportamento
tipo-depressivo e resposta antidepressiva (Miller 2014)[ML]; e a **inibição gabaérgica** é leitura
parceira da ação rápida da cetamina (Luscher 2020)[OB]. **Regra [AT]:** glutamato aumentado ≠
plasticidade benéfica automática (B3.C07) — a valência depende de compartimento, subunidade e tempo.

"""+listra('G')+"\n\n")
INS['H']=("### 4.1 Neurogênese adulta (giro denteado)","""[AT 2026-09-08] A interface inflamação↔plasticidade ganhou caminhos próprios — em coordenação, não
colonização, com B1: síntese de BDNF dependente de **ERK1/2 na micróglia** é exigida para o efeito
antidepressivo (Lu 2022)[ML]; a sinalização microglial **ERK-NRBP1-CREB-BDNF** sustenta a ação de
(R)-cetamina (Yao 2022)[ML]; deficiência de BDNF exacerba anedonia induzida por inflamação (Parrott
2021)[ML] — todos [APENAS PRÉ-CLÍNICO]; e o eixo inflamação→BDNF/TrkB foi organizado em revisão
(Zhang 2016)[OB]. **Regra [AT]:** micróglia ativada ≠ necessariamente patológica; inflamação ≠ redução
uniforme da plasticidade (B3.C12).

"""+listra('H')+"\n\n")
INS['I']=("### 5.2 Densidade sináptica in vivo (SV2A-PET) e volumetria","""[AT 2026-09-08] **Controvérsia formal — BDNF periférico (B3.C05):** a leitura translacional do BDNF
sanguíneo segue limitada por correlação indireta (Arosio 2021)[OB]; a associação diagnóstica é
populacional, não molecular (Nikolac Perkovic 2023)[OB]; em roedor, BDNF periférico produz efeito
tipo-antidepressivo por vias celular/comportamental [EXTRAPOLADO: roedor→humano] (Schmidt 2010)[ML];
e meta-análise de psicoplastógenos **não encontrou efeito significativo da cetamina sobre BDNF
periférico** (Calder 2025)[MA] — somando-se à meta de TRD já incorporada (Meshkat 2022).
**Regra [AT] (B3.C05):** BDNF periférico não é equivalente ao cerebral nem biomarcador clínico validado
isoladamente; jamais ler como \"medidor de neuroplasticidade cerebral\".

"""+listra('I')+"\n\n")
INS['JK']=("### 6.1 Antidepressivos monoaminérgicos","""[AT 2026-09-08] Outras sondas de assinatura trófica: **GLYX-13** (agonista parcial do sítio glicina
do NMDAR) produz respostas sinápticas e comportamentais rápidas (Liu 2017b)[ML]; **óxido nitroso**
reproduz efeitos tipo-cetamina sobre transmissão excitatória em hipocampo (Izumi 2022)[ML] — ambos
[APENAS PRÉ-CLÍNICO; sondas experimentais de alvo, sem leitura de conduta (P20)].

"""+listra('J')+"""

### 5.4 Evidência humana direta e regionalidade [AT 2026-09-08]
A plasticidade pôde ser medida no humano — com proxies reados com cuidado: aprendizagem serve de modelo
de plasticidade neural na depressão maior (Nissen 2010)[EC]; **LTP-like visual associa-se negativamente
a sintomas depressivos** [dado negativo central] (Rygvold 2022)[EC]; S-cetamina modula subcampos
hipocampais em voluntários (Höflich 2021)[EC]; adaptações conservadas de rede unem estresse humano e
animal (Nikolova 2018)[EC]; e a neuroplasticidade hipocampal adulta aparece desregulada na depressão em
síntese translacional (Tartt 2022)[OB]. Métodos e limites para medir plasticidade em saúde mental foram
sistematizados (Appelbaum 2023)[OB]. Sobre a **regionalidade** do efeito rápido: a ação da cetamina é
específica de região (Chen 2024)[ML]; imagem longitudinal mostra remodelação dendrítica in vivo
(Phoumthipphavong 2016)[ML]; S-cetamina reverte déficits de espinhos hipocampais em linhagem sensível
(Treccani 2019)[ML]; a arquitetura de espinhos muda com o comportamento crônico (Pryazhnikov 2018)[ML];
e a cetamina aumenta plasticidade estrutural em neurônios dopaminérgicos de camundongo e derivados de
iPSC humano (Cavalleri 2018)[ML] — pré-clínico com ponte iPSC. **Regra [AT]:** evidência humana de
plasticidade é proxy-dependente; a tese \"depressão = baixa plasticidade\" é simplificação rejeitada
(B3.C01/02).

"""+listra('K')+"\n\n")
INS['L']=("### 6.4 Extinção e o subtipo ansiedade/TEPT","""[AT 2026-09-08] A convergência mecanística entre cetamina e **psicodélicos clássicos** passa pela
neuroplasticidade — a janela reaberta precisa ser preenchida por experiência (Aleksandrova 2021)[OB].

"""+listra('L')+"\n\n")
INS['M']=("\n## BLOCO_07 — NÓS MOLECULARES CENTRAIS (SÍNTESE)","""[AT 2026-09-08] No subtipo **ansiedade**, as moléculas reguladoras da plasticidade foram mapeadas como
arquitetura própria (Sha 2023)[OB]; e a correção precoce de LTD sináptico melhora comportamento
tipo-ansiedade (Shin 2020)[ML]; [APENAS PRÉ-CLÍNICO]. **Regra [AT]:** em ansiedade, o problema é mais
de **direção/valência** da plasticidade (aprendizagem de medo mal-adaptativa) do que de quantidade
bruta — assimetria que o distingue da hipoplasticidade depressiva.

"""+listra('M')+"\n\n")
INS['N']=("### 9.1 Reversibilidade é a tese","""[AT 2026-09-08] Variantes em genes do eixo plástico (**BDNF, NTRK2, NGFR, CREB1, GSK3B, AKT, MAPK1,
MTOR, PTEN**) associam-se a fenótipos de tratamento antidepressivo em humano (Santos 2023)[EC]; e
modificações **epigenéticas** acoplam neuroplasticidade à patogênese da depressão — elo com B5
(Benatti 2024)[OB].

"""+listra('N')+"\n\n")
INS['O']=("\n## TABELA DE EVIDÊNCIAS","""
## BLOCO_03/08 (SÍNTESE [AT] 2026-09-08) — ESTRESSE→REMODELAÇÃO REGIONAL E FRONTEIRAS

**Estresse e remodelação regional (síntese auditada).** O mapa estresse→plasticidade não é monótono:
a plasticidade estrutural/sináptica nos transtornos de estresse tem arquitetura própria (Pittenger
2008)[OB]; os efeitos do estresse sobre neurônios divergem entre hipocampo, amígdala e CPF (McEwen
2016)[OB]; estresse e ansiedade acoplam plasticidade estrutural e regulação epigenética (McEwen
2012)[OB]; o mesmo estresse diverge por \"vizinhança\" — hipocampo vs. amígdala (Chattarji 2015)[OB] —
e por paradigma (Wilson 2015)[OB]; neurônios estrelados da amígdala remodelam-se sob estresse (Lau
2017)[ML]; estresse social reorganiza arquitetura límbica em modelos (Patel 2019)[OB]; espinhas
dendríticas são o elo com ansiedade (Leuner 2013)[OB]; o CPF acumula evidência estrutural-funcional-
molecular do desenvolvimento ao envelhecimento (Algaidi 2025)[OB]; a plasticidade mal-adaptativa tem
leitura neuronal-sináptica própria (Ren 2025)[OB]; a sinalização molecular do estresse interage com a
cognição (Lugenbühl 2025)[OB]; e o modelo integrativo liga cognição, psicologia e plasticidade na
depressão (Price 2020)[OB]. Enquadramento: revisões estruturais-sinápticas (Christoffel 2011)[OB],
molecular-celular-funcional (Marsden 2013)[OB], hipocampo→CPF (Liu 2017)[OB]; dendritos na doença
neuropsiquiátrica (Forrest 2018)[OB]; plasticidade e conectividade HPC-CPF (Ruggiero 2021)[OB]; o
estresse reduz sinalização BDNF→TrkB e o elo TrkB-NMDAR (Robinson 2021)[ML]; a matriz extracelular
modula a plasticidade sob estresse (Laham 2021)[OB]; e a molécula-guia **DCC** desenha a vulnerabilidade
ao estresse — fronteira (Aguilar-Valles 2026)[OB]. **Regra [AT]:** \"estresse reduz plasticidade\" é
simplificação — o que muda é a configuração regional, temporal e intensidade-dependente (B3.C03/C11).

**Fronteiras 2025–2026.** Mecanismos de neuroplasticidade em doença psiquiátrica (O'Donnell 2026)[OB];
plasticidade estrutural evocada por antidepressivos de ação rápida (Liao 2025)[OB]; dos déficits
monoaminérgicos à plasticidade multiescalar — 25 anos de cetamina (Bulek 2026)[OB]; cetamina e
neuroplasticidade evolutiva — a dimensão temporal (Prabakar 2026)[OB]; e o framework conectômico do
glutamato na depressão (Carmellini 2025)[OB].

**Regras de leitura [AT] (governança B3.C01–C20, auditadas no insumo externo).** (01) plasticidade
implicada ≠ alteração única/uniforme; (02) sinápticas observadas em modelos e em alguns humanos;
(03) estresse remodela por região/intensidade/duração; (04) BDNF/TrkB é via importante, não única;
(05) BDNF periférico ≠ cerebral ≠ biomarcador validado isolado; (06) NMDAR/AMPAR participam de
plasticidade e de rápidos; (07) glutamato ↑ ≠ plasticidade benéfica; (08) LTP/LTD fundamentais com
relação clínica indireta; (09) metaplasticidade altera respostas futuras; (10) dendritos/espinhas
remodelam-se com estresse e intervenções, sobretudo em modelos; (11) HPA/glicocorticoides modulam
plasticidade por região/contexto; (12) neuroinflamação modula sem equivalência imune↔dano; (13) estresse
oxidativo/mitocôndria interferem na capacidade plástica; (14) mTOR participa, mas ≠ sinônimo de
plasticidade; (15) cetamina: rápido em modelos + evidência clínica, ponte causal incompleta; (16) nenhum
mecanismo único explica toda resposta antidepressiva; (17) exercício modula vias sem cadeia uniforme
biomarcador→benefício; (18) plasticidade ≠ neurogênese (escopo B16 — P16); (19) TRD sem biomarcador
plástico único validado; (20) plasticidade é integrador mecanístico, não causa única.

"""+listra('O')+"\n\n")

# aplica inserções
for k,(anchor,payload) in INS.items():
    assert txt.count(anchor)==1, f"âncora {k} não-única ({txt.count(anchor)}): {anchor[:60]}"
    txt = txt.replace(anchor, payload+anchor, 1)

# cabeçalho + nota de rodada
old_hdr="**artefato_rotulo:** CANÔNICA v1 · G1 (51/51 PMIDs eutils) + G2 (espécie/desenho/elegibilidade) + G3 (suporte por vínculo; abstracts dos achados de alto risco lidos)."
new_hdr="**artefato_rotulo:** CANÔNICA v2 · G1/G2/G3 (53 refs) + rodada **[AT] 2026-09-08** (P-7): insumo externo auditado ref a ref — 112 incorporadas, 0 FP, 3 correções de autoria, 33 EXC escopo + 42 baixo incremento + 2 erratas + 8 não-resolvidos → **53→165 refs**; P-6 2ª verificação cega PENDENTE."
assert txt.count(old_hdr)==1; txt=txt.replace(old_hdr,new_hdr,1)
txt=txt.replace("# B3 NEUROPLASTICIDADE V1 CANÔNICA","# B3 NEUROPLASTICIDADE V2 CANÔNICA",1)
old_nota="> independente (P-6) fica como pendência de fase para o avaliador cego."
assert txt.count(old_nota)==1
txt=txt.replace(old_nota, old_nota+"""

> **[AT] 2026-09-08 (V2 — reconciliação de insumo externo, P-7).** Insumo \"matriz canônica B3\" (Consensus, 193 itens)
auditado ref a ref via eutils: **0 falsos positivos de identidade**; 3 divergências de autoria no anexo corrigidas
(\"Schofield\"→Gatt 2009; \"Pich\"→Cavalleri 2018; \"Zhang\"→Yao N 2018); substitutas oficiais do insumo verificadas
(Storey 2025; Brown 2026; Ma 2025 = Science; \"Zhang 2016\" cravado como Zhang JC 2016). Ganho: BDNF periférico
formalizado como **controvérsia B3.C05**; eixo cetamina multiescalar/temporal (rápido↔sustentado); evidência humana
direta de plasticidade (incl. dado negativo Rygvold); caixa LTP/LTD SUPPORT/METH; subtipo ansiedade reforçado;
fronteiras 2026; governança B3.C01–C20 como regras de leitura. G3 declarado = IA (geração); **P-6 (2ª verificação
cega) permanece PENDENTE** e entra no pacote Via 2 junto com B1/B2.""",1)

# TABELA DE EVIDÊNCIAS
old_row="| Revisão | BDNF/TrkB (Duman, Castrén); CRF/dinâmica do estresse; psicodélicos (RCTs ainda a confirmar) | alto/médio |"
assert txt.count(old_row)==1
txt=txt.replace(old_row, old_row+"""
| Meta/sistemática [AT 2026-09-08] | via rápida da cetamina: convergência multiescalar (Kang); cetamina **não** move BDNF periférico (Calder — NEG) | médio-alto (síntese; heterogeneidade) |
| Humano direto [AT 2026-09-08] | plasticidade em TDM (Nissen); LTP-like ↓ com sintomas (Rygvold — NEG); S-cetamina/hipocampo RCT (Höflich); Val66Met×cérebro (Youssef, Gatt, Tian); farmacogenética (Santos) | médio (associativo/RCT pequeno) |
| Pré-clínico mecanismo [AT 2026-09-08] | GluN2B→GluN2A (Storey); ERK/DUSP6 CA3-CA1 (Ma); TrkB×mGluR5 (Arefin); HNK (Yao N, Suzuki K); micróglia-ERK-BDNF (Lu, Yao W) | médio (animal, [EXT]) |""",1)

# CONTROVÉRSIAS
old_cont="- Fármacos que falharam na tradução (agonistas TrkB, AMPAkinas, inibidores GSK-3)."
assert txt.count(old_cont)==1
txt=txt.replace(old_cont, old_cont+"""
- **[AT 2026-09-08] BDNF periférico como \"biomarcador\":** meta de psicoplastógenos sem efeito cetamina→BDNF sanguíneo (Calder 2025) + meta TRD (Meshkat 2022) → B3.C05 permanece **controvérsia/limitação**, nunca marcador clínico isolado.
- **[AT] Plasticidade humana direta é proxy — e pode ser negativa:** LTP-like visual associou-se negativamente a sintomas (Rygvold 2022); leitura dependente de paradigma/tarefa/região.
- **[AT] Janela temporal dos rápidos:** efeito molecular imediato ≠ remodelamento sustentado ≠ efeito clínico sustentado (Brown 2025/2026; Kim 2023) — exige endpoints temporais.
- **[AT] Exclusões formais da rodada:** TEPT, TCE, AVE, Alzheimer, EM, dor, anorexia, Fragile X e intervenções fitoquímicas ficaram fora (escopo permanente); neurogênese adulta permanece escopo B16 (P16).""",1)

# APÊNDICE
old_apx="*LI_2017[ML] | ERICKSON_2011[OB] | SEKAR_2016[MA]*"
assert txt.count(old_apx)==1
def apx_line(gs):
    items=[]
    for g in gs:
        for o in by[g]:
            items.append(f"{o['ID'].replace('REF_','')}[{o['tag']}]")
    return '*'+' | '.join(items)+'*'
novas=[apx_line(['A','D']), apx_line(['B']), apx_line(['C']), apx_line(['E']), apx_line(['F','L']),
       apx_line(['G','H','J']), apx_line(['I','K']), apx_line(['M','N']), apx_line(['O'])]
txt=txt.replace(old_apx, old_apx+"\n"+"\n".join(novas),1)

V.write_text(txt,encoding='utf-8')
# varredura: toda label [AT] aparece ≥2× (prosa/listra + apêndice)
falta=[]
for o in CFG:
    n = txt.count(o['label'])
    if n<2: falta.append((o['pmid_final'],o['label'],n))
print("inserções OK · palavras:", len(txt.split()))
print("labels <2 menções:", falta)
print("PMIDs 7-9 dígitos no corpo:", [m for m in __import__('re').findall(r'\b\d{7,9}\b', txt)][:5])
for ln in novas: assert ln in txt
print("apêndice [AT]:", len(novas), "linhas OK")
