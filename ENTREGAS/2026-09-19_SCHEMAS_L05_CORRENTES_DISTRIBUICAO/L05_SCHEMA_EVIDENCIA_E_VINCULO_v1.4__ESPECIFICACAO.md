# L-05 — SCHEMA DE EVIDÊNCIA E VÍNCULO COM ANCORAGEM MULTI-ENTIDADE
## v1.4 — PROPOSTA, NÃO NORMATIVO — aguardando decisão do responsável pelo projeto

**Status:** PROPOSTA v1.4 — NÃO NORMATIVO. Não foi aplicado a nenhum dado.
**Identidade de versão:** nome do arquivo, título e status dizem o mesmo número. Na v1.3 diziam três coisas diferentes — ver §15.1.

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

**Proposta:** a âncora vira lista, e a principal sai de dentro dela.

```json
"ancora_principal": "mecanismo_B1_neuroinflamacao",

"ancoras": [
  {
    "id_oficial": "mecanismo_B1_neuroinflamacao",
    "papel": "sustenta_mecanismo",
    "escopo": "BLOCO_02",
    "direcao_suporte": "sustenta"
  },
  {
    "id_oficial": "exame_il6",
    "papel": "sustenta_biomarcador",
    "escopo": null,
    "direcao_suporte": "sustenta"
  },
  {
    "id_oficial": "cenario_E5",
    "papel": "contextualiza_cenario",
    "escopo": null,
    "direcao_suporte": "condicional",
    "condicao": "pertinência restrita ao subgrupo com marcador inflamatório elevado"
  }
]
```

Uma evidência, três ancoragens, **um registro só**. Sem duplicação — exatamente o que o P20 exige e o que a regra de 14/09 determina.

## 3.2 Regras da âncora

1. `id_oficial` é validado contra o catálogo oficial de IDs. ID fora do catálogo = vínculo inválido. É a aplicação direta da precedência de nível 2 do P11.
2. `escopo` só é preenchido quando o domínio do ID tem subdivisão interna. Para mecanismo, `BLOCO_XX[/sub]` **normalizado** — o prefixo do mecanismo mora em `id_oficial`, nunca no escopo. Valor reservado `APENDICE_CORPUS` para selos de índice. Para exame, suplemento e cenário, `null`.
3. **A âncora principal é campo do vínculo, não propriedade da âncora.** `ancora_principal` guarda o `id_oficial` da entidade em cuja biblioteca a evidência foi trabalhada. Como o campo é único por construção, "exatamente uma principal" deixa de ser invariante a contar e passa a ser cardinalidade de campo. `principal: true/false` dentro da âncora **não existe mais** — era a forma v1.0.
4. `ancora_principal` marca **contexto de curadoria**. Não implica posse nem precedência epistêmica sobre as demais âncoras.
5. `papel` e `direcao_suporte` são **eixos ortogonais**, ambos obrigatórios em toda âncora. Ver §3.3.
6. Ancorar **não** promove nível de evidência. Uma âncora em `exame_il6` declara que a evidência fala daquele biomarcador; não afirma utilidade clínica dele.

## 3.3 Dois eixos na âncora — `papel` e `direcao_suporte`

Separados por exigência do R7. Misturá-los foi o defeito da v1.0: `refuta` vivia dentro de `papel`, o que permitia a um motor ingênuo ler `papel: sustenta_intervencao` como veredito de eficácia.

### `papel` — relação temática, nunca veredito

| valor | significa |
|---|---|
| `sustenta_mecanismo` | a evidência trata da fisiopatologia daquela entidade |
| `sustenta_biomarcador` | a evidência trata do marcador como medida |
| `sustenta_intervencao` | a evidência trata de efeito de intervenção sobre a entidade |
| `contextualiza_cenario` | a evidência é pertinente ao recorte clínico do cenário |
| `fronteira` | pertence tematicamente a outra entidade; ancorado aqui por cross-reference declarado, ou selo de índice |

`refuta` **saiu deste enum**. O prefixo `sustenta_` nomeia o assunto, não o desfecho: `sustenta_intervencao` significa "esta evidência é sobre uma intervenção", nunca "esta intervenção funciona".

### `direcao_suporte` — eixo epistêmico

