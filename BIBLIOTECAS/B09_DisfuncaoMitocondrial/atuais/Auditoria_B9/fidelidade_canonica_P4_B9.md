# FASE 3 — CHECKLIST DE FIDELIDADE CANÔNICA (P-4, adendo v2.1)
## B9 — Disfunção Mitocondrial

**Mini-rodada PRÓPRIA** (Processo de Geração v2.1, item 11 da execução; documento
`04_fase3_auditoria_fidelidade/FASE 3- CHECKLIST FIDELIDADE CANONICA.md`). Relatório item a
item **SIM / NÃO + evidência**. Não corrige — aprova ou devolve.

- **Aplicado por:** operador/IA em sessão dedicada (fase atual = **1 operador**, P-6)
- **Data:** 2026-09-07
- **Biblioteca:** B9 Disfunção Mitocondrial — V1 CANÔNICA (7211 palavras)
- **ID canônico:** `mecanismo_B9_disfuncao_mitocondrial`
- **Contagem:** 35 referências (evid_role: {'preclinical_mechanistic': 7, 'human_clinical': 17, 'review': 11}) · 35 vínculos N2 · 35 registros de ledger

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
  09"; gate P-5 = refs 35 / vínculos 35; rótulos descritivos de listra
  (estilo `SobrenomeAno_tema`) são o padrão aprovado da série e são resolvidos por alias.
- [x] **A2 — Nada de rejeitado/pendente residual.** **SIM.** Nenhum trecho de claim
  rejeitado/`NAO_LOCALIZADO`/`NAO_SUSTENTA_CLAIM` permanece no corpo; vínculos com
  `status_auditoria` fora do enum oficial = **0**. Itens `[G1]`/emergentes são
  mencionados como não-resolvidos (sem PMID inventado), não como lastro de afirmação.
- [x] **A3 — Zero citação nova na Rodada 3.** **SIM.** Todas as refs com
  `origem_pipeline = BUSCA_FERRAMENTA` e **35/35** com `g1_metodo =
  eutils_automatico` (existência por ferramenta). Nenhuma referência introduzida na
  consolidação sem G1→G3.
- [x] **A4 — Log de reconciliação aplicado integralmente.** **SIM.** Ações de
  remoção/rebaixamento/substituição registradas em `decisoes_B9.md` têm efeito verificável
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
  7/7 refs pré-clínicas com `especie_mesh=["Animals"]` e
  `extrapolacao_por_analogia` marcada; afirmações humanas são lastreadas por refs [EC]/[OB]
  humanas. Dados animais apresentados como mecanismo em modelo, com tradução humana declarada.

## C. RASTREABILIDADE ESTRUTURAL

- [x] **C1 — Mão-dupla texto ⇄ Módulo 09.** **SIM.** Vínculos órfãos (id sem registro) =
  **0**; gate P-5: "refs Módulo09: 35 | vínculos N2: 35".
- [x] **C2 — Vínculos íntegros.** **SIM.** 35/35 vínculos com
  `trecho_ancora` não vazio (=**0** vazios), `forca_causal` preenchido
  (=**0** vazios) e `status_auditoria` no enum oficial (=**0** fora). Os
  âncoras são texto literal da canônica (listra ou prosa); o framework reporta
  **35 AVISO(S)** de `citacao_literal` (rótulo descritivo vs. label literal) —
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

- [x] **E1 — `g1_metodo` é sempre ferramenta.** **SIM.** 35/35 refs =
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
(35 avisos não-bloqueantes); checklist de entrega **41/41 itens OK | 0 FALHA**.

**Ressalvas/observações de fase (não bloqueiam o gate; registradas com honestidade):**
- Sem observação de legado estrutural.
- Os **35 aviso(s)** de `citacao_literal` do framework refletem o padrão de listra
  descritiva da série (rótulo `SobrenomeAno_tipo` resolvido por alias); são ressalva de fase
  1-operador, não erro de conteúdo.
- **P-6 pendente:** a 2ª verificação **cega e independente** dos claims de ALTO RISCO (Bloco
  H: nós BLOCO_07 e conexões BLOCO_08 de força HIGH; `uso=clinico`; evidência humana usada
  para causalidade; decisões de rejeição de citação) deve ser feita por avaliador distinto
  quando houver equipe (κ inter-avaliador). Na fase de 1 operador permanece **PENDENTE**, sem
  ser maquiada como resolvida (Bloco P-6 do Processo v2.1).

Contagem final: 35 refs · 35 vínculos · 7 pré-clínicas [ML] · claims de
alto risco = ver BLOCO_07/BLOCO_08 (2ª verificação cega = P-6).


