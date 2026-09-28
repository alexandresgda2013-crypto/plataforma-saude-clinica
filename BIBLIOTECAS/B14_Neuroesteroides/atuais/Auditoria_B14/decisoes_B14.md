# Decisões de Auditoria — B14 Neuroesteroides / Esteroides Neuroativos

Data: 2026-09-07 · Prompt v4.2 · Pipeline v2.6 · Mecanismo: `mecanismo_B14_neuroesteroides_hormonios_neuroativos`

## G1 — Existência (eutils/PubMed)
- Briefing B14 consolidado declarou **255 âncoras em tabelas** (17 blocos A–Q; 40 clusters de
  busca C01–C40 + 3 insumos externos auditados).
- Varredura automática via E-utilities (esummary em lote, com backoff): **255/255 PMIDs
  resolvem no PubMed** (0 sem resolução).
- Conferência autor+ano+tema: 16 sinalizações iniciais, todas resolvidas — 15 eram ruído do
  bloco N ou falsos-positivos do conferidor; 4 correções reais de rótulo (PMID inalterado e
  on-topic, ver abaixo).

## Correções de rótulo (sem inventar PMID; regra anti-PMID-falso)
| PMID | Briefing rotulava | Real (esummary) | Decisão |
|---|---|---|---|
| 24756763 | "Schüle et al., 2014" | **Crowley SK & Girdler SS, 2014**, *Psychopharmacology* | id = REF_CROWLEY_2014; alias SCHULE preservado |
| 17159334 | "Eser 2007" | Eser D, **2006** (impresso), *Neuroendocrinology* | id = REF_ESER_2006 |
| 34506047 | "Reddy 2021" | Reddy DS, **2022**, *J Neuroendocrinol* | id = REF_REDDY_2022 |
| 32435660 | "Belelli 2019" | Belelli D, **2020**, *Neurobiol Stress* | id = REF_BELELLI_2020 |
| 37715106 | "Patterson/Morrow 2023" | Patterson R, **2024**, *Neuropsychopharmacology* | id = REF_PATTERSON_2024; alias MORROW |

## G2 — Elegibilidade (espécie/desenho)
- **240 âncoras mecanísticas** no `01_pmids.json`: 137 revisões/meta [OB], 69 humano/ECR/coorte
  [EC], 34 pré-clínico/estrutural/animal [ML].
- Classificação por conteúdo do Briefing + overrides científicos (Purdy 1991, Majewska 1986,
  Vicini δ-KO, Miller/Legesse/Sun/Zhou estruturais, Cadeddu, Vallee CB1-SSi, Kenney, etc. = ML;
  ensaios/metas humanos = EC; revisões = OB).
- **15 PMIDs do bloco N** (acupuntura/TCM, óleo de cânhamo, Shuyu, crisina, isoflavonas,
  intervenções nutricionais/mente-corpo) são **intervenção não-mecanismo**: excluídos do corpo
  e registrados em `producao/ruido_excluido_blocoN.json` (status EXCLUIDO_RUIDO), conforme o
  próprio Briefing determina ("NÃO ancorar como mecanismo").

## G3 — Suporte / fidelidade
- Ledger: **240 entradas, todas APROVADO**, ancoradas em **listra literal** da canônica
  (prose 0 / listra 240 / fallback 0).
- Citações em prosa `(Sobrenome Ano)[TAG]` casam por sobrenome/alias; rótulos de listra batem
  1:1 com o id oficial. Zero rótulo inexistente; zero id órfão (os 240 ids são citados).

## Regras canônicas aplicadas
- **P20/P19:** sem doses/prescrição/cortes; fármacos (brexanolone/zuranolona/ganaxolona/
  etifoxina/golexanolona) e reposição (estradiol/DHEA/testosterona/pregnenolona) entram apenas
  como SINAL de alvo/janela. Exames referenciados por ID oficial (`exame_cortisol_matinal`,
  `exame_acth`, etc.); neuroesteroides não têm exame catalogado → pesquisa, sem corte.
- **R04:** dados animais/estruturais marcados `[APENAS PRÉ-CLÍNICO]`/`[EXTRAPOLAÇÃO POR
  ANALOGIA]`.
- **P16:** neurogênese remetida a `mecanismo_B16_neurogenese` (B14 só registra modulação).
- **P12:** contrato de suporte de decisão (não diagnostica, não substitui julgamento).
- **P17:** 16 chaves de conexão B1–B16 presentes.
- **RAG:** zero PMID no texto corrido (PMIDs vivem no Briefing/JSON).
- Bifasicidade (subida vs. retirada), PMDD = sensibilidade (não nível), perimenopausa =
  variabilidade do estradiol, periférico ≠ central, TSPO-PET ≠ síntese, sexo como variável
  intrínseca e fenótipos masculinos preservados.
- Itens `[G1]` do Briefing (knock-in α2 Durkin 2018 bioRxiv; originais α4/δ Smith/Shen/Gong;
  Baulieu 1981; genética GABRA4/GABRD; metilação srd5a1 primária; golexanolona/PRAX-114
  primário; finasterida→ideação suicida de farmacovigilância; etifoxina RCT grande na TAG)
  permanecem **sem PMID inventado**, para a Rodada 2/avaliador cego. Tamanhos de efeito
  (SMD/OR) são alegação a confirmar no G3.

## Pendência
- **P-6**: Fase 3 de Fidelidade Canônica (checklist A1–A4/B1–B3/C1–C5/E1–E3) depende de
  **avaliador cego independente** — não autocertificado.

---

# ALTERAÇÃO 2026-09-10 — REPARO AT-00 (detectado na re-varredura motivada pela perícia externa)

**O quê:** normalização de 50 entradas da leva [AT] 2026-09-09.
**Motivo:** a perícia externa dos scripts (LOTEs 1–7) levou à re-execução do checklist nas 16;
B14 reprovou 3 itens. Causa: o script `B14_json_apply.py` copiou vocabulário de **ledger** para
o arquivo de **vínculos** — classe "vocabulário cruzado entre artefatos" (depois formalizada
pelo perito como furo F2 das ferramentas oficiais).
**Alterado:**
1. `Evidencias/Vinculos/vinculos_referencia_afirmacao.json` — 50 vínculos com
   `status_auditoria: "APROVADO"` → `"CONFIRMADO"` (enum oficial de vínculos).
2. `Evidencias/Bibliografia/01_pmids.json` — 50 refs com `g1_metodo` descritivo →
   `"eutils_automatico"` (string exata do checklist); detalhe preservado em `g1_resumo`.
**Nada de conteúdo científico foi alterado** — apenas vocabulário de campos.
**Verificação pós-reparo:** gate ✅ APROVADO · framework ✅ 0 ERRO · checklist ✅ **41/41**.
**Rastreio cruzado:** registrado como IMPL-AT-00 em `CONTRARRAZAO_PERICIA_EXTERNA_SCRIPTS_2026-09-10.md` §6
e em `BIBLIOTECAS/CHANGELOG_GERAL.md`. **Licão (nova regra AT-10):** toda alteração passa a
exigir nota datada como esta.
