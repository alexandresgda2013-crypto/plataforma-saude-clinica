# B13 — Sistema Endocanabinoide na Ansiedade e Depressão
## Briefing Científico Abrangente: Fisiopatologia Estabelecida + Ciência de Fronteira

**ID canônico do mecanismo:** `sistema_endocanabinoide` (B13 — numeração própria de Gabriel)
**Escopo:** ansiedade e depressão (transtorno depressivo maior, TAG, transtorno de ansiedade social, componente ansioso do TEPT)
**Data de compilação:** setembro de 2026

---

## 0. Nota metodológica (leia antes de usar este documento)

Mesma metodologia aplicada ao briefing de B9: busca ativa na literatura (PubMed/PMC, ScienceDirect, Nature, Science, NEJM, bioRxiv/medRxiv quando sinalizado como pré-print) — não memória treinada. Cada PMID na Seção 9 foi confirmado individualmente por mim visualizando a página do PubMed/PMC correspondente. Trate esta lista como **Fase 1 — pré-PQ-09A**.

Uma exceção fica registrada com transparência: o artigo de Juhász et al. (2009) sobre o gene CNR1 e neuroticismo/depressão aparece de forma consistente em três fontes independentes (repositório institucional da Universidade de Manchester, página de pesquisa da mesma universidade, e SNPedia — banco de dados especializado em associações PMID↔SNP) com PMID 19242408, mas eu não consegui abrir diretamente a página do PubMed para essa confirmação final (bloqueio técnico da ferramenta de busca). Incluí essa referência na Seção 9 num bloco separado, sinalizada como "alta confiança via fonte secundária — não reconfirmada diretamente", em vez de misturá-la com as demais. Recomendo que a verificação PQ-09A trate esse item com prioridade.

Princípios inalterados em relação ao briefing de B9: nenhum PMID inventado; achados negativos mantidos (ex.: o ensaio de PF-04457845 que falhou para dor); extrapolação sinalizada como extrapolação; espécie e nível de evidência sempre indicados.

---

## 1. Nomenclatura molecular e IDs canônicos

### 1.1 Ligantes endógenos e receptores
| Termo | Sigla/gene | Observação |
|---|---|---|
| Anandamida (N-araquidonoiletanolamina) | AEA | ligante endógeno, agonista parcial de CB1 |
| 2-araquidonoilglicerol | 2-AG | ligante endógeno, agonista pleno de CB1 e CB2, mais abundante no SNC |
| Receptor canabinoide tipo 1 | CB1 / CNR1 | predominantemente neuronal, pré-sináptico, denso em regiões límbicas |
| Receptor canabinoide tipo 2 | CB2 / CNR2 | predominantemente imune/glial (micróglia), historicamente tido como "periférico" |
| Receptor de potencial transitório vanilóide 1 ("canabinoide ionotrópico") | TRPV1 | também ativado por AEA em altas concentrações |
| Receptor órfão acoplado à proteína G 55 | GPR55 | candidato a "CB3", ligantes incluem lisofosfatidilinositol |
| Receptores ativados por proliferadores de peroxissomo | PPAR-α/γ | alvos nucleares de alguns canabinoides e seus metabólitos |

### 1.2 Síntese e degradação (o "circuito de sinalização sob demanda")
| Termo | Sigla/gene | Função |
|---|---|---|
| N-acil-fosfatidiletanolamina fosfolipase D | NAPE-PLD | síntese de AEA |
| Diacilglicerol lipase α/β | DAGLα/β | síntese de 2-AG |
| Hidrolase de amidas de ácidos graxos | FAAH | degrada AEA (e outras N-aciletanolaminas: OEA, PEA) |
| Monoacilglicerol lipase | MAGL | degrada 2-AG (via principal) |
| Proteínas de ligação a ácidos graxos | FABPs (incl. FABP3, FABP5, FABP7) | transportadoras intracelulares de AEA até a FAAH — alvo farmacológico emergente |

