# GPM_B4 — DEFICIÊNCIA DE MONOAMINAS EM ANSIEDADE E DEPRESSÃO
## Gerador de Profundidade Molecular — Rodada 1 (insumo para a Rodada 2/canônica)

Mecanismo: `mecanismo_B4_deficiencias_monoaminas` · Data: 2026-09-05 · Prompt: v4.2.
Base: `BRIEFING_B4_CONSOLIDADO_RODADA0` (fusão Arena + Claude/Gemini; ~31 PMIDs verificados G1).

---

## MÓDULO 00 — METADADOS E ESCOPO

- **ID canônico:** mecanismo_B4_deficiencias_monoaminas. **Natureza:** suporte à decisão — não diagnostica.
- **Escopo:** neuromodulação por **serotonina (5-HT), noradrenalina (NA) e dopamina (DA)** em
  ansiedade e depressão. É o mecanismo mais antigo e o mais contestado, nascido das hipóteses das catecolaminas (Schildkraut, 1965, PMID 5319766) e da serotonina (Coppen, 1967, PMID 4169954), e criticado por Lacasse & Leo (2005, PMID 16268734): cobre (i) a história da
  hipótese monoaminérgica, (ii) sua reformulação moderna como **gating/neuromodulação** (não "estoque"),
  e (iii) as camadas de fronteira (código temporal/microcircuitos, transcriptômica, outros moduladores).
- **Corte de conhecimento / busca em tempo real:** **busca ativa realizada em 2026-09-05** via
  E-utilities/PubMed. As ~31 âncoras da tabela-semente do briefing tiveram o **PMID verificado**
  (G1: existência + título/periódico/autor). A auditoria corrigiu 2 PMIDs trocados na v2
  (Vetulani: **170534**; Blier: **7940983**) e marcou ressalvo no Yano 2015 (5-HT entérica). Itens
  sem PMID (STAR*D, heterodímero 5-HT2A–mGlu2, TAAR1, TPH2, Marcinkiewcz, Okaty/von Ziegler scRNA,
  NPY/galanina, Salamone, CYP em resposta, TOC/pânico) seguem `[G1]` para a Rodada 2.
- **Selos:** `[ML]` roedor/célula; `[EC]` humano; `[OB]` revisão; `[MA]` meta; `[EXT]` extrapolado;
  `[EMERGENTE]` evidência humana mista. G2/G3 (espécie/força) é curadoria da Rodada 2.
- **Fronteira editorial:** receptor/fármaco (NMDA/AMPA/5-HT2A como alvo) na **B5**; estado de humor/
  neuromodulação/gating na **B4**; desfecho estrutural de sinapse (espinho) na **B3**.

`[REF_MODULO_00: briefing consolidado B4 (2026-09-05); política de selos herdada da B1]`

---

## MÓDULO 01 — MAPA EXAUSTIVO DE VIAS MOLECULARES

1. **Síntese:** triptofano → **TPH** (**TPH1** periférico vs **TPH2** neuronal) → 5-HT; tirosina →
   **tirosina hidroxilase (TH)** → L-DOPA → DA → **dopamina-β-hidroxilase (DβH)** → NA; descarboxilação
   por **AAAD/DDC**. Variantes loss-of-function de **TPH2** ligadas a humor (Zhang [G1]).
2. **Degradação:** **MAO-A/MAO-B** (atividade **elevada no cérebro na TDM por PET** — Meyer 2006,
   PMID 17088501) e **COMT** (**Val158Met**; quebra de DA/NE cortical).
3. **Transporte/recaptação:** **SERT/5-HTT (SLC6A4; polimorfismo 5-HTTLPR)**, **NET (SLC6A2)**,
   **DAT (SLC6A3)** — alvo de ISRS/IRSN/bupropiona e das medidas de ocupação em PET.
4. **Receptores 5-HT:** **5-HT1A** (auto-receptor somatodendrítico), **5-HT1B** (pré-sináptico),
   **5-HT2A** (agonismo alucinógeno/psicodélico; frontera B5/B3), **5-HT2C** (controle de DA;
   agomelatina/mirtazapina), **5-HT3** (emese), **5-HT4**, **5-HT6** e **5-HT7** (cognição/ânimo; o 5-HT7 é alvo antidepressivo em investigação). Adrenérgicos:
   **α2** (auto-receptor), **α1, β**. Dopaminérgicos: **D1-like vs D2-like** (auto D2/D3).
