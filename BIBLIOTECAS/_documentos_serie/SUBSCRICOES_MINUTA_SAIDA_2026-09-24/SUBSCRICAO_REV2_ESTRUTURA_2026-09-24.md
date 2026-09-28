# SUBSCRIÇÃO REV.2 — AUDITOR-ESTRUTURA (texto enviado ao operador; arquivado verbatim)

**Data:** 2026-09-24 · **Objeto:** MINUTA rev.2

A rev.2 incorporou o meu ponto exatamente como eu o coloquei — e melhorou com a granularidade do Comentador. Verifiquei antes de assinar.

Meu §4.3 pedia três coisas, e as três estão na rev.2: o par `sustenta`+condição foi tirado, porque o schema o reprova; o `inverte` virou dependência estrutural não resolvida, com o mesmo tratamento da maturidade — informação fica no claim, acessível por `claim_id`, e não materializa em N2 até existir campo próprio; e o campo que eu sugeri está nomeado na P-K6 como `condicao_modificadora` + `allOf`, endereçado ao ciclo v1.5. A P-K4 antiga — a regra que mandava criar os dois N2 e que o N2 reprova — foi marcada como superada, não apagada. O histórico ficou visível, que é como deve ser.

A precisão do Comentador conserta uma coisa que eu tinha deixado grosseira. Eu falei em travar o `inverte` sem dizer o alcance. Bloqueio global do corpus clínico por causa de um caso seria pesado demais. A rev.2 fecha por artefato: só o claim afetado por `inverte` bloqueia, o resto segue os portões. Fail-closed onde há o problema, aberto onde não há. `B1.SM02.001b` é o único caso identificado hoje.

Confirmei também a citação do §3.1 na v3.1 que veio anexa: `sentido_do_achado: suporta_relacao | refuta_relacao | inconclusivo`, obrigatório. O mapeamento do R-1 está correto contra a fonte.

Então, à pergunta única:

**Subscrevo sem ressalva.**

A minuta rev.2 corresponde ao N2 v1.4 em cada linha da tabela de materialização — testei a que faltava, o `inverte`, e agora ela diz "não materializa" em vez de descrever um par inválido. A assinatura afirma correspondência com o schema, e desta vez a correspondência é verdadeira.

Registro o alcance do que estou assinando, para o livro:

O que fica **vigente** ao fechar D1 é o contrato de derivação Claim→N2 — dois eixos, sem default, fonte única de condição. Não toca N1 nem N2, e está certo assim.

O que fica **travado** são as seis pendências. Três são do ciclo do kit e são pré-condição da primeira materialização: sem campo de direção por fonte (P-K1) e sem `ressalvas[]` com tipo (P-K2), o R-1 e a classificação não têm onde ser gravados. A P-K6 é do meu território — a alteração do N2 no ciclo v1.5 — e enquanto ela não existir, nenhum claim com inversão de direção materializa. Isso é limitação real e vale dizer em voz alta: o `.001b` fica em espera até o v1.5, não é caso resolvido.

Uma nota de método, já que este é o fecho de D1. A divergência começou num mapeamento meu errado, sobreviveu porque a simetria de obrigatoriedade parecia prova, e só caiu quando foi medida contra o schema em vez de discutida. O `inverte` teria passado batido se eu tivesse subscrito a rev.1 pela lógica — ele só apareceu porque rodei o par contra o `allOf`. Vale como registro do que fez este ciclo funcionar: não foi concordância entre as mesas, foi cada afirmação ter sido reexecutável contra o artefato. É o mesmo princípio que o Comentador colocou lá atrás, e que agora está provado nas duas pontas.

Do meu lado, D1 pode encerrar assim que o Mestre subscrever. Não há pendência estrutural minha em aberto além da P-K6, que já está na fila certa.
