# FASE 3 — CHECKLIST DE FIDELIDADE CANÔNICA (P-4, adendo v2.1)
## B4 — Monoaminas

**Mini-rodada PRÓPRIA** (Processo de Geração v2.1, item 11 da execução; documento
`04_fase3_auditoria_fidelidade/FASE 3- CHECKLIST FIDELIDADE CANONICA.md`). Relatório item a
item **SIM / NÃO + evidência**. Não corrige — aprova ou devolve.

- **Aplicado por:** operador/IA em sessão dedicada (fase atual = **1 operador**, P-6)
- **Data:** 2026-09-07
- **Biblioteca:** B4 Monoaminas — V1 CANÔNICA (7518 palavras)
- **ID canônico:** `mecanismo_B4_deficiencia_monoaminas`
- **Contagem:** 37 referências (evid_role: {'human_clinical': 29, 'preclinical_mechanistic': 7, 'human_experimental': 1}) · 37 vínculos N2 · 37 registros de ledger

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
  09"; gate P-5 = refs 37 / vínculos 37; rótulos descritivos de listra
  (estilo `SobrenomeAno_tema`) são o padrão aprovado da série e são resolvidos por alias.
- [x] **A2 — Nada de rejeitado/pendente residual.** **SIM.** Nenhum trecho de claim
  rejeitado/`NAO_LOCALIZADO`/`NAO_SUSTENTA_CLAIM` permanece no corpo; vínculos com
  `status_auditoria` fora do enum oficial = **0**. Itens `[G1]`/emergentes são
  mencionados como não-resolvidos (sem PMID inventado), não como lastro de afirmação.
- [x] **A3 — Zero citação nova na Rodada 3.** **SIM.** Todas as refs com
  `origem_pipeline = BUSCA_FERRAMENTA` e **37/37** com `g1_metodo =
  eutils_automatico` (existência por ferramenta). Nenhuma referência introduzida na
  consolidação sem G1→G3.
- [x] **A4 — Log de reconciliação aplicado integralmente.** **SIM.** Ações de
  remoção/rebaixamento/substituição registradas em `decisoes_B4.md` têm efeito verificável
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
  2/7 refs pré-clínicas com `especie_mesh=["Animals"]` e
  `extrapolacao_por_analogia` marcada; afirmações humanas são lastreadas por refs [EC]/[OB]
  humanas. Dados animais apresentados como mecanismo em modelo, com tradução humana declarada.

## C. RASTREABILIDADE ESTRUTURAL

- [x] **C1 — Mão-dupla texto ⇄ Módulo 09.** **SIM.** Vínculos órfãos (id sem registro) =
  **0**; gate P-5: "refs Módulo09: 37 | vínculos N2: 37".
- [x] **C2 — Vínculos íntegros.** **SIM.** 37/37 vínculos com
  `trecho_ancora` não vazio (=**0** vazios), `forca_causal` preenchido
  (=**0** vazios) e `status_auditoria` no enum oficial (=**0** fora). Os
  âncoras são texto literal da canônica (listra ou prosa); o framework reporta
  **37 AVISO(S)** de `citacao_literal` (rótulo descritivo vs. label literal) —
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

- [x] **E1 — `g1_metodo` é sempre ferramenta.** **SIM.** 37/37 refs =
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
(37 avisos não-bloqueantes); checklist de entrega **41/41 itens OK | 0 FALHA**.

**Ressalvas/observações de fase (não bloqueiam o gate; registradas com honestidade):**
- Sem observação de legado estrutural.
- Os **37 aviso(s)** de `citacao_literal` do framework refletem o padrão de listra
  descritiva da série (rótulo `SobrenomeAno_tipo` resolvido por alias); são ressalva de fase
  1-operador, não erro de conteúdo.
