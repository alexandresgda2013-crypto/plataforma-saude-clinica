PARECER DO COMENTADOR EXTERNO

L-05 v1.3 + Triagem de Direção de Suporte

1. Objeto

Foram analisados conjuntamente:

1. o script `triagem_direcao_suporte.py`;
2. o relatório de execução da triagem sobre 274 vínculos;
3. o `L05/schema_vinculo_v1.3.json`.

A análise considerou a coerência entre o contrato estrutural do L-05, a execução da triagem e a separação entre validação estrutural, auditoria semântica e resultado transitório de processamento.

2. Conclusão sobre o L-05 v1.3

O schema v1.3 encontra-se **estruturalmente coerente com as decisões registradas**.

Não foi identificada necessidade de reengenharia.

Permanecem corretamente separados:

- `papel` e `direcao_suporte`;
- `status_auditoria` e `verification_status`;
- `trilha` e `uso`;
- `ancora_principal` e conjunto de `ancoras`;
- `forca_causal` e `forca_biologica_conexao`;
- identidade do avaliador (`g3_verificado_por`) e nota metodológica (`g3_nota_metodo`);
- contrato L-05 e contrato do grafo;
- schema e gates externos.

A implementação de `condicao` por `allOf` também está adequada: é obrigatória para `direcao_suporte=condicional` e proibida nos demais valores.

A permanência de `forca_biologica_conexao` como requisito de portão, e não como regra do Draft-07, está igualmente adequada, pois sua obrigatoriedade depende do escopo da âncora principal.

3. Relatório de triagem

O relatório apresentado é internamente consistente:

- total: **274**
- automáticos: **172**
- fila humana: **102**
- regra 2: **82**
- regra 3: **19**
- regra 0: **1**

As contagens fecham integralmente.

O teste específico de `REF_RAISON_2013` também foi corretamente preservado: os dois vínculos identificados permaneceram pendentes e não foram promovidos automaticamente a `sustenta`.

Portanto, como **relatório de execução da triagem**, o resultado é coerente.

4. Ressalva semântica sobre a regra 1

Este é o único ponto que deve permanecer explicitamente registrado.

A regra:

`CONFIRMADO + ausência de sinal textual → sustenta`

deve ser entendida como **triagem heurística**, e não como validação científica definitiva da direção epistemológica.

`status_auditoria=CONFIRMADO` estabelece que a referência foi confirmada em relação ao trecho-âncora. Isso, isoladamente, não determina que a relação epistemológica seja necessariamente `sustenta`.

Uma evidência confirmada pode conter, por exemplo:

- associação sem causalidade;
- resultado neutro;
- resultado misto;
- limitação;
- efeito restrito a determinado subgrupo;
- dependência de condição;
- ausência de efeito;
- conclusão inconclusiva.

O conjunto atual de sinais textuais captura parte importante desses casos, mas não substitui a leitura semântica quando a direção não é inequívoca.

5. Regra operacional necessária

A saída produzida pela regra 1 deve permanecer caracterizada como:

**resultado transitório de triagem.**

Ela não deve ser interpretada como alteração definitiva do vínculo L-05 nem como decisão epistemológica final.

O fluxo correto é:

`Vínculo original`  
→ `Triagem automática`  
→ `resultado transitório`  
→ `portão/auditoria`  
→ `direcao_suporte definitiva`

e não:

`Vínculo original`  
→ `regra 1`  
→ `sustenta definitivo`.

Essa distinção deve permanecer explícita no contrato operacional para impedir que uma heurística de processamento seja posteriormente confundida com validação científica.

6. Sobre o regex

A estratégia conservadora do script é adequada para triagem.

Existe apenas uma melhoria técnica futura possível: ampliar os sinais para construções condicionais e de resultado misto, por exemplo linguagem equivalente a "depende de", "condicionado a", "sem evidência clara", "não associado", "não demonstrou" e "resultados mistos".

Isso não constitui bloqueio do L-05 v1.3 e não justifica reabertura estrutural neste momento.

7. Parecer final

**L-05 v1.3: estruturalmente aprovado para avanço como proposta consolidada, sem nova reengenharia.**

**Script de triagem: aprovado para uso como mecanismo de triagem, com a ressalva de que sua saída de** `sustenta` **é transitória e não equivale a validação epistemológica definitiva.**

**Relatório de execução: consistente com o script e com as contagens apresentadas.**

A ressalva acima deve ser registrada como **regra operacional de uso da triagem**, não como alteração do schema L-05.

8. Encaminhamento à Arena/Casa

A Arena/Casa deve verificar, de forma independente:

1. que o relatório foi produzido sobre o arquivo de entrada identificado pelo SHA-256 apresentado;
2. que as contagens 274 / 172 / 102 permanecem reproduzíveis;
3. que o teste `REF_RAISON_2013` continua falhando fechado caso qualquer vínculo seja promovido automaticamente a `sustenta`;
4. que a saída da triagem não é gravada diretamente como decisão epistemológica definitiva no acervo;
5. que a separação entre `status_auditoria` e `direcao_suporte` permanece preservada;
6. que os campos e regras do L-05 v1.3 correspondem ao artefato efetivamente apresentado.

A Casa deve tratar a confirmação desses pontos como **verificação de execução e integridade**, não como nova decisão sobre o desenho do L-05.

Estado recomendado

**L-05 v1.3 — consolidado estruturalmente.**

**Triagem — operacional, com saída transitória.**

**102 registros — fila para tratamento humano/semântico.**

**Nenhuma reengenharia estrutural necessária neste ciclo.**
