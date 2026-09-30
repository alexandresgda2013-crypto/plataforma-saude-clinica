# CHANGELOG GERAL — Plataforma BIBLIOTECAS (B1–B16)
**Regra vigente a partir de 2026-09-10 (IMPL-AT-10, exigência do usuário): TODA alteração em
qualquer documento, canônica, JSON de evidência ou script gera uma entrada neste arquivo E uma
nota datada dentro do próprio artefato alterado. Nada mais se altera "em silêncio".**
Formato: `data · artefato · o quê · por quê · evidência/verificação`.

---

## 2026-09-09 · B16 — rodada [AT] (auditoria + fusão dirigida)
- `B16 NEUROGENESE V2 CANONICA.md` **criada** (de V1): +2 âncoras (REF_DOLUDDA_2026 consenso;
  REF_ZHOU_2025 pós-parto) após falha silenciosa da rodada 0 detectada; REGISTRO DE AUDITORIA
  [AT] inserido; contagens/corte/rag atualizados. V1 arquivada em
  `B16_Neurogenese/producao/historico/v1_canonica_2026-09-09.md`.
- Tríade B16 288→290 (pmids/vínculos/ledger +2 cada); manifesto normalizado por ADIÇÃO
  (versao v2, rodada_at, identificadores_falsos_expostos, exclusões ratificadas, aliases DOI,
  historico_rodadas, pendencias_fase); trilha `04_AT_ciclo_2026-09-09.json`; matriz
  `producao/insumos/matriz_b16_decisao.json`; decisões + bloco RODADA [AT]; P-4 + ADENDO V2;
  relatório `RELATORIO_EXECUCAO_B16_AT_2026-09-09.md`.
- Reparo interno: 46 vínculos + 46 ledger reancorados às listras atualizadas §1.2/§11.2;
  `origem_entrada` das 2 novas = LISTA_CANONICA (vocabulário do framework).
- Portões: gate ✅ · framework 0 ERRO (290 avisos legados) · checklist **41/41**.
- Registros in-band: blocos datados em decisoes_B16.md / fidelidade_P4_B16 / manifesto.

## 2026-09-09/10 · Documento consolidado da série
- `RESUMO_CORRECOES_RODADA_AT_B1_B16.md` **criado** (placar 1.702→2.690; 988 incorporadas,
  conferido contra as 16 trilhas). Origem dos números: `producao/04_AT_*.json` de cada pasta.

## 2026-09-10 · Perícia externa dos scripts (LOTEs 1–7)
- `CONTRARRAZAO_PERICIA_EXTERNA_SCRIPTS_2026-09-10.md` **criada** (v1): concordâncias com
  evidência viva, dívidas novas medidas (B7 31 órfãos; B2 126 sem vínculo; B8 62/58; B1 17 +
  literality 33%), plano IMPL-AT-00..09.
- Re-varredura motivada pela perícia: checklist re-executado nas 16 → **B14 reprovou 3 itens**
  (vocabulário cruzado ledger→vínculos nas 50 entradas [AT]).

## 2026-09-10 · IMPL-AT-00 — reparo B14
- `B14: Evidencias/Vinculos/*.json` 50 vínculos `status_auditoria APROVADO→CONFIRMADO`;
  `01_pmids.json` 50 refs `g1_metodo`→`"eutils_automatico"` (detalhe preservado em `g1_resumo`).
- Verificação: gate ✅ · framework ✅ · checklist **41/41**. **Sem alteração de conteúdo.**
- **Nota de falha de processo (confessada):** este reparo foi executado e reportado apenas no
  chat, sem nota nos artefatos — é exatamente a falha que gerou a regra AT-10. Marcas
  retroativas agora gravadas em: `Auditoria_B14/decisoes_B14.md` (bloco ALTERAÇÃO 2026-09-10),
  manifesto `alteracoes[]`, trilha `producao/05_reparo_AT00_2026-09-10.json`.

## 2026-09-10 · Re-verificação integral das 16 (pós-B14)
- Checklist **41/41 em 16/16** (B1–B9 exigem `Bn` explícito por bug de padding do checklist:
  pasta `B01_...` deriva `B01` ≠ `Auditoria_B1` — falso-falha de invocação, registrado para o
  time das ferramentas, IMPL-AT-06 vii).

## 2026-09-10 · TRÍPLICE do perito + resposta
- Recebida `TRIPLICA_CONTRARRAZAO.md` (3 retratações do perito; perícia do framework com 5
  furos F1–F5; 4 emendas E1–E4 ao plano; aceite da Rodada 2).
- `CONTRARRAZAO...md`: **ADENDO v2 2026-09-10** anexado em seção marcada (sem reescrita da v1):
  resposta à tríplice, integração das emendas E1–E4, plano v2 = AT-00..09 + E1–E4 + **AT-10**
  (governança de rastreio — este arquivo + notas in-band).
- `RESUMO_CORRECOES_RODADA_AT_B1_B16.md`: seção "REGISTRO DE ALTERAÇÕES" anexada (v1 = criação).

---
*(Próximas alterações: anotar aqui ANTES de executar — a entrada é pré-condição do reparo.)*

## 2026-09-10 · REORGANIZAÇÃO ESTRUTURAL — pastas `atuais/` × `antigos/` (a executar agora)
**Pedido do usuário:** dentro de cada B01–B16 criar `atuais/` e `antigos/`; material vigente →
`atuais/`, material superado → `antigos/`.
**Regra de classificação:** `atuais/` = canônica vigente + `Evidencias/` + `Auditoria_*/` +
`producao/` (menos historico) + scripts/artefatos da versão vigente; `antigos/` = conteúdo de
`producao/historico/` (versões V1/anteriores, pré-canônicas, briefings e relatórios superados).
**Restrição de engenharia respeitada:** `gate_script.py` e `checklist_entrega.py` localizam a
canônica por glob NÃO-recursivo na pasta alvo → a unidade canônica+Evidencias+Auditoria move-se
JUNTA; invocação dos portões passa a ter pasta `Bxx/atuais` (+ `Bn` explícito no checklist).
**Verificação obrigatória pós-mudança:** gate+framework+checklist re-executados nas 16 antes
de dar por concluído (resultados anotados abaixo nesta entrada).

**RESULTADO (2026-09-10):** reorganização executada — 95 movimentos registrados em
`reorg_move_log_2026-09-10.txt`; `README_ORGANIZACAO.md` gravado nas 16 pastas com a nova
invocação dos portões; **verificação pós-mudança: checklist 41/41 em 16/16** (gate ✅,
framework 0 ERRO via subprocess do checklist). Estado: séries íntegra, enxuta e rastreável.

## 2026-09-10 · Enxugamento da raiz de BIBLIOTECAS/ (mesma reorganização, nível série)
- Criada `_documentos_serie/` e movidos: `RESUMO_CORRECOES_RODADA_AT_B1_B16.md`,
  `CONTRARRAZAO_PERICIA_EXTERNA_SCRIPTS_2026-09-10.md`, `reorg_move.py`,
  `reorg_move_log_2026-09-10.txt`. `CHANGELOG_GERAL.md` permanece na raiz (é o livro-caixa).
- Referências internas são textuais e permanecem válidas; portões não leem esses arquivos.

## 2026-09-10 · Organização de uploads/: insumos soltos → bibliotecas (dedupe por hash)
- Auditoria prévia: 89 arquivos em uploads/ · **18 byte-idênticos já existem dentro das
  bibliotecas** (em `producao/rodada1_gpm/`) · 1 par idêntico interno (BRIEFING_B16 ×2).
- Ação: (i) idênticos → removidos de uploads (conteúdo preservado dentro da biblioteca — hash
  registrado); (ii) únicos → movidos para `Bxx/atuais/producao/insumos/uploads_originais/`
  com **nome original preservado** (trilhas citam por nome); (iii) docs da perícia →
  `_documentos_serie/pericia_externa/`.
- Mapa completo origem→destino (com md5): `_documentos_serie/uploads_reorg_map_2026-09-10.json`.

**RESULTADO (2026-09-10):** uploads/ esvaziado — 71 insumos movidos para
`Bxx/atuais/producao/insumos/uploads_originais/` (nomes originais preservados), 18 removidos
por byte-identidade (registrados com md5 + caminho interno no mapa), 8 documentos da perícia
externa em `_documentos_serie/pericia_externa/`. Verificação: checklist B16 = 41/41 (arquivos
não são lidos por portões — checagem de sanidade executada por segurança).

## 2026-09-10 · Recolhimento de scripts soltos na raiz do workspace (~100 arquivos)
- Pedido do usuário (scripts/artefatos fora das bibliotecas). Classificação:
  (i) `B<n>_*.py` e artefatos por biblioteca → `Bxx/atuais/producao/scripts/`
  (incl. realocação dos apply-scripts B14/B15/B16 de `atuais/` para lá — uniformidade;
  RELATORIO B16 idem → producao/); `B1?_canonica.md` (rascunhos de build) → `producao/scripts/` (NUNCA
  em `atuais/` raiz — poluiria o glob do gate/checklist);
  (ii) scripts transversais (regen/upd_b567, p4_*, retrocompat etc.) → `_documentos_serie/scripts_serie/`.
- Mapa origem→destino com md5: `_documentos_serie/scripts_reorg_map_2026-09-10.json`.
**RESULTADO (2026-09-10):** 123 movimentos executados; raiz do workspace com **zero arquivos
soltos** (restam os 3 diretórios: BIBLIOTECAS/, Ferramentas de geração e auditoria/,
uploads/ vazio). Verificação pós-mudança: checklist B14 = **41/41** · B10 = **41/41**.

## 2026-09-10 · Perícia externa 4ª rodada (PARA_O_AGENTE_2026-09-10.md) — CICLO ABERTO
- Recebido o parecer da 4ª rodada (arquivo `uploads/PARA_O_AGENTE_2026-09-10.md`; **anexos
  citados — `contrato.py`, `canonico/literalidade_b1.json`, 2 relatórios — NÃO vieram no
  pacote**; replicação feita com ferramentas próprias, conforme o método pactuado).
- **Abertos nesta entrada (resultados serão anexados ao final):**
  1. Replicação independente: (a) achado AT-11 (`tier_2_intervencao` fantasma em 3 vínculos
     B1-v2 e `tier_1_intervencao` fantasma no `gate_script.py` L101); (b) classificação de
     literalidade dos 257 vínculos B1 (teste das teses 103/77/55/22 e "0 rótulo na leva v2");
     (c) contagens por categoria para B2/B7/B8.
  2. **IMPL-AT-11 (decisão do agente):** opção (b) — remapear os 3 registros ao tier oficial e
     corrigir a string do gate. Justificativa registrada nos artefatos e na resposta ao perito.
  3. Reparo de dados: `B01` vínculos — 3 registros `tier_2_intervencao → tier_2_necessidade_ou_suficiencia`
     (forca_causal) e `natureza_relacao → causal`, com nota datada in-band.
  4. Reparo de ferramenta: `gate_script.py` L101 `tier_1_intervencao → tier_1_necessidade_e_suficiencia`,
     com backup prévio, nota datada em comentário e re-execução do gate nas 16 bibliotecas.
  5. Novo script transversal de análise: `_documentos_serie/scripts_serie/literalidade_classify.py`.
  6. Resposta formal ao perito: `_documentos_serie/RESPOSTA_PERICIA_RODADA4_2026-09-10.md`.

### 2026-09-10 · 4ª rodada perícia — RESULTADOS (anexo à entrada aberta acima)
1. **Replicação AT-11: CONFIRMADO.** 3 vínculos B1-v2 (VINC_B1V2_0205/0207/0208) com
   `tier_2_intervencao` fantasma (forca_causal E natureza_relacao); `gate_script.py` L101 tinha
   `tier_1_intervencao` fantasma — INFO[6] B1 media 36 pré (ramo de força nunca disparava).
2. **Classificador independente v2** (`_documentos_serie/scripts_serie/literalidade_classify.py`;
   v1 corrigida após auto-detecção de 3 bugs: markdown `**` nas âncoras, seed só no offset 0,
   rótulo dentro de parêntese): B1 = **103 LITERAL (número exato do perito)** · 21 LITERAL_APROX ·
   3 SELO · 93 ROTULO · 7 PROSA · 30 AUSENTE · **ROTULO na leva v2 = 0 (fato replicado)** ·
   auto-reparáveis 96 vs 99 do perito (divergências definicionais transparentes no doc-resposta).
3. **IMPL-AT-11 executado — decisão opção (b):** 3 registros → `tier_2_necessidade_ou_suficiencia`
   (forca_causal) + `causal` (natureza); `nota_reparo` com valores originais em cada registro;
   trilha `B01/atuais/producao/05_reparo_AT11_2026-09-10.json` (sha pré/pós); nota datada em
   `decisoes_B1.md` (com rev.1 corrigindo projeção 41→38 do INFO[6] para o valor MEDIDO) e
   `alteracoes[]` no manifesto B1. Enum `forca_causal` da B1 pós-reparo: 0 fora do oficial.
4. **Reparo de ferramenta oficial:** `gate_script.py` L101 → `tier_1_necessidade_e_suficiencia`,
   backup `gate_script.py.bak_2026-09-10`, nota datada em código. **16/16 gates APROVADOS**
   pós-reparo; INFO[6] B1 = 38 (36 → 38: 2 refs tier_1 novos no conjunto). B1: framework 0 ERRO ·
   checklist 41/41.
5. **Achado ampliado (novo, o perito não tinha):** vocabulário estendido fora do enum oficial
   concentrado em B7 (57 registros/6 valores) e B8 (49/5) — família fantasma real = 13 registros
   `*_intervencao*` (3 B1 + 10 B7/B8) e 106 no total. **Declaração E1 provisória** gravada nos
   manifestos B07/B08 (`vocabulario_estendido_declarado` + alteracoes), harmonização enfileirada
   (AT-03/AT-04/AT-09); NÃO remapear em silêncio. Checklists B7/B8 re-verificados: 41/41.
6. **Censo pedido #4 (B2/B7/B8)** em `_documentos_serie/RESPOSTA_PERICIA_RODADA4_2026-09-10.md`
   §4 — os 33 da B1 NÃO são exclusivos: B2 (61 trechos-rascunho "PMID" + 61 claim_id vazio),
   B7 (71/71 sem claim_id), B8 (83/83 sem claim_id).
7. Anexos do perito (`contrato.py`, `literalidade_b1.json`, 2 relatórios) NÃO vieram no pacote;
   solicitado reenvio na resposta. Pacote da Rodada 2 segue na fila (após P-6 Via 2: AT-01..05).
- Documento-resposta criado: `_documentos_serie/RESPOSTA_PERICIA_RODADA4_2026-09-10.md`.

## 2026-09-11 · 5ª rodada perícia externa (FERRAMENTAS_PERITO_v1) — CICLO ABERTO
- Recebido pacote completo (6 scripts colados + 8 anexos). Arquivado em
  `_documentos_serie/pericia_externa/5a_rodada/`. Bancada isolada montada em
  `_documentos_serie/bancada_at02/` (NADA roda no vivo).
