# COMO EXECUTAR — v1.11 (MINUTA rev.2 — não vigente)
# Correção vs. v1.10 (E-04 do ensaio pré-piloto .014 — 25/09)
# consolidada pelo Comentador (25/09):
#   - DUAS paradas operacionais: após LISTA G2 (fim da Rodada 1)
#     e após PARECER G3 (fim da Rodada 2); G1→G2 é contínuo
#     (concluir G1 NÃO é parada)
#   - auditoria cruzada das listas G2 antes de congelar
#   - G3 registra nível de leitura por PMID
#     (texto_completo | abstract | nao_lido; nao_lido ≠ analisado)
#   - avanço entre rodadas só com comando explícito do operador
#   - Nenhuma outra mudança vs. v1.10 (portões, critérios G1/G2/G3,
#     4 decisões, materialização — intactos)
# Correção vs. v1.9 (fecha a fila da Rodada 76 + interface + ciclo do kit):
#   - C-1: a IA 3 EMITE PARECER; o fechamento do claim é ato conjunto
#     posterior (retorno às IAs 1 e 2) — a IA 3 não fecha sozinha
#   - C-2: as TRÊS análises são INDEPENDENTES e CEGAS antes da comparação
#     (IA 2 não inspeciona "sobre a análise da IA 1"; IA 3 não vê as duas
#     antes de produzir a própria) — anti-ancoragem
#   - C-3: o parecer da IA 3 RETORNA às IAs 1 e 2; cada uma registra
#     confirmo / altero / mantenho divergência, sem apagar a análise original
#   - C-4: divergência factual vai à FONTE PRIMÁRIA, nunca à contagem de
#     concordâncias entre IAs
#   - C-5: ressalvas e limitações são PRESERVADAS no fechamento
#   - Fechamento entrega as 4 decisões do Contrato de Saída do Claim Kit
#     (vigente, 841532da): estado · direção por fonte (sentido_do_achado)
#     · tipo da ressalva (ressalvas[]) · moderadores — schema vigente é o
#     Schema-Claim v1.3 (28cbc9c7)
#   - Divergência cega é FUNCIONAMENTO CORRETO, não falha
#   - Materialização só após portões (Contrato de Saída §8) — este
#     documento não materializa; o materializador copia decisão pronta
#   - referências Schema-Claim v1.3 → v1.3 (vigente)
#   - Nenhuma mudança nas seções de portões G1/G2/G3, verificação ao
#     vivo, texto completo, heurísticas, exclusion terms, blindagem
#     (herdadas da v1.9 intactas)
# Correção vs. v1.8:
#   - nova seção "Protocolo de três IAs" (ChatGPT → Arena → Claude),
#     com papéis, princípio de arbitragem, tipos de divergência, limite
#     de rodadas, entrega mínima de rastreabilidade e formato do parecer
#   - status do protocolo: EM TESTE — piloto em B1.SM02.014; vira norma
#     operacional se o piloto passar
# Correção vs. v1.7:
#   - nova seção "Verificação ao vivo" e alteração da Regra inegociável 2:
#     o abstract exigido por G3 pode agora ser (a) colado pelo usuário OU
#     (b) recuperado AO VIVO pela IA na própria sessão, desde que o PMID
#     esteja confirmado em fonte verificável (PubMed/PMC, site do editor
#     ou repositório institucional) e a fonte seja nomeada. Nada muda
#     quanto à proibição de PMID ou número vindo de memória da IA
#   - regra de vocabulário fechado correspondente atualizada
#   - passo 6 e passo 13 do Fluxo de validação atualizados
#   - nota de destino: os claims de SM-xx são CLÍNICOS e alimentam a
#     pasta evidencias/bibliografia, não a biblioteca canônica mecanística
# Correção vs. v1.6:
#   - adicionada seção "Quando exigir texto completo em vez de resumo"
#     (heurística para decidir quando abstract não é suficiente e
#     texto completo deve ser priorizado). Motivada por caso real:
#     abstract publicado de PMID 33515765 (BIODEP/Schubert 2021) não
#     mencionava estratificação por ideação suicida; texto completo
#     revelou comparação post-hoc explícita (resultado nulo) que mudou
#     o desfecho de B1.SM02.017 e enriqueceu a ressalva de B1.SM02.015
#   - adicionada regra de vocabulário fechado correspondente na tabela
#     de blindagem ("abstract não é teto de evidência")
#   - passo 6 do Fluxo de validação de PMID atualizado com referência
#     cruzada à nova seção
#   - Nenhuma outra mudança de conteúdo em relação à v1.6
# Correção vs. v1.5:
#   - adicionado campo `redirecionados` em resultados_query: PMID
#     pré-clínico achado em busca de trilha_humana nunca vira
#     fontes_rejeitadas, vai para SM-03/SM-04/SM-08
#   - adicionada exclusion_terms_padrao_SM02 (filtro NOT formal,
#     escopado a Grupos 1 e 6 — não aplicar em literatura escassa)
#   - adicionadas 2 regras de vocabulário fechado: PMIDs pré-clínicos
#     nunca descartados; PMID nunca citado de memória da IA

