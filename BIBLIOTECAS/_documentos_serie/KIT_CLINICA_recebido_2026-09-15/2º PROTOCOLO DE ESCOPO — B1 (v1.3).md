#PROTOCOLO DE ESCOPO — B1 (v1.3)

module_id: B1_NEUROINFLAMMATION
version: 1.3
disease_context: [ansiedade, depressao]
status: ativo
last_updated: 2026-08-04
nota_v1.3: >
  Corrigida nota_regra_fronteira_B1_B4 → nota_regra_fronteira_B1_B4_B5:
  quinolinato tem dupla fronteira — enzimologia IDO/TDO pertence a B4;
  excitotoxicidade via agonismo NMDA do quinolinato pertence a B5.
  Claim B1.SM02.011, quando aprovado em G3, deve referenciar ambos
  via referencia_cruzada: [mecanismo_B4_deficiencias_monoaminas,
  mecanismo_B5_gaba_glutamato]. Adicionada entrada correspondente em
  relacoes_cruzadas_semanticas para mecanismo_B5_gaba_glutamato.

nota_v1.2: >
  Adicionada seção relacoes_cruzadas_semanticas — descreve a NATUREZA
  das relações entre B1 e outros mecanismos/biomarcadores, traduzindo
  nomenclatura antiga (MECH_*, BIO_*) para os IDs oficiais do catálogo
  _ids_oficiais.json. Identificados 2 biomarcadores usados em claims
  já existentes (NLR em .008, S100B em .012) sem ID oficial catalogado
  — registrados em CANDIDATOS_IDS_OFICIAIS.yaml. Sem outras mudanças
  de conteúdo em relação à v1.1.

nota_v1.1: >
  Correção estrutural: inclusion_criteria dividido em trilha_humana e
  trilha_preclinica. Motivo: estudos em modelo animal não devem ser
  dispensados da biblioteca de conhecimento — são necessários para
  explicar mecanismo (ex: causalidade direta via infusão de citocinas,
  manipulação genética de microglia), algo que evidência observacional
  humana não pode oferecer. Porém, essa evidência nunca compete na
  mesma hierarquia/priorização da evidência clínica humana, e nunca
  alimenta uso:clinico (ver Schema-Claim v1.2, evidence_role).

