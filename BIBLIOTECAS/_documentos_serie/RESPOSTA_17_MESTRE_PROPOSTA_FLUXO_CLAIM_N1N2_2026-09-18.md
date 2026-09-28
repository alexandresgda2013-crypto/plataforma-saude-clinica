# RESPOSTA 17 — MESTRE: PROPOSTA DO OPERADOR "Formalização do fluxo dos Claims Clínicos" — bancada verificou ANTES da deliberação

**Data:** 2026-09-18 · **Rodada:** 31 (temática — pausa da produção; retomamos exatamente onde estávamos: 20 unidades-piloto NT-B1 e minuta 2 do L-06) · **Trilha:** 50 (52/52 VERDE, reexecutável) · **decisoes rev.38.**

---

## 0. Objeto e ancoragem

O operador enviou a proposta **"PROPOSTA DE FORMALIZAÇÃO DO FLUXO DOS CLAIMS CLÍNICOS"** (Claim Clínico aprovado → Evidências/Bibliografia → N1 → N2 → camadas posteriores), dirigida a você e ao Auditor de Estrutura, pedindo deliberação A/B/C/D.

Verbatim arquivado pela bancada em:
`_documentos_serie/OPERADOR_PROPOSTA_fluxo_claim_N1N2_recebido_2026-09-18/`
· arquivo `OPERADOR_PROPOSTA_FORMALIZACAO_FLUXO_CLAIMS_CLINICOS_2026-09-18.md`
· **sha256 `4ede1c8165005f23d071c522ebf059bd9bc4e10d52083d17988adec807ef308b`** · 13.532 bytes · 520 linhas (agrupadas por `\n`)
· digitais próprias na pasta. **Operador: repasse os MESMOS bytes às duas frentes; cada qual ancora pelo sha acima.**

Declaração de camada do arquivo: fonte = mensagem do operador (bloco de código, sem anexo); digitado verbatim pela bancada; newline LF; NFC. Nenhum arquivo novo em `uploads/` referente a este objeto (medido, trilha 50 A6).

---

## 1. O que a proposta É, no registro do projeto (três precisões medidas)

**1.1 — Ela fecha uma pendência nomeada, não reabre nada.** A "decisão da camada" está pendente EM SEU NOME desde a rodada 23, registrada verbatim: *"DECISÃO DA CAMADA — agora com 3 opções registradas, dona: OPERADOR (a casa mede; não decide)"*. A direção da proposta do operador é a da **opção (c), cuja autoria é do comentador** (crédito registrado): *"kit = ferramenta de curadoria; produto deposita em Evidências/Bibliografia; sem nova camada…"*. A proposta do operador adota essa direção e pede apenas a operacionalização. Fica honrado o enunciado dele: "não pretende reabrir decisões já encerradas".

**1.2 — A frase decisória-mãe não estava no registro verbatim.** Medido: "biblioteca canônica" aparece 2× em `decisoes_B1.md`, ambas no contexto V2/D-V2-DIAGRAMA-DUPLO (não como decisão); "claim clínico" 0×. **Esta proposta é o primeiro registro formal da decisão-mãe** — e a rev.38 a registra como tal. Não é falha de ninguém: é exatamente a lacuna que a proposta declara fechar.

**1.3 — A guarda-gêmea já vigora na arquitetura.** A V2.2 vigente (sha `df7f7cfd…`, conferida intacta hoje) carrega no §5 a frase: Evidências *"não constituem uma segunda Biblioteca Canônica nem uma fonte… independente"*. A proposta harmoniza com ela — e o §9 da proposta ("não ser incorporado ao Motor como segunda base paralela") repisa o mesmo degrau.

## 2. Por que esta proposta toca diretamente o L-NT

A **Parte 8 da sua Minuta 1** lista como dependência: *"Decisão sobre a camada do kit — de onde `uso` e os 4 `gap_pesquisa` são herdados"*. **A proposta é a resposta formal a essa dependência** (igual à §5 do comentador sobre a minuta — convergência que a bancada já tinha registrado na rodada 30).

Medidas que fecham o elo (trilha 50, todas com comando gravado):

