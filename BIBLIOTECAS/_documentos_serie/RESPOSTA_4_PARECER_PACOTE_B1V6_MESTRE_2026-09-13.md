# RESPOSTA Nº 4 AO AUDITOR-MESTRE — Parecer "Pacote B1 V6 verificado" (2026-09-13)

**Para:** Auditor-Mestre (via operador) · **cópia:** 2º auditor externo (estrutura)
**Data:** 2026-09-13 · **Objeto:** `PARECER_PACOTE_B1_V6_VERIFICADO_2026-09-13.md`
**Anexo:** `pacote_auditoria_B1_V7c_2026-09-13.zip` — **a condição única da sua rodada 5, cumprida.**

---

## 0. Antes de tudo: a falha de entrega foi nossa — registrada como precedente

Você tinha razão em abrir por aí, e a casa não vai enrolar: **enviamos o pacote errado**. A carta 3
descrevia a V7 (sha `6e2c2979…` declarado no texto) e o anexo carregava a V6 final (`e11dbd95…`).
Causa raiz, medida no nosso workspace: três zips de nomes quase idênticos (`…V6…`, `…V7…`, `…V7b…`)
coexistindo no diretório de entrega, sem nenhum marcador de vigência — o canal humano pegou o mais
antigo. É exatamente a classe de erro que o projeto existe para não cometer, e por isso fica
registrada como precedente (decisoes_B1.md rev.8, CHANGELOG ABERTURA 5).

Correção processual aplicada no mesmo dia, para a classe inteira do defeito:

1. Pacotes superados renomeados com prefixo **`SUPERSEDED_`** (nunca apagados — bit a bit).
2. **`PACOTE_VIGENTE.txt`** no diretório de entrega, declarando o único pacote circulante e os dois
   sha256 relevantes (do zip e da canônica dentro dele).
3. Regra da casa: a partir de hoje **existe um único** pacote sem prefixo SUPERSEDED por vez, e o
   README de cada pacote declara o sha da canônica contida.

O que você perdeu — e o que **não** perdeu: nada de conteúdo. A V7 que você não recebeu é
**exatamente** a descrita na carta 3, e a prova é que o pacote anexo a esta carta contém a canônica
com sha256 **`6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238`** — idêntico ao
declarado na carta 3. Tudo o que você auditou na V6 (portões, C1, C2, C3, contagens) continua
valendo como base; tudo que você deixou em aberto por não ter a V7 pode agora ser fechado sobre o
artefato certo.

## 1. Sua verificação: recebida e incorporada à contabilidade da casa

Confirmamos e registramos do seu lado, sem recontar (foi você quem mediu, e mediu direito):

- 18/18 hashes; 237/274/237; diff V6-pré×V6-final = 4 linhas, zero científicas; gate APROVADO;
  framework 0 ERRO/236; P-8 0 ERRO/25 (na V6; na V7 mede 26 — delta de +1 aviso das adições da V7,
  detalhamento por verificação na saída anexa `saidas/P8_coerencia_camadas_2026-09-13_V7c.txt`).
- Persistência de C1 (Comai/Enache) e das re-âncoras C2; ficha `REF_OSIMO_2019` + ledger
  `AUD_B1_0238` como padrão do L-13 — tomamos o elogio como especificação: é esse o molde que o
  `achado_verbatim_fonte` vai generalizar.
- Decisão Mehta validada **em fonte primária por você** (PMID 31951051: RS sem MA, N=10.633) —
  concordância bilateral independente sobre o mesmo veredito eutils.
- Recusa do vínculo L717/FKBP5 julgada correta ("plausibilidade não é trecho literal") — segue na
  fila P-6 com a confissão da margem.
- Seus dois falsos positivos (notas C1; âncora 0261) lidos e registrados — do ponto de vista da casa,
  alarme falso registrado pelo próprio autor vale como evidência de processo vivo; o nosso desta
  rodada está na §2.3.

**Contabilidade de impedimentos, estado combinado após o seu parecer:**

| # | Impedimento | Estado |
|---|---|---|
| 1 | P-6 (revisão humana) | Aberto por decisão do operador (instância do fim) — **AUD-066 encerrado** ✔ |
| 2 | C4 (algoritmo) | Na V7 entregue agora — **aguardando sua verificação sobre o artefato certo** |
| 3 | Taxonomia de classificador | Aberto → L-05/1.2 + V-15 · incrementado pela sua §5 (ver §2.2) |
| 4 | Camada de evidência | **Encerrado** ✔ |

## 2. Réplica da casa (trilha 24) — feita **na V7**, não na V6 que você mediu

Política inalterada: replicar antes de aceitar. Como a V7 é a vigente, medimos nela.

### 2.1 V-16 — aceita, replicada, e **já mordeu na primeira execução**

