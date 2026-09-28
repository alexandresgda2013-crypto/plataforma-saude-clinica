# RESPOSTA À AUDITORIA INTEGRAL — B1 CANÔNICA V4.1 (2026-09-11)
## Réplica item a item — regra da casa: nenhum achado aceito sem replicação empírica

**Fonte:** `RELATORIO_AUDITORIA_INTEGRAL_B1_CANONICA.md` (Auditor-Mestre, veredito
**APROVADA COM RESSALVAS**, condições R1–R13).
**Replicação executada nesta sessão:** portões oficiais (gate 16/16, checklist
41/41 B1, framework validar_auditoria B1, contrato do perito), arquivos do
workspace, **E-utilities PubMed ao vivo** (esummary+efetch dos PMIDs pivôs) e o
relatório lido na íntegra. Convenção: ✅ aceito · 🟡 aceito parcial · ❌ refutado.

---

## A. GRAVE — os 2 erros confirmam, e a correção é de conteúdo (→ V5)

### AUD-026 (Almulla 2022, §2.10) — ✅ ACEITO (GRAVE, replicado por efetch)
- Abstract PubMed 36231075, verbatim: *"Kynurenine (KYN) levels were **unaltered**
  in severe MDD/BD phenotypes, while the KYN/TRP ratio showed a significant
  increase only in patients with psychotic features (SMD 0.224). Quinolinic acid
  (QA) was significantly increased (SMD 0.358) and kynurenic acid (KA)
  significantly decreased (SMD −0.260)"*; graves têm TRP↓ (SMD −0.517) e
  TRP/CAAs↓; *"normal IDO enzyme activity but a lowered availability of
  plasma/serum TRP to the brain"* (35 estudos, 4.647 participantes).
- O corpo diz "redução de **quinurenina**" — **invertido**: quem cai é TRP e KA;
  KYN inalterada; QA sobe. Erro de direção de biomarcador no lote [AT] — exatamente
  o risco-máximo de atualização mal re-verificada. **Correta é a R1.**
- Ressalva científica adicional (a ciência decide): a meta TRAZ um achado que a
  correção deve incorporar com honestidade — IDO **normal** com oferta de TRP ao
  cérebro reduzida (por albumina baixa), ou seja, a elevação de KYN/TRP no
  psicótico é de **denominador**, não de indução de IDO. Isso afina o §5.2
  ("inflamação desvia triptofano") na direção que o próprio auditor sugeriu.

### AUD-027 (Comai 2022, §5.2) — ✅ ACEITO (GRAVE, replicado por esummary)
- Título ofic.: *"Selective association of cytokine levels and
  kynurenine/tryptophan ratio with alterations in white matter microstructure in
  **bipolar but not in unipolar** depression"* (Eur Neuropsychopharmacol 2022).
- A prosa rouba a seletividade do paper ("bipolares **e deprimidos**"), com selo
  [VERIFICADO]. **Correta é a R2** (texto + vínculo G3 correspondente).

## B. MODERADO — 11 itens

