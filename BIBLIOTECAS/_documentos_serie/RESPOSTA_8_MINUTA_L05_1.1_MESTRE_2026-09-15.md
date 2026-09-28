# RESPOSTA Nº 8 — MINUTA L-05 1.1 (CONTRATO DA CADEIA DO MOTOR) — VERIFICAÇÃO DA CASA

**Data:** 2026-09-15 · **De:** casa (verificação empírica antes de aceitar) · **Para:** Auditor-Mestre
**Trilha:** `producao/29_verificacao_minuta_1.1_mestre_e_comentador_2026-09-15.json` (regex, escopo, chave e comandos gravados)
**Método anunciado na rodada 12 e cumprido aqui:** a minuta da casa é **bancada de verificação** do 1.1 dele — cláusula a cláusula contra a V2, os schemas e o acervo. Não se criam duas normas concorrentes.

---

## 1. Objeto e integridade

- Minuta recebida: `L05_1.1_CONTRATO_CADEIA_MOTOR_minuta1_2026-09-15.md`, sha256 `f91042b7fee82d0fbf537b7e848f6d37a782181738ff69ce97e3f69f7ac6b14d` (241 linhas). **Arquivada verbatim** em `_documentos_serie/L05_1.1_minuta_mestre_recebida_2026-09-15/`.
- A V2 que ela cita (`09692e18…`) **confere** com o sha medido hoje: `09692e18a5a65958bde4545ed6ff804c21c5945411159988654c7664c8a4a4e2`.
- B1 V7 intacta: sha `6e2c2979…` (recomputado nesta rodada). **Ciência tocada nesta rodada: 0 linhas.**

## 2. Parte 0 — REPRODUZIDO EXATO. Pointer "158/405" ENCERRADO

Rodei o método publicado na Parte 0, exatamente como declarado:

| Medida dele | Réplica da casa | Resultado |
|---|---|---|
| 102 linhas-lote (`*`…`*` contendo `[`) | 102 | ✔ exato |
| 405 prefixos distintos (regex dele, chave group(1), só nas lotes) | 405 | ✔ exato |
| 247 resolvem / 158 não-resolvem (por prefixo; 1º segmento maiúsculo como substring em algum `id_referencia_interna`) | 247 / 158 (soma 405) | ✔ exato |
| 158 são "temáticos" | amostra: `A1BLOCK, AQP4, AMIGDALA, ANSIEDADE, ARCTIGENIN, ASTROSWITCH, BBB, BIFIDO, CCL2, CCR2` | ✔ de fato não são sobrenomes |

A explicação das "4 camadas" como **4 lugares** do mesmo código `[XX]` também confere com a medição: (a) prosa com `[XX]` fora das lotes = apenas **7 pares** AUTOR_ANO distintos (11 ocorrências); (b) linha-lote = 405; (c) Módulo 09 = 201/33/3 (OB/MA/EC); (d) desenho em texto livre = o resíduo que a v1.1 formalizou como `desenho_estudo_bruto`. **O pointer que a casa pediu na rodada 12 está respondido por réplica, não por argumento** — precedente 71×84 fechado a favor dele.

Registrado o aceite dele da errata do delimitador (**94→91**), que sobrevive à mudança de regime exatamente como prevíamos: muda o rótulo, não o fato.

## 3. ERRATA DA CASA (confissão datada): o nosso "446" não é rederivável

A trilha 28 registrou "446 tokens AUTOR_ANO distintos, regex declarada" — **mas não gravou a regex nem o comando**. Hoje rodei, sobre a V7 (sha intacto), uma grade inteira: {regex dele × regex do P-8} × {escopos: inteiro, pré-REGISTRO, só-lotes, sem-lotes} × {chaves: g1, g1+g2, g1+g2+g3} × {códigos `{2}`, `{2,3}`} + variantes (lowercase, ano de 4 dígitos). Nada dá 446; os mais próximos são **474** (regex dele, g1+g2, arquivo inteiro) e **477** (regex do P-8, g1+g2).

**Confissão:** o número 446 é **não verificável no estado** e a falha é nossa — uma medida sem comando gravado viola a própria norma da casa. Sem efeito material (a V-15 é medida **por item**, não por população), mas sem desculpa. **Lição incorporada, a partir do exemplo da Parte 0 dele:** toda medida da casa passa a gravar regex + escopo + chave + sha no mesmo registro. Os números canônicos ficam: **405** (escopo-b, dele, replicado) · **474/477** (arquivo inteiro, por regex declarada) · **675** marcadores `[XX]` (replicado exato).

## 4. Verificação cláusula a cláusula

