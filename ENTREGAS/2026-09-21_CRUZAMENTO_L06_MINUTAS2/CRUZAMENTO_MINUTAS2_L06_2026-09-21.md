# CRUZAMENTO DAS MINUTAS 2 DA L-06 — verificação técnica da casa
**casa (agente Arena) · 2026-09-21 · Rodada 60 · trilha 73: 15/15 medidas verdes**

> ## SUA AÇÃO (operador)
> 1. Ler o **Resumo em 5 linhas** (fim do documento) — ali está a posição da casa, sem muro.
> 2. Encaminhar este documento aos **dois projetos** (Auditor-Mestre e comentador). Ele é o mapa para a consolidação.
> 3. A decisão final da L-06 é sua — quando a minuta consolidada chegar, aí você aprova.
>
> **Precisa de resposta?** Não para a casa. Mestre e comentador respondem com a minuta consolidada.

---

## Caixa de errata da casa (antes de tudo — quem corrige, corrige em cima)

1. **C73-1 — atribuição retirada:** na nota R59 a casa disse que o operador havia perguntado "dá para usar a regra por fora?". **Ele não perguntou.** A casa leu como pergunta dele um trecho de contexto colado. A medição feita continua válida como conteúdo verificado; a atribuição é retirada e fica datada na ata.
2. **C73-2 — enquadramento refinado:** a carta 22 declarou "a minuta do mestre será a base da consolidação, com 2 resgates da do comentador" **antes** deste cruzamento técnico existir. Isso antecipava uma decisão que pertence aos autores e ao operador. **Este relatório substitui aquele enquadramento**: aqui há vereditos item a item — e eles corrigem **as duas** minutas.
3. **Reclassificação:** a "anomalia de assinatura" no texto do comentador deixa de ser tratada como incidente de nome e vira **nota editorial** (o comentador é comentador, não produtor de documento — correção do operador, aceita). Ainda assim, o bloco não deve circular dentro dos projetos como se fosse "do mestre"; a consolidada resolve isso por autoria.

## Método (declarado)

Duas minutas lidas byte a byte (mestre `eb54337c…`, 12.837 b · comentador verbatim arquivado pela casa com nota de topo). 15 conferências codificadas (trilha 73, `comando = python3 TRILHA73_script_cruzamento_minutas2_L06_2026-09-21.py`, mesma régua de sempre: NFC, `open()` texto, casefold em prosa, matrizes executadas sobre os 274 vínculos reais com proxy declarado). Nada aceito "no raciocínio".

---

## A — Convergências técnicas (verificadas nas duas, não presumidas)

| # | Ponto | Onde | Veredito |
|---|-------|------|----------|
| A1 | Invariante **literal idêntica**: "O Motor não fabrica precedência científica onde a ciência não estabeleceu precedência" | M §invariante · C INVARIANTE | ✔ medida |
| A2 | **Não-descarte** ("nenhum degrau elimina relação"; implementação que descartar está em desacordo) | M §2 · C Parte 2 | ✔ medida |
| A3 | **Mesma escada de 7 perguntas**, mesma ordem normativa, mesmas saídas-base (`sem_conflito` → `conflito_nao_resolvido` + lacuna com os dois IDs) | M §2 · C Parte 2 | ✔ medida |
| A4 | Degraus **5 e 6 rotulam, não desempatam** | M §2 · C Parte 3 (seção dedicada) | ✔ medida |
| A5 | **Escada degradada** (degrau indisponível não resolve, não conta como testado; `multifatorial` barrado em escada com buraco) | M §3 · C Parte 4 | ✔ de propósito — **com divergência de extensão** (ver F2) |
| A6 | Determinismo: ordem lexicográfica, simetria, ordem normativa dos degraus, idempotência, sem estado entre pares | M §4 · C Parte 6 | ✔ medida |
| A7 | **Força, maturidade ou desenho não criam gatilho** (isso é D-02) | M §1/§7 · C Parte 1.3 | ✔ medida |
| A8 | Separação resolução × decisão clínica (**D-08**: não decide o que aparece no laudo) | M §7 · C Parte 9 | ✔ medida |
| A9 | Não criam campos, não criam fonte de conhecimento, não fazem pesquisa nova | M §7 · C Parte 9/estado | ✔ medida |
| A10 | **Fecho operacional**: resolver com estrutura; degradar com lacuna estrutural; preservar ambas + registrar lacuna quando irresolvido | M §2/§7 · C INVARIANTE/Partes 2–4 | ✔ medida |