| valor | significa |
|---|---|
| `sustenta` | a evidência apoia a afirmação ancorada |
| `refuta` | a evidência **contraria** a afirmação — achado negativo preservado |
| `inconclusivo` | a evidência toca o tema sem decidir |
| `condicional` | apoia sob restrição declarada — exige o campo `condicao` |

`refuta` aqui é mais forte do que era dentro de `papel`: fica num eixo que o motor é obrigado a ler, em vez de escondido numa lista de assuntos.

**Regra normativa que acompanha os dois eixos:** o veredito sobre o que a evidência sustenta e com que força mora em `trecho_ancora` + `natureza_relacao` + `forca_causal` + `direcao_suporte` + `verification_status`. Motor e leitor humano são proibidos de inferir eficácia ou direção a partir de `papel` isolado.

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
| `verification_status` inválido | 0 | **era 1 — `REF_OSIMO_2019`, valor livre com typo, não a dívida de full-text (ver errata 2). Corrigido pela casa na errata T25 de 2026-09-14, manifesto 2.10. Medição de 15/09: zero inválidos.** |

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

> **ATUALIZADO em 2026-09-17 — critério satisfeito.** O derivador da casa (trilha 46) reproduz **146 = 48 + 71 + 16 + 11**, idêntico por chave ao bloco `contagem` do próprio catálogo, 146 distintos, zero duplicados, 5 removidos. Artefato candidato gravado com sha e arquivo de proveniência.
>
> A causa dos 103 está escrita: o catálogo-fonte é JSON inteiro, e a camada de texto subconta por desenho — suplementos, cenários e mecanismos não têm prefixo capturável. Parser de texto rende 103; regex de prefixo rende 74; só a estrutura reproduz 146.
>
> **O que falta é adoção formal**, não medição: o gate ou o Auditor-Mestre declarar o `.json` derivado como fonte única do catálogo. Enquanto isso não acontecer, o nível 2 da hierarquia do P11 continua sendo bloco embutido em markdown — e este documento continua registrando isso como o achado mais sério do ciclo.

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

**O que isso revelava era maior que o pointer:** o repositório normativo da casa não tinha os documentos da trilha clínica, e por isso media trilha clínica com régua mecanística — causa-raiz do caso `uso`, não episódio dele.

> **ATUALIZADO em 2026-09-17.** Resolvido. O operador entregou o kit completo em 15/09 e a casa o ancorou byte a byte em 16/09, 9 de 9. Este parágrafo ficou no documento depois de perder a validade — a mesma falha de documentação atrasada que a minuta diagnostica em outros. Mantido com a correção à vista em vez de apagado.


---

# 10. CHANGELOG v1.1 → v1.2 E RESPOSTA ÀS TRÊS LINHAS PENDENTES

## 10.1 O que mudou

| Mudança | Motivo |
|---|---|
| **§3 reescrito na forma R1+R7** | Erro meu, e do tipo que venho apontando nos outros. O CHANGELOG da v1.1 declarava R1 e R7 incorporados, os JSON já estavam certos, e a prosa do §3 ficou na forma v1.0 — com `principal: true` no exemplo, a regra de contar principais, e `refuta` ainda dentro de `papel`. Especificação atrás da implementação, exatamente o que diagnostiquei como doença do projeto na segunda mensagem deste ciclo. A casa ampliou o achado para o R1; a ampliação procede. |
| **`direcao` → `direcao_suporte`** | Adotado o nome do Contrato da Cadeia L-05 1.1. Ver §10.2. |
| **N1: `status_auditoria` → `status_validacao`**, com o nome antigo mantido como alias `deprecated` | Decisão 5 executada em vez de adiada. Ver §10.4. |
| **Guarda determinística de migração em `natureza_evidencia`** | Ponto 3 do comentador externo, adotado com a redação da casa. |
| **V-17 declarado na descrição de `ancora_principal`** | Ponto 2 aceito: presença é declarativa, integridade é de portão. |

## 10.2 Linha (iii) — colisão de nomes: adoto `direcao_suporte`

Palavra dada para a dívida `D-L05-NOMES-DIRECAO` morrer.

