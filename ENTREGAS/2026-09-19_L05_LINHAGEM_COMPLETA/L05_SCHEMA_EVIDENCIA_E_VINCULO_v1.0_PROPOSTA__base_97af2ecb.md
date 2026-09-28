# L-05 — SCHEMA DE EVIDÊNCIA E VÍNCULO COM ANCORAGEM MULTI-ENTIDADE
## v1.0 — PROPOSTA, aguardando decisão do responsável pelo projeto

**Status:** PROPOSTA v1.1. Não é normativo. Não foi aplicado a nenhum dado.

## CHANGELOG v1.0 → v1.1

Emitida após o Parecer da Casa nº 2 e seu Adendo nº 1. Os sete ajustes pedidos foram incorporados; dois deles com contraproposta, explicitada abaixo.

| Ajuste | Tratamento |
|---|---|
| **R1** — "exatamente 1 principal" inexprimível em draft-07 | **Contraproposta.** Em vez de mover o invariante para portão imperativo, o invariante foi eliminado por construção: `principal` sai da âncora e vira `ancora_principal`, campo único no topo do vínculo. Cardinalidade de campo não precisa ser contada. Ao portão sobra apenas integridade referencial — checagem trivial. Se a casa preferir manter o booleano por âncora, a proposta do P-8/V-17 continua válida e esta contraproposta é descartável. |
| **R2** — `_ids_oficiais.json` não existe como arquivo | **Aceito, com critério de aceitação adicional.** Ver §7. |
| **R3** — E2 por substring morde avaliador legítimo | **Aceito, com solução diferente.** Ver §8. |
| **R4** — normalização de prefixo + `APENDICE_CORPUS` | Aceito. `escopo` normalizado documentado no schema; `APENDICE_CORPUS` vira valor reservado de escopo. |
| **R5** — manual de classificação de desenho | Aceito. A regra "natureza = material revisto" entrou na descrição do campo, que é onde ela precisa estar para não se perder. |
| **R6** — `citacao_confirmada` é default de geração | Aceito integralmente. Campo marcado `deprecated`, descrição corrigida, Decisão 4 encerrada com a prova documental da casa. |
| **R7** — `papel` lido como veredito; eixo `direcao` | **Aceito sem ressalva, e é o melhor ajuste do ciclo.** `refuta` sai de `papel` e vira `direcao: refuta`. É o mesmo princípio dos três eixos que sustenta esta proposta inteira, aplicado a um lugar onde eu mesmo o violei. |

## ERRATA v1.0 — três erros meus, confirmados por medição própria

1. **§3.1 media o objeto errado.** Escrevi "21 valores distintos" descrevendo a âncora do vínculo. 21 é a contagem nas *fichas*; nos *vínculos* são 92, em três formatos. A tese ("100% dentro de B1, zero em exame, cenário ou suplemento") está confirmada, mas o número citado era de outro objeto. Corrigido em §3.1.
2. **§4B atribuiu mal o `verification_status` inválido.** A contagem (1) estava certa; a identidade, não. Não era a dívida de full-text — era `REF_OSIMO_2019`, com valor livre e erro de digitação, escrito na própria rodada de auditoria e invisível a todos os portões. Eu encaixei o achado na dívida conhecida em vez de abrir o registro. É o mesmo erro de raciocínio que apontei na difusão de bug do ramo morto, cometido por mim uma mensagem depois.
3. **A regra E2 do schema tinha o defeito que ela deveria impedir.** Ver §8.

**Origem:** decisão de arquitetura do responsável (2026-09-14): *"a lacuna não é uma nova Biblioteca de Evidências Clínicas. O ponto que faltava é o vínculo estruturado entre cada evidência bibliográfica e os objetos científicos do sistema."*
**Subordinado a:** DECISOES_ARQUITETURAIS (P11, P12, P18, P20), _ids_oficiais.json, Filosofia do Projeto.
**Medido contra:** acervo B1 V7 — 237 referências, 274 vínculos.

```json
"natureza_sistema": {
  "tipo": "suporte_decisao_clinica",
  "nao_substitui_julgamento_profissional": true,
  "nao_realiza_diagnostico": true,
  "decisao_final_profissional": true
}
```

---

