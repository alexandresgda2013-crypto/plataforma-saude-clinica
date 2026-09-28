


# DECISOES_ARQUITETURAIS_v2_5.json — Documento Unificado e Completo          (AUDITADO POR ARENA E CHATGPT 14/06/2022 17:50H)

{
  "documento": "DECISOES_ARQUITETURAIS_v2_5",
  "versao": "2.5",
  "descricao": "Decisões arquiteturais e notas de reconciliação do Briefing v2.5. Este documento é fonte de verdade para ambiguidades e conflitos entre as 5 partes do briefing.",
  "data_criacao": "2025",
  "revisao": "final",
  "aplicar_em": [
     "PARTE_D",
    "_ids_oficiais.json",
    "_regras_globais.json",
    "_interacoes_cruzadas_globais.json",
    "_fluxo_primeira_consulta.json",
    "BACKLOG_TECNICO.json"
  ],
  "decisoes": {
    "P1_slot6": {
      "titulo": "Encerramento do Slot_6 Pendente",
      "tipo": "DECISÃO ARQUITETURAL",
      "status": "ENCERRADO ✅",
      "decisao": "Remover definitivamente o conceito de slot_6 pendente. A versão v2.5 considera apenas os suplementos oficialmente catalogados em _ids_oficiais.json.",
      "regra": "Não existem mais placeholders ou suplementos indefinidos aguardando decisão. Qualquer novo suplemento entra exclusivamente via revisão de versão futura (v2.6+).",
      "impacto": {
        "suplementos_removidos_confirmados": 5,
        "ids_removidos": [
          "coq10_ubiquinol",
          "pqq",
          "resveratrol",
          "espermidina",
          "acido_alfa_lipoico"
        ],
        "campo_pendente_confirmacao": "REMOVER de todos os arquivos onde aparecer",
    },
    }
    "P2_dexametasona": {
      "titulo": "Classificação Oficial do exame_dexametasona",
      "tipo": "DECISÃO ARQUITETURAL",
      "status": "DEFINIDO ✅",
      "decisao": "exame_dexametasona = C-LAB (não C-FUNC)",
      "justificativa": "O teste de supressão com dexametasona depende de mensuração laboratorial objetiva de cortisol após intervenção farmacológica padronizada, possuindo interpretação baseada em valores de referência e critérios laboratoriais — característica de C-LAB.",
      "impacto_contagens": {
        "C_LAB": "29 → 30 (exame_dexametasona migrado para cá)",
        "C_FUNC": "10 → 9 (exame_dexametasona removido daqui)"
      },
      "nota_c5": "C5_EIXO_HPA continua com 5 exames. A classificação do template não altera a subsecao — exame_dexametasona permanece em C5, agora com template C-LAB.",
      "nota_consistencia": "Após a execução de IMPL-02, PARTE_D deve refletir as contagens 30/9 como fonte canônica de contagens estruturais (P11). P2 é o registro histórico da decisão. Em caso de divergência entre P2 e PARTE_D, PARTE_D prevalece para contagens, mas a divergência deve ser investigada e corrigida.",
      },
    "P3_status_progresso": {
      "titulo": "Regra de Precedência para Status de Progresso",
      "tipo": "DECISÃO ARQUITETURAL",
      "status": "DEFINIDO ✅",
      "decisao": "Em caso de divergência entre documentação histórica e estrutura atual, a estrutura atual prevalece.",
      "regra": "Percentuais e indicadores de conclusão devem refletir exclusivamente o estado atual da árvore principal. Documentação histórica é mantida apenas como changelog — não como fonte de verdade para progresso.",
      "aplicacao": "Qualquer conflito entre indicadores de progresso registrados em documentos de acompanhamento (ex.: Documento de Continuidade v2.9) e a arvore_repositorio (Parte D) deve ser resolvido pela arvore_repositorio, que representa o estado real dos arquivos. Parte A e Parte C — que continham os campos originais progresso_atual e status_migracao — foram arquivadas; a regra permanece válida para qualquer documento de acompanhamento que venha a substituí-las."
    },
    "P4_ltriptofano_tag": {
      "titulo": "Remoção da Tag augmentation_ssri do L-Triptofano",
      "tipo": "DECISÃO CLÍNICA — SEGURANÇA",
      "status": "CORRIGIDO ✅",
      "decisao": "Remover a tag augmentation_ssri do exemplo e de qualquer JSON de ltriptofano.",
      "motivo": "A associação de L-triptofano com medicamentos serotoninérgicos (SSRI/SNRI) exige avaliação clínica específica e não deve aparecer como recomendação automática ou padrão do sistema. Risco de síndrome serotoninérgica.",
      "tags_corretas_ltriptofano": [
        "serotonina",
        "melatonina",
        "depressao_leve",
        "insonia",
        "precursor_serotoninergico",
        "monoterapia_depressao"
      ],
      "tags_removidas": ["augmentation_ssri"],
      "nota_seguranca": "A associação de precursores ou moduladores serotoninérgicos com antidepressivos deve depender de avaliação clínica individualizada e não de regras automáticas.",
     },
    "P5_b15_autofagia_mtor": {
      "titulo": "Classificação do Mecanismo B15 — Autofagia, mTOR e Clearance",
      "tipo": "DECISÃO ARQUITETURAL",
      "status": "DEFINIDO ✅",
      "decisao": "B15 mantido como mecanismo secundário / emergente na arquitetura v2.5.",
      "classificacao": {
        "tipo": "mecanismo_emergente",
        "prioridade_clinica": "secundaria",
        "nivel_evidencia": "moderado",
        "influencia_algoritmos_principais": "baixa"
      },
      "justificativa": "Existe literatura relacionando mTOR, autofagia, neuroplasticidade, BDNF, cetamina, neuroinflamação e envelhecimento cerebral. Entretanto, o mecanismo não possui o mesmo peso clínico e operacional dos mecanismos centrais do sistema.",
      "mecanismos_centrais_referencia": [
        "mecanismo_B1_neuroinflamacao",
        "mecanismo_B2_eixo_hpa_cortisol",
        "mecanismo_B3  Neuroplasticidade          ← MECANISMO INTEGRADOR CENTRAL",
        "mecanismo_B7_eixo_intestino_cerebro",
        "mecanismo_B8_deficiencias_micronutrientes"
      ],
      "diretrizes_modelagem": {
        "manter_ativo": true,
        "mover_para_backlog": false,
        "remover_da_arvore": false,
        "usar_como_mecanismo_prioritario": false,
        "usar_como_gatilho_principal_protocolos": false,
        "permitir_influencia_complementar_regras_combinadas": true
      },
      "status_final": "mecanismo_secundario_emergente"
		},
	  "P6_arquitetura_modular_prevalece_sobre_template_monolitico": {
	  "titulo": "Arquitetura Modular Prevalece sobre Template Monolítico Histórico",
	  "tipo": "NOTA DE RECONCILIAÇÃO — PRINCÍPIO GERAL",
	  "status": "RESOLVIDO ✅",
	  "decisao": "Sempre que um módulo tiver arquitetura modular vigente (implementada em KIT específico) e também um template monolítico histórico, a arquitetura modular do KIT é a oficial. O template monolítico serve só como referência de campos, nunca como instrução de geração.",
	  "aplicacoes_confirmadas": [
		{"modulo": "C-ESC", "fonte_viva": "KIT_C_ESC", "arquivos": ["core","estrutura_escala","interpretacao","psicometria","monitoramento","alertas","semantic"]},
		{"modulo": "B-MEC (mecanismos)", "fonte_viva": "KIT_MECANISMO", "arquivos": ["core","fisiopatologia","evidencias","alvos_terapeuticos","semantic"]}
	  ],
	  "nota": "Não há conflito funcional — apenas diferença de representação entre a fonte histórica que originou o template e o KIT que hoje o implementa."
	  },
      }
    "P7_json_d_comp": {
      "titulo": "Template para Seções D6-D10 (Complementares)",
      "tipo": "NOTA DE RECONCILIAÇÃO",
      "status": "RESOLVIDO ✅",
      "decisao": "As seções D6-D10 (secao_exercicio, secao_sono_luz, secao_trauma_epigenetica, secao_dieta_nutricao, secao_psicoterapia) seguem o template modular definido na árvore D (5 arquivos: core, evidencias, protocolos, regras, semantic).",
      "template_oficial": "D-COMP — definido na arvore_repositorio da Parte D",
      "arquivos_por_secao": [
        "core.json",
        "evidencias.json",
        "protocolos.json",
        "regras.json",
        "semantic.json"
      ],
      "nota": "O template de suplementos (D1-D5), hoje implementado em KIT_SUPLEMENTO, é exclusivo para suplementos e não deve ser confundido com D-COMP. D-COMP ainda não tem KIT próprio — só a estrutura de pastas existe hoje."
    },
    "P8_epidemiologia_modular": {
      "titulo": "Estrutura da Seção A_EPIDEMIOLOGIA",
      "tipo": "NOTA DE RECONCILIAÇÃO",
      "status": "RESOLVIDO ✅",
      "decisao": "A seção A_EPIDEMIOLOGIA evoluiu de estrutura simples (1 arquivo) para estrutura modular (1 pasta × 5 arquivos). A árvore atual substitui integralmente a descrição anterior.",
      "estrutura_atual": {
        "fonte": "PARTE_D — arvore_repositorio.A_EPIDEMIOLOGIA",
        "arquivos": [
          "core.json",
          "dados_prevalencia.json",
          "impacto_saude_publica.json",
          "evidencias_reversibilidade.json",
          "semantic.json"
        ]
      },
      }
    "P9_acento_b3": {
      "titulo": "Correção de Acento no ID do Mecanismo B3",
      "tipo": "DECISÃO ARQUITETURAL",
      "status": "CORRIGIDO ✅",
      "regra_ids": "IDs e nomes de diretórios devem seguir: letras minúsculas, números, underscore, sem espaços, sem acentos, sem caracteres especiais.",
      "correcao": {
        "incorreto": "mecanismo_B3_bdnf_neurogênese",
        "correto": "mecanismoB3  Neuroplasticidade          ← MECANISMO INTEGRADOR CENTRAL"
      },
      }
    "P10_coesao_vs_completude": {
      "titulo": "Distinção entre Coesão Estrutural e Completude de Conteúdo",
      "tipo": "NOTA METODOLÓGICA",
      "status": "DEFINIDO ✅",
      "decisao": "Coesão estrutural não implica completude de conteúdo.",
      "definicoes": {
        "coesao_estrutural": "Todas as 5 partes do briefing usam os mesmos IDs, templates, versões e regras — sem contradições internas.",
        "completude_conteudo": "Todos os JSONs previstos foram gerados com conteúdo clínico real."
      },
      "regra": "Uma seção pode estar estruturalmente correta e semanticamente integrada e ainda assim possuir conteúdo pendente. As métricas devem ser avaliadas separadamente.",
      "aplicacao": "O campo auditoria_cruzada_v2_5 na Parte D declara coesão estrutural — não completude. Adicionar nota: 'escopo_auditoria: coesão entre as 5 partes do briefing — não implica completude dos JSONs gerados. Ver progresso_geral para status de geração.'"
    },
    "P11_hierarquia_fontes": {
      "titulo": "Hierarquia Oficial de Fontes de Verdade",
      "tipo": "DECISÃO ARQUITETURAL",
      "status": "DEFINIDO ✅",
      "regra": "Em caso de conflito entre documentos, prevalece a fonte de maior precedência na hierarquia abaixo.",
      "hierarquia": [
        "1. DECISOES_ARQUITETURAIS_v2_5.json — decisões explícitas prevalecem sobre tudo",
        "2. _ids_oficiais.json — catálogo canônico de IDs. Escopo: existência e validade de IDs",
        "3. PARTE_D (arvore_repositorio) — fonte de verdade de estrutura de pastas, organização e contagens.",
       "4. KITs (KIT_MECANISMO, KIT_SUPLEMENTO, KIT_C_ESC, KIT_C_LAB, KIT_CENARIO) — templates e guia de construção de JSON modular",
       "5. PROMPT_GERADOR_* (mecanismos e demais grupos de módulo) — geração de Biblioteca de Conhecimento",
       "6. (histórico) Partes A, B, C, E — arquivadas em [28/07/26]. Consultar apenas como changelog/rationale, nunca como fonte ativa.
      ],
      "aplicacao": "Qualquer conflito futuro entre partes deve ser resolvido consultando esta hierarquia de cima para baixo, sem necessidade de revisão manual de todas as partes.",
      "escopo_precedencia": {
        "nota": "A hierarquia define quem prevalece. O escopo define em quê cada fonte prevalece.",
        "_ids_oficiais.json": "Catálogo canônico de IDs — validade e existência. Um ID não listado aqui não existe no sistema, independente do que qualquer outra parte declare.",
        "PARTE_D": "Estrutura física, organização de pastas e contagens. Em conflito de total_exames ou total_arquivos entre PARTE_D e _ids_oficiais.json, PARTE_D prevalece para contagens estruturais.",
        "exemplo_conflito": {
          "cenario": "PARTE_D declara total_exames=30. _ids_oficiais.json lista 29 IDs de exames.",
          "resolucao": "_ids_oficiais.json vence para IDs (29 IDs são os válidos). PARTE_D vence para estrutura (30 pastas fisicamente existentes — 1 pode estar pendente de ID). Investigar a divergência antes de gerar JSONs."
        }
      },
      "se_ambiguo": "Registrar em BACKLOG_TECNICO.json como pendente_resolucao. NUNCA gerar output com conflito silencioso não resolvido."
    },
    "P12_natureza_sistema": {
      "titulo": "Declaração Oficial da Natureza do Sistema",
      "tipo": "DECISÃO ARQUITETURAL — PROTEÇÃO JURÍDICA",
      "status": "DEFINIDO ✅",
      "decisao": "O sistema é classificado como ferramenta de suporte à decisão clínica — não realiza diagnóstico nem substitui julgamento profissional.",
      "schema_obrigatorio": {
        "campo": "natureza_sistema",
        "enforcement": "hard_fail — ausência de natureza_sistema em qualquer output clínico invalida o arquivo. A definição operacional e o mecanismo de verificação estão em _regras_globais.json (R06_output_obrigatorio).",
        "incluir_em": "todos os módulos clínicos com output",
        "lista_explicita_modulos_output": [
          "JSON_D (template suplemento)",
          "JSON_E (template cenário)",
          "JSON_F (resumo executivo)",
          "algoritmo_resultado_protocolo.json",
          "_regras_globais.json",
          "_fluxo_primeira_consulta.json",
          "_interacoes_cruzadas_globais.json",
          "_ids_oficiais.json"
        ],
        "estrutura": {
          "tipo": "suporte_decisao_clinica",
          "nao_substitui_julgamento_profissional": true,
          "nao_realiza_diagnostico": true,
          "decisao_final_profissional": true
        }
      },
      "justificativa_juridica": "A declaração explícita de que o sistema apoia decisões — e não as realiza — é requisito arquitetural para proteção do desenvolvedor. O campo 'Responsabilidade de aplicação é do profissional' é necessário mas insuficiente isoladamente. A combinação dos dois estabelece que: (a) o sistema é ferramenta, não agente clínico; (b) o profissional detém o julgamento final; (c) o sistema não realiza diagnóstico.",
      "diferenca_critica": {
        "sistema_suporte": "Apresenta dados, evidências, alertas e recomendações baseadas em protocolo",
        "diagnostico": "Conclusão clínica sobre condição do paciente — exclusividade do profissional habilitado"
      },
      "arquivos_corrigir": [
        "JSON_D (template suplemento)",
        "JSON_E (template cenário)",
        "JSON_F (resumo executivo)",
        "algoritmo_resultado_protocolo.json",
        "_regras_globais.json"
      ]
    },
    "P13_ordem_execucao_seguranca": {
      "titulo": "Ordem Canônica de Execução do Pipeline de Segurança",
      "tipo": "DECISÃO ARQUITETURAL",
      "status": "DEFINIDO ✅",
      "decisao": "A ordem de execução do pipeline de segurança clínica é canônica e única em todo o sistema.",
      "ordem_canonica": [
        "1. Risco vital — R01 absoluto — prevalece sobre tudo",
        "2. Restrições legais por perfil — profissional pode prescrever?",
        "3. Contraindicações absolutas — paciente pode receber?",
        "4. Interações críticas — combinação é segura?",
        "5. Eficácia — evidência suficiente?",
        "6. Output — gerar apenas se todas anteriores aprovadas"
      ],
      "justificativa": "Restrições legais antes de CI absolutas porque se o profissional não pode prescrever, todo processamento posterior é irrelevante. CI absolutas antes de interações porque existem independentemente de combinações. Interações só fazem sentido após confirmar que profissional pode e paciente pode receber.",
      "arquivos_corrigir": [
        "_regras_globais.json — R05.ordem_execucao"
      ],
      "conflito_resolvido": "Conflito histórico resolvido durante consolidação da v2.5."
    },
    "P14_perfil_enfermeiro": {
      "titulo": "Perfil Enfermeiro — Escopo de Atuação no Sistema",
      "tipo": "DECISÃO ARQUITETURAL",
      "status": "DEFINIDO ✅",
      "decisao": "Perfil enfermeiro MANTIDO com escopo baseado em evidência GRADE B e base legal brasileira.",
      "justificativa": "C-SSRS foi desenvolvida para uso por qualquer profissional de saúde treinado. Avaliação de risco suicida em triagem é competência de enfermagem (COFEN 564/2017). Rastreio de risco vital não configura teste psicológico (CFP 09/2018).",
      "base_evidencia": {
        "grade": "B",
        "referencias": [
          {
            "autor": "Posner K et al.",
            "ano": 2011,
            "revista": "Psychiatry",
            "volume": "68(12)",
            "paginas": "1066-1077",
            "resultado": "C-SSRS desenvolvida para uso por qualquer profissional de saúde treinado — não restrita a médicos ou psicólogos"
          },
          {
            "autor": "Mundt JC et al.",
            "ano": 2013,
            "revista": "Depression and Anxiety",
            "volume": "30(8)",
            "paginas": "777-783",
            "n": 284,
            "resultado": "Validação multi-profissional incluindo enfermeiros de triagem"
          }
        ]
      },
      "base_legal": [
        "COFEN Resolução 564/2017 — avaliação e mensuração de riscos à saúde como competência de enfermagem (Art. 35)",
        "Lei 7.498/1986 — regulamentação do exercício de enfermagem",
        "CFP Resolução 09/2018 — rastreio de risco vital NÃO configura teste psicológico restrito"
      ],
      "escopo_pode": [
        "exame_phq9",
        "exame_gad7",
        "exame_dass21",
        "exame_isi",
        "exame_pss",
        "exame_mbi",
        "exame_cssrs — aplicação completa em contexto de triagem e emergência"
      ],
      "escopo_nao_pode": [
        "exame_ham_d",
        "exame_ham_a",
        "exame_ybocs",
        "exame_pdss"
      ],
      "escopo_cautela": [
        "exame_pcl5 — encaminhar obrigatoriamente se pontuação ≥33"
      ],
      "diferenca_naturopata": {
        "naturopata": "exame_cssrs — rastreio itens 1-2 (ideação passiva) apenas",
        "enfermeiro": "exame_cssrs — aplicação completa em contexto de triagem e emergência"
      },
      "arquivos_implementados": [
        "_regras_globais.json — R02 ✅",
        "_fluxo_primeira_consulta.json — bloco_1 ✅"
      ],
      "arquivos_atualizar_sprint2": [
        "exame_cssrs/alertas.json — adicionar enfermeiro em aplicadores_autorizados",
        "demais alertas.json C-ESC — verificar se enfermeiro está corretamente mapeado"
      ],
      "sem_implementacao_estrutural": true,
      "nota": "Não requer pasta, caminho, template ou JSON próprio. Regra operacional implementada em _regras_globais.json. alertas.json das escalas serão atualizados naturalmente no Sprint 2."
  	 },
	  "P15_hierarquia_conceitual_b3_central": {
	  "titulo": "B3 — Neuroplasticidade como Mecanismo Integrador Central da Biblioteca de Mecanismos",
	  "tipo": "DECISÃO ARQUITETURAL",
	  "status": "DEFINIDO ✅",
	  "decisao": "B3 (Neuroplasticidade) é formalmente designado o mecanismo integrador central de toda a Biblioteca de Mecanismos (B1–B16). Todo mecanismo da biblioteca deve conter uma seção explícita descrevendo como suas vias biológicas influenciam a neuroplasticidade.",
	  "contexto": "A biblioteca de mecanismos cresceu de forma incremental (B1 em auditoria, demais em construção), sem uma diretriz explícita de integração central. Isso gerou risco de tratamento isolado de vias com papel bem estabelecido na literatura como moduladoras de plasticidade sináptica (ex: neuroinflamação, eixo HPA, microbiota-intestino-cérebro), sem conexão declarada ao nó conceitual comum.",
	  "escopo_b3": [
		"Plasticidade sináptica (LTP/LTD)",
		"Remodelamento dendrítico e espinhas dendríticas",
		"Densidade sináptica e conectividade funcional",
		"Aprendizagem, memória e flexibilidade cognitiva",
		"Redes cortico-límbicas",
		"Vias moleculares: BDNF, CREB, mTOR, Arc, PSD-95, Synapsin, GAP-43"
	  ],
	  "regra_pratica": "Campo obrigatório 'influencia_neuroplasticidade' (ou equivalente semântico) em cada arquivo de mecanismo B1-B16, descrevendo objetivamente a via de conexão com B3 (1-2 frases, direção do efeito, nível de evidência). Ausência deste campo em mecanismo já auditado deve ser registrada como pendência em BACKLOG_TECNICO.json.",
	  "justificativa": "Formalizar B3 como nó central evita fragmentação conceitual entre mecanismos e melhora a navegabilidade semântica da biblioteca, permitindo que a Ontologia correlacione mecanismos distintos por meio de um eixo comum, em vez de tratá-los como silos independentes.",
	  "impacto": {
		"mecanismos_afetados": "B1–B16 (todos)",
		"acao_requerida": "Auditoria retroativa de cada mecanismo já publicado ou em auditoria, para verificar/inserir a seção de conexão com B3",
		"mecanismos_com_revisao_pendente": ["mecanismo_B1_neuroinflamacao"]
	  },
	  "nota_nomenclatura": "O ID oficial 'mecanismo_B3_bdnf_neurogenese' (acento corrigido em P9) contém o termo 'neurogenese' em sua nomenclatura, o que hoje gera sobreposição conceitual com B16 (mecanismo dedicado exclusivamente à neurogênese — ver P16). Recomenda-se avaliar em v2.6+ a renomeação do ID para algo como 'mecanismo_B3_neuroplasticidade', mantendo BDNF como via molecular pertencente ao escopo de B3, sem repetir 'neurogenese' no nome do ID. Não executar renomeação em v2.5 — apenas registrar.",
	  "arquivos_corrigir": [
		"PARTE_D — arvore_repositorio (avaliação de nomenclatura futura, sem execução em v2.5)",
		"BACKLOG_TECNICO.json — registrar avaliação de renomeação de ID para v2.6"
	  ]
	},
	"P16_neurogenese_b16_especializado": {
	  "titulo": "B16 — Neurogênese como Mecanismo Especializado Subordinado a B3 e Regra Anti-Duplicação",
	  "tipo": "DECISÃO ARQUITETURAL",
	  "status": "DEFINIDO ✅",
	  "decisao": "B16 (Neurogênese) é o mecanismo especializado e componente da neuroplasticidade (B3), dedicado exclusivamente à geração, maturação e integração de novos neurônios. Nos mecanismos B1-B15, a neurogênese só pode ser abordada como consequência ou moduladora da neuroplasticidade — o aprofundamento do tema ocorre exclusivamente em B16.",
	  "hierarquia_formal": {
		"b3_neuroplasticidade": {
		  "subcomponentes": [
			"plasticidade_sinaptica",
			"remodelamento_dendritico",
			"reorganizacao_de_circuitos",
			"b16_neurogenese (mecanismo especializado)"
		  ]
		}
	  },
	  "principio_logico": "Toda neurogênese contribui para a neuroplasticidade. Nem toda neuroplasticidade depende de neurogênese.",
	  "regra_anti_duplicacao": "Conteúdo aprofundado sobre neurogênese (proliferação de células-tronco neurais, migração, diferenciação, integração sináptica de novos neurônios, zona subgranular do hipocampo, etc.) reside exclusivamente em B16. Mecanismos B1-B15 que mencionem neurogênese devem fazê-lo em 1-2 frases, no papel de efeito/consequência, com referência cruzada ao ID oficial de B16 — nunca replicando o conteúdo mecanístico completo.",
	  "justificativa": "Sem essa regra, mecanismos com literatura tangencial a neurogênese (ex: B2 eixo HPA/cortisol, B7 intestino-cérebro, B8 micronutrientes) tenderiam a desenvolver seções extensas próprias sobre o tema, criando múltiplos pontos de verdade divergentes para os mesmos processos biológicos. É extensão direta do mesmo princípio anti-duplicação já aplicado entre Biblioteca de Mecanismo e módulos operacionais (ver P16 anterior sobre biomarcadores/suplementos, se aplicável neste documento) e em KIT_SUPLEMENTO/NT_TEMPLATE: uma única fonte de verdade por dado, referenciada por ID.",
	  "escopo_b16": [
		"Proliferação de células-tronco/progenitoras neurais",
		"Migração neuronal",
		"Diferenciação e maturação de novos neurônios",
		"Integração sináptica funcional de neurônios recém-formados",
		"Zona subgranular do giro denteado e zona subventricular",
		"Fatores reguladores específicos de neurogênese (ex: Wnt, Notch, Sonic Hedgehog aplicados à neurogênese)"
	  ],
	  "diferenca_de_b3": "B3 trata da plasticidade em sentido amplo, incluindo remodelamento de circuitos e sinapses já existentes (LTP/LTD). B16 trata exclusivamente da criação de novas unidades neuronais. B16 é subconjunto/especialização de B3 — não um mecanismo paralelo e independente.",
	  "aplicacao": "Aplicar retroativamente durante auditoria de cada biblioteca de mecanismo já iniciada (ex: B1). Onde B1-B15 já contenham parágrafos extensos sobre neurogênese, mover o conteúdo para B16 (se ainda não coberto) e substituir por referência cruzada + resumo de 1-2 frases.",
	  "status_dependente": "Depende de confirmação se 'mecanismo_B16_neurogenese' já existe em _ids_oficiais.json. Caso não exista, registrar criação formal em BACKLOG_TECNICO.json antes de aplicar a regra anti-duplicação retroativamente.",
	  "arquivos_corrigir": [
		"_ids_oficiais.json — confirmar/criar entrada mecanismo_B16_neurogenese",
		"PARTE_D — arvore_repositorio, incluir pasta mecanismo_B16_neurogenese se ainda não existente",
		"mecanismo_B1_neuroinflamacao (e demais mecanismos já auditados) — revisar menções a neurogênese conforme regra_anti_duplicacao"
	  ]
	},
		"P17_atualizacao_lista_mecanismos_b3_b12_b16": {
	  "titulo": "Atualização da Lista Oficial de Mecanismos — Renomeação de B3 e B12, Inclusão de B16",
	  "tipo": "DECISÃO ARQUITETURAL",
	  "status": "DEFINIDO ✅",
	  "decisao": "A lista oficial de mecanismos (mecanismos_ativos) passa de 15 para 16 itens. Os IDs mecanismo_B3_bdnf_neurogenese e mecanismo_B12_neuroplasticidade_trauma são renomeados para eliminar sobreposição semântica com a hierarquia B3↔B16 formalizada em P15/P16. É criado o novo mecanismo mecanismo_B16_neurogenese.",
	  "resolve_pendencia": "Esta decisão executa e encerra a avaliação registrada como pendente-não-executada em P15.nota_nomenclatura ('recomenda-se avaliar em v2.6+... Não executar renomeação em v2.5 — apenas registrar'). Com a formalização explícita da arquitetura de 16 mecanismos, a renomeação deixa de ser uma antecipação e passa a ser execução imediata dentro da própria v2.5.",
	  "tabela_migracao_ids": [
		{
		  "posicao": "B3",
		  "id_antigo": "mecanismo_B3_bdnf_neurogenese",
		  "id_novo": "mecanismo_B3_neuroplasticidade",
		  "titulo_oficial": "Neuroplasticidade",
		  "motivo": "Remove 'neurogenese' do nome — neurogênese é escopo exclusivo de B16 (P16). BDNF permanece como via molecular dentro do escopo de B3 (ver P15.escopo_b3), mas não integra mais o ID.",
		  "marcador": "MECANISMO INTEGRADOR CENTRAL"
		},
		{
		  "posicao": "B12",
		  "id_antigo": "mecanismo_B12_neuroplasticidade_trauma",
		  "id_novo": "mecanismo_B12_neurobiologia_trauma",
		  "titulo_oficial": "Neurobiologia do Trauma",
		  "motivo": "Remove 'neuroplasticidade' do nome — o termo é reservado a B3 como mecanismo integrador central (P15). B12 continua descrevendo os efeitos do trauma sobre circuitos neurais, mas referencia B3 via campo influencia_neuroplasticidade (P15.regra_pratica) em vez de carregar o termo no próprio ID."
		},
		{
		  "posicao": "B16",
		  "id_antigo": null,
		  "id_novo": "mecanismo_B16_neurogenese",
		  "titulo_oficial": "Neurogênese",
		  "motivo": "Novo mecanismo especializado, componente de B3, conforme P16. Encerra a pendência status_dependente registrada em P16.",
		  "marcador": "MECANISMO ESPECIALIZADO COMPONENTE DE B3"
		}
	  ],
	  "lista_mecanismos_atualizada": [
		"mecanismo_B1_neuroinflamacao",
		"mecanismo_B2_eixo_hpa_cortisol",
		"mecanismo_B3_neuroplasticidade",
		"mecanismo_B4_deficiencias_monoaminas",
		"mecanismo_B5_gaba_glutamato",
		"mecanismo_B6_estresse_oxidativo",
		"mecanismo_B7_eixo_intestino_cerebro",
		"mecanismo_B8_deficiencias_micronutrientes",
		"mecanismo_B9_disfuncao_mitocondrial",
		"mecanismo_B10_desregulacao_circadiana",
		"mecanismo_B11_disfuncao_tireoidiana",
		"mecanismo_B12_neurobiologia_trauma",
		"mecanismo_B13_sistema_endocanabinoide",
		"mecanismo_B14_neuroesteroides_hormonios",
		"mecanismo_B15_autofagia_mtor",
		"mecanismo_B16_neurogenese"
	  ],
	  "titulos_display_atualizados_nao_afetam_id": {
		"nota": "Os títulos abaixo foram expandidos/ajustados na documentação de referência do usuário, mas NÃO exigem alteração de ID — divergem apenas como nome de exibição (rótulo), não como slug estrutural. Mantidos por rastreabilidade.",
		"mecanismo_B7_eixo_intestino_cerebro": "Disbiose e Eixo Intestino-Cérebro",
		"mecanismo_B10_desregulacao_circadiana": "Desregulação Circadiana e Sono"
	  },
	  "impacto_contagens": {
		"total_mecanismos": "15 → 16",
		"nota_p10": "Coesão estrutural (lista atualizada) não implica completude de conteúdo — mecanismo_B16_neurogenese precisa de geração de conteúdo clínico completo, não apenas do registro do ID (aplicação direta de P10)."
	  },
	  "compatibilidade_retroativa": {
		"regra": "Qualquer referência cruzada a mecanismo_B3_bdnf_neurogenese ou mecanismo_B12_neuroplasticidade_trauma em arquivos já gerados (bibliotecas de mecanismo, algoritmos, protocolos, tags de suplementos/exames) deve ser buscada e substituída pelo novo ID. Não deve existir período de 'ID duplo válido' — a migração é imediata e total.",
	  "risco_se_nao_migrado": "Quebra de correlação na Ontologia (busca por ID antigo retorna vazio) e divergência silenciosa entre PARTE_D/arvore_repositorio e _ids_oficiais.json — exatamente o cenário que P11.escopo_precedencia instrui a nunca deixar sem resolução."
	  },
	  "arquivos_corrigir": [
		"_ids_oficiais.json — atualizar IDs de B3 e B12, adicionar B16",
		"PARTE_D — arvore_repositorio (renomear pastas de B3/B12, criar pasta de B16), atualizar contagens de mecanismos",
		"mecanismo_B1_neuroinflamacao (e demais já auditados) — atualizar referências cruzadas a B3/B12 nos campos influencia_neuroplasticidade",
		"BACKLOG_TECNICO.json — remover a pendência de avaliação registrada em P15 (id substituído por execução direta via P17)"
	  ]
	},
	"P18_bibliotecas_conhecimento_fonte_canonica": {
	  "titulo": "Bibliotecas de Conhecimento como Fonte Canônica e Prioritária de Conteúdo Científico",
	  "tipo": "DECISÃO ARQUITETURAL — GOVERNANÇA DE CONHECIMENTO",
	  "status": "DEFINIDO ✅",
	  "decisao": "As Bibliotecas de Conhecimento constituem a fonte canônica e prioritária de conhecimento científico da plataforma. Toda Narrativa Transversal, JSON Modular, motor de raciocínio clínico e demais componentes derivados devem utilizar exclusivamente a Biblioteca de Conhecimento correspondente como fonte primária de conteúdo, não realizando nova pesquisa bibliográfica nem introduzindo conhecimento externo.",
	  "regra_atualizacao": "Atualizações da literatura científica devem ser incorporadas inicialmente à Biblioteca de Conhecimento correspondente. Somente após essa atualização os artefatos derivados podem ser regenerados. Nunca o inverso — nenhum artefato derivado pode introduzir evidência científica nova que não esteja primeiro refletida na Biblioteca de Conhecimento correspondente.",
	  "regra_precedencia_conflito": "Em caso de divergência entre uma Biblioteca de Conhecimento e qualquer artefato derivado, a Biblioteca de Conhecimento prevalece obrigatoriamente, devendo o artefato derivado ser regenerado ou corrigido. Não há espaço para interpretação caso a caso — a precedência é automática e independe do tipo ou da idade do artefato divergente.",
	  "justificativa": "Sem uma fonte única de verdade para conhecimento científico, cada artefato derivado (narrativa de suplemento, JSON de cenário, algoritmo de protocolo) tenderia a buscar e citar literatura de forma independente, gerando: (a) inconsistência entre módulos que tratam do mesmo tema científico; (b) impossibilidade de auditar de onde vem uma afirmação clínica específica; (c) risco de desatualização assimétrica, onde um artefato reflete uma versão da literatura mais nova que outro. Centralizar a entrada de conhecimento científico nas Bibliotecas de Conhecimento resolve os três problemas simultaneamente.",
	  "fluxo_obrigatorio": {
		"diagrama": [
      "Literatura científica nova",
      "↓",
      "Biblioteca de Conhecimento",
      "↓",
      "Revisão / Atualização",
      "↓",
      "Narrativas Transversais | JSON Modular | Algoritmos | Motor Clínico"
		],
		"entrada_conhecimento": "Literatura científica nova → Biblioteca de Conhecimento correspondente → revisão/atualização formal",
		"consumo_conhecimento": "Biblioteca de Conhecimento (atualizada) → todos os artefatos derivados regenerados a partir dela",
		"proibido": "Qualquer artefato derivado inserir citação, evidência ou dado científico que não exista na Biblioteca de Conhecimento correspondente no momento da geração"
	  },
	  "escopo_bibliotecas_conhecimento": {
		"nota": "Esta decisão é agnóstica ao número e tipo de Bibliotecas de Conhecimento existentes na plataforma. Aplica-se igualmente às já existentes e a quaisquer futuras, sem necessidade de revisão desta decisão quando novas bibliotecas forem criadas.",
		"exemplos_atuais_nao_exaustivos": [
      "Bibliotecas de Mecanismo (B1-B16)",
      "Bibliotecas de Biomarcadores e Exames",
      "Bibliotecas de Intervenções e Suplementos",
      "Bibliotecas de Cenários Clínicos"
    ],
		"aviso": "A lista acima é ilustrativa do estado atual — não é normativa nem exaustiva. Novas categorias de Biblioteca de Conhecimento entram automaticamente sob esta decisão, sem exigir nova entrada em DECISOES_ARQUITETURAIS."
	  },
	"relacao_com_p20": "Complementar a P20 — Biblioteca de Conhecimento é fonte canônica de conteúdo científico; P20 define os limites desse conteúdo frente a dados operacionais de outros módulos."
	  "relacao_com_p11": {
		"gap_identificado": "A hierarquia de fontes de P11 trata de precedência estrutural e de identidade/negócio, mas não posiciona explicitamente as Bibliotecas de Conhecimento nessa cadeia.",
		"resolucao": "As Bibliotecas de Conhecimento não substituem a hierarquia de P11 — operam em eixo ortogonal e específico: são a fonte canônica exclusivamente para CONTEÚDO CIENTÍFICO (evidências, mecanismos biológicos, associações). Para ESTRUTURA, IDs e regras de negócio, a hierarquia de P11 permanece integralmente válida sem alteração.",
		"acao_requerida": "Adicionar em P11.escopo_precedencia uma entrada específica para Bibliotecas de Conhecimento, esclarecendo esse escopo ortogonal."
	  },
	  "risco_se_nao_seguido": "Divergência de evidência científica entre módulos que tratam do mesmo tema (ex: JSON de suplemento afirma algo diferente do que a Biblioteca de Conhecimento correspondente estabelece sobre o mesmo biomarcador/mecanismo), sem possibilidade de auditoria de qual é a versão correta — cenário resolvido automaticamente pela regra_precedencia_conflito acima.",
	  "aplicacao": "Aplica-se a todos os artefatos derivados da plataforma — Narrativas Transversais, JSON Modular, algoritmos de protocolo e qualquer motor de raciocínio clínico do pipeline, presentes ou futuros.",
	  "arquivos_corrigir": [
		
		"_regras_globais.json — considerar adicionar regra formal (ex: R09) operacionalizando esta checagem e a regra_precedencia_conflito",
		"P11 — adicionar nota de escopo ortogonal para Bibliotecas de Conhecimento (ver relacao_com_p11.acao_requerida)"
	  ]
	},
    	"P_EVID_01_qualidade_evidencia_cientifica": {
		  "titulo": "Política de Qualidade do Conhecimento Científico",
		  "tipo": "POLÍTICA DE GOVERNANÇA CIENTÍFICA",
		  "status": "DEFINIDO ✅",
		  "decisao": "As regras de qualidade da literatura científica — critérios de seleção das evidências, atualidade, robustez metodológica e sistema de rating para intervenções e sugestões clínicas — estão definidas nos prompts de geração das bibliotecas (Mecanismos, Biomarcadores e Exames, Intervenções e Suplementos, Cenários Clínicos). Esses prompts constituem a especificação operacional oficial desta política.",
		  "relacao_com_p18": "Detalha o critério de qualidade aplicado na etapa de 'revisão/atualização' do fluxo obrigatório definido em P18."
		},

		"P_EVID_02_fontes_cientificas": {
		  "titulo": "Política de Fontes Científicas",
		  "tipo": "POLÍTICA DE GOVERNANÇA CIENTÍFICA",
		  "status": "DEFINIDO ✅",
		  "decisao": "As regras de seleção das bases de busca e das fontes permitidas/proibidas estão definidas nos prompts de geração das bibliotecas e devem ser aplicadas integralmente.",
		  "relacao_com_p18": "Define a origem legítima de entrada de conhecimento citada em P18.fluxo_obrigatorio."
		},
		"P19_reconciliacao_catalogo_ids_146_vs_132": {
		  "titulo": "Reconciliação de Divergência entre Snapshots do Catálogo de IDs (146 vs 132) e Correlação Mecanística Obrigatória",
		  "tipo": "DECISÃO ARQUITETURAL — INCIDENTE DE PROCESSO",
		  "status": "DEFINIDO ✅",
		  "decisao": "O catálogo _ids_oficiais.json restaura os 146 IDs originais (9 exames individuais de C4/C5/C8 + categoria C11_estresse_oxidativo completa + cenario_E99), preservando integralmente as notas de segurança e governança introduzidas na auditoria intermediária de 132 IDs (notas_seguranca, nota_dhea, regra_novo_id, nota_desenvolvimento, exemplo_canonico).",
		  "causa_raiz": "Duas linhas de evolução do catálogo se desenvolveram em paralelo — uma aplicou correções estruturais e notas de segurança (132 IDs), outra expandiu o escopo de conteúdo (146 IDs) — sem que uma linha herdasse automaticamente os avanços da outra, exigindo reconciliação manual consciente.",
		  "regra_processo_derivada": "Toda nova auditoria de _ids_oficiais.json deve executar diff item-a-item contra a última versão confirmada antes de ser aceita como substituição. Verificação apenas por total numérico é insuficiente — remoções e adições simultâneas podem coincidir no total.",
		  "correlacao_mecanistica_obrigatoria": {
			"nota": "Todo ID restaurado que representa biomarcador precisa de correlação mecanística declarada. Tabela abaixo é normativa — não pode ser gerado conteúdo de mecanismo B1/B2/B3/B4/B6/B9/B14 sem contemplar os biomarcadores correlatos listados.",
			"tabela": [
		  { "ids": ["exame_il1beta", "exame_tnfalpha"], "mecanismo_primario": "mecanismo_B1_neuroinflamacao" },
		  { "ids": ["exame_razao_kyn_trp"], "mecanismo_primario": "mecanismo_B1_neuroinflamacao", "mecanismo_secundario": "mecanismo_B4_deficiencias_monoaminas" },
		  { "ids": ["exame_acth"], "mecanismo_primario": "mecanismo_B2_eixo_hpa_cortisol" },
		  { "ids": ["exame_estradiol", "exame_progesterona", "exame_testosterona_shbg"], "mecanismo_primario": "mecanismo_B14_neuroesteroides_hormonios", "mecanismo_secundario": "mecanismo_B2_eixo_hpa_cortisol" },
		  { "ids": ["exame_apoe"], "mecanismo_primario": "mecanismo_B9_disfuncao_mitocondrial", "mecanismo_secundario": ["mecanismo_B6_estresse_oxidativo", "mecanismo_B3_neuroplasticidade"], "nota": "Correlação tripla — maior risco de conteúdo incompleto, priorizar auditoria" },
		  { "ids": ["exame_snps_inflamatorios"], "mecanismo_primario": "mecanismo_B1_neuroinflamacao" },
		  { "ids": ["exame_glutationa_gsh", "exame_gssg", "exame_8_ohdg", "exame_capacidade_antioxidante_total"], "mecanismo_primario": "mecanismo_B6_estresse_oxidativo", "nota": "Correlação exclusiva — categoria C11 inteira" },
		  { "ids": ["cenario_E99_urgencias_psiquiatricas"], "conecta_com": ["R01_risco_vital (_regras_globais.json)", "P13_ordem_execucao_seguranca"], "nota": "Não é mecanismo — é gatilho de prioridade máxima do pipeline" }
		]
	  },
	  "aplicacao_p20_anti_duplicacao": "A correlação acima é referência por ID (papel biológico resumido), não duplicação de conteúdo laboratorial completo — em conformidade com P20 (separação biblioteca de mecanismo vs módulos operacionais). Valores de corte de cada exame permanecem exclusivamente em seu próprio C-LAB.",
	  "arquivos_corrigir": [
		"_ids_oficiais.json — já corrigido",
		"mecanismo_B1_neuroinflamacao, B2, B3, B4, B6, B9, B14 — verificar se biomarcadores da tabela já constam; se ausentes, registrar em BACKLOG_TECNICO.json",
		"_fluxo_primeira_consulta.json e exame_cssrs/alertas.json — confirmar gatilho de cenario_E99"
	  ]
    },
		"P20_separacao_biblioteca_mecanismo_modulos": {
		  "titulo": "Separação de Escopo entre Biblioteca de Mecanismo e Módulos Operacionais (Biomarcadores, Suplementos, Escalas, Cenários)",
		  "tipo": "PRINCÍPIO ARQUITETURAL",
		  "status": "DEFINIDO ✅",
		  "decisao": "A Biblioteca de Mecanismo referencia biomarcadores, suplementos, escalas e cenários exclusivamente por ID oficial (_ids_oficiais.json) e descreve apenas seu papel biológico dentro do mecanismo em estudo. Valores numéricos de corte, faixas de referência, protocolos de coleta, doses, posologias e demais conteúdos operacionais NÃO são replicados na Biblioteca de Mecanismo — residem exclusivamente no módulo correspondente (C-LAB, C-ESC, D-SUPL, E-CEN). Quando qualquer elemento pertencente aos módulos citados acima ainda não possuir ID oficial catalogado, esse estado deve ser informado explicitamente em prosa, sem criação de IDs provisórios e sem utilização de marcadores de evidência científica.",
		  "justificativa": "Duplicar esse conteúdo cria dois pontos de verdade para o mesmo dado, com risco de divergência silenciosa e maior custo de manutenção. Extensão do princípio 'nunca duplicar informação entre arquivos' já aplicado em outras camadas do sistema.",
		  "regra_pratica": "Na Biblioteca de Mecanismo, ao referenciar elementos pertencentes aos módulos citados nesta decisão, citar o respectivo ID oficial e descrevê-los em 1–2 frases exclusivamente quanto ao seu papel biológico no mecanismo (direção do efeito, especificidade e nível de evidência, quando aplicável). Quando não existir ID oficial catalogado, informar apenas que o elemento ainda não foi catalogado no módulo correspondente. Esses elementos devem ser utilizados apenas como componentes da cascata mecanística, sem expandir para conteúdos próprios do módulo de origem, como fisiologia detalhada, farmacologia, tabelas de corte, protocolos de coleta, critérios diagnósticos, doses, posologias, algoritmos, fluxos decisórios ou recomendações clínicas.",
		 "aplicacao": "Válido para todas as bibliotecas de mecanismo, atuais e futuras."
	},
		"P21_gpm_ferramenta_pipeline": {
		  "titulo": "Gerador de Profundidade Molecular (GPM) — Ferramenta Preparatória do Pipeline de Mecanismos",
		  "tipo": "DECISÃO ARQUITETURAL",
		  "status": "DEFINIDO ✅",
		  "decisao": "O Gerador de Profundidade Molecular (GPM) é uma ferramenta preparatória do pipeline de geração de Bibliotecas de Conhecimento de mecanismos fisiopatológicos (B1-B16). Não é um artefato permanente da plataforma nem uma fonte independente de conhecimento clínico.",
		  "regra": "GPM não deve ser referenciado pela Ontologia, pelo JSON Modular, nem por nenhum módulo consumidor de conhecimento canônico. Existem 16 documentos GPM, um por mecanismo, cada um gerado a partir de um prompt-molde comum, precedido por um Briefing de direcionamento específico daquele mecanismo. O GPM alimenta exclusivamente a geração da Biblioteca via FASE_2-_01_PROMPT_4_0 correspondente e pode ser descartado após a aprovação da Biblioteca final.",
		  "escopo_relacao_p18": "GPM não é Biblioteca de Conhecimento (P18) nem a substitui — é insumo de trabalho que precede e alimenta a redação da Biblioteca. Após a Biblioteca aprovada, ela — não o GPM — passa a ser a fonte canônica, sujeita a regra_precedencia_conflito de P18.",
		  "natureza_ferramenta": "Esta ferramenta não está sujeita às mesmas exigências de rastreabilidade, versionamento e schema aplicadas aos artefatos permanentes (Biblioteca, Narrativa Transversal, JSON Modular). Mesma categoria de UNIVERSAL_CORE_COMPACTO e KIT_QUALIDADE_NARRATIVA — ver nota_desenvolvimento em _ids_oficiais.json, _interacoes_cruzadas_globais.json e _fluxo_primeira_consulta.json.",
		  "arquivos_corrigir": [
			"_ids_oficiais.json — nota_desenvolvimento: incluir GPM na lista de ferramentas de desenvolvimento externas ✅ concluído",
			"_interacoes_cruzadas_globais.json — nota_desenvolvimento: idem ✅ concluído",
			"_fluxo_primeira_consulta.json — nota_desenvolvimento: idem ✅ concluído"
		  ]
		},
	  "resumo_correcoes_pendentes": {
	  "nota": "Decisões já tomadas acima. Implementações ainda necessárias nos arquivos:",
    "correcoes": [
      {
        "id": "IMPL-01",
        "decisao": "P1",
        "acao": "Remover campo pendente_confirmacao e referências a slot_6",
        "status": "⏳ PENDENTE",
        "arquivos": ["PARTE_D"]
      },
      {
        "id": "IMPL-02",
        "decisao": "P2",
        "acao": "Mover exame_dexametasona de C-FUNC para C-LAB. Atualizar contagens: C-LAB 29→30, C-FUNC 10→9",
        "status": "⏳ PENDENTE",
        "arquivos": ["PARTE_D"]
      },
      {
        "id": "IMPL-03",
        "decisao": "P4",
        "acao": "Remover tag augmentation_ssri do exemplo ltriptofano",
        "status": "⏳ PENDENTE",
        "arquivos": []
      },
      {
        "id": "IMPL-04",
        "decisao": "P9",
        "acao": "Corrigir mecanismo_B3_bdnf_neurogênese → mecanismo_B3_bdnf_neurogenese",
        "status": "✅ CORRIGIDO — SUPERADO POR P17, aplicar diretamente o ID final mecanismo_B3_neuroplasticidade",
        "arquivos": ["PARTE_D"]
      },
      {
        "id": "IMPL-05",
        "decisao": "P12",
        "acao": "Adicionar campo natureza_sistema em todos os módulos clínicos com output",
        "status": "⏳ PARCIAL",
        "implementado_em": [
          "_regras_globais.json ✅",
          "_interacoes_cruzadas_globais.json ✅",
          "_ids_oficiais.json ✅",
          "_fluxo_primeira_consulta.json ✅"
        ],
        "pendente_em": [
          "JSON_D (template suplemento)",
          "algoritmo_resultado_protocolo.json"
        ]
      },
	  "id": "IMPL-06",
	  "decisao": "P14",
	  "acao": "Atualizar aplicadores_autorizados nas escalas C-ESC para incluir enfermeiro onde aplicável",
	  "status": "⏳ PENDENTE — executar durante Sprint 2",
	  "nota": "Implementação parcial — _regras_globais.json e _fluxo_primeira_consulta.json já implementados (ver P14.arquivos_implementados). Pendente: escalas C-ESC no Sprint 2.",
	  "arquivos": [
		"exame_cssrs/alertas.json",
		"demais alertas.json C-ESC conforme escopo P14"
	  ]
	},
	  "id": "IMPL-07",
	  "decisao": "P15",
	  "acao": "Inserir campo 'influencia_neuroplasticidade' em todos os mecanismos B1-B16 e registrar avaliação de renomeação do ID de B3 para v2.6",
	  "status": "⏳ PENDENTE",
	  "arquivos": ["mecanismo_B1_neuroinflamacao (e demais)", "PARTE_D", "BACKLOG_TECNICO.json"]
	},
	{
	  "id": "IMPL-08",
	  "decisao": "P16",
	  "acao": "Confirmar/criar mecanismo_B16_neurogenese em _ids_oficiais.json e revisar mecanismos já auditados para remover duplicação de conteúdo sobre neurogênese",
	  "status": "⏳ PENDENTE",
	  "arquivos": ["_ids_oficiais.json", "mecanismo_B1_neuroinflamacao", "PARTE_D"]
	},
	{
	  "id": "IMPL-09",
	  "decisao": "P17",
	  "acao": "Migrar IDs mecanismo_B3_bdnf_neurogenese → mecanismo_B3_neuroplasticidade e mecanismo_B12_neuroplasticidade_trauma → mecanismo_B12_neurobiologia_trauma em todos os arquivos. Criar mecanismo_B16_neurogenese em _ids_oficiais.json e PARTE_D.",
	  "status": "⏳ PARCIAL — _ids_oficiais.json ✅ e _fluxo_primeira_consulta.json ✅ concluídos (mecanismos, contagem e ids_proibidos sincronizados; bloco_5_mecanismos corrigido — arquivo não constava na lista original de arquivos_pendentes, achado e corrigido em auditoria posterior). Pendente: PARTE_D, 
	  "arquivos_concluidos": ["_ids_oficiais.json", "_fluxo_primeira_consulta.json"],
      "arquivos_pendentes": ["PARTE_D",  "NT_TEMPLATE_v2_0", 
	},
	{
    "id": "IMPL-10",
    "decisao": "P18",
    "acao": "Auditar mecanismo_B1, B2, B3, B4, B6, B9, B14 para confirmar presença dos biomarcadores restaurados (C4/C5/C8/C11) conforme tabela de correlação de P18. Priorizar exame_apoe (correlação tripla: B9+B6+B3).",
    "status": "⏳ PENDENTE",
    "arquivos": ["mecanismo_B1_neuroinflamacao", "mecanismo_B2_eixo_hpa_cortisol", "mecanismo_B3_neuroplasticidade", "mecanismo_B4_deficiencias_monoaminas", "mecanismo_B6_estresse_oxidativo", "mecanismo_B9_disfuncao_mitocondrial", "mecanismo_B14_neuroesteroides_hormonios"]
  },
  {
    "id": "IMPL-11",
    "decisao": "P5 (achado novo nesta auditoria)",
    "acao": "P5.mecanismos_centrais_referencia ainda lista o ID descontinuado 'mecanismo_B3_bdnf_neurogenese'. Atualizar para 'mecanismo_B3_neuroplasticidade'.",
    "status": "⏳ PENDENTE — NÃO HAVIA SIDO DETECTADO ATÉ AGORA",
    "arquivos": ["DECISOES_ARQUITETURAIS_v2_5.json — campo P5.mecanismos_centrais_referencia"]
  },
  {
    "id": "IMPL-12",
    "decisao": "P9 / P15 / P16 — consistência interna do documento de decisões",
    "acao": "Aplicar as atualizações de status já redigidas mas ainda não confirmadas como aplicadas: P9.status → anotar 'superado por P17'; P15.nota_nomenclatura → 'SUPERADO POR P17 ✅'; P16.status_dependente → 'RESOLVIDO POR P17 ✅'.",
    "status": "⏳ PENDENTE — texto já redigido em resposta anterior, falta confirmação de aplicação no documento real",
    "arquivos": ["DECISOES_ARQUITETURAIS_v2_5.json"]
  },
  {
    "id": "IMPL-13",
    "decisao": "Correção de escopo — _ids_oficiais.json",
    "acao": "Remover o bloco 'p18_correlacao_biomarcadores' de dentro de notas_seguranca em _ids_oficiais.json. Conteúdo deve existir apenas em P18 (DECISOES_ARQUITETURAIS_v2_5.json), por violar o princípio anti-duplicação de P16 (correlação inter-categoria não é metadado de existência de ID).",
    "status": "⏳ PENDENTE — recomendação dada, remoção ainda não confirmada como aplicada",
    "arquivos": ["_ids_oficiais.json — bloco notas_seguranca"]
  },	
    ],
  {
        "id": "IMPL-14",
        "decisao": "P18",
        "acao": "Adicionar nota de escopo ortogonal para Bibliotecas de Conhecimento dentro de P11.escopo_precedencia",
        "status": "⏳ PENDENTE",
        "arquivos": ["DECISOES_ARQUITETURAIS_v2_5.json — campo P11.escopo_precedencia"]
      },
      {
        "id": "IMPL-15",
        "decisao": "P18",
        "acao": "Avaliar necessidade de regra formal em _regras_globais.json (ex: R09) operacionalizando checagem de que conteúdo científico deriva de Biblioteca de Conhecimento",
        "status": "⏳ PENDENTE DE DECISÃO",
        "arquivos": ["_regras_globais.json"]
      },
      {
        "id": "IMPL-16",
        "decisao": "P18",
        "acao": "Auditar artefatos derivados já existentes em busca de divergências científicas com a Biblioteca de Conhecimento correspondente, aplicando regra_precedencia_conflito onde encontradas",
        "status": "⏳ PENDENTE",
        "arquivos": ["mecanismo_B1_neuroinflamacao", "JSON_D correlatos"]
      },
      {
        "id": "IMPL-17",
        "decisao": "P20",
        "acao": "Formalizar P20 em DECISOES_ARQUITETURAIS_v2_5.json",
        "status": "⏳ PENDENTE",
        "arquivos": ["DECISOES_ARQUITETURAIS_v2_5.json"]
      },
      {
        "id": "IMPL-18",
        "decisao": "P20",
        "acao": "Aplicar retroativamente em B1 — remover valores de corte e protocolos de coleta do BLOCO_05, substituir por referência de ID + papel biológico resumido",
        "status": "⏳ PENDENTE",
        "arquivos": ["mecanismo_B1_neuroinflamacao — BLOCO_05"]
      }
	   {
	  "id": "IMPL-19",
	  "decisao": "P19",
	  "acao": "Corrigir referência cruzada em _ids_oficiais.json — campo nota_mecanismos_b3_b12_b16 cita 'P18 para correlação obrigatória', deve citar 'P19'",
	  "status": "⏳ PENDENTE",
	  "arquivos": ["_ids_oficiais.json — campo mecanismos.nota_mecanismos_b3_b12_b16"]
	}
	],
	
    "total_implementacoes_pendentes": 18,
	
	"arquivos": ["_ids_oficiais.json — campo mecanismos.nota_mecanismos_b3_b12_b16"]
	},
	{
	  "id": "IMPL-20",
	  "decisao": "P21 (achado em auditoria de coesão contra FASE_2-_01_PROMPT_4_0)",
	  "acao": "Formalizar P21 (definição do GPM como ferramenta preparatória do pipeline, não fonte canônica) e incluir GPM na nota_desenvolvimento de _ids_oficiais.json, _interacoes_cruzadas_globais.json e _fluxo_primeira_consulta.json.",
	  "status": "✅ CONCLUÍDO",
	  "arquivos": ["DECISOES_ARQUITETURAIS_v2_5.json — P21", "_ids_oficiais.json", "_interacoes_cruzadas_globais.json", "_fluxo_primeira_consulta.json"]
	},
	{
	  "id": "IMPL-21",
	  "decisao": "R12 (achado em auditoria de coesão contra FASE_2-_01_PROMPT_4_0)",
	  "acao": "Adicionar limites_contexto.max_mecanismos_por_sessao_geracao = 1 e nota_max_mecanismos_geracao em R12, espelhando max_suplementos_por_sessao para a geração de Bibliotecas de mecanismo.",
	  "status": "✅ CONCLUÍDO",
	  "arquivos": ["_regras_globais.json — R12"]
	},
	{
	  "id": "IMPL-22",
	  "decisao": "R06 (achado em auditoria de coesão contra FASE_2-_01_PROMPT_4_0)",
	  "acao": "Adicionar corte_literatura a campos_obrigatorios_todo_json em R06, generalizando o campo já exigido em FASE_2-_01_PROMPT_4_0 para todo módulo do sistema.",
	  "status": "✅ CONCLUÍDO",
	  "arquivos": ["_regras_globais.json — R06"]
	},
	{
	  "id": "IMPL-23",
	  "decisao": "R04 (achado em auditoria de coesão contra FASE_2-_01_PROMPT_4_0)",
	  "acao": "Adicionar sinalizador_extrapolacao_por_analogia em R04, generalizando o sinalizador [EXTRAPOLAÇÃO POR ANALOGIA] já em uso em FASE_2-_01_PROMPT_4_0 para todo módulo do sistema.",
	  "status": "✅ CONCLUÍDO",
	  "arquivos": ["_regras_globais.json — R04"]
	},
	{
	  "id": "IMPL-24",
	  "decisao": "R06 (achado em auditoria de coesão contra FASE_2-_01_PROMPT_4_0)",
	  "acao": "Adicionar regra_historico_correcoes e regra_verificacao_abrangencia_upstream em R06, generalizando o 'Histórico de correções' (BLOCO_00) e a verificação de abrangência contra GPM (BLOCOs 2.6/4.4) já em uso em FASE_2-_01_PROMPT_4_0.",
	  "status": "✅ CONCLUÍDO",
	  "arquivos": ["_regras_globais.json — R06"]
	}
	],

    "nota_contagem": "O contador abaixo foi corrigido nesta auditoria: o array 'correcoes' já continha 19 itens (IMPL-01 a IMPL-19) antes desta revisão, não 18 como o campo indicava. Contagem atual reflete IMPL-01 a IMPL-24 (19 + 5 novos itens desta auditoria, todos já concluídos).",
    "total_implementacoes_pendentes": 24,
	
    "decisoes_implementadas_via_regras_operacionais": [
     "P3", "P6", "P7", "P8", "P10", "P11", "P13", "P_EVID_01", "P_EVID_02"
]
  }
}


