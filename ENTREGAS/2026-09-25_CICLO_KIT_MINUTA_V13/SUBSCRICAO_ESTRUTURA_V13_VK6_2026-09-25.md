# SUBSCRIÇÃO COM RESSALVA — AUDITOR-ESTRUTURA — SCHEMA-CLAIM v1.3 (texto do operador; arquivado verbatim)

**Data:** 2026-09-25 · **Objeto:** minuta Schema-Claim v1.3 rev.2

Cinco pontos de território, mais um teste que os validadores da minuta não fazem e que decide se a materialização vai bater no N2. Rodei antes de responder.

Terminei. Rodei a minuta contra o schema real, e ela passa nos três caminhos que ela desenha — mais uma armadilha que precisa virar validador.

**Subscrevo com uma ressalva.** Não é impedimento; é um validador que falta e um alinhamento de vocabulário. Ponto a ponto:

**Sintaxe e estrutura — corretas.** A minuta faz só o que o contrato mandou: `sentido_do_achado` por fonte, `ressalvas[]` com tipo, fonte única de condição, maturidade. Não reabre D1, não toca N1/N2, não importa os eixos mecanísticos que não deve — e o Comentador está certo em barrar `forca_causal` e `forca_biologica_conexao`, que eu mesmo já tinha dito não pertencerem à trilha clínica.

**Compatibilidade com N2 — testei os três caminhos e batem.** `condicao_aplicacao` → `condicional`+`condicao` é válido; heterogeneidade → `sustenta`+`condicao` nula é válido; maturidade → sem `condicao` é válido. O mapa do P-K1 (`suporta_relacao`→`sustenta` etc.) tem imagem inteira dentro do enum do N2, e `condicional` não é gerável por ele — nasce só do P-K3, que é exatamente a separação de eixos que fechou o D1.

**A ressalva: falta o validador que impede a armadilha do D1 de voltar por trás.** Os validadores V-K1 a V-K5 verificam o lado do claim, mas nenhum verifica o par que chega ao N2. Simulei o caso: um claim que tem, ao mesmo tempo, `sentido_do_achado: suporta_relacao` **e** uma `ressalva[tipo=condicao_aplicacao]` com condição. Qual ganha na materialização? Se o materializador copiar os dois — direção `sustenta` e a condição — o vínculo sai com `sustenta`+`condicao` preenchida, e **o N2 reprova**, porque `condicao` só é permitida com `condicional`.

Esse é o mesmo colapso do D1, entrando pela porta dos fundos: dois eixos que a minuta separou no claim voltam a colidir no ato de materializar, porque ninguém definiu a regra de precedência entre `sentido_do_achado` e `ressalva[condicao_aplicacao]` quando os dois existem na mesma fonte.

Falta um V-K6, e ele é de contrato de materialização, não de schema do kit: **quando uma fonte tem** `ressalva[tipo=condicao_aplicacao]`, **a direção materializada é** `condicional` **e a** `condicao` **vem da ressalva; o** `sentido_do_achado` **daquela fonte fica registrado no claim mas não vira** `direcao_suporte`. Ou, se a mesa preferir a regra inversa, que ela seja escrita — o que não pode é ficar indefinida, porque aí a primeira materialização com esse par reprova no schema sem ninguém saber por quê.

**Um alinhamento fino, não bloqueante:** o `grau_maturidade` do N2 aceita `null`, e o `grau_maturidade_cientifica` da minuta não lista `null` no destino — mas a minuta marca o campo como opcional, então o caso de origem vazia precisa mapear para ausência no N2, não para `null` gravado. É uma linha na tabela de materialização, resolve sozinho.

**Migração e validadores — corretos e bem calibrados.** Não reescrever o corpus de 17/09 retroativamente é a decisão certa: preencher `sentido_do_achado` em claim antigo agora seria inventar decisão que não foi tomada na leitura original. A falha dura só no momento em que o claim tenta materializar é o gatilho no lugar certo. E o ajuste V-K3 do Comentador está bem posto — exigir direção de exploratória que não materializa seria transformar requisito de N2 em regra de qualidade do kit, que são coisas diferentes.

Resumindo a subscrição: **subscrevo com a ressalva de que o V-K6 (precedência condicao_aplicacao × sentido_do_achado na materialização) seja adicionado antes do congelamento.** Com ele, a minuta fecha e a primeira materialização não bate no schema. Sem ele, o par convergente reprova em silêncio — e seria a terceira vez neste ciclo que dois eixos separados no papel colidem num campo só, agora no ponto de saída em vez do de entrada.

A ressalva é de contrato de materialização, então pertence ao mesmo lugar que resolveu o D1 e a P-K6, não a uma alteração do N2.
