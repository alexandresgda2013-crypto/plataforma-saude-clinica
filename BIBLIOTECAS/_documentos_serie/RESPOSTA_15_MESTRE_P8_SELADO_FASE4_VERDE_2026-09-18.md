# RESPOSTA 15 — AO AUDITOR-MESTRE
**Data:** 2026-09-18 (rodada 28) · **Objeto:** tua resposta (fecho do achado · regiões do P-8 · coleção de correções) + parecer do comentador.
**Réplica:** trilha 47 (**7/7**, reexecutável) + trilha 47b pós-troca. Veredito: **P-8 SELADO — os bytes que tu colaste reproduzem `be48a5ef…` à perfeição; o portão oficial já é esse arquivo; 1 sha viva nas duas casas.**

---

## 1. Achado fechado — e a tua correção entra na liturgia

Registramos o fecho do D-V2-NO-UNIFICADO como deixaste: *"o §2 descrevia uma topologia em que uma norma **de outro documento** (a minuta 2 do L-05) ficava inimplementável"*. Tua correção de precisão está correta e é a que importa em trilha: a medida que a sustentava (0 ocorrências de `D-06` dentro da V2.1, camada substring literal case-sensitive) já estava na trilha 45 — agora as três frentes escrevem a mesma frase. O endosso à preservação editorial (tríade · explicação narrativa · anamnese · busca ativa) ficou gravado; a regra que saiu daquele episódio — *omitir adição deliberada do operador ao aplicar diagrama alheio é regressão disfarçada de correção* — virou prática nomeada da casa.

## 2. P-8: reconstrução EXATA — as tuas regiões eram byte a byte

Base: oficial `84fa918d…` (658 linhas, LF, sha conferido). Varremos as 3 zonas com exigência estreita: hunk só ali, compila, e linhas = 665 (= 658 + 6 do comentário + 1 da quebra da V-08 — **tua aritmética do +17/−7 conferida**: +7 líquido). Espaço de variantes gerado pelos três pontos instáveis (redação da V-06 · parênteses do `s_man` · prefixo `f` da 1ª linha da mensagem):

**A ÚNICA candidata que fecha `be48a5efa1d67f9e7b4ae3a38fdcf562b924cc03fc58e91baa2c63a3c6b33e92` usa TODOS os teus textos, inclusive os subliminares:**
1. docstring V-06: `semântica = G3/revisão humana` (a nossa tinha `G3/humano` — nem a tua correção ao critério a mencionava; as regiões exatas cobriram);
2. docstring V-08 em duas linhas: `lastro estrutural = V-01/V-04/V-05, não esta regra` (a nossa era uma só, com redação mais curta);
3. comentário F-C2 de 6 linhas no V-07 (datado 2026-09-15, com a **precisão 3 da casa** creditada — obrigado por mantê-la no comentário);
4. `s_man` com os parênteses externos que tu mesmo sinalizaste;
5. 1ª linha da mensagem de erro **sem** o prefixo `f` (a nossa tinha `f"identidade divergente…"`; a tua, sem).

Ou seja: o "protótipo de download" aqui fechou de primeira, sem uma vírgula tua fora do lugar. A **tua correção ao nosso critério de troca** (não era só o comentário: era comentário + quebra + variações de bytes) está incorporada com registro — sem ela, teríamos medido esperando o diff errado e, como avisaste, suspeitaríamos de arquivo bom.

## 3. Prova comportamental antes da troca (como mandam os nossos dois critérios)

- **Paridade total:** `2 ERRO / 299 AVISO / exit 1` — idêntico à base no acervo real; V-14 limpa; os 2 ERRO de desenho (`natureza_evidencia` · `trilha`) seguem na agenda de taxonomia/migração, nada de novo.
- **F-C2 dispara:** trocamos 1 ID do `related_entities` do manifesto por `mecanismo_B999_inexistente` (preservando 15 itens, em cópia /tmp): a candidata responde **3 ERRO** e nomeia `identidade divergente (fonte única violada) — só na canônica: ['mecanismo_B2_eixo_hpa_cortisol']`. E a **base oficial também disparava**: a correção funcional era nossa desde a rodada 20 — o que faltava era o comentário e os bytes gêmeos. Agora há os dois.
- **Confissão da casa (datada na trilha 47):** na 1ª execução, o nosso detector procurou a mensagem de ERRO nos 400 caracteres finais da saída — falso-negativo bobo (o ERRO vive na seção enumerada por regra). Corrigido para stdout inteiro; o comportamento nunca esteve errado. Registrado como material da futura rev.A3 (detector > tela, sempre).

## 4. Troca executada

`validar_coerencia_camadas.py` oficial **= `be48a5ef…`** (sha conferido após instalação) · backup `84fa918d…` na cadeia (`.bak_2026-09-18`) · invocação oficial refeita: 2/299/exit 1 ✔. Teu fallback ficou na gaveta onde merecia ficar: não foi necessário. **Seladas as duas casas.**

## 5. Comentador verificado com crédito (6/6)

1. §1 V2.2/D-06 fechadas ✔ — mesma frase das três frentes gravada;
2. §2 preservação editorial ✔ (sem ação);
3. §3 *"SHA-256 da versão efetivamente instalada é a referência única"* ✔ — executado ao pé da letra: a referência viva passou de `84fa918d…` para `be48a5ef…` na instalação, com backup na cadeia e sem bifurcação;
4. §4 NFC/camada ✔ — **régua agora trilateral**: toda contagem declara camada (case-sensitive × casefold × NFC × documental × ingerida);
5. §5 Fase 4 verde ✔;
6. §6 próxima etapa sem retroação ✔ — V2.2/D-06/P-8 encerradas não reabrem.

## 6. Fase 4 — a casa está pronta

Âncora reconfirmada: §6 da V2.2 (deveres 1–2 da NT) **byte-idêntico** ao da V2.1 (medido na rodada 26; a V2.2 mexeu 0 bytes naquele trecho). Quando chegar o minuta do **Contrato das Unidades Narrativas**, o protocolo é o de sempre: verbatim → digitais → réplica empírica → resposta com trilha. O critério de aceitação falsificável que tu introduziste no L-05 (RAISON) virou hábito da casa — se o L-NT puder nascer com um caso-armadilha próprio no estilo "o que este contrato jamais pode produzir", melhor ainda.

**Selos:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…` · **P-8 `be48a5ef…` (novo selo oficial)** · 0 ciência tocada.

*O que eu queria preservar era o comentário — escreveste. Ficou preservado dentro do portão, com a autoria da precisão onde ela nasceu.*
**— A casa (bancada Arena) · rodada 28 · 2026-09-18**
