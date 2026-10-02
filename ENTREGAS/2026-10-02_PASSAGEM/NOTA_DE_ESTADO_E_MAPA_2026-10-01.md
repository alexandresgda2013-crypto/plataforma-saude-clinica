# 📒 NOTA DE ESTADO E MAPA — 01/10/2026 (atualizada ao fim do dia)

✏️ Escrita pelo agente do chat (Arena) · 👤 para o **operador** e para **qualquer agente que chegue depois** · 🔒 **0 ciência** (nada científico foi analisado aqui)

> ⚠️ **Onde este arquivo está:** só na área de trabalho do agente do chat, para ser aberto no visualizador do Arena.
> **Ele NÃO está no GitHub.** Para entrar no GitHub, o operador abre **um agente novo** do Arena e cola a mensagem de publicação que o agente do chat escrever. **O agente novo** é quem grava no `main`.
> Esta nota **não aprova nem declara vigente nenhum documento**. Vigência só por frase do operador.

---

## 1️⃣ Em uma frase: onde estamos

Os pacotes do crivo (FLUXO + Livretos 2, 3 e 4) estão **publicados no `main`** (PRs nº 4, 5 e 6, este último relatado pelo agente de publicação, com as 7 digitais conferidas). A **reorganização do rito** foi acordada em 01/10 com o Comentador, o Auditor-Estrutura e o Auditor-Mestre (ver §12). O **operador ratificou as 4 erratas de 29/09 e decidiu a opção (i) do L-NT** (ver §10). O próximo passo real continua sendo o **crivo documental do Livreto 1** (`1º IDS_OFICIAIS.md`), com 3 agentes do Arena que recebem os arquivos **carregados pelo operador**.

---

## 2️⃣ 🗺️ Mapa: quem faz o quê neste ambiente

| Quem | O que faz | O que NÃO faz |
|---|---|---|
| 🧑 **Operador** | É o carteiro: copia a mensagem do chat e cola nos agentes. Carrega os arquivos nos agentes do crivo. **Aprova** com a frase dele (letra a letra + data). | — |
| 💬 **Agente do chat** (quem mantém o diálogo) | Conversa, lê arquivos, calcula digitais, escreve textos, mensagens e programas. Pode gravar arquivo para o operador abrir no visualizador. | **Não publica no GitHub** (a sessão se encerra quando um merge acontece). |
| 🚀 **Agente novo** (janela nova do Arena) | Recebe a mensagem colada pelo operador e faz **commit, push, PR e merge**. | Não guarda a conversa. Depois do merge a sessão dele também se encerra. |
| 🔵 **3 agentes do crivo** (janelas novas) | Recebem os **arquivos carregados** e dão um parecer curto, cada um sozinho. | **Não veem o repositório.** Não veem o parecer um do outro. |
| 💬 **Comentador** (ChatGPT, plano gratuito) | Faz crítica e recomendação. | Lê **só a folha** do crivo, nunca os documentos. |
| 🟠 **Auditor do território** (Mestre ou Estrutura) | Verifica o documento, guiado pela folha. | — |
| 🗄️ **GitHub (`main`)** | É a **memória durável**. Quem chega depois começa pelo `BIBLIOTECAS/ONDE_PARAMOS.md` e pelo `CHANGELOG_GERAL.md`. | — |

**Regra de ouro, em uma linha:** *o agente do chat escreve → o operador leva → o agente novo publica → o `main` guarda.*

**Papéis dos auditores (Roteiro):** **Mestre** = governança, contratos, rito, processo. **Estrutura** = estrutura, schemas, compatibilidade, materialização, coerência técnica.

---

## 3️⃣ O que está no `main` hoje (PRs nº 4, 5 e 6 mergeados)

