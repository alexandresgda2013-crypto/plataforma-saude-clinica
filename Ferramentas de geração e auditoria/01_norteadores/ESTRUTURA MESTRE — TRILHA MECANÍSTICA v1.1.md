ESTRUTURA MESTRE — TRILHA MECANÍSTICA v1.1
yaml
# ============================================
# ESTRUTURA MESTRE — PAINEL MACRO — TRILHA MECANÍSTICA
# v1.1
# Correção vs. v1.0: a tabela referencia_cruzada_documentos apontava
# para "Protocolo de Escopo M1_NEUROINFLAMACAO_MECANISMO" (nome
# antigo, Documento 1) e "Schema-Claim Mecanismo v2.0" (versão
# desatualizada, Documento 2 é agora v3.1). Corrigido. Nenhuma outra
# mudança — o restante do documento já estava correto (B1-B16, sem
# M1-M16) desde a entrega anterior.
# ============================================

nota_sincronizacao: >
  Fonte de verdade para status macro da TRILHA MECANÍSTICA (claims
  B{n}.MEC.*), paralela e independente ao painel macro da TRILHA
  CLÍNICA (claims B{n}.SM*). Os dois painéis referenciam os MESMOS
  16 mecanismos oficiais (B1-B16, _ids_oficiais.json) — a diferença
  é a trilha de trabalho (mecanística vs. clínica) sobre o mesmo
  mecanismo, nunca uma numeração de mecanismo separada.

MECANISMOS_TRILHA_MECANISTICA:
  B1:  {nome: Neuroinflamação, status: EM_PRODUCAO, trilha_clinica_correspondente: "B1/SM-02 (EM_PRODUCAO_ATIVO)"}
  B2:  {nome: "Eixo HPA e Cortisol Crônico", status: nao_iniciado}
  B3:  {nome: Neuroplasticidade, status: nao_iniciado, nota: "NÓ CENTRAL — obrigatório para todos os demais via BLOCO09"}
  B4:  {nome: "Deficiência de Monoaminas", status: nao_iniciado}
  B5:  {nome: "Desregulação GABA/Glutamato", status: nao_iniciado}
  B6:  {nome: "Estresse Oxidativo Cerebral", status: nao_iniciado}
  B7:  {nome: "Disbiose e Eixo Intestino-Cérebro", status: nao_iniciado}
  B8:  {nome: "Deficiências de Micronutrientes", status: nao_iniciado}
  B9:  {nome: "Disfunção Mitocondrial", status: nao_iniciado}
  B10: {nome: "Desregulação Circadiana e Sono", status: nao_iniciado}
  B11: {nome: "Disfunção Tireoidiana", status: nao_iniciado}
  B12: {nome: "Neurobiologia do Trauma", status: nao_iniciado}
  B13: {nome: "Sistema Endocanabinoide", status: nao_iniciado}
  B14: {nome: "Neuroesteroides e Hormônios", status: nao_iniciado}
  B15: {nome: "Autofagia, mTOR e Clearance", status: nao_iniciado}
  B16: {nome: Neurogênese, status: nao_iniciado, nota: "componente especializado de B3"}

B1_SUBMODULOS_MECANISTICOS:  # 11 total — espelham BLOCO do Prompt 4.0
  B1.MEC.BLOCO01: {nome: "Fundamentos", status: nao_iniciado, prioridade: P0}
  B1.MEC.BLOCO02: {nome: "Mecanismos moleculares (vias, genética)", status: nao_iniciado, prioridade: P0}
  B1.MEC.BLOCO03: {nome: "Mediadores específicos", status: nao_iniciado, prioridade: P0}
  B1.MEC.BLOCO04: {nome: "Células e estruturas", status: nao_iniciado, prioridade: P0}
  B1.MEC.BLOCO05: {nome: "Biomarcadores", status: nao_iniciado, prioridade: P0}
  B1.MEC.BLOCO06: {nome: "Tradução clínica + insuficiência monoaminérgica", status: nao_iniciado, prioridade: P1}
  B1.MEC.BLOCO07: {nome: "Nós moleculares centrais", status: nao_iniciado, prioridade: P1}
  B1.MEC.BLOCO08: {nome: "Conexões B2-B16 e loops de amplificação", status: nao_iniciado, prioridade: P0}
  B1.MEC.BLOCO09: {nome: "Impacto sobre neuroplasticidade (B3)", status: nao_iniciado, prioridade: P0}
  B1.MEC.BLOCO10: {nome: "Impacto sobre neurogênese (B16) — condicional", status: nao_iniciado, prioridade: P2}
  B1.MEC.BLOCO11_12: {nome: "Estratificação e cenários — condicional/dependente", status: nao_iniciado, prioridade: P2}

