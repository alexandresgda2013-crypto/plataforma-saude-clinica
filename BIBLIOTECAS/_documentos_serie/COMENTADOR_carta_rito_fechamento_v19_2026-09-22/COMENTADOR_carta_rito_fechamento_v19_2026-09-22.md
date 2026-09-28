À ARENA CASA — ENCAMINHAMENTO PARA PARECERES

COMO EXECUTAR v1.9 → proposta de rito de fechamento por rodadas

Arena Casa,

Recebi e analisei integralmente o confronto COMO EXECUTAR v1.9 × L-06 vigente apresentado na rodada 74.

Minha conclusão, neste momento, é que não devemos aprovar o COMO EXECUTAR v1.9 em sua forma atual, mas também não devemos ampliar indiscriminadamente o documento com decisões que ainda não tenham fundamento técnico suficiente.

O encaminhamento que proponho é trabalhar por rodadas de pareceres, cada qual dentro da competência de cada frente, até que as questões materiais estejam resolvidas e então o documento possa ser aprovado de forma limpa.

1. Ponto já suficientemente demonstrado — P1

A medição da Casa demonstrou que a correção conhecida desde 18/09, referente ao papel da IA3, não está incorporada ao v1.9.

O problema não é apenas terminológico.

O rito correto precisa distinguir:

- análise independente das três IAs;
- comparação das três análises somente depois de concluídas;
- parecer da IA3;
- retorno desse parecer às IAs 1 e 2;
- confirmação, alteração ou manutenção de divergência pelas IAs 1 e 2;
- fechamento posterior do claim;
- preservação das divergências e ressalvas materialmente relevantes.

Portanto, considero P1 uma correção necessária para a próxima versão, antes da aprovação final.

A formulação que proponho para o v1.10 é:

> A IA3 produz parecer, não fechamento do claim.
>
> As IAs 1, 2 e 3 devem realizar suas análises de forma independente sobre o mesmo corpus de evidências e a mesma questão do claim. A comparação entre as análises somente ocorre depois de concluídas as três análises independentes.
>
> Após a análise da IA3, seu parecer retorna às IAs 1 e 2. Cada uma registra, por item relevante, se confirma, altera ou mantém divergência em relação à análise anterior, sem apagar ou substituir o registro das análises independentes originais.
>
> O claim não é fechado pela conclusão isolada da IA3, nem pela concordância entre IAs tomada como evidência. O fechamento ocorre somente após a confirmação conjunta das IAs 1 e 2 segundo este rito.
>
> Quando permanecer divergência factual relevante, a resolução deve recorrer à fonte primária ou à evidência correspondente, e não à contagem de concordâncias entre as IAs.
>
> A confirmação final deve preservar as ressalvas, limitações e divergências que permaneçam materialmente relevantes para a afirmação do claim.

Peço à Casa que apresente essa proposta como correção P1, e não como decisão já aprovada, para que Mestre e Estrutura possam emitir parecer dentro de sua competência.

2. O L-06 não precisa ser incorporado ao COMO EXECUTAR

O confronto demonstrou que os dois documentos pertencem a camadas diferentes.

COMO EXECUTAR disciplina a entrada, análise e fechamento do conhecimento clínico.

L-06 disciplina a resolução posterior de relações concorrentes já materializadas na estrutura do sistema.

Não identifiquei, portanto, necessidade de transportar regras do L-06 para dentro do COMO EXECUTAR.

O ponto de convergência entre eles é filosófico e arquitetural:

> divergência não deve ser transformada artificialmente em precedência; quando não houver fundamento suficiente para resolver, a divergência deve permanecer explícita.

Isso pode ser usado como argumento de compatibilidade entre os documentos, mas não como justificativa para acrescentar ao v1.9 regras que pertencem ao L-06.

3. P2 não deve ser resolvida por preferência pessoal do operador

Aqui faço uma correção importante em relação ao enquadramento da pergunta da Casa.

A linha da bifurcação não deve ser definida simplesmente porque o operador prefere uma redação.

Ela deve ser derivada da engenharia do software, da arquitetura documental, da filosofia de rastreabilidade do projeto e da função científica de cada objeto.

A questão técnica a responder é:

> Qual é a trajetória correta de um claim aprovado para que afirmação, evidência, N1, N2 e Biblioteca Canônica permaneçam semanticamente distintos e, ao mesmo tempo, plenamente rastreáveis?

A análise preliminar indica uma bifurcação necessária porque claim, evidência, N1, N2 e Biblioteca não são o mesmo objeto.

Em termos funcionais:

Claim aprovado
→ percurso da afirmação para a Biblioteca Canônica;

e, paralelamente,

evidência que sustenta/limita/contradiz o claim
→ Evidências/Bibliografia
→ N1/N2
→ relações com claim e entidades.

Mas essa é, neste momento, uma conclusão preliminar de engenharia, não uma norma já aprovada.

Solicito, portanto:

Ao Auditor Estrutura

Avaliar P2 sob os seguintes critérios:

1. separação semântica entre claim, evidência, N1 e N2;
2. rastreabilidade bidirecional claim ↔ evidência ↔ relações;
3. não duplicação de evidência;
4. compatibilidade com os schemas vigentes;
5. impacto sobre NT-02 e sobre a materialização na Biblioteca Canônica;
6. necessidade ou não de alteração do Schema-Claim/N1/N2.

O parecer do Estrutura deve responder qual bifurcação é arquiteturalmente necessária, e não apenas sugerir uma frase.

Ao Auditor-Mestre

