# Mecanismo B15 — Autofagia–mTOR na Ansiedade e Depressão

**Briefing científico completo, incluindo ciência de fronteira (2024–2026)**

---

## Nota metodológica sobre os PMIDs

Todos os PMIDs listados na Seção 12 foram **verificados individualmente por busca direta** (título + PMID conferidos contra a página do PubMed/PMC ou contra o registro cruzado do próprio editor). Nenhum PMID foi gerado de memória. Onde não consegui confirmar um PMID com segurança (por exemplo, alguns achados citados apenas indiretamente dentro de outras revisões), preferi **não incluir** a citação a arriscar um número incorreto — nesses casos, o achado é mencionado no texto sem número de referência, ou omitido.

Uma referência (nº 27, espermidina) é um **preprint do bioRxiv**, não um artigo revisado por pares publicado em periódico — isso está sinalizado explicitamente onde aparece, porque é a fronteira mais "crua" de tudo o que está aqui.

---

## 1. Resumo executivo

A autofagia (processo de degradação e reciclagem de organelas e proteínas danificadas) e a via mTOR (mechanistic/mammalian target of rapamycin) formam um eixo regulatório que é hoje um dos mecanismos mais discutidos em psiquiatria biológica para depressão e, em menor volume de estudos, para ansiedade. O quadro que emerge da literatura **não é uma linha reta** do tipo "mais autofagia é sempre melhor" ou "mTOR é sempre vilão". Em vez disso, há pelo menos quatro camadas de complexidade que qualquer resumo honesto precisa registrar:

1. **mTORC1 agudo e sináptico é bom**: a ativação rápida e transitória de mTORC1 no córtex pré-frontal está por trás do efeito antidepressivo de ação rápida da cetamina — é o mecanismo mais replicado desta área inteira.
2. **mTOR cronicamente deprimido é ruim**: em tecido pós-morte de pacientes com depressão maior, a sinalização mTOR no córtex pré-frontal está reduzida, não aumentada.
3. **Autofagia insuficiente e autofagia excessiva podem, ambas, ser prejudiciais**, dependendo da região cerebral, do tipo celular e da cronicidade do estresse — há estudos mostrando o padrão em ambas as direções.
4. **A fronteira mais recente (2023–2026) está migrando da "autofagia geral" para a mitofagia especificamente** (remoção seletiva de mitocôndrias danificadas) e para moduladores farmacológicos diretos de mTORC1 e de mitofagia, incluindo o primeiro ensaio clínico de fase 1b/2 em humanos com um ativador direto de mTORC1 (NV-5138), publicado já em 2026.

---

## 2. Fundamentos moleculares

### 2.1 Autofagia — o essencial

Autofagia é o processo pelo qual a célula envolve componentes citoplasmáticos danificados (proteínas mal dobradas, organelas disfuncionais) em uma vesícula de dupla membrana (autofagossomo), que depois se funde ao lisossomo para degradação. Existem três formas principais: macroautofagia (a mais estudada em neurociência), microautofagia e autofagia mediada por chaperonas (CMA). Um subtipo seletivo especialmente relevante para humor é a **mitofagia** — a remoção seletiva de mitocôndrias danificadas, mediada principalmente pelas vias PINK1/Parkin e por receptores como BNIP3L/NIX.

### 2.2 A via mTOR

mTOR é uma serina/treonina-cinase que forma dois complexos com funções distintas:
- **mTORC1** (com RAPTOR): sensível a rapamicina; integra sinais de nutrientes, energia e fatores de crescimento; controla síntese proteica (via p70S6K e 4E-BP1) e **inibe** a autofagia ao fosforilar o complexo ULK1.
- **mTORC2** (com RICTOR): menos sensível a rapamicina em curto prazo; regula citoesqueleto de actina e sobrevivência celular via AKT.

A relação central é: **mTORC1 ativo = freio da autofagia**; quando mTORC1 é inibido (por jejum, rapamicina, ou ativação de AMPK), a autofagia é destravada.

### 2.3 Principais moléculas do eixo (referência rápida)

