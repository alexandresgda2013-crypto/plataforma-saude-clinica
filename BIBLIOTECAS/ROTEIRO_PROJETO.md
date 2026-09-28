# ROTEIRO DO PROJETO — o que já foi feito e o que falta
**Atualização mais recente: 2026-09-13 (rodada de re-auditoria do Auditor-Mestre, ciclo fechado)**
*(bloco anterior: 2026-09-11, noite — pós-distribuição Módulo 09)*

> **2026-09-13 — Re-auditoria do Auditor-Mestre sobre a B1 V5 processada por inteiro:**
> replicadas F-01…F-10 nos nossos arquivos (confirmadas; 2 variações de contagem documentadas na carta);
> executado o reparo de coerência dele (trilha 15; manifesto final idêntico ao dele); trilhas próprias 16
> (2 re-ancoragens finas) e 17 (**rename factual REF_HAFIZI_2005→2007** — ano vinha do nome NLM do
> periódico; eutils: pub 2007). Confissão C1 (propagação nossa) registrada. Ferramentas F-08/F-09
> consertadas na casa (checklist relativo a `__file__`; gate com docstring honesta → P-8) — os arquivos
> corrigidos dele não vieram anexados; aplicamos o equivalente descrito. **Varredura série (2.689 fichas):
> 1 caso-idêntico resolvido (B13 Saito 1999→2010, rito completo); 3 epub×print viram dívida de convenção
> D-SERIE-CONVENCAO-ANO-ID.** Portões: gate OK · checklist 41/41 · framework 0 ERRO · **P-8 4 ERRO
> (0261/0262/0265/0266 → fila humana de especialista) / 24 avisos** · censo 32/32 BLOQ 0.
> **Descoberta:** P-8 na B13 = 167 ERRO V-02 — as demais 15 bibliotecas precisam do mesmo ciclo de
> reancoragem da B1 (entra no plano abaixo). Carta-resposta: `_documentos_serie/RESPOSTA_REAUDITORIA_AUDITOR_MESTRE_2026-09-13.md`.
> Próximos marcos (ordem da Parte IV do plano dele): etapa 0 — C3 Osimo [AT] + C4 (autor); 1 — Contrato
> do Motor Clínico (L-05) + precedência (L-06), maior risco do projeto; 2 — ontologia mínima (L-04);
> 3 — schemas NT/JSON (L-01/02/03); 4 — gerar NT-B1/JSON-B1; 5 — portões round-trip + não-elevação
> epistemológica; 6 — mini-bibliotecas; 7 — caso clínico sintético auditado frase a frase; 8 — CI+série.
> **Marco de decisão vigente: replicar para as demais só quando 100% das frases do relatório sintético
> forem rastreáveis à frase canônica com P-5, P-8 e portão de saída verdes.**

> **Mesma data, bloco 3 — Distribuição Módulo 09 executada (pedido do operador):**
> `02_meta_analises.json` (272 fichas) e `03_ensaios_clinicos.json` (64) preenchidos
> nas 16 bibliotecas a partir do `01_pmids.json` (lei PROMPT v4.2 [MA]→02/[EC]→03,
> especificada na geração e nunca executada); 293 ponteiros `arquivo_modulo09` dos
> ledgers reconciliados (framework pegou → corrigido → framework 0 ERRO ×16).
> Consolidado do motor clínico em `BIBLIOTECAS/MOTOR_CLINICO/` (MA 268 + EC 58
> dedup-PMID, `bibliotecas[]`). Portões pós-mudança: gates 16/16 · checklists
> 41/41 ×16 · framework 0 ERRO ×16 · contrato 0 bloq ×32. Ciência: 0 linhas.
> Dívidas nomeadas: 390 refs tag-[EC]-amplo sem sinal RCT (não migraram; ratificação),
> 27 conflitos tag×título [REVISAVEL], `forca_evidencia_afirmacao` vazio nas migradas.
*Documento vivo: números sempre computados de arquivo; cada mudança também no `CHANGELOG_GERAL.md`.*

> **Delegação vigente (operador, 2026-09-11):** "sobre as âncoras, ou qualquer outro
> ajuste, quero que a IA faça — tudo o que tem de material da ciência e da engenharia
> está disponível para todos, inclusive para a IA. Eu participo lembrando das
> ferramentas, leis e regras; avaliação de especialista, se quiser, só no final."