A lista de convergências do pedido confere integralmente contra os bytes — e cresce de 7 para 10 pontos medidos.

## B — Correções efetivamente necessárias (posição da casa, uma a uma)

**Na versão do COMENTADOR:**

- **B1 — degrau 5 com campo errado.** A linha do degrau 5 lê `ancoras[].direcao_suporte` + "marcação de extrapolação". O schema selado define `direcao_suporte` como **eixo epistêmico do suporte** (`sustenta/refuta/inconclusivo/condicional`, "ortogonal ao papel") — não mede extrapolação. **Correção:** degrau 5 lê `verification_status` + `extrapolacao_por_analogia` (274/274, degrau pleno hoje). Detalhe que decide: a própria minuta do comentador já lista `verification_status` nos requisitos de consumo (Parte 5) — o campo certo estava na mão, na seção ao lado. (É a mesma correção que o mestre retratou publicamente no §0.1 da dele.)
- **B2 — célula da matriz `compensatoria × {causal, contributiva} = candidato`.** Executada sobre os 274 vínculos: dispara **exatamente 4 pares, todos falsos positivos** (`VINC_B1_0035×0036`, `0036×0037` no claim B1.MEC.BLOCO02.011; `0052×0261`, `0053×0261` no BLOCO02.019) — TNFR1≠TNFR2, IL-10 na mesma direção. `natureza_relacao` qualifica o **tipo** da relação, não o **sinal**. **Correção:** as duas células passam a `compatível`. Com a matriz corrigida, a mesma execução dá **0 pares**.
- **B3 — caminho do campo do degrau 3.** A tabela escreve `condicao` solto; o campo mora em **`ancoras[].condicao`** (medido no schema v1.4). Menor, mas contrato exige caminho exato.
- **B4 — T-14 (direção não-precedente) NÃO precisa de reformulação.** A casa disse na carta 22 que o teste seria "reformulável no regime novo". Revisão desta trilha: o teste usa `direcao_suporte` **na semântica certa** (sustenta × refuta → divergência não produz descarte nem ranking). É justamente o invariante que protege o campo depois da retratação. **Válido como está.**

**Na versão do MESTRE:**

- **B5 — regra degradada do degrau 7 restrita demais.** O texto dele barra `multifatorial` apenas quando o degrau **2 ou 4** está indisponível. Mas o degrau **3** hoje também está indisponível no acervo (`condicao` 0/274) — e pela justificativa dele mesmo ("perguntas que, sem resposta, deixam aberta a hipótese de o conflito ser aparente"), o degrau 3 deveria barrar igual. **Correção:** adotar a regra geral do comentador (Parte 4: **qualquer** degrau anterior indisponível barra `multifatorial`), citando 2 e 4 como os casos críticos do acervo atual. Hoje o efeito coincide; a diferença aparece no futuro.
- **B6 — colisão de IDs de teste (ver F1).** Renumerar os três testes novos (sugestão operacional: T-16/T-17/T-18), preservando os critérios — o T-14 dele (os 4 pares reais como regressão) é materialmente o teste mais valioso das duas versões, porque não é sintético.
- **B7 — citação interna por numeração local ("aceita da carta 10").** O conteúdo confere com o registro da casa (condição `condicao` ausente, 0/274), mas a numeração "carta 10" vive no projeto dele e não é auditável aqui. **Correção editorial:** mapear a referência na consolidada (número + documento-datado).

**Síntese B:** quatro correções no lado do comentador, três no lado do mestre. **Nenhuma das duas versões sai intacta** — e as correções de um lado já estavam resolvidas no outro. É o cenário ideal de consolidação.

## C — Elementos exclusivos úteis (veredito: preservar na consolidada?)