Avaliar P2 à luz de:

1. filosofia de governança do conhecimento;
2. separação entre afirmação científica e fonte de evidência;
3. cadeia de proveniência e responsabilidade;
4. coerência com o princípio de que o sistema não deve transformar processo de validação em evidência;
5. compatibilidade com o rito de aprovação do claim;
6. eventual risco de a bifurcação alterar o significado epistemológico do claim.

O parecer do Mestre deve responder por que a bifurcação é ou não necessária do ponto de vista epistemológico e de governança.

Somente depois desses dois pareceres deve a Casa consolidar a redação normativa da P2.

4. P3 pertence principalmente ao território do Estrutura

A Casa identificou corretamente a questão de aprovado_com_ressalva.

Não considero apropriado resolver isso por uma frase improvisada no COMO EXECUTAR.

A pergunta estrutural é:

> onde uma ressalva material permanece armazenada quando um claim aprovado é materializado nos objetos estruturais?

Portanto, peço ao Auditor Estrutura parecer específico sobre:

- destino da nota_ressalva;
- preservação da ressalva na passagem para N2;
- rastreabilidade entre estado do claim e vínculo estrutural;
- possibilidade de perda semântica durante a materialização.

O COMO EXECUTAR deve declarar o comportamento operacional, mas não inventar um campo para solucionar uma deficiência de schema.

5. P4 é governança e deve receber parecer antes de virar regra

A questão de quem audita os N1/N2 produzidos pela linha clínica deve ser avaliada como questão de governança, não pressuposta como já resolvida.

O Auditor-Mestre levantou a possibilidade de que, se ele coordenar a produção, exista auditoria adversarial independente.

O Auditor Estrutura seria uma candidata natural para essa função, mas isso deve ser objeto de parecer, não de atribuição automática.

Peço à Casa que encaminhe essa questão separadamente e registre:

- proposta;
- fundamento;
- território responsável;
- eventuais conflitos de função;
- necessidade de segregação de funções.

6. P7 — o piloto do .014 deve ser tratado separadamente da existência do claim

Peço que a Casa preserve a distinção entre:

claim .014 já trabalhado/fechado em determinado estado

e

piloto do protocolo COMO EXECUTAR v1.9 efetivamente executado e medido como piloto do processo.

Para fins de homologação do v1.9, deve existir um registro específico do piloto.

Além disso, o desenho do piloto deve respeitar a independência das três IAs:

mesmo corpus + mesma questão → IA1 independente

mesmo corpus + mesma questão → IA2 independente

mesmo corpus + mesma questão → IA3 independente

e somente depois:

comparação → retorno da IA3 → confirmação pelas IAs 1 e 2.

Isso é importante para impedir que as análises posteriores apenas auditem ou reproduzam a análise anterior por efeito de ancoragem.

7. Proposta de rito de aprovação

Minha recomendação é que a Casa não tente obter uma aprovação única neste momento.

Proponho o seguinte fluxo:

Rodada 1 — Casa → Auditor-Mestre + Auditor Estrutura

Enviar o v1.9, a correção P1 proposta e as questões P2/P3/P4 separadas por competência.

Rodada 2 — pareceres independentes

Mestre e Estrutura respondem separadamente, sem que um parecer seja usado como fundamento do outro antes da entrega.

Rodada 3 — Casa

A Casa faz confronto mecânico, separa:

- concordância;
- divergência;
- questão fora de território;
- questão ainda sem dados.

Não transforma divergência em consenso.

Rodada 4 — retorno aos territórios responsáveis

Cada auditor responde somente aos pontos ainda divergentes do seu território.

Rodada 5 — consolidação

A Casa apresenta uma proposta consolidada de v1.10 e um quadro explícito das questões que ainda permanecem abertas.

Rodadas adicionais

Continuam enquanto existir divergência material entre os pareceres.

Fechamento

Quando Mestre, Estrutura, Comentador e Casa estiverem materialmente de acordo com o texto final, o documento é encaminhado ao operador para a formalização da aprovação.

A aprovação final pelo operador, portanto, será ato de homologação de uma solução tecnicamente construída, e não uma escolha pessoal arbitrária entre alternativas técnicas.

8. Pedido específico à Arena Casa

Peço que você transforme esta carta em dois encaminhamentos técnicos, preservando a separação de competências:

Encaminhamento ao Auditor-Mestre

Concentrar-se em:
filosofia, governança epistemológica, proveniência, papel das IAs, fechamento do claim, P2 e P4.

Encaminhamento ao Auditor Estrutura

Concentrar-se em:
arquitetura, schemas, materialização, N1/N2, destino da ressalva, bifurcação P2 e consequências estruturais.

A Casa deve solicitar pareceres, não pedir aprovação automática.

Depois dos pareceres, a própria Casa deve fazer nova réplica e apresentar somente as divergências restantes para uma nova rodada.

O objetivo não é chegar rapidamente a uma assinatura. O objetivo é chegar a um texto em que cada regra tenha fundamento técnico identificável, cada campo tenha destino definido e cada decisão possa ser rastreada à competência correta.

Neste momento, considero:

P1 — suficientemente demonstrada para correção no v1.10.

P2 — aberta, devendo ser derivada por engenharia + filosofia + função científica, e não por preferência pessoal.

P3 — aberta no território estrutural.

P4 — aberta como questão de governança.

P7 — requer registro próprio do piloto.

Por favor, encaminhe essas questões aos respectivos territórios e retorne com os pareceres para nova rodada de análise.

Não tratar este encaminhamento como aprovação do v1.9.
