# Auditoria Científica de Conteúdo — B7 (Eixo Intestino–Cérebro/Microbiota)

**Data:** 2026-09-05 · **Sessão:** Rodada 2/3 (operador de geração; P-6 2ª verificação independente/avaliador cego PENDENTE).
**Objeto:** trechos-âncora da `B7 EIXO INTESTINO CEREBRO V1 CANONICA.md` (7.693 palavras).
**Ferramentas:** G1 eutils (esearch+esummary+efetch), G2 espécie/elegibilidade, G3 suporte por abstract colado; `gate_script.py` (P-5) + `validar_auditoria.py` (framework).

## Contagem
- Trechos no ledger: **47** · status: {'APROVADO': 42, 'APROVADO_COM_RESSALVA': 5}
- G1: {'VERIFIED_REFERENCE': 47}
- G2: {'NAO_APLICAVEL': 13, 'ELIGIBLE_SOURCE': 34}
- G3: {'APROVADO': 42, 'APROVADO_COM_RESSALVA': 5}

## Decisões-chave (abstract colado nesta sessão)
1. **Vagotomia (Bravo 2011):** efeito de L. rhamnosus sobre GABA/ansiedade AUSENTE em vagotomizados → prova de rota em roedor [APENAS PRÉ-CLÍNICO]; em humano não testado.
2. **FMT trans-fenótipo (Kelly 2016; Zheng 2016):** FMT de deprimidos→roedor induz anedonia/ansiedade → causalidade animal; abismo roedor↔humano.
3. **FMT-RCT 2026 (Li J 42309058):** endpoint PRIMÁRIO (remissão semana 8) NULO; HARD-17 reduziu mais → APROVADO_COM_RESSALVA/emergente; único, aguarda replicação.
4. **Meta FMT (Li B 41921871):** g=-0,81/-1,05, heterogênea → ressaltada.
5. **Probióticos (Moshfeghinia 40440772):** SMD grande aparente mas I²≈96%; Cohen Kadosh 34131108 NULO em jovens (SMD -0,03); Shakir 41605120 sem queda de IL-6/TNF → efeito pequeno/heterogêneo, sem mediação citocínica obrigatória.
6. **Associação (Nikolova 34524405):** padrão transdiagnóstico, sem táxon universal; região/medicação confundem.
7. **5-HT (Yano 25860609):** entérica/periférica, NÃO cerebral; GABA microbiano (Strandwitz) é ecologia, não reposição.
8. **Barreira:** Maes 2008 (um grupo) e Stevens 2018 (carta n pequeno) ressaltados; zonulina/FABP2 não validados (Bibolar).

## Redirecionamentos
- Animal/germ-free/FMT/vagotomia → `redirecionado_mecanistico`, [APENAS PRÉ-CLÍNICO]/[EXT].
- Associação populacional → linguagem associativa; MR/intervenção emergente não afirmada como causal.
- Nenhum trecho removido por falta de fonte; claims rebaixados/ressalvados onde a força era menor.

## Declaração
> A Biblioteca_B7 foi auditada quanto a conteúdo em 2026-09-05: cada afirmação factual tem vínculo verificado (G1→G2→G3) ou está sinalizada como parcial/pré-clínica. `validar_auditoria.py`: **0 ERRO, 0 AVISO**; `gate_script.py`: **GATE APROVADO**.
> **Pendência P-6:** 2ª verificação independente (avaliador cego) dos claims de alto risco (FMT-RCT/meta, Bravo vagotomia, metas de probiótico).

---

# Rodada [AT] 2026-09-09 — reconciliação de insumo externo (P-7) → V2

**Insumos (5):** GPM_B7_EixoIntestinoCerebro.md (oficial) + BRIEFING_B7_EIXO_INTESTINO_CEREBRO_RODADA0.md + BRIEFING_CONSOLIDADO_B7_v1.md + anexo de citações (196 DOIs) + Resumo do insumo para B7 Chatgpt.md (34 claims B7.SM02.001–034 + 3 regras de ouro).
**Regra aplicada:** auditoria ref a ref ANTES de qualquer fusão; nada entra sem resolver no PubMed.

## Auditoria (números reais vs. briefing)
- Anexo: 196 DOIs únicos (briefing dizia "178" — incongruência exposta) + Carabotti 2015 sem DOI,
  resgatada por busca dirigida = PMID 25830558 (verificada por autor+ano+tema).
