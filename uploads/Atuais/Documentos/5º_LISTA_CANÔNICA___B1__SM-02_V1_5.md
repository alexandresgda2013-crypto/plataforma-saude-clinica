# LISTA CANÔNICA — B1 / SM-02 (Prova de Existência)
# 35 claims + subclaims — esquema oficial único válido
# v1.5 — 2026-09-17
# Correção vs. v1.4:
#   - .014 aprovado_com_ressalva (fontes + resultados_query registrados)
#   - Q014 base v2 confirmada em uso
#   - status_geral e proximo_alvo atualizados
# v1.4 — 2026-09-16
# Correção vs. v1.3:
#   - REPOSICIONAMENTO: claims de SM-02 são CLÍNICOS e têm destino na
#     pasta evidencias/bibliografia, não na biblioteca canônica
#     mecanística (ver nota_destino e Bloco de Estado v1.7)
#   - status sincronizados com o Bloco de Estado v1.7: .015 pendente →
#     aprovado_com_ressalva; .013 "Aprovado" → aprovado_com_ressalva;
#     .012 "Aprovado_com_ressalva" → aprovado_com_ressalva (enum exato)
#   - .012b, .012c adicionados (existiam só no Bloco); .013b reescrito
#     (entrada malformada: sem "- ", com TAB, sem claim/fontes)
#   - campo fontes adicionado em .008, .012, .013, .015
#   - .017, .023, .028, .032 → status em_busca (trabalho iniciado sem
#     desfecho — ver claims_em_andamento no Bloco de Estado)
#   - Q014 base reformulada para v2 (query_historico em .014) — decisão
#     P3 pendente no Bloco de Estado
#   - status_geral e proximo_alvo atualizados
#   - nota_conflito_pendente movida para pendencias_decisao_usuario (P2)
#     do Bloco de Estado
# ============================================
# HISTÓRICO ANTERIOR
# v1.3 — 2026-08-13
# Correção vs. v1.2:
#   - status atualizado: .005, .006, .009, .010, .011 aprovados
#     (nesta sessão); .005b criado como novo subclaim
#   - corrigida capitalização de status (Aprovado/aprovada → aprovado,
#     valor precisa bater exato com o enum do Schema-Claim)
#   - .011: claim reescrito para refletir população real (comportamento/
#     tentativa de suicídio, não "MDD com ideação suicida"); bloco
#     referencia_cruzada_esperada substituído por referencia_cruzada real
#     (inclui cenario_E99_urgencias_psiquiatricas)
#   - removida prioridade: proximo_alvo de .010/.011 (já aprovados)
#   - fontes_rejeitadas e fontes_exploratorias REMOVIDOS deste arquivo —
#     eram log duplicado; única fonte de verdade agora é o Bloco de
#     Estado ("LOG DE EXCLUSÃO... vive só aqui", regra já existente,
#     só não estava sendo seguida)
#   - fila_realocacao consolidada: eram 3 chaves "fila_realocacao:"
#     duplicadas com PMIDs repetidos (parser silenciosamente descartava
#     as duas primeiras); agora é uma lista única, sem duplicata
#   - removidas da fila_realocacao entradas já resolvidas: 34999196
#     (avaliado e rejeitado em .011, ver fontes_rejeitadas no Bloco de
#     Estado), 31928628 (duplicata do que já está em fontes_rejeitadas)
#   - CONFLITO ENCONTRADO E MARCADO (não resolvido sozinho — ver nota
#     no rodapé): 33339712 e 30696814 apareciam como "descartado" em
#     fontes_rejeitadas E como "avaliar se serve a B4" em
#     fila_realocacao ao mesmo tempo
# Correção vs. v1.1:
#   - nota_regra_fronteira_B1_B4 → nota_regra_fronteira_B1_B4_B5
#   - adicionados nota_priorizacao e distribuicao_esperada_checklist
#     em status_geral; adicionado nota_trilha_constante
#   - adicionado referencia_cruzada_esperada em .011, .013, .029
#   - .031 passou a aplicar exclusion_terms completo (Grupo 6)
#   - adicionada 4ª entrada em fila_futura_outros_submodulos (SM-14,
#     resposta diferencial do subgrupo inflamatório de .007)
# Correção vs. v1.0:
#   - adicionado campo `filtro_desenho_na_query` em cada entrada
#   - adicionado campo `trilha` em cada entrada (humana | preclinica)
#   - Nenhuma outra mudança de conteúdo em relação à v1.0
# ============================================

# (arquivo próprio, substituível quando SM-02 fechar e SM-03 assumir)

nota_destino: >
  Os claims deste submódulo são de natureza CLÍNICA (meta-análise,
  caso-controle, coorte, post-mortem humano, ômicas humanas) e alimentam
  a pasta evidencias/bibliografia da plataforma — não a biblioteca
  canônica mecanística, que tem pipeline próprio (16 bibliotecas em
  auditoria). A cascata bioquímica/fisiológica não é objetivo destes
  claims; eles documentam o quanto a ciência clínica sustenta a
  existência do fenômeno. Formato de saída: Schema-Claim v1.2 até
  decisão do schema de evidencias/bibliografia.

nota_auditoria: >
  Esquema de 35 é o único válido (esquema de 26 descontinuado).
  Subclaims .00Xb/c/d são extensões criadas quando a literatura
  revela discriminação por comparador ou moderador dentro do
  mesmo claim-alvo.

nota_regra_fronteira_B1_B4_B5:
  tema: "quinurenina/quinolinato — dupla fronteira"
  regra: >
    Claim .011 trata quinolinato/ativação imune no LCR como
    BIOMARCADOR de neuroinflamação central (prova de existência),
    não como explicação da via bioquímica. Enzimologia da via
    IDO/TDO pertence a B4; excitotoxicidade via agonismo NMDA do
    quinolinato pertence a B5. Quando aprovado, B1.SM02.011
    referencia AMBOS via referencia_cruzada:
    [mecanismo_B4_deficiencias_monoaminas, mecanismo_B5_gaba_glutamato].
    Mantém scope_out "quinurenina em profundidade" (Protocolo de
    Escopo v1.3) compatível com existência do claim .011 dentro de B1.

