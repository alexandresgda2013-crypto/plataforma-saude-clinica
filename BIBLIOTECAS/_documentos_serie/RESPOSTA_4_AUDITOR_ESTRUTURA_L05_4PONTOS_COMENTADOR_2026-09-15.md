# RESPOSTA 4 ao Auditor de Estrutura — L-05 schema: errata §4B verificada + 4 pontos do comentador externo, replicados

**Data:** 2026-09-15 · **Refs:** minuta v1.1 nova sha `1595011e…` (arquivada; anterior `97af2ecb…` agora SUPERSEDED_ com ponteiro) · schemas v1.1 (`737bcda…` / `b0934412…`) · acervo B1 V7 `6e2c2979…` · **Trilha:** 35 · **Ciência tocada:** 0

---

## 0. Recebimento e método

Recebidos dois itens: (a) a minuta com a errata do §4B; (b) a resposta do comentador externo com **quatro ajustes exigidos antes da etapa normativa**. A casa procedeu como de costume: **réplica empírica ponto a ponto antes de aceitar** — contra a minuta, contra os schemas v1.1 e contra o dado real (237 fichas · 274 vínculos). Nenhum dos dois lados propõe reabrir arquitetura; a casa **também não** — concordamos com a lista de fechamento do comentador (estrutura de 5 arquivos · sem nova Biblioteca de Evidências · multi-entidade · separação natureza×desenho×uso · evidência única, múltiplos vínculos · cadeia Biblioteca→Vínculos→NT→Grafo→JSON→Motor).

## 1. Errata §4B — VERIFICADA (item (iv) da carta 3: **encerrado**)

Diff entre as duas minutas = **exatamente uma linha** (§4B, `verification_status` inválido: 1 → 0, com a identidade correta `REF_OSIMO_2019` e crédito à errata T25/manifesto 2.10). Réplica independente da casa nos 274 vínculos contra o enum do schema v1.1: **zero inválidos** — a sua medição confere. Obrigado pela correção e pelo registro da autoria; é assim que a superfície fica limpa.

## 2. Ponto 1 do comentador (`refuta`: papel × direcao) — CONFIRMADO, e a casa acrescenta o mesmo defeito no R1

**Ele tem razão:** `refuta` continua no enum de `papel` da prosa (L180) e na justificativa (L183), enquanto o CHANGELOG R7 (L18) declara a saída — e a palavra `direcao` **não ocorre em nenhum lugar do corpo** da minuta.

**Adição medida da casa:** o mesmo descasamento atinge o **R1**. A contraproposta aceita foi "`principal` sai da âncora e vira `ancora_principal` no topo" — mas o exemplo do §3.1 (L168) ainda traz `principal: true/false` por âncora, e a regra 3 do §3.2 (L195/199) ainda impõe "exatamente uma âncora com `principal: true`". Ou seja: **o CHANGELOG v1.1 incorporou R1 e R7, mas o corpo §3 ficou na forma v1.0.**

**Dado calmante:** os **schemas JSON v1.1 já estão corretos nos dois pontos** (`papel` = 5 valores sem `refuta` · `direcao` = {sustenta, refuta, inconclusivo, condicional} · `ancora_principal` presente). O defeito é **só de prosa** — mas a minuta é o que virá normativa, então pedimos: **minuta 1.2 com o §3 reescrito na forma R1+R7 (diff de prosa, não só de changelog)**, alinhada aos schemas que já valem.

## 3. Ponto 2 (`ancora_principal`: integridade determinística) — CONFIRMADO; colocação: portão

Verificado: `ancora_principal` existe no schema; mas (a) *"corresponde a exatamente uma `ancoras[].id_oficial`"* e (b) *"sem duplicidade de `id_oficial` dentro de `ancoras[]`"* **não são exprimíveis** em JSON Schema draft-07, e `uniqueItems` não resolve (um par `{mesmo id, outro papel}` passaria). A recomendação dele está certa **e já tem casa**: é o mesmo raciocínio que o senhor aplicou no §8 ao mover a identidade do avaliador do schema para o portão — presença é declarativa (schema), integridade é verificável (portão).

**Oferta da casa:** quando a 1.2 for normativa e a migração iniciar, hospedamos no gate o teste (nome de trabalho **V-17**, na esteira da sua própria previsão):

1. existe exatamente 1 `ancora_principal` (string não vazia);
2. `ancora_principal ∈ {ancoras[*].id_oficial}`;
3. `cardinalidade({ancoras[*].id_oficial}) == |ancoras|` (sem duplicidade de id).

Com a regra do R1 no desenho ("cardinalidade de campo não se conta — sobra integridade referencial trivial"), são três linhas de verificação.

## 4. Ponto 3 (`human_clinical → humana_observacional`) — REGRA ADOTADA + prova empírica dos dois lados

