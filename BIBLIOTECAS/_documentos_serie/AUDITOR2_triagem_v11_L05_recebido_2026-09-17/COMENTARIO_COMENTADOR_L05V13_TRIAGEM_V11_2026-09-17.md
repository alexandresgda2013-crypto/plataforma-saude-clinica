RESPOSTA DO COMENTADOR EXTERNO

L-05 — Schema de Evidência e Vínculo com Ancoragem Multi-Entidade

Referência: proposta v1.3 — pós-triagem e consolidação das decisões

A resposta apresentada pelo Auditor de Estrutura demonstra que o L-05 v1.3 atingiu um nível de consolidação suficiente para avançar para o fechamento das decisões ainda abertas, sem necessidade de nova reengenharia estrutural.

1. Decisões já suficientemente consolidadas

Considero adequadamente resolvidos, no estado atual:

- `ancora_principal` como campo top-level, com integridade referencial às âncoras;
- separação entre `papel` e `direcao_suporte`;
- distinção entre `natureza_evidencia`, `desenho_estudo` e `uso`;
- adoção das duas trilhas (`clinica` e `mecanistica`), com `gap_pesquisa` compartilhado;
- substituição normativa de `status_auditoria` por `status_validacao` no N1;
- separação entre schema, gate e classificação humana;
- correção da regra E2 para validação da identidade do avaliador;
- remoção do sinal regex de extrapolação quando a informação já está representada por campos estruturados;
- triagem revisada em 231 registros automáticos e 43 registros destinados à revisão humana;
- manutenção de `sustenta` como estado transitório de triagem, e não como decisão científica definitiva.

Não recomendo reabrir essas decisões.

2. Pontos que permanecem efetivamente abertos

Restam três decisões de governança/execução:

**D2 — classificação das 30 revisões**

É necessário definir se os 30 registros classificados como `review` serão reclassificados agora segundo o material efetivamente revisado ou se permanecerão temporariamente nessa condição, com prazo/regra explícita para encerramento.

Minha recomendação é que a classificação seja feita antes do fechamento normativo do conjunto atual, porque `natureza_evidencia` é um atributo epistemológico do registro e não deveria permanecer indefinido por conveniência operacional.

**D3 — ancoragem retroativa**

É necessário decidir o momento da expansão das âncoras secundárias nos 274 vínculos.

A separação conceitual apresentada está correta: a âncora secundária é elemento de curadoria e não deve ser confundida com precedência epistemológica.

A estratégia incremental proposta — começando pelos 20 casos `redirecionado_clinico` — é operacionalmente coerente. Entretanto, o encerramento do L-05 deve registrar explicitamente se a ancoragem secundária é:

1. requisito para fechamento do corpus atual; ou
2. tarefa posterior de enriquecimento curatorial.

Sem essa distinção, o estado do corpus continuará ambíguo.

**D4 —** `citacao_confirmada`

A existência de `citacao_confirmada=true` em 237/237 registros, sem origem conhecida, deve ser tratada como questão de proveniência histórica, não como evidência de validação.

Não recomendo transformar esse campo em critério de validade científica.

A decisão deve estabelecer se o campo será:

- removido após migração;
- mantido apenas como legado/deprecated; ou
- normalizado mediante auditoria da origem.

O ponto essencial é que seu valor atual não seja interpretado como comprovação independente.

3. Inconsistência documental

Há uma correção editorial necessária antes do fechamento:

O documento se apresenta no cabeçalho como:

`v1.0 — PROPOSTA`

enquanto o próprio conteúdo declara:

`PROPOSTA v1.3`

Essas duas identificações precisam ser unificadas.

A identificação normativa do documento deve refletir o estado efetivamente consolidado: **v1.3 — PROPOSTA, NÃO NORMATIVO**, caso essa seja a decisão vigente.

4. Catálogo oficial

Permanece importante o gate dos `_ids_oficiais`.

O fato de o catálogo estar atualmente incorporado ao Markdown, e não em um arquivo independente, é aceitável como implementação documental desde que o derivador consiga reproduzir integralmente:

- 146 IDs oficiais;
- 48 suplementos/complementares;
- 71 exames/algoritmo;
- 16 mecanismos;
- 11 cenários.

O resultado anterior de 103 IDs não deve ser tratado como falha do catálogo sem antes identificar a causa da diferença. O critério de aceitação deve ser a reprodução integral dos 146 IDs oficiais.

5. Estado do L-05

Com base na resposta apresentada, considero que o L-05 v1.3 está **estruturalmente consolidado**.

Não identifico, neste momento, necessidade de criar novos campos ou alterar novamente a arquitetura do schema.

O próximo passo deve ser exclusivamente:

**D2 → D3 → D4 → correções documentais → execução dos gates finais → fechamento do L-05 v1.3.**

Somente após essa sequência faz sentido declarar o schema normativo e prosseguir para a consolidação da estrutura geral da plataforma.

6. Conclusão

O trabalho do Auditor de Estrutura respondeu adequadamente às questões levantadas nas rodadas anteriores.

A partir deste ponto, novas alterações estruturais devem ser evitadas salvo surgimento de falha objetiva de consistência, validação ou governança.

**Parecer do Comentador Externo:**

> **L-05 v1.3 — ACEITO COMO PROPOSTA ESTRUTURAL CONSOLIDADA, PENDENTE APENAS DO ENCERRAMENTO DAS DECISÕES D2, D3 E D4, DOS GATES FINAIS E DA NORMALIZAÇÃO DOCUMENTAL.**

Após esses encerramentos, o L-05 poderá seguir para fechamento normativo sem necessidade de nova rodada de reengenharia.
