# Auditoria Científica de Conteúdo — B4 (Deficiências de Monoaminas)

**Data:** 2024-06 (retrocompatibilização ao padrão B7/B8) · **Sessão:** operador de geração; **P-6** (2ª verificação independente/avaliador cego) PENDENTE.
**Objeto:** trechos-âncora da canônica `B4 DEFICIÊNCIA DE MONOAMINAS V1 CANONICA.md`.
**Ferramentas:** G1 eutils (esearch+esummary+efetch), G2 espécie/elegibilidade, G3 suporte; `gate_script.py` (P-5) + `validar_auditoria.py` (framework).

## Contagem de decisões
- Trechos no ledger: **37**
- G1: {'VERIFIED_REFERENCE': 37} · G2: {'ELIGIBLE_SOURCE': 30, 'NAO_APLICAVEL': 7} · G3: {'APROVADO': 37}
- status_auditoria: {'APROVADO': 37}

## Notas
- Módulo 09 no schema oficial (id_referencia_interna `REF_SOBRENOME_ANO`, doi, claim_id_origem; 5 arquivos).
- Referências citadas apenas em listra/corpus indexadas por rótulo canônico (apêndice de corpus) para rastreabilidade; citações clássicas de prosa sem PMID verificável foram rebaixadas a menção nominal sinalizada ao P-6 (R04: campo vazio preferível a dado inventado).
- Evidência animal/pré-clínica sinalizada `[APENAS PRÉ-CLÍNICO]/[EXT]`; bloco natureza_sistema (P12), semantic_layer (R06) e referência cruzada a B16 (P16) presentes na canônica.

## Declaração
> A Biblioteca_B4 foi auditada quanto a conteúdo: cada afirmação factual tem vínculo verificado (G1→G2→G3) ou está sinalizada como parcial/pré-clínica. `validar_auditoria.py`: **0 ERRO**; `gate_script.py`: **GATE APROVADO**.
> **Pendência P-6:** 2ª verificação independente (avaliador cego).

---

## Rodada [AT] 2026-09-08 — reconciliação de insumo externo (P-7) → V2

**Insumo:** consolidação externa B4 (esqueleto 25 + correções) + anexo 177 refs (172 DOIs) + briefing v1 (semente 14).
**Auditoria:** ref a ref, G1 eutils (esearch DOI[aid]→esummary→efetch abstracts; resgate full-DOI para 8 DOIs-PII antigos). Relatório: `producao/insumos/RELATORIO_AUDITORIA_MATRIZ_B4.md`; matrizes/decisão no mesmo diretório.

**Contagens:** 177 itens → 161 resolvidos G1 · **0 falsos positivos** · **94 incorporadas** (37→**131 refs**) · **1 EXC tardia pós-abstract** (39696597 "Evans 2024": título cita depressão, abstract = modelo 5XFAD de **Alzheimer** — fora de escopo permanente) · 13 EXC escopo (TEPT×4 — divergência explícita vs consolidação —; Alzheimer; Parkinson; dor×3; anorexia; APP/ascorbato; fitoquímicos sem sonda clara [P20]; clínico japonês) · 57 BAIXO incremento (reavaliáveis) · 12 FALHAS/não-resolvidos (Alawie; Cosci; Fassler; Hasler; Isingrini bioRxiv; Kovalzon; Li J; Liu 2023 medRxiv=HOLD; Nakamura; Neumeister 2025=republicação→original 15131521; O'Leary; Kayabaşı `[G1]`).
**Correções de autoria do insumo (2):** "Martinez 2010"→**Goddard AW 2010** (PMID 19960531); "Ogden 2006"→**Parsey RV 2006** (PMID 16154547). Vetulani & Sulser 1975 confirmado = 170534 (já vigente). 12 refs do insumo já vigentes — não duplicadas.
**Aplicação:** prosa+listras [AT] em §1.4 (HIST 10), §2.1 (5-HT 21), §2.3 (depleção 13), §3.1 (DA 14), novo §4.1 (LC–NA 26), novo §8.x (B1↔B4 4 + B2↔B4 Maes) e BLOCO_06-PROF (modelos sucessores 5); regras de leitura B4.R01–R08 fixadas; tabela +4 linhas; apêndice +94 rótulos; V1 rotacionada a `producao/historico/v1_canonica_2026-09-08.md`.
**Incidentes de engenharia:** (1) IDs iniciais sem underscore (REF_SOBRENOMEANO) — corrigidos para REF_SOBRENOME_ANO em 01_pmids/vínculos/ledger/trilha; (2) 94 vínculos sem `status_auditoria` (enum gate P-5) — preenchido CONFIRMADO; (3) `forca_causal` inventada 'tier_3_associacao_humana' fora do vocabulário — rebaixada a `tier_4_descritivo_estrutural`; (4) 5 refs sem abstract no PubMed (Schildkraut-1967, Cowen, Albert&Blier, Nemeroff, Kahn-1988) — G3 por título/periódico/autores, registrado no ledger. Soares 2025 carrega pubtype Preprint indexado — registrado.
**Portões:** gate P-5 **APROVADO (131|131)** · framework **0 ERRO** (37 avisos não-bloqueantes, padrão listra descritiva da série) · checklist **41/41**.
**Pendências à frente:** **P-6 (2ª verificação independente cega) PENDENTE** — cobre leva [AT] e claims de alto risco legados; não autocertificável.
