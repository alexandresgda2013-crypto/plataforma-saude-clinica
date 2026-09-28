# PROCESSO DE GERAÇÃO DE BIBLIOTECAS DE CONHECIMENTO
Pipeline de Produção — Mecanismos B1-B16
**Versão 2.1** — uso interno, não colar em nenhum chat com IA

## HISTÓRICO DE VERSÃO DESTE DOCUMENTO (auditoria da própria especificação)

**v2.0:** processo original de duas rodadas (GPM → Biblioteca), com dois checklists de conformidade estrutural e uma etapa nomeada "Auditoria científica de conteúdo (etapa a formalizar)" — reconhecida no próprio documento como pendência aberta.

**v2.0 → v2.1 (esta versão):** formaliza a etapa que estava pendente. Insere:
(a) **Bloco H** — Gate obrigatório e artefato-verificável entre Pré-Canônica e Canônica (antes inexistente; a auditoria científica não tinha portão de bloqueio real);
(b) **P-1** — ordem interna da Rodada 2 em três atos (busca por ferramenta → geração → declaração de rótulo Pré-Canônica);
(c) **P-2** — novo Portão de Auditoria Científica (G1→G2→G3) como etapa nomeada, sequenciada e com critérios de saída explícitos, substituindo a antiga "etapa a formalizar";
(d) **P-3** — nova Rodada 3 (Consolidação Canônica), com proibição dura de introduzir citação nova;
(e) **P-4** — Checklist de Fidelidade Canônica como gate de fechamento;
(f) **P-5** — validação por script como pré-requisito de infraestrutura (não mais opcional), com distinção entre falha de conteúdo e falha de infraestrutura;
(g) **P-6** — registro honesto do risco residual do avaliador único (não maquiado como resolvido);
(h) **P-7** — ciclo de vida das atualizações pós-publicação (`[AT]`), impedindo edição direta da Canônica vigente.

Esta versão é alinhada ao **Prompt 4.2** (antes 4.0/4.1) e ao **Checklist de Auditoria Estrutural v1.1**. Nenhuma frase da v2.0 foi removida; todas as inserções são aditivas e marcadas inline.

---

## VISÃO GERAL

```
Rodada 1: Molde GPM + Briefing(Bx)
↓
GPM_Bx.md
↓
[Checklist de Sanidade do GPM — mini-rodada]
↓
Rodada 2 (três atos — ver Bloco P-1): 
  Ato 1: Busca Sistemática por Ferramenta (PubMed eutils) 
       → corpus_pubmed.json + log_de_busca
  Ato 2: Prompt 4.2 + IDs oficiais + Filosofia (resumida) + 
       Lista Canônica de claims aprovados (Bx, se existir) + GPM_Bx.md 
       + corpus_pubmed.json
  Ato 3: declaração de rótulo
↓
Biblioteca_Bx_PRE_CANONICA.md  (audit_status: pending)
↓
[Checklist de Auditoria Estrutural v1.1 — mini-rodada — verifica FORMA]
↓
PORTÃO DE AUDITORIA CIENTÍFICA (G1→G2→G3) — sessão separada, verifica VERDADE
  G1 existência (ferramenta) → G2 elegibilidade → G3 suporte por vínculo
  G2 (elegibilidade — julgamento, com rascunho de espécie via MeSH/abstract):
  desenho/espécie/população/ano servem para o que a frase afirma? É da trilha
  certa? Há contaminação por desfecho de tratamento (BLOCO02-05, salvo
  06.7/09.6)? Resultado gravado no vínculo:
  g2_elegibilidade = eligible | redirecionado_clinico | redirecionado_mecanistico
                     | excluido_contaminacao | nao_avaliado; com g2_motivo.
  Redirecionado/excluído NÃO entra no G3 desta trilha (vai à fila da outra
  trilha; o trabalho não se apaga). G3 só roda em vínculo eligible.
↓
GATE OBRIGATÓRIO (Bloco H) — artefato-verificável, não é decisão de chat
↓
Rodada 3 — CONSOLIDAÇÃO CANÔNICA (proibido citação nova)
↓
[Checklist de Fidelidade Canônica — mini-rodada]
↓
Biblioteca_Bx_CANONICA.md (artefato permanente, versionado)
↓
Aprovação e integração ao sistema
```

Este processo se repete 16 vezes — uma por mecanismo — trocando apenas o Briefing na Rodada 1 e o arquivo GPM correspondente na Rodada 2.

