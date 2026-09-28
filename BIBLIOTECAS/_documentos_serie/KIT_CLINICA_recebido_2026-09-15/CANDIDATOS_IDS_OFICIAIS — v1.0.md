# ============================================
# CANDIDATOS_IDS_OFICIAIS — v1.1
# Correção vs. v1.0: adicionados 2 campos opcionais/aditivos —
# trilha_origem e claim_id_origem — para preservar proveniência
# completa agora que existem 2 trilhas de validação (clínica e
# mecanística) alimentando o mesmo ledger único. Entradas anteriores
# (v1.0) continuam válidas sem esses campos; preencher
# retroativamente é opcional, não obrigatório.
# Ledger lateral, cross-mecanismo, baixíssima frequência.
# NÃO faz parte do kit de produção diário (não recarregar por sessão).
# Só recebe entrada quando a validação de PMID (qualquer mecanismo)
# revelar entidade de nível superior ainda não catalogada em
# _ids_oficiais.json (ex: exame, biomarcador, suplemento recorrente
# na literatura que ainda não tem ID oficial).
# Revisão periódica decide se entra na próxima versão de _ids_oficiais.
# ============================================

candidatos:
  # cada item, quando surgir:
  # - nome_sugerido: string        (snake_case, seguindo regras_nomenclatura)
  #   categoria_provavel: string   (ex: C4_inflamatorios, D3_fitoterapicos)
  #   motivo: string                (por que parece merecer virar ID oficial)
  #   pmid_origem: string
  #   mecanismo_origem: string      (ex: B1, B7 — mecanismo, não trilha)
  #   trilha_origem: clinica | mecanistica    # NOVO (v1.1) — opcional
  #   claim_id_origem: string                  # NOVO (v1.1) — opcional
  #                                             # ex: "B1.SM02.008" ou "B1.MEC.BLOCO03.002"
  #   status: sugerido | em_avaliacao | incorporado | rejeitado
  #   data: string

  - nome_sugerido: exame_s100b
    categoria_provavel: C4_inflamatorios
    motivo: "Usado em B1.SM02.012 — evidência em LCR é nula/inconsistente (não confirma marcador útil), mas segue candidato a catalogar pela frequência de uso na literatura. Verificar se C4_inflamatorios comporta ou se merece categoria própria."
    pmid_origem: "25264292"
    mecanismo_origem: B1
    status: em_avaliacao
    data: "2026-08-14"
    acao_pendente: "B1.SM02.012 fechado em G3 — revisar para incorporação, mantendo explícito que a evidência em LCR para S100B em MDD é nula/inconsistente."

  - nome_sugerido: exame_strem2
    categoria_provavel: C4_inflamatorios
    motivo: "Usado em B1.SM02.012b (sTREM2 reduzido no LCR em MDD tardia). Nota: é marcador de atividade fagocítica microglial, não citocina clássica — mesma ressalva de categoria que exame_s100b."
    pmid_origem: "38795783"
    mecanismo_origem: B1
    status: sugerido
    data: "2026-08-14"
    acao_pendente: "Revisar categoria (C4_inflamatorios vs. categoria própria de marcadores microgliais) antes de promover para em_avaliacao."

  - nome_sugerido: exame_il10
    categoria_provavel: C4_inflamatorios
    motivo: "Citocina anti-inflamatória; usada no claim aprovado B1.SM02.001d sem ID oficial. Hiles et al. (22687336) quantifica d=-0,31 (IC99% -0,95 a 0,32, I²=94,1%), efeito não significativo."
    pmid_origem: "36893912 (uso aprovado em .001d); 22687336 (candidato em avaliação, .032)"
    mecanismo_origem: B1
    status: sugerido
    data: "2026-08-13"

  - nome_sugerido: exame_il1ra
    categoria_provavel: C4_inflamatorios
    motivo: "Antagonista do receptor de IL-1, medido separadamente de IL-1β em Howren et al. (d=0,25, IC95% 0,04-0,46). Distinto de exame_il1beta já catalogado; sem ID oficial próprio."
    pmid_origem: "19188531"
    mecanismo_origem: B1
    status: sugerido
    data: "2026-08-13"

  - nome_sugerido: exame_razao_neutrofilos_linfocitos
    categoria_provavel: C4_inflamatorios
    motivo: "Usado em claim B1.SM02.008 (NLR elevada em MDD), sem ID oficial catalogado"
    pmid_origem: 41481888
    mecanismo_origem: B1
    status: em_avaliacao
    data: "2026-08-14"
    acao_pendente: "Revisar para possível incorporação em C4_inflamatorios na próxima versão de _ids_oficiais.json."

  - nome_sugerido: exame_aisi
    categoria_provavel: C4_inflamatorios
    motivo: "Índice Agregado de Inflamação Sistêmica — identificado por regressão ridge como fator mais robusto associado a MDD (AUC=0.710), acima de NLR/PLR/MLR isolados"
    pmid_origem: 41707720
    mecanismo_origem: B1
    status: sugerido
    data: "2026-08-13"
    acao_pendente: "Candidato baseado em achado exploratório único (n=236) — reavaliar se aparecer em mais fontes antes de promover a em_avaliacao."

  - nome_sugerido: exame_mcp1
    categoria_provavel: C4_inflamatorios
    motivo: "Quimiocina inflamatória (MCP-1/CCL2), usada como marcador em estudo de RM causal com transtornos neuropsiquiátricos (PMID 41066853); sem ID oficial catalogado"
    pmid_origem: "41066853"
    mecanismo_origem: B1
    status: sugerido
    data: "2026-08-13"

  - nome_sugerido: exame_gfap
    categoria_provavel: C4_inflamatorios
    motivo: "Usado no subclaim B1.SM02.012c — achado positivo forte (p<0,001) mas contraditório com fonte já rejeitada (PMID 20132991) e com comparador metodologicamente comprometido (HII, não saudável)."
    pmid_origem: "34021122"
    mecanismo_origem: B1
    status: sugerido
    data: "2026-08-14"
    acao_pendente: "Evidência contraditória/comprometida — não promover para em_avaliacao até replicação com comparador saudável de verdade. Revisar categoria (C4_inflamatorios vs. marcador astrocitário próprio) junto com exame_s100b e exame_strem2."

  - nome_sugerido: exame_complemento_c5
    categoria_provavel: C4_inflamatorios
    motivo: "Usado em B1.SM02.013 (C5 elevado no LCR em MDD, p<0,001)."
    pmid_origem: "29454970"
    mecanismo_origem: B1
    status: sugerido
    data: "2026-08-14"
    acao_pendente: "Revisar se C4_inflamatorios comporta proteínas do complemento ou se merece categoria própria (via imune inata ≠ citocina clássica)."

  - nome_sugerido: exame_complemento_c3
    categoria_provavel: C4_inflamatorios
    motivo: "Usado em B1.SM02.013 (C3/C3a elevados no soro em MDD) e B1.SM02.013b (C3 discrimina BD de MDD)."
    pmid_origem: "36447174"
    mecanismo_origem: B1
    status: sugerido
    data: "2026-08-14"
    acao_pendente: "Mesma revisão de categoria que exame_complemento_c5."

  - nome_sugerido: exame_complemento_c1q
    categoria_provavel: C4_inflamatorios
    motivo: "Usado em B1.SM02.013 — evidência contraditória entre 2 fontes (ver nota_ressalva), catalogar mesmo assim pela frequência de uso na literatura."
    pmid_origem: "32272297"
    mecanismo_origem: B1
    status: sugerido
    data: "2026-08-14"
    acao_pendente: "Mesma revisão de categoria. Nota explícita de evidência mista ao promover."

  - nome_sugerido: exame_complemento_fator_h
    categoria_provavel: C4_inflamatorios
    motivo: "Usado em B1.SM02.013 (CFH elevado, população geriátrica) e B1.SM02.013b (fator H discrimina BD de MDD)."
    pmid_origem: "29798743"
    mecanismo_origem: B1
    status: sugerido
    data: "2026-08-14"
    acao_pendente: "Mesma revisão de categoria. Nota de restrição a população geriátrica na fonte de origem."