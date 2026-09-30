# CARTA PARA A PRÓXIMA OFICINA — 30/09/2026

**De:** oficina Arena de 29/09/2026 (trabalhou o dia todo; **perdeu o acesso ao GitHub** no fim do dia)
**Para:** a oficina nova (a que tem acesso ao GitHub)
**Assunto:** o que aconteceu · o que ficou preso · como publicar a rodada final **sem depender de arquivo nenhum**

> Registro da passagem de turno, salvo no repositório em 30/09/2026 e publicado junto com a rodada final.
> O **Anexo F** (no fim) foi acrescentado em 30/09 com os blocos exatos do Contrato, em base64 — a cópia em
> texto do Anexo A.3 havia perdido 1 linha + espaços de fim de linha na colagem, e a oficina nova só
> conseguiu fechar a digital `03cdd19a` depois de receber os blocos. Se um dia for preciso reenviar ou
> reconstruir qualquer peça, está tudo aqui.

---

## 1. O que aconteceu, em ordem e com datas

1. **29/09 (manhã):** a oficina concluiu a primeira rodada (etiqueta do COMO EXECUTAR v1.11 rev.2; decisão da anamnese; decisão
   "plataforma × esboço"; crivo do 1º livreto; pacote do dia v1). O **PR nº 1** foi aberto e **integrado ao `main` às 19:20 UTC**.
2. **No mesmo instante, o Arena encerrou o acesso remoto daquela oficina** (regra da plataforma: integrado o pedido, a sessão
   perde a chave do repositório). A ordem do operador era **continuar trabalhando e publicar o dia inteiro de uma vez**.
3. **29/09 (tarde/noite): a rodada final ficou pronta, mas presa na oficina.** Enquanto isso:
   - as **4 pendências de vigência** foram resolvidas **dentro dos documentos** (§18 do Roteiro, bilhete do Roteiro,
     bilhete do v1.10, autodeclaração do L-06);
   - as **etiquetas internas** do Schema-Claim v1.3 e do Contrato de Saída rev.2 foram corrigidas (diziam "minuta / não vigente");
   - a **conferência de digitais** foi medida: **5/5 vigentes · 6/6 cópias assinadas · ZERO divergências**;
   - o **pacote do dia foi refeito** (20 arquivos + zip) e o cartão **ONDE_PARAMOS.md** foi criado.
4. **30/09:** tentamos transportar os arquivos por um **link temporário** montado na oficina antiga. **Falhou** — ver §2.
   Conclusão: **não existe arquivo de transporte**. O caminho é **refazer a rodada final a partir do que já está no GitHub**,
   seguindo esta carta (são edições pequenas e cirúrgicas, com conferência por digital).

## 2. O link que não funcionou (para não repetir)

- A oficina antiga montou um balcão de download e passou ao operador este endereço:
  `https://8000-isktqi68mdhy44xv1ohk1.e2b.app/MALOTE_29-09-2026.zip`
- **No navegador do operador deu "link não encontrado".** Causa medida pela própria oficina: **a bancada se recicla** — o
  identificador da instância mudou (`isktqi68mdhy44xv1ohk1` → `iix941rw8nxjtuscwnre1`), o servidor temporário morre junto e o
  endereço deixa de existir. **Servidor ou link temporário da oficina NÃO serve para transporte.** Não tentar de novo, não
  pedir ao operador que tente links antigos.
- **A solução é esta carta:** tudo o que falta é pequeno e **reproduzível a partir do GitHub + as instruções dos anexos**.

## 3. O que já está no GitHub (confira antes de agir)

- `main` = integração do **PR nº 1** (29/09, 19:20 UTC): a **versão da manhã** de 29/09.
- A gaveta `ENTREGAS/2026-09-29_ATUALIZACOES/` publicada tem **10 arquivos** (LEIA_PRIMEIRO, DIGITAIS.txt, `01_…` a `06_…`,
  um ANEXO com a versão assinada do manual pré-errata, e o zip da manhã de 39.608 bytes).
- **Falta publicar (a rodada final):** as etiquetas/autodeclarações nos 5 documentos · o Roteiro com o §18 corrigido e a errata
  de 29/09 · as duas cópias da série com CRLF restaurado · os 4 bilhetes atualizados · o pacote do dia refeito (21 itens) ·
  o cartão `ONDE_PARAMOS.md` · os itens 7 a 11 do CHANGELOG.

## 4. A tarefa — passo a passo (idempotente: conferir, pular o que já está pronto, aplicar o que falta)

**Passo 0 — conferir.** Para cada arquivo do Anexo D, meça a digital (`sha256sum`). Três casos:
 (a) **já é a digital final** → nada a fazer, siga adiante;
 (b) **bate com a digital do texto assinado** → aplique a edição do Anexo A (a digital final é a régua);
 (c) **qualquer outra coisa** → **PARE e reporte ao operador** (não "ajuste" por conta própria).

**Passo 1 — os 5 documentos.** Aplique as edições do **Anexo A**. São **etiqueta e procedência**: **0 (zero) mudança de conteúdo**
(nenhuma regra, critério, campo, portão, parada ou vocabulário). Ao final, **a digital tem de bater exatamente** com o Anexo D.
Se não bater: desfaça a edição e refaça com cuidado; **nunca** "arredonde" o resultado.

**Passo 2 — as duas cópias do Roteiro na série** (`BIBLIOTECAS/_documentos_serie/ROTEIRO_plataforma_vigente_2026-09-27/`):
o conteúdo está certo; falta **restaurar as quebras de linha CRLF** (a normalização veio da cópia de segurança do workspace).
Converter as quebras de linha (LF → CRLF) e conferir as digitais do Anexo D.