---

## OS DOCUMENTOS E SEUS PAPÉIS

**0. Lista Canônica de claims aprovados** (única por mecanismo/submódulo, cresce entre sessões — quando existir)
Define o que já foi cientificamente validado claim a claim, via G1→G2→G3, antes de qualquer geração de Biblioteca começar. Quando existir para o mecanismo/submódulo em produção, é a fonte de maior prioridade do processo — acima do GPM. Não é obrigatória: mecanismos sem claims aprovados ainda seguem o processo normalmente, usando GPM + Prompt 4.2 sem essa camada extra.

**1. Molde GPM** (fixo, reutilizado 16 vezes)
Define como conduzir um levantamento científico exaustivo: metodologia de camadas, regra de escopo por doença, formato de citação, proibições, piso mínimo de fontes. É processo, não conteúdo — não sabe nada de específico sobre nenhum mecanismo.

**2. Briefing** (único por mecanismo, 16 no total)
Define o que deve ser investigado: nomenclatura específica, subfamílias moleculares, ângulos de busca, áreas adjacentes pouco exploradas, isoformas e subtipos relevantes daquele mecanismo em particular. Direciona a atenção do modelo para território que o molde genérico, sozinho, não visitaria.

**3. Prompt 4.2** *(ADENDO v2.1 — antes "Prompt 4.0", fixo, reutilizado 16 vezes)*
Define como redigir a Biblioteca **Pré-Canônica**: estrutura de blocos, rigor científico, hierarquia de evidência, política de fontes, formato de saída, JSON, rastreabilidade de Nível 1 e Nível 2. Autoridade final sobre qualidade e seleção de evidência — mas não sobre a verificação de existência/suporte de cada citação, que é papel do Portão G1→G2→G3.

**4. Checklists** (dois documentos fixos, reutilizados 16 vezes cada: Sanidade do GPM e Auditoria Estrutural v1.1)
Não geram conteúdo — verificam conformidade estrutural em mini-rodadas dedicadas, separadas das rodadas de geração, para evitar o viés de autoavaliação no mesmo turno em que o conteúdo foi produzido. **Nenhum dos dois checklists atesta veracidade científica** — isso é exclusivo do Portão G1→G2→G3 (ver C-1, no Checklist de Auditoria Estrutural v1.1).

**5. Portão de Auditoria Científica (G1→G2→G3)** *(ADENDO v2.1 — documento antes citado apenas como "etapa a formalizar", agora com processo próprio)*
Valida existência real do PMID (G1, por ferramenta), elegibilidade do desenho para a trilha mecanística (G2), e suporte de cada vínculo frase↔referência (G3). É o único estágio do processo que atesta veracidade — não forma. Roda em sessão separada de quem gerou a Pré-Canônica.

Nenhum documento duplica o papel do outro:
- O molde GPM não decide hierarquia de evidência (isso é do Prompt 4.2).
- O Prompt 4.2 não decide o que buscar dentro do mecanismo (isso é do Briefing).
- Os checklists não avaliam mérito científico — só estrutura e formato.
- A Lista Canônica não decide território de busca nem redação — isso é papel do Briefing/GPM e do Prompt 4.2, respectivamente. Ela só fornece achados já validados individualmente, que têm prioridade sobre os demais quando existir sobreposição.
- **O Portão G1→G2→G3 não redige nem decide estrutura — só atesta se o que já foi redigido é verdadeiro e suficiente** *(ADENDO v2.1)*.

---

## RODADA 1 — GERAÇÃO DO GPM DO MECANISMO

Preparação prévia obrigatória: o Briefing deve estar completamente escrito antes de iniciar. Sem Briefing, o GPM roda "vazio" — repete apenas conhecimento genérico, falhando no propósito central da ferramenta.

Barra de qualidade do Briefing: o Briefing B1 (Neuroinflamação) é a referência de profundidade mínima esperada para os 15 briefings restantes — cobrir, no mínimo: nomenclatura e famílias moleculares que exigem busca por nome específico, termos de busca alternativos usados pela literatura, áreas adjacentes frequentemente subexploradas, crosstalk prioritário com outros mecanismos, polimorfismos/genes a verificar especificamente, e sinalizadores de extrapolação a antecipar. Um Briefing abaixo dessa profundidade produz um GPM que converge para o conhecimento óbvio do mecanismo — exatamente o viés que o Briefing existe para evitar.