| Molécula | Papel | Relação com humor |
|---|---|---|
| mTORC1 | Inibe autofagia; promove síntese proteica/sinaptogênese | Ativação aguda = efeito antidepressivo rápido (cetamina) |
| AMPK | Sensor de energia; inibe mTORC1; ativa ULK1 | Ativado por exercício, restrição calórica; via alternativa de indução de autofagia |
| ULK1 | Cinase iniciadora da autofagia | Alvo direto de inibição por mTORC1 |
| Beclin-1 (BECN1) | Nucleação do autofagossomo | Biomarcador sérico candidato de resposta a antidepressivo |
| LC3-I/LC3-II | Conjugação à membrana do autofagossomo (marcador padrão de fluxo autofágico) | Reduzido em astrócitos do córtex pré-frontal na depressão maior |
| p62/SQSTM1 | Adaptador degradado durante autofagia (acumula quando autofagia falha) | Usado como marcador inverso de fluxo autofágico |
| BNIP3L/NIX | Receptor de mitofagia | Reduzido no sangue de pacientes com depressão maior; alvo da cetamina |
| PINK1/Parkin | Via clássica de mitofagia | Envolvida em modelos de depressão pós-parto e mitofagia hipocampal |
| FKBP5/FKBP51 | Co-chaperona do receptor de glicocorticoide; regula Beclin-1 | Elo mecanístico entre estresse, eixo HPA e indução de autofagia por antidepressivos |
| TFEB | Fator de transcrição mestre da biogênese lisossomal/autofagia | Mencionado como alvo terapêutico emergente em revisões recentes |

---

## 3. Autofagia–mTOR na depressão

### 3.1 Evidência humana direta

O achado fundacional em tecido humano é de **Jernigan et al. (2011)** [2]: em amostras de córtex pré-frontal post-mortem de pacientes com transtorno depressivo maior (TDM), houve redução significativa de mTOR, p70S6K e eIF4B fosforilado em comparação com controles pareados por idade — ou seja, **sinalização mTOR reduzida**, não aumentada, no tecido cerebral de quem morreu deprimido.

Em sangue periférico, dois achados clínicos se destacam:
- **Beclin-1 sérico** foi testado como biomarcador preditivo de resposta a antidepressivos (ISRS/IRSN) em pacientes chineses com TDM: níveis basais mais altos de Beclin-1 se associaram a *pior* resposta ao tratamento, e Beclin-1 aumentou nos respondedores após 8 semanas [8].
- **LC3A em sangue total** foi identificado, por sequenciamento de núcleo único combinado com dados transcriptômicos de tecido pós-morte, como reduzido em astrócitos do córtex pré-frontal de pacientes com TDM, com correlação negativa entre LC3A no sangue e gravidade dos sintomas depressivos — um candidato a biomarcador diagnóstico [9].

### 3.2 Modelos animais de estresse crônico

Múltiplos paradigmas de estresse crônico (estresse crônico imprevisível/CUMS, derrota social crônica, restrição crônica) convergem em alterações de autofagia no hipocampo e em outras regiões límbicas, mas a **direção do efeito varia por região e por desenho experimental**:

- No hipocampo, o padrão mais comum descrito é de **autofagia insuficiente/bloqueada** contribuindo para morte de células-tronco neurais e prejuízo de neurogênese adulta. Um estudo de 2023 mostrou que a proteína NRBF2 (componente do complexo VPS34) fica reduzida no giro denteado sob estresse crônico; sua deficiência prejudica o fluxo autofágico em células-tronco neurais adultas e causa fenótipo depressivo, enquanto superexpressá-la resgata neurogênese e comportamento [18].
- Em contraste direto, um estudo usando um paradigma de estresse com/sem controle comportamental (executive vs. yoke) mostrou o oposto: animais sem controle sobre o estressor desenvolveram **hiperatividade do fluxo autofágico** no hipocampo ventral, e bloquear farmacologicamente essa autofagia (com 3-metiladenina) preveniu o comportamento do tipo depressivo [19]. Ou seja, **excesso de autofagia também pode ser patogênico**, não apenas a falta dela.
- Um achado de 2025 na *Nature* deslocou o foco da amígdala/hipocampo para o **núcleo habenular lateral (LHb)**: estresse agudo ativa a autofagia nessa região, enquanto estresse crônico a suprime; restaurar farmacológica ou geneticamente a autofagia no LHb produziu efeito antidepressivo rápido, e antidepressivos de classes distintas convergiram em restaurar essa autofagia — apontando o LHb como um alvo comum e até então pouco explorado [21].

