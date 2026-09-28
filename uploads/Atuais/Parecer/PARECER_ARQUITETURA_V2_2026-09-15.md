# PARECER SOBRE A ARQUITETURA CONSOLIDADA V2 — E O QUE O CONTRATO DO MOTOR PRECISA FECHAR

**Auditor-Mestre · 2026-09-15**
**Objeto:** `ARQUITETURA CONSOLIDADA DA PLATAFORMA V2 — 15.09.26.md` — sha256 `09692e18…`, **46.129 bytes, 1.351 linhas, 30 seções**, conferido byte a byte contra o que a casa declarou no Adendo 1. Confere exatamente.

*Nota: o bloco de texto que me chegou renderizado no corpo da mensagem é uma versão resumida de 13 seções. Auditei o arquivo, não o resumo.*

---

## 1. A V2 extingue a dívida de taxonomia — e é o próprio operador quem a extingue

Na rodada passada eu disse que a decisão que destravava a V-15 não era "como corrigir 158 tokens", e sim **quais camadas o motor lê**. A V2 responde, e de forma vinculante:

> **§28** — *"O Motor não deverá assumir que a Biblioteca Canônica é a camada final de consumo. Ele deverá respeitar a cadeia: Biblioteca → NT → Ontologia → JSONs → Motor, e utilizar a infraestrutura de Evidências/Vínculos para preservar a rastreabilidade."*

Consequência direta, e eu a registro formalmente:

- As **linhas-lote da prosa canônica não estão no caminho de leitura do motor.** Os 158 tokens temáticos (`Arctigenin_2020`, `Bifido_2017`, `taVNS_2020`…) vivem num índice mnemônico legível por humano, dentro da Biblioteca, que o motor não consome. **Deixam de ser dívida de plataforma e passam a ser convenção editorial interna da Biblioteca.**
- O que **está** no caminho de leitura é `/Evidencias/` — ficha e vínculo. Logo, o campo autoritativo de desenho/força de evidência precisa existir **no schema da ficha e no do vínculo**, não na prosa.

**A dívida D-B1-R4-TOKENS encolhe de "4 camadas, 405 tokens, 94 erros" para "um campo no L-05 Nível 1".** Isso é uma redução de escopo de ordem de grandeza, obtida por decisão arquitetural e não por mutirão — que era exatamente o desfecho que eu esperava e não podia impor.

Ajuste correspondente no meu portão: a **V-15 passa a rodar em modo de aviso sobre a prosa e em modo de erro sobre ficha/vínculo.** Publico na próxima versão do P-8. Enquanto isso, os 94 erros de V-15 devem ser lidos como avisos editoriais, não como bloqueio.

## 2. O que a V2 acrescenta e que eu endosso sem ressalva

**§7 LIMITES DA NT.** É a regra de não-elevação escrita como norma, e vai além do que eu havia formulado: *"converter uma relação mecanística em eficácia clínica sem sustentação"* é uma proibição que eu não tinha enunciado e que cobre a falha mais provável de uma camada narrativa. Acrescento uma só observação técnica: a lista de distinções a preservar (fato / associação / causalidade / hipótese / evidência direta / extrapolação / lacuna) **só é verificável por máquina se for um campo enumerado**, não um compromisso de redação. Entra no schema da NT.

**§5.4 e §5.5** resolvem o problema que eu não tinha visto e que apareceria em B2–B16: a evidência existe uma vez e é reutilizada por vínculos, e o aprofundamento mora na Biblioteca do objeto. Sem essa regra, a mesma meta-análise seria catalogada em cinco bibliotecas com cinco fichas divergentes — a versão multiplicada por 146 do problema que passamos quatro rodadas corrigindo na B1.

**§22 cadeia de autoridade** e **§29** (*"nenhuma etapa deve alterar silenciosamente a autoridade científica da etapa anterior"*) formalizam como norma o princípio que vinha operando como acordo bilateral.

**§13 e §14** decidem algo maior do que parece, e quero deixar explícito porque governa tudo que vem depois: a NT produz **unidades narrativas endereçáveis** com `texto_explicativo`, e o motor **seleciona e combina** — não gera. É o significado operacional concreto de "a plataforma não terá IA interna". A consequência prática é que **a NT-B1 não pode ser escrita como prosa corrida**; se for, o motor não consegue montar laudo sem gerar texto de ligação, e a arquitetura trava exatamente no ponto que ela existe para evitar.

## 3. Duas correções de nome — concordo com a casa nas duas

