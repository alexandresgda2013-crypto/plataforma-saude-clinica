# RELATÓRIO DE AUDITORIA DO INSUMO B6 — ESTRESSE OXIDATIVO (eixo B6-vitamina → transsulfuração → GSH)
**Data:** 2026-09-08 · **Auditor:** assistente (pipeline P-7 oficial) · **Status:** auditoria concluída — **aguardando decisão do usuário sobre aplicação**

---

## 1. Insumos recebidos (4 arquivos)

| Insumo | Papel | Veredito da auditoria |
|---|---|---|
| `Resumo do insumo para B6 Chatgpt.md` | Matriz canônica de triagem (13 claims B6.SM02.001–013 + 4 PMIDs de validação) | íntegro; 4/4 PMIDs validados (Cabrini 9844729 · Dalto 28245568 · Shen 19955400 · Wondrak 22116705) |
| `BRIEFING_B6_STRESS_OXIDATIVO_RODADA0.md` | Dossiê: 45 âncoras→PMIDs, NAO-IDX, não-citadas, pendências [G1] | tabela-mestra **45/45 confirmada** por esummary; 1 incongruência interna (contagem "93 refs" — anexo real tem **106** DOIs) |
| `GPM_B6_EstresseOxidativo.md` | GPM rodada 0 (M00–M10, 12 regras fundadoras, molde v2.0) | estrutura sólida; 2 âncoras que o briefing declarou "não localizadas" foram **resolvidas pela nossa auditoria** (ver §4) |
| `Artigos cientificos do mecanismo B6 Stress oxidativo.md` | 106 entradas compostas (autor/ano/título/DOI) | 106 DOIs todos parseados; zero duplicatas; zero erro de rótulo autor/ano |

## 2. Pipeline G1 (eutils) — números

- **106/106** entradas extraídas → esearch `DOI[aid]` → esummary → efetch (abstracts guardados em `matriz_b6_g1.json`).
- **95 resolvidas** por DOI · **11 falhas iniciais** → resgate dirigido por título/autor: **1 resgatada** (Kéry & Kraus 1994 = **7929220**; o DOI CrossRef do anexo não está registrado no PubMed — falha do briefing, sanada aqui) → **NAO-IDX finais = 10**.
- **+2 âncoras fora do anexo** citadas pelo GPM, verificadas por esummary direto: **Wondrak & Jacobson 2012 (22116705)** e **Kannan & Jain 2004 (14975445)** (1º autor real = Kannan K — correção de metadados do briefing "Jain/Kannan"→"Kannan & Jain" confirmada correta).
- **Universo novo auditado = 98 PMIDs**.
- **Cruzamento com a V1 vigente (36 refs O&NS gerais): overlap = 0.** A leva é arquitetura nova (eixo B6-vitamin→TS→GSH), sem colisão com corpus vigente.
- **Abstracts lidos** antes de qualquer decisão (97/98 com abstract; 2 sem abstract no PubMed: Singh 2007 e Kannan 2004 → G3 por título/periódico/autor, padrão da série).

## 3. Falsos positivos e incongruências

- **Falsos positivos do insumo: 0** (diferente de B1=4 e B5=1). Cada DOI resolveu para o artigo declarado; divergências de autor/ano = **0/95**.
- **Incongruências internas expostas:**
  1. Briefing/GPM alegam "93 refs"; o anexo tem **106** (o próprio Resumo ChatGPT diz "106 artigos"). Auditoria prevalece: 106+2 = 108 itens brutos, 98 resolvidos.
  2. Briefing §5 declara Kéry 1994 "sem resolução" → **resolvida** (7929220).
  3. Briefing §4.3 declara "Ereño-Orbea não localizada → fora" → **está resolvida** por DOI (10.1073/pnas.1313683110 = **24043838**), com abstract íntegro.
  4. Gonzalez-Recio 2020 (eLS) é NAO-IDX e **não consta** no §5 do briefing (silêncio do insumo; registrado aqui).

## 4. Matriz de decisão ref a ref (98 decididas)

**ENTRA = 72** · **BAIXO = 10** · **EXC = 16** · NAO-IDX = 10 (não entram; expostas) · Resgate = 1 (já no ENTRA).

### ENTRA por grupo (72)

| Grupo | n | Conteúdo |
|---|---|---|
| **ENZ** — enzimologia/estrutura/regulação CBS·CGL·H₂S·PLP | 33 | Stipanuk ×2, Kéry (resgate), Kabil, Taoka ×2, Mosharov, Meier, Banerjee, Prudova, Singh ×2, Zhu, Ishii (Cth-KO), Aitken, Smith, Yadav, Casique, Ereño-Orbea, Gregory, Dalto, Sbodio, Wilson, Gould, Ciapaite, Rivero, Al-Sadeq, McFarlane, Conter-2025, Petrosino, Pajares, Chen-2006, **Xi 2025** (TS→GSH→ferroptose — elo direto com a V1) |
| **B6DEF** — deficiência/estado de B6 → redox (modelos) | 9 | Cabrini (âncora heterogeneidade), Mahfouz-2004, Lima (âncora paradoxo), Choi, Hsu, Danielyan, Todorović ×2, McGowan |
| **ANTIOX** — ação antioxidante direta (química/celular; [APENAS PRÉ-CLÍNICO]) | 11 | Wondrak, Hu (anti+pró-oxidante!), Jain&Lim, Kannan&Jain, Mahfouz-2009, Matxain ×2, Natera, Ngo (scavenger+risco pró-ox), Ramis, Zhou |
| **HUM** — humano dieta/estado B6 → fluxo TS/GSH/marcadores | 8 | Davis (âncora paradoxo), Lamers (âncora heterogeneidade), Shen (associativo), Pusceddu (associativo), Ford (¹H-MRS cerebral — ponte com a V1), Lai, Cheng, Van Den Eynde |
| **GSH** — biologia/método da glutationa (CONTEXT; regra 6: não gera claim de B6) | 8 | Averill-Bates, Giustarini ×2, Labarrere, Lapenna, Nuhu, Valgimigli, Schmitt |
| **HIP** — hipótese emergente | 1 | Kato 2026 (B6→Nrf2; selo NÃO-CONSOLIDADO/[G1]) |
| **NEG** — lição anti-extrapolação (âncoras da regra causal) | 2 | Bønaa 2006 (NORVIT, RCT 3749: Hcy↓ ≠ desfecho), Christen 2018 (WAFACS: biomarcadores inflamação/endotélio não alteraram) |