**Passo 3 — cópias de segurança (`.bak`)** — preservam byte a byte o texto assinado. Criar ao lado de cada documento, com o
nome exato do Anexo D, a partir da versão atual do GitHub **antes** de aplicar a edição (ou do ANEXO já publicado, no caso do manual).
Nunca editar o `.bak` depois de criado.

**Passo 4 — bilhetes + cartão.** Atualizar os 4 bilhetes em `BIBLIOTECAS/_documentos_serie/`
(`COMO_EXECUTAR_V111_VIGENTE.txt` · `SCHEMA_CLAIM_V1_3_VIGENTE.txt` · `CONTRATO_SAIDA_CLAIMKIT_VIGENTE.txt` · `ROTEIRO_PLATAFORMA_VIGENTE.txt` ·
`L06_VIGENTE.txt`): cada um deve declarar **as duas digitais** (texto assinado + arquivo vigente), o **caminho** do arquivo e,
quando for o caso, a razão histórica. O `COMO_EXECUTAR_V110_VIGENTE.txt` deve declarar-se **HISTÓRICO (NÃO VIGENTE)** — o nome do
arquivo fica (é citado por 5 registros antigos) e **a razão fica escrita dentro dele**. Criar o cartão `BIBLIOTECAS/ONDE_PARAMOS.md`
com o **texto do Anexo B** (é o primeiro arquivo a ler por quem chegar depois — inclusive você).

**Passo 5 — o pacote do dia** `ENTREGAS/2026-09-29_ATUALIZACOES/` — refeito com os **20 arquivos do Anexo E** + zip.
Regras: **nomes sem acento** (só para exibir bem em qualquer tela; os documentos canônicos mantêm o nome com acento) ·
`DIGITAIS.txt` com a digital **medida** de cada item (inclusive a do zip) · o zip é de conveniência do operador.

**Passo 6 — o diário.** Acrescentar ao `BIBLIOTECAS/CHANGELOG_GERAL.md` os **itens 7 a 11** (conteúdo no Anexo C), depois do
item 6 já publicado, mantendo o fecho "**0 ciência.**".

**Passo 7 — publicar e entregar.** Registrar no git · subir na prateleira `arena/01a0e9e1-plataforma-saude-clinica` · **PR → `main`**
Salvar **esta carta** no repositório em `BIBLIOTECAS/CARTA_PARA_A_PROXIMA_OFICINA_2026-09-30.md` e publicar junto (é o registro da passagem de turno).
(ordem expressa do operador, já dada) · **entregar: link da pasta do dia no GitHub + caminho de download.** Atualizar no cartão
`ONDE_PARAMOS.md` a linha da publicação (de "PENDENTE" para "publicado em 30/09/2026").
**Nunca** force (`push --force`, `reset` destrutivo). Se algo conflitar: **PARE e reporte.**

## 5. Regras do operador (valem sempre)

- **Publicar só com ordem expressa**; toda publicação vem com **link da pasta do dia + caminho de download**.
- **O documento se declara sozinho** — o bilhete é apoio, não substituto (o documento vai às janelas sem acompanhante).
- **A frase de aprovação é do operador**: só existe quando ele a diz, registrada **letra a letra + data** (R-CITA-1). Sugestão da
  casa vai rotulada "ainda não dita pelo operador". Na dúvida, **pergunta-se — não se supõe**.
- **Não decidir conflito sozinho** (indicar o conflito) · **não executar os scripts do repositório** · **não varrer o repositório**
  inteiro (listagens pontuais) · linguagem simples, com analogias.
- Se o GitHub não responder: **avisar o operador — não tentar contornar.**

---

# ANEXO A — edições exatas (etiqueta e procedência; 0 mudança de conteúdo)

> Nota de 30/09: a cópia em texto do item A.3 abaixo perdeu 1 linha + espaços de fim de linha na colagem
> (faltavam 93 bytes para fechar `03cdd19a`). O texto correto e completo está no **Anexo F** (blocos em base64).
> Os itens A.1, A.2, A.4 e A.5 fecharam a partir desta cópia em texto, sem reparo.

## A.1 COMO EXECUTAR v1.11 rev.2 — de `2efc0edd` para `1ea6d354`
```diff
@@ -1,3 +1,17 @@
-# COMO EXECUTAR — v1.11 (MINUTA rev.2 — não vigente)
+# COMO EXECUTAR — v1.11 rev.2 — VIGENTE
+# ---------------------------------------------------------------------------
+# ERRATA DE ETIQUETA — 2026-09-29 (decisão do operador · registrada via Arena)
+# A linha de título dizia "(MINUTA rev.2 — não vigente)": ficou da época em que
+# o documento ainda era minuta. A vigência do v1.11 rev.2 foi declarada em ato
+# próprio de 25/09/2026 (bilhete COMO_EXECUTAR_V111_VIGENTE.txt, com a frase do
+# operador) — o que não havia sido trocada era a etiqueta.
+# Esta correção é de ETIQUETA e PROCEDÊNCIA: 0 (zero) mudança de conteúdo —
# nenhuma regra, critério, portão, parada ou vocabulário foi tocado.
+# Texto aprovado em 25/09 = digital 2efc0edd, preservado byte a byte em
+#   "COMO_EXECUTAR_v1.11rev2_ASSINADA_2efc0edd_2026-09-29.bak"
+#   (nome sem acentos, só para exibir corretamente nas telas do projeto).
+# As referências a v1.10 no corpo são marcas de ORIGEM das regras (histórico)
+# e estão corretas — preservadas de propósito.
+# ---------------------------------------------------------------------------
 # Correção vs. v1.10 (E-04 do ensaio pré-piloto .014 — 25/09)
 # consolidada pelo Comentador (25/09):

```