---

## REGRA DE VERSIONAMENTO (vigente desde 2026-09-11)

| Tipo de mudança | Versão | Precedente |
|---|---|---|
| Pequena (metadado, rótulo, âncora, registro) | Sobe o ponto: `V4 → V4.1 → V4.2…` | Canônica B1 `V4 → V4.1` |
| Conteúdo científico | Sobe o principal: `V4 → V5` | (a ocorrer) |

Sempre: versão anterior em `antigos/historico/` (data no nome) · nota datada dentro do artefato · CHANGELOG antes e depois.

---

## ESTADO FINAL DO DIA ✅

**Contrato da perícia: 16/16 bibliotecas × vínculos × ledgers = 0 bloqueantes.**
**Portões: 16/16 gates ✅ · checklists de entrega 41/41 ✅ · framework de fidelidade 0 ERRO ✅**
**Ciência: zero linhas alteradas nas 16 Canônicas** (a única edição de prosa da série
segue sendo a linha §6.2 da B1, da rodada 5 — versionada V4.1).

---

## PARTE 1 — O QUE JÁ FOI FEITO ✅

### Base (até 10/09)
- 16/16 bibliotecas canônicas entregues (B1–B16) · 5 rodadas de perícia replicadas e respondidas.
- B1: 257/257 âncoras 100% literais · AT-02/AT-13 fechados · AT-11 · gate oficial corrigido.
- Política de versionamento formalizada e aplicada (V4.1).

### 2026-09-11 — Harmonização de contrato (2.594 reparos de metadado, 13 bibliotecas)
| Item | Bib | Resultado |
|---|---|---|
| **AT-01** | B1 | 27 `natureza_relacao` por conteúdo (teto por tier, tabela id-a-id na trilha) + 237 status legados→oficiais. **FECHADO** |
| **AT-03** | B7 | 31 assinaturas G3 separadas de método + natureza ×11 + grau ×17. **FECHADO** |
| **AT-04** | B8 | 49 assinaturas G3 + natureza ×16 + grau ×53. **FECHADO** |
| **AT-12** | B7/B8 | 106 forca_causal híbridas decompostas lossless → tier oficial + **`desenho_evidencia`** novo. **FECHADO** |
| Fila B | B3–B6, B9–B13 | 1.496 conversões status (D1), 346 evid_role (D2), 150 verification_status campo-trocado (D6), 118 g2 (D7). **FECHADO** |

### 2026-09-11 — Âncoras (135 reancoragens/notas)
| Item | Bib | Resultado |
|---|---|---|
| **AT-05** | B2 | 14 re-extrações + status ×84; depois a fila (abaixo). **FECHADO** |
| Literalidade | B6/B7/B8 | 8 reparos (lote→prosa ×3, fuzzy-lit ×5). **FECHADO** |
| Fila de confirmação (**delegada → executada pela IA**) | B2/B6/B7/B8/B12 | **97/97 resolvidos**: 94 por score achado+título da ref (desempates `diretoria` documentados com scores), 3 ao ÍNDICE-DE-CORPUS (LEE_2025/HARTMANN_2024/MULLER_2000 — sem claim na prosa, verificado eutils; observação registrada). Rev.1 própria: VINC_B2_026 (stub→frase-claim, pega pelo checklist). |
| **AT-13b** (**delegada → executada**) | B1 | 6 RE-ANCORAR aplicados + 6 co-citações confirmadas legítimas. **FECHADO** |
| B12 (Etkin) | B12 | resolvido na fila. **FECHADO** |

### 2026-09-11 — Decisões de schema (nomeadas, sem invenção de dado)
- **D9:** 1.541 ids legados de 3 dígitos legitimados (`\d{4}` só p/ novos); aviso nomeado no instrumento.
- **D7:** B13 `nao_aplicavel` ×49 = extensão declarada no manifesto.
- **F1:** B14–B16 sem campos de verificação — lacuna de arquitetura documentada; recomendação: reprocessamento assistido (SCHEMA v2/perícia).