---


3 # REGRAS GLOBAIS          (AUDITADO PELO CHATGPT, ARENA E DEEPSEEK  14/06/2026  19:15H)

{
"id": "_regras_globais",
"tipo": "infraestrutura_global",
"subtipo": "regras_operacionais",
"versao": "2.5",
"pipeline_versao_geracao": "2.6",
"titulo": "Regras Globais do Sistema",
"descricao": "Consolidação das regras operacionais que governam todo o sistema. Documento consultado em qualquer dúvida sobre comportamento padrão. Subordinado apenas a DECISOES_ARQUITETURAIS_v2_5.json.",
"subordinado_a": ["DECISOES_ARQUITETURAIS_v2_5.json"],
"complementar_a": [
"_fluxo_primeira_consulta.json",
"_interacoes_cruzadas_globais.json",
"_ids_oficiais.json"
],
"natureza_sistema": {
"tipo": "suporte_decisao_clinica",
"nao_substitui_julgamento_profissional": true,
"nao_realiza_diagnostico": true,
"decisao_final_profissional": true
},

"R01_risco_vital": {
"descricao": "Regra absoluta de risco vital — prevalece sobre qualquer outra regra do sistema",
"precedencia": "absolute_system_interrupt — esta regra prevalece sobre qualquer outra, incluindo P11. Nenhuma regra, decisão arquitetural ou pipeline pode sobrepujar R01.",
"regra": "Qualquer sinal de risco vital identificado em qualquer momento → interromper tudo → acionar recursos de crise",
"gatilhos": [
"PHQ-9 item 9 > 0",
"C-SSRS positivo em qualquer item",
"Relato verbal de ideação suicida",
"Comportamento de risco vital observado"
],
"recursos_obrigatorios": {
"CVV": "188 — gratuito — 24h",
"SAMU": "192",
"CAPS": "encaminhar imediatamente",
"UPA": "encaminhar imediatamente"
},
"consequencia": "Nenhum protocolo de suplementação, nenhuma escala adicional, nenhum exame é processado até risco vital resolvido",
"excecao": "Nenhuma"
},

"R02_perfil_profissional": {
"descricao": "Regras de escopo por perfil — determinam o que o sistema pode oferecer",
"base_legal": "CFP Resolução 09/2018",
"perfis": [
{
"perfil": "naturopata",
"pode": [
"Aplicar PHQ-9, GAD-7, DASS-21, ISI, PSS",
"Aplicar MBI (uso educacional — declarar ao paciente)",
"Aplicar PCL-5 (encaminhar obrigatoriamente se >= 33)",
"Aplicar C-SSRS (rastreio itens 1-2 — encaminhar se positivo)",
"Solicitar exames C2, C3, C4, C5, C6, C7, C8, C9, C10, C11",
"Prescrever suplementos D1-D5 exceto DHEA",
"Recomendar intervenções D6"
],
"nao_pode": [
"Aplicar HAM-D → alternativa: PHQ-9",
"Aplicar HAM-A → alternativa: GAD-7",
"Aplicar Y-BOCS → encaminhar especialista",
"Aplicar PDSS → encaminhar especialista",
"Prescrever DHEA → médico ou médico ortomolecular",
"Realizar diagnóstico psiquiátrico"
]
},
{
"perfil": "medico_ortomolecular",
"herda_de": "naturopata",
"nota_heranca": "Inclui todo o escopo do naturopata. Consultar bloco naturopata para lista completa de permissões e restrições.",
"adiciona": [
"Aplicar HAM-D e HAM-A",
"Aplicar Y-BOCS e PDSS (dentro do CRM)",
"Prescrever DHEA (requer exame_dhea_s)",
"Prescrever medicamentos dentro do CRM"
],
"nao_pode": [
"Realizar diagnóstico psiquiátrico sem CRM ativo",
"Prescrever além do escopo do CRM"
]
},
{
"perfil": "medico",
"herda_de": "medico_ortomolecular",
"nota_heranca": "Inclui todo o escopo do médico ortomolecular. Consultar blocos naturopata e medico_ortomolecular para lista completa.",
"adiciona": [
"Aplicar C-SSRS protocolo completo",
"Solicitar todos os exames C2 a C11"
],
"nao_pode": []
},
{
"perfil": "psiquiatra",
"herda_de": "medico",
"nota_heranca": "Inclui todo o escopo do médico. Consultar blocos anteriores para lista completa.",
"adiciona": [
"Realizar diagnóstico psiquiátrico",
"Prescrever medicamentos psiquiátricos"
]
},
{
"perfil": "psicologo",
"pode": [
"Aplicar todas as escalas incluindo HAM-D, HAM-A, C-SSRS completo",
"Realizar diagnóstico psicológico"
],
"nao_pode": [
"Prescrever suplementos → encaminhar naturopata ou médico habilitado"
]
},
{
"perfil": "nutricionista",
"pode": [
"Aplicar PHQ-9, GAD-7, DASS-21, ISI, PSS (rastreio — encaminhar se positivo)",
"Indicar suplementos dentro do escopo CRN conforme regulamentação vigente"
],
"nao_pode": [
"Prescrever DHEA → médico ou médico ortomolecular",
"Realizar diagnóstico psiquiátrico ou psicológico",
"Aplicar HAM-D, HAM-A, Y-BOCS, PDSS"
],
"nota": "Escopo nutricional funcional — verificar regulamentação CRN vigente por estado",
"base_legal_especifica": "CRN/CFN — regulamentação do exercício profissional de nutrição"
},
{
"perfil": "enfermeiro_treinado",
"pode": [
"Aplicar PHQ-9, GAD-7, DASS-21, ISI, PSS (rastreio — encaminhar se positivo)",
"Aplicar MBI (rastreio ocupacional — declarar uso como triagem ao paciente)",
"Aplicar C-SSRS (aplicação COMPLETA em contexto de triagem e emergência — encaminhar imediatamente se positivo)",
"Aplicar PCL-5 (rastreio — encaminhar obrigatoriamente se pontuação >= 33)"
],
"nao_pode": [
"Prescrever suplementos ou medicamentos",
"Realizar diagnóstico",
"Aplicar HAM-D → alternativa: PHQ-9",
"Aplicar HAM-A → alternativa: GAD-7",
"Aplicar Y-BOCS → encaminhar especialista",
"Aplicar PDSS → encaminhar especialista"
],
"base_legal": [
"COFEN Resolução 564/2017 — Art. 35: avaliação e mensuração de riscos à saúde",
"Lei 7.498/1986 — regulamentação do exercício de enfermagem",
"CFP Resolução 09/2018 — rastreio de risco vital NÃO configura teste psicológico restrito"
],
"base_evidencia": {
"grade": "B",
"referencias": [
{
"autor": "Posner K et al.",
"ano": 2011,
"revista": "Psychiatry",
"volume": "68(12)",
"paginas": "1066-1077",
"resultado": "C-SSRS desenvolvida para uso por qualquer profissional de saúde treinado"
},
{
"autor": "Mundt JC et al.",
"ano": 2013,
"revista": "Depression and Anxiety",
"volume": "30(8)",
"paginas": "777-783",
"n": 284,
"resultado": "Validação multi-profissional incluindo enfermeiros de triagem"
}
]
},
"diferenca_naturopata": {
"naturopata": "C-SSRS — rastreio itens 1-2 (ideação passiva) apenas",
"enfermeiro": "C-SSRS — aplicação COMPLETA em contexto de triagem e emergência"
},
"nota": "Qualquer resultado positivo: encaminhar imediatamente ao profissional responsável. Escopo baseado em DECISOES_ARQUITETURAIS_v2_5.json P14."
},
{
"perfil": "outro",
"instrucao": "Encaminhar para profissional habilitado. Usar somente escalas abertas sem restrição."
}
]
},

"R03_entrada_suplementos": {
"descricao": "Regras que determinam quando e como um suplemento entra no protocolo",
"TIPO_1": {
"nome": "Intervenção por doença",
"alerta_visual": "✅ TIPO_1 — Intervenção por doença",
"regra": "Entra por diagnóstico ou quadro clínico. Independe de exame laboratorial.",
"exame_necessario": false,
"regra_complementar": "Exame normal NÃO exclui suplemento TIPO_1.",
"exemplo": "omega3_epa_dha para depressão — entra por diagnóstico. Exame omega3_index normal NÃO exclui."
},
"TIPO_2": {
"nome": "Correção de déficit",
"alerta_visual": "⚠️ TIPO_2 — Corrigível por exame",
"regra": "Entra APENAS se exame laboratorial identifica déficit.",
"exame_necessario": true,
"regra_negativa": "Exame normal = NÃO incluir. Sem exceção.",
"exemplo": "vitd3_k2 — VitD < 30 ng/mL → corrigir | VitD > 50 ng/mL → sem ação"
},
"DUAL": {
"nome": "TIPO_1 primário + TIPO_2 secundário",
"regra": "tipo_primario determina critério de ENTRADA. tipo_secundario reforça indicação mas não é bloqueante.",
"declaracao_obrigatoria": "tipo_primario + tipo_secundario em todo suplemento DUAL",
"fonte_ids_dual": "_ids_oficiais.json → ids_duais",
"nota_ferro": "ferro_bisglicinato = TIPO_2 puro. Entrada depende exclusivamente de déficit laboratorial confirmado. NÃO consta na lista DUAL.",
"exemplo": "omega3_epa_dha: tipo_primario=TIPO_1 (entra por depressão). tipo_secundario=TIPO_2 (déficit no omega3_index reforça e orienta dose — mas exame normal NÃO exclui)"
},
"regras_gerais": [
"Todo suplemento deve declarar tipo_primario",
"GRADE ausente = suplemento não entra no protocolo",
"EA ausente = output incompleto",
"IDs removidos definitivamente nunca entram: coq10_ubiquinol | pqq | resveratrol | espermidina | acido_alfa_lipoico"
]
},

"R04_evidencia_grade": {
"descricao": "Regras de qualidade de evidência — determinam o que pode ser recomendado",
"pergunta_decisora": "O que a ciência e a literatura publicada dizem?",
"fonte_de_verdade": "GRADE Working Group (Guyatt et al. 2011) + CONSORT 2010 + COCHRANE HANDBOOK v6.3 + PRISMA 2020",
"grade_minimo_recomendacao": "GRADE B",
"grade_minimo_interacao_critica": "GRADE B (ou REGRA_5 aplicada)",
"grades": [
{
"grade": "A",
"descricao": "Meta-análise de RCTs bem conduzidos",
"criterios": ["I² < 50%", "IC95% estreito", "Replicação independente", "Ausência viés publicação"],
"n_preferencial": "n > 300 total",
"n_minimo_excecional": "n > 150 SE: SMD > 1.0 + IC95% estreito + I² < 40% + 3+ RCTs independentes",
"nota_n_menor_300": "Declarar: 'GRADE A com ressalva de n total = X. Replicação adicional fortaleceria a evidência.'",
"uso": "Base de recomendação forte"
},
{
"grade": "B",
"descricao": "RCT duplo-cego n > 50 por braço ou meta-análise com limitações",
"criterios": ["IC95%", "p-valor", "CONSORT 2010"],
"elevacao_regra_5": "Mecanismo farmacocinético estabelecido em humanos com >= 2 fontes independentes → eleva para GRADE B para fins de severidade de interação",
"uso": "Base de recomendação. Declarar limitações."
},
{
"grade": "C",
"descricao": "RCT único sem replicação ou observacional",
"uso": "APENAS com declaração explícita: 'GRADE C — evidência limitada'. NUNCA como base única de recomendação forte."
},
{
"grade": "D",
"descricao": "Piloto n < 30, in vitro, animal, opinião de especialista isolada",
"uso": "EXCLUSIVAMENTE para contextualização mecanística. Declarar: 'GRADE D — contextual apenas. Sem base para recomendação.'",
"proibido": "Extrapolar para recomendação ou interação em qualquer circunstância."
}
],
"campos_obrigatorios_rct": [
"n por braço", "IC95%", "p-valor", "SMD ou OR ou RR ou WMD", "GRADE declarado"
],
"campos_obrigatorios_meta": [
"n total", "número de RCTs", "I²", "IC95% pooled", "GRADE declarado"
],
"campos_obrigatorios_nnt": [
"valor NNT", "IC95% do NNT", "população", "comparador",
"desfecho", "duração", "GRADE base"
],
"rating_minimo": "⭐⭐⭐⭐ ou ⭐⭐⭐⭐⭐ — ⭐⭐⭐ ou inferior = reprovar",
"nota_rating": "Sistema de estrelas é filtro de entrada. Não substitui GRADE. Ver pipeline para critérios de aplicação.",
"regras_absolutas": [
"Sem evidência humana direta → não entra",
"Só in vitro ou animal → não entra como recomendação",
"Dúvida sobre qualidade → não entra. Entra como observação.",
"Alternativa mais robusta disponível → usar a alternativa",
"Extrapolação sem evidência direta → não é evidência",
"Campo vazio preferível a dado inventado"
],
"excecao_regra_5": {
"condicao": "Mecanismo farmacocinético estabelecido em humanos com >= 2 fontes independentes publicadas",
"efeito": "Eleva efetivamente ao GRADE B para fins de severidade de interação",
"escopo": "EXCLUSIVAMENTE para classificação de severidade de interações. NUNCA para eficácia de suplementos. NÃO altera GRADE de evidência de desfecho clínico.",
"exemplo": "int_001: erva_sao_joao + 5htp → síndrome serotoninérgica. Steele 2015 PMID:25815753"
}
},
"exemplo": "int_001: erva_sao_joao + 5htp → síndrome serotoninérgica. Steele 2015 PMID:25815753"
},
"sinalizador_extrapolacao_por_analogia": {
"descricao": "Sinalizador obrigatório aplicável a qualquer módulo do sistema (mecanismos, suplementos, biomarcadores, intervenções, nutrição, exercício, psicoterapia) cujo conteúdo derive de evidência científica.",
"quando_aplicar": "Quando um achado científico foi estabelecido em um contexto diferente do contexto de aplicação deste módulo — outra condição clínica (ex.: mecanismo validado em Alzheimer, estendido a depressão), outra população (ex.: suplemento validado só em idosos, estendido a adultos jovens), ou outro desfecho (ex.: eficácia demonstrada para sintoma A, estendida a sintoma B por mecanismo comum) — sem validação direta equivalente no contexto de aplicação real.",
"formato": "(Autor, Ano)[tipo] [EXTRAPOLAÇÃO POR ANALOGIA: contexto original do estudo-fonte — validação direta no contexto de aplicação pendente]",
"diferenca_de_controverso": "Não indica debate científico sobre o achado em si — indica que a extensão específica do achado a este novo contexto ainda não foi testada diretamente. Mais preciso que um sinalizador genérico de controvérsia.",
"excecao": "Não aplicar a biologia básica sem contexto de doença/população (ex.: diferenciação celular in vitro, bioquímica geral) — isso é fundamento mecanístico direto, não extrapolação.",
"origem": "Generaliza para todo o sistema o sinalizador homônimo já em uso em FASE_2-_01_PROMPT_4_0 (Bibliotecas de Mecanismo B1-B16) — ver IMPL-23."
}
},