- **Réplicas independentes executadas:** contrato.py autoteste **8/8**; sha256 da canônica
  idêntico ao declarado pelo perito (8b9fe0e6…2ce5); contrato nos dados vivos: vínculos
  33→**27** bloqueantes (AT-11 aparece como −6); ledger 0/0; pipeline 5 passadas na cópia:
  **80+6+38+0+27 = 151 reparos — números idênticos ao relatório dele**; diff bancada×vivo:
  apenas `trecho_ancora` ×151, ordem/contagem preservados; 146/151 âncoras novas contêm
  sobrenome+ano da própria ref — os 5 restantes inspecionados 1 a 1: falso-negativos do MEU
  checador (O'Connor, Więdłocha, Virtanen-rótulo-canônico, Lapchak×2 citação interna).
- **Decisões do agente (conteúdo), já executadas na bancada:** (a) rótulo defasado
  `— IL-6 predictor, 2015) → ; Virtanen et al., 2015)` NA CANÔNICA (fonte: 01_pmids PMID
  25697833); (b) AT-13×3 reancorados manualmente (markdown-aware): VINC_B1_0095→frase Zhang
  2024; VINC_B1_0121/0122→frase S100B que cita Arora 2019 E Gulen 2016 (co-citação legítima,
  uma frase sustenta as duas cláusulas); (c) VINC_B1_0130 reancorado à frase corrigida;
  (d) AT-02c: 26 prefixos de cabeçalho `###` removidos das âncoras.
- **Estado da bancada: literalidade 257/257 (100%)**, zero `###` em âncora, 0 falhas de guarda.
- **A executar (resultados anexados abaixo):** promoção ao vivo (backups + trilha +
  decisoes/manifesto + nota na própria canônica), portões re-verificados, contrato nas 16 com
  LEGADO estendido (pedido #1), resposta formal rodada 5.

### 2026-09-11 · 5ª rodada perícia — RESULTADOS (anexo à entrada aberta acima)
1. **Pipeline promovido ao vivo:** vínculos B1 = 257/257 literais (era 40%); diff só `trecho_ancora`;
   `reancorado_em` datado nos 158 registros alterados; backups `…json.bak_pre_rodada5_2026-09-11`.
2. **AT-13×3 decididos por conteúdo** (0095→frase Zhang 2024; 0121/0122→frase S100B/Arora+Gulen);
   `nota_reparo` em cada um.
3. **Canônica V4: 1 linha de prosa** (rótulo `— IL-6 predictor, 2015)` → `; Virtanen et al., 2015)`;
   backup `antigos/historico/v4_canonica_pre_rodada5_2026-09-11.md`; nota datada no apêndice
   (com rev.1: o próprio portão do framework me reprovou por citar o PMID numericamente na
   nota — corrigido dentro da própria nota; `rs1800795` na prosa é SNP dbSNP, falso-positivo
   da minha régua crua).
4. **Portões re-verificados: gate ✅ · framework 0 ERRO · checklist 41/41 · gates 16/16.**
5. **Contrato nas 16 (pedido #1):** `_documentos_serie/scripts_serie/contrato_censo_16.py`,
   ledgers 16/16 = 0 bloqueantes; bloqueantes de vínculos decompostos por causa (id 3 dígitos,
   vocab-pt, campo ausente da geração nova, AT-01/AT-05, 31 assinantes G3 mistos em B7).
6. **Censo AT-13 refinado (vivo):** 26 trechos compartilhados/59 refs → 21 co-citação
   legítima · 5 grupos/12 vínculos = **AT-13b** (proposta-máquina + confirmação humana, P-6);
   interseção com AT-01 (VINC_B1V2_0182/0183).
7. Resposta formal: `_documentos_serie/RESPOSTA_PERICIA_RODADA5_2026-09-11.md`.
- Nota de discrepância registrada ao perito: `literalidade_b1.json` anexado era o snapshot de
  88% (pós-4ª passada), não o de 98,8% citado na LEIA-ME — sem impacto (medimos o vivo).

---

### 2026-09-11 — NOTA (sem alteração de artefato)
- **O quê:** criado `BIBLIOTECAS/STATUS_SIMPLES_2026-09-11.md` — painel em linguagem simples do que foi alterado de fato nas Canônicas e do estado dos portões.
- **Base:** números re-verificados na data (diff B1 vs backup pré-rodada-5 = 1 linha de prosa + nota de auditoria; gates 16/16 APROVADOS; checklist B1 41/41; framework B1 0 ERRO). Nenhum arquivo de ciência foi tocado nesta ação.

---

### 2026-09-11 — ABERTURA (versionamento visível da Canônica B1)
- **O quê:** a Canônica B1 foi alterada na rodada 5 (1 linha) mas manteve nome "V4" na pasta `atuais/` — impossível ver pela listagem do workspace que mudou. Correção: **rename para `B1 NEUROINFLAMAÇÃO V4.1 CANONICA.md`** (rev. menor: 1 linha de prosa), com bump do título interno e `artefato_rotulo` v4→v4.1, rev.2 na nota de auditoria do documento, entrada `alteracoes[]` no manifesto e ALTERAÇÃO datada em `decisoes_B1.md`. A v4 integral pré-mudança já está preservada em `antigos/historico/v4_canonica_pre_rodada5_2026-09-11.md`.
- **Não muda:** ciência (0 linhas novas de conteúdo), vínculos (257), ledger (237). Ferramentas oficiais localizam a canônica pelo padrão "CANONICA" no nome — rename é compatível (verificado antes).
- **Resultado:** anexado abaixo após execução (portões re-rodados).
- **RESULTADO (2026-09-11, mesmo dia):** rename executado. `atuais/` agora lista `B1 NEUROINFLAMAÇÃO V4.1 CANONICA.md` (sha256 43b7673bd2f9d65f…). Portões re-rodados no novo nome: gate **APROVADO**, checklist **41/41 OK**, framework **0 ERRO**. Sem nenhuma linha científica nova — só versão/rótulo/nota. v4 original: `B01_Neuroinflamacao/antigos/historico/v4_canonica_pre_rodada5_2026-09-11.md`.

---

### 2026-09-11 — POLÍTICA FORMAL DE VERSIONAMENTO (palavra do operador, verbatim)
- **Regra vigente a partir de hoje:** mudança pequena (metadado, rótulo, âncora, registro) → mantém o número principal e sobe o ponto (`V4 → V4.1 → V4.2 …`), versão anterior vai para `antigos/historico/`; mudança de **conteúdo científico** → sobe o número principal (`V4 → V5`). Sempre com nota datada dentro do artefato + entrada neste CHANGELOG. Precedente inaugural: Canônica B1 `V4 → V4.1` (2026-09-11).
- **Também criado:** `BIBLIOTECAS/ROTEIRO_PROJETO.md` — mapa vivo "o que já foi feito / o que falta", com números do censo de contrato re-rodado hoje (B01–B16). Sem nenhuma alteração de artefato de ciência nesta ação.

---

### 2026-09-11 — ABERTURA (Rodada de Harmonização de Contrato — Fila A + Fila B do ROTEIRO)
- **O quê:** execução autônoma autorizada pelo operador ("faça tudo o que está determinado no roteiro"). Reparos de METADADO por causa, governados pelo documento de decisões `_documentos_serie/DECISOES_HARMONIZACAO_SCHEMA_2026-09-11.md` (D1–D9, F1–F2): traduções lossless de vocabulário pt/legado→enums oficiais, decomposição tier+desenho (AT-12), separação assinatura/método G3 (AT-03/04/B09/B10), natureza por conteúdo (AT-01/B07/B08), correction de campo em verification_status (B11–13), g2 B13; decisões de schema nomeadas (IDs 3 dígitos, g2 `nao_aplicavel`, B14–16) SEM escrita em dado onde seria invenção.
- **Liturgia garantida:** nota_reparo por registro + backup datado + trilha `producao/06_harmoniza_<Bn>_2026-09-11.json` + portões re-rodados por biblioteca (gate/checklist/framework) + varredura final 16 gates. Âncoras (AT-05/B02 ×62 e B12 ×4): extração por citação nominal com guardas; ambíguas → fila de confirmação humana (nada fabricado). Nenhuma linha de ciência em nenhuma Canônica é tocada nesta rodada.
- **Resultado:** anexado ao fim desta rodada (item a item).
- **RESULTADO (2026-09-11, fim da rodada de harmonização):** 13 bibliotecas reparadas; **2.619 alterações de campo** = 2.594 reparos de metadado (D1 1.496 · D2 346 · D3 54 · D4 70 · D5 106 · D6 150 · D7 118 · D8 254) + 25 reancoragens (AT-05×17, lote→prosa×3, lit_PROSA×5). rev.1: a redação inicial desta linha trazia estimativa truncada — números acima computados das trilhas `producao/06_harmoniza_*`/`07_ancoras_*` (somas conferidas: 2.594 e 25). Censo final do contrato: **14/16 bibliotecas com 0 bloqueantes**; B2 = 48 e B12 = 1 (fila de confirmação humana com candidatas pré-resolvidas — `CONFIRMACAO_HUMANA_ANCORAS_2026-09-11.json`); ledgers 16/16 = 0. Avisos remanescentes = decisões nomeadas D9/D7/F1 (nunca silenciadas) + literalidade da fila humana. **Portões: 16/16 gates APROVADOS; checklist 41/41 em todas as tocadas; framework B1 0 ERRO; round-trip gerador blindado = 0 novo/0 bloqueante.** Documentos: DECISOES_HARMONIZACAO_SCHEMA, SCHEMA_V2_PROPOSTA, PROPOSTAS_AT13B, RODADA2_PACOTE_PERICIA (autoteste 6/6). Erro próprio registrado: entrada de manifesto gravada por engano em B14–B16 → corrigida no ato com rev.1 datada dentro dos manifestos.

### 2026-09-11 — ABERTURA (SCHEMA v2 proposta + pacote Rodada 2 perícia)
- **O quê:** documentos `SCHEMA_V2_PROPOSTA_2026-09-11.md` (P1–P10 p/ ratificação) e `RODADA2_PACOTE_PERICIA/` (3 escritores originais + blindados, autoteste, série AT completa).
- **Resultado:** anexado — pacote montado e provado (6/6 + round-trip); aguarda acionamento do operador para envio à perícia. ✅ CONCLUÍDO nesta data.

### 2026-09-11 — ABERTURA (Resolução da fila de âncoras + AT-13b, por delegação do operador)
- **O quê:** operador delegou ("sobre as âncoras, ou qualquer outro ajuste, a IA faz; material disponível para a IA como para todos"). Resolvidos os 97 itens da fila de confirmação (S1–S4: candidata = frase de prosa com citação nominal própria; score achado+título da ref; desempate documentado) + AT-13b (12 vínculos B1: 6 re-ancorados à frase da própria ref, 6 confirmados como co-citação legítima). 3 refs sem claim na prosa (LEE_2025/HARTMANN_2024/MULLER_2000) ancoradas ao ÍNDICE DE CORPUS (arquitetura Módulo 09) com observação eutils-registrada para revisão de conteúdo final (`OBSERVACAO_REFS_SEM_CLAIM_B02_2026-09-11.md`).
- **Resultado:** censo final do contrato = **16/16 bibliotecas com 0 bloqueantes em vínculos E ledgers**. Rev.1 própria: VINC_B2_026 desempatou em stub de citação (19 chars) — pega pelo checklist >20, corrigida à frase-claim com rev datada; lição gravada no resolvedor. Gates 16/16 ✅, checklist B02 41/41 ✅. Total do dia: 2.729 alterações de campo (2.594 metadado + 135 âncoras/notas), todas com nota_reparo + trilha + backup. AT-05/AT-13b: **FECHADOS**; roteiro atualizado.

---

### 2026-09-11 — ABERTURA (Distribuição Módulo 09: [MA]→02_meta_analises.json e [EC]→03_ensaios_clinicos.json + consolidado motor clínico)
- **Pedido do operador (verbatim):** "não tem nenhuma meta análise e nenhum ensaio clínico? (…) Precisa separar por mecanismo pode fazer, mas é bom também ter todos juntos para o motor clínico".
- **Diagnóstico:** a regra oficial de distribuição do Módulo 09 (`[OB]`→01, `[MA]`→02, `[EC]`→03) foi **especificada pelo pipeline (PROMPT v4.2, instrução final de geração) mas nunca executada** — `02_meta_analises.json` e `03_ensaios_clinicos.json` estão vazios (`[]`) nas 16 bibliotecas e tudo ficou misturado em `01_pmids.json`. O framework (`validar_auditoria.py`) exige array puro na raiz + id único GLOBAIS entre os 5 arquivos → cópia é vedada; a única saída conforme a lei da plataforma é **MOVE** (distribuição oficial).
- **O quê (a executar agora):** (1) mover de 01→02 as fichas de meta-análise/revisão sistemática (sinal: tag `[MA]` da canônica OU título com "meta-anal"/"systematic review" — PubMed-verificável) e de 01→03 as de ensaio clínico randomizado (título/desenho com randomized/double-blind/placebo-controlled/crossover); (2) **sem tocar em id, pmid ou qualquer campo de dado** — só casa do registro muda; campos de schema acrescentados somente quando exigidos (09.2: `bloco_origem`, `forca_evidencia_afirmacao` — vazio quando a ficha não traz; NUNCA inventado — dívida nomeada); (3) cada registro migrado ganha `sinais_classificacao` + `migrado_em` (rastreabilidade); conflitos e casos tag-EC-amplo-sem-sinal-RCT ficam NOMEADOS na trilha p/ revisão; (4) consolidado para o motor clínico em `BIBLIOTECAS/MOTOR_CLINICO/` (`evidencias_ma_serie.json`, `evidencias_ec_serie.json`, dedup por PMID com `bibliotecas[]`); (5) ferramentas da série que liam só `01_pmids.json` (`ancora_extrai.py`, `ancora_resolve_fila.py`) atualizadas para ler Bibliografia inteira; (6) backups antes de gravar + manifesto `alteracoes[]` por biblioteca.
- **Ciência: zero linhas tocadas nas 16 Canônicas.** `[ML]`→05 e outros classificadores: fora de escopo (não pedido; mapeamento doc [ML]→05 é ambíguo — nomeado para decisão futura, não executado).
- **Resultado:** anexado abaixo após execução (contagens por biblioteca, trilha, portões re-rodados).
- **RESULTADO (2026-09-11):** distribuição Módulo 09 executada nas 16. **336 fichas migradas** de `01_pmids.json` → `02_meta_analises.json` (272; MA + revisões sistemáticas) e `03_ensaios_clinicos.json` (64; RCT) — por biblioteca: B01 33+3, B02 32+4, B03 7+2, B04 8+1, B05 8+6, B06 10+3, B07 21+3, B08 55+14, B09 7+0, B10 11+0, B11 8+2, B12 36+0, B13 15+9, B14 20+16, B15 0+1, B16 1+0 (verificadas título a título na amostra; B15/B16 quase-zero reflete o campo, não falha). **Motor clínico:** `BIBLIOTECAS/MOTOR_CLINICO/` criada — `evidencias_ma_serie.json` (268 após dedup-PMID) e `evidencias_ec_serie.json` (58 após dedup) com `bibliotecas[]` por registro + README datado. **Reconciliação ledger (pega pelo framework):** 293 ponteiros `arquivo_modulo09` corrigidos 01→02/03 (mecânico, com nota_reparo + trilha 09b). Trilhas `producao/09_*` e `09b_*` por biblioteca + série. **Portões re-rodados pós-mudança: gates 16/16 APROVADOS · checklists 41/41 nas 16 · framework 0 ERRO nas 16 · censo contrato 0 bloqueantes (32/32).** Ciência: 0 linhas tocadas (a âncora B1 acima exibe o *id* da ref em linha-lote — o MD em si não mudou).

---

### 2026-09-11 — REGISTRO (Mapa de resposta antecipada ao agente auditor externo + correção rev.1)
- **O quê:** o operador informou que as perguntas sobre `b1_anchormap.json`, "Lista Canônica + A1–A8 da v3.1" e "registros G1–G3" vêm de um agente auditor externo; veredito chega em seguida. Varredura hermética executada e consolidada em `_documentos_serie/MAPA_RESPOSTA_AUDITORIA_AGENTE_2026-09-11.md` (status de cada insumo, caminhos, lacunas reais × falsos positivos prováveis).
- **Correção rev.1:** resposta anterior afirmou que a Lista Canônica B1 não existia no workspace — **erro de rastreio** (`find` com padrão `*canon*` não casa "CANÔNICA"). O arquivo existe: `02_fase1_gpm_profundidade/7º LISTA CANÔNICA — B1 TRILHA MECANÍSTICA GPM_B1 ARENA.md` (736 linhas, v1.1, 83 itens). Confessado aqui e no mapa.
- **Ciência: 0 linhas tocadas.** Nenhum artefato governado alterado nesta ação (apenas o documento de mapeamento criado).

### 2026-09-11 — REGISTRO (consolidado "TODOS juntos" para o motor clínico)
- **Pedido do operador:** confirmar a pasta onde pmids/meta-análises/ensaios estão todos juntos. Resposta: `BIBLIOTECAS/MOTOR_CLINICO/`. Verificação apontou que só MA (268) e EC (58) estavam consolidados; gerado agora o consolidado de **todas** as referências: `MOTOR_CLINICO/evidencias_todas_serie.json` — **2.577 únicas** (dedup pmid_oficial; `bibliotecas[]` por registro; 102 multi-biblioteca): 268 MA/revisão sistemática · 58 RCT · 2.251 nível base. rev.1: classe por prioridade MA>EC>base (1 conflito nomeado: PMID 30646157). Trilha `scripts_serie/trilha_consolidado_todas_motor_2026-09-11.json`. Derivação mecânica de leitura — 0 linhas de ciência, 0 artefatos governados alterados; README da pasta atualizado.

### 2026-09-11 — REGISTRO (rename consolidado do motor: evidencias_pmids_serie.json)
- **Pedido do operador:** nome consistente com ma/ec → `MOTOR_CLINICO/evidencias_todas_serie.json` renomeado para **`evidencias_pmids_serie.json`** (conteúdo idêntico, move; espelha `01_pmids.json`). README da pasta + trilha com rev. datada. 0 ciência tocada.

---

### 2026-09-11 — ABERTURA (Rodada 6 perícia externa: relatório integral do Agente Auditor sobre B1 V4.1)
- **O quê:** recebido `RELATORIO_AUDITORIA_INTEGRAL_B1_CANONICA.md` (veredito APROVADA COM RESSALVAS; AUD-026…048; condições R1–R13). Método da casa aplicado: cada achado replicado antes de aceito — portões oficiais re-rodados (gate 16/16, checklist 41/41 B1, framework B1, contrato), arquivos do workspace e **E-utilities PubMed ao vivo** (esummary+efetch: 36231075, 34847455, 39595067, 40036275, 31195092, 17639827, 21605657…).
- **Resultado da réplica (registrado em `_documentos_serie/RESPOSTA_AUDITORIA_AGENTE_B1_V41_2026-09-11.md`):** 17 itens ACEITOS (incl. **os 2 GRAVE** — AUD-026 Almulla: KYN "redução" invertida, abstract confirma "KYN unaltered/QA↑/KA↓/TRP↓/KYN/TRP↑ só psicótico"; AUD-027 Comai: seletividade "bipolar but not unipolar" apagada), 4 PARCIAIS (AUD-034 omissões reais 12/13 mas "36 incorporadas" não se sustenta nos artefatos internos — 49 AT em N1; AUD-038 ano 2007 errado OK mas "abstract existe" FALSO — PubMed não tem abstract; AUD-043/031 parciais de escopo), **1 FALSO POSITIVO completo: AUD-040 (Sublette "melhor especificidade")** — frase não existe nem em v4 nem em V4.1; texto vigente é idêntico ao título PubMed 21605657. 2 observações aceitas.
- **Execução:** R1–R2 = conteúdo científico ⇒ **V5** (regra do operador); R3–R8/R11 na mesma manutenção (metadado/rodapé/tabela); R9–R10/R12–R13 nomeadas. Aguardando comando de execução — plano completo na resposta.

### 2026-09-11 — REGISTRO (carta-resposta ao Auditor-Mestre — envio pelo operador)
- **Artefato:** `_documentos_serie/RESPOSTA_AO_AUDITOR_MESTRE_B1_V41_2026-09-11.md` — resposta formal item a item ao veredito APROVADA COM RESSALVAS: 2 GRAVE aceitos com prova eutils (→ V5 pela regra do operador), 11 MODERADOS aceitos (com replicação), 3 parciais (AUD-034 omissões reais mas contagem 36 não sustentada — 49 AT/49 em N1; pedida cópia do insumo de reconciliação; AUD-038 ano OK/"abstract existe" refutado — PubMed sem abstract; AUD-017-escopo), **AUD-040 REFUTADO com prova tripla** (V4.1 + v4 histórico + título PubMed 21605657 verbatim-espelho), compromissos R1–R13 mapeados 1:1, confissão institucional do erro de rastreio da Lista Canônica. Ciência: 0 linhas alteradas neste ato (a execução das correções é a etapa seguinte).

---

### 2026-09-11 — ABERTURA (EXECUÇÃO R1–R13 → Canônica B1 V5 + governança — pós-réplica do auditor)
- **Contexto:** réplica do Auditor-Mestre recebida (3 erratas do próprio auditor: AUD-040 retirado, AUD-038 reduzido ao ano, AUD-034 13→12; veredito APROVADA COM RESSALVAS inalterado; **status canônico PROVISÓRIO obrigatório na V5** até revisão cega dos 59; lote de re-auditoria definido). Operador lembrou a regra `antigos/`/`atuais/` para toda atualização.
- **Escopo desta execução:** (1) **Canônica V5** (conteúdo ⇒ sobe o principal): R1 Almulla, R2 Comai + vínculo G3 correspondente, R11 (Gavril rótulo, Wijesinghe, Enache, Hafizi-2007, §7.2 "()"→Lang 2025 — Sublette: nada, AUD-040 retirado), R7 tabela sem "PCR>3", rodapé metadados alinhado + status PROVISÓRIO declarado (R9–R10 obrigatório); v4.1 → `antigos/historico/` com data; (2) **R3** vínculos: 19 g3_nota / 30 claim_id (só o recuperável; resto dívida nomeada); (3) **R4** Lista Canônica v1.2; (4) **R6** manifesto 237/33 + nota v2.1→v2.6; (5) **R5/R8/R12** em decisoes_B1.md (12 PMIDs com esummary; ANNETT_2020; 16 órfãs; ratificação ordem invertida); (6) portões re-rodados + CHANGELOG fechado com números.
- **Resultado:** anexado ao fim.

### 2026-09-12 — RESULTADO (EXECUÇÃO R1–R13 → Canônica B1 V5 + governança) — ciclo FECHADO, portões verdes

- **(0) Regra antigos/atuais:** `B1 NEUROINFLAMAÇÃO V4.1 CANONICA.md` removida de `atuais/` após prova de identidade sha256 com a cópia assinada `antigos/historico/v4_1_canonica_pos_auditoria_integral_2026-09-11.md` (43b7673bd2f9d65f, os 3 arquivos idênticos). `atuais/` passa a ter **somente a V5**.
- **(1) Canônica V5:** já criada na sessão anterior (15/15 substituições assert · sha 1b3ff6f759d69e5b) + nesta sessão o item 9 do REGISTRO (R8) e a remoção do token ANNETT_2020 do APÊNDICE (sha final 3c6dda4d2f319dd6).
- **(2) R8 (AUD-032, 17 órfãs):** 16 vínculos criados (VINC_B1_0258–0273) do ledger, âncora = linha-lote literal do APÊNDICE DE CORPUS (verificação computada: NENHUMA das 17 tem citação nominal em prosa; convenção de âncora idêntica à do próprio ledger); REF_ANNETT_2020 removida do Módulo 09 + apêndice (isolada sem prosa; zero-citação-nova) com AUD_B1_0075 preservada verbatim na trilha; 23 âncoras de ledger re-apontadas. Contagens finais: **01=200 · 02=33 · 03=3 · módulo09=236 · ledger=236 · vínculos=273**. Trilha `producao/11_R8_orfas_B01_2026-09-11.json`.
- **(3) R3 (AUD-036):** 15/19 PARCIAIS já tinham g3_notas com motivo (item a item); 4 sem nota (VINC_B1V2_0190/0197/0198/0202) receberam nota reconstruída do ledger + `reavaliacao_g3_pendente: true`; 30 VINC_B1V2 sem claim_id: herança por co-ocorrência = **0/30 elegíveis** → dívida D-B1-R3-V2CLAIM. Trilha `12_R3_parciais_v2_B01_2026-09-11.json`.
- **(3b) Manutenção descoberta no ciclo (confissão de método):** 159/273 âncoras de vínculo não literais por espaçamento/pontuação (deriva pré-existente — o framework só checa âncora do LEDGER). **124 reparadas** mecanicamente (sítio único, sim ≥0.985; método rev1/rev2 corrigido na mesma sessão e a correção registrada na trilha — a 1ª medição "159 fora" estava certa, a 1ª classificação "deriva de conteúdo" estava errada: era pontuação); **35 com deriva lexical 0.90–0.985 → dívida D-B1-ANCORA-DERIVA** (lista na trilha 13; decisão humana, a IA não reescreve âncora com troca de palavras).
- **(4) R4 (AUD-035):** Lista Canônica → **v1.2**: 78/83 `em_busca`→`usado_em_biblioteca` (+`uso_registrado`); 5 permanecem em_busca; 2 claim_ids em uso sem item (B1.MEC.BLOCO03.017, B1.MEC.BLOCO10.004) = dívida D-B1-R4-2CLAIMS. Backup `.bak_preV12_2026-09-11`, CRLF preservado, trilha 14.
- **(5) R5 (12 PMIDs):** rastro factual: **11/12 nunca entraram no nosso funil** (ausentes de matrizes/corpus/log — candidatos externos do auditor, não omissões de corpus); 29895691 (McKenzie) candidato sem G1 (`g1[pmid]=null`) e fora do at_final. Decisão: **10 → incorporar no próximo [AT]** (prioridade sub-bloco suicidalidade; rito G1+G3); **2 → não-incorporar motivado** (27221623 redundância; 29895691 opcional+cobertura). Registro completo em `decisoes_B1.md` rev.3.
- **(6) R6 (AUD-037):** manifesto sincronizado por contagem de arquivo: pmids_total 184→**236** (dedup), meta_analises 6→**33**, +ensaios_clinicos=**3**, +referencias_total_modulo09=**236**, versao 2.5→2.6 (divergência de rotulagem confessada), `artefato_rotulo`→"CANONICA V5 — status PROVISÓRIO", +`status_canonico: PROVISÓRIO` (R9–R10) + 6 entradas em `alteracoes[]`.
- **(7) R12:** ordem invertida RATIFICADA ex post (`matriz_b1_at_final.json` presente: 49 entrantes todos no Módulo 09 + 19 rejeitados com motivo; auditoria ref-a-ref anterior à incorporação, elo a elo datado). **R13:** log completo não preservado (workspace tem top-10/622) → declaração honesta + dívida D-B1-R13-LOG (reconstruir de eutils no próximo [AT]; queries na Lista v1.2).
- **(8) Portões (2026-09-12):** gate **APROVADO** (nota informativa [6]: 38 claims alto-risco — mitigação P-6 declarada) · checklist **41/41** · framework **0 ERRO** (236 avisos [TAG] não-bloqueantes, padrão da série) · censo 16 bibliotecas: **32/32 linhas BLOQ 0** (B1: vínculos 273, ledger 236, 0 bloqueios) — saída em `producao/censo_pos_R1_R13_2026-09-12.txt`.
- **Dívidas nomeadas do ciclo:** D-B1-R8-CLAIM (16) · D-B1-R3-V2CLAIM (30) · D-B1-R3-G3NOTA (4) · D-B1-R4-2CLAIMS (2) · D-B1-ANCORA-DERIVA (35) · D-B1-R13-LOG (1). **Nada fabricado:** o não decidível virou dívida com evidência negativa computada.
- **Pendente (lado do usuário):** envio do lote de re-auditoria ao Auditor-Mestre (V5 + manifesto + vínculos + Lista v1.2 + decisoes_B1.md + matriz_b1_at_final.json + trilhas + lista dos 59 + instrumento da revisão cega; anchormap e log completo declarados como dívidas de preservação de insumo).

### 2026-09-12 — EXECUÇÃO (lote de re-auditoria B1 V5 montado — sem alteração de conteúdo)
- **O quê:** pasta `B01_Neuroinflamacao/atuais/producao/LOTE_REAUDITORIA_V5_2026-09-12/` com 20 itens + `MANIFESTO_LOTE.json` (sha256 por arquivo; cópias congeladas das fontes vivas). Mapa 1:1 ao §6 da réplica do Auditor-Mestre em `LEIA_ME_LOTE_REAUDITORIA_B1_V5.md`.
- **Gerados no lote:** (a) `FILA_REVISAO_CEGA_ALTO_RISCO_B1_2026-09-12.json` — **108 vínculos / 91 refs** (critério operacional declarado: união das classes nominais do relatório de fidelidade V3; cobertura completa dos 22 da rodada full-text; reconciliação honesta do "59" nominal não-preservado — superconjunto datado); (b) `INSTRUMENTO_REVISAO_CEGA_P6_PROPOSTA_2026-09-12.md` — rotulado **PROPOSTA** (não havia instrumento formal preservado; a ratificar pelo auditor); (c) `DECLARACAO_LOG_BUSCA_D-B1-R13-LOG.md` (dívida honesta do log completo); cópia literal do log top-10 (622 linhas).
- **Hashes chave:** V5 `3c6dda4d2f319dd6…` · v4.1 preservada `43b7673bd2f9d65f…`.
- **Ciência:** 0 linhas alteradas (empacotamento). Pendência transferida: envio do lote ao Auditor-Mestre (ato do operador).

### 2026-09-13 — ABERTURA (Re-auditoria do Auditor-Mestre sobre o lote V5: análise F-01…F-10, condições C1–C6, novo portão P-8, lacunas L-01…L-16)
- **Recebido:** `ANALISE_FERRAMENTAS_E_LACUNAS_2026-09-13.md` + scripts `reparo_coerencia_2026-09-13.py` e `validar_coerencia_camadas.py` (via chat) + manifestos pós-reparo (2)/(3) + `PROPOSTA_AT_OSIMO_2019.json` (uploads).
- **Regra da casa (inalterada):** nada entra sem replicação. Ordem desta execução: (1) replicar as medições F-01…F-10 nos nossos arquivos; (2) auditar os 2 scripts linha a linha (desvios registrados); (3) `--dry-run` do reparo + inspeção item a item da trilha; (4) execução real com backups; (5) todos os portões (P-5, checklist, framework, **P-8**, censo); (6) RESULTADO abaixo.
- **Fora do escopo automático (ficam nomeados):** C3 (Osimo 2019 — próximo [AT]), C4 (BLOCO_11.4 — autor científico), F-04/L-03 (migração de âncora do ledger — decisão de esquema), L-01…L-16 (arquitetura — respondidas à parte).
- **Resultado:** anexado ao fim.

### 2026-09-13 — RESULTADO (Re-auditoria do Auditor-Mestre: reparo de coerência + trilhas 15/16/17 + ferramentas F-08/F-09 + varredura série família-Hafizi) — ciclo FECHADO

- **(1) Replicação ANTES (regra da casa):** F-01…F-10 confirmadas nos nossos arquivos (280 citações narrativas —
  regex oficial ~7–8%; 0 âncoras `[REF_BLOCO_XX:…]`; 236/236 âncoras de ledger em linha-lote; 221/236
  citacao_literal-TOKEN; 0 âncora com "(Autor, ANO)"; docstring do gate prometia o que não fazia; checklist com
  `/home/user` hardcoded; manifesto dessincronizado AUD-056/057). Dry-run do reparo replicou seus números
  EXATOS (R-01 4 · R-02 12/16 · R-05 34 · R-06 5 · R-07 0).
- **(2) Execução real:** reparo de coerência (trilha 15; backups ×6; **manifesto final idêntico ao do auditor**,
  0 campos divergentes; P-8 pós 6 ERRO/24 AVISO = número dele) → trilha 16 (VINC_B1_0005 + Steiner 0175
  re-ancoradas) → **trilha 17: rename Hafizi 2005→2007 completo** (ficha id + campo-lista; vínculos; ledger id +
  citacao_literal + 25 âncoras propagate; 1 token na canônica, 0 prosa; sha 3c6dda4d→**5051080b**; manifesto com
  sha vigente). Assert: nenhum campo vivo usa REF_HAFIZI_2005 (notas históricas datadas preservam o id antigo).
- **(3) Ferramentas (F-08/F-09):** aplicado o equivalente descrito pelo auditor (arquivos dele não anexados —
  desvio registrado): `checklist_entrega.py` com caminhos relativos a `__file__`; `gate_script.py` com docstring
  honesta + "COBERTURA QUE ESTE PORTÃO NÃO TEM" → P-8. Backups `.bak_F08/F09_2026-09-13`. Patches da casa no
  material dele: `nota()` string (não-lista) no reparo; validador P-8 tolerando `corte_literatura` string/dict.
- **(4) Portões (todos verdes no envelope contratual):** gate APROVADO · checklist **41/41** · framework
  **0 ERRO** · **P-8 4 ERRO / 24 AVISO** (V-02 = 0261/0262/0265/0266 → fila humana; V-01 0; V-05 0; V-13 OK) ·
  censo série **32/32 BLOQ 0**. Avisos residuais não-bloqueantes: V-06 18 heurísticos, V-08 4, V-09 34/273
  (12,5% < 25%), V-10 221 tokens (aguarda F-04/L-03).
- **(5) Varredura série família-Hafizi (`_documentos_serie/VARREDURA_FAMILIA_HAFIZI_B1_B16_2026-09-13.md`):**
  2.689 fichas; **1 caso nominal achado e RESOLVIDO: B13 `REF_SAITO_1999→REF_SAITO_2010`** (rito completo;
  trilha B13 producao/01; backups ×5; eutils pubdate 2010; B13 re-validada gate+framework 0 ERRO); **3
  epub×print** (B09 Gebara 2020/2021, B09 Scaini 2021/2022, B14 Schweizer-Schubert 2021/2020) → **dívida
  D-SERIE-CONVENCAO-ANO-ID** (recomendação: pubdate-ano NLM; autor científico decide); B05 Du 2023 = falso-
  divergente do parser v1 (eutils confirma 2023); 3 fichas B06 sem ano detectável (trabalho nomeado).
- **(6) Dívidas atualizadas:** D-B1-ANCORA-DERIVA **ENCERRADA** (35/35) · D-B1-R8-CLAIM 16→**residual 4**
  (0261/0262/0265/0266 na fila humana) · novas: D-SERIE-CONVENCAO-ANO-ID (3) · permanecem: D-B1-R3-V2CLAIM (30),
  D-B1-R3-G3NOTA (4), D-B1-R4-2CLAIMS (2), D-B1-R13-LOG (1). **Confissão C1 (propagação) registrada em
  decisoes_B1.md rev.4.**
- **(7) Descoberta arquitetural:** 1ª corrida do P-8 fora da B1 → **B13 = 167 ERRO V-02** (âncoras em
  linha-lote; perfil da B1 pré-R1–R13) — as 15 demais bibliotecas precisarão do mesmo ciclo de reancoragem
  (valida a etapa 5/da Parte IV do plano dele).
- **Pendente:** C3 Osimo 2019 (próximo [AT], ficha pronta) · C4 BLOCO_11.4 (autor científico) · F-04/L-03
  (migração de âncora do ledger — decisão de esquema) · L-01…L-16 (carta-resposta em `_documentos_serie/`).

### 2026-09-13 — ABERTURA 2 (Continuidade da re-auditoria: ERRATA do Auditor-Mestre E-01…E-05 + parecer)
- **Recebido:** `ERRATA_E_PARECER_CONTINUIDADE_2026-09-13.md` (V-14 implementada; R-05 reparado com
  fatia_literal; V-07 3-formatos; V-05 universo-fix; reconciliação 24×22 → **22 da casa correto**;
  convenção pubdate-NLM endossada; tabela V-02 de série ≈1.514/2.495 = 61%; parecer: manter casa e
  método; novo critério de replicação: P-8 0 ERRO V-02 na piloto E em mais uma; lacuna nova L-17) +
  os 4 scripts oficiais corrigidos (validar_coerencia_camadas.py, reparo_coerencia_2026-09-13.py,
  gate_script.py, checklist_entrega.py).
- **Delegação nova do operador (registrada):** "use a ciência e a engenharia de software para decidir
  os caminhos; a equipe humana de especialistas revisa no final, quando a plataforma estiver pronta."
  Aplica-se a: re-ancoras V-02 da B01, convenções técnicas e redações de método (C4) — sempre com
  nota datada e trilha; NÃO se aplica a inventar dado científico (proibido sempre).
- **Foco do operador:** B01. Ordem: (1) adotar os 4 scripts com conferência bilateral empírica;
  (2) replicar a tabela V-02 de série com o script dele; (3) re-ancorar os 4 vínculos B01 restantes
  com justificativa científica (delegação) → P-8 fecha V-02 na piloto; (4) C3 Osimo 2019 no rito [AT]
  + correção §11.1 + C4 BLOCO_11.4 → **conteúdo científico: sobe o principal (V5→V6)**; (5) governança
  + carta. Resultado anexado ao fim.

### 2026-09-13 — RESULTADO 2 (rodada de continuidade concluída: etapa 0 do parecer cumprida na piloto)
- **Antes:** B1 V5 sha `3c6dda4d…`→(trilha 17)→`5051080b…`; P-8 4 ERRO V-02 (0261/0262/0265/0266, fila
  aguardando decisão); C3 Osimo com ficha pronta não aplicada; C4 pendente; scripts da casa com patches
  defensivos nossos; tabela V-02 de série medida só pelo lado dele.
- **Depois:** **B1 CANÔNICA V6** sha `e11dbd959c59d191…` (errata mesmo dia: H1 interno V5→V6, achado do operador, sem toque científico; sha intermediário `d8f41662c4e41ec3…` preservado em historico) (V5 preservada bit-a-bit em
  `antigos/historico/v5_canonica_pos_reauditoria_master_2026-09-13.md`; manifesto 2.7;
  237 refs · 274 vínculos · 237 ledger; 34 MAs com REF_OSIMO_2019). Trilhas 18 (re-ancoras V-02 por
  autoria; rev.1 confessa a ida-e-volta inicial→sufixo), 19 ([AT] C3 Osimo completo; rev.1 enum+query),
  20 (C4: não-validação + circularidade do Critério C). 4 scripts oficiais da ERRATA instalados verbatim
  (backups `.bak_pre_oficial_2026-09-13`; versões dele = superconjunto — nossos patches aposentados).
- **Portões (computados, V6):** gate **APROVADO** · checklist **41/41** · framework **0 ERRO/236 AVISO** ·
  **P-8 0 ERRO/25 AVISO** (V-02 **0** = nova fronteira; V-05 96,9%; **V-14 14/14**) · censo série
  **32/32 BLOQ 0** (1 bloqueio transitório enum `elegivel`→`eligible` achado pelo próprio censo e
  corrigido com rev.1).
- **Réplica bilateral da tabela §4 dele:** P-8 oficial nas 16 (JSONs em
  `_documentos_serie/replicacoes/2026-09-13_P8_serie/`): **15/16 exatas**; única diferença = B01
  (ele 273/5 com dados pré-V6 × casa 274/0 hoje — diferença = o trabalho desta rodada, fecha
  aritmeticamente: totais 2.496/1.509 × 2.495/1.514). B02 confirmada: 126 órfãs V-04 + 7 V-05.
- **Dívidas:** **D-B1-R8-CLAIM 4→0 ENCERRADA** (decisão científica da casa sob delegação do operador);
  observação-L717 (FKBP/Mehta) → fila P-6 (não decidida, nunca fabricada); L-17 aceita (pacote de
  schema); demais dívidas nomeadas mantidas. **P-6 permanece** — revisão humana de especialistas no fim.
- **Governança:** decisoes_B1.md rev.5 · STATUS_SIMPLES atualizado · ROTEIRO (etapa 0 FECHADA; próximo:
  pacote de schema L-05/L-06/L-13 + reancoragem série quando houver 0 ERRO em mais uma biblioteca) ·
  2ª carta ao auditor: `_documentos_serie/RESPOSTA_2_REAUDITORIA_AUDITOR_MESTRE_2026-09-13.md`.

- **Errata 2026-09-13 (pós-RESULTADO 2):** H1 interno da V6 ainda dizia V5 — apontado pelo operador.
  Corrigido na liturgia (backup do sha intermediário em `antigos/historico/v6_canonica_sha_d8f41662_pre_correcao_titulo_2026-09-13.md`,
  manifesto com `historico_sha_v6`, portões re-rodados: gate APROVADO · 41/41 · framework 0 ERRO · P-8 0 ERRO · V-13 confere novo sha).
  Também corrigida no rótulo L5 a convenção homônima vigente (sufixo de ano — trilha 18 rev.1). SEM mudança de conteúdo científico.

### 2026-09-13 — ABERTURA 3 (Parecer rodada 3: C4-algoritmo + AUD-066 + AUD-067 + §3 taxonomia + réplica)
- **Recebido:** `PARECER_B1_V6_E_PLANO_TRIO_2026-09-13.md` (rodada 3): C3 ENCERRADA · C4 PARCIAL
  (declaração exemplar, algoritmo inalterado — permanece aberta; 2 correções mínimas sugeridas) ·
  achado novo GRAVE: **3 taxonomias de classificador, nenhuma autoritativa** (prosa×apêndice×balde;
  pede declaração de semântica normativa; recomenda portão V-15) · **AUD-066** (4 números p/ a mesma
  condição PROVISÓRIO: 59/108/39/~58 — escolher UM derivado de artefato) · **AUD-067** (Mehta pela
  metade: token da recompensa [L647] classificado como revisão no apêndice) · veredito **APROVADA COM
  RESSALVAS — base piloto** (4 impedimentos: P-6, C4, taxonomia, camada de evidência não auditada —
  a 4ª já sanável: o pacote-zip montado nesta data cobre exatamente o mínimo pedido por ele) · caminho
  do trio em 4 blocos · §7: reancoragem da série deve **virar script**.
- **Réplica executada ANTES de aceitar (trilha 21):** autodivergentes **7/7 exatas e as mesmas
  nomeadas**; concordância prosa×balde 39,6% × dele 37,1%; apêndice×balde **21,5% × 21,3%**; divergentes
  prosa×apêndice 84 × 71 (mesmo defeito; universo do parser declarado). Achado §3 CONFIRMADO.
- **Correções a aplicar na mesma liturgia (trilha 22) — conteúdo científico (algoritmo 11.4) ⇒
  sobe o principal: V6 → V7** (V6 final e11dbd95 preservada bit a bit):
  (1) **C4 decidida:** Critério C sai de condição de linha e vira **modificador de a priori/especificidade**
  (regra executável: A satisfeito APENAS por marcadores sistêmicos inespecíficos + C presente ⇒ rebaixa
  alta→indeterminada) — atende ao falso-positivo (obesidade+apneia) e ao falso-negativo (sem contexto)
  apontados por ele; perfis §12.1/12.3/12.4 harmonizados;
  (2) **AUD-066:** cabeçalho amarrado a UM número derivado de artefato = fila operacional
  `FILA_REVISAO_CEGA_ALTO_RISCO_B1_2026-09-12.json` (108 vínculos/91 refs) com a linhagem
  59→108→39(gate)→~58(carta) declarada;
  (3) **AUD-067:** eutils 2026-09-13 confirma REF_MEHTA_2020b = **Systematic Review, SEM Meta-Analysis**
  (confissão: a casa propagou [MA] na rodada 2) → ficha move 02→01_pmids, ledger AUD_B1_0151 MA→OB,
  apêndice MEHTA_2020[OB]→[EC] (ficha é EC fMRI) e MEHTA_2020b[MA]→[OB], **duplicata de token no
  apêndice removida com propagação das ~50 âncoras de ledger**; L717 (FKBP) → token 2020b por
  **eliminação de desenho** (única revisão Mehta 2020 do acervo; a outra ficha é EC — impossível),
  com confissão: sem confirmação nominal de FKBP5 no abstract; vínculo formal fica na P-6;
  (4) **declaração normativa §3 (posição da casa):** semântica vigente de fato ambígua — confessa;
  correção material das demais 6 autodivergentes e das ~84 divergentes entra no **pacote L-05/1.2
  (taxonomia única + V-15 aceita)**, não se arbitra desenho sem fonte primária.
- **Resultado** anexado ao fim, com portões re-rodados e sha novo.

### 2026-09-13 — RESULTADO 3 (rodada 3 concluída: parecer processado; B1 V7 vigente)
- **Antes:** B1 CANÔNICA V6 final sha `e11dbd95…` (pós-errata do título); C4 só declarada; Mehta 2020b
  contada como MA no balde 02 e [MA] no apêndice; cabeçalho do PROVISÓRIO citando o "59" nominal;
  L717-FKBP aberta; taxonomia de classificador medida só pelo lado do auditor.
- **Depois:** **B1 CANÔNICA V7** sha `6e2c2979…` (V6 final bit-a-bit em
  `antigos/historico/v6_canonica_final_sha_e11dbd95_2026-09-13.md`; manifesto 2.8). C4 decidida no
  algoritmo (C = modificador de especificidade, regra executável; falso-positivo e falso-negativo
  corrigidos) · AUD-066 (PROVISÓRIO ← fila 108/91) · AUD-067 fechado por eutils (RS sem MA; ficha,
  ledger, tokens, duplicata, 50 âncoras; MAs 34→33) · L717→2020b por eliminação (vínculo N2 no P-6) ·
  §3 replicada e confirmada (trilha 21) · semântica normativa declarada (pacote L-05/1.2 + V-15 aceita).
- **Portões (computados, V7):** gate APROVADO · 41/41 · framework **0 ERRO**/236 · **P-8 0 ERRO**/26
  · censo **32/32**. Trilhas 21 (réplica) e 22 (V7, rev.1). Dois bugs da própria execução confessados
  e corrigidos (PMID/DOI no REGISTRO; alteracoes-string — L-17 na prática).
- **Governança:** decisoes_B1.md rev.6 · STATUS/ROTEIRO atualizados (Bloco 1 = próximo ato: L-05+L-06+
  L-13+C4 já decidida) · **carta nº 3** ao Auditor-Mestre em `_documentos_serie/RESPOSTA_3_PARECER_B1V6_AUDITOR_MESTRE_2026-09-13.md`
  · pacote-zip de evidências **atualizado para V7** (vai aos dois auditores; cobre o pacote mínimo do §0).

### 2026-09-13 — ABERTURA 4 + RESULTADO 4 (auditor externo de ESTRUTURA; portão P-5 rev.A2)
- **Recebido:** parecer do 2º revisor (estrutura): pacote reproduzido em máquina limpa (18/18 · gate
  APROVADO · framework 0 ERRO/236 — B1 validada) + 6 achados de código sobre o portão P-5.
- **Réplica (trilha 23): 6/6 confirmados** — incluindo o campo `uso` fora do enum v3.1 com
  `nucleo_causal`×0 (ramo morto do alto-risco: mesmo padrão do bug tier_1/2026-09-10, 2ª ocorrência) e
  o selo por frase especificado e não implementado (8 pendente/7 CONFIRMADO+pendente — bateu no número).
- **Correção:** `gate_script.py` **rev.A2** (backup do oficial; proposta ao Auditor-Mestre): Bloco H
  completo com contadores por critério (51/38) · E1/E2 viram FALHA · E3 INFO (2 casos) · INFO permanente
  `uso` fora do enum · selo por frase implementado (1 full-text nomeado; 7 índice-APENDICE) · bypass
  `citacao_confirmada` banido (dependência=FALHA; campo preenchido nas 237 fichas=INFO — descoberta da
  própria execução, confessada).
- **Portões pós-patch:** gate rev.A2 APROVADO · 41/41 · framework 0 ERRO/236 · P-8 0 ERRO/26.
- **Dívidas novas nomeadas (pacote L-05):** D-A2-USO-ENUM · D-A2-HIGH-VAZIO · D-A2-CC-ORIGEM ·
  D-A2-E3-2 (P-6).
- **Governança:** decisoes_B1.md rev.7 · carta ao auditor de estrutura
  (`_documentos_serie/RESPOSTA_AUDITOR_ESTRUTURA_2026-09-13.md`) · pacote-zip **V7b** (com o gate
  rev.A2 e as saídas novas) para os dois auditores.

### 2026-09-13 — ABERTURA 5 + RESULTADO 5 (Auditor-Mestre rodada 4: pacote V6 verificado; rodada 5 dele = pacote V7)
- **Recebido:** `PARECER_PACOTE_B1_V6_VERIFICADO_2026-09-13.md` — auditou o pacote **V6** (erro de
  entrega: a carta 3 descrevia a V7). Tudo reproduzido exato (18/18 hashes; contagens 237/274/237;
  gate APROVADO; framework 0 ERRO/236; P-8 0 ERRO/25 — medição dele na V6). **AUD-066 ENCERRADO**;
  **camada de evidência ENCERRADA**; Mehta validado em fonte primária; recusa L717 julgada correta;
  adota nosso **84** como referência do §3. **C4 aberto na contabilidade dele apenas até a V7 chegar.**
  Novo achado: **12 tokens com dois classificadores + 3 tokens temáticos sem autor**. Propõe **V-16**.
  Aceita **B13** como "mais uma" da replicação — **reancorador escrito ANTES, B13 = 1ª execução**.
  Condição única da rodada 5: **pacote da V7 no mesmo formato**.
- **Confissão processual:** erro de versionamento de ENTREGA (3 zips homônimos; canal humano pegou o
  superseded). Correção: prefixo `SUPERSEDED_` nos pacotes antigos + `PACOTE_VIGENTE.txt`.
- **Réplica (trilha 24, na V7):** V-16 **confirmada** (manifesto ainda dizia V5) → **errata manifesto
  2.9** (rótulo V7; `refs_01_pmids_base` 201; motivo PROVISÓRIO amarrado à fila 108/91; canônica
  intacta) → re-medição **V-16 OK 4/4**. Tokens ambíguos **confirmados com resolução por camada**:
  apêndice interno 0 (Mehta zerado pela V7) · 6 no índice inline · 5 divergentes apêndice×índice ·
  1 nome-duplo (STEINER) · união 11/12 dele + 1 novo (QUIMIO_META82). Temáticos identificados por
  contexto: Psoriase_2025↔REF_KEENAN_2025 · PrimingPrinc_2018↔REF_HERMAN_2018 · Stress_Epi_2019 sem
  ficha (dívida). FP meu confessado na trilha rev.0→rev.1 (REGISTRO narrativo citando token antigo).
- **NÃO feito (fronteira):** nenhum [XX] tocado → **D-B1-R4-TOKENS** ao pacote L-05/1.2 com V-15.
- **Portões pós-errata (2026-09-13):** gate rev.A2 APROVADO exit 0 · 41/41 · framework 0 ERRO/236 ·
  **P-8 0 ERRO/26** · censo **32/32 BLOQ 0**.
- **Governança:** decisoes_B1.md **rev.8** · **carta nº 4** ao Auditor-Mestre
  (`_documentos_serie/RESPOSTA_4_PARECER_PACOTE_B1V6_MESTRE_2026-09-13.md`) · **pacote-zip V7c**
  (= condição única da rodada 5 dele cumprida: V7 + manifesto 2.9 + trilha 24 + rev.8).

### 2026-09-14 — ABERTURA 6 + RESULTADO 6 (auditor de ESTRUTURA: proposta L-05 v1.0)
- **Recebido:** schema de evidência (Nível 1) + vínculo multi-entidade (Nível 2) v1.0 com mapa de
  migração medido + 5 decisões devolvidas ao projeto.
- **Réplica (trilha 25):** 14/16 alvos exatos; 2 com correção de precisão (secao_origem: 92 valores
  em 3 formatos, tese confirmada; o "1 inválido" era REF_OSIMO_2019 — typo da casa na C3 — e não a
  dívida full-text). **Errata T25 aplicada** (ficha + manifesto 2.10 + backup; portões verdes).
- **Veredito da casa: VIÁVEL e CORRETO — APROVADO como base do L-05/1.2 nos níveis 1–2**, com 6
  ajustes (R1 invariante principal → portão · R2 ids_oficiais.json derivado · R3 E2 pattern ancorado —
  falso-positivo demonstrado · R4 regras de migração da âncora · R5 manual de desenho + natureza=material
  revisto · R6 citacao_confirmada = default de geração, prova PROMPT v4.2).
- **Decisões respondidas com provas:** D1→A (rigor: régua do gate era a trocada; enum clínico = PROMPT
  v4.2 L1440) · D2→triagem semiassistida antes da leitura · D3→B1 antes de B2 pelos 20 redirecionados ·
  D4→resolvida documentalmente (default true de geração) · D5→três escopos declarados + dívida
  D-L05-CAMPO-DUPLO (renomeação no próximo major).
- **Dívidas novas:** D-L05-CAMPO-DUPLO · D-L05-IDS-JSON · D-L05-E2-PATTERN · D-L05-MANUAL-DESENHO.
- **Governança:** decisoes rev.9 · carta-parecer nº 2 (`RESPOSTA_2_AUDITOR_ESTRUTURA_L05_2026-09-14.md`,
  cópia ao Auditor-Mestre) · canônica V7 e sha intactos.

### 2026-09-14 — ABERTURA 7 + RESULTADO 7 (análise externa — "ChatGPT" — sobre o L-05 v1.0)
- **Recebido:** comentário de terceiro revisor trazido pelo operador: endossa o núcleo (evidência
  única × âncoras múltiplas; sem pastas por tipo) e pede atenção a 3 pontos (triagem dos 133;
  principal≠posse; papel≠veredito, caso Raison 2013) + sequência da D3 (nunca B1-antigo × B2-novo).
- **Verificação da casa (trilha 26):** exemplo Raison 2013 factualmente confirmado; regra "não posse"
  já estava escrita na proposta (re-endosso, não correção) — adotada como cláusula explícita na
  definição de `principal`.
- **Adotado formalmente:** **R7** — `papel` nunca é veredito (regra normativa) + eixo ortogonal
  `direcao` (sustenta/refuta/inconclusivo/condicional + condicao); `refuta` migra de `papel` para
  `direcao`. **D3 refinada:** consolidação só com a B1 inteira retroancorada em corte único; modelo
  nunca misto em produção.
- **Ajustes ao L-05 agora: R1–R7.** Adendo ao parecer nº 2 publicado
  (`_documentos_serie/ADENDO_1_PARECER2_L05_ANALISE_EXTERNA_2026-09-14.md`) · decisoes rev.10 ·
  canônica e portões intocados.

### 2026-09-14 — ABERTURA 8 + RESULTADO 8 (Auditor-Mestre: C4 ratificada; P-8 de 16 regras)
- **Recebido:** ratificação do C4 (ENCERRADA — 3 casos simulados + leitura integral do §12.3) +
  verificação do V7c (V-16 4/4; AUD-066 "da forma certa") + **novo P-8 oficial com V-15 e V-16**.
  Impedimentos restantes são os dois do plano: P-6 e taxonomia.
- **Réplica da casa:** números EXATOS dele (V-15: 94 ERRO/181 AVISO na V7; V-16 OK) — dívida =
  D-B1-R4-TOKENS com portão próprio, nada de não-conforme novo.
- **Achado da réplica:** delimitador do REGISTRO não casa o cabeçalho em negrito da B1; um ERRO
  (Mehta DENTRO-índice) era o falso-positivo já confessado da trilha 24 rev.0. Proposta fina de
  errata enviada (one-liner; 94→91 medido). Instalação verbatim com backup + sha registrado.
- **Portões:** gate rev.A2 APROVADO · 41/41 · framework 0 ERRO/236 · P-8 (16) = 94 ERRO / 207 AVISO
  (dívida nomeada) · **Bloco 1 formalmente destravado.**
- **Governança:** decisoes rev.11 · carta nº 5 ao Auditor-Mestre
  (`_documentos_serie/RESPOSTA_5_C4_RATIFICADA_P8_V1516_2026-09-14.md`).

### 2026-09-15 — ABERTURA 9 + RESULTADO 9 (operador: ARQUITETURA CONSOLIDADA DA PLATAFORMA — rodada documental, pré-motor)
- **Recebido:** `ARQUITETURA CONSOLIDADA DA PLATAFORMA.MD` (uploads/; sha256 `8f050469632ce3e8…`,
  37.466 B, 1.019 linhas, 23 seções) com pedido de transmissão ao Auditor-Mestre **antes** do arranque
  do motor clínico. Cadeia oficializada: **Biblioteca → Narrativa Transversal (NT) → Ontologia/Grafo →
  JSONs Modulares → Motor → Laudo** + **Pasta de Atualização** paralela (ciência recente, nunca
  equiparada ao canônico) + regra: necessidade estrutural = problema de contrato, nunca remapear a
  ciência da B1. Cópia verbatim arquivada: `_documentos_serie/ARQUITETURA CONSOLIDADA DA PLATAFORMA.MD`
  (sha idêntico, conferido).
- **Verificação factual computada antes de comentar (regra da casa):**
  (1) "146 IDs oficiais" → **EXATO** — catálogo `1º IDS_OFICIAIS.md`: 151 entradas menos 5
  `ids_removidos_definitivo` = **146 ativos** (suplementos 48 · exames 71 · mecanismos 16 · cenários 11);
  **errata da casa: o "103 ids" da trilha 25 (rodada 6) era parse parcial — corrigido aqui e na carta 6**;
  (2) constantes de segurança do motor (suporte_decisao_clinica etc.) **já são o cabeçalho oficial do
  próprio catálogo** — o documento ratifica norma vigente; (3) evidência única × âncoras múltiplas =
  correspondência exata com o acervo (incl. `MOTOR_CLINICO/` de 2026-09-11) e **4ª convergência
  independente** do princípio (L-05/auditor-2 · ChatGPT rodada 7 · casa · norma do operador);
  (4) esquema de relação §10 = convergente com o R7 (e com cuidado novo nomeado: `direção`-grafo ×
  `direcao`-epistêmica colidem — proposta `sentido_relacao` ≠ `direcao_suporte`);
  (5) **Pasta de Atualização NÃO EXISTE ainda** (busca: 0) — componente novo, exige contrato próprio
  (proposta **L-PU**); (6) NT não existe como artefato, mas "NT-B1" já constava do Bloco 2 do plano do
  Auditor-Mestre — o documento dá a definição normativa; exige **L-NT** + portão **V-NT**.
- **Rodada documental: 0 linhas de ciência** — sha da V7 recomputado = `6e2c2979…` (intocado).
- **Portões re-rodados nesta data (medidos):** gate rev.A2 APROVADO exit 0 · checklist **41/41** ·
  framework **0 ERRO/236** · **P-8 (16 regras) 94 ERRO/207 AVISO** (100% dívida nomeada V-15) ·
  **V-16 OK 4/4**. Série sem alteração desde o censo 32/32 BLOQ 0 de 2026-09-14.
- **Governança:** decisoes_B1.md **rev.12** (minuta L-05 1.1 re-enquadrada = Contrato da Cadeia;
  L-06 com fonte normativa no §21 do documento; regras de risco R-A…R-D; herança de enums R1–R7 com
  proibição de vocabulário paralelo) · STATUS_SIMPLES atualizado (rodadas 7–9; 7–8 registradas
  retroativamente — lapso da casa confessado) · ROTEIRO atualizado (Bloco 1 re-enquadrado) ·
  **carta nº 6** ao Auditor-Mestre (cópia auditor-2):
  `_documentos_serie/RESPOSTA_6_ARQUITETURA_CONSOLIDADA_NT_PRE_MOTOR_2026-09-15.md`.
- **Pendências inalteradas:** aceite do delimitador do P-8 (94→91) · v1.1 do schema (R1–R7) · minuta
  L-05 1.1 em preparação (nova forma: cadeia completa + anexos L-NT/V-NT/L-PU) · P-6 permanece.

### 2026-09-15 — ABERTURA 10 + RESULTADO 10 (ARQUITETURA CONSOLIDADA **V2** — mesma data, rodada documental)
- **Recebido:** `ARQUITETURA CONSOLIDADA DA PLATAFORMA V2 - 15.09.26.md` (uploads/; sha256
  `09692e18a5a65958…`, 46.129 B, 1.351 linhas, 30 seções) — o operador declarou "colocar as evidências
  bibliográficas no desenho"; pedido: atualizar o projeto para a V2.
- **Diff V1→V2 computado linha a linha (antes de aceitar — regra da casa):** confirmado o declarado E
  o delta maior: (1) diagrama principal redesenhado com **EVIDÊNCIAS BIBLIOGRÁFICAS → VÍNCULOS
  ("L-05 N1 + N2")** ao lado das NTs; (2) §5 reescrita + **5.1/5.2 citam `L05/schema_referencia_v1.1.json`
  e `L05/schema_vinculo_v1.1.json`** (o lugar oficial dos schemas do auditor-2 — já na versão pendente
  com R1–R7); (3) classificação não duplicada por pastas físicas (propriedade do registro — converge
  com auditor-2/rodada 7); (4) **§7 LIMITES DA NT nova** (proibições + "não converter relação
  mecanística em eficácia clínica sem sustentação" — adotada no L-NT); (5) bloco final da V1 (que tinha
  trecho com formatação corrompida) reescrito limpo em §23–§25 (+1 linha: "Vínculos preservam a
  relação entre evidência, claim e entidade"); (6) **novas seções de programa §26–§30** (piloto B1
  vertical · expansão multidomínio · motor em paralelo CONTRA os contratos, "não assumir a Biblioteca
  como camada final de consumo" · divisão de responsabilidades sem alteração silenciosa da autoridade
  da etapa anterior). Seções 23→30; §3 (146 IDs) inalterado.
- **Liturgia de supersessão:** V1 arquivada renomeada `SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA
  V1 - 15.09.26.md` (sha inalterado `8f050469…`); V2 arquivada verbatim com sha conferido; criado
  `_documentos_serie/ARQUITETURA_VIGENTE.txt` (ponteiro com nome+sha — regra nascida da errata dos
  zips). Notas de nome para o contrato: documento cita `/Evidencias/Bibliograficas`; diretório real =
  `Evidencias/Bibliografia` (recomendado o real); schemas em mãos = v1.0 × v1.1 citada = pendente R1–R7.
- **Rodada documental: 0 linhas de ciência** — sha V7 recomputado = `6e2c2979…` (portões da rodada 9
  desta data seguem medidos: gate rev.A2 APROVADO · 41/41 · framework 0 ERRO/236 · P-8 94/207 · V-16 4/4).
- **Governança:** **ADENDO 1 à carta 6** (`_documentos_serie/ADENDO_1_RESPOSTA6_ARQUITETURA_V2_2026-09-15.md`,
  vai anexo ao envio da carta 6) · decisoes_B1.md **rev.13** · STATUS_SIMPLES atualizado · ROTEIRO
  com referência vigente = V2. Minuta L-05 1.1 passa a citar a V2 (§2/§5/§7/§22/§25/§26–§29).

### 2026-09-15 — ABERTURA 11 + RESULTADO 11 (auditor-2 entrega **L-05 v1.1** com R1–R7 + operador pede envio da V2; rodada documental)
- **Recebido (mesmos nomes, conteúdo NOVO):** `schema_referencia_v1.json` + `schema_vinculo_v1.json`
  (descrição "**PROPOSTA v1.1**"; `$id: L05/schema_*_v1.1.json` — os caminhos EXATOS que a V2 cita) +
  proposta MD com **CHANGELOG v1.0→v1.1 + ERRATA v1.0 (3 erros dele) + §7 R2 + §8 R3 + §9 pointer**.
  Arquivado verbatim: `_documentos_serie/L05_v1.1_recebido_2026-09-15/` (shas na trilha 27).
- **Réplica estrutural completa ANTES de aceitar (trilha 27, simulação em cópia — zero dado escrito):**
  (a) **R1 contraproposta** (`ancora_principal` campo único — invariante eliminado por construção):
  **ACEITA** (simulação: 274/274 ∈ catálogo; V-17 aposentado p/ este item); (b) **R2/§7**: critério de
  aceitação dele **atendido** — derivador reproduz **146** (151−5) batendo `contagem.total_ids_validos:
  146` (L282) e por família; (c) **R3/§8**: padrão ancorado medido 237+274 = **0 FP** (substring morde
  exatamente 1 = Osimo, o exemplo dele); gate rev.A2 confirmado substring (L186–187) → proposta
  **rev.A3-E2** ao mestre na liturgia inversa; (d) **erratas dele conferidas**: 92/3-formatos EXATO ·
  Osimo = já corrigido pela nossa T25 de 2026-09-14 (hoje 0 inválido) — única pendência fina: rodapé
  da tabela §4B ainda com atribuição antiga (pedido de 1 linha); (e) **§9 pointer confirmado pela
  AUSÊNCIA**: kit da trilha clínica NÃO está no repositório da casa (só v3.1) → **pedido formal ao
  operador dos 5 documentos** (SCHEMA-CLAIM v1.2 · COMO EXECUTAR v1.7 · LISTA CANÔNICA B1/SM-02 v1.3 ·
  BLOCO DE ESTADO v1.6 · PROTOCOLO DE ESCOPO B1 v1.3).
- **Migração simulada (números honestos):** N1: 24/237 integrais puros; pendências = review **30**
  (exato) · desenho sinal-forte **40** / leitura **197** · origem 49/50 (50ª = Osimo → 1 linha de mapa
  declarada proposta) · status 162/162 · padrões 0 violações. N2: **243/274 integrais**; pendências =
  uso/trilha **30** (exatos) · `direcao`: triagem proposta casa (sustenta se CONFIRMADO/PARCIAL) 273,
  exceção ÚNICA **VINC_B1_0047** — o mesmo já nominado à fila P-6 · `forca_biologica` BLOCO_07/08:
  **24** medidos · enums vigentes 100% cobertos (zero remapeamento semântico nesses campos).
- **Veredito da casa: v1.1 APROVADA como base do L-05/1.2-normativo nos níveis 1–2.** Decisão 1
  encerrada na prática (v1.1 já implementa Opção A com `trilha`); Decisão 4 encerrada bilateralmente;
  Decisão 5 = 3 escopos + dívida (aceita dele). Perguntas à v1.1 (1 linha cada): papel principal =
  sustenta_mecanismo + fronteira nos 20 · triagem de `direcao` · colisão `direção`-grafo × `direcao`
  (V2 §11 × schema) → proposta: `sentido_relacao` na ontologia · rodapé §4B.
- **Transmissão oficial ao auditor-2 (pedido do operador): ARQUITETURA V2** — pontos: $id dele =
  citações §5.1/§5.2 da V2 (zero ajuste de caminho) · nota de nome (`Bibliograficas`×real
  `Bibliografia`) · §7 LIMITES DA NT asse o futuro V-NT sobre seus enums · Pasta de Atualização =
  sinalização (marcador epistemológico futuro, nada a desenhar hoje) · piloto §26–§29 inalterado.
- **Rodada documental: 0 linhas de ciência; simulação 100% em cópia.** sha V7 `6e2c2979…` intacto.
- **Governança:** decisoes_B1.md **rev.14** · **carta nº 3 ao auditor-2**
  (`_documentos_serie/RESPOSTA_3_AUDITOR_ESTRUTURA_L05_V11_ARQUITETURA_V2_2026-09-15.md`, cópia ao
  Auditor-Mestre) · STATUS/ROTEIRO atualizados. Pendências: 4 linhas-resposta do auditor-2 · derivador
  oficial (D-L05-IDS-JSON) · rev.A3-E2 (proposta ao mestre) · kit trilha clínica (operador) · P-6 fim.

### 2026-09-15 — ABERTURA 12 + RESULTADO 12 (Auditor-Mestre emite parecer sobre a V2 + resposta da análise externa; rodada documental)
- **Recebido:** `PARECER_ARQUITETURA_V2_2026-09-15.md` (audita o ARQUIVO V2, não o resumo — sha confere)
  + resposta do ChatGPT ao parecer (colada pelo operador, sem anexo). **Decisão estrutural do parecer
  (§1): os tokens editoriais da prosa saem do caminho de leitura do motor (V2 §28) → deixam de ser
  dívida de plataforma; V-15 passará a aviso-na-prosa/erro-em-ficha-vínculo**; §4 nomeia D-01…D-08
  (precedência entre mecanismos · combinação de forças · ausência de unidade · texto de ligação ·
  granularidade · Pasta de Atualização · determinismo · hierarquia de segurança).
- **Verificação antes de comentar (trilha 28, execução fresca do P-8):** §28 verbatim ✔ · D-07/D-08
  realmente ausentes da V2 (grep 0) ✔ · 94 ERRO = 19 DENTRO (6 prosa · 1 índice · 12 apêndice) + 75
  "divergente entre camadas" — **0 itens tocam ficha/vínculo → todos viram aviso no novo regime** ·
  seus 3 tokens-exemplo sem ficha ✔ · **NÃO reproduzidos** seus "158 temáticos/405 tokens": casa mede
  446 tokens AUTOR_ANO distintos (regex declarada) e 675 [XX] → pointer pedido (precedente 71×84).
  Confissão própria rev.1: regex "ENTRE" maiúsculo deu 0 na 1ª leitura (msg é minúscula) — corrigido
  na hora (mesmo padrão do FP trilha-24 rev.0).
- **D-B1-R4-TOKENS reescopada pela casa:** convenção editorial (sem bloqueio) + taxonomia migra para
  o que já existe na v1.1 (campos N1/N2 em enum) — trabalho medido: 197 desenhos · 30 review · 24
  forca_biologica · manual de classificação.
- **Análise externa verificada e ADOTADA com crédito:** restrição **D-01** (sem hierarquia artificial;
  escada de discriminação em 7 passos + preservar concorrentes com lacuna) · restrição **D-02** (sem
  escalar único → **solução da casa: piso POR EIXO** — saída carrega vetor natureza×desenho×força×
  maturidade×trilha, nunca excede elo mais fraco por eixo, laudo nomeia elo limitante) · campo
  `status_epistemologico` (fato/associação/causalidade/hipótese/evidência_direta/extrapolação/lacuna)
  fechando a exigência dele com o adendo técnico do mestre · adição D-06 (rastro da consulta à pasta)
  ao L-PU · template de 6 partes por decisão adotado.
- **Autoria do 1.1:** mestre redige os defaults (autorizado pelo operador via resposta); **a minuta
  da casa vira bancada de verificação** (cláusula a cláusula contra V2/acervo/trilhas) — sem duas
  normas concorrentes. Ordens de entrega (mestre × 9 fases) lidas como convergentes e registradas.
- **CARTA Nº 3 ao auditor-2 fica EM ESPERA por decisão do operador:** sai quando a V2 estiver
  resolvida bilateralmente (V2 + análises dos schemas no mesmo envio).
- **Rodada documental: 0 ciência.** Portões medidos hoje inalterados; sha V7 `6e2c2979…`.
- **Governança:** decisoes **rev.15** · **carta nº 7 ao mestre**
  (`_documentos_serie/RESPOSTA_7_PARECER_ARQUITETURA_V2_MESTRE_2026-09-15.md`) · STATUS/ROTEIRO.

### 2026-09-15 — ABERTURA 13 + RESULTADO 13 (minuta L-05 1.1 do mestre verificada na bancada + resposta do comentador; rodada documental)
- **Recebido:** `L05_1.1_CONTRATO_CADEIA_MOTOR_minuta1_2026-09-15.md` (sha `f91042b7…`, 241 linhas,
  **arquivada verbatim** em `_documentos_serie/L05_1.1_minuta_mestre_recebida_2026-09-15/`) + resposta
  do comentador externo com **4 correções finais**. A V2 citada pela minuta confere com o sha medido
  (`09692e18…`); B1 V7 intacta (`6e2c2979…`). **Casa cumpre o papel combinado: bancada de verificação
  cláusula a cláusula (trilha 29: regex, escopo, chave e comandos gravados).**
- **Parte 0 (reconciliação de números) REPRODUZIDA EXATA:** 102 linhas-lote · 405 prefixos distintos ·
  247/158 por prefixo · os 158 são temáticos (amostra gravada) · 4 lugares do `[XX]` confirmados
  (prosa fora das lotes = 7 pares; Módulo 09 = 201/33/3; `desenho_estudo_bruto` é o resíduo
  formalizado). **Pointer "158/405" ENCERRADO por réplica.** Aceite do delimitador 94→91 registrado.
- **ERRATA DA CASA (confessada):** o "446 tokens" da trilha 28 não é rederivável (a trilha não gravou
  o comando; grade completa hoje: 474/477 por regex declarada, 675 [XX] exatos). Sem efeito material;
  norma nova: **medida sem comando gravado não vale** — regex+escopo+chave+sha em todo registro.
- **Verificação contra os schemas v1.1:** eixos da D-02 divididos 2×3 (ficha N1 × vínculo N2) →
  corrobora o ponto 1 do comentador; D-01 §3: `contexto`/`sentido_relacao` inexistem como campo e o
  epistêmico real chama-se `direcao` → **dívida nova D-L05-NOMES-DIRECAO**; âncora formal de lacuna
  já existe (`natureza_relacao = nao_estabelecida`).
- **4 pontos do comentador verificados e ADOTADOS com crédito:** D-02 sem vetor homogêneo · D-03
  `inexistencia_cientifica` restrito (+ âncora machine-verificável) · D-07 determinismo qualificado
  (conteúdo clínico/semântico/estrutural + conjunto de versões; envelope não-semântico em lista
  fechada) · Parte 1 "As entradas autorizadas do Motor são:" (com a condição da casa: manter o
  "Não consome: a prosa (§28)"). Não se reabre D-01/D-04/D-05/D-06/D-08.
- **Decisão:** **minuta 1 APROVADA como base do contrato normativo** com as 4 correções + 3 precisões
  fáticas (F-1/F-2/F-3, errata técnica sem reabrir semântica). Contribuição própria: semântica por
  eixo (carta nº 8 §7) — `trilha` = metadado preservado, não ordenável.
- **Rodada documental: 0 ciência.** Filas: P-8 nova versão (prometida por ele) · kit clínica com o
  operador · **carta nº 3 ao auditor-2 EM ESPERA** até a V2 fechar neste eixo (ordem do operador).
- **Governança:** decisoes **rev.16** · trilha 29 · **carta nº 8 ao mestre**
  (`_documentos_serie/RESPOSTA_8_MINUTA_L05_1.1_MESTRE_2026-09-15.md`) · STATUS atualizado.
- **Adendo (rodada 13, continuação):** mestre registrou não ter recebido os schemas v1.1 — origem
  confirmada (auditor de estrutura, verbatim arquivado, shas publicados). Casa publica
  `_documentos_serie/ADENDO_1_RESPOSTA8_ORIGEM_SCHEMAS_V11_2026-09-15.md`: atribuição da citação,
  causa-raiz do F-1 (escrita sem artefato), guia mínimo de leitura e replicabilidade. 0 ciência.

### 2026-09-15 — ABERTURA 14 + RESULTADO 14 (minuta 2 normativa + P-8 em regime por camada, verificados e adotados; eixo V2 fecha bilateralmente)
- **Recebido:** minuta 2 do Contrato da Cadeia do Motor (sha `54ba243d…`) + nova versão do P-8
  (sha `0e67328e…`) — ambos arquivados verbatim. Bancada da casa executada (trilha 30).
- **Minuta 2 APROVADA:** diff 1→2 completo (268 linhas), **0 mudança silenciosa**; 4 correções do
  comentador + 3 precisões fáticas da casa + Anexo A (semântica por eixo, idêntico à carta 8 §7)
  incorporados; melhorias espontâneas dele: teste adversarial D-03 e lista fechada D-07 sob errata
  datada. §0.3 replicado EXATO no dado (0/237 e 0/274 ausentes; 274/274; nao_estabelecida 4× nos 4
  vínculos nomeados).
- **P-8 novo regime VERIFICADO e instalado como oficial:** diff = só o prometido (delimitador de
  REGISTRO em negrito · V-15 dentro/entre → AVISO [editorial] · bloco novo dos eixos D-02 com origem
  N1×N2). Oficial: **2 ERRO / 298 AVISO / exit 1** — 91 editoriais (18+73) = errata 94→91 por medição
  independente; 2 ERRO = `natureza_evidencia` e `trilha` ausentes (régua da D-02; corredor vermelho
  por desenho até a migração taxonômica). Backup + evidências B/A em producao/. Script anterior
  preservado em `.bak_oficial_pre_REGIME_CAMADAS_2026-09-15`.
- **Rodada documental: 0 ciência** (sha V7 intacto). **Governança:** decisoes **rev.17** · trilha 30
  · **carta nº 9 ao mestre** (`RESPOSTA_9_…2026-09-15.md`) · STATUS.
- **Destravado pela ordem do operador:** a **carta nº 3 ao auditor de estrutura** dispara com a V2
  final + análises dos schemas v1.1 (trilha 27) e trilhas 28–30 como prova de método.
- **Despacho (rodada 14, continuação):** carta nº 3 ao auditor-2 atualizada com nota datada de fecho
  (contrato do Motor aprovado · P-8 novo regime · âncora de lacuna · nomes) e pacote montado em
  `_documentos_serie/ENVIO_AUDITOR_ESTRUTURA_2026-09-15/` — 4 arquivos com LEIA-ME e shas
  (carta `17ad73d3…` · V2 `09692e18…` · trilhas 27/30). Pronto para o operador repassar. 0 ciência.
- **Governança (rodada 14, continuação):** publicado
  `_documentos_serie/MAPA_DE_AUTORIDADE_E_COMUNICACAO_2026-09-15.md` — papéis das 4 IAs + operador +
  P-6; schema×Motor como camadas da cadeia; regra de comunicação por artefatos; proveniência da V2
  (rascunho do comentador externo, adotado pós-verificação). 0 ciência.
- **Mapa v2 (rodada 14, continuação):** Claude 3 (narrativas/anamnese) acrescentado com parecer de
  engenharia — sem segundo Motor; papel de revisor cego (D-05); camada NT/anamnese sob sua curadoria;
  importação só de artefatos. Kit clínico (5 docs) formalmente cobrado do operador. 0 ciência.

### 2026-09-15 — ABERTURA 15 + RESULTADO 15 (L-06 minuta 1 + P-8 harmonizado, verificados; 0 ciência)
- **L-06 (especificação da D-01) APROVADA na bancada (trilha 31):** matriz 1.2 EXATA no acervo
  (109/100/56/4/4/1) · coerência total com a minuta 2 (fronteira D-02 · escada degradada da Parte 3 ·
  determinismo da Parte 4) · 1 errata fina (`condicao` = ausente no dado, não esparso) + 1 nota
  (degrau 5 já parcial via `extrapolado`, 62/274) para a minuta 2 da L-06.
- **P-8 harmonizado verificado e instalado como oficial (sha `76e526cf…`):** diff = somente o bloco
  pedido na carta 9 §4; dupla via de checagem byte-idêntica; **2 ERRO / 299 AVISO**; linha OK agora
  declara as duas leituras (preenchido × normatizado). Backup + evidência em producao/.
- **Governança:** decisoes **rev.18** · trilha 31 · **carta nº 10 ao mestre** · STATUS.
- **Kit clínico:** régua de envio fixada (operador envia à casa e ao mestre; casa mede e publica as
  digitais; mestre recebe os mesmos bytes).

### 2026-09-15 — ABERTURA 16 + RESULTADO 16 (nota do comentador externo sobre o P-8: replicada, 3 pontos adotados; 0 ciência)
- **Fluxo decidido:** nota crua NÃO segue ao mestre; os pontos **verificados** seguem na **carta nº 11**
  (padrão da rodada 13). Crédito ao comentador nos 3 pontos.
- **Réplica ponto a ponto (trilha 32, sha `76e526cf…`):** (1) V-06 — título "COERÊNCIA SEMÂNTICA"
  contradiz o próprio código ("Heurística de deriva"), a mensagem prudente e a §FILOSOFIA → retítulo;
  (2) V-08 — escopo "mesma linha" confirmado; **F-C1:** 6 atuais = 5 governança + 1 substantiva →
  status declarado de triagem, sem mudança de mecânica; (3) V-07 `related_entities` — comparava
  CONTAGEM em ramo `rel.erro`: **F-C2** contraexemplo executado (troca de ID com cardinalidade
  preservada passa muda; conjunto dispara) · **F-C3** o irmão `clinical_domains` já usa conjuntos;
  no dado real 15×15 idênticos → reforço preventivo antes da série.
- **Governança:** decisoes **rev.19** · **carta nº 11 ao mestre** · STATUS. Script oficial intacto
  nesta rodada (`76e526cf…`); revisão sai do mestre e a bancada aceita por totals idênticos + V-14
  verde + backup/B-A. **0 ciência.**

### 2026-09-15 — ABERTURA 17 + RESULTADO 17 (kit clínica arquivado e medido × B1 V7; 0 ciência)
- **Kit clínica recebido (7 documentos)** → pasta `_documentos_serie/KIT_CLINICA_recebido_2026-09-15/`
  byte a byte + digitais públicas. Mapa de leitura e digitais no **GUIA_ENVIO_KIT_CLINICA_AO_MESTRE**
  (operador repassa os mesmos bytes ao mestre). Item 1º (`_ids_oficiais.json`) não veio → cobrança
  nomeada ao operador junto de `CANDIDATOS_IDS_OFICIAIS.yaml` e `Estudos que não foram escolhidos.md`.
- **Medição central (trilha 33):** 49 PMIDs únicos dos 22 claims aprovados do kit: **10 (20,4%) na
  B1 V7 · 39 ausentes** (integral 4/parcial 4/zero 14) · **0 claims ligados formalmente** (namespaces
  SM-02 manual × MEC pipeline sem fio) · 3 fichas V7 com realocação no kit · 1 rejeitada PRISMA na V7
  (GARCIAGARCIA_2022 — conferir uso como intervenção) · enum `evid_role=review` (30 fichas) fora do
  enum do kit · cabeçalhos do kit dessincronizados do corpo + disposição dupla 20132991 + conflito
  humano 33339712/30696814.
- **Esclarecimento estrutural:** kit **alimenta** a biblioteca por design — não é produto separado;
  o "separado" observado é estado (duas linhas de claims), não decisão. Destrava §9-`uso`, régua 1.2
  (objeto real medido), matéria-prima da tipagem D-08 e **2 candidatos reais ao piloto L-06**
  (33339712/30696814 · C1q Luo×Yao&Li .013).
- **Governança:** decisoes **rev.20** · trilha 33 · STATUS. **0 ciência** (V7 `6e2c2979…` intacta).

### 2026-09-15 — ABERTURA 18 + RESULTADO 18 (parecer de engenharia: frente dedicada de produção de claims; 0 ciência)
- **Pedido do operador:** abrir novo projeto pago para produzir o kit de claims em paralelo ("não vão
  para as bibliotecas, vão para Evidencias/bibliografia").
- **Correção de premissa (referência: trilha 33):** objeto-claim mora nos artefatos do kit; FONTES
  aprovadas viram fichas do Módulo 09 em Evidencias/Bibliografia com claim_id_origem; narrativa
  consome via usado_em_biblioteca → "não vão para as bibliotecas" é errado no fim da cadeia; e a
  pasta-alvo das fichas está com o schema N1 em migração (2 ERRO do P-8 por desenho).
- **Parecer da casa:** projeto dedicado = SIM (o COMO EXECUTAR já prescreve "Modo B — Projeto");
  Claude 3 free NÃO (G3 exige abstract longo colado; trava). **4 portões antes:** (1) ressincronizar
  Bloco (13×22; incluir .017); (2) decidir 33339712/30696814 e a disposição dupla 20132991;
  (3) `_ids_oficiais.json` VIGENTE como item 1º (casa publica a digital se pedido); (4) repassar
  primeiro cartas 10/11 + ADENDO+kit v1.1 + guia do kit ao mestre (régua 1.2 vem de lá).
- **Recorte de escopo:** claims SM-02 SIM em paralelo (Schema-Claim v1.2 estável, artefatos do kit) ·
  fichas Módulo 09 NÃO até nascer o 1.2-normativo (não fabricar retro-trabalho) · não misturar no
  projeto do mestre (cegueira bilateral) · ordem: fechar SM-02 antes de SM-03 · Grupo 3 TSPO com a
  regra de texto completo v1.7.
- **Oferta da casa aguardando "vai":** validador executável Schema-Claim v1.2 (lint: enums,
  nota_ressalva obrigatória, comparador, sem TAB, chave única, capitalização) + trilha de réplica
  por leva. **Governança:** decisoes rev.21 · STATUS 18. **0 ciência.**

**Continuação (rodada 18):** complementos do kit recebidos e verificados — `1º IDS_OFICIAIS.md`
**byte a byte idêntico** ao catálogo oficial (sha `f3a74fbc…`, 146/5) → pendência fechada e digital
publicada para a frente de produção; `CANDIDATOS_IDS_OFICIAIS` (sha `556bb82d…`) com 12 entradas,
0/12 já catalogados, NLR/S100B em avaliação acionável; "Estudos que não foram escolhidos.md"
identificado como **referência da última linha do próprio BLOCO v1.6** — aguardando: existe (enviar)
ou não existe (ponteiro morto nomeado). Trilha 34 · decisoes **rev.22** · **0 ciência.**

### 2026-09-15 — ABERTURA 19 + RESULTADO 19 (L-05 schema: errata §4B e 4 pontos do comentador replicados; 0 ciência)
- **Auditor-2:** errata §4B verificada (1 linha; zero inválidos replicados) → item (iv) das 4 linhas
  encerrado; (i)-(iii) aguardando. Minuta nova arquivada (`1595011e…`); anterior SUPERSEDED_ + ponteiro.
- **Comentador externo:** 4/4 pontos CONFIRMADOS com crédito — (1) refuta na prosa × R7, com **adição da
  casa: R1 também não propagado à prosa §3** (defeito só de prosa; schemas corretos); (2) integridade
  ancora_principal → portão (oferta V-17: 3 testes); (3) regra anti-acréscimo automático adotada +
  **0/66 human_clinical intervencionais medidos** + guarda de migração (regime das 30 review);
  (4) status_auditoria N1×N2 → renomear N1 (= Decisão 5 dele).
- **Governança:** decisoes **rev.23** · trilha 35 · **carta nº 4 ao auditor-2** · STATUS. **0 ciência**
  (V7 `6e2c2979…` intacta; schemas intactos).
- **Registros administrativos:** ponteiro morto "Estudos que não foram escolhidos.md" declarado
  (17 PMIDs não encontrados); frente de claims clínicos pausada pelo operador (ofertas abertas).

### 2026-09-16 — ABERTURA 20 + RESULTADO 20 (revisão do mestre do P-8 replicada e instalada; kit clínica liberado p/ envio; 0 ciência)
- **Mestre:** revisão dos 3 pontos da carta 11 arquivada verbatim (`0cfe820b…`) e **replicada item a
  item** — baseline 2/299/exit 1 · F-C2 muda no script antigo · F-C2 dispara nomeando os dois lados no
  candidato · placar inalterado · V-14 verde (16 regras). Tudo conferiu.
- **P-8 novo oficial:** sha `84fa918d…` (antes `76e526cf…`, backup `.bak_oficial_pre_3pontos_R16_2026-09-16`).
  Escopo = só os 3 pontos; B/A gravado; invocação inalterada; os 2 ERRO por desenho intactos.
- **Notas L-06 replicadas:** `condicao` 0/274 (ausente) · `extrapolado` 62/274 → degrau 5 com meia perna.
- **Kit clínica:** envio AUTORIZADO com análise da casa (GUIA + ADENDO_1 novo: IDS resolvido
  `f3a74fbc…`, CANDIDATOS 0/12, ponteiro morto nomeado; escopo ancoragem/medida, produção pausada).
- **Fila:** eixo P-8 pendência zero bilateral; Fase 4 (L-NT, contrato das unidades narrativas)
  registrada como próxima do mestre; bancada segue taxonomia/IDS-JSON/rev.A3-E2 em paralelo.
- **Governança:** decisoes **rev.24** · trilha 36 · carta nº 12 ao mestre · STATUS. **0 ciência**
  (V7 `6e2c2979…` e manifesto `79d1309a…` íntegros por sha ao fim).

### 2026-09-16 — ABERTURA 21 + RESULTADO 21 (schemas L-05 v1.2 verificados; 3 pontos do comentador replicados; 2 adições da bancada; 0 ciência)
- **Auditor-2:** schemas v1.2 recebidos (sha `19f4f29a…`/`b8bcea80…`) — incorporação da carta 4
  **9/9 verificada** programaticamente; V-17 declarado na formulação da bancada; guarda 0/66 embarcada.
- **Comentador externo:** 3 pontos + obs — 4/4 CONFIRMADOS na bancada: (1) furo `condicao` provado
  com validador real + bloco de fecho medido em 5 casos; (2) sentido_relacao 0 em dados/21 em prosa
  → cláusulas retiradas, D-NOMES encerrada do lado L-05; (3) 20 redirecionados medidos (17 uso=clinico)
  → papel semântico, não de fluxo (funde com a linha (i) da casa); rótulo PENDENTE sai com Decisão 1.
- **Adições da bancada:** paradoxo do alias N1 (162/237 compostos passariam com canônico vazio) +
  superfície de migração quantificada (N2: 3 campos + uso 30; N1: 2 campos + desenho 175 valores +
  origem 50; 0 pattern) + 2 finos (`cross-over`; ponteiro forca_biologica — 24 na zona BLOCO_07/08).
- **Governança:** decisoes **rev.25** · trilha 37 · **carta nº 5 ao auditor-2** · STATUS.
  Falta para a 1.2: prosa §3 (R1+R7) + linha (ii) + fechos desta rodada. **0 ciência.**

**Continuação (rodada 21):** parecer formal v1.0 do comentador arquivado (`a1935438…`) e **replicado** —
veredito favorável condicionado confirmado como coerente com o nosso tabuleiro; 5/5 números verificáveis
conferem; 1 número indecidível (172/102) → **pedido do relatório de execução** ao auditor-2; §12/D4
envelhecida (proveniência já resolvida na v1.2); §13 (catálogo 146) = dívida da casa, demonstrada a
instabilidade de grep (parse estrutural fecha 146 exatos). Trilha 38 · decisoes **rev.26** ·
**ADENDO_1 à carta 5** · **0 ciência.**

**Continuação 2 (rodada 21):** cronologia do comentador corrigida (parecer veio antes dos JSONs); resposta
pós-JSON arquivada (`d4ad1545…`) e replicada — veredito "fechamento sem reestruturação" confirmado;
2 pontos novos com prova executável (pmid vazio passa onde não devia — fecho medido · texto de `uso`
impreciso — texto oferecido); medições de rodada fora das descriptions (adotado, eco da nossa norma);
convergências com carta 5 mapeadas; **tensão §3.3 × ponto 1 anterior nomeada** (confirmação pedida;
proposta da casa independe dela). Trilha 39 · decisoes **rev.27** · **ADENDO_2 à carta 5** · **0 ciência.**

### 2026-09-16 — ABERTURA 22 + RESULTADO 22 (mestre ancora o kit 9/9; diff reconciliado; precisão de escopo aceita; achado da camada a montante; 0 ciência)
- **Kit:** ancoragem 9/9 byte a byte pelo mestre (nomes mutilados no upload — o caso-didático das digitais).
  Sha da revisão por extenso recebido (prefixo confere; selagem byte só com arquivo).
- **P-8:** diff reconciliado (hunks 3 ✔ · −7 ✔ · +7 = comentário F-C2) — **casa adota as bytes do mestre**
  quando o anexo chegar (critérios: só comentário, 2/299/exit1, V-14, F-C2; backup; 1 sha viva).
- **Réplica das contagens dele no kit:** TODAS conferem após confissão datada nossa (escopo Bloco +
  chave livre): uso 23 (12/6/4) · comparador 59/8 · moderadores 22 · usado_em_biblioteca 23 ·
  evidence_role 22/22 · 43 SM02 × 0 MEC.
- **Correção nossa aceita:** o kit tipifica a SEMÂNTICA dos 2 ERRO; dados só na fatia humana
  (133 preclin + 30 review do acervo ficam com taxonomia/Decisão 2).
- **Achado arquitetural confirmado + adição da casa:** kit = camada ausente da V2 (0 wiring; fio
  projetado nas 2 pontas — `usado_em_biblioteca`×`claim_id_origem` — nunca executado). Decisão do
  operador; D-03 medida (4 gap_pesquisa × 4 nao_estabelecida); piloto L-06 preferido C1q.
- **Governança:** decisoes **rev.28** · trilha 40 · **carta nº 13 ao mestre** · STATUS. **0 ciência.**

### 2026-09-17 — ABERTURA 23 + RESULTADO 23 (comentário do comentador sobre a carta do mestre replicado; opção (c) registrada para a decisão da camada; errata fina da rodada 22; 0 ciência)
- **Recebido do operador** o comentário do comentador (ChatGPT) respondendo à resposta do mestre
  (ancoragem 9/9 + reconciliação do diff + achado da camada). Arquivado verbatim
  (`79f01bbe…` · 192 linhas) — a nota crua não circula; os pontos verificados viajam na carta da casa com crédito.
- **§3 (números do kit):** CONFERE na camada de valor em TUDO (uso 22=12/6/4 · ub 22 "nao"/0 "sim" ·
  comparador 48/8 valores (a dist citada confere exata) · moderadores 22 · ER 22/22 · gap 4 ·
  PMIDs 49 únicos/10 na V7/39 fora). Totais textuais citados (23/23/59) separados por camada com
  linhas espúrias nomeadas (prosa L182 · comentário L28 · prosa de comparador); "59" não reproduz
  no BLOCO isolado (hipótese fechada: 58+placeholder no SCHEMA=59). **Errata fina datada da rodada 22**
  (M2b): camadas agora nomeadas; nenhuma conclusão muda.
- **§6:** sustentado pelo próprio kit (instrução L87–92 "rastreabilidade… não bloqueia") +
  coerência de dados (sim 0/22 × claim_id_origem SM02 0/237).
- **§4/§5/§8/§9 (arquitetura):** "NT consome Biblioteca+Evidências" bate no §6 vigente da V2; MAS
  "Evidências = eixo paralelo" diverge do diagrama §2 (que só declara a **Pasta de Atualização** como
  paralela) — e coincide com o minidiagrama §5.3. **Dívida nova: D-V2-DIAGRAMA-DUPLO** (V2 tem dois
  desenhos internos opostos para Evidências). Kit = **0 ocorrências na V2** (inalterado); kit também
  **não menciona Evidências/Bibliografia** em nenhum .md (o destino proposto por (c) não está escrito
  no próprio kit); caminho §5.1 (`/Evidencias/Bibliograficas`, raiz) × disco real (aninhado na B1).
- **Opção (c) registrada** na decisão da camada (dono: OPERADOR): kit = ferramenta; produto →
  Evidências/Bibliografia; sem nova camada; sem contrato claim→biblioteca como condição;
  rastreabilidade quando houver uso. Concorre com (a) histórico/superado × (b) camada de origem V2.
  Compromissos incondicionais reconfirmados: D-03 (4 gap_pesquisa × 4 nao_estabelecida sobrevivem).
  Janela do mestre antes da Fase 4 (L-NT) segue aberta.
- **Governança:** decisoes **rev.29** · trilha 41 (script+JSON, 21/21 verdes) ·
  **ADENDO_1 à RESPOSTA_13 ao mestre** (via operador; carta da casa com os pontos verificados e
  crédito ao comentador) · STATUS. **0 ciência** (V7 `6e2c2979…` · manifesto `79d1309a…` ·
  P-8 `84fa918d…` conferidos por sha ao fim).

### 2026-09-17 — ABERTURA 24 + RESULTADO 24 (operador atualizou a ARQUITETURA V2; casa verificou: escopo limpo §2+§21; parecer FAVORÁVEL com 2 correções de formato; instalação pendente de decisão; 0 ciência)
- **Upload mesmo-nome sha `5be36836…`** × vigente `09692e18…`. Diff provado: 5 hunks +112/−76 **só em §2 e §21**;
  resto byte-idêntico.
- **Mudanças verificadas coerentes:** topo `[CIÊNCIA]` (catálogo sai do desenho; prosa §1/§3 OK) · Pasta de
  Atualização espelhada com convergência "VÍNCULOS UNIFICADOS" · Motor com consulta ativa + **ANAMNESE**
  (definição nova; prosa preexistia) · tríade MEC/CLÍN/TER→EXPLICAÇÃO NARRATIVA (só desenho; sem prosa).
- **Guarda da Pasta preservada e redistribuída** (§§18/19/20). **Não tocado: kit (0 ocorrências)** — decisão
  da camada (a/b/c) segue com o operador.
- **Dívida ampliada:** D-V2-DIAGRAMA-DUPLO → agora 4 representações (§2-novo × §21-novo × §20 × §5.3), com
  título duplicado e direção Evidência↔Biblioteca divergente entre prosa (a montante) e desenhos (a jusante)
  — sugerido 1 canônico + rebatismo. **Higiene:** fence do §21 indentado sem fechamento (render quebrado).
- **Governança:** decisoes **rev.30** · trilha 42 (9/9) · parecer ao operador com 3 opções de instalação · STATUS.
  Após instalar: SUPERSEDED_ no anterior + ponteiro + ARQUITETURA_VIGENTE.txt c/ nova sha + aviso ao mestre via operador.
  **0 ciência.**

**Continuação datada (rodada 24):** decisão do operador = **opção A**. V2.1 **INSTALADA** como vigente
(sha `1a50645e…`; upload exato `5be36836…`; anterior `09692e18…` → SUPERSEDED_ + ponteiro). Diff
upload→instalada = 4 linhas de formato (Rev. line + rótulo §2 + fence §21 ×2), CRLF preservado —
com confissão datada: 1ª candidata (fins-de-linha reescritos) descartada antes de instalar; sha morta
registrada. Pós-instalação verificada 14/14. Nota adicional à trilha 42: **5º desenho** (§30) →
D-V2-DIAGRAMA-DUPLO passa a 5 representações. **ADENDO_2 ao mestre** produzido; envio via operador.
Decisoes **rev.31** · **0 ciência.**

### 2026-09-17 — ABERTURA 25 + RESULTADO 25 (o ".py" do auditor-2 chegou: 172/102 ENCERRADO por réplica executável; schemas v1.3 = todas as adições da casa incorporadas; minuta verde; parecer do comentador 6/6; 0 ciência)
- **Pacote arquivado verbatim + executado aqui:** o script triagem roda limpo contra a V7 — sha da entrada
  idêntico, 274/172/102, regras 172/82/19/1, fila e automáticos idênticos por id E por motivo, RAISON pendente
  nos 2 vínculos, exit 0. A dívida aberta na trilha 38 ("172/102 não reversível") **fecha**: o número vinha de
  screening textual não publicado (confissão dele, §13). §8 do comentador: 6/6.
- **Schemas v1.3:** N2 adota byte a byte o bloco `condicao` da casa (jsonschema 10/10, furo provado na trilha 37
  fechado) + obrigação quando condicional; N1 fecha o paradoxo do alias (Adição A integral + confissão dele na
  description), adota o bloco pmid da trilha 39, restitui cross-over, limpa descriptions. Minuta: §3 reescrito,
  linha (ii) com falsificável, relatório §13, erratas §4B/âncoras registradas.
- **E2 resolvido e medido (486 avaliador, 0 FP; valores-ferramenta reprovam):** padrão dele adotado como proposta
  unificada da casa à rev.A3-E2 para o mestre (convergência independente). R2 aceito (derivador 146=48+71+16+11).
- **Adição da casa:** 58/172 transitórios não-'verificado' (marca dupla no portão de migração). **0 ciência.**

### 2026-09-17 — ABERTURA 26 + RESULTADO 26 (achado do mestre PROCEDENTE 5/5 — nó "UNIFICADOS" fundia os fluxos antes da Ontologia e inviabilizava a D-06 — parecer do comentador convergente 10/10; **V2.2 INSTALADA por decisão do operador (opção A)**; trilhas 45 18/18 e 45b 11/11; 0 ciência)
- **Entradas arquivadas verbatim:** achado do mestre sha `2841bc66…` (ele auditou o upload `5be36836…` = registro
  exato da casa; 1.388 linhas/50.964 bytes dele conferem) · parecer do comentador ao mestre sha `dfbd9ab7…`.
- **Réplica da casa (trilha 45, camadas declaradas):** §2 desenhava eixo-espelho da Pasta (EVIDÊNCIAS+NARRATIVAS
  próprias) convergindo para "EVIDÊNCIAS / VÍNCULOS UNIFICADOS" ANTES da ONTOLOGIA → D-06 inimplementável
  (a cláusula vive na minuta 2 do L-05, 0 ocorrências dentro da V2.1 — conferida e citada). Verbatim "O Motor
  busca ativamente" + "[ CONEXÃO / CONSULTA ]" ✔. Itens 1-2 do achado já saneados na instalação da rodada 24
  (Rev V2.1; rótulo '# 21.'); restavam H1 e a duplicata '# 2.' — corrigidos agora.
- **Convergência independente mestre × comentador:** proveniência no item recuperado
  (`origem_conhecimento = canonico | atualizacao`) — era 0 ocorrências na V2.1; a V2.2 a incorpora no desenho
  e na prosa, e declara "prosa prevalece sobre os desenhos".
- **V2.2 instalada:** vigente sha `df7f7cfd…`; V2.1 `1a50645e…` → SUPERSEDED_; **escopo cirúrgico: sufixo
  §3→fim BYTE-IDÊNTICO** (catálogo 146 IDs, §§5-30, §18/§19/§20 intactos); 30 seções únicas; CRLF preservado;
  tríade MEC/CLÍN/TER + EXPLICAÇÃO NARRATIVA + ANAMNESE preservadas. Item novo **D-V2-NO-UNIFICADO** criado por
  rec. 4 do mestre e RESOLVIDO nesta instalação; **D-V2-DIAGRAMA-DUPLO permanece** só para a direção Evidência↔Biblioteca.
- **Confissões da casa (datadas):** régua C1 apertada demais (Rev cita o nó removido — corrigida por camada) ·
  régua da 45b esperava 2 para 'canonico | atualizacao' (real = 3, inclui a Rev — corrigida). **Nota de método:**
  contagens em acervo acentuado passam a usar camada oficial python NFC (grep raso divergiu por forma Unicode).
- **Comentador:** 10/10 blocos verificados com crédito; §9 mantém L-05 v1.3 sem reengenharia (frente auditor-2 estável).
  **0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · P-8 `84fa918d…` · vínculos `490675e6…` ✔.

### 2026-09-17 — ABERTURA 27 + RESULTADO 27 (triagem v1.1 replicada INTEIRA E EXATA — 13/13, byte a byte · §14 do auditor-2 5/5 sob camadas declaradas · **derivador IDS-JSON APROVADO: 146 = 48+71+16+11 por categoria** · comentador 6/6 com crédito · 0 ciência)
- **v1.1 dele reproduzida byte a byte:** 274/231/43, regras 231/16/19/8, RAISON pelos motivos certos, exit 0;
  v1.0 lado a lado também reproduz 172/102; segunda via da casa: 0 divergências em 274 pares (valor, motivo).
- **§14 (a confissão grande dele) medido número a número:** 62 mandados = 66 da rodada 25 − 4 pendente+sinal ·
  60 com campo · 78 silenciosos (fronteira media nomeada: VINC_B1_0263) · 57 já extrapolado/preclinico · regra 4
  = 7 CONF + 1 NAO_LOCALIZADO com os 3 ex-sustenta exatos. Tese CONFERE: 2 campos já carregam extrapolação em 274/274.
- **D-L05-IDS-JSON:** o fonte é JSON inteiro → camada estrutural dá 146 por categoria idêntico ao bloco `contagem`;
  artefato + proveniência gravados; causa do 103 (e do 74) = camada de texto. Adoção formal pedida ao gate/mestre.
- **Marca dupla v1.1 (corpo):** 112/231 automáticos não-'verificado' (ressalva mais pesada na fila menor — §14.4 dele).
- **Comentador:** §§1-6 verificadas; D2/D3/D4 no colo do operador (endossos registrados); §3 do documento v1.0×v1.3
  CONFERE — eco da doença do H1 V2.1. **Confissões da casa:** 146-impreciso + 3 réguas do §14, todas datadas. **0 ciência.**

### 2026-09-18 — ABERTURA 28 + RESULTADO 28 (**P-8 SELADO: reconstrução byte a byte das regiões do mestre — oficial `be48a5ef…`, 1 sha viva nas duas casas** · comentário F-C2 agora dentro do portão · F-C2 dispara no contraexemplo · achado V2.1 fechado · régua NFC bilateral · Fase 4 VERDE · trilhas 47 7/7 + 47b · 0 ciência)
- As 3 regiões coladas eram byte-exatas: a única montagem que fecha o sha `be48a5ef…` usa TODOS os textos dele
  (665 = 658 + 6 comentário + 1 quebra V-08); diferença restante vs 84fa918d = só as 2 zonas declaradas. Backup na cadeia.
- Paridade comportamental: 2 ERRO / 299 AVISO / exit 1 idêntico; V-14 limpa; F-C2 dispara (e a base já disparava).
- Critério de troca corrigido pelo mestre e aceito (não era só o comentário); confissão da casa: detector do F-C2
  procurava no tail — corrigido, datado. Três frentes com a mesma frase sobre a D-06 (vive na minuta 2 do L-05).
- Fase 4 verde: próximo artefato esperado do mestre = Contrato das Unidades Narrativas; âncora §6 intacta (rodada 26).

### 2026-09-18 — ABERTURA 29 + RESULTADO 29 (**L-05: N1 v1.3 + N2 v1.4 do auditor-estrutura VERIFICADOS por réplica integral — trilha 48: 52/52** · parecer do comentador confirmado número a número · D4 resolvida nos DOIS lados (schema + portão) · D3 respondida em estrutura (efeito medido: exatos 20) · mapa de migração dele fechado por 2ª via independente, ZERO extras · dívida documental da minuta fechada · 0 ciência)
- Pacote arquivado verbatim: minuta v1.4 `78a0f2af…` · N1 `b06660fd…` (byte-idêntico ao da r.27 — N1 não mudou) ·
  N2 v1.4 `d96ad15b…` (novo). Diff v1.3→v1.4 medido: 3 linhas + bloco de 19 linhas (D3: redirecionado⇒minItems 2). Nada mais.
- 9+9 alegações do comentador replicadas 1 a 1: estrutura + **26 casos sintéticos falsificáveis (26/26)**, incluindo
  os 3 testes que a própria minuta declara no §15.2. check_schema draft-07 verde nos dois schemas.
- D4: `citacao_confirmada` deprecated no schema E banida como via no gate (depender dela = FALHA) — resolvida de fato;
  falta só o aceno do operador. D3: requisito×curadoria declarado em schema; os 20 redirecionados agora reprovam até
  ganhar a 2ª âncora — por desenho, não por acidente.
- 2ª via da casa contra os dados reais: 274×N2 falham SÓ em {trilha, ancoras, ancora_principal ausentes} + {uso=B1_v2 ×30};
  237×N1: 0 conformes, compostos 162/50 batendo com o mapa dele. Marca dupla reconferida: 112/231; fila 43 íntegra;
  triagem v1.1 reexecutada: 274/231/43, RAISON, exit 0.
- Confissões da casa datadas (4): régua do diff (índice), régua 0-ocorrências (o gate carrega o campo como detector
  de banimento — a régua certa é semântica), régua de topo (menções históricas legítimas), camada do "vazio" (é AUSENTE).
- Restam para o fechamento normativo do L-05 EXATAMENTE: **D2 (30 review — leitura, operador, com prazo)** +
  **adoção formal do _ids_oficiais.json (146) pelo gate/mestre**. **0 ciência:** V7 · manifesto · vínculos intactos ✔.

### 2026-09-18 — ABERTURA 30 + RESULTADO 30 (**L-NT MINUTA 1: réplica integral 49/49** · dimensionamento do mestre EXATO sob camadas declaradas · **casa descobre a camada completa de claims: 89 (não 81) — e o órfão real BLOCO01.001 com 6 vínculos** · régua de existência do NT-02 definida por achado da casa · armadilha RAISON com lastro medido · crédito 'a casa pediu' verificado no texto (com meta-errata) · 0 ciência)
- Parte 1 reproduzida número a número: 90/81 · 11 blocos · 1/7/30 · 244/274 · 80 · 1/2/15 · 628 frases
  (camada exata: split por ponto+espaço, corte ≥60 — receita de rodapé subespecificada ±3) · 21.503 palavras.
- A3b/A7: 4 cabeçalhos com ids agrupados e abreviação (`(BLOCO03.009, 012)` etc.) somam 8 ids que a regex
  do rodapé ignora → 89 canônicos; referenciados existentes = 79; **órfão real único: BLOCO01.001
  (VINC_B1_0001–0006)** → dívida candidata D-LNT-CLAIM-LEGADO; 10 canônicos sem vínculo para a Parte 5.
- Âncoras: V2.2/P-8 intactos; §6/§7/§13/§14 conferidos; minuta 2 L-05 com D-02..D-08 na fonte; P-8 oficial
  roda hoje: 2 ERRO (natureza_evidencia · trilha) / 299 AVISO / exit 1 — exatamente a Parte 8 da minuta.
- Kit: uso por claim 12/6/4 (22) conferido linha a linha; 'uso não existe no acervo' = verdade por-claim.
- Comentador 9/9 conferido; Parte 8 = sua §5 (uso × Claim Kit = decisão do operador, já pendente).
- Confissões datadas da casa: meta-errata (confissão falsa abortada a tempo) + 2 réguas (caixa; grupo capturante).

### 2026-09-18 — ABERTURA 31 + RESULTADO 31 (**rodada temática: PROPOSTA DO OPERADOR "Formalização do fluxo dos Claims Clínicos"** — Claim Kit → Evidências/Bibliografia → N1 → N2 → camadas · arquivada verbatim (`4ede1c81…`) e verificada ANTES da deliberação das frentes — trilha 50: **52/52** · 0 ciência)
- Pausa pedida pelo operador: produção retoma exatamente onde parou (piloto NT-B1 nas mãos do mestre · portão L-05 na mesa do estrutura).
- A proposta FECHA uma pendência nomeada desde a rodada 23 ("decisão da camada do kit", dona: operador) na direção (c) —
  autoria do comentador, crédito registrado; e é o PRIMEIRO registro formal da decisão-mãe ("claim não entra na Biblioteca
  Canônica"), que não constava verbatim em lugar nenhum (medido). Guarda-gêmea já vive na V2.2: Evidências "não constituem
  uma segunda Biblioteca Canônica".
- Números replicados 1 a 1: 35 claims (Lista) · 22 aprovados (8+14 ressalva) · uso 12/6/4 · 4 lacunas = {.003,.006,.012,.012c}
  · PMIDs 49 = 10 na biblioteca + 39 fora · kit sem âncora (fortuna-zero medida) · evidence_role 22/22 human_clinical.
- Schemas prontos sem mudar uma linha: N1/N2 intactos; claim_id já admite o namespace do kit (sintético passa); ids genéricos;
  uso superset; sintéticos trilha×uso 3/3. Única nota de precisão: §2.3 atribui "entidades" ao N2 — campo inexiste lá; vive no NT.
- Mapa de fortuna do materializador entregue medido às frentes (direto/derivável/mapeável/zero + taxonomia = os 2 ERRO do P-8).
- Casa recomenda **B — concordância com ajustes**; decisão formal: mestre + estrutura + homologação do operador.
  Cartas: RESPOSTA_17 (mestre) + RESPOSTA_9 (estrutura) com os MESMOS bytes anexados. Confissões datadas: 6 (réguas).

### 2026-09-18 — ABERTURA 32 + RESULTADO 32 (**consolidado B ancorado na Arquitetura V2.2 por instrução do operador — trilha 51: 28/28** · 5 dos 6 pontos verbatim/quase à letra · 1 precisão da casa (o kit NÃO está escrito na arquitetura) · questão v1.7×v1.9 medida (v1.9 não existe no acervo; correção G3 multi-IA é aditiva e cobre lacuna real) · 0 ciência)
- Consolidado `ff8daf6f…` arquivado com digitais; remetente sem assinatura (presumido comentador; confirmação pedida).
- Âncoras exatas registradas: §5 L243 · §5.1 L292 (referência única vez = base normativa do dedupe 10/39) · L369 vínculos transversais
  · §1 L31 + mapa camadas + §6 NT · §22 L1214 (nenhuma camada aumenta a certeza) — citação futura garantida à letra.
- Precisão de redação entregue: "compatível por via dos contratos L-05", nunca "a arquitetura confirma que o kit pode…".
- Pedidos da casa: pareceres originais das frentes · bytes do COMO EXECUTAR corrente (v1.8/v1.9?) · remetente · homologação.
- Confissões datadas: 4 (réguas). Produção inalterada: piloto NT-B1 (mestre) · portão L-05 (estrutura) · rev.A3-E2 (casa).

### 2026-09-18 — ABERTURA 33 + RESULTADO 33 (**DIVERGÊNCIA DUPLA‑V2.2 identificada por bytes e seções — trilha 52: 22/22** · o 'V2.2' do projeto do mestre (`309aa65f…`, sem as 3 guardas) é, em conteúdo, o UPLOAD da rodada 24 rotulado — assinatura 28‑seções/§§2‑21 exata · vigente correta = `df7f7cfd…` (as marcas que o mestre sente falta vieram do ACHADO dele, instalado na casa) · L‑NT não muda: já cita o sha certo · 0 ciência)
- Medição por elo: 3 marcas (origem_conhecimento · prosa prevalece · fora do cânone) SÓ na `df7f7cfd…` (L4·L117·L121·L172·L175).
- Assinatura fechada: upload r24 (`5be36836…`) × V2.1 = EXATAMENTE o relato do mestre (28 idênticas · §§2 e §21 · §§6/7/13/14 byte a byte).
- Respostas (a)–(d) medidas e publicadas no RELATORIO da casa; correção de rota INVERTIDA: troca‑se o arquivo no projeto dele
  (52.181 b · CRLF · `df7f7cfdfc01…`), NÃO a citação do cabeçalho da minuta.
- Nova dívida: D‑V22‑BYTES‑PROJETO. Pedidos: bytes da vigente → mestre · bytes do `309aa65f…` → casa (diff final).
- Produção segue intacta (piloto NT‑B1 · portão L‑05 · rev.A3‑E2 da casa).

### 2026-09-19 — ABERTURA 34 + RESULTADO 34 (**rodada temática: AUDITORIA INDEPENDENTE da 2ª rodada da IA externa sobre o Motor — trilha 53: 74/74** · base nova arquivada verbatim (Filosofia `dedbff6c…` · Roteiro `5e3f9163…` · parecer `40a58381…`) · ACHADO RAIZ: a IA auditou a linha SUPERSEDED, não a vigente `df7f7cfd…` · 0 ciência)
- Achado documental medido (checks 0.6–0.13): C-10 impossível contra H1/Rev "V2.2"; 0 menção às 3 marcas exclusivas da vigente; citação E6 "literal" = 0× em TODAS as versões (casefold) — **regra nova da casa: citação dessa frente não vale como literal até verificação**.
- Vereditos G1–G20: 15 pendências reais confirmadas · G2/G5 indetermináveis nesta base (correto) · G3/G6/G15 reduções validadas · G20 reformulado (dupla contagem sob G19) · agravante do G1 invalidado · ordem da IA ajustada para **G19 → G16 → G1**.
- Vereditos C1–C10: C-3/C-4 contraditórios reais (exigem G19) · C-5 real de cobertura · C-6 real taxonomia (→G18) · C-7 rebaixada (glossário 1 linha) · C-8 real de registro (correção menor) · **C-1/C-9 falsas contradições** · **C-2 já era: resolvida na vigente (rodada 26; = o ACHADO do mestre residual = desenhos §21/§30)** · **C-10 falso (artefato de base)**.
- E/P: 16/16 confirmações de E validadas (E6 re-ancorado · E8 precisão de escopo) · módulos M/T = 0× na base (proposta dela, bem marcada) · autocorreções validadas.
- Ordem recomendada entregue SEM soluções (regra do operador): saneamento → G19 → G16 → G1 → C-3/C-4 → G18/G7 → G8 → G4/G5/G6/G10 → G15/G17 → registros.
- Pedidos novos: remetente da frente · bytes da 1ª rodada · vigente `df7f7cfd…` à frente externa (D-V22-BYTES-PROJETO) · homologações antigas mantidas. Confissões datadas: 6 (réguas, trilha 53).

### 2026-09-19 — ABERTURA 35 + RESULTADO 35 (**COBRANÇA FORMAL DO OPERADOR sobre a "V2.2 vigente" — trilha 54: 15/15** · origem/cadeia/entrega medidas · SUSPENSÃO acatada · regra nova de versionamento adotada verbatim · 0 ciência)
- Verdade medida, sem defesa: `df7f7cfd…` nasceu na casa (rodada 26) sobre o upload do operador + achado do mestre + parecer; a
  aprovação registrada foi de DIREÇÃO ("opção A"). **Entrega do documento completo para aprovação: NÃO CONSTA** — 0 cópias
  fora da pasta interna; 0 artefatos de entrega; 0 aprovação-com-sha.
- `df7f7cfd…` reclassificado CANDIDATA pendente · ponteiro com nota de suspensão datada · orientação ao mestre (rodada 33)
  suspensa · base recebida provisória = upload r24 `5be36836…` · âncoras §2-novo das rodadas 31–34 re-carimbadas "medidas
  na candidata" (C-2, E6, mitigação C-3, G1) — sufixo §3→fim segue válido em qualquer elo.
- REGRA NOVA (verbatim, rev.42): PROPOSTA → ALTERAÇÃO → DOCUMENTO COMPLETO ENTREGUE → APROVAÇÃO → SHA/DATA → VIGENTE.
- SUBMISSÃO formal ao operador: documento completo + sha + diff (+42/−18, 3 blocos) + cadeia de evidências → decisão
  (a) aprovar / (b) devolver / (c) rejeitar. Nada instalado antes da decisão.
- Confissões: 1 processual gravada (da casa) + régua idiomática do check 1.1 saneada na própria trilha.

### 2026-09-19 — ABERTURA 36 + RESULTADO 36 (**DECISÃO DO OPERADOR: letra A — V2.2 APROVADA como arquitetura oficial** · regra nova cumprida ponta a ponta: submissão (r35) → aprovação → sha/data → vigente (r36) · decisoes rev.43 · ponteiro com nota de aprovação · 0 ciência)
- sha oficial: `df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1` · 52.181 b · CRLF · 30 seções · H1/Rev V2.2.
- Efeitos: âncoras do §2 novo voltam a valer como norma (rodadas 31–34 re-carimbadas→normativas) · repasse autorizado às
  frentes com os mesmos bytes (mestre primeiro — D-V22-BYTES-PROJETO pronta para fechar; base da IA externa saneada) ·
  echo de conferência (mestre re-confirma sha) fica para a próxima rodada. Regra nova permanece vigente para todo
  documento normativo futuro (rev.42).
- Distribuição (rodada 36): cópia de entrega em `ENTREGAS/2026-09-19_V2.2_OFICIAL/` — `.md` verbatim (sha idêntico
  `df7f7cfd…`, verificado) + `ARQUITETURA_V2.2_OFICIAL_2026-09-19.zip` (11.562 b; conteúdo re-extraído confere o sha).
- Entrega (rodada 36): `ENTREGAS/2026-09-19_SCHEMAS_L05/` — `schema_vinculo_v1.1.json` verbatim (sha `b0934412…`,
  idêntico ao arquivado de 15/09) + zip. **Dívida documental menor registrada (D-V22-SCHEMA-NOMES):** a V2.2 aprovada cita
  "schema_referencia_v1.1.json"/"schema_vinculo_v1.1.json" (§5.1/§5.2), mas os schemas APROVADOS no acervo são N1 v1.3
  (`b06660fd…`) e N2 v1.4 (`d96ad15b…`) — correção de glossário candidata a próxima revisão editorial da arquitetura.

## ABERTURA 37 — 2026-09-19
- Pergunta do operador: "o schema_vinculo_v1.1.json não é o atualizado?" (ele baixou o v1.1 na rodada 36 e notou a dúvida).
- Ação: réplica empírica da cadeia completa N1+N2 ANTES de responder (trilha 55) + verificação do status de governança sob a regra nova (rev.42) + montagem do pacote com os VIGENTES.

## RESULTADO 37 — 2026-09-19
- Trilha 55: **30/30 VERDE** (reexecução limpa após 3 correções de régua confessadas: C55-1 classificação×contagem · C55-2 slice · C55-3 caminhos).
- **Resposta: NÃO — o v1.1 é o 1º elo (histórico, 15/09). VIGENTES: N2 v1.4 `d96ad15b…` (18/09) · N1 v1.3 `b06660fd…` (17/09).** A versão real vive no `$id` interno do JSON — os nomes de upload (`v1`/`(1)`/`(2)`) são do navegador.
- Medido no oficial: a V2.2 aprovada (`df7f7cfd…`) cita os nomes **v1.1** em §5.1/§5.2 (0× v1.3/v1.4) → D-V22-SCHEMA-NOMES confirmada no documento oficial; o próprio vigente N2 ainda diz "PROPOSTA v1.4 — não normativo" na description.
- **Precisão de governança (franqueza, regra nova):** consta aceite técnico do ciclo (r29, comentador + casa, trilha 48 52/52, 26/26 casos) — **NÃO consta aprovação formal do operador com sha/data** (as 2 linhas casadas no log são PENDÊNCIAS de homologação da D4). Falta o selo final, exatamente como na V2.2 da rodada 35. Sugerido: ato formal simples do operador; na mesma emenda editorial futura, corrigir os nomes na V2.2 §5.1/§5.2.
- Entrega: `ENTREGAS/2026-09-19_SCHEMAS_L05_VIGENTES/` (N2 v1.4 + N1 v1.3 + minuta v1.4 + LEIAME + zip 25.840 b, re-extração confere). Pacote r36 (v1.1) fica como histórico.
- decisoes_B1.md → **rev.44** · STATUS_SIMPLES → bloco Rodada 37 · **0 ciência tocada** (V7/manifesto/vínculos reconferidos início e fim).

## ABERTURA 38 — 2026-09-19
- Operador montando o Motor Clínico com uma IA externa pergunta: "o 1.4 ainda não está aprovado?"

## RESULTADO 38 — 2026-09-19
- Resposta (ancorada na trilha 55, 30/30): **tecnicamente validado (ciclo, r29) · formalmente NÃO aprovado pelo operador** (regra nova, rev.42). Selo final = 1 palavra do operador.
- Alerta emitido: V2.2 oficial cita nomes v1.1 → risco de a IA externa ancorar o schema errado; orientação: N2 v1.4 `d96ad15b…` + N1 v1.3 `b06660fd…`, conferência por sha256.
- decisoes_B1.md → **rev.45** · STATUS_SIMPLES → bloco Rodada 38 · **0 ciência**.

## ABERTURA 39 — 2026-09-19
- Operador cola o parecer do auditor-2 sobre "schema_vinculo_v1.1" (nunca existiu · vigente v1.4 · ponteiro errado na V2 · sugestões).

## RESULTADO 39 — 2026-09-19
- Verbatim arquivado (`82a8b5b4…`) + digitais · **TRILHA 56: 26/26 verdes** — réplica afirmação por afirmação.
- **Veredito: substantivamente correto e convergente** (shas exatos · ponteiro defasado real = D-V22-SCHEMA-NOMES redescoberta · 20 redirecionados exato · catálogo não adotado · "não normativo" = nossa posição r38). **3 precisões:** P1 o aceite r29 foi do comentador (casa subscreveu) · **P2 "direção/condição nasceram na v1.4" é FALSO — existem desde a v1.1; prosa §5.2 é de 15/09 e compatível com a v1.1; o defeito é só o nome do ponteiro** · P3 o "parecer de ontem" com CLAIM_KIT_CLINICO não chegou à casa → pedir bytes.
- **Confissão da casa — dívida nova D-L05-NOME-X-ID:** a carta 3 registrou nome≠$id sem nomear defeito; o nome v1.1 só existe como marca de arquivamento nossa (+ na V2.2 oficial) — origem exata da busca impossível do operador.
- Sugestões dele: sha-invariantes (medido) mas exigem decisão do operador (V2.2 oficial = regra nova). Casa oferece preparar a emenda editorial.
- decisoes_B1.md → **rev.46** · STATUS_SIMPLES → bloco Rodada 39 · **0 ciência** (re-checar início/fim na trilha).

## ABERTURA 40 — 2026-09-19
- Operador: "ok pode fazer" → casa prepara a EMENDA EDITORIAL 01 da V2.2 (ponteiros §5.1/§5.2) pela regra nova.

## RESULTADO 40 — 2026-09-19
- **TRILHA 57: 11/11 verdes.** CANDIDATA sha `3cbc131d…` (52.476 b): exatas 3 linhas substituídas (269 · 306 · Rev) · 0 normativo alterado · CRLF/30 seções/âncoras intactos · vigente continua `df7f7cfd…` até aprovação.
- Pacote de submissão entregue (`ENTREGAS/2026-09-19_EMENDA_V22_E01_CANDIDATA/` + zip). Confissão C57-1 (régua global×por-linha).
- **Linha de fecho proposta ao operador (1 frase resolve a emenda E o selo dos schemas):** "APROVADO: emenda editorial 01 da V2.2 E os schemas N1 v1.3 / N2 v1.4".
- decisoes_B1.md → **rev.47** · STATUS_SIMPLES → bloco Rodada 40 · **0 ciência**.

## ABERTURA 41 — 2026-09-19
- Decisão do operador: número de versão no cabeçalho (não só data) + cartas às 3 frentes + regra permanente: toda mudança documental → download.

## RESULTADO 41 — 2026-09-19
- **TRILHA 58: 12/12 verdes.** CANDIDATA V2.3 sha `498e7df9…` (52.740 b): 4 linhas substituídas (H1 · Rev · §5.1 · §5.2), histórico da Rev V2.2 preservado inteiro, resto byte-idêntico. Vigente oficial NÃO movido (`df7f7cfd…`) até aprovação.
- 3 cartas geradas (mestre · auditor-estrutura · comentador), direcionadas com especificidades por frente. Regra **R-DOWNLOAD-SEMPRE** registrada verbatim (rev.48) e já aplicada: pacote `ENTREGAS/2026-09-19_V2.3_CANDIDATA_E_CARTAS/` + zip.
- Confissão C58-1 (ordem do replace global × cláusula histórico) — pega pela régua C5, corrigida, guarda permanente C3b.
- Na mesa do operador: "APROVADO: V2.3 (498e7df9…) E os schemas N1 v1.3 / N2 v1.4" → vigência + selo + repasses.
- decisoes_B1.md → **rev.48** · STATUS_SIMPLES → bloco Rodada 41 · **0 ciência**.

## ABERTURA 42 — 2026-09-19
- Operador pede zip dos schemas para as frentes; dúvida antiviés: quem deve receber (auditor-2? comentador? mestre?).

## RESULTADO 42 — 2026-09-19
- Posição da casa registrada (rev.49): artefato comum ≠ contaminação; LEIAME neutro torna o pacote universal; minimalismo: auditor-2 dispensável · comentador OK · mestre recomenda-se adiar (decisão final do operador — mesmo zip serve).
- **TRILHA 59: 3/3** — pacote `ENTREGAS/2026-09-19_SCHEMAS_L05_CORRENTES_DISTRIBUICAO/` (N1 v1.3 + N2 v1.4 + especificação + LEIAME neutro + zip) com LEIAME verificado 0-menções-a-frentes.
- STATUS_SIMPLES → bloco Rodada 42 · **0 ciência**.

## ABERTURA 43 — 2026-09-19
- Operador traz a resposta do auditor-2 à carta 9 + V2.3 e pergunta: qual zip serve para ele (o das versões explicadas? o neutro? ou um novo?).

## RESULTADO 43 — 2026-09-19
- Resposta: nenhum dos anteriores servia (só correntes/só antigo) → **PACOTE DE LINHAGEM criado** (trilha 60: 6/6): 7 schemas + 5 especificações + manifesto de 12 digitais; distribuição passa a usar nome==`$id` (sugestão dele, aplicada).
- Pontos dele replicados: eco V2.3 exato ✔ (não substitui aprovação do operador) · causa raiz unificada das 2 dívidas subscrita ✔ · CLAIM_KIT_CLINICO: premissa verificada ✔ (subordinada, "morre junto se não homologar" — correto) · ponto único de falha respondido com espelho + manifesto.
- **Alerta novo: existe um "Como Executar v1.9" fora da casa** (acervo só tem v1.7) — pedido formal dos bytes (v1.8? v1.9 + os 2 reenviados dele).
- decisoes_B1.md → **rev.50** · STATUS_SIMPLES → bloco Rodada 43 · **0 ciência**.

## ABERTURA 44 — 2026-09-19
- Operador explica o estado do projeto (pausas até o motor), resolve o mistério do "v1.1" (= IA externa do motor lendo a V2.2), esclarece o "v1.9" (discussão, não documento) e anexa o Roteiro de Trabalho.

## RESULTADO 44 — 2026-09-19
- Roteiro medido: **byte-idêntico ao da base r34** (`5e3f9163…`) — eco registrado.
- **Mistério do pedido "v1.1" FECHADO:** foi a IA externa do motor (leu a V2.2 com ponteiro defasado). Pacote dedicado montado para ela (`ENTREGAS/2026-09-19_PARA_IA_EXTERNA_MOTOR/`, trilha 61: 3/3 — V2.3 + schemas + LEIAME neutro-antiviés).
- Mapa de pausas registrado (mestre · estrutura · claims — todos aguardando o motor).
- decisoes_B1.md → **rev.51** · STATUS_SIMPLES → bloco Rodada 44 · **0 ciência**.

## ABERTURA 45 — 2026-09-19
- Mestre responde à carta 18 + V2.3 (eco de sha · correções próprias · CONFLITO: arquivo do projeto não é a V2.2 oficial · pede os schemas · nomeia o DELIBERACAO do fluxo claim).

## RESULTADO 45 — 2026-09-19
- **TRILHA 62: 7/7** — tudo que era verificável dele conferiu (eco V2.3 · âncoras L-NT idênticas · N-4/herança · residuais históricos na Rev).
- **Conflito provado bilateralmente:** o projeto do mestre não contém a V2.2 oficial (nem o endurecimento de proveniência). **Confissão da casa:** "upload r24 rotulado" estava impreciso — o marcador "O Motor busca ativamente" (1× no r24 × 0 no projeto) prova que os bytes diferem; identidade exata só com os bytes do arquivo do projeto (pedido ao operador).
- Ações recomendadas: repassar V2.2 oficial ao projeto AGORA (fecha a dívida) · enviar ao mestre o zip neutro de schemas (posição revista: ele pediu com causa nominal) · pedir `DELIBERACAO_FLUXO_CLAIM_CLINICO_2026-09-18.md` verbatim.
- decisoes_B1.md → **rev.52** · STATUS_SIMPLES → bloco Rodada 45 · **0 ciência**.

## ABERTURA 46 — 2026-09-20
- Operador pede a carta ao auditor-mestre: pedir os bytes da `DELIBERACAO_FLUXO_CLAIM_CLINICO_2026-09-18.md` e anunciar que ele envia junto os schemas L-05 e a V2.2 oficial.

## RESULTADO 46 — 2026-09-20
- **TRILHA 63: 10/10 verdes.** CARTA 19 medida (`c2f799d6…`, 5.638 b): 5 blocos — acuse r45 (7/7 + confissão `309aa65f`) · anúncio de envio (zip V2.2 oficial `1444ae44…` → substitui base do projeto e fecha D-V22-BYTES-PROJETO com eco; zip schemas `72f8f2e5…` N1 v1.3/N2 v1.4 com nota franca: selo formal pendente) · **PEDIDO CENTRAL: bytes verbatim da deliberação (base da casa = 0 ocorrências — varredura gravada)** · pedido secundário do export `309aa65f…` · fila.
- Guarda anticípada (C08): carta sem eco de aprovação ("APROVADO: V2.3" = 0×) — a frase de selo continua exclusivamente na mesa do operador.
- Zips de envio (2026-09-19) re-extraídos e conferidos — inalterados. Confissão C63-1 (tupla no dict ciência) datada.
- decisoes_B1.md → **rev.53** · STATUS_SIMPLES → bloco Rodada 46 · pacote `ENTREGAS/2026-09-20_CARTA19_MESTRE/` (R-DOWNLOAD-SEMPRE) · **0 ciência**.

## ABERTURA 47 — 2026-09-20
- Correção do operador: o mestre JÁ tinha disponibilizado a deliberação do fluxo do claim clínico — o arquivo segue anexado; carta 19 precisa ser reformulada.

## RESULTADO 47 — 2026-09-20
- **TRILHA 64: 14/14 verdes.** Deliberação recebida, arquivada (`fe5a18b3…`, 8.141 b) e **replicadinha antes de comentar**: TUDO mensurável conferiu EXATO — veredito B (1+3) · shas dos 2 arquivos-base ≡ acervo · 41/22/21 (régua de conjunto; .012b/.012c) · 8+14 · 12/12 campos · 49×237→39 ausentes · wiring zero 2 faces · quotes §6 exatas · NT-02/N-4/uso herdado · proposta: 35/item13/sem-Biblioteca/L215. 2 precisões de citação (§5.5 L421 · proposta L215) — essência certa, literal registrado.
- **Confissão C64-1:** régua de conjunto após falha de aritmética cega (mesma lição da C55-1) — datada.
- **CARTA 19 REFEITA (v2, `74e1e1cb…`):** deixa de pedir os bytes (já verificados) e vira acuse + envio V2.2/schemas + único pedido aberto (export `309aa65f…`). v1 arquivada SUPERSEDED. Pacote ENTREGAS re-feito (R-DOWNLOAD-SEMPRE); guarda: 0 eco antecipado de aprovação.
- Posição da casa registrada: saída (i) subscrita; homologação B + 4 fechos + frase "APROVADO: V2.3 (498e7df9…) E os schemas N1 v1.3 / N2 v1.4" seguem na mesa do operador. Antiviés: deliberação não circula a frentes.
- decisoes_B1.md → **rev.54** · STATUS_SIMPLES → bloco Rodada 47 · **0 ciência**.

## ABERTURA 48 — 2026-09-20
- Pergunta de governo do operador: a aprovação da V2.3 e dos schemas não deveria ser dos auditores ou da bancada, com base em ciência/engenharia, já que as IAs constroem o projeto?

## RESULTADO 48 — 2026-09-20
- Resposta da casa (rev.55): NÃO — separação dos dois "aprovar": conformidade técnica (já cumprida pelas IAs/bancada: medição e ecos) × vigência normativa (ato de governo, só do operador — desenho intencional da ponte). Motivos: produção×auditoria×decisão; histórico de erros reais de todas as frentes capturados justamente pela ponte; "quem audita o auditor"; nenhuma IA responde pelo projeto. Analogia: reviewers/CI × maintainer com chave.
- Oferecido: dossiê go/no-go de 1 tela por submissão; delegação futura só por contrato normatizado pelo operador.
- Sem mudança documental normativa (rodada conceitual) · decisoes_B1.md → **rev.55** · STATUS_SIMPLES → bloco Rodada 48 · **0 ciência** (trio reconferido).

## ABERTURA 49 — 2026-09-20
- Operador esclarece seu modelo: IAs respondem com rastreabilidade se funciona conforme a filosofia (engenharia/ciência); quando todas fecham um assunto/documento, ele aprova; no fim da plataforma, auditoria por especialistas humanos.

## RESULTADO 49 — 2026-09-20
- Casa subscreve como contrato de regime (rev.56): é a separação rev.55 bem formulada — vereditos técnicos das frentes (cada qual na alçada) → assinatura do operador sobre dossiê convergente → especialistas no fim sobre acervo periciável.
- Precisões registradas: rastreabilidade ≠ "funciona" (valoração funcional por teste: casos/portões/pilotos); "fechado" precisa ser por checklist; nenhuma frente cobre o todo — o global é soma das peças.
- Estado medido do critério "todas fecharam": V2.3 = 3/3 → pronta para a frase; schemas = 3 frentes já se manifestaram, falta o eco do mestre sobre os bytes em trânsito agora (o envio atual fecha o elo).
- Oferecido: dossiê go/no-go 1 tela por submissão + DOSSIÊ PERÍCIA EXTERNA no fim da plataforma.
- decisoes_B1.md → **rev.56** · STATUS_SIMPLES → bloco Rodada 49 · **0 ciência** (trio reconferido).

## ABERTURA 50 — 2026-09-20
- Operador traz a resposta do mestre (V2.2 instalada no projeto + ecos) com o export do fóssil 309aa65f anexo; pergunta por que o mestre manteve a V2.2 como oficial e se ficarão as duas (V2.2 e V2.3); os 2 JSONs ainda não foram, mas ele os enviará. Traz também a análise do comentador (status normativo × correção técnica da V2.3 + o "documento gerado").

## RESULTADO 50 — 2026-09-20
- **TRILHA 65: 14/14 verdes.** Ecos do mestre EXATOS (V2.2 · V2.3 · spec `78a0f2af…`); **D-V22-BYTES-PROJETO fechada bilateralmente**. Precisão dele verdadeira e adotada: shas individuais passam a constar nas cartas. FÓSSIL cravado: **4º artefato "V2 15.09.26" (51.235 b), desconhecido até da casa** — confissão da rev.52 encerrada ("upload r24 rotulado" aposentado). As 3 correções dele ao L-NT **PROCEDEM** na especificação v1.4 (uso 2 trilhas + Opção A · natureza_evidencia 7 valores exatos · direcao_suporte 14× com resíduo histórico no changelog) — réplica bônus: uso do acervo = {178·37·29·30} ⇒ 244/274 EXATO; evid_role = {133·66·30·6·2} EXATO.
- **"Como Executar v1.9" (sha 1cd90b40…): 0 bytes na casa** — pedido formal dos bytes (2 frentes citam o artefato).
- Comentador: método correto (status ≠ técnica), subscrito; 2 premissas imprecisas (anexo ≠ V2.2 · ponteiros v1.1 existem até na oficial). Resposta ao operador: o mestre age certo — 1 vigente + 1 candidata + 1 fóssil aposentado; ao seu "APROVADO", ele substitui.
- **Critério do operador medido:** V2.3 = 3/3 técnicos → frase pronta; schemas = falta o eco do mestre sobre os JSONs em trânsito.
- decisoes_B1.md → **rev.57** · STATUS_SIMPLES → bloco Rodada 50 · **0 ciência**.

## ABERTURA 51 — 2026-09-20
- Operador envia o "COMO EXECUTAR v1.9" (em fase de aprovação, frente própria de claims — para arquivo e atualização contínua) e avisa: não achou o pacote SCHEMAS_L05_CORRENTES no workspace para enviar ao mestre.

## RESULTADO 51 — 2026-09-20
- **TRILHA 66: 7/7 verdes.** v1.9 = sha `1cd90b40…` — **ECO BILATERAL fechado com o mestre** (de "declarado" a VERIFICADO); arquivado com status EM ATUALIZAÇÃO/não-normativo e a regra registrada: novas versões fluem com sha. Elo v1.8 = 0 na base (dívida de linhagem nomeada). Nota de interface: "claims SM-xx são CLÍNICOS e alimentam evidencias/bibliografia, não a biblioteca mecanística" — convergente com a saída (i).
- **Pacote remontado:** `ENTREGAS/2026-09-20_ENVIO_MESTRE_SCHEMAS/` — 5/5 itens byte-idênticos à distribuição de 19/09 (zip `72f8f2e5…`) + DIGITAIS com shas individuais. Apresentado ao operador para download direto.
- decisoes_B1.md → **rev.58** · STATUS_SIMPLES → bloco Rodada 51 · **0 ciência**.

## ABERTURA 52 — 2026-09-20
- Operador traz a resposta do auditor-2 ao pacote L-05 LINHAGEM COMPLETA (12 digitais conferem · genealogia confirmada no artefato · pedido: espelhar no Projeto dele · aviso: o ambiente dele não persiste entre sessões; e o Projeto dele está com arquitetura de 15/09).

## RESULTADO 52 — 2026-09-20
- **TRILHA 67: 8/8 verdes.** Ecos VERIFICADOS: manifesto 12/12 reexecutado (confissão C67-1 do parse, corrigida e datada) · tabela de genealogia EXATA nos 4 N2 (chaves JSON: direcao+condicao nascem na v1.1; v1.2 só renomeia) — correção (b) confirmada dos dois lados sobre os mesmos bytes · correntes ≡.
- **Causa-raiz aposentada pelo autor:** nome == `$id` vira regra de PRODUÇÃO dele, não só de distribuição. D-L05-NOME-X-ID: distribuição resolvida; nomes internos/rótulo aguardam só o selo do operador.
- **DESCOBERTA:** 2ª base de projeto com documento superseded (a "de 15/09" no Projeto do auditor-2) → pacote-espelho `ENTREGAS/2026-09-20_ENVIO_AUDITOR2_PROJETO/` (V2.2 VIGENTE — candidata não sobe antes da frase — + schemas correntes + especificação + manifesto; shas individuais). Pedido novo: eco do sha do arquivo antigo antes da troca (casa crava o elo).
- decisoes_B1.md → **rev.59** · STATUS_SIMPLES → bloco Rodada 52 · **0 ciência**.

## ABERTURA 53 — 2026-09-21
- Operador traz a verificação técnica do mestre sobre a V2.3 candidata (`VERIFICACAO_TECNICA_V23_CANDIDATA_2026-09-21 (1).md`) **E A FRASE DE APROVAÇÃO** (verbatim): "a oficial agora é a Arquitetura Consolidada da Plataforma V2.3 assim como os schemas vínculo 1.4 e referencia 1.3" — com pedido conjugado: refazer resposta e zip do pacote-espelho do auditor-2, pois a oficial deixou de ser a V2.2.
- Regra nova de rótulos do operador (verbatim, registrada nesta rodada): nada de "Candidata"/"Proposta" em nome/título que a casa EMITE — "somente a mudança da versão"; se as IAs acharem defeito, argumentam e a gente corrige até de fato estar aprovado.

## RESULTADO 53 — 2026-09-21
- **TRILHA 68: 13/13 verdes** (1 confissão: C68-1 — régua do manifesto assumia coluna de estado de 1 token; o manifesto pós-selo introduziu "APROVADO vige" de 2 tokens; 1ª corrida leu 10/12 com 0 divergências — era cobertura do parser, não dado; régua corrigida com sha ancorado no fim da linha, datada no script).
- **Réplica integral da verificação do mestre — TUDO CONFERE nos bytes:** A.1 shas+bytes exatos dos 2 schemas + draft-07 `check_schema` OK (mesma biblioteca) · A.2 `$id` == ponteiros §5.1/§5.2 da V2.3 caractere a caractere · A.4 **0 `$ref`** (sem acoplamento de versão) · A.6 rótulos internos "PROPOSTA — não normativo" confirmados nos bytes como resíduo pré-selo · O-2 verdadeira (`uso` em `required` do N2, ausente do §5.2 → próxima revisão) · precisão NOVA dele confirmada: `direcao_suporte` existe APENAS sob `ancoras[]` (degrau 5 da L-06 deve ler `ancoras[].direcao_suporte`) · O-3 confirmada e promovida a dívida nomeada **D-JSONM-ORIGEM-CONHECIMENTO** (`origem_conhecimento` 0× nos 4 artefatos L-05 × 3× na V2.3 — schema dos JSONs Modulares terá de carregar o campo).
- **APROVAÇÃO EXECUTADA (o marco do projeto):** ponteiro `ARQUITETURA_VIGENTE.txt` reescrito — cabeça "APROVACAO FORMAL — 2026-09-21" com a frase verbatim + sha da V2.3 + selo dos schemas N1 v1.3/N2 v1.4 (histórico integral preservado) · **V2.3 promovida à série raiz** (`498e7df9…`, 52.740 b, sha conferido) · V2.2 permanece na série SEM rename (17 scripts a citam — vigência vive no ponteiro) · **D-V22-SCHEMA-NOMES FECHADA** (a correção vivia na V2.3) · selo dos schemas encerra a pendência aberta desde a rodada 38.
- **Pacote-espelho REFEITO sob a regra nova de rótulos:** `ENTREGAS/2026-09-21_ENVIO_AUDITOR2_PROJETO_V23/` — 5 artefatos com nomes limpos (0 CANDIDATA/PROPOSTA/CORRENTE; nome do schema == `$id`) ≡ fontes oficiais + DIGITAIS com shas individuais + MANIFESTO_LINHAGEM_2026-09-21 (espelho pós-selo, 12 digitais, substitui o de 19/09) + zip `948dbb35ed635a0236a593d91061c805384963fbaaa611fdd83a565087f4487d` (re-extração ≡) · pasta de 20/09 marcada **SUPERSEDED** antes de circular.
- decisoes_B1.md → **rev.60** · STATUS_SIMPLES → bloco Rodada 53 · **0 ciência** (trio reconferido início/fim: V7 `6e2c2979…` · manifesto bib `79d1309a…` · vínculos `490675e6…`).

## ABERTURA 54 — 2026-09-21
- Operador pede: (1) resposta direta sobre o que enviar a cada frente ("é para mandar só o zip?"); (2) **retomar o canal de cartas ao auditor-mestre** (a casa havia substituído por nota de 3 linhas — correção aceita: a carta é o canal); (3) **links dos arquivos** na tela (workspace cheio); (4) linguagem mais simples nas respostas.

## RESULTADO 54 — 2026-09-21
- **CARTA 20 AO AUDITOR-MESTRE escrita e selada:** `ENTREGAS/2026-09-21_CARTA20_MESTRE/` — md `1de3e72d903b27b38715dffa036546efd226744d056191deb0d596749c80a392` (6.217 b) + zip `408a17ecd3c1523dddef691e617e9e6ab74df01fe20fad665fc495be11935a61` (3.954 b · re-extração ≡ 2/2) + DIGITAIS (sha do zip publicado fora do zip — auto-referência impossível, registrado). Conteúdo: frase de aprovação verbatim · pedido único (trocar base V2.2→V2.3 no projeto e ecoar) · acuse da verificação técnica dele replicada 13/13 · destino das 3 observações (O-1→V2.4 · O-2→V2.4 · O-3→D-JSONM-ORIGEM-CONHECIMENTO) · crédito da precisão nova (`ancoras[].direcao_suporte` → minuta 2 L-06) · regra nova de rótulos · mesa ((i)×(ii), v1.5).
- **Regra de comunicação do operador (registrada, vigente daqui em diante):** respostas em linguagem simples · link direto de cada arquivo de entrega · carta ao mestre a cada movimento do projeto 1 (não notas soltas).
- **Resposta dada:** auditor-2 = SÓ o zip `948dbb35…` (instruções dentro; pedir sha do arquivo velho antes) · mestre = a CARTA 20 (md ou zip, tela) · CHANGELOG aberto na tela.
- decisoes_B1.md → **rev.61** · STATUS_SIMPLES → bloco Rodada 54 · **0 ciência** (nenhum artefato científico tocado; conversa + carta de regime).

## ABERTURA 55 — 2026-09-21
- Operador traz DOIS documentos: (1) resposta do mestre à carta 20 — eco 3/3 (V2.3+N1+N2 conferem) · registro: os schemas foram RENOMEADOS no projeto (sufixos caíram, '.'→'_'; bytes intactos) · base dele agora V2.3+selados · sugestão de higiene do projeto (tirar V2.2 e a cópia 'CANDIDATA_...') · destravado: minuta 2 L-06 PRONTA; minuta 2 L-NT espera só a decisão (i)×(ii). (2) análise do comentador pedindo VALIDAÇÃO documental: de onde a NT tira o conhecimento — verificar compatibilidade com Filosofia/V2.3/fluxos/Roteiro/DECISOES e classificar (i) e (ii).

## RESULTADO 55 — 2026-09-21
- **TRILHA 69: 15/15 verdes** (2 confissões datadas: C69-1 — régua case-sensitive na 1ª sondagem marcou 0× com quote presente de inicial maiúscula; C69-2 — comentador comprime quotes sem marcar (A1 sem '(NT)' · dever 6 sem 'integração à' · tríade-lista rendida como setas · paráfrase do fluxo do Motor) — conteúdo fiel, literal registrado).
- **Eco do mestre VERIFICADO:** 3/3 digitais == bytes da casa · "elo autêntico" ✔ · renome medido: apenas o separador difere do `$id` (risco da O-1 cai, como ele disse) · higiene ENDOSSADA com precisão de escopo: não-renomear vale só para a SÉRIE de trilha (17 scripts); base de projeto deve ficar só com o vigente de nome limpo (operador executa).
- **Réplica da análise do comentador (nos bytes):** 12 citações literais confirmadas (Filosofia F1/F2/F3 + bônus 'derivar exclusivamente' · V2.3 A2/A3/A4/A5 · §NT função+vedação de busca+deveres · fluxos segregados) · 4 compressões registradas · 1 síntese dele ('memória paramétrica' 0× nos textos; gancho na Filosofia) · Roteiro: 0 contradições · **DECISOES_ARQUITETURAIS ausente da base → dívida D-DECIS-ARQ-BYTES nomeada**.
- **Classificação entregue (régua do próprio pedido — passo 7):** (i) = compatível com todas as camadas, formaliza o fluxo JÁ decidido (não cria decisão arquitetural; bifurcação afirmação→Biblioteca §5.5 · evidência→N1→N2, com a medida 39/49 na mesa) · **(ii) = NÃO é escolha livre** — contradiz 'única fonte canônica' e exige emendar o §6 dever 1; só via emenda arquitetural formal sem necessidade demonstrada até agora. Resta 1 linha do operador: "(i), com a bifurcação desenhada" → destrava a minuta 2 do L-NT. Triangulação: COMO EXECUTAR v1.9 declara a mesma saída (registro, não auditoria).
- **Verbatims arquivados:** mestre `15384354…` (2.935 b) · comentador `3f67cd70…` (8.545 b, NÃO CIRCULA), com DIGITAIS.
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-21_CARTA21_MESTRE/` — md `c991fa9d612b549c7ef842987fb5a8445f0fb1f18856054ddd9276c4f4f238f5` (6.997 b) · zip `d7394cbe35eb7d2ebcb406ceb9cfd12f8296c96771c64182206368f3af202c49` (re-extração ≡) — pede ao mestre o envio da minuta 2 da L-06 (declarada pronta por ele).
- decisoes_B1.md → **rev.62** · STATUS_SIMPLES → bloco Rodada 55 · **0 ciência** (trio reconferido C01/C15).

## ABERTURA 56 — 2026-09-21
- Operador traz a resposta pendente do auditor-2 (eco do pacote 21/09 + a digital do arquivo velho do projeto dele) **E o documento DECISÕES ARQUITETURAIS** (upload `0 DECISÕES ARQUITETURAIS.md`, pedido da casa da rodada 55 — D-DECIS-ARQ-BYTES).

## RESULTADO 56 — 2026-09-21
- **TRILHA 70: 13/13 verdes.**
- **O fantasma era dos DOIS projetos:** a digital medida pelo auditor-2 no arquivo velho do projeto dele = `309aa65f…` (51.235 b · 1.421 l) — **BYTE-IDÊNTICA ao fóssil arquivado pela casa em 20/09** (vindo do projeto do mestre). Réplica interna 6/6 nos bytes: título V2 15.09.26 (l.1) · "…V2.2" no corpo (l.45) · §5.1 (l.276) · ponteiros v1.1 (l.280/317) · §26 (l.1.228) · contraste: V2 real de 15/09 (`09692e18…`, 46.129 b, 1.351 l) com §26 na 1.158. Suas leituras passadas transferem (mesmos bytes; registro agora com a digital certa). Correção dele cravada: "o nome mentia" — 6ª vez que a digital salva a mesa de um nome movido, 1ª vez com o mesmo nome mentiroso em 2 projetos ao mesmo tempo.
- **Remoções liberadas:** a condição dele ("depois que a casa registrar") já estava cumprida — fóssil arquivado com DIGITAIS desde 20/09 → sai hoje do projeto dele, junto com o `MANIFESTO_LINHAGEM.txt` de 19/09 (substituído pelo de 21/09); renomear a V2.3 dele para tirar `CANDIDATA_` = ENDOSSADO (projeto ≠ série). Faxina idêntica à do projeto do mestre (carta 21).
- **DECISÕES_ARQUITETURAIS recebido e verificado:** `1830ff9939d8c8028dbcad680f307196ede4155d59ecce1b512c31b8df42f296` (148.454 b · 2.781 l CRLF) — verbatim arquivado na série com DIGITAIS · 21 decisões P1–P21 (JSON interno não-estrito: vírgulas traseiras; extração por regex) · **P18 [DEFINIDO]: NT/JSON/Motor usam EXCLUSIVAMENTE a Biblioteca correspondente — "não realizando nova pesquisa bibliográfica nem introduzindo conhecimento externo"** + regras de atualização ("nunca o inverso") e precedência automática · P11: hierarquia de fontes ("decisões explícitas prevalecem sobre tudo") · **zero tensão Filosofia × V2.3 × DECISÕES → D-DECIS-ARQ-BYTES FECHADA** · a camada 4 do checklist do comentador reforça o veredito da r55: (i) formaliza o decidido; (ii) não é escolha livre · proveniência registrada (cabeçalho "v2_5 · AUDITADO POR ARENA E CHATGPT · 14/06/2022" — data anacrônica, conteúdo cita B16/GPM de set/2026; rótulo tipográfico, bytes preservados).
- **Eco 5/5** dos itens do pacote 21/09 no projeto dele · nota de régua: especificação aparece com "PROPOSTA" no nome no projeto dele (arquivo distribuído é limpo; bytes 78a0f2af ✔ — ornamento de plataforma/transcrição).
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-21_RESPOSTA_AUDITOR2/` — md `dec9678eaa4fd09e96a739fca257ca977c0daf43e20ef54f38e29ada6efa03ba` (6.699 b) · zip `315b0b103760fb928761c0787af8ed04b99852555a359d4338fb7d2670a34dae` (re-extração ≡).
- **Mesa:** continua valendo tudo da r55, agora reforçada pela P18 — sua linha "(i), com a bifurcação desenhada" destrava a minuta 2 do L-NT; minuta 2 da L-06 esperada do mestre (pedida na carta 21).
- decisoes_B1.md → **rev.63** · STATUS_SIMPLES → bloco Rodada 56 · **0 ciência** (C01/C13).

## ABERTURA 57 — 2026-09-21
- Operador envia a Minuta 2 da L-06 (protocolo de relações concorrentes · escada D-01) declarando autoria do **comentador** e pede análise de compatibilidade frente aos documentos e a tudo que foi decidido. Anomalia detectada já na entrada: o documento se assina "Auditor-Mestre · 2026-09-21" e se destina "à auditoria do Auditor-Mestre".

## RESULTADO 57 — 2026-09-21
- **TRILHA 71: 15/15 verdes. VEREDITO: COMPATÍVEL nas camadas verificáveis** (medida; nada aceito "no raciocínio").
- **Conferiu integralmente:** regime citado correto (V2.3+L-05+N1 v1.3+N2 v1.4 selados) · a correção-chefe = a correção PÚBLICA do mestre (linha 110 da verificação dele: "o degrau 5 da L-06 precisa ler `ancoras[].direcao_suporte`" — a minuta aplica 8×) · acervo B1: 6 naturezas EXATAS (109·100·56·4·4·1), matriz consistente, grau_maturidade 274/274 (degrau 6 executável), campos da Parte 5 274/274 · ausências declaradas verdadeiras (contexto/nivel_cadeia/sentido 0×; sentido marcado pela própria minuta como 'requer mapeamento') · schema N2 v1.4 tem `ancoras[].condicao`+`direcao_suporte` · Parte 9 ≡ P18/Filosofia · determinismo + errata datada + sem-precedência-emergente coerentes · V2.3 tem 0× L-06/escada (objeto vive no espaço de contratos do mestre; nota RESP6 da casa = camada de portão, sem choque).
- **2 precisões na ata:** P-1 `condicao` AUSENTE (0/274; não "esparsa") e `ancoras[]` 0/274 nos dados (contrato sim, dados não — retrofit) · P-2 degrau 5: a "marcação de extrapolação" EXISTE sem ser nomeada (`extrapolacao_por_analogia` 274/274 + verification_status extrapolado/preclinico) e `ancoras[].direcao_suporte` tem 0 portadores nos dados → degrau 5 parcialmente indisponível até o retrofit (mesmo regime honesto pedido).
- **1 pendência estrutural (do nosso acervo, não da minuta):** D-01/D-02 = 0× em 12 documentos; D-08 só 2× na deliberação → **dívida D-D01-D02-FONTE** (pedir o(s) documento(s)-fonte via operador; conteúdo coerente — é procedência, não choque) · mapa de fases da ordem (a minuta diz "Fase 3") declarado, não verificado.
- **1 correção de rito:** autoria declarada (comentador) × assinatura no documento ("Auditor-Mestre", destinado à auditoria dele) → corrigir a linha ANTES de circular (assinatura é metadado normativo — seria o 7º incidente de nome). Compatibilidade medida independe de autoria.
- **Recomendação de fluxo (decisão do operador):** (a) mestre audita esta minuta (duas minutas convergentes — esta já aplica a correção pública dele) ou (b) aguarda a do mestre e reconciliam · promoção futura pelo rito: proposta → réplica (feita) → aprovação formal do operador → vigente com sha/data.
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-21_ANALISE_MINUTA2_L06/` — md `7c6f56f0b5db29446e4db4ff3d616339ec212e50e33d9d2aac3dcc9c927db426` (6.145 b) · zip `441fb5709fdab580a2988fc5cd9c97d6600601f223ece16a91bec3a8e1cb4114` (re-extração ≡) · minuta verbatim arquivada `COMENTADOR_minuta2_L06_recebida_2026-09-21/` com DIGITAIS + nota de autoria.
- **Mesa (atualizada):** continua a linha "(i), com a bifurcação desenhada" · agora + caminho (a)/(b) para a Minuta 2 L-06 · pacote D-D01-D02-FONTE se quiser a ata final completa · demais itens inalterados (v1.5 · v1.8 · O-1/O-2→V2.4 · D-JSONM-ORIGEM-CONHECIMENTO).
- decisoes_B1.md → **rev.64** · STATUS_SIMPLES → bloco Rodada 57 · **0 ciência** (C01/C15).

## ABERTURA 58 — 2026-09-21
- Mestre envia a **Minuta 2 da L-06** dele (pedida na carta 21): retratação datada do degrau 5 + 1ª execução real da matriz sobre os 274 vínculos (4 falsos positivos → matriz corrigida → 0 pares) + regras novas do gatilho. Casa replica integralmente antes de responder.

## RESULTADO 58 — 2026-09-21
- **TRILHA 72: 15/15 verdes.** Minuta `eb54337c7f17c20fbd0ad1b926fd0d575b33462141537e837c4aff9fa13bbd13` (12.837 b · 185 l · LF) arquivada na série com DIGITAIS.
- **Retratação verdadeira (§0.1):** a frase dele de 21/09 ("degrau 5 lê `ancoras[].direcao_suporte`") localizava certo o campo e errava a semântica — o enum selado é direção do SUPORTE (sustenta/refuta/inconclusivo/condicional), não extrapolação. Degrau 5 passa a ler `verification_status` + `extrapolacao_por_analogia`. 7ª confissão bilateral datada. Coincide com a P-2 da casa (r57).
- **Execução replicada EXATA (§0.2):** matriz velha (proxy claim_id) dispara nos exatos 4 pares / 2 claims que ele relata (BLOCO02.011: 0035×0036 ×2; BLOCO02.019: 0052×0261, 0053×0261); bioleitura dos 6 vínculos confere (TNFR1≠TNFR2, arctigenina↓TNF, IL-10 mesma direção); **matriz nova → 0 pares**. Razões cravadas: natureza_relacao qualifica TIPO, não SINAL; **claim_id PROIBIDO como proxy de "mesmo objeto"**; gatilho passa a ser `ancoras[].id_oficial`+`escopo`+oposição.
- **CONFISSÃO C72-1 (casa):** 1ª corrida da réplica agrupou vínculos com claim_id='' como grupo → 77 pares espúrios; régua corrigida: vazio = ausente = sem par. Datada no script e aqui.
- **Comparativo codificado (C13):** a minuta do comentador carrega os 2 defeitos que a do mestre corrige (degrau 5 com campo errado; célula compensatoria×{causal,contributiva} geradora dos 4 FP) + marcador×nao_estabelecida sem caso no acervo. **Veredito da casa: minuta do MESTRE = base da consolidação + 2 RESGATES da do comentador** (teste T-14 "direção não-precedente" reformulável no regime novo; redação do determinismo "atribuição por relação, nunca pela posição").
- **Portão real (trilha 71/72):** `ancoras[]` 0/274 nos dados → gatilho não executável hoje; "a L-06 só roda sobre a B1 depois da migração" (243/274 migráveis à máquina, trilha 27 — registro RESPOSTA_7 da casa).
- **Continua valendo:** D-D01-D02-FONTE (a minuta 1 da L-06 nunca chegou à casa — entra no pacote; "substitui a minuta 1" é inverificável sem ela).
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-21_CARTA22_MESTRE/` — md `81f86e00987ccf255eccb5b42e744d0d42fee2952408911470f3f52add279995` · **zip `53efe37e8d503f959dc2133bb66e4a18ccefdf60ae81199b1c6abf9b4f9c089d`** (re-extração ≡).
- **Mesa:** sem mudança de fundo — linha "(i)"; consolidação L-06 (base mestre + 2 resgates) aguarda eco; aprovação formal do operador ao final do rito.
- decisoes_B1.md → **rev.65** · STATUS_SIMPLES → bloco Rodada 58 · **0 ciência**.

## ABERTURA 59 — 2026-09-21
- Operador: (1) "verifique se é possível usar a regra por fora" (rótulos fora do schema); (2) não sabe o que fazer com as cartas → **regra nova: todo documento passa a abrir com a ação do operador no cabeçalho**; (3) pede para comunicar os remetentes.

## RESULTADO 59 — 2026-09-21
- **"Por fora" verificado nos bytes (sem trilha nova — medida direta, env-arena):** a rotulagem [ETIQUETA-STATUS/B1] vive no documento de Governo B1-N1, INTEIRA fora do schema — nenhum byte selado (b06660fd/d96ad15b) se toca. Degraus 5-6 leem campos 274/274 existentes (rótulo calculável hoje); degraus 1-4 leem `ancoras[]`: 0/274 → esperam a migração N2 v1.4. Coerente item a item com a minuta 2 do mestre.
- **NOTA R59 "o que você faz com cada documento"** escrita com cabeçalho SUA AÇÃO + tabela documento-a-documento + MENSAGEM PRONTA para colar nos projetos (todo documento futuro abre com "AÇÃO DO OPERADOR / PRECISA DE RESPOSTA?").
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-21_NOTA_ACOES_R59/` — md `d3906fa9dcca53d92e553622ccbe9bfed9e20dafa868c2270a527a402d46505f` · **zip `ec943130cb584a7de4d3edc84748f23c63e17ceb817768f6746424677447ca3c`** (re-extração ≡).
- **Mesa (inalterada):** colar carta 22 no projeto do mestre · mensagem-pronta nos 2 projetos · linha "(i)" quando puder · pacote D-D01-D02-FONTE.
- decisoes_B1.md → **rev.66** · STATUS_SIMPLES → bloco Rodada 59 · **0 ciência**.

## ABERTURA 60 — 2026-09-21
- Operador: (1) corrige a casa — "não fiz a pergunta 'dá para usar por fora?'"; (2) diagnóstico de ritmo: endurecimento técnico, comentador é comentador (sugere, não produz documento), casa recebe comentário E posiciona-se, sem muro; ninguém é chefe; um corrige o outro; (3) envia a resposta do comentador: pedido de **cruzamento técnico A–F** das duas Minutas 2 da L-06, sem pré-decisão de arquitetura.

## RESULTADO 60 — 2026-09-21
- **TRILHA 73: 15/15 verdes** (nota de régua datada no script: prefixo do id 0261 corrigido na 1ª corrida — esperado errado, dado certo).
- **Cruzamento A–F entregue** (`ENTREGAS/2026-09-21_CRUZAMENTO_L06_MINUTAS2/`): 10 convergências medidas (invariante literal idêntica · não-descarte · escada 7 · 5-6 rotulam · degradada c/ nuance · determinismo · D-02 fora do gatilho · D-08 · não-criação · fecho operacional) · **correções nos DOIS lados**: comentador B1 degrau 5 campo errado (o campo certo estava na própria Parte 5 dela) · B2 matriz compensatoria×{causal,contributiva} = 4 FP medidos → 0 com a corrigida · B3 caminho ancoras[].condicao · B4 T-14 REVISADO: válido como está (casa retira o "reformulável" da carta 22) — mestre B5 regra degradada sub-inclusiva (só 2/4; pela própria justificativa dele, o 3 também barra) → adotar a geral do comentador · B6 renumerar testes novos · B7 mapear "carta 10" (numeração local).
- **Elementos exclusivos úteis:** mestre = mesmo-objeto operacional (id_oficial+escopo) + proibição claim_id · matriz corrigida c/ nota piloto · execução 4→0 + regressão real · tabela executabilidade · anti-armadilhas escopo/papel — comentador = gate de consumo (E1: amarrar 'aprovado' ao fluxo) · Parte 3 · Parte 1.3 (fronteira D-02) · Parte 4 (contrato do rastro) · determinismo 6.3/6.7 · regra anti-substituição-silenciosa · Parte 10 (arco do risco) · ausência-de-estrutura × fragilidade-de-evidência · T-14 — **todos com veredito PRESERVAR**.
- **Inconsistências novas (F):** F1 **colisão T-14/T-15** (mesmos IDs, critérios diferentes nas duas — must-fix) · F2 extensão da regra degradada · F3 ponte conceitual×operacional do "mesmo objeto" · F4 dívida comum sentido_relacao/Ontologia · F5 numerações locais cruzadas.
- **Propostas novas ≠ decididas (E1–E7),** incl. **D-GOV-B1N1-FONTE** (documento "Governo B1-N1" citado na conversa, 0 bytes na casa).
- **Confissões datadas:** C73-1 (atribuição "por fora" ao operador — errada; retirada, medição mantida) · C73-2 (carta 22 declarou "base+resgates" ANTES do cruzamento — enquadramento antecipado; este relatório o substitui por vereditos item a item) · assinatura do texto do comentador reclassificada: incidente de nome → **nota editorial** (correção do operador aceita: comentador sugere, não produz documento).
- **Diagnóstico de ritmo (registrado):** a casa aponta onde saiu dos trilhos — (a) veredito de base antes do cruzamento (r58); (b) tom de regra sobre as outras frentes na mensagem-pronta r59 (cláusula de devolução retirada — ninguém é chefe); (c) peso técnico nas respostas ao operador (sha/zips demais). Mantém-se: replicar antes de comentar, posicionar-se sempre, linguagem simples + link.
- **Entrega (R-DOWNLOAD-SEMPRE):** md `560537f64963fde163c4864522480d331e13b10dd1319831cfc995c07c2bb750` · **zip `c5f1b24e02be6ad4a633f8e3748e75e78bbbc8f0d01f6ae127d2aad457f3c2e8`** (re-extração ≡).
- **Mesa:** consolidada da L-06 aguardada (autores + operador) · "(i)" · D-D01-D02-FONTE · D-GOV-B1N1-FONTE · v1.5/v1.8 · O-1/O-2→V2.4 · D-JSONM-ORIGEM-CONHECIMENTO.
- decisoes_B1.md → **rev.67** · STATUS_SIMPLES → bloco Rodada 60 · **0 ciência**.

## ABERTURA 61 — 2026-09-21
- Operador envia a **Minuta 3 consolidada rev.1** (Auditor-Mestre, arquivo) + a **análise do comentador** (colada): pedido de parecer sobre os dois, verificação de proveniência/créditos e confirmação de 3 pontos técnicos (A degradada · B §7 · C testes T-19..T-23) — e carta ao mestre.

## RESULTADO 61 — 2026-09-21
- **TRILHA 74: 15/15 verdes** (4 réguas corrigidas no ato, datadas: bytes×ch UTF-8 · escopo da enumeração · conjunto×contagem T-18 · escopo do rótulo).
- **Parecer (carta 23):** conteúdo normativo VERIFICADO nas camadas medidas · **A confirmado+aceito** (resolutivo/qualificador resolve B5 melhor que as 2 anteriores) · **B confirmado** (§7 fiel ao N2 v1.4: escopo=subdivisão · TNFR1/2 0× no catálogo 146 · falha segura pós-migração) · **C confirmado**: regra ampla executada = **244 pares/41 claims, decomposição EXATA** (113/96/31/2+2 inclui os 4 FP) · T-19/T-23 não-sintéticos · T-18 oráculo pendente (E1) · suíte 23 IDs únicos (F1 resolvida).
- **PROVENIÊNCIA — autópsia nos bytes:** sha da minuta 1 declarado pelo mestre = **EXATO** (`3b6a15a0…`, arquivada na casa desde 15/09 c/ trilha 31 + RESPOSTA_10 `cc40dfa0…`) · os 7 grupos enumerados do achado = VERDADEIROS linha a linha na minuta 1 · **2 células que não batem: "atribuição por relação" 0× na minuta 1 (existe no TextoH 6.3 → emendar §6.3) e a linha "Parte 8 anti-substituição" (0× na minuta 1, fora da enumeração dele)** · o cruzamento r60 foi FIEL ao insumo (os 9 elementos existem no TextoH, linha a linha — inclusive `ancoras[].direcao_suporte` no degrau 5) → **TextoH ≠ texto recebido pelo mestre: existem DOIS textos sob um nome** · evidência independente: 8/8 frases "(Comentador)" da minuta 3 são 0× no TextoH · similaridade literal TextoH×minuta1 = 4% (reescrito, com conteúdo a mais) · ao comentador (pedido 1): listas proveniência×créditos são DISJUNTAS — não há atribuição dupla literal; bastam 3 emendas (§6.3 · marcar créditos TextoM-dependentes · frase-ponte).
- **CONFISSÕES datadas:** **C74-1** (r60: a zeroagem dos 4 FP é da matriz, não do objeto operacional — §7 do mestre aceito) · **C74-2** (rev.64 errada: "minuta 1 nunca chegou" — arquivada desde 15/09; dívida estreitada) · **C74-3** (varrimento r57 com escopo errado: D-01 a D-08 estão definidos na L05 1.1 desde 15/09 → **D-D01-D02-FONTE FECHADA por consumo interno**; remanescente pequena D-ORDEM-FASES).
- **Dívidas novas/pequenas:** D-L06-M3-ORIG (bytes da minuta 3 original a6a0027c — rev.1 declara "conteúdo normativo idêntico", inverificável sem ela) · D-TEXTO-M (o texto que o mestre recebeu como minuta 2 do comentador) · declaração de autoria do comentador (pergunta pronta na carta 23) · D-ORDEM-FASES.
- **Semelhança com o episódio V2.2 subscrita:** desta vez a salvação foi leitura comparada, não digital.
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-21_CARTA23_MESTRE/` — md `9921c58b83e54b9ffb8ddb0209745fd1d00272daa5bd84abe3c8593ca5ccc197` · **zip `d72e22afdab7b1e7a049b1eaed28f0ea65fc521040b311f472291344a54ab859`** (re-extração ≡).
- **Mesa:** rev.2 da minuta 3 (3 emendas) → réplica final da casa em 1 rodada → aprovação do operador · "(i)" continua · demais herdadas.
- decisoes_B1.md → **rev.68** · STATUS_SIMPLES → bloco Rodada 61 · **0 ciência**.

## ABERTURA 62 — 2026-09-21
- Comentador envia **carta de autoria**: escreveu as DUAS versões (rascunho com cabeçalho errado "Auditor-Mestre" = preparado p/ auditoria · canônica "Comentador · 2026-09-21") · pede des-atribuição da minuta 2 canônica dos 9 elementos · separa 3 artefatos · pede a cadeia documental dos 244/41 com digital exata, "sem reconstrução".

## RESULTADO 62 — 2026-09-21
- **TRILHA 75: 8/8 verdes.** Carta arquivada verbatim (`1cba2b14…`) com DIGITAIS.
- **Autoria registrada** (declaração = fonte de autoria; conteúdo = bytes; os dois vivem juntos na ata).
- **2 precisões com evidência:** (a) a fusão é **anterior ao cruzamento** — TextoH chegou contendo os 9 grupos no mesmo arquivo (o cruzamento foi fiel ao insumo; a mistura nasceu no rascunho) · (b) **2 órfãos de frase**: "atribuição por relação, nunca por posição" e "não substituir silenciosamente por campo parecido" = 0× na minuta 1 E 0× na RESPOSTA_10 → **redação do comentador** (crédito dele, com a emenda do §6.3 da minuta 3 agora com destino medido); linhagem de conceito registrada ("falta de dado vira afirmação" já na RESPOSTA_10 da casa, 15/09, l.79).
- **Mapa final de proveniência** na ata: 7 grupos → minuta 1 mestre (`3b6a15a0…`) · degrau 5 correto+matriz+proxy+execução → minuta 2 mestre (`eb54337c…`) · 2 frases → comentador/TextoH (`1a51d9b9…`) · itens canônicos → comentador/TextoM (bytes pendentes) · síntese (degradada resolutivo×qualificador · §7 · suíte 23 · 244) → minuta 3 rev.1 (`2ce9698c…`).
- **Cadeia dos 244/41 respondida:** enunciado (TextoM, declarado) → dados (`490675e6…`, 274) → execução casa trilhas 74/75 (comando declarado) → registro minuta 3 rev.1 §1.2 (`2ce9698c…`). **Artefato portador do número = minuta 3 rev.1 + arquivo de dados** · `a6a0027c…` segue digital-sem-bytes (D-L06-M3-ORIG), sem reconstrução.
- **Pedido que destrava:** TextoM (versão canônica em arquivo único) → casa fecha a ata em 1 rodada → rev.2 → aprovação do operador.
- **2 normas domésticas permanentes cravadas na ata:** todo texto que chega vira arquivo com digital no ato · autoria é metadado normativo.
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-21_ATA_PROVENIENCIA_L06/` — md `c926d4b1fd96f750520919eb8753def7c040bcc7fa641084bbedbdb4bf429e04` · **zip `c065d6760931fddc9f3581798ffd07d8c59e6bb7575afba0b7b14b973a6ec805`** (re-extração ≡).
- **Mesa:** rev.2 da minuta 3 · TextoM · minuta 3 original · "(i)" · herdadas inalteradas.
- decisoes_B1.md → **rev.69** · STATUS_SIMPLES → bloco Rodada 62 · **0 ciência**.

## ABERTURA 63 — 2026-09-21
- Operador cola a **minuta 2 CANÔNICA do comentador** ("Comentador · 2026-09-21 · Fase 3 da ordem de desenvolvimento") — o TextoM, peça da dívida D-TEXTO-M.

## RESULTADO 63 — 2026-09-21
- **TRILHA 76: 8/8 verdes.** TextoM arquivado verbatim (`8ad6bc157efe4c1a41f84a686a21a0f27a1549221508b46638d21cdb20968e09`) com DIGITAIS → **D-TEXTO-M FECHADA**.
- **O achado do mestre = 9/9 contra os bytes do TextoM** (degrau 5 sem campo · §1.2 significados · sem Parte 1.3/D-02 na 9 · Parte 3 degradada · Parte 4 direcao_suporte · 6.3 ordem testes/sem 6.7/sem "atribuição por relação" · Parte 8 dependências · Parte 10 fecho · sem disjuncao/niveis) — **o texto que ele recebeu é este; prova agora direta**.
- **Créditos canônicos todos com casa:** as 8 frases "(Comentador)" da minuta 3 presentes literalmente no TextoM → emenda nº2 da carta 23 SUPERADA (créditos verificáveis, sem etiqueta de pendência).
- **Mapa §9 lado C: 13/13 casam semanticamente** (T-02…T-15 × T-1…T-15 da canônica; grafia T-2×T-02 cosmética) → trava editorial da carta 23 destravada.
- **Órfãos confirmados na canônica-NÃO:** "atribuição por relação" e anti-substituição pertencem ao rascunho TextoH → destino final do §6.3 medido (Comentador, rascunho, Parte 6.3).
- **Cadeia 244/41 com TODOS os elos em bytes** (enunciado §1.1 canônica ≡ citação minuta 3 → dados → execução → registro) · único elo aberto: minuta 3 original `a6a0027c…` (D-L06-M3-ORIG, completude).
- **Caso das minutas misturadas: ENCERRADO** (5 artefatos com digital na casa). Próximos passos: rev.2 do mestre (3 emendas) → réplica final da casa em 1 rodada → aprovação do operador. Engenharia de fundo: migração N2 v1.4 (243/274).
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-21_ADENDA_ATA_L06/` — md `61f8ae64f6dfa1892755bd89e7ee3fd73a2378a36e53a3f9b2579d5972981e69` · **zip `6cb79f5ac9acad1bdb9ccf0ef72cec5ae1144fc0a89e26b22f2efde570950f45`** (re-extração ≡).
- **Mesa:** rev.2 da minuta 3 · "(i)" · herdadas.
- decisoes_B1.md → **rev.70** · STATUS_SIMPLES → bloco Rodada 63 · **0 ciência**.

## ABERTURA 64 — 2026-09-21
- Chegam a **minuta 3 consolidada REV.5** do mestre (`601c1f18d074e6e4488dd8a6ee3364345e51713f7d0277cd1637add838a79608` · 25.581 b · LF) e a **carta do comentador** sobre ela (4 pontos vistos como tratados + ponto 5: rodapé `f8ec8b72…` como intermediário + pedido de réplica mecânica final em 3 testes). "Não há solicitação de reabertura do conteúdo normativo."

## RESULTADO 64 — 2026-09-21 (pacote selado em 2026-09-22, rodada 65)
- **TRILHA 77: 11/11 verdes.** Recorte §2–§13 por âncoras de linha inteira = 186 linhas nos dois lados.
- **Pedido 2 (comentador): EXATO** — diff bruto = exatamente 1 diferença (−1/+1), a linha §6.3.
- **Pedido 3: EXATO** — `c863b8ed…` (rev.5 com nota) e `8a8ff986…` (rev.1/original com nota) reproduzidos byte a byte. Bônus: prova por bytes de que rev.1 ≡ minuta 3 original dentro do recorte (D-L06-M3-ORIG perde peso prático).
- **Pedido 1: na essência, com digital própria** — neutralizados, os dois recortes saem byte-idênticos; **digital-da-igualdade da casa = `4217cc635ee12842ad32c3520cda8f61adbef4e7765cdbcecb85065bac4971d0`**. `95c7cb41…`/`f8ec8b72…` não reproduzidos (bateria 6×4) e `95c7cb41` = 0× dentro da rev.5 → ou o mestre publica o comando exato, ou vale a digital da casa. Posição tomada (nada de muro).
- **Diff integral rev.1×rev.5 confinado a 5 zonas** (notas de revisão · proveniência · linha §6.3 · créditos · rodapé do rito) → conteúdo normativo estável. Auto-correção do mestre nos CRÉDITOS + retratação rev.3→rev.4 registradas.
- Confissões datadas **C77-1** (flexão "atribuídos") e **C77-2** (âncora caiu na citação inline) na réplica.
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-21_REPLICA_FINAL_L06/` — md `e80497bc5e5048fac71e4a4334c78b9dd1513e78f246bf62c5be42aec5764983` · **zip `e3ddd2233b309d84c3d16ad550597269eb791680add870c3683460677ffac684`** (re-extração ≡) · carta do comentador arquivada `b6c6b081…` · rev.5 copiada à série com DIGITAIS (rodada 65) · veredito: **RÉPLICA APROVADA, L-06 apta à aprovação do operador**.
- **Mesa:** frase de aprovação da L-06 · opcional rodapé `f8ec8b72…` · "(i)" · herdadas.
- decisoes_B1.md → **rev.71** · STATUS_SIMPLES → bloco Rodada 64 · **0 ciência**.

## ABERTURA 65 — 2026-09-22
- **Operador pesca erro da casa:** "a gente esqueceu que na minuta 1 tinha o 'atribui'" — de fato, linha 97, PARTE 4: "rótulos **atribuídos por relação**, não por posição". Pede solução coerente com o procedimento correto, para o erro não subir, com todos alinhados.

## RESULTADO 65 — 2026-09-22
- **TRILHA 78: 10/10 verdes** (primeiro teste saiu VERMELHO no falso amigo do radical — "atribuir força" no TextoM l.169 — e a regra pegou antes de publicar).
- **Autópsia com linha de código:** trilha 74 l.40 e 75 l.43 buscaram `atribui` (7 letras) → zero fabricado no `í` de `atribuídos`; régua assimétrica (7l na minuta 1 × 6l na RESPOSTA_10) no mesmo teste; e raiz "falta de dado vira afirmação de coexistência" creditada à RESPOSTA_10 quando é da **minuta 1 l.79 (mestre)**.
- **Mapa corrigido final:** (1) atribuição por relação — conceito = minuta 1 l.97 (mestre) · forma-regra = TextoH l.229-230 (comentador) · **rev.5 §6.3 já estava certa, sem 4ª emenda** · (2) anti-substituição silenciosa — raiz = minuta 1 l.79 (mestre) · norma-redação = TextoH Parte 8 l.278 (comentador).
- **Regra permanente R-BUSCA-1 cravada:** corpus fechado com digitais · padrão exato · família de flexão (radical sem cruzar vogal acentuável) · trinca de cada ocorrência · comando gravado · **nível L1/L2/L3 declarado — "ausente" só depois dos 3** · mesma régua para todos os corpora · correção sempre por adenda datada.
- **Confissões datadas C78-1** (padrão cego ao acento + régua assimétrica) e **C78-2** (fonte trocada a favor da casa) na adenda.
- Housekeeping da série: rev.5 copiada byte a byte para `MESTRE_L06_minuta3_consolidada_rev5_recebida_2026-09-21/` com DIGITAIS; DIGITAIS da carta do comentador (`b6c6b081…`) selados; placeholder da réplica substituído pelo sha real.
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-22_ADENDA2_ATA_L06/` — md `7dcd31b2733ea7b850023968458de4160035a9d89bedc20c54053032a889bee3` · **zip `9063178f2c2ddd497e52ebde32d6fe295bb3be4342f461d0c049f7019a4b4406`** (re-extração ≡).
- **Mesa:** adenda 2 aos dois projetos (alinha os três lados) · frase de aprovação da L-06 (inalterada) · aceite da R-BUSCA-1 como régua comum · "(i)" · herdadas.
- decisoes_B1.md → **rev.72** · STATUS_SIMPLES → bloco Rodada 65 · **0 ciência**.

## ABERTURA 66 — 2026-09-22
- Operador: "eu não disse essa frase" (a de aprovação sugerida pela casa) + diagnóstico de leituras equivocadas da ponte + pedido de re-análise da rev.5 e da carta do comentador.

## RESULTADO 66 — 2026-09-22
- **TRILHA 79: 9/9 verdes.** Confissão **C79-1**: a frase "Aprovo como vigente…" é de autoria da casa (nasceu na réplica, rotulada "Sugestão"); a adenda 2 a chamou de "a sua frase" (2×) — corrigido por errata datada. Livro-razão limpo: nenhuma aprovação inexistente registrada em CHANGELOG/decisoes.
- **Regra nova R-CITA-1** (extensão da R-BUSCA-1 p/ falas de pessoas): palavra de pessoa só como fato com citação verbatim+data · aprovação existe só quando a frase do operador chega · sugestão da casa sempre rotulada · sem a fala: a casa pergunta. Padrão reconhecido: 2ª vez (C73-1 "por fora" foi a 1ª).
- **Re-leitura verbatim:** rito da rev.5 · 4 pontos da carta · ponto 5 ("não é alteração normativa") · "sem reabertura" · fluxo de fechamento — leitura da casa CORRETA em todos, com trincas.
- **ACHADO A-79-1:** parágrafo dos órfãos (CRÉDITOS rev.5) sem a raiz do 2º item (minuta 1 l.79) + frase "a casa mediu 0× nela" medida na régua velha (verdade só no nível exato) → proposta: precisão de 1–2 linhas no toque editorial rev.6, junto do rodapé `f8ec8b72…` (opcional, não normativo, timing do operador; não bloqueia aprovação).
- **Dívida nova D-4AJUSTES-OPERADOR:** rev.5 diz "quatro ajustes do operador"; casa não tem a fala dele arquivada → pergunta feita na nota (régua nova: perguntar, não supor).
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-22_ERRATA_NOTA_R66/` — md `e142409c937842df244f4d065b8e170639093f527dd50f9106fad22ac6b04018` · **zip `4048963f409a5b0931f2340c41a452e03afa826afed5e471b42a33384a060dbb`** (re-extração ≡).
- **Mesa:** pergunta D-4AJUSTES-OPERADOR · opcional rev.6-2-linhas · aprovação L-06 só com a fala real do operador · "(i)" · herdadas.
- decisoes_B1.md → **rev.73** · STATUS_SIMPLES → bloco Rodada 66 · **0 ciência**.

## ABERTURA 67 — 2026-09-22
- Operador: esclarecimento mútuo sobre a frase (ele também tinha lido como obrigação; resolvido sem culpados — a ambiguidade nasceu na formulação da adenda 2, errata R66 de pé). **E define o RITO DE APROVAÇÃO correto (verbatim):** o ciclo é mestre → comentador → casa (organiza + opina) → volta ao mestre; **"caso ele aprove sem ressalva ta aprovado, caso ele mude algo, volto a passar pelo comentador, arena e depois devolvo para ele, até ser aprovado sem nenhuma ressalva"** · **"toda ressalva levantada deve passar pelos 3, comentador, arena e auditor mestre, ou estrutura, quando for o caso"** · **"só será aprovado qualquer documento ou decisão quando passar por todo os 3 e os mesmos concorde 100% sem ressalva."**

## RESULTADO 67 — 2026-09-22
- **Rito de aprovação do operador gravado verbatim** (decisoes rev.74) — substitui/refina a formulação anterior ("réplica da casa → aprovação do operador"): a aprovação do operador anda SOBRE a unanimidade sem ressalva dos três (mestre · comentador · casa; estrutura quando couber); antes de escrever "aprovado", o mestre responde primeiro.
- **Posição da casa registrada (sem muro):** aprova a rev.5 **sem ressalva no conteúdo normativo**; as duas precisões (rodapé f8ec8b72 + raiz do 2º órfão/medida corrigida) são editoriais, cabem no toque rev.6 e **não bloqueiam**.
- **CARTA 24 ao mestre redigida** (minuta da casa para o operador enviar): 4 anexos com digitais (réplica · carta do comentador — que pede encaminhamento a ele · adenda 2 · nota R66) + estado dos 3 testes (2 EXATOS · 1 com digital da casa) + **3 perguntas pontuais** (P1 texto sem ressalva? · P2 comando exato da neutralização OU aceita a digital da casa 4217cc63 · P3 rev.6-2-linhas agora ou depois?) + rito verbatim do operador.
- **TRILHA 80:** integridade dos anexos × digitais citadas na carta.
- **Ao comentador: nada agora** — a P2 decide se o encerramento dele fecha exato (comando reproduzido) ou por substituição (digital da casa); aviso na volta.
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-22_CARTA24_MESTRE/` — md `c02d530f978e99b2ded0daaa96975cbe6f520f26e17214914f11848e0e0166f8` · **zip `bec7e11a3ef4b8f7e80c27a3cac54f68e6f20759f91f5dfdf0389beffab1bead`** (re-extração ≡).
- **Mesa:** resposta do mestre às 3 perguntas → casa organiza → operador decide (frase dele) ou cicla · D-4AJUSTES-OPERADOR (aguardando; se vier junto, melhor) · "(i)" · herdadas.
- decisoes_B1.md → **rev.74** · STATUS_SIMPLES → bloco Rodada 67 · **0 ciência**.

## ABERTURA 68 — 2026-09-22
- Chegam, pelo operador: **rev.6 do mestre** (arquivo) + **parecer final do mestre** (P1 sem ressalva · P2 resolvida: publica o comando exato E aceita a digital da casa 4217cc63 como canônica · P3 executada na rev.6 no ato · subscreve R-BUSCA-1/R-CITA-1 sem reserva) + **parecer do comentador: "REV.6 — SEM RESSALVA DO COMENTADOR"** (pede a réplica mecânica final da casa com 6 verificações; aprovação reservada ao operador).

## RESULTADO 68 — 2026-09-22
- Arquivados no ato com DIGITAIS: rev.6 `98e90bdc…` (26.830 b · LF) · parecer mestre `72fe01f3…` · parecer comentador `b651bd8c…` (verbatim da ponte).
- **TRILHA 81: 10/10 verdes** — checklist do comentador ponto a ponto: identidade ok · 2 ajustes verbatim (órfão-2 com raiz na minuta 1 l.97/l.79 e "0×" recontextualizado por nível — l.305 da rev.6; rodapé f8ec8b72 rebaixado) · diff rev.5×rev.6 = 7 linhas confinadas às 4 zonas editoriais (§0/§1 intactos) · recorte §2–§13 invariante · **comando do mestre REPRODUZIDO EXATO: 95c7cb41… (valor integral 95c7cb410f369410…) nos dois lados — teste 1 fecha EXATO** (detalhe de serialização: \n final; bateria de 12 variantes) · **digital canônica da casa 4217cc63… reconfirmada na rev.6** · §6.3 byte-idêntico · 244/41 e T-23 com âncoras iguais.
- **Triângulo fechado SEM RESSALVA nos 3 lados** (mestre `72fe01f3` · comentador `b651bd8c` · casa: réplica md abaixo). Veredito da casa: **L-06 rev.6 apta à aprovação do operador — falta só a fala dele** (com as palavras dele; a casa ofereceu molde ROTULADO como sugestão).
- Posição sem muro registrada: **D-4AJUSTES-OPERADOR NÃO é ressalva** (pergunta de registro sobre o cabeçalho; zero regra envolvida; responde quando quiser) · pendências internas do documento (E1/E3/§7/migração) seguem como dívidas declaradas do próprio texto · D-L06-M3-ORIG perdeu peso de vez.
- Mestre **subscreve as duas réguas (R-BUSCA-1/R-CITA-1) sem reserva** e confessa os erros dele (rev.3 sem bytes; hashes sem comando).
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-22_REPLICA_FINAL_L06_REV6/` — md `4fdb0c5212ca34beb46c5b3e2b6ace26ec05d6b8b717689c7a088a4d7bd0b40b` · **zip `c47a407faa2ee9e90278b7f59723ff31e3dba1980d5a6bd6c9d71ad38ff12b64`** (re-extração ≡).
- **Mesa:** a frase de aprovação do operador (sobre a rev.6 `98e90bdc…`) → casa executa §6 da réplica (L06_VIGENTE.txt + registros + comunicado aos dois) · "(i)" · herdadas.
- decisoes_B1.md → **rev.75** · STATUS_SIMPLES → bloco Rodada 68 · **0 ciência**.

## ABERTURA 69 — 2026-09-22 — ★ A FRASE CHEGOU ★
- Operador, verbatim (R-CITA-1): **"Aprovo como vigente a L-06 — Minuta 3 consolidada rev.6, digital 98e90bdc, de 22/09/2026."**

## RESULTADO 69 — 2026-09-22 — ★ L-06 VIGENTE ★ (primeiro contrato da série a completar o rito ponta a ponta)
- **TRILHA 82: 3/3** — a digital da frase bate com o arquivo da rev.6 na série (`98e90bdc755162b28fd16817d65692cebe81f939c466ef1d29c7a0a1124f2b41`); a frase cobre artefato+digital+data; a aprovação pousa sobre o triângulo sem ressalva (decisoes rev.75).
- **ESCRITURA FEITA:** `_documentos_serie/L06_VIGENTE.txt` (`e8be95f5f6602d6c92e7c79d8c9f0317f0ec8bca2ab5f7b8f936c1e6808dcb9b`) — estado **VIGENTE — EM ESPERA DE PRODUÇÃO** · frase verbatim do operador · rito completo · triângulo com digitais · duas provas de estabilidade (`95c7cb410f369410…` · `4217cc635ee12842…`) · cadeia minuta1→rev.6 · medidas 244/41 e matriz 0 · portão de produção declarado · pendências herdadas vivas e nomeadas.
- **COMUNICADO DE VIGÊNCIA preparado** para o operador levar aos dois projetos (registro, não pedido) · regra suprema reafirmada: texto da L-06 agora congelado por digital; mudanças só pelo rito completo.
- **Fila destravada (não iniciada):** migração dos vínculos para N2 v1.4 (243/274, trilha 27) → piloto E2 → E1 oráculo gate → revisão formal E4 · L-NT (falta a "(i)").
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-22_COMUNICADO_VIGENCIA_L06/` — md `9091d7f32fe7641cdfe7eb66f8d9aea01cad24903cbb1d393fcb9e4daf67a9e9` · **zip `921e434499d9c142fde2a046941a1a02aa70a98f0543855500645fb43931892e`** (re-extração ≡).
- **Mesa:** "(i), com a bifurcação desenhada" (destrava L-NT minuta 2) · D-4AJUSTES-OPERADOR (registro; quando quiser) · v1.5 schemas · v1.8 COMO EXECUTAR · O-1/O-2→V2.4 · D-JSONM-ORIGEM-CONHECIMENTO · D-ORDEM-FASES · D-GOV-B1N1-FONTE · E1–E5 (documento vigente, dívidas declaradas) · planejar fila N2 v1.4.
- decisoes_B1.md → **rev.76** · STATUS_SIMPLES → bloco Rodada 69 · **0 ciência**.

## ABERTURA 70 — 2026-09-22
- Pergunta de fecho do operador: "no Arena não foi mudado nenhuma linha/letra/palavra da L-06 rev.6? Estou salvando nos meus arquivos como ela chegou."

## RESULTADO 70 — 2026-09-22
- **TRILHA 83: 3/3** — prova de integridade: uploads ≡ série (cmp byte a byte: IDÊNTICOS) ≡ digital da escritura L06_VIGENTE.txt; a mesma digital `98e90bdc…` foi medida na chegada (trilha 81 T1) e agora. **Dentro do Arena, a rev.6 não mudou um byte: a casa apenas a leu.**
- Resposta dada com escopo honesto + comandos para o operador conferir o arquivo no próprio computador (Get-FileHash/certutil/shasum) e para o mestre conferir o dele — todos devem dar `98e90bdc755162b28fd16817d65692cebe81f939c466ef1d29c7a0a1124f2b41`. Se algum der diferente: incidente a investigar, avisar a casa.
- **Mesa:** inalterada · decisoes → **rev.77** · STATUS → bloco Rodada 70 · **0 ciência**.

## ABERTURA 71 — 2026-09-22
- Operador pergunta: a L-06 precisa ir ao Auditor-Estrutura também, ou lá é outro caminho?

## RESULTADO 71 — 2026-09-22
- **Resposta (posição da casa):** o caminho da L-06 era o do mestre — aprovação completa e regular sem o estrutura (regra do operador: "…ou estrutura, quando for o caso"; L-06 é contrato do Motor). **Recomendada CIÊNCIA ao estrutura** porque o texto vigente nomeia 5 dívidas do território dele (medidas na rev.6: §8 portão N2 v1.4 l.220 · §7 D-L05-GRANULARIDADE-OBJETO "no N2 ou na Ontologia" l.198 · §11 contexto/nivel_cadeia · §1.1 sentido_relacao→Ontologia l.77 · §2 papel-proxy→Ontologia E3 l.139) — aviso de janela, não submissão; agenda dele (v1.5) inalterada; se levantar ressalva sobre o território dele → assunto NOVO do ciclo dele, não reabertura da vigência.
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-22_CIENCIA_AUDITOR2_L06/` — md `2e98c30a41a26f902e99c7aa04a050d811d2d7a9398b9be7b6f3f91ccb53ee19` · **zip `a253d8cad784a3816258cb6d4678c397462ee24502a3b46cb60e4f0b7395a1c8`** (re-extração ≡).
- **Mesa:** inalterada · decisoes → **rev.78** · STATUS → bloco Rodada 71 · **0 ciência**.

## ABERTURA 72 — 2026-09-22
- Operador: o Roteiro de Trabalho está acompanhando o processo? Pensa em enviá-lo a todos para seguirem o mesmo roteiro.

## RESULTADO 72 — 2026-09-22
- **Leitura honesta:** filosofia do roteiro INTACTA e confirmada pela prática (G1 comentador→casa→mestres · convergência sem teto de rodadas · contratos antes de produção · vertical slice B1) — **mas os campos de status pararam na era V2.2** (checklist e marcos desatualizados). Duas versões circulando: **plataforma** `5e3f9163…` (enviável) × **ROTEIRO_PROJETO.md** raiz `e280de03…` (DIÁRIO INTERNO da casa, parado em 13/09 — **não enviar**).
- **Posição da casa:** enviar o roteiro original + a **ATUALIZAÇÃO DE ESTADO datada (2026-09-22)** juntos, aos 4 projetos · página renovável por era, roteiro do operador não reescrito pela casa (revisão formal futura pelo rito).
- **Página escrita:** estado real item a item do §13 (V2.3 vigente `498e7df9…` · grupos subscritos+régua de aprovação verbatim · schemas selados N1v1.3/N2v1.4 + v1.5 pendente · L-NT minuta 1 verificada / aguarda "(i)" · **L-06 rev.6 VIGENTE** · claims estáveis com dívidas nomeadas · fila aberta: migração N2 243/274 → E2 → E1 → E4) · marcos §18 sugeridos · 3 réguas de mesa novas · 5 próximos passos.
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-22_ATUALIZACAO_ESTADO_ROTEIRO/` — md `8b5d1c8a28dee664f0963de75bad092a7136aae7f62bb14cf96482513ea488cd` · **zip `259e31a3522a1ea083f535f58eeaa404d983d5da1a79d3055d91d10a24cbb183`** (re-extração ≡).
- **Mesa:"(i)" · decisão dele sobre envio do roteiro+página · herdadas · decisoes → **rev.79** · STATUS → bloco Rodada 72 · **0 ciência**.

---

## ABERTURA 73 — 2026-09-22 (resposta do auditor-2/estrutura sobre o §8 da L-06)

Reação ao veredito do auditor-2/estrutura sobre a nota de ciência: o número do §8 da L-06 vigente (243/274) é da era v1.1; contra o **v1.4** a mesma migração mecânica dá **224/274** (a regra D3, nova na v1.4, exige segunda âncora dos 20 redirecionados). Ele sugere portão por critério, não por número. Casa replica tudo antes de responder.

## RESULTADO 73 — 2026-09-22 (trilha 84: ponto dele CONFERE · portão por critério adotado)

- **Trilha 84 (10/10):** regra D3 verbatim no v1.4 digital d96ad15b620fa373…; regra condicional entrou na v1.4 (0× em v1.1/v1.3, nível L1); V7 lida: 20 redirecionados (todos CANDIDATO) · 30 B1_v2 VALIDADO · 224 = 274−30−20 (nível declarado: mecânico) · 223 estrito elegível-curatorial · era v1.1: 243 (trilha 27 reconfirmada); papel não-proxy verbatim na R7/enum v1.4; contexto/nivel_cadeia inexistentes como propriedade (0× nas três versões); nuance do campo escopo confirmada verbatim (R4).
- **PONTO DELE CONFERE 100%.** Nota histórica da casa: a data "v1.3" para a saída do `sentido_relacao` não se confirma (campo inexiste nas três versões; zero impacto).
- **CASA ADOTA O PORTÃO POR CRITÉRIO:** "migração concluída quando o validador acusar ZERO não-conformes contra o N2 v1.4 digital d96ad15b…" — conselho técnico ao operador; L-06 doc não tocada (portão é da casa; linha doc = citação datada).
- **Adendo datado anexado ao L06_VIGENTE.txt:** sha vigente 31b9d4c06938a2c8932606fc75cca9c18acfc5b0cd3960dd7686c25a4e08bbe5.
- **Página do roteiro rev.p1:** portão por critério (ref. 224/274; era v1.1: 243). Pacote: md a0d8df54b2c40d012a6b93efbfbd9d8bfa3033f0c4bd64af5e8c292c23d9ef3e · DIGITAIS atualizado · zip c6e566924c264dd48be5cd68b55f7c644a2150388031cb7d512897e036d3a2f7 (re-extração ≡).
- **Nota de resposta ao estrutura selada:** ENTREGAS/2026-09-22_RESPOSTA_AUDITOR2_PORTAO/ · md 2380f73c7a736a25ea44ad8718fdd3c77586990cb329ce8e606078d30cad9b87 · zip 8bff7412d102c35130eca9c576cc096abea7fd4f9aee10b03d2f2cbdb249c7ec (re-extração ≡).
- Enquadre dele aceito (assunto do ciclo estrutura, não reabertura) → mestre e comentador NÃO acionados neste ponto nesta rodada. Rito respeitado: se a mesa um dia tocar o texto L-06, passa pelos 3.
- decisoes_B1.md rev.80 · STATUS_SIMPLES → Rodada 73.

## ABERTURA 74 — 2026-09-22 (operador pede: confrontar COMO EXECUTAR v1.9 × L-06 vigente; mapear pendências que esperavam mestre/estrutura; desenhar a aprovação do v1.9 para uso nos claims clínicos)

## RESULTADO 74 — 2026-09-22 (trilha 85: 7/7 · confronto entregue · 0 contradições; pendências re-mapeadas por dono: 4 do operador, 1 de ciclo editorial (correção G3), 2 registradas)
- **Identidade:** v1.9 `1cd90b40…` upload ≡ série ✔ · L-06 `98e90bdc…` vigente ✔.
- **Veredito do confronto:** documentos ORTOGONAIS (alfândega da evidência × juiz de concorrências) · 0× acoplamento nominal nos dois sentidos · convergência filosófica verbatim (consenso não é prova ≡ não fabricar precedência · registrar divergência ≡ preservar as duas + lacuna · nunca estimar ≡ nunca preenchimento implícito · ressalva viaja ≡ rotular não desempatar).
- **ACHADO PRINCIPAL:** a correção "G3 é parecer, não fechamento / retorno às IAs 1-2 / confirmação conjunta" (consolidado B de 18/09) está **AUSENTE do v1.9** — 0× nos 3 padrões exatos (trilha 85, trincas; 4 "retorn" casuais descartados por leitura — C85-2).
- **Pendências re-mapeadas:** mestre e estrutura JÁ responderam em 18/09 (deliberação B + resposta 9). O que falta: **P2** linha "(i)" (operador) · **P3** destino da ressalva em N2 (estrutura/v1.5 + operador) · **P4** quem audita os N1/N2 (operador) · **P6** homologação do fluxo (operador) · **P1** correção G3 → v1.10/adendo (ciclo editorial) · **P7** piloto .014 sem resultado na base (pergunta) · **P8** elo v1.8 (linhagem, baixa) · **base ancorada 15/09 defasada** (Bloco v1.6 × trabalho de 17/09 citado no v1.9) → pedido de bytes.
- **Réplica do kit:** 41/22/8/14 ✔ e o "21" do mestre reconciliado (22 entradas − 2 ids fora da Lista (012b/012c) → 41−20=21 ✔). C85-1 confessada (26 citações ≠ 22 entradas; corrigido antes de publicar).
- **Posição da casa:** v1.9 aprovável no conteúdo, mas NÃO agora — Rota A recomendada (v1.10 com P1 primeiro; um ciclo de aprovação só) × Rota B (aprovar já com trava no protocolo 3-IAs). Decisão: operador.
- **Entrega:** `ENTREGAS/2026-09-22_CONFRONTO_V19_X_L06/` md + DIGITAIS + zip (re-extração ≡; shas abaixo).
- 0 ciência nos vigentes; nada enviado a auditor. decisoes → rev.81 · STATUS → bloco Rodada 74.
- Shas R74: md confronto `2e4ee31a65b1559d66500df1cdf571f0f0cf7908c28ed2505a9d3f5087879407` · zip `d1ad5c463ba95a3e7a6811e17cf69490dc5becd54deff8adbb6fb516ec2e0b52` · trilha85 json `72e07ac1245988b8…`.

## ABERTURA 75 — 2026-09-22 (comentador responde ao confronto v1.9×L-06 com carta: NÃO aprovar o v1.9 agora; rito de fechamento por rodadas de pareceres territoriais; pedido à casa: transformar em 2 encaminhamentos)

## RESULTADO 75 — 2026-09-22 (trilha 86: 5/5 · posição da casa: ACEITO o rito, 0 discordância material · 2 encaminhamentos escritos (carta 25 mestre · encaminhamento estrutura) · supersede declarado de 2 perguntas da r74)
- **Carta arquivada no ato:** `COMENTADOR_carta_rito_fechamento_v19_2026-09-22/` sha `b6af4662a0985d72ceb0888a337db056bcf332e53c0a036934f401aade34879b` (11.051 b).
- **Trilha 86 (5/5):** citações factuais dele ≡ trilha 85 ✔ · toca P1/P2/P3/P4/P7, não toca P5/P6/P8 (registrado) · **a P1 dele ESTENDE o consolidado B: "independent" 9× na carta × 0× no consolidado — reescreve o papel da IA2 e resolve a tensão anti-ancoragem do v1.9** · P3 dele ≡ L-06 §5 verbatim (mesma regra, chegada independente) · rito dele compatível com o rito supremo do operador (4 frases verbatim).
- **Posição da casa (sem muro):** aceito integral; complementos marcados como complemento (deliberação 18/09 já cobre 4 dos 6 eixos filosóficos de P2 — carta 25 pede formalização + 2 novos; custo operacional das 3 janelas cegas declarado).
- **Supersede declarado (honestidade de registro):** PERGUNTA 2 da r74 (linha "(i)") → P2 virou derivação técnica; PERGUNTA 3 (rota A×B) → respondida pela carta (ninguém aprova agora = Rota A com método mais fino).
- **Entrega:** `ENTREGAS/2026-09-22_ENCAMINHAMENTOS_V19_RITO/` — resposta casa `728e40e1…` · carta 25 mestre `a12187e3…` · encaminhamento estrutura `d385d772…` · zip `9b7087925e461c1a1a956ff159a2e5d22f6475f4e8f26a4946a50af1371a126a` (re-extração ≡ 3/3).
- **Envio depende do operador:** 2 janelas limpas separadas (anti-contaminação). Perguntas mantidas: piloto .014 (execução formal? registro?) · bytes Bloco/Lista ≥17/09 (necessários na Rodada 5).
- 0 ciência nos vigentes · decisoes → rev.82 · STATUS → Rodada 75.

## ABERTURA 76 — 2026-09-22 (comentador encaminha os 2 pareceres territoriais e pede a Rodada 3: confronto mecânico classificado A–E, sem transformar em aprovação)

## RESULTADO 76 — 2026-09-22 (trilha 87: 16/16 · CONFRONTO RODADA 3 entregue: ZERO divergência material · P2 núcleo convergente · P4 invariante convergente · 9 itens fora do manual)
- **Pareceres arquivados no ato:** estrutura `cd86bc7aa635fc6d9289b0acbd41604208ddf24048e4135a7e3208eccae18f07` · mestre `bad402385b1f9d7ac94d65eb5856e866fd25afd16e90895eadbeae7d566b64fc` (upload ≡ série). Anti-contaminação declarada pelos dois ✔.
- **Classificação:** P1 = D (estrutura recusa expressamente) + território do mestre ✔ · P2 = **A núcleo** + 1 item de silêncio registrado (assimetria/ordem — não lido como consenso) · P3 = C + D (mestre recusa) · P4 = **A invariante** ("a fidelidade de um N1/N2 nunca é atestada por quem o produziu" — enunciada pelo mestre, demonstrada pelo estrutura ao recusar o papel tautológico) · **B (divergência material) = NENHUMA**.
- **Medida replicada pela casa:** o 274/274 trecho_ancora do estrutura CONFERE — 273/274 em L1 estrito + 1 caso (VINC_B1_0153) que exige L2/whitespace (texto idêntico palavra a palavra) → invariante real, nível declarado. Mais: 274 vínculos ✔ · 237 fichas ✔ (201+33+3) · mapeamento da ressalva campo a campo no N2 v1.4 ✔ (if/then de `condicao` obrigatória/proibida) · `CLAIM_KIT_CLINICO` ausente do N1 ✔ · 0 chaves-âncora no kit ✔ · 4/4 referências de linha do mestre ao v1.9 ✔.
- **Confissão C87-1:** primeiro teste da casa acusou 1 falso órfão (régua sensível a whitespace) — corrigido antes de publicar.
- **Consequências para a v1.10 (demonstradas):** C-1 a C-5 (IA3 parecer ≠ fechamento · análises cegas independentes · retorno e registro sem apagar originais · fonte primária árbitro · ressalvas preservadas). **Extensões não normativas:** X-1 a X-4. **Fora do manual (ciclos próprios):** dedup N1 por pmid_oficial · portões de ancoragem textual e de fidelidade da ressalva · CLAIM_KIT_CLINICO (v1.5) · atribuição da auditoria (depende de E-2) · instrumentos e critério falsificável do piloto · herança do rito dos três. **E-6 novo:** o portão de fidelidade da ressalva cai sob a invariante do mestre se executado por quem escreve a `condicao` — registrado sem decisão.
- **Rodada 4 não acionada** (zero divergência); E-1 (ordem) fica opcional ao operador. **Entrega:** `ENTREGAS/2026-09-22_CONFRONTO_PARECERES_RODADA3/` md `658b0de8db2d37be48d9fa42965d7f049907a59a1cacad2b1c71dafc7504def8` · zip `fdf3e13cc384766d34ffc806d555cb746e921ce87392621f2dd86ac4c14c3cd9` (re-extração ≡ 5/5).
- 0 ciência nos vigentes · decisoes → rev.83 · STATUS → Rodada 76.

## ABERTURA 77 — 2026-09-23 (comentador: carta de interface Claim Clínico → N1/N2 + anexo com 3 estruturas)

Operador colou a carta do Comentador “Proposta de solução de engenharia após a Rodada 3” (2026-09-23) e anexou `ESTRUTURAS DE JSONS VÍNCULOS,PMIDS, BLOCO DE ESTADO.md`. Pedido: classificação campo a campo (A–I + matriz §15) antes de levar proposta concreta aos dois auditores.

## RESULTADO 77 — 2026-09-23 (trilha 88: 16/16 · classificação entregue · menor alteração suficiente · ordem Biblioteca→N2 reafirmada)

- **Arquivamento:** série `COMENTADOR_carta_interface_claim_N1N2_2026-09-23/` — carta sha `6c8042da5430d6ccf5f6c9f7ddf3a3ccdf47c07dca26e514ebb7de441133680c` · anexo upload ≡ série `c58617a976362428b0dc91d7c7a77551578e3a590e44bda6fa5bb23954a58886` (27.518 b, CRLF).
- **TRILHA 88 (16/16):** anexo ≡ corpus real (VINC_B1_0001..0006 ✓; trecho VINC_B1_0001 byte-idêntico; claims SM02 ✓) · N1 `claim_id_origem` string e 54/237 preenchidos com um claim_id cada (§10 confirmado) · `CLAIM_KIT_CLINICO` ausente do enum ✓ · Bibliografia 237 fichas / **0 duplicidade de PMID** ✓ · N2 required ancora/condicao ✓ · kit 0× chaves-âncora ✓ · Bloco 8+14=22 statuses · **14 PMIDs do Bloco fora da Bibliografia** (12 claims) — reconciliação técnica, não ciência · **C88-1** (régua T13 sem indentação → 0/0; corrigida antes de publicar).
- **Posição da casa:** aceita a hipótese “sem sistema paralelo”; **correção de ordem** — `usado_em_biblioteca` 22/22 `nao` e `trecho_ancora` exige frase na canônica ⇒ passo de entrada na Biblioteca **antes** do N2 (mesma assimetria E-1 da r76); segregação de auditoria da r76 preservada.
- **Matriz A–I + §15:** o kit não deve ganhar `trecho_ancora`/`ancoras`/`condicao` por antecipação; falta real = contrato de saída + passo Biblioteca + resolução pmid→referência + enum v1.5 (ciclo próprio) + reconciliação dos 14 PMIDs.
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-23_CLASSIFICACAO_INTERFACE_CLAIM_N1N2/` — md `9770fe6a128b6a72e4aa97d3161c4b8eec75dd63c496bbce41589eb04ff9dc27` · **zip `839c2cff21ab2c59002c9bf8930bc535134aaac8bee405d922f0a61949adc63b`** (re-extração 6/6 ≡).
- **Mesa:** operador leva a peça aos **Mestre e Estrutura** em janelas separadas com a pergunta de compatibilidade da carta §16 · nada vigente alterado · **0 ciência**.
- decisoes_B1.md → **rev.84** · STATUS → bloco Rodada 77.

## ABERTURA 78 — 2026-09-23 (operador envia os dois pareceres de interface Claim→N1/N2)

Pareceres territoriais de 2026-09-23 (Mestre e Estrutura) sobre a pergunta da carta §16 / Arena §3. Pedido implícito do rito: confronto mecânico.

## RESULTADO 78 — 2026-09-23 (trilha 89: 15/15 · CONFRONTO · 1 divergência material D1 · Rodada 4 a acionar)

- **Arquivamento:** `PARECERES_INTERFACE_CLAIM_N1N2_2026-09-23/` — Mestre `cbc0ab796b59f577f9faac94f23cd0c89817f2ee0184ffd215a0fc926d262c99` (8.654 b) · Estrutura `86d09995eb7a09070e0020feb0f19875b294c4fd0420fbf3ed40266348d46fd3` (8.632 b) · uploads ≡ série.
- **TRILHA 89 (15/15):** todos os números técnicos do Estrutura conferem (REF+sufixos · pattern VINC · 244+30 · max 0274 · forca/gm 274/274 · evid_role fora do schema e 237/237 no legado · escopo sem SM-02) · cadeia L-06 regra 3 1× verbatim · ressalvas do kit com heterogeneidade 4/7 · anti-contaminação: Mestre declarou “não li”; Estrutura 0× (fato textual).
- **Convergências (A):** núcleo arquitetônico compatível · ordem Biblioteca→N2 · `claim_id_origem` proveniência · enum via ciclo · fidelidade não é do produtor.
- **DIVERGÊNCIA MATERIAL (B):** **D1** — Estrutura: ressalva com **mapeamento único** → `condicional`+`condicao` (reafirma r76) × Mestre: **roteio por tipo**; universal **fabrica condição** e envenena degrau 3 da L-06 · **D2** = mesma coisa na forma binária da pergunta (impedimento epistemológico: não × sim).
- **C+D:** 4 pontos técnicos só do Estrutura (colisão REF→sufixo **corre a minuta r77 §E.4** · escopo pelo destino · prefixo da série clínica · eixos vazios=não-aplicável) · E-6 fechada por ele com condição; roteio é montante (classe I).
- **Posição da casa:** D1 é tese real, não ruído; casa **não** escolhe vencedor; minuta r77 tem erro de falha dura de id — corrigir na reemissão; **acionar Rodada 4** só com D1/D2 pelo rito dos 3 do operador.
- **Entrega:** `ENTREGAS/2026-09-23_CONFRONTO_INTERFACE_PARECERES/` — md + 2 pareceres + classificação r77 + trilha 89 + DIGITAIS + zip (re-extração 7/7).
- **Mesa:** confronto ao Comentador (condutor) + devolutiva D1 aos dois em janela de Rodada 4 · 0 ciência · nada vigente alterado.
- decisoes → **rev.85** · STATUS → bloco Rodada 78.

## ABERTURA 79 — 2026-09-24 (comentador envia SOLUÇÃO DA D1 — dois eixos; casa prepara Rodada 4)

Carta “SOLUÇÃO DO COMENTADOR — D1” (2026-09-24): separar estado de validação (`status_auditoria`) de direção evidencial (`direcao_suporte`); abolir `aprovado_com_ressalva → condicional` automático; classificar ressalva no Claim Kit antes da materialização.

## RESULTADO 79 — 2026-09-24 (trilha 90: 11/11 · casa ACEITA a tese · Rodada 4 pronta com §17)

- **Arquivado:** `COMENTADOR_resolucao_D1_2026-09-24/COMENTADOR_SOLUCAO_D1_2026-09-24.md` sha `b83bcc9457846fe2010976f3ba202e53446a38c2eea002d1cf19ce57c03b57dc` (15.072 b).
- **TRILHA 90 (11/11):** N2 enums/if-then ✓ · `.001` verbatim ✓ · Schema-Claim sem `ressalvas[]` (lacuna real) ✓ · kit heterogeneidade ✓ · L-06 inferência silenciosa 1× ✓ · **Tabela G r77 da casa continha a cadeia abolida** (autocrítica) · eixos em camadas distintas do N2.
- **Posição da casa: ACEITA** a solução de dois eixos; preserva os dois pareceres; E-6 em duas camadas. Ressalvas H-1..H-3: `ressalvas[]` = ciclo do kit; direção efetiva não-condicional = item de contrato (H-2); D1 não encerra sem 2× sem ressalva.
- **Tabela G da r77 SUPERADA** (condicionada à subscrição territorial). 0 alteração de schema/kit/L-06.
- **Entrega:** `ENTREGAS/2026-09-24_RESPOSTA_D1_RODADA4_PRONTA/` — resposta + carta do comentador + **textos prontos §3.A/§3.B** para as duas janelas da Rodada 4 + trilha 90 + zip (re-extração 5/5).
- **Mesa:** operador cola Rodada 4 nos dois auditores (janelas separadas, anexo = carta D1) · 0 ciência.
- decisoes → **rev.86** · STATUS → bloco Rodada 79.

### Ajuste r79 — 2026-09-24 (operador perguntou se H-1/H-3 estavam nos blocos de colagem)
- Confirmou-se lacuna: H-2 só no §3.A (ok); H-1 e H-3 ausentes dos blocos. Bloco rev.2: H-1 e H-3 acrescentados aos §3.A e §3.B. Zip refeito (re-extração 5/5). Conteúdo técnico da tese inalterado.
- rev.3: 1ª correção só pegou no §3.A; §3.B refeito. Validação final: H-1 2× e H-3 2× (um em cada bloco) · zip novo re-extração 5/5.
- rev.4 (pedido do operador): §0 de envio da digital da casa nas duas janelas + bloco de assinatura. **Digital da casa (RESPOSTA md):** `cd9167da718540708952dc080479df714467f1240ca6011f5d1a6de3d228576f` · zip `cdc25cffd062fdf1ab22adbef013addd417372d0d4915dd337528b4080dce906` (re-extração 5/5).
- rev.5 (operador apontou vazamento cruzado se mandasse o doc único): split em `CASA_POSICAO_D1` (só posição+digital, vai às 2 janelas) + `COLA_RODADA4_ESTRUTURA` + `COLA_RODADA4_MESTRE` (verificação: sem nome do outro no arquivo alheio). Rodada 4 permanece necessária (rito dos 3); o que mudou é só o embalagem. zip refeito (re-extração 8/8).

## ABERTURA 80 — 2026-09-24 (Rodada 4 · D1: pareceres do Mestre e do Estrutura; operador pede análise + carta ao comentador sobre rito das 3 IAs)

## RESULTADO 80 — 2026-09-24 (trilha 91: 13/13 · D1 ABERTA por H-3 · carta ao comentador · rito 3 IAs: manter, fortalecido)

- **Arquivados:** `PARECERES_RODADA4_D1_2026-09-24/` — Mestre `db0ed08c73f82f46240be97916e1fb2fff96c1a88a807c30063c5a8c2e1f8541` · Estrutura `c41717c81dce8eae78cc4a05e19ce0b9afb0da2243cd64fb623a6ab335a10472` · uploads ≡ série.
- **TRILHA 91 (13/13):** vereditos (E sem ressalva; M modelo sem + fechamento **com 2 ressalvas**) · `direcao`/`refuta` 0× · 15 marcadores (stem `nul`=15; rótulo “nula”=nulo 4 — número confere) · moderadores 3/5/1 · `inverte` no `.001b` aprovado_com_ressalva · `grau_maturidade` 274/274 · v1.2 sem `sentido_do_achado` · **v3.1 com campo OBRIGATÓRIO** (`f7e664d7…`) · L-06 disjunção ✓ · confissão do Estrutura ✓ · **T12: D1 ABERTA**.
- **Confronto:** modelo subscrito pelos dois sem ressalva · H-2 convergente (vocabulário v3.1 × classificação no fechamento) · pendências = R-1 e R-2 do Mestre · Estrutura confessa autoria da regra abolida · Mestre: solução melhor que a própria formulação.
- **Carta ao comentador:** estado H-3 · rota A/B/C · **casa prefere A** (integrar R-1+R-2 e devolver minuta final) · decisão = condução.
- **Rito 3 IAs (pedido do operador): NECESSIDADE SIM.** Padrão das rodadas: classificação científica migrou para o fechamento do claim; materializador ficou mais mecânico. Casa: manter + **piloto .014** (E-4) como gesto coerente seguinte.
- **Entrega:** `ENTREGAS/2026-09-24_CARTA_COMENTADOR_RODADA4_D1/` — carta + 2 pareceres + trilha 91 + zip (re-extração 6/6).
- **Mesa:** operador leva carta+pacote ao Comentador · 0 ciência · nada vigente alterado · **D1 aberta**.
- decisoes → **rev.87** · STATUS → bloco Rodada 80.

## ABERTURA 81 — 2026-09-24 (comentador decide ROTA A: integrar R-1/R-2; pede minuta final do contrato de saída + dupla subscrição)

## RESULTADO 81 — 2026-09-24 (trilha 92: 13/13 · MINUTA escrita · pacote de subscrição pronto)

- **Carta arquivada:** `COMENTADOR_conducao_RotaA_2026-09-24/COMENTADOR_CONDUCAO_ROTA_A_2026-09-24.md` sha `1cefd1489af72a43e958fce4064389d98a3caec7c074b397ce4e3f827c05f160`.
- **Rota A escolhida** (§20): D1 núcleo resolvido · R-1 direção por fonte com vocabulário v3.1 · R-2 fonte única de condição + atenua/amplifica no claim + inverte→dois N2 + maturidade→grau_maturidade · rito 3 IAs **mantido** · piloto .014 com desenho congelado · 6 portões · §18 define o conteúdo da minuta · §19 critério de encerramento.
- **TRILHA 92 (13/13):** enums dos dois eixos distintos ✓ · mapeamento 3→3 biunívoco ✓ · v3.1 enum+OBRIGATÓRIO ✓ · .001b ✓ · 6 portões ✓ · minuta cobre D1/R-1/R-2 e declara 0 alteração N1/N2 ✓ · confissões de régua: 2 falsos negativos corrigidos antes de publicar (negrito/caso).
- **MINUTA escrita:** `ENTREGAS/2026-09-24_MINUTA_CONTRATO_SAIDA_CLAIMKIT/MINUTA_CONTRATO_SAIDA_CLAIMKIT_2026-09-24.md` — 11 §§: princípio único · D1 · R-1 (falha dura sem direção) · R-2 (fonte única; inverte dois N2) · ressalvas[] delimitado · tabela de materialização · P-K1..P-K5 com trava · 6 portões · §19 · pergunta única de subscrição.
- **Entrega:** mesmo diretório — minuta + carta Rota A + COLA única (mesmo texto para os 2) + trilha 92 + zip (re-extração 6/6).
- **Mesa:** operador cola a COLA nas duas janelas com os anexos · 0 ciência · **minuta NÃO vigente** até dupla subscrição limpa.
- decisoes → **rev.88** · STATUS → bloco Rodada 81.

## ABERTURA 82 — 2026-09-24 (subscrições da minuta: Mestre sem ressalva; Estrutura segura no §4.3 inverte; operador pergunta se o Mestre precisa da v3.1)

## RESULTADO 82 — 2026-09-24 (trilha 93: 12/12 · objeção CONFIRMADA no allOf · minuta rev.2 (P-K6) · v3.1 a ir ao Mestre)

- **Arquivados:** Mestre `40b0205c…` (upload ≡ série) · Estrutura `63e23c2a…` (texto do operador, verbatim).
- **TRILHA 93 (12/12):** allOf âncoras: condicional⇒condicao required · sustenta/refuta/inconclusivo⇒condicao **null** · simulações T4/T5 **violam** (objeção do Estrutura CERTA) · par do §4.3 rev.1 presente · 30 refs multi-vínculo e SWANSON 3 (medida do Mestre) ✓ · Mestre declarou não receber v3.1 ✓ · v3.1 existe com enum ✓ · rev.2 com P-K6 e sem instrução ativa antiga ✓ · estado: 1 sem + 1 impedimento ⇒ rev.1 **não encerra**.
- **Resposta à pergunta do operador:** regras de materialização do Mestre **não** precisam da v3.1 (alvo = N2); a **assinatura do documento** sim — ele assinou citação de fato sobre arquivo não recebido. **Enviar v3.1** na rev.2.
- **Minuta rev.2:** §4.3 → P-K6 travado (`inverte` não materializa; info no claim; caminho `condicao_modificadora` = ciclo v1.5). Com essa troca, Estrutura declarou que subscreve inteira.
- **Confissão C92-2:** trilha 92 checou cobertura textual da minuta, não validade schema do §4.3 — método corrigido (simulação de schema obrigatória para regra de materialização nova).
- **Entrega:** `ENTREGAS/2026-09-24_ANALISE_SUBSCRICOES_REV2/` — análise + rev.2 + 2 respostas + v3.1 + COLA + trilha 93 + zip (re-extração 9/9).
- **Mesa:** operador manda o pacote às duas janelas · 2× subscrição sobre a **rev.2** · D1 aberta · 0 ciência.
- decisoes → **rev.89** · STATUS → bloco Rodada 82.

## ABERTURA 83 — 2026-09-24 (operação: rito — ressalva do §4.3 volta ao Comentador antes das janelas; resposta: P-K6 ratificado)

## RESULTADO 83 — 2026-09-24 (trilha 94: 10/10 · rev.2 FINAL com granularidade §6 · pacote pronto para as 2 janelas)

- **Supersede da mesa r82:** “mandar o pacote às duas janelas” **retirado** — o operador detectou que a ressalva do Estrutura tinha de passar pelo Comentador primeiro (rito dos 3). Correto. Ciclo: Estrutura → Arena → **Comentador** → (agora) janelas.
- **Carta arquivada:** `COMENTADOR_resposta_P-K6_2026-09-24/` sha `4783526ae58288dcd972963fb85a59eaa993abece42556808eb3816da365ca3c`. Veredito: **P-K6 preserva a Rota A**; sem novo ajuste conceitual; rev.2 segue aos dois auditores; **precisão §6: fail-closed por claim** (sem inverte → portões normais; com inverte → bloqueio; `.001b` = caso).
- **TRILHA 94 (10/10):** decisões §1–§10 verbatim · rev.2 incorporou granularidade · **resíduos da rev.1 removidos** (tabela “dois N2” → “não materializa”; P-K4 superada; pergunta P-K1..P-K6).
- **Minuta rev.2 FINAL sha:** `841532dad13cd3fea1356c9e23e37067e78876685db52d3c1f2cd8b2a96e535c` (11.205 b).
- **Pacote janelas atualizado** no mesmo diretório da análise: + carta P-K6 + rev.2 final + trilha 94 + COLA reescrita. Zip refeito (re-extração 12/12).
- **Mesa (corrigida):** operador manda **agora** a COLA + pacote às duas janelas · 2× subscrição sobre a rev.2 final · D1 aberta até lá · 0 ciência.
- decisoes → **rev.90** · STATUS → bloco Rodada 83.
- r83b: operador não achou as "respostas da rev.1" (nomes SUBSCRICAO_*). Renomeadas no pacote: `RESPOSTA_REV1_MESTRE_2026-09-24.md` + `RESPOSTA_REV1_ESTRUTURA_2026-09-24.md` (bytes/digitais idênticos). COLA e DIGITAIS atualizados; zip refeito.

## ABERTURA 84 — 2026-09-24 (chegam as 2 subscrições da rev.2: Estrutura sem ressalva; Mestre sem ressalva + retratação)

## RESULTADO 84 — 2026-09-24 (trilha 95: 12/12 · D1 ENCERRADA · ato de encerramento publicado)

- **Estrutura (texto arquivado):** “Subscrevo sem ressalva” — §4.3 íntegro, granularidade ok, v3.1 conferida, alcance registrado (vigente = derivação; `.001b` espera v1.5).
- **Mestre (`c01321ed…`, upload ≡ série):** “SUBSCREVO SEM RESSALVA” + **retratação** do erro da rev.1, reproduzido com Draft7Validator (4 casos).
- **TRILHA 95 (12/12):** digitais · 2× sem ressalva · rev.2 `841532da…` · allOf · v3.1 · P-K1..P-K6 · retratação · alcance. payload `D1: ENCERRAVEL`.
- **D1 ENCERRADA** pelo critério §19 do Comentador. Ato: `ENTREGAS/2026-09-24_ENCERRAMENTO_D1/` — encerramento + rev.2 + 2 assinaturas + resposta P-K6 + trilha 95 + zip (re-extração 8/8).
- **Vigente:** contrato de derivação Claim→N2 (dois eixos, sem default, fonte única, inverte travado P-K6). **0 alteração de schema.**
- **Mesa:** próximo = **piloto `.014`** (rito corrigido) · P-K1/P-K2 pré-condição do kit · P-K6 ciclo v1.5 · bytes ≥17/09 pendentes com o operador.
- decisoes → **rev.91** · STATUS → bloco Rodada 84 · **0 ciência**.
- Shas r84: encerramento md `5518912fe9af32eb09be667dd4ee40607ae458971b795f8ff781dae9929efb62` · zip `4871367517ab34f811de0d41e9b7de62445c09c74d3f5fd76e118c1d66c28de8` (re-extração 8/8) · estrutura rev2 `aa62e9a340b7fb02eab0ab2a3ee5e5fabe7d18c0d905ef70b535df30dbad3535`.

## ABERTURA 85 — 2026-09-24 (operador aprova: "Aprovo como vigente o Contrato de Saída do Claim Kit — rev.2, digital 841532da, de 24/09/2026.")

## RESULTADO 85 — 2026-09-24 (VIGÊNCIA oficializada · série + ponteiro + ato)

- **Digital conferida antes de selar:** minuta = `841532dad13cd3fea1356c9e23e37067e78876685db52d3c1f2cd8b2a96e535c` ≡ frase da aprovação.
- **Série:** `_documentos_serie/CONTRATO_SAIDA_CLAIMKIT_rev2_vigente_2026-09-24/` (contrato + encerramento).
- **Ponteiro:** `_documentos_serie/CONTRATO_SAIDA_CLAIMKIT_VIGENTE.txt` sha `6300495fd07231ed2e5ed485364716320df28004a91ae6765f5ccd1a6e2c8114` — frase verbatim, vigente × travado (P-K1..P-K6) × fora (v1.9/v1.10, piloto, bytes).
- **Entrega:** `ENTREGAS/2026-09-24_VIGENCIA_CONTRATO_SAIDA_CLAIMKIT/` — contrato + ponteiro + ATO_VIGENCIA + encerramento + zip (re-extração 5/5).
- **Escopo:** só o contrato de derivação Claim→N2. **Nada de schema alterado.** Continuidade declarada: kit P-K1/P-K2 → COMO EXECUTAR v1.10 → piloto `.014` → v1.5 (P-K6).
- decisoes → **rev.92** · STATUS → bloco Rodada 85 · **0 ciência**.

## ABERTURA 86 — 2026-09-25 (operador envia kit atualizado: Bloco v1.8 + Lista v1.5 datados 17/09 — pendência de bytes)

## RESULTADO 86 — 2026-09-25 (trilha 96: 14/14 · corpus 17/09 arquivado · bytes FECHADOS)

- **Série:** `KIT_CLINICA_ATUALIZADO_recebido_2026-09-25/` — 8 arquivos, uploads ≡ série.
- **Novos:** Bloco **v1.8** `7db41d40…` · Lista **v1.5** `20efa89f…` (ambos **2026-09-17**) · ESTRUTURA MESTRE **v2.2** `f6e54545…`.
- **Inalterados:** Schema-Claim v1.2 `56dc0e94…` ≡ 15/09 · COMO EXECUTAR v1.9 `1cd90b40…` ≡ 20/09 · IDS/ESCOPO/CANDIDATOS ≡ 15/09.
- **Medidas:** 27 claims (8+15+4 `em_busca`) · +6 novos (`.014 .015 .017 .023 .028 .032`) · 0 removidos · `.014` `aprovado_com_ressalva` pmids 39938607/34864233 · Lista 43 alvos (`.012b/c` entram) · bloco ⊆ lista · `usado_em` 23× `nao` · P-K1/P-K2 ausentes (ciclo pendente).
- **Pendência de bytes ENCERRADA.** Corpus vigente das medições clínicas: **17/09**. 15/09 → histórico.
- **Mantidas abertas:** E-4 piloto de processo (ter `.014` no Bloco ≠ rito cego ter rodado) · materialização travada por P-K1/P-K2 · v1.10 e piloto podem avançar com corpus fechado.
- **Entrega:** `ENTREGAS/2026-09-25_RECEPCAO_KIT_17_09/` zip (re-extração 4/4).
- decisoes → **rev.93** · STATUS → bloco Rodada 86 · **0 ciência**.

## ABERTURA 87 — 2026-09-25 (operador abre o CICLO DO KIT — P-K1/P-K2 pré-condição da 1ª materialização)

## RESULTADO 87 — 2026-09-25 (trilha 97: 13/13 · minuta Schema-Claim v1.3 escrita · COLA ao comentador pronta)

- **Minuta** `ENTREGAS/2026-09-25_CICLO_KIT_MINUTA_V13/MINUTA_SCHEMA_CLAIM_v1.3_2026-09-25.md`: só P-K1 (sentido_do_achado por fonte, enum literal v3.1) + P-K2 (ressalvas[] 3 tipos) + P-K3 (fonte única de condicao por escrito) + P-K5 (grau_maturidade_cientifica) + V-K1..V-K5 + migração sem retroatividade. Resto do v1.2 preservado.
- **TRILHA 97 (13/13):** baseline v1.2 `56dc0e94` intacta · contrato `841532da` como base normativa · enums conferidos contra v3.1 e N2 · proibições R-1 e P-K6 no kit · validadores declarados.
- **Rito:** COLA ao **Comentador primeiro** (após correção do operador na r82); depois auditores (Estrutura=schema · Mestre=fechamento) → operador aprova.
- **Entrega:** pacote com minuta + COLA + v1.2 + v3.1 + trilha 97 + zip.
- decisoes → **rev.94** · STATUS → bloco Rodada 87 · **0 ciência** · minuta **não vigente**.

## ABERTURA 88 — 2026-09-25 (comentador avalia minuta v1.3: P-K1..P-K5 aprovados; 1 ajuste V-K3; levar aos 2 auditores)

## RESULTADO 88 — 2026-09-25 (trilha 98: 10/10 · minuta rev.2 com V-K3 · COLAs territoriais prontas)

- **Carta arquivada:** `COMENTADOR_resposta_ciclo_kit_v13_2026-09-25/` sha `162423a5dd8e94de56973f9b0e79c6ff0ca67c1271a064114c71e428dc742508`.
- **Veredito:** minuta cobre P-K1..P-K5; baseline preservada; contrato não reaberto; N1/N2 intocados; **V-K3** = opção preferida (exploratórias só exigem `sentido_do_achado` se materializarem); proíbe importar eixos mecanísticos; não reabrir D1; após dupla avaliação → encerrar ciclo → v1.10.
- **Minuta rev.2** sha `bd9360e0aa8f59ce3308659684e17cfbb820f9daab133d18d09a57ecdad87101` — V-K3 + bloco exploratórias ajustados.
- **TRILHA 98 (10/10).**
- **COLA_V13_ESTRUTURA** e **COLA_V13_MESTRE** (perguntas territoriais do §12 da carta).
- **Mesa:** operador cola cada COLA na janela com os anexos · 2× subscrição sobre a rev.2 · ciclo do kit fecha · depois v1.10.
- decisoes → **rev.95** · STATUS → bloco Rodada 88 · **0 ciência** · minuta não vigente.
- r88b (operador): pacote renomeado com os nomes do workspace — `3º SCHEMA-CLAIM — v1.3 (MINUTA rev.2).md` (mesmo sha bd9360e0…), `3º SCHEMA-CLAIM — v1.2.md`, `3º SCHEMA-CLAIM — MECANISMO v3.1.md`. COLAs atualizadas. Novo zip (re-extração 12/12).

## ABERTURA 89 — 2026-09-25 (subscrições v1.3: Mestre sem ressalva; Estrutura com ressalva V-K6 — armadilha da saída)

## RESULTADO 89 — 2026-09-25 (trilha 99: 9/9 · minuta rev.3 com V-K6/V-K7 · ressalva cicla pelo Comentador)

- **Mestre** `124d9137…`: SUBSCREVO SEM RESSALVA (enums byte a byte; por-fonte; V-K3 ok).
- **Estrutura** `88289248…`: SUBSCREVO COM RESSALVA — sem V-K6, par `suporta_relacao`+`condicao_aplicacao` materializado ingenuamente gera `sustenta`+`condicao` e **N2 reprova** (D1 pela saída). + V-K7 fino (ausência ≠ null).
- **TRILHA 99 (9/9):** armadilha reproduzida (`sustenta`+cond viola; `condicional`+cond ok; `sustenta`+null ok).
- **Minuta rev.3** `28cbc9c76006f485f340da124aa1795833afa56d38e6572a9279d94a88f6b94c`: V-K6 precedência (condicao_aplicacao → condicional+condicao; sentido fica no claim) + V-K7; rev.2 preservada.
- **Rito:** ressalva da casa → **Comentador valida rev.3** → 2× janelas sobre a rev.3.
- **Entrega:** pacote atualizado (subscrições + rev.3 + RESPOSTA_CASA + COLA_CENTADOR + zip).
- decisoes → **rev.96** · STATUS → bloco Rodada 89 · **0 ciência** · N2 intocado.

## ABERTURA 90 — 2026-09-25 (comentador ACEITA rev.3: V-K6/V-K7 resolvem a ressalva do Estrutura; libera as duas janelas)

## RESULTADO 90 — 2026-09-25 (aceitação arquivada · COLAs rev.3 · pacote pronto)

- **Carta arquivada:** `COMENTADOR_ACEITA_REV3_VK6_2026-09-25.md` (série + pacote). Veredito: rev.3 aceita; V-K6 resolve a colisão da TRILHA99 sem escopo novo; V-K7 omitir campo vs null; **prossegir para as duas janelas**.
- **COLA_V13_ESTRUTURA** e **COLA_V13_MESTRE** atualizadas para **rev.3** (com registro da resolução da ressalva).
- **Mesa:** operador cola cada COLA na janela → 2× subscrição sobre a rev.3 → ciclo do kit encerra → v1.10.
- Zip refeito (re-extração 14/14). decisoes → **rev.97** · STATUS → bloco Rodada 90 · **0 ciência**.

## ABERTURA 91 — 2026-09-25 (subscrições rev.3: Estrutura e Mestre sem ressalva; episódio do arquivo rev.2 por engano registrado)

## RESULTADO 91 — 2026-09-25 (trilha 100: 10/10 · CICLO DO KIT ENCAVEL · vigência = frase do operador)

- **Estrutura (final):** “Subscrevo sem ressalva a minuta Schema-Claim v1.3 rev.3” — testou V-K6/V-K7 contra o N2; arquivo rev.2 detectado e não medido; rev.3 canônica confirmada. **Mestre:** “SUBSCREVO SEM RESSALVA” com sha `28cbc9c7…` declarado (`fa7edc88…`, upload ≡ série).
- **TRILHA 100 (10/10)** → `ciclo_kit = ENCAVEL`. Diff rev.2→rev.3 confinado a V-K6/V-K7; corpo P-K idêntico.
- **Nota de método (Estrutura):** 3× a mesma classe de erro (dois eixos colidindo: R7/D1/V-K6) só apareceu **reexecutável contra o artefato**.
- **Entrega:** `ENTREGAS/2026-09-25_FECHO_CICLO_KIT_V13/` — ato + rev.3 + 2 assinaturas + aceitação + trilha 100 + zip.
- **Mesa:** operador dá frase de vigência (padrão) → série + ponteiro → depois v1.10. Travas: P-K1/P-K2 antes da 1ª materialização · P-K6 v1.5 · E-4 piloto. **0 ciência.**
- decisoes → **rev.98** · STATUS → bloco Rodada 91.

## ABERTURA 92 — 2026-09-25 (operador aprova: "Aprovo como vigente o Schema-Claim v1.3 — rev.3, digital 28cbc9c7, de 25/09/2026.")

## RESULTADO 92 — 2026-09-25 (VIGÊNCIA do Schema-Claim v1.3 · série + ponteiro + ato)

- **Digital conferida antes de selar:** `28cbc9c76006f485f340da124aa1795833afa56d38e6572a9279d94a88f6b94c` ≡ frase.
- **Série:** `SCHEMA_CLAIM_v1.3_rev3_vigente_2026-09-25/` (schema + fecho).
- **Ponteiro:** `SCHEMA_CLAIM_V1_3_VIGENTE.txt` — frase, linhagem, P-K1..K5+V-K1..K7, travas (materialização/P-K6/E-4), não altera N1/N2/contrato.
- **Entrega:** `ENTREGAS/2026-09-25_VIGENCIA_SCHEMA_CLAIM_V13/` — ato + schema + ponteiro + fecho + zip (re-extração 5/5).
- **Próximo:** v1.10 (COMO EXECUTAR) com corpus 17/09 + contrato de saída vigente + schema v1.3 vigente. **0 ciência.**
- decisoes → **rev.99** · STATUS → bloco Rodada 92.

## ABERTURA 93 — 2026-09-25 (operador: "vamos abrir" — ciclo COMO EXECUTAR v1.10)

## RESULTADO 93 — 2026-09-25 (minuta v1.10 escrita · trilha 101: 12/12 · COLA ao comentador)

- **Minuta:** `ENTREGAS/2026-09-25_COMO_EXECUTAR_V110_MINUTA/4º COMO EXECUTAR — v1.10 (MINUTA).md` — 597 linhas · 33.265 b · sha `4951434417f24a329d41fc31f0ec13a5d6da5e1191edde1e72e6cbe2fee4038e`.
- **Método:** v1.9 (`1cd90b40`, intacta) como base + correções C-1..C-5 + 4 decisões do Contrato + X-1 + materialização separada + refs v1.3. Frases mortas da era v1.9 confirmadas 0× ("segunda inspeção sobre a análise da IA 1" · "emite parecer e redige o claim no schema").
- **TRILHA 101 (12/12):** 3 bases vigentes com digitais ✓ · C-1..C-5 ✓ · 4 decisões ✓ · portões §8 ✓.
- **Rito:** COLA ao Comentador primeiro → auditores → operador.
- **Entrega:** minuta + COLA + trilha 101 + zip. **0 ciência** · v1.9 não alterada · minuta não vigente.
- decisoes → **rev.100** · STATUS → bloco Rodada 93.

## ABERTURA 94 — 2026-09-25 (comentador libera v1.10 para as duas janelas territoriais)

## RESULTADO 94 — 2026-09-25 (liberação arquivada · COLAs territoriais prontas)

- **Carta:** `COMENTADOR_libera_v110_2026-09-25/` — v1.10 apta; P-K5 = refinamento não-bloqueio; sem reabrir D1 / N1/N2 / escopo.
- **COLA_V110_ESTRUTURA** (contrato §8, portões, 4 decisões × materializador) e **COLA_V110_MESTRE** (C-1..C-5, arbitragem, fechamento conjunto).
- **Mesa:** operador cola cada COLA na janela → 2× subscrição → ciclo v1.10 → palavra do operador. Zip refeito. **0 ciência.**
- decisoes → **rev.101** · STATUS → bloco Rodada 94.

## ABERTURA 95 — 2026-09-25 (subscrições v1.10: Estrutura e Mestre sem ressalva; notas não-bloqueantes E/M)

## RESULTADO 95 — 2026-09-25 (trilha 102: 8/8 · CICLO v1.10 ENCAVEL · vigência = frase do operador)

- **Estrutura:** sem ressalva; sha conferido; 4 pontos fecham; **nota** (não ressalva): passagem literal na mesa das três → portão L-05 quando escrito.
- **Mestre:** sem ressalva (`13b2939d…`); C-1..C-5/X-1/4 decisões linha a linha; **nota** (não ressalva): coerência dos 3 documentos.
- **TRILHA 102 (8/8)** → `ciclo_v110 = ENCAVEL`. Correção de régua T3 (prefixo sha 12) antes de publicar — C102-1.
- **Entrega:** `ENTREGAS/2026-09-25_FECHO_V110/` — ato + minuta + 2 assinaturas + liberação + trilha + zip.
- **Mesa:** frase do operador → série+ponteiro → **3 documentos vigentes** (contrato · schema v1.3 · COMO EXECUTAR v1.10) → piloto `.014` pode começar. **0 ciência.**
- decisoes → **rev.102** · STATUS → bloco Rodada 95.

## ABERTURA 96 — 2026-09-25 (operador aprova: "Aprovo como vigente o COMO EXECUTAR — v1.10, digital 49514344, de 25/09/2026.")

## RESULTADO 96 — 2026-09-25 (VIGÊNCIA do COMO EXECUTAR v1.10 · série + ponteiro + ato · TRÊS documentos vigentes)

- **Digital conferida:** `4951434417f24a329d41fc31f0ec13a5d6da5e1191edde1e72e6cbe2fee4038e` ≡ frase.
- **Série:** `COMO_EXECUTAR_v1.10_vigente_2026-09-25/` · **ponteiro:** `COMO_EXECUTAR_V110_VIGENTE.txt`.
- **Três vigentes do processo:** Contrato `841532da` · Schema-Claim v1.3 `28cbc9c7` · COMO EXECUTAR v1.10 `49514344`.
- **Entrega:** `ENTREGAS/2026-09-25_VIGENCIA_V110/` (ato + zip, re-extração 5/5).
- **Próximo marco:** **piloto `.014`** com desenho congelado (cegas → comparação → parecer → retorno → fechamento conjunto com as 4 decisões). **0 ciência.**
- decisoes → **rev.103** · STATUS → bloco Rodada 96.

## ABERTURA 97 — 2026-09-25 (comunicação: ensaio operacional pré-piloto .014 com o grupo da construção; depois tríade dedicada)

## RESULTADO 97 — 2026-09-25 (trilha 103: 10/10 · casa ACEITA o ensaio com 5 ressalvas S-1..S-5)

- **Comunicação arquivada:** `COMUNICACAO_ENSAIO_PRE_PILOTO_2026-09-25/` sha `d53d6ec9e35aca6992e4a916186f7006893c28e44ddf9375aeefedcc3c1e20b4`.
- **TRILHA 103 (10/10):** 3 bases citadas × digitais reais ✓ · ensaio ≠ piloto ✓ · bases intocadas ✓ · classificação operacional×normativa ✓ · sem ajuste silencioso ✓ · tríade dedicada cega ✓ · atribuição transitória ✓.
- **Posição da casa: ACEITA** — quem constrói testa a ferramenta; quem mede o método (piloto) é a tríade que não conhece o histórico.
- **Ressalvas (não bloqueiam):** S-1 ensaio não regrava estado do `.014` no Bloco · S-2 corpus do ensaio ≠ corpus congelado do piloto · S-3 E-4 só baixa com o piloto oficial · S-4 registro final vai para a série · S-5 no ensaio testa-se o mecanismo de janelas, não cegueira epistêmica.
- **Mesa:** casa participa como executor transitório; ao fim retorna a bancada. 3 bases intactas. **0 ciência.**
- decisoes → **rev.104** · STATUS → bloco Rodada 97.

## ABERTURA 98 — 2026-09-25 (pedido: errata oficial da Casa — complemento às comunicações do ensaio que não tinham S-1..S-5)

## RESULTADO 98 — 2026-09-25 (errata emitida · COLA única para os 2 auditores · histórico preservado)

- **Errata:** `ENTREGAS/2026-09-25_ERRATA_ENSAIO/ERRATA_CASA_ENSAIO_PRE_PILOTO_2026-09-25.md` — 10 pontos (ensaio≠piloto · .014 não regrava · corpus×2 · E-4 aberta · registro+digital · cegueira não testada · 3 bases · **Contrato normativo ≠ item do pacote mínimo de sessão** · sem silêncio · pacotes da tríade ao fim). Natureza: complemento; não apaga nem reabre.
- **COLA_ERRATA_AUDITORES** (mesmo texto, janelas separadas).
- **Série:** `ERRATA_CASA_ENSAIO_PRE_PILOTO_2026-09-25/`.
- **Mesa:** operador cola a COLA nos dois → 1ª rodada do ensaio. Zip (re-extração 6/6). **0 ciência** · bases intactas.
- decisoes → **rev.105** · STATUS → bloco Rodada 98.

## ABERTURA 99 — 2026-09-25 (operador abre NOVO chat do Auditor-Estrutura — projeto pesado/travando; pede carta de abertura no lugar da errata)

## RESULTADO 99 — 2026-09-25 (carta de abertura emitida)

- **Carta:** `ENTREGAS/2026-09-25_ABERTURA_CHAT_ESTRUTURA/ABERTURA_CHAT_ESTRUTURA_ENSAIO_2026-09-25.md` — identidade + 3 bases + ensaio≠piloto + teor da errata (8 itens) + estado Rodada 1 (E-01..E-03) + papel transitório + comandos de sessão. **Substitui a errata como mensagem inicial**; histórico preservado.
- Série: `ABERTURA_CHAT_ESTRUTURA_ENSAIO_2026-09-25/`.
- **Mesa:** operador cola a carta na 1ª mensagem do novo chat → ensaio segue. **0 ciência.**
- decisoes → **rev.106** · STATUS → bloco Rodada 99.
- r99b: versão MESTRE da carta de abertura (mesma estrutura; identidade/terrítório/papéis do Mestre). Pacote com as duas cartas.

## ABERTURA 100 — 2026-09-25 (pareceres do ensaio: IA1 FUNCIONOU · Estrutura recusa G3 + 3 achados · Mestre auditoria científica; operador pede fluxo em 2 rodadas)

## RESULTADO 100 — 2026-09-25 (instrução do ensaio escrita · papel do Estrutura definido · G1 reclassificado)

- **Pareceres arquivados:** `PARECERES_TESTE_ENSAIO_2026-09-25/` (IA1 `5948241a…` · Estrutura `0f68da60…` · Mestre `7ddf7a89…`).
- **Análise (linguagem simples):** só a IA1 respondeu “a ferramenta funciona”; Estrutura achou 3 achados e recusou G3 (correto); Mestre fez ciência (útil, outra pergunta). Operador acertou: testes não olharam o mesmo ponto.
- **Correção do operador sobre G1 (ACEITA):** lista na tela = G1 em execução; buscar PMID arquivo a arquivo **é** o G1, não defeito do pacote. **E-01 reclassificado** de “defeito” para “execução do G1”.
- **Fluxo do operador (2 rodadas):** filtro cego das 3 (G2) → comparação → lista acordada → G3 cego com texto → comparação → fechamento 4 decisões. **Confere com v1.10** (lotes).
- **Entregas:** `ENTREGAS/2026-09-25_INSTRUCAO_ENSAIO/` — INSTRUCAO_OPERACAO (linguagem simples, para colar nas 3 IAs) + RESPOSTA_ESTRUTURA (papel = observador+registrador; escolha do operador). Zip (re-extração 3/3).
- decisoes → **rev.107** · STATUS → bloco Rodada 100 · **0 ciência**.

## ABERTURA 101 — 2026-09-25 (comentador corrige papéis do ensaio: 4 participantes fixos; estrutura aceita papel de observador + 2 observações)

## RESULTADO 101 — 2026-09-25 (instrução rev.2 · contagem 107×92 registrada · limite do G1 reescrito)

- **Comentador:** fixar papéis — ChatGPT e Arena executam G1/G2/G3; Estrutura e Mestre percurso do território + parecer; 4 resultados = ensaio, não votos; piloto oficial inalterado. Pedido de ajuste antes da Rodada 1.
- **Estrutura:** aceita observador+registrador; 2 observações: (1) contagem 107 (casa) × 92 (anexo dele) — baseline única antes de congelar; (2) “lista na tela” ≠ G1 cumprido — resolução do PMID obrigatória.
- **Instrução rev.2:** papéis fixados (Mestre executa G1/G2/G3 no território de ciência/protocolo — coerente com o desenho de 3 filtros do operador; Estrutura não executa) · G1 reescrito (“põe ao alcance… só aí verified_reference”) · nota de contagem 107×92 · “4 não é voto”.
- **Contagem medida:** pool = **107** DOI únicos (3 réguas). 92 = anexo do Estrutura — reconciliar qual arquivo circulou antes do congelamento.
- **Entrega:** pacote com rev.2 + rev.1 + resposta estrutura. **0 ciência.**
- decisoes → **rev.108** · STATUS → bloco Rodada 101.

## ABERTURA 102 — 2026-09-25 (execução do Mestre no ensaio + pedido do operador: "quero sua rodada, sem viés")

## RESULTADO 102 — 2026-09-25 (execução da Arena · G1 ao vivo · achado G1-a · 4 decisões)

- **Mestre** arquivado (`e4c00afd…`): G1/G2/G3 ponta a ponta · ~80% fundo · 3 defeitos de lista · 0 normativo.
- **Arena executa** (`EXECUCAO_ENSAIO_014_ARENA_2026-09-25.md` sha `b482490b…`): G1 ao vivo 6 âncoras · G2 próprio (~14–17 materializam) · G3 com texto nas âncoras verificadas · resto marcado não-verificado.
- **Achado G1-a (factual):** Mestre citou PMID 25671328 (Setiawan 2015); PubMed e Bloco = **25629589** → divergência factual resolvida na fonte.
- Pacote `ENTREGAS/2026-09-25_INSTRUCAO_ENSAIO/` atualizado (zip novo). **0 ciência** · `.014` não muda.
- decisoes → **rev.109** · STATUS → bloco Rodada 102.

## ABERTURA 103 — 2026-09-25 (IA 1 entrega G1/G2/G3 completo — 3 execuções no mesa)

## RESULTADO 103 — 2026-09-25 (CRUZAMENTO dos filtros · 3 acordos factuais · 4 divergências factuais)

- **IA1** arquivado (`1bb5eccd…`): 9 PMIDs ✓ (inclui 25629589 e 23850810) · núcleo/síntese/fora · G3 por fonte · “Yrondi=protocolo”.
- **Cruzamento** (`CRUZAMENTO_FILTROS_014_2026-09-25.md`): **acordo dos 3** no veredito (suporta + heterogeneidade; status mantido) · acordos factuais (PMIDs certos, Hannestad=refuta, 80% fundo, HDAC6, Li×2) · **divergências → fonte:** D-a/D-b PMIDs errados na execução do Mestre · D-c “Yrondi protocolo” da IA1 parece errado (título é resultado — confirmar) · D-d contagem 107×92.
- **Estado:** ensaio responde “SIM com correções de pacote”; falta fechamento conjunto + S-4 consolidado.
- **0 ciência** · `.014` intacto. decisoes → **rev.110** · STATUS → bloco Rodada 103.

## ABERTURA 104 — 2026-09-25 (operador: sanear primeiro; contagem = mesma lista; e aponta que as 3 IAs fizeram G1-G2-G3 sem enviar no meio)

## RESULTADO 104 — 2026-09-25 (E-04 e E-05 registrados · instrução rev.2.1 com PARADAS obrigatórias)

- **E-04 (sequência):** as janelas correram até o fim sem entrega intermediária do G2. Causa: instrução sem ponto de parada explícito. Corrigido na **rev.2.1**: “ENTREGA E PÁRA” em cada etapa; operador comanda a passagem; quem avança sozinho = fora do rito.
- **E-05 (fecha D-d):** mesma lista a todas as IAs → **baseline 107** (parágrafo com DOI); 92 = regra de contagem do Estrutura → unificar a regra.
- **Sequência do operador:** sanear lista → fechamento → registro final. **0 ciência.**
- decisoes → **rev.111** · STATUS → bloco Rodada 104.

## ABERTURA 105 — 2026-09-25 (operador: fechar o ciclo do ensaio — pesou procurar os PMIDs; adia redirecionados e candidatos a ID)

## RESULTADO 105 — 2026-09-25 (REGISTRO FINAL do ensaio · fase ENCERRADA · S-4 consolidado)

- **Resposta final:** SIM — v1.10 executou ponta a ponta com correções de pacote/instrução; 0 normativo; 3 bases intactas.
- **Registro final:** `ENTREGAS/2026-09-25_FECHO_ENSAIO_014/REGISTRO_FINAL_ENSAIO_014_2026-09-25.md` — funcionou / travou (E-01..E-05, D-a..D-d) / congelar (8 condições) / **adiados** (redirecionados p/ outros mecanismos · candidatos a ID oficial) / retorno aos territórios.
- **Veredito comum das 3:** suporta + heterogeneidade · `.014` intacto.
- Zip (re-extração 6/6). **0 ciência.**
- decisoes → **rev.112** · STATUS → bloco Rodada 105.

## ABERTURA 106 — 2026-09-25 (operador: paradas do E-04 devem entrar no COMO EXECUTAR — ciclo v1.10 → v1.11)

## RESULTADO 106 — 2026-09-25 (minuta v1.11 · TRILHA105 8/8 · COLA ao comentador)

- **Minuta:** `ENTREGAS/2026-09-25_V110_PARADAS_MINUTA/4º COMO EXECUTAR — v1.11 (MINUTA).md` sha `ef27f8b3a492cd2f667b8892ec99603e57a5b22f46f5797e52705293d004fc66` — só: sequência com ENTREGA→PÁRA · comando do operador · fora do rito · nota E-04. Corpo idêntico ao v1.10 (TRILHA105).
- **Rito:** COLA ao Comentador → auditores → operador. v1.10 **vigente permanece** `49514344` até nova frase.
- **0 ciência.** decisoes → **rev.113** · STATUS → bloco Rodada 106.
- r106b: operador não achou a trilha (faltava o .py — só JSON). Script TRILHA105 gravado, reexecutado (8/8), copiado ao pacote; zip refeito (re-extração 5/5).

## ABERTURA 107 — 2026-09-25 (comentador aprova minuta v1.11; pede só reforço do T3 — ordem, não contagem)

## RESULTADO 107 — 2026-09-25 (T3 por ordem ENTREGA→PÁRA→COMANDO · 8/8 · COLAs aos 2 auditores)

- **Parecer do Comentador** arquivado (`f05870dd…`): v1.11 resolve E-04 com menor alteração; minuta apta às janelas; sem mudança na minuta.
- **T3 reescrito:** verifica posição de cada transição na sequência (5 marcas ordenadas), não só contagem. TRILHA105 **8/8** (script `8a2449d1…`, json `db29c335…`).
- **COLA_V111_ESTRUTURA** e **COLA_V111_MESTRE** emitidas.
- **Mesa:** operador cola cada COLA na janela → 2× subscrição sobre a rev.2 (v1.11) → frase do operador. v1.10 segue vigente. **0 ciência.**
- decisoes → **rev.114** · STATUS → bloco Rodada 107.

## ABERTURA 108 — 2026-09-25 (subscrições v1.11: Estrutura e Mestre sem ressalva)

## RESULTADO 108 — 2026-09-25 (trilha 106: 7/7 · CICLO v1.11 ENCAVEL · vigência = frase do operador)

- **Estrutura** (verbatim arquivado): diff próprio T6 byte a byte · “mudam quando se avança, não o que se decide” · **sem ressalva**.
- **Mestre** (`aeeaf905…`): 10 elementos do protocolo · comando = cadeado da cegueira · E-04 = defeito dele, solução bate · **sem ressalva**.
- **TRILHA106 7/7** → `ENCAVEL`. sha minuta `ef27f8b3…`.
- **Entrega:** `ENTREGAS/2026-09-25_FECHO_V111/` (ato + minuta + 2 assinaturas + parecer comentador + trilha + zip).
- **Mesa:** frase do operador → v1.11 vigente (substitui v1.10 `49514344`). **0 ciência.**
- decisoes → **rev.115** · STATUS → bloco Rodada 108.

## ABERTURA 109 — 2026-09-25 (comentador: formulação consolidada — 2 paradas de rodada; G1+G2 contínuos; níveis de leitura no G3)

## RESULTADO 109 — 2026-09-25 (rev.2 emitida · TRILHA107 10/10 · COLA de RECONFIRMAÇÃO aos 2 auditores)

- **Avaliação da casa:** formulação fecha o E-04 (paradas entre rodadas) e é mais próxima do desenho de 2 rodadas do operador. Aceita.
- **Minuta v1.11 rev.2** sha `2efc0edd9ba8fdf312cae23aceafc840b9ec3f8a2bc5e9ed147fe2f5bb2f9a2c` — só o bloco de sequência/paradas muda; corpo = v1.10 (T7). Acrescenta LISTA G1/G2/G2-CONGELADA · níveis `texto_completo|abstract|nao_lido` · regra verbatim do Comentador.
- **Timing honesto:** auditores assinaram a rev.1 (micro-paradas `ef27f8b3`); documento mudou → **assinaturas não cobrem a rev.2** → COLA única de reconfirmação.
- TRILHA107 **10/10** (inclui T10: rev.2 ≠ rev.1). **0 ciência.** decisoes → **rev.116** · STATUS → bloco Rodada 109.

## ABERTURA 110 — 2026-09-25 (reconfirmações da rev.2: Estrutura e Mestre sem ressalva; achado do T7)

## RESULTADO 110 — 2026-09-25 (TRILHA108 7/7 · ENCAVEL · T7 refeito com total real)

- **Estrutura** (`e1961e79…`): sem ressalva · diff próprio ✓ · achado operacional T7 (exibir comprimento real).
- **Mestre** (`d7610d32…`): sem ressalva · reauditei o delta (não estendi rev.1) · rev.2 **melhor** que rev.1 · destaque `nao_lido ≠ analisado`.
- **Resposta honesta ao achado:** 27.667 **era** o corpo da rev.2 (igualdade de corpos **é** o teste); o que faltava era exibir **total 34.004 + divergentes 0** — agora publicados (TRILHA108 T5).
- **Entrega:** `ENTREGAS/2026-09-25_FECHO_V111_REV2/` — ato + rev.2 + 2 reconfirmações + trilha + zip (6/6).
- **Mesa:** frase do operador → rev.2 vigente (substitui v1.10). **0 ciência.**
- decisoes → **rev.117** · STATUS → bloco Rodada 110.

## ABERTURA 111 — 2026-09-26 (vigência v1.11 rev.2 selada · operador envia roteiro atualizado 26.09.26 · pede análise + carta aos auditores)

## RESULTADO 111 — 2026-09-26 (vigência v1.11 · trilha 109: 7/8 · carta aos auditores com S-1..S-3)

- **VIGÊNCIA:** `COMO EXECUTAR v1.11 rev.2` `2efc0edd…` selado (ato `205c0cc5…`); v1.10 → histórico. Três vigentes: `841532da` · `28cbc9c7` · `2efc0edd`.
- **Roteiro novo** arquivado: `ROTEIRO_atualizado_recebido_2026-09-26/` sha `454b0c4c…`.
- **TRILHA 109 (7/8):** 15/15 intenções do operador presentes · bases coerentes · **S-1** roteiro ainda cita v1.10 (4+×) · **S-2** ensaio “A INICIAR” (real: encerrado r105) · **S-3** regra das 3 IAs para documentos **ausente**.
- **Carta aos auditores:** `ENTREGAS/2026-09-26_ANALISE_ROTEIRO/` — pede concordância com roteiro + S-1..S-3; depois: aplicar, publicar na plataforma (substitui `5e3f9163`), registrar digital.
- **0 ciência.** decisoes → **rev.118** · STATUS → bloco Rodada 111.

## ABERTURA 112 — 2026-09-26 (operador: comentador reescreveu o roteiro (27.09) para poupar créditos dos auditores; pede análise da casa antes das janelas)

## RESULTADO 112 — 2026-09-26 (TRILHA110: 18/18 · S-1..S-3 RESOLVIDOS · carta final pronta)

- **Arquivo:** `ROTEIRO DE TRABALHO DA PLATAFORMA - 27.09.2026.md` sha `2c286ca17b582a5fcad425d55b6a8f4ca7fd77cb1e95e23f6280fd58aa8357ce`.
- **TRILHA 110 (18/18):** S-1 v1.11 rev.2 vigente com SHAs ✓ · S-2 ensaio encerrado ✓ · S-3 §6.1 regra das 3 IAs (EXISTENTE≠VALIDADO≠VIGENTE) + anamnese validada ✓ · protocolo 2 paradas + nao_lido ✓ · digitais bases conferem · intenções preservadas.
- **Carta final** `CARTA_FINAL_ROTEIRO_2709_AUDITORES_2026-09-26.md` pronta para as 2 janelas (1 rodada, pedido único).
- **0 ciência.** decisoes → **rev.119** · STATUS → bloco Rodada 112.

## ABERTURA 113 — 2026-09-26 (operador pede organização do uploads: Atuais/ e Antigos/ × 5 categorias)

## RESULTADO 113 — 2026-09-26 (uploads organizado · 49 atuais + 37 antigos · 0 soltos)

- **Estrutura:** `uploads/{Atuais,Antigos}/{Schemas,Resolução,Parecer,Relatorio,Documentos}` + `INDEX_DA_PASTA.md`.
- **Antigos:** schemas v1/v1.2/propostas L05 · L-06 antigas · 4 subscrições superadas · triagem 16/09 · COMO EXECUTAR v1.7/v1.9 · Lista v1.3 · Bloco v1.6 + duplicata v1.8 · roteiros/arquiteturas antigas · dups.
- **Atuais:** kit vigente (Escopo · Lista v1.5 · Bloco v1.8 · IDS) · L-06 rev6 · roteiro 27.09 · subscrições vigentes · registros únicos (pareceres, relatórios) · pool `.014`.
- **0 arquivos soltos na raiz.** Atuais/Schemas vazio (vigentes na série). **0 ciência.**
- decisoes → **rev.120** · STATUS → bloco Rodada 113.

## ABERTURA 114 — 2026-09-26 (concordâncias dos 2 auditores ao roteiro 27.09: 2× sem ressalva)

## RESULTADO 114 — 2026-09-26 (ROTEIRO DA PLATAFORMA PUBLICADO · sha 2c286ca1)

- **Estrutura:** concorda — digitais, ensaio×piloto, §6.1 no texto; sem ressalva.
- **Mestre:** SIM CONCORDO — leu o arquivo real; nota (não ressalva): §6.1 é **prospectivo**, não reabre bases já fechadas por rito (leitura confirmada pela casa: correta).
- **Publicado:** série `ROTEIRO_plataforma_vigente_2026-09-27/` + ponteiro `ROTEIRO_VIGENTE` no índice do diretório; cópia operacional em `uploads/Atuais/Documentos/`. Substitui roteiros antigos (já em Antigos).
- **TRILHA110 18/18** · concordâncias arquivadas (`5be66fb0…` Mestre · estrutura verbatim).
- **Próximo passo do roteiro (§19):** VALIDAÇÃO DOS DOCUMENTOS E FERRAMENTAS (anamnese + instrumentos do piloto) → vigência → pacotes finais → PILOTO OFICIAL .014. **0 ciência.**
- decisoes → **rev.121** · STATUS → bloco Rodada 114.

## ABERTURA 115 — 2026-09-26 (operador: roteiro deveria ficar em lugar principal · Arquitetura é V2.3, não V2.2 · checklist aponta outra sequência)

## RESULTADO 115 — 2026-09-26 (errata do roteiro aplicada · local principal = raiz · sha 5f8b89dc)

- **Local:** roteiro movido para a **raiz do workspace** `/home/user/ROTEIRO DE TRABALHO DA PLATAFORMA.md` (cópia em uploads/Atuais + série errata).
- **Errata (10 linhas de diff contra `2c286ca1`):** V2.2 → **V2.3** (checklist 1 + §19; vigente = `ARQUITETURA_VIGENTE.txt` 19/09) · **nota de sequência** (checklist = inventário; ordem = §19: 28–29 → vigência → pacotes → 11) · cabeçalho de errata com sha original concordado.
- **Ninguém dos auditores pegou o V2.2** (fato do operador — R-CITA). Errata factual/editorial; estrutura = a concordada. Sha novo `5f8b89dc524adecb3a4046740ff469970996827aae8861e3fdbbdd14d717435d` (36.237 b, CRLF preservado).
- **Pendência de cortesia:** avisar os 2 auditores da errata (1 parágrafo cada, opcional — estrutura não mudou).
- **0 ciência.** decisoes → **rev.122** · STATUS → bloco Rodada 115.
- r115b: limpeza — plataforma com ÚNICO roteiro na raiz (`5f8b89dc…`); cópia de uploads/Atuais removida; antigos em Antigos; série mantida como arquivo com shas.

## ABERTURA 116 — 2026-09-26 (operador: vamos seguir o pacote piloto)

## RESULTADO 116 — 2026-09-26 (corpus CONGELADO + pacote da tríade dedicada)

- **Saneamento aplicado** (8 condições do ensaio): nomes corrigidos (De Picker L.D. · Kim J.-H. · Liu H.) · HDAC6 `[FORA_LOTE_TSPO]` · Yrondi `[RESULTADO_CONFIRMADO]` · Li2018_A/B distintos · fundo marcado · contagem = parágrafo-DOI (**107**) · data da busca 25/09 · G1 âncoras com PMIDs no cabeçalho.
- **Corpus congelado:** `ENTREGAS/2026-09-26_PILOTO_014/CORPUS_CONGELADO_PILOTO_B1SM02014_2026-09-26.md` sha `20c7159b5e8b30bad19b08617e387dd99a0364bc07f9e41088e4c5c0ce974b0d` (38.448 b).
- **Entrega tríade:** `ENTREGA_TRIDE_…` (regras, 2 paradas, papéis dedicados) + `COLA_PARA_JANELA_DEDICADA_…` (operador cola em cada janela; corpus idêntico, sem cruzamento).
- **Estado:** `.014` = `aprovado_com_ressalva` — piloto não regrava · protocolo v1.11 rev.2 · 0 ciência.
- decisoes → **rev.123** · STATUS → bloco Rodada 116.

## RESULTADO 117 — 2026-09-26 (pacotes para chats novos dos auditores — economia de créditos)

- `ENTREGAS/2026-09-26_PACOTES_CHAT_NOVOS/PACOTES_CHAT_NOVOS_PILOTO_2026-09-26.md` — listas de arquivos + prompts de abertura prontos (Estrutura · Mestre) para a etapa do piloto. 0 ciência. decisoes → rev.124.
- r118: reforço no ENTREGA_TRIDE — sequência em 1 linha (fecha “escolher o melhor G3”: confronto + fonte primária + fechamento conjunto; auditoria de M/E vem DEPOIS). zip refeito (5/5).
- r119 final: PACOTES_CHAT_NOVOS corrigido (auditam o RESULTADO/G3, não o G2) sha `b2868853e7c2d0aedde4b5be572cea3dba887dfa05e9fed2b1ac165cea185791`; confirmação: 2× "auditar o RESULTADO"; ordem: cruzamento G2 = tríade; auditores entram DEPOIS do resultado.

---

## 2026-09-29 — DECISÕES DO OPERADOR (registradas via Arena · sem rodada de casa)

- **1. A Anamnese não bloqueia o piloto oficial.** A validação documental da Anamnese (item 28 do Roteiro) pertence ao **teste integrado** e à frente do **contrato do Motor**; o piloto `.014` segue com o corpus congelado e as bases vigentes. Roteiro intocado. Artefato: `BIBLIOTECAS/_documentos_serie/DECISAO_OPERADOR_ANAMNESE_NAO_BLOQUEIA_PILOTO_2026-09-29.md`.
- **2. Errata de etiqueta no COMO EXECUTAR v1.11 rev.2.** Linha 1: "(MINUTA rev.2 — não vigente)" → "v1.11 rev.2 — VIGENTE" + nota de errata datada no próprio arquivo. **0 mudança de conteúdo.** Texto aprovado em 25/09 preservado byte a byte (`2efc0edd`, 35.223 b) em `COMO_EXECUTAR_v1.11rev2_ASSINADA_2efc0edd_2026-09-29.bak` (nome sem acentos, para exibir corretamente nas telas; renomeado no mesmo dia — era `.bak_pre_errata_etiqueta_2026-09-29`). Digital final do arquivo vigente: `1ea6d3547ff5acbc5160c0a5ff4e2fd704611846482caeeaaecdccc6ec7a7033` (36.254 b · 651 linhas). Bilhete `COMO_EXECUTAR_V111_VIGENTE.txt` atualizado com as duas digitais.
- **5. Pacote de envio das atualizações (29/09) + atalhos de download na raiz.** `ENTREGAS/2026-09-29_ATUALIZACOES/` + zip — reúne, com nomes sem acento e digitais, tudo o que mudou hoje para envio a terceiros (auditores/tríade). Na **raiz do projeto**, criados para facilitar o download do operador: `BAIXAR_AGORA_MANUAL-ATUALIZADO-29-09.zip` (só o manual, 651 linhas, 14 KB) · `BAIXAR_TUDO_ATUALIZACOES-29-09.zip` (os 9 arquivos do dia) · `MANUAL_COMO-EXECUTAR_v1.11rev2_ATUALIZADO-29-09.md` (o manual fora do zip) · `LEIA_EM-30-SEGUNDOS.txt` (mapa curto: qual dos 3 "COMO EXECUTAR" é qual). Cópias **bit a bit** conferidas (`1ea6d354`). Os atalhos criados na raiz foram **removidos no mesmo dia a pedido do operador** (não baixavam e geravam confusão na interface); em substituição, foi aberta uma **página local de download** (serviço temporário de trabalho, fora do repositório) com os arquivos do dia. Artefatos de trabalho do operador; **0 ciência**.
- **3. Plataforma × esboço — as ferramentas de conteúdo são descartáveis ao fim da construção.** Registro do operador: a plataforma funcionará com **Motor Clínico** (não com IA); a estrutura atual é **andaime** para a construção dos conteúdos; o **repositório oficial** virá depois e também passará por auditoria; **descartável ≠ lixo**. Contexto registrado: Auditor-Mestre, Auditor-Estrutura, Arena-Casa e Comentador seguem ajudando a construir o projeto. Artefato: `BIBLIOTECAS/_documentos_serie/DECISAO_OPERADOR_PLATAFORMA_X_ESBOCO_FERRAMENTAS_DESCARTAVEIS_2026-09-29.md`. Não altera vigências, não suspende o §6.1, não autoriza descarte agora.
- **4. Crivo documental dos 4 livretos do kit — iniciado.** Livreto 1 de 4 (`1º IDS_OFICIAIS.md`): pacote para as três IAs em `ENTREGAS/2026-09-29_CRIVO_LIVRETOS/`. Ponto de atenção medido e **esclarecido** no mesmo dia: a digital da proveniência do derivado (`f3a74fbc`, 17/09) é a **mesma matéria** com quebras de linha CRLF; o arquivo atual está em LF (normalização do backup do workspace) — conteúdo idêntico, derivado confere. **Nenhum impedimento à vigência.**
- **6. Regra operacional do operador (29/09) — publicação no GitHub.** Toda atualização do repositório no GitHub **só será feita por ordem expressa do operador**, e **cada publicação deve vir acompanhada de link da pasta do dia + caminho de download**. Publicações não pedidas não acontecem. *(Registrado localmente pelo Arena; entra no GitHub junto da próxima publicação ordenada.)*
- **7. Errata de etiqueta no Schema-Claim v1.3 e no Contrato de Saída rev.2 (29/09).** Os dois documentos vigentes declaravam internamente "MINUTA / não vigente", contradizendo o rito e o §18/§19 do Roteiro. Corrigido **dentro dos próprios documentos** (princípio: o documento se declara sozinho). Schema `28cbc9c7` → `e9f9e5d8…` (10.304 b · 204 l). Contrato `841532da` → `03cdd19a…` (12.950 b · 232 l — inclui o rodapé). **0 mudança de conteúdo.**
- **8. Pendências declaradas no item 7 — TODAS resolvidas no mesmo dia (29/09):** (a) §18 do Roteiro com digitais velhas; (b) bilhete do Roteiro desatualizado (sha pré-errata + cópia inexistente em `uploads/`); (c) bilhete do v1.10 usando o nome "VIGENTE" para versão histórica; (d) L-06 sem declarar o próprio estado no interior.
- **9. Resolução das pendências — princípio firmado pelo operador: O DOCUMENTO SE DECLARA SOZINHO** (o bilhete é apoio, não substituto). (a) §18 do Roteiro: cada base passa a registrar **duas digitais** (texto assinado em `.bak` + arquivo vigente); Roteiro → `507eaefa…` (37.919 b · 1.171 l · CRLF); as duas cópias da série tiveram as **quebras de linha restauradas** para CRLF (`5f8b89dc…` 36.237 b · `2c286ca1…` 35.438 b) — cada uma reproduz a digital declarada. (b) Bilhete do Roteiro reescrito (raiz do projeto como principal; linha falsa de `uploads/` removida). (c) Bilhete do v1.10 → **HISTÓRICO (NÃO VIGENTE)**; nome mantido como legado, razão declarada dentro. (d) L-06 declara o próprio estado no título e em nota datada → `acd76b24…` (27.523 b · 315 l); texto aprovado `98e90bdc…` preservado em `.bak`.
  **CONFERÊNCIA FINAL DE DIGITAIS (medida, não declarada): 5/5 vigentes · 6/6 cópias assinadas · ZERO divergências.**
- **10. Rito de aprovação — mantido; esclarecido a pedido do operador (29/09).** A frase de aprovação continua sendo o ato de fechamento: só existe quando o operador a diz, **letra a letra + data** (R-CITA-1), e anda sobre a unanimidade sem ressalva. A autodeclaração **não substitui o rito**: o rito é o **ato**; a autodeclaração é o **estado** (o documento carrega o próprio rótulo e viaja sem acompanhante). Nenhuma etiqueta criou aprovação. **Sem cerimônia nova — o filtro fica.**
- **11. Sistema da "prateleira" (29/09).** Trabalha-se o dia; ao fim do dia — **hora decidida pelo operador** — **sobe tudo de uma vez** por ordem expressa; gaveta datada por dia (`ENTREGAS/<data>/`); o último acontecimento é atualizado **com data** no CHANGELOG e no cartão `ONDE_PARAMOS.md`. **Publicação de 29/09: pendente nesta mesma rodada** (a oficina de 29/09 perdeu o acesso ao GitHub ao ser integrada a junção anterior; o transporte por link temporário falhou). **Conclusão registrada:** a oficina nova publica a rodada final a partir do GitHub + desta carta, sem arquivo de transporte.
- **0 ciência.** Nenhum conteúdo científico foi analisado, produzido ou alterado.

---

## 2026-09-30 — LOTE PUBLICADO · PRÓXIMO TRABALHO · CRIVO DOS LIVRETOS 2–4 (registrado via Arena · sem rodada de casa)

- **1. Lote de chats novos do piloto — PUBLICADO.** `ENTREGAS/2026-09-30_PACOTES_CHAT_NOVOS/PACOTES_CHAT_NOVOS_PILOTO_2026-09-30.md` (181 linhas · 10.162 bytes) — digital `204e244bbec2dd9f3ffd01c8bac106e035389ce0fd71a06936d88d2d3db28697`, conferida no disco e **re-medida no `main`** após o merge (PR nº 3; `main` em `1b4e971`). O documento foi reconstruído a partir de base64 (método Opção C); a primeira tentativa (cola de texto) não fechou a digital e foi abandonada. Três erros de transcrição do bloco foram corrigidos antes de a digital bater.
- **2. Próximo trabalho segundo o Roteiro (§19).** Ordem: validação dos documentos/ferramentas (itens 28–29) → vigência → pacotes finais → piloto oficial `.014` (item 11, que **depende** dos itens 28–29). O trabalho que destrava é o **crivo documental dos 4 livretos** (item 29).
- **3. Orientação do Comentador sobre o crivo (carta do operador, 30/09).** O crivo e o fechamento são feitos pelas **3 IAs**, documento por documento, antes de cada documento ser considerado vigente. **Auditor-Mestre** (governança, contratos, rito, processo, aderência normativa) e **Auditor-Estrutura** (estrutura, schemas, compatibilidade, materialização, coerência técnica) auditam cada um o seu território, **sem substituir** o crivo das IAs, em janelas próprias e **sem ciência** do parecer um do outro. Pacote **enxuto** (base comum indispensável + só o adicional necessário). Nível C (Anamnese, bibliotecas de conteúdo, ciência clínica) **fora** quando não for necessário. Pendências internas dos documentos entram como **pontos de verificação**, **não** como correções prévias. Antes de fechar cada pacote, conferir que o Roteiro incluído é o **vigente** — conferido: raiz `507eaefa…` = bilhete.
- **4. Pacote do Livreto 2 — Protocolo de Escopo B1 v1.3** (`943425cd…`). Pontos de verificação: V1 (cita Schema-Claim v1.2) · V2 (cita `CANDIDATOS_IDS_OFICIAIS.yaml`; o kit tem `.md`) · V3 (data interna 2026-08-04) · V4 (`.011` "quando aprovado" × estado atual; 3º item em `referencia_cruzada`) · V5 (8 atalhos permitidos × 10 no mapa). Medido: 14 IDs citados, 14 presentes no catálogo. Dependência: Livreto 1 sem veredito.
- **5. Pacote do Livreto 3 — Lista Canônica B1/SM-02 v1.5** (`20efa89f…`). Medido: 43 entradas (35 claims + 8 subclaims), 0 duplicados, 13 chaves de 1º nível sem repetição, 0 TAB, contadores batem; 8 IDs citados, 8 presentes; Lista × Bloco v1.8 sem divergência. Pontos L1–L7 (Schema v1.2 · `pendente` fora do enum do Schema · "aprovados" × `aprovado_com_ressalva` · referências ao Bloco v1.7 e à pendência P2 · Estrutura Mestre v2.2 desatualizada · `.011` com 3 IDs · nome/vigência/documento de nome parecido). Nota: o Schema-Claim v1.3 valida `claim_id` **exclusivamente** contra esta Lista.
- **6. Pacote do Livreto 4 — Bloco de Estado v1.8** (`7db41d40…`). Medido: 23 entradas aprovadas (15 + 8), 0 duplicados, `aprovado_com_ressalva` 15/15 com `nota_ressalva`, 92 entradas em `fontes_rejeitadas` sem repetição, 0 divergência de status contra a Lista. Pontos B1–B8 (Schema v1.2 · campo `forca_evidencia_afirmacao` fora do Schema v1.3 · campos do Schema v1.3 · pendências P1/P2/P4 abertas · referências a versões antigas · documento **mutável** — a vigência cobre só a digital · cópia na pasta `Antigos/` e arquivo externo ausente · "JSONS" × YAML).
- **7. Digitais dos pacotes** (`ENTREGAS/2026-09-30_CRIVO_LIVRETOS/DIGITAIS.txt`): Livreto 2 `2210e5b39d06ea70598bdfce67515d93f54903a2b355499567541477830a25a2` · Livreto 3 `c2aa46467e2c3a3e747d10fa658f69dd31f0dc9bbc3bfb580db100751b81d9a0` · Livreto 4 `21564747af18cd117f674f4c3b94c8104ab83c57df0c15bd27c48dff12c65a99`. Os documentos sob crivo **não foram alterados** (digitais re-medidas ao final).
- **8. Emenda 2 (bilhetes se declaram) — NÃO aplicada.** A carta listava 6 digitais-alvo; aplicada a receita em cópias, **1 de 6 bateu** (`COMO_EXECUTAR_V111_VIGENTE.txt`); as outras 5 (`SCHEMA_CLAIM_V1_3`, `CONTRATO_SAIDA_CLAIMKIT`, `ROTEIRO_PLATAFORMA`, `L06`, `COMO_EXECUTAR_V110`) não bateram. Aplicação **parada** conforme a carta ("se não bater, pare e reporte"); **nenhum bilhete alterado**; o commit `b2aaed6` citado na carta não existe nesta bancada. Sem ordem do operador para aplicar; o operador perguntou se poderia deixar de lado. Para retomar: texto exato dos 5 bilhetes (base64) ou as digitais deles antes da emenda.
- **9. Sessão do Arena encerrada.** O PR nº 3 foi integrado e o GitHub deixou de aceitar envios desta sessão. Os Livretos 2–4 ficam na pasta do dia, **não publicados** (`ONDE_PARAMOS.md` §7). Commits locais **não** sobrevivem entre turnos nesta bancada (o `.git` é recriado; um commit feito no meio da sessão sumiu) — **os arquivos ficam, o registro do git não**. O operador informou que **não consegue baixar o zip** pelo Arena. Publicação: sessão nova, **só por ordem expressa do operador**, com link da pasta + caminho de download.
- **Aguardando (24 h):** créditos dos Auditores Mestre e Estrutura e de uma das IAs do Grupo 2; o crivo dos livretos abre depois.
- **0 ciência.** Nenhum conteúdo científico foi analisado, produzido ou alterado.