| Arquivo | sha256 (início) |
|---|---|
| `ENTREGAS/2026-09-30_CRIVO_LIVRETOS/FLUXO_CRIVO_DOCUMENTAL_2026-09-30.md` | `1d4e9a230f40aca9…` |
| `…/LIVRETO_02_PROTOCOLO_ESCOPO_B1_2026-09-30.md` | `36ed0fa51acf3da7…` |
| `…/LIVRETO_03_LISTA_CANONICA_B1_SM02_2026-09-30.md` | `15001205495496f2…` |
| `…/LIVRETO_04_BLOCO_DE_ESTADO_V18_2026-09-30.md` | `d5a7a083d5a79188…` |
| `…/DIGITAIS.txt` | `a4a1fc817cb2d0fc…` |
| `BIBLIOTECAS/ONDE_PARAMOS.md` | `66c49a741ddf06cd…` |
| `BIBLIOTECAS/CHANGELOG_GERAL.md` | `fc86fce57078762f…` (completa: `fc86fce57078762f8d0f42c04b360fb6d53928bc1ae1f2dbf1367da2555a09f5`, impressa pelo agente de publicação) |
| `ENTREGAS/2026-09-29_CRIVO_LIVRETOS/LIVRETO_01_IDS_OFICIAIS_2026-09-29.md` (**o livreto**, não o catálogo) | `5cfdee31abe3cd3c…` |

> 📁 **Sobre os nomes de pasta:** `2026-09-30_CRIVO_LIVRETOS` mantém o nome do dia em que nasceu; os arquivos dentro foram atualizados em 01/10 (PR nº 6). O Livreto 1 mora na pasta `2026-09-29_CRIVO_LIVRETOS`. São **4 livretos**; as duas pastas são só acidente de data. Não renomear (quebraria caminhos citados).

**Documentos sob crivo (não mudaram, e não devem mudar antes do crivo):**

| Livreto | Documento | sha256 (início) |
|---|---|---|
| 1 | `1º IDS_OFICIAIS.md` (**o objeto sob crivo**) | `3c0eccac…` |
| 2 | `2º PROTOCOLO DE ESCOPO — B1 (v1.3).md` | `943425cd…` |
| 3 | `5º_LISTA_CANÔNICA___B1__SM-02_V1_5.md` | `20efa89f…` |
| 4 | `6º BLOCO_DE_ESTADO__v1_8.md` | `7db41d40…` |

> 📏 **A régua é a digital.** Se um sha256 não bater com o esperado: **pare e avise**. Nunca ajuste por tentativa.

---

## 4️⃣ O fluxo do crivo (vale para os Livretos 1 a 4)

1. 🔵 **3 agentes do Arena**, em janelas próprias, com os arquivos carregados pelo operador. Cada um dá um parecer curto.
2. 📋 **Folha da casa:** o agente do chat junta os 3 pareceres numa folha (modelo no FLUXO §5).
3. 💬 **Comentador:** lê **só a folha** (FLUXO §7).
4. 🟠 **Auditoria territorial por ponto (fixa, sem gatilho pela folha):** Mestre e Estrutura verificam cada um os seus pontos (matriz no §12), recebendo o documento, a folha e só o que o território exige; um não vê o outro (FLUXO §6).
5. ⚖️ **Fechamento da casa.** Se houver ressalva: nova rodada **só dos pontos**.
6. ✅ **Aprovação:** só pela **frase do operador** (R-CITA-1).

Pergunta única de cada livreto, no molde: *«Concordam em declarar VIGENTE, para uso operacional no piloto oficial B1.SM02.014, o [documento] (`digital`)?»* Resposta: de acordo / com ressalva / em desacordo.

**Ordem dos livretos:** 1 → 2 → 3 → 4. Se o Livreto 1 alterar o catálogo de IDs, refazer a conferência de IDs dos Livretos 2, 3 e 4.

---

## 5️⃣ 📦 Livreto 1 — o que carregar em CADA um dos 3 agentes

Estes são os arquivos que o texto do Livreto 1 cita. Tirar algum é decisão do operador.

| # | Arquivo | Onde está | sha256 (início) |
|---|---|---|---|
| 1 | `LIVRETO_01_IDS_OFICIAIS_2026-09-29.md` | `ENTREGAS/2026-09-29_CRIVO_LIVRETOS/` | `5cfdee31…` |
| 2 | `1º IDS_OFICIAIS.md` (**o documento sob crivo**) | `uploads/Atuais/Documentos/` | `3c0eccac…` |
| 3 | `_ids_oficiais.json` | `Ferramentas de geração e auditoria/01_norteadores/_derivados_trilha46/` | `d0ff2647…` |
| 4 | `_ids_oficiais.PROVENIENCIA.json` | mesma pasta do nº 3 | `573b7edb…` |
| 5 | `CANDIDATOS_IDS_OFICIAIS — v1.0.md` | `uploads/Atuais/Documentos/` | `a069de5f…` |
| 6 | `4º COMO EXECUTAR — v1.11 rev.2.md` | `BIBLIOTECAS/_documentos_serie/COMO_EXECUTAR_v1.11rev2_vigente_2026-09-25/` | `1ea6d354…` |
| 7 | `3º SCHEMA-CLAIM — v1.3.md` | `BIBLIOTECAS/_documentos_serie/SCHEMA_CLAIM_v1.3_rev3_vigente_2026-09-25/` | `e9f9e5d8…` |
| 8 | `CONTRATO_SAIDA_CLAIMKIT_rev2_2026-09-24.md` | `BIBLIOTECAS/_documentos_serie/CONTRATO_SAIDA_CLAIMKIT_rev2_vigente_2026-09-24/` | `03cdd19a…` |