### 3.3 Mitofagia e neuroinflamação especificamente

Uma linha de pesquisa mais recente enfoca não a autofagia geral, mas a mitofagia:

- **BNIP3L/NIX**: o TNF-α (citocina inflamatória associada a estresse) degrada NIX no córtex pré-frontal, bloqueando a mitofagia e causando acúmulo de mitocôndrias danificadas, disfunção sináptica e comportamento de enfrentamento passivo ao estresse em camundongos. Notavelmente, a cetamina reverte esse quadro ativando a mitofagia dependente de NIX, e NIX está reduzido no sangue de pacientes com TDM e em tecido de modelos animais — um dos elos mais diretos entre inflamação, mitofagia e mecanismo de ação da cetamina descritos até agora [12].
- **Eixo ApoE–complemento–mTOR–autofagia**: um estudo de 2025 mostrou que a ausência de ApoE (apolipoproteína E) em camundongos leva à hiperativação de microglia, elevação do complemento C3, ativação sustentada de mTOR, bloqueio de autofagia hipocampal e comportamento depressivo — revertido com rapamicina (inibidor de mTOR) [22]. Isso conecta este mecanismo à literatura de neuroinflamação e, potencialmente, a fatores de risco genético já conhecidos em outras doenças (ApoE é o principal gene de risco para Alzheimer de início tardio).

---

## 4. Autofagia–mTOR na ansiedade

A literatura sobre ansiedade especificamente é menor que a de depressão, mas cresceu de forma notável nos últimos dois anos, com foco principal na **amígdala** e, mais recentemente, no **núcleo accumbens**.

### 4.1 Amígdala

- Em um modelo de TEPT (transtorno de estresse pós-traumático) em camundongos, a inibição da autofagia especificamente na amígdala (e não no córtex pré-frontal medial ou hipocampo) foi suficiente para reduzir comportamentos do tipo ansioso — sugerindo que, nessa região e nesse contexto, é o **excesso** de autofagia que é anxiogênico, um padrão que contrasta com o LHb, onde é a **falta** de autofagia que piora o quadro [16].
- Em um modelo de ansiedade induzida por abstinência prolongada de morfina, o mesmo padrão se repetiu: a abstinência aumentou marcadores de autofagia (ATG5, Beclin-1, LC3) especificamente na amígdala, e o inibidor de autofagia 3-metiladenina atenuou o comportamento ansioso [17].

### 4.2 Núcleo accumbens e mitofagia — Urolithin A

O achado mais robusto e recente de toda essa seção vem de um estudo publicado em 2025/2026 na *Biological Psychiatry*, do grupo de Carmen Sandi (EPFL), em colaboração com a Columbia University: usando dois modelos independentes de ansiedade elevada em ratos, os autores mostraram que a **mitofagia** (não a autofagia geral) estava consistentemente desregulada em neurônios espinhosos médios do núcleo accumbens de animais ansiosos, e que a suplementação crônica com **Urolithin A** (metabólito derivado da microbiota intestinal a partir de elagitaninos de romã e frutas vermelhas) restaurou a via de mitofagia, a estrutura sináptica e **aboliu o comportamento ansioso** nos dois modelos, sem afetar animais com ansiedade basal normal [28]. Um comentário editorial que acompanhou o artigo destacou isso como uma possível estratégia nutricional/farmacológica dirigida à mitocôndria, sem os efeitos colaterais típicos de ansiolíticos clássicos [29]. Como Urolithin A já tem segurança estabelecida em humanos, os autores indicaram que ensaios clínicos são o próximo passo natural.

Um segundo estudo, também de 2025/2026, mostrou que Urolithin A melhora comprometimento cognitivo e ansiedade induzidos por privação crônica de sono em camundongos, por um mecanismo que envolve supressão de ferroptose hipocampal via sinalização Nrf2 — uma via distinta, mas convergente, de proteção mitocondrial/oxidativa [30].

