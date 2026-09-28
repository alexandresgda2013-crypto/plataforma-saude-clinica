# PARECER DO COMENTADOR EXTERNO

## Correção Arquitetural e L-05 v1.3

**Objeto:** Resposta à auditoria da Arquitetura Consolidada da Plataforma e avaliação do L-05 v1.3
**Destinatário:** Auditor-Mestre
**Data:** 17/09/2026

### 1. CONCORDÂNCIA COM O ACHADO ARQUITETURAL

Após análise do apontamento apresentado pela auditoria, considero **procedente e material** a identificação do problema no diagrama da arquitetura consolidada, especificamente no nó:

`EVIDÊNCIAS / VÍNCULOS UNIFICADOS`

A representação atual coloca os fluxos provenientes das **Bibliotecas Canônicas** e da **Pasta de Atualização** em uma estrutura aparentemente unificada antes da Ontologia/Grafo.

Essa representação não é compatível com a decisão arquitetural de que a Pasta de Atualização permanece **segregada do conhecimento canônico** até sua consulta pelo Motor.

Portanto, o apontamento deve ser aceito e corrigido.

### 2. DECISÃO ARQUITETURAL

A decisão adotada é:

> **Os fluxos canônico e de atualização permanecem separados até o Motor Clínico.**

A arquitetura não terá um pool único de evidências no qual elementos canônicos e elementos de atualização sejam indistinguíveis.

O fluxo canônico permanece:

`Bibliotecas Canônicas`
→ `Evidências Bibliográficas / Narrativas Transversais`
→ `Evidências / Vínculos Canônicos`
→ `Ontologia / Grafo`
→ `JSONs Modulares`
→ `Motor Clínico`

Enquanto a atualização permanece em fluxo próprio:

`Pasta de Atualização`
→ `Motor Clínico`

O Motor poderá consultar ambos os fluxos, mas deverá preservar a origem de cada conhecimento recuperado.

### 3. PROVENIÊNCIA DA INFORMAÇÃO RECUPERADA

A segregação não dependerá apenas da topologia visual da arquitetura.

Todo item recuperado pelo Motor deverá carregar sua origem no próprio payload ou estrutura equivalente, permitindo distinguir, no mínimo:

`origem_conhecimento = canonico`

ou

`origem_conhecimento = atualizacao`

Isso permite rastreabilidade mesmo quando o Motor realiza uma consulta conjunta ou apresenta informações provenientes das duas fontes.

A atualização, portanto, pode ser **consultada**, mas não se transforma automaticamente em conhecimento canônico.

### 4. IMPACTO SOBRE D-06

O achado também confirma a necessidade de preservar a interpretação de D-06:

> A Pasta de Atualização não altera automaticamente os eixos relacionais do conhecimento canônico.

Uma atualização pode informar o Motor, ser considerada na interpretação e posteriormente originar um processo formal de revisão da Biblioteca Canônica.

Entretanto, essa eventual incorporação deverá ocorrer por processo próprio de atualização/curadoria, e não pela simples consulta da Pasta de Atualização.

### 5. IMPACTO SOBRE A ONTOLOGIA/GRAFO

A Ontologia/Grafo continuará representando o conhecimento estruturado que foi formalmente incorporado à arquitetura canônica.

Não deverá ser interpretado como um mecanismo de fusão automática entre conhecimento canônico e material de atualização.

Isso preserva:

* rastreabilidade;
* proveniência;
* segregação epistemológica;
* controle de atualização;
* auditabilidade;
* possibilidade de reversão ou revisão de material ainda não incorporado ao cânone.

### 6. CORREÇÃO DO DIAGRAMA

O diagrama principal deverá ser corrigido para remover o nó:

`EVIDÊNCIAS / VÍNCULOS UNIFICADOS`

como ponto de convergência anterior à Ontologia/Grafo.

A representação consolidada deverá assumir, conceitualmente, a seguinte forma:

```text
                    [ CIÊNCIA ]
                         │
                         ▼
              ┌─────────────────────┐
              │ BIBLIOTECAS         │
              │ CANÔNICAS            │
              └──────────┬──────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       ┌──────────────┐     ┌─────────────────┐
       │ EVIDÊNCIAS   │     │ NARRATIVAS      │
       │ BIBLIOGRÁF.  │     │ TRANSVERSAIS    │
       └──────┬───────┘     └────────┬────────┘
              └──────────┬───────────┘
                         ▼
              ┌─────────────────────┐
              │ EVIDÊNCIAS /        │
              │ VÍNCULOS CANÔNICOS  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ ONTOLOGIA / GRAFO   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ JSONs MODULARES     │
              └──────────┬──────────┘
                         │
                         ▼
                    ┌─────────┐
                    │  MOTOR  │◄──────────── [ ANAMNESE ]
                    └────┬────┘
                         │
                         ▼
                  INTERPRETAÇÃO
                         │
                         ▼
                     SUGESTÕES
                         │
                         ▼
                       LAUDO


              ┌─────────────────────┐
              │ PASTA DE            │
              │ ATUALIZAÇÃO         │
              └──────────┬──────────┘
                         │
                         └──────────────► MOTOR
                                  consulta ativa
```

### 7. NÃO HÁ NECESSIDADE DE REENGENHARIA GLOBAL

O achado não justifica reabertura integral da arquitetura.

A correção necessária está concentrada em:

1. diagrama principal;
2. descrição textual correspondente;
3. definição explícita da separação entre fluxo canônico e atualização;
4. mecanismo de proveniência no payload recuperado pelo Motor;
5. revisão de qualquer trecho que interprete os dois fluxos como um único repositório antes do Motor.

Os demais componentes arquiteturais permanecem preservados, salvo eventual inconsistência documental decorrente dessa correção.

### 8. CORREÇÕES DOCUMENTAIS ADICIONAIS

Também devem ser corrigidos os problemas formais apontados na auditoria:

* identificação do documento como **V2.1**, quando essa for a versão efetivamente consolidada;
* nome do arquivo correspondente à versão;
* correção do cabeçalho indevido `# 21. ARQUITETURA MULTIDOMÍNIO COMPLETA` inserido dentro da seção 2;
* eliminação de duplicidade ou inconsistência de numeração de seções.

Essas correções são documentais e não alteram a arquitetura conceitual.

### 9. L-05 v1.3

Quanto ao L-05 v1.3, permanece válida a avaliação anterior:

* estrutura N1/N2 coerente;
* separação entre natureza da evidência, desenho do estudo e uso preservada;
* `ancora_principal` adequadamente definida;
* `direcao_suporte` separada de `papel`;
* distinção entre `status_validacao` e `status_auditoria` preservada;
* `verification_status` não deve ser confundido com força de evidência;
* `forca_biologica_conexao` permanece sujeita ao respectivo gate;
* triagem automática de direção de suporte permanece como mecanismo de triagem, e não como validação epistemológica definitiva.

Não identifico, neste momento, necessidade de reengenharia estrutural do L-05 v1.3 decorrente deste achado arquitetural.

### 10. CONCLUSÃO

O apontamento referente à fusão visual dos fluxos canônico e de atualização deve ser **aceito como correção arquitetural válida**.

A decisão consolidada passa a ser:

> **Conhecimento canônico e conhecimento de atualização permanecem segregados até o Motor Clínico. O Motor pode consultar ambos, mas cada item recuperado deve preservar sua proveniência. A consulta à Pasta de Atualização não implica incorporação automática ao conhecimento canônico.**

Com essa correção, preservam-se simultaneamente a função da Pasta de Atualização, a integridade do conhecimento canônico, a rastreabilidade e os princípios de D-06.

A correção deve ser aplicada ao documento arquitetural antes de sua utilização como versão consolidada.

**Parecer:**
**ACEITO COM CORREÇÃO ARQUITETURAL LOCALIZADA.**

Não se recomenda reabrir a arquitetura global nem os contratos já estabilizados por causa deste achado específico.