- **P-6 pendente:** a 2ª verificação **cega e independente** dos claims de ALTO RISCO (Bloco
  H: nós BLOCO_07 e conexões BLOCO_08 de força HIGH; `uso=clinico`; evidência humana usada
  para causalidade; decisões de rejeição de citação) deve ser feita por avaliador distinto
  quando houver equipe (κ inter-avaliador). Na fase de 1 operador permanece **PENDENTE**, sem
  ser maquiada como resolvida (Bloco P-6 do Processo v2.1).

Contagem final: 37 refs · 37 vínculos · 7 pré-clínicas [ML] · claims de
alto risco = ver BLOCO_07/BLOCO_08 (2ª verificação cega = P-6).

---

## ADENDO V2 — revalidação dos 15 itens após rodada [AT] 2026-09-08 (P-7, insumo externo)

**Objeto revalidado:** `B4 DEFICIÊNCIA DE MONOAMINAS V2 CANONICA.md` (37→131 refs; 9.802 palavras).
Portões: gate P-5 **APROVADO (131|131)** · framework **0 ERRO** (37 avisos = padrão listra da série) ·
checklist **41/41**.

- **A1 (ID/P12):** inalterado; bloco natureza_sistema intacto na V2. **SIM.**
- **A2 (escopo):** EXC tardia Evans 2024 (Alzheimer) prova que o portão pós-abstract funciona; TEPT,
  Parkinson, dor, anorexia, fitoterápicos sem sonda e demais fora-de-escopo barrados (13 EXC). **SIM.**
- **A3 (P16 neurogênese=B16):** intocado; nenhuma ref da leva invade B16. **SIM.**
- **A4 (P19 exames por ID oficial):** nenhum exame novo introduzido; BLOCO_05 preservado. **SIM.**
- **B1 (G1=eutils):** 94/94 novas refs com `g1_metodo=eutils_automatico`, DOI/PMID resolvidos,
  8 resgates full-DOI documentados. **SIM.**
- **B2 (G2 espécie/elegibilidade):** especie_mesh e desenho derivados de MeSH; overrides OB
  justificados por pubtype/resenha (9 casos documentados). **SIM.**
- **B3 (G3 por vínculo):** 131 vínculos trecho-âncora; 5 refs sem abstract têm G3 por
  título/periódico/autores, explicitado no ledger. **SIM.**
- **C1 (sem PMID no texto corrido):** varredura `\b\d{7,9}\b` = 0 na V2. **SIM.**
- **C2 (rótulos canônicos):** corpo TitleCase `Sobrenome_Ano[TAG]`, apêndice UPPERCASE; 94 rótulos
  novos presentes nos dois planos (assert de script). **SIM.**
- **C3 (R04 pré-clínico):** 14 refs [ML] carregam `[APENAS PRÉ-CLÍNICO]`/`[EXTRAPOLADO: animal→humano]`
  na prosa e `extrapolacao_por_analogia` no Módulo 09. **SIM.**
- **C4 (P20 sem conduta):** zero doses/posologia; depleções descritas como **sonda experimental**;
  fármacos citados apenas como alvo/sonda (levodopa=Bekhbat, reserpina=historiografia). **SIM.**
- **C5 (controvérsias atualizadas):** disputa serotonina mantida sem lado (Moncrieff×Jauhar já vigentes)
  + regras B4.R01–R08 fixadas. **SIM.**
- **E1 (ferramenta > memória):** 2 correções de autoria do insumo provadas por efetch; Vetulani=170534. **SIM.**
- **E2 (verificado só com avaliador):** `g3_verificado_por` da leva = "IA G3 (geração) … P-6 … PENDENTE". **SIM.**
- **E3 (sem veredito sobre trecho truncado):** abstracts efetch completos; editoriais sem abstract
  sinalizados, não inferidos. **SIM.**
- **P-6:** **PENDENTE** (2ª verificação cega, Via 2 — pacote alto-risco B1–B16 incluirá a leva [AT] da B4).
  Não há autocertificação. **SIM (registrado como pendência honesta).**

**Veredito:** B4 V2 **APROVADA COMO CANÔNICA (revalidada)** — 15/15 itens SIM, com P-6 pendente declarado.
