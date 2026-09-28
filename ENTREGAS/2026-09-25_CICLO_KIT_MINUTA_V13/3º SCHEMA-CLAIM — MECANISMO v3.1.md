SCHEMA-CLAIM — MECANISMO v3.1
yaml
# ============================================
# SCHEMA_CLAIM_MECANISMO — v3.1
# Correção vs. v3.0:
#   - único ajuste: nomenclatura de claim_id de M1.BLOCOxx para
#     B1.MEC.BLOCOxx (ver Documento 1, changelog v1.1, mesma razão:
#     "M1" não é ID de mecanismo válido em _ids_oficiais.json).
#     Nenhuma mudança de conteúdo científico ou estrutural.
#   - citação Guyatt et al. 2011 verificada nesta sessão via busca
#     (J Clin Epidemiol 2011;64(4):383-394 — primeiro artigo da
#     série "GRADE guidelines"). Removida a alegação de correspondência
#     com "_regras_globais.json R04" — esse arquivo não foi
#     compartilhado nesta sessão, não posso confirmar seu conteúdo.
# Correção vs. v2.0 (histórico, já aplicada em v3.0):
#   - removido grade_simplificado [A/B/C] do nível do claim — era
#     mapeamento fixo tipo-de-estudo→nota, erro categorial: GRADE é
#     propriedade de um CORPO de evidência para uma afirmação
#     específica, nunca de uma fonte isolada. Substituído por
#     dominios_grade_observados (por fonte, dentro de fontes:).
# Correção vs. v1.0 (histórico, já aplicada em v2.0):
#   - abandonado enum único de posição em cascata linear (AOP) →
#     substituído por relacoes_causais_declaradas (arestas, permite
#     rede/bifurcação/loop, conforme exigido pelo BLOCO_07/BLOCO_08
#     do Prompt 4.0)
#   - adicionados classificador_tipo_fonte [MA/EC/OB/ML/AT] e
#     forca_biologica_conexao [HIGH/MEDIUM/LOW] como eixos próprios
#   - vocabulário de natureza_da_relacao e grau_maturidade_cientifica
#     importado literalmente do GPM v2.0
#   - campo generalizacao_interespecie substituído por
#     origem_da_evidencia + teste_conexao_fenotipo
#   - adicionado mapa_exportacao_modulo09 (contrato de interface
#     Claim → Schema de Entrada Módulo 09 do Prompt 4.0)
#   - removida exigência de "in vitro + 2 humanos" do nível do claim
#     — é regra de síntese no Prompt 4.0, não de admissão do claim
# ============================================

> **NOTA DE VERSÃO (reconciliação com o processo atual):** as menções a
> "Prompt 4.0" abaixo correspondem, na pipeline em uso hoje, ao Prompt
> 4.2 (PMID) — a numeração dos BLOCOs não mudou. A migração de
> nomenclatura GRADE → forca_evidencia_afirmacao (v4.1→v4.2) é
> posterior à última revisão desta ferramenta: onde este documento
> cita "GRADE"/"nota GRADE" no nível de mecanismo, leia-se
> forca_evidencia_afirmacao (alto|medio|baixo).

nota_4_eixos_de_evidencia: >
  Este schema mantém 4 eixos de avaliação SIMULTÂNEOS e NUNCA
  fundidos entre si, porque respondem perguntas diferentes:
  1) forca_causal (tier 1-4) — responde "o desenho experimental
     demonstra necessidade/suficiência causal?" (lógica de biologia
     molecular — knockout/resgate). Definições em Documento 1,
     inclusion_criteria.tiers_forca_causal.
  2) classificador_tipo_fonte [MA/EC/OB/ML/AT] — responde "que tipo
     de documento é esta fonte, para fins de arquivamento
     bibliográfico?" (Módulo 09 do Prompt 4.0)
  3) forca_biologica_conexao [HIGH/MEDIUM/LOW] — responde "a via está
     completa e validada em humano, ou é plausibilidade animal?"
     (BLOCO_08 do Prompt 4.0)
  4) dominios_grade_observados (por fonte, dentro de cada item de
     fontes:) — responde "que domínios reais do GRADE Working Group
     (Guyatt et al., 2011, J Clin Epidemiol 64(4):383-394 — primeiro
     artigo da série, verificado nesta sessão) esta fonte específica
     evidencia?" Não produz nota final — a nota real (forca_evidencia_afirmacao, 
	 calculado no Prompt 4.2 — ver DEFINIÇÕES DE GRADAÇÃO) é responsabilidade
     exclusiva da síntese da Biblioteca, nunca do claim individual.
  Um claim pode ser, simultaneamente: tier_1 (knockout+resgate), [OB]
  (observacional/mecanístico para fins de arquivo), LOW (só validado
  em roedor), com dominios_grade_observados registrando indirecao=
  indireto. As 4 informações coexistem sem contradição — cada uma
  serve a um consumidor diferente downstream. Nenhum dos 4 deve ser
  lido isoladamente como "qualidade global" da fonte — a
  interpretação integrada pertence exclusivamente à etapa de
  construção/auditoria da Biblioteca (Prompt 4.0).