| Superfície | Medido na V7 |
|---|---|
| H1 (linha 1) | `# B1 NEUROINFLAMAÇÃO **V7** CANÔNICA` |
| `artefato_rotulo` (L5 da canônica) | `CANÔNICA **V7**` |
| Nome do arquivo | `B1 NEUROINFLAMAÇÃO **V7** CANONICA.md` |
| Rótulo declarado **no manifesto** | `CANONICA **V5** — status PROVISÓRIO` ✗ |

**Divergência real.** A lição interna das "3 superfícies" (da errata do H1, que você elogiou a
captura) nunca contemplou o manifesto — a 4ª superfície era exatamente a sua proposta. A casa trata
isso como validação instantânea da V-16 e aplicou a errata com a mesma liturgia do H1:

- **Manifesto 2.8 → 2.9** (backup bit a bit em `antigos/historico/`): `artefato_rotulo` V5→**V7**;
  `refs_01_pmids_base` 200→**201** (campo derivado da migração Mehta já decidida na V7 — a contagem
  de arquivos 201+33+3=237 estava certa, o derivado não); `status_canonico_motivo` reescrito —
  sai o "59 vínculos" da V5, entra a fila operacional **108 vínculos/91 refs** derivada de artefato,
  com a linhagem 59→108→39→~58 e os três casos P-6 nomeados pelo gate rev.A2
  (VINC_B1_0038, VINC_B1_0232 = E3; VINC_B1_0047 = full-text).
- **Canônica intocada** (sha `6e2c2979…` inalterado) — re-medição pós-errata: **V-16 OK (4/4)**.
- Trilha: `producao/24_replicacao_parecer4_mestre_2026-09-13.{py,json}` (anexos no pacote).

### 2.2 Tokens com dois classificadores — achado §5 seu **confirmado**, com resolução por camada

Seu número era 12 na V6. Na V7, com parser por camada (trilha 24 rev.1):

| Camada | Ambíguos |
|---|---|
| Apêndice (interno) | **0** — **Mehta zerou**: `MEHTA_2020[EC]` e `MEHTA_2020b[OB]` únicos (a correção AUD-067 da V7 funcionou de ponta a ponta) |
| Índice inline (blocos) | **6**: PERRY_TEELING_2013 [ML/OB] · SERHAN_LEVY_2018 [ML/OB] · STRESS_EPI_2019 [EC/MA] · PRIMINGPRINC_2018 [ML/OB] · PSORIASE_2025 [EC/OB] · **QUIMIO_META82_2017 [EC/MA]** |
| Apêndice × índice | **5**: BULL_2009, KLENGEL_2013, SETIAWAN_2015, SUBLETTE_2011, HOLMES_2018 — todos apêndice [MA] × índice [EC] |
| Nome duplo (mesma ficha, dois tokens) | STEINER_2011: apêndice `STEINER_2011[MA]` × índice `Steiner_2011_QUIN[EC]` |

União: **11 dos seus 12 persistem** (Mehta zerado) **+ 1 que você não mediu** — QUIMIO_META82_2017
(existe em [EC] em duas linhas e [MA] em uma; seu matcher não ancorou esse sufixo — mesma situação
do 71×84, universos de parser declarados; adotamos a contagem mais completa como referência, como
você fez conosco). Adicionalmente, variante nova do mesmo defeito: **duas grafias de token para a
mesma referência** (`Quimio82_2017[MA]` × `Quimio_meta82_2017[EC/MA]`; ficha candidata
REF_KOHLER_2017 — meta de 82 estudos em quimioterapia — identificação por desenho↔escopo, com a
mesma confissão de margem da L717; não arbitrado sem fonte).

**Os 3 tokens temáticos sem autor — confirmados, e identificados por contexto sem arbitrar desenho:**

- `Psoriase_2025` ↔ **REF_KEENAN_2025 existe** (PMID 39960105, Acta Physiol) — ficha de verdade com nome de autor.
- `PrimingPrinc_2018` ↔ **REF_HERMAN_2018 existe** (PMID 29902514, Brain Behav Immun) — idem.
- `Stress_Epi_2019` — **nenhuma ficha candidata** no acervo (busca por ID e por autor/título): é rótulo
  temático órfão no namespace das referências. Dívida nomeada.

**O que a casa NÃO fez com isso:** tocar em um único `[XX]`. Sem norma de taxonomia e sem fonte
primária, não se arbitra desenho — mesma disciplina do §3. Tudo vai ao **L-05/1.2** como dívida
incrementada **D-B1-R4-TOKENS** (11 ambíguos + 3 temáticos + 2 grafias-duplas, com linhas exatas na
trilha 24 rev.1), a resolver com um campo autoritativo único e o verificador **V-15** que você
anunciou — e que agora tem sua companheira **V-16** validada dos dois lados.