## Destino dos claims deste kit

Os claims produzidos aqui são CLÍNICOS (meta-análise, caso-controle,
coorte, post-mortem humano, ômicas humanas) e alimentam a pasta
evidencias/bibliografia da plataforma. A biblioteca canônica
mecanística (fisiologia, cascata bioquímica) tem pipeline próprio e
não consome estes claims.

## Ordem de leitura/colagem dos documentos

A ordem não é arbitrária — vai do mais estável/fundacional para o mais
volátil/imediato. Isso garante que, no momento de agir, o que está
"mais fresco" no contexto da IA é exatamente o estado atual do
trabalho (Bloco de Estado), não uma regra genérica.

### Pacote mínimo obrigatório (toda sessão de validação de PMID)

1. **_ids_oficiais.json** — vocabulário de entidades válidas (base)
2. **Protocolo de Escopo** — fronteiras do mecanismo em trabalho
3. **Schema-Claim** — formato de saída obrigatório
4. **Como Executar** (este documento) — processo, portões G1/G2/G3,
   regras de vocabulário fechado
5. **Lista Canônica do submódulo ativo** — os alvos de trabalho (claims
   pendentes/aprovados daquele submódulo específico)
6. **Bloco de Estado** — sempre por último. É o mais mutável (muda a
   cada claim fechado) e o que efetivamente diz "onde paramos, o que
   fazer agora"

### Documentos condicionais (só entram quando o gatilho ocorrer)

- **Estrutura Mestre** — NÃO faz parte do pacote mínimo diário. Entra
  ANTES do item 5 acima (antes da Lista Canônica), apenas quando a
  sessão envolver decisão de escopo maior: abrir um submódulo novo,
  encerrar um submódulo e escolher o próximo, ou trocar de mecanismo
  (B1 → B2, etc.). Numa sessão comum de validação de PMID dentro do
  submódulo já ativo, não é necessária.

- **CANDIDATOS_IDS_OFICIAIS.yaml** — NÃO faz parte do pacote mínimo
  diário. O formato de registro já está embutido neste documento (Como
  Executar), então a IA consegue gerar uma sugestão de candidato sem o
  arquivo presente. Só cole o arquivo real se: (a) quiser que a IA
  consulte candidatos já registrados em sessões passadas antes de
  sugerir um novo (evitando duplicidade), ou (b) quiser que a IA edite
  o arquivo diretamente nesta sessão. Se colado, entra depois do item 1
  (_ids_oficiais.json), por pertencer à mesma família de catálogo de
  entidades.

Em Modo B (Projeto): itens 1-5 do pacote mínimo ficam anexados
permanentemente nessa ordem de upload, se a plataforma preservar ordem.
Item 6 (Bloco de Estado) é sempre colado manualmente no início da
conversa, por último em relação aos anexados, nunca substituído por
versão desatualizada. Estrutura Mestre e Candidatos podem ficar
anexados também, mas são consultados apenas quando o gatilho específico
de cada um ocorrer — não influenciam a validação rotineira de PMID.

Em Modo A (Chat avulso): colar os 6 do pacote mínimo, nesta ordem, na
mesma mensagem inicial ou em mensagens sequenciais antes de começar a
validação de qualquer PMID. Estrutura Mestre e Candidatos só entram na
sessão se o gatilho específico de cada um se aplicar naquele momento.

## Modos de operação

### Modo A — Chat avulso (sem persistência)
Colar SEMPRE, toda sessão nova, os 6 documentos do pacote mínimo:
Bloco de Estado + Protocolo de Escopo + Schema-Claim + _ids_oficiais.json
+ este documento + Lista Canônica do submódulo ativo.
Motivo: zero memória entre sessões. Sem o documento colado, a regra
não existe para a IA naquele momento.

### Modo B — Projeto (persistência via arquivos anexados)
Arquivos podem ficar anexados de forma permanente: Protocolo de
Escopo, Schema-Claim, _ids_oficiais.json, este documento, Lista
Canônica ativa.
MESMO ASSIM:
  - Colar SEMPRE o Bloco de Estado no início da sessão, mesmo em
    Projeto — é o único documento que muda a cada rodada de trabalho
    (claims aprovados crescem), não é seguro depender de versão
    antiga anexada.
  - Por ser conta gratuita, retrieval de arquivo anexado NÃO é
    garantido com alta confiabilidade. Regra de segurança: no início
    de cada sessão, pedir explicitamente à IA para confirmar quais
    arquivos anexados ela está lendo antes de iniciar validação de
    PMID. Se houver dúvida sobre se um arquivo foi lido corretamente,
    colar o trecho relevante manualmente — nunca assumir leitura
    silenciosa correta.
  - Ao fechar sessão, se algum documento mudou (Bloco de Estado,
    Lista Canônica), reanexar/atualizar o arquivo no Projeto antes
    da próxima sessão.

