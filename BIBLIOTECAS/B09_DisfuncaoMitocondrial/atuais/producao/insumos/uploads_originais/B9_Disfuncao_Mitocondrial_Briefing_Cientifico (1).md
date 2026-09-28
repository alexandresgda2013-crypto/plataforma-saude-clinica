# B9 — Disfunção Mitocondrial na Ansiedade e Depressão
## Briefing Científico Abrangente: Fisiopatologia Estabelecida + Ciência de Fronteira

**ID canônico do mecanismo:** `disfuncao_mitocondrial` (B9)
**Escopo:** ansiedade e depressão (transtorno depressivo maior e transtornos de ansiedade), com extensões pontuais a transtorno bipolar e esquizofrenia quando a literatura de depressão/ansiedade isolada é escassa (sinalizado explicitamente onde ocorre)
**Data de compilação:** setembro de 2026

---

## 0. Nota metodológica (leia antes de usar este documento)

Este briefing foi construído a partir de buscas ativas na literatura (PubMed/PMC, ScienceDirect, Nature, bioRxiv/medRxiv para pré-prints sinalizados como tal) — não de memória treinada. Cada PMID na Seção 9 foi individualmente confirmado por mim visualizando a página do PubMed/PMC correspondente (não apenas inferido de um DOI ou de uma citação de terceiros). Ainda assim, dado o histórico já registrado neste projeto de PMIDs fabricados ou mal atribuídos por IA, trate esta lista como **Fase 1 — pré-PQ-09A**: recomendo rodar sua verificação externa padrão antes de qualquer PMID entrar em JSON de produção ou GRADE A/B.

Princípios que segui:
- **Nenhum PMID foi inventado.** Onde encontrei um conceito relevante mas não consegui confirmar um PMID real (ex.: alguns artigos publicados em 2026 muito recentes, ainda não indexados no PubMed), descrevo o achado em prosa com DOI/periódico, mas **não** o incluí na lista de PMIDs validados.
- **Achados negativos foram mantidos.** Quando uma busca trouxe um estudo que não encontrou associação (ex.: haplogrupos mitocondriais e depressão), eu o incluí — omitir estudos negativos distorceria o quadro científico.
- **Extrapolação é marcada como extrapolação.** Seções inteiras (peptídeos derivados de mitocôndria, por exemplo) são hipóteses de ponte a partir de literatura de outras áreas (envelhecimento, Alzheimer, metabolismo) — não achados diretos em ansiedade/depressão. Isso está sinalizado explicitamente na Seção 8, não escondido no meio do texto.
- **Espécie e nível de evidência sempre indicados.** "Camundongos" ou "in vitro" nunca é apresentado como se fosse humano.

---

## 1. Nomenclatura molecular e IDs canônicos

### 1.1 Bioenergética / cadeia transportadora de elétrons (CTE) e OXPHOS
| Termo | Sigla/gene | Observação |
|---|---|---|
| Fosforilação oxidativa | OXPHOS | processo central do mecanismo |
| Complexo I (NADH:ubiquinona oxidorredutase) | subunidades NDUFV1, NDUFV2, NDUFS1, NDUFS7, genes mitocondriais MT-ND1–6 | alvo mais estudado em achados post-mortem |
| Complexo II (succinato desidrogenase) | SDH | ponto de conexão com o ciclo de Krebs |
| Complexo III (citocromo bc1) | MT-CYB | |
| Complexo IV (citocromo c oxidase) | COX, MT-CO1–3 | codificado pelo mtDNA — mais sensível a estresse psicológico em revisões sistemáticas |
| Complexo V (ATP sintase) | MT-ATP6/8 | |
| Potencial de membrana mitocondrial | ΔΨm | hiperpolarização documentada em fibroblastos de pacientes com TDM |

### 1.2 Genoma mitocondrial e dinâmica
| Termo | Sigla/gene |
|---|---|
| Número de cópias de DNA mitocondrial | mtDNAcn |
| DNA mitocondrial livre de células circulante | ccf-mtDNA / cf-mtDNA |
| Heteroplasmia | — |
| Haplogrupos mitocondriais | H, U, K, J, T, V, HV, etc. |
| Fissão mitocondrial | DRP1 (DNM1L), FIS1, MFF |
| Fusão mitocondrial | MFN1, MFN2, OPA1 |
| Biogênese mitocondrial | PGC-1α (PPARGC1A), NRF1, TFAM |
| Mitofagia (via PINK1/Parkin) | PINK1, PRKN (Parkin) |
| Receptores mitofágicos independentes de ubiquitina | BNIP3, NIX (BNIP3L), FUNDC1 |
| Poro de transição de permeabilidade mitocondrial | mPTP — ciclofilina D (PPIF), VDAC, ANT (incl. ANT2) |
| Uniportador de cálcio mitocondrial | MCU |
| Resposta a proteínas mal dobradas mitocondrial | UPRmt — ATF5, HSP60, ClpP |
| Proteína desacopladora 2 | UCP2 |

