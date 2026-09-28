# FASE 3 — CHECKLIST DE FIDELIDADE CANÔNICA (P-4, adendo v2.1)
## B3 — Neuroplasticidade

**Mini-rodada PRÓPRIA** (Processo de Geração v2.1, item 11 da execução; documento
`04_fase3_auditoria_fidelidade/FASE 3- CHECKLIST FIDELIDADE CANONICA.md`). Relatório item a
item **SIM / NÃO + evidência**. Não corrige — aprova ou devolve.

- **Aplicado por:** operador/IA em sessão dedicada (fase atual = **1 operador**, P-6)
- **Data:** 2026-09-07 · **adendo V2:** 2026-09-08 (rodada [AT], ver ADENDO ao final)
- **Biblioteca:** B3 Neuroplasticidade — **V2 CANÔNICA** (10.206 palavras)
- **ID canônico:** `mecanismo_B3_neuroplasticidade`
- **Contagem (V2):** **165 referências** (evid_role somando a leva [AT]: human_clinical, preclinico_mecanistico, revisao_mecanistica, meta_analise; 112 refs novas) · **165 vínculos N2** · **165 registros de ledger**

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
  09"; gate P-5 = refs 53 / vínculos 53; rótulos descritivos de listra
  (estilo `SobrenomeAno_tema`) são o padrão aprovado da série e são resolvidos por alias.
- [x] **A2 — Nada de rejeitado/pendente residual.** **SIM.** Nenhum trecho de claim
  rejeitado/`NAO_LOCALIZADO`/`NAO_SUSTENTA_CLAIM` permanece no corpo; vínculos com
  `status_auditoria` fora do enum oficial = **0**. Itens `[G1]`/emergentes são
  mencionados como não-resolvidos (sem PMID inventado), não como lastro de afirmação.
- [x] **A3 — Zero citação nova na Rodada 3.** **SIM.** Todas as refs com
  `origem_pipeline = BUSCA_FERRAMENTA` e **53/53** com `g1_metodo =
  eutils_automatico` (existência por ferramenta). Nenhuma referência introduzida na
  consolidação sem G1→G3.
- [x] **A4 — Log de reconciliação aplicado integralmente.** **SIM.** Ações de
  remoção/rebaixamento/substituição registradas em `decisoes_B3.md` têm efeito verificável
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
  12/17 refs pré-clínicas com `especie_mesh=["Animals"]` e
  `extrapolacao_por_analogia` marcada; afirmações humanas são lastreadas por refs [EC]/[OB]
  humanas. Dados animais apresentados como mecanismo em modelo, com tradução humana declarada.

## C. RASTREABILIDADE ESTRUTURAL

- [x] **C1 — Mão-dupla texto ⇄ Módulo 09.** **SIM.** Vínculos órfãos (id sem registro) =
  **0**; gate P-5: "refs Módulo09: 53 | vínculos N2: 53".
- [x] **C2 — Vínculos íntegros.** **SIM.** 53/53 vínculos com
  `trecho_ancora` não vazio (=**0** vazios), `forca_causal` preenchido
  (=**0** vazios) e `status_auditoria` no enum oficial (=**0** fora). Os
  âncoras são texto literal da canônica (listra ou prosa); o framework reporta
  **53 AVISO(S)** de `citacao_literal` (rótulo descritivo vs. label literal) —
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

- [x] **E1 — `g1_metodo` é sempre ferramenta.** **SIM.** 53/53 refs =
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
(53 avisos não-bloqueantes); checklist de entrega **41/41 itens OK | 0 FALHA**.

**Ressalvas/observações de fase (não bloqueiam o gate; registradas com honestidade):**
- Sem observação de legado estrutural.
- Os **53 aviso(s)** de `citacao_literal` do framework refletem o padrão de listra
  descritiva da série (rótulo `SobrenomeAno_tipo` resolvido por alias); são ressalva de fase
  1-operador, não erro de conteúdo.
- **P-6 pendente:** a 2ª verificação **cega e independente** dos claims de ALTO RISCO (Bloco
  H: nós BLOCO_07 e conexões BLOCO_08 de força HIGH; `uso=clinico`; evidência humana usada
  para causalidade; decisões de rejeição de citação) deve ser feita por avaliador distinto
  quando houver equipe (κ inter-avaliador). Na fase de 1 operador permanece **PENDENTE**, sem
  ser maquiada como resolvida (Bloco P-6 do Processo v2.1).

Contagem final: 53 refs · 53 vínculos · 17 pré-clínicas [ML] · claims de
alto risco = ver BLOCO_07/BLOCO_08 (2ª verificação cega = P-6).

---

# ADENDO V2 — revalidação após rodada [AT] 2026-09-08 (P-7)