## Portões de aprovação (G1 · G2 · G3) — núcleo do processo

| Portão | Pergunta | Saída |
|---|---|---|
| G1 Existência | PMID/DOI resolvem; metadados conferem via API/busca | verified_reference |
| G2 Elegibilidade | desenho, espécie, população, ano, revista; retratação | eligible_source |
| G3 Suporte ao claim | o trecho sustenta a afirmação, no contexto e comparador corretos | approved_claim (3 saídas possíveis — ver abaixo) |

**Regra de ouro:** PMID aprovado em G1/G2 é fonte elegível, não
conhecimento. Conhecimento nasce em G3. Obrigatório: guardar o log de
exclusão, não só o de inclusão (estilo PRISMA) — ver `fontes_rejeitadas`
no Bloco de Estado.

## G3 detalhado — as 3 saídas possíveis (correção crítica)

G3 não é binário (aprova/rejeita). São 3 desfechos possíveis, e a
diferença entre eles é o que permite ao motor clínico, no fim da
cadeia, comunicar nuance real ao profissional em vez de simplificar
demais a evidência:

| Saída | Quando usar | O que o motor faz com isso |
|---|---|---|
| **aprovado** (pleno) | O abstract sustenta o claim de forma direta, comparador correto, sem heterogeneidade relevante levantada no próprio texto | Motor usa como evidência plena na narrativa clínica |
| **aprovado_com_ressalva** | O abstract sustenta o claim, MAS há limitação relevante (heterogeneidade alta, efeito pequeno/incerto, amostra restrita, comparador parcial) — não invalida, mas não é robustez plena | Motor SEMPRE inclui a ressalva na narrativa (ex: "há evidência de X, porém Y limita a certeza"). Nunca omite a ressalva, nunca promove a claim como se fosse plena |
| **rejeitado** | O abstract não sustenta o claim, ou pertence a outro mecanismo/submódulo, ou não atinge critério de elegibilidade | Vai para `fontes_rejeitadas` (log de exclusão), nunca é citado na narrativa clínica |

**Regra inegociável:** `status: aprovado_com_ressalva` exige
`nota_ressalva` preenchido (Schema-Claim já obriga isso) — sem
`nota_ressalva`, o claim não pode ser fechado com esse status, porque
o motor não teria o que comunicar ao profissional.

**C-5 (v1.10):** ressalvas e limitações levantadas em QUALQUER das
três análises são preservadas no fechamento — nada de "fechar limpo"
apagando limitação registrada por uma das IAs.

**Regra inegociável 2 (revista na v1.8):** G3 exige o **texto da fonte
presente nesta sessão**, obtido de uma de duas formas: (a) colado pelo
usuário, ou (b) recuperado ao vivo pela IA nesta sessão — ver
"Verificação ao vivo" abaixo. Sem o texto presente, a IA não avalia G3 — no máximo classifica G1/G2
e aguarda o abstract. Isso vale nos dois modos (Chat avulso e Projeto):
mesmo com PMID já conhecido de sessões anteriores, a avaliação de
suporte ao claim (G3) exige o texto presente *nesta* conversa, para
não depender de memória não verificável.

Ao avaliar G3 com o abstract colado, a IA responde 3 perguntas, nesta ordem:
1. **Pertencimento:** este PMID pertence de fato ao mecanismo/submódulo
   em validação, ou seria mais apropriado em outro dos 16 mecanismos?
2. **Suporte:** o trecho sustenta a afirmação do claim, no contexto e
   comparador corretos?
3. **Robustez:** a evidência é suficiente para uso clínico pleno, ou
   há limitação que exige ressalva (sem, no entanto, justificar rejeição)?

## Protocolo de três IAs (v1.10) — EM TESTE

Status: em teste. Piloto em B1.SM02.014 com o rito DESTE documento
(análises cegas → comparação → parecer → retorno → fechamento conjunto →
classificações do Contrato de Saída). O piloto da era v1.9 (se existir)
NÃO conta: o desenho mudou. Se o piloto passar, esta seção perde o
rótulo "em teste" e vira norma operacional.

### Papéis
- Operador (usuário): roda a sequência, decide, e é o único que roda
  PubMed; aprova o fechamento com as próprias palavras
- IA 1 (ChatGPT): busca inicial, triagem e **primeira análise
  INDEPENDENTE** do lote (cega: não vê análise da IA 2 nem da IA 3)