---

## 5. Cetamina: o elo central entre mTOR/autofagia e efeito antidepressivo rápido

Se há um "hub" que conecta praticamente todas as partes deste mecanismo, é a cetamina.

### 5.1 O achado fundacional (2010)

O estudo de Li e colegas, publicado na *Science*, é a pedra fundamental de todo este campo: uma dose única de cetamina ativa rapidamente mTOR no córtex pré-frontal de ratos, aumentando proteínas sinápticas e a densidade de espinhas dendríticas; bloquear a sinalização de mTOR (com rapamicina infundida localmente) **aboliu completamente** tanto a sinaptogênese quanto o efeito comportamental do tipo antidepressivo [1]. Esse resultado — mTORC1 como necessário e suficiente para o efeito rápido da cetamina — foi replicado e estendido dezenas de vezes na década seguinte.

### 5.2 Autofagia como componente adicional (não apenas mTORC1)

Estudos mais recentes mostraram que o quadro é mais rico do que "cetamina ativa mTORC1 e ponto":
- Em microglia do córtex pré-frontal e hipocampo, cetamina em dose subanestésica **induz autofagia** (aumento de LC3B, redução de p62), e esse efeito está associado à supressão do inflamassoma NLRP3 e à redução de IL-1β; bloquear a autofagia com bafilomicina A1 anulou tanto o efeito anti-inflamatório quanto o comportamental da cetamina [10].
- Cetamina também restaura funções astrocitárias prejudicadas em modelos de depressão [11].
- Como já descrito na Seção 3.3, cetamina reverte déficits de mitofagia mediada por NIX causados por TNF-α [12].

### 5.3 O paradoxo da rapamicina

Aqui está uma das maiores tensões não resolvidas da área. Se mTORC1 é necessário para o efeito da cetamina, inibir mTORC1 com rapamicina deveria sempre bloquear esse efeito — e em alguns paradigmas pré-clínicos isso é exatamente o que acontece, de forma dependente da tarefa comportamental testada [13]. Mas em um ensaio clínico randomizado, duplo-cego, cross-over, em 20 pacientes com episódio depressivo maior, pré-tratamento com rapamicina oral (6 mg) antes da infusão de cetamina **não bloqueou** o efeito antidepressivo em 24 horas e, surpreendentemente, **prolongou** a resposta e aumentou as taxas de resposta/remissão em duas semanas de acompanhamento (47% vs. 13% no grupo placebo+cetamina, no relato de um estudo relacionado) [14]. Os próprios autores levantaram a hipótese de que a rapamicina pode estar agindo por uma via que envolve estabilização de autofagia/densidade sináptica a médio prazo, distinta do mecanismo agudo de sinaptogênese dependente de mTORC1. Esse resultado é citado repetidamente na literatura mais recente como evidência de que a relação mTOR–autofagia–humor não é uma via de mão única.

### 5.4 Ativação direta de mTORC1 sem NMDA — já em humanos

Paralelamente à cetamina, existe uma linha de desenvolvimento farmacêutico baseada em ativar mTORC1 diretamente, sem passar pelo receptor NMDA:

- **NV-5138 (mefluleucina)**, um análogo sintético de leucina que se liga à sestrina e ativa mTORC1 diretamente no cérebro, produziu efeito antidepressivo rápido e revertida de anedonia em roedores, dependente de liberação de BDNF [23].
- Isso avançou para humanos: um ensaio clínico fase 1b, randomizado, duplo-cego, controlado por placebo, publicado em 2026, testou dose única de NV-5138 (2400 mg) em pacientes com depressão resistente a tratamento. Houve melhora significativa em escalas de depressão já em 4 e 12 horas após a dose, com tamanhos de efeito entre -0,5 e -0,8, sem eventos psicotomiméticos — o desenho do estudo foi explicitamente pensado para capturar respostas rápidas do tipo "estilo cetamina" [24]. Um estudo de fase 2 com dose diária por 4 semanas está registrado como próximo passo.

---

