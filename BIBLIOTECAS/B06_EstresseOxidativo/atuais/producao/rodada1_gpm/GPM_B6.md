# GPM_B6 — ESTRESSE OXIDATIVO / NITROSATIVO (REDOX, O&NS) EM ANSIEDADE E DEPRESSÃO
## Gerador de Profundidade Molecular — Rodada 1 (insumo para a Rodada 2/canônica)

Mecanismo: `mecanismo_B6_estresse_oxidativo` · Data: 2026-09-05 · Prompt: v4.2.
Base: `BRIEFING_B6_CONSOLIDADO_RODADA0` (fusão Arena + Claude 13/13 + ChatGPT 18/18; ~45 PMIDs
verificados G1; Gemini 0/5 — reenraizado/descrito no apêndice do briefing).

> **Regra de leitura:** a B6 é uma biblioteca de **mecanismo** — descreve biologia, não diagnostica
> nem prescreve. O principal risco deste módulo é transformar uma associação biológica sólida em
> recomendação de suplementação antioxidante. Por isso o MÓDULO 08 (controvérsias/negativo) tem o
> mesmo peso do miolo.

---

## MÓDULO 00 — METADADOS E ESCOPO

- **ID canônico:** mecanismo_B6_estresse_oxidativo. **Natureza:** suporte à decisão — não diagnostica.
- **Escopo:** a **desregulação do equilíbrio redox** — produção de espécies reativas de oxigênio
  (**ROS**: O₂•⁻, H₂O₂, •OH) e de nitrogênio (**RNS**: •NO, ONOO⁻) versus a capacidade antioxidante
  (enzimática + glutationa + Nrf2) — e o dano daí decorrente a lipídios, proteínas e DNA, em
  ansiedade e depressão. Cobre (i) fontes de ROS/RNS, (ii) defesas escalonadas, (iii) glutationa e
  Nrf2, (iv) marcadores de dano, (v) fronteira **ferroptose/GPX4** e mitocôndria-imunidade, e
  (vi) ansiedade/TEPT e o eixo telômero/envelhecimento.
- **Corte de conhecimento / busca em tempo real:** **busca ativa em 2026-09-05** via E-utilities/
  PubMed. ~45 âncoras com **PMID verificado** (G1: existência+título/periódico/autor). Três insumos
  auditados: Claude **13/13**; ChatGPT **18/18** (incl. 4 de 2025–26); Gemini **0/5** confiável
  (3 PMIDs trocados; 2 reais com atribuição errada — Palta 2014=**24336428** e Bhatt&Patil
  2020=**32404275**, reenraizados). Alvos sem PMID seguem `[G1]`.
- **Selos:** `[ML]` roedor/célula; `[EC]` humano; `[OB]` revisão; `[MA]` meta-análise;
  `[EXT]` extrapolado de outro campo/modelo; `[EMERGENTE]` disputa/evidência mista. G2/G3
  (espécie/desenho/força) é curadoria da Rodada 2.
- **Fronteira editorial B6×B9 (decisão):** B6 fica com a **química redox** (produção/dano de
  ROS/RNS, defesas, GSH, Nrf2, peroxidação, ferroptose, marcadores). A **bioenergética mitocondrial**
  como maquinaria (ATP, biogênese/PGC-1α, fissão/fusão, mitofagia, cópias de mtDNA) é a **B9**. A ETC
  aparece na B6 apenas como **fonte de ROS** e vítima de dano; os papers puramente mitocondriais
  (Tobe 23650447, Rappeneau 32979495, Allen 33220501, Khan 37189442, Larrea 38541952, Wang
  42399415) entram como **crosstalk/B9**, não como miolo.

`[REF_MODULO_00: briefing consolidado B6 (2026-09-05); política de selos herdada da B1/B5; Maes 2011 PMID 20471444]`

---

## MÓDULO 01 — MAPA EXAUSTIVO DE VIAS MOLECULARES

1. **Definição operacional (O&NS):** desequilíbrio entre geração de ROS/RNS e a capacidade de
   neutralizar/reparar/adaptar — não é "radicais livres altos" nem uma doença isolada. Termo
   **oxidative & nitrosative stress (O&NS)** cunhado por Maes para não invisibilizar o nitrosativo
   (Maes, Galecki, Chang & Berk, 2011, *PNPBP*, PMID **20471444** `[OB]`; revisões de base Morris/Maes
   2018, *Mol Neurobiol*, PMID **29294244**, e Leonard & Maes 2012, *Neurosci Biobehav Rev*,
   PMID **22197082**).
