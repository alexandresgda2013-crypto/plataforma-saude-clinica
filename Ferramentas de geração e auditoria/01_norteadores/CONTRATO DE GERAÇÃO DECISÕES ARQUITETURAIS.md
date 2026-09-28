#Contrato de Geração de Biblioteca de Mecanismo


> **NOTA DE IDENTIDADE DESTE ARQUIVO:** este documento consolida, para
> fins de sessão, tanto os itens P (decisões arquiteturais, P1-P20)
> quanto os itens R (regras globais, R01-R12). Onde outro documento
> deste kit cita `_regras_globais.json` ou `DECISOES_ARQUITETURAIS_v2_5.json`
> como arquivo separado, entenda-se: mesmo conteúdo deste arquivo
> único, seções R e P respectivamente — não há arquivo adicional
> faltando.

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
"regra_grade_escopo": "GRADE A-D (regra acima) rege exclusivamente Zona 1E — Intervenções/Suplementos/C-LAB (ver Checklist de Fidelidade Canônica, item C3). A Biblioteca de Mecanismo usa forca_evidencia_afirmacao (alto|medio|baixo), namespace separado, nunca cruzado (ver Prompt 4.2, DEFINIÇÕES DE GRADAÇÃO). Campo grade literal A-D em arquivo de mecanismo é hard-fail, não cobertura desta regra.",
"regra_limitacoes": "Limitações declaradas sempre — nunca omitir",
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
"max_mecanismos_por_sessao_geracao": 1,
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
	  
	  
	  
	  