# 0. ACHADO QUE ANTECEDE O DESENHO

Antes de propor qualquer campo, um fato medido que muda o diagnóstico anterior.

O campo `uso` **não está fora de enum nenhum.** Ele está no enum do SCHEMA-CLAIM **v1.2** — o schema da trilha clínica:

| | v1.2 (trilha clínica) | v3.1 (trilha mecanística) | acervo B1 |
|---|---|---|---|
| valor 1 | `clinico` | `nucleo_causal` | `clinico` — 37 |
| valor 2 | `contexto_mecanistico` | `suporte_correlacional` | `contexto_mecanistico` — 178 |
| valor 3 | `gap_pesquisa` | `gap_pesquisa` | `gap_pesquisa` — 29 |

**244 dos 274 vínculos (89%) conformam exatamente ao enum da v1.2.** O gate valida contra a v3.1. Não houve deriva de vocabulário: houve dois schemas vivos e uma comparação contra o errado.

Os 30 restantes (`B1_v2`) são outra coisa. São exatamente os mesmos 30 registros cujo `secao_origem` na Bibliografia termina em `/v2`. `B1_v2` é etiqueta de leva de produção que vazou para dentro de um campo semântico — não é valor de `uso`, é procedência sem campo próprio.

**Consequência para este desenho:** o schema abaixo trata `uso` como campo de **duas trilhas legítimas**, não como campo a normalizar, e cria campo próprio para procedência.

---

# 1. PRINCÍPIO DO DESENHO

Três eixos que hoje estão misturados, separados em três campos independentes:

```
QUEM/O QUE FOI ESTUDADO     →  natureza_evidencia   (humano? animal? in vitro? tecido?)
COMO FOI ESTUDADO           →  desenho_estudo       (meta-análise? RCT? coorte? knockout?)
PARA QUE O SISTEMA USA      →  uso                  (clínico? mecanístico? lacuna?)
```

Hoje os três colidem. `review` aparece 30 vezes em `natureza_evidencia` — mas revisão é **desenho**, não natureza. Uma revisão sistemática de estudos humanos é, ao mesmo tempo, `humana` em natureza e `revisao_sistematica` em desenho. Com um campo só, é preciso escolher, e a informação que sobra se perde.

Separados, os três coexistem sem contradição — é o mesmo raciocínio dos 4 eixos de evidência já consagrado no SCHEMA-CLAIM v3.1, aplicado uma camada acima.

---

# 2. NÍVEL 1 — REGISTRO DE REFERÊNCIA

Um registro por referência bibliográfica. Mora em `/Evidencias/Bibliografia/`, na estrutura de 5 arquivos do Módulo 09, **sem criação de pastas por tipo de estudo** (ver §6).

## 2.1 Campos preservados sem alteração

`pmid_oficial` · `doi` · `titulo_artigo` · `autores` · `revista_ano` · `id_referencia_interna` · `ids_referencia_interna` · `_aliases` · `origem_pipeline` · `g1_metodo` · `g3_verificado_por` · `status_auditoria` · `verification_status` · `claim_id_origem` · `achado_central_molecular` · `extrapolacao_por_analogia` · `especie_mesh`

Nenhum campo existente é removido por esta proposta.

## 2.2 Campos com enum fechado (novo)

### `natureza_evidencia` — enum obrigatório

| valor | definição |
|---|---|
| `humana_observacional` | estudo em humanos sem manipulação pelo investigador |
| `humana_experimental` | estudo em humanos com intervenção atribuída pelo investigador |
| `humana_post_mortem` | tecido humano post mortem |
| `preclinica_in_vivo` | modelo animal |
| `preclinica_in_vitro` | célula, cultura, organoide, tecido isolado |
| `mista` | a mesma fonte reporta braço humano e braço pré-clínico |
| `nao_aplicavel` | manual, consenso, livro-texto |

Mapeamento a partir dos valores atuais:

```
human_clinical            (66) → humana_observacional
human_experimental         (6) → humana_experimental
post_mortem                (2) → humana_post_mortem
preclinical_mechanistic  (133) → preclinica_in_vivo | preclinica_in_vitro   ← exige triagem
review                    (30) → NÃO MAPEÁVEL AUTOMATICAMENTE               ← ver Decisão 2
```