Sequência exata (mensagens separadas, nunca combinadas):

1. Colar somente o Molde GPM. Aguardar confirmação de entendimento da estrutura antes de prosseguir.
2. Colar somente o Briefing do mecanismo. A IA gera a Parte 1 (Módulos 00-05).
3. Pedir explicitamente: "Prossiga com a Parte 2 (Módulos 06-10), mantendo consistência com a Parte 1." A IA gera a Parte 2.
4. Unir as duas partes em um único arquivo GPM_Bx.md.

Saída: GPM_Bx.md — nomeado de forma simples e identificável.

Mini-rodada de verificação: aplicar o Checklist de Sanidade do GPM, colando-o junto com o GPM gerado e o Briefing original. Resultado: aprovado para Rodada 2, ou nova execução necessária.

Este documento não precisa de rastreabilidade rígida. É ferramenta de produção, descartável após aprovação da Biblioteca correspondente.

---

## RODADA 2 — GERAÇÃO DA BIBLIOTECA PRÉ-CANÔNICA

*(ADENDO v2.1 — título anterior: "RODADA 2 — GERAÇÃO DA BIBLIOTECA FINAL". Renomeado porque o produto desta rodada nunca é final — ver rótulo obrigatório no Prompt 4.2.)*

Recomenda-se iniciar um chat novo, evitando que o histórico da Rodada 1 permaneça no contexto e compita por atenção durante a redação da Biblioteca.

> **(ADENDO — BLOCO P-1, v2.1) Rodada 2 — ordem interna de execução (três atos, mesma conversa):**
>
> - **Ato 1 (descoberta por ferramenta):** o operador executa a BUSCA SISTEMÁTICA guiada pelo GPM_Bx+Briefing (ver Prompt 4.2, seção "BUSCA SISTEMÁTICA POR FERRAMENTA"): queries por categoria do GPM → PubMed eutils → salva `corpus_pubmed.json` + `log_de_busca`.
> - **Nota:** quando existir Lista Canônica para o mecanismo/submódulo ativo (Documento 5 da trilha mecanística), suas queries já formuladas por BLOCO são o ponto de partida deste Ato 1 (também chamado "etapa 2a" no Prompt 4.2) — compor query nova só para claim-alvo ainda sem query registrada lá.
> - **Ato 2 (geração):** a IA redige a Biblioteca PRÉ-CANÔNICA a partir do corpus + GPM + Briefing [+ Lista Canônica, se existir], e emite o Módulo 09 (registros de Nível 1 + vínculos de Nível 2) como CANDIDATOS — `pmid_oficial` em branco ou vindo do corpus da ferramenta, `status_auditoria` vazio.
> - **Ato 3 (declaração):** o artefato é rotulado "Pré-Canônica / `audit_status: pending`". Nada desta etapa é Canônico.
>
> **Proibição dura:** a IA não inventa PMID/DOI; a Busca (Ato 1) é feita por ferramenta, não por memória do modelo.

Sequência exata (mensagens separadas, nunca combinadas):

1. Executar o **Ato 1** acima (Busca Sistemática por Ferramenta) — gera `corpus_pubmed.json` + `log_de_busca`. *(ADENDO v2.1 — passo novo, antes inexistente)*
2. Colar somente o Prompt 4.2. Aguardar confirmação de entendimento da estrutura, blocos e regras.
3. Colar a Filosofia do Projeto (resumida) + o Contrato de Geração de Biblioteca de Mecanismo (extrato condensado das Decisões Arquiteturais, contendo apenas P12/P16/P17/P19/P20, R04/R06/R12 relevantes, e recorte de IDs oficiais para este mecanismo). Aguardar confirmação. Nunca carregar o documento completo de Decisões Arquiteturais (3000+ linhas) nesta rodada.
4. Se existir Lista Canônica de claims aprovados para este mecanismo ou submódulo, colar a Lista Canônica (ou o recorte de claims com status aprovado/aprovado_com_ressalva). Aguardar confirmação de leitura antes de prosseguir. Se não existir, pular esta etapa e seguir direto para o próximo passo.
5. Colar o GPM_Bx.md correspondente **e o `corpus_pubmed.json` gerado no passo 1**. A IA gera a Parte 1 (BLOCO_00-06).
6. Pedir explicitamente: "Prossiga com a Parte 2 (BLOCO_07 até o final), mantendo consistência com a Parte 1." A IA gera a Parte 2.
7. Unir as duas partes em um único arquivo **Biblioteca_Bx_PRE_CANONICA.md**.

