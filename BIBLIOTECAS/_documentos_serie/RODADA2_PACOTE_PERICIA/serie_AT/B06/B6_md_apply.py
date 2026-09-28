# -*- coding: utf-8 -*-
import json, unicodedata, re

BASE = '/home/user/BIBLIOTECAS/B06_EstresseOxidativo/'
AT = json.load(open(BASE + 'producao/insumos/matriz_b6_at_final.json'))
assert len(AT) == 72
doc = open(BASE + 'B6 ESTRESSE OXIDATIVO V2 CANONICA.md', encoding='utf-8').read()

def norm_up(lab):
    s = unicodedata.normalize('NFKD', lab).encode('ascii', 'ignore').decode()
    if s.endswith('b') and not s.endswith('bb') and s[-2].isdigit():
        return s[:-1].upper() + 'b'
    return s.upper()

LAB = {}
TAG = {}
for r in AT:
    LAB.setdefault(r['grupo'], []).append(r['label'])
    TAG[r['label']] = r['tag']

def listra(grupos):
    itens = []
    for g in grupos:
        itens += [(l, TAG[l]) for l in LAB[g]]
    return '*' + ' | '.join(f"{l}[{t}]" for l, t in itens) + '*'

def listra_up(grupos):
    itens = []
    for g in grupos:
        itens += [(l, TAG[l]) for l in LAB[g]]
    return '*' + ' | '.join(f"{norm_up(l)}[{t}]" for l, t in itens) + '*'

ops = []

# ============ 1) CABEÇALHO ============
ops.append(('# B6 ESTRESSE OXIDATIVO V1 CANÔNICA', '# B6 ESTRESSE OXIDATIVO V2 CANÔNICA'))
ops.append(("**artefato_rotulo:** CANÔNICA v1 · G1 (30/30 PMIDs eutils) + G2 + G3 (suporte por vínculo; abstracts de alto risco lidos).",
            "**artefato_rotulo:** CANÔNICA v2 · G1 (108/108 PMIDs eutils) + G2 + G3 (suporte por vínculo; abstracts lidos) · leva [AT] 2026-09-08: +72 refs do eixo B6-vitamina→transsulfuração→glutationa (insumos externos auditados ref a ref, P-7)."))