### `desenho_estudo` — enum obrigatório

`meta_analise` · `revisao_sistematica` · `revisao_narrativa` · `ensaio_randomizado` · `ensaio_nao_randomizado` · `coorte_prospectiva` · `coorte_retrospectiva` · `caso_controle` · `transversal` · `serie_de_casos` · `experimento_animal` · `experimento_in_vitro` · `estudo_post_mortem` · `manual_ou_consenso` · `outro`

### `desenho_estudo_bruto` — string, obrigatório

A string original como veio do PubMed. **Nunca descartada.** Hoje há 175 valores distintos em 237 registros; esse texto é a única prova do que foi lido e continua sendo a fonte para preencher e auditar o enum acima.

### `leva_origem` — string, opcional

Procedência de produção (ex.: `B1_v2`). Campo criado para receber o que hoje ocupa indevidamente o campo `uso`.

## 2.3 Campo a auditar antes de decidir

`citacao_confirmada` está `True` nos 237 registros. Já foi banido como via de portão no gate rev.A2. Esta proposta **não remove o campo** — remover campo sem norma é o mesmo erro que preencher sem norma. Fica marcado como `_pendente_decisao` até a origem ser auditada (Decisão 4).

---

# 3. NÍVEL 2 — VÍNCULO COM ANCORAGEM MULTI-ENTIDADE

Aqui está a mudança que motiva o pacote inteiro.

## 3.1 O que muda

**Hoje:** a âncora é uma string única — `secao_origem: "mecanismo_B1_neuroinflamacao/BLOCO_02"`. Um vínculo pertence a um mecanismo e a mais nada. Medido nos 274 vínculos: 92 valores distintos em três formatos — 232 `BLOCO_XX` puro, 30 prefixados com o mecanismo, 12 `APENDICE_CORPUS`. Todos dentro de B1; zero apontando para cenário, exame, biomarcador ou suplemento. *(v1.0 citava 21, que é a contagem nas fichas, não nos vínculos — ver errata.)*

**Proposta:** a âncora vira lista.

```json
"ancoras": [
  {
    "id_oficial": "mecanismo_B1_neuroinflamacao",
    "papel": "sustenta_mecanismo",
    "escopo": "BLOCO_02",
    "principal": true
  },
  {
    "id_oficial": "exame_il6",
    "papel": "sustenta_biomarcador",
    "escopo": null,
    "principal": false
  },
  {
    "id_oficial": "cenario_E5",
    "papel": "contextualiza_cenario",
    "escopo": null,
    "principal": false
  }
]
```

Uma evidência, três ancoragens, **um registro só**. Sem duplicação — exatamente o que o P20 exige e o que a sua regra de 14/09 determina.

## 3.2 Regras da âncora

1. `id_oficial` é validado contra `_ids_oficiais.json`. ID fora do catálogo = vínculo inválido. É a aplicação direta da precedência de nível 2 do P11.
2. `escopo` só é preenchido quando o domínio do ID tem subdivisão interna (BLOCO, para mecanismo). Para exame, suplemento e cenário, `null`.
3. Exatamente **uma** âncora com `principal: true` — é a entidade em cuja biblioteca a evidência foi trabalhada. As demais são relações declaradas, não posse.
4. `papel` tem enum fechado — ver §3.3.
5. Ancorar **não** promove nível de evidência. Uma âncora em `exame_il6` declara que a evidência fala daquele biomarcador; não afirma utilidade clínica dele.

## 3.3 `papel` — enum fechado

| valor | significa |
|---|---|
| `sustenta_mecanismo` | a evidência sustenta afirmação sobre a fisiopatologia daquela entidade |
| `sustenta_biomarcador` | a evidência trata do marcador como medida |
| `sustenta_intervencao` | a evidência trata de efeito de intervenção sobre a entidade |
| `contextualiza_cenario` | a evidência é pertinente ao recorte clínico do cenário |
| `refuta` | a evidência **contraria** a afirmação ancorada — achado negativo preservado |
| `fronteira` | pertence tematicamente a outra entidade; ancorado aqui por cross-reference declarado |

`refuta` existe por exigência da Filosofia: achado negativo não pode desaparecer porque não confirma.