### 1.3 Sinalização mitocôndria → resto da célula/organismo
| Termo | Observação |
|---|---|
| DAMPs mitocondriais (mtDNA, cardiolipina, N-formil peptídeos) | ativam resposta imune inata quando liberados |
| Via cGAS–STING | detecta mtDNA citosólico |
| Inflamassoma NLRP3 | ativado por ROS mitocondrial e mtDNA oxidado |
| GDF-15 (mitocina) | biomarcador circulante de estresse energético mitocondrial |
| Peptídeos derivados de mitocôndria (MDPs) | humanina, MOTS-c, SHLP1–6 — **ver sinalizador de extrapolação na Seção 8** |
| SIRT3 | sirtuína mitocondrial, sensor de NAD+ |
| AMPK | sensor energético upstream de PGC-1α |

### 1.4 Conceitos de fronteira (nomenclatura específica)
- **Carga alostática mitocondrial (mitochondrial allostatic load, MAL)** — termo cunhado por Picard & McEwen.
- **Psicobiologia mitocondrial (mitochondrial psychobiology)** — campo emergente que estuda a mitocôndria como transdutora de experiência psicossocial.
- **Índice de saúde mitocondrial (Mitochondrial Health Index, MHI)** — composto proposto por Picard et al. combinando atividade de complexos I–IV e conteúdo mitocondrial.

---

## 2. Fisiopatologia estabelecida

### 2.1 Bioenergética mitocondrial e OXPHOS
Revisões e estudos originais convergem numa tese central: o TDM está associado a desequilíbrios na produção de energia e a estresse oxidativo de origem mitocondrial, com múltiplos mecanismos moleculares (biogênese, autofagia, dinâmica, mutações de mtDNA) contribuindo para a fisiopatologia (PMID 32979495; PMID 22510887; PMID 26923778). Um dos achados mais replicados é a **redução da atividade e expressão de subunidades do Complexo I** (NDUFV1, NDUFV2, NDUFS1) no córtex pré-frontal e no cerebelo lateral em estudos post-mortem — presente também, embora com padrão distinto, em esquizofrenia e transtorno bipolar (revisado em PMID 29928190). Em um estudo post-mortem controlado comparando TDM, transtorno bipolar, esquizofrenia e controles, a redução de NDUFS7 e da atividade do Complexo I, junto com aumento de carbonilação proteica, foi **significativa no transtorno bipolar, mas não no grupo com TDM isolado** — um resultado importante para não generalizar "Complexo I baixo = depressão" sem qualificação (PMID 20368511).

Em fibroblastos de pele cultivados a partir de pacientes com TDM, observou-se respiração basal e máxima reduzidas, capacidade respiratória de reserva menor, produção de ATP mais baixa e potencial de membrana mitocondrial hiperpolarizado — um fenótipo bioenergético mensurável fora do sistema nervoso central, o que sustenta a hipótese de disfunção mitocondrial sistêmica (não restrita ao cérebro) no TDM.

### 2.2 Dinâmica mitocondrial: fissão, fusão e mitofagia
A homeostase de uma população mitocondrial saudável depende do equilíbrio entre biogênese (formação de novas mitocôndrias) e mitofagia (remoção das danificadas). Uma revisão focada especificamente nesse eixo em transtornos psiquiátricos (ansiedade, depressão, TEPT, transtorno bipolar e esquizofrenia) mapeia alterações na rede mitocondrial, na morfologia e nos marcadores moleculares de fissão/fusão/mitofagia tanto em modelos animais quanto em coortes humanas.

**PGC-1α** (o "regulador mestre da biogênese mitocondrial") tem papel central: em camundongos, o silenciamento de PGC-1α no giro denteado do hipocampo produz comportamento do tipo depressivo e reduz sinapses excitatórias; a superexpressão produz o efeito oposto. Em humanos, níveis de PGC-1α no sangue foram associados a sintomas depressivos e à resposta à eletroconvulsoterapia (ECT) (PMID 30191781) — o primeiro estudo a examinar PGC-1α em pacientes deprimidos e resposta a tratamento.

Do lado da mitofagia, um estudo de 2025 (muito recente) mostrou que a enzima HDAC7, superexpressa em astrócitos, desacetila PINK1 e suprime a mitofagia mediada por PINK1/Parkin, reduzindo a liberação mitocondrial de ATP e produzindo comportamento depressivo em camundongos expostos a LPS — o bloqueio farmacológico de HDAC7 reverteu o quadro (PMID 41286926). Isso conecta diretamente disfunção mitocondrial (B9) a neuroinflamação (B1) através de um mecanismo específico em astrócitos.

### 2.3 DNA mitocondrial: número de cópias, mutações e heteroplasmia
Os achados sobre **mtDNAcn (número de cópias de mtDNA)** em sangue periférico são heterogêneos entre estudos — um padrão que deve ser comunicado com honestidade, não escondido:
- Em um estudo com 179 pacientes de atenção primária com depressão, ansiedade e transtornos de ajustamento vs. 320 controles saudáveis, o mtDNAcn médio foi **significativamente mais alto** nos pacientes (84,9 vs. 75,9; p<0,0001), associado à gravidade dos sintomas (PHQ-9) e à resposta ao tratamento (mindfulness/TCC) (PMID 28647451).
- Em transtorno bipolar, uma meta-análise encontrou mtDNAcn **mais baixo** em pacientes, com heterogeneidade significativa entre estudos e resultado positivo apenas em análise específica de população asiática.
- Isso sugere que a direção do efeito pode depender do diagnóstico específico, da fase do transtorno de humor, da matriz biológica (sangue vs. tecido post-mortem) e possivelmente de fatores populacionais — não há um padrão único "mtDNA baixo = depressão".