- IA 2 (Arena): **segunda análise INDEPENDENTE** (cega: não é
  "inspeção sobre a análise da IA 1" — produz a própria leitura antes
  de ver qualquer comparação)
- IA 3 (Claude): **terceira análise INDEPENDENTE** (cega) + verificação
  dos dados contra fontes primárias; **emite parecer** (não fecha o
  claim); o claim em schema é redigido/aprovado no fechamento conjunto

### Sequência em duas rodadas (anti-ancoragem — C-2 · consolidada pelo Comentador)
```
RODADA 1 — G1 + G2 (contínuo dentro da etapa)
  mesma lista bruta para as três IAs
  IA1: G1 (confirma/localiza TODOS os PMIDs → LISTA G1)
       → G2 (elegibilidade → LISTA G2)
       → ⛔ ENTREGA + PARADA
  IA2: idem → ⛔ ENTREGA + PARADA
  IA3: idem → ⛔ ENTREGA + PARADA
  [concluir G1 NÃO é parada — segue direto ao G2]
  só com as três LISTA G2 entregues:
  operador: auditoria cruzada (concorda / incluído errado /
  excluído errado / justificativa; sem votação; factual →
  fonte primária) → LISTA G2 CONGELADA → ⛔ comando do operador

RODADA 2 — G3 (só na lista congelada)
  IA1: G3 por PMID com texto na mesa → ⛔ ENTREGA + PARADA
  IA2: idem → ⛔ ENTREGA + PARADA
  IA3: idem → ⛔ ENTREGA + PARADA
  cada entrega registra nível de leitura por PMID:
  texto_completo | abstract | nao_lido
  (nao_lido NÃO conta como analisado em G3)
  só com as três entregas:
  operador: comparação (C-3) → divergência factual à fonte
  primária (C-4), nunca votação → ⛔ comando do operador

FECHAMENTO CONJUNTO (IA 3 propõe; IAs 1 e 2 respondem;
operador aprova) com as 4 decisões do Contrato de Saída
  → ⛔ PÁRA (nada se materializa sem portões §8)

Materialização futura: só com portões do Contrato de Saída §8.
```

### Regra de parada (E-04 — texto do Comentador)
> A IA pode executar continuamente todas as operações pertencentes
> à etapa corrente. A conclusão do G1 não constitui uma parada: a IA
> deve prosseguir imediatamente para o G2. A primeira parada ocorre
> somente após a conclusão de G1+G2 e a entrega da LISTA G2. A segunda
> parada ocorre somente após a conclusão da G3 e a entrega do
> parecer/tabela. O avanço para a etapa seguinte depende de comando
> explícito do operador.

Quem avança sozinho para a etapa seguinte está **fora do rito**
(E-04, ensaio 25/09). O operador comanda: quem entrega, quem compara,
quem abre o fechamento — nunca o conteúdo de cada análise.

**Divergência cega entre as três é funcionamento correto, não falha
(X-1):** independência aumenta a taxa de divergência aparente; isso é
sinal de análise limpa, não de erro de processo.

### Princípio de arbitragem (inegociável)
A fonte primária é o árbitro factual. Concordância entre IAs NÃO é
evidência e não fecha nada: três pareceres alinhados sobre um número
errado continuam errados. Nenhuma análise de IA entra como fonte de
claim; a evidência é sempre o artigo ou a revisão original. Análise de
IA orienta a leitura e nada mais.

Corolário (C-2/C-4): cada IA recontra o artigo na própria leitura; o
parecer da IA 3 é escrito DA FONTE, não das análises alheias. PMID,
desenho, população e números são reconferidos contra o artigo mesmo
quando as três análises depois concordam.

### Tipos de divergência e como cada uma fecha
| Tipo | Exemplos | Como resolve | Rodadas |
|---|---|---|---|
| Factual | PMID errado, número que não bate, desenho ou população mal classificados, n incorreto | Direto contra o artigo (C-4). Não vai a acordo nem a votação | 1 |
| Interpretativa | Texto do claim, força da evidência, ressalva vs. rejeição, qual achado é o principal | Discussão entre as três análises já produzidas | até 2 |
| De escopo | SM-02 vs. SM-14, B1 vs. B4, dentro ou fora do disease_context | Protocolo de Escopo B1 — critérios já escritos | 1 |

### Limite de rodadas interpretativas
Duas. Se não fechar, a divergência é REGISTRADA no próprio claim
(nota_ressalva / ressalvas[] conforme schema v1.3), com as duas
leituras nomeadas, e o trabalho segue. Não se força consenso: insistir
até concordar produz acordo por desgaste, não por evidência. Divergência
preservada é heterogeneidade real da literatura aparecendo (C-5).

