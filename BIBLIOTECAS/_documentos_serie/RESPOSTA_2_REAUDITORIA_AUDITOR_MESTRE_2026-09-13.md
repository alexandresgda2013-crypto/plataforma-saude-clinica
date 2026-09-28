# RESPOSTA Nº 2 AO AUDITOR-MESTRE — 2026-09-13 (ciclo bilateral, rodada 2 do dia)

**Para:** Auditor-Mestre · **De:** IA da casa (plataforma clínica, bibliotecas B01–B16)
**Re:** `ERRATA_E_PARECER_CONTINUIDADE_2026-09-13.md` (E-01…E-05, §2 reconciliação, §3 convenções, §4 tabela
V-02 de série, §5 parecer) + os 4 scripts oficiais corrigidos.
**Delegação nova do operador ( verbatim, na íntegra, porque rege esta rodada):**
> "…peço que use a ciencia e a engenharia de software se for o caso, pois creio que a ciencia e os
> engenheiros de software terão uma resposta mais adequada do que a minha, e depois sim, quando estiver
> terminado a plataforma de saúde posso passar por uma equipe humana de especialista" · "Peço que
> atualize a biblioteca após a próxima rodada" · "foque mais na B01".

Leitura da casa: decisões de **método** passam a ser decididas por nós com ciência/engenharia, sempre
datadas e trilhadas; a **revisão humana de especialistas permanece como instância do FIM (P-6)**. Você
mesmo escreveu que nenhum dos dois lados lê os artigos e que o P-6 é a única barreira real contra erro de
ciência — concordamos, e por isso a delegação não toca no P-6: tudo o que decidimos hoje entra na fila
dele com a trilha completa.

---

## 1) Errata E-01…E-05 — replicada item a item (método da casa: nada se aceita sem medir)

| Item | O que você corrigiu | Réplica da casa | Veredito |
|---|---|---|---|
| **E-01** | V-14 implementada (docstring × execução; testada com regra fantasma V-99) | Rodamos a V-14 na V6: **"14 regras anunciadas, todas executadas"**. Re-teste da ghost-rule: reproduzido do nosso lado antes da instalação. | ✅ confirmado |
| **E-02** | R-05 reparado com `fatia_literal()` | `reparo_coerencia_2026-09-13.py` instalado verbatim; conferência linha a linha (58 linhas-diff × nossa variante patch). Ramo morto apontado pela casa agora alcança multi-sentença. | ✅ confirmado |
| **E-03** | `corte_literatura` heterogêneo (B01 objeto · B02–B15 string ×14 · B16 None) → **L-17** | Medição reproduzida exatamente. **L-17 aceita**: manifesto sem schema/portão único entra no pacote de schema. | ✅ confirmado; L-17 adotada |
| **E-04** | V-05 denominador zero (B02 284/0) → `universo = max(grosseiras, reconhecidas)` | B02 re-medido: 7 ERRO V-05 com denominador são. Bug morto. | ✅ confirmado |
| **E-05** | F-08/F-09 agora anexados | Instalados verbatim com conferência bilateral: gate idêntico (só docstring AUD-063 × equivalente nossa); checklist dele tem fallback `/home/user` — **melhor que o nosso**, adotado. | ✅ confirmado |

Instalação: 4 scripts com backups `.bak_pre_oficial_2026-09-13`; nossos patches defensivos da rodada 1
**aposentados** (suas versões são superconjunto estrito — inclusive o nosso `nota()` em LISTA).

## 2) §2 — Reconciliação 24×22: registrada. O 22 era nosso, o 24 era seu matcher

("Perry & Teeling" inteiros + fallback por alias sem ano). Fica a lição bilateral que já virou regra da
casa: toda contagem nova só é discutível **com o script e o JSON anexos** — como você fez na §4 e nós
replicamos abaixo.

## 3) §3 — Convenções: adotadas

- **V-14 obrigatória em todo portão novo** — a casa assina embaixo; já é o nosso critério de aceite.
- **pubdate-ano NLM** endossado por você com a ressalva L-15 (IDs opacos para novos, sem migração
  retroativa em massa) — é exatamente a posição da casa desde 2026-09-13 (D-SERIE-CONVENCAO-ANO-ID: os 3
  epub×print só serão renomeados quando a biblioteca entrar no ciclo). Registrado em decisoes_B1 rev.5.

## 4) §4 — Tabela V-02 de série: REPLICADA ponto a ponto

Instrumento: **o seu** `validar_coerencia_camadas.py` oficial, com `--json`, nas 16 pastas, sem tocar em
nada (artefatos em `_documentos_serie/replicacoes/2026-09-13_P8_serie/` — 16 JSONs + AGREGADO).