## 6. Antidepressivos convencionais e indução de autofagia (o eixo FKBP5)

Também existe evidência de que antidepressivos monoaminérgicos "clássicos" (ISRS, IRSN, tricíclicos) — não apenas cetamina — dependem, ao menos em parte, de indução de autofagia. O trabalho mais citado aqui é o de **Gassen e colegas**: a co-chaperona FKBP5/FKBP51 (reguladora do receptor de glicocorticoide, já associada geneticamente a risco e resposta a tratamento em depressão) se associa a Beclin-1, altera sua fosforilação e **aumenta marcadores de autofagia**; os efeitos comportamentais e fisiológicos de antidepressivos em células, camundongos e humanos dependeram da presença de FKBP5 nos experimentos realizados [6,7]. Uma revisão de 2019 dos mesmos autores sintetiza essa linha inteira de evidência e é hoje uma referência-padrão do campo [4]. Um artigo mais recente (2025) estendeu esse mecanismo mostrando que FKBP5 participa da montagem do complexo VPS34 necessário para iniciar a autofagia — aprofundando o mecanismo molecular exato dessa associação.

Um exemplo adicional, vindo da farmacologia de plantas medicinais chinesas, é o Xiaoyaosan, uma formulação tradicional com efeito antidepressivo demonstrado em modelos animais, cujo mecanismo parece envolver regulação de autofagia e da expressão de GLUT4 em neurônios hipotalâmicos — um exemplo de como a "medicina tradicional" está sendo reanalisada sob a lente exata desse mecanismo molecular [20].

---

## 7. Ciência de fronteira (2024–2026): o que está realmente na ponta agora

Reunindo o que há de mais recente e ainda em consolidação:

1. **Núcleo habenular lateral como alvo comum de antidepressivos (Nature, 2025)** — já descrito na Seção 3.2 [21]. É provavelmente o achado conceitualmente mais importante do período recente, porque propõe uma região cerebral específica e um mecanismo (autofagia dependente da via de degradação de receptores de glutamato) como ponto de convergência de antidepressivos com mecanismos farmacológicos muito diferentes entre si.

2. **Espermidina como intervenção metabólica para depressão** — esta é a peça mais "quente" e, ao mesmo tempo, a menos madura cientificamente do conjunto todo. Um estudo epidemiológico com dados do NHANES (2005–2014, mais de 19 mil participantes) encontrou associação inversa entre ingestão dietética de espermidina e sintomas depressivos, publicado no *Journal of Affective Disorders* [26]. Mais adiante na cadeia de evidência, um grupo liderado por Frank Madeo, Guido Kroemer e Nils Gassen — pesquisadores centrais no campo mundial de autofagia — depositou em dezembro de 2024 um preprint (ainda não publicado em periódico com revisão por pares completa até a elaboração deste briefing) relatando que o estresse agudo desregula o metabolismo de poliaminas e aumenta o fluxo autofágico em humanos e camundongos; que antidepressivos convencionais aumentam espermidina plasmática **apenas em quem responde ao tratamento**; e que, em um ensaio clínico controlado por placebo, três semanas de suplementação de espermidina em pacientes deprimidos sem tratamento farmacológico prévio aumentou autofagia e melhorou sintomas depressivos [27]. **Friso**: por ser preprint, esse achado precisa ser lido com uma reserva de cautela maior do que qualquer outra referência deste documento — não passou por revisão por pares completa em uma revista até o momento desta pesquisa.

3. **Psilocibina via BDNF–mTORC1** — um estudo de 2024 mostrou que psilocibina produz efeito antidepressivo rápido e sustentado em camundongos expostos a corticosterona crônica, associado a ativação da via BDNF–TrkB–mTOR e aumento de neurogênese no giro denteado — posicionando psicodélicos clássicos dentro da mesma arquitetura mecanística da cetamina, embora por receptor de entrada diferente (5-HT2A em vez de NMDA) [25].

4. **Ativadores diretos de mTORC1 já testados em humanos (NV-5138)** — Seção 5.4, PMIDs [23,24]. Esse é provavelmente o desenvolvimento mais avançado clinicamente de toda esta lista, com ensaio de fase 2 já em andamento.

