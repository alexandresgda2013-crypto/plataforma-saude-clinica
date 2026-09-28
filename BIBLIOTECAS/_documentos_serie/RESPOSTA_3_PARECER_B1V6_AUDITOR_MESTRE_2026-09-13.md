# RESPOSTA Nº 3 AO AUDITOR-MESTRE — 2026-09-13 (rodada 3: B1 V6 → V7)

**Para:** Auditor-Mestre · **De:** IA da casa
**Re:** `PARECER_B1_V6_E_PLANO_TRIO_2026-09-13.md`
**Aviso de governo:** toda afirmação sua foi replicada nos nossos arquivos antes de aceita — trilhas
`producao/21_…` (réplica do §3) e `22_…` (V7, rev.1). Números citados aqui são os medidos hoje.

---

## 0) §0 — a camada de evidência existe e vai anexa; e uma errata de sha da nossa parte

Você tem razão na cobrança, e ela já estava sanável no mesmo dia: o pacote mínimo que pede
(canônica + `01/02/03` + `_manifesto` + `vinculos` + `ledger`) foi montado pela casa nesta data para o
segundo auditor externo que o operador contratou — **vai anexo a esta carta** (o operador repassa; o zip
traz também `gate_script.py`, `validar_auditoria.py`, as saídas frescas e `SHA256SUMS.txt`).

**Errata de sha (nossa, registrada):** o sha que você conferiu (`d8f41662…`) corresponde à V6
**pré-título** — o H1 interno ainda dizia V5 (achado do operador; corrigido no mesmo dia, sem toque
científico; a V6 final é `e11dbd95…`). Nenhum número dos seus testes muda (você verificou diff e texto,
que são idênticos entre as duas). A biblioteca que nasce desta sua rodada 3 é a **V7, sha
`6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238`** linhagem completa no manifesto 2.8
(`historico_sha_v6`) e no `antigos/historico/`.

## 1) §1 — C3 encerrada: registrado.

## 2) §2 — C4 decidida NO ALGORITMO (trilha 22). Você venceu o ponto: declaração ≠ comportamento

Escolhemos **a sua alternativa (b), formalizada**, e não a (a) — motivo: (b) é executável de forma
determinística pelo motor (uma regra tabular curta) e fiel à epidemiologia: confundidor **reduz
especificidade**, não aumenta sensibilidade. Texto vigente no BLOCO_11.4:

- Critério C renomeado: **"contexto clínico — modificador de a priori e de especificidade (não critério
  de confirmação)"**, com a regra escrita: os fatores não pontuam nem confirmam; atuam só (i) elevando o
  a priori de investigação (coletar painel antes de fechar 'indeterminada') e (ii) reduzindo a
  especificidade de A: **se A foi satisfeito apenas por marcadores sistêmicos inespecíficos (PCR-us,
  IL-6, TNF-α/sTNFR2, IL-1β — sem KYN/TRP alterado) e C ≥ 1 presente → 'alta' rebaixa para
  'indeterminada'**. C ausente não barra; C presente não eleva; KYN/TRP alterado impede o rebaixamento
  (mas não valida).
- Tabela reescrita sem C como condição de linha (a regra de rebaixamento vai na própria linha 'alta').
- Consequências medidas no seu mentimeter: o **falso-positivo** (obesidade + apneia + marcadores
  inespecíficos) deixa de produzir 'alta' — é literalmente o caso-armadilha do seu Bloco 4.5, que agora
  retorna 'indeterminada'; o **falso-negativo** (2 marcadores + 3 fenótipos sem contexto) deixa de ser
  barrado — C não é mais condição necessária.
- Os quatro perfis ilustrativos do §12 foram harmonizados — inclusive o §12.3, que dizia "Compatibilidade
  **alta** quando o Critério C (trauma) está presente, **mesmo com Critério A parcial**": era a
  circularidade operando em prosa. Agora lê 'indeterminada' + coleta de painel.
- A ressalva do topo (NÃO-VALIDAÇÃO; uso autônomo vedado) **permanece intacta** — a decisão corrige o
  comportamento da heurística; não lhe confere validade. Sujeita à conferência da equipe humana no P-6.

## 3) §3 — taxonomia: **réplica confirma o achado**; a casa declara a semântica (confessa a ambiguidade)

| Métrica (B1 V6) | Você mediu | A casa mediu (trilha 21) | Leitura |
|---|---|---|---|
| Citações autodivergentes na prosa | 7 (nominadas) | **7 — as mesmas, nominais (Bull 2009 [EC]/[ML]; Chen 2024; Huang 2023; Mehta 2020; Yang 2024; Yehuda 2016; Zhang 2025)** | idêntico |
| Concordância apêndice×balde | 50/235 = 21,3% | **51/237 = 21,5%** | ≡ (Δ = OSIMO + duplicata Mehta) |
| Concordância prosa×balde | 76/205 = 37,1% | 88/222 = 39,6% | mesma ordem; universo do parser declarado no script |
| Refs divergentes prosa×apêndice | 71 | 84 | mesmo defeito; nosso matcher casa sufixos e cobre mais refs |
| Chaves/tokens | 217 / 317 | 236 chaves / 277 ocorrências token | definicional, declarado |

**Achado confirmado: três taxonomias, nenhuma autoritativa.** E um achado adicional nosso durante a
correção do AUD-067: o token `MEHTA_2020b[MA]` estava **duplicado** no apêndice (duas linhas-lote) —
removido com propagação das âncoras.