Estudos post-mortem de córtex pré-frontal dorsolateral encontraram uma taxa 22% maior de substituições sinônimas no genoma mitocondrial em esquizofrenia comparado a controles, e associação entre pH cerebral e o "super-haplogrupo" U/K/UK — independente do tempo post-mortem (PMID 19290059).

### 2.4 Genética: haplogrupos, variantes mitocondriais e estudos populacionais em larga escala
Aqui a literatura é mista e vale reportar isso com precisão:
- Um estudo transversal de grande porte (coorte Osteoarthritis Initiative, América do Norte) **não encontrou associação** entre nenhum haplogrupo mitocondrial específico e sintomas depressivos (PMID 28391108) — um achado negativo relevante que contrasta com achados positivos em esquizofrenia/transtorno bipolar noutros estudos.
- Em contraste, dois estudos de 2022–2023 usando dados do UK Biobank (portanto amostras muito maiores, na casa de 70.000–85.000 indivíduos) encontraram sinal positivo:
  - Um estudo de associação "mitochondria-wide" (MiWAS) identificou 25 SNPs mitocondriais associados a ansiedade autorreferida e interações significativas entre variantes mitocondriais (ex.: m.3915G>A no MT-ND1) e proteína C-reativa (CRP) no risco de ansiedade e depressão — os próprios autores classificam os achados como preliminares e necessitando replicação, e restringiram a amostra a ancestralidade europeia branca (PMID 37344456).
  - Um segundo estudo, usando escores de risco poligênico para função mitocondrial combinados com fatores comportamentais (tabagismo, álcool, atividade física), mostrou efeitos de interação nos desfechos de ansiedade e depressão (PMID 36206883).

---

## 3. Crosstalk mecanístico prioritário com outros mecanismos B

### 3.1 B9 × B1 (Neuroinflamação)
Este é provavelmente o crosstalk mais robusto na literatura atual. mtDNA danificado, liberado no citosol ou na circulação, funciona como DAMP e ativa o inflamassoma NLRP3 e a via cGAS-STING. Em sangue de pacientes com TDM, o inflamassoma NLRP3 está ativado em células mononucleares (PMID 24513871). Uma revisão dedicada a como mitocôndria e micróglia interagem em transtornos afetivos descreve a mitocôndria como reguladora de múltiplas funções da resposta imune inata relevantes à fisiopatologia do TDM (PMID 30687139). Uma revisão de 2021 detalha especificamente a "falha bioenergética neuronal" como elo entre inflamação e depressão (PMID 34790089). Em modelos animais, a proteína desacopladora mitocondrial UCP2 regula negativamente o NLRP3 em astrócitos — seu nocaute agrava comportamento depressivo e ativa a via ROS-TXNIP-NLRP3; e melatonina (um composto de interesse ortomolecular) atenua comportamento depressivo induzido por LPS via SIRT1/Nrf2, reduzindo ativação do inflamassoma NLRP3 microglial (PMID 31327964).

### 3.2 B9 × B2 (Eixo HPA-Cortisol)
O receptor de glicocorticoide (GR) não age apenas no núcleo: a isoforma GRα transloca-se para dentro da mitocôndria após ligação ao cortisol/corticosterona, onde se liga a sequências no genoma mitocondrial com similaridade parcial aos elementos responsivos a glicocorticoide (GREs) nucleares, modulando diretamente a transcrição mitocondrial (revisado em PMID 34205227). O efeito é dose e tempo-dependente: doses agudas ou baixas/moderadas de corticosterona aumentam a oxidação mitocondrial; exposição crônica ou em alta dose a reduz — um padrão bifásico consistente com o modelo de carga alostática (ver Seção 4.1). Estresse crônico também altera a fosforilação do GR mitocondrial de forma região-específica (aumento no córtex pré-frontal, alteração de fosforilação no hipocampo).