## A.2 Schema-Claim v1.3 rev.3 — de `28cbc9c7` para `e9f9e5d8`
```diff
@@ -2,5 +2,18 @@
 ---

-# SCHEMA-CLAIM — v1.3 (MINUTA rev.3 do ciclo do kit — não vigente)
+# SCHEMA-CLAIM — v1.3 (rev.3 — VIGENTE)
+# ---------------------------------------------------------------------------
# ERRATA DE ETIQUETA — 2026-09-29 (decisão do operador · registrada via Arena)
# O título dizia "(MINUTA rev.3 do ciclo do kit — não vigente)", e o comentário
# do bloco de schema repetia "(MINUTA rev.3 — não vigente)": ficaram da época
# em que o documento ainda era minuta. A vigência do v1.3 rev.3 foi declarada
# em ato próprio de 25/09/2026 (bilhete SCHEMA_CLAIM_V1_3_VIGENTE.txt, com a
# frase do operador) — o que não havia sido trocada era a etiqueta.
# Correção de ETIQUETA e PROCEDÊNCIA: 0 (zero) mudança de conteúdo — as
# alterações são apenas em linhas de comentário (#); nenhum campo, enum,
# obrigatoriedade ou regra foi tocado.
# Texto aprovado em 25/09 = digital 28cbc9c7, preservado byte a byte em
#   "SCHEMA_CLAIM_v1.3_rev3_ASSINADO_28cbc9c7_2026-09-29.bak".
# ---------------------------------------------------------------------------

 rev.2 (2026-09-25): V-K3 alinhado à opção preferida do Comentador
@@ -11,5 +24,5 @@ rev.3 (2026-09-25): V-K6 adicionado (ressalva do Estrutura) + linha de
 yaml
 # ============================================
-# SCHEMA_CLAIM — v1.3 (MINUTA rev.3 — não vigente)
+# SCHEMA_CLAIM — v1.3 (rev.3 — VIGENTE · ver nota de errata no topo)
 # Ciclo do kit · 2026-09-25 · Arena Casa
 # Mudança vs. v1.2 (somente isto; mais nada):

```

## A.3 Contrato de Saída do Claim Kit rev.2 — de `841532da` para `03cdd19a`

> **Ver Anexo F** — a cópia em texto abaixo está incompleta (perdeu 1 linha + espaços de fim de linha
> na colagem, 93 bytes). Mantida aqui como registro fiel do que chegou; a reconstrução usa o Anexo F.
> (Assinatura da cópia recebida: bloco de errata com 15 linhas no lugar de 16; linha
> "# subscrição dos dois territoriais…" no singular, quando o original é "subscrições…".)

```diff
@@ -1,7 +1,24 @@
-# MINUTA FINAL — CONTRATO DE SAÍDA DO CLAIM KIT
+# CONTRATO DE SAÍDA DO CLAIM KIT
+# ---------------------------------------------------------------------------
# ERRATA DE ETIQUETA — 2026-09-29 (decisão do operador · registrada via Arena)
# O título dizia "MINUTA FINAL" e o campo Status dizia "não vigente até dupla
# subscrição dos dois territoriais. A vigência foi declarada em ato próprio de
# 24/09/2026 (bilhete CONTRATO_SAIDA_CLAIMKIT_VIGENTE.txt, com a
# operador) — o que não havia sido trocado era o título e o status.
# Correção de ETIQUETA e PROCEDÊNCIA: 0 (zero) mudança de conteúdo — nenhum
# eixo, campo, trava ou regra foi tocado. O parágrafo original de status foi
# preservado e marcado como "(na redação)". As passagens do corpo que falam em
# "esta minuta" pertencem ao relato do rito de subscrição (histórico) e foram
# preservadas de propósito.
# Texto aprovado em 24/09 = digital 841532da, preservado byte a byte em
#   "CONTRATO_SAIDA_CLAIMKIT_rev2_ASSINADO_841532da_2026-09-29.bak".
# ---------------------------------------------------------------------------
 ## Claim Clínico Aprovado → materialização N1/N2 (D1 + R-1 + R-2 integrados)

 **Data:** 2026-09-24 · **Origem:** Arena Casa (redação da Rota A do Comentador)
-**Status:** MINUTA **rev.2** (2026-09-24) — … (parágrafo original; ver arquivo)
+**Status (atualizado em 2026-09-29):** **VIGENTE — rev.2** · … (ver Anexo F, Bloco B)
+*Nota histórica — … (ver Anexo F, Bloco B)*
+**Status (na redação):** MINUTA **rev.2** (2026-09-24) — … (parágrafo original preservado)
 **Base:** Solução D1 (r79) · Pareceres R4 (r80) · Condução Rota A (§18)
 **Não altera:** N1 v1.3, N2 v1.4, Bibliografia, nem o Schema-Claim v1.2 **no texto** — as extensões de campo do kit são listadas como **pendências do ciclo do Claim Kit** (§7), com trava de materialização.
@@ -213,3 +230,3 @@
-*Minuta da casa **rev.2** · Rodada 82 · 2026-09-24 · não vigente até dupla subscrição limpa sobre a rev.2.*
+*Contrato da casa **rev.2** · Rodada 82 · 2026-09-24 · **VIGENTE** … (ver Anexo F, Bloco C)*

```

