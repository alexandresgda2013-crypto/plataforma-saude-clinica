# GERADOR DE PROFUNDIDADE MOLECULAR (GPM) — PARTE 1
## Mecanismo: B11 — Disfunção Tireoidiana (Eixo HPT / Hormônios Tireoidianos / Sinalização Tireoidiana Central) em Ansiedade e Depressão
### (Módulos 00–05 · Parte 2 = Módulos 06–10, a gerar após liberação)

> Geração conforme **Molde GPM v2.0**. Citações no corpo em **(Autor, Ano)**; ao fim de cada
> item, origem da evidência **+ natureza da relação + maturidade**; ao fim de cada módulo, âncora
> `[REF_MODULO_XX: Autor_Ano | ...]`. Os **PMIDs verificados** (153 âncoras, 14 blocos A–N)
> permanecem no **Briefing B11 consolidado** (pré-caça eutils/PubMed + insumo mecanístico A +
> insumo consolidado B + relatório Consensus C, todos auditados) e são a chave
> frase↔referência para o G1→G2→G3 da Rodada 2 — o GPM **aponta território**, não substitui a
> verificação. **Sem medicamentos/suplementos/intervenções como conteúdo** (proibição do molde):
> levotiroxina, liotironina/T3, a terapia combinada T4+T3, a *augmentation* com T3 na depressão
> resistente e o lítio entram apenas como **sinal experimental/clínico de plasticidade do eixo**,
> nunca como prescrição; vivem no Briefing e entram na Biblioteca via Prompt 4.2.
>
> **Regras fundadoras deste mecanismo.**
> (1) ***TSH é um marcador dentro do sistema, não o mecanismo* — B11 ≠ TSH ≠ hipotireoidismo.**
> O mecanismo compreende todo o percurso do hormônio: eixo HPT → transporte através da barreira
> (MCT8/OATP1C1) → conversão local por desiodinases (D2/D3) → receptores nucleares (TRα/β) →
> expressão gênica → circuitos de humor/ansiedade.
> (2) **Relação em U / não-linear:** não é "pouco hormônio → depressão". Tanto a deficiência
> quanto o excesso de hormônio tireoidiano associam-se a depressão/ansiedade; o alvo biológico é
> a **homeostase**, não a reposição indiscriminada.
> (3) **Separar doença periférica de sinalização central:** a doença tireoidiana periférica
> (hipo/hiper/autoimune) é, em humanos, majoritariamente um **fator de risco associativo, modesto
> e bidirecional**; a **sinalização tireoidiana central** (transporte/conversão/receptor neurais)
> tem lastro **causal em modelo animal/molecular**. As duas coisas convivem e não devem ser
> confundidas.
> (4) **Evidência negativa é parte do mecanismo:** no hipotireoidismo subclínico, os dados
> prospectivos e o ensaio randomizado de maior peso **não** sustentam causalidade forte nem
> benefício de normalizar o TSH sobre o sintoma subjetivo — "normalizar o biomarcador ≠ tratar o
> quadro".

---

## MÓDULO 00 — METADADOS E ESCOPO

- **ID do mecanismo:** B11 — Disfunção Tireoidiana (eixo hipotálamo–hipófise–tireoide/HPT;
  hormônios T4/T3; desiodinases; transportadores MCT8/OATP1C1; receptores TRα/β; sinalização
  tireoidiana central no cérebro adulto).
- **Condições em escopo:** Transtorno Depressivo Maior (TDM), Depressão Resistente ao Tratamento
  (TRD — aqui apenas quanto ao **sinal** de plasticidade do eixo, não como conduta), Distimia,
  Transtorno de Ansiedade Generalizada, Transtorno do Pânico, Transtorno de Ansiedade Social,
  TEPT (quando tratado no espectro trauma/ansiedade — sinal fraco, ver Módulo 06). O **transtorno
  bipolar** entra como condição-irmã com literatura tireoidiana **própria e extensa** (ciclagem
  rápida, lítio, T3) — sempre sinalizado como bipolar, **nunca fundido** à TDM. Os **estados
  tireoidianos** (hipotireoidismo clínico/subclínico, hipertireoidismo/Graves, tireoidite
  autoimune/Hashimoto, síndrome do T3 baixo/NTIS, tireoidite pós-parto) são os fenótipos
  endócrinos de exposição.
- **Corte de conhecimento:** busca em tempo real **executada em 2026-09-06** via
  PubMed/E-utilities (esearch/esummary/efetch, com backoff), resolução de DOIs do relatório
  Consensus via PubMed, e três insumos externos auditados (insumo mecanístico A; briefing
  consolidado B; relatório Consensus C), incluindo a resolução, via eutils, de duas referências
  que o insumo B deixara "a confirmar" (Prange 1969; Bauer/Heinz/Whybrow 2002). O GPM reflete
  literatura até essa data.
- **Observação de escopo:** a regra de delimitação por doença foi aplicada item a item. A
  **biologia fundamental do eixo HPT e da ação do T3** (Brent, 2012; Groeneweg et al., 2020) entra
  como base universal, sem exigir contexto de doença. Achados em **outra condição** (cretinismo/
  deficiência grave de iodo, síndrome MCT8/Allan-Herndon-Dudley, resistência ao hormônio
  tireoidiano, câncer de tireoide, apneia do sono, doença crítica/NTIS de UTI, TDAH/
  neurodesenvolvimento) entram no corpo só quando há estudo-ponte para humor/ansiedade,
  sinalizados `[EXTRAPOLAÇÃO POR ANALOGIA: ...]`; os sem ponte vão para o Módulo 10. Dados de
  **sangue/periferia** (TSH, T4 livre, anti-TPO) entram com rótulo explícito de **marcador
  periférico (≠ sinalização neuronal)**.

