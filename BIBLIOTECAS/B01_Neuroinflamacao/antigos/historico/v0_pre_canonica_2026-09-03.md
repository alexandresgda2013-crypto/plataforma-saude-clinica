# B1 — NEUROINFLAMAÇÃO
## Biblioteca de Conhecimento Científico — Clinical Dominion
### Versão PRÉ-CANÔNICA · Rodada 2 (Prompt PMID v4.2 + GPM v3)

**Mecanismo:** mecanismo_B1_neuroinflamacao · **Data:** 2026-09-03
**Fonte primária:** GPM_B1_NEUROINFLAMACAO_v3 · 7ª Lista Canônica (trilha mecanística)
**G1 (ferramenta):** NCBI eutils (esearch+efetch) · 145 referências com PMID real e abstract baixado.
**Status:** PRÉ-CANÔNICA — toda referência `CANDIDATO`, `verification_status=pending`, `g3_verificado_por=""`. G2/G3 são da auditoria, não desta geração.

**Módulo 9 (arquivos separados, mesma Rodada 2):**
- N1 `/Evidencias/Bibliografia/01_pmids.json` (145 refs, schema 09.1)
- N1 `/Evidencias/Bibliografia/02_meta_analises.json` (6 metas, schema 09.2)
- N1 `/Evidencias/Bibliografia/03_ensaios_clinicos.md` (1 RCT, template 09.3)
- N2 `/Evidencias/Vinculos/vinculos_referencia_afirmacao.json` (178 vínculos, trecho_ancora literal por sentença — E3)

> Espécie declarada em cada vínculo (`especie_mesh`,`evid_role`); extrapolação marcada (`extrapolacao_por_analogia`, [ML]/[OB]/[EXT]). TOC fora do escopo central.

---

## BLOCO_00 — IDENTIDADE E ASSINATURA SEMÂNTICA

```
ID canônico:          mecanismo_B1_neuroinflamacao
Nome canônico:        Neuroinflamação
Categoria funcional:  imunológico
Cronicidade:          crônico (com fases agudas de precipitação)
Reversibilidade:      moderada
Janela temporal:      horas (ativação aguda) a anos (cronificação/priming)
Status de validação:  estabelecido (heterogêneo por sub-via e por subgrupo de pacientes)
```

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

Em condições saudáveis, a interação sistema imune–cérebro é um programa **adaptativo e autolimitado**, não uma falha. Diante de patógeno, lesão tecidual ou estressor agudo, células mieloides (monócitos, macrófagos, micróglia) reconhecem motivos moleculares conservados (PAMPs, ex. LPS bacteriano; DAMPs de células lesadas) por receptores de reconhecimento padrão — TLR2/4 e o inflamassoma NLRP3 — e disparam transcrição NF-κB de citocinas pró-inflamatórias (IL-1β, IL-6, TNF-α) seguida de maturação por caspase-1 (Swanson et al., 2019)[OB; revisão, humano+animal]. Essa ativação aguda é programada para **resolver ativamente**: mediadores lipídicos pró-resolutivos especializados (SPMs — resolvinas D/E, protectinas, maresinas, lipoxina A4), derivados do metabolismo de ômega-3/6, sinalizam a parada do recrutamento neutrofílico, o clearence de células apoptóticas por macrófagos e o retorno da micróglia ao estado ramificado homeostático (Serhan, 2014)[OB; revisão fisiológica, humano+animal; Serhan & Levy, 2018][OB]. A micróglia homeostática exerce vigilância contínua com processos móveis, sem produção sustentada de citocinas (revisão de biologia microglial; Perry & Teeling, 2013)[OB; revisão, humano+camundongo].

O que distingue ativação **adaptativa** de **patológica** não é a presença de citocinas — elas são fisiológicas — e sim três parâmetros: **duração** (horas/dias vs. semanas/anos), **magnitude** (pico transitório vs. elevação de baixo grau contínua, "low-grade inflammation"/inflammaging) e, sobretudo, **capacidade de resolução ativa** (Barrientos et al., 2015)[OB; revisão, camundongo+humano]. Quando o programa de resolução falha — por SPMs insuficientes, senescência celular ("SASP" secretando citocinas em baixo grau contínuo) ou reprogramação metabólica da micróglia (glicólise/mtROS sustentando o fenótipo pró-inflamatório) — a resposta deixa de ser autolimitada. O estado resultante é de **priming microglial**: a micróglia permanece "sensibilizada", com limiar rebaixado, e responde de forma amplificada e prolongada a um segundo desafio (Norden et al., 2015)[OB; revisão, humano]. Esse limiar adaptação↔patologia é o eixo conceitual de todo o mecanismo B1: a neuroinflamação clínica não é "inflamação no cérebro" como evento pontual, e sim a **falha do desligamento** de um programa que, em sua forma aguda, é protetor.

### 1.2 — Sickness behavior: o modelo de neuroinflamação aguda adaptativa (BLOCO01.002)

O melhor modelo de neuroinflamação aguda fisiológica é o **sickness behavior** (comportamento de adoecimento): após administração de LPS ou indução por citocinas, o organismo exibe um conjunto coordenado e estereotipado — retraimento social, anedonia transitória, fadiga/hipersonia, redução de exploração e apetite, hiperalgesia leve — que redireciona energia para combate ao patógeno e reparo (Dantzer et al., 2001)[EC; revisão mecanística, camundongo+humano]. Cronologicamente, o quadro inicia-se em horas (pico de citocinas 2–6 h pós-LPS), atinge o máximo comportamental em 6–24 h e **resolve espontaneamente em 24–72 h** com o término do estímulo e a entrada dos programas de resolução — inclusive febre e sickness foram reinterpretados como respostas amigas ou adversas a depender do contexto temporal (Harden et al., 2015)[OB; revisão, camundongo+humano]. A via molecular está descrita: citocinas periféricas sinalizam ao cérebro por vias neurais (nervo vago), humorais (transporte através da barreira e em órgãos circunventriculares) e celulares (monócitos trafegando), e ativam IL-1β central e IDO — a transição de sickness para comportamento tipo-depressivo persistente é mediada pela via da quinurenina induzida por citocinas (Dantzer, 2006)[OB; revisão, camundongo+humano].