status_geral:
  aprovados_principais: 15   # .001-.015
  aprovados_subclaims: 8     # .001b/c/d, .005b, .007b, .012b/c, .013b
  em_busca: 4                # .017, .023, .028, .032
  pendentes: 16              # .016, .018-.022, .024-.027, .029-.031, .033-.035
  proximo_alvo: [".017", ".016", ".018", ".019", ".020"]
  nota_priorizacao: >
    Grupos 1 e 2 completos; Grupo 3 em fechamento (.014 e .015
    aprovados). Segue .017 (achado herdado a confirmar), .016, .018,
    .019. Depois Grupos 4, 5 e 6, retomando os claims em_busca.
  distribuicao_esperada_checklist:
    nota: "Consultar APENAS ao declarar SM-02 fechado — não é regra de bloqueio durante o processo"
    total_claims: 35
    suportados_por_metanalise_minimo: 14
    disorder_specificity_anxiety_minimo: 4
    claims_limitacao_confundimento_minimo: 7
    evidence_role_preclinical_esperado: 0
    acao_se_anxiety_abaixo_minimo: >
      Registrar evidence_gap: escassez_ansiedade_vs_depressao como
      achado formal em fontes_rejeitadas com motivo "ausência de
      meta-análise em transtornos de ansiedade — gap documentado".
      Não bloqueia fechamento de SM-02, mas deve constar na narrativa
      transversal futura. Status atual: .005/.005b/.006 já garantem
      representação de ansiedade — gap não se aplica mais como estava.

nota_trilha_constante: >
  Todas as entradas de SM-02 são trilha: humana, porque o submódulo
  "Prova de Existência" (SM-02) foi desenhado com inclusion_criteria
  species=[human] desde a origem. Evidência pré-clínica correlata
  (ex: infusão de citocinas em roedor) pertence a SM-03/SM-04/SM-08,
  não a SM-02 — por isso trilha é constante aqui, mas o campo fica
  explícito para nunca ser assumido tacitamente em submódulos futuros.

