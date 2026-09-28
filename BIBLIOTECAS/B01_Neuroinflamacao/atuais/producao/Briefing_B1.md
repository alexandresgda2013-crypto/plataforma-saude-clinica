# BRIEFING CONSOLIDADO B1 v2 — NEUROINFLAMAÇÃO EM ANSIEDADE E DEPRESSÃO

**Rodada 0 — Briefing de direcionamento único para a B1 v2 (expansão da canônica de depressão).**
Data: 2026-09-04 · Prompt de referência: **v4.2 — "Mecanismos de Ansiedade e Depressão"**.
Mecanismo: `mecanismo_B1_neuroinflamacao` (segue o mesmo ID; v2 amplia, não substitui o conceito).

> **O que este documento é:** a lista de caça consolidada da B1 v2. Não é biblioteca e não entra
> afirmação sem G1→G2→G3 (existência PubMed → elegibilidade/espécie → suporte/força), com selo.
> Ele integra TRÊS insumos:
> 1. **Profundidade molecular** — briefing do Gemini (18 eixos de mecanismo de ponta), usado como
>    *checklist do que procurar no miolo* (sem PMID próprio → cada alvo vira busca nossa).
> 2. **Ansiedade** — nosso mapa com **~85 PMIDs reais** (TAG, pânico, fobia social, TOC, TEPT) em
>    `rodada0_briefing/BRIEFING_B1_EXPANSAO_ANSIEDADE.md` + `_refs_brutas_ansiedade.txt`.
> 3. **Depressão** — já completa na canônica (154 PMIDs, blocos 00–12, fidelidade aprovada); a v2
>    **não refaz**, só adiciona os eixos novos e o trilho de ansiedade.

---

## 0. Tese-central da v2 (o que muda em relação à canônica)

A canônica atual é **depressão-centrada** e cobre o eixo clássico. A v2 precisa:

1. **Adicionar o trilho de ANSIEDADE** (TAG, pânico, fobia social, TOC, TEPT) — incluindo o achado
   contraintuitivo de **subgrupos com supressão/hipo-reatividade neuroimune** (PET TSPO/pós-morte no
   TEPT), paralelo ao hipocortisolismo da B2. "Inflamação alta" **não é universal**.
2. **Adicionar profundidade molecular nova** que a canônica só tangencia: **imunometabolismo**
   (succinato/HIF-1α/itaconato/IRG1, chaveamento glicolítico), **necroptose RIPK1–RIPK3–MLKL**,
   **hemicanais Cx43/panexinas**, **AQP4/polarização glinfática**, e o elo fino **IL-1R/p38 → TrkB/CREB/BDNF**.
3. **Elevar mecanismos que estavam rasos** a subseções com PMID: microgliopatia/senescência,
   dimorfismo sexual da topologia inflamatória (com cautela), itaconato como freio endógeno.
4. **Importar a tabela de confundidores de biomarcador** (IMC/adiposidade, horário de coleta,
   genótipo TSPO rs6971, fitoterápicos) — método para não aceitar falsas correlações.
5. Manter **toda** a disciplina de extrapolação: o que é animal/célula entra `[PRÉ-CLÍNICO]`/
   `[EXTRAPOLADO]`, o que é hipótese sedutora mas mista em humano entra `[EMERGENTE]`.

---

## 1. Nomenclatura e famílias moleculares — busca por nome específico

### 1a. Já coberto pela canônica (não repetir a busca, só referenciar)
Inflamassomas NLRP3/NLRP1/AIM2/NLRC4; GSDMD/GSDME; TLR4/2/3 (MyD88/TRIF, MD-2/CD14); RAGE/scavenger;
HMGB1 redox (dissulfeto); S100B dual/S100A8-A9; ATP/mtDNA; quinurenina IDO1/2/TDO2, KMO/QUIN vs KAT/KYNA;
DAM/TREM2/ApoE; priming microglial; astrócitos C3+/A1-A2; TNF TNFR1/TNFR2; IL-6 clássica vs trans (sIL-6R/gp130);
SPMs (resolvinas/protectinas/maresinas, GPR37/ALX-FPR2); BHE (claudina-5/pericitos); CCL2/CCR2/Ly6C/ICAM-1;
vago/NTS; OVLT/área postrema/PGE2; complemento C1q/C3/CR3; P2X7/MAMs; glinfática/linfáticos meníngeos; TSPO.

