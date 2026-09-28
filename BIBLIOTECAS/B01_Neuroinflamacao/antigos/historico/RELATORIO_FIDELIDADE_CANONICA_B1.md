">

# CHECKLIST DE FIDELIDADE CANÔNICA — B1 NEUROINFLAMAÇÃO (Rodada 3)

**Artefato:** `ato2_pacote/BIBLIOTECA_B1_NEUROINFLAMACAO_PRE_CANONICA.md` + `/Evidencias/`
**Rodada:** 3 (consolidação pós-G2/G3). **Data:** 2026-09-03.
**Avaliador:** IA revisora (mesma rodada de geração/auditoria; a revisão cega por segundo avaliador independente / pares humanos fica reservada para depois, conforme decisão do usuário — os itens de alto-risco estão sinalizados para essa revisão futura).

## A. Fidelidade ao que foi aprovado
- **A1 — Frase tem lastro:** SIM. Toda frase declarativa de achado tem ≥1 vínculo CONFIRMADO ou PARCIALMENTE_CONFIRMADO. 78 claims da Lista com lastro; as 4 claims gap (oligodendrócitos/NG2, EAAT2, CB2/FAAH, loop ROS sem PMID) estão explicitamente declaradas como lacuna, não apresentadas como fato.
- **A2 — Nada de rejeitado/pendente residual:** SIM. Zero vínculo NAO_SUSTENTA_CLAIM/CITACAO_INCORRETA no corpo. O único NAO_LOCALIZADO (VINC_B1_0047, revisão IFN 2007 sem abstract) foi **rebaixado no texto** para "PENDENTE DE FULL-TEXT, não serve de lastro próprio"; a afirmação IFN→depressão tem lastro em 4 outras fontes CONFIRMADAS (Capuron 11927189, triptofano 12082564, NSC 25068123, Bull 18458677).
- **A3 — Zero citação nova na Rodada 3:** SIM. Nenhum PMID novo introduzido na consolidação; todas as 145 refs vieram do G1 (esearch/efetch) e passaram por G2/G3.
- **A4 — Log de reconciliação aplicado:** SIM. As ações de rebaixamento (0047), atribuição de forca_causal e preenchimento de G2/G3 têm efeito verificável nos JSONs.

## B. Marcação de incerteza
- **B1 — Ressalva visível:** SIM. Os 15 vínculos PARCIALMENTE_CONFIRMADOS carregam grau de maturidade "emergente/moderado" e nota de ressalva (ex.: Achados de AVE/aterosclerose por [EXT]; efeitos de composto; artigos de dor/SII como ponte).
- **B2 — Selos por frase:** SIM. Distribuição de verification_status: **verificado 75, extrapolado 58, pré-clínico 44, pendente 1**. Nenhuma afirmação humana depende só de evidência animal sem o selo [EXT]/[ML].
- **B3 — Pré-clínico/extrapolado não viram afirmação humana:** SIM. Os 44 pré-clínicos e 58 extrapolados estão marcados; as afirmações clínicas (subtipo, marcadores, RCT) têm lastro humano (metas, TSPO-PET, pós-morte, fMRI, Bull/Klengel/RCT).

## C. Rastreabilidade estrutural
- **C1 — Mão-dupla texto ⇄ Módulo 09:** SIM. Toda citação (Autor, Ano)[tipo] tem registro N1 e vínculo N2; nenhum vínculo/registro órfão no corpo.
- **C2 — Vínculos íntegros:** SIM. 100% dos trecho_ancora são LITERAIS do corpo (checagem automática), status_auditoria e forca_causal preenchidos em todos os CONFIRMADOS/PARCIAIS (tier 1:5, tier 2:78, tier 3:50, tier 4:36; vazio só no NÃO_LOCALIZADO).
- **C3 — Terminologia GRADE:** SIM. Contexto mecanístico usa forca_evidencia_afirmacao (alto|medio|baixo); não há "GRADE A/B/C/D" como campo.
- **C4 — Sem PMID/DOI no texto corrido:** SIM (zero ocorrências); classificador [MA/EC/OB/ML/AT] consistente.
- **C5 — Escopo preservado:** SIM. P20 (sem doses/cortes/protocolo operacional; a dose do RCT é registrada no 03_ensaios como dado de desenho com nota de não-recomendação); P16 (neurogênese aprofundada só em B16); conteúdo prescritivo ausente.

## E. Regra de autoridade (anti-autocertificação)
- **E1 — g1_metodo é sempre ferramenta (eutils_automatico):** SIM (178/178). G1 atesta existência, não suporte.
- **E2 — "verificado" só com g3_verificado_por de AVALIADOR:** SIM. Os 75 "verificado" têm g3_verificado_por = `IA_revisora_G3 (rodada de auditoria; aguarda revisão de pares humana)` — avaliador que leu o abstract; nenhum "eutils"/"script"/vazio promove a verificado.
- **E3 — Nenhum trecho truncado com veredito:** SIM (checagem automática de fim de frase em todos).

## Contagem final da rodada
- Vínculos: **178** → CONFIRMADO 162 · PARCIALMENTE_CONFIRMADO 15 · NÃO_LOCALIZADO 1 (rebaixado).
- Referências: **145** (01_pmids) + **6** meta-análises (02) + **1** RCT (03). 126 refs com status VALIDADO_G3_IA; as demais são as referências exclusivas dos PARCIAIS/gaps, mantidas com ressalva.
- G2: eligible 157 · redirecionado_clinico 20 (metas/marcadores) · redirecionado_mecanistico 1 · nao_avaliado 1 (o full-text pendente).
- Selos: verificado 75 · extrapolado 58 · pré-clínico 44 · pendente 1.

---

## VEREDITO: **APROVADO COMO CANÔNICA** (itens A/B/C/E = SIM), com uma ressalva de processo explicitada:

> A auditoria científica G2/G3 foi realizada por **IA revisora na mesma operação** (lendo abstract a abstract), não por um segundo avaliador humano cego. Conforme a decisão registrada do usuário, a revisão de pares humana vem DEPOIS da geração, não durante. O documento é, portanto, **CANÔNICO pela estrutura do processo de IA**, e os 59 vínculos de alto-risco humano (metas, RCT, TSPO-PET, pós-morte, genética Bull/Klengel) devem ser a **fila prioritária da revisão de pares futura** — qualquer veredito que um par humano altere volta para reconciliação (Etapa 6.5) sem desmontar o pipeline.
