# ADENDO Nº 1 AO PARECER Nº 2 — Revisão da análise externa do L-05
## (comentário de terceiro revisor — "ChatGPT" — trazido pelo operador, 2026-09-14)

**De:** a casa · **Para:** operador (repasse livre a quem quiser) · **cópia:** auditor de estrutura, Auditor-Mestre
**Data:** 2026-09-14 · **Base:** análise colada pelo operador + trilha 26 (`producao/26_verificacao_analise_externa_L05_2026-09-14.json`)
**Regra aplicada:** a casa só concorda ou discorda depois de checar os fatos — inclusive (e sobretudo) quando o comentador concorda conosco.

---

## Veredito em uma frase

**A análise está ESSENCIALMENTE CERTA — e dois dos seus pontos são adotados formalmente pela casa (viram o ajuste R7 e o refinamento da D3). Um ponto seu é re-endosso, não correção; nenhuma posição sua conflita com o parecer que a casa já emitiu, e os dois documentos se complementam.**

## Ponto a ponto — certo, parcial, ou por quê

### 1. "O núcleo está correto" (evidência única × âncoras múltiplas; sem pastas por tipo)
**CERTO, com concordância independente.** É a mesma conclusão do parecer da casa nº 2 (§3.1–3.4, §4.1–4.3). Taxonomia no dado, não na árvore de pastas — a pasta congela um eixo; a meta-análise pré-clínica (McColgan 2026) é o caso-teste que ambos citamos. Sem ressalva.

### 2. Ponto 1 — não automatizar os 133 pré-clínicos (in vivo × in vitro)
**CERTO, e já era a posição da casa.** A própria proposta diz "← exige triagem"; a casa reforçou na D2 (triagem semiassistida por MeSH/pubtype + revisão por registro; *nunca classificar sem texto*). O freio que ele pede existe e está na mesma direção. Nada a opor.

### 3. Ponto 2 — "`principal` não deve significar posse; manter 'relações declaradas, não posse'"
**Substância CERTA, enquadramento impreciso: é re-endosso, não correção.** A proposta já diz literalmente (§3.2, regra 3): *"é a entidade em cuja biblioteca a evidência foi trabalhada. As demais são relações declaradas, **não posse**."* O comentador chega à mesma regra citando o próprio texto — portanto concorda com o desenho, em vez de corrigi-lo. **A casa adota mesmo assim o refinamento de documentação por ele inspirado:** a definição do campo `principal` ganhará a cláusula explícita *"marca o contexto de curadoria da evidência; não implica posse nem precedência epistêmica"*, para blindar a leitura futura (motor incluído). Custo zero, ganho real.

### 4. Ponto 3 — "`papel` pode ser lido como veredito; caso Raison 2013"
**O ponto mais valioso da análise — CERTO na crítica, e a casa transforma em ajuste formal (R7).**

- **Fatos da própria análise verificados:** `REF_RAISON_2013` (PMID 22945416, RCT JAMA Psychiatry, N=60) existe no acervo; a ficha registra exatamente o quadro que ele descreveu (amostra geral negativa; subgrupo com inflamação alta respondendo ao anti-TNF). A canônica usa o estudo como prova-condição do subtipo inflamatório. *Extra curioso:* no apêndice herdado, esse RCT aparece como `RAISON_2013[MA]` — mais uma amostra viva da dívida de taxonomia já nomeada (D-B1-R4-TOKENS); não se corrige aqui, mas ilustra o tema.
- **Onde a casa enxerga a proteção que a análise não viu:** o vínculo já carrega `trecho_ancora` literal + `natureza_relacao` + `forca_causal` + `grau_maturidade` + `verification_status`, e a referência tem `achado_central_molecular`. Ou seja, "o que a evidência sustenta, e com que força" **nunca** morou em `papel`. **Mas** o comentador tem razão no que importa: o *contrato* não proibia um motor ingênuo de ler `papel: sustenta_intervencao` como "eficaz". Lacuna de regra, não de dados.

