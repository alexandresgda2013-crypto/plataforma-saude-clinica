CHECKLIST DE SANIDADE DO GPM
Verificação estrutural pós-geração — antes da Rodada 2
Markdown

# CHECKLIST DE SANIDADE DO GPM
## Uso: colar junto com o GPM recém-gerado, em mini-rodada própria, 
## entre a Rodada 1 (geração do GPM) e a Rodada 2 (geração da Biblioteca)

---

# INSTRUÇÃO PARA A IA

Você vai receber um documento GPM (Gerador de Profundidade Molecular) 
já gerado para um mecanismo específico. Sua tarefa não é avaliar 
qualidade científica, mérito do conteúdo ou fazer julgamento 
subjetivo sobre profundidade. Sua tarefa é aplicar os critérios 
objetivos abaixo, um por um, e reportar o resultado exatamente no 
formato de saída especificado ao final.

Não corrija o documento. Apenas reporte o que encontrou.

---

# CRITÉRIOS DE VERIFICAÇÃO

## A. Completude estrutural dos módulos

Verificar se os 10 módulos estão presentes, na ordem, com título 
identificável:

- [ ] MÓDULO 00 — Metadados e Escopo
- [ ] MÓDULO 01 — Mapa Exaustivo de Vias Moleculares
- [ ] MÓDULO 02 — Mapa Exaustivo de Mediadores Moleculares
- [ ] MÓDULO 03 — Mapa Exaustivo de Tipos Celulares e Estruturas
- [ ] MÓDULO 04 — Variabilidade Genética e Epigenética Exaustiva
- [ ] MÓDULO 05 — Biomarcadores Exaustivos
- [ ] MÓDULO 06 — Interconexões Exaustivas com B1–B16
- [ ] MÓDULO 07 — Subtipos e Fenótipos Clínicos Documentados
- [ ] MÓDULO 08 — Controvérsias, Heterogeneidade e Lacunas
- [ ] MÓDULO 09 — Checklist de Verificação Cruzada com o Prompt 4.0
- [ ] MÓDULO 10 — Observações em Outras Condições

Reportar: quantos de 10 estão presentes. Se algum estiver ausente, 
nomear qual.

## B. Piso mínimo de conteúdo por módulo

Para os Módulos 01 a 08, verificar se cada um contém no mínimo 3 
itens desenvolvidos (vias, mediadores, tipos celulares, 
polimorfismos, biomarcadores, conexões, subtipos ou controvérsias, 
conforme o módulo) OU uma declaração explícita do tipo "literatura 
insuficiente para maior resolução nesta camada".

Reportar, módulo por módulo: número de itens encontrados, e se há 
declaração de insuficiência nos módulos que não atingiram 3 itens.

## C. Cobertura do Briefing

Esta é a verificação mais importante. Localizar o Briefing usado na 
geração deste GPM (fornecido junto nesta mini-rodada) e conferir, 
termo por termo, se cada item citado nominalmente no Briefing 
aparece referenciado em algum lugar do GPM gerado — não precisa ser 
desenvolvido em profundidade, mas precisa aparecer citado.

Reportar em formato de tabela:

| Termo do Briefing | Aparece no GPM? (sim/não) | Módulo onde aparece |
|---|---|---|
| [listar cada termo do Briefing] | | |

Se algum termo não aparece em lugar nenhum, isso deve ser reportado 
explicitamente como falha de cobertura — não deve ser interpretado 
como "provavelmente não relevante".

## D. Presença de âncoras de rastreabilidade

Verificar se cada um dos Módulos 01 a 08 termina com uma âncora no 
formato `[REF_MODULO_XX: ...]` contendo ao menos uma citação.

Reportar: quantos módulos têm a âncora presente, quantos não têm.

## E. Ausência de citação genérica não verificável

Verificar se existe algum trecho do tipo "estudos mostram que..." ou 
"a literatura indica..." sem nenhuma citação (Autor, Ano) associada.

Reportar: listar trechos encontrados nessa condição, se houver, com 
localização (módulo e subseção aproximada).

## F. Presença do Inventário Negativo (Módulo 02)

Verificar se o Módulo 02 contém uma subseção de inventário negativo 
(mediadores investigados sem associação consistente encontrada).

Reportar: presente / ausente.

## G. Nota de natureza do Módulo 10

Verificar se o Módulo 10 contém a nota explicando que os itens ali 
listados são amostra ilustrativa, não triagem completa.

Reportar: presente / ausente.

---

## H. Declaração de busca em tempo real (Módulo 00)

Verificar se o campo "Corte de conhecimento" do Módulo 00 contém uma
declaração explícita: data de busca em tempo real realizada, OU a
declaração de ausência de busca com o texto de risco especificado no
Molde GPM.

Reportar: presente com busca ativa / presente com declaração de
ausência / ausente (nenhuma declaração encontrada).

---

# FORMATO DE SAÍDA OBRIGATÓRIO
CHECAGEM DE SANIDADE — GPM [nome do mecanismo]

A. Módulos presentes: [X/10]
Ausentes: [listar ou "nenhum"]

B. Piso mínimo por módulo:
Módulo 01: [n itens] | Módulo 02: [n itens] | Módulo 03: [n itens]
Módulo 04: [n itens] | Módulo 05: [n itens] | Módulo 06: [n itens]
Módulo 07: [n itens] | Módulo 08: [n itens]
Módulos abaixo do piso sem declaração de insuficiência: [listar ou "nenhum"]

C. Cobertura do Briefing:
[tabela completa termo a termo]
Termos do Briefing ausentes do GPM: [listar ou "nenhum"]

D. Âncoras de rastreabilidade: [X/8 módulos aplicáveis]
Módulos sem âncora: [listar ou "nenhum"]

E. Citações genéricas não verificáveis encontradas: [listar ou "nenhuma"]

F. Inventário Negativo (Módulo 02): [presente/ausente]

G. Nota de natureza (Módulo 10): [presente/ausente]

H. Declaração de busca em tempo real: [presente com busca ativa / presente com declaração de ausência / ausente]

VEREDITO FINAL: [APROVADO PARA RODADA 2] ou
[REQUER NOVA EXECUÇÃO DO GPM — motivo: ...]

text


---

# CRITÉRIO DE VEREDITO

Marcar como **[REQUER NOVA EXECUÇÃO DO GPM]** se qualquer uma das
condições abaixo for verdadeira:
- Menos de 10/10 módulos presentes
- Qualquer termo do Briefing (item C) ausente do GPM
- Mais de 2 módulos sem âncora de rastreabilidade (item D)
- Qualquer citação genérica não verificável encontrada (item E)
- Item H reportado como "ausente" (nenhuma declaração de busca em
  tempo real nem de sua ausência)

Caso contrário, marcar como **[APROVADO PARA RODADA 2]**.

Este veredito é estrutural, não científico. Um GPM "aprovado" aqui 
ainda passará pelo rigor de qualidade de evidência do Prompt 4.0 na 
Rodada 2 — este checklist apenas garante que o material bruto está 
completo o suficiente para ser curado.
Como usar na prática: depois da Rodada 1 gerar o GPM_B1_Neuroinflamacao.md, abra uma mini-rodada (pode ser no mesmo chat, logo em seguida) e cole: este Checklist + o GPM gerado + o Briefing original usado. A IA aplica os critérios e devolve o relatório no formato especificado. Se vier [APROVADO PARA RODADA 2], siga para a Rodada 2 normalmente. Se vier [REQUER NOVA EXECUÇÃO], você já sabe exatamente qual módulo ou termo falhou, sem precisar reler o documento inteiro manualmente.