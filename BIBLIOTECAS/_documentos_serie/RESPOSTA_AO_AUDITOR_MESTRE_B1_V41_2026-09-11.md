# AO AUDITOR-MESTRE — RESPOSTA À AUDITORIA INTEGRAL B1 CANÔNICA V4.1
**Data:** 2026-09-11 · **Origem:** linha de produção da série mecanística (B1–B16)
**Objeto:** seu veredito **APROVADA COM RESSALVAS** (AUD-026…048; condições R1–R13)

Prezado Auditor-Mestre,

A casa segue a regra que o senhor mesmo exerce: **nenhum achado foi aceito por
declaração — nem o seu, nem o nosso**. Antes desta carta, cada item foi
replicado empiricamente: portões oficiais re-executados, arquivos re-computados
e **PubMed E-utilities ao vivo** (esummary+efetch dos PMIDs pivôs, nesta data).
Segue a posição item a item. Onde o senhor acertou, confirmamos com a mesma
evidência externa que o senhor usou — e corrigimos. Onde erramos na réplica,
dizemos. Onde o senhor errou, provamos com o documento primário.

---

## 1. OS DOIS GRAVE — ACEITOS, REPLICADOS POR EUTILS, E SERÃO CORRIGIDOS (V5)

**AUD-026 (Almulla 2022, §2.10) — ACEITO.** O efetch 36231075 confirma verbatim:
*«Kynurenine (KYN) levels were **unaltered** in severe MDD/BD phenotypes, while
the KYN/TRP ratio showed a significant increase only in patients with psychotic
features (SMD 0.224). Quinolinic acid (QA) was significantly increased (SMD
0.358) and kynurenic acid (KA) significantly decreased (SMD −0.260)»*; graves
com TRP↓ (SMD −0.517) e *«normal IDO enzyme activity but a lowered availability
of plasma/serum TRP to the brain»*. A nossa frase "redução de quinurenina"
inverteu o metabólito — no biomarcador central da biblioteca, no lote [AT].
A sua leitura está exata, inclusive a colateral do §5.2: a elevação de KYN/TRP
no psicótico é **de denominador (TRP↓)**, não de indução de IDO — ambos os
pontos entram na reformulação.

**AUD-027 (Comai 2022, §5.2) — ACEITO.** Título oficial PubMed 34847455:
*«Selective association of cytokine levels and kynurenine/tryptophan ratio with
alterations in white matter microstructure in **bipolar but not in unipolar**
depression»*. A selo [VERIFICADO] sobre uma prosa que apagou o "not unipolar" é
o pior tipo de falha. Correção da prosa + revisão do veredito G3 do vínculo
correspondente, com log de substituição.

**Consequência de versionamento (regra da casa):** correção de conteúdo
científico ⇒ **B1 V4.1 → V5** (versão principal), v4.1 preservada bit a bit,
nunca correção silenciosa.

## 2. MODERADO — ACEITOS (com evidência de replicação)

- **AUD-028:** PubMed 39595067 pubtype = `["Journal Article"]` — o "[OB; revisão]"
  está errado mesmo; a origem no insumo (AUD-043) anotada para o ciclo [AT]. Aceito.
- **AUD-029:** efetch 40036275 (Brain 2025, Validation Study): correlação
  **positiva** significativa in vivo↔pós-morte (n=8, PSP) — resultado
  enunciado na correção; o guarda-chuva [EXTRAPOLADO: PSP→TDM] permanece. Aceito.
- **AUD-030:** efetch 31195092, Methods verbatim: *«A meta-analysis was performed
  **only for CSF and PET studies**»* (69 estudos; pós-morte narrativo 2↑/4).
  Escopo será corrigido; a claim central se mantém. Aceito.
- **AUD-031:** replicação local: o §11.1 já defere ao C-LAB; **a TABELA** não.
  Corte removido da tabela + cross-ref B1.SM02.007 registrada. Aceito.
- **AUD-032:** computado ao dígito — N1 237, ligadas 220, **órfãs 17, idênticas à
  sua lista**; ANNETT_2020 existe apenas na linha-lote do apêndice (zero citação
  no corpo). Aceito (R8: citar com vínculo **ou** remover de N1 — decisão com
  lastro sobre relevância FKBP, documentada em `decisoes_B1.md`).
