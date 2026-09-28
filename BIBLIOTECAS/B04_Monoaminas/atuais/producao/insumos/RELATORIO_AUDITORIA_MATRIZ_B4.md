# RELATÓRIO DE AUDITORIA — INSUMO EXTERNO B4 ("Matriz B4 — Deficiência de Monoaminas")
**Rodada [AT] 2026-09-08 · Pipeline P-7 (auditoria ref a ref, G1 eutils) · Status: AUDITORIA CONCLUÍDA, aguardando decisão do usuário**

## 1. Insumo recebido
- Consolidação colada (outro modelo): "esqueleto" de 25 refs + eixos (hipótese clássica vs. evidência contemporânea; depleção; DA→anedonia; NE→LC; modelo de circuitos), EXC/HOLD e correções bibliográficas.
- Anexo Consensus `Artigos cientificos do mecanismo B4 Deficiencias monoaminas.md`: **177 referências** (172 com DOI; 4 sem DOI + título, 1 = Kayabaşı).
- Briefing "BRIEFING CONSOLIDADO B4 v1": tabela-semente 14 refs + Vetulani & Sulser 1975 "PMID a confirmar".

## 2. Execução G1 (eutils)
- esearch `"DOI"[aid]` ×172 → **153 na 1ª passada**; **resgate de DOIs antigos com parênteses** (PII) + busca autor/título → **+8** (Berman, Berridge & Waterhouse 2003, Kahn 1988, Meltzer 1989, Moore 2000, Owens & Nemeroff 1994, Salomon 1997, Takahashi 1975).
- Busca dedicada dos 6 pendentes: **Vetulani & Sulser 1975 = 170534** (já vigente na B4 ✓); **Heninger 1996 = 8852528** (novo, modulatory role); **Charney 1998 = 9818625**; **Hirschfeld 2000 = 10775017**; **Leonard 2000 = 10775019**; **Kayabaşı 2021 não localizado** → sinalizado [G1].
- Esummaries/efetch abstracts arquivados (`matriz_b4_g1_full.json`, universo único = 177 PMIDs).

## 3. Veredito global
**INSUMO LIMPO — ZERO falsos positivos de identidade.** Todas as correções declaradas pela consolidação foram verificadas como **corretas**: Tillage = artigo publicado (PMID 33911187, NPP 2021 — não preprint); Liu 2023 = medRxiv (HOLD, não entra); Neumeister "2025" = **republicação** (original 2003 = PMID 15131521); Schildkraut 1965 (5319766) e 1967 (4863731) = registros distintos ✓; Vetulani & Sulser 1975 = 170534 cravado (pendência do briefing RESOLVIDA — e já consta na B4).

## 4. Divergências de rótulo no ANEXO
28 divergências = quase todas defasagem de ano (online-first). **2 divergências de AUTORIA reais** (artigos válidos):
1. "Martinez 2010" (`10.1002/da.20642`) → **Goddard AW 2010** — "Current perspectives... central norepinephrine system in anxiety and depression".
2. "Ogden 2006" (`10.1016/j.biopsych.2005.06.016`) → **Parsey RV 2006** — 5-HT1A [carbonyl-11C]WAY100635 PET em TDM.

## 5. Já cobertos pela B4 vigente (12; não duplicar)
Schildkraut 1965 · Coppen 1967 · Lesch 1996 · Caspi 2003 · Risch 2009 · Ruhé 2007 · Meyer 2006 · Morris 2020 · Yano 2015 · Moncrieff 2023 · Jauhar 2023 · Vetulani & Sulser 1975.

## 6. Não-resolvidos / excluídos da forma (12)
Alawie (periódico não indexado), Cosci & Chouinard (livro), Fassler (resumo FASEB), Hasler (resumo ECP), Isingrini (bioRxiv), Kovalzon (IntechOpen), Li J (SPIE), **Liu 2023 (medRxiv → HOLD consistente com a consolidação)**, Nakamura (IntechOpen), Neumeister 2025 (republicação → usa-se o original), O'Leary 2020 (capítulo), Kayabaşı (sem registro PubMed → [G1]).

## 7. EXC por escopo (13, verificados por título/MESH/abstract)
Parkinson (Costello), Alzheimer (Tahiri), modelo APP/ascorbato (Consoli), **dor ×3** (Markovic; Ji; Suárez-Pereira), **TEPT ×4** (Naegeli — divergência explícita vs. consolidação —, Nwokafor — idem —, Strawn, McCall militar), anorexia (Weinert 2023), fitoquímicos como intervenção (Naoi — divergência registrada vs. "SUP" da consolidação; regra P20/sondas), artigo em japonês sem tratamento viável (Mouri).
**+ 57 de baixo incremento/redundância** (revisões genéricas sobrepostas, modelos animais de nicho, adjacências de outros mecanismos — quinurenina/glutamato TRD/vitamina D/insulina — e redundâncias da onda LC-NE). Lista completa: `matriz_b4_decisao.json`.