## A.4 L-06 (Minuta 3 consolidada rev.6) — de `98e90bdc` para `acd76b24`
```diff
@@ -1,4 +1,6 @@
 # L-06 — PROTOCOLO DE RESOLUÇÃO DE RELAÇÕES CONCORRENTES
-## Minuta 3 · consolidada · rev.6
+## Minuta 3 · consolidada · rev.6 — **VIGENTE (em espera de produção)**
+
+**Status (nota de etiqueta — 2026-09-29, decisão do operador):** documento **VIGENTE** desde 22/09/2026, por aprovação verbatim do operador (frase registrada no bilhete `L06_VIGENTE.txt`); "em espera de produção" porque a L-06 não roda sozinha — depende da migração dos vínculos ao N2 v1.4 e das dívidas declaradas que o próprio texto carrega. Esta linha é **acréscimo de etiqueta**: 0 (zero) mudança no texto normativo (§2–§13 intactos). A versão aprovada em 22/09 (digital `98e90bdc`) está preservada byte a byte em `L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev6_ASSINADO_98e90bdc_2026-09-29.bak`, ao lado deste arquivo.

 *rev.1 (2026-09-21): ajuste de proveniência após o operador confirmar o texto enviado à Arena.*

```

## A.5 Roteiro da Plataforma (raiz) — mudanças de conteúdo (§18 + errata de 29/09)
*(o arquivo é **CRLF**: aplicar preservando as quebras de linha; o diff abaixo já ignora a diferença de quebra de linha.
Se o arquivo que está no GitHub estiver com quebras **LF** (normalização da cópia de segurança do workspace), **converta
primeiro para CRLF** e só depois aplique as mudanças — a digital final do Anexo D pressupõe CRLF.)*
```diff
@@ -9,6 +9,10 @@
 **(2)** Nota de sequência no Checklist: o quadro é **inventário de status**, não ordem de execução — ordem operacional = §19.
 **(3)** Sha original concordado pelos auditores: `2c286ca1…` — esta revisão é errata factual/editorial; estrutura inalterada.

+**Errata 29-09-2026 (pedido do operador):**
+**(4)** §18: cada uma das três bases passa a registrar **duas digitais** — a do **texto assinado** (preservado byte a byte em `.bak`) e a do **arquivo vigente** (após as erratas de etiqueta de 29/09, que trocaram apenas a palavra "minuta/não vigente" no interior dos documentos). Nenhuma regra, marco, sequência ou seção foi alterada.
+**(5)** O **texto aprovado em 26/09** (errata) permanece preservado na série `ROTEIRO_plataforma_vigente_2026-09-27/`, com digital `5f8b89dc…`; a digital deste arquivo após a presente errata consta do bilhete `ROTEIRO_PLATAFORMA_VIGENTE.txt`.
+
 **Objetivo:** organizar a sequência de desenvolvimento, validação, integração e teste da plataforma antes da replicação para os demais IDs oficiais.

 ---
@@ -1034,18 +1038,26 @@ As decisões específicas continuam pertencendo ao documento/contrato correspond

 ```text
 Contrato de Saída do Claim Kit rev.2
-SHA:
+SHA do texto assinado (preservado byte a byte em .bak):
 841532dad13cd3fea1356c9e23e37067e78876685db52d3c1f2cd8b2a96e535c
+SHA do arquivo vigente (após errata de etiqueta de 29/09):
+03cdd19af99801f34858427f1cc42de85189b29f6e9561fad5872173233e2d27
         ↓
 Schema-Claim v1.3 rev.3
-SHA:
+SHA do texto assinado (preservado byte a byte em .bak):
 28cbc9c76006f485f340da124aa1795833afa56d38e6572a9279d94a88f6b94c
+SHA do arquivo vigente (após errata de etiqueta de 29/09):
+e9f9e5d8d8949b3e38cf2d187520d7611d4665d7750579351e43774a5c70229e
         ↓
 COMO EXECUTAR v1.11 rev.2
-SHA prefix:
-2efc0edd
+SHA do texto assinado (preservado byte a byte em .bak):
+2efc0edd9ba8fdf312cae23aceafc840b9ec3f8a2bc5e9ed147fe2f5bb2f9a2c
+SHA do arquivo vigente (após errata de etiqueta de 29/09):
+1ea6d3547ff5acbc5160c0a5ff4e2fd704611846482caeeaaecdccc6ec7a7033
 ```

+Cada base traz agora **duas digitais**: a do **texto assinado** (preservado byte a byte ao lado do arquivo, em `.bak`) e a do **arquivo vigente**, que recebeu em 29/09/2026 apenas **errata de etiqueta** — os três documentos declaravam-se "minuta/não vigente" no próprio interior, contradizendo o rito e este §19. Na ocasião ficou registrado, como princípio do projeto: **o documento deve se declarar sozinho**; o bilhete é apoio, não substituto.
+
 O **COMO EXECUTAR v1.10** é histórico e não é a versão vigente.

 O Roteiro apenas organiza a execução do projeto em torno dessas bases.

```

# ANEXO B — `BIBLIOTECAS/ONDE_PARAMOS.md` (criar com este texto)

*Nota para a oficina nova: ajuste a linha "Publicação" conforme o resultado real (publicado em 30/09/2026).*

