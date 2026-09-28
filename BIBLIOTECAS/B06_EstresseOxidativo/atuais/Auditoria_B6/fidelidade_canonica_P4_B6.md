# FASE 3 — CHECKLIST DE FIDELIDADE CANÔNICA (P-4, adendo v2.1)
## B6 — Estresse Oxidativo

**Mini-rodada PRÓPRIA** (Processo de Geração v2.1, item 11 da execução; documento
`04_fase3_auditoria_fidelidade/FASE 3- CHECKLIST FIDELIDADE CANONICA.md`). Relatório item a
item **SIM / NÃO + evidência**. Não corrige — aprova ou devolve.

- **Aplicado por:** operador/IA em sessão dedicada (fase atual = **1 operador**, P-6)
- **Data:** 2026-09-07
- **Biblioteca:** B6 Estresse Oxidativo — V1 CANÔNICA (7566 palavras)
- **ID canônico:** `mecanismo_B6_estresse_oxidadivo`
- **Contagem:** 36 referências (evid_role: {'preclinical_mechanistic': 4, 'human_clinical': 27, 'review': 5}) · 36 vínculos N2 · 36 registros de ledger

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
  09"; gate P-5 = refs 36 / vínculos 36; rótulos descritivos de listra
  (estilo `SobrenomeAno_tema`) são o padrão aprovado da série e são resolvidos por alias.
- [x] **A2 — Nada de rejeitado/pendente residual.** **SIM.** Nenhum trecho de claim
  rejeitado/`NAO_LOCALIZADO`/`NAO_SUSTENTA_CLAIM` permanece no corpo; vínculos com
  `status_auditoria` fora do enum oficial = **0**. Itens `[G1]`/emergentes são
  mencionados como não-resolvidos (sem PMID inventado), não como lastro de afirmação.
- [x] **A3 — Zero citação nova na Rodada 3.** **SIM.** Todas as refs com
  `origem_pipeline = BUSCA_FERRAMENTA` e **36/36** com `g1_metodo =
  eutils_automatico` (existência por ferramenta). Nenhuma referência introduzida na
  consolidação sem G1→G3.
- [x] **A4 — Log de reconciliação aplicado integralmente.** **SIM.** Ações de
  remoção/rebaixamento/substituição registradas em `decisoes_B6.md` têm efeito verificável
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
  0/4 refs pré-clínicas com `especie_mesh=["Animals"]` e
  `extrapolacao_por_analogia` marcada; afirmações humanas são lastreadas por refs [EC]/[OB]
  humanas. Dados animais apresentados como mecanismo em modelo, com tradução humana declarada.

## C. RASTREABILIDADE ESTRUTURAL

- [x] **C1 — Mão-dupla texto ⇄ Módulo 09.** **SIM.** Vínculos órfãos (id sem registro) =
  **0**; gate P-5: "refs Módulo09: 36 | vínculos N2: 36".
- [x] **C2 — Vínculos íntegros.** **SIM.** 36/36 vínculos com
  `trecho_ancora` não vazio (=**0** vazios), `forca_causal` preenchido
  (=**0** vazios) e `status_auditoria` no enum oficial (=**0** fora). Os
  âncoras são texto literal da canônica (listra ou prosa); o framework reporta
  **36 AVISO(S)** de `citacao_literal` (rótulo descritivo vs. label literal) —
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

- [x] **E1 — `g1_metodo` é sempre ferramenta.** **SIM.** 36/36 refs =
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
(36 avisos não-bloqueantes); checklist de entrega **41/41 itens OK | 0 FALHA**.

**Ressalvas/observações de fase (não bloqueiam o gate; registradas com honestidade):**
- Sem observação de legado estrutural.
- Os **36 aviso(s)** de `citacao_literal` do framework refletem o padrão de listra
  descritiva da série (rótulo `SobrenomeAno_tipo` resolvido por alias); são ressalva de fase
  1-operador, não erro de conteúdo.
- **P-6 pendente:** a 2ª verificação **cega e independente** dos claims de ALTO RISCO (Bloco
  H: nós BLOCO_07 e conexões BLOCO_08 de força HIGH; `uso=clinico`; evidência humana usada
  para causalidade; decisões de rejeição de citação) deve ser feita por avaliador distinto
  quando houver equipe (κ inter-avaliador). Na fase de 1 operador permanece **PENDENTE**, sem
  ser maquiada como resolvida (Bloco P-6 do Processo v2.1).

Contagem final: 36 refs · 36 vínculos · 4 pré-clínicas [ML] · claims de
alto risco = ver BLOCO_07/BLOCO_08 (2ª verificação cega = P-6).


---

## ADENDO V2 [AT 2026-09-08] — revalidação dos 15 itens após reconciliação de insumo externo (P-7)

1. ✅ Citações (Autor, ano)[tag] sem PMID/DOI no corpo (varredura \b\d{7,9}\b = 0).
2. ✅ Toda citação do corpo resolve no Módulo 09 (framework 0 ERRO; 3 órfãs de epub detectadas e corrigidas no ciclo: Banerjee/Sbodio/Pusceddu).
3. ✅ 01_pmids: 108/108 verificados por eutils com abstract; 2 sem abstract no PubMed (Singh 2007; Kannan 2004) → G3 por título/periódico/autor declarado no ledger.
4. ✅ Vínculos N2: 108, todos com trecho_ancora literal presente na canônica V2 e status_auditoria CONFIRMADO.
5. ✅ Ledger: 108 entradas reconciliadas, verificacao preenchida, portões G1/G2/G3 completos.
6. ✅ Selos honestos: 20 refs [ML] com extrapolacao_por_analogia '[APENAS PRÉ-CLÍNICO] —'; observacionais humanos marcados ASSOCIATIVO na prosa; Kato com selo [G1] hipótese.
7. ✅ Negativos/controvérsias preservados e promovidos à regra: Bønaa/NORVIT + Christen/WAFACS como âncoras NEG; polaridade pró-oxidante de B6 (Hu; Ngo) declarada.
8. ✅ Sem extrapolação: causalidade transversal, in vitro→tecido→humano e animal→humano travados por B6.R01–R09; CONTEXT de glutationa sem claim de B6.
9. ✅ P19/P20 intactos: bloco de exames oficiais inalterado; zero dose/posologia/corte nas 6 novas seções; RCTs citados como sondas/sinais, nunca conduta.
10. ✅ Fronteiras respeitadas: B1 (cascata), B4, B8, B9, B16 sem invasão; Parkinson/autismo/Alzheimer/MCI/CV-DM/não-mamífero = EXC expostos.
11. ✅ Estrutura de blocos V1 preservada; inserções apenas aditivas (1.9, 2.4, 3.x, subseções, regras, nota, tabela, apêndice); V1 arquivada.
12. ✅ Tríade e manifesto atualizados no mesmo commit lógico (108|108|108; manifesto v2; trilha producao/04_AT_ciclo_2026-09-08.json).
13. ✅ Relatórios de insumo em producao/insumos/ (auditoria da matriz + execução); baixo incremento (10) e EXC (16) e NAO-IDX (10) documentados.
14. ✅ Falsos positivos: 0; divergências autor/ano do insumo: 0/95; incongruências internas do insumo (contagem 93 vs 106; Kéry/Ereño-Orbea) expostas e resolvidas.
15. ✅ P-6 (2ª verificação cega) registrado como PENDENTE em ledger/vínculos/manifesto/decisoes — não autocertificável.

Veredito P-4 V2: **15/15 SIM — fidelidade canônica mantida na V2.**