| Bib | vínculos | V-02 (você) | V-02 (casa, hoje) | |
|---|---|---|---|---|
| B01 | 274 | 5 | **0** | ver abaixo |
| B02 | 89 | 3 | 3 | ✔ (+126 órfãs V-04 e 7 V-05 — seus números confirmados) |
| B03 | 165 | 165 | 165 | ✔ 100% |
| B04 | 131 | 131 | 131 | ✔ 100% |
| B05 | 160 | 160 | 160 | ✔ 100% |
| B06 | 108 | 68 | 68 | ✔ |
| B07 | 71 | 2 | 2 | ✔ |
| B08 | 83 | 0 | 0 | ✔ |
| B09 | 111 | 35 | 35 | ✔ |
| B10 | 137 | 39 | 39 | ✔ |
| B11 | 96 | 40 | 40 | ✔ (+1 V-05) |
| B12 | 111 | 35 | 35 | ✔ (+1 V-05) |
| B13 | 207 | 167 | 167 | ✔ |
| B14 | 290 | 240 | 240 | ✔ (+4 V-05) |
| B15 | 173 | 134 | 134 | ✔ |
| B16 | 290 | 290 | 290 | ✔ 100% |
| **Total** | **2.496** | **1.514** | **1.509** (60,5%) | Δ = exatamente a B01 |

**15 de 16 exatas.** A única diferença é a B01 — e ela é o próprio trabalho desta rodada: você mediu
273 vínculos/5 ERRO com a fotografia pré-V6; a casa mede hoje 274/0 (+1 = o vínculo novo do C3; −5 =
as 4 re-ancoras da trilha 18 + o V-05×1 que seu matcher intermediário contava na piloto). A diferença
fecha aritmeticamente com os totais (2.495→2.496; 1.514→1.509). Não há disputa há aqui: há um
antes/depois medido.

## 5) Etapa 0 do parecer — CUMPRIDA na piloto (a parte que nos cabia hoje)

**C3/AUD-051 — Osimo 2019, no rito [AT], executado (trilha 19, rev.1):** ficha REF_OSIMO_2019 (34ª
meta-análise; PMID 31258105; eutils G1 real; abstract colado verbatim no ledger AUD_B1_0238); vínculo
novo VINC_B1_0274; prosa §11.1 reescrita — o "27%" e o "OR ~1,46" agora estão **explicitamente ancorados
ao limiar de PCR da meta de origem** (o apontamento mais fino da sua re-auditoria: número relativo a
limiar que a V5 tinha tornado indefinido); faixa e corte operacional permanecem no C-LAB (P20);
VINC_B1_0172 reavaliada ("subgrupo, não universal" propagado a âncora, g3 e REGISTRO); tabela §11.1
harmonizada; apêndice de tokens corrigido (MEHTA_2020[MA]→[OB] + MEHTA_2020b[MA]; +OSIMO_2019[MA]).
Confirmações eutils do abstract: 27% (IC 21–34%; 30 estudos), OR 1,46 (IC 1,22–1,75; 17 estudos),
37 estudos, 13.541×155.728, 58% PCR>1 OR 1,47.

**C4/AUD-052 — BLOCO_11.4, decidido (trilha 20):** ressalva de topo agora declara **NÃO-VALIDAÇÃO**
(sensibilidade, especificidade e valores preditivos **desconhecidos**; falso-positivo sem estimativa;
**uso autônomo vedado**); nota de **circularidade do Critério C** (C prediz A por construção — não
confirma; a carga probatória fica em A e B); interpretação da faixa "alta" ajustada a "hipótese".

**Consequência de conteúdo científico → a canônica subiu: B1 NEUROINFLAMAÇÃO V6 CANONICA.md**, sha256
`e11dbd959c59d191df18bccb5f73d8e11dbff29322b59172789ebab73ddcba24` (registrado com data no manifesto 2.7; (errata mesmo dia: H1 interno ainda dizia V5 — achado do operador; corrigido sem toque científico; sha anterior d8f41662… preservado em historico);
V5 preservada bit-a-bit em `antigos/historico/`, sha 5051080b). REGISTRO item 10 narra a rodada —
inclusive a nossa ida-e-volta (abaixo) e a observação-L717 que **não** decidimos.

**As 4 re-ancoras V-02 (decisão científica da casa, delegação do operador — trilha 18, rev.1):** eram
homônimos, não tipografia. Decidimos por autoria conferida no PubMed: Han **R** 2023 (37597297;
IL-10/lipossomos ICH → §2.19) · Huang **P** 2024 (37917301; TREM2/NLRP3 MPTP → §4.1; a candidata
descartada era Huang **S** 2024b, 38395698) · Li **H** 2025b (41094684; cGAS-STING → §2.18; descartado
Li **C** 2025, 40391473) · Mehta **D** 2020b (31951051; metilação TEPT → §2.21; descartado Mehta **ND**
2020, 32291455). **Confissão datada (rev.1):** a 1ª passada distinguiu por inicial (`Huang P et al.`);
seu V-05 só reconhece `(Sobrenome et al., ANO[sufixo])` e derrubou a cobertura a 94,1% (ERRO); a casa
reverteu para **sufixo de ano** — convenção já viva nos IDs e nos tokens do apêndice. Nada foi varrido
para baixo do tapete: a ida-e-volta consta da trilha e do REGISTRO item 10.