# --------------------------------------------
# GRUPO 1 — Evidência periférica (sangue)
# --------------------------------------------
grupo_1_perifericos:
  - id: B1.SM02.001
    status: aprovado_com_ressalva
    claim: "MDD apresenta IL-6 periférica mais elevada que controles (transdiagnóstica)"
    query: '("Depressive Disorder, Major"[MeSH]) AND ("Interleukin-6"[MeSH]) AND (meta-analysis[pt] OR systematic review[pt]) NOT (electroconvulsive therapy[mh] OR antidepressive agents[mh] OR treatment outcome[mh])'
    filtro_desenho_na_query: sim
    trilha: humana
    fontes: [36893912, 39089535]

  - id: B1.SM02.001b
    tipo: subclaim
    status: aprovado_com_ressalva
    claim: "Direção do efeito de sexo na relação inflamação-depressão diverge entre estudos"
    filtro_desenho_na_query: herda_da_query_pai   # deriva de .001
    trilha: humana
    fontes: [39089535, 22832816]

  - id: B1.SM02.001c
    tipo: subclaim
    status: aprovado
    claim: "IL-1β elevada em MDD vs. transtorno bipolar"
    filtro_desenho_na_query: herda_da_query_pai   # deriva de .001
    trilha: humana
    fontes: [36893912]

  - id: B1.SM02.001d
    tipo: subclaim
    status: aprovado
    claim: "IL-10 elevada em bipolar vs. MDD"
    filtro_desenho_na_query: herda_da_query_pai   # deriva de .001
    trilha: humana
    fontes: [36893912]

  - id: B1.SM02.002
    status: aprovado
    claim: "MDD apresenta PCR mais elevada que controles (27% PCR>3; 58% PCR>1)"
    query: '("Depressive Disorder, Major"[MeSH]) AND ("C-Reactive Protein"[MeSH]) AND (meta-analysis[pt] OR systematic review[pt]) NOT (electroconvulsive therapy[mh] OR antidepressive agents[mh] OR treatment outcome[mh])'
    filtro_desenho_na_query: sim
    trilha: humana
    fontes: [31258105]

  - id: B1.SM02.003
    status: aprovado_com_ressalva
    claim: "MDD apresenta TNF-α periférico mais elevado que controles (evidência incerta)"
    query: '("Depressive Disorder, Major"[MeSH]) AND ("Tumor Necrosis Factor-alpha"[MeSH]) AND (meta-analysis[pt] OR systematic review[pt]) NOT (electroconvulsive therapy[mh] OR antidepressive agents[mh] OR treatment outcome[mh])'
    filtro_desenho_na_query: sim
    trilha: humana
    fontes: [26065825]

  - id: B1.SM02.004
    status: aprovado
    claim: "IL-1β não difere de controles saudáveis; discrimina apenas MDD de bipolar"
    query: '("Depressive Disorder, Major"[MeSH]) AND ("Interleukin-1beta"[MeSH]) AND (meta-analysis[pt] OR systematic review[pt]) NOT (electroconvulsive therapy[mh] OR antidepressive agents[mh] OR treatment outcome[mh])'
    filtro_desenho_na_query: sim
    trilha: humana
    fontes: [26065825, 36893912]

  - id: B1.SM02.005
    status: aprovado_com_ressalva
    claim: "Transtornos de ansiedade (TAG, transtorno do pânico) apresentam elevação de marcadores inflamatórios periféricos vs. controles"
    query: '("Anxiety Disorders"[MeSH]) AND ("Cytokines"[MeSH] OR "Inflammation"[MeSH]) AND (meta-analysis[pt] OR systematic review[pt]) AND humans[MeSH]'
    filtro_desenho_na_query: sim
    trilha: humana
    nota_escopo: "TOC excluído do escopo de ansiedade (DSM-5 classifica TOC em capítulo próprio, não em Transtornos de Ansiedade) — decisão registrada em 2026-08-09."
    fontes: [31326932, 29241050]

  - id: B1.SM02.005b
    tipo: subclaim
    status: aprovado_com_ressalva
    claim: "Elevação inflamatória de .005 não replica, com a mesma robustez, em população pediátrica/adolescente"
    filtro_desenho_na_query: herda_da_query_pai   # deriva de .005
    trilha: humana
    fontes: [33200498]

  - id: B1.SM02.006
    status: aprovado_com_ressalva
    claim: "Magnitude da elevação inflamatória difere entre ansiedade e MDD"
    query: '("Anxiety Disorders"[MeSH] AND "Depressive Disorder, Major"[MeSH]) AND "Inflammation"[MeSH] AND (meta-analysis[pt] OR systematic review[pt] OR comparative study[pt]) AND humans[MeSH]'
    filtro_desenho_na_query: sim
    trilha: humana
    query_historico:
      - versao: 1
        query: 'query original acima'
        motivo_substituicao: "termo entre aspas não reconhecido pelo índice de frase do PubMed (tradução automática do navegador alterou o texto colado)"
        data: "2026-08-09"
      - versao: 2
        query: '("Anxiety Disorders"[MeSH] OR "Depressive Disorder, Major"[MeSH] OR "Mood Disorders"[MeSH]) AND (...)'
        motivo_substituicao: "'Mood Disorders[MeSH]' é termo pai que inclui bipolar inteiro — 151/159 resultados irrelevantes (bipolar isolado)"
        data: "2026-08-09"
      - versao: 3
        query: '(...) AND ("diagnostic specificity"[tiab] OR "across disorders"[tiab] OR ...) AND (meta-analysis[pt] OR systematic review[pt])'
        motivo_substituicao: "interseção de frase rara + filtro de tipo de publicação — zero resultados"
        data: "2026-08-09"
      - versao: 4
        query: '(anxiety[tiab] AND (depression[tiab] OR "major depressive"[tiab])) AND (inflammat*[tiab] OR cytokine*[tiab] OR "C-reactive protein"[tiab]) AND (...)'
        motivo_substituicao: "247 resultados, fonte aprovada (37931509) encontrada por leitura manual dos títulos, não por refinamento adicional de query"
        data: "2026-08-09"
    fontes: [37931509]

  - id: B1.SM02.007
    status: aprovado
    claim: "Apenas subgrupo (~27%) de MDD apresenta elevação inflamatória, não a totalidade"
    query: '("Depressive Disorder, Major"[MeSH]) AND ("Inflammation"[MeSH]) AND (subgroup* OR subtype* OR stratif* OR heterogen* OR "latent class") AND (meta-analysis[pt] OR systematic review[pt] OR "Cohort Studies"[MeSH])'
    filtro_desenho_na_query: sim
    trilha: humana
    fontes: [31258105, 39615605]
    fontes_exploratorias: [32696276]

  - id: B1.SM02.007b
    tipo: subclaim
    status: aprovado
    claim: "Maus-tratos na infância identifica subgrupo de MDD com PCR elevada (moderador de .007)"
    filtro_desenho_na_query: herda_da_query_pai   # deriva de .007
    trilha: humana
    fontes: [18391129]
    referencia_cruzada: [mecanismo_B12_neurobiologia_trauma]

  - id: B1.SM02.008
    status: aprovado_com_ressalva
    claim: "NLR (razão neutrófilos/linfócitos) elevada em MDD vs. controles"
    query: '("Depressive Disorder"[MeSH]) AND ("neutrophil-to-lymphocyte ratio" OR "neutrophil lymphocyte ratio" OR "systemic immune-inflammation index") AND (meta-analysis[pt] OR systematic review[pt]) AND humans[MeSH] NOT (electroconvulsive therapy[mh] OR antidepressive agents[mh] OR treatment outcome[mh])'
    filtro_desenho_na_query: sim
    trilha: humana
    fontes: [41481888, 36517638, 40856326]
    fontes_exploratorias: [38802507, 40345445]

