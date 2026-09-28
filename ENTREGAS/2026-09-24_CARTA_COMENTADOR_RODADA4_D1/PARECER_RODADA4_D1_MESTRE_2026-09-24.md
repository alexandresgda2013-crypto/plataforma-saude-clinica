# PARECER DO AUDITOR-MESTRE — RODADA 4 · D1
## Sobre a solução de dois eixos do Comentador

**Auditor-Mestre · 2026-09-24**
**Pergunta:** *"Os dois territórios subscrevem que a separação entre estado de validação e direção de suporte resolve D1 sem alterar indevidamente N1/N2?"*
**Base medida:** N2 v1.4 `d96ad15b…` · Schema-Claim v1.2 `56dc0e94…` · Bloco de Estado v1.6 `0a630dba…` · L-06 rev.6 vigente
**Anti-contaminação:** não li o bloco de colagem do Auditor-Estrutura.

---

## RESPOSTA

**Subscrevo o modelo de dois eixos sem ressalva. Subscrevo a solução como fechamento de D1 com duas ressalvas**, ambas resolvíveis por regra no contrato de saída do Claim Kit, sem tocar em N1/N2.

Separo as duas coisas de propósito, para o operador ver onde está o acordo e onde está o que falta.

---

## 1. O modelo — subscrito sem ressalva

O diagnóstico é o correto e é melhor que a minha própria formulação de 23/09. Eu propus rotear a ressalva por tipo; o Comentador viu a coisa mais funda: **`status_auditoria` e `direcao_suporte` respondem perguntas diferentes**, e o erro nascia de derivar uma da outra. "Toda condição é uma ressalva, mas nem toda ressalva é uma condição" é a relação lógica exata.

Nos quatro pontos pedidos, para o **eixo de condição**:

1. **Suficiência da classificação** — os três tipos (condição, heterogeneidade, maturidade) cobrem o que eu havia apontado.
2. **Preservação do significado** — preservado: a ressalva de heterogeneidade não vira condição, a de maturidade não vira condição.
3. **Casos não cobertos** — ver ressalvas abaixo.
4. **Fabricação de condição** — **impedida**. `condicional` só com condição cientificamente afirmada; `condicao = null` nos demais. O exemplo `.001` ("efeito por sexo diverge") é o caso-teste certo e sai corretamente como `sustenta` + `condicao = null`.

A E-6 em duas camadas (classificar = ciência; preservar = mecânica) está correta e não conflita com "quem produz não atesta".

---

## 2. Ressalva R-1 — a solução impede fabricar condição, mas não impede fabricar direção

Nos §4.1, 4.3 e 4.4, a direção é dada como **"conforme a relação científica efetiva"**. Mas ninguém a decide. Medi o kit:

| No Bloco de Estado | Ocorrências |
|---|---|
| campo `direcao` / `direcao_suporte` | **0** |
| `refuta` | **0** |
| marcadores de divergência/contradição (`contradit`, `diverg`, `inconsist`, `nula`) | **15** |

O kit **não registra direção por fonte**, e contém contradição real dentro de claims — o `.013` carrega a divergência C1q entre duas fontes. Se o materializador tiver de produzir `direcao_suporte` sem entrada decidida, ele vai **inferir** — e o default natural, `sustenta` para toda fonte de um claim aprovado, **fabrica suporte** onde uma fonte não sustenta.

É **o mesmo erro de D1, no outro eixo.** D1 proíbe fabricar condição; a solução, como está, permite fabricar direção.

**Resolução (regra de contrato, não de schema):** a direção por fonte é **decisão científica**, e entra no fechamento do claim do mesmo modo que o tipo da ressalva — classificada pelo processo das três IAs, auditada pela fidelidade científica, e apenas **copiada** pelo materializador. Isso casa com a H-2 da casa, que levantou a mesma lacuna pelo lado estrutural: **peço que a H-2 seja resolvida como classificação científica de entrada, e nunca como default estrutural.**

---

## 3. Ressalva R-2 — o kit já tem um campo de condição estruturada, e a solução não o menciona

A solução propõe criar `ressalvas[]` com `tipo: condicao_aplicacao`. Mas o Schema-Claim v1.2 **já tem** uma estrutura de modificação de efeito:

```
moderadores:
  - variavel:    (ex: IMC, classe_antidepressivo)
    efeito:      atenua | inverte | amplifica | nulo
    regra_motor: tradução operacional para o motor
    fonte_pmid:
```

E ela está em uso: **9 moderadores no Bloco** — `atenua` 3, `amplifica` 5, **`inverte` 1**.