5. **Mitofagia como alvo mais específico que "autofagia" em geral** — Urolithin A/B para ansiedade e depressão [28,29,30], BNIP3L/NIX [12], e uma revisão de 2023 dedicada especificamente a "targeting mitophagy for depression amelioration" como estratégia terapêutica emergente e ainda pouco explorada clinicamente [31].

6. **Eixo ApoE–complemento–mTOR** [22] — uma ponte potencialmente importante entre a literatura de neuroinflamação/Alzheimer e a de depressão, ainda muito recente (2025).

---

## 8. Diferenças de sexo

Autofagia é regulada de forma sexualmente dimórfica em múltiplos sistemas (câncer, doença cardiovascular, neurodegeneração, resposta a isquemia cerebral), com hormônios esteroides sexuais modulando diretamente componentes da via, incluindo BECN1 e sinalização mTOR [32]. Isso ainda não foi mapeado de forma sistemática especificamente para depressão/ansiedade, mas é uma lacuna reconhecida na literatura — a maioria dos estudos pré-clínicos de autofagia-humor citados neste briefing foi conduzida majoritariamente ou exclusivamente em machos, o que limita a generalização, especialmente considerando que depressão e transtornos de ansiedade são mais prevalentes em mulheres.

---

## 9. Controvérsias e não-linearidades (o que uma leitura simplista erraria)

- **"Ativar mTOR é bom" e "ativar mTOR é ruim" são ambos verdadeiros**, dependendo do contexto: ativação aguda/sináptica (cetamina) é antidepressiva; supressão crônica basal (achado post-mortem) caracteriza o estado depressivo; e inibição farmacológica de mTOR com rapamicina tanto bloqueia quanto — em outro desenho — prolonga o efeito da cetamina.
- **"Mais autofagia é sempre protetora" é falso**: no LHb, restaurar autofagia é antidepressivo; na amígdala, em pelo menos dois modelos (TEPT e abstinência de morfina), é a *redução* da autofagia que é ansiolítica. A direção do efeito parece depender fortemente da região cerebral e do tipo de estressor.
- A maior parte da evidência mecanística ainda vem de **roedores**; a evidência humana direta é mais escassa e concentrada em: (a) tecido post-morte, (b) biomarcadores séricos/sanguíneos, e (c) um punhado de ensaios clínicos farmacológicos (rapamicina+cetamina; NV-5138; espermidine, este último ainda em preprint).
- Não há, até o momento desta pesquisa, um consenso sobre se medir "autofagia" perifericamente (sangue) reflete de forma confiável o que acontece no tecido cerebral — os biomarcadores (Beclin-1, LC3A) são promissores, mas preliminares.

---

## 10. Implicações terapêuticas emergentes (síntese)

| Abordagem | Estágio | Mecanismo proposto |
|---|---|---|
| Cetamina/escetamina | Aprovada clinicamente (uso já estabelecido) | Ativação de mTORC1 + autofagia + mitofagia via NIX |
| Rapamicina como adjuvante da cetamina | Ensaio clínico piloto positivo | Prolongamento do efeito, mecanismo ainda incerto |
| NV-5138 (mefluleucina) | Fase 2 em andamento | Ativação direta de mTORC1 via sestrina, sem NMDA |
| Psilocibina | Ensaios clínicos em estágio avançado (para depressão em geral) | BDNF–TrkB–mTOR, neuroplasticidade |
| Urolithin A | Segurança estabelecida em humanos; ensaios para ansiedade ainda não iniciados | Restauração de mitofagia no núcleo accumbens |
| Espermidina | Epidemiologia + 1 ensaio clínico piloto (preprint) | Indução de autofagia via metabolismo de poliaminas |
| Exercício físico / restrição calórica | Uso já recomendado clinicamente por outras razões | Ativação de AMPK → indução de autofagia |

---

## 11. O que ainda falta (lacunas explícitas)