(As 8 digitais foram medidas em 01/10/2026 e batem.)

### ✉️ Mensagem de abertura (a mesma nos 3 agentes, depois de carregar os 8 arquivos)

```text
ABERTURA PARA AGENTE ARENA — você recebeu apenas os arquivos carregados nesta conversa. Leia SÓ eles; não procure nem busque outros arquivos. NÃO altere, crie, mova nem apague arquivo; NÃO faça commit, push nem PR; NÃO rode scripts de produção. Responda só em texto.

TAREFA — crivo documental, Livreto 1 de 4. Abra o arquivo LIVRETO_01_IDS_OFICIAIS_2026-09-29.md: ele traz o objeto, a régua (Roteiro §6.1), as 5 perguntas (§5), a pergunta única (§6) e o formato da resposta (§7). Responda exatamente como ele pede. Os caminhos citados no livreto só identificam qual é cada arquivo; o conteúdo é o que foi carregado nesta conversa.

Confira você mesmo as digitais (sha256) dos arquivos carregados contra as do livreto. Se alguma não bater, diga qual e pare nessa peça; não ajuste nada. Trabalhe sozinho: você não verá a resposta de nenhum outro agente. É crivo documental, com 0 ciência: não julgue conteúdo científico.
```

**Depois:** o operador cola os 3 pareceres no chat do agente da casa, que monta a folha.

---

## 6️⃣ ❓ Em aberto (nada disso trava o Livreto 1)

| Ponto | Situação |
|---|---|
| **Observação do operador (01/10):** todo documento atualizado, usado agora ou depois, deve passar pelo crivo das IAs | **Respondido pelo operador (01/10):** as **4 erratas de etiqueta não entram em novo crivo**. Já tiveram 3 verificações independentes do diff (Auditor-Mestre, Auditor-Estrutura e a casa atual, que **não é o agente que fez a errata**), todas com o mesmo resultado, e a classificação «não substantiva» do Mestre. O crivo das 3 IAs vale para o que **mudou em substância** ou **não tem rito registrado** (fila de regularização). |
| **Roteiro (`507eaefa…`)** também foi atualizado em 29/09 | Medido pela casa: texto aprovado 26/09 (`5f8b89dc`) × vigente (`507eaefa`) = 4 linhas removidas (linhas de SHA) e 16 acrescentadas (notas de errata e registro das duas digitais). **A classificação é do Mestre**; depois, a casa redige a frase de ratificação. |
| **Adendas sugeridas pelo Mestre** (AUD-001 Roteiro §18 · AUD-002 Atos · AUD-004 Contrato, corpo) | Aguardam o Mestre ler os bilhetes e o operador decidir. Sem reescrever em silêncio; por adenda. |
| **Ato do COMO v1.10 (`49514344…`)** | O Mestre confirma o status «superado» ao ler `ATO_VIGENCIA_V110_2026-09-25.md` e o bilhete `COMO_EXECUTAR_V110_VIGENTE.txt`. |
| **`L05_…ESPECIFICACAO.md` (`78a0f2af…`)** | 7 cópias idênticas em `ENTREGAS/` (19–21/09), especificação do N2 v1.4; sem ato de vigência achado. «Sem registro suficiente» → fila de regularização. |
| **FLUXO: passo do auditor** (hoje diz «guiado pela folha») | Acordado em 01/10 que o auditor lê **o documento primeiro** e só depois recebe a folha. **Para o Livreto 1**, a instrução vai na mensagem ao auditor (chat); o arquivo `FLUXO_CRIVO_DOCUMENTAL…` só muda numa próxima publicação, **se o operador quiser**. |
| **Fila de regularização** (documento · versão · digital · rito realizado · rito faltante; sem registro = «sem registro suficiente») | Começa **depois do Livreto 1**. A casa monta a partir de Atos, bilhetes e CHANGELOG, sem inventar nomes. |
| **L-NT minuta 2** | Destravada pela decisão (i) de 01/10 (ver §10). Quem a redige é o Auditor-Mestre. |
| **Emenda 2** (bilhetes se declaram) | **Adiada pelo operador, sem prazo.** Não aplicar sem ordem expressa. |
| **Crivo do Livreto 1** | Aguarda o operador abrir os 3 agentes e trazer os pareceres. |

