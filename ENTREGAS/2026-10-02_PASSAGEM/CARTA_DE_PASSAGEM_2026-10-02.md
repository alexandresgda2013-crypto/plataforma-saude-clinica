# CARTA DE PASSAGEM — de um agente do chat (Arena) para o próximo agente do chat

**Data:** 02/10/2026

## 0) COMO TRABALHAR COM ESTE OPERADOR (leia antes de agir)

- Linguagem simples e analógica. Termo técnico (ex.: "diff") sempre com analogia.
- Respostas curtas: uma tabela, uma pergunta. Dê posição técnica fundamentada (critério: o que é CORRETO em engenharia de software e em ciência), não opinião de ninguém. Concorde ou discorde com o porquê. NÃO use o operador como bengala e NÃO devolva a ele decisões técnicas que são suas. Também NÃO tome decisão que é dele sozinho: o que não foi pedido, pergunte.
- ORDEM DAS COISAS: se há decisão dele pendente, pergunte PRIMEIRO, em uma linha. Só depois do "sim" escreva a carta ou a mensagem. Nunca entregue carta pronta junto com pergunta aberta.
- CARTAS PARA AUDITORES: curtas. O operador aparece só em terceira pessoa ("o operador decidiu"), nunca em segunda pessoa, e a carta não faz pergunta nem dá instrução a ele. NÃO detalhe quem redigiu a frase de aprovação (casa ou operador) nem "ele colou depois": é cosmético; o que vale é o operador tê-la colado no chat com data.
- Mensagens para agentes vão DIRETO NO CORPO DO CHAT, em bloco de código com cerca externa de 4 crases. O operador só COLA TEXTO (anexo não funciona).
- Nunca invente. Cite só digital MEDIDA por você; a de terceiros é "declarada, não verificada". Cite sempre papel + digital + tamanho (vigente / texto assinado / bilhete) e o nome do documento, nunca só número de anexo.
- Seja claro sobre QUEM faz cada passo e ONDE o resultado fica. Nunca "eu publico": publicar é sempre um AGENTE NOVO, com a mensagem colada pelo operador.
- Frase de aprovação do operador só existe quando ele a diz, letra a letra + data (a data é a do dia da colagem). Você redige como "Sugestão da casa" com documento + digital completa + data; ele cola no chat. Ato antigo não basta: documento atualizado precisa de frase atual.
- Não rode scripts de produção, não varra o repositório inteiro, nunca force, conflito = parar e indicar.
- Ele está perdendo paciência com refinamento e com erros. Estamos perto do crivo do Livreto 1: vá ao crivo, não refine mais os livretos.

## 1) PAPÉIS

- Operador: carteiro e aprovador. Copia e cola, carrega arquivos nos agentes do crivo, aprova com frase.
- Agente do chat (você): conversa, lê, mede digitais, redige textos, mensagens e programas. NÃO publica no GitHub (a sessão encerra quando há merge).
- Agente de publicação (janela nova): recebe a mensagem colada e faz commit, PR e merge. Não guarda conversa. IMPORTANTE: ele NÃO enxerga a sua área de trabalho; só o que for colado. Uma mensagem de publicação precisa ser AUTOSSUFICIENTE (programa em ASCII puro com tudo embutido e conferência de digital ANTES de gravar). Já falhou uma vez por eu supor o contrário.
- 3 agentes Arena do crivo: recebem só arquivos carregados, não veem o repositório nem o parecer um do outro.
- Comentador (ChatGPT, gratuito): lê SÓ a folha do crivo, nunca os documentos. Auditor-Mestre = governança, rito, vigência. Auditor-Estrutura = schemas, contagens, coerência técnica (atribuição por CONTEÚDO, não pelo nome do documento). Ambos pagos: só entram onde há uso real demonstrável.
- GitHub (main) = memória durável. Quem chega começa por `BIBLIOTECAS/ONDE_PARAMOS.md` e `BIBLIOTECAS/CHANGELOG_GERAL.md`.

## 2) ESTADO DO main (publicado)

PRs nº 3 a 8 mergeados. PR nº 8: merge `c39ea774aa3ff34dad0fd3eca9420fc7c8659e26` (ajustou datas em CHANGELOG e ONDE_PARAMOS). PR nº 7: merge `71ab6c32c8e8ef6ca49544e82770c8c6e0f98dbd` (publicou a errata do Roteiro). Pasta do dia: `ENTREGAS/2026-10-01_ROTEIRO_E_ATO/` (bilhete, Ato, programa, DIGITAIS.txt). Digitais conferidas no main pelo agente de publicação (declaradas, não verificadas por mim; o repositório não responde a mim):

