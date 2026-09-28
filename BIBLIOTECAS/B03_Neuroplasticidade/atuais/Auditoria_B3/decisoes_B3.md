# Auditoria Científica de Conteúdo — B3 (Neuroplasticidade)

**Data:** 2025-08 (retrocompatibilização ao padrão B7/B8) · **Sessão:** operador de geração; **P-6** (2ª verificação independente/avaliador cego) PENDENTE.
**Objeto:** trechos-âncora da canônica `B3 NEUROPLASTICIDADE V1 CANONICA.md`.
**Ferramentas:** G1 eutils (esearch+esummary+efetch), G2 espécie/elegibilidade, G3 suporte; `gate_script.py` (P-5) + `validar_auditoria.py` (framework).

## Contagem de decisões
- Trechos no ledger: **51**
- G1: {'VERIFIED_REFERENCE': 51} · G2: {'ELIGIBLE_SOURCE': 34, 'NAO_APLICAVEL': 17} · G3: {'APROVADO': 40, 'APROVADO_COM_RESSALVA': 11}
- status_auditoria: {'APROVADO': 40, 'APROVADO_COM_RESSALVA': 11}

## Notas
- Módulo 09 no schema oficial (id_referencia_interna `REF_SOBRENOME_ANO`, doi, claim_id_origem; 5 arquivos).
- Referências citadas apenas em listra/corpus indexadas por rótulo canônico (apêndice de corpus) para rastreabilidade; citações clássicas de prosa sem PMID verificável foram rebaixadas a menção nominal sinalizada ao P-6 (R04: campo vazio preferível a dado inventado).
- Evidência animal/pré-clínica sinalizada `[APENAS PRÉ-CLÍNICO]/[EXT]`; bloco natureza_sistema (P12), semantic_layer (R06) e referência cruzada a B16 (P16) presentes na canônica.

## Declaração
> A Biblioteca_B3 foi auditada quanto a conteúdo: cada afirmação factual tem vínculo verificado (G1→G2→G3) ou está sinalizada como parcial/pré-clínica. `validar_auditoria.py`: **0 ERRO**; `gate_script.py`: **GATE APROVADO**.
> **Pendência P-6:** 2ª verificação independente (avaliador cego).

---

# Rodada [AT] 2026-09-08 — reconciliação de insumo externo (P-7) → V2

**Insumo:** "matriz canônica B3" (texto de consolidação) + anexo Consensus (193 itens, 193 DOIs únicos).
**Auditoria (obrigatória antes da fusão):** esearch DOI[aid] ×193 + esummary/efetch ×194 PMIDs; conferência autor+ano+tema; cruzamento com 53 vigentes. Relatório: `producao/insumos/RELATORIO_AUDITORIA_MATRIZ_B3.md`.

## Resultados G1
- 185/193 DOIs resolvidos (95,9%); **0 falsos positivos de identidade**; 58/58 PMIDs da consolidação conferem (incluindo as substitutas: Storey 39562042, Brown 41633835, Ma 40339008 [Science 2025], Calder 39613915, Arefin 42066082, Prabakar 42287566, Bulek 41526004).
- "Zhang 2016 PMID ?" cravado pela auditoria: **Zhang JC 2016 = 26786147**.
- 34 divergências de rótulo = defasagem de ano (online-first); **3 divergências de autoria** no anexo corrigidas (artigos válidos): "Schofield 2009"→Gatt JM 2009 (19153574); "Pich 2018"→Cavalleri L 2018 (29158584); "Zhang 2018"→Yao N 2018 (29158578).
- Já vigentes (não duplicar): Li 2010 (20724638), Autry 2011 (21677641), Kavalali 2012 (23534055), Zanos 2016 (27144355), Meshkat 2022 (36194941).

## Rejeições (documentadas na trilha P-7)
- **8 não-resolvidos:** dissertação, 2 bioRxiv, arXiv, resumo de congresso, periódico não indexado, capítulo Bremner (substituto 18037014 = TEPT-específico → EXC escopo), pré-print Storey (substituído pela versão publicada).
- **2 erratas** (34880451, 35364073): metadados dos artigos incluídos, não refs independentes (unicidade Módulo 09).
- **33 EXC escopo** (verificadas por MESH/abstract): EM, anorexia, Alzheimer ×3, dor, neurodegeneração ×4, Fragile X ×2 (incl. Thomazeau Fmr1-KO), β-amiloide, **TBI/TCE**, **modelo pós-AVE**, **TEPT×3 (Bremner 18037014 — divergência explícita vs. insumo —, He 2018, López-López 2025)**, editorial cardiovascular, FND, fitoterápicos/miméticos/baicalina ×3, histórico, meta-ciência, rede genérica, redundâncias pontuais.
- **42 baixo incremento/redundância:** plasticidade básica sem vínculo doença (GRIP1, STEP61, AIDA-1, cortactina, palmitoilação, subunidades GluN2 genéricas etc.), neurogênese-estrutural (P16 → B16), didático EMT, revisões genéricas redundantes.

