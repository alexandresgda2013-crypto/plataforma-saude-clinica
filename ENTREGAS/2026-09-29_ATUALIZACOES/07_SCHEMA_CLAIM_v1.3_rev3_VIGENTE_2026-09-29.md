---
---

# SCHEMA-CLAIM — v1.3 (rev.3 — VIGENTE)
# ---------------------------------------------------------------------------
# ERRATA DE ETIQUETA — 2026-09-29 (decisão do operador · registrada via Arena)
# O título dizia "(MINUTA rev.3 do ciclo do kit — não vigente)", e o comentário
# do bloco de schema repetia "(MINUTA rev.3 — não vigente)": ficaram da época
# em que o documento ainda era minuta. A vigência do v1.3 rev.3 foi declarada
# em ato próprio de 25/09/2026 (bilhete SCHEMA_CLAIM_V1_3_VIGENTE.txt, com a
# frase do operador) — o que não havia sido trocada era a etiqueta.
# Correção de ETIQUETA e PROCEDÊNCIA: 0 (zero) mudança de conteúdo — as
# alterações são apenas em linhas de comentário (#); nenhum campo, enum,
# obrigatoriedade ou regra foi tocado.
# Texto aprovado em 25/09 = digital 28cbc9c7, preservado byte a byte em
#   "SCHEMA_CLAIM_v1.3_rev3_ASSINADO_28cbc9c7_2026-09-29.bak".
# ---------------------------------------------------------------------------

rev.2 (2026-09-25): V-K3 alinhado à opção preferida do Comentador
  (exploratórias só exigem sentido_do_achado se materializarem)
rev.3 (2026-09-25): V-K6 adicionado (ressalva do Estrutura) + linha de
  grau_maturidade ausente → sem campo no N2

yaml
# ============================================
# SCHEMA_CLAIM — v1.3 (rev.3 — VIGENTE · ver nota de errata no topo)
# Ciclo do kit · 2026-09-25 · Arena Casa
# Mudança vs. v1.2 (somente isto; mais nada):
#   - P-K1: sentido_do_achado POR FONTE (vocabulário importado da
#           SCHEMA-CLAIM MECANISMO v3.1, sem renomear)
#   - P-K2: ressalvas[] com tipo estruturado
#   - P-K3: fonte única de condicao escrita no contrato
#   - P-K5: grau_maturidade_cientifica (vocabulário v3.1) quando
#           houver ressalva de maturidade
#   - Nenhuma outra mudança vs. v1.2 (claim_id, status, evidence_role,
#     uso, especificidade, nota_ressalva, moderadores, fontes,
#     fontes_exploratorias, referencia_cruzada, usado_em_biblioteca,
#     fila_realocacao permanecem idênticos)
# Base normativa: Contrato de Saída do Claim Kit vigente (rev.2,
#   sha 841532da…, aprovado 24/09/2026) — §§ R-1, R-2, P-K1..P-K5
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
  # OBRIGATÓRIO. (idêntico ao v1.2)
  # VALIDAÇÃO CRUZADA OBRIGATÓRIA: se evidence_role = preclinical_mechanistic,
  # então uso DEVE ser contexto_mecanistico. Nunca clinico.

uso: clinico | contexto_mecanistico | gap_pesquisa
  # OBRIGATÓRIO. (idêntico ao v1.2)

especificidade: especifico_depressao | especifico_ansiedade | transdiagnostico | nulo

# ---------- P-K2 (NOVO) ----------
ressalvas: [ ]            # lista, pode ser vazia
  # OBRIGATÓRIO não-vazia quando status = aprovado_com_ressalva
  # (substitui a obrigatoriedade solta do nota_ressalva textual —
  #  nota_ressalva permanece como sumário legível, mas a classificação
  #  estruturada é esta lista)
  # cada item:
  # - tipo: condicao_aplicacao | heterogeneidade | maturidade_evidencia
  #     OBRIGATÓRIO. Enum fechado. É a classificação científica feita
  #     no fechamento do claim (rito das três IAs) — nunca inferida
  #     rio abaixo pelo materializador.
  # - nota: string        # texto da ressalva (o que a nota_ressalva diz)
  # - condicao: string    # SOMENTE quando tipo = condicao_aplicacao
  #     OBRIGATÓRIO se tipo = condicao_aplicacao; proibido (nulo) nos
  #     demais tipos.
  #
  # P-K3 — FONTE ÚNICA DE CONDIÇÃO (regra de contrato, vinculante):
  #   A única origem de condicao no N2 é ressalvas[tipo=condicao_aplicacao]
  #   declarada e aprovada no fechamento.
  #   nota_ressalva (texto livre) NUNCA autoriza condicao.
  #   moderadores[] NUNCA autoriza condicao.
  #   sentido_do_achado NUNCA autoriza condicao.
  #   O materializador COPIA; não interpreta.
  #
  # Papel delimitado (Comentador §11 / contrato §5):
  #   ressalvas[] classifica e registra. NÃO é fonte de direção
  #   (direção é sentido_do_achado por fonte) nem uma "segunda"
  #   condição concorrente.

nota_ressalva: string | nulo
  # OBRIGATÓRIO se status = aprovado_com_ressalva (mantido do v1.2).
  # Sumário textual. NÃO é origem de condicao nem de direcao_suporte.

