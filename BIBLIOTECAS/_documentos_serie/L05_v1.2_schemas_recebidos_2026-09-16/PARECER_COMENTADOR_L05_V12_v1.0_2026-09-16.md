```
Claro. Abaixo está o parecer já em formato formal, com a posição do **Comentador Externo** claramente separada da autoridade do Auditor de Estrutura, da Casa e da decisão do responsável pelo projeto. Também incorporei a verificação técnica externa apenas para os pontos relativos ao comportamento do JSON Schema. ([JSON Schema][1])

# PARECER DO COMENTADOR EXTERNO

## L-05 — Schema de Evidência e Vínculo com Ancoragem Multi-Entidade

**Versão do parecer:** 1.0
**Data:** 16/09/2026
**Objeto:** L-05 v1.2 — proposta submetida pelo Auditor de Estrutura
**Instância:** Comentador Externo — ChatGPT
**Natureza:** parecer técnico externo, não normativo
**Autoridade decisória:** Responsável pelo Projeto / Operador
**Verificação independente:** Arena / Casa
**Autoridade do contrato de execução:** Auditor-Mestre

---

## 1. OBJETO DO PARECER

Este parecer analisa a proposta **L-05 v1.2 — Schema de Evidência e Vínculo com Ancoragem Multi-Entidade**, juntamente com os resultados de execução apresentados pelo Auditor de Estrutura contra o acervo real B1 V7.

A análise considera também o mapa de autoridade e comunicação da plataforma, segundo o qual:

* o Auditor de Estrutura é responsável pelo contrato dos dados;
* o Auditor-Mestre é responsável pelo contrato de execução do Motor;
* a Arena/Casa é a bancada independente de verificação;
* o Comentador Externo produz esclarecimentos e minutas, sem autoridade final;
* o Operador é o responsável pela decisão de adoção;
* especialistas humanos permanecem como instância de revisão final.

Este parecer, portanto, **não substitui nenhuma dessas autoridades**.

Seu objetivo é identificar:

1. o que está tecnicamente bem fundamentado;
2. o que pode ser considerado resolvido em nível estrutural;
3. o que ainda depende de decisão do responsável pelo projeto;
4. o que deve permanecer como dívida ou bloqueador;
5. quais condições devem ser satisfeitas antes de o L-05 tornar-se normativo.

---

# 2. CONCLUSÃO EXECUTIVA

A análise do Auditor de Estrutura demonstra uma evolução significativa do L-05.

A proposta não se limita a acrescentar campos. Ela corrige problemas de modelagem identificados por execução contra dados reais e, em vários pontos, substitui inferências implícitas por relações explicitamente representadas.

A direção arquitetural do L-05 v1.2 é considerada **tecnicamente consistente e adequada para prosseguir para a fase de fechamento normativo**, desde que as decisões e pendências identificadas neste parecer sejam formalmente encerradas.

Entretanto, **não considero apropriado declarar o L-05 v1.2 integralmente normativo neste momento**.

A classificação adequada é:

> **L-05 v1.2 — proposta estrutural tecnicamente aprovada para fechamento, ainda não congelada como norma.**

Essa distinção é necessária porque permanecem decisões que não pertencem ao Auditor de Estrutura e não podem ser resolvidas silenciosamente pelo schema.

---

# 3. PRINCÍPIO CENTRAL CONFIRMADO

O aspecto mais importante do ciclo é a confirmação de que o problema do L-05 não deve ser tratado como simples organização de campos.

O processo revelou uma separação necessária entre:

```text
ESTRUTURA DO DADO
        ↓
SEMÂNTICA DO DADO
        ↓
PROVENIÊNCIA
        ↓
RELAÇÃO EPISTÊMICA
        ↓
EXECUÇÃO PELO MOTOR
```

Essas camadas não devem ser confundidas.

O JSON Schema é apropriado para expressar restrições estruturais, tipos, propriedades obrigatórias e conjuntos fechados de valores. `enum`, por exemplo, restringe um valor a um conjunto explicitamente definido; já regras semânticas mais complexas ou dependentes de conteúdo podem exigir portões externos ao schema. ([JSON Schema][2])

Essa distinção está corretamente refletida na evolução do L-05.

---

# 4. PARECER SOBRE A SEPARAÇÃO `natureza_evidencia` × `desenho_estudo`

Considero esta alteração **estruturalmente correta**.

O problema identificado é real:

```text
review
```

não descreve adequadamente a natureza da evidência.

Uma revisão pode reunir estudos:

* humanos;
* animais;
* in vitro;
* post mortem;
* mistos.

Portanto, são eixos diferentes:

```text
natureza_evidencia
→ quem/o que foi estudado

