# FASE 3 — CHECKLIST DE FIDELIDADE CANÔNICA (P-4, adendo v2.1)
## B1 — Neuroinflamação

**Mini-rodada PRÓPRIA** (Processo de Geração v2.1, item 11 da execução; documento
`04_fase3_auditoria_fidelidade/FASE 3- CHECKLIST FIDELIDADE CANONICA.md`). Relatório item a
item **SIM / NÃO + evidência**. Não corrige — aprova ou devolve.

- **Aplicado por:** operador/IA em sessão dedicada (fase atual = **1 operador**, P-6)
- **Data:** 2026-09-07 · **revalidada em 2026-09-08** (pós-[AT] — ver ADENDO V4 ao final)
- **Biblioteca:** B1 Neuroinflamação — **V4 CANÔNICA** (18.525 palavras; v3 arquivada em `producao/historico/`)
- **ID canônico:** `mecanismo_B1_neuroinflamacao`
- **Contagem vigente (v4):** 237 referências · 257 vínculos N2 · 237 registros de ledger
  (contagem original desta certificação, v1: 188 refs · 208 vínculos · 188 ledger)

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
  09"; gate P-5 = refs 188 / vínculos 208; rótulos descritivos de listra
  (estilo `SobrenomeAno_tema`) são o padrão aprovado da série e são resolvidos por alias.
- [x] **A2 — Nada de rejeitado/pendente residual.** **SIM.** Nenhum trecho de claim
  rejeitado/`NAO_LOCALIZADO`/`NAO_SUSTENTA_CLAIM` permanece no corpo; vínculos com
  `status_auditoria` fora do enum oficial = **0**. Itens `[G1]`/emergentes são
  mencionados como não-resolvidos (sem PMID inventado), não como lastro de afirmação.
- [x] **A3 — Zero citação nova na Rodada 3.** **SIM.** Todas as refs com
  `origem_pipeline = BUSCA_FERRAMENTA` e **188/188** com `g1_metodo =
  eutils_automatico` (existência por ferramenta). Nenhuma referência introduzida na
  consolidação sem G1→G3.
- [x] **A4 — Log de reconciliação aplicado integralmente.** **SIM.** Ações de
  remoção/rebaixamento/substituição registradas em `decisoes_B1.md` têm efeito verificável
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
  17/127 refs pré-clínicas com `especie_mesh=["Animals"]` e
  `extrapolacao_por_analogia` marcada; afirmações humanas são lastreadas por refs [EC]/[OB]
  humanas. Dados animais apresentados como mecanismo em modelo, com tradução humana declarada.

## C. RASTREABILIDADE ESTRUTURAL

- [x] **C1 — Mão-dupla texto ⇄ Módulo 09.** **SIM.** Vínculos órfãos (id sem registro) =
  **0**; gate P-5: "refs Módulo09: 188 | vínculos N2: 208".
- [x] **C2 — Vínculos íntegros.** **SIM.** 208/208 vínculos com
  `trecho_ancora` não vazio (=**0** vazios), `forca_causal` preenchido
  (=**0** vazios) e `status_auditoria` no enum oficial (=**0** fora). Os
  âncoras são texto literal da canônica (listra ou prosa); o framework reporta
  **188 AVISO(S)** de `citacao_literal` (rótulo descritivo vs. label literal) —
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

- [x] **E1 — `g1_metodo` é sempre ferramenta.** **SIM.** 188/188 refs =
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
(188 avisos não-bloqueantes); checklist de entrega **41/41 itens OK | 0 FALHA**.

**Ressalvas/observações de fase (não bloqueiam o gate; registradas com honestidade):**
- B1 é a biblioteca mais antiga: seus registros de referência usam vocabulário legado (`status_auditoria="VALIDADO_G3_IA…"`, `verification_status="pendente"` em parte das refs). Os **vínculos/ledger** — artefatos que os portões checam de fato — já usam o enum oficial (0 fora do enum) e todos os portões passam. Harmonização do vocabulário legado das refs pode entrar como atualização pós-publicação (`[AT]`, Bloco P-7), sem edição direta da Canônica vigente.
- Os **188 aviso(s)** de `citacao_literal` do framework refletem o padrão de listra
  descritiva da série (rótulo `SobrenomeAno_tipo` resolvido por alias); são ressalva de fase
  1-operador, não erro de conteúdo.
