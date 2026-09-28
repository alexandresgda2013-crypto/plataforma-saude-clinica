# Auditoria Científica de Conteúdo — B9 (Disfunção Mitocondrial)

**Data:** 2026-09-06 · **Sessão:** Rodada 2/3 (operador de geração; **P-6** avaliador cego PENDENTE).
**Objeto:** trechos-âncora da `B9 DISFUNCAO MITOCONDRIAL V1 CANONICA.md` (7.008 palavras).
**Ferramentas:** G1 eutils (esearch+esummary+efetch; tema validado contra o GPM), G2 espécie/desenho, G3 suporte; gate_script.py (P-5) + validar_auditoria.py (framework).

## Contagem
- Trechos no ledger: **28** · status: {'APROVADO': 28}
- G1: 28 âncoras resolvidas por autor+ano+tema (falsos positivos de sobrenome rejeitados)
- G2: 5 pré-clínicas (redirecionado_mecanistico), 23 humanas/revisão (eligible)

## Decisões-chave
- **Reserva respiratória** é o defeito humano funcional (Karabatsiakis/Hroudová/Fernström) — não "ATP baixo".
- **Causalidade forte é animal** (MFN2-NAc Gebara; PGC-1α Deng; GSH Madrigal) → [ML]/[EXT]/[APENAS PRÉ-CLÍNICO].
- **Bipolar ≠ TDM**: supressão OXPHOS pós-morte mais robusta no bipolar (Konradi/Andreazza/Ben-Shachar).
- mtDNA copy number sem direção única (Calarco); cf-mtDNA inespecífico (Trumpff) → marcadores de pesquisa, não diagnóstico.
- Estresse → GRα mitocondrial/COX (Picard & McEwen).
- Âncoras animais/emergentes sem PMID humano confirmado (fissão Nat Metab, Zhang Redox, HDAC7, NDUFB9, transplante mito, urolitina) sinalizadas [ML]/[EMERGENTE]/P-6; nenhuma forjada.

## Declaração
> A Biblioteca_B9 foi auditada quanto a conteúdo em 2026-09-06: cada afirmação factual tem vínculo verificado (G1→G2→G3) ou está sinalizada como parcial/pré-clínica. `validar_auditoria.py` e `gate_script.py` no resultado final. **Pendência P-6:** 2ª verificação independente (avaliador cego).


## Atualização GPM2 (2026-09-06)
- Adicionadas 7 refs (total 35): Bodenstein 2019 (mtDNA bipolar pós-morte), Clay/Sillivan/Konradi 2011 (revisão bipolar), Giménez-Palomo 2024 (fase maníaca), Kuang/Duong/Jeong 2018 (lactato bipolar), Kato/Kunugi 2000 (polimorfismo 5178 mtDNA), Misiewicz 2019 (multi-ômica ansiedade), Einat/Yuan/Manji 2005 (animal ansiedade).
- Rejeitados por falso-positivo: McManus (válvula aórtica), Wang 2022 (dieta) — sinalizados P-6, não forjados.
- Ledger: Counter({'APROVADO': 35}).


---

## Rodada [AT] 2026-09-09 — reconciliação de insumo externo (P-7) → V2 (35→111 refs)

**Insumos:** GPM oficial molde v2.0 (47 âncoras com PMIDs; 12 regras fundadoras; inventário negativo
×10; fenótipos F1–F7; submecanismos B9.1–B9.7) + briefing de rodada 0 + briefing científico +
anexo de artigos (**165 entradas reais — o briefing dizia 152; exposto**) + matriz ChatGPT
(7 submecanismos; defesa de manter o MR negativo de Lu 2024).

**Auditoria ref a ref (ciência primeiro, engenharia depois):**
- Parse do anexo real: 165 itens (164 com DOI + 1 preprint).
- **G1 (eutils esearch DOI[aid] + esummary + efetch): 161/161 resolvidos · 0 falso positivo ·
  4 não-indexados confirmados fora** — Heyat 2024 (s40747), Nunes 2025 (clinbioenerg), Niu 2024
  (preprint medRxiv), Giménez-Palomo 2023 (Eur Psychiatry; busca dirigida sem match). Nenhuma
  fonte forjada; sem fonte = `[G1]`.
- 13 alertas de metadado: diacríticos, anos epub-vs-print (anos canônicos = impressão, regra 10)
  e 2 relabels reais; sobreposição com a V1 = 10; fila de decisão = 151.
- **Matriz final: 76 ENTRA / 69 BAIXO / 6 EXC** — usuário aprovou "completo (76)".