"R05_seguranca_clinica": {
"descricao": "Regras de segurança — executam ANTES de qualquer protocolo",
"ordem_execucao": "R01 (risco vital) → restricoes_legais_por_perfil → contraindicacoes_absolutas → interacoes_criticas → eficacia → output",
"fonte_canonica_ordem": "P13_ordem_execucao_seguranca — DECISOES_ARQUITETURAIS_v2_5.json",
"vinculo_evidencia": "Todas as interações críticas listadas foram classificadas conforme R04.",
"referencia_completa_interacoes": "_interacoes_cruzadas_globais.json",
"interacoes_criticas": {
"descricao": "BLOQUEIO SEM OVERRIDE",
"resumo": [
{"id": "int_001", "par": "erva_sao_joao + 5htp", "risco": "Síndrome serotoninérgica", "acao": "NUNCA"},
{"id": "int_002", "par": "erva_sao_joao + SSRI ou SNRI", "risco": "Síndrome serotoninérgica", "acao": "NUNCA"},
{"id": "int_003", "par": "SAMe + IMAO", "risco": "Crise hipertensiva", "acao": "NUNCA"},
{"id": "int_004", "par": "SAMe + bipolar sem estabilizador", "risco": "Indução de mania", "acao": "NUNCA"},
{"id": "int_005a", "par": "5htp > 100mg/dia + SSRI", "severidade": "critica", "acao": "BLOQUEAR — sem override"},
{"id": "int_006", "par": "kava_kava + hepatopatia ou álcool", "risco": "Hepatotoxicidade", "acao": "NUNCA"},
{"id": "int_007", "par": "rhodiola_rosea + lítio", "risco": "Toxicidade por lítio", "acao": "NUNCA"}
]
},
"interacoes_altas": [
{"id": "int_005b", "par": "5htp <= 100mg/dia + SSRI", "severidade": "alta", "acao": "ALERTAR — override com documentação médica"}
],
"interacoes_moderadas": [
{"id": "int_009", "par": "omega3_epa_dha + kava_kava", "severidade": "observacao_protocolo", "acao": "Informar — não bloquear em dose padrão"},
{"id": "int_008", "tripla": ["ashwagandha", "rhodiola_rosea", "passiflora"], "severidade": "moderada", "acao": "Máx 2 dos 3"}
],
"contraindicacoes_absolutas": [
"kava_kava: hepatopatia ou uso de álcool",
"SAMe: transtorno bipolar sem estabilizador",
"SAMe: em uso de IMAO",
"erva_sao_joao: em uso de SSRI, SNRI ou IMAO",
"5htp > 100mg/dia em uso de SSRI (alta dose definida como >100mg/dia → BLOQUEAR)",
"rhodiola_rosea: em uso de lítio",
"DHEA: sem prescrição médica"
]
},

