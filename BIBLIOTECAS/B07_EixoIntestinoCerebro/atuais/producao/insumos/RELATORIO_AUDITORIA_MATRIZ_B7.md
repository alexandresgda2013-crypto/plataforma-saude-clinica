# RELATÓRIO DE AUDITORIA — Insumos externos B7 (Eixo Intestino–Cérebro)
**Data:** 2026-09-09 · **Alvo:** B7 V1 (85 refs vigentes) → proposta V2
**Insumos auditados (5):** `GPM_B7_EixoIntestinoCerebro.md` (oficial da rodada) + `BRIEFING_B7_EIXO_INTESTINO_CEREBRO_RODADA0.md` + `BRIEFING_CONSOLIDADO_B7_v1.md` (rodada 0) + `Artigos cientificos do mecanismo B7 eixo intestino cérebro.md` (anexo de citações) + `Resumo do insumo para B7 Chatgpt.md` (matriz 34 claims B7.SM02.001–034 + 3 regras de ouro)
**Regra aplicada:** auditoria ref a ref **antes** de qualquer fusão; nada entra sem resolver no PubMed (G1 = eutils esearch DOI[aid] → esummary → efetch abstract).

---

## 1. Números reais vs. números do briefing (incongruências expostas)

| Item | Briefing dizia | Auditado | Ambos certos? |
|---|---|---|---|
| Refs no anexo | "178" | **196 DOIs únicos + 1 sem DOI (Carabotti)** = 197 itens | ❌ subcontagem do briefing (exposta, sem impacto: tudo foi resolvido igualmente) |
| Tabela-mestra | texto: "31 âncoras" | tabela: **30** | ❌ inconsistência menor interna do GPM; auditadas 30/30 |
| Masters já na V1 | não informado | **7 das 30 masters já vigentes** (Braniste/Cryan/Socała/Góralczyk + Bonaz/Hwang/Margolis — as 3 "fora do anexo" do briefing já estavam dentro da V1) | masters realmente novas = **23** |
| Overlap anexo ∩ V1 | não informado | **8 refs** (as 7 masters acima + Kennedy 2017) | fila real = 196+1−8−... ajustada: **188 itens únicos por PMID** |
| §5 NÃO-INDEXADOS | Thomas 2021 (bioRxiv), Towriss 2026 (preprint), Xia 2025, Zhang 2026 | **confirmados 4/4 como não resolvíveis** em DOI[aid]/esummary | ✅ briefing correto |
| Conferência rótulo autor/ano/tema | — | **0 falsos positivos**; 8 alertas de forma (Bărcuțean→Barcutean, Lukić→Lukic, Joly Condette, De Palma, "Mei 2025"→Chenghan M, Tulkens 2018/2020, parser "Q. 2019"→Ma Q, von Buchholz) — todos falso-alarme de grafia/parse | ✅ |
| Carabotti 2015 | sem DOI | resgatada por busca dirigida = PMID 25830558 (conforme §4.4 do briefing, revalidado) | ✅ |
| PMIDs §4 (Chen 2024 ×2, Zhao 2023 ×2, Socała) | — | confirmados: 38939042 citado (39408347 também consta no anexo, decidido BAIXO por ser cienciométrica); 36776388 citado (36758839 também no anexo, decidido BAIXO — mesmo grupo/pergunta da master); Socała 34450312 = já vigente | ✅ |

## 2. G1 (resolução PubMed)
- 196/196 DOIs processados → **192 resolvidos · 4 NÃO-INDEXADOS** (exatamente o §5 do briefing: Thomas/Towriss preprints; Xia/Zhang periódicos não indexados) → permanecem **fora**; se a ciência amadurecer, entram como `[G1]` declarado, nunca com PMID inventado.
- Abstracts efetched: 196 · **2 sem abstract no PubMed**: Tulkens 2020 (Gut, letter+research) e Akiba 2021 (editorial, Dig Dis Sci) → tratados por G3 (título/periódico/autor) quando usados.

