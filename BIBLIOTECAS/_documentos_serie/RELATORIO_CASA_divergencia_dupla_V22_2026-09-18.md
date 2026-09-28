# RELATÓRIO DA CASA — Divergência documental: os dois artefatos rotulados "V2.2"
**Rodada 33 · 2026-09-18 · Trilha 52 (22/22 VERDE, reexecutável) · decisoes rev.40**

Operador, a casa mediu a divergência de ponta a ponta. Resposta curta: **os dois artefatos existem de fato, e a origem do diverso está identificada por conteúdo; a `df7f7cfd…` é a vigente correta; o arquivo do projeto do mestre é um elo ANTERIOR (o upload da rodada 24, pré-achado) com o rótulo "V2.2" — e a sua Minuta 1 não precisa mudar, porque ela já cita o sha certo.**

---

## 0. Inventário de bytes (medido)

| Artefato (rotulado) | sha256 | Bytes | H1 interno | Seções `# N.` | `origem_conhecimento` | prevalência prosa | "fora do cânone" |
|---|---|---|---|---|---|---|---|
| V½ (upload 15.09) | `8f050469…` | 37.466 | ARQUITETURA … | 23 | 0 | 0 | 0 |
| V2-15.09 (rodadas 9–24) | `09692e18…` | 46.129 | … V2 15.09.26 | 30 únicas | 0 | 0 | 0 |
| **upload rodada 24** (o seu upload de 17/09) | `5be36836…` | 50.964 | … V2 15.09.26 | 31 (**§21 duplicada**) | 0 | 0 | 0 |
| V2.1 instalada (17.09) | `1a50645e…` | 51.324 | … V2 15.09.26 | 31 (**§2 duplicada**) | 0 | 0 | 0 |
| **V2.2 INSTALADA (17.09 · vigente)** | **`df7f7cfd…`** | 52.181 | **… V2.2 17.09.26** | **30 únicas** | **3** | **1** | **1** |
| **"V2.2" do projeto do mestre** | **`309aa65f…`** | **arquivo ausente do workspace** (varredura global: 0 arquivos com esse sha) | — | (relato dele: só §§2/21 ≠ V2.1; 28 idênticas) | **0 (relato)** | 0 | 0 |

**As três marcas que o mestre NÃO encontra no arquivo dele existem SOMENTE na `df7f7cfd…`** — e existem porque o pedido delas veio dele: foram instaladas na correção do §2 a partir do **ACHADO do próprio Auditor-Mestre** (`ACHADO_V21_NO_UNIFICADO_2026-09-17.md`, sha `2841bc66…`, arquivado) com parecer concorrente do comentador. Linhas âncoras na vigente: **L4** (Rev. V2.2) · **L117** ("fora do cânone", bloco da Pasta) · **L121** (desenho `origem_conhecimento =`) · **L172** (prosa `origem_conhecimento = canonico | atualizacao`) · **L175** ("a prosa deste documento prevalece sobre os desenhos").

## 1. A assinatura do relato bate exata (identificação por conteúdo)

Comparação por seções (fatias `# N.` sobre os bytes, mesma régua das trilhas 45/45b):

- **upload rodada 24 × V2.1 instalada:** **28 seções idênticas; DIFEREM exatamente §2 e §21** — e §§6, 7, 13, 14 estão entre as 28, **byte a byte**.
- **V2.1 × V2.2 instalada:** 29 idênticas; difere **somente §2**.
- **upload r24 × V2.2 instalada:** 28 idênticas; difere **§2 e §21**.

O relato do mestre ("a V2.2 do projeto dela difere da V2.1 em §§2 e §21; 28 idênticas; §§6/7/13/14 byte a byte") é **exatamente a assinatura do upload da rodada 24 comparado à V2.1 instalada**. Conclusão documental: **o arquivo no projeto dele é, em conteúdo, o upload da rodada 24 (rotulado internamente "V2 … 15.09.26", com §21 duplicada, sem as três guardas) ao qual, em algum ponto da cadeia de repasse, se atribuiu o rótulo "V2.2"** — sem nunca ter recebido as correções da V2.1 (deduplicação) nem o achado da V2.2 instalada. Como o sha dele (`309aa65f…`) difere do upload (`5be36836…`), há uma diferença residual de bytes (cabeçalho editado e/ou newlines) que **só se confirma quando você nos enviar o arquivo** — pedido obrigatório abaixo. Seja como for, não muda a conclusão de conteúdo nem a recomendação.

## 2. Respostas (a)–(d), medidas

**(a) `df7f7cfd…` é versão posterior/editada?** **SIM — posterior, editada e INSTALADA sob decisão registrada:** rodada 26 (2026-09-17), opção A escolhida por você, a partir do achado do mestre sobre a V2.1 ("nó EVIDÊNCIAS / VÍNCULOS UNIFICADOS tornava a D-06 inimplementável" — correção de segurança). Não é uma edição espúria nem paralela: é a instalação oficial, com ponteiro, backup e trilha.