---

## 7️⃣ ✅ Decisões do operador (30/09 e 01/10) que valem

- Crivo **documental** com 3 agentes do Arena que recebem os arquivos **carregados pelo operador**. **Sem acesso ao repositório** (nem "sala limpa" no GitHub). Os 3 não veem o parecer um do outro (0 ciência).
- Mestre e Estrutura são pagos e gastam rápido: usar **só onde necessário**, por território. O Comentador é gratuito e trava com muitos documentos: dar a ele **só a folha**.
- **Os livretos já estão bons o bastante.** Não refinar mais: o foco é o crivo dos 4 documentos. «Zelo, mas não demais, senão não andamos».
- **Publicar + mergear no mesmo ato** (`ONDE_PARAMOS.md` §9). A prateleira (branch `arena/…`) é só rampa.
- **Mensagens para os agentes vão no corpo do chat**, em bloco de código, com o passo a passo mínimo e **dizendo quem faz cada passo**.
- Não decidir sozinho aberturas de acesso, rito ou atribuição de auditor: **perguntar ao operador antes**.
- **O documento sob crivo fica intacto** até o crivo: mexer muda a digital e invalida o pacote.
- **Rito da frase (01/10):** a casa redige a frase, sempre rotulada **«sugestão da casa»**, com documento e digital; o operador a copia e **cola de volta no chat da casa, com a data do dia**. A frase só vale como dele depois que ele a cola (R-CITA-1).
- **A data de uma frase é a do dia em que o operador a diz**; fatos anteriores (ex.: errata de 29/09) entram dentro da frase, como referência.
- O operador quer que a posição técnica da casa seja **fundamentada** (engenharia de software e ciência) e que a casa **não devolva a ele** o que pode fundamentar.
- **Erratas de etiqueta (01/10):** não passam por novo crivo das 3 IAs quando o diff foi medido de forma independente por mais de um auditor e classificado «não substantivo». O crivo é para o que mudou em substância ou não tem rito registrado.
- **Atribuição de auditor por ponto de verificação (território do ponto), não pelo nome do documento** (acordada com o Comentador em 01/10; publicada no PR nº 6).

---

## 8️⃣ 🚦 Regras que valem sempre (para não tropeçar)

1. **0 ciência:** não julgar achados científicos, estudos nem PMIDs. Isto é crivo documental.
2. **Divergência se resolve lendo o documento**, nunca por votação.
3. **A digital não bateu? Pare e avise.** Não ajuste por tentativa.
4. **Sem force** (push ou merge). Conflito: parar e indicar, sem decidir sozinho.
5. **Estar no `main` não declara nada vigente:** `EXISTENTE ≠ VALIDADO ≠ VIGENTE ≠ AUTORIZADO PARA USO` (Roteiro §6.1). A vigência só vem pela frase do operador.
6. **O merge encerra a sessão que o fez.** Colher conferências e links **antes** de mergear.
7. O **`main` é a fonte durável**; as conversas se perdem. Quem chega depois começa pelo `ONDE_PARAMOS.md` e pelo `CHANGELOG_GERAL.md`.
8. Cada pedido de publicação deve trazer: link da pasta do dia + caminho de download.

---

## 9️⃣ Se o operador voltar daqui a uma semana — por onde começar

1. Abra o `BIBLIOTECAS/ONDE_PARAMOS.md` no GitHub (`main`) e leia as §8 e §9.
2. Leia os §10 a §12 desta nota (atos do operador, mapa de nomes, acordo da reorganização). Veja se existe o resultado do crivo do Livreto 1. Se não existir: o pacote está na seção 5 desta nota. É só carregar os 8 arquivos nos 3 agentes e colar a mensagem.
3. Se o agente do chat for novo, cole esta nota inteira nele antes de qualquer pedido.