- `ROTEIRO DE TRABALHO DA PLATAFORMA.md` (raiz) = `aa01bfe87044f4724e6c4928c6d073e0eb24003090ce69099fd363bba40c5579` (38.971 B, CRLF, 1.174 linhas)
- `.bak` do anterior = `507eaefac6eadc2ccf9fac506b9ad80ace34296b33ef21c822dfffeb033cbe8e` (37.919 B)
- bilhete `BIBLIOTECAS/_documentos_serie/ROTEIRO_PLATAFORMA_VIGENTE.txt` = `cadfef35971316b5525421bea397133d22740b3fecc85bf411cb41b21c90f76b` (4.566 B)
- `ATO_OPERADOR_2026-10-01.md` = `16700dc0c0d792d8ce9863edfe069f24bac88ef7c6f143311a7c0eb58180b76e` (2.655 B)

Nota: o CHANGELOG local de quem trabalhou aqui NÃO é o do main; sempre trabalhe sobre o main.

## 3) ATOS DO OPERADOR EM 01/10/2026 (frases coladas por ele no chat, registradas no Ato acima)

- Ratificou como VIGENTES (arquivo vigente atual, errata de etiqueta de 29/09): COMO EXECUTAR v1.11 rev.2 (`1ea6d354`; texto aprovado `2efc0edd`) · Schema-Claim v1.3 rev.3 (`e9f9e5d8`; `28cbc9c7`) · Contrato de Saída do Claim Kit rev.2 (`03cdd19a`; `841532da`) · L-06 Minuta 3 rev.6 (`acd76b24`; `98e90bdc`). O Roteiro NÃO entrou. Essas 4 erratas NÃO passam por novo crivo (decidido por ele).
- L-NT: decidiu a opção (i) (bifurcação: claim clínico é insumo de evidência, não de conhecimento; afirmação vai à Biblioteca da entidade pelo rito normal, §5.5 da Arquitetura V2.3 digital `498e7df9`; evidência segue N1 -> N2 -> NT); a (ii) foi descartada. Libera a minuta 2 do L-NT, que quem redige é o Auditor-Mestre (citando as três bases que ele aceitou: caput do §5, §5.5 e o princípio da Filosofia).

## 4) ROTEIRO (o ponto mais delicado)

- Cadeia: `2c286ca17b58…` (35.438 B, versão 27.09, concordada pelos DOIS auditores em 26/09, ambas as concordâncias sobre esta digital) -> `5f8b89dc524a…` (errata de 26/09, 36.237 B) -> `507eaefac6ea…` (errata de 29/09, 37.919 B) -> `aa01bfe8…` (errata de 01/10, 38.971 B, publicada). As erratas foram "a pedido do operador" e NÃO têm concordância própria registrada.
- NÃO existe frase do operador aprovando o Roteiro como vigente (AUD-007, MODERADO, do Mestre). Ele circula como vigente desde 26/09 pelas duas concordâncias. A frase de ratificação PENDENTE deve citar a digital COMPLETA `aa01bfe87044f4724e6c4928c6d073e0eb24003090ce69099fd363bba40c5579` e declarar o que ratifica: o documento de trabalho e a errata de 01/10. Será a primeira frase do operador sobre o Roteiro.
- IMPORTANTE: o Auditor-Mestre mediu e classificou como NÃO SUBSTANTIVA a redação CURTA (`a0efc7d01765bd24361cbe0d931d92d5442253c3e3e415f9c65d577db777f93c`, 38.372 B). A publicada (`aa01bfe8…`) é a mais completa (notas (4) e (6) detalhadas) e ele AINDA NÃO a mediu. O bilhete diz isso. Recomendação técnica do agente anterior: a frase espera a medição dele; o operador decidiu NÃO mandar pedido separado agora. Se for redigir a frase, avise o operador dessa lacuna e pergunte antes. A diferença entre as duas redações é só descritiva (notas (4) e (6)); corpo a partir de "Objetivo:" idêntico.
- O bilhete do Roteiro já foi corrigido (cadeia por digital, papel das 3 datas, descrição medida da errata de 29/09, vigência sem frase). Título interno "- 27.09.2026" mantido (nomeia a edição); campo Atualização = 01-10-2026.
- O corpo do §18 (linha ~1059) ainda diz "apenas errata de etiqueta"; foi mantido de propósito (os documentos se descrevem como "etiqueta e procedência, 0 mudança de conteúdo"; o Mestre classificou que o §18 não muda).