# ---------- P-K5 (NOVO; opcional) ----------
grau_maturidade_cientifica: muito_estabelecido | bem_suportado | moderadamente_suportado | emergente | hipotese_inicial | nulo
  # NOVO no kit clínico. Vocabulário idêntico ao SCHEMA-CLAIM MECANISMO
  # v3.1 e ao enum grau_maturidade do N2 v1.4 (sem renomear).
  # Preencher quando houver ressalva[tipo=maturidade_evidencia].
  # Materialização: ressalva de maturidade → grau_maturidade no N2;
  #   NUNCA → condicional.

moderadores: [ ]  # lista, pode ser vazia
  # cada item: (idêntico ao v1.2)
  # - variavel: string          (ex: IMC, classe_antidepressivo, trauma_infancia)
  #   efeito: atenua | inverte | amplifica | nulo
  #   regra_motor: string       # tradução operacional para o motor clínico
  #   fonte_pmid: string
  # atenua/amplifica/nulo: permanecem no claim; não materializam em N2.
  # inverte: NÃO materializa em N2 v1.4 (P-K6 travada no contrato de
  #   saída); informação integral fica aqui + ressalvas até o v1.5.

fontes:
  - pmid: string
    autor: string
    ano: int
    nivel: principal | corroborante | exploratorio
    comparador: string
      # OBRIGATÓRIO. (idêntico ao v1.2)
    # ---------- P-K1 (NOVO, por fonte) ----------
    sentido_do_achado: suporta_relacao | refuta_relacao | inconclusivo
      # NOVO. OBRIGATÓRIO para toda fonte de claim com status em
      #   {aprovado, aprovado_com_ressalva}.
      # Vocabulário importado LITERALMENTE do SCHEMA-CLAIM MECANISMO
      #   v3.1 (sem renomear; sem segundo vocabulário).
      # É a direção fonte → afirmação, decidida no fechamento científico.
      # PROIBIÇÕES (contrato R-1):
      #   - inferir de status ("aprovado → suporta_relacao")
      #   - inferir de nivel ("principal → suporta_relacao")
      #   - inferir de achado positivo
      #   - inferir de prosa (statement/comparador)
      # Ausência no claim fechado = claim NÃO fechado /
      #   FALHA DE MATERIALIZAÇÃO (nunca default).
      # Materialização: suporta_relacao→sustenta ·
      #   refuta_relacao→refuta · inconclusivo→inconclusivo
      #   (condicional NÃO vem daqui — nasce só de P-K3)
      # PRECEDÊNCIA (V-K6): se há ressalva[tipo=condicao_aplicacao]
      #   aplicável nesta materialização, vale a linha condicional+
      #   condicao da ressalva; este sentido fica no claim e não
      #   é copiado como direcao_suporte neste ato.
    especie: humano | roedor | outro_animal | in_vitro
      # OBRIGATÓRIO apenas quando evidence_role = preclinical_mechanistic
    n: int | nulo
    k: int | nulo
    achado: string
    papel: string | nulo
    verificado_nesta_conversa: sim | nao

fontes_exploratorias: [ ]    # mesma estrutura de fontes
  # sentido_do_achado: OBRIGATÓRIO apenas se a exploratória for
  #   usada em materialização; se só informativa, pode ficar fora
  #   (opção preferida do Comentador, V-K3 — 2026-09-25).
  #   Default proibido sempre que o campo existir: ou é decidido,
  #   ou a fonte não materializa.

referencia_cruzada: [ ]

usado_em_biblioteca: sim | nao

fila_realocacao:
  - pmid: string
    motivo: string
    destino: string

# ============================================
# MIGRAÇÃO (compatibilidade)
#   - v1.2 → v1.3: claims existentes (corpus 17/09, 27 entries)
#     NÃO são reescritos retroativamente. P-K1 e P-K2 são preenchidos
#     no PRÓXIMO fechamento de cada claim (e sempre antes de qualquer
#     materialização). Claim v1.2 sem sentido_do_achado NÃO materializa
#     (falha dura do contrato de saída).
#   - Validadores cruzados novos (a implementar no ciclo):
#       V-K1: status aprovado_com_ressalva ⇒ ressalvas[] não vazia
#       V-K2: ressalvas[tipo=condicao_aplicacao] ⇒ condicao preenchida;
#             outros tipos ⇒ condicao nula
#       V-K3 (ajuste Comentador 2026-09-25, opção preferida):
#            toda fonte que PARTICIPAR DA MATERIALIZAÇÃO ⇒
#            sentido_do_achado presente; fonte_exploratoria não
#            materializável fica fora — ausência nela NÃO é erro
#            de materialização (se exigir por qualidade do kit,
#            declarar como regra de kit, não como pré-requisito
#            N1/N2)
#       V-K4: grau_maturidade_cientifica preenchido ⇔ existe
#             ressalva[tipo=maturidade_evidencia]
#       V-K5: sentidos ∉ {vazio} para status ∉ {em_busca, rejeitado}
#       V-K6 (ressalva Estrutura 2026-09-25 — PRECEDÊNCIA na materialização):
#            quando a MESMA fonte participa de materialização e existe
#            ressalva[tipo=condicao_aplicacao] aplicável a ela:
#              direcao_suporte materializada = condicional
#              condicao = texto de ressalvas[tipo=condicao_aplicacao].condicao
#              sentido_do_achado da fonte FICA REGISTRADO no claim,
#                mas NÃO vira direcao_suporte neste ato
#            (sem esta regra: copiar os dois gera sustenta+condicao
#             e o N2 reprova — mesmo colapso do D1 na SAÍDA;
#            V-K6 é contrato de materialização, não altera N2)
#       V-K7 (alinhamento fino Estrutura): grau_maturidade_cientifica
#            vazio/opcional ⇒ N2 sem campo grau_maturidade (ausência),
#            nunca null gravado
# ============================================
