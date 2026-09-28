# FASE 3 — CHECKLIST DE FIDELIDADE CANÔNICA (P-4, adendo v2.1)
## B14 — Neuroesteroides / Esteroides Neuroativos

**Mini-rodada PRÓPRIA** (Processo de Geração v2.1, item 11 da execução; documento
`04_fase3_auditoria_fidelidade/FASE 3- CHECKLIST FIDELIDADE CANONICA.md`).
Relatório item a item **SIM / NÃO + evidência**. Não corrige — aprova ou devolve.

- **Aplicado por:** operador/IA em sessão dedicada (fase atual = **1 operador**, P-6)
- **Data:** 2026-09-07
- **Biblioteca:** B14 NEUROESTEROIDES V1 CANÔNICA (9.564 palavras; audit_status: canônica)
- **Contagem:** 240 referências (137 OB / 69 EC / 34 ML) · 240 vínculos · 240 ledger · 15 ruído bloco N excluído

> **Escopo da certificação (honestidade P-6).** Este checklist é aplicado pelo mesmo
> operador/IA que gerou e auditou a biblioteca. O Processo v2.1 (Bloco P-6) declara que, na
> fase de 1 operador, isso **mitiga mas não elimina** o risco de viés de confirmação; a
> **2ª verificação independente cega** dos claims de ALTO RISCO (nó central BLOCO_07 /
> conexões BLOCO_08 HIGH; `uso=clinico`; evidência humana usada para causalidade; decisão de
> rejeitar citação) é **pendência de fase (P-6)**, não autocertificável. O gate de script
> P-5 passou; a certificação abaixo atesta os itens verificáveis por artefato.

---

## A. FIDELIDADE AO QUE FOI APROVADO

- [x] **A1 — Frase tem lastro.** **SIM.** 242 rótulos citados no corpo; todos têm registro no
  Módulo 09 (`01_pmids.json`) e vínculo N2. As 2 ocorrências aparentes sem registro
  ("1998"/"2014") são citações em prosa `(Uzunova 1998)[EC]` e `(Vallee 2014)[ML]` — ambas com
  id `REF_UZUNOVA_1998` e `REF_VALLEE_2014` no Módulo 09 e casadas por sobrenome/alias
  (framework `validar_auditoria`: **0 ERRO** de citação sem entrada). Zero claim sustentado só
  por em_busca/rejeitado.
- [x] **A2 — Nada de rejeitado/pendente residual.** **SIM.** As 15 referências do bloco N
  (intervenção não-mecanismo) foram marcadas `EXCLUIDO_RUIDO` e **não aparecem no corpo**
  (0 residual). Nenhuma ref mecanística com status ≠ CONFIRMADO. Itens `[G1]` (knock-in α2
  Durkin bioRxiv; originais α4/δ; metilação srd5a1; etc.) são mencionados **como
  não-resolvidos/pendentes de Rodada 2**, sem PMID inventado — marcação de incerteza, não
  lastro de afirmação.
- [x] **A3 — Zero citação nova na Rodada 3.** **SIM.** Todas as 240 refs têm
  `origem_pipeline = BUSCA_FERRAMENTA` e `g1_metodo = eutils_automatico` (255/255 PMIDs do
  Briefing validados via eutils). Nenhuma referência introduzida na consolidação sem G1→G3.
- [x] **A4 — Log de reconciliação aplicado integralmente.** **SIM.** Correções de rótulo
  aplicadas no texto e nos JSON: **Crowley 2014** (Briefing "Schüle"; alias SCHULE
  preservado), Eser 2006, Reddy 2022, Belelli 2020, Patterson 2024; 3 ids reconciliados
  (WHEDON_2017, GERBASI_2021, DELIGIANNIDIS_2023c errata); ruído bloco N removido do corpo.
  Efeito verificável (grep/script), não só no log.

## B. MARCAÇÃO DE INCERTEZA

