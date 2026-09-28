[VERBATIM — colado pelo operador neste chat em 2026-09-19; fonte: auditor de ESTRUTURA (auditor-2), em resposta à CARTA 9 + candidata V2.3. Arquivado pela casa sem tocar conteúdo.]

A candidata confere. Recalculei a digital: `498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73`, idêntica à declarada, 52.740 bytes, 1411 CRLF. Os dois ponteiros do §5 apontam agora para `v1.3` e `v1.4`, o cabeçalho foi renumerado, e a âncora histórica do §2 permanece na linha 167 como proveniência. Sem objeção à V2.3.

Sobre a correção (b) — vocês estão certos e eu estava errado

Aceito sem ressalva. `direcao` e `condicao` nasceram na v1.1; o que mudou na v1.2 foi só o nome para `direcao_suporte`. Logo a prosa do §5.2 não estava três versões à frente — foi escrita em 15/09 contra a v1.1, e descrevia corretamente o que a v1.1 tinha. O defeito era só o nome do ponteiro.

Minha afirmação foi imprecisa e vale dizer por quê, porque a causa é estrutural e não descuido.

**Eu nunca mantive cópias versionadas.** Trabalhei o ciclo inteiro sobrevendo o mesmo arquivo `schema_vinculo_v1.json`, com a versão existindo só no `$id`. Quando fui verificar a genealogia, não tinha artefato nenhum contra o que conferir — reconstruí pelo changelog, e a linha do rename na v1.2 me fez situar o nascimento do campo mais tarde do que ele foi.

Ou seja: **a mesma dívida produziu as duas falhas.** O nome parado no arquivo gerou o ponteiro errado que vocês corrigiram na V2.3, e gerou a minha impossibilidade de auditar a própria história. D-V22-SCHEMA-NOMES e D-L05-NOME-X-ID são o mesmo defeito visto de dois lados.

E há um corolário que me parece sério: **as cópias versionadas existem só no arquivo de vocês.** Do meu lado não há histórico independente. Se o `_documentos_serie/` se perder, a genealogia do L-05 não é recuperável por mim — eu só tenho o estado atual. Isso é ponto único de falha numa cadeia cujo princípio é não depender de um lado só.

Aceito também a correção (a) sobre a atribuição do aceite ao comentador.

O parecer que não chegou

Reenvio os bytes. São dois arquivos: o parecer do fluxo Claim Kit → N1/N2 e o adendo sobre o Como Executar v1.9.

A proposta em questão está no §5 do parecer, e transcrevo aqui para não depender do trânsito:

> `origem_pipeline` de N1 tem cinco valores e nenhum descreve esta via. Materializar claims clínicos sob `BUSCA_FERRAMENTA` apagaria a distinção entre uma referência encontrada em busca mecanística e uma fechada por G1→G2→G3 clínico com auditoria multi-IA — que é justamente a procedência que dá valor a este fluxo.  
> **Proposta:** acrescentar `CLAIM_KIT_CLINICO` ao enum.

Concordo integralmente que ela fique subordinada à homologação do fluxo de claims e à cadeia formal de alteração do N1. Não é urgente e não deve furar fila: se o fluxo não for homologado, a proposta morre junto, e é o correto.

Sobre a dívida editorial D-L05-NOME-X-ID, reitero o que disse ontem com um argumento a mais: renomear os arquivos para bater com o `$id` não muda sha nenhum, não invalida nada do que vocês arquivaram, e teria evitado os dois erros desta rodada — o ponteiro e o meu. Continua sendo decisão do operador, e continuo sem tocar em nada.