- G1 eutils (esearch DOI[aid] + esummary + efetch): 192/196 resolvidos; **4 NÃO-INDEXADOS
  confirmados** (Thomas 2021 bioRxiv, Towriss 2026 preprint, Xia 2025, Zhang 2026) → fora, sem
  fonte forjada. **0 falsos positivos** (8 alertas de grafia/parse: falso-alarme).
- Tabela-mestra GPM: 30 âncoras validadas (texto dizia "31" — menor); **7 já vigentes** na V1
  (Braniste, Cryan 2019, Socała, Góralczyk + Bonaz, Hwang, Margolis) → 23 masters novas.
- Sobreposição anexo∩V1: 8 refs (7 masters + Kennedy 2017) → fila real = 188 itens únicos.
- 2 refs sem abstract no PubMed: Tulkens 2020 (Gut, letter+research — G3 por título/periódico/
  autores; ENTRA como janela humana de translocação, claim ASSOCIATIVO) e Akiba 2021 (editorial — BAIXO).

## Matriz de decisão (188) — RELATORIO_AUDITORIA_MATRIZ_B7.md + matriz_b7_decisao.json
- **ENTRA 31** — 23 masters GPM + 8 janelas com seta causal ausente na V1 (Tulkens 2020;
  Nøhr 2013; Chenghan 2025 rhesus/BBB; Kuo 2021 "ZO-1 dispensável"; Stanimirov 2025 bile;
  Ohara 2025 neuroepitélio; Baj 2019 glutamato; Zhang Q 2025 multiômica cognição TDM).
- **BAIXO 131** — redundância auditada por família (reviews genéricas do eixo/AGCC/Trp-KYN;
  primários de barreira Caco-2 com intervenção única; sepse/doença-órgão; tangenciais).
- **EXC 26** — malha de escopo exposta: pecuária/veterinária (5), Alzheimer (5),
  neurodegenerativos gerais (4), Parkinson (3), EM/EAE (3), epilepsia/TCE (2), AVC (3), autismo (1).

## Fusão (V2 = 116 refs; 9.356 palavras)
- Inserções aditivas: §1.1 (Aburto & Cryan; Carabotti), §2.2 (cadeia LPS→TLR4→MyD88→MLCK→TJ
  + endotoxemia + EVs humanas + freio ZO-1), §2.4 (AGCC mecanístico: Erny/Spichak/Caetano-Silva/
  Barki/Cheng/Chen N/Chenghan/Nøhr/Saikachain), §2.5 (Trp-KYN: Agus/Bosi/Chen LM/Schwarcz/
  Sathyasaikumar/Zhao/Li CC), §2.6 (Stanimirov), §2.7 (Baj), §4.1 (Ohara), §5.2 (Lin/Zhou/Zhang Q),
  TABELA DE EVIDÊNCIAS (+3 linhas), CONTROVÉRSIAS.
- **Regras fixadas verbatim:** B7-CAUSAL-01 (sem ponte funcional, composição ≠ mecanismo causal),
  B7-CAUSAL-02 (metabólito isolado ⇒ claim metabólito→cérebro; guarda Sathyasaikumar/Schwarcz),
  B7-CAUSAL-03 (microbiota↔depressão humana = ASSOCIATIVA); formulações protegidas
  (Erny = acetato→aptidão/maturação microglial; Chen N 2024 = cadeia de ROEDOR AGCC→ACSS2→
  PPARγ→TPH2, vedada a transcrição clínica).
- Tríade sincronizada: pmids **85→116** · vínculos **40→71** (trechos-âncora literais na V2) ·
  ledger **47→78** (rodada identificada em verificacao.verificador; vocabulário controlado do
  framework observado em origem_entrada/acao_correcao) · manifesto v2 · trilha
  producao/04_AT_ciclo_2026-09-09.json.

## Portões (revalidados 2026-09-09)
- gate_script.py (P-5): **APROVADO** (refs Módulo09: 116; vínculos N2: 71).
- validar_auditoria.py (framework): **0 ERRO, 0 AVISO**.
- checklist_entrega.py: **41/41 OK, 0 FALHA**.

## Pendências declaradas
- **P-6 (2ª verificação cega, Via 2):** PENDENTE ao fim da rodada (16/16), cobrindo todas as
  levas [AT] B1–B16 — não autocertificável.
- NAO-IDX (4) monitorados; se a ciência amadurecer, entram como [G1] declarado.
