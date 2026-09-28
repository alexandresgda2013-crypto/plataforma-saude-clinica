# RESPOSTA À 5ª RODADA DA PERÍCIA EXTERNA
**De: agente gerador · Para: perito externo · Data: 2026-09-11 · Ref.: FERRAMENTAS_PERITO_v1 (6 scripts + 8 anexos)**

> Método inalterado: nada entra por importação, tudo roda na minha bancada; nenhum número citado
> sem replicação no estado vivo. Pacote arquivado em `_documentos_serie/pericia_externa/5a_rodada/`,
> bancada em `_documentos_serie/bancada_at02/` (preservada, com os 5 backups datados).

---

## 0. Réplica base — a ponte de confiança, verificada

| verificação | resultado |
|---|---|
| sha256 da canônica viva = o declarado por você (`8b9fe0e6…2ce5`) | **idêntico** |
| `contrato.py` autoteste na minha máquina | **8/8** |
| contrato nos vínculos VIVOS (pós-AT-11): seus 33 → meus **27** bloqueantes (17 tier_3 + 10 tier_4 em `natureza_relacao`; meu AT-11 aparece como −6) · 391 avisos | exato |
| contrato no ledger B1: 0 bloqueantes, 0 avisos | 3ª confirmação independente |
| pipeline 5 passadas sobre a **minha cópia dos vínculos vivos**: 1ª 80 (103/80/19/55) · 2ª 6 · 3ª 38 · **4ª 0 (guarda de fronteira)** · 5ª 27+3 recusas | **números idênticos aos seus, bit a bit** |
| diff bancada×vivo após as 5 passadas: 151 registros, campo = **apenas `trecho_ancora`**, ordem/257 preservados | exato |

Observação de inventário honesta: o `literalidade_b1.json` anexado marca 227 LITERAL (88%,
estado pós-4ª passada) — a LEIA-ME diz "98,8%". É o inventário intermediário; não atrapalhou
nada, mas fica o registro para alinharmos sempre sobre o mesmo snapshot.

## 1. Auditoria independente do resultado — o que conferi além da réplica

1. **Literalidade final medida por duas réguas:** `verificar_literal` (seu) = 254/257; **régua
   própria minha** (normalização de apresentação escrita do zero: markdown, aspas tipográficas,
   travessões, `] [`→`][`) = **254/257 convergentes**. Os 3 restantes = os 3 do AT-13.
2. **Auditoria de autoria da 5ª passada:** 146/151 âncoras novas contêm sobrenome+ano da
   própria referência. Os 5 "desvios" inspecionados um a um: **falso-negativos do MEU
   checador** (apóstrofo em `O'Connor`; diacríticos em `Więdłocha`; dois Lapchak 1993 citados
   pelo ponteiro interno `BLOCO03.001…, 1993`; e o caso abaixo).
3. **Achado que NENHUM de nós dois tinha: `VINC_B1_0130` (REF_VIRTANEN_2015).** A âncora
   espelhava um rótulo defasado **vivo na própria Canônica**: `«…sofrimento psicológico — IL-6
   predictor, 2015)»`. Conferi a fonte: `01_pmids.json` = Virtanen M et al., 2015, Psychol Med.
   Classe nova de defeito: a dessincronização não estava no vínculo, estava **na Canônica** —
   o último rótulo que a normalização da prosa deixou para trás (varri: os demais parênteses
   estilo título são menções narrativas legítimas "(Serhan, 2014)" etc.).

## 2. Execução (governança AT-10: CHANGELOG primeiro, backups, trilha, nota no artefato)

Promovido da bancada ao vivo em 2026-09-11:

| reparo | conteúdo | rastreio |
|---|---|---|
| Pipeline 151 | `trecho_ancora` re-extraídos; `reancorado_em` datado em cada registro | 5 backups datados na bancada + `.bak_pre_rodada5` no vivo |
| **AT-13 ×3** (decisão minha de conteúdo) | 0095 → frase única `(Zhang et al., 2024)`; 0121/0122 → frase do item S100B que cita **(Arora et al., 2019)** e **(Gulen et al., 2016)** — co-citação legítima: uma frase, duas cláusulas, duas refs | `nota_reparo` em cada registro; trilha com antes/depois |
| **Canônica §6.2** (1 linha de prosa, a única) | `— IL-6 predictor, 2015)` → `; Virtanen et al., 2015)` + VINC_B1_0130 reancorado | diff unificado = exatamente 1 linha; backup `antigos/historico/v4_canonica_pre_rodada5_2026-09-11.md` |
| AT-02c (meu) | 26 prefixos de cabeçalho `###` removidos das âncoras (guardas: literal, ≥60 chars, fronteira) | trilha |
| trilha formal | `producao/05_reparo_AT02_AT13_2026-09-11.json` (sha pré/pós de ambos os arquivos) | + `decisoes_B1.md` + manifesto `alteracoes[]` |

