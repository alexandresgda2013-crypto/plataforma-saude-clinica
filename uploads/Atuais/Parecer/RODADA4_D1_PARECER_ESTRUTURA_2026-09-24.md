# RODADA 4 — D1 — PARECER DO AUDITOR-ESTRUTURA

**Data:** 2026-09-24 · **Em resposta a:** `COLA_RODADA4_ESTRUTURA_2026-09-24.md` + `COMENTADOR_SOLUCAO_D1_2026-09-24.md` + posição da casa (H-1..H-3)
**Medido contra:** N2 v1.4 `d96ad15b…` · N1 v1.3 `b06660fd…` · SCHEMA-CLAIM v1.2 (clínico) · SCHEMA-CLAIM v3.1 (mecanístico) · acervo B1 V7

---

# RESPOSTA À PERGUNTA ÚNICA

## **SUBSCREVO SEM RESSALVA.**

A separação entre estado de validação e direção de suporte resolve D1 sem alterar indevidamente N1 ou N2.

A H-2 está respondida abaixo como **item de contrato**, não como condição da subscrição — e a resposta dela não exige campo novo nem semântica nova, o que é o motivo de eu não precisar condicionar.

---

# 1. ANTES DOS CINCO PONTOS — O ERRO ERA MEU

O mapeamento que o Comentador aboliu é meu. Escrevi `aprovado_com_ressalva → condicional → condicao = nota_ressalva` no parecer de 18/09 e repeti em 22/09 como se fosse achado feliz de encaixe.

Era erro de derivação, e da pior espécie disponível para mim: **eu criei a separação de eixos e depois a violei.** O R7 existe porque `refuta` dentro de `papel` misturava relação temática com veredito — e eu argumentei, na época, que misturar eixos é o defeito que a proposta inteira combate. Um mês depois derivei direção evidencial a partir de estado de validação, que é a mesma operação com outros dois campos.

O que me enganou foi a simetria de obrigatoriedade: `nota_ressalva` é obrigatória quando há ressalva, `condicao` é obrigatória quando condicional, e o encaixe pareceu prova. Simetria de cardinalidade não é identidade semântica. O Mestre viu isso e está certo.

Registro sem atenuação porque a regra esteve em duas peças minhas e pode ter sido citada rio abaixo.

---

# 2. OS CINCO PONTOS DO ENCAMINHAMENTO

## 2.1 Compatibilidade com o N2 v1.4

**Total.** A solução não toca o N2. Os três campos que ela usa já existem com a semântica que ela pede: `status_auditoria` no vínculo, `direcao_suporte` e `condicao` na âncora.

A observação de que os eixos vivem em camadas distintas — estado no vínculo, direção na âncora — é exata e é estrutural, não acidental. Um vínculo tem um estado de validação; suas âncoras podem ter direções diferentes, porque a mesma evidência pode sustentar uma entidade e ser inconclusiva em outra. Colapsar os dois seria impossível de representar mesmo que alguém quisesse.

## 2.2 Manutenção dos `if/then`

**Mantidos, e são o que torna a solução executável.**

A regra do §4.3 e do §4.4 — ressalva de heterogeneidade ou de maturidade **não** produz `condicao` — não depende de disciplina: o `allOf` do N2 v1.4 já **proíbe** `condicao` preenchida quando `direcao_suporte` é `sustenta`, `refuta` ou `inconclusivo`. Um materializador que tentasse preservar a ressalva enfiando texto em `condicao` sem marcar `condicional` seria reprovado pelo schema.

Ou seja: a proibição de fabricar condição que o Mestre pede **já está no contrato estrutural**, escrita antes desta discussão. A solução do Comentador não precisa de nova trava; ela se apoia numa que existe.

## 2.3 Necessidade de alteração de schema

**Nenhuma**, nem no N2 nem no N1, para D1.

O que muda é o contrato de derivação Claim→N2, que nunca foi schema. O diagnóstico da casa está certo: era erro de derivação, não colisão de campo.

## 2.4 Testes mecânicos possíveis

Quatro, sendo o terceiro novo e habilitado justamente pela classificação:

1. `direcao_suporte = condicional` ⇒ `condicao` não nula — **já no schema**.
2. `direcao_suporte ∈ {sustenta, refuta, inconclusivo}` ⇒ `condicao` nula — **já no schema**.
3. **Correspondência tipo → destino**, novo: `tipo = condicao_aplicacao` ⇒ `condicional` com `condicao` preenchida; `tipo ∈ {heterogeneidade, maturidade_evidencia}` ⇒ `condicao` nula.
4. Identidade da condição materializada com a condição aprovada, quando houver.

Nota de implementação sobre o teste 3: ele **não pode morar no schema do N2**, porque `tipo` fica no Claim Kit e não viaja para o vínculo — o §11 está certo em não copiá-lo. É checagem de materialização, que lê as duas pontas: o claim e o vínculo produzido. Cabe no portão L-05, junto com ancoragem textual e deduplicação.