# ============ 2) ENZ — nova seção 1.9 (fim do BLOCO_01) ============
SEC_ENZ = """### 1.9 O eixo B6-vitamina → transsulfuração → cisteína → glutationa (arquitetura validada) [AT 2026-09-08]
A defesa redox tem um braço **nutricionalmente controlado** que a V1 deixava implícito: o estado de
**vitamina B6/PLP** governa a **transulfuração** (Hcy → cistationina → **cisteína**, o substrato
limitante da glutationa) e, por ela, a dinâmica do sistema GSH/GPx. A leitura canônica é de
**arquitetura mecanística, não de direção clínica**: "B6 = antioxidante = antidepressivo" é
cadeia proibida (B6.R01); cada seta tem evidência própria.

**O cofator e suas enzimas.** PLP é cofator obrigatório da **CBS** e da **CGL/CSE**; a revisão
dos sítios ativos das enzimas da transulfuração fixa a base (Aitken 2011)[OB]. A CBS humana é uma
**hemoproteína PLP-dependente** singular: heme b confirmado em fígado humano/rato (Kéry & Kraus 1994)[OB],
cofatores heme/PLP com sítios não-equivalentes e funções mapeadas por região (Taoka & Banerjee 1999, dois
artigos)[OB], estrutura cristalina resolvida (Meier 2001)[OB], regulação/oligomerização estrutural
(Ereño-Orbea 2013)[OB], mecanismo de reação como **hemesensor redox** (Banerjee 2004)[OB] e cofator
heme incomum revisado (Singh 2007)[OB]. A regulação é multiescamada: o domínio regulador C-terminal
modula o defeito de mutantes catalíticos (Kabil 1999)[OB]; **AdoMet** estabiliza a CBS e modula a
capacidade redox celular (Prudova 2006)[OB]; há comunicação alostérica **PLP–heme** (Yadav 2012)[OB];
e o hememedia **inibição gasosa** da via por NO/CO — elo molecular direto com a sinalização do B1
(McFarlane 2024)[OB]. CGL/CSE apresenta variantes polimórficas e mutantes patogênicas com cinética
caracterizada (Zhu 2008)[OB].

**Janelas genéticas (estrutura → janela mecanística, nunca fenótipo psiquiátrico).** Mutações de
homocistinúria dissecam a enzima: localização intracelular diferente de mutantes (Casique 2013)[OB],
ambiente heme/PLP da variante R266K (Smith 2012)[OB], comportamentos contrastantes de mutantes
associados à resposta à piridoxina (Chen 2006)[OB], duas novas missense (Al-Sadeq 2024)[OB] e a
mutação R336C que rompe a comunicação com o cofator PLP mantendo a integridade global (Conter 2025)[OB].
**Mutação monogênica rara não é variação comum** — polimorfismos CBS/CGL ↔ fenótipo psiquiátrico = [G1].

**A via além da cisteína: H₂S.** CBS/CGL também geram **sulfeto de hidrogênio**, gaseotransmissor
PLP-dependente (Singh & Banerjee 2011)[OB]; a inibição farmacológica da CBS e o papel inesperado da
serina foram dissecados (Petrosino 2022)[OB].

**Regulação da via e elo com GSH.** O metabolismo de aminoácidos sulfurados controla produção e remoção
de homocisteína e cisteína (Stipanuk 2004)[OB] e responde a excessos de metionina/cisteína/sulfeto
(Stipanuk 2020)[OB]; reguladores da via foram revisados (Sbodio 2018)[OB] junto à regulação
pós-traducional (Pajares 2025)[OB]. A relação **quantitativa** Hcy↔síntese de GSH e sua modulação por
estado redox é clássica (Mosharov 2000)[OB]; micronutrientes/dieta → homeostase de GSH em revisão
(Gould & Pazdro 2019)[OB]. **Estado nutricional de B6 e disponibilidade celular de PLP governam as
reações canônicas da via e a produção de H₂S por reações laterais** — a âncora que transforma
"enzima existe" em "estado de B6 importa" (Gregory 2016)[OB]; a piridoxina conecta metabolismo de
um carbono ao sistema da glutationa peroxidase (Dalto & Matte 2017, revisão — nunca ensaio causal)[OB].
Manutenção do pool de PLP: biossíntese pela PNPO com particularidades por espécie (Rivero 2024)[OB],
proteína de homeostase de PLP (PLPBP) sustenta B6 celular e função oxidativa mitocondrial
(Ciapaite 2023)[OB]; os distúrbios do metabolismo de B6 foram mapeados (Wilson 2019)[OB].

**Fecho mecanístico com a V1.** A ablação de CGL (Cth⁻/⁻) torna a cisteína dietética essencial contra
miopatia oxidativa letal em camundongos — prova causal mamífera de que a transulfuração sustenta a
defesa redox in vivo (Ishii 2010)[ML]. E a via fecha o círculo da B6: ativar a transulfuração via CBS
atenua estresse oxidativo e **ferroptose** em eritroblastos falciformes humanos e camundongos
transgênicos — contexto de outra doença, mas a sequência **TS → cisteína → GSH → freio da ferroptose**
(§2.2) fica demonstrada como arquitetura (Xi 2025)[ML].

*LISTRA_ENZ*

---

"""
SEC_ENZ = SEC_ENZ.replace('*LISTRA_ENZ*', listra(['ENZ']))
ops.append(('## BLOCO_02 — VIAS MOLECULARES', SEC_ENZ + '## BLOCO_02 — VIAS MOLECULARES'))