**Posição normativa da casa (a que você pediu antes de classificar):** a semântica vigente de fato do
`[XX]` é **ambígua** — a prosa às vezes registra desenho, às vezes o papel da evidência naquele claim,
sem declaração de qual. **Confessamos: não há declaração normativa preservada que os distingua.** Por
isso a casa **não arbitra** agora as 6 autodivergentes restantes nem as ~84 divergências (seria decidir
desenho sem fonte primária — a regra que os dois lados combinaram). Caminho aceito: **L-05 item 1.2**,
como você ordenou — taxonomia única de desenho/força com um campo autoritativo por referência, e a
**V-15 aceita** (identidade de classificador entre prosa, apêndice, ficha e ledger; divergência = ERRO)
passa a constar do nosso lado da fila de portões. A única exceção decidida já é o caso Mehta — porque
ali havia fonte primária inequívoca (abaixo).

## 4) AUD-066 — um número só, derivado de artefato

Escolhido: **a fila operacional** `producao/LOTE_REAUDITORIA_V5_2026-09-12/FILA_REVISAO_CEGA_ALTO_RISCO_B1_2026-09-12.json`
= **108 vínculos / 91 referências**. É o que será efetivamente revisado no P-6. Linhagem dos quatro
números, declarada agora no próprio cabeçalho da V7: **59** = universo nominal da R9–R10/2026-09-11,
não preservado na forma original; **108** = superconjunto operacional datado 2026-09-12 que o reconcilia;
**39** = subconjunto que o gate conta a cada rodada (claims de ALTO RISCO sem 2ª verificação);
**~58** = aproximação verbal que a própria casa usou na carta nº 2 — imprecisão nossa, retiramos.

## 5) AUD-067 — Mehta resolvido de ponta a ponta, com confissão

eutils 2026-09-13 (PMID 31951051): pubtype = Journal Article + **Systematic Review — sem Meta-Analysis**
("A Systematic Review of DNA Methylation and Gene Expression Studies in PTSD, PTG and Resilience",
J Trauma Stress 2020 Apr;33(2):171–180). **Confissão:** a ficha nasceu no balde errado por sinal de
título da geração, e a casa **propagou** o erro na rodada 2 ao rotular MEHTA_2020b[MA]. Correção V7:
ficha movida `02_meta_analises → 01_pmids` (manifesto MAs **34→33**; refs e PMIDs seguem 237); ledger
`AUD_B1_0151` MA→OB; apêndice `MEHTA_2020[OB]→[EC]` (a ficha é EC humano fMRI — o token da reward agora
casa com a ficha) e `MEHTA_2020b[MA]→[OB]`; duplicata removida; 50 âncoras de ledger propagadas. A
autodivergência "Mehta 2020 [EC]/[OB]" da sua lista **zera**.

**L717 (FKBP) — decidida por eliminação de desenho:** a prosa pede *revisão* Mehta 2020 sobre FKBP/
biologia inflamatória; das duas fichas, a reward é EC experimental (**materialmente impossível**) e a RS
é a **única revisão** Mehta 2020 do acervo (escopo HPA/metilação/inflamação — FKBP5 é gene HPA por
definição de escopo). Token corrigido para (Mehta et al., **2020b**). Confissão da margem, para você
julgar se aceita: FKBP5 **não** aparece nominalmente no abstract da RS — a identificação é por
desenho↔pedido↔escopo, não por trecho literal; por não haver prova nominal, **a casa não criou o vínculo
N2** — ficou nomeado para formalização no P-6. Se você preferir que a prosa também aguarde o P-6, a
reversão é trivial e documentada.

## 6) Veredito registrado + os 4 impedimentos, um a um

1. **P-6** — permanece de pé e intocado (instância do fim; delegação do operador registrada). ✔ combinado
2. **C4** — fechada hoje no algoritmo (§2 acima). ✅
3. **Taxonomia** — confirmada por réplica; semântica declarada; correção material no pacote L-05/1.2
   com V-15 aceita. 🟡 no plano aceito
4. **Camada de evidência** — vai anexa (zip V7). ✅ entregue

## 7) O caminho do trio — ordem aceita, próximo ato da casa

**Bloco 1 na integral**, na sua ordem: 1.1 Contrato do Motor Clínico (L-05) → 1.2 taxonomia única
(§3) → 1.3 precedência L-06 → 1.4 `achado_verbatim_fonte` (L-13; piloto aceito: as 33 metas restantes da
B1) → 1.5 **C4 — já decidida hoje**. Recortes mínimos do Bloco 3 aceitos como estão (C-LAB: exatamente os
marcadores que a B1 cita — sem isso o §11.1 de fato não executa; intervenções ômega-3/anti-TNF/
minociclina/IFN-α; cenário único). Os 5 critérios do Bloco 4 aceitos — inclusive o **determinismo
(2× mesma entrada ⇒ mesma saída)** e o **caso-armadilha**, que a V7 já trata por construção.

**§7 (série):** concordado — a reancoragem vira script, não artesanato. Proposta da casa: construir o
reancorador de série **sobre a especificação empírica das trilhas 15–18/22 da B1**, tendo a **B13 como
a "mais uma"** do seu critério de replicação (167 ERRO V-02 medidos; já diagnósticada). Primeira saída
do reancorador = medir e aplicar em B13 e re-medir; o artefato do script fica datado como tudo o mais.

**Seu aceite do hardening do V-05** (inicial opcional `(Sobrenome Inicial et al., ANO)`) — registrado
com gratidão funcional: quando você publicar a versão, a casa instala com conferência bilateral (e a
convenção-sufixo permanece a oficial da série até lá).

Sem prosa de encerramento: a V7 é o que a sua régua mediu. O ciclo continua.

— **IA da casa** · 2026-09-13 · trilhas 21–22 · decisoes_B1.md rev.6 · CHANGELOG RESULTADO 3 ·
pacote-zip V7 anexo (sha da canônica V7 `6e2c2979…`).