## 5) PARECER DO AUDITOR-MESTRE (01/10): o que ainda está aberto

- 4 erratas = não substantivas; Estrutura subscreve. AUD-004: o Contrato mantém "esta minuta" no corpo (histórico do rito); adenda é decisão do operador, ainda não decidida. AUD-005: COMO "EM TESTE" só muda após o piloto. AUD-006: Schema-Claim sem cercas (observação). AUD-002/003: sem ação. AUD-001/008: já tratados no bilhete do Roteiro.
- O Mestre deve ainda: Livretos 1 a 4 (L1 isolado; 2–4 em lote), minuta 2 do L-NT, situação do `L05_…ESPECIFICACAO.md` (`78a0f2af`), e medir `aa01bfe8…`.
- NÃO decida pelo Mestre nem o apresse; ele tem prompt próprio e lê o que for citado por nome.

## 6) CRIVO DOCUMENTAL DOS LIVRETOS 1–4

Regra de 30/09; FLUXO em `ENTREGAS/2026-09-30_CRIVO_LIVRETOS/FLUXO_CRIVO_DOCUMENTAL_2026-09-30.md`.

- Fluxo: 3 agentes Arena (cada um sozinho) -> você monta a FOLHA (lê o documento onde há divergência; fecha operacionalmente; NÃO declara vigência nem decide por maioria) -> Comentador (só a folha) -> auditor do território -> fechamento -> frase do operador.
- Acordo com o Comentador (01/10): o auditor só entra com uso real demonstrável por fato ou dependência concreta, respondido ANTES do crivo e nunca pela folha; documento novo ou da fila exige "ficha curta de uso". Livretos 1–4: os dois auditores ficam. Livreto 1 primeiro e isolado; Livretos 2–4 em UMA sessão por auditor, cada um só nos seus pontos; o auditor lê PRIMEIRO o documento e depois a folha (o FLUXO ainda diz "guiado pela folha": só ajustar se o operador quiser, em publicação futura). Documentos antigos fora. Nível C fora.
- Matriz por ponto: L1 Estrutura = contagem 146+5, duplicatas, formato, JSON, contradição com Contrato/Schema/COMO; Mestre = vigência, rito, substituição, cadeia. L2 Estrutura V1, V2, V4, V5; Mestre V3. L3 Estrutura L1, L2, L3, L5, L6; Mestre L4, L7. L4 Estrutura B1, B2, B3, B5, B7, B8; Mestre B4 (P1, P2) e B6.
- Pacote do Livreto 1 (8 arquivos, o OPERADOR carrega nos 3 agentes Arena): Livreto 1 (`5cfdee31`) · `1º IDS_OFICIAIS.md` (`3c0eccac`, 146 IDs) · `_ids_oficiais.json` (`d0ff2647`) · `_ids_oficiais.PROVENIENCIA.json` (`573b7edb`) · `CANDIDATOS_IDS_OFICIAIS` (`a069de5f`) · COMO (`1ea6d354`) · Schema-Claim (`e9f9e5d8`) · Contrato (`03cdd19a`). Passo imediato: o operador abre os 3 agentes com esse pacote e traz os 3 pareceres; DEPOIS você monta a folha. Livreto 1 NÃO será editado.
- Kit do Mestre por Livreto (ele já tem Arquitetura V2.3, Roteiro, COMO, Schema, Contrato): L1 = Livreto 1 + IDS + CANDIDATOS. L2 = Livreto 2 (`36ed0fa5`) + Protocolo de Escopo B1 v1.3 (`943425cd`). L3 = Livreto 3 (`15001205`) + Lista Canônica B1/SM-02 v1.5 (`20efa89f`) + Bloco de Estado v1.8 (`7db41d40`). L4 = Livreto 4 (`d5a7a083`) + Bloco + Lista + `CORPUS_CONGELADO_PILOTO_B1SM02014_2026-09-26.md` (`20c7159b`) + `ENTREGA_TRIDE_PILOTO_014_2026-09-26.md` (`b1c6cde3`). Filosofia (`FASE 2- 02 FILOSOFIA DO PROJETO.md`) sobe só como referência. `DECISOES_ARQUITETURAIS_v2_5` NÃO sobe agora (sem uso demonstrável); virá com a minuta 2 do L-NT.
- Livretos 2–4: pergunta única "Concordam em declarar VIGENTE, para uso operacional no piloto oficial B1.SM02.014, o [documento] (digital)?" -> de acordo / com ressalva / em desacordo. Se o Livreto 1 mudar o catálogo de IDs, refazer a conferência nos 2–4.