"R06_output_obrigatorio": {
"descricao": "O que todo output clínico deve conter — output incompleto = reprovar",
"campos_obrigatorios_todo_suplemento": [
"id canônico",
"tipo_primario (TIPO_1 | TIPO_2 | DUAL)",
"GRADE declarado",
"IC95% + tamanho do efeito + p-valor",
"NNT com contexto completo (se disponível)",
"ea_esperados (eventos adversos)",
"contraindicacoes",
"dose e posologia",
"tempo de resposta esperado"
],
"campos_obrigatorios_todo_json": [
"natureza_sistema (4 campos P12)",
"semantic_layer (6 campos)",
"versao: '2.5'",
"pipeline_versao_geracao: '2.6' — obrigatório em arquivos NOVOS. Arquivos gerados antes da v2.6 não possuem este campo — não retroativo.",
"corte_literatura — data ou período até o qual o levantamento de literatura usado para gerar o conteúdo é considerado válido; declarar se reflete data de corte de treinamento do modelo gerador ou data de busca ativa com ferramenta externa. Aplicável a todo módulo cujo conteúdo derive de levantamento científico (mecanismos, biomarcadores, suplementos, intervenções, nutrição, exercício, psicoterapia). Obrigatório em arquivos NOVOS, mesma regra de não-retroatividade de pipeline_versao_geracao. Ver IMPL-22."
],
"natureza_sistema_obrigatorio": {
"tipo": "suporte_decisao_clinica",
"nao_substitui_julgamento_profissional": true,
"nao_realiza_diagnostico": true,
"decisao_final_profissional": true
},
"semantic_layer_obrigatorio": {
"clinical_summary": "exatamente 3 frases: o que é | para que serve | quando usar",
"rag_context_hint": "iniciar com 'Recuperar quando:' — máx 50 palavras",
"clinical_domains": "máx 4 dos domínios oficiais",
"semantic_keywords": "8 a 12 termos",
"related_entities": "IDs exatos — máx 12",
"embedding_priority": "alta | media | baixa"
},
"regra_ea": "EA ausente = output incompleto. Campo vazio preferível a dado inventado.",
"regra_grade": "GRADE ausente em qualquer evidência = reprovar",
"regra_limitacoes": "Limitações declaradas sempre — nunca omitir",
"cross_field_consistency": "obrigatorio — verificar: (a) TIPO_2 requer exame confirmatório; (b) DUAL requer tipo_primario + tipo_secundario; (c) dose compatível com via e faixa etária."
"cross_field_consistency": "obrigatorio — verificar: (a) TIPO_2 requer exame confirmatório; (b) DUAL requer tipo_primario + tipo_secundario; (c) dose compatível com via e faixa etária.",
"regra_historico_correcoes": {
"descricao": "Todo módulo do sistema deve registrar, em campo estruturado histórico_correcoes, qualquer correção factual aplicada a uma versão anterior do conteúdo.",
"formato": "data | campo afetado | erro anterior | correção aplicada | ação downstream necessária",
"regra": "Conteúdo gerado a partir de uma versão com erro conhecido deve ser marcado para reprocessamento.",
"origem": "Formaliza como campo estruturado obrigatório o princípio de changelog já registrado em P3 e já operacionalizado como 'Histórico de correções' em FASE_2-_01_PROMPT_4_0 (BLOCO_00). Ver IMPL-24."
},
"regra_verificacao_abrangencia_upstream": {
"descricao": "Todo módulo cujo conteúdo derive de um documento de levantamento preparatório externo (ex.: GPM para mecanismos — ver P21 — ou ferramenta equivalente de outros domínios) deve incluir, na etapa de geração, verificação explícita de que cada categoria de conteúdo mapeada no documento upstream foi incorporada ao conteúdo final ou declarada 'N/A — [motivo]'.",
"regra": "Nenhuma categoria do documento upstream deve desaparecer silenciosamente do artefato final.",
"origem": "Generaliza o padrão já em uso nas verificações de abrangência de FASE_2-_01_PROMPT_4_0 (BLOCOs 2.6 e 4.4). Ver IMPL-24."
}
},