### 1b. Eixos NOVOS a aprofundar (do Gemini; cada um = busca PubMed dedicada)
- **Imunometabolismo da micróglia (o gap maior):**
  - chaveamento OXPHOS/β-oxidação → **glicólise aeróbica** (Warburg glial) sob ativação;
  - quebra do ciclo de Krebs → acúmulo de **succinato** → inibe PHD → estabiliza **HIF-1α** →
    sustenta NF-κB e impede retorno ao repouso;
  - **itaconato** (sintetizado por **IRG1/ACOD1** mitocondrial) como freio endógeno do NLRP3 e
    ativador de **Nrf2** — buscar se insuficiência de itaconato liga-se à cronificação.
- **Necroptose como morte lítica paralela à piroptose:** complexo **RIPK1–RIPK3–MLKL** (via TNFR1
  quando caspases inibidas); fosforilação de MLKL → poro de membrana → lise e liberação massiva de DAMPs.
- **Hemicanais e junções comunicantes astrocitárias:** **conexina-43 (Cx43/GJA1)** — fosforilação
  aberrante por citocinas (IFN-α/IL-6) fecha *gap junctions* (desliga a rede de distribuição de
  energia/glicose) e abre **hemicanais**, com vazamento de glutamato/ATP; **panexina-1 (Panx1)**.
- **Aquaporina-4 (AQP4):** polarização nos pés astrocitários dirige o fluxo glinfático;
  despolarização por neuroinflamação → acúmulo de citocinas/detritos/QUIN.
- **Elo B1→B3 fino:** IL-1R1/IRAK → **p38 MAPK** fosforila e inibe **TrkB** e a translocação de
  **CREB** → bloqueia indução de BDNF (hipótese de refratariedade a antidepressivo monoaminérgico).
- **Detalhe de receptor a confirmar:** TLR3 endossomal em neurônio hipocampal lendo dsRNA de dano
  (não viral); CRH extra-hipotalâmico fica na B2.

## 2. Termos de busca alternativos (variar conforme a tradição)

- Mecanismo: "immunometabolism", "microglial metabolic reprogramming", "succinate–HIF-1α inflammation",
  "itaconate/IRG1 anti-inflammatory", "aerobic glycolysis glia", "necroptosis/MLKL/RIPK3 neuroinflammation",
  "connexin-43 hemichannel astrocyte", "pannexin", "AQP4 glymphatic polarization", "pyroptosis vs necroptosis".
- Ansiedade: "anxiety disorders cytokines/meta-analysis", "fear conditioning microglia amygdala",
  "fear extinction inflammation", "PTSD neuroinflammation/PET TSPO", "OCD cytokines", "panic disorder IL-6/CRP",
  "social anxiety immune", "sickness behavior anxiety", "interferon anxiety".
- Depressão (já na canônica): "cytokine-induced depression", "low-grade inflammation", "microglial priming".
- Método/ruído: "TSPO rs6971 affinity", "BMI-adjusted CRP depression", "hair/cortisol e inflammatory diurnal".

## 3. Áreas adjacentes subexploradas — priorizar

- **Ansiedade como fenótipo próprio de circuito:** amígdala basolateral (BLA), extinção do medo,
  IL-18 local na amígdala, P2X7/Na⁺-K⁺-ATPase microglial, TET2/NLRP3 — com o alerta de que a
  **direção do NLRP3 na ansiedade não é monotônica** (a deficiência de NLRP3 também gera ansiedade: Komleva).
- **TEPT neuroimune suprimido:** o subtipo que mostra TSPO baixo/supressão pós-trauma (Bhatt 2020) —
  tratar como contra-padrão documentado, não como ruído.
- **Trilho infantil/adolescente:** transtornos internalizantes têm inflamação (Parsons 2021, Howe 2022).
- **Microgliopatia/senescência** como hipótese alternativa à "hiperativação" (distrofia/SASP, perda de
  suporte) — procurar lastro real em humor; maior parte é extrapolada de envelhecimento/neurodegeneração.
- **Dimorfismo sexual** (ver seção 6 — entra como EMERGENTE).

## 4. Crosstalk prioritário (BLOCO 08 da v2)

- **B1↔B2 (HPA):** resistência glicocorticoide — JNK/p38/IKK fosforilam o GR (Ser211/226), impedem
  dissociação de Hsp90/p23 e translocação; NF-κB/RELA fica desinibido. (Lado molecular fino novo;
  o lado endócrino vive na B2.)
- **B1↔B3 (plasticidade):** IL-1β/TNF suprimem BDNF/CREB/TrkB (detalhe p38 novo); complemento/poda.
- **B1↔B6/B9 (oxidativo/mitocôndria):** mtROS/mtDNA ativam NLRP3; NLRP3 inibe complexos I/III → loop;
  **imunometabolismo é a ponte nova** (succinato/itaconato são metabólitos-imunes).
