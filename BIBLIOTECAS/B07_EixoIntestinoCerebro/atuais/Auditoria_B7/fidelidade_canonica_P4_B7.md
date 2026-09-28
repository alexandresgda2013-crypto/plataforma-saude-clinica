# FASE 3 — CHECKLIST DE FIDELIDADE CANÔNICA (P-4, adendo v2.1)
## B7 — Eixo Intestino-Cérebro

**Mini-rodada PRÓPRIA** (Processo de Geração v2.1, item 11 da execução; documento
`04_fase3_auditoria_fidelidade/FASE 3- CHECKLIST FIDELIDADE CANONICA.md`). Relatório item a
item **SIM / NÃO + evidência**. Não corrige — aprova ou devolve.

- **Aplicado por:** operador/IA em sessão dedicada (fase atual = **1 operador**, P-6)
- **Data:** 2026-09-07
- **Biblioteca:** B7 Eixo Intestino-Cérebro — V1 CANÔNICA (8170 palavras)
- **ID canônico:** `mecanismo_B7_eixo_intestino_cerebro`
- **Contagem:** 85 referências (evid_role: {'preclinical_mechanistic': 17, 'human_clinical': 31, 'human_experimental': 7, 'review': 30}) · 40 vínculos N2 · 47 registros de ledger

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
  09"; gate P-5 = refs 85 / vínculos 40; rótulos descritivos de listra
  (estilo `SobrenomeAno_tema`) são o padrão aprovado da série e são resolvidos por alias.
- [x] **A2 — Nada de rejeitado/pendente residual.** **SIM.** Nenhum trecho de claim
  rejeitado/`NAO_LOCALIZADO`/`NAO_SUSTENTA_CLAIM` permanece no corpo; vínculos com
  `status_auditoria` fora do enum oficial = **0**. Itens `[G1]`/emergentes são
  mencionados como não-resolvidos (sem PMID inventado), não como lastro de afirmação.
- [x] **A3 — Zero citação nova na Rodada 3.** **SIM.** Todas as refs com
  `origem_pipeline = BUSCA_FERRAMENTA` e **85/85** com `g1_metodo =
  eutils_automatico` (existência por ferramenta). Nenhuma referência introduzida na
  consolidação sem G1→G3.
- [x] **A4 — Log de reconciliação aplicado integralmente.** **SIM.** Ações de
  remoção/rebaixamento/substituição registradas em `decisoes_B7.md` têm efeito verificável
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
  15/17 refs pré-clínicas com `especie_mesh=["Animals"]` e
  `extrapolacao_por_analogia` marcada; afirmações humanas são lastreadas por refs [EC]/[OB]
  humanas. Dados animais apresentados como mecanismo em modelo, com tradução humana declarada.

## C. RASTREABILIDADE ESTRUTURAL

- [x] **C1 — Mão-dupla texto ⇄ Módulo 09.** **SIM.** Vínculos órfãos (id sem registro) =
  **0**; gate P-5: "refs Módulo09: 85 | vínculos N2: 40".
- [x] **C2 — Vínculos íntegros.** **SIM.** 40/40 vínculos com
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

- [x] **E1 — `g1_metodo` é sempre ferramenta.** **SIM.** 85/85 refs =
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

Contagem final: 85 refs · 40 vínculos · 17 pré-clínicas [ML] · claims de
alto risco = ver BLOCO_07/BLOCO_08 (2ª verificação cega = P-6).

---

# ADENDO V2 — Checklist de Fidelidade Canônica (P-4) revalidado após Rodada [AT] 2026-09-09

Objeto: `B7 EIXO INTESTINO CEREBRO V2 CANONICA.md` (9.356 palavras; 116 refs; V1 arquivada em
producao/historico/v1_canonica_2026-09-09.md). Os 15 itens foram re-avaliados sobre a V2.

- **A1** Identidade/assinatura semântica preservada (BLOCO_00 intacto; título/artefato_rotulo v2) — SIM.
- **A2** Corte/ID canônico/mecanismo_id coerentes (corte 2026-09-09; manifesto rodada 4, versão 2.6) — SIM.
- **A3** Natureza_sistema P12 intacta (sem diagnóstico/prescrição) — SIM.
- **A4** Semantic layer R06 intacta (clinical_summary 3 frases; domains; keywords; related_entities) — SIM.
- **B1** Antialucinação: 31 refs novas todas resolvidas por eutils (G1 192/196 + busca dirigida
  Carabotti; 0 FP; 4 NAO-IDX fora) — SIM.
- **B2** Fidelidade de citação: citações `(Autor Ano)[TAG]` em prosa + listras-resumo; trechos-âncora
  dos 31 novos vínculos são literais e únicos na V2 (verificado por asserção) — SIM.
- **B3** Sem PMID/DOI no texto corrido (varredura \d{7,9} = 0 após fusão) — SIM.
- **C1** Selos honestos: todo conteúdo ML marcado `[APENAS PRÉ-CLÍNICO]`/[EXT] nos parágrafos novos;
  masters humanos (Lin/Zhou/Zhang Q/Tulkens) como ASSOCIATIVOS (B7-CAUSAL-03) — SIM.
- **C2** Regras do domínio: P20 (sem doses/posologia/cortes; nada de posologia probiótica) — SIM.
- **C3** P16: neurogênese não invadida (BLOCO_10 condicional/B16 intacto) — SIM.
- **C4** P19: exames só por ID oficial (bloco 5.x inalterado) — SIM.
- **C5** Escopo da série: EXC expostos (malha pecuária/Alzheimer/Parkinson/EM-EAE/epilepsia/AVC/autismo)
  em relatório; TEPT ≠ depressão ≠ ansiedade preservado — SIM.
- **E1** Tríade coerente: pmids 116 | vínculos 71 (CONFIRMADO) | ledger 78; mesmo conjunto de IDs;
  verificação cruzada executada — SIM.
- **E2** Portões: gate P-5 APROVADO; framework 0 ERRO/0 AVISO; checklist 41/41 — SIM.
- **E3** P-6 declarado PENDENTE (Via 2, avaliador cego, incluindo levas [AT]) em ledger/decisões/
  fidelidade/manifesto/fecho da canônica — SIM.

**Regras novas fixadas na V2 (domínio):** B7-CAUSAL-01 / B7-CAUSAL-02 (guarda-case IPrA/KYNA) /
B7-CAUSAL-03, com formulações protegidas (Erny 2021; Chen N 2024 roedor). GF/germ-free segue
[EXTRAPOLAÇÃO POR ANALOGIA] obrigatória.

Veredito do adendo: **APROVADO COMO CANÔNICA V2** — contagem final: 116 refs · 71 vínculos ·
18 [ML] novas · 4 EC associativas novas · 9 OB novas · P-6 PENDENTE (não bloqueia, declarado).
