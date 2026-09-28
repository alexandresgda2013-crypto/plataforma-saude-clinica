# 04 — Protocolo de Auditoria Científica de Conteúdo

**Quando roda:** mini-rodada dedicada, após o Checklist de Auditoria Estrutural aprovar a Biblioteca, antes da aprovação/integração.
**Quem:** sessão separada (não o chat de geração). Pacote mínimo (Como Executar — B1 MEC): `_ids_oficiais`, Protocolo de Escopo B1 MEC, Schema-Claim v3.1, este protocolo, GPM_B1 + Briefing, Lista Canônica do BLOCO ativo, Bloco de Estado, **a Biblioteca_Bx.md e o Módulo 09 aprovados estruturalmente**.

A auditoria de conteúdo reutiliza **exatamente** os portões G1→G2→G3 e as regras de blindagem do fluxo de validação de claims (Como Executar — B1 MEC). A diferença é o ponto de partida: aqui o objeto é cada **trecho-âncora** da Biblioteca já redigida, não um `claim_alvo` da seed.

---

## 1. Preparação da leva

1. Montar o ledger (doc 02): uma entrada por trecho citado na Biblioteca, com `status_auditoria: "PENDENTE"`.
2. Ordenar a fila:
   - 1º) `origem_entrada: GPM` e `POLITICA_FONTES` com `citacao_confirmada: false` / "referência a confirmar";
   - 2º) trechos com `grau_maturidade_cientifica` = `hipotese_inicial`/`emergente`;
   - 3º) trechos que alimentam BLOCO_07 (nós centrais) e BLOCO_08 (loops/conexões) — exigem mais por serem síntese;
   - 4º) `origem_entrada: LISTA_CANONICA` (integridade apenas).
3. Trabalhar por BLOCO (a Lista Canônica é organizada por BLOCO), não aleatoriamente.

## 2. Para cada trecho — os três portões

### G1 — Existência (`portao_G1_existencia`)
- O `pmid_oficial` (ou DOI) da entrada do Módulo 09 resolve no PubMed? Os metadados (título, autor, ano, revista) conferem via esearch/esummary?
  - **Sim** → `VERIFIED_REFERENCE`.
  - **Não resolve / não acessível** → `FALHOU` → `status_auditoria: NAO_LOCALIZADO`.
  - **Resolve mas é outro artigo** → `FALHOU` → `status_auditoria: PMID_INCORRETO`.
- Se a entrada veio do GPM sem PMID (comum): formular a query a partir do **trecho-âncora + Briefing** (termos alternativos do Briefing antes de aceitar "zero resultados"), rodar no PubMed, colar a lista de resultados.
- **PMID nunca de memória.** Sem abstract/resultado colado nesta sessão, o PMID não existe para o sistema.

### G2 — Elegibilidade (`portao_G2_elegibilidade`)
Depois de colar o abstract (ou texto completo, se gatilho):
- O desenho é aceito pelo Protocolo de Escopo? (`tiers_forca_causal`, `tipos_modelo_aceitos`; espécie declarada).
- Sem contaminação por desfecho de tratamento em BLOCO_02–05 (salvo BLOCO_06.7/09.6, onde é o próprio objeto).
- Sem `exclusion_criteria`: ferramenta farmacológica/genética de especificidade contestada sem controle de off-target; case report sem contraste; preprint sem peer review; artigo retratado; predição in silico sem validação empírica.
- **Natureza epistemológica:** o achado é mecanístico (manipulação causal/contraste experimental) ou é associação populacional clínica?
  - Puramente associativo/epidemiológico → `status_auditoria: ASSOCIATIVO_REDIRECIONAR`, destino `REDIRECIONADO_MODULO_CLINICO` (com `destino_sugerido`, ex.: B1/SM-02). **Nunca** rejeitar por esse motivo.
  - Elo causal de outro BLOCO/mecanismo → `REALOCAR` (`fila_realocacao`).
- Passou? → `ELIGIBLE_SOURCE`. Não, por desenho/exclusão → `FALHOU` + `ELEGIBILIDADE_FALHOU` → `fontes_rejeitadas` com motivo.

### G3 — Suporte ao trecho (`portao_G3_suporte`)
As mesmas 3 perguntas do Como Executar, agora aplicadas ao **trecho-âncora**:
1. **Pertencimento:** o PMID pertence a este BLOCO/mecanismo? (ou é de outro BLOCO, de B2–B16, ou do módulo clínico).
2. **Suporte causal:** o abstract/texto sustenta a relação específica que o trecho afirma, com `tipo_manipulacao` e `contraste_experimental` corretos? A aresta (`no_origem → no_destino`) está demonstrada pelo desenho, ou é inferência além do que o estudo mostra? O trecho respeita o **sistema experimental** (humano/animal/in vitro) e a **direção/força**?
3. **Robustez:** a evidência sustenta o nível de linguagem usado? Preencher `dominios_grade_observados` (nunca antes). Verificar off-target (pode rebaixar para ressalva/justificar rejeição).

Saídas do G3: `APROVADO` / `APROVADO_COM_RESSALVA` (exige nota de ressalva) / `REJEITADO` / `INCONCLUSIVO`.
**Regra inegociável:** G3 exige abstract colado nesta sessão.

## 3. Árvore de decisão (consolidada)

