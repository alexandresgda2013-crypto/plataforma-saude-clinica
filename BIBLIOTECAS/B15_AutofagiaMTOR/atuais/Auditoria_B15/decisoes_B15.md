# Decisões de Auditoria — B15 Autofagia / mTOR

Data: 2026-09-08 · Prompt v4.2 · Pipeline v2.6 · Mecanismo: `mecanismo_B15_autofagia_mtor`

## G1 — Existência (eutils/PubMed)
- Briefing B15 declarou **140 âncoras em tabelas** (14 blocos A–N; 40 clusters C01–C40 +
  3 insumos externos auditados).
- Varredura eutils (esummary em lote, backoff): **140/140 PMIDs resolvem no PubMed** (0 sem
  resolução). O pré-print bioRxiv da espermidina (39677641, Mackert 2024) **resolveu** no
  PubMed como *bioRxiv* — mantido com marcação `[G1]/pré-print` e evidência emergente; o achado
  epidemiológico publicado (NHANES, Qi 2024) foi separado.
- Conferência autor+ano+tema: âncoras-teto confirmadas (Li 2010 *Science*, Autry 2011
  *Nature*, Yang 2025 *Nature* gatilho causal, Klionsky 2021 diretriz de fluxo, Gassen 2014
  FKBP51, He 2019/2023 Beclin/LC3A, Abdallah 2020 ECR rapamicina, Kato/Targum NV-5138,
  Mallet/Sandi 2026 urolitina A, Lyu 2022 NLRP3, Lu 2023 NIX). As sinalizações de "autor
  divergente" eram o Briefing usar autor sênior vs. 1º autor do PubMed (Abdallah/Zanos,
  Krystal/Monteggia, Duman/Scheuing, Licznerski) — usou-se o 1º autor real com alias do rótulo
  do Briefing.

## G2 — Elegibilidade (espécie/desenho)
- **134 âncoras mecanísticas** no `01_pmids.json`: 39 revisões/meta/diretriz [OB],
  21 humano/pós-morte/ECR [EC], 74 pré-clínico/animal/celular [ML].
- **6 PMIDs de ruído** excluídos do corpo (composto vegetal/suplemento/TCM/contexto
  metabólico, conforme o próprio Briefing): apigenina (31322238), α-tocoferol/vitamina E
  (29782858), Xiaoyaosan/TCM (35784760), quercetina (34082381), gálico/astragalina
  (40089077), obesidade high-fat como confundidor (34902357). Registrados em
  `producao/ruido_excluido.json` (status EXCLUIDO_RUIDO). BGP-15 (38677623) foi **mantido**
  como sinal de alvo mitofágico (fármaco co-indutor de chaperonas).

## G3 — Suporte / fidelidade
- Ledger: **134 entradas, todas APROVADO**, ancoradas em **listra literal** da canônica
  (prose 0 / listra 134 / fallback 0). Zero rótulo inexistente; zero id órfão.

## Regras canônicas aplicadas
- **P20/P19:** sem doses/prescrição/cortes; cetamina/rapamicina/everolimo/NV-5138/trealose/
  espermidina/urolitina/psilocibina/DBS/jejum entram como SINAL de alvo/plasticidade. Exames
  por ID oficial (`exame_*`); autofagia/mTOR não têm exame catalogado → pesquisa, sem corte.
- **R04:** dados animais/celulares marcados `[APENAS PRÉ-CLÍNICO]`/`[EXTRAPOLAÇÃO]`.
- **P16:** neurogênese adulta dependente de autofagia remetida a `mecanismo_B16_neurogenese`
  (B15 só registra modulação).
- **P12:** contrato de suporte de decisão; **P17:** 16 chaves de conexão; **R06:** camada
  semântica; **RAG:** zero PMID no texto corrido.
- Regras centrais preservadas: **fluxo** (não LC3); **bidirecionalidade regional**
  (suprimida no LHb/neurogênese/microglia vs. excessiva ansiogênica na amígdala/hipocampo
  ventral); **janela homeostática** (nem mTOR baixo nem autofagia alta crônica); contestação
  cetamina-mTOR (Li vs. Autry vs. norketamina; paradoxo da rapamicina); separação temporal
  horas(mTOR)/dias(autofagia); dimorfismo sexual; "autofagia ≠ detox"; evidência humana como
  elo crescente mas preliminar.
- Itens `[G1]` (espermidina clínica = pré-print bioRxiv; DISC1; Yamamoto; pós-morte de
  fluxo em suicidas; TREM2; GSK3/lítio×autofagia; ECRs de moduladores em ansiedade)
  **sem PMID inventado**, para G3 cego. Tamanhos de efeito são alegação a confirmar no G3.

## Pendência
- **P-6**: Fase 3 de Fidelidade Canônica (itens A/B/C/E) depende de **avaliador cego
  independente** — não autocertificado.

---

## Rodada [AT] 2026-09-09 — reconciliação de insumo externo (P-7) → V2

**Universo novo triado ref a ref ao vivo (eutils):** 145 PMIDs únicos (146 registros; Li 2023/vortioxetina vinha duplicada no insumo e foi colapsada) fora da V1 (31 âncoras do GPM + 125 leva N §6/documentações).

**Decisões** (matriz em producao/insumos/matriz_b15_decisao.json):
- ENTRA 39 → 31 âncoras §3 não vigentes + 8 §6 de núcleo mecanístico
- BAIXO 93 → leva N (ketamina-suporte B3, BDNF-suporte, HPA B2, mitocôndria B8, reviews/contexto NLRP3-B1, metodológicos)
- EXC 13 → CAMADA C (Alzheimer ×5, Parkinson, autismo, fragil-X, dor somática, esclerose)
- NAO-IDX 2 (mantidos fora)

**Exposições:** (i) "Pich & Millan 2018" = Cavalleri 2018 (Millan sênior); (ii) Deyama print 2020; (iii) Li-obesidade print 2022; (iv) Sun print 2022; (v) Zhang-S6K1 print 2024; (vi) Aguilar-Valles print 2021; (vii) Chandran print 2013; (viii) Alcocer-Gómez tem DOIS artigos 2017 (V1 / novo); (ix) Xu-2023a = comorbidade T2DM×CUMS; (x) aliases GPM↔V1: "Zhang 2023d"=REF_ZHANG_2023b · "Li 2026a"=REF_LI_2026 · "Li 2025"=REF_LI_2025b.

**[G1] resolvidos:** Su-[G1 insumo] = Peng 2025 (formononetina; REGISTRADA) · vortioxetina×mTORC1 (§4/7 cravada = REF_LI_2023). **[G1] mantidos honestos:** TFEB humano, marcador periférico de fluxo, mTORC2 além VTA, dor×depressão dedicada, envelhecimento/sexo em humano, pós-parto humano, Pich&Millan real, "Choe"/"Liu-BNIP3L" não resolvidos.
