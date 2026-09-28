[VERBATIM — colado pelo operador neste chat em 2026-09-19; fonte: auditor de ESTRUTURA (Claude auditor-2), em resposta à pergunta do operador "você sabia da versão 1.1?". Arquivado pela casa sem tocar conteúdo.]

Confirmo, e o achado é o próprio motivo de você não estar encontrando.

## 1. O arquivo com esse nome nunca existiu

Nenhum artefato chamado `schema_vinculo_v1.1.json` foi produzido em momento algum. O arquivo sempre se chamou `schema_vinculo_v1.json`, com o número da versão vivendo apenas no campo `$id` interno, que foi evoluindo enquanto o nome ficou parado.

A casa registrou isso sem nomear como defeito: a carta 3 lista o objeto como *"`schema_vinculo_v1.json` (conteúdo **v1.1**)"*. Os dois lados já sabiam que nome e conteúdo diziam coisas diferentes.

É a terceira ocorrência da mesma doença neste ciclo — depois do título da minuta e do rodapé do §4B — e desta vez foi o nome do arquivo. Minha responsabilidade.

## 2 e 3. Localização e versão vigente

A versão vigente é a **v1.4**, e a v1.1 está superada por três incrementos.

| $id interno | sha256 | estado |
|---|---|---|
| `L05/schema_vinculo_v1.1.json` | `b0934412…` | superado — rodada 15/09 |
| `L05/schema_vinculo_v1.2.json` | `19f4f29a…` | superado — rodada 16/09 |
| `L05/schema_vinculo_v1.3.json` | `ec4f0de8…` | superado — rodada 17/09 |
| `L05/schema_vinculo_v1.4.json` | `d96ad15b…` | **vigente** |

Conferi agora a minha cópia de trabalho: `$id` = `L05/schema_vinculo_v1.4.json`, sha256 começando em `d96ad15b620fa373`. Bate exatamente com a digital que a casa publicou na carta 8. O par N1 está em `b06660fd985a8186`, também idêntico ao registrado por eles.

O `L05/` que aparece nos `$id` e na V2 é **caminho declarado, não diretório existente**. A casa registrou na carta 3 que ele vira diretório canônico quando o 1.2 for normatizado. Hoje as cópias oficiais estão no arquivo verbatim da casa, em `_documentos_serie/`, uma pasta por rodada de recebimento.

## 4. Referência oficial

A v1.4, pelo sha `d96ad15b…`. As anteriores são histórico arquivado, não alternativas.

**E há um ponteiro errado em circulação que provavelmente originou a sua busca.** O §5.2 da Arquitetura Consolidada V2 aponta para `L05/schema_vinculo_v1.1.json`, e o §5.1 para `L05/schema_referencia_v1.1.json`. Os dois apontam para versões superadas, sob nomes que não existem. Pior: a lista de campos do próprio §5.2 já descreve a v1.4, porque menciona direção da relação e condição, que nasceram ali. A prosa está três versões à frente do ponteiro.

## 5. Governança, dependências e ressalvas

- **O schema é PROPOSTA, não normativo.** A casa aprovou como base de fechamento, sem ressalva estrutural, mas o L-05 ainda não foi declarado normativo.

- **Dependência crítica não resolvida:** a regra central do N2 manda validar `ancoras[].id_oficial` contra o catálogo oficial — e o catálogo ainda não existe como arquivo adotado. Há um derivado candidato com sha `d0ff2647…` que reproduz os 146, mas a adoção formal não saiu. Enquanto não sair, o schema aponta para uma fonte que ninguém declarou.

- **Regras que ficaram fora do schema por desenho, e dependem do portão L-05 que ainda não nasceu:** integridade referencial da âncora principal, obrigatoriedade de `forca_biologica_conexao` em BLOCO_07/08, e a identidade do avaliador com padrão ancorado.

- **Efeito já declarado sobre o acervo:** os 20 vínculos redirecionados ficam não-conformes até ganharem a segunda âncora. É intencional.

- **Pendente do meu parecer de ontem, ainda não incorporado:** acrescentar `CLAIM_KIT_CLINICO` ao enum de `origem_pipeline` do N1.

## Sugestão, para você decidir depois

Não alterei nada, como pedido. Mas a correção que evita essa busca se repetir é barata e não toca conteúdo: renomear o arquivo para bater com o `$id`, e corrigir os dois ponteiros do §5 da V2. Renomear não muda o sha, então nada do que a casa arquivou perde validade — e a próxima pessoa que procurar pelo nome o encontra.