**Propósito deste GPM (nota de direção de atenção):** o tema "tireoide e humor" seduz o
levantamento genérico a parar no óbvio — "hipotireoidismo deprime, reposição resolve" — e a
colapsar o mecanismo no **TSH** e na **doença periférica**. Os pontos cegos que este documento
deve trazer à tona são: (i) o **transporte através da barreira** (MCT8/SLC16A2, MCT10/SLC16A10,
OATP1C1/SLCO1C1) e a **conversão local** por desiodinases (D2 = T4→T3 neuronal; D3 = inativação)
como etapa distinta do hormônio circulante; (ii) os **receptores nucleares TRα (THRA; TRα1
majoritário no cérebro adulto) vs TRβ (THRB; mais glia/desenvolvimento)** e sua ação
transcricional sobre genes neurais; (iii) a **sinalização tireoidiana central no cérebro adulto**
como regulador direto de neurogênese, interneurônios GABAérgicos, memória de medo na amígdala e
córtex/exploração (Hochbaum, 2024; Maddox, 2025; Mayerl, 2022) — não só hormônio de
desenvolvimento/metabolismo; (iv) a **relação em U** (hipo E hiper associam-se a depressão) e a
**ansiedade como evidência mais fraca/inconclusiva** que a depressão; (v) a **evidência negativa**
do subclínico (IPD prospectivo e RCT TRUST) e a genética UK Biobank que atribui a
co-hereditariedade à **autoimunidade geral**, não aos hormônios (Soheili-Nezhad, 2023); (vi) o
**DIO2 Thr92Ala (rs225014)** como história de medicina personalizada com mecanismo celular
(estresse do retículo/UPR; Jo, 2019) mas **replicação mista**; e (vii) o **inventário negativo**
— anti-TPO isolado, DIO1/DIO3 e o próprio SCH não dão assinação consistente. O GPM cobre
**mecanismo**; **não cobre terapia** (reposição/augmentation/lítio são sinal, não conduta).

[REF_MODULO_00: Briefing_B11_2026 | Molde_GPM_v2.0 | Brent_2012 | Groeneweg_2020 |
Hochbaum_2024 | Bode_2021 | Soheili-Nezhad_2023]

---

## MÓDULO 01 — MAPA EXAUSTIVO DE VIAS MOLECULARES

### Via 1 — Eixo HPT clássico: síntese, secreção e retroalimentação
- **Sequência:** o hipotálamo (núcleo paraventricular) libera **TRH (hormônio liberador de
  tireotrofina/TSH)** → a hipófise anterior secreta **TSH (tireotrofina)** → a tireoide produz
  **tiroxina (T4, pró-hormônio, em maior quantidade)** e **tri-iodotironina (T3, forma ativa, em
  menor quantidade)**; a síntese depende de **iodo** (substrato) e de **selênio** (cofator das
  desiodinases). O T3/T4 circula ligado a **TBG, TTR e albumina**. O **feedback negativo** de
  T3/T4 sobre o hipotálamo/hipófise inibe TRH/TSH (Brent, 2012; revisões Endotext; Zimmermann,
  2009 para o iodo).
- **Papel em ansiedade/depressão:** é o eixo cuja disfunção periférica é triada na prática
  clínica. O hipotireoidismo clínico produz síndrome pseudodepressiva (lentificação, anedonia,
  fadiga) e o hipertireoidismo síndrome pseudoansiosa/agitação — descritos classicamente e
  reversíveis com o tratamento do estado endócrino (revisões: Dayan & Panicker, 2013; Jackson,
  1998; Lee et al., 2023 para o hipertireoidismo; Demet et al., 2002) [evidência humana;
  **associativa/contributiva**; muito estabelecido como fenômeno clínico]. A força da associação
  com transtorno psiquiátrico **primário** é, porém, modesta (ver Via 8 e Módulo 08).
- **Convergência/divergência:** é o eixo de **entrada**; as vias 2–4 descrevem o que o hormônio
  faz **depois** de cruzar a barreira — é aí que está o mecanismo neural, e é o que o TSH
  periférico não mede diretamente.

### Via 2 — Transporte através da barreira hematoencefálica e de membranas celulares
- **Sequência:** os hormônios tireoidianos são aminoácidos iodados **carregados** e não cruzam
  membranas por difusão livre; dependem de transportadores — **MCT8 (SLC16A2)** e **MCT10
  (SLC16A10)** (monocarboxilato, transportam T3/T4) e **OATP1C1 (SLCO1C1)** (preferencial para
  T4, no endotélio da barreira). A distribuição tecidual e a entrada neuronal são assim
  **etapas reguladas** (Groeneweg et al., 2020, revisão-teto; Friesema et al., 2005; Felmlee et
  al., 2020).
- **Papel em ansiedade/depressão:** a perda de função do MCT8 (síndrome de Allan-Herndon-Dudley)
  causa retardo neurológico grave, provando que o **transporte é obrigatório** para a ação
  cerebral do hormônio — mas isso é doença do neurodesenvolvimento
  `[EXTRAPOLAÇÃO POR ANALOGIA: síndrome MCT8/desenvolvimento — a tradução para humor adulto é
  indireta]` (Chakraborty et al., 2025; Groeneweg et al., 2025 em heterozigotas). No cérebro
  adulto, o defeito de transporte altera a **astróg lia** (Guillén-Yunta et al., 2024) e a
  deleção combinada de *Mct8*+*Dio2* compromete a neurogliogênese da zona subventricular/olfato
  (Valcárcel-Hernández et al., 2024) [evidência em modelo animal/molecular; **causal sobre o
  transporte e a neurogênese**; bem suportado para o desenvolvimento, emergente para humor
  adulto]. A dopamina cerebral também se altera na deficiência de MCT8, com resposta a levodopa
  (Bruschi et al., 2026) [evidência mista animal/humano; mecanística; emergente — ponte B4].
- **Divergência:** esta via **revoga** o modelo "TSH/T4 sanguíneo = estado tireoidiano do
  cérebro": o transporte pode dissociar o hormônio circulante do sinal neuronal (o subtipo
  "molecular" F8 do Módulo 07).

### Via 3 — Conversão local por desiodinases: ativação e inativação teciduais
- **Sequência:** **D2 (DIO2)** converte T4→T3 no próprio tecido (é a principal fonte de T3
  cerebral local, expressa em astrócitos/tânicitas); **D1 (DIO1)** atua sobretudo em fígado/
  rim e na circulação; **D3 (DIO3)** inativa T3/T4 (gera T3 reverso/rT3), limitando a sinalização.
  O balanço D2/D3 define o **T3 intracelular ativo**, independentemente do T4 sérico (revisão:
  Bianco et al., 2018).
- **Papel em ansiedade/depressão:** a conversão local é o nó que torna o cérebro
  **autônomo** em relação ao sangue. O polimorfismo **DIO2 Thr92Ala (rs225014)** produz uma
  enzima que se acumula no aparelho de Golgi, ativa a **resposta a proteína mal-dobrada (UPR)/
  estresse do retículo endoplasmático** e gera menos T3 local — mecanismo celular de
  "hipotireoidismo cerebral" com T4 periférico normal (Jo et al., 2019) [evidência in vitro +
  animal; **causal/mecanístico sobre a enzima**; bem suportado molecularmente]. A associação
  desse polimorfismo a humor é, porém, de **replicação mista** (Módulo 04). Citocinas
  pró-inflamatórias (IL-6, TNF-α) desviam a atividade de desiodinase periférica e produzem
  padrão **T3-baixo/NTIS** sem falha glandular (Toma et al., 2026) [evidência humana/revisão;
  **contributiva/marcador**; emergente — ponte B1].