### 3.3 B9 × B4 / B5 (Monoaminas / GABA-Glutamato)
A monoaminoxidase (MAO-A/B) está ancorada na membrana externa mitocondrial — a própria degradação de monoaminas é, portanto, um evento mitocondrial, e o subproduto (H₂O₂) contribui à carga oxidativa mitocondrial. Do lado oposto (mitocôndria → monoamina), um achado elegante mostra que a **serotonina regula diretamente a biogênese e função mitocondrial** em neurônios corticais de roedores, via receptor 5-HT2A e o eixo SIRT1–PGC-1α (PMID 31072928) — ou seja, o mesmo neurotransmissor central ao mecanismo B4 é também um regulador upstream da maquinaria de biogênese mitocondrial do mecanismo B9. Já a excitotoxicidade glutamatérgica (B5) opera via sobrecarga de cálcio mitocondrial: glutamato em excesso ativa receptores NMDA, o influxo de Ca²⁺ é tamponado pela mitocôndria via MCU, e a sobrecarga resultante pode abrir o poro de transição de permeabilidade mitocondrial (mPTP), levando a colapso do potencial de membrana e, em última instância, apoptose. É também neste ponto que a cetamina (antagonista NMDA) parece atuar: um estudo de metaboloma/proteoma em hipocampo de camundongos tratados com cetamina implica diretamente o metabolismo energético mitocondrial e o sistema de defesa antioxidante como efetores a jusante da resposta à cetamina, com ativação de mTORC1 estimulando biogênese mitocondrial dentro de 30–60 minutos do tratamento.

### 3.4 Nota sobre B9 × B6 (Estresse oxidativo)
Dado que a Biblioteca B1/NT-06 deste projeto já trata estresse oxidativo com centralidade em B3/BDNF, friso aqui apenas o ponto de fronteira conceitual: a mitocôndria é a **principal fonte endógena de ROS** (via vazamento de elétrons na CTE, sobretudo nos Complexos I e III) e também o **principal alvo** do dano oxidativo resultante — portanto B9 e B6 descrevem, em grande parte, o mesmo sistema físico visto de dois ângulos (fonte/produção vs. consequência/dano). Ao integrar os dois módulos no pipeline, vale explicitar que não são mecanismos independentes, mas um circuito de retroalimentação: ROS mitocondrial → dano a proteínas/lipídeos/mtDNA → mais disfunção mitocondrial → mais ROS.

---

## 4. Ciência de fronteira

### 4.1 Carga alostática mitocondrial (Picard & McEwen)
Talvez o desenvolvimento conceitual mais influente da última década nesta área. Martin Picard e Bruce McEwen propuseram que a mitocôndria não é apenas uma vítima passiva do estresse crônico, mas um **transdutor ativo** de experiência psicossocial em mudanças bioquímicas mensuráveis — cunhando o termo "carga alostática mitocondrial" (PMID 29389736, revisão sistemática de 23 estudos controlados sobre estresse psicológico e mitocôndria; ver também o artigo conceitual companheiro do mesmo número da revista). Entre os complexos da CTE, o **Complexo IV (COX)** — parcialmente codificado pelo próprio mtDNA — foi o mais consistentemente afetado pelo estresse nos estudos revisados, com reduções de atividade específica de 0 a 80%.

### 4.2 mtDNA circulante livre de células (ccf-mtDNA)
Um biomarcador de sangue periférico cada vez mais estudado. Uma revisão sistemática de referência (mesmo grupo de Picard) mostra que o ccf-mtDNA no sangue varia em resposta a estressores do mundo real — incluindo psicopatologia, estresse psicológico agudo e exercício — sendo induzível em minutos e com alta variação dia-a-dia intraindividual (PMID 33839318). Isso o torna candidato a biomarcador dinâmico de estado (não apenas de traço), potencialmente mais sensível a mudanças clínicas de curto prazo do que o mtDNAcn convencional.

### 4.3 GDF-15 como mitocina de estresse
GDF-15 é uma citocina de estresse energético que sinaliza ao cérebro (via receptor GFRAL, restrito ao tronco encefálico) sobre demanda celular elevada. Um estudo publicado em 2024 usando as coortes UK Biobank (n=53.026) e Framingham Heart Study Offspring (n=3.460) encontrou níveis plasmáticos de GDF-15 **elevados em indivíduos com sintomas de depressão e ansiedade**, e também mais altos em quem reportava estressores psicossociais crônicos (menor escolaridade, menor renda familiar, maior tensão no trabalho) (PMID 38659958). Um estudo populacional subsequente, porém, mostrou que a relação entre GDF-15 e sintomas depressivos é **dependente da idade** — GDF-15 mais alto associou-se a menos sintomas depressivos em adultos jovens, mas a mais sintomas em idosos — e que a associação com ansiedade não foi significativa nesse estudo. Isso reforça que GDF-15 é promissor, mas não deve ser tratado como biomarcador linear e universal.

### 4.4 Eixo microbiota–mitocôndria
Campo emergente com forte apelo para medicina integrativa, mas ainda majoritariamente pré-clínico/associativo em humanos — isso precisa ser dito explicitamente ao cliente/profissional que for consumir este material. Uma revisão de 2025 mapeia mecanismos bidirecionais: metabólitos da microbiota (especialmente ácidos graxos de cadeia curta — SCFAs, como butirato) atravessam a barreira hematoencefálica e aumentam a biogênese mitocondrial via ativação da via AMPK–PGC1α, ao mesmo tempo em que ROS de origem mitocondrial altera a composição da microbiota intestinal ao modificar o microambiente epitelial — um verdadeiro loop bidirecional (PMID 40313405). Essa mesma revisão aponta terapias emergentes ainda experimentais nessa interseção: transplante de mitocôndria, terapia fágica, bactérias geneticamente modificadas, além das intervenções já mais estabelecidas (probióticos, fibra dietética, transplante de microbiota fecal). Revisões relacionadas de contexto mais amplo sobre microbiota e depressão (sem foco mitocondrial específico) reforçam a plausibilidade biológica geral do eixo (PMID 34350881; PMID 36963238; PMID 34524405 — meta-análise publicada na JAMA Psychiatry; PMID 35565888).