### 2026-09-11 — Entregáveis de engenharia
- `fatiador_md.py` (markdown-aware, round-trip 99,3%) — substitui o fatiador condenado.
- `RODADA2_PACOTE_PERICIA/` — 3 escritores **blindados** com contrato.py (bug D1 corrigido na fonte) · autoteste **6/6** · round-trip no B1 vivo: **0 novo, 0 bloqueante, 0 aviso** · 97 scripts série AT · contrato.py intocado · README.
- `SCHEMA_V2_PROPOSTA_2026-09-11.md` (P1–P10 p/ ratificação) · `DECISOES_HARMONIZACAO_SCHEMA_2026-09-11.md` · trilhas `producao/06_*`–`08_*` · `OBSERVACAO_REFS_SEM_CLAIM_B02…md`.

---

## PARTE 2 — O QUE FALTA 🔧 (nesta ordem)

1. **Dia a dia da plataforma:** nada pendente de bloqueio — qualquer nova rodada de conteúdo científico entra pela liturgia padrão (+1 versão principal, se for o caso).
2. **Quando o operador acionar (ratificação externa, não-bloqueante):**
   - Enviar `RODADA2_PACOTE_PERICIA/` + `SCHEMA_V2_PROPOSTA…md` à perícia;
   - Se P2 ratificado: re-aplicar `refutadora` nos 13 vínculos (trilha id-a-id pronta).
3. **Revisão de conteúdo no final da plataforma (só se o operador quiser especialista):**
   - REF_LEE_2025 / REF_HARTMANN_2024 (existem, são válidas, mas sem claim na prosa B2 — decidir incorporar ou realocar);
   - Linhas **[REVISAVEL]** das trilhas (meta_análise→human_clinical ×15, incipiente→emergente ×27, PARCIAL→TRIADO ×13, refutadora ×13, VINC_B7_034/B8_033, 4 empates `diretoria` da resolução de âncoras — todos com scores e alternativas registradas).
4. **P-6 Via 2 formal** (2ª verificação cega de amostra das levas [AT]) — disciplina já executada na prática; passe cego formal a agendar.

---
*Liturgia permanente: ciência primeiro · zero extrapolação (o que não é decidível com prova vira dívida nomeada, nunca dado fabricado) · CHANGELOG antes/depois · nota datada no artefato · backup · portões re-rodados · versionamento.*

---

### 2026-09-12 — R1–R13 encerradas; antes dos itens da PARTE 2, o próximo ato do projeto
0. **Lote de re-auditoria B1 V5 ao Auditor-Mestre** (aguarda acionamento do operador): canônica V5 + manifesto sincronizado + vínculos (273) + ledger (236) + Lista v1.2 + decisoes_B1.md rev.3 + `producao/insumos/matriz_b1_at_final.json` + trilhas `producao/10…14_*` + censo_pos_R1_R13 + declaração das dívidas de insumo (anchormap não preservado · log de busca completo = D-B1-R13-LOG) + lista dos 59 + instrumento da revisão cega. Próximo ciclo de conteúdo: **[AT] R5** — 10 PMIDs aprovados entram pelo rito G1+G3 (prioridade: sub-bloco suicidalidade §5.2), 2 motivadamente fora.

### 2026-09-13 (rodada 2) — Etapa 0 do parecer do Auditor-Mestre FECHADA na piloto (B1 V6)
- **Feito hoje:** 4 scripts oficiais instalados verbatim (conferência bilateral, backups) · [AT] C3 Osimo
  2019 aplicado (ficha 34, VINC_B1_0274, AUD_B1_0238, prosa §11.1 re-ancorada ao limiar de PCR) · C4
  BLOCO_11.4 (não-validação + circularidade do Critério C) · 4 re-ancoras homônimas decididas com ciência
  (trilha 18 rev.1 — sufixo de ano; confissão da ida-e-volta) · **B1 CANÔNICA V6** (sha d8f41662…, V5 no
  histórico) · P-8 piloto **0 ERRO V-02** (critério de replicação, 1ª metade) · réplica da tabela §4 dele:
  15/16 exatas (única diferença = B01 pré/pós-V6, aritmeticamente fechada).
- **Delegação do operador registrada:** método decidido pela casa com ciência+engenharia (datado, com
  trilha); equipe humana de especialistas revisa NO FIM (P-6 permanece).
