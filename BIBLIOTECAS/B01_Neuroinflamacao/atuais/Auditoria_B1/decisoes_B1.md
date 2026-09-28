# Auditoria Científica de Conteúdo — B1 (Neuroinflamação)

**Data:** 2026-05 (retrocompatibilização ao padrão B7/B8) · **Sessão:** operador de geração; **P-6** (2ª verificação independente/avaliador cego) PENDENTE.
**Objeto:** trechos-âncora da canônica `B1 NEUROINFLAMAÇÃO V3 CANONICA.md`.
**Ferramentas:** G1 eutils (esearch+esummary+efetch), G2 espécie/elegibilidade, G3 suporte; `gate_script.py` (P-5) + `validar_auditoria.py` (framework).

## Contagem de decisões
- Trechos no ledger: **188**
- G1: {'VERIFIED_REFERENCE': 188} · G2: {'ELIGIBLE_SOURCE': 60, 'NAO_APLICAVEL': 128} · G3: {'APROVADO': 168, 'APROVADO_COM_RESSALVA': 19, 'INCONCLUSIVO': 1}
- status_auditoria: {'APROVADO': 168, 'APROVADO_COM_RESSALVA': 19, 'NAO_LOCALIZADO': 1}

## Notas
- Módulo 09 no schema oficial (id_referencia_interna `REF_SOBRENOME_ANO`, doi, claim_id_origem; 5 arquivos).
- Referências citadas apenas em listra/corpus indexadas por rótulo canônico (apêndice de corpus) para rastreabilidade; citações clássicas de prosa sem PMID verificável foram rebaixadas a menção nominal sinalizada ao P-6 (R04: campo vazio preferível a dado inventado).
- Evidência animal/pré-clínica sinalizada `[APENAS PRÉ-CLÍNICO]/[EXT]`; bloco natureza_sistema (P12), semantic_layer (R06) e referência cruzada a B16 (P16) presentes na canônica.

## Declaração
> A Biblioteca_B1 foi auditada quanto a conteúdo: cada afirmação factual tem vínculo verificado (G1→G2→G3) ou está sinalizada como parcial/pré-clínica. `validar_auditoria.py`: **0 ERRO**; `gate_script.py`: **GATE APROVADO**.
> **Pendência P-6:** 2ª verificação independente (avaliador cego).

---

## Rodada [AT] 2026-09-08 — reconciliação de insumo externo (P-7) → V4

**Objeto:** insumo externo "matriz canônica B1" (autoria de outro modelo), oferecido pelo
usuário para revisão cruzada da B1 vigente (V3 → **V4**).
**Fluxo:** P-7 (mini-ciclo Pré→G1→G2→G3→nova versão). V3 **não** editada in place —
arquivada em `producao/historico/v3_canonica_2026-09-08.md`.

### Entrada do insumo
- 74 itens com identificador + 13 só (Autor, Ano) — G1 eutils: **68/74 resolvidos**.
- **4 NÃO localizados:** identificador ilegível `03946320231198828`; DOI não indexado
  `10.1186/s12974-026-03614-3`; DOI malformado `10.1038/s12974-023-02769-y` (s12974 é BMC/10.1186);
  pré-print `10.20944/preprints202201.0134.v1`.
- **4 FALSOS POSITIVOS rejeitados e expostos** (PMID não corresponde ao paper declarado):
  "Min 2023"→1110775 (chumbo 1975); "Setiawan 2015"→25797247 (oncologia); "Richards 2018"→30156409
  (toxina biofísica); "Setiawan 2018"→30563872 (melanoma). (Setiawan 2015/2018 verdadeiros já
  estavam na B1 vigente.)
- **Correção do relatório prévio (honestidade):** o item "fluoxetina psychres" que havia sido
  marcado como 5º falso positivo **estava correto** — o DOI `10.1016/j.psychres.2021.114317`
  resolve para o mesmo PMID 34864233 (García-García 2022, meta ~292 pacientes TDM). O item
  **ENTROU** (tag MA). Saldo final: **4 FPs**, não 5.