| # | Veredito | Evidência replicada |
|---|---|---|
| AUD-028 (Gavril 2024 rotulado "revisão") | ✅ | PubMed: pubtype **["Journal Article"]** — estudo original ("Predictive Value of Inflammatory Biomarkers", Biomedicines 2024). A claim em si ("valor preditivo isolado baixo") é sustentada; só a etiqueta [OB; **revisão**] está errada. Origem do erro no insumo (AUD-043) — notado. |
| AUD-029 (Wijesinghe 2025) | ✅ | efetch 40036275 (Brain 2025, *Validation Study*): n=8 PSP; "significant **positive correlation**" BP in vivo ↔ CD68+/TSPO pós-morte; "largely driven by microglia… in tauopathies". Resultado positivo apagado pela prosa ("permanece questão aberta"). Enquadramento [EXTRAPOLADO: PSP→TDM] mantém-se; enunciar o positivo de pequena amostra. |
| AUD-030 (Enache 2019, escopo) | ✅ | efetch 31195092, Methods verbatim: "A meta-analysis was performed **only for CSF and PET studies**, as studies on post-mortem markers…" (69 estudos; pós-morte narrativo: 2↑/4 sem alteração). Claim central OK; corrigir escopo. |
| AUD-031 ("PCR>3" na TABELA) | ✅ | Replicação: §11.1 **já defere** ao C-LAB (correto); a TABELA (linha) traz "~27% com **PCR>3** (OR~1,46)" — violação P20 localizada na tabela. Remover da tabela + registrar cross-ref B1.SM02.007 (origem está declarada no corpo e na Lista — boa prática mantida). |
| AUD-032 (17 refs sem vínculo; ANNETT_2020 só no apêndice) | ✅ | Computado: N1=237, refs ligadas=220, **órfãs=17** — a MESMA lista do auditor. ANNETT_2020: zero ocorrências em prosa; única é a linha-lote do apêndice. Hard-fail "referência isolada" corretamente apontado. |
| AUD-033 (42 refs BUSCA sem trilha) | ✅ | Computado: origem_pipeline N1 = {BUSCA_FERRAMENTA 188, AT_2026-09-08 49}; **89 PMIDs ausentes de corpus∪log — exatamente o número do auditor**, decompondo 47 [AT] (trilha própria em `matriz_b1_at…json` + `RELATORIO_AUDITORIA_MATRIZ_B1.md` — existem no workspace) + **42 BUSCA_FERRAMENTA sem trilha consultável** (log fornecido é top-10). | 
| AUD-034 (13 refs omcidas sem decisão) | 🟡 | **Omissão factual CONFIRMADA:** os 12 PMIDs citados estão ausentes de N1 **e** de `matriz_b1_at_final.json` (entrantes+rejeitados) — sem decisão em nenhum artefato interno. **Mas "36 incorporadas" NÃO se sustenta:** os 49 entrada marcadas `ATUALIZACAO_AT_2026-09-08` estão **49/49 em N1** e o cabeçalho declara 49 — a contagem fina (49 propostas × 49 entrantes com ~13 não coincidentes) exige o `RECONCILIACAO_B1_INSUMO_CONSENSUS.md`, **que não está no workspace** (o auditor o teve; a casa não). Ação: R5 aceita de qualquer forma — decisão documentada por item para os 13, com atenção expressa ao sub-bloco suicidalidade (Sublette+Holmes hoje só 2 âncoras). |
| AUD-035 (Lista Canônica parada) | ✅ | Computado: 83 itens, **83 status `em_busca`, zero `usado_em_biblioteca`** (Passo 13 do processo não executado). A própria Lista EXISTE (Documento 5) — confesso aqui o erro de rastreio anterior do assistente (padrão de busca não casava "CANÔNICA" com Ô): ela está em `02_fase1_gpm_profundidade/7º LISTA CANÔNICA…`. |
| AUD-036 (19 "parcial" sem g3_nota; 30 V2 sem claim_id) | ✅ | Computado: PARCIALMENTE_CONFIRMADO=19, **19 sem g3_nota**; VINC_B1V2_*=30, **30 sem claim_id e 30 sem achado_referencia**. O trabalho pode ter ocorrido — o registro, não. Correto. |
| AUD-037 (manifesto 184/6; pipeline 2.6) | ✅ | Lido agora: `pmids_total: 184` (real **237**), `meta_analises: 6` (real **33** em 02; e já existiam MA dentro de 01 pré-distribuição), `pipeline_versao_geracao: 2.6` sem nota no kit (v2.1). Fonte dupla ambígua — correto. Artefatos referenciados (CHANGELOG, decisoes_B1, producao/…) **existem no workspace** — "não fornecidos" = escopo do lote, não ausência. |
| AUD-038 (Hafizi: ano; "SEM abstract falso") | 🟡 | **Ano: ACEITO** — PubMed 17639827 = Br J Hosp Med, **2007 Jun**; o id/citação "2005" estão errados. **"Abstract existe": REFUTADO** — efetch 17639827 retorna citação **sem abstract** (esummary `attributes: []`); o "SEM abstract… não serve de lastro" do corpo é essencialmente verdadeiro. Resta: corrigir ano (2007), manter a ressalva de não-lastro (ela não é falsa), e o registro N1 TRIADO/NAO_LOCALIZADO como estado real. |

## C. MENOR — 8 itens

| # | Veredito | Nota de replicação |
|---|---|---|
| AUD-039 (24/237 títulos divergentes) | ✅ consistente | Truncamentos/glifos; 0 troca de paper — nas minhas verificações ao vivo (esummary dos pivôs) idem: 0 troca. |
| AUD-040 (Sublette 2011 "melhor especificidade") | ❌ **REFUTADO (duplo)** | A frase citada **não existe** na V4.1 **nem na v4 original** (`antigos/historico/`). Texto vigente: "Em tentadores de suicídio com TDM, quinurenina plasmática está elevada" — que é *exatamente* o título PubMed 21605657 ("Plasma kynurenine levels are elevated in suicide attempters with MDD"). Gambit zero em v4 e V4.1. |
| AUD-041 (citação "()" vazia §7.2) | ✅ | Presente na linha 697. Recuperável: a mesma ref é citada nominalmente no §3 (…) "(**Lang et al., 2025**)[ML; rato/camundongo]" e a âncora de seção traz `NEK7_2025[ML]`. Correção trivial com lastro interno. |
| AUD-042 (rodapé METADADOS obsoleto) | ✅ | Verificado: corte rodapé 2026-05 vs cabeçalho 2026-09-04+[AT]; `clinical_domains` traz `decisao_terapeutica` (semântica oposta ao P20 do próprio rodapé) e diverge do "Domínios: fisiopatologia/biomarcadores/estratificação" do cabeçalho; keywords com "NAC, cetamina inflamatória" (fármaco em biblioteca de mecanismo). Fonte única violada no mesmo arquivo — correto. |
| AUD-043 (erros internos da reconciliação) | 🟡 | Kaufmann: N1 confirma **REF_KAUFMANN_2017**, BBI 2017, pmid 28263786 ✓ (o "2016" é da reconciliação — doc que não está no workspace). Elgellaie: N1 = **37070163** ✓ correto (o typo 37070103 é do insumo). Gavril "revisão" = origem do AUD-028 ✓. Aceita como auditoria do INSUMO; sem efeito no canônico. |
| AUD-044 (fidelidade cobria 184 citações) | ✅ | Cabeçalho confirma a frase; a 5ª rodada re-extraiu as 257 âncoras (mitigação parcial) e esta auditoria + minha replicação (0 troca nos pivôs) convergem — falta só o registro explícito de re-fidelidade autor↔ref das 53 novas; aceito como melhoria de registro. |
| AUD-045 (linha agregada da TABELA) | ✅ | Confirmada a mistura na mesma linha (agregados 4 metas + "27%/OR~1,46" da trilha SM). Corrigida junto ao AUD-031. |
| AUD-046 (Kaufmann journal) | ✅ | N1/âncora coerentes (BBI 2017); sem impacto. |