| De | Elemento exclusivo | Veredito da casa |
|----|--------------------|------------------|
| Mestre | "Mesmo objeto" = `ancoras[].id_oficial` + `ancoras[].escopo` + **proibição de `claim_id` como proxy** (com teste dedicado) | **Preservar** — é a operacionalização medida; evita os 4 FP |
| Mestre | **Matriz corrigida** (só `×nao_estabelecida` candidato; `marcador×nao_estabelecida` incluído por coerência, com nota "sem caso no acervo — revisar no piloto") | **Preservar** — a nota de honestidade vai junto (medida da casa: sem caso mesmo, C15) |
| Mestre | **Execução real 4→0 + T-14(novo)** sobre pares do acervo | **Preservar** — regressão não-sintética |
| Mestre | Tabela de executabilidade medida ("a L-06 só roda após a migração"; 243/274 migráveis) | **Preservar** — é o mapa do portão real |
| Mestre | Avisos anti-armadilha: **`escopo` não é contexto clínico** (degrau 2); `papel` **não adotado** como proxy do degrau 4 (decisão aberta) | **Preservar** — fiéis ao schema, medidos |
| Mestre | Gatilho em 3 formas de oposição (epistêmica/negação/efeito) com estado de executabilidade + "sustenta×inconclusivo não dispara" | **Preservar** |
| Comentador | **Gate de consumo** (Parte 5 + T-15): existência no acervo ≠ autorização; nada de campos de transição/depreciados | **Preservar** — é o anti-vazamento do funil; amarrar a definição de "aprovado" ao fluxo vigente (ver E1) |
| Comentador | **Parte 3** — degraus 5/6 não são desempate, com a frase-régua "direção de suporte não vira ranking" | **Preservar** — redundância de segurança que já se provou necessária (a retratação existiu) |
| Comentador | **Parte 1.3** — fronteira explícita L-06 × D-02 (resolução de concorrência não é autoridade epistemológica) | **Preservar** — o mestre tem 1 linha lateral; a seção própria é contrato |
| Comentador | **Parte 4 enumerada** — contrato do rastro: `degrau_N_indisponivel`, campo ausente, lista de degraus no resultado | **Preservar** — o mestre resume em 1 parágrafo; a especificação do rastro é mais auditável |
| Comentador | **Determinismo 6.3/6.7 explícitos** — "atribuição por relação, nunca pela posição" + sem precedência emergente | **Preservar** — o §4 do mestre não cobre o 6.3 |
| Comentador | **Parte 8, regra de implementação** — ausência de dependência não autoriza substituição silenciosa por campo "parecido" | **Preservar** — gêmea do aviso do mestre sobre `escopo`; juntas, fecham a porta dos dois lados |
| Comentador | **Parte 10** — risco residual do gatilho estreito + reavaliação pós-piloto + ampliação só por revisão formal | **Preservar** — com o arco completo: o risco a priori era "estreito demais"; o dado mostrou célula errada. Os dois lados da história ficam |
| Comentador | Distinção **ausência de estrutura × fragilidade de evidência** (Parte 1.3 + Parte 4) | **Preservar** — o núcleo está no texto; a consolidada deve dizê-lo em 1 frase explícita, porque é o erro de leitura mais provável |
| Comentador | **T-14** (direção não-precedente) | **Preservar como está** (ver B4) |

## D — Diferenças só de redação/organização (nenhuma ação técnica)

Estrutura (§0–8 × Partes 1–10) · listas × tabelas · ordem de apresentação da matriz · nomes de saída extra do comentador (`disjuncao_de_contexto`, `niveis_distintos`) — sinônimos; unificar vocabulário quando as saídas virarem enum (ver E5) · ênfases e títulos de seção · a nota de autoria/dedicatória ("Fase 3 da ordem" × "substitui a minuta 1" — procedência, tratada nas dívidas).

## E — Propostas novas que NÃO estão decididas (entram como deliberação, não como fato)

