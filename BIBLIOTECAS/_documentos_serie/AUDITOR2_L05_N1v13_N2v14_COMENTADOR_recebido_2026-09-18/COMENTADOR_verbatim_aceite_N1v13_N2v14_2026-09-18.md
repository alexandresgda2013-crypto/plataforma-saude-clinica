# COMENTADOR (ChatGPT) — VERBATIM recebido via operador em 2026-09-18

Origem: resposta do comentador à remessa conjunta N1 v1.3 + N2 v1.4 (L-05).
Política da casa: nota crua de comentador NUNCA circula — este arquivo é REGISTRO INTERNO
da casa com fins de verificação; os pontos verificados serão carregados em carta própria,
com crédito. Verbatim integral abaixo (invariante: nenhum ponto/vírgula tocado).

---

## RESPOSTA AO AUDITOR ESTRUTURAL

### L-05 — N1 v1.3 + N2 v1.4

Os dois schemas foram recebidos e analisados conjuntamente:

* `L05/schema_referencia_v1.3.json` — Nível 1 / Módulo 09
* `L05/schema_vinculo_v1.4.json` — Nível 2 / Vínculo

A análise conjunta confirma coerência entre N1 e N2 e aderência às decisões estruturais registradas na bancada.

### 1. N1 — Referência

Considero estruturalmente resolvidos:

* `status_validacao` como campo canônico;
* `status_auditoria` como alias legado/deprecated;
* regra condicional de `pmid_oficial`;
* separação entre `natureza_evidencia` e `desenho_estudo`;
* preservação de `desenho_estudo_bruto`;
* guarda de migração incluindo `cross-over`;
* separação entre `g3_verificado_por` e `g3_nota_metodo`;
* separação entre `origem_pipeline` e `origem_detalhe`;
* retirada de carga verificacional de `citacao_confirmada`.

Em especial, D4 fica considerada resolvida no estado atual: `citacao_confirmada` permanece apenas como campo deprecated de compatibilidade, sem função de verificação ou de gate.

### 2. N2 — Vínculo

Também considero estruturalmente resolvidos:

* `ancora_principal` como campo único de contexto de curadoria;
* `ancoras[]` como estrutura multi-entidade;
* D3: `minItems=1` no caso geral e `minItems=2` para `redirecionado_clinico`;
* separação entre `papel` e `direcao_suporte`;
* regra de `condicao` para `direcao_suporte=condicional`;
* compatibilidade `trilha × uso`;
* exigência de `g3_verificado_por` quando `verification_status=verificado`;
* tratamento de `forca_biologica_conexao` como regra de portão;
* distinção entre redirecionamento clínico e papel semântico da âncora de destino.

Não identifico, nos dois schemas apresentados, necessidade de nova reengenharia estrutural.

### 3. Pendências efetivas

Permaneçam registradas apenas as pendências já identificadas:

1. **D2** — classificação dos 30 registros `review`;
2. **adoção formal do catálogo `_ids_oficiais.json` com os 146 IDs** como fonte única de verdade.

Após o fechamento desses pontos e a respectiva migração/validação dos dados, o L-05 poderá avançar da condição de **PROPOSTA NÃO NORMATIVA** para a etapa normativa correspondente.

### 4. Diretriz para a próxima etapa

Não é necessário abrir nova rodada de redesenho dos schemas por questões já resolvidas.

A prioridade passa a ser **fechamento das pendências, execução dos gates e migração controlada**, preservando a arquitetura v1.3/v1.4 apresentada.

Considero, portanto, os dois schemas estruturalmente aprovados como base de fechamento do L-05, sujeitos apenas às pendências acima.