---

---

# ADENDO V2 — Rodada [AT] 2026-09-09 (reconciliação de insumo externo, P-7)

**Objeto:** `B9 DISFUNCAO MITOCONDRIAL V2 CANONICA.md` (11.176 palavras) — fusão V1(35) → V2(111).
**Incorporação:** 76 refs ENTRA (43 masters GPM + Lu 2024 resgatado + 32 extras auditados),
auditadas ref a ref: G1 eutils 161/161 da fila real do anexo (165 itens; briefing dizia 152),
0 falso positivo, 4 não-indexados confirmados fora, sobreposição V1 = 10, matriz 76/69/6.
**Reaplicado por:** operador/IA (fase de 1 operador — ressalva P-6 mantida e AMPLIADA, ver E/veredito).
**Contagem:** 111 referências (evid_role: {'preclinical_mechanistic': 25, 'human_clinical': 42,
'review': 41, 'human_experimental': 3}) · 111 vínculos N2 · 111 registros de ledger.

## A. FIDELIDADE AO QUE FOI APROVADO (revalidação V2)

- [x] **A1 — Frase tem lastro.** **SIM.** Toda citação `(Autor, Ano)[tipo]` nova (76 refs) casa
  com registro do Módulo 09 por `id_referencia_interna`/`_aliases` e com vínculo N2 cujo
  `trecho_ancora` é texto literal presente **exatamente 1×** na V2 (assert em lote: 111/111
  vínculos). Framework = **0 ERRO**; as citações novas localizam literalmente na prosa (0 aviso
  das levas [AT]); os 35 avisos remanescentes são o padrão de listra-resumo da V1 (ressalva de
  fase, não erro).
- [x] **A2 — Nada de rejeitado/pendente residual.** **SIM.** Os 69 BAIXO e 6 EXC da matriz NÃO
  entram na prosa; os 4 não-indexados (Heyat 2024; Nunes 2025; Niu 2024 preprint; Giménez-Palomo
  2023) ficaram fora e declarados — nenhum `${PMID}` inventado, NAO_LOCALIZADO ou
  NAO_SUSTENTA_CLAIM no corpo; itens `[G1]` permanecem como não-resolvidos (UPRmt humana,
  Mito-Mood).
- [x] **A3 — Toda ref nova passou por G1→G3 nesta rodada.** **SIM.** 76/76 com
  `origem_pipeline = GPM_RODADA_AT`, `g1_metodo = eutils_automatico`, `citacao_confirmada =
  true`, e `g3_verificado_por` preenchido com método (esearch DOI[aid] + esummary + efetch,
  abstract lido); nada promovido automaticamente de G1 (existência) para G3 (suporte).
- [x] **A4 — Log de reconciliação aplicado integralmente.** **SIM.** As 7 fragilidades do
  briefing revertidas estão registradas em `decisoes_B9.md` e no fecho da V2 (Lu 2024 resolvido;
  Triebelhorn 2024 identificado; Mańczak→Reddy 2011; Li→Wang 2018; impressão Scaini 2022 — ID
  mantido; anos de impressão corrigidos; anexo 165≠152) e no manifesto
  (`historico_correcoes`).

## B. MARCAÇÃO DE INCERTEZA (revalidação V2)

- [x] **B1 — Ressalva visível.** **SIM.** Regras fundadoras B9-01..12 e inventário negativo ×10
  fixados em CONTROVÉRSIAS; camadas A–E nomeadas na prosa; fronteiras ilustrativas marcadas
  (Parkinson/OPA1 — Burté/Carelli; manganês — Alaimo; esquizofrenia — Bergman; lúpus — Zong;
  envelhecimento — Wei/Klein); "Mito-Mood" e UPRmt humana como `[G1]`/emergente; transplante/
  intranasal/fitoterápico como "sinal, não terapia".
- [x] **B2 — Selos de verificação por frase.** **SIM.** Leva nova usa [EC] (humano, inclui
  3 human_experimental de células derivadas de pacientes), [OB] (revisão/conceitual) e [ML]
  (pré-clínico); citações novas = prosa `(Autor Ano)[TAG]` unificada sem quebra de linha.
- [x] **B3 — Pré-clínico/extrapolado não viram afirmação humana.** **SIM.** 18 refs [ML] novas:
  17/18 com `especie_mesh` contendo "Animals" (Hofstra 2024 tem MeSH pendente — cross-espécies
  declarado textualmente em `extrapolacao_por_analogia`); todas com
  `g2_elegibilidade = redirecionado_mecanistico` e `verification_status = preclinico`; causalidade
  animal (Dong 2023; Gebara 2020; Hollis 2015; Rosenberg 2023; Watanabe 2022; Xie 2020) sempre
  com [EXTRAPOLAÇÃO POR ANALOGIA]; a prova humana é periférica/associativa (tese 2 mantida).