- **B1↔B7 (disbiose):** LPS/TLR4, inflamassoma, C3 (mantido).
- **B1↔B13 (endocanabinoide):** CB2 microglial (gap já sinalizado na canônica).
- **B1↔B5 (GABA/glutamato):** hemicanais Cx43 liberando glutamato → excitotoxicidade (elo novo).

## 5. Polimorfismos / variantes a verificar na v2

- Manter os da canônica: **IL1B, TNF -308, IL6 -174, CRP, TLR4, NLRP3**.
- Adicionar/confirmar na varredura:
  - **FKBP5 rs1360780** (interação gene×trauma — já na canônica e na B2).
  - **TSPO rs6971** — afeta afinidade do ligante de PET (falso-negativo; é confundidor de imagem, não marcador de doença).
  - **TET2** (metilação/ativação NLRP3/IL-1β em ansiedade — Gao 2023, pré-clínico).
  - miR-146a (freio de IRAK1/TRAF6; a topologia sexual do Gemini cita via estradiol — verificar lastro).

## 6. Sinalizadores de extrapolação — o que NÃO entra como fato

- **Topologia sexual binária do Gemini** (mulheres=ínsula/interocepção/miR-146a/estradiol; homens=accumbens/
  dopamina/D2/anedonia): hipótese atraente mas a evidência humana é **mista**; entra como
  **[EMERGENTE]/[EXTRAPOLADO]**, nunca como fato estabelecido.
- **Microgliopatia como causa de depressão "que piora com imunossupressor"**: especulativo; lastro em
  neurodegeneração/envelhecimento → **[EXTRAPOLADO: animal/célula→humano]**.
- **Detalhes biofísicos** (poros de 10–14 nm, resíduos Ser exatos, números de maquinaria): só com PMID
  conferido; caso contrário `[PRÉ-CLÍNICO]`.
- **RACIONAL PRÉ-CLÍNICO ≠ FÁRMACO:** antagonistas de CRHR1 (da B2) e vários anti-inflamatórios têm
  tradução mista/fracassada — registrar como lição translacional, não como promessa.

## 7. Cobertura equilibrada (não subrepresentar)

1. O **lado suprimido/hipo-reativo** (TEPT) junto ao lado ativado.
2. **Imunometabolismo** (succinato/HIF/itaconato) — ainda raro em resumos de psiquiatria.
3. **Necroptose (MLKL)** ao lado de piroptose (GSDMD).
4. **Hemicanais Cx43/AQP4** (astrofisiologia da inflamação) além da micróglia.
5. **Ansiedade** por transtorno (não colapsar tudo em "estresse").
6. **Freios endógenos** (itaconato/Nrf2, SPMs, IL-10/TGF-β) — não só o lado pró-inflamatório.
7. **Fitoterápicos/polifenóis**: ceticismo metodológico (biodisponibilidade no SNC, viés de publicação
   positivo, superdosagem in vitro) — só entrar com ensaio humano de desfecho robusto.

---

## 8. Camada clínica de ANSIEDADE — evidência mapeada (resumo; detalhe no arquivo dedicado)

Mapa completo com PMID em `BRIEFING_B1_EXPANSAO_ANSIEDADE.md`. Âncoras a auditar:

| Tema | Autor-ano | PMID | Tipo |
|---|---|---|---|
| Inflamação ↔ ansiedade/estresse traumático/TOC | Renna, 2018 | 30199144 | Meta/revisão |
| Marcadores inflamatórios periféricos na ansiedade | Costello, 2019 | 31326932 | Meta-análise |
| **TEPT = supressão neuroimune (PET+pós-morte)** | Bhatt, 2020 | 32398677 | Estudo-chave (Nat Commun) |
| Marcadores no TEPT | Passos, 2015 | 26544749 | Meta (Lancet Psychiatry) |
| Aberrações imunes no TOC | Cosco, 2019 | 30382535 | Meta |
| Citocinas no pânico | Quagliato, 2018 | 29241050 | Revisão sistemática |
| Citocinas modulam circuitos da amígdala | Lee, 2025 | 40199321 | Revisão/experimento (Cell) |
| P2X7/Na⁺-K⁺-ATPase microglial → ansiedade | Huang, 2024 | 38395698 | Mecanístico (Immunity) |
| IL-18 local na amígdala basolateral | Kim TK, 2017 | 27590137 | ML |
| TET2/NLRP3 → ansiedade | Gao, 2023 | 38012545 | ML |
| Deficiência de NLRP3 → ansiedade (direção não monotônica) | Komleva, 2021 | 33358726 | ML |
| **Minociclina atenua memória de medo em humano** | Xia, 2024 | 38233395 | **RCT** |
| Mega-análise de imunomoduladores | Wittenberg, 2020 | 31427751 | Mega-análise RCT |
| Ômega-3 e ansiedade | Su, 2018 | 30646157 | Meta (JAMA Netw Open) |
| Quinurenina-imune na ansiedade | Kim YK, 2018 | 28901278 | Revisão |
| Microbiota na ansiedade/depressão | Simpson, 2021 | 33271426 | Revisão sistemática |
| Ansiedade internalizante pediátrica | Parsons, 2021 / Howe, 2022 | 33200498 / 35880170 | Meta |