### Decisões de conteúdo
- **ENTRARAM 49 refs verificadas** (188 → 237), com G2/G3 individual (`producao/insumos/matriz_b1_at_final.json`),
  `origem_pipeline="ATUALIZACAO_AT_2026-09-08"` e `origem_entrada=POLITICA_FONTES` no ledger:
  - 5.4 TSPO (10): evidência negativa/heterogeneidade/interpretação celular + confundidor K1 2026.
  - 5.6 central (4): Enache meta tri-compartimental; Wang&Miller CSF; micróglia single-cell
    não-inflamatória (Böttcher 2020; Nagy 2020).
  - 5.7 (1): Anderson 2020 multi-escala.
  - 5.1 subgrupos (7): longitudinal (Mac Giollabhui 2021), 1º episódio/drug-naïve (Gędek 2025;
    Li 2026), adolescentes (Jadhav 2025; D'Acunto 2019), sexo (Elgellaie 2023), predição (Gavril 2024).
  - 2.1 NLRP3 (7): Zhang 2015; Kaufmann 2017; McColgan 2026; MCC950 Liu 2022b [sinal de alvo];
    Kouba 2022; Xia 2023; Xu 2025.
  - 2.3 GSDMD (3): Li 2021 astrócitos; Wang 2021 GSDMD-independente; Han 2023b [EXTRAPOLADO].
  - 2.10 KP (10): Almulla 2022; Haroon 2020; Savitz 2020; Stone 2024; Badawy 2023; Bertollo 2025;
    O'Regan 2026; Murata 2026; Parrott 2016; Martín-Hernández 2019.
  - 6.1 antidepressivo→inflamação (5): Köhler 2018; Liu 2020b; Wang 2019; Xie 2025; García-García 2022.
  - 3.17 IL-33 (1, submódulo novo, "mediador candidato — emergente").
  - 10.4 Hua 2026 (1, submódulo novo; [APENAS PRÉ-CLÍNICO][EXTRAPOLADO: ED→TDM]; P16 mantido).
- **Rótulos de autoria do insumo corrigidos contra PubMed:** "Ng 2018"→Mac Giollabhui N 2021;
  "Kouba 2023 (phrs)"→Xia CY 2023; "Kouba 2023"→Kouba BR 2022 (ijms); meta de TAG do insumo =
  Costello 2019, já presente na B1.
- **NÃO ENTRARAM (19, motivo registrado):** 4 FPs; TCE/TBI (2); Alzheimer (2, 1 já ausente);
  esclerose múltipla (2); minociclina (2 — intervenção, P20); redundâncias editoriais (3);
  duplicatas bibliográficas internas (2: Liu 2020 Mol Psych; Więdłocha-equivalente);
  já cobertos na B1 por PMID (6); 1 DOI não re-resolvido na etapa final.
- **13 itens apenas (Autor, Ano):** permanecem `[G1: a cravar]` — não entram sem identificador.
- **Regras SE-ENTÃO / claims-mãe do insumo:** não são fontes; a formulação foi adotada como
  governança textual (regras de leitura TSPO, periferia≠centro) com lastro nas refs verificadas.

### Portões pós-fusão (V4)
- gate P-5: **APROVADO** (refs 237 | vínculos 257) — INFO[6] P-6 fase 1-operador (não bloqueante).
- framework: **0 ERRO** (237 avisos não-bloqueantes de citacao_literal — padrão da série).
- checklist entrega: **41/41**.
- Correção de conformidade: refs [AT] viviam em 01 e 04 simultaneamente → migração da trilha
  para `producao/04_AT_ciclo_2026-09-08.json` (Módulo 09 volta a ter identidade única por ref).

**P-6:** continua PENDENTE — a leva [AT] passa a fazer parte do pacote cego de alto risco.


---

## ALTERAÇÃO 2026-09-10 — IMPL-AT-11 (4ª rodada perícia: enum fantasma `*_intervencao`) — opção (b)
**O quê:** 3 vínculos da leva v2 (VINC_B1V2_0205 REF_XIA_2024 minociclina/medo condicionado;
VINC_B1V2_0207 REF_WITTENBERG_2020 mega-análise 18 RCTs imunomoduladores; VINC_B1V2_0208
REF_SU_2018 ômega-3/ansiedade) tinham `forca_causal = natureza_relacao = "tier_2_intervencao"`,
valor INEXISTENTE no enum oficial (SCHEMA-CLAIM v3.1: tier_1_necessidade_e_suficiencia |
tier_2_necessidade_ou_suficiencia | tier_3_correlacional_mecanistico | tier_4_descritivo_estrutural).
**Decisão (conteúdo, opção b):** evidência de intervenção (RCT/MA) demonstra necessidade-OU-suficiência,
não ambas → `forca_causal = tier_2_necessidade_ou_suficiencia`; a relação reportada é intervencionista
(modular o mecanismo altera o desfecho) → `natureza_relacao = causal`. NÃO se cria tier novo: "intervenção"
é tipo de desenho (prova), não nível da escala de força causal; desenho já é registrável nos selos/g3.
**Por quê:** perito externo (PARA_O_AGENTE_2026-09-10 §2) bloqueou os 3 até decisão; a mesma string
fantasma (`tier_1_intervencao`) existia no gate_script.py L101 — o ramo de força causal do critério [6]
nunca disparava no acervo (replicado 2026-09-10: INFO[6] B1 = 36 pré-correção → **38** pós [rev.1: corrige projeção inicial de 41 registrada neste bloco; número medido no gate pós-reparo = 38 — 2 dos 5 refs tier_1 da B1 já estavam cobertos pelo ramo de uso 'clinico/nucleo_causal']).
**Evidência:** trilha `producao/05_reparo_AT11_2026-09-10.json` (sha pré/pós, valores originais
preservados em `nota_reparo` nos 3 registros — rollback declarativo); gate 16/16 APROVADO pós-reparo;
não-conformidade residual de enum em `forca_causal` da B1: **0** (censo pós-reparo). Achado ampliado
registrado na resposta ao perito (B7/B8 têm 106 registros com vocabulário estendido não-oficial:
`tier_2_intervencao_humana` ×10, `tier_2_meta_analise` ×24 etc. → declarado nos manifestos de B7/B8
e enfileirado para harmonização no SCHEMA v2/AT-09 junto de AT-03/AT-04 — NÃO remapear em silêncio:
re-classificação científica por conteúdo, não mecânica).


---

## ALTERAÇÃO 2026-09-11 — AT-02/AT-13 fechados (5ª rodada perícia externa)
**O quê:** os 257 `trecho_ancora` dos vínculos chegaram a **100% de literalidade** contra a
Canônica (era 103/257 = 40%). Pipeline do perito rodado em bancada com réplica exata
(80+6+38+0+27 = 151 re-extrações; autoteste contrato 8/8; hash da canônica conferido).
**Decisões de conteúdo do agente:** (1) AT-13×3 — VINC_B1_0095 (→frase Zhang 2024),
VINC_B1_0121/0122 (→frase S100B que cita Arora 2019 **e** Gulen 2016; co-citação legítima:
uma frase, duas cláusulas, duas refs) reancorados manualmente com extração markdown-aware —
o perito recusou por ferramenta, e a recusa estava certa: era caso de conteúdo;
(2) correção da Canônica §6.2: rótulo `— IL-6 predictor, 2015)` → `; Virtanen et al., 2015)`
(única linha de prosa alterada; fonte REF_VIRTANEN_2015, PMID 25697833) + VINC_B1_0130
reancorado; (3) AT-02c: 26 prefixos de cabeçalho `###` removidos de âncoras.
**Por quê:** vínculo = afirmação × fonte; âncora na frase de outra fonte (VINC_B1_0147-era)
faz o G3 julgar a frase errada. Regra determinística adotada: âncora = frase da Canônica que
contém a citação nominal da própria referência (Prompt v4.2 L1256 + L1450).
**Evidência:** `producao/05_reparo_AT02_AT13_2026-09-11.json` (sha pré/pós); backups
`vinculos…json.bak_pre_rodada5_2026-09-11` e `antigos/historico/v4_canonica_pre_rodada5_2026-09-11.md`;
nota datada no fim da própria Canônica; verificação pós ao final deste bloco quando registrada.

---

## ALTERAÇÃO 2026-09-11 (rev.2 do dia) — RENAME/versionamento: Canônica B1 V4 → V4.1

- **O quê:** `B1 NEUROINFLAMAÇÃO V4 CANONICA.md` renomeado para `B1 NEUROINFLAMAÇÃO V4.1 CANONICA.md`; título interno e `artefato_rotulo` v4→v4.1 (manifesto também tinha o rótulo defasado em "v3" — corrigido no mesmo ato).
- **Por quê:** a mudança da rodada 5 (1 linha de prosa, §6.2) ficava invisível na listagem do workspace enquanto o arquivo mantinha nome e número antigos. Solicitação direta do operador: sinalizar mudança por nota **e** por versão.
- **O que NÃO mudou:** zero linhas de conteúdo científico nesta rev.2; vínculos (257) e ledger (237) intactos; v4 pré-mudança preservada bit a bit em `antigos/historico/v4_canonica_pre_rodada5_2026-09-11.md`.
- **Trilha:** CHANGELOG_GERAL.md (2026-09-11, abertura+resultado) · rev.2 da nota de auditoria no fim da própria Canônica · `alteracoes[]` do manifesto.

---

## ALTERAÇÃO 2026-09-11 (rev.3 do dia) — EXECUÇÃO R1–R13, AUDITORIA EXTERNA INTEGRAL (agente auditor; veredito na v4.1: APROVADA COM RESSALVAS)

Ciclo registrado em `producao/10_execucao_V5_N2_reparos_2026-09-11.json` a `14_R4_lista_v12_B01_2026-09-11.json` e na ata REGISTRO DE AUDITORIA da V5 (itens 1–9). Síntese das decisões desta sessão:

**R1/R2 (GRAVE) + R7/R11 (menores):** executados na Canônica V5 e nos vínculos N2 correspondentes — ver REGISTRO V5 itens 1–5 e trilha 10. AUD-038 reduzido a ano (Hafizi 2007; PubMed 17639827 sem abstract — efetch replicado); AUD-040 retirado pelo próprio auditor (errata append-only) — sem ação.

**R5 (12 PMIDs assinalados pelo auditor como omissões candidatas):** decisão item a item, APÓS rastro factual no nosso pipeline (matrizes, corpus, log): 11 dos 12 NUNCA entraram no nosso funil — ausentes de `matriz_b1_g1/at_final/cruzamento`, `corpus_pubmed.json` (761) e `log_de_busca` (622; top-10). Não são "omissões de corpus", são candidatos externos trazidos pelo auditor.
- **INCORPORAR no próximo ciclo [AT] (10):** 26820800 (Bryleva & Brundin 2017, revisão KYN/suicidalidade), 42525506 (Behera 2026, GWAS metilação PFC suicidas), 39504032 (Herzog 2025 JAMA Psychiatry, neuroinflamação+ideação), 17457312 (Müller & Schwarz 2007 Mol Psychiatry, paper fundador serotonina/glutamato), 24633997 (Dantzer & Walker 2014, contraponto excitotoxicidade), 25124710 (Bay-Richter 2015 BBI, metabólitos inflamatórios/NMDA), 29971587 (Richards 2018, TSPO↑ em TDM NÃO medicado), 29496589 (Setiawan 2018, duração de doença), 41752782 (Erdem Ş 2026), 40638969 (Erdem M 2025, ponte BDNF↔NLRP3 — BLOCO_09). Prioridade declarada ao sub-bloco de suicidalidade (§5.2). Todos passarão por G1 eutils + G3 antes de entrar (mesmo rito [AT] 2026-09-08); NENHUM é agregável à V5 (regra de consolidação: zero citação nova — só reformulação).
- **NÃO-incorporar, motivado (2):** 27221623 (Bryleva 2017, revisão CTBN — marcada "opcional" pelo próprio auditor; sobreposição temática com 26820800 do mesmo grupo, já incorporada; redundância) e 29895691 (McKenzie 2018, caspase-1 glial — trilha real: candidato em `matriz_b1_cruzamento.json/novos` sem verificação G1 (`g1[29895691]=null`) e sem decisão no `matriz_b1_at_final.json`; "opcional" do auditor; eixo caspase-1/piroptose glial já coberto no BLOCO_02 com refs verificadas). Caso a revisão cega discorde, a porta é o mesmo ciclo [AT] com racional explícito.

**R8 (AUD-032, 17 órfãs Módulo 09 ↔ vínculos):** 16 vínculos criados (VINC_B1_0258–0273) por reconciliação de registro a partir do ledger — âncora = linha-lote literal do APÊNDICE DE CORPUS (única ocorrência do token na V5; NENHUMA das 17 tem citação nominal em prosa — verificação computada); REF_ANNETT_2020 removida do Módulo 09 e do apêndice (referência isolada sem uso em prosa; anexá-la a uma afirmação violaria zero-citação-nova). Consequências registradas: ledger 237→236 (AUD_B1_0075 preservada verbatim na trilha 11); 23 âncoras de ledger re-apontadas para a linha pós-remoção; Módulo 09 = 236 (01=200 · 02=33 · 03=03). Dívida: D-B1-R8-CLAIM (16 vínculos sem claim_id — ausente no ledger de origem GPM).

**R3 (AUD-036):** (a) 19 PARCIAIS — 15 já tinham g3_notas com o motivo enunciado (verificação item a item, trilha 12); 4 sem nota (VINC_B1V2_0190/0197/0198/0202) receberam nota reconstruída do ledger (veredito + ação corretiva; NÃO é a nota contemporânea, que se perdeu) + `reavaliacao_g3_pendente: true` → dívida D-B1-R3-G3NOTA. (b) 30 VINC_B1V2 sem claim_id: herança por co-ocorrência no mesmo parágrafo da V5 = **0/30 elegíveis** (computado); Lista Canônica v1.1 não traz campo subseção → mapeamento não decidível sem extrapolação → dívida D-B1-R3-V2CLAIM (decisão aceita pelo auditor: "ou dívida nomeada"). Campo `achado_central_molecular` já existia nos 30 (0 vazios — verificado).

**R4 (AUD-035):** Lista Canônica → v1.2: 78/83 itens `em_busca` → `usado_em_biblioteca` (+`uso_registrado` com os vínculos); observação nomeada: 2 claim_ids em uso SEM item na Lista (B1.MEC.BLOCO03.017, B1.MEC.BLOCO10.004) → dívida D-B1-R4-2CLAIMS. Backup `.bak_preV12_2026-09-11`; CRLF preservado; trilha 14.

**R6 (AUD-037):** manifesto sincronizado por contagem de arquivo: pmids_total 184→**236** (dedup), meta_analises 6→**33**, +ensaios_clinicos=**3**, +referencias_total_modulo09=**236** (01=200+02+03), versao 2.5→2.6 (divergência com `pipeline_versao_geracao` era rotulagem sem bump — confessada aqui e na entrada `alteracoes[]`), `artefato_rotulo` → "CANONICA V5 — status PROVISÓRIO", +`status_canonico: PROVISÓRIO` com motivo e data (R9–R10).

**R9–R10 (status PROVISÓRIO obrigatório):** declarado no cabeçalho da V5 (artefato_rotulo), no manifesto (`status_canonico` + motivo) e aqui: a canônica segue PROVISÓRIA até a revisão cega humana dos 59 vínculos de alto-risco (instrumento e lista integram o lote de re-auditoria §6 da réplica).

**R12 (ratificação da ordem invertida — pendência oficial desde a Fase 1):** RATIFICADA nesta data com a trilha agora completa: a matriz externa B1 ([AT] 2026-09-08) foi recebida como insumo, auditada ref-a-ref (`insumos/RELATORIO_AUDITORIA_MATRIZ_B1.md`), congelada em `insumos/matriz_b1_at_final.json` (49 entrantes — todos presentes no Módulo 09 — e 19 rejeitados com motivo), e só então incorporada; a ordem efetiva de execução (reconciliação documental ANTES da ratificação formal) é reconhecida como inversão processual e fica ratificada **ex post**, sem prejuízo da evidência, porque cada elo está em arquivo datado. O arquivo `matriz_b1_at_final.json` passa a integrar o lote de re-auditoria.

**Manutenção descoberta no ciclo (IA, sem extrapolação):** 159/273 âncoras de vínculo não literais por espaçamento/pontuação (deriva pré-existente; nunca checada por portão — o framework valida âncora do LEDGER, não dos vínculos). 124 reparadas mecanicamente (sítio único, similaridade ≥0.985, sem mudança de conteúdo; rev do método registrada na trilha 13); **35 com deriva lexical 0.90–0.985 → dívida D-B1-ANCORA-DERIVA** (lista na trilha 13; exige leitura humana/caso-a-caso — a IA não re-escreve âncora com troca de palavras).

**R13 (log de busca completo, não top-10):** pendente de empacotamento — o `log_de_busca` disponível no workspace é o top-10 (622 linhas). O log completo da busca ativa 2026-09-03 não está preservado no workspace (mesma situação do anchormap, dívida já declarada); a declaração honesta vai no lote: corpus (761), matrizes, ledger e Módulo 09 cobrem a rastreabilidade ref-a-ref; o log completo fica como dívida D-B1-R13-LOG a montar de eutils no próximo [AT] (queries salvas na Lista v1.2).

**Dívidas nomeadas desta rev.3:** D-B1-R8-CLAIM (16) · D-B1-R3-V2CLAIM (30) · D-B1-R3-G3NOTA (4) · D-B1-R4-2CLAIMS (2) · D-B1-ANCORA-DERIVA (35) · D-B1-R13-LOG (1). Nenhum dado foi fabricado: tudo o que não era decidível virou dívida com método e evidência negativa computada.

---

## rev.4 — 2026-09-13 (re-auditoria do Auditor-Mestre sobre o lote V5: C1–C6, F-01…F-10, P-8, L-01…L-16)

### Confissão da casa (obrigatória): C1/AUD-049 — propagação incompleta NOSSA
Réplica confirmou nos nossos arquivos, ANTES do reparo: ficha `REF_COMAI_2022` contradizia a prosa R2
("…bipolar/TDM"); `VINC_B1_0219` g3_notas "Meta tri-compartimental"; `VINC_B1_0247` "questão aberta do PET";
ledger Enache "tri-compartimental"=True e Wijesinghe "questao aberta"=True. **As correções R2/R11 da V5
não haviam propagado a ficha/g3/ledger — falha nossa de propagação**, agora reparada pelo script dele
(R-01 4 campos · R-02 12/16 · R-05 34 · R-06 5 · R-07 0; trilha 15, backups ×6 `.bak_pre_reparo_20260913`).
Manifesto final **idêntico** ao enviado por ele (0 campos divergentes, comparação computada).

### Decisões executadas (esta sessão)
- **Reparo de coerência (trilha 15):** executado com 1 desvio registrado — patch em `nota()` (auditor
  convertia nota para LISTA; casa mantém string " || "; semântica idêntica — comunicado na carta).
- **Trilha 16:** VINC_B1_0005 re-ancorada à fatia literal multi-sentença (prova nt(fatia)==nt(armazenada))
  + VINC_B1_0175 (Steiner) re-ancorada da linha-lote §11 à frase nominal ÚNICA L572.
- **Trilha 17 (AUD-038/V-05 causa-raiz):** `REF_HAFIZI_2005 → REF_HAFIZI_2007` COMPLETO — ficha (id +
  campo-lista), vínculos (VINC_B1_0047), ledger (id + citacao_literal-token + 25 âncoras da listra-índice
  propagadas), canônica (1 token do APÊNDICE; **0 linhas de prosa**; sha 3c6dda4d→5051080b), manifesto com
  sha vigente registrado. eutils: pub 2007, PMID 17639827; o "2005" veio do nome NLM do periódico.
- **C2 (V-02):** 4 vínculos finais (Han 0261, Huang 0262, Li_2025b 0265, Mehta_2020b 0266) com 2–3 frases
  candidatas — **recusa automática correta → fila humana de especialista**. Dívida atualizada:
  **D-B1-R8-CLAIM residual 4** (era 16). **D-B1-ANCORA-DERIVA: ENCERRADA** (34 do reparo + VINC_B1_0005
  nossa = 35/35).
- **Ferramentas (F-08/F-09):** auditor relatou ter corrigido do lado dele mas NÃO anexou os arquivos;
  aplicamos o equivalente descrito, com backups `.bak_F08/F09_2026-09-13`: (i) `checklist_entrega.py`
  caminhos relativos ao próprio script (`Path(__file__)`); (ii) `gate_script.py` docstring reescrita
  honesta + seção **"COBERTURA QUE ESTE PORTÃO NÃO TEM"** apontando para o P-8.
- **P-8 na casa: 2 patches defensivos nossos** datados: (a) `nota()` do reparo (acima); (b) validador
  tolerando `corte_literatura` string/dict (uso série; B13 quebrava com AttributeError). **Flags ao
  auditor:** V-14 consta da docstring mas NÃO está implementada; reparo tem ramo morto em R-05
  (âncora multi-sentença nunca reparada por ele — VINC_B1_0005 ficou por nossa trilha 16).

### Divergências de contagem (réplica × relatório dele) — transparentes
P-8 ante-reparo: nosso 22 ERRO × dele 24 (varância 2, a esclarecer bilateralmente); linhas-lote F-02:
nossas 102 × dele 86 (mérito intacto).

### Não decididos nesta instância (nomeados, nunca fabricados)
- **C3/AUD-051 Osimo 2019:** ficha pronta (`producao/insumos/reauditoria_2026-09-13/PROPOSTA_AT_OSIMO_2019.json`);
  entra no **próximo [AT]** com as 6 ações obrigatórias + correção de prosa (restaurar vínculo número↔limiar
  sem fixar corte). Observação crítica dele: o "27%" era definido por PCR>3 e a V5 (R7) removeu o corte —
  número relativo a limiar indefinido.
- **C4/AUD-052 BLOCO_11.4:** declaração de não-validação/circularidade do Critério C = autor científico.
- **F-04/L-03:** reancorar as 236 entradas do ledger à frase nominal = migração de esquema (decisão de
  modelo-alvo; a susceptibilidade de hoje ficou demonstrada pela trilha 17: 25 âncoras de listra
  propagaram 1 token renomeado). **D-SERIE-CONVENCAO-ANO-ID** (3 refs epub×print — ver decisoes_B13.md).
- **L-01…L-16:** respondidas ponto a ponto na carta `_documentos_serie/RESPOSTA_REAUDITORIA_AUDITOR_MESTRE_2026-09-13.md`.
- **V-13 (B13 e demais):** manifestos fora da B1 não registram sha vigente — trilhas datadas cobrem hoje.

### Portões pós-rodada (2026-09-13, computados)
P-5 gate APROVADO · checklist **41/41** · framework **0 ERRO** · **P-8: 4 ERRO / 24 AVISO**
(V-02: exatamente 0261/0262/0265/0266 → fila humana; V-01 0; V-05 0; V-13 OK sha 5051080b) ·
censo série **32/32 BLOQ 0** (`producao/censo_pos_reauditoria_2026-09-13.txt`).

---

## Rev.5 — 2026-09-13 (rodada 2 do dia: ERRATA do Auditor-Mestre + nova delegação do operador)

### Delegação do operador (verbatim, registrada íntegra)
> "referente a decisão humana é porque você não em acesso a ciencia ou a engenharia de software para saber
> qual caminho tomar? Se for peço que use a ciencia e a engenharia de software se for o caso, pois creio
> que a ciencia e os engenheiros de software terão uma resposta mais adequada do que a minha, e depois sim,
> quando estiver terminado a plataforma de saúde posso passar por uma equipe humana de especialista"
> + "Peço que atualize a biblioteca após a próxima rodada" + "foque mais na B01".

**Como a casa lê:** decisões de método (ciência/engenharia) são decididas PELA CASA com evidência e data,
não terceirizadas ao operador; a revisão humana de especialistas acontece NO FIM, como instância própria
(**P-6 permanece de pé e intocado** — é o próprio auditor quem afirma que nenhum agente dos dois lados é
barreira suficiente contra erro de ciência; a casa concorda e registra).

### Executado nesta rodada (trilhas em producao/18, 19, 20)
1. **Etapa 0 do parecer dele — C3 [AT] Osimo 2019:** ficha REF_OSIMO_2019 (34ª MA; PMID 31258105; eutils
   G1 real feito; abstract colado no ledger AUD_B1_0238), vínculo VINC_B1_0274, prosa §11.1 reescrita
   (27% e OR ~1,46 re-ancorados ao limiar de PCR da meta de origem; faixa/corte no C-LAB — P20), tabela
   harmonizada, VINC_B1_0172 reavaliada (subgrupo, não universal). Trilha 19 (rev.1: g2 enum `eligible`
   conforme contrato do perito; rev.1 ledger: `query_utilizada` registrada).
2. **Etapa 0 — C4 BLOCO_11.4:** ressalva de NÃO-VALIDAÇÃO (sensibilidade/especificidade/valores
   preditivos desconhecidos; uso autônomo vedado) + nota de circularidade do Critério C (C prediz A por
   construção; carga probatória em A e B). Trilha 20.
3. **Re-ancoras V-02 decididas pela casa, com ciência (trilha 18, rev.1):** os 4 ERRO V-02 eram decisão
   CIENTÍFICA de homônimos, não loja de correção tipográfica — resolvidos por autoria via PubMed:
   VINC_B1_0261→Han R 2023 (37597297, IL-10 ICH, §2.19); VINC_B1_0262→Huang **P** 2024 (37917301, TREM2/
   NLRP3 MPTP, §4.1 — § outra era Huang **S** 2024b, 38395698); VINC_B1_0265→Li **H** 2025b (41094684,
   cGAS-STING, §2.18 — descartado Li **C** 2025, 40391473); VINC_B1_0266→Mehta **D** 2020b (31951051,
   metilação TEPT, §2.21 — descartado Mehta **ND** 2020, 32291455).
   **rev.1 (confissão datada):** a 1ª passada distinguiu por inicial do autor; o V-05 oficial só reconhece
   `(Sobrenome et al., ANO[sufixo])` e a cobertura caiu a 94,1% (ERRO); **reversão documentada para
   sufixo de ano** (que já vive nos IDs e tokens). Sugestão levada ao auditor: regex aceitar inicial
   (APA/ABNT admitem). Nada foi escondido: a ida-e-volta consta do REGISTRO item 10 da V6.
4. **Canônica V6** (principal sobe; V5 bit-a-bit em antigos/historico/, sha 5051080b): manifesto 2.7,
   237 refs · 274 vínculos · 237 ledger, sha V6 `d8f41662…` registrado com data. REGISTRO item 10 narra
   a rodada (inclui a observação L717: "(Mehta et al., 2020)" FKBP sem ficha inequívoca — **fila P-6
   humana; NÃO decidido pela casa**, e nunca preenchido com referência de asma).
5. **Ferramentas:** os 4 scripts oficiais da ERRATA instalados verbatim com conferência bilateral
   (backups `.bak_pre_oficial_2026-09-13`); nossos patches da rodada 1 aposentados (versão dele é
   superconjunto; V-14 implementada de verdade — re-testado: "14 regras anunciadas, todas executadas").

### Portões pós-rodada-2 (2026-09-13, computados)
- P-5 gate: **APROVADO** (ressalva de fase: 39 claims alto-risco sem 2º avaliador — é o P-6, declarado).
- Checklist: **41/41**.
- Framework: **0 ERRO / 236 AVISO** (tokens [TAG]×235 da dívida nomeada D-B1-R13 + …; 0 erros).
- **P-8: 0 ERRO / 25 AVISO** — V-02 **0** (eram 4); V-01 0; V-04 0; V-05 277/286 = **96,9%**; V-06 18
  avisos (qualificadores não propagados — dívida D-B1-R3-G3NOTA viva); V-08 5 (números em prosa
  editorial do REGISTRO/rótulo — não científicos); V-09 30 s/ claim_id (D-B1-R8 parcial… ver abaixo);
  V-10 221 tokens no ledger (L-13); V-13 sha conferido; **V-14 14/14**.
- Censo série: **32/32, BLOQ 0** (o bloqueio transitório `g2_elegibilidade=elegivel`×1 foi achado pelo
  próprio censo e corrigido com rev.1 — instrumento funcionando como deve).

### Réplica bilateral da tabela §4 dele (P-8 oficial nas 16, JSONs em
### _documentos_serie/replicacoes/2026-09-13_P8_serie/)
**15 de 16 batem EXATAMENTE** (V-02: B02 3, B03 165, B04 131, B05 160, B06 68, B07 2, B08 0, B09 35,
B10 39, B11 40, B12 35, B13 167, B14 240, B15 134, B16 290; B02 também confirma 126 órfãs V-04 + 7 V-05).
Única diferença: **B01 — ele mediu 273 vínculos/5 ERRO com dados pré-V6; a casa mede hoje 274/0**
(+1 vínculo = VINC_B1_0274 Osimo; −5 ERRO = as 4 re-ancoras da trilha 18 + o 5º que era o V-05×1 dele,
contado com o matcher intermediário). Total: casa 2.496 vínculos/1.509 V-02 (60,5%) × dele 2.495/1.514 —
a diferença fecha aritmeticamente com o trabalho desta rodada. **B01 V-05 = 0 medido hoje** (dele: 1).

### Dívidas — estado após a rodada 2
- **D-B1-R8-CLAIM (re-ancoras V-02 pendentes):** 4 → **0 — ENCERRADA** (trilha 18; decisão científica
  da casa sob a nova delegação; P-6 revisa no fim).
- D-B1-R3-V2CLAIM (30 sem claim↔v2), D-B1-R3-G3NOTA (4→ mantida, V-06 cobre 18), D-B1-R4-2CLAIMS (2),
  D-B1-R13-LOG (1 + tokens ledger, L-13), D-SERIE-CONVENCAO-ANO-ID (3 epub×print; convenção pubdate-NLM
  endossada por ele — renomear só quando cada biblioteca entrar no ciclo): **mantidas, nomeadas**.
- Observação-L717 (FKBP/Mehta): **fila P-6** (registrada no REGISTRO item 10 da V6).
- **P-6 (fila humana ~58 vínculos alto risco + itens desta rodada):** de pé — entra na revisão final
  por especialistas, conforme a delegação ("quando estiver terminada a plataforma").
- **L-17 (nova, dele):** manifestos sem schema/portão único medidos na série (B01 objeto; B02–B15 string;
  B16 None) — aceita pela casa; entra no pacote de schema.
- **L-13 subiu a prioridade máxima na fila dele** (`achado_verbatim_fonte`) — a casa registra e concorda:
  maior retorno do projeto; vai no pacote de schema com L-05 (Contrato Motor) e L-06 (precedência).

### Próximo passo (ordem dele, aceita pela casa)
L-05/L-06/L-13 (pacote de schema) → reancoragem série (etapa 5, mecânica, em paralelo) com o novo
critério de replicação: **só replicar quando o P-8 fechar 0 ERRO V-02 na piloto (feito hoje: B01 = 0)
e em mais uma biblioteca**.


### Adendo rev.5a (2026-09-13, mesmo dia) — correção editorial de ponto
- **H1 interno da V6 dizia V5** (esquecido na rotulação da rodada 2) — achado do operador. Corrigido; rótulo L5
  atualizado para a convenção-sufixo vigente (trilha 18 rev.1). Sem toque científico. Sha vigente passa a
  `e11dbd959c59d191…`; o intermediário `d8f41662…` vigorou algumas horas e está preservado bit a bit em
  `antigos/historico/v6_canonica_sha_d8f41662_pre_correcao_titulo_2026-09-13.md`. Portões re-rodados verdes.
- Lição registrada: ao trocar versão principal, conferir **as três** superfícies de rótulo — nome do arquivo,
  `artefato_rotulo` (L5) **e H1 (L1)**. Checklist da casa passa a incluir essa verificação de rótulo.

---

## Rev.6 — 2026-09-13 (rodada 3: parecer V6 → V7; taxonomia; C4 decidida no algoritmo)

### Entrada
`PARECER_B1_V6_E_PLANO_TRIO_2026-09-13.md` (Auditor-Mestre): C3 ENCERRADA · C4 PARCIAL (algoritmo
inalterado — 2 correções sugeridas) · §3 GRAVE: 3 taxonomias de classificador (pede semântica normativa;
recomenda V-15) · AUD-066 (4 números p/ o PROVISÓRIO) · AUD-067 (Mehta pela metade) · veredito
APROVADA COM RESSALVAS—base piloto · caminho do trio em 4 blocos · §7: reancoragem da série deve virar script.

### Réplicas executadas ANTES de aceitar (trilha 21)
- §3: autodivergentes **7/7 exatas e as mesmas nomeadas** · apêndice×balde **21,5% × 21,3% dele** ·
  prosa×balde 39,6% × 37,1% · divergentes prosa×apêndice 84 × 71 (universos de parser declarados).
  **Achado confirmado.**
- AUD-067: eutils 2026-09-13 (PMID 31951051) → pubtype Journal Article + **Systematic Review, SEM
  Meta-Analysis**. **Confissão:** a casa propagou [MA] na rodada 2 (REGISTRO 10/ledger) sobre um erro
  pré-existente de balde — agora corrigido de ponta a ponta.

### Decisões aplicadas (trilha 22; conteúdo científico ⇒ V6 → V7)
1. **C4 decidida NO ALGORITMO** — alternativa (b) do parecer, formalizada: **C vira modificador de
   a priori/especificidade, nunca condição de linha.** Regra executável: A satisfeito APENAS por
   marcadores sistêmicos inespecíficos (PCR-us/IL-6/TNF-α/sTNFR2/IL-1β) sem KYN/TRP alterado + C ≥1
   presente ⇒ rebaixa alta→indeterminada; C ausente não barra; C presente não eleva. Fundamento:
   confundidor reduz especificidade, não aumenta sensibilidade. Atende ao falso-positivo (obesidade+
   apneia = caso-armadilha do Bloco 4) e ao falso-negativo (sem contexto) demonstrados por ele.
   Perfis §12.1/12.3/12.4 harmonizados (o §12.3 dizia "alta mesmo com A parcial" — corrigido).
   **Instrumento continua NÃO VALIDADO** (ressalva do topo intacta). P-6 confere no fim.
2. **AUD-066:** cabeçalho amarrado a UM artefato: `FILA_REVISAO_CEGA_ALTO_RISCO_B1_2026-09-12.json`
   (**108 vínculos/91 refs**); linhagem 59(nominal, não preservado)→108(superconjunto declarado)→
   39(subconjunto do gate/rodada)→~58(aproximação verbal da carta) declarada.
3. **AUD-067:** ficha REF_MEHTA_2020b 02→01_pmids · ledger AUD_B1_0151 MA→OB · apêndice
   MEHTA_2020[OB]→[EC] (ficha é EC fMRI) e MEHTA_2020b[MA]→[OB] · **duplicata de token removida** ·
   50 âncoras de ledger propagadas · manifesto MAs 34→33 (refs/PMIDs seguem 237). Autodivergência
   "Mehta 2020 [EC]/[OB]" **zera**.
4. **L717-FKBP decidida por eliminação de desenho** (única revisão Mehta 2020 do acervo; a outra
   ficha é EC — impossível): token→(Mehta et al., 2020b). **Confissão:** FKBP5 não aparece nominal
   no abstract — identificação por desenho↔pedido↔escopo; **vínculo N2 formal NÃO criado** — a casa
   não fabrica vínculo; fica como item nomeado do P-6.
5. **Declaração normativa §3 (posição da casa):** a semântica vigente do [XX] é ambígua de fato
   (desenho × papel-no-claim sem declaração) — confessa. Correção material das 6 autodivergentes
   restantes e das ~84 divergências **não é arbitrada sem fonte primária**: entra no **pacote L-05/1.2
   (taxonomia única de desenho/força)** com **V-15 aceita** (identidade de classificador em prosa,
   apêndice, ficha e ledger; divergência = ERRO).
6. **Aceites registrados:** hardening do V-05 (inicial opcional) — ele aceitou; V-15 — aceita da nossa
   parte; ordem dos Blocos 1–4 — aceita; §7 (reancoragem da série precisa virar script) — concordado.

### Bugs da própria execução (confessados, corrigidos na mesma liturgia)
- **rev.1 da trilha 22:** framework/checklist derrubou PMID/DOI em texto corrido no REGISTRO item 11
  (o identificador fica na trilha/ficha; na prosa vai "PubMed nnnn"/periódico). sha V7 final
  `6e2c2979…` (intermediário 0f31372b).
- **manifesto:** minha entrada de `alteracoes` foi escrita como string e derrubou o P-8 (AttributeError)
  — a lacuna L-17 mordendo na prática; corrigida para dict no molde das demais.

### Portões na V7 (computados)
gate **APROVADO** · checklist **41/41** · framework **0 ERRO/236 AVISO** · **P-8 0 ERRO/26 AVISO**
(V-01 274/274 literal · V-05 96,9% · V-13 sha `6e2c2979…` conferido · V-14 14/14) · censo série
**32/32 BLOQ 0**.

### Filas
- **P-6 (revisão humana final):** 108 vínculos/91 refs (fila operacional) + formalização do vínculo N2
  de L717 + revisão da regra C4.
- **Pacote L-05/1.2:** as 6 autodivergentes restantes (Bull 2009, Chen 2024, Huang 2023, Yang 2024,
  Yehuda 2016, Zhang 2025) + ~84 divergentes prosa×apêndice (lista na trilha 21) + semântica normativa
  do [XX] + implementação da V-15 + V-05 com inicial.

---

## Rev.7 — 2026-09-13 (auditor externo de ESTRUTURA: revisão do código do P-5; gate rev.A2)

**Entrada:** parecer do 2º revisor (estrutura): reprodução independente do pacote (18/18, APROVADO,
0 ERRO/236 — qualidade da B1 validada) + 6 achados de código no portão.

**Réplica (trilha 23) — 6/6 confirmados:** uso fora do enum v3.1 (178/37/29/30; nucleo_causal 0 —
ramo morto do item 6, mesmo padrão do bug tier_1 de 2026-09-10, 2ª vez) · Bloco H 1,5/4 critérios ·
selo por frase não checado (7 pendente + 1 fulltext = 8; 7 CONFIRMADO+pendente — bate) · E1/E2/E3 fora
do código (0 violações hoje — confirmado) · bypass `citacao_confirmada` (0 dependências) · divergência
59×39 (era da V6; na V7 já resolvida pelo AUD-066).

**Aplicado — gate_script.py rev.A2 (backup `.bak_gateOficial_pre_revA2_2026-09-13`; PROPOSTA ao
Auditor-Mestre para a oficial):** item 6 reescrito com os 4 critérios do Bloco H (a=6 BLOCO_07/HIGH,
b=37 uso clínico, c=14 humano→causal, d=0 rejeição → 51 vínculos/38 refs, INFO fase) · E1/E2 viram
FALHA funcional · E3 INFO (2 âncoras possível truncagem: VINC_B1_0038/0232) · [10] INFO permanente de
`uso` fora do enum · [11]/[11b] selo por frase (1 full-text nomeado — vira FALHA ao fim da fila P-6;
7 APENDICE) · [1b]/[1c] bypass banido: dependência=FALHA (0 hoje), campo preenchido=INFO.

**Descobertas novas da própria execução (confessadas):** as **237 fichas trazem
`citacao_confirmada=True`** (sem dependência — todas têm g1_metodo; origem a auditar no L-05) ·
2 âncoras E3 · `forca_biologica_conexao` vazio em 274/274 (ramo HIGH mensurável, não mensurado).

**NÃO feito (fronteira):** remapear `uso` e preencher forca_biologica_conexao sem norma → pacote
**L-05/1.2** (mesma disciplina do §3); apagar `citacao_confirmada` idem.

**Portões pós-patch:** gate rev.A2 **APROVADO** · checklist **41/41** · framework **0 ERRO/236** ·
P-8 **0 ERRO/26** (dados intactos por construção e re-medido). **Dívidas novas nomeadas:**
D-A2-USO-ENUM (237 fora do enum) · D-A2-HIGH-VAZIO (274) · D-A2-CC-ORIGEM (237 fichas com o campo) ·
D-A2-E3-2 (2 âncoras) — todas vão ao pacote L-05 exceto E3 (fila P-6).

## Rev.8 — 2026-09-13 (Auditor-Mestre rodada 4: pacote V6 verificado; errata de ENTREGA; V-16 morde na hora)

**Entrada:** `PARECER_PACOTE_B1_V6_VERIFICADO_2026-09-13.md`. Ele auditou o pacote **V6** (a carta 3
descrevia a V7): integridade 18/18, portões reproduzidos exatos, C1/C2/C3 persistentes, decisão Mehte
validada em fonte primária, recusa do vínculo L717 julgada correta, **AUD-066 ENCERRADO**, camada de
evidência ENCERRADA; **C4 segue aberto na contabilidade dele só até a V7 chegar** (não contestada —
não entregue); adota nosso **84** como contagem de referência da dívida §3; novo achado: **12 tokens de
apêndice com dois classificadores simultâneos + 3 tokens temáticos sem autor**; propõe **V-16** (H1 ×
artefato_rotulo × nome de arquivo × rótulo do manifesto; divergência=ERRO); aceita **B13** como a
"mais uma" da replicação, **desde que o reancorador seja escrito ANTES e a B13 seja a 1ª execução
dele** (não piloto manual). Veredito: V6 aprovada com ressalvas mantida; **condição única da rodada 5:
pacote da V7 no mesmo formato**.

**CONFISSÃO — erro de versionamento de ENTREGA (classe nova, registrada como precedente):** a casa
montou três zips homônimos (V6/V7/V7b) em sequência e o canal humano encaminhou ao mestre o mais
antigo. Causa raiz: nenhum marcador de vigência no workspace. Correção processual aplicada no dia:
pacotes superados renomeados com prefixo `SUPERSEDED_` + `PACOTE_VIGENTE.txt` ao lado deles.

**Réplica (trilha 24, feita na V7 — não na V6 que ele mediu):**
- **V-16 confirmada e já mordendo:** H1/L5/nome=V7, mas o **manifesto dizia V5** — divergência real.
  **Errata aplicada (manifesto 2.8→2.9, backup em antigos/historico/):** artefato_rotulo V5→V7;
  `refs_01_pmids_base` 200→201 (derivado da migração Mehta — a contagem de arquivos estava certa, o
  campo derivado não); `status_canonico_motivo` reescrito amarrado à fila P-6 (108/91, linhagem,
  +VINC_B1_0038/0232/0047). Canônica **intacta** (sha 6e2c2979). Trilha re-rodada: **V-16 OK (4/4)**.
- **Tokens ambíguos — achado dele CONFIRMADO na V7 com resolução por camada:** apêndice interno
  **0 ambíguos** (Mehta zerado — a correção AUD-067 funcionou); **6 no índice inline**
  (PERRY_TEELING_2013, SERHAN_LEVY_2018, STRESS_EPI_2019, PRIMINGPRINC_2018, PSORIASE_2025,
  QUIMIO_META82_2017); **5 divergentes apêndice×índice** (BULL_2009, KLENGEL_2013, SETIAWAN_2015,
  SUBLETTE_2011, HOLMES_2018: apêndice [MA] × índice [EC]); **STEINER_2011 com nome duplo**
  (apêndice STEINER_2011[MA] × índice Steiner_2011_QUIN[EC]); união = 11 dos 12 dele persistem
  (Mehta zerado) **+ 1 que ele não mediu** (QUIMIO_META82_2017 [EC]×[MA]; o matcher dele não ancorou
  o sufixo — universos declarados, mesma reconciliação do 71×84).
- **Falso positivo meu confessado (trilha 24 rev.0→rev.1):** o parser varria o REGISTRO narrativo e
  contava o texto histórico ("MEHTA_2020[MA]" citado como passado) como token vivo: aparentava
  MEHTA_2020{EC,MA,OB}. Rev.1 corta o apêndice no próximo cabeçalho `## `. Registro da lição: o
  REGISTRO é append-only e **cita tokens antigos em prosa** — qualquer parser de token tem de
  delimitar seção.
- **Tokens temáticos sem autor — confirmados e identificados por contexto (sem arbitrar desenho):**
  PSORIASE_2025 ↔ REF_KEENAN_2025 (existe, PMID 39960105) · PRIMINGPRINC_2018 ↔ REF_HERMAN_2018
  (existe, PMID 29902514) · STRESS_EPI_2019 **sem ficha candidata** no acervo · e variante nova do
  mesmo defeito: **duas grafias de token para a mesma ficha** (Quimio82_2017 × Quimio_meta82_2017;
  candidata REF_KOHLER_2017 por desenho↔escopo, confissão da mesma margem da L717).

**NÃO feito (fronteira, mesma disciplina do §3):** nenhum classificador [XX] tocado. Correção material
dos 11+1 tokens e dos 3 temáticos (unificar namespace: temático sai do espaço de nomes de referência)
fica no **L-05/1.2 com V-15**. Dívida incrementada: **D-B1-R4-TOKENS** = 11 ambíguos + 3 temáticos +
2 grafias-duplas (STEINER, QUIMIO) — itens e linhas exatos na trilha 24 rev.1.

**Aceites registrados dele:** V-15/V-16 entram na fila de portões do lado dele · B13 = primeira
execução do reancorador (a escrever ANTES) · camada de evidência encerrada · AUD-066 encerrado.

**Portões pós-errata V-16 (computados 2026-09-13):** gate rev.A2 **APROVADO** exit 0 · checklist
**41/41** · framework **0 ERRO**/236 AVISO · **P-8 0 ERRO**/26 AVISO · censo série **32/32 BLOQ 0**
(B01 274/237, 11 avisos 'legado' = D7). **Suíte V7 + manifesto 2.9 totalmente verde.**

## Rev.9 — 2026-09-14 (auditor de ESTRUTURA: proposta L-05 v1.0 — réplica trilha 25; errata T25)

**Entrada:** proposta L-05 v1.0 (schema evidência Nível 1 + vínculo multi-entidade Nível 2), submetida
como PROPOSTA não-normativa com mapa de migração medido.

**Réplica (trilha 25, contra o acervo real):** 14 dos 16 alvos **exatos** (244/274 no enum clínico;
30×30×30 B1_v2↔/v2; 66/6/2/133/30 evid_role; 175 desenhos brutos; 20 redirecionados; 165 G3_IA;
162 status compostos; 50 origem compostos; forca_biologica 274/274; 0/237 desenhos no enum; simulação
de migração fecha só com os 30 B1_v2 pendentes; 0 ids fora do catálogo). 2 com correção de precisão:
(a) secao_origem não é "21 valores" — são **92 em 3 formatos** (232 BLOCO-puro / 30 prefixados / 12
APENDICE_CORPUS), com a tese qualitativa confirmada (274/274 dentro da B1); (b) o "1 verification
inválido" não era a dívida full-text (essa mora nos vínculos): era **REF_OSIMO_2019** com valor-livre
typado que a própria casa escreveu na C3 — **errata T25 aplicada** (→'verificado'; backup; manifesto
2.9→2.10; irmãos auditados; portões verdes de novo). **O schema rodando pegou defeito que 4 portões
oficiais não pegavam** — caso-prova da especificação executável.

**Achado da própria execução (confessado, vira ajuste R3):** após a errata, o allOf E2 do schema
marca Osimo inválida **por falso-positivo de substring** — o avaliador legítimo cita "eutils" como
fonte do abstract na nota-metodológica. A casa ajusta o PADRÃO (âncora/padrão delimitado), nunca o
dado (não apagamos informação legítima para satisfazer regex).

**Decisões da casa (sob delegação científica, com provas documentais):**
D1 → **A** (enum-união + campo `trilha`): o enum clínico é o de GERAÇÃO (PROMPT v4.2 L1440) — o
acervo não derivou, a régua do gate era a trocada; ramo-morto nucleo_causal explicado. Pedido
factual: pointer do "SCHEMA-CLAIM v1.2".
D2 → transitório aceito + **triagem semiassistida** (pubtype/MeSH/bruto) antes da leitura; nunca
sem texto.
D3 → **B1 ANTES de B2, pelos 20 redirecionados** (piloto canônico; motor do Bloco 4 precisa das
âncoras na B1; gradiente mais barato).
D4 → **contornada por prova**: `citacao_confirmada` é DEFAULT TRUE de geração (PROMPT v4.2
L1290/L1313) → deprecated sem remoção; descrição corrigida.
D5 → ampliada: são **TRÊS escopos** (ficha × vínculo × ledger — contrato.py L62 já documenta 2);
renomear agora = breaking 3 scripts + 16 bibliotecas → **declarar os três por escopo no L-05** +
dívida **D-L05-CAMPO-DUPLO** (renomeação no próximo major). `status_auditoria_nota` aceito (162 ★).

**Ajustes pedidos (R1–R6):** R1 invariante principal-única → portão imperativo (V-17?) · R2
_ids_oficiais.json oficial derivado do MD (casa oferece script; **D-L05-IDS-JSON**) · R3 E2 pattern
ancorado (**D-L05-E2-PATTERN**) · R4 migração âncora: normalização de prefixo + 12 APENDICE nomeados.
R5 manual de classificação desenho_estudo (árvore dos 175 brutos; "natureza = material revisto" para
sínteses — caso McColgan 2026) **D-L05-MANUAL-DESENHO** · R6 descrição corrigida de citacao_confirmada.

**Veredito da casa: VIÁVEL (migração mecânica confirmada por simulação) e CORRETO (3-eixos =
decomposição certa; refuta/fronteira preservam negativo; aderente P11/P20/Filosofia) — APROVADO como
base do L-05/1.2 nos níveis 1–2.** Canônica intocada (sha 6e2c2979). Carta-parecer:
_documentos_serie/RESPOSTA_2_AUDITOR_ESTRUTURA_L05_2026-09-14.md (com cópia ao Auditor-Mestre).

## Rev.10 — 2026-09-14 (análise externa de terceiro revisor — "ChatGPT" — sobre o L-05; trilha 26)
**Entrada:** comentário externo (colado pelo operador) sobre a proposta L-05 v1.0 e o parecer nº 2.
**Verificação (trilha 26):** exemplo factual dele confirmado (REF_RAISON_2013 RCT N=60: geral negativo,
subgrupo inflamação-alta com resposta — como na ficha e na canônica); IDs do exemplo no catálogo
(exame_pcr_us/tnfalpha ✔); regra 3.2 citada à letra ("relações declaradas, não posse").
**Veredito da casa: essencialmente certo.** Adotado: **R7** (crédito a ele): `papel` declara relação
temática, NUNCA veredito (proibido inferir eficácia de papel isolado); novo eixo ortogonal opcional
`direcao: sustenta | refuta | inconclusivo | condicional` (+`condicao`); `refuta` sai do enum de
`papel` e vira `direcao` — padrao dos eixos ortogonais (PROMPT L1438). E **D3 refinada**: corte de
consolidação = B1 INTEIRA retroancorada (274) em corte único após shadow 0-erro; os 20 redirecionados
são subetapa operacional, não estado; modelo nunca roda misto; B2 só depois.
**Notas de enquadramento:** ponto 2 dele (principal≠posse) é re-endosso da regra 3.2 já escrita —
adotado como refinamento de redação da definição de `principal` (blindagem contra leitura de motor);
ponto 1 (triagem dos 133) já era a D2 da casa; nomenclatura "acervo de evidências científicas
auditadas" adotada. Sem conflitos com o parecer nº 2; ajustes ficam R1–R7. Adendo:
_documentos_serie/ADENDO_1_PARECER2_L05_ANALISE_EXTERNA_2026-09-14.md.

## Rev.11 — 2026-09-14 (Auditor-Mestre: C4 RATIFICADA + P-8 com V-15/V-16 instalado)
**Entradas:** `RATIFICACAO_C4_V7_2026-09-13 (1).md` (rodada 5 dele) + `validar_coerencia_camadas.py`
novo (16 regras) + mensagem de verificação do V7c.
**C4 ENCERRADA bilateralmente:** ele implementou a regra como escrita e simulou os 3 casos em disputa
(armadilha obesidade+apneia → rebaixada ✔; falso-negativo sem contexto → alta ✔; KYN/TRP presente →
rebaixamento impedido ✔) e leu o §12.3 na íntegra ("foram atrás da circularidade onde ela estava
escondida"). **Impedimentos restantes: P-6 e taxonomia — os mesmos que o plano previa.**
**V7c verificado por ele:** zip/sha ok, 24/24 hashes, canônica inalterada, V-16 4/4, manifesto 2.9
com 201, AUD-066 "encerrado da forma certa".
**P-8 novo (oficial do mestre, 16 regras):** réplica EXATA na casa — V-15: **94 ERRO / 181 AVISO**,
V-16 OK (4/4), demais regras 0 erro; composição da V-15: 19 DENTRO (6 prosa = as 6 autodivergentes
restantes da trilha 21; apêndice = classes herdadas já nomeadas) + 75 ENTRE (o mesmo fenômeno do
71×84 trilha-21/§3) — nenhum não-conforme novo: é a D-B1-R4-TOKENS agora com portão próprio.
**ACHADO DA RÉPLICA (proposta fina ao oficial):** o delimitador `^#{1,3}\s*REGISTRO DE AUDITORIA`
não casa o cabeçalho em **negrito** da canônica (`**REGISTRO DE AUDITORIA 2026-09-11…**`, L1287/1309):
1 ERRO ("Mehta_2020 DENTRO índice", com 2 satélites) vem de tokens citados em NARRATIVA histórica —
exatamente o falso-positivo da trilha 24 rev.0 que ele mesmo invoca na lição incorporada. One-liner
`^(?:#{1,3}\s*|\*\*)` medido: 94→**91**, zero dados tocados. Instalado verbatim com backup
(`.bak_oficial_pre_V15V16_2026-09-14`; sha d41df57d…) aguardando o aceite do ajuste fino.
**Portões pós-instalação:** gate rev.A2 APROVADO · 41/41 · framework 0 ERRO/236 · P-8 16 regras:
94 ERRO (todos V-15, dívida nomeada) / 207 AVISO · V-16 OK · censo a calcular.
**Bloco 1 formalmente destravado dos dois lados.** Próxima entrega da casa: minuta do Contrato do
Motor Clínico (L-05 1.1 — "quais camadas o motor lê") + reancorador de série (B13 = 1ª execução) +
retroancoragem B1 na régua D3-revisada quando a v1.1 do schema (auditor-2, R1–R7) chegar.

## Rev.12 — 2026-09-15 (ARQUITETURA CONSOLIDADA do operador — rodada 9, documental; 0 ciência)
**Entrada:** `ARQUITETURA CONSOLIDADA DA PLATAFORMA.MD` (sha256 `8f050469632ce3e8…`, 37.466 B, 23
seções) via operador, para alinhar o Auditor-Mestre ANTES do arranque do motor. Oficializa a cadeia
**Biblioteca → NT → Ontologia/Grafo → JSONs → Motor → Laudo** + Pasta de Atualização paralela + regra
"necessidade estrutural = problema de contrato, nunca remapear a ciência". Cópia verbatim arquivada em
`_documentos_serie/ARQUITETURA CONSOLIDADA DA PLATAFORMA.MD` (sha idêntico).
**Verificação factual (6 itens computados):** ① "146 IDs" **EXATO** (151 listados − 5
`ids_removidos_definitivo` = 146 ativos: suplementos 48 · exames 71 · mecanismos 16 · cenários 11) —
**ERRATA da casa: o "103" da trilha 25 era parse parcial; o autoritativo é 146/151** ② constantes do
motor já são cabeçalho oficial do catálogo (verbatim) ③ evidência-única/âncora-múltipla corresponde ao
acervo (MOTOR_CLINICO/ 2026-09-11) = 4ª convergência independente ④ relação §10 converge com R7 ⑤
**Pasta de Atualização não existe** (novo componente; contrato L-PU pendente) ⑥ NT não existe; já
prevista como "NT-B1" no Bloco 2 do plano do mestre (contrato L-NT + portão V-NT pendentes).
**Decisões da casa (delegação engenharia, datadas):**
- **D1 enquadre da minuta L-05 1.1:** passa de "camadas que o motor lê da B1" para **Contrato da
  Cadeia** (Biblioteca→NT→Ontologia→JSON→Motor→Laudo), leitura em **dois tempos** — derivação: a
  cadeia lê as 4 superfícies da carta 5 (prosa · fichas+vínculos · manifesto/semantic_layer · ledger
  como filtro de elegibilidade); execução: o motor consome o pacote §16/§20 do documento. Anexos
  exigidos pela arquitetura: **L-NT** (schema da NT) · **V-NT** (portão) · **L-PU** (Pasta de
  Atualização) · L-06.
- **D2 L-06 com fonte normativa:** precedência formal **Biblioteca > NT > Ontologia/JSON > Motor**,
  citando o §21 (cadeia de autoridade) do documento; conflito entre camadas = **ERRO de portão**,
  nunca remapeamento silencioso (§22 aplicado à engenharia).
- **D3 herança de enums:** NT/Ontologia herdam os vocabulários do L-05 1.2-normativo com **R1–R7**;
  **proibido vocabulário paralelo** (lição dos "dois schemas vivos"). **Colisão de nome nomeada:**
  `direção` do §10 (sentido do grafo) ≠ `direcao` do R7 (sentido epistêmico) → propostos
  `sentido_relacao` × `direcao_suporte` no contrato.
- **D4 regras de risco R-A…R-D:** **R-A** enquanto a V-15 medir 94 ERRO, a NT-piloto ancora
  marcadores/classificadores **só via fichas+vínculos** (via 0-erro), nunca via tokens de prosa até o
  1.2; **R-B** piloto multidomínio só com IDs do catálogo (146) — falta de ID = pedido ao catálogo,
  nunca ad-hoc (domínio "intervenções" ainda sem família: abrir pela liturgia quando ativado);
  **R-C** constantes de segurança do catálogo viram cabeçalho normativo de TODO JSON modular e do
  contrato do motor; **R-D** Pasta de Atualização só existe sob L-PU — até lá o motor lê apenas o
  fluxo canônico.
- **D5 piloto (§8 do documento, aceito):** B1 inteira auditada → NT-B1 → Ontologia-B1 → JSONs-B1 →
  motor → teste de raciocínio; sequência bilateral respeitada (taxonomia = 1º item material; B13 = 1ª
  execução do reancorador de série, a escrever antes).
**Material inalterado:** taxonomia = primeiro item material do Contrato; V-15 medindo 94 ERRO (dívida
D-B1-R4-TOKENS com portão próprio). **Ciência: 0 linhas (sha V7 `6e2c2979…` recomputado).** Portões
hoje: gate rev.A2 APROVADO · 41/41 · framework 0 ERRO/236 · P-8 (16) 94 ERRO/207 · V-16 4/4.
**Carta:** `_documentos_serie/RESPOSTA_6_ARQUITETURA_CONSOLIDADA_NT_PRE_MOTOR_2026-09-15.md` (ao
Auditor-Mestre; cópia auditor-2). Pendências: delimitador P-8 (94→91) · v1.1 R1–R7 · minuta 1.1 no
novo enquadre · P-6 permanece.

## Rev.13 — 2026-09-15 (mesma data — ARQUITETURA **V2** substitui a V1; diff verificado)
**Entrada:** `ARQUITETURA CONSOLIDADA DA PLATAFORMA V2 - 15.09.26.md` (sha256 `09692e18a5a65958…`,
46.129 B, 30 seções). **Diff V1→V2 computado linha a linha** (+332 líquidas; 23→30 seções): declarado
("evidências bibliográficas no desenho") confirmado **e ampliado** — diagrama com EVIDÊNCIAS
BIBLIOGRÁFICAS → VÍNCULOS ("L-05 N1 + N2") · §5 reescrita com §5.1/§5.2 citando
`L05/schema_referencia_v1.1.json` / `L05/schema_vinculo_v1.1.json` (o lugar oficial dos schemas do
auditor-2, já na versão pendente R1–R7) · sem pastas físicas por desenho de estudo · **§7 LIMITES DA
NT** (proibições; "não converter relação mecanística em eficácia clínica sem sustentação" — **adotada
como regra do L-NT**) · §23–§25 reescritas limpas (V1 tinha trecho com formatação corrompida; +linha
"vínculos preservam a relação evidência-claim-entidade") · **§26–§29 novas** (piloto B1 · expansão
multidomínio · motor em paralelo CONTRA contratos — Biblioteca não é camada final de consumo · divisão
de responsabilidades sem alteração silenciosa de autoridade entre etapas).
**Decisões (datadas):** (a) **referência vigente = V2**; V1 → `SUPERSEDED_` (sha inalterado) + ponteiro
`ARQUITETURA_VIGENTE.txt`; (b) notas de nome para o contrato: `/Evidencias/Bibliograficas` do doc ×
diretório real `Evidencias/Bibliografia` → adotar o real; schemas v1.0 em mãos × v1.1 citada = entrega
pendente do auditor-2 (cumprir, nada a corrigir); (c) colisão `direção`-grafo (§11) × `direcao`-epistêmica
(§5.2 — coincide com R7 ✔) persiste → mantida a proposta `sentido_relacao` × `direcao_suporte`;
(d) minuta 1.1 passa a citar a V2 (§2/§5/§7/§22/§25/§26–§29); (e) demais decisões da rev.12 permanecem.
**Ciência: 0 linhas** (sha V7 `6e2c2979…` recomputado). **ADENDO 1 à carta 6** publicado
(`_documentos_serie/ADENDO_1_RESPOSTA6_ARQUITETURA_V2_2026-09-15.md`).

## Rev.14 — 2026-09-15 (auditor-2: L-05 **v1.1** recebida + transmissão da V2; trilha 27)
**Entradas:** `schema_referencia_v1.json` + `schema_vinculo_v1.json` (conteúdo **v1.1**: `$id
L05/schema_*_v1.1.json` = caminhos exatos citados na V2) + proposta MD com CHANGELOG v1.0→v1.1 +
ERRATA (3 erros dele) + §7/§8/§9 novas. Verbatim em `_documentos_serie/L05_v1.1_recebido_2026-09-15/`.
**Réplica (trilha 27, tudo em cópia):** R1-contraproposta **`ancora_principal`** — invariante
"exatamente-1" eliminado por construção; simulação 274/274 ∈ catálogo → **ACEITA, e aposenta o V-17
para este item** (melhor que portão) · R2/§7: derivador reproduz **146** batendo
`contagem.total_ids_validos` (L282) + famílias — critério de aceitação dele atendido · R3/§8: ancorado
**0 FP** em 511 campos (substring morde só Osimo); gate rev.A2 confirmado substring → **proposta
rev.A3-E2 ao mestre (liturgia inversa)** · erratas dele: 92/3 EXATO; Osimo já corrigido (T25, hoje 0
inválido) — pedida 1 linha de rodapé na §4B · §9: kit trilha clínica **ausente do repositório** —
tesse dele confirmada pela ausência; **pedido formal ao operador dos 5 documentos**.
**Migração simulada:** N1: pendências = 30 review (exato) + desenho 40 sinal-forte/**197 leitura** +
origem 49/50 (Osimo → 1 linha de mapa `AT_AUDITORIA_EXTERNA_* → AUDITORIA_EXTERNA`, proposta casa) +
status 162/162; N2: **243/274 integrais**; uso/trilha 30 exatos; **`direcao`: triagem PROPOSTA casa** —
sustenta quando status ∈ {CONFIRMADO, PARCIALMENTE_CONFIRMADO} (273), exceção única **VINC_B1_0047**
(= o mesmo já nominado à fila P-6/full-text: a fila humana engole o não-triável); `forca_biologica`
BLOCO_07/08 = **24** (backlog de portão); enums vigentes 100% cobertos → zero remapeamento semântico.
**Veredito: v1.1 APROVADA como base do L-05/1.2-normativo (níveis 1–2).** Decisão 1 encerrada na
prática (Opção A implementada com `trilha`); D4 encerrada bilateralmente; D5 aceita (3 escopos +
dívida). **Perguntas abertas à v1.1 (1 linha cada):** papel principal `sustenta_mecanismo` + fronteira
nos 20 redirecionados · triagem `direcao` transitória datada · colisão `direção`-grafo (V2 §11) ×
`direcao` (schema) → proposta `sentido_relacao` na ontologia · rodapé §4B. **V2 transmitida ao
auditor-2** (pedido do operador) com pontos de encaixe: $id = §5.1/§5.2 V2 · nome real `Bibliografia`
· §7 V-NT sobre seus enums · L-PU sinalizado · piloto §26–§29.
**Ciência:** 0 linhas; simulação integralmente em cópia (trilha `producao/27_*` com shas dos 3
arquivos). **Carta nº 3:** `_documentos_serie/RESPOSTA_3_AUDITOR_ESTRUTURA_L05_V11_ARQUITETURA_V2_2026-09-15.md`
(cópia ao Auditor-Mestre).

## Rev.15 — 2026-09-15 (parecer do mestre sobre a V2 + resposta externa; trilha 28; V-15 reescopada)
**Entradas:** `PARECER_ARQUITETURA_V2_2026-09-15.md` (audita o arquivo V2 — sha confere; decide §1:
tokens editoriais fora do caminho do motor por V2 §28; V-15 → aviso-na-prosa/erro-em-ficha-vínculo; §4
nomeia D-01…D-08) + resposta do ChatGPT ao parecer (colada pelo operador para envio ao mestre).
**Decisão do operador:** carta nº 3 ao auditor-2 fica **EM ESPERA** até a V2 estar resolvida
bilateralmente; depois sai V2 + análises dos schemas no mesmo envio.
**Verificação (trilha 28, P-8 fresco):** §28 verbatim ✔ · D-07/D-08 ausentes da V2 (grep 0) ✔ · 94
ERRO = 19 DENTRO (6/1/12) + 75 "divergente entre camadas", **0 conteúdo de ficha/vínculo → 100%
viram aviso sob o novo regime** · 3 tokens-exemplo sem ficha ✔ · 158/405 dele **não reproduzidos**
(casa: 446 tokens distintos, 675 [XX], método declarado) — pointer pedido. Confissão rev.1: regex
MAIÚSCULA na 1ª leitura; msg "entre" minúscula — corrigido no ato (padrão FP trilha-24).
**Decisões da casa (datadas):**
- **D-B1-R4-TOKENS reescopada:** tokens de prosa = convenção editorial (higiene, sem bloqueio) ·
  taxonomia autoritativa migra p/ campos da v1.1 (desenho/natureza/força) — trabalho medido: 197
  desenhos · 30 review · 24 forca_biologica · manual D-L05-MANUAL-DESENHO. Quando normatizar, V-15
  modo-erro vigia ficha/vínculo. Errata do delimitador (94→91) mantida e pedida (só muda rótulo).
- **Restrições externas ADOTADAS com crédito:** **D-01** — proibido hierarquia artificial entre
  mecanismos; L-06 = **escada de discriminação em 7 passos** + "preservar concorrentes + lacuna" quando
  irresolúvel (determinismo pela escada). **D-02** — veto a escalar único; **solução da casa: piso POR
  EIXO** — saída carrega vetor (natureza×desenho×forca_causal/tier×grau_maturidade×trilha), cada eixo
  teto no elo mais fraco, laudo nomeia elo limitante (computável e sem falsa equivalência; usa campos
  que a v1.1 já tem).
- **NT:** campo **`status_epistemologico`** adotado (7 valores) — fecha a exigência do ChatGPT com o
  adendo técnico do mestre (distinções só verificáveis se enum) · `sentido_relacao`=3ª convergência do
  nome · template **6 partes por decisão** adotado como padrão de redação da casa · adição D-06 (rastro
  da consulta à Pasta de Atualização) ao futuro L-PU.
- **Autoria do 1.1:** mestre redige defaults D-01…D-08 (autorizado); **minuta da casa = bancada de
  verificação** do 1.1 dele — não se criam duas normas concorrentes. Ordens de entrega convergentes
  registradas.
**Ciência:** 0 linhas (sha V7 intacto). **Carta nº 7:**
`_documentos_serie/RESPOSTA_7_PARECER_ARQUITETURA_V2_MESTRE_2026-09-15.md`.

## Rev.16 — 2026-09-15 (minuta L-05 1.1 do mestre verificada na bancada + 4 pontos do comentador; trilha 29; 0 ciência)
- **Recebido:** `L05_1.1_CONTRATO_CADEIA_MOTOR_minuta1_2026-09-15.md` (sha `f91042b7…`, arquivada verbatim
  em `_documentos_serie/L05_1.1_minuta_mestre_recebida_2026-09-15/`) + resposta do comentador externo
  com 4 correções. V2 citada (sha `09692e18…`) confere; V7 intacta (`6e2c2979…`).
- **Parte 0 (reconciliação de números): REPRODUZIDA EXATA pela casa** — 102 linhas-lote · 405 prefixos
  distintos · 247 resolvem / 158 não-resolvem (por prefixo, 1º segmento maiúsculo × substring em
  `id_referencia_interna`) · os 158 são de fato temáticos. **Pointer "158/405" da rodada 12 ENCERRADO
  por réplica** (precedente 71×84). Aceite do delimitador 94→91 por ele registrado.
- **ERRATA DA CASA (confessada):** o "446 tokens" da trilha 28 **não é rederivável** — a trilha não
  gravou regex/comando; grade completa hoje dá 474 (regex dele, g1+g2) / 477 (regex do P-8) / 675 [XX]
  exatos. Sem efeito material (V-15 é por item), mas a norma passa a ser: **medida sem comando gravado
  não vale** — regex+escopo+chave+sha no mesmo registro (lição aprendida da Parte 0 dele).
- **Verificação contra os schemas v1.1 (shas `737bcda8…`/`b0934412…`):** (a) eixos da D-02 existem em
  enum fechado mas divididos — `natureza_evidencia`+`desenho_estudo` na ficha N1, `forca_causal`+
  `grau_maturidade`+`trilha` no vínculo N2; (b) D-01 §3: `contexto` e `sentido_relacao` NÃO existem
  como campo; o epistêmico real chama-se `direcao` → **dívida nova D-L05-NOMES-DIRECAO** (resolver na
  etapa de schema: rename ou dicionário); (c) âncora formal p/ lacuna: `natureza_relacao` já tem
  `nao_estabelecida` → `inexistencia_cientifica` fica machine-verificável.
- **4 pontos do comentador verificados e ADOTADOS com crédito:** D-02 sem vetor homogêneo (corroborado
  pela divisão N1/N2) · D-03 `inexistencia_cientifica` restrito (adoção + âncora formal) · D-07
  determinismo = conteúdo clínico/semântico/estrutural + conjunto de versões, envelope técnico em
  lista fechada fora do hash · Parte 1 "As entradas autorizadas do Motor são:" **com a condição da
  casa:** manter verbatim o "Não consome: a prosa (§28)". Não se reabre D-01/D-04/D-05/D-06/D-08.
- **Decisão da casa:** **minuta 1 APROVADA como base do contrato normativo** com as 4 correções + 3
  precisões fáticas (F-1 campos D-01 · F-2 origem N1/N2 dos eixos · F-3 nomenclatura) — sem reabrir
  semântica. Contribuição própria: semântica por eixo (tabela na carta nº 8 §7) — `trilha` é metadado
  preservado, não ordenável (nova falsa equivalência evitada).
- **Filas mantidas:** P-8 nova versão (aviso/erro, prometida por ele) · kit da trilha clínica com o
  operador · carta nº 3 ao auditor-2 EM ESPERA até a V2 fechar neste eixo (ordem do operador).
- **Adendo à carta 8 (mesma data):** o mestre registrou não ter recebido os schemas v1.1 citados na
  verificação. **Origem confirmada: são do auditor de estrutura (rodada 11), arquivados verbatim com
  shas** — a citação na carta 8 é proposital e atribuída (bancada verifica contra o artefato; a
  própria minuta invoca "a v1.1 já os tem"). Causa-raiz do F-1 diagnosticada: minuta escrita sem os
  arquivos. Publicado `ADENDO_1_RESPOSTA8_ORIGEM_SCHEMAS_V11_2026-09-15.md` com inventário, guia de
  leitura para a minuta 2 e shas — kit para o operador repassar ao mestre.

## Rev.17 — 2026-09-15 (minuta 2 normativa + P-8 em regime por camada VERIFICADOS; eixo V2 fecha; trilha 30)
- **Recebido e verificado:** minuta 2 (sha `54ba243d…`, verbatim arquivada) + P-8 nova versão (sha
  `0e67328e…`, verbatim arquivado). V2 (`09692e18…`) confere; V7 intacta; 0 ciência.
- **Minuta 2:** diff 1→2 lido na integra (268 linhas) — **0 mudança silenciosa de semântica**; as 4
  correções do comentador, as 3 precisões da casa e o Anexo A (idêntico à carta 8 §7) incorporados;
  duas melhorias espontâneas dele com crédito: teste adversarial da D-03 e lista fechada da D-07 sob
  errata datada.
- **§0.3 replicado EXATO no dado:** natureza_evidencia 0/237 (ausente) · desenho 237/237 · forca_causal
  274/274 · grau_maturidade 274/274 · trilha 0/274 (ausente) · natureza_relacao 274/274 com
  nao_estabelecida 4× exatamente em VINC_B1_0028 e VINC_B1V2_0197/0198/0202. "O dado é mais restritivo
  que o schema" — leitura correta.
- **P-8 novo regime medido e ADOTADO como oficial:** diff = só o prometido (delimitador negrito
  94→91 · dentro/entre ERRO→AVISO [editorial] · bloco novo dos 5 eixos D-02 N1×N2). Execução oficial:
  **2 ERRO / 298 AVISO / exit 1**; decomposição 18dentro+73entre=91 editoriais (94→91 por medição
  independente) + 181 sem-ficha + 26 fora da V-15; B/A gravado (antigo 94/207). Backup
  `.bak_oficial_pre_REGIME_CAMADAS_2026-09-15`; evidências `producao/p8_regime_camadas_oficial_*` e
  `p8_BA_regime_anterior_2026-09-15.json`. **Corredor vermelho por desenho** até a migração criar
  `natureza_evidencia` (fichas) e `trilha` (vínculos) — os 2 ERRO são a régua da D-02, não defeito.
- **Harmonização registrada (sem errata):** portão conta 3/5 (não-vazio) × minuta "2 plenos + 1
  parcial" (curadoria) — preenchido ≠ normatizado; desenho_estudo só é pleno após manual + 197 leituras.
- **Fechamento bilateral do eixo V2:** zerado (minuta 2 ✔ · P-8 ✔ · pointer 158/405 ✔ · delimitador ✔).
  **Carta nº 9 ao mestre publicada** (`RESPOSTA_9_MINUTA2_E_P8_REGIME_CAMADAS_2026-09-15.md`).
  **Carta nº 3 ao auditor-2 DESTRAVADA pela ordem do operador** — dispara com V2 final + análises dos
  schemas v1.1 (trilha 27) e trilhas 28–30 como prova de método.
- **Filas que permanecem:** kit da trilha clínica (5 docs, com o operador) · P-6 (fim) · dependências
  Parte 4 da minuta (taxonomia 197/30/24/manual · campos novos · status_epistemologico · D-L05-NOMES).
- **Despacho ao auditor-2 (mesma data):** carta nº 3 ganhou nota datada de **fecho** (§6: contrato do
  Motor aprovado — fala a língua do v1.1 dele; P-8 novo régua 2 ERRO/298 com os 2 campos v1.1 ausentes;
  âncora de lacuna `nao_estabelecida` machine-verificável; colisão de nomes resolvida como proposto).
  Pacote montado em `_documentos_serie/ENVIO_AUDITOR_ESTRUTURA_2026-09-15/` (carta + V2 + trilhas
  27/30 + LEIA-ME com shas). Carta atualizada: sha `17ad73d3…` (mesmo da cópia do pacote).
- **Esclarecimento do operador (mesma data):** os dois Claudes não se conhecem; quatro IAs no projeto
  (mestre · estrutura · comentador externo — incl. rascunho da V2 a pedido dele — · casa) + operador
  como ponte e decisão. Casa respondeu e formalizou em
  `_documentos_serie/MAPA_DE_AUTORIDADE_E_COMUNICACAO_2026-09-15.md`: **schema ≠ Motor** (contratos de
  camadas distintas da cadeia, encaixe já medido) · manter conversa **por artefatos via ponte** (a
  separação foi o que achou os erros reais) · proveniência da V2 registrada (rascunho externo
  adotado após verificação — autoria não dispensa medição).
- **4ª frente revelada (mesma data):** Claude 3 (free) = ferramentas de NT/anamnese. Parecer de
  engenharia da casa, adotado no MAPA: **sem segundo Motor** (fase de contrato; duas normas vedadas;
  free não sustenta trilha reproduzível — "medida sem comando gravado não vale"; differential
  testing vale em implementação, não em spec) · seu papel comparativo é o da D-05 (**revisor cego**,
  ≥90% nos 3 testes) · NT/anamnese é a camada sem dono → ele permanece nela; importam-se artefatos,
  nunca conversas. **Kit clínico cobrado de novo: operador envia agora (causa-raiz §9 + régua do 1.2
  + tipagem D-08).**

## Rev.18 — 2026-09-15 (L-06 minuta 1 + P-8 harmonizado, verificados; trilha 31; 0 ciência)
- **L-06 minuta 1 (sha `3b6a15a0…`, verbatim): APROVADA como especificação executável da D-01.**
  Parte 6 replicada: natureza_relacao 274/274 com a matriz 1.2 EXATA (109/100/56/4/4/1) ·
  grau_maturidade 274/274 · contexto/sentido_relacao/nivel_cadeia 0/274 ✔ · **errata fina:**
  `condicao` no acervo é AUSENTE (não "esparso"; ancoras[] 0/274 — esparso só no schema v1.1) ·
  **nota de precisão:** degrau 5 já parcialmente executável (`verification_status=extrapolado`,
  62/274). Coerência total com a minuta 2/V2: gatilho por natureza/sinal (nunca por força —
  fronteira D-02) · **Parte 3 escada_degradada aprovada** (degrau indisponível não resolve nem conta;
  multifatorial rebaixa p/ conflito_nao_resolvido+motivo) · Parte 4 alinha com D-07 (sem propagação
  entre pares = fim da precedência emergente) · T-9/T-10/T-12 prendem o invariante.
- **P-8 harmonizado (sha `76e526cf…`, verbatim):** dupla via (cópia × reconstrução) byte-idêntica →
  diff = SÓ o bloco da carta 9 §4. Execução oficial: **2 ERRO / 299 AVISO**; V-15 272→273 avisos;
  linha OK em dupla leitura (com dado 3/5 × normatizados 2/5) — reconciliada a divergência de
  nomenclatura. Adotado como oficial; backup `.bak_oficial_pre_HARMONIZACAO_2026-09-15`.
- **Kit clínico — regra de envio registrada:** o operador envia para a casa E para o mestre (a ponte);
  a casa arquiva/mede e devolve guia+shas; o mestre recebe os MESMOS bytes. Casa não envia direto.
- **Carta nº 10 ao mestre** (`RESPOSTA_10_L06_MINUTA1_E_P8_HARMONIZADO_2026-09-15.md`).

## Rev.19 — 2026-09-15 (nota do comentador externo sobre o P-8: 3 pontos replicados e adotados; trilha 32; 0 ciência)
- **Decisão de fluxo:** a nota crua do comentador NÃO circula (norma da bancada: réplica antes de
  aceitar). Os 3 pontos **verificados** seguem na **carta nº 11** ao mestre, com crédito.
- **Ponto 1 (V-06) — ADOTADO com atenuação:** código (L446-448 "Heurística de deriva"), severidade
  (só AVISO) e mensagem ("possível correção não propagada") já estavam corretos; defeito real =
  TÍTULO L20 "COERÊNCIA SEMÂNTICA" + cabeçalho L445, que contradizem a §FILOSOFIA L32 ("NÃO julga
  verdade científica — G3/humano"). Ação: retítulo + declaração — superfície textual, 0 comportamento.
- **Ponto 2 (V-08) — ADOTADO com reforço factual:** escopo "mesma linha" confirmado (L520); já AVISO
  puro e a mensagem já confessa o escopo. **F-C1 medido:** 6 ocorrências atuais = 5 prosa de
  governança (artefato_rotulo · literalidade 100% · R11 · C3/AUD-051 · trilha 21) + 1 substantiva
  (TSPO-PET 18%). Lastro estrutural permanece V-01/V-04/V-05. SEM mudança de mecânica.
- **Ponto 3 (V-07 related_entities) — ADOTADO, mais grave que o enunciado:** **F-C2:** o ramo é
  `rel.erro` (L498) — furo na superfície BLOQUEANTE; contraexemplo executado (B16→ID falso, 15
  itens: contagem SILENCIA, conjunto DISPARA). **F-C3 (auditoria dos irmãos):** `clinical_domains`
  na mesma regra já compara CONJUNTOS; related_entities é o ÚNICO teste cardinalidade-sem-identidade
  do portão. Medido no dado real (mesmo regex/chave/escopo): 15×15, conjuntos IDÊNTICOS → reforço
  preventivo, marco natural = antes da ingestão B2…B16. Aceite da revisão: totals idênticos
  (2 ERRO/299/exit 1) + V-14 verde + backup/B-A gravados.
- **Carta nº 11 ao mestre** (`RESPOSTA_11_P8_PRECISOES_NOTA_COMENTADOR_2026-09-15.md`) · trilha 32 ·
  **0 ciência** (canônica V7 `6e2c2979…` intacta; script oficial `76e526cf…` intacto nesta rodada).

## Rev.20 — 2026-09-15 (kit clínica recebido: arquivo verbatim + medição × B1 V7; trilha 33; 0 ciência)
- **7 documentos arquivados byte a byte** em `_documentos_serie/KIT_CLINICA_recebido_2026-09-15/`
  (Protocolo v1.3 · Schema-Claim v1.2 · Como Executar v1.7 · Lista SM-02 v1.3 · Bloco de Estado v1.6 ·
  Estrutura Mestre v2.1 · Texto Explicativo) com **digitais públicas** (`DIGITAIS_KIT_2026-09-15.txt`).
  É o kit MANUAL da camada atômica (claims G1/G2/G3, SM-02, esquema de 35) — a origem do projeto
  (2026-08). Item 1º (`_ids_oficiais.json`) **não veio** — pendência nomeada.
- **Resposta medida à pergunta do operador ("a B1 já tem os achados?"): PARCIAL.** 49 PMIDs únicos
  sustentando 22 claims aprovados: **10 (20,4%) em V7 · 39 (79,6%) ausentes**; integral 4 · parcial 4 ·
  zero 14. **Wiring formal claim→biblioteca: 0** (V7 usa namespace `B1.MEC.BLOCOxx.nnn` × kit
  `B1.SM02.*`; `usado_em_biblioteca: nao` em 22/22). Das 92 rejeitadas PRISMA, 1 está na V7
  (GARCIAGARCIA_2022 — coerente só se usada como intervenção). 3 fichas V7 têm destino de realocação
  no kit (HOWREN/SUBLETTE/YANG). Conteúdo de área existe; achados-curadoria (QUIN-LCR·maus-tratos·
  S100B/sTREM2/GFAP·complemento) não (trilha 33, K1–K7 com comandos gravados).
- **Esclarecimento "produzido separado?"**: por design, **NÃO** — o kit ALIMENTA a biblioteca
  (claim→evidência→narrativa; `usado_em_biblioteca`↔`claim_id_origem`). O "separado" é ESTADO
  (duas linhas de claims sem fio), não decisão. Separados por decisão: contratos do Motor, NT, PU,
  anamnese clínica (L-NT futuro).
- **Destravamentos registrados:** §9-`uso` (kit já tipifica uso/evidence_role/trilha/comparador =
  material dos 2 ERRO do P-8) · régua 1.2 (duas linhas medidas; `evid_role=review` fora do enum do
  kit = a dívida das 30 fichas) · D-08 (moderadores.regra_motor já em linguagem de motor) ·
  **piloto L-06: 2 candidatos reais oferecidos** (disposição 33339712/30696814 · C1q Luo×Yao&Li em .013).
- **Estado interno do kit (medido, sem bloqueio):** BLOCO cabeçalho×corpo (13×22; .017 sem entrada;
  TAB 69 linhas; `fontes_rejeitadas` redividido) · LISTA (aprovados 13×15; .008/.012/.013 aprovadas e
  alvo ao mesmo tempo; enum com capitalização errada; .013b mal indentado) · disposição dupla
  20132991 · conflito 33339712/30696814 aguarda humano · ausentes: `_ids_oficiais.json`,
  `CANDIDATOS_IDS_OFICIAIS.yaml`, `Estudos que não foram escolhidos.md`. Repartição: Mestre=contratos;
  operador=produção/P-6; casa=guarda e réplica.
- **Guia de envio publicado** (`GUIA_ENVIO_KIT_CLINICA_AO_MESTRE_2026-09-15.md`): operador repassa os
  MESMOS bytes + digitais ao mestre. **0 ciência.**

## Rev.21 — 2026-09-15 (parecer de engenharia: projeto dedicado de claims — parecer, portões, escopo; 0 ciência)
- **SIM à frente dedicada paga** (alinhada ao "Modo B — Projeto" do próprio COMO EXECUTAR) · **NÃO ao
  Claude 3 free para G3** (abstract longo + trava) · **premissa corrigida:** claims → artefatos do
  kit (schema v1.2 estável); fontes → fichas Módulo 09 (schema em migração — NÃO fichar até o
  1.2-normativo); narrativa consome via usado_em_biblioteca.
- **4 portões prévios:** ressincronizar Bloco (13×22, .017) · decidir 33339712/30696814 + 20132991 ·
  `_ids_oficiais.json` vigente (digitais: casa publica) · repassar pendências ao mestre antes
  (régua 1.2 define a costura SM02×MEC).
- **Oferta registrada:** validador executável Schema-Claim v1.2 (lint TAB/dupe/enum/ressalva) +
  trilha por leva — pendente de "vai" do operador. **0 ciência.**

## Rev.22 — 2026-09-15 (complementos do kit: IDS verificado idêntico; CANDIDATOS verificado; trilha 34; 0 ciência)
- **Pendência `_ids_oficiais.json` FECHADA:** o `1º IDS_OFICIAIS.md` enviado é **byte a byte idêntico**
  ao catálogo em uso (sha `f3a74fbc…` · 146 válidos · 5 removidos, L237/280/282). Operador confirmado
  por medição: "é o mesmo das bibliotecas". **Digital publicada para a frente de produção:** esse
  mesmo sha. Nota: o `.json` da era-kit é derivado; a dívida **D-L05-IDS-JSON** (derivador oficial
  da casa) permanece e passa a alimentar também a frente de claims.
- **Pendência CANDIDATOS FECHADA:** recebido (sha `556bb82d…`), arquivado verbatim. 12 candidatos ·
  **0/12 no catálogo** (regra do kit reverificada) · NLR e S100B `em_avaliacao` com acao_pendente
  acionável (.008/.012 fechados) · C4_inflamatorios existe (7 itens) · filename diz v1.0 × conteúdo
  v1.1 (renomear no próximo toque) · o próprio ledger documenta as **2 trilhas** (ex.: `B1.SM02.008`
  × `B1.MEC.BLOCO03.002`) — corrobora a dupla linha da trilha 33.
- **"Estudos que não foram escolhidos.md" = referência do próprio BLOCO v1.6** (última linha:
  `nao_escolhidos_arquivo_externo: … 17+ PMIDs catalogados`). Operador não reconhece → pedido:
  enviar se existir; senão confirmar e a casa declara **ponteiro morto nomeado**. Não-bloqueante.
- **0 ciência** (todos os bytes arquivados intactos; nada gerado nem remapeado).

## Rev.23 — 2026-09-15 (L-05 schema: errata §4B verificada; 4 pontos do comentador replicados; trilha 35; 0 ciência)
- **Errata do auditor-2 VERIFICADA:** diff = 1 linha (§4B: verification_status inválido 1→0, REF_OSIMO_2019,
  crédito à T25 da casa). Réplica nos 274 vínculos: zero inválidos ✔. Item (iv) da carta 3 ENCERRADO;
  (i) papel-âncora nos 20 redirecionados · (ii) triagem direcao (273 + exceção VINC_B1_0047) ·
  (iii) D-L05-NOMES-DIRECAO — SEGUEM pendentes (1 linha cada).
- **Comentador externo — 4/4 confirmados na bancada (crédito integral):** (1) refuta ainda no enum papel
  da prosa (L180/183) × R7 no changelog; **ADIÇÃO DA CASA: R1 também não propagado** (principal booleano
  em L168/195/199) — defeito é de PROSA; schemas v1.1 já corretos (papel 5 sem refuta · direcao 4 ·
  ancora_principal presente); (2) integridade ancora_principal não é exprimível em draft-07 nem via
  uniqueItems → colocação no portão (oferta: V-17 com 3 testes, simétrico ao §8 dele); (3) regra
  "nenhum auto-mapeamento acrescenta o que a origem não garante" ADOTADA + **prova da casa: 0/66
  human_clinical com marcador intervencional** (regex gravada) e 6/6 human_experimental de fato
  intervencionais → mapeamento seguro HOJE + guarda de migração com fila de leitura (regime das 30
  review/Decisão 2); (4) status_auditoria N1×N2 = dois vocabulários reais → ADOTADO renomear N1 para
  status_validacao (= Decisão 5 dele).
- **§9 do auditor-2 encerrado pela vida:** kit clínica arquivado com digitais; seu §0 (uso v1.2 244/274)
  replicado; objetos da régua 1.2 medidos (20,4% cobertura · 0 wiring).
- **Critério da casa p/ assinar a 1.2:** minuta 1.2 com diff prosa§3 reescrito + schemas na íntegra +
  §4B atualizado + 3 linhas pendentes; casa replica antes de assinar.
- **Registros:** ponteiro morto "Estudos que não foram escolhidos.md" declarado; frente de claims
  clínicos PAUSADA pelo operador; nova minuta arquivada (sha `1595011e…`), anterior SUPERSEDED_ com
  ponteiro; **carta nº 4 ao auditor-2** (`RESPOSTA_4_AUDITOR_ESTRUTURA_L05_4PONTOS_COMENTADOR…`). **0 ciência.**

## Rev.24 — 2026-09-16 (revisão do mestre do P-8 replicada; 3 pontos instalados como oficial; kit liberado p/ envio; trilha 36; 0 ciência)
- **Resposta do mestre arquivada verbatim** (sha cópia `0cfe820b…`; sha da revisão informado truncado `be48a5ef…` — pedido por extenso). Réplica independente de TODAS as afirmações: baseline 2 ERRO/299 AVISO/exit 1 ✔ · F-C2 no script antigo muda (furo real) ✔ · candidato dispara nomeando os dois lados ✔ · placar inalterado no dado limpo ✔ · V-14 verde "16 regras anunciadas, todas executadas" ✔.
- **P-8 novo oficial:** sha `84fa918d09899d54995ae41d65b0787a7a52888ba6177ce77583483b1124fe8b` (antes `76e526cf…`, aposentado com backup `.bak_oficial_pre_3pontos_R16_2026-09-16`). Escopo do diff = exatamente os 3 pontos da carta 11 (medido: 17 linhas tocadas em 3 hunks; o mestre mediu 24/5 — divergência de contagem, não de escopo; oferecido confronto byte a byte do arquivo dele). Execução pós-instalação: 2 ERRO/299/exit 1 (2 ERRO por desenho intactos, aguardando taxonomia). B/A gravado (passo 7b com correção datada de rótulos do diff: conteúdo idêntico).
- **Notas finas da carta 10 aceitas pelo mestre e REPLICADAS pela bancada:** `condicao` preenchida 0/274 (ausente, não esparso) · `extrapolado` 62/274 (degrau 5 da L-06 com meia perna: "gatilho + degraus 1, 6 e metade do 5") → minuta 2 da L-06.
- **Kit clínica AUTORIZADO ao envio** com o arranjo clássico (bytes idênticos + digitais públicas): 9 arquivos + DIGITAIS/ADENDO1 + GUIA + **ADENDO_1 novo** (item 1º resolvido sha `f3a74fbc…` = catálogo oficial; CANDIDATOS 0/12; ponteiro morto nomeado; escopo: ancoragem/medida, frente de produção segue pausada pelo operador).
- **Fila:** eixo P-8 com pendência ZERO dos dois lados. Registrada Fase 4 — **Contrato das Unidades Narrativas (L-NT)** como próxima do eixo do mestre (D-05; NT-B1). Bancada em paralelo sem colisão: taxonomia (197 desenhos · 30 review/D2 · 24 forca_biologica) · derivador IDS-JSON · rev.A3-E2. **0 ciência** (V7 `6e2c2979…` e manifesto `79d1309a…` conferidos por sha ao fim; manifesto adulterado apenas em teste, sempre restaurado + sha verificado).

## Rev.25 — 2026-09-16 (schemas L-05 v1.2 verificados 9/9; 3 pontos do comentador + obs replicados; 2 adições medidas; trilha 37; 0 ciência)
- **Recebidos e arquivados verbatim** (pasta `L05_v1.2_schemas_recebidos_2026-09-16/`): schema_vinculo v1.2 `19f4f29a…` · schema_referencia v1.2 `b8bcea80…` · análise do comentador `80248f53…`. **Nota:** o ".py" citado pelo operador NÃO chegou — nomeado, aguardando.
- **Incorporação da carta 4: 9/9 verificada programaticamente** (papel sem refuta · direcao_suporte 4v · ancora_principal+V-17 · guarda 0/66 embarcada · status_validacao+alias · R1 ausente · R3 ancorado nos 2 g3 — com confissão datada de um falso negativo meu por caixa-alta).
- **Comentador 4/4 CONFIRMADO:** (1) furo `condicao` com PROVA EXECUTÁVEL (sustenta+condicao passa) + proposta da bancada medida em 5 casos (`then condicao type null` — draft-07 EXPRESSA, fica no schema); (2) sentido_relacao: **0 em dados / 21 em prosa** — adotado retirar as 2 cláusulas; D-L05-NOMES-DIRECAO encerrada do lado L-05; (3) redirecionado_clinico≠fronteira automático: **20 medidos** (17 uso=clinico!) — funde com nossa linha (i): papel pela função na entidade de destino; (obs) rótulo PENDENTE sai com a Decisão 1 registrada.
- **ADICÃO A (bancada) — paradoxo do alias N1:** v1.1 alias required COM enum → v1.2 alias required SEM enum e canônico NÃO-required; **162/237 fichas com composto hoje passariam com o campo limpo vazio**. Proposta: required→status_validacao; alias deprecated com o mesmo enum, fora do required; 162 migram base→canônico, parêntese→status_auditoria_nota.
- **ADICÃO B — superfície de migração quantificada:** N2: required {trilha, ancoras, ancora_principal}×274 + uso 30 ("B1_v2"→leva_origem) + 0 outras; N1: required {natureza_evidencia, desenho_estudo_bruto}×237 + desenho 237 (175 valores) + origem_pipeline 50 + 0 pattern. Finos: regex da guarda perdeu `cross-over` (impacto 0 hoje; restituição preventiva) · forca_biologica BLOCO_07/08 só em prosa (campo 0/274; **24 vínculos** na zona — pedir ponteiro "portão").
- **Checklist de assinatura (rev.23):** schemas ✔ · §4B rodapé conferido 274/274 · falta: prosa §3 (R1+R7) + linha (ii) triagem direcao (273+VINC_B1_0047) + fechos §2/§5/§6/finos. Casa replica a minuta 1.2 e assina se verde. **Carta nº 5 ao auditor-2** · decisoes rev.25 · **0 ciência** (V7 `6e2c2979…` e manifesto `79d1309a…` íntegros).

## Rev.26 — 2026-09-16 (continuação rodada 21: parecer formal do comentador verificado; trilha 38; 0 ciência)
- **Parecer v1.0 arquivado verbatim** (sha `a1935438…`): veredito FAVORÁVEL condicionado (D1–D5 operador + §21). Réplica: 30 review ✔ · RAISON_2013 tem **2 vínculos** (VINC_B1_0128/0173, CONFIRMADO·verificado·clinico — perfil do caso-teste) ✔ · "fila de 1" = VINC_B1_0047 ✔ · **172/102 NÃO reversível** (nenhuma soma simples fecha 102) → **pedido formal do relatório de execução do auditor-2** (provável conteúdo do ".py" faltante).
- **§12/D4 premissa envelhecida (medido):** citacao_confirmada 237/237=true confere, MAS a própria v1.2 registra R6/D4 RESOLVIDO (default de geração PROMPT v4.2 L1290/L1313; DEPRECATED; 0 ocorrências no gate rev.A2) — dívida de proveniência encerrada; sobra formalizar o destino (D4 operador).
- **§13 × D-L05-IDS-JSON (a casa assume):** parse ESTRUTURAL do catálogo = 146 exatos (48+71+16+11, 5 removidos); grep de texto instável (74×103×…) porque suplementos não têm prefixo — demonstração empírica do bloqueador §13. Derivador estrutural + sha = dívida da casa, reforçada externamente. (Correção datada V4b na trilha 38: primeira regex subcapturou.)
- **Convergências registradas:** §7 papel≠eficácia JÁ no schema v1.2 (falta contrato do Motor/prosa) · §19 regra transversal adotável (sugerida § própria na 1.2 + rebatimento no Motor) · §9/§10 sustentados por medida (30 "B1_v2").
- **ADENDO_1 à RESPOSTA 5 ao auditor-2** · decisoes rev.26 · **0 ciência** (RAISON citado só por status; V7/manifesto íntegros).

## Rev.27 — 2026-09-16 (continuação 2 rodada 21: resposta pós-JSON do comentador verificada; trilha 39; 0 ciência)
- **Cronologia corrigida (operador):** parecer §1-§24 = PRÉ-JSON · análise 3 pontos = intermediária · esta = PÓS-JSON. Explica a premissa envelhecida do §12 (trilha 38); §2.6 daqui já correto.
- **Veredito dele (fechamento, não reestruturação) confirmado pela bancada:** nada mediu incompatibilidade N1×N2 (trilhas 37-39).
- **2 pontos NOVOS confirmados com prova:** (a) `pmid_oficial` — pattern admite vazio sempre, sem allOf; ficha humana_observacional+pmid vazio **passa**; bloco de fecho da casa medido em 6 casos (regra só disparará pós-migração: hoje 0/237 vazio, natureza 0/237); (b) description de `uso` "3+3" imprecisa (5 valores: 2+2 exclusivos + 1 comum) — texto oferecido.
- **D3 dele ADOTADO com eco da nossa norma:** 2 descriptions com medição de rodada ("0/66" · "os 20 vinculos") — regra fica, medição vai ao relatório de migração com data+trilha.
- **Convergências:** D1≡Adição A da casa (a nossa com 162/237 + enum-less fix) · D6≡fino 2 (portão, idem) · D5≡Decisão 1 registro · §3.1 V-17 · §6 ciclo ≡ método bilateral.
- **TENSÃO INTERNA NOMEADA:** §3.3 ("solução atual é suficiente") × ponto 1 anterior (exclusividade do condicao) — pedida confirmação explícita; a proposta da casa (5 casos) não depende da resposta.
- **ADENDO_2 à RESPOSTA 5** ao auditor-2 · decisoes rev.27 · **0 ciência.**

## Rev.28 — 2026-09-16 (rodada 22: resposta do mestre — kit ancorado 9/9; diff reconciliado; escopo corrigido; achado da camada; trilha 40; 0 ciência)
- **Kit ancorado pelo mestre 9/9 byte a byte** (nomes mutilados no upload; digitais fizeram o trabalho). Sha da revisão por extenso recebido (`be48a5efa…`, prefixo confere; selagem byte condicionada ao arquivo).
- **Diff reconciliado:** hunks 3 ✔ (confissão dele) · −7 idênticas ✔ · +7 = comentário F-C2 de 6 linhas. **Casa adota as bytes do mestre** (1 sha viva + convenção do próprio arquivo + norma de memória datada) — critério: anexo chega via operador, diff = só comentário, 2/299/exit1, V-14, F-C2 dispara; backup 84fa918d… na cadeia.
- **Contagens do kit dele: TODAS conferem** após CONFISSÃO datada nossa (regex ancorada subcapturou; o dele = Bloco + chave livre): uso 23 (12/6/4) · comparador 59/8 · moderadores 22 · usado_em_biblioteca 23 · evidence_role 22/22 human_clinical · 43 SM02 × 0 MEC. Convite registrado: comando+escopo viajam com a contagem.
- **Precisão de escopo ACEITA com os nossos números (confissão 2):** acervo 133 preclinical + 30 review + 66 + 6 + 2 → frase do guia §4 corrigida: kit tipifica a SEMÂNTICA dos 2 ERRO; dados só cobrem a fatia humana (163 ficam com taxonomia/Decisão 2).
- **Camada a montante (achado do mestre):** confirmado com medida + ADIÇÃO da casa — o fio foi PROJETADO nas 2 pontas e nunca executado (kit `usado_em_biblioteca` com instrução explícita × M09 `claim_id_origem` 237/237). Decisão = operador (histórico-superado × camada-de-origem-V2); D-03 medida 2 lados: 4 gap_pesquisa × 4 nao_estabelecida/274 (VINC_B1_0028, VINC_B1V2_0197/0198/0202) — "os 4 sobrevivem". Piloto L-06 preferido: C1q Luo×Yao. Fase 4 sem objeção.
- **RESPOSTA_13** ao mestre · trilha 40 · decisoes rev.28 · **0 ciência.**

## Rev.29 — 2026-09-17 (rodada 23: comentário do comentador sobre a resposta do mestre (kit ancorado/diff/camada) replicado; opção (c) registrada; errata fina da rodada 22; trilha 41; 0 ciência)
- **Comentário arquivado verbatim** (sha `79f01bbe19d95e9bbec2de8a3cbbe681d2642e5f279080ae6e0e345f4ca5ede5` · 192 linhas · 9 seções), pasta `COMENTADOR_kit_arquitetura_recebido_2026-09-17/`. Nota crua NUNCA circula — pontos verificados viajam na carta da casa com crédito.
- **§1/§2 (aceites):** ancoragem 9/9 encerrada (rodada 22) · reconciliação do diff aceita; pedido dele ("arquivo adotado identificado no registro final") JÁ é critério da casa desde rev.28 (1 sha viva publicada + backup .bak_* + registro aqui).
- **§3 (números do kit) — CONFERE na camada de VALOR em todos os itens; totais citados separados por camada (comandos gravados, trilha 41):**
  - uso: campos com valor válido **22** (12 clinico/6 contexto_mecanistico/4 gap_pesquisa); o "23" citado reproduz na camada "chave com ':'" (22 + **1 espúria de prosa L182**: `papel_geral: "Regra de uso: IL-1β…"`).
  - usado_em_biblioteca: **22 valores, todos "nao"** (0 "sim"); o "23" citado reproduz na camada "palavra" (22 + **1 espúria: comentário L28** do changelog interno, sem ':').
  - comparador: **48 campos / 8 valores** — os 8 valores citados CONFEREM exatos (dist 38/3/2/1/1/1/1/1); o total "59" NÃO reproduz no BLOCO isolado (palavra=58, chave/valor=48); hipótese fechada: 58(BLOCO)+1(placeholder `comparador: string` no SCHEMA-CLAIM)=59 → escopo provavelmente > BLOCO. (A dist que reportamos/ele (38/3/2/…) soma 48, não 59: divergência de contagem pontual, **sem efeito semântico**.)
  - moderadores **22** ✔ · evidence_role **22/22 human_clinical** ✔ · gap_pesquisa **4** ✔ (B1.SM02.003/.006/.012/.012c) · PMIDs: **49 únicos · 10 na V7 · 39 fora** ✔ (nota de método: 30/49 com aspas `pmid: "N"` — parser sem aspas-opcional subcaptura 19/49).
  - claims: **22 blocos** (B1.SM02.015 usa "Claim_id" maiúsculo + indentação TAB/3-espaços — parser case-sensitive perde 1 de 22).
  - **ERRATA FINA da rodada 22 (datada, sem reescrita):** a trilha 40 (M2b) endossou os totais 23/23/59 por camada textual; hoje as camadas ficam nomeadas com linhas e comandos. Nenhuma conclusão muda. Confissão própria desta rodada: 1ª execução da trilha 41 repetiu a regex ancorada já confessada — corrigida antes de qualquer JSON; repositório nunca recebeu número errado.
- **§4/§5/§8/§9 (arquitetura) — confronto com a V2 vigente (sha `09692e18a5a65958bde4545ed6ff804c21c5945411159988654c7664c8a4a4e2`):**
  - "NT consome Biblioteca + Evidências/Vínculos" = redação vigente do §6 da V2 (deveres 1–2) — **o §5/§8 dele bate no texto oficial**.
  - MAS "Evidências = eixo paralelo à Biblioteca" NÃO é o desenho do §2 (diagrama oficial: CATÁLOGO→BIBLIOTECAS→{EVIDÊNCIAS, NT}→VÍNCULOS→…; única "posição paralela à cadeia canônica" no texto = **Pasta de Atualização**). É porém consistente com o **§5.3** (minidiagrama EVIDÊNCIA BIBLIOGRÁFICA→BIBLIOTECA CANÔNICA→NT).
  - **Achado da casa — DÍVIDA NOVA nomeada: D-V2-DIAGRAMA-DUPLO.** A V2 tem DOIS desenhos internos para Evidências (§2 × §5.3) com direções opostas; qualquer decisão de camada precisa da redação única. V2 §5 ainda diz que Evidências "não constituem uma segunda Biblioteca Canônica nem uma fonte… independente" (nuance × "eixo paralelo" do comentador).
  - **Kit: 0 ocorrências na V2** (kit/SM-02/SCHEMA-CLAIM/claim-kit) — INALTERADO em qualquer opção; e **0 menções a "Evidências/Bibliografia" nos .md do kit** — o destino proposto pela opção (c) NÃO está escrito no próprio kit (design aponta p/ M09/claim_id_origem).
  - V2 §5.1 declara caminho `/Evidencias/Bibliograficas` (raiz); disco real: `BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia` (aninhado na B1; nome sem "cas") — divergência texto×implantação nomeada para a decisão.
- **§6 — SUSTENTADO pelo próprio kit:** instrução SCHEMA-CLAIM L87–92 ("usado_em_biblioteca… rastreabilidade de consumo rio abaixo… não bloqueia nada no fluxo G1→G2→G3") + dados coerentes: sim **0/22** casa com claim_id_origem B1.SM02.* = **0/237** (wiring projetado nas 2 pontas, nunca executado — adição da casa, rev.28).
- **§7 — convergência com a D-03 medida dos 2 lados:** 4 gap_pesquisa (kit) × 4 nao_estabelecida (acervo 274: VINC_B1_0028, VINC_B1V2_0197/0198/0202) — ele endossa "permanece rastreável"; compromisso incondicional reconfirmado: **os 4 sobrevivem a qualquer decisão**.
- **DECISÃO DA CAMADA — agora com 3 opções registradas, dona: OPERADOR** (a casa mede; não decide): (a) kit histórico/superado (39 PMIDs à curadoria arquivada) · (b) camada de origem na V2 (contrato do fio claim→biblioteca) · **(c) NOVA — do comentador:** kit = ferramenta de curadoria; produto deposita em Evidências/Bibliografia; sem nova camada e sem contrato claim→biblioteca como condição; rastreabilidade quando houver utilização. Janela do mestre (antes da Fase 4/L-NT) segue aberta. Em todas: D-03 + D-V2-DIAGRAMA-DUPLO a resolver se a escolha redesenhar Evidências.
- **Notas de higiene do kit** (para a decisão, qualquer opção): aspas opcionais em pmid · "Claim_id" maiúsculo (SM02.015) · indentação TAB/3-espaços misturada · chaves em prosa/comentários · placeholder no SCHEMA — medidas com comando gravado na trilha 41.
- **Fila inalterada:** anexo do mestre (P-8 da versão dele — troca pendente) · relatório 172/102 + ".py" (auditor-2) · minuta 1.2 (auditor-2) · derivações caseiras.
- **0 ciência:** selos conferidos no fim — V7 `6e2c2979…` · manifesto `79d1309a…` · P-8 `84fa918d…` íntegros.

## Rev.30 — 2026-09-17 (rodada 24: V2 atualizada pelo operador verificada; trilha 42; parecer FAVORÁVEL c/ 2 correções de formato; decisão de instalação = operador; 0 ciência)
- **Upload novo, mesmo nome** ("…V2  -  15.09.26.md"): sha `5be36836610d26832506b73dac45baa09e7041bc9ce22e6557f2be59b258e06a` (1387 linhas · 50.964 bytes) × vigente `09692e18…` (1351). **Diff: 5 hunks, +112/−76, escopo PROVADO = só §2 e §21** (resto byte-idêntico; comando gravado, diff arquivado `diff_v2_vigente_x_upload_2026-09-17.txt`).
- **O que muda:** topo do §2 sai de CATÁLOGO (prosa §1/§3 preservadas) → `[CIÊNCIA]` · Pasta de Atualização vira eixo paralelo ESPELHADO (Evidências+NT próprias) convergindo em "VÍNCULOS UNIFICADOS" · MOTOR passa a "buscar ativamente" (seta CONSULTA) e recebe **ANAMNESE** (novo bloco DEFINIÇÃO; prosa já existia §§23/24) · tríade de saída vira **MECANÍSTICA / CLÍNICA / TERAPÊUTICA → EXPLICAÇÃO NARRATIVA** → LAUDO (só nos 2 desenhos; **sem prosa — dívida editorial**) · §21 ganha ANAMNESE/CONTEXTO e perde o tridente CANÔNICO/ATUALIZAÇÃO/CONTEXTO.
- **Guarda da Pasta:** parágrafo do §2 ("posição paralela à cadeia canônica") removido, MAS o regime permanece escrito: §18 camada diferente (L891) + não-canônico automático (L920) · §19 não-equivalência no Motor (L966) · §20 "não possuem o mesmo status epistemológico" (L1016). **Preservada, redistribuída.**
- **D-V2-DIAGRAMA-DUPLO AMPLIA → 4 representações:** §2-novo (espelhado/UNIFICADOS) × §21-novo (linear/Pasta externa) × §20 (EVIDÊNCIA→BIBLIOTECA, a montante) × §5.3 (idem, inalterado). **§2 e §21 dividem o MESMO título "ARQUITETURA MULTIDOMÍNIO COMPLETA" com desenhos diferentes** (e o §2 repete o rótulo "# 21." na linha 45). Direção normativa diverge: prosa (§5.3/§20) = evidência a montante; desenhos gerais (§2/§21) = a jusante. Sugestão da casa: declarar UM canônico e rebatizar os demais. (Contexto: o comentador da rodada 23 fica apoiado pela prosa na direção, não na topologia completa.)
- **Higiene a corrigir (formato, 0 semântica):** fence do §21 indentado 4 espaços (não-fence em markdown) e SEM fechamento (60 fences ^``` pares + 1 indentado) → render quebrado do desenho; + o rótulo "# 21." dentro do desenho do §2.
- **Kit: 0 ocorrências no novo texto** — atualização NÃO decide a camada; **(a)/(b)/(c) continuam com o operador** (janela do mestre antes da Fase 4 segue aberta).
- **Motor consulta-ativa:** coerente com §19 (prosa "deverá consultar a Pasta"); o §21-novo desenha JSONs→MOTOR sem a seta de volta — reforça o pedido de canônico único.
- **Parecer da casa: FAVORÁVEL à instalação** com as 2 correções de formato (nota datada) + dívidas nomeadas (unificar desenhos; prosa da tríade). **Proposta de versionamento:** instalar como **"…PLATAFORMA V2.1 - 17.09.26.md"**, anterior 09692e18… → SUPERSEDED_ + ponteiro, ARQUITETURA_VIGENTE.txt com a nova sha. 3 opções apresentadas ao operador no chat (instalar c/ correções · instalar bytes exatos · segurar p/ unificar desenhos).
- **Fila:** anexo do mestre (P-8) · relatório 172/102 + ".py" (auditor-2) · minuta 1.2 · comunicar V2.1 ao mestre após instalação (operador repassa). **0 ciência** (trilha 42 = leituras/diff; acervo intocado).

## Rev.31 — 2026-09-17 (rodada 24, continuação: V2.1 INSTALADA como vigente por decisão do operador [opção A]; trilha 43; ADENDO_2 ao mestre)
- **Decisão do operador (2026-09-17):** instalar com as 2 micro-correções de formato (opção A) + comunicar ao mestre.
- **Instalação executada:** vigente = "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.1  -  17.09.26.md", sha **`1a50645e260984ab7b78b95abc177bdb171203f55f22990c195e5cefa0a94b60`** · upload exato `5be36836…` · anterior `09692e18…` → SUPERSEDED_ · ponteiro `ARQUITETURA_VIGENTE.txt` reescrito (cadeia V1→V2→V2.1). Diff upload→instalada = exatamente 4 linhas (linha Rev. V2.1 datada + rótulo §2 "# 2. …(MAPA EXECUTIVO)" + fence §21 desindentado + fechamento "```"), CRLF preservado.
- **CONFISSÃO datada (trilha 43, passo 1):** 1ª candidata reescreveu fins-de-linha (CRLF→LF, diff cobriria 1.387 linhas); detectada pela verificação de escopo antes da instalação e DESCARTADA (sha morta `c3a22c23…` registrada); refeita com newline=''. Repositório nunca recebeu os bytes errados.
- **Verificação pós-instalação executada (14/14):** kit 0 · fences 62 pares/0 indentados · título "ARQUITETURA MULTIDOMÍNIO COMPLETA" 1× (só §21) · guardas §§18/19/20 4/4 · §5.3 e §20 evidência a montante ✔ · tríade nova 2×/2× antiga 0 · definição anamnese + prosa §§23/24 · Rev. line presente · CRLF íntegro.
- **NOTA adicional à A5 da trilha 42 (datada, sem reescrita):** 5ª representação identificada — §30 SÍNTESE FINAL também desenha a cadeia (inalterado desde a V2). **D-V2-DIAGRAMA-DUPLO = agora 5 representações internas** (§2-novo × §21 × §20 × §5.3 × §30).
- **ADENDO_2 à RESPOSTA_13** para o mestre produzido (anúncio V2.1 + sha + o que afeta a Fase 4: §6 deveres 1–2 intactos = âncora do L-NT; mapas mudaram, prosa não); envio via operador junto dos demais. Auditor-2: não comunicado (eixo L-05 intocado).
- **Pendências atualizadas:** unificação dos 5 desenhos (sugestão: 1 canônico numa próxima revisão do operador) · prosa da tríade MEC/CLÍN/TER · kit (a/b/c) com o operador · anexo P-8 do mestre · relatório 172/102 + ".py" · minuta 1.2.
- **0 ciência** em toda a rodada 24 (V7 `6e2c2979…` · manifesto `79d1309a…` · P-8 `84fa918d…`).

## Rev.32 — 2026-09-17 (rodada 25: pacote do auditor-2 — triagem .py + relatório 172/102 + schemas v1.3 + minuta — e parecer do comentador REPLICADOS integralmente; trilha 44 41/41; 0 ciência)
- **Arquivados verbatim** (pasta `AUDITOR2_triagem_L05v13_recebido_2026-09-17/`): parecer do comentador sha registrado · `triagem_direcao_suporte.py` (colado pelo operador; cópia da casa com sha própria) · relatório 2026-09-16 · schema_vinculo v1.3 (`ec4f0de8…`) · schema_referencia v1.3 (`b06660fd…`) · **minuta normativa 496 linhas** (`fc05f470…`). Nota crua do comentador não circula.
- **O ".py" chegou e a dívida 172/102 está ENCERRADA (réplica executável 9/9):** rodando o script dele aqui: sha256 da entrada idêntico (`490675e6…`) · 274/172/102 ✔ · regras 172/82/19/1 ✔ · fila 102 e automáticos 172 **idênticos por id E por motivo** · RAISON_2013: VINC_B1_0128/0173 ambos `__PENDENTE__` (sinais "negativ"/"so no") → APROVADO · exit 0. **O que separava os 82 dos 172 era screening de texto sobre g3_notas+trecho_ancora — regra que não estava publicada (confissão dele na §13, exatamente a cobrança da trilha 38).** 254 CONFIRMADO = 172+82 ✔ (bate com a medida histórica da casa).
- **§8 do parecer (6 pontos à casa): 6/6 atendidos** — relatório sobre o sha apresentado ✔ · contagens reproduzíveis ✔ · RAISON falha-fechado ✔ · **nada gravado no acervo** (direcao_suporte 0/274; campo 'direcao' legado None 274) ✔ · separação status×direcao ✔ · campos/regras == artefatos ✔.
- **Schemas v1.3 = TODAS as adições da casa incorporadas:** N2 — bloco `condicao` allOf[1] **byte-idêntico à proposta da trilha 37** complementado por allOf[0] (obriga quando condicional): prova jsonschema **10/10** (furo fechado); texto de `uso` = redação da casa (2+2+1); `forca_biologica` → ponteiro de portão sem medição (D3 adotado); retirada das cláusulas de sentido_relacao (fica só a nota na meta). N1 — **Adição A integral**: required `status_validacao` dentro / alias fora; alias deprecated **com enum legado** e description confessando "defeito meu, medido pela bancada em 162/237" + critério de aposentadoria (portão medir os 2 campos idênticos em 100%); `status_auditoria_nota` criado (base→canônico, parêntese→nota); **trilha 39 adotada**: allOf pmid byte-equivalente ao bloco da casa (base {0,8} provisório; regra {1,8} pós-migração); **cross-over restituído**; sem '(?i' inválido; sem "Medido hoje" em descriptions.
- **Minuta: checklist verde** — §3 R1+R7 reescrito (confissão com ampliação creditada à casa) · §10.5 linha (ii) mantida a recusa + critério falsificável RAISON + tabela 273/1→172/102 · §13 relatório inline · **ERRATA v1.0 registrada**: (i) 21→92 era contagem nas fichas × vínculos (histórico; no dado atual os campos-novos NÃO existem ainda 0/274); (ii) §4B inválido era REF_OSIMO_2019 (hoje N1 'verificado' — corrigido; o atípico ATUAL do rodapé 274 é VINC_B1_0047·HAFIZI 'pendente_fulltext', a dívida conhecida).
- **R3/E2 RESOLVIDO e medido dos 2 lados:** padrão dele `^\s*(eutils|script|retrofit)[a-z0-9_]*\s*$` (CI) → **486 campos de avaliador · 0 falsos-positivos** (confissão nossa: 1ª varredura incluiu g1_metodo e deu 511 — campo errado; medida correta = só avaliador) · 5 valores-ferramenta seguem reprovados · avaliador legítimo NÃO morde. Ele ainda aponta proativamente o **gate rev.A2** (substring morderá quando a nota migrar) = convergência com a nossa dívida **rev.A3-E2**: a casa adota o padrão dele como proposta unificada a caminho do mestre.
- **R2: critério de aceitação do derivador IDS-JSON ACEITO:** 146 exatos = 48+71+16+11 por categoria + sha + fonte declarada (regra formalizada por ele; a trilha 38 da casa já tinha medido os 146 estruturais — execução do derivador agora tem critério bilateral).
- **§9 da minuta verificado na fonte:** kit SCHEMA-CLAIM evidence_role = 4 valores exatos `human_clinical | human_experimental | post_mortem | preclinical_mechanistic` (**sem review** — reforça Decisão 2). Nota registrada: a casa TEM o kit arquivado e ancorado; disponibilização ao auditor-2 fica a critério do operador.
- **ADIÇÃO medida da casa (corpo à ressalva §4/§5 do comentador):** dos 172 'sustenta transitório', **58 (33,7%) não são 'verificado'** (preclinico 49 · extrapolado 5 · pendente 3 · emergente 1) — não é furo do script (ele mira direção; maturidade mora em verification_status, eixo separado); proposta: portão/migração carregam marca dupla (transitório-de-direção × verification_status).
- **Confissões da casa nesta trilha:** 4 regex de checagem apertadas demais na 1ª execução (identificadores draft-07/V-17 lidos como medição · caixa de 'A casa' · [^.]+ curto · crase do ID) — material dele estava certo nos 4; corrigidas com nota datada; JSON reescrito. Objeto-base jsonschema inválido na 1ª prova (papel fora do enum) — refeito: 10/10.
- **Posição da casa: ENDOSSA** — L-05 v1.3 estruturalmente consolidado (responder RESPOSTA_6) · triagem operacional com saída transitória registrada como regra de uso · 102 = fila humana/semântica · melhoria de sinais (§6 comentador) deferida: se adotada, republicar relatório com MESMO critério RAISON e nova contagem datada. Sobras do eixo: migração (agenda operador/taxonomia: 274 campos N2 + 237×3 N1 + 162 notas + 30 uso 'B1_v2'→leva_origem) · portão L-05 futuro (condicao/forca/uso) · alinhamento futuro do eixo de aresta do grafo (sentido_relacao) · taxonomia de natureza/desenho (minuta já ensaia preclinica_in_vivo/vitro — vem a seguir).
- **0 ciência:** selos finais V7 `6e2c2979…` · manifesto `79d1309a…` · P-8 `84fa918d…` ✔.

## Rev.33 — 2026-09-17 (rodada 26: ACHADO do mestre sobre a V2.1 + parecer do comentador → V2.2 INSTALADA por decisão do operador, opção A; trilhas 45 18/18 e 45b 10/10; 0 ciência)
- **Arquivados verbatim:** achado do mestre `ACHADO_V21_NO_UNIFICADO_2026-09-17.md` sha `2841bc66…` (auditou o upload `5be36836…` = exatamente o registro da casa) · parecer do comentador (destinatário: o mestre) sha `dfbd9ab7…` — digitais nas pastas `MESTRE_achado_V21_no_unificado_recebido_2026-09-17/` e `COMENTADOR_achado_V21_recebido_2026-09-17/`.
- **Achado PROCEDENTE (5/5 verificado na V2.1 vigente, trilha 45):** o nó §2 "EVIDÊNCIAS / VÍNCULOS UNIFICADOS" recebe os DOIS fluxos (linhas 53/59/65: eixo da Pasta espelhado com EVIDÊNCIAS+NARRATIVAS próprias, duas setas) **antes** da ONTOLOGIA (linha 72) — fusão que torna a D-06 inimplementável (D-06 vive na minuta 2 do L-05: 'segregada e rotulada · não altera nenhum eixo · toda consulta registrada'). Busca ativa + `[ CONEXÃO / CONSULTA ]` verbatim confirmados (item 5 dele).
- **Convergência independente mestre × comentador:** endurecimento de proveniência — todo item recuperado carrega `origem_conhecimento = canonico | atualizacao` (item 5 do achado = §3 do parecer). Medida: o campo NÃO existia na V2.1 (0 ocorrências).
- **Itens 1-2 do achado já estavam saneados na instalação da rodada 24** (Rev V2.1 + rótulo do mapa desambiguado de '# 21.'); restavam **H1 'V2 15.09.26'** e a **duplicata '# 2.'** (§8.4 do parecer) — ambos corrigidos na V2.2.
- **V2.2 INSTALADA (decisão do operador, opção A):** vigente sha `df7f7cfd…` · V2.1 `1a50645e…` → SUPERSEDED_ (cadeia no ponteiro) · escopo cirúrgico provado: **sufixo §3→fim BYTE-IDÊNTICO** (catálogo 146 IDs, §§5-30, §18/§19/§20 intactos) · 30 seções numeradas únicas · CRLF preservado · tríade MEC/CLÍN/TER + EXPLICAÇÃO NARRATIVA + ANAMNESE preservadas (o diagrama do parecer as omitia — preservação editorial da casa, registrada).
- **Rec. 4 do mestre acatada: item novo D-V2-NO-UNIFICADO** — sai da D-V2-DIAGRAMA-DUPLO por ter consequência de segurança; **RESOLVIDO na instalação da V2.2** (nasceu e fechou na rodada 26). **D-V2-DIAGRAMA-DUPLO permanece** só para a DIREÇÃO Evidência↔Biblioteca (prosa a montante × desenhos).
- **Parecer do comentador: 10/10 blocos verificados com crédito** (trilha 45); §9: L-05 v1.3 **sem reengenharia** — a frente do auditor-2 segue estável (RESPOSTA_6). Correção de fato registrada: a casa TEM o kit; oferta de repasse continua com o operador.
- **Confissão da casa (datada, na trilha):** o 1º critério C1 (unificad=0 no arquivo inteiro) era apertado demais — a linha Rev cita legitimamente o nó removido; régua corrigida por camada (desenho §2 = 0 · total = 1 histórico). **Nota de método:** grep raso divergiu da contagem real por formas Unicode de acentos (ex.: 'terapêutica' CI retornou 0); a casa adota **python NFC** como camada oficial de contagem em acervos acentuados.
- **0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · P-8 `84fa918d…` · vínculos `490675e6…` ✔. Decisões pendentes do operador inalteradas (kit a/b/c · P-6 e fila humana dos 102 · anexo P-8 do mestre + arquivo `be48a5ef…` ainda por vir · Fase 4 L-NT — âncora §6 verificada intacta na V2.2).

## Rev.34 — 2026-09-17 (rodada 27: triagem v1.1 do auditor-2 + minuta (5) + comentador — réplica 13/13 INTEIRA E EXATA; derivador IDS-JSON APROVADO; 0 ciência)
- **Arquivados verbatim:** minuta (5) sha `2b06b365…` · relatório v11 `a6ede6f3…` · reenvio do relatório v1.0 = **byte-idêntico** ao da rodada 25 · .py v1.1 (cópia casa) `f8b29ad0…` · comentador verbatim próprio. Digitais na pasta `AUDITOR2_triagem_v11_L05_recebido_2026-09-17/`.
- **v1.1 reproduzida byte a byte (exceto data):** 274/231/43 · por regra 231/16/19/8 · RAISON __PENDENTE__ pelos motivos corretos (`negativ`, `so no `) · exit 0. Lado a lado oferecido por ele e aceito: a v1.0 também reproduz 172/102. **Segunda via independente da casa: 274 pares (valor, motivo), zero divergência.**
- **Diff v1.0→v1.1 pelo AST:** `sha256` e `main` idênticos; `triar` muda como declarado (regra 4); SINAIS perde `extrapol`; STATUS_NAO_AUTOMATICO novo. 2 mudanças = 2 mudanças.
- **§14 dele INTENSAMENTE EXATO (5/5 sob camadas declaradas):** 62 mandados por menção a extrapolação (reconcilia o 66 da rodada 25: 66 − 4 CONF+pendente+sinal) · 138 com campo declara no pool CONF∧¬pendente · **60** dos 62 com o campo · **78** passando em silêncio · **57** já `extrapolado|preclinico`. Fronteira nomeada: VINC_B1_0263 (`media (revisao; …, extrapolado para transtornos de humor)`). Regra 4: bucket 8 = 7 CONFIRMADO + 1 NAO_LOCALIZADO; ex-sustenta = exatos os 3 nomeados (0259/0268/0270). Tese dele CONFERE: extrapolação já tem 2 campos estruturados (274/274) — sinal de texto era P20 dentro do próprio script. **Casa ENDOSSA a v1.1 e o critério de admissão de sinais futuros do §14.5.**
- **Marca dupla recalculada (adição da casa, corpo à ressalva):** dos 231 automáticos, **112 (48,5%) não-'verificado'** — extrapolado 52 · preclinico 59 · emergente 1. Fila 43 = verificado 21 · extrapolado 10 · preclinico 4 · pendente 7(+1 fulltext). A fila encolheu; o peso da ressalva cresceu (§14.4 dele, subscrito).
- **DERIVADOR IDS-JSON: dívida D-L05-IDS-JSON instrumentada — critério bilateral R2 saturado.** Descoberta: o fonte (`1º IDS_OFICIAIS.md`, sha `f3a74fbc…`) **é JSON inteiro**. Camada estrutural: **146 = 48+71+16+11 exatos, POR CHAVE == bloco `contagem`**; removidos 5 ✔. Artefato candidato `_ids_oficiais.json` (sha `d0ff2647…`) + PROVENIÊNCIA em `01_norteadores/_derivados_trilha46/`. **Causa do 103 identificada:** parsers de texto subcontam (103 trilha 25 · 74 regex de prefixo — IDs sem prefixo); só a estrutura reproduz os 146. Adoção formal = gate/mestre (fonte única do catálogo) — fica pedido.
- **Comentador verificado com crédito (6/6 seções):** consolidações batem na v1.3 medida · D2/D3/D4 = as Decisões 2/3/4 da minuta, mesa do OPERADOR (casa endossa D2-com-prazo · D3 registro explícito requisito×tarefa-posterior + 20 medidos: uso 17 clinico/2 gap/1 contexto ✔ · D4 proveniência histórica — default de geração já provado pela casa em R6-v1.3) · §3 CONFERE (cabeçalho v1.0 × conteúdo v1.3 — **mesma doença do H1 da V2.1 que o mestre achou**) · §4 respondido pelo derivador.
- **Pergunta fina da rodada 25 ENCERRADA:** a correção de REF_OSIMO_2019 foi feita pela casa (errata T25 de 2026-09-14, manifesto 2.10) — a errata 2 da minuta (5) integra esse fato. Minuta (3)→(5): **2 hunks, +52/−1** (só o §14 e ajustes adjacentes).
- **Confissões da casa nesta trilha (datadas):** (1) "trilha 38 mediu 146 estrutural" era impreciso — mediu 74 mecânicos e citou 146 declarados; entrega real só na trilha 46. (2) "CONF+pendente = 3" — são 7, dos quais 3 ex-sustenta. (3) régua "campo ≠ nao" larga; régua só-sim|parcial dava 77≠78; camada final com a fronteira media nomeada.
- **0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · P-8 `84fa918d…` · vínculos `490675e6…` intactos após 3 execuções ✔.

## Rev.35 — 2026-09-18 (rodada 28: P-8 SELADO nas duas casas — reconstrução byte a byte das 3 regiões do mestre · achado V2.1 fechado · NFC bilateral · Fase 4 VERDE; trilhas 47 7/7 + 47b; 0 ciência)
- **Verbatim arquivados:** resposta do mestre (fecho do achado · correção dele sobre onde vive a D-06 · 3 regiões do P-8 · critério de troca corrigido · adota NFC · Fase 4 verde) sha registrado · parecer do comentador (6 blocos) sha registrado.
- **Reconstrução: EXATA.** Sobre a base 84fa918d… (658 linhas, LF) apliquei as 3 regiões coladas — a única candidata que fecha é a que usa **todos os textos dele byte a byte** (v06 'G3/revisão humana' · V-08 em 2 linhas ('lastro estrutural…não esta regra') · comentário F-C2 6 linhas · s_man com parênteses externos · 1ª linha da mensagem sem prefixo f). **658+6+1 = 665 linhas = sha `be48a5efa1d6…`**. Aritmética dele do +17/−7: conferida (+7 líquido). Hunks confinados às 2 zonas; compila.
- **Comportamento idêntico e provado:** 2 ERRO / 299 AVISO / exit 1 = base; V-14 limpa; **F-C2 dispara** (1 ID trocado por falso preservando 15 → ERRO V-07 'identidade divergente', 3 ERRO) — e a **base também disparava**: a correção funcional já era da casa desde a rodada 20; o que faltava eram o comentário e os bytes gêmeos. **Troca executada:** backup 84fa918d → `.bak_2026-09-18` · **oficial = `be48a5ef…`** · invocação oficial 2/299/exit 1. **1 sha viva nas duas casas.** Os 2 ERRO de desenho (natureza_evidencia · trilha) seguem na agenda de taxonomia/migração.
- **Correção dele incorporada com crédito:** o critério de troca publicado pela casa dizia "só o comentário" — eram dois (+ variações de bytes entregues como regiões exatas). Registrado: medir sem o critério corrigido teria gerado falsa suspeita.
- **Precisão da D-06:** as três frentes agora falam a mesma frase — "uma norma de outro documento (minuta 2 do L-05) ficava inimplementável". Endosso dele à preservação editorial: registrado.
- **NFC/camada: régua bilateral adotada** (mestre declara camada em toda contagem; o comentador endossa).
- **Confissão da casa (datada, trilha 47):** o detector do teste F-C2 procurou a mensagem no tail de 400 chars (falso-negativo — o ERRO vive na seção enumerada por regra); corrigido para stdout inteiro. Comportamento nunca esteve errado.
- **Fase 4 = VERDE (mestre + comentador + casa):** âncora §6 (deveres 1–2 da NT) medida intacta na V2.2 vigente (rodada 26). Quando chegar o Contrato das Unidades Narrativas: réplica de sempre.
- **0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…` ✔ (contraexemplo F-C2 rodou em /tmp).

## Rev.36 — 2026-09-18 (rodada 29: L-05 N1 v1.3 + N2 v1.4 + minuta v1.4 do auditor-2 + parecer do comentador — trilha 48: 52/52 VERDE; réplica integral; 0 ciência)
- **Arquivados verbatim:** minuta v1.4 sha `78a0f2af…` (42.809 b) · N1 v1.3 sha `b06660fd…` = **BYTE-IDÊNTICO** ao ancorado na r.27 (N1 não mudou) · N2 v1.4 sha `d96ad15b…` (novo; anterior v1.3 `ec4f0de8…`) · verbatim do comentador `c188169e…` (registro interno). Digitais na pasta `AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/`.
- **Diff N2 v1.3→v1.4 medido (opcodes):** 3 linhas substituídas ($id · description raiz · ancoras.description) + 19 linhas inseridas = **bloco allOf da D3** (`g2_elegibilidade=redirecionado_clinico` ⇒ `ancoras.minItems 2`). A minuta (§15.2) é fiel ao schema; check_schema draft-07 verde nos dois.
- **9 alegações do comentador sobre N1 + 9 sobre N2: replicadas 1 a 1** (estrutura: enums/required/deprecated/allOf; comportamento: **26 casos sintéticos falsificáveis, 26/26** — N1 10/10: condicional pmid das duas direções · alias não satisfaz required do canônico · verificado⇒g3_verificado_por · citacao_confirmada deprecated mas transitória; N2 16/16 — inclui os 3 casos do §15.2 "Testado": base 1 âncora passa · redirecionado com 1 reprova · redirecionado com 2 passa · exclusividade de `condicao` nas duas direções · trilha×uso 2+2+1 · papel≠refuta/direcao=refuta).
- **D4 (citacao_confirmada) — RESOLVIDA NOS DOIS LADOS, medido:** N1 traz `deprecated: true`, `[boolean,null]`, descrição "DEFAULT DE GERAÇÃO… sem carga verificacional"; no portão: **P-8 = 0 ocorrências**; gate rev.A2 carrega o campo **só como detector de banimento** (depender dele = FALHA [1b] · preenchido = Info nomeada [1c]). A Decisão 4 da minuta foi APLICADA em norma de schema (deprecated, sem via) — falta só o aceno-homologação do operador (endosso D4-proveniência já registrado na r.27).
- **D3 (retroancoragem) — RESPONDIDA EM ESTRUTURA, medido:** caso geral `minItems 1` (curadoria posterior) × `redirecionado_clinico` `minItems 2` (requisito de corpus), exatamente o que o comentador exigiu declarado. Efeito medido no acervo real: **exatos 20** vínculos ficam não-conformes até a 2ª âncora (0 campos `ancoras` hoje) — o portão fará o vazamento aparecer. O trabalho de curadoria dos 20 segue na mesa do operador/equipe.
- **Segunda via independente da casa (jsonschema Draft7, 274×N2 e 237×N1, dados reais):** únicas não-conformidades N2 = {`trilha, ancoras, ancora_principal` ausentes ×274} + {`uso=B1_v2` ×30} — **fecha o mapa de migração dele, zero assinaturas extras**. N1: 0 conformes (§11 dele confere) · faltas {natureza_evidencia, desenho_estudo_bruto, status_validacao ×237} · compostos medidos **status_auditoria 162 · origem_pipeline 50** (bate § 4B). Patterns: id_vinculo 274/274 · REF_ (com sufixo) 274+237. verificado⇒g3_verificado_por: 140/140 íntegro.
- **Marca dupla recomputada (§15.3 dele):** corpo 112/231 = extrapolado 52 · preclinico 59 · emergente 1; fila 43 = verificado 21 · extrapolado 10 · preclinico 4 · pendente 7 · pendente_fulltext 1. Reexecução da triagem v1.1 nesta rodada: 274/231/43 · 231/16/19/8 · RAISON · exit 0.
- **Dívida documental da minuta FECHADA (comentador §3 da r.27):** identidade de versão agora coerente — H1 sem número · H2 "v1.4 — PROPOSTA, NÃO NORMATIVO" · Status "PROPOSTA v1.4" · arquivo v1.4; tokens históricos só em changelog/ponteiro. Kit: §15.4 registra não-bloqueio (dívida 'curadoria dos 39 PMIDs' fica subordinada à decisão da camada, inalterada).
- **Dívidas movidas:** D-L05-CAMPO-DUPLO **formalmente fechada** (campo único direcao_suporte consolidado; nome morto da D-L05-NOMES-DIRECAO confirmado em schema). Permanecem: **adoção formal do `_ids_oficiais.json` (146)** = gate/mestre (pendência nº 2 do comentador, subscrita) · **D2 = classificação dos 30 `review`** = operador, com leitura, com prazo (pendência nº 1 do comentador, subscrita) · portão L-05 a nascer (V-17 integridade âncora principal · condicao × BLOCO_07/08 de forca_biologica_conexao · trilha×uso).
- **Nota para a futura rev.A3 (gate):** além do padrão E2 unificado (dívida da casa com o mestre), o texto da Info [1c] do gate rev.A2 ("remoção/ignorância a decidir no pacote L-05") já tem decisão tomada pela D4 — candidato a atualização documental junto da rev.A3.
- **Confissões da casa (datadas, na trilha 48):** C1 — fatia errada do opcode 'insert' (o insert real = 19 linhas do bloco D3) · C2 — régua ingênua "0 ocorrências de citacao_confirmada": o gate a carrega como detector de banimento, régua corrigida para classificação semântica · C3 — régua ingênua de topo do MD: menções históricas (changelog v1.0→v1.1, ponteiro §15.1) são legítimas; régua passou a separar camadas de identidade × histórico · C4 — camada: "forca_biologica_conexao vazio 274/274" = campo **AUSENTE** (não null) nos 274.
- **Posição da casa: CONFIRMA E SUBSCREVE** — o aceite do comentador ("N1 v1.3 + N2 v1.4 estruturalmente aprovados como base de fechamento do L-05") está correto número a número. Pendências efetivas = exatamente as 2 nomeadas por ele (D2-operador · adoção formal-gate/mestre) + homologação do operador do desfecho já aplicado da D4. **0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…` ✔ (medido no início e no fim da trilha).

## Rev.37 — 2026-09-18 (rodada 30: **L-NT Minuta 1 do mestre + comentador — trilha 49: 49/49 VERDE**; dimensionamento dele reproduzido EXATO; casa descobre camada completa de claims (89×81) e o órfão real BLOCO01.001; 0 ciência)
- **Arquivados verbatim:** minuta L-NT m1 sha `294119b9…` (11.803 b) · verbatim do comentador `3b5bbbc3…` (interno). Pasta `MESTRE_LNT_minuta1_recebido_2026-09-18/` com DIGITAIS.
- **Dimensionamento da Parte 1 reproduzido EXATO sob camadas declaradas:** 90 marcadores/81 distintos · 11 blocos · claims/bloco 1/7/30 (camada com repetição; distintos daria 6/27 — nota) · claim_id 244/274 · 80 ids referenciados · vínculos/claim 1/2/15 · **628 frases** (camada exata encontrada entre 8 variantes medidas: split `r"\.\s+"` com corte **≥60**; vizinhas 625/626/872 — receita de rodapé subespecificada, sensibilidade ±3; pedido: rodapés passam a trazer o COMANDO literal) · **21.503 palavras** exato · aritmética 12–19 mil = 80×146≈11.680 · 130×146≈18.980 ✔.
- **DESCOBERTA A3b/A7 (contribuição da casa):** a canônica tem **89 claims distintos**, não 81 — 4 cabeçalhos agrupam ids com abreviação (`(BLOCO03.009, 012)` · `(BLOCO04.004, 008)` · `(BLOCO08.002, 003)` · `(BLOCO08.004, 006)`) e a regex do rodapé (com `\)` final) os perde inteiros. Dos 80 referenciados existem **79** na camada completa ("80 dos 81" → "79 dos 89"); **órfão real = 1: BLOCO01.001 (VINC_B1_0001–0006)** → **dívida candidata D-LNT-CLAIM-LEGADO**; 10 canônicos sem vínculo (escopo da cobertura Parte 5). Consequência normativa: **a régua de existência do NT-02 deve ser a camada completa** — com a estrita reprovaria 7 claims válidos e não veria os formatos agrupados.
- **Âncoras normativas conferidas:** V2.2 `df7f7cfd…` intacta · §6 deveres 1–2 ✔ · §7 com a frase-limite verbatim (com 'uma'; a minuta elide — precisão fina sem erro) · §7 enumera os mesmos 7 estados do `status_epistemologico` · §13/§14 existem · L-05 minuta 2 carrega D-02 (5 eixos) · D-03 (6 tipos) · D-04 (ligação) · D-05 (aceite 20/cego/≥90%) · D-06 (pasta) · D-07/D-08 ✔ · **P-8 oficial hoje: 2 ERRO / 299 AVISO / exit 1 e os ERRO nomeiam `natureza_evidencia` e `trilha`** (Parte 8 da minuta confere) · `natureza_relacao` da minuta == enum N2 v1.4 ✔ · 4 `nao_estabelecida` medidos ✔.
- **Kit/camada `uso`:** BLOCO DE ESTADO tem 22 linhas `uso:` por claim = 12 clinico · 6 contexto_mecanistico · 4 gap_pesquisa (confere Parte 2.2 e Parte 5) · SCHEMA-CLAIM v1.2 define os 3 valores ✔. Precisão de camada registrada: "uso não existe no acervo" é correto **por-claim** (censo: nenhum registro); por-vínculo existe 274/274.
- **Armadilha Parte 7 = lastro real medido:** RAISON 2013 (2 vínculos) "negativo na amostra toda; resposta só no subgrupo hs-CRP/TNF/sTNFR2" ✔ (a mesma prova que a triagem exige) · repertório das pernas presente (citocinas × depressão; TNF em animal — Xu 2020 camundongo [PRÉ-CLÍNICO]) · '27%' e '1,46' presentes na V7 (lastro NT-10 = dívida D-B1-R4-TOKENS) · lição HAFIZI conferida documentalmente: **25 âncoras propagadas** (decisões, trilha 17) + token dentro da âncora (ledger); atual `REF_HAFIZI_2007` ✔.
- **Crédito 'a casa pediu o caso-armadilha' verificado NO TEXTO:** RESPOSTA_15 (linha 45) contém o pedido no estilo "o que este contrato jamais pode produzir" — fato, não cortesia.
- **Comentador × minuta: 9/9 pontos conferidos** (invariante · N-1..6 · V-NT NT-01..10 · claim_origem ≥1 · isolamento/remoção/reutilização + 20 + cego + ≥90% · estimativas marcadas como estimativa · cobertura/não-cobertura · lacunas gap+nao_estabelecida · Parte 8 = §5 do comentador: uso × Claim Kit = dependência contratual, **a mesma decisão da camada do kit pendente do operador**).
- **Erratas/confissões da casa (datadas, na trilha 49):** META-ERRATA D5 — 1ª execução quase gravou CONFISSÃO FALSA (grep truncado em 150 colunas numa exploração preliminar; a memória estava certa) · F4 — agulha em caixa mista sobre feno casefoldado · D2 — `findall` com grupo capturante devolve o grupo, não a linha · nota evolutiva A7 (camada estrita→completa; as duas gravadas).
- **Posição da casa: APROVADA a Minuta 1 e subscrito o comentador** — prosseguir aceite-piloto de 20 unidades (revisor cego, ≥90%, 3 testes) sem reabrir a V2.2; pendências: (a) régua NT-02 = camada completa (nossa contribuição); (b) órfão BLOCO01.001 → D-LNT-CLAIM-LEGADO; (c) rodapés com comando literal; (d) dependências da Parte 8 (taxonomia · uso×kit ← decisão do operador · natureza_evidencia+trilha no dado). **0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…` · V2.2 `df7f7cfd…` · P-8 `be48a5ef…` intactos antes e depois.

## Rev.38 — 2026-09-18 (rodada 31 TEMÁTICA: proposta do operador "Formalização do fluxo dos Claims Clínicos — Claim Kit → Evidências/Bibliografia → N1 → N2 → camadas" arquivada verbatim e verificada ANTES da deliberação das duas frentes; trilha 50: 52/52; 0 ciência)
- **Arquivado verbatim** (`_documentos_serie/OPERADOR_PROPOSTA_fluxo_claim_N1N2_recebido_2026-09-18/`): sha `4ede1c81…` · 13.532 b · 520 linhas · digitais próprias. Fonte: mensagem do operador (bloco de código, sem anexo — medido: 0 arquivos novos em uploads/ para este objeto); digitado verbatim pela casa; camada NFC/LF declarada. Operador repassa os MESMOS bytes às duas frentes.
- **Posição de registro (3 precisões medidas):** (1) a proposta FECHA a pendência "DECISÃO DA CAMADA — 3 opções, dona: OPERADOR" (rev.29, rodada 23) na direção da **opção (c), autoria do comentador** (crédito registrado: "kit = ferramenta de curadoria; produto deposita em Evidências/Bibliografia; sem nova camada"); (2) a frase decisória-mãe "claim não integra a Biblioteca Canônica" NÃO constava verbatim no registro (2 ocorrências da expressão, ambas no contexto V2/D-V2-DIAGRAMA-DUPLO; 'claim clínico' 0×) — **esta proposta é o primeiro registro formal da decisão-mãe**; (3) a V2.2 vigente JÁ carrega a guarda-gêmea: Evidências "não constituem uma segunda Biblioteca Canônica nem uma fonte… independente" (harmonia com o §9 da proposta).
- **Números da proposta replicados 1 a 1:** 35 claims do kit (Lista = exatos B1.SM02.001–.035; o exemplo §2.1 existe: .014) · 22 blocos aprovados (8 aprovado + 14 aprovado_com_ressalva — 63,6% ressalvados para o §13.13) · uso 12/6/4 camada ancorada (23 = 22 + 1 espúria documentada) · **as "quatro lacunas" = exatos {.003 · .006 · .012 · .012c}** · PMIDs 49 = 10 na Bibliografia + 39 fora (dedupe por `pmid_oficial`) · 6 ferramentas existem (4 documentos + PubMed/esearch-G1-verificação + G1/G2/G3 medidos) · **kit sem chave-âncora** (0 na camada-chave) · SCHEMA-CLAIM confirma os 3 desfechos nomeados.
- **Schemas L-05 prontos para o eixo ADITIVO (medidos, nada muda neles):** N1 `b06660fd…`/N2 `d96ad15b…` intactos e draft-07 ✔ · `N2.claim_id` já cita o namespace do kit na description (teste sintético com B1.SM02.014 passa) · `id_vinculo`/`id_referencia_interna` genéricos (transversal estruturalmente aberta) · uso enum superset dos 3 do kit ✔ · sintéticos trilha×uso 3/3: kit⇒clinica PASSA · clinico+mecanistica REPROVA · nucleo_causal+clinica REPROVA · §2.2: 10/10 campos em N1 (+claim_id_origem·leva_origem bônus de proveniência) · §2.3: 11/12 (**`entidades` não é campo do N2 — vive no L-NT; nota de precisão à deliberação**).
- **Mapa de fortuna do materializador (entregue medido):** direto (claim_id·uso·pmid·statement·moderadores.regra_motor·comparador·nota_ressalva) · derivável (trilha⇒clinica; dedupe 10/39) · mapeável por decisão (status→status_auditoria · verification→verification_status · g3_verificado_por se 'verificado') · **fortuna-zero: trecho_ancora/ancoras/ancora_principal = leitura dos 49 artigos** · taxonomia natureza×desenho = o MESMO bloqueio dos 2 ERRO vivos do P-8 (evidence_role 22/22 human_clinical; 2 mapas diretos + 2 dependentes) — um só trabalho destrava acervo e materializador.
- **Arquitetura:** nenhum conflito detectado nas camadas medidas (ordem EVIDÊNCIAS<VÍNCULOS<ONTOLOGIA<MOTOR no mapa vigente ✔ · §6 deveres 1–2 NT a jusante ✔ · papéis §5 da proposta = prática histórica mestre/estrutura ✔). D-V2-DIAGRAMA-DUPLO segue viva (não criada pela proposta; redação final deve respeitar a prosa).
- **Pergunta-âncora ao mestre:** Parte 2.2 do L-NT passa a ler a herança como `uso`: kit → N2.uso → NT.uso — ajuste de linha na minuta 2, sem reescrever o contrato (o N2 é o portador contratual; enum superset). Transversalidade (§8/§12): catálogo hoje = 48+71+16+11; 'exercício'/'intervenção' sem grupo próprio — decisão pós-piloto, medida entregue.
- **Posição da casa: B — concordância com ajustes** (os nomeados acima: precisão `entidades` · herança `uso` via N2 · ressalvados 14/22 · formato de entrada com mapa de fortuna · transversalidade pós-piloto). Decisão formal: frentes + homologação do operador.
- **Cartas:** RESPOSTA_17 (mestre) + RESPOSTA_9 (auditor de estrutura) com o MESMO verbatim anexado (sha `4ede1c81…`). Confissões datadas da sessão: 6 (C0–C5b — réguas de contagem; nenhum dado do acervo tocado).
- **Produção retoma exatamente onde parou:** 20 unidades-piloto NT-B1 (mestre) + portão L-05 (estrutura) + rev.A3-E2 (casa, em preparação). **0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…` · V2.2 `df7f7cfd…` · P-8 `be48a5ef…` (reexecutado: 2 ERRO nomeando natureza_evidencia·trilha / 299 AVISO / exit 1).

## Rev.39 — 2026-09-18 (rodada 32: consolidado recebido ("confirma conclusão B") ancorado NA ARQUITETURA V2.2 VIGENTE por instrução do operador; trilha 51: 28/28; 0 ciência)
- **Arquivado verbatim** (`CONSOLIDADO_fluxo_B_recebido_2026-09-18/`): sha `ff8daf6f…` · 2.215 b · 34 linhas · digitais próprias. Remetente não assinado — presumido comentador pela voz; confirmação pedida ao operador. Instrução do operador honrada: ancoragem no documento vigente (V2.2 `df7f7cfd…` conferido).
- **6 pontos atribuídos à Arquitetura, verificados linha a linha:** itens 1·2·3 VERBATIM (§5 L243 · §5.1 L292 · L369+diagrama de vínculos) · item 5 conferido (cadeia §1 L31 + mapa NT→ONTOLOGIA/GRAFO→JSONs→MOTOR + §6) · item 6 verbatim-próximo (§22 L1214 + L1184 + L1350) · **item 4 = PRECIÃO da casa: a V2.7 NÃO diz que "o Claim Kit pode atuar como produtor de N1/N2" — 0× 'kit' e 0× 'produtor' no texto vigente; a afirmação vale como COMPATIBILIDADE (L-05 já admite o namespace do kit — trilha 50), não como citação da arquitetura. Redação sugerida à homologação registrada.
- **Questão G3 multi-IA medida:** acervo ancorado = COMO EXECUTAR **v1.7** (sha ok); **v1.8/v1.9 NÃO existem no acervo** (busca global). A v1.7 diz: "Conhecimento nasce em G3" (L114) · 3 saídas · ressalva exige nota_ressalva · abstract colado na sessão — executado por 'a IA' no singular; **o arranjo multi-IA não consta em NENHUM texto do kit** (0× IA1/IA2/IA3·votação·consenso·fonte primária; nenhum arquivo traz mecanismo de resolução). **Correção do consolidado é ADITIVA (não contradiz nada) e aponta lacuna real: a prática multi-IA do projeto não está normatizada** → deve entrar em versão normativa a ancorar (v1.9 se existir fora; senão adendo sobre a v1.7 — a casa prepara). Princípio anti-votação ('fonte primária árbitro; consenso não cria evidência') = §22 V2.2 + guarda P-6 — a casa subscreve e propõe carregar no dado (g3_verificado_por + nota de divergência).
- **Convergências:** B == B da casa (rev.38) · os 5 ajustes do consolidado = os 5 medidos e nomeados pela casa · sequência proposta == §7/§11 da proposta do operador (piloto controlado) · camada registrada: pareceres originais das frentes NÃO chegaram à casa — homologação sobre os bytes deles (pedido 1 ao operador).
- **Pedidos ao operador:** (1) pareceres originais das 2 frentes · (2) COMO EXECUTAR versão corrente, se houver v1.8/v1.9 fora · (3) confirmação do remetente do consolidado · (4) homologação A/B/C/D por decisão sua.
- Relatório emitido na pasta (repassável). Confissões datadas: 4 (DIGITAIS na raiz por caminho relativo C1 · agulha 'consolid' C2 · ordem por find global C3 · split sem maxsplit C4).
- **0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…` · V2.2 `df7f7cfd…` · P-8 `be48a5ef…` intactos.

## Rev.40 — 2026-09-18 (rodada 33: DIVERGÊNCIA DUPLA‑V2.2 resolvida documentalmente por bytes — trilha 52: 22/22; 0 ciência)
- **O fato:** o projeto do mestre tem 'V2.2' sha `309aa65f…` (relato dele: ≠ V2.1 só em §§2/21, 28 seções idênticas, SEM `origem_conhecimento`/prevalência-da-prosa/'fora do cânone'); a casa declarou vigente `df7f7cfd…`. Operador pede o confronto (a–d).
- **Inventário medido:** `309aa65f…` NÃO existe no workspace (varredura global .md) — diff byte-a-byte final pendente dos bytes (pedido 3 ao operador). As 3 marcas ausentes existem **somente** na `df7f7cfd…` (3·1·1; âncoras L4·L117·L121·L172·L175); todos os outros elos: 0·0·0.
- **Identificação por conteúdo FECHADA:** a assinatura do relato do mestre bate EXATA com **upload da rodada 24 (`5be36836…`) × V2.1 instalada** — 28 seções idênticas, difere exatamente §2 e §21, §§6/7/13/14 byte a byte. O arquivo do projeto dele é, em conteúdo, o upload r24 (pré-achado, rotulado 'V2 … 15.09.26', §21 duplicada) com rótulo 'V2.2' atribuído em algum ponto do repasse — **nunca passou pela instalação da V2.1 (dedup) nem da V2.2 (achado)**.
- **(a) SIM, `df7f7cfd…` é posterior/editada sob decisão registrada** (rodada 26, opção A do operador, ACHADO do próprio mestre `2841bc66…`); não é edição espúria. **(b)** vs upload r24: §2 (nó UNIFICADOS removido · fluxos segregados até o Motor · bloco Pasta 'fora do cânone' · `origem_conhecimento` desenho+prosa · 'prosa prevalece sobre desenhos' · H1 V2.2‑17.09 · 30 seções únicas) + §21 consolidada; sufixo §3→fim BYTE‑IDÊNTICO re‑verificado (39.165 b). **(c) vigente = `df7f7cfd…`** (única com as guardas exigidas pelo achado; conteúdo do L‑NT idêntico nos dois lados). **(d)** documentação: rev.33 · ARQUITETURA_VIGENTE.txt · trilhas 45/45b · ACHADO arquivado · RESPOSTA_14 + ADENDO_2_RESPOSTA_13.
- **Correção de rota pedida pelo mestre: INVERTIDA com prova** — a Minuta 1 JÁ cita `df7f7cfd…` corretamente (grep); não se retifica a citação, troca‑se o ARQUIVO no projeto dele (52.181 b · CRLF · sha completo publicado no relatório).
- **Dívida nova nomeada: D‑V22‑BYTES‑PROJETO** (bytes da vigente não confirmados no projeto do mestre — esta divergência é a prova; o repasse do arquivo fecha). Pedidos: (1) enviar V2.2‑instalada ao mestre · (2) enviar `309aa65f…` à casa para arquivar na cadeia como 'V2.2 declarada = upload r24, nunca vigorou' + diff final · (3) crédito ao mestre: relato dele exato e decisivo; conclusão 'conteúdo suficiente para a Minuta' endossada com prova byte‑a‑byte.
- **0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…` · V2.2 `df7f7cfd…` · P‑8 `be48a5ef…` intactos. Confissão C0 (script, sem medida afetada).

## Rev.41 — 2026-09-19 (rodada 34: AUDITORIA INDEPENDENTE da 2ª rodada da IA externa sobre o Motor — trilha 53: 74/74; 0 ciência)
- **Base arquivada verbatim:** Filosofia `dedbff6c…` (5.264 b) · Roteiro `5e3f9163…` (22.447 b) · parecer-transcrição `40a58381…` — pasta `BASE_AUDITORIA_MOTOR_recebida_2026-09-19/` + DIGITAIS. Vigente conferida: `df7f7cfd…` intacta.
- **ACHADO DOCUMENTAL-RAIZ:** a IA externa auditou a linha SUPERSEDED (r24 `5be36836…` ×31§/dup§21 · ou V2.1 `1a50645e…` ×31§/dup§2 — indistinguíveis pelas âncoras dela), NÃO a vigente. Provas: C-10 impossível contra H1/Rev “V2.2”; 0 menção a `origem_conhecimento`/prevalência/“fora do cânone”; E6 com citação “literal” **inexistente em TODAS as versões** (`"preservando a origem de cada informação"` 0× casefold em 5 arquivos; `"quando pertinente"` 0× na base). **Regra nova da casa: citação dessa frente não vale como literal até verificação.** Consequência demarcada: âncoras fora de §2 mantêm-se (sufixo byte-idêntico); §2/§19/C-2/C-10/agravante-do-G1 re-ancorados.
- **Vereditos (A=G1–G20):** 15 pendências reais confirmadas (G1,G4,G7–G14,G16–G19) · 2 “não determinável nesta base” corretas (G2,G5) · 3 reduções da própria IA confirmadas (G3,G6,G15; +G10 parcial) · **G20 reformulado** (agregado de C-3/C-4 sob G19 — dupla contagem) · **agravante do G1 invalidado** (prevalência da prosa na vigente) · ordem da IA substancialmente correta, casa inverte para **G19 → G16 → G1**. Nenhuma pendência inventada do zero.
- **Vereditos (B=C1–C10):** C-3/C-4 **contraditórios reais interdocumentais** (exigem G19) · C-5 divergência real de cobertura (fecha com G19) · C-6 real de taxonomia (→G18) · **C-7 REBAIXADA** (constituição × consumo — 1 linha de glossário; não bloqueia contrato) · C-8 divergência real **de registro** (status B1, correção menor; mitigação no próprio §26) · **C-1 e C-9 FALSAS contradições** (reconciliação interna medida: §6 itens/§8 “integração por relações”/§9·§15; “pendente de registro” ≠ “não feito”) · **C-2 FOI real na base lida = o ACHADO do mestre já corrigido na vigente (rodada 26)**; residual = desenhos frios §21/§30 (D-V2-DIAGRAMA-DUPLO) · **C-10 FALSO contra a vigente (artefato de base)**. Contra a conta da IA (“quatro impedem a especificação”): restam **C-3/C-4**.
- **E/P/[?]:** 16/16 confirmações substantivas de E1–E20 validadas (E6 re-ancorado na vigente; E8 com precisão — §11 vincula “o sistema”, ao Motor é derivável) · autocorreções E11/E15/E18/P6 validadas · correção estrutural validada: módulos M1–M9/T1–T3 = **0× tokens na base** (proposta dela, bem rotulada) · Parte C validada, com “preservação de procedência” [E] **só na vigente** (âncora dela fabricada).
- **Ordem recomendada entregue (sem soluções, regra do operador):** 0 saneamento da base (D-V22-BYTES-PROJETO + regra anti-literal) → 1 G19 → 2 G16 (+G2,G3-residual) → 3 G1 (+G9,G13) → 4 C-3/C-4 homologação (+G14/G20, C-5) → 5 G18/G7 (+G11) → 6 G8 (+G12) → 7 G4/G5/G6/G10 → 8 G15/G17 → 9 correções de registro.
- **Dívidas/pedidos novos:** identificar frente/remetente da auditoria · obter a 1ª rodada (bytes — casa só viu a 2ª) · repasse da vigente à frente (fecha junto de D-V22-BYTES-PROJETO) · homologações antigas mantidas (decisão B; pareceres originais; COMO EXECUTAR corrente; D2/146 IDs/D4/órfão). **Ciência: 0 tocada** (V7/manifesto/vínculos/P-8 reconferidos). Confissões datadas: 6 (réguas da trilha 53).

## Rev.42 — 2026-09-19 (rodada 35: COBRANÇA FORMAL DO OPERADOR sobre a "V2.2 vigente" — origem/cadeia/entrega medidas (trilha 54: 15/15) · SUSPENSÃO acatada · REGRA NOVA de versionamento registrada verbatim)
- **Fatos medidos (trilha 54):** `df7f7cfd…` foi CONSTRUÍDO PELA CASA na rodada 26 (17/09) sobre o upload do operador `5be36836…` + ACHADO do mestre `2841bc66…` + parecer `dfbd9ab7…` · a decisão registrada foi de DIREÇÃO ("opção A" — a trilha 45 declara "candidata em STAGING… APLICAÇÃO aguarda decisão") · **ENTREGA DO DOCUMENTO COMPLETO AO OPERADOR PARA APROVAÇÃO NÃO CONSTA: 0 cópias fora de `_documentos_serie/` (varredura sha global); 0 artefatos de entrega; 0 registro de aprovação-com-sha** · evidência convergente: o projeto do mestre detém o r24 rotulado, não a df7f7cfd.
- **Diff r24→df7f7cfd… (última recebida): +42/−18 linhas em 3 blocos** — (i) duplicata do mapa (114 linhas, com o nó UNIFICADOS do achado) eliminada · (ii) §2 novo (fluxos segregados · bloco Pasta · `origem_conhecimento` · prosa normativa · prevalência) · (iii) H1/Rev V2.2, 30 seções únicas · sufixo §3→fim byte-idêntico.
- **CONFISSÃO PROCESSUAL (gravada):** a casa converteu aprovação de direção em marca de vigência sem a etapa entrega-completa→aprovação-com-sha; e na rodada 33 orientou o mestre a trocar para arquivo nunca formalmente entregue. **SUSPENSO:** `df7f7cfd…` não é versão oficial do operador; reclassificado CANDIDATA pendente · ponteiro com nota datada · orientação ao mestre suspensa · referência recebida provisória = upload r24.
- **REGRA NOVA DE VERSIONAMENTO (verbatim do operador, vigente desde já, aplicável a TODO documento normativo futuro):** *PROPOSTA → ALTERAÇÃO DOCUMENTAL → DOCUMENTO COMPLETO ENTREGUE AO OPERADOR → APROVAÇÃO → SHA/DATA → VERSÃO VIGENTE.* Uma IA não altera documento arquitetural e transforma a própria cópia em fonte normativa sem entrega e aprovação.
- **Efeito retroativo medido (rodadas 31–34):** âncoras no sufixo §3→fim permanecem válidas em qualquer elo; âncoras do §2 novo passam a "medidos na candidata pendente" (na auditoria do Motor da rodada 34: C-2, E6-âncora, mitigação de C-3, agravante do G1) — re-carimbadas como proposta-pronta, não apagadas.
- **SUBMISSÃO formal desta rodada (relatório na série):** documento completo 52.181 b + sha + diff + cadeia de evidências, para a decisão (a) APROVAR / (b) DEVOLVER / (c) REJEITAR. Nada será instalado/vigenciado antes. Pedidos antigos mantidos; + aguardar a decisão do operador sobre a V2.2-candidata.
- **0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…` · P-8 reconferidos.

## Rev.43 — 2026-09-19 (rodada 36: DECISÃO DO OPERADOR — letra A: V2.2 APROVADA como oficial · regra nova cumprida ponta a ponta · vigência restabelecida com sha+data)
- **Aprovação formal registrada:** o operador aprovou a candidata V2.2 (`df7f7cfd…`, 52.181 b · CRLF · 30 seções unanimadas…) como **ARQUITETURA OFICIAL** nesta data. Cadeia da regra nova fechada: submissão documental completa (rodada 35) → **aprovação (esta rodada)** → **sha/data gravados** → **versão vigente**.
- **Efeitos:** (1) vigência restabelecida no ponteiro (nota de aprovação acima da nota de suspensão — histórico preservado); (2) âncoras do §2 novo recuperam força normativa — os itens das rodadas 31–34 re-carimbados "medidos na candidata" voltam a valer como norma (C-2 resolvida · E6 · mitigação C-3 · G1 sem agravante); (3) **repasse autorizado:** mestre recebe exatamente os mesmos 52.181 b e confere `df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1` — **D-V22-BYTES-PROJETO pronta para fechar** (operador repassa; casa não envia direto) · base da IA externa (rodada 34) saneada pelo mesmo ato; (4) projeto do mestre substitui `309aa65f…` (= upload r24 rotulado) quando o operador fizer o repasse.
- **Pendente do ato:** confirmar na próxima rodada que o mestre re-conferiu o sha no projeto dele (eco do repasse). Demais pendências inalteradas (rodadas 31–34).
- **0 ciência:** V7/manifesto/vínculos/P-8 reconferidos intactos.

## Rev.44 — 2026-09-19 (rodada 37: «o schema_vinculo_v1.1.json não é o atualizado?» — NÃO; cadeia medida ponta a ponta; vigentes entregues; precisão de governança sob a regra nova)
- **Pergunta do operador** sobre o arquivo baixado na rodada 36 (`schema_vinculo_v1.1.json`). Resposta verificada ANTES de responder (trilha 55: **30/30 VERDE**, reexecução limpa).
- **Medido — cadeia N2 (vínculo; a versão real vive no `$id` interno, não no nome do upload):** v1.1 `b0934412…` (15/09, 10.708 b) → v1.2 `19f4f29a…` (16/09) → v1.3 `ec4f0de8…` (17/09) → **v1.4 `d96ad15b…` (18/09) = VIGENTE corrente** ($id `L05/schema_vinculo_v1.4.json`). **Cadeia N1 (referência):** v1.1 `737bcda8…` → v1.2 `b8bcea80…` → **v1.3 `b06660fd…` = VIGENTE corrente** (uploads "(1)"≡"(2)" byte-idênticos). O v1.1 entregue na rodada 36 é o **1º elo, histórico** — entregue porque pedido pelo nome exato; o pedido veio provavelmente da citação defasada na V2.2.
- **Causas da confusão, nomeadas e medidas:** (a) uploads com nomes `v1`/`(1)`/`(2)` do navegador — versão real só no `$id`; (b) **a V2.2 OFICIAL `df7f7cfd…` cita `schema_referencia_v1.1.json` (§5.1, 1×) e `schema_vinculo_v1.1.json` (§5.2, 1×), 0× v1.3/v1.4** → dívida D-V22-SCHEMA-NOMES confirmada no documento oficial (correção editorial futura pela regra nova); (c) os vigentes ainda trazem `PROPOSTA v1.4 — nao normativo` na description interna (rótulo nunca atualizado pós-aceite).
- **PRECISÃO DE GOVERNANÇA à luz da regra nova (rev.42) — registrado com franqueza:** o que consta é aceite TÉCNICO do ciclo — comentador ("estruturalmente aprovados como base de fechamento do L-05", rodada 29, subscrito pela casa após réplica 52/52 + 26/26 casos sintéticos). Busca classificada no log (regex tripla → leitura linha a linha): **0 afirmações de aprovação formal do operador com sha/data sobre N1 v1.3/N2 v1.4; as 2 linhas casadas são PENDÊNCIAS de homologação (D4)**. Ou seja: vigentes de fato e validados em profundidade, mas o **selo final da regra nova falta** — igualdade exata com o caso V2.2 da rodada 35. **Sugestão da casa: ato formal simples do operador ("aprovado") → a casa grava sha/data dos dois JSONs e atualiza o ponteiro; e a futura emenda editorial da V2.2 (D-V22-SCHEMA-NOMES) já corrige os nomes no §5.1/§5.2.** Até lá, nenhuma frente trata outro arquivo como schema corrente.
- **Confissões de régua da casa (datadas, na trilha 55):** C55-1 contagem ≠ classificação (as 2 linhas "casadas" eram pendências; régua passou a classificar cada linha antes do veredito) · C55-2 slice [:14] com espaço · C55-3 caminhos do trio ciência desatualizados no script (V7 = nome próprio; manifesto em `Bibliografia/_manifesto_biblioteca.json`). Vereditos inalterados.
- **Entrega:** `ENTREGAS/2026-09-19_SCHEMAS_L05_VIGENTES/` — `schema_vinculo_v1.4__N2_VIGENTE.json` + `schema_referencia_v1.3__N1_VIGENTE.json` + minuta v1.4 (`78a0f2af…`) + LEIAME.txt + `SCHEMAS_L05_VIGENTES_2026-09-19.zip` (25.840 b; re-extraído confere byte a byte). O pacote antigo `ENTREGAS/2026-09-19_SCHEMAS_L05/` (v1.1) fica como histórico — o vigente é o de hoje.
- **0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos `490675e6…` intactos início→fim (caminhos corrigidos e medidos).

## Rev.45 — 2026-09-19 (rodada 38: «estou montando o motor clínico com uma IA externa — o 1.4 ainda não está aprovado?»)
- **Pergunta de governança sobre documento normativo em uso ATIVO.** Resposta ancorada na trilha 55 (30/30, rodada 37 — sem entrada nova desde lá).
- **Resposta registrada:** N2 v1.4 `d96ad15b…` (e o irmão N1 v1.3 `b06660fd…`) = **tecnicamente validado e corrente de fato** (aceite do ciclo r29: comentador + casa, 52/52 + 26/26) · **formalmente AINDA NÃO aprovado pelo operador** no padrão da regra nova (rev.42) — as únicas menções no log são pendências de homologação (D4). Mesma situação da V2.2 antes da rodada 36.
- **Alerta operativo ao operador (risco concreto):** a V2.2 oficial cita os nomes **v1.1** (§5.1/§5.2 — D-V22-SCHEMA-NOMES). Uma IA montando o Motor seguindo a V2.2 ao pé da letra pode ancorar no schema ERRADO (v1.1, histórico). Orientação dada: qualquer IA do ciclo deve usar **N2 v1.4 `d96ad15b…` + N1 v1.3 `b06660fd…`**; conferência por sha256.
- **Na mesa do operador (decisão simples, 1 palavra):** «aprovado o v1.4 e o v1.3» → casa grava sha/data e o selo formal fecha (cadeia regra nova completa); se preferir, aprovação condicionada à leitura da especificação v1.4 (já entregue na pasta _VIGENTES).
- **0 ciência:** sem toque no acervo; resposta foi citação de medida já gravada (trilha 55).

## Rev.46 — 2026-09-19 (rodada 39: RÉPLICA do parecer do auditor-2 sobre «schema_vinculo_v1.1» — trilha 56: 26/26; veredito substantivamente correto + 3 precisões nomeadas; dívida nova D-L05-NOME-X-ID)
- **Entrada:** parecer do auditor-2 (verbatim `82a8b5b4…` arquivado com digitais) respondendo ao operador se ele sabia da "versão 1.1".
- **Replicado e CONFERE (26/26):** tabela de 4 shas/datas EXATA byte a byte (b0934412·19f4f29a·ec4f0de8·**d96ad15b=vigente**) · prefixos do eco dele batem · carta 8 publica as digitais ✔ · `L05/` = caminho declarado (0 diretórios) ✔ · ponteiro defasado na V2.2 oficial (§5.1/§5.2 citam v1.1, 0× v1.3/v1.4) ✔ — **e é a D-V22-SCHEMA-NOMES, nomeada pela casa na rodada 36: redescoberta convergente** · catálogo d0ff2647 existe e adoção formal pendente ✔ · **20 redirecionados/0 `ancoras` EXATO** (274 totais) · portão L-05 não nascido ✔ (3 regras mapeiam: V-17 · condicao×BLOCO_07/08 · padrão avaliador E2=rev.A3-E2) · enum origem_pipeline sem CLAIM_KIT_CLINICO ✔ · "renomear não muda sha" medido ✔ · "schema é PROPOSTA/não normativo" = posição da casa das rodadas 37–38 ✔.
- **PRECISÃO P1 (autoria):** "a casa aprovou como base de fechamento" → a frase de aceite é do COMENTADOR (r29); a casa SUBSCREVEU após réplica 52/52, com ressalvas não-estruturais nomeadas (D2 · adoção formal · homologação D4).
- **PRECISÃO P2 (genealogia — a única afirmação factual FALSA do parecer, derrubada na bancada):** "a prosa do §5.2 descreve a v1.4 porque menciona direção da relação e condição, que nasceram ali" → **medido nas 4 versões: `condicao`+`direcao` existem desde a v1.1** (rename p/ `direcao_suporte` na v1.2); o §5.2 é byte-idêntico desde 15/09 (contemporâneo da v1.1) e compatível com ela. O defeito real é SÓ o nome/versão do ponteiro (D-V22-SCHEMA-NOMES). A gravidade extra alegada não existe nos bytes.
- **PRECISÃO P3 (verificabilidade):** "pendente do meu parecer de ontem: CLAIM_KIT_CLINICO no enum do N1" — **0 arquivos na base arquivada · 0× na minuta v1.4** → os bytes desse parecer não chegaram à casa; PEDIDO ao operador: enviar. Mérito registrado como PROPOSTA subordinada à homologação da letra B + regra nova (alterar enum do N1 exige a cadeia completa).
- **CONFISSÃO/DÍVIDA NOVA da casa (D-L05-NOME-X-ID):** o auditor-2 tem razão no §1 — a carta 3 da casa registrou nome≠conteúdo **sem nomear defeito**; e o nome `schema_vinculo_v1.1.json` existe desde 15/09 no acervo verbatim como MARCA DE ARQUIVAMENTO da casa (o recebido chamava-se `schema_vinculo_v1.json`). A "busca impossível" do operador nasceu do par (nome citado na V2.2 oficial) × (arquivo que só existe com esse nome no arquivamento). Citação dele da carta 3: sentido exato, forma não-literal ("conteúdo" pertencia ao objeto-referência).
- **Confissões de régua da trilha (datadas):** C56-1 (implícita no B4: nuance arquivamento) · C56-2 self-match da agulha (régua exclui os artefatos da própria trilha) · C56-3 varredura global passou a bytes p/ agulha ASCII (UnicodeDecodeError em binário) · C56-4 tmp fora do workspace (PermissionError).
- **Sobre a sugestão dele (renomear arquivo + corrigir §5 da V2):** tecnicamente sha-invariante (medido); **decisão é do operador** e a correção do documento OFICIAL exige a regra nova completa (proposta → documento completo → aprovação → sha/data). Casa pode preparar a emenda editorial completa (V2.2 §5.1/§5.2 + tabela de nomes) sob encomenda.
- **0 ciência:** V7/manifesto/vínculos intactos início→fim.

## Rev.47 — 2026-09-19 (rodada 40: operador autoriza ("ok pode fazer") → EMENDA EDITORIAL 01 da V2.2 preparada como CANDIDATA pela regra nova — trilha 57: 11/11; NADA instalado)
- **Registro de governança (precisão):** "ok pode fazer" = autorização para PREPARAR. A aprovação (regra nova: PROPOSTA→DOCUMENTO→APROVAÇÃO→SHA/DATA→VIGENTE) fica para a linha de fecho do operador — nem a emenda nem o selo formal dos schemas foram gravados como vigentes.
- **CANDIDATA construída e medida (11/11):** base `df7f7cfd…` intacta · escopo fechado (as únicas 2 ocorrências de 'v1.1' do documento — linhas 269/306, ambas ponteiros) · construção EM BYTES: CRLF 1411/1411 · 0 LF solto · 30 seções únicas · H1 preservado · **diff = exatas 3 linhas substituídas, 0 inseridas/removidas** · sufixo §3→fim preservado fora §5 (âncoras da auditoria r34 não quebram).
- **Candidata:** sha `3cbc131d687610d9…` (52.476 b) · arquivo marcado CANDIDATA na série · linha Rev ganha cláusula "· **Emenda editorial 01 — 2026-09-19**: …D-V22-SCHEMA-NOMES · 0 conteúdo normativo alterado" (estilo da própria linha Rev; identidade V2.2 preservada como em V2.1→V2.2; rótulo alternativo, ex. V2.3, reemendo sem custo).
- **Confissão de régua (C57-1):** contagem global ingênua falhou porque a própria cláusula da emenda cita os 4 nomes (2 antigos+2 novos); régua corrigida para por-linha (269/306/Rev=4). Construção estava certa; a régua, errada. Datada na trilha.
- **Pacote de submissão (documento completo + diff + proveniência = regra nova):** `ENTREGAS/2026-09-19_EMENDA_V22_E01_CANDIDATA/` (md candidato + RELATORIO_SUBMISSAO + zip; re-extração confere).
- **Na mesa do operador (1 linha sela tudo):** "APROVADO: emenda editorial 01 da V2.2 E os schemas N1 v1.3 / N2 v1.4" → grava vigência da emenda (sha/data) + selo formal dos schemas (fecha rodada 38) + ponteiro com histórico preservado + repasses. Alternativas registradas no relatório. Segue pendente: bytes do "parecer de ontem" do auditor-2 (CLAIM_KIT_CLINICO).
- **0 ciência:** V7/manifesto/vínculos intactos início→fim.

## Rev.48 — 2026-09-19 (rodada 41: DECISÃO DO OPERADOR — número de versão no cabeçalho · CANDIDATA V2.3 medida (trilha 58: 12/12) · 3 cartas geradas · REGRA PERMANENTE de downloads registrada verbatim)
- **Decisão do operador (verbatim):** "tem que mudar a versão e colocar no cabeçalho porque mudou aí há uma rastreabilidade de versão e saberemos qual é a vigente atual, só mudar a data é pouco, precisa mudar o número da versão". A candidata "emenda editorial 01" da rodada 40 (`3cbc131d…`) vira SUPERSEDED antes de nascer (decisão de rótulo; 0 custo — trilha 57 preservada como histórico).
- **CANDIDATA V2.3 construída e medida (12/12):** H1 «…PLATAFORMA V2.3    19.09.26» · linha Rev «Rev. V2.3 — 2026-09-19» com o histórico INTEIRO da Rev V2.2 preservado na mesma linha · §5.1→`schema_referencia_v1.3` · §5.2→`schema_vinculo_v1.4` · **diff = exatas 4 linhas substituídas (1·4·269·306), 0 ins/rem · CRLF 1411/1411 · 30 seções intactas · L167 "(Rev. V2.2, 2026-09-17)" FICA** (proveniência histórica correta da regra do §2). sha **`498e7df9d8abe8be…`** · 52.740 b.
- **REGRA PERMANENTE NOVA (verbatim do operador, vigente desde já):** "apartir de agora qualquer conversa que gerou uma mudança no documento, seja ele qual for, você tem que me disponibilizar para download para eu ter controle do que está acontecendo." → a casa batiza **R-DOWNLOAD-SEMPRE**: toda mudança documental (qualquer documento) gera pacote datado em `ENTREGAS/` no ato. Primeira aplicação = esta rodada.
- **3 cartas geradas (na série `CARTAS_V23_2026-09-19/` + cópias na entrega):** CARTA 18 ao Auditor-Mestre (substituir por vigente D-V22-BYTES-PROJETO · depois V2.3 · pendências intactas) · CARTA 9 ao Auditor-Estrutura (convergência do ponteiro · 3 precisões da trilha 56 · pedido dos bytes do parecer CLAIM_KIT_CLINICO) · CARTA ao Comentador (aceite r29 intacto · regra nova · ancoragem por sha). Todas: candidata marcada CANDIDATA, vigente hoje = V2.2 `df7f7cfd…`.
- **Confissão C58-1 (registrada na trilha):** `.replace()` global em bytes, executado depois de inserir a cláusula da Rev, devorou as citações históricas "v1.1 → …" dentro da própria cláusula — a régua C5 pegou (0 linhas com v1.1). Ordem corrigida (ponteiros primeiro, cláusula depois) + guarda C3b contra regressão. Candidata final válida = `498e7df9…` (a intermediária `6fb90955…` da execução com a régua furada está descartada e marcada).
- **Governança:** ponteiro NÃO movido — vigente oficial permanece V2.2 `df7f7cfd…` até aprovação do operador. Na mesa: "APROVADO: V2.3 (498e7df9…) E os schemas N1 v1.3 / N2 v1.4".
- **0 ciência:** V7/manifesto/vínculos intactos início→fim.

## Rev.49 — 2026-09-19 (rodada 42: pacote NEUTRO de distribuição dos schemas + posição antiviés da casa sobre quem recebe o quê)
- **Pedido do operador:** zip dos schemas para enviar às frentes; dúvida de desenho: auditor-2 "talvez não precise"; mestre? — lembrando o princípio que a própria casa registrou (cada frente trabalha sem ver a outra).
- **Posição da casa (critério declarado):** segregação vale para PARECER/TRABALHO, não para ARTEFATO COMUM — todas as frentes podem receber os mesmos bytes normativos (calibram sobre o mesmo alvo); o que nunca circula é o que uma frente DISSE antes da outra trabalhar. Consequência: **LEIAME neutro** (0 menções a qualquer frente, check na trilha 59) — o mesmo pacote serve a qualquer destinatário sem contaminar. Minimalismo de alçada: auditor-2 = dispensável (é o autor; ecoou v1.4 oficial na r39) · comentador = OK (ancora pareceres futuros) · mestre = recomendação de ADIAR (alçada atual = L-NT/20 pilotos, não depende dos schemas; entra no pacote dele quando o eixo do contrato do Motor abrir, junto com a V2.3 aprovada) — mas se o operador preferir uniformidade, o mesmo zip serve sem violar o antiviés.
- **Entrega (trilha 59: 3/3):** `ENTREGAS/2026-09-19_SCHEMAS_L05_CORRENTES_DISTRIBUICAO/` — N1 v1.3 `b06660fd…` + N2 v1.4 `d96ad15b…` + especificação v1.4 + LEIAME neutro + zip (25.015 b, re-extração confere). Nota de status no LEIAME: rótulo interno "PROPOSTA — não normativo" herdado (dívida editorial conhecida) + selo formal do operador pendente.
- 1ª execução da trilha falhou por compreensão de lista torta (check c1) — simplificada; confessado no JSON da trilha. **0 ciência.**

## Rev.50 — 2026-09-19 (rodada 43: resposta do auditor-2 à carta 9 · eco V2.3 conferido pela frente · causa raiz unificada subscrita · PACOTE DE LINHAGEM entregue (trilha 60: 6/6) · alerta: "Como Executar v1.9" existe fora da casa)
- **Entrada:** resposta do auditor-2 (verbatim `8112a4c0…` arquivado). Réplica dos pontos:
- **(i) Eco da V2.3:** ele recalculou a digital `498e7df9…` idêntica, 52.740 b, 1411 CRLF, ponteiros e L167 conferem → **verificado: exato** (nossa trilha 58 bate). "Sem objeção" registrado como evidência convergente — **NÃO substitui a aprovação formal do operador** (elo que falta na regra nova).
- **(ii) Correção (b) aceita por ele COM causa raiz elegante:** ele nunca manteve cópias versionadas (sobrescrevia o mesmo arquivo; versão só no `$id`) → reconstruiu genealogia pelo changelog e o rename v1.2 o induziu ao erro de nascimento. Equação dele **subscrita pela casa**: D-V22-SCHEMA-NOMES × D-L05-NOME-X-ID = **mesmo defeito (nome parado × versão viva no $id) visto de dois lados**. Honestidade técnica reconhecida e registrada.
- **(iii) PONTO ÚNICO DE FALHA (procedente e sério):** as cópias versionadas existiam só no acervo da casa. **Respondido no ato:** PACOTE DE LINHAGEM `ENTREGAS/2026-09-19_L05_LINHAGEM_COMPLETA/` — 7 schemas (N1 ×3 · N2 ×4, shas oficiais conferidos) + 5 especificações md (incl. a doença head-v1.0×v1.x-efetivo, marcada) + MANIFESTO com 12 digitais + regra de verificação. **Camada de distribuição adota a partir de agora nome do arquivo == `$id`** (a sugestão dele aplicada na prática; série verbatim preserva nomes de recebimento = arqueologia do trânsito). Proposta de regime: espelhamento bilateral via manifesto datado a cada mudança (1ª aplicação = este pacote).
- **(iv) Proposta CLAIM_KIT_CLINICO (§5 transcrito com crédito):** premissa verificada — enum `origem_pipeline` do N1 = 5 valores (trilha 56) e nenhum cobre o fluxo do kit ✔; a regra proposta (não apagar a distinção de procedência) é coerente; permanece subordinada à homologação do fluxo (letra B) + alteração formal do N1 pela regra nova. Posição dele ("se o fluxo não for homologado, a proposta morre junto") — correta, subscrita.
- **(v) PENDENTE → PEDIDO AO OPERADOR:** os 2 arquivos reenviados por ele (parecer "Claim Kit → N1/N2" + **"adendo sobre o Como Executar v1.9"**) NÃO chegaram à casa — enviar verbatim. **ALERTA DE GOVERNANÇA DOCUMENTAL:** a casa só conhece "COMO EXECUTAR **v1.7**" no acervo; **v1.8/v1.9 nunca passaram por aqui** (0 bytes) — se existem, precisamos da cadeia (v1.8? · v1.9) para arquivar/medir; é o mesmo padrão de ruptura da V2.1→V2.2.
- **(vi) Renomear arquivos-oficiais aos $ids:** subscrito tecnicamente (sha-invariante, provado; sanado na distribuição desde já); decisão formal continua do operador, junto do selo.
- **Mesa do operador (acumulada):** frase "APROVADO: V2.3 (498e7df9…) E os schemas N1 v1.3 / N2 v1.4" · bytes: parecer Claim Kit + adendo v1.9 + COMO EXECUTAR v1.9 (e v1.8 se existir) · decisão sobre o renome oficial.
- **0 ciência:** intacta.

## Rev.51 — 2026-09-19 (rodada 44: mapa de estado do projeto registrado · mistério do "v1.1" RESOLVIDO · Roteiro = byte-idêntico ao da base r34 · pacote dedicado à IA externa do motor (trilha 61: 3/3))
- **Mistério resolvido (registro):** quem pediu "schema_vinculo_v1.1" (rodada 36) foi a **IA externa que desenha o contrato/motor clínico** — ela leu a V2.2 com o ponteiro defasado (§5.2 → v1.1). Convergência: mesma classe de base-superseded da auditoria r34. A V2.3 que o operador envia a ela corrige exatamente a armadilha em que ela caiu.
- **"Como Executar v1.9": REBAIXADO** — não existe documento; é discussão futura (o adendo do auditor-2 refere-se a ela). Os bytes do adendo + parecer Claim Kit seguem aguardados (pedido mantido).
- **Mapa de estado (verbatim do operador, registrado):** auditor-mestre PAUSADO · auditor-estrutura PAUSADO · grupo de claims clínicos PAUSADO — todos aguardando a conclusão do contrato/motor pela IA externa + comentador; foco do operador: liberar tudo de uma vez após o motor. Filas internas da casa permanecem à disposição, sem despacho enquanto as frentes estão pausadas.
- **Roteiro de Trabalho recebido = `5e3f9163…` (22.447 b) BYTE-IDÊNTICO ao já arquivado na base da auditoria r34** — eco registrado; nenhum acréscimo; suas marcações (checklist §13) já foram auditadas na rodada 34. Nota de precisão: o Roteiro §3 normatiza o fluxo multi-IA dos claims e o §13 traz status — mantém-se subordinado à Filosofia/Arquitetura (hierarquia G19 segue pendente do operador).
- **Entrega:** `ENTREGAS/2026-09-19_PARA_IA_EXTERNA_MOTOR/` — V2.3 candidata + N1 v1.3 + N2 v1.4 + especificação + LEIAME neutro (check antiviés: 0 menções a frentes) + zip. Nota no LEIAME: "se você leu a V2.2, os ponteiros §5 citavam v1.1 — a V2.3 corrige; o restante é idêntico". **Regra de frente nova cumprida: só artefatos, nunca conversas.**
- **Mesa do operador (inalterada):** "APROVADO: V2.3 (498e7df9…) E os schemas N1 v1.3 / N2 v1.4" · bytes do adendo+parecer do auditor-2 · palavra sobre renome-oficial aos $ids.
- **0 ciência:** intacta.

> **NOTA datada — 2026-09-19 (pós-rodada 44):** reenvio do "ROTEIRO DE TRABALHO DA PLATAFORMA.md" pelo operador
> ("esqueci de te enviar"). Medido de novo: sha `5e3f916335c4d631c2639e2aaf8efd48c98f6762e263ff301c4dfc9022bd04ac`
> · 22.447 b — **byte-idêntico** ao upload anterior e ao arquivado na base da auditoria r34. Eco duplo registrado;
> nada a verificar, nenhuma mudança. 0 ciência.

## Rev.52 — 2026-09-19 (rodada 45: MESTRE responde à carta 18 — trilha 62: 7/7 · eco V2.3 exato · âncoras L-NT idênticas · CONFLITO do arquivo do projeto provado dos dois lados + CONFISSÃO de caracterização da casa)
- **Entrada:** resposta do mestre (verbatim `1817615d…` arquivado).
- **Verificados exatos (7/7):** sha V2.3 + estrutura (1411 CRLF · "H1 se identifica — V-16 cumprida" ✔) · ponteiros 269/306 ativos ✔ · residuais v1.1 (2 substrings) e UNIFICADOS (1×) só na Rev-L4 = histórico ✔ · **âncoras L-NT §§6/7/13/14 V2.2 ≡ V2.3 (sha por seção idêntico)** ✔ · N-4/herança `uso` na minuta L-NT (`N-4`, "`uso` herdado do kit", NT-05→N-4) ✔ · "V2.3 contém os 4 marcadores 3/1/1/1" ✔.
- **CONFLITO (a peça central da resposta dele):** o arquivo do projeto `309aa65f…` tem 0/4 marcadores novos e diverge da V2.3 em §2/§5/§21 → **VERDADEIRO: o projeto não contém a V2.2 oficial** (= D-V22-BYTES-PROJETO, agora provada por medição dele + cruzamento nosso). Correção dele sobre a própria análise V2.1×V2.2 (comparou com o arquivo errado; "o arquivo do projeto não contém `origem_conhecimento`; a V2.2 oficial contém") — **exata e registrada**.
- **CONFISSÃO DE CARACTERIZAÇÃO DA CASA (datada):** teste cruzado no upload r24 (que TEMOS) — os 3 marcadores §2-novo são 0 (bate com o projeto), **MAS "O Motor busca ativamente" = 1× na L82 do r24 × 0 no projeto (declarado pelo mestre)** → `309aa65f` **NÃO é byte-idêntico ao upload r24**: a fórmula "upload r24 rotulado" (carta 18) estava imprecisa. O que permanece verdadeiro: SUPERSEDED, não-oficial, e não contém o endurecimento de proveniência. **PEDIDO NOVO ao operador: exportar do projeto o arquivo `309aa65f…` e enviar verbatim → a casa identifica exatamente qual elo é e aposenta a ambiguidade.**
- **Schemas para o mestre — posição da casa REVISADA (ele pediu com causa de trabalho: auditar D-02/N-1/NT-03/NT-04 do L-NT):** enviar já o zip neutro existente `ENTREGAS/2026-09-19_SCHEMAS_L05_CORRENTES_DISTRIBUICAO/` (serve; minimalismo satisfeito pelo pedido nominal do mestre). Registrou como "declaradas pela casa, não verificadas" — ao receber, ele ecoe os shas.
- **Pendências dele atualizadas:** `DELIBERACAO_FLUXO_CLAIM_CLINICO_2026-09-18.md` — **0 bytes na base da casa (confirmado por glob) → pedido formal dos bytes verbatim** (a posição B dele bate com o consolidado r32 e com a casa) · piloto 20 + minuta 2 L-06 + minuta 2 L-NT na fila (condição: "de onde a NT tira o conhecimento clínico" = decisão do operador, já nomeada).
- **Recomendação da casa (ordem):** (1) repassar JÁ a V2.2 oficial ao projeto mestre (`ENTREGAS/2026-09-19_V2.2_OFICIAL/` pronto) → fecha D-V22-BYTES-PROJETO com eco; (2) enviar ao mestre o zip neutro de schemas; (3) pedir o DELIBERACAO; (4) mesa-mãe: "APROVADO: V2.3 (498e7df9…) E os schemas N1 v1.3 / N2 v1.4".
- **0 ciência:** intacta início→fim.

## Rev.53 — 2026-09-20 (rodada 46: CARTA 19 ao Auditor-Mestre — pedido dos bytes da deliberação do fluxo claim + anúncio de envio da V2.2 oficial e dos schemas L-05 correntes — trilha 63: 10/10)
- **Pedido do operador (escopo desta rodada):** carta ao mestre pedindo a deliberação (`DELIBERACAO_FLUXO_CLAIM_CLINICO_2026-09-18.md`) e dizendo que ele envia junto os schemas L-05 e a V2.2 oficial.
- **CARTA 19 escrita e medida (trilha 63: 10/10):** sha `c2f799d621b5b2e768f322471c69ed6925f6614f57270aed5ecd57de2d717a49` (5.638 b) · série em `_documentos_serie/CARTA19_MESTRE_2026-09-20/` + pacote datado `ENTREGAS/2026-09-20_CARTA19_MESTRE/` (carta + DIGITAIS + zip `e2cf2a71…`; re-extração ≡ disco). **R-DOWNLOAD-SEMPRE cumprida no ato.**
- **Conteúdo da carta (5 blocos):** (1) acuse da r45 (7/7) + confissão da casa sobre `309aa65f` reafirmada; (2) envio — zip V2.2 oficial `1444ae44…` (substituir já o arquivo do projeto e ecoar sha → fecha D-V22-BYTES-PROJETO; V2.3 depois, só candidata ainda) + zip schemas correntes `72f8f2e5…` (N1 v1.3 `b06660fd…` · N2 v1.4 `d96ad15b…` · nomes==`$id`) com nota franca de governança (validados tecnicamente r29 — 52/52 + 26/26; **selo formal pendente**; rótulo "PROPOSTA — não normativo" herdado) — os shas deixam de ser "declarados pela casa" após o eco dele; (3) **PEDIDO CENTRAL:** bytes verbatim da deliberação — varredura global na base = **0 ocorrências do nome** (trilha 63, C05) → posição B registrada como "declarada, não verificada"; finalidades: extrair os "ajustes" + conferir herança `uso` contra enunciado (N-4 já verificado na Minuta 1); (4) pedido secundário mantido: export `309aa65f…` do projeto; (5) fila inalterada.
- **Guarda antiviés/anticipação (C08):** a carta NÃO contém eco antecipado de aprovação (0 ocorrência de "APROVADO: V2.3") — a frase de selo segue na mesa do operador, não na boca da casa. Régua: 8 marcadores obrigatórios presentes, variáveis por substring em texto NFC (camada declarada).
- **Confissão C63-1 (datada no JSON):** 1ª execução da trilha falhou por desempacotamento de tupla no dict CIENCIA (FileNotFoundError imediato; nenhuma medida fabricada) — mesma classe da C62-1. Corrigido, reexecutado: 10/10.
- **O que acompanha fisicamente a carta no envio do operador:** os 2 zips de 2026-09-19, INALTERADOS (trilha 63 re-extraiu e conferiu: V2.2 ≡ série · schemas 4/4). Estado normativo intocado: vigente = V2.2 `df7f7cfd…` · candidata V2.3 `498e7df9…` aguardando a frase.
- **0 ciência:** trio intacto início→fim (C07/C10).

## Rev.54 — 2026-09-20 (rodada 47: correção de trânsito — os bytes da deliberação EXISTIAM desde 18/09; chegaram · réplica empírica COMPLETA da deliberação (trilha 64: 14/14) · CARTA 19 REFEITA (v2) antes de sair)
- **Correção do operador (registro honesto de trânsito):** o mestre tinha razão — a deliberação (`DELIBERACAO_FLUXO_CLAIM_CLINICO_2026-09-18.md`) estava disponibilizada desde 18/09; o elo que faltou foi o repasse do lado da casa/operador. Upload recebido · medido · arquivado verbatim: sha `fe5a18b3542305014147cf85d00676b4b92d483453c8d04fe331b8a5b5536543` (8.141 b · 115 linhas · LF) em `_documentos_serie/MESTRE_deliberacao_fluxo_claim_recebida_2026-09-20/` (+DIGITAIS). A dívida de bytes da rev.52 está **encerrada como VERIFICADA**; a carta 19 v1 (que a pedia — `c2f799d6…`) vira SUPERSEDED arquivada na série CARTA19.
- **Réplica da deliberação (política da casa: medir antes de comentar) — VERIFICADO em tudo que é mensurável:** (i) veredito no texto "B — concordância com ajustes" (1 estrutural + 3 de precisão, 4 pedidos de fecho) ✔; (ii) os 2 arquivos-base dele (LISTA `3252a920…` · BLOCO `0a630dba…`) são byte-idênticos ao acervo da casa ✔; (iii) §2 exato: 41 alvos · 22 entradas · **21 sem = |Lista−Bloco| (interseção 20 — o Bloco carrega .012b/.012c não-listados; convergente com a trilha 33)** · 8 aprovado + 14 com_ressalva ✔; (iv) §3: 12/12 campos exatos (régua que casa as 12 medidas = substring `chave:` no BLOCO inteiro: pmid 158 · autor 37 · ano 41 · nivel 39 · especie 25 · comparador 48 · achado 52 · papel 36 · evidence_role 22 · uso 23 =22 ancoradas+1 interna · moderadores 22 · statement 22) ✔; (v) §1: 49 pmids únicos (seção, regex trilha33) × 237 fichas V7 → **39 ausentes** ✔ · wiring zero nas 2 faces (22/22 `usado_em_biblioteca: nao` · 0 fichas `claim_id_origem B1.SM02.*` no acervo) ✔; (vi) quotes V2.2: §6 (L446–447) exatas ✔ · NT-02/N-4/"uso herdado do kit" na minuta `294119b9…` ✔; (vii) contra a proposta (`4ede1c81…`): "os 35" ✔ · item 13 ressalva ✔ · §3/§10/§5: percurso claim→Evidências/Bibliografia→N1→N2 com "Biblioteca Correspondente" 0× ✔ · papel do mestre L215 ✔.
- **2 precisões de citação (essência correta; literal registrado):** (a) §5.5 V2.2 L421: "…o aprofundamento **específico** do objeto **científico**." — a forma dele suprime adjetivo+substantivo; (b) proposta L215: "coorden**a** a transformação do resultado em N1/N2 **conforme os contratos vigentes**" — ele citou na forma infinitiva e sem o sufixo. Nenhuma altera sentido; registradas porque quote é medida.
- **Confissão C64-1 (datada no JSON):** C05 falhou na 1ª corrida (13/14) por aritmética cega da casa (41−22==21, falso); régua correta por conjunto salvou a tabela dele INTEIRA — mesma lição da C55-1.
- **Posição da casa sobre a matéria (declarada como posição — decisão é do operador):** a medição sustenta o ajuste estrutural; a saída **(i)** — bifurcação: afirmação→Biblioteca da entidade pelo rito normal (§5.5) · evidência→N1→N2→NT (rastreabilidade) — preserva a fonte única de conhecimento sem tocar contratos; subscrita. Os 4 pedidos de fecho dele (§6) entram na mesa do operador junto com a homologação da letra B (inclui destino da ressalva em N2 e número real do piloto 41/22/21). **Minuta 2 do L-NT: condicionada por ele à decisão (i)×(ii) — "cabe em uma linha" — aguarda só a palavra do operador.**
- **CARTA 19 v2 final:** sha `74e1e1cbe415870dbe3b865c9fe6435ea864dd5db1e0e11bf0d6dabbf5d7e6f2` (7.623 b) — acuse da deliberação verificada + finura da régua do 21 + envios (V2.2 oficial → eco fecha D-V22-BYTES-PROJETO · schemas correntes → eco transforma "declaradas" em "verificadas") + único pedido aberto: export `309aa65f…`. Guarda C11: 0 "APROVADO: V2.3" (a frase de selo fica só na mesa do operador). Pacote `ENTREGAS/2026-09-20_CARTA19_MESTRE/` re-feito (md+zip+2 DIGITAIS; re-extração ≡ disco) — R-DOWNLOAD-SEMPRE.
- **Nota antiviés (para o operador):** a deliberação é parecer de uma frente — NÃO circular a outras frentes; se quiser distribuir, a casa monta pacote de artefatos neutros.
- **0 ciência:** trio intacto início→fim (C01/C14).

## Rev.55 — 2026-09-20 (rodada 48: pergunta de governo do operador — "a aprovação (V2.3/schemas) não deveria ser dos auditores/bancada, com base em ciência e engenharia?")
- **Posição da casa (registrada com clareza):** NÃO. Separamos dois verbos "aprovar": (1) **conformidade técnica** (= o que é mensurável: diff, shas, réguas, ecos — isso as IAs e a bancada já cumpriram; declaração honesta máxima da medição: "não há impedimento técnico conhecido"); (2) **vigência normativa** (= "este documento passa a ser a lei do projeto": ato de governo, não sai de cálculo; cabe SÓ ao operador — desenho intencional da ponte um-a-um).
- **Razões (engenharia + histórico da mesa):** separação produção × auditoria × decisão — o próprio mestre reafirmou no §4 da deliberação (quem produz não confere o próprio artefato); estendemos: quem audita não coroa o próprio parecer ("quem audita o auditor" falharia no ponto mais sensível). Histórico real: mestre reconheceu 4+ erros, auditor-2 errou genealogia, a casa errou de régua 2+ vezes na semana — se uma frente aprovasse, cada um desses erros teria virado lei; o elo que capturou todos foi a ponte com o operador. Autoridade ≠ competência: nenhuma IA responde pelo projeto.
- **Analogia registrada:** auditores = reviewers/CI · bancada = CI local que reexecuta antes de aceitar · operador = maintainer com a chave do merge. Reviewer assina review; merge é do maintainer.
- **Precisão:** V2.3/schemas são troca de ponteiros + rótulo — 0 ciência dentro; "baseada na ciência" não se aplica aqui. Quando a decisão for científica (ex.: aceite de claim), a régua manda evidência — e mesmo assim a casa recomenda assinatura do operador sobre o parecer, porque a ciência também já pegou erro de IA.
- **Oferecimento:** dossiê go/no-go de 1 tela por submissão (mudança · quem mediu · réguas de ambos os lados · faltas) → a assinatura do operador leva segundos e fica soberana. Classe delegável futura: SÓ por contrato normatizado pelo operador (quais classes, quais réguas) — nunca por hábito informal.
- **0 ciência:** trio reconferido e intacto (medida gravada nesta rodada; conversa conceitual, nenhum artefato tocado).

## Rev.56 — 2026-09-20 (rodada 49: operador ESCLARECE seu modelo de aprovação — e a casa subscreve como contrato de regime)
- **Verbatim do sentido (registrado):** "quando todas [as IAs] derem como fechado tal assunto ou documento aí sim vejo que não há porque no presente momento não dar como aprovado" · "a IA vai fazer a rastreabilidade e vai apontar que da forma que está vai funcionar ou não, baseado na engenharia ou na ciência" · "após terminada toda a plataforma posso levar por especialistas e pedir auditoria e averiguação".
- **A casa subscreve — é exatamente a separação da rev.55 em outra formulação:** as frentes emitem VEREDITO TÉCNICO sobre engenharia/ciência com rastreabilidade (cada uma na sua alçada) → o operador aprova **sobre dossiê convergente** (nunca no escuro, nunca delegando) → **especialistas humanos ao fim** = a camada de auditoria de regime (independente das IAs, sobre artefatos periciáveis). A frase de aprovação do operador não é um ato solitário: é a assinatura de governo em cima do consenso verificado.
- **Duas precisões da casa (para o modelo funcionar de verdade):** (a) rastreabilidade ≠ "vai funcionar" — a 1ª prova ligação/procedência; a 2ª é valoração funcional (casos sintéticos, portões, pilotos — ex.: 52/52+26/26 dos schemas, P-8 2 ERRO abertos, piloto de 20 NT pendente); o "fechado" de cada assunto precisa de definição por checklist, senão vira impressão; (b) nenhuma frente sozinha cobre "o programa funciona conforme a filosofia" — o veredito é por PEÇA (documento, schema, contrato, claim), e o "fechado" global é a soma das peças fechadas com o mapa delas na mesa.
- **Estado do seu critério "todas fecharam", medido hoje:** V2.3 = 3/3 ecos (casa 58/62 · mestre r45 · auditor-2 r43) → **pronta para sua frase**; schemas N1 v1.3/N2 v1.4 = casa (48: 52/52+26/26) + comentador (r29: "estruturalmente aprovados") + auditor-2 (autor/eco v1.4) = fechados por 3 frentes, **faltando o 4º eco: o mestre recalcular os bytes que você enviará agora** (audita D-02/N-1/NT-03/NT-04) — o envio atual fecha exatamente esse elo.
- **Oferecimento (mantido e agora operacional):** dossiê go/no-go de 1 tela por submissão: assunto · mudança · quem mediu e o quê · réguas · falta o quê · frase sugerida de 1 linha. E para o futuro dos especialistas: o acervo já é periciável por desenho (série verbatim + trilhas reexecutáveis N/N + confissões datadas + manifestos sha); no fim a casa monta o DOSSIÊ PERÍCIA EXTERNA (índice de contratos vigentes + cadeia de versões + filas abertas) — especialista audita artefato com procedência, nunca fé no relato.
- **0 ciência:** trio reconferido e intacto (conversa conceitual, 0 artefato tocado).

## Rev.57 — 2026-09-20 (rodada 50: mestre instala a V2.2 oficial e ECOA — D-V22-BYTES-PROJETO fechada pelos dois lados · FÓSSIL 309aa65f cravado · 3 correções novas dele ao L-NT VERIFICADAS na especificação · 'Como Executar v1.9' desconhecido da casa · comentador certo no método, 2 premissas imprecisas — trilha 65: 14/14)
- **Eco do mestre (verificado EXATO):** instalou a V2.2 oficial (`df7f7cfd…` · 52.181 b · 1.411 CRLF) — o projeto passa a conter as 3 cláusulas e o H1 que se identifica; **D-V22-BYTES-PROJETO FECHADA bilateralmente** (nossa recomendação da rev.52 cumprida). Eco também da V2.3 `498e7df9…` e da especificação v1.4 `78a0f2af…` (≡ bytes da nossa distribuição). Precisão dele VERDADEIRA e adotada: a carta publicava sha dos zips mas não a do md isolado — **a partir de agora, shas individuais constam nas cartas** (confissão leve da casa, registrada).
- **FÓSSIL cravado (a confissão da rev.52 FECHA):** o export `309aa65fa75de6b…` (51.235 b · 1.421 linhas CRLF · H1 «…PLATAFORMA V2    15.09.26» · 0/4 cláusulas · ponteiros v1.1) **não é byte-idêntico a nenhum elo que a casa já teve** — é um 4º artefato "V2 15.09.26" (distinto de: série SUPERSEDED 46.129 b · upload r24 50.964 b · V2.2 oficial 52.181 b). Ou seja: o projeto do mestre rodou com um intermediário desconhecido até da casa. Arquivado na série com DIGITAIS. A fórmula da carta 18 ("upload r24 rotulado") fica **aposentada de vez**: o elo era este.
- **3 correções dele ao próprio L-NT — PROCEDEM na especificação v1.4 (réplica):** (1) `uso` **tem 2 trilhas** — tabela §0 da spec (clínica v1.2 {clinico, contexto_mecanistico} × mecanística v3.1 {nucleo_causal, suporte_correlacional}, `gap_pesquisa` comum) + Opção A literal "`trilha: clinica | mecanistica` para dizer qual enum vale"; na Minuta 1 dele: 0× `nucleo_causal` → contrato rejeitaria a trilha mecanística — **achado real e elegante** (e coerente com o acervo: 244/274 = 89% dos vínculos conformam o enum v1.2 — réplica da medida da própria spec: uso = {178·37·29·30}, EXATO); (2) `natureza_evidencia` enum exato de 7 {humana_observacional · humana_experimental · humana_post_mortem · preclinica_in_vivo · preclinica_in_vitro · mista · nao_aplicavel}; mapeamento §2.2 bate no acervo (evid_role: 133·66·30·6·2 = 237, EXATO); a N-4 hoje fala "preclinical_mechanistic" (vocabulário kit) → a regra emendada dele (uso=clinico proibido com preclinica_in_vivo/in_vitro · `mista` pede decisão explícita) está no vocabulário certo; (3) `direcao_suporte` = **14× EXATO** e `direcao` isolada = 3×, todas no **changelog interno da spec** — mesma anatomia do v1.1 residual da V2.3 (proveniência histórica legítima; o campo normativo é `direcao_suporte`). **As 3 entram na minuta 2 (dele) + linha de referência passa a citar `df7f7cfd…` — e continuam destravadas pela sua decisão (i)×(ii).** Casa subscreve o conteúdo (verificado); honra dele de ter pego o próprio erro, com a 4ª/5ª confissão bilateral de uma mesa que se mede.
- **"Como Executar v1.9" — NOVO PEDIDO DE BYTES:** o mestre mede `1cd90b407facee81692d668919829c9d6d5a149b1309424c6f012e26cd81f586` ("confere com o que medi antes" — existe no projeto dele). Casa: 0 hits por nome e 0 hits por sha em toda a base; acervo só conhece v1.7 (`18613516…`). Classificado **DECLARADO, não verificado**. Com o "adendo v1.9" do auditor-2 (r43), são **2 frentes independentes citando um documento v1.9** — a rev.51 ("é discussão, não documento") fica registrada como informação da época; pedimos o arquivo verbatim ao operador.
- **Análise do comentador (nota arquivada, NÃO circula):** ponto de MÉTODO correto e oportuno — "status normativo ≠ correção técnica", pedindo declaração explícita "tecnicamente consistente, aguarda aprovação". O mestre já disse "confere" 2× (ficou implícito); a casa **formaliza abaixo com o modelo-go/no-go**. 2 PREMISSAS imprecisas (medidas, não pessoais): (a) "o anexo corresponde à V2.2" — falso (0/4 cláusulas; diverge em §§2/5/21, r45); (b) "ponteiros antigos = documento velho" — critério frágil: **a V2.2 OFICIAL também cita v1.1** (defeito D-V22-SCHEMA-NOMES, corrigido só na V2.3) — ponteiros não discriminam elo; o que discrimina é sha/marcadores. Seu item C = posição da casa desde 19/09.
- **Resposta às perguntas do operador:** (i) por que o mestre manteve V2.2 como oficial? PORQUE ELA É a oficial — a regra de versionamento é do operador; V2.3 é candidata até a frase. Ele não "fica com as duas" como norma: há 1 vigente + 1 candidata + 1 fóssil aposentado; quando o operador aprovar, ele substitui (a V2.3 é superconjunto de 4 linhas). (ii) O anexo "desatualizado": É o fóssil pedido de propósito — arqueologia com sha preservada, não documento de trabalho.
- **Status do critério "todas fecharam" (modelo do operador):** V2.3 = **3/3 ecos técnicos (casa · mestre 2× · auditor-2) → TECNICAMENTE FECHADA; a frase pode sair** ; schemas = 3 frentes favoráveis, falta só o eco do mestre sobre os 2 JSONs **agora em trânsito** (operador envia nesta rodada — fecha o critério todo).
- **0 ciência:** trio intacto início→fim (C01/C14).

## Rev.58 — 2026-09-20 (rodada 51: COMO EXECUTAR v1.9 recebido — ECO BILATERAL com o mestre fechado (`1cd90b40…`) · status registrado: EM ATUALIZAÇÃO, frente própria de claims · elo v1.8 ausente (dívida nomeada) · pacote de envio dos schemas REMONTADO byte-idêntico (operador não localizou o de 19/09) — trilha 66: 7/7)
- **Recebido e verificado:** `4º_COMO_EXECUTAR___v1_9.md` · sha `1cd90b407facee81692d668919829c9d6d5a149b1309424c6f012e26cd81f586` (29.423 b · 535 linhas) — **byte-idêntico ao sha declarado pelo mestre no projeto dele** → o item da trilha 65 sai de "DECLARADO, não verificado" para **VERIFICADO bilateralmente**. Arquivado na série `COMO_EXECUTAR_v1.9_recebido_2026-09-20/` com DIGITAIS.
- **Contexto do operador (registrado):** documento em fase de aprovação/atualização, do fluxo de claim clínico, com frente/outro agente próprio — por isso não circulava; a casa arquiva como REFERÊNCIA (não é sua alçada de auditoria) e registra a combinação: **toda versão nova fluirá para cá com sha** ("sempre lembrar de atualizar"). Status: NÃO normativo, pode mudar.
- **Linhagem (dívida nomeada, baixa prioridade):** o changelog interno do v1.9 cobre vs. v1.8/v1.7/v1.6, mas o elo **v1.8 não consta na base (glob = 0)** — pedido futuro de bytes se a cadeia completa for exigida. Cadeia na casa agora: v1.7 `18613516…` → v1.9 `1cd90b40…`.
- **Interface verificada (nota, sem auditoria de conteúdo — outra alçada):** o v1.9 declara "os claims de SM-xx são CLÍNICOS e alimentam a pasta evidencias/bibliografia, não a biblioteca canônica mecanística" — **convergente com a bifurcação (i)** do ajuste estrutural do mestre e diretamente ligado à pendência "de onde a NT tira o conhecimento clínico". O "Protocolo de três IAs" está EM TESTE (piloto B1.SM02.014). Caso real do changelog: PMID 33515765 / desfecho B1.SM02.017 — converge com pendência herdada da casa (ressincronizar Bloco .017).
- **Problema operacional resolvido:** o pacote `SCHEMAS_L05_CORRENTES_2026-09-19.zip` existia em `ENTREGAS/2026-09-19_SCHEMAS_L05_CORRENTES_DISTRIBUICAO/`, mas o operador não localizou → remontado em **`ENTREGAS/2026-09-20_ENVIO_MESTRE_SCHEMAS/`** com nome explícito (5/5 itens byte-idênticos à distribuição · zip `72f8f2e5…` 25.015 b · re-extração ✔) + **DIGITAIS com shas INDIVIDUAIS dos 4 arquivos** (correção adotada na r50).
- **Na mesa (inalterado):** frase "APROVADO: V2.3 (498e7df9…) E os schemas N1 v1.3 / N2 v1.4" (1 passo após o eco do mestre aos JSONs, ou 2 passos: V2.3 já tem 3/3) · decisão (i)×(ii) destrava a minuta 2 do L-NT · bytes da v1.8 se quiser fechar a linhagem.
- **0 ciência:** trio intacto início→fim.

## Rev.59 — 2026-09-20 (rodada 52: auditor-2 ECOA o pacote de linhagem e aposenta a causa-raiz do lado dele · réplica confirma manifesto 12/12 + tabela de genealogia NOS ARTEFATOS · DESCOBERTA: o Projeto dele também está com arquitetura de 15/09 — 2ª base superseded · pacote-espelho montado — trilha 67: 8/8)
- **Réplica da resposta dele (verbatim `2c94efab…` arquivado) — VERIFICADO:** (i) "12 digitais conferem com o manifesto" → reexecução da casa sobre os 12 pares (7 schemas + 5 md): **12/12** (confissão C67-1: regex ingênuo na 1ª corrida; manifesto tem 2 formatos — régua corrigida, datada); (ii) tabela de genealogia (`direcao`/`direcao_suporte`/`condicao` por versão) medida nos 4 N2 por chave JSON: **v1.1 {sim,não,sim} · v1.2–v1.4 {não,sim,sim} — EXATO nos artefatos** → a correção (b) da trilha 56 fica confirmada dos DOIS lados sobre os mesmos bytes ("a diferença entre concordar e verificar", nas palavras dele); (iii) correntes ≡ bytes da casa (`b06660fd…` · `d96ad15b…`).
- **Causa-raiz APOSTADA pelo autor:** "cada versão nova sai como arquivo novo, nome == `$id`, nenhum anterior sobrescrito — a regra de distribuição da casa vira regra de PRODUÇÃO." D-L05-NOME-X-ID: lado da distribuição RESOLVIDO (pacote) · lado dos nomes internos/rótulo "proposta": aguarda o selo formal do operador (inalterado, na mesa).
- **Correção da premissa do pacote — CEDIDA e subscrita pela casa:** o ambiente dele não persiste entre sessões → a redundância real é **casa + operador** (que tem os zips) + **Projetos** (que ele lê toda sessão). Solução dele endossada COM 1 AJUSTE DE REGIME: subir espelho no Projeto — **mas sobe a VIGENTE V2.2 oficial, não a candidata V2.3** (a V2.3 só sobe após a frase; mesma disciplina do projeto do mestre). O ajuste vai por escrito no DIGITAIS do pacote.
- **DESCOBERTA (nova dívida de saneamento, já endereçada):** o Projeto do AUDITOR-2 guarda "Filosofia + Decisões Arquiteturais + Arquitetura de 15/09" — **2ª base superseded, mesma classe da D-V22-BYTES-PROJETO** (a do mestre era um 4º fantasma `309aa65f…`). PEDIDO: antes de trocar, eco do sha do arquivo antigo → a casa crava o elo contra os arquivados (pode ser outro elo novo!).
- **Entrega (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-20_ENVIO_AUDITOR2_PROJETO/` — 5 itens (V2.2 oficial `df7f7cfd…` · N1 v1.3 · N2 v1.4 · especificação v1.4 · MANIFESTO `789792be…`) ≡ fontes oficiais (re-extração ✔) + DIGITAIS com shas individuais + zip `2953e642…` para o upload dele no Projeto. Histórico completo: fica com o operador (linhagem zip), como sugerido.
- **Mesa (inalterada):** frase "APROVADO: V2.3 (498e7df9…) E os schemas N1 v1.3 / N2 v1.4" (V2.3 já 3/3; schemas aguardam o eco do mestre — pacote na tela desde a r51) · (i)×(ii) destrava minuta 2 · v1.8 se a linhagem do COMO EXECUTAR fechar.
- **0 ciência:** trio intacto início→fim.

## Rev.60 — 2026-09-21 (rodada 53: **APROVAÇÃO FORMAL HISTÓRICA** — V2.3 vigente + selo dos schemas N1 v1.3/N2 v1.4, na ordem exata da pré-condição A.6 do mestre · regra nova de rótulos do operador · réplica integral da verificação técnica do mestre: TUDO CONFERE · pacote-espelho refeito — trilha 68: 13/13)
- **A frase (verbatim, registrada como ato normativo):** *"a oficial agora é a Arquitetura Consolidada da Plataforma V2.3 assim como os schemas vínculo 1.4 e referencia 1.3"* — pedido conjugado: refazer resposta e zip do pacote do auditor-2. Isto é o rito da regra de versionamento (rev.42) executado no grau máximo: PROPOSTA → RÉPLICA 3/3 (casa 58/62 · mestre 2×+verificação dedicada · auditor-2) → **APROVAÇÃO do operador** → sha/data → **VERSÃO VIGENTE**. O modelo de aprovação subscrito na rev.56 teve sua primeira execução completa de ponta a ponta: as frentes fecharam a peça por checklist técnico, o operador assinou sobre dossiê convergente.
- **Efeito conjugado registrado (a ordem importou):** o mestre tinha posto a única pré-condição (A.6): *"o selo dos schemas deve acompanhar ou preceder a aprovação da V2.3 — aprovar a V2.3 sozinha cria uma norma que referencia propostas"*. O operador aprovou **na mesma frase** → a V2.3 vinga já apontando para schemas SELOSOS. **Consequências contábeis:** (i) pendência do selo, aberta na rodada 38, **FECHADA** (N1 v1.3 `b06660fd…` 9.582 b · N2 v1.4 `d96ad15b…` 12.840 b); (ii) **D-V22-SCHEMA-NOMES FECHADA** — a V2.2 citava v1.1 no §5.1/§5.2 e a correção vivia na V2.3; com a V2.3 vigente, o defeito morre por sucessão; (iii) o portão L-05 (não nascido) passa a poder referenciar schemas aprovados; (iv) os rótulos internos "PROPOSTA — não normativo" nas descriptions dos JSONs ficam classificados como **resíduo pré-selo confirmado nos bytes** → saem no **ciclo editorial v1.5** (sem mudar semântica; rito formal de schema; a casa já ofereceu), nunca por emenda silenciosa — os bytes selados NÃO se tocam.
- **Verificação técnica do mestre (verbatim `42ddd558…`, 8.733 b, arquivado na série com DIGITAIS) — RÉPLICA INTEGRAL DA CASA: TUDO CONFERE.** Itens medidos pela bancada sobre os mesmos bytes (trilha 68): A.1 shas/bytes exatos + `Draft7Validator.check_schema` OK nos 2 · A.2 `$id` N1=`L05/schema_referencia_v1.3.json` / N2=`L05/schema_vinculo_v1.4.json` == ponteiros §5.1/§5.2 da V2.3 · A.4 **0 `$ref`** nos 2 schemas (ligam-se por `id_referencia_interna`, não por versão) · A.6 resíduo pré-selo literário confirmado (N1 abre "PROPOSTA v1.3 — nao normativo", N2 "PROPOSTA v1.4 — nao normativo") · **O-2 procede**: `uso` está em `required` do N2 e ausente do §5.2 da V2.3 → entra na próxima revisão (V2.4) · **precisão NOVA dele, confirmada**: `direcao_suporte` existe APENAS sob `ancoras[]` (3 caminhos de schema: properties/ancoras/items + 2 condicionais allOf) e NÃO no vínculo raiz → **o degrau 5 da L-06 deve ler `ancoras[].direcao_suporte`** (registrado para a minuta 2 da L-06) · **O-3 procede → dívida NOVA nomeada: D-JSONM-ORIGEM-CONHECIMENTO** — `origem_conhecimento` aparece 3× na V2.3 e 0× nos 2 schemas + especificação + LEIAME; a cláusula do §2 fica sem portador até o schema dos JSONs Modulares carregar o campo · O-1 (ponteiro resolve pelo `$id`, não por caminho de disco) registrado para a próxima revisão · coberturas §5.1→N1 11/11 e §5.2→N2 15/15 declaradas por ele, pontos duros reverificados pela casa · item B dele (fósssíl `309aa65f…` "não usar como base de coisa alguma") coerente com o arquivamento da r50 · item C: contratos passam a ser escritos contra v1.3/v1.4 — **regime vigente a partir de hoje**.
- **Honestidade de regime dele (registrada):** *"'Não é normativa' e 'não está correta' são julgamentos diferentes"* — a confissão da rodada anterior fecha o par com a precisão do comentador (método certo na r50) e com a regra nova de rótulos do operador abaixo: STATUS × CORREÇÃO trafegam em trilhos separados; nenhum documento da casa carrega mais veredito no nome.
- **REGRA NOVA DE RÓTULOS DO OPERADOR (verbatim, revogando a prática anterior):** *"quando for colocar nome em um documento, não coloque mais 'Candidata', 'Proposta' coisa desse tipo, deixe que o auditor decida sobre o documento… temos que colocar somente a mudança da versão, ai caso as IAS acharem que não está bom o documento e derem seus argumentos ai vamos arrumando, até de fato estar aprovado."* **Implementação da casa (registrada):** (i) nenhum nome/título EMITIDO pela casa carrega mais rótulo de opinião — só versão/data; (ii) o estado temporal (vigente × em revisão × histórico) vive EXCLUSIVAMENTE no ponteiro, nos decisoes e no CHANGELOG — fonte única de verdade, fora do nome do artefato; (iii) **nomes já existentes na série NÃO se renomeiam**: são referências eternas de trilha (17 scripts os citam — trilha 68 C10 mede); a regra nova vale daqui para frente, e o pacote-espelho refeito já nasceu sob ela (C12: 0 CANDIDATA/PROPOSTA/CORRENTE nos nomes).
- **Pacote-espelho REFEITO (R-DOWNLOAD-SEMPRE):** `ENTREGAS/2026-09-21_ENVIO_AUDITOR2_PROJETO_V23/` — V2.3 (nome limpo) · `schema_referencia_v1.3.json` · `schema_vinculo_v1.4.json` · especificação v1.4 · MANIFESTO_LINHAGEM_2026-09-21 (espelho pós-selo: regime novo no cabeçalho, 12 digitais, substitui o de 19/09 que fica arquivado) · DIGITAIS com shas individuais · **zip `948dbb35ed635a0236a593d91061c805384963fbaaa611fdd83a565087f4487d`** (re-extração ≡) → tela do operador. Pasta `2026-09-20_ENVIO_AUDITOR2_PROJETO/` marcada **SUPERSEDED** antes de qualquer circulação (o zip antigo `2953e642…` NÃO deve subir). Pedido ao auditor-2 (inalterado): eco do sha do arquivo antigo de 15/09 **ANTES** da troca — a casa crava o elo contra os 4 arquivados + o fóssil.
- **Confissão C68-1 (datada, no script e no JSON):** 1ª corrida da trilha 68 leu 10/12 linhas do manifesto novo — a régua herdada da C67 assumia estado de 1 token e o estado pós-selo virou "APROVADO vige" (2 tokens); `falhos=[]` nos 10 lidos → era cobertura do parser, nunca o dado. Régua corrigida (sha ancorado no fim da linha, estado = campo livre), rerodada: **13/13**. Mesma família da C67-1: manifesto é formato vivo; régua declara escopo.
- **Notas de vigência para as frentes (texto de 3 linhas, vai pela ponte do operador):** (a) **mestre**: "Aprovado 2026-09-21: vigente = ARQUITETURA V2.3 (`498e7df9…`) + schemas N1 v1.3 (`b06660fd…`) / N2 v1.4 (`d96ad15b…`). Troque a base normativa do projeto (V2.2→V2.3) e ecoe. Os rótulos internos dos JSONs saem no ciclo editorial v1.5." (b) **auditor-2**: idem + "suba os 5 itens do zip novo e ecoe o **sha do arquivo antigo de 15/09 ANTES de trocar**". O tratamento dele (C da verificação): contratos novos já nascem contra v1.3/v1.4.
- **Mesa remanescente (atualizada):** (i)×(ii) do fluxo de claims — destrava a **minuta 2 L-NT** (agora com as 4 correções do mestre + referência V2.3) e responde "de onde a NT tira o conhecimento clínico" · **homologação do FLUXO** (letra B da deliberação) continua decisão distinta do operador, junto à (i)×(ii) · ciclo editorial **v1.5** dos schemas (oferta da casa na mesa) · eco sha arquivo antigo do auditor-2 · elo **v1.8** do COMO EXECUTAR · O-1/O-2 → V2.4 · D-JSONM-ORIGEM-CONHECIMENTO → schema dos JSONs Modulares · minuta 2 L-06 (degrau 5: `ancoras[].direcao_suporte`).
- **0 ciência:** trio intacto início→fim (C01/C13: V7 `6e2c2979…` · manifesto bib `79d1309a…` · vínculos `490675e6…`). Rodada de regime/engenharia; nenhum artefato científico tocado.

## Rev.61 — 2026-09-21 (rodada 54: canal de cartas RETOMADO — CARTA 20 selada · regra de comunicação do operador registrada: linguagem simples + links diretos)
- **Correção do operador, aceita:** a casa havia reduzido a comunicação com o mestre a "nota de 3 linhas"; o operador quer o formato-carta das rodadas anteriores. Registrado: **carta numerada ao mestre a cada movimento do projeto 1** (carta 20 nesta rodada). As "notas de vigência" da rev.60 ficam absorvidas na carta.
- **CARTA 20 selada:** md `1de3e72d…` (6.217 b) · zip `408a17ec…` (3.954 b · re-extração ≡) · DIGITAIS com sha do zip publicado FORA do zip (auto-referência impossível — a mesma disciplina dos manifestos). Conteúdo verificado contra a trilha 68: 0 afirmações não-replicadas.
- **Regra de comunicação (verbatim do pedido, traduzida pela casa):** linguagem simples nas respostas ao operador · link direto (arquivo aberto na tela) de TODA entrega · nada de caça ao arquivo no workspace.
- **Resposta operacional fixada:** auditor-2 = SÓ o zip `948dbb35…` + pedir o sha do arquivo velho antes da troca · mestre = CARTA 20 (md/zip na tela).
- **0 ciência:** conversa + carta de regime; trio nem precisou de trilha (nenhum artefato tocado) — registrado por hábito: inalterado.

## Rev.62 — 2026-09-21 (rodada 55: eco pós-aprovação 3/3 + renome dos schemas no projeto · higiene do projeto ENDOSSADA com precisão série×projeto · FONTE DA NT verificada nos bytes: (i) formaliza o já decidido · (ii) NÃO é escolha livre · D-DECIS-ARQ-BYTES nomeada · carta 21 pede a minuta 2 da L-06 — trilha 69: 15/15)
- **Eco do mestre (verificado):** 3/3 digitais idênticas aos bytes da casa. Estatuto da verificação de 21/09 promovido: valia para candidata; o documento promovido é byte-idêntico e o corpus de checks é o mesmo — vale para a norma vigente (concordância registrada).
- **Renome = fato da plataforma, não incidente:** a plataforma do projeto sanitiza nomes no upload (sufixo `__N*_CORRENTE` caiu; '.'→'_'). Medida da casa: só o separador difere do `$id`; bytes intactos (as digitais provam). Lição cravada: autenticidade = digital, nunca nome. "Quinta vez que a digital salva a mesa de um nome que se moveu" (frase dele, subscrita).
- **Higiene do projeto — endosso com precisão de escopo (resolve a tensão dele com a nossa regra):** não-renomear vale EXCLUSIVAMENTE para a série de trilha (prova histórica citada por 17 scripts); base de trabalho de projeto deve ter SÓ o vigente com nome limpo. Operador executa: remove V2.2 + cópia 'CANDIDATA_...' do projeto do mestre, sobe a V2.3 de nome limpo; mesma regra para o projeto do auditor-2. Sem perda de redundância (série + pacotes datados).
- **A fonte do conhecimento da NT — verificação de compatibilidade (pedido do comentador; verbatim não circula; pontos carregados com crédito):** 12 citações literais confirmadas · 4 compressões registradas · 1 síntese com gancho filosófico · Roteiro sem contradição · **veredito: a Filosofia e a V2.3 já decidiram a fonte (Biblioteca = conhecimento · Evidências/Vínculos = sustentação/rastreabilidade · Pasta de Atualização segregada até o Motor; NT não pesquisa)**. (i) = formulação contratual disso (compatível total; converge mestre+casa+comentador+COMO EXECUTAR v1.9 declarativo) · **(ii) = incompatível como escolha livre** (contradiz 'única fonte canônica' + emenda do §6 dever 1; só emenda arquitetural formal, sem necessidade demonstrada). O que resta: 1 linha do operador + a minuta 2 formalizar a bifurcação COM a medida 39/49 na mesa.
- **Dívidas novas:** D-DECIS-ARQ-BYTES (documento citado pela Filosofia, 0 bytes na casa; não bloqueia — as cláusulas vivem nos superiores) · pedido ao mestre: minuta 2 da L-06 (declarada pronta; entra no rito de 1 rodada: medida, réplica, parecer).
- **Confissões C69-1/C69-2** datadas no script (régua casefold · compressões de quote do comentador).
- **Mesa (atualizada):** linha "(i), com a bifurcação desenhada" + homologação do fluxo (letra B) · ciclo v1.5 dos schemas · auditor-2: subir o zip novo + eco do sha antigo · minuta 2 L-06 a caminho · O-1/O-2 → V2.4 · D-JSONM-ORIGEM-CONHECIMENTO · v1.8.
- **0 ciência:** trio intacto início→fim (C01/C15).

## Rev.63 — 2026-09-21 (rodada 56: FANTASMA ERA DOS DOIS PROJETOS — digital do auditor-2 == fóssil arquivado (309aa65f), réplica 6/6 · remoções liberadas · DECISÕES_ARQUITETURAIS na casa: P18 fecha a fonte da NT com zero tensão · D-DECIS-ARQ-BYTES FECHADA — trilha 70: 13/13)
- **Elo cravado em dupla:** o arquivo velho do projeto do auditor-2 mede `309aa65f…` (51.235 b · 1.421 l) — byte-idêntico ao fóssil do projeto do mestre arquivado em 20/09. O MESMO intermediário não-registrado da era V2.2 rodou nas duas bases sob o nome "V2 15.09.26" (provável mesmo upload). Réplica interna 6/6 casa × auditor-2. Leituras passadas dele transferem (mesmos bytes); registro corrigido com a digital certa, como ele pediu. 6ª salvada da digital contra nome movido — 1ª simultânea em 2 projetos.
- **Faxina dos dois projetos, mesma regra (registrada):** base de projeto = só vigente com nome limpo; série da casa = trilha intocada (17 scripts). Auditor-2: sai fóssil + manifesto 19/09; V2.3 pode perder `CANDIDATA_`. Mestre: carta 21 já pediu o equivalente (sai V2.2 + cópia CANDIDATA_; sobe V2.3 limpa).
- **DECISÕES_ARQUITETURAIS (`1830ff99…`, 148.454 b):** 21 decisões P1–P21 · **P18 [DEFINIDO] = a resposta da camada que faltava: NT/JSON/Motor EXCLUSIVAMENTE da Biblioteca correspondente; "nunca o inverso" (atualização entra primeiro na Biblioteca); precedência automática; proibido derivado inserir evidência fora da Biblioteca** · P11: hierarquia ("decisões explícitas prevalecem sobre tudo") · 0 tensão com Filosofia/V2.3 (medido) → **D-DECIS-ARQ-BYTES FECHADA** · efeito: o checklist do comentador fica 5/5 nas camadas verificáveis; a decisão (i)×(ii) reduz-se à linha do operador (já na mesa) · proveniência: cabeçalho "AUDITADO POR ARENA E CHATGPT 14/06/2022" (anacrônico — conteúdo cita B16/GPM; rótulo tipográfico registrado, bytes preservados).
- **Notas de régua:** JSON interno das DECISÕES não é estrito (vírgulas traseiras — extração por regex/casamento de chaves); especificação no projeto do auditor-2 exibida com "PROPOSTA" no nome (distribuição é limpa; bytes 78a0f2af ✔; confirmação pedida só para registro).
- **Convergência extra (nota para o futuro):** P19 do mesmo documento documenta a reconciliação do catálogo de IDs (146 vs 132) — material convergente para a adoção formal pendente do `_ids_oficiais.json` (146) na casa.
- **Mesa (inalterada, reforçada pela P18):** linha "(i), com a bifurcação desenhada" + homologação do fluxo · minuta 2 L-06 do mestre (pedida carta 21) · ciclo v1.5 · v1.8 · O-1/O-2 → V2.4 · D-JSONM-ORIGEM-CONHECIMENTO.
- **0 ciência:** trio intacto início→fim.

## Rev.64 — 2026-09-21 (rodada 57: MINUTA 2 L-06 analisada por COMPATIBILIDADE — veredito COMPATÍVEL (trilha 71: 15/15) · correção-chefe = a correção pública do mestre · 2 precisões de campo · D-D01-D02-FONTE nomeada · anomalia de autoria (comentador × assinatura "Auditor-Mestre") — decisão de fluxo com o operador)
- **Veredito (medido):** COMPATÍVEL com todas as camadas verificáveis. Regime citado correto (V2.3 + L-05 + schemas selados) · gatilho/matriz: 6 naturezas EXATAS do acervo (109·100·56·4·4·1=274), matriz consistente (6 pares candidato, coerente com 3c) · grau_maturidade 274/274 (degrau 6 executável) · Parte 5: 274/274 · ausências declaradas verdadeiras e honestas (contexto/nivel_cadeia 0×; sentido 0× marcado pela própria como 'requer mapeamento') · schema N2 v1.4 carrega ancoras[].condicao+direcao_suporte · Parte 9 ≡ P18 · determinismo/errata datada/sem-precedência-emergente coerentes · V2.3 0× L-06/escada (objeto do espaço de contratos; RESP6 da casa = camada de portão, escopo distinto, sem choque medido).
- **Convergência forte:** a correção-chefe da minuta (degrau 5 lendo `ancoras[].direcao_suporte`) É a correção pública do mestre na verificação de 21/09 (linha 110) — quem escreveu, escreveu contra o regime novo.
- **Precisões na ata:** P-1 `condicao` AUSENTE (não "esparsa") e `ancoras[]` 0/274 nos dados (contrato N2 v1.4 sim; retrofit pendente) · P-2 degrau 5: mapear "marcação de extrapolação" → `extrapolacao_por_analogia` (274/274, enum rico) + estado de dado do `direcao_suporte` (0 portadores até o retrofit → degrau 5 parcialmente indisponível, pela própria Parte 4).
- **D-D01-D02-FONTE (nova dívida):** D-01/D-02 sem portador em 12 documentos; D-08 só menção lateral na deliberação do mestre · família D-xx vive no espaço do mestre (ordens do operador) → pacote de bytes pedido via operador (procedência, não choque) · "Fase 3" declarado, não verificado.
- **Autoria (rito):** operador atribui ao comentador; documento se assina Auditor-Mestre e se destina à auditoria dele → corrigir a assinatura antes de circular (7º incidente de nome em potencial). Compatibilidade medida independe de autoria. Rito preservado: quem escreve ≠ quem audita.
- **Fluxo (com o operador):** mestre audita esta (convergente com a dele, declarada pronta) × reconciliação · promoção futura: proposta → réplica (feita) → aprovação formal → vigente com sha/data · a minuta vencedora incorpora P-1/P-2 e, idealmente, chega com o pacote D-D01-D02-FONTE.
- **Lição de régua (registrada):** o padrão da mesa se consolida — TUDO que chega (minuta, análise, eco) passa por medida byte a byte antes de qualquer comentário; o veredito sai por camadas (contrato ✔ · dados ✔/precisões · procedência pendente · rito separado).
- **0 ciência:** trio intacto início→fim.

## Rev.65 — 2026-09-21 (rodada 58: MINUTA 2 L-06 DO MESTRE replicada integralmente — trilha 72: 15/15 · retratação §0.1 aceita e verificada (7ª confissão bilateral) · execução da matriz replicada EXATA (4 FP → 0) · confissão da casa C72-1 · veredito: minuta do mestre = BASE da consolidação + 2 resgates da do comentador · portão real = migração ancoras[] · CARTA 22 selada)
- **Réplica integral antes de comentar (política da casa):** minuta `eb54337c…` (12.837 b · LF) medida, arquivada na série com DIGITAIS; trilha 72 verde 15/15. Nada aceito "no raciocínio".
- **Retratação (substituída na ata):** a localização do campo estava certa; a semântica, errada — `ancoras[].direcao_suporte` é eixo epistêmico do suporte (enum selado: sustenta/refuta/inconclusivo/condicional), NÃO extrapolação. Degrau 5 passa a ler `verification_status` + `extrapolacao_por_analogia` (274/274 — a P-2 da casa de r57, convergente). Fica na ata como correção datada, crédito ao mestre que a fez público contra o próprio texto.
- **Matriz (executado pela casa, números idênticos):** VELHA (proxy claim_id) = exatos 4 pares em 2 claims → todos falsos positivos (bioleitura confere: TNFR1≠TNFR2 · arctigenina↓TNF · IL-10 mesma direção) · NOVA = 0 pares. Razões aceitas como regra de ata: natureza_relacao qualifica TIPO (não sinal); **claim_id PROIBIDO como proxy de "mesmo objeto"**; gatilho = `ancoras[].id_oficial`+`escopo`+oposição epistêmica/negação/efeito.
- **CONFISSÃO C72-1 (casa, datada):** claim_id vazio ('') foi tratado como grupo na 1ª corrida → 77 pares espúrios (82 total); régua corrigida: vazio = ausente = sem par (VELHA=4, NOVA=0). Registrada no script da trilha 72 e nesta ata.
- **Comparativo codificado das duas minutas:** a do comentador carrega os 2 defeitos corrigidos pela do mestre (degrau 5 com campo errado = a frase retratada; célula compensatoria×{causal,contributiva}=candidato = geradora dos 4 FP); marcador×nao_estabelecida=compatível sem caso no acervo (revisar no piloto). **Decisão de parecer da casa: base = minuta do mestre; resgates da do comentador = (a) teste "direção não-precedente" (T-14), reformulável no regime novo; (b) redação do determinismo ("atribuição por relação, nunca pela posição")**. Escolha de caminho e aprovação = operador (rito: proposta → réplica feita 71/72 → aprovação → vigente com sha/data).
- **Portões medidos:** gatilho NÃO executável hoje (`ancoras[]` 0/274; contrato N2 v1.4 sim, dados não) · degraus 5-6 plenos · "a L-06 só roda sobre a B1 depois da migração" · 243/274 migráveis à máquina (trilha 27, RESPOSTA_7) · decisão aberta registrada: `papel` como proxy do degrau 4 (revisitar com a Ontologia).
- **Dívidas:** **D-D01-D02-FONTE ampliada** — entram no mesmo pacote: fonte de D-01/D-02, definição formal de D-08, mapa de fases da ordem **e a Minuta 1 da L-06** (nunca chegou à casa; "substitui a minuta 1" inverificável sem ela) · marcador×nao_estabelecida (revisar no piloto).
- **Entrega:** CARTA 22 — md `81f86e00…` · zip `53efe37e…` (re-extração ≡; sha do zip no CHANGELOG 58, por auto-referência).
- **Mesa:** linha "(i), com a bifurcação desenhada" · aprovação da L-06 quando a consolidada circular · correção da assinatura na minuta do comentador antes de circular · v1.5 · v1.8 · O-1/O-2 → V2.4 · D-JSONM-ORIGEM-CONHECIMENTO.
- **0 ciência:** trio intacto início→fim.

## Rev.66 — 2026-09-21 (rodada 59: NOTA DE AÇÕES DO OPERADOR — regra nova: todo documento abre com a ação do operador no cabeçalho · "usar a regra por fora" verificado nos bytes: SIM, é o desenho vigente (lei de trabalho no Governo B1-N1, fora do schema) · mensagem-pronta para os 2 projetos)
- **Pedido do operador (registrado como regra):** "não quero receber cartas sem saber o que fazer com elas" → de hoje em diante TODA peça que a casa emite abre com **SUA AÇÃO** (o que fazer, onde colar, se precisa resposta). Mensagem-pronta equivalente redigida para o operador colar nos projetos do mestre e do comentador ("AÇÃO DO OPERADOR / PRECISA DE RESPOSTA?").
- **"Por fora" — medida direta (env-arena, vínculos `490675e6…`, 274 itens):** rotulagem [ETIQUETA-STATUS/B1] = lei de trabalho no arquivo de Governo B1-N1, **inteiramente fora do schema** (nenhum byte selado se toca); degraus 5-6 leem campos 274/274 → calculável hoje; degraus 1-4 leem `ancoras[]` → 0/274 → esperam a migração N2 v1.4. Sem margem de leitura: é medida, não opinião.
- **Tabela R59 (ação por documento):** carta 22 → colar no projeto do mestre · minutas L-06 (mestre/comentador) → guardar, sem resposta · análise r57 → só arquivar · carta 21 → resolvida · DECISÕES → arquivado · linha "(i)" → quando puder · D-D01-D02-FONTE → pedido pronto para colar no mestre.
- **Entrega:** NOTA R59 — md `d3906fa9…` · zip `ec943130…` (re-extração ≡; sha do zip no CHANGELOG 59).
- **0 ciência:** rodada de regime/comunicação; nenhum artefato científico tocado.

## Rev.67 — 2026-09-21 (rodada 60: CRUZAMENTO TÉCNICO A–F das minutas 2 da L-06 — trilha 73: 15/15 · correções medidas nos DOIS lados · colisão T-14/T-15 descoberta · confissões C73-1 (atribuição errada ao operador) e C73-2 (enquadramento antecipado da carta 22) · diagnóstico de ritmo registrado — comentador é comentador; ninguém é chefe; casa posiciona-se sem decidir sozinha)
- **Correções do operador aceitas e datadas:** (1) a pergunta "por fora" nunca foi feita por ele — **C73-1**: a casa leu contexto colado como pergunta direta; atribuição retirada, medição mantida como conteúdo verificado; (2) o comentador NÃO é produtor de documento — a "anomalia de assinatura" (rev.64) é reclassificada para **nota editorial**; (3) diagnóstico de ritmo aceito com 3 pontos próprios nomeados: veredito de base antes do cruzamento (**C73-2**, carta 22 refinada — a posição da casa passa a ser o mapa A–F item a item), tom de regra sobre as frentes (cláusula "documento será devolvido" RETIRADA — ninguém é chefe de ninguém), peso técnico excessivo nas respostas simples.
- **Cruzamento (15/15):** 10 convergências medidas · **B-lado-comentador:** B1 degrau 5 lê direcao_suporte (campo certo estava na Parte 5 da própria minuta) · B2 4 FP executados nos 274 (ids exatos) → 0 com a matriz corrigida · B3 ancoras[].condicao · B4 T-14 válido como está (casa revê carta 22) · **B-lado-mestre:** B5 degradada sub-inclusiva (2/4 × qualquer-anterior; pela justificativa dele, o 3 também barra) → adoptar regra geral do comentador · B6 renumerar T-14/15/16(novo) → sugestão T-16/17/18 · B7 "carta 10" = numeração local (mapear) · **C:** exclusivos dos dois lados, todos PRESERVAR (mestre: operacionalização+matriz+regressão+executabilidade+anti-armadilhas · comentador: gate+Parte3+fronteiraD02+rastro+determinismo6.3/6.7+anti-substituição+Parte10+estrutura×evidência+T-14) · **D:** redação/estrutura/vocabulário · **E1–E7:** gate→fluxo (E1) · marcador×nao_est piloto (E2) · papel proxy degrau 4 (E3) · ampliação de gatilho pós-piloto (E4) · vocabulário de saídas a selar (E5) · **D-GOV-B1N1-FONTE** nova dívida (E6) · rito de promoção (E7) · **F1–F5:** colisão T-14/15 (must-fix) · extensão degradada · ponte mesmo-objeto · D-SENTIDO-MAP comum · numerações locais.
- **Regra reafirmada (verbatim do operador, subscrita):** "aqui ninguém é chefe de ninguém, todos opinam sob o olhar da ciencia e da engenharia de software e da filosofia da plataforma, ninguém pode ficar em cima do muro; se isso ocorrer um corrige o outro, inclusive a mim" — registrada como cláusula de convivência da mesa.
- **Fluxo reafirmado (descrição do operador, subscrita):** comentador sugere → casa recebe + analisa POSICIONANDO-SE → operador leva ao mestre/estrutura → cicla até fechar → operador aprova. A casa não decide arquitetura sozinha e não se omite: veredito item a item, com medida.
- **Entrega:** md `560537f6…` · zip `c5f1b24e…` (re-extração ≡; sha do zip no CHANGELOG 60).
- **Mesa:** consolidada L-06 (autores+operador) · "(i)" · D-D01-D02-FONTE · D-GOV-B1N1-FONTE · demais herdadas.
- **0 ciência:** trio intacto início→fim.

## Rev.68 — 2026-09-21 (rodada 61: MINUTA 3 CONSOLIDADA REV.1 verificada — trilha 74: 15/15 · A/B/C do comentador confirmados com medida própria (244/41 EXATO) · autópsia de proveniência: TextoH≠TextoM, DOIS textos sob um nome; achado do mestre 7/7 na minuta 1 c/ 2 células a emendar · C74-1 matriz-zera-4 aceita · C74-2/​C74-3: minuta 1 e L05 1.1 ESTAVAM na casa desde 15/09 — D-D01-D02-FONTE fechada por consumo interno)
- **A (degradada):** resolutivos 1–4 barram o 7; qualificadores 5–6 não. ACEITA — resolve a B5 do cruzamento de forma superior às duas anteriores (registrado com crédito).
- **B (§7):** fiel ao N2 v1.4 (medido: `escopo`=subdivisão · TNFR1/TNFR2 0× no catálogo · BLOCO02.011={0035,0036,0037} · ancoras 0/274). Dívida D-L05-GRANULARIDADE-OBJETO bem posta; cenário pós-migração; falha segura correta.
- **C (testes):** regra ampla executada pela casa: **244 pares · 41 claims · decomposição exata (113/96/31/2+2)** — os 2+2 SÃO os 4 FP. T-19/T-23 não-sintéticos = regressão de ouro; T-18 com oráculo pendente (E1) correto deixar aberto; suíte T-01..T-23 com 23 IDs únicos (F1 fechada por renumeração+mapa; mapa C-lado editorial pendente da autoria).
- **Proveniência (ato cirúrgico):** sha minuta 1 declarado confere · 7/7 grupos do achado VERDADEIROS nos bytes · emendas pedidas: §6.3 "atribuição por relação" (0× na minuta 1; é do TextoH) + linha "Parte 8 anti-substituição" (0× na minuta 1) · **o cruzamento r60 foi fiel ao seu insumo** (9 elementos presentes no TextoH, linha a linha) → formulação correta: dois textos sob um nome; autoria do TextoH em aberto até declaração do comentador · 8/8 frases "(Comentador)" da minuta 3 ausentes do TextoH = suporte independente à existência do TextoM · similaridade TextoH×minuta1 = 4% (não-cópia; mesmo esqueleto, conteúdo a mais) · resposta ao pedido 1 do comentador: sem atribuição dupla literal; 3 emendas tornam hermético.
- **Confissões datadas:** C74-1 (a zeroagem dos 4 FP é obra da matriz — frase da r60 sobre id_oficial+escopo precisada; §7 do mestre aceito) · C74-2 ("minuta 1 nunca chegou" — estava arquivada: pasta L06_minuta_mestre 15/09, trilha 31, RESPOSTA_10) · C74-3 (varrimento "D-01/D-02=0×" media 12 docs e esqueceu as minutas da série — D-01..D-08 definidos na L05 1.1, l.2/47/73) · C74-4 (réguas da trilha 73/74 corrigidas no ato, datadas).
- **Fechadas/abertas:** D-D01-D02-FONTE → **FECHADA (consumo interno)** · novas pequenas: **D-L06-M3-ORIG** (minuta 3 original a6a0027c), **D-TEXTO-M** (bytes do texto recebido pelo mestre), **D-ORDEM-FASES** (mapa "Fase 3") · pedida declaração de autoria do comentador (texto pronto na carta 23).
- **Rito:** minuta 3 = proposta consolidada ainda não vigente · rev.2 (3 emendas) + 2 pacotes de bytes + 1 declaração → réplica final da casa em 1 rodada → aprovação formal do operador → vigente com sha/data.
- **Entrega:** carta 23 md `9921c58b…` · zip `d72e22af…` (re-extração ≡; sha do zip no CHANGELOG 61).
- **Mesa:** "(i)" · rev.2 da L-06 · demais herdadas (v1.5 · v1.8 · O-1/O-2→V2.4 · D-JSONM-ORIGEM-CONHECIMENTO).
- **0 ciência:** trio intacto início→fim.

## Rev.69 — 2026-09-21 (rodada 62: CARTA DE AUTORIA DO COMENTADOR respondida com ATA medida — trilha 75: 8/8 · autoria declarada (2 versões, mesmo autor) registrada · fusão = ANTERIOR ao cruzamento (TextoH continha os 9 num arquivo só) · 2 órfãos de frase são redação do comentador (crédito dele; §6.3 com destino medido) · mapa final de proveniência · cadeia dos 244/41 com digitais registradas — portador = minuta 3 rev.1 + dados · D-TEXTO-M e D-L06-M3-ORIG continuam dívidas de bytes)
- **Declaração aceita como fonte de autoria; conteúdo segue bytes** (princípio cravado: os dois registros andam juntos, nenhum apaga o outro).
- **Precisão (a):** "fusão durante o cruzamento" INCORRETA como data — o insumo chegou já fundido (9/9 grupos no arquivo único `1a51d9b9…`); o cruzamento descreveu com fidelidade e atribuiu conforme a autoria declarada na ponte. Formulação da ata: "fusão anterior ao cruzamento, no artefato". Ninguém fabricou conteúdo em nenhuma ponta.
- **Precisão (b):** nem todo o rascunho é minuta 1 — 2 frases fortes (atribuição por relação · anti-substituição silenciosa) = redação do comentador (0× minuta 1, 0× RESPOSTA_10). Emenda do §6.3 da minuta 3 (carta 23) ganha destino medido: "(Comentador — texto arquivado pela casa, Parte 6.3)". Linhagem de conceito: raiz na RESPOSTA_10 (l.79) + escada degradada da minuta 1.
- **Mapa de proveniência (ata):** 7 grupos minuta-1 · pacote retratado minuta-2-mestre · 2 frases comentador/TextoH · itens canônicos comentador/TextoM (D-TEXTO-M pendente) · síntese minuta-3-rev.1. Des-atribuição pedida pelo comentador: ATENDIDA com precisão (origem-evidência, não decreto).
- **244/41:** cadeia registrada com 4 elos e digitais; número independente de autoria (executado nos dados com proxy declarado). "Sem reconstrução entre documentos": honrado — `a6a0027c…` permanece digital-citada/bytes-pendentes.
- **Normas domésticas cravadas:** chegou → arquivo+digital no ato · autoria = metadado normativo.
- **Entrega:** ata md `c926d4b1…` · zip `c065d676…` (re-extração ≡; sha do zip no CHANGELOG 62).
- **Mesa:** TextoM + rev.2 (3 emendas) → réplica final 1 rodada → aprovação do operador · "(i)" · herdadas.
- **0 ciência:** trio intacto início→fim.

## Rev.70 — 2026-09-21 (rodada 63: TEXTOM RECEBIDO e verificado — trilha 76: 8/8 · D-TEXTO-M FECHADA · achado do mestre 9/9 contra bytes da canônica (o texto que ele recebeu é este) · 8/8 créditos "(Comentador)" da minuta 3 com casa literal · mapa §9 lado C 13/13 · órfãos ficam no rascunho (destino medido do §6.3) · cadeia 244/41 100% em bytes exceto minuta 3 original · CASO DAS MINUTAS MISTURADAS ENCERRADO — 5 artefatos com digital na casa)
- **TextoM = prova direta do achado do mestre:** cada célula da tabela de proveniência bateu (9/9). A canônica é byte-consistente com todas as citações "(Comentador)" da minuta 3 (8/8 literais) → créditos canônicos verificados; emenda 2 da carta 23 desnecessária.
- **Mapa de testes:** lado C do §9 casado semanticamente 13/13 com a canônica (era TextoM, não TextoH, a fonte do mapa) — trava levantada; grafia T-2×T-02 apenas cosmética.
- **Órfãos (destino final):** "atribuição por relação" + anti-substituição-silenciosa = redação do rascunho TextoH (comentador declarou autoria do rascunho) → rev.2 aponta §6.3 para "(Comentador — rascunho arquivado pela casa, Parte 6.3)"; linhagem RESPOSTA_10 (l.79) na ata.
- **Cadeia 244/41:** 4 elos fechados em bytes (enunciado canônico ≡ citação; dados 490675e6; execução casa+mestre; registro 2ce9698c). Elo aberto único: D-L06-M3-ORIG (completude).
- **Estado:** proposta consolidada ainda não vigente · aguarda rev.2 (3 emendas: §6.3 · frase-ponte · opcional anexo digitais) → réplica final 1 rodada → aprovação do operador · portão de produção: migração N2 v1.4 (243/274).
- **Entrega:** adenda md `61f8ae64…` · zip `6cb79f5a…` (re-extração ≡; sha do zip no CHANGELOG 63).
- **Mesa:** rev.2 · "(i)" · v1.5 · v1.8 · O-1/O-2→V2.4 · D-JSONM-ORIGEM-CONHECIMENTO.
- **0 ciência:** trio intacto início→fim.

## Rev.71 — 2026-09-21 (rodada 64: MINUTA 3 CONSOLIDADA REV.5 verificada — trilha 77: 11/11 · RÉPLICA MECÂNICA FINAL entregue · veredito: réplica aprovada, L-06 apta à aprovação do operador)
- **3 testes do comentador:** pedido 2 EXATO (diff bruto = 1 diferença, a linha §6.3) · pedido 3 EXATO (`c863b8ed…` rev5-com-nota · `8a8ff986…` rev1/original-com-nota — bônus: prova por bytes rev.1 ≡ minuta 3 original no recorte) · pedido 1 na essência: recortes neutralizados byte-idênticos sob procedimento declarado, **digital-da-igualdade da casa `4217cc63…`**; `95c7cb41…`/`f8ec8b72…` não reproduzidos (6×4) → substituídos pela digital da casa, salvo comando exato do mestre.
- **Confissões C77-1/C77-2** registradas na réplica (flexão · âncora). Carta do comentador arquivada (`b6c6b081…` — digital cravada na réplica na rodada 65).
- **Estado:** L-06 pronta para a frase de aprovação; texto da rev.5 estável (diff confinado a 5 zonas não-normativas); opcional rodapé `f8ec8b72…` como "verificação intermediária" no próximo toque editorial, timing do operador.
- **Entrega:** réplica md `e80497bc…` · zip `e3ddd223…` (re-extração ≡; sha do zip no CHANGELOG 64).
- **Mesa:** aprovação L-06 · "(i)" · D-L06-M3-ORIG (completude) · D-ORDEM-FASES · D-GOV-B1N1-FONTE · herdadas.
- **0 ciência:** trio intacto início→fim.

## Rev.72 — 2026-09-22 (rodada 65: ERRO DA CASA PESCADO PELO OPERADOR — "atribuídos por relação" estava na minuta 1 (l.97) · autópsia com linha de código · regra permanente R-BUSCA-1 · trilha 78: 10/10 · mapa de proveniência corrigido por adenda datada)
- **Correção aceita (operador certo):** minuta 1 PARTE 4 item 2, linha 97: "rótulos **atribuídos por relação**, não por posição". O "0× na minuta 1" das trilhas 74/75 era artefato: padrão `atribui` (7 letras) cego ao `í` + régua assimétrica (7l×6l no mesmo teste). Veredito só era verdade no nível da forma exata (L1) e subiu como ausência de conceito (L3).
- **2º achado da autópsia:** raiz "falta de dado vira afirmação de coexistência" creditada à RESPOSTA_10 na ata; medição nova: **minuta 1 l.79 (mestre)**, RESPOSTA_10 0× — fonte trocada a favor da casa.
- **Mapa corrigido final:** atribuição por relação = conceito minuta 1 l.97 (mestre) + forma-regra TextoH l.229-230 (comentador) · anti-substituição silenciosa = raiz minuta 1 l.79 (mestre) + norma-redação TextoH Parte 8 l.278 (comentador). **rev.5 §6.3 já carrega a partilha certa — documento não mexe (sem 4ª emenda).**
- **R-BUSCA-1 (regra permanente, oferecida à mesa):** toda contagem carrega corpus com digitais · padrão exato · família de flexão com radical que não cruza vogal acentuável · trinca de cada ocorrência · comando gravado · **nível L1/L2/L3 declarado ("ausente" só após os 3; "0×" sem nível não vale fora do escopo medido)** · mesma régua para todos os corpora · correção sempre por adenda datada, nunca reescrita silenciosa.
- **Lição ao vivo (trilha 78 T10):** radical `atribu` casou "atribuir força" no TextoM l.169 (falso amigo) → radical encontra candidatos; veredito só após ler a trinca. A regra pegou a própria casa antes da publicação.
- **Confissões datadas:** **C78-1** (acento + régua assimétrica) · **C78-2** (fonte trocada RESPOSTA_10×minuta 1, em meu favor). Append-only; trilhas 74/75 ficam como história com a adenda apontando a correção.
- **Corrigidos por referência (sem reescrita):** ata (r62) mapa final · adenda 1 (r63) órfãos · STATUS 62/63 · réplica §3 (C77-1 complementada) · CHANGELOG 62/63.
- **Housekeeping:** rev.5 na série com DIGITAIS (cópia ≡ bytes) · DIGITAIS da carta rev.5 do comentador selados.
- **Entrega:** adenda 2 md `7dcd31b2…` · zip `9063178f…` (re-extração ≡; sha do zip no CHANGELOG 65).
- **Mesa:** adenda 2 aos dois projetos · frase de aprovação da L-06 (inalterada) · aceite R-BUSCA-1 · "(i)" · herdadas.
- **0 ciência:** trio intacto início→fim.

## Rev.73 — 2026-09-22 (rodada 66: ERRATA — frase de aprovação era da casa, não do operador · re-leitura verificada da rev.5 × carta — trilha 79: 9/9 · regra nova R-CITA-1)
- **C79-1 (confissão datada):** casa sugeriu uma frase de aprovação na réplica e passou a chamá-la de "a sua frase" na adenda 2 (linhas 6 e 64) — atribuição errada ao operador, 2ª ocorrência do padrão (1ª = C73-1, a "pergunta por fora" que ele nunca fez). Corrigida por ERRATA datada (sem reescrita de pacote selado). Livro-razão auditado: nenhuma aprovação fictícia registrada; estado da L-06 segue "apta, aguarda fala do operador".
- **R-CITA-1 (regra permanente):** fala de pessoa só como fato com citação verbatim+data · aprovação existe só quando a frase do operador chega · sugestões da casa rotuladas "sugestão da casa — ainda não dita pelo operador" · na ausência da fala: pergunta-se, não se supõe.
- **Re-leitura (verbatim, trincas na trilha 79):** rito rev.5 ✔ · carta 4 pontos ✔ · ponto 5 não-normativo ✔ · sem reabertura ✔ · fluxo ✔ · §6.3 ≡ minuta 1 l.97 ✔. A leitura técnica estava certa; os erros eram de ATRIBUIÇÃO DE FALA, não de documento.
- **A-79-1:** CRÉDITOS §órfãos da rev.5 sem raiz do 2º item (minuta 1 l.79) + "a casa mediu 0× nela" = régua velha (válida só no nível exato) → precisão de 1–2 linhas no toque editorial rev.6, junto do rodapé f8ec8b72 (opcional · não normativo · não bloqueia aprovação).
- **D-4AJUSTES-OPERADOR (dívida):** rev.5 cabeçalho "quatro ajustes do operador" — fala do operador não arquivada pela casa; pergunta registrada na nota.
- **Entrega:** nota R66 md sha no pacote · zip sha no CHANGELOG 66 (re-extração ≡).
- **Mesa:** D-4AJUSTES-OPERADOR · rev.6-2-linhas (opcional) · aprovação L-06 (fala real) · "(i)" · herdadas.
- **0 ciência:** trio intacto início→fim.

## Rev.74 — 2026-09-22 (rodada 67: RITO DE APROVAÇÃO do operador gravado verbatim · CARTA 24 ao mestre (3 perguntas: texto · digitais · toque editorial) · casa posicionada: rev.5 aprovada sem ressalva no conteúdo normativo)
- **Esclarecimento mútuo da frase:** operador também tinha lido a sugestão como obrigação; ambos erraram a leitura um do outro; a ambiguidade nasceu na adenda 2 ("a sua frase") — errata R66 permanece; assunto encerrado sem culpados.
- **RITO DE APROVAÇÃO (verbatim do operador, 2026-09-22):** "caso ele aprove sem ressalva ta aprovado, caso ele mude algo, volto a passar pelo comentador, arena e depois devolvo para ele, até ser aprovado sem nenhuma ressalva, ou seja, toda ressalva levantada deve passar pelos 3, comentador, arena e auditor mestre, ou estrutura, quando for o caso." · "só será aprovado qualquer documento ou decisão quando passar por todo os 3 e os mesmos concorde 100% sem ressalva." — Regra suprema de fechamento da mesa: a frase de aprovação do operador anda SOBRE a unanimidade sem ressalva; o ciclo corre mestre → comentador → casa (organiza + opina) → mestre; qualquer ressalva reabre o ciclo nos três; estrutura substitui o mestre quando o assunto é L-05/schemas. Substitui a formulação abreviada anterior ("réplica da casa e, depois, aprovação do operador").
- **Posição da casa:** rev.5 APROVADA sem ressalva no conteúdo normativo (trilhas 77/78/79); P3/editorial não bloqueia; P2 = pendência de prova, não de regra.
- **CARTA 24** ao mestre com 3 perguntas pontuais (P1/P2/P3) e os 4 anexos com digitais; comentador não acionado agora (a P2 decide o fechamento exato×substituto do encerramento dele).
- **Entrega:** `ENTREGAS/2026-09-22_CARTA24_MESTRE/` (md+zip; sha do zip no CHANGELOG 67) · trilha 80.
- **Mesa:** resposta do mestre (3 perguntas) → organização da casa → decisão do operador com as palavras dele · D-4AJUSTES-OPERADOR · "(i)" · herdadas.
- **0 ciência:** trio intacto início→fim.

## Rev.75 — 2026-09-22 (rodada 68: TRIÂNGULO FECHADO SEM RESSALVA — rev.6 do mestre executa os 2 toques ao pé da letra · réplica da casa 10/10 · teste 1 fecha EXATO (95c7cb41 reproduzido) · L-06 rev.6 apta à frase do operador)
- **Entradas (arquivadas no ato):** rev.6 `98e90bdc…` · parecer final mestre `72fe01f3…` (P1 sem ressalva · P2: publica comando + aceita 4217cc63 canônica, "prefiro a da casa" · P3: rev.6 emitida agora · subscreve R-BUSCA-1/R-CITA-1 sem reserva e confessa rev.3-sem-bytes/hashes-sem-comando) · parecer comentador `b651bd8c…` (**"REV.6 — SEM RESSALVA DO COMENTADOR"** · pedido de réplica com 6 verificações · aprovação reservada ao operador).
- **Réplica da casa (trilha 81, 10/10):** identidade · ajustes verbatim l.305+nota rev.4 · diff confinado (7 linhas, 4 zonas editoriais, §0/§1 intactos) · recorte §2–§13 invariante · **95c7cb410f369410… EXATO nos dois lados (serialização resolvida: \n final)** · **4217cc63… reconfirmada** · §6.3 intacto · 244/41/T-23 âncoras iguais. Regime da própria casa: primeiro teste saiu vermelho no classificador de zonas e na serialização — corrigido ANTES da publicação (a régua segue pegando a casa primeiro).
- **Estado:** triângulo sem ressalva (3/3); **a mesa entrega a palavra ao operador** — aprovação com as palavras DELE sobre a rev.6 `98e90bdc…` (molde da casa rotulado como sugestão, R-CITA-1). Ao chegar: L06_VIGENTE.txt + CHANGELOG + decisoes + estado "vigente em espera de produção" + comunicado aos dois projetos.
- **Não-ressalvas posicionadas:** D-4AJUSTES-OPERADOR (registro; responde quando quiser) · dívidas internas declaradas do documento · D-L06-M3-ORIG residual.
- **Entrega:** réplica rev.6 md sha no pacote · zip sha no CHANGELOG 68 (re-extração ≡).
- **Mesa:** frase do operador · "(i)" · fila de produção pós-aprovação (migração N2 v1.4 243/274 trilha 27 → piloto E2 → revisão formal E4) · herdadas.
- **0 ciência:** trio intacto início→fim.

## Rev.76 — 2026-09-22 (RODADA 69: ★ APROVAÇÃO DO OPERADOR — L-06 VIGENTE ★ escritura na série · comunicado aos dois projetos · fila de produção destravada)
- **FRASE VERBATIM DO OPERADOR (2026-09-22, R-CITA-1):** "Aprovo como vigente a L-06 — Minuta 3 consolidada rev.6, digital 98e90bdc, de 22/09/2026." — Trilha 82 (3/3) homologou: digital bate com o arquivo · frase cobre artefato+digital+data · apoio no triângulo sem ressalva (rev.75). Regra de versionamento honrada na íntegra: PROPOSTA → ALTERAÇÃO DOCUMENTAL → DOCUMENTO COMPLETO ENTREGUE → APROVAÇÃO → SHA/DATA → VIGENTE.
- **Estado:** **L-06 VIGENTE — EM ESPERA DE PRODUÇÃO** · escritura `_documentos_serie/L06_VIGENTE.txt` (sha no CHANGELOG 69) · texto congelado por digital; mudanças futuras somente pelo rito (dois lados não bastam: os três sem ressalva + frase do operador, verbatim).
- **Provas de estabilidade do corpo normativo:** `95c7cb410f369410…` (procedimento do mestre, reproduzido pela casa) e `4217cc635ee12842…` (canônica da casa, aceita por ele) — duas mãos, uma propriedade. `f8ec8b72…` fica na história como intermediário rotulado no próprio documento.
- **Créditos finais (escola da mesa):** conceito das duas frases-clássicas = minuta 1 do mestre (l.97 e l.79) · redação-regra = comentador (TextoH Partes 6.3/8) · síntese e execução 244→0, matriz, suíte T-01..T-23 = minuta 3 (mestre) · verificação, réguas e correções de método = casa · **aprovação = operador**.
- **Destrava:** a decisão sobre produção passa a ser de calendário do operador: migração N2 v1.4 (243/274, trilha 27) → piloto E2 (marcador×nao_estabelecida) → E1 oráculo do gate → E4 revisão formal · E3/E5 no ciclo da Ontologia · L-NT segue esperando a "(i), com a bifurcação desenhada".
- **Entrega:** comunicado md sha no pacote · zip sha no CHANGELOG 69 (re-extração ≡) · `L06_VIGENTE.txt` sha no CHANGELOG 69.
- **Mesa:** "(i)" · D-4AJUSTES-OPERADOR (aberta, responde quando quiser) · v1.5 · v1.8 · O-1/O-2→V2.4 · D-JSONM · D-ORDEM-FASES · D-GOV-B1N1-FONTE · fila N2 v1.4 (propor cronograma quando ele quiser).
- **0 ciência:** trio intacto início→fim. **Ciclo L-06 encerrado com chave de ouro: ninguém em cima do muro, ninguém acima da régua.**

## Rev.77 — 2026-09-22 (rodada 70: integridade da rev.6 provada — uploads ≡ série ≡ escritura, digital igual na chegada e agora; resposta ao operador com comandos de conferência local)
- **Trilha 83 (3/3):** dentro do Arena a rev.6 é intocada (apenas lida pelas trilhas 81/82). Digital de referência para conferência em qualquer ponta: `98e90bdc755162b28fd16817d65692cebe81f939c466ef1d29c7a0a1124f2b41`. O mestre nunca publicou hash da rev.6 — a medição da casa no recebimento é a referência; divergência em qualquer ponta = incidente a reportar.
- **0 ciência.**

## Rev.78 — 2026-09-22 (rodada 71: L-06 × Auditor-Estrutura — aprovação NÃO passava por ele (caso do mestre); CIÊNCIA recomendada com os 5 pontos do território dele mapeados na rev.6; ressalva dele, se vier, é assunto novo do ciclo dele — não reabre vigência)
- **0 ciência.**

## Rev.79 — 2026-09-22 (rodada 72: ROTEIRO de trabalho — filosofia confirmada, status desatualizado (era V2.2); casa entrega ATUALIZAÇÃO DE ESTADO datada p/ acompanhar o original na distribuição; ROTEIRO_PROJETO.md = diário interno, não enviar; roteiro formal só muda por rito)
- **0 ciência.**

## Rev.80 — 2026-09-22 (rodada 73: ponto do auditor-2/estrutura CONFERE 100% (trilha 84, 10/10) · casa ADOTA o portão por critério, não por número · adendo datado no L06_VIGENTE.txt · página do roteiro rev.p1 · mestre/comentador não acionados — assunto do ciclo estrutura)
- **O ponto dele, replicado e confirmado:** a régua 243/274 citada no §8 da L-06 vigente é da era **v1.1** (trilha 27, 15/09, correta à época). Contra o **N2 v1.4** (`d96ad15b620fa373…`), a mesma migração mecânica mede **224/274**: a regra D3 (verbatim no description de `ancoras` e no if/then `g2_elegibilidade == redirecionado_clinico → minItems 2`) entrou na v1.4 (condicional: 0× em v1.1 e v1.3, nível L1) e exige segunda âncora dos 20 redirecionados (todos CANDIDATO; 18/20 já com destino em texto livre no g2_motivo — trabalho de curadoria, não defeito). Assinaturas: 20 segunda-âncora + 30 trilha + 30 uso (os mesmos 30 B1_v2, VALIDADO). Estrito elegível-curatorial: 223 (diferença = VINC_B1_0047, nao_avaliado).
- **3 confirmações dele VERDADEIRAS:** papel não-proxy (R7/description + enum v1.4 verbatim) · contexto/nivel_cadeia 0× como propriedade nas três versões · granularidade: a âncora já tem `escopo` (BLOCO_XX[/sub], APENDICE_CORPUS, null) — **D-L05-GRANULARIDADE-OBJETO relabelada: não é estrutura faltante, é decisão de EXTENDER subdivisão às famílias não-mecanismo** (volta no ciclo v1.5 dele). Nota histórica da casa (honestidade, zero impacto): a data "retirado na v1.3" do `sentido_relacao` não se confirma — campo inexiste nas três versões (v1.1 0× · v1.3 1× só em prosa · v1.4 0×).
- **DECISÃO DA CASA (conselho técnico ao operador):** portão de produção da migração passa a fechar por **CRITÉRIO, não número** — *"migração concluída quando o validador acusar ZERO não-conformes contra o N2 v1.4 digital d96ad15b620fa373…"* — anexado como **adendo datado** ao `L06_VIGENTE.txt` (novo sha `31b9d4c0…`). **L-06 doc: sem toque** — §8 é citação de linhagem com data e fica como está; se a mesa tocar o texto no futuro, a precisão entra no mesmo toque (caso `f8ec8b72`, rito completo dos 3 + frase do operador).
- **Enquadre dele aceito:** "assunto do meu ciclo, não reabertura da vigência" → mestre e comentador **NÃO acionados** neste ponto nesta rodada (rito: se um dia virar toque no texto L-06, passa pelos 3). Ciência anterior (rodada 71) cumpriu seu papel: ele recebeu, leu o §8 e apontou o número antes de virar produção — o circuito de ciência funcionou.
- **Página do roteiro rev.p1:** linha do item 9 e passo 2 agora dizem "portão por critério… ref. 224/274, era v1.1: 243" (md `a0d8df54…`, zip `c6e56692…`). **Nota de resposta ao estrutura selada** (`ENTREGAS/2026-09-22_RESPOSTA_AUDITOR2_PORTAO/`, md `2380f73c…`, zip `8bff7412…`) com tabelas de veredito, adoção do critério e posições da casa.
- **Mesa:** revisão do operador à nota → envio ao estrutura (nada aos outros dois) · envio roteiro+página rev.p1 quando ele quiser · D-4AJUSTES-OPERADOR (aberta) · "(i)" · cronograma da fila de produção (ponto de partida da curadoria: 224/274 mecânico / 223 estrito; 20 redirecionados, 18 com destino marcado) · v1.5 schemas · herdadas.
- **0 ciência:** L-06 VIGENTE intacta (`98e90bdc…`) · trio mestre/comentador/estrutura sem nova ressalva nesta rodada.

## Rev.81 — 2026-09-22 (rodada 74: CONFRONTO COMO EXECUTAR v1.9 × L-06 vigente — ortogonais, 0 contradições, convergência verbatim · correção "G3 é parecer" AUSENTE do v1.9 (0× medido) · pendências re-mapeadas: mestre/estrutura já responderam em 18/09; 4 são do operador · posição: aprovável no conteúdo, NÃO agora — Rota A recomendada (v1.10 primeiro))
- **Escopo do confronto:** v1.9 = manual da linha clínica (G1/G2/G3, protocolo 3-IAs, filas) · L-06 = contrato do Motor (escada de concorrências). Acoplamento nominal 0× nos dois sentidos (medido). A ponte entre os dois é a mesa e a futura alimentação N1/N2.
- **Interface honrada:** E1 (oráculo do gate de consumo, L-06 §5) ganha candidata concreta no fluxo do v1.9 (fechamento pelo operador + confirmação conjunta — sugestão da casa rotulada, ninguém citou antes). Nenhuma linha do v1.9 obrigada pela L-06.
- **Confissões da rodada:** C85-1 (item 6: 26 citações ≠ 22 entradas; 4 ids em logs alheios) · C85-2 (item 3: radical 'retorn' com falso amigo; veredito por trinca) · adendo L2-prosa normalizada (2 padrões zerados por wrap de linha). Todas datadas no JSON da trilha 85.
- **PERGUNTAS ao operador (R-CITA-1, 4):** piloto .014 aconteceu? · linha "(i)" registrável? · Rota A × B? · Bloco/Lista mais novos existem (base da casa para em 15/09)?
- **Mesa:** as 4 perguntas · P1 (correção G3 → ciclo v1.10) · P3 (ressalva em N2 → pacote v1.5 estrutura) · P4 (auditor dos N1/N2) · P6 (homologação fluxo) · herdadas (v1.5 · v1.8 · O-1/O-2→V2.4 · D-JSONM · D-ORDEM-FASES · D-GOV-B1N1-FONTE · D-4AJUSTES-OPERADOR).
- **0 ciência** nos vigentes (L-06 intacta; nada enviado a auditor).

## Rev.82 — 2026-09-22 (rodada 75: carta do comentador — não aprovar v1.9 agora · rito de rodadas territoriais ACEITO pela casa (trilha 86: 5/5) · P1 dele estende o consolidado B (independência cega) · 2 encaminhamentos escritos e selados · envio pendente do operador em 2 janelas limpas)
- **O pedido dele é lei de método:** pareceres independentes (um não vê o do outro antes de entregar) · divergência por território · consolidação da casa sem transformar divergência em consenso · fechamento = homologação do operador sobre solução tecnicamente construída. Compatível com o rito supremo (rev.74): opera dentro, com disciplina anti-contaminação a mais.
- **P1 v1.10 (texto do comentador) carrega mudança de desenho:** análises independentes ANTES da comparação — reescreve IA2 do v1.9 e atende o alerta anti-ancoragem do próprio v1.9. Vai a parecer do mestre na carta 25 (Q1: endosso · princípio de arbitragem preservado? · o que se perde?).
- **P2 re-enquadrada:** derivação técnica (6 eixos estruturais ao estrutura · 6 eixos filosóficos ao mestre — 4 já cobertos pela deliberação 18/09; formalizar + 2 novos) · palavra do operador = homologação no fim. SUPRESEDE declarado: perguntas 2 (linha "(i)") e 3 (rota A×B) da r74 canceladas por escrito.
- **P3** destino da ressalva → estrutura, sob o princípio L-06 §5 (o comentador chegou à mesma regra independentemente). **P4** → parecer registrável dos dois lados (proposta/fundamento/território/conflitos/segregação). **P7** → pergunta mantida ao operador + requisito de homologação (registro próprio do piloto). Base real ≥17/09 necessária na Rodada 5.
- **Mesa:** operador envia as 2 cartas (janelas limpas) + responde piloto/bytes · demais herdadas · fila N2 v1.4 (portão por critério, r73) na fila de produção.
- **0 ciência** nos vigentes.

## Rev.83 — 2026-09-22 (rodada 76: RODADA 3 do rito — CONFRONTO dos 2 pareceres territoriais · ZERO divergência material · trilha 87: 16/16 · 274/274 do estrutura replicado pela casa com nível declarado · 9 itens fora do manual, 5 consequências demonstradas para a v1.10)
- **Divergência material: nenhuma (B = ∅).** P1 = fora de território do estrutura por declaração + resposta do mestre; P2 = convergência material no núcleo (bifurcação necessária · N2 como junta · NT-02 preservada · nenhum contrato novo · mesmo defeito descrito nas duas linguagens); P3 = mapeamento estrutural verificado campo a campo + recusa expressa do mestre; P4 = convergência forte da invariante "quem produz não atesta fidelidade", demonstrada pelo estrutura ao recusar o papel tautológico.
- **Silêncio registrado (não consenso):** assimetria/ordem da bifurcação (precondição da afirmação para N2) sustentada só pelo estrutura → E-1, opcional na Rodada 4. "Os quatro tipos de divergência" citados sem enumeração → E-3.
- **Medições reexecutadas pela casa:** 274/274 ✔ com níveis (273 L1 + 1 L2 — VINC_B1_0153, whitespace) · 237 fichas ✔ · if/then de condicao no N2 v1.4 ✔ · trecho_ancora minLength 1 sem checagem de canônica ✔ · CLAIM_KIT_CLINICO ausente ✔ · 0 chaves-âncora no kit ✔ · 4/4 linhas do v1.9 citadas pelo mestre ✔. Confissão C87-1 (falso órfão por régua da casa).
- **Fila própria da rodada:** E-1 (ordem) · E-2 (quem produz N1/N2 → destrava a atribuição de P4) · E-3 (enumeração) · E-4 (piloto .014: fato do operador) · E-5 (corpus da medida 39/49 declarado) · E-6 (portão de fidelidade da ressalva × invariante do mestre).
- **Mesa:** confronto segue ao comentador (Rodada 5 = consolidação + proposta v1.10, dependente dos bytes ≥17/09) · herdadas intactas (fila N2 v1.4 portão-por-critério · v1.5 · v1.8 · O-1/O-2→V2.4 · D-JSONM · D-ORDEM-FASES · D-GOV-B1N1-FONTE · D-4AJUSTES-OPERADOR).
- **0 ciência** nos vigentes (L-06 intacta; v1.9 não aprovado nem alterado).

---

## Rev.84 — 2026-09-23 (rodada 77: classificação de interface Claim → Biblioteca → N1/N2 · trilha 88 16/16 · matriz A–I + §15 · menor alteração suficiente)

- **Carta do comentador arquivada** (`6c8042da…`) + anexo estruturas (`c58617a9…`, upload ≡ série). Foco mudado: não “quem produz claims” (processo já existe) e sim **como a saída de um claim aprovado usa N1/N2 existentes sem sistema paralelo**.
- **Trilha 88 16/16** — inclui: exemplos do anexo batem com V7/Bloco; `claim_id_origem` escalar (§10 **confirmado** no acervo: 54 preenchidos, um claim cada; uso múltiplo vive nos N2); 0 dup PMID em 237; kit sem chaves-âncora; **14 PMIDs do Bloco fora da Bibliografia** (fila de criação de N1, 12 claims). C88-1 confessada.
- **Posição da casa (sem muro):** aceita “não criar segundo sistema”; **ordem obrigatória:** afirmação entra na Biblioteca → só então N2 (`usado_em_biblioteca` 22/22 `nao` hoje). Ressalva: tabela única G (Estrutura r76). Invariante r76 intacto.
- **Classificação:** faltam contrato de saída + passo de entrada na canônica + resolução pmid→`id_referencia_interna` + enum `CLAIM_KIT_CLINICO` (ciclo N1 v1.5) + reconciliação técnica prévia. **Não** copiar `trecho_ancora`/`ancoras`/`condicao` para o Claim Kit.
- **Mesa:** peça vai aos dois auditores (janelas limpas) com pergunta de compatibilidade da carta §16; depois confronto; só então comentador consolida. v1.9/v1.10 e ciência intocados.
- **Pacote:** `ENTREGAS/2026-09-23_CLASSIFICACAO_INTERFACE_CLAIM_N1N2/` md `9770fe6a…` · zip `839c2cff…` (re-extração 6/6).

---

## Rev.85 — 2026-09-23 (rodada 78: confronto dos pareceres de interface · trilha 89 15/15 · D1 divergência material · Rodada 4 a acionar)

- **Digitais:** Mestre `cbc0ab79…` · Estrutura `86d09995…` · uploads ≡ série · trilha 89 `a3ac7428…` (15/15).
- **A:** núcleo arquitetônico · ordem Biblioteca→N2 · `claim_id_origem` · enum v1.5 via ciclo · fidelidade ≠ produtor.
- **B / D1:** destino de `aprovado_com_ressalva` — **mapeamento único** (Estrutura §5, reaff. r76) × **roteio por tipo** (Mestre §2, com fabricação de condição × L-06 regra 3 medida). D2 = forma binária de D1. Única divergência substantiva.
- **C/D:** 4 itens técnicos do Estrutura 100% replicados; **minuta r77 §E.4 (falha dura de id) corrigida por ele** (sufixo minúsculo); escopo=destino da frase; prefixo clínico de `id_vinculo` a decidir; `forca_causal`/`grau_maturidade` ausentes em clínica = não-aplicável. E-6: comparação de cópias ∉ invariante, com condição de quem executa.
- **Casa:** não adjudica D1; aciona **Rodada 4** com pergunta única (a)/(b)/(c); fecho só com 3× sem ressalva (rito do operador). Contrato de interface **não** emite texto final de ressalva até D1 fechar.
- **Pacote:** `ENTREGAS/2026-09-23_CONFRONTO_INTERFACE_PARECERES/`.

---

## Rev.86 — 2026-09-24 (rodada 79: solução Comentador D1 · trilha 90 11/11 · casa aceita dois eixos · Rodada 4 pronta)

- **Tese aceita:** `status_auditoria` ≠ `direcao_suporte`; `aprovado_com_ressalva → condicional` **abolida** como derivação universal; classificação semântica da ressalva no fechamento do claim; `condicao` só com condição real (L-06 degrau 3 protegido).
- **Trilha 90 11/11** — inclui autocrítica: a Tabela G da minuta r77 da casa era o erro de derivação alvo da carta.
- **H-1** `ressalvas[]`/vocabulário = contrato do kit (ciclo próprio) · **H-2** direção efetiva não-condicional precisa de fonte determinística no Claim→N2 (pergunta ao estrutura na R4) · **H-3** D1 fecha só com 2× subscrever sem ressalva.
- **Não vigente:** nada de N1/N2/kit/L-06 alterado; proposta submetida ao rito dos 3.
- **Pacote:** `ENTREGAS/2026-09-24_RESPOSTA_D1_RODADA4_PRONTA/` com textos prontos para as duas janelas.

---

## Rev.87 — 2026-09-24 (rodada 80: R4 D1 confrontada · D1 aberta · carta ao comentador · rito 3 IAs reafirmado)

- **H-3:** E = sem ressalva; M = modelo sem + fechamento com **duas** ressalvas (R-1 direção; R-2 moderadores) → **D1 aberta**.
- **H-2 fechada em duas pontas** (para a minuta do Comentador): vocabulário `sentido_do_achado` (v3.1, obrigatório, medido) + direção como classificação científica no fechamento (Mestre), nunca default do materializador.
- **R-2 medido:** `inverte` 1× no `.001b` (aprovado_com_ressalva) → caminho de dois vínculos + L-06 disjunção; `atenua`3/`amplifica`5 com destino a declarar; fonte única de `condicao` a eleger.
- **Confissão do Estrutura** (regra abolida era dele) e **generosidade do Mestre** (solução melhor que a própria) registradas.
- **Rito das 3 IAs: manter — fortalecido.** Cada rodada adicionou classificação científica no fechamento (cego → retorno G3 → tipo de ressalva → direção por fonte). **E-4 piloto .014** continua pendente e é o gesto coerente seguinte.
- **Casa prefere Rota A** (integrar R-1+R-2 → minuta final → 2× sem ressalva). Decisão: Comentador.
- **Pacote:** `ENTREGAS/2026-09-24_CARTA_COMENTADOR_RODADA4_D1/` · trilha 91 `30034379232cea90…`.

---

## Rev.88 — 2026-09-24 (rodada 81: Rota A conduzida · minuta do contrato de saída escrita · trilha 92 13/13)

- **Decisão do Comentador:** Rota A; pedido verbatim de minuta final integrando D1+R-1+R-2; encerramento só com 2× sem ressalva + verificação mecânica da casa + pacote limpo ao operador.
- **Minuta da casa** (`fe27012a…`): 4 saídas do claim fechado; direção por fonte com `sentido_do_achado` (v3.1) e falha dura sem direção; proibição de defaults; fonte única de `condicao`; `inverte` → dois N2 (`.001b`); atenua/amplifica ficam no claim; maturidade → `grau_maturidade`; tabela de materialização; pendências P-K1..P-K5 travam a 1ª materialização; 0 alteração de N1/N2.
- **Ressalvas de régua:** T2 e T13 falsos negativos (negrito e caixa) corrigidos antes de publicar — C92-1.
- **Pacote subscrição:** mesma COLA para as duas janelas (a minuta é o mesmo documento). Zip re-extração 6/6.

---

## Rev.89 — 2026-09-24 (rodada 82: ponto do inverte CONFIRMADO · rev.2 P-K6 · v3.1 ao Mestre · C92-2)

- **Objeção do Estrutura ao §4.3: CORRETA** (TRILHA93 12/12, simulação do allOf). Rev.1 não encerra D1.
- **Mestre:** sem ressalva; fronteira declarada (não testou schema); **lacuna honesta: não recebeu v3.1** mas assinou texto que a cita → pacote rev.2 **inclui v3.1**.
- **Rev.2:** `inverte` = P-K6, não materializa; `condicao_modificadora` registrado como caminho v1.5 (não adotado). Documento mudou ⇒ **2× novo**.
- **C92-2:** medir citação ≠ medir validade; simulação de schema agora obrigatória em regra de materialização nova.
- **Pacote:** `ENTREGAS/2026-09-24_ANALISE_SUBSCRICOES_REV2/` · zip re-extração 9/9.

---

## Rev.90 — 2026-09-24 (rodada 83: rito corrigido — ressalva passou pelo Comentador · P-K6 ratificado · rev.2 FINAL)

- **Operador acertou o rito:** antes de reenviar aos auditores, a ressalva do §4.3 voltou ao Comentador. Mesa da r82 superseded.
- **Comentador (sha 4783526a…):** P-K6 = fail-closed de integridade; preserva Rota A; **granularidade por claim** (§6); sem alterar de novo o inverte; pergunta P-K1..P-K6.
- **Rev.2 FINAL (sha 841532da…):** granularidade incorporada + resíduos rev.1 removidos (tabela, P-K4, §11). TRILHA94 10/10.
- **Próximo:** COLA do pacote às duas janelas → 2× sem ressalva → réplica final → D1 encerra → piloto .014.

---

## Rev.91 — 2026-09-24 (rodada 84: D1 ENCERRADA — 2× sem ressalva na rev.2 · TRILHA95 12/12)

- **Encerrada** pelo critério do Comentador §19: E sem ressalva · M sem ressalva (retratação) · réplica 12/12 · pacote publicado.
- **Vigente:** minuta rev.2 `841532da…` como contrato de derivação Claim→N2. Trava P-K1..P-K6. `.001b` espera v1.5 (P-K6). N1/N2 intocados.
- **Método provado nas duas pontas** (assinaturas): reexecutabilidade contra artefato > concordância entre mesas · C92-2 mantida.
- **Próximo:** piloto `.014` com rito corrigido · ciclo do kit (P-K1/P-K2) · ciclo v1.5 (P-K6) · bytes ≥17/09.
- **Pacote:** `ENTREGAS/2026-09-24_ENCERRAMENTO_D1/`.

---

## Rev.92 — 2026-09-24 (rodada 85: VIGÊNCIA do Contrato de Saída do Claim Kit rev.2)

- **Frase do operador (verbatim):** "Aprovo como vigente o Contrato de Saída do Claim Kit — rev.2, digital 841532da, de 24/09/2026."
- **Selado:** série `CONTRATO_SAIDA_CLAIMKIT_rev2_vigente_2026-09-24/` + ponteiro `CONTRATO_SAIDA_CLAIMKIT_VIGENTE.txt` (6300495f…).
- **Vigente:** derivação Claim→N2 (dois eixos, sem default, fonte única, inverte P-K6 travado). Trava P-K1..P-K6. 0 alteração N1/N2/kit.
- **Continuidade (próximos, nesta ordem):** (1) ciclo do kit P-K1/P-K2; (2) COMO EXECUTAR v1.10 (C-1..C-5 + cegos + referência ao contrato vigente); (3) piloto `.014`; (4) v1.5 P-K6.
- **Pacote:** `ENTREGAS/2026-09-24_VIGENCIA_CONTRATO_SAIDA_CLAIMKIT/`.

---

## Rev.93 — 2026-09-25 (rodada 86: kit 17/09 recebido · TRILHA96 14/14 · bytes encerrados)

- **Corpus vigente clínico:** Bloco v1.8 + Lista v1.5 (2026-09-17). Digitais seladas; série `KIT_CLINICA_ATUALIZADO_recebido_2026-09-25/`.
- **27 claims** · +6 (`.014`=`aprovado_com_ressalva`) · `.012b/c` na Lista · Schema-Claim e v1.9 intocados.
- **E-4 permanece aberta:** claim no Bloco ≠ piloto de processo (3 IAs cegas + retorno G3).
- **Próximos desbloqueios:** ciclo do kit (P-K1/P-K2) → v1.10 sobre corpus 17/09 → piloto `.014`.

---

## Rev.94 — 2026-09-25 (rodada 87: ciclo do kit aberto · minuta Schema-Claim v1.3 · TRILHA97 13/13)

- **Pedido do operador:** "Ciclo do kit" — fechar P-K1/P-K2 (trava da 1ª materialização).
- **Minuta v1.3** (não vigente): 4 mudanças nomeadas (P-K1/P-K2/P-K3/P-K5) + V-K1..V-K5 + migração honesta (claims 17/09 não reescritos; sem sentido_do_achado não materializa).
- **Próximo:** Comentador → auditores → aprovação do operador (rito dos 3 + palavra dele).

---

## Rev.95 — 2026-09-25 (rodada 88: comentador aprova v1.3 p/ ciclo · V-K3 ajustado · rev.2 · COLAs territoriais)

- **Comentador:** P-K1..P-K5 aprovados para o ciclo; 1 ajuste (V-K3 opção preferida); ordem: auditores em janelas; fechar ciclo → v1.10.
- **Minuta rev.2** `bd9360e0…` com V-K3 alinhado; TRILHA98 10/10.
- **Próximo:** COLA_ESTRUTURA + COLA_MESTRE nas janelas → dupla subscrição → encerramento do ciclo do kit.

---

## Rev.96 — 2026-09-25 (rodada 89: V-K6 ressalva real · rev.3 escrita · trilha 99 9/9)

- **Divergência:** M sem ressalva × E com ressalva V-K6 (precedência na materialização). Ressalva **confirmada empírica** (TRILHA99 T4).
- **Rev.3** aplica a formulação do próprio Estrutura (condicao_aplicacao governa o ato; sentido fica no claim) + V-K7. Documento mudou ⇒ 2× novo após validação do Comentador.
- **Próximo:** COLA_V13rev3_COMENTADOR → depois janelas.

---

## Rev.97 — 2026-09-25 (rodada 90: comentador aceita rev.3 · COLAs rev.3 prontas)

- **Aceitação:** V-K6/V-K7 válidos; sem segunda semântica; libera janelas.
- **Próximo:** 2× subscrição sobre a rev.3 (`28cbc9c7…`). Depois: encerrar ciclo do kit → v1.10.

---

## Rev.98 — 2026-09-25 (rodada 91: ciclo do kit ENCAVEL — 2× sem ressalva na rev.3 · TRILHA100 10/10)

- **Encavel** pelo critério do rito: Comentador aceitou rev.3; E e M subscreveram sem ressalva; casa replicou 10/10.
- **Epílogo bytes:** rev.2 enviada por engano → detectada pelo E → rev.3 canônica `28cbc9c7` confirmada antes da assinatura (disciplina do ciclo inteiro).
- **Vigência** depende da frase do operador. Depois: v1.10.

---

## Rev.99 — 2026-09-25 (rodada 92: VIGÊNCIA Schema-Claim v1.3)

- **Frase do operador (verbatim):** "Aprovo como vigente o Schema-Claim v1.3 — rev.3, digital 28cbc9c7, de 25/09/2026."
- **Selado:** série `SCHEMA_CLAIM_v1.3_rev3_vigente_2026-09-25/3º SCHEMA-CLAIM — v1.3.md` + ponteiro `SCHEMA_CLAIM_V1_3_VIGENTE.txt`.
- **Ciclo do kit oficialmente encerrado.** Travas mantidas. Próximo: v1.10.

---

## Rev.100 — 2026-09-25 (rodada 93: ciclo v1.10 aberto · minuta + TRILHA101 12/12)

- **Pedido:** "vamos abrir". Três bases vigentes confirmadas (contrato 841532da · schema 28cbc9c7 · corpus 17/09).
- **Minuta v1.10** (não vigente): C-1..C-5 + 4 decisões + X-1 + materialização separada; v1.9 intacta.
- **Próximo:** Comentador → auditores → operador.

---

## Rev.101 — 2026-09-25 (rodada 94: comentador libera v1.10 · COLAs territoriais)

- **Liberação:** sem falha estrutural; P-K5 não bloqueia; apta às janelas.
- **Próximo:** 2× subscrição sobre a minuta v1.10 (sha 49514344…).

---

## Rev.102 — 2026-09-25 (rodada 95: ciclo v1.10 ENCAVEL · TRILHA102 8/8)

- **2× sem ressalva** na minuta `49514344…`. Notas E/M registradas sem bloqueio.
- **Próximo:** frase de vigência do operador → os 3 documentos do processo ficam vigentes → piloto `.014` com desenho congelado.

---

## Rev.103 — 2026-09-25 (rodada 96: VIGÊNCIA COMO EXECUTAR v1.10)

- **Frase do operador (verbatim):** "Aprovo como vigente o COMO EXECUTAR — v1.10, digital 49514344, de 25/09/2026."
- **Selado:** série + ponteiro `COMO_EXECUTAR_V110_VIGENTE.txt`.
- **Processo com 3 vigentes.** Próximo: piloto `.014` (E-4) com o desenho deste documento.

---

## Rev.104 — 2026-09-25 (rodada 97: ensaio pré-piloto · trilha 103 10/10 · casa aceita com S-1..S-5)

- **Desenho aceito:** ensaio com o grupo da construção (testa a máquina) → congelar pacotes → piloto oficial com tríade dedicada cega (mede o método).
- **S-1..S-5** registradas: estado do .014 no Bloco · corpus ×2 · E-4 aberta · registro na série · mecanismo ≠ cegueira.
- **Próximo:** execução do ensaio (operador) → registro → pacotes → piloto oficial.

---

## Rev.105 — 2026-09-25 (rodada 98: errata da Casa · complemento do ensaio)

- **Emitida** a errata com os 10 pontos (S-1..S-5 + bases + pacote mínimo + sem silêncio + tríade). Histórico preservado; não é aprovação nem reabertura.
- **Novo explícito:** Contrato rev.2 = base normativa, mas **não entra no pacote mínimo de sessão** se o v1.10 não exige.
- **Próximo:** COLA nos 2 auditores → 1ª rodada do ensaio.

---

## Rev.106 — 2026-09-25 (rodada 99: carta de abertura do novo chat do Estrutura)

- Carta única: identidade · bases · ensaio · errata condensada · estado r1 · papel transitório. No lugar da errata como 1ª mensagem.

---

## Rev.107 — 2026-09-25 (rodada 100: instrução do ensaio · papel do Estrutura · G1 = execução)

- **Fluxo aprovado pelo operador:** 2 rodadas (G2 cego → acordo → G3 cego → fechamento). Mapeia o v1.10 em lotes.
- **G1:** lista na tela + busca de PMID ao vivo = G1 executando (correção do operador aceita; E-01 reclassificado).
- **Estrutura:** observador+registrador (escolha do operador registrada); G1/G2/G3 = IA1+IA2 (+Mestre se quiser).
- **Instrução em linguagem simples** pronta para colar nas 3 IAs.

---

## Rev.108 — 2026-09-25 (rodada 101: instrução rev.2 — papéis fixados · G1 com limite · contagem 107×92)

- **rev.2** da instrução: 4 papéis fixos (Comentador); G1 = lista disponibiliza, resolução completa (Estrutura); nota de contagem; 4 resultados ≠ votos.
- Pendência operacional: reconciliar 107 × 92 antes de congelar lista.

---

## Rev.109 — 2026-09-25 (rodada 102: execuções do ensaio — Mestre e Arena)

- Duas execuções completas (G1+G2+G3) arquivadas. Achado factual G1-a: PMID do Setiawan 2015 na execução do Mestre errado; certo 25629589.
- Próximo: cruzar filtros (IA1 × Mestre × Arena) e congelar lista saneada.

---

## Rev.110 — 2026-09-25 (rodada 103: cruzamento 3 filtros · D-a..D-d)

- Veredito comum: suporta + heterogeneidade; status mantido. Divergências factuais isoladas e resolvidas na fonte (ou marcadas: Yrondi, contagem).

---

## Rev.111 — 2026-09-25 (rodada 104: E-04 sequência · E-05 contagem · rev.2.1 paradas)

- Mesma lista confirmada → baseline 107. Instrução ganha PARADAS obrigatórias (ENTREGA E PÁRA) para piloto. Próximo: sanear → fechamento → S-4 consolidado.

---

## Rev.112 — 2026-09-25 (rodada 105: FECHO DO ENSAIO .014)

- Registro final S-4 publicado; fase de ensaio encerrada; adiados registrados (redirecionados · candidatos ID).
- Próximo: sanear lista → congelar pacotes da tríade → PILOTO OFICIAL .014.

---

## Rev.113 — 2026-09-25 (rodada 106: minuta v1.11 — paradas E-04 no documento)

- Mudança mínima no protocolo de 3 IAs; TRILHA105 8/8; v1.10 intacta. Próximo: Comentador.

---

## Rev.114 — 2026-09-25 (rodada 107: T3 reforçado · v1.11 vai às janelas)

- Comentador: apta após T3 por ordem. T3 reescrito (5 marcas ordenadas), 8/8. COLAs prontas.

---

## Rev.115 — 2026-09-25 (rodada 108: v1.11 ENCAVEL · TRILHA106 7/7)

- 2× sem ressalva. Próximo: frase de vigência → substitui v1.10. Depois: sanear lista → piloto oficial.

---

## Rev.116 — 2026-09-25 (rodada 109: rev.2 consolidada · reconfirmação pendente)

- Formulação do Comentador aceita e incorporada (2 paradas de rodada). Rev.1 assinada ≠ rev.2 → COLA de reconfirmação aos 2. TRILHA107 10/10.

---

## Rev.117 — 2026-09-25 (rodada 110: v1.11 rev.2 ENCAVEL · TRILHA108 7/7)

- 2× sem ressalva na rev.2 (2efc0edd). T7 refeito: total 34004 · corpo 27667 · divergentes 0. Próximo: frase do operador.

---

## Rev.118 — 2026-09-26 (rodada 111: vigência v1.11 · roteiro 26.09.26 analisado · carta aos auditores)

- v1.11 rev.2 VIGENTE (`2efc0edd`). Roteiro novo alinhado às intenções; 3 correções de sincronia (v1.10→v1.11 · ensaio encerrado · regra 3 IAs). Carta emitida — após dupla concordância: aplicar S-1..S-3 e publicar.

---

## Rev.119 — 2026-09-26 (rodada 112: roteiro 27.09 analisado — 18/18 · S-1..S-3 resolvidos)

- Comentador corrigiu tudo; casa confirma. Carta final pronta — 1 rodada junto aos auditores.

---

## Rev.120 — 2026-09-26 (rodada 113: uploads organizado Atuais/Antigos)

- 86 arquivos classificados por vigência e categoria. Índice gravado. Raiz limpa.

---

## Rev.121 — 2026-09-26 (rodada 114: roteiro 27.09 PUBLICADO — 2× sem ressalva)

- Próximo do roteiro: validar documentos/ferramentas (crivo 3 IAs, anamnese primeiro) → vigência → pacotes → piloto oficial .014.

---

## Rev.122 — 2026-09-26 (rodada 115: errata do roteiro — V2.3 + nota de sequência · local principal na raiz)

- Correções do operador aplicadas (10 linhas); sha `5f8b89dc…`. Próximo: (opcional) avisar auditores · seguir §19 (validação anamnese → piloto).

---

## Rev.123 — 2026-09-26 (rodada 116: corpus do piloto congelado + pacote da tríade)

- Saneamento completo · corpus sha 20c7159b · COLA por janela dedicada. Próximo: operador entregar às 3 IAs dedicadas e comandar Rodada 1.

---

## Rev.124 — 2026-09-26 (rodada 117: prompts de sessão nova para os auditores)
