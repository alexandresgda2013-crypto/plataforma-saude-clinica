# FASE 3 — CHECKLIST DE FIDELIDADE CANÔNICA (P-4, adendo v2.1)
## B15 — Autofagia / mTOR

**Mini-rodada PRÓPRIA** (Processo de Geração v2.1, item 11; documento
`04_fase3_auditoria_fidelidade/FASE 3- CHECKLIST FIDELIDADE CANONICA.md`). Relatório item a
item **SIM / NÃO + evidência**. Não corrige — aprova ou devolve.

- **Aplicado por:** operador/IA em sessão dedicada (fase atual = **1 operador**, P-6)
- **Data:** 2026-09-08
- **Biblioteca:** B15 AUTOFAGIA/MTOR — V1 CANÔNICA (8.280 palavras)
- **ID canônico:** `mecanismo_B15_autofagia_mtor`
- **Contagem:** 134 referências (74 ML / 39 OB / 21 EC) · 134 vínculos N2 · 134 ledger · 6 ruídos de composto/suplemento excluídos

> **Escopo da certificação (honestidade P-6).** Aplicado pelo mesmo operador/IA que gerou e
> auditou a biblioteca. O Processo v2.1 (Bloco P-6) declara que, na fase de 1 operador, isso
> mitiga mas não elimina o viés de confirmação; a **2ª verificação cega independente** dos
> claims de ALTO RISCO é **pendência de fase (P-6)**, não autocertificável.

---

## A. FIDELIDADE AO QUE FOI APROVADO

- [x] **A1 — Frase tem lastro.** **SIM.** Toda citação `(Autor, Ano)[tipo]` e toda listra
  casa com registro do Módulo 09 (por `id_referencia_interna`, `ids_referencia_interna` ou
  `_aliases`, com normalização de acento) e com vínculo N2. Evidência: framework
  `validar_auditoria.py` = **0 ERRO** de "citação sem entrada"; gate P-5 = 134 vínculos N2.
  Correções de nome aplicadas na prosa para o **1º autor real do PubMed**: o metiloma de
  monócitos é **Zhu** (não "Li") e a rede mTOR co-expressa é **Park** (não "Chen"); rótulos
  descritivos (Kallergi para a autofagia dendrítica que o briefing chamava "Shen 2022";
  Wang para a urolitina/sono) resolvidos por alias.
- [x] **A2 — Nada de rejeitado/pendente residual.** **SIM.** 0 vínculo com status fora do
  enum oficial; as 6 refs de composto/suplemento/TCM/contexto metabólico foram
  `EXCLUIDO_RUIDO` e não aparecem no corpo. Itens `[G1]` (espermidina clínica = pré-print
  bioRxiv; DISC1; TREM2) mencionados como não-resolvidos, sem PMID inventado.
- [x] **A3 — Zero citação nova na Rodada 3.** **SIM.** Todas com
  `origem_pipeline = BUSCA_FERRAMENTA` e `g1_metodo = eutils_automatico` (140/140 resolvem
  no PubMed; 134 mecanísticas).
- [x] **A4 — Log de reconciliação aplicado.** **SIM.** 6 ruídos removidos do corpo; aliases
  de 1º autor/rótulo reconciliados; pró-print separado do epidemiológico publicado; efeito
  verificável no texto e nos JSON.

## B. MARCAÇÃO DE INCERTEZA

- [x] **B1 — Ressalva visível.** **SIM.** `[G1]` (espermidina pré-print), "emergente/
  frontier/translacional", `[EXTRAPOLAÇÃO POR ANALOGIA]`, `[APENAS PRÉ-CLÍNICO]`, lacuna
  humana da ansiedade e tensão do paradoxo da rapamicina marcadas.
- [x] **B2 — Selos por frase.** **SIM (padrão da série).** [ML] = pré-clínico/animal/
  celular (74 refs), [EC] = humano/pós-morte/ECR (21), [OB] = revisão/meta/diretriz (39);
  incerteza por `[G1]`/"emergente".
- [x] **B3 — Pré-clínico não vira humano.** **SIM.** 74/74 refs ML com
  `especie_mesh=["Animals"]` e `extrapolacao_por_analogia` marcada; afirmações humanas (mTOR
  PFC, Beclin/LC3A, FKBP5, ECR rapamicina/NV-5138) lastreadas por refs [EC]/[OB] humanas.

## C. RASTREABILIDADE ESTRUTURAL

- [x] **C1 — Mão-dupla texto ⇄ Módulo 09.** **SIM.** 0 vínculo órfão (gate P-5).
- [x] **C2 — Vínculos íntegros.** **SIM.** 134/134 com `trecho_ancora` literal (listra),
  `status_auditoria` no enum e `forca_causal` preenchido. Framework reporta **134 AVISO(S)**
  de `citacao_literal` (rótulo descritivo vs. label literal) — ressalva **não-bloqueante**,
  padrão da série (0 ERRO).