# --------------------------------------------
# GRUPO 2 — Compartimento central (LCR)
# --------------------------------------------
grupo_2_lcr:
  - id: B1.SM02.009
    status: aprovado
    claim: "Citocinas pró-inflamatórias elevadas no LCR de MDD"
    query: '("Depressive Disorder"[MeSH]) AND ("Cerebrospinal Fluid"[MeSH]) AND ("Cytokines"[MeSH]) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana
    fontes: [35442429]

  - id: B1.SM02.010
    status: aprovado_com_ressalva
    claim: "Correlação entre citocinas plasma×LCR é fraca ou inconsistente"
    query: '("Cerebrospinal Fluid"[MeSH]) AND ("Cytokines"[MeSH]) AND (correlat* AND (plasma OR serum OR periph*)) AND ("Depressive Disorder"[MeSH] OR "Mental Disorders"[MeSH]) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana
    nota_query: "1 resultado na v1 (fora de escopo, HIV), descartado sem registro formal de query_historico por ser resultado único e claramente irrelevante."
    fontes: [31195092]

  - id: B1.SM02.011
    status: aprovado_com_ressalva
    claim: >
      Quinolinato (QUIN) e marcadores de ativação imune/permeabilidade
      de BHE alterados no LCR em indivíduos com comportamento/tentativa
      de suicídio (população definida por comportamento, não por
      diagnóstico de MDD estrito e exclusivo — ver ressalva completa no
      claim aprovado, Bloco de Estado).
    query: '("Suicidal Ideation"[MeSH] OR "Suicide"[MeSH]) AND ("Cerebrospinal Fluid"[MeSH]) AND ("Quinolinic Acid"[MeSH] OR "Kynurenine"[MeSH] OR neuroinflamm*) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana
    nota: "ver nota_regra_fronteira_B1_B4_B5 no topo deste documento"
    referencia_cruzada: [mecanismo_B4_deficiencias_monoaminas, mecanismo_B5_gaba_glutamato, cenario_E99_urgencias_psiquiatricas]
    fontes: [27483383, 25124710, 19268915, 23299933, 26796235]
    fontes_exploratorias: [41388730, 28448609]

  - id: B1.SM02.012
    status: aprovado_com_ressalva
    claim: "Marcadores de ativação glial detectáveis no LCR em MDD"
    query: '("Depressive Disorder"[MeSH]) AND ("Cerebrospinal Fluid"[MeSH]) AND ("S100 Calcium Binding Protein beta Subunit"[MeSH] OR "Chitinase-3-Like Protein 1"[MeSH] OR YKL-40 OR sTREM2) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana
    fontes: [25264292, 29764272, 34021122]
    fontes_exploratorias: [32439851]

  - id: B1.SM02.012b
    tipo: subclaim
    status: aprovado_com_ressalva
    claim: "sTREM2 no LCR reduzido/inversamente associado a sintomas depressivos em idosos (não generalizável a MDD adulto geral)"
    filtro_desenho_na_query: herda_da_query_pai   # deriva de .012
    trilha: humana
    fontes: [38795783, 34246952, 39044521]

  - id: B1.SM02.012c
    tipo: subclaim
    status: aprovado_com_ressalva
    claim: "Evidência de GFAP no LCR em MDD é insuficiente/contraditória — direção não resolvida"
    filtro_desenho_na_query: herda_da_query_pai   # deriva de .012
    trilha: humana
    fontes: [34021122, 20132991]   # 20132991: ver pendência P1 no Bloco de Estado

  - id: B1.SM02.013
    status: aprovado_com_ressalva
    claim: "MDD apresenta alteração de proteínas do complemento no LCR ou soro"
    query: '("Depressive Disorder"[MeSH]) AND ("Complement System Proteins"[MeSH] OR "Complement C3"[MeSH] OR C1q) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana
    referencia_cruzada_esperada:
      valores: [mecanismo_B3_neuroplasticidade, mecanismo_B16_neurogenese]
      nao_influencia_G3: true
      nota_blindagem: >
        PLANEJAMENTO apenas. Preencher referencia_cruzada de forma
        independente ao avaliar o abstract em G3. Complemento C1q/C3
        → poda sináptica é o mecanismo esperado, conectando tanto B3
        (neuroplasticidade) quanto B16 (neurogênese), mas deve ser
        confirmado pelo abstract, não assumido.
    nota_exclusion_terms: >
      Query de nicho (LCR — literatura escassa).
      NÃO aplicar NOT de antidepressivos. Apenas humans[MeSH].
    referencia_cruzada: [mecanismo_B3_neuroplasticidade]   # G3 confirmou só B3; B16 não sustentado pelos abstracts
    fontes: [29454970, 36447174, 32272297, 33794316, 29798743, 36285542]

  - id: B1.SM02.013b
    tipo: subclaim
    status: aprovado
    claim: "C3, C4 e fator H mais elevados em transtorno bipolar do que em MDD (mesmo desenho)"
    filtro_desenho_na_query: herda_da_query_pai   # deriva de .013
    trilha: humana
    fontes: [36285542]

