# B1 NEUROINFLAMAÇÃO V4 CANÔNICA
## Biblioteca de Conhecimento Canônica v3 — Mecanismo Fisiopatológico

**ID canônico:** mecanismo_B1_neuroinflamacao · **Natureza:** ferramenta de suporte à decisão — não diagnostica nem substitui o julgamento profissional.
**artefato_rotulo:** CANÔNICA v4 (ansiedade + depressão; atualização [AT] 2026-09-08 via P-7 — reconciliação de insumo externo auditado ref-a-ref: +49 referências verificadas eutils; v1/v2/v3 arquivadas em producao/historico/) (fonte única do mecanismo B1; o motor/RAG lê somente este arquivo + `/Evidencias/`).
**Corte de literatura:** 2026-09-04 · **Rodada de auditoria:** Rodada 4 — expansão v2 (trilho de ansiedade + imunometabolismo/necroptose/Cx43-AQP4/ansiedade) sobre a Rodada 3 consolidada; checklist de fidelidade canônica+estrutural e checagem de troca de nomes (autor↔referência, 184 citações) sem erros **encontrados nesta rodada**; as referências antes pendentes foram todas resgatadas no PubMed com PMID real. Auditoria por amostragem não garante ausência absoluta de erro. **Atualização [AT] 2026-09-08 (P-7):** insumo externo ("matriz canônica B1" de terceiro) auditado ref-a-ref — G1 eutils em 68/74 identificadores, **4 falsos positivos rejeitados e expostos**, 19 itens barrados por escopo/redundância/duplicidade, rótulos de autoria corrigidos contra o PubMed; **49 referências verificadas incorporadas nesta v4** por mini-ciclo Pré→G1-G3→nova versão (nunca edição direta); trilha completa em `producao/insumos/` e `Auditoria_B1/decisoes_B1.md`.
**Rastreabilidade:** cada afirmação científica tem lastro em referência catalogada no Módulo 9 (`/Evidencias/`) por vínculo frase↔referência; o catálogo de identificadores das referências, meta-análises e RCTs reside nesse módulo.

---

## Resumo para recuperação (semantic_layer)

1. Mecanismo de inflamação cerebral e sistêmica (NF-kB/NLRP3) que produz citocinas, desvio quinurenínico e supressão de plasticidade.
2. Serve para identificar o subtipo minoritário, mas replicado, de depressão/ansiedade associado a marcadores inflamatórios e a traducao sintoma-mecanismo.
3. Usar como lastro biológico do subtipo inflamatório e para raciocínio de estratificação — não para diagnóstico nem conduta.

**Recuperar quando: depressão/ansiedade com inflamação, citocinas elevadas, anedonia/recompensa, TSPO/PCR/IL-6, resistência a antidepressivo, paradigma interferon, priming microglial; TSPO negativo/heterogêneo, micróglia humana não-inflamatória, primeiro episódio drug-naïve, NLRP3 priming/ativação, piroptose astrocitária, saída GSDMD-independente, antidepressivo e citocina (sonda), periferia≠centro.**

**Domínios clínicos:** fisiopatologia, biomarcadores, estratificacao · **Prioridade de incorporação:** alta

**Palavras-chave:** neuroinflamacao, NLRP3, NF-kB, IL-6, TNF, IDO quinurenina, TSPO, microglia, sickness behavior, inflamacao baixo grau, FKBP5, SPMs resolucao

**Mecanismos relacionados (IDs oficiais):** mecanismo_B2_eixo_hpa_cortisol, mecanismo_B3_neuroplasticidade, mecanismo_B4_deficiencias_monoaminas, mecanismo_B5_gaba_glutamato, mecanismo_B6_estresse_oxidativo, mecanismo_B7_eixo_intestino_cerebro, mecanismo_B8_deficiencias_micronutrientes, mecanismo_B9_disfuncao_mitocondrial, mecanismo_B10_desregulacao_circadiana, mecanismo_B11_disfuncao_tireoidiana, mecanismo_B12_neurobiologia_trauma, mecanismo_B13_sistema_endocanabinoide, mecanismo_B14_neuroesteroides_hormonios, mecanismo_B15_autofagia_mtor, mecanismo_B16_neurogenese

---
## BLOCO_00 — IDENTIDADE E ASSINATURA SEMÂNTICA

**Frase-síntese canônica:**
A neuroinflamação (B1) é a ativação sustentada de vias imunes inatas — centralmente o eixo NF-κB (nó transcricional) e o inflamassoma NLRP3 (nó executor) — que converte estresse, infecção, trauma precoce, disbiose ou senescência em produção de citocinas (IL-1β, IL-6, TNF-α), desvio quinurenínico do triptofano (IDO) e supressão da plasticidade/neurogênese mediada por BDNF, caracterizando um subtipo biológico — minoritário (subgrupo com PCR elevada), replicado meta-analiticamente — de ansiedade e depressão.

**Assinatura molecular (impressão digital para RAG):**
1. Cascata PAMP/DAMP → TLR4/MyD88 → IRAK/TRAF6 → IKK → NF-κB → priming de NLRP3 e transcrição de IL1B/IL6/TNF/PTGS2.
2. Inflamassoma NLRP3 (dois sinais) → ASC → caspase-1 → IL-1β/IL-18 maduros + GSDMD/piroptose.
3. Desvio do triptofano por IDO1: astrócito→KYNA (neuroprotetor) vs. micróglia→QUIN (neurotóxico).
4. Resolução ativa por SPMs (resolvinas/protectinas/maresinas) e freios IL-10/STAT3, miR-146a, GR — a falha do "desligamento" cronifica.
5. Priming microglial e memória imune inata (epigenética/H3K18) como base da cronificação.

**Moléculas compartilhadas (resolver por papel, não por nome):** cortisol/GR/FKBP5 (B2), BDNF/TrkB/CREB (B3), triptofano/5-HT e SERT (B4), QUIN/NMDA (B5), ROS mitocondrial (B6/B9), LPS/permeabilidade intestinal (B7), vitamina D/zinco (B8), relógio/sono (B10), tireoide/D2 (B11), FKBP5/trauma (B12), endocanabinoides CB2 (B13), esteroides neuroativos (B14), neurogênese hipocampal (B16).

**Nós centrais (BLOCO_07):** NF-κB (transcrição/priming) e NLRP3 (execução) — síntese dedicada no BLOCO_07.

---
## BLOCO_01 — FUNDAMENTOS

### 1.1 — Estado fisiológico: ativação adaptativa e o limiar para a patologia

Em condições saudáveis, a interação sistema imune–cérebro é um programa **adaptativo e autolimitado**, não uma falha. Diante de patógeno, lesão tecidual ou estressor agudo, células mieloides (monócitos, macrófagos, micróglia) reconhecem motivos moleculares conservados (PAMPs, ex. LPS bacteriano; DAMPs de células lesadas) por receptores de reconhecimento padrão — TLR2/4 e o inflamassoma NLRP3 — e disparam transcrição NF-κB de citocinas pró-inflamatórias (IL-1β, IL-6, TNF-α) seguida de maturação por caspase-1 (Swanson et al., 2019)[OB; revisão, humano+animal] [VERIFICADO]. Essa ativação aguda é programada para **resolver ativamente**: mediadores lipídicos pró-resolutivos especializados (SPMs — resolvinas D/E, protectinas, maresinas, lipoxina A4), derivados do metabolismo de ômega-3/6, sinalizam a parada do recrutamento neutrofílico, o clearence de células apoptóticas por macrófagos e o retorno da micróglia ao estado ramificado homeostático (Serhan, 2014)[OB; revisão fisiológica, humano+animal; Serhan & Levy, 2018] [VERIFICADO][OB]. A micróglia homeostática exerce vigilância contínua com processos móveis, sem produção sustentada de citocinas (Perry & Teeling, 2013)[OB; revisão, humano+camundongo] [VERIFICADO].

O que distingue ativação **adaptativa** de **patológica** não é a presença de citocinas — elas são fisiológicas — e sim três parâmetros: **duração** (horas/dias vs. semanas/anos), **magnitude** (pico transitório vs. elevação de baixo grau contínua, "low-grade inflammation"/inflammaging) e, sobretudo, **capacidade de resolução ativa** (Barrientos et al., 2015)[OB; revisão, camundongo+humano] [EXTRAPOLADO: animal/célula→humano]. Quando o programa de resolução falha — por SPMs insuficientes, senescência celular ("SASP" secretando citocinas em baixo grau contínuo) ou reprogramação metabólica da micróglia (glicólise/mtROS sustentando o fenótipo pró-inflamatório) — a resposta deixa de ser autolimitada. O estado resultante é de **priming microglial**: a micróglia permanece "sensibilizada", com limiar rebaixado, e responde de forma amplificada e prolongada a um segundo desafio (Norden et al., 2015)[OB; revisão, humano] [EXTRAPOLADO: animal/célula→humano]. Esse limiar adaptação↔patologia é o eixo conceitual de todo o mecanismo B1: a neuroinflamação clínica não é "inflamação no cérebro" como evento pontual, e sim a **falha do desligamento** de um programa que, em sua forma aguda, é protetor.

---

*Swanson_2019[ML] | Serhan_2014[ML] | Serhan_Levy_2018[ML] | Perry_Teeling_2013[ML] | Barrientos_2015[ML] | Norden_2015[ML]*

### 1.2 — Sickness behavior: o modelo de neuroinflamação aguda adaptativa (BLOCO01.002)

O melhor modelo de neuroinflamação aguda fisiológica é o **sickness behavior** (comportamento de adoecimento): após administração de LPS ou indução por citocinas, o organismo exibe um conjunto coordenado e estereotipado — retraimento social, anedonia transitória, fadiga/hipersonia, redução de exploração e apetite, hiperalgesia leve — que redireciona energia para combate ao patógeno e reparo (Dantzer et al., 2001)[EC; revisão mecanística, camundongo+humano] [VERIFICADO]. Cronologicamente, o quadro inicia-se em horas (pico de citocinas 2–6 h pós-LPS), atinge o máximo comportamental em 6–24 h e **resolve espontaneamente em 24–72 h** com o término do estímulo e a entrada dos programas de resolução — inclusive febre e sickness foram reinterpretados como respostas amigas ou adversas a depender do contexto temporal (Harden et al., 2015)[OB; revisão, camundongo+humano] [EXTRAPOLADO: animal/célula→humano]. A via molecular está descrita: citocinas periféricas sinalizam ao cérebro por vias neurais (nervo vago), humorais (transporte através da barreira e em órgãos circunventriculares) e celulares (monócitos trafegando), e ativam IL-1β central e IDO — a transição de sickness para comportamento tipo-depressivo persistente é mediada pela via da quinurenina induzida por citocinas (Dantzer, 2006)[OB; revisão, camundongo+humano] [EXTRAPOLADO: animal/célula→humano].

A distinção crucial para a clínica: **sickness é agudo e autolimitado; depressão associada a inflamação é crônica e não resolve**. No animal, o LPS induz comportamento tipo-depressivo transitório que depende de IDO1 (O'Connor et al., 2009)[ML; camundongo] [PRÉ-CLÍNICO]; quando o estímulo inflamatório persiste ou se repete (estresse crônico, envelhecimento, infecção latente), a resposta não retorna à linha de base — é a ponte para o item 1.3.

---

*Dantzer_2001[ML] | Harden_2015[ML] | Dantzer_2006[ML] | OConnor_2009[ML]*

### 1.3 — Cronificação: priming microglial e memória imune inata (BLOCO01.003)

A passagem do estado agudo resolutivo para a neuroinflamação crônica tem um correlato molecular: o **priming (sensibilização) microglial**. Após um primeiro insulto — infecção sistêmica, lesão, estresse crônico, envelhecimento ou inflamação neonatal — a micróglia (e macrófagos perivasculares) mantém uma assinatura transcricional e epigenética alterada: limiar de ativação rebaixado, resposta amplificada a um segundo estímulo (menor dose de LPS já induz resposta maior e mais longa) e resolução mais lenta (Perry & Teeling, 2013)[OB; revisão, camundongo+humano]; (Norden et al., 2015)[OB; revisão, humano]. No envelhecimento normal do hipocampo, o priming é acompanhado de aumento basal de IL-1β e microgliose — terreno no qual uma infecção ou cirurgia ("segundo golpe") desencadeia delirium/declínio persistente (Barrientos et al., 2015)[OB; revisão, camundongo+humano].

Experimentalmente, o priming tem janela temporal longa: inflamação neonatal induz priming microglial no hipocampo ventral via regulação epigenética, persistindo até a vida adulta e aumentando a vulnerabilidade comportamental (Yang et al., 2026)[ML; camundongo]; lesão cerebral leve repetida ("mTBI") cria vulnerabilidade a insultos subsequentes por priming (Qiu et al., 2026)[ML; camundongo] [PRÉ-CLÍNICO]. Em nível mecanístico, o priming associa-se a: (a) manutenção do "sinal 1" transcricional (NF-κB/priming de pró-IL-1β) sem resolução; (b) disfunção mitocondrial e mtROS (crosstalk B9) baixando o limiar do inflamassoma; (c) SPMs insuficientes; (d) marcações epigenéticas em células imunes e centrais. Em humanos, o priming é inferido por marcadores (PCR/IL-6 persistentemente elevados, sinal TSPO-PET aumentado — ver BLOCO05) e por epidemiologia (infecção/adversidade precoces como fator de risco tardio); a demonstração causal direta é animal/in vitro, e essa fronteira [EXT] é mantida explícita ao longo da Biblioteca.

---

*Norden_2015[ML] | Barrientos_2015[ML] | Yang_2026_neonatal[ML] | Qiu_2026_mTBI[ML] | Perry_Teeling_2013[OB]*

### 1.4 — Notas de espécie e extrapolação

- A cascata PAMP/DAMP → TLR/NLRP3 → NF-κB → caspase-1 → IL-1β/IL-18 é **causal e manipulável em camundongo/célula**; em humanos o elo é fechado por marcadores, genética e intervenção de prova (IFN-α, anti-citocina em subgrupo — BLOCO05/06). Toda vez que um achado animal embasar uma afirmação sobre o paciente humano, ela é sinalizada como extrapolada ([EXT]) — a fronteira entre o que foi demonstrado em camundongo/célula e o que é fechado em humano é mantida explícita em toda a Biblioteca.
- Sickness behavior é conservado em vertebrados (Lopes, 2021)[OB; revisão comparada] [EXTRAPOLADO: animal/célula→humano], reforçando que se trata de programa adaptativo evolutivo — mas a tradução para "sintoma depressivo humano" é análoga [EXT], não identidade.

---
Evidência pré-clínica da via (Lopes_2021[ML]; modelo animal, [APENAS PRÉ-CLÍNICO]).

---

## BLOCO_02 — VIAS MOLECULARES DO MECANISMO

### 2.1 — Inflamassoma NLRP3: sequência de ativação e prova causal (BLOCO02.001)

O NLRP3 é o inflamassoma mais implicado na neuroinflamação. Sua ativação exige **dois sinais**: o sinal 1 (priming) — TLR4/TNFR/IL-1R → NF-κB — induz a transcrição de NLRP3 e da pró-IL-1β; o sinal 2 (ativação) — disparado por ATP/P2X7, dano mitocondrial (mtROS, mtDNA), eflixo de K+ ou cristais — promove a montagem do complexo NLRP3–ASC–pró-caspase-1, com autoclivagem da caspase-1 e maturação de IL-1β/IL-18 e clivagem de GSDMD (Swanson et al., 2019)[OB; revisão, humano+animal]. A dependência de dois sinais é explorada fisiologicamente como tolerância: em macrófagos, o itaconato induzido por TLR regula o sinal 2 após priming prolongado por LPS, estabelecendo **tolerância à ativação tardia do NLRP3** em sinergia com iNOS — demonstração manipulável de que priming e ativação são etapas dissociáveis (Bambouskova et al., 2021)[ML; camundongo] [PRÉ-CLÍNICO]. A prova de que a montagem do complexo é necessária e suficiente vem da genética humana: variantes ganho-de-função de NLRP3 (síndromes cryopyrin/CAPS) formam inflamassomas **constitutivamente ativos**, com clivagem basal de gasdermina D, liberação de IL-18 e piroptose mesmo sem gatilho externo — em pacientes e modelos animais (Molina-López et al., 2024)[EC; humano+camundongo] [EXTRAPOLADO: animal/célula→humano][EXT para TDM]. Em SNC, a inibição seletiva de NLRP3 reduz inflamação e dano em modelos [ML; EXT]. Natureza: causal em animal/célula; em humanos o elo para depressão é fechado por marcadores e intervenção (ver BLOCO05).

**[AT 2026-09-08] Lastro translacional do NLRP3 em depressão (pré-clínico → humano):** em modelo de estresse crônico leve, a via NLRP3/caspase-1 no hipocampo media o fenótipo tipo-depressivo, e seu bloqueio (farmacológico ou genético) o reverte (Zhang et al., 2015)[ML; camundongo] [APENAS PRÉ-CLÍNICO]. A revisão clínico–pré-clínica do eixo consolida aumento de componentes do inflamassoma (NLRP3, ASC, caspase-1, IL-1β) em sangue periférico e em cérebro pós-morte de pacientes com TDM (Kaufmann et al., 2017)[OB; revisão, humano+animal]. Revisão sistemática/meta-análise de 2026 sobre **modelos animais** conclui que tanto o **priming** quanto a **ativação** do NLRP3 participam da patologia tipo-depressiva — as duas etapas dissociáveis deste BLOCO têm assim lastro agregado (McColgan et al., 2026)[MA; pré-clínico, modelos animais]. O bloqueio microglial de NLRP3 por antagonista experimental (MCC950) atenua o eixo NLRP3/caspase-1/IL-1β e a morfologia reativa da micróglia em modelo — leitura estrita como **sinal experimental de alvo validável**, sem qualquer implicação posológica em humano (regra P20) (Liu et al., 2022b)[ML; camundongo] [APENAS PRÉ-CLÍNICO]. Revisões recentes detalham mecanismos e janelas de modulação do NLRP3 na depressão (Kouba et al., 2022; Xia et al., 2023)[OB] e nas doenças do SNC em geral (Xu et al., 2025)[OB; revisão multi-condições — especificidade para TDM limitada]. Natureza: causal em animal (bem_suportado); em humano, envolvimento por marcadores/pós-morte — moderadamente_suportado.

---

*Swanson_2019[ML] | Bambouskova_2021[ML] | CAPS_2024[EC] | Zhang_2015[ML] | Kaufmann_2017[OB] | Liu_2022b[ML] | Kouba_2022[OB] | Xia_2023[OB] | Xu_2025[OB] | McColgan_2026[MA]*

### 2.2 — Outros inflamassomas no SNC: NLRP1, AIM2, NLRC4 (BLOCO02.002)

Os inflamassomas são complexos supramoleculares citosólicos que respondem a PAMPs/DAMPs e desencadeiam liberação de citocinas e piroptose; a família inclui NLRP3, NLRP1, AIM2 (sensor de DNA) e NLRC4, com estruturas e ligantes distintos (Fu et al., 2024)[OB; revisão, humano+animal] [VERIFICADO]. No parênquima cerebral, há evidência direta de via análoga para **NLRP1 em neurônios**: após hemorragia intracerebral experimental, a ativação de CCR5 promove piroptose neuronal dependente de NLRP1 via CCR5/PKA/CREB, e o antagonismo de CCR5 (maraviroc) reduz o dano (Yan et al., 2021)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]. AIM2 aparece como sensor de DNA em contexto de morte celular imune na neuroinflamação (Rajesh et al., 2022)[OB; revisão] [EXTRAPOLADO: animal/célula→humano][EXT]; NLRC4 tem evidência indireta. Maturidade: NLRP3 bem_suportado; NLRP1 neuronal emergente; AIM2/NLRC4 hipótese_inicial no SNC comportamental.

---

*Inflamassomas_2024[ML] | CCR5_NLRP1_2021[ML] | InnateCellDeath_2022[ML]*

### 2.3 — Gasderminas como efetoras da piroptose (BLOCO02.003)

A piroptose é executada pela família das gasderminas. Demonstração recente e forte no SNC: a **ativação de GSDMD no endotélio cerebral** — pela caspase-11 sensora de LPS citosólico, e não pelas citocinas induzidas por TLR4 — medeia a ruptura inflamatória da barreira hematoencefálica na sepse/desafio com LPS circulante; camundongos deficientes na via LBP–CD14 de internalização de LPS resistem à quebra da barreira (Wei et al., 2024)[EC; camundongo+humano] [EXTRAPOLADO: animal/célula→humano][EXT]. Em microglia, GSDMD medeia piroptose na encefalopatia séptica via eixo TRIM45/Atg5/NLRP3 (Huang et al., 2023)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]. GSDME (executor alternativo, acionado por caspase-3) é citado em revisões de morte celular imune no SNC [OB; EXT]. Natureza: causal em animal; a relevância direta para comportamento depressivo é emergente.

**[AT 2026-09-08] Piroptose além da micróglia — e a saída sem GSDMD:** em modelo de depressão, a piroptose por NLRP3/caspase-1/GSDMD ocorre também em **astrócitos**, contribuindo para injúria astrocitária patológica — a morte lítica inflamatória não é privilégio microglial (Li et al., 2021)[ML; camundongo] [APENAS PRÉ-CLÍNICO]. Nuance canônica obrigatória: a ativação de NLRP3 pode deflagrar inflamação **independente de GSDMD** (resposta secretora não-lítica) — portanto "NLRP3 ativo" **não** equivale automaticamente a "piroptose" (Wang et al., 2021)[ML; camundongo] [APENAS PRÉ-CLÍNICO]. Em doenças neurodegenerativas, a piroptose neuronal mediada por NLRP3 é revista como mecanismo compartilhado entre condições (Han et al., 2023b)[OB; neurodegeneração] [EXTRAPOLADO: neurodegeneracao→TDM]. Natureza: arquitetura celular causal em animal; presença em depressão humana por inferência — emergente.

