# BRIEFING CONSOLIDADO B16 v1 — NEUROGÊNESE EM ANSIEDADE E DEPRESSÃO

**Rodada 0 — Briefing de direcionamento para a B16 (construção nova, mesmo padrão de profundidade das B5-B12).**
Data: 2026-09-06 · Prompt de referência: **v4.2 — "Mecanismos de Ansiedade e Depressão"** (mesmo framework da B1/B3-B12).
Mecanismo: `mecanismo_B16_neurogenese`.

> **Nota de proveniência — leia antes de usar.** Mesma ressalva das B3-B12: sem canônica prévia, sem
> mapa próprio auditado. **Pendências abertas de rodadas anteriores nesta conversa, não resolvidas
> ainda:** B13 (endocanabinoide) ficou com só 1 busca feita; B14 e B15 nunca foram solicitadas — há
> um salto de numeração até esta B16. Registrado, não bloqueia este documento.
> 4 buscas ao vivo, **14 PMIDs confirmados**, 0 "a confirmar". **Sobreposição intencional com a B3:**
> a B3 já cobriu neurogênese brevemente (Sorrells 2018/Boldrini 2018, PMIDs 29513649/29625071,
> citados aqui por referência cruzada, não rebuscados); esta B16 aprofunda muito além disso —
> linhagem celular completa, a disputa Sorrells/Boldrini em 6 capítulos até 2024, e o achado
> contraintuitivo de que mais neurogênese nem sempre significa menos ansiedade.

---

## 0. Tese-central da B16

B16 cobre a neurogênese hipocampal adulta — a geração contínua de novos neurônios na zona
subgranular do giro denteado ao longo da vida — como mecanismo próprio, distinto da plasticidade
sináptica geral já coberta na B3. Pontos centrais:

1. **A disputa sobre neurogênese humana adulta não está resolvida em 2024**, apesar de uma
   revisão de 2019 declarar "controvérsia consertada" — Sorrells et al. (2018) reportaram
   neurogênese praticamente ausente em adultos; Boldrini et al. (2018), no mesmo ano, reportaram
   persistência até a 8ª década; Moreno-Jiménez/Llorens-Martín (2019-2022) defenderam persistência
   com protocolo de fixação otimizado; e o estudo mais recente com transcriptômica espacial
   (Simard et al., 2024) **ainda encontra resultados discordantes** dependendo da técnica usada. A
   fonte do desacordo é majoritariamente **metodológica** — fixação de tecido, anticorpo, intervalo
   post-mortem — não uma disputa sobre os dados brutos em si.
2. **A relação com ansiedade é genuinamente não-monotônica** — camundongos que correm
   voluntariamente têm mais neurogênese E mais ansiedade nos mesmos paradigmas comportamentais;
   ablar a neurogênese induzida por corrida **previne** esse aumento de ansiedade. Os próprios
   autores concluem que níveis **intermediários** de neurogênese, não o máximo possível, associam-se
   à menor ansiedade — uma curva em U, não uma reta. Aumentar neurogênese "por si só" também não
   produz efeito ansiolítico ou antidepressivo-símile em outro estudo do mesmo campo.
3. **A evidência causal robusta é toda de roedor** — ablação genética ou por irradiação demonstra
   que neurogênese é necessária para resiliência ao estresse crônico e para regulação de retorno do
   cortisol ao basal; em humano, por razões éticas óbvias, não existe (nem pode existir) o
   equivalente experimental — toda evidência humana é correlacional ou post-mortem.
4. **Um mecanismo específico de resiliência já foi identificado**, não apenas "mais neurônio, mais
   resiliência" — neurogênese protege inibindo a atividade de "células responsivas ao estresse" no
   giro denteado ventral especificamente (Anacker et al., 2018), um circuito, não um número total de
   células novas.
5. **Fronteira farmacológica em 2024-2025**: compostos que aumentam farmacologicamente a
   neurogênese (não por exercício ou genética) já melhoram separação de padrões comportamentais em
   camundongos jovens e envelhecidos — candidato real a classe de fármaco "pró-neurogênico", ainda
   pré-clínico.
