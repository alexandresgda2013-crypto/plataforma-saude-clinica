# SUBSCRIÇÃO REV.3 — AUDITOR-ESTRUTURA — SCHEMA-CLAIM v1.3 (arquivado verbatim; inclui epílogo do arquivo errado e fecho)

**Data:** 2026-09-25 · **Objeto:** minuta Schema-Claim v1.3 rev.3

## Epílogo (registro honesto do operador e da casa)

O operador havia enviado primeiro a rev.2 por engano; o Estrutura detectou ("o anexo tem rev.2 no nome e no corpo... para em V-K5"), recusou medir o que não tinha, mas confirmou pela formulação da aceitação do Comentador que V-K6/V-K7 eram as dele. Depois o operador enviou a rev.3 correta.

## Texto do primeiro momento (rev.2 errada — registrado)

Recebi a rev.2 do arquivo, não a rev.3 — o anexo tem "rev.2" no nome e no corpo, e para nele em V-K5. As duas confirmações que você resume, do Comentador e da carta do operador, descrevem V-K6 e V-K7, que não estão neste arquivo. Então não posso medir a rev.3 contra o schema; só tenho a descrição dela.

Mas há uma coisa que eu posso fazer sem a rev.3 em mãos, e ela basta: verificar se a formulação de V-K6 e V-K7 que o Comentador transcreveu é a minha, e se resolve a colisão que eu apontei.

**V-K6** — o Comentador escreve: havendo `ressalva[tipo=condicao_aplicacao]`, a materialização usa `condicional` + `condicao`; o `sentido_do_achado` fica preservado no claim e não vira `direcao_suporte` neste ato; sem `condicao_aplicacao`, vale o mapeamento normal. É exatamente a precedência que pedi, na ordem que pedi. Foi a regra que testei: `sustenta` + `condicao` reprova no N2, `condicional` + `condicao` passa. V-K6 escolhe o ramo que passa.

**V-K7** — quando `grau_maturidade_cientifica` está vazio, o campo é **omitido** na materialização, não gravado como `null`. É o alinhamento fino que apontei... Resolvido como sugerido.

As duas correspondem à ressalva. No conteúdo, a rev.3 fecha o que faltava.

Por isso vou dar a subscrição, mas com o alcance exato do que verifiquei... **Uma condição só, e é de forma, não de mérito:** que a rev.3 que vai a registro contenha essas duas regras no texto, com o número de versão batendo... Se a Arena confirmar que a rev.3 canônica tem V-K6 e V-K7 no corpo e me passar a digital, a subscrição é lisa e sem qualquer reserva.

## Texto final (rev.3 correta recebida)

Agora é a rev.3, e ela contém as duas regras. Cabeçalho, changelog e corpo dizem rev.3, com V-K6 escrito no campo `sentido_do_achado` e no bloco de validadores, e V-K7 logo abaixo. O arquivo que fica no registro é o que estou subscrevendo.

Rodei o teste final contra o N2 v1.4:

- **V-K6 aplicado** (condicional + condicao) → válido.
- **V-K6 ignorado** (sustenta + condicao, que era a armadilha) → reprova, que é exatamente o que a regra existe para evitar.
- **V-K7** (grau ausente omitido) → válido.

A precedência está escrita na ordem que pedi: havendo `condicao_aplicacao`, materializa `condicional` + `condicao`, e o `sentido_do_achado` fica registrado no claim sem virar `direcao_suporte` naquele ato. É contrato de materialização, não toca o N2, não cria segunda semântica.

**Subscrevo sem ressalva a minuta Schema-Claim v1.3 rev.3.**

Do meu território não resta nada em aberto no ciclo do kit. As duas pendências que continuam são as já registradas e não são minhas para fechar: os campos P-K1 e P-K2 precisam existir no kit antes da primeira materialização, e a P-K6 — a representação fiel do `inverte`, com campo de condição que coexista com `sustenta`/`refuta` — fica no ciclo do N2 v1.5. Enquanto a P-K6 não sair, claim com inversão de direção não materializa, e isso está corretamente travado por artefato.

Uma nota de fecho, já que este foi um ciclo longo. O V-K6 é a terceira vez que a mesma classe de erro apareceu: dois eixos separados no papel colidindo num campo só. No R7 foi `refuta` dentro de `papel`; no D1 foi direção derivada de estado de validação; aqui foi direção e condição convergindo na saída. As três só apareceram porque foram rodadas contra o schema em vez de aceitas pela lógica — e a terceira teria passado batida se a subscrição fosse pela descrição. Vale como o registro central deste ciclo: o que sustentou o rigor não foi a concordância entre as mesas, foi cada afirmação ter sido reexecutável contra o artefato. Confirmada a cópia, está fechado do meu lado.
