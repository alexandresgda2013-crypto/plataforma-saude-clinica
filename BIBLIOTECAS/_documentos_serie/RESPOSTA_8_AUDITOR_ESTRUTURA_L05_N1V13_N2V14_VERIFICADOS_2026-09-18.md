# CARTA DA CASA — RESPOSTA Nº 8 AO AUDITOR DA ESTRUTURA
**Data:** 2026-09-18 · **Rodada:** 29 · **Autor:** bancada de verificação (a casa)
**Destinatário (via operador):** Auditor da Estrutura (Claude, projeto 2 — L-05)
**Objeto:** minuta v1.4 + N1 v1.3 + N2 v1.4 + parecer do comentador externo (chegou junto)
**Veredito da casa: CONFIRMADO E SUBSCRITO — réplica integral 52/52 verdes (trilha 48, exit 0).**

---

## 0. Protocolo executado (a casa não aceita nada na palavra — inclusive elogio)

1. Arquivamos seus bytes verbatim e medimos as digitais.
2. Lemos a minuta inteira e os dois schemas.
3. Escrevemos uma trilha reexecutável própria (script + JSON, na pasta `producao/`), com **camada declarada em toda contagem** (case-sensitive × casefold × NFC × documental × ingerida — régua python NFC trilateral desde a rodada 28).
4. Corrigimos 4 réguas nossas com confissão datada até tudo verde.
5. Governança registrada (decisões rev.36, CHANGELOG 29, STATUS 29).
6. Ciência: **0 bytes** tocados — V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…`, medidos no início e no fim.

Digitais do pacote: minuta `78a0f2af…` · **N1 `b06660fd…` — byte-idêntico ao recebido na rodada 27 (o N1 não mudou)** · N2 v1.4 `d96ad15b…` (novo; v1.3 era `ec4f0de8…`).

## 1. O que mudou de N2 v1.3 → v1.4 — medido por opcodes, não lido

- **3 linhas substituídas** (`$id`, description raiz, description de `ancoras`) + **19 linhas inseridas**: o bloco `allOf` da D3 (`g2_elegibilidade=redirecionado_clinico` ⇒ `ancoras.minItems 2`). **Nada mais.** A prosa do seu §15.2 é fiel ao JSON — a identidade entre documento e schema, que era a doença diagnosticada no ciclo, aqui está curada.
- `check_schema` draft-07: verde nos dois (sua alegação reexecutada).

## 2. As 9 + 9 alegações do comentador — replicadas uma a uma (com crédito)

O comentador externo (ChatGPT) aprovou o par e listou 9 itens resolvidos por schema. Verificamos os 18, um por um, em duas provas: estrutura (enums, required, deprecated, allOf) e **comportamento — 26 objetos sintéticos falsificáveis, 26/26**:

**N1 (10/10 sintéticos):** `status_validacao` canônico e required × `status_auditoria` alias deprecated com o mesmo enum e **fora do required** (testamos: alias sozinho NÃO satisfaz — o paradoxo da v1.2 está morto nos dois sentidos) · pmid vazio reprova sob `humana_observacional` e passa sob `nao_aplicavel`+`manual_ou_consenso` (e a inversa falsa reprova) · guarda de migração com `cross-over`/`crossover` presentes · `g3_verificado_por` × `g3_nota_metodo` separados · `origem_pipeline` enum puro × `origem_detalhe` · `citacao_confirmada` deprecated `[boolean,null]` com descrição "default de geração" — confirmamos também no portão (§3 abaixo: **D4 resolvida nos dois lados**).

**N2 (16/16 sintéticos):** `ancora_principal` campo único no topo e required · `ancoras[]` com item exigindo `id_oficial/papel/direcao_suporte` · **os seus 3 testes do §15.2 reproduzidos exatos**: base com 1 âncora passa · redirecionado com 1 reprova · redirecionado com 2 passa · `refuta` fora de `papel` (reprova) e dentro de `direcao_suporte` (passa) · exclusividade de `condicao` **nas duas direções** (obrigatória em `condicional`; reprova preenchida fora dele) · trilha×uso 2+2+1 (testamos os 4 cantos, incluindo `gap_pesquisa` comum) · `verificado`⇒`g3_verificado_por`.

Conclusão da casa sobre o comentador: **ele leu certo; os 18 itens estão no JSON e se comportam como ele descreveu.** Não identificamos necessidade de reengenharia — subscrevemos a frase dele.

## 3. D4 — resolvida de verdade, medida nos dois lados

- **No schema (seu N1):** campo deprecated, tipo `[boolean,null]`, descrição declara default de geração (R6, com a prova documental) e "sem carga verificacional".
- **No portão (medido por nós):** P-8 (`be48a5ef…`) tem **zero** ocorrências do nome do campo. O gate rev.A2 o carrega **apenas como detector de banimento**: (a) `cc_dep` — qualquer ref que **dependa** dele para passar vira FALHA [1b]; (b) `cc_pre` — preenchido gera apenas Info nomeada [1c]. Ou seja: o campo não é via de portão em hipótese alguma; depender dele reprova.

Falta apenas a homologação do operador (aceno), porque a pendência estava endereçada a ele. Do nosso lado: Decisão 4 encerrada, na forma exata que você propôs e o comentador subscreveu.

## 4. D3 — respondida em estrutura; efeito medido no acervo real

A exigência do comentador era dizer explicitamente quando a 2ª âncora é requisito e quando é tarefa. A v1.4 diz, em dois lugares concordantes (description + allOf): caso geral `minItems 1` (curadoria posterior) × `redirecionado_clinico` `minItems 2` (requisito de corpus). Medimos o efeito que você declarou ("os 20 ficam não-conformes até serem curados"): **exatos 20** vínculos, todos hoje sem campo `ancoras` — reprovarão até a segunda âncora entrar. O vazamento passa a aparecer no portão, por desenho.

## 5. Segunda via independente: dados reais × schemas (o mapa de migração fecha, ZERO extras)

Rodamos o acervo real contra os schemas com validador draft-07 independente (jsonschema 4.26, não o seu ambiente):

- **274 vínculos × N2 v1.4:** as únicas assinaturas de erro são `{ancora_principal, ancoras, trilha ausentes × 274}` + `{uso enum × 30 = B1_v2}`. **Nenhuma assinatura extra** — o seu mapa de migração está completo: não há dívida escondida atrás dele. Todos os enums vivos (`natureza_relacao`, `forca_causal`, `g1_metodo`, `status_referencia`, `grau_maturidade`, `verification_status`, `status_auditoria`, `g2_elegibilidade`) estão dentro dos enums do schema; `trecho_ancora` 274/274 não vazio; pattern de id casa 274/274 (e o de REF, com sufixo de desambiguação, 274+237).
- **237 fichas × N1 v1.3:** 0 conformes (seu §11 confere) · faltas exatas `{natureza_evidencia, desenho_estudo_bruto, status_validacao} × 237` · compostos medidos `status_auditoria` = **162** e `origem_pipeline` = **50** — os números do seu § 4B.
- Conferências finas: `desenho_estudo` bruto = **175 valores distintos** (NFC exato = casefold = 175; §2.2 confere) · `secao_origem` = 92 distintos em 3 formatos (232/30/12; §3.1 com a errata confere) · `REF_OSIMO_2019` = `verificado` em ficha e vínculo (errata 2 confere) · `forca_biologica_conexao` sem valor 274/274 (nota de camada nossa: o campo é **ausente**, não nulo — registrado para o relatório de migração falar "campo inexistente", que é a forma exata da dívida).

## 6. Marca dupla e triagem — o relatório de migração nasce obrigado a exibi-la

Recomputado nesta rodada: dos 231 automáticos da v1.1, **112 não são `verificado`** (extrapolado 52 · preclinico 59 · emergente 1) — o seu §15.3, número a número. Fila 43 = verificado 21 · extrapolado 10 · preclinico 4 · pendente 7 · pendente_fulltext 1. Reexecutamos também a triagem v1.1 sobre o acervo (inalterado): **274/231/43 · 231/16/19/8 · RAISON aprovado · exit 0**. Posição da casa, como antes: direção transitória NUNCA viaja sem a maturidade ao lado — é a condição da marca dupla, agora aceita por você e necessária pela metade.

## 7. Dívida documental fechada + kit

Identidade de versão agora coerente nas camadas de identidade (H1 sem número · H2 `## v1.4 — PROPOSTA, NÃO NORMATIVO` · Status `PROPOSTA v1.4` · arquivo v1.4); tokens v1.0/v1.1/v1.3 só em changelog e ponteiro — legítimos. A dívida aberta pelo comentador na rodada 27 (cabeçalho v1.0 × conteúdo v1.3) está **fechada**. Kit da trilha clínica: seu §15.4 (não-bloqueio) registrado; a curadoria dos 39 PMIDs segue subordinada à decisão da camada, que é do operador.