---

*GSDMD_BBB_2024[ML] | TRIM45_2023[ML] | Li_2021[ML] | Wang_2021[ML] | Han_2023b[OB]*

### 2.4 — TLR4 como receptor de LPS até NF-κB (BLOCO02.004)

O TLR4 (com co-receptores MD-2/CD14) é o receptor canônico do LPS. A via completa — LPS → TLR4/MyD88 → IRAK/TRAF6 → IKK → degradação de IκBα → NF-κB nuclear → transcrição de IL1B/IL6/TNF — é demonstrada por manipulação: o desafio com LPS induz sickness, déficit cognitivo e ativação microglial (Iba-1+) em camundongos, com elevação de citocinas pró-inflamatórias, bloqueável por interferência na via (Zhao et al., 2019)[ML; camundongo] [PRÉ-CLÍNICO]. A modulação farmacológica a jusante confirma os elos: gastrodina reduz neuroinflamação e ativação microglial regulando TLR4/TRAF6/NF-κB (Wang et al., 2024)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]. Causal e bem_suportado em animal; a tradução para inflamação humana de baixo grau é associativa/[EXT].

---

*LPS_cog_2019[ML] | Gastrodin_2024[ML]*

### 2.5 — TLR2 e TLR3: vias distintas (BLOCO02.005)

TLR2 (lipopeptídeos de Gram-positiva, com TLR1/6) e TLR3 (RNA de fita dupla/viral e RNAs extracelulares) têm ligantes e efeitos próprios. TLR3 neuronal é relevante para função cognitiva: em camundongos com dor neuropática crônica, RNAs extracelulares sinalizam via TLR3 no hipocampo e contribuem para o declínio cognitivo; o knockout de TLR3 e o knockdown neuronal específico melhoram a cognição, reduzem citocinas e apoptose neuronal versus selvagens (Zhang et al., 2023)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]. TLR2 media resposta imune a bactéria em nociceptores de forma distinta da via glial (Chiu et al., 2013)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano]. Em glia, TLR2 responde a componentes de parede bacteriana com produção de citocinas [OB]. Maturidade: bem_suportado em animal; humanos [EXT].

---

*TLR3_2023[ML] | TLR2_nociceptor_2013[ML]*

### 2.6 — RLRs (RIG-I/MDA5) no SNC: inventário honesto (BLOCO02.006)

Não há literatura direta robusta ligando **RIG-I/MDA5** a comportamento/neuroinflamação depressiva. O que existe é periférico: TBK1 — que integra a sinalização de RLRs e cGAS-STING para IFN tipo I e NF-κB — quando perdido em humanos por mutações homozigotas causa autoinflamação crônica sistêmica dirigida por morte celular induzida por TNF, sem infecções virais graves (Taft et al., 2021)[EC; humano] [VERIFICADO]. Isso documenta a existência da maquinaria de detecção de RNA/DNA e sua interseção com TNF, mas **não estabelece RLRs como via de neuroinflamação comportamental**. Estado: `nao_estabelecido` / escassez de evidência direta — registrado como N/A parcial no inventário negativo, não forçado.

---

Perda homozigota de TBK1 integra sinalização RLR/cGAS→IFN na neuroinflamação (TBK1_2021[EC]).

### 2.7 — RAGE e receptores scavenger para DAMPs (BLOCO02.007)

O receptor de produtos finais de glicação avançada (RAGE) é o principal receptor de DAMP para S100 e HMGB1 no SNC. A família S100 compreende 24 membros com funções intra/extracelulares, alguns induzidos em patologia em células que não os expressam normalmente (Donato et al., 2013)[OB; revisão, humano+animal] [VERIFICADO]. RAGE em astrócitos é tratado como "mais que uma questão de humor" pela literatura (Franklin et al., 2018)[ML; camundongo] [PRÉ-CLÍNICO]. A ligação DAMP–RAGE aciona NF-κB e produz retroalimentação positiva (RAGE é induzível por NF-κB). Detalhes dose-dependentes em 2.24.

---

*S100func_2013[ML] | RAGE_stress_2018[ML]*

### 2.8 — HMGB1 como DAMP (BLOCO02.008)

HMGB1 é uma proteína nuclear liberada por células lesadas/piroptóticas ou secretada ativamente; a forma **dissulfeto-HMGB1** (oxidada) é a imunoativa, sinalizando via RAGE/TLR4. Em lesão cerebral isquêmica, ácido hipocloroso derivado de mieloperoxidase microglial oxida HMGB1 facilitando sua secreção e amplificando a neuroinflamação (Chen et al., 2024)[ML; rato+humano] [EXTRAPOLADO: animal/célula→humano][EXT]. Em revisão focada em depressão, DAMPs (incluindo HMGB1) são apresentados como alarmes que disparam ativação microglial e liberação de citocinas na TDM, com modulação lipídica (Malau et al., 2024)[OB; revisão, humano+animal] [VERIFICADO]. Natureza: mecanística em animal; associação em depressão [EXT], emergente.

---

*HMGB1_HOCl_2024[ML] | Omega3_DAMP_2024[EC]*

### 2.9 — DNA mitocondrial livre como DAMP ativador de NLRP3 (BLOCO02.009)

O mtDNA extracelular/livre funciona como DAMP: ativa inflamassomas e a resposta de IFN via cGAS-STING (ver 2.18). Em lesão pulmonar aguda induzida por DAMP mitocondrial, miR-223 de neutrófilos Ly6G+ inibe o NLRP3 — demonstrando que DAMPs mitocondriais são gatilho fisiológico do complexo (Feng et al., 2017)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]. A disfunção mitocondrial e o "inflamm-aging" são alimentados por vazamento de mtDNA e sinalização imune (Picca et al., 2017)[OB; revisão, humano] [EXTRAPOLADO: animal/célula→humano]. Elo causal específico com comportamento depressivo: cross-ref B9 (disfunção mitocondrial); no B1, fica como mecanismo a montante do NLRP3, causal em modelos de dano, [EXT] para TDM.

---

*miR223_2017[ML] | InflammAging_2017[EC]*

### 2.10 — Via da quinurenina: bifurcação celular e enzimas (BLOCO02.010)

O triptofano é desviado da serotonina para a via da quinurenina por ação de **IDO1** (induzida por citocinas/IFN-γ), IDO2 e TDO2. A bifurcação celular é funcionalmente oposta: em **astrócitos**, KAT (kynurenine aminotransferase) gera **KYNA** (ácido quinurênico) — antagonista NMDA no sítio glicina/agonista α7nACh, neuroprotetor; em **micróglia/macrófagos**, KMO direciona para **QUIN** (ácido quinolínico) e 3-HK — agonista NMDA, gerador de ROS, neurotóxico. A IDO1 e a via são reguladoras centrais do envelhecimento e da imunidade (Salminen et al., 2022)[OB; revisão, humano], e o eixo triptofano–quinurenina é apontado como ligação intestino-cérebro na depressão inflamatória (Chen et al., 2021)[OB; revisão, humano+animal]. Em adolescentes deprimidos, metabolômica de triptofano e microbioma associam-se ao fenótipo [EC; humano]. A prova causal de que a transição sickness→depressão depende de IDO foi mostrada em camundongo (O'Connor et al., 2009)[ML] no BLOCO01. Natureza: enzimas e bifurcação muito_estabelecido; direção em depressão bem_suportado.

**[AT 2026-09-08] TRYCATs em humano e espacialização cerebral da via:** meta-análise de catabolitos do triptofano no episódio depressivo atual documenta alterações de TRYCATs — redução de quinurenina e das razões neuroprotetoras/neurotóxicas — sobretudo nos subtipos melancólico, psicótico e na ideação suicida (Almulla et al., 2022)[MA; humano]. Em depressão, os metabólitos da via no sangue e no líquor associam-se a marcadores inflamatórios com **concordância apenas parcial** entre compartimentos — reforço empírico da regra "periferia ≠ centro" (Haroon et al., 2020)[EC; humano]. Revisões recentes consolidam a via como interface imune–neurotransmissão (Savitz, 2020; Stone et al., 2024; Badawy, 2023; Bertollo et al., 2025)[OB; revisão], sua desregulação como convergência excitotóxico-neuroinflamatória no TDM (O'Regan et al., 2026)[OB; fronteira] e sua regulação contextual como candidata a estratificação personalizada (Murata et al., 2026)[OB; fronteira]. No território pré-clínico, o metabolismo neurotóxico da quinurenina aumenta seletivamente no **hipocampo dorsal** e dirige comportamentos tipo-depressivos distintos (Parrott et al., 2016)[ML; camundongo] [APENAS PRÉ-CLÍNICO], e o estresse crônico leve remodela a via alterando a neurotransmissão glutamatérgica no córtex frontal (Martín-Hernández et al., 2019)[ML; rato] [APENAS PRÉ-CLÍNICO]. Natureza: enzimas/bifurcação muito_estabelecido; subtipos fenomenológicos moderadamente_suportado.

---

*KYN_gutbrain_2021[ML] | IDO1_aging_2022[ML] | OConnor_2009[ML] | Almulla_2022[MA] | Haroon_2020[EC] | Savitz_2020[OB] | Stone_2024[OB] | Badawy_2023[OB] | Bertollo_2025[OB] | ORegan_2026[OB] | Murata_2026[OB] | Parrott_2016[ML] | MartinHernandez_2019[ML]*

### 2.11 — TNF solúvel/TNFR1 vs. TNF transmembrana/TNFR2 (BLOCO02.011)

O TNF tem dois receptores de sinal oposta: **TNFR1 (p55)**, acionado sobretudo por TNF solúvel, medeia resposta pró-inflamatória/apoptótica/necroptótica; **TNFR2 (p75)**, preferencialmente ativado por TNF transmembrana, é homeostático/neuroprotetor e imunorregulador. Em modelo de Alzheimer, a necroptose neuronal dependente de TNF-α é regulada pela coordenação RIPK1 (Xu et al., 2021)[ML; camundongo+humano] [EXTRAPOLADO: animal/célula→humano][EXT]. Ao contrário, TNFR2 em microglia molda propriedades remielinizantes e protetoras após dano, de forma sexo-dependente (Raffaele et al., 2025)[ML; camundongo+humano] [EXTRAPOLADO: animal/célula→humano][EXT]. Em modelo de depressão induzida, a inibição de microglia/neuroinflamação por arctigenina envolve a redução de TNF (Xu et al., 2020)[ML; camundongo] [PRÉ-CLÍNICO]. A distinção de isoforma de receptor é assim causal em animal; a maioria dos estudos clínicos mede "TNF total" e não separa os ramos — limitação registrada para o marcador (BLOCO05).

---

*TNFR1_RIPK1_2021[ML] | TNFR2_2025[ML] | Arctigenin_2020[ML]*

### 2.12 — Polimorfismos funcionais e genética (BLOCO02.012)

A genética funcional da inflamação fornece prova humana. O achado mais diretamente ancorado nesta trilha: polimorfismos funcionais em **IL-6 (rs1800795/-174G>C)** e no transportador de serotonina (5-HTTLPR) modificam a depressão induzida por interferon-α em hepatite C — variantes que elevam sinalização IL-6 associam-se a maior risco de depressão sob terapia com citocina (Bull et al., 2009)[EC; humano] [VERIFICADO]. É interação gene–ambiente (genótipo × exposição inflamatória), não associação transversal pura. Para FKBP5, ver 2.20. Para outras variantes (IL1B, TNF -308G/A, TLR4, NLRP3, CRP), a literatura genética disponível não testa diretamente esses polimorfismos no contexto; permanecem como `(gene, associação reportada)` sem estudo dedicado — a direção funcional (alelo hiper-expressor aumenta transcrição pró-inflamatória) é proposta na literatura e fica para confirmação em estudos de genética humana. Natureza do conjunto: associativo/interação em humano.

---

*Bull_2009[EC]*

### 2.13 — Lipídios pró-resolutivos (SPMs): resolução ativa (BLOCO02.013)

A resolução é um programa ativo, não a simples diluição da inflamação. Mediadores lipídios especializados — resolvinas (série E de EPA e D de DHA), protectinas/PD1/NPD1, maresinas (MaR), lipoxina A4 (do araquidônico) — produzidos por lipoxigenases, param o recrutamento neutrofílico, promovem eferocitose e retornam tecidos à homeostase (Serhan, 2014)[OB; revisão, humano+animal]; a superfamília das resolvinas é detalhada quanto a receptores e ações (Serhan & Levy, 2018)[OB; revisão] [VERIFICADO]. Em dor neuropática, mecanismos imunes pró-resolutivos são mapeados como alvo terapêutico (Fiore et al., 2023)[OB; revisão], e a maresina MaR2 derivada de tecido adiposo marrom contribui para a resolução da inflamação no frio (Sugimoto et al., 2022)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]. O GPR37 em macrófagos regula fagocitose e resolução da dor inflamatória (Bang et al., 2018)[ML; camundongo+humano] [EXTRAPOLADO: animal/célula→humano][EXT]. Em depressão, a insuficiência relativa de SPMs é hipótese mecanística [EXT; gap_pesquisa].

---

*Serhan_2014[ML] | Serhan_Levy_2018[OB] | PainResolv_2023[ML] | GPR37_2018[ML] | MaR2_2022[ML]*

### 2.14 — Senescência celular e SASP em glia (BLOCO02.014)

Células senescentes secretam um fenótipo secretório associado à senescência (SASP) — citocinas/quimiocinas/proteases em baixo grau contínuo. Em microglia senescente no envelhecimento/Alzheimer, a lactilação de histona H3K18 potencializa o SASP e o declínio cerebral (Wei et al., 2023)[ML; camundongo+humano] [EXTRAPOLADO: animal/célula→humano][EXT]. O envelhecimento celular e a senescência estão consolidados como mecanismo de neuroinflamação crônica (Liu et al., 2022)[OB; revisão] [EXTRAPOLADO: animal/célula→humano]. Astócitos reativos associados a neuropatologia são revisados sistematicamente (Lawrence et al., 2023)[OB; revisão, humano+animal] [VERIFICADO]. Nível de evidência para ansiedade/depressão: o SASP glial é bem demonstrado em envelhecimento/neurodegeneração; a extrapolação para transtornos de humor é análoga [EXT], parte do conceito de inflamação de baixo grau.

---

*H3K18_2023[ML] | Senesc_2022[ML] | AstroReat_2023[OB]*

### 2.15 — Via NF-κB: sequência completa receptor→transcrição (BLOCO02.015)

O NF-κB é o nó transcricional da inflamação. Sequência: receptor (TLR4/MyD88, TNFR1 ou IL-1R1) → **IRAK/TRAF6 → complexo IKK → fosforilação e degradação de IκBα → libertação e translocação nuclear de NF-κB (p65/p50)** → transcrição de IL1B, IL6, TNF, NLRP3 (priming), PTGS2 (COX-2) e NOS2 (iNOS). A via é confirmada por manipulação em microglia: gastrodina reduz neuroinflamação agindo em TLR4/TRAF6/NF-κB (Wang et al., 2024)[ML; camundongo], e o polifenol punicalina atenua prejuízo de memória induzido por LPS por supressão da mesma cascata (Chen et al., 2024)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]. A resistência a glicocorticoides (BLOCO08/B2) desinibe o NF-κB porque o GR ativado normalmente reprime esta via. Causal e muito_estabelecido em sistemas imunes/neurais; humano por marcadores [EXT].

---

*Gastrodin_2024[ML] | Punicalin_2024[ML]*

### 2.16 — JAK-STAT e interferon: o paradigma causal humano (BLOCO02.016)

IFN tipo I (IFN-α/β via IFNAR) e tipo II (IFN-γ via IFNGR) sinalizam por JAK1/JAK2/TYK2 → STAT1/STAT2 → genes estimulados por IFN (ISGs), incluindo **indução de IDO1** (2.10). O paradigma de causalidade humana mais próximo de B1 é a **depressão induzida por interferon-α**: pacientes tratados com IFN-α (hepatite C/melanoma) desenvolvem sintomas depressivos de novo com curso previsível, e a maquinaria JAK-STAT/IDO está documentada em células-tronco neurais (Zheng et al., 2014)[ML; célula+revisão]; um composto natural (paeoniflorin) alivia neuroinflamação e comportamento tipo-depressivo induzidos por IFN-α (Li et al., 2017)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT], e trans-cinamaldeído restaura a função astrocitária no mesmo modelo (Zhou et al., 2025)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]. A revisão clínica da depressão induzida por interferon reconta mecanismos e manejo (Hafizi et al., 2005)[OB; revisão, SEM abstract no corpus — PENDENTE DE FULL-TEXT, não serve de lastro próprio]. Somado a Bull 2009 (genótipo modera o risco), este é o eixo de prova-de-conceito: uma citocina exógena causa comportamento depressivo em humano.

---

*IFN_NSC_2014[ML] | IFN_dep_review_2007[EC] | Paeoniflorin_2017[ML] | Cinnam_2025[ML]*

### 2.17 — Ácido araquidônico → COX-2 → PGE2 → EP e CRH (BLOCO02.017)

A inflamação induz COX-2 (PTGS2, transcrito de NF-κB), que gera PGE2 do araquidônico. PGE2 sinaliza pelos receptores EP1–EP4 e é o mediador central da **febre** e de parte do sickness: os mecanismos neurais da febre induzida por inflamação, com PGE2 hipotalâmico à frente, estão detalhados (Blomqvist et al., 2018)[OB; revisão, humano+animal] [VERIFICADO]. COX-2 também tem papel em sinalização sináptica (Yang et al., 2008)[OB; revisão, humano+animal] [VERIFICADO]. O elo com o HPA: PGE2 estimula CRH hipotalâmico, conectando inflamação aguda ao eixo do estresse (cross-ref B2). Bem_suportado; a participação na depressão crônica é [EXT].

---

*Fever_2018[ML] | COX2_synap_2008[ML]*

### 2.18 — Via cGAS-STING (sensor de DNA citosólico) (BLOCO02.018)

DNA ectópico no citosol (mtDNA vazando, DNA nuclear dano) é detectado por **cGAS**, que produz cGAMP; cGAMP ativa **STING** → TBK1 → IRF3 → IFN tipo I, além de NF-κB. A via está consolidada como mecanismo de neuroinflamação em doenças neurológicas (Huang et al., 2023)[OB; revisão, humano]; o cruzamento mitofagia–cGAS-STING é revisado na neuroinflamação (Zhou et al., 2024)[OB; revisão] [EXTRAPOLADO: animal/célula→humano][EXT]. Há prova manipulável no SNC: na disfunção cognitiva pós-operatória por sevoflurano, a ativação do **NLRP3 dependente do eixo mtDNA–cGAS-STING** em microglia conduz a neuroinflamação (Yang et al., 2024)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]. Vazamento de mtDNA e cGAS-STING no envelhecimento cerebral são alvo terapêutico emergente (Li et al., 2025)[OB; revisão] [EXTRAPOLADO: animal/célula→humano][EXT]. Majoritariamente animal/in vitro; [EXT] para TDM.

---

*cGAS_neuro_2023[ML] | cGAS_POCD_2024[ML] | Mitophagy_cGAS_2024[OB] | cGAS_aging_2025[OB]*

### 2.19 — Freios anti-inflamatórios: IL-10/JAK1/STAT3 e TGF-β/SMAD (BLOCO02.019)

A resposta é contida por freios compensatórios. IL-10 liga IL-10Rα + IL-10Rβ (receptor compartilhado) e sinaliza por JAK1/TYK2 → **STAT3**, suprimindo transcrição pró-inflamatória. A biologia estrutural recente desacoplou as funções pró e anti-inflamatórias da IL-10 e mostrou limiares distintos entre populações imunes (Saxton et al., 2021)[EC; humano+camundongo] [VERIFICADO]. O eixo IL-10–STAT3–galectina-3 é essencial para macrófagos reparativos (Shirakawa et al., 2018)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]; a entrega direcionada de IL-10 a microglia/macrófago melhora desfecho em hemorragia intracerebral (Han et al., 2023)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]. A insuficiência relativa deste freio (ex.: IL-10 baixa sob estresse crônico — Voorhees 2013 no BLOCO01) contribui à cronificação. TGF-β→TGFBR→SMAD2/3 é o segundo freio (imunorregulação/fibrose), reportado em revisões [OB]. Contributivo; bem_suportado.

---

*IL10_struct_2021[ML] | IL10_Gal3_2018[ML] | IL10_ICH_2023[ML]*

### 2.20 — Epigenética do estresse precoce: NR3C1 e FKBP5 (BLOCO02.020)

Adversidade precoce grava marcações epigenéticas que desregulam o eixo do cortisol. O achado humano seminal: um polimorfismo funcional em **FKBP5** (regulador do receptor de glicocorticoide) altera a interação da cromatina entre o sítio de início de transcrição e enhancers de longo alcance, e produz **desmetilação alelo-específica dependente de trauma de infância** em elementos de resposta a glicocorticoide, aumentando o risco de transtorno psiquiátrico relacionado ao estresse no adulto (Klengel et al., 2013)[EC; humano] [VERIFICADO]. A revisão sistemática do estresse/epigenética/depressão consolida NR3C1 (metilação do promotor do GR), FKBP5, BDNF e outros genes correlacionados com depressão (Park et al., 2019)[OB; revisão sistemática, humano] [VERIFICADO]. A consequência funcional é a **resistência a glicocorticoides** — o GR deixa de reprimir NF-κB — fechando o loop estresse→inflamação (cross-ref B2/BLOCO08). Muito_estabelecido em humano para FKBP5/NR3C1.