5. **Núcleos de origem:** 5-HT nos **núcleos da rafe**; NA no **locus coeruleus (LC)**; DA na **VTA/
   substância negra**, com projeções **mesolímbica** (NAc) e **mesocortical** (CPF) — sistemas de
   modulação difusa.
6. **Paradoxo temporal (latência):** a recaptação é bloqueada em **horas**, mas a resposta clínica
   leva **semanas**; a **dessensibilização do auto-receptor 5-HT1A** (Blier & de Montigny, 1994,
   PMID 7940983) e a **downregulation β-adrenérgica** (Vetulani & Sulser, 1975, PMID 170534) explicam
   a janela — e apontam para a plasticidade a jusante (B3).
7. **DA como código temporal (TEMA NOVO 1 — optogenética/microcircuitos):** o disparo **fásico
   (burst, milissegundos)** de subpopulações dopaminérgicas é, por si só, suficiente para o
   condicionamento comportamental (Tsai et al., 2009, *Science*, PMID 19389999); a DA codifica o
   **erro de predição de recompensa** (Schultz et al., 1997, PMID 9054347) e o **esforço/motivação**
   (não "anedonia = baixa DA"). A NA do **LC** também tem código distinto: estimulação **tônica vs
   burst** desloca as redes de forma diferente (Grimm et al., 2024, PMID 39284964). Tudo `[ML]/[EXT]`.
8. **Heterodimerização e receptores de aminas-traço:** heterodímeros como **5-HT2A–mGlu2** alteram a
   cascata independentemente da concentração na fenda (González-Maeso [G1]); **TAAR1** modula o tom
   pré-sináptico de DA/5-HT (Revel [G1]).
9. **Indução experimental (prova humana de gating):** **depleção aguda de triptofano (ATD)** e de
   catecolaminas (α-MPT/AMPT) rebaixam humor em **remitidos/vulneráveis, não em sadios** — sinal de
   que a monoamina é **permissiva/estado-dependente**, não causal linear (Ruhé et al., 2007,
   PMID 17389902; Harrison 2004, PMID 15107182; Homan 2015, PMID 25781231).

`[REF_MODULO_01: Meyer 2006 PMID 17088501; Blier 1994 PMID 7940983; Vetulani 1975 PMID 170534; Tsai 2009 PMID 19389999; Schultz 1997 PMID 9054347; Grimm 2024 PMID 39284964; Ruhé 2007 PMID 17389902]`

---

## MÓDULO 02 — MAPA EXAUSTIVO DE MEDIADORES MOLECULARES

1. **Serotonina (5-HT):** neuromodulador amplo de humor, ansiedade, compulsão e ruminação; da rafe.
2. **Noradrenalina (NA):** vigília/arousal, energia, resposta de estresse; do locus coeruleus (Morris
   et al., 2020, PMID 32954002).
3. **Dopamina (DA):** recompensa, esforço, saliência, erro de predição; da VTA/SN; BDNF na via
   mesolímbica media suscetibilidade no social defeat (Berton et al., 2006, PMID 16469931).
4. **Neuropeptídeos moduladores:** **NPY** e **galanina** regulam a liberação de monoaminas sob
   estresse crônico (crosstalk B2) [G1].
5. **Endocanabinoides (TEMA NOVO 3a):** **2-AG/anandamida → CB1** modulam recompensa e interagem com
   DA/NA em tempo real (Parsons & Hurd, 2015, PMID 26373473 — crosstalk B13).
6. **Opioides endógenos (TEMA NOVO 3b):** neurônios **μ-opioide na rafe dorsal** interfaceiam com 5-HT
   (Welsch et al., 2023, PMID 37393045); **dinorfina/κ-opioide** em circuito claustrum-córtex media
   resposta ao estresse (Wang et al., 2023, PMID 38036497; relevância a anedonia/estresse).
7. **Neuroesteroides (TEMA NOVO 3c):** **alopregnanolona** modula **GABA-A**; a síntese de
   neuroesteroide regula GABA-A no estresse reprodutivo (Maguire & Mody, 2007, PMID 17329412) e
   **brexanolone** (alopregnanolona IV) é aprovada na depressão pós-parto (Meltzer-Brody et al., 2018,
   PMID 30177236 — crosstalk B14).
