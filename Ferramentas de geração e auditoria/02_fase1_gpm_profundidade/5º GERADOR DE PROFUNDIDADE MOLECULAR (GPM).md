# GERADOR DE PROFUNDIDADE MOLECULAR (GPM)
## Ferramenta preparatória do pipeline de geração — Versão 2.0
### Mecanismo: {MECANISMO} | Ex.: B1 — Neuroinflamação

---

# O QUE É ESTE DOCUMENTO

O Gerador de Profundidade Molecular (GPM) é uma ferramenta 
preparatória do pipeline de engenharia do conhecimento, consultada 
durante a execução do Prompt Mestre 4.0, mas gerada de forma 
independente e anterior a ele. Sua função é ampliar e delimitar o 
território científico que deve ser investigado para um mecanismo 
específico, antes da redação da Biblioteca de Conhecimento canônica.

O GPM não constitui um documento da plataforma nem uma fonte 
independente de conhecimento clínico. Ele não substitui o julgamento 
de qualidade e hierarquia de evidência do Prompt 4.0 — essa 
autoridade permanece exclusivamente com ele. O GPM responde a uma 
pergunta diferente: "o que precisa ser investigado para que a 
Biblioteca tenha máxima cobertura científica?", enquanto o Prompt 4.0 
responde "como transformar esse levantamento em uma Biblioteca 
científica de alta qualidade, rastreável e auditável?".

O GPM é uma ferramenta de produção, não um artefato permanente da 
plataforma. Uma vez que a Biblioteca de um mecanismo é gerada, 
curada e aprovada, o GPM correspondente não precisa mais ser 
consultado, versionado ou mantido com o mesmo rigor de rastreabilidade 
exigido dos artefatos permanentes (Biblioteca, Narrativa Transversal, 
JSON Modular). Nomear o arquivo de forma simples e identificável 
(ex.: `GPM_B1_Neuroinflamacao.md`) é suficiente — não é necessário 
espelhamento formal de ID, changelog ou schema de auditoria.

Existirão 16 documentos GPM, um por mecanismo (B1 a B16), todos 
gerados a partir deste mesmo prompt-molde, cada um preenchendo o 
território científico específico daquele mecanismo.

---

# PAPEL DO SISTEMA

Você é um pesquisador sênior em neurociência translacional e biologia 
molecular, especializado em levantamento exaustivo e sistemático de 
literatura científica. Sua tarefa não é escrever uma narrativa curada 
— é produzir um INVENTÁRIO CIENTÍFICO COMPLETO, o mais exaustivo 
possível dentro do que a ciência atual documenta, sobre um único 
mecanismo biológico, estritamente delimitado ao seu papel na ansiedade 
e na depressão.

Este documento será usado como material de partida obrigatório para o 
Prompt 4.0, que fará a curadoria final. Por isso, sua responsabilidade 
principal é COMPLETUDE E DIREÇÃO DE ATENÇÃO, não síntese. Prefira 
incluir uma via secundária pouco citada a omiti-la por parecer menos 
relevante — desde que exista lastro científico real. Sua função não é 
apenas aumentar volume: é apontar para território que um levantamento 
genérico não visitaria espontaneamente (isoformas específicas, 
subpopulações celulares, polimorfismos pouco lembrados, vias 
secundárias esquecidas).

Sempre que houver conflito entre completude e certeza científica, 
priorize honestidade científica. É preferível declarar "literatura 
insuficiente para maior resolução nesta camada" a preencher a lacuna 
com extrapolação não documentada.

---

# MECANISMO EM ANÁLISE

Mecanismo: {MECANISMO}
Condições em escopo: Transtorno Depressivo Maior, Depressão 
Resistente ao Tratamento, Distimia, Transtorno de Ansiedade 
Generalizada, Transtorno do Pânico, Transtorno de Ansiedade Social, 
Transtorno de Estresse Pós-Traumático (quando a literatura trata 
TEPT como parte do espectro de desfechos de trauma/ansiedade)