---

*Klengel_2013[EC] | Stress_Epi_2019[EC]*

### 2.21 — Metilação de IL6/TNF e direção de expressão (BLOCO02.021)

Em cérebro humano pós-morte, a regulação da expressão de TNF-α envolve chaveamento epigenético complexo: no córtex pré-frontal de indivíduos que morreram por suicídio, a superexpressão de TNF-α é explicada por mecanismos de microRNA e proteína de ligação a RNA que destravam o gene (Wang et al., 2018)[EC; post-mortem humano] [VERIFICADO]. Fatores psicológicos associam-se a metilação de DNA de genes do sistema imune/inflamatório (Mehta et al., 2020)[OB; revisão sistemática, humano] [VERIFICADO]. A direção funcional (hipometilação de promotor → maior expressão pró-inflamatória) é o princípio; a evidência direta para o promotor de IL6 em depressão é mais esparsa e fica como emergente [humano].

---

*TNF_suicide_2018[EC] | MetilPTSD_2020[OB]*

### 2.22 — Reguladores pós-transcricionais: miR-155 e miR-146a (BLOCO02.022)

Dois microRNAs formam um par de retroalimentação sobre NF-κB/JAK-STAT. **miR-146a** é o freio: tem como alvos IRAK1/TRAF6, e sua superexpressão em microglia hipocampal melhora função cognitiva reduzindo a via IRAK1/TRAF6/NF-κB (Zhang et al., 2025)[ML; camundongo]; vesículas extracelulares enriquecidas em miR-146a têm efeito imunomodulador/neuroprotetor (Zhang et al., 2025)[EC; célula/camundongo/humano] [EXTRAPOLADO: animal/célula→humano], e miR-146a-5p reduz neuroinflamação em outros modelos [ML]. **miR-155** é o acelerador (alvo SOCS1, desinibindo JAK-STAT); a busca dedicada não retornou artigo SNC-comportamental forte para miR-155 na literatura, ficando como mecanismo proposto, a confirmar (`nao_estabelecido` no SNC comportamental). Em microglia, o balanço miR-155↑/miR-146a↓ mantém o priming; a restauração de miR-146a é candidata terapêutica [EXT; gap_pesquisa].

---

A superexpressão de miR-146a em microglia hipocampal modula a resposta inflamatória (miR146a_2025[ML]; pré-clínico).

### 2.23 — Modificações de histona como memória celular inata (BLOCO02.023)

O priming microglial tem base em marcas de cromatina. Em microglia senescente, a **lactilação de H3K18** mantém o programa transcricional pró-inflamatório no envelhecimento/Alzheimer (Wei et al., 2023)[ML; camundongo+humano][EXT]. A inflamação neonatal induz priming microglial no hipocampo ventral via **regulação epigenética (metilação de DNA)** que persiste até a vida adulta e sensibiliza a um segundo estresse — "two-hit" (Yang et al., 2026)[ML; camundongo]. Marcas de histona (acetilação/metilação) reconfiguram a acessibilidade de genes inflamatórios, baixando o limiar de resposta. Demonstrado em animal; a tradução para memória traumática humana é [EXT], emergente.

---

*H3K18_2023[ML] | Yang_2026_neonatal[ML]*

### 2.24 — Proteínas S100 como DAMPs: efeito dual dose-dependente via RAGE (BLOCO02.024)

S100B e S100A8/A9 (calprotectina) são DAMPs distintos de HMGB1. Têm efeito **dual por concentração e afinidade de receptor**: em níveis fisiológicos (nanomolar), S100B é trófico para neurônios; em níveis altos (micromolar), liberados por astrócitos lesados, S100B age via RAGE e é pró-inflamatório/tóxico (Bianchi et al., 2011)[ML; camundongo/rato]; a ligação S100B–RAGE em microglia estimula expressão de COX-2 e, em alta concentração, iNOS/NO em sinergia com LPS/IFN-γ (Bianchi et al., 2007)[ML; camundongo/humano] [EXTRAPOLADO: animal/célula→humano]. A revisão de 2025 consolida S100B e S100A8/A9 como DAMPs que interagem com RAGE/TLRs disparando cascatas pró-inflamatórias e ativação glial, com nota explícita de que concentrações baixas podem ser neuroprotetoras (García-Domínguez et al., 2025)[OB; revisão, humano+animal] [EXTRAPOLADO: animal/célula→humano]. Mecanística em animal; marcador S100B em depressão é [EXT]/emergente.

---
*S100B_2011[ML] | S100_review_2025[ML] | S100B_COX2_2007[ML]*

---

### 2.25 — Imunometabolismo da micróglia: succinato/HIF-1α, glicólise e itaconato (BLOCO02.025)

A resposta inflamatória é também uma **reprogramação bioenergética**. Ao ser ativada por LPS/estresse, a micróglia troca a fosforilação oxidativa e a β-oxidação por **glicólise aeróbica** (chaveamento tipo-Warburg), necessária à produção de citocinas (Cheng et al., 2021)[ML; camundongo/célula] [PRÉ-CLÍNICO]; o perfil glicolítico no hipocampo por neuroinflamação aguda é reproduzido em rato (Vizuete et al., 2022)[ML; rato] [PRÉ-CLÍNICO]. Na quebra do ciclo de Krebs, o acúmulo de **succinato** funciona como sinal inflamatório: estabiliza **HIF-1α** (ao inibir a prolil-hidroxilase), que induz IL-1β e sustenta o fenótipo pró-inflamatório (Tannahill et al., 2013)[ML; macrófago] [EXTRAPOLADO: animal/célula→humano][EXT]. Em contraponto, a ativação inflamatória induz a enzima mitocondrial **IRG1/ACOD1**, que produz **itaconato** — freio endógeno que inibe o NLRP3 e ativa o eixo Nrf2/antioxidante (Liu et al., 2023)[OB; revisão, célula/animal] [EXTRAPOLADO: animal/célula→humano]; o eixo glicolítico/IRG1-itaconato/Nrf2 é ativamente regulado em células expostas a LPS (Engskog-Vlachos et al., 2025)[ML; célula] [PRÉ-CLÍNICO]. Natureza: causal em animal/célula; a hipótese de que insuficiência de itaconato croniciza a depressão humana é **emergente** [humano por marcador].

---

*Glicolise_microglia_2021[ML] | Glicolise_hipocampo_2022[ML] | Succinato_HIF_2013[ML] | Itaconato_Nrf2_2023[OB] | IRG1_itaconato_2025[ML]*

### 2.26 — Necroptose: morte lítica por RIPK1–RIPK3–MLKL paralela à piroptose (BLOCO02.026)

Além da piroptose (inflamassoma/gasdermina), o SNC tem uma via de morte programada **lítica e independente de caspase**: via TNFR1 (ou outros receptores de morte), quando as caspases estão inibidas, **RIPK1–RIPK3** fosforilam **MLKL**, que transloca à membrana, forma poros e rompe a célula, liberando DAMPs. Na depressão experimental, as quinases da necroptose estão envolvidas na redução de astrócitos e nas alterações gliais induzidas por estresse crônico (Zeb et al., 2022)[ML; camundongo] [PRÉ-CLÍNICO]. Natureza: mecanística em animal; a participação direta em TDM/ansiedade humana é emergente [EXT]. Diferencia-se da piroptose pelo gatilho (TNF/RIPK vs. inflamassoma/caspase), mas ambas amplificam a liberação de DAMPs.

---

*Necroptose_dep_2022[ML]*

### 2.27 — Hemicanais astrocitários (conexina-43/panexina) e aquaporina-4 no sistema glinfático (BLOCO02.027)

A neuroinflamação também corrompe a fisiologia astrocitária de suporte. Citocinas como IL-6/IFN induzem fosforilação aberrante da **conexina-43 (Cx43)**: fecham-se as *gap junctions* que distribuem energia/glicose pela rede astrocitária e abrem-se **hemicanais**, com vazamento de ATP e glutamato para o espaço extracelular — excitotoxicidade e amplificação do sinal purinérgico. A abertura de hemicanais Cx43 em hipocampo por micróglia ativada prejudica a interação neuro-glial (Abudara et al., 2015)[ML; camundongo/célula] [PRÉ-CLÍNICO]; neuroinflamação altera as junções comunicantes de forma região-dependente (Karpuk et al., 2011)[ML; camundongo] [PRÉ-CLÍNICO]; o Cx43 astrocitário é proposto como alvo antidepressivo (Lei et al., 2023)[OB; revisão, célula/animal] [EXTRAPOLADO: animal/célula→humano]. Paralelamente, a despolarização da **aquaporina-4 (AQP4)** nos pés astrocitários desorganiza o fluxo glinfático, com acúmulo de citocinas e detritos; a disfunção glinfática no comportamento tipo-depressivo é documentada por imagem dinâmica e revertida por cetamina (Wen et al., 2024)[ML; camundongo] [PRÉ-CLÍNICO], (Lyu et al., 2025)[ML; camundongo] [PRÉ-CLÍNICO]. Natureza: mecanística em animal; humano por marcador [EXT].

---

*Cx43_hemicanal_2015[ML] | Cx43_GJ_2011[ML] | Cx43_antidep_2023[OB] | AQP4_glinfatica_2024[ML] | Glinfatica_RM_2025[ML]*

## BLOCO_03 — MEDIADORES ESPECÍFICOS (CITOCINAS, QUIMIOCINAS)

### 3.1 — IL-1β: fonte, receptor e impacto sobre BDNF/CREB (BLOCO03.001)

IL-1β, maturada pelo inflamassoma (BLOCO02), é a citocina que mais diretamente deprime a plasticidade neuronal. O achado clássico: IL-1β sistêmica reduz a expressão de mRNA de BDNF no hipocampo de rato — ligação direta entre sinal imune periférico e o fator trófico central (Lapchak et al., 1993)[ML; rato] [PRÉ-CLÍNICO]. Em cultura, IL-1β suprime a sobrevivência neuronal mediada por neurotrofinas e interage com crescimento neurítico de forma contexto-dependente (Boato et al., 2011)[ML; célula/camundongo]. Mecanisticamente, IL-1β/IL-1R1 suprime a sinalização BDNF/TrkB/CREB que sustenta LTP e neurogênese (cross-ref B3). Em condições fisiológicas, citocinas residentes mantêm plasticidade; quando elevadas na neuroinflamação, IL-1β e TNF interferem com circuitos de aprendizado/cognição e promovem excitotoxicidade (Rizzo et al., 2018)[OB; revisão, humano+animal] [VERIFICADO]. Natureza: causal em animal/célula; o elo com BDNF em depressão humana é [EXT].

---

*IL1b_BDNF_1993[ML] | Plasticity_2018[ML] | IL1b_NT3_2011[ML]*

### 3.2 — TNF-α e plasticidade sináptica (BLOCO03.002)

O TNF tem papel fisiológico na plasticidade hebbiana e homeostática (escala de força sináptica) e patológico quando elevado: em neuroinflamação, TNF e IL-1β modulam plasticidade sináptica e contribuem para excitotoxicidade e neurodegeneração (Rizzo et al., 2018)[OB; revisão, humano+animal] [VERIFICADO]. O bloqueio periférico de TNF com etanercepte por via perispinhal é explorado em distúrbios neuroinflamatórios, sugerindo efeito central mesmo sem cruzar a BHE (Tobinick et al., 2009)[OB; revisão, humano] [EXTRAPOLADO: animal/célula→humano]. Em modelos, intervenções anti-inflamatórias restauram sinalização CREB e memória/sono [ML; EXT]. Natureza: bem_suportado o efeito sobre plasticidade em animal; tradução humana emergente.

---

*Plasticity_2018[ML] | Etanercept_2009[EC]*

### 3.3 — IL-6: trans-sinalização e o duplo papel reparativo (BLOCO03.003)

O IL-6 não é unicamente danoso. Demonstração elegante: após lesão cerebral traumática, a simples remoção da micróglia pouco altera o desfecho, mas induzir a **renovação** da população gera um fenótipo microglial neuroprotetor que auxilia a recuperação — e esse efeito benéfico depende criticamente da **trans-sinalização de IL-6 via IL-6R solúvel + gp130** (Willis et al., 2020)[ML; camundongo+humano] [PRÉ-CLÍNICO]. Isso separa o ramo clássico (IL-6R de membrana, regenerativo) do trans-sinalizante (sIL-6R, pró-inflamatório) e mostra que o IL-6 tem faces opostas conforme contexto e receptor. Na periferia, a meta-análise de 82 estudos confirma IL-6 elevada na TDM (Köhler et al., 2017)[MA; humano] [VERIFICADO] — ver BLOCO05. Natureza: mecanística dual em animal; marcador humano bem_suportado.

---

*RepopIL6_2020[ML] | Quimio_meta82_2017[EC]*

### 3.4 — TGF-β1 como freio glial (BLOCO03.004)

TGF-β1 é citocina imunorreguladora; níveis reduzidos são relatados tanto em Alzheimer quanto em depressão, e a via é proposta como elo restaurativo compartilhado (Eleni et al., 2025)[OB; revisão, humano+animal] [EXTRAPOLADO: animal/célula→humano]. A meta-análise do efeito de antidepressivos sobre marcadores periféricos mostra deslocamento do balanço pró/anti-inflamatório (Więdłocha et al., 2018)[MA; humano] [VERIFICADO]. Natureza: associativo em humano; mecanístico de reparo [EXT].

---

*TGFb_2025[ML] | Antidep_meta_2018[EC]*

### 3.5 — Priming microglial por IFN-γ via STAT1/NLRP3 (BLOCO03.005)

O priming microglial tem gatilhos imunes específicos. IFN-γ induz priming em micróglia por ativação **STAT1-mediada do inflamassoma NLRP3**: em cultura primária e em cérebro de camundongo, IFN-γ produz morfologia ativada ("hedgehog"), sobe marcadores CD86/CD11b e sensibiliza o NLRP3 (He et al., 2024)[ML; célula/camundongo] [PRÉ-CLÍNICO]. Os princípios de priming e inibição do inflamassoma são revisados com implicações psiquiátricas (Herman et al., 2018)[OB; revisão, humano+animal] [EXTRAPOLADO: animal/célula→humano]. Em modelo de depressão, o alvo NEK7 (regulador a montante do NLRP3) modula piroptose e microbiota e alivia comportamento tipo-depressivo (Lang et al., 2025)[ML; rato/camundongo] [PRÉ-CLÍNICO][EXT]. Natureza: causal em animal; humano [EXT].

---

*IFNg_PRIMING_2024[ML] | PrimingPrinc_2018[ML] | NEK7_2025[ML]*

### 3.6 — Subpopulações microgliais: homeostática, priming, DAM (BLOCO03.006)

A micróglia não é uma entidade única. Coexistem estados: **homeostática/ramificada** (vigilância, P2Y12, TMEM119), **priming/reativa** (limalar rebaixado) e **DAM — microglia associada a doença** (assinatura transcricional de fagocitose/ativação, originalmente em neurodegeneração). Antidepressivos modulam a ativação microglial, deslocando o fenótipo para menos pró-inflamatório (Mariani et al., 2022)[OB; revisão, humano+animal] [EXTRAPOLADO: animal/célula→humano]. Citocinas pró-inflamatórias e neuropeptídeos conectam inflamação sistêmica, estresse e pele (psoríase) a depressão/ansiedade (Keenan et al., 2025)[OB; revisão, humano+animal] [VERIFICADO]. A identidade DAM em depressão é majoritariamente extrapolada de Alzheimer/doenças [EXT] — não há ainda perfil DAM específico de TDM consolidado.

---

*Antidep_microglia_2022[ML] | Psoriase_2025[EC]*

### 3.7 — Astrócitos reativos A1 vs. A2 (BLOCO03.007)

Astócitos reativos se polarizam em **A1 (neurotóxico, induzido por citocinas microgliais)** e **A2 (neuroprotetor)**. Em camundongo, IFN-γ também priming astrocitário e a modulação por antidepressivos/anti-inflamatórios desloca o balanço (He et al., 2024)[ML]; revisões farmacológicas registram a modulação astrocitária por antidepressivos (Mariani et al., 2022)[OB] [EXTRAPOLADO: animal/célula→humano]. A validação direta de A1/A2 em ansiedade/depressão humana é fraca — o binário A1/A2 é mais robusto em AVC/neurodegeneração; para TDM permanece [EXT], e o campo ressalta que a polarização é um continuum, não dois estados estanques.

---

*Antidep_microglia_2022[ML] | IFNg_PRIMING_2024[ML]*

### 3.8 — Sinalização purinérgica P2X7/P2Y12 (BLOCO03.008)

A comunicação micróglia–neurônio usa ATP/adenosina. **P2Y12** é receptor homeostático microglial que guia processos ao dano e mantém vigilância (marcador do estado ramificado); **P2X7** é receptor de ATP extracelular em alta concentração que funciona como "sinal 2" do NLRP3 (e fluxo de K+), disparando IL-1β. A ativação de P2X7 está implicada na despolarização e saída do estado homeostático; a perda de P2Y12 marca a transição para reatividade. Estes alvos são centrais nos princípios de priming/inibição do inflamassoma (Herman et al., 2018)[OB; revisão, humano+animal]. A literatura disponível retorna material esparso para ensaios P2X7 específicos em comportamento; o mecanismo é bem_suportado em célula/animal, o vínculo comportamental humano é [EXT]/gap_pesquisa.

---

*PrimingPrinc_2018[ML]*

### 3.9 — Barreira hematoencefálica: CCL2/CCR2 e transmigração de monócitos (BLOCO03.009, 012)

A BHE controla o tráfego de leucócitos. A quimiocina **CCL2 (MCP-1)** produzida no parênquima atravessa o endotélio microvascular cerebral por transporte transcelular, formando um gradiente que recruta monócitos por trás da barreira (Ge et al., 2008)[ML; célula] [PRÉ-CLÍNICO]. O receptor **CCR2** é o receptor dominante de quimiotaxia de monócitos Ly6C^high; inibição de HMG-CoA redutase reduz expressão de CCR2 e recrutamento (Han et al., 2005)[ML; célula/humano/animal] [PRÉ-CLÍNICO]. A adesão depende de **ICAM-1** no endotélio/astrócito ativado: telmisartana inibe adesão leucocitária induzida por TNF bloqueando ICAM-1 em astrócitos, com melhora de depressão/memória e redução de inflamação cerebral (Jang et al., 2020)[ML] [EXTRAPOLADO: animal/célula→humano]. Estresse crônico de restrição induz marcadores inflamatórios e oxidativos na microvasculatura cerebral (Zhu et al., 2023)[ML; camundongo] [PRÉ-CLÍNICO]. Natureza: passos celulares causais em animal/célula; transmigração na depressão humana [EXT].

---

*CCL2_2008[ML] | CCR2_2005[ML] | ICAM_2020[ML] | Microvasc_2023[ML]*

### 3.10 — CX3CL1/CX3CR1: o freio neurônio→micróglia (BLOCO03.010)

A fractalcina **CX3CL1** é expressa por neurônios; seu único receptor **CX3CR1** é microglial — um eixo de comunicação direta que mantém a micróglia em estado homeostático. A perda de sinalização CX3CL1 desinibe a micróglia (reatividade). Em lesão cerebral, CX3CL1 atenua déficit neurológico e neuroinflamação via CX3CR1/p38 MAPK/ERK1/2 (Zhu et al., 2026)[ML; camundongo+humano/célula] [EXTRAPOLADO: animal/célula→humano]. Durante o desenvolvimento, a poda sináptica pela micróglia é necessária para a maturação normal do cérebro (Paolicelli et al., 2011)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano] — a fagocitose sináptica, regulada por CX3CR1 e complemento (BLOCO10), quando excessiva no adulto é candidata a mecanismo de perda sináptica na depressão [EXT]. Natureza: freio homeostático bem_suportado; exagero de poda na TDM emergente.

---

*CX3CL1_2026[ML] | Poda_2011[ML]*

### 3.11 — CXCL8/IL-8 e sintomas somáticos (BLOCO03.011)

CXCL8 (IL-8) é quimiocina neutrofílica. A meta-análise de 82 estudos confirma alterações periféricas de quimiocinas na TDM, incluindo CCL2 e quimiocinas correlacionadas a sintomas somáticos/fadiga (Köhler et al., 2017)[MA; humano]. A busca dedicada para IL-8 específica retornou material limitado na literatura; o vínculo direto IL-8↔sintomas somáticos fica como associativo [humano], menos específico que citocinas maiores — registrado como emergente, sem forçar mecanismo.

---

*Quimio_meta82_2017[EC]*

### 3.12 — Populações imunes perivasculares e portas de entrada (BLOCO03.006–009, 012; vagal/OVLT)