O contrato já tinha feito o que eu recomendei na carta anterior: qualificar o nome enquanto nenhum registro carrega o campo. `direcao_suporte` é autodescritivo, não colide com o sentido de aresta do grafo, e portanto **dispensa renomear o lado da ontologia** — `sentido_relacao` deixa de ser necessário como desambiguador. Um nome resolvido em vez de dois nomes convivendo.

## 10.3 Linha (i) — âncora principal nos 20 redirecionados: confirmado

Principal fica `sustenta_mecanismo` na entidade de origem; o destino entra como segunda âncora com `papel: fronteira`.

Conferi antes de confirmar, porque `sustenta_mecanismo` num vínculo julgado inelegível parecia contraditório. Não é: 18 dos 20 estão `CONFIRMADO` contra frase real da canônica. O redirecionamento é sobre pertencimento epistemológico, não sobre suporte. Exceção já acordada no R4: os 12 `APENDICE_CORPUS` nascem com `papel: fronteira` na própria principal — medido, zero interseção com os 20.

## 10.4 Linha (iv-bis) — `status_validacao`: executado agora, com espelho

A carta 2 dizia que renomear quebraria três scripts e dezesseis bibliotecas; a carta 4 adere ao renomear. As duas posições se reconciliam por um fato que mudou no meio: **o campo de N1 vai ser reescrito de qualquer jeito** — 162 fichas têm veredito e ressalva grudados e serão separadas em dois campos. O custo em dado é marginal; o custo real está nos scripts.

Por isso o nome antigo permanece no schema como alias `deprecated`, pela mesma liturgia de espelho já usada em `secao_origem`/`mecanismo_origem`: os dois campos coexistem, o portão mede identidade, e o antigo só é aposentado quando a medição der 100%. Nenhum script quebra de forma atômica.

## 10.5 Linha (ii) — triagem de `direcao_suporte`: mantenho a recusa

A carta 4 repete a regra original (`CONFIRMADO` ou `PARCIALMENTE_CONFIRMADO` → `sustenta`, 273 de 274, exceção `VINC_B1_0047`). Suponho que tenha sido escrita antes da minha resposta chegar. Repito com o dado, porque é o único item aberto de substância.

`REF_RAISON_2013` está `CONFIRMADO` nos dois vínculos em que aparece. Pela regra, os dois seriam gravados `sustenta`. O `g3_notas` deles diz: negativo na amostra toda, resposta só no subgrupo com marcadores basais altos. E o molde do Adendo nº 1 diz que Raison é `condicional`.

A regra grava `sustenta` no registro que fez o valor `condicional` existir.

**Regra alternativa, em três linhas:**

1. `CONFIRMADO` sem sinal de qualificação nas notas → `sustenta`, transitório datado.
2. `CONFIRMADO` com sinal → `__PENDENTE__`, fila humana.
3. `PARCIALMENTE_CONFIRMADO` → nunca automático. É a vizinhança semântica de `condicional`.

**Critério de aceitação falsificável:** qualquer triagem só é aceita se `REF_RAISON_2013` não sair `sustenta`. Se sair, a regra está errada por mais registros que ela acerte.

# 11. RELATÓRIO DE EXECUÇÃO — v1.2 CONTRA O ACERVO B1 V7

Migração simulada em cópia, zero bytes escritos. Ambos os schemas passam em `check_schema` draft-07.

## Nível 2 — 274 vínculos

| | Regra da casa | Regra desta minuta |
|---|---|---|
| conformes mecanicamente | 243 | **155** |
| `direcao_suporte: sustenta` automático | 273 | **172** |
| enviados à fila humana | 1 | **102** (82 `CONFIRMADO` com sinal · 19 `PARCIALMENTE_CONFIRMADO` · 1 `NAO_LOCALIZADO`) |
| `uso`/`trilha` pendentes (`B1_v2` → `leva_origem`) | 30 | 30 |
| `ancora_principal` fora do catálogo | 0 | 0 |

**A diferença de 88 registros é o preço de não gravar veredito epistêmico por derivação.** Está declarada, não escondida, e é reversível: se a leitura humana confirmar que a maioria dos 82 é mesmo `sustenta`, eles entram depois com autoria registrada.

**Teste de aceitação:** `VINC_B1_0128` e `VINC_B1_0173` (Raison) saem `__PENDENTE__`. Aprovado.

## Nível 1 — 237 fichas