# ============ 3) B6DEF — nova seção 2.4 (fim do BLOCO_02) ============
SEC_DEF = """### 2.4 Estado/deficiência de B6 × carga oxidativa em modelos animais — a heterogeneidade é o dado [AT 2026-09-08]
Os modelos de deficiência/repleção de B6 são a evidência causal **pré-clínica** do eixo — e a sua lição
mais importante é a **não-linearidade**. O estudo âncora: deficiência marginal de B6 em ratos elevou a
peroxidação (TBARS) em fígado e coração, **reduziu a razão GSH/GSSG** e induziu **resposta compensatória
de GPx e GR — sem diferença na glutationa total**: a defesa fica sob tensão mesmo com o pool preservado
(Cabrini 1998)[ML]. No mesmo sentido de heterogeneidade, a deficiência de B6 **suprimiu a transulfuração
hepática mas aumentou a concentração de GSH** em ratos em duas dietas de referência — o paradoxo que
proíbe o claim "deficiência de B6 → GSH↓" (Lima 2006)[ML]. Deficiência de B6 também piorou o estado
antioxidativo sob estresse oxidativo por exercício (Choi 2009)[ML]; status de B6 modulou defesas,
glutationa e enzimas associadas em camundongos sob EO induzido por homocisteína (Hsu 2015)[ML];
vitamina C ou B6 preveniram EO e a queda de prostaciclina em ratos homocisteinêmicos (Mahfouz 2004)[ML];
a piridoxina mostrou proteção in vivo e in vitro incluindo **inibição da xantina oxidase** (fonte de ROS,
§1.2) (Danielyan 2017)[ML]; em ratos sob hiperhomocisteinemia, B6 sozinho (Todorović 2025)[ML] ou com
folato (Todorović 2026)[ML] modulou biomarcadores cardiometabólicos e EO cardíaco; e num desenho fatorial
antigo, o status de B6 determinou a **direção** do efeito do chumbo sobre o GSH hepático (McGowan 1989)[ML].
**Trava:** esses efeitos são de modelo, com doses dietéticas manipuladas; a transferência para humano
passa obrigatoriamente pelos estudos de restrição controlada (§5.y), nunca por extrapolação direta
[APENAS PRÉ-CLÍNICO] (B6.R01).

*LISTRA_DEF*

---

"""
SEC_DEF = SEC_DEF.replace('*LISTRA_DEF*', listra(['B6DEF']))
ops.append(('## BLOCO_03 — MEDIADORES', SEC_DEF + '## BLOCO_03 — MEDIADORES'))

# ============ 4) ANTIOX — nova seção 3.x (fim do BLOCO_03) ============
SEC_ANT = """### 3.x Atividade antioxidante direta dos vitâmeros de B6 (química/celular) — selo [APENAS PRÉ-CLÍNICO] [AT 2026-09-08]
Além da função de coenzima, vitâmeros de B6 apresentam **atividade antioxidante direta** demonstrada em
química e célula: piridoxina e piridoxamina inibem superóxido, peroxidação lipídica, glicosilação de
proteínas e a queda da Na/K-ATPase em eritrócitos humanos expostos a glicose alta (Jain & Lim 2001)[ML];
em monócitos U937 sob H₂O₂, B6 reduziu radical livre, colapso de potencial mitocondrial e peroxidação
(Kannan & Jain 2004)[ML]; em endotélio vascular, piridoxamina/piridoxina/PLP reduziram superóxido e
peróxidos gerados por H₂O₂ (via NADPH oxidase) (Mahfouz 2009)[ML]. A química física sustenta o efeito:
reatividade elevada da piridoxina com •OH/•OOH/•O₂⁻ por DFT (Matxain 2006)[ML] e alta eficiência de
captura de **•OH** confirmada experimentalmente (Matxain 2009)[ML]; estudo cinético-mecanístico com ROS
fotogeradas por B2 (Natera 2012)[ML]; e piridoxina como scavenger de ânion superóxido em comparativo com
fenólicos (Zhou 1991)[ML]. **Honestidade de polaridade:** a mesma química admite face **pró-oxidante** —
vitaminas B mostraram ação anti e pró-oxidante dependendo do vitâmero e do sistema (Hu 1995)[ML], e o
risco pró-oxidante do piridoxal foi avaliado como competitivo em DFT (Ngo 2022)[ML]. A piridoxamina se
distingue por **sequestro de espécies carbonílicas e íons metálicos** e inibição de produtos finais de
glicação (AGEs) por atividade antioxidante primária (Ramis 2019)[OB]; o panorama "B6 além da coenzima"
(ROS, RCS, metais, fotoexcitados) foi consolidado em revisão mecanística (Wondrak & Jacobson 2012)[OB].
**Travamento total da cadeia (B6.R01):** captura de radical in vitro ≠ proteção de tecido ≠ efeito em
humano; e vitâmeros não são intercambiáveis (B6.R08) — nenhuma inferência clínica nasce desta camada.

*LISTRA_ANT*

---

"""
SEC_ANT = SEC_ANT.replace('*LISTRA_ANT*', listra(['ANTIOX']))
ops.append(('## BLOCO_04 — CÉLULAS / ESTRUTURAS', SEC_ANT + '## BLOCO_04 — CÉLULAS / ESTRUTURAS'))

