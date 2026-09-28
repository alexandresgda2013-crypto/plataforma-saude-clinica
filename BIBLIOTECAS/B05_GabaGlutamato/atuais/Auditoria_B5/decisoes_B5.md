# Auditoria Científica de Conteúdo — B5 (GABA / Glutamato)

**Data:** 2024-07 (retrocompatibilização ao padrão B7/B8) · **Sessão:** operador de geração; **P-6** (2ª verificação independente/avaliador cego) PENDENTE.
**Objeto:** trechos-âncora da canônica `B5 GABA GLUTAMATO V1 CANONICA.md`.
**Ferramentas:** G1 eutils (esearch+esummary+efetch), G2 espécie/elegibilidade, G3 suporte; `gate_script.py` (P-5) + `validar_auditoria.py` (framework).

## Contagem de decisões
- Trechos no ledger: **42**
- G1: {'VERIFIED_REFERENCE': 42} · G2: {'ELIGIBLE_SOURCE': 37, 'NAO_APLICAVEL': 5} · G3: {'APROVADO': 41, 'APROVADO_COM_RESSALVA': 1}
- status_auditoria: {'APROVADO': 41, 'APROVADO_COM_RESSALVA': 1}

## Notas
- Módulo 09 no schema oficial (id_referencia_interna `REF_SOBRENOME_ANO`, doi, claim_id_origem; 5 arquivos).
- Referências citadas apenas em listra/corpus indexadas por rótulo canônico (apêndice de corpus) para rastreabilidade; citações clássicas de prosa sem PMID verificável foram rebaixadas a menção nominal sinalizada ao P-6 (R04: campo vazio preferível a dado inventado).
- Evidência animal/pré-clínica sinalizada `[APENAS PRÉ-CLÍNICO]/[EXT]`; bloco natureza_sistema (P12), semantic_layer (R06) e referência cruzada a B16 (P16) presentes na canônica.

## Declaração
> A Biblioteca_B5 foi auditada quanto a conteúdo: cada afirmação factual tem vínculo verificado (G1→G2→G3) ou está sinalizada como parcial/pré-clínica. `validar_auditoria.py`: **0 ERRO**; `gate_script.py`: **GATE APROVADO**.
> **Pendência P-6:** 2ª verificação independente (avaliador cego).

---

## Rodada [AT] 2026-09-08 — reconciliação de insumos externos (P-7) → V2

**Insumos:** consolidação externa B5 (colada) + anexo 190 entradas (autores/ano/título/DOI) + BRIEFING v1 (rodada 0; sementes já vigentes).
**Auditoria:** ref a ref, G1 eutils (esearch DOI[aid]→esummary→efetch abstracts dos 190). Relatório: `producao/insumos/RELATORIO_AUDITORIA_MATRIZ_B5.md`.

**Contagens:** 192 itens → 190 resolvidos · **116 incorporadas** (44→**160 refs**; grupos KET 21 · GABA 20 · NMDA 19 · PLAST 14 · MRS 14 · ANX 10 · STR 6 · IFACE 7) · 53 BAIXO · 14 EXC escopo (Alzheimer×5, autismo×4, epilepsia×3, apneia, carta Babber redundante↔Xu 2020) · 1 **FP exposto** ("Prosowski 2024": DOI do anexo resolve para artigo não correlato (Zhang 2026, γ-butyrolactones); artigo pretendido inexistente no PubMed → **[G1]**, não entrou) · 2 não-resolvidos (congresso Alzheimer; Prosowski [G1]) · 6 já vigentes (não duplicadas).
**Correções de autoria (3):** "Matthew & Samba 2013"→**Carver CM 2013** · "Pich & Millan 2018"→**Cavalleri L 2018** · Hollestein 2021→**2023** (EXC autismo). Correções de metadados do insumo **confirmadas corretas** (Guntupalli, Storey, Vereczki, prioridade Xu 2020, Duman Neuron 2019).
**Aplicação:** prosa+listras [AT] nos blocos MRS/GABA/NMDA+AMPA/KET/PLAST/ANX/STR/IFACE; controvérsia pareada Godfrey(NEG)×Kantrowitz; trava "MRS≠E/I" (Steel×Rideaux); regras **B5.R01–R09** fixadas; tabela +4 linhas; apêndice +116 rótulos; V1 arquivada em `producao/historico/v1_canonica_2026-09-08.md`.
**Incidentes de engenharia (corrigidos):** (1) grupo AMPA (5 refs) esquecido no iterador — detectado por assert de contagem; (2) `claim_id` fora do formato (`B5.MEC.<grupo>` → `B5.MEC.BLOCOxx.nnn`); (3) sufixo de colisão em ID: padrão oficial minúsculo (`Zanos_2018b`, `Le_2026b` ↔ IDs `REF_ZANOS_2018b`, `REF_LE_2026b`) alinhado à B3.
**Portões:** gate P-5 **APROVADO (160|160)** · framework **0 ERRO** (44 avisos não-bloqueantes, padrão listra da série) · checklist **41/41**.
**Pendência:** **P-6 (2ª verificação cega) PENDENTE** para a leva [AT]; não autocertificável.
