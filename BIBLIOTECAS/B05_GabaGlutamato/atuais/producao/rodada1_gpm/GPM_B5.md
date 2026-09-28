# GPM_B5 — GABA / GLUTAMATO EM ANSIEDADE E DEPRESSÃO
## Gerador de Profundidade Molecular — Rodada 1 (insumo para a Rodada 2/canônica)

Mecanismo: `mecanismo_B5_gaba_glutamato` · Data: 2026-09-05 · Prompt: v4.2.
Base: `BRIEFING_B5_CONSOLIDADO_RODADA0` (fusão Arena+Claude; ~40 PMIDs verificados G1).

---

## MÓDULO 00 — METADADOS E ESCOPO

- **ID canônico:** mecanismo_B5_gaba_glutamato. **Natureza:** suporte à decisão — não diagnostica.
- **Escopo:** o **balanço excitação/inibição (E/I)** do cérebro — glutamato (excitatório) e GABA
  (inibitório) — em ansiedade e depressão. Cobre (i) o eixo GABA clássico (GABA-A por subtipo,
  GABA-B, neuroesteroides), (ii) a revolução glutamatérgica da cetamina/ação rápida, (iii) a
  fronteira (neuroesteroides aprovados, HNK, homeostase de cloreto, mGluR), e (iv) ansiedade/extinção.
- **Corte de conhecimento / busca em tempo real:** **busca ativa em 2026-09-05** via E-utilities/
  PubMed. ~40 âncoras com **PMID verificado** (G1). Três insumos externos foram auditados: o do
  Claude passou **19/19**; o "Consensus" (sem PMID) tinha referências fabricadas e o do Gemini tinha
  **6/6 PMIDs trocados** — ambos reenraizados ou descartados (apêndice do briefing). Itens sem PMID
  (Rudolph 1999 α1, Ressler 2004, Yang 2018 habeˆnula, Zorumski 2016, KCC2/NKCC1, TPA023,
  GABA-B/humor, esketamina spray) seguem `[G1]`.
- **Selos:** `[ML]` roedor/célula; `[EC]` humano; `[OB]` revisão; `[MA]` meta; `[EXT]` extrapolado;
  `[EMERGENTE]` disputa/evidência mista. G2/G3 é curadoria da Rodada 2.
- **Fronteira editorial:** **receptor/fármaco e circuito E/I na B5**; **desfecho estrutural
  (espinho/sinaptogênese) na B3**; estado de humor/modulação monoaminérgica na B4.

`[REF_MODULO_00: briefing consolidado B5 (2026-09-05); política de selos herdada da B1]`

---

## MÓDULO 01 — MAPA EXAUSTIVO DE VIAS MOLECULARES

1. **Síntese/degradação do GABA:** glutamato → **GAD65/GAD67** (GAD2/GAD1) → GABA; degradação por
   **GABA-T**; vesícula **VGAT**; recaptação **GAT-1/GAT-3**. GAD67/interneurônios reduzidos em
   depressão (pós-morte; Fee 2017, PMID 28697889; Maciag/Rajkowska 2010, PMID 20004363).
2. **GABA-A (ionotrópico, Cl⁻):** pentâmero de subunidades **α1–6, β1–3, γ1–3, δ**. Inibição
   **fásica/sináptica** (α1–3+γ2) vs **tônica/extrassináptica** (α4/6+β+**δ**, corrente de
   vazamento) — revisão Farrant & Nusser, 2005, PMID 15738957. Sítio benzodiazepínico (interface
   α/γ2); sítio neuroesteroide (δ/tônico).
3. **Farmacologia de subtipo do GABA-A:** **α1 = sedação/amnesia**; **α2/α3 = ansiólise** (Löw et
   al., 2000, *Science*, PMID 11021797; Smith/Rudolph, 2012, PMID 22465203); **α5 = cognitivo/
   ansiólise** (Behlke, 2016, PMID 27067130); revisão Reynolds/McKernan, 2001, PMID 11515499;
   Lüscher, 2023, PMID 37543478. Busca do "benzodiazepínico sem sedação" (TPA023/TP003) [G1].