- **Fase temporal:** atua na **manutenção/modulação fina** contínua do T3 tecidual; D3 é
  induzida em doença/hipóxia (regulação defensiva).

### Via 4 — Ação nuclear via receptores TRα/TRβ: transcrição de genes neurais
- **Sequência:** o T3 liga-se a receptores nucleares **TRα (THRA; isoformas TRα1/TRα2)** e
  **TRβ (THRB; TRβ1/TRβ2)** — fatores de transcrição da superfamília dos receptores
  esteroides/ tireoidianos — que, com co-reguladores, ligam-se a elementos responsivos (TRE) e
  regulam a expressão gênica. Há também ações **não-genômicas** rápidas. No cérebro adulto o
  **TRα1 é majoritário** (neurônios), enquanto TRβ pesa mais na glia e no desenvolvimento
  (Iskaros et al., 2000, cérebro fetal; Ishii et al., 2021, cerebelo).
- **Papel em ansiedade/depressão:** o TRα1 hipotalâmico controla inclusive a **temperatura
  corporal** (Sentis et al., 2024); a transdução do sinal tireoidiano varia entre estruturas
  cerebrais (Sinkó et al., 2025); e o T3 age de forma **sinérgica com o glicocorticoide** na
  regulação gênica do hipocampo (Espina et al., 2022) — base molecular da interseção com o eixo
  de estresse (Via 7) [evidência em modelo animal/molecular; **mecanística/causal sobre a
  transcrição**; bem suportada]. A resistência ao hormônio tireoidiano β (RTHβ) é condição
  monogênica que ilustra a via, mas fica fora do escopo de humor (Módulo 10; Pappa et al., 2021).
- **Convergência:** é o **elo final comum** das vias 2–3; é também onde o sinal tireoidiano
  encontra a maquinaria de plasticidade (Via 5) e de monoaminas (Via 6).

### Via 5 — Sinalização tireoidiana central → circuitos de humor e ansiedade (cérebro adulto)
- **Sequência:** T3 → TRα/β → expressão de genes que controlam **neurogênese hipocampal
  adulta**, **plasticidade sináptica/BDNF**, **interneurônios GABAérgicos**, **memória de medo
  dependente da amígdala** e a **coordenação córtex–metabolismo–comportamento**.
- **Papel em ansiedade/depressão:** é o coração mecanístico da B11. (a) O hormônio tireoidiano
  **remodela o córtex** para coordenar metabolismo corporal e exploração/comportamento
  (Hochbaum et al., 2024, *Cell*) [animal; **causal/marco**; emergente-maduro]. (b) O T3
  regulariza a **memória de medo** dependente da amígdala e a plasticidade associada (Maddox et
  al., 2025, *Mol Psychiatry*) [animal; causal; emergente — eixo ansiedade/medo]. (c) A
  deficiência de transporte impacta **interneurônios GABAérgicos** (Mayerl et al., 2022) [animal;
  causal; emergente-maduro — ponte B5]. (d) O hormônio promove neurogênese fetal e adulta
  (Salas-Lucia et al., 2025; Kapri et al., 2022) e a deleção Mct8+Dio2 compromete
  neurogliogênese (Valcárcel-Hernández et al., 2024) [animal/molecular; causal; emergente —
  ponte B16/B3]. (e) No humano, o hipotireoidismo adulto reduz **volume hipocampal** (Cooke et
  al., 2014) e altera o **metabolismo cerebral de glicose** ao PET, revertendo com a reposição
  (Bauer, Silverman et al., 2009) [humano/neuroimagem; **associativo/marcador**; moderadamente
  suportado]. (f) O hipertireoidismo experimental prejudica aprendizado/memória via receptor
  NMDA (GRIN2B) (Sahin et al., 2023) [animal; causal; emergente].
- **Natureza:** evidência **causal forte em animal/molecular** para a regulação de circuitos;
  **associativa em humano**. Este é o nó que a B11 propõe como integrador com **B3
  (neuroplasticidade/BDNF)** — detalhado no Módulo 06.

### Via 6 — Interação com monoaminas (serotonina, dopamina, noradrenalina)
- **Sequência:** o estado tireoidiano regula a expressão/função de receptores e a síntese de
  monoaminas. Mecanismo melhor descrito: o T3 **reduz a transcrição de autorreceptores
  serotoninérgicos 5-HT1A/5-HT1B**, o que amplificaria a neurotransmissão 5-HT; modula ainda
  receptores **β-adrenérgicos**, **5-HT2A** e o sistema **dopaminérgico** (revisão mecanística:
  Bauer, Heinz & Whybrow, 2002; Bauer & Whybrow, 2001).
- **Papel em ansiedade/depressão:** em modelo animal, o hipotireoidismo altera receptores
  β-adrenérgicos e serotoninérgicos (Mason et al., 1987), o T3 controla a serotonina no cérebro
  em desenvolvimento (Schwark, 1975, clássico) e o receptor 5-HT2A medeia comportamento
  tipo-depressão no hipotireoidismo de rato (Jin et al., 2021) [animal; **causal/contributivo**;
  moderadamente a bem suportado]. Em humanos, a função dopaminérgica e a atividade do eixo HPT
  co-variam na TDM (Duval et al., 2021; Duval et al., 2022) [humano; **associativo**;
  moderadamente suportado]. Esta é a **ponte molecular concreta B11→B4** e o mecanismo proposto
  para a *augmentation* com T3 (que, por regra do molde, fica apenas como **sinal experimental**
  no Briefing, não como conduta).
- **Convergência:** dialoga diretamente com a Via 5 (a modulação monoaminérgica é uma das saídas
  da sinalização TR sobre circuitos).

### Via 7 — Interação com o eixo de estresse (HPA) e com o sistema circadiano
- **Sequência (HPA):** TRH e CRH têm origem hipotalâmica comum e cruzam-se funcionalmente; o
  hormônio tireoidiano modula a sensibilidade do receptor de glicocorticoide, e o T3 e o
  glicocorticoide regulam genes hipocampais de forma sinérgica (Espina et al., 2022). O estresse
  agudo/crônico altera o eixo HPT (revisões: Chrousos, 2009; Petrowski et al., 2025; Bunevicius &
  Bunevicius, 2010). **(Circadiano):** o TSH tem secreção pulsátil e ritmo circadiano (pico
  noturno) controlado pelo relógio; o gene-relógio BMAL1 controla a senescência tireoidiana e o
  eixo responde ao fotoperíodo (Ikegami et al., 2019; Zong et al., 2025; Sawant et al., 2017).