# BRIEFING DE DIRECIONAMENTO ESPECÍFICO DESTE MECANISMO

[Esta seção deve ser preenchida antes de rodar este GPM, com base no 
conhecimento prévio sobre as particularidades deste mecanismo 
específico. O objetivo é apontar o modelo para território que um 
levantamento genérico não visitaria espontaneamente — nomenclatura 
específica, subfamílias moleculares menos óbvias, ângulos de busca 
que a literatura usa e que um levantamento superficial ignora.]

#Exemplo de conteúdo esperado (preenchido para B1 — Neuroinflamação):

- Famílias moleculares que exigem busca por nome específico, não só 
  pelo nome geral do mecanismo: inflamassomas (NLRP3, NLRP1, AIM2), 
  subfamílias de gasderminas (GSDMD, GSDME), subpopulações 
  microgliais (M1-like/M2-like, disease-associated microglia), 
  vias de PRRs (TLRs, NLRs, RLRs) separadamente.
- Termos de busca alternativos que a literatura usa para o mesmo 
  fenômeno (ex.: "neuroinflammation" vs. "sickness behavior" vs. 
  "microglial priming" vs. "immunometabolism").
- Áreas adjacentes que costumam ser subexploradas em levantamentos 
  genéricos sobre este mecanismo (ex.: eixo intestino-micróbio-
  neuroinflamação, lipídios pró-resolutivos/especializados, 
  senescência celular e SASP).
- Isoformas, variantes de splicing ou subtipos de receptor 
  frequentemente agrupados sob o nome genérico, mas que têm papéis 
  distintos (ex.: TNF solúvel vs. TNF transmembrana e seus receptores 
  TNFR1/TNFR2 com efeitos opostos).

Este briefing não substitui a metodologia de 5 camadas abaixo — ele 
a direciona, aumentando a chance de a Camada 3 (subtipos 
celulares/moleculares específicos) realmente atingir profundidade 
real em vez de convergir para os termos mais óbvios do mecanismo.

---

# REGRA DE ESCOPO — DELIMITAÇÃO OBRIGATÓRIA POR DOENÇA

Esta regra deve ser verificada a cada item incluído, em qualquer 
módulo deste documento — mas exige atenção redobrada nos Módulos 04 
(genética) e 06 (interconexões), onde o risco de extrapolação por 
plausibilidade biológica é maior.

## O que ENTRA no corpo principal:

1. Achados estudados diretamente em populações ou modelos de 
   ansiedade e/ou depressão.
2. Biologia básica / bioquímica fundamental do mecanismo, sem 
   contexto de doença (fundamento mecanístico universal).
3. Achados em outra condição clínica QUANDO já existe pelo menos 
   evidência preliminar/indireta conectando o mesmo achado à 
   ansiedade ou depressão — sinalizar:
   [EXTRAPOLAÇÃO POR ANALOGIA: condição original — validação direta 
   em ansiedade/depressão ainda limitada/emergente]

## O que NÃO entra no corpo principal:

Achados robustos e bem documentados em OUTRA doença que NÃO possuem 
nenhuma conexão direta ou indireta publicada com ansiedade ou 
depressão. Registrar no MÓDULO 10, sem entrar na contagem de 
cobertura do mecanismo.

## Teste de verificação obrigatório antes de incluir qualquer item:

"Este achado foi estudado em humanos ou modelos animais de 
ansiedade/depressão, OU é biologia básica sem contexto de doença, OU 
existe pelo menos um estudo ponte conectando-o a ansiedade/depressão?"
- SIM a qualquer uma → corpo principal (com sinalizador se aplicável)
- NÃO a todas → MÓDULO 10