scope_in:
  - citocinas pro/anti-inflamatorias perifericas e centrais
  - microglia, astrocitos, ativacao glial
  - vias de sinalizacao inflamatoria (NF-kB, NLRP3, TLR2/4)
  - estresse oxidativo/nitrosativo acoplado a inflamacao
  - permeabilidade da BHE e trafego imune central
  - neuroimagem inflamatoria (TSPO-PET)
  - evidencia post-mortem, LCR e ex-vivo
  - fenotipo clinico "depressao inflamatoria" e heterogeneidade
  - resposta a intervencao anti-inflamatoria como PROVA mecanistica
    (nao como protocolo terapeutico — isso e' de INT_*)

scope_out:
  - eixo HPA em profundidade              -> B2
  - neuroplasticidade/BDNF em profundidade -> B3 (no central, so' cross-ref)
  - GABA/glutamato em profundidade         -> B5
  - microbiota intestinal em profundidade  -> B7
  - mitocondria/bioenergetica em profundidade -> B9
  - sono/circadiano em profundidade        -> B10
  - dose/protocolo de suplemento ou farmaco -> INT_*

nota_regra_fronteira_B1_B4_B5:
  tema: "quinurenina/quinolinato — dupla fronteira"
  regra_B1: >
    O uso de quinolinato/ativação imune no LCR COMO BIOMARCADOR
    de neuroinflamação central (ex: claim B1.SM02.011) é permitido
    dentro de B1, pois serve à prova de existência do mecanismo,
    não à explicação da via. Regra geral: menção funcional = dentro
    do escopo; aprofundamento bioquímico = cross-ref por ID oficial.
  regra_B4: >
    Enzimologia da via IDO/TDO, cinética de depleção de triptofano
    e competição com serotonina → pertence a
    mecanismo_B4_deficiencias_monoaminas.
  regra_B5: >
    Quinolinato como agonista NMDA → excitotoxicidade glutamatérgica
    → pertence a mecanismo_B5_gaba_glutamato.
  aplicacao_claim_011: >
    Quando B1.SM02.011 for aprovado em G3, campo referencia_cruzada
    DEVE incluir ambos:
    [mecanismo_B4_deficiencias_monoaminas, mecanismo_B5_gaba_glutamato].
    Não incluir apenas B4 como era o padrão anterior.

cross_ref_allowed_shorthand: [B2, B3, B5, B6, B7, B9, B10, B16]
cross_ref_ids_oficiais:
  # mapeamento shorthand -> ID oficial completo (_ids_oficiais.mecanismos)
  B2: mecanismo_B2_eixo_hpa_cortisol
  B3: mecanismo_B3_neuroplasticidade
  B5: mecanismo_B5_gaba_glutamato
  B6: mecanismo_B6_estresse_oxidativo
  B7: mecanismo_B7_eixo_intestino_cerebro
  B9: mecanismo_B9_disfuncao_mitocondrial
  B10: mecanismo_B10_desregulacao_circadiana
  B16: mecanismo_B16_neurogenese
  B4: mecanismo_B4_deficiencias_monoaminas   # usado na regra de quinurenina
  B12: mecanismo_B12_neurobiologia_trauma    # usado em .007b

relacoes_cruzadas_semanticas:
  # Extensão de cross_ref_ids_oficiais — descreve a NATUREZA da relação,
  # não apenas que ela existe. Curto, por design (regra: cross-ref é
  # sempre breve, aprofundamento pertence ao módulo de destino).
  # Origem: nomenclatura antiga (MECH_*, BIO_*) traduzida para IDs
  # oficiais do catálogo _ids_oficiais.json.
  - mecanismo: mecanismo_B2_eixo_hpa_cortisol
    relacao: "resistência a glicocorticoides ↔ desinibição inflamatória"
  - mecanismo: mecanismo_B4_deficiencias_monoaminas
    relacao: "IDO/TDO ativada por citocinas → quinolinato/quinurenina (ver nota_regra_fronteira_B1_B4_B5)"
  - mecanismo: mecanismo_B5_gaba_glutamato
    relacao: "quinolinato como agonista NMDA → excitotoxicidade glutamatérgica (ver nota_regra_fronteira_B1_B4_B5)"
  - mecanismo: mecanismo_B7_eixo_intestino_cerebro
    relacao: "disbiose como fonte periférica de sinal inflamatório (LPS, translocação bacteriana)"
  - mecanismo: mecanismo_B9_disfuncao_mitocondrial
    relacao: "acoplamento bidirecional inflamação-bioenergética"
  - mecanismo: mecanismo_B10_desregulacao_circadiana
    relacao: "privação de sono eleva citocinas pró-inflamatórias"
  - mecanismo: "sem ID dedicado — tratado como confundidor em B1.SM02.031"
    relacao: "obesidade/adipocinas/resistência insulínica — via metabólica"
  - mecanismo: "sem ID dedicado — candidato a nota futura"
    relacao: "via colinérgica anti-inflamatória / tônus vagal"

biomarcadores_referenciados:
  # Biomarcadores mencionados em claims de B1 — status de catalogação
  # oficial. Gap identificado nesta revisão: NLR e S100B usados em
  # claims (.008 e .012) sem ID oficial correspondente.
  catalogados:
    - {nome: IL-6, id_oficial: exame_il6}
    - {nome: "PCR ultrassensível", id_oficial: exame_pcr_us}
    - {nome: TNF-alfa, id_oficial: exame_tnfalpha}
    - {nome: IL-1beta, id_oficial: exame_il1beta}
  nao_catalogados_registrados_em_candidatos:
    - {nome: "razão neutrófilos/linfócitos (NLR)", usado_em: "B1.SM02.008", ver: CANDIDATOS_IDS_OFICIAIS}
    - {nome: S100B, usado_em: "B1.SM02.012", ver: CANDIDATOS_IDS_OFICIAIS}

inclusion_criteria:
  trilha_humana:
    species: [human]
    designs: [meta_analysis, systematic_review, RCT, prospective_cohort,
              case_control, post_mortem]
    disorder: [MDD, anxiety_disorders, transdiagnostic]
    year_min: 2005
    exceptions: "estudo seminal pre-2005 aceito com justificativa registrada"
    priorizacao_leitura: "ver Como Executar — heurística desenho > amostra/k > recência"

  trilha_preclinica:
    species: [animal, in_vitro]
    proposito: "mechanistic_support exclusivamente — nunca clinical_claim"
    uso_obrigatorio: contexto_mecanistico
    evidence_role_obrigatorio: preclinical_mechanistic
    ano: "sem restrição de year_min salvo justificativa de obsolescência técnica"
    aplicacao_preferencial:
      - "SM-03 (Direção de causalidade) — ex: infusão direta de citocinas"
      - "SM-04 (Microglia) — ex: manipulação genética/optogenética"
      - "SM-08 (Vias de sinalização intracelular)"
    nota_validade_translacional: >
      Modelos comportamentais em roedor (ex: nado forçado, preferência
      por sacarose) são proxies, não equivalem a MDD humano. Isso deve
      constar como limitação sempre que citado na narrativa transversal,
      nunca apresentado como equivalente a achado clínico.
    priorizacao_leitura: "não compete com trilha_humana; triagem própria, sem ranking cruzado"

exclusion_criteria:
  - case_report isolado sem grupo controle
  - pre-print sem revisao por pares
  - artigo retratado
  - desenho pre/pos-tratamento sem controle saudavel
    (quando o claim exige comparador — regra nascida do caso Dellink/Garcia-Garcia)

target_claims: "definido incrementalmente pela pratica, nao fixado a priori"