Além da micróglia parenquimal, o SNC conta com populações distintas: macrófagos perivasculares/meníngeos, monócitos infiltrantes Ly6C^high (via CCL2/CCR2), e linfócitos meníngeos. O recrutamento e adesão seguem os passos de CCL2/CCR2 e ICAM-1 descritos em 3.9. A sinalização imune→cérebro também usa **vias independentes de BHE**: nervo vago aferente (sinal neural rápido, ver Dantzer/Banks no BLOCO01) e órgãos circunventriculares/barreira porosa (área postrema), onde o endotélio é permeável. A disbiose intestinal agrava depressão pós-AVE via inflamassoma NLRP3 microglial (Chen et al., 2025)[ML; rato][EXT], e probióticos melhoram déficit de memória modulando glia/eixo intestino-cérebro (Yang et al., 2020)[ML; camundongo] [PRÉ-CLÍNICO][EXT] — cross-ref mecanismo_B7_eixo_intestino_cerebro. A revisão de eixo intestino-cérebro e inflamassoma consolida como microbiota hospedeira influencia fisiologia cerebral (Rutsch et al., 2020)[OB; revisão, humano+animal] [EXTRAPOLADO: animal/célula→humano].

---

*PSD_gut_2025[ML] | Prob_2020[ML] | GutInfl_2020[ML]*

### 3.13 — IL-18: clivagem pelo inflamassoma e papel dual (BLOCO03.005)

IL-18 é, como IL-1β, maturada por caspase-1 no inflamassoma (compartilha o eixo NLRP3→ASC→caspase-1). Diferentemente de IL-1β, tem papel dual surpreendente no SNC: além das funções imunes, IL-18 participa de homeostase energética e estabilidade neural; a **deficiência de IL-18 em camundongos causa disfunção mitocondrial em células hipocampais e síndrome tipo-depressiva** — sugerindo que nem todo produto do inflamassoma é unicamente deletério e que a direção da alteração em depressão não é simplesmente "IL-18 alta" (Yamanishi et al., 2023)[ML; camundongo+humano] [EXTRAPOLADO: animal/célula→humano][EXT]. É elevada em alguns contextos inflamatórios (Köhler et al., 2017)[MA; humano] [VERIFICADO], mas sua função neural protetora merece qualificador distinto de IL-1β. Natureza: emergente; direção em TDM humana não consolidada — registrado como mediador com associação não simples.

---

*IL18_2023[ML] | Quimio_meta82_2017[MA]*

### 3.14 — IL-17A e Th17 (BLOCO03.006)

IL-17A é produzida por linfócitos Th17 (diferenciados sob IL-6 + TGF-β) e age via IL-17RA. Em modelo camundongo de comportamento tipo-depressivo induzido por metanfetamina, metabolismo de betaína desregulado direciona diferenciação Th17 periférica, e essa via imune periférica media dano ao SNC (Hui et al., 2025)[ML; camundongo] [PRÉ-CLÍNICO][EXT]. A revisão de citocinas/neuropeptídeos em psoríase/depressão/ansiedade inclui IL-17 entre os mediadores que conectam inflamação sistêmica e estresse (Keenan et al., 2025)[OB; revisão]. Natureza: mecanística emergente em animal; humano associativo [EXT], menos robusto que IL-6/TNF.

---

*Th17_2025[ML] | Psoriase_2025[OB]*

### 3.15 — Inventário NEGATIVO de mediadores (BLOCO03.004)

Registro honesto do que foi investigado mas **não mostra associação consistente** com ansiedade/depressão neste corpus, ou cuja direção é ambígua:
- **IL-18** — ver 3.13: função dual; "IL-18 sempre alta" é falso (deficiência também gera fenótipo depressivo em camundongo).
- **Quimiocinas neutrofílicas (CXCL8/IL-8)** — alterações periféricas presentes na meta-análise, mas sem especificidade mecanística para humor; fraco sinal direto (ver 3.11).
- **IFN-γ periférico** — marcador inconsistente nas meta-análises de sangue (o papel robusto é indutor de IDO/priming, não como marcador sérico de TDM).
- **IL-2, IL-12, IL-13** — aparecem em meta-análises com tamanhos de efeito pequenos e heterogêneos; sem via molecular dedicada ao humor.
Estes não são "inexistentes" — são marcadores sem associação robusta/consistente, e por isso não recebem nó próprio nem vínculo causal forte; ficam como ruído de fundo na citoquina-ampla, distinguindo o sinal replicado (IL-6, TNF, IL-1β, PCR, KYN/TRP) do não-replicado.

---

### 3.16 — Neuroimunologia da ansiedade: amígdala, IL-18 local, P2X7/Na⁺-K⁺-ATPase e NLRP3 (BLOCO03.016)

A ansiedade tem nós moleculares próprios, centrados na **amígdala basolateral (BLA)** e na extinção do medo. Em camundongo, **IL-17A/IL-17C** na amígdala basolateral aumentam a excitabilidade neuronal e induzem comportamento ansiogênico, ao passo que a citocina anti-inflamatória **IL-10**, sobre a mesma população neuronal, tem efeito oposto — modulação bidirecional do circuito do medo/ansiedade por citocinas (Lee et al., 2025)[ML; camundongo] [PRÉ-CLÍNICO]. Um sistema local de **IL-18 na BLA** regula a suscetibilidade ao estresse crônico (Kim TK et al., 2017)[ML; camundongo] [PRÉ-CLÍNICO]. Na micróglia, a ruptura do complexo **Na⁺/K⁺-ATPase–P2X7** promove o comportamento tipo-ansiedade (Huang S et al., 2024)[ML; camundongo] [PRÉ-CLÍNICO]. O inflamassoma na ansiedade tem direção **não monotônica**: a deficiência de **TET2** (que desreprime metilação) ativa NLRP3/IL-1β e induz ansiedade/depressão (Gao et al., 2023)[ML; camundongo] [PRÉ-CLÍNICO], mas a própria **deficiência de NLRP3** também provoca disfunção hipocampal e comportamento tipo-ansiedade (Komleva et al., 2021)[ML; camundongo] [PRÉ-CLÍNICO] — aviso contra leituras unidirecionais do inflamassoma. Natureza: causal em animal; humano por marcador/imagem [EXT].

---

*Amigdala_citocinas_2025[OB] | IL18_amigdala_2017[ML] | P2X7_NaK_ansiedade_2024[ML] | TET2_NLRP3_2023[ML] | NLRP3_def_ansiedade_2021[ML]*

### 3.17 — IL-33: alarmina da família IL-1 com sinal meta-analítico emergente (BLOCO03.017) [AT 2026-09-08]

A **IL-33** (alarmina nuclear da família IL-1, liberada por dano tecidual; receptor ST2/IL1RL1) tem associação com depressão documentada em revisão sistemática com meta-análise de 2023 (Liu et al., 2023b)[MA; humano]. Leitura canônica: **sinal emergente** — a IL-33 entra como **mediador candidato**, no mesmo registro epistêmico cauteloso do inventário (ver 3.15), e **não** como nó causal dedicado ao humor; neste corpus não há via molecular mapeada da IL-33 ao sintoma com lastro equivalente ao de IL-1β/IL-6/TNF. Natureza: associativo humano, ainda sem cadeia mecanística dedicada. [AT]

---

*Liu_2023b[MA]*

## BLOCO_04 — CÉLULAS E ESTRUTURAS: MICRÓGLIA, ASTRÓCITOS, BHE, VAGO E FRONTEIRAS IMUNES

### 4.1 — Subpopulações microgliais: homeostática, priming e DAM (BLOCO04.001)

A micróglia compreende estados funcionais distintos com identidade molecular. O estado **DAM (microglia associada a doença)** depende do eixo **TREM2–APOE**: uma assinatura transcricional APOE-dependente identifica micróglia disfuncional em modelos de ALS, esclerose múltipla e Alzheimer e ao redor de placas Aβ em cérebro humano (Krasemann et al., 2017)[ML; camundongo+humano] [EXTRAPOLADO: animal/célula→humano]. O sequenciamento mononuclear em camundongo e humano confirma populações DAM dependentes e independentes de TREM2 associadas à patologia (Zhou et al., 2020)[EC; humano+camundongo] [EXTRAPOLADO: animal/célula→humano]. TREM2 é também receptor de fagocitose que limita o NLRP3 (Huang et al., 2024)[ML; camundongo, ver BLOCO02.003] [PRÉ-CLÍNICO]. Em depressão, o perfil DAM específico não está consolidado — a identidade molecular é transplantada da neurodegeneração [EXT], mas a existência de micróglia funcionalmente heterogênea é muito_estabelecido.

---

*TREM2_APOE_2017[ML] | snRNA_TREM2_2020[ML] | TREM2_Park_2024[ML]*

### 4.2 — Astrócitos reativos: chave molecular A1/A2 (BLOCO04.002)

Astrócitos reativos não são um estado único. Um trabalho de 2024 identificou uma **chave molecular** que separa reatividade neuroprotetora de neurotóxica: astrócitos de substância branca lesada diferenciam-se em populações C3+ e C3− (a simplificação anterior "A1/A2"), subdivisíveis por trajetórias de reparo (Cameron et al., 2024)[ML; camundongo] [PRÉ-CLÍNICO]. O bloqueio da conversão ao fenótipo A1 neurotóxico (induzido por mediadores microgliais) é neuroprotetor em modelos de Parkinson, e agonistas GLP1R inibem essa conversão (Yun et al., 2018)[ML; camundongo+humano] [EXTRAPOLADO: animal/célula→humano][EXT]. Em depressão, IL-6 derivada de micróglia pode induzir apoptose de astrócitos hipocampais (Shen et al., 2025)[ML; camundongo] [PRÉ-CLÍNICO]. A validação direta A1/A2 em TDM humana é fraca; o binário é [EXT] e hoje visto como continuum.

---

*AstroSwitch_2024[ML] | A1block_2018[ML] | IL6astro_2025[ML]*

### 4.3 — Sinalização purinérgica P2X7/P2Y12 e estresse microglial (BLOCO04.003)

A comunicação micróglia–neurônio por ATP tem mecanismo direto ligado a depressão: a crença padrão era que ATP extracelular → P2X7 → montagem do NLRP3; um achado mais fino mostra que o ATP e o estresse aumentam **contatos retículo-mitocôndria (MAMs)** na micróglia, e essa plataforma media o comportamento tipo-depressivo (Zhang et al., 2024)[ML; camundongo] [PRÉ-CLÍNICO]. P2X7 funciona como "sinal 2" do inflamassoma (Herman et al., 2018)[OB; revisão], enquanto P2Y12 marca o estado homeostático/ramificado e guia processos ao dano. Natureza: causal em camundongo para o eixo ATP/MAMs/NLRP3-comportamento; humano [EXT].

---

*MAMs_P2X7_2024[ML] | PrimingPrinc_2018[OB]*

### 4.4 — Barreira hematoencefálica: componentes e disfunção por estresse (BLOCO04.004, 008)

A BHE é formada por endotélio com tight junctions (claudina-5, ocludina), pericitos e pés astrocitários. Os **pericitos regulam a BHE**: sua integridade é necessária para manter as junções e a baixa vesiculação endotelial (Armulik et al., 2010)[ML; camundongo] [PRÉ-CLÍNICO]. O achado mais relevante para depressão: estresse social crônico (derrota social em camundongo) induz **patologia neurovascular promotora de depressão** — reduz a tight junction claudina-5 (Cldn5), altera morfologia vascular e aumenta permeabilidade/passagem de sinais imunes periféricos (Menard et al., 2017)[ML; camundongo] [PRÉ-CLÍNICO]. A BHE na neurodegeneração é revista com componentes celulares separados (Zenaro et al., 2017)[OB; revisão] [EXTRAPOLADO: animal/célula→humano][EXT]. O pé astrocitário (unidade neurovascular) propaga o sinal endotélio→parênquima. Natureza: claudina-5/pericitos causal em animal; BHE na TDM humana [EXT]/emergente (ver marcadores sérios de BHE no BLOCO05).

---

*Pericitos_2010[ML] | SocialStress_BBB_2017[ML] | BBB_AD_2017[OB]*

### 4.5 — Nervo vago como via periferia→SNC (BLOCO04.005)

O nervo vago (80% fibras aferentes) detecta metabólitos da microbiota e sinais inflamatórios periféricos e os conduz ao SNC independentemente da BHE, na interface do eixo intestino-cérebro (Bonaz et al., 2018)[OB; revisão] [VERIFICADO]. Em humanos, a **estimulação vagal auricular transcutânea (taVNS)** aumenta conectividade amígdala–córtex pré-frontal dorsolateral e tem efeito anti-inflamatório na TDM (Liu et al., 2020)[EC; humano] [VERIFICADO]. É a tradução clínica da via neural aferente (colinérgica anti-inflamatória). Natureza: via neural bem_suportado; taVNS como intervenção em depressão é moderadamente_suportado/emergente em humano.

---

*Vago_2018[ML] | taVNS_2020[EC]*

### 4.6 — Populações imunes de fronteira: perivasculares, Treg, meníngeas (BLOCO04.006)

Além da micróglia parenquimal, macrófagos de borda (perivasculares/meníngeos) ocupam a interface SNC-periferia. Macrófagos perivasculares promovem clearance glinfático de Aβ pós-AVE por mecanismo próprio (Li et al., 2025)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano]. Tregs periféricas têm fenótipos modificados em sofrimento psicológico pré-natal (Wiley et al., 2024)[EC; humano] [VERIFICADO]. Estas populações são distintas da micróglia e acessíveis sem transposição completa da BHE. Natureza: mecanística em animal/humano; papel específico em depressão emergente. Oligodendrócitos/NG2-glia sob TNF/IFN-γ (claim 4.007) não recebido vínculo dedicado na literatura (redução de densidade em CPF é dado pós-morte reportado na literatura) — fica para lote de célula glial.

---

*PVM_2025[ML] | Treg_2024[EC]*

### 4.7 — Estruturas cerebrais-alvo: ínsula, amígdala, accumbens (BLOCO04.009)

O sinal inflamatório atinge circuitos específicos. A taVNS modula conectividade **amígdala–CPFdl** (Liu et al., 2020)[EC; humano] [VERIFICADO]. Probiótico (Bifidobacterium longum NCC3001, RCT) reduz escores de depressão e altera ativação cerebral em áreas límbicas em humanos com SII (Pinto-Sanchez et al., 2017)[EC; humano, RCT] [VERIFICADO]. A ínsula/anterior é modulada por microglia em comportamento tipo-depressivo/ASD em camundongo (Zhang et al., 2026)[ML; camundongo] [PRÉ-CLÍNICO]. Accumbens e ínsula respondem a desafio inflamatório (ver Muscatell/fMRI no BLOCO05). Natureza: conectividade em humano bem_suportado para amígdala/Ínsula; causalidade circuito-específica em animal.

---

*taVNS_2020[EC] | Bifido_2017[EC] | Insula_2026[ML]*

### 4.8 — Portas de entrada sem BHE: linfa meníngea, plexo coroide, glinfática (BLOCO04.010)

O SNC drena pela **glinfática** e por **vasos linfáticos meníngeos**, que afetam a resposta microglial e a imunoterapia (Da et al., 2021)[ML; camundongo+humano]; a revisão de 2025 consolida como o "código imune" do cérebro (Kim et al., 2025)[OB; revisão, humano+animal] [EXTRAPOLADO: animal/célula→humano]. O **plexo coroide** funciona como barreira e fonte de LCR e sinergiza com células imunes durante neuroinflamação (neutrófilos/monócitos acumulam no estroma; ChP regula inflamação meningítica) (Xu et al., 2024)[ML; camundongo] [PRÉ-CLÍNICO]. Essas portas permitem tráfego de sinal imune sem transposição completa da BHE — junto com área postrema/OVLT e vago, completam as rotas periferia→SNC. Natureza: estrutural bem_suportado; relevância psiquiátrica [EXT]/emergente.
---
*MenLinf_2021[ML] | Glinf_2025[ML] | Plexo_2024[ML]*

---

## BLOCO_05 — BIOMARCADORES PERIFÉRICOS E CENTRAIS

> **Referência por ID oficial (IDs oficiais de exame):** os biomarcadores abaixo têm catálogo oficial — PCR ultra-sensível = `exame_pcr_us`, IL-6 = `exame_il6`, IL-1β = `exame_il1beta`, TNF-α = `exame_tnfalpha`, razão quinurenina/triptofano = `exame_razao_kyn_trp`, painel de SNPs inflamatórios = `exame_snps_inflamatorios`. Valores de corte, faixas de referência e protocolos de coleta residem no módulo operacional (C-LAB), NÃO nesta Biblioteca de Mecanismo (aqui fica apenas o papel biológico/direção do efeito). TSPO-PET, S100B sérico, YKL-40/sTREM2 no líquor e resolvina D1 ainda **não têm ID de exame catalogado** — referidos apenas como componente da cascata, sem criar IDs provisórios (padrão de catálogo).

### 5.1 — Marcadores periféricos centrais: hs-CRP, IL-6, TNF-α, sTNFR2 (BLOCO05.004)

O alicerce do subtipo inflamatório é meta-analítico. A meta-análise seminal de citocinas na depressão maior demonstrou concentrações significativamente elevadas de TNF-α e IL-6 em deprimidos versus controles (Dowlati et al., 2010)[MA; humano] [VERIFICADO]. A meta-análise de PCR, IL-1 e IL-6 confirmou associação positiva entre depressão e PCR/IL-6 em amostras comunitárias e clínicas (Howren et al., 2009)[MA; humano] [VERIFICADO]. A meta-análise da rede de citocinas no sangue comparou esquizofrenia, bipolar e TDM e mostrou padrões distintos de alteração conforme estado clínico (Goldsmith et al., 2016)[MA; humano] [VERIFICADO]. A meta-análise mais recente quantificou tanto diferenças de média quanto **variabilidade**, testando se só um subgrupo de pacientes tem elevação — Osimo et al. (2020/2021)[MA; humano] consolidam que as alterações são heterogêneas e concentram-se num subgrupo. A meta-análise de 82 estudos confirmou IL-6, TNF-α, CCL2 e outras citocinas elevadas na TDM (Köhler et al., 2017)[MA; humano] [VERIFICADO]. IL-6 também prediz pior resolução de sintomas em sofrimento psicológico (Virtanen et al., 2015)[EC; humano] [VERIFICADO]. Diferenças sexuais na ligação inflamação-depressão são meta-analisadas, com efeito mais consistente em mulheres em alguns marcadores (Jarkas et al., 2024)[MA; humano] [VERIFICADO].

**Especificidade:** PCR é marcador de fase aguda (fígado, induzido por IL-6) — sensível mas inespecífico (sobe em obesidade, infecção, tabaco); IL-6 é mais próximo da fonte imune mas também pulsátil; TNF-α e **sTNFR2** (receptor solúvel) refletem ativação TNF crônica mais estável. A combinação >1 marcador aumenta especificidade doravante (ver 5.3). Marcadores de revisão recente consolidam mediadores inflamatórios em TDM e bipolar (Poletti et al., 2024)[OB; humano].