claim_id: string
  # formato: B1.MEC.BLOCO{nn}.{nnn}[a-z opcional para subclaim]
  # ex: B1.MEC.BLOCO02.001, B1.MEC.BLOCO08.003b
  # "B1" = mecanismo oficial (_ids_oficiais.json), invariável
  # "MEC" = infixo fixo que marca trilha mecanística, distinguindo
  # do namespace clínico já existente (B1.SM02.xxx)
  # namespace próprio, validado contra Lista Canônica do submódulo,
  # NÃO contra _ids_oficiais.json (mesma regra do schema clínico)

version: int
status: aprovado | aprovado_com_ressalva | em_busca | rejeitado | aposentado
verification: verificado_nesta_conversa | herdado_nao_verificado_por_mim

statement: string
  # Deve descrever um mecanismo causal (via, elo, ou resultado de
  # manipulação) — não uma associação estatística com população
  # clínica. Se o statement puder ser reescrito como "grupo A difere
  # de grupo B" sem perda de sentido, provavelmente pertence ao
  # módulo clínico, não a este.

relacoes_causais_declaradas: [ ]
  # Lista de arestas — permite rede, bifurcação, convergência e
  # ciclos (loops de amplificação, BLOCO_08). Vazio permitido quando
  # o claim descreve um nó isolado (ex: identidade molecular de um
  # mediador, BLOCO_03) sem elo causal específico sendo o objeto do
  # claim.
  # cada item:
  # - no_origem: string       # ex: "NLRP3_inflamassoma_ativo"
  #   no_destino: string      # ex: "IL1B_maturacao_caspase1"
  #   natureza_da_relacao: causal | contributiva | associativa |
  #     compensatoria | marcador | nao_estabelecida
  #     # vocabulário importado literalmente do GPM v2.0 — não inventar
  #     # variação própria
  #   direcao: unidirecional | bidirecional
  #   sentido_do_achado: suporta_relacao | refuta_relacao | inconclusivo
  #     # OBRIGATÓRIO. Captura achado negativo/refutação.

grau_maturidade_cientifica: muito_estabelecido | bem_suportado |
  moderadamente_suportado | emergente | hipotese_inicial
  # OBRIGATÓRIO. Vocabulário GPM v2.0, importado literalmente.
  # Mede CONSENSO/REPLICAÇÃO na literatura como um todo — eixo
  # ortogonal a forca_causal (mede rigor de UM desenho específico).

forca_causal: tier_1_necessidade_e_suficiencia |
  tier_2_necessidade_ou_suficiencia | tier_3_correlacional_mecanistico |
  tier_4_descritivo_estrutural
  # Definições em Documento 1 (Protocolo de Escopo B1 — Trilha
  # Mecanística v1.1), inclusion_criteria.tiers_forca_causal.
  # NÃO EXISTE regra "in vitro exige 2+ humanos" neste nível — isso
  # é decisão de síntese do Prompt 4.0, cruzando múltiplos claims.

forca_biologica_conexao: HIGH | MEDIUM | LOW
  # OBRIGATÓRIO quando o claim alimenta BLOCO_07 ou BLOCO_08.
  # Definição herdada verbatim do Prompt 4.0:
  # HIGH = mecanismo demonstrado em múltiplos estudos humanos, via
  #        molecular completa descrita
  # MEDIUM = demonstrado em humano mas via parcial, OU completa em
  #          animal + evidência humana associacional
  # LOW = plausibilidade animal/in vitro, sem validação robusta humana

classificador_tipo_fonte: MA | EC | OB | ML | AT
  # OBRIGATÓRIO. Vocabulário verbatim do Prompt 4.0 — determina pasta
  # de arquivo no Módulo 09 (01_pmids a 05_manuais_e_livros).
  # MA = meta-análise/revisão sistemática (inclui meta-análise
  #      PRÉ-CLÍNICA/mecanística — não confundir com meta-análise
  #      clínica de associação, que é módulo clínico)
  # EC = ensaio controlado (inclui desafio experimental humano, ex:
  #      endotoxina em voluntário saudável)
  # OB = observacional/mecanístico/série de casos/modelo animal/
  #      in vitro — categoria mais frequente neste módulo
  # ML = livro-texto/consenso formal — bioquímica de manual
  # AT = atualização pós-geração inicial

uso: nucleo_causal | suporte_correlacional | gap_pesquisa
  # nucleo_causal exige >=1 fonte principal com forca_causal tier_1
  # ou tier_2. tier_3/tier_4 isolados -> maximo suporte_correlacional.

origem_da_evidencia: [ ]
  # lista combinável, vocabulário GPM: evidencia_humana |
  # evidencia_modelo_animal | evidencia_in_vitro

