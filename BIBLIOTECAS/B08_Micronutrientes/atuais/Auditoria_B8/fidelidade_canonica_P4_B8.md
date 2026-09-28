# FASE 3 — CHECKLIST DE FIDELIDADE CANÔNICA (P-4, adendo v2.1)
## B8 — Micronutrientes

**Mini-rodada PRÓPRIA** (Processo de Geração v2.1, item 11 da execução; documento
`04_fase3_auditoria_fidelidade/FASE 3- CHECKLIST FIDELIDADE CANONICA.md`). Relatório item a
item **SIM / NÃO + evidência**. Não corrige — aprova ou devolve.

- **Aplicado por:** operador/IA em sessão dedicada (fase atual = **1 operador**, P-6)
- **Data:** 2026-09-07
- **Biblioteca:** B8 Micronutrientes — V1 CANÔNICA (7879 palavras)
- **ID canônico:** `mecanismo_B8_micronutrientes`
- **Contagem:** 96 referências (evid_role: {'human_clinical': 59, 'human_experimental': 15, 'review': 20, 'preclinical_mechanistic': 2}) · 34 vínculos N2 · 38 registros de ledger

> **Escopo da certificação (honestidade P-6).** Aplicado pelo mesmo operador/IA que gerou e
> auditou a biblioteca. O Processo v2.1 (Bloco P-6) declara que, na fase de 1 operador, isso
> **mitiga mas não elimina** o viés de confirmação; a **2ª verificação cega e independente**
> dos claims de ALTO RISCO (Bloco H) é **pendência de fase (P-6)**, não autocertificável.
> Os portões de script (P-5) e o framework de auditoria passaram; abaixo, itens verificáveis
> por artefato.

---

## A. FIDELIDADE AO QUE FOI APROVADO

- [x] **A1 — Frase tem lastro.** **SIM.** Toda citação `(Autor, Ano)[tipo]` e toda listra
  `Label[tipo]` do corpo casa com registro do Módulo 09 (por `id_referencia_interna`,
  `ids_referencia_interna` ou `_aliases`, com normalização de acento) e com vínculo N2.
  Evidência: framework `validar_auditoria.py` = **0 ERRO** de "citação sem entrada no Módulo
  09"; gate P-5 = refs 96 / vínculos 34; rótulos descritivos de listra
  (estilo `SobrenomeAno_tema`) são o padrão aprovado da série e são resolvidos por alias.
- [x] **A2 — Nada de rejeitado/pendente residual.** **SIM.** Nenhum trecho de claim
  rejeitado/`NAO_LOCALIZADO`/`NAO_SUSTENTA_CLAIM` permanece no corpo; vínculos com
  `status_auditoria` fora do enum oficial = **0**. Itens `[G1]`/emergentes são
  mencionados como não-resolvidos (sem PMID inventado), não como lastro de afirmação.
- [x] **A3 — Zero citação nova na Rodada 3.** **SIM.** Todas as refs com
  `origem_pipeline = BUSCA_FERRAMENTA` e **96/96** com `g1_metodo =
  eutils_automatico` (existência por ferramenta). Nenhuma referência introduzida na
  consolidação sem G1→G3.
- [x] **A4 — Log de reconciliação aplicado integralmente.** **SIM.** Ações de
  remoção/rebaixamento/substituição registradas em `decisoes_B8.md` têm efeito verificável
  no texto (refs excluídas não aparecem; correções de rótulo aplicadas nos JSON e no corpo).

## B. MARCAÇÃO DE INCERTEZA

- [x] **B1 — Ressalva visível.** **SIM.** Claims de baixo lastro carregam marcação textual
  (`[G1]`, "emergente"/"fronteira", `[EXTRAPOLAÇÃO POR ANALOGIA]`, `[APENAS PRÉ-CLÍNICO]`),
  nunca nivelados ao muito-estabelecido.
- [x] **B2 — Selos de verificação por frase.** **SIM (padrão da série).** Cada claim leva tag
  de tipo/verificação: **[ML]** = pré-clínico/animal/estrutural, **[EC]** = evidência
  clínica/humana, **[OB]** = revisão/meta; incerteza explícita por `[G1]`/"emergente".
  Mapeia [PRÉ-CLÍNICO]=ML, [VERIFICADO/clínico]=EC, revisão=OB, [EMERGENTE]=[G1].
- [x] **B3 — Pré-clínico/extrapolado não viram afirmação humana.** **SIM.**
  2/2 refs pré-clínicas com `especie_mesh=["Animals"]` e
  `extrapolacao_por_analogia` marcada; afirmações humanas são lastreadas por refs [EC]/[OB]
  humanas. Dados animais apresentados como mecanismo em modelo, com tradução humana declarada.

## C. RASTREABILIDADE ESTRUTURAL

- [x] **C1 — Mão-dupla texto ⇄ Módulo 09.** **SIM.** Vínculos órfãos (id sem registro) =
  **0**; gate P-5: "refs Módulo09: 96 | vínculos N2: 34".