## D. OBSERVAÇÕES — 2

- **AUD-047:** ✔ aceito como desenho (`redirecionado_clinico` = comportamento previsto, Processo lin. 50/177); a ressalva administrativa é justa: o destino B1.SM não está publicado como trilha — dívida nomeada (o claim B1.SM02.007 existe na Lista Canônica).
- **AUD-048:** ✔ aceito como escopo: os artefatos "não fornecidos" **existem no workspace** (`producao/`, `decisoes_B1.md`, `CHANGELOG_GERAL.md`, `antigos/historico/v4_…`, `RELATORIO_AUDITORIA_MATRIZ_B1.md`, a bancada AT-02, o `fatiador_md.py`). Para o fechamento do AUD-033/048, a casa são envía: log de busca **completo** (não top-10) — item R13.

## E. Dois pontos do lote do auditor que a casa NÃO tem (dívidas nomeadas)
1. **`b1_anchormap.json` (160 chaves)** — o auditor o teve no lote; o workspace não o preserva (coerente com o censo anterior: nenhum anchormap existe aqui). Decidir: preservar cópia como insumo histórico.
2. **`RECONCILIACAO_B1_INSUMO_CONSENSUS.md`** — idem; necessário para fechar a contagem fina do AUD-034.

## F. PLANO DE CORREÇÃO (mapeamento R → execução, na liturgia)
- **R1–R2 (ciência):** reformular Almulla/Comai + vínculos G3 correspondentes → **conteúdo científico ⇒ Canônica V4.1 → V5** (regra de versionamento do operador), com log de substituição + CHANGELOG antes/depois + gate/checklist/framework re-rodados + revisão cega de amostra no diff.
- **R3 (19 g3_nota + 30 claim_id):** metadado — preencher do que os vereditos dos vínculos já trazem, sem inventar (o que não estiver recuperável = dívida nomeada por vínculo).
- **R4:** statuses da Lista Canônica + `usado_em_biblioteca` a partir dos claim_id mapeados (R3 primeiro).
- **R5:** decisão item a item das 13 omissões (inclui sub-bloco suicidalidade) — com critério escopo/G1, registrada em decisoes_B1.md.
- **R6:** manifesto sincronizado (237/33) + documentar salto de processo v2.1→v2.6 (declaração de norma aplicada).
- **R7:** TABELA sem "PCR>3" (deferir ao C-LAB) + cross-ref B1.SM02.007 registrada.
- **R8:** ANNETT_2020: citar com vínculo **ou** remover de N1 (decisão com lastro — checar relevância FKBP); 16 órfãs: vínculos de claim_id correspondente **ou** declaração "referência de contexto" no registro.
- **R10:** revisão cega da fila de 59 — permanece ressalva **provisória** do canonicado (status declarado), a executar fora da IA se o operador quiser especialista humano.
- **R11 (menores textuais):** dentro da mesma V5: Gavril→`[OB; estudo original, humano]`; Wijesinghe→enunciar positivo n=8 PSP; Enache→"meta LCR+PET (+revisão do pós-morte)"; Hafizi→2007; §7.2→"(Lang et al., 2025)". **Sublette: NADA a fazer** (AUD-040 é falso positivo).
- **R12–R13:** ratificação escrita da ordem invertida + nota do salto de processo + log de busca completo a fornecer no próximo lote da perícia.

**Resumo da réplica:** 17 aceitos plenos · 4 parciais · **1 falso positivo completo (AUD-040)** · 2 observações aceitas. Os 2 GRAVE estão **empiricamente confirmados e corrigíveis por reformulação pontual** — nada exige regeneração da biblioteca. A fila está pronta para execução.
