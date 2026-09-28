# BLOCO DE ESTADO
# ============================================
# ESTADO v1.8 — 2026-09-17
# Muda em relação à v1.7:
#   - B1.SM02.014 APROVADO_COM_RESSALVA (Grupo 3 / TSPO-PET): 23 entradas
#     aprovadas (15 principais + 8 subclaims)
#   - fluxo de verificação ao vivo autorizado (Como Executar v1.8):
#     29971587 e 23850810 tiveram PMID e números conferidos nesta sessão
#     contra PMC/editor; 36226319 idem
#   - proximo_alvo: .017
#   - P3 (Q014 base v2) resolvida por uso; P1 e P2 seguem abertas
#
# ESTADO v1.7 — 2026-09-16
# Muda em relação à v1.6:
#   - REPOSICIONAMENTO: claims de SM-02 são claims CLÍNICOS (meta-análise,
#     caso-controle, coorte) e têm destino na pasta evidencias/bibliografia,
#     NÃO na biblioteca canônica mecanística (as 16 bibliotecas mecanísticas
#     foram produzidas em pipeline próprio e estão em auditoria). Ver
#     campo destino_final. Formato de saída segue Schema-Claim v1.2 até que
#     o schema de evidencias/bibliografia seja decidido.
#   - corpo já continha claims fechados em 14/08 não refletidos no
#     cabeçalho/contadores: .008, .012, .012b, .012c, .013, .013b, .015 (v2)
#     — contadores corrigidos: 22 entradas aprovadas (14 principais + 8
#     subclaims)
#   - TABs reintroduzidos em .012/.012b/.012c/.015 removidos de novo;
#     indentação de .012, .013, .015 normalizada ("Claim_id" → "claim_id";
#     fontes_exploratorias/referencia_cruzada/usado_em_biblioteca de .015
#     estavam fora do claim)
#   - chave "fontes_rejeitadas:" duplicada no log (o parser descartava o
#     1º bloco inteiro) unificada — 92 entradas únicas, sem PMID repetido
#   - .001b: preenchida nota_ressalva que faltava (status exigia);
#     preenchida especificidade em .001b/.001c/.001d/.002/.003/.004/.007/
#     .007b; completados autor/ano/nivel das fontes de .001c/.001d — tudo
#     a partir de dados já registrados neste arquivo, sem evidência nova
#   - 20132991: entrada do log escopada ao claim .012 (reuso em .012c é
#     permitido pela regra de reuso) — nível em .012c marcado como decisão
#     pendente
#   - nova seção claims_em_andamento (.017, .023, .028, .032) — trabalho
#     iniciado em 13-14/08 sem desfecho formal
#   - nova seção pendencias_decisao_usuario
#   - proximo_alvo atualizado; referência a Como Executar atualizada p/ v1.7
# ============================================
# HISTÓRICO ANTERIOR
# ESTADO v1.6 — 2026-08-13
# Muda em relação à v1.5:
#   - 6 novos claims aprovados nesta sessão: .005, .005b (novo
#     subclaim), .006, .009, .010, .011 — total sobe de 9 para 13
#   - .011: referencia_cruzada corrigido de posição (estava preso
#     dentro de fontes_exploratorias, virou string órfã fora de
#     qualquer chave); ganhou cenario_E99_urgencias_psiquiatricas
#   - removidos TAB characters de .005/.006/.009/.010/.011 (misturados
#     com espaço, quebravam parser — ScannerError confirmado)
#   - padronizado marcador de lista "- claim_id:" em 2 espaços em
#     todos os 13 claims (havia inconsistência: 0, 1 ou 2 espaços)
#   - fontes_rejeitadas consolidado: este arquivo tinha 7 entradas,
#     a Lista Canônica tinha outro bloco (repetido 4x por chave
#     duplicada) com mais 13 — unificados aqui, 20 entradas únicas,
#     Lista Canônica não guarda mais cópia própria (log único, regra
#     que já existia desde v1.4 mas não estava sendo seguida)
#   - nova regra adicionada: registro de resultado de query não é
#     por padrão — só quando tem valor de decisão futura real
#   - proximo_alvo atualizado e corrigido (estava malformado: aspas
#     faltando, sem prefixo "B1.SM02.", e a nota "9/9 são MDD" já
#     não era mais verdade)
# Muda em relação à v1.4:
#   - adicionadas 2 regras: PMID pré-clínico nunca vai para
#     fontes_rejeitadas (vai para resultados_query.redirecionados);
#     PMID nunca citado de memória da IA
#   - adicionado campo usado_em_biblioteca em cada claim aprovado
# Muda em relação à v1.3:
#   - alinhado ao Schema-Claim v1.1 (referencia_cruzada agora usa
#     ID oficial completo, não shorthand)
#   - fontes_rejeitadas confirmado como log único (não duplicado
#     na Estrutura Mestre, que agora é só painel macro)
#   - lista canônica de SM-02 não vive mais aqui — ver arquivo
#     "Lista Canônica — SM-02" para os claims-alvo/queries pendentes
# ============================================

modulo: B1_NEUROINFLAMMATION
natureza_claims: clinico
destino_final: "pasta evidencias/bibliografia (não biblioteca canônica mecanística)"
schema_saida: "Schema-Claim v1.2 — provisório até decisão do schema de evidencias/bibliografia"
objetivo_fase: "fechar SM-02 (.001 a .035); SM-03 só inicia após decisão do contrato do motor clínico e dos schemas de evidencias/bibliografia"
submodulo_ativo: SM-02
fase: 1
portoes: G1 existencia | G2 elegibilidade | G3 suporte_claim
vocabulario: [target, verified_reference, eligible_source, approved_claim]

regras:
  - "Nunca crio ID de claim — vem da Lista Canônica do submódulo. PMID sem ID = unmapped, você decide."
  - "Número só de fonte colada NESTA conversa. Sem caçar referência terciária."
  - "1 pergunta por PMID: sustenta o claim, direto? Sim/uso -> aprova. Não -> 1 linha, próximo."
  - "Reuso de fonte entre claims permitido, se o achado citado for específico daquele claim."
  - "Se PMID sugerir entidade candidata a ID oficial (novo exame/suplemento/biomarcador
     ainda não catalogado), registrar em CANDIDATOS_IDS_OFICIAIS.yaml — não bloqueia
     a validação do claim em curso."
  - "PMID encontrado em busca de trilha_humana que seja estudo animal ou in vitro
     nunca vai para fontes_rejeitadas — vai para resultados_query.redirecionados
     com destino_sugerido (SM-03 | SM-04 | SM-08 conforme natureza do achado)
     e trilha: preclinica. Ver Como Executar v1.7."
  - "Nenhum PMID é citado pela IA de memória — todo PMID vem de abstract colado
     nesta sessão ou verificado via G1 (esearch/esummary). PMID não verificado
     nesta sessão = não existe para o sistema."
  - "Query que retorna lote fora de escopo (termo genérico demais, população errada)
     é descartada e reformulada direto — sem registrar cada PMID individualmente.
     resultados_nao_triados/query_historico só entra quando tem valor real de
     decisão futura (query com escopo CERTO mas leitura incompleta; ou reformulação
     que evita repetir um erro específico). Registro não é objetivo — decisão rápida
     e correta é."

# ============================================
# BIBLIOTECA APROVADA — B1_NEUROINFLAMMATION / SM-02
# Status: 23 entradas aprovadas = 15 claims principais (.001-.015)
#         + 8 subclaims (.001b/c/d, .005b, .007b, .012b/c, .013b)
# Em andamento (sem desfecho formal): .017, .023, .028, .032
# Pendentes (não iniciados): .016, .018-.022, .024-.027, .029-.031, .033-.035 (16)
# Formato: Schema-Claim v1.2
# ============================================

