# RELATÓRIO DE AUDITORIA — INSUMO EXTERNO B3 ("MATRIZ CANÔNICA B3 — Neuroplasticidade")
**Rodada [AT] 2026-09-08 · Pipeline P-7 (auditoria ref a ref, G1 eutils) · Status: EXECUTADO (aprovado pelo usuário: "aplicar agora — 112 refs")**

> **EXECUÇÃO (2026-09-08):** V1→V2 rotacionada (histórico em `producao/historico/v1_canonica_2026-09-08.md`); 112 refs incorporadas (53→165); prosa [AT] em 14 submódulos/grupos + 2 novos submódulos (1.6, 5.4) + bloco síntese BLOCO_03/08 + B3.C01–C20 como regras de leitura; JSONs 01_pmids/vínculos/ledger = 165 cada; manifesto+trilha P-7 gravados; **portões: gate P-5 APROVADO (165|165) · framework 0 ERRO · checklist 41/41 · P-4 adendo V2 revalidado · decisoes_B3 atualizado.** P-6 (2ª verificação cega) permanece PENDENTE (pacote Via 2 com B1/B2).

## 1. Insumo recebido
- Texto colado "B3 — Consolidação Canônica" (outro modelo): camadas CORE/SUPPORT/NEG-CONT/FRONT-SUP, 3 falsasExpectativas, claims B3.C01–C20, EXC e correções bibliográficas declaradas; 58 PMIDs citados.
- Anexo `Artigos cientificos do mecanismo B3 Neuroplasticidade.md` (Consensus): **193 referências**, todas com DOI único.

## 2. Execução G1 (eutils)
- esearch `"DOI"[aid]` ×193 → **185 resolvidos (95,9%)**, **8 não resolvidos**; esummary 194 PMIDs; efetch abstracts (194) arquivados.
- Cruzamento com a B3 vigente (53 refs).

## 3. Veredito global
**INSUMO LIMPO — ZERO falsos positivos de identidade** (todo identificador resolve o artigo certo; nenhum PMID/DOI aponta para artigo alheio ao tema). As 20 claims B3.C01–C20 são convergentes com a arquitetura da B3 vigente ("plasticidade não-uniforme dependente de região/contexto"; BDNF periférico ≠ biomarcador; mTOR ≠ sinônimo de plasticidade) e não trazem doses/posologia (P20 OK).

## 4. Falsos positivos / rótulos divergentes
- **0 FPs.** 34 divergências são quase todas **defasagem de ano** (online-first vs impressão; ex.: Appelbaum 2022→2023, McEwen 2011→2012) — correção catalográfica, não altera mérito.
- **3 divergências de AUTORIA no ANEXO** (artigos válidos, rótulo errado; corrigir na geração):
  1. "Schofield 2009" (`10.1038/mp.2008.143`) → **Gatt JM 2009** (PMID 19153574) — a Consolidação já o citava corretamente.
  2. "Pich 2018" (`10.1038/mp.2017.241`) → **Cavalleri L 2018** (PMID 29158584).
  3. "Zhang 2018" (`10.1038/mp.2017.239`) → **Yao N 2018** (PMID 29158578).

## 5. 8 não-resolvidos (justificativa)
| DOI | Item | Motivo | Destino |
|---|---|---|---|
| 10.1016/S0079-6123(07)… | Bremner et al. 2007 (capítulo) | não indexado; substituto da Consolidação (18037014) é TEPT-específico | **EXC (TEPT)** |
| 10.33612/diss.1479578477 | De Jager 2026 | dissertação | EXC |
| 10.54254/2753-8818/2024.19967 | Gao 2025 | periódico não indexado | EXC |
| 10.1101/330688 | Glasgow | pré-print bioRxiv | EXC |
| 10.48550/arXiv.1711.09536 | Singh & Karkare | pré-print arXiv | EXC |
| 10.1101/2024.05.01.592099 | Storey (pré-print) | **substituído pela versão publicada PMID 39562042** ✔ (Consolidação correta) | entra como 39562042 |
| 10.1192/j.eurpsy.2023.71 | Vestring | resumo de congresso | EXC |
| 10.1101/2025.07.28.667139 | Yong 2025 | pré-print bioRxiv | EXC |

## 6. Já cobertos pela B3 vigente (não entram)
20724638 (Li 2010) · 21677641 (Autry 2011) · 23534055 (Kavalali 2012) · 27144355 (Zanos 2016) · 36194941 (Meshkat 2022, meta TRD-BDNF).

## 7. Erratas da Consolidação (rejeitadas como refs independentes)
34880451 (erratum de Yao 34819637) e 35364073 (corrigendum de Robinson 34298123) — metadados dos artigos já selecionados, não constituem referências próprias (unicidade Módulo 09).