6. Mesma disciplina de selos: `[VERIFICADO]` só após G1→G2→G3; `[PRÉ-CLÍNICO]`/`[EXTRAPOLADO]` para
   animal/célula sem tradução humana direta (a maioria desta B); `[EMERGENTE]` para disputa em curso.

---

## 1. Nomenclatura e famílias moleculares — busca por nome específico

### 1a. Núcleo estabelecido
**Nichos neurogênicos:** zona subgranular (ZSG) do giro denteado do hipocampo (foco desta B); zona
subventricular (ZSV) dos ventrículos laterais (neurônios migram pela via rostral migratória até o
bulbo olfatório — neurogênese na ZSV humana é ainda mais contestada que na ZSG). **Linhagem
celular completa:** células tipo-1 (glia radial, GFAP+/Nestin+/Sox2+, quiescentes na maior parte do
tempo) → células tipo-2 (progenitoras intermediárias, Tbr2+, proliferativas) → neuroblastos
(doublecortina/DCX+) → neurônios imaturos → neurônios granulares maduros totalmente integrados.
**Marcadores de uso corrente:** Ki67 (proliferação ativa), DCX (neurônio imaturo, semanas de
idade), NeuN (neurônio maduro); datação por incorporação de BrdU (roedor) ou por carbono-14
retrospectivo (humano, método de Frisén, baseia-se em testes nucleares atmosféricos do século XX).
**Função computacional:** separação de padrões (*pattern separation*) — capacidade do giro denteado
de codificar contextos/memórias semelhantes como representações distintas, evitando interferência.

### 1b. Eixos que precisam de aprofundamento dedicado (a maioria já tem PMID nesta sessão — ver Seção 8)
- **A raiz metodológica da disputa humana:** protocolo de fixação de tecido (tempo, tipo de
  fixador), especificidade de anticorpo (DCX tem reatividade cruzada questionada por alguns
  grupos), intervalo post-mortem, e mais recentemente divergência entre plataformas de
  transcriptômica de célula única/espacial — cada fator sozinho já explica parte da discordância
  entre laboratórios.
- **Datação por carbono-14 como método independente da imuno-histoquímica:** estima taxa de
  renovação neuronal em nível populacional a partir da incorporação de ¹⁴C atmosférico
  remanescente dos testes nucleares — não sofre dos mesmos problemas de anticorpo, mas também não
  identifica células individuais nem sua localização exata.
- **Modulação circadiana da neurogênese:** ablação de neurogênese altera especificamente a resposta
  ao estresse durante o ciclo escuro (período ativo de roedores) — ponte pouco explorada com a B10.
- **Aprimoramento farmacológico da neurogênese** como classe de composto experimental (2024-2025) —
  distinto de aumentar neurogênese por exercício/ambiente enriquecido, ainda em fase pré-clínica.
- **NMDA e neurogênese em direção oposta à sinaptogênese da B3/B5:** bloqueio de receptor NMDA
  **aumenta** proliferação de progenitores no giro denteado (achado de 1997, espécie tree shrew) —
  mecanismo aparentemente oposto ao da cetamina (que depende de ativação, não bloqueio, de
  AMPA/mTORC1 para sinaptogênese) operando na mesma via glutamatérgica geral.

## 2. Termos de busca alternativos

- Mecanismo: "dentate gyrus neural stem cell lineage", "doublecortin immature neuron marker",
  "radiocarbon dating human neurogenesis", "single-cell transcriptomics hippocampus neurogenesis",
  "hippocampal neurogenesis stress resilience".
- Ansiedade: "hippocampal neurogenesis anxiety non-monotonic", "exercise neurogenesis anxious
  phenotype", "pattern separation anxiety disorder".
- Método/confundidor: "tissue fixation protocol neurogenesis marker", "postmortem interval
  doublecortin", "antibody specificity adult neurogenesis controversy".

## 3. Áreas adjacentes subexploradas — priorizar

- **A relação não-monotônica com ansiedade** — praticamente ausente de resumos de divulgação, que
  tratam "mais neurogênese = melhor" como regra universal.
- **A persistência da discordância em 2024 mesmo com transcriptômica espacial** — contraria a
  narrativa popular de que a controvérsia já foi resolvida.