**[AT 2026-09-08] Temporalidade, primeiro episódio, sexo e desenvolvimento:** a associação longitudinal inflamação↔depressão é **bidirecional, porém de magnitude modesta**, o que limita leituras causais diretas (Mac Giollabhui et al., 2021)[MA; humano]. O sinal inflamatório **já está presente no primeiro episódio e em pacientes nunca medicados** — afastando a hipótese de artefato de tratamento ou de cronicidade (Gędek et al., 2025)[MA; humano, primeiro episódio] e, para TNF-α especificamente, replicado em caso-controle com meta-análise em TDM **drug-naïve** (Li et al., 2026)[EC; humano]. Em **adolescentes drug-naïve**, citocinas periféricas também diferem de controles (Jadhav et al., 2025)[MA; humano, adolescentes], achado coerente com a meta-análise em crianças e adolescentes (D'Acunto et al., 2019)[MA; humano]. A ligação é **modulada por sexo**: IL-1α, IL-6 e TNF-α apresentam padrões sexo-específicos de associação com o TDM (Elgellaie et al., 2023)[EC; humano]. Por fim, o **valor preditivo individual** de biomarcadores inflamatórios isolados permanece baixo — reforça a regra do painel (5.3), nunca marcador único (Gavril et al., 2024)[OB; revisão]. Natureza: consistência transversal replicada em subgrupos; causalidade temporal ainda moderada.

---

*Dowlati_2010[MA] | Howren_2009[MA] | Goldsmith_2016[MA] | Osimo_2020[MA] | Quimio82_2017[MA] | SexDiff_2024[MA] | IL6resol_2015[EC] | Mediadores_2024[OB] | MacGiollabhui_2021[MA] | Gedek_2025[MA] | Li_2026[EC] | Jadhav_2025[MA] | DAcunto_2019[MA] | Elgellaie_2023[EC] | Gavril_2024[OB]*

### 5.2 — Razão KYN/TRP e marcadores da via da quinurenina (BLOCO05.001)

A **razão quinurenina/triptofano (KYN/TRP)** é o índice plasmático/sérico de atividade de IDO: inflamação desvia triptofano para quinurenina, elevando a razão. Em pacientes bipolares e deprimidos, níveis de citocinas e a razão KYN/TRP associam-se seletivamente a alterações de substância branca (Comai et al., 2022)[EC; humano] [VERIFICADO]. Em tentadores de suicídio com TDM, quinurenina plasmática está elevada (Sublette et al., 2011)[EC; humano] [VERIFICADO]. A ativação cerebral de IDO contribui para comportamento tipo-depressivo em modelo animal (Souza et al., 2017)[ML; camundongo], e o balanço quinurenínico hipocampal é rompido por inflamação periférica (Yehuda et al., 2016)[ML; camundongo] [PRÉ-CLÍNICO]. O KYN/TRP é assim um marcador funcional (reflete atividade enzimática induzida por citocina), mais próximo do mecanismo que PCR, mas ainda periférico/indireto sobre o cérebro.

---

*KYNTRP_WM_2022[EC] | Sublette_2011[EC] | BrainIDO_2017[ML] | Holocausto_2016[EC]*

### 5.3 — Painel combinado e por que múltiplos marcadores (BLOCO05.003)

Nenhum marcador isolado é sensível e específico o bastante para definir o subtipo inflamatório, porque cada um captura um andar diferente: PCR (fase aguda hepática), IL-6 (citocina pivô, pulsátil), sTNFR2 (ativação TNF crônica), KYN/TRP (atividade de IDO/desvio triptofano). A heterogeneidade demonstrada pela meta-análise de variabilidade (Osimo et al., 2020)[MA] é a justificativa biológica para um painel: combinar um marcador upstream (PCR/IL-6) com um downstream (KYN/TRP) e um de estabilidade (sTNFR2) reduz falso-positivo por confundidores (obesidade, infecção — ver BLOCO08). A obesidade é um confundidor/mediador central da relação inflamação-depressão (Monsalve et al., 2025)[OB; revisão, humano] [VERIFICADO].

---

*Obesidade_2025[EC] | Osimo_2020[MA]*

### 5.4 — Marcadores centrais: TSPO-PET (BLOCO05.002)

O **TSPO (proteína translocadora de 18 kDa)** é alvo de PET que marca ativação glial in vivo. Em TDM, a densidade de TSPO está elevada em regiões cortico-límbicas (Setiawan et al., 2015)[EC; humano, PET] [VERIFICADO] — primeira demonstração de neuroinflamação central em pacientes vivos. O TSPO no córtex cingulado anterior está elevado na depressão maior e relacionado a ideação suicida (Holmes et al., 2018)[EC; humano, PET] [VERIFICADO]. Ressalva técnica crítica: TSPO tem polimorfismo rs6971 (ligante de baixa/alta afinidade) que exige genotipagem, e TSPO não é exclusivo de micróglia (astrócitos também expressam) — é marcador de ativação glial, não de "micróglia" pura. Mecanisticamente, o TSPO revela que a ativação é central e não só periférica, mas não separa pró de anti-inflamatório.

**[AT 2026-09-08] Evidência negativa, heterogeneidade e o que o TSPO de fato mede:** o sinal TSPO-PET **não é uniforme**: não se eleva em depressão leve–moderada (Hannestad et al., 2013)[EC; humano, evidência negativa] e, quando elevado, o aumento é **modesto** (~18% na meta-análise de imagem molecular) e **sem especificidade celular** (Eggerstorfer et al., 2022)[MA; humano]; coorte com ligante PK11195 encontrou aumento discreto **sem correlação com o PCR periférico** (Schubert et al., 2021)[EC; humano]. No substrato celular, TSPO é expresso por micróglia, astrócitos, endotélio e outros compartimentos (Nutma et al., 2021; Guilarte et al., 2022)[OB; revisão]; em **roedores** o TSPO marca micróglia ativada, mas essa equivalência **não se sustenta em tecido humano** (Nutma et al., 2023)[OB; revisão] — e a validação pós-morte do PET como biomarcador microglial permanece questão aberta mesmo em condição demonstradora neurodegenerativa (Wijesinghe et al., 2025)[EC; humano, PSP como demonstradora] [EXTRAPOLADO: PSP→TDM]. Correlatos séricos do volume de distribuição do TSPO foram replicados como estratificadores de baixo custo (Attwells et al., 2020)[EC; humano]. Fronteiras 2026: a inflamação periférica pode **reduzir o influxo do radiotraçador ao cérebro** — confundidor farmacocinético do sinal PET (Barzon et al., 2026a)[EC; humano] — e o fingerprinting de rede sobre matrizes TSPO-PET individuais ainda é exploratório (Barzon et al., 2026b)[EC; humano, multicêntrico]. **Regra de leitura [AT]:** TSPO-PET é evidência de **alteração do sinal/distribuição de TSPO**, nunca leitura direta e específica de "ativação microglial"; e um PET negativo em depressão leve **não refuta** a hipótese nos subgrupos graves/inflamados.

---

*Setiawan_2015[EC] | Holmes_2018[EC] | Hannestad_2013[EC] | Eggerstorfer_2022[MA] | Schubert_2021[EC] | Nutma_2021[OB] | Nutma_2023[OB] | Guilarte_2022[OB] | Wijesinghe_2025[EC] | Attwells_2020[EC] | Barzon_2026[EC] | Barzon_2026b[EC]*

### 5.5 — Biomarcadores secundários: S100B, neopterina, LBP, resolvina D1 (BLOCO05.005)

- **S100B sérico:** proteína glial (astrócito) usada como marcador de integridade da BHE/dano glial; níveis séricos elevados são relatados em depressão (Arora et al., 2019)[OB; humano] e propostos como marcador substituto em burnout/depressão (Gulen et al., 2016)[EC; humano] [VERIFICADO]. Após ECT, marcadores inflamatórios e de volume hipocampal mudam (Belge et al., 2020)[EC; humano] [VERIFICADO]. Especificidade baixa (sobe em qualquer dano glial/BHE); papel dual por concentração (BLOCO02.24).
- **Neopterina:** marcador de ativação de macrófago/IFN-γ (co-produto da via BH4); medida com IL-6/KYN em contexto cirúrgico/inflamatório (Noah et al., 2021)[MA; revisão sistemática+meta-análise, humano] [VERIFICADO] — reflecte ativação imune celular, menos validada em TDM.
- **LBP/endotoxina sérica:** marcador indireto de translocação bacteriana/permeabilidade (cross-ref mecanismo_B7_eixo_intestino_cerebro); a literatura não traz validação forte em TDM — fica como candidato [EXT].
- **Resolvina D1 plasmática:** mede o lado da resolução (SPMs); a literatura não reporta ensaio clínico robusto em depressão — hipótese mecanística (BLOCO02.13), gap de pesquisa.

---

*S100B_dep_2019[EC] | S100B_burnout_2016[EC] | HippVol_ECT_2020[EC] | Neopterin_surg_2021[MA]*

### 5.6 — Biomarcadores centrais no líquor e pós-morte (BLOCO05.006)

No SNC, o achado mais forte é o **ácido quinolínico microglial**: depressão grave associa-se a QUIN elevado em subregiões do córtex cingulado anterior (Steiner et al., 2011)[EC; pós-morte/tecidos humanos] [VERIFICADO] — popular de suicídio com alta inflamação, não "TDM geral" (qualificador obrigatório). Marcadores gliais no LCR (sTREM2, YKL-40) têm associação longitudinal com depressão e disponibilidade de transportador de dopamina em Parkinson (Yang et al., 2024)[EC; humano, LCR] [EXTRAPOLADO: animal/célula→humano] — sugerindo que marcadores de ativação glial no líquor preveem fenótipo depressivo. IL-6/QUIN/YKL-40 no LCR são mais próximos do tecido cerebral que marcadores séricos, mas invasivos e de baixa disponibilidade.

**[AT 2026-09-08] Central ≠ periférico com âncora meta-analítica — e o fenótipo real da micróglia humana:** meta-análise conjunta de **líquor, PET e pós-morte** mostra que os marcadores centrais de inflamação no TDM são **parcialmente independentes** dos periféricos, com alta heterogeneidade entre estudos (Enache et al., 2019)[MA; humano]; no líquor, meta-análise de citocinas e TRYCATs em transtornos psiquiátricos documenta alterações discretas e transdiagnósticas (Wang & Miller, 2018b)[MA; humano, LCR]. Em tecido humano pós-morte, a micróglia do deprimido **não exibe fenótipo pró-inflamatório clássico**: a citometria de massa single-cell revela perfil homeostático/suprimido (Böttcher et al., 2020)[EC; humano pós-morte], e o transcriptoma de núcleos isolados do córtex pré-frontal implica sobretudo **oligodendrócitos**, sem assinatura microglial inflamatória dominante (Nagy et al., 2020)[EC; humano pós-morte]. **Regras reforçadas [AT]:** (i) inflamação periférica ≠ neuroinflamação cerebral comprovada — todo marcador de sangue desta biblioteca tem teto de evidência para "neuroinflamação"; (ii) "TDM = micróglia M1" é falso — o modelo M1/M2 simplista, já rejeitado aqui, passa a ter contra-evidência celular humana direta.

---

*Steiner_2011_QUIN[EC] | YKL40_2024[EC] | Enache_2019[MA] | Wang_2018b[MA] | Bottcher_2020[EC] | Nagy_2020[EC]*

### 5.7 — Neuroimagem complementar: conectividade, MRS (mio-inositol), volume hipocampal (BLOCO05.007)

Além do TSPO-PET, três camadas de imagem complementam o quadro: **conectividade funcional córtico-estriatal** e cortico-límbica modificada por inflamação (taVNS altera amígdala-CPFdl, BLOCO04); **mio-inositol por MRS** como marcador glial in vivo; e **volume hipocampal**, que se associa a inflamação e desfecho terapêutico — após ECT, marcadores inflamatórios (IL-6/TNF) relacionam-se a volume hipocampal e resposta (Belge et al., 2020)[EC; humano] [VERIFICADO]. Estes marcadores não medem inflamação diretamente, mas capturam suas consequências estruturais/funcionais, e combinados ao TSPO aumentam a caracterização do subtipo. Assinaturas **convergentes multi-escala** — moleculares, celulares e de imagem cortical — reforçam que o sinal inflamatório se ancora em circuitos mensuráveis, e não em marcador isolado (Anderson et al., 2020)[EC; humano, multi-escala]. [AT]
---
*HippVol_ECT_2020[EC] | Anderson_2020[EC]*

---

### 5.8 — Controle de confundidores na leitura dos biomarcadores inflamatórios (anti-falso-positivo)

Painel único não decide; variáveis de ruído precisam ser controladas para não rotular como neuroinflamação o que é metabólico, circadiano ou analítico:

| Marcador / exame | Confundidor principal | Cuidado de interpretação |
|---|---|---|
| `exame_pcr_us` | IMC/adiposidade visceral (gordura secreta IL-6/TNF), infecção recente, tabaco, exercício | exigir ajuste por IMC; separar inflamação metabólica da do humor (p. ex. razão sTNFR2/adiponectina) |
| `exame_il6` | pulsatilidade e meia-vida curta; horário da coleta; privação de sono (B10) | padronizar coleta matinal; repetir; afastar privação de sono |
| `exame_tnfalpha` | adiposidade, inflamação metabólica | ajuste por IMC e comorbidades |
| `exame_il1beta` | instabilidade plasmática; difícil detecção em baixo-grau | não usar isolado para excluir mecanismo |
| TSPO-PET (central) | **genótipo rs6971** (baixa afinidade = falso-negativo) | exigir genotipagem antes de interpretar ausência de sinal |
| `exame_razao_kyn_trp` | triptofano dietético recente, insuficiência renal | controle de jejum/função renal |
| `exame_snps_inflamatorios` | marca risco estático, não estado atual | não usar como marcador de estado inflamatório ativo |
| Polifenóis/fitoterápicos como "evidência" | viés de publicação positivo, superdosagem in vitro, biodisponibilidade no SNC incerta | só valorar ensaio humano com desfecho mecanístico robusto (TSPO-PET, KYN/TRP) |

---

*Mediadores_2024[OB]*



### 5.x Biomarcadores (exames oficiais) — Exames referenciados por ID oficial (P19/P20)
- **`exame_pcr_us`**
- **`exame_il6`**
- **`exame_il1beta`**
- **`exame_tnfalpha`**
- **`exame_razao_kyn_trp`**
> ID oficial: exame_pcr_us, exame_il6, exame_il1beta, exame_tnfalpha, exame_razao_kyn_trp, exame_vhs, exame_fibrinogenio, exame_snps_inflamatorios. Elementos ainda não catalogados no módulo C-LAB (ex.: marcadores microgliais periféricos) são citados como papel biológico; cortes e protocolos residem no módulo laboratorial, não nesta biblioteca.

## BLOCO_06 — TRADUÇÃO CLÍNICA: DO MECANISMO AO SINTOMA

### 6.1 — Por que o SSRI não reverte o efeito da citocina sobre BDNF/CREB (BLOCO06.001)

Os antidepressivos monoaminérgicos atuam sobre disponibilidade de monoaminas, mas a citocina ataca um elo a jusante diferente: IL-1β/TNF suprimem BDNF/TrkB/CREB e plasticidade sináptica (ver BLOCO03.001/002) — um mecanismo que não é contornado apenas por aumentar serotonina sináptica. Em linhagens celulares humanas (linfoblastos) de pacientes deprimidos, biomarcadores de resposta a antidepressivo distinguem remitters de não-remitters, sugerindo que a resposta ao fármaco depende do estado imune/transcricional basal (Chukaew et al., 2021)[EC; humano] [VERIFICADO]. Isso explica por que, no subgrupo inflamado, a falha ao SSRI é mais comum (Raison et al., 2013)[EC; humano] [VERIFICADO]. Plasticidade sináptica e antidepressivos de ação rápida são revista nesta interface (Duman et al., 2016)[OB; revisão, humano] [VERIFICADO]. Natureza: mecanística em célula/humano; bem_suportado que inflamação alta prediz não-resposta.

**[AT 2026-09-08] Antidepressivos como sonda do eixo (sinal de alvo; nunca posologia — P20):** meta-análises de marcadores periféricos **antes/depois** de tratamento antidepressivo mostram queda de citocinas inflamatórias acompanhando a resposta clínica — IL-6, IL-1β e TNF-α caem sobretudo em **respondedores** (Köhler et al., 2018)[MA; humano] (Liu et al., 2020b)[MA; humano] (Wang et al., 2019)[MA; humano, ISRIs]. O achado repete-se molécula a molécula: sertralina (Xie et al., 2025)[MA; humano] e fluoxetina, em ~292 pacientes com TDM (García-García et al., 2022)[MA; humano]. Leitura canônica: a normalização inflamatória está **acoplada ao estado clínico** (marcador/consequência da resposta tanto quanto causa) — isso **modula**, e não fortalece, a inferência causal humana do mecanismo; os fármacos funcionam aqui como **sonda experimental de validação de alvo**, não como recomendação (P20).

---

*LCL_biom_2021[EC] | RCT_infliximab[EC] | PlastDep_2016[EC] | Kohler_2018[MA] | Liu_2020b[MA] | Wang_2019[MA] | Xie_2025[MA] | GarciaGarcia_2022[MA]*

### 6.2 — Gradiente de severidade: dose-resposta biológica (BLOCO06.002)

Existe relação entre magnitude da ativação inflamatória e intensidade/alcance do sintoma: níveis mais altos de marcadores associam-se a sintomas mais graves e a pior resolução (IL-6 baixa prediz melhor resolução de sintomas em sofrimento psicológico; Virtanen et al., 2015)[EC; humano] [VERIFICADO]. A meta-análise de variabilidade (Osimo et al., 2020)[MA; humano] [VERIFICADO] mostra que não há "deprimido inflamado" binário — a elevação é contínua e concentrada num subgrupo, e o risco/intensidade escalam com o marcador. A progressão do sickness agudo (autolimitado) para o comportamento depressivo persistente acompanha a persistência/amplitude do sinal citocínico (Dantzer, ver BLOCO01). Natureza: gradiente associativo bem_suportado em humano.

---

*IL6resol_2015[EC] | Osimo_meta[EC]*

### 6.3 — Depressão induzida por interferon-α: paradigma causal humano (BLOCO06.003)

O modelo mais próximo de causalidade direta em humanos é a terapia com **IFN-α** (hepatite C/melanoma): um indutor inflamatório exógeno precipita sintomas depressivos de novo em indivíduos sem transtorno de humor prévio, com cronologia previsível (semanas) e fenomenologia característica. Análise dimensional dos sintomas em pacientes com melanoma mostra clusters neuropsiquiátricos específicos que emergem ao longo dos primeiros três meses e são prevenidos/revertidos por paroxetina (Capuron et al., 2002)[EC; humano] [VERIFICADO]. O mecanismo bioquímico inclui queda de triptofano sérico associada aos sintomas depressivos (Capuron et al., 2002)[EC; humano] [VERIFICADO] — consistente com indução de IDO/desvio quinurenínico. A inflamação por IFN-α também reduz o feedback negativo de glicocorticoide (resistência ao eixo HPA), ligando inflamação à disfunção do estresse (Felger et al., 2016)[EC; humano] [VERIFICADO]. Revisões clínicas consolidam hepatite C/IFN-α e depressão (Zdilar et al., 2000)[OB; humano, sem abstract — texto completo]. Natureza: causal humano (intervenção), muito_estabelecido.

---

*IFNcancer_2002[EC] | Trp_2002[EC] | IFN_HPA_2016[EC] | HepC_2000[OB]*

### 6.4 — Subtipo anedônico e circuito de recompensa (BLOCO06.004)

A inflamação impacta seletivamente o **circuito de recompensa córtico-estriatal ventral**, produzindo anedonia. Em TDM, inflamação elevada associa-se a baixa conectividade funcional nos circuitos cortico-estriatais de recompensa e a sintomas de anedonia — relação que envolve impacto da inflamação sobre síntese/liberação de dopamina (Bekhbat et al., 2022)[EC; humano, fMRI] [VERIFICADO]. Em mulheres expostas a trauma, PCR/citocinas elevadas associam-se a alteração do circuito de recompensa e a anedonia/sintomas de TEPT (Mehta et al., 2020)[EC; humano, fMRI] [VERIFICADO]. Este é o embrião do "subtipo anedônico-inflamatório": inflamação → redução de conectividade córtico-estriatal ventral → anedonia, com análogo animal no comportamento de não-preferência. O desafio experimental com endotoxina (LPS humano) reproduz alterações de recompensa/anedonia transitória [EC; revisão]. Natureza: associativo/neural em humano, bem_suportado; causalidade via desafio endotoxinal e IFN.

---

*Reward_2022[EC] | RewardTrauma_2020[EC]*

### 6.5 — Nota de escopo clínico

Este bloco descreve mecanismos de tradução e estratificação biológica, não conduta. Não há recomendação de dosagem de anti-inflamatório/biológico para depressão fora das bibliotecas de Intervenções; o RCT do infliximabe (BLOCO05, 09.3) é prova de conceito de estratificação por biomarcador, com resultado primário negativo na amostra total.
---
> *Sem referência específica nesta seção — trata-se de nota de escopo/lacuna declarada (ver CONTROVÉRSIAS E LACUNAS).*
---

### 6.6 — Ansiedade e estresse traumático: meta-evidência e o subtipo TEPT neuroimune suprimido (BLOCO06.006)

A tradução clínica da neuroinflamação **não é exclusiva da depressão**, mas a evidência por transtorno de ansiedade é **heterogênea e de tamanho de efeito pequeno**. Uma meta-análise transdiagnóstica encontra diferença significativa (porém modesta, Hedge's g≈0,4) nas citocinas pró-inflamatórias entre indivíduos com ansiedade/TEPT/TOC e controles, com o efeito moderado por comorbidade depressiva (Renna et al., 2018)[MA; humano] [VERIFICADO]; a meta-análise dedicada ao transtorno de ansiedade generalizada (14 estudos) encontra alterações periféricas com heterogeneidade (Costello et al., 2019)[MA; humano] [VERIFICADO]. Por transtorno, o quadro é **misto, não universal**: no **TOC**, as citocinas (TNF-α, IL-6, IL-1β, IL-4, IL-10, IFN-γ) **não diferiram significativamente** dos controles na meta-análise, que reporta resultados inconsistentes (Cosco et al., 2019)[MA; humano] [VERIFICADO] — um achado nulo relevante; no **pânico**, uma revisão sistemática narrativa (não meta-análise) relata elevação de IL-6/IL-1β em parte dos estudos, com conflitos para outras citocinas (Quagliato et al., 2018)[OB; revisão sistemática]; no **TEPT**, a meta-análise confirma marcadores periféricos elevados (Passos et al., 2015)[MA; humano] [VERIFICADO].

**Contra-padrão decisivo:** o TEPT não é uniformemente "inflamação alta". Estudo combinando **PET de TSPO e tecido pós-morte** encontra **supressão neuroimune** (sinal glial reduzido) em subgrupo de TEPT (Bhatt et al., 2020)[EC; humano, PET+pós-morte] [VERIFICADO] — paralelo ao hipocortisolismo da B2; o TSPO como alvo em doenças relacionadas ao estresse é revisado (Rupprecht et al., 2022)[OB; revisão] [VERIFICADO]. Em crianças/adolescentes, a revisão sistemática de transtornos de base ansiosa encontra uma associação combinada que **se aproxima da significância** mas permanece inconsistente entre estudos (Parsons et al., 2021)[OB; revisão sistemática], e a meta-análise exploratória de internalizantes pediátricos reporta alterações de citocinas dependentes de moderadores (Howe et al., 2022)[MA; humano] [VERIFICADO]. A via imuno-quinurenina está implicada nos transtornos de ansiedade (Kim YK et al., 2018)[OB; revisão, humano] [VERIFICADO]. Natureza: associativo em humano; o subtipo suprimido exige não tratar "inflamação alta" como universal.

---

*Renna_ansiedade_2018[MA] | Costello_ansiedade_2019[MA] | TOC_imune_2019[MA] | Panico_citocinas_2018[OB] | PTSD_marc_2015[MA] | PTSD_supressao_2020[EC] | TSPO_estresse_2022[OB] | Ansiedade_ped_2021[OB] | Internalizante_ped_2022[MA] | Quinur_ansiedade_2018[OB]*

### 6.7 — Tradução anti-inflamatória na ansiedade: medo/extinção e ensaios (descrever o estudo; P20) (BLOCO06.007)

Há tradução experimental em mecanismo de medo/ansiedade. **Minociclina atenua a retenção de memória de medo em voluntários saudáveis** em ensaio randomizado placebo-controlado (recrutados 107 voluntários; N=105 no teste de evocação da memória de medo, 53 minociclina/54 placebo) (Xia et al., 2024)[EC; humano, RCT em saudáveis] [VERIFICADO] — evidência de modulabilidade farmacológica da memória do medo, **não** teste do fármaco em pacientes com transtorno de ansiedade; em rato, reverte o prejuízo de extinção do medo induzido por IFN-α (Bi et al., 2016)[ML; rato] [PRÉ-CLÍNICO]. Uma mega-análise de 18 RCTs de fármacos imunomoduladores (N=10.743, nove doenças) mostra benefício para **sintomas depressivos/psicológicos** (SF-36/HADS), restrito ao estrato com sintomas basais altos — prova de conceito imunomodulador, não específica de ansiedade (Wittenberg et al., 2020)[MA; mega-análise de RCT] [VERIFICADO]. Ômega-3 (LCPUFA) associa-se a redução de sintomas de ansiedade (Su et al., 2018)[MA; humano, JAMA Netw Open] [VERIFICADO]. Estes são achados de **estudo**, não recomendação de conduta (doses/posologia pertencem ao módulo operacional, não a esta biblioteca). Natureza: intervencionista em humano (minociclina/ômega/imunomoduladores) com heterogeneidade; a qualidade da evidência é variável.

---

*Minociclina_medo_2024[EC] | Minociclina_extincao_2016[ML] | Mega_imunomod_2020[MA] | Omega3_ansiedade_2018[MA]*

## BLOCO_07 — NÓS MOLECULARES CENTRAIS (síntese)

> Não gera query própria. Sintetiza claims já aprovados nos BLOCOs 02/03/08. Critério de "nó central": (1) está a montante de múltiplas vias; (2) recebe convergência de gatilhos distintos; (3) tem prova de manipulação causal; (4) conecta marcador periférico a mecanismo central.

### 7.1 — NF-κB como nó central candidato (BLOCO07.001)

O **NF-κB** atende aos quatro critérios e é o principal candidato a nó molecular central da neuroinflamação B1:

1. **Montante de múltiplas vias:** NF-κB é o saída transcricional comum de TLR4/MyD88, TNFR1 e IL-1R1 — via IRAK/TRAF6→IKK→degradação de IκBα→translocação nuclear — dirigindo a transcrição de IL1B, IL6, TNF, do próprio NLRP3 (priming), PTGS2/COX-2 e NOS2/iNOS (BLOCO02.015)[ML].
2. **Convergência de gatilhos distintos:** PAMPs (LPS bacteriano/translocação intestinal B7), DAMPs (HMGB1, S100, mtDNA), citocinas e estresse psicológico todos convergem em NF-κB (BLOCO02.004/008/009/08.005).
3. **Prova causal por manipulação:** inibição farmacológica da cascata TLR4/TRAF6/NF-κB reduz neuroinflamação, ativação microglial e prejuízo comportamental em modelos (BLOCO02.015)[ML; camundongo]; resistência a glicocorticoide desinibe NF-κB (BLOCO08.001, GR reprime genes inflamatórios gene-especificamente)[ML/EC].
4. **Ligação marcador↔mecanismo:** NF-κB é o elo que transforma sinal imune periférico (PCR/IL-6 elevados) em transcrição central de citocinas, IDO (quinurenina), COX-2/PGE2 e priming do NLRP3 — fechando o caminho do marcador de sangue ao sintoma (anedonia, BLOCO06).

---

*Gastrodin_2024[ML] | GR_repress_2018[ML]*

### 7.2 — NLRP3 como segundo nó (executor)

Se NF-κB é o nó transcricional, o **inflamassoma NLRP3** é o nó executor a jusante: recebe o priming de NF-κB e o "sinal 2" (ATP/P2X7, mtROS/MAMs, K+, cristais, mtDNA via cGAS-STING) e produz IL-1β/IL-18 maduros e piroptose GSDMD (BLOCO02.001, 08.006/009). Prova causal forte: variantes humanas ganho-de-função geram inflamassoma constitutivo (CAPS)[EC humano]; inibidores e a deleção reduzem dano; NEK7 modula o complexo e alivia comportamento depressivo em rato ()[ML].

---

*CAPS_2024[EC] | NEK7_2025[ML]*

### 7.3 — Relação entre os dois nós e o subtipo

NF-κB (transcrição/priming) e NLRP3 (execução/piroptose) formam um eixo de dois estágios, contido por freios (IL-10/STAT3, miR-146a, SPMs, GR) e amplificado por loops (B6/ROS, B9/mitocôndria, B2/resistência a glicocorticoide). A falha dos freios + persistência de gatilhos (obesidade, trauma, disbiose, sono) cronifica o eixo — substrato do subtipo "depressão inflamatória" (BLOCO11). Ambos os nós são mecanísticos em animal/célula; em humanos o fechamento causal vem de marcadores (PCR/IL-6/KYN-TRP/TSPO), genética (Bull IL-6, FKBP5) e intervenção de prova (IFN-α, infliximabe no subgrupo).
---
*Swanson_2019[ML] | cGAS_POCD_2024[ML]*

---

## BLOCO_08 — CONEXÕES BIDIRECIONAIS E LOOPS (B1 ↔ B2…B14)

> Cada conexão aponta o mecanismo-alvo (cross-ref). O foco aqui é o ELO molecular; a biologia completa do mecanismo parceiro reside na biblioteca dele (regra de fronteira).

### 8.1 — B1→B2: resistência a glicocorticoides (NF-κB/GR/FKBP5) (BLOCO08.001)

O glicocorticoide ativado (GR) reprime potemente a inflamação de macrófagos; análise genômica mostra que o GR reprime genes pró-inflamatórios por mecanismos gene-específicos (genes "pausados" prontos para transcrição, controlados por NELF/Pol2) (Sacta et al., 2018)[ML; célula/camundongo] [PRÉ-CLÍNICO]. Quando FKBP5 está elevada/desmetilada (Klengel 2013, BLOCO02.20) ou a citocina sinaliza NF-κB de forma sustentada, o GR perde eficácia repressora — a resistência a glicocorticoides desinibe o NF-κB, fechando loop. A inflamação por IFN-α reduz o feedback negativo do HPA em humanos (Felger et al., 2016)[EC; humano] [VERIFICADO]. Biologia de FKBP e sinalização inflamatória é revista (Mehta et al., 2020)[OB; revisão]. Cross-ref: **mecanismo_B2_eixo_hpa_cortisol**.

---

*GR_repress_2018[ML] | IFN_HPA_2016[EC] | FKBP_inflam_2020[OB] | RewardTrauma_2020[EC]*

### 8.2 — B1→B3: citocinas suprimem BDNF/CREB e complemento faz poda (BLOCO08.002, 003)

IL-1β/TNF suprimem BDNF/TrkB/CREB (ver BLOCO03.001/002; IL-1β reduz mRNA de BDNF hipocampal, 1993)[ML] [PRÉ-CLÍNICO]. Paralelamente, a **poda sináptica mediada por complemento C1q/C3** pela micróglia é necessária ao desenvolvimento (Schafer et al., 2012)[ML; camundongo], mas quando excessiva no adulto é candidata a perda sináptica na depressão: a disbiose intestinal induz comportamento tipo-depressivo via poda anormal dependente de complemento (Hao et al., 2024)[ML; camundongo], e a inibição de PDE4 alivia poda fagocítica excessiva mediada por HMGB1/C1q/C3 (Zhao et al., 2025)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano]. Cross-ref: **mecanismo_B3_neuroplasticidade**.

---

*IL1b_BDNF_1993[ML] | Poda_2012[ML] | GutC3_2024[ML] | PDE4_2025[ML]*

### 8.3 — B1↔B6/B9: ROS/mtDNA amplificam o NLRP3 (BLOCO08.004, 006)

Espécies reativas e disfunção mitocondrial alimentam o "sinal 2" do NLRP3: mtROS e vazamento de mtDNA ativam tanto o inflamassoma quanto cGAS-STING (BLOCO02.018), e a resposta inflamatória por sua vez gera mais dano mitocondrial — loop B1→B6 (estresse oxidativo)→B9 (disfunção mitocondrial)→B1. Os contatos retículo-mitocôndria (MAMs) na micróglia medeiam comportamento tipo-depressivo (BLOCO04.003)[ML; camundongo]. Cross-ref: **mecanismo_B6_estresse_oxidativo**, **mecanismo_B9_disfuncao_mitocondrial**, **mecanismo_B15_autofagia_mtor** (a falha de mitofagia/autofagia do mtDNA lesado alimenta o loop — conexão B1↔B15, a aprofundar na biblioteca B15).

---

*MAMs_2024[ML]*

### 8.4 — B1↔B7: LPS-TLR4 periférico e translocação (BLOCO08.005)

Estresse psicológico compromete a barreira intestinal, permitindo translocação bacteriana (LPS) que ativa TLR4 periférico e central: LPS derivado do intestino e TLR4 periférico medeiam inflamação no estresse (Cho et al., 2024)[ML; camundongo], e a estimulação da via TLR4 cerebral no estresse crônico é relevante para depressão (Gárate et al., 2011)[ML; rato] [EXTRAPOLADO: animal/célula→humano]. Disbiose agrava depressão pós-AVE via NLRP3 microglial (BLOCO03/04). Cross-ref: **B7_eixo_intestino_cerebro**.

---

*GutLPS_2024[ML] | TLR4brain_2011[ML]*

### 8.5 — B1→B4: SERT/p38 MAPK e dopamina de recompensa (BLOCO08.007)

Citocinas aumentam atividade/expressão do transportador de serotonina (SERT) via p38 MAPK, reduzindo serotonina sináptica — eixo que conecta inflamação à monoamina. Em paralelo, IFN-α/inflamação reduzem disponibilidade de dopamina em circuitos de recompensa, produzindo anedonia (ver BLOCO06.004: conectividade córtico-estriatal e anedonia)[EC; humano]. Cross-ref: **B4_deficiencias_monoaminas**. (O vínculo SERT/p38 específico  sem estudo dedicado na literatura consultada; mecanismo proposto na literatura.)

---

*Reward_2022[EC]*

### 8.6 — B1→B5: glutamato glial e EAAT2 (BLOCO08.008)

Citocinas deprimem o transportador de glutamato EAAT2/GLT-1 astrocitário e promovem liberação de glutamato via hemicanais (conexina/panexina), com redução de glutamina sintetase — levando a glutamato extracelular excessivo e excitotoxicidade. A privação de sono induz ansiedade via IL-6 e eixo astrócito-GABA no PAG (Xu et al., 2026)[ML; camundongo], ilustrando modulação glial do neurotransmissor. Cross-ref: **mecanismo_B5_gaba_glutamato**. (O mecanismo de modulação glial do glutamato/EAAT2 é proposto na literatura, sem estudo dedicado direto na literatura consultada.)

---

*SleepIL6_2026[ML]*

### 8.7 — B1→B8: vitamina D/VDR, zinco/NLRP3, magnésio/NF-κB (BLOCO08.009)

Micronutrientes modulam a ativação imune: vitamina D/VDR modula ativação microglial (Menéndez et al., 2024)[OB; revisão, humano+animal]. Zinco regula NLRP3 e magnésio inibe NF-κB (mecanismos propostos na literatura, sem estudo dedicado na literatura consultada). Cross-ref: **B8_deficiencias_micronutrientes**.

---

A vitamina D/VDR modula a ativação microglial e a neuroinflamação (VitD_2024[ML]; pré-clínico).

### 8.8 — B1→B10: sono, relógio e NLRP3 (BLOCO08.010)

Privação de sono eleva IL-6/TNF/PCR: privação aguda de sono exacerba inflamação sistêmica e distúrbios psiquiátricos (Yang et al., 2023)[ML; camundongo], e sono perdido induz ansiedade via IL-6 (Xu et al., 2026)[ML] [PRÉ-CLÍNICO]. Genes do relógio (BMAL1/CLOCK/PER) regulam o limiar do NLRP3 e a fagocitose microglial varia no ciclo claro-escuro (crosstalk ritmo-imune). Cross-ref: **B10_desregulacao_circadiana**.

---

*SleepInflam_2023[ML] | SleepIL6_2026[ML]*

### 8.9 — B1→B11: desiodase tipo 2 (D2) e tireoide (BLOCO08.011)

LPS induz a desiodase tipo 2 (D2) em tanicitos do hipotálamo mediobasal — a principal enzima que converte T4 em T3 ativo no SNC (Fekete et al., 2004)[ML; rato/humano], e o gene dio2 humano tem elemento responsivo a NF-κB (Zeöld et al., 2006)[ML] [PRÉ-CLÍNICO]. Assim a inflamação altera o metabolismo tireoidiano central (síndrome do eutireoideo doente). Cross-ref: **B11_disfuncao_tireoidiana**.

---

*D2_LPS_2004[ML] | dio2_NFkB_2006[ML]*

### 8.10 — B1→B12: trauma precoce, FKBP5 e priming (BLOCO08.012)

Adversidade na infância faz priming microglial e marca FKBP5: desmetilação alelo-específica dependente de trauma (Klengel 2013, BLOCO02.20) e efeitos intergeracionais na metilação de FKBP5 em sobreviventes do Holocausto e seus filhos (Yehuda et al., 2016)[EC; humano] [VERIFICADO]. FKBP5 é nó compartilhado trauma↔inflamação; TEPT tem marcadores inflamatórios elevados. Cross-ref: **B12_neurobiologia_trauma**.

---

*Klengel_2013[EC] | Holocausto_2016[EC]*

### 8.11 — B1→B13: endocanabinoides (CB2/FAAH/MAGL) (BLOCO08.013)

O receptor CB2 microglial tem efeito anti-inflamatório compensatório, e metabólitos de FAAH/MAGL alimentam a via de prostaglandinas (crosstalk com 2.17). Mecanismo proposto, ainda sem estudo dedicado na literatura consultada. Cross-ref: **B13_sistema_endocanabinoide** — gap de busca.

### 8.12 — B1→B14: esteroides neuroativos (alopregnanolona, estrogênio) (BLOCO08.014)

Alopregnanolona tem efeito anti-inflamatório microglial, e estrogênio/17β-estradiol derivado do cérebro (BDE2) modula ativação glial com diferenças entre sexos (Brann et al., 2022)[OB; revisão] [EXTRAPOLADO: animal/célula→humano] — consistente com as diferenças sexuais na ligação inflamação-depressão (BLOCO05, meta 2024). Cross-ref: **mecanismo_B14_neuroesteroides_hormonios**.

---

O 17beta-estradiol derivado do cérebro (BDE2) modula a resposta neuroinflamatória (Estrogen_2022[ML]; pré-clínico).

### 8.13 — B1↔B15: autofagia/mitofagia e o loop com o inflamassoma (BLOCO08.015)

A autofagia (e, especificamente, a **mitofagia** — degradação seletiva de mitocôndrias danificadas) regula a inflamação: a falha da mitofagia deixa mtDNA e mtROS vazarem, alimentando o "sinal 2" do NLRP3 e o loop B1→B6/B9→B1 (ver 8.3). Reciprocamente, a ativação de NF-κB pode suprimir a autofagia, fechando um ciclo de amplificação. Ainda não há, neste corpus, um estudo dedicado B1↔B15 específico para comportamento depressivo em humano; a conexão é inferida de trabalhos mecanísticos em célula/animal sobre mitofagia e NLRP3 (campo emergente). Cross-ref: **mecanismo_B15_autofagia_mtor** — fica como **gap de busca** (conexão mecanisticamente esperada, a confirmar com literatura dedicada na biblioteca B15).

---

> *Sem referência específica dedicada nesta seção — conexão inferida de 8.3 (mtDNA/mtROS/NLRP3); gap declarado (ver CONTROVÉRSIAS E LACUNAS).*

---

## BLOCO_09 — IMPACTO DA NEUROINFLAMAÇÃO SOBRE NEUROPLASTICIDADE (elo B1→B3)

> Regra de fronteira: a biologia da plasticidade (LTP/LTD, BDNF, AMPA) reside em B3; aqui fica o ELO da citocina sobre ela.

### 9.1 — Citocinas sobre LTP/LTD hipocampal (BLOCO09.001)

IL-1β e TNF-α, em níveis fisiológicos, modulam plasticidade; quando elevados na neuroinflamação, deprimem LTP e favorecem LTD no hipocampo. IL-1 é regulador central da resposta de estresse e a produção cerebral de IL-1 liga o desafio imunológico/psicológico à ativação neuroendócrina e à plasticidade (Goshen et al., 2009)[OB; revisão, humano+animal] [VERIFICADO]. A revisão de ativação glial em transtornos mentais consolida que citocinas interferem com plasticidade sináptica e memória (Almeida et al., 2020)[OB; revisão] [VERIFICADO]. O mecanismo molecular é a supressão de BDNF/CREB (BLOCO03.001: IL-1β reduz mRNA de BDNF hipocampal, 1993)[ML; rato] [PRÉ-CLÍNICO]. Natureza: causal em fatia/animal; em humanos por marcadores e desfecho cognitivo.

---

*IL1_stress_2009[ML] | GliaMental_2020[ML] | IL1b_BDNF_1993[ML]*

### 9.2 — Remodelamento dendrítico e reversibilidade (BLOCO09.002)

Ativação inflamatória induz retração dendrítica e perda de espinhas, com componente de dano sinaptodendrítico. Microglia controla sinapses glutamatérgicas no hipocampo adulto: a depleção farmacológica de microglia altera a transmissão CA3-CA1, demonstrando regulação contínua da sinapse pela glia (Basilico et al., 2022)[ML; camundongo] [PRÉ-CLÍNICO]. Em HIV, dano sinaptodendrítico cortical é regulado por opioides e quimiocinas mesmo sem morte neuronal (Nash et al., 2019)[EC; humano+animal] [EXTRAPOLADO: animal/célula→humano] — modelo de dano reversível por modulação imune. A reversibilidade após normalização da inflamação é consistente com a melhora de marcadores/cognição após anti-inflamatório/antidepressivo, mas o vínculo direto de reversibilidade dendrítica em TDM humana é [EXT]/emergente.

---

*MicrogliaGlut_2022[ML] | HIVdend_2019[ML]*

### 9.3 — TNF-α e scaling sináptico homeostático (BLOCO09.003)

Além do LTP/LTD (ajuste rápido de sinapses individuais), existe o **scaling sináptico homeostático** — ajuste lento e multiplicativo da força global de sinapses para manter a atividade neural em faixa. Esse scaling é mediado por **TNF-α glial**: o TNF derivado da glia ajusta a força de receptores AMPA na membrana para estabilizar a atividade da rede (Stellwagen et al., 2006)[ML; camundongo/rato, Nature] [PRÉ-CLÍNICO]. É um papel FISIOLÓGICO do TNF — quando a inflamação crônica desregula esse sinal, o mecanismo homeostático deixa de estabilizar e passa a contribuir a disfunção de circuito. Distingue-se do LTP/LTD (9.1) e do remodelamento dendrítico (9.2): o scaling é glia-dependente e homeostático, não hebbiano. Natureza: mecanismo clássico muito_estabelecido em animal; relevância para depressão é inferida [EXT].
---
*TNFscaling_2006[ML]*

---

## BLOCO_10 — IMPACTO SOBRE A NEUROGÊNESE ADULTA (elo B1→B16; condicional)

> Regra P16: a biologia completa da neurogênese adulta reside na biblioteca **B16 (neurogênese)**. Aqui fica apenas o ELO das citocinas sobre proliferação/sobrevivência de células-tronco neurais (NSC) no giro denteado — 1–2 frases por ponto, com referência cruzada.

### 10.1 — IL-6 suprimindo proliferação de NSC (BLOCO10.001)

Citocinas pró-inflamatórias deprimem a neurogênese hipocampal adulta. O ambiente inflamatório e a ativação microglial alteram o destino das NSC; a maquinaria de IFN-α/IL-6 em células-tronco neurais está documentada na depressão induzida por citocinas (Zheng et al., 2014)[ML; célula, BLOCO02.16] [EXTRAPOLADO: animal/célula→humano] — IL-6/STAT3 em contexto inflamatório sustém o estado antiproliferativo, ainda que IL-6 trans-sinalizante seja reparativo em microglia (BLOCO03.003, dualidade). O efeito sobre NSC do giro denteado é supressivo na inflamação crônica [ML; EXT]. Cross-ref: **mecanismo_B16_neurogenese**.

---

*IFN_NSC_2014[ML]*

### 10.2 — IL-1β e TNF-α suprimindo proliferação/sobrevivência de NSC (BLOCO10.002)

IL-1 é regulador central da resposta de estresse e da função neural (Goshen et al., 2009)[OB; revisão, humano+animal] [VERIFICADO]; IL-1β e TNF ativam NF-κB nas NSC e reduzem proliferação/sobrevivência de novos neurônios do giro denteado — elo causal distinto e complementar ao do IL-6. Em modelo, estresse crônico/inflamação reduz neurogênese e intervenções anti-inflamatórias a restauram [ML; EXT]. Cross-ref: **B16** (fases da neurogênese em detalhe).

---

*IL1_stress_2009b[ML]*

### 10.3 — Microglia homeostática/IL-4 como contraponto pró-neurogênico (BLOCO10.003)

Nem toda glia inibe: a microglia em fenótipo anti-inflamatório (M2/Th2) SUPORTA a neurogênese. Vesículas extracelulares derivadas de microglia M2 modulam o destino das NSC após isquemia, promovendo neurogênese (Zhang et al., 2025)[ML; camundongo] [PRÉ-CLÍNICO]. TREM2 polariza microglia para M2 e melhora neurogênese (Peng et al., 2025)[ML; camundongo], e o eixo IL-4/STAT6 reverte defeito proliferativo em células-tronco neurais humanas (Chen et al., 2024)[EC; humano] [EXTRAPOLADO: animal/célula→humano]. É o contraponto compensatório aos elos supressivos: o sinal imune tem duas faces sobre NSC, dependendo do fenótipo glial. Natureza: pró-neurogênico M2/IL-4 bem demonstrado em animal/célula humana; contexto depressão [EXT].
---
*M2ves_2025[ML] | TREM2_2025[ML] | IL4_STAT6_2024[EC]*

### 10.4 — NLRP3 microglial como freio da neurogênese: sinal pré-clínico de 2026 (BLOCO10.004) [AT]

[APENAS PRÉ-CLÍNICO] [EXTRAPOLADO: encefalopatia diabética→TDM] Em modelo murino de **encefalopatia diabética**, a hiperglicemia induz **piroptose microglial dependente de NLRP3/GSDMD** que **inibe a neurogênese hipocampal adulta** e produz disfunção cognitiva; o bloqueio do eixo resgata a neurogênese e a cognição (Hua et al., 2026)[ML; camundongo]. Leitura canônica: é o elo molecular direto e manipulável "inflamassoma → supressão neurogênica" mais recente do corpus, mas demonstrado **fora do contexto depressivo** — reforça a plausibilidade dos elos 10.1–10.2 **sem** alterar o status **condicional** do BLOCO_10. Regra P16 mantida: a neurogênese em si (magnitude humana, controvérsia ativa) é território da **B16**; aqui fica apenas a modulação imune sobre ela. [AT]

---

*Hua_2026[ML]*

---

## BLOCO_11 — ESTRATIFICAÇÃO (subtipo inflamatório; condicional)

> Este bloco só existe na medida em que há subtipos biologicamente documentados. Depende dos BLOCOs 02–09 já triados; não gera query própria. Conteúdo de conduta clínica/dosagem permanece nas bibliotecas de Intervenções.

### 11.1 — Substrato mecanístico do subtipo "depressão inflamatória" (BLOCO11.001)

Aproximadamente **27%** dos pacientes com depressão apresentam PCR-us elevada (acima do limiar de inflamação de baixo grau definido no módulo C-LAB), com razão de chances ~1,46 para inflamação de baixo grau versus controles (achado epidemiológico da trilha SM; a meta de Osimo 2020 confirma que a elevação é de um SUBGRUPO e não universal — ver BLOCO05)[MA; humano] [VERIFICADO]. O substrato mecanístico deste subtipo é a **ativação sustentada do eixo NF-κB→NLRP3** (BLOCO07) com: (a) marcadores periféricos elevados (PCR, IL-6, sTNFR2) e índice KYN/TRP desviado (BLOCO05.001/004); (b) sinal central (TSPO-PET elevado em córtex cingulado/ínsula; QUIN pós-morte em subregião cingulada — BLOCO05.002/006); (c) assinatura neural de anedonia (baixa conectividade córtico-estriatal ventral; BLOCO06.004); e (d) modificabilidade por intervenção anti-TNF exclusivamente quando o marcador basal está alto (RCT infliximabe: negativo na amostra toda, positivo no subgrupo inflamado — BLOCO05/09.3)[RCT; humano].

A estratificação por biomarcador (painel combinado PCR+IL-6+sTNFR2+KYN/TRP, BLOCO05.003) é o que dá especificidade — o subtipo não é diagnosticável por um marcador único nem por sintoma isolado, e a inflamação NÃO está elevada na maioria dos pacientes.

---

*Osimo_2020[MA] | RCT_infliximab[EC] | Setiawan_2015[EC] | Steiner_2011_QUIN[EC] | Reward_2022[EC]*

### 11.2 — Candidatos futuros (NÃO convertidos em claim formal agora)

Os subtipos abaixo aguardam que o bloco seja priorizado e ganhem item formal só com documentação biológica:
- **Depressão resistente ao tratamento (TRD):** perfil TNF/sTNFR2/PCR mais elevado que a depressão responsiva; inflamação prediz não-resposta a SSRI (BLOCO06.001).
- **Depressão perinatal:** disfunção do ajuste imunológico gestacional; Treg/Th17 (BLOCO04.006).
- **TEPT com fenótipo pró-inflamatório:** elevação consistente IL-6/TNF/PCR associada a trauma infantil; FKBP5 como nó compartilhado (BLOCO08.012, Klengel/Holocausto).
- **Depressão tardia/geriátrica:** componente de senescência glial/SASP e priming (BLOCO02.014, inflamm-aging) — hipótese inicial.

Estes permanecem como `gap_pesquisa`/candidatos, sem vínculo de assertividade forte.

---

*Bull_2009[EC] | Treg_2024[EC]*

### 11.3 — Nota de escopo

TOC (transtorno obsessivo-compulsivo) fica FORA do escopo central (capítulo próprio do DSM); o exame Y-BOCS entra apenas para rastreio/diferencial de comorbidade, conforme o protocolo de escopo. Este bloco descreve estratificação biológica e não recomendação de tratamento; dosagem/posologia de anti-inflamatórios ou biológicos pertencem às bibliotecas de Intervenções e Suplementos.
---
> *Sem referência específica nesta seção — trata-se de nota de escopo/lacuna declarada (ver CONTROVÉRSIAS E LACUNAS).*

### 11.4 — Critérios operacionais de estratificação (raciocínio clínico estruturado)

> **Ressalva obrigatória:** os critérios abaixo destinam-se ao raciocínio fisiopatológico e à pesquisa. **Não constituem diagnóstico formal, não substituem o julgamento clínico individualizado e não contêm prescrição ou protocolo de tratamento.** Limiares numéricos e faixas de referência residem exclusivamente na Biblioteca de Biomarcadores/Exames (C-LAB), referenciada por ID oficial.

---

#### Critério A — biomarcadores (por ID oficial)

Referenciados por **ID oficial de exame**, com direção esperada e papel discriminativo (o valor de corte fica no C-LAB, nunca aqui):

- **`exame_pcr_us`** — ↑ ; papel discriminativo **primário** (marcador periférico mais replicado do subtipo; sensível, inespecífico sozinho).
- **`exame_il6`** — ↑ ; papel discriminativo **primário** (mediador a montante da PCR; pulsátil).
- **`exame_tnfalpha`** e o receptor solúvel **sTNFR2** — ↑ ; papel discriminativo **secundário** (via paralela que converge em NF-κB; mais informativo na depressão resistente ao tratamento).
- **`exame_il1beta`** — ↑ ; papel discriminativo **secundário** (produto do inflamassoma; menos disponível clinicamente).
- **`exame_razao_kyn_trp`** — ↑ ; papel discriminativo **complementar** (indica ativação específica da via da quinurenina/IDO; mais informativo quando há sintomas de recompensa/ideação).
- **`exame_snps_inflamatorios`** — contexto de **predisposição** (não estado agudo); reforça probabilidade, não isolado (ex.: IL-6 rs1800795 modulando a depressão induzida por interferon — Bull 2009; FKBP5 trauma-dependente — Klengel 2013).

> **Por que painel e não marcador único:** PCR é fase aguda hepática e sobe com obesidade/infecção/sono; IL-6 é pulsátil; sTNFR2 reflete ativação TNF crônica; KYN/TRP reflete atividade enzimática. Combinar um marcador *upstream* (PCR/IL-6) com um *downstream* (KYN/TRP) e um de *estabilidade* (sTNFR2) reduz falso-positivo por confundidor (ver BLOCO_05.003).

---

#### Critério B — fenótipo clínico (itens pontuáveis)

Cada item tem a **base mecanística** correspondente nesta Biblioteca (máximo de 6 itens, 1 ponto por item presente):

1. **Sintomas atípicos** (hiperfagia, hipersonia) — sobreposição do subtipo inflamatório com o fenótipo atípico (BLOCO_06.02).
2. **Fadiga/lentificação psicomotora** marcada e desproporcional ao humor deprimido relatado — *sickness behavior* mediado por via vagal/BBB (BLOCO_01.002, BLOCO_06).
3. **Histórico de depressão resistente** a ≥2 linhas de tratamento monoaminérgico — divergência de alvo mecanístico: a citocina suprime BDNF/CREB independentemente da recaptação de monoaminas (BLOCO_06.001).
4. **Sintomas somáticos/dor difusa** não explicados por outra condição — quimiocinas/PGE2 e sensibilização periférica (BLOCO_03.011, BLOCO_06).
5. **Comprometimento cognitivo** desproporcional à gravidade do humor — impacto sobre plasticidade e conectividade córtico-límbica (BLOCO_09).
6. **Anedonia proeminente** com redução de recompensa — inflamação sobre o circuito córtico-estriatal ventral/dopamina (BLOCO_06.004).

---

#### Critério C — contexto clínico que eleva a probabilidade do mecanismo

Fatores presentes/ausentes, cada um com base mecanística já descrita:

- **Comorbidade autoimune/sistêmica** documentada — sobreposição direta de vias imunes.
- **Obesidade/síndrome metabólica** — tecido adiposo como fonte adicional de IL-6/TNF e confundidor (BLOCO_01.004, BLOCO_05.003).
- **Histórico de trauma/adversidade na infância** — FKBP5 e priming microglial de longo prazo (BLOCO_08.012; Klengel 2013; efeito intergeracional — Holocausto 2016).
- **Doença cardiovascular estabelecida** — PCR/IL-6 compartilhados como marcador de risco (BLOCO_06.005).
- **Privação de sono crônica** ou transtorno do sono não tratado — conexão B1↔B10 (BLOCO_08.010).
- **Exposição a interferon/citocina exógena** com sintomas de novo — prova-de-conceito causal humana (BLOCO_06.003).

---

#### Tabela de classificação final

| Classificação | Critério A (biomarcadores) | Critério B (fenótipo, mínimo) | Critério C (contexto) | Interpretação |
|---|---|---|---|---|
| **Compatibilidade alta** com mecanismo inflamatório | ≥2 marcadores de A alterados | ≥3 de 6 itens | ≥1 presente | O quadro é bem explicado por B1; priorizar leitura mecanística inflamatória (sempre integrada aos demais Bx) |
| **Compatibilidade indeterminada** | 1 marcador alterado **ou** exame indisponível | 2 itens | variável | Dados insuficientes; considerar coleta do painel (C-LAB) antes de fechar |
| **Compatibilidade baixa** | nenhum marcador alterado | ≤1 item | ausente | B1 pouco provável como eixo central; ponderar outros mecanismos B2–B16 |

> **Precedência e integração:** esta classificação é **hipótese mecanística de apoio**, nunca critério diagnóstico autônomo. Na plataforma ela deve ser sempre integrada à avaliação dos demais mecanismos B1–B16 potencialmente concorrentes ou coexistentes no mesmo paciente (Filosofia do Projeto). Ajustes por população: em **idosos**, marcadores inflamatórios basais elevam-se por *inflammaging* senescente (distinto do fenômeno patológico central) — exige interpretação ajustada por idade (quantitativo no C-LAB); em **mulheres**, flutuações hormonais podem modular PCR/IL-6 basais (modulação ainda não quantificada com precisão); em **comorbidade autoimune ativa**, marcadores sistêmicos perdem especificidade para o mecanismo de humor.

---

*Osimo_2020[MA] | Howren_2009[MA] | Quimio82_2017[MA] | Dowlati_2010[MA] | RCT_infliximab[EC] | Bull_2009[EC] | Klengel_2013[EC] | Reward_2022[EC] | RewardTrauma_2020[EC] | IL6resol_2015[EC] | Treg_2024[EC]*

---
## BLOCO_12 — CENÁRIOS CLÍNICOS ILUSTRATIVOS

> Aplicável em modo **ilustrativo**: o BLOCO_11.4 formalizou os critérios de estratificação, então os perfis abaixo são exemplos de raciocínio mecanístico — **não** estratégias terapêuticas. Não há nenhuma menção a intervenção, fármaco, suplemento, dose, protocolo ou conduta clínica (a menção ao RCT do infliximabe permanece apenas como prova de estratificação, no BLOCO_05/06, nunca como recomendação).

---

### 12.1 — Depressão com padrão atípico e inflamação de baixo grau

- **Perfil clínico:** humor deprimido com reatividade preservada, hiperfagia e hipersonia, sensação de peso nos membros, fadiga desproporcional, sensibilidade a rejeição interpessoal.
- **Substrato mecanístico:** ativação sustentada de NF-κB/NLRP3 (nós centrais do BLOCO_07) sustentando elevação de IL-6/TNF-α; possível contribuição de disbiose/permeabilidade intestinal (B7, BLOCO_08.005) e de adiposidade/obesidade como fonte adicional de citocinas (BLOCO_01.004).
- **Biomarcadores esperados:** PCR e IL-6 consistentemente elevados; TNF-α frequentemente elevado; razão KYN/TRP com elevação leve a moderada.
- **Raciocínio de estratificação:** tende a **Compatibilidade alta** no BLOCO_11.4 (Critério A com ≥2 marcadores, Critério B com itens atípicos/fadiga, Critério C com contexto metabólico presente).
- **Nível de evidência do perfil:** associação meta-analítica replicada (subtipo inflamatório e fenótipo atípico) — força **média**, em amostra humana observacional; não é diagnóstico.

---

*Osimo_2020[MA] | Quimio82_2017[MA] | Dowlati_2010[MA] | Obesidade_2025[EC]*

### 12.2 — Depressão resistente ao tratamento com ativação imune sustentada

- **Perfil clínico:** múltiplas tentativas de tratamento monoaminérgico sem resposta adequada, curso crônico, sintomas somáticos proeminentes.
- **Substrato mecanístico:** divergência de alvo mecanístico (BLOCO_06.001) — a citocina suprime BDNF-CREB e desvia triptofano pela IDO1 para QUIN (glutamato/NMDA, BLOCO_02.010), independentemente da recaptação de serotonina; possível sobreposição com o loop de amplificação ROS–NLRP3–disfunção mitocondrial (BLOCO_08.003).
- **Biomarcadores esperados:** TNF-α e sTNFR2 tendem a estar mais elevados que na depressão responsiva; PCR na faixa associada a maior probabilidade de não-resposta; o painel combinado (não um marcador isolado) é o que discrimina.
- **Raciocínio de estratificação:** **Compatibilidade alta**, com peso do item "resistência a ≥2 linhas monoaminérgicas" (Critério B) e de marcadores de estabilidade (sTNFR2) no Critério A.
- **Nível de evidência do perfil:** marcadores predizem não-resposta a antidepressivo e a intervenção anti-TNF beneficia **somente** o subgrupo com marcador basal alto (prova de estratificação, não de tratamento) — força **média**.

---

*RCT_infliximab[EC] | IL6resol_2015[EC] | LCL_biom_2021[EC] | Steiner_2011_QUIN[EC]*

### 12.3 — Fenótipo pós-traumático com priming neuroinflamatório

- **Perfil clínico:** sintomas depressivos/ansiosos de início relacionado a trauma precoce ou adversidade significativa, com hipervigilância e reatividade emocional desproporcional a estressores atuais leves.
- **Substrato mecanístico:** loop trauma–FKBP5–resistência glicocorticoide (BLOCO_08.012; desmetilação FKBP5 dependente de trauma — Klengel 2013; efeito intergeracional — Holocausto 2016) fechando o circuito B1→B12→B2→B1; priming microglial de longo prazo (BLOCO_01.003; inflamação neonatal/mTBI) estabelecido precocemente, latente até novo estressor precipitante.
- **Biomarcadores esperados:** IL-6/TNF/PCR possivelmente elevados de forma **desproporcional à gravidade do estressor atual** (reatividade aumentada, não só nível basal); alelo de risco FKBP5 quando genotipado (`exame_snps_inflamatorios` como aproximação do contexto genético).
- **Raciocínio de estratificação:** **Compatibilidade alta** quando o Critério C (histórico de trauma) está presente, mesmo com Critério A parcial — reflete a natureza latente/reativa deste subtipo, distinta dos dois anteriores.
- **Nível de evidência do perfil:** genética humana gene×ambiente muito estabelecida para FKBP5; priming causal é predominantemente animal/[EXT] — força **média** para o perfil, **alta** para o componente FKBP5.

---

*Klengel_2013[EC] | Holocausto_2016[EC] | Bull_2009[EC] | Stress_Epi_2019[MA]*

### 12.4 — TEPT/ansiedade traumática com o subtipo neuroimune suprimido

- **Perfil clínico:** sintomas de TEPT/ansiedade crônica pós-trauma (hipervigilância, evitação, reatividade de sobressalto) que se acompanham de queixas somáticas atenuadas e **falta de elevação** dos marcadores inflamatórios periféricos, ou até tendência ao esgotamento neuroendócrino (conecta com o hipocortisolismo da B2).
- **Substrato mecanístico:** não é "ausência de neuroinflamação", mas um **estado neuroimune distinto** — dado combinado de PET de TSPO e tecido pós-morte aponta supressão neuroimune em subgrupo de TEPT (Bhatt et al., 2020); coexiste reatividade de circuitos de medo/extinção (amígdala, extinção prejudicada; minociclina atenua retenção de medo em humano — Xia 2024).
- **Biomarcadores esperados:** marcadores periféricos podem estar **normais ou baixos** (não esperar PCR/IL-6 elevados); TSPO-PET reduzido quando disponível (atenção ao confundidor genótipo rs6971); possível achatamento da reatividade cortisol/ansiedade.
- **Raciocínio de estratificação:** é um **contra-arquétipo** dos três anteriores — alerta contra tratar "inflamação alta" como universal. No BLOCO_11.4 este perfil tende a **Compatibilidade indeterminada/baixa** pelo Critério A, embora o Critério B/C (hipervigilância, trauma) esteja presente; sinaliza a necessidade de integrar B2 (HPA/TEPT) e B12 (trauma).
- **Nível de evidência do perfil:** PET+pós-morte humano para a supressão neuroimune (força **média**, amostra pequena/heterogênea); ensaio RCT humano para minociclina/memória de medo (força **média**).

---

*PTSD_supressao_2020[EC] | Minociclina_medo_2024[EC] | PTSD_marc_2015[MA] | TSPO_estresse_2022[OB]*

> **Nota de fechamento:** estes três cenários são **arquétipos didáticos** do mesmo eixo mecanístico (NF-κB/NLRP3), não categorias mutuamente exclusivas nem rótulos diagnósticos. Na prática clínica eles se sobrepõem e devem ser lidos em conjunto com os demais mecanismos B2–B16. Qualquer decisão sobre exames, intervenções ou conduta pertence às bibliotecas operacionais (Biomarcadores/Exames, Intervenções, Cenários) e ao julgamento do profissional.

---
---

## TABELA DE EVIDÊNCIAS

Agrupada por afirmação/tipo de desenho. `forca_evidencia_afirmacao` reflete o corpo de evidência por afirmação (não o rótulo do desenho).

| Tipo de estudo | Principais resultados | Tamanho de efeito | Limitações | forca_evidencia_afirmacao (alto\|medio\|baixo) |
|---|---|---|---|---|
| Meta-análise | Citocinas elevadas na TDM: IL-6, TNF-α, PCR (Dowlati; Howren; Goldsmith; Osimo; 82 estudos); heterogeneidade concentrada em subgrupo | Diferenças de média positivas consistentes (IL-6/TNF/PCR); ~27% com PCR>3 (OR~1,46) | Medição periférica, confundidores (obesidade, sono, medicação), publicação | alto |
| Meta-análise | Diferenças sexuais na ligação inflamação-depressão | Efeito mais consistente em mulheres em parte dos marcadores | Heterogeneidade, poucos estudos estratificados | medio |
| Meta-análise [AT 2026-09-08] | TSPO-PET elevado apenas de forma modesta/heterogênea (~18%) e ausente em depressão leve–moderada; TRYCATs alterados em subtipos (melancolia/psicótico/suicida); inflamação já presente no 1º episódio drug-naïve (incl. adolescentes); queda de citocinas acompanhando resposta antidepressiva | Efeito pequeno-moderado, heterogêneo; sem especificidade celular | Imagem indireta, confundidor farmacocinético do radiotraçador, severidade como moderador | medio |
| Evidência negativa/calibradora [AT 2026-09-08] | Micróglia pós-morte homeostática/suprimida (não pró-inflamatória); TSPO×PCR sem correlação; equivalência TSPO=micróglia ativada negada em humano; central parcialmente independente do periférico | N/A (função de limitar claims) | Amostras pós-morte pequenas; estágio da doença/tratamento confunde | alto como CALIBRAÇÃO (impede overclaim) |
| RCT | Infliximabe anti-TNF em depressão resistente | Negativo na amostra total; benefício restrito ao subgrupo com hs-CRP/TNF/sTNFR2 basais altos | N=60, resultado primário negativo, não é indicação clínica | medio (prova de estratificação) |
| Estudo observacional humano | TSPO-PET elevado (Setiawan; Holmes); QUIN pós-morte (Steiner); KYN/TRP e substância branca; conectividade córtico-estriatal e anedonia; FKBP5/trauma (Klengel); Bull IL-6×IFN | Associações replicadas em amostras independentes | Transversal/pós-morte (suicídio), TSPO exige genotipagem rs6971, correlação ≠ causalidade | medio |
| Modelo animal | Manipulação causal: NLRP3/TLR4/NF-κB/KO, IDO1, GSDMD/BHE, claudina-5 por estresse social, poda C1q/C3, priming neonatal, MAMs/P2X7 | Efeitos grandes e reversíveis por antagonista/deleção | [APENAS PRÉ-CLÍNICO] translacionalidade indireta; cepa/sexo; janela | medio (mecanismo) / alto para a via em si |
| Estudo in vitro/célula | Repressão gênica pelo GR, S100B-RAGE/COX-2, CCL2/transcitose, IFN-γ/STAT1/NLRP3, IL-10/STAT3 | Mecanismo molecular direto | Sistema reduzido, sem circuito/comportamento | medio |

---
## CONTROVÉRSIAS E LACUNAS

**Questões de causalidade não resolvidas**
- Inflamação→depressão vs. depressão→inflamação: a maior evidência humana é transversal (associação). Os argumentos a favor de causalidade são o paradigma IFN-α (citocina exógena precipita sintomas), o desafio com endotoxina e a interação gene×inflamação (Bull). Contra: marcadores periféricos não provam direção, e o estresse da doença pode elevar citocinas. Resolveria com: ensaios anti-inflamatórios estratificados por biomarcador e estudos longitudinais de coorte com medidas repetidas.
- Subgrupo vs. contínuo: Osimo (variabilidade) sugere um subgrupo, mas a elevação pode ser um gradiente contínuo. Resolveria com modelagem de mistura (mixture models) em coortes grandes.

**Heterogeneidade de estudos**
- Medição de "IL-6 total" vs. trans-sinalização (sIL-6R/gp130); "TNF total" vs. TNFR1/TNFR2; PCR como marcador hepático inespecífico. Resultados conflitantes derivam de não separar isoformas/receptores e de diferentes kits/momentos.
- TSPO-PET: o polimorfismo rs6971 (ligante baixa/alta afinidade) e a expressão em astrócitos além de micróglia tornam "TSPO = micróglia ativada" impreciso entre estudos não genotipados. **[AT 2026-09-08]** Somam-se evidência negativa (ausência de elevação em depressão leve–moderada; aumento modesto ~18% sem especificidade celular), a negação da equivalência roedor→humano (em humano, TSPO não marca especificamente micróglia ativada) e um confundidor farmacocinético novo (inflamação periférica reduz influxo do radiotraçador).
- **Micróglia humana pós-morte sem fenótipo pró-inflamatório [AT 2026-09-08]:** single-cell no TDM mostra perfil homeostático/suprimido, e a assinatura dominante recai sobre oligodendrócitos. Tensão aberta com o PET positivo: ou o PET capta outra célula (astrócito/fronteira/endotélio), ou o pós-morte retrata estágio terminal/tratado da doença.
- **Central ≠ periférico, agora ancorado [AT 2026-09-08]:** meta-análise tri-compartimental (líquor/PET/pós-morte) confirma dissociação parcial — marcador de sangue elevado não autoriza, sozinho, o claim de "neuroinflamação cerebral".
- **NLRP3 ≠ piroptose automática [AT 2026-09-08]:** saídas inflamatórias independentes de GSDMD estão documentadas — os claims desta biblioteca mantêm priming/ativação como etapas dissociáveis e a morte lítica como desfecho condicional.

**Limitações dos modelos animais**
- [APENAS PRÉ-CLÍNICO] Cascata NLRP3/GSDMD/poda e priming demonstrados por manipulação em camundongo/ratos/célula; a tradução para depressão humana é por analogia [EXT]. Comportamento "tipo-depressivo" animal (suspensão por cauda, preferência por sacarose) não equivale ao quadro humano.

**Subgrupos não identificados**
- TRD (resistente), depressão perinatal, TEPT pró-inflamatório, depressão geriátrica/senescente, e diferenças por sexo estão listados como candidatos (BLOCO_11) sem formalização; cada um pode ter eixo imune distinto.

**Vieses de publicação identificados**
- Viés de publicação positivo em estudos de citocinas; revisões de composto (polifenóis, fitoterápicos) nos resultados de busca tendem a relatar efeitos benéficos. As meta-análises (Osimo, Howren) atenuam parcialmente, mas conflito de interesse e pequenos estudos persistem.

**Lacunas de busca (registradas no inventário negativo)**
- RLRs (RIG-I/MDA5) diretos no SNC; miR-155/SOCS1 comportamental; oligodendrócitos/NG2 sob TNF/IFN-γ em CPF; SERT/p38 MAPK; EAAT2/GLT-1; zinco/NLRP3 e magnésio/NF-κB; CB2/FAAH/MAGL; LBP/endotoxina e resolvina D1 plasmáticas em TDM; estimulação de CRH por PGE2 — todos  sem estudo dedicado na literatura consultada (propostos na literatura, sem evidência direta consistente).

---
## ELEMENTOS MOLECULARES CRÍTICOS

Molécula/Gene/Receptor/Proteína: NLRP3
UniProt ID:

Q96P20
Gene (HGNC):

NLRP3
HMDB ID:

null
Função fisiológica normal: sensor do inflamassoma; monta complexo ASC/caspase-1 após priming (NF-κB) + sinal 2
Alteração em ansiedade: ↑ ativação (emergente)
Alteração em depressão: ↑ ativação em subgrupo inflamado (marcadores/genética)
Células/estruturas onde atua: micróglia, macrófagos, monócitos, astrócitos
Vias moleculares associadas: NF-κB (priming); caspase-1/GSDMD (piroptose); cGAS-STING (mtDNA)
Impacto sobre B3 (Neuroplasticidade): indireto via IL-1β/IL-18 que suprimem BDNF/CREB e promovem poda
Força da evidência da afirmação: alto (via em si, animal/célula) / medio (depressão humana)
Referência: (Swanson, 2019)[OB]; (Molina-López et al., 2024)[EC]

Molécula/Gene/Receptor/Proteína: NF-κB (subunidade RELA/p65)
UniProt ID:

Q04206
Gene (HGNC):

RELA
HMDB ID:

null
Função fisiológica normal: fator de transcrição pró-inflamatório; saída comum de TLR/TNFR/IL-1R
Alteração em ansiedade: ↑ atividade transcricional
Alteração em depressão: ↑ no subgrupo; desinibido por resistência a glicocorticoide
Células/estruturas onde atua: todas as células imunes e neurais
Vias moleculares associadas: TLR4/MyD88/IRAK/TRAF6/IKK; NLRP3 priming; COX-2/iNOS
Impacto sobre B3: dirige transcrição de IL1B/IL6/TNF que deprimem plasticidade
Força da evidência: alto (mecanismo) / medio (humano)
Referência: (Wang et al., 2024)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]; (Sacta et al., 2018)[ML; célula/camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]