B1_PRIORIDADES_RACIONAL:
  P0_conteudo_molecular_obrigatorio:
    submodulos: [B1.MEC.BLOCO01, B1.MEC.BLOCO02, B1.MEC.BLOCO03, B1.MEC.BLOCO04, B1.MEC.BLOCO05]
    porque: >
      São os blocos de conteúdo bruto do mecanismo (fundamentos, vias,
      mediadores, células, biomarcadores) — sem eles não existe
      substância científica para nenhum bloco posterior sintetizar.
      Todos com contagem mínima de palavras obrigatória no Prompt 4.0
      (não condicionais).
  P0_mandato_arquitetural_explicito:
    submodulos: [B1.MEC.BLOCO08, B1.MEC.BLOCO09]
    porque: >
      BLOCO09 é obrigatório por princípio hierárquico declarado no
      Prompt 4.0 ("Todos os mecanismos... devem explicar explicitamente
      como influenciam a neuroplasticidade" — B3 é mecanismo integrador
      central, não opcional). BLOCO08 é obrigatório porque o JSON final
      (connection_strength) exige valor para as 16 posições B1-B16, e o
      próprio Prompt 4.0 proíbe deixar qualquer uma sem "correspondência
      mínima registrada no corpo deste bloco".
  P1_explicacao_e_hierarquizacao:
    submodulos: [B1.MEC.BLOCO06, B1.MEC.BLOCO07]
    porque: >
      Tradução clínica e identificação de nós centrais aprofundam e
      hierarquizam o que já foi levantado em P0 — de alto valor, mas
      dependem logicamente do conteúdo de BLOCO02-05 já existir.
  P2_condicional:
    submodulos: [B1.MEC.BLOCO10, B1.MEC.BLOCO11_12]
    porque: >
      Explicitamente opcionais no próprio Prompt 4.0 ("aplicar apenas
      quando..."), com regra de dependência declarada (BLOCO12 só
      existe se BLOCO11 existir). Podem legitimamente fechar como N/A.

totais_B1:
  claims_reais_auditados: 0
  estimativa_projetada_completa: >
    a definir incrementalmente pela prática — sem faixa numérica a
    priori, diferente do módulo clínico, porque a densidade de PMID
    por BLOCO varia muito mais entre categorias moleculares (ex:
    inflamassomas vs. RLRs) do que entre compartimentos de amostra
    clínica (sangue/LCR/PET seguem volume mais previsível)

referencia_cruzada_documentos:
  lista_canonica_ativa: "Lista Canônica — B1/MEC (Documento 5)"
  escopo: "Protocolo de Escopo B1 — Trilha Mecanística v1.1 (Documento 1)"
  processo: "Como Executar — B1 Trilha Mecanística v1.1 (Documento 3)"
  formato_claim: "Schema-Claim Mecanismo v3.1 (Documento 2)"
  bloco_de_estado: "Bloco de Estado — B1 Trilha Mecanística v1.0 (Documento 6)"
  candidatos_ids: "CANDIDATOS_IDS_OFICIAIS.yaml — ledger único, compartilhado com a trilha clínica (Documento 7)"
  gpm_correspondente: "GPM_B1_Neuroinflamacao.md + Briefing B1 — obrigatório, ver Como Executar"
  painel_espelho_clinico: "Estrutura Mestre B1 (trilha clínica, B1/SM-02) — painel irmão, não fundir"