```markdown
# ONDE PARAMOS
O PRIMEIRO ARQUIVO A LER — por qualquer agente, auditor ou pessoa que chegue depois.

Atualizado em: **29/09/2026** (fim do dia)

> Como este cartão funciona: ele é atualizado **todo dia** — o último acontecimento entra sempre **com data**.
> Quem publica no GitHub, publica este cartão junto. O histórico completo e antigo fica em
> `BIBLIOTECAS/CHANGELOG_GERAL.md`. Se a sessão do Arena parar de funcionar, **outro agente retoma o trabalho
> lendo este arquivo** — não é preciso adivinhar nada.

## 1) Último acontecimento — 29/09/2026
- As **4 pendências de vigência** foram resolvidas no mesmo dia (Roteiro §18 com as duas digitais por base ·
  bilhete do Roteiro reescrito · bilhete do v1.10 virou HISTÓRICO · L-06 passou a declarar o próprio estado).
- **Conferência de digitais medida:** 5/5 arquivos vigentes batem com o bilhete · 6/6 cópias assinadas
  reproduzem a digital original · **ZERO divergências**.
- **PRATELEIRA DO DIA PRONTA, MAS AINDA NÃO PUBLICADA:** a sessão do Arena perdeu o acesso ao GitHub quando a
  junção anterior foi integrada. A publicação do dia acontece na **PRÓXIMA sessão** (gaveta do dia abaixo).

## 2) A seguir (combinado com o operador)
- **4 livretos pelo crivo das 3 IAs**, um por um: o **1º** (IDS oficial) já está entregue, aguardando resultado;
  depois vêm o **2º** (Protocolo de Escopo B1 v1.3), o **3º** (Lista SM-02 v1.5) e o **4º** (Bloco de Estado v1.8).
- **Anamnese:** registrada — entra **depois** do piloto oficial; os arquivos estão com o operador.

## 3) Regras combinadas (valem para todos)
- **O documento se declara sozinho** — o bilhete é apoio, não substituto.
- **Rito de aprovação:** a frase é do **operador** e só existe quando ele a diz, registrada **letra a letra + data**.
  Sugestão da casa vai rotulada "sugestão da casa — ainda não dita pelo operador"; na dúvida, **pergunta-se**,
  não se supõe (R-CITA-1).
- **Publicar no GitHub só com ordem expressa do operador**; toda publicação vem com **link da pasta do dia +
  caminho de download**.
- **Sistema da prateleira:** trabalha-se o dia todo; ao fim do dia — hora decidida pelo operador — **sobe tudo
  de uma vez**.
- Não decidir conflito sozinho (indicar o conflito) · não rodar os scripts · não varrer o repositório inteiro.

## 4) Onde está tudo
- **Gaveta do dia:** `ENTREGAS/2026-09-29_ATUALIZACOES/` (LEIA_PRIMEIRO + documentos + bilhetes + zip + DIGITAIS.txt)
- **Diário datado:** `BIBLIOTECAS/CHANGELOG_GERAL.md`
- **Documentos vigentes + bilhetes:** `BIBLIOTECAS/_documentos_serie/`
- **Roteiro da plataforma:** `ROTEIRO DE TRABALHO DA PLATAFORMA.md` (raiz do projeto)

## 5) Para o agente que chega agora (retomada em 1 minuto)
1. **Confira o estado:** branch `arena/01a0e9e1-plataforma-saude-clinica` (a prateleira) — `git log --oneline -5` e `git status`.
   Se houver mudanças locais não registradas, registre-as primeiro (a cópia de segurança da bancada pode descartar o registro do commit — os arquivos ficam).
2. **O lote a publicar** é a **gaveta datada mais recente** em `ENTREGAS/` — em 29/09: `ENTREGAS/2026-09-29_ATUALIZACOES/` (20 arquivos + zip + DIGITAIS.txt).
3. **Publique:** prateleira `arena/…` → depois `main` pelo caminho normal (PR → merge). Nunca force.
4. **Entregue ao operador:** **link da pasta do dia no GitHub + caminho de download** (é obrigatório a cada publicação — regra do operador).
5. **Combinações do operador:** linguagem simples e analógica · não decidir conflito sozinho (indicar o conflito) · **não rodar os scripts** · não varrer o repositório inteiro · se o GitHub não responder, avisar — não tentar contornar.
```

# ANEXO C — CHANGELOG: itens 7 a 11 (acrescentar depois do item 6)

- **7. Errata de etiqueta no Schema-Claim v1.3 e no Contrato de Saída rev.2 (29/09).** Os dois documentos vigentes declaravam
  internamente "MINUTA / não vigente", contradizendo o rito e o §18/§19 do Roteiro. Corrigido **dentro dos próprios documentos**
  (princípio: o documento se declara sozinho). Schema `28cbc9c7` → `e9f9e5d8…` (10.304 b · 204 l). Contrato `841532da` →
  `03cdd19a…` (12.950 b · 232 l — inclui o rodapé). **0 mudança de conteúdo.**
- **8. Pendências declaradas no item 7 — TODAS resolvidas no mesmo dia (29/09):** (a) §18 do Roteiro com digitais velhas;
  (b) bilhete do Roteiro desatualizado (sha pré-errata + cópia inexistente em `uploads/`); (c) bilhete do v1.10 usando o nome
  "VIGENTE" para versão histórica; (d) L-06 sem declarar o próprio estado no interior.
- **9. Resolução das pendências — princípio firmado pelo operador: O DOCUMENTO SE DECLARA SOZINHO** (o bilhete é apoio, não
  substituto). (a) §18 do Roteiro: cada base passa a registrar **duas digitais** (texto assinado em `.bak` + arquivo vigente);
  Roteiro → `507eaefa…` (37.919 b · 1.171 l · CRLF); as duas cópias da série tiveram as **quebras de linha restauradas** para
  CRLF (`5f8b89dc…` 36.237 b · `2c286ca1…` 35.438 b) — cada uma reproduz a digital declarada. (b) Bilhete do Roteiro reescrito
  (raiz do projeto como principal; linha falsa de `uploads/` removida). (c) Bilhete do v1.10 → **HISTÓRICO (NÃO VIGENTE)**; nome
  mantido como legado, razão declarada dentro. (d) L-06 declara o próprio estado no título e em nota datada → `acd76b24…`
  (27.523 b · 315 l); texto aprovado `98e90bdc…` preservado em `.bak`.
  **CONFERÊNCIA FINAL DE DIGITAIS (medida, não declarada): 5/5 vigentes · 6/6 cópias assinadas · ZERO divergências.**