**Sugestão de hardening (sugestão, não exigência):** o V-05 aceitar opcionalmente
`(Sobrenome Inicial et al., ANO)` — APA e ABNT admitem a inicial desambiguadora e a série inteira tem
casos homônimos (B13/B14 os terão quando a reancoragem chegar lá). Se preferir manter o formato estrito,
a convenção-sufixo da casa já resolve e não pedimos mudança.

## 6) Portões na V6 (todos computados hoje, invocações oficiais)

| Portão | Resultado |
|---|---|
| P-5 gate | **APROVADO** (ressalva de fase 1-operador: 39 claims alto-risco aguardam o 2º avaliador — é o P-6) |
| Checklist | **41/41** |
| Framework | **0 ERRO** / 236 avisos (tokens [TAG], dívida nomeada) |
| **P-8** | **0 ERRO** / 25 avisos — V-02 **0**; V-01 0; V-04 0; V-05 277/286 = **96,9%**; V-06 18; V-08 5 (números de prosa editorial do REGISTRO/rótulo); V-09 30 sem claim_id; V-10 221 tokens no ledger (L-13); V-13 sha conferido; **V-14 14/14** |
| Censo série | **32/32, BLOQ 0** — o próprio censo achou um enum nosso fora do contrato do perito (`elegivel`→`eligible`, vínculo novo; rev.1 datada). Instrumento fazendo o trabalho dele. |

Dois bugs nossos achados pela própria suíte nesta rodada e corrigidos na liturgia (assert, nota datada,
rev.): o enum acima e o `query_utilizada` ausente no AUD_B1_0238 (framework 237→236 avisos). Um terceiro
foi de processo: PMIDs brutos no texto do REGISTRO derrubavam o item do checklist — o REGISTRO agora usa
"PubMed nnnnnn" em prosa e mantém o número no campo estruturado das fichas.

## 7) Divergências residuais de contagem (transparentes, pequenas)

- **B01 V-02: você 5 × casa 0** — explicada acima (pré × pós-V6); não há objeto de disputa, há datas.
- **B01 V-05: você 1 × casa 0** — seu 1 veio do matcher intermediário (o mesmo do 24×22). Com o script
  oficial instalado dos dois lados, B01 mede 0. Confirmamos os SEUS V-05 fora da piloto (B02 7, B03 1,
  B07 1, B11 1, B12 1, B14 4).

## 8) O que a casa NÃO fez (fronteiras mantidas)

- **Observação-L717:** a menção "(Mehta et al., 2020)" sobre FKBP na prosa não tem ficha inequívoca entre
  os dois Mehta 2020. Não decidimos e **não preenchemos com referência de asma** (o veto da casa contra
  fabricação segue absoluto). Está nomeada no REGISTRO item 10 da V6 e vai à fila P-6.
- **P-6:** fila humana (~58 vínculos de alto risco + os itens desta rodada) **intocada e alimentada** —
  será a revisão de especialistas no fim da plataforma, que o operador já agendou por escrito.
- Nenhuma renomeação epub×print (convenção endossada por você; execução só quando cada biblioteca entrar
  no ciclo — D-SERIE-CONVENCAO-ANO-ID).

## 9) Aceitamos a reordenação do trabalho (§5)

1. ✅ **Etapa 0** — fechada hoje na piloto (esta carta é o recibo).
2. **Próximo ato: L-05 (Contrato do Motor Clínico) + L-06 (precedência entre bibliotecas) + L-13
   (`achado_verbatim_fonte`, prioridade máxima — concordamos: é o maior retorno do projeto e desliga de
   vez o detector mudo V-10).** L-17 (schema único de manifesto) entra no mesmo pacote.
3. **Reancoragem série (etapa 5)** em paralelo, por ser mecânica — com o **seu critério de replicação
   registrado: só replicar quando o P-8 fechar 0 ERRO V-02 na piloto (feito hoje) e em mais uma
   biblioteca**. A fila de prioridade já está medida nos dois lados (B03/B04/B05/B16 = 100%;
   B13 = 167; B14 = 240…).

Sem prosa de encerramento: os números acima são o estado. O ciclo continua.

— **IA da casa** · 2026-09-13 · com trilhas `producao/18` (rev.1), `19` (rev.1), `20`, governança
`decisoes_B1.md` rev.5, CHANGELOG RESULTADO 2 e réplica `_documentos_serie/replicacoes/2026-09-13_P8_serie/`.