# ============ 5) GSH + HIP — subseção no BLOCO_03 (PROFUNDIDADE) ============
SEC_GSH = """### Glutationa como sistema — biologia, medida e a hipótese Nrf2–B6 [AT 2026-09-08]
A camada CONTEXT da glutationa sustenta o vocabulário do módulo **sem gerar claim de vitamina B6**
(B6.R06): GSH é o antioxidante não-enzimático essencial e cofator de GPx/GST/glyoxalases
(Averill-Bates 2023)[OB]; as estratégias de elevação do GSH celular foram revistas sob o crivo de
precursores e limites de biodisponibilidade (Giustarini 2023)[OB]; a molécula como eixo de proteção
contra EO, envelhecimento e inflamação (Labarrere & Kassab 2022)[OB]; e as enzimas GSH-dependentes da
bioquímica à gerontologia (Lapenna 2023)[OB]. A química do dano alvo do GSH — peroxidação lipídica,
cinética dos processos e elo com **ferroptose** — foi consolidada (Valgimigli 2023)[OB]. **Medida:**
determinação simultânea de GSH/GSSG por HPLC (Nuhu 2020)[OB] e razão GSH/GSSG + proteínas
S-glutationiladas em sangue, tecidos e células (Giustarini 2017)[OB] padronizam o marcador; o trial
comparativo NAC × GSH oral × GSH sublingual mostra por que "elevar GSH por suplemento" é problema de
**bioquímica de biodisponibilidade**, não de intenção (Schmitt 2015)[EC]. **A fronteira declarada do
módulo:** foi proposta uma cadeia B6/PLP → metabólitos antioxidantes → NADPH/GSH → sinalização **Nrf2**;
ela é **hipótese emergente, não mecanismo estabelecido de suplementação de B6** — entra com selo
NÃO-CONSOLIDADO e dívida [G1] (Kato 2026)[OB] (B6.R05).

*LISTRA_GSH*

"""
SEC_GSH = SEC_GSH.replace('*LISTRA_GSH*', listra(['GSH', 'HIP']))
ops.append(('## BLOCO_04 (PROFUNDIDADE) — QUÍMICA POR CÉLULA', SEC_GSH + '## BLOCO_04 (PROFUNDIDADE) — QUÍMICA POR CÉLULA'))

