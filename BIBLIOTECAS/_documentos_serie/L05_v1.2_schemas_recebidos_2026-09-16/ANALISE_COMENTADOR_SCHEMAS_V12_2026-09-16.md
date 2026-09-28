Recebi também o `L05/schema_vinculo_v1.2.json` e fiz a conferência da implementação, não apenas da prosa da minuta.

Os pontos anteriores sobre `refuta`, `ancora_principal`, classificação conservadora de `natureza_evidencia` e `status_validacao` foram incorporados adequadamente.

Encontrei, porém, três pontos que precisam ser fechados antes da passagem à Casa.

1. `condicao` — o schema garante a obrigatoriedade, mas não a exclusividade

O `allOf` atual garante corretamente:

```text
direcao_suporte = condicional
→ condicao obrigatória e não vazia

```

Mas ainda permite:

```text
direcao_suporte = sustenta
→ condicao = "..."

```

e o mesmo para `refuta` ou `inconclusivo`.

Se a semântica normativa é que `condicao` pertence exclusivamente ao eixo `condicional`, o schema precisa expressar também o lado negativo:

```text
condicional
→ condicao obrigatória

sustenta/refuta/inconclusivo
→ condicao ausente ou null

```

Peço que isso seja fechado no schema/gate para evitar estado semanticamente inválido.

2. A conclusão sobre `sentido_relacao` não deve ser fechada pelo L-05

A adoção de:

```text
direcao_suporte

```

está correta e resolve a colisão nominal no L-05.

Mas a descrição do campo ainda afirma:

> “dispensa renomear o lado da ontologia”

Eu retiraria essa conclusão do schema.

`direcao_suporte` e `sentido_relacao` podem representar dimensões diferentes:

```text
direcao_suporte
→ direção epistemológica do suporte da evidência à afirmação

sentido_relacao
→ semântica/direção da relação formal no grafo

```

A decisão de manter, renomear ou eliminar `sentido_relacao` deve ser feita no contrato da Ontologia/Grafo.

O L-05 deve apenas afirmar que seu próprio campo se chama `direcao_suporte`.

3. `redirecionado_clinico` não deve determinar automaticamente `papel: fronteira`

A §10.3 está conceitualmente próxima disso:

```text
redirecionado_clinico
→ nova âncora
→ papel: fronteira

```

Quero que a regra normativa deixe explícito que essa derivação não é automática.

O fato de uma evidência ter sido redirecionada pela curadoria é uma informação de fluxo/processo. O `papel` da nova âncora é uma classificação semântica da relação entre a evidência e a entidade.

Portanto:

```text
trajetória de curadoria
≠
papel científico da âncora

```

Se a evidência apenas pertence tematicamente a outra entidade como cross-reference, `fronteira` pode ser adequado.

Se a evidência efetivamente desempenha outro papel em relação à entidade de destino, o `papel` deve refletir essa função, e não o fato de ter sido redirecionada.

Observação final sobre o estado da decisão

O schema já implementa:

```text
trilha = clinica | mecanistica

```

e já restringe corretamente o enum de `uso` conforme a trilha.

Portanto, depois que a Decisão 1 for formalmente tomada pelo responsável, a descrição do campo não deveria continuar dizendo:

```text
"PENDENTE DE DECISAO"

```

A implementação pode estar em proposta, mas o estado semântico da decisão precisa ficar coerente entre minuta, schema e registro da decisão.

Fora esses pontos, considero o JSON v1.2 coerente com a arquitetura apresentada e não vejo necessidade de abrir novos eixos de revisão neste ciclo.
