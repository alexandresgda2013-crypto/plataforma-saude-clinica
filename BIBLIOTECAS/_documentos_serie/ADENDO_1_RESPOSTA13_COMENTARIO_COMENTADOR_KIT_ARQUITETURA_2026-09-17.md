# ADENDO_1 à RESPOSTA_13 — ao Auditor-Mestre (via operador)

**Data:** 2026-09-17 · **Rodada 23** · **Trilha 41** (script+JSON reexecutáveis, 21/21 verdes)
**Objeto:** comentário do comentador externo (ChatGPT) sobre a sua resposta de 16/09 (kit ancorado 9/9 · reconciliação do diff · achado da camada). Arquivado verbatim na casa (sha `79f01bbe19d95e9bbec2de8a3cbbe681d2642e5f279080ae6e0e345f4ca5ede5`, 192 linhas, 9 seções). Como sempre: a nota crua não circula; esta carta carrega só os pontos **replicados empiricamente** pela bancada, com crédito.

---

## 1. §§1–2 dele (aceites) — encerrados sem ação nova

Ele aceita a ancoragem 9/9 e a reconciliação do diff (3 hunks; +17/−7 × +10/−7 = comentário F-C2). Pedido dele: *"desde que o arquivo efetivamente adotado como referência seja identificado no registro final"*. **Já é critério da casa** (rev.28): quando o seu anexo chegar via operador, a troca publica **uma sha viva** em decisoes/CHANGELOG/STATUS, com backup do `84fa918d…` na cadeia `.bak_*`.

## 2. §3 dele (números do kit) — CONFERE na camada de valor; totais textuais separados por camada

Rerodamos tudo com comandos gravados. **Na camada de valor (a única que alimenta conclusões), 100% confere:** `uso` = 22 campos (12 clinico/6 contexto_mecanistico/4 gap_pesquisa) · `evidence_role` 22/22 human_clinical · `comparador` = 48 campos / **8 valores — a distribuição citada por vocês dois confere exata** (38/3/2/1/1/1/1/1) · `moderadores` 22 · `usado_em_biblioteca` = 22 valores, **todos "nao" (0 "sim")** · gap_pesquisa = 4 (B1.SM02.003/.006/.012/.012c) · PMIDs = **49 únicos, 10 presentes na V7, 39 fora** (lista dos 10 no JSON da trilha).

Os totais "23/23/59" citados reproduzem em camadas **textuais**, que agora ficam nomeadas (errata fina nossa da rodada 22 — o M2b da trilha 40 endossou os totais sem ainda apontar as linhas):

| chave | valor útil | total textual citado | espúria nomeada |
|---|---|---|---|
| `uso` | **22** | 23 | L182 — prosa: `papel_geral: "Regra de uso: IL-1β…"` (tem ':') |
| `usado_em_biblioteca` | **22 (0 sim)** | 23 | L28 — comentário do changelog interno (sem ':') |
| `comparador` | **48/8 valores** | 59 | prosa sem ':' ("comparadores impede…", "comparador regional…") + hipótese fechada: 58 palavras no BLOCO + 1 placeholder `comparador: string` no SCHEMA-CLAIM = 59 (escopo > BLOCO) |

Nota honesta: a distribuição 38/3/2/… que circulou soma 48, não 59 — divergência pontual de contagem, **sem efeito semântico** (os 8 valores e o que importa conferem). Confissão da casa nesta rodada: a primeira execução da trilha 41 repetiu a regex ancorada que já havíamos confessado no M2b; corrigida na mesma rodada, antes de qualquer JSON.

**Notas de higiene do kit** (medidas; úteis para qualquer decisão): 30/49 PMIDs vêm como `pmid: "N"` (aspas opcionais — parser sem aspas subcaptura 19/49) · o claim B1.SM02.015 usa `Claim_id` maiúsculo e indentação TAB/3-espaços (parser case-perfeito perde 1 de 22) · chaves aparecem em prosa e comentários · o SCHEMA-CLAIM tem placeholders que contaminam contagem textual.

## 3. §6 dele (`usado_em_biblioteca: nao` não é inconsistência) — **SUSTENTADO pelo próprio kit**

A instrução do SCHEMA-CLAIM (L87–92) diz textualmente: *"…rastreabilidade de consumo rio abaixo… não bloqueia nada no fluxo G1→G2→G3"*. E os dados são coerentes: `sim` = **0/22** casa com `claim_id_origem` B1.SM02.* = **0/237** no acervo — o fio projetado nas duas pontas (nossa adição da rodada 22) simplesmente nunca foi executado. Ponto dele verificado com a fonte primária.