- [x] **C2 — Vínculos íntegros.** **SIM.** 34/34 vínculos com
  `trecho_ancora` não vazio (=**0** vazios), `forca_causal` preenchido
  (=**0** vazios) e `status_auditoria` no enum oficial (=**0** fora). Os
  âncoras são texto literal da canônica (listra ou prosa); o framework reporta
  **0 AVISO(S)** de `citacao_literal` (rótulo descritivo vs. label literal) —
  ressalva de fase **não-bloqueante**, padrão de toda a série (0 ERRO).
- [x] **C3 — Terminologia GRADE.** **SIM.** Sem campo "GRADE A/B/C/D" em contexto
  mecanístico (o hard-fail `GRADE [A-D]` do gate não dispara; usa `forca_evidencia_afirmacao`
  alto|médio|baixo). Menções a "certeza GRADE" de meta-análise clínica, quando existem, são
  domínio de intervenção (R04/Zona clínica), não o campo mecanístico proibido.
- [x] **C4 — Sem PMID/DOI no texto corrido.** **SIM.** Zero PMID numérico (7–8 dígitos) e
  zero DOI no corpo (números de 7–8 dígitos, quando presentes, são códigos de fármacos
  compostos, não PMIDs); classificador [ML]/[EC]/[OB] único por tag.
- [x] **C5 — Escopo preservado.** **SIM.** P20: sem doses/posologia/cortes; biomarcadores por
  ID oficial (`exame_*`); P16: neurogênese remetida a `mecanismo_B16_neurogenese`; conteúdo
  terapêutico prescritivo ausente (fármacos como sinal experimental). 13 BLOCOs (00–12)
  presentes: **True**.

## E. REGRA DE AUTORIDADE DOS CAMPOS (anti-autocertificação)

- [x] **E1 — `g1_metodo` é sempre ferramenta.** **SIM.** 96/96 refs =
  `eutils_automatico` (prova EXISTÊNCIA, não suporte).
- [x] **E2 — `verificado` só com avaliador.** **SIM.** 0 registro(s) com
  `verification_status="verificado"` e `g3_verificado_por` inválido (eutils/script/vazio).
  Refs pré-clínicas = `preclinico`; sem promoção automática G1→G3.
- [x] **E3 — Sem trecho truncado com veredito.** **SIM.** Os `trecho_ancora` são texto literal
  presente na canônica (listra ou frase completa); nenhuma decisão de G3 foi tomada sobre
  trecho sem fim de frase (as diferenças de rótulo são os avisos não-bloqueantes de C2).

---

## VEREDITO

**[x] APROVADO COMO CANÔNICA — itens A1–A4 / B1–B3 / C1–C5 / E1–E3 = SIM**, com evidência
acima e nos 3 portões oficiais: gate P-5 **APROVADO**; framework de auditoria **0 ERRO**
(0 avisos não-bloqueantes); checklist de entrega **41/41 itens OK | 0 FALHA**.

**Ressalvas/observações de fase (não bloqueiam o gate; registradas com honestidade):**
- Sem observação de legado estrutural.
- Os **0 aviso(s)** de `citacao_literal` do framework refletem o padrão de listra
  descritiva da série (rótulo `SobrenomeAno_tipo` resolvido por alias); são ressalva de fase
  1-operador, não erro de conteúdo.
- **P-6 pendente:** a 2ª verificação **cega e independente** dos claims de ALTO RISCO (Bloco
  H: nós BLOCO_07 e conexões BLOCO_08 de força HIGH; `uso=clinico`; evidência humana usada
  para causalidade; decisões de rejeição de citação) deve ser feita por avaliador distinto
  quando houver equipe (κ inter-avaliador). Na fase de 1 operador permanece **PENDENTE**, sem
  ser maquiada como resolvida (Bloco P-6 do Processo v2.1).

Contagem final: 96 refs · 34 vínculos · 2 pré-clínicas [ML] · claims de
alto risco = ver BLOCO_07/BLOCO_08 (2ª verificação cega = P-6).

---

## ADENDO V2 — Rodada [AT] 2026-09-09 (reconciliação de insumo externo, P-7)

Revalidação dos 15 itens após a fusão V1(96)→V2(145). Objeto: `B8 DEFICIENCIAS DE
MICRONUTRIENTES V2 CANONICA.md` (10.007 palavras).

- [x] **A1 — Toda afirmação factual tem fonte.** **SIM.** 83 vínculos (34 vigentes + 49 novos) com
  `trecho_ancora` literal presente 1× na V2; nenhum trecho órfão.
- [x] **A2 — Prosa sem PMID/DOI.** **SIM.** Varredura `\d{7,9}` na V2 = 0; citações em
  (Autor ano)[TAG]; DOIs apenas no Módulo 09.