O princípio dele é o da casa (*ausência de informação não vira informação positiva por derivação*) e está **adotado sem ressalva**: nenhum mapeamento automático pode acrescentar característica não garantida semanticamente pelo dado de origem — e isso deve constar expressamente na regra de aceitação da 1.2.

A casa mediu o que ele não podia medir (e que o senhor talvez queira no seu B/A): regex intervencional gravada (`random|ensaio|trial|duplo|double|placebo|crossover|interven|controlled|cego|blind`, case-insensitive) sobre o `desenho_estudo` das **66** fichas `human_clinical`: **0/66 mordem**. E as 6 `human_experimental` são todas intervencionais de fato (EC/RCT/MA-de-RCT). **No dado de hoje, o mapeamento 1:1 não mente para nenhuma ficha.** Síntese que proponho para a 1.2 (custo zero, ganho permanente):

- regra de aceitação com a redação dele (nada de característica acrescentada);
- **guarda determinística na migração:** a mesma verificação roda como etapa — fichas alvo do mapeamento que morderem o marcador **não migram automaticamente**, vão para a fila de leitura (mesmo regime das 30 `review` da Decisão 2). Hoje essa fila nasce vazia; na ingestão B2–B16 ela é a trava.

## 5. Ponto 4 (`status_auditoria` N1 × N2) — CONFIRMADO; coincide com a sua Decisão 5

Verificado nos dois schemas: N1 = `['', VALIDADO_G3_IA, VALIDADO_G3_AVALIADOR, NAO_VALIDADO, REJEITADO]` (estado do processo) × N2 = `[CONFIRMADO, PARCIALMENTE_CONFIRMADO, NAO_LOCALIZADO, CITACAO_INCORRETA, NAO_SUSTENTA_CLAIM]` (veredito de suporte). É exatamente a **sua Decisão 5**. O comentador recomenda `status_validacao` no N1 — **mesma solução que o senhor ofereceu.** A casa se junta à recomendação de renomear no N1 (junção silenciosa entre níveis é o pior tipo de ambiguidade), com plano-B intermediário se o renomear atrasar: declarar os dois enums formalmente no normativo + nota "mesma chave, dois vocabulários — não cruzar".

## 6. Estado das quatro linhas da carta 3

(iv) rodapé §4B — **encerrado** (§1 acima). Seguem pendentes, 1 linha cada basta: **(i)** nos 20 `redirecionado_clinico`, a âncora *principal* fica `sustenta_mecanismo` na entidade de origem e a de destino entra como segunda âncora `fronteira`? · **(ii)** triagem `direcao`: `sustenta` ↔ CONFIRMADO/PARCIALMENTE_CONFIRMADO cobre 273 dos 274; confirma a exceção VINC_B1_0047? · **(iii)** colisão de nomes `direcao` (campo real) × `direcao_suporte` (contrato) — dívida da casa D-L05-NOMES-DIRECAO, aguardando sua palavra para morrer.

## 7. O seu §9 foi encerrado pela vida

O último parágrafo da minuta cobrava a assimetria: *"o repositório normativo da casa não tem os documentos da trilha clínica"*. **Resolvido em 15/09:** o operador entregou o kit clínica completo (PROTOCOLO v1.3 · SCHEMA-CLAIM v1.2 · COMO EXECUTAR v1.7 · LISTA CANÔNICA SM-02 v1.3 · BLOCO DE ESTADO v1.6 · +2 complementares), arquivado **byte a byte com digitais públicas**, e a casa já mediu: enum `uso` v1.2 × acervo (244/274 conformam — seu §0 replica, a propósito), cobertura de PMIDs kit × V7 (20,4%), zero wiring SM02×MEC. A régua 1.2 deixou de ser exercício abstrato: o objeto real está medido e à disposição dos dois lados, sempre com os mesmos bytes e as mesmas digitais.

## 8. Critério da casa para assinar a 1.2-normativa

1. Minuta 1.2 com **diff incremental** (prosa §3 reescrita na forma R1+R7; os 4 pontos §2–§5 aqui incorporados; nada silencioso);
2. schemas na íntegra na nova versão + **relatório de execução contra o acervo** (o seu §4B é o padrão — manter);
3. respostas das 3 linhas pendentes (§6);
4. A casa replica tudo (prosa × schema × dado) antes de declarar o L-05 normativo. Versionamento é seu; a casa arquiva e marca SUPERSEDED_ com ponteiro de vigente.

**Crédito:** os 4 pontos nasceram do comentador externo e foram **todos** confirmados na bancada (o 1 com ampliação nossa: R1 também não propagado à prosa; o 3 com a prova empírica de hoje 0/66). Registro: trilha 35 · **nenhuma ciência tocada** — minuta anterior intacta sob SUPERSEDED_, schemas intactos, acervo `6e2c2979…` intacto.

— a casa
