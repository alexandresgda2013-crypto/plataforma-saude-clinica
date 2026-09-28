# FASE 3 — CHECKLIST DE FIDELIDADE CANÔNICA (P-4, adendo v2.1)
## B10 — Desregulação Circadiana

**Mini-rodada PRÓPRIA** (Processo de Geração v2.1, item 11 da execução; documento
`04_fase3_auditoria_fidelidade/FASE 3- CHECKLIST FIDELIDADE CANONICA.md`). Relatório item a
item **SIM / NÃO + evidência**. Não corrige — aprova ou devolve.

- **Aplicado por:** operador/IA em sessão dedicada (fase atual = **1 operador**, P-6)
- **Data:** 2026-09-07
- **Biblioteca:** B10 Desregulação Circadiana — V1 CANÔNICA (7029 palavras)
- **ID canônico:** `mecanismo_B10_desregulacao_circadiana`
- **Contagem:** 39 referências (evid_role: {'preclinical_mechanistic': 10, 'human_clinical': 14, 'review': 15}) · 39 vínculos N2 · 39 registros de ledger

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
  09"; gate P-5 = refs 39 / vínculos 39; rótulos descritivos de listra
  (estilo `SobrenomeAno_tema`) são o padrão aprovado da série e são resolvidos por alias.
- [x] **A2 — Nada de rejeitado/pendente residual.** **SIM.** Nenhum trecho de claim
  rejeitado/`NAO_LOCALIZADO`/`NAO_SUSTENTA_CLAIM` permanece no corpo; vínculos com
  `status_auditoria` fora do enum oficial = **0**. Itens `[G1]`/emergentes são
  mencionados como não-resolvidos (sem PMID inventado), não como lastro de afirmação.
- [x] **A3 — Zero citação nova na Rodada 3.** **SIM.** Todas as refs com
  `origem_pipeline = BUSCA_FERRAMENTA` e **39/39** com `g1_metodo =
  eutils_automatico` (existência por ferramenta). Nenhuma referência introduzida na
  consolidação sem G1→G3.
- [x] **A4 — Log de reconciliação aplicado integralmente.** **SIM.** Ações de
  remoção/rebaixamento/substituição registradas em `decisoes_B10.md` têm efeito verificável
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
  10/10 refs pré-clínicas com `especie_mesh=["Animals"]` e
  `extrapolacao_por_analogia` marcada; afirmações humanas são lastreadas por refs [EC]/[OB]
  humanas. Dados animais apresentados como mecanismo em modelo, com tradução humana declarada.

## C. RASTREABILIDADE ESTRUTURAL

- [x] **C1 — Mão-dupla texto ⇄ Módulo 09.** **SIM.** Vínculos órfãos (id sem registro) =
  **0**; gate P-5: "refs Módulo09: 39 | vínculos N2: 39".
- [x] **C2 — Vínculos íntegros.** **SIM.** 39/39 vínculos com
  `trecho_ancora` não vazio (=**0** vazios), `forca_causal` preenchido
  (=**0** vazios) e `status_auditoria` no enum oficial (=**0** fora). Os
  âncoras são texto literal da canônica (listra ou prosa); o framework reporta
  **39 AVISO(S)** de `citacao_literal` (rótulo descritivo vs. label literal) —
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

- [x] **E1 — `g1_metodo` é sempre ferramenta.** **SIM.** 39/39 refs =
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
(39 avisos não-bloqueantes); checklist de entrega **41/41 itens OK | 0 FALHA**.

**Ressalvas/observações de fase (não bloqueiam o gate; registradas com honestidade):**
- Sem observação de legado estrutural.
- Os **39 aviso(s)** de `citacao_literal` do framework refletem o padrão de listra
  descritiva da série (rótulo `SobrenomeAno_tipo` resolvido por alias); são ressalva de fase
  1-operador, não erro de conteúdo.
- **P-6 pendente:** a 2ª verificação **cega e independente** dos claims de ALTO RISCO (Bloco
  H: nós BLOCO_07 e conexões BLOCO_08 de força HIGH; `uso=clinico`; evidência humana usada
  para causalidade; decisões de rejeição de citação) deve ser feita por avaliador distinto
  quando houver equipe (κ inter-avaliador). Na fase de 1 operador permanece **PENDENTE**, sem
  ser maquiada como resolvida (Bloco P-6 do Processo v2.1).