### 4.5 Genômica populacional em larga escala (além da Seção 2.4)
Os estudos de UK Biobank citados na Seção 2.4 (PMID 37344456; PMID 36206883) representam uma nova geração de evidência: em vez de comparar grupos pequenos de pacientes vs. controles, usam dezenas de milhares de participantes para testar interação gene mitocondrial × ambiente/inflamação. É ciência de fronteira genuína — os próprios autores enquadram os achados como preliminares.

### 4.6 Peptídeos derivados de mitocôndria (MDPs) — ver Seção 8 para o sinalizador de extrapolação completo
Humanina, MOTS-c e os SHLPs (small humanin-like peptides) são pequenos peptídeos codificados por regiões do mtDNA classicamente tidas como "não-codificantes" (16S e 12S rRNA). Têm papel bem estabelecido em citoproteção, neuroproteção contra insultos relacionados à doença de Alzheimer e regulação metabólica (sensibilidade à insulina, resposta ao exercício). **Não encontrei estudos que testem diretamente MDPs em ansiedade ou depressão** — a conexão a B9/ansiedade-depressão é, no estado atual da literatura que localizei, uma extrapolação plausível (mitocôndria → peptídeo de sinalização → neuroproteção/resiliência ao estresse), não um achado direto.

---

## 5. Intervenções com ancoragem mitocondrial (relevância clínica / ortomolecular)

### 5.1 Agentes nutracêuticos "mitocondriais" — evidência clínica em humanos
Uma meta-análise de 2022 (13 ensaios clínicos randomizados) avaliou moduladores mitocondriais como adjuvantes no tratamento da depressão bipolar: **N-acetilcisteína (NAC)** foi o único com efeito antidepressivo estatisticamente significativo isoladamente (SMD -0,88 vs. placebo); o efeito geral do conjunto de moduladores mitocondriais (NAC, ômega-3, inositol, CoQ10, creatina monoidratada, vitamina D, ALCAR+ácido alfalipoico) foi moderado e estatisticamente significativo (SMD global -0,48) (PMID 35013098). Um ensaio randomizado de referência (n=181, 16 semanas) testou NAC isolada vs. NAC + coquetel nutracêutico de 16 compostos (incluindo ALCAR, CoQ10 e ácido alfalipoico) vs. placebo em depressão bipolar — os elementos centrais dessa combinação são precisamente os "nutrientes mitocondriais" de interesse ortomolecular.

### 5.2 Precursores de NAD+ (nicotinamida ribosídeo / NMN)
NAD+ é o cofator central da CTE e substrato de sirtuínas (incluindo a SIRT3 mitocondrial). Não localizei nenhum ensaio clínico randomizado com nicotinamida ribosídeo (NR) tendo depressão ou ansiedade como desfecho primário. O achado mais próximo é um ensaio de 24 semanas em long-COVID (NR 2000mg/dia) que incluía sintomas depressivos e ansiosos entre os desfechos exploratórios secundários: não houve melhora significativa na função cognitiva primária, mas análises exploratórias sugeriram melhora em funcionamento executivo, qualidade do sono e redução de fadiga e de sintomas depressivos após 10 semanas — os próprios autores pedem ensaios maiores e mais focados antes de qualquer conclusão (PMID 41357333). **Isto deve ser comunicado como sinal exploratório de um ensaio com outro desfecho primário, não como evidência de eficácia antidepressiva do NR.**

### 5.3 Exercício físico
Uma revisão de 2025 dedicada especificamente a exercício, função mitocondrial e depressão resistente a tratamento descreve o exercício físico como indutor de biogênese mitocondrial, neuroplasticidade, e redução de estresse oxidativo e neuroinflamação, via vias como BDNF, AMPK, PGC-1α ativo e CaMKII — com evidência de que treino de resistência e intervalado de alta intensidade também promovem adaptações mitocondriais benéficas, além do exercício aeróbico moderado já mais estudado (PMID 40943622). Os próprios autores apontam que a dose ótima de exercício e quais subgrupos de pacientes mais se beneficiam ainda são lacunas abertas.

