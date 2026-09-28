# Auditoria Científica de Conteúdo — B8 (Deficiências de Micronutrientes)

**Data:** 2026-09-06 · **Sessão:** Rodada 2/3 (operador de geração; P-6 2ª verificação independente/avaliador cego PENDENTE).
**Objeto:** trechos-âncora da `B8 DEFICIENCIAS DE MICRONUTRIENTES V1 CANONICA.md` (7.414 palavras).
**Ferramentas:** G1 eutils (esearch+esummary+efetch), G2 elegibilidade/espécie, G3 suporte por abstract colado na sessão; `gate_script.py` (P-5) e `validar_auditoria.py` (framework).

## Contagem de decisões

- **G1:** {'VERIFIED_REFERENCE': 38}
- **G2:** {'ELIGIBLE_SOURCE': 36, 'NAO_APLICAVEL': 2}
- **G3:** {'APROVADO': 30, 'APROVADO_COM_RESSALVA': 8}
- **status_auditoria:** {'APROVADO': 30, 'APROVADO_COM_RESSALVA': 8}

## Decisões-chave (abstract colado nesta sessão)

1. **VITAL-DEP D3 (Okereke 2020):** RCT ~18 mil/5,3 anos, HR 0,97 (0,87–1,09), PHQ-8 Δ0,01 → prevenção **NULA** → APROVADO como âncora refutadora.
2. **VITAL-DEP ômega-3 (Okereke 2021):** HR 1,13 (1,01–1,26), humor NS → prevenção **NULA/não-benéfica** → APROVADO como refutador.
3. **B12 em não-deficientes (Markun 2021):** 16 RCTs/6.276, sem efeito em depressão/cognição/fadiga → APROVADO (âncora limitadora).
4. **Selênio (Sajjadi 2022):** soro sem diferença (I²=98%) → APROVADO; Johnson 2013 = exposição ambiental (água), não pílula (RESSALVA).
5. **Magnésio:** Rajizadeh 2017 (duplo-cego) positivo **só em hipomagnesêmicos** → APROVADO; Tarleton 2017 é **aberto/sem cegueira** → APROVADO_COM_RESSALVA; Sartori 2012 = roedor [APENAS PRÉ-CLÍNICO].
6. **Vitamina D:** Mikola 2023 g=−0,317, I²=88%, GRADE muito baixa; Ghaemi 2024 ansiedade SEM efeito → APROVADO_COM_RESSALVA (força menor que a associação Anglin).
7. **Mendelian randomization (Carnegie 2024; Fang 2025):** MR tradicional nulo; sinais sugestivos ferro/cobre/25OHD na recorrente; Se/Mg em excesso possivelmente adversos → APROVADO_COM_RESSALVA (MR≠RCT).
8. **MTHFR:** Gaysina 2008 nula vs Wu 2013/Rai 2017 positivas → heterogêneo; L-metilfolato (Papakostas) é adjuvante de subgrupo, não destino genético.
9. **Dieta:** SMILES (Jacka 2017) d=−1,16/remissão 32% vs 8%; Lassale 2019 dose-gradiente → APROVADO (lado forte do abismo alimento×pílula).

## Redirecionamentos / rebaixamentos
- Associação populacional clínica (elementos séricos, MR, estudos transversais) → linguagem de associação, nunca causal-terapêutica.
- Evidência animal (Sartori, Kemp, Kim-mecanismo) → [APENAS PRÉ-CLÍNICO]/[EXT], `redirecionado_mecanistico`.
- Nenhum trecho REMOVIDO por falta de fonte; claims rebaixados onde a força era menor que a alegada.

## Declaração de aprovação
> A Biblioteca_B8 foi auditada quanto a conteúdo em 2026-09-06: cada afirmação factual tem vínculo verificado por fonte (G1→G2→G3) ou está explicitamente sinalizada como evidência parcial/pré-clínica. Referências não sustentadas foram rebaixadas/ressalvadas. Ledger (38 trechos) e decisões arquivados em /Auditoria_B8. `validar_auditoria.py`: **0 ERRO, 0 AVISO**. `gate_script.py`: **GATE APROVADO**.
>
> **Pendência P-6:** 2ª verificação independente (avaliador cego) dos claims de alto risco (VITAL, MR Carnegie, metas D/Mg/Se) — fase do avaliador externo.

---

# Rodada [AT] 2026-09-09 — reconciliação de insumo externo (P-7) → CANÔNICA V2