2. **Fontes de ROS — mitocôndria/ETC (fronteira B9):** vazamento de elétrons nos complexos I/III
   gera O₂•⁻ → dismutação a H₂O₂; queda de eficiência da cadeia aumenta a produção. Loop
   disfunção→ROS→dano→mais disfunção (Tobe 2013, PMID **23650447** `[OB]`; Rappeneau/Touma 2020,
   PMID **32979495** `[OB]`; Allen/Kalynchuk 2021, PMID **33220501** `[OB]`).
3. **Fontes de ROS — NADPH oxidases (NOX1/2/4):** fonte enzimática independente da mitocôndria,
   ativada por citocinas; **NOX2 microglial** é fonte relevante de surto oxidativo na neuroinflamação
   (ponte B1). Lastro direto em comportamento de humor `[G1]`.
4. **Fontes de ROS — MAO (elo B4):** a monoamina oxidase A/B, ao degradar 5-HT/DA/NE, gera
   **H₂O₂** como subproduto obrigatório; maior atividade de MAO = fonte direta de ROS. PMID próprio
   em humor `[G1]`.
5. **Fontes de RNS — NOS desacoplada/peroxinitrito (elo B1):** •NO (nNOS/iNOS/eNOS) é fisiológico,
   mas sob **BH4 limitante** a NOS desacopla e •NO + O₂•⁻ → **ONOO⁻** (peroxinitrito), que nitra
   proteínas (**3-nitrotirosina**). A via da BH4 liga redox, inflamação e síntese de monoaminas/NO
   (Fanet, Capuron, Castanon, Calon & Vancassel, 2021, *Curr Neuropharmacol*, PMID **32744952** `[OB]`).
6. **Outras fontes:** peroxissomos (H₂O₂), xantina oxidase, ciclo do araquidonato/CYP, metais
   redox-ativos (Fe²⁺/Cu).
7. **Dano oxidativo — lipídios:** ROS atacam PUFAs de membrana → hidroperóxidos → aldeídos reativos
   (**MDA/malondialdeído**, 4-HNE) e **F2-isoprostanos**; 4-HNE modifica proteínas e altera função.
   Meta de peroxidação lipídica em TDM/bipolar (176 estudos, 34.051 participantes): Almulla,…,Maes
   2023, *Brain Behav Immun*, PMID **37557967** `[MA]`.
8. **Dano oxidativo — proteínas:** carbonilação, AOPP, 3-nitrotirosina, oxidação de sulfidrilas.
9. **Dano oxidativo — DNA/RNA:** **8-OHdG/8-oxo-dG** (DNA nuclear e **mtDNA**, que está perto da
   ETC e sem histona), 8-oxoGuo (RNA). Meta: Black, Bot, Scheffer, Cuijpers & Penninx, 2015,
   *Psychoneuroendocrinology*, PMID **25462890** `[MA]` (8-OHdG g≈0,31; F2-isoprostanos g≈0,48).
10. **Defesas enzimáticas (sistema escalonado):** **SOD1** (Cu/Zn, citosol), **SOD2** (Mn,
    mitocôndria), **SOD3** (extracelular) convertem O₂•⁻→H₂O₂; **catalase** e **GPx** removem H₂O₂;
    **GPX4** reduz hidroperóxidos de membrana e é o freio central da **ferroptose**; completam
    **glutationa redutase (GSR)**, peroxirredoxinas (PRDX), tiorredoxina (TRX/TXN), GST.
11. **Defesas não-enzimáticas:** **glutationa (GSH/GSSG)** — principal antioxidante solúvel,
    síntese limitada por **cisteína** (GCL: GCLC/GCLM); vitaminas E (lipofílica)/C; **ácido úrico**,
    zinco `[G1]`; melatonina; NAC como doador de cisteína.
12. **Sensor-mestre Nrf2/Keap1-ARE:** em basal Keap1 degrada Nrf2; sob estresse redox, Keap1 é
    modificado, Nrf2 estabiliza, transloca e liga **ARE**, induzindo HO-1, NQO1, GCLC/GCLM, GST,
    GPX, enzimas de GSH. Nrf2 está reduzido na maior parte dos estudos de depressão e sobe com
    antidepressivo; **mas a tradução humana é fraca** (revisão sistemática com 89 estudos, só **4
    humanos**: Sani et al., 2023, *Antioxidants*, PMID **37107192** `[OB]`; Hashimoto 2018,
    PMID **30386243** `[OB]`; mecanismo geral Tebay/Hayes 2015, PMID **26122708** `[OB]`).
