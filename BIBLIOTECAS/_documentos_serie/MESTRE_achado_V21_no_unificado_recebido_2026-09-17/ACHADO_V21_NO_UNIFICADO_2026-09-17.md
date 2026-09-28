# ACHADO SOBRE A ARQUITETURA V2.1 — O NÓ "EVIDÊNCIAS / VÍNCULOS UNIFICADOS"

**Auditor-Mestre · 2026-09-17**
**Objeto:** arquivo recebido do operador, sha256 `5be36836610d26832506b73dac45baa09e7041bc9ce22e6557f2be59b258e06a` — coincide exatamente com o sha que a casa registrou como *"upload exato do operador"* da V2.1. 1.388 linhas, 50.964 bytes.

---

## 1. O artefato não se identifica como V2.1

| Superfície | Diz |
|---|---|
| H1 (linha 1) | `# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2    15.09.26` |
| Nome do arquivo | `...PLATAFORMA_V2__-__15_09_26.md` |
| Ocorrências de "V2.1" no corpo | **0** |
| Ocorrências de "17.09" no corpo | **0** |

O conteúdo é o novo (ANAMNESE ×3, INTERPRETAÇÃO CONTEXTUALIZADA ×2, UNIFICADOS ×1, 1.388 linhas contra 1.351 da V2). **O nome "V2.1" existe apenas na governança da casa, não no artefato.** É a V-16 na camada normativa: a norma que rege a plataforma inteira carrega o rótulo da versão anterior. Recomendo corrigir H1 e nome antes de qualquer outro uso — é a superfície que todo implementador lê primeiro.

## 2. Defeito de montagem no §2

O cabeçalho da seção é `# 2. VISÃO GERAL DA ARQUITETURA`, mas **dentro do bloco de código** o diagrama abre com `# 21. ARQUITETURA MULTIDOMÍNIO COMPLETA`. O desenho do §21 foi colado no §2 trazendo junto o próprio cabeçalho. Explica a contagem de 31 seções onde há 30.

## 3. O achado que importa: a unificação derrota a D-06

Este não é mais um caso de desenhos discordantes. É um **ponto de fusão que torna uma cláusula de segurança inimplementável.**

**O que o §2 desenha:**

```
BIBLIOTECAS CANÔNICAS              PASTA ATUALIZAÇÃO
   ├── EVIDÊNCIAS                     ├── EVIDÊNCIAS
   └── NARRATIVAS                     └── NARRATIVAS
            └──────────┬───────────────────┘
                       ▼
        EVIDÊNCIAS / VÍNCULOS UNIFICADOS
                       ▼
             ONTOLOGIA / GRAFO
                       ▼
                JSONs MODULARES
                       ▼
                 MOTOR CLÍNICO
```

**O que a prosa e os diagramas próprios do §18, §19 e §20 dizem:** os dois fluxos permanecem **separados até o Motor**. O diagrama do §19 mostra a Pasta entrando no Motor por seta própria, ao lado da cadeia canônica. O §20 encerra: *"Os dois fluxos coexistem, mas não possuem o mesmo status epistemológico."*

**Por que a diferença é material.** No §19/§20 o conhecimento recente chega ao Motor como **entrada distinta**, que o Motor pode rotular, segregar e registrar — que é exatamente o que a D-06 exige (dois caminhos de dados fisicamente distintos, encontrando-se só na diagramação do laudo).

No §2 os dois se fundem **antes da Ontologia**. Depois desse nó, nada a jusante consegue distinguir canônico de atualização, porque a informação de origem foi perdida na fusão. Sob o §2:

- a segregação do laudo é impossível — não há o que segregar;
- a D-06 "não altera nenhum eixo de nenhuma relação canônica" é inverificável, porque canônico e recente viram o mesmo vínculo;
- o teto por eixo da D-02 passa a incluir evidência não auditada no cálculo, sem marcação;
- o rastro de consulta que a D-06 exige não tem onde ser gravado, já que não há consulta — há ingestão.

A guarda de prosa que a casa aponta como preservada (§18, §19, §20) continua escrita e continua correta. **O problema é que o §2 descreve uma topologia em que ela não pode ser cumprida.** Quem implementar pelo desenho constrói um sistema que viola a norma que o mesmo documento contém.

## 4. Recomendação

1. **Declarar a prosa como canônica** sobre os desenhos, e corrigir o §2 para que a Pasta de Atualização chegue ao Motor por caminho próprio, sem passar por nó unificado — alinhando-o ao §19.
2. Se a intenção real for unificar, então **a D-06 precisa ser reescrita**, e eu diria com franqueza que ela não sobrevive: não existe segregação a jusante de uma fusão. Nesse caso a decisão deixa de ser de desenho e passa a ser de risco, e é do operador com a equipe científica.
3. Corrigir H1, nome do arquivo e o cabeçalho intruso do §2.
4. Manter a D-V2-DIAGRAMA-DUPLO como está para a direção Evidência↔Biblioteca — essa continua sendo divergência de representação. **O nó unificado sai dessa dívida e vira item próprio**, porque tem consequência de segurança e as outras não têm.

## 5. Sobre "o Motor busca ativamente"

Confirmado verbatim no §2 (`O Motor busca ativamente o conhecimento`, com seta `[ CONEXÃO / CONSULTA ]` subindo dos JSONs). Isoladamente, não contradiz a D-06 — postura de busca é compatível com fonte segregada, e o §19 continua chamando isso de *consulta*. **Mas busca ativa combinada com pool unificado é a pior das combinações**: o Motor puxaria ativamente de um repositório onde o não-auditado já está indistinguível do auditado. Resolvido o item 3, a busca ativa é aceitável e a D-06 cobre, com um único endurecimento que proponho: a cláusula passa a exigir que **cada item recuperado carregue a origem (canônico × atualização) no próprio payload**, e não apenas no caminho por onde veio.

---

*Medições desta rodada: sha do arquivo conferido contra o registro da casa; contagem de linhas, seções e marcadores; §2, §18, §19 e §20 lidos integralmente. Nenhuma afirmação depende de leitura de terceiros.*