- **Papel em ansiedade/depressão:** as alterações tireoidiana e adrenal na depressão estão
  ligadas (Mokrani et al., 2020) e a disfunção tireoidiana associa-se a distúrbios do sono
  (Green et al., 2021; Baumgartner et al., 1990 para TSH na privação de sono) [evidência humana +
  revisão/animal; **bidirecional/contributiva**; moderadamente a bem suportada — pontes B2 e
  B10, detalhadas no Módulo 06].
- **Fase temporal:** o componente de estresse atua na **iniciação/amplificação** (o estresse
  perturba o HPT); o componente rítmico é contínuo.

### Via 8 — Via autoimune/neuroinflamatória e a leitura populacional (doença periférica)
- **Sequência:** na tireoidite autoimune (Hashimoto/Graves), anticorpos (anti-TPO, anti-Tg,
  TRAb) e infiltrado inflamatório/estresse oxidativo acompanham a disfunção glandular (Ates et
  al., 2018); citocinas podem alterar desiodinase (Via 3). Em paralelo, a **epidemiologia**
  estima a associação entre estados tireoidianos e transtornos de humor/ansiedade.
- **Papel em ansiedade/depressão:** metas de hipotireoidismo→depressão mostram associação
  **modesta**, maior no quadro clínico que no subclínico (Bode et al., 2021) e presente também
  no **hipertireoidismo** (Bode et al., 2022) — configurando a relação em U. A tireoidite
  autoimune mostra OR mais alto mas com **heterogeneidade muito grande** (Siegmann et al., 2018),
  enquanto a meta mais robusta **não** acha associação significativa do **anti-TPO isolado** com
  depressão (Bode et al., 2021) e a genética de larga escala atribui a co-hereditariedade à
  **autoimunidade geral**, não aos hormônios (Soheili-Nezhad et al., 2023) [evidência humana/meta
  + genética; **associativa**; bem suportada quanto à modéstia do efeito; controvertida quanto à
  autoimunidade — ver Módulos 02 e 08].
- **Natureza:** esta via descreve majoritariamente **associação populacional**, não mecanismo
  causal neural; a ponte inflamação→sinalização central é emergente.

> **Autoauditoria do Módulo 01:** as vias 1 e 4 (eixo HPT; receptores TR) são muito
> estabelecidas; as vias 2–3 (transporte/conversão) e 5 (sinalização central em circuitos
> adultos) são as camadas **emergentes** que um levantamento genérico perderia — estão
> sinalizadas. A causalidade **animal/molecular** (Via 5) foi explicitamente separada da
> **associação humana** (Via 8). Nenhuma intervenção (reposição, T3, lítio) é apresentada como
> conduta — a *augmentation* aparece apenas como o fenômeno que a Via 6 explicaria
> mecanisticamente. Achados de desenvolvimento (MCT8/Allan-Herndon-Dudley, RTHβ, cerebelo fetal)
> foram sinalizados com `[EXTRAPOLAÇÃO POR ANALOGIA]` ou remetidos ao Módulo 10. Os números de
> efeito das metas (OR/IC/I²) não são afirmados aqui (vivem no Briefing e aguardam G3).

[REF_MODULO_01: Brent_2012 | Groeneweg_2020 | Friesema_2005 | Felmlee_2020 | Guillen-Yunta_2024 |
Valcarcel-Hernandez_2024 | Jo_2019 | Bianco_2018 | Sentis_2024 | Sinko_2025 | Espina_2022 |
Hochbaum_2024 | Maddox_2025 | Mayerl_2022 | Cooke_2014 | Salas-Lucia_2025 | Kapri_2022 |
Sahin_2023 | Bauer_Silverman_2009 | Bauer_Heinz_Whybrow_2002 | Jin_2021 | Mason_1987 |
Duval_2021 | Mokrani_2020 | Ikegami_2019 | Bode_2021 | Bode_2022 | Siegmann_2018 |
Soheili-Nezhad_2023]

---

## MÓDULO 02 — MAPA EXAUSTIVO DE MEDIADORES MOLECULARES

*Categorias adaptadas à natureza endócrina/sinalizadora do mecanismo (não são as categorias
imunológicas do molde).*

### 2.1 Hormônios e peptídeos do eixo
- **T4 (tiroxina)** — pró-hormônio majoritário, secretado pela tireoide; depende de conversão
  para exercer ação; T4 livre baixo-normal prediz depressão major futura em alguns estudos
  (Odawara et al., 2023) [humano/coorte; **preditivo/associativo**; moderadamente suportado].
- **T3 (tri-iodotironina)** — forma ativa; liga TRα/β e regula genes neurais (Via 4–5). T3 total/
  livre e sua relação com desfecho na depressão foram medidos classicamente (Iosifescu et al.,
  2001) [humano; marcador; moderadamente suportado]. O T3 exógeno como *augmentation* é **sinal
  terapêutico**, não conteúdo deste GPM.
- **rT3 (T3 reverso)** — produto de inativação (D3); marcador de NTIS/conversão periférica, não
  disponível na rotina [básico/humano; marcador; moderadamente suportado].
- **TRH (protirelina)** — peptídeo hipotalâmico que estimula TSH; também presente no líquor e
  com ações extra-endócrinas (sinalização imune: Kamath et al., 2009; plasticidade cerebelar
  LTD: Watanave et al., 2018) [revisão/animal; mecanístico; emergente].
- **TSH (tireotrofina)** — hormônio hipofisário de rastreio; **marcador dentro do sistema, não o
  mecanismo**; tem ritmo circadiano e sobe com a idade/sexo feminino/lítio. Associa-se
  transversal/longitudinalmente a depressão em coortes (Varella et al., 2021, ELSA-Brasil; Kumar
  et al., 2023; Roa et al., 2024), mas nem todos replicam (Samuels et al., 2018, revisão
  crítica) [humano/coorte; **marcador/associativo**; moderadamente suportado, heterogêneo].
- **Proteínas transportadoras séricas (TBG, TTR, albumina)** — carregam o hormônio; alteram o
  total sem mudar o livre [básico; mecanístico; muito estabelecido].

### 2.2 Enzimas de conversão (desiodinases)
- **D2 / DIO2** — T4→T3 local (astrócitos/tânicitas); principal fonte de T3 cerebral; a variante
  Thr92Ala altera retenção/UPR (Jo et al., 2019; Bianco et al., 2018) [in vitro+animal;
  causal/mecanístico; bem suportado molecularmente].