Molécula/Gene/Receptor/Proteína: IL-6
UniProt ID:

P05231
Gene (HGNC):

IL6
HMDB ID:

null
Função fisiológica normal: citocina pleiotrópica; resposta de fase aguda, reparo
Alteração em ansiedade: ↑ periférica
Alteração em depressão: ↑ replicada em meta-análises; prediz não-resposta e anedonia
Células: monócitos, macrófagos, micróglia, astrócitos, adipócitos
Vias associadas: IL-6R clássico vs. trans-sinalização sIL-6R/gp130/JAK-STAT3
Impacto sobre B3: suprime BDNF; trans-sinalização também reparativa (dual)
Força da evidência: alto (humano, marcador)
Referência: (Dowlati, 2010)[MA]; (Osimo, 2020)[MA]; (Willis et al., 2020)[ML]

Molécula/Gene/Receptor/Proteína: TNF-α / TNFR1 / TNFR2
UniProt ID:

P01375 / P19438 / P20333
Gene (HGNC):

TNF / TNFRSF1A / TNFRSF1B
HMDB ID:

null
Função: citocina pró-inflamatória; TNFR1 apoptótico/pró-inflamatório, TNFR2 homeostático/neuroprotetor
Alteração em depressão: ↑ TNF e sTNFR2 no subgrupo
Células: micróglia, macrófagos, linfócitos
Vias: NF-κB; necroptose RIPK1; scaling sináptico glial (fisiológico)
Impacto sobre B3: modula força de AMPA/scaling; em excesso deprime LTP
Força da evidência: alto (meta/RCT de estratificação)
Referência: (Goldsmith, 2016)[MA]; (Klengel et al., 2013)[EC]; (Stellwagen et al., 2006)[ML]