### Entrega mínima de cada leva (sem isso, não há rastreabilidade)
1. Query exata, como rodada
2. Data da busca
3. Lista COMPLETA de resultados — não apenas os selecionados
4. Triagem: o que foi priorizado e por quê
5. As TRÊS análises independentes + o parecer da IA 3

### Parecer da IA 3 (formato)
1. Veredito G1 / G2 / G3 por PMID, com o que foi confirmado e onde
   (fonte do texto nomeada — ver "Verificação ao vivo")
2. Divergências em relação às análises 1 e 2, separadas por tipo
   (factual / interpretativa / escopo)
3. Claim PROPOSTO no Schema-Claim v1.3, campo a campo (proposta —
   o fechamento é ato conjunto, item 7 da sequência)
4. O que NÃO foi possível verificar, explicitamente

### Fechamento conjunto — as 4 decisões (Contrato de Saída vigente)
Todo claim fechado entrega, além do corpo do Schema-Claim v1.3:
1. **Estado:** aprovado | aprovado_com_ressalva
2. **Direção por fonte:** sentido_do_achado (suporta_relacao |
   refuta_relacao | inconclusivo) em CADA fonte que materializar —
   decidido com leitura da fonte, sem default (R-1)
3. **Tipo da ressalva:** ressalvas[] com tipo (condicao_aplicacao |
   heterogeneidade | maturidade_evidencia) quando houver (P-K2/P-K3)
4. **Moderadores:** variavel/efeito/regra_motor já estruturados;
   `inverte` materializa só no N2 v1.5 (P-K6 travado)

Ausência de direção em fonte materializável = claim não fechado /
falha de materialização. O materializador NÃO decide nenhum dos quatro.

### Registro das rodadas
- Rodada factual e de escopo: o desfecho já aparece no claim
- Rodada interpretativa não fechada: entra em nota_ressalva/ressalvas[]
- Histórico das rodadas: na entrada do claim na Lista Canônica
- Análises originais das três IAs são preservadas (não apagadas) no
  registro da sessão

### Lote em vez de claim a claim
Quando o tema permitir, agrupar por lote em uma leva só — mantendo a
ordem cega (cada IA entrega a análise do lote antes de ver as outras).

## Verificação ao vivo (v1.8)

A IA pode buscar e recuperar o texto da fonte na própria sessão. O que
isso NÃO muda: PMID e número continuam proibidos de virem de memória
da IA, de sessão anterior ou de inferência. O que muda: "colado pelo
usuário" deixa de ser a única origem aceitável do texto.

Condições, todas obrigatórias:
1. O PMID tem de ser confirmado em fonte verificável nesta sessão —
   PubMed/PMC, site do editor, ou repositório institucional que exiba
   o par PMID ↔ título/DOI. Achar o artigo sem achar o PMID = G1
   incompleto, o PMID não entra
2. A IA nomeia a fonte de onde tirou o texto ao reportar o claim
3. Resumo de terceiro (tabela de revisão, notícia, agregador) serve
   para LOCALIZAR o estudo, nunca como origem do número. O número sai
   do abstract/texto do próprio artigo
4. Matriz de extração pronta trazida pelo usuário (ou por outro agente)
   não substitui a fonte: os números precisam ser conferidos contra o
   texto recuperado antes de virarem verificado_nesta_conversa: sim
5. Se a recuperação falhar (paywall, sem texto acessível), o PMID fica
   em G1/G2 e aguarda o usuário colar — nunca se estima o conteúdo

A busca da query no PubMed continua sendo do usuário: a IA não roda
PubMed, e a lista completa de resultados é o que sustenta
resultados_nao_triados e o log de exclusão.

## Quando exigir texto completo em vez de resumo (novo)

Resumo (abstract) continua sendo o padrão mínimo — G3 exige "abstract
colado nesta sessão" (Regra inegociável 2, acima), isso não muda. Mas
resumo não é sinônimo de evidência completa: resumos científicos
comprovadamente omitem análises secundárias/post-hoc do próprio
artigo, com viés sistemático a favor de achados positivos e contra
achados nulos — fenômeno documentado na literatura de meta-pesquisa
como "abstract reporting bias". Caso real que motivou esta seção: o
abstract publicado de PMID 33515765 (BIODEP/Schubert 2021) não
menciona nenhuma estratificação por ideação suicida; o texto completo
revelou uma comparação post-hoc explícita (MDD com vs. sem ideação
suicida, resultado nulo) que mudou o desfecho de B1.SM02.017 e
enriqueceu a ressalva de B1.SM02.015.

Puxar texto completo passa a ser PREFERENCIAL (não obrigatório) quando
qualquer um destes se aplica:

1. O claim depende de 3 ou menos fontes principais — poucas fontes
   significam que cada uma carrega peso desproporcional; erro ou
   omissão em uma muda o resultado do claim inteiro
2. O dado sendo extraído é de subgrupo/análise post-hoc/exploratória
   do estudo — não o desfecho primário declarado no título/objetivo
3. Grupo 3 de SM-02 (TSPO-PET) especificamente — padrão de subanálise
   múltipla por artigo (região × severidade × subgrupo clínico) já
   confirmado mais de uma vez nesta submódulo
4. Antes de tratar "o resumo não menciona X" como evidência de que o
   estudo não testou X — silêncio no resumo não é ausência no estudo
5. Quando o desfecho da leva atual está caminhando para
   `aprovado_com_ressalva` ou `rejeitado` com base em evidência
   aparentemente fraca ou escassa — antes de aceitar como final,
   checar se o texto completo muda o quadro (mesma lógica do gatilho
   de revisão já existente para `resultados_nao_triados`, abaixo)

Quando o texto completo mudar o desfecho de um claim já fechado com
base no resumo, a fonte é reclassificada dentro da entrada existente
(não criada como nova fonte solta) e o `version` do claim é
incrementado — ver Schema-Claim. Isso NÃO é uma falha do processo:
`aprovado_com_ressalva` existe justamente para comunicar incerteza
real ao motor clínico, e revisar um claim à luz de evidência mais
completa é o processo funcionando como projetado, não retrabalho a
evitar.

Esta seção não obriga reabertura retroativa de claims já fechados
apenas com resumo — decisão de auditoria retroativa (quais claims,
quando) fica a critério do usuário, caso a caso.

## Heurística de priorização de leitura de resultados de query (novo)

Quando a query no PubMed retornar múltiplos resultados, a ordem de
leitura NÃO deve ser "os mais recentes primeiro" por padrão — recência
sozinha não é critério científico suficiente e já causou perda de
evidência definitiva em rodadas anteriores. Seguir esta ordem:

1. **Desenho do estudo**, na ordem de `inclusion_criteria.designs` do
   Protocolo de Escopo (meta-análise/revisão sistemática > RCT >
   coorte prospectiva > caso-controle > post-mortem)
2. **Tamanho amostral/k**, se visível no título ou resumo da lista de
   resultados (meta-análise com k=37 estudos pesa mais que k=5)
3. **Recência**, apenas como critério de desempate dentro do mesmo
   nível dos dois critérios acima

Ler em lotes práticos (ex: 5-10 por vez), não a lista inteira de uma vez.

## Fila de resultados não triados (novo)

Todo PMID que a query retornou, mas que não foi lido/avaliado na leva
atual, DEVE ser registrado em `resultados_nao_triados` (dentro da
entrada do claim, na Lista Canônica) — nunca descartado silenciosamente.
Isso é diferente de `fontes_rejeitadas` (já lido, não sustentou) e de
`fila_realocacao` (já lido, pertence a outro lugar/submódulo): esta
fila é para "encontrado pela query, ainda não lido".


Caso adicional — estudo pré-clínico encontrado em busca de trilha_humana:
nunca classificar como rejeitado nem descartar silenciosamente. Registrar
em resultados_query.redirecionados, com destino_sugerido apontando o
submódulo onde esse achado tem valor mecanístico (ex: SM-03 para
causalidade, SM-04 para microglia, SM-08 para vias de sinalização).
Motivo: evidência animal não serve à trilha_humana do submódulo atual,
mas pode ser ouro para submódulos pré-clínicos futuros — descartá-la
viola a regra "nenhum resultado de query descartado sem registro".


**Gatilho de revisão obrigatório:** se a primeira leva de PMIDs lidos
resultar em `aprovado_com_ressalva`, `rejeitado`, ou evidência
insuficiente/inconclusiva para fechar o claim com confiança — antes de
aceitar esse desfecho como final, reabrir `resultados_nao_triados`
daquele claim e avaliar se algum PMID ali pode mudar o resultado.
Marcar `revisado_apos_gatilho: sim` quando isso ocorrer.

Formato do campo na Lista Canônica:
yaml
resultados_query:
  triados:
    - {pmid: "xxxxxxxx", desfecho: aprovado | aprovado_com_ressalva | rejeitado}
  nao_triados:
    - {pmid: "xxxxxxxx", titulo: "string", motivo: "não priorizado na primeira leva de triagem", data_registro: "AAAA-MM-DD"}
  redirecionados:
    - {pmid: "xxxxxxxx", motivo: "estudo pré-clínico (animal/in vitro) encontrado em busca de trilha_humana",
       destino_sugerido: "SM-03 | SM-04 | SM-08 (conforme natureza do achado)",
       trilha: preclinica, data_registro: "AAAA-MM-DD"}
  revisado_apos_gatilho: sim | nao
  