4. **Neuroesteroides e GABA-A tônico:** alopregnanolona potencializa GABA-A em receptores δ;
   **brexanolone** IV (Kanes 2017 fase 2, PMID 28619476; Meltzer-Brody 2018 fase 3, PMID 30177236)
   e **zuranolona** oral (Deligiannidis 2021 ROBIN, PMID 34190962; 2023 SKYLARK, PMID 37491938) —
   aprovados para depressão pós-parto.
5. **GABA-B (metabotrópico Gi/Go, GIRK):** lento, pré/pós-sináptico; **baclofeno**; mais lastro em
   dependência que em humor [G1]. Gabapentinoides agem em **α2δ do canal de cálcio** (não são
   GABAérgicos diretos).
6. **Homeostase de cloreto (KCC2/NKCC1):** define se GABA é hiperpolarizante (adulto, KCC2 alto) ou
   despolarizante (desenvolvimento/pós-trauma, NKCC1 relativo) — relevante a TEPT e replasticidade
   [G1].
7. **Síntese/recaptação do glutamato:** glutamina→**glutaminase (GLS)**→glutamato; vesícula
   **VGLUT1/2**; recaptação glial **EAAT1(GLAST)/EAAT2(GLT-1)**; **ciclo glutamina–glutamato**
   astrocitário (sinapse tripartite; Yudkoff 1988, PMID 2900878; Rajkowska 2018, PMID 29660602).
   Falha de EAAT2 deixa glutamato em excesso (excitotoxicidade).
8. **Receptores ionotrópicos glutamatérgicos:** **NMDA** (GluN1 + GluN2A–D/GluN3; coagonista
   glicina/D-serina; Mg²⁺) — **sináptico GluN2A (LTP)** vs **extrassináptico GluN2B (LTD/toxicidade)**;
   **AMPA** (GluA1–4, condutor rápido da plasticidade); **cainato**.
9. **mGluR (metabotrópicos):** grupo I (**mGlu1/5**, pós, excitatório), grupo II (**mGluR2/3**, pré,
   freiam glutamato; níveis elevados no CPF de deprimidos pós-morte — Feyissa, 2010, PMID 19945495),
   grupo III (mGlu4/6/7/8). mGluR2/3 como ansiolítico alternativo [G1].
10. **Via da cetamina (elo B5↔B3):** antagonismo NMDA atinge **interneurônios GABAérgicos**
    (Homayoun & Moghaddam, 2007, PMID 17959792) → desinibição → surto de glutamato no CPF
    (Moghaddam, 1997, PMID 9092613) → **AMPA** → BDNF/TrkB → mTORC1 → sinaptogênese/espinhos
    (Moda-Sava, 2019, PMID 30975859; Li 2010, PMID 20724638). Arco clínico: Krystal 1994
    (psicotomimético, PMID 8122957) → Berman 2000 (1º RCT, PMID 10686270) → Zarate 2006
    (PMID 16894061) → bipolar Diazgranados 2010 (PMID 20679587).
11. **Disputa do mecanismo:** metabólito **(2R,6R)-HNK** com efeito alegadamente independente de
    NMDAR (Zanos, 2016, PMID 27144355) — **contestado**; debate Zorumski 2016 [G1]; tratamento com
    controle ativo **midazolam** (Wilkinson, 2019, PMID 30653192). Habeˆnula (Cui 2018,
    PMID 30718267; Yang 2018 [G1]).
12. **QUIN (ácido quinolínico, do B1) é agonista NMDA** — elo inflamação→glutamato/excitotoxicidade.

`[REF_MODULO_01: Farrant&Nusser 2005 PMID 15738957; Löw 2000 PMID 11021797; Meltzer-Brody 2018 PMID 30177236; Deligiannidis 2023 PMID 37491938; Homayoun 2007 PMID 17959792; Zarate 2006 PMID 16894061; Moda-Sava 2019 PMID 30975859; Feyissa 2010 PMID 19945495]`

---

## MÓDULO 02 — MAPA EXAUSTIVO DE MEDIADORES MOLECULARES