## 8. ENTRANTES APROVADOS: **95** (37 → 132 refs)
- **Esqueleto consolidação verificado (27):** Baumeister 12953623 [CONT-HIST] · Berman 11922881 [NEG] · Bell 11331552 · Moore 11063917 [METH/CONT] · Booij 12431859 [METH] · Cowen 26043325 [CONT] · Albert&Blier 37857415 · Page 38816586 [FRONT] · Argyropoulos 15450786 [RCT-CORE] · Schopman 33574223 [NEG/META] · Bîlc 37430145 [NEG] · Strawbridge 36000248 [NEG/META-reserpina] · Wang 27623971 [MA 5-HT1A] · Savitz 19428959 · Moriya 32363761 [PET DAT↓NAc] · **Peciña 28870407 [PET D2/3↑ — direção invertida]** · Phillips 37301129 [anedonia PET/fMRI] · Felger&Treadway 27480574 [B1↔B4] · **Bekhbat 39694342 [L-DOPA×inflamação — fenótipo]** · Nestler&Carlezon 16566899 · Slavova 39427811 · Mir 41167443 · Korukonda 42332025 [FRONT 2026] · Tillage 33911187 [NE+galanina] · Neumeister 15131521 (original) · Schildkraut 4863731 (registro 1967) · Treadway&Zald 20603146.
- **Pendentes cravados (4):** Heninger 1996 (8852528, modelo modulatório), Charney 1998, Hirschfeld 2000, Leonard 2000 (história/contestação).
- **Eixo 5-HT/receptores (18):** Parsey 16154547 · Hirvonen 17971260 · Albert 2014 (24936175) · Garcia-García 24337875 · Akimova 19423077 · Popova 23492554 · Nautiyal 28232871 / 27353308 · Fakhoury 25823514 · Pourhamzeh 33651238 · Villas-Boas 33673205 · Borroto-Escuela 33672070/28920103 · Żmudzka 30144453 · Steinberg 31120232 · Heisler 9844013 · Mosienko 22832966 · **Frick 26083190 [PET 5-HT ansiedade social — humano]**.
- **Depleção — reforços (5):** Booij 2003 (14647394) · Hughes 14731308 · McLean 12955284 · **Salomon 1997 (8988796) [NEG: sem efeito em saudáveis]** · Kahn 3275471 [desafio pânico 5-HTP].
- **Eixo NE/LC (23):** Goddard 19960531 · Berridge&Waterhouse 12668290 · Valentino 18255055 · Itoi 20210846 · Borodovitsyna 28596922/29341884 · Bangasser 26607253 · Atzori 27616990 · McCall 26212712/28708061 · Maletic 28367128 · Zhang H 36289638 · Songtachalert 30430940 · Bouras 37139472 · Giustino 29593511/31801809 · Fernandes 40442382 · Reyes 40219735 · Scroger 41225565 · Toyoda 41066175 · Soares AR 41000807 · Zhang Q 38155473 · Dos-Santos 41938091.
- **Eixo DA/anedonia/circuito (9):** Szczypiński 29573379 · Belujon 29106542 · Knowland 29309799 · Heshmati 26525751 · **Salamone 26323245 [esforço≠"pouca dopamina"]** · Shirayama 18654637 · Wang S 33631251 · Jiang 36889362 · Trifilieff 23711983.
- **Interfaces/história/modelo contemporâneo (9):** Evans 39696597 · Lucido 34285088 · Hersey 34265868 · Liu B 29033793 · Boku 28926161 · Dale 25813654 · Carmellini 42198336 · Meltzer 7899535 · Owens&Nemeroff 19498050.

## 9. Regras de leitura [AT] incorporadas (da consolidação, com aderência verificada)
1. **"Depressão = deficiência de monoamina" NÃO entra como fato** — Moncrieff/Jauhar (vigentes) como disputa ativa, sem lado escolhido; B4.23 evidência negativa é estrutural, não rodapé.
2. **5-HT ≠ receptor 5-HT ≠ SERT ≠ síntese ≠ liberação ≠ circuito** (Wang 2016; Akimova; Parsey).
3. **Depleção ≠ indução universal de depressão** (salvos gating: remissão recente com ISRS/SSA; Berman/Salomon/Bîlc/Schopman negativos preservados).
4. **DA: não é "pouca dopamina"** — direção pode ser ↑ (Peciña), e anedonia = liberação tarefa-ligada (Phillips), esforço (Salamone), fenótipo inflamatório (Bekhbat).
5. **LC-NE é dinâmico/estado-dependente/heterogêneo** (Morris vigente + onda 2024-2026).
6. Eficácia dos ISRS ≠ prova do mecanismo causal; TEPT/TCE/AVE/Alzheimer/dor/anorexia/Parkinson fora; fitoquímicos sem sonda de alvo fora (P20).

## 10. Pendências
- Kayabaşı 2021 sem registro → `[G1: a cravar]`; Liu 2023 = HOLD até publicação final; Mouri = tratamento bibliográfico separado.
- G3 declarado = IA; **P-6 (2ª verificação cega) permanece PENDENTE** (pacote Via 2 B1–B5+).

*Auditoria conforme Bloco P-7 do Processo v2.1: nada entrou sem resolver no PubMed; falsos positivos e rejeições expostos.*
