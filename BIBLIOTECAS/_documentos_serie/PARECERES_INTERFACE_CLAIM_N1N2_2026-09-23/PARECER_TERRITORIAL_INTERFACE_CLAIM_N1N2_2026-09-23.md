# PARECER TERRITORIAL — INTERFACE CLAIM CLÍNICO → BIBLIOTECA → N1/N2

**Data:** 2026-09-23 · **Em resposta à pergunta da carta §16, na redação mantida pela Arena §3**
**Escopo:** arquitetura, schemas, materialização, N1/N2. Não aprovo o COMO EXECUTAR v1.9 nem delibero sobre filosofia ou protocolo de IAs.
**Medido contra:** N1 v1.3 `b06660fd…` · N2 v1.4 `d96ad15b…` · acervo B1 V7 (274 vínculos · 237 fichas · canônica)

---

# 1. VEREDITO

**A solução é compatível. Não há impedimento técnico nem epistemológico.**

Os seis itens da minuta de contrato da Arena (§3) são compatíveis com o N1 v1.3 e o N2 v1.4 como estão. A leitura de engenharia está correta: padronização de saída, extensão mínima do kit no passo de entrada na Biblioteca, e uma alteração pontual de enum. Nada arquitetural novo.

Registro quatro pontos do meu território que a classificação não fechou — **nenhum é impedimento**; três são itens de contrato a declarar antes da primeira materialização, e um é uma correção a uma regra proposta.

---

# 2. CORREÇÃO A UMA REGRA PROPOSTA

## §E item 4 — colisão de `id_referencia_interna` não deve ser falha dura

A Arena propõe: *"Colisão de `id_referencia_interna` (PMID novo × mesmo id legado) → falha dura da materialização"*.

Isso reprovaria o caso normal. `REF_SOBRENOME_ANO` colide sempre que dois artigos distintos compartilham primeiro autor e ano — situação corriqueira em literatura de um mesmo grupo. O N1 v1.3 já resolve: o padrão é `^REF_[A-Z0-9_]+[a-z]?$`, e o sufixo minúsculo existe exatamente para desambiguar. O acervo já usa — `REF_CAPURON_2002b`, `REF_CHEN_2024b`, `REF_CHEN_2024c`.

Regra correta, em dois graus:

- **PMID novo, id já ocupado** → alocar próximo sufixo livre. Operação mecânica, sem intervenção.
- **Mesmo id apontando para dois PMIDs diferentes depois da alocação** → aí sim falha dura, porque é corrupção de chave.

O que nunca pode acontecer é o inverso: dois ids distintos para o mesmo PMID. Esse é o caso que a deduplicação por `pmid_oficial` impede.

---

# 3. TRÊS ITENS A DECLARAR NO CONTRATO

## 3.1 O `escopo` da âncora clínica — resolvido pela própria ordem, mas precisa estar escrito

O `escopo` da âncora é hoje `BLOCO_XX[/sub]` para mecanismo, mais o valor reservado `APENDICE_CORPUS`. Um claim clínico nasce em `B1.SM02.xxx` — e `SM-02` não está nesse vocabulário.

A tentação seria acrescentar `SM-02` ao escopo. Seria erro: o escopo descreve subdivisão **da entidade**, e a entidade é o mecanismo, cuja biblioteca é dividida em BLOCOs, não em submódulos de trabalho.

A regra H resolve sozinha. Como a afirmação entra na Biblioteca **antes** do N2, ela aterrissa em algum BLOCO — e o escopo da âncora é **o BLOCO onde a frase caiu**, não o submódulo de origem do claim. A proveniência do trabalho clínico continua registrada em `claim_id`, que já carrega `SM02`.

Isso é mais um efeito da ordem Biblioteca → N2, e vale declarar no contrato: **o escopo da âncora é determinado pelo destino da frase, nunca pela origem do claim.** Sem isso, a primeira materialização vai inventar um valor.

## 3.2 Numeração de `id_vinculo` — o padrão aceita, mas a série precisa de política

Testei o padrão `^VINC_[A-Z0-9]+_[0-9]{4}$` contra candidatos:

| candidato | resultado |
|---|---|
| `VINC_B1_0275` | aceita — **e colide com a série mecanística** |
| `VINC_B1SM02_0001` | aceita |
| `VINC_B1CLIN_0001` | aceita |
| `VINC_B1.SM02_0001` | rejeita — ponto não é permitido |
| `VINC_B1_10001` | rejeita — o contador é fixo em 4 dígitos |

O acervo usa dois prefixos: `VINC_B1` (244) e `VINC_B1V2` (30). Continuar a série `VINC_B1_` a partir de 0275 é sintaticamente válido e **é a pior opção**: mistura duas trilhas num mesmo espaço de numeração, e a origem deixa de ser legível no identificador.