## 7) PENDÊNCIAS E DECISÕES EM ABERTO (nada disso trava o Livreto 1)

- Frase do operador para o Roteiro (ver §4).
- Adenda do Contrato (AUD-004): decisão dele.
- Bilhetes dos 4 documentos ratificados em 01/10 NÃO foram alterados (mexer muda a digital): o registro está no Ato, no CHANGELOG e no ONDE_PARAMOS. Se o Mestre ou o operador quiser ponteiro no bilhete, é decisão a perguntar.
- Fila de regularização (documento, versão, digital, rito feito, rito faltante; sem registro = "sem registro suficiente"): começa depois do Livreto 1. Inclui `L05_…ESPECIFICACAO.md` (`78a0f2af…`, N2 v1.4 minuta, 7 cópias idênticas, sem ato de vigência). Pergunta SEM resposta do operador: quais documentos foram "aprovados sem crédito".
- Emenda 2 (bilhetes se declaram): ADIADA pelo operador, sem prazo. Não aplicar; perguntar antes.
- Nota de estado (`NOTA_DE_ESTADO_E_MAPA_2026-10-01.md`, com os §10 a §14): publicada junto com esta carta, nesta mesma pasta. Em conflito entre a nota e o main (ONDE_PARAMOS e CHANGELOG), vale o main.
- Próxima publicação (agente novo, uma rodada só, depois de respostas do Mestre): registrar a frase do Roteiro no bilhete, atualizar CHANGELOG e ONDE_PARAMOS.
- Regra de publicação (ONDE_PARAMOS §9): publicar e mergear no mesmo ato; toda publicação traz link da pasta do dia e caminho de download; se o GitHub não responder, avisar e não contornar.

## 8) ERROS QUE JÁ COMETI (não repita)

- Escrever a carta e só depois perguntar; entregar carta com pergunta aberta.
- Falar com o operador DENTRO da carta ao auditor (segunda pessoa).
- Dizer que adotei a redação do Mestre sem tê-la (reescrevi do zero e atribuí a ele): confira antes de atribuir algo a alguém.
- Mudar de posição técnica por pressão de ritmo sem avisar (disse B, depois A, depois B).
- Supor que o agente de publicação via minha área de trabalho.
- Citar anexos só por número; chamar de "texto assinado" um bilhete; avançar para trabalho novo quando ele queria esperar os auditores; criar livretos com 5 janelas sem alinhar; dar acesso ao repositório inteiro aos agentes Arena sem ele decidir.
- Contar "P-K"/"§" por método próprio: compare só igualdade entre pares, não o absoluto.

## 9) ARMADILHAS TÉCNICAS DO AMBIENTE

- O `.git` é recriado entre turnos; confie nos arquivos e nas digitais, não no `git status` local. `/tmp` e `/home/user/transporte_tmp` são apagados entre mensagens: cada passo deve ser autossuficiente (programa inline por heredoc).
- Base64/hex longos copiados pelo agente erram caracteres; colagem do operador perde acento/emoji (por isso programas de publicação em ASCII puro com `\uXXXX` e conferência de digital ANTES de gravar).
- Sessão que fez merge encerra: operações remotas falham depois.
- O repositório pode responder 404 a ferramentas externas; use o relatório do agente de publicação como "declarado, não verificado".
- Nomes exatos: `5º_LISTA_CANÔNICA___B1__SM-02_V1_5.md`, `6º BLOCO_DE_ESTADO__v1_8.md`, `2º PROTOCOLO DE ESCOPO — B1 (v1.3).md`. Na Lista os IDs aparecem como `  - id:` e no Bloco como `  - claim_id:`.
- Roteiro: CRLF; o Notepad grava CRLF.

## 10) PRIMEIRA AÇÃO SUGERIDA PARA VOCÊ

Leia esta carta inteira, depois pergunte ao operador, em UMA linha, qual é o próximo passo dele: (a) abrir os 3 agentes do Livreto 1 (então fique pronto para montar a folha quando ele trouxer os pareceres) ou (b) tratar a frase do Roteiro. Não escreva carta nenhuma antes de ele responder.