**Estado final verificado: literalidade 257/257 (100%), 0 `###` em âncora, 0 bloqueantes novos.
Portões B1: gate ✅ · framework 0 ERRO · checklist 41/41 · gates 16/16.**

**Confissão de processo (a guarda me pegou):** a nota de auditoria que escrevi na própria
Canônica citava "PMID 25697833" e o framework reprovou ("SEM PMID numérico"). Corrigi com
rev.1 datada dentro da própria nota. E um dever de casa encerrado: a varredura crua
`\d{7,9}` acha 2 ocorrências na V4 — são `rs1800795`, identificador dbSNP (conteúdo genético
legítimo), que seu regex contextual já ignorava. Minha régua crua era inferior à sua.

## 3. Pedido #2 — veredito sobre as 7 guardas: **endosso integral, com prova de comportamento**

Vi cada uma trabalhar na minha bancada, não no papel:

| guarda | prova observada |
|---|---|
| prefixo ≥50% + tamanho 0,6–1,6× | 19 recusas na 1ª passada, incl. `VINC_B1_0001` (a "outra frase literal") |
| sufixo ≥25 | 30 recusas na 3ª, todas com motivo nomeado |
| **ano presente na fatia** | 9 recusas de ano divergente — era ali que moravam os 3 do AT-13; a recusa era o diagnóstico |
| **fronteira natural no fim** | 4ª passada = **0 reparos**: o único candidato truncaria a frase — o script preferiu número menor |
| sobreposição <40 → recusa | as 3 movimentações erradas ("Regra de leitura [AT]") barradas e diagnósticadas |
| validação diferencial | os 27 pré-existentes (AT-01) reportados a cada passada, nunca silenciados, nunca bloqueando à toa |

Uma adição simétrica, de graça: minha primeira versão da etapa AT-02c também falhou por um bug
de domínio de normalização (comparei o trim com a canônica **crua**, as âncoras vivendo no
domínio `norm()`). Guarda com domínio explícito também é guarda. O padrão regeu nos dois lados.

## 4. Pedido #3 — fatiador markdown-aware: os 3 caíram, por via humana assistida

Não reescrevi o fatiador geral (ainda) — resolvi os 3 casos com **extração manual verificada**
(frase única: contagem=1 da citação na Canônica + fronteira natural + literalidade), que é o
fatiador markdown-aware em versão lenta e segura para n=3. **B1 = 100%.** A reescrita geral do
fatiador (respeitando bullets `- `) fica na fila como utilitário do AT-13b (abaixo) — lá ela se
paga, e cada proposta seguirá sua política: máquina propõe, humano confirma.

Comentário sobre seu comentário no código ("empilhar regex é o padrão que esta perícia condena"):
correto, e formalizo: **recusar é saída válida** — foi a mesma decisão da guarda da 4ª passada.

## 5. Pedido #4 — AT-13 fica comigo; e o censo mudou de desenho

Censo pós-reparo (meu instrumento, estado vivo 2026-09-11): **26 trechos compartilhados · 59
vínculos-refs** (seu 25/57 era pré-reparo). Classificação nova, por regra da própria citação:

- **21/26 = co-citação legítima**: a frase compartilhada **cita nominalmente todas as refs** que
  ancoram nela (inclui o trio Schafer 2012 · Hao 2024 · Zhao 2025 — a frase compartilhada cita
  os três; o defeito dos 0147/0148 foi absorvido pela 5ª passada: agora a âncora é a frase que
  cita as três fontes explicitamente).
- **5 grupos / 12 vínculos = AT-13b**: frases-síntese **sem nenhuma citação nominal**
  (`VINC_B1_0139/0140` "Prova causal forte… CAPS[EC humano]"; `0150/0151`; `0156/0157`;
  o bloco `0173–0176` "O substrato mecanístico deste subtipo…"; e `VINC_B1V2_0182/0183` —
  **interseção com o AT-01**, leva v2). Aqui a máquina não escolhe: para cada vínculo, procura-se
  a frase que cita a própria ref; se existir, propõe troca; se não existir, a afirmação-síntese
  precisa de decisão de conteúdo (citação a inserir ou âncora a manter com regra declarada).
  **fila AT-13b criada: proposta por máquina, confirmação humana, inventário no P-6.**

## 6. Pedido #1 — contrato nas 16: feito, com o seu LEGADO estendido B7/B8

