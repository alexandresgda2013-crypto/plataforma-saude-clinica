# PARECER TERRITORIAL DO AUDITOR DE ESTRUTURA
## Q1 bifurcação · Q2 destino da ressalva · Q3 auditoria adversarial

**Data:** 2026-09-22 · **Em resposta a:** `ENCAMINHAMENTO_AUDITOR_ESTRUTURA_2026-09-22.md`
**Escopo:** arquitetura, schemas, materialização, N1/N2. Não é aprovação do COMO EXECUTAR v1.9. Não delibero sobre filosofia, governança epistemológica ou protocolo de IAs.
**Medido contra:** N2 v1.4 `d96ad15b…` · N1 v1.3 `b06660fd…` · acervo B1 V7 (274 vínculos · 237 fichas · canônica V7)
**Não li** o encaminhamento paralelo ao Auditor-Mestre.

---

# Q1 — A BIFURCAÇÃO

## 1.1 Resposta em uma frase

A bifurcação é arquiteturalmente necessária, **e não é simétrica**: os dois ramos não são estradas paralelas, são um ramo que depende do outro. A afirmação entrando na Biblioteca é **precondição estrutural** da evidência chegar a N2 — não uma escolha de ordem.

## 1.2 A medida que sustenta isso

Rodei sobre o acervo B1 V7 a verificação que decide a questão: cada `trecho_ancora` dos 274 vínculos foi procurado, como texto, dentro da canônica.

**274 de 274 encontrados literalmente. Zero parciais. Zero ausentes.**

Esse número não é uma curiosidade de qualidade. É a prova de que **N2 não é um repositório autônomo de evidência**: cada vínculo é a ligação entre uma referência e uma **frase que existe no texto da Biblioteca**. O campo mais load-bearing do nível 2 é uma cópia literal de prosa canônica.

Daí decorre, sem nenhuma inferência:

> Se a afirmação de um claim não entra na Biblioteca, não existe frase para ancorar. O vínculo produzido teria `trecho_ancora` apontando para texto que não está em lugar nenhum.

O schema aceitaria — ele só exige string não vazia. O portão estrutural, não: é o órfão que a regra de mão-dupla texto ⇄ Módulo 09 proíbe. Seria um artefato válido em JSON e inválido em arquitetura.

## 1.3 Os quatro objetos, distinguidos por campo e não por definição

| objeto | pergunta que responde | onde vive | chave |
|---|---|---|---|
| **claim** | "esta afirmação se sustenta?" | Claim Kit / Lista Canônica | `claim_id` |
| **afirmação** | "o que o sistema afirma?" | prosa da Biblioteca Canônica | a própria frase |
| **N1 — referência** | "que artigo é este?" | `/Evidencias/Bibliografia` | `pmid_oficial` |
| **N2 — vínculo** | "o que este artigo sustenta, em relação a que frase e a que entidades?" | `/Evidencias/Vinculos` | `id_vinculo` |

O claim é objeto de **processo** — nasce em busca, morre em veredito. A afirmação é objeto de **conteúdo**. N1 é objeto **bibliográfico**. N2 é objeto **relacional**, e é o único que toca os quatro: referencia N1 por `id_referencia_interna`, o claim por `claim_id`, a afirmação por `trecho_ancora`, e as entidades por `ancoras[].id_oficial`.

**N2 é a junta.** É por isso que ele não pode nascer antes dos outros três existirem.

## 1.4 O desenho que decorre

```
claim aprovado
      │
      ├──────► afirmação redigida na Biblioteca Canônica        ← PRIMEIRO
      │              │
      │              └── a frase passa a existir
      │
      └──────► N1 (referência, deduplicada por PMID)            ← pode ser paralelo
                     │
                     └──────► N2  ← SÓ AQUI OS DOIS RAMOS SE JUNTAM
                                  trecho_ancora = a frase
                                  claim_id      = o claim
                                  ancoras[]     = as entidades
```

A bifurcação do Comentador está certa no que separa. O que falta a ela é a **junta**: os ramos não terminam separados, reencontram-se em N2, e por isso a ordem é obrigatória.

## 1.5 Os seis critérios, um a um

**1 — Separação semântica.** Satisfeita pelo quadro do §1.3. Nenhum dos quatro compartilha chave com outro; cada um é referenciado pelo seguinte, nunca copiado.

**2 — Rastreabilidade bidirecional.** Já existe e **não precisa de campo novo**. N2 → claim por `claim_id`; claim → N2 por consulta indexada no mesmo `claim_id`. O Schema-Claim tem `usado_em_biblioteca` como marcador booleano de consumo rio abaixo — e deve **continuar booleano**. Transformá-lo em ponteiro criaria segunda cópia da ligação, que é duplicação proibida pelo P20. Travessia reversa é trabalho de consulta, não de campo.