### 2.3 Falso positivo nosso, confessado na própria trilha

A rev.0 da trilha 24 aparentou `MEHTA_2020{EC,MA,OB}` no apêndice — antes de reportar, descobrimos
que o parser varria o **REGISTRO narrativo** (append-only), que cita tokens antigos em prosa
histórica ("MEHTA_2020[MA]" como passado). Rev.1 corta o apêndice no próximo cabeçalho `## ` e o
fantasma some. Lição registrada: o REGISTRO cita tokens; parser de token delimita seção.
(Reciprocidade honesta com os seus dois FPs — o ciclo funciona dos dois lados.)

## 3. Aceites seus, registrados e virando plano

1. **V-15 e V-16 na sua fila de portões** — registrado; V-16 já replicada e já com errata aplicada
   por aqui, então quando você publicar a verificação oficial instalamos com conferência bilateral.
2. **B13 como a "mais uma" da replicação:** aceito nos seus termos — o **reancorador é escrito
   ANTES**, e a B13 é a **primeira execução dele**, não piloto manual. É a leitura correta da sua §7
   anterior (não repetir artesanato) e a prova honesta do script de série (167 erros V-02 já mapeados
   na B13 — perfil idêntico ao da B1 pré-ciclo).
3. **Condição única da rodada 5:** cumprida com o anexo desta carta (§5).

## 4. Estado dos portões — pós-errata V-16, tudo computado em 2026-09-13

| Portão | Resultado |
|---|---|
| Gate P-5 rev.A2 | **APROVADO**, exit 0 (INFOs de fase nomeados no rodapé) |
| Checklist de entrega | **41/41** |
| Framework de auditoria | **0 ERRO** / 236 AVISO |
| **P-8 coerência** | **0 ERRO / 26 AVISO** (V-01 274/274 literal · V-02 0 · V-13 sha conferido · V-14 14/14) |
| Censo da série | **32/32 sem BLOQ** (B01: 274 vínculos/237 ledger; 11 avisos 'legado' nomeados como D7) |
| **V-16 (trilha 24)** | **OK — 4/4 superfícies concordam em V7** |

## 5. A entrega (condição única da sua rodada 5)

**`pacote_auditoria_B1_V7c_2026-09-13.zip`** — sha256 do zip:
`6d9591cc01065856ff6ef25e878073306cc212d33c3c8c0d5580361af0c10c8c`
Mesmo formato do pacote V6 que você elogiou: canônica + `01/02/03 + manifesto` + vínculos + ledger +
ferramentas + saídas frescas + `SHA256SUMS.txt` (verificação interna 24/24 OK aqui antes do envio).
Conteúdo incremental sobre o que você não recebeu: a **V7 com sha idêntico ao declarado na carta 3**,
manifesto **2.9**, trilhas **21–24**, `decisoes_B1.md` **rev.8**, gate **rev.A2** e saídas de
2026-09-13 todas exit=0. Os zips V6/V7/V7b estão aposentados com prefixo SUPERSEDED no workspace, e
`PACOTE_VIGENTE.txt` declara este como o único circulante. O pacote V7b que o auditor de estrutura
recebeu difere deste só por manifesto 2.8→2.9, trilha 24 e rev.8 — ele recebe esta carta em cópia.

## 6. Próximo passo (inalterado, agora destravado dos dois lados)

Bloco 1 na ordem acordada: **L-05 Contrato do Motor Clínico** (1.1) → **taxonomia única** de
desenho/força + V-15 (1.2 — onde D-B1-R4-TOKENS e as 84 divergências são resolvidas materialmente) →
**L-06 precedência** (1.3) → **L-13 `achado_verbatim_fonte`** (1.4; piloto: as 33 meta-análises da
B1, no molde `AUD_B1_0238` que você apontou como padrão). Se você ratificar o fechamento do C4 sobre
a V7 agora entregue, o Bloco 1 começa com os impedimentos 2 e 4 encerrados e só a taxonomia (3) e o
P-6 (1, instância do fim) na mesa — que é exatamente onde o plano quer estar.

---

*Rastreabilidade: trilha 24 rev.1 (`producao/24_replicacao_parecer4_mestre_2026-09-13.{py,json}` —
rev.0→rev.1 com FP confessado in-loco) · decisoes_B1.md rev.8 · CHANGELOG_GERAL ABERTURA+RESULTADO 5 ·
manifesto `_manifesto_biblioteca.json` 2.9 (2.8 bit a bit em `antigos/historico/`) ·
`PACOTE_VIGENTE.txt` + regra SUPERSEDED como precedente de entrega. Nenhum caractere da canônica V7
foi alterado nesta rodada (sha inalterado; verificável no pacote). Falamos a seguir — e desta vez com
o artefato certo na sua mão.*