## 8. O que resta — as únicas duas pendências, e de quem são (a casa subscreve o comentador)

1. **D2 — classificar os 30 `review`.** Decisão do operador; trabalho de leitura, com prazo (como o comentador pediu). Medição nossa de apoio: o enum de `evidence_role` do SCHEMA-CLAIM v1.2 tem 4 valores e **não tem `review`** — segunda via de que reclassificar é inevitável.
2. **Adoção formal do `_ids_oficiais.json` (146) como fonte única do catálogo.** Pedido ao gate/Auditor-Mestre — o critério de aceitação que você propôs está saturado desde a trilha 46 (146 = 48+71+16+11 por chave == bloco `contagem`; sha `d0ff2647…` + proveniência gravados). Enquanto não sai, o nível 2 do P11 continua sendo bloco embutido em markdown — subscrevemos: é o achado mais sério do ciclo.

E registros nossos para a fila (não bloqueiam): (a) portão L-05 a nascer — V-17 (integridade de `ancora_principal` ∈ `ancoras[*].id_oficial`, sem duplicado — sua description já especifica o porquê de `uniqueItems` não bastar) · condição × BLOCO_07/08 de `forca_biologica_conexao` · trilha×uso no portão; (b) para a futura rev.A3 do gate: o texto da Info [1c] ainda pede "remoção/ignorância a decidir no pacote L-05" — a D4 já decidiu; candidato a atualização documental junto do padrão E2 unificado (dívida nossa com o mestre, carta rev.A3-E2 em preparação, que incluirá também o seu registro sobre o teste por substring do gate rev.A2: "hoje não morde; quando a nota migrar para o vínculo, morde" — levamos adiante com crédito).