- **O mecanismo de circuito específico** (giro denteado ventral, "células responsivas ao estresse")
  — mais preciso e mais recente do que a narrativa genérica de "novos neurônios ajudam o humor".
- **Neurogênese farmacológica como classe emergente** — ainda muito nova, quase ausente de
  resumos de divulgação em português.

## 4. Crosstalk prioritário (equivalente ao BLOCO 08 da B1/B3-B12)

- **B16↔B2 (HPA):** relação bidirecional bem estabelecida — glicocorticoides suprimem
  neurogênese; reciprocamente, camundongos sem neurogênese têm retorno mais lento do cortisol ao
  basal após estresse, sugerindo que o giro denteado participa da própria retroalimentação negativa
  do eixo HPA.
- **B16↔B3 (plasticidade) — a fronteira mais próxima de toda a série:** B3 cobre plasticidade
  sináptica/estrutural de forma ampla (espinhos, BDNF, mTOR); B16 é especificamente o
  compartimento de células-tronco/progenitoras e a integração de neurônios inteiramente novos —
  processos relacionados mas mecanisticamente distintos (um remodela conexões existentes, o outro
  adiciona células novas à rede).
- **B16↔B5 (GABA/glutamato):** bloqueio de NMDA aumenta proliferação de progenitores — mecanismo
  na direção oposta ao papel do NMDA na sinaptogênese induzida por cetamina (B3/B5), mesma
  molécula-alvo, funções distintas dependendo do estágio celular afetado.
- **B16↔B10 (circadiano):** ablação de neurogênese altera especificamente a resposta ao estresse
  durante o ciclo escuro — interação pouco explorada fora deste achado específico.
- **B16↔B8 (micronutrientes)/exercício:** já tocado indiretamente na B3 (Cotman & Berchtold,
  Knaepen) — exercício aumenta neurogênese, mas o achado de ansiedade não-monotônica (Seção 8)
  complica a leitura simples de "exercício aumenta neurogênese, logo reduz ansiedade".

## 5. Polimorfismos / variantes a verificar

- Nenhum polimorfismo humano específico de neurogênese foi buscado com PMID nesta sessão — a
  maior parte do campo trabalha com manipulação genética em camundongo (ablação condicional,
  Nestin-CreERT2, Tbr2 condicional), não com variantes populacionais humanas. Candidato a lacuna
  real da área, não apenas desta sessão de busca.

## 6. Sinalizadores de extrapolação — o que NÃO entra como fato

- **"A controvérsia da neurogênese humana foi resolvida"** — um comentário de 2019 já usou esse
  enquadramento no próprio título; um estudo de 2024 com tecnologia mais avançada (transcriptômica
  espacial) **ainda encontra resultados discordantes**. Tratar como debate ativo, não fechado.
- **"Mais neurogênese é sempre melhor para ansiedade"** — falso pelo próprio desenho experimental
  mapeado aqui: aumentar neurogênese por corrida aumentou ansiedade; ablar a neurogênese induzida
  por corrida prevenil esse aumento; em outro estudo, aumentar neurogênese "por si só" não teve
  efeito ansiolítico. A relação é não-monotônica.
- **Extrapolar ablação causal de roedor diretamente para humano** — é experimentalmente impossível
  replicar em humano por razões éticas; toda evidência humana de causalidade é indireta
  (correlacional, post-mortem, ou inferência a partir de intervenção como exercício, que tem
  múltiplos outros efeitos simultâneos).
- **Contagem por imuno-histoquímica como medida definitiva** — a própria história da disputa
  (2018-2024) mostra que o método é sensível a decisões de protocolo que mudam completamente a
  conclusão; tratar contagens absolutas com cautela, preferir triangulação entre métodos
  (IHQ + carbono-14 + transcriptômica) quando disponível.

## 7. Cobertura equilibrada (não subrepresentar)

1. **A não-resolução da disputa humana em 2024**, não a versão "já foi resolvida" de 2019.
2. **A relação não-monotônica com ansiedade** — tão importante quanto o achado de que neurogênese
   "ajuda" na depressão, e muito menos citado.
3. **Mecanismo de circuito específico** (giro denteado ventral) ao lado da narrativa genérica de
   "novos neurônios = resiliência".