# --------------------------------------------
# GRUPO 3 — Neuroimagem in vivo (TSPO-PET)
# --------------------------------------------
grupo_3_tspo_pet:
  - id: B1.SM02.014
    status: aprovado_com_ressalva
    claim: "MDD apresenta maior ligação de TSPO no cérebro que controles"
    query: '("Depressive Disorder, Major"[MeSH] OR "major depressive"[tiab] OR "major depression"[tiab]) AND (TSPO[tiab] OR "translocator protein"[tiab] OR "peripheral benzodiazepine receptor"[tiab] OR PBR28[tiab] OR PK11195[tiab] OR FEPPA[tiab] OR "DPA-713"[tiab] OR ER176[tiab]) AND ("Positron-Emission Tomography"[MeSH] OR PET[tiab]) NOT ("spreading depression"[tiab] OR "flumazenil"[tiab])'
    nota_q014_base: >
      Esta é a "Q014 base" referenciada por .015, .016 e .017. Sem
      humans[MeSH] de propósito (literatura escassa + artigos recentes
      ainda não indexados); estudos animais que aparecerem vão para
      redirecionados, não para fontes_rejeitadas.
    query_historico:
      - versao: 1
        query: '("Depressive Disorder, Major"[MeSH]) AND ("Receptors, GABA"[MeSH] OR TSPO OR "translocator protein" OR PBR28 OR PK11195) AND ("Positron-Emission Tomography"[MeSH]) AND humans[MeSH]'
        motivo_substituicao: "\"Receptors, GABA\"[MeSH] indexa receptor GABA-A/benzodiazepínico central — leva de .015 (13/08) trouxe falsos-positivos de flumazenil/pânico e 'cortical spreading depression' (enxaqueca). Termos TSPO passaram a [tiab] + radioligantes de 2ª/3ª geração; NOT para os dois falsos-positivos recorrentes"
        data: "2026-09-16"
    filtro_desenho_na_query: nao
    trilha: humana
    fontes: [36226319, 25629589, 28939116, 29971587, 23850810]
    resultados_query:
      triados:
        - {pmid: "36226319", desfecho: aprovado_com_ressalva}
        - {pmid: "25629589", desfecho: aprovado_com_ressalva}
        - {pmid: "28939116", desfecho: aprovado_com_ressalva}
        - {pmid: "29971587", desfecho: aprovado_com_ressalva}
        - {pmid: "23850810", desfecho: aprovado_com_ressalva}
      nao_triados:
        - {pmid: "29496589", titulo: "Setiawan/Attwells et al. 2018 — TSPO VT e duração de MDD não tratado (Lancet Psychiatry): ~15-23% elevado no MDE; ~29-42% elevado em MDD não tratado por >10 anos; 50 MDD vs 30 controles",
           motivo: "já registrado como fonte exploratória de .015 (duração da doença não tratada como preditor mais forte); identidade PMID↔artigo a confirmar ao vivo antes de virar fonte de .014",
           acao: "candidato a moderador duracao_doenca_nao_tratada em .014", data_registro: "2026-09-17"}
        - {pmid: null, titulo: "Li H, Sagar AP, Kéri S 2018 — 50 nunca-medicados vs 30 controles, [18F]FEPPA, TSPO VT elevado em todas as ROIs (substância branca, cinzenta, córtex frontal, temporal, hipocampo), associado a pior atenção/memória (RBANS)",
           motivo: "encontrado ao vivo em 17/09 sem PMID confirmado; é um dos 8 estudos da meta-análise de Eggerstorfer",
           acao: "confirmar PMID; candidato a fonte de .014 e de .012 (cognição) ou .016", data_registro: "2026-09-17"}
      redirecionados:
        - {pmid: "29269262", titulo: "Li H, Sagar AP, Kéri S 2018 — ligação de TSPO reduzida em depressão maior durante terapia cognitivo-comportamental",
           motivo: "desenho com intervenção (TCC) — resposta a intervenção, não prova de existência basal",
           destino_sugerido: "SM-14", trilha: humana, data_registro: "2026-09-17"}
      revisado_apos_gatilho: sim
      nota_gatilho: >
        Desfecho foi aprovado_com_ressalva, o que aciona a revisão da
        fila de não triados. Os dois não triados são estudos POSITIVOS
        já incluídos na meta-análise que serve de fonte principal —
        podem reforçar a direção, não invertê-la, e não são evidência
        independente dela. Por isso não alteram o desfecho nem a força
        média atribuída. A lista completa da query não foi colada nesta
        leva: os 3 itens acima vieram de busca ao vivo e de tabela de
        revisão, não de varredura completa do PubMed.

  - id: B1.SM02.015
    status: aprovado_com_ressalva
    claim: "Aumento de TSPO em MDD é regionalmente mais pronunciado no cíngulo anterior"
    query: '[Q014 base] AND ("Gyrus Cinguli"[MeSH] OR "anterior cingulate" OR regional) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana
    nota_leitura: >
      Leva de 2026-08-13 trouxe 7 falsos-positivos temáticos (ver
      fontes_rejeitadas no Bloco de Estado) — termos que colidem com
      vocabulário TSPO/depressão sem serem o mesmo construto:
      "cortical spreading depression" (fenômeno de enxaqueca, não
      transtorno depressivo), atlas de receptor GABA-A/flumazenil
      (sistema receptor diferente de TSPO), população Parkinson/EM
      (fora de disease_context). Vale refinar a query para excluir
      "spreading depression"[tiab] e restringir explicitamente a
      TSPO/translocator protein antes da próxima leva. → Aplicado na
      Q014 base v2 (ver .014).
    fontes: [36226319, 31195092, 28939116, 33515765, 25629589, 35654450]
    fontes_exploratorias: [34153835, 37543251, 29496589, 27758838]

  - id: B1.SM02.016
    status: pendente
    claim: "Ligação de TSPO correlaciona-se com severidade do episódio depressivo"
    query: '[Q014 base] AND (severity OR correlat* OR "Psychiatric Status Rating Scales"[MeSH]) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

  - id: B1.SM02.017
    status: em_busca
    claim: "TSPO aumentado em MDD com ideação suicida vs. MDD sem ideação"
    query: '[Q014 base] AND ("Suicidal Ideation"[MeSH] OR "Suicide"[MeSH]) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

  - id: B1.SM02.018
    status: pendente
    claim: "TSPO não é marcador exclusivo de microglia ativada — limitação interpretativa"
    query: '(TSPO OR "translocator protein") AND (specificity OR limitation* OR interpret* OR "cell type" OR astrocyt*) AND (review[pt] OR "Reproducibility of Results"[MeSH]) AND humans[MeSH]'
    filtro_desenho_na_query: sim   # inclui review[pt]
    trilha: humana

  - id: B1.SM02.019
    status: pendente
    claim: "Existem dados de TSPO-PET em transtornos de ansiedade"
    query: '("Anxiety Disorders"[MeSH] OR "Stress Disorders, Post-Traumatic"[MeSH]) AND (TSPO OR "translocator protein") AND ("Positron-Emission Tomography"[MeSH]) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

# --------------------------------------------
# GRUPO 4 — Evidência post-mortem
# --------------------------------------------
grupo_4_postmortem:
  - id: B1.SM02.020
    status: pendente
    claim: "Cérebros post-mortem de MDD apresentam alteração de densidade/morfologia microglial"
    query: '("Depressive Disorder"[MeSH]) AND ("Microglia"[MeSH]) AND (postmortem OR "post-mortem" OR "Autopsy"[MeSH]) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

  - id: B1.SM02.021
    status: pendente
    claim: "Redução de densidade/marcadores astrocitários em regiões límbicas e pré-frontais em MDD"
    query: '("Depressive Disorder"[MeSH]) AND ("Astrocytes"[MeSH] OR "Glial Fibrillary Acidic Protein"[MeSH]) AND (postmortem OR "Autopsy"[MeSH]) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

  - id: B1.SM02.022
    status: pendente
    claim: "Expressão de genes inflamatórios aumentada em córtex pré-frontal em MDD"
    query: '("Depressive Disorder"[MeSH]) AND ("Prefrontal Cortex"[MeSH]) AND ("Gene Expression Profiling"[MeSH] OR transcriptom*) AND (inflamm* OR immune) AND (postmortem OR "Autopsy"[MeSH]) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

  - id: B1.SM02.023
    status: em_busca
    claim: "Suicídio associa-se a marcadores de ativação microglial e recrutamento de monócitos no SNC"
    query: '("Suicide"[MeSH]) AND ("Microglia"[MeSH] OR "Monocytes"[MeSH]) AND (postmortem OR "Autopsy"[MeSH]) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

  - id: B1.SM02.024
    status: pendente
    claim: "Achados post-mortem em MDD são heterogêneos entre estudos e regiões"
    query: '("Depressive Disorder"[MeSH]) AND (neuroinflamm* OR "Microglia"[MeSH]) AND postmortem AND (systematic review[pt] OR review[pt]) AND humans[MeSH]'
    filtro_desenho_na_query: sim   # inclui systematic review[pt] OR review[pt]
    trilha: humana

  - id: B1.SM02.025
    status: pendente
    claim: "Uso prévio de antidepressivos e causa de morte confundem achados post-mortem"
    query: '(postmortem OR "Autopsy"[MeSH]) AND ("Brain"[MeSH]) AND (confound* OR limitation* OR "Antidepressive Agents"[MeSH] OR "agonal") AND ("Mental Disorders"[MeSH]) AND review[pt] AND humans[MeSH]'
    filtro_desenho_na_query: sim   # inclui review[pt]
    trilha: humana