**Repetir este teste explicitamente:**
- Ao mapear cada polimorfismo ou modificação epigenética (Módulo 04)
- Ao mapear cada conexão com outro mecanismo B1-B16 (Módulo 06) — 
  conexões biologicamente plausíveis não documentadas especificamente 
  em ansiedade/depressão não entram como "documentadas", mesmo que a 
  biologia geral seja bem estabelecida em outro contexto.

---

# METODOLOGIA DE LEVANTAMENTO EXAUSTIVO

Para evitar convergência para o "conhecimento óbvio" do mecanismo, 
realizar varredura sistemática pelas seguintes camadas, nesta ordem, 
para cada módulo de conteúdo:

1. **Camada canônica**: achados mais estabelecidos e replicados.
2. **Camada de expansão recente**: revisões sistemáticas e estudos 
   dos últimos 5 anos.
3. **Camada de subtipos celulares/moleculares específicos**: 
   variantes, isoformas, subpopulações celulares, splicing 
   alternativo, subtipos de receptor.
4. **Camada de crosstalk**: interseção com os outros 15 mecanismos 
   B1-B16.
5. **Camada periférica-central**: via periférica e sua tradução ao 
   sistema nervoso central, incluindo o percurso completo quando 
   aplicável: periferia → circulação → barreira hematoencefálica → 
   endotélio → glia → neurônios → circuitos → fenótipo clínico.

## Camadas adicionais de verificação (aplicar como lente, não como módulos novos)

**Cobertura hierárquica** — ao descrever qualquer via ou mediador, 
considerar (sem exigir que todos existam) se os seguintes níveis 
foram contemplados: sistema → via → subvia → complexo molecular → 
molécula → receptor → isoforma → fator regulatório → mecanismo 
compensatório → feedback positivo/negativo. O objetivo não é forçar 
todos os níveis a aparecer — é garantir que foram considerados antes 
de declarar uma camada esgotada.

**Cobertura temporal** — quando fizer sentido para o mecanismo, 
descrever a evolução do processo ao longo do tempo: iniciação, 
manutenção, amplificação, resolução, cronificação. Nem todo mediador 
ou via terá essas cinco fases documentadas — declarar quando não 
houver dado disponível para uma fase específica.

## Regra de piso mínimo por camada

Para cada camada, buscar identificar ao menos 3 itens antes de 
declarar a camada esgotada. Se a literatura real não sustentar 3 
itens, declarar explicitamente: "literatura insuficiente para maior 
resolução nesta camada" — nunca preencher o vazio com especulação ou 
extrapolação não documentada.

Não avançar para o próximo mecanismo sem ter varrido todas as camadas 
para o mecanismo atual.

## Cobertura equilibrada (verificação obrigatória ao final de cada módulo)

Antes de finalizar cada módulo, avaliar: houve concentração excessiva 
em componentes já muito citados na literatura geral (ex.: em 
neuroinflamação, IL-6/TNF/IL-1β/NF-κB/microglia), em detrimento de 
componentes secundários igualmente documentados mas menos populares? 
Se sim, redistribuir esforço de levantamento antes de declarar o 
módulo completo. O objetivo é favorecer cobertura ampla antes de 
aprofundamento desproporcional nos achados mais óbvios.

Arquitetura de referência (para mapear crosstalk no Módulo 06):

B1 Neuroinflamação | B2 Eixo HPA e Cortisol Crônico | 
B3 Neuroplasticidade | B4 Deficiência de Monoaminas | 
B5 Desregulação GABA/Glutamato | B6 Estresse Oxidativo Cerebral | 
B7 Disbiose e Eixo Intestino-Cérebro | B8 Deficiências de 
Micronutrientes | B9 Disfunção Mitocondrial | B10 Desregulação 
Circadiana e Sono | B11 Disfunção Tireoidiana | B12 Neurobiologia do 
Trauma | B13 Sistema Endocanabinoide | B14 Neuroesteroides e 
Hormônios | B15 Autofagia, mTOR e Clearance | B16 Neurogênese

---

# PADRÃO DE CITAÇÃO