Regras de query — quando gerar, quando reformular
Caso	Situação	Ação
A — Query já existe	Lista Canônica do submódulo ativo já tem query para o claim-alvo	Usar tal como está
B — Query não existe	Submódulo novo, Lista Canônica ainda não tem entrada para esse claim	IA gera query nova; só vira "oficial" quando registrada na Lista Canônica
C — Query falhou	Zero resultados ou resultados fora do escopo	IA reformula. Registrar em query_historico, dentro da própria entrada do claim na Lista Canônica, com motivo e data — nunca substituir silenciosamente a query antiga sem deixar rastro
Formato do histórico (só existe se houve reformulação de query):

YAML

query_historico:
  - versao: 1
    query: "query original"
    motivo_substituicao: "zero resultados" | "resultados fora do escopo" | outro
    data: "AAAA-MM-DD"
	
	
## Exclusion terms — regra formal por submódulo

Submódulos de "prova de existência basal" (SM-02) exigem filtros NOT
para evitar contaminação com perguntas de intervenção/tratamento,
que pertencem a SM-14. O NOT NÃO é regra universal — aplicar apenas
onde o racional abaixo se sustenta. Em queries de nicho com literatura
escassa (LCR, TSPO-PET, post-mortem, ômicas), o NOT pode zerar
resultados por falso-negativo de indexação MeSH.

exclusion_terms_padrao_SM02:
  aplicacao: "Grupos 1 e 6 de SM-02 (periférico e confundidores — alto volume de literatura)"
  nao_aplicar_em: "Grupos 2, 3, 4, 5 (LCR, TSPO-PET, post-mortem, ômicas — literatura escassa)"
  termos:
    - termo: "electroconvulsive therapy[mh]"
      motivo: "contamina prova de existência basal com resposta a intervenção — pertence a SM-14"
    - termo: "antidepressive agents[mh]"
      motivo: "idem — efeito de antidepressivo sobre citocina é pergunta de SM-14, não de SM-02"
    - termo: "treatment outcome[mh]"
      motivo: "idem — desfecho de tratamento não é prova de existência basal"
  como_usar: >
    Anexar ao final de queries dos Grupos 1 e 6 ainda não executadas:
    NOT (electroconvulsive therapy[mh] OR antidepressive agents[mh]
    OR treatment outcome[mh])
  nota_retroatividade: >
    As 9 queries já executadas (claims aprovados .001-.007b) mantêm
    seus resultados — não retrofiitar. Aplicar apenas nas queries
    pendentes antes de rodar no PubMed.

regra_geral_novos_submodulos: >
  Cada novo submódulo (SM-03 em diante) deve declarar seus próprios
  exclusion_terms explicitamente ao abrir sua Lista Canônica, com
  justificativa por termo. Nunca herdar silenciosamente os termos de
  SM-02 — o racional de "prova de existência basal" é específico
  deste submódulo.
	
	
# Fluxo de validação de PMID

1 Escolha do claim-alvo (próximo pendente na Lista Canônica ativa)

2 Verificar Caso A/B/C acima para a query

3 Rodar no PubMed (celular ou navegador)

4 Colar a lista completa de resultados (títulos + PMIDs) no chat
— não apenas os que parecem melhores à primeira vista

5 Aplicar a heurística de priorização (desenho > amostra/k > recência)
para decidir a ordem de leitura

6 Colar PMID/título + abstract completo dos priorizados no chat, OU
pedir à IA que recupere ao vivo (ver "Verificação ao vivo" — o texto
da fonte é obrigatório para G3, a origem dele pode ser qualquer uma
das duas). Se o claim se
enquadrar em algum critério de "Quando exigir texto completo em vez
de resumo", priorizar texto completo já nesta etapa

7 IA aplica G2 (elegibilidade) e G3 (pertencimento, suporte, robustez —
3 perguntas, gera uma das 3 saídas possíveis)

8 FECHAMENTO CONJUNTO do claim (C-1/C-3): a IA 3 propõe o preenchimento;
as IAs 1 e 2 registram confirmo/altero/mantenho; o operador aprova.
Preenche Schema-Claim v1.3 completo com as 4 decisões do Contrato de
Saída vigente: uso, comparador, estado (status), DIREÇÃO POR FONTE
(sentido_do_achado em cada fonte materializável), TIPO DE RESSALVA
(ressalvas[] quando houver — P-K2/P-K3), moderadores, e nota_ressalva
se status = aprovado_com_ressalva. Sem direção decidida → claim não
fechado (falha dura). Ou vai para fila_realocacao (outro mecanismo)
ou fontes_rejeitadas (não sustenta). A materialização em N1/N2 é
PASSO SEPARADO, só com os portões do Contrato de Saída §8 — este
fluxo não materializa.