### 1.3 Conceitos de circuito e sinalização
| Termo | Observação |
|---|---|
| Sinalização retrógrada | eCBs sintetizados pós-sinapticamente, agem em CB1 pré-sináptico |
| DSI (depolarization-induced suppression of inhibition) | supressão retrógrada de liberação de GABA — ponto de crosstalk direto com B5 |
| DSE (depolarization-induced suppression of excitation) | supressão retrógrada de liberação de glutamato — idem |
| LTD endocanabinoide | depressão de longo prazo mediada por eCB, relevante à extinção do medo |
| "Tônus endocanabinoide" | nível basal de sinalização eCB; hipoteticamente reduzido em estados de estresse crônico/ansiedade |
| N-aciletanolaminas correlatas | OEA (oleoiletanolamida), PEA (palmitoiletanolamida) — não se ligam a CB1/CB2 com afinidade relevante, mas compartilham via de degradação (FAAH) e são frequentemente medidas junto com AEA em estudos periféricos |

### 1.4 Genética
| Termo | Observação |
|---|---|
| FAAH C385A (rs324420) | polimorfismo mais estudado; alelo A ("perda de função") associado a maior sinalização de AEA |
| CNR1 rs1049353, rs806380, rs7766029, rs2180619, entre outros | SNPs associados de forma inconsistente a traços de personalidade, dependência de cannabis e sintomas depressivos conforme o SNP e a população |
| Haplótipos CNR1 (H1–H5) | descritos em contexto metabólico (resposta de HDL-colesterol), não diretamente em ansiedade/depressão |

---

## 2. Fisiopatologia estabelecida

### 2.1 O modelo geral: "tampão" contra o estresse
A tese central, sustentada por múltiplas revisões independentes ao longo de mais de uma década, é que o sistema endocanabinoide (SEC) funciona como um **sistema de retroalimentação que amortece (buffers) a resposta ao estresse e regula o humor**, e que déficits na sinalização endocanabinoide favorecem respostas depressivas e ansiogênicas, enquanto o aumento farmacológico dessa sinalização produz efeitos ansiolíticos e antidepressivos em modelos pré-clínicos (PMID 19839936; PMID 26068727; PMID 27130852). Essas ações protetoras concentram-se em estruturas corticolímbicas — particularmente amígdala e córtex pré-frontal.

### 2.2 CB1: genética, knockouts e comportamento
Camundongos com deleção genética completa do receptor CB1 (knockout de Cnr1) exibem, de forma consistente entre diferentes linhagens geradas independentemente, comportamento do tipo ansioso e maior propensão a comportamento anedônico/desesperançado após estresse crônico leve. Um estudo mostrou esse efeito como **dependente do sexo**: machos knockout apresentaram maior comportamento ansioso do que fêmeas knockout comparadas a seus respectivos controles selvagens — a ooforectomia não reverteu o efeito em fêmeas, mas ambos os sexos foram sensíveis ao antagonista SR141716A (rimonabanto) quando adultos com desenvolvimento normativo (PMID 26684509). Isso é um lembrete importante contra generalizar "menos CB1 = mais ansiedade" sem considerar sexo e desenvolvimento.

Em humanos, o antagonista de CB1 rimonabanto — desenvolvido e comercializado brevemente para obesidade — foi **retirado do mercado** por aumentar risco de depressão e ideação suicida, um dos achados clínicos mais diretos (embora "acidental", via evento adverso de outro fármaco) ligando bloqueio de CB1 a piora do humor em humanos.

### 2.3 FAAH e anandamida: o eixo mais estudado mecanisticamente
Este é o bloco de evidência mais sólido e mais bem replicado do mecanismo B13, com tradução clara de camundongo para humano:

- Em camundongos, a inibição farmacológica de FAAH (elevando AEA) facilita a extinção do medo e é bloqueada por antagonista de CB1 infundido diretamente na amígdala — localizando o efeito.
- Em humanos, portadores do alelo de baixa expressão de FAAH (385A; rs324420) mostraram **habituação mais rápida da reatividade da amígdala a estímulos de ameaça** e escores mais baixos no traço de personalidade "reatividade ao estresse" (PMID 22688188 — Gunduz-Cinar et al. 2012, o estudo-ponte entre camundongo e humano nesse eixo).
- O estudo de imagem genética fundador desse campo (Hariri et al. 2009) mostrou que portadores do alelo 385A têm reatividade de amígdala reduzida a faces de ameaça e correlação diminuída entre reatividade amigdalar e ansiedade traço (PMID 19103437).
- Um ensaio clínico **randomizado, controlado, de medicina experimental** em humanos saudáveis (não apenas observacional) testou inibição farmacológica de FAAH e encontrou resposta fisiológica de estresse atenuada durante um teste de estresse psicossocial, associada a concentrações mais altas de anandamida (PMID 31590924 — Mayo et al. 2020). O mesmo grupo replicou, em humanos e camundongos no mesmo artigo, que anandamida elevada tem efeito protetor sobre comportamentos relacionados a medo e estresse (PMID 30120421).
- Em adolescentes (estudo ABCD, n=4.811, dados longitudinais), a variante FAAH C385A associou-se a menor risco de sintomas de ansiedade e depressão e a atividade neural alterada relacionada a ameaça/recompensa — um dos maiores estudos humanos já feitos sobre esse polimorfismo especificamente em sintomas de ansiedade/depressão (PMID 38423255).

Vale registrar um contraponto de rigor: nem todo estudo sobre FAAH C385A e emoção encontrou o mesmo padrão — um estudo de resposta de sobressalto (startle) encontrou direção diferente da esperada para reatividade emocional, e um estudo em militares não encontrou associação entre FAAH rs324420 (isolado ou em interação com CRHR1/CNR1) e sintomas de ansiedade/TEPT pós-deployment, embora trauma na infância tenha permanecido como covariável significativa em todos os modelos. Isso sugere que o efeito do polimorfismo é robusto em paradigmas de neuroimagem/fisiologia mas mais inconsistente em medidas de autorrelato — um padrão, aliás, coerente com a própria natureza do sistema (regulação implícita/automática de circuitos de ameaça, não necessariamente acessível à introspecção verbal).

### 2.4 2-AG: um papel parcialmente distinto de AEA
Menos estudado que AEA em humanos, mas emergindo como biologicamente distinto: em modelos animais, a prevenção da degradação de 2-AG (via bloqueio de MAGL) também produziu efeito antidepressivo-símile e aumento de neurogênese, e camundongos com deleção de DAGLα (enzima de síntese de 2-AG) mostraram níveis reduzidos de endocanabinoides no hipocampo, neurogênese prejudicada e comportamento do tipo ansioso.

---

## 3. Crosstalk mecanístico prioritário com outros mecanismos B

### 3.1 B13 × B2 (Eixo HPA-Cortisol)
O SEC está posicionado estruturalmente para regular o eixo HPA: a sinalização endocanabinoide participa da alça de retroalimentação negativa do cortisol, e evidências indicam que glicocorticoides podem induzir liberação rápida de endocanabinoides em neurônios do núcleo paraventricular do hipotálamo e da amígdala como parte de seus efeitos não-genômicos rápidos — um mecanismo pelo qual o cortisol "usa" o SEC como braço executor de curto prazo. Esse é provavelmente o crosstalk mais antigo e mais bem estabelecido na literatura de eCB e estresse, presente de forma consistente nas revisões fundamentais da área (PMID 19839936; PMID 26068727).

### 3.2 B13 × B1 (Neuroinflamação)
O receptor CB2, embora historicamente descrito como "periférico", está presente em micróglia e é regulado para cima em contextos neuroinflamatórios, onde agonistas de CB2 promovem fenótipo microglial anti-inflamatório (via PPAR-γ e supressão de NF-κB, entre outras vias). Um estudo recente em modelo pré-clínico combinando periodontite (fonte de inflamação sistêmica) com estresse crônico moderado encontrou alterações no fenótipo morfológico/inflamatório da micróglia associadas a redução nos níveis das enzimas metabólicas do SEC (NAPE-PLD, DAGL, MAGL) no córtex frontal, junto com alterações em CB1 e vias de sinalização intracelular (PI3K/Akt/ERK1/2) — evidência direta e recente do acoplamento B13×B1 (PMID 39245706, J Neuroinflammation 2024).