"R07_ids": {
"descricao": "Regras sobre identificadores — IDs são contratos do sistema",
"regra_principal": "ID não listado no catálogo canônico = não existe. Não gerar, não referenciar.",
"formato": "snake_case puro — sem acentos, sem espaços, sem maiúsculas, sem hífens",
"ids_removidos_definitivo": [
"coq10_ubiquinol", "pqq", "resveratrol", "espermidina", "acido_alfa_lipoico"
],
"ids_proibidos_usar_alternativa": [
{"proibido": "exame_hamd", "usar": "exame_ham_d"},
{"proibido": "exame_hama", "usar": "exame_ham_a"},
{"proibido": "exame_magnesio", "usar": "exame_magnesio_eritrocitario"},
{"proibido": "exame_cortisol_manha", "usar": "exame_cortisol_matinal"},
{"proibido": "kava", "usar": "kava_kava"},
{"proibido": "rhodiola", "usar": "rhodiola_rosea"},
{"proibido": "gaba", "usar": "gaba_lipossomal"},
{"proibido": "acafrao", "usar": "acafrao_crocus"},
{"proibido": "bacopa", "usar": "bacopa_monnieri"},
{"proibido": "zinco", "usar": "zinco_bisglicinato"},
{"proibido": "omega3", "usar": "omega3_epa_dha"},
{"proibido": "alcar_carnitina", "usar": "alcar"},
{"proibido": "vitamina_c_ascorbato", "usar": "vitamina_c"},
{"proibido": "vitamina_b12_5mthf", "usar": "b12_metilfolato_combo"},
{"proibido": "omega3__epa_dha", "usar": "omega3_epa_dha", "nota": "underscore duplo — ID inválido histórico"},
{"proibido": "mecanismo_B3_bdnf_neurogênese", "usar": "mecanismo_B3_bdnf_neurogenese"}
],
"regra_novo_id": "Novo ID criado → atualizar _ids_oficiais.json na mesma sessão. Proibido adiar para sessão futura.",
"decisoes_arquiteturais_ids": [
"P1: Slot_6 encerrado — 5 IDs removidos definitivamente",
"P2: exame_dexametasona = C-LAB. Não C-FUNC.",
"P9: mecanismo_B3_bdnf_neurogenese — sem acento"
]
},

"R08_conflito_hierarquia": {
"descricao": "Regras de resolução de conflito entre documentos do sistema",
"autoridade_ref": "P11 — DECISOES_ARQUITETURAIS_v2_5.json",
"hierarquia_p11": [
"1. DECISOES_ARQUITETURAIS_v2_5.json — decisões explícitas prevalecem sobre tudo",
"2. _ids_oficiais.json — catálogo canônico de IDs",
"3. PARTE_D (arvore_repositorio) — fonte de verdade de estrutura de pastas, organização e contagens.",
"4. KITs (KIT_MECANISMO, KIT_SUPLEMENTO, KIT_C_ESC, KIT_C_LAB, KIT_CENARIO) — templates e guia de construção de JSON modular",
"5. PROMPT_GERADOR_* (mecanismos e demais grupos de módulo) — geração de Biblioteca de Conhecimento",
"6. (histórico) Partes A, B, C, E — arquivadas em [28/07/26]. Consultar apenas como changelog/rationale, nunca como fonte ativa."
],
"fontes_verdade": {
"contagens": "PARTE_D",
"ids": "_ids_oficiais",
"decisoes": "DECISOES_ARQUITETURAIS"
},
"fluxo_resolucao": [
"1. Identificar o conflito explicitamente",
"2. Consultar P11 — qual fonte prevalece?",
"3. Se DECISOES_ARQUITETURAIS decide → aplicar",
"4. Se ambíguo → registrar BACKLOG_TECNICO.json status=pendente_resolucao",
"5. NUNCA gerar output com conflito silencioso não resolvido"
],
"rollback": {
"regra": "Após 2 reprovações consecutivas na mesma etapa → voltar ao início",
"reprovacao_definida_como": "falha em R04, R05 ou R06",
"acao": "Revisar narrativa fonte. Se evidência insuficiente: documentar e não prosseguir.",
"proibido": "Continuar gerando JSON com evidência insuficiente"
}
},

"R09_monitoramento": {
"descricao": "Regras de monitoramento e reavaliação de protocolos",
"prerequisito": "R01 executado antes de qualquer reavaliação — independente de protocolo em curso",
"frequencia_padrao": "4-6 semanas para primeira reavaliação",
"obrigacoes_reavaliacao": [
"Reaplicar escalas do baseline",
"Comparar pontuações",
"Verificar exames TIPO_2 — suspender se déficit normalizado",
"Registrar EA observados",
"Verificar novas interações se medicamentos alterados",
"Atualizar protocolo conforme resposta"
],
"criterios_ajuste": [
{
"cenario": "Melhora > 50% em 6 semanas",
"acao": "Manter. Considerar redução gradual em 3-6 meses."
},
{
"cenario": "Melhora < 25% em 8 semanas",
"acao": "Revisar mecanismos. Verificar adesão. Considerar encaminhamento."
},
{
"cenario": "Piora ou novo sintoma",
"acao": "Reavaliar interações. Suspeitar EA. Encaminhar se necessário."
},
{
"cenario": "PHQ-9 item 9 > 0 em qualquer reavaliação",
"acao": "R01 imediatamente — independente de protocolo em curso"
}
],
"regra_tipo_2_normalizacao": "Déficit TIPO_2 normalizado → reavaliar necessidade de continuidade. Exame normal não justifica manutenção de TIPO_2 puro."
},

"R10_encaminhamentos": {
"descricao": "Critérios globais de encaminhamento — não opcionais",
"encaminhamentos_obrigatorios": [
{
"gatilho": "PHQ-9 >= 20",
"destino": "Psiquiatria",
"urgencia": "alta"
},
{
"gatilho": "C-SSRS positivo",
"destino": "Urgência / CAPS",
"urgencia": "imediata"
},
{
"gatilho": "PCL-5 >= 33",
"destino": "Psicologia ou Psiquiatria",
"urgencia": "alta"
},
{
"gatilho": "GAD-7 >= 15",
"destino": "Avaliação psiquiátrica",
"urgencia": "alta"
},
{
"gatilho": "Suspeita de transtorno bipolar",
"destino": "Psiquiatria",
"urgencia": "alta",
"nota": "ANTES de iniciar SAMe ou rhodiola_rosea"
},
{
"gatilho": "Hepatopatia + interesse em kava_kava",
"destino": "Hepatologista",
"urgencia": "programada"
},
{
"gatilho": "Y-BOCS ou PDSS solicitados",
"destino": "Especialista",
"urgencia": "programada"
}
],
"principio": "Protocolo integrativo é adjuvante — nunca substituto de cuidado especializado quando indicado"
},

"R11_versionamento": {
"descricao": "Regras de versionamento — campos independentes e obrigatórios",
"versao": {
"valor_fixo": "2.5",
"significado": "Schema do conteúdo clínico — invariável",
"regra": "Nunca alterar sem aprovação formal de nova versão de schema"
},
"pipeline_versao_geracao": {
"valor_atual": "2.6",
"significado": "Versão da ferramenta de geração usada para criar este arquivo — metadado de rastreabilidade",
"natureza": "METADADO — não implica dependência funcional do programa",
"regra": "Todo arquivo novo gerado declara a versão da ferramenta que o criou. Após gerado, o arquivo funciona independentemente dessa ferramenta.",
"retroatividade": "PROSPECTIVA APENAS — arquivos gerados anteriormente não precisam ser regerados"
},
"nota": "versao e pipeline_versao_geracao são campos INDEPENDENTES. Nunca confundir."
},

"R12_gestao_contexto": {
"descricao": "Regras para manter integridade entre sessões de trabalho",
"verificacao_inicio_sessao": {
"obrigatoria": true,
"checklist": [
"Q1: Qual é a pergunta decisora? → O que a ciência e a literatura dizem?",
"Q2: 6 PROIBIDOS confirmados como PROIBIDO",
"Q3: TIPO_1 vs TIPO_2 — 5 afirmações VERDADEIRO",
"Q4: Documento que prevalece em conflito → DECISOES_ARQUITETURAIS_v2_5.json"
],
"criterio": "Todas corretas → iniciar. Qualquer incorreta → não iniciar geração."
},
"limites_contexto": {
"max_suplementos_por_sessao": 2,
"max_mecanismos_por_sessao_geracao: 1
"max_arquivos_sem_briefing": 5,
"sessao_definida_como": "janela de contexto única de uma IA ou bloco de trabalho delimitado",
"contexto_minimo_recomendado": [
"DECISOES_ARQUITETURAIS_v2_5.json",
"_ids_oficiais.json",
"_regras_globais.json",
"_interacoes_cruzadas_globais.json",
"_fluxo_primeira_consulta.json"
]
},
"nota_max_mecanismos_geracao": "A geração de uma Biblioteca de mecanismo via FASE_2-_01_PROMPT_4_0 já ocorre em múltiplas partes sequenciais dentro de uma mesma sessão (Parte 1 e Parte 2). Combinar a geração de mais de um mecanismo na mesma sessão aumenta risco de contaminação cruzada de nomenclatura, direção de achado ou força de evidência entre mecanismos distintos, além de agravar risco de degradação de instrução-seguimento por volume acumulado de contexto. Ver limites_contexto.max_mecanismos_por_sessao_geracao e IMPL-21.",

"sinal_degradacao": "Sistema contradiz ID gerado anteriormente na mesma sessão ou perde referência a campo já definido",
"acao_degradacao": "Salvar trabalho → reiniciar sessão → recarregar contexto → continuar",
"anti_deriva": "Em sessões longas: verificar filosofia a cada 5 arquivos gerados"
},

"semantic_layer": {
"clinical_summary": "Consolidação das regras operacionais que governam todo o sistema de suporte à decisão clínica em saúde mental integrativa. Define o comportamento padrão em segurança, evidência, IDs, conflitos, output e versionamento. Consultar sempre que houver dúvida sobre como o sistema deve se comportar em qualquer situação.",
"rag_context_hint": "Recuperar quando: dúvida sobre regra operacional do sistema | critério de entrada de suplemento | GRADE mínimo | output obrigatório | resolução de conflito entre documentos | regra de ID | encaminhamento obrigatório | versionamento",
"clinical_domains": [
"seguranca_clinica",
"decisao_terapeutica",
"monitoramento",
"triagem_clinica"
],
"semantic_keywords": [
"regras globais", "TIPO_1 TIPO_2 DUAL", "GRADE evidência",
"interações críticas", "contraindicações absolutas",
"output obrigatório", "hierarquia de conflito",
"IDs canônicos", "CFP 09/2018", "versionamento",
"risco vital", "perfis profissionais"
],
"related_entities": [
"_fluxo_primeira_consulta.json",
"_interacoes_cruzadas_globais.json",
"_ids_oficiais.json",
"DECISOES_ARQUITETURAIS_v2_5.json",
"algoritmo_resultado_protocolo",
"exame_phq9",
"exame_cssrs",
"omega3_epa_dha",
"vitd3_k2",
"erva_sao_joao",
"kava_kava",
"same"
],
"embedding_priority": "alta"
}
}


4 # interacoes_cruzadas_globais.json — Completo e Corrigido         (AUDITADO PELO CHATGPT, ARENA E DEEPSEEK  14/06/2026 22:50H)