1. O documento cita `/Evidencias/Bibliograficas`; o diretório real é `Evidencias/Bibliografia`. **Adotar o nome real no contrato.** Renomear diretório seria breaking change sem ganho, e quebraria os hashes de todos os pacotes já selados.
2. `direção` aparece com dois sentidos: epistêmico no §5.2 (vínculo) e de grafo no §11 (B1 → S-X). **Adotar `sentido_relacao` (grafo) e `direcao_suporte` (epistêmico).** Colisão de nome em contrato de dados é defeito, não estilo.

## 4. O que a V2 **não** fecha — e o contrato precisa fechar

O §17 lista o que o contrato deve especificar. É um índice do contrato, não o contrato. Os itens abaixo são decisões, não redação, e sem elas o motor não é construível de forma determinística.

**D-01 · Precedência entre mecanismos (L-06).** Continua ausente. Quando B1 e B9 apontam direções opostas para o mesmo achado, o que o motor faz? Sem regra declarada a saída não é reprodutível — e o §24 exige rastreabilidade, que pressupõe determinismo.

**D-02 · Combinação de forças de evidência.** Se uma relação tem suporte de meta-análise humana e outra de modelo animal, como se combinam numa mesma linha de raciocínio? Proponho a regra do **mínimo da cadeia**: a força de uma saída é a menor força do caminho que a produziu — é a única regra que torna a não-elevação do §22 **computável** em vez de declarativa.

**D-03 · Comportamento na ausência de unidade narrativa.** O §12 do texto do operador já diz o princípio ("necessidade de contrato, não autorização para inventar"), mas o comportamento não está definido. Precisa ser: **lacuna nomeada e impressa no laudo**, com o ID que faltou. Silêncio é pior que lacuna, porque o profissional não distingue "não há mecanismo" de "não há unidade escrita".

**D-04 · Texto de ligação entre unidades.** Se o motor só seleciona, as transições entre unidades também precisam ser pré-escritas ou templadas. É o item mais fácil de esquecer e o que mais rapidamente força alguém a ligar um gerador de texto no fim do pipeline.

**D-05 · Granularidade e endereçamento das unidades.** Uma unidade por relação? por claim? por bloco? Isso determina o volume da NT-B1 e, por 146 IDs, o tamanho do projeto inteiro.

**D-06 · Pasta de Atualização no laudo — o item mais sensível.** O §19 autoriza o motor a consultá-la e adia a modalidade para o contrato. É a única rota pela qual ciência **não auditada** alcança o relatório do profissional. Minha recomendação, para constar: conteúdo de Atualização entra **apenas em seção segregada e rotulada**, **nunca** se mistura ao raciocínio mecanístico, **nunca** contribui para classificação ou estratificação, e **nunca** altera a força de uma relação canônica. Se essa fronteira não for escrita agora, ela será atravessada por conveniência depois.

**D-07 · Determinismo como requisito contratual.** A mesma entrada precisa produzir a mesma saída. A V2 implica isso ao dispensar IA interna, mas não o exige em lugar nenhum. Sem cláusula, não há como reprovar uma implementação que o viole.

**D-08 · Hierarquia de segurança na saída.** Risco vital → restrição legal → contraindicação → interação → eficácia → sugestão. Não aparece na V2 e não existe em nenhum portão.

## 5. Posição

A V2 é uma boa norma: decide o que precisava ser decidido na camada certa, e decide contra a conveniência — inclusive fechando uma dívida que a casa e eu vínhamos carregando. Adoto-a como fonte normativa do Contrato do Motor, como o §13 do texto do operador autoriza.

Vou redigir o contrato sobre ela, com uma escolha de método: **para cada uma das oito decisões acima eu escrevo um default declarado, com a justificativa**, em vez de devolver oito perguntas. É mais rápido objetar a um texto do que responder a um questionário, e cada default fica marcado como tal — se o operador ou a equipe científica discordar, muda-se uma cláusula nomeada, não o contrato inteiro.

Ordem de entrega: **L-05 1.1 Contrato da Cadeia (motor) → taxonomia única no schema de ficha/vínculo → precedência (L-06) → `achado_verbatim_fonte` (L-13)**.

---

*Verificações: sha256, byte count, contagem de linhas e de seções do arquivo de arquitetura conferidos contra o Adendo 1 da casa — coincidem exatamente. Seções §5, §7, §13, §14, §17, §19, §22, §23–§25 e §26–§30 lidas na íntegra. Nenhuma afirmação deste parecer depende do resumo recebido no corpo da mensagem.*