teste_conexao_fenotipo: tecido_snc_relevante | fenotipo_comportamental_validado |
  biologia_basica_sem_doenca | referencia_cruzada_biblioteca_clinica
  # OBRIGATÓRIO. Teste de 3 braços do GPM/Prompt4.0, adaptado.
  claim_id_clinico_relacionado: string | nulo
  extrapolacao_por_analogia: string | nulo
    # Preencher EXATAMENTE com o texto da tag quando aplicável:
    # "[EXTRAPOLAÇÃO POR ANALOGIA: condição original — validação
    # direta em ansiedade/depressão pendente]" — string vazia por
    # padrão, replicando o campo homônimo do Schema de Entrada
    # Módulo 09, para exportação sem retrabalho.

nota_ressalva: string | nulo
  # OBRIGATÓRIO se status = aprovado_com_ressalva

moderadores: [ ]
  # cada item:
  # - variavel: string   (ex: tipo_celular, dose, tempo_estimulo,
  #   estagio_desenvolvimento, especie, regiao_encefalica)
  #   efeito: atenua | inverte | amplifica | nulo
  #   regra_motor: string
  #   fonte_pmid: string

fontes:
  - pmid: string
    autor: string
    ano: int
    nivel: principal | corroborante | exploratorio
    tipo_manipulacao: knockout_genetico | knockdown_sirna_shrna |
      farmacologico_inibidor | farmacologico_agonista | optogenetico |
      quimiogenetico | infusao_direta | correlacional_sem_manipulacao |
      descritivo_estrutural
    contraste_experimental: string
      # ex: veiculo_salino | shRNA_scramble | wild_type_litermates |
      #     condicao_basal_sem_estimulo
    especie: humano | camundongo | rato | primata_nao_humano |
      linha_celular_humana | linha_celular_murina | cultura_primaria |
      organoide | tecido_post_mortem_humano | outro_especificar
    n: int | nulo
    achado: string
    papel: string | nulo
    verificado_nesta_conversa: sim | nao
    dominios_grade_observados:
      # Domínios reais do GRADE Working Group (Guyatt et al. 2011).
      # nao_avaliado em todos os subcampos quando classificador_tipo_fonte
      # = ML (GRADE não se aplica a bioquímica de manual).
      # Viés de publicação NÃO entra aqui — é estruturalmente
      # inavaliável numa fonte isolada; só existe na síntese da
      # Biblioteca (Prompt 4.0), cruzando múltiplos claims/fontes.
      risco_de_vies: baixo | moderado | alto | nao_avaliado
      inconsistencia_com_outros_estudos: nao_aplicavel_fonte_unica |
        consistente_com_literatura_correlata | inconsistente | nao_avaliado
      indirecao: direto | indireto | nao_avaliado
      imprecisao: string | nulo
      fatores_de_upgrade_observacional: [ ]
        # aplicável sobretudo a tier_3/tier_4: efeito_de_grande_magnitude |
        # gradiente_dose_resposta | confundimento_plausivel_atuaria_
        # contra_o_efeito_observado. Preencher SOMENTE quando a
        # própria fonte relatar explicitamente o padrão.

fontes_exploratorias: [ ]  # mesma estrutura
  # revisao_mecanistica_narrativa (sem método sistemático) só entra
  # aqui, nunca em fontes principais.

referencia_cruzada: [ ]
  # ID oficial completo, validado contra _ids_oficiais.json

usado_em_biblioteca: sim | nao   # padrão nao

mapa_exportacao_modulo09:
  # Contrato de interface explícito — como este claim se comprime no
  # Schema de Entrada do Módulo 09 (Prompt 4.0). Preenchido no
  # fechamento do claim (G3), não durante a busca.
  
  # NOTA DE ESCOPO: doi, titulo_artigo e revista_ano — também exigidos
  # pelo Schema de Entrada do Módulo 09 — NÃO são capturados aqui, por
  # decisão de design, não por omissão. São metadado bibliográfico
  # puro, mecanicamente recuperável a partir do pmid_oficial (mesma
  # verificação que já ocorre em G1), sem exigir leitura ou julgamento
  # científico. O claim carrega exclusivamente o que exige avaliação
  # humana/IA (G1→G2→G3); quem resolve doi/titulo/revista é o próprio
  # processo de geração da Biblioteca (Prompt 4.0), por busca direta
  # via PMID no momento em que popula o Módulo 09. Guardar esse dado
  # aqui duplicaria informação que já tem ponto único de verdade — ver
  # P20, Decisões Arquiteturais.
  id_referencia_interna: string        # formato REF_SOBRENOME_ANO
  pmid_oficial: string                 # = fontes[0].pmid da fonte principal
  desenho_estudo: string               # síntese de tipo_manipulacao + especie
  achado_central_molecular: string     # síntese de 1 frase do achado
  extrapolacao_por_analogia: string    # = teste_conexao_fenotipo.extrapolacao_por_analogia
  claim_id_origem: string              # = este próprio claim_id

fila_realocacao:
  - pmid: string
    motivo: string
    destino: string

nota_uso_downstream: >
  A certeza final (equivalente às 4 categorias reais do GRADE Working
  Group: Alta/Moderada/Baixa/Muito Baixa) é calculada na etapa de
  síntese da Biblioteca, cruzando dominios_grade_observados de TODOS
  os claims relevantes a uma mesma afirmação/relação — nunca no nível
  do claim individual.