Revalidados os 15 itens do checklist após a incorporação de **112 referências [AT]** (53→165).
Evidências da rodada: relatório `producao/insumos/RELATORIO_AUDITORIA_MATRIZ_B3.md`, trilha
`producao/04_AT_ciclo_2026-09-08.json`, portões ao final deste adendo.

## A. FIDELIDADE AO QUE FOI APROVADO
- [x] **A1 — SIM.** Toda citação/listra [AT] casa com Módulo 09 (165 regs) e vínculo N2 (165). Framework = **0 ERRO**; gate P-5 refs 165 / vínculos 165.
- [x] **A2 — SIM.** Nenhuma afirmação nova sem lastro: as 112 refs passaram G1 eutils individual (esearch DOI/PMID + esummary + efetch abstracts); 3 correções de autoria do insumo anotadas; 0 falsos positivos.
- [x] **A3 — SIM.** Aprovações anteriores preservadas: rotação V1→histórico (`producao/historico/v1_canonica_2026-09-08.md`); V2 derivada por adição, sem edição in place de conteúdo v1.
- [x] **A4 — SIM.** Rejeições documentadas (33 EXC escopo verificadas por MESH/abstract; 42 baixo incremento; 2 erratas; 8 não-resolvidos com motivo; 5 já vigentes) na trilha AT e no relatório.

## B. FIDELIDADE TÉCNICA
- [x] **B1 — SIM.** BLOCOs 00–12 preservados; 13 BLOCOs exigidos pelo checklist presentes; novos submódulos (1.6, 5.4, BLOCO_03/08 síntese) seguem o padrão prosa+listra.
- [x] **B2 — SIM.** Sem PMID/DOI no texto corrido (C4/RAG) — varredura de 7–9 dígitos = 0; citações `(Autor, ano)[TAG]` e listras `Label[TAG]`.
- [x] **B3 — SIM.** P20 (sem doses/posologia; fármacos como sonda — GLYX-13/N₂O marcados), P16 (neurogênese mantida no escopo B16; refs de neurogênese do insumo rejeitadas por P16), P19 (sem exames novos; bloco 5.x intacto), R04 (`[APENAS PRÉ-CLÍNICO]`/`[EXTRAPOLADO: roedor→humano]` em Schmidt 2010 etc.).

## C. CONTEÚDO
- [x] **C1 — SIM.** TEPT/TCE/AVE/Alzheimer/EM/dor/anorexia/Fragile X mantidos fora (EXC verificadas - inclui **divergência documentada vs. insumo**: Bremner 2008 e He 2018, TEPT-específicos, não entraram pese a indicação do insumo).
- [x] **C2 — SIM.** Controvérsias novas com lastro: B3.C05 (BDNF periférico) formalizada com meta NEG (Calder 2025) + Meshkat vigente; dado negativo humano (Rygvold 2022) incorporado como tal.
- [x] **C3 — SIM.** Estratificação limitada a evidência (farmacogenética Santos 2023 = observacional).
- [x] **C4 — SIM.** Sem conduta/dose; sondas experimentais sinalizadas.
- [x] **C5 — SIM.** Interfaces com B1/B2/B16 creditadas sem colonização (H: inflamação↔plasticidade coordenada com B1; P16 mantido; elo B5 epigenético via Benatti 2024).

## E. ENGAJAMENTO/AUDITORIA
- [x] **E1 — SIM.** Ledger 165 com `verificacao`+`abstract_ou_trecho` (efetch real), origem_entrada `POLITICA_FONTES`, ids AUD_B3_0054–0165 sem duplicidade no Módulo 09 (`04_atualizacoes_literatura.json` = [] após arquivamento na trilha P-7).
- [x] **E2 — SIM.** Claim_ids [AT] no padrão `B3.MEC.BLOCOxx.nnn`; âncoras do ledger = listras de apêndice verbatim presentes na V2 (assert no script de aplicação).
- [x] **E3 — SIM.** G3 declarado = IA (geração); **P-6 (2ª verificação cega) permanece PENDENTE** — leva [AT] entra no pacote Via 2 junto com B1/B2.

## Portões da rodada [AT] (V2)
- `gate_script.py` (P-5): **APROVADO** (165 refs | 165 vínculos; INFO[6] alto risco = ressalva de fase, não bloqueante).
- `validar_auditoria.py` (framework): **0 ERRO** (53 avisos `citacao_literal [TAG]` do bloco vigente — padrão da série, não bloqueante).
- `checklist_entrega.py`: **41/41**.
- Palavras: 10.206 (≥7.000) · período corte: 2026-09-08.

Contagem final V2: **165 refs · 165 vínculos · 165 ledger** · claims de alto risco: BLOCO_07/08 + leva [AT] humana → **P-6 Via 2 PENDENTE** (não autocertificável).
