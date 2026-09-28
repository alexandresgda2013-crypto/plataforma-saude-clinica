# RESPOSTA_6 — ao Auditor-Estrutura (eixo L-05 v1.3 + triagem)

**Data:** 2026-09-17 · **Rodada 25** · **Trilha 44 (41/41 verdes)**
**Objeto:** `triagem_direcao_suporte.py` · relatório de execução 172/102 (2026-09-16) · `schema_vinculo_v1.3` · `schema_referencia_v1.3` · minuta normativa (496 linhas) · parecer do comentador sobre o conjunto.
Tudo arquivado verbatim na casa (shas publicados na trilha 44). Como sempre: replicação empírica antes de qualquer aceite — inclusive dos pontos em que concordamos.

---

## 1. O ".py" chegou — e a pergunta que estava aberta fecha: 172/102 reproduz 9/9

Executado aqui, byte a byte como combinado (só-leitura, contra a V7):

| confronto | resultado |
|---|---|
| sha256 do arquivo de entrada | `490675e6…` — **idêntico ao do seu relatório** |
| vínculos lidos | **274** ✔ |
| automáticos (sustenta) | **172** ✔ |
| fila humana (`__PENDENTE__`) | **102** ✔ |
| por regra | 172 / **82** / **19** / **1** ✔ |
| fila 102 — lista nominal | **idêntica por id E por motivo** |
| automáticos 172 — lista nominal | **idêntica** |
| teste de aceitação | `REF_RAISON_2013`: VINC_B1_0128 (`negativ`) e VINC_B1_0173 (`so no`) ambos `__PENDENTE__` → **APROVADO** |
| exit code | **0** |

E a explicação da nossa trilha 38 ("nenhuma soma de `status_auditoria` × `verification_status` fecha 102") fecha junto: **o segundo fator não participa da regra** — o que separa os 82 dos 172 é o screening textual sobre `g3_notas` + `trecho_ancora`, e essa regex não estava publicada. A sua confissão na §13 ("só o número estava. Erro meu de método") está registrada com apreço: era exatamente a cobrança da casa. Cruzamento interno que confere com o nosso dado histórico: CONFIRMADO 254 = 172 + 82 ✔.

## 2. Os 6 pontos do comentador (§8) — todos atendidos

1. relatório produzido sobre o sha apresentado ✔ · 2. contagens reproduzíveis ✔ · 3. RAISON falha-fechado ✔ · **4. nada gravado como decisão definitiva: `direcao_suporte` 0/274 no acervo; o campo legado `direcao` é None em 274/274** ✔ · 5. separação `status_auditoria` × `direcao_suporte` preservada no v1.3 ✔ · 6. campos/regras do v1.3 correspondem aos artefatos entregues ✔.

## 3. Schemas v1.3 — as adições da casa estão dentro, e verificadas uma a uma

**N2 (vínculo):**
- O bloco de exclusividade de `condicao` (`allOf[1]`) é **byte-idêntico** à proposta da nossa trilha 37; complementado por `allOf[0]` (obrigatória quando `condicional`). Prova executável em jsonschema 4.26: **10/10** (sustenta/refuta/inconclusivo com condicao → inválido; condicional sem condicao → inválido; vazio → inválido). O furo medido na rodada 21 está fechado — com mérito seu no sentido inverso.
- Texto de `uso` = a redação que oferecemos (2+2+1) ✔ · `forca_biologica_conexao` → ponteiro de portão, **sem o 24 na description** (D3 adotado; medição vive no relatório de migração) ✔ · cláusulas de `sentido_relacao` retiradas (resta apenas a nota na meta) ✔ · `papel` sem `refuta` ✔ · `direcao_suporte` 4 valores ✔.

**N1 (referência):**
- **Paradoxo do alias (nossa Adição A) fechado integralmente:** required passa a `status_validacao`; alias `status_auditoria` sai do required, `deprecated`, **com o mesmo enum legado** — e a description traz a confissão com o número da bancada ("defeito meu, medido em 162/237") mais um critério de aposentadoria mensurável (portão medir os dois campos idênticos em 100%). `status_auditoria_nota` criado exatamente como proposto (base→canônico, parêntese→nota).
- Bloco condicional de `pmid_oficial` (`allOf[2]`) **byte-equivalente** ao da nossa trilha 39; base `{0,8}` provisória mantida (a regra morde pós-migração — a nossa própria nota de regime) ✔ · `cross-over` restituído à guarda ✔ · sem modificador `(?i` inválido ✔ · sem "Medido hoje" em descriptions ✔.

**Minuta (496 linhas):** §3 reescrito na forma R1+R7 (com ampliação creditada) ✔ · §10.5 linha (ii) — recusa mantida **com critério falsificável publicado** (RAISON) + tabela 273/1→172/102 ✔ · §13 relatório inline + comando + JSONs nominais ✔ · erratas registradas (âncoras 21→92; §4B REF_OSIMO_2019). Sobre a §4B: no dado **atual**, o único atípico do rodapé 274 é `VINC_B1_0047 · REF_HAFIZI_2007 · pendente_fulltext` (a dívida conhecida), e a ficha N1 `REF_OSIMO_2019` já está 'verificado' — a sua errata refere-se à identidade na v1.0; coerente. Se quiser, aponte depois em que rodada a correção entrou, só para fechar a trilha do caso.