Molécula/Gene/Receptor/Proteína: IDO1 (indoleamina 2,3-dioxigenase 1)
UniProt ID:

P14902
Gene (HGNC):

IDO1
HMDB ID:

null
Função: converte triptofano em quinurenina; induzida por IFN-γ/citocinas
Alteração em depressão: ↑ atividade (razão KYN/TRP desviada)
Células: monócitos, micróglia, astrócitos
Vias: JAK-STAT/IFN-γ; quinurenina (KYNA astrocitário vs. QUIN microglial)
Impacto sobre B3: reduz triptofano para 5-HT; QUIN excitatório/ROS
Força da evidência: alto (animal causal) / medio (humano marcador)
Referência: (Bull et al., 2009)[ML]; (Salminen et al., 2022)[OB]

Molécula/Gene/Receptor/Proteína: TSPO (proteína translocadora 18 kDa)
UniProt ID:

P30536
Gene (HGNC):

TSPO
HMDB ID:

null
Função: transporte de colesterol/esteroides na mitocôndria; marcador PET de ativação glial
Alteração em depressão: ↑ densidade em córtex cingulado/ínsula (subgrupo)
Células: micróglia e astrócitos (não exclusivo micróglia)
Vias: esteroidogênese; resposta glial
Impacto sobre B3: marcador de neuroinflamação central, não agente direto
Força da evidência: medio (ressalva rs6971)
Referência: (Setiawan, 2015)[EC]; (Holmes, 2018)[EC]

