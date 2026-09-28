# BRIEFING CONSOLIDADO B5 v1 — GABA/GLUTAMATO EM ANSIEDADE E DEPRESSÃO

**Rodada 0 — Briefing de direcionamento para a B5 (construção nova, profundidade ampliada por pedido explícito).**
Data: 2026-09-05 · Prompt de referência: **v4.2 — "Mecanismos de Ansiedade e Depressão"** (mesmo framework da B1/B3/B4).
Mecanismo: `mecanismo_B5_gaba_glutamato`.

> **Nota de proveniência — leia antes de usar.** Mesma ressalva das B3/B4: sem canônica prévia, sem
> mapa de ansiedade auditado. Diferença desta rodada: o pedido foi explicitamente por **profundidade
> máxima — "tudo que tem na ciência e na fronteira da ciência"** — então esta B5 é sensivelmente maior
> que a B3/B4: 22 buscas ao vivo nesta sessão, 19 PMIDs confirmados diretamente numa página que os
> cita (G1 caso a caso), cobrindo desde os marcos históricos dos anos 1990 até fármacos aprovados
> pela FDA em 2023 (zuranolona). **Nenhum PMID foi inventado**; dois itens que não localizei com
> segurança (Rudolph et al. 1999, Nature — o paper fundador da anxiólise via subunidade α2; e Ressler
> et al. 2004, Arch Gen Psychiatry — o primeiro ensaio humano de D-cicloserina) entram só com citação
> bibliográfica completa e `PMID: a confirmar`, substituídos na tabela por artigos-irmãos da mesma
> linha de pesquisa que **foram** confirmados. Como nas B3/B4, isto é G1 caso a caso — **não** substitui
> G2/G3 nem os scripts de fidelidade.

---

## 0. Tese-central da B5

B5 cobre DOIS sistemas de neurotransmissão que a literatura tratou por décadas como campos quase
separados — GABA (inibitório) e glutamato (excitatório) — e que hoje colidem no mesmo mecanismo
central: o **desequilíbrio excitação/inibição (E/I)** no córtex pré-frontal e estruturas límbicas. A
B5 precisa cobrir:

1. **O eixo GABAérgico clássico** — receptores GABA-A (canal de cloreto, sítio benzodiazepínico) e
   GABA-B (metabotrópico); décadas de uso clínico de benzodiazepínicos, mas só nos anos 1999-2012 a
   farmacologia foi decomposta por subunidade (α1 = sedação; α2 = ansiólise — ver Seção 8).
2. **O eixo glutamatérgico e a revolução da cetamina** — de observação psicotomimética em
   voluntários saudáveis (Krystal, 1994) a antidepressivo de ação rápida (Berman, 2000; Zarate,
   2006) em 12 anos; o mecanismo celular (bloqueio de NMDA em interneurônios GABAérgicos →
   desinibição → surto de glutamato → AMPA → mTORC1/sinaptogênese) **é o ponto exato onde B5 e B3 se
   fundem** — ver Seção 4.
3. **A fronteira mais recente e literal: neuroesteroides como fármaco** — brexanolona (2019) e
   zuranolona (2023) são moduladores alostéricos positivos do receptor GABA-A **aprovados pela FDA**,
   não hipóteses de bancada. Este é provavelmente o ponto mais "fronteira" de toda a série B1-B5 até
   agora: mecanismo, ensaio clínico e aprovação regulatória já fechados no mesmo eixo.
