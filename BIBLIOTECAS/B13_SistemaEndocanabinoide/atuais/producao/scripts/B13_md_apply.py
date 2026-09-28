# -*- coding: utf-8 -*-
import re, shutil, unicodedata
BASE='/home/user/BIBLIOTECAS/B13_SistemaEndocanabinoide/'
V1=BASE+'B13 SISTEMA ENDOCANABINOIDE V1 CANONICA.md'
V2=BASE+'B13 SISTEMA ENDOCANABINOIDE V2 CANONICA.md'
doc=unicodedata.normalize('NFC', open(V1,encoding='utf-8').read())
shutil.copy(V1, BASE+'producao/historico/v1_canonica_2026-09-09.md')
a="# B13 SISTEMA ENDOCANABINOIDE V1 CANÔNICA"
assert doc.count(a)==1
doc=doc.replace(a,"# B13 SISTEMA ENDOCANABINOIDE V2 CANÔNICA")
anc="## TABELA DE EVIDÊNCIAS"
assert doc.count(anc)==1
B="""## BLOCO_14 — CAMADA RODADA [AT] 2026-09-09 (insumo externo auditado ref a ref; P-7)

[[AT 2026-09-09]] Reconciliação do insumo (RODADA0 + GPM molde v2.0 **reescrito** — o antigo tinha 5 PMIDs vazando no corpo — + matriz ChatGPT B13). Universo: 38 âncoras (20 já vigentes) + 66 não citadas (25 já vigentes) + NAO-IDX. Decisão: **ENTRA 40** (18 âncoras novas + 22 selecionados), **BAIXO 19**, **EXC 4** (1 falso mapeamento explícito + 3 sem indexação). Camadas preservadas: núcleo humano ≠ experimental `[ML]` ≠ **camada exógena** (via 10, isolada por regra). Números de efeito do insumo = alegação não copiada.

### 14.1 Humano endógeno: periféricos, exercício, genética, sexo

eCB séricos e humor após exercício na depressão maior — interface exercício em humano (Meyer 2019)[EC].
Exercício intenso aumenta eCB circulantes e BDNF concomitantemente em humanos — elo exercício×plasticidade (Heyman 2012)[EC].
O polimorfismo FAAH rs324420 modula o recall de extinção em humanos saudáveis medido por fMRI (Spohrs 2022)[EC].
Variação conjunta 5-HT1A/5-HT2A/CNR1 associa-se a tônus endocanabinoide alterado (Obermanns 2023)[EC].
Biomarcadores do ECS foram identificados e validados experimentalmente na depressão maior — candidatos, não diagnóstico (Wang 2025)[EC].
A revisão sistemática de endocanabinoides em indivíduos do sexo feminino com depressão fecha a janela sexo-específica (McWhirter 2024)[OB].

*Meyer2019_exercicio[EC] | Heyman2012_BDNF[EC] | Spohrs2022_FAAH[EC] | Obermanns2023_CNR1[EC] | Wang2025_biomarcadores[EC] | McWhirter2024_sexo[OB]*

### 14.2 Causalidade experimental do medo/estresse [ML — extrapolação por analogia]

Receptores canabinoides em amígdala e pré-frontal atuam na aprendizagem de medo em ratos (Kuhnert 2013)[ML].
A redução dos níveis de endocanabinoides intensifica ansiedade, estresse e medo em camundongos (Jenniches 2016)[ML].
A modulação endocanabinoide controla a ansiedade de longo prazo pós-estresse predatório (Lim 2016)[ML].
A fluoxetina facilita a extinção do medo via endocanabinoides amigdalares em camundongo (Gunduz-Cinar 2016)[ML].
O estresse agudo suprime inibição sináptica e aumenta ansiedade via eCB na BLA (Di 2016)[ML].
O colapso da sinalização eCB medeia o fortalecimento amigdalo-cortical induzido por estresse (Marcus 2020)[ML].
O ensaio de hidrólise de anandamida na BLA reduz a expressão da memória de medo (Morena 2019)[ML].
CB1 e FAAH no BNST modulam o comportamento ansioso conforme o contexto (Borges-Assis 2023)[ML].
A facilitação endocanabinoide no hipocampo ventral modula a ansiedade (Campos 2010)[ML].
Receptores CB2 medeiam efeito ansiolítico via monoacilglicerol (Ivy 2020)[ML].
A atividade constitutiva de CB2 atenua o comportamento induzido por estresse (Ribeiro 2021)[ML].
Moduladores de eCB melhoram ansiedade sem corrigir a expressão de medo no fenótipo de extinção fraca — dissociação crítica (Vimalanathan 2020)[ML].
A perda de SCP-2 reduz ansiedade e potencializa a extinção — camada de transporte lipídico intracelular (Liedhegner 2026)[ML].
CB1 hipocampal interage com privação de sono REM no comportamento (Azizi 2025)[ML].
Sexo e modalidade de estressor modulam a dinâmica corticolímbica de eCB sob estresse agudo (Vecchiarelli 2022)[ML].
Uma nova via FABP5–CB2 foi identificada no córtex — transporte intracelular como alvo (Uzuneser 2023)[ML].

*Kuhnert2013_CB1[ML] | Jenniches2016_reducao[ML] | Lim2016_predador[ML] | GunduzCinar2016_fluoxetina[ML] | Di2016_inibicao[ML] | Marcus2020_colapso[ML] | Morena2019_FAAH[ML] | BorgesAssis2023_BNST[ML] | Campos2010_hipocampo[ML] | Ivy2020_CB2[ML] | Ribeiro2021_CB2basal[ML] | Vimalanathan2020_dissociacao[ML] | Liedhegner2026_SCP2[ML] | Azizi2025_REM[ML] | Vecchiarelli2022_sexo[ML] | Uzuneser2023_FABP5[ML]*

### 14.3 Arquitetura e revisões estruturais (conceito, não evidência primária adicional)

O sistema endocanabinoide e o cérebro — síntese fundacional (Mechoulam 2013)[OB].
Revisão geral atualizada da arquitetura do ECS (Lu 2021)[OB].
As interações neurobiológicas estresse×ECS em síntese estrutural central (Morena 2016)[OB].
A evidência translacional do ECS em estresse e humor (Hill 2013)[OB], os efeitos neurocomportamentais do estresse (Hill 2010)[OB] e o feedback negativo glicocorticoide mediado por eCB (Hill 2012)[OB] formam a tríade da ponte B2.
ECS, estresse e eixo HPA em revisão dedicada (Micale 2018)[OB].
Os estudos HUMANOS de ECS em transtornos do humor revistos em separado da camada animal (Garani 2021)[OB].
As interações endocanabinoide–noradrenérgicas na extinção (Warren 2022)[OB].
O ECS como sistema vigilante da homeostase e da qualidade de vida (de Melo Reis 2021)[OB].
eCB na aquisição do medo contextual — consolidação em revisão pré-clínica (Balogh 2019)[OB].
eCB em hipocampo e amígdala na memória emocional e plasticidade (Segev 2018)[OB].
Depressão e antidepressivos sobre o sistema endocanabinoide — elo fármaco×eCB como sinal (Dragon 2024)[OB].
Endocanabinoides, depressão e resistência ao tratamento (Rosa 2025)[OB].
Visão geral atual de depressão maior×ECS (Zarazúa-Guzmán 2024)[OB].

*Mechoulam2013_fundacao[OB] | Lu2021_review[OB] | Morena2016_interacoes[OB] | Hill2013_translacional[OB] | Hill2010_neurocomp[OB] | Hill2012_feedback[OB] | Micale2018_HPA[OB] | Garani2021_humanos[OB] | Warren2022_NA[OB] | deMeloReis2021_homeostase[OB] | Balogh2019_contextual[OB] | Segev2018_hipocampo[OB] | Dragon2024_farmaco[OB] | Rosa2025_resistencia[OB] | ZarazuaGuzman2024_overview[OB]*

### 14.4 Interfaces declaradas (B12 desenvolvimento; B1 PUFA)

Estresse precoce e desenvolvimento do ECS em regulação bidirecional sexo- e região-dependente — ponte trauma (Goldstein Ferber 2021)[OB].
PUFAs dietéticos e exercício com ações dinâmicas sobre endocanabinoides — interface sem invasão do molecular de B1 (Park 2022)[OB].

*GoldsteinFerber2021_desenvolvimento[OB] | Park2022_interface[OB]*

### 14.5 Camada exógena (via 10 — isolada por regra 1)

A modulação canabinoide (THC) da ativação corticolímbica durante a extinção em adultos saudáveis entra APENAS como camada translacional exógena: não sustenta nenhum claim do núcleo endógeno (Zabik 2023)[EC].

*Zabik2023_exogena[EC]*

## BLOCO_15 — DEZ REGRAS FUNDADORAS FIXADAS (B13-REGRA-01..10) E EXPOSIÇÕES DA RODADA

[[AT 2026-09-09]] Regras do GPM oficial (M00), promovidas a canônicas:

- **B13-REGRA-01 (endógeno ≠ exógeno):** THC/CBD/cannabis/entourage ficam na camada translacional separada (via 10); nenhum claim do núcleo deriva de exógenos.
- **B13-REGRA-02 (desregulação SELETIVA, não queda global):** a meta mais recente mostra AEA/PEA ↑ na TDM com 2-AG/OEA sem alteração consistente — o slogan "deficiência de eCB = doença" está proibido.
- **B13-REGRA-03 (periférico ≠ diagnóstico):** eCB periféricos são biomarcadores mecanísticos/estratificadores potenciais; heterogeneidade (sexo, estado, medicação, método, matriz) impede uso diagnóstico.
- **B13-REGRA-04 (TEPT = interface, não centro):** não infla a evidência de TDM/TAG.
- **B13-REGRA-05 (animal ≠ clínica):** "anxiety-like/depression-like" em modelo não é clínica; toda causalidade animal leva `[ML]` + extrapolação.
- **B13-REGRA-06 (reviews = arquitetura):** revisões estruturais contam como conceito, não como evidência primária adicional.
- **B13-REGRA-07 (causalidade é experimental e regional):** amígdala/mPFC/hipocampo/BNST/septo-habênula — não valida intervenção clínica.
- **B13-REGRA-08 (exercício/PUFA = interface):** Meyer é CORE humano; os demais, interface documentada.
- **B13-REGRA-09 (sandbox):** preprint sem versão confirmada e abstract de congresso NÃO entram (Spohrs-preprint só entrou quando a versão publicada foi localizada).
- **B13-REGRA-10 (multi-tag permitida):** CORE humano + SUPPORT experimental convivem com identidades separadas.

**Exposições desta rodada:** (a) seis chaves do insumo divergiam do artigo real ao PMID — "Cota 2008"=de Melo Reis 2021, "Bedse 2017"=Borges-Assis 2023, "Mazurka 2024"=McWhirter 2024, "Gray 2015"=Gunduz-Cinar 2016, "Gamelin 2012"=Heyman 2012, "Zabik 2024"=Zarazúa-Guzmán 2024 — todas normalizadas com alias; (b) **falso mapeamento "Spohrs 2021"** (o PMID apontado é um VÍDEO NEUROCIRÚRGICO de fístula carótido-cavernosa) → EXC, exposto; o Spohrs real entrou pela versão publicada de 2022; (c) **"Segev 2018"** do dossiê resolvia Șerban 2025 (genérico, BAIXO) — o Segev real (hipocampo/amígdala, Neuropsychopharmacology) foi localizado por busca; (d) o **[G1] "McWhirter (sexo feminino)"** era exatamente a âncora rotulada "Mazurka" — RESOLVIDO; (e) o **[G1] "Zabik-RCT"** é o estudo THC×extinção em humanos — RESOLVIDO na camada exógena (via 10); (f) **Ibarra-Lecue** já estava vigente na V1 (REF_IBARRALECUE_2018) — removido da lista de pendências; (g) "Hill 2009 (19903506)" é Hill 2010 distinto do REF_HILL_2009 vigente — entrou com identidade corrigida.

**[G1] mantidos:** Bloemhof-Bris (ECT×eCB) não localizada; McLaughlin ×3 (pPFC/coping) não indexadas; "Gunduz-Cinar 2012" não resolvida; a Mazurka REAL (eCB×trauma infantil×hipocampo); GWAS eCB×psiquiatria; circuitos ECS humanos in vivo; réplica da desregulação seletiva em coortes independentes; NAO-IDX declarados (Liu-chinês, Saito-SciELO, Wang-congresso).

"""
doc=doc.replace(anc, B+anc)
linha="| Microbiota→SEC causal | FMT transfere fenótipo | alto em modelo [ML] |"
assert doc.count(linha)==1
doc=doc.replace(linha, linha+"""
| [AT] Causalidade experimental medo/estresse | CB1 amigdala/mPFC; colapso eCB→fortalecimento amigdalo-cortical; dissociação ansiedade×expressão de medo | alto em modelo [ML] |
| [AT] Humano endógeno | FAAH rs324420×recall extinção; exercício↑eCB/BDNF; sexo feminino revisado | médio (associativo/marcador) |
| [AT] Revisões estruturais | Mechoulam/Lu/Morena/Hill×3 — arquitetura ECS×estresse | alto conceitual (regra 6) |
| [AT] Interfaces | Desenvolvimento/ELS (Goldstein Ferber); PUFA/exercício (Park) | médio (interface) |
| [AT] Camada exógena (via 10) | THC×extinção humano — isolada por regra 1 | emergente (isolada) |""")
i=doc.index("> **Canônica v1 (Rodada 3).**")
fim=doc.index("é pendência do avaliador externo.")+len("é pendência do avaliador externo.")
doc=doc.replace(doc[i:fim],"""> **Canônica v2 (Rodada 4 — [AT] 2026-09-09).** Reconciliação de insumo externo auditado
> ref a ref (P-7): ENTRA 40 / BAIXO 19 / EXC 4. Camadas núcleo/experimental/exógena
> preservadas (regra 1); dez regras fundadoras fixadas no BLOCO 15; seis exposições de
> divergência de chave + um falso mapeamento explícito + um falso par Segev/Șerban.
> [G1] resolvidos: McWhirter, Zabik-RCT, Spohrs-versão-publicada; Ibarra-Lecue já vigente.
> Sem PMID no texto; farmacologia exógena = sinal isolado (P20). 2ª verificação
> independente (P-6, avaliador cego) permanece pendência — cobrindo levas [AT] B1–B16.""")
assert doc.count("corte 2026-09-07")==1
doc=doc.replace("corte 2026-09-07","corte 2026-09-09 (rodada [AT])")
# saneamento: apenas a exposição (g) continha um número a remover; códigos de fármaco (JNJ-/PF-) e rs-ids são legítimos
doc=doc.replace('"Hill 2009 (19903506)" é Hill 2010','"Hill 2009" (segundo registro do dossiê) é Hill 2010')
_chk=re.sub(r'\brs\d+\b','',doc)
_chk=re.sub(r'(?<=-)\d{7,9}','',_chk)
_hits=re.findall(r'\d{7,9}', _chk)
assert not _hits, _hits[:10]
open(V2,'w',encoding='utf-8').write(doc)
print("V2 palavras:", len(doc.split()))
import json
R=json.load(open(BASE+'producao/insumos/b13_refs_data.json'))
ESP={"REF_GUNDUZCINAR_2016":"(Gunduz-Cinar 2016)","REF_DEMELOREIS_2021":"(de Melo Reis 2021)","REF_BORGESASSIS_2023":"(Borges-Assis 2023)","REF_MCWHIRTER_2024":"(McWhirter 2024)","REF_GOLDSTEINFERBER_2021":"(Goldstein Ferber 2021)","REF_ZARAZUAGUZMAN_2024":"(Zarazúa-Guzmán 2024)","REF_LIEDHEGNER_2026":"(Liedhegner 2026)","REF_GARANI_2021":"(Garani 2021)","REF_WARREN_2022":"(Warren 2022)","REF_MORENA_2019":"(Morena 2019)","REF_MORENA_2016":"(Morena 2016)","REF_HILL_2010":"(Hill 2010)","REF_HILL_2012":"(Hill 2012)","REF_LU_2021":"(Lu 2021)","REF_VECCHIARELLI_2022":"(Vecchiarelli 2022)","REF_OBERMANNS_2023":"(Obermanns 2023)","REF_UZUNESER_2023":"(Uzuneser 2023)"}
falt=[]
for r in R:
    rid=r['id_referencia_interna']; tag=r['desenho_estudo'][1:3]
    e=ESP.get(rid) or f"({rid[4:].rsplit('_',1)[0].capitalize()} {rid.rsplit('_',1)[1]})"
    if f"{e}[{tag}]" not in doc: falt.append((rid,e))
print("faltantes:", falt)