**Escopo:** insumo externo GPM B8 (oficial, molde v2.0 — módulos M00–M10, 44 âncoras, 12 regras) + BRIEFING RODADA0 (tabela-mestra §3 com 44 PMIDs) + BRIEFING CONSOLIDADO v1 + anexo de artigos (106 entradas reais — o briefing alegava "98") + matriz ChatGPT (50 claims B8.SM02.001–050, 10 regras B8-Causal verbatim, bloco NEG vitamina C/vitamina D, cadeia-mãe e quatro-pontos A/B/C/D). **Auditado ref a ref antes de qualquer fusão.**
**Objeto:** `B8 DEFICIENCIAS DE MICRONUTRIENTES V1 CANONICA.md` (96 refs) → `V2 CANONICA.md` (145 refs).

## Pipeline (idêntico ao das rodadas B5/B6/B7)
1. **Parse do anexo:** 106 entradas; 105 com DOI + 1 sem DOI (Bourre 2006).
2. **G1 eutils (esearch `DOI[aid]` + busca dirigida + esummary + efetch):** 96/105 DOIs resolvidos e batendo autor+ano+tema; **0 falso positivo**; 9 NÃO-INDEXADOS confirmados (Barakat; Chambers; Fedulova; Jayashree; Júnior; Kim; Lubis; Medford; Wróblewska) — mantidos fora, sem fonte forjada. **Bourre 2006 resgatado por busca dirigida** (J Nutr Health Aging, Parte 1: micronutrientes) — o briefing o dava como NAO-IDX, e o artigo existe e é a âncora bioquímica das claims .001–.002. 34 alertas de rótulo eram apenas forma e ano **epub-vs-print**, normalizados pelo print oficial (ex.: Barks 2019; Firth 2017/2018; Ferriani 2022; Rucklidge 2025; Lu 2025).
3. **CEGUEIRA DO BRIEFING (erros factuais revertidos — expostos):** (i) "Mattei 2019 = McWilliams 2022" — **falso**, Mattei D 2019 existe (Curr Nutr Rep, Micronutrients and Brain Development); (ii) "Yoon 2026 = Zielińska 2023" — **falso**, Yoon 2026 existe (Nutrients, coenzimas B em neuropatia nutricional) — ficou BAIXO por redundância, não por inexistência; (iii) "Dehesh 2026 = Domański 2025" — **falso**, Dehesh 2026 existe (Iran J Psychiatry, network de ingestão em estudantes) — BAIXO (ingestão ≠ deficiência); (iv) "Cortés-Albornoz 2021 não localizada" — localizada (Nutrients, scoping nutrição materna) — BAIXO; (v) "Das 2025 não localizada" — localizada — BAIXO; (vi) "Bourre 2006 NAO-IDX" — resgatado e ENTRA; (vii) "Wang 2018 sem PMID → [G1]" — **já vigente** na V1 (REF_WANG_2018), não entra duplicado.
4. **Masters GPM:** 41/41 validados (0 já vigentes). **Sobreposição V1:** 6 (Wang 2018; Zielińska 2023; Carnegie 2024; Han 2025; Fang 2025; Hachmeriyan 2026) → fila de decisão = 91.
5. **Matriz de decisão (arquivada em `producao/insumos/matriz_b8_decisao.json`):** **49 ENTRA / 30 BAIXO / 12 EXC**. EXC por malha de escopo permanente: autismo ×5 (Altamimi; Guo; Indika; Avram; Daniel), neurodegeneração ×2 (Kumar; Miteva), demência/AVC (Navale — resgatada do apagamento mas fora de escopo), anorexia (Hanachi), epilepsia (Chen H), delirium (Ceolin), botânica (Gupta).
6. **Usuário aprovou "completo (49)"** (padrão B5/B6/B7) → fusão integral dos 49.

## Conteúdo incorporado (V2)
- **§1.1:** fundamentação histórica do escopo (Bourre 2006). **§1.2:** B12 neuropsiquiátrica (Sahu 2022; Mathew 2024; Badar 2022 = **relato de caso**, possibilidade clínica); coortes TUDA (Moore 2019) e ELSA-Brasil (Ferriani 2022); mecanismos do complexo B (Kennedy 2016). **§1.3:** catálogo ampliado (Nogueira-de-Almeida 2023; Muscaritoli 2021); nutrientes×mitocôndria (Du 2016 — **TEPT fora do escopo nominal**); fronteira neurológica (Lahoda Brodska 2023). **§1.6/§2.2:** Eyles 2013; Cui 2021 (esquizofrenia = fronteira ilustrativa); hipótese complemento-sinapse/VDBP-megalin (Yang 2026 — **hipótese, sem lastro intervencional**); Kohl 2025; **Horsdal 2025 (iPSYCH2012: significativo p/ esquizofrenia/TEA/TDAH, NULO p/ TDM com n≈24 mil casos — NEG no desfecho-âncora)**; Skoczek-Rubińska 2025 (inconsistente); **Moroianu 2026 (sinais colapsam ao nulo pós trim-and-fill; suplementação de B12 esparsa e nula — avaliação direcionada, não universal)**. **§2.1:** Rajen 2025; Faugere 2025; Al Jassem 2024 (todos associativos — B8-CAUSAL-02). **§2.3:** Shayganfard 2022; Astorino 2025; Faa 2025. **§2.4:** Barks 2019/2021 (ferro-modelo; epigenoma hipocampal); fronteira neurodesenvolvimental (McWilliams 2022; Fiani 2023; Mattei 2019). **BLOCO_05:** Domański 2025; Radoeva 2025 (ingestão ≠ status; TEA ilustrativo). **§6.3:** Firth 2018 (status no FEP) e Firth 2017 (suplementação em esquizofrenia) — fronteira ilustrativa de método; Tortajada 2026 (ponte B9); Rajasekar 2024. **§7.5:** MRs Hui 2024, Lu 2025, Ye 2025 — com a cláusula **MR ≠ eficácia de suplementação (B8-CAUSAL-03)**. **BLOCO_08:** pontes Rudzki 2021 e Barone 2022 (B7), Wesselink 2019 e Tortajada 2026 (B9), Shahini 2026 (B1), Scuto 2024 (B6/B3) — conexões entre mecanismos, não duplicação (B8-CAUSAL-10). **BLOCO_11:** populações (Alexa 2026; Islam 2025 perinatal; Anmella 2025 N=729 jovens; Berger 2024; Rucklidge 2025). **BLOCO_12:** Cenário F — vitamina C (Plevin 2020, associação sem prova intervencional).

## REGRAS B8-CAUSAL-01..10 — fixadas em CONTROVÉRSIAS (contrato da biblioteca)
01 deficiência ≠ causa automática · 02 associação ≠ precedência/causa · 03 MR = causalidade instrumental, não eficácia · 04 suplementação é pergunta causal distinta da associação status×doença · 05 ingestão ≠ deficiência bioquímica · 06 soro ≠ deficiência funcional automática · 07 evidência animal/celular sem linguagem clínica sem ponte humana · 08 proibido termo genérico mascarar heterogeneidade (par micronutriente×desfecho) · 09 afirmação sobre suplementação exige evidência intervencional específica · 10 relações B8→módulos = conexões entre mecanismos, não duplicação.

## Tríade sincronizada
- `Evidencias/Bibliografia/01_pmids.json`: 96 → **145** (id único; claim_id `B8.MEC.BLOCOxx.nnn`).
- `Evidencias/Vinculos/vinculos_referencia_afirmacao.json`: 34 → **83** (trechos-âncora únicos, verificados literalmente 1× na V2).
- `Auditoria_B8/ledger_auditoria_B8.json`: 38 → **87** (`origem_entrada=GPM`, `acao_correcao=MANTER`, verificador "IA G3 Rodada [AT] GPM B8 2026-09-09 (insumo externo auditado ref a ref; P-7) — P-6 pendente").
- Manifesto: `artefato_rotulo=CANONICA v2`, rodada 4, pmids_total 145, vínculos 83, palavras 10.007, versão 2.6, pendência P-6 AMPLIADA; trilha `producao/04_AT_ciclo_2026-09-09.json`.

## Portões oficiais (pós-fusão)
- `gate_script.py` (P-5): **APROVADO (conteúdo)** — 145 refs Módulo 09, 83 vínculos.
- `validar_auditoria.py` (framework): **0 ERRO, 0 AVISO** (87 trechos no ledger; 145 refs únicas).
- `checklist_entrega.py B8`: **41/41 OK, 0 FALHA**.

## Pendências honestas
- **P-6 (2ª verificação cega, Via 2): PENDENTE** — cobrirá ao fim da rodada 16/16 todas as levas [AT] (inclui os 49 novos claims B8; claims de alto risco desta leva: MRs Hui/Lu/Ye, Moroianu, Horsdal, Masters GPM). Não autocertificável.