8. **Enzimas/transportadores como mediadores:** MAO-A/B, COMT, SERT/NET/DAT, TPH2, DβH (ver MÓDULO 01).

### Inventário negativo (mediadores/hipóteses investigados SEM associação causal consistente)
- **"Baixa serotonina causa depressão"** (modelo de estoque): forma ingênua **falsificada** (Ruhé
  2007; Moncrieff 2022 em disputa) — entra como histórico, não mecanismo vigente.
- **5-HTTLPR/MAOA como marcador de risco/resposta:** a interação gene×estresse **não replicou** em
  meta grande (Risch 2009, PMID 19531786; Culverhouse 2018, PMID 29268203).
- **"Desequilíbrio químico"** como explicação popular: sem lastro mecanístico.
- **Inferência reversa fármaco→causa:** "antidepressivo funciona → faltava serotonina" (falácia da
  aspirina); a eficácia não prova o déficit.
- **5-HT/5-HIAA periférico (plaquetário/entérico) como espelho do SNC:** ~95% da 5-HT é periférica;
  Yano 2015 (PMID 25860609) é 5-HT **entérica**, não cerebral.
- **"Anedonia = baixa dopamina"** como frase simples: a DA é código fásico/esforço/erro de predição,
  não nível tônico baixo.
- **Precursores (5-HTP/triptofano/SAM-e) como "reposição de serotonina":** sem RCT robusto.
- **Fitoterápicos "serotoninérgicos":** biodisponibilidade/viés; só com desfecho clínico robusto.

`[REF_MODULO_02: Berton 2006 PMID 16469931; Morris 2020 PMID 32954002; Parsons 2015 PMID 26373473; Welsch 2023 PMID 37393045; Wang 2023 PMID 38036497; Meltzer-Brody 2018 PMID 30177236; Maguire 2007 PMID 17329412; Risch 2009 PMID 19531786]`

---

## MÓDULO 03 — MAPA EXAUSTIVO DE TIPOS CELULARES E ESTRUTURAS

1. **Neurônios serotoninérgicos da rafe** (dorsal/mediana): modulação difusa; subtipos moleculares
   distintos (mapeados por single-cell — Okaty [G1]).
2. **Neurônios noradrenérgicos do locus coeruleus:** tônico vs burst; moldam hipocampo sob estresse
   (Privitera et al., 2024, eLife, PMID 38477670); papel na ansiedade patológica (Morris 2020).
3. **Neurônios dopaminérgicos da VTA/substância negra:** subpopulações; projeções mesolímbica (NAc) e
   mesocortical; disparo fásico causal (Tsai 2009).
4. **Microcircuitos e subpopulações:** o efeito depende de **subpopulações minúsculas** e do padrão
   temporal, não do volume global de monoamina (Tsai 2009; Grimm 2024).
5. **Transcriptômica de célula única sob estresse (TEMA NOVO 2):** scRNA-seq revela **quais genes
   ligam/desligam em neurônios (e glia)** individuais sob estresse severo e a habituação
   transcriptômica a estresse repetido (Waag et al., 2025, PMID 41430076; astroglia hipocampal sob
   estresse — von Ziegler [G1]).
6. **Estruturas-alvo:** CPF/vmPFC (decisão/extinção), amígdala/BLA (ansiedade), NAc (recompensa),
   hipocampo (humor/memória) — todos modulados pelos três sistemas.
7. **Células periféricas:** enterocromafins intestinais (maior fonte de 5-HT do corpo; Yano 2015) e
   plaquetas (armazenam 5-HT) — relevantes ao confundidor de biomarcador, não ao SNC.

`[REF_MODULO_03: Tsai 2009 PMID 19389999; Grimm 2024 PMID 39284964; Privitera 2024 PMID 38477670; Waag 2025 PMID 41430076; Morris 2020 PMID 32954002; Yano 2015 PMID 25860609]`

---

## MÓDULO 04 — VARIABILIDADE GENÉTICA E EPIGENÉTICA EXAUSTIVA