## 3. Matriz ChatGPT (34 claims + regras de ouro) — papel na fusão
- As **3 regras de ouro** serão fixadas verbatim em CONTROVÉRSIAS/REGRAS da canônica:
  - **B7-CAUSAL-01:** sem ponte funcional intestino→cérebro, correlação de composição ≠ mecanismo causal.
  - **B7-CAUSAL-02:** metabólito administrado/rastreado exogenamente ⇒ claim permitido é **metabólito→cérebro**, não microbiota→cérebro (guarda-case Sathyasaikumar/IPrA; Schwarcz in vitro).
  - **B7-CAUSAL-03:** associação microbiota↔depressão humana permanece **ASSOCIATIVE** (claims .028/.031/.032 deliberadamente associativos).
- Formulações específicas preservadas: **Erny 2021** = "microbiota → acetato → aptidão metabólica/maturação microglial → função" (proibido reduzir a "AGCC é anti-inflamatório"); **Chen N 2024** = cadeia exata **AGCC cerebral → ACSS2 → PPARγ → TPH2 → serotonina → comportamento** com knockdown neuronal de ACSS2 abolindo o efeito — **proibido escrever a cadeia clínica completa em humano** (é roedor); GF/germ-free ⇒ `[APENAS PRÉ-CLÍNICO]`/extrapolação por analogia obrigatória.

## 4. Decisão ref a ref (fila real: 188 itens únicos por PMID)

### 4.1 ENTRA — 31 (23 masters GPM novas + 8 não-masters com seta causal ausente)
Masters (23): Aburto & Cryan 2024 · Agus 2018 · Barki 2022 · Bosi 2020 · Caetano-Silva 2023 · Carabotti 2015 · Chen LM 2021 · Chen N 2024 · Cheng 2024 · Erny 2021 · Guo 2013 · Guo 2015 · Kurita 2020 · Li CC 2023 · Lin 2023 (ASSOCIATIVE) · Nighot 2017 · Nighot 2019 · Saikachain 2023 · Sathyasaikumar 2024 (guarda) · Schwarcz 2024 (guarda) · Spichak 2021 · Zhao 2022 · Zhou 2023.

Não-masters (8), cada uma com janela que a V1 + masters não cobrem:
1. **Tulkens 2020** (Gut) — janela **humana** de translocação: EVs bacterianas LPS+ sistêmicas ↑ em disfunção de barreira (claim ASSOCIATIVO; sem abstract → G3).
2. **Nøhr 2013** (Endocrinology) — mapa FFAR3/FFAR2 em células EEC (GLP-1/PYY/CCK/GIP) e neurônios entéricos: o "sensor" intestinal de AGCC (elo metabólito→receptor→via neural).
3. **Chenghan 2025** (Ann N Y Acad Sci) — antibióticos orais perturbam BBB; AGCC restauram integridade, **em macaco rhesus e camundongo** (janela translacional BBB×AGCC; [APENAS PRÉ-CLÍNICO]).
4. **Kuo 2021** (Gastroenterology) — **ZO-1 dispensável para barreira, crítico para reparo**: afia o ceticismo da V1 sobre ZO-1 como "marcador de barreira" (elementos moleculares).
5. **Stanimirov 2025** — única revisão dedicada **sais biliares↔eixo** (FXR/TGR5); ancora mecanisticamente a §2.6.
6. **Ohara 2025** (Nat Rev Microbiol) — **sinalização neuroepitelial** no eixo (neuropods/EEC): janela ausente na V1.
7. **Baj 2019** — única revisão dedicada ao **glutamato** no eixo (elo B5).
8. **Zhang Q 2025** (J Affect Disord) — humano TDM (N=86×120): multiômica microbiota+KYN+inflamação × cognição (**ASSOCIATIVE** por B7-CAUSAL-03).