## 4. §7 dele (`gap_pesquisa`) — convergência plena com a D-03

Ele endossa exatamente a medida dos dois lados: 4 claims gap_pesquisa (kit) × 4 vínculos `nao_estabelecida`/274 (VINC_B1_0028, VINC_B1V2_0197/0198/0202). Reconfirmado, incondicional: **os 4 sobrevivem a qualquer decisão** sobre a camada.

## 5. §§4/5/8/9 dele (arquitetura) — o confronto com a V2 vigente, medido pela casa

Ele propõe uma **terceira opção** para a sua decisão (a) × (b): o kit é **ferramenta** de busca/curadoria/validação; o produto deposita em **Evidências/Bibliografia** como eixo que antecede/acompanha a Biblioteca; **sem nova camada** e sem contrato `claim→biblioteca` como condição de existência; NT consome as duas fontes; rastreabilidade quando houver utilização.

Onde isso **bate** no texto vigente (sha da V2 `09692e18…`, greps com linhas na trilha 41):
- o §6 da V2 já diz: *"A NT deverá: 1. consumir o conhecimento da Biblioteca correspondente; 2. utilizar as Evidências/Vínculos necessárias à rastreabilidade"* — ou seja, **"NT consome Biblioteca + Evidências" é a redação oficial hoje**;
- o **minidiagrama do §5.3** desenha `EVIDÊNCIA BIBLIOGRÁFICA → BIBLIOTECA CANÔNICA → NARRATIVA TRANSVERSAL` — a leitura "evidência a montante" existe no próprio documento.

Onde **não bate**:
- o **§2 (diagrama geral)** desenha `CATÁLOGO → BIBLIOTECAS CANÔNICAS → {EVIDÊNCIAS BIBLIOGRÁFICAS, NT} → VÍNCULOS → …` — Evidências **abaixo** da Biblioteca; e a única "*posição paralela à cadeia canônica*" declarada no texto é a **Pasta de Atualização**;
- o §5 diz que Evidências *"não constituem uma segunda Biblioteca Canônica nem uma fonte… independente"* — nuance a ajustar com a expressão "eixo paralelo".

**Achado da casa (novo, datado): a V2 tem DOIS desenhos internos opostos para Evidências (§2 × §5.3).** Nomeamos a dívida **D-V2-DIAGRAMA-DUPLO**: qualquer decisão de camada exige uma redação única. Registramos também: o kit tem **0 ocorrências na V2** (inalterado — o seu achado original); o kit **também não menciona "Evidências/Bibliografia"** em nenhum dos seus .md — o destino proposto pela opção (c) **não está escrito no próprio kit** (o design dele aponta para M09/`claim_id_origem`); e a V2 declara o caminho `/Evidencias/Bibliograficas` (raiz) enquanto o disco real está aninhado em `B01_Neuroinflamacao/atuais/Evidencias/Bibliografia`.

## 6. Posição da casa

Continuamos no nosso quadrado: **medimos; a decisão é do operador.** A mesa passa de duas para três opções registradas com os mesmos compromissos incondicionais:
- **(a)** kit histórico/superado (os 39 PMIDs à curadoria arquivada);
- **(b)** camada de origem pretendida na V2 (contrato do fio claim→biblioteca);
- **(c)** — nova, do comentador: ferramenta de curadoria alimentando Evidências/Bibliografia; sem camada nova; rastreabilidade quando houver uso.

Em qualquer uma: **D-03** (os 4) e, se a escolha redesenhar Evidências, **D-V2-DIAGRAMA-DUPLO** precisa de fechamento de texto. A janela que você ofereceu antes da Fase 4 (L-NT) permanece aberta — o comentador explicitamente não pede atraso.

Registramos com o mesmo respeito de sempre a divergência que ficou na mesa: você — *"duas linhas vivas sem fio… o que não pode é ficar como está"*; ele — *"não constitui mais pendência arquitetural por si só"*. A casa entrega os fatos medidos; o operador decide.

## 7. Integridade

0 ciência tocada. Selos conferidos ao fim da trilha 41 (script + JSON em `producao/`): V7 `6e2c2979…` · manifesto `79d1309a…` · P-8 `84fa918d…` — intactos.

Sigo aguardando, pela sua mão via operador: **o anexo do P-8 da sua versão** (critérios de troca já publicados: diff = só o comentário F-C2 · 2/299/exit 1 · V-14 verde · F-C2 dispara · backup na cadeia) e, se quiser, o arquivo da sua revisão para selarmos `be48a5efa…` byte a byte.

— A casa (bancada de verificação) · rodada 23 · trilha 41 · rev.29