### 3.3 B13 × B5 (GABA/Glutamato)
Este crosstalk não é uma hipótese — é o **mecanismo celular fundamental** de como o SEC opera: a sinalização retrógrada eCB (DSI/DSE, ver Seção 1.3) é, por definição, supressão da liberação de GABA ou glutamato mediada por CB1 pré-sináptico. Em outras palavras, B13 não age "ao lado" de B5 — atua como um modulador fino, sináptico e em tempo real, da própria neurotransmissão GABAérgica/glutamatérgica que B5 descreve. Isso tem implicação prática para o pipeline: qualquer NT-05 (GABA/glutamato) que não mencione modulação endocanabinoide retrógrada está descrevendo o circuito de forma incompleta.

### 3.4 B13 × B4 (Monoaminas)
O canabidiol (CBD) — apesar de não ser um agonista direto relevante de CB1/CB2 — exerce parte de seu efeito ansiolítico via ativação parcial do receptor serotoninérgico 5-HT1A, criando uma ponte farmacológica direta entre B13 e B4. Estudos em camundongos knockout mostraram que o efeito ansiolítico do CBD depende de CB1 (ausente em CB1-KO, presente em CB2-KO e GPR55-KO), mesmo quando o mecanismo primário envolve 5-HT1A — sugerindo uma interação, não uma via isolada.

### 3.5 B13 × B3 (BDNF / Neuroplasticidade)
Camundongos com deleção de DAGLα (síntese de 2-AG) apresentam neurogênese hipocampal prejudicada junto com comportamento ansioso; inversamente, o bloqueio da degradação de 2-AG (inibição de MAGL) aumenta neurogênese e produz efeito antidepressivo-símile — posicionando a sinalização de 2-AG como reguladora upstream de neuroplasticidade hipocampal, o desfecho central que B3 descreve.

---

## 4. Ciência de fronteira

### 4.1 Genômica populacional em larga escala
O estudo ABCD (PMID 38423255) já citado na Seção 2.3 é o melhor exemplo atual: coorte longitudinal de quase 5.000 jovens atravessando a transição para a adolescência, ligando genótipo FAAH a trajetórias de sintomas de ansiedade/depressão e a função cerebral relacionada a ameaça/recompensa ao longo do tempo — um desenho que praticamente não existia há uma década nesse campo específico.

### 4.2 Biomarcadores periféricos: um quadro genuinamente misto (não hype)
A literatura sobre níveis plasmáticos/séricos de AEA e 2-AG em pacientes com TDM é heterogênea entre estudos individuais — alguns encontram AEA/2-AG reduzidos em depressão maior sem tratamento, outros encontram elevação em coortes mistas (tratados + não tratados), e a duração/gravidade do episódio parece interagir com a direção do efeito. A síntese mais recente e mais rigorosa que localizei é uma **meta-análise de 2026** especificamente sobre esse tema: encontrou AEA e palmitoiletanolamida (PEA) circulantes significativamente **mais altos** em pacientes com TDM comparado a controles (AEA: SMD=0,32; PEA: SMD=0,35), mas **nenhuma diferença significativa** para 2-AG ou oleoiletanolamida (OEA) (PMID 42431383). Isso contradiz parcialmente relatos anteriores de "AEA baixa em depressão" — um bom exemplo de por que meta-análise recente deve pesar mais que estudos individuais mais antigos e menores nesse tópico específico. Uma revisão sistemática separada (17 estudos, 359 pacientes com TDM) chegou a uma leitura complementar: 2-AG parece acompanhar gravidade/cronicidade da depressão, enquanto AEA correlaciona-se inversamente com sintomas de ansiedade (Fuentes et al. 2024, *BMC Psychiatry* 24:551, DOI 10.1186/s12888-024-05986-8 — não consegui confirmar o PMID individualmente nesta rodada; cito por DOI, não incluído na lista numerada da Seção 9).