# --------------------------------------------
# GRUPO 5 — Assinaturas moleculares e ômicas
# --------------------------------------------
grupo_5_omicas:
  - id: B1.SM02.026
    status: pendente
    claim: "Assinatura transcricional inflamatória em leucócitos periféricos de MDD"
    query: '("Depressive Disorder, Major"[MeSH]) AND ("Gene Expression Profiling"[MeSH] OR transcriptom*) AND ("Leukocytes"[MeSH] OR blood) AND (inflamm* OR immune) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

  - id: B1.SM02.027
    status: pendente
    claim: "Monócitos de MDD apresentam resposta inflamatória alterada a estímulo ex vivo"
    query: '("Depressive Disorder, Major"[MeSH]) AND ("Monocytes"[MeSH]) AND (ex vivo OR stimulat* OR lipopolysaccharide) AND ("Cells, Cultured"[MeSH] OR "Cytokines"[MeSH]) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

  - id: B1.SM02.028
    status: em_busca
    claim: "Escores de risco genético para vias inflamatórias associam-se a diagnóstico/sintomas depressivos"
    query: '("Depressive Disorder, Major"[MeSH]) AND ("Multifactorial Inheritance"[MeSH] OR "polygenic risk score" OR "Genome-Wide Association Study"[MeSH]) AND (inflamm* OR immune) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

  - id: B1.SM02.029
    status: pendente
    claim: "Alterações epigenéticas em genes inflamatórios presentes em MDD"
    query: '("Depressive Disorder, Major"[MeSH]) AND ("DNA Methylation"[MeSH] OR "Epigenomics"[MeSH]) AND (inflamm* OR "NR3C1" OR cytokine*) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana
    referencia_cruzada_esperada:
      valores: [mecanismo_B12_neurobiologia_trauma]
      nao_influencia_G3: true
      nota_blindagem: >
        PLANEJAMENTO apenas. Preencher referencia_cruzada de forma
        independente ao avaliar o abstract em G3. Adversidade precoce
        → programação epigenética inflamatória é o vínculo esperado
        com B12, mas deve ser sustentado pelo abstract do PMID aprovado.
    nota_exclusion_terms: >
      Query de nicho (ômicas — literatura escassa).
      NÃO aplicar NOT de antidepressivos. Apenas humans[MeSH].

  - id: B1.SM02.030
    status: pendente
    claim: "Proteômica/metabolômica identificam módulos inflamatórios associados a fenótipos depressivos"
    query: '("Depressive Disorder, Major"[MeSH]) AND ("Proteomics"[MeSH] OR "Metabolomics"[MeSH]) AND (inflamm* OR immune) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

# --------------------------------------------
# GRUPO 6 — Delimitação e confundidores
# --------------------------------------------
grupo_6_confundidores:
  - id: B1.SM02.031
    status: pendente
    claim: "IMC e adiposidade confundem parcialmente a associação inflamação-depressão"
    query: '("Depressive Disorder"[MeSH]) AND ("Inflammation"[MeSH]) AND ("Body Mass Index"[MeSH] OR "Obesity"[MeSH] OR "Adiposity"[MeSH]) AND (meta-analysis[pt] OR systematic review[pt]) AND humans[MeSH] NOT (electroconvulsive therapy[mh] OR antidepressive agents[mh] OR treatment outcome[mh])'
    filtro_desenho_na_query: sim
    trilha: humana
    referencia_cruzada_esperada:
      valores: [mecanismo_B9_disfuncao_mitocondrial]
      nao_influencia_G3: true
      nota_blindagem: >
        PLANEJAMENTO apenas. Preencher referencia_cruzada de forma
        independente ao avaliar o abstract em G3. Obesidade/adipocinas
        como ponte inflamação-bioenergética é o vínculo esperado com
        B9, mas deve ser sustentado pelo abstract.
    nota_exclusion_terms: >
      Grupo 6 (confundidores — alto volume). Aplica NOT completo.
      IMC é confundidor independente de tratamento, mas o NOT de
      antidepressivos e ECT é aplicado para manter foco em
      associação basal, não em efeito de intervenção.

  - id: B1.SM02.032
    status: em_busca
    claim: "Tabagismo, sedentarismo, álcool e comorbidades influenciam marcadores inflamatórios em MDD"
    query: '("Depressive Disorder"[MeSH]) AND ("Inflammation"[MeSH]) AND ("Smoking"[MeSH] OR "Sedentary Behavior"[MeSH] OR "Alcohol Drinking"[MeSH] OR "Comorbidity"[MeSH]) AND (systematic review[pt] OR meta-analysis[pt]) AND humans[MeSH]'
    filtro_desenho_na_query: sim
    trilha: humana

  - id: B1.SM02.033
    status: pendente
    claim: "Variabilidade pré-analítica afeta medida de citocinas"
    query: '("Cytokines"[MeSH]) AND ("Blood Specimen Collection"[MeSH] OR preanalytic* OR "Specimen Handling"[MeSH] OR "Circadian Rhythm"[MeSH] OR fasting) AND ("Reproducibility of Results"[MeSH] OR variabilit*) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

  - id: B1.SM02.034
    status: pendente
    claim: "Elevação inflamatória em MDD é de baixo grau, com sobreposição substancial com controles"
    query: '("Depressive Disorder, Major"[MeSH]) AND ("Inflammation"[MeSH]) AND ("low-grade" OR overlap OR "effect size" OR distribution) AND (meta-analysis[pt] OR systematic review[pt]) AND humans[MeSH]'
    filtro_desenho_na_query: sim
    trilha: humana

  - id: B1.SM02.035
    status: pendente
    claim: "Marcadores inflamatórios não têm acurácia diagnóstica suficiente para diagnosticar MDD isoladamente"
    query: '("Depressive Disorder"[MeSH]) AND ("Biomarkers"[MeSH]) AND (inflamm* OR "C-Reactive Protein"[MeSH]) AND ("Sensitivity and Specificity"[MeSH] OR "diagnostic accuracy" OR ROC) AND humans[MeSH]'
    filtro_desenho_na_query: nao
    trilha: humana