### BAIXO (10 — registradas, adiáveis)
Chen 2003 (Schiff derivada) · Lindschinger 2019 (piloto n=30) · Song 2009 (WAFACS-DM2; lição coberta) · Lizzo 2022 (GlyNAC sem B6) · Chen 2024 (GSH mitocondrial — fronteira B9) · Lu 2023 (RCT preliminar Hcy) · Liu 2025 (network meta Hcy) · Bajic 2022 (rev. IM/ICC) · Balakina 2021 (derivado B6NO) · D'Elia 2025 (narrativa CV).

### EXC (16 — fora de escopo permanente, expostas)
- **Doença-alvo excluída:** Chen 2021 (autismo) · Corona-Trejo 2023 (Parkinson — relevância neural reconhecida, mas Parkinson fora da série) · An 2019 (MeSH Alzheimer) · Olaso-González 2021 (MCI) · Li 2025 (trombose/CV) · Yin 2025 (DM2).
- **Não-mamífero:** Pilesi (Drosophila/Ras) · Havaux, Neugart, Hacham (plantas) · Ankisettypalli (micobactéria) · Devi (H. pylori) · Lee-2025 (S. aureus) · Matoba (Lactobacillus) · Conter-2020 (Toxoplasma — o GPM a citou como "NON-CANONICAL"; a série formaliza como EXC-registrada) · Tu 2018 (levedura).

### NAO-IDX (10 — não entram; honestidade [G1])
Dawood 2024 · González-Recio 2020 · İnceören 2023 · **Itoh 2024** (âncora neuronal do claim SM02.011 → fica [G1], sem inventor) · Lee 2019 · Li 2026 · Mendes 2017 · Serhiyenko 2025 · Shrayner 2025 · Velásquez 2019.

## 5. Regras que a leva imporá à V2 (herdadas da triagem/GPM — fixar em CONTROVÉRSIAS como **B6.R01–R09**)

1. **R01 (REGRA B6-STRESS-OXIDATIVO-01):** proibido inferir "B6 → ↓estresse oxidativo humano" a partir de (a) antioxidante in vitro, (b) GSH em animal, (c) PLP→CBS/CGL, (d) PLP↔marcador. Cada seta exige evidência própria.
2. **R02:** "B6 aumenta GSH" é claim proibido — efeito depende de tecido/modelo (Cabrini sem Δ no total; Davis/Lima paradoxo; Lamers taxa↔concentração divergem).
3. **R03:** revisão nunca vira ensaio causal (Dalto, Wondrak, Gregory).
4. **R04:** observacional nunca vira causalidade (Shen, Pusceddu = ASSOCIATIVO; âncora NEG Christen).
5. **R05:** Nrf2 = hipótese emergente [G1] (Kato), nunca mecanismo provado.
6. **R06:** CONTEXT de glutationa não gera claim de B6.
7. **R07:** não-mamífero = EXC-registrado (sem transferência direta).
8. **R08:** vitâmeros não-intercambiáveis (PM ≠ PN ≠ PL; Ramis, Van Den Eynde); B6 pode ser **pró-oxidante** in vitro (Hu, Ngo) — polaridade honesta.
9. **R09:** fronteiras mantidas — ROS mitocondrial→B9; neuroinflamação→B1 (cascata, nunca salto); cofatores Se/Zn/Cu/Mg→B8; neurotransmissores PLP-dependentes→B4.

## 6. Projeção da V2

- 36 vigentes + 72 [AT] = **108 refs**; palavras-alvo ~7.500→10.000+.
- Nova arquitetura de seções: eixo **B6-vitamina → transsulfuração (CBS/CGL) → cisteína → GSH/GPx → carga oxidativa**, com heterogeneidade (Cabrini/Davis/Lima/Lamers) como centro, ação antioxidante direta selada [APENAS PRÉ-CLÍNICO], observacional marcado ASSOCIATIVO, Nrf2 como hipótese, e o par Bønaa/Christen como trava anti-causal-invertida (mesma espinha da regra).
- Tríade 01_pmIds/vínculos/ledger + manifesto + trilha + decisoes_B6 + P-4 ADENDO — conforme protocolo das rodadas B1–B5.
- P-6 (2ª verificação cega) permanece registrada como pendente.

---
**Pronto para decisão do usuário.**