## 8. Correções bibliográficas da Consolidação — VERIFICADAS
- Youssef 2018 = PMID 29432620 ✔ (autor/ano conferem).
- Storey 2025 = PMID 39562042 ✔ (Art. J Neurosci publicado substitui o pré-print).
- Brown 2026 = PMID 41633835 ✔ (time-sensitive plasticity, racetamina×(2R,6R)-HNK).
- "Z., Z., Guzikowski…" = **Ma ZZ et al., Science 2025, PMID 40339008, DOI 10.1126/science.abb6748** ✔ — conferido (ERK/DUSP6, potenciação CA3-CA1).
- "Zhang 2016, PMID ?" (BDNF-TrkB×inflamação) → **cravado: Zhang JC 2016, PMID 26786147** ✔ (MESH Depressive Disorder+Inflammation+BDNF).

## 9. Divergências minhas vs. Consolidação (escopo)
1. **Bremner 2008 (18037014)** — a Consolidação o incluiu como núcleo; **eu REJEITO**: título/abstract são TEPT-específicos; regra permanente TEPT≠depressão≠ansiedade. Idem He 2018 (30457048) e López-López 2025 (40767105).
2. **Thomazeau 2021 (32606374)** — não incluído: modelo **Fmr1-KO (Fragile X)**, fora de escopo.
3. **Jiang 2025 (40817330)** — não incluído: acoplamento estrutura-função temporal, sem vínculo com depressão.
4. **Mitrovic 2025 (40430064)** — não incluído: proBDNF/apoptose em contexto de doenças neurodegenerativas.
5. Consolidação ignorou 12 itens in-scope que **eu incluo por auditoria própria** (ex.: Mizui 2015 pró-peptídeo×Val66Met, Schmidt 2010 BDNF periférico, Sha 2023 plasticidade na ansiedade, Brown KA 2024 metaplasticidade, Izumi 2022 N₂O, Aguilar-Valles 2026 DCC).

## 10. EXC por escopo (33) — cada um verificado por título/MESH/abstract
esclerose múltipla (Al-Kuraishy 39654365); anorexia (Cao 39203753); Alzheimer (Liu F 42488724; Numakawa 34071978; Pláteník 24334212); dor (Mazzitelli 40214430); neurodegeneração (Weerasinghe 35328770; Basha 42136057; Numakawa 41596628; Mitrovic 40430064); Fragile X (Banke 33343326; Thomazeau 32606374); β-amiloide (Sanderson 34610314); **TBI/TCE (Hoffman 33937912)**; **modelo pós-AVE (Abdoulaye 33981335)**; **TEPT (Bremner 18037014; He 30457048; López-López 40767105)**; editorial cardiovascular (Stein 26715164); FND (Mavroudis 42376131); indol-3-carbinol (Singh 39061415); intervenções fitoquímicas/miméticos/baicalina (Jia 34280458; Yoon 36694423; Mezhlumyan 35337082); artigo histórico (Hashimoto 31215725); meta-ciência/opinião (Mateos-Aparicio 30873009); rede genérica (Stampanoni Bassi 31817968); redundâncias pontuais (37781095, 36291261, 29516301, 29736744, 36158555, 40817330).
**+ 42 de baixo incremento/redundância** (plasticidade básica sem vínculo doença: GRIP1, STEP61, AIDA-1, cortactina, palmitoilação, subunidades GluN2 genéricas etc.; neurogênese-estrutural → escopo B16 per P16: Shridhar 35561083, Numakawa 30463271; didático EMT Brown JC 35088731). Lista completa em `matriz_b3_decisao.json`.