### 5.4 Antioxidantes mitocôndria-alvo (MitoQ, SS-31/elamipretide)
Este é o achado de fronteira mais direto e mecanisticamente elegante para **ansiedade especificamente** (não apenas depressão): pesquisadores do Max Planck Institute of Psychiatry compararam camundongos com fenótipo de alta ansiedade (HAB) e baixa ansiedade, identificaram alterações em vias mitocondriais (fosforilação oxidativa e estresse oxidativo) no cérebro dos HAB, e então trataram os HAB com **MitoQ** (antioxidante que se acumula seletivamente na mitocôndria) — o tratamento **reduziu comportamento ansioso** de forma específica ao fenótipo de alta ansiedade (sem efeito em linhagens de ansiedade normal), sendo o primeiro estudo a ligar diretamente direcionamento mitocondrial farmacológico a efeito ansiolítico in vivo (PMID 26567514). **É um estudo pré-clínico em camundongos — não há, até onde localizei, ensaio equivalente em humanos com ansiedade ou depressão como desfecho.** MitoQ já passou por ensaios de fase II em humanos para outras indicações (Parkinson, hepatite C), o que sustenta viabilidade de segurança/tolerabilidade, mas não eficácia psiquiátrica.

### 5.5 Intervenções farmacológicas/procedimentais com mecanismo mitocondrial documentado
- **Cetamina**: ver Seção 3.3 — biogênese mitocondrial via mTORC1 dentro de 30–60 min, redução da razão ATP/ADP correlacionada com desfecho comportamental em modelo animal.
- **ECT**: níveis de PGC-1α no sangue associados à resposta clínica (PMID 30191781).
- **Iptakalim** (abridor de canal KATP mitocondrial, ainda experimental): atenua dano sináptico via esse canal específico em modelo de depressão (PMID 33871072) — sinalizador de um alvo farmacológico mitocondrial novo, não uma intervenção validada clinicamente.

---

## 6. Termos de busca alternativos (para aprofundamento futuro / expansão da NT-09)

- mitochondrial bioenergetics + major depressive disorder / anxiety disorder
- mitochondrial dynamics OR mitochondrial fission fusion + mood disorder
- mitophagy PINK1 Parkin + stress OR depression
- cell-free mitochondrial DNA OR ccf-mtDNA + psychiatric
- mitochondrial allostatic load
- GDF15 OR growth differentiation factor 15 + depression OR anxiety OR stress
- mitochondria-wide association study (MiWAS)
- mitochondrial-derived peptides + neuropsychiatric (para monitorar se a lacuna da Seção 4.6/8 for preenchida por novos estudos)
- microbiota mitochondria crosstalk + depression
- mitochondrial transplantation + neuropsychiatric OR depression
- NAD+ precursor + depression clinical trial
- mitochondrial glucocorticoid receptor + stress
- platelet mitochondrial respiration + depression (biomarcador periférico pouco explorado neste briefing)
- mitochondrial complex IV COX + psychological stress
- UPRmt OR mitochondrial unfolded protein response + neuropsychiatric
- SS-31 elamipretide + brain OR neuropsychiatric

## 7. Áreas adjacentes subexploradas

1. **Respirometria plaquetária/PBMC como biomarcador clínico de rotina** — tecnicamente viável, usada em pesquisa, mas quase ausente de estudos de desfecho terapêutico em depressão/ansiedade.
2. **Mitocôndria e resposta a psicodélicos** — a literatura de cetamina é robusta; a de psilocibina/outros psicodélicos e mecanismo mitocondrial específico é escassa no que localizei.
3. **Diferenças de sexo na bioenergética mitocondrial cerebral** — mencionada de passagem em vários artigos (mtDNAcn mais alto em mulheres, por exemplo), mas raramente é o desfecho primário de um estudo em ansiedade/depressão.
4. **Mitocôndria e cronobiologia/ritmo circadiano** — a CTE tem ritmicidade circadiana própria; a interseção com transtornos do humor via esse ângulo específico é pouco representada nos artigos que revisei.
5. **Transplante de mitocôndria como terapêutica psiquiátrica** — mencionado como direção futura em pelo menos duas revisões, mas ainda sem ensaio clínico em humanos para depressão/ansiedade que eu tenha localizado; os desafios de entrega e segurança imunológica são citados como barreiras abertas.
6. **Fotobiomodulação (luz vermelha/infravermelho próximo) e função mitocondrial cerebral** — citada en passant em pelo menos uma revisão sobre TDM e mitocôndria como intervenção não-farmacológica emergente, mas não aprofundei essa literatura especificamente neste ciclo de busca — fica registrado como pendência para uma rodada futura.

## 8. Sinalizadores de extrapolação — o que é estabelecido vs. o que é hipótese de ponte

Para uso direto no pipeline (marcação de confiança/GRADE):

**Estabelecido com replicação humana (GRADE A/B plausível, sujeito à sua verificação PQ-09A):**
- Redução de atividade/expressão do Complexo I em subconjuntos de transtornos psiquiátricos (post-mortem).
- Disfunção bioenergética mensurável perifericamente (fibroblastos, sangue) em TDM.
- mtDNAcn alterado em depressão/ansiedade/transtornos de ajustamento — direção do efeito não é consistente entre diagnósticos.
- Ativação do inflamassoma NLRP3 associada a mtDNA/ROS mitocondrial em TDM.
- PGC-1α associado a sintomas depressivos e resposta a ECT em humanos.
- Eficácia antidepressiva modesta de NAC como adjuvante em depressão bipolar (meta-análise de ECRs).
- ccf-mtDNA responsivo a estresse psicológico agudo em humanos (revisão sistemática).