13. **Nrf2 × NF-κB (crosstalk molecular B6↔B1):** Nrf2 comanda a resposta antioxidante/citoprotetora
    e antagoniza o eixo inflamatório NF-κB; não é apenas associação conceitual (Czarny et al., 2018,
    *PNPBP*, PMID **28669580** `[OB]`).
14. **Ciclo vicioso integrado:** estressores (HPA/Inflamação/metabólico) → mitocôndria → ROS/RNS ↑ →
    redução da capacidade redox/GSH → dano + sinalização anormal (Nrf2↓, NF-κB↑, GSH↓) → disfunção
    mitocondrial + microglia → alteração de glutamato/BDNF/ferroptose → disfunção sináptica →
    sintomas; cada braço retroalimenta o EO.
15. **Redox como sinal fisiológico (hormese):** ROS em baixa concentração participam de plasticidade,
    diferenciação e defesa; só o excesso crônico é patológico (Kakizawa, 2017, PMID **29118286**
    `[OB/ML]`) — fundamento para não "suprimir tudo".

`[REF_MODULO_01: Maes 2011 PMID 20471444; Almulla 2023 PMID 37557967; Black 2015 PMID 25462890; Sani 2023 PMID 37107192; Fanet 2021 PMID 32744952; Czarny 2018 PMID 28669580; Tobe 2013 PMID 23650447]`

---

## MÓDULO 02 — MAPA EXAUSTIVO DE MEDIADORES MOLECULARES

1. **Superóxido O₂•⁻** — ETC/NOX/XO; dismutado por SOD.
2. **Peróxido de hidrogênio H₂O₂** — mais difusível; removido por catalase/GPx; subproduto da MAO (B4).
3. **Radical hidroxila •OH** — o mais reativo (reação de Fenton com Fe²⁺/Cu); dano irreversível.
4. **Óxido nítrico •NO** — sinalizador fisiológico (nNOS/iNOS/eNOS); vira RNS quando em excesso.
5. **Peroxinitrito ONOO⁻** — •NO+O₂•⁻; nitração (3-nitrotirosina); ponte inflamação↔redox.
6. **Glutationa GSH/GSSG** — razão como "termômetro" redox; GSSG→GSH por GSR usando NADPH;
   disponibilidade de cisteína é o gargalo.
7. **GPX4** — glutationa peroxidase que reduz peróxidos de membrana; freio da ferroptose.
8. **Produtos de peroxidação lipídica:** MDA, 4-HNE, F2-isoprostanos (8-iso-PGF2α).
9. **Marcadores de dano:** 8-OHdG/8-oxo-dG, carbonóis proteicos, AOPP.
10. **Nrf2/Keap1; HO-1; NQO1; GCLC/GCLM** — eixo de transcrição antioxidante.
11. **BH4 (tetraidrobiopterina)** — cofator da síntese de monoaminas e da NOS; oxidada sob EO,
    reduz síntese de 5-HT/DA e desacopla NOS (Fanet **32744952**).
12. **Ferro lábil (Fe²⁺)/ferritina/transferrina** — alimentam Fenton e a ferroptose.
13. **TAC (capacidade antioxidante total)** e atividades SOD/catalase/GPx — marcadores de "defesa".

### Inventário negativo (mediadores/hipóteses SEM associação causal consistente)
- **"A depressão é causada por estresse oxidativo"** — maioria transversal; direção causal
  `[EMERGENTE]` (Fedoce 2018, PMID **29742940**).
- **"Antioxidantes tratam depressão"** — metas de suplementos (vit. C/E, polifenóis) pequenas/mistas/
  nulas; NAC é adjuvante promissor, não terapia de primeira linha.
- **"Todo deprimido tem deficiência antioxidante"** — marcadores medem processos distintos e nem
  sempre concordam; GSH é **regional** (occipital ↓, PFC medial inalterado na meta Bell 2025).
- **"Nrf2 baixo causa depressão"** — evidência majoritariamente molecular/celular/animal (4 de 89
  estudos humanos em Sani 2023).
- **"Ferroptose causa MDD"** — hipótese de fronteira, quase toda roedor/pós-morte `[EXT]`.
- **"Quanto mais antioxidante, melhor"** — ROS é sinal fisiológico (plasticidade/defesa/hipóxia).
- **Fitoterápicos/polifenóis antioxidantes como lastro** — superdosagem in vitro, má biodisponibilidade
  no SNC, viés positivo (ruído dominante da busca).