**D-01 · escada de 7 degraus + preservar concorrentes:** APROVADO sem reabertura. É a restrição do comentador implementada com ordem total (determinismo pela ordem, não por tabela de autoridade) e saída honesta quando nada resolve (`conflito_nao_resolvido` + dois IDs). **Uma precisão de fato no §3** — ver F-1.

**D-02 · teto por eixo:** APROVADO. A formulação é da casa (carta 7) e ele a adotou com crédito — registrado. O teste negativo (eixo vazio → `indefinido`, nunca herda o mais forte) fecha a última porta de elevação silenciosa. **Uma precisão de fato no §4** — ver F-2.

**D-03 · lacunas tipadas:** APROVADO **com a correção do comentador incorporada** (§5). Nota da casa: o fechamento fica **machine-verificável** porque o schema_vinculo v1.1 **já tem** `natureza_relacao ∈ {…, nao_estabelecida}` — proponho que `inexistencia_cientifica` só seja emitível quando existir relação canônica auditada marcada `nao_estabelecida` (ou `status_epistemologico = lacuna` registrado). Ausência de recuperação nunca gera esse tipo.

**D-04 · templates:** APROVADO. O teste de diferença de conjunto (afirmações do laudo − afirmações das unidades = ∅) é de fato o mais importante da minuta; a casa o adota como requisito de aceite do Motor.

**D-05 · três testes de granularidade:** APROVADO. A dependência humana assumida por ele (em vez de regra automática fingida) fica registrada como risco aceito. O multiplicador de escala — 146 IDs do catálogo — confere com a `contagem` do catálogo oficial.

**D-06 · Pasta segregada:** APROVADO. Verificado que a **adição do comentador (rastro de consulta/apresentação) já está incorporada** no texto dele — a via bilateral de adições externas funcionou dentro do próprio ciclo.

**D-07 · determinismo:** APROVADO **com a qualificação do comentador incorporada** (§5). Redação proposta pela casa: *"o conteúdo clínico, semântico e estrutural do resultado — incluído o conjunto de versões declaradas — deve ser deterministicamente reproduzível; compõem envelope não-semântico, fora do hash, apenas itens de lista fechada (timestamp de execução, id de execução, logs técnicos)"*.

**D-08 · hierarquia de segurança:** APROVADO com a cobertura parcial declarada por ele (só os 2 níveis superiores testáveis até a fase multidomínio). Lacuna de teste conhecida, não defeito de contrato — registro igual ao dele.

**Parte 3 (cláusula de fecho) e Parte 4 (o que a minuta não faz):** APROVADAS. A cláusula de fecho é a regra de ouro do operador, e as três dependências nomeadas (taxonomia v1.1, `status_epistemologico`, `condicao`/`contexto`) batem 1:1 com as filas nomeadas da casa — `status_epistemologico` foi proposto por nós na carta 7 e permanece oferecido com os 7 valores declarados.

## 5. Os 4 pontos do comentador externo — verificados um a um e ADOTADOS COM CRÉDITO

Pela política da casa, ele foi verificado **contra o texto e contra os schemas** antes de qualquer aceite. Nenhum dado fabricado; os números que ele cita (197/30/24) batem com nossas medidas.

1. **D-02 — não congelar os 5 eixos como vetor homogêneo.** PROCEDENTE E CORROBORADO empiricamente (ver F-2): os eixos não são homogêneos — 2 são da ficha N1, 3 são do vínculo N2. A regra de não-elevação está aprovada; a semântica de composição (propagado / herdado / recalculado / limitante / metadado) fica para a etapa de schema, e a casa contribui a proposta da seção 7.
2. **D-03 — `inexistencia_cientifica` restrito.** PROCEDENTE: o gloss da minuta ("a ciência não estabeleceu a relação") era mais largo que o necessário; a restrição dele fecha o deslize e a âncora formal já existe (`natureza_relacao = nao_estabelecida`). Adotado.
3. **D-07 — determinismo qualificado.** PROCEDENTE tecnicamente: "byte a byte" sem exceção de envelope torna o requisito intestável ou proíbe metadado útil. Adotado com a redação da seção 4/D-07 acima.
4. **Parte 1 — "As entradas autorizadas do Motor são:".** PROCEDENTE (a tabela mistura tipos heterogêneos de entrada) **com uma condição da casa:** manter verbatim a frase negativa — **"Não consome: a prosa da Biblioteca Canônica (§28 da V2)"** — porque é ela que dá força vinculante ao fechamento (lista exaustiva + exclusão explícita).

Concordado com ele em **não reabrir** D-01 (só a precisão F-1), D-04, D-05, D-06 e D-08.

## 6. Precisões de FATO da casa (errata técnica — nenhuma reabre semântica)

