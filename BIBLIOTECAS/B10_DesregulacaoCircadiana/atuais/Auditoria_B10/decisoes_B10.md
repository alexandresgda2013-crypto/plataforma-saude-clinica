# Auditoria Científica de Conteúdo — B10 (Desregulação Circadiana)

**Data:** 2026-09-06 · **P-6** (avaliador cego) PENDENTE.

- Trechos no ledger: **39** · status: Counter({'APROVADO': 39})
- 39 âncoras G1 (autor+ano+tema vs GPM); causalidade forte animal [ML] (Clock/Bmal1-SCN/NPAS2/mPFC); humana associativa/preditiva.
- Sinalizadas P-6 sem forja: Meyer 2024 (NAc clock), Satyanarayanan 2020 (agomelatina), Mendoza 2024, Walker 2020; falso-positivo Takahashi/NLRP3 descartado.
- Bipolar = doença-relógio (nunca fundido à TDM); cronoterapia é sinal, não conduta.

---

## Rodada [AT] 2026-09-09 — reconciliação de insumo externo (P-7) → V2

**Insumos:** GPM oficial molde v2.0 (M00–M10; regra fundadora *timing* ≠ *estado*) + dossiê
RODADA0 (38 âncoras → PMID; 148 não citadas) + matriz ChatGPT RC.SM02.001–058 + anexo (193
entradas) + briefing consolidado v1 (12 sementes). **Verificação:** ref a ref por eutils
(esearch PMID + DOI[aid] + esummary + efetch; 182 candidatos; abstracts dos finalistas lidos).

**Decisões (matriz completa em `producao/insumos/matriz_b10_decisao.json`; 209 itens):**
- **ENTRA 98** — TTFL/SCN/entrada fótica 33 · HPA circadiano 17 · clínica humana 9 · genética
  genes-relógio 4 · bipolar 14 · exposição luminosa 1 · cronoterapia (sinal) 2 · causal
  experimental [ML] 5 · ponte B7 1 · sínteses 12. Cada ref com citação única na V2, trecho-âncora
  literal, ledger AUD_B10_0040–0137, vínculo VINC_B10_040–137, G1/G2/G3 preenchidos.
- **BAIXO 98** — SUP/CONTEXT/redundância/malha de escopo; nenhum descarte por contrariar tese.
- **EXC 13** — Burns 2024 (preprint medRxiv indexado — falso positivo do dossiê) + NAO-IDX
  confirmados (Burns 2022/2023; Mendoza 2024; Sandate 2020; Palagini 2023; Cao 2025; Gosztyła
  2026; Noweta 2026; You 2024; Feng 2025) + não-fontes (Rumanova; Albrecht) + duplicatas
  (Murray 2016; Takahashi 2016 cap.).

**Correções do insumo externo (auditoria própria):** 11 divergências autor/ano/PMID expostas
(p.ex. pendências do dossiê resolvidas: McGlashan 2018=30555405; Serrano-Serrano 2021=34640406);
2 sobre-correções revertidas (Palagini 2022 É REAL, 35821870; Spiga 2014 É indexada, 24944037);
15 itens do anexo omitidos pelo dossiê cobertos; anos canônicos pelo print (McCarthy 2022;
Dollish 2024; Ketchesin 2020; Kinlein 2020; van Dalfsen 2018; Kırlıoğlu 2020).

**Reparo técnico (ressalva documentada):** 38/39 vínculos legados referenciavam a listra do
apêndice com grafias obsoletas de ids; reanclados mecanicamente para a listra vigente (mesmo
conteúdo de referências; 39/39 literais). 39 citações de prosa legadas quebradas por quebra de
linha foram reunidas (conteúdo inalterado). Renome de 3 ids novos para conformidade do padrão
(`RAOANDROULAKIS_2019a/b`, `GEOFFROYMARUANI_2025`).

**Regras fundadoras fixadas na V2 (CONTROVÉRSIAS):** (1) timing ≠ estado; (2) sem biomarcador
circadiano único validado; (3) causalidade assimétrica animal↔humano; (4) intervenção ≠ mediador
demonstrado; (5) melatonina ≠ antidepressivo; (6) [ML] é roedor/modelo (extrapolação por analogia);
(7) anos = print; (8) bipolar sinalizado, nunca fundido à TDM.

**Portões:** gate P-5 ✅ · framework 0 ERRO (39 avisos legados `citacao_literal X[TAG]`, não
bloqueantes) · checklist 41/41 ✅ · tríade 137/137/137 mesmo ID-set.

**Pendências:** P-6 (2ª verificação cega, Via 2) — pendência honesta, ampliada para cobrir as
levas [AT] de B1–B16 ao fim da rodada; Satyanarayanan 2020 (agomelatina) [G1]; Mendoza 2024 /
Burns 2023 (Nature Mental Health) [G1]; DLMO como desfecho em ensaios; GRADE formal.