- [x] **C3 — Terminologia GRADE.** **SIM.** Sem "GRADE A/B/C/D" mecanístico; usa
  `forca_evidencia_afirmacao` alto|médio|baixo-médio.
- [x] **C4 — Sem PMID/DOI no texto corrido.** **SIM.** O número de pré-print que havia
  vazado na seção de controvérsias foi substituído pela citação `(Mackert 2024)[ML]`; zero
  PMID/DOI no corpo.
- [x] **C5 — Escopo preservado.** **SIM.** P20 (sem doses/posologia/cortes; biomarcadores
  por ID `exame_*`; autofagia/mTOR sem exame catalogado = pesquisa); P16 (neurogênese →
  `mecanismo_B16_neurogenese`); fármacos/indutores como sinal. 13 BLOCOs (00–12) presentes.

## E. ANTI-AUTOCERTIFICAÇÃO

- [x] **E1 — `g1_metodo` é sempre ferramenta.** **SIM.** 134/134 = `eutils_automatico`.
- [x] **E2 — `verificado` só com avaliador.** **SIM.** 0 registro `verificado` com
  `g3_verificado_por` inválido (eutils/script/vazio); refs ML = `preclinico`.
- [x] **E3 — Sem trecho truncado com veredito.** **SIM.** Os 134 `trecho_ancora` são listra
  literal (0 fallback; 0 truncado).

---

## VEREDITO

**[x] APROVADO COMO CANÔNICA — A1–A4 / B1–B3 / C1–C5 / E1–E3 = SIM**, com evidência acima
e nos 3 portões: gate P-5 **APROVADO**; framework **0 ERRO** (134 avisos não-bloqueantes);
checklist de entrega **41/41 itens OK | 0 FALHA**.

**Ressalvas/observações de fase (não bloqueiam):**
- Os **134 avisos** de `citacao_literal` refletem o padrão de listra descritiva da série
  (rótulo resolvido por alias); ressalva de fase 1-operador, não erro de conteúdo.
- Correção de autoria na prosa: **Zhu 2019** (metiloma de monócitos, não "Li") e
  **Park 2022** (rede mTOR co-expressa, não "Chen") — 1º autor real do PubMed; PMIDs
  inalterados e on-topic.
- **P-6 pendente:** 2ª verificação **cega e independente** dos claims de ALTO RISCO (Bloco
  H: nós BLOCO_07 e conexões BLOCO_08 HIGH — B3/B5/B2/B12; `uso=clinico` — cetamina,
  NV-5138, rapamicina; evidência humana de direção causal — Jernigan pós-morte, He
  Beclin/LC3A, Gassen FKBP51, Abdallah ECR, Targum ECR; decisões de rejeição — 6 ruídos e
  a contestação Li-vs-Autry) deve ser feita por avaliador distinto (κ inter-avaliador). Na
  fase de 1 operador permanece **PENDENTE**, sem ser maquiada como resolvida.

Contagem final: 134 refs · 134 vínculos · 74 pré-clínicas [ML] · claims de alto risco =
BLOCO_07/conexões BLOCO_08 (2ª verificação cega = P-6).

---

## ADENDO V2 — Fase de Fidelidade Pós-Aplicação (rodada [AT] 2026-09-09, 40 itens novos)

A4-a. Consistência no pacote: tríade atualizada em conjunto (01_pmids 173 · vínculos 173 · ledger 173) — mesmos ids internos em todos, verificado por script (assert tríade).
A4-b. Revisão e limpeza de duplicidades: esummary/elink por PMID contra 134 vigentes; anexos id↔pmid (tabela §3 oficial + parse §6); até aliases GPM↔V1 reconciliados sem dupla contagem (Zhang-d=ZHANG_2023b; Li-2026a=LI_2026; Li-2025=LI_2025b).
A4-c. Leitura estrita antes de integrar: todos os 39 abstracts lidos integralmente; decisões por evidência real (ptypes+MeSH), não por rótulo do insumo.
A4-d. As novelties achadas: confirmação 39/39 existência PubMed; integração na canônica V2 (blocos 14.1–14.5); recusa/adiamento de TUDO quanto fora do eixo: leva N (87 BAIXO) e CAMADA C (28 EXC).
A4-e. Anti-alucinação: 100% dos PMIDs novos resolvidos por eutils; correções integrais (Pich&Millan→Cavalleri; Deyama 2020; Li-obesidade 2022; Sun 2022; Zhang-S6K1 2024; Aguilar-Valles 2021; Chandran 2013; segundo Alcocer; T2DM×CUMS; aliases).