Regra de bloqueio: se o GPM correspondente não for fornecido, o Prompt 4.2 deve interromper e sinalizar `[GPM AUSENTE]` — nunca gerar a Biblioteca sem ele como base. A Lista Canônica NÃO é bloqueante: quando fornecida, tem prioridade máxima como fonte (ver Hierarquia de Fontes Obrigatória no Prompt 4.2); quando ausente, a Biblioteca segue normalmente pela Política de Fontes padrão. **A ausência do corpus de busca por ferramenta também não é bloqueante — eleva o risco declarado da Pré-Canônica (ver Prompt 4.2, item 0.0a).** *(ADENDO v2.1)*

Saída: **Biblioteca_Bx_PRE_CANONICA.md** — artefato de trabalho, **não permanente ainda**, com rigor de rastreabilidade de Nível 1 e Nível 2.

Mini-rodada de verificação: aplicar o **Checklist de Auditoria Estrutural da Biblioteca v1.1**. Resultado: aprovado estruturalmente (libera o Portão de Auditoria Científica), ou requer correção estrutural.

Nota: a seção de "Padrões de Qualidade para Aprovação" foi removida do corpo do Prompt 4.2 e migrou integralmente para este checklist separado — o Prompt 4.2 não se autoavalia mais no mesmo turno em que gera a Biblioteca.

---

## PORTÃO DE AUDITORIA CIENTÍFICA (G1→G2→G3)

*(ADENDO — BLOCO P-2, v2.1 — substitui a etapa antes nomeada "Auditoria científica de conteúdo (etapa a formalizar)")*

Entre a Pré-Canônica aprovada estruturalmente e a Rodada 3, executar a auditoria científica em **sessão SEPARADA** (quem gera não audita):

- **G1 existência:** 100% das referências resolvidas via ferramenta (eutils) → `verified_reference`; ou marcadas `NAO_LOCALIZADO`/`CITACAO_INCORRETA`.
- **G2 elegibilidade:** desenho aceito segundo `tiers_forca_causal` + `tipos_modelo_aceitos` + `exclusion_criteria` do Protocolo de Escopo do mecanismo; sem contaminação por desfecho de tratamento em BLOCO02-05 (salvo 06.7/09.6); redirecionamento de associativo puro → trilha clínica; pré-clínico achado em busca humana → redirecionados.
- **G3 suporte:** por VÍNCULO (frase), abstract colado/lido (full-text quando o abstract não basta), respondendo nesta ordem:
  1. *Pertencimento* — a referência pertence de fato ao BLOCO/mecanismo onde foi citada, a outro BLOCO do mesmo mecanismo, a outro mecanismo B1-B16, ou ao domínio clínico (associação populacional sem manipulação causal)?
  2. *Suporte causal* — o `trecho_ancora` é sustentado pelo achado real da fonte, ou é inferência do avaliador além do que o desenho do estudo demonstra?
  3. *Robustez* — a evidência disponível sustenta o `uso` que a frase faz dela (`nucleo_causal` exige tier_1/tier_2 em fonte principal; do contrário, no máximo `suporte_correlacional`)?
  → `CONFIRMADO | PARCIALMENTE_CONFIRMADO | NAO_SUSTENTA_CLAIM`. Claims de **ALTO RISCO** (4 critérios do Bloco H, abaixo) recebem 2ª verificação independente.

*Todos os claims passam por G1→G2→G3 e pela re-validação de consolidação. Apenas a revisão cega por um segundo avaliador independente é, nesta fase, restrita aos claims de alto risco (4 critérios), com extensão a todos prevista para a fase com equipe.

**Saída:** `status_auditoria` preenchido por vínculo + `verification_status` por frase.

**Gate:** a Rodada 3 não inicia enquanto houver vínculo sem status.

> **Regras de vocabulário fechado herdadas do fluxo G1→G2→G3 (fonte: "Como Executar — [Mecanismo] Trilha Mecanística", documento instanciado por mecanismo, mesmo padrão do GPM+Briefing):**
> - Nenhum dos 4 eixos de evidência decide sozinho o G3 — a decisão é julgamento do avaliador sobre o conjunto das 3 perguntas de G3, nunca uma fórmula automática.
> - PMID puramente associativo/epidemiológico encontrado em busca mecanística nunca é rejeitado por essa razão isolada — vai para `redirecionados_modulo_clinico`.
> - GPM nunca é citado como fonte de PMID — o GPM aponta território, nunca substitui a verificação G1.