desenho_estudo
→ como o estudo ou conjunto de estudos foi produzido/analisado
```

A preservação de:

```text
desenho_estudo_bruto
```

também deve ser mantida.

Ela fornece rastreabilidade entre a classificação normativa e o valor original utilizado para produzi-la:

```text
valor original
      ↓
desenho_estudo_bruto
      ↓
classificação
      ↓
auditoria
```

### Parecer

**Aceito como direção estrutural.**

Os 30 registros atualmente classificados como `review` devem, entretanto, permanecer em fila de classificação humana até que o manual de classificação esteja formalmente fechado.

---

# 5. PARECER SOBRE A MULTI-ANCORAGEM

A transformação de uma âncora única em uma estrutura de:

```text
ancora_principal
+
ancoras[]
```

é considerada uma evolução arquitetural importante.

Ela resolve uma limitação da representação anterior, na qual uma evidência podia ficar artificialmente vinculada a apenas uma entidade.

O modelo proposto permite representar:

```text
EVIDÊNCIA
│
├── mecanismo
│
├── biomarcador
│
└── cenário
```

sem duplicar a referência bibliográfica.

Isso é particularmente compatível com a arquitetura geral da plataforma, na qual os 146 IDs oficiais constituem entidades de diferentes domínios.

### Parecer

**Aceito como direção arquitetural.**

A implementação, entretanto, depende da existência de um catálogo operacional confiável dos IDs oficiais.

---

# 6. PARECER SOBRE `ancora_principal`

A mudança de:

```text
principal: true/false
```

para:

```text
ancora_principal: "ID"
```

é tecnicamente adequada.

Ela elimina a necessidade de contar quantos elementos de uma lista receberam `principal=true`.

O contrato passa a representar diretamente:

> existe um identificador principal para o vínculo.

O JSON Schema consegue exigir a presença de uma propriedade, mas determinadas relações entre múltiplos objetos e cardinalidades semânticas podem continuar exigindo um portão de integridade externo. ([JSON Schema][2])

A proposta, portanto, reduz a complexidade do portão sem eliminar a necessidade de validação de integridade referencial.

### Parecer

**Aceito.**

A validação de:

```text
ancora_principal ∈ catálogo_oficial
```

deve permanecer como requisito de portão.

---

# 7. PARECER SOBRE `papel` × `direcao_suporte`

Considero esta uma das correções mais importantes do ciclo.

O modelo anterior permitia uma ambiguidade perigosa:

```text
papel = sustenta_intervencao
```

poderia ser interpretado indevidamente como:

> a intervenção é eficaz.

A nova separação estabelece:

```text
papel
→ qual é a relação temática da evidência com a entidade

direcao_suporte
→ qual é a direção da relação epistêmica
```

Assim:

```text
papel = sustenta_intervencao
direcao_suporte = refuta
```

é semanticamente possível.

Também é possível:

```text
papel = sustenta_intervencao
direcao_suporte = condicional
```

Isso impede que o Motor utilize o nome do papel como substituto de um julgamento epistêmico.

### Parecer

**Aceito integralmente como princípio estrutural.**

A regra deve ser incorporada explicitamente ao contrato do Motor:

> `papel` isoladamente nunca constitui evidência de eficácia, causalidade, utilidade clínica ou direção do efeito.

---

# 8. PARECER SOBRE `direcao_suporte`

Considero correta a recusa apresentada pelo Auditor de Estrutura em converter automaticamente todos os casos:

```text
CONFIRMADO → sustenta
```

O caso utilizado como teste — `REF_RAISON_2013` — demonstra que confirmação da relação documental não equivale necessariamente a suporte simples e incondicional.

Uma evidência pode estar confirmada e, ainda assim, apresentar:

```text
condicionalidade
subgrupo
efeito restrito
resultado negativo global
heterogeneidade
```

Portanto:

```text
status_auditoria
        ≠
direcao_suporte
```

é uma distinção que deve permanecer.

O aumento da fila humana de 1 para 102 registros não deve ser interpretado como falha do schema.

É consequência de uma regra mais conservadora.

### Parecer

**Aceito o princípio conservador.**

A fila humana deve ser preservada como estado explícito, e não convertida artificialmente em valores positivos para aumentar a conformidade automática.

---

# 9. PARECER SOBRE `uso` E AS DUAS TRILHAS

Este é um dos pontos que considero mais importantes para decisão do Operador.

A execução revelou que o problema original não era simplesmente um conjunto de valores inválidos.

Havia duas trilhas normativas:

```text
TRILHA CLÍNICA
clinico
contexto_mecanistico
gap_pesquisa