- **D1 / DIO1** — ativação periférica (fígado/rim); variantes associadas a função frontal/
  história de TDM em estudos pequenos (Gałecka et al., 2016; Philibert et al., 2011) [humano/
  genética; associativo; fraco/emergente].
- **D3 / DIO3** — inativação (T3→rT3); induzida em doença; polimorfismos **não** associados a
  recorrência depressiva (Gałecka et al., 2016, achado nulo) [humano; **inventário negativo**;
  moderadamente suportado].

### 2.3 Transportadores de membrana
- **MCT8 / SLC16A2** — transporte de T3/T3 através da barreira e em neurônios; perda =
  Allan-Herndon-Dudley (desenvolvimento); defeito altera astróglia e dopamina (Groeneweg et al.,
  2020; Guillén-Yunta et al., 2024; Bruschi et al., 2026) [revisão/animal/humano; mecanístico;
  bem suportado para desenvolvimento].
- **OATP1C1 / SLCO1C1** — transporte preferencial de T4 no endotélio da barreira [básico;
  mecanístico; bem suportado].
- **MCT10 / SLC16A10** — transportador de T3/aminoácidos aromáticos (Felmlee et al., 2020)
  [básico; mecanístico; moderadamente suportado].

### 2.4 Receptores nucleares e maquinaria transcricional
- **TRα / THRA (TRα1)** — receptor majoritário no cérebro adulto (neurônios); controla
  temperatura hipotalâmica e transcrição neural (Sentis et al., 2024) [animal; mecanístico; bem
  suportado].
- **TRβ / THRB (TRβ1/TRβ2)** — mais glia/desenvolvimento e eixo feedback hipofisário; mutações =
  RTHβ (fora de escopo de humor; Módulo 10) [básico; mecanístico; muito estabelecido].
- **Co-reguladores / elemento TRE / ação não-genômica** — modulam a direção (ativação/repres são)
  da resposta ao T3 (Brent, 2012) [básico; mecanístico; muito estabelecido].
- **TSHR (receptor de TSH)** — alvo dos anticorpos de Graves (TRAb); variantes pouco estudadas
  em psiquiatria (permanece `[G1]` para humor) [lacuna].

### 2.5 Autoanticorpos e mediadores imunes
- **Anti-TPO (TPOAb)** — marcador de autoimunidade tireoidiana; prevalência de base alta
  (~15–20% em mulheres). Associação com humor **heterogênea e contestada**: meta robusta sem
  sinal do anticorpo isolado (Bode et al., 2021), revisão que aponta superestimação (Tian et al.,
  2025) vs. metas/estudos comunitários positivos (Siegmann et al., 2018; Carta et al., 2004;
  Yang W. et al., 2023) [humano; **associativo/controverso**; moderadamente suportado].
- **Anti-tireoglobulina (TgAb)** — co-ocorre com anti-TPO; correlaciona-se com escores de
  ansiedade em alguns estudos transversais e com alterações corticais em neuroimagem (Karagun —
  fonte sem PMID, descartada; Yang W. et al., 2023; frontier 2026) [humano; associativo;
  emergente].
- **TRAb (anti-TSHR)** — anticorpo estimulador na Graves; associação direta própria com humor
  pouco estudada além da tireotoxicose [humano; marcador; emergente].
- **Citocinas (IL-6, TNF-α)** e **estresse oxidativo** na tireoidite — desviam desiodinase
  (Toma et al., 2026; Ates et al., 2018) [revisão/humano; contributivo; emergente — B1/B6].

### 2.6 Mediadores neurais e tróficos (saída da sinalização TR)
- **BDNF (fator neurotrófico derivado do cérebro)** — o hormônio tireoidiano modula BDNF/
  plasticidade hipocampal e amigdalar (Hochbaum, 2024; Maddox, 2025; Cooke, 2014) [animal +
  humano/neuroimagem; mediacional/associativo; emergente — nó com B3].
- **Receptores monoaminérgicos (5-HT1A/1B, 5-HT2A, β-adrenérgicos) e dopamina** — modulados
  pelo estado tireoidiano (Bauer, Heinz & Whybrow, 2002; Jin, 2021; Mason, 1987; Duval, 2021;
  Bruschi, 2026) [animal+humano; contributivo; moderadamente suportado — B4].
- **Sinalização GABAérgica (interneurônios)** — impactada pela deficiência de transporte
  (Mayerl, 2022) [animal; causal; emergente — B5].

### 2.7 INVENTÁRIO NEGATIVO (subseção obrigatória)
Mediadores/parâmetros **repetidamente investigados sem associação consistente** ou sem validação
em ansiedade/depressão:
- **Anti-TPO isolado:** a meta-análise mais robusta e maior **não** encontra associação
  estatisticamente significativa entre positividade de anti-TPO **sozinha** e depressão clínica
  (Bode et al., 2021); revisão crítica sustenta que a relação anticorpo→humor é superestimada
  (Tian et al., 2025) [meta/revisão humana; **inventário negativo**; bem suportado].
- **Hipotireoidismo subclínico como preditor:** a análise de dados de participantes individuais
  de coortes prospectivas **não** achou associação clinicamente relevante entre disfunção
  subclínica basal e sintomas depressivos futuros (estudo IPD, 2020) [coorte prospectiva/humano;
  **negativo**; bem suportado].
- **TSH como "teste de depressão":** não existe valor de TSH que defina transtorno de humor;
  coortes divergem (Samuels et al., 2018) e a normalização do TSH não resolve o sintoma (sinal
  do ensaio TRUST — ver Módulo 08) [revisão/ensaio; **negação de marcador único**; bem
  suportado].
- **Polimorfismos de DIO1/DIO3:** não associados a recorrência depressiva (Gałecka et al.,
  2016) [humano/genética; **achado nulo**; moderadamente suportado].
- **Ansiedade:** na meta populacional de 2026, hipotireoidismo e TPOAb **não** foram
  significativos para ansiedade (só hipertireoidismo com OR pequeno; I² alto) — evidência
  **inconclusiva**, mais fraca que para depressão [meta/humano; **inconclusivo/negativo para
  hipo e TPOAb**; moderadamente suportado].
- Alegações quantitativas fortes de fontes não indexadas/de baixo peso (ex.: OR elevados em
  revisões narrativas de periódicos predatórios descartados no insumo C) **não** entram como
  fato — seguem `[G1]`/descarte.