## 3.4 O que isso resolve sozinho

Os **20 vínculos com `g2_elegibilidade: redirecionado_clinico`** hoje registram que o material saiu da trilha mecanística e não registram para onde. Com âncora em lista, redirecionar deixa de ser saída e vira **acréscimo de âncora**: a evidência ganha `papel: fronteira` apontando para a entidade clínica de destino, e continua no acervo, rastreável.

O campo `destino_sugerido`, exigido pelo *Como Executar* e ausente do arquivo, deixa de ser necessário — a âncora É o destino.

## 3.5 Campos preservados no vínculo

`id_vinculo` · `claim_id` · `id_referencia_interna` · `pmid_oficial` · `trecho_ancora` · `status_auditoria` · `status_referencia` · `verification_status` · `forca_causal` · `grau_maturidade` · `natureza_relacao` · `g1_metodo` · `g2_elegibilidade` · `g2_motivo` · `g3_notas` · `g3_verificado_por` · `data_verificacao` · `uso` · `evid_role` · `achado_central_molecular` · `extrapolacao_por_analogia` · `reancorado_em` · `nota_reparo`

`mecanismo_origem` e `secao_origem` permanecem durante a transição, como espelho da âncora principal, e só são aposentados quando o gate validar as duas fontes como idênticas em 100% dos registros.

## 3.6 Campo hoje vazio que o desenho torna obrigatório

`forca_biologica_conexao` está vazio em **274/274**. O gate rev.A2 já declara isso como dívida nomeada. Nesta proposta o campo é obrigatório quando a âncora principal tiver `escopo` em BLOCO_07 ou BLOCO_08 — que é exatamente onde o Bloco H o usa como critério de alto risco. Fora desses casos, permanece opcional.

---

# 4. DECISÕES NECESSÁRIAS DO RESPONSÁVEL

Nenhuma delas é minha para tomar.

### Decisão 1 — Duas trilhas de `uso`, ou uma

O acervo usa o enum v1.2 (clínico). O gate valida contra v3.1 (mecanístico). Ambos são schemas seus, ambos legítimos.

- **Opção A** — assumir as duas trilhas: `uso` passa a ter enum-união declarado, e o vínculo ganha `trilha: clinica | mecanistica` para dizer qual enum se aplica. Preserva os 244 registros como estão.
- **Opção B** — unificar em um enum só e remapear os 244.

*Recomendação:* A. O acervo não está errado; a régua é que estava trocada. E a trilha mecanística foi criada justamente porque as duas perguntas são diferentes.

### Decisão 2 — Os 30 registros com `review`

Revisão é desenho, não natureza. Para reclassificá-los é preciso ler cada um e dizer se a revisão é de literatura humana, pré-clínica ou mista. São 30 registros, trabalho de leitura, não de script.

*Decisão necessária:* reclassificar agora, ou manter `review` como valor transitório com data de expiração declarada.

### Decisão 3 — Ancoragem retroativa

O schema aceita N âncoras. Os 274 vínculos existentes têm uma. Popular as demais é trabalho de curadoria por vínculo.

*Decisão necessária:* B1 é retroancorado antes de B2 entrar, ou o schema vale só do próximo mecanismo em diante e B1 é retroancorado depois?

*Observação:* os 20 redirecionados são o subconjunto onde a segunda âncora já existe implicitamente no campo `g2_motivo` em texto livre — é o ponto de partida mais barato.

### Decisão 4 — `citacao_confirmada`

Preenchido `True` em 237/237 sem que se saiba quem preencheu. Auditar origem antes de decidir entre remover, ignorar ou normatizar.

### Decisão 5 — `status_auditoria` carrega dois vocabulários

Descoberto ao rodar o schema contra os dados. O mesmo nome de campo tem vocabulários diferentes nos dois níveis:

- **Nível 1 (referência):** `VALIDADO_G3_IA` — 165 registros
- **Nível 2 (vínculo):** `CONFIRMADO`, `PARCIALMENTE_CONFIRMADO`, `NAO_LOCALIZADO`, `CITACAO_INCORRETA`, `NAO_SUSTENTA_CLAIM`