- **AUD-033:** computado — origem_pipeline N1 = {BUSCA_FERRAMENTA 188, AT 49};
  **89 ausentes de corpus∪log: exatamente o seu número** (47 [AT] com trilha
  própria existente no workspace; **42 BUSCA sem trilha consultável**). R13: o
  log **completo** (não top-10) acompanhará o próximo lote. Aceito.
- **AUD-035:** computado — Lista Canônica: **83 × `em_busca`; zero
  `usado_em_biblioteca`** (Passo 13 pendente). Aceito.
- **AUD-036:** computado — **19 "parcial" sem `g3_nota`; 30 VINC_B1V2 sem
  `claim_id` e sem `achado_referencia`**. O que for recuperável dos vereditos
  será preenchido; o que não for, vira dívida nomeada por vínculo — nada
  fabricado. Aceito.
- **AUD-037:** lido agora — `pmids_total: 184` (real **237**), `meta_analises: 6`
  (real **33**), salto `pipeline_versao_geracao 2.6` sem nota no kit v2.1.
  Manifesto será sincronizado + nota do salto de processo documentada. Aceito.
  (Registro de escopo: os artefatos "não fornecidos" — CHANGELOG, decisoes_B1,
  producao/, antigos/historico/ — **existem**; acompanham o próximo lote.)

## 3. PARCIAIS — aceitos com correção de fatos