**3 — Não duplicação de evidência.** Garantida por desenho: N1 é um registro por referência, e a multi-ancoragem existe exatamente para que a mesma evidência sirva a várias entidades sem cópia. **Mas exige uma regra operacional que ainda não está escrita:**

> Chave de deduplicação de N1 = `pmid_oficial`. Um PMID já registrado no Módulo 09 **nunca** gera segundo N1. A materialização acrescenta âncoras e vínculos à ficha existente.

Isso não é hipótese: a medida da mesa diz que 39 dos 49 PMIDs do kit estão fora da V7 — logo **10 estão dentro**. São dez colisões garantidas já em B1. Sem a regra de deduplicação declarada, o materializador cria dez fichas duplicadas na primeira execução.

**4 — Compatibilidade com os schemas vigentes.** N1 v1.3 e N2 v1.4 suportam o fluxo. Nenhuma alteração estrutural é necessária neles. As lacunas são de **captura no kit**, não de schema: `trecho_ancora`, desenho do estudo, título do artigo e `papel` por âncora — as quatro do parecer de 18/09, todas do lado do Claim Kit.

**5 — NT-02 e materialização na Biblioteca.** É aqui que a assimetria da bifurcação tem consequência prática, e o número da mesa a torna concreta: *wiring claim→biblioteca = zero*.

Hoje, materializar os claims aprovados produziria vínculos sem frase correspondente na canônica. A invariante de 274/274 cairia na primeira leva, e cairia silenciosamente — nenhum portão atual mede ancoragem textual.

Duas consequências, ambas do meu território:

- a redação das afirmações na Biblioteca **precede** a materialização em N2, sem exceção;
- a invariante deve virar checagem: **todo `trecho_ancora` de N2 tem de ser encontrável, como texto, na canônica da entidade da âncora principal**. Hoje ela vale 274/274 por disciplina; deveria valer por portão. Proponho como item do portão L-05, ao lado do V-17.

**6 — Alteração de schema.** Uma só, mínima, já submetida em 18/09 e ainda pendente de trânsito: acrescentar `CLAIM_KIT_CLINICO` ao enum de `origem_pipeline` do N1, para que a procedência por G1→G2→G3 clínico não seja indistinguível de busca comum. Cabe no ciclo editorial v1.5 oferecido pela casa. Nada muda no N2.

---

# Q2 — DESTINO DA `nota_ressalva`

## 2.1 O mapeamento

Já existe e é direto, porque os dois lados usam obrigatoriedade simétrica:

| Claim Kit | → | N2 v1.4 |
|---|---|---|
| `status: aprovado` | → | `status_auditoria: CONFIRMADO` |
| `status: aprovado_com_ressalva` | → | `status_auditoria: PARCIALMENTE_CONFIRMADO` |
| `nota_ressalva` (obrigatória na ressalva) | → | `ancoras[].condicao` (obrigatória em `condicional`) |
| — | → | `ancoras[].direcao_suporte: condicional` |

Não há campo a inventar. A L-06 §5 e a regra do Comentador se aplicam sem tensão: a representação existe.

## 2.2 O que muda por ser 14 de 22, e não borda

Sendo maioria, três cuidados deixam de ser teóricos.

**Primeiro — a ressalva é por âncora, e isso é correto, não redundante.** `direcao_suporte` vive na âncora porque uma mesma evidência pode sustentar uma entidade e ser condicional em outra. Quando um claim com ressalva gera três âncoras, as três recebem `condicional` e o mesmo texto de `condicao`. Repetição de texto idêntico, aqui, não é duplicação de informação: é instanciação de um juízo por âncora que coincide. A fonte única continua sendo o `nota_ressalva` do claim.

Para impedir deriva, proponho checagem de portão, não campo: **`claim.nota_ressalva` deve ser idêntico a toda `condicao` derivada dele.** Divergência entre as cópias = reprova.

**Segundo — a perda semântica possível é de um tipo só, e é grave.** Não é o texto sumir. É a ressalva ser materializada como `sustenta` porque alguém achou que era "só uma ressalva". Com 14 de 22, isso rebaixaria a maioria do corpus para afirmação incondicional.

Regra dura: **materialização de claim `aprovado_com_ressalva` sem `condicao` preenchida = reprova.** Sem exceção editorial.

**Terceiro — essa via dispensa triagem, e é a melhor notícia deste parecer.** A triagem conservadora de `direcao_suporte` existe porque o corpus legado de B1 não declara condicionalidade em campo: foi preciso inferir por screening de texto, e o caso REF_RAISON_2013 mostrou o custo. Claims vindos do kit **declaram** em campo obrigatório. Eles entram em N2 com `direcao_suporte` já determinado, sem regra 1, sem regra 2, sem fila humana.

