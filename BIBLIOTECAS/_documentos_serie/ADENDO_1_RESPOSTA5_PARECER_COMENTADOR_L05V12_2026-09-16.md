# ADENDO 1 à RESPOSTA 5 — Parecer formal v1.0 do comentador sobre a v1.2: verificado pela bancada

**Data:** 2026-09-16 · **Ref.:** `PARECER_COMENTADOR_L05_V12_v1.0_2026-09-16.md` sha `a193543843740732189f4f3b7ff9352cb4372392b6036cc9c80913ca013dea87` (arquivado verbatim na pasta `L05_v1.2_schemas_recebidos_2026-09-16/`) · **Trilha:** 38 · **Ciência tocada:** 0

---

## 0. O que é e como foi tratado

O comentador selou parecer formal: **FAVORÁVEL à direção estrutural da v1.2, aprovação condicionada** ao fechamento das decisões normativas e bloqueadores operacionais (D1–D5 do operador + condições §21). A nota crua não circula; esta carta carrega o que a bancada **verificou contra o acervo e o catálogo**, com crédito. Os 3 pontos de schema da análise anterior dele seguem seu próprio trilho na RESPOSTA 5 — não há contradição: são condições de fechamento do mesmo caminho.

## 1. Conferido contra os dados — tudo que era mensurável

| § do parecer | Afirmação | Réplica da bancada |
|---|---|---|
| §4/D2 | "30 registros review" | **confere** — `evid_role=review` = 30 (a dívida D-B1-R3-V2CLAIM, regime da Decisão 2) |
| §8/§16 | caso-teste REF_RAISON_2013 | **confere e é bem escolhido** — tem **2 vínculos** (VINC_B1_0128, VINC_B1_0173), ambos `CONFIRMADO`·`verificado`·`clinico`: exatamente o perfil que NÃO deve virar `sustenta` automático. A casa não reabriu o artigo — a leitura do subgrupo é do senhor e do G3 |
| §8 | "fila de **1**" anterior | **confere** — VINC_B1_0047 (a exceção da nossa linha (ii)) |
| §8/§16 | "**172 automáticos / 102 humanos**" | **não reversível da nossa bancada**: nenhuma soma simples de `status_auditoria`×`verification_status` fecha 102 (cruzamento completo na trilha 38). A regra vive no **relatório de execução do senhor — que não chegou até nós**. **PEDIDO FORMAL:** enviar o relatório/script (regra conservadora, lista dos 102, aplicação RAISON); a casa replica no mesmo padrão que replicou o P-8 |
| §5 | 146 IDs em domínios distintos | **confere** — parse estrutural: 48 suplementos (D1–D6) + 71 exames (C1–C13) + 16 mecanismos + 11 cenários = **146**, 5 removidos |

## 2. §12/D4 (`citacao_confirmada`) — premissa envelhecida: a dívida de proveniência já está encerrada

O parecer parte de "237/237=true **sem origem conhecida**". Medido: 237/237=true **confere** — mas a v1.2 que o próprio comentador analisou já registra **R6/D4 RESOLVIDO**: o valor é *default de geração* (PROMPT v4.2 L1290/L1313), DEPRECATED, banido de portão desde o gate rev.A2 (grep: 0 ocorrências no gate). Não há origem oculta a auditar. Sob a própria sequência dele (preservar→auditar origem→registrar→decidir), os três primeiros passos **estão feitos** — falta ao operador apenas formalizar o destino: manter deprecated sem carga verificacional (= o estado atual).

## 3. §13 (catálogo dos 146 = bloqueador principal) — confirmado em dobro, e a casa assume

Ele cita "146 declarados × 103 capturados": são **números da nossa trilha 25** — o bloqueador §13 dele é a dívida já nomeada da casa **D-L05-IDS-JSON**. Esta rodada a bancada demonstrou o porquê em laboratório: parse estrutural fecha 146 exatos, mas **grep de texto rende 74, 103 ou outro número conforme o padrão** — suplementos não carregam prefixo (`omega3_epa_dha`, `5htp`…). O derivador oficial nascerá **estrutural** (walk do JSON + contagem por categoria + sha público), conforme a sequência dele — que é a mesma que tínhamos planejado. Reforço externo de prioridade, registrado.

## 4. Convergências já implementadas (registro, não pedido)

- **§7 (papel ≠ eficácia):** a proibição de inferência já está **no próprio schema v1.2** (description de `papel`) — falta carregá-la no contrato de execução do Motor (autoridade do Auditor-Mestre) ou na prosa da 1.2;
- **§6/§15 (fronteira schema × portão):** bate com as nossas medições — integridade referencial inexprimível em draft-07 foi para o V-17 (trilha 35); exclusividade de `condicao` É exprimível e propusemos no schema (carta 5 §2);
- **§9 (não unificar vocabulários) e §10 (`B1_v2`→`leva_origem`):** a medida da bancada sustenta ambos — 30 valores `"B1_v2"` medidos;
- **§17/§23 (papéis e autoridade):** conforme o MAPA V2 — casa não assina ciência, comentador não decide, auditor de estrutura não aprova sozinho;
- **§19 (regra transversal proveniência≠epistemologia≠causalidade≠decisão):** princípio **adotável** — a casa sugere § próprio na prosa da 1.2 (dados) e rebatimento no contrato do Motor (execução); o schema v1.2 já implementa pedaços (papel, leva_origem, status_validacao).

## 5. Estado do tabuleiro após o parecer

O L-05 v1.2 tem agora: 9/9 de incorporação verificada (carta 5 §1) + parecer externo favorável condicionado + superfície de migração quantificada (N2: 3 campos + 30; N1: 2 campos + 175 valores de desenho + 50 origens). O que separa a 1.2 da assinatura da casa: (a) minuta 1.2 com prosa §3 (R1+R7), §4B do rodapé e linha (ii) da triagem `direcao`; (b) fechos da carta 5 (`condicao`, paradoxo do alias, `cross-over`, ponteiro `forca_biologica`); (c) o relatório de execução do senhor (§1 acima); (d) decisões do operador D1–D5 — a casa já entregou a ele o material medido de cada uma.

## 6. Crédito e registro

Parecer: **comentador externo** (v1.0, 16/09). Execução e schemas: **auditor-2**. Réplica, demonstração do parser instável, paradoxo do alias, superfície: **bancada**. Trilhas 37/38 · decisoes **rev.26** · **0 ciência** (V7 `6e2c2979…` e manifesto `79d1309a…` íntegros; RAISON citado só por status — nenhum artigo reaberto).

— a casa