| | Medida |
|---|---|
| conformes com mecânica conservadora | 0 |
| `desenho_estudo` pendente | 237 |
| `natureza_evidencia` pendente | 163 (133 pré-clínicas a separar in vivo/in vitro · 30 `review`) |
| guarda intervencional acionada | 0 de 66 — confere com a medição da casa |
| `status_validacao` + nota separados | 162, sem resíduo |
| `origem_pipeline` + detalhe separados | 50, incluindo a linha de mapa da casa para `AT_AUDITORIA_EXTERNA_*` |

Os 0 conformes de N1 contra os 24 da casa não são divergência: a casa classificou automaticamente as 40 fichas com sinal forte de desenho, e esta simulação deixou as 237 em `__PENDENTE__` de propósito. A diferença é deliberadamente conservadora, pelo mesmo princípio do item anterior.


---

# 12. CHANGELOG v1.2 → v1.3 — OS OITO FECHOS

Todos verificados por teste sintético: **11/11 conforme**. Ambos os schemas passam em `check_schema` draft-07.

| Fecho | Origem | Tratamento |
|---|---|---|
| **Paradoxo do alias no N1** | bancada, Adição A | Defeito meu. Na v1.2 o `required` continuou apontando para `status_auditoria` — alias required sem enum — enquanto o canônico `status_validacao` ficou fora do required. Inverso do alvo: o valor composto passava e o campo limpo podia faltar. Corrigido: required no canônico, alias fora do required e com o mesmo enum legado. |
| **Exclusividade de `condicao`** | comentador, ponto 1 | Aceito no schema, não no portão — a regra é expressável em draft-07 nos dois sentidos. `condicao` obrigatória em `condicional` e proibida (`null`) em `sustenta`, `refuta` e `inconclusivo`. |
| **`pmid_oficial` vazio** | comentador, pós-JSON §2.3 | Aceito. Vazio só sob `nao_aplicavel`, por `allOf`. A inversa — `nao_aplicavel` exigir vazio — deixo em aberto de propósito: há consenso formal com DOI e sem PMID. |
| **`sentido_relacao` fora do schema** | comentador, ponto 2 | Aceito, e o argumento é o correto: zero registros carregam o campo, então decidir era decidir sem lastro. Retirei as duas cláusulas. O schema agora só afirma que o campo do L-05 se chama `direcao_suporte`. O nome do eixo de aresta é do contrato do grafo. |
| **`redirecionado_clinico` ≠ `fronteira` automático** | comentador, ponto 3 | Aceito, e corrige a minha linha (i). Eu havia confirmado `fronteira` para a âncora de destino como se decorresse do fluxo. Não decorre: 17 dos 20 têm `uso: clinico`, e derivar o papel do `g2_elegibilidade` apagaria exatamente a informação que o `uso` carrega. O papel da âncora de destino é decidido pela **função da evidência na entidade de destino**. |
| **Texto de `uso` (2+2+1)** | comentador, pós-JSON §3.4 | Aceito. "3 primeiros + 3 últimos" lia-se como 3+3. Agora: clínica = {clinico, contexto_mecanistico} · mecanística = {nucleo_causal, suporte_correlacional} · `gap_pesquisa` comum às duas. |
| **`cross-over` na guarda** | bancada, fino 1 | Restituído. Impacto hoje 0/237; valor é preventivo para B2–B16. |
| **`forca_biologica_conexao` ao portão** | bancada, fino 2 | Declarado. A regra depende do escopo da âncora *principal*, portanto é referência cruzada entre campos e não é expressável em draft-07 — mesma simetria do V-17. |
| **Medições fora das descriptions** | comentador, pós-JSON §2.4 | Aceito, e o princípio é o da própria casa: medida sem comando gravado não vale, e em texto normativo o comando se perde. As duas instâncias saíram; a regra ficou, a contagem foi para o relatório datado. |
| **Rótulo "PENDENTE DE DECISAO" em `trilha`** | comentador, observação final | Decisão 1 registrada (Opção A). Rótulo removido. |

# 13. RELATÓRIO DE EXECUÇÃO DA TRIAGEM — 172/102

Pedido formal reiterado duas vezes. Entregue como script reexecutável, não como número.

```
python3 triagem_direcao_suporte.py <pasta_atuais> --json relatorio.json
```

