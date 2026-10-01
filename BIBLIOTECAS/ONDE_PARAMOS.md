# ONDE PARAMOS
O PRIMEIRO ARQUIVO A LER — por qualquer agente, auditor ou pessoa que chegue depois.

Atualizado em: **30/09/2026** (fim do dia)

> Como este cartão funciona: ele é atualizado **todo dia** — o último acontecimento entra sempre **com data**.
> Quem publica no GitHub, publica este cartão junto. O histórico completo e antigo fica em
> `BIBLIOTECAS/CHANGELOG_GERAL.md`. Se a sessão do Arena parar de funcionar, **outro agente retoma o trabalho
> lendo este arquivo** — não é preciso adivinhar nada.

## 1) Último acontecimento — 30/09/2026
- **Publicado (PR nº 3, `main` em `1b4e971`):** `ENTREGAS/2026-09-30_PACOTES_CHAT_NOVOS/` — documento de 181 linhas,
  digital `204e244b…`, conferida de novo no `main` depois do merge.
- **Próximo trabalho do Roteiro (§19):** a ordem é validação dos documentos → vigência → pacotes finais → piloto oficial
  `.014`. O que destrava é o **crivo documental dos 4 livretos** (item 29).
- **Crivo — orientação do Comentador (repassada pelo operador):** quem faz o crivo e o fechamento são as **3 IAs**,
  documento por documento. O Auditor-Mestre (governança, rito, processo) e o Auditor-Estrutura (estrutura, schemas,
  coerência técnica) auditam cada um o seu território, **sem substituir** as IAs, em janelas próprias e sem ciência do
  parecer um do outro. Pacote **enxuto**: base comum indispensável + só o adicional necessário.
  Pontos que o auditor deve verificar entram como **pontos de verificação**, nunca como correção prévia.
- **Pacotes dos Livretos 2, 3 e 4 montados** (documentos sob crivo **intactos**): Protocolo de Escopo B1 v1.3 (`943425cd…`),
  Lista Canônica B1/SM-02 v1.5 (`20efa89f…`) e Bloco de Estado v1.8 (`7db41d40…`). Pasta:
  `ENTREGAS/2026-09-30_CRIVO_LIVRETOS/` (3 livretos + `DIGITAIS.txt` + zip). **AINDA NÃO PUBLICADOS** — ver §7.
- **Aguardando (24 h):** crédito dos Auditores Mestre e Estrutura e de uma das IAs. O crivo dos 4 livretos abre depois disso.
- **Emenda 2 (bilhetes com prefixo `BILHETE —`) — NÃO aplicada.** A carta trouxe 6 digitais-alvo; das 6, só **1** bateu
  (`COMO_EXECUTAR_V111_VIGENTE.txt`); as outras 5 não. A aplicação **parou**, como a carta manda. Nenhum bilhete foi
  alterado. Para retomar: pedir ao outro agente o texto exato dos 5 bilhetes (de preferência em base64) ou as digitais
  deles **antes** da emenda. O operador ainda não deu ordem de aplicar.

### Acontecimento anterior — 29/09/2026
- As **4 pendências de vigência** foram resolvidas no mesmo dia (Roteiro §18 com as duas digitais por base ·
  bilhete do Roteiro reescrito · bilhete do v1.10 virou HISTÓRICO · L-06 passou a declarar o próprio estado).
- **Conferência de digitais medida:** 5/5 arquivos vigentes batem com o bilhete · 6/6 cópias assinadas
  reproduzem a digital original · **ZERO divergências**.
- *(corrigido em 30/09)* A prateleira de 29/09 **foi publicada em 30/09/2026** (`main`, PR nº 2). A linha de 29/09 que dizia
  "pronta, mas ainda não publicada" era do fim daquele dia e ficou desatualizada.

## 2) A seguir (combinado com o operador)
- **4 livretos pelo crivo das 3 IAs** (+ Mestre e Estrutura nos seus territórios), um por um: o **1º** (IDs oficiais) está
  no GitHub aguardando veredito; os **pacotes do 2º, 3º e 4º estão prontos** (em `ENTREGAS/2026-09-30_CRIVO_LIVRETOS/`) e
  **faltam publicar**. Ordem sugerida de abertura das janelas: 1 → 2 → 3 → 4 (um pacote depende do veredito do anterior).