- **AUD-034 — omissões CONFIRMADAS, contagem NÃO sustentada.** Os 12 PMIDs que o
  senhor lista estão ausentes de N1 **e** da trilha interna de incorporação
  (`matriz_b1_at_final.json`: 49 entrantes + 19 rejeitados) — ou seja, **sem
  decisão registrada em nenhum artefato da casa**: aceito, e a R5 (decisão item a
  item, com atenção expressa ao sub-bloco suicidalidade — hoje só Sublette 2011
  e Holmes 2018) será executada. **Mas o "36 incorporadas" não fecha com os
  nossos artefatos:** as 49 referências marcadas `ATUALIZACAO_AT_2026-09-08` em
  `origem_pipeline` estão **49/49 em N1** — coerente com o cabeçalho ("49
  incorporadas nesta v4") e com a trilha (49 entrantes). A aparente
  discrepância (propostas 49 ≠ entrantes 49, com ~13 não coincidentes) só se
  resolve com o seu insumo `RECONCILIACAO_B1_INSUMO_CONSENSUS.md`, **que não foi
  preservado pela casa** — pedimos cópia para o fechamento definitivo deste item.
- **AUD-038 — ANO aceito; "abstract existe" REFUTADO.** PubMed 17639827 = *Br J
  Hosp Med (Lond)*, **2007 Jun** — a correção de ano (2005→2007) entra na V5.
  **Mas** o efetch 17639827 retorna o registro **sem abstract** (esummary
  `attributes: []` — "Has Abstract" ausente). A nota do nosso corpo ("SEM
  abstract… não serve de lastro próprio") **não é falsa**: é a realidade do
  registro PubMed hoje. Corrigimos o ano; a ressalva de não-lastro permanece por
  mérito próprio — e o estado N1 (TRIADO/pendente_fulltext) é o correto.
- **AUD-043:** aceito como auditoria do insumo (e já re-ancorado: N1 confirma
  `REF_KAUFMANN_2017` BBI 2017 pmid 28263786 ✓ e Elgellaie **37070163** ✓ — o
  typo e o ano errado nasceram fora do canônico).

## 4. MENOR — aceitos, com UMA refutação completa

Aceitos: AUD-039 (24 títulos divergentes, 0 troca de paper — coerente com a
nossa replicação por amostragem), AUD-041 (citação "()" do §7.2: recuperável
internamente — o mesmo ref é citado nominalmente no §3, *Lang et al., 2025*),
AUD-042 (rodapé METADADOS obsoleto — divergências confirmadas campo a campo),
AUD-044 (registro de re-fidelidade das 53 novas será acrescentado), AUD-045
(linha agregada — corrigida junto ao AUD-031), AUD-046 (sem impacto).

- **AUD-040 — REFUTADO, com prova tripla.** O senhor cita o corpo trazendo
  "a razão KYN/TRP é o biomarcador com a **melhor especificidade** para ideação
  suicida (Sublette et al., 2011)". **Essa frase não existe no artefato auditado
  — e nunca existiu.** Prova: (i) `B1 NEUROINFLAMAÇÃO V4.1 CANONICA.md`, §5.2,
  texto vigente: *«Em tentadores de suicídio com TDM, quinurenina plasmática
  está elevada (Sublette et al., 2011)»*; (ii) `antigos/historico/v4_canonica_pre
  _rodada5_2026-09-11.md` — a v4 original traz o **mesmo** texto (preservação
  bit a bit auditável); (iii) PubMed 21605657, título: *«Plasma kynurenine
  levels are elevated in suicide attempters with major depressive disorder»* —
  o texto vigente é **verbatim-espelho** do título. Pedimos que o senhor
  reconfira a fonte que lhe serviu essa citação — se houver uma linhagem
  paralela do documento, ela não é a canônica.

## 5. OBSERVAÇÕES (AUD-047/048) — aceitas
`redirecionado_clinico` é comportamento de desenho (Processo lin. 50/177); a
ressalva administrativa é justa e vira dívida nomeada: a trilha B1.SM/claim
B1.SM02.007 precisa existir como destino dos redirecionamentos. O lote externo
não cobria `producao/`, `decisoes_B1.md`, CHANGELOG, histórico bit a bit — todos
existem e seguem no próximo lote, junto ao log de busca completo (R13).

## 6. COMPROMISSOS DE CORREÇÃO (mapeamento 1:1 com suas condições)

| Sua condição | Nossa ação | Versão/alvo |
|---|---|---|
| R1, R2 (GRAVE) | reformulação §2.10/§5.2 + vínculos G3 revisado, log de substituição | **Canônica V5** |
| R3 | `g3_nota` dos 19 "parcial" ou reclassificação; `claim_id`+`achado` dos 30 V2 (recuperável; resto = dívida nomeada) | vínculos |
| R4 | Lista Canônica: statuses + `usado_em_biblioteca` a partir dos claim_id mapeados | Lista v1.2 |
| R5 | decisão item a item das 13 (incl. sub-bloco suicidalidade) em `decisoes_B1.md` | decisões |
| R6 | manifesto 237/33 + nota documentada do salto processo v2.1→v2.6 | manifesto |
| R7 | TABELA sem "PCR>3"; cross-ref B1.SM02.007 registrada | Canônica V5 |
| R8 | ANNETT_2020: citar com vínculo **ou** remover — decisão com lastro; 16 órfãs: vínculo ou "contexto" declarado | N1/vínculos |
| R9–R10 (sua ressalva própria) | revisão cega humana dos 59 vínculos de alto-risco: **status canônico provisório declarado** até fechamento | manifesto/rodapé |
| R11 | Gavril rótulo; Wijesinghe positivo (n=8, PSP); Enache "LCR+PET (+revisão pós-morte)"; Hafizi 2007; §7.2 "(Lang et al., 2025)"; **Sublette: nenhuma ação** (AUD-040 refutado) | Canônica V5 |
| R12 | ratificação escrita da exceção de ordem invertida (cond. 2 da sua Fase 1 — pendência real) | decisões |
| R13 | log de busca completo no próximo lote | trilha |

## 7. DOS SEUS PONTOS FORTES — e o que eles mudam

Registramos (e agradecemos) a re-verificação externa 237/237, o 0-hard-fail, a
verificação das nossas correções da sua Fase 1 sem resíduo e a confirmação do
anti-nivelamento. Declarado de nossa parte: o status canônico permanece
**condicional às correções acima** (a executar já) e à revisão cega pendente —
como o próprio pipeline sempre declarou.

Solicitações à sua escrivaninha, para fechamento simétrico:
1. cópia de `RECONCILIACAO_B1_INSUMO_CONSENSUS.md` (fecha o AUD-034);
2. cópia de `b1_anchormap.json` (160 chaves — insumo que a casa não preservou);
3. indicação da fonte da citação AUD-040 (se houver documento paralelo, queremos ratificar qual é o falso).

E, em nome da casa, uma confissão institucional: numa resposta anterior interna
afirmamos que a Lista Canônica B1 não estava no nosso repositório — estava (a sua
própria citação a ela nos fez re-verificar; o erro de rastreio foi de padrão de
busca, "CANÔNICA" com Ô). Registrado no nosso CHANGELOG com rev.1 datada.

Respeitosamente,
**linha de produção — série mecanística** (execução assistida por IA sob liturgia
IMPL-AT-10: CHANGELOG antes/depois · nota datada no artefato · backup · portões
re-rodados · zero correção silenciosa)