- Ensaios clínicos randomizados, com poder estatístico adequado, testando indutores de autofagia/mitofagia *isoladamente* (sem cetamina) para depressão ou ansiedade em humanos são praticamente inexistentes fora do que foi listado acima.
- Faltam estudos de imagem molecular em humanos vivos que consigam medir autofagia ou mitofagia diretamente no cérebro (hoje isso só é possível post-mortem ou por biomarcador periférico indireto).
- A literatura de ansiedade (em oposição à depressão) ainda é numericamente pequena e concentrada em 2024–2026 — é a parte deste mecanismo que mais provavelmente vai mudar nos próximos 2–3 anos.

---

## 12. Lista de PMIDs validados (referências completas)

*Todos verificados por busca direta em 07/09/2026. Formato: [nº] Autores (quando disponíveis). Título. Periódico. Ano;volume(número):páginas. PMID.*

1. Li N, Lee B, Liu RJ, Banasr M, Dwyer JM, Iwata M, Li XY, Aghajanian G, Duman RS. mTOR-dependent synapse formation underlies the rapid antidepressant effects of NMDA antagonists. *Science*. 2010;329(5994):959-964. **PMID: 20724638**

2. Jernigan CS, Goswami DB, Austin MC, Iyo AH, Chandran A, Stockmeier CA, Karolewicz B. The mTOR signaling pathway in the prefrontal cortex is compromised in major depressive disorder. *Prog Neuropsychopharmacol Biol Psychiatry*. 2011;35(7):1774-1779. **PMID: 21635931**

3. Role of mTOR1 signaling in the antidepressant effects of ketamine and the potential of mTORC1 activators as novel antidepressants (revisão). *Neuropharmacology*. 2022. **PMID: 36334763**

4. Gassen NC, Rein T. Is There a Role of Autophagy in Depression and Antidepressant Action? *Front Psychiatry*. 2019;10:337. **PMID: 31156481**

5. Autophagy Modulation by Antidepressants: Mechanisms and Implications (revisão). *Neurochemical Research*. 2025. **PMID: 40906308**

6. Gassen NC, Hartmann J, Zschocke J, et al. Association of FKBP51 with Priming of Autophagy Pathways and Mediation of Antidepressant Treatment Response: Evidence in Cells, Mice, and Humans. *PLOS Medicine*. 2014. **PMID: 25386878**

7. Gassen NC, Hartmann J, Schmidt MV, Rein T. FKBP5/FKBP51 enhances autophagy to synergize with antidepressant action. *Autophagy*. 2015. **PMID: 25714272**

8. He S, Zeng D, Xu F, et al. Baseline Serum Levels of Beclin-1, but Not Inflammatory Factors, May Predict Antidepressant Treatment Response in Chinese Han Patients With MDD. *Front Psychiatry*. 2019;10:378. **PMID: 31244689**

9. He S, Shi Y, Ye J, et al. Does decreased autophagy and dysregulation of LC3A in astrocytes play a role in major depressive disorder? *Transl Psychiatry*. 2023;13:362. **PMID: 38001115**

10. Lyu D, Wang F, Zhang M, et al. Ketamine induces rapid antidepressant effects via the autophagy-NLRP3 inflammasome pathway. *Psychopharmacology*. 2022. **PMID: 35925279**

11. Rapid and sustained restoration of astrocytic functions by ketamine in depression model mice. *Biochem Biophys Res Commun*. 2022;616:89-94. **PMID: 35653826**

12. Lu JJ, Wu PF, He JG, et al. BNIP3L/NIX-mediated mitophagy alleviates passive stress-coping behaviors induced by tumor necrosis factor-α. *Mol Psychiatry*. 2023;28:5062-5076. **PMID: 36914810**

13. Rapamycin blocks the antidepressant effect of ketamine in task-dependent manner. 2016. **PMID: 27004790**

14. Abdallah CG, Averill LA, Gueorguieva R, et al. Modulation of the antidepressant effects of ketamine by the mTORC1 inhibitor rapamycin. *Neuropsychopharmacology*. 2020;45(6):990-997. **PMID: 32092760**

15. Targeting inflammation in depression: Ketamine as an anti-inflammatory antidepressant in psychiatric emergency (revisão). 2021. **PMID: 34849492**

