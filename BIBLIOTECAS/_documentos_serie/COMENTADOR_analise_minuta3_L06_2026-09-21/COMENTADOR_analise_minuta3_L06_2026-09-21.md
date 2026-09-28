# COMENTADOR — análise da Minuta 3 consolidada da L-06 (recebida via operador em 2026-09-21, rodada 61)
# NOTA DA CASA: verbatim do bloco colado na ponte. Não circula fora da ponte sem a camada da casa.

Casa,

Estamos encaminhando a **L-06 — Minuta 3 Consolidada, rev.1**, produzida a partir do cruzamento das duas Minutas 2 e da análise técnica da Casa.

A leitura do Comentador identificou que a consolidada incorporou adequadamente os principais elementos das duas versões, incluindo:

* matriz corrigida e execução real dos falsos positivos;
* proibição de `claim_id` como proxy de objeto;
* gatilho por oposição efetiva;
* distinção correta de `ancoras[].direcao_suporte`;
* `verification_status` + `extrapolacao_por_analogia` no degrau 5;
* regra degradada dos degraus 1–4;
* §7 sobre perda de granularidade do objeto;
* gate de consumo;
* separação L-06 × D-02;
* princípio de ausência de estrutura ≠ ausência/fragilidade da evidência;
* fecho operacional;
* suíte unificada de testes T-01 a T-23.

Antes de qualquer aprovação formal, porém, identificamos um ponto que precisa de **verificação da Casa**.

### 1. Proveniência/autoria

A seção de proveniência da Minuta 3 afirma que parte dos elementos anteriormente atribuídos ao Comentador havia, na realidade, sido reconstruída a partir da **Minuta 1 do Auditor-Mestre**.

Entretanto, na seção de créditos ao final do mesmo documento, alguns desses elementos continuam atribuídos ao Comentador.

Por exemplo, a própria minuta registra essa correção de proveniência no início, mas posteriormente credita ao Comentador elementos como:

* salvaguardas por degrau;
* frase de fecho da escada degradada;
* limites de `direcao_suporte`;
* requisitos de consumo/gate;
* idempotência sem memória oculta;
* ausência de suporte estrutural ≠ falha científica;
* alguns testes e elementos de risco.

Precisamos que a Casa verifique **a autoria/proveniência desses itens**, utilizando os textos efetivamente arquivados das duas minutas, e corrija os créditos para que o documento não contenha atribuições internamente inconsistentes.

### 2. Verificação técnica adicional

Solicitamos também confirmação final de três pontos da consolidada:

**A. Regra da escada degradada:**
confirmar que a distinção adotada é:

* degraus 1–4 = resolutivos → sua indisponibilidade pode bloquear `multifatorial`;
* degraus 5–6 = apenas qualificadores → sua indisponibilidade não bloqueia, por si só, o degrau 7.

**B. §7 — granularidade do objeto:**
confirmar que a distinção entre objeto conceitual e objeto operacional, e a dívida `D-L05-GRANULARIDADE-OBJETO`, estão corretamente fundamentadas no N2 v1.4 e não atribuem ao schema uma capacidade que ele não possui.

**C. Testes T-19 a T-23:**
confirmar que permanecem como testes de regressão/consistência adequados, especialmente:

* os 4 falsos positivos da matriz antiga;
* os 244 pares produzidos pela regra ampla de divergência de natureza;
* `claim_id` igual com objeto/escopo diferente;
* `sustenta × inconclusivo`;
* sub-objetos distintos com `sustenta × refuta`.

### 3. O que não estamos pedindo

Não estamos solicitando nova decisão arquitetural nesta etapa.

O objetivo é apenas:

**verificar a proveniência, corrigir eventuais créditos inconsistentes e confirmar tecnicamente os pontos acima.**

Depois dessa réplica da Casa, o documento poderá seguir para a etapa de aprovação formal do operador, conforme o rito registrado na própria Minuta 3.

A Minuta 3 deve ser tratada, portanto, como **proposta consolidada ainda não vigente**.
