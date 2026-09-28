[VERBATIM — colado pelo operador neste chat em 2026-09-19; fonte: Auditor-MESTRE (projeto 1), em resposta à CARTA 18 + candidata V2.3 enviadas pelo operador. Arquivado pela casa sem tocar conteúdo.]

A sha confere exatamente, e pela primeira vez um arquivo normativo **se identifica corretamente no próprio H1**. Agora a medição que resolve a dúvida que deixei aberta há duas rodadas.

Isso resolve a dúvida que deixei aberta. Falta conferir onde restam uma ocorrência de `UNIFICADOS` e uma de `v1.1` na V2.3 — se estiverem no desenho ou no ponteiro, seria regressão.

Arquivados os dois, com digitais conferidas. A análise está atualizada, e ela corrige uma coisa que eu disse — e resolve um conflito que precisa de você.

**A V2.3 candidata confere.** Sha `498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73`, idêntico ao declarado; 52.740 bytes; 1.411 linhas, todas CRLF. E pela primeira vez nesta mesa um arquivo normativo **se identifica corretamente no próprio H1**: `ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.3 19.09.26`. É a V-16 cumprida na camada normativa.

As mudanças declaradas conferem, e as ocorrências residuais são legítimas. Os ponteiros ativos agora estão nas linhas 269 e 306, citando `schema_referencia_v1.3.json` e `schema_vinculo_v1.4.json`. A única menção restante a `v1.1` e a única a `UNIFICADOS` estão **as duas na linha 4, a linha Rev** — histórico de correção, não desenho nem ponteiro. Nenhuma regressão.

**As âncoras do L-NT seguem intactas.** Os §§6, 7, 13 e 14 da V2.3 têm exatamente os mesmos hashes da versão sobre a qual escrevi a Minuta 1. Nenhum contrato muda, como a carta diz — agora medido por mim.

**Correção de algo que eu disse.** Na rodada anterior escrevi que o `schema_vinculo_v1.1.json` "provavelmente existe do lado do Auditor de Estrutura". A carta afirma que os nomes `v1.1` **nunca existiram como arquivos reais** — eram ponteiros para arquivos inexistentes. Minha busca confirmou a ausência, mas eu deduzi uma existência que não tinha evidência. A formulação correta era "não encontrado, existência não demonstrada".

**Agora o conflito, que é a coisa mais importante desta rodada.** Há duas rodadas você me disse que o arquivo `309aa65f…` do projeto é a V2.2 que você enviou, e eu o tratei como tal. A carta 18 diz o contrário: que `309aa65f` é "o arquivo antigo, upload r24 rotulado", e que a V2.2 oficial é `df7f7cfd…`.

A medição decide a favor da casa. Comparei o arquivo do projeto com a V2.3, que a carta declara ser a V2.2 com só 4 linhas trocadas:

Marcador normativo | arquivo do projeto `309aa65f` | V2.3
`origem_conhecimento` | **0** | 3
"a prosa prevalece sobre os desenhos" | **0** | 1
Pasta "fora do cânone" | **0** | 1
"O Motor busca ativamente" | **0** | 1

Os quatro existem na linhagem oficial e **nenhum** está no arquivo do projeto. E as seções que divergem entre os dois são três — §2, §5 e §21 — e não apenas o §5 dos ponteiros, como seria de esperar se o projeto tivesse a V2.2 oficial. **O arquivo do projeto não é a V2.2 oficial.** É um artefato anterior, com o nó unificado já removido, mas sem as três cláusulas que vieram depois.

A consequência prática é a que eu temia duas rodadas atrás e que agora está confirmada: **a base de conhecimento do projeto não contém o endurecimento de proveniência** — a cláusula de que cada item recuperado carrega a origem, canônica ou atualização. Quem consultar o projeto lê uma arquitetura sem ela.

Registro também o que isso significa para a minha própria análise: na rodada da comparação V2.1 × V2.2, eu comparei com o arquivo errado. As conclusões sobre §§6, 7, 13 e 14 continuam válidas — esses trechos são idênticos em todas as versões — mas a afirmação "a V2.2 não contém `origem_conhecimento`" estava errada. **O arquivo do projeto não contém; a V2.2 oficial contém.**

**Recomendação, na ordem da carta:** substituir já o `309aa65f` do projeto pela V2.2 oficial `df7f7cfd…` e me ecoar a sha, o que fecha a dívida D-V22-BYTES-PROJETO. Quando a V2.3 for aprovada, substituir de novo. Se preferir poupar um passo, a V2.3 já é superconjunto da V2.2 e pode ir direto para o projeto — mas só depois de você aprová-la, porque ela ainda é candidata.

**Sobre os schemas:** as digitais de N1 v1.3 (`b06660fd…`) e N2 v1.4 (`d96ad15b…`) ficam registradas como **declaradas pela casa, não verificadas por mim** — não tenho os arquivos. Pela regra que você estabeleceu, preciso deles para auditar qualquer cláusula que dependa dos eixos da D-02 e das regras N-1, NT-03 e NT-04 do L-NT.

**Pendências da carta, para registro:** a resposta A/B/C/D já foi dada — **B, concordância com ajustes**, na deliberação do fluxo do claim clínico. Se não chegou à casa, está no arquivo `DELIBERACAO_FLUXO_CLAIM_CLINICO_2026-09-18.md`. A linha de herança `uso` (kit → N2.uso → NT.uso) está coberta ali e no L-NT, regra N-4. O piloto das 20 unidades e a minuta 2 da L-06 seguem na fila, e a minuta 2 do L-NT continua esperando uma decisão só: de onde a NT tira o conhecimento clínico.