```
Trecho pendente
  │
  ├─ G1: identificador existe e metadados conferem?
  │    NÃO (não resolve/acessível) ──► NAO_LOCALIZADO
  │         → RESGATE: 1 busca por query do trecho+Briefing
  │              achou fonte? → segue para G2 com a fonte nova (CORRIGIR_PMID/TROCAR_REFERENCIA)
  │              não achou?   → trecho NÃO tem fonte: REMOVER_TRECHO ou REBAIXAR_LINGUAGEM
  │                             (não é "rejeição científica": é ausência de fonte — R04 "campo vazio
  │                              preferível a dado inventado")
  │    Existe mas é outro artigo ──► PMID_INCORRETO
  │         → RESGATE (1x) pelo artigo correto; achou e sustenta? → APROVADO; senão → ramo G3
  │
  ├─ G2: desenho elegível para a trilha mecanística?
  │    Puramente associativo/clínico-epidemiológico ──► ASSOCIATIVO_REDIRECIONAR
  │         → redirecionados_modulo_clinico (NUNCA fontes_rejeitadas)
  │    Elo causal de outro BLOCO/mecanismo ──► REALOCAR (fila_realocacao)
  │    Desenho excluído (off-target sem controle, preprint, retratado, in silico, anedótico)
  │         ──► ELEGIBILIDADE_FALHOU → fontes_rejeitadas (motivo do exclusion_criteria)
  │
  └─ G3: a fonte sustenta o trecho no nível em que está escrito?
         SIM (sistema, direção, força batem)
              ──► APROVADO → destino FICA_MECANISMO
         PARCIAL (outro sistema experimental; só parte do trecho; força menor que a alegada;
                  ferramenta com ressalva)
              ──► APROVADO_COM_RESSALVA → fica, com nota de ressalva + ação:
                    - evidência animal para frase redigida como humana → ADICIONAR_SINALIZADOR
                      ([APENAS PRÉ-CLÍNICO] / [EXTRAPOLAÇÃO POR ANALOGIA: ...]) e REBAIXAR_LINGUAGEM
         NÃO (não diz / diz o contrário)
              ──► NAO_SUSTENTA → RESGATE (1x) por fonte que sustente:
                    achou? → validar a nova fonte (volta ao G1)
                    não?    → REMOVER_TRECHO (ou, se o conhecimento é plausível, REBAIXAR
                              para hipótese sinalizada) — claim correspondente vira rejeitado/em_busca
```

## 4. O resgate (uma única tentativa estruturada)

- Uma busca substituta por trecho, com query registrada (`query_utilizada`, `caso_query`).
- Fonte substituta encontrada: vira entrada própria no Módulo 09 (mini-rodada C) e passa por G1/G2/G3 normal — não se herda aprovação.
- Sem segunda tentativa nesta passagem: o trecho fica com o estado que merece e segue para reconciliação.

## 5. Quando texto completo é obrigatório (gatilhos oficiais)

- Claim/trecho depende de ≤3 fontes principais;
- dado de subanálise/subgrupo (não desfecho primário);
- leva caminhando para ressalva/rejeição com evidência aparentemente fraca;
- preencher `risco_de_vies` (abstract só permite `nao_avaliado`);
- `tipo_manipulacao` = inibidor/agonista (especificidade/off-target é informação de Métodos);
- trecho que alimenta BLOCO_07/BLOCO_08 (múltiplas arestas no mesmo estudo).

Sem acesso a texto completo quando ele é exigido: resultado `INCONCLUSIVO`/pendência, **não** aprovação por abstract.

## 6. Regras anti-viés (blindagem — Como Executar)

1. Nenhum dos 4 eixos decide sozinho; G3 é julgamento do avaliador sobre as 3 perguntas.
2. `relacoes`/arestas devem refletir o que o desenho demonstra; abstract que sugere mas não demonstra → `INCONCLUSIVO`, nunca `suporta_relacao`.
3. GPM nunca é fonte de PMID; "referência a confirmar" é só território de busca.
4. Número só de fonte colada nesta sessão.
5. Nenhum resultado de query é descartado sem registro (vai para `resultados_nao_triados`).
6. Não completar lacuna com conhecimento pessoal: a fonte não diz = a fonte não diz.

## 7. Fechamento da leva

- Atualizar o Bloco de Estado do mecanismo: `claims_aprovados` (trechos que correspondem a claims novos aprovados — preencher Schema-Claim completo, com `mapa_exportacao_modulo09`), `fontes_rejeitadas`, `fila_realocacao`, `redirecionados_modulo_clinico`, `resultados_nao_triados`.
- Atualizar o ledger: todos os trechos com `status_auditoria` definitivo e `verificacao` preenchida.
- Emitir o relatório `Auditoria_Bx/decisoes_Bx.md` (conta por status) e passar para a mini-rodada C (doc 06).

### Sobre claims novos
Um trecho `GPM/POLITICA_FONTES` que passa G1/G2/G3 com fontes reais é um **achado validado novo**. Ele deve ser registrado como claim no Schema-Claim v3.1 (com `status: aprovado` ou `aprovado_com_ressalva`, `verification: verificado_nesta_conversa`, fontes completas e `mapa_exportacao_modulo09`) e incorporado à Lista Canônica do BLOCO — fechando o ciclo: da próxima vez, a Biblioteca já o recebe como entrada prioritária. O `claim_id` então volta para o ledger e, na mini-rodada C, para `claim_id_origem` do Módulo 09.
