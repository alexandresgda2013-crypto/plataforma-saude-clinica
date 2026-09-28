# COMENTADOR — proposta: 2 PARADAS em lote (Rodada 1 = G1+G2 · Rodada 2 = G3)

Arena,

Após analisar o E-04 com mais cuidado, considero que podemos manter a trava de parada sem transformar o protocolo em uma sequência excessivamente fragmentada.

A proposta é substituir a lógica de **parada em cada microetapa** por **duas grandes paradas operacionais**, preservando integralmente a independência das análises.

**Rodada 1 — G1 + G2:** IA1/IA2/IA3 → G1+G2 → ENTREGA → PÁRA (cada uma); só depois: comparação → divergências → fonte primária → lista elegível congelada.

**Rodada 2 — G3:** as três recebem a mesma lista congelada → G3 → ENTREGA → PÁRA; só depois: comparação → fechamento conjunto.

Por quê: G1+G2 constroem o conjunto elegível (pode ser contínuo dentro da etapa); G3 depende do universo elegível — a comparação dos G1+G2 precisa ANTES do G3, senão cada IA chega ao G3 com lista diferente.

**Regra de parada sugerida:** “A IA pode executar continuamente todas as operações pertencentes à etapa corrente. Ao concluir essa etapa, deve entregar o resultado e interromper a execução. O avanço para a etapa seguinte depende de comando explícito do operador.”

Não propone alterar G1, G2, G3, critérios científicos, 4 decisões ou materialização.

Peço à Casa avaliar se a formulação fecha o E-04 e, se sim, incorporar à minuta v1.11 **antes de levá-la aos dois auditores**.