## 2.5 H-2 — de onde sai a direção efetiva

A pergunta da casa é a certa, e hoje a resposta é: **de lugar nenhum.** O SCHEMA-CLAIM v1.2 não tem eixo de direção. `achado` é o efeito numérico, `nivel` é o peso da fonte no claim, `comparador` é contra o quê se mediu. Nenhum dos três diz se a fonte sustenta, refuta ou é inconclusiva quanto à afirmação.

Deixar assim obrigaria o materializador a inferir direção a partir de prosa — exatamente o que acabamos de proibir, só que num campo diferente. A D1 seria fechada e reaberta em outro lugar.

**Mas o campo não precisa ser inventado. Ele já existe no projeto.**

O SCHEMA-CLAIM v3.1, da trilha mecanística, define dentro de `relacoes_causais_declaradas`:

```
sentido_do_achado: suporta_relacao | refuta_relacao | inconclusivo
```

marcado como OBRIGATÓRIO, com a justificativa de capturar achado negativo. Os três valores mapeiam um a um para `sustenta`, `refuta` e `inconclusivo`.

**Recomendação:** o contrato de saída do kit clínico importa `sentido_do_achado` da v3.1, por fonte, com o mesmo vocabulário e sem renomear. Não é campo novo, é vocabulário já normativo na trilha irmã — o que evita a segunda semântica que todos os lados querem impedir.

O quarto valor, `condicional`, não vem daí: nasce da classificação da ressalva, como o Comentador desenhou. Os dois caminhos convergem no mesmo campo sem se sobrepor, porque respondem em momentos diferentes — a direção vem da fonte, a condicionalidade vem da ressalva classificada.

---

# 3. UMA CORREÇÃO AO §4.4, A FAVOR DA SOLUÇÃO

O §4.4 diz: *"Quando houver eixo de maturidade aplicável no contrato N2, ele poderá representar a limitação."*

**Ele já existe.** Medi: o N2 v1.4 tem `grau_maturidade`, com enum `muito_estabelecido | bem_suportado | moderadamente_suportado | emergente | hipotese_inicial`, e está preenchido em 274 de 274 vínculos do acervo mecanístico.

Isso importa porque remove a última tentação estrutural que restava. A ressalva de maturidade não fica sem casa: a casa dela é `grau_maturidade`, e "achado preliminar baseado em coorte única" tem valor próprio nesse enum. Ninguém precisa recorrer a `condicional` para não perder a informação.

A ressalva do lado do kit é a mesma da H-2: o SCHEMA-CLAIM v1.2 não tem esse campo, enquanto a v3.1 tem — lá chamado `grau_maturidade_cientifica`, com o mesmo enum. Vale importar junto, pelo mesmo motivo.

Duas observações de fronteira, para não gerar trabalho indevido:

- **Não proponho exigir isso para fechar D1.** É item do contrato de saída do kit, no ciclo dele.
- **`forca_causal` é diferente e não deve ser importada.** Mede manipulação experimental, não se aplica a evidência clínica associativa, e sua ausência em vínculo clínico significa não aplicável — conforme já registrei em 23/09.

---

# 4. E-6 — CONCORDO COM O FECHAMENTO EM DUAS CAMADAS

A distinção do §10 é a correta e resolve o que eu tinha deixado em aberto: classificar é decisão científica, preservar é comparação mecânica. A objeção contra autoauditoria continua valendo para a primeira e não alcança a segunda.

Acrescento a condição que já tinha declarado: a checagem de preservação é minha desde que eu não escreva o materializador. Se escrever, ela sai da minha mão junto.

---

# 5. SOBRE AS RESSALVAS DA CASA

**H-1** — concordo integralmente. `ressalvas[]` com `tipo` é contrato do Claim Kit, no ciclo do kit e com palavra do operador. Não pressuponho vigência, e nada do meu parecer depende de que esteja fechado. O teste 3 do §2.4 só se torna executável quando o campo existir; até lá ele fica especificado e inerte.

**H-2** — respondida no §2.5. Item de contrato, não impedimento.

**H-3** — registrado. Subscrevo sem ressalva justamente para não deixar D1 aberta por item que pertence a outro ciclo.

---

# 6. O QUE CONSIDERO CONSOLIDADO DO MEU LADO

A lista do §18 do Comentador é compatível com tudo que o meu território protege. Acrescento que continuam válidos, e não são tocados por D1: ordem Biblioteca → N2 como precondição estrutural, deduplicação por PMID, escopo da âncora determinado pelo destino da frase, política de numeração dos vínculos clínicos ainda a fixar, e a correção do §E.4 sobre colisão de identificador.

---

*Parecer territorial. Subscrevo sem ressalva. A regra abolida era minha, e a abolição está correta.*