- **Marcador periférico (sangue) = redox cerebral** — sangue não espelha SNC; MDA/TBARS inespecífico.
- **GSH oral como reposição direta** — mal atravessa a barreira; NAC é precursor, não GSH.
- **Teoria dos radicais livres do envelhecimento (Harman, 1956) como fato simples** — revisada na
  biogerontoria; aplicar com cautela.
- **Neo-epítopos oxidativos/autoimunidade (Maes)** — neoantígenos de dano O&NS → IgM; hipótese de um
  grupo, pouco replicada `[EMERGENTE]`.

`[REF_MODULO_02: Fedoce 2018 PMID 29742940; Bell 2025 PMID 39708105; Sani 2023 PMID 37107192; Fanet 2021 PMID 32744952; Almulla 2023 PMID 37557967; Kakizawa 2017 PMID 29118286]`

---

## MÓDULO 03 — MAPA EXAUSTIVO DE TIPOS CELULARES E ESTRUTURAS

1. **Mitocôndria neuronal (fonte e vítima):** ETC vaza O₂•⁻; mtDNA vulnerável; EO danifica
   complexos e fecha o loop (ver B9); sobrecarga de Ca²⁺ por excitotoxicidade (B5) estoura ROS.
2. **Microglia:** ao ativar-se (citocinas/QUIN/LPS do B1/B7) monta **NOX2** e **iNOS**, gerando
   surto de ROS/RNS; mtROS/DAMPs ativam o **inflamassoma NLRP3** (Sorbara & Girardin, 2011, *Cell
   Res*, PMID **21283134** `[OB]`; Wang et al., 2026, *Mol Psychiatry*, PMID **42399415** `[OB]`).
3. **Astrócito:** sustentação redox — fornece precursores de **GSH** aos neurônios, expressa o
   transportador **system Xc⁻** (troca cistina/glutamato) e **EAAT1/2**; o EO oxida EAAT e deixa
   glutamato em excesso (elo B5). Regulação astrocitária de ferro/PCBP1 e ferroptose no estresse
   (Zhang et al., 2026, *Adv Sci*, PMID **41387185** `[ML]`).
4. **Neurônio:** rico em PUFAs e metais, alto consumo de O₂ — vulnerável a peroxidação; ablação de
   **GPX4** causa degeneração neuronal por ferroptose (Chen et al., 2015, *J Biol Chem*, PMID
   **26400084** `[ML]`).
5. **Ferro lábil/ferroptose:** morte regulada ferro-dependente por peroxidação de fosfolipídios,
   freada por GPX4/GSH; revisões de humor Feng 2025 (PMID **40177374**), Liu 2025 (eixo
   ferroptose-mitocôndria, PMID **40427494**), Zhang 2026 (PMID **42507173**) — todas majoritariamente
   pré-clínicas `[EXT]/[EMERGENTE]`.
6. **Telômero/senescência celular:** estresse psicológico crônico → EO → menor atividade de
   telomerase → encurtamento de telômero (Epel et al., 2004, *PNAS*, PMID **15574496** `[EC]`);
   hipótese de **envelhecimento acelerado** no TEPT (Miller & Sadeh, 2014, *Mol Psychiatry*, PMID
   **25245500** `[OB]`).
7. **Por que o cérebro é vulnerável:** ~20% do O₂ corporal, grande massa de PUFAs, metais
   redox-ativos, metabolismo mitocondrial intenso, demanda contínua de ATP/neurotransmissão e defesas
   relativamente limitadas (Bouayed, Rammal & Soulimani, 2009, PMID **20357926** `[OB]`).
8. **Estruturas-regionais:** GSH cerebral é **regional** (córtex occipital vs PFC medial vs
   cingulado); amígdala/hipocampo no estresse/medo (ansiedade/TEPT).

`[REF_MODULO_03: Sorbara 2011 PMID 21283134; Wang 2026 PMID 42399415; Chen 2015 PMID 26400084; Epel 2004 PMID 15574496; Miller&Sadeh 2014 PMID 25245500; Bouayed 2009 PMID 20357926; Feng 2025 PMID 40177374]`

---

## MÓDULO 04 — VARIABILIDADE GENÉTICA E EPIGENÉTICA EXAUSTIVA