- [x] **B1 — Ressalva visível.** **SIM.** Claims de baixo lastro carregam marcação textual:
  `[G1]` (4×), "emergente"/"fronteira" (5×), `[EXTRAPOLAÇÃO POR ANALOGIA]` (3×),
  `[APENAS PRÉ-CLÍNICO]` (R04), e ressalvas explícitas ("lacuna real da TAG", "PRAX-114
  falhou", "evidência muito baixa DHEA", "não há deficiência universal"). Nunca nivelados ao
  muito-estabelecido.
- [x] **B2 — Selos de verificação por frase.** **SIM (padrão da série).** Cada claim leva tag
  de tipo/verificação: **[ML]** = pré-clínico/animal/estrutural (172), **[EC]** = evidência
  clínica/humana (209), **[OB]** = revisão/meta (296); incerteza explícita por `[G1]`/
  "emergente"/extrapolação. Equivale ao mapeamento [PRÉ-CLÍNICO]=ML, [VERIFICADO/clínico]=EC,
  revisão=OB, [EMERGENTE]=[G1]. (Mesmo padrão aprovado em B1–B13.)
- [x] **B3 — Pré-clínico/extrapolado não viram afirmação humana.** **SIM.** 34/34 refs ML têm
  `especie_mesh = ["Animals"]` e `extrapolacao_por_analogia` marcada; afirmações humanas
  (TEPT/líquor, PMDD, perimenopausa, DPP, TDM) são lastreadas por refs [EC]/[OB] humanas.
  Dados animais de bifasicidade/α4δ apresentados como mecanismo em modelo, com tradução
  humana declarada parcial.

## C. RASTREABILIDADE ESTRUTURAL

- [x] **C1 — Mão-dupla texto ⇄ Módulo 09.** **SIM.** 0 vínculo órfão; 240/240 refs do M09
  citadas no corpo (0 id órfão). Gate P-5: "refs Módulo09: 240 | vínculos N2: 240".
- [x] **C2 — Vínculos íntegros.** **SIM.** 100% com `trecho_ancora` LITERAL (240/240 ancorados
  em **listra literal**, terminam em `*`; 0 truncado — E3), `status_auditoria` no enum
  (CONFIRMADO) e `forca_causal` preenchido (tier_1/2/3/4). _2ª avaliação de alto-risco =
  P-6 pendente._
- [x] **C3 — Terminologia GRADE.** **SIM.** Sem "GRADE A/B/C/D" em contexto mecanístico
  (checagem negativa); usa `forca_evidencia_afirmacao` alto|médio|baixo-médio.
- [x] **C4 — Sem PMID/DOI no texto corrido.** **SIM.** Zero PMID numérico (7-8 dígitos) e zero
  DOI no corpo; classificador [ML]/[EC]/[OB] único por tag.
- [x] **C5 — Escopo preservado.** **SIM.** P20: sem doses/posologia/cortes; biomarcadores por
  ID oficial (`exame_cortisol_matinal`, `exame_acth`, etc.); neuroesteroides sem exame
  catalogado → pesquisa, sem corte. P16: neurogênese remetida a
  `mecanismo_B16_neurogenese` (B14 só registra modulação). Fármacos/reposição como SINAL, não
  prescrição.

## E. REGRA DE AUTORIDADE DOS CAMPOS (anti-autocertificação)

- [x] **E1 — `g1_metodo` é sempre ferramenta.** **SIM.** 240/240 = `eutils_automatico`
  (prova EXISTÊNCIA, não suporte).
- [x] **E2 — `verificado` só com avaliador.** **SIM.** 0 registro com
  `verification_status="verificado"` e `g3_verificado_por` contendo "eutils"/"script"/vazio.
  Refs pré-clínicas = `preclinico`; refs humanas = `verificado` com `g3_verificado_por`
  descritivo (IA G3, G1 validado; P-6 pendente) — sem promoção automática G1→G3.
- [x] **E3 — Sem trecho truncado com veredito.** **SIM.** 0 `trecho_ancora` truncado (todos
  findam em listra `*` ou frase completa).

---

## VEREDITO

**[x] APROVADO COMO CANÔNICA — itens A1–A4 / B1–B3 / C1–C5 / E1–E3 = SIM** (evidência acima;
gate P-5 APROVADO; framework 0 ERRO; checklist de entrega 41/41).

**Ressalva de fase (P-6, não bloqueia o gate de script mas é registrada como pendência
honesta):** a 2ª verificação **cega e independente** dos claims de ALTO RISCO (Bloco H:
nós BLOCO_07 e conexões BLOCO_08 HIGH — B5/B3/B2/B12; `uso=clinico` — brexanolone/zuranolona
na DPP e zuranolona na TDM; evidência humana usada para afirmar direção causal — Rasmusson
líquor/TEPT, Pineles 3α-HSD, Grotch/Osborne/Schoretsanitis predição periparto; e decisões de
rejeição — 15 refs do bloco N, PRAX-114, remoção de narrativa "deficiência universal")
**deve ser feita por avaliador distinto** quando houver equipe (κ inter-avaliador). Na fase de
1 operador ela permanece **PENDENTE**, sem ser maquiada como resolvida — conforme Bloco P-6 do
Processo v2.1.

Contagem final: frases verificadas (claims com tag) = toda a canônica · com ressalva/[G1] =
itens sinalizados no texto · pré-clínicas [ML] = 34 refs · extrapoladas/[EXT] = marcadas ·
removidas na reconciliação = 15 (bloco N) + 0 claim científico.