1. **GABA** — inibitório; reduzido no córtex na TDM (Sanacora, 1999, PMID 10565505; meta Schür,
   2016, PMID 27145016).
2. **Glutamato** — excitatório; anormalidades regionais por MRS (meta Yüksel & Öngür, 2010,
   PMID 20728076) — bidirecional conforme região/estado.
3. **Glicina / D-serina** — coagonistas do NMDA (sítio da glicina); **D-cicloserina** é agonista
   parcial e facilita a extinção (Davis/Ressler, 2006, PMID 16919524; dose/timing Rosenfield 2019,
   PMID 31698111).
4. **Neuroesteroides** — alopregnanolona/brexanolone/zuranolona sobre GABA-A δ (ver MÓDULO 01).
5. **Glutamina** — carro-chefe do ciclo astrocitário; entra no pool **Glx** do MRS.
6. **QUIN (ácido quinolínico)** — agonista NMDA derivado do triptofano/IDO (B1).
7. **Endocanabinoides (2-AG/AEA → CB1)** — sinal retrógrado que medeia **DSI** (terminais GABA) e
   **DSE** (terminais glutamatérgicos), ajustando E/I em tempo real (crosstalk B13).
8. **Enzimas/transportadores** — GAD65/67, GABA-T, GAT, VGAT; GLS, VGLUT, EAAT1/2.

### Inventário negativo (mediadores/hipóteses SEM associação causal consistente)
- **"Depressão = glutamato alto / GABA baixo" como frase simples** — regionalmente heterogêneo e
  bidirecional (MRS mostra reduções e elevações); não é um nível único.
- **"Bloqueio NMDA = mecanismo fechado da cetamina"** — o HNK (Zanos 2016) e o debate Zorumski
  mostram que a causalidade não está fechada; `[EMERGENTE]`.
- **Memantina (antagonista NMDA oral) como antidepressivo** — afinidade/cinética distintas; não
  reproduz a cetamina.
- **AMPAkinas / agonistas do sítio da glicina** como sucesso clínico — tradução mista/negativa.
- **Benzodiazepínicos como antidepressivos** — ansiolíticos agudos, não tratam depressão; tolerância/
  dependência/risco cognitivo; mascaram o tônus inibitório basal ("inibição artificial").
- **Pregabalina/gabapentina como "moduladores glutamatérgicos"** — agem em α2δ do canal de cálcio,
  não no sistema glutamatérgico diretamente.
- **Neuroesteroides generalizados** — aprovação é para depressão pós-parto, não TDM geral.
- **Déficit de interneurônio como causa provada em humano** — majoritariamente roedor/pós-morte
  correlacional → `[EXT]`.
- **Fitoterápicos "GABAérgicos/glutamatérgicos"** — sem RCT robusto (biodisponibilidade no SNC).
- **Microbiota produzindo GABA central via vagal** — majoritariamente pré-clínico `[EXT]`.

`[REF_MODULO_02: Sanacora 1999 PMID 10565505; Schür 2016 PMID 27145016; Yüksel 2010 PMID 20728076; Davis/Ressler 2006 PMID 16919524; Zanos 2016 PMID 27144355]`

---

## MÓDULO 03 — MAPA EXAUSTIVO DE TIPOS CELULARES E ESTRUTURAS

1. **Interneurônios GABAérgicos por subtipo:** **PV (parvalbumina)** — disparo rápido, alvo
   peri-somático, orquestra oscilações gama; **SST (somatostatina)** — alvo dendrítico de piramidais,
   déficit replicado em depressão (Fee 2017, PMID 28697889); **CCK/VIP**; BLA PV e CCK modulam
   ansiedade/depressão (Asim, 2024, PMID 39368965).
2. **Neurônios piramidais glutamatérgicos** do CPF/hipocampo — saída excitatória; perda de
   conectividade/espinhos na depressão (resgate por cetamina, Moda-Sava 2019).
3. **Astrócitos (sinapse tripartite):** capturam glutamato/GABA via EAAT/GAT, convertem em glutamina
   (Yudkoff 1988, PMID 2900878); patologia glial/astrocitária no CPF na depressão (Rajkowska 2018,
   PMID 29660602; Sanacora riluzole 2007, PMID 17141740).