4. **Limite ético da evidência causal humana** — sempre mencionar que causalidade direta só existe
   em roedor.
5. **B16 como distinta de B3**, não repetição — apontar a fronteira conceitual explicitamente.

---

## 8. Camada clínica — evidência mapeada nesta sessão (ponto de partida; precisa de Rodada 2)

Tabela-semente. Cada PMID confirmado numa página que o cita explicitamente, durante busca ao vivo
nesta sessão (G1 caso a caso) — **não passou por G2/G3 nem pelos scripts de fidelidade**.

| Tema | Autor-ano | PMID | Tipo |
|---|---|---|---|
| Controle transcricional da diferenciação glutamatérgica na neurogênese adulta (linhagem celular) | Hodge, Kahoud & Hevner, 2012 | 22249196 | Revisão — biologia do nicho |
| *(referência cruzada, já citada na B3)* Neurogênese humana adulta quase ausente | Sorrells et al., 2018 | 29513649 | Estudo-chave — já citado em B3 |
| *(referência cruzada, já citada na B3)* Neurogênese humana persiste até a 8ª década | Boldrini et al., 2018 | 29625071 | Estudo-chave — já citado em B3 |
| Evidências para neurogênese hipocampal adulta em humanos (defesa da persistência, protocolo otimizado) | Moreno-Jiménez, Terreros-Roncal et al., 2021 | 33762406 | Revisão |
| Métodos para estudar neurogênese hipocampal adulta em humanos e na filogenia (revisão metodológica) | Terreros-Roncal, Flor-García et al., 2022 | 36259116 | Revisão metodológica |
| Neurogênese no hipocampo de adultos humanos: controvérsia "consertada" por fim (comentário — ler com ceticismo à luz de achados posteriores) | Lima & Gomes-Leal, 2019 | 31290449 | Comentário |
| **Análise transcriptômica espacial de neurogênese hipocampal adulta humana — resultados ainda discordantes com nova tecnologia** | Simard, Rahimian, Davoli et al., 2024 | 39414359 | Estudo humano (transcriptômica) — fronteira |
| Neurogênese no giro denteado de musaranho-árvore adulto é regulada por estresse psicossocial e ativação de receptor NMDA (marco histórico) | Gould, McEwen, Tanapat, Galea & Fuchs, 1997 | 9065509 | Mecanístico (musaranho) — marco |
| Estresse, hormônios do estresse e neurogênese adulta (revisão, nota o paradoxo de que corticosterona às vezes aumenta neurogênese) | Schoenfeld & Gould, 2011 | 21281629 | Revisão |
| **Neurogênese hipocampal adulta amortece respostas ao estresse e comportamento depressivo (evidência causal direta, ablação)** | Snyder, Soumier, Brewer, Pickel & Cameron, 2011 (Nature) | 21814201 | Mecanístico (camundongo) — marco causal |
| **Neurogênese confere resiliência ao estresse inibindo o giro denteado ventral — mecanismo de circuito específico** | Anacker, Luna, Stevens et al., 2018 (Nature) | 29950730 | Mecanístico (camundongo) — fronteira mecanística |
| Efeitos de exercício e estresse na sobrevivência/maturação de células granulares adultas (direções opostas) | Snyder, Glover, Sanzone, Kamhi & Cameron, 2009 | 19156854 | Mecanístico (camundongo) |
| **Neurogênese induzida por corrida aumenta ansiedade; ablação previne o aumento — relação não-monotônica** | Fuss, Ben Abdallah, Hensley, Weber, Hellweg & Gass, 2010 | 20862278 | Mecanístico (camundongo) — âncora ANSIEDADE |
| Ablação de neurogênese hipocampal prejudica a resposta ao estresse durante o ciclo escuro (modulação circadiana) | Tsai, Tsai, Arnold & Huang, 2015 | 26415720 | Mecanístico (camundongo) — crosstalk B16↔B10 |

**O que falta (prioridade da Rodada 2):**
1. PMID para o aprimoramento farmacológico da neurogênese (Chang, Tegang, Samuels et al., 2025,
   Biol Psychiatry Glob Open Sci) — citação bibliográfica completa localizada, PMID não confirmado
   nesta sessão.