Contagem final: 39 refs · 39 vínculos · 10 pré-clínicas [ML] · claims de
alto risco = ver BLOCO_07/BLOCO_08 (2ª verificação cega = P-6).

---

# ADENDO V2 — Rodada [AT] 2026-09-09 (P-4 revalidado após fusão GPM externa)

Aplicado em sessão única (1 operador), mesma honestidade P-6: mitiga, não elimina; 2ª verificação
cega segue **pendência de fase**. Contagem pós-fusão: **137 referências** (39 legadas + 98 [AT]),
137 vínculos N2, 137 registros de ledger; canônica V2 ≈ 9.3 mil palavras.

- [x] **A1 — Frase tem lastro.** SIM. 98/98 citações novas `(Autor ano)[TAG]` ocorrem exatamente
  1× na V2 e casam com Módulo 09 por `id_referencia_interna`; vínculos novos com trecho-âncora
  literal 1×; framework 0 ERRO.
- [x] **A2 — Nada de rejeitado/pendente como lastro.** SIM. EXC/preprints/NAO-IDX declarados em
  CONTROVÉRSIAS e decisões, não usados como suporte; [G1] honestos (Satyanarayanan; Mendoza).
- [x] **A3 — Zero citação sem G1→G3.** SIM. Toda ref nova `origem_pipeline=GPM_RODADA_AT`,
  `g1_metodo=eutils_automatico`, G2 e verification_status preenchidos.
- [x] **A4 — Log de reconciliação aplicado.** SIM. decisoes_B10.md registra matriz 98/98/13,
  11 divergências autor/ano/PMID, 2 sobre-correções revertidas, reparos técnicos documentados.
- [x] **B1 — Biomarcadores sem corte/protocolo.** SIM. DLMO/actigrafia/genes-clock seguem como
  pesquisa; Deprato (LAN) classificado como exposição ambiental, não marcador de fase (P20).
- [x] **B2 — Sem medicamento/dose.** SIM. Cronoterapia permanece sinal (Wescott; Campbell);
  melatonina ≠ antidepressivo regra fixada; agomelatina como fármaco do módulo próprio.
- [x] **B3 — Exames por ID oficial.** SIM. Nenhum novo `exame_*` inventado; exposição luminosa
  descrita em prosa sem ID (elemento não catalogado, P19/P20).
- [x] **C1 — ML marcado e extrapolação.** SIM. 27 [ML] com `extrapolacao_por_analogia` SIM e
  `evid_role=preclinical_mechanistic`; inventário negativo 6 regra isso explícito.
- [x] **C2 — Sem PMID/DOI na prosa.** SIM. Varredura `\d{7,9}` = 0 após fusão.
- [x] **C3 — Ansiedade com lastro próprio.** SIM. Cox & Olatunji 2019 [EC] + Francis 2023 [ML]
  endossam o eixo ansiedade independente de insônia; TEPT/depressão não fundidos.
- [x] **C4 — Neurogênese é da B16.** SIM. Nenhum conteúdo de neurogênese adicionado (P16).
- [x] **C5 — Bipolar sinalizado.** SIM. Bloco BLOCO_11.6 novo sempre sinalizado como bipolar.
- [x] **E1 — Malha de escopo.** SIM. Long-COVID (Boiko; Camici), SUD (Serrano-Serrano), diabetes
  (Joseph), neurodegeneração (Başer) → BAIXO; predatórios → EXC.
- [x] **E2 — Anos de print.** SIM. Seis renomeações canônicas documentadas (McCarthy 2022;
  Dollish 2024; Ketchesin 2020; Kinlein 2020; van Dalfsen 2018; Kırlıoğlu 2020).
- [x] **E3 — Tríade sincronizada + portões.** SIM. 137/137/137 mesmo ID-set; gate P-5 ✅;
  framework 0 ERRO (39 avisos legados não-bloqueantes); checklist 41/41 ✅.

**Pendências revalidadas:** P-6 (ampliado às levas [AT] de B1–B16); [G1] Satyanarayanan 2020;
Mendoza 2024/Burns 2023 (NMH); DLMO como desfecho; GRADE.
