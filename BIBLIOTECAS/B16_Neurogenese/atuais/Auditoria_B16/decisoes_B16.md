# DECISÕES EDITORIAIS — B16 (Neurogênese hipocampal adulta)

## 1. Escopo e fontes
- GPM B16 completo (gate de completude: 11 Módulos 00–10) + Briefing Rodada 0 consolidado
  (298 âncoras validadas; 289 citadas nas tabelas A–N + notas).
- Extração por script das tabelas A–N: **288 PMIDs únicos** (289º = 26758842, off-scope
  SVZ/bulbo olfatório, retido apenas em nota do Briefing — não entra).
- **G1 eutils: 288/288 resolvem no PubMed**. Zero PMID inventado.
- **Zero ruído excluído das tabelas**: diferente de B14/B15, o Briefing B16 já filtrou os 136
  off-topic na caça; fármacos/compostos permanecem como **sinal experimental** (desenho
  oficial do GPM, blocos G/N/J), nunca como prescrição (P20).
- Não-fundidos (registro de transparência, não elegíveis como âncora): 2 anais EWA
  ("Theoretical and Natural Science", não indexado), 2 resumos de congresso IJNPP
  (Boldrini 2025; Ueda 2025), 1 revisão em venue não indexado (Loumpourdi 2026), 1 off-scope
  (Siopi 2016, bulbo olfatório).

## 2. Correções de autoria (1º autor real PubMed; briefing citava autor sênior/errado)
- 31165247: Park SC 2019 (briefing: "Bortolotto") — alias BORTOLOTTO.
- 30236533: Micheli L 2018 (briefing: "Banasr") — alias BANASR.
- 29941977: Huckleberry KA 2018 (briefing: "Jin") — alias JIN_MEDO.
- 31310776: Yamada J 2019 (briefing: "Ardalan") — consistente com GPM ("Yamada 2019 — ventral").
- 27106168: Clarke M 2017 (briefing: "Ardalan").
- 30622299: Takamiya A 2019 (briefing: "Dukart").
- 30414016: Gheorghe A 2019 (briefing: "Barha").
- Rótulos genéricos do briefing resolvidos por 1º autor PubMed: Wang P 2020 (adiponectina),
  Nuninga 2020b (7T/ECT), Jorgensen 2016, Mikolas 2019, Sierra 2011, Ramírez-Rodríguez 2020
  (melatonina), Brydges 2018, Ferreira FF 2018, Scarante 2017, Lee SY 2025 (KBN2202).

## 3. Pré-prints bioRxiv (emergentes; resolvem no PubMed mas NÃO fecham claim)
- 37790349 (Agrimi 2023, ERβ/violência) — versão publicada já fundida: 39228787 (iScience 2024).
- 38352378 (Chang 2024 pré-neurogênese/separação) — versão publicada: 39830600
  (*Biol Psychiatry Glob Open Sci* 2025).

## 4. Decisões de conteúdo (ciência)
- **Regra temporal** como espinha dorsal (semanas ≠ horas; rápido=atividade de imaturos,
  sustentado=↓BMP→nova linhagem; Ma 2017/Rawat 2024) — regra anti-nivelamento contra a
  conflação "psicoplastógeno reinicia neurogênese".
- **Controvérsia humana mantida VIVA e método-dependente** (Sorrells vs. Boldrini/
  Moreno-Jiménez; 2025–2026 reabre, não fecha). Formulação canônica adotada do Briefing.
- **Exigência de neurogênese por antidepressivos declarada CONTESTADA** (Santarelli vs.
  Holick/David/Surget/Zou) — versão não resolvida.
- **Curva em U** (Fuss 2010) e **dualidade dorsoventral** como freios anti-"mais=melhor".
- **Hierarquia: depressão (âncora humana molecular 2026 — B/mecanístico-translacional) >
  ansiedade (causalidade animal; lastro humano indireto — C/frontier)**. Não nivelado.
- Inventário negativo com 11 itens (3.2). Volume/BDNF/sangue ≠ neurogênese (5.2/5.3).
- B16↔B11 (tireoide): **lacuna honesta [G1]** — sem âncora cravada; não inventado.
- Exames: nenhum lê a ZSG; IDs oficiais apenas como contexto sistêmico (5.4); marcador de
  neurogênese "ainda não catalogado" (P19/P20).

## 5. Pipeline e verificações
- Classificação evid_role: 147 preclinical_mechanistic [ML] | 96 review [OB] | 45
  human_clinical [EC] (total 288). Primatas tratados como pré-clínico (Gould 1998; Perera
  2011); revisões sistemáticas de primatas (Elliott 2025) como OB.
- Colisões de rótulo resolvidas por sufixo: ANACKER_2013/2013b, LI_2022/b/c, LUCASSEN_2020/b,
  MA_2017/b, NUNINGA_2020/b, SAHAY_2011/b.
