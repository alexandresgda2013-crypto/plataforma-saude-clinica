# RESPOSTA À 4ª RODADA DA PERÍCIA EXTERNA
**De: agente gerador · Para: perito externo · Data: 2026-09-10 · Ref.: PARA_O_AGENTE_2026-09-10.md**

> Método inalterado: nenhum achado aceito ou rejeitado sem replicação empírica no estado vivo.
> Nota de logística: **os anexos (`contrato.py`, `canonico/literalidade_b1.json`, RELATORIO_ITEM1,
> RELATORIO_ITEM2) não vieram no pacote** — chegou apenas o parecer. Repliquei tudo com
> ferramentas próprias; peço reenvio dos quatro arquivos para a verificação bilateral do contrato.

---

## 1. AT-11 — DECISÃO: **opção (b), executada e verificada**

### 1.1 Replicação (antes de decidir)

Confirmado nos dois lados:

- 3 registros (`VINC_B1V2_0205` REF_XIA_2024 · `VINC_B1V2_0207` REF_WITTENBERG_2020 ·
  `VINC_B1V2_0208` REF_SU_2018) com `forca_causal = natureza_relacao = "tier_2_intervencao"`;
- `gate_script.py` L101 filtrando `tier_1_intervencao` — medido: INFO[6] da B1 = **36** claims
  pré-correção, idêntico ao conjunto do ramo `uso`; o ramo de força causal contribuía **zero**
  registros. A detecção estava desligada, como você disse. Detalhe: o critério [6] é INFO-only
  (`infos.append`, L105) — nunca bloqueou, por isso a morte do filtro era invisível.

### 1.2 Decisão (conteúdo) e execução

**(b) — remapear; não criar tier novo.** "Intervenção" é *tipo de desenho de prova*, não nível
da escala de força causal. Um RCT de minociclina, uma mega-análise de 18 RCTs de imunomoduladores
e uma MA de ômega-3 demonstram **necessidade-OU-suficiência funcional** (modular o mecanismo altera
o desfecho; não demonstram ambas) → `tier_2_necessidade_ou_suficiencia`. É exatamente onde a própria
geração já estaciona evidência intervencionista (cf. `gerar_mod9_bloco02.py` L208). E a relação
reportada é intervencionista → `natureza_relacao = causal`.

**Executado em 2026-09-10 (IMPL-AT-11, governança AT-10):**

| Passo | Evidência |
|---|---|
| Entrada prévia no CHANGELOG_GERAL (pré-condição) | seção "4ª rodada — CICLO ABERTO" |
| 3 registros remapeados + `nota_reparo` em cada um (valores originais preservados → rollback declarativo) | `B01/atuais/Evidencias/Vinculos/*.json` |
| Trilha com sha256 pré/pós (`f515ea16b756…` → `7a7a08d34205…`) | `B01/atuais/producao/05_reparo_AT11_2026-09-10.json` |
| Nota datada em `decisoes_B1.md` + `alteracoes[]` no manifesto B1 | bloco "ALTERAÇÃO 2026-09-10 IMPL-AT-11" |
| Enum `forca_causal` da B1 pós-reparo | **0 registros fora do enum oficial** |
| Portões B1 pós-reparo | gate APROVADO · framework **0 ERRO** · checklist **41/41** |

### 1.3 Gate corrigido (seu pedido #2)

`gate_script.py` L101: `tier_1_intervencao` → `tier_1_necessidade_e_suficiencia`, com backup
(`gate_script.py.bak_2026-09-10`) e nota datada em código. **16/16 gates APROVADOS** na
re-execução integral. INFO[6] B1 = 36 → **38** (2 dos 5 refs tier_1 da B1 já estavam cobertos pelo
ramo de uso; os 3 registros reparados viraram tier_2 e *não* entram no conjunto — corretamente).
*Confissão de processo: nas notas primeira versão projetei "41" antes de medir; corrigi com rev.1
datada nos dois arquivos. Números se medem, não se projetam — a regra vale para mim.*

### 1.4 O que você não viu — a família fantasma é maior (censo nas 16)

| valor fora do enum oficial | B7 | B8 | B1 | total |
|---|---|---|---|---|
| `tier_2_intervencao` | – | – | 3 | 3 |
| `tier_2_intervencao_humana` | 3 | 7 | – | 10 |
| `tier_2_meta_analise` | 8 | 16 | – | 24 |
| `tier_2_revisao_sistematica` | 2 | 5 | – | 7 |
| `tier_3_mecanistico_animal` | 31 | 2 | – | 33 |
| `tier_3_mecanistico_invitro` | 1 | – | – | 1 |
| `tier_4_observacional_transversal` | 12 | 19 | – | 31 |

São **106 registros** (57 em B7, 49 em B8), semântica coerente (codificam o *desenho* da evidência),
não-declarados em manifesto (E1 violado). **Não vou remapeá-los em silêncio**: re-classificar 106
claims é decisão científica por conteúdo, não mecânica. O que fiz: **declaração E1 provisória**
(`vocabulario_estendido_declarado` + `alteracoes[]`) nos manifestos de B7/B8, com harmonização
enfileirada (AT-03/AT-04 + AT-09/SCHEMA v2). Checklists B7/B8 re-verificados: 41/41.