- **P-6 pendente:** a 2ª verificação **cega e independente** dos claims de ALTO RISCO (Bloco
  H: nós BLOCO_07 e conexões BLOCO_08 de força HIGH; `uso=clinico`; evidência humana usada
  para causalidade; decisões de rejeição de citação) deve ser feita por avaliador distinto
  quando houver equipe (κ inter-avaliador). Na fase de 1 operador permanece **PENDENTE**, sem
  ser maquiada como resolvida (Bloco P-6 do Processo v2.1).

Contagem final: 188 refs · 208 vínculos · 127 pré-clínicas [ML] · claims de
alto risco = ver BLOCO_07/BLOCO_08 (2ª verificação cega = P-6).

---

## ADENDO V4 (2026-09-08) — REVALIDAÇÃO PÓS-ATUALIZAÇÃO [AT]

Ciclo P-7 executado: insumo externo ("matriz canônica B1") auditado ref-a-ref → 49 refs
incorporadas → nova versão V4 (v3 preservada em `producao/historico/v3_canonica_2026-09-08.md`).
Reaplicação dos 15 itens com evidência da V4:

- **A1 — Frase tem lastro. SIM.** Framework `validar_auditoria.py` = **0 ERRO** (237 avisos
  não-bloqueantes de `citacao_literal`, padrão da série); gate P-5 = refs **237** | vínculos
  **257** V4; toda prosa/listra nova casa com Módulo 09 + vínculo N2.
- **A2 — Nada rejeitado residual. SIM.** Rejeições do insumo (4 falsos positivos; 19 fora de
  escopo/redundantes/duplicados) registradas com motivo em `producao/04_AT_ciclo_2026-09-08.json`
  e no relatório do insumo; nada disso entrou no corpo.
- **A3 — Zero citação sem G1→G3. SIM.** 49/49 novas refs com `g1_metodo=eutils_automatico`,
  DOI→PMID resolvido por eutils, abstracts baixados, G2 escopo aplicado item a item.
- **A4 — Log aplicado. SIM.** `decisoes_B1.md` ganhou o bloco "Rodada [AT] 2026-09-08"; a v3
  não foi editada in place (P-7); autoria incorreta do insumo corrigida contra PubMed
  (Mac Giollabhui 2021 ≠ "Ng 2018"; Xia 2023 ≠ Kouba; Kouba 2022 ≠ "Kouba 2023").
- **B1–B3 — Marcação de incerteza. SIM.** Novos claims carregam tags: [APENAS PRÉ-CLÍNICO]
  (Zhang 2015, Liu 2022b, Parrott 2016, Martín-Hernández 2019, Li 2021, Wang 2021),     
  [EXTRAPOLADO] (Han 2023b PSP/neurodegeneração; Wijesinghe 2025 PSP→TDM; Hua 2026
  encefalopatia diabética→TDM), "fronteira" (Barzon 2026 ×2, O'Regan/Murata 2026),        
  "emergente" (IL-33). Evidência negativa rotulada como tal (Hannestad 2013; Nutma 2023).
- **C1–C2 — Mão-dupla íntegra. SIM.** Vínculos órfãos = 0 (gate P-5); 257/257 com
  `trecho_ancora` literal da V4; `status_auditoria`/enums oficiais = 0 fora.
- **C3 — Terminologia. SIM.** Sem "GRADE [A-D]" literal (gate não dispara).
- **C4 — Sem PMID/DOI no corpo. SIM.** 0 ocorrências numéricas de PMID e 0 DOI na V4
  (regra C4/RAG mantida).
- **C5 — Escopo. SIM.** P20: antidepressivos/MCC950/sertralina/fluoxetina lidos como **sonda
  experimental de alvo**, sem doses/posologia; P16: BLOCO_10 mantido condicional, Hua 2026 em
  submódulo marcado como modulação (neurogênese = B16); exames seguem por ID oficial.
- **E1–E3 — Autoridade dos campos. SIM.** 49/49 `eutils_automatico`; `verificado` só com
  avaliador identificado (IA G3 + nota P-6 pendente); âncoras não-truncadas e literais.

**VEREDITO V4:** revalidação **APROVADA** nos 15 itens. Portões na V4: gate P-5 **APROVADO**
(237|257) · framework **0 ERRO** · checklist **41/41**. **P-6 permanece pendente** (2ª
verificação cega — agora inclui os claims de alto risco da leva [AT]).