TRILHA MECANÍSTICA
nucleo_causal
suporte_correlacional
gap_pesquisa
```

Portanto, validar um conjunto de registros pertencente a uma trilha contra o enum de outra produz falso diagnóstico.

### Parecer

**Não recomendo unificar artificialmente os dois vocabulários.**

A direção proposta pelo Auditor de Estrutura — explicitar:

```text
trilha
```

e interpretar:

```text
uso
```

de acordo com a trilha — é arquiteturalmente mais coerente.

A decisão final, entretanto, pertence ao Operador.

---

# 10. PARECER SOBRE `B1_v2`

A identificação de:

```text
uso = B1_v2
```

como informação de procedência, e não como uso semântico, é consistente.

A separação:

```text
uso
```

versus:

```text
leva_origem
```

preserva dois eixos distintos:

```text
uso
→ significado do vínculo

leva_origem
→ procedência de produção
```

### Parecer

**Aceito.**

A migração deve ser feita somente depois do fechamento do contrato.

---

# 11. PARECER SOBRE `status_auditoria` EM N1 E N2

A colisão semântica identificada é real.

O mesmo nome está sendo utilizado para:

```text
N1
estado da validação da referência
```

e:

```text
N2
estado da relação evidência ↔ afirmação
```

São conceitos diferentes.

A proposta de:

```text
N1:
status_validacao

N2:
status_auditoria
```

é adequada.

A manutenção temporária do nome anterior como alias `deprecated` também é compatível com uma estratégia de migração não destrutiva.

### Parecer

**Aceito como direção de migração.**

O alias deve possuir condição explícita de aposentadoria e não pode permanecer indefinidamente como segunda fonte de verdade.

---

# 12. PARECER SOBRE `citacao_confirmada`

A decisão de não remover imediatamente o campo é correta.

O problema é de proveniência:

```text
237/237 = true
```

sem origem conhecida.

Não se deve:

1. transformar esse campo em portão;
2. assumir que o valor é confiável;
3. apagá-lo apenas porque sua origem não foi localizada.

A sequência correta é:

```text
preservar
→ auditar origem
→ registrar resultado
→ decidir destino
```

### Parecer

**Permanece como dívida nomeada.**

Não deve influenciar a decisão epistêmica do Motor enquanto sua proveniência não estiver estabelecida.

---

# 13. O CATÁLOGO DOS 146 IDs É O PRINCIPAL BLOQUEADOR OPERACIONAL

Este ponto merece tratamento separado.

O L-05 depende de:

```text
id_oficial
      ↓
catálogo oficial
```

Entretanto, a própria auditoria identificou diferença entre:

```text
146 IDs declarados
```

e:

```text
103 IDs capturados pelo parser
```

Essa diferença não deve ser silenciosamente resolvida por normalização.

Antes do congelamento, deve ocorrer:

```text
fonte declarada
       ↓
derivador
       ↓
146 IDs
       ↓
contagem por categoria
       ↓
conferência
       ↓
hash / versão
       ↓