4. **Microglia:** poda e modulação sináptica (complemento — B1/B3); sensível a QUIN/citocinas.
5. **Redes perineuronais (PNN):** matriz pericelular que envolve PV+ e "engessa" plasticidade
   (crosstalk B3); relevante à extinção do medo.
6. **Estruturas-circuitos:** **CPF/vmPFC** (conectividade, tomada de decisão, extinção), **amígdala/
   BLA** (ameaça/ansiedade — Asim 2024), **hipocampo**, **habeˆnula lateral** (anti-recompensa,
   burst; Cui 2018), circuito **cortico-estriado-tálamo-cortical** (TOC — Pittenger 2011,
   PMID 21963369).
7. **Células periféricas:** enterocromafins/GABA entérico e microbiota (sinal vagal; `[EXT]`).

`[REF_MODULO_03: Fee 2017 PMID 28697889; Asim 2024 PMID 39368965; Rajkowska 2018 PMID 29660602; Maciag 2010 PMID 20004363; Pittenger 2011 PMID 21963369; Yudkoff 1988 PMID 2900878]`

---

## MÓDULO 04 — VARIABILIDADE GENÉTICA E EPIGENÉTICA EXAUSTIVA

1. **GABRA2/GABRA3/GABRA5/GABRD** (subunidades α2/α3/α5/δ) — variantes; GABRA2 mais ligada a
   dependência de álcool; extensão a humor/ansiedade precisa de lastro [G1].
2. **GAD1 (GAD67)** — variantes mais robustas em esquizofrenia que em humor; expressão reduzida.
3. **GRIN1/GRIN2B (GluN1/GluN2B)**, **GRIA1 (GluA1)**, **GRM2/GRM3/GRM5 (mGluR)** — alvos
   farmacológicos e de risco.
4. **SLC1A2 (EAAT2/GLT-1)** — recaptação glial; mais estabelecido em epilepsia/ELA, emergente em humor.
5. **Epigenética:** expressão de GAD67/subunidades GABA-A e EAAT regulada por metilação/histonas sob
   estresse; interface com BDNF (B3) e FKBP5 (B2/B12) [G1].
6. Cruzamentos: 5-HTTLPR/MAOA (B4), FKBP5 (B2/B12), BDNF Val66Met (B3) modulam o E/I.

`[REF_MODULO_04: Fee 2017 PMID 28697889; Feyissa 2010 PMID 19945495; Fogaça&Duman 2019 PMID 30914923]`

---

## MÓDULO 05 — BIOMARCADORES EXAUSTIVOS

1. **GABA cortical por MRS (GABA+/MEGA-PRESS):** reduzido na TDM (Sanacora 1999; meta Schür 2016);
   sensível a campo/região/medicação.
2. **Glutamato/Glx por MRS (¹H; ¹³C para separar Glu/Gln):** anormalidades regionais (Yüksel 2010);
   Glx junta glutamato+glutamina.
3. **PET de receptor benzodiazepínico** ([¹¹C]flumazenil/[¹²³I]iomazenil): densidade/afinidade, não
   neurotransmissor em tempo real.
4. **Pós-morte:** densidade de interneurônios calbindina+/SST+ (Maciag 2010; Fee 2017), mGluR2/3
   (Feyissa 2010) — correlacional.
5. **Alopregnanolona sérica:** marcador de neuroesteroide (ciclo/gestação confundem).
6. **EEG/oscilações gama** como proxy de E/I (indireto).
7. **Sem marcador in vivo direto de neurotransmissor sináptico** — toda medida é indireta (ver
   confundidores no briefing §3).

`[REF_MODULO_05: Sanacora 1999 PMID 10565505; Schür 2016 PMID 27145016; Yüksel 2010 PMID 20728076; Maciag 2010 PMID 20004363]`

---

## MÓDULO 06 — INTERCONEXÕES EXAUSTIVAS COM B1–B16