- [x] **A3 — Selos de espécie honestos.** **SIM.** Nenhum [ML] novo nesta leva (49/49 são
  revisões/estudos humanos/metas); os [ML] vigentes (Sartori; Kemp) permanecem
  [APENAS PRÉ-CLÍNICO]/[EXT]; extrapolação `parcial — revisão mistura espécies` nas revisões com
  MeSH Animals (Wesselink, Cui, Scuto, Faa, Skoczek-Rubińska, Yang, Barks 2021).
- [x] **A4 — P20 (sem doses/posologia/cortes).** **SIM.** Nenhuma dose, faixa de corte ou
  posologia introduzida; números citados são descritivos de estudo (N, OR/HR/IC, I², trim-and-fill).
- [x] **B1 — P16 (neurogênese = B16).** **SIM.** BLOCO_10 inalterado; nenhuma mecânica de
  neurogênese acrescentada (Barks/mattei tratam desenvolvimento, não neurogênese adulta).
- [x] **B2 — P19 (exames por ID oficial).** **SIM.** Nenhum exame novo inventado; `exame_*`
  vigentes cobrem 25(OH)D/DBP-adjacentes (exame_vitd), B12, folato, homocisteína etc.
- [x] **B3 — Malha de escopo.** **SIM.** 12 EXC respeitaram a malha (autismo ×5, neurodegeneração
  ×2, anorexia, epilepsia, delirium, botânica, demência/AVC); TDAH/TEA/psicose/TEPT/neurológicos
  entram apenas como **fronteira ilustrativa** formulação-protegida (CONTROVÉRSIAS).
- [x] **C1 — TEPT ≠ depressão ≠ ansiedade.** **SIM.** Du 2016 citado pela mecânica mitocondrial
  com nota explícita; nenhum desfecho TEPT incorporado.
- [x] **C2 — Rótulos forma/ano por print oficial.** **SIM.** 34 alertas epub-vs-print normalizados
  (Barks 2019; Firth 2017/2018; Ferriani 2022; Lu 2025; Rucklidge 2025; Shayganfard 2022; Eyles
  2013; Skoczek-Rubińska 2025; Nogueira 2023; Freedman; Kumar; Wu).
- [x] **C3 — Inventário negativo preservado e ampliado.** **SIM.** Blocos NEG acrescentados:
  vitamina C (Plevin 2020 — sem estudos de desfecho de reposição), vitamina D (Moroianu 2026 —
  sinais nulos pós trim-and-fill; suplementação de B12 esparsa e nula), Horsdal 2025 (**nulo p/
  TDM**), MRs lidos como ≠ RCT (B8-CAUSAL-03).
- [x] **C4 — Regras causais fixadas.** **SIM.** B8-CAUSAL-01..10 incorporadas verbatim da matriz
  ChatGPT auditada, em CONTROVÉRSIAS, com formulações protegidas (Badar relato de caso;
  fronteiras ilustrativas; ingestão ≠ status; soro ≠ função).
- [x] **C5 — Briefing externo não é verdade por decreto.** **SIM.** 7 erros factuais do briefing
  revertidos e expostos (ver decisoes_B8.md); anexo real = 106 entradas (não 98); 0 FP; 9+1
  não-indexados fora sem inventar fonte.
- [x] **E1 — `g1_metodo` é sempre ferramenta.** **SIM.** 145/145 refs = `eutils_automatico`
  (inclui busca dirigida do Bourre 2006, sem DOI no anexo).
- [x] **E2 — `verificado` só com avaliador.** **SIM.** Novos `verification_status` ∈
  {emergente, preclinico}; nenhum auto-verificado.
- [x] **E3 — Sem trecho truncado com veredito.** **SIM.** Os 49 trechos-âncora novos são
  sentenças/linhas completas variadas da V2 (assert programático de ocorrência única).

### VEREDITO DO ADENDO V2
**[x] APROVADO COMO CANÔNICA V2 — itens A1–A4 / B1–B3 / C1–C5 / E1–E3 = SIM**, com os 3 portões
oficiais pós-fusão: gate P-5 **APROVADO**; framework **0 ERRO / 0 AVISO**; checklist **41/41 OK**.
Contagem final: **145 refs · 83 vínculos · 87 trechos no ledger** · 2 pré-clínicas [ML] vigentes.

**Ressalvas/observações de fase (não bloqueiam; registradas com honestidade):**
- O INFO do gate P-5 ([4b] 5 registros do Módulo 09 sem rótulo em listra: BOTTIGLIERI_2000,
  COPPEN_2000, TAYLOR_2004, COPPEN_2005, BOTTIGLIERI_2005) é **legado da V1** (refs citadas em
  prosa sem espelho em listra-resumo); não-bloqueante, fica para saneamento editorial futuro.
- **P-6 pendente:** 2ª verificação **cega e independente** (Via 2, avaliador distinto) de todos os
  claims de alto risco — agora incluindo os 49 novos (MRs Hui/Lu/Ye; Moroianu; Horsdal; masters
  GPM) — ao fim da rodada 16/16. Permanece **PENDENTE**, sem maquiagem.