> **Autoauditoria do Módulo 02:** os mediadores foram distribuídos entre hormônios (2.1),
> enzimas (2.2), transportadores (2.3), receptores (2.4), imune (2.5) e saída neural (2.6),
> evitando parar em TSH/T4 (o óbvio). O **inventário negativo** está explícito e é uma marca
> deste mecanismo (anti-TPO isolado, SCH, DIO1/DIO3, ansiedade). O TSHRB em humor e o anti-Tg
> específico permanecem `[G1]`/emergentes. Nenhuma entidade molecular foi inventada; o que é de
> desenvolvimento (MCT8/RTHβ) foi sinalizado.

[REF_MODULO_02: Brent_2012 | Jo_2019 | Bianco_2018 | Galecka_2016 | Philibert_2011 |
Groeneweg_2020 | Guillen-Yunta_2024 | Felmlee_2020 | Sentis_2024 | Bode_2021 | Tian_2025 |
Siegmann_2018 | Carta_2004 | Yang_W_2023 | Toma_2026 | Ates_2018 | Hochbaum_2024 |
Maddox_2025 | Mayerl_2022 | Bauer_Heinz_Whybrow_2002 | Duval_2021 | Odawara_2023 |
Samuels_2018 | Varella_2021]

---

## MÓDULO 03 — MAPA EXAUSTIVO DE TIPOS CELULARES E ESTRUTURAS

### 3.1 Tipos celulares
- **Tireócitos (glândula tireoide)** — sintetizam T4≫T3 a partir de iodo, com selênio nas
  desiodinases/peroxidases; alvo do TSH e do ataque autoimune (Hashimoto/Graves) [básico;
  mecanístico; muito estabelecido].
- **Neurônios paraventriculares hipotalâmicos (TRH)** — integram sinal de feedback e
  estresse/ritmo; expressam TRα1 que controla temperatura (Sentis et al., 2024) [animal;
  mecanístico; emergente-maduro].
- **Tireotrofos hipofisários** — secretam TSH sob TRH e inibição por T3/T4 [básico;
  mecanístico; muito estabelecido].
- **Astrócitos e tânicitas (D2)** — principal sítio de conversão T4→T3 cerebral; o defeito de
  transporte tireoidiano altera a astróglia (Guillén-Yunta et al., 2024; Mayerl et al., 2022)
  [animal/molecular; causal; emergente-maduro].
- **Neurônios que expressam TRα1 (majoritários) vs. células TRβ (glia/desenvolvimento)** —
  neurônios adultos são predominantemente TRα; a identidade espectral/regional da sinalização
  varia (Sinkó et al., 2025; Ishii et al., 2021) [animal/molecular; mecanístico; bem suportado].
- **Interneurônios GABAérgicos** — impactados pela deficiência de transporte de hormônio, com
  repercussão sobre inibição cortical/hipocampal (Mayerl et al., 2022) [animal; causal;
  emergente — B5].
- **Células progenitoras / zona subventricular e giro denteado (neurogênese adulta)** — o
  hormônio promove neurogênese fetal e adulta; a deleção Mct8+Dio2 compromete
  neurogliogênese SVZ/olfato (Salas-Lucia et al., 2025; Kapri et al., 2022;
  Valcárcel-Hernández et al., 2024) [animal/molecular; causal; emergente — B16].
- **Células imunes (linfócitos autoimunes; citocinas)** — infiltram a tireoide na Hashimoto e
  sustentam o estado inflamatório sistêmico que pode desviar desiodinase (Siegmann et al., 2018;
  Toma et al., 2026; Li et al., 2024) [humano/revisão; associativo/contributivo; emergente].

### 3.2 Estruturas anatômicas e circuitos
- **Glândula tireoide / hipotálamo (PVN) / hipófise** — o eixo periférico de síntese e
  retroalimentação (Brent, 2012) [básico; mecanístico; muito estabelecido].
- **Barreira hematoencefálica / endotélio capilar** — sítio de MCT8/OATP1C1; o "portão" do
  hormônio ao cérebro (Groeneweg et al., 2020; Felmlee et al., 2020) [básico/revisão;
  mecanístico; bem suportado].
- **Hipocampo** — neurogênese adulta e volume reduzidos no hipotireoidismo humano (Cooke et al.,
  2014); sítio de sinergia T3–glicocorticoide (Espina et al., 2022) [humano+animal;
  associativo/causal; moderadamente a bem suportado].
- **Amígdala** — o T3 regula a memória de medo dependente da amígdala (Maddox et al., 2025);
  estruturalmente no sistema límbico que expressa TR (Yang R. et al., 2022) [animal+humano;
  causal/associativo; emergente — eixo ansiedade].
- **Córtex (remodelagem/exploração)** — o hormônio remodela o córtex coordenando metabolismo e
  exploração (Hochbaum et al., 2024); metabolismo cortical medido por PET (Bauer, Silverman et
  al., 2009) [animal+humano; causal/marcador; emergente].
- **Cerebelo** — modelo clássico de ação do hormônio no desenvolvimento; TRH contribui para LTD
  cerebelar (Ishii et al., 2021; Watanave et al., 2018) [animal/revisão; mecanístico;
  desenvolvimento — ponte indireta para humor adulto].
- **Sistema monoaminérgico (rafe, substância negra/VTA, locus coeruleus)** — síntese/receptores
  modulados pelo estado tireoidiano (Jin et al., 2021; Duval et al., 2021; Bruschi et al., 2026)
  [animal+humano; contributivo; moderadamente suportado].
- **Métodos de avaliação na literatura:** dosagem hormonal sérica (TSH/T4 livre/T3/anticorpos),
  teste dinâmico ao TRH, PET de metabolismo, volumetria por RM — ver Módulo 05.

> **Autoauditoria do Módulo 03:** cobriu-se o eixo endócrino periférico (ó bvio) **e** as
> estruturas centrais menos lembradas — astrócitos/tânicitas D2, interneurônios GABAérgicos,
> células progenitoras adultas e os circuitos córtex/amígdala/hipocampo da literatura de 2022–
> 2026. O componente de **neurogênese adulta** (não só desenvolvimento) foi destacado. O
> cerebelo/desenvolvimento ficou sinalizado como ponte indireta. Nenhuma estrutura foi inventada.

[REF_MODULO_03: Brent_2012 | Sentis_2024 | Guillen-Yunta_2024 | Mayerl_2022 | Sinko_2025 |
Salas-Lucia_2025 | Kapri_2022 | Valcarcel-Hernandez_2024 | Groeneweg_2020 | Cooke_2014 |
Espina_2022 | Maddox_2025 | Hochbaum_2024 | Bauer_Silverman_2009 | Ishii_2021 | Watanave_2018 |
Jin_2021 | Duval_2021 | Siegmann_2018]

