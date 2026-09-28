# L-NT — CONTRATO DAS UNIDADES NARRATIVAS
## Minuta 1 · Fase 4

**Auditor-Mestre · 2026-09-18**
**Normativa:** Arquitetura V2.2 (sha `df7f7cfd…`), §6 deveres 1–2 · §7 limites da NT · §13 unidades de explicação · §14 NT e laudo
**Contratos irmãos:** L-05 1.1 minuta 2 (D-02 a D-08) · L-06 minuta 1
**Acervo de referência:** B1 V7 (sha `6e2c2979…`) · P-8 `be48a5ef…`

**Invariante:**

> A NT reorganiza significado. Não produz ciência, não eleva certeza, e não é o lugar onde uma afirmação nasce.

---

# PARTE 1 — DIMENSIONAMENTO MEDIDO

Antes de definir a unidade, medi a B1 V7 para que a regra de granularidade não nasça de hipótese:

| Medida | Valor |
|---|---|
| Blocos canônicos | 11 |
| Marcadores de claim `(BLOCOxx.nnn)` | 90 · **81 distintos** |
| Claims por bloco | mín 1 · mediana 7 · máx 30 |
| Vínculos com `claim_id` | 244/274 |
| Claims referenciados por algum vínculo | **80** |
| Vínculos por claim | mín 1 · mediana 2 · máx 15 |
| Frases de prosa (>60 caracteres) | 628 |
| Palavras na canônica | 21.503 |

**Leitura.** A B1 tem **81 claims distintos** e **628 frases**. A unidade narrativa fica entre os dois: mais grossa que a frase, mais fina que o bloco. O claim é o candidato natural — 80 dos 81 já têm vínculo, e a mediana de 2 vínculos por claim significa que a unidade típica carrega poucas referências, o que a torna verificável.

**Estimativa para a NT-B1: 80 a 130 unidades** (os 81 claims, mais unidades de ligação e de lacuna). Por 146 IDs, na mesma proporção, a ordem de grandeza do programa é **12 a 19 mil unidades**. Esse número precisa estar na mesa antes de alguém aprovar a granularidade, porque é ele que decide se o projeto é executável.

---

# PARTE 2 — A UNIDADE NARRATIVA

## 2.1 Definição

Uma unidade narrativa é o **registro endereçável de uma afirmação ou relação principal**, com os qualificadores necessários para permanecer verdadeira quando lida isoladamente, acompanhada do texto que a explica.

Regra de origem, sem exceção: **toda unidade deriva de pelo menos um claim canônico**. Unidade sem claim de origem é ciência nova e é proibida (§7 da V2.2).

## 2.2 Campos

| Campo | Papel |
|---|---|
| `id_unidade` | endereço estável e opaco (ver 2.3) |
| `claim_origem[]` | claims canônicos de onde deriva — **≥1, obrigatório** |
| `entidades[]` | IDs oficiais envolvidos |
| `relacao` | o que a unidade afirma |
| `sentido_relacao` | direção no grafo (aumenta/reduz/modula) |
| `natureza_relacao` | enum do acervo: causal · contributiva · associativa · compensatoria · marcador · nao_estabelecida |
| `status_epistemologico` | fato · associacao · causalidade · hipotese · evidencia_direta · extrapolacao · lacuna |
| `condicao` / `contexto` | quando vale — **consumidos pelos degraus 2 e 3 da L-06** |
| `eixos` | os cinco da D-02, propagados, nunca recalculados |
| `vinculos[]` | vínculos N2 que a sustentam |
| `origem_conhecimento` | canonico \| atualizacao (V2.2) |
| `uso` | clinico \| contexto_mecanistico \| gap_pesquisa |
| `dependencias[]` | unidades que precisam vir antes |
| `texto_explicativo` | a prosa que o Motor insere no laudo |

Duas observações de fundo.

**O texto não é a unidade; é um campo dela.** É a distinção que o operador pediu e é o que separa NT de resumo. Uma unidade sem `relacao`, `sentido_relacao` e `natureza_relacao` estruturados obriga o Motor a interpretar prosa para descobrir o que ela diz — e interpretar prosa é a função que a arquitetura eliminou ao dispensar IA interna.