Stdlib pura, somente leitura, exit 1 se o teste de aceitação falhar.

**Execução sobre o V7b:**

| | |
|---|---|
| vínculos lidos | 274 |
| automáticos (`sustenta`) | **172** |
| fila humana (`__PENDENTE__`) | **102** |
| regra 1 — `CONFIRMADO` sem sinal | 172 |
| regra 2 — `CONFIRMADO` com sinal | 82 |
| regra 3 — `PARCIALMENTE_CONFIRMADO` | 19 |
| regra 0 — status não triável (`NAO_LOCALIZADO`) | 1 |

**Por que a bancada não conseguiu reverter os 102:** nenhuma soma de `status_auditoria` × `verification_status` fecha 102, porque o segundo fator não participa da regra. O que separa os 82 dos 172 é um screening de texto sobre `g3_notas` + `trecho_ancora`, e essa regra não estava publicada — só o número estava. Erro meu de método, do mesmo tipo que venho apontando. O script agora carrega a regex inteira e o motivo por registro.

**Teste de aceitação:** `VINC_B1_0128` sai por `negativ`, `VINC_B1_0173` sai por `so no`. Nenhum dos dois vira `sustenta`. Exit 0.

O JSON acompanha a lista nominal dos 102 e dos 172, cada um com o motivo e o marcador que o disparou — verificável um a um.


---

# 14. TRIAGEM v1.1 — UM DEFEITO NA MINHA PRÓPRIA REGRA

A casa mediu que, dos 172 automáticos, 58 não são `verificado` (49 pré-clínicos · 5 extrapolados · 3 pendentes · 1 emergente) e propôs marca dupla no relatório de migração. Fui verificar e encontrei duas coisas — a segunda contra mim.

## 14.1 Regra 4 — verificação pendente não gera direção

Três vínculos saíam `sustenta` com `status_auditoria: CONFIRMADO` e `verification_status: pendente`: `VINC_B1_0259`, `VINC_B1_0268`, `VINC_B1_0270`. Par contraditório — a citação sustenta a frase, mas a verificação não concluiu. Regra 4 avalia isso primeiro. Captura 8 no total, contando os `pendente_fulltext` que já estavam na fila por outra via.

## 14.2 O sinal `extrapol` não deveria existir — e o defeito não é rigor, é inconsistência

A casa observou que `EXTRAPOL` dispara 66 dos 82 da regra 2. Fui ver por quê.

Extrapolação **já tem dois campos próprios**: `extrapolacao_por_analogia`, preenchido em **274 de 274**, com valores como `sim (camundongo)` e `parcial`; e `verification_status`, com `extrapolado` em 62. Rastrear o mesmo fato na prosa duplica o campo — P20, dentro do meu próprio script.

E o efeito medido é pior que duplicação. A regra mandava **62 vínculos** para a fila por mencionarem extrapolação nas notas, e deixava passar **78** cujo campo próprio a declara em silêncio. Dos 62 mandados, 60 tinham o campo declarado e 57 já carregavam `extrapolado` ou `preclinico` no `verification_status`. Ou seja: eu não estava sendo conservador com a extrapolação. Estava sendo conservador com quem a escreveu por extenso.

Inconsistência é pior que rigor ou frouxidão, porque torna a fila arbitrária — e fila é orçamento de leitura humana.

`extrapol` sai dos sinais. A limitação continua registrada, nos dois campos que existem para ela, e é exatamente onde a marca dupla proposta pela casa deve lê-la.

## 14.3 Reexecução, no protocolo pedido pela casa

Regras republicadas no cabeçalho do script · mesmo critério de aceite · contagem nova datada · efeito nomeado.

| | v1.0 (16/09) | v1.1 (17/09) |
|---|---|---|
| automáticos | 172 | **231** |
| fila humana | 102 | **43** |
| regra 1 — sem sinal | 172 | 231 |
| regra 2 — sinal | 82 | 16 |
| regra 3 — parcialmente confirmado | 19 | 19 |
| regra 4 — verificação pendente | — | 8 |
| **teste RAISON** | aprovado | **aprovado** |

Raison continua saindo por `negativ` e `so no`; nunca dependeu de `extrapol`.