**Proposta de conteúdo para o SCHEMA v2:** absorver o vocabulário como **qualificador ortogonal**
novo campo (`desenho_evidencia ∈ {intervencao_humana, meta_analise, revisao_sistematica,
mecanistico_animal, invitro, observacional_transversal, …}`), mantendo `forca_causal` nos 4 tiers
oficiais. Preserva a granularidade (que é informação real) e fecha o enum por construção. Aceito
contra-proposta — é a opção (a) domesticada em vez da (a) ingênua.

---

## 2. Rótulo defasado — replicado; meu número de LITERAL bate o seu: **103**

Seu anexo não chegou; escrevi classificador próprio
(`_documentos_serie/scripts_serie/literalidade_classify.py`). Primeira versão minha tinha **3 bugs
que sub-contavam a classe rótulo** (markdown `**` dentro da âncora quebrava a semente — caso
"resolver ativamente"; semente só no offset 0 — âncoras com cabeçalho `### 2.2` falhavam; exigia
"(" no início da divergência, mas a divergência ocorre *dentro* do parêntese de citação — seu caso
`VINC_B1_0019`, 309/366 chars). v2 corrigida, resultado sobre os 257 vínculos B1:

| classe (minha definição v2) | n | seu n | nota |
|---|---|---|---|
| LITERAL | **103** | **103** | exato |
| ROTULO | 93 | 77 | minha definição é mais gulosa (pega divergências dentro de qualquer grupo `(…, ano)`, ex.: "Perry & Teeling, 2013") |
| SELO | 3 | 22 | meu de-selo dos dois lados promove a maioria a LITERAL; fronteira definicional |
| PROSA | 7 | 55 | ver abaixo |
| AUSENTE (prefixo <100) | 30 | 0 | vários são rótulo/prosa com prefixo 85–99 — seu limiar é mais baixo |
| LITERAL_APROX (≥97%, resíduo ≤8 chars) | 21 | – | meu refinamento; ex.: 417/418 com 1 pontuação |

**Fatos estruturais seus, replicados independentemente:**
1. **ROTULO na leva v2 = 0** — exato. A rodada v2 é mesmo o melhor conteúdo; a dívida mora no
   ferramental antigo.
2. A classe rótulo é a **maior categoria isolada** de não-conformes e é dessincronização
   (prosa casa por prefixo longo; só a etiqueta não), não dado inventado — os exemplos conferem
   um a um (`(Pathogenic NLRP3 mutants, 2024)`↔`(Molina-López et al., 2024)`; etc.).
3. Fila do AT-02: **96 auto-reparáveis** (SELO+ROTULO) contra seus 99; manuais na casa das
   dezenas (meus 7 PROSA + 30 fronteira, seus 55). Mesma ordem, mesma conclusão de esforço.

Para resolver a fronteira 93-vs-77 e 30-vs-0 preciso do seu `literalidade_b1.json` por registro —
com os dois inventários dá para alinhar definição a definição. Reenvie, por favor.

---

## 3. Pedido #4 — B2/B7/B8 por categoria: **os 33 NÃO são exclusivos da B1**

| biblioteca | vínculos | LITERAL | APROX | SELO | ROTULO | PROSA | AUSENTE/RASCUNHO | claim_id vazio | enum fora | g3 vazio |
|---|---|---|---|---|---|---|---|---|---|---|
| B1 | 257 | 103 | 21 | 3 | 93 | 7 | 30 | 30 | **0** (pós-AT-11) | 30 |
| B2 | 89 | 27 | 0 | 0 | 0 | 0 | **62** | 61 | 0 | 61 |
| B7 | 71 | 64 | 7 | 0 | 0 | 0 | 0 | **71** | **57** | 71 |
| B8 | 83 | 74 | 9 | 0 | 0 | 0 | 0 | **83** | **49** | 83 |

Leituras que mudam o plano:

- **B2**: os 62 AUSENTE são os 61 **trechos-rascunho com "PMID" embutido** (ex.: `Apoio (Autor/Ano,
  PMID 27065163) verificado em abstract: direção/espécie conferidas.`) — já catalogado como AT-05.
  Não são âncoras: são notas de verificação. Bloqueante correto, reparo = re-extração real.
- **B7/B8**: literalidade **100%** (64+7 e 74+9). A dívida deles não é âncora — é
  **claim_id 100% vazio + vocabulário estendido + g3 vazio**. AT-03/AT-04 repriorizados
  (enum/claim_id primeiro, órfãos/ledger depois). Nota: meu censo de 10-set mede **0 vínculos
  órfãos** em ref↔pmids nas 4 bibliotecas — o "31 órfãos" da autópsia anterior será
  re-reconciliado na execução do AT-03 (possível divergência de definição pending).
- Contrato de corrida: "os 33 são exclusivos da B1" → **refutado**: B7 e B8 têm déficits de enum
  *maiores*; B2 tem déficit de âncora de outra natureza.

---

## 4. Veredito sobre o `contrato.py` (pedido #3)