{
  "id": "_interacoes_cruzadas_globais",
  "tipo": "infraestrutura_global",
  "subtipo": "catalogo_interacoes",
  "versao": "2.5",
  "pipeline_versao_geracao": "2.6",
  "titulo": "Interações Cruzadas Globais",
  "descricao": "Catálogo autoritativo de interações entre suplementos, fitoterápicos e medicamentos. Consultado em tempo real durante geração de qualquer protocolo. Bloqueia ou alerta antes de qualquer combinação entrar no output clínico.",
  "subordinado_a": [
    "DECISOES_ARQUITETURAIS_v2_5.json",
    "_ids_oficiais.json",
    "_regras_globais.json"
  ],
  "nota_subordinacao": "Subordinação refere-se à hierarquia de governança arquitetural — não de conteúdo clínico. Para dados de interações, este catálogo é fonte canônica conforme declarado em _regras_globais.json R05.",
  "referenciado_por": [
    "_fluxo_primeira_consulta.json → bloco_6",
    "_regras_globais.json → R05"
  ],
  "natureza_sistema": {
    "tipo": "suporte_decisao_clinica",
    "nao_substitui_julgamento_profissional": true,
    "nao_realiza_diagnostico": true,
    "decisao_final_profissional": true
  },
  "versionamento": {
    "versao": "2.5",
    "pipeline_versao_geracao": "2.6",
    "nota": "versao = schema do conteudo clinico (invariavel). pipeline_versao_geracao = metadado de rastreabilidade da ferramenta que gerou este arquivo. Sao independentes."
  },

  "metarregras": {
    "regra_consulta": "Consultar ANTES de qualquer suplemento entrar no protocolo",
    "regra_medicamentos": "Todo medicamento em uso → cruzar com este catálogo antes de prosseguir",
    "regra_bloqueio": "Severidade=critica → BLOQUEAR sem override. Sem exceção.",
    "regra_override": "Severidade=alta → override permitido APENAS com documentação explícita do profissional",
    "regra_incompleto": "Dúvida sobre interação não catalogada → tratar como alta até esclarecimento",
    "regra_atualizacao": "Nova interação identificada com evidência GRADE B ou superior → registrar aqui na mesma sessão",
    "regra_dose": "Interações dose-dependentes → especificar faixa de risco. Dose padrão do protocolo prevalece.",
    "fonte_evidencia_critica": "REGRA_5 — mecanismo farmacocinético estabelecido em humanos com >= 2 fontes independentes publicadas eleva para GRADE B para fins de severidade crítica"
  },

  "tabela_severidade": {
    "critica": {
      "definicao": "Risco de vida ou dano grave irreversível",
      "grade_minimo": "GRADE B (ou REGRA_5 aplicada)",
      "acao": "BLOQUEAR — sem override",
      "documentacao": "Não requer documentação — combinação simplesmente não ocorre",
      "cor_referencia": "VERMELHO",
      "excecao_dose_dependente": "ver int_005a e int_005b"
    },
    "alta": {
      "definicao": "Risco significativo — dano reversível grave",
      "grade_minimo": "GRADE C",
      "acao": "Alertar — override permitido com documentação explícita",
      "documentacao": "Obrigatória — profissional deve registrar ciência do risco",
      "cor_referencia": "LARANJA"
    },
    "moderada": {
      "definicao": "Risco presente — manejo possível com ajuste de protocolo",
      "grade_minimo": "GRADE C ou D",
      "acao": "Alertar — informativo — ajustar protocolo",
      "documentacao": "Recomendada",
      "cor_referencia": "AMARELO"
    },
    "baixa": {
      "definicao": "Risco teórico ou mínimo",
      "grade_minimo": "Qualquer",
      "acao": "Informar",
      "documentacao": "Opcional",
      "cor_referencia": "VERDE",
      "status": "categoria_prevista_sem_entradas_v2_5"
    },
    "observacao_protocolo": {
      "definicao": "Combinação segura na dose padrão do protocolo — risco apenas fora da faixa terapêutica",
      "evidencia_direta_combinacao": false,
      "grade_combinacao": "D",
      "acao": "Informar profissional — não bloquear em dose padrão",
      "documentacao": "Registrar dose utilizada",
      "cor_referencia": "AZUL"
    }
  },

  "interacoes_criticas": {
    "descricao": "BLOQUEIO SEM OVERRIDE — risco de vida confirmado",
    "nota_evidencia": "Todas as interações críticas fundamentadas em mecanismo farmacocinético estabelecido em humanos (REGRA_5) com >= 2 fontes independentes publicadas — equivalente GRADE B para fins de severidade",
    "entradas": [
      {
        "id": "int_001",
        "elementos": ["erva_sao_joao", "5htp"],
        "tipo": "par",
        "logica_elementos": "AND — ambos os elementos devem estar presentes para a interação ocorrer",
        "severidade": "critica",
        "mecanismo": "Potencialização serotoninérgica dupla — inibição de recaptação (hipericina) + aumento de substrato (5-HTP) → síndrome serotoninérgica",
        "risco_clinico": "Síndrome serotoninérgica — tremor, hipertermia, confusão, colapso cardiovascular",
        "base_evidencia": {
          "tipo": "mecanismo_farmacologico_humano",
          "regra_5_aplicada": true,
          "grade_efetivo": "B",
          "fontes": [
            {"referencia": "Steele 2015", "pmid": "25815753", "descricao": "Revisão de interações serotoninérgicas — erva de São João"},
            {"referencia": "Borrelli & Izzo 2009", "pmid": "19234396", "descricao": "Interações farmacológicas da Hypericum perforatum"}
          ]
        },
        "acao": "BLOQUEAR — sem override",
        "manejo": "Nunca combinar. Washout >= 2 semanas antes de iniciar qualquer um após o outro.",
        "alternativas": [
          "Se depressão leve-moderada: erva_sao_joao OU acafrao_crocus — não combinar com 5htp",
          "Se déficit serotoninérgico: ltriptofano como alternativa ao 5htp com menor risco"
        ]
      },
      {
        "id": "int_002",
        "elementos": ["erva_sao_joao", "SSRI", "SNRI"],
        "tipo": "suplemento_vs_classe",
        "logica_elementos": "OR — a interação aplica-se quando erva_sao_joao é combinado com SSRI OU com SNRI. Não requer a presença simultânea dos três elementos.",
        "nota_ids": "SSRI e SNRI são classes farmacológicas externas ao catálogo — não possuem ID canônico no sistema",
        "severidade": "critica",
        "mecanismo": "Inibição dupla de recaptação de serotonina — hipericina (erva de São João) + SSRI/SNRI → excesso serotoninérgico central e periférico",
        "risco_clinico": "Síndrome serotoninérgica — potencialmente fatal",
        "base_evidencia": {
          "tipo": "mecanismo_farmacologico_humano",
          "regra_5_aplicada": true,
          "grade_efetivo": "B",
          "fontes": [
            {"referencia": "Dannawi 2002", "pmid": "11865130", "descricao": "Caso clínico — síndrome serotoninérgica com paroxetina + Hypericum"},
            {"referencia": "Izzo 2004", "pmid": "14984367", "descricao": "Revisão sistemática — interações erva de São João com medicamentos"}
          ]
        },
        "acao": "BLOQUEAR — sem override",
        "manejo": "Nunca combinar. Washout >= 2 semanas ao trocar.",
        "alternativas": [
          "Se em uso de SSRI/SNRI: acafrao_crocus como adjuvante fitoterápico mais seguro",
          "Se em uso de SSRI/SNRI: omega3_epa_dha como augmentation GRADE A"
        ]
      },
      {
        "id": "int_003",
        "elementos": ["same", "IMAO"],
        "tipo": "par_medicamento",
        "logica_elementos": "AND — ambos os elementos devem estar presentes para a interação ocorrer",
        "nota_ids": "IMAO é classe farmacológica externa ao catálogo — não possui ID canônico no sistema",
        "severidade": "critica",
        "mecanismo": "SAMe doa grupos metil para síntese de catecolaminas + IMAO bloqueia degradação → acúmulo de noradrenalina e dopamina → crise hipertensiva",
        "risco_clinico": "Crise hipertensiva — risco de AVC hemorrágico",
        "base_evidencia": {
          "tipo": "mecanismo_farmacologico_humano",
          "regra_5_aplicada": true,
          "grade_efetivo": "B",
          "fontes": [
            {"referencia": "Mischoulon & Fava 2002", "pmid": "12420704", "descricao": "SAMe — farmacologia e interações clínicas"},
            {"referencia": "Bottiglieri 2002", "pmid": "12420703", "descricao": "SAMe — metabolismo e segurança clínica"}
          ]
        },
        "acao": "BLOQUEAR — sem override",
        "manejo": "Nunca combinar. Intervalo >= 14 dias após suspensão de IMAO irreversível.",
        "alternativas": [
          "Se depressão sem IMAO: same é GRADE A",
          "Se em uso de IMAO: aguardar washout completo — decisão médica"
        ]
      },
      {
        "id": "int_004",
        "elementos": ["same", "bipolar_sem_estabilizador"],
        "tipo": "condicao_clinica",
        "nota_elementos": "bipolar_sem_estabilizador é uma condição clínica — não é um ID do sistema. Ver _fluxo_primeira_consulta.json → bloco_2B para critérios de suspeita de bipolaridade.",
        "severidade": "critica",
        "mecanismo": "SAMe aumenta síntese de monoaminas — em paciente bipolar sem proteção de estabilizador pode desencadear switch maníaco",
        "risco_clinico": "Episódio maníaco agudo — risco de comportamento impulsivo, auto e heteroagressão",
        "base_evidencia": {
          "tipo": "mecanismo_farmacologico_humano",
          "regra_5_aplicada": true,
          "grade_efetivo": "B",
          "fontes": [
            {"referencia": "Rosenbaum et al. 1990", "pmid": "2122129", "descricao": "SAMe e switch maníaco em pacientes bipolares"},
            {"referencia": "Carney et al. 1989", "pmid": "2571064", "descricao": "SAMe — risco de mania em depressão bipolar"}
          ]
        },
        "acao": "BLOQUEAR — sem override",
        "manejo": "Encaminhar psiquiatria ANTES de qualquer tentativa. Estabilizador confirmado e em nível terapêutico = reavaliação médica.",
        "alternativas": [
          "Se bipolar estabilizado com estabilizador confirmado: decisão médica",
          "Alternativas sem risco de switch: omega3_epa_dha GRADE A | acafrao_crocus GRADE B"
        ]
      },
      {
        "id": "int_005a",
        "elementos": ["5htp", "SSRI"],
        "tipo": "par_medicamento",
        "subtipo": "dose_dependente",
        "logica_elementos": "AND — ambos os elementos devem estar presentes. Condição adicional: dose de 5htp > 100mg/dia",
        "nota_ids": "SSRI é classe farmacológica externa ao catálogo — não possui ID canônico no sistema",
        "severidade": "critica",
        "dose_de_risco": "5htp > 100mg/dia em combinação com SSRI",
        "mecanismo": "5-HTP aumenta síntese de serotonina + SSRI bloqueia recaptação → acúmulo serotoninérgico → síndrome serotoninérgica em dose alta",
        "risco_clinico": "Síndrome serotoninérgica — risco de vida",
        "base_evidencia": {
          "tipo": "mecanismo_farmacologico_humano",
          "regra_5_aplicada": true,
          "grade_efetivo": "B",
          "fontes": [
            {"referencia": "Hinz et al. 2012", "pmid": "22642567", "descricao": "5-HTP e interações serotoninérgicas — revisão clínica"},
            {"referencia": "Turner et al. 2006", "pmid": "16648321", "descricao": "Suplementos serotoninérgicos e risco em combinação com SSRI"}
          ]
        },
        "acao": "BLOQUEAR — sem override",
        "manejo": "Nunca combinar 5htp acima de 100mg/dia com SSRI. Risco de síndrome serotoninérgica."
      },
      {
        "id": "int_006",
        "elementos": ["kava_kava", "hepatopatia", "alcool"],
        "tipo": "condicao_clinica",
        "logica_elementos": "OR — a interação aplica-se quando kava_kava é combinado com hepatopatia OU com alcool. Não requer a presença simultânea dos dois.",
        "nota_elementos": "hepatopatia e alcool são condições clínicas independentes — não são IDs do sistema. Cada uma, isoladamente, já contra-indica kava_kava. Hepatopatia deve ser confirmada por avaliação médica. Álcool refere-se a uso ativo ou dependência.",
        "severidade": "critica",
        "mecanismo": "Kava-lactonas são metabolizadas pelo CYP450 hepático — em fígado comprometido ou sob álcool: acúmulo de metabólitos hepatotóxicos → hepatotoxicidade grave",
        "risco_clinico": "Hepatotoxicidade grave — insuficiência hepática — potencialmente fatal",
        "base_evidencia": {
          "tipo": "mecanismo_farmacologico_humano",
          "regra_5_aplicada": true,
          "grade_efetivo": "B",
          "fontes": [
            {"referencia": "Teschke et al. 2011", "pmid": "21277832", "descricao": "Kava e hepatotoxicidade — revisão sistemática de casos clínicos"},
            {"referencia": "Sarris et al. 2013", "pmid": "23433940", "descricao": "Kava — segurança clínica e contraindicações"}
          ]
        },
        "acao": "BLOQUEAR — sem override",
        "manejo": "Avaliar função hepática ANTES de kava_kava em qualquer paciente. Hepatopatia presente ou uso de álcool = contraindicação absoluta.",
        "alternativas": [
          "Ansiedade com hepatopatia: passiflora GRADE B | lavanda_silexan GRADE A",
          "Ansiedade com álcool: lteanina GRADE B | magnesio_glicinato GRADE B"
        ]
      },
      {
        "id": "int_007",
        "elementos": ["rhodiola_rosea", "litio"],
        "tipo": "par_medicamento",
        "logica_elementos": "AND — ambos os elementos devem estar presentes para a interação ocorrer",
        "nota_ids": "Lítio é fármaco externo ao catálogo — não possui ID canônico no sistema",
        "severidade": "critica",
        "mecanismo": "Rhodiola pode alterar excreção renal de lítio — janela terapêutica do lítio é estreita — pequenas alterações de nível sérico causam toxicidade",
        "risco_clinico": "Toxicidade por lítio — tremor, confusão, convulsão, comprometimento renal",
        "base_evidencia": {
          "tipo": "mecanismo_farmacologico_humano",
          "regra_5_aplicada": true,
          "grade_efetivo": "B",
          "fontes": [
            {"referencia": "Brinker 2010", "isbn": "9780443068171", "descricao": "Herb-drug interactions — Elsevier. Rhodiola e lítio."},
            {"referencia": "Ulbricht et al. 2011", "pmid": "21671252", "descricao": "Rhodiola rosea — revisão de segurança e interações"}
          ]
        },
        "acao": "BLOQUEAR — sem override",
        "manejo": "Nunca combinar. Paciente em uso de lítio = rhodiola_rosea contraindicada.",
        "alternativas": [
          "Adaptógeno sem risco com lítio: ashwagandha — avaliar com médico",
          "Fadiga em uso de lítio: decisão psiquiátrica"
        ]
      }
    ]
  },

  "interacoes_altas": {
    "descricao": "ALERTA COM OVERRIDE DOCUMENTADO — risco significativo presente",
    "entradas": [
      {
        "id": "int_005b",
        "elementos": ["5htp", "SSRI"],
        "tipo": "par_medicamento",
        "subtipo": "dose_dependente",
        "logica_elementos": "AND — ambos os elementos devem estar presentes. Condição adicional: dose de 5htp <= 100mg/dia",
        "nota_ids": "SSRI é classe farmacológica externa ao catálogo — não possui ID canônico no sistema",
        "severidade": "alta",
        "dose_limite": "5htp <= 100mg/dia em combinação com SSRI",
        "dose_padrao_protocolo": "5htp 50-100mg/dia",
        "mecanismo": "5-HTP aumenta síntese de serotonina + SSRI bloqueia recaptação → acúmulo serotoninérgico possível",
        "risco_clinico": "Síndrome serotoninérgica — risco presente e monitorável",
        "base_evidencia": {
          "tipo": "mecanismo_farmacologico_humano",
          "regra_5_aplicada": true,
          "grade_efetivo": "B",
          "fontes": [
            {"referencia": "Hinz et al. 2012", "pmid": "22642567", "descricao": "5-HTP e interações serotoninérgicas — revisão clínica"},
            {"referencia": "Turner et al. 2006", "pmid": "16648321", "descricao": "Suplementos serotoninérgicos e risco em combinação com SSRI"}
          ]
        },
        "acao": "ALERTAR — override permitido com documentação médica obrigatória",
        "manejo": "Dose <= 100mg/dia com SSRI: risco serotoninérgico presente e monitorável — requer decisão médica documentada e monitoramento ativo. Protocolo padrão do sistema: 50-100mg/dia.",
        "alternativas": [
          "Se em uso de SSRI e deseja suporte serotoninérgico: ltriptofano tem menor risco relativo — decisão médica",
          "Nota P4: ltriptofano NUNCA tag augmentation_ssri — ver DECISOES_ARQUITETURAIS P4"
        ]
      }
    ]
  },

  "interacoes_moderadas": {
    "descricao": "Risco presente — manejo possível com ajuste de protocolo",
    "entradas": [
      {
        "id": "int_008",
        "elementos": ["ashwagandha", "rhodiola_rosea", "passiflora"],
        "tipo": "tripla",
        "logica_elementos": "AND — os três elementos devem estar presentes simultaneamente para a interação ocorrer",
        "severidade": "moderada",
        "mecanismo": "Combinação de três moduladores do eixo HPA e GABAérgicos — potencial de sedação excessiva e hipocortisolismo em uso simultâneo",
        "risco_clinico": "Sedação excessiva — potencial hipocortisolismo iatrogênico",
        "base_evidencia": {
          "tipo": "observacional_clinico",
          "grade": "C",
          "fontes": [
            {"referencia": "Savage et al. 2018", "pmid": "28930577", "descricao": "Interações entre adaptógenos e ansiolíticos fitoterápicos"}
          ]
        },
        "acao": "Alertar — ajustar protocolo",
        "manejo": {
          "regra_principal": "Máximo 2 dos 3 simultaneamente",
          "se_3_necessarios": "rhodiola_rosea pela manhã | ashwagandha + passiflora à noite",
          "justificativa": "Rhodiola tem efeito estimulante diurno — separação temporal reduz sobreposição"
        },
        "alternativas": [
          "Escolher 2 conforme mecanismo predominante do paciente",
          "Ansiedade predominante: ashwagandha + passiflora",
          "Fadiga predominante: rhodiola_rosea + ashwagandha"
        ]
      }
    ]
  },

  "observacoes_protocolo": {
    "descricao": "Combinações seguras na dose padrão — risco apenas fora da faixa terapêutica",
    "nota": "Observação de protocolo NÃO é contraindicação. É informação para o profissional.",
    "entradas": [
      {
        "id": "int_009",
        "elementos": ["omega3_epa_dha", "kava_kava"],
        "tipo": "par",
        "logica_elementos": "AND — ambos os elementos devem estar presentes. Condição adicional: dose de omega3 > 4g EPA/dia",
        "severidade": "observacao_protocolo",
        "mecanismo": "omega3 em dose muito alta (> 4g EPA/dia) pode potencializar efeito anticoagulante — teórico na combinação com kava_kava",
        "dose_padrao_protocolo": "1-2g EPA/dia",
        "dose_de_risco": "> 4g EPA/dia",
        "status_dose_padrao": "FORA DO RISCO — dose padrão 1-2g EPA/dia não apresenta evidência de risco",
        "evidencia_direta_combinacao": false,
        "grade_combinacao": "D",
        "base_evidencia": {
          "nota": "Sem evidência direta da combinação em dose padrão. Risco teórico apenas em supradose."
        },
        "acao": "Informar profissional — não bloquear em dose padrão",
        "manejo": "Manter dose padrão 1-2g EPA/dia. Se dose > 4g/dia necessária: avaliar individualmente.",
        "alternativas": [
          "Se dose alta de omega3 necessária: considerar suspensão temporária de kava_kava",
          "Ansiedade sem kava_kava: lavanda_silexan GRADE A | passiflora GRADE B"
        ]
      }
    ]
  },

  "instrucoes_uso": {
    "descricao": "Fluxo de consulta a este catálogo durante geração de protocolo — ordem canônica P13",
    "referencia_arquitetural": "DECISOES_ARQUITETURAIS_v2_5.json — P13",
    "quando_consultar": "ANTES de qualquer suplemento entrar no output clínico",
    "fluxo": [
      {
        "passo": 0,
        "acao": "Verificar risco vital — R01 absoluto",
        "referencia": "_regras_globais.json → R01",
        "resultado_bloqueio": "INTERROMPER TUDO — acionar recursos de crise (CVV 188, SAMU 192, CAPS, UPA). Nenhuma interação de suplemento é processada até risco vital resolvido.",
        "excecao": "Nenhuma"
      },
      {
        "passo": 1,
        "acao": "Verificar perfil profissional — item pode ser prescrito?",
        "referencia": "_regras_globais.json → R02",
        "resultado_bloqueio": "BLOQUEAR — item fora do escopo legal do profissional"
      },
      {
        "passo": 2,
        "acao": "Verificar condições clínicas do paciente — contraindicações absolutas",
        "foco": "hepatopatia → int_006 | bipolar sem estabilizador → int_004",
        "resultado_bloqueio": "BLOQUEAR — contraindicação absoluta — sem override"
      },
      {
        "passo": 3,
        "acao": "Listar todos os medicamentos em uso do paciente"
      },
      {
        "passo": 4,
        "acao": "Para cada suplemento candidato: verificar interações críticas com medicamentos",
        "foco": "int_002 (erva_sao_joao + SSRI/SNRI) | int_003 (SAMe + IMAO) | int_005a (5htp > 100mg + SSRI) | int_007 (rhodiola_rosea + lítio)",
        "resultado_bloqueio": "BLOQUEAR — sem override"
      },
      {
        "passo": 5,
        "acao": "Verificar combinações entre suplementos do próprio protocolo",
        "foco": "int_001 (erva_sao_joao + 5htp) | int_005b (5htp <= 100mg + SSRI) | int_008 (tripla adaptógenos)",
        "resultado_por_severidade": {
          "critica": "BLOQUEAR — sem override (int_001)",
          "alta": "ALERTAR — override permitido com documentação médica (int_005b)",
          "moderada": "ALERTAR — informativo — ajustar protocolo (int_008)"
        }
      },
      {
        "passo": 6,
        "acao": "Verificar observações de protocolo para suplementos em dose não-padrão",
        "foco": "int_009 — omega3 > 4g/dia",
        "resultado": "INFORMAR profissional — não bloquear em dose padrão"
      },
      {
        "passo": 7,
        "acao": "Documentar no output: interações verificadas + resultado da verificação"
      }
    ],
    "regra_interacao_nao_catalogada": "Combinação não listada aqui + suspeita de interação → tratar como severidade=alta até revisão bibliográfica",
    "regra_atualizacao_catalogo": "Nova interação identificada com evidência GRADE B ou superior → adicionar neste arquivo na mesma sessão"
  },

  "historico_mapeamento_ids": {
    "descricao": "Registro histórico de realocação de IDs durante fase de desenvolvimento",
    "natureza": "CHANGELOG — não constitui instrução operacional do programa",
    "nota_para_ia": "Este campo é registro histórico de desenvolvimento. Não representa dependência funcional. Os IDs canônicos ativos são os declarados nas entradas de interacoes_criticas, interacoes_altas, interacoes_moderadas e observacoes_protocolo deste documento.",
    "mapeamento_historico": {
      "int_008": {
        "conteudo": "tripla adaptógenos — ashwagandha + rhodiola_rosea + passiflora",
        "severidade": "moderada",
        "status": "ID CANÔNICO ATIVO"
      },
      "int_009": {
        "conteudo": "omega3_epa_dha + kava_kava",
        "severidade": "observacao_protocolo",
        "status": "ID CANÔNICO ATIVO"
      },
      "ids_descontinuados": {
        "pipeline_int_002": "realocado → int_009",
        "pipeline_int_003": "realocado → int_008",
        "nota": "IDs pipeline_int_00X eram nomenclatura interna de desenvolvimento. Não existem no programa. Não confundir com IDs canônicos int_002 (erva_sao_joao + SSRI/SNRI) e int_003 (SAMe + IMAO) que são entradas ativas e distintas neste catálogo."
      }
    }
  },

  "semantic_layer": {
    "clinical_summary": "Catálogo autoritativo de interações entre suplementos, fitoterápicos e medicamentos para uso em saúde mental integrativa. Garante segurança clínica ao bloquear combinações de risco comprovado e orientar o manejo de interações moderadas antes da geração de qualquer protocolo. Consultar obrigatoriamente antes de qualquer suplemento entrar no output clínico.",
    "rag_context_hint": "Recuperar quando: verificar segurança de combinação suplemento-medicamento | paciente em uso de SSRI SNRI IMAO lítio | suspeita de síndrome serotoninérgica | kava_kava e função hepática | SAMe e bipolaridade | rhodiola e lítio | omega3 e kava em dose alta",
    "clinical_domains": [
      "seguranca_clinica",
      "farmacologia_integrativa",
      "fitoterapia_clinica",
      "psiquiatria_integrativa"
    ],
    "semantic_keywords": [
      "interações medicamentosas", "síndrome serotoninérgica",
      "hepatotoxicidade", "crise hipertensiva", "switch maníaco",
      "toxicidade lítio", "bloqueio sem override", "REGRA_5",
      "erva de São João", "SAMe", "kava_kava", "dose-dependente"
    ],
    "related_entities": [
      "_regras_globais.json",
      "_fluxo_primeira_consulta.json",
      "erva_sao_joao",
      "5htp",
      "same",
      "kava_kava",
      "rhodiola_rosea",
      "omega3_epa_dha",
      "ashwagandha",
      "passiflora",
      "ltriptofano",
      "acafrao_crocus"
    ],
    "embedding_priority": "alta"
  },

  "nota_desenvolvimento": "Este documento é componente permanente do programa. As ferramentas de geração de conteúdo (UNIVERSAL_CORE_COMPACTO, KIT_QUALIDADE_NARRATIVA, KITs específicos e GPM — Gerador de Profundidade Molecular, ver P21) são ferramentas de desenvolvimento externas — não fazem parte do programa e não devem ser referenciadas durante sua operação."
}