1. **B5↔B3 (plasticidade — fronteira mais tênue):** NMDA/AMPA → desinibição → BDNF/TrkB → mTORC1 →
   espinhos/sinaptogênese; psicodélico 5-HT2A→espinhos (Shao 2021, PMID 34228959). Receptor na B5,
   espinho na B3.
2. **B5↔B4 (monoaminas):** 5-HT3 (único 5-HT ionotrópico) em interneurônios GABA; monoamina modula
   liberação de glutamato no CPF.
3. **B5↔B1 (neuroinflamação):** **QUIN é agonista NMDA**; citocinas reduzem EAAT2 e alteram GAD67/
   tráfego de GABA-A; poda por complemento afeta sinapses E e I.
4. **B5↔B2 (HPA):** alopregnanolona vem da progesterona (5α-redutase/3α-HSD), mesma via
   esteroidogênica do cortisol; glicocorticoides alteram subunidades GABA-A e homeostase de Cl⁻.
5. **B5↔B12 (trauma/TEPT):** extinção do medo é NMDA-dependente (amígdala/vmPFC); D-cicloserina;
   homeostase KCC2/NKCC1 [G1].
6. **B5↔B13 (endocanabinoide — o mais fechado mecanisticamente):** CB1 retrógrado media DSI/DSE,
   ajustando E/I em tempo real.
7. **B5↔B14 (neuroesteroides/hormônios):** alopregnanolona/brexanolone/zuranolona em GABA-A.
8. **B5↔B6/B9 (oxidativo/mitocôndria):** excitotoxicidade por sobrecarga de Ca²⁺ mitocondrial;
   estresse oxidativo prejudica GAD65/67 e EAAT.
9. **B5↔B7 (disbiose):** algumas cepas produzem GABA no lúmen; via vagal proposta (`[EXT]`).
10. **B5↔B10 (sono/circadiano):** oscilações E/I e homeostase do sono.

`[REF_MODULO_06: Homayoun 2007 PMID 17959792; Moda-Sava 2019 PMID 30975859; Shao 2021 PMID 34228959; Meltzer-Brody 2018 PMID 30177236; Davis/Ressler 2006 PMID 16919524]`

---

## MÓDULO 07 — SUBTIPOS E FENÓTIPOS CLÍNICOS DOCUMENTADOS

1. **Subtipo "hipoinibido" (déficit GABAérgico predominante):** ansiedade/hipervigilância,
   hiperreatividade amigdaliana, GABA cortical baixo; responde a ansiolíticos GABAérgicos agudos
   (subtipo α2/α3) e a estratégias de extinção.
2. **Subtipo "hiperexcitável/conectividade" (glutamato predominante):** TOC (circuito
   cortico-estriatal; Pittenger 2011), subgrupo de depressão com anedonia/rigidez; candidato a
   cetamina/ação rápida.
3. **Depressão pós-parto (neuroesteroide):** queda de alopregnanolona; responde a brexanolone/
   zuranolona (Meltzer-Brody 2018; Deligiannidis 2023).
4. **Depressão resistente / não respondedor monoaminérgico:** cetamina/esketamina (Zarate 2006;
   Berman 2000) — mecanismo glutamatérgico; controle ativo midazolam (Wilkinson 2019).
5. **Ansiedade/TEPT/fobias (extinção):** D-cicloserina como potencializador de exposição (Davis/
   Ressler 2006; Rosenfield 2019); benzodiazepínicos no alívio agudo (não na extinção de fundo).
6. **Intervenções (descritas, NÃO prescritas):** benzodiazepínicos (subtipo α), cetamina/esketamina,
   brexanolone/zuranolona, riluzole (Sanacora 2007), D-cicloserina+exposição, psicodélicos
   (5-HT2A), rTMS/ECT (indutores glutamatérgicos/plásticos); **falhas**: memantina, AMPAkinas.

`[REF_MODULO_07: Zarate 2006 PMID 16894061; Meltzer-Brody 2018 PMID 30177236; Deligiannidis 2023 PMID 37491938; Pittenger 2011 PMID 21963369; Davis/Ressler 2006 PMID 16919524; Wilkinson 2019 PMID 30653192]`

---

## MÓDULO 08 — CONTROVÉRSIAS, HETEROGENEIDADE E LACUNAS