1. **SOD2 (Ala16Val, rs4880)** — altera o direcionamento mitocondrial da Mn-SOD; mais estudado dos
   polimorfismos redox; lastro específico em humor `[G1]`/`[EMERGENTE]`.
2. **GPX1 (Pro198Leu)** — atividade da glutationa peroxidase; `[G1]`.
3. **GSTM1/GSTT1 (nulos), CAT (−262C>T), NQO1, NFE2L2 (gene do Nrf2)** — variantes de fase II/
   defesa; NFE2L2 emergente.
4. **HFE (hemocromatose/ferro)** — interface ferro lábil/ferroptose `[G1]`.
5. **Haplogrupos de mtDNA** (herança materna) — variabilidade basal de ROS; mais dados em
   neurodegeneração que em psiquiatria `[EXT]`.
6. **Epigenética:** Nrf2/NFE2L2, enzimas antioxidantes e reparo regulados por metilação/histonas sob
   estresse crônico; interface com BDNF (B3) e FKBP5 (B2/B12) `[G1]`.
7. **Cruzamentos:** MAOA/B (B4 — fonte de H₂O₂), NOS/iNOS (B1), TFAM/mtDNA (B9), BDNF Val66Met (B3).

`[REF_MODULO_04: variantes majoritariamente [G1]/[EMERGENTE] — busca na Rodada 2; Sani 2023 PMID 37107192 (contexto Nrf2)]`

---

## MÓDULO 05 — BIOMARCADORES EXAUSTIVOS

1. **Glutationa cerebral por ¹H-MRS (espectroscopia por ressonância magnética — janela humana in
   vivo mais direta):**
   - Godlewska, Near & Cowen, 2015, *Psychopharmacology*, PMID **25074444** `[EC]` (GSH reduzido na TDM).
   - Lapidus,…,Shungu, 2014, *Neurosci Lett*, PMID **24704328** `[EC]` (GSH↔EO↔anedonia).
   - **Meta Bell et al., 2025, *Psychopharmacology*, PMID 39708105** `[MA]` — 8 estudos, 230
     pacientes/216 controles; GSH menor no **córtex occipital** (g≈−0,98; IC95% −1,45 a −0,50),
     **sem** diferença no PFC medial nem na análise combinada → redução **regional**, não global.
   - Lee et al., 2025, *Biol Psychiatry*, PMID **39218137** `[EC]` — GSH menor em mPFC/precuneus na
     TDM (e TOC), associado à relação GSH–glutamato–atividade neuronal espontânea (MRS+fMRI).
2. **Marcadores de dano (periféricos):** MDA/TBARS (inespecífico), 4-HNE, **F2-isoprostanos** (mais
   específico), 8-OHdG/8-oxo-dG, carbonóis, 3-nitrotirosina. Metas: Black 2015 (**25462890**),
   Almulla 2023 (**37557967**), Jiménez-Fernández 2015 (**26579881**), Palta 2014 (**24336428**);
   coorte longitudinal CARDIA (cross-sectional e longitudinal: Black, Penninx, Bot et al., 2016,
   *Transl Psychiatry*, PMID **26905415** `[EC]`).
3. **Marcadores de capacidade/defesa:** atividades SOD/catalase/GPx, **TAC**, razão GSH/GSSG,
   ácido úrico/zinco `[G1]`.
4. **Telômero (sangue):** comprimento telomérico como marcador de carga oxidativa/envelhecimento
   (Epel **15574496**; Miller&Sadeh **25245500**) — com confundidores fortes (ver §9 do briefing).
5. **Confundidores críticos (briefing §9):** método (TBARS vs HPLC; ELISA vs HPLC-MS), coleta
   (**GSH degrada ex vivo — congelar a −80 °C**), hemólise, suplemento antioxidante recente (~72h,
   afeta TAC), tabaco/dieta/IMC/exercício/idade, inflamação/PCR (ferritina de fase aguda), campo de
   MRS (3T/7T) e edição de espectro, medicação (NAC/antioxidante), composição leucocitária
   (telômero), e o princípio geral **periférico ≠ redox cerebral**.
6. **Sem marcador in vivo direto de ferroptose/Nrf2 em humano** — toda leitura é indireta.

`[REF_MODULO_05: Bell 2025 PMID 39708105; Lee 2025 PMID 39218137; Godlewska 2015 PMID 25074444; Lapidus 2014 PMID 24704328; Black 2015 PMID 25462890; Almulla 2023 PMID 37557967; Jiménez-Fernández 2015 PMID 26579881; Palta 2014 PMID 24336428]`