# ============================================
# FILA FUTURA — PMIDs encontrados mas fora de SM-02,
# destinados a outros submódulos (não é rejeição)
# ============================================
fila_futura_outros_submodulos:
  - {pmid: 41951112, destino: SM-03, tema: "TNF-α × risco causal (RM)"}
  - {pmid: 41905486, destino: SM-13, tema: "trajetória inflamação × remissão"}
  - {pmid: 42252042, destino: SM-14, tema: "biomarcador preditor — limitação"}
  - {pmid: "32402468", destino: SM-14, tema: "TSPO como preditor de resposta a celecoxibe (open-label)"}
  - {pmid: "34052828", destino: SM-14, tema: "RCT minociclina × volume de distribuição de TSPO em TDM resistente"}
  - {pmid: null, destino: SM-14, origem_claim: "B1.SM02.007",
     tema: "Subgrupo inflamatório (.007 — ~27% com PCR>3mg/L) × resposta diferencial a intervenção anti-inflamatória.",
     descricao: "PMIDs que demonstrem que APENAS o subgrupo com inflamação basal elevada responde a anti-IL-6, infliximab, celecoxibe ou equivalentes pertencem a SM-14 (modulação e reversibilidade), não a SM-02 (prova de existência basal). SM-14 provará a acionabilidade clínica do claim .007: existência do subgrupo (SM-02) + resposta diferencial (SM-14) = argumento completo para estratificação clínica.",
     instrucao_triagem: "Se durante busca de .007 ou queries relacionadas surgir PMID com foco em 'resposta a tratamento em subgrupo inflamatório', não rejeitar — registrar aqui com PMID real e encaminhar para SM-14."}