- **Depois dos vereditos:** vigência **só por ordem do operador** → pacotes finais → piloto oficial `.014` (Roteiro §19).
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
- **Gaveta do dia (30/09):** `ENTREGAS/2026-09-30_CRIVO_LIVRETOS/` (Livretos 2, 3 e 4 + DIGITAIS.txt + zip) — **não publicada**
- **Publicada em 30/09:** `ENTREGAS/2026-09-30_PACOTES_CHAT_NOVOS/` · **Livreto 1:** `ENTREGAS/2026-09-29_CRIVO_LIVRETOS/`
- **Gaveta de 29/09:** `ENTREGAS/2026-09-29_ATUALIZACOES/` (LEIA_PRIMEIRO + documentos + bilhetes + zip + DIGITAIS.txt) — publicada
- **Diário datado:** `BIBLIOTECAS/CHANGELOG_GERAL.md`
- **Documentos vigentes + bilhetes:** `BIBLIOTECAS/_documentos_serie/`
- **Roteiro da plataforma:** `ROTEIRO DE TRABALHO DA PLATAFORMA.md` (raiz do projeto)

## 5) Para o agente que chega agora (retomada em 1 minuto)
1. **Confira o estado:** branch `arena/01a0e9e1-plataforma-saude-clinica` (a prateleira) — `git log --oneline -5` e `git status`.
   Se houver mudanças locais não registradas, registre-as primeiro (a cópia de segurança da bancada pode descartar o registro do commit — os arquivos ficam).
2. **O lote a publicar** é a **gaveta datada mais recente** em `ENTREGAS/` — em 30/09: `ENTREGAS/2026-09-30_CRIVO_LIVRETOS/` (ver §7).
3. **Publique:** prateleira `arena/…` → depois `main` pelo caminho normal (PR → merge). Nunca force.
4. **Entregue ao operador:** **link da pasta do dia no GitHub + caminho de download** (é obrigatório a cada publicação — regra do operador).
5. **Combinações do operador:** linguagem simples e analógica · não decidir conflito sozinho (indicar o conflito) · **não rodar os scripts** · não varrer o repositório inteiro · se o GitHub não responder, avisar — não tentar contornar.

## 6) Pós-30/09 — lote vindo de outra sessão (colado pelo operador)
- A rodada final de 29/09 está publicada (`main`, PR nº 2).
- **Lote novo:** `ENTREGAS/2026-09-30_PACOTES_CHAT_NOVOS/` (pacotes revisados p/ chats novos do piloto, com fluxograma) — recebido do operador em 30/09, colado da sessão anterior (que perdeu o GitHub após o merge do PR nº 2). Digital do documento: `204e244b…` (conferir após recriar; se não bater, parar e avisar — não ajustar).
- **Publicado (feito em 30/09):** nivelamento com o `main` (merge, sem force) → commit `59315c4` → **PR nº 3** → `main` em `1b4e971`. Digital re-medida no `main`: `204e244b…` ✓.

## 7) Pendente de publicação — Livretos 2, 3 e 4 (30/09/2026, fim do dia)
- **Por que não subiu:** a sessão do Arena foi encerrada quando o PR nº 3 foi integrado (o GitHub deixou de aceitar envios dela).
  O operador **não consegue baixar o zip** pelo Arena; a publicação só pode sair de uma **sessão nova**.
- **O que publicar:** a pasta `ENTREGAS/2026-09-30_CRIVO_LIVRETOS/`:
  - `LIVRETO_02_PROTOCOLO_ESCOPO_B1_2026-09-30.md` — 253 linhas · `2210e5b3…`
  - `LIVRETO_03_LISTA_CANONICA_B1_SM02_2026-09-30.md` — 282 linhas · `c2aa4646…`
  - `LIVRETO_04_BLOCO_DE_ESTADO_V18_2026-09-30.md` — 284 linhas · `21564747…`
  - `DIGITAIS.txt` e `CRIVO_LIVRETOS_2_3_4_2026-09-30.zip` (este último é empacotamento; pode ser refeito).