1. **Mecanismo da cetamina:** NMDA como gatilho (Homayoun) vs HNK independente de NMDAR (Zanos,
   disputado) vs habeˆnula; não fechado.
2. **Cegamento/efeito:** dissociação rompe o cego; cetamina vs midazolam reduz (mas não elimina) a
   diferença (Wilkinson 2019).
3. **E/I heterogêneo:** MRS mostra glutamato/GABA para os dois lados conforme região/estado/medicação.
4. **Neuroesteroides:** aprovação restrita ao pós-parto; generalização para TDM não provada.
5. **mGluR2/3 e "benzodiazepínico sem sedação" (TPA023):** décadas de pré-clínica, tradução clínica mista.
6. **Interneurônios SST/PV:** causalidade humana não fechada (pós-morte/roedor `[EXT]`).
7. **Gap de ansiedade por transtorno:** TOC mapeado (Pittenger); TAG/pânico/fobia/TEPT por circuito
   ainda rasos.
8. **Lacuna de PMID:** Rudolph 1999, Ressler 2004, Yang 2018, Zorumski 2016, KCC2/NKCC1, GABA-B/
   humor, esketamina spray seguem `[G1]`.
9. **Insumos externos não confiáveis:** 6/6 PMIDs trocados (Gemini) e referências fabricadas
   (Consensus) — reforça a regra de chave=PMID.

`[REF_MODULO_08: Zanos 2016 PMID 27144355; Wilkinson 2019 PMID 30653192; Schür 2016 PMID 27145016; Deligiannidis 2021 PMID 34190962; Feyissa 2010 PMID 19945495]`

---

## MÓDULO 09 — CHECKLIST DE VERIFICAÇÃO CRUZADA COM O PROMPT 4.0

- [x] Demarcação humano/pré-clínico (`[ML]/[EC]/[EXT]/[EMERGENTE]`).
- [x] Inventário negativo presente (MÓDULO 02): memantina, AMPAkina, benzo como antidepressivo,
      pregabalina, neuroesteroide generalizado, "glutamato alto/GABA baixo" simples.
- [x] Controvérsia explícita (HNK/NMDA, midazolam, neuroesteroide restrito) no MÓDULO 08.
- [x] Crosstalk nomeado por ID (B1/B2/B3/B4/B6-9/B7/B10/B12/B13/B14) no MÓDULO 06.
- [x] Confundidores de biomarcador (MRS Glx, benzodiazepínico/"inibição artificial", PET,
      pós-morte, ciclo/gestação) — briefing §3.
- [x] Intervenções descritas sem prescrever (MÓDULO 07).
- [ ] **Pendente da Rodada 2:** G2/G3; resolução dos `[G1]`; mapa de ansiedade por transtorno;
      chave primária = PMID; zero rótulo órfão.

`[REF_MODULO_09: verificações estruturais do Prompt 4.0; curadoria G2/G3 na Rodada 2]`

---

## MÓDULO 10 — OBSERVAÇÕES EM OUTRAS CONDIÇÕES

> **Nota de natureza:** os itens abaixo são **amostra ilustrativa** de onde o balanço E/I também
> comparece, para orientar cruzamento do motor — **não constituem triagem completa** nem mecanismo
> compartilhado provado.

- **Epilepsia:** E/I desequilibrado por excelência; EAAT/GABA-A (modelo, não humor).
- **Esquizofrenia:** hipofunção NMDA/interneurônio PV; referência histórica da cetamina.
- **TOC:** hiperatividade cortico-estriatal glutamatérgica (Pittenger 2011).
- **TEPT/fobias:** extinção, homeostase de cloreto, D-cicloserina.
- **Dor crônica/neuralgia:** gabapentinoides (α2δ); modulação glutamatérgica.
- **Insônia:** GABA-A (fármacos Z), homeostase do sono.
- **Doenças neurodegenerativas/ELA:** EAAT2/GLT-1 (contexto distinto do humor).

`[REF_MODULO_10: amostra ilustrativa; Pittenger 2011 PMID 21963369; Schür 2016 PMID 27145016]`