### 4.3 O "eixo endocanabinoide do exercício" (runner's high)
Uma revisão sistemática de ensaios clínicos em humanos (21 estudos elegíveis de 278 triados) encontrou aumento de endocanabinoides após exercício agudo em 14 de 17 estudos — consistente entre corrida, natação e musculação, e presente tanto em pessoas saudáveis quanto com condições de saúde preexistentes —, ao passo que exercício de resistência crônico/prolongado tende a **reduzir** os níveis basais, com consequências neurobiológicas ainda pouco claras (PMID 35081831). Um estudo controlado com bloqueio farmacológico de receptores opioides (naltrexona) mostrou que euforia e ansiólise induzidas por corrida **persistem mesmo com os opioides bloqueados**, mas são acompanhadas por elevação de AEA e 2-AG — evidência de que o "barato do corredor" depende mais do SEC do que das endorfinas, contrariando a crença popular. Esse é um ponto de interesse direto para orientação de estilo de vida em protocolos integrativos.

### 4.4 Desenvolvimento de fármacos: um estudo de caso sobre sucesso e fracasso translacional
Vale documentar com cuidado porque é exatamente o tipo de contexto que evita ingenuidade terapêutica:
- **PF-04457845** (inibidor seletivo de FAAH, Pfizer): reduziu atividade de FAAH em >96% em humanos e não causou eventos adversos do tipo canabinoide, mas **falhou** em produzir analgesia clinicamente relevante em osteoartrite de joelho (estudo interrompido por futilidade na análise interina) (PMID 22727500) — mostrando que "aumentar anandamida" nem sempre se traduz no desfecho clínico esperado, mesmo com engajamento de alvo confirmado. Em contraste, o mesmo composto **reduziu** sintomas de abstinência e uso de cannabis em homens dependentes, em ensaio fase 2a controlado por placebo (PMID 30528676) — eficácia dependente do desfecho estudado, não generalizável de uma indicação para outra. Sob o nome JZP150, esse composto avançou para fase 2 em TEPT (patrocinado pela Jazz Pharmaceuticals), mas o desenvolvimento foi **descontinuado em dezembro de 2023** — um desfecho negativo recente que deveria ser mencionado em qualquer avaliação honesta do potencial clínico de inibidores de FAAH para ansiedade/TEPT.
- **BIA 10-2474** (inibidor de FAAH, Bial/Biotrial): um ensaio de fase 1 na França em 2016 resultou na morte de um voluntário saudável e dano neurológico grave em quatro outros. Análise proteômica subsequente revelou que, diferente do PF-04457845, o BIA 10-2474 inibia **múltiplas lipases fora do alvo** (não apenas FAAH), incluindo PNPLA6 — associada a neurodegeneração induzida por compostos organofosforados —, e alterava substancialmente o metabolismo lipídico em neurônios corticais humanos, enquanto o PF-04457845 não produzia esse efeito (PMID 28596366). A FDA concluiu que essa toxicidade era **específica do composto BIA 10-2474**, não uma propriedade de classe dos inibidores de FAAH. É um caso importante para qualquer discussão sobre segurança de moduladores farmacológicos do SEC — a mensagem correta não é "inibidores de FAAH são perigosos", mas "seletividade de alvo importa muito mais do que a classe farmacológica".

---

## 5. Intervenções com ancoragem no sistema endocanabinoide (relevância clínica/ortomolecular)