1. **5-HTTLPR (SLC6A4/rs4795541):** achado inicial de interação com estresse (Caspi et al., 2003,
   PMID 12869766) e associação a traços de ansiedade (Lesch et al., 1996, PMID 8929413); **meta
   grande não replica a interação** (Risch 2009, PMID 19531786; Culverhouse 2018, PMID 29268203) —
   efeito pequeno, não marcador clínico.
2. **MAOA-uVNTR:** interação com maus-tratos/agressividade (Caspi et al., 2002, PMID 12161658); mesma
   ressalva de replicação/estratificação.
3. **TPH2 neuronal:** variantes/haplótipos de loss-of-function em TDM/borderline (Zhang; Canli [G1]).
4. **COMT Val158Met (rs4680):** degradação de DA pré-frontal; plausível, efeito clínico modesto.
5. **Farmacogenômica:** **CYP2D6 e CYP2C19** definem metabolizador lento/rápido e alteram
   biodisponibilidade/pseudorrefratariedade aos ISRS (avaliar em "resistente") [G1].
6. **Epigenética:** metilação/acetilação de promotores monoaminérgicos (e.g., SLC6A4) após trauma de
   infância, silenciando genes; interface com FKBP5 (B2/B12) e BDNF (B3) [G1].
7. Variantes de receptor (5-HT1A C-1019G, 5-HT2A/2C, NET, DAT) na resposta a fármaco — verificar força.

`[REF_MODULO_04: Caspi 2003 PMID 12869766; Lesch 1996 PMID 8929413; Risch 2009 PMID 19531786; Culverhouse 2018 PMID 29268203; Caspi 2002 PMID 12161658]`

---

## MÓDULO 05 — BIOMARCADORES EXAUSTIVOS

1. **PET de MAO-A:** atividade elevada na TDM (Meyer 2006, PMID 17088501); **confundidor: tabagismo
   reduz MAO-A** — excluir/estratificar fumantes.
2. **PET de transportadores (SERT/NET/DAT):** ocupação por fármaco; genótipo basal (5-HTTLPR) e tabaco
   (DAT) alteram a ligação; ocupação ≠ melhora clínica.
3. **Depleção aguda (ATD/AMPT):** teste de vulnerabilidade estado-dependente (Ruhé 2007, PMID
   17389902; Homan 2015, PMID 25781231); não rebaixa sadio.
4. **5-HIAA no LCR / 5-HT plaquetária:** marcadores periféricos com confundidores (dieta, ritmo, nível
   da punção, ativação plaquetária); não espelham o SNC.
5. **Triptofano/razão quinurenina:** o IDO inflamatório (B1) desvia triptofano da síntese de 5-HT.
6. **Farmacogenômica (CYP2D6/2C19):** covariável de resposta/metabolização, não marcador de estado.
7. **Sem marcador de "estoque cerebral de monoamina"** in vivo válido — toda afirmação de nível central
   é indireta.

`[REF_MODULO_05: Meyer 2006 PMID 17088501; Ruhé 2007 PMID 17389902; Homan 2015 PMID 25781231; Harrison 2004 PMID 15107182]`

---

## MÓDULO 06 — INTERCONEXÕES EXAUSTIVAS COM B1–B16

1. **B4↔B1 (neuroinflamação):** citocinas induzem **IDO1**, desviando triptofano da 5-HT para
   quinurenina/QUIN; inflamação prediz não-resposta a ISRS.
2. **B4↔B2 (HPA/estresse):** cortisol modula TPH e a atividade de MAO-A; **NPY e galanina** modulam a
   liberação de monoamina sob estresse; FKBP5/gene×ambiente.
3. **B4↔B3 (plasticidade — o elo central):** ISRS dependem de sinalização **BDNF/TrkB** intacta;
   Berton 2006 (BDNF na via DA mesolímbica, PMID 16469931); a monoamina **destrava a janela plástica**
   (dessensibilização de auto-receptor → neurogênese/BDNF, Santarelli na B3) e a experiência preenche.
4. **B4↔B5 (GABA/glutamato):** 5-HT2A modula glutamato pré-frontal; fronteira receptor (B5) vs humor (B4).
5. **B4↔B6/B9 (oxidativo/mitocôndria):** degradação por MAO gera H₂O₂/estresse oxidativo.
6. **B4↔B7 (intestino/cérebro):** microbiota regula a 5-HT do hospedeiro — **entérica/periférica**
   (Yano et al., 2015, PMID 25860609); a ponte ao SNC é indireta.