- **F-1 · D-01 §3, "campos que já existem":** inventário real na v1.1 — `natureza_evidencia` existe (ficha N1) e `grau_maturidade` existe (vínculo N2); `condicao` existe apenas como exigência condicional dentro de `ancoras[]` (hoje esparsa); **`contexto` não existe** em schema nem em dado (grep nulo); **`sentido_relacao` não existe como campo** (aparece só na nossa governança; é conceito da ontologia futura); e o campo epistêmico real chama-se **`direcao`**, não `direcao_suporte`. O §4 da própria D-01 ("é requisito de schema, derivado do contrato") já diz o correto — pede-se 1 linha de ajuste no §3 para não prometer campo inexistente.
- **F-2 · D-02 §4, "a v1.1 já os tem":** verdade no nível **plataforma**; no **vínculo** só existem `forca_causal`, `grau_maturidade` e `trilha`. `natureza_evidencia` e `desenho_estudo` moram na **ficha N1**. É a prova material de que a composição não pode ser homogênea — eixo de evidência viaja por herança (`id_referencia_interna`), eixo de relação viaja por propagação.
- **F-3 · nomenclatura de direção:** a casa mantém a distinção `sentido_relacao` (grafo, futuro) × eixo epistêmico; para o eixo epistêmico vale decidir, **na etapa de schema**, entre renomear `direcao` → `direcao_suporte` ou publicar dicionário oficial. **Dívida nomeada: D-L05-NOMES-DIRECAO.** Não bloqueia a minuta 2.

## 7. Proposta da casa para a semântica por eixo (apoio à etapa de schema; NÃO congela agora)

| Eixo | Origem real | Natureza | Semântica de composição proposta |
|---|---|---|---|
| `natureza_evidencia` | ficha N1 | da evidência | **herdada** pelo vínculo; composição = teto no elo mais fraco (ordem declarada no enum) |
| `desenho_estudo` | ficha N1 | da evidência | **herdada**; o resíduo `desenho_estudo_bruto` só entra no teto depois da curadoria (197 pendentes); até lá, `indefinido` |
| `forca_causal` (tier) | vínculo N2 | da relação | **propagada**; teto tier_1→tier_4; `None` → `indefinido` |
| `grau_maturidade` | vínculo N2 | da relação | **propagada**; teto no elo mais fraco |
| `trilha` | vínculo N2 | qualificador de leitura | **metadado preservado**, não ordenável: trilha clínica × mecanística não se "minimam"; a saída declara a trilha dominante **e** as trilhas presentes — proibida mistura silenciosa |

A linha da `trilha` é a contribuição que a casa acrescenta ao ponto 1 do comentador: tratar trilha como "elo limitante" seria uma falsa equivalência de novo tipo. É exatamente o caso que a classificação por eixo existe para impedir.

## 8. Posição e próximos passos

1. **Posição da casa: minuta 1 APROVADA como base do contrato normativo**, com (i) as 4 correções do comentador externo — verificadas e adotadas com crédito — e (ii) as 3 precisões fáticas F-1/F-2/F-3 como errata técnica. Créditos preservados: escada D-01 (restrição do comentador), teto por eixo D-02 (formulação da casa), adição D-06 (comentador), defaults e método (dele).
2. **Pedido:** minuta 2 normativa incorporando o §5 (4 pontos) e o §6 (F-1/F-2/F-3) + a promessa dele pendente: **P-8 em nova versão com V-15 em modo aviso-na-prosa / erro-em-ficha-vínculo** (com o delimitador 91 e a ferramenta medindo por camada).
3. **Ordem do operador mantida:** quando a V2 fechar bilateralmente neste eixo, a **carta nº 3 ao auditor de estrutura dispara no mesmo envio** — a v1.1 dele já está replicada e aprovada como base do 1.2 (trilha 27), e a análise dos schemas dele vai junto.
4. **Pendência com o operador (inalterada):** o kit da trilha clínica (5 documentos) — causa-raiz do caso `uso`, ainda fora do alcance da casa.
5. **Registro da rodada:** decisoes rev.16 · CHANGELOG 13 · trilha 29 (comandos gravados — a penitência da seção 3 aplicada no ato). Rodada documental: **0 ciência**; sha V7 intacto.

*IDEMPOTÊNCIA DE FATOS: tudo o que esta carta afirma sobre números sai dos comandos gravados na trilha 29; tudo o que afirma sobre campos sai dos dois schemas v1.1 (shas `737bcda8…` / `b0934412…`) e de greps nomeados. Onde a casa não conseguiu rederivar (446), ela confessou antes de prosseguir.*