**(b) Quais alterações ela introduz?** Medido por seções e por bytes: em relação ao upload da rodada 24 (≈ conteúdo do arquivo do mestre), a `df7f7cfd…` muda **somente §2 e §21**: remove o nó "EVIDÊNCIAS / VÍNCULOS UNIFICADOS" e segrega os fluxos canônico × atualização até o Motor (alinhado ao §19); cria o bloco próprio da **Pasta de Atualização** com consulta ativa direta ao Motor e o rótulo **"fora do cânone"**; endurece a proveniência com **`origem_conhecimento` = canonico | atualizacao** (desenho + prosa normativa); crava a regra **"prosa prevalece sobre desenhos"**; corrige o H1 para **V2.2 – 17.09.26**; elimina a duplicata `# 2.`/`# 21.` restando **30 seções numeradas únicas**; preserva CRLF; e mantém **byte a byte idêntico o sufixo §3→fim** (39.165 bytes re-verificados hoje: §§5–30, catálogo 146, §§18/19/20 intactos). **Tudo que há na "V2.2" do mestre está contido na `df7f7cfd…` — exceto o defeito que o achado removeu.**

**(c) Qual deve vigorar?** **`df7f7cfd…`** — por três razões medidas: (i) é a única com as três guardas exigidas **pelo próprio achado do mestre** — deixar a `309aa65f…` vigorar seria reverter uma correção de segurança arquitetural; (ii) o conteúdo normativo que o L-NT usa (§§6, 7, 13, 14) é **byte a byte idêntico nos dois lados** — ou seja, a afirmação do mestre de que "o arquivo do projeto dele é suficiente para a Minuta 1" está **CORRETA quanto a conteúdo**, mas é o rótulo (e a cadeia documental) que está errado; (iii) só a `df7f7cfd…` tem rastreabilidade completa (instalada por decisão, com trilha reexecutável 18/18 + pós-instalação 10/10, ponteiro e SUPERSEDED em cadeia).

**(d) Onde está documentado?** `decisoes_B1.md` **rev.33** (rodada 26, instalação detalhada) · **ARQUITETURA_VIGENTE.txt** (ponteiro: escopo cirúrgico provado + cadeia SUPERSEDED V2.1→V2→V1) · **trilhas 45 e 45b** em `atuais/producao/` (reexecutáveis) · **ACHADO `2841bc66…`** arquivado verbatim · **RESPOSTA_14** (carta de instalação da V2.2) + **ADENDO_2_RESPOSTA_13** (anúncio da V2.1) · CHANGELOG rodadas 24–26.

## 3. O que precisa acontecer (sem tocar o L-NT)

1. **A Minuta 1 NÃO muda:** seu cabeçalho **já cita `df7f7cfd…`** (verificado hoje) e não cita `309aa65f…`. O pedido do mestre de "corrigir a referência de sha para `309aa65f…`" deve ser **invertido**: não se retifica a citação — **troca-se o arquivo no projeto dele**.
2. **Repasse dos bytes (o passo que fecha a identidade):** envie ao projeto do mestre o arquivo vigente da casa: `ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md` (**52.181 bytes · CRLF · sha `df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1`**). Mestre substitui e re-verifica o sha — aí `309aa65f…` morre documentalmente e a Minuta segue citando o mesmo sha de sempre. **Dívida nova nomeada: D-V22-BYTES-PROJETO** (os bytes da vigente seguem não confirmados no projeto dele — esta divergência é a prova).
3. **A casa precisa do arquivo do mestre:** envie o `ARQUITETURA_CONSOLIDADA_DA_PLATAFORMA_V2__-__15_09_26.md` (`309aa65f…`) → arquivo verbatim na cadeia (rótulo: **"V2.2 declarada — conteúdo = upload rodada 24, pré-achado — nunca vigorou"**), executo o diff byte-a-byte final (residual de cabeçalho/newlines) e confirmo de onde exatamente ele derivou.
4. Nota para o mestre, com ética de crédito: **o relato dele está correto e foi decisivo** — a comparação dele (28 idênticas · §§2/21) é a assinatura exata do upload r24; a conclusão de que "para o L-NT o conteúdo não muda" é endossada pela casa com prova byte-a-byte (C4 da trilha 52). O que muda é só a identidade do documento — e o motivo das três marcas que ele sentiu falta é que elas nasceram do achado dele, instalado depois do arquivo que ele tem.

**0 ciência nesta rodada:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos (274) `490675e6…` · P-8 `be48a5ef…` intactos. Trilha 52 em `atuais/producao/TRILHA52_*` (22 checks reexecutáveis).
— A casa (bancada de verificação)