## 11. ENTRANTES APROVADOS NA AUDITORIA: **112** (53→165 refs)
- **Núcleo da Consolidação verificado (51)**: Nissen 20655508 · Kishi 29387021 · Arosio 33643008 · Castrén 34053675 · Appelbaum 35810199 · Tartt 35354926 · Youssef 29432620 · Gatt 19153574 · Yu H 22442074 · Tian 33053385 · Notaras 31900428 · Robinson 34298123 · Lu 35995236 · Yao W 34819637 · Chen 39116252 · Liao 39558048 · O'Donnell 41620807 · Rygvold 35601905 · Höflich 33795646 · Kailainathan 26687096 · Anastasia 24048383 · Pagliusi 35722560 · Duman 21907221/30894661 · Kang 35546951 · He 37124348 · Wang YT 35074585 · Elmeseiny 38278430 · Lin 34407417 · Suzuki 34731624 · Wu M 33637303 · Zaytseva 37358072 · Zanos&Gould 29532791 · Bottemanne 37793581 · Brown 40097740/41633835 · Calder 39613915 · Storey 39562042 · Arefin 42066082 · Prabakar 42287566 · Bulek 41526004 · Pittenger 17851537 · McEwen 26076834/21807003 · Forrest 29545546 · Treccani 31037646 · Pryazhnikov 29691465 · Algaidi 39864644 · Parrott 34601342 · Ma ZZ 40339008 · Zhang JC 26786147.
- **SUPPORT/METH nomeados pela Consolidação §8, resolvidos por mim (11)**: Sanderson ×3 (23100425, 26938443, 29440558) · Diering 2014 (25451194) · Diering&Huganir 2018 (30359599) · Fernández-Monreal 2012 (22993436) · Peng 2009/2010 (19489005) · Sumi&Harada 2020 (32895399)/2023 (36866246) · Soares 2013 (23946413) · Yong 2020 (32071234).
- **Adicionais in-scope aprovados na auditoria (50)**: Christoffel 21967517 · Marsden 23268191 · Leuner 22522470 · Chattarji 26404711 · Wilson 26844236 · Liu W 28246558 · Lau 27240534 · Notaras 28926000 · Price 31801966 · Luscher 32616214 · Aleksandrova 34565579 · Wu H 34016377 · Hess 34968492 · Zanos 36596696 · Wei 33963284 · Parekh 35508195 · Kim 36907686 · Sha 37435365 · Krystal 37488280 · Benatti 39457754 · Brown KA 38177353 · Comai 39770460 · Numakawa 38338875 · Shi 38687826 · Carmellini 41594739 · Kavalali 39343821 · Lugenbühl 39368530 · Ren 40545507 · Aguilar-Valles 41659277 · Izumi 36050137 · Laham 35145379 · Schmidt 20686454 · Kozisek 17949819 · Miller OH 25340958 · Phoumthipphavong 27066532 · Nikolac Perkovic 37038358 · Moya-Alvarado 36826992 · Alsalloum 37761014 · Yao N 29158578 · Cavalleri 29158584 · Marshall 29507199 · Shin 32353004 · Patel 31022420 · Wang JQ 30737641 · Nikolova 29353879 · Ruggiero 34707481 · Santos 37047730 · Mizui 26015580 · Liu RJ 27634355 · Suzuki K 28640258.

## 12. Eixo de ganho previsto (V1→V2)
1. **5.1 BDNF periférico virar CONTROVÉRSIA formal** (Calder 2025 [MA negativo cetamina→BDNF sangue], Meshkat já vigente, Schmidt 2010 [EXTRAPOLADO pré-clínico], Nikolac 2023, Arosio 2021) — implementa B3.C05.
2. **Eixo cetamina multiescalar/temporal** (Kang 2022 sistemática; Kim 2023 rápido↔sustentado; HNK: Zanos, Yao N, Suzuki K, Brown 2025/2026; regionalidade Chen 2024; ERK/DUSP6 Ma ZZ 2025; fronteiras Arefin 2026, Prabakar 2026, Bulek 2026).
3. **NMDAR/AMPAR estrutural**: Storey 2025, Lin 2021, Wu M 2021, Zaytseva 2023, Suzuki 2021, Miller OH 2014, Suzuki K 2017, He 2023, Elmeseiny 2024, Wang YT 2022, Comai 2024.
4. **Plasticidade humana direta** (Nissen 2010, Rygvold 2022 [dado negativo!], Höflich 2021 [S-ketamina hipocampo RCT], Nikolova 2018, Santos 2023 [farmacogenética]).
5. **Estresse→remodelação regional** (McEwen ×2, Chattarji, Wilson, Lau, Patel, Leuner, Ren 2025, Algaidi 2025, Price 2020, Ruggiero 2021, Aguilar-Valles 2026 DCC).
6. **Val66Met/profil-domínio** (Gatt, Youssef, Yu H, Tian, Notaras 2020, Kailainathan, Anastasia, Mizui 2015).
7. **Interface inflamação↔plasticidade** (Lu 2022, Yao W 2022, Parrott 2021, Zhang JC 2016) — sem colonizar com conclusões B1.
8. **Metaplasticidade** (2.4 reforçado: Brown KA 2024, Arefin 2026).
9. **Ansiedade** (Sha 2023, Shin 2020 — cobertura antes fraca do eixo ansiedade).
10. **Claims B3.C01–C20** entram como regras de leitura/governança (sem ref própria), com ressalvas: C05 já amparado; C17 (exercício) e C19 (TRD-biomarcador) ficam como regra de prudência sem submódulo novo.

## 13. Pendências desta etapa
- 0 identificadores pendentes de validação (consolidação sem "METH_PENDING" além dos acima resolvidos).
- G3 declarado = IA (geração); **P-6 2ª verificação cega** segue PENDENTE (entrará no pacote Via 2 junto com B1/B2).

---
*Auditoria executada conforme `00_PROCESSO_DE_GERACAO_LEIA_PRIMEIRO.md` (Bloco P-7), com G1/eutils, conferência autor+ano+tema, detecção de FP, cruzamento com canônica vigente e registro de rejeições.*