- **Bug corrigido no build**: `revista_ano` capturava o ano impresso no nome do periódico
  (ex.: *Cerebral Cortex (…: 1991)*) e o retrocompat gerava REF_*_1991 — corrigido por
  remoção de parênteses com ano do nome do journal; pipeline reexecutado do zero.
- Vínculos N2: 288 (trecho_ancora = listra literal; natureza/maturidade/tier por evid_role).
- Retrocompat: 288 refs | 288 ledger | 288 APROVADO | 288 listra | **0 fallback**.
- Gate P-5: APROVADO. Framework: ver rodada final. Checklist: ver rodada final.
- **P-6 (2ª verificação cega de claims de alto risco): PENDENTE** — não autocertificável;
  claims de alto risco: existência/magnitude da AHN humana (controvérsia), Peng 2026
  (processo interrompido na TDM), regra temporal da cetamina, curva em U, exigência
  contestada de neurogênese, volume≠neurogênese.

---

# RODADA [AT 2026-09-09] — DECISÃO: V2 COM FUSÃO DIRIGIDA (288 → 290)

## A. Resultado da reconferência ref a ref (todos os insumos × canônica vigente)
- **Universo numérico (8 dígitos): 285** — 283 vigentes confirmados; 1 off-scope OFICIAL
  (Siopi 2016, *J Neurosci* — decisão explícita do próprio insumo: ZSV/bulbo olfatório fora do
  escopo ZSG/giro denteado; registrado sem fundição); 2 eram **fragmentos de DOI** lidos por
  extração numérica como se fossem PMID (Palmer 2000; Fares 2018 — obras reais, já triadas como
  contexto/redundância na rodada 0).
- **Checagem autor-ano × anexo DOI × matriz externa (17 seções) detectou FALHA SILENCIOSA da
  rodada 0:** duas obras demandadas nos dois insumos (Tier 1 e Tier 2) nunca haviam sido
  carregadas. **ENTRA 2**, só após G1 (esearch por DOI → esummary → efetch com abstract lido):
  - **REF_DOLUDDA_2026** (consenso de 17 líderes do campo, *Cell Stem Cell* 2026) — âncora-teto da
    controvérsia humana e das revisões de campo; prosa §1.2 + CONTROVÉRSIAS (1).
  - **REF_ZHOU_2025** (*Molecular Psychiatry* 2025) — resiliência pós-parto mediada por AHN em
    fêmeas lactantes; **ancora a lacuna [G1] de pós-parto/sexo** (evidência ainda pré-clínica);
    prosa §11.2 + CONTROVÉRSIAS (8).
- **Identificadores falsos expostos, NÃO fundidos:** 2 fragmentos de DOI (acima) + 2 da matriz
  externa ("Allen 2025" e "Zhou 2024") que **não resolvem em esummary** — exposição registrada no
  manifesto; sem [G1] elegível. Regra: sem fonte verificável não entra, nem como citação formal.
- **Ratificadas:** exclusões da matriz externa (Zhang 2017 APP/PS1 — EXC/Alzheimer; Nejad 2024 —
  morfina; Li 2024 — B3; "W. 2025" — venue/conceito duplicado; Yang 2025 e Wang 2025 — anais não
  indexados, permanecem nota sem citação); duplicata consecutiva do anexo (Jones–Zhou–Jhaveri
  2022) colapsada na ocorrência única vigente; divergências de ano online×print resolvidas por DOI
  (Gage 2024→2025; Zhang IL-4 2020→2021; Elliott 2024→2025; Simard 2023→pré-print de 2024) —
  mesma obra, nenhuma nova inserção.

## B. Reparos técnicos da rodada
- 46 vínculos + 46 entradas de ledger reancorados às listras atualizadas de §1.2 e §11.2
  (divergência apontada pelo framework — 0 restos).
- `origem_entrada` das 2 novas entradas = LISTA_CANONICA (vocabulário controlado do framework;
  proveniência detalhada em verificacao.query_utilizada/manifesto/trilha).
- V1 arquivada em producao/historico/v1_canonica_2026-09-09.md.

## C. Portões oficiais (pós-fusão, estado final)
- gate_script (P-5): **APROVADO** (refs 290 | vínculos 290).
- framework validar_auditoria: **0 ERRO** (290 avisos não-bloqueantes de citacao_literal — padrão
  legado documentado em B14/B15/B16).
- checklist_entrega: **41/41**.

## D. Pendências
- **P-6 (Via 2 — 2ª verificação cega): PENDENTE** para o fecho 16/16, cobrindo também as 2 âncoras
  fundidas nesta rodada. Claims de alto risco atualizados: + consenso 2026 (Doludda) como
  formulação-teto; + resiliência pós-parto mediada por AHN (Zhou 2025, [ML]).
