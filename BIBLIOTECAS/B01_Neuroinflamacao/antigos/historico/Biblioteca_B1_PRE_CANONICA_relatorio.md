# RELATÓRIO ATO 2 — BIBLIOTECA B1 PRÉ-CANÔNICA COM MÓDULO 9 NATIVO

**Mecanismo:** B1 — Neuroinflamação · **Data:** 2026-09-03 · **Rodada:** 2 (geração).
**Prompt:** FINAL PMID v4.2 (atualizado pelo usuário, com g1/g3 e regra E3) + GPM v3 + 7ª Lista Canônica + Filosofia + corpus Ato 1.

## O que foi gerado

11 checkpoints (BLOCOs 01–11), cada um com corpo da Biblioteca + fragmento de Módulo 9, e uma consolidação final em `/Evidencias/`:

| Bloco | Tema | Claims | N1 refs | N2 vínculos |
|---|---|---|---|---|
| 01 | Fundamentos (adaptação/sickness/priming) | 3 | 13 | 15 |
| 02 | Vias moleculares (NLRP3, TLR, NF-κB, JAK-STAT, cGAS…) | 24 | 48 | 46 |
| 03 | Mediadores (citocinas/quimiocinas + inventário negativo) | 12 | 24 | 28 |
| 04 | Células/estruturas (microglia, astrócito, BHE, vago, meníngeas) | 10 | 18 | 19 |
| 05 | Biomarcadores (metas, TSPO-PET, LCR) | 7 | 13 (+6 meta +1 RCT) | 18 |
| 06 | Tradução clínica (IFN-α, anedonia/recompensa) | 4 | 11 | 10 |
| 07 | Nós centrais (NF-κB + NLRP3) — síntese | 1 | 6 | 6 |
| 08 | Conexões B1↔B2…B14 | 14 | 19 | 18 |
| 09 | Impacto sobre plasticidade (B3) | 3 | 6 | 6 |
| 10 | Impacto sobre neurogênese (B16) | 3 | 5 | 5 |
| 11/12 | Estratificação (subtipo inflamatório) — condicional | 1 | 7 | 7 |

**Consolidado final (`ato2_pacote/Evidencias/`):**
- `Bibliografia/01_pmids.json` — **135 referências únicas** (schema 09.1), todas com PMID real do corpus
- `Bibliografia/02_meta_analises.json` — **6 meta-análises** (schema 09.2 com `forca_evidencia_afirmacao`)
- `Bibliografia/03_ensaios_clinicos.md` — **1 RCT** (infliximabe, template narrativo 09.3)
- `Vinculos/vinculos_referencia_afirmacao.json` — **163 vínculos** frase↔referência

## Regras cumpridas (validadas por script, zero problemas)

- **G1 ≠ G3:** todo registro tem `g1_metodo="eutils_automatico"` e `g3_verificado_por=""`; nenhuma autocertificação. `verification_status` nasce `"pendente"`, `g2_elegibilidade="nao_avaliado"`, `status_referencia="CANDIDATO"`.
- **Regra E3:** os 163 `trecho_ancora` terminam em pontuação/tag e são cópia LITERAL do corpo (checado por matching automático). Sem corte por caracteres.
- **PMIDs só da ferramenta:** 100% dos 135 PMIDs existem no `abstracts_pubmed.json` (busca esearch/efetch). Zero PMID de memória.
- **Espécie declarada:** `especie_mesh` (Humans/Mice/Rats/Cells) e `evid_role` em todos; extrapolação marcada (`extrapolacao_por_analogia`, tags [EXT]/[ML]/[OB]).
- **Inventário negativo honesto:** RLRs (02.006), miR-155, oligodendrócitos/NG2 (04.007), B4 SERT/p38, B5 EAAT2, B8 zinco/Mg, B13 CB2/FAAH, resolvina D1/LBP séricos, IL-8 — registrados como gap/[EXT], sem forçar.
- **Dois achados canônicos confirmados por PMID real:** Bull IL-6 × IFN-α (18458677) e Klengel FKBP5 (23201972).
- **RCT com resultado primário negativo** apresentado como prova de ESTRATIFICAÇÃO (subgrupo), não recomendação.

## Próximos passos (pós-Rodada 2, conforme o Processo)

1. **Checklist Estrutural** da Biblioteca (artefato) — pode rodar agora sobre os arquivos consolidados.
2. **Portão G1→G2→G3** (sessão de auditoria separada): G1 já nasce cumprido (ferramenta + log); **G2** pré-preenche espécie via MeSH mas o veredito `eligible` é do avaliador; **G3** lê abstract/texto e preenche `g3_verificado_por`, `status_auditoria`, `forca_causal`, `verification_status`.
3. **Gate/Bloco H** → **Rodada 3** (consolidação, proibida citação nova) → **Checklist Fidelidade** → Biblioteca **CANÔNICA**.

## Limites honestos desta geração

- Não houve leitura G3: tudo está CANDIDATO/pendente por design (a ciência foi escrita a partir dos abstracts, mas o veredito de suporte frase-a-frase é da auditoria).
- O corpus foi top-10 por relevância por query + âncoras dirigidas; referências canônicas que porventura não vieram no top foram cobertas pelas âncoras, e o que não veio ficou declarado no inventário negativo.