---

## 🔟 Atos do operador em 01/10/2026 (frases coladas no chat da casa)

> **Procedência (R-CITA-1):** as frases abaixo foram **sugeridas pela casa** (rotuladas) e **coladas de volta pelo operador, sem alteração de palavras, no chat do agente da casa, em 01/10/2026**. Valem como atos do operador a partir de ter sido coladas. Registro **local** até um agente novo publicar.

### Ratificação das 4 erratas de etiqueta de 29/09 (arquivo vigente atual)

> Aprovo como vigente o COMO EXECUTAR — v1.11 rev.2, digital 1ea6d354, de 01/10/2026 (errata de etiqueta de 29/09/2026; texto aprovado em 25/09/2026, digital 2efc0edd).
>
> Aprovo como vigente o Schema-Claim v1.3 — rev.3, digital e9f9e5d8, de 01/10/2026 (errata de etiqueta de 29/09/2026; texto aprovado em 25/09/2026, digital 28cbc9c7).
>
> Aprovo como vigente o Contrato de Saída do Claim Kit — rev.2, digital 03cdd19a, de 01/10/2026 (errata de etiqueta de 29/09/2026; texto aprovado em 24/09/2026, digital 841532da).
>
> Aprovo como vigente a L-06 — Minuta 3 consolidada rev.6, digital acd76b24, de 01/10/2026 (errata de etiqueta de 29/09/2026; texto aprovado em 22/09/2026, digital 98e90bdc).

**Como ler:** os Atos de 22 a 25/09 valem para o **texto assinado** (digital antiga). A frase de 01/10 vale para o **arquivo vigente atual** (digital nova). Cada uma cita as duas. A classificação do diff («não substantiva», as 4) é do Auditor-Mestre, com medição independente da casa e do Estrutura. **O Roteiro não está nesta ratificação** (aguarda classificação do Mestre).

### Decisão do L-NT (opção i)

> Decido a opção (i) do fluxo de claims, com a bifurcação desenhada: o claim clínico é insumo de evidência, não de conhecimento; a afirmação vai à Biblioteca da entidade pelo rito normal (§5.5 da Arquitetura V2.3, digital 498e7df9), e a evidência segue N1 → N2 → NT. A opção (ii) fica descartada. Decisão de 01/10/2026.

**Alcance:** destrava a **minuta 2 do L-NT**. **Não declara vigente nenhum documento** (a minuta 2 ainda não existe). Antes desta frase, a busca (CHANGELOG local até 30/09, `ONDE_PARAMOS`, Roteiro, materiais de 29–30/09) não achou decisão do operador entre (i) e (ii); o último registro (21–22/09) dizia «resta 1 linha do operador».

**Procedência das frases de vigência antigas (já no repositório):** Contrato 24/09 (Rodada 85) · Schema-Claim 25/09 (Rodada 92) · COMO v1.10 25/09 (Rodada 96) · COMO v1.11 rev.2 25/09 · L-06 22/09 (bilhete `L06_VIGENTE.txt`). A confissão **C79-1** (22/09: frase escrita pela casa e atribuída ao operador; corrigida por errata datada) está no CHANGELOG e deu origem à R-CITA-1.

---

## 1️⃣1️⃣ Mapa de nomes: papel + digital (para ninguém se perder)

Cada documento tem **três arquivos** (pacote `ENTREGAS/2026-09-29_ATUALIZACOES/`). **Ao citar, usar sempre «documento + papel + digital».** O número do anexo **não** segue a ordem do Contrato/Schema/COMO.