9 Registrar o restante da lista (não lido nesta leva) em
resultados_nao_triados

10 Se o desfecho da leva atual for ressalva/rejeitado/inconclusivo →
aplicar o gatilho de revisão da fila resultados_nao_triados
antes de fechar o claim como final

11 Se surgir candidato a ID oficial (novo exame/biomarcador/suplemento
não catalogado em _ids_oficiais) → checar contra o
_ids_oficiais.json presente na sessão antes de declarar "não
catalogado" → registrar usando o formato compacto abaixo. Não
bloqueia a validação do claim em curso.

12 Ao fechar sessão: salvar YAML do Bloco de Estado atualizado — só o
YAML, sem texto de explicação — versionado (v1.5, v1.6...) com data

13 Todo dado numérico (%, d, OR, IC95%) só entra como
verificado_nesta_conversa: sim se o texto de origem esteve presente
NESTA thread — colado pelo usuário ou recuperado ao vivo pela IA. Senão → nao ("herdado_nao_verificado"), mesmo que
o número pareça correto

# Formato compacto — registro em CANDIDATOS_IDS_OFICIAIS
Quando o gatilho do passo 11 ocorrer, gerar entrada neste formato
(mesmo sem o arquivo completo colado na sessão — este é o contrato):

YAML

- nome_sugerido: string        # snake_case, sem acentos/hífen/espaço
  categoria_provavel: string   # ex: C4_inflamatorios, D3_fitoterapicos
  motivo: string
  pmid_origem: string
  mecanismo_origem: string     # ex: B1, B7
  status: sugerido
  data: string

Essa entrada é reportada ao usuário no chat; a inclusão física no
arquivo CANDIDATOS_IDS_OFICIAIS.yaml é feita por você, fora da sessão
corrente (ou colando o arquivo se quiser que a IA edite diretamente).

#Regras de vocabulário fechado (blindagem)

*Regra	                                                                        Efeito
Nunca criar ID de claim - IDs só vêm da Lista Canônica do submódulo. PMID sem ID mapeável → unmapped, você decide

Vocabulário fechado - Só target · verified_reference · eligible_source · approved_claim. Nada de sinônimos informais

Números só de fonte visível - Se não está na Lista Canônica nem no texto colado nesta sessão → ?, e pergunto

claim_id ≠ ID oficial - claim_id nunca é validado contra _ids_oficiais; só referencia_cruzada usa ID oficial completo

Formato nunca por inferência - Todo campo de claim segue Schema-Claim v1.3 colado/anexado na sessão — nunca por "padrão observado" em exemplos anteriores

G3 exige o texto nesta sessão - Sem o texto presente (colado pelo usuário ou recuperado ao vivo pela IA, com PMID confirmado e fonte nomeada), não há avaliação de suporte ao claim — no máximo G1/G2 ficam pendentes de G3

Matriz pronta não é fonte - Extração já tabulada (por você ou por outro agente) orienta a leitura, mas os números só viram verificado_nesta_conversa: sim depois de conferidos contra o texto do próprio artigo nesta sessão

Abstract não é teto de evidência - Resumo satisfaz o mínimo exigido por G3, mas não é blindagem contra achado relevante omitido no texto completo (viés documentado de omissão de análise secundária/nula em resumos). Ver "Quando exigir texto completo em vez de resumo".

Ressalva nunca é omitida nem inflada - aprovado_com_ressalva sempre carrega nota_ressalva; motor clínico nunca apresenta essa evidência como plena, nem a descarta

Candidato a ID checado contra catálogo real - _ids_oficiais.json precisa estar presente na sessão antes de declarar algo "não catalogado"

Nenhum resultado de query descartado sem registro - Todo PMID retornado pela busca e não lido vai para resultados_nao_triados — nunca simplesmente ignorado

PMIDs pré-clínicos nunca descartados - Estudo animal ou in vitro encontrado em busca de trilha_humana NÃO vai para fontes_rejeitadas. Vai para resultados_query.redirecionados com destino_sugerido (SM-03 | SM-04 | SM-08 conforme natureza do achado) e trilha: preclinica. Descartar é perder PMID potencialmente útil para submódulos futuros.

PMID nunca de memória de IA - Nenhum PMID entra no sistema sem: (a) abstract colado pelo usuário nesta sessão, OU (b) retorno verificado via API em G1. A IA jamais cita PMID de sessões anteriores, de "conhecimento geral" ou por inferência de autor/ano/tema — mesmo que o formato numérico pareça válido. PMID não verificado nesta sessão = não existe para o sistema. Erro distinto de "Números só de fonte visível": aquele cobre dados numéricos dentro do claim; este cobre o identificador da fonte em si.

*Se eu produzir ID, número, status ou campo fora dessas regras, corta na hora.