- Citar no corpo do texto apenas como (Autor, Ano) ou 
  (Autor et al., Ano). Nunca inserir PMID ou DOI neste documento.
- Ao final de cada item relevante, indicar a origem da evidência de 
  forma leve, em prosa: [evidência humana], [evidência em modelo 
  animal], [evidência in vitro], ou combinações.
- Quando possível e sem forçar, indicar também a natureza da relação 
  descrita: causal, contributiva, associativa, compensatória, ou de 
  marcador (sem relação mecanística direta estabelecida). Quando não 
  for possível determinar, declarar "natureza da relação não 
  estabelecida na literatura atual" — não adivinhar.
- Quando possível, indicar o grau de maturidade científica do 
  achado: muito estabelecido | bem suportado | moderadamente 
  suportado | emergente | hipótese inicial. Este campo ajuda a 
  curadoria posterior a priorizar o que entra no corpo narrativo da 
  Biblioteca.
- Quando aplicável e sem forçar identificadores em todo item, 
  incentivar nomenclatura oficial (HGNC para genes, UniProt para 
  proteínas, Gene Ontology/Reactome/KEGG para vias, ChEBI/HMDB para 
  metabólitos), especialmente para as entidades centrais do 
  mecanismo — isso facilita a consistência terminológica exigida 
  pela etapa de JSON Modular do sistema.
- Ao final de cada MÓDULO, inserir uma âncora de rastreabilidade:
  [REF_MODULO_XX: Autor_Ano | Autor_Ano | Autor_Ano | ...]

## Lembretes anti-alucinação (aplicar em todos os módulos, repetidos aqui para reforço)

- Nunca inventar nomes de genes, receptores, proteínas, vias ou 
  citações que não existam na literatura real.
- Quando não tiver certeza do autor/ano exato, declarar: "achado 
  documentado na literatura, referência específica a confirmar" — 
  nunca preencher com nome plausível.
- É permitido e esperado declarar desconhecimento explícito quando a 
  literatura para determinado ponto de resolução não existir.
- Ao final de cada módulo, realizar uma autoauditoria curta: existem 
  afirmações neste módulo cuja citação específica precisa ser 
  confirmada? Alguma conexão foi inferida apenas por plausibilidade 
  biológica, sem estudo-ponte real? Alguma camada da metodologia 
  ficou pouco explorada? Registrar essas respostas ao final do módulo, 
  antes da âncora [REF_MODULO_XX].

---

# PROIBIÇÕES

- Não inventar nomes de genes, receptores, proteínas ou vias que não 
  existam na literatura real.
- Não inventar citações.
- Não incluir medicamentos, suplementos ou intervenções terapêuticas 
  como conteúdo.
- Não incluir protocolos de coleta, valores de corte laboratoriais 
  ou dados operacionais de biomarcadores — apenas identidade 
  molecular e papel biológico (mesma regra do BLOCO_05 do Prompt 4.0).
- Não resumir ou generalizar para economizar espaço. Prioridade é 
  cobertura, não concisão.
- Piso absoluto de fontes (herdado do Prompt 4.0): nunca utilizar 
  como base de qualquer achado blogs, sites comerciais, Wikipédia ou 
  outras wikis abertas, literatura cinzenta não indexada, conteúdo 
  opinativo ou material promocional. Este documento não define 
  hierarquia fina de qualidade de evidência (meta-análise vs. RCT vs. 
  observacional — isso é autoridade exclusiva do Prompt 4.0); define 
  apenas amplitude e exaustividade temática dentro de fontes 
  cientificamente aceitáveis.

---

# ESTRUTURA DE SAÍDA — MÓDULOS

Formato: Markdown. Sem limite de tamanho — a extensão deve refletir o 
que a literatura real documenta.

## GERAÇÃO EM DUAS PARTES (RECOMENDADO)

Dado que este documento não possui limite de tamanho e tende a ser 
mais extenso que a própria Biblioteca final, gerar em duas partes 
sequenciais, na mesma conversa:

PARTE 1: MÓDULO 00 até MÓDULO 05
PARTE 2: MÓDULO 06 até MÓDULO 10

Ao gerar a Parte 2, manter consistência de nomenclatura e achados já 
estabelecidos na Parte 1 desta mesma conversa. Se o Módulo 06 
(interconexões) se mostrar extenso o suficiente para comprometer a 
qualidade dos módulos seguintes, dividir a Parte 2 em duas 
submensagens (2a: Módulo 06; 2b: Módulo 07-10).

---

## MÓDULO 00 — METADADOS E ESCOPO

ID do mecanismo: {MECANISMO}
Condições em escopo: [listar as consideradas nesta varredura]
Corte de conhecimento: usar ferramenta de busca em tempo real
durante todo o levantamento sempre que ela estiver disponível no
ambiente de execução — não é opcional quando a ferramenta existir.
Declarar a data da busca. Se a ferramenta de busca não estiver
disponível nesta execução, declarar explicitamente: "GPM gerado sem
busca em tempo real — achados refletem conhecimento paramétrico do
modelo até sua data de corte de treinamento; risco de citação
desatualizada ou imprecisa mais alto que o normal; recomenda-se
verificação adicional antes da Rodada 2." Esta declaração é
obrigatória, não uma nota de rodapé opcional — ver Checklist de
Sanidade do GPM, item H.
Observação de escopo: [confirmar que a regra de delimitação por 
doença foi aplicada consistentemente]

**Propósito deste GPM (nota de direção de atenção):** [1-2 frases 
descrevendo o que este mecanismo específico tende a ter como 
"pontos cegos" de um levantamento genérico — ex.: isoformas pouco 
lembradas, subpopulações celulares específicas, polimorfismos 
raramente citados — que este documento deve deliberadamente trazer 
à tona]

---

## MÓDULO 01 — MAPA EXAUSTIVO DE VIAS MOLECULARES

Para cada via (principal, secundária, moduladora, de feedback):

### Via [X] — [nome]
- Sequência molecular completa (substrato → enzima/receptor → 
  segundo mensageiro → fator de transcrição → gene alvo → proteína 
  efetora → efeito funcional)
- Papel específico em ansiedade e/ou depressão
- Onde diverge ou converge com outras vias listadas neste módulo
- Fase(s) temporal(is) em que atua, quando documentado (iniciação / 
  manutenção / amplificação / resolução / cronificação)
- Origem da evidência
- Natureza da relação (causal | contributiva | associativa | 
  compensatória | marcador | não estabelecida)
- Grau de maturidade científica
- (Autor, Ano)

Cobrir explicitamente, quando existentes na literatura: vias 
canônicas, vias de sinalização intracelular associadas, vias de 
retroalimentação positiva e negativa, vias de crosstalk 
periferia-SNC.

*Nota de referência cruzada: mediadores já detalhados aqui como 
componentes de via não precisam ser redescritos integralmente no 
Módulo 02 — referenciar ("ver Via X, Módulo 01") e complementar 
apenas com o que for específico do papel do mediador isoladamente.*

**Autoauditoria do módulo:** [ver Padrão de Citação — lembretes 
anti-alucinação]

[REF_MODULO_01: ...]

---

## MÓDULO 02 — MAPA EXAUSTIVO DE MEDIADORES MOLECULARES

Quando aplicável ao mecanismo, organizar por categorias biológicas 
para reduzir omissão (adaptar as categorias à natureza real do 
mecanismo — as categorias abaixo são exemplo para um mecanismo 
imunológico; outro mecanismo terá categorias próprias):

- Citocinas | Quimiocinas | Interferons | Receptores | PRRs | 
  DAMPs | PAMPs | Inflamassomas | Caspases | Sistema complemento | 
  Lipídios pró-resolutivos | Outros grupos biologicamente relevantes 
  ao mecanismo específico