Recomendo prefixo próprio para a trilha clínica. Não proponho qual — é decisão de quem mantém a série. Mas o contrato precisa fixá-lo antes da primeira materialização, porque identificador atribuído não se renumera depois sem quebrar tudo que já citou.

Segundo ponto, menor e com prazo longo: o contador de quatro dígitos limita cada prefixo a 9.999 vínculos. B1 tem 274. Não é problema hoje; é problema se algum dia uma entidade passar disso e alguém precisar mudar o padrão com acervo em produção.

## 3.3 Os eixos mecanísticos vão ficar vazios nos vínculos clínicos — e isso precisa ser declarado

Este é o único ponto com risco epistemológico, e é por omissão, não por conflito.

Medi no V7: `forca_causal` está em **274 de 274**, e `grau_maturidade` em **274 de 274**. Os dois são opcionais no N2 v1.4, e nenhum dos dois existe no SCHEMA-CLAIM v1.2 — são eixos da trilha mecanística, definidos na v3.1.

Consequência: depois da primeira materialização clínica, esses dois campos deixam de estar em 100% dos vínculos de B1. Passam a estar presentes nos mecanísticos e ausentes nos clínicos.

Isso é **correto por desenho** — força causal é pergunta de manipulação experimental, e não se aplica a evidência clínica associativa. Mas cria uma armadilha de leitura rio abaixo:

> Um consumidor que hoje encontra `forca_causal` em todos os registros pode tratar ausência como fraqueza, quando ela significa não-aplicabilidade.

A distinção entre "tier baixo" e "eixo não aplicável" é exatamente o tipo de colapso que a arquitetura inteira existe para impedir. Hoje ela não pode acontecer porque não há caso; depois da materialização, passa a poder.

**Recomendação:** declarar no contrato que a ausência de `forca_causal` e `grau_maturidade` em vínculo com `trilha: clinica` significa **não aplicável**, nunca grau mínimo. E que nenhum portão, motor ou relatório pode inferir força a partir da ausência.

Não proponho campo novo para isso. O `trilha` já discrimina: quem lê `trilha: clinica` sabe qual conjunto de eixos se aplica. Falta a regra dizer isso em voz alta.

---

# 4. SOBRE OS PONTOS QUE A ARENA DEIXOU EM ABERTO NO MEU TERRITÓRIO

## 4.1 E-6 — portão de fidelidade da ressalva × invariante da r76

A preocupação é legítima mas não se aplica a esta checagem. Comparar `claim.nota_ressalva` com toda `condicao` derivada é **comparação de duas cópias**, não julgamento de fidelidade. Detecta divergência introduzida por edição ou suavização; não opina sobre se a ressalva está certa.

O invariante da r76 dispara quando o mesmo agente **escreve a regra e julga a aderência a ela**. Aqui eu não escrevo o materializador. Se algum dia eu escrever, a checagem sai da minha mão junto.

Proponho fechar E-6 assim: instrumento mecânico do Estrutura, com a condição declarada de que quem executa não escreveu o materializador.

## 4.2 Confirmação do §10 — `claim_id_origem`

Confirmo, medido no schema: `claim_id_origem` é `type: string`, escalar. Não comporta catálogo. A leitura da Arena está certa, inclusive na parte mais importante — **não reescrever `claim_id_origem` de N1 legado para "fazer bater"**. A origem é o nascimento; o uso vive em N2 via `claim_id`. Reescrever seria falsificar proveniência para satisfazer uma consulta.

## 4.3 Um detalhe do quadro A que vale corrigir

A tabela A mapeia `evidence_role` para *"`natureza_evidencia` / `evid_role` do acervo"*. Conferi: **`evid_role` não é propriedade do N1 v1.3** — existe no acervo legado, não no schema. Um N1 novo criado pelo kit deve preencher `natureza_evidencia` e não deve receber `evid_role`, sob pena de nascer com campo que o contrato não conhece.

O mapeamento `human_clinical → humana_observacional` continua sujeito à guarda determinística do schema: se o `desenho_estudo_bruto` trouxer marcador intervencional, a ficha não migra automaticamente. Para N1 criado do zero isso é barato, porque o desenho é lido da fonte primária no ato.

---

# 5. O QUE CONTINUA VALENDO DA RODADA 3

Sem alteração: a ordem Biblioteca → N2 é precondição estrutural, não preferência (E-1); a deduplicação por PMID é regra de materialização; a ressalva tem mapeamento único e reprova se ausente; e a fidelidade claim→N1→N2 não pode ficar com quem produz a materialização.

A ancoragem textual, que hoje vale 274 de 274 por disciplina, deve virar portão antes da primeira leva clínica — é a checagem que detecta o vínculo órfão sem ler nada.

---

*Parecer territorial. Compatível, sem impedimento. Os quatro pontos acima são itens de contrato, não objeções.*