A distinção crucial para a clínica: **sickness é agudo e autolimitado; depressão associada a inflamação é crônica e não resolve**. No animal, o LPS induz comportamento tipo-depressivo transitório que depende de IDO1 (O'Connor et al., 2009)[ML; camundongo]; quando o estímulo inflamatório persiste ou se repete (estresse crônico, envelhecimento, infecção latente), a resposta não retorna à linha de base — é a ponte para o item 1.3.

### 1.3 — Cronificação: priming microglial e memória imune inata (BLOCO01.003)

A passagem do estado agudo resolutivo para a neuroinflamação crônica tem um correlato molecular: o **priming (sensibilização) microglial**. Após um primeiro insulto — infecção sistêmica, lesão, estresse crônico, envelhecimento ou inflamação neonatal — a micróglia (e macrófagos perivasculares) mantém uma assinatura transcricional e epigenética alterada: limiar de ativação rebaixado, resposta amplificada a um segundo estímulo (menor dose de LPS já induz resposta maior e mais longa) e resolução mais lenta (Perry & Teeling, 2013)[OB; revisão, camundongo+humano]; (Norden et al., 2015)[OB; revisão, humano]. No envelhecimento normal do hipocampo, o priming é acompanhado de aumento basal de IL-1β e microgliose — terreno no qual uma infecção ou cirurgia ("segundo golpe") desencadeia delirium/declínio persistente (Barrientos et al., 2015)[OB; revisão, camundongo+humano].

Experimentalmente, o priming tem janela temporal longa: inflamação neonatal induz priming microglial no hipocampo ventral via regulação epigenética, persistindo até a vida adulta e aumentando a vulnerabilidade comportamental (Yang et al., 2026)[ML; camundongo]; lesão cerebral leve repetida ("mTBI") cria vulnerabilidade a insultos subsequentes por priming (Qiu et al., 2026)[ML; camundongo]. Em nível mecanístico, o priming associa-se a: (a) manutenção do "sinal 1" transcricional (NF-κB/priming de pró-IL-1β) sem resolução; (b) disfunção mitocondrial e mtROS (crosstalk B9) baixando o limiar do inflamassoma; (c) SPMs insuficientes; (d) marcações epigenéticas em células imunes e centrais. Em humanos, o priming é inferido por marcadores (PCR/IL-6 persistentemente elevados, sinal TSPO-PET aumentado — ver BLOCO05) e por epidemiologia (infecção/adversidade precoces como fator de risco tardio); a demonstração causal direta é animal/in vitro, e essa fronteira [EXT] é mantida explícita ao longo da Biblioteca.

### 1.4 — Notas de espécie e extrapolação

- A cascata PAMP/DAMP → TLR/NLRP3 → NF-κB → caspase-1 → IL-1β/IL-18 é **causal e manipulável em camundongo/célula**; em humanos o elo é fechado por marcadores, genética e intervenção de prova (IFN-α, anti-citocina em subgrupo — BLOCO05/06). Toda vez que um achado animal embasar afirmação sobre o paciente humano, o vínculo nasce com `g2_motivo` de extrapolação e `verification_status = "pendente"` até o G3 marcar `extrapolado`/`preclinico`.
- Sickness behavior é conservado em vertebrados (Lopes, 2021)[OB; revisão comparada], reforçando que se trata de programa adaptativo evolutivo — mas a tradução para "sintoma depressivo humano" é análoga [EXT], não identidade.

[REF_BLOCO_01: Swanson_2019 | Serhan_2014 | Serhan_Levy_2018 | Perry_Teeling_2013 |
Barrientos_2015 | Norden_2015 | Dantzer_2001 | Dantzer_2006 | Harden_2015 |
OConnor_2009 | Lopes_2021 | Yang_2026_neonatal | Qiu_2026_mTBI]

---

# MÓDULO 9 (NATIVO) — fragmentos do BLOCO_01

## Nível 1 — /Evidencias/Bibliografia/01_pmids.json (referências usadas neste bloco)

```json
[
 {"id_referencia_interna":"REF_Swanson_2019","pmid":"31036962","doi":"10.1038/s41577-019-0165-0","autores":"Swanson KV; Deng M; Ting JP-Y","titulo":"The NLRP3 inflammasome: molecular activation and regulation to therapeutics","revista":"Nat Rev Immunol","ano":"2019","idioma":"eng","tipo_publicacao":"Review","especie_mesh":["Humans","Animals"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"ancora_REF_MODULO_01"},
 {"id_referencia_interna":"REF_Serhan_2014","pmid":"24899309","doi":"10.1038/nature13479","autores":"Serhan CN","titulo":"Pro-resolving lipid mediators are leads for resolution physiology","revista":"Nature","ano":"2014","idioma":"eng","tipo_publicacao":"Review","especie_mesh":["Humans","Animals"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"ancora_REF_MODULO_01"},
 {"id_referencia_interna":"REF_Serhan_Levy_2018","pmid":"29757195","doi":"10.1172/JCI97943","autores":"Serhan CN; Levy BD","titulo":"Resolvins in inflammation: emergence of the pro-resolving superfamily of mediators","revista":"J Clin Invest","ano":"2018","idioma":"eng","tipo_publicacao":"Review","especie_mesh":["Humans","Animals"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"ancora_REF_MODULO_01"},
 {"id_referencia_interna":"REF_Perry_Teeling_2013","pmid":"23732506","doi":"","autores":"Perry VH; Teeling J","titulo":"Microglia and macrophages of the central nervous system: the contribution of microglia priming and systemic inflammation to chronic neurodegeneration","revista":"Semin Immunopathol","ano":"2013","idioma":"eng","tipo_publicacao":"Review; Research Support","especie_mesh":["Humans","Animals","Mice"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"claim_BLOCO01.003"},
 {"id_referencia_interna":"REF_Barrientos_2015","pmid":"25772789","doi":"10.1016/j.neuroscience.2015.03.007","autores":"Barrientos RM; Kitt MM; ...","titulo":"Neuroinflammation in the normal aging hippocampus","revista":"Neuroscience","ano":"2015","idioma":"eng","tipo_publicacao":"Review; Research Support","especie_mesh":["Humans","Animals"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"claim_BLOCO01.003"},
 {"id_referencia_interna":"REF_Norden_2015","pmid":"25445485","doi":"10.1016/j.neuropharm.2014.12.028","autores":"Norden DM; Muccigrosso MM; Godbout JP","titulo":"Microglial priming and enhanced reactivity to secondary insult in aging, and traumatic CNS injury, and neurodegenerative disease","revista":"Neuropharmacology","ano":"2015","idioma":"eng","tipo_publicacao":"Review","especie_mesh":["Humans"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"ancora_REF_MODULO_01"},
 {"id_referencia_interna":"REF_Dantzer_2001","pmid":"12000023","doi":"10.1111/j.1749-6632.2001.tb03017.x","autores":"Dantzer R","titulo":"Cytokine-induced sickness behavior: mechanisms and implications","revista":"Ann N Y Acad Sci","ano":"2001","idioma":"eng","tipo_publicacao":"Review; Research Support","especie_mesh":["Humans","Animals","Mice","Rats"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"claim_BLOCO01.002"},
 {"id_referencia_interna":"REF_Dantzer_2006","pmid":"16877117","doi":"10.1016/j.ncl.2006.03.003","autores":"Dantzer R","titulo":"Cytokine, sickness behavior, and depression","revista":"Neurol Clin","ano":"2006","idioma":"eng","tipo_publicacao":"Review; Research Support","especie_mesh":["Humans","Animals","Mice","Rats"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"claim_BLOCO01.002"},
 {"id_referencia_interna":"REF_Harden_2015","pmid":"26187566","doi":"10.1016/j.bbi.2015.07.012","autores":"Harden LM; Kent S; ...","titulo":"Fever and sickness behavior: Friend or foe?","revista":"Brain Behav Immun","ano":"2015","idioma":"eng","tipo_publicacao":"Review; Research Support","especie_mesh":["Humans","Animals"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"claim_BLOCO01.002"},
 {"id_referencia_interna":"REF_OConnor_2009","pmid":"18195714","doi":"10.1038/sj.mp.4002102","autores":"O'Connor JC; Lawson MA; André C; ...","titulo":"Lipopolysaccharide-induced depressive-like behavior is mediated by indoleamine 2,3-dioxygenase activation in mice","revista":"Mol Psychiatry","ano":"2008","idioma":"eng","tipo_publicacao":"Research Support (N.I.H.)","especie_mesh":["Animals","Mice"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"ancora_Dantzer_2008 (3o candidato)"},
 {"id_referencia_interna":"REF_Lopes_2021","pmid":"33942101","doi":"10.1242/jeb.228537","autores":"Lopes PC; French SS; ...","titulo":"Sickness behaviors across vertebrate taxa: proximate and ultimate mechanisms","revista":"J Exp Biol","ano":"2021","idioma":"eng","tipo_publicacao":"Review; Research Support","especie_mesh":["Animals"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"claim_BLOCO01.002"},
 {"id_referencia_interna":"REF_Yang_2026_neonatal","pmid":"41707799","doi":"","autores":"Yang Y; Rong J; ...","titulo":"Neonatal inflammation induces ventral hippocampal microglial priming via epigenetic regulation","revista":"Brain Behav Immun","ano":"2026","idioma":"eng","tipo_publicacao":"Journal Article","especie_mesh":["Animals","Mice"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"claim_BLOCO01.003"},
 {"id_referencia_interna":"REF_Qiu_2026_mTBI","pmid":"41519246","doi":"","autores":"Qiu J; Yang G; ...","titulo":"Injury-environment interaction: microglial priming by mTBI creates vulnerability to subsequent challenge","revista":"Brain Behav Immun","ano":"2026","idioma":"eng","tipo_publicacao":"Journal Article","especie_mesh":["Animals","Mice"],"evid_role":"preclinical_mechanistic","g1_metodo":"eutils_automatico","g3_verificado_por":"","status_referencia":"CANDIDATO","verification_status":"pendente","data_verificacao":"","origem_busca":"claim_BLOCO01.003"}
]
```

## Nível 2 — /Evidencias/Vinculos/vinculos_referencia_afirmacao.json (um por frase-âncora)

> trecho_ancora = cópia LITERAL da frase do corpo acima, terminando em pontuação (regra E3).
> claim_id preenchido na extração de claims; nesta Rodada 2 vai com o claim_alvo da lista.
> g2 nasce "nao_avaliado"; g3 vazio; verification_status "pendente".

```json
[
 {"id_vinculo":"VINC_B1_0001","id_referencia_interna":"REF_Swanson_2019","claim_id":"B1.MEC.BLOCO01.001","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.1","trecho_ancora":"Diante de patógeno, lesão tecidual ou estressor agudo, células mieloides (monócitos, macrófagos, micróglia) reconhecem motivos moleculares conservados (PAMPs, ex. LPS bacteriano; DAMPs de células lesadas) por receptores de reconhecimento padrão — TLR2/4 e o inflamassoma NLRP3 — e disparam transcrição NF-κB de citocinas pró-inflamatórias (IL-1β, IL-6, TNF-α) seguida de maturação por caspase-1 (Swanson et al., 2019)[OB; revisão, humano+animal].","achado_central_molecular":"ativação de PRR/TLR/NLRP3 -> NF-kB -> caspase-1 em mieloides","natureza_relacao":"causal","grau_maturidade":"bem_suportado","forca_causal":"","extrapolacao_por_analogia":"sim (mecanismo descrito em animal/in vitro; humano por marcadores)","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0002","id_referencia_interna":"REF_Serhan_2014","claim_id":"B1.MEC.BLOCO01.001","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.1","trecho_ancora":"Essa ativação aguda é programada para resolver ativamente: mediadores lipídicos pró-resolutivos especializados (SPMs — resolvinas D/E, protectinas, maresinas, lipoxina A4), derivados do metabolismo de ômega-3/6, sinalizam a parada do recrutamento neutrofílico, o clearence de células apoptóticas por macrófagos e o retorno da micróglia ao estado ramificado homeostático (Serhan, 2014)[OB; revisão fisiológica, humano+animal; Serhan & Levy, 2018][OB].","achado_central_molecular":"SPMs induzem resolução ativa (parada de neutrófilos, eferocitose, retorno homeostático)","natureza_relacao":"causal","grau_maturidade":"bem_suportado","forca_causal":"","extrapolacao_por_analogia":"parcial (fisiologia da resolução; relevância psiquiátrica é contexto)","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0003","id_referencia_interna":"REF_Serhan_Levy_2018","claim_id":"B1.MEC.BLOCO01.001","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.1","trecho_ancora":"Essa ativação aguda é programada para resolver ativamente: mediadores lipídicos pró-resolutivos especializados (SPMs — resolvinas D/E, protectinas, maresinas, lipoxina A4), derivados do metabolismo de ômega-3/6, sinalizam a parada do recrutamento neutrofílico, o clearence de células apoptóticas por macrófagos e o retorno da micróglia ao estado ramificado homeostático (Serhan, 2014)[OB; revisão fisiológica, humano+animal; Serhan & Levy, 2018][OB].","achado_central_molecular":"superfamília de resolvinas e mediação pró-resolutiva","natureza_relacao":"contributiva","grau_maturidade":"bem_suportado","forca_causal":"","extrapolacao_por_analogia":"parcial","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0004","id_referencia_interna":"REF_Perry_Teeling_2013","claim_id":"B1.MEC.BLOCO01.001","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.1","trecho_ancora":"A micróglia homeostática exerce vigilância contínua com processos móveis, sem produção sustentada de citocinas (revisão de biologia microglial; Perry & Teeling, 2013)[OB; revisão, humano+camundongo].","achado_central_molecular":"micróglia ramificada homeostática vs. priming","natureza_relacao":"associativa","grau_maturidade":"muito_estabelecido","forca_causal":"","extrapolacao_por_analogia":"nao (biologia basal conservada)","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0005","id_referencia_interna":"REF_Barrientos_2015","claim_id":"B1.MEC.BLOCO01.001","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.1","trecho_ancora":"O que distingue ativação adaptativa de patológica não é a presença de citocinas — elas são fisiológicas — e sim três parâmetros: duração (horas/dias vs. semanas/anos), magnitude (pico transitório vs. elevação de baixo grau contínua, \"low-grade inflammation\"/inflammaging) e, sobretudo, capacidade de resolução ativa (Barrientos et al., 2015)[OB; revisão, camundongo+humano].","achado_central_molecular":"inflammaging/baixo grau no hipocampo envelhecido; limiar duração/magnitude/resolução","natureza_relacao":"associativa","grau_maturidade":"bem_suportado","forca_causal":"","extrapolacao_por_analogia":"sim (envelhecimento animal -> vulnerabilidade humana)","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0006","id_referencia_interna":"REF_Norden_2015","claim_id":"B1.MEC.BLOCO01.001","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.1","trecho_ancora":"O estado resultante é de priming microglial: a micróglia permanece \"sensibilizada\", com limiar rebaixado, e responde de forma amplificada e prolongada a um segundo desafio (Norden et al., 2015)[OB; revisão, humano].","achado_central_molecular":"priming/reatividade aumentada a segundo insulto (envelhecimento, lesão, doença)","natureza_relacao":"contributiva","grau_maturidade":"bem_suportado","forca_causal":"","extrapolacao_por_analogia":"sim","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0007","id_referencia_interna":"REF_Norden_2015","claim_id":"B1.MEC.BLOCO01.003","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.3","trecho_ancora":"Após um primeiro insulto — infecção sistêmica, lesão, estresse crônico, envelhecimento ou inflamação neonatal — a micróglia (e macrófagos perivasculares) mantém uma assinatura transcricional e epigenética alterada: limiar de ativação rebaixado, resposta amplificada a um segundo estímulo (menor dose de LPS já induz resposta maior e mais longa) e resolução mais lenta (Perry & Teeling, 2013)[OB; revisão, camundongo+humano]; (Norden et al., 2015)[OB; revisão, humano].","achado_central_molecular":"priming microglial: assinatura epigenética, limiar rebaixado, resposta amplificada","natureza_relacao":"causal","grau_maturidade":"bem_suportado","forca_causal":"","extrapolacao_por_analogia":"sim (demonstração causal é animal)","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0008","id_referencia_interna":"REF_Dantzer_2001","claim_id":"B1.MEC.BLOCO01.002","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.2","trecho_ancora":"O melhor modelo de neuroinflamação aguda fisiológica é o sickness behavior (comportamento de adoecimento): após administração de LPS ou indução por citocinas, o organismo exibe um conjunto coordenado e estereotipado — retraimento social, anedonia transitória, fadiga/hipersonia, redução de exploração e apetite, hiperalgesia leve — que redireciona energia para combate ao patógeno e reparo (Dantzer et al., 2001)[EC; revisão mecanística, camundongo+humano].","achado_central_molecular":"sickness behavior induzido por citocinas/LPS como programa coordenado","natureza_relacao":"causal","grau_maturidade":"muito_estabelecido","forca_causal":"","extrapolacao_por_analogia":"parcial (modelo conservado; tradução a sintoma humano é análoga)","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0009","id_referencia_interna":"REF_Harden_2015","claim_id":"B1.MEC.BLOCO01.002","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.2","trecho_ancora":"Cronologicamente, o quadro inicia-se em horas (pico de citocinas 2–6 h pós-LPS), atinge o máximo comportamental em 6–24 h e resolve espontaneamente em 24–72 h com o término do estímulo e a entrada dos programas de resolução — inclusive febre e sickness foram reinterpretados como respostas amigas ou adversas a depender do contexto temporal (Harden et al., 2015)[OB; revisão, camundongo+humano].","achado_central_molecular":"cronologia de iniciação/resolução do sickness (horas -> 24-72h)","natureza_relacao":"associativa","grau_maturidade":"bem_suportado","forca_causal":"","extrapolacao_por_analogia":"parcial","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0010","id_referencia_interna":"REF_Dantzer_2006","claim_id":"B1.MEC.BLOCO01.002","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.2","trecho_ancora":"A via molecular está descrita: citocinas periféricas sinalizam ao cérebro por vias neurais (nervo vago), humorais (transporte através da barreira e em órgãos circunventriculares) e celulares (monócitos trafegando), e ativam IL-1β central e IDO — a transição de sickness para comportamento tipo-depressivo persistente é mediada pela via da quinurenina induzida por citocinas (Dantzer, 2006)[OB; revisão, camundongo+humano].","achado_central_molecular":"vias neural/humoral/celular imune->cérebro; IDO/quinurenina na transição sickness->depressão","natureza_relacao":"causal","grau_maturidade":"bem_suportado","forca_causal":"","extrapolacao_por_analogia":"sim","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0011","id_referencia_interna":"REF_OConnor_2009","claim_id":"B1.MEC.BLOCO01.002","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.2","trecho_ancora":"No animal, o LPS induz comportamento tipo-depressivo transitório que depende de IDO1 (O'Connor et al., 2009)[ML; camundongo]; quando o estímulo inflamatório persiste ou se repete (estresse crônico, envelhecimento, infecção latente), a resposta não retorna à linha de base — é a ponte para o item 1.3.","achado_central_molecular":"LPS -> comportamento depressivo depende de IDO1 em camundongo","natureza_relacao":"causal","grau_maturidade":"bem_suportado","forca_causal":"tier_2_necessidade_ou_suficiencia","extrapolacao_por_analogia":"sim (camundongo)","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0012","id_referencia_interna":"REF_Barrientos_2015","claim_id":"B1.MEC.BLOCO01.003","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.3","trecho_ancora":"No envelhecimento normal do hipocampo, o priming é acompanhado de aumento basal de IL-1β e microgliose — terreno no qual uma infecção ou cirurgia (\"segundo golpe\") desencadeia delirium/declínio persistente (Barrientos et al., 2015)[OB; revisão, camundongo+humano].","achado_central_molecular":"hipocampo envelhecido: IL-1b basal e microgliose; segundo golpe -> declínio","natureza_relacao":"contributiva","grau_maturidade":"bem_suportado","forca_causal":"","extrapolacao_por_analogia":"sim","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0013","id_referencia_interna":"REF_Yang_2026_neonatal","claim_id":"B1.MEC.BLOCO01.003","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.3","trecho_ancora":"Experimentalmente, o priming tem janela temporal longa: inflamação neonatal induz priming microglial no hipocampo ventral via regulação epigenética, persistindo até a vida adulta e aumentando a vulnerabilidade comportamental (Yang et al., 2026)[ML; camundongo]; lesão cerebral leve repetida (\"mTBI\") cria vulnerabilidade a insultos subsequentes por priming (Qiu et al., 2026)[ML; camundongo].","achado_central_molecular":"inflamação neonatal -> priming epigenético no hipocampo ventral até a vida adulta","natureza_relacao":"causal","grau_maturidade":"emergente","forca_causal":"tier_2_necessidade_ou_suficiencia","extrapolacao_por_analogia":"sim (camundongo; artigo recente)","evid_role":"preclinical_mechanistic","uso":"gap_pesquisa","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0014","id_referencia_interna":"REF_Qiu_2026_mTBI","claim_id":"B1.MEC.BLOCO01.003","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.3","trecho_ancora":"Experimentalmente, o priming tem janela temporal longa: inflamação neonatal induz priming microglial no hipocampo ventral via regulação epigenética, persistindo até a vida adulta e aumentando a vulnerabilidade comportamental (Yang et al., 2026)[ML; camundongo]; lesão cerebral leve repetida (\"mTBI\") cria vulnerabilidade a insultos subsequentes por priming (Qiu et al., 2026)[ML; camundongo].","achado_central_molecular":"mTBI -> priming microglial -> vulnerabilidade a insulto subsequente","natureza_relacao":"causal","grau_maturidade":"emergente","forca_causal":"tier_2_necessidade_ou_suficiencia","extrapolacao_por_analogia":"sim (camundongo)","evid_role":"preclinical_mechanistic","uso":"gap_pesquisa","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""},

 {"id_vinculo":"VINC_B1_0015","id_referencia_interna":"REF_Lopes_2021","claim_id":"B1.MEC.BLOCO01.002","mecanismo_origem":"B1","secao_origem":"BLOCO_01/1.4","trecho_ancora":"Sickness behavior é conservado em vertebrados (Lopes, 2021)[OB; revisão comparada], reforçando que se trata de programa adaptativo evolutivo — mas a tradução para \"sintoma depressivo humano\" é análoga [EXT], não identidade.","achado_central_molecular":"sickness conservado em táxons de vertebrados (mecanismos proximais/ultimatos)","natureza_relacao":"associativa","grau_maturidade":"bem_suportado","forca_causal":"","extrapolacao_por_analogia":"sim (comparado -> humano)","evid_role":"preclinical_mechanistic","uso":"contexto_mecanistico","status_referencia":"CANDIDATO","status_auditoria":"","verification_status":"pendente","data_verificacao":"","g2_elegibilidade":"nao_avaliado","g2_motivo":"","g1_metodo":"eutils_automatico","g3_verificado_por":""}
]
```

---

## Fila de busca complementar (sugeridas pelo GPM, SEM PMID ainda — não inventar)

- **Dantzer_2008** (Nature Reviews Neuroscience, "From inflammation to sickness and depression") → **já localizado:** (usar no BLOCO02/06, não aqui).
- **Miller_Raison_2016** → (Nature Reviews Immunology; usar no BLOCO02).
- miR-146a/IRAK1/TRAF6 como feedback negativo (mencionado no GPM 1.x): não há artigo dedicado no corpus do BLOCO01 — deixar como `(Autor, Ano)` sem PMID ou buscar na rodada de BLOCO03 (microglia).
- Feedback do eixo HPA/cortisol-GR inibindo NF-κB: pertence ao BLOCO06 (estresse/HPA) — referência cruzada, não cita aqui.
- **Capuron_Miller_2011** (, sinalização imune→cérebro): usar no BLOCO02/06.

[REF_BLOCO_01: Barrientos_2015[ML] | Dantzer_2001[ML] | Dantzer_2006[ML] | Harden_2015[ML] | Lopes_2021[ML] | Norden_2015[ML] | OConnor_2009[ML] | Perry_Teeling_2013[ML] | Qiu_2026_mTBI[ML] | Serhan_2014[ML] | Serhan_Levy_2018[ML] | Swanson_2019[ML] | Yang_2026_neonatal[ML]]

---

## BLOCO_02 — VIAS MOLECULARES DO MECANISMO

### 2.1 — Inflamassoma NLRP3: sequência de ativação e prova causal (BLOCO02.001)

O NLRP3 é o inflamassoma mais implicado na neuroinflamação. Sua ativação exige **dois sinais**: o sinal 1 (priming) — TLR4/TNFR/IL-1R → NF-κB — induz a transcrição de NLRP3 e da pró-IL-1β; o sinal 2 (ativação) — disparado por ATP/P2X7, dano mitocondrial (mtROS, mtDNA), eflixo de K+ ou cristais — promove a montagem do complexo NLRP3–ASC–pró-caspase-1, com autoclivagem da caspase-1 e maturação de IL-1β/IL-18 e clivagem de GSDMD (Swanson et al., 2019)[OB; revisão, humano+animal]. A dependência de dois sinais é explorada fisiologicamente como tolerância: em macrófagos, o itaconato induzido por TLR regula o sinal 2 após priming prolongado por LPS, estabelecendo **tolerância à ativação tardia do NLRP3** em sinergia com iNOS — demonstração manipulável de que priming e ativação são etapas dissociáveis (Bambouskova et al., 2021)[ML; camundongo]. A prova de que a montagem do complexo é necessária e suficiente vem da genética humana: variantes ganho-de-função de NLRP3 (síndromes cryopyrin/CAPS) formam inflamassomas **constitutivamente ativos**, com clivagem basal de gasdermina D, liberação de IL-18 e piroptose mesmo sem gatilho externo — em pacientes e modelos animais (Pathogenic NLRP3 mutants, 2024)[EC; humano+camundongo][EXT para TDM]. Em SNC, a inibição seletiva de NLRP3 reduz inflamação e dano em modelos [ML; EXT]. Natureza: causal em animal/célula; em humanos o elo para depressão é fechado por marcadores e intervenção (ver BLOCO05).

### 2.2 — Outros inflamassomas no SNC: NLRP1, AIM2, NLRC4 (BLOCO02.002)

Os inflamassomas são complexos supramoleculares citosólicos que respondem a PAMPs/DAMPs e desencadeiam liberação de citocinas e piroptose; a família inclui NLRP3, NLRP1, AIM2 (sensor de DNA) e NLRC4, com estruturas e ligantes distintos (Mechanistic insights from inflammasome structures, 2024)[OB; revisão, humano+animal]. No parênquima cerebral, há evidência direta de via análoga para **NLRP1 em neurônios**: após hemorragia intracerebral experimental, a ativação de CCR5 promove piroptose neuronal dependente de NLRP1 via CCR5/PKA/CREB, e o antagonismo de CCR5 (maraviroc) reduz o dano (CCR5/NLRP1 neuronal pyroptosis, 2021)[ML; camundongo][EXT]. AIM2 aparece como sensor de DNA em contexto de morte celular imune na neuroinflamação (Innate Immune Cell Death in Neuroinflammation, 2022)[OB; revisão][EXT]; NLRC4 tem evidência indireta. Maturidade: NLRP3 bem_suportado; NLRP1 neuronal emergente; AIM2/NLRC4 hipótese_inicial no SNC comportamental.

### 2.3 — Gasderminas como efetoras da piroptose (BLOCO02.003)

A piroptose é executada pela família das gasderminas. Demonstração recente e forte no SNC: a **ativação de GSDMD no endotélio cerebral** — pela caspase-11 sensora de LPS citosólico, e não pelas citocinas induzidas por TLR4 — medeia a ruptura inflamatória da barreira hematoencefálica na sepse/desafio com LPS circulante; camundongos deficientes na via LBP–CD14 de internalização de LPS resistem à quebra da barreira (Brain endothelial GSDMD activation mediates inflammatory BBB breakdown, 2024)[EC; camundongo+humano][EXT]. Em microglia, GSDMD medeia piroptose na encefalopatia séptica via eixo TRIM45/Atg5/NLRP3 (TRIM45 microglia pyroptosis, 2023)[ML; camundongo][EXT]. GSDME (executor alternativo, acionado por caspase-3) é citado em revisões de morte celular imune no SNC [OB; EXT]. Natureza: causal em animal; a relevância direta para comportamento depressivo é emergente.

### 2.4 — TLR4 como receptor de LPS até NF-κB (BLOCO02.004)

O TLR4 (com co-receptores MD-2/CD14) é o receptor canônico do LPS. A via completa — LPS → TLR4/MyD88 → IRAK/TRAF6 → IKK → degradação de IκBα → NF-κB nuclear → transcrição de IL1B/IL6/TNF — é demonstrada por manipulação: o desafio com LPS induz sickness, déficit cognitivo e ativação microglial (Iba-1+) em camundongos, com elevação de citocinas pró-inflamatórias, bloqueável por interferência na via (LPS-induced cognitive impairment in mice, 2019)[ML; camundongo]. A modulação farmacológica a jusante confirma os elos: gastrodina reduz neuroinflamação e ativação microglial regulando TLR4/TRAF6/NF-κB (Gastrodin TLR4/TRAF6/NF-κB, 2024)[ML; camundongo][EXT]. Causal e bem_suportado em animal; a tradução para inflamação humana de baixo grau é associativa/[EXT].

### 2.5 — TLR2 e TLR3: vias distintas (BLOCO02.005)

TLR2 (lipopeptídeos de Gram-positiva, com TLR1/6) e TLR3 (RNA de fita dupla/viral e RNAs extracelulares) têm ligantes e efeitos próprios. TLR3 neuronal é relevante para função cognitiva: em camundongos com dor neuropática crônica, RNAs extracelulares sinalizam via TLR3 no hipocampo e contribuem para o declínio cognitivo; o knockout de TLR3 e o knockdown neuronal específico melhoram a cognição, reduzem citocinas e apoptose neuronal versus selvagens (Extracellular RNAs–TLR3 cognitive impairment, 2023)[ML; camundongo][EXT]. TLR2 media resposta imune a bactéria em nociceptores de forma distinta da via glial (Bacteria activate sensory neurons, 2013)[ML; camundongo]. Em glia, TLR2 responde a componentes de parede bacteriana com produção de citocinas [OB]. Maturidade: bem_suportado em animal; humanos [EXT].

### 2.6 — RLRs (RIG-I/MDA5) no SNC: inventário honesto (BLOCO02.006)

A busca por ferramenta não retornou literatura direta robusta ligando **RIG-I/MDA5** a comportamento/neuroinflamação depressiva. O que existe é periférico: TBK1 — que integra a sinalização de RLRs e cGAS-STING para IFN tipo I e NF-κB — quando perdido em humanos por mutações homozigotas causa autoinflamação crônica sistêmica dirigida por morte celular induzida por TNF, sem infecções virais graves (Human TBK1 deficiency autoinflammation, 2021)[EC; humano]. Isso documenta a existência da maquinaria de detecção de RNA/DNA e sua interseção com TNF, mas **não estabelece RLRs como via de neuroinflamação comportamental**. Estado: `nao_estabelecido` / escassez de evidência direta — registrado como N/A parcial no inventário negativo, não forçado.

### 2.7 — RAGE e receptores scavenger para DAMPs (BLOCO02.007)

O receptor de produtos finais de glicação avançada (RAGE) é o principal receptor de DAMP para S100 e HMGB1 no SNC. A família S100 compreende 24 membros com funções intra/extracelulares, alguns induzidos em patologia em células que não os expressam normalmente (Functions of S100 proteins, 2013)[OB; revisão, humano+animal]. RAGE em astrócitos é tratado como "mais que uma questão de humor" pela literatura (Astrocyte's RAGE, 2018)[OB; revisão][EXT]. A ligação DAMP–RAGE aciona NF-κB e produz retroalimentação positiva (RAGE é induzível por NF-κB). Detalhes dose-dependentes em 2.24.

### 2.8 — HMGB1 como DAMP (BLOCO02.008)

HMGB1 é uma proteína nuclear liberada por células lesadas/piroptóticas ou secretada ativamente; a forma **dissulfeto-HMGB1** (oxidada) é a imunoativa, sinalizando via RAGE/TLR4. Em lesão cerebral isquêmica, ácido hipocloroso derivado de mieloperoxidase microglial oxida HMGB1 facilitando sua secreção e amplificando a neuroinflamação (HOCl microglial MPO → HMGB1 release, 2024)[ML; rato+humano][EXT]. Em revisão focada em depressão, DAMPs (incluindo HMGB1) são apresentados como alarmes que disparam ativação microglial e liberação de citocinas na TDM, com modulação lipídica (Omega-3/DAMPs in depression, 2024)[OB; revisão, humano+animal]. Natureza: mecanística em animal; associação em depressão [EXT], emergente.

### 2.9 — DNA mitocondrial livre como DAMP ativador de NLRP3 (BLOCO02.009)

O mtDNA extracelular/livre funciona como DAMP: ativa inflamassomas e a resposta de IFN via cGAS-STING (ver 2.18). Em lesão pulmonar aguda induzida por DAMP mitocondrial, miR-223 de neutrófilos Ly6G+ inibe o NLRP3 — demonstrando que DAMPs mitocondriais são gatilho fisiológico do complexo (miR-223 inhibits NLRP3 in mitochondrial DAMP injury, 2017)[ML; camundongo][EXT]. A disfunção mitocondrial e o "inflamm-aging" são alimentados por vazamento de mtDNA e sinalização imune (Fueling Inflamm-Aging through Mitochondrial Dysfunction, 2017)[OB; revisão, humano]. Elo causal específico com comportamento depressivo: cross-ref B9 (disfunção mitocondrial); no B1, fica como mecanismo a montante do NLRP3, causal em modelos de dano, [EXT] para TDM.

### 2.10 — Via da quinurenina: bifurcação celular e enzimas (BLOCO02.010)

O triptofano é desviado da serotonina para a via da quinurenina por ação de **IDO1** (induzida por citocinas/IFN-γ), IDO2 e TDO2. A bifurcação celular é funcionalmente oposta: em **astrócitos**, KAT (kynurenine aminotransferase) gera **KYNA** (ácido quinurênico) — antagonista NMDA no sítio glicina/agonista α7nACh, neuroprotetor; em **micróglia/macrófagos**, KMO direciona para **QUIN** (ácido quinolínico) e 3-HK — agonista NMDA, gerador de ROS, neurotóxico. A IDO1 e a via são reguladoras centrais do envelhecimento e da imunidade (IDO1/kynurenine in aging, 2022)[OB; revisão, humano], e o eixo triptofano–quinurenina é apontado como ligação intestino-cérebro na depressão inflamatória (Tryptophan-kynurenine metabolism gut-brain depression, 2021)[OB; revisão, humano+animal]. Em adolescentes deprimidos, metabolômica de triptofano e microbioma associam-se ao fenótipo [EC; humano]. A prova causal de que a transição sickness→depressão depende de IDO foi mostrada em camundongo (O'Connor et al., 2009)[ML] no BLOCO01. Natureza: enzimas e bifurcação muito_estabelecido; direção em depressão bem_suportado.

### 2.11 — TNF solúvel/TNFR1 vs. TNF transmembrana/TNFR2 (BLOCO02.011)

O TNF tem dois receptores de sinal oposta: **TNFR1 (p55)**, acionado sobretudo por TNF solúvel, medeia resposta pró-inflamatória/apoptótica/necroptótica; **TNFR2 (p75)**, preferencialmente ativado por TNF transmembrana, é homeostático/neuroprotetor e imunorregulador. Em modelo de Alzheimer, a necroptose neuronal dependente de TNF-α é regulada pela coordenação RIPK1 (TNF-α neuronal necroptosis RIPK1, 2021)[ML; camundongo+humano][EXT]. Ao contrário, TNFR2 em microglia molda propriedades remielinizantes e protetoras após dano, de forma sexo-dependente (TNFR2 microglia remyelination, 2025)[ML; camundongo+humano][EXT]. Em modelo de depressão induzida, a inibição de microglia/neuroinflamação por arctigenina envolve a redução de TNF (Arctigenin anti-depression microglia, 2020)[ML; camundongo]. A distinção de isoforma de receptor é assim causal em animal; a maioria dos estudos clínicos mede "TNF total" e não separa os ramos — limitação registrada para o marcador (BLOCO05).

### 2.12 — Polimorfismos funcionais e genética (BLOCO02.012)

A genética funcional da inflamação fornece prova humana. O achado mais diretamente ancorado nesta trilha: polimorfismos funcionais em **IL-6 (rs1800795/-174G>C)** e no transportador de serotonina (5-HTTLPR) modificam a depressão induzida por interferon-α em hepatite C — variantes que elevam sinalização IL-6 associam-se a maior risco de depressão sob terapia com citocina (Bull et al., 2009)[EC; humano]. É interação gene–ambiente (genótipo × exposição inflamatória), não associação transversal pura. Para FKBP5, ver 2.20. Para outras variantes (IL1B, TNF -308G/A, TLR4, NLRP3, CRP), a busca do top-10 retornou material genético periférico que não testa diretamente esses polimorfismos no contexto; permanecem como `(gene, associação reportada)` sem vínculo G3 dedicado neste lote — a direção funcional (alelo hiper-expressor aumenta transcrição pró-inflamatória) é herdada do GPM e fica para confirmação em lote de genética humana. Natureza do conjunto: associativo/interação em humano.

### 2.13 — Lipídios pró-resolutivos (SPMs): resolução ativa (BLOCO02.013)

A resolução é um programa ativo, não a simples diluição da inflamação. Mediadores lipídios especializados — resolvinas (série E de EPA e D de DHA), protectinas/PD1/NPD1, maresinas (MaR), lipoxina A4 (do araquidônico) — produzidos por lipoxigenases, param o recrutamento neutrofílico, promovem eferocitose e retornam tecidos à homeostase (Serhan, 2014)[OB; revisão, humano+animal]; a superfamília das resolvinas é detalhada quanto a receptores e ações (Serhan & Levy, 2018)[OB; revisão]. Em dor neuropática, mecanismos imunes pró-resolutivos são mapeados como alvo terapêutico (Pain-resolving immune mechanisms, 2023)[OB; revisão], e a maresina MaR2 derivada de tecido adiposo marrom contribui para a resolução da inflamação no frio (Brown adipose MaR2 resolution, 2022)[ML; camundongo][EXT]. O GPR37 em macrófagos regula fagocitose e resolução da dor inflamatória (GPR37 macrophage phagocytosis resolution, 2018)[ML; camundongo+humano][EXT]. Em depressão, a insuficiência relativa de SPMs é hipótese mecanística [EXT; gap_pesquisa].

### 2.14 — Senescência celular e SASP em glia (BLOCO02.014)

Células senescentes secretam um fenótipo secretório associado à senescência (SASP) — citocinas/quimiocinas/proteases em baixo grau contínuo. Em microglia senescente no envelhecimento/Alzheimer, a lactilação de histona H3K18 potencializa o SASP e o declínio cerebral (H3K18 lactylation of senescent microglia, 2023)[ML; camundongo+humano][EXT]. O envelhecimento celular e a senescência estão consolidados como mecanismo de neuroinflamação crônica (Aging, Cellular Senescence and Alzheimer's, 2022)[OB; revisão]. Astócitos reativos associados a neuropatologia são revisados sistematicamente (Reactive astrocytes systematic review, 2023)[OB; revisão, humano]. Nível de evidência para ansiedade/depressão: o SASP glial é bem demonstrado em envelhecimento/neurodegeneração; a extrapolação para transtornos de humor é análoga [EXT], parte do conceito de inflamação de baixo grau.

### 2.15 — Via NF-κB: sequência completa receptor→transcrição (BLOCO02.015)

O NF-κB é o nó transcricional da inflamação. Sequência: receptor (TLR4/MyD88, TNFR1 ou IL-1R1) → **IRAK/TRAF6 → complexo IKK → fosforilação e degradação de IκBα → libertação e translocação nuclear de NF-κB (p65/p50)** → transcrição de IL1B, IL6, TNF, NLRP3 (priming), PTGS2 (COX-2) e NOS2 (iNOS). A via é confirmada por manipulação em microglia: gastrodina reduz neuroinflamação agindo em TLR4/TRAF6/NF-κB (Gastrodin TLR4/TRAF6/NF-κB, 2024)[ML; camundongo], e o polifenol punicalina atenua prejuízo de memória induzido por LPS por supressão da mesma cascata (Punicalin LPS memory NF-κB, 2024)[ML; camundongo][EXT]. A resistência a glicocorticoides (BLOCO08/B2) desinibe o NF-κB porque o GR ativado normalmente reprime esta via. Causal e muito_estabelecido em sistemas imunes/neurais; humano por marcadores [EXT].

### 2.16 — JAK-STAT e interferon: o paradigma causal humano (BLOCO02.016)

IFN tipo I (IFN-α/β via IFNAR) e tipo II (IFN-γ via IFNGR) sinalizam por JAK1/JAK2/TYK2 → STAT1/STAT2 → genes estimulados por IFN (ISGs), incluindo **indução de IDO1** (2.10). O paradigma de causalidade humana mais próximo de B1 é a **depressão induzida por interferon-α**: pacientes tratados com IFN-α (hepatite C/melanoma) desenvolvem sintomas depressivos de novo com curso previsível, e a maquinaria JAK-STAT/IDO está documentada em células-tronco neurais (Mechanisms for IFN-α-induced depression and NSC dysfunction, 2014)[ML; célula+revisão]; um composto natural (paeoniflorin) alivia neuroinflamação e comportamento tipo-depressivo induzidos por IFN-α (Paeoniflorin IFN-α depression, 2017)[ML; camundongo][EXT], e trans-cinamaldeído restaura a função astrocitária no mesmo modelo (Trans-cinnamaldehyde IFN-α astrocyte, 2025)[ML; camundongo]. A revisão clínica da depressão induzida por interferon reconta mecanismos e manejo (Interferon-induced depression: mechanisms and management, 2007)[OB; revisão, SEM abstract no corpus — PENDENTE DE FULL-TEXT, não serve de lastro próprio]. Somado a Bull 2009 (genótipo modera o risco), este é o eixo de prova-de-conceito: uma citocina exógena causa comportamento depressivo em humano.

### 2.17 — Ácido araquidônico → COX-2 → PGE2 → EP e CRH (BLOCO02.017)

A inflamação induz COX-2 (PTGS2, transcrito de NF-κB), que gera PGE2 do araquidônico. PGE2 sinaliza pelos receptores EP1–EP4 e é o mediador central da **febre** e de parte do sickness: os mecanismos neurais da febre induzida por inflamação, com PGE2 hipotalâmico à frente, estão detalhados (Neural Mechanisms of Inflammation-Induced Fever, 2018)[OB; revisão, humano+animal]. COX-2 também tem papel em sinalização sináptica (Cyclooxygenase-2 in synaptic signaling, 2008)[OB; revisão, humano+animal]. O elo com o HPA: PGE2 estimula CRH hipotalâmico, conectando inflamação aguda ao eixo do estresse (cross-ref B2). Bem_suportado; a participação na depressão crônica é [EXT].

### 2.18 — Via cGAS-STING (sensor de DNA citosólico) (BLOCO02.018)

DNA ectópico no citosol (mtDNA vazando, DNA nuclear dano) é detectado por **cGAS**, que produz cGAMP; cGAMP ativa **STING** → TBK1 → IRF3 → IFN tipo I, além de NF-κB. A via está consolidada como mecanismo de neuroinflamação em doenças neurológicas (cGAS-STING in neurological disorders, 2023)[OB; revisão, humano]; o cruzamento mitofagia–cGAS-STING é revisado na neuroinflamação (Mitophagy and cGAS-STING crosstalk, 2024)[OB]. Há prova manipulável no SNC: na disfunção cognitiva pós-operatória por sevoflurano, a ativação do **NLRP3 dependente do eixo mtDNA–cGAS-STING** em microglia conduz a neuroinflamação (mtDNA-cGAS-STING–NLRP3 postoperative cognition, 2024)[ML; camundongo][EXT]. Vazamento de mtDNA e cGAS-STING no envelhecimento cerebral são alvo terapêutico emergente (cGAS-STING brain aging, 2025)[OB; revisão][EXT]. Majoritariamente animal/in vitro; [EXT] para TDM.

### 2.19 — Freios anti-inflamatórios: IL-10/JAK1/STAT3 e TGF-β/SMAD (BLOCO02.019)

A resposta é contida por freios compensatórios. IL-10 liga IL-10Rα + IL-10Rβ (receptor compartilhado) e sinaliza por JAK1/TYK2 → **STAT3**, suprimindo transcrição pró-inflamatória. A biologia estrutural recente desacoplou as funções pró e anti-inflamatórias da IL-10 e mostrou limiares distintos entre populações imunes (Structure-based decoupling of IL-10 functions, 2021)[EC; humano+camundongo]. O eixo IL-10–STAT3–galectina-3 é essencial para macrófagos reparativos (IL-10-STAT3-Galectin-3 reparative macrophages, 2018)[ML; camundongo], e a entrega direcionada de IL-10 a microglia/macrófago melhora desfecho em hemorragia intracerebral (microglia-targeted IL-10 ICH, 2023)[ML; camundongo][EXT]. A insuficiência relativa deste freio (ex.: IL-10 baixa sob estresse crônico — Voorhees 2013 no BLOCO01) contribui à cronificação. TGF-β→TGFBR→SMAD2/3 é o segundo freio (imunorregulação/fibrose), citado em revisões do GPM [OB]. Contributivo; bem_suportado.

### 2.20 — Epigenética do estresse precoce: NR3C1 e FKBP5 (BLOCO02.020)

Adversidade precoce grava marcações epigenéticas que desregulam o eixo do cortisol. O achado humano seminal: um polimorfismo funcional em **FKBP5** (regulador do receptor de glicocorticoide) altera a interação da cromatina entre o sítio de início de transcrição e enhancers de longo alcance, e produz **desmetilação alelo-específica dependente de trauma de infância** em elementos de resposta a glicocorticoide, aumentando o risco de transtorno psiquiátrico relacionado ao estresse no adulto (Klengel et al., 2013)[EC; humano]. A revisão sistemática do estresse/epigenética/depressão consolida NR3C1 (metilação do promotor do GR), FKBP5, BDNF e outros genes correlacionados com depressão (Stress, epigenetics and depression: systematic review, 2019)[OB; revisão sistemática, humano]. A consequência funcional é a **resistência a glicocorticoides** — o GR deixa de reprimir NF-κB — fechando o loop estresse→inflamação (cross-ref B2/BLOCO08). Muito_estabelecido em humano para FKBP5/NR3C1.

### 2.21 — Metilação de IL6/TNF e direção de expressão (BLOCO02.021)

Em cérebro humano pós-morte, a regulação da expressão de TNF-α envolve chaveamento epigenético complexo: no córtex pré-frontal de indivíduos que morreram por suicídio, a superexpressão de TNF-α é explicada por mecanismos de microRNA e proteína de ligação a RNA que destravam o gene (Complex Epigenetic Switching in TNF-α Upregulation in suicide PFC, 2018)[EC; post-mortem humano]. Fatores psicológicos associam-se a metilação de DNA de genes do sistema imune/inflamatório (Psychological factors and DNA methylation of inflammatory genes, 2016)[EC; humano]. A direção funcional (hipometilação de promotor → maior expressão pró-inflamatória) é o princípio; a evidência direta para o promotor de IL6 em depressão é mais esparsa e fica como emergente [humano].

### 2.22 — Reguladores pós-transcricionais: miR-155 e miR-146a (BLOCO02.022)

Dois microRNAs formam um par de retroalimentação sobre NF-κB/JAK-STAT. **miR-146a** é o freio: tem como alvos IRAK1/TRAF6, e sua superexpressão em microglia hipocampal melhora função cognitiva reduzindo a via IRAK1/TRAF6/NF-κB (miR-146a hippocampal microglia IRAK1/TRAF6, 2025)[ML; camundongo]; vesículas extracelulares enriquecidas em miR-146a têm efeito imunomodulador/neuroprotetor (miR-146a-enriched MSC EV, 2025)[EC; célula/camundongo/humano], e miR-146a-5p reduz neuroinflamação em outros modelos [ML]. **miR-155** é o acelerador (alvo SOCS1, desinibindo JAK-STAT); a busca dedicada não retornou artigo SNC-comportamental forte para miR-155 neste lote, ficando como mecanismo previsto pelo GPM, com vínculo a confirmar (`nao_estabelecido` no SNC comportamental). Em microglia, o balanço miR-155↑/miR-146a↓ mantém o priming; a restauração de miR-146a é candidata terapêutica [EXT; gap_pesquisa].

### 2.23 — Modificações de histona como memória celular inata (BLOCO02.023)

O priming microglial tem base em marcas de cromatina. Em microglia senescente, a **lactilação de H3K18** mantém o programa transcricional pró-inflamatório no envelhecimento/Alzheimer (H3K18 lactylation senescent microglia, 2023)[ML; camundongo+humano][EXT]. A inflamação neonatal induz priming microglial no hipocampo ventral via **regulação epigenética (metilação de DNA)** que persiste até a vida adulta e sensibiliza a um segundo estresse — "two-hit" (Neonatal inflammation microglial priming epigenetic BAI1, 2026)[ML; camundongo]. Marcas de histona (acetilação/metilação) reconfiguram a acessibilidade de genes inflamatórios, baixando o limiar de resposta. Demonstrado em animal; a tradução para memória traumática humana é [EXT], emergente.

### 2.24 — Proteínas S100 como DAMPs: efeito dual dose-dependente via RAGE (BLOCO02.024)

S100B e S100A8/A9 (calprotectina) são DAMPs distintos de HMGB1. Têm efeito **dual por concentração e afinidade de receptor**: em níveis fisiológicos (nanomolar), S100B é trófico para neurônios; em níveis altos (micromolar), liberados por astrócitos lesados, S100B age via RAGE e é pró-inflamatório/tóxico (S100B stimulates microglia migration via RAGE chemokines, 2011)[ML; camundongo/rato]; a ligação S100B–RAGE em microglia estimula expressão de COX-2 e, em alta concentração, iNOS/NO em sinergia com LPS/IFN-γ (S100B–RAGE microglia COX-2, 2007)[ML; camundongo/humano]. A revisão de 2025 consolida S100B e S100A8/A9 como DAMPs que interagem com RAGE/TLRs disparando cascatas pró-inflamatórias e ativação glial, com nota explícita de que concentrações baixas podem ser neuroprotetoras (Relationship of S100 Proteins with Neuroinflammation, 2025)[OB; revisão, humano+animal]. Mecanística em animal; marcador S100B em depressão é [EXT]/emergente.

---

[REF_BLOCO_02: Arctigenin_2020[ML] | Bambouskova_2021[ML] | Bull_2009[EC] | CAPS_2024[EC] | CCR5_NLRP1_2021[ML] | COX2_synap_2008[ML] | Fever_2018[ML] | GPR37_2018[ML] | GSDMD_BBB_2024[ML] | Gastrodin_2024[ML] | H3K18_2023[ML] | HMGB1_HOCl_2024[ML] | IDO1_aging_2022[ML] | IFN_NSC_2014[ML] | IFN_dep_review_2007[EC] | IL10_Gal3_2018[ML] | IL10_struct_2021[ML] | Inflamassomas_2024[ML] | InflammAging_2017[EC] | InnateCellDeath_2022[ML] | KYN_gutbrain_2021[ML] | Klengel_2013[EC] | LPS_cog_2019[ML] | Omega3_DAMP_2024[EC] | PainResolv_2023[ML] | Punicalin_2024[ML] | S100B_2011[ML] | S100_review_2025[ML] | S100func_2013[ML] | Senesc_2022[ML] | Serhan_2014[ML] | Stress_Epi_2019[EC] | Swanson_2019[ML] | TBK1_2021[EC] | TLR2_nociceptor_2013[ML] | TLR3_2023[ML] | TNFR1_RIPK1_2021[ML] | TNFR2_2025[ML] | TNF_suicide_2018[EC] | TRIM45_2023[ML] | cGAS_POCD_2024[ML] | cGAS_neuro_2023[ML] | miR146a_2025[ML] | miR223_2017[ML]]

---

## BLOCO_03 — MEDIADORES ESPECÍFICOS (CITOCINAS, QUIMIOCINAS)

### 3.1 — IL-1β: fonte, receptor e impacto sobre BDNF/CREB (BLOCO03.001)

IL-1β, maturada pelo inflamassoma (BLOCO02), é a citocina que mais diretamente deprime a plasticidade neuronal. O achado clássico: IL-1β sistêmica reduz a expressão de mRNA de BDNF no hipocampo de rato — ligação direta entre sinal imune periférico e o fator trófico central (Systemic IL-1β decreases BDNF mRNA in hippocampus, 1993)[ML; rato]. Em cultura, IL-1β suprime a sobrevivência neuronal mediada por neurotrofinas e interage com crescimento neurítico de forma contexto-dependente (IL-1β and neurotrophin-3 neurite growth, 2011)[ML; célula/camundongo]. Mecanisticamente, IL-1β/IL-1R1 suprime a sinalização BDNF/TrkB/CREB que sustenta LTP e neurogênese (cross-ref B3). Em condições fisiológicas, citocinas residentes mantêm plasticidade; quando elevadas na neuroinflamação, IL-1β e TNF interferem com circuitos de aprendizado/cognição e promovem excitotoxicidade (TNF and IL-1β modulate synaptic plasticity during neuroinflammation, 2018)[OB; revisão, humano+animal]. Natureza: causal em animal/célula; o elo com BDNF em depressão humana é [EXT].

### 3.2 — TNF-α e plasticidade sináptica (BLOCO03.002)

O TNF tem papel fisiológico na plasticidade hebbiana e homeostática (escala de força sináptica) e patológico quando elevado: em neuroinflamação, TNF e IL-1β modulam plasticidade sináptica e contribuem para excitotoxicidade e neurodegeneração (TNF and IL-1β modulate synaptic plasticity, 2018)[OB; revisão, humano+animal]. O bloqueio periférico de TNF com etanercepte por via perispinhal é explorado em distúrbios neuroinflamatórios, sugerindo efeito central mesmo sem cruzar a BHE (Perispinal etanercept for neuroinflammatory disorders, 2009)[OB; revisão, humano]. Em modelos, intervenções anti-inflamatórias restauram sinalização CREB e memória/sono [ML; EXT]. Natureza: bem_suportado o efeito sobre plasticidade em animal; tradução humana emergente.

### 3.3 — IL-6: trans-sinalização e o duplo papel reparativo (BLOCO03.003)

O IL-6 não é unicamente danoso. Demonstração elegante: após lesão cerebral traumática, a simples remoção da micróglia pouco altera o desfecho, mas induzir a **renovação** da população gera um fenótipo microglial neuroprotetor que auxilia a recuperação — e esse efeito benéfico depende criticamente da **trans-sinalização de IL-6 via IL-6R solúvel + gp130** (Repopulating Microglia Promote Brain Repair in an IL-6-Dependent Manner, 2020)[ML; camundongo+humano]. Isso separa o ramo clássico (IL-6R de membrana, regenerativo) do trans-sinalizante (sIL-6R, pró-inflamatório) e mostra que o IL-6 tem faces opostas conforme contexto e receptor. Na periferia, a meta-análise de 82 estudos confirma IL-6 elevada na TDM (Peripheral cytokine/chemokine meta-analysis 82 studies, 2017)[MA; humano] — ver BLOCO05. Natureza: mecanística dual em animal; marcador humano bem_suportado.

### 3.4 — TGF-β1 como freio glial (BLOCO03.004)

TGF-β1 é citocina imunorreguladora; níveis reduzidos são relatados tanto em Alzheimer quanto em depressão, e a via é proposta como elo restaurativo compartilhado (TGF-β1 pathway in Alzheimer's and depression, 2025)[OB; revisão, humano+animal]. A meta-análise do efeito de antidepressivos sobre marcadores periféricos mostra deslocamento do balanço pró/anti-inflamatório (Antidepressant effect on peripheral inflammation meta-analysis, 2018)[MA; humano]. Natureza: associativo em humano; mecanístico de reparo [EXT].

### 3.5 — Priming microglial por IFN-γ via STAT1/NLRP3 (BLOCO03.005)

O priming microglial tem gatilhos imunes específicos. IFN-γ induz priming em micróglia por ativação **STAT1-mediada do inflamassoma NLRP3**: em cultura primária e em cérebro de camundongo, IFN-γ produz morfologia ativada ("hedgehog"), sobe marcadores CD86/CD11b e sensibiliza o NLRP3 (Microglial priming by IFN-γ involves STAT1/NLRP3, 2024)[ML; célula/camundongo]. Os princípios de priming e inibição do inflamassoma são revisados com implicações psiquiátricas (Principles of inflammasome priming and inhibition: psychiatric disorders, 2018)[OB; revisão, humano+animal]. Em modelo de depressão, o alvo NEK7 (regulador a montante do NLRP3) modula piroptose e microbiota e alivia comportamento tipo-depressivo (Targeting NEK7 pyroptosis depression, 2025)[ML; rato/camundongo][EXT]. Natureza: causal em animal; humano [EXT].

### 3.6 — Subpopulações microgliais: homeostática, priming, DAM (BLOCO03.006)

A micróglia não é uma entidade única. Coexistem estados: **homeostática/ramificada** (vigilância, P2Y12, TMEM119), **priming/reativa** (limalar rebaixado) e **DAM — microglia associada a doença** (assinatura transcricional de fagocitose/ativação, originalmente em neurodegeneração). Antidepressivos modulam a ativação microglial, deslocando o fenótipo para menos pró-inflamatório (Modulation of microglial activation by antidepressants, 2022)[OB; revisão, humano+animal]. Citocinas pró-inflamatórias e neuropeptídeos conectam inflamação sistêmica, estresse e pele (psoríase) a depressão/ansiedade (Proinflammatory cytokines and neuropeptides in psoriasis, depression and anxiety, 2025)[OB; revisão, humano+animal]. A identidade DAM em depressão é majoritariamente extrapolada de Alzheimer/doenças [EXT] — não há ainda perfil DAM específico de TDM consolidado.

### 3.7 — Astrócitos reativos A1 vs. A2 (BLOCO03.007)

Astócitos reativos se polarizam em **A1 (neurotóxico, induzido por citocinas microgliais)** e **A2 (neuroprotetor)**. Em camundongo, IFN-γ também priming astrocitário e a modulação por antidepressivos/anti-inflamatórios desloca o balanço (Microglial priming by IFN-γ, 2024)[ML]; revisões farmacológicas registram a modulação astrocitária por antidepressivos (Modulation of microglial activation by antidepressants, 2022)[OB]. A validação direta de A1/A2 em ansiedade/depressão humana é fraca — o binário A1/A2 é mais robusto em AVC/neurodegeneração; para TDM permanece [EXT], e o campo ressalta que a polarização é um continuum, não dois estados estanques.

### 3.8 — Sinalização purinérgica P2X7/P2Y12 (BLOCO03.008)

A comunicação micróglia–neurônio usa ATP/adenosina. **P2Y12** é receptor homeostático microglial que guia processos ao dano e mantém vigilância (marcador do estado ramificado); **P2X7** é receptor de ATP extracelular em alta concentração que funciona como "sinal 2" do NLRP3 (e fluxo de K+), disparando IL-1β. A ativação de P2X7 está implicada na despolarização e saída do estado homeostático; a perda de P2Y12 marca a transição para reatividade. Estes alvos são centrais nos princípios de priming/inibição do inflamassoma (Principles of inflammasome priming and inhibition, 2018)[OB; revisão, humano+animal]. A busca dedicada do lote retornou material esparso para ensaios P2X7 específicos em comportamento; o mecanismo é bem_suportado em célula/animal, o vínculo comportamental humano é [EXT]/gap_pesquisa.

### 3.9 — Barreira hematoencefálica: CCL2/CCR2 e transmigração de monócitos (BLOCO03.009, 012)

A BHE controla o tráfego de leucócitos. A quimiocina **CCL2 (MCP-1)** produzida no parênquima atravessa o endotélio microvascular cerebral por transporte transcelular, formando um gradiente que recruta monócitos por trás da barreira (Transcellular transport of CCL2 across brain microvascular endothelial cells, 2008)[ML; célula]. O receptor **CCR2** é o receptor dominante de quimiotaxia de monócitos Ly6C^high; inibição de HMG-CoA redutase reduz expressão de CCR2 e recrutamento (Statin reduces CCR2 monocyte recruitment, 2005)[ML; célula/humano/animal]. A adesão depende de **ICAM-1** no endotélio/astrócito ativado: telmisartana inibe adesão leucocitária induzida por TNF bloqueando ICAM-1 em astrócitos, com melhora de depressão/memória e redução de inflamação cerebral (Telmisartan blocks ICAM-1 in astroglia, 2020)[ML]. Estresse crônico de restrição induz marcadores inflamatórios e oxidativos na microvasculatura cerebral (Cerebral microvascular inflammatory markers under depressive stress, 2023)[ML; camundongo]. Natureza: passos celulares causais em animal/célula; transmigração na depressão humana [EXT].

### 3.10 — CX3CL1/CX3CR1: o freio neurônio→micróglia (BLOCO03.010)

A fractalcina **CX3CL1** é expressa por neurônios; seu único receptor **CX3CR1** é microglial — um eixo de comunicação direta que mantém a micróglia em estado homeostático. A perda de sinalização CX3CL1 desinibe a micróglia (reatividade). Em lesão cerebral, CX3CL1 atenua déficit neurológico e neuroinflamação via CX3CR1/p38 MAPK/ERK1/2 (CX3CL1 attenuates neuroinflammation via CX3CR1, 2026)[ML; camundongo+humano/célula]. Durante o desenvolvimento, a poda sináptica pela micróglia é necessária para a maturação normal do cérebro (Synaptic pruning by microglia is necessary for normal brain development, 2011)[ML; camundongo] — a fagocitose sináptica, regulada por CX3CR1 e complemento (BLOCO10), quando excessiva no adulto é candidata a mecanismo de perda sináptica na depressão [EXT]. Natureza: freio homeostático bem_suportado; exagero de poda na TDM emergente.

### 3.11 — CXCL8/IL-8 e sintomas somáticos (BLOCO03.011)

CXCL8 (IL-8) é quimiocina neutrofílica. A meta-análise de 82 estudos confirma alterações periféricas de quimiocinas na TDM, incluindo CCL2 e quimiocinas correlacionadas a sintomas somáticos/fadiga (Peripheral cytokine/chemokine meta-analysis 82 studies, 2017)[MA; humano]. A busca dedicada para IL-8 específica retornou material limitado neste lote; o vínculo direto IL-8↔sintomas somáticos fica como associativo [humano], menos específico que citocinas maiores — registrado como emergente, sem forçar mecanismo.

### 3.12 — Populações imunes perivasculares e portas de entrada (BLOCO03.006–009, 012; vagal/OVLT)

Além da micróglia parenquimal, o SNC conta com populações distintas: macrófagos perivasculares/meníngeos, monócitos infiltrantes Ly6C^high (via CCL2/CCR2), e linfócitos meníngeos. O recrutamento e adesão seguem os passos de CCL2/CCR2 e ICAM-1 descritos em 3.9. A sinalização imune→cérebro também usa **vias independentes de BHE**: nervo vago aferente (sinal neural rápido, ver Dantzer/Banks no BLOCO01) e órgãos circunventriculares/barreira porosa (área postrema), onde o endotélio é permeável. A disbiose intestinal agrava depressão pós-AVE via inflamassoma NLRP3 microglial (Gut dysbiosis post-stroke depression NLRP3, 2025)[ML; rato][EXT], e probióticos melhoram déficit de memória modulando glia/eixo intestino-cérebro (Probiotics gut-brain memory SAMP8, 2020)[ML; camundongo][EXT] — cross-ref B7. A revisão de eixo intestino-cérebro e inflamassoma consolida como microbiota hospedeira influencia fisiologia cerebral (Gut-brain axis microbiota inflammasome, 2020)[OB; revisão, humano+animal].

### 3.13 — IL-18: clivagem pelo inflamassoma e papel dual (BLOCO03.005)

IL-18 é, como IL-1β, maturada por caspase-1 no inflamassoma (compartilha o eixo NLRP3→ASC→caspase-1). Diferentemente de IL-1β, tem papel dual surpreendente no SNC: além das funções imunes, IL-18 participa de homeostase energética e estabilidade neural; a **deficiência de IL-18 em camundongos causa disfunção mitocondrial em células hipocampais e síndrome tipo-depressiva** — sugerindo que nem todo produto do inflamassoma é unicamente deletério e que a direção da alteração em depressão não é simplesmente "IL-18 alta" (Molecular Mechanisms of IL18 in Disease, 2023)[ML; camundongo+humano][EXT]. É elevada em alguns contextos inflamatórios (meta-análise de quimiocinas/citocinas, 2017)[MA], mas sua função neural protetora merece qualificador distinto de IL-1β. Natureza: emergente; direção em TDM humana não consolidada — registrado como mediador com associação não simples.

### 3.14 — IL-17A e Th17 (BLOCO03.006)

IL-17A é produzida por linfócitos Th17 (diferenciados sob IL-6 + TGF-β) e age via IL-17RA. Em modelo camundongo de comportamento tipo-depressivo induzido por metanfetamina, metabolismo de betaína desregulado direciona diferenciação Th17 periférica, e essa via imune periférica media dano ao SNC (Disrupted betaine metabolism drives Th17 in depression-like model, 2025)[ML; camundongo][EXT]. A revisão de citocinas/neuropeptídeos em psoríase/depressão/ansiedade inclui IL-17 entre os mediadores que conectam inflamação sistêmica e estresse (Proinflammatory cytokines and neuropeptides, 2025)[OB; revisão]. Natureza: mecanística emergente em animal; humano associativo [EXT], menos robusto que IL-6/TNF.

### 3.15 — Inventário NEGATIVO de mediadores (BLOCO03.004)

Registro honesto do que foi investigado mas **não mostra associação consistente** com ansiedade/depressão neste corpus, ou cuja direção é ambígua:
- **IL-18** — ver 3.13: função dual; "IL-18 sempre alta" é falso (deficiência também gera fenótipo depressivo em camundongo).
- **Quimiocinas neutrofílicas (CXCL8/IL-8)** — alterações periféricas presentes na meta-análise, mas sem especificidade mecanística para humor; fraco sinal direto (ver 3.11).
- **IFN-γ periférico** — marcador inconsistente nas meta-análises de sangue (o papel robusto é indutor de IDO/priming, não como marcador sérico de TDM).
- **IL-2, IL-12, IL-13** — aparecem em meta-análises com tamanhos de efeito pequenos e heterogêneos; sem via molecular dedicada ao humor.
Estes não são "inexistentes" — são marcadores sem associação robusta/consistente, e por isso não recebem nó próprio nem vínculo causal forte; ficam como ruído de fundo na citoquina-ampla, distinguindo o sinal replicado (IL-6, TNF, IL-1β, PCR, KYN/TRP) do não-replicado.
---

[REF_BLOCO_03: Antidep_meta_2018[MA] | Antidep_microglia_2022[ML] | CCL2_2008[ML] | CCR2_2005[ML] | CX3CL1_2026[ML] | Etanercept_2009[EC] | GutInfl_2020[ML] | ICAM_2020[ML] | IFNg_PRIMING_2024[ML] | IL18_2023[ML] | IL1b_BDNF_1993[ML] | Microvasc_2023[ML] | NEK7_2025[ML] | PSD_gut_2025[ML] | Plasticity_2018[ML] | Poda_2011[ML] | PrimingPrinc_2018[ML] | Prob_2020[ML] | Psoriase_2025[EC] | Quimio_meta82_2017[MA] | RepopIL6_2020[ML] | TGFb_2025[ML] | Th17_2025[ML]]

---

## BLOCO_04 — CÉLULAS E ESTRUTURAS: MICRÓGLIA, ASTRÓCITOS, BHE, VAGO E FRONTEIRAS IMUNES

### 4.1 — Subpopulações microgliais: homeostática, priming e DAM (BLOCO04.001)

A micróglia compreende estados funcionais distintos com identidade molecular. O estado **DAM (microglia associada a doença)** depende do eixo **TREM2–APOE**: uma assinatura transcricional APOE-dependente identifica micróglia disfuncional em modelos de ALS, esclerose múltipla e Alzheimer e ao redor de placas Aβ em cérebro humano (TREM2-APOE pathway drives dysfunctional microglia, 2017)[ML; camundongo+humano]. O sequenciamento mononuclear em camundongo e humano confirma populações DAM dependentes e independentes de TREM2 associadas à patologia (Human and mouse single-nucleus transcriptomics TREM2, 2020)[EC; humano+camundongo]. TREM2 é também receptor de fagocitose que limita o NLRP3 (TREM2 deficiency aggravates NLRP3/pyroptosis in Parkinson's, 2024)[ML; camundongo, ver BLOCO02.003]. Em depressão, o perfil DAM específico não está consolidado — a identidade molecular é transplantada da neurodegeneração [EXT], mas a existência de micróglia funcionalmente heterogênea é muito_estabelecido.

### 4.2 — Astrócitos reativos: chave molecular A1/A2 (BLOCO04.002)

Astrócitos reativos não são um estado único. Um trabalho de 2024 identificou uma **chave molecular** que separa reatividade neuroprotetora de neurotóxica: astrócitos de substância branca lesada diferenciam-se em populações C3+ e C3− (a simplificação anterior "A1/A2"), subdivisíveis por trajetórias de reparo (A molecular switch for neuroprotective astrocyte reactivity, 2024)[ML; camundongo]. O bloqueio da conversão ao fenótipo A1 neurotóxico (induzido por mediadores microgliais) é neuroprotetor em modelos de Parkinson, e agonistas GLP1R inibem essa conversão (Block of A1 astrocyte conversion is neuroprotective, 2018)[ML; camundongo+humano][EXT]. Em depressão, IL-6 derivada de micróglia pode induzir apoptose de astrócitos hipocampais (Microglia-derived IL-6 triggers astrocyte apoptosis hippocampus, 2025)[ML; camundongo]. A validação direta A1/A2 em TDM humana é fraca; o binário é [EXT] e hoje visto como continuum.

### 4.3 — Sinalização purinérgica P2X7/P2Y12 e estresse microglial (BLOCO04.003)

A comunicação micróglia–neurônio por ATP tem mecanismo direto ligado a depressão: a crença padrão era que ATP extracelular → P2X7 → montagem do NLRP3; um achado mais fino mostra que o ATP e o estresse aumentam **contatos retículo-mitocôndria (MAMs)** na micróglia, e essa plataforma media o comportamento tipo-depressivo (Augmented microglial ER-mitochondria contacts mediate depression-like behavior, 2024)[ML; camundongo]. P2X7 funciona como "sinal 2" do inflamassoma (Principles of inflammasome priming, 2018)[OB; revisão], enquanto P2Y12 marca o estado homeostático/ramificado e guia processos ao dano. Natureza: causal em camundongo para o eixo ATP/MAMs/NLRP3-comportamento; humano [EXT].

### 4.4 — Barreira hematoencefálica: componentes e disfunção por estresse (BLOCO04.004, 008)

A BHE é formada por endotélio com tight junctions (claudina-5, ocludina), pericitos e pés astrocitários. Os **pericitos regulam a BHE**: sua integridade é necessária para manter as junções e a baixa vesiculação endotelial (Pericytes regulate the blood-brain barrier, 2010)[ML; camundongo]. O achado mais relevante para depressão: estresse social crônico (derrota social em camundongo) induz **patologia neurovascular promotora de depressão** — reduz a tight junction claudina-5 (Cldn5), altera morfologia vascular e aumenta permeabilidade/passagem de sinais imunes periféricos (Social stress induces neurovascular pathology promoting depression, 2017)[ML; camundongo]. A BHE na neurodegeneração é revista com componentes celulares separados (BBB in Alzheimer's, 2017)[OB; revisão]. O pé astrocitário (unidade neurovascular) propaga o sinal endotélio→parênquima. Natureza: claudina-5/pericitos causal em animal; BHE na TDM humana [EXT]/emergente (ver marcadores sérios de BHE no BLOCO05).

### 4.5 — Nervo vago como via periferia→SNC (BLOCO04.005)

O nervo vago (80% fibras aferentes) detecta metabólitos da microbiota e sinais inflamatórios periféricos e os conduz ao SNC independentemente da BHE, na interface do eixo intestino-cérebro (Vagus nerve at microbiota-gut-brain axis, 2018)[OB; revisão]. Em humanos, a **estimulação vagal auricular transcutânea (taVNS)** aumenta conectividade amígdala–córtex pré-frontal dorsolateral e tem efeito anti-inflamatório na TDM (Neural networks and anti-inflammatory effect of taVNS in MDD, 2020)[EC; humano]. É a tradução clínica da via neural aferente (colinérgica anti-inflamatória). Natureza: via neural bem_suportado; taVNS como intervenção em depressão é moderadamente_suportado/emergente em humano.

### 4.6 — Populações imunes de fronteira: perivasculares, Treg, meníngeas (BLOCO04.006)

Além da micróglia parenquimal, macrófagos de borda (perivasculares/meníngeos) ocupam a interface SNC-periferia. Macrófagos perivasculares promovem clearance glinfático de Aβ pós-AVE por mecanismo próprio (Perivascular macrophage glymphatic Aβ clearance after stroke, 2025)[ML; camundongo]. Tregs periféricas têm fenótipos modificados em sofrimento psicológico pré-natal (Regulatory T-cell phenotypes in prenatal psychological distress, 2024)[EC; humano]. Estas populações são distintas da micróglia e acessíveis sem transposição completa da BHE. Natureza: mecanística em animal/humano; papel específico em depressão emergente. Oligodendrócitos/NG2-glia sob TNF/IFN-γ (claim 4.007) não receberam vínculo dedicado no lote (redução de densidade em CPF é herança do GPM/pós-morte Steiner) — fica para lote de célula glial.

### 4.7 — Estruturas cerebrais-alvo: ínsula, amígdala, accumbens (BLOCO04.009)

O sinal inflamatório atinge circuitos específicos. A taVNS modula conectividade **amígdala–CPFdl** (taVNS MDD, 2020)[EC; humano]. Probiótico (Bifidobacterium longum NCC3001, RCT) reduz escores de depressão e altera ativação cerebral em áreas límbicas em humanos com SII (Bifidobacterium longum NCC3001 reduces depression and alters brain activation, 2017)[EC; humano, RCT]. A ínsula/anterior é modulada por microglia em comportamento tipo-depressivo/ASD em camundongo (Anterior insular cortex depression-like/ASD via microglia, 2026)[ML; camundongo]. Accumbens e ínsula respondem a desafio inflamatório (ver Muscatell/fMRI no BLOCO05). Natureza: conectividade em humano bem_suportado para amígdala/Ínsula; causalidade circuito-específica em animal.

### 4.8 — Portas de entrada sem BHE: linfa meníngea, plexo coroide, glinfática (BLOCO04.010)

O SNC drena pela **glinfática** e por **vasos linfáticos meníngeos**, que afetam a resposta microglial e a imunoterapia (Meningeal lymphatics affect microglia responses and anti-Aβ immunotherapy, 2021)[ML; camundongo+humano]; a revisão de 2025 consolida como o "código imune" do cérebro (Glymphatics and meningeal lymphatics unlock brain-immune code, 2025)[OB; revisão, humano+animal]. O **plexo coroide** funciona como barreira e fonte de LCR e sinergiza com células imunes durante neuroinflamação (neutrófilos/monócitos acumulam no estroma; ChP regula inflamação meningítica) (Choroid plexus synergizes with immune cells during neuroinflammation, 2024)[ML; camundongo]. Essas portas permitem tráfego de sinal imune sem transposição completa da BHE — junto com área postrema/OVLT e vago, completam as rotas periferia→SNC. Natureza: estrutural bem_suportado; relevância psiquiátrica [EXT]/emergente.
---

[REF_BLOCO_04: A1block_2018[ML] | AstroSwitch_2024[ML] | Bifido_2017[EC] | Glinf_2025[ML] | IL6astro_2025[ML] | Insula_2026[ML] | MAMs_P2X7_2024[ML] | MenLinf_2021[ML] | PVM_2025[ML] | Pericitos_2010[ML] | Plexo_2024[ML] | SocialStress_BBB_2017[ML] | TREM2_APOE_2017[ML] | Treg_2024[EC] | Vago_2018[ML] | snRNA_TREM2_2020[ML] | taVNS_2020[EC]]

---

## BLOCO_05 — BIOMARCADORES PERIFÉRICOS E CENTRAIS

### 5.1 — Marcadores periféricos centrais: hs-CRP, IL-6, TNF-α, sTNFR2 (BLOCO05.004)

O alicerce do subtipo inflamatório é meta-analítico. A meta-análise seminal de citocinas na depressão maior demonstrou concentrações significativamente elevadas de TNF-α e IL-6 em deprimidos versus controles (Dowlati et al., 2010)[MA; humano]. A meta-análise de PCR, IL-1 e IL-6 confirmou associação positiva entre depressão e PCR/IL-6 em amostras comunitárias e clínicas (Howren et al., 2009)[MA; humano]. A meta-análise da rede de citocinas no sangue comparou esquizofrenia, bipolar e TDM e mostrou padrões distintos de alteração conforme estado clínico (Goldsmith et al., 2016)[MA; humano]. A meta-análise mais recente quantificou tanto diferenças de média quanto **variabilidade**, testando se só um subgrupo de pacientes tem elevação — Osimo et al. (2020/2021)[MA; humano] consolidam que as alterações são heterogêneas e concentram-se num subgrupo. A meta-análise de 82 estudos confirmou IL-6, TNF-α, CCL2 e outras citocinas elevadas na TDM (Leighton/quimiocinas, 2017)[MA; humano]. IL-6 também prediz pior resolução de sintomas em sofrimento psicológico (IL-6 predictor of symptom resolution, 2015)[EC; humano]. Diferenças sexuais na ligação inflamação-depressão são meta-analisadas, com efeito mais consistente em mulheres em alguns marcadores (Sex differences inflammation-depression meta-analysis, 2024)[MA; humano].

**Especificidade:** PCR é marcador de fase aguda (fígado, induzido por IL-6) — sensível mas inespecífico (sobe em obesidade, infecção, tabaco); IL-6 é mais próximo da fonte imune mas também pulsátil; TNF-α e **sTNFR2** (receptor solúvel) refletem ativação TNF crônica mais estável. A combinação >1 marcador aumenta especificidade doravante (ver 5.3). Marcadores de revisão recente consolidam mediadores inflamatórios em TDM e bipolar (Inflammatory mediators in depression and bipolar, 2024)[OB; humano].

### 5.2 — Razão KYN/TRP e marcadores da via da quinurenina (BLOCO05.001)

A **razão quinurenina/triptofano (KYN/TRP)** é o índice plasmático/sérico de atividade de IDO: inflamação desvia triptofano para quinurenina, elevando a razão. Em pacientes bipolares e deprimidos, níveis de citocinas e a razão KYN/TRP associam-se seletivamente a alterações de substância branca (KYN/TRP and white matter, 2022)[EC; humano]. Em tentadores de suicídio com TDM, quinurenina plasmática está elevada (Sublette et al., 2011)[EC; humano]. A ativação cerebral de IDO contribui para comportamento tipo-depressivo em modelo animal (Brain IDO depressive-like, 2017)[ML; camundongo], e o balanço quinurenínico hipocampal é rompido por inflamação periférica (Kynurenine balance hippocampus, 2016)[ML; camundongo]. O KYN/TRP é assim um marcador funcional (reflete atividade enzimática induzida por citocina), mais próximo do mecanismo que PCR, mas ainda periférico/indireto sobre o cérebro.

### 5.3 — Painel combinado e por que múltiplos marcadores (BLOCO05.003)

Nenhum marcador isolado é sensível e específico o bastante para definir o subtipo inflamatório, porque cada um captura um andar diferente: PCR (fase aguda hepática), IL-6 (citocina pivô, pulsátil), sTNFR2 (ativação TNF crônica), KYN/TRP (atividade de IDO/desvio triptofano). A heterogeneidade demonstrada pela meta-análise de variabilidade (Osimo et al., 2020)[MA] é a justificativa biológica para um painel: combinar um marcador upstream (PCR/IL-6) com um downstream (KYN/TRP) e um de estabilidade (sTNFR2) reduz falso-positivo por confundidores (obesidade, infecção — ver BLOCO08). A obesidade é um confundidor/mediador central da relação inflamação-depressão (Obesity and depression pathophysiotoxic relationship, 2025)[OB; revisão, humano].

### 5.4 — Marcadores centrais: TSPO-PET (BLOCO05.002)

O **TSPO (proteína translocadora de 18 kDa)** é alvo de PET que marca ativação glial in vivo. Em TDM, a densidade de TSPO está elevada em regiões cortico-límbicas (Setiawan et al., 2015)[EC; humano, PET] — primeira demonstração de neuroinflamação central em pacientes vivos. O TSPO no córtex cingulado anterior está elevado na depressão maior e relacionado a ideação suicida (Holmes et al., 2018)[EC; humano, PET]. Ressalva técnica crítica: TSPO tem polimorfismo rs6971 (ligante de baixa/alta afinidade) que exige genotipagem, e TSPO não é exclusivo de micróglia (astrócitos também expressam) — é marcador de ativação glial, não de "micróglia" pura. Mecanisticamente, o TSPO revela que a ativação é central e não só periférica, mas não separa pró de anti-inflamatório.

### 5.5 — Biomarcadores secundários: S100B, neopterina, LBP, resolvina D1 (BLOCO05.005)

- **S100B sérico:** proteína glial (astrócito) usada como marcador de integridade da BHE/dano glial; níveis séricos elevados são relatados em depressão (Serum S100B in depression, 2019)[OB; humano] e propostos como marcador substituto em burnout/depressão (S100B surrogate burnout/depression, 2016)[EC; humano]. Após TCE, S100B cai (S100B after ECT, 2022)[EC; humano]. Especificidade baixa (sobe em qualquer dano glial/BHE); papel dual por concentração (BLOCO02.24).
- **Neopterina:** marcador de ativação de macrófago/IFN-γ (co-produto da via BH4); medida com IL-6/KYN em contexto cirúrgico/inflamatório (Neopterin/IL-6 surgery, 2014)[EC; humano] — reflecte ativação imune celular, menos validada em TDM.
- **LBP/endotoxina sérica:** marcador indireto de translocação bacteriana/permeabilidade (cross-ref B7); a busca dedicada não retornou validação forte em TDM neste lote — fica como candidato [EXT].
- **Resolvina D1 plasmática:** mede o lado da resolução (SPMs); a busca do lote não retornou ensaio clínico robusto em depressão — hipótese mecanística (BLOCO02.13), gap de pesquisa.

### 5.6 — Biomarcadores centrais no líquor e pós-morte (BLOCO05.006)

No SNC, o achado mais forte é o **ácido quinolínico microglial**: depressão grave associa-se a QUIN elevado em subregiões do córtex cingulado anterior (Steiner et al., 2011)[EC; pós-morte/tecidos humanos] — popular de suicídio com alta inflamação, não "TDM geral" (qualificador obrigatório). Marcadores gliais no LCR (sTREM2, YKL-40) têm associação longitudinal com depressão e disponibilidade de transportador de dopamina em Parkinson (CSF glial markers YKL-40 depression, 2024)[EC; humano, LCR] — sugerindo que marcadores de ativação glial no líquor preveem fenótipo depressivo. IL-6/QUIN/YKL-40 no LCR são mais próximos do tecido cerebral que marcadores séricos, mas invasivos e de baixa disponibilidade.

### 5.7 — Neuroimagem complementar: conectividade, MRS (mio-inositol), volume hipocampal (BLOCO05.007)

Além do TSPO-PET, três camadas de imagem complementam o quadro: **conectividade funcional córtico-estriatal** e cortico-límbica modificada por inflamação (taVNS altera amígdala-CPFdl, BLOCO04); **mio-inositol por MRS** como marcador glial in vivo; e **volume hipocampal**, que se associa a inflamação e desfecho terapêutico — após ECT, marcadores inflamatórios (IL-6/TNF) relacionam-se a volume hipocampal e resposta (Inflammation, hippocampal volume and ECT outcome, 2020)[EC; humano]. Estes marcadores não medem inflamação diretamente, mas capturam suas consequências estruturais/funcionais, e combinados ao TSPO aumentam a caracterização do subtipo.
---

[REF_BLOCO_05: BrainIDO_2017[ML] | Dowlati_2010[MA] | Goldsmith_2016[MA] | HippVol_ECT_2020[EC] | Holmes_2018[EC] | Howren_2009[MA] | IL6resol_2015[EC] | KYNTRP_WM_2022[EC] | Obesidade_2025[EC] | Osimo_2020[MA] | Quimio82_2017[MA] | S100B_burnout_2016[EC] | S100B_dep_2019[EC] | Setiawan_2015[EC] | SexDiff_2024[MA] | Steiner_2011_QUIN[EC] | Sublette_2011[EC] | YKL40_2024[EC]]

---

## BLOCO_06 — TRADUÇÃO CLÍNICA: DO MECANISMO AO SINTOMA

### 6.1 — Por que o SSRI não reverte o efeito da citocina sobre BDNF/CREB (BLOCO06.001)

Os antidepressivos monoaminérgicos atuam sobre disponibilidade de monoaminas, mas a citocina ataca um elo a jusante diferente: IL-1β/TNF suprimem BDNF/TrkB/CREB e plasticidade sináptica (ver BLOCO03.001/002) — um mecanismo que não é contornado apenas por aumentar serotonina sináptica. Em linhagens celulares humanas (linfoblastos) de pacientes deprimidos, biomarcadores de resposta a antidepressivo distinguem remitters de não-remitters, sugerindo que a resposta ao fármaco depende do estado imune/transcricional basal (Depression and antidepressant-response biomarkers in human lymphoblasts, 2021)[EC; humano]. Isso explica por que, no subgrupo inflamado, a falha ao SSRI é mais comum (a inflamação "sabota" os mecanismos de ação do antidepressivo, como o próprio RCT do infliximabe enquadra — Raison et al., 2013)[EC; humano]. Plasticidade sináptica e antidepressivos de ação rápida são revista nesta interface (Synaptic plasticity and depression/rapid-acting antidepressants, 2016)[OB; revisão, humano]. Natureza: mecanística em célula/humano; bem_suportado que inflamação alta prediz não-resposta.

### 6.2 — Gradiente de severidade: dose-resposta biológica (BLOCO06.002)

Existe relação entre magnitude da ativação inflamatória e intensidade/alcance do sintoma: níveis mais altos de marcadores associam-se a sintomas mais graves e a pior resolução (IL-6 baixa prediz melhor resolução de sintomas em sofrimento psicológico — IL-6 predictor, 2015)[EC; humano]. A meta-análise de variabilidade (Osimo et al., 2020)[MA; humano] mostra que não há "deprimido inflamado" binário — a elevação é contínua e concentrada num subgrupo, e o risco/intensidade escalam com o marcador. A progressão do sickness agudo (autolimitado) para o comportamento depressivo persistente acompanha a persistência/amplitude do sinal citocínico (Dantzer, ver BLOCO01). Natureza: gradiente associativo bem_suportado em humano.

### 6.3 — Depressão induzida por interferon-α: paradigma causal humano (BLOCO06.003)

O modelo mais próximo de causalidade direta em humanos é a terapia com **IFN-α** (hepatite C/melanoma): um indutor inflamatório exógeno precipita sintomas depressivos de novo em indivíduos sem transtorno de humor prévio, com cronologia previsível (semanas) e fenomenologia característica. Análise dimensional dos sintomas em pacientes com melanoma mostra clusters neuropsiquiátricos específicos que emergem ao longo dos primeiros três meses e são prevenidos/revertidos por paroxetina (Neurobehavioral effects of interferon-alpha in cancer patients, 2002)[EC; humano]. O mecanismo bioquímico inclui queda de triptofano sérico associada aos sintomas depressivos (Decreased serum tryptophan and depressive symptoms during cytokine therapy, 2002)[EC; humano] — consistente com indução de IDO/desvio quinurenínico. A inflamação por IFN-α também reduz o feedback negativo de glicocorticoide (resistência ao eixo HPA), ligando inflamação à disfunção do estresse (IFN-α inflammation and reduced glucocorticoid negative feedback, 2016)[EC; humano]. Revisões clínicas consolidam hepatite C/IFN-α e depressão (Hepatitis C, interferon alfa, and depression, 2000)[OB; humano, sem abstract — texto completo]. Natureza: causal humano (intervenção), muito_estabelecido.

### 6.4 — Subtipo anedônico e circuito de recompensa (BLOCO06.004)

A inflamação impacta seletivamente o **circuito de recompensa córtico-estriatal ventral**, produzindo anedonia. Em TDM, inflamação elevada associa-se a baixa conectividade funcional nos circuitos cortico-estriatais de recompensa e a sintomas de anedonia — relação que envolve impacto da inflamação sobre síntese/liberação de dopamina (Functional connectivity in reward circuitry and anhedonia as therapeutic target, 2022)[EC; humano, fMRI]. Em mulheres expostas a trauma, PCR/citocinas elevadas associam-se a alteração do circuito de recompensa e a anedonia/sintomas de TEPT (Inflammation, reward circuitry and anhedonia/PTSD in trauma-exposed women, 2020)[EC; humano, fMRI]. Este é o embrião do "subtipo anedônico-inflamatório": inflamação → redução de conectividade córtico-estriatal ventral → anedonia, com análogo animal no comportamento de não-preferência. O desafio experimental com endotoxina (LPS humano) reproduz alterações de recompensa/anedonia transitória [EC; revisão]. Natureza: associativo/neural em humano, bem_suportado; causalidade via desafio endotoxinal e IFN.

### 6.5 — Nota de escopo clínico

Este bloco descreve mecanismos de tradução e estratificação biológica, não conduta. Não há recomendação de dosagem de anti-inflamatório/biológico para depressão fora das bibliotecas de Intervenções; o RCT do infliximabe (BLOCO05, 09.3) é prova de conceito de estratificação por biomarcador, com resultado primário negativo na amostra total.
---

[REF_BLOCO_06: IFN_HPA_2016[EC] | IFNcancer_2002[EC] | IL6resol_2015[EC] | LCL_biom_2021[EC] | Osimo_meta[MA] | PlastDep_2016[EC] | RCT_infliximab[EC] | RewardTrauma_2020[EC] | Reward_2022[EC] | Trp_2002[EC]]

---

## BLOCO_07 — NÓS MOLECULARES CENTRAIS (síntese)

> Não gera query própria. Sintetiza claims já aprovados nos BLOCOs 02/03/08. Critério de "nó central": (1) está a montante de múltiplas vias; (2) recebe convergência de gatilhos distintos; (3) tem prova de manipulação causal; (4) conecta marcador periférico a mecanismo central.

### 7.1 — NF-κB como nó central candidato (BLOCO07.001)

O **NF-κB** atende aos quatro critérios e é o principal candidato a nó molecular central da neuroinflamação B1:

1. **Montante de múltiplas vias:** NF-κB é o saída transcricional comum de TLR4/MyD88, TNFR1 e IL-1R1 — via IRAK/TRAF6→IKK→degradação de IκBα→translocação nuclear — dirigindo a transcrição de IL1B, IL6, TNF, do próprio NLRP3 (priming), PTGS2/COX-2 e NOS2/iNOS (BLOCO02.015, PMID gastrodina/punicalina)[ML].
2. **Convergência de gatilhos distintos:** PAMPs (LPS bacteriano/translocação intestinal B7), DAMPs (HMGB1, S100, mtDNA), citocinas e estresse psicológico todos convergem em NF-κB (BLOCO02.004/008/009/08.005).
3. **Prova causal por manipulação:** inibição farmacológica da cascata TLR4/TRAF6/NF-κB reduz neuroinflamação, ativação microglial e prejuízo comportamental em modelos (BLOCO02.015)[ML; camundongo]; resistência a glicocorticoide desinibe NF-κB (BLOCO08.001, GR reprime genes inflamatórios gene-especificamente)[ML/EC].
4. **Ligação marcador↔mecanismo:** NF-κB é o elo que transforma sinal imune periférico (PCR/IL-6 elevados) em transcrição central de citocinas, IDO (quinurenina), COX-2/PGE2 e priming do NLRP3 — fechando o caminho do marcador de sangue ao sintoma (anedonia, BLOCO06).

### 7.2 — NLRP3 como segundo nó (executor)

Se NF-κB é o nó transcricional, o **inflamassoma NLRP3** é o nó executor a jusante: recebe o priming de NF-κB e o "sinal 2" (ATP/P2X7, mtROS/MAMs, K+, cristais, mtDNA via cGAS-STING) e produz IL-1β/IL-18 maduros e piroptose GSDMD (BLOCO02.001, 08.006/009). Prova causal forte: variantes humanas ganho-de-função geram inflamassoma constitutivo (CAPS)[EC humano]; inibidores e a deleção reduzem dano; NEK7 modula o complexo e alivia comportamento depressivo em rato ()[ML].

### 7.3 — Relação entre os dois nós e o subtipo

NF-κB (transcrição/priming) e NLRP3 (execução/piroptose) formam um eixo de dois estágios, contido por freios (IL-10/STAT3, miR-146a, SPMs, GR) e amplificado por loops (B6/ROS, B9/mitocôndria, B2/resistência a glicocorticoide). A falha dos freios + persistência de gatilhos (obesidade, trauma, disbiose, sono) cronifica o eixo — substrato do subtipo "depressão inflamatória" (BLOCO11). Ambos os nós são mecanísticos em animal/célula; em humanos o fechamento causal vem de marcadores (PCR/IL-6/KYN-TRP/TSPO), genética (Bull IL-6, FKBP5) e intervenção de prova (IFN-α, infliximabe no subgrupo).
---

[REF_BLOCO_07: CAPS_2024[EC] | GR_repress_2018[ML] | Gastrodin_2024[ML] | NEK7_2025[ML] | Swanson_2019[ML] | cGAS_POCD_2024[ML]]

---

## BLOCO_08 — CONEXÕES BIDIRECIONAIS E LOOPS (B1 ↔ B2…B14)

> Cada conexão aponta o mecanismo-alvo (cross-ref). O foco aqui é o ELO molecular; a biologia completa do mecanismo parceiro reside na biblioteca dele (regra de fronteira).

### 8.1 — B1→B2: resistência a glicocorticoides (NF-κB/GR/FKBP5) (BLOCO08.001)

O glicocorticoide ativado (GR) reprime potemente a inflamação de macrófagos; análise genômica mostra que o GR reprime genes pró-inflamatórios por mecanismos gene-específicos (genes "pausados" prontos para transcrição, controlados por NELF/Pol2) (GR-driven repression of inflammatory genes, 2018)[ML; célula/camundongo]. Quando FKBP5 está elevada/desmetilada (Klengel 2013, BLOCO02.20) ou a citocina sinaliza NF-κB de forma sustentada, o GR perde eficácia repressora — a resistência a glicocorticoides desinibe o NF-κB, fechando loop. A inflamação por IFN-α reduz o feedback negativo do HPA em humanos (IFN-α glucocorticoid negative feedback, 2016)[EC; humano]. Biologia de FKBP e sinalização inflamatória é revista (FKBP and inflammation, 2020)[OB; revisão]. Cross-ref: **mecanismo_B2_eixo_hpa_cortisol**.

### 8.2 — B1→B3: citocinas suprimem BDNF/CREB e complemento faz poda (BLOCO08.002, 003)

IL-1β/TNF suprimem BDNF/TrkB/CREB (ver BLOCO03.001/002; IL-1β reduz mRNA de BDNF hipocampal, 1993)[ML]. Paralelamente, a **poda sináptica mediada por complemento C1q/C3** pela micróglia é necessária ao desenvolvimento (Microglia sculpt circuits in complement-dependent manner, 2012)[ML; camundongo], mas quando excessiva no adulto é candidata a perda sináptica na depressão: a disbiose intestinal induz comportamento tipo-depressivo via poda anormal dependente de complemento (Gut dysbiosis depression-like via complement C3, 2024)[ML; camundongo], e a inibição de PDE4 alivia poda fagocítica excessiva mediada por HMGB1/C1q/C3 (PDE4 inhibition HMGB1/C1q/C3 pruning, 2025)[ML; camundongo]. Cross-ref: **mecanismo_B3_neuroplasticidade**.

### 8.3 — B1↔B6/B9: ROS/mtDNA amplificam o NLRP3 (BLOCO08.004, 006)

Espécies reativas e disfunção mitocondrial alimentam o "sinal 2" do NLRP3: mtROS e vazamento de mtDNA ativam tanto o inflamassoma quanto cGAS-STING (BLOCO02.018), e a resposta inflamatória por sua vez gera mais dano mitocondrial — loop B1→B6 (estresse oxidativo)→B9 (disfunção mitocondrial)→B1. Os contatos retículo-mitocôndria (MAMs) na micróglia medeiam comportamento tipo-depressivo (BLOCO04.003)[ML; camundongo]. Cross-ref: **B6_estresse_oxidativo**, **B9_disfuncao_mitocondrial**.

### 8.4 — B1↔B7: LPS-TLR4 periférico e translocação (BLOCO08.005)

Estresse psicológico compromete a barreira intestinal, permitindo translocação bacteriana (LPS) que ativa TLR4 periférico e central: LPS derivado do intestino e TLR4 periférico medeiam inflamação no estresse (Gut-derived LPS and peripheral TLR4 in stress, 2024)[ML; camundongo], e a estimulação da via TLR4 cerebral no estresse crônico é relevante para depressão (Brain TLR4 pathway stimulation in stress, 2011)[ML; rato]. Disbiose agrava depressão pós-AVE via NLRP3 microglial (BLOCO03/04). Cross-ref: **B7_eixo_intestino_cerebro**.

### 8.5 — B1→B4: SERT/p38 MAPK e dopamina de recompensa (BLOCO08.007)

Citocinas aumentam atividade/expressão do transportador de serotonina (SERT) via p38 MAPK, reduzindo serotonina sináptica — eixo que conecta inflamação à monoamina. Em paralelo, IFN-α/inflamação reduzem disponibilidade de dopamina em circuitos de recompensa, produzindo anedonia (ver BLOCO06.004: conectividade córtico-estriatal e anedonia)[EC; humano]. Cross-ref: **B4_deficiencias_monoaminas**. (O vínculo SERT/p38 específico não teve artigo dedicado no lote; mecanismo herdado do GPM.)

### 8.6 — B1→B5: glutamato glial e EAAT2 (BLOCO08.008)

Citocinas deprimem o transportador de glutamato EAAT2/GLT-1 astrocitário e promovem liberação de glutamato via hemicanais (conexina/panexina), com redução de glutamina sintetase — levando a glutamato extracelular excessivo e excitotoxicidade. A privação de sono induz ansiedade via IL-6 e eixo astrócito-GABA no PAG (Sleep deprivation IL-6 astrocyte-GABA PAG, 2026)[ML; camundongo], ilustrando modulação glial do neurotransmissor. Cross-ref: **B5_gaba_glutamato**. (Vínculo EAAT2 dedicado não veio no top do lote; mecanismo do GPM.)

### 8.7 — B1→B8: vitamina D/VDR, zinco/NLRP3, magnésio/NF-κB (BLOCO08.009)

Micronutrientes modulam a ativação imune: vitamina D/VDR modula ativação microglial (Vitamin D as a modulator of neuroinflammation, 2024)[OB; revisão, humano+animal]. Zinco regula NLRP3 e magnésio inibe NF-κB (mecanismos do GPM; sem vínculo PMID dedicado neste lote). Cross-ref: **B8_deficiencias_micronutrientes**.

### 8.8 — B1→B10: sono, relógio e NLRP3 (BLOCO08.010)

Privação de sono eleva IL-6/TNF/PCR: privação aguda de sono exacerba inflamação sistêmica e distúrbios psiquiátricos (Acute sleep deprivation systemic inflammation, 2023)[ML; camundongo], e sono perdido induz ansiedade via IL-6 (IL-6 astrocyte PAG, 2026)[ML]. Genes do relógio (BMAL1/CLOCK/PER) regulam o limiar do NLRP3 e a fagocitose microglial varia no ciclo claro-escuro (crosstalk ritmo-imune). Cross-ref: **B10_desregulacao_circadiana**.

### 8.9 — B1→B11: desiodase tipo 2 (D2) e tireoide (BLOCO08.011)

LPS induz a desiodase tipo 2 (D2) em tanicitos do hipotálamo mediobasal — a principal enzima que converte T4 em T3 ativo no SNC (LPS induces D2 in mediobasal hypothalamus, 2004)[ML; rato/humano], e o gene dio2 humano tem elemento responsivo a NF-κB (NF-κB responsiveness of human dio2, 2006)[ML]. Assim a inflamação altera o metabolismo tireoidiano central (síndrome do eutireoideo doente). Cross-ref: **B11_disfuncao_tireoidiana**.

### 8.10 — B1→B12: trauma precoce, FKBP5 e priming (BLOCO08.012)

Adversidade na infância faz priming microglial e marca FKBP5: desmetilação alelo-específica dependente de trauma (Klengel 2013, BLOCO02.20) e efeitos intergeracionais na metilação de FKBP5 em sobreviventes do Holocausto e seus filhos (Holocaust intergenerational FKBP5 methylation, 2016)[EC; humano]. FKBP5 é nó compartilhado trauma↔inflamação; TEPT tem marcadores inflamatórios elevados. Cross-ref: **B12_neurobiologia_trauma**.

### 8.11 — B1→B13: endocanabinoides (CB2/FAAH/MAGL) (BLOCO08.013)

O receptor CB2 microglial tem efeito anti-inflamatório compensatório, e metabólitos de FAAH/MAGL alimentam a via de prostaglandinas (crosstalk com 2.17). Não retornou artigo PMID dedicado no top do lote; mecanismo herdado do GPM. Cross-ref: **B13_sistema_endocanabinoide** — gap de busca.

### 8.12 — B1→B14: esteroides neuroativos (alopregnanolona, estrogênio) (BLOCO08.014)

Alopregnanolona tem efeito anti-inflamatório microglial, e estrogênio/17β-estradiol derivado do cérebro (BDE2) modula ativação glial com diferenças entre sexos (Brain-derived estrogen and neurological disorders, 2022)[OB; revisão] — consistente com as diferenças sexuais na ligação inflamação-depressão (BLOCO05, meta 2024). Cross-ref: **B14_esteroides_neuroativos**.
---

[REF_BLOCO_08: D2_LPS_2004[ML] | Estrogen_2022[ML] | GR_repress_2018[ML] | GutC3_2024[ML] | GutLPS_2024[ML] | Holocausto_2016[EC] | IFN_HPA_2016[EC] | IL1b_BDNF_1993[ML] | Klengel_2013[EC] | MAMs_2024[ML] | PDE4_2025[ML] | Poda_2012[ML] | Reward_2022[EC] | SleepIL6_2026[ML] | SleepInflam_2023[ML] | TLR4brain_2011[ML] | VitD_2024[ML] | dio2_NFkB_2006[ML]]

---

## BLOCO_09 — IMPACTO DA NEUROINFLAMAÇÃO SOBRE NEUROPLASTICIDADE (elo B1→B3)

> Regra de fronteira: a biologia da plasticidade (LTP/LTD, BDNF, AMPA) reside em B3; aqui fica o ELO da citocina sobre ela.

### 9.1 — Citocinas sobre LTP/LTD hipocampal (BLOCO09.001)

IL-1β e TNF-α, em níveis fisiológicos, modulam plasticidade; quando elevados na neuroinflamação, deprimem LTP e favorecem LTD no hipocampo. IL-1 é regulador central da resposta de estresse e a produção cerebral de IL-1 liga o desafio imunológico/psicológico à ativação neuroendócrina e à plasticidade (Interleukin-1: a central regulator of stress responses, 2009)[OB; revisão, humano+animal]. A revisão de ativação glial em transtornos mentais consolida que citocinas interferem com plasticidade sináptica e memória (Neuroinflammation and glial activation in mental disorders, 2020)[OB; revisão]. O mecanismo molecular é a supressão de BDNF/CREB (BLOCO03.001: IL-1β reduz mRNA de BDNF hipocampal, 1993)[ML; rato]. Natureza: causal em fatia/animal; em humanos por marcadores e desfecho cognitivo.

### 9.2 — Remodelamento dendrítico e reversibilidade (BLOCO09.002)

Ativação inflamatória induz retração dendrítica e perda de espinhas, com componente de dano sinaptodendrítico. Microglia controla sinapses glutamatérgicas no hipocampo adulto: a depleção farmacológica de microglia altera a transmissão CA3-CA1, demonstrando regulação contínua da sinapse pela glia (Microglia control glutamatergic synapses in adult hippocampus, 2022)[ML; camundongo]. Em HIV, dano sinaptodendrítico cortical é regulado por opioides e quimiocinas mesmo sem morte neuronal (Synaptodendritic damage in HIV, 2019)[EC; humano+animal] — modelo de dano reversível por modulação imune. A reversibilidade após normalização da inflamação é consistente com a melhora de marcadores/cognição após anti-inflamatório/antidepressivo, mas o vínculo direto de reversibilidade dendrítica em TDM humana é [EXT]/emergente.

### 9.3 — TNF-α e scaling sináptico homeostático (BLOCO09.003)

Além do LTP/LTD (ajuste rápido de sinapses individuais), existe o **scaling sináptico homeostático** — ajuste lento e multiplicativo da força global de sinapses para manter a atividade neural em faixa. Esse scaling é mediado por **TNF-α glial**: o TNF derivado da glia ajusta a força de receptores AMPA na membrana para estabilizar a atividade da rede (Synaptic scaling mediated by glial TNF-alpha, 2006)[ML; camundongo/rato, Nature]. É um papel FISIOLÓGICO do TNF — quando a inflamação crônica desregula esse sinal, o mecanismo homeostático deixa de estabilizar e passa a contribuir a disfunção de circuito. Distingue-se do LTP/LTD (9.1) e do remodelamento dendrítico (9.2): o scaling é glia-dependente e homeostático, não hebbiano. Natureza: mecanismo clássico muito_estabelecido em animal; relevância para depressão é inferida [EXT].
---

[REF_BLOCO_09: GliaMental_2020[ML] | HIVdend_2019[ML] | IL1_stress_2009[ML] | IL1b_BDNF_1993[ML] | MicrogliaGlut_2022[ML] | TNFscaling_2006[ML]]

---

## BLOCO_10 — IMPACTO SOBRE A NEUROGÊNESE ADULTA (elo B1→B16; condicional)

> Regra P16: a biologia completa da neurogênese adulta reside na biblioteca **B16 (neurogênese)**. Aqui fica apenas o ELO das citocinas sobre proliferação/sobrevivência de células-tronco neurais (NSC) no giro denteado — 1–2 frases por ponto, com referência cruzada.

### 10.1 — IL-6 suprimindo proliferação de NSC (BLOCO10.001)

Citocinas pró-inflamatórias deprimem a neurogênese hipocampal adulta. O ambiente inflamatório e a ativação microglial alteram o destino das NSC; a maquinaria de IFN-α/IL-6 em células-tronco neurais está documentada na depressão induzida por citocinas (Mechanisms for IFN-α-induced depression and neural stem cell dysfunction, 2014)[ML; célula, BLOCO02.16] — IL-6/STAT3 em contexto inflamatório sustém o estado antiproliferativo, ainda que IL-6 trans-sinalizante seja reparativo em microglia (BLOCO03.003, dualidade). O efeito sobre NSC do giro denteado é supressivo na inflamação crônica [ML; EXT]. Cross-ref: **mecanismo_B16_neurogenese**.

### 10.2 — IL-1β e TNF-α suprimindo proliferação/sobrevivência de NSC (BLOCO10.002)

IL-1 é regulador central da resposta de estresse e da função neural (Interleukin-1 central regulator of stress responses, 2009)[OB; revisão, humano+animal]; IL-1β e TNF ativam NF-κB nas NSC e reduzem proliferação/sobrevivência de novos neurônios do giro denteado — elo causal distinto e complementar ao do IL-6. Em modelo, estresse crônico/inflamação reduz neurogênese e intervenções anti-inflamatórias a restauram [ML; EXT]. Cross-ref: **B16** (fases da neurogênese em detalhe).

### 10.3 — Microglia homeostática/IL-4 como contraponto pró-neurogênico (BLOCO10.003)

Nem toda glia inibe: a microglia em fenótipo anti-inflamatório (M2/Th2) SUPORTA a neurogênese. Vesículas extracelulares derivadas de microglia M2 modulam o destino das NSC após isquemia, promovendo neurogênese (M2 microglia-derived small extracellular vesicles modulate NSC fate, 2025)[ML; camundongo]. TREM2 polariza microglia para M2 e melhora neurogênese (TREM2 improves neurogenesis, 2025)[ML; camundongo], e o eixo IL-4/STAT6 reverte defeito proliferativo em células-tronco neurais humanas (IL-4/STAT6 reverses proliferative defect, 2024)[EC; humano]. É o contraponto compensatório aos elos supressivos: o sinal imune tem duas faces sobre NSC, dependendo do fenótipo glial. Natureza: pró-neurogênico M2/IL-4 bem demonstrado em animal/célula humana; contexto depressão [EXT].
---

[REF_BLOCO_10: IFN_NSC_2014[ML] | IL1_stress_2009b[ML] | IL4_STAT6_2024[EC] | M2ves_2025[ML] | TREM2_2025[ML]]

---

## BLOCO_11/12 — ESTRATIFICAÇÃO E CENÁRIOS (condicional; síntese)

> Este bloco só existe na medida em que há subtipos biologicamente documentados. Depende dos BLOCOs 02–09 já triados; não gera query própria. Conteúdo de conduta clínica/dosagem permanece nas bibliotecas de Intervenções.

### 11.1 — Substrato mecanístico do subtipo "depressão inflamatória" (BLOCO11.001)

Aproximadamente **27%** dos pacientes com depressão apresentam PCR >3 mg/L, com razão de chances ~1,46 para inflamação de baixo grau versus controles (achado epidemiológico da trilha SM; a meta de Osimo 2020 confirma que a elevação é de um SUBGRUPO e não universal — ver BLOCO05)[MA; humano]. O substrato mecanístico deste subtipo é a **ativação sustentada do eixo NF-κB→NLRP3** (BLOCO07) com: (a) marcadores periféricos elevados (PCR, IL-6, sTNFR2) e índice KYN/TRP desviado (BLOCO05.001/004); (b) sinal central (TSPO-PET elevado em córtex cingulado/ínsula; QUIN pós-morte em subregião cingulada — BLOCO05.002/006); (c) assinatura neural de anedonia (baixa conectividade córtico-estriatal ventral; BLOCO06.004); e (d) modificabilidade por intervenção anti-TNF exclusivamente quando o marcador basal está alto (RCT infliximabe: negativo na amostra toda, positivo no subgrupo inflamado — BLOCO05/09.3)[RCT; humano].

A estratificação por biomarcador (painel combinado PCR+IL-6+sTNFR2+KYN/TRP, BLOCO05.003) é o que dá especificidade — o subtipo não é diagnosticável por um marcador único nem por sintoma isolado, e a inflamação NÃO está elevada na maioria dos pacientes.

### 11.2 — Candidatos futuros (NÃO convertidos em claim formal agora)

Conforme a nota da Lista Canônica, estes subtipos aguardam que o bloco seja priorizado e ganhem item formal só com documentação biológica:
- **Depressão resistente ao tratamento (TRD):** perfil TNF/sTNFR2/PCR mais elevado que a depressão responsiva; inflamação prediz não-resposta a SSRI (BLOCO06.001).
- **Depressão perinatal:** disfunção do ajuste imunológico gestacional; Treg/Th17 (BLOCO04.006).
- **TEPT com fenótipo pró-inflamatório:** elevação consistente IL-6/TNF/PCR associada a trauma infantil; FKBP5 como nó compartilhado (BLOCO08.012, Klengel/Holocausto).
- **Depressão tardia/geriátrica:** componente de senescência glial/SASP e priming (BLOCO02.014, inflamm-aging) — hipótese inicial.

Estes permanecem como `gap_pesquisa`/candidatos, sem vínculo de assertividade forte nesta Rodada 2.

### 11.3 — Nota de escopo

TOC (transtorno obsessivo-compulsivo) fica FORA do escopo central (capítulo próprio do DSM); o exame Y-BOCS entra apenas para rastreio/diferencial de comorbidade, conforme o protocolo de escopo. Este bloco descreve estratificação biológica e não recomendação de tratamento; dosagem/posologia de anti-inflamatórios ou biológicos pertencem às bibliotecas de Intervenções e Suplementos.
---

[REF_BLOCO_11: Bull_2009[EC] | Osimo_2020[MA] | RCT_infliximab[EC] | Reward_2022[EC] | Setiawan_2015[EC] | Steiner_2011_QUIN[EC] | Treg_2024[EC]]

---

## BLOCO_12 — CENÁRIOS CLÍNICOS ILUSTRATIVOS

**Status: N/A nesta Rodada 2.**
O BLOCO_12 depende de subtipos clínicos biologicamente documentados no BLOCO_11. O BLOCO_11 descreve o substrato mecanístico do subtipo "depressão inflamatória" e lista candidatos futuros (TRD, perinatal, TEPT, geriátrica), mas estes ainda não foram convertidos em subtipos formais com cenário próprio — decisão registrada na Lista Canônica (nota de candidatos futuros). Portanto, em conformidade com a regra de dependência arquitetural, o BLOCO_12 é declarado **N/A — a desenvolver quando os subtipos do BLOCO_11 forem formalizados**. Nenhum conteúdo terapêutico (fármaco/protocolo/conduta) é inserido aqui, por design.

[REF_BLOCO_12: —]


---

## TABELA DE EVIDÊNCIAS

Agrupada por afirmação/tipo de desenho. `forca_evidencia_afirmacao` reflete o corpo de evidência por afirmação (não o rótulo do desenho).

| Tipo de estudo | Principais resultados | Tamanho de efeito | Limitações | forca_evidencia_afirmacao (alto\|medio\|baixo) |
|---|---|---|---|---|
| Meta-análise | Citocinas elevadas na TDM: IL-6, TNF-α, PCR (Dowlati; Howren; Goldsmith; Osimo; 82 estudos); heterogeneidade concentrada em subgrupo | Diferenças de média positivas consistentes (IL-6/TNF/PCR); ~27% com PCR>3 (OR~1,46) | Medição periférica, confundidores (obesidade, sono, medicação), publicação | alto |
| Meta-análise | Diferenças sexuais na ligação inflamação-depressão | Efeito mais consistente em mulheres em parte dos marcadores | Heterogeneidade, poucos estudos estratificados | medio |
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
- TSPO-PET: o polimorfismo rs6971 (ligante baixa/alta afinidade) e a expressão em astrócitos além de micróglia tornam "TSPO = micróglia ativada" impreciso entre estudos não genotipados.

**Limitações dos modelos animais**
- [APENAS PRÉ-CLÍNICO] Cascata NLRP3/GSDMD/poda e priming demonstrados por manipulação em camundongo/ratos/célula; a tradução para depressão humana é por analogia [EXT]. Comportamento "tipo-depressivo" animal (suspensão por cauda, preferência por sacarose) não equivale ao quadro humano.

**Subgrupos não identificados**
- TRD (resistente), depressão perinatal, TEPT pró-inflamatório, depressão geriátrica/senescente, e diferenças por sexo estão listados como candidatos (BLOCO_11) sem formalização; cada um pode ter eixo imune distinto.

**Vieses de publicação identificados**
- Viés de publicação positivo em estudos de citocinas; revisões de composto (polifenóis, fitoterápicos) nos resultados de busca tendem a relatar efeitos benéficos. As meta-análises (Osimo, Howren) atenuam parcialmente, mas conflito de interesse e pequenos estudos persistem.

**Lacunas de busca (registradas no inventário negativo)**
- RLRs (RIG-I/MDA5) diretos no SNC; miR-155/SOCS1 comportamental; oligodendrócitos/NG2 sob TNF/IFN-γ em CPF; SERT/p38 MAPK; EAAT2/GLT-1; zinco/NLRP3 e magnésio/NF-κB; CB2/FAAH/MAGL; LBP/endotoxina e resolvina D1 plasmáticas em TDM; estimulação de CRH por PGE2 — todos sem vínculo PMID dedicado neste lote (herdados do GPM ou gap de pesquisa).

---

## ELEMENTOS MOLECULARES CRÍTICOS

```
Molécula/Gene/Receptor/Proteína: NLRP3
UniProt ID:    Q96P20
Gene (HGNC):   NLRP3
HMDB ID:       null
Função fisiológica normal: sensor do inflamassoma; monta complexo ASC/caspase-1 após priming (NF-κB) + sinal 2
Alteração em ansiedade: ↑ ativação (emergente)
Alteração em depressão: ↑ ativação em subgrupo inflamado (marcadores/genética)
Células/estruturas onde atua: micróglia, macrófagos, monócitos, astrócitos
Vias moleculares associadas: NF-κB (priming); caspase-1/GSDMD (piroptose); cGAS-STING (mtDNA)
Impacto sobre B3 (Neuroplasticidade): indireto via IL-1β/IL-18 que suprimem BDNF/CREB e promovem poda
Força da evidência da afirmação: alto (via em si, animal/célula) / medio (depressão humana)
Referência: (Swanson, 2019)[OB]; (Pathogenic NLRP3 mutants, 2024)[EC]
```

```
Molécula/Gene/Receptor/Proteína: NF-κB (subunidade RELA/p65)
UniProt ID:    Q04206
Gene (HGNC):   RELA
HMDB ID:       null
Função fisiológica normal: fator de transcrição pró-inflamatório; saída comum de TLR/TNFR/IL-1R
Alteração em ansiedade: ↑ atividade transcricional
Alteração em depressão: ↑ no subgrupo; desinibido por resistência a glicocorticoide
Células/estruturas onde atua: todas as células imunes e neurais
Vias moleculares associadas: TLR4/MyD88/IRAK/TRAF6/IKK; NLRP3 priming; COX-2/iNOS
Impacto sobre B3: dirige transcrição de IL1B/IL6/TNF que deprimem plasticidade
Força da evidência: alto (mecanismo) / medio (humano)
Referência: (Gastrodin TLR4/TRAF6/NF-κB, 2024)[ML]; (GR-driven repression, 2018)[ML]
```

```
Molécula/Gene/Receptor/Proteína: IL-6
UniProt ID:    P05231
Gene (HGNC):   IL6
HMDB ID:       null
Função fisiológica normal: citocina pleiotrópica; resposta de fase aguda, reparo
Alteração em ansiedade: ↑ periférica
Alteração em depressão: ↑ replicada em meta-análises; prediz não-resposta e anedonia
Células: monócitos, macrófagos, micróglia, astrócitos, adipócitos
Vias associadas: IL-6R clássico vs. trans-sinalização sIL-6R/gp130/JAK-STAT3
Impacto sobre B3: suprime BDNF; trans-sinalização também reparativa (dual)
Força da evidência: alto (humano, marcador)
Referência: (Dowlati, 2010)[MA]; (Osimo, 2020)[MA]; (Repopulating microglia IL-6, 2020)[ML]
```

```
Molécula/Gene/Receptor/Proteína: TNF-α / TNFR1 / TNFR2
UniProt ID:    P01375 / P19438 / P20333
Gene (HGNC):   TNF / TNFRSF1A / TNFRSF1B
HMDB ID:       null
Função: citocina pró-inflamatória; TNFR1 apoptótico/pró-inflamatório, TNFR2 homeostático/neuroprotetor
Alteração em depressão: ↑ TNF e sTNFR2 no subgrupo
Células: micróglia, macrófagos, linfócitos
Vias: NF-κB; necroptose RIPK1; scaling sináptico glial (fisiológico)
Impacto sobre B3: modula força de AMPA/scaling; em excesso deprime LTP
Força da evidência: alto (meta/RCT de estratificação)
Referência: (Goldsmith, 2016)[MA]; (Raison infliximabe, 2013)[EC]; (Synaptic scaling glial TNF, 2006)[ML]
```

```
Molécula/Gene/Receptor/Proteína: IDO1 (indoleamina 2,3-dioxigenase 1)
UniProt ID:    P14902
Gene (HGNC):   IDO1
HMDB ID:       null
Função: converte triptofano em quinurenina; induzida por IFN-γ/citocinas
Alteração em depressão: ↑ atividade (razão KYN/TRP desviada)
Células: monócitos, micróglia, astrócitos
Vias: JAK-STAT/IFN-γ; quinurenina (KYNA astrocitário vs. QUIN microglial)
Impacto sobre B3: reduz triptofano para 5-HT; QUIN excitatório/ROS
Força da evidência: alto (animal causal) / medio (humano marcador)
Referência: (O'Connor IDO1/LPS, 2009)[ML]; (IDO1/kynurenine aging, 2022)[OB]
```

```
Molécula/Gene/Receptor/Proteína: TSPO (proteína translocadora 18 kDa)
UniProt ID:    P30536
Gene (HGNC):   TSPO
HMDB ID:       null
Função: transporte de colesterol/esteroides na mitocôndria; marcador PET de ativação glial
Alteração em depressão: ↑ densidade em córtex cingulado/ínsula (subgrupo)
Células: micróglia e astrócitos (não exclusivo micróglia)
Vias: esteroidogênese; resposta glial
Impacto sobre B3: marcador de neuroinflamação central, não agente direto
Força da evidência: medio (ressalva rs6971)
Referência: (Setiawan, 2015)[EC]; (Holmes, 2018)[EC]
```

```
Molécula/Gene/Receptor/Proteína: FKBP5
UniProt ID:    Q13451
Gene (HGNC):   FKBP5
HMDB ID:       null
Função: co-chaperona que modula sensibilidade do receptor de glicocorticoide (GR)
Alteração: desmetilação dependente de trauma × alelo de risco → resistência a GR → NF-κB desinibido
Células: neurônios, células imunes
Vias: eixo HPA/GR; NF-κB (loop B1↔B2/B12)
Impacto sobre B3: indireto via cortisol/citocinas
Força da evidência: alto (humano, gene×ambiente)
Referência: (Klengel, 2013)[EC]; (Holocausto FKBP5, 2016)[EC]
```

*Não incluídos: medicamentos, suplementos ou agentes terapêuticos (pertencem às bibliotecas de Intervenções/Suplementos).*

---

## MARCADORES_PARA_JSON

```json
{
  "id_canonico": "mecanismo_B1_neuroinflamacao",
  "nome_canonico": "Neuroinflamação",
  "categoria_funcional": "imunológico",
  "cronicidade": "crônico (com fases agudas de precipitação)",
  "reversibilidade": "moderada",
  "janela_temporal": "horas (agudo) a anos (cronificação/priming)",
  "status_validacao": "estabelecido, heterogêneo por sub-via e por subgrupo",

  "key_molecules": ["NLRP3", "NF-κB/RELA", "IL-1β", "IL-6", "TNF-α", "GSDMD", "IDO1", "quinurenina/QUIN/KYNA", "TSPO", "FKBP5", "SPMs/resolvinas", "IL-10", "CX3CL1/CX3CR1", "CCL2/CCR2", "S100B/RAGE", "HMGB1"],
  "key_pathways": ["TLR4/MyD88→NF-κB", "inflamassoma NLRP3→caspase-1→GSDMD", "JAK-STAT/IFN→IDO1/quinurenina", "COX-2/PGE2", "cGAS-STING/IFN-I", "IL-10/STAT3 (freio)", "resolução por SPMs"],

  "biomarkers_peripheral": ["hs-CRP", "IL-6", "TNF-α", "sTNFR2", "razão KYN/TRP", "IL-10", "CCL2/MCP-1", "S100B", "neopterina"],
  "biomarkers_central": ["TSPO-PET", "QUIN (pós-morte/LCR)", "IL-6/YKL-40/sTREM2 no LCR", "conectividade córtico-estriatal (fMRI)", "volume hipocampal", "mio-inositol (MRS)"],

  "symptoms_linked": ["anedonia", "fadiga/lentificação psicomotora", "sintomas somáticos", "retraimento social", "humor deprimido", "disfunção cognitiva"],

  "clinical_phenotypes_predominant": ["subtipo inflamatório (~PCR elevada, minoria)", "depressão resistente ao tratamento (candidato)", "anedonia/circuito de recompensa", "sobreposição TEPT/trauma precoce"],

  "forca_evidencia_afirmacao_geral": "medio",

  "ssri_insufficient_reason": "Citocinas (IL-1β/TNF) suprimem BDNF/TrkB/CREB e plasticidade a jusante da monoamina; aumentar serotonina sináptica não reverte esse elo, e a inflamação elevada prediz não-resposta a antidepressivo.",
  "drug_resistance_link": {
    "value": true,
    "mechanism": "Resistência a glicocorticoide (FKBP5/GR) desinibe NF-κB; inflamação basal alta prediz não-resposta a SSRI e resposta a anti-TNF apenas no subgrupo inflamado (RCT infliximabe)."
  },

  "connection_strength": {
    "B1": "self", "B2": "high", "B3": "high", "B4": "medium",
    "B5": "medium", "B6": "medium", "B7": "medium-high", "B8": "low-medium",
    "B9": "medium", "B10": "medium", "B11": "low-medium", "B12": "high",
    "B13": "low", "B14": "low", "B15": "low", "B16": "medium"
  },

  "amplification_loops": [
    "B1→B6(ROS)→B9(mitocôndria/mtDNA)→B1 (NLRP3/cGAS-STING)",
    "B12(trauma/FKBP5)→B2(resistência GR)→B1(NF-κB desinibido)→B12",
    "B7(disbiose/LPS)→B1(TLR4)→quebra de BHE→B1"
  ],

  "upstream_mechanisms": ["B2_estresse_HPA", "B7_eixo_intestino_cerebro", "B12_trauma_adversidade", "B10_sono_circadiano", "B8_micronutrientes", "senescência/idade"],
  "downstream_mechanisms": ["B3_neuroplasticidade", "B4_monoaminas", "B5_glutamato", "B16_neurogenese", "B6_estresse_oxidativo"]
}
```

> Nota: os identificadores UniProt/HGNC acima foram preenchidos com os símbolos oficiais padrão; a conferência exata campo a campo (e HMDB quando aplicável a metabólitos) é tarefa da auditoria de conteúdo (G3), não desta geração estrutural.
