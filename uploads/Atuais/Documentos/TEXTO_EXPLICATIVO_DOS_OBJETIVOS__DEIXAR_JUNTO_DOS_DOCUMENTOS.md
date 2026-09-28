Texto explicativo do objetivo (para ficar junto aos documentos/arquivos)

# SOBRE ESTE PROJETO

## O que é
Este é o repositório de curadoria científica de uma plataforma
comercial B2B de conhecimento biomédico modular, voltada a
profissionais de saúde (médicos, hospitais, laboratórios,
universidades). A plataforma realiza análise mecanística de
ansiedade e depressão, construindo narrativas de mecanismos
biológicos prováveis/improváveis e sugestões terapêuticas ancoradas
em literatura científica revisada por pares.

Filosofia fechada: a plataforma analisa e sugere; o profissional
decide. Não há diagnóstico automatizado nem substituição de
julgamento clínico.

## Por que este processo existe
O conhecimento da plataforma é organizado em 16 mecanismos biológicos
(eixo HPA, neuroinflamação, neuroplasticidade, disbiose intestinal,
etc.), cada um decomposto em submódulos temáticos, e cada submódulo
decomposto em claims atômicos — afirmações científicas específicas,
cada uma ancorada a PMIDs (identificadores do PubMed) auditados.

A unidade de verdade do sistema é o claim atômico, não o artigo
inteiro. A ordem é inviolável: claim → evidência ancorada → narrativa.
Isso significa que nenhuma afirmação entra na base de conhecimento
sem antes passar por um processo formal de auditoria em 3 etapas
(G1 Existência, G2 Elegibilidade, G3 Suporte ao Claim) — descrito
em detalhe no documento "Como Executar".

## Duas trilhas, dois destinos
O projeto tem duas trilhas que não devem ser confundidas:
- Trilha mecanística: a biblioteca canônica de cada um dos 16
  mecanismos (fisiologia, cascata bioquímica, conexões). Produzida em
  pipeline próprio; as 16 bibliotecas já existem e estão em auditoria.
- Trilha clínica (este kit): claims atômicos que documentam o quanto a
  ciência clínica (meta-análises, caso-controle, coortes, post-mortem,
  ômicas humanas) sustenta cada fenômeno. Esses claims NÃO entram na
  biblioteca canônica mecanística — alimentam a pasta
  evidencias/bibliografia da plataforma.

## Para que serve, no fim
Estas bibliotecas de conhecimento, uma vez validadas mecanismo por
mecanismo, alimentarão um motor clínico capaz de ler múltiplos
mecanismos simultaneamente e suas conexões (cross-references),
gerando uma análise clínica integrada e baseada em evidência real —
nunca em suposição, extrapolação não verificada ou achado isolado
promovido acima do que a ciência de fato sustenta.

## Como este repositório está organizado
Os documentos aqui presentes formam um "kit de produção" para a
validação manual de PMIDs, mecanismo por mecanismo, submódulo por
submódulo. Cada documento tem um papel específico e não deve ser
confundido com os demais — ver "Como Executar" para a ordem correta
de leitura e o fluxo operacional completo.

## Estado atual
Em fechamento: Mecanismo B1 (Neuroinflamação), Submódulo SM-02
(Prova de Existência), trilha clínica — meta é concluir os 35
claims-alvo. SM-03 em diante só inicia após a decisão do contrato do
motor clínico e dos schemas da pasta evidencias/bibliografia. Ver
Bloco de Estado vigente (v1.8) para status detalhado.