### 4.2 EXC — 26 (malha de escopo da série, expostos)
Pecuária/veterinária (5): galinhas DON (35367310), IPEC-J2/porcos (25888437, 29705796, 35736894), BMC Vet Res betaina (32131830).
Alzheimer (4): 32829453, 32583667, 35855330, 36757399, 39833898 → (5 com Akkermansia AD).
Neurodegenerativos gerais (4): 42245509, 41798063, 37960284, 38360862.
Parkinson (3): 33905875, 38377788, 39904963.
EM/EAE/autoimune (3): 38542172, 31222050, 37264394.
Epilepsia/TCE (2): 34707612, 33893636.
AVC (3): 35420913, 41155363, 40723792.
Autismo (1): 41010510.

### 4.3 BAIXO — 131 (redundância auditada, por família)
| n | Família |
|---|---|
| 17 | Revisões gerais de AGCC (imunidade/metabolismo/doenças) — núcleo AGCC→cérebro coberto por masters Erny/Spichak/Caetano-Silva/Barki/Cheng |
| 17 | Revisões gerais triptofano/quinurenina — arquitetura coberta por masters Agus/Bosi/Schwarcz/Sathyasaikumar + §2.5 da V1 |
| 16 | Revisões narrativas genéricas do eixo (2016–2026) — cobertas por Cryan/Bonaz/Margolis vigentes + Aburto 2024 |
| 13 | Barreira intestinal + agente isolado (clorpirifós, vitamina A, acroleína, orexina, daidzeína, catalpol, zinco, antibiótico→NLRP3, NEC, patógenos…) — seta LPS→TJ coberta pelas masters Guo×2/Nighot×2 |
| 8 | Biologia de tight junctions (reviews TJ, claudinas, sepse-barreira TJ) — mesma cobertura |
| 7 | Doença-órgão não psiquiátrica (cirrose, DRC, insuficiência cardíaca, endotélio) — tangencial |
| 6 | Sepse (inclui autópsia Erikson) + editorial Akiba — fora do miolo |
| 5+4 | Primários AGCC periféricos/imunes/metabólicos (Lin HV 2012 obesidade, Kibbie 2021 CD4, Roseburia-HDAC…) — sem ponte SNC |
| 6 | Obesidade/metabolismo energético (Luo, Ikeda, He J…) — confundidor V1 12.x |
| demais | Casos únicos justificados individualmente na matriz (Leclercq AUD, Zhao 36758839 redundante da master, Ramos-Chávez KYNA cerebral, O'Mahony 2015, De Palma 2014, Morais 2021, Chen X 2024 cienciométrica, Kumara… ver `matriz_b7_decisao.json`) |

**Critério global:** regras B7-CAUSAL-01/02/03 + malha de escopo da série (TCE/AVC/Alzheimer/Parkinson/EM/epilepsia/autismo/pecuária excluídos) + "ciência em primeiro lugar": nenhuma primária mecanística com seta causal **nova** e fechada ficou de fora; nenhuma revisão entra só por ser recente.

## 5. Pendências e selos
- NAO-IDX (4): Thomas 2021, Towriss 2026, Xia 2025, Zhang 2026 → monitorar; `[G1]` se citados.
- Sem abstract: Tulkens (ENTRA via G3), Akiba (BAIXO).
- Kurita 2020 é master em contexto de isquemia experimental: entra pela seta **endotoxemia→neuroinflamação**; a isquemia é apenas o modelo — redação sem transformar AVC em escopo.
- Todo germ-free/roedor ⇒ `[APENAS PRÉ-CLÍNICO]` + extrapolação por analogia; masters humanos (Lin, Zhou-parte humana, Zhang Q, Tulkens) ⇒ ASSOCIATIVE.
- **P-6 Via 2** (2ª verificação cega B1–B16): PENDENTE ao fim da rodada — será redeclarada em todos os artefatos da V2.

## 6. Artefatos
- `producao/insumos/b7_anexo_entries.json` (196 entradas)
- `producao/insumos/matriz_b7_g1.json` (G1 completo: 192 ok, 4 NAO-IDX, 4 buscas dirigidas, 196 abstracts)
- `producao/insumos/b7_fila_real.json` (cruzamento anexo×V1: overlap 8; fila 188)
- `producao/insumos/matriz_b7_decisao.json` (decisão ref a ref: 31/26/131, todos com motivo)