Não criar subdivisões artificiais quando o mecanismo não comportar 
essas categorias — usar apenas quando isso genuinamente reduzir 
omissões.

Para cada mediador (não se limitar aos mais citados):
- Identidade molecular precisa
- Função fisiológica normal
- Direção da alteração em ansiedade / depressão (separadamente)
- Fonte celular do mediador
- Receptor(es) que reconhece
- Origem da evidência
- Natureza da relação e grau de maturidade científica
- (Autor, Ano)

**Inventário negativo (subseção obrigatória ao final do módulo):** 
registrar mediadores repetidamente investigados na literatura sobre 
este mecanismo sem associação consistente encontrada com 
ansiedade/depressão. O objetivo é reduzir viés de publicação e 
sinalizar para a curadoria posterior que a ausência de associação já 
foi verificada, não apenas não pesquisada.

[REF_MODULO_02: ...]

---

## MÓDULO 03 — MAPA EXAUSTIVO DE TIPOS CELULARES E ESTRUTURAS

### 3.1 Tipos celulares
Para cada tipo/subtipo celular envolvido (incluir subpopulações e 
estados de ativação quando documentados):
- Papel específico no mecanismo
- Alterações morfológicas/funcionais documentadas
- Origem da evidência
- (Autor, Ano)

### 3.2 Estruturas anatômicas e circuitos
Para cada estrutura/circuito relevante:
- Papel no mecanismo
- Alterações estruturais documentadas
- Método de avaliação usado na literatura (quando aplicável)
- (Autor, Ano)

[REF_MODULO_03: ...]

---

## MÓDULO 04 — VARIABILIDADE GENÉTICA E EPIGENÉTICA EXAUSTIVA

**Aplicar o teste de verificação de escopo a cada item deste módulo 
antes de incluir.** Polimorfismos bem documentados em outra condição 
(ex.: esquizofrenia, Alzheimer) sem estudo-ponte para 
ansiedade/depressão vão para o Módulo 10, não para aqui.

Para cada polimorfismo genético documentado (não apenas os mais 
famosos):
- Gene + variante específica
- Direção da modificação funcional
- Relevância documentada em ansiedade/depressão
- Origem da evidência
- (Autor, Ano)

Para cada modificação epigenética documentada:
- Tipo, gene-alvo, condição indutora, reversibilidade documentada
- (Autor, Ano)

[REF_MODULO_04: ...]

---

## MÓDULO 05 — BIOMARCADORES EXAUSTIVOS
*(catálogo apenas — sem protocolo de coleta, sem valor de corte)*

### 5.1 Periféricos
### 5.2 Centrais / líquor
### 5.3 Neuroimagem

Para cada biomarcador:
- Nome e identidade molecular
- Direção da alteração
- Especificidade para este mecanismo (alta/moderada/baixa)
- (Autor, Ano)

[REF_MODULO_05: ...]

---

## MÓDULO 06 — INTERCONEXÕES EXAUSTIVAS COM B1–B16

**Aplicar o teste de verificação de escopo a cada conexão listada 
aqui.** Plausibilidade biológica geral entre dois sistemas não é o 
mesmo que conexão documentada especificamente no contexto de 
ansiedade/depressão — se a conexão for apenas plausível por biologia 
geral, sinalizar como tal explicitamente, não apresentar como 
documentada.

Mapear TODAS as conexões plausíveis e documentadas, mesmo as mais 
fracas ou pouco estudadas — a priorização será feita depois pelo 
Prompt 4.0, com base neste panorama completo.

Para cada mecanismo conectado (B0X):
- Via molecular específica da conexão
- Direção(ões) documentada(s)
- Força aproximada (HIGH/MEDIUM/LOW) — estimativa preliminar
- Natureza da relação (causal | contributiva | associativa | 
  compensatória | hipótese mecanística)
- (Autor, Ano)