- **E1 — Gate de consumo:** quem declara uma relação "aprovada para consumo"? Precisa amarrar no fluxo de aprovação vigente (deliberação do mestre de 20/09 + P-11). Sem isso, o T-15 não tem oráculo.
- **E2 — `marcador × nao_estabelecida` = candidato:** mudança lógica correta, sem caso no acervo (medido). Fica condicionada à revisão no piloto.
- **E3 — `papel` como proxy do degrau 4:** decidido pelo mestre NÃO adotar; a decisão final fica para a Ontologia.
- **E4 — Ampliação futura do gatilho** (além dos extremos): só por revisão formal pós-piloto, com testes — o texto do comentador já diz; a consolidada confirma.
- **E5 — Vocabulário das saídas** (`sem_conflito`, `disjuncao_de_condicao`, `conflito_nao_resolvido`, rótulos 5–6…): quando a L-06 virar contrato, o conjunto selável precisa ser declarado. Hoje é prosa convergente.
- **E6 — Rótulos de trabalho [ETIQUETA-STATUS/B1] e o documento "Governo B1-N1":** citado na conversa como a casa das etiquetas, **mas esse documento não está na bancada (0 bytes)**. Registrada a dívida **D-GOV-B1N1-FONTE** — e o padrão dos rótulos é proposta nova a deliberar.
- **E7 — Rito de promoção:** a consolidada segue o rito de sempre: proposta → réplica da casa → **aprovação formal do operador** → vigente com sha/data.

## F — Inconsistências adicionais (não estavam no pedido)

1. **F1 — Colisão de IDs de teste (medida):** o comentador já usava **T-14** (direção não-precedente) e **T-15** (gate); a minuta do mestre marca **T-14/T-15/T-16 como "(novo)"** com critérios diferentes. Se consolidar sem renumerar, T-14 e T-15 passam a significar duas coisas ao mesmo tempo. *Nota: a atribuição do pedido está correta — os três testes novos são mesmo do mestre; o problema é que os IDs já tinham dono.*
2. **F2 — Extensão da regra degradada diverge** (medida): comentador = qualquer degrau anterior indisponível barra `multifatorial`; mestre = só 2 ou 4. Hoje o efeito coincide (2 e 4 indisponíveis); num acervo futuro com só o 3 indisponível, divergem. Resolução recomendada em B5.
3. **F3 — Dupla definição de "mesmo objeto":** comentador = conceitual (extremos + objeto: desfecho/marcador/processo); mestre = operacional (`id_oficial`+`escopo`). Não contradizem — são duas camadas; a consolidada deve declarar a ponte entre elas, senão implementadores lerão como duas coisas.
4. **F4 — Dependência comum não nomeada:** as duas versões dependem de `sentido_relacao`/Ontologia para a oposição de efeito (gatilho e degrau 4). Não é defeito de nenhuma; é dívida compartilhada (já registrada como D-SENTIDO-MAP).
5. **F5 — Numerações locais cruzadas:** o mestre cita "carta 10"; a casa registra por rodadas; o comentador cita "Fase 3 da ordem". A consolidada precisa de referências datadas, não de números de projeto (B7 + D-D01-D02-FONTE continua de pé).

---

## Resumo em 5 linhas (posição da casa — sem muro)

1. **O núcleo da L-06 já está de pé**: 10 convergências medidas, incluindo o invariante palavra por palavra nas duas versões.
2. **Correções caem dos dois lados** — 4 na do comentador (B1–B4), 3 na do mestre (B5–B7). Nenhuma versão sai intacta, e quase toda correção de um lado já está resolvida do outro.
3. **O conteúdo técnico novo mais valioso é do mestre** (execução real 4→0, matriz corrigida, proibição do proxy, mapa de executabilidade). **As proteções estruturais mais valiosas são do comentador** (gate de consumo, fronteira com D-02, contrato do rastro, determinismo por relação, T-14, Parte 10). A consolidada forte precisa **dos dois pacotes inteiros**.
4. **A casa não decide a arquitetura sozinha**: base e consolidação pertencem aos autores, com aprovação sua no fim do rito. Este documento é o mapa de verificação — cada item tem onde medir.
5. **O portão real continua sendo a migração** dos vínculos para o N2 v1.4 (243/274 por máquina): sem `ancoras[]`, nem o gatilho dispara — nas duas versões.

---
*Anexos técnicos (série da casa): trilha 73 script+JSON · minutas verbatim arquivadas com DIGITAIS · digitais deste pacote no anexo DIGITAIS e sha do zip no CHANGELOG 60. Documento-mestre B1: intocado (0 ciência).*
