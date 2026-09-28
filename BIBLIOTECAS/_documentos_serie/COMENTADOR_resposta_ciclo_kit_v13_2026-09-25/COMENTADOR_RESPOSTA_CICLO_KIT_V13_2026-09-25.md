# RESPOSTA DO COMENTADOR À ARENA CASA

## CICLO DO KIT — SCHEMA-CLAIM v1.3

**Data:** 2026-09-25
**Origem:** Comentador
**Objeto:** avaliação da minuta SCHEMA-CLAIM v1.3 — P-K1/P-K2/P-K3/P-K5
**Base:** contrato de saída rev.2 + Schema-Claim v1.2 + Schema-Claim Mecanismo v3.1 + TRILHA97

---

# 1. VEREDITO

**A minuta v1.3 cobre corretamente P-K1, P-K2, P-K3 e P-K5 e pode seguir para os dois auditores.**

A arquitetura proposta é compatível com o contrato de saída já encerrado e respeita o princípio de **mínima alteração suficiente**.

A v1.3:

* preserva a baseline v1.2;
* não reabre o contrato rev.2;
* não altera N1/N2;
* importa somente os vocabulários necessários do v3.1;
* desloca as decisões científicas para o fechamento do Claim;
* impede inferência posterior pelo materializador;
* mantém P-K6 como dependência estrutural futura do N2 v1.5.

A TRILHA97 confirma os 13 testes declarados.

---

# 2. P-K1 — SENTIDO DO ACHADO

**Aprovado para o ciclo.**

A escolha de importar literalmente:

```text
suporta_relacao
refuta_relacao
inconclusivo
```

do Schema-Claim Mecanismo v3.1 é correta.

Não deve ser criado um segundo vocabulário clínico equivalente.

A decisão é cientificamente tomada no fechamento do Claim e apenas posteriormente transformada em:

```text
suporta_relacao → sustenta
refuta_relacao → refuta
inconclusivo → inconclusivo
```

no N2.

A regra de fail-closed também está correta:

> ausência de `sentido_do_achado` em Claim elegível para materialização = Claim não fechado / falha de materialização.

Não existe default permitido.

Isso atende simultaneamente:

**engenharia:** nenhuma inferência implícita;

**ciência:** direção da relação é decidida com leitura da fonte;

**filosofia:** o sistema não inventa semântica para preencher estrutura.

---

# 3. P-K2 — RESSALVAS ESTRUTURADAS

**Aprovado para o ciclo.**

A estrutura:

```text
ressalvas[]
 ├── condicao_aplicacao
 ├── heterogeneidade
 └── maturidade_evidencia
```

é compatível com a solução D1 encerrada.

A regra mais importante está correta:

> a classificação da ressalva é decisão científica do fechamento, nunca inferência do materializador.

Também está correto manter `nota_ressalva` como sumário legível.

Ela não volta a ser fonte estrutural de `condicao`.

---

# 4. P-K3 — FONTE ÚNICA DE CONDIÇÃO

**Aprovado e deve permanecer exatamente assim.**

A única origem de `condicao` é:

```text
ressalvas[tipo = condicao_aplicacao].condicao
```

Não podem produzir `condicao`:

* `nota_ressalva`;
* `moderadores[]`;
* `sentido_do_achado`;
* status do Claim;
* nível da fonte;
* texto do `statement`.

Esse ponto é especialmente importante porque evita que a solução de D1 seja reaberta em outro campo.

O materializador deve somente copiar.

---

# 5. P-K5 — MATURIDADE

**Aprovado.**

A reutilização literal do vocabulário:

```text
muito_estabelecido
bem_suportado
moderadamente_suportado
emergente
hipotese_inicial
```

é adequada porque o mesmo eixo já existe no v3.1 e no N2.

A regra:

```text
maturidade_evidencia
→ grau_maturidade_cientifica
→ grau_maturidade no N2
```

mantém os eixos separados e não utiliza `condicional` como recipiente genérico para limitação de evidência.

---

# 6. MODERADORES

A preservação dos `moderadores[]` da v1.2 está correta.

Também está correta a trava:

```text
atenua  → permanece no Claim
amplifica → permanece no Claim
nulo → permanece no Claim
inverte → P-K6
```

Não devemos importar `forca_causal`, `forca_biologica_conexao` ou outros eixos do schema mecanístico apenas porque existem no v3.1.

Isso seria extrapolação de escopo.

---

# 7. UM AJUSTE DE PRECISÃO RECOMENDADO — V-K3

Há um único ponto que recomendo ajustar antes do congelamento final da minuta.

Atualmente:

> "fonte de claim fechado → `sentido_do_achado` presente"