4. **O lado ainda debatido:** se o bloqueio de NMDA é sequer necessário para o efeito antidepressivo
   da cetamina — há questionamento ativo na literatura (Zorumski, Izumi & Mennerick, 2016, *"Ketamine:
   NMDA Receptors and Beyond"*) sobre se o gatilho psicotomimético e o gatilho antidepressivo são o
   mesmo mecanismo. Registrar como `[EMERGENTE]`, não como consenso.
5. Mesma disciplina de selos: `[VERIFICADO]` só após G1→G2→G3; `[PRÉ-CLÍNICO]`/`[EXTRAPOLADO]` para
   animal/célula sem tradução humana direta; `[EMERGENTE]` para disputa em curso.

---

## 1. Nomenclatura e famílias moleculares — busca por nome específico

### 1a. Núcleo estabelecido
**GABA:** síntese por **GAD65/GAD67** (glutamato descarboxilase); receptor **GABA-A** (pentâmero,
canal de cloreto — subunidades α1-6, β1-3, γ1-3, δ, entre outras; sítio benzodiazepínico entre
subunidades α e γ); receptor **GABA-B** (metabotrópico, acoplado a Gi/Go, canais GIRK); inibição
**fásica** (sináptica) vs. **tônica** (extrassináptica, receptores com subunidade δ). **Glutamato:**
receptor **NMDA** (subunidades GluN1, GluN2A-D, GluN3 — heterotetrâmero); receptor **AMPA**
(GluA1-4, tráfego dependente de atividade); receptores metabotrópicos — **Grupo I** (mGluR1/5,
pós-sinápticos, excitatórios) e **Grupo II** (mGluR2/3, autorreceptores pré-sinápticos, inibitórios);
transportadores gliais **EAAT1/2** (GLT-1) e o ciclo glutamato-glutamina astrocitário;
transportadores vesiculares **VGLUT1/2**. **Farmacologia clássica:** benzodiazepínicos (moduladores
alostéricos positivos do GABA-A), cetamina (antagonista não competitivo de NMDA), riluzol (modula
recaptação glial de glutamato).

### 1b. Eixos que precisam de aprofundamento dedicado (a maioria já tem PMID nesta sessão — ver Seção 8; alguns ficaram só no checklist)
- **Neuroesteroides (o eixo mais "fronteira"):** alopregnanolona — metabólito da progesterona,
  modulador alostérico positivo potente de receptores GABA-A **sinápticos e extrassinápticos**
  (estes últimos contêm subunidade δ, mediam inibição tônica); queda abrupta pós-parto como gatilho
  proposto de depressão pós-parto; brexanolona e zuranolona (Seção 8) são a tradução farmacêutica
  direta desta hipótese.
- **Hipótese da desinibição (o elo B5-B3 mais fino):** antagonismo de NMDA atinge **preferencialmente**
  interneurônios GABAérgicos (que dependem mais de NMDA para disparo espontâneo do que neurônios
  piramidais) → desinibição → surto de glutamato → ativação de AMPA → cascata mTORC1 (ver B3).
- **Interneurônios GABAérgicos por subtipo:** somatostatina (SST, alvo dendrítico de piramidais) vs.
  parvalbumina (PV, alvo peri-somático/axônico) — déficit de SST é achado replicado em depressão
  post-mortem; a proporção SST/PV parece mais relevante que "GABA total".
- **Farmacologia de subunidade do GABA-A:** α2/α3 mediam ansiólise; α1 medeia sedação/hipnose; α5
  (hipocampal) parece ligado a efeitos ansiolíticos e cognitivos distintos — a busca histórica por um
  "benzodiazepínico sem sedação" (ex.: TP003, TPA023) nasce diretamente desta subunidade-especificidade.
- **Homeostase de cloreto (KCC2/NKCC1):** determina se GABA é hiperpolarizante (adulto, KCC2 alto) ou
  despolarizante (desenvolvimento inicial/pós-trauma, NKCC1 relativamente alto); relevante a TEPT e
  a janelas de replasticidade.
- **mGluR2/3 como alvo ansiolítico alternativo ao GABA-A:** agonistas/moduladores de mGluR2/3 reduzem
  liberação pré-sináptica de glutamato sem o perfil de abuso/sedação dos benzodiazepínicos —
  candidato histórico a "ansiolítico de próxima geração", com tradução clínica ainda mista.
- **GABA-B e baclofeno:** menos explorado em ansiedade/depressão do que GABA-A; relevância maior
  documentada em dependência química do que em transtornos de humor per se — verificar lastro
  próprio antes de estender.

## 2. Termos de busca alternativos

- Mecanismo: "GABA-A receptor subunit anxiolysis", "NMDA receptor antagonist antidepressant",
  "disinhibition hypothesis ketamine", "neurosteroid GABA-A allosteric modulator", "somatostatin
  interneuron depression", "mGluR2/3 anxiolytic", "chloride homeostasis KCC2 NKCC1", "excitation
  inhibition balance prefrontal cortex".
- Ansiedade/TOC/TEPT: "benzodiazepine alpha2 subunit fear", "D-cycloserine exposure therapy",
  "glutamate obsessive-compulsive disorder", "GABA-A receptor PTSD", "fear extinction NMDA".
- Método/confundidor: "MRS GABA glutamate depression reliability", "peripheral vs central GABA",
  "TSPO GABA-A benzodiazepine receptor imaging".

## 3. Áreas adjacentes subexploradas — priorizar

- **Neuroesteroides como categoria farmacológica própria**, não como nota de rodapé do GABA-A — é
  a única classe nova de fármaco aprovada pela FDA para depressão nas últimas décadas fora do eixo
  glutamatérgico/monoaminérgico.
- **A proporção SST/PV, não "GABA total"** — resumos de divulgação tendem a tratar déficit
  GABAérgico como uniforme; a literatura de subtipo é mais fina e mais recente.
- **O debate sobre se NMDA é mesmo o gatilho do efeito antidepressivo da cetamina** — Zorumski et al.
  (2016) questionam isso abertamente; quase nunca aparece em resumos de divulgação, que tratam o
  mecanismo NMDA→mTOR como fechado.
- **mGluR2/3 como classe alternativa** — pouco citada fora de círculos especializados, apesar de
  décadas de pesquisa.
- **mGluR5 e a farmacologia "espelhada"**: moduladores positivos de mGluR5 podem, por outra via
  (ativação direta de neurônios GABAérgicos e glutamatérgicos), também aumentar o efluxo de
  glutamato no córtex pré-frontal — mecanismo diferente do antagonismo de NMDA, mesmo desfecho final.

## 4. Crosstalk prioritário (equivalente ao BLOCO 08 da B1/B3/B4)

- **B5↔B1 (neuroinflamação):** citocinas alteram o tráfego de receptores GABA-A e a expressão de
  GAD67; poda sináptica mediada por complemento (já detalhada na B1/B3) afeta sinapses excitatórias
  e inibitórias de formas diferentes.
- **B5↔B2 (HPA):** conexão **bioquímica direta**, não só funcional — alopregnanolona é sintetizada a
  partir da progesterona pela mesma via esteroidogênica que produz cortisol (5α-redutase/3α-HSD);
  glicocorticoides também alteram a expressão de subunidades do GABA-A.
- **B5↔B3 (plasticidade):** a fronteira mais tênue de toda a série — o mecanismo da cetamina
  (NMDA→desinibição→glutamato→AMPA→mTORC1→sinaptogênese) é ao mesmo tempo B5 (farmacologia do
  receptor) e B3 (desfecho estrutural); sugestão editorial: B5 fica com o receptor e o circuito
  E/I, B3 fica com o espinho dendrítico e a sinaptogênese resultante.
- **B5↔B4 (monoaminas):** receptores 5-HT3 (únicos receptores de serotonina ionotrópicos) ficam em
  interneurônios GABAérgicos; serotonina modula liberação de glutamato no córtex pré-frontal.
- **B5↔B6/B9 (oxidativo/mitocôndria):** excitotoxicidade glutamatérgica via sobrecarga de cálcio
  mitocondrial; estresse oxidativo prejudica a função de GAD65/67.
- **B5↔B7 (disbiose):** algumas cepas de *Lactobacillus*/*Bifidobacterium* produzem GABA
  diretamente no lúmen intestinal; sinalização vagal é a via proposta de comunicação com expressão
  central de GABA-A — mecanismo com lastro ainda majoritariamente pré-clínico.
- **B5↔B13 (endocanabinoide):** o crosstalk mais bem estabelecido de toda a B5 — sinalização
  endocanabinoide retrógrada (2-AG/anandamida, receptor CB1) medeia tanto **DSI**
  (*depolarization-induced suppression of inhibition*, terminais GABAérgicos) quanto **DSE**
  (*...of excitation*, terminais glutamatérgicos) a partir do mesmo neurônio pós-sináptico — é
  literalmente o mecanismo que ajusta o balanço E/I em tempo real.

## 5. Polimorfismos / variantes a verificar

- **GABRA2** (subunidade α2 do GABA-A) — associado principalmente a dependência de álcool na
  literatura de genética; extensão a ansiedade/depressão per se precisa de lastro próprio.
- **GAD1** (codifica GAD67) — variantes associadas a esquizofrenia com mais robustez do que a
  transtornos de humor; verificar antes de estender.
- **GRIN2B** (subunidade GluN2B do NMDA) — alvo de fármacos experimentais seletivos (ex.:
  CP-101,606); variantes genéticas menos estudadas clinicamente do que o alvo farmacológico em si.
- **SLC1A2** (codifica EAAT2/GLT-1) — relevante à hipótese glial/glutamato, lastro ainda emergente
  em humor especificamente (mais estabelecido em epilepsia/ELA).

## 6. Sinalizadores de extrapolação — o que NÃO entra como fato

- **"Bloqueio de NMDA é o mecanismo do efeito antidepressivo da cetamina"** — apresentado com
  frequência como fato fechado; Zorumski, Izumi & Mennerick (2016) argumentam que a ligação entre o
  bloqueio de NMDA (bem documentado) e o efeito antidepressivo (também bem documentado) pode não ser
  causal direta — outros alvos (ex.: metabólito hidroxinorquetamina) foram propostos. Tratar como
  `[EMERGENTE]`.
- **"Déficit de GABA" como achado uniforme** — a maioria dos estudos de espectroscopia (MRS) mede
  GABA occipital ou pré-frontal em amostras pequenas, com técnica sensível a protocolo/campo
  magnético; tratar reduções de GABA cortical como achado replicado em direção, não como medida
  precisa e comparável entre estudos.
- **Subtipo de interneurônio (SST/PV) em humor como causa estabelecida** — a maior parte do lastro
  mecanístico vem de camundongo geneticamente modificado; a contrapartida humana é principalmente
  post-mortem (correlacional, não causal) → `[EXTRAPOLADO: animal→humano]` para a direção causal.
- **mGluR2/3 e neuroesteroides como "sucesso já provado"** — neuroesteroides têm aprovação
  regulatória para depressão pós-parto especificamente (evidência forte e localizada), não para
  depressão em geral; mGluR2/3 tem décadas de pesquisa pré-clínica robusta mas tradução clínica
  ainda mista — não generalizar o sucesso de um contexto estreito para o mecanismo inteiro.
- **Microbiota-GABA via vagal** — mecanismo com lastro majoritariamente pré-clínico (camundongo);
  tradução humana direta ainda escassa.

## 7. Cobertura equilibrada (não subrepresentar)

1. **GABA e glutamato como sistemas interdependentes**, não dois capítulos separados — o mecanismo
   da cetamina só faz sentido narrando os dois juntos (Seção 4).
2. **Neuroesteroides como capítulo próprio**, não rodapé do GABA-A — é fronteira regulatória real,
   não hipótese de bancada.
3. **Ansiedade com farmacologia de subunidade própria** (α2/α3 vs. α1) — mais fina do que "GABA
   baixo = mais ansiedade".
4. **O debate sobre o mecanismo real da cetamina** — incluir a voz cética (Zorumski 2016), não só a
   narrativa linear NMDA→mTOR.
5. **OCD e TEPT com literatura de glutamato/GABA própria** (cortico-estriado-tálamo-cortical no TOC;
   homeostase de cloreto no TEPT) — não colapsar toda a B5-ansiedade em "benzodiazepínico para
   pânico".
6. **Tradução clínica não-farmacológica** (D-cicloserina como potencializador de exposição) ao lado
   do eixo puramente farmacológico.

---

## 8. Camada clínica — evidência mapeada nesta sessão (ponto de partida; precisa de Rodada 2)

Tabela-semente. Cada PMID confirmado numa página que o cita explicitamente, durante busca ao vivo
nesta sessão (G1 caso a caso) — **não passou por G2/G3 nem pelos scripts de fidelidade**.

| Tema | Autor-ano | PMID | Tipo |
|---|---|---|---|
| Cetamina subanestésica produz sintomas psicotomiméticos em humanos saudáveis (marco histórico) | Krystal et al., 1994 | 8122957 | Estudo humano — marco |
| Cetamina aumenta liberação de glutamato no córtex pré-frontal (mecanismo) | Moghaddam et al., 1997 | 9092613 | Mecanístico (roedor) |
| **Primeiro ensaio controlado: cetamina tem efeito antidepressivo rápido** | Berman et al., 2000 | 10686270 | RCT — marco |
| **Cetamina em depressão resistente ao tratamento — réplica maior e mais rigorosa** | Zarate et al., 2006 | 16894061 | RCT — marco |
| **Antagonismo de NMDA desinibe neurônios piramidais via inibição de interneurônios GABAérgicos** | Homayoun & Moghaddam, 2007 | 17959792 | Mecanístico (roedor) — elo GABA↔glutamato |
| Riluzol (modulador glial de glutamato) como potencializador de antidepressivo | Sanacora et al., 2006 | 17141740 | Ensaio clínico piloto |
| Rumo a uma hipótese glutamatérgica da depressão (revisão de fronteira) | Sanacora, Treccani & Popoli, 2012 | 21827775 | Revisão |
| GABA cortical reduzido em pacientes deprimidos (primeira evidência por espectroscopia) | Sanacora et al., 1999 | 10565505 | Estudo humano (MRS) |
| Densidade reduzida de interneurônios GABAérgicos (calbindina+) no córtex occipital em depressão post-mortem | Maciag, Rajkowska et al., 2009 | 20004363 | Post-mortem humano |
| **Déficit de interneurônios GABAérgicos somatostatina+ na depressão (revisão)** | Fee, Banasr & Sibille, 2017 | 28697889 | Revisão |
| Disfunção GABAérgica cortical no estresse e depressão — liga ao mecanismo de ação rápida | Fogaça & Duman, 2019 | 30914923 | Revisão |
| **Subunidade α2 do GABA-A medeia ansiólise, dissociável do medo condicionado** | Smith, Engin, Meloni & Rudolph, 2012 | 22465203 | Mecanístico (camundongo) — âncora ANSIEDADE |
| Subunidade α5 do GABA-A também associada a efeito tipo-ansiolítico | Behlke et al., 2016 | 27067130 | Mecanístico (camundongo) — âncora ANSIEDADE |
| **Brexanolona (neuroesteroide IV) — ensaio de fase 2 em depressão pós-parto grave** | Kanes et al., 2017 | 28619476 | RCT — fronteira |
| **Brexanolona — dois ensaios de fase 3, base da aprovação FDA (Zulresso)** | Meltzer-Brody et al., 2018 | 30177236 | RCT fase 3 — fronteira |
| Zuranolona (neuroesteroide oral) vs. placebo em depressão pós-parto (estudo ROBIN) | Deligiannidis et al., 2021 | 34190962 | RCT — fronteira |
| **Zuranolona — estudo SKYLARK, base da aprovação FDA (Zurzuvae, 1º antidepressivo oral neuroesteroide)** | Deligiannidis et al., 2023 | 37491938 | RCT fase 3 — fronteira |
| Anormalidades de glutamato no TOC: neurobiologia, fisiopatologia e tratamento (revisão) | Pittenger, Bloch & Williams, 2011 | 21963369 | Revisão — âncora ANSIEDADE (TOC) |
| D-cicloserina (agonista parcial do sítio da glicina no NMDA) potencializa extinção do medo — tradução pré-clínico→clínico | Davis, Ressler, Rothbaum & Richardson, 2006 | 16919524 | Revisão translacional — âncora ANSIEDADE |

**O que falta (prioridade da Rodada 2):**
1. Confirmação dos PMIDs de Rudolph et al. 1999 (Nature — paper fundador da α2-ansiólise) e Ressler
   et al. 2004 (Arch Gen Psychiatry — primeiro ensaio humano de D-cicloserina); ambos entram por
   citação completa mas sem PMID nesta sessão.
   ambos ficaram só descritos por artigos-irmãos confirmados.
2. Mapa de ansiedade por transtorno específico (TAG, pânico, fobia social, TEPT) com o mesmo nível
   de detalhe que já existe aqui para TOC — TEPT/homeostase de cloreto e pânico/GABA-benzodiazepínico
   (desafio com flumazenil) ficaram só no checklist molecular (Seção 1b), sem PMID.
3. mGluR2/3 como classe farmacológica — nenhum PMID buscado ainda nesta sessão.
4. Literatura pós-2011 sobre GABA-B/baclofeno em humor (distinta de dependência química).

## 9. Tabela de confundidores de biomarcador (importar para BLOCO 05/11)

| Marcador / exame | Confundidor a controlar | Ação na busca |
|---|---|---|
| GABA cortical (MRS) | técnica sensível a campo magnético/protocolo de edição espectral; amostras tipicamente pequenas (n<40); mede região específica (occipital ≠ pré-frontal) | reportar campo/protocolo; não generalizar de uma região cortical para "GABA cerebral" |
| Glutamato cortical (MRS/¹³C-MRS) | resolução limitada entre glutamato e glutamina (Glx); estudos mais recentes usam ¹³C para separar, mas são raros | preferir estudos que reportem Glu separado de Gln quando a distinção importar |
| PET de receptor benzodiazepínico ([¹²³I]iomazenil, [¹¹C]flumazenil) | reflete densidade/afinidade de receptor, não neurotransmissão em tempo real; poucos estudos, amostras pequenas | tratar como complementar à MRS, não substituto |
| Interneurônios GABAérgicos (post-mortem) | causa vs. consequência indeterminável; efeito de medicação psiquiátrica no tecido; tempo post-mortem | controlar por exposição a medicação e intervalo post-mortem; não inferir causalidade |
| Alopregnanolona sérica | flutua com ciclo menstrual/gestação/parto; extração e ensaio variam entre laboratórios | padronizar momento da coleta em relação a ciclo/parto; especificar método de ensaio |

---

## 10. Estrutura-alvo da B5 (blocos do Prompt v4.2 — mesma numeração da B1/B3/B4)

- **BLOCO 02/03 (vias/mediadores):** GABA-A (subunidades, sítio benzodiazepínico, neuroesteroides)
  e GABA-B; NMDA/AMPA/mGluR; hipótese da desinibição como elo B5↔B3.
- **BLOCO 04 (células/estruturas):** interneurônios SST vs. PV; astrócitos (ciclo
  glutamato-glutamina, EAAT); circuito cortico-estriado-tálamo-cortical (TOC).
- **BLOCO 05 (biomarcadores):** + tabela de confundidores (Seção 9); MRS como técnica central e
  suas limitações.
- **BLOCO 06 (tradução clínica):** depressão (cetamina/esketamina, neuroesteroides, riluzol) e
  **ansiedade** (benzodiazepínicos por subunidade, D-cicloserina em exposição, glutamato no TOC) —
  descritos sem prescrever (P20).
- **BLOCO 08 (crosstalk):** ver Seção 4 — B5↔B1/B2/B3/B4/B6-B9/B7/B13; destacar B5↔B3 como fronteira
  conceitual mais tênue de toda a série e B5↔B13 como o mais mecanisticamente fechado.
- **BLOCO 11 (estratificação):** eixo "hiperexcitável" (glutamato predominante, ex.: TOC) vs.
  "hipoinibido" (déficit GABAérgico predominante, ex.: subtipo de depressão) — não necessariamente
  mutuamente exclusivos no mesmo paciente.
- **BLOCO 12 (cenários):** cenário depressão-resistente-responsiva-a-cetamina, cenário TOC com
  hiperatividade glutamatérgica cortico-estriatal, cenário depressão-pós-parto-neuroesteroide.

## 11. Plano de execução

1. **Rodada 1 (miolo molecular):** aprofundar mGluR2/3, GABA-B/baclofeno e homeostase de cloreto
   (KCC2/NKCC1) em TEPT — ficaram só no checklist molecular (Seção 1b), sem PMID nesta sessão.
2. **Rodada 2 (corpus eutils):** fechar o mapa de ansiedade por transtorno (TAG, pânico, fobia
   social, TEPT) no mesmo padrão que já existe aqui para TOC; confirmar os dois PMIDs pendentes
   (Rudolph 1999, Ressler 2004).
3. **Rodada 3 (fidelidade):** rodar `check_fidelidade_b1` e `check_troca_nomes`; conferir que a
   seção sobre o debate NMDA-é-mesmo-o-gatilho (Zorumski 2016) não resolveu a disputa por conta
   própria; verificar que B5↔B3 está delimitado do mesmo jeito nos dois documentos.
4. Publicar como **B5 v1** — não há canônica anterior para congelar.

> **Nota sobre profundidade:** esta B5 tem quase o dobro de PMIDs confirmados da B3/B4 (19 vs.
> 13-14), reflexo direto do pedido por profundidade máxima — não de a B5 ter mais evidência
> disponível na literatura por si só. Ao comparar as três, vale lembrar que a diferença de tamanho
> é, em parte, artefato de quanto tempo de busca foi investido em cada uma nesta sessão, não uma
> medida objetiva de qual mecanismo tem mais base científica.