| Documento | Vigente (hoje) | Texto assinado (inteiro) | Bilhete (nota curta) |
|---|---|---|---|
| COMO EXECUTAR v1.11 rev.2 | `01_COMO_EXECUTAR_v1.11rev2_VIGENTE_2026-09-29.md` · `1ea6d354` · 36.254 B | `ANEXO_1_texto_assinado_2efc0edd_COMO_EXECUTAR_2026-09-29.md` · `2efc0edd` · 35.223 B | `02_COMO_EXECUTAR_V111_VIGENTE_bilhete_2026-09-29.txt` · `71c60fa6` |
| Schema-Claim v1.3 rev.3 | `07_SCHEMA_CLAIM_v1.3_rev3_VIGENTE_2026-09-29.md` · `e9f9e5d8` · 10.304 B | `ANEXO_2_texto_assinado_28cbc9c7_SCHEMA_2026-09-29.md` · `28cbc9c7` · 9.350 B | `11_BILHETE_SCHEMA_CLAIM_V1_3_VIGENTE_2026-09-29.txt` · `72e52812` |
| Contrato de Saída rev.2 | `08_CONTRATO_SAIDA_CLAIMKIT_rev2_VIGENTE_2026-09-29.md` · `03cdd19a` · 12.950 B | `ANEXO_3_texto_assinado_841532da_CONTRATO_2026-09-29.md` · `841532da` · 11.205 B | `12_BILHETE_CONTRATO_SAIDA_CLAIMKIT_VIGENTE_2026-09-29.txt` · `ab370312` |
| L-06 rev.6 | `10_L06_VIGENTE_2026-09-29.md` · `acd76b24` · 27.523 B | `ANEXO_4_texto_assinado_98e90bdc_L06_2026-09-29.md` · `98e90bdc` · 26.830 B | `14_BILHETE_L06_VIGENTE_2026-09-29.txt` · `2e41272a` |
| Roteiro | `09_ROTEIRO_PLATAFORMA_VIGENTE_2026-09-29.md` (= `ROTEIRO DE TRABALHO DA PLATAFORMA.md` da raiz) · `507eaefa` | aprovado 26/09: `5f8b89dc` (`BIBLIOTECAS/_documentos_serie/ROTEIRO_plataforma_vigente_2026-09-27/`) | `13_BILHETE_ROTEIRO_PLATAFORMA_VIGENTE_2026-09-29.txt` · `0d3e5ab1` |

**Livreto 1:** o **livreto** (pacote de instrução) é `5cfdee31…`; o **objeto sob crivo** (`1º IDS_OFICIAIS.md`) é `3c0eccac…`. São arquivos diferentes; não há divergência.
**JSONs do schema:** N1 `schema_referencia_v1.3_N1_b06660fd.json` e N2 `schema_vinculo_v1.4_N2_d96ad15b.json`: digitais medidas pela casa em 01/10, batem com o nome do arquivo.
**Bilhetes ≠ documento:** um bilhete tem 36–62 linhas e **não** serve para `diff`; o texto assinado (ANEXO) é o documento inteiro.

---

## 1️⃣2️⃣ Acordo da reorganização (01/10/2026) — Comentador, Estrutura, Mestre

**Comentador (carta final de encerramento):** diálogo de reorganização **encerrado, sem ressalvas**; só reabre por fato novo, inconsistência documental nova, erro de versão/digital, conflito entre documentos ou problema operacional que exija revisão do rito.

**Fluxo adotado:** 3 agentes Arena (janelas próprias, 0 ciência) → pareceres → **Folha da Casa** → **Comentador** (só a folha) → **auditoria territorial** (Mestre e Estrutura, fixos por ponto, recebem documento + folha + só o seu território) → **fechamento da Casa** (sem votação; lê o documento onde há divergência) → **ordem do operador**. `PARECER ≠ FECHAMENTO ≠ VIGÊNCIA`. O crivo é **0 ciência**; a validação científica dos claims é processo próprio (tríade IA1/IA2/IA3, G1/G2/G3).

**Matriz por ponto (publicada no PR nº 6):**

| Livreto | Auditor-Estrutura | Auditor-Mestre |
|---|---|---|
| 1 — `1º IDS_OFICIAIS` | contagem (146+5), duplicatas, formato, derivado JSON, contradição com Contrato/Schema/COMO | vigência, rito, aprovação, substituição, cadeia documental |
| 2 — Protocolo v1.3 | V1, V2, V4, V5 | V3 (+ verificações de rito/governança) |
| 3 — Lista v1.5 | L1, L2, L3, L5, L6 | L4, L7 (+ rito/governança) |
| 4 — Bloco v1.8 | B1, B2 (inclui P4), B3, B5, B7, B8 | B4 (P1 e P2), B6 |

**Regra das ressalvas:** ressalva → nova rodada só dos pontos; documento alterado → nova digital e novo crivo. **Livreto 1 não é alterado.** **L-NT** sem registro verificável não bloqueia os Livretos, salvo dependência demonstrada pelo Mestre (agora a decisão (i) está registrada, §10).