## C. RASTREABILIDADE ESTRUTURAL (revalidação V2)

- [x] **C1 — Mão-dupla texto ⇄ Módulo 09.** **SIM.** pmids 111 = vínculos 111 = ledger 111;
  ids únicos (111/111); sem pmid duplicado; nenhum vínculo órfão.
- [x] **C2 — Rótulos de listra coerentes com ids.** **SIM (com ressalva de fase declarada).**
  Novos rótulos `SobrenomeAno_tema[TAG]` adicionados às listras de 9 blocos e ao APÊNDICE
  (linha própria com os 76 ids SOBRENOME_ANO[TAG], espelhando o padrão V1); diferenças de rótulo
  resolvidas por `_aliases` (diacríticos incluídos: Burté/Büttiker/Ľupták/Kolár/Giménez-Palomo/
  Valiente-Pallejà/Ulecia-Morón/Fernández-Pech).
- [x] **C3 — Manifesto sincronizado.** **SIM.** `_manifesto_biblioteca.json`: artefato_rotulo
  CANONICA v2; rodada 4; data_corte 2026-09-09; pmids_total 111; g1 (111 resolvidos;
  descartados_auditoria com EXC/BAIXO/não-indexados); g2 (eligible 86 /
  redirecionado_mecanistico 25; evid_role por tipo); g3 (vinculos_n2 111; CONFIRMADO 111);
  palavras_canonica 11.176; versao 2.6; pendencias_fase = P-6 AMPLIADA; trilha
  `producao/04_AT_ciclo_2026-09-09.json` gravada.
- [x] **C4 — Sem PMID/DOI no texto corrido.** **SIM.** Varredura de 7–9 dígitos = **0**
  (executada na fusão e reexecutada na V2); prosa em `(Autor, ano)[tag]`.
- [x] **C5 — Escopo preservado.** **SIM.** P20: zero doses/posologia/cortes; exames por ID
  oficial `exame_*` (9 ids); exames mitocondriais sem ID ficam como papel biológico sem marcador
  diagnóstico; P16: neurogênese permanece remetida a `mecanismo_B16_neurogenese`; malha de escopo
  aplicada nos 6 EXC (autismo, fadiga crônica, diabetes, metanfetamina, demência ×2); TEPT ≠
  depressão ≠ ansiedade preservado. 13 BLOCOs (00–12) presentes: **True**.

## E. REGRA DE AUTORIDADE DOS CAMPOS (revalidação V2)

- [x] **E1 — `g1_metodo` é sempre ferramenta.** **SIM.** 111/111 refs = `eutils_automatico`.
- [x] **E2 — `verificado` só com avaliador.** **SIM.** Leva nova: `verification_status` =
  `preclinico` (18 ML) / `emergente` (58 demais) — nenhuma promoção a `verificado`; `verificador`
  humano/cego continua pendência P-6.
- [x] **E3 — Sem trecho truncado com veredito.** **SIM.** Os 76 `trecho_ancora` novos são texto
  literal com fim de frase, únicos no documento (assert 111/111); o vínculo guarda a citação
  literal `(Autor Ano)[TAG]` e o ledger replica o mesmo trecho.

## VEREDITO (ADENDO)

**[x] APROVADO COMO CANÔNICA V2 — A1–A4 / B1–B3 / C1–C5 / E1–E3 = SIM** nos 3 portões oficiais:
gate P-5 **APROVADO (conteúdo)** · framework **0 ERRO** (35 avisos de legado V1, não-bloqueantes)
· checklist **41/41 itens OK | 0 FALHA**.

**Ressalvas/observações de fase (não bloqueiam o gate; honestidade):**
- Os 35 avisos de `citacao_literal` referem-se somente ao legado V1 (listras descritivas); as 76
  levas [AT] localizam literalmente.
- **P-6 pendente e AMPLIADA:** a 2ª verificação **cega e independente** (Bloco H — nós BLOCO_07,
  conexões HIGH, uso=clinico, decisões de rejeição; e, nesta rodada, MR Lu 2024 ↔ Xue 2026,
  ccf-mtDNA Lindqvist 2018 + SR Fernández-Pech 2026, UPRmt Hofstra 2024, cadeia causal Dong 2023,
  fenótipos F1–F7) permanece **PENDENTE** — sem autocertificação; cobrirá todas as levas [AT]
  de B1–B16 ao fim da rodada (16/16).