---

## MÓDULO 04 — VARIABILIDADE GENÉTICA E EPIGENÉTICA EXAUSTIVA

**Teste de escopo aplicado a cada item:** variantes de genes do eixo tireoidiano só entram
quando há estudo em ansiedade/depressão/bipolar (humano) ou manipulação em modelo de humor
(animal). O que é só de outra doença/desenvolvimento (MCT8/Allan-Herndon-Dudley, RTHβ, cretinismo)
sem ponte para humor adulto vai para o Módulo 10.

### 4.1 Polimorfismos de desiodinases em transtornos de humor (humano)
- **DIO2 Thr92Ala (rs225014):** a variante central da B11. Mecanismo celular — a enzima Ala92
  retém-se no Golgi, ativa UPR/estresse do RE e gera menos T3 local (Jo et al., 2019) [in
  vitro+animal; causal/mecanístico; bem suportado]. Associação a humor: ligada a depressão em
  estudo brasileiro (Beltrão et al., 2024) e a transtorno depressivo recorrente (Gałecka et al.,
  2015), e a bipolar (He et al., 2009) [humano/genética; **associativo; moderadamente/fracamente
  suportado**]. **Replicação mista:** a preferência por terapia combinada T4+T3 associada ao
  genótipo replicou em parte da literatura (Reino Unido) e **não** replicou em outra coorte
  (Amsterdã) — tratar como **disputa**, não consenso (a coorte negativa não tem PMID cravejado
  neste levantamento; referência específica a confirmar no G2).
- **DIO1:** SNPs associados a função frontal/história de TDM (Gałecka et al., 2016, *Adv Med
  Sci*) e a história de TDM (Philibert et al., 2011) [humano/genética; associativo; fraco/
  emergente]. Variante de D1 e resposta à *augmentation* com T3 (Cooper-Kazaz et al., 2009) é
  farmacogenética de **intervenção** — fica como sinal no Briefing, não como conduta.
- **DIO3:** polimorfismos **não** associados a recorrência depressiva (Gałecka et al., 2016,
  *Pharmacol Rep*) [humano/genética; **achado nulo**; moderadamente suportado].
- **Polimorfismos de desiodinase/OATP e sintomas de ansiedade pós-AVC** (Taroza et al., 2020)
  `[EXTRAPOLAÇÃO POR ANALOGIA: AVC/ansiedade — não é TDM/ansiedade primária; ponte indireta]`
  [humano; associativo; hipótese inicial].

### 4.2 Genética de larga escala: co-hereditariedade mediada por autoimunidade
- **UK Biobank (~498 mil indivíduos):** existe **co-hereditariedade** entre hipotireoidismo e
  transtornos de humor/ansiedade (rg ~0,17), mas ela **não é mediada pelos hormônios
  tireoidianos** — e sim por **autoimunidade geral**; os autores associam isso à falha da
  reposição de disfunção leve e defendem atitude restrita (Soheili-Nezhad et al., 2023)
  [humano/genética epidemiológica; **associativo/mecanismo-implícito**; bem suportado]. Os OR
  observacionais reportados (hipo→TDM ~1,31; bipolar ~1,55; ansiedade ~1,16; hiper→TDM ~1,11;
  ansiedade ~1,34) são **alegação a confirmar no G3**.
- **THRA/THRB (receptores) e TSHR em humor:** plausibilidade mecanística clara, mas lastro
  específico em ansiedade/depressão **insuficiente** — permanecem `[G1]` (a RTHβ monogênica é
  condição de Módulo 10; Pappa et al., 2021) [lacuna].