- **Como transportar, se a sessão nova não herdar os arquivos:** o método já usado em 30/09 — **base64** do arquivo, recriar,
  conferir o `sha256` contra o `DIGITAIS.txt` (se não bater, parar e avisar) — **um arquivo por vez**.
- **Regras que continuam valendo:** publicar só por ordem expressa do operador · nivelar com o `main` por merge, sem force ·
  entregar link da pasta + caminho de download.

## 8) Decisão do operador — fluxo do crivo documental (30/09/2026, noite)
- **Registro:** a partir da mensagem do operador: «O comentador é muito bom para crítica e aprovação, confirmou o fluxo, concordo com o 2 também». É decisão de rito; **não** aprova documento algum.
- **Vale** `ENTREGAS/2026-09-30_CRIVO_LIVRETOS/FLUXO_CRIVO_DOCUMENTAL_2026-09-30.md`: 3 agentes Arena → folha da casa → Comentador (lê só a folha) → auditor do território (Mestre e/ou Estrutura) → fechamento da casa → aprovação por frase do operador.
- **Substitui** o que o §1, o §7 e o CHANGELOG de 30/09 dizem sobre «3 IAs + 2 auditores em 5 janelas independentes». Motivo: nos documentos não havia produto das 3 IAs para os auditores inspecionarem; agora há a folha. Também poupa créditos.
- **Quem audita (atualizado em 01/10/2026):** cada ponto de verificação vai ao auditor do território do ponto, não do nome do documento (Estrutura: formato, schema, coerência; Mestre: vigência, rito, decisões do operador; todo documento tem ao menos um ponto do Mestre). Tabela no FLUXO §3. Substitui a atribuição por documento de 30/09.
- **Publicação:** as alterações desta rodada entram no PR nº 4; merge e push só por ordem expressa do operador. Os 3 agentes Arena recebem os arquivos do pacote enxuto carregados no chat pelo operador (sem acesso ao repositório).

## 9) REGRA DE PUBLICAÇÃO (oficializada pelo operador em 30/09/2026, noite) — vale até ele revogar
- **A prateleira é só rampa.** A branch `arena/…` não guarda documento: tudo o que sobe para ela **segue para o `main` no mesmo ato** (publicar + mergear). Nada fica parado na branch.
- **Motivo: rastreabilidade.** Se um agente parar, o que está no `main` não se perde, e qualquer agente retoma pelo `ONDE_PARAMOS.md` e pelo `CHANGELOG`. Não é questão de vigência: `EXISTENTE ≠ VALIDADO ≠ VIGENTE ≠ AUTORIZADO PARA USO` (Roteiro §6.1).
- **Como:** ao fim de cada bloco, o agente que envia (1) atualiza o `ONDE_PARAMOS.md`, (2) faz o push sem force, (3) abre ou atualiza o PR e o **mergeia** no `main`, (4) entrega o link da pasta do dia e o caminho de download. Conflito: parar e indicar, sem decidir sozinho.
- **Consequência conhecida:** o merge encerra a sessão que o fez. Por isso a sessão que mantém o diálogo deixa o `ONDE_PARAMOS.md` em dia **antes** de cada envio, e a sessão seguinte começa pelo `main`. Conferências e links devem ser colhidos **antes** do merge.
- **Fim do transporte manual:** base64, conferidores e pastas temporárias deixam de ser necessários.
- **Ressalva:** estar no `main` não declara nada vigente; a vigência segue só por frase do operador (R-CITA-1).
- **Origem (palavras do operador):** «a prateleira é só uma rampa até o main, não pode servir de depósito de documento, nela não para nada, só passa» · «vamos oficializar a questão de a hora de enviar para a prateleira já publicar» · «pode fazer que eu já envio junto com o último código para o agente publicar e mergear (junção)».
