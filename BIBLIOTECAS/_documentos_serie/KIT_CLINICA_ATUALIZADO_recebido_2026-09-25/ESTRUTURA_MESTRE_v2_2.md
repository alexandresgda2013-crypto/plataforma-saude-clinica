# ============================================
# ESTRUTURA MESTRE — PAINEL MACRO
# v2.2 — 2026-09-16
#
# Histórico de versões:
#   v2.0 — Lista canônica de SM-02 foi EXTRAÍDA para arquivo próprio
#          (ver "Lista Canônica — SM-02"). Este documento passou a ser
#          só painel de progresso, permanece pequeno e estável
#          independente de quantos claims existam em cada submódulo.
#   v2.1 — Adicionada seção B1_PRIORIDADES_RACIONAL — justificativa
#          por trás das marcações P0/P1/P2 já existentes nos
#          submódulos (o "porquê" da priorização, não apenas o rótulo).
#   v2.2 — Reposicionamento: a trilha de claims por submódulo (SM-01 a
#          SM-14) é a trilha CLÍNICA e alimenta a pasta
#          evidencias/bibliografia. A biblioteca canônica mecanística
#          dos 16 mecanismos tem pipeline próprio (bibliotecas prontas,
#          em auditoria). Adicionada seção TRILHAS; contagem real de
#          SM-02 atualizada; SM-03+ aguardando decisão de contrato do
#          motor clínico e schemas de evidencias/bibliografia.
# ============================================

nota_sincronizacao: >
  Este documento é fonte de verdade para status macro (quais
  mecanismos/submódulos estão ativos, contagem real vs. estimada).
  Detalhamento claim-a-claim do submódulo ativo vive em "Lista
  Canônica — Submódulo Ativo" (arquivo separado, trocado a cada
  novo SM).

TRILHAS:
  mecanistica:
    produto: "biblioteca canônica mecanística (fisiologia, cascata bioquímica)"
    escopo: "16 mecanismos"
    status: "16 bibliotecas produzidas — em auditoria"
    observacao: "pipeline próprio; NÃO usa os claims de SM-xx deste painel"
  clinica:
    produto: "claims clínicos atômicos ancorados em PMID (G1/G2/G3)"
    destino: "pasta evidencias/bibliografia"
    status: "B1/SM-02 em fechamento; demais submódulos aguardando decisão"
    formato_saida: "Schema-Claim v1.2 — provisório até decisão do schema de evidencias/bibliografia"
  dependencias_em_aberto:
    - "contrato do motor clínico"
    - "schemas da pasta evidencias/bibliografia"

MODULOS_MECANISMO:  # 16 total — ver _ids_oficiais.mecanismos
  B1: {nome: Neuroinflamação, status: EM_PRODUCAO}
  B2: {nome: "Eixo HPA e Cortisol Crônico", status: nao_iniciado}
  B3: {nome: Neuroplasticidade, status: nao_iniciado, nota: "NÓ CENTRAL"}
  B4: {nome: "Deficiência de Monoaminas", status: nao_iniciado}
  B5: {nome: "Desregulação GABA/Glutamato", status: nao_iniciado}
  B6: {nome: "Estresse Oxidativo Cerebral", status: nao_iniciado}
  B7: {nome: "Disbiose e Eixo Intestino-Cérebro", status: nao_iniciado}
  B8: {nome: "Deficiências de Micronutrientes", status: nao_iniciado}
  B9: {nome: "Disfunção Mitocondrial", status: nao_iniciado}
  B10: {nome: "Desregulação Circadiana e Sono", status: nao_iniciado}
  B11: {nome: "Disfunção Tireoidiana", status: nao_iniciado}
  B12: {nome: "Neurobiologia do Trauma", status: nao_iniciado}
  B13: {nome: "Sistema Endocanabinoide", status: nao_iniciado}
  B14: {nome: "Neuroesteroides e Hormônios", status: nao_iniciado}
  B15: {nome: "Autofagia, mTOR e Clearance", status: nao_iniciado}
  B16: {nome: Neurogênese, status: nao_iniciado, nota: "componente de B3"}

