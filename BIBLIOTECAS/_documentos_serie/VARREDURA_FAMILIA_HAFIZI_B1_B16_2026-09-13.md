# VARREDURA FAMÍLIA HAFIZI — B01–B16 (2026-09-13)

Causa-raiz AUD-038/V-05: ano extraído do NOME NLM do periódico `Revista (Local : AAAA) (AAAA)`
contaminando o ano do ID interno. Script read-only; correções exigem rito (backup+trilha+nota+CHANGELOG).

## Placar agregado

- fichas analisadas (Módulo 09, 16 bibliotecas): **2689**
- (a) com ano no nome da revista: **5**
- (b) ano-do-ID ≠ ano-de-publicação: **3**
- (c) família-Hafizi nominal (ID bate com o ano do NOME): **0**
- sem ano parseável no ID: 0 · sem ano de publicação detectável: 3

## B01_Neuroinflamacao — 236 fichas | (a) 1 · (b) 0 · (c) 0

  - `REF_HAFIZI_2007` (01_pmids.json) id=2007 pub=2007 nome=[2005] PMID 17639827 — «British journal of hospital medicine (London, England : 2005) (2007)»

## B02_Eixo_HPA_cortisol — 213 fichas | (a) 0 · (b) 0 · (c) 0


## B03_Neuroplasticidade — 165 fichas | (a) 0 · (b) 0 · (c) 0


## B04_Monoaminas — 131 fichas | (a) 0 · (b) 0 · (c) 0


## B05_GabaGlutamato — 160 fichas | (a) 1 · (b) 0 · (c) 0

  - `REF_DU_2023` (01_pmids.json) id=2023 pub=2023 nome=[2020] PMID 37101797 — «MedComm (2020) 2023»

## B06_EstresseOxidativo — 108 fichas | (a) 0 · (b) 0 · (c) 0 · s/ano-ID 0 · s/ano-pub 3


## B07_EixoIntestinoCerebro — 116 fichas | (a) 0 · (b) 0 · (c) 0


## B08_Micronutrientes — 145 fichas | (a) 1 · (b) 0 · (c) 0

  - `REF_TONIOLO_2018` (03_ensaios_clinicos.json) id=2018 pub=2018 nome=[1996] PMID 29177955 — «Journal of neural transmission (Vienna, Austria : 1996) (2018)»

## B09_DisfuncaoMitocondrial — 111 fichas | (a) 0 · (b) 2 · (c) 0

  - `REF_GEBARA_2020` (01_pmids.json) id=2020 pub=2021 PMID 33583561 — «Biological psychiatry (2021)»
  - `REF_SCAINI_2021` (01_pmids.json) id=2021 pub=2022 PMID 34650203 — «Molecular psychiatry (2022)»

## B10_DesregulacaoCircadiana — 137 fichas | (a) 0 · (b) 0 · (c) 0


## B11_DisfuncaoTireoidiana — 96 fichas | (a) 1 · (b) 0 · (c) 0

  - `REF_MAYERL_2022` (01_pmids.json) id=2022 pub=2022 nome=[1991] PMID 34339499 — «Cerebral cortex (New York, N.Y. : 1991) (2022)»

## B12_NeurobiologiaTrauma — 111 fichas | (a) 0 · (b) 0 · (c) 0


## B13_SistemaEndocanabinoide — 207 fichas | (a) 1 · (b) 0 · (c) 0

  - `REF_SAITO_2010` (01_pmids.json) id=2010 pub=2010 nome=[1999] PMID 20512266 — «Revista brasileira de psiquiatria (Sao Paulo, Brazil : 1999) (2010)»

## B14_Neuroesteroides — 290 fichas | (a) 0 · (b) 1 · (c) 0

  - `REF_SCHWEIZERSCHUBERT_2021` (01_pmids.json) id=2021 pub=2020 PMID 33585496 — «Front Med (Lausanne) (2020)»

## B15_AutofagiaMTOR — 173 fichas | (a) 0 · (b) 0 · (c) 0


## B16_Neurogenese — 290 fichas | (a) 0 · (b) 0 · (c) 0


---

## DESFECHO (2026-09-13, mesma rodada)

1. **B13 Saito — CASO NOMINAL RESOLVIDO.** `REF_SAITO_1999 → REF_SAITO_2010` aplicado com rito completo
   (backups ×5 `.bak_saito_2026-09-13`; 2 substituições ficha, 43 vínculos, 43 ledger, 1 token na canônica;
   manifesto com entrada datada; trilha `B13.../producao/01_rename_saito_1999_2010_2026-09-13.json`).
   Verificação eutils 2026-09-13: pubdate *2010 May*, PMID 20512266. B13 re-validada: gate APROVADO,
   framework 0 ERRO, censo série 32/32 BLOQ 0. **A varredura acima já roda PÓS-correção: (c) = 0.**
2. **3 divergentes residuais = dívida nomeada D-SERIE-CONVENCAO-ANO-ID (epub × print):**
   - B09 `REF_GEBARA_2020` (PMID 33583561): epub 2020-12-08 × print 2021-06-01 — revista_ano=(2021)
   - B09 `REF_SCAINI_2021` (PMID 34650203): epub 2021-10-14 × print 2022-02 — revista_ano=(2022)
   - B14 `REF_SCHWEIZERSHUBERT_2021` (PMID 33585496): epub 2021-01-18 × volume 2020 — revista_ano=(2020)
   Factos eutils verificados 2026-09-13. NÃO são erro factual como Saito/Hafizi (o ano do ID corresponde
   a uma data real de publicação — o epub). Renomear exige tocar PROSA citacional ("(Gebara 2020)" ×4+[EC listras]
   em 3 bibliotecas) e decidir a convenção da série. **Recomendação da casa: adotar pubdate-ano NLM**
   (coerente com revista_ano e com a citação padrão PubMed) e replicar o rito da trilha 17 / B13-Saito.
   Decisão do autor científico.
3. **B05 `REF_DU_2023`** era falso-divergente do parser v1 (formato "MedComm (2020) 2023"); eutils confirma
   pubdate 2023 — ID correto. Parser rev.2 cobre os 3 formatos conviventes da série.
4. **3 fichas (B06) sem ano localizável no campo revista_ano** (formato sem parênteses e sem ano solto) —
   risco Hafizi nelas exige enriquecimento via eutils ficha-a-ficha (trabalho nomeado, fora do escopo
   desta rodada; sem sinal de contágio nas 2.686 varridas com ano).
5. **Descoberta arquitetural anexa:** primeira execução do P-8 fora da B1 — B13 = 167 ERRO V-02
   (âncoras em linha-lote; perfil idêntico ao que a B1 tinha antes das reancoragens) + 1 V-09 + V-13
   (manifesto sem sha vigente). Confirma a trilha da Parte IV do auditor: o portão generaliza, e as demais
   15 precisam do mesmo ciclo de reancoragem. Patch defensivo aplicado no validador (corte_literatura
   string × dict) com nota datada no cabeçalho do script.