## Incorporadas: 112 (53→165)
- **A (2.1)** Kozisek 2008, Castrén 2021, Marshall 2018, Moya-Alvarado 2023, Numakawa 2024, Alsalloum 2023, Wang JQ 2019.
- **B (2.2)** Kang 2022 [MA], Krystal 2024, Duman 2012/2019, Kavalali 2025, Bottemanne 2023, Parekh 2022, Zanos & Gould 2018, Lin 2021, Wu M 2021, Zaytseva 2023, Suzuki 2021, Shi 2024.
- **C (2.3)** Hess 2022, Kim 2023, Yao N 2018, Suzuki K 2017, Zanos 2023, Brown 2025/2026, Wu H 2021, Wei 2022, Ma 2025.
- **D (2.4)** Brown KA 2024, Arefin 2026, Elmeseiny 2024.
- **E (novo 1.6 METH)** Storey 2025, Sanderson ×3, Diering ×2, Soares 2013, Peng 2010, Sumi 2020/2023, Fernández-Monreal 2012, Yong 2020.
- **F (3.1 Val66Met)** Anastasia 2013, Kailainathan 2016, Mizui 2015, Youssef 2018, Kishi 2017, Yu 2012, Tian 2021, Gatt 2009, Notaras 2017/2020, Pagliusi 2022.
- **G (3.2)** He 2023, Comai 2024, Wang YT 2022, Miller OH 2014, Luscher 2020.
- **H (3.3 B1↔B3)** Lu 2022, Yao W 2022, Parrott 2021, Zhang JC 2016.
- **I (5.1 B3.C05)** Arosio 2021, Nikolac Perkovic 2023, Schmidt 2010 [EXTRAPOLADO], Calder 2025 [MA-NEG].
- **J (5.3 sondas)** Liu RJ 2017 (GLYX-13), Izumi 2022 (N₂O).
- **K (novo 5.4 humano direto)** Nissen 2010, Rygvold 2022 [NEG], Höflich 2021, Nikolova 2018, Tartt 2022, Appelbaum 2023, Chen 2024, Phoumthipphavong 2016, Treccani 2019, Pryazhnikov 2018, Cavalleri 2018.
- **L (6.3)** Aleksandrova 2021. **M (6.4 ansiedade)** Sha 2023, Shin 2020. **N (7.1)** Santos 2023, Benatti 2024.
- **O (síntese+fronteiras)** Pittenger 2008, McEwen 2012/2016, Chattarji 2015, Wilson 2015, Lau 2017, Patel 2019, Leuner 2013, Algaidi 2025, Ren 2025, Lugenbühl 2025, Price 2020, Christoffel 2011, Marsden 2013, Liu W 2017, Forrest 2018, Ruggiero 2021, Robinson 2021, Laham 2021, Aguilar-Valles 2026, O'Donnell 2026, Liao 2025, Bulek 2026, Prabakar 2026, Carmellini 2025.

## Incidentes da rodada
1. TAGs iniciais distorcidas (reviews humanas classificadas EC por ordem de regra) → corrigidas (MA2/OB54/ML42/EC14); Ma 2025 e Cavalleri 2018 reclassificados ML (H+iPSC/mouse) após conferência MESH.
2. Bug destruturação de tupla no gerador de claim_id (`base[1]` = char) → corrigido antes de gravar; nenhum artefato inválido persistiu.

## Portões (V2)
- gate_script.py (P-5): **APROVADO** (165|165) · framework: **0 ERRO** (53 avisos padrão) · checklist_entrega: **41/41** · P-4: adendo V2 revalidado (15/15 SIM) · palavras 10.206 · 0 PMID no corpo.
- **P-6: PENDENTE** — leva [AT] incorporada ao pacote cego Via 2 (com B1/B2); não autocertificável.

## Declaração
> V2 aprovada nos portões oficiais com ciência primeiro (auditoria ref a ref do insumo antes da fusão; nada entrou sem resolver no PubMed; TEPT/TCE/AVE/neurodegeneração mantidos fora; erratas não viraram refs). Pendências explícitas: P-6 Via 2.