# ============================================
# FILA DE REALOCAÇÃO — PMIDs que pertencem a OUTRO
# mecanismo/claim dentro do próprio B1 (não SM-02 → outro submódulo,
# isso é fila_futura acima; isso aqui é "achei, mas é de outro lugar
# dentro de B1 ou de outro mecanismo B2-B16")
# Consolidada nesta versão — antes existiam 3 blocos duplicados com
# a mesma chave "fila_realocacao:" (parser silenciosamente descartava
# os 2 primeiros). Também removidas entradas já resolvidas:
#   - 34999196: avaliado e rejeitado em .011 (ver fontes_rejeitadas,
#     Bloco de Estado) — pointer já não é mais tarefa em aberto
#   - 31928628: duplicata do que já está em fontes_rejeitadas com o
#     mesmo destino (SM-14)
# ============================================
fila_realocacao:
  - {pmid: "27225499", motivo: "revisão narrativa sobre dopamina/monoaminas no LCR, não citocinas", destino: "mecanismo_B4_deficiencias_monoaminas"}
  - {pmid: "21605657", motivo: "quinurenina/via da monoamina apenas plasmática, sem componente LCR/correlação — relevante tanto para triagem de .010 quanto de .011, nenhum dos dois usa", destino: "mecanismo_B4_deficiencias_monoaminas"}
  - {pmid: "19918244", motivo: "modelo experimental de indução causal (IFN-alfa em hepatite C), não prova de existência basal", destino: "SM-03"}
  - {pmid: "18801471", motivo: "idem — modelo IFN-alfa experimental, direção de causalidade", destino: "SM-03"}
  - {pmid: "23896207", motivo: "S100B em astrócitos/oligodendrócitos — estudo POST-MORTEM (densidade de astrócitos S100B+ reduzida em MDD/bipolar vs. controles), não LCR", destino: "B1.SM02.021"}
  - {pmid: "33734498", motivo: "revisão narrativa de patologia astrocitária post-mortem em MDD — não é fonte primária, mas contextualiza hipótese S100B", destino: "B1.SM02.021 (referência de contexto, não fonte principal)"}
  - {pmid: "39666148", motivo: "sTREM2/YKL-40 no LCR, mas população é Parkinson com depressão comórbida — disorder primário é PD", destino: "avaliar mecanismo/gap — depressão é variável secundária, não usar como fonte principal de .012"}
  - {pmid: "41611983", motivo: "achado de GFAP é em tecido cerebral, não LCR; marcadores do LCR reportados (Afamina, SERPINF1) não são de ativação glial clássica", destino: "B1.SM02.026 ou .030 (ômicas/proteômica)"}
  - {pmid: "41297678", motivo: "tema central é poluição do ar como exposição; sTREM2/depressão é mediador secundário", destino: "avaliar relevância para B1 apenas como corroborante do padrão sTREM2, não fonte principal"}
  - {pmid: "35918160", motivo: "população de risco para Alzheimer (não MDD/ansiedade clínica); IL-6 no LCR com direção inversa ao padrão periférico", destino: "nota de gap/interação com neurodegeneração, fora do escopo direto de B1/SM-02"}
  - {pmid: "22982200", motivo: "população neurológica geral (DNNI) com sintoma depressivo dimensional, não MDD diagnosticado", destino: "nota de heterogeneidade de S100B — não usar como fonte principal de .012"}
  - {pmid: "28211584", motivo: "YKL-40: achado nulo para estado depressivo (texto explícito); achado positivo é para ideação suicida — tematicamente ligado a .011, mas .011 já fechou sem essa fonte (base já robusta); manter como candidato a reforço futuro, não ação pendente", destino: "B1.SM02.011 (informativo, não bloqueante)"}
  - {pmid: "41961543", motivo: "revisão sobre eixo intestino-cérebro e suicídio — tema pertence a B7, não B1", destino: "mecanismo_B7_eixo_intestino_cerebro"}
  - {pmid: "32062729", motivo: "população esquizofrenia+bipolar, sem braço de MDD — fora do disease_context de B1 (mesmo padrão de 33339712/30696814)", destino: "avaliar se serve a mecanismo focado em psicose/bipolar"}
  - {pmid: "19188531", motivo: "achado central é IMC como mediador/moderador da associação PCR/IL-6-depressão — pertence ao escopo de .031 (IMC/adiposidade), não ao de .032 (tabagismo/sedentarismo/álcool/comorbidades)", destino: "B1.SM02.031"}
  - {pmid: "29928963", motivo: "achado central é atenuação do efeito PCR-depressão sob controle metodológico rigoroso (r=0,05→0,005 ns) — mais afim a .034 (baixo grau/sobreposição com controles); obesidade aparece só como critério de ajuste, tangencial a .031", destino: "B1.SM02.034 (avaliar também relevância secundária pra .031)"}
  - {pmid: "36319817", motivo: "meta-análise de EWAS (metilação de DNA) em MDD — pertence ao domínio de .029, não .028", destino: "B1.SM02.029 (mesmo submódulo, claim distinto)"}
  - {pmid: "33106475", motivo: "GWAS de resposta a classe de antidepressivo — resposta a tratamento, não prova de existência basal", destino: "SM-14"}
  - {pmid: "34739073", motivo: "MR bidirecional depressão × DII — pergunta causal para marcador específico, não associação de escore de risco poligênico", destino: "SM-03"}
  - {pmid: "41066853", motivo: "MR causal de MCP-1 → transtornos neuropsiquiátricos — mesmo padrão causal", destino: "SM-03"}
  - {pmid: "41429762", motivo: "MR de proteínas inflamatórias circulantes → SCZ/BD/MDD — causal, marcador específico", destino: "SM-03"}
  - {pmid: "41528645", motivo: "MR bidirecional + colocalização, células B de memória × MDD — mesmo padrão causal", destino: "SM-03"}
  - {pmid: "41398384", motivo: "meta-análise GWAS de obesidade; humor/depressão é correlação secundária — tema de fundo mais afim a .031", destino: "avaliar B1.SM02.031 (mesmo submódulo, claim distinto)"}
  - {pmid: "40408832", motivo: "escores genéticos → proteômica prevista, combinado com desfecho de tratamento — mistura .030 com possível SM-14", destino: "avaliar B1.SM02.030 ou SM-14 (confirmar com abstract)"}
  - {pmid: "40768164", motivo: "arquitetura genética de homeostase energética (IMC, triglicerídeos, glicose, PCR, leptina) e heterogeneidade da depressão", destino: "avaliar B1.SM02.031"}
  - {pmid: "32724131", motivo: "PRS aplicado à predição de resposta ao tratamento com esketamina", destino: "SM-14"}
  - {pmid: "37390107", motivo: "multimorbidade psicocardiometabólica via GWAS multivariado", destino: "avaliar B1.SM02.031"}
  - {pmid: "29906483", motivo: "revisão sobre farmacogenética de antidepressivos", destino: "SM-14"}
  - {pmid: "33431106", motivo: "depressão × saúde cardiometabólica, estudo longitudinal de gêmeos", destino: "avaliar B1.SM02.031"}
  - {pmid: "41152404", motivo: "integração de escores poligênicos para prever resultado de tratamento antidepressivo", destino: "SM-14"}
  - {pmid: "35354486", motivo: "EWAS usando PRS-depressão como exposição para achar metilação em genes de resposta imune", destino: "B1.SM02.029 (mesmo submódulo, claim distinto)"}
  - {pmid: "30130674", motivo: "predisposição genética a inflamação testada contra resposta a antidepressivo (ensaio clínico)", destino: "SM-14"}
  - {pmid: "29790996", motivo: "perfis de metilação do DNA + PRS + IL-6/telômero; ênfase primária é epigenética", destino: "B1.SM02.029 (mesmo submódulo, claim distinto)"}
  - {pmid: "40977463", motivo: "perfil genético da via da quinurenina — pertence à fronteira B4/B5 (ver nota_regra_fronteira_B1_B4_B5)", destino: "mecanismo_B4_deficiencias_monoaminas"}
  - {pmid: "30521077", motivo: "fenótipos de depressão × 20 características cardiometabólicas via análise poligênica", destino: "avaliar B1.SM02.031"}

# ============================================
# REDIRECIONADOS — PMID pré-clínico achado em busca de trilha_humana
# (regra: nunca vira fontes_rejeitadas — ver Bloco de Estado/Como Executar)
# ============================================
redirecionados:
  - {pmid: "40081592", motivo: "modelo primata de depressão", destino_sugerido: "SM-08 (vias de sinalização) ou SM-04 (microglia)", trilha: preclinica}
  - {pmid: "21614209", motivo: "modelo de estresse crônico leve em ratos, S100B hipocampal", destino_sugerido: "SM-04 (microglia/astrócitos)", trilha: preclinica}
  - {pmid: "22776451", motivo: "primatas não-humanos, inflamação sistêmica induzida por endotoxina — pré-clínico", destino_sugerido: "SM-04 (microglia)", trilha: preclinica, data_registro: "2026-08-13"}
  - {pmid: "37167824", motivo: "estudo pré-clínico (camundongos); saponinas de Pulsatilla, IDO1, triptofano e inflamação intestinal — achado com valor mecanístico para B1 mesmo sendo animal", destino_sugerido: "SM-08 (toca fronteira B4/B5 via IDO1/triptofano)", trilha: preclinica, data_registro: "2026-08-13"}

# nota_conflito_pendente (33339712/30696814) → movida para
# pendencias_decisao_usuario (P2) no Bloco de Estado v1.7