**Fragilidades do briefing externo revertidas (7):**
1. "Lu 2024 MR não resolvido" → **resolvido** (J Affect Disord) — MR bidirecional **NULO** para
   mtDNA-CN × TDM/ansiedade/bipolar/esquizofrenia/TOC e reversos; sinal potencial apenas para TEA
   (fora do escopo) — âncora da regra fundadora 3.
2. "Triebelhorn 2024 não localizado" → **é o mesmo registro já citado como pendente** (Mol
   Psychiatry, impressão 2024; o GPM o trata como "2021").
3. "Mańczak 2010" → o estudo real é **Reddy 2011** (Mańczak é coautora) — coberto na auditoria.
4. "Li 2018" → o estudo real é **Wang 2018** (BMC Psychiatry, bipolar mtDNAcn) — ficou BAIXO.
5. Scaini vigente tem **impressão 2022** — o ID REF_SCAINI_2021 foi mantido (regra 10).
6. Anos de impressão corrigidos: Burté 2015, Chandhok 2018, Culmsee 2018, Feng 2020, Lagos 2026,
   Mafikandi 2025, Palma 2024, Triebelhorn 2024.
7. **10 itens do anexo fora de §3∪§6** (Reddy 2011, Rovira 2017, El-Hattab 2018, Ľupták 2019,
   Kolár 2021, Giménez-Palomo 2021, Valiente-Pallejà 2022, Büttiker 2022, Ciubuc-Batcu 2024,
   Timón-Gómez 2026) — cobertos pela auditoria (2 ENTRA, demais BAIXO/vigente).

**Fusão V2:** 35 → **111 refs** (35 vigentes + 76 ENTRA: 43 masters GPM + Lu 2024 resgatado +
32 extras auditados). Inserções em §1.1 (células humanas), §1.2 (mecânica da dinâmica), §1.5
(ROS = sinal), §1.6 (mitofagia/UPRmt), §1.7 (mito-inflamação), §1.8 (cadeia causal animal +
ansiedade social), §1.9 (MAO→respiração), §1.10 (fronteira/integradores), **§2.5 novo** (mtDNA
sob quatro lentes — regra 2), BLOCO_03 (mediadores + inventário negativo), BLOCO_05 (+ detalhe),
BLOCO_07 (item 7 — genética ≠ causalidade), BLOCO_08 (mtDNA×PCR, MAO-A, Mito-Mood `[G1]`),
BLOCO_11 (fenótipos F1–F7 operacionais), BLOCO_12 (3 cenários novos), TABELA (+6 linhas),
CONTROVÉRSIAS (**12 regras fundadoras B9 + inventário negativo ×10 fixados**), MARCADORES,
METADADOS, listras-resumo e APÊNDICE. Prosa sem PMID/DOI (varredura 7–9 dígitos = 0);
`[[AT 2026-09-09]]` ×13.

**Tríade sincronizada:** pmids 111 (= vínculos N2 111 = ledger 111); trechos-âncora literais
presentes na V2 (assert de contagem 1); vínculos VINC_B9_036–111; ledger AUD_B9_0036–0111
(vocabulário oficial: natureza contributiva/associativa/nao_estabelecida; maturidade
bem_suportado/moderadamente_suportado/emergente; acao MANTER/ADICIONAR_SINALIZADOR;
origem_entrada GPM; `verification_status` emergente/preclinico — sem promoção automática G1→G3).

**Portões oficiais (todos verdes):** gate P-5 **APROVADO (conteúdo)**; framework de auditoria
**0 ERRO** (35 avisos não-bloqueantes de legado V1 — padrão de listra descritiva, ressalva de
fase); checklist de entrega **41/41 itens OK | 0 FALHA**.

**Hierarquia de leitura preservada:** defeito real (funcional + pós-morte), causalidade animal
[ML]/[EXTRAPOLAÇÃO POR ANALOGIA] (Dong 2023; Gebara 2020; Hollis 2015; Rosenberg 2023; Watanabe
2022; Xie 2020), terapêutica experimental só como sinal (Javani 2022; Mafikandi 2025; Tian 2026)
— nunca recomendação (P20). Mutação/heteroplasmia e exames mitocondriais sem ID no C-LAB ficam
como papel biológico, sem marcador diagnóstico (P19).

**Pendência P-6 (não autocertificável):** a 2ª verificação **cega e independente** permanece
PENDENTE — AMPLIADA nesta rodada: cobrirá as levas [AT] de todas as bibliotecas B1–B16 ao fim
da rodada (16/16), incluindo os claims de alto risco novos desta V2 (MR Lu 2024; Xue 2026; ccf-
mtDNA Lindqvist 2018 + SR Fernández-Pech 2026; UPRmt Hofstra 2024; cadeia Dong 2023; fenótipos).