- **PRÓXIMO ATO (ordem do parecer dele, aceita):** pacote de schema **L-05 Contrato do Motor Clínico +
  L-06 precedência entre bibliotecas + L-13 `achado_verbatim_fonte`** (maior retorno); L-17 entra junto
  (schema único de manifesto). Em paralelo (mecânico): reancoragem série — **só replicar quando mais uma
  biblioteca fechar 0 ERRO V-02** (B01 já fechou hoje). Fila de prioridade da série medida e guardada em
  `_documentos_serie/replicacoes/2026-09-13_P8_serie/`.
- **Carta nº 2 ao auditor:** `_documentos_serie/RESPOSTA_2_REAUDITORIA_AUDITOR_MESTRE_2026-09-13.md`.

### 2026-09-13 (rodada 3) — Parecer V6 processado; B1 V7 (sha 6e2c2979…)
- **Feito hoje:** réplica do §3 (trilha 21 — 7/7 autodivergentes exatas; achado taxonomia confirmado) ·
  **C4 decidida no algoritmo** (C vira modificador de a priori/especificidade; regra de rebaixamento
  executável; caso-armadilha obesidade+apneia não classifica mais 'alta') · AUD-066 (PROVISÓRIO ← fila
  operacional 108/91) · AUD-067 por eutils (Mehta 2020b = RS, não MA — ficha, ledger, tokens, duplicata;
  MAs 34→33) · L717→2020b por eliminação (vínculo N2 no P-6) · semântica da taxonomia declarada
  (correção material no L-05/1.2; **V-15 aceita**) · portões V7 todos verdes · carta nº 3 + pacote-zip V7.
- **PRÓXIMO ATO — BLOCO 1 do parecer (aceito):** (1.1) **Contrato do Motor Clínico (L-05)** → (1.2)
  **taxonomia única de desenho/força + V-15** (resolve o §3; fila nomeada: 6 autodivergentes restantes +
  ~84 divergentes da trilha 21) → (1.3) precedência L-06 → (1.4) `achado_verbatim_fonte` (L-13; piloto:
  as 33 metas da B1) → (1.5) C4 — **já cumprida**. Depois: Bloco 2 (SCHEMA-NT + NT-B1 + SCHEMA-JSON +
  JSON-B1), Bloco 3 (recortes mínimos), Bloco 4 (teste do motor — com determinismo e caso-armadilha).
- **Série (§7 dele, aceito):** reancoragem vira **script** construído sobre as trilhas 15–18/22; B13 é
  a "mais uma" do critério de replicação (167 ERRO V-02 medidos).

### 2026-09-13 — rodada 5 (Auditor-Mestre: pacote V6 verificado) — aceites que afetam a fila
- **AUD-066 encerrado** e **camada de evidência encerrada** (dois impedimentos a menos). C4 fecha quando a V7 chegar a ele (pacote V7c entregue junto com a carta 4).
- **V-15 e V-16** entram na fila de portões do lado dele; V-16 já replicada e já aplicada por errata no manifesto 2.9 (trilha 24).
- **B13 = primeira execução do reancorador de série**, que será escrito ANTES de tocar a B13 (critério dele, aceito — nada de piloto manual artesanal). Sequência da série: escrever reancorador (base trilhas 15–18/22) → B13 → demais 14.
- **Próximo ato inalterado (Bloco 1):** L-05 Contrato do Motor (1.1) → taxonomia única de desenho/força + V-15 (1.2) → L-06 precedência (1.3) → L-13 `achado_verbatim_fonte` (1.4; piloto = 33 MAs da B1).
- **Dívidas incrementadas nesta rodada:** D-B1-R4-TOKENS (11 ambíguos + 3 temáticos + 2 grafias-duplas — linhas exatas na trilha 24 rev.1) ao pacote L-05/1.2; fila P-6 ganha os 3 casos nomeados pelo gate rev.A2 (VINC_B1_0038, VINC_B1_0232, VINC_B1_0047).