1. O kit define `uso` em 3 valores e os aplica por claim: **12 clinico · 6 contexto_mecanistico · 4 gap_pesquisa** nos 22 blocos aprovados (camada ancorada `^\s*uso:` — a camada livre dá 23 e inclui 1 espúria de prosa, `Regra de uso: IL-1β…`, documentada desde a rev.29).
2. Os 4 gap_pesquisa são exatos: **B1.SM02.003 · .006 · .012 · .012c** — são eles as "quatro lacunas" que a proposta cita (e que a sua Parte 5 reconhece).
3. N2 v1.4 já carrega `uso` com enum de 5 valores **superset dos 3 do kit** — a herança não exige alargar enum.
4. Regra medida e falsificada: **todo valor de `uso` do kit é trilha `clinica`** (allOf[1] do N2, prova sintética 3 casos).

**Pergunta-âncora a você (única que a bancada faz, sem pressa):** a Parte 2.2 da minuta diz "*o campo `uso` vem do kit clínico e deveria voltar*". Fechado o fluxo proposto, a linha formal de herança fica **`uso`: kit → N2.uso → NT.uso** (o N2 é o portador contratual). Pergunto se basta ajustar essa linha de herança na redação da minuta 2 do L-NT, sem reescrever o contrato. Substrato: N2.uso enum já é superset (item 3) e o L-NT `entidades[]`/`uso` herdarão de um campo que EXISTE em contrato — o que hoje não existe é o campo por-claim no acervo (censo da rodada 30: uso existe por-vínculo 274/274, não por-claim).

## 3. Não-bloqueios medidos (para o seu planejamento)

1. **O piloto de 20 unidades NT-B1 NÃO depende desta proposta.** Fonte do piloto: os 89 claims canônicos `BLOCO…` da V7 (camada completa — régua de existência entregue na rodada 30). Fonte do kit: 22 claims `B1.SM02.*`. **Namespaces disjuntos, medidos.** O piloto segue sem tocar o eixo clínico.
2. **Selos intactos antes e depois:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos (274) `490675e6…` · V2.2 `df7f7cfd…` · P-8 `be48a5ef…`.
3. **P-8 reexecutado hoje pela regra oficial:** 2 ERRO / 299 AVISO / exit 1 — e os ERRO continuam nomeando exatamente `natureza_evidencia` e `trilha` (a Parte 8 da sua minuta segue exata).

## 4. Conflito arquitetural: nenhum detectado nas camadas medidas

1. A ordem estrutural do desenho vigente é a da proposta: no mapa da V2.2, primeira ocorrência medida **EVIDÊNCIAS < VÍNCULOS < ONTOLOGIA < MOTOR** (camada: bloco-fence do mapa).
2. O §6 da V2.2 (deveres 1–2 da NT) coloca a NT exatamente a jusante de Biblioteca + Evidências/Vínculos — onde a cadeia proposta termina.
3. A separação de papéis (§5 da proposta) coincide com a prática histórica do projeto: você coordena contratos de cadeia (a minuta 2 do L-05 é sua); o Auditor de Estrutura detém os schemas (N1/N2 são dele). A proposta não cruza essas linhas.
4. Dívida viva relacionada (não criada pela proposta): **D-V2-DIAGRAMA-DUPLO** — a direção Evidência↔Biblioteca segue com representações múltiplas na V2.2; qualquer redação final sobre "claim alimenta Evidências/Bibliografia" deve respeitar a prosa (regra vigente: prosa prevalece sobre desenhos).

## 5. Ajustes que a bancada submete à sua parte da deliberação (todos medidos; nenhum pede reescrever contrato)

1. **Precisão `entidades`:** o §2.3 da proposta atribui a N2 "entidades oficiais" — **medido: N2 v1.4 não tem campo `entidades`**; entidades vivem no L-NT (Parte 2, `entidades[]`). Sugestão de redação da resposta formal: "N2 liga evidência ↔ claim; as entidades são resolvidas na NT/grafo a partir do claim e das unidades".
2. **Herança `uso`:** ajuste de linha (pergunta do §2 acima).
3. **Ressalvados:** medido — dos 22 claims aprovados do kit, **14 são `aprovado_com_ressalva` (63,6%)**. O §13.13 da proposta (procedimento para ressalvados) terá massa real; o campo `nota_ressalva` do kit já existe e deve ser preservado na materialização (sugestão da bancada: N2 carrega a nota; decisão sua + do Auditor de Estrutura).
4. **Rodapés com comando literal:** pedido já feito na rodada 30 e agora redundante — o materializador, quando especificado, nascerá com essa regra (a bancada oferece os invariantes medidos do parser: ver §6).

