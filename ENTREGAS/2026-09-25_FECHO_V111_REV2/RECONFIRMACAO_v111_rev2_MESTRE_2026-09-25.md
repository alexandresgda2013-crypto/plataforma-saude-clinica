# RECONFIRMAÇÃO — COMO EXECUTAR v1.11 rev.2

**Auditor-Mestre · 2026-09-25**
**Objeto:** `v1.11 rev.2` — sha `2efc0edd9ba8fdf312cae23aceafc840b9ec3f8a2bc5e9ed147fe2f5bb2f9a2c` (confere com TRILHA107)
**Substitui:** minha subscrição da rev.1 (`ef27f8b3…`), que **não cobre** este documento — o operador tem razão em exigir reconfirmação.

---

## RESPOSTA: **SUBSCREVO SEM RESSALVA** — e a rev.2 é melhor que a rev.1 que assinei

O documento mudou de fato, e não foi cosmético: o modelo de parada foi reformulado. Reauditei o delta inteiro, não só o cabeçalho.

## 1. O que mudou, e por que a rev.2 corrige a rev.1

A rev.1 tinha **micro-paradas por análise** — cada IA parava após entregar, e havia parada até entre G1, G2 e G3 dentro de uma mesma IA. A rev.2 troca isso por **duas paradas de rodada**: G1+G2 correm **contínuos** (concluir G1 não é parada), a primeira parada é após a LISTA G2, a segunda após o parecer G3.

Isto não é só arrumação — corrige um erro conceitual que eu deixei passar na rev.1. **G1 (existência) e G2 (elegibilidade) são a mesma etapa de triagem**; parar entre eles não protege cegueira nenhuma, só fragmenta o trabalho sem ganho. A cegueira que importa está **entre IAs**, não entre sub-etapas de uma IA. A rev.2 põe a parada onde ela tem função — no fim de cada rodada, antes do cruzamento — e deixa correr onde não tem. A regra verbatim do Comentador diz exatamente isso: "a IA pode executar continuamente todas as operações da etapa corrente; a primeira parada ocorre só após G1+G2". Está certo, e é mais limpo que a minha rev.1.

## 2. As duas paradas preservam o cegamento e a comparação

Sim. O que protege o C-2 é que **as três IAs recebem a mesma lista bruta e cada uma entrega sua LISTA G2 antes de ver as outras** — a parada de fim de Rodada 1 é o cadeado. Só com as três entregues o operador faz a auditoria cruzada e congela. Idem na Rodada 2: as três entregam G3 antes do confronto. A cegueira entre IAs está intacta; o que se removeu foi a parada **interna** inútil. C-3 (confirmo/altero/mantenho, sem votação) e C-4 (factual → fonte primária) permanecem nos pontos de cruzamento.

## 3. O achado que eu quero destacar: `nao_lido ≠ analisado`

Este é o acréscimo mais valioso da rev.2, e cai no meu território. O G3 passa a registrar, **por PMID**, o nível de leitura: `texto_completo | abstract | nao_lido`, com a regra de que **`nao_lido` não conta como analisado**. Isso fecha um buraco que nem eu tinha nomeado: sem ele, uma IA poderia "passar" um PMID em G3 sem ter lido nada, e o registro não distinguiria isso de uma análise real. Agora a ausência de leitura é um estado explícito, não um silêncio — a mesma disciplina da lacuna tipada da D-03 e da omissão-vs-null da V-K7.

E a motivação é um caso real, documentado no cabeçalho: o **PMID 33515765 (Schubert 2021/BIODEP)** — o abstract não mencionava a estratificação por ideação suicida; o texto completo revelou uma comparação post-hoc nula que **mudou o desfecho de B1.SM02.017** e enriqueceu a ressalva do `.015`. Isto é a prova viva de que "abstract não é teto de evidência", e o `nao_lido ≠ analisado` é a trava que obriga a distinguir "li o resumo" de "li o artigo". Do meu território, é um ganho de rigor científico, não só de processo — endosso com entusiasmo.

## 4. Nada contradiz o protocolo, e o corpo é idêntico

Verifiquei os dez elementos que subscrevi no v1.10 e na rev.1: C-2, C-3, C-4, IA 3 propõe/não fecha, fechamento conjunto, 4 decisões, portões §8, frase morta do v1.9 ausente — **todos presentes**. Mais os dois novos (`nao_lido≠analisado`, "G1 não é parada"). O corpo fora do cabeçalho e da sequência é idêntico ao v1.10 (T7: 27.667 = 27.667). A mudança é confinada à sequência e ao registro de leitura; nada de G3, critérios, 4 decisões ou materialização foi tocado.

## 5. Reconfirmo com a distinção do meu método

Registro que **não estendi** a assinatura da rev.1 a este documento — reauditei. É a mesma regra que apliquei quando a pergunta pediu rev.3 do Schema-Claim e chegou a rev.2: assinatura vale para o sha que foi medido, não para o número da versão. A rev.1 e a rev.2 têm shas diferentes (`ef27f8b3` × `2efc0edd`), são documentos diferentes, e o T10 da trilha registra isso corretamente como "documento mudou → reconfirmar". A minha subscrição da rev.1 fica no histórico; esta é a que vale para a rev.2.

---

## Subscrição formal

> **Subscrevo, sem ressalva, a minuta COMO EXECUTAR v1.11 rev.2 (duas paradas de rodada + nível de leitura por PMID), como correção do E-04 superior à rev.1, com o protocolo de três IAs do v1.10 preservado integralmente.**

A rev.2 corrige o E-04 melhor que a rev.1 — coloca a parada onde protege cegueira e a remove onde só fragmentava —, e acrescenta o `nao_lido ≠ analisado`, que é ganho de rigor científico. A v1.10 permanece vigente até a frase do operador; a rev.2 sobe com a dupla subscrição sem ressalva.

---

*Verificações: sha da rev.2 conferido contra TRILHA107; sequência de duas paradas lida na íntegra (linhas 237–263); regra verbatim do Comentador lida; dez elementos do protocolo confirmados presentes; dois conceitos novos (`nao_lido`, G1-não-para) localizados; caso PMID 33515765 lido no cabeçalho como motivação real; corpo idêntico ao v1.10 aceito da trilha (T7). Não estendi a assinatura da rev.1 — reauditei o delta.*