**Ajuste R7 (adotado, com crédito explícito à análise externa):**
1. **Regra normativa:** `papel` declara a **relação temática** da evidência com a entidade — **nunca o veredito**. O veredito mora na quádrupla `trecho_ancora + natureza_relacao + forca_causal + verification_status`. Motor e leitor humano são proibidos de inferir eficácia/direção a partir de `papel` isolado.
2. **Eixo ortogonal opcional na âncora:** `direcao: sustenta | refuta | inconclusivo | condicional` (+ `condicao`: texto curto quando condicional). É o mesmo padrão dos eixos ortogonais consagrados no PROMPT v4.2 (L1438): não se mistura dois eixos num enum.
3. **Migração mínima de enum:** `refuta` sai de `papel` e vira `direcao: refuta` — o papel fica limpo e o sinal de refutação (exigência da Filosofia) fica no eixo próprio, mais forte do que estava.

Molde do caso Raison: âncora `suplemento_infliximabe` {papel: `sustenta_intervencao`, direcao: `condicional`, condicao: *"resposta restrita ao subgrupo inflamação alta; amostra geral negativa"*}; âncora `exame_pcr_us` {papel: `sustenta_biomarcador`, direcao: `sustenta`}. (IDs do exemplo conferidos no catálogo oficial: `exame_pcr_us` ✔, `exame_tnfalpha` ✔; suplementos e o rótulo semântico do cenário se fecham no recorte C-LAB, Bloco 3 — nada inventado.)

### 5. "Não é pasta de evidências clínicas — é acervo de evidências científicas auditadas"
**CERTO — adotado como nomenclatura.** O Módulo 09 é o acervo científico auditado; "camada clínica" passa a ser uma **leitura por filtro** (`natureza`/`desenho`), não um lugar. Sem custo, ganho conceitual.

### 6. D3 — "não consolidar com a B1 no modelo antigo enquanto B2 sai no novo"
**CERTO no risco — e a casa refina a sua própria resposta.** A casa havia dito "B1 antes de B2, começando pelos 20 redirecionados"; a análise externa torna explícito o risco de exceção arquitetural permanente. Faseamento revisado (corte de consolidação):
1. v1.1 do schema com **R1–R7** fechada;
2. validação *shadow* com **0 não-conformes** na B1;
3. retroancoragem da **B1 inteira como corte único** — os 20 redirecionados entram primeiro por conveniência operacional, mas **o corte só fecha com os 274**; 
4. só então B2.
O modelo **nunca** roda misto em produção. O que "começar pelos 20" significava — subetapa interna — ficou agora escrito direito.

### 7. Conclusão dele ("aprovar o princípio; manter PROPOSTA até revisão dos enums/papel")
**ALINHADO.** É exatamente o estado em que a casa deixou o tema: aprovado com ajustes, shadow antes de normativo. Com este adendo, os ajustes passam de R1–R6 para **R1–R7**.

## O que a análise externa não cobriu (e a casa já cobria) — sem demérito

R1 (invariante "1 principal" em portão imperativo) · R2 (`_ids_oficiais.json` inexistente como arquivo) · R3 (falso-positivo de substring no teste E2) · R4 (migração da âncora: 3 formatos de `secao_origem` + 12 `APENDICE_CORPUS`) · R5 (manual de classificação do desenho) · R6 (`citacao_confirmada` = default de geração, PROMPT v4.2). São pontos que exigiam as ferramentas da própria casa (portões, trilhas, acervo); os dois relatórios não se contradizem em nenhuma linha — **se complementam**.

## Efeito prático

- A lista de ajustes ao L-05 fica **R1–R7** (R7 com dois subitens: regra + eixo `direcao`; `refuta` migra de enum).
- A D3 fica na sua forma revisada (§6 acima) — a publicamos também ao auditor de estrutura, para a v1.1.
- Nada muda na canônica, nos dados ou nos portões (todos verdes); muda apenas o caminho do contrato — agora melhor.

---

*Rastreabilidade: trilha 26 (verificações factuais: ficha REF_RAISON_2013; tokens da canônica; catálogo de IDs; citação literal da regra 3.2) · este adendo é anexo do `RESPOSTA_2_AUDITOR_ESTRUTURA_L05_2026-09-14.md` · decisoes_B1.md rev.10 · CHANGELOG ABERTURA/RESULTADO 7.*