**O campo `uso` vem do kit clínico e deveria voltar.** O kit o define em três valores e o aplica por claim (12 clinico / 6 contexto_mecanistico / 4 gap_pesquisa nos 22 claims aprovados). É o campo que impede o Motor de usar evidência pré-clínica como base de sugestão clínica, e hoje ele não existe no acervo. Seja qual for a decisão sobre a camada do kit, **esta é a peça que a NT precisa herdar.**

## 2.3 Endereçamento

`id_unidade` é **opaco e estável**: `NT-B1-0001`. Sem autor, sem ano, sem número de bloco embutido — é a lição do `REF_HAFIZI_2005`, onde um dado mutável dentro do identificador custou o rename de 25 âncoras. O bloco e o claim de origem vivem em campos, não no nome.

## 2.4 Unidades de ligação

Família própria, prevista pela D-04. Uma unidade de ligação tem `texto_explicativo` e `dependencias[]`, mas **não tem `claim_origem`, `eixos` nem `vinculos[]`** — porque não afirma ciência. Se precisar afirmar, deixa de ser ligação e vira unidade comum, com claim e vínculo.

É essa assimetria de schema que torna a regra da D-04 verificável por máquina: **um registro sem `claim_origem` que contenha afirmação científica é detectável**, porque afirmação científica exige campos que a ligação não possui.

---

# PARTE 3 — NÃO-ELEVAÇÃO, EXECUTÁVEL

O §7 da V2.2 proíbe elevar evidência, converter hipótese em fato, associação em causalidade e relação mecanística em eficácia clínica. Traduzido em regras verificáveis:

| Regra | Verificação |
|---|---|
| **N-1** Os cinco eixos são **propagados**, nunca recalculados na NT | comparar `eixos` da unidade com os dos vínculos de origem: iguais ou mais baixos, nunca mais altos |
| **N-2** `status_epistemologico` não pode subir em relação ao claim de origem | ordem declarada: lacuna < hipotese < associacao < extrapolacao < evidencia_direta < causalidade < fato |
| **N-3** `natureza_relacao` não pode subir | associativa não vira contributiva nem causal |
| **N-4** `uso = clinico` exige origem humana | proibido quando o claim de origem é `preclinical_mechanistic` — é a validação cruzada do Schema-Claim v1.2 |
| **N-5** Sem eficácia sem ensaio | unidade que afirme eficácia terapêutica exige claim de origem com desenho intervencional humano |
| **N-6** Toda unidade tem `claim_origem` | exceto ligação, que não pode afirmar |

N-1, N-2 e N-3 são comparações de enum contra a origem — mecânicas. N-4 é conferência cruzada de dois campos. N-5 e N-6 são estruturais. **Nenhuma exige julgamento**, o que é o ponto: a não-elevação deixa de depender de quem escreve a NT.

---

# PARTE 4 — GRANULARIDADE

Os três testes da D-05, agora com procedimento:

- **Isolamento** — a unidade é lida sem contexto. Continua verdadeira? Induz certeza maior que o seu `status_epistemologico`? Falhou: falta qualificador.
- **Remoção** — retira-se a unidade de um laudo montado. Alguma vizinha muda de sentido? Falhou: a fronteira está errada, ou falta declarar `dependencias[]`.
- **Reutilização** — outro contexto clínico a seleciona sem reescrita? Falhou: está grande demais ou específica demais.

**Aceite da NT-B1:** 20 unidades sorteadas, revisor cego, **≥90% aprovadas nos três**. Abaixo disso, a NT-B1 é refeita antes de qualquer B2. A razão unidades/claim medida na NT-B1 vira a métrica de dimensionamento dos 146.

*Risco assumido, repetido da D-05: os três testes têm componente de julgamento. É o item de maior dependência humana deste contrato, e prefiro declará-lo a fingir uma regra automática.*

---

# PARTE 5 — COBERTURA E LACUNAS

**Cobertura.** Todo claim canônico com vínculo gera ao menos uma unidade, ou uma **declaração explícita de não-cobertura** com motivo. Silêncio não é permitido — um claim que some entre a Biblioteca e a NT é perda de conhecimento sem rastro.

**Lacunas.** Os seis tipos da D-03 são representáveis como unidade, com `status_epistemologico = lacuna`. Isso resolve o descarte que apontei na rodada do kit: os **4 claims `gap_pesquisa`** e os **4 vínculos `nao_estabelecida`** viram unidades de lacuna, e o Motor passa a poder dizer "aqui a ciência não estabeleceu" com lastro, em vez de calar.