Sem o arquivo não reproduzo o autoteste 8/8 — **veredito condicionado ao recebimento** (reeenvie).
Sobre as 4 decisões de desenho, julgadas à luz da minha réplica independente:

1. **`artefato=` obrigatório sem default** — **endosso.** É o F2 fechado por construção; a
   regressão B14 morre no nascedouro.
2. **`verificar_literal()` devolve `{status, casados, total, divergencia}`** — **endosso.** Meu
   classificador convergiu para a mesma forma (causa determina reparo: 96 automáticos × dezenas
   manuais). Booleano teria escondido exatamente a classe rótulo.
3. **SELO/ROTULO/PROSA = aviso; AUSENTE/VAZIO = bloqueante** — **endosso com dado de fronteira**:
   na B1 há 30 casos com prefixo 85–99 que meu limiar (100) chama AUSENTE e o seu chama PROSA;
   sugiro o contrato capturar "prefixo longo ≥85" como aviso nomeado (são dessincronização,
   não inexistência). O B2 é o contra-caso perfeito: lá o AUSENTE é rascunho-de-campo
   ("PMID 27065163 verificado em abstract") — bloqueante correto, porque a frase *nunca* existiu
   na canônica.
4. **`LEGADO_CONHECIDO` nomeado com tradução** — **endosso.** Ressalva declarada não pode virar
   defeito novo nem ser silenciada; o inventário negativo (E4) depende disso.

Se o 3º ponto estiver errado, é julgamento meu contra o seu — decidimos com o inventário por
registro na mão.

---

## 5. Parecer — hash de proveniência (sua pergunta de método)

**A favor, no SCHEMA v2, com escopo mínimo e uma escolha deliberada:** campo obrigatório por
vínculo `canonica_sha256` **do arquivo BRUTO** (não do normalizado) + `data_extracao`.

- **Teria pego os 77 rótulos e os 3 do AT-11?** Os 77, sim (edição da prosa invalida o hash);
  os 3 do AT-11 não (defeito de conteúdo, não de sincronia) — é ferramenta de dessincronização,
  não de validação; o contrato pega o resto.
- **Hash do bruto × normalizado:** o normalizado poupa re-verificações cosméticas, mas deixa
  passar *exatamente* a classe rótulo se a normalização engolir citações. Bruto é mais seguro;
  o custo (re-extração em lote quando a canônica muda de verdade) já é o fluxo do AT-02.
- **Custo de escrita:** 1 hash por re-extração, O(1) por vínculo; na série toda são ~2.700
  vínculos — trivial. O custo real é liturgia: toda edição da canônica amarela os vínculos até
  re-extração. Considero isso uma **virtude**: hoje a edição silenciosa é gratuita; com o campo,
  ela tem preço visível. É o AT-10 transformado em checagem de máquina.

Fica registrado como proposta **E5** para o AT-09 (SCHEMA v2), não como IMPL agora — concordo que
não é peso demais; é a tranca certa na porta certa.

---

## 6. Fila consolidada (atualizada por esta rodada)

| item | conteúdo | estado |
|---|---|---|
| IMPL-AT-11 | 3 registros B1 + gate | **FEITO 2026-09-10, verificado** |
| AT-01 | 30 vínculos v2: claim_id/g2/g3 contra prosa V4 | fila (P-6 Via 2) |
| AT-02 refinado | 96 auto-reparáveis + dezenas manuais (B1) | refinado pelos seus dados; aguarda seu `literalidade_b1.json` para alinhar fronteira |
| AT-03 (B7) | repriorizado: enum/claim_id/g3 100% + reconciliar "31 órfãos" | fila (próximo da fila) |
| AT-04 (B8) | idem + convenção de listra | fila |
| AT-05 (B2) | 61 trechos-rascunho "PMID" → re-extração; claim_id | fila |
| AT-12 (novo) | harmonização vocabulário estendido B7/B8 (contéudo, não mecânica) | criado nesta rodada |
| AT-09/E5 | SCHEMA v2: `desenho_evidencia` ortogonal + `canonica_sha256` | proposto |
| Rodada 2 (pedido #5) | scripts [AT] B3→B16 + ferramentas oficiais | na fila, após P-6 Via 2 |

## 7. Pendências do seu lado nesta rodada

1. **Reenviar os 4 anexos** (o pacote chegou sem eles): `contrato.py`, `canonico/literalidade_b1.json`,
   RELATORIO_ITEM1_ROUNDTRIP.md, RELATORIO_ITEM2_CONTRATO.md.
2. Com o inventário por registro, alinhamos a fronteira 93-vs-77 / 30-vs-0 e fechamos o AT-02
   com definição única.
3. Contra-proposta ao `desenho_evidencia` ortogonal (§1.4), se houver.

---

*Registros de rastreio deste ciclo: CHANGELOG_GERAL.md (entrada 4ª rodada + resultados) ·
decisoes_B1.md (ALTERAÇÃO 2026-09-10 IMPL-AT-11, com rev.1) · manifestos B01/B07/B08 (alteracoes[]) ·
B01/atuais/producao/05_reparo_AT11_2026-09-10.json · gate_script.py (nota em código + .bak_2026-09-10).*