claims_aprovados:

  - claim_id: B1.SM02.001
    version: 2
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: clinico
    statement: >
      IL-6 elevada em MDD vs. controles saudáveis. Transdiagnóstica
      (sem diferença entre transtornos psiquiátricos).
    especificidade: transdiagnostico
    nota_ressalva: "Efeito por sexo diverge entre estudos — ver .001b"
    moderadores: []
    fontes:
      - {pmid: 36893912, autor: "Zhang Y et al.", ano: 2023, nivel: principal,
         comparador: outros_transtornos_psiquiatricos,
         achado: "sem diferença significativa de IL-6 entre transtornos",
         verificado_nesta_conversa: sim}
      - {pmid: 39089535, autor: "Jarkas DA et al.", ano: 2024, nivel: principal,
         comparador: controles_saudaveis,
         achado: "d=0.51 mulheres (p=0.04); d=0.16 ns homens",
         verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.001b
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: contexto_mecanistico
    statement: >
      Direção do efeito de sexo na relação inflamação-depressão diverge
      entre estudos (mulheres: Jarkas; homens/início tardio: Vogelzangs).
    especificidade: especifico_depressao
    nota_ressalva: "Direção do efeito por sexo é inconsistente entre as duas fontes; moderadores IMC e classe de antidepressivo vêm de fonte única (Vogelzangs 2012), sem replicação registrada."
    moderadores:
      - variavel: IMC
        efeito: atenua
        regra_motor: "Associação PCR/IL-6-depressão em homens perde força após ajuste por IMC, mas PCR permanece significativa"
        fonte_pmid: 22832816
      - variavel: classe_antidepressivo
        efeito: inverte
        regra_motor: "ISRS associado a ↓IL-6; tricíclicos/tetracíclicos associados a ↑PCR"
        fonte_pmid: 22832816
    fontes:
      - {pmid: 39089535, comparador: controles_saudaveis, achado: "efeito em mulheres", verificado_nesta_conversa: sim}
      - {pmid: 22832816, autor: "Vogelzangs N et al.", ano: 2012, comparador: controles_saudaveis,
         achado: "efeito em homens, mais forte em início tardio (PCR d=0.32; IL-6 d=0.23)",
         verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.001c
    status: aprovado
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: clinico
    statement: "IL-1β elevada em MDD vs. transtorno bipolar (comparador: bipolar, não controle saudável)"
    especificidade: especifico_depressao
    moderadores: []
    fontes: [{pmid: 36893912, autor: "Zhang Y et al.", ano: 2023, nivel: principal, comparador: transtorno_bipolar, verificado_nesta_conversa: sim}]
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.001d
    status: aprovado
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: clinico
    statement: "IL-10 elevada em bipolar vs. MDD"
    especificidade: especifico_depressao
    moderadores: []
    fontes: [{pmid: 36893912, autor: "Zhang Y et al.", ano: 2023, nivel: principal, comparador: transtorno_bipolar, verificado_nesta_conversa: sim}]
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.002
    version: 4
    status: aprovado
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: clinico
    statement: >
      Prevalência de inflamação de baixo grau (PCR>3mg/L) em MDD: 27%
      (IC95% 21-34%). PCR>1mg/L: 58% (IC95% 47-69%). OR vs. controles
      pareados: 1.46 e 1.47. Robusto a origem da amostra, tratamento,
      idade, IMC, etnia.
    especificidade: especifico_depressao
    moderadores: []
    fontes:
      - {pmid: 31258105, autor: "Osimo EF et al.", ano: 2019, nivel: principal,
         comparador: controles_saudaveis, n: 13541, k: 37,
         achado: "27% PCR>3 (IC 21-34); 58% PCR>1 (IC 47-69); OR=1.46/1.47",
         verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.003
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: gap_pesquisa
    statement: "TNF-α associado a MDD (d=0.40, p=0.002), mas evidência incerta"
    nota_ressalva: "Heterogeneidade extensa entre estudos; efeito cumulativo permanece incerto"
    especificidade: especifico_depressao
    moderadores: []
    fontes: [{pmid: 26065825, autor: "Haapakoski R et al.", ano: 2015, comparador: controles_saudaveis, verificado_nesta_conversa: sim}]
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.004
    status: aprovado
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: clinico
    statement: >
      IL-1β NÃO difere entre MDD e controles saudáveis (d=-0.05, ns).
      Só discrimina MDD de transtorno bipolar (ver .001c).
    especificidade: especifico_depressao
    moderadores: []
    fontes:
      - {pmid: 26065825, comparador: controles_saudaveis, achado: "d=-0.05, p=0.86", verificado_nesta_conversa: sim}
    papel_geral: "Regra de uso: IL-1β não serve para detectar MDD isolado; serve para diferenciar MDD de bipolar"
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.005
    version: 1
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: clinico
    statement: >
      Transtornos de ansiedade (TAG, transtorno do pânico) apresentam
      elevação de marcadores inflamatórios periféricos vs. controles
      saudáveis. TAG: PCR d=0.38 (IC95% 0.06-0.69). Pânico: IL-6,
      IL-1β elevados (revisão qualitativa, sem metanálise).
    especificidade: especifico_ansiedade
    nota_ressalva: "Heterogeneidade alta (I²=75% na metanálise de TAG); efeito pequeno; restrito a PCR. Painel de pânico é revisão qualitativa, sem tamanho de efeito agrupado. Evidência pediátrica é limitada/inconclusiva, não confirma o mesmo padrão — ver .005b. TOC excluído do escopo (DSM-5 não classifica como transtorno de ansiedade)."
    moderadores: []
    fontes:
      - {pmid: 31326932, autor: "Costello H et al.", ano: 2019, nivel: principal,
         comparador: controles_saudaveis, n: 1188, k: 14,
         achado: "PCR d=0.38 (IC95% 0.06-0.69, I²=75%); TNF-α e IFN-γ elevados em ≥2 estudos (contagem de estudos, não efeito agrupado)",
         verificado_nesta_conversa: sim}
      - {pmid: 29241050, autor: "Quagliato LA, Nardi AE", ano: 2018, nivel: corroborante,
         comparador: controles_saudaveis,
         achado: "IL-6, IL-1β, IL-5 elevados (revisão sistemática qualitativa, 11 estudos, sem metanálise); IL-2/IL-12/IFN-γ conflitantes",
         verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.005b
    tipo: subclaim
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: contexto_mecanistico
    statement: >
      Evidência disponível não confirma, em população pediátrica/
      adolescente, a mesma elevação inflamatória observada em
      ansiedade adulta (.005) — metanálise combinada com significância
      limítrofe, sem diferença significativa em marcadores individuais.
    especificidade: especifico_ansiedade
    nota_ressalva: "Achados classificados como provisórios pelos próprios autores (k=9, heterogeneidade alta, amostras pequenas, sem controle de confundidores). Não é comparação estatística direta adulto-vs-criança — estudo pediátrico isolado, não teste de interação com .005."
    moderadores:
      - variavel: faixa_etaria
        efeito: atenua
        regra_motor: "SE paciente < 18 anos → reduzir confiança na extrapolação direta de .005, mas não concluir ausência de inflamação nem bloquear investigação de outros mecanismos"
        fonte_pmid: 33200498
    fontes:
      - {pmid: 33200498, autor: "Parsons C et al.", ano: 2021, nivel: principal,
         comparador: controles_saudaveis, k: 9,
         achado: "metanálise combinada (16 citocinas + PCR) com significância limítrofe; sem diferença significativa em marcadores individuais",
         papel: "Não estabelece comparação direta com adultos; achado próprio classificado como provisório pelos autores",
         verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.006
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: gap_pesquisa
    statement: >
      Depressão, ansiedade e TEPT estão individualmente associados a
      resposta inflamatória periférica, controlando por comorbidades
      inflamatórias conhecidas — mas a magnitude/perfil da resposta
      difere entre os transtornos: evidência para depressão é mais
      estabelecida, para ansiedade é preliminar.
    especificidade: transdiagnostico
    nota_ressalva: "Achado é qualitativo (direção), sem efeito numérico por transtorno no abstract disponível. Evidência de ansiedade e TEPT é descrita pelos próprios autores como preliminar/limitada — não confirma isoladamente neuroinflamação na ansiedade."
    moderadores: []
    fontes:
      - {pmid: 37931509, autor: "Kuring JK et al.", ano: 2023, nivel: corroborante,
         comparador: controles_sem_comorbidades_inflamatorias_conhecidas, k: 64,
         achado: "Depressão associada a resposta inflamatória (evidência estabelecida); ansiedade e TEPT também associados, evidência preliminar; resposta específica difere entre os 3 transtornos",
         verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.007
    status: aprovado
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: clinico
    statement: >
      Apenas um subgrupo (~1/4) de pacientes com MDD apresenta
      inflamação de baixo grau mensurável (PCR>3), não a totalidade.
    especificidade: especifico_depressao
    moderadores: []
    fontes:
      - {pmid: 31258105, papel: prevalencia_nucleo, comparador: controles_saudaveis, verificado_nesta_conversa: sim}
      - {pmid: 39615605, comparador: controles_saudaveis,
         papel: "PCR+AES combinados mostram gradiente dose-resposta imunometabólico",
         verificado_nesta_conversa: sim}
    fontes_exploratorias:
      - {pmid: 32696276, nivel: exploratorio, achado: "~20% subgrupo via IgM, sem controle saudável"}
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.007b
    status: aprovado
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: clinico
    statement: >
      Maus-tratos na infância identifica subgrupo de MDD com PCR
      elevada (RR=2.07, IC95% 1.23-3.47) vs. MDD sem maus-tratos
      (RR=1.40, ns). Moderador de .007.
    especificidade: especifico_depressao
    moderadores:
      - variavel: historico_maus_tratos_infancia
        efeito: amplifica
        regra_motor: "SE historico_maus_tratos_infancia=true → aumentar peso da hipótese de subgrupo inflamatório (.007), citando RR=2.07"
        fonte_pmid: 18391129
    fontes: [{pmid: 18391129, autor: "Danese A et al.", ano: 2008, comparador: controles_saudaveis, n: 1000, verificado_nesta_conversa: sim}]
    referencia_cruzada: [mecanismo_B12_neurobiologia_trauma]
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.008
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: clinico
    statement: >
      NLR (razão neutrófilos/linfócitos) elevada em MDD vs. controles
      saudáveis.
    especificidade: especifico_depressao
    nota_ressalva: "Heterogeneidade alta em pelo menos uma das metanálises (I²=73%); faixa de efeito varia consideravelmente entre as duas fontes principais (SMD 0.24 a 0.73) — direção consistente, magnitude não."
    moderadores:
      - variavel: comportamento_suicida
        efeito: amplifica
        regra_motor: "SE comportamento/ideação suicida presente → NLR mais elevado que em MDD geral (DMP até 1.02 vs. controles, contra 0.24-0.73 do MDD geral) — mesmo padrão de amplificação por suicidalidade já visto em .011 (LCR)"
        fonte_pmid: 38802507
    fontes:
      - {pmid: 41481888, ano: 2025, nivel: principal, comparador: controles_saudaveis, k: 37, n: 88019,
         achado: "OR=1.57 (IC95% 1.28-1.93) presença de NLR elevado; SMD=0.73 (IC95% 0.51-0.94) nível contínuo; NLR elevado também associado a maior risco de suicídio (OR=1.56)",
         verificado_nesta_conversa: sim}
      - {pmid: 36517638, ano: 2023, nivel: principal, comparador: controles_saudaveis, k: 104,
         achado: "NLR: SMD=0.24 (IC95% 0.06-0.42, I²=73%, 11 estudos); leucócitos totais SMD=0.46, neutrófilos SMD=0.52, monócitos SMD=0.32 — perfil imune mais amplo além de NLR isolado",
         verificado_nesta_conversa: sim}
      - {pmid: 40856326, ano: 2025, nivel: corroborante, comparador: controles_saudaveis,
         achado: "17/22 estudos (revisão sistemática qualitativa, sem metanálise) associam NLR elevado a fadiga, comprometimento cognitivo, inflamação crônica",
         verificado_nesta_conversa: sim}
    fontes_exploratorias:
      - {pmid: 38802507, achado: "NLR SMD=0.695 em ideação/comportamento suicida vs. controles; leucócitos e neutrófilos também elevados, k=19 estudos em metanálise", papel: "Base do moderador de comportamento suicida", verificado_nesta_conversa: sim}
      - {pmid: 40345445, achado: "NLR em MDD+comportamento suicida: DMP=0.34 vs. MDD sem, DMP=1.02 vs. controles saudáveis; k=10", papel: "Corrobora gradiente de amplificação por suicidalidade", verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.009
    status: aprovado
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: clinico
    statement: >
      IL-6 e proteína total elevadas no LCR de MDD vs. controles
      saudáveis, com baixa heterogeneidade entre estudos.
    especificidade: especifico_depressao
    moderadores: []
    fontes:
      - {pmid: 35442429, autor: "Mousten IV et al.", ano: 2022, nivel: principal,
         comparador: controles_saudaveis, k: 97,
         achado: "IL-6 no LCR: 7 estudos, DMP 0.35 (IC95% 0.12-0.59, I²=16%); proteína total no LCR: 5 estudos, DMP 0.53 (IC95% 0.35-0.72, I²=0%)",
         verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.010
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: contexto_mecanistico
    statement: >
      Marcadores inflamatórios no LCR e em PET (TSPO) não se
      correlacionam com os marcadores periféricos correspondentes em
      MDD — compartimento central e periférico não são intercambiáveis.
    especificidade: especifico_depressao
    nota_ressalva: "Achado de não-correlação é síntese qualitativa da revisão; abstract não reporta coeficiente de correlação próprio para esse ponto especificamente."
    moderadores: []
    fontes:
      - {pmid: 31195092, autor: "Enache D, Pariante CM, Mondelli V", ano: 2019, nivel: principal,
         comparador: controles_saudaveis, k: 69,
         achado: "Anormalidades em marcadores de LCR e PET não se correlacionaram com os marcadores periféricos correspondentes",
         verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.011
    version: 4
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: contexto_mecanistico
    statement: >
      Em indivíduos com comportamento/tentativa de suicídio, QUIN está
      elevado no LCR (associado a IL-6 e a gravidade da intenção suicida),
      com razão PIC/QUIN reduzida e desregulação persistente por >2 anos.
      IL-6 também elevada de forma independente, com gradiente por
      violência do método. Marcadores de permeabilidade de barreira
      hematoencefálica (ácido hialurônico, MMP9) também alterados no LCR
      vs. controles saudáveis.
    especificidade: transdiagnostico
    nota_ressalva: >
      Seis das fontes (27483383, 25124710, 19268915, 23299933, 26796235,
      41388730) compartilham autores do mesmo grupo de pesquisa (Erhardt S,
      Brundin L, Lindqvist D, Träskman-Bendz L — Lund, Suécia), sugerindo
      possível sobreposição de coorte/biobanco ao longo de múltiplas
      publicações — reduz a independência real entre as "replicações" e
      não deve ser lido como confirmação por múltiplos grupos
      independentes. População definida por comportamento/tentativa de
      suicídio (MADRS, Escala de Intenção Suicida, DSM-IV), não por
      diagnóstico MDD estrito e exclusivo — por essa razão, o claim
      também serve de âncora para a futura Biblioteca de Conhecimento de
      Cenários (cenario_E99_urgencias_psiquiatricas), não só para B1.
      Resultado para KYNA é inconsistente entre estudos: sem diferença em
      corte transversal (23299933) vs. redução ao longo do tempo em
      desenho longitudinal (25124710) — QUIN é o achado mais consistente,
      KYNA não. Em 27483383, achado central é razão PIC/QUIN, com
      elevação direta de QUIN restrita a subgrupo genético ACMSD. Em
      26796235, distribuição por sexo desigual entre grupos.
    moderadores:
      - variavel: genotipo_ACMSD_rs2121337
        efeito: amplifica
        regra_motor: "Presença do alelo C minoritário associada a maior QUIN no LCR"
        fonte_pmid: "27483383"
      - variavel: metodo_violento_tentativa
        efeito: amplifica
        regra_motor: "Tentativas violentas apresentam níveis mais elevados de IL-6 no LCR"
        fonte_pmid: "19268915"
      - variavel: tempo_desde_tentativa
        efeito: atenua
        regra_motor: "QUIN no LCR diminui significativamente em reavaliação <6 meses após a tentativa — achado é mais robusto no episódio agudo"
        fonte_pmid: "23299933"
    fontes:
      - {pmid: "27483383", autor: "Brundin L et al.", ano: 2016, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 137,
         achado: "Razão PIC/QUIN reduzida no LCR (P<0,001); persistência >2 anos; SNP rs2121337 associado a aumento de QUIN no LCR",
         papel: "Desregulação PIC/QUIN, componente genético", verificado_nesta_conversa: sim}
      - {pmid: "25124710", autor: "Bay-Richter C et al.", ano: 2015, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 30,
         achado: "QUIN aumentado e KYNA diminuído ao longo do tempo; IL-6 elevada associada a sintomas suicidas mais graves",
         papel: "Desregulação longitudinal", verificado_nesta_conversa: sim}
      - {pmid: "19268915", autor: "Lindqvist D, Brundin L et al.", ano: 2009, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 110,
         achado: "IL-6 no LCR elevada vs. controles; maior em tentativas violentas; correlação com MADRS; sem associação plasma-LCR",
         papel: "Elevação de IL-6, gradiente de gravidade", verificado_nesta_conversa: sim}
      - {pmid: "23299933", autor: "Erhardt S, Brundin L et al.", ano: 2013, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 64,
         achado: "QUIN elevado no LCR (p<0,001), KYNA sem diferença; QUIN associado a IL-6 no LCR e à Escala de Intenção Suicida; QUIN diminuiu em reavaliação <6 meses; amostra não medicada",
         papel: "Suporte mais direto e específico para elevação de QUIN; controla confundidor de medicação; liga QUIN a NMDA (B5) e IL-6",
         verificado_nesta_conversa: sim}
      - {pmid: "26796235", autor: "Ventorp F et al.", ano: 2016, nivel: corroborante,
         comparador: controles_saudaveis, especie: humano, n: 139,
         achado: "HA elevado (p=0,003) e MMP9 elevado (p=0,004) no LCR; HA correlaciona com permeabilidade de BHE",
         papel: "Amplia para permeabilidade de BHE/ativação glial", verificado_nesta_conversa: sim}
    fontes_exploratorias:
      - {pmid: "41388730", achado: "Sem diferença significativa de Galectina-3 entre grupos; correlação plasma-LCR forte (r=0,77, p<0,001, n=22)",
         papel: "Achado negativo pra Gal-3 como marcador — mas confirma que ALGUNS marcadores centrais correlacionam bem com plasma, nuance útil pra .010",
         verificado_nesta_conversa: sim}
      - {pmid: "28448609", achado: "Nenhum autoanticorpo de encefalite autoimune detectado no LCR (n=29, sem comparador)",
         papel: "Delimita hipótese alternativa", verificado_nesta_conversa: sim}
    referencia_cruzada: [mecanismo_B4_deficiencias_monoaminas, mecanismo_B5_gaba_glutamato, cenario_E99_urgencias_psiquiatricas]
    usado_em_biblioteca: nao
  - claim_id: B1.SM02.012
    version: 1
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: gap_pesquisa
    statement: >
      S100B no LCR não difere de forma consistente entre MDD e
      controles saudáveis. Estudos caso-controle diretos em MDD
      encontram ausência de diferença significativa, enquanto revisão
      sistemática caracteriza a evidência de S100B no LCR em transtornos
      afetivos como escassa e inconsistente. O conjunto disponível não
      sustenta S100B como marcador glial de LCR consistentemente elevado
      em MDD. Nenhum dado suficiente foi identificado nesta busca para
      estabelecer uma direção consistente de YKL-40/CHI3L1 no LCR em MDD.
      Ver subclaims .012b (sTREM2) e .012c (GFAP).
    especificidade: especifico_depressao
    nota_ressalva: >
      A revisão sistemática de Kroksmark & Vinberg (2018, n=1292,
      transtornos afetivos mistos entre depressão e transtorno bipolar)
      descreve o S100B sérico como mais consistentemente elevado, mas
      caracteriza especificamente a evidência no LCR como baseada em
      poucos estudos e com resultados inconsistentes. O estudo de
      Schmidt et al. (2015, n=63) não encontrou diferença significativa
      de S100B no LCR entre MDD e controles saudáveis, apesar de encontrar
      NSE significativamente elevado no mesmo desenho. O estudo de
      Heidrich et al. (2021, n=141) também não encontrou diferença
      significativa de S100B no LCR entre depressão unipolar e seu grupo
      comparador, embora esse comparador fosse composto por pacientes com
      hipertensão intracraniana idiopática, e não controles saudáveis.
      Portanto, os achados diretos são compatíveis com ausência de
      elevação consistente, mas a heterogeneidade dos desenhos e dos
      comparadores impede tratar o resultado como evidência definitiva
      de ausência de alteração. PMID 32439851 fornece evidência
      exploratória de associação entre S100B no LCR e sintomas de sono
      dentro do grupo MDD, mas não demonstra diferença de nível absoluto
      entre MDD e controles. PMID 20132991 mediu GFAp e NFL em mulheres
      idosas com depressão, mas não deve ser usado para inferir resultado
      nulo de GFAP; o abstract relata especificamente elevação de NFL.
      Ver .012c para GFAP.
    moderadores: []
    fontes:
      - {pmid: "25264292", autor: "Schmidt FM et al.", ano: 2015,
         nivel: principal,
         comparador: controles_saudaveis,
         especie: humano,
         n: 63,
         achado: "S100B no LCR sem diferença significativa entre MDD (n=31) e controles (n=32), 1,12 vs 0,97 ng/ml; NSE elevado no mesmo desenho (11,73 vs 6,17 ng/ml, p=0,004, d=1,23)",
         papel: "Achado nulo direto para S100B em MDD; fornece o caso-controle direto mais limpo do lote e mostra contraste com marcador neuronal NSE",
         verificado_nesta_conversa: sim}
      - {pmid: "29764272", autor: "Kroksmark H, Vinberg M", ano: 2018,
         nivel: principal,
         comparador: controles_saudaveis,
         especie: humano,
         n: 1292,
         k: 20,
         achado: "Revisão sistemática de S100B em transtornos afetivos; S100B sérico mais consistentemente elevado, enquanto os estudos de S100B no LCR são poucos e apresentam resultados inconsistentes",
         papel: "Maior nível de evidência do conjunto; documenta especificamente a lacuna e inconsistência da evidência de LCR",
         verificado_nesta_conversa: sim}
      - {pmid: "34021122", autor: "Heidrich CM et al.", ano: 2021,
         nivel: principal,
         comparador: controles_com_hipertensao_intracraniana_idiopatica,
         especie: humano,
         n: 141,
         achado: "S100B no LCR sem diferença significativa entre depressão unipolar e grupo comparador com HII (1,06 vs 1,17 ng/ml, p=0,385)",
         papel: "Segundo achado direto de ausência de diferença para S100B; limitado pelo comparador não saudável",
         verificado_nesta_conversa: sim}
    fontes_exploratorias:
      - {pmid: "32439851",
         achado: "S100B no LCR apresentou correlação com subescala de sono do HAM-D dentro do grupo MDD (n=104), sem diferença de nível absoluto MDD-vs-controle relatada para S100B",
         papel: "Associação com sintoma, não comparador exigido pelo claim",
         verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao
  - claim_id: B1.SM02.012b
    tipo: subclaim
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: contexto_mecanistico
    statement: >
      sTREM2 no LCR apresenta sinal de redução ou associação inversa
      com sintomas depressivos em populações idosas/geriátricas,
      incluindo redução em MDD de início tardio e associação negativa
      com sintomas depressivos em uma coorte independente de idosos.
      O achado sugere alteração da atividade fagocítica microglial,
      mas não estabelece sTREM2 reduzido como marcador de MDD em
      população geral.
    especificidade: especifico_depressao
    nota_ressalva: >
      PMID 38795783 encontrou sTREM2 significativamente reduzido no
      LCR de pacientes com MDD tardia em comparação com controles idosos
      cognitivamente íntegros (n=27 vs 19), mas a diferença deixou de
      ser significativa no seguimento de 3 anos. PMID 34246952, da mesma
      equipe e provavelmente da mesma coorte, não encontrou diferença
      significativa no basal e encontrou evidência bayesiana moderada
      de redução somente no seguimento de 3 anos (fator de Bayes=7,9).
      Portanto, esses dois estudos não devem ser tratados como
      replicações independentes e apresentam padrão temporal
      inconsistente. PMID 39044521 fornece evidência independente em
      amostra muito maior de idosos da coorte ADNI (n=1017), encontrando
      associação negativa entre sTREM2 basal no LCR e escore de sintomas
      depressivos GDS-15 (β=-0,21, p=0,022), após ajuste para múltiplos
      fatores clínicos e genéticos. Entretanto, esse estudo avalia
      sintomas depressivos de forma dimensional e não comparação
      categórica MDD-vs-controles, além de ocorrer em população de
      pesquisa relacionada à doença de Alzheimer. Assim, a evidência
      converge quanto à direção geral de menor sTREM2 associada a maior
      carga depressiva em idosos, mas permanece insuficiente para
      generalização a MDD adulto em geral. sTREM2 também não deve ser
      interpretado como citocina inflamatória clássica: trata-se de
      marcador relacionado à atividade fagocítica/microglial.
    moderadores: []
    fontes:
      - {pmid: "38795783", autor: "Reichert Plaska C et al.", ano: 2024,
         nivel: principal,
         comparador: controles_saudaveis,
         especie: humano,
         n: 46,
         achado: "sTREM2 no LCR significativamente reduzido em MDD tardia vs. controles idosos (n=27 vs 19); redução não significativa no seguimento de 3 anos",
         papel: "Achado direto mais forte para redução de sTREM2 em MDD tardia; população idosa cognitivamente íntegra",
         verificado_nesta_conversa: sim}
      - {pmid: "34246952", autor: "Teipel S et al.", ano: 2021,
         nivel: corroborante,
         comparador: controles_saudaveis,
         especie: humano,
         n: 49,
         achado: "sTREM2 basal no LCR sem diferença significativa entre MDD e controles; evidência bayesiana moderada de redução somente no seguimento de 3 anos (fator de Bayes=7,9)",
         papel: "Fonte da mesma equipe/coorte de 38795783; demonstra que a direção não é robusta transversalmente e apresenta padrão temporal diferente",
         verificado_nesta_conversa: sim}
      - {pmid: "39044521", autor: "Wang Y et al.", ano: 2024,
         nivel: corroborante,
         comparador: correlacao_continua_dentro_coorte_gds15,
         especie: humano,
         n: 1017,
         achado: "sTREM2 basal no LCR correlacionou-se negativamente com escore GDS-15 (β=-0,21, p=0,022), com ajuste para idade, sexo, raça, escolaridade, APOE ε4, variante TREM2, estado civil, tabagismo e status cognitivo; seguimento médio de 4,65 anos",
         papel: "Corrobora a direção em coorte grande e independente (ADNI), mas é evidência dimensional de sintomas depressivos e não comparação categórica MDD-vs-controles",
         verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao
  - claim_id: B1.SM02.012c
    tipo: subclaim
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: gap_pesquisa
    statement: >
      Evidência para GFAP no LCR em MDD é insuficiente e potencialmente
      contraditória: PMID 34021122 encontrou elevação forte de GFAP em
      depressão unipolar, mas utilizou controles com hipertensão
      intracraniana idiopática; PMID 20132991 mediu GFAp em mulheres
      idosas com depressão, porém o abstract não relata diferença
      significativa de GFAp entre grupos. Portanto, não há evidência
      suficiente para estabelecer uma direção consistente do GFAP no
      LCR em MDD.
    especificidade: especifico_depressao
    nota_ressalva: >
      PMID 34021122 (n=141) encontrou GFAP significativamente elevado
      em depressão unipolar vs. controles com hipertensão intracraniana
      idiopática (733,22 vs. 245,56 pg/ml, p<0,001), mantido em
      subanálise pareada por idade/sexo. Entretanto, o comparador não
      é composto por controles saudáveis e o desenho é retrospectivo,
      limitando a interpretação do achado como evidência específica
      de MDD. PMID 20132991 avaliou GFAp em 78 mulheres idosas, das
      quais 11 apresentavam TDM; o abstract destaca elevação de NFL,
      mas não relata diferença significativa para GFAp. Assim, esse
      estudo não deve ser usado para afirmar que GFAP é nulo no MDD.
      A direção do GFAP no LCR permanece não resolvida nesta busca.
    moderadores: []
    fontes:
      - {pmid: "34021122", autor: "Heidrich CM et al.", ano: 2021,
         nivel: principal,
         comparador: controles_com_hipertensao_intracraniana_idiopatica,
         especie: humano, n: 141,
         achado: "GFAP no LCR elevado em depressão unipolar vs. controles com HII (733,22 vs 245,56 pg/ml, p<0,001); efeito mantido em subanálise pareada por idade/sexo",
         papel: "Evidência positiva para GFAP, porém com comparador metodologicamente inadequado para sustentar especificidade de MDD",
         verificado_nesta_conversa: sim}
      - {pmid: "20132991", autor: "Gudmundsson P et al.", ano: 2010,
         nivel: corroborante,
         comparador: mulheres_idosas_sem_depressao,
         especie: humano, n: 78,
         achado: "GFAp e NFL foram medidos no LCR; o abstract relata NFL elevado em TDM, mas não apresenta diferença significativa para GFAp",
         papel: "Evidência complementar; não permite classificar GFAP como elevado ou nulo",
         verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao
  - claim_id: B1.SM02.013
    version: 1
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: clinico
    statement: >
      MDD apresenta alteração de proteínas do complemento tanto no LCR
      quanto no soro/plasma vs. controles saudáveis: C5 elevado no LCR;
      C3, C3a, CFH, C1q (efeito pequeno, uma de duas fontes), C4, fator
      B e properdina elevados no soro/plasma. Redução de volume de
      substância cinzenta em córtex orbitofrontal medial e cíngulo
      médio correlaciona com níveis de complemento.
    especificidade: especifico_depressao
    nota_ressalva: >
      C1q tem resultado contraditório entre fontes séricas: Luo et al.
      2022 (n=94, sem medicação) não encontra diferença; Yao & Li 2020
      (n=319) encontra elevação com efeito pequeno (r=0,239) —
      compatível com diferença de poder estatístico. Uma terceira fonte
      sobre C1q (PMID 36156342, MDD vs. subtipos de bipolar) foi
      rejeitada por contradição interna irresolúvel entre Resultados e
      Conclusão do próprio abstract — confirmado no texto original em
      inglês, não é erro de tradução — não usada em nenhuma direção.
      CFH agora tem 2 fontes convergentes (Wang et al. 2022, n=215,
      população geral; Shin et al. 2019, n=152, população geriátrica) —
      reduz a restrição etária que existia com fonte única. PMID
      29454970 (C5, LCR) compartilha equipe de pesquisa com fontes já
      usadas em .012 (Hidese S, Hattori K, Miyakawa T, Ota M, Kunugi H
      — NCNP Tóquio) — mesmo padrão de biobanco único já visto em .011
      e .012b.
    moderadores:
      - variavel: presenca_anedonia
        efeito: amplifica
        regra_motor: "SE anedonia presente no quadro de MDD → CFH tende a estar mais elevado que em MDD sem anedonia (fonte única, não replicado)"
        fonte_pmid: "33794316"
    fontes:
      - {pmid: "29454970", autor: "Ishii T et al.", ano: 2018, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 206,
         achado: "C5 no LCR significativamente aumentado em MDD vs. controles (p<0,001); taxa de 'nível anormalmente alto' de C5 aumentada (p<0,01)",
         papel: "Único achado de LCR do lote; ver nota_ressalva sobre biobanco NCNP", verificado_nesta_conversa: sim}
      - {pmid: "36447174", autor: "Luo X et al.", ano: 2022, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 94,
         achado: "C3 e C3a plasmáticos maiores em MDD sem medicação vs. controles; C1q e PCR sem diferença",
         papel: "Amostra medication-free", verificado_nesta_conversa: sim}
      - {pmid: "32272297", autor: "Yao Q, Li Y", ano: 2020, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 319,
         achado: "C1q sérico maior em MDD (p<0,0001, efeito pequeno r=0,239); correlaciona com HAMD-24 e log(hsPCR)",
         papel: "Contradiz 36447174 pra C1q — ver nota_ressalva", verificado_nesta_conversa: sim}
      - {pmid: "33794316", autor: "Tang W et al.", ano: 2021, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 215,
         achado: "CFH, IL-10 e TNF-α plasmáticos maiores em MDD sem tratamento prévio vs. controles; dentro do MDD, subgrupo com anedonia tem CFH e IL-6 mais altos que subgrupo sem anedonia; CFH associado especificamente à gravidade de anedonia (SHAPS), não à gravidade geral (HAMD-17)",
         papel: "Segunda fonte de CFH, população geral não-geriátrica", verificado_nesta_conversa: sim}
      - {pmid: "29798743", autor: "Shin C et al.", ano: 2019, nivel: corroborante,
         comparador: controles_saudaveis, especie: humano, n: 152,
         achado: "CFH plasmático maior em MDD (339,67±66,23) vs. comparação (289,51±21,16), p<0,001; sem correlação com escore GDS dentro do grupo deprimido",
         papel: "População geriátrica restrita; números reconciliados via título/conclusão do artigo", verificado_nesta_conversa: sim}
      - {pmid: "36285542", autor: "Yu H, Ni P, Tian Y et al.", ano: 2022, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 88,
         achado: "C1q, C4, fator B, fator H e properdina maiores em MDD+BD combinados vs. controles; volume de substância cinzenta em COFm e cíngulo médio menor em ambos grupos; C1q/fator H/properdina correlacionam negativamente com volume em COFm",
         papel: "Sustenta referencia_cruzada com B3; ver .013b", verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao
    referencia_cruzada: [mecanismo_B3_neuroplasticidade]

  - claim_id: B1.SM02.013b
    tipo: subclaim
    status: aprovado
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: clinico
    statement: >
      Complemento C3, C4 e fator H estão mais elevados em transtorno
      bipolar do que em MDD, no mesmo desenho — diferencia os dois
      transtornos, apesar de ambos mostrarem elevação de C1q/C4/fator
      B/fator H/properdina vs. controles saudáveis.
    especificidade: especifico_depressao
    moderadores: []
    fontes:
      - {pmid: "36285542", ano: 2022, nivel: principal, comparador: transtorno_bipolar,
         especie: humano, n: 87,
         achado: "C3, C4 e fator H significativamente mais altos em BD do que em MDD, no mesmo desenho/amostra",
         papel: "Único estudo com esse comparador — sem replicação ainda, mesma ressalva de fonte única já vista em .001c/.001d",
         verificado_nesta_conversa: sim}
    usado_em_biblioteca: nao
  - claim_id: B1.SM02.015
    version: 2
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: contexto_mecanistico
    statement: >
      TSPO elevado em MDD (~18% de aumento generalizado vs. controles).
      Em metanálise formal (k=8 estudos, n=402), o córtex cingulado
      anterior (ACC) apresenta o maior tamanho de efeito estimado entre 5
      regiões testadas (g=0,60), seguido de perto pelo hipocampo (g=0,54,
      IC sobreposto ao do ACC) — não estatisticamente distinguíveis entre
      si nesta metanálise. Meta-análise independente de estudos PET
      (Enache 2019) também encontrou o ACC com o maior tamanho de efeito
      estimado entre as regiões passíveis de pooling (SMD=0,78), embora
      com córtex temporal como comparador regional. Em desenhos de
      comparação inter-regional direta (sem teste de hipocampo), dois
      estudos independentes observaram o ACC como a única região
      significativa frente a PFC e ínsula. O estudo seminal do campo
      (Setiawan 2015, n=40) encontra elevação significativa e comparável
      nas 3 regiões testadas.
    especificidade: especifico_depressao
    nota_ressalva: >
      A metanálise de Eggerstorfer 2022 fortalece a elevação geral de
      TSPO e identifica o ACC como maior efeito estimado entre as regiões
      analisadas, mas são metanálises paralelas por região, não teste
      estatístico direto de "ACC > outras regiões" — os ICs do ACC e do
      hipocampo se sobrepõem. Enache 2019 fornece corroboração
      meta-analítica independente, mas seu pooling regional foi restrito
      ao ACC e córtex temporal, conforme disponibilidade de dados, não
      reproduzindo as comparações diretas com PFC e ínsula. Portanto,
      Enache confirma o ACC como maior efeito entre as regiões agrupáveis,
      mas não constitui réplica do mesmo desenho inter-regional.
      O hipocampo nunca foi testado nos desenhos de comparação
      inter-regional direta de Holmes e Schubert, portanto não se sabe se
      o ACC supera o hipocampo em um desenho pareado. O padrão "ACC como
      única região significativa frente a PFC e ínsula" foi observado em
      dois estudos independentes, mas o estudo mais citado do campo
      (Setiawan 2015) permanece uma exceção importante: encontrou PFC,
      ACC e ínsula elevados de forma comparável, sem isolar o ACC como
      região de maior magnitude. Além disso, a amostra deprimida do
      BIODEP/Schubert 2021 foi definida por HDRS>13, e não por diagnóstico
      confirmado de MDD/episódio depressivo em curso para 100% dos
      participantes; 65% eram resistentes ao tratamento. Assim, essa
      amostra é mais heterogênea que a de Holmes 2018. Amostras pequenas
      nos estudos individuais (Holmes n=27; Setiawan n=40) e fontes
      corroborantes restritas a subpopulações (TRD em Cakmak; terceira
      idade em Su, n=5) limitam a generalização plena. Em conjunto, a
      evidência sustenta elevação de TSPO no MDD e fornece suporte
      consistente para envolvimento do ACC, mas não permite afirmar que
      o ACC seja definitivamente superior a todas as demais regiões.
    moderadores: []
    fontes:
      - {pmid: "36226319", autor: "Eggerstorfer B et al.", ano: 2022, nivel: principal,
         comparador: controles_saudaveis, k: 8, n: 402,
         achado: "TSPO elevado em ACC (g=0.60, IC95% 0.36-0.84), hipocampo (g=0.54, IC95% 0.26-0.81), ínsula (g=0.43, IC95% 0.17-0.69), PFC (g=0.36, IC95% 0.14-0.59); temporal ns (g=0.39, IC95% -0.04-0.81). ~18% aumento generalizado. Sem associação com gravidade/idade/IMC/radioligante/status de tratamento nas 4 regiões significativas",
         papel: "Evidência quantitativa mais forte — mas teste paralelo por região, não comparação estatística direta entre regiões",
         verificado_nesta_conversa: sim}
      - {pmid: "31195092", autor: "Enache D et al.", ano: 2019, nivel: principal,
         comparador: controles_saudaveis, especie: humano,
         achado: "Meta-análise de estudos PET em MDD: TSPO elevado no ACC (SMD=0.78, IC95% 0.41-1.16) e córtex temporal (SMD=0.52, IC95% 0.19-0.85); entre as regiões passíveis de pooling, o ACC apresentou o maior tamanho de efeito estimado",
         papel: "Corroboração meta-analítica independente do padrão regional; pooling restrito às regiões com dados suficientes, com comparação regional distinta da de Holmes e Schubert (temporal, não PFC/ínsula), portanto não constitui teste direto de ACC > outras regiões",
         verificado_nesta_conversa: sim}
      - {pmid: "28939116", autor: "Holmes SE et al.", ano: 2018, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 27,
         achado: "TSPO maior em MDD vs controles apenas no ACC (d=0.95, p=0.022); PFC (d=0.38, p=0.342) e ínsula (d=0.29, p=0.466) não significativos",
         papel: "Comparação inter-regional direta no mesmo desenho; amostra não-medicada",
         verificado_nesta_conversa: sim}
      - {pmid: "33515765", autor: "Schubert JJ et al.", ano: 2021, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 76,
         achado: "ACC única região significativa (d=0.49, p=0.03); PFC (d=0.27) e ínsula (d=0.36) não significativos",
         papel: "Maior amostra entre fontes de comparação direta; replica padrão de Holmes 2018",
         verificado_nesta_conversa: sim}
      - {pmid: "25629589", autor: "Setiawan E et al.", ano: 2015, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 40,
         achado: "TSPO elevado em PFC (+26%)/ACC (+32%)/ínsula (+33%), as 3 regiões significativas; ACC não isolado como maior magnitude",
         papel: "Estudo seminal — fonte central da tensão do claim",
         verificado_nesta_conversa: sim}
      - {pmid: "35654450", autor: "Cakmak JD et al.", ano: 2022, nivel: corroborante,
         comparador: controles_saudaveis, especie: humano, n: 35,
         achado: "sgACC esquerdo elevado em MDD resistente a tratamento vs controles; sem comparação inter-regional no mesmo desenho",
         papel: "Corrobora subregião; população restrita a TRD",
         verificado_nesta_conversa: sim}
    fontes_exploratorias:
      - {pmid: "34153835", achado: "Revisão de 9 estudos: TSPO ↑ 'especialmente' em ACC, PFC, hipocampo, ínsula, sem hierarquia de magnitude", verificado_nesta_conversa: sim}
      - {pmid: "37543251", achado: "Meta-análise transdiagnóstica k=156: circuito corticolímbico (composto) ↑ em transtornos de humor; MDD não isolada como categoria própria", verificado_nesta_conversa: sim}
      - {pmid: "29496589", achado: "TSPO ↑ conjunto; preditor mais forte é duração da doença não tratada (p<0.0001), não região", papel: "Candidato a moderador de .014 (duração da doença), não suporte à especificidade regional", verificado_nesta_conversa: sim}
      - {pmid: "27758838", achado: "PK11195 ↑ incluindo cíngulo subgenual em depressão da terceira idade, n=5 casos", papel: "Amostra quase anedótica", verificado_nesta_conversa: sim}
    referencia_cruzada: []
    usado_em_biblioteca: nao

  - claim_id: B1.SM02.014
    version: 1
    status: aprovado_com_ressalva
    verification: verificado_nesta_conversa
    evidence_role: human_clinical
    uso: contexto_mecanistico
    statement: >
      Em indivíduos com MDD/MDE, estudos de PET indicam, em conjunto,
      maior ligação/disponibilidade cerebral de TSPO em comparação com
      controles saudáveis (~18% de aumento generalizado na meta-análise
      de 8 estudos). Não é elevação universal em todo MDD.
    especificidade: especifico_depressao
    nota_ressalva: >
      Base pequena: a meta-análise agrega apenas 8 estudos PET, com
      heterogeneidade de radioligante, parâmetro de ligação e amostra.
      Os 4 estudos primários listados abaixo estão entre os estudos que
      compõem essa meta-análise — não são replicação independente dela,
      e o achado negativo de Hannestad 2013 já está incorporado ao
      efeito agrupado. Existe resultado negativo direto (Hannestad 2013,
      n=20, depressão leve a moderada, pareamento por genótipo TSPO) e
      resultado que não atingiu o limiar corrigido de significância
      (Richards 2018). Efeito do status de medicação é discordante:
      Richards encontra elevação concentrada nos não medicados, enquanto
      a meta-análise não encontra relação com status de tratamento nas
      4 regiões significativas. TSPO não é marcador exclusivo de
      microglia ativada — limitação interpretativa tratada em .018.
      Não há dado de ansiedade neste claim (ver .019).
    forca_evidencia_afirmacao: media   # campo experimental — oficializar em Schema-Claim v1.3
    moderadores:
      - variavel: status_medicacao
        efeito: amplifica
        regra_motor: "SE paciente sem antidepressivo em curso → evidência de TSPO elevado é mais forte (análise exploratória, Richards 2018). NÃO tratar como moderador estabelecido: a meta-análise de 8 estudos não confirma relação com status de tratamento"
        fonte_pmid: "29971587"
    fontes:
      - {pmid: "36226319", autor: "Eggerstorfer B et al.", ano: 2022, nivel: principal,
         comparador: controles_saudaveis, especie: humano, k: 8, n: 402,
         achado: "TSPO elevado: ACC g=0,60 (IC95% 0,36-0,84); hipocampo g=0,54 (0,26-0,81); ínsula g=0,43 (0,17-0,69); PFC g=0,36 (0,14-0,59); córtex temporal g=0,39 (-0,04-0,81, IC cruza zero); ~18% de aumento generalizado; sem relação com gravidade, idade, IMC, radioligante ou status de tratamento nas 4 regiões significativas",
         papel: "Síntese de maior peso; engloba os 4 primários abaixo",
         fonte_texto: "PMC9549359 / Front Mol Neurosci 10.3389/fnmol.2022.981442",
         verificado_nesta_conversa: sim}
      - {pmid: "25629589", autor: "Setiawan E et al.", ano: 2015, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 40,
         achado: "TSPO VT ([18F]FEPPA) maior em todas as regiões: PFC +26%, ACC +32%, ínsula +33%; correlação com gravidade no ACC; pacientes sem medicação >=6 semanas",
         papel: "Estudo seminal do campo", verificado_nesta_conversa: sim}
      - {pmid: "28939116", autor: "Holmes SE et al.", ano: 2018, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 27,
         achado: "Multivariada p=0,005; ACC p=0,022 (d=0,95); PFC e ínsula não significativos; [11C]PK11195; amostra livre de medicação",
         papel: "Positivo, concentrado no ACC", verificado_nesta_conversa: sim}
      - {pmid: "29971587", autor: "Richards EM et al.", ano: 2018, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 48,
         achado: "sgPFC d=0,64 (p=0,038; IC95% 0,04-1,24) e ACC d=0,60 (p=0,049; IC95% 0,001-1,21), ambos abaixo do limiar corrigido alfa=0,025; exploratória: não medicados com maior ligação, medicados indistinguíveis dos controles",
         papel: "Favorável qualificado; base do moderador de medicação",
         fonte_texto: "PMC6029989 / EJNMMI Res 10.1186/s13550-018-0401-9",
         verificado_nesta_conversa: sim}
      - {pmid: "23850810", autor: "Hannestad J et al.", ano: 2013, nivel: principal,
         comparador: controles_saudaveis, especie: humano, n: 20,
         achado: "Sem diferença significativa de VT ([11C]PBR28, função de entrada arterial); 7 de 10 deprimidos com ligação MENOR que seus controles pareados por genótipo TSPO em todas as ROIs; depressão leve a moderada",
         papel: "Evidência contraditória direta — mantida na matriz, não descartada",
         fonte_texto: "PMC3899398 / Brain Behav Immun 10.1016/j.bbi.2013.06.010",
         verificado_nesta_conversa: sim}
    referencia_cruzada: []
    usado_em_biblioteca: nao

# ============================================
# LOG DE EXCLUSÃO (único, estilo PRISMA — vive só aqui)
# v1.7: chave duplicada unificada — 92 entradas únicas.
# Rejeição é SEMPRE por claim (origem_claim): PMID rejeitado para um
# claim pode ser reutilizado em outro se o achado for específico dele.
# ============================================
fontes_rejeitadas:
  - {pmid: 39938607, motivo: "sem controle saudável, desenho ECT", destino: SM-14}
  - {pmid: 34864233, motivo: "pré/pós fluoxetina, sem controle", destino: "INT_*"}
  - {pmid: "34999196", motivo: "abstract não menciona ideação suicida/suicídio (população exigida pelo claim ausente); achado central no LCR é sobre PIC (ácido picolínico), não QUIN (ácido quinolínico) — aumento de QUIN relatado é apenas plasmático, não central",
     origem_claim: "B1.SM02.011", data: "2026-08-04"}
  - {pmid: "33339712", motivo: "população transtorno bipolar — fora do disease_context", destino: "descartado"}
  - {pmid: "30696814", motivo: "população transtorno bipolar — fora do disease_context", destino: "descartado"}
  - {pmid: "32209024", motivo: "estudo de validação metodológica/bioanalítica, não comparação clínica de pacientes",
     origem_claim: "B1.SM02.011", data: "2026-08-04"}
  - {pmid: "31928628", motivo: "intervenção farmacológica (AINEs) — pertence a INT_*/SM-14, não a prova de existência basal",
     origem_claim: "B1.SM02.011", data: "2026-08-04", destino: SM-14}
  - {pmid: "42059933", motivo: "revisão narrativa, não systematic_review/meta-análise",
     origem_claim: "B1.SM02.011", data: "2026-08-04"}
  - {pmid: "36913003", motivo: "revisão narrativa, não systematic_review/meta-análise",
     origem_claim: "B1.SM02.011", data: "2026-08-04"}
  - {pmid: "25335166", motivo: "sem comparação com controles saudáveis para IL-6; correlação intragrupo com traço de personalidade",
     origem_claim: "B1.SM02.011", data: "2026-08-04", nota: "candidato a reforçar .010 — considerar se necessário"}
  - {pmid: "36265195", motivo: "série de 2 casos, sem grupo controle — viola exclusion_criteria do Protocolo de Escopo",
     origem_claim: "B1.SM02.012", data: "2026-08-04"}
  - {pmid: "20132991", motivo: "GFAP sem diferença significativa relatada; achado positivo (NFL) é marcador neuronal/axonal, não glial",
     origem_claim: "B1.SM02.012", data: "2026-08-04",
     escopo_rejeicao: "rejeitado APENAS para .012 (S100B); reutilizado em .012c (GFAP) conforme regra de reuso — ver pendencias_decisao_usuario"}
  - {pmid: "20031110", motivo: "não é revisão sistemática/metanálise (carta breve, sem abstract); tema é resposta a antidepressivo por IMC",
     origem_claim: "B1.SM02.032", data: "2026-08-12"}
  - {pmid: "23791710", motivo: "população Parkinson, fora do disease_context (ansiedade/depressão)",
     origem_claim: "B1.SM02.015", data: "2026-08-13"}
  - {pmid: "30918090", motivo: "enxaqueca com aura; 'depressão alastrante cortical' é fenômeno neurológico (Leão), falso cognato de TDM",
     origem_claim: "B1.SM02.015", data: "2026-08-13"}
  - {pmid: "24665088", motivo: "síndrome de fadiga crônica/EM, fora do disease_context",
     origem_claim: "B1.SM02.015", data: "2026-08-13"}
  - {pmid: "33610745", motivo: "atlas de receptor GABA-A/benzodiazepínico (flumazenil) em cérebro saudável — não é TSPO, não é população clínica",
     origem_claim: "B1.SM02.015", data: "2026-08-13"}
  - {pmid: "17606813", motivo: "transtorno de pânico + GABA-A/flumazenil — mecanismo é B5, não TSPO/B1",
     origem_claim: "B1.SM02.015", data: "2026-08-13"}
  - {pmid: "18838633", motivo: "idem — pânico + GABA-A/flumazenil; abstract afirma que achado NÃO é explicado por depressão comórbida",
     origem_claim: "B1.SM02.015", data: "2026-08-13"}
  - {pmid: "40199850", motivo: "GABA/glutamato via MRS (não PET-TSPO) + estimulação TBS (intervenção → SM-14); dupla incompatibilidade com B1/.015",
     origem_claim: "B1.SM02.015", data: "2026-08-13"}
  - {pmid: "34595576", motivo: "revisão narrativa (autoclassificada); mesmo padrão de exclusão de .011", origem_claim: "B1.SM02.023", data: "2026-08-13"}
  - {pmid: "27824355", motivo: "revisão narrativa — abstract afirma explicitamente não ser systematic review", origem_claim: "B1.SM02.023", data: "2026-08-13"}
  - {pmid: "24040799", motivo: "revisão narrativa, sem metodologia sistemática declarada", origem_claim: "B1.SM02.023", data: "2026-08-13"}
  - {pmid: "24317097", motivo: "fora de tema — case report forense de queda fatal por neurossífilis; também viola exclusion_criteria (case report sem grupo controle)", origem_claim: "B1.SM02.023", data: "2026-08-13"}
  - {pmid: "35886039", motivo: "falso positivo — 'depression' no texto refere-se a achatamento anatômico da parede brônquica em DPOC, não a transtorno depressivo", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "40360802", motivo: "foco primário é TOC; depressão aparece apenas como correlação genética entre múltiplas doenças", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "38548265", motivo: "foco primário é olho seco × depressão; não trata de escore de risco genético para vias inflamatórias", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "39837361", motivo: "foco primário é diabetes tipo 2 × depressão; sobreposição genética geral, não escore inflamatório específico", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "40460570", motivo: "foco primário é epilepsia; MDD é um entre vários transtornos correlacionados", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "40257431", motivo: "foco primário é PTSD × lúpus; depressão citada como comorbidade, não objeto do estudo", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "38858783", motivo: "foco primário é função renal; inclui população bipolar, fora do disorder scope", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "42114417", motivo: "foco é volume hipocampal em população geral; sem depressão como desfecho central no material disponível", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "42014469", motivo: "estratificação TSPO×suicídio reportada no braço de transtorno bipolar (achado: 'suicide or psychosis stratification revealing subgroup effects' em BD), não no braço MDD — fora do disease_context para esta claim específica. Conteúdo geral do braço MDD (TSPO elevado em regiões frontolímbicas) pode ter valor como contexto exploratório para .014, não avaliado aqui.", origem_claim: "B1.SM02.017", data: "2026-08-13"}
  - {pmid: "36156342", motivo: "contradição interna irresolúvel entre Resultados ('C1q maior em MDD que BD-II') e Conclusão ('C1q maior em BD-II que MDD') — confirmado no texto original em inglês, não é erro de tradução",
     origem_claim: "B1.SM02.013", data: "2026-08-14"}
  - {pmid: "38417323", motivo: "falso positivo temático — CTRP4 é adipocina da família C1q/TNF (homologia estrutural de domínio), não proteína funcional do sistema complemento",
     origem_claim: "B1.SM02.013", data: "2026-08-14"}
  - {pmid: "39149815", motivo: "compara MDD tratado × não-tratado, sem grupo controle saudável — resposta a tratamento, não existência basal",
     origem_claim: "B1.SM02.013", data: "2026-08-14", destino: SM-14}
  - {pmid: "37995499", motivo: "desenho e conclusão focados em monitorar resposta a medicação; sem número extraível para comparação basal não-tratado-vs-controle isolada",
     origem_claim: "B1.SM02.013", data: "2026-08-14", destino: SM-14}
  - {pmid: "39424870", motivo: "compara estados de remissão entre si (com/sem comprometimento residual), sem grupo saudável ativo — trajetória pós-tratamento, não existência basal",
     origem_claim: "B1.SM02.013", data: "2026-08-14", destino: SM-14}
  - {pmid: "39471050", motivo: "foco primário é dor neuropática; PRS para depressão é apenas variável secundária/covariável", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "42107849", motivo: "foco visível é comorbidade ansiedade-depressão; ligação com inflamação exigida pela query não aparece no trecho disponível", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "40775298", motivo: "foco primário é TDAH, não depressão", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "38199582", motivo: "foco primário é síndrome do intestino irritável", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "41572266", motivo: "PRS-depressão predizendo risco de asma; direção e construto diferentes do que .028 pede", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "42248509", motivo: "foco primário é cronotipo circadiano em comorbidade câncer-depressão", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "42105630", motivo: "população bipolar; domínio é metilação/epigenética, não GWAS/PRS", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "41319386", motivo: "genética do eixo glicocorticoide/HPA (mecanismo B2), não vias inflamatórias", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "40655020", motivo: "pré-print (bioRxiv) sem revisão por pares", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "32817414", motivo: "estudo multi-doença amplo; depressão é só um exemplo entre vários", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "33517931", motivo: "testa PCR fenotípica (nível medido), não escore de risco poligênico", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "36695075", motivo: "comorbidade genética alopecia areata × MDD, não escore de risco para vias inflamatórias", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "38782831", motivo: "foco primário é dificuldade auditiva relacionada à idade", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "17651905", motivo: "revisão sobre modelo animal de estresse pré-natal; mecanismo é eixo HPA (B2), não neuroinflamação (B1) — fora do escopo mesmo na trilha pré-clínica", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "38414355", motivo: "população é espectro de psicose; PRS é para esquizofrenia, não depressão", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "40931166", motivo: "população TEPT; PRS é para TEPT, não depressão", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "42225622", motivo: "comorbidade genética MDD × doença autoimune de tireoide (mais afim a B11)", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "41067425", motivo: "foco primário é síndrome da ardência bucal", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "40230026", motivo: "foco primário é doença hepática; depressão não é claramente o desfecho central", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "40630521", motivo: "pré-print superado pela versão publicada (PMID 41821624, já classificado como candidato G3)", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "35191176", motivo: "desfecho é tentativa de suicídio/ideação emergente durante tratamento — mais afim a SM-14 ou .011", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "36948466", motivo: "população oncológica (cabeça e pescoço); desfecho é sobrevida", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "37963865", motivo: "escore derivado de expressão placentária, não PRS convencional; toca aspirina como intervenção", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "36928559", motivo: "foco primário é fragilidade (aging)", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "37185864", motivo: "artigo retratado — Retratação em J Med Virol 2023;95(7):e28937", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "42536096", motivo: "foco primário é doença inflamatória intestinal e suas comorbidades", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "40343334", motivo: "doença neuroinflamatória não relacionada (mielopatia HTLV-1); também pré-print", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "35526724", motivo: "expressão de receptor de quimiocina (CCR4) é biomarcador fenotípico, não escore de risco genético", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "38555990", motivo: "inflamação-engajamento social moderada por depressão, não PRS predizendo diagnóstico/sintoma", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "30999091", motivo: "população TEPT pós-serviço militar; depressão é correlação genética secundária", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "39300237", motivo: "coagregação familiar com transtornos gastrointestinais, não vias inflamatórias especificamente", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "39072004", motivo: "revisão narrativa (não sistemática/meta-análise) sobre genética de comportamento suicida", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "34481527", motivo: "interação PCR × microbioma intestinal; construto de PRS não evidente no trecho", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "20190127", motivo: "sem construto genético/PRS evidente; estudo antigo sobre apoio social e asma", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "42267619", motivo: "foco primário é enxaqueca", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "39624483", motivo: "foco primário é fadiga/EBV; depressão e PRS são apenas covariáveis de ajuste", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "39766785", motivo: "subtipo de depressão periparto; ligação específica com vias inflamatórias não evidente no trecho", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "33243845", motivo: "foco primário é apneia obstrutiva do sono; depressão é uma comorbidade entre várias", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "34267256", motivo: "ligação familiar para transtornos psiquiátricos graves em geral; sem ligação com inflamação evidente", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "39606413", motivo: "pré-print superado pela versão publicada (PMID 42107849)", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "34488150", motivo: "estressores ocupacionais × biomarcadores inflamatórios; sem construto genético/PRS evidente", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "36457826", motivo: "interação microbioma intestinal × DII; construto de PRS não evidente no trecho", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "42369496", motivo: "pré-print; foco é desregulação metabólica periférica, não vias inflamatórias especificamente", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "42469454", motivo: "exposição primária é qualidade da dieta; genética/inflamação entram como modificadores de efeito", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "42417024", motivo: "assinatura de envelhecimento transcriptômico (expressão), não escore de risco genético", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "36777759", motivo: "falso positivo — farmacoterapia pós-cirúrgica em DII, sem conteúdo de depressão/genética", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "42006515", motivo: "artigo de hipótese/especulativo (autor único); PRS mencionado como predição futura, não dado relatado", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "39671776", motivo: "PRS é para esquizofrenia; desfecho é resposta de anticorpo a vacina", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "22541937", motivo: "modelo animal (ratos); mecanismo é eixo HPA/intestino (B2/B7), não neuroinflamação — 'PRS' no original é protocolo de estresse por contenção, não polygenic risk score", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "1535102", motivo: "falso positivo — imunoterapia oncológica (1992), sem conteúdo de depressão/genética", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "22184371", motivo: "falso positivo — imunoterapia em melanoma; depressão só como evento adverso", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "25456346", motivo: "vulnerabilidade/resiliência a estresse de combate (TEPT); PRS-depressão é preditor secundário", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "10999727", motivo: "falso positivo — ensaio oncológico com citocinas (2000), sem conteúdo de depressão/genética", origem_claim: "B1.SM02.028", data: "2026-08-13"}
  - {pmid: "23794217", motivo: "p-nominal com FDR por via, não significância genome-wide; N real ~3.643; metodologia de 2013 superada", origem_claim: "B1.SM02.028", data: "2026-08-13"}




# ============================================
# CLAIMS EM ANDAMENTO — busca iniciada, desfecho G3 não registrado
# Nada aqui é approved_claim. Números/achados abaixo são herdados de
# sessões anteriores (herdado_nao_verificado) e exigem texto colado
# na sessão de fechamento.
# ============================================
claims_em_andamento:
  - claim_id: B1.SM02.017
    status: em_busca
    registrado: "42014469 rejeitado (13/08, estratificação por suicídio só no braço bipolar)"
    achado_herdado: >
      Como Executar v1.7 registra que o texto completo de 33515765
      (Schubert 2021/BIODEP) contém comparação post-hoc MDD com vs. sem
      ideação suicida com resultado NULO, e que isso mudou o desfecho
      deste claim. Desfecho formal nunca foi gravado.
    verificacao: herdado_nao_verificado
    para_fechar: "colar texto completo (seção de resultados) de 33515765 + rodar Q017 com Q014 base v2"
  - claim_id: B1.SM02.023
    status: em_busca
    registrado: "4 rejeições em 13/08 (34595576, 27824355, 24040799, 24317097); nenhum candidato G3 registrado"
    verificacao: herdado_nao_verificado
    para_fechar: "rodar a query de novo e colar lista completa"
  - claim_id: B1.SM02.028
    status: em_busca
    registrado: "triagem extensa em 13/08 (~60 rejeições, ~15 realocações); 41821624 citado como 'candidato G3' no log, sem avaliação gravada"
    verificacao: herdado_nao_verificado
    para_fechar: "colar abstract de 41821624; verificar se há outros candidatos não registrados"
  - claim_id: B1.SM02.032
    status: em_busca
    registrado: "20031110 rejeitado (12/08); 22687336 (Hiles et al.) 'em avaliação' segundo CANDIDATOS_IDS_OFICIAIS"
    verificacao: herdado_nao_verificado
    para_fechar: "colar abstract de 22687336 + lista completa da query"

# ============================================
# PENDÊNCIAS QUE EXIGEM DECISÃO DO USUÁRIO
# ============================================
pendencias_decisao_usuario:
  - id: P1
    tema: "20132991 em .012c"
    situacao: "usado como fonte nivel corroborante, mas o próprio papel registrado diz que 'não permite classificar GFAP como elevado ou nulo'"
    recomendacao: "rebaixar para fontes_exploratorias de .012c (não sustenta direção nenhuma)"
  - id: P2
    tema: "33339712 e 30696814 (população bipolar)"
    situacao: "herdado da Lista Canônica v1.3 — descartado vs. realocar a B4"
    recomendacao: "manter descartado: B4 é mecanismo, e estes claims clínicos têm disease_context ansiedade/depressão"
  - id: P3
    tema: "Q014 base reformulada (v2) na Lista Canônica v1.4"
    situacao: "RESOLVIDA por uso em 17/09 — .014 fechado com a v2; segue valendo para .016 e .017"
    recomendacao: "nenhuma ação"
  - id: P4
    tema: "Schema-Claim v1.3"
    situacao: "campo forca_evidencia_afirmacao usado em .014 como experimental; sem vocabulário fechado definido"
    recomendacao: "oficializar com valores alta|media|baixa e critério escrito por valor, junto da decisão do schema de evidencias/bibliografia"

nao_escolhidos_arquivo_externo: "Estudos que não foram escolhidos.md — 17+ PMIDs catalogados"

proximo_alvo:
  ordem: [".017", ".016", ".018", ".019", ".020"]
  motivo: >
    Grupo 3 (TSPO-PET) em fechamento: .014 e .015 aprovados. Segue
    .017, que já tem achado herdado a confirmar (texto completo de
    33515765), depois .016, .018 e .019. Depois: Grupo 4 (.020-.025, com
    .023 em andamento), Grupo 5 (.026-.030, com .028 em andamento),
    Grupo 6 (.031-.035, com .032 em andamento).