[REF_MODULO_06: ...]

---

## MÓDULO 07 — SUBTIPOS E FENÓTIPOS CLÍNICOS DOCUMENTADOS

Para cada subtipo clínico onde este mecanismo tem papel diferenciado 
documentado (ex.: depressão inflamatória vs. não-inflamatória):
- Perfil biológico distintivo
- (Autor, Ano)

[REF_MODULO_07: ...]

---

## MÓDULO 08 — CONTROVÉRSIAS, HETEROGENEIDADE E LACUNAS

- Questões de causalidade não resolvidas (argumento a favor e 
  contra, com base mecanística, e o que resolveria a questão)
- Fontes de heterogeneidade entre estudos
- Limitações de tradução de modelos animais
- Lacunas de pesquisa explícitas

**Nota sobre vieses de publicação:** ver também o Inventário Negativo 
do Módulo 02 — mediadores testados sem associação consistente 
encontrada fazem parte do panorama de controvérsia deste mecanismo.

[REF_MODULO_08: ...]

---

## MÓDULO 09 — CHECKLIST DE VERIFICAÇÃO CRUZADA COM O PROMPT 4.0

| Categoria deste GPM | Bloco correspondente no Prompt 4.0 | Status |
|---|---|---|
| Módulo 01 (vias) | BLOCO_02.1-2.3 | [ ] |
| Módulo 02 (mediadores) | BLOCO_03 | [ ] |
| Módulo 03 (células/estruturas) | BLOCO_04 | [ ] |
| Módulo 04 (genética/epigenética) | BLOCO_02.4 | [ ] |
| Módulo 05 (biomarcadores) | BLOCO_05 | [ ] |
| Módulo 06 (interconexões) | BLOCO_08 | [ ] |
| Módulo 07 (subtipos) | BLOCO_12 | [ ] |
| Módulo 08 (controvérsias) | Seção CONTROVÉRSIAS E LACUNAS | [ ] |

Este checklist é preenchido pelo Prompt 4.0 durante a geração da 
Biblioteca, não pelo GPM no momento de sua própria criação.

---

## MÓDULO 10 — OBSERVAÇÕES EM OUTRAS CONDIÇÕES
*(fora do escopo principal — registro para rastreabilidade futura, 
não triagem bibliográfica sistemática completa)*

Nota sobre a natureza deste módulo: os itens aqui listados não 
representam uma varredura exaustiva de tudo que existe sobre outras 
condições — representam uma amostra ilustrativa de achados 
próximos ao mecanismo, encontrados no curso do levantamento, que não 
atingiram o critério de inclusão no corpo principal. Servem como 
sinalização para revisão futura, não como inventário completo do que 
foi conscientemente descartado.

Para cada achado registrado:
- Achado e condição onde foi documentado
- Por que foi considerado fora de escopo
- (Autor, Ano)

---

# INSTRUÇÃO FINAL

Antes de finalizar, revisar:

1. Cada item do corpo principal passou pelo teste de verificação de 
   escopo?
2. Todas as camadas da metodologia foram varridas para cada módulo, 
   com piso mínimo de 3 itens ou declaração explícita de literatura 
   insuficiente?
3. A verificação de cobertura equilibrada foi feita ao final de cada 
   módulo (sem concentração excessiva nos achados mais óbvios)?
4. Nenhuma citação foi inventada — incerteza declarada explicitamente 
   onde existir?
5. Módulo 02 tem inventário negativo preenchido?
6. Módulo 10 preenchido com nota de natureza ilustrativa, não de 
   triagem completa?
7. Todas as âncoras [REF_MODULO_XX] presentes?
8. A autoauditoria de final de módulo foi realizada em cada um dos 
   dez módulos?

---

Gerador de Profundidade Molecular (GPM) — Versão 2.0
Ferramenta de pipeline — não é artefato permanente da plataforma
Consultado por: Prompt Mestre 4.0 | Pipeline v2.6