B1_SUBMODULOS:  # 14 total
  SM-01: {nome: "Definição e delimitação", claims_estimado: "8-12", status: nao_iniciado}
  SM-02: {nome: "Prova de existência", claims_real: 35, aprovados: "14 principais + 8 subclaims", em_busca: 4, pendentes: 17, status: EM_FECHAMENTO, prioridade: P0}
  SM-03: {nome: "Direção de causalidade", claims_estimado: "15-25", status: aguardando_decisao_contrato_e_schemas, prioridade: P0}
  SM-04: {nome: Microglia, claims_estimado: "20-30", status: nao_iniciado, prioridade: P1}
  SM-05: {nome: Astrócitos, claims_estimado: "15-20", status: nao_iniciado}
  SM-06: {nome: "Imunidade periférica/interface", claims_estimado: "15-20", status: nao_iniciado}
  SM-07: {nome: "Citocinas e quimiocinas", claims_estimado: "35-50", status: nao_iniciado, prioridade: P0}
  SM-08: {nome: "Vias de sinalização intracelular", claims_estimado: "20-30", status: nao_iniciado, prioridade: P1}
  SM-09: {nome: "Estresse oxidativo/nitrosativo", claims_estimado: "20-25", status: nao_iniciado}
  SM-10: {nome: "Barreira hematoencefálica", claims_estimado: "15-20", status: nao_iniciado}
  SM-11: {nome: "Neurotransmissão e plasticidade", claims_estimado: "25-35", status: nao_iniciado, prioridade: P1}
  SM-12: {nome: "Circuitos, cognição, comportamento", claims_estimado: "20-30", status: nao_iniciado}
  SM-13: {nome: "Fenótipo clínico e heterogeneidade", claims_estimado: "25-35", status: nao_iniciado, prioridade: P1}
  SM-14: {nome: "Resposta a intervenção", claims_estimado: "20-30", status: nao_iniciado, prioridade: P0}

B1_PRIORIDADES_RACIONAL:
  # Justificativa por trás das marcações de prioridade já atribuídas
  # em B1_SUBMODULOS acima — não duplica dado, complementa com o "porquê".
  P0_nucleo:
    submodulos: [SM-02, SM-03, SM-07, SM-14]
    porque: >
      Provam o fenômeno (existência), a causalidade (direção), os
      mediadores (citocinas/quimiocinas) e a reversibilidade (resposta
      a intervenção). Sem esses 4, não há base suficiente para o motor
      clínico operar sobre este mecanismo.
  P1_mecanismo:
    submodulos: [SM-04, SM-08, SM-11, SM-13]
    porque: >
      Explicam o "como" (células, sinalização) e a heterogeneidade
      clínica (por que só um subgrupo responde) — aprofundam sem
      serem pré-requisito absoluto do núcleo.
  P2_completude:
    submodulos: [SM-01, SM-05, SM-06, SM-09, SM-10, SM-12]
    porque: >
      Profundidade e cobertura adicional — enriquecem a biblioteca,
      mas o motor clínico pode operar com informação parcial aqui
      sem comprometer a análise central.

totais_B1:
  claims_reais_auditados: 35   # apenas SM-02, único com lista canônica fechada
  claims_aprovados_em_G3: 22   # 14 principais + 8 subclaims (Bloco de Estado v1.7)
  estimativa_projetada_completa: "280-420"
  nota: >
    "REAL" = claims-alvo formalizados em lista canônica com query
    definida (independente de status de aprovação em G1/G2/G3).
    "estimativa" = faixa de planejamento para dimensionamento de
    esforço, não é contagem auditada.

referencia_cruzada_documentos:
  lista_canonica_ativa: "Lista Canônica — SM-02 v1.4 (arquivo separado)"
  estado: "Bloco de Estado v1.7"
  escopo: "Protocolo de Escopo B1 vigente"
  processo: "Como Executar vigente"
  formato_claim: "Schema-Claim vigente"

