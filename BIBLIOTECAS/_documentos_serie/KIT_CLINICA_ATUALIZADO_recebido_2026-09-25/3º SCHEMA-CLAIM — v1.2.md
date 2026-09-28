
---

# SCHEMA-CLAIM — v1.2

yaml
# ============================================
# SCHEMA_CLAIM — v1.2
# Correção vs. v1.1:
#   - reintroduzido campo evidence_role (existia na Especificação da
#     Plataforma original, Seção 7, mas caiu na reescrita do schema
#     para v1.0/v1.1 — erro de continuidade, corrigido agora)
#   - adicionada regra de validação cruzada evidence_role × uso
#   - Nenhuma outra mudança em relação à v1.1
# ============================================

nota_namespace: >
  claim_id NÃO é validado contra _ids_oficiais.json. Claims seguem
  namespace próprio (B{n}.SM{nn}.{nnn}[a-z opcional]), validados
  exclusivamente contra a Lista Canônica do submódulo de origem.
  _ids_oficiais valida apenas entidades de nível superior (mecanismos,
  exames, suplementos, cenários, escalas) referenciadas no campo
  referencia_cruzada.

claim_id: string          # formato: B{n}.SM{nn}.{nnn} ou subclaim .{nnn}{a-z}
version: int
status: aprovado | aprovado_com_ressalva | em_busca | rejeitado | aposentado
verification: verificado_nesta_conversa | herdado_nao_verificado_por_mim
statement: string

evidence_role: human_clinical | human_experimental | post_mortem | preclinical_mechanistic
  # OBRIGATÓRIO. Define a natureza da evidência de origem:
  # human_clinical = estudo observacional/clínico em humanos (coorte,
  #   caso-controle, meta-análise de estudos humanos)
  # human_experimental = estudo intervencional em humanos (RCT)
  # post_mortem = tecido humano post-mortem
  # preclinical_mechanistic = modelo animal ou in vitro — serve
  #   exclusivamente para explicar mecanismo, nunca para clinical_claim
  # VALIDAÇÃO CRUZADA OBRIGATÓRIA: se evidence_role = preclinical_mechanistic,
  # então uso DEVE ser contexto_mecanistico. Nunca clinico.

uso: clinico | contexto_mecanistico | gap_pesquisa
  # OBRIGATÓRIO. Define como o motor clínico pode empregar o claim:
  # clinico = pode embasar sugestão/narrativa direta ao profissional
  # contexto_mecanistico = suporta explicação de mecanismo, não ação clínica
  # gap_pesquisa = evidência incerta/insuficiente, sinaliza lacuna, não sustenta ação

especificidade: especifico_depressao | especifico_ansiedade | transdiagnostico | nulo

nota_ressalva: string | nulo
  # OBRIGATÓRIO se status = aprovado_com_ressalva
  # Curta, objetiva, sem alarme. Ex: "Efeito por sexo não é consistente entre estudos."

moderadores: [ ]  # lista, pode ser vazia
  # cada item:
  # - variavel: string          (ex: IMC, classe_antidepressivo, trauma_infancia)
  #   efeito: atenua | inverte | amplifica | nulo
  #   regra_motor: string       # tradução operacional para o motor clínico
  #   fonte_pmid: string

fontes:
  - pmid: string
    autor: string
    ano: int
    nivel: principal | corroborante | exploratorio
    comparador: string
      # OBRIGATÓRIO. Contra o quê o achado foi medido.
      # ex: controles_saudaveis | transtorno_bipolar | outros_transtornos_psiquiatricos
      # Para evidence_role=preclinical_mechanistic, comparador pode ser
      # ex: veiculo_salino | grupo_sham | wild_type
    especie: humano | roedor | outro_animal | in_vitro
      # OBRIGATÓRIO apenas quando evidence_role = preclinical_mechanistic;
      # opcional/nulo nos demais casos (implícito = humano)
    n: int | nulo
    k: int | nulo           # nº de estudos, se meta-análise
    achado: string           # número/efeito literal (d, OR, IC95%, RR)
    papel: string | nulo     # o que ESTA fonte prova, especificamente (se distinto do achado)
    verificado_nesta_conversa: sim | nao

fontes_exploratorias: [ ]    # mesma estrutura de fontes, nível informativo/não decisivo

referencia_cruzada: [ ]
  # formato: ID oficial completo, conforme _ids_oficiais.mecanismos
  # ex: [mecanismo_B12_neurobiologia_trauma]
  # shorthand (B12) aceito apenas em anotações informais, NUNCA no campo estruturado

usado_em_biblioteca: sim | nao
  # OBRIGATÓRIO, padrão nao. Marca sim quando este claim já foi
  # incorporado a uma Biblioteca de Conhecimento gerada (Prompt 4.0),
  # com claim_id_origem preenchido no Módulo 09 correspondente. Não
  # bloqueia nada no fluxo G1→G2→G3 — é rastreabilidade de consumo
  # rio abaixo, atualizada no passo 8 do Processo de Geração.

fila_realocacao:
  - pmid: string
    motivo: string
    destino: string   # submódulo ou mecanismo de destino