7. **B4↔B10 (circadiano/sono):** agomelatina (MT1/MT2 + 5-HT2C); ritmos modulam monoaminas.
8. **B4↔B12 (trauma/TEPT):** ansiedade/extinção, 5-HTT, farmacologia da exposição; epigenética.
9. **B4↔B13 (endocanabinóide):** eCB/CB1 modulam recompensa e interagem com DA/NA (Parsons 2015,
   PMID 26373473).
10. **B4↔Opioide (sistema próprio/cruzamento):** μ-opioide na rafe (Welsch 2023, PMID 37393045) e
    dinorfina/κ (Wang 2023, PMID 38036497) modulam 5-HT e estresse.
11. **B4↔B14 (neuroesteroides/hormônios):** alopregnanolona/GABA-A (Maguire 2007); brexanolone na
    depressão pós-parto (Meltzer-Brody 2018, PMID 30177236).
12. **B4↔B15/B16:** autofagia/mTOR e neurogênese como saída plástica do gating monoaminérgico.

`[REF_MODULO_06: Berton 2006 PMID 16469931; Yano 2015 PMID 25860609; Parsons 2015 PMID 26373473; Welsch 2023 PMID 37393045; Wang 2023 PMID 38036497; Meltzer-Brody 2018 PMID 30177236]`

---

## MÓDULO 07 — SUBTIPOS E FENÓTIPOS CLÍNICOS DOCUMENTADOS

1. **Subtipo respondedor monoaminérgico (depressão clássica):** melhora com ISRS/IRSN; efeito real mas
   modesto (Cipriani 2018, PMID 29477251), com viés de publicação (Turner 2008, PMID 18199864).
2. **Subtipo DA/anedonia/motivação (falha ao ISRS):** redução de esforço/recompensa, erro de predição;
   candidatos a alvos dopaminérgicos/glutamatérgicos (Berton 2006; DA fásica Tsai 2009) `[EXT]`.
3. **Subtipo ansiedade/TOC com farmacologia distinta:** TOC responde a ISRS em dose alta (sinal
   serotoninérgico próprio); pânico/TEPT ligados a LC/arousal e extinção (Morris 2020; Lesch 1996 —
   com cautela genética). Trilho por transtorno a abrir na Rodada 2.
4. **Depressão pós-parto (neuroesteroide):** alvo de alopregnanolona/brexanolone (Meltzer-Brody 2018)
   — subtipo com janela hormonal.
5. **Intervenções (descritas, NÃO prescritas):** ISRS/IRSN/ATC/IMAO; mirtazapina (α2/5-HT2C),
   bupropiona (DA/NE), buspirona (5-HT1A), agomelatina (MT/5-HT2C); brexanolone; e **outras portas
   que abrem a mesma janela plástica sem a via clássica** — cetamina/esketamina (B5/B3), psicodélicos
   (5-HT2A), rTMS/ECT.
6. **STAR*D:** remissão escalonada com citalopram (Trivedi 2006 [G1]) — taxa de resposta decrescente
   por etapa; não inferir mecanismo da resposta.

`[REF_MODULO_07: Cipriani 2018 PMID 29477251; Turner 2008 PMID 18199864; Berton 2006 PMID 16469931; Morris 2020 PMID 32954002; Meltzer-Brody 2018 PMID 30177236; Tsai 2009 PMID 19389999]`

---

## MÓDULO 08 — CONTROVÉRSIAS, HETEROGENEIDADE E LACUNAS

1. **A disputa da serotonina:** Moncrieff et al., 2022 (revisão guarda-chuva: sem evidência de
   serotonina baixa causal, PMID 35854107) vs a réplica metodológica Jauhar et al., 2023 (PMID
   37322065) — registrar como **disputa ativa**, não veredito.
2. **Refutação do modelo ingênuo:** depleção não rebaixa sadio (Ruhé 2007); latência agudo-vs-tardio;
   a hipótese de estoque caiu — mas a farmacologia funciona para um subconjunto.
3. **Viés de publicação e tamanho de efeito:** Turner 2008 (PMID 18199864); Cipriani 2018 (PMID
   29477251) — efeito agudo real porém modesto.