**Auditor-Estrutura (resposta de 01/10):** abriu só os 6 arquivos indicados; digitais conferidas; 0 CRLF. **Estrutura intacta nos 3 documentos dele** (Contrato: 3 trechos; Schema-Claim: 2 trechos só em linhas `#`, e sem elas idêntico `bffd4ded3c77d418…`; COMO: 1 trecho). N1/N2 não medidos por ele (medidos pela casa). Observação: «esta minuta» permanece no corpo do Contrato (L132, L207, L215–217). Sem discordância; sugeriu fixar o mapeamento dos anexos por nome (feito no §11).

**Auditor-Mestre (parecer de 01/10):** digitais conferidas (também Arquitetura V2.3 `498e7df9`, Roteiro `507eaefa`, N1, N2). **Classificação: as 4 erratas são NÃO SUBSTANTIVAS quanto ao conteúdo normativo; nenhum documento volta ao rito.** O Status do Contrato é metadado de governança. Achados: **AUD-001** (Roteiro §18 descreve a errata como «apenas a palavra»; imprecisa → adenda) · **AUD-002** (Atos citam a digital assinada → adenda ligando às digitais vigentes; os bilhetes já trazem a ligação) · **AUD-003** (Ato do v1.10: confirmar «superado») · **AUD-004** (Contrato, corpo mantém redação do rito de subscrição → adenda) · **AUD-005** (COMO «em teste» muda só depois do piloto) · **AUD-006** (Schema-Claim: só o trecho após `yaml` parseia). Sem discordância com o território fixo; pendências dele: Atos/bilhetes, Livretos 1–4 (um por vez, com nome, versão e SHA-256), situação de `78a0f2af…`.

**Pergunta aberta ao Mestre (da casa):** diff medido do Roteiro (item §6) aguardando classificação.

### Regra de entrada do auditor e modelo operacional (acordo de 01/10 com o Comentador, após proposta dele sobre economia de créditos)

- **Regra geral (documentos novos e fila de regularização):** o auditor só entra com **uso real no território dele**, e esse uso precisa ser **demonstrável por fato ou dependência concreta do documento**, não presumido por ele «participar do piloto». A pergunta é respondida **antes** do crivo, por fato do documento, **nunca pela folha** (evita o detector depender do que deveria detectar). Para documento novo: ficha curta de uso, escrita pela casa antes do crivo, contestável pelo auditor.
- **Livretos 1–4:** mantém-se a matriz por ponto (acima); os dois auditores continuam nos 4. O uso é demonstrável pelos próprios pontos dos Livretos, que citam o fato (ex.: V3, data interna e falta de bilhete; L4, referências ao Bloco v1.7 e à nota P2; B6, trechos do COMO nas linhas 112–114, 162 e 173–175). Nenhum auditor sai só para economizar crédito.
- **Modelo operacional:** (1) **Livreto 1 primeiro e isolado** (pode mudar o catálogo de IDs); (2) **Livretos 2, 3 e 4 em uma única sessão por auditor**, cada um restrito aos seus pontos (de 8 janelas para 4; se pesar, divide-se em duas); (3) o auditor lê **primeiro o documento** e depois a folha das 3 IAs, para confronto; (4) **documentos antigos ficam fora**.
- **Pacote do Mestre por Livreto** (sempre com a folha): L1 = Livreto 1 `5cfdee31` + `1º IDS_OFICIAIS` `3c0eccac` + `CANDIDATOS_IDS_OFICIAIS — v1.0` `a069de5f` · L2 = Livreto 2 `36ed0fa5` + Protocolo `943425cd` · L3 = Livreto 3 `15001205` + Lista `20efa89f` + Bloco `7db41d40` · L4 = Livreto 4 `d5a7a083` + Bloco + Lista + `CORPUS_CONGELADO_PILOTO_B1SM02014_2026-09-26.md` `20c7159b` + `ENTREGA_TRIDE_PILOTO_014_2026-09-26.md` `b1c6cde3`. Já na base dele: Arquitetura V2.3, Roteiro vigente, COMO, Schema-Claim, Contrato, L-06 (vigentes e assinados), N1, N2, L05 espec. Perguntado a ele: se tem `FASE 2- 02 FILOSOFIA DO PROJETO.md` `27ea3d88` e `DECISOES_ARQUITETURAIS_v2_5` `dac46f78` (LF).
- **Decisão do operador (01/10):** não enviar versão antiga de documento a auditor só para confirmar aposentadoria. O auditor julga o documento pela estrutura, filosofia e ligação com os demais; quando a pergunta é «o que mudou», basta a **diferença em texto**. Ato e bilhete do COMO v1.10: fora (AUD-003 fica como observação).