Três consequências, na ordem de gravidade:

**(a) Caso real não coberto — inversão de efeito.** O único `inverte` do kit está no `.001b`, que é `aprovado_com_ressalva`:

> variavel: classe_antidepressivo · efeito: **inverte** · regra_motor: *"ISRS associado a ↓IL-6; tricíclicos/tetracíclicos associados a ↑PCR"*

Aqui a direção **troca de sinal** conforme a variável. Um único N2 com `condicional` e uma `condicao` não consegue representar isso: ele carrega um lado e perde o outro. **Perder a metade invertida é perder ciência**, e é exatamente a informação que o motor precisaria para não sugerir a mesma coisa para ISRS e tricíclicos.

A representação fiel sob o N2 v1.4 é **dois vínculos com condições complementares**, um para cada ramo — e a L-06 vigente já sabe resolver esse par: é `sustenta × refuta` no mesmo objeto, que o degrau 3 fecha por **disjunção de condição**. O contrato vigente já tem o caminho; falta a regra de materialização dizer que `inverte` vai por ele, e nunca colapsa num `condicional` único. *(Que o N2 v1.4 aceite dois vínculos sobre a mesma âncora é ponto estrutural — peço confirmação ao Estrutura.)*

**(b) Duas fontes para `condicao`.** Se `ressalvas[tipo=condicao_aplicacao]` nascer ao lado de `moderadores[]`, o kit passa a ter **dois lugares** de onde uma condição pode vir. Se divergirem, é uma D1 nova, nascida da própria solução de D1. A regra precisa eleger **uma fonte** de `condicao`, ou definir a precedência entre as duas.

**(c) Os demais moderadores precisam de destino declarado.** `atenua` e `amplifica` não são condição de aplicação no sentido de `condicional` — são modificação de magnitude. A solução não diz para onde vão. Sem destino, 8 moderadores estruturados, escritos em linguagem de motor, **se perdem na materialização** — e justamente os que o motor foi desenhado para ler.

**Resolução (regra de contrato, sem mudar N2):** a regra de saída do Claim Kit precisa dizer, para `moderadores[]`: qual `efeito` produz `condicional` + `condicao`; que `inverte` produz dois vínculos complementares; e onde `atenua`/`amplifica` ficam (no claim, via `N2.claim_id`, como a solução já faz com a ressalva de heterogeneidade — o que é aceitável, desde que declarado).

---

## 4. Nota não bloqueante — maturidade já tem destino

O §4.4 diz que a limitação de maturidade *"poderá"* ser representada *"quando houver eixo de maturidade aplicável"*. **Esse eixo já existe:** `grau_maturidade`, na raiz do N2 v1.4, preenchido em 274/274 vínculos do acervo. Não é ressalva à subscrição porque não há risco de elevação — se o campo ficar nulo, a D-02 dá `indefinido` no eixo, nunca herda o mais forte —, mas a solução ganha precisão apontando o destino que já está lá.

---

## 5. Veredito

| Item | Posição |
|---|---|
| Modelo de dois eixos | **subscrito sem ressalva** |
| Impede fabricação de condição | **sim** |
| R-1 — direção precisa de entrada decidida | ressalva — resolver a H-2 como classificação científica |
| R-2 — `moderadores[]`: inversão, fonte única de `condicao`, destino dos demais | ressalva — regra de contrato |
| Maturidade → `grau_maturidade` | nota, não bloqueia |
| Alteração de N1/N2 | **nenhuma** |

As duas ressalvas **não questionam o modelo**; completam a regra de materialização. Nenhuma exige mudar N1 ou N2 — ambas vivem no contrato de saída do Claim Kit, o mesmo ciclo da H-1. Pelo rito, D1 permanece aberta até elas entrarem nesse contrato.

Se o operador preferir fechar D1 sobre o modelo e tratar R-1 e R-2 no ciclo do contrato do kit, isso é coerente com a H-1 — mas então **a primeira materialização não pode ocorrer antes de R-1 e R-2 fecharem**, porque o `.001b` é justamente um dos 22 claims candidatos, e ele cai nas duas.

---

*Medições desta rodada: estrutura de `moderadores[]` lida no Schema-Claim v1.2; efeitos contados no Bloco (atenua 3, amplifica 5, inverte 1); o `inverte` localizado no `.001b` com o texto de `regra_motor`; `direcao`/`refuta` = 0 e 15 marcadores de divergência no Bloco. Camada: substring case-sensitive sobre o texto integral dos arquivos ancorados.*