## 9. Tabela de confundidores de biomarcador (importar para BLOCO 05/11; método anti-falso-positivo)

| Marcador / exame | Confundidor a controlar | Ação na busca |
|---|---|---|
| `exame_pcr_us` | IMC/adiposidade visceral (gordura secreta IL-6/TNF), infecção recente, tabaco, exercício | exigir ajuste de IMC; separar inflamação metabólica da neuroinflamação (sTNFR2/adiponectina) |
| `exame_il6` | pulsatilidade, meia-vida curta, horário da coleta | padronizar coleta matinal (7–9h) |
| `exame_tnfalpha` | adiposidade | ajuste de IMC |
| `exame_il1beta` | estabilidade plasmática baixa | cautela em baixo-grau |
| TSPO-PET | **genótipo rs6971** (baixa afinidade = falso-negativo) | exigir genotipagem nos estudos de imagem |
| `exame_razao_kyn_trp` | triptofano dietético agudo, insuficiência renal | controle de jejum/função renal |
| `exame_snps_inflamatorios` | é risco estático, não estado atual | não usar como marcador de estado |
| Fitoterápicos/polifenóis | viés de publicação, biodisponibilidade | só ensaio humano com desfecho mecanístico (TSPO/KYN-TRP) |

---

## 10. Estrutura-alvo da B1 v2 (blocos do Prompt v4.2)

Mantém os 13 blocos da canônica, com:
- **BLOCO 02/03 (vias/mediadores):** + imunometabolismo (succinato/HIF/itaconato), necroptose MLKL, hemicanais Cx43/panexina, AQP4, elo p38/TrkB.
- **BLOCO 04 (células):** + microgliopatia/senescência (com selo), AQP4 polarização.
- **BLOCO 05 (biomarcadores):** + tabela de confundidores; TSPO rs6971.
- **BLOCO 06 (tradução clínica):** adicionar subseções por transtorno de **ansiedade** (TAG, pânico,
  fobia social, TOC, TEPT), com direção das citocinas e o subtipo TEPT suprimido; ensaios
  (minociclina/medo, imunomoduladores, ômega-3) descritos SEM prescrever (P20).
- **BLOCO 11 (estratificação):** fenótipos de ansiedade (hipervigilância/ruminação/extinção
  prejudicada) e o eixo **ativado vs. suprimido** (paralelo ao hiper/hipo da B2).
- **BLOCO 12 (cenários):** adicionar cenário **TEPT** e cenário **ansiedade inflamatória**, além
  dos três de depressão já existentes.

## 11. Plano de execução

1. **Rodada 1 (GPM):** gerar miolo molecular dos eixos novos (imunometabolismo, necroptose, Cx43/AQP4,
   p38/TrkB) com espécie/força — usando o Gemini apenas como lista de alvos.
2. **Rodada 2 (corpus eutils):** buscar os ~85 PMIDs de ansiedade (lista bruta já salva) + os novos
   eixos; montar Módulo 9 (`Evidencias/`) no mesmo esquema da canônica (pmids/meta/RCT/vínculos).
3. **Rodada 3 (fidelidade):** rodar `check_fidelidade_b1` e `check_troca_nomes` (já validados) sobre
   a v2; selar `[VERIFICADO]/[PRÉ-CLÍNICO]/[EXTRAPOLADO]/[EMERGENTE]`; zero título em inglês na prosa;
   zero rótulo órfão.
4. Congelar a canônica atual como **B1 v1** e publicar a **B1 v2 (ansiedade + depressão + profundidade)**.

> **Decisão em aberto:** v2 como arquivo novo (B1_v2) preservando a v1 (recomendado, rastro limpo),
> ou expansão por incremento sobre o arquivo atual.