- **10. Rito de aprovação — mantido; esclarecido a pedido do operador (29/09).** A frase de aprovação continua sendo o ato de
  fechamento: só existe quando o operador a diz, **letra a letra + data** (R-CITA-1), e anda sobre a unanimidade sem ressalva.
  A autodeclaração **não substitui o rito**: o rito é o **ato**; a autodeclaração é o **estado** (o documento carrega o próprio
  rótulo e viaja sem acompanhante). Nenhuma etiqueta criou aprovação. **Sem cerimônia nova — o filtro fica.**
- **11. Sistema da "prateleira" (29/09).** Trabalha-se o dia; ao fim do dia — **hora decidida pelo operador** — **sobe tudo de
  uma vez** por ordem expressa; gaveta datada por dia (`ENTREGAS/<data>/`); o último acontecimento é atualizado **com data** no
  CHANGELOG e no cartão `ONDE_PARAMOS.md`. **Publicação de 29/09: pendente nesta mesma rodada** (a oficina de 29/09 perdeu o
  acesso ao GitHub ao ser integrada a junção anterior; o transporte por link temporário falhou). **Conclusão registrada:** a
  oficina nova publica a rodada final a partir do GitHub + desta carta, sem arquivo de transporte.
- **0 ciência.** Nenhum conteúdo científico foi analisado, produzido ou alterado.

# ANEXO D — digitais (a régua: medir e conferir)

| # | arquivo | digital final (destino) | tamanho |
|---|---|---|---|
| 1 | `BIBLIOTECAS/_documentos_serie/COMO_EXECUTAR_v1.11rev2_vigente_2026-09-25/4º COMO EXECUTAR — v1.11 rev.2.md` | `1ea6d3547ff5acbc5160c0a5ff4e2fd704611846482caeeaaecdccc6ec7a7033` | 36254 b · 651 l |
| 2 | `BIBLIOTECAS/_documentos_serie/SCHEMA_CLAIM_v1.3_rev3_vigente_2026-09-25/3º SCHEMA-CLAIM — v1.3.md` | `e9f9e5d8d8949b3e38cf2d187520d7611d4665d7750579351e43774a5c70229e` | 10304 b · 204 l |
| 3 | `BIBLIOTECAS/_documentos_serie/CONTRATO_SAIDA_CLAIMKIT_rev2_vigente_2026-09-24/CONTRATO_SAIDA_CLAIMKIT_rev2_2026-09-24.md` | `03cdd19af99801f34858427f1cc42de85189b29f6e9561fad5872173233e2d27` | 12950 b · 232 l |
| 4 | `ROTEIRO DE TRABALHO DA PLATAFORMA.md` | `507eaefac6eadc2ccf9fac506b9ad80ace34296b33ef21c822dfffeb033cbe8e` | 37919 b · 1171 l · CRLF |
| 5 | `BIBLIOTECAS/_documentos_serie/MESTRE_L06_minuta3_consolidada_rev6_recebida_2026-09-22/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev6_2026-09-22.md` | `acd76b244b430027506a17f18c4ec4b2196359719f2c09d06749d6682f094740` | 27523 b · 315 l |
| 6 | série `ROTEIRO … (errata 26-09).md` | `5f8b89dc524adecb3a4046740ff469970996827aae8861e3fdbbdd14d717435d` | 36237 b · CRLF |
| 7 | série `ROTEIRO … - 27.09.2026.md` | `2c286ca17b582a5fcad425d55b6a8f4ca7fd77cb1e95e23f6280fd58aa8357ce` | 35438 b · CRLF |

**Cópias de segurança a criar (byte a byte, antes da edição):**

| `.bak` (nome exato) | digital do texto assinado | tamanho |
|---|---|---|
| `COMO_EXECUTAR_v1.11rev2_ASSINADA_2efc0edd_2026-09-29.bak` | `2efc0edd9ba8fdf312cae23aceafc840b9ec3f8a2bc5e9ed147fe2f5bb2f9a2c` | 35223 b |
| `SCHEMA_CLAIM_v1.3_rev3_ASSINADO_28cbc9c7_2026-09-29.bak` | `28cbc9c76006f485f340da124aa1795833afa56d38e6572a9279d94a88f6b94c` | 9350 b |
| `CONTRATO_SAIDA_CLAIMKIT_rev2_ASSINADO_841532da_2026-09-29.bak` | `841532dad13cd3fea1356c9e23e37067e78876685db52d3c1f2cd8b2a96e535c` | 11205 b |
| `L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev6_ASSINADO_98e90bdc_2026-09-29.bak` | `98e90bdc755162b28fd16817d65692cebe81f939c466ef1d29c7a0a1124f2b41` | 26830 b |

*(para o manual, o texto assinado `2efc0edd` também está preservado no ANEXO já publicado da manhã: `ANEXO_versao_assinada_pre_errata_2efc0edd.md`)*

# ANEXO E — o pacote do dia (`ENTREGAS/2026-09-29_ATUALIZACOES/`, 20 arquivos + zip)