Molécula/Gene/Receptor/Proteína: FKBP5
UniProt ID:

Q13451
Gene (HGNC):

FKBP5
HMDB ID:

null
Função: co-chaperona que modula sensibilidade do receptor de glicocorticoide (GR)
Alteração: desmetilação dependente de trauma × alelo de risco → resistência a GR → NF-κB desinibido
Células: neurônios, células imunes
Vias: eixo HPA/GR; NF-κB (loop B1↔B2/B12)
Impacto sobre B3: indireto via cortisol/citocinas
Força da evidência: alto (humano, gene×ambiente)
Referência: (Klengel, 2013)[EC]; (Yehuda et al., 2016)[EC]

*Não incluídos: medicamentos, suplementos ou agentes terapêuticos (pertencem às bibliotecas de Intervenções/Suplementos).*

---
## MARCADORES RESUMIDOS (para RAG/ontologia)

> Estrutura computável completa (key_molecules, key_pathways, biomarkers, connection_strength B1–B16, loops, semantic_fields) está em `Evidencias/Bibliografia/_manifesto_biblioteca.json`.

> Os identificadores UniProt/HGNC seguem os símbolos oficiais; a conferência campo-a-campo está registrada no Módulo 9.


---


---


---


---

## APÊNDICE DE CORPUS (ÍNDICE DE REFERÊNCIAS AUDITADAS — B1)
> Entradas do Módulo 09 (G1 eutils) do corpus de auditoria; rótulos canônicos para rastreabilidade.
*ZDILAR_2000[MA] | CAPURON_2002[EC] | DANTZER_2001[ML] | CAPURON_2002b[EC] | FEKETE_2004[ML] | HAN_2005[ML] | STELLWAGEN_2006[ML] | ZEOLD_2006[ML] | DANTZER_2006[ML] | BIANCHI_2007[ML] | HAFIZI_2005[MA] | OCONNOR_2009[ML] | GE_2008[ML] | BULL_2009[MA] | YANG_2008[ML] | GOSHEN_2009[ML] | TOBINICK_2009[MA] | ARMULIK_2010[ML] | BIANCHI_2011[ML] | SUBLETTE_2011[MA] | PAOLICELLI_2011[ML] | STEINER_2011[MA] | GARATE_2011[ML] | BOATO_2011[ML] | SCHAFER_2012[ML]*
*DONATO_2013[ML] | RAISON_2013[MA] | KLENGEL_2013[MA] | PERRY_2013[ML] | CHIU_2013[ML] | SERHAN_2014[ML] | ZHENG_2014[ML] | NORDEN_2015[ML] | SETIAWAN_2015[MA] | VIRTANEN_2015[MA] | BARRIENTOS_2015[ML] | HARDEN_2015[ML] | YEHUDA_2016[MA] | FELGER_2016[EC] | DUMAN_2016[MA] | GULEN_2016[MA] | ZENARO_2017[ML] | LI_2017[ML] | KOHLER_2017[MA] | PICCA_2017[MA] | PINTOSANCHEZ_2017[MA] | SOUZA_2017[ML] | KRASEMANN_2017[ML] | HOLMES_2018[MA] | FENG_2017[ML]*
*MENARD_2017[ML] | WANG_2018[MA] | SACTA_2018[ML] | BONAZ_2018[ML] | BLOMQVIST_2018[ML] | SERHAN_2018[ML] | RIZZO_2018[ML] | YUN_2018[ML] | HERMAN_2018[ML] | SHIRAKAWA_2018[ML] | BANG_2018[ML] | ARORA_2019[MA] | ZHAO_2019[ML] | PARK_2019[MA] | SWANSON_2019[ML] | NASH_2019[ML] | ZHOU_2020[ML] | LIU_2020[MA] | OSIMO_2020[MA] | BELGE_2020[MA] | YANG_2020[ML] | WILLIS_2020[ML] | MEHTA_2020[MA] | CHUKAEW_2021[MA] | ANNETT_2020[ML]*
*JANG_2020[ML] | XU_2020[ML] | RUTSCH_2020[ML] | BAMBOUSKOVA_2021[ML] | SAXTON_2021[ML] | DA_2021[ML] | LOPES_2021[ML] | CHEN_2021[ML] | TAFT_2021[MA] | XU_2021[ML] | BASILICO_2022[ML] | YAN_2021[ML] | COMAI_2022[MA] | SALMINEN_2022[ML] | MARIANI_2022[ML] | LIU_2022[ML] | RAJESH_2022[ML] | SUGIMOTO_2022[ML] | BEKHBAT_2022[MA] | BRANN_2022[ML] | YANG_2023[ML] | ZHU_2023[ML] | FIORE_2023[ML] | ZHANG_2023[ML] | WEI_2023[ML]*
*CHEN_2024[MA] | HUANG_2023[ML] | WILEY_2024[MA] | HUANG_2023b[ML] | CAMERON_2024[ML] | YAMANISHI_2023[ML] | MENENDEZ_2024[ML] | MOLINALOPEZ_2024[MA] | FU_2024[ML] | ALMEIDA_2020[ML] | HAO_2024[ML] | YANG_2024[ML] | CHO_2024[ML] | CHEN_2024b[ML] | WANG_2024[ML] | WEI_2024[ML] | CHEN_2024c[ML] | ZHANG_2024[ML] | XU_2024[ML] | HE_2024[ML] | MALAU_2024[MA] | YANG_2024b[MA] | SHEN_2025[ML] | ZHAO_2025[ML] | KEENAN_2025[MA]*
*ZHANG_2025[ML] | KIM_2025[ML] | ZHANG_2025b[ML] | LI_2025[ML] | LANG_2025[ML] | ZHANG_2026[ML] | HUI_2025[ML] | GARCIADOMINGUEZ_2025[ML] | ELENI_2025[ML] | RAFFAELE_2025[ML] | CHEN_2025[ML] | ZHU_2026[ML] | PENG_2025[ML] | MONSALVE_2025[MA] | QIU_2026[ML] | YANG_2026[ML] | XU_2026[ML] | LAPCHAK_1993[ML] | LAWRENCE_2023[MA] | HUANG_2024[ML] | FRANKLIN_2018[ML] | ZHOU_2025[ML] | ZHOU_2024[ML] | LI_2025b[ML] | HAN_2023[ML]*
*MEHTA_2020b[MA] | CHENG_2021[ML] | TANNAHILL_2013[ML] | LIU_2023[ML] | ENGSKOGVLACHOS_2025[ML] | VIZUETE_2022[ML] | ZEB_2022[ML] | ABUDARA_2015[ML] | KARPUK_2011[ML] | LEI_2023[MA] | WEN_2024[ML] | LYU_2025[ML] | LEE_2025[ML] | KIM_2017[ML] | HUANG_2024b[ML] | GAO_2023[ML] | KOMLEVA_2021[ML] | BHATT_2020[MA] | XIA_2024[EC] | BI_2016[ML] | DOWLATI_2010[MA] | HOWREN_2009[MA] | GOLDSMITH_2016[MA] | JARKAS_2024[MA] | WIEDOCHA_2018[MA]*
*POLETTI_2024[MA] | NOAH_2021[MA] | RENNA_2018[MA] | COSTELLO_2019[MA] | COSCO_2019[MA] | QUAGLIATO_2018[MA] | PASSOS_2015[MA] | RUPPRECHT_2022[MA] | PARSONS_2021[MA] | HOWE_2022[MA] | KIM_2018[MA] | WITTENBERG_2020[EC] | SU_2018[EC]*
*HANNESTAD_2013[EC] | ZHANG_2015[ML] | PARROTT_2016[ML] | KAUFMANN_2017[OB] | WANG_2018b[MA] | KOHLER_2018[MA] | DACUNTO_2019[MA] | ENACHE_2019[MA] | WANG_2019[MA] | MARTINHERNANDEZ_2019[ML] | NAGY_2020[EC] | HAROON_2020[EC] | ANDERSON_2020[EC] | ATTWELLS_2020[EC] | LIU_2020b[MA] | BOTTCHER_2020[EC] | SAVITZ_2020[OB] | LI_2021[ML] | WANG_2021[ML] | MACGIOLLABHUI_2021[MA] | NUTMA_2021[OB] | SCHUBERT_2021[EC] | ALMULLA_2022[MA] | KOUBA_2022[OB] | LIU_2022b[ML]*
*EGGERSTORFER_2022[MA] | GUILARTE_2022[OB] | GARCIAGARCIA_2022[MA] | ELGELLAIE_2023[EC] | NUTMA_2023[OB] | XIA_2023[OB] | BADAWY_2023[OB] | HAN_2023b[OB] | LIU_2023b[MA] | STONE_2024[OB] | GAVRIL_2024[OB] | JADHAV_2025[MA] | GEDEK_2025[MA] | WIJESINGHE_2025[EC] | XU_2025[OB] | XIE_2025[MA] | BERTOLLO_2025[OB] | LI_2026[EC] | MCCOLGAN_2026[MA] | HUA_2026[ML] | OREGAN_2026[OB] | MURATA_2026[OB] | BARZON_2026[EC] | BARZON_2026b[EC]*

---

## METADADOS CANÔNICOS (Contrato de Geração — P12 / R06 / P17)

**natureza_sistema (P12 — hard_fail):**
```json
{
  "natureza_sistema": {
    "tipo": "suporte_decisao_clinica",
    "nao_substitui_julgamento_profissional": true,
    "nao_realiza_diagnostico": true,
    "decisao_final_profissional": true
  }
}
```
> Biblioteca de **mecanismo** (P20): descreve o papel biológico da via; **não** diagnostica,
> **não** prescreve dose/protocolo nem substitui a avaliação clínica.

**semantic_layer (R06):**
- **clinical_summary (3 frases):** Microglia, citocinas e vias inflamatórias modulam o humor. | Baseada na resposta imune inata e na sinalização neuroinflamatória. | Use para interpretar marcadores inflamatórios e adjuvantes — sem diagnosticar nem prescrever.
- **rag_context_hint:** Recuperar quando: houver menção a microglia, citocinas (IL-6/TNF/IDO-quinurenina), anti-inflamatórios ou vacinação; para contrapor associação humana a prova animal
- **clinical_domains (máx 4):** decisao_terapeutica · seguranca_clinica · triagem_clinica · monitoramento
- **semantic_keywords (8–12):** microglia, citocinas, IL-6, TNF, IDO, quinurenina, neuroinflamação, NAC, cetamina inflamatória
- **related_entities (IDs exatos):** mecanismo_B2_eixo_hpa_cortisol, mecanismo_B3_neuroplasticidade, mecanismo_B4_deficiencias_monoaminas, mecanismo_B6_estresse_oxidativo, mecanismo_B7_eixo_intestino_cerebro, mecanismo_B9_disfuncao_mitocondrial
- **embedding_priority:** alta

**corte_literatura (R06):** busca ativa E-utilities/PubMed — corte 2026-05.

**R04 — sinalizador de extrapolação:** evidência animal/in vitro (germ-free, modelos, cultura)
é marcada `[ML]/[APENAS PRÉ-CLÍNICO]` e **[EXTRAPOLAÇÃO POR ANALOGIA: contexto-fonte animal/in vitro — validação humana direta pendente]`;
não sustenta recomendação (R04: sem evidência humana direta → não entra como recomendação).

**P17 — posição na arquitetura de 16 mecanismos:** ID `mecanismo_B1_neuroinflamacao` (Neuroinflamação).
- **P16 (anti-duplicação):** a neurogênese (proliferação de progenitores, migração, diferenciação,
  integração sináptica, zona subgranular/giro denteado) é escopo **exclusivo de
  `mecanismo_B16_neurogenese`**, subordinada a `mecanismo_B3_neuroplasticidade`. Nesta biblioteca
  ela aparece apenas como efeito/modulação indireta em 1–2 frases, sem replicar o conteúdo.