# ============ 6) HUM — nova seção 5.y (antes do BLOCO_06) ============
SEC_HUM = """### 5.y Vitamina B6 em humano: fluxo de transulfuração, glutationa e marcadores [AT 2026-09-08]
A camada humana do eixo tem três ordens de evidência, com hierarquia estrita. **(i) Dieta controlada
(experimental humana):** a restrição dietética de B6 em adultos jovens **elevou GSH e cistationina
plasmáticas sem alterar o fluxo de cisteína** — o paradoxo humano do eixo, que veda a leitura
"menos B6 → menos GSH" (Davis 2006)[EC]; e a restrição de B6 mostrou tendência de **redução da taxa
de síntese eritrocitária de GSH sem alterar as concentrações** de GSH em eritrócitos ou plasma — a
dinâmica muda antes do pool (Lamers 2009)[EC]. **(ii) Observacional (associativo, nunca causal):**
status de B6/PLP associou-se a marcadores de inflamação e estresse oxidativo (CRP, 8-OHdG) na coorte
Boston Puerto Rican — transversal, com bidirecionalidade possível (Shen 2010)[OB]; e na LURIC, PLP,
homocisteína, telômeros e mortalidade se associaram prospectivamente em pacientes cardiovasculares —
associação prognóstica, não prova de intervenção (Pusceddu 2020)[OB]. **(iii) Intervenção como sinal
(sujeita a P20 — jamais posologia):** complexo B em alta dose alterou a **relação entre metabolismo
cerebral (¹H-MRS) e biomarcadores sanguíneos de EO** — a única janela da leva que observa cérebro e
periferia ao mesmo tempo, ponte direta com o bloco GSH-MRS vigente (Ford 2018)[EC]; B6 mediar capacidade
antioxidante via Hcy em pacientes pós-ressecção de hepatocarcinoma (Cheng 2016)[EC]; e GSH+B6 em
cirrose em RCT com seguimento (Lai 2020)[EC]. Completando a infraestrutura da regra B6.R08, os vitâmeros
foram quantificados em plasma e urina humanos sob suplementação de piridoxamina — as formas têm
destinos distintos, sem intercambiabilidade (Van den Eynde 2021)[EC]. **Trava:** nenhum desfecho desta
seção é psiquiátrico; a ponte para humor/ansiedade permanece em cascata via B1 (regra 10 do GPM),
nunca em salto.

*LISTRA_HUM*

---

"""
SEC_HUM = SEC_HUM.replace('*LISTRA_HUM*', listra(['HUM']))
ops.append(('## BLOCO_06 — TRADUÇÃO CLÍNICA (descritivo, NÃO prescritivo)', SEC_HUM + '## BLOCO_06 — TRADUÇÃO CLÍNICA (descritivo, NÃO prescritivo)'))

# ============ 7) NEG — subseção no BLOCO_06 (PROFUNDIDADE) ============
SEC_NEG = """### A lição dos grandes ensaios com vitaminas B: mover o biomarcador não é mover o desfecho [AT 2026-09-08]
Duas âncoras NEG — externas ao desfecho psiquiátrico, internas à **lógica causal** do módulo — foram
preservadas de propósito. No **NORVIT**, 3.749 pessoas pós-infarto receberam folato+B6±B12: a
homocisteína caiu, os eventos cardiovasculares **não** — a dissociação entre intermediário metabólico e
desfecho clínico em seu formato mais austero (Bønaa 2006)[EC]. No substudy do **WAFACS**, folato+B6+B12
**não alteraram biomarcadores plasmáticos de inflamação e função endotelial** em mulheres de risco
cardiovascular — o contraponto experimental à associação observacional de PLP↔inflamação (Christen
2018)[EC]. Juntas, elas operacionalizam a **B6.R01**: nem "PLP baixo ↔ marcador alto" (Shen) nem
"intervenção move Hcy" autorizam "B6 reduz estresse oxidativo humano com benefício"; cada seta da
cadeia exige evidência própria, e o elo que falta é o do desfecho.

*LISTRA_NEG*

"""
SEC_NEG = SEC_NEG.replace('*LISTRA_NEG*', listra(['NEG']))
ops.append(('## BLOCO_08 (PROFUNDIDADE) — CROSSTALK COM B1 E B9', SEC_NEG + '## BLOCO_08 (PROFUNDIDADE) — CROSSTALK COM B1 E B9'))