**O sentido da mudança merece ser dito com todas as letras:** esta é a primeira vez neste ciclo em que eu afrouxo em vez de apertar, e afrouxo 59 registros. Não é recuo de princípio. O que muda é que a restrição desses 59 passa a ser lida onde ela está declarada — em campo estruturado, por todos os registros que a têm — em vez de onde ela por acaso foi mencionada. Se a casa preferir manter a v1.0 enquanto avalia, os dois relatórios estão publicados e são reexecutáveis lado a lado.

## 14.4 Ressalva do comentador — adotada

`sustenta` da regra 1 é **saída transitória de triagem**, nunca veredito definitivo. O fluxo é triagem → transitório → portão/auditoria → definitiva. Com a v1.1 isso vale para 231 registros em vez de 172, o que aumenta o peso da ressalva em vez de diminuí-lo.

## 14.5 Sinais adicionais (§6 do comentador) — concordo que é futuro, com o protocolo já fixado

"depende de", "não associado", "resultados mistos" são boas candidatas. Mas a lição do `extrapol` vale como critério de admissão: **um sinal só entra se não existir campo estruturado que já carregue o mesmo fato.** Antes de ampliar a regex, vale varrer o schema por campo equivalente — senão amplia-se a fila com trabalho que o dado já responde.


---

# 15. v1.3 → v1.4 — FECHOS DA RODADA 27

## 15.1 Identidade de versão — o defeito estava na capa

O comentador apontou, e é constrangedor: o título dizia `v1.0 — PROPOSTA`, o campo de status dizia `v1.3`, e o nome do arquivo dizia `v1.0_PROPOSTA`. Três camadas, três números.

É a mesma doença que o Auditor-Mestre achou no H1 da V2.1, e a quinta vez neste ciclo em que eu cometo a versão pessoal do defeito que o documento diagnostica. As três camadas agora dizem o mesmo número, e o nome do arquivo foi corrigido junto — nome de arquivo é a primeira coisa que alguém lê e a última que alguém atualiza.

Adotada a normalização proposta: `v1.4 — PROPOSTA, NÃO NORMATIVO`.

## 15.2 D3 — âncora secundária: requisito ou curadoria? Resposta estrutural

O comentador exigiu que o fechamento diga explicitamente se a âncora secundária é requisito de corpus ou tarefa posterior. A resposta é: **as duas coisas, e a fronteira é declarável em schema**.

- **Caso geral:** curadoria posterior. `minItems: 1` basta. Exigir segunda âncora de todos os 274 transformaria o schema num mandato de trabalho que ninguém orçou.
- **`g2_elegibilidade: redirecionado_clinico`:** requisito de corpus. `minItems: 2`, por `allOf`.

O motivo é o vazamento que este documento existe para fechar. Nesses 20 registros, a âncora principal sozinha perde a informação de para onde a evidência foi redirecionada — e o redirecionamento volta a ser uma saída sem destino, que foi o achado original do §3.4.

Testado: vínculo comum com uma âncora passa; redirecionado com uma âncora reprova; redirecionado com duas passa.

**Efeito medido:** os 20 ficam não-conformes até serem curados. É deliberado. Faz o vazamento aparecer no portão em vez de permanecer invisível, e dá aos 20 um critério de pronto.

## 15.3 Marca dupla — aceita, e o argumento ficou mais forte com a v1.1

Na v1.0 eram 58 de 172 não-verificados. Na v1.1 são **112 de 231**, quase metade. A proposta da casa — direção e maturidade lado a lado no relatório de migração — deixa de ser refinamento e passa a ser necessária: sem ela, metade do `sustenta` transitório esconde maturidade pré-clínica ou extrapolada.

Isso reforça a ressalva do §14.4 em vez de enfraquecê-la, e é o preço declarado de ter tirado a extrapolação do screening de texto. A restrição não sumiu; mudou de lugar para onde é lida por todos os registros, e o relatório precisa exibi-la.

## 15.4 Kit da trilha clínica

Não é necessário para fechar o L-05 — a casa já ancorou as nove peças e a medição do `evidence_role` foi feita na fonte primária. Passa a ser útil quando a trilha clínica voltar a produzir, que é quando a régua de `uso` sai do papel. Fica a critério do operador; não é bloqueio meu.