---

## MÓDULO 06 — INTERCONEXÕES EXAUSTIVAS COM B1–B16

1. **B6↔B1 (neuroinflamação) — muito alta:** mtROS/DAMPs → **NLRP3** (Sorbara **21283134**; Wang
   **42399415**); iNOS→ONOO⁻; NOX2 microglial; **Nrf2↔NF-κB** antagonistas; citocinas induzem EO;
   Czarny **28669580**.
2. **B6↔B9 (mitocôndria) — muito alta (fronteira):** ETC como fonte de ROS e vítima; loop
   disfunção→ROS; papers B9: Tobe **23650447**, Rappeneau **32979495**, Allen **33220501**, Khan
   **37189442**, Larrea **38541952**, Wang **42399415**.
3. **B6↔B3 (plasticidade/BDNF) — muito alta:** EO em excesso prejudica LTP/sinaptogênese e
   BDNF/TrkB/CREB; GSH é necessária à plasticidade; Nrf2↔BDNF; ROS fisiológico sinaliza plasticidade
   (Kakizawa **29118286**); revisão Correia, Cardoso & Vale, 2023, *Antioxidants*, PMID **36830028**;
   cetamina reverte EO em modelo (Réus **25613382** `[ML]`).
4. **B6↔B4 (monoaminas) — alta:** **MAO gera H₂O₂** ao degradar 5-HT/DA/NE `[G1]`; **BH4** limita a
   síntese de monoaminas e o acoplamento da NOS (Fanet **32744952**).
5. **B6↔B5 (GABA/glutamato) — alta:** GSH = glutamato+cisteína+glicina; **system Xc⁻** (troca
   cistina/glutamato); EO oxida **EAAT** → ↑glutamato extracelular → excitotoxicidade → sobrecarga
   de Ca²⁺ mitocondrial → mais ROS; NAC atua nesse eixo; GSH↔glutamato↔atividade neuronal
   (Lee **39218137**); ansiolíticos que contrapõem EO+neuroinflamação+glutamato (Santos/Piato, 2019,
   *Braz J Psychiatry*, PMID **30328963**).