### 4.3 Prova mecanística animal (manipulação do transporte/conversão → comportamento/neurogênese)
- Perda/deleção de **Mct8** (+/*Dio2*) altera astróglia e neurogliogênese e o sistema
  dopaminérgico (Guillén-Yunta et al., 2024; Valcárcel-Hernández et al., 2024; Bruschi et al.,
  2026); o **D2 mutante (Thr92Ala-equivalente)** reproduz o estresse do RE e o T3 local reduzido
  (Jo et al., 2019) [animal/in vitro; **causal sobre o mecanismo enzimático/transportador**;
  emergente-maduro]. São provas de que o eixo é **molecularmente plástico**, não de que um SNP
  cause depressão em humano.
- **Viés de tradução a registrar:** quase toda a causalidade geneticamente definida vem de
  mutações de **desenvolvimento** (MCT8) ou de engenharia em camundongo; a genética comum
  humana de humor é de efeito pequeno e heterogênea.

### 4.4 Epigenética e expressão
- Metilação/expressão de genes do eixo (DIO2, THRA/THRB, transportadores) em tecido humano e
  sua reversibilidade por estado/tratamento em ansiedade/depressão: **literatura insuficiente
  para maior resolução nesta camada** — declarado como lacuna, não preenchido com extrapolação
  (a epigenética do eixo tireoidiano está bem descrita em desenvolvimento/metabolismo, mas não
  especificamente em humor).

> **Autoauditoria do Módulo 04:** cada variante humana passou pelo teste de escopo (há estudo
> em humor/bipolar). O contraste **mecanismo celular forte (DIO2/Jo; MCT8) × associação humana
> fraca/replicação mista** está explícito; a coorte de Amsterdã (não replicação) é citada como
> "referência a confirmar no G2", sem PMID inventado. A genética UK Biobank é apresentada como
> co-hereditariedade por **autoimunidade**, não como "gene da tireoide causa depressão". THRA/
> THRB/TSHR em humor e a epigenética permanecem `[G1]`/lacuna. O achado pós-AVC foi sinalizado
> como extrapolação.

[REF_MODULO_04: Jo_2019 | Beltrao_2024 | Galecka_2015 | Galecka_2016 | He_2009 |
Philibert_2011 | Cooper-Kazaz_2009 | Taroza_2020 | Soheili-Nezhad_2023 | Pappa_2021 |
Guillen-Yunta_2024 | Valcarcel-Hernandez_2024 | Bruschi_2026 | Bianco_2018]

---

## MÓDULO 05 — BIOMARCADORES EXAUSTIVOS
*(catálogo apenas — **sem protocolo de coleta, sem valor de corte**; regra do BLOCO_05 do Prompt
4.0. Lista-se a identidade molecular, a direção da alteração e a especificidade; a operação fica
para a clínica/Prompt 4.2.)*

### 5.1 Periféricos / sangue
- **TSH (sérico)** — rastreio de função; eleva-se no hipotireoidismo (e na disfunção induzida
  por lítio), suprime-se no hipertireoidismo. Associação transversal/longitudinal com depressão
  heterogênea (Varella et al., 2021; Kumar et al., 2023; Roa et al., 2024; revisão crítica
  Samuels et al., 2018). **Especificidade baixa para humor** — é marcador de função tireoidiana,
  não "teste de depressão"; confundido por hora do dia (pico noturno), idade, sexo, lítio,
  gestação e doença aguda [humano; **marcador**; bem suportado como teste endócrino, fraco como
  marcador psiquiátrico].
- **T4 livre (T4L)** — hormônio circulante; T4L baixo-normal prediz depressão futura em parte
  das coortes (Odawara et al., 2023); confundido por NTIS/desnutrição/medicação. Especificidade
  baixa [humano; preditivo/associativo; moderadamente suportado].
- **T3 livre / T3 total** — forma ativa circulante; T3 baixo é marcador de NTIS/doença (Nader
  et al., 1996; Iosifescu et al., 2001; Schorr & Miller, 2017). Especificidade baixa.
- **rT3 (T3 reverso)** — marcador de desvio de conversão/NTIS; não disponível na rotina.
  Especificidade baixa [humano; marcador; emergente].
- **TBG** — altera o total sem mudar o livre [básico; marcador; muito estabelecido].
- **Anti-TPO (TPOAb)** — marcador de autoimunidade; positividade isolada **não** é sinônimo de
  doença nem de depressão (alta prevalência de base; Bode et al., 2021; Tian et al., 2025).
  Especificidade baixa para humor [humano; marcador/controverso; moderadamente suportado].
- **Anti-tireoglobulina (TgAb) e TRAb** — marcadores de autoimunidade/Graves; TgAb correlaciona-se
  com ansiedade/neuroimagem em estudos pequenos (Yang W. et al., 2023). Especificidade baixa
  [humano; marcador; emergente].
- **Artefato de ensaio a registrar (identidade, não protocolo):** a **biotina** em altas doses
  interfere nos imunoensaios de TSH/T3/T4, podendo gerar resultado falso; e o **corte de TSH**
  que define "subclínico" varia entre diretrizes, alterando a prevalência estimada (insumo B)
  [metodológico; confundidor; bem suportado].

### 5.2 Centrais / líquor e dinâmicos
- **Teste de estímulo ao TRH (resposta de TSH):** marcador **histórico** da psiquiatria
  biológica — resposta de TSH achatada/alterada em subgrupo de deprimidos (Sternbach et al.,
  1983; Extein et al., 1981; Bunevicius et al., 1996; revisão do teste, 1982). **Hoje fora de
  uso rotineiro**; especificidade baixa [humano; **marcador histórico**; moderadamente
  suportado na literatura clássica].
- **TRH no líquor (CSF)** — diferenças de sexo e implicações descritas (Frye et al., 1999)
  [humano; marcador central; emergente].
- **Relação rT3/T3 e marcadores de conversão central** — estimam o metabolismo tecidual;
  pesquisa, não rotina [humano; marcador; hipótese inicial].

### 5.3 Neuroimagem
- **Volume hipocampal** — reduzido no hipotireoidismo adulto (Cooke et al., 2014) [humano/RM;
  **marcador/associativo**; moderadamente suportado]. Inespecífico (compartilhado por outros
  mecanismos B3/estresse).
- **Metabolismo cerebral de glicose (PET)** — alterado no hipotireoidismo, revertendo após
  correção do estado endócrino (Bauer, Silverman et al., 2009) [humano/PET; marcador/estado;
  moderadamente suportado].
- **Alterações corticais e anticorpos (TgAb) em MDD + Hashimoto** — neuroimagem 2026
  (frontier, não causal) [humano; associativo/exploratório; **emergente**].
- **Piso de resolução:** a neuroimagem da **sinalização** tireoidiana central em humor
  (receptores/transportadores in vivo) é, hoje, limitada — "literatura ainda em consolidação
  nesta camada"; os três itens acima satisfazem o piso mínimo, mas não há marcador de imagem
  validado.

### 5.4 Genéticos / moleculares (pesquisa)
- **Genótipo DIO2 Thr92Ala (rs225014)** — marcador **estático de risco** (não de estado);
  replicação mista; **não** deve ser usado isoladamente para decidir conduta (Beltrão et al.,
  2024; Jo et al., 2019) [humano/in vitro; marcador de predisposição; emergente].
- **Expressão cerebral de transportadores/receptores (MCT8, D2, TRα/β)** — hoje acessível só em
  modelo/tecido; não é marcador clínico [pesquisa; hipótese inicial].

> **Especificidade global (a levar ao Módulo 08):** **nenhum** desses marcadores é específico de
> ansiedade/depressão — todos são marcadores de **função/estado tireoidiano periférico**, de
> autoimunidade ou de estrutura cerebral inespecífica, compartilhados por outras condições. O
> achado central e negativo do mecanismo é que **normalizar o TSH não equivale a resolver o
> sintoma subjetivo** (sinal do ensaio TRUST e do IPD; Módulo 08), e que 10–15% dos pacientes com
> o hormônio normalizado seguem sintomáticos (Soheili-Nezhad et al., 2023). Os confundidores
> (biotina, corte de TSH, sexo, idade, lítio, gestação, NTIS, hora da coleta, causalidade
> reversa) estão catalogados no Briefing.

> **Autoauditoria do Módulo 05:** catálogo em quatro níveis (periférico / central-dinâmico /
> neuroimagem / genético), **sem protocolo nem valor de corte**. Indicou-se direção da alteração
> e especificidade (toda baixa/moderada, **nenhuma alta**). O teste de TRH foi apresentado como
> marcador histórico, não prática corrente; a neuroimagem de sinalização in vivo foi declarada
> como camada em consolidação. Não se apresentou nenhum marcador como "teste de depressão" nem
> qualquer intervenção como conduta.

[REF_MODULO_05: Varella_2021 | Kumar_2023 | Roa_2024 | Samuels_2018 | Odawara_2023 |
Nader_1996 | Iosifescu_2001 | Bode_2021 | Tian_2025 | Yang_W_2023 | Sternbach_1983 |
Extein_1981 | Bunevicius_1996 | Frye_1999 | Cooke_2014 | Bauer_Silverman_2009 | Beltrao_2024 |
Jo_2019 | Soheili-Nezhad_2023]

---

*Fim da PARTE 1 (Módulos 00–05). A PARTE 2 (Módulos 06–10: interconexões B1–B16, subtipos/
fenótipos, controvérsias/evidência negativa, tabela × Prompt 4.0 e outras condições) será gerada
após liberação explícita, e então unida a este arquivo.*