| item | conteúdo | fonte |
|---|---|---|
| `01_` | COMO EXECUTAR v1.11 rev.2 (vigente) | Anexo D, #1 |
| `02_` | bilhete `COMO_EXECUTAR_V111_VIGENTE.txt` | Passo 4 |
| `03_` | DECISAO_OPERADOR_ANAMNESE_NAO_BLOQUEIA_PILOTO_2026-09-29.md | já publicado |
| `04_` | DECISAO_OPERADOR_PLATAFORMA_X_ESBOCO_FERRAMENTAS_DESCARTAVEIS_2026-09-29.md | já publicado |
| `05_` | crivo do 1º livreto (IDS oficiais) | já publicado |
| `06_` | trecho do CHANGELOG de 29/09 (itens 1 a 11) | Passo 6 |
| `07_` | Schema-Claim v1.3 rev.3 (vigente) | Anexo D, #2 |
| `08_` | Contrato de Saída rev.2 (vigente) | Anexo D, #3 |
| `09_` | Roteiro da Plataforma (vigente) | Anexo D, #4 |
| `10_` | L-06 (vigente) | Anexo D, #5 |
| `11_`–`14_` | os 4 bilhetes (schema · contrato · roteiro · L-06) | Passo 4 |
| `ANEXO_1`–`ANEXO_4` | as provas assinadas: `2efc0edd` · `28cbc9c7` · `841532da` · `98e90bdc` | `.bak` do Passo 3 |
| `LEIA_PRIMEIRO_2026-09-29.md` | o que é a pasta, o que mudou, como conferir | redigir |
| `DIGITAIS.txt` | digitais **medidas** de todos os itens + do zip | medir |
| `ATUALIZACOES_2026-09-29.zip` | o pacote inteiro, para o operador baixar de uma vez | zipar |

---

# ANEXO F — Opção C: blocos exatos do Contrato (base64) — 30/09/2026

*(Recebido do operador em 30/09/2026, após a oficina nova medir que a cópia em texto do A.3 não fechava.
Registro referenciado pelo operador: registro local `3420e38`.)*

OPÇÃO C — nem A, nem B. A linha não se perdeu. A digital correta continua 03cdd19a — não formular linha nova; nada mais muda nos registros.

Causa dos 93 bytes: a cópia em texto perdeu 1 linha (83 b) + 5 pares de espaços no fim de linha (10 b) = 93. (Os espaços finais são marcação de quebra de linha do markdown; foram comidos na colagem.) Por isso os blocos vão em base64 — a decodificação devolve os bytes exatos.

Receita (provada por reconstrução): partindo do arquivo original 841532da (o `.bak` conferido), fazer só estas três trocas e nada mais:

- linha 1 (# MINUTA FINAL — …) → BLOCO A (16 linhas)
- linha 5 (o parágrafo **Status:** MINUTA **rev.2** …) → BLOCO B (3 linhas)
- última linha (215) (*Minuta da casa **rev.2** …) → BLOCO C (1 linha)

Conferência obrigatória: 12.950 bytes · 232 linhas · sha256 03cdd19a…. Se não fechar: pare e reporte.

BLOCO A — 16 linhas · 1.160 b · sha256 3965008adb8f847a11295c215ae7de930efcddfe7a7f25764c341ab13bd90610

```text
IyBDT05UUkFUTyBERSBTQcONREEgRE8gQ0xBSU0gS0lUCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgRVJSQVRBIERFIEVUSVFVRVRBIOKAlCAyMDI2LTA5LTI5IChkZWNpc8OjbyBkbyBvcGVyYWRvciDCtyByZWdpc3RyYWRhIHZpYSBBcmVuYSkKIyBPIHTDrXR1bG8gZGl6aWEgIk1JTlVUQSBGSU5BTCIgZSBvIGNhbXBvIFN0YXR1cyBkaXppYSAibsOjbyB2aWdlbnRlIGF0w6kgZHVwbGEKIyBzdWJzY3Jpw6fDo28gc2VtIHJlc3NhbHZhIjogZXJhIG8gZXN0YWRvIG5hIGRhdGEgZGEgcmVkYcOnw6NvICgyNC8wOSksIGFudGVzIGRhcwojIHN1YnNjcmnDp8O1ZXMgZG9zIGRvaXMgdGVycml0b3JpYWlzLiBBIHZpZ8OqbmNpYSBmb2kgZGVjbGFyYWRhIGVtIGF0byBwcsOzcHJpbyBkZQojIDI0LzA5LzIwMjYgKGJpbGhldGUgQ09OVFJBVE9fU0FJREFfQ0xBSU1LSVRfVklHRU5URS50eHQsIGNvbSBhIGZyYXNlIGRvCiMgb3BlcmFkb3IpIOKAlCBvIHF1ZSBuw6NvIGhhdmlhIHNpZG8gdHJvY2FkbyBlcmEgbyB0w610dWxvIGUgbyBzdGF0dXMuCiMgQ29ycmXDp8OjbyBkZSBFVElRVUVUQSBlIFBST0NFRMOKTkNJQTogMCAoemVybykgbXVkYW7Dp2EgZGUgY29udGXDumRvIOKAlCBuZW5odW0KIyBlaXhvLCBjYW1wbywgdHJhdmEgb3UgcmVncmEgZm9pIHRvY2Fkby4gTyBwYXLDoWdyYWZvIG9yaWdpbmFsIGRlIHN0YXR1cyBmb2kKIyBwcmVzZXJ2YWRvIGUgbWFyY2FkbyBjb21vICIobmEgcmVkYcOnw6NvKSIuIEFzIHBhc3NhZ2VucyBkbyBjb3JwbyBxdWUgZmFsYW0gZW0KIyAiZXN0YSBtaW51dGEiIHBlcnRlbmNlbSBhbyByZWxhdG8gZG8gcml0byBkZSBzdWJzY3Jpw6fDo28gKGhpc3TDs3JpY28pIGUgZm9yYW0KIyBwcmVzZXJ2YWRhcyBkZSBwcm9ww7NzaXRvLgojIFRleHRvIGFwcm92YWRvIGVtIDI0LzA5ID0gZGlnaXRhbCA4NDE1MzJkYSwgcHJlc2VydmFkbyBieXRlIGEgYnl0ZSBlbQojICAgIkNPTlRSQVRPX1NBSURBX0NMQUlNS0lUX3JldjJfQVNTSU5BRE9fODQxNTMyZGFfMjAyNi0wOS0yOS5iYWsiLgojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQo=
```

BLOCO B — 3 linhas · 974 b · sha256 eaba804a90d15c740254c841ae4c31cad6477e1f933ed9373d38edbd90e18fbf

```text
KipTdGF0dXMgKGF0dWFsaXphZG8gZW0gMjAyNi0wOS0yOSk6KiogKipWSUdFTlRFIOKAlCByZXYuMioqIMK3IGFwcm92YWRvIHBlbG8gb3BlcmFkb3IgZW0gMjQvMDkvMjAyNiAoZnJhc2UgZGUgdmlnw6puY2lhIG5vIGJpbGhldGUgYENPTlRSQVRPX1NBSURBX0NMQUlNS0lUX1ZJR0VOVEUudHh0YCkgwrcgZGlnaXRhbCBkbyB0ZXh0byBhcHJvdmFkbzogYDg0MTUzMmRh4oCmYCAocHJlc2VydmFkbyBieXRlIGEgYnl0ZTsgdmVyIG5vdGEgZGUgZXJyYXRhIG5vIHRvcG8pLiAgCipOb3RhIGhpc3TDs3JpY2Eg4oCUIG8gcGFyw6FncmFmbyBhYmFpeG8gZGVzY3JldmUgbyBlc3RhZG8gbmEgZGF0YSBkYSByZWRhw6fDo28gKDI0LzA5LzIwMjYpLCBhbnRlcyBkYXMgc3Vic2NyacOnw7VlcywgZSBmb2kgcHJlc2VydmFkbyBzZW0gYWx0ZXJhw6fDo286KiAgCioqU3RhdHVzIChuYSByZWRhw6fDo28pOioqIE1JTlVUQSAqKnJldi4yKiogKDIwMjYtMDktMjQpIOKAlCDCpzQuMyBjb252ZXJ0aWRvIGVtIFAtSzYgYXDDs3MgbWVkacOnw6NvIGRvIEVzdHJ1dHVyYSAoVFJJTEhBOTMpIMK3ICoqUC1LNiByYXRpZmljYWRvIHBlbG8gQ29tZW50YWRvcioqIChtZXNtbyBkaWEpIGNvbSBwcmVjaXPDo28gZGUgZ3JhbnVsYXJpZGFkZSBwb3IgY2xhaW0gKMKnNiBkYSByZXNwb3N0YSk7IHNlbSBub3ZvIGFqdXN0ZSBjb25jZWl0dWFsLiBSYXNjdW5obyBmaW5hbCAqKmFudGVzKiogZGEgY2lyY3VsYXJpemHDp8OjbyBhb3MgYXVkaXRvcmVzIChyZXYuMiBudW5jYSBoYXZpYSBzYcOtZG8gw6BzIGphbmVsYXMpLiBQYXJhICoqw7psdGltYSBzdWJzY3Jpw6fDo28qKiBkb3MgZG9pcyB0ZXJyaXRvcmlhaXMg4oCUICoqbsOjbyB2aWdlbnRlKiogYXTDqSBkdXBsYSBzdWJzY3Jpw6fDo28gc2VtIHJlc3NhbHZhLiBBIHJldi4xIHBlcmRlIHZpZ8OqbmNpYSBkZSBjYW5kaWRhdHVyYTsgZG9jdW1lbnRvIG11ZG91IOKHkiAyw5cgbm92by4gIAo=
```

BLOCO C — 1 linha · 309 b · sha256 b9710cbe6d8bc4476dad3ba2443fe9f4f6f1e8322a5f2ee8da1566728177a2fa

```text
KkNvbnRyYXRvIGRhIGNhc2EgKipyZXYuMioqIMK3IFJvZGFkYSA4MiDCtyAyMDI2LTA5LTI0IMK3ICoqVklHRU5URSoqIGRlc2RlIDI0LzA5LzIwMjYgKGR1cGxhIHN1YnNjcmnDp8OjbyBsaW1wYSBjdW1wcmlkYSDigJQgdmVyIGJpbGhldGUgYENPTlRSQVRPX1NBSURBX0NMQUlNS0lUX1ZJR0VOVEUudHh0YCkgwrcgdGV4dG8gYXByb3ZhZG8gPSBkaWdpdGFsIGA4NDE1MzJkYWAsIHByZXNlcnZhZG8gYnl0ZSBhIGJ5dGUgZW0gYENPTlRSQVRPX1NBSURBX0NMQUlNS0lUX3JldjJfQVNTSU5BRE9fODQxNTMyZGFfMjAyNi0wOS0yOS5iYWtgLioK
```

Como decodificar (o decodificador ignora quebras de linha):

```python
import base64, hashlib
A = base64.b64decode("<cole o BLOCO A aqui>")
print(len(A), hashlib.sha256(A).hexdigest())
# esperado: 1160  3965008adb8f847a11295c215ae7de930efcddfe7a7f25764c341ab13bd90610
```

---

*Fim da carta. Se qualquer conferência do Anexo D não fechar depois das edições dos Anexos A e B, **não improvise**: pare e reporte
ao operador com o que mediu. O projeto roda com regra clara: a digital é a verdade.*

*Adendo da oficina nova (30/09): todas as conferências fecharam — 5/5 vigentes · 6/6 cópias assinadas · ZERO divergências.
A.3 reconstruído via Anexo F (Opção C do operador). Publicado em 30/09/2026.*