# ============ 8) NOTA [AT] antes da tabela ============
NOTA = """> **Atualização [AT] 2026-09-08 (insumos externos, P-7).** Anexo (106 refs) + GPM/briefing/triagem auditados ref a ref (esearch DOI[aid] → esummary → efetch): **98 resolvidas** (95 por DOI; Kéry & Kraus 1994 resgatada do [G1] do briefing por busca dirigida; Wondrak & Kannan fora do anexo, verificadas), tabela-mestra do GPM **45/45** confirmada, **zero falsos positivos**, divergências de autor/ano = 0. Incorporadas **72** (36→**108**): enzimologia/transulfuração 33, deficiência animal 9, antioxidante direto [APENAS PRÉ-CLÍNICO] 11, contexto glutationa 8, humano 8, âncoras NEG 2, hipótese Nrf2 1. BAIXO 10 e EXC 16 (autismo, Parkinson, Alzheimer/MCI, CV/DM sem lição nova, não-mamífero) registradas; NAO-IDX 10 expostas (incl. Itoh 2024 → [G1]). Overlap com o corpus vigente: **0** (arquitetura inédita no módulo). Incongruências do insumo expostas: "93 refs" vs 106 reais; Ereño-Orbea/Kéry dadas como não-localizadas — resolvidas aqui. P-6 (2ª verificação cega) permanece pendente.

"""
ops.append(('## TABELA DE EVIDÊNCIAS', NOTA + '## TABELA DE EVIDÊNCIAS'))

# ============ 9) TABELA +4 linhas ============
ops.append(('| Pré-clínico | Ferroptose/GPX4 (Chen); mitocôndria fonte de ROS (Tobe) | médio (animal→humano, [EXT]) |',
"""| Pré-clínico | Ferroptose/GPX4 (Chen); mitocôndria fonte de ROS (Tobe) | médio (animal→humano, [EXT]) |
| Bioquímica estrutural/revisão | PLP→CBS/CGL→transulfuração→cisteína (Kéry–Pajares; 33 refs [AT]) | alto (estabelecido) |
| Animal causal | deficiência de B6 → peroxidação com compensação GPx/GR e GSH total preservado (Cabrini; Lima); Cth-KO (Ishii) | médio ([ML]) |
| Humano dieta/observacional | restrição de B6: fluxo alterado sem queda do pool de GSH (Davis; Lamers); PLP↔inflamação associativo (Shen; Pusceddu) | médio (mecanismo); associação ≠ causa |
| Vitamina B como sonda (sinal/NEG) | Hcy↓ sem desfecho CV (Bønaa/NORVIT); biomarcadores de inflamação não alterados (Christen/WAFACS) | alto (âncora NEG, anti-extrapolação) |"""))

# ============ 10) REGRAS B6.R01–R09 ============
REGRAS = """**Regras fixadas na rodada [AT] (B6.R01–R09) — não reversíveis sem nova auditoria.**
- **B6.R01 (REGRA B6-STRESS-OXIDATIVO-01):** proibido inferir "B6 → ↓estresse oxidativo humano" a partir de antioxidante in vitro, GSH em animal, PLP→CBS/CGL ou PLP↔marcador observacional; cada seta exige evidência própria, e etapa não demonstrada = hipótese/inferência/associação.
- **B6.R02:** "B6 aumenta GSH" é claim proibido. O canônico é: B6/PLP modifica a **dinâmica** do sistema glutationa; o efeito sobre GSH/GSSG depende de tecido, estado nutricional e modelo (Cabrini sem Δ no total; Davis e Lima com elevação paradoxal; Lamers com taxa↔concentração divergentes).
- **B6.R03:** revisão nunca vira ensaio causal (Dalto & Matte; Wondrak & Jacobson; Gregory).
- **B6.R04:** observacional nunca vira causalidade — Shen e Pusceddu permanecem ASSOCIATIVO; a intervenção NEG de Christen decorre dessa trava.
- **B6.R05:** Nrf2/NADPH = hipótese emergente [G1] (Kato); jamais mecanismo comprovado de suplementação.
- **B6.R06:** literatura CONTEXT de glutationa não gera claim de B6.
- **B6.R07:** sistemas não-mamíferos (planta/bactéria/levedura/parasita/inseto) = EXC-registrado, sem transferência direta.
- **B6.R08:** vitâmeros não-intercambiáveis (piridoxina ≠ piridoxal/PLP ≠ piridoxamina); B6 pode ser **pró-oxidante** in vitro (Hu; Ngo) — polaridade honesta.
- **B6.R09:** fronteiras inalteradas — ROS mitocondrial é B9; neuroinflamação é B1 (cascata, nunca salto); Se/Zn/Cu/Mg é B8; PLP nas monoaminas é B4.

"""
ops.append(('## ELEMENTOS MOLECULARES CRÍTICOS (UniProt/HGNC)', REGRAS + '## ELEMENTOS MOLECULARES CRÍTICOS (UniProt/HGNC)'))