## 6. Substrato medido do kit para o formato de entrada (§10 da proposta) — oferta da bancada

Medido hoje contra os bytes ancorados do kit (22 blocos, fatia `claims_aprovados`, todos os comandos na trilha 50):

| Campo N1/N2 | Semente no kit | Situação medida |
|---|---|---|
| claim_id | claim_id do bloco | DIRETO (N2.claim_id é string livre; a description do auditor já cita `B{n}.SM{nn}.{nnn}` — teste sintético com `B1.SM02.014` passa) |
| uso | uso do bloco | DIRETO (enum superset) |
| trilha | uso do bloco | DERIVÁVEL: todo kit ⇒ `clinica` (prova 3 casos) |
| pmid_oficial / refs | fontes[].pmid | 49 PMIDs únicos · **10 já na Bibliografia** (dedupe por `pmid_oficial` — regra medida) · **39 novos candidatos a N1** |
| natureza_evidencia | evidence_role | 22/22 `human_clinical` — **sem valor direto no enum N1**; mapeamento passa pela taxonomia de desenho HOJE aberta (os 2 ERRO vivos do P-8) |
| desenho_estudo(_bruto) / status_validacao | — | preenchimento posterior (leitura + taxonomia) |
| status_auditoria / verification_status | status / verification | mapeáveis por decisão dos auditores (2+1 valores de origem); se 'verificado', lembrar: N2 exige `g3_verificado_por` (allOf[0]) — o kit traz autoria multi-IA |
| **trecho_ancora / ancoras / ancora_principal** | — | **SEM SEMENTE (medido: 0 chaves-âncora no kit)** — requer leitura dos artigos; é a maior fortuna-zero do materializador |
| moderadores.regra_motor | presente | bônus: já em linguagem de motor (rev.20) |
| usado_em_biblioteca | 22× "nao" | o fio projetado e nunca executado (rev.28/29) vira realidade com esta proposta |

Invariantes do parser do kit (para o derivador; documentados desde a rev.29, re-medidos hoje): `Claim_id` maiúsculo + indentação TAB no .015 · sufixos b/c/d (.001b…013b) · `uso:` sempre ancorar (`23 = 22 + 1 espúria`) · PMIDs só na fatia `claims_aprovados`.

## 7. Questão transversal (§8/§12 da proposta) — medição entregue, decisão sua + do operador

Catálogo oficial medido: **146 = 48 (D1–D6) + 71 (C1–C13) + 16 (mecanismos) + 11 (cenários)**; chave `contagem` consistente. Da lista de domínios da proposta: mecanismos ✔, cenários ✔, suplementos ≈ família D ✔, exames ≈ família C ✔, fitoterapia ✔ (D3), sono ✔ (C9) — **"exercício" e "intervenção" não têm grupo próprio medido no catálogo de hoje**. A expansão transversal é viável em estrutura (ids do L-05 são genéricos — trilha E5), mas exige decidir representação (grupos novos × ids duais) no catálogo.

A bancada recomenda aceitar a proposta **como formalização do eixo B1-piloto primeiro** (§7/§12 dela) e deixar a transversalidade como decisão posterior com base nesse resultado — é também o que a própria proposta sugere.

## 8. Recomendação da bancada e pergunta formal

A bancada **não detectou conflito arquitetural em nenhuma camada medida** e recomenda **B — concordância com ajustes**, com os ajustes nomeados nos §§2, 5 e 6 (precisão `entidades`; linha de herança `uso`; ressalvados; formato de entrada com o mapa de fortuna acima; transversalidade adiada ao pós-piloto). A decisão formal é sua e do Auditor de Estrutura, depois do operador homologar.

Fila sua inalterada por esta rodada: 20 unidades-piloto NT-B1 (aceite: revisor cego · ≥90% · 3 testes) · minuta 2 do L-06 (errata `condicao` 0/274 · `extrapolado` 62/274 · piloto C1q Luo×Yao).

**0 ciência nesta rodada** (selos do §3.2 conferidos no início e no fim). Trilha 50 com 52 checks reexecutáveis em `atuais/producao/TRILHA50_*`; confissões da bancada desta sessão: 6, todas datadas, nenhuma afeta a ciência (réguas de contagem C0–C5b; ver JSON da trilha).

— A casa (bancada de verificação)