### 2026-09-15 (rodada 9) — ARQUITETURA CONSOLIDADA publicada pelo operador; Bloco 1 re-enquadrado
- **Documento normativo recebido** (arquivado verbatim em `_documentos_serie/`): cadeia oficial
  **Biblioteca → NT → Ontologia/Grafo → JSONs → Motor → Laudo** + **Pasta de Atualização** paralela
  (ciência recente; nunca equiparada ao canônico) + regra "necessidade estrutural = problema de
  contrato, nunca remapear a ciência da B1". **[Atualização no mesmo dia: a referência vigente é a
  V2 — sha `09692e18…` (a V1, sha `8f050469…`, foi SUPERSEDED_; ponteiro `ARQUITETURA_VIGENTE.txt`).
  A V2 redesenha o diagrama com EVIDÊNCIAS BIBLIOGRÁFICAS → VÍNCULOS marcados "L-05 N1 + N2", cria
  a §7 LIMITES DA NT (incl. "não converter relação mecanística em eficácia clínica sem sustentação" —
  adotada no L-NT) e adiciona as seções de programa §26–§29: piloto B1 vertical, expansão
  multidomínio, motor construído CONTRA os contratos (Biblioteca não é camada final de consumo) e
  divisão de responsabilidades entre agentes. Diff V1→V2 verificado linha a linha; §7 entra como
  regra do futuro portão V-NT.]**
- **Verificação da casa (computada hoje):** 146 IDs **exato** (151 − 5 removidos; **errata nossa: o
  "103" da trilha 25 era parse parcial**) · constantes de segurança do motor **já oficiais** no
  cabeçalho do catálogo · evidência-única/âncora-múltipla = 4ª convergência independente · **Pasta de
  Atualização e NT ainda não existem** como artefatos — exigem contratos novos (**L-PU**, **L-NT** +
  portão **V-NT**). Relação §10 converge com o R7; colisão de nome nomeada (`direção`-grafo ×
  `direcao`-epistêmica → `sentido_relacao` × `direcao_suporte`).
- **PRÓXIMO ATO re-enquadrado:** a minuta **L-05 1.1** passa a ser o **Contrato da Cadeia** (leitura
  em dois tempos: derivação = 4 superfícies da B1; execução = pacote §16/§20 do documento) + **L-06**
  (precedência; fonte normativa = §21) + anexos **L-NT/V-NT/L-PU**. **Material inalterado:** taxonomia
  = primeiro item (1.2), régua V-15 (94 ERRO, dívida nomeada); regra de risco R-A: NT-piloto ancora
  marcadores **só via fichas+vínculos** até o 1.2.
- **Portões re-rodados hoje:** gate rev.A2 APROVADO · 41/41 · framework 0 ERRO/236 · P-8 (16) 94
  ERRO/207 (dívida nomeada) · V-16 4/4. Ciência: 0 linhas; sha V7 `6e2c2979…` intacto.
- **Carta nº 6 ao Auditor-Mestre:** `_documentos_serie/RESPOSTA_6_ARQUITETURA_CONSOLIDADA_NT_PRE_MOTOR_2026-09-15.md`
  (cópia auditor-2). Pendências: delimitador P-8 (94→91) · v1.1 do schema (R1–R7) · P-6 permanece.
- **[Mesmo dia] v1.1 do auditor-2 RECEBIDA e REPLICADA (trilha 27):** R1–R7 incorporados; contraproposta
  `ancora_principal` ACEITA (invariante por construção); §8 padrão ancorado 0 FP medido; migração
  simulada: N2 243/274 mecânicos, pendências honestas medidas (197 desenhos a ler · 30 review · 30
  B1_v2 · 24 forca_biologica · exceção única VINC_B1_0047 = já na P-6). **v1.1 APROVADA como base do
  L-05/1.2 níveis 1–2; V2 transmitida a ele** (carta nº 3, cópia ao mestre). Novo pedido formal ao
  operador: kit da trilha clínica (5 docs — SCHEMA-CLAIM v1.2 etc.) **não existe no nosso repositório**.
- **[Mesmo dia, noite] Parecer do mestre sobre a V2 + resposta externa — trilha 28:** §1 dele
  REESCOPA a dívida de taxonomia (tokens editoriais fora do caminho do motor; V-15 vira aviso-na-prosa
  / erro-em-ficha-vínculo) — casa confirma: 94 ERRO 100% editoriais. **D-01…D-08 nomeadas**; restrições
  do ChatGPT ADOTADAS com crédito (sem hierarquia artificial — escada de 7 passos + preservar
  concorrentes; sem escalar único — **piso por eixo**, solução da casa) + `status_epistemologico` na NT
  + template de 6 partes + rastro no L-PU. **mestre redige o 1.1; minuta da casa = bancada de
  verificação.** **CARTA Nº 3 ao auditor-2 EM ESPERA** (sai com a V2 resolvida — decisão do operador).