4. **Falha de replicação genética:** 5-HTTLPR/MAOA (Risch 2009; Culverhouse 2018) — lição de
   gene×ambiente; a "âncora genética da ansiedade" é frágil.
5. **Fármacos não-monoaminérgicos como contraprova:** cetamina, psicodélicos, rTMS/ECT, agomelatina
   funcionam sem elevar monoaminas da forma clássica — a janela plástica tem várias portas.
6. **Tradução temporal/espacial:** optogenética e scRNA são roedor/célula `[EXT]`; faltam equivalentes
   in vivo humanos do código temporal e da identidade transcriptômica.
7. **Outros moduladores são emergentes:** eCB/opioide/neuroesteroide interagem com monoaminas, mas o
   lastro direto em humor/ansiedade humana ainda é pequeno (exceto brexanolone).
8. **Gap de ansiedade por transtorno:** cobertura ainda concentrada em genética frágil; falta mapa
   TAG/pânico/fobia/TOC/TEPT por circuito.
9. **Lacuna de PMID:** STAR*D, heterodímero 5-HT2A–mGlu2, TAAR1, TPH2, NPY/galanina, scRNA da rafe/
   astroglia seguem `[G1]` até a Rodada 2.

`[REF_MODULO_08: Moncrieff 2022 PMID 35854107; Jauhar 2023 PMID 37322065; Ruhé 2007 PMID 17389902; Turner 2008 PMID 18199864; Cipriani 2018 PMID 29477251; Risch 2009 PMID 19531786]`

---

## MÓDULO 09 — CHECKLIST DE VERIFICAÇÃO CRUZADA COM O PROMPT 4.0

- [x] Demarcação humano/pré-clínico (`[ML]/[EC]/[EXT]/[EMERGENTE]`) em cada afirmação.
- [x] Inventário negativo presente (MÓDULO 02), incluindo a hipótese ingênua e a genética não-replicada.
- [x] Controvérsia explícita (Moncrieff vs Jauhar; viés; latência) no MÓDULO 08.
- [x] Crosstalk nomeado por ID (B1/B2/B3/B5/B6-9/B7/B10/B12/B13/opioide/B14) no MÓDULO 06.
- [x] Confundidores de biomarcador (tabaco/MAO-A, plaqueta, genótipo, CYP, depleção estado-dependente).
- [x] Intervenções descritas sem prescrever (MÓDULO 07).
- [x] Os três temas de fronteira cobertos: optogenética/microcircuitos (01/03), scRNA (03), outros
      moduladores eCB/opioide/neuroesteroide (02/06).
- [ ] **Pendente da Rodada 2:** G2/G3 de todas as âncoras; resolução dos `[G1]`; mapa de ansiedade por
      transtorno; zero rótulo órfão; chave primária = PMID.

`[REF_MODULO_09: verificações estruturais do Prompt 4.0; curadoria G2/G3 na Rodada 2]`

---

## MÓDULO 10 — OBSERVAÇÕES EM OUTRAS CONDIÇÕES

> **Nota de natureza:** os itens abaixo são **amostra ilustrativa** de onde a modulação
> monoaminérgica também comparece, para orientar cruzamento do motor — **não constituem triagem
> completa** nem afirmação de mecanismo compartilhado provado.

- **TOC:** resposta a ISRS em dose alta; sinal serotoninérgico distinto do da depressão.
- **Pânico/TEPT/fobias:** locus coeruleus/arousal e extinção (Morris 2020).
- **TDAH:** DA/NE (transportadores; metilfenidato/atomoxetina) — alvo de neuromodulação próximo.
- **Dor crônica:** vias descendentes serotoninérgicas/noradrenérgicas (antidepressivos como analgésicos).
- **Parkinson:** degeneração DA da substância negra (modelo de depleção real de DA, não depressivo).
- **Adição/recompensa:** DA mesolímbica, eCB, opioide endógeno (cruzamento com Tema 3).
- **Depressão pós-parto/Pré-menstrual:** neuroesteroides/GABA-A (B14; brexanolone).

`[REF_MODULO_10: amostra ilustrativa; Morris 2020 PMID 32954002; Meltzer-Brody 2018 PMID 30177236]`