A regra é correta para **fontes que participarão da materialização**.

Já `fontes_exploratorias` têm função informativa e não materializam.

Portanto, recomendo explicitar uma das duas intenções:

### Opção preferida

V-K3:

> **Toda fonte que participar da materialização deve possuir `sentido_do_achado`; fonte exploratória que não materializa pode permanecer fora dessa exigência.**

Se a governança quiser deliberadamente exigir direção também para fontes exploratórias, isso pode permanecer, mas deve ser declarado como **regra de qualidade do Claim Kit**, e não como requisito necessário ao N1/N2.

O ponto deve ser decidido agora para evitar que a validação futura interprete a ausência em exploratórias como erro de materialização.

---

# 8. MIGRAÇÃO

A regra de migração está correta.

Não reescrever retroativamente o corpus anterior.

O modelo deve ser:

```text
Claim existente v1.2
        ↓
próximo fechamento
        ↓
P-K1
P-K2
P-K5
        ↓
aptidão para materialização
```

Isso preserva a história do acervo e evita falsificar retroativamente decisões que não foram tomadas no momento original.

A falha dura para Claim antigo ainda sem fechamento compatível é apropriada **somente no momento em que ele tentar entrar na materialização**.

---

# 9. RELAÇÃO COM O CONTRATO REV.2

A v1.3 não deve reproduzir novamente o contrato de saída inteiro.

Ela deve apenas **implementar no Schema aquilo que o contrato já determinou**.

A distinção fica:

```text
Contrato rev.2
→ define o que o processo deve entregar

Schema v1.3
→ torna estruturalmente possível e verificável essa entrega
```

Isso mantém a separação entre norma operacional e estrutura de dados.

---

# 10. RELAÇÃO COM O SCHEMA MECANÍSTICO v3.1

A v1.3 está correta ao importar apenas:

* `sentido_do_achado`;
* `grau_maturidade_cientifica`.

Não deve importar automaticamente:

* `relacoes_causais_declaradas`;
* `forca_causal`;
* `classificador_tipo_fonte`;
* `forca_biologica_conexao`;
* `dominios_grade_observados`;
* `origem_da_evidencia`;
* `teste_conexao_fenotipo`.

Esses campos pertencem à semântica mecanística e não devem contaminar o namespace clínico.

A regra é:

> **reutilizar vocabulário comum quando o conceito é realmente comum; não importar estrutura apenas porque existe em outra trilha.**

---

# 11. VALIDAÇÃO DA MINUTA

A TRILHA97 demonstra:

**13/13 testes verdes.**

Isso é suficiente para considerar a minuta tecnicamente consistente com os critérios que a própria Arena estabeleceu para esta pré-rodada.

Não significa aprovação normativa.

Significa:

> **a minuta está suficientemente madura para receber a avaliação territorial.**

---

# 12. PRÓXIMO RITO

Minha recomendação é encaminhar agora a v1.3 aos dois auditores em janelas separadas, mantendo a pergunta territorial já definida.

### Auditor-Estrutura

Avaliar:

* sintaxe/estrutura;
* compatibilidade com N2/N1;
* coerência dos novos validadores;
* migração;
* possibilidade de implementação sem alteração indevida.

### Auditor-Mestre

Avaliar:

* suficiência científica das classificações;
* se P-K1 realmente impede fabricação de direção;
* se P-K2 preserva significado das ressalvas;
* se P-K5 não transforma maturidade em força ou condição;
* se a saída disponível ao materializador é suficiente para preservar o significado científico.

---

# 13. NÃO ABRIR NOVAMENTE D1

A Rodada 4 já encerrou D1.

O ciclo do Kit deve agora implementar:

```text
D1
 ↓
P-K1
P-K2
P-K3
P-K5
```

P-K6 permanece separado no ciclo N2 v1.5.

Não devemos reabrir a arquitetura de N1/N2 neste ciclo.

---

# 14. CONCLUSÃO DO COMENTADOR

**Minha recomendação é: levar a minuta v1.3 aos dois auditores, com apenas o ajuste de precisão do V-K3 acima.**

O desenho atual é coerente com a engenharia do sistema:

> **decisões científicas no Claim → estrutura de dados no Schema → cópia mecânica para N1/N2 → auditoria separada.**

E preserva a filosofia central do projeto:

> **quando uma informação não pode ser representada com segurança, ela não deve ser inventada, inferida silenciosamente nem comprimida em outro campo apenas para satisfazer o schema.**

P-K1 e P-K2 transformam justamente esse princípio em contrato executável.

Após a dupla avaliação da v1.3, o ciclo do Kit poderá ser encerrado e então a v1.10 poderá ser redigida com base em um contrato de saída efetivamente disponível.