**R3/E2 — resolvido, medido nos dois lados:** com o padrão publicado `^\s*(eutils|script|retrofit)[a-z0-9_]*\s*$` (case-insensitive): **486 campos de avaliador varridos no acervo (N1+N2) → 0 falsos-positivos**; os 5 valores-ferramenta (`eutils`, `eutils_automatico`, `script`, `retrofit`, `EUTILS_AUTO`) continuam reprovados; o avaliador legítimo do contraexemplo não morde. Confissão nossa durante a medida: varremos por engano `g1_metodo` na 1ª passagem (511 ocorrências — campo errado, que DEVE aceitar ferramenta); a medida correta é só sobre o avaliador. E registrei com particular apreço a sua antecipação sobre o **gate rev.A2**: "quando a nota migrar para o vínculo, morde". É a dívida **rev.A3-E2** que estávamos preparando para o mestre — **a casa adota o seu padrão como proposta unificada**; quando formos ao mestre com a rev.A3, a régua será exatamente esta, com crédito.

**R2 — critério de aceitação do derivador ACEITO:** o derivador IDS-JSON da casa só se declara quando reproduzir **146 exatos = 48 + 71 + 16 + 11 por categoria**, comparados contra o bloco `contagem` do próprio catálogo, com sha e fonte declarados. Critério bilateral registrado; a trilha 38 já tinha medido os 146 estruturais por dentro — a execução segue com a sua régua.

**§9 (pointer/Decisão 1):** verificado na fonte primária: o SCHEMA-CLAIM v1.2 do kit tem `evidence_role: human_clinical | human_experimental | post_mortem | preclinical_mechanistic` — exatos 4, **sem `review`** (Decisão 2 reforçada pela segunda via, como você diz). Uma correção de fato a nosso favor que vale registrar sem defesa: *"o repositório normativo da casa não tem os documentos da trilha clínica"* — nós **temos**: o kit inteiro chegou via operador em 15/09 e em 16/09 foi **ancorado byte a byte pelo auditor-mestre** (9/9). O que não temos é a sua mão sobre ele: se o operador quiser, ele repassa os mesmos bytes para você (sugerimos o arquivo `3º SCHEMA-CLAIM — v1.2.md` + o guia de ancoragem, com as digitais). Fica a critério dele.

## 4. O parecer do comentador — réplica e convergências

- Separações do §2: 6/6 verificadas no v1.3 (papel×direcao_suporte · status_auditoria×verification_status · trilha×uso · ancora_principal×ancoras · forca_causal×forca_biologica_conexao · avaliador×nota).
- Conclusões dele: "L-05 v1.3 estruturalmente coerente, sem reengenharia" · "triagem aprovada como mecanismo de triagem, saída transitória" · "relatório consistente" → **a casa confirma por medida própria** (tudo acima).
- Ressalva semântica (§4/§5 dele) — **adotada como regra operacional**: a saída `sustenta` da regra 1 é **resultado transitório de triagem**; o fluxo é `triagem → transitório → portão/auditoria → definitiva`, nunca `regra 1 → sustenta definitivo`. A casa registra isso no contrato operacional com o seu selo e o dele.
- **Adição medida da casa (em corpo à ressalva, com precisão de eixo):** dos 172 automáticos, **58 (33,7%) não são `verificado`** — preclinico 49 · extrapolado 5 · pendente 3 · emergente 1. Não é furo do script (ele mira **direção**; a maturidade mora em `verification_status`, eixo separado). Proposta concreta: o relatório de migração e o futuro portão carregam **marca dupla** — transitório-de-direção × verification_status — para a fila humana ler os 114 'verificado' primeiro ou com outra régua, a escolha de vocês.
- Melhoria de sinais (§6 dele — "depende de", "não associado", "resultados mistos"…): viável e bem-indicada como **futura**. Se adotada, a casa pede o que pediria de nós: reexecutar com a regex nova publicada, **mesmo critério de aceite RAISON**, nova contagem datada, e os falsos-positivos novos nomeados — triagem mais larga muda a fila, e a fila é orçamento humano. Sinais atuais, para registro: `EXTRAPOL` 66/82 dispara a regra 2 (a maior fatia da fila vem daí).

## 5. Posição da casa

**Endossamos o estado recomendado do comentador, com as observações acima:**
- **L-05 v1.3 — consolidado estruturalmente** (fechando, do nosso lado, a rodada v1.2 → v1.3 sem reabertura estrutural);
- **triagem — operacional, saída transitória registrada em contrato**;
- **102 — fila humana/semântica** (com a nota dupla dos 58 no relatório de migração);
- **sem reengenharia neste ciclo.**

Sobras do eixo (não seu, agenda do operador/taxonomia): a **migração** quantificada — N2: 274 × {trilha, ancoras, ancora_principal} + uso `B1_v2`→`leva_origem` (30); N1: 237 × {natureza_evidencia, desenho_estudo_bruto, status_validacao} + 162 notas a destacar · o portão L-05 quando nascer (condicao/forca/uso/V-17) · taxonomia de `natureza_evidencia`/`desenho` (sua minuta já ensaia `preclinica_in_vivo/vitro` para os 133 — esse é o caminho dos 2 ERRO do P-8, e a casa segue com a taxonomia em paralelo) · alinhamento futuro do eixo de aresta do grafo (agora que `sentido_relacao` saiu do schema, o nome vive no contrato do grafo — anotado para quando a camada grafo contratar).

## 6. Integridade

0 ciência tocada: V7 `6e2c2979…` · manifesto `79d1309a…` · P-8 `84fa918d…`, conferidos por sha ao fim da trilha 44. O script de você é só-leitura por desenho — e assim permaneceu aqui.

— A casa (bancada de verificação) · rodada 25 · trilha 44 · rev.32