---

### GATE OBRIGATÓRIO ENTRE PRÉ-CANÔNICA E CANÔNICA

*(ADENDO — BLOCO H, v2.1 — inserido conforme indicado no adendo original: "não é opcional")*

Uma Biblioteca só avança para a Rodada 3 (Consolidação Canônica) quando, em **artefato verificável** (não em mensagem de chat):

1. 100% das referências do Módulo 09 passaram por G1 (existência via ferramenta) OU estão explicitamente `NAO_LOCALIZADO`/`PENDENTE`;
2. todo claim a ser usado na Canônica tem `status_auditoria` preenchido (`CONFIRMADO`/`PARCIALMENTE_CONFIRMADO`) por sessão de auditoria separada;
3. claims de **ALTO RISCO** tiveram 2ª verificação independente (cego ao 1º veredito; divergência arbitrada). Define-se ALTO RISCO por critério objetivo:
   - (a) nó central BLOCO_07 ou conexão BLOCO_08 de força biológica HIGH;
   - (b) `uso=clinico` (embasa narrativa ao profissional);
   - (c) evidência humana usada para afirmar causalidade;
   - (d) decisão de REJEITAR/remover uma citação.
4. rodou o Checklist de Fidelidade Canônica (toda frase tem claim verificado/ressalvado; nenhum trecho rejeitado residual; `verification_status` presente).

Enquanto isso não estiver em artefato, o artefato permanece **"Pré-Canônica"**.

---

### VALIDAÇÃO POR SCRIPT — PRÉ-REQUISITO DE INFRAESTRUTURA

*(ADENDO — BLOCO P-5, v2.1)*

A validação automatizada é **INFRAESTRUTURA OBRIGATÓRIA (gate)**, não um bônus de quem tem orquestrador. Nenhuma Pré-Canônica avança para a auditoria e nenhuma Canônica é gerada sem o script de validação rodar e passar:

**GATE-SCRIPT** (pré-requisito de infraestrutura), verifica por código:
1. 100% das referências do Módulo 09 tem G1 registrado (`verified_reference`) OU marcadas `NAO_LOCALIZADO`/`PENDENTE`;
2. 100% dos vínculos (Nível 2) tem `trecho_ancora` não vazio;
3. 100% das frases declarativas da Canônica tem `verification_status` preenchido (≠ pendente);
4. mão-dupla texto⇄registro: zero citação sem vínculo, zero registro/vínculo órfão (fora das adições prospectivas marcadas);
5. campo `"grade"` literal `A|B|C|D` AUSENTE em arquivo de mecanismo (deve ser `forca_evidencia_afirmacao`) — hard-fail;
6. claims de ALTO RISCO (4 critérios do Bloco H) tem 2ª verificação independente registrada.

Qualquer item falhado → o script aborta o avanço (`exit ≠ 0`). Não há "avançar mesmo assim": a validação é o portão, não um checklist manual opcional. **O LLM não tem permissão de escrever os campos de verificação** — esses campos são escritos pelo script/ferramenta (G1 via eutils) e pelo registro da sessão de auditoria, tornando a fraude tecnicamente bloqueada, não só desencorajada.

**Distinção OBRIGATÓRIA de tipo de falha (gate bem-formado):**
- **FALHA DE CONTEÚDO** (citação sem vínculo, grade literal em mecanismo, status vazio, trecho_ancora ausente) → gate REPROVA (`exit ≠ 0`), bloqueia o avanço e aponta o item.
- **FALHA DE INFRAESTRUTURA** (API PubMed indisponível/timeout, rede, rate-limit) → NÃO é reprova de conteúdo: o gate marca o estado como `BLOQUEADO_POR_INFRA` (retry com backoff; se persistir, registra `g1_pendente_infra` e NÃO marca o PMID como verificado nem como rejeitado — fica PENDENTE para retomada). Nunca se confunde "não consegui consultar" com "a citação é inválida".
- O gate só devolve APROVADO quando as checagens de CONTEÚDO passam; falha de infra impede o veredito (não o falsifica).