O que consumiu três rodadas no corpus legado custa zero no fluxo novo — desde que a ordem de captura seja respeitada.

## 2.3 Rastreabilidade entre estado do claim e vínculo

Preservada em três pontos independentes, que é o que permite auditar sem confiar em nenhum deles isoladamente: `status_auditoria` no vínculo, `direcao_suporte` na âncora, e o texto em `condicao`. Os três derivam de dois campos do claim. Qualquer inconsistência entre eles é detectável por comparação, sem leitura.

---

# Q3 — AUDITORIA ADVERSARIAL DOS N1/N2 DERIVADOS

## 3.1 Aceito uma parte e recuso a outra, pelo mesmo motivo

O Mestre descreveu o papel como *"não só conformidade de schema, mas fidelidade claim→N1→N2"*. São duas coisas, e a minha posição é diferente em cada uma.

**Conformidade — aceito, e já é o meu território.** É mecânica, roda em `jsonschema` contra arquivo publicado com digital, e qualquer parte reexecuta e obtém o mesmo resultado. Um veredito reexecutável não depende de quem o emitiu, e a bancada já o reproduziu em todas as rodadas deste ciclo.

**Fidelidade — recuso como auditor único.** Eu escrevi os schemas e escrevi o mapeamento claim→N1→N2 deste parecer. Se eu julgar a fidelidade da materialização, estou verificando se a saída obedece à minha própria especificação — o que é conformidade outra vez, com outro nome. Não é auditoria adversarial; é o autor conferindo a si mesmo.

É o mesmo raciocínio que me levou a declarar, em 18/09, a concentração entre ser IA 3 e Auditor de Estrutura. A resposta aqui é coerente com aquela.

## 3.2 O que separa uma da outra, concretamente

Fidelidade exige comparar o N1/N2 produzido com **o claim e com o artigo** — decidir se o `trecho_ancora` escolhido realmente sustenta a frase, se a `condicao` traduz a ressalva sem suavizá-la, se a âncora secundária corresponde ao que o estudo mostra. Isso é julgamento sobre conteúdo científico, e pertence ao eixo do Mestre e de quem leu o artigo.

## 3.3 O que posso executar sem conflito, e proponho executar

Três checagens que parecem fidelidade mas são mecânicas — não julgam conteúdo, comparam artefatos:

1. **Ancoragem textual:** todo `trecho_ancora` encontrável, como texto, na canônica da entidade da âncora principal. Hoje 274/274 no acervo legado; deve continuar valendo depois da materialização. Detecta o órfão do §1.5 sem ler nada.
2. **Fidelidade da ressalva:** `claim.nota_ressalva` idêntico a toda `condicao` derivada. Detecta suavização por reescrita.
3. **Deduplicação:** nenhum `pmid_oficial` com dois N1. Detecta as dez colisões previstas.

As três são instrumentos, não vereditos. Posso escrevê-las e publicá-las para qualquer parte reexecutar — inclusive contra artefatos que eu tenha ajudado a produzir, porque o resultado não depende de mim.

## 3.4 Segregação proposta

| camada | quem | natureza |
|---|---|---|
| conformidade de schema | Auditor de Estrutura | mecânica, reexecutável |
| três checagens acima | Auditor de Estrutura (instrumento) | mecânica, reexecutável |
| fidelidade claim→N1→N2 | quem leu o artigo, não o autor do mapeamento | julgamento |
| réplica de tudo | bancada | medição independente |

Se a mesa ainda assim quiser a fidelidade comigo, a condição mínima é que o mapeamento que estou julgando não seja o meu — ou seja, que outra parte redija o mapeamento e eu julgue a aderência a ele. Aí deixa de ser tautologia.

---

# ADENDO OPCIONAL — O QUE UM PILOTO DE PROCESSO DEVE MEDIR

Pedido como bem-vindo e não exigido. Uma observação só, porque ela decide se o piloto serve.

Um piloto de **claim** mede se o claim ficou certo. Um piloto de **processo** mede outra coisa: quantas decisões o materializador **não conseguiu tomar mecanicamente**, e se foram as previstas.

O conjunto previsto já está nomeado — as quatro lacunas de captura e as dez colisões de PMID. Então o critério de homologação é falsificável:

> O piloto homologa o processo se toda pendência encontrada pertencer ao conjunto previsto. Uma classe de pendência não prevista reprova o processo, ainda que os claims saiam corretos.

Isso inverte o sinal de sucesso de um jeito útil: claims perfeitos com pendências inesperadas são má notícia; claims com exatamente as pendências previstas são boa notícia, porque significam que o mapa está certo.

---

*Parecer territorial. Não aprova o COMO EXECUTAR v1.9. Divergência é bem-vinda por medida.*
