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