2. Datação por carbono-14 (método de Frisén) — mencionado no checklist (Seção 1b), sem busca
   própria com PMID nesta sessão.
3. Mapa de ansiedade por transtorno específico além do achado geral de exercício/irradiação já
   mapeado aqui.
4. Polimorfismos genéticos humanos específicos de neurogênese — lacuna reconhecida da área, não
   só desta sessão (Seção 5).

## 9. Tabela de confundidores de biomarcador (importar para BLOCO 05/11)

| Marcador / exame | Confundidor a controlar | Ação na busca |
|---|---|---|
| Contagem de DCX/Ki67 (post-mortem, imuno-histoquímica) | protocolo de fixação, especificidade de anticorpo, intervalo post-mortem — a própria causa histórica da disputa Sorrells/Boldrini | reportar protocolo completo; preferir triangulação com outro método quando possível |
| Datação por carbono-14 | estima taxa populacional, não identifica células individuais nem localização | tratar como complementar à IHQ, não substituto |
| Transcriptômica de célula única/espacial | plataformas diferentes ainda produzem resultados discordantes entre si (Simard et al., 2024) | especificar plataforma; não comparar diretamente estudos com tecnologias distintas sem ressalva |
| Neurogênese induzida por exercício (proxy comportamental humano) | exercício tem múltiplos outros efeitos simultâneos (BDNF, cardiovascular, humor direto) — não isola neurogênese como mecanismo único | não atribuir todo benefício do exercício à neurogênese especificamente |

---

## 10. Estrutura-alvo da B16 (blocos do Prompt v4.2 — mesma numeração da B1/B3-B12)

- **BLOCO 02/03 (vias/mediadores):** sinalização Wnt/Notch na manutenção de células-tronco
  (checklist, sem PMID nesta sessão), regulação glicocorticoide, modulação por NMDA.
- **BLOCO 04 (células/estruturas):** linhagem completa tipo-1→tipo-2→neuroblasto→neurônio maduro;
  giro denteado ventral como circuito específico de resiliência.
- **BLOCO 05 (biomarcadores):** + tabela de confundidores (Seção 9); a disputa metodológica como
  item central, não nota de rodapé.
- **BLOCO 06 (tradução clínica):** neurogênese farmacológica como classe emergente pré-clínica;
  exercício como intervenção indireta — descritos sem prescrever (P20).
- **BLOCO 08 (crosstalk):** ver Seção 4 — B16↔B2/B3/B5/B10; destacar B16↔B3 como a fronteira
  conceitual mais próxima de toda a série, exigindo delimitação editorial clara.
- **BLOCO 11 (estratificação):** eixo "neurogênese ótima intermediária" vs. extremos (muito
  baixa OU muito alta) — modelo de curva em U, não hiper/hipo linear como em outras B.
- **BLOCO 12 (cenários):** cenário depressão-com-neurogênese-reduzida-responsiva-a-exercício,
  cenário ansiedade-por-neurogênese-excessiva-não-regulada (contra-intuitivo, mas documentado).

## 11. Plano de execução

1. **Rodada 1 (miolo molecular):** buscar PMID para neurogênese farmacológica (Chang et al., 2025)
   e datação por carbono-14 (Seção 1b) — ficaram só no checklist/prosa nesta sessão.
2. **Rodada 2 (corpus eutils):** ampliar mapa de ansiedade por transtorno específico; buscar
   polimorfismos humanos de neurogênese (lacuna reconhecida, Seção 5).
3. **Rodada 3 (fidelidade):** rodar `check_fidelidade_b1` e `check_troca_nomes`; **delimitar
   explicitamente a fronteira B3↔B16** antes de publicar, para não duplicar conteúdo entre os dois
   documentos; conferir que a relação não-monotônica com ansiedade não foi simplificada.
4. Publicar como **B16 v1** — não há canônica anterior para congelar.

> **Pendências da série que seguem em aberto:** B13 (endocanabinoide, 1 busca feita) e o salto de
> numeração B14/B15 (nunca solicitadas) continuam pendentes desta mesma conversa, não resolvidos
> por este documento.