6. **B6↔B2 (HPA) — alta:** glicocorticoides/**cortisol** bifásicos (agudo podem ter propriedade
   antioxidante; exposição crônica ↑EO); é o caminho proposto por Epel para o encurtamento de
   telômero (**15574496**).
7. **B6↔B7 (disbiose) / B8 (dieta/micronutrientes) — moderada:** translocação de LPS intestinal
   (disbiose, B7) provoca surto oxidativo além da via inflamatória; alguns ácidos graxos de cadeia
   curta modulam o estado redox; cofatores nutricionais (Se→GPx; Zn/Cu/Mn→SOD), NAC e ômega-3
   (Liao 2019, *Transl Psychiatry*, PMID **31383846** `[MA]`, efeito pequeno) — com ceticismo de
   suplementação.
8. **B6↔B12 (trauma/TEPT):** envelhecimento acelerado/EO no TEPT (Miller&Sadeh **25245500**);
   amígdala/medo.
9. **B6↔B13 (endocanabinoide) — emergente:** CBD como antioxidante/ativador de Nrf2
   extra-CB1/CB2 `[G1]`.
10. **B6↔B10 (sono/ritmo):** ritmo da defesa antioxidante; privação de sono eleva EO `[G1]`.

`[REF_MODULO_06: Sorbara 2011 PMID 21283134; Wang 2026 PMID 42399415; Czarny 2018 PMID 28669580; Fanet 2021 PMID 32744952; Lee 2025 PMID 39218137; Correia 2023 PMID 36830028; Epel 2004 PMID 15574496; Liao 2019 PMID 31383846]`

---

## MÓDULO 07 — SUBTIPOS, FENÓTIPOS E INTERVENÇÕES (DESCRIÇÃO, NÃO PRESCRIÇÃO)

1. **Eixo de estratificação redox:** subgrupo **"dano predominante"** (MDA/8-OHdG/F2-isoprostanos
   ↑) vs subgrupo **"defesa reduzida"** (SOD/GPx/GSH/Nrf2 ↓) — nem sempre coincidem no mesmo
   paciente; e a **regionalidade** do GSH (occipital vs PFC).
2. **Subgrupo TEPT/envelhecimento acelerado:** carga de estresso crônico, telômero curto, EO
   elevado (Miller&Sadeh **25245500**; Epel **15574496**).
3. **Transtorno bipolar vs TDM unipolar:** NAC tem sinal melhor em **bipolar** (Kishi et al., 2020,
   *Psychopharmacology*, PMID **32767039** `[MA]`) do que em TDM unipolar.
4. **Ansiedade:** literatura própria de desequilíbrio oxidativo (Bouayed **20357926**; Krolow et
   al., 2014, *Curr Neuropharmacol*, PMID **24669212**; Hassan et al., 2014, PMID **24669207**;
   Fedoce **29742940**), com causalidade mais fraca que a associação; ansiolíticos que contrapõem
   EO (Santos/Piato **30328963**). **Pânico e fobia social ainda sem âncora própria** `[G1]`.
5. **Intervenções descritas (NÃO prescritas):**
   - **N-acetilcisteína (NAC)** — doadora de cisteína → GSH; também modula system Xc⁻/glutamato.
     Meta Fernandes, Dean, Dodd, Malhi & Berk, 2016, *J Clin Psychiatry*, PMID **27137430** `[MA]`
     (benefício significativo mas de magnitude pequeno-moderada, heterogeneidade alta); meta
     atualizada Peng 2024, PMID **39504621** `[MA]` (resultado misto em TDM); mediação por
     inflamação/neurogênese Panizzutti 2018, PMID **30008280**; bipolar Kishi **32767039**.
   - **Ômega-3** — efeito pequeno/heterogêneo (Liao **31383846**).
   - **Antioxidantes dirigidos à mitocôndria (MitoQ, MitoTEMPO, SkQ1)** — fortes em roedor,
     tradução humana incipiente `[G1]`.
   - **Moduladores de Nrf2 (sulforafano, dimetilfumarato)** — maioria pré-clínica `[G1]`; **não há
     fármaco Nrf2-específico aprovado para humor** (assimetrio honesta vs B5, que tem neuroesteroides).
   - **Cetamina** — reverte parcialmente EO/dano energético em modelo (Réus 2015, PMID **25613382**
     `[ML]`), ligando ação rápida (B5) a redox.
   - **Fracassos/mistos:** vitaminas C/E, polifenóis/fitoterápicos (sinal nulo/misto, viés,
     biodisponibilidade).

`[REF_MODULO_07: Kishi 2020 PMID 32767039; Fernandes 2016 PMID 27137430; Peng 2024 PMID 39504621; Panizzutti 2018 PMID 30008280; Liao 2019 PMID 31383846; Miller&Sadeh 2014 PMID 25245500; Fedoce 2018 PMID 29742940; Réus 2015 PMID 25613382]`

---

## MÓDULO 08 — CONTROVÉRSIAS, HETEROGENEIDADE E LACUNAS

1. **Causa ou consequência?** — pergunta central não resolvida; maioria transversal; Fedoce 2018
   (**29742940**) nomeia no título. Direção causal `[EMERGENTE]`; a plataforma não a resolve.
2. **Sinal biológico robusto × tradução farmacológica fraca** — marcadores alterados e GSH reduzido
   por MRS convivem com metas de antioxidantes pequenas/mistas/nulas; NAC é adjuvante, não cura.
3. **Heterogeneidade de marcadores/tecidos/métodos** — I² alto; dano vs defesa nem sempre andam
   juntos; GSH é regional (occipital ↓ / PFC medial inalterado na meta Bell).
4. **Periférico ≠ cerebral** — MDA/TBARS inespecíficos; sangue é proxy imperfeito.
5. **Redox fisiológico/hormese** — ROS não é só dano; "suprimir tudo" é fisiologicamente ingênuo.
6. **Ferroptose em humor** — fronteira excitável mas quase toda roedor/pós-morte `[EXT]`; sem
   marcador in vivo humano.
7. **Nrf2 como alvo** — 4 de 89 estudos humanos (Sani 2023); sem fármaco aprovado; agonistas
   indiretos majoritariamente pré-clínicos.
8. **Ruído dos fitoterápicos/polifenóis** — domina as buscas de "antioxidante + depressão", com
   superdosagem in vitro e viés positivo; não é lastro.
9. **Teoria dos radicais livres do envelhecimento** — versão simplificada não é consenso atual.
10. **Lacuna de ansiedade por transtorno:** TAG/TEPT/ansiedade geral ancorados; **pânico e fobia
    social** sem âncora `[G1]`.
11. **Lacuna de PMID (`[G1]`):** NOX2↔comportamento; MAO→H₂O₂ em humor; MitoQ/SkQ1 humano;
    SOD2 rs4880 e GPX1/CAT/NFE2L2/HFE; sulforafano/dimetilfumarato em humor; ácido úrico/albumina;
    CBD antioxidante; pânico/fobia social.
12. **Insumos externos não confiáveis:** Gemini **0/5** (3 PMIDs trocados: lesão facial,
    lovastatina/leucemia, cirurgia de coluna; 2 reais com atribuição errada) — reforça a regra de
    chave=PMID e a lição de que aparência de rigor (tabela com PMC id) engana.

`[REF_MODULO_08: Fedoce 2018 PMID 29742940; Bell 2025 PMID 39708105; Sani 2023 PMID 37107192; Fernandes 2016 PMID 27137430; Feng 2025 PMID 40177374]`

---

## MÓDULO 09 — CHECKLIST DE VERIFICAÇÃO CRUZADA COM O PROMPT 4.0

- [x] Demarcação humano/pré-clínico (`[EC]/[ML]/[MA]/[OB]/[EXT]/[EMERGENTE]`) em todos os módulos.
- [x] Inventário negativo presente (MÓDULO 02): "antioxidante cura", "todo deprimido tem
      deficiência", "Nrf2 baixo causa", "ferroptose causa MDD", "quanto mais melhor", fitoterápicos,
      periférico=central, GSH oral, Harman simplificado, neo-epítopos.
- [x] Controvérsia explícita (causa/consequência; sinal forte × terapia fraca; GSH regional;
      ferroptose `[EXT]`) no MÓDULO 08.
- [x] Crosstalk nomeado por ID (B1/B2/B3/B4/B5/B7/B8/B9/B10/B12/B13) no MÓDULO 06, com fronteira
      B6×B9 decidida.
- [x] Confundidores de biomarcador (MÓDULO 05 + briefing §9): método, −80 °C para GSH, hemólise,
      suplemento/TAC, tabaco/dieta/IMC, MRS 3T/7T, periférico≠central, leucócitos/telômero.
- [x] Intervenções descritas sem prescrever (MÓDULO 07); NAC como adjuvante, não terapia.
- [x] Cobertura equilibrada: O&NS juntos; defesa escalonada; ansiedade/TEPT próprios; redox
      fisiológico; telômero/envelhecimento; fitoterápicos como ruído; assimetria de tradução.
- [ ] **Pendente da Rodada 2:** G2/G3 (espécie/desenho/força); resolução dos `[G1]`; âncoras de
      pânico/fobia social; chave primária = PMID; zero rótulo órfão.

`[REF_MODULO_09: verificações estruturais do Prompt 4.0; curadoria G2/G3 na Rodada 2]`

---

## MÓDULO 10 — OBSERVAÇÕES EM OUTRAS CONDIÇÕES

> **Nota de natureza:** os itens abaixo são **amostra ilustrativa** de onde o desequilíbrio redox
> também comparece, para orientar cruzamento do motor — **não constituem triagem completa** nem
> mecanismo compartilhado provado.

- **Neurodegeneração (Alzheimer/Parkinson/ELA):** ferroptose/GPX4, dano oxidativo e metais têm o
  lastro mais forte (contexto de onde muito da B6 é extrapolado — `[EXT]`).
- **AVC/isquemia-reperfusão:** surto de ROS e antioxidantes dirigidos (modelo clássico).
- **Envelhecimento/inflammaging:** telômero, declínio de Nrf2, EO crônico de baixo grau.
- **Esquizofrenia:** EO periférico e disfunção mitocondrial descritos; campo paralelo.
- **TEPT/trauma:** envelhecimento acelerado, telômero curto (Miller&Sadeh **25245500**).
- **Câncer/hematologia:** reservatório de literatura de NOX/Nrf2/ferroptose (fonte de extrapolação;
  cuidado com PMIDs de outros campos — lição da auditoria Gemini).
- **Fronteira 2025–2026:** cross-talk mitocôndria–imunidade (Wang **42399415**), eixo
  ferroptose-mitocôndria (Liu **40427494**), single-cell/spatial transcriptomics, lipidômica/
  metabolômica redox multimodal.

`[REF_MODULO_10: amostra ilustrativa; Miller&Sadeh 2014 PMID 25245500; Wang 2026 PMID 42399415; Liu 2025 PMID 40427494; Chen 2015 PMID 26400084]`