**Herança de `origem_conhecimento`.** Unidade derivada de claim canônico nasce `canonico`. A Pasta de Atualização **não gera unidade** enquanto não homologada (D-06). Se um dia gerar, nasce `atualizacao` e carrega a origem no próprio payload — o endurecimento aceito na V2.2.

---

# PARTE 6 — O PORTÃO V-NT

| Regra | O que reprova |
|---|---|
| NT-01 | unidade sem `claim_origem` que não seja ligação |
| NT-02 | `claim_origem` inexistente na Biblioteca |
| NT-03 | eixo acima da origem (N-1) |
| NT-04 | `status_epistemologico` ou `natureza_relacao` acima da origem (N-2, N-3) |
| NT-05 | `uso = clinico` com origem pré-clínica (N-4) |
| NT-06 | afirmação de eficácia sem origem intervencional humana (N-5) |
| NT-07 | claim canônico sem unidade e sem declaração de não-cobertura |
| NT-08 | `id_unidade` com dado mutável embutido |
| NT-09 | unidade de ligação com `vinculos[]`, `eixos` ou conteúdo afirmativo |
| NT-10 | `texto_explicativo` contendo PMID, DOI ou número que não esteja em campo estruturado |

NT-10 merece nota: é a defesa contra a NT virar prosa com dados soltos. Um número no texto que não exista em campo é um dado que nenhuma camada pode verificar — e é assim que "27% / OR 1,46" atravessou cinco rodadas na B1.

---

# PARTE 7 — CASO-ARMADILHA

A casa pediu que o contrato nascesse com o seu próprio caso do tipo *"o que este contrato jamais pode produzir"*. Proponho este, construído sobre ciência real da B1:

> **A armadilha da eficácia por ligação.**
>
> Monta-se uma NT com três unidades legítimas: (1) citocinas elevadas associam-se a depressão — origem humana observacional, `associativa`, `uso: clinico`; (2) anti-TNF reduz citocinas — origem intervencional humana; (3) em modelo animal, bloqueio de TNF reverte comportamento tipo-depressivo — origem `preclinical_mechanistic`, `uso: contexto_mecanistico`.
>
> **A saída proibida:** um laudo que, encadeando as três, afirme ou sugira que anti-TNF trata depressão.
>
> Nenhuma das três unidades afirma isso. A afirmação nasceria **na costura** — exatamente o vazamento que a D-04 existe para impedir, e o caso que o §7 da V2.2 nomeia como "converter relação mecanística em eficácia clínica sem sustentação".

**Critério de aprovação:** o encadeamento é permitido e as três unidades aparecem; a conclusão de eficácia **não aparece em forma nenhuma** — nem afirmada, nem sugerida, nem implicada por template. O teste da D-04 executa aqui: afirmações do laudo menos afirmações das unidades = ∅.

E o teste tem lastro no acervo: a B1 carrega o RCT de infliximabe como **negativo no todo e positivo no subgrupo inflamado**. Uma NT que produza a conclusão proibida estará contradizendo a própria evidência que a sustenta — o que torna a armadilha falsificável, e não retórica.

---

# PARTE 8 — DEPENDÊNCIAS

| Dependência | Trava |
|---|---|
| `status_epistemologico` (7 valores) | N-2, NT-04, lacunas |
| `condicao` e `contexto` estruturados | degraus 2–3 da L-06 consumidos pela unidade |
| `uso` herdado do kit | N-4, NT-05 |
| `natureza_evidencia` e `trilha` | 2 dos 5 eixos da D-02 — os 2 ERRO vivos do P-8 |
| Taxonomia de desenho normatizada | eixo `desenho_estudo` |
| Decisão sobre a camada do kit | de onde `uso` e os 4 `gap_pesquisa` são herdados |

**Nenhuma impede escrever a NT-B1.** Todas impedem **validá-la por inteiro**. Recomendo escrever as 20 unidades do aceite primeiro, medir, e só então produzir as 80 — para que um erro de granularidade custe 20 unidades, não a biblioteca inteira.

---

*Medições desta rodada: 81 claims distintos, 11 blocos, 244/274 vínculos com claim_id, 80 claims com vínculo, 628 frases, 21.503 palavras — todas na B1 V7 `6e2c2979…`, camada declarada: regex `\(BLOCO(\d{2})\.(\d{3})\)` sobre a canônica; `claim_id` não-vazio sobre os vínculos; frases por split em pontuação final com corte em 60 caracteres.*