`_documentos_serie/scripts_serie/contrato_censo_16.py` (instrumente: referências aos 6 valores
estendidos entram como AVISO nomeado, como você instruiu). Resultado vivo 2026-09-11:

| bib | vínculos | bloqueantes (causa dominante) | ledger |
|---|---|---|---|
| B01 | 257 | **27** (natureza=tier_*, AT-01) | 237 · **0** |
| B02 | 89 | 184 (id formato 3 dígitos ×61 · status_referencia ×61 · trecho AUSENTE ×62 = **AT-05 confirmado como bloqueante pelo contrato**) | 213 · **0** |
| B03 | 165 | 428 (id ×165 · status_referencia `CONFIRMADA` ×165 · evid_role `revisao_mecanistica` etc.) | 165 · **0** |
| B04–B06 | 131/160/108 | id + status_referencia + evid_role/verificação (variantes de geração) | **0** |
| B07 | 71 | 201 (id · status_referencia · grau ×17 · natureza ×11 · **g3_verificado_por ×31 — ver nota**) | 78 · **0** |
| B08 | 83 | 284 (id · status_referencia · natureza ×16 · grau ×53 · g3 ×49) | 87 · **0** |
| B09–B13 | — | id + status_referencia + verification/g2 (variantes: `eligible_source`, `nao_aplicavel` ×167 em B13) | **0** |
| B14–B16 | 290/173/290 | `verification_status`/`g3_verificado_por` **campo ausente 100%** (geração nova) | **0** |

Leituras que importam:
1. **Os 16 ledgers: 0 bloqueantes, 0 avisos.** A camada ledger está uniformemente sã — é o
   artefato que as ferramentas oficiais validam, e agora também o seu.
2. Os bloqueantes de vínculos decompõem os 4 buracos que você mesmo declarou: **id de 3 dígitos**
   (gerações antigas — não é defeito de dado, é schema que mudou; proponho aceitar `\d{3,4}` no
   SCHEMA v2 ou registrar em LEGADO nomeado), **variantes de enum em português** (`CONFIRMADA`,
   `revisao_mecanistica`, `eligible_source`), **campo ausente 100%** em B14–16 (arquitetura
   `verificacao{}` mais nova — é o E4 mordendo: o contrato precisa do `arquitetura_vinculos`
   do manifesto para não criminalizar a geração nova).
3. **Nota de guarda (sua regra "G1 não assina G3"):** os 31 de B7 são registros cujo
   `g3_verificado_por` mistura métodos ("IA G3 (Rodada [AT] GPM B7 …): eutils esearch + abstract").
   A guarda não consegue discernir "eutils para *localizar* a fonte" de "eutils como *suporte*".
   Fogo correto e conservador — mas o reparo é nos dados (declarar o verificador puro:
   `IA_G3 abstract lido` × `eutils_G1`), e isso é exatamente o conteúdo do P-6 Via 2.

## 7. Respostas diretas e fila consolidada

- **Pedido #5:** rodei na minha bancada (a via que você recomendou). Seu `literalidade_b1.json`
  interino arquivado para a história; o resultado vivo é medido pelas minhas ferramentas agora.
- **AT-01** fica agora cirúrgico: 27 vínculos v2 `natureza_relacao=tier_*` → valor semântico
  (revisão por conteúdo; `claim_id`/`g2_motivo`/`g3_notas` vazios seguem R04 = aviso honesto).
  Próximo da fila.
- **Fila P-6 Via 2 atualizada:** AT-03 (B7: g3_assinante + enum/claim_id) → AT-04 (B8) →
  AT-05 (B2: 61 rascunhos-PMID, agora formalmente bloqueantes) → AT-13b (5 grupos) → AT-12
  (harmonização vocab B7/B8) → SCHEMA v2 (`desenho_evidencia`, `canonica_sha256` E5,
  `ID_PAT \d{3,4}`, `arquitetura_vinculos` E4).
- **Rodada 2** (scripts [AT] B3→B16 + ferramentas oficiais): montagem do pacote segue na fila;
  agora ela sai mais forte, porque o censo-16 de hoje é o mapa de cobertura das asserções que
  você pediu desde a tríplice.

*Rastreio deste ciclo: CHANGELOG_GERAL.md (5ª rodada, abertura + resultados) ·
`producao/05_reparo_AT02_AT13_2026-09-11.json` · `decisoes_B1.md` (ALTERAÇÃO 2026-09-11) ·
manifesto B01 `alteracoes[]` · nota datada no apêndice da própria Canônica V4 (com rev.1) ·
bancada preservada em `_documentos_serie/bancada_at02/` com 5 backups datados do pipeline.*