16. The downregulation of Autophagy in amygdala is sufficient to alleviate anxiety-like behaviors in Post-traumatic Stress Disorder model mice. *Transl Psychiatry*. 2025. **PMID: 41073381**

17. Han S, Zhu C, Min D, Li Z. Inhibition of autophagy in the amygdala ameliorates anxiety-like behaviors induced by morphine-protracted withdrawal in male mice. *NeuroReport*. 2025;36(9):487-496. **PMID: 40269606**

18. Zhang SQ, Deng Q, Zhu Q, et al. Cell type-specific NRBF2 orchestrates autophagic flux and adult hippocampal neurogenesis in chronic stress-induced depression. *Cell Discovery*. 2023;9:90. **PMID: 37644025**

19. Liao YH, Chan YH, Chen H, et al. Stress while lacking of control induces ventral hippocampal autophagic flux hyperactivity and a depression-like behavior. *Biomed J*. 2022;45(6):896-906. **PMID: 34971825**

20. Yang FR, Zhu XX, Kong MW, et al. Xiaoyaosan Exerts Antidepressant-Like Effect by Regulating Autophagy Involves the Expression of GLUT4 in the Mice Hypothalamic Neurons. *Front Pharmacol*. 2022;13:873646. **PMID: 35784760**

21. Yang L, Guo C, Zheng Z, et al. Stress dynamically modulates neuronal autophagy to gate depression onset. *Nature*. 2025;641(8062):427-437. **PMID: 40205038**

22. Targeting the complement-mTOR-autophagy axis: the role of apolipoprotein E in depression. 2025. **PMID: 40722026**

23. Kato T, Pothula S, Liu RJ, et al. Sestrin modulator NV-5138 produces rapid antidepressant effects via direct mTORC1 activation. *J Clin Invest*. 2019;129(6):2542-2554. **PMID: 30990795**

24. Targum SD, Sanacora G, Formella AE, Ceresoli-Borroni G, Owen R. A novel, experimental design to assess rapid antidepressant action: results from a phase 1b randomized trial of NV-5138. *J Psychiatr Res*. 2026;194:211-220. **PMID: 41512716**

25. Zhao X, Du Y, Yao Y, et al. Psilocybin promotes neuroplasticity and induces rapid and sustained antidepressant-like effects in mice. *J Psychopharmacol*. 2024;38(5):489-499. **PMID: 38680011**

26. Qi G, Wang J, Chen Y, Wei W, Sun C. Association between dietary spermidine intake and depressive symptoms among US adults: National Health and Nutrition Examination Survey (NHANES) 2005-2014. *J Affect Disord*. 2024;359:125-132. **PMID: 38729223**

27. Mackert S, Niemeyer C, Mecdad Y, et al. Spermidine alleviates depression via control of the stress response. *bioRxiv* [preprint]. 2024. **PMID: 39677641** — ⚠️ **PREPRINT, ainda sem publicação revisada por pares em periódico até a data desta pesquisa.**

28. Mallet D, Ülgen DH, Grosse J, et al. Urolithin A abolishes high anxiety and rescues the associated mitochondria-related transcriptomic signatures and synaptic function. *Biological Psychiatry*. 2025/2026;100(1):14-29. **PMID: 40752777**

29. Chaudhari PR, Vaidya VA. Urolithin A: A Mitochondrial Remedy for the Anxious Mind. *Biological Psychiatry*. 2026;100(1):4-6. **PMID: 42270169**

30. Urolithin A supplementation improves chronic sleep deprivation-induced cognitive impairments and anxiety in mice by suppressing hippocampal ferroptosis via the Nrf2 signaling. **PMID: 42372600**

31. Xu W, Gao W, Guo Y, et al. Targeting mitophagy for depression amelioration: a novel therapeutic strategy. *Front Neurosci*. 2023;17:1235241. **PMID: 37869512**

32. Shang D, Wang L, Klionsky DJ, Cheng H, Zhou R. Sex differences in autophagy-mediated diseases: toward precision medicine. *Autophagy*. 2021;17(5):1065-1076. **PMID: 32264724**

---

*Todos os PMIDs acima podem ser conferidos diretamente em: `https://pubmed.ncbi.nlm.nih.gov/[PMID]/`*