5 # FLUXO PRIMEIRA consulta            (AUDITADO PELO CHATGPT, ARENA, DEEPSEEK  15/06/2026   02:30h)


{
  "id": "_fluxo_primeira_consulta",
  "tipo": "infraestrutura_global",
  "subtipo": "fluxo_decisorio",
  "versao": "2.5",
  "pipeline_versao_geracao": "2.6",
  "titulo": "Fluxo da Primeira Consulta",
  "descricao": "Guia decisório sequencial para o profissional de saúde integrativa conduzir a primeira consulta — da triagem de risco vital à geração do protocolo individualizado.",
  "subordinado_a": [
    "DECISOES_ARQUITETURAIS_v2_5.json",
    "_regras_globais.json",
    "_interacoes_cruzadas_globais.json",
    "_ids_oficiais.json"
  ],
  "natureza_sistema": {
    "tipo": "suporte_decisao_clinica",
    "nao_substitui_julgamento_profissional": true,
    "nao_realiza_diagnostico": true,
    "decisao_final_profissional": true
  },
  "versionamento": {
    "versao": "2.5",
    "pipeline_versao_geracao": "2.6",
    "nota": "versao = schema do conteudo clinico (invariavel). pipeline_versao_geracao = metadado de rastreabilidade. Sao independentes."
  },

  "bloco_0_triagem_risco_vital": {
    "posicao": "SEMPRE PRIMEIRO — antes de qualquer outra ação",
    "regra_absoluta": "Nenhuma etapa subsequente se inicia com risco vital não resolvido",
    "gatilhos": [
      {
        "gatilho": "PHQ-9 item 9 > 0",
        "acao": "PARAR TUDO",
        "recursos": {
          "CVV": "188 — gratuito — 24h",
          "SAMU": "192",
          "CAPS": "encaminhar imediatamente",
          "UPA": "encaminhar imediatamente"
        },
        "instrucao": "Não prosseguir com protocolo. Acompanhar o paciente até recurso de crise acionado."
      },
      {
        "gatilho": "C-SSRS positivo em qualquer item",
        "acao": "PARAR TUDO",
        "recursos": {
          "CVV": "188 — gratuito — 24h",
          "SAMU": "192",
          "CAPS": "encaminhar imediatamente",
          "UPA": "encaminhar imediatamente"
        },
        "instrucao": "Não prosseguir com protocolo. C-SSRS positivo = emergência clínica."
      },
      {
        "gatilho": "Relato verbal de ideação suicida",
        "acao": "PARAR TUDO",
        "recursos": {
          "CVV": "188 — gratuito — 24h",
          "SAMU": "192",
          "CAPS": "encaminhar imediatamente",
          "UPA": "encaminhar imediatamente"
        },
        "instrucao": "Não prosseguir com protocolo. Acompanhar até recurso acionado."
      },
      {
        "gatilho": "Comportamento de risco vital observado",
        "acao": "PARAR TUDO",
        "recursos": {
          "CVV": "188 — gratuito — 24h",
          "SAMU": "192",
          "CAPS": "encaminhar imediatamente",
          "UPA": "encaminhar imediatamente"
        },
        "instrucao": "Não prosseguir com protocolo. Acionar recurso de crise imediatamente."
      }
    ],
    "nota": "Este bloco prevalece sobre toda lógica subsequente do fluxo. Sem exceção."
  },

  "bloco_1_perfil_profissional": {
    "descricao": "Identificar perfil antes de determinar quais ferramentas estão disponíveis nesta sessão",
    "perfis": [
      {
        "perfil": "naturopata",
        "base_legal": "CFP Resolução 09/2018",
        "escalas_permitidas": [
          "exame_phq9",
          "exame_gad7",
          "exame_dass21",
          "exame_isi",
          "exame_pss",
          "exame_mbi",
          "exame_pcl5",
          "exame_cssrs"
        ],
        "escalas_restringidas": [
          {
            "escala": "exame_ham_d",
            "alternativa": "exame_phq9",
            "instrucao": "Não aplicar HAM-D. Usar PHQ-9."
          },
          {
            "escala": "exame_ham_a",
            "alternativa": "exame_gad7",
            "instrucao": "Não aplicar HAM-A. Usar GAD-7."
          },
          {
            "escala": "exame_ybocs",
            "alternativa": null,
            "instrucao": "Encaminhar especialista."
          },
          {
            "escala": "exame_pdss",
            "alternativa": null,
            "instrucao": "Encaminhar especialista."
          }
        ],
        "notas_especiais": [
          "exame_mbi: uso educacional — declarar explicitamente ao paciente",
          "exame_pcl5: cautela — encaminhar obrigatoriamente se pontuação >= 33",
          "exame_cssrs: rastreio itens 1-2 (ideação passiva) apenas — encaminhar se qualquer item positivo",
          "dhea: restrito — médico ou médico ortomolecular apenas"
        ]
      },
      {
        "perfil": "medico_ortomolecular",
        "escalas_disponiveis": "todas",
        "acesso_adicional": [
          "dhea — requer exame_dhea_s",
          "exame_ham_d",
          "exame_ham_a",
          "exame_ybocs — dentro do CRM",
          "exame_pdss — dentro do CRM",
          "Prescrever medicamentos dentro do CRM"
        ]
      },
      {
        "perfil": "medico",
        "escalas_disponiveis": "todas",
        "acesso_adicional": [
          "exame_ham_d",
          "exame_ham_a",
          "exame_ybocs — dentro do CRM",
          "exame_pdss — dentro do CRM",
          "dhea — requer exame_dhea_s",
          "Solicitar todos os exames C2 a C11",
          "Prescrever medicamentos dentro do CRM"
        ]
      },
      {
        "perfil": "psiquiatra",
        "escalas_disponiveis": "todas",
        "acesso_adicional": [
          "Tudo do medico",
          "exame_cssrs — protocolo completo",
          "Realizar diagnóstico psiquiátrico",
          "Prescrever medicamentos psiquiátricos"
        ]
      },
      {
        "perfil": "psicologo",
        "escalas_disponiveis": "todas",
        "acesso_adicional": [
          "exame_ham_d",
          "exame_ham_a",
          "exame_cssrs — protocolo completo",
          "Realizar diagnóstico psicológico"
        ],
        "restricao": "Suplementação: encaminhar para médico ou naturopata habilitado"
      },
      {
        "perfil": "nutricionista",
        "base_legal": "Regulamentação CRN vigente por estado",
        "escalas_permitidas": [
          "exame_phq9",
          "exame_gad7",
          "exame_dass21",
          "exame_isi",
          "exame_pss"
        ],
        "escalas_restringidas": [
          {
            "escala": "exame_ham_d",
            "alternativa": "exame_phq9",
            "instrucao": "Não aplicar HAM-D. Usar PHQ-9."
          },
          {
            "escala": "exame_ham_a",
            "alternativa": "exame_gad7",
            "instrucao": "Não aplicar HAM-A. Usar GAD-7."
          },
          {
            "escala": "exame_ybocs",
            "alternativa": null,
            "instrucao": "Encaminhar especialista."
          },
          {
            "escala": "exame_pdss",
            "alternativa": null,
            "instrucao": "Encaminhar especialista."
          }
        ],
        "notas_especiais": [
          "Escalas: uso de rastreio — encaminhar se positivo",
          "Suplementação: dentro do escopo CRN conforme regulamentação vigente",
          "dhea: restrito — médico ou médico ortomolecular apenas",
          "Não realizar diagnóstico psiquiátrico ou psicológico"
        ]
      },
      {
        "perfil": "enfermeiro_treinado",
        "base_legal": "COFEN 564/2017 | Lei 7.498/1986 | CFP 09/2018",
        "base_evidencia_grade_b": "Posner 2011 — Psychiatry 68(12) | Mundt 2013 — Depression and Anxiety 30(8) n=284",
        "escalas_permitidas": [
          "exame_phq9",
          "exame_gad7",
          "exame_dass21",
          "exame_isi",
          "exame_pss",
          "exame_mbi",
          "exame_cssrs",
          "exame_pcl5"
        ],
        "escalas_restringidas": [
          {
            "escala": "exame_ham_d",
            "alternativa": "exame_phq9",
            "instrucao": "Não aplicar HAM-D. Usar PHQ-9."
          },
          {
            "escala": "exame_ham_a",
            "alternativa": "exame_gad7",
            "instrucao": "Não aplicar HAM-A. Usar GAD-7."
          },
          {
            "escala": "exame_ybocs",
            "alternativa": null,
            "instrucao": "Encaminhar especialista."
          },
          {
            "escala": "exame_pdss",
            "alternativa": null,
            "instrucao": "Encaminhar especialista."
          }
        ],
        "notas_especiais": [
          "exame_mbi: rastreio ocupacional — declarar uso como triagem ao paciente",
          "exame_cssrs: aplicação COMPLETA em triagem e emergência — diferença do naturopata que aplica apenas itens 1-2 — encaminhar imediatamente se positivo",
          "exame_pcl5: rastreio — encaminhar obrigatoriamente se pontuação >= 33",
          "Qualquer resultado positivo: encaminhar imediatamente ao profissional responsável",
          "Não prescrever suplementos ou medicamentos",
          "Não realizar diagnóstico"
        ]
      },
      {
        "perfil": "outro",
        "instrucao": "Encaminhar para profissional habilitado. Usar somente escalas abertas sem restrição."
      }
    ]
  },

  "bloco_2_queixa_principal": {
    "descricao": "Coleta estruturada da queixa antes de aplicar escalas",
    "campos": [
      {
        "campo": "queixa_principal",
        "tipo": "texto_livre",
        "obrigatorio": true
      },
      {
        "campo": "dominios_afetados",
        "tipo": "multipla_escolha",
        "opcoes": ["humor", "ansiedade", "sono", "cognicao", "energia", "dor", "outro"],
        "obrigatorio": true
      },
      {
        "campo": "tempo_evolucao",
        "tipo": "texto",
        "opcoes_sugeridas": [
          "< 2 semanas", "2-4 semanas", "1-3 meses",
          "3-6 meses", "> 6 meses", "> 1 ano"
        ],
        "obrigatorio": true
      },
      {
        "campo": "tratamentos_anteriores",
        "tipo": "texto_livre",
        "obrigatorio": false,
        "nota": "Incluir psicoterapia, medicamentos, suplementos anteriores"
      },
      {
        "campo": "medicamentos_em_uso",
        "tipo": "lista",
        "obrigatorio": true,
        "gatilho": "Qualquer medicamento listado → verificar bloco_6 antes de prosseguir",
        "flags_criticas": [
          {
            "medicamento_classe": "SSRI ou SNRI",
            "alerta": "Bloquear erva_sao_joao (int_002). Bloquear 5htp > 100mg/dia (int_005). Ver _interacoes_cruzadas_globais.json."
          },
          {
            "medicamento_classe": "IMAO",
            "alerta": "Bloquear SAMe (int_003). Bloquear erva_sao_joao (int_002). Risco de crise hipertensiva."
          },
          {
            "medicamento_classe": "Lítio",
            "alerta": "Bloquear rhodiola_rosea (int_007). Risco de toxicidade por lítio."
          },
          {
            "medicamento_classe": "Estabilizador de humor",
            "alerta": "Suspeita de bipolaridade → avaliar SAMe com cautela máxima (int_004). Encaminhar psiquiatria antes."
          }
        ]
      },
      {
        "campo": "condicoes_associadas",
        "tipo": "lista",
        "obrigatorio": true,
        "gatilho": "Condições listadas → verificar bloco_6 contraindicações absolutas",
        "flags_criticas": [
          {
            "condicao": "Hepatopatia ou uso de álcool",
            "alerta": "Bloquear kava_kava — hepatotoxicidade (int_006)."
          },
          {
            "condicao": "Transtorno bipolar",
            "alerta": "Bloquear SAMe sem estabilizador confirmado (int_004). Encaminhar psiquiatria primeiro."
          },
          {
            "condicao": "Gravidez ou lactação",
            "alerta": "Revisão individual obrigatória antes de qualquer suplemento."
          }
        ]
      }
    ]
  },

  "bloco_3_escalas": {
    "descricao": "Aplicação sequencial de escalas conforme domínios afetados e perfil profissional",
    "regra_sequencia": "PHQ-9 sempre primeiro — item 9 é gatilho de risco vital",
    "escalas": [
      {
        "ordem": 1,
        "id": "exame_phq9",
        "indicacao": "Sempre — triagem depressão",
        "gatilho_item_9": "Score > 0 no item 9 → Bloco 0 imediatamente",
        "encaminhamento": "PHQ-9 >= 20 → psiquiatria obrigatório"
      },
      {
        "ordem": 2,
        "id": "exame_gad7",
        "indicacao": "Sempre — triagem ansiedade",
        "encaminhamento": "GAD-7 >= 15 → avaliação psiquiátrica recomendada"
      },
      {
        "ordem": 3,
        "id": "exame_isi",
        "indicacao": "Se domínio sono afetado",
        "condicional": "dominios_afetados inclui sono"
      },
      {
        "ordem": 4,
        "id": "exame_pss",
        "indicacao": "Se domínio estresse afetado ou suspeita burnout"
      },
      {
        "ordem": 5,
        "id": "exame_dass21",
        "indicacao": "Panorama tripartido — alternativa ou complementar ao PHQ-9 + GAD-7",
        "nota": "Não duplicar PHQ-9 se DASS-21 já aplicado e vice-versa — escolher conforme tempo disponível"
      },
      {
        "ordem": 6,
        "id": "exame_mbi",
        "indicacao": "Suspeita burnout — uso educacional",
        "restricao_naturopata": "Declarar uso educacional ao paciente",
        "condicional": "queixa de esgotamento + contexto ocupacional"
      },
      {
        "ordem": 7,
        "id": "exame_pcl5",
        "indicacao": "Suspeita de trauma",
        "condicional": "queixa de evento traumático ou hipervigilância",
        "encaminhamento": "PCL-5 >= 33 → encaminhar psicologia ou psiquiatria"
      },
      {
        "ordem": 8,
        "id": "exame_cssrs",
        "indicacao": "Rastreio de suicídio — aplicar se PHQ-9 item 9 > 0 OU suspeita clínica",
        "restricao_naturopata": "Apenas rastreio itens 1-2 — qualquer item positivo = encaminhar imediatamente",
        "escopo_enfermeiro": "Aplicação COMPLETA em triagem e emergência",
        "encaminhamento": "C-SSRS positivo → Bloco 0 imediatamente"
      }
    ],
    "escalas_fora_do_escopo_naturopata": [
      {"id": "exame_ham_d", "acao": "Não aplicar. Usar exame_phq9."},
      {"id": "exame_ham_a", "acao": "Não aplicar. Usar exame_gad7."},
      {"id": "exame_ybocs", "acao": "Encaminhar especialista."},
      {"id": "exame_pdss", "acao": "Encaminhar especialista."}
    ]
  },

  "bloco_4_exames": {
    "descricao": "Solicitação de exames por prioridade clínica",
    "regra_tipo_2": "Exames C3 só geram ação se déficit confirmado. Exame normal = sem ação TIPO_2.",
    "exames_essenciais_minimos": {
      "descricao": "Obrigatórios para protocolo base — solicitar em toda primeira consulta",
      "lista": [
        "exame_hemograma_completo",
        "exame_tireoide_funcional",
        "exame_vitd",
        "exame_b12",
        "exame_ferritina_ferro"
      ],
      "nota": "Estes 5 exames são pré-requisito mínimo antes de qualquer protocolo de suplementação"
    },
    "grupos": [
      {
        "grupo": "C2_causa_organica",
        "prioridade": 1,
        "descricao": "Sempre solicitar — excluir causa orgânica antes de suplementar",
        "exames": [
          "exame_tireoide_funcional",
          "exame_hemograma_completo",
          "exame_ferritina_ferro",
          "exame_glicemia_hba1c",
          "exame_glicemia_insulina",
          "exame_cortisol_matinal",
          "exame_funcao_hepatica",
          "exame_albumina",
          "exame_eletrolitos"
        ],
        "nota_glicemia": "exame_glicemia_hba1c e exame_glicemia_insulina são IDs distintos — hba1c rastreia DM, insulina rastreia resistência insulínica"
      },
      {
        "grupo": "C3_deficiencias",
        "prioridade": 2,
        "descricao": "TIPO_2 — só age com déficit confirmado",
        "exames": [
          {
            "id": "exame_vitd",
            "limiar_acao": "< 30 ng/mL → corrigir vitd3_k2",
            "limiar_normal": "> 50 ng/mL → sem ação TIPO_2"
          },
          {
            "id": "exame_b12",
            "limiar_acao": "< 300 pg/mL → corrigir b12_metilcobalamina",
            "nota": "Valores 300-450 pg/mL — zona cinzenta — avaliar contexto clínico"
          },
          {
            "id": "exame_folato",
            "limiar_acao": "< 4 ng/mL → corrigir com metilfolato"
          },
          {
            "id": "exame_magnesio_eritrocitario",
            "nota": "Magnésio sérico NÃO suficiente — eritrocitário obrigatório",
            "limiar_acao": "< 4.2 mg/dL → corrigir magnesio_treonato ou magnesio_glicinato"
          },
          {
            "id": "exame_zinco",
            "limiar_acao": "< 70 mcg/dL → corrigir zinco_bisglicinato"
          },
          {
            "id": "exame_homocisteina",
            "limiar_acao": "> 10 mcmol/L → investigar B12 + folato + B6"
          },
          {
            "id": "exame_omega3_index",
            "nota": "TIPO_2 secundário — omega3_epa_dha entra por diagnóstico (TIPO_1 primário). Exame orienta dose, não entrada.",
            "limiar_acao": "< 4% → déficit significativo — reforçar dose"
          },
          {
            "id": "exame_selenio",
            "limiar_acao": "< 70 mcg/L → investigar déficit"
          },
          {
            "id": "exame_b6_p5p",
            "limiar_acao": "< 20 nmol/L → corrigir vitamina_b6_p5p"
          }
        ]
      },
      {
        "grupo": "C4_inflamatorios",
        "prioridade": 3,
        "condicional": "Suspeita de neuroinflamação — fadiga crônica, depressão refratária, dor difusa",
        "exames": [
          "exame_pcr_us",
          "exame_il6",
          "exame_fibrinogenio",
          "exame_vhs"
        ]
      },
      {
        "grupo": "C5_hpa",
        "prioridade": 4,
        "condicional": "Suspeita de disfunção do eixo HPA — fadiga, hipocortisolismo, hipercortisolismo",
        "exames": [
          "exame_cortisol_salivar_4pts",
          "exame_cortisol_urinario_24h",
          "exame_dhea_s",
          "exame_dutch_test",
          {
            "id": "exame_dexametasona",
            "template": "C-LAB",
            "nota_p2": "Classificado como C-LAB por DECISOES_ARQUITETURAIS_v2_5.json P2. Não C-FUNC. Permanece em C5_hpa."
          }
        ],
        "nota_dhea_gate": "dhea (suplemento D1): TIPO_2 puro. Gate duplo obrigatório: (1) exame_dhea_s com déficit confirmado + (2) perfil médico ou médico_ortomolecular ativo. Ausência de qualquer um = BLOQUEAR prescrição de dhea."
      },
      {
        "grupo": "C6_neurotransmissores",
        "prioridade": 5,
        "condicional": "Suspeita de déficit de monoaminas — depressão refratária, anedonia intensa",
        "exames": [
          "exame_serotonina_plaquetaria",
          "exame_aminoacidos_plasmaticos",
          "exame_acido_metilmalonico"
        ]
      },
      {
        "grupo": "C8_farmacogenomica",
        "prioridade": 6,
        "condicional": "Resposta inconsistente a tratamentos anteriores",
        "exames": [
          "exame_mthfr",
          "exame_comt",
          "exame_slc6a4",
          "exame_bdnf_val66met",
          "exame_mao_a",
          "exame_cyp2d6_2c19"
        ]
      },
      {
        "grupo": "C9_sono",
        "prioridade": 7,
        "condicional": "Distúrbio de sono significativo — ISI >= 15 ou suspeita de apneia",
        "exames": [
          "exame_melatonina_salivar_dlmo",
          "exame_polissonografia",
          "exame_actigrafia"
        ]
      },
      {
        "grupo": "C10_microbiota",
        "prioridade": 8,
        "condicional": "Suspeita de eixo intestino-cérebro — sintomas gastrointestinais + humor",
        "exames": [
          "exame_zonulina",
          "exame_lps_serico",
          "exame_calprotectina",
          "exame_16s_rrna"
        ]
      },
      {
        "grupo": "C7_acidos_organicos",
        "prioridade": 9,
        "condicional": "Investigação metabólica ampla — fadiga refratária, suspeita mitocondrial",
        "exames": ["exame_oat"]
      },
      {
        "grupo": "C11_metais",
        "prioridade": 10,
        "condicional": "Suspeita de intoxicação por metais pesados",
        "exames": ["exame_metais_pesados"]
      }
    ]
  },

  "bloco_5_mecanismos": {
    "descricao": "Mapeamento dos mecanismos fisiopatológicos ativos com base em escalas + exames",
    "instrucao": "Identificar mecanismos predominantes para orientar seleção de intervenções",
    "mecanismos": [
      {
        "id": "mecanismo_B1_neuroinflamacao",
        "gatilhos_clinicos": ["PCR-us elevado", "IL-6 elevado", "depressão com fadiga", "resistência a tratamento"],
        "exames_correlatos": ["exame_pcr_us", "exame_il6", "exame_fibrinogenio"]
      },
      {
        "id": "mecanismo_B2_eixo_hpa_cortisol",
        "gatilhos_clinicos": ["fadiga matinal", "hipocortisolismo", "hipercortisolismo", "PSS elevado"],
        "exames_correlatos": ["exame_cortisol_salivar_4pts", "exame_cortisol_matinal", "exame_dutch_test", "exame_dhea_s"]
      },
      {
        "id": "mecanismo_B3_neuroplasticidade",
        "gatilhos_clinicos": ["depressão crônica", "déficit cognitivo", "anedonia"],
        "exames_correlatos": ["exame_bdnf_val66met"]
      },
      {
        "id": "mecanismo_B4_deficiencias_monoaminas",
        "gatilhos_clinicos": ["anedonia", "baixa motivação", "depressão com hipersonia"],
        "exames_correlatos": ["exame_serotonina_plaquetaria", "exame_aminoacidos_plasmaticos"]
      },
      {
        "id": "mecanismo_B5_gaba_glutamato",
        "gatilhos_clinicos": ["ansiedade generalizada", "insônia de manutenção", "hiperexcitabilidade"],
        "exames_correlatos": ["exame_oat"]
      },
      {
        "id": "mecanismo_B6_estresse_oxidativo",
        "gatilhos_clinicos": ["fadiga oxidativa", "envelhecimento precoce", "exposição a toxinas"],
        "exames_correlatos": ["exame_oat", "exame_metais_pesados"]
      },
      {
        "id": "mecanismo_B7_eixo_intestino_cerebro",
        "gatilhos_clinicos": ["sintomas gastrointestinais + humor", "SII + depressão", "disbiose"],
        "exames_correlatos": ["exame_zonulina", "exame_lps_serico", "exame_calprotectina", "exame_16s_rrna"]
      },
      {
        "id": "mecanismo_B8_deficiencias_micronutrientes",
        "gatilhos_clinicos": ["múltiplos déficits em C3", "dieta restritiva", "má absorção"],
        "exames_correlatos": ["exame_vitd", "exame_b12", "exame_folato", "exame_magnesio_eritrocitario", "exame_zinco"]
      },
      {
        "id": "mecanismo_B9_disfuncao_mitocondrial",
        "gatilhos_clinicos": ["fadiga profunda", "intolerância ao exercício", "névoa cognitiva"],
        "exames_correlatos": ["exame_oat", "exame_acido_metilmalonico"]
      },
      {
        "id": "mecanismo_B10_desregulacao_circadiana",
        "gatilhos_clinicos": ["ISI elevado", "inversão de ciclo", "trabalho noturno", "jet lag crônico"],
        "exames_correlatos": ["exame_melatonina_salivar_dlmo", "exame_actigrafia", "exame_cortisol_salivar_4pts"]
      },
      {
        "id": "mecanismo_B11_disfuncao_tireoidiana",
        "gatilhos_clinicos": ["fadiga + ganho de peso", "depressão + frio", "TSH alterado"],
        "exames_correlatos": ["exame_tireoide_funcional"]
      },
      {
        "id": "mecanismo_B12_neurobiologia_trauma",
        "gatilhos_clinicos": ["PCL-5 positivo", "trauma precoce", "TEPT", "dissociação"],
        "exames_correlatos": ["exame_pcl5", "exame_bdnf_val66met"]
      },
      {
        "id": "mecanismo_B13_sistema_endocanabinoide",
        "gatilhos_clinicos": ["dor crônica + ansiedade", "fibromialgia", "resistência a tratamento"],
        "exames_correlatos": []
      },
      {
        "id": "mecanismo_B14_neuroesteroides_hormonios",
        "gatilhos_clinicos": ["perimenopausa", "andropausa", "DHEA-s baixo", "progesterona baixa"],
        "exames_correlatos": ["exame_dhea_s", "exame_dutch_test"]
      },
      {
        "id": "mecanismo_B15_autofagia_mtor",
        "gatilhos_clinicos": ["envelhecimento + cognição", "síndrome metabólica + humor"],
        "exames_correlatos": ["exame_glicemia_insulina", "exame_glicemia_hba1c"],
        "nota_p5": "MECANISMO SECUNDÁRIO — P5. Não usar como gatilho principal de protocolo. Pode influenciar como mecanismo complementar em regras combinadas."
      },
	  {
  "id": "mecanismo_B16_neurogenese",
  "gatilhos_clinicos": ["depressão crônica de longa duração", "resposta parcial a antidepressivo", "défice de memória hipocampal", "idade avançada com declínio cognitivo associado a humor"],
  "exames_correlatos": ["exame_bdnf_val66met"]
    }
    ]
  },

  "bloco_6_seguranca_pre_protocolo": {
    "descricao": "Verificação de segurança obrigatória ANTES de gerar qualquer protocolo de suplementação",
    "nota_precedencia": "Etapa 1 da ordem canônica P13 (risco vital) já executada em bloco_0 — pré-requisito obrigatório para chegar a este bloco. Este bloco executa as etapas 2-4 da ordem canônica P13.",
    "ordem_canonica_p13_completa": [
      "1. Risco vital — VERIFICADO em bloco_0 (interrompe consulta se positivo)",
      "2. Restrições legais por perfil → etapa_1_restricoes_legais",
      "3. Contraindicações absolutas → etapa_2_contraindicacoes_absolutas",
      "4. Interações críticas → etapa_3_interacoes_criticas"
    ],
    "ordem_execucao": "etapa_1_restricoes_legais → etapa_2_contraindicacoes_absolutas → etapa_3_interacoes_criticas",
    "referencia_arquitetural": "DECISOES_ARQUITETURAIS_v2_5.json — P13",
    "regra": "Todo medicamento e condição listada no Bloco 2 deve ser cruzado aqui antes de prosseguir",
    "referencia_completa": "_interacoes_cruzadas_globais.json",
    "etapa_1_restricoes_legais": {
      "descricao": "Profissional pode prescrever este item?",
      "referencia": "_fluxo_primeira_consulta.json → bloco_1_perfil_profissional",
      "acao_bloqueio": "Item fora do escopo do perfil → bloquear → oferecer alternativa legal se existir"
    },
    "etapa_2_contraindicacoes_absolutas": {
      "descricao": "Paciente pode receber este item?",
      "lista": [
        "kava_kava: hepatopatia ou uso de álcool",
        "SAMe: transtorno bipolar sem estabilizador",
        "SAMe: em uso de IMAO",
        "erva_sao_joao: em uso de SSRI, SNRI ou IMAO",
        "5htp > 100mg/dia: em uso de SSRI — alta dose = > 100mg/dia → BLOQUEAR | <= 100mg/dia → decisão médica documentada obrigatória",
        "rhodiola_rosea: em uso de lítio",
        "DHEA: sem prescrição médica"
      ],
      "acao_bloqueio": "BLOQUEAR — sem override"
    },
    "etapa_3_interacoes_criticas": {
      "descricao": "A combinação é segura?",
      "referencia_completa": "_interacoes_cruzadas_globais.json",
      "resumo": [
        {
          "id": "int_001",
          "par": "erva_sao_joao + 5htp",
          "severidade": "critica",
          "acao": "BLOQUEAR — sem override. Washout >= 2 semanas."
        },
        {
          "id": "int_002",
          "par": "erva_sao_joao + SSRI ou SNRI",
          "severidade": "critica",
          "acao": "BLOQUEAR — sem override"
        },
        {
          "id": "int_003",
          "par": "SAMe + IMAO",
          "severidade": "critica",
          "acao": "BLOQUEAR — sem override"
        },
        {
          "id": "int_004",
          "par": "SAMe + bipolar sem estabilizador confirmado",
          "severidade": "critica",
          "acao": "BLOQUEAR — sem override"
        },
        {
          "id": "int_005",
          "par": "5htp + SSRI",
          "severidade": "critica",
          "limiar": "> 100mg/dia = BLOQUEAR | <= 100mg/dia = decisão médica documentada",
          "acao": "BLOQUEAR acima de 100mg/dia — sem override"
        },
        {
          "id": "int_006",
          "par": "kava_kava + hepatopatia ou álcool",
          "severidade": "critica",
          "acao": "BLOQUEAR — sem override"
        },
        {
          "id": "int_007",
          "par": "rhodiola_rosea + lítio",
          "severidade": "critica",
          "acao": "BLOQUEAR — sem override"
        },
        {
          "id": "int_008",
          "tripla": ["ashwagandha", "rhodiola_rosea", "passiflora"],
          "severidade": "moderada",
          "acao": "Máx 2 dos 3. Se os 3: rhodiola manhã, ashwagandha + passiflora noite."
        },
        {
          "id": "int_009",
          "par": "omega3_epa_dha + kava_kava",
          "severidade": "observacao_protocolo",
          "nota": "Dose padrão 1-2g EPA/dia fora do risco. Risco apenas > 4g/dia.",
          "acao": "Informar — não bloquear em dose padrão"
        }
      ]
    }
  },

  "bloco_7_geracao_protocolo": {
    "descricao": "Geração do protocolo individualizado após aprovação de todos os blocos anteriores",
    "pre_requisitos": [
      "Bloco 0 — risco vital descartado ou resolvido",
      "Bloco 1 — perfil profissional identificado",
      "Bloco 2 — queixa coletada e flags verificadas",
      "Bloco 3 — escalas aplicadas",
      "Bloco 4 — exames solicitados ou resultados disponíveis",
      "Bloco 5 — mecanismos mapeados",
      "Bloco 6 — segurança verificada em ordem P13"
    ],
    "sequencia_geracao": [
      {
        "passo": 1,
        "acao": "Selecionar cenário E1-E10 mais próximo do perfil clínico",
        "ids_cenarios": [
          "cenario_E1", "cenario_E2", "cenario_E3", "cenario_E4", "cenario_E5",
          "cenario_E6", "cenario_E7", "cenario_E8", "cenario_E9", "cenario_E10"
        ]
      },
      {
        "passo": 2,
        "acao": "Mapear suplementos TIPO_1",
        "regra": "Entram por diagnóstico ou quadro clínico — independem de exame",
        "declaracao_obrigatoria": "tipo_primario: TIPO_1 em cada suplemento",
        "gate_bloqueante": true,
        "gate_regra": "tipo_primario ausente = suplemento não entra no protocolo. Equivalente a GRADE ausente."
      },
      {
        "passo": 3,
        "acao": "Mapear suplementos TIPO_2",
        "regra": "Entram APENAS se exame confirma déficit",
        "declaracao_obrigatoria": "tipo_primario: TIPO_2 + exame + valor que justifica",
        "gate_bloqueante": true,
        "gate_regra": "Exame normal = NÃO incluir suplemento TIPO_2. Sem exceção."
      },
      {
        "passo": 4,
        "acao": "Verificar suplementos DUAL",
        "ids_dual": [
          "omega3_epa_dha", "vitd3_k2", "b12_metilcobalamina",
          "magnesio_treonato", "zinco_bisglicinato"
        ],
        "nota_ferro": "ferro_bisglicinato = TIPO_2 puro — entrada depende exclusivamente de déficit laboratorial confirmado",
        "regra": "Declarar tipo_primario + tipo_secundario. tipo_primario determina critério de entrada."
      },
      {
        "passo": 5,
        "acao": "Declarar GRADE de cada intervenção",
        "regra": "GRADE ausente = suplemento não entra no protocolo"
      },
      {
        "passo": 6,
        "acao": "Documentar EA esperados",
        "regra": "EA ausente = output incompleto — reprovar"
      },
      {
        "passo": 7,
        "acao": "Definir frequência de seguimento",
        "padrao": "4-6 semanas para primeira reavaliação"
      }
    ]
  },

  "bloco_8_encaminhamentos": {
    "descricao": "Critérios de encaminhamento obrigatório — não opcionais",
    "encaminhamentos": [
      {
        "gatilho": "PHQ-9 >= 20",
        "destino": "Psiquiatria",
        "urgencia": "alta",
        "instrucao": "Encaminhar antes ou simultaneamente ao protocolo integrativo"
      },
      {
        "gatilho": "C-SSRS positivo",
        "destino": "Urgência / CAPS",
        "urgencia": "imediata",
        "instrucao": "Bloco 0 — não prosseguir com protocolo"
      },
      {
        "gatilho": "PCL-5 >= 33",
        "destino": "Psicologia ou Psiquiatria",
        "urgencia": "alta",
        "instrucao": "Encaminhar. Protocolo integrativo pode ser adjuvante — não substituto."
      },
      {
        "gatilho": "Escala Y-BOCS ou PDSS solicitada",
        "destino": "Especialista",
        "urgencia": "programada",
        "instrucao": "Escala fora do escopo — encaminhar para avaliação especializada"
      },
      {
        "gatilho": "Suspeita de transtorno bipolar",
        "destino": "Psiquiatria",
        "urgencia": "alta",
        "instrucao": "ANTES de iniciar SAMe ou rhodiola_rosea — risco de indução de mania"
      },
      {
        "gatilho": "Hepatopatia + interesse em kava_kava",
        "destino": "Hepatologista",
        "urgencia": "programada",
        "instrucao": "kava_kava contraindicada em hepatopatia — avaliar alternativas"
      },
      {
        "gatilho": "GAD-7 >= 15",
        "destino": "Avaliação psiquiátrica",
        "urgencia": "alta",
        "instrucao": "Ansiedade grave — considerar coadjuvância psiquiátrica"
      }
    ]
  },

  "bloco_9_monitoramento": {
    "descricao": "Estrutura de reavaliação sistemática após protocolo iniciado",
    "frequencia_padrao": "4-6 semanas",
    "acoes_reavaliacao": [
      "Reaplicar escalas usadas na primeira consulta",
      "Comparar pontuações com baseline",
      "Verificar exames TIPO_2 corrigidos — suspender suplemento se déficit normalizado",
      "Registrar EA observados pelo paciente",
      "Verificar novas interações se medicamentos foram alterados",
      "Atualizar protocolo conforme resposta clínica",
      "Reavaliação de encaminhamento se piora clínica"
    ],
    "criterios_ajuste_protocolo": [
      {
        "cenario": "Melhora > 50% nas escalas em 6 semanas",
        "acao": "Manter protocolo. Considerar redução gradual em 3-6 meses."
      },
      {
        "cenario": "Melhora < 25% em 8 semanas",
        "acao": "Revisar mecanismos. Verificar adesão. Considerar encaminhamento adicional."
      },
      {
        "cenario": "Piora ou surgimento de novo sintoma",
        "acao": "Reavaliar interações. Suspeitar EA. Encaminhar se necessário."
      },
      {
        "cenario": "PHQ-9 item 9 > 0 em qualquer reavaliação",
        "acao": "Bloco 0 imediatamente — independente de qualquer protocolo em curso"
      }
    ]
  },

  "semantic_layer": {
    "clinical_summary": "Fluxo decisório sequencial para condução da primeira consulta em saúde integrativa — da triagem de risco vital à geração de protocolo individualizado. Estrutura o raciocínio clínico em 10 blocos encadeados garantindo segurança, legalidade e coerência com a literatura. Usar como guia operacional em toda primeira consulta.",
    "rag_context_hint": "Recuperar quando: profissional inicia primeira consulta | dúvida sobre ordem das etapas clínicas | triagem de risco vital | seleção de escalas por perfil profissional | verificação de segurança pré-protocolo | encaminhamentos obrigatórios | monitoramento pós-protocolo",
    "clinical_domains": [
      "triagem_clinica",
      "seguranca_clinica",
      "decisao_terapeutica",
      "monitoramento"
    ],
    "semantic_keywords": [
      "primeira consulta", "fluxo decisório", "triagem de risco",
      "PHQ-9", "C-SSRS", "escalas validadas", "exames C2 C3",
      "TIPO_1 TIPO_2", "encaminhamento obrigatório",
      "naturopata", "CFP 09/2018", "mecanismos fisiopatológicos",
      "perfil profissional", "segurança clínica"
    ],
    "related_entities": [
      "_regras_globais.json",
      "_interacoes_cruzadas_globais.json",
      "_ids_oficiais.json",
      "DECISOES_ARQUITETURAIS_v2_5.json",
      "exame_phq9",
      "exame_gad7",
      "exame_cssrs",
      "exame_pcl5",
      "exame_vitd",
      "exame_b12",
      "exame_magnesio_eritrocitario",
      "algoritmo_resultado_protocolo"
    ],
    "embedding_priority": "alta"
  },

  "nota_desenvolvimento": "Este documento é componente permanente do programa. As ferramentas de geração de conteúdo (UNIVERSAL_CORE_COMPACTO, KIT_QUALIDADE_NARRATIVA, KITs específicos e GPM — Gerador de Profundidade Molecular, ver P21) são ferramentas de desenvolvimento externas — não fazem parte do programa e não devem ser referenciadas durante sua operação."
}