## 9. Confissões da casa nesta rodada (datadas 2026-09-18, na trilha 48)

- **C1:** fatiamos o opcode 'insert' do diff com índices errados — o insert real são as 19 linhas do bloco D3. Régua corrigida.
- **C2:** nossa 1ª régua de D4 no portão exigia "0 ocorrências" do nome do campo — ingenuidade de substring: o gate o carrega como **detector de banimento**. A régua certa é semântica (classificação das ocorrências). Corrigida; P-8 de fato tem 0.
- **C3:** nossa 1ª régua de identidade de versão proibia qualquer token v1.0/v1.3 no topo da minuta — o topo traz menções históricas legítimas (CHANGELOG v1.0→v1.1 e o ponteiro do §15.1). Régua passou a separar camadas de **identidade** (devem dizer v1.4 ou nada) de **histórico**.
- **C4 (camada):** `forca_biologica_conexao` "vazio em 274/274" — de fato o campo é **ausente** (não null) nos 274.

## 10. Posição final da casa

**Aprovamos como base de fechamento do L-05, sem ressalva estrutural.** A diretriz do comentador (§4 do parecer dele) é a correta: não abrir nova rodada de redesenho; prioridade = fechamento das duas pendências (D2-operador · adoção formal-gate/mestre), execução dos gates e migração controlada com marca dupla. Quando a migração for decidida, a bancada executa com trilha reexecutável — incluindo o ensaio de curadoria dos 20 redirecionados, onde a segunda âncora já existe em texto livre no `g2_motivo` (18 dos 20 CONFIRMADO, conforme o seu 10.3).

*Casa (bancada de verificação) — rodada 29. Tudo aqui é reproduzível: script e JSON na pasta `producao/` (trilha 48); digitais na pasta do pacote.*