**Ciência de fronteira genuína, ainda preliminar mesmo nos termos dos próprios autores:**
- Carga alostática mitocondrial como framework unificador (conceitual, com evidência de suporte parcial).
- GDF-15 como biomarcador de estresse/depressão (relação dependente de idade, não linear).
- Achados de MiWAS/UK Biobank sobre variantes mitocondriais × inflamação em ansiedade/depressão (replicação pendente, amostra restrita a ancestralidade europeia).
- Eixo microbiota-mitocôndria em depressão (mecanismo bem descrito em animais; humano "heterogêneo e majoritariamente associativo" nas palavras dos próprios revisores da área).

**Extrapolação — ponte hipotética a partir de literatura de outra área, não achado direto em ansiedade/depressão:**
- Peptídeos derivados de mitocôndria (humanina, MOTS-c) como moduladores de ansiedade/depressão — evidência direta que localizei está em Alzheimer, envelhecimento e metabolismo, não em transtornos de humor/ansiedade.
- MitoQ como ansiolítico — validado em camundongos de fenótipo de alta ansiedade; nenhum ensaio humano psiquiátrico localizado.
- Precursores de NAD+ como antidepressivo/ansiolítico — sinal exploratório secundário de um ensaio de long-COVID, não um ensaio dedicado.
- Transplante de mitocôndria para depressão — mencionado como direção futura em revisões, sem ensaio clínico psiquiátrico.

---

## 9. Lista de PMIDs validados (verificados individualmente — não inventados)

Organizados por bloco temático. Todos confirmados via visualização direta da página PubMed/PMC correspondente.

### Revisões fundamentais / fisiopatologia geral
1. **22510887** — Manji H et al. (2012). Impaired mitochondrial function in psychiatric disorders. *Nat Rev Neurosci*.
2. **20691744** — Gardner A, Boles RG (2011). Beyond the serotonin hypothesis: mitochondria, inflammation and neurodegeneration in major depression and affective spectrum disorders. *Prog Neuropsychopharmacol Biol Psychiatry*.
3. **26923778** — Bansal Y, Kuhad A (2016). Mitochondrial dysfunction in depression. *Curr Neuropharmacol*.
4. **29928190** — Allen J, Romay-Tallon R, Brymer KJ, Caruncho HJ, Kalynchuk LE (2018). Mitochondria and Mood: Mitochondrial Dysfunction as a Key Player in the Manifestation of Depression. *Front Neurosci*.
5. **25262287** — Klinedinst NJ, Regenold WT (2015). A mitochondrial bioenergetic basis of depression. *J Bioenerg Biomembr*.
6. **31551791** — Caruso G, Benatti C, Blom JMC, Caraci F, Tascedda F (2019). The many faces of mitochondrial dysfunction in depression: from pathology to treatment. *Front Pharmacol*.
7. **32979495** — (2020). Molecular correlates of mitochondrial dysfunctions in major depression: Evidence from clinical and rodent studies.
8. **34295268** — Giménez-Palomo A, Dodd S, Anmella G, Carvalho AF, Scaini G, et al. (2021). The role of mitochondria in mood disorders: from physiology to pathophysiology and to treatment. *Front Psychiatry*.
9. **27839913** — Kato T (2017). Neurobiological basis of bipolar disorder: mitochondrial dysfunction hypothesis and beyond. *Schizophr Res*.
10. **36203007** — Fries GR, Saldana VA, Finnstein J, Rein T (2023). Molecular pathways of major depressive disorder converge on the synapse. *Mol Psychiatry*.

### mtDNA, genética e estudos populacionais
11. **28647451** — Association of mitochondrial DNA in peripheral blood with depression, anxiety and stress- and adjustment disorders in primary health care patients.
12. **20368511** — Andreazza AC et al. Mitochondrial complex I activity and oxidative damage to mitochondrial proteins in the prefrontal cortex of patients with bipolar disorder.
13. **19290059** — Mitochondrial Variants in Schizophrenia, Bipolar Disorder, and Major Depressive Disorder. *PLoS One*.
14. **28391108** — Mitochondrial genetic haplogroups and depressive symptoms: A large study among people in North America. *(achado negativo)*
15. **37344456** — Liu L et al. (2023). Mitochondria-wide association study observed significant interactions of mitochondrial respiratory and the inflammatory in the development of anxiety and depression. *Transl Psychiatry*.
16. **36206883** — Assessing the joint effects of mitochondrial function and human behavior on the risks of anxiety and depression. *J Affect Disord*.

### Dinâmica mitocondrial, mitofagia e biogênese
17. **38492883** — Deng Y et al. PGC-1α in the hippocampus mediates depressive-like and stress-coping behaviours and regulates excitatory synapses in the dentate gyrus in mice. *Neuropharmacology*. (corrigendum: PMID 39043539)
18. **30191781** — Peroxisome proliferator-activated receptor gamma co-activator-1 alpha in depression and the response to electroconvulsive therapy.
19. **41286926** — Upregulated astrocytic HDAC7 induces depression-like disorders via deacetylating PINK1 and inhibiting mitophagy (2025). *J Neuroinflammation*.
20. **31072928** — Fanibunda SE et al. (2019). Serotonin regulates mitochondrial biogenesis and function in rodent cortical neurons via the 5-HT(2A) receptor and SIRT1-PGC-1α axis. *PNAS*.