catálogo operacional
```

Somente depois o L-05 poderá depender desse catálogo como fonte de validação.

### Parecer

**Bloqueador de fechamento normativo.**

Não bloqueia a direção do schema, mas bloqueia sua declaração como contrato operacional completo.

---

# 14. PARECER SOBRE A EXECUÇÃO CONTRA O ACERVO REAL

Considero este um ponto forte do trabalho do Auditor de Estrutura.

A proposta foi efetivamente confrontada com:

```text
B1 V7
237 referências
274 vínculos
```

e a execução encontrou problemas que não estavam evidentes na prosa.

Isso inclui:

* valores de enum não previstos;
* colisões de nomes;
* problemas de classificação;
* regras automáticas excessivamente agressivas;
* discrepâncias de procedência;
* necessidade de triagem humana;
* diferenças entre contratos clínicos e mecanísticos.

Isso demonstra que a proposta não está sendo tratada apenas como documentação.

Está sendo tratada como **especificação executável e auditável**.

### Parecer

**Método de validação aprovado como princípio.**

A execução contra o acervo deve continuar sendo requisito para qualquer mudança relevante do L-05.

---

# 15. PARECER SOBRE A FILOSOFIA “ESPECIFICAÇÃO QUE NÃO RODA É OPINIÃO”

A formulação é forte, mas o princípio subjacente é correto para este projeto:

> uma especificação estrutural destinada a governar dados deve ser testada contra dados reais.

Entretanto, é necessário manter uma distinção:

```text
schema válido
≠
dado semanticamente correto
```

O JSON Schema pode validar estrutura, tipos, enums e outras restrições declarativas; não deve ser tratado como substituto de auditoria semântica ou científica. ([JSON Schema][1])

Portanto, a arquitetura correta permanece:

```text
SCHEMA
+
PORTÕES
+
AUDITORIA SEMÂNTICA
+
REVISÃO HUMANA
```

e não:

```text
SCHEMA = verdade científica
```

---

# 16. PARECER SOBRE OS 102 CASOS EM FILA HUMANA

O resultado:

```text
172 automáticos
102 humanos
```

não deve ser “otimizado” artificialmente.

A redução da fila não é objetivo em si.

O objetivo é:

> somente atribuir `direcao_suporte` quando existir base suficiente para fazê-lo.

Assim, a existência de uma fila humana é um estado legítimo do sistema.

A fila deve possuir:

* identificação do registro;
* motivo da pendência;
* regra que impediu a automação;
* responsável pela resolução;
* resultado;
* data;
* eventual referência à decisão.

Isso transforma a revisão humana em parte rastreável da cadeia, e não em edição manual invisível.

---

# 17. PARECER SOBRE O PAPEL DA CASA

A atuação da Casa descrita no documento é compatível com a governança estabelecida.

A Casa não deve funcionar como autora do L-05.

Sua função é:

```text
RECEBER
   ↓
REPRODUZIR
   ↓
MEDIR
   ↓
VERIFICAR
   ↓
REGISTRAR
```

A Casa pode identificar que:

> o schema está errado.

Mas não deve, por isso, adquirir automaticamente autoridade para definir a ciência ou alterar a arquitetura.

Da mesma forma:

> o Auditor de Estrutura ter produzido o schema não significa que ele possa aprová-lo sozinho.

Essa separação deve permanecer.

---

# 18. PARECER SOBRE A RELAÇÃO COM O MOTOR

O documento confirma adequadamente que:

```text
L-05
=
contrato de dados
```

enquanto:

```text
Contrato do Motor
=
contrato de execução
```

O Motor pode consumir os campos definidos pelo L-05, mas não deve modificar a semântica deles por interpretação própria.

Particularmente, o Motor não deve inferir:

```text
papel
→ eficácia

ancora_principal
→ maior força científica

status_validacao
→ maior evidência

leva_origem
→ maior confiabilidade

ancoragem em exame
→ utilidade clínica
```

Essas inferências devem ser proibidas.

---

# 19. REGRA ADICIONAL RECOMENDADA

Recomendo acrescentar ao contrato uma regra transversal:

> **Campos de proveniência, curadoria, organização de produção, auditoria ou estado administrativo não podem, isoladamente, ser interpretados pelo Motor como evidência de eficácia, causalidade, utilidade clínica ou aumento da força epistêmica de uma afirmação.**

Em termos conceituais:

```text
PROVENIÊNCIA
      ≠
EPISTEMOLOGIA

EPISTEMOLOGIA
      ≠
CAUSALIDADE

CAUSALIDADE
      ≠
DECISÃO CLÍNICA
```

Essa regra protegerá o Motor contra uma classe inteira de inferências indevidas.

---

# 20. QUESTÕES QUE DEVEM SER DECIDIDAS PELO OPERADOR

Após a análise, considero que as seguintes questões permanecem legitimamente pertencentes ao responsável pelo projeto:

### D1 — `uso` e `trilha`

Decidir se serão formalizadas duas trilhas:

```text
clinica
mecanistica
```

com seus respectivos vocabulários.

**Posição deste parecer:** a separação é tecnicamente preferível à unificação artificial.

---

### D2 — os 30 `review`

Decidir a política de classificação.

**Posição deste parecer:** realizar a triagem humana antes do congelamento do campo.

---

### D3 — retroancoragem B1

Decidir se:

```text
B1
```

será retroancorado antes da entrada de B2 ou se o novo contrato começará pelos novos mecanismos.

**Posição deste parecer:** a decisão deve considerar a necessidade de coerência do piloto vertical B1. Se B1 é o piloto de referência, existe justificativa arquitetural para concluir sua retroancoragem antes de expandir o modelo.

---

### D4 — `citacao_confirmada`

Manter em estado pendente até auditoria de proveniência.

---

### D5 — catálogo operacional dos 146 IDs

Resolver a diferença:

```text
146 declarados
vs.
103 capturados
```

antes de tornar a validação referencial definitiva.

**Esta é a principal condição técnica de fechamento.**

---

# 21. CONDIÇÕES PARA O L-05 SE TORNAR NORMATIVO

Minha recomendação é que o L-05 só passe de:

```text
PROPOSTA
```

para:

```text
NORMATIVO
```

quando forem satisfeitas, no mínimo, as seguintes condições:

```text
[ ] catálogo operacional dos 146 IDs validado