> **(ADENDO — reconciliação de vocabulário, ver MAPEAR_VOCABULARIO.md)**
> `verified_reference`, `target`, `eligible_source` e `approved_claim`
> (usados acima e no "Como Executar") são rótulos de FLUXO — descrevem
> o estágio do vínculo, não um valor a gravar em `status_auditoria`.
> O único vocabulário gravável no arquivo é o enum fechado do Prompt
> 4.2 (09.4): `CONFIRMADO | PARCIALMENTE_CONFIRMADO | NAO_LOCALIZADO |
> CITACAO_INCORRETA | NAO_SUSTENTA_CLAIM`, mais o estado inicial `""`.
> Da mesma forma, `PENDENTE` (item 1 do GATE-SCRIPT) e
> `BLOQUEADO_POR_INFRA`/`g1_pendente_infra` são estados de EXECUÇÃO do
> gate (log de rodada), não valores de `status_auditoria` — nunca
> escrever esses literais no schema de conteúdo. Tabela de tradução
> completa: `MAPEAR_VOCABULARIO.md`.

---

### RISCO RESIDUAL DO AVALIADOR ÚNICO — REGISTRO HONESTO

*(ADENDO — BLOCO P-6, v2.1)*

"Sessão separada (quem gera não audita)" impede contaminação de contexto, mas **NÃO é identidade distinta**: o mesmo operador humano pode, na sessão de auditoria, validar o próprio trabalho com menos ceticismo.

**Fase atual (1 operador):** mitigação aceita e declarada — exige-se sessão separada + log de busca auditável + critério objetivo de alto risco. **Risco residual conhecido: viés de confirmação do operador sobre o próprio material.** Este risco é registrado aqui como pendência de fase, **não como problema resolvido**.

**Evolução obrigatória quando houver equipe:** rotação real de revisor para os claims de alto risco (Bloco H) — pessoa/identidade diferente de quem gerou/conduziu a validação inicial, com registro de divergência e arbitragem. Alinhado ao padrão inter-avaliador (κ) já previsto para a fase de estruturação comercial do projeto.

---

## RODADA 3 — CONSOLIDAÇÃO CANÔNICA

*(ADENDO — BLOCO P-3, v2.1 — rodada nova, antes inexistente. É re-escrita, não descoberta.)*

**Entrada:** Pré-Canônica + resultado G1–G3 + log de reconciliação.

**REGRA DURA: PROIBIDO introduzir citação/achado novo.** Só se reescreve o que tem claim `APROVADO` ou `APROVADO_COM_RESSALVA`. Citação nova aqui = reprova.

Claims rejeitados → frase REMOVIDA/REBAIXADA/SUBSTITUÍDA conforme o log de reconciliação; ressalvas carregam marcação textual de maturidade (visível, não só no JSON).

Toda afirmação declarativa da Canônica tem `verification_status` por frase e propaga para NT_TEMPLATE e JSONs modulares (hard-fail como P12 — ver "NÍVEL DE VERIFICAÇÃO VISÍVEL" no Prompt 4.2).

**Saída:** `Biblioteca_Bx_CANONICA.md` (artefato permanente, versionado).

---

### CICLO DE VIDA DAS ATUALIZAÇÕES PÓS-PUBLICAÇÃO (`[AT]`)

*(ADENDO — BLOCO P-7, v2.1)*

Evidência publicada **DEPOIS** de uma Canônica NÃO entra por edição direta na Canônica vigente. Fluxo de atualização:

1. A nova literatura entra em `04_atualizacoes_literatura.json` (`[AT]`) e em vínculos NOVOS com `status_referencia: CANDIDATO` — NÃO toca a Canônica.
2. Reabre-se uma mini-rodada de auditoria (G1→G2→G3) SÓ para os vínculos `[AT]`.
3. Se aprovada: gera-se uma NOVA VERSÃO da Canônica ("versão N+1"); a Canônica anterior permanece como histórico versionado (não editada in place).

**Em resumo:** `[AT]` é um mini-ciclo Pré→auditoria→Canônica (nova versão), nunca uma inserção direta na Canônica aprovada.

---

## CHECKLIST DE EXECUÇÃO POR MECANISMO

*(ADENDO v2.1 — sequência renumerada e expandida a partir da v2.0 para refletir Pré-Canônica → Portão G1-G3 → Rodada 3 → Fidelidade)*