### 5.1 Canabidiol (CBD) — o composto com mais evidência clínica direta em humanos
Uma revisão sistemática de 2024 (11 ECRs elegíveis de 284 triados, 2013–2023) encontrou que CBD pode reduzir ansiedade com efeitos adversos mínimos comparado a placebo, mas resultados **frequentemente contraditórios** entre estudos quanto a dose e tipo de transtorno de ansiedade, com recomendação explícita de mais ECRs metodologicamente robustos antes de conclusões firmes (PMID 39598172). Uma meta-análise separada do mesmo ano, com 8 estudos elegíveis (316 participantes), encontrou efeito substancial do CBD sobre ansiedade (Hedges' g = -0,92), cobrindo TAG, transtorno de ansiedade social e TEPT, mas alerta para o tamanho amostral limitado da evidência disponível (PMID 38924898). Uma revisão mais antiga e amplamente citada (Blessing et al. 2015) já havia sintetizado evidência pré-clínica robusta para múltiplos transtornos de ansiedade administrados de forma aguda, mas apontou escassez de dados sobre dosagem crônica — um problema que, dez anos depois, ainda aparece nas revisões mais recentes (PMID 26341731). Uma revisão focada especificamente no uso clínico (8 artigos: 6 ECRs pequenos, 1 série de casos, 1 relato de caso) não encontrou nenhum estudo sobre transtorno de pânico, fobia específica, ansiedade de separação ou TOC — mapeando claramente onde a lacuna de evidência está mais aberta (PMID 31866386).

### 5.2 Inibidores de FAAH — status de desenvolvimento (não uma opção clínica disponível)
Ver Seção 4.4. Não há inibidor de FAAH aprovado para uso clínico em ansiedade ou depressão até onde localizei; o programa mais avançado (JZP150/PF-04457845) foi descontinuado. Isso deve ser comunicado com clareza a qualquer usuário do sistema — o mecanismo é validado cientificamente, mas não há produto farmacêutico correspondente disponível.

### 5.3 Exercício físico
Ver Seção 4.3. A elevação de AEA/2-AG induzida por exercício agudo é um dos achados mais replicados e mais diretamente acionáveis desta seção inteira — com a ressalva de que exercício crônico/prolongado parece ter efeito oposto sobre os níveis basais, o que sugere que a variável relevante para orientação clínica é provavelmente "sessões agudas regulares" mais do que "volume total acumulado", embora isso ainda não tenha sido testado diretamente como hipótese em desfecho de ansiedade/depressão.

---

## 6. Termos de busca alternativos (para aprofundamento futuro / expansão da NT-13)

- endocannabinoid tone + stress OR resilience
- FAAH C385A + amygdala OR fear extinction OR PTSD
- 2-arachidonoylglycerol OR 2-AG + depression OR neurogenesis
- monoacylglycerol lipase MAGL inhibitor + depression OR anxiety
- CB2 receptor + microglia + depression
- endocannabinoid + HPA axis + rapid glucocorticoid signaling
- cannabidiol 5-HT1A + anxiety
- FAAH inhibitor + clinical trial + safety
- peripheral endocannabinoid + biomarker + major depressive disorder
- GPR55 + anxiety OR depression (candidato a "CB3", pouco explorado neste briefing)
- fatty acid binding protein FABP + anandamide transport (alvo farmacológico emergente)
- oleoylethanolamide OR palmitoylethanolamide + mood
- endocannabinoid + sex differences + estrogen
- endocannabinoid + gut microbiome (ver Seção 7)
- mitochondrial CB1 receptor (achado recente de CB1 em membranas mitocondriais neuronais — não aprofundado aqui, ver Seção 7)

## 7. Áreas adjacentes subexploradas

1. **Eixo microbiota-endocanabinoide** — existe literatura estabelecida sobre o SEC regulando permeabilidade intestinal e inflamação de baixo grau, e sobre a microbiota modulando expressão de receptores CB no epitélio intestinal, mas eu não localizei, neste ciclo de busca, estudos que fechem esse círculo diretamente até ansiedade/depressão da forma como o eixo microbiota-mitocôndria foi mapeado no briefing de B9. Fica como pendência explícita para rodada futura.
2. **CB1 mitocondrial** — há relatos na literatura de receptores CB1 funcionais na própria membrana mitocondrial neuronal (não apenas na membrana plasmática), regulando respiração celular — um ponto de crosstalk direto e ainda pouco explorado com B9 (disfunção mitocondrial) que não aprofundei aqui por escopo, mas que vale nota para expansão futura da NT-13.
3. **GPR55 ("CB3")** — mencionado en passant em vários artigos como candidato a terceiro receptor canabinoide relevante ao comportamento emocional, mas com literatura específica em ansiedade/depressão muito mais rala do que CB1/CB2.
4. **Diferenças de sexo além de CB1-KO** — o achado de dimorfismo sexual em camundongos CB1-KO (Seção 2.2) sugere que boa parte da literatura de FAAH/CB1 em humanos (majoritariamente amostras mistas ou masculinas) pode estar sub-representando efeitos específicos de sexo — relevante para individualização clínica.
5. **Interação com psicodélicos** — mencionada esporadicamente na literatura mais ampla de neuroplasticidade, mas não localizei, neste ciclo, estudos robustos testando diretamente a interação farmacológica SEC × psicodélicos clássicos em ansiedade/depressão.
6. **Entourage effect de fitocanabinoides menores** (CBG, CBN, terpenos) além de THC/CBD — mencionado com frequência em contexto comercial/popular, mas com base de evidência controlada em humanos, para ansiedade/depressão especificamente, que não localizei de forma consistente nesta busca.

## 8. Sinalizadores de extrapolação — o que é estabelecido vs. o que é hipótese de ponte

**Estabelecido com replicação humana (GRADE A/B plausível, sujeito à sua verificação PQ-09A):**
- Sinalização retrógrada eCB como mecanismo celular de DSI/DSE — bioquímica de circuito bem estabelecida (não é hipótese, é mecanismo demonstrado).
- FAAH C385A associado a reatividade de amígdala reduzida e habituação mais rápida a ameaça (replicado em múltiplos estudos de imagem genética independentes, incluindo uma coorte de quase 5.000 adolescentes).
- Inibição farmacológica de FAAH reduz reatividade fisiológica a estresse psicossocial agudo em humanos saudáveis (ensaio randomizado controlado, não apenas observacional).
- Retirada do rimonabanto do mercado por piora de humor/risco de suicídio em bloqueio de CB1 — evento clínico documentado, não modelo animal.
- CBD com efeito ansiolítico mensurável em meta-análises de ECRs, embora heterogêneo entre estudos e transtornos.
- Toxicidade específica do BIA 10-2474 (não de classe) — confirmada por perfil proteômico comparativo.

**Ciência de fronteira genuína, ainda preliminar nos termos dos próprios autores:**
- Biomarcadores periféricos de AEA/2-AG em TDM — direção do efeito ainda inconsistente entre estudos individuais; a meta-análise mais recente (2026) é o achado mais confiável disponível, mas cobre uma fração pequena da literatura publicada.
- Runner's high dependente de endocanabinoides (não endorfinas) — replicado em múltiplos estudos controlados, mas a tradução direta para "exercício como terapia SEC-mediada para ansiedade/depressão clínica" ainda não foi testada como hipótese primária de um ECR.
- Interação CBD × 5-HT1A × CB1 — mecanismo demonstrado em camundongos knockout; grau de tradução para humanos ainda não mapeado com a mesma granularidade.

**Extrapolação — ponte hipotética a partir de literatura de outra área ou de mecanismo celular geral, não achado direto em ansiedade/depressão:**
- Eixo microbiota-endocanabinoide como via específica para ansiedade/depressão — plausível por analogia com o eixo microbiota-mitocôndria (B9) e com literatura estabelecida de SEC intestinal, mas sem o fechamento direto que localizei para B9.
- CB1 mitocondrial como mecanismo unificador entre B13 e B9 — biologicamente plausível e mencionado na literatura, mas não testado diretamente como hipótese de ansiedade/depressão neste ciclo de busca.
- Entourage effect de fitocanabinoides menores — amplamente promovido em contexto comercial, com base controlada em humanos insuficiente para tratar como achado estabelecido.

---

## 9. Lista de PMIDs validados (verificados individualmente — não inventados)

### Revisões fundamentais / fisiopatologia geral
1. **19839936** — The endocannabinoid system and the treatment of mood and anxiety disorders.
2. **36831868** — Endocannabinoid System and Exogenous Cannabinoids in Depression and Anxiety: A Review.
3. **31714262** — Cannabinoids and the endocannabinoid system in anxiety, depression, and dysregulation of emotion in humans.
4. **26068727** — Morena M, Patel S, Bains JS, Hill MN (2016). Neurobiological Interactions Between Stress and the Endocannabinoid System. *Neuropsychopharmacology*.
5. **27130852** — Hill MN, Lee FS (2016). Endocannabinoids and Stress Resilience: Is Deficiency Sufficient to Promote Vulnerability? *Biol Psychiatry*.

### Genética, receptor CB1 e comportamento
6. **26684509** — Sex-dependence of anxiety-like behavior in cannabinoid receptor 1 (Cnr1) knockout mice.
7. **19103437** — Hariri AR et al. (2009). Divergent Effects of Genetic Variation in Endocannabinoid Signaling on Human Threat- and Reward-Related Brain Function. *Biol Psychiatry*.
8. **38423255** — Desai S et al. (2024). Genetic variation in endocannabinoid signaling: Anxiety, depression, and threat- and reward-related brain functioning during the transition into adolescence. *Behav Brain Res*. (estudo ABCD, n=4.811)

### FAAH, anandamida e extinção do medo
9. **22688188** — Gunduz-Cinar O et al. (2012). Convergent translational evidence of a role for anandamide in amygdala-mediated fear extinction, threat processing and stress-reactivity. *Mol Psychiatry*.
10. **30120421** — Mayo LM et al. (2020). Protective effects of elevated anandamide on stress and fear-related behaviors: translational evidence from humans and mice. *Mol Psychiatry*.
11. **31590924** — Mayo LM et al. (2020). Elevated Anandamide, Enhanced Recall of Fear Extinction, and Attenuated Stress Responses Following Inhibition of Fatty Acid Amide Hydrolase: A Randomized, Controlled Experimental Medicine Trial. *Biol Psychiatry*. (ECR em humanos)

### Canabidiol (CBD) — ensaios e revisões clínicas
12. **39598172** — de Faria Coelho C et al. (2024). The Impact of Cannabidiol Treatment on Anxiety Disorders: A Systematic Review of Randomized Controlled Clinical Trials. *Life*.
13. **26341731** — Blessing EM et al. (2015). Cannabidiol as a Potential Treatment for Anxiety Disorders. *Neurotherapeutics*.
14. **38924898** — Wang JY et al. (2024). Therapeutic potential of cannabidiol (CBD) in anxiety disorders: A systematic review and meta-analysis. *Psychiatry Research*.
15. **31866386** — Use of cannabidiol in anxiety and anxiety-related disorders.

### Inibidores de FAAH — desenvolvimento clínico e segurança
16. **22727500** — Efficient randomised, placebo-controlled clinical trial with PF-04457845... fails to induce effective analgesia in osteoarthritis of the knee. *(achado negativo para dor, engajamento de alvo confirmado)*
17. **30528676** — Efficacy and safety of a fatty acid amide hydrolase inhibitor (PF-04457845) in the treatment of cannabis withdrawal and dependence in men. *Lancet Psychiatry*.
18. **28596366** — Activity-based protein profiling reveals off-target proteins of the FAAH inhibitor BIA 10-2474. *Science*. (episódio de segurança de 2016)

### Exercício e endocanabinoides
19. **35081831** — Do Endocannabinoids Cause the Runner's High? Evidence and Open Questions.

### Biomarcadores periféricos e crosstalk com neuroinflamação
20. **42431383** — Neuroimmune lipidome dysregulation in major depressive disorder: A meta-analysis of peripheral endocannabinoid and N-acylethanolamine signaling. *(2026, síntese mais recente)*
21. **39245706** — Robledo-Montaña J et al. (2024). Microglial morphological/inflammatory phenotypes and endocannabinoid signaling in a preclinical model of periodontitis and depression. *J Neuroinflammation*.

### Referência de alta confiança via fonte secundária — não reconfirmada diretamente (ver Seção 0)
22. **19242408** *(não reconfirmado via página do PubMed nesta rodada — ver nota metodológica)* — Juhász G et al. (2009). CNR1 gene is associated with high neuroticism and low agreeableness and interacts with recent negative life events to predict current depressive symptoms. *Neuropsychopharmacology*, 34(8):2019-2027.

---

**Achados relevantes que localizei mas NÃO incluí acima por não ter confirmado um PMID individualmente:**
- Fuentes JJ et al. Peripheral endocannabinoids in major depressive disorder and alcohol use disorder: a systematic review. *BMC Psychiatry*. 2024;24(1):551. DOI 10.1186/s12888-024-05986-8 — revisão sistemática recente e diretamente relevante (17 estudos, 359 pacientes com TDM), citada em prosa na Seção 4.2, mas sem PMID confirmado nesta rodada de busca.
- Microglial cannabinoid receptor 2 and epigenetic regulation: Implications for the treatment of depression. *European Journal of Pharmacology*, vol. 995, artigo 177422, publicado em 15-05-2025. DOI não localizado diretamente; achei apenas via página institucional sem PMID exibido.