# ============ 11) APÊNDICE ============
ops.append(('*PENG_2024[MA] | BELL_2025[MA] | FENG_2025[MA] | LIU_2025[MA] | WANG_2026[MA] | RAPPENEAU_2020[MA] | ALLEN_2021[OB] | LEONARD_2012[OB] | HARMAN_1956[OB] | TEBAY_2015[OB] | BHATT_2020[OB]*',
            '*PENG_2024[MA] | BELL_2025[MA] | FENG_2025[MA] | LIU_2025[MA] | WANG_2026[MA] | RAPPENEAU_2020[MA] | ALLEN_2021[OB] | LEONARD_2012[OB] | HARMAN_1956[OB] | TEBAY_2015[OB] | BHATT_2020[OB]*\n*Leva [AT] 2026-09-08 (+72; eixo B6-vitamina→transulfuração→GSH):*\n'
            + listra_up(['ENZ']) + '\n' + listra_up(['B6DEF', 'ANTIOX']) + '\n' + listra_up(['GSH', 'HUM']) + '\n' + listra_up(['NEG', 'HIP'])))

# ============ 12) FECHO ============
FECHO_ADD = """
> **Canônica v2 [AT 2026-09-08] (insumos externos, P-7).** +72 refs auditadas ref a ref (36→**108**; 98 avaliadas, zero falso-positivo; tabela-mestra do GPM 45/45 revalidada). Entra o eixo **B6-vitamina → transulfuração (CBS/CGL) → cisteína → glutationa → carga oxidativa** com a heterogeneidade como dado central (Cabrini/Davis/Lima/Lamers), antioxidante direto selado [APENAS PRÉ-CLÍNICO], observacional marcado ASSOCIATIVO, hipótese Nrf2 com [G1] e âncoras NEG (NORVIT/WAFACS) sustentando a B6.R01. EXC 16 e NAO-IDX 10 expostas em producao/insumos/. Sem número de estudo, sem dose, sem conduta (P20). P-6 (2ª verificação cega) permanece pendente.
"""
ops.append(('> **Canônica v1 (Consolidação, Rodada 3).**', '> **Canônica v1 (Consolidação, Rodada 3).**' + FECHO_ADD.replace('> **Canônica v2', '\n> **Canônica v2')))

# ============ APLICAR ============
for old, new in ops:
    assert doc.count(old) == 1, 'âncora não-única: ' + old[:70]
    doc = doc.replace(old, new, 1)

# ============ VERIFICAÇÕES PÓS-EDIÇÃO ============
for r in AT:
    key = r['label'] + '[' + r['tag'] + ']'
    assert key in doc, 'rótulo ausente no corpo: ' + key
    up = norm_up(r['label']) + '[' + r['tag'] + ']'
    assert up in doc, 'rótulo ausente no apêndice: ' + up
digitos = re.findall(r'\b\d{7,9}\b', doc)
assert not digitos, 'PMID-like no texto: ' + str(digitos[:5])

open(BASE + 'B6 ESTRESSE OXIDATIVO V2 CANONICA.md', 'w', encoding='utf-8').write(doc)
import subprocess
wc = subprocess.run(['wc', '-w', BASE + 'B6 ESTRESSE OXIDATIVO V2 CANONICA.md'], capture_output=True, text=True)
print('OK; palavras:', wc.stdout.strip())
print('operações aplicadas:', len(ops))