Para cada um dos 16 mecanismos, seguir nesta ordem:

1. Escrever o Briefing específico do mecanismo (usar o Briefing B1 — Neuroinflamação como padrão mínimo de profundidade)
2. Rodar Rodada 1 (Molde GPM → Briefing, mensagens separadas) → obter GPM_Bx.md
3. Aplicar Checklist de Sanidade do GPM (mini-rodada) → aprovado ou requer nova execução
4. Executar Ato 1 da Rodada 2 (Busca Sistemática por Ferramenta) → obter `corpus_pubmed.json` + `log_de_busca` *(ADENDO v2.1)*
5. Rodar Ato 2-3 da Rodada 2 (Prompt 4.2 → IDs+Filosofia → Lista Canônica, se existir, → GPM_Bx.md + corpus, mensagens separadas, chat novo) → obter Biblioteca_Bx_PRE_CANONICA.md
6. Aplicar Checklist de Auditoria Estrutural da Biblioteca v1.1 (mini-rodada) → aprovado estruturalmente ou requer correção
7. Rodar GATE-SCRIPT (validação por código) → passa ou aborta com item apontado *(ADENDO v2.1)*
8. Executar Portão de Auditoria Científica G1→G2→G3 em sessão separada, incluindo 2ª verificação independente nos claims de ALTO RISCO *(ADENDO v2.1)*
9. Confirmar Gate Obrigatório (Bloco H) satisfeito em artefato verificável *(ADENDO v2.1)*
10. Rodar Rodada 3 (Consolidação Canônica) → obter Biblioteca_Bx_CANONICA.md *(ADENDO v2.1)*
11. Aplicar Checklist de Fidelidade Canônica (mini-rodada) *(ADENDO v2.1)*
    - [ ] (I) toda frase declarativa tem claim APROVADO/RESSALVA;
    - [ ] (II) nenhum trecho de claim REJEITADO/PENDENTE permanece sem alteração;
    - [ ] (III) ressalva tem marcação de maturidade visível no texto;
    - [ ] (IV) log de reconciliação 100% aplicado;
    - [ ] (V) nenhuma citação nova entrou na Rodada 3 sem G1–G3.
12. Aprovação e integração da Biblioteca Canônica ao sistema
13. Marcar, na Lista Canônica correspondente, os claims incorporados com `usado_em_biblioteca: sim`
14. Arquivar Pré-Canônica e GPM como histórico — Canônica passa a ser a fonte ativa *(ADENDO v2.1)*
15. GPM_Bx.md e Biblioteca_Bx_PRE_CANONICA.md podem ser arquivados sem necessidade de manutenção futura

---

## O QUE NÃO MUDA ENTRE MECANISMOS

- Molde GPM (texto idêntico nos 16)
- Prompt 4.2 (texto idêntico nos 16) *(ADENDO v2.1 — antes "Prompt 4.0")*
- Checklist de Sanidade do GPM (texto idêntico nos 16)
- Checklist de Auditoria Estrutural da Biblioteca v1.1 (texto idêntico nos 16) *(ADENDO v2.1)*
- Filosofia do Projeto resumida (texto idêntico nos 16)
- Processo de rodadas, incluindo Portão G1→G3, Gate-Script e Rodada 3 (idêntico nos 16) *(ADENDO v2.1)*

## O QUE MUDA A CADA MECANISMO

- Briefing (conteúdo único, escrito antes da Rodada 1)
- Lista Canônica de claims aprovados (se existir — nem todo mecanismo terá, ao menos não nas fases iniciais do projeto)
- GPM gerado (resultado único da Rodada 1)
- `corpus_pubmed.json` e `log_de_busca` (resultado único do Ato 1 da Rodada 2) *(ADENDO v2.1)*
- Recorte de IDs oficiais relevantes (se optar por recorte em vez do JSON completo)
- Biblioteca_Bx_PRE_CANONICA.md gerada (resultado único do Ato 2-3 da Rodada 2)
- Resultado do Portão G1→G2→G3 (vínculos, `status_auditoria`, `verification_status`) *(ADENDO v2.1)*
- Biblioteca_Bx_CANONICA.md (resultado único da Rodada 3) *(ADENDO v2.1)*

---

Processo de Geração de Bibliotecas de Conhecimento — Clinical Dominion
**Versão do documento: 2.1** | Alinhado com Prompt 4.2 | Checklist de Auditoria Estrutural v1.1