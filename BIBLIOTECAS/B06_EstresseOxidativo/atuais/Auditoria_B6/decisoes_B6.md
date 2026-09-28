# Auditoria Científica de Conteúdo — B6 (Estresse Oxidativo)

**Data:** 2025-05 (retrocompatibilização ao padrão B7/B8) · **Sessão:** operador de geração; **P-6** (2ª verificação independente/avaliador cego) PENDENTE.
**Objeto:** trechos-âncora da canônica `B6 ESTRESSE OXIDATIVO V1 CANONICA.md`.
**Ferramentas:** G1 eutils (esearch+esummary+efetch), G2 espécie/elegibilidade, G3 suporte; `gate_script.py` (P-5) + `validar_auditoria.py` (framework).

## Contagem de decisões
- Trechos no ledger: **33**
- G1: {'VERIFIED_REFERENCE': 33} · G2: {'NAO_APLICAVEL': 4, 'ELIGIBLE_SOURCE': 29} · G3: {'APROVADO': 33}
- status_auditoria: {'APROVADO': 33}

## Notas
- Módulo 09 no schema oficial (id_referencia_interna `REF_SOBRENOME_ANO`, doi, claim_id_origem; 5 arquivos).
- Referências citadas apenas em listra/corpus indexadas por rótulo canônico (apêndice de corpus) para rastreabilidade; citações clássicas de prosa sem PMID verificável foram rebaixadas a menção nominal sinalizada ao P-6 (R04: campo vazio preferível a dado inventado).
- Evidência animal/pré-clínica sinalizada `[APENAS PRÉ-CLÍNICO]/[EXT]`; bloco natureza_sistema (P12), semantic_layer (R06) e referência cruzada a B16 (P16) presentes na canônica.

## Declaração
> A Biblioteca_B6 foi auditada quanto a conteúdo: cada afirmação factual tem vínculo verificado (G1→G2→G3) ou está sinalizada como parcial/pré-clínica. `validar_auditoria.py`: **0 ERRO**; `gate_script.py`: **GATE APROVADO**.
> **Pendência P-6:** 2ª verificação independente (avaliador cego).


---

## Rodada [AT] 2026-09-08 — reconciliação de insumo externo (P-7) → V2

**Insumos (4):** anexo "Artigos cientificos do mecanismo B6 Stress oxidativo" (106 refs) + GPM_B6 (M00–M10) + briefing rodada 0 + triagem (matriz 13 claims). Objetivo declarado do insumo: eixo **B6-vitamina → transulfuração → cisteína → GSH → redox** como arquitetura nova do módulo, sem conflito com o corpus vigente (verificado: overlap 0/36).

**Pipeline G1 ref a ref (eutils):** 106/106 DOIs parseados → esearch DOI[aid] → esummary → efetch (abstracts em producao/insumos/matriz_b6_g1.json). 95 resolvidas por DOI; +2 âncoras fora do anexo verificadas (Wondrak 22116705; Kannan & Jain 14975445 — correção de autoria do insumo "Jain/Kannan"→"Kannan & Jain" confirmada); **1 resgate**: Kéry & Kraus 1994 = 7929220 (busca dirigida autor+tema; o briefing declarou "sem resolução" — resolvida pela nossa auditoria); Ereño-Orbea 2013 = 24043838 também consta resolvida (briefing a dava como não-localizada). **NAO-IDX finais = 10** (Dawood, González-Recio, İnceören, Itoh→[G1], Lee-2019, Li-2026, Mendes, Serhiyenko, Shrayner, Velásquez). Tabela-mestra do GPM **45/45 confirmada** por autor+ano+PMID. Divergências autor/ano: **0/95**. Falsos positivos: **0**. Incongruência interna exposta: briefing/GPM dizem "93 refs"; o anexo tem 106 (a própria triagem diz "106").

**Matriz de decisão ref a ref (98 avaliadas com abstract lido antes de incorporar):** ENTRA **72** (ENZ 33 · B6DEF 9 · ANTIOX 11 · GSH 8 · HUM 8 · NEG 2 · HIP 1) · BAIXO 10 · EXC 16 (autismo Chen-2021; Parkinson Corona-Trejo; Alzheimer/MCI An/Olaso-González; CV-DM sem lição nova Li-2025/Yin; não-mamífero Pilesi/Havaux/Neugart/Hacham/Ankisettypalli/Devi/Lee-2025/Matoba/Conter-2020/Tu). Decisão do usuário: **aplicar completo** (padrão B5: tudo que é mecanisticamente importante, selos honestos, sem extrapolação).

**Correções de dado aplicadas nesta rodada:**
1. Renomeadas 3 refs para o **ano do Epub oficial** (ano usado pelo insumo/GPM e consagrado na literatura), com print documentado em revista_ano: Banerjee 2004 (print 2005; pii/DOI 2004), Sbodio 2018 (DEP 20180823; print 2019), Pusceddu 2019 (DEP 20190525; print 2020). Apanhado pelo framework de auditoria (3 ERROs de citação órfã) e corrigido no mesmo ciclo.
2. Alias 'Bønaa' adicionado (o ø não decompõe em NFKD; a citação tipográfica "(Bønaa 2006)" precisava do alias para casar REF_BONAA_2006 no framework oficial).
3. Campo mecanismo_origem bugado dos 36 vínculos vigentes ("mecanismo_Bn[1:].lower()+_x") → corrigido para mecanismo_B6_estresse_oxidativo.
4. manifesto vinculos_n2 19 → 108 (estava defasado na V1).
5. Rótulos normalizados: Bonaa_2006 (Bønaa), Vandeneynde_2021 (Van den Eynde).

**Aplicação V2:** canônica 7.571 → **10.126 palavras**; +72 refs (36→**108**). Novas seções: 1.9 (eixo enzimologia/transulfuração), 2.4 (deficiência animal, Cabrini/Lima como centro da heterogeneidade), 3.x antioxidante direto selado [APENAS PRÉ-CLÍNICO], subseção glutationa-CONTEXT + hipótese Nrf2 [G1] (Kato), 5.y humano (Davis/Lamers/Shen/Pusceddu/Ford/Lai/Cheng/Vandeneynde), subseção âncoras NEG (Bønaa/NORVIT, Christen/WAFACS) na B6.R01. Regras fixadas **B6.R01–R09** em CONTROVÉRSIAS. V1 arquivada em producao/historico/v1_canonica_2026-09-08.md. Tríade atualizada e verificada cruzada: **01_pmids 108 = vínculos 108 = ledger 108 (conjuntos idênticos; trechos-âncora literais)**.

**Portões:** gate_script P-5 **APROVADO (108|108)** · framework validar_auditoria **0 ERRO** (36 avisos [TAG] pré-existentes da geração V1 + padrão não-bloqueante) · checklist_entrega **41/41** · varredura de PMID no texto = 0 · P-4 adendo V2 15/15.

**Pendências declaradas:** P-6 (2ª verificação cega, Via 2) **PENDENTE** para toda a leva [AT]; âncora neuronal do claim SM02.011 permanece **[G1]** (Itoh 2024 — periódico não indexado; sem inventar fonte); Kato/Nrf2 selado como hipótese emergente [G1]; polimorfismos CBS/CGL ↔ fenótipo psiquiátrico = [G1] (zero na coleção).
