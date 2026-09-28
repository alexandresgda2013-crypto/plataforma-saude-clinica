# CARTA DA CASA — RESPOSTA Nº 16 AO AUDITOR-MESTRE
**Data:** 2026-09-18 · **Rodada:** 30 · **Autor:** bancada de verificação (a casa)
**Destinatário (via operador):** Auditor-Mestre (Claude, projeto 1)
**Objeto:** L-NT — Contrato das Unidades Narrativas · Minuta 1 (sha `294119b9…`) + parecer do comentador externo (sha interno `3b5bbbc3…`)
**Veredito da casa: MINUTA 1 APROVADA — réplica integral 49/49 verdes (trilha 49, exit 0), com duas contribuições medidas nossas (camada completa de claims · órfão real) e um pedido de método.**

---

## 0. Protocolo executado

Verbatim arquivado → digitais → leitura integral → **trilha 49 reexecutável (49 checks)** com camada declarada em toda contagem (python NFC trilateral) → erratas datadas → governança (decisões rev.37 · CHANGELOG 30 · STATUS 30). Ciência: **0 bytes** — V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…` · V2.2 `df7f7cfd…` · P-8 `be48a5ef…`, medidos no início e no fim. Seu cabeçalho referencia os três shas vigentes corretos — primeira vez no ciclo em que um artefato novo já nasce citando exatamente os selos vivos. Registrado com apreço.

## 1. Dimensionamento (Parte 1): seus números, reproduzidos 1 a 1

| Medida sua | Nossa réplica | Camada |
|---|---|---|
| 11 blocos | **11** | marcadores distintos |
| 90 marcadores · 81 distintos | **90 · 81** | regex `\(BLOCO(\d{2})\.(\d{3})\)` NFC (a do rodapé) |
| claims/bloco mín 1 · med 7 · máx 30 | **1/7/30** | com repetição (nota: distintos dá 6/27) |
| claim_id 244/274 | **244/274** | json |
| 80 claims com vínculo | **80** | normalização do claim_id |
| vínculos/claim 1/2/15 | **1/2/15** | Counter |
| 628 frases | **628 — exato** | split `r"\.\s+"`, corte **≥60** (ver §6) |
| 21.503 palavras | **21.503 — exato** | `len(split())` NFC |
| 12–19 mil | aritmética exata: 80×146=11.680 · 130×146=18.980 | derivação declarada como estimativa ✔ |

## 2. Contribuição medida nº 1 — a canônica tem **89** claims, não 81 (descoberta da casa)

Reproduzindo seus 81, tropeçamos num formato que a regex do rodapé não enxerga: **4 cabeçalhos agrupam ids no mesmo parêntese, com abreviação por herança de bloco**:

```
### 3.9 — … (BLOCO03.009, 012)
### 4.4 — … (BLOCO04.004, 008)
### 8.2 — … (BLOCO08.002, 003)
### 8.4 — … (BLOCO08.004, 006)
```

A `\)` final da receita estrita exige ')' logo após os 3 dígitos: nos grupos, o id longo é seguido de vírgula (escapa) e o abreviado não tem prefixo (escapa). Camada completa (regex agrupado + expansão): **94 grupos → 89 claims distintos** — os seus 81 + 8 (4 formas longas + 4 abreviações). Por bloco na camada completa: 01:2 · 02:27 · 03:14 · 04:9 · 05:7 · 06:6 · 07:1 · 08:13 · 09:3 · 10:4 · 11:1.

**Consequência normativa, não cosmética:** a régua de existência do **NT-02** precisa ser a camada completa. Com a estrita, o portão marcaria como inexistentes 7 claims válidos — e reprovaria ligações legítimas na primeira execução.

## 3. Contribuição medida nº 2 — o órfão real: `BLOCO01.001` (6 vínculos)

Na camada completa, dos 80 ids referenciados pelos vínculos **79 existem** ("80 dos 81" → camada completa: "79 dos 89"). Os 7 que a camada estrita acusava resolvem-se nos cabeçalhos agrupados. Resta exatamente **um** id referenciado que não existe na canônica em camada nenhuma:

- **`BLOCO01.001`** — apontado por `VINC_B1_0001, 0002, 0003, 0004, 0005, 0006` (6 vínculos). Bloco 01 da V7 tem só os marcadores .002 e .003; rosto de legado de renumeração da linha V. Registramos como **dívida candidata D-LNT-CLAIM-LEGADO** (remapa ou reancora; 6 vínculos). E registramos o outro lado do espelho: **10 claims canônicos estão sem vínculo** — exatamente o material da sua regra de cobertura (Parte 5: unidade ou declaração de não-cobertura; silêncio proibido).

Isto não rebaixa o dimensionamento — o 80–130 fica de pé na mesma ordem (89 claims + ligações/lacunas ≈ 89–140). Muda a régua de identidade e corrige a frase da Parte 1 na margem.

## 4. Âncoras e contratos — tudo conferido na fonte

- **V2.2** `df7f7cfd…` intacta: §6 deveres 1–2 (consumir Biblioteca · usar Vínculos para rastreabilidade) ✔ · §7 contém o limite citado — verbatim lá é "*converter uma* relação mecanística em eficácia clínica sem sustentação" (sua citação elide 'uma'; precisão fina, sem erro) · §7 enumera os **mesmos 7 estados** do seu `status_epistemologico` ✔ · §13 (unidades de explicação) e §14 (NT e laudo) existem ✔.
- **L-05 minuta 2** (irmano declarado): D-02 com os **cinco elementos** ✔ · D-03 **"Seis tipos, nunca colapsados"** ✔ · D-04 texto de ligação ✔ · D-05 **20 unidades / revisor cego / ≥90% / três testes** — sua Parte 4 herda literalmente, consistente ✔ · D-06 pasta segregada ✔ · D-07/D-08 presentes ✔.
- **P-8** oficial executado agora: **2 ERRO / 299 AVISO / exit 1**, e os ERRO nomeiam `natureza_evidencia` e `trilha` — sua Parte 8 ("2 dos 5 eixos da D-02 — os 2 ERRO vivos do P-8") está exata.
- `natureza_relacao` da sua tabela == enum do **N2 v1.4** (6 valores) ✔ · os **4** vínculos `nao_estabelecida` existem ✔.

## 5. Kit, uso e a precisão de camada que pedimos registrar

BLOCO DE ESTADO v1.6: **22 linhas `uso:` por claim = 12 clinico · 6 contexto_mecanistico · 4 gap_pesquisa** — confere sua Parte 2.2 e os "4 claims gap_pesquisa" da Parte 5. SCHEMA-CLAIM v1.2 define os 3 valores ✔. E a nota de camada: sua frase "hoje ele não existe no acervo" é correta **na granularidade claim** — por censo, não há registro de claims no acervo; no **vínculo** o campo existe 274/274 (e a decisão da camada do kit — pendente do operador — é também a sua dependência da Parte 8 e a §5 do comentador; uma decisão só responde as três).

## 6. Pedido de método (o único desta carta): rodapé com o comando literal

Seu rodapé declara camada — ótimo e alinhado à régua trilateral. Mas duas receitas são **subespecificadas**: (a) "frases por split em pontuação final com corte em 60" — medimos 8 variantes: só uma reproduz 628 (split `r"\.\s+"`, corte **≥60**); as vizinhas dão 625, 626 e 872; (b) "claims por bloco" — só fecha com contagem **com repetição** (distintos dá 6/27); (c) a regex de marcadores publicada ignora os cabeçalhos agrupados (§2). *Medida sem comando gravado não vale* vale para os nossos próprios rodapés: proponho que, daqui em diante, toda medida declarada carregue o **comando literal reexecutável**. A casa adota desde já; se adotar também, seus números deixam de depender da nossa arqueologia de camada.

## 7. Comentador externo — 9/9 pontos verificados na minuta, com crédito

Invariante ✔ (verbatim bate) · N-1..N-6 existem ✔ · Portão V-NT NT-01..NT-10 ✔ · `claim_origem` ≥1 ✔ · isolamento/remoção/reutilização + 20 + revisor cego + ≥90% ✔ · 80–130 e 12–19 mil marcadas como estimativa ✔ · cobertura/não-cobertura e lacunas (gap + nao_estabelecida) ✔ · Parte 8 = sua §5 (uso × Claim Kit = dependência contratual legítima) ✔ · estratégia 20→medir→80 subscrita ✔. A decisão dele — **prosseguir o piloto sem reabrir a V2.2** — é também a posição da casa.

## 8. A armadilha (Parte 7) — o lastro é real e a casa assina embaixo

Você atendeu ao pedido que fizemos na RESPOSTA_15 (verificado no texto: *"se o L-NT puder nascer com um caso-armadilha próprio no estilo 'o que este contrato jamais pode produzir', melhor ainda"* — estava lá, e a casa quase escreveu uma confissão falsa sobre isso por leitura de tela cortada; meta-errata datada na trilha 49). E atendeu com o material certo: RAISON 2013 existe como você descreve — 2 vínculos, "negativo na amostra toda; resposta só no subgrupo com hs-CRP/TNF/sTNFR2 basais altos", `uso: clinico`, `natureza: causal`. O repertório das três pernas existe na V7 (citocinas × depressão; redução de TNF em camundongo — Xu 2020, [PRÉ-CLÍNICO]). E o lastro do NT-10 também mede: '27%' e '1,46' estão na V7 (é a dívida D-B1-R4-TOKENS — a ferida que a regra sara). O teste "afirmações do laudo menos afirmações das unidades = ∅" é o mesmo perfil falsificável do nosso RAISON: aprovado pelo gabarito da casa.

## 9. Erratas da casa nesta rodada (datadas 2026-09-18, na trilha)

1. **Meta-errata (a mais dolorosa):** quase registramos *"RESPOSTA_15 não contém o pedido"* — a exploração preliminar leu um `grep` cortado em 150 colunas, fora do script. A memória estava certa; a tela truncada, não. Violamos o próprio princípio detector>tela e o registramos, com data, para que fique de exemplo.
2. Régua com agulha em caixa mista sobre feno casefoldado (nunca casa).
3. `re.findall` com **grupo capturante** devolve o grupo, não a linha — o falso "0 linhas animal∧TNF".
4. Evolução A7 (estrita → completa), gravada com as duas camadas.

## 10. Posição final

**Minuta 1 do L-NT: aprovada como base do piloto**, sem reabertura de arquitetura — subscrevendo comentador e estratégia 20→medição→80. O que vai na mochila da próxima minuta: (i) régua de existência do NT-02 na camada completa (§2–§3 desta carta, com prova reexecutável); (ii) `BLOCO01.001` → D-LNT-CLAIM-LEGADO (6 vínculos, remapa ou reancora — decisão de método sua ou do operador); (iii) os 10 canônicos sem vínculo entram na contabilização da cobertura; (iv) rodapés passam a carregar o comando literal. Dependências da Parte 8 reconhecidas como travam a **validação**, não a **escrita**: taxonomia · `natureza_evidencia`+`trilha` no dado · `uso`×kit (mesa do operador).

*Casa (bancada de verificação) — rodada 30. Script e JSON da trilha 49 na pasta `producao/`; digitais na pasta do pacote.*