Os dois são legítimos e significam coisas diferentes: no Nível 1 é o estado do processo de validação; no Nível 2 é o veredito sobre o suporte à frase. Mas com o mesmo nome, qualquer consulta que cruze os dois níveis quebra em silêncio.

*Decisão necessária:* renomear o de Nível 1 para `status_validacao`, ou manter o nome e declarar os dois enums formalmente.

---

# 4B. MAPA DE MIGRAÇÃO — MEDIDO, NÃO ESTIMADO

Os schemas foram executados contra o acervo B1 V7 real. O que falta para conformidade total:

## Referências (237)

| Item | Quantos | Natureza do trabalho |
|---|---|---|
| `natureza_evidencia` a preencher | 237 | automático em 207; **30 exigem leitura** (os `review`, Decisão 2) |
| `desenho_estudo` a preencher | 237 | semiautomático a partir do texto bruto, com revisão |
| `desenho_estudo_bruto` a preencher | 237 | **automático** — é cópia do campo atual |
| `status_auditoria` a separar | 162 | automático — separar veredito de ressalva em dois campos |
| `origem_pipeline` a separar | 50 | automático — separar categoria de data/observação |
| `verification_status` inválido | 1 | é a dívida de full-text já nomeada na fila P-6 |

## Vínculos (274)

| Item | Quantos | Natureza do trabalho |
|---|---|---|
| `ancoras` a criar | 274 | **automático na âncora principal** (derivada de `secao_origem`); âncoras secundárias são curadoria |
| `trilha` a declarar | 274 | automático — deriva do enum de `uso` já presente |
| `uso` = `B1_v2` a corrigir | 30 | automático — o valor vai para `leva_origem`; `uso` real vem da curadoria |

**Leitura honesta:** a maior parte da migração é mecânica. O trabalho humano real são três bolsões: os 30 `review`, os 30 de `B1_v2`, e a curadoria das âncoras secundárias — que pode começar pelos 20 redirecionados, onde a segunda âncora já existe em texto livre no campo `g2_motivo`.

## Erros meus que a execução pegou

Escrever a especificação como código executável e rodá-la contra os dados corrigiu quatro enganos meus antes da entrega: o padrão de ID rejeitava sufixos de desambiguação (`REF_CAPURON_2002b`), o enum de procedência não previa os valores reais, o campo de força de evidência não aceitava vazio, e eu havia removido `redirecionado_clinico` do enum de elegibilidade antes da transição terminar. Todos corrigidos nos arquivos entregues.

Especificação que não roda contra o acervo é opinião. Esta rodou.

---

# 5. O QUE ESTA PROPOSTA NÃO FAZ

- Não altera dado nenhum. Nenhum arquivo do acervo foi tocado.
- Não renomeia campo existente sem necessidade estrutural.
- Não remove campo. Nem `citacao_confirmada`, nem `secao_origem`.
- Não decide as 4 decisões acima.
- Não toca em conteúdo científico da Canônica.
- Não substitui o Módulo 09 nem o gate — estende o contrato que os dois já usam.

---

# 6. NOTA SOBRE ORGANIZAÇÃO POR TIPO DE ESTUDO

A proposta original previa pastas por tipo (Meta_Analises, RCT, Observacionais, Pre_Clinicos/Animais, Pre_Clinicos/In_Vitro).

Esta especificação mantém a estrutura de 5 arquivos do Módulo 09 e coloca a taxonomia inteira em campos, por três razões:

1. **P20.** Com `desenho_estudo` e `natureza_evidencia` em campo, pastas por tipo repetem o mesmo dado na estrutura de diretórios.
2. **Pasta congela um eixo.** Uma meta-análise de estudos de knockout é meta-análise *e* pré-clínica. Em pasta, escolhe uma. Em campo, é as duas.
3. **O Módulo 09 de 5 arquivos é normativo** no Prompt 4.2 e no Checklist de Auditoria Estrutural. Trocar a estrutura física obrigaria a revisar os dois.

Com os campos preenchidos, "todas as meta-análises humanas de B1" vira consulta de uma linha — sem mover arquivo nenhum.

---

*Proposta submetida para aprovação, revisão ou devolução. Nada aqui é normativo até decisão registrada.*


---