[ ] decisão formal sobre as duas trilhas de uso

[ ] 30 registros review classificados ou política transitória formalizada

[ ] política de retroancoragem B1 registrada

[ ] destino de citacao_confirmada decidido

[ ] migração N1/N2 executada

[ ] alias deprecated com regra de aposentadoria registrada

[ ] B1_v2 separado para leva_origem

[ ] regra de direcao_suporte aprovada

[ ] fila humana documentada e rastreável

[ ] execução final do schema contra o acervo

[ ] resultado final reproduzível pela Casa

[ ] sha/manifests atualizados

[ ] nenhuma divergência estrutural não explicada
```

---

# 22. DECISÃO DO PARECER

Após análise do material apresentado, **não identifico fundamento técnico para rejeitar a arquitetura proposta pelo L-05 v1.2**.

Ao contrário, considero que as principais mudanças estruturais representam uma melhoria clara na separação de:

* natureza da evidência;
* desenho;
* uso;
* procedência;
* ancoragem;
* papel;
* direção epistêmica;
* estado de validação.

Entretanto, também não considero adequado declarar o L-05 definitivamente aprovado como norma neste momento.

### Formulação formal recomendada:

> **PARECER: FAVORÁVEL À DIREÇÃO ESTRUTURAL DO L-05 v1.2, COM APROVAÇÃO CONDICIONADA AO FECHAMENTO DAS DECISÕES NORMATIVAS E DOS BLOQUEADORES OPERACIONAIS IDENTIFICADOS.**
>
> **O L-05 v1.2 pode prosseguir como proposta técnica de fechamento e migração controlada, mas não deve ser declarado contrato normativo definitivo até que as condições de fechamento sejam verificadas pela Casa e as decisões pertencentes ao responsável pelo projeto sejam formalmente registradas.**

---

# 23. REGRA DE AUTORIDADE DESTE PARECER

Este documento não altera:

* o L-05;
* o Contrato do Motor;
* a Biblioteca Canônica;
* o catálogo de IDs;
* os dados B1;
* os gates da Casa;
* as decisões arquiteturais.

Ele constitui apenas:

```text
PARECER EXTERNO
      ↓
ANÁLISE
      ↓
RECOMENDAÇÕES
      ↓
DECISÃO DO OPERADOR
      ↓
VERIFICAÇÃO DA CASA
```

Nenhuma recomendação deste parecer deve ser incorporada automaticamente.

---

# 24. REGISTRO FINAL

A análise do ciclo demonstrou algo relevante para a arquitetura geral da plataforma:

> **o sistema está começando a distinguir adequadamente conhecimento, representação, proveniência, relação epistêmica, execução e decisão profissional.**

Essa separação é fundamental para que o futuro Motor Clínico possa operar sobre um estoque estruturado sem transformar lacunas de dados em conclusões, sem elevar força de evidência por inferência e sem confundir organização do conhecimento com decisão clínica.

O próximo passo correto, portanto, não é ampliar o L-05 indefinidamente.

É **fechar as decisões pendentes, verificar o catálogo dos 146 IDs, executar a migração controlada e permitir que a Casa reproduza o resultado antes do congelamento normativo.**

**Fim do Parecer.**

Esse documento já está no formato que eu recomendaria colocar na **ponte formal**: ele não “manda” no Auditor de Estrutura nem na Casa; registra a minha análise, separa o que considero tecnicamente resolvido do que ainda depende de você e deixa condições objetivas para o fechamento.

[1]: https://json-schema.org/draft-07/json-schema-core?utm_source=chatgpt.com "JSON Schema: A Media Type for Describing JSON Documents"
[2]: https://json-schema.org/draft-07/draft-handrews-json-schema-validation-01?utm_source=chatgpt.com "JSON Schema Validation: A Vocabulary for Structural Validation of JSON"
```