### Estresse psicológico, carga alostática mitocondrial e biomarcadores de fronteira
21. **29389736** — Picard M, McEwen BS (2018). Psychological Stress and Mitochondria: A Systematic Review. *Psychosom Med*.
22. **33839318** — Trumpff C et al. (2021). Stress and circulating cell-free mitochondrial DNA: A systematic review of human studies, physiological considerations, and technical recommendations. *Mitochondrion*.
23. **38659958** — The energetic stress cytokine GDF15 is elevated in the context of chronic and acute psychosocial stress.
24. **26567514** — Nussbaumer M et al. (2015). Selective Mitochondrial Targeting Exerts Anxiolytic Effects In Vivo. *Neuropsychopharmacology*. *(camundongos)*

### Crosstalk com neuroinflamação (B1)
25. **30687139** — Culmsee C, Michels S, Scheu S, Arolt V, Dannlowski U, Alferink J (2019). Mitochondria, Microglia, and the Immune System—How Are They Linked in Affective Disorders? *Front Psychiatry*.
26. **24513871** — Alcocer-Gómez E et al. (2014). NLRP3 inflammasome is activated in mononuclear blood cells from patients with major depressive disorder. *Brain Behav Immun*.
27. **34790089** — Casaril AM, Dantzer R, Bas-Orth C (2021). Neuronal mitochondrial dysfunction and bioenergetic failure in inflammation-associated depression. *Front Neurosci*.
28. **31327964** — Melatonin Attenuates LPS-Induced Acute Depressive-Like Behaviors and Microglial NLRP3 Inflammasome Activation Through the SIRT1/Nrf2 Pathway.

### Crosstalk com eixo HPA (B2)
29. **34205227** — Kokkinopoulou I, Moutsatsou P (2021). Mitochondrial Glucocorticoid Receptors and Their Actions. *Int J Mol Sci*.

### Eixo microbiota–mitocôndria (fronteira)
30. **40313405** — Zhao H et al. (2025). Multiple pathways through which the gut microbiota regulates neuronal mitochondria constitute another possible direction for depression. *Front Microbiol*.
31. **34350881** — Kunugi H (2021). Gut microbiota and pathophysiology of depressive disorder. *Ann Nutr Metab*.
32. **36963238** — Liu L et al. (2023). Gut microbiota and its metabolites in depression: from pathogenesis to treatment. *EBioMedicine*.
33. **34524405** — Nikolova VL et al. (2021). Perturbations in gut microbiota composition in psychiatric disorders: a review and meta-analysis. *JAMA Psychiatry*.
34. **35565888** — (2022). The Role of the Microbiome-Brain-Gut Axis in the Pathogenesis of Depressive Disorder. *Nutrients*.

### Intervenções nutracêuticas/ortomoleculares e farmacológicas
35. **35013098** — Liang L, Chen J, Xiao L, Wang Q, Wang G (2022). Mitochondrial modulators in the treatment of bipolar depression: a systematic review and meta-analysis. *Transl Psychiatry*.
36. **40943622** — (2025). Adaptations in Mitochondrial Function Induced by Exercise: A Therapeutic Route for Treatment-Resistant Depression.
37. **41357333** — Effects of nicotinamide riboside on NAD+ levels, cognition, and symptom recovery in long-COVID: a randomized controlled trial. *(desfecho depressivo/ansioso é exploratório secundário, não primário)*
38. **33871072** — Guo W et al. (2021). Iptakalim alleviates synaptic damages via targeting mitochondrial ATP-sensitive potassium channel in depression. *FASEB J*.

### Peptídeos derivados de mitocôndria (contexto — extrapolação, ver Seção 8)
39. **36670507** — Mitochondria-derived peptide MOTS-c: effects and mechanisms related to stress, metabolism and aging.
40. **11717357** — Hashimoto Y et al. (2001). Detailed Characterization of Neuroprotection by a Rescue Factor Humanin against Various Alzheimer's Disease-Relevant Insults. *J Neurosci*. *(contexto Alzheimer, não depressão/ansiedade)*

---

**Achados relevantes que localizei mas NÃO incluí acima por não ter confirmado um PMID individualmente** (para não violar "sem inventar" — se quiser, posso tentar verificar em uma rodada dedicada):
- Zhao H et al., "Microbiota–mitochondria crosstalk in the gut–brain axis..." *Explor Neurosci* 2026;5:1006133 (DOI 10.37349/en.2026.1006133) — revisão muito recente e diretamente relevante, mas o periódico pode não estar indexado no PubMed ainda.
- Estudo sobre via ROS/TXNIP/NLRP3 em "depressão ansiosa" (comórbida), *Front Immunol* 2026, DOI 10.3389/fimmu.2026.1803956 — publicação de maio/2026, possivelmente ainda sem PMID atribuído no momento desta busca.