# 7. R2 — O CATÁLOGO OFICIAL NÃO EXISTE COMO ARQUIVO

Aceito, e é o achado mais sério do ciclo — mais que qualquer item de schema.

O nível 2 da hierarquia do P11 é o catálogo de IDs. Todo `id_oficial` de toda âncora valida contra ele. E ele não existe como objeto: é bloco JSON embutido dentro de um markdown.

**Critério de aceitação que a casa não declarou e que proponho como condição:** o derivador só é aceito quando o JSON produzido reproduzir **146 IDs válidos**, que é o total declarado pelo próprio catálogo e que confere na soma por categoria (48 de suplementos e complementares + 71 de exames e algoritmo + 16 mecanismos + 11 cenários). A trilha 25 parseou 103. A diferença de 43 é, até prova em contrário, blocos não capturados pelo parser — mas pode ser outra coisa, e um derivador que normalize 103 como se fossem 146 congelaria a perda em artefato oficial.

Sugestão de ordem: rodar o derivador, comparar contagem por categoria contra o bloco `contagem` do próprio catálogo, e só depois registrar sha e declarar fonte derivada.

# 8. R3 — A REGRA E2 TINHA O DEFEITO QUE DEVERIA IMPEDIR

O padrão que escrevi procurava as palavras `eutils`, `script` e `retrofit` em qualquer posição do campo. Mordeu `IA_casa (rito [AT]; abstract eutils colado no ledger AUD_B1_0238)` — avaliador humano legítimo cuja nota cita a ferramenta que trouxe o abstract. E como todo abstract do acervo veio de eutils, a regra tendia a morder justamente as fichas mais bem documentadas.

A casa está certa em recusar apagar informação para satisfazer regex.

**Solução adotada, em duas partes.**

Primeira: **a checagem sai do schema.** Presença de avaliador é restrição declarativa e fica no JSON Schema. Identidade do avaliador é julgamento sobre conteúdo e vai para o portão — pelo mesmo raciocínio do R1, invertido. Isto também remove uma incompatibilidade que eu não tinha notado: o modificador de case que usei não é válido no dialeto de regex previsto pelo JSON Schema, e só funcionava porque o validador em uso é Python.

Segunda: **o padrão do portão passa a ser ancorado ao valor inteiro** — casa quando o campo *é* a ferramenta, não quando a *menciona*:

```
^\s*(eutils|script|retrofit)[a-z0-9_]*\s*$     (comparação sem distinção de caixa)
```

Testado contra as 237 fichas e os 274 vínculos: **zero falsos-positivos**, e continua reprovando `eutils`, `eutils_automatico`, `script`, `retrofit`.

Terceira, opcional mas recomendada: o campo `g3_nota_metodo` foi criado nos dois schemas. Migrar a parte metodológica para ele deixa o identificador do avaliador limpo e torna a regra robusta independentemente do padrão.

**Registro para a casa:** o gate rev.A2 usa teste por substring no mesmo lugar. Hoje não morde porque os vínculos não carregam a nota. Quando a nota migrar para o vínculo, morde. Vale corrigir o padrão do gate junto, não depois.

# 9. DECISÃO 1 — O POINTER PEDIDO

O `SCHEMA-CLAIM v1.2` existe e não é nome informal do contrato do Prompt 4.2. É documento próprio, da trilha clínica, no kit que acompanha `COMO EXECUTAR v1.7`, `LISTA CANÔNICA B1/SM-02 v1.3`, `BLOCO DE ESTADO v1.6` e `PROTOCOLO DE ESCOPO B1 v1.3`.

Define, além do enum de `uso` que já discutimos, o campo `evidence_role` com exatamente quatro valores: `human_clinical`, `human_experimental`, `post_mortem`, `preclinical_mechanistic` — os mesmos quatro que aparecem no acervo, o que confirma por segunda via que `review` está fora de enum também ali, e não só contra a proposta.

**O que isso revela é maior que o pointer:** o repositório normativo da casa não tem os documentos da trilha clínica. Eles estão com o operador. Enquanto essa assimetria existir, a casa vai continuar medindo a trilha clínica contra réguas mecanísticas — que é exatamente a causa-raiz do caso `uso`, e não um episódio isolado dele.