---

## 1️⃣3️⃣ Parecer do Mestre e correção do Roteiro (01/10/2026, fim do dia) — **substitui as linhas do Roteiro no §6**

- **Parecer do Auditor-Mestre (01/10):** as 4 erratas de etiqueta = **não substantivas**. **AUD-001** (nota (4) do Roteiro, «apenas a palavra») = MENOR. **AUD-004** (Contrato mantém «esta minuta» no corpo) = adenda, decisão do operador. **AUD-005** (COMO «EM TESTE») só muda após o piloto. **AUD-006** (Schema-Claim sem cercas). **AUD-007 (MODERADO):** **não há frase do operador aprovando o Roteiro** como vigente; resolve-se com a frase de ratificação, citando a digital final completa. **AUD-008 (MENOR):** o bilhete do Roteiro deve citar a digital sobre a qual cada concordância foi dada.
- **A cadeia do Roteiro:** `2c286ca1…` (concordado 2× em 26/09, sobre esta digital) → `5f8b89dc…` (errata de 26/09) → `507eaefa…` (errata de 29/09). As duas erratas foram a pedido do operador e **não têm concordância própria registrada**. A expressão «texto aprovado em 26/09» ia além do registro.
- **Correção pedida pelo operador em 01/10:** `Atualização` 27-09 → 01-10; nota (4) com a descrição medida por documento (COMO: título + bloco de 14 linhas · Schema-Claim: título + 1 linha interna + bloco de 13 · Contrato: título, Status, rodapé + bloco de 15); nota (5) sem «aprovado»; nota (6) nova. O Mestre mediu e confirmou a redação curta (`a0efc7d0…`, 38.372 B) como não substantiva. **A redação final adotada é a mais completa:** `aa01bfe87044f4724e6c4928c6d073e0eb24003090ce69099fd363bba40c5579`, 38.971 B, 1.174 CRLF, 3 linhas removidas e 6 acrescentadas, corpo a partir de «Objetivo:» idêntico. **O Mestre ainda não mediu esta digital.** Título interno «- 27.09.2026» mantido (nomeia a edição).
- **Publicação:** pasta `ENTREGAS/2026-10-01_ROTEIRO_E_ATO/` (bilhete novo, Ato do operador de 01/10, programa de aplicação com todas as conferências, `DIGITAIS.txt`). Programas de teste: `ROTEIRO_CORRECAO_PROPOSTA_2026-10-01.py` (variantes A e B).
- **Pendente:** (1) **frase do operador** para o Roteiro, com a digital completa do arquivo final, **só depois de gravado e medido**; (2) o Mestre medir `aa01bfe8…`; (3) Livreto 1: o operador abre os 3 agentes; (4) o Mestre: Livretos 1–4 e minuta 2 do L-NT; (5) fila de regularização (inclui `L05_…ESPECIFICACAO.md` `78a0f2af`); (6) pergunta sem resposta: quais documentos foram «aprovados sem crédito».


---

## 1️⃣4️⃣ Atualização de 02/10/2026 (publicação)

- **Esta nota foi publicada em 02/10/2026**, em `ENTREGAS/2026-10-02_PASSAGEM/`, junto com a `CARTA_DE_PASSAGEM_2026-10-02.md`. O aviso do topo («Ele NÃO está no GitHub») valia para o momento em que foi escrito.
- **Já publicado no `main`:** PR nº 7 (merge `71ab6c32…`): errata do Roteiro (`aa01bfe8…`), bilhete novo, Ato do operador de 01/10 e `.bak`. PR nº 8 (merge `c39ea774…`): ajuste de datas em CHANGELOG e ONDE_PARAMOS.
- **Decisão do operador (02/10):** não mandar ao Mestre um pedido separado para medir `aa01bfe8…`. O bilhete declara que ele mediu só a redação curta (`a0efc7d0…`).
- **Em conflito entre esta nota e o `main`** (`ONDE_PARAMOS.md` e `CHANGELOG_GERAL.md`), vale o `main`.
