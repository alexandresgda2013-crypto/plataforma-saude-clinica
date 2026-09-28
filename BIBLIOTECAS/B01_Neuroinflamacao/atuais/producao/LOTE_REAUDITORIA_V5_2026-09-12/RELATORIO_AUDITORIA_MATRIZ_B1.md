# RELATÓRIO DE AUDITORIA — INSUMO "MATRIZ CANÔNICA B1" (externo) vs. B1 V3 CANÔNICA
**Data:** 2026-09-08 · Auditoria ref a ref (regra permanente) · G1 eutils · Nada fundido sem verificação

## 1. Identificadores totais do insumo
- 74 itens com identificador (PMID ou DOI) + 13 itens apenas (Autor, Ano).
- **68/74 resolvidos no PubMed** (esearch DOI + esummary).
- **4 NÃO localizados:** `03946320231198828` (sequência ilegível, não é PMID nem DOI);
  `10.1186/s12974-026-03614-3` (Nussbaumer 2026 — DOI não indexado/inexistente);
  `10.1038/s12974-023-02769-y` (Vicente-Rodríguez 2023 — **DOI malformado** no insumo:
  s12974 é BMC, prefixo correto seria 10.1186, não 10.1038);
  `10.20944/preprints202201.0134.v1` (pré-print Almulla & Maes — não indexado).

## 2. FALSOS POSITIVOS do insumo (PMID não corresponde ao paper declarado) — REJEITADOS
| Declarado no insumo | PMID dado | O que o PMID realmente é (PubMed) |
|---|---|---|
| Min 2023 (citocinas/MDD) | 1110775 | Waldron HA **1975** — chumbo no sangue, Birmingham |
| Setiawan 2015 (TSPO) | 25797247 | Koo J 2015 — GSK3/rapalogs **oncologia** |
| Richards 2018 (TSPO) | 30156409 | Dingfelder F 2018 — **toxina citolítica** (biofísica) |
| Setiawan 2018 (TSPO) | 30563872 | Ojha R 2019 — **melanoma BRAF** (oncologia) |

> **Correção de rodada (2026-09-08, honestidade):** o item "fluoxetina (psychres)" havia sido
> listado aqui como 5º falso positivo. Na etapa de resolução DOI→PMID da reconciliação,
> `10.1016/j.psychres.2021.114317` resolveu para o **mesmo PMID 34864233** — o insumo estava
> **correto** nesse item (García-García ML 2022, meta-análise de fluoxetina×IL-6/IL-1β/TNF-α em
> ~292 pacientes com TDM). Item **incluído** (tag MA). Saldo final: **4 falsos positivos**.
> **Consequência:** o insumo contém erros de citação graves (4 PMID trocados + 2 DOI inválidos).
> Não pode ser fundido em bloco; só entra o que resolveu E confere autor/ano/tema.
> Setiawan 2015/2018 verdadeiros **já estão na nossa B1** por nome (com referência correta).

## 3. Cobertura já existente na B1 V3 CANÔNICA (188 refs)
- **Por PMID (6):** Dowlati 2010 (20015486), Köhler 2017 (28122130), Osimo 2020 (32113908),
  Costello 2019 (31326932), Holmes 2018 (28939116), Więdłocha 2018 (28445690).
- **Por nome/tema (referência equivalente já presente):** Setiawan 2015, Haroon (via KP),
  Zhang/NLRP3, GSDMD (tema), Gong, Xia, Huang, Xu & Núñez — reforço incremental apenas.

## 4. NOVOS verificados que acrescentam valor real (recomendo ENTRAR via fluxo [AT]-P7)
**Núcleo evidência NEGATIVA/metodológica (maior ganho conceitual — nossa B1 não os tem):**
- **Hannestad 2013** (23850810) — TSPO NÃO elevado em depressão leve/moderada [NEG].
- **Enache 2019** (31195092) — meta CSF/PET/post-mortem; centrais≠periféricos; heterogêneo.
- **Böttcher 2020** (32917850) — micróglia pós-morte NÃO pró-inflamatória; homeostática [NEG/CONT].
- **Eggerstorfer 2022** (36226319) — meta TSPO-PET (+~18%), sem especificidade celular.
- **Nutma 2021** (33433698) + **Nutma 2023** (37640701) — TSPO ≠ marcador específico de
  microglia ativada em humanos [METH].
- **Guilarte 2022** (34848203) — fontes celulares/subcelulares do TSPO [METH].
- **Wijesinghe 2025** (40036275) — validação post-mortem do TSPO-PET [METH].
- **Schubert 2021** (33515765) — aumento modesto, SEM relação com CRP [CONT].
- **Attwells 2020** (31683271) — correlatos séricos do volume de distribuição TSPO.
- **Barzon 2026** (42034206; 41957656) — influxo de radiotraçador ↓ com inflamação
  periférica; fingerprinting de rede [FRONT/METH].
- **Anderson 2020** (32958675) — convergência molecular/celular/imagem (astrócitos!).
- **Nagy 2020** (32341540) — snRNA-seq PFC em TDM.

**Kynurenine (humano/translacional):** Almulla 2022 meta (36231075); Parrott 2016 neurotóxico
hipocampal (27754481); Savitz 2019 (30980044); Wang & Miller 2018 meta-CSF TRYCATs
(28338954); Stone 2023 (38102897); Badawy 2023 (37123095); Bertollo 2025 (39245854);
Gong 2023 reforço (36054612); Martín-Hernández 2018 KP→glutamato (29725904);
O'Regan 2026 (41749295); Murata 2026 contextual (41745408).

**NLRP3/piroptose:** Zhang 2015 (25603858); Kaufmann 2017 (28263786);
MCC950 Liu 2022 (34978026) [sinal de alvo]; McColgan 2026 meta (41712983);
Kouba 2023 (36613574); Xu 2025 (40075143); **Li 2021 GSDMD/astrócitos** (34877938);
**Wang 2021 NLRP3 independente de GSDMD** (34678046) [METH — impede equação NLRP3=piroptose];
Han 2023 revisão (37725102).

**Temporalidade/subgrupos:** Ng 2018 longitudinal (32807846); Gędek 2025 1º episódio
(41226404); Li 2026 TNF drug-naïve (41588410); Jadhav 2024 adolescentes (39603515);
D'Acunto 2019 (30939048); Elgellaie 2023 sexo (37070163); Gavril 2024 (39595067).

**Antidepressivo → inflamação:** Liu 2019 TNF/respondedores (31427752);
Köhler 2018 pós-antidepressivo (28612257); Wang 2019 SSRI (30797959);
Xie 2025 sertralina (41023687).

**Pontes:** NLRP3 microglial → IL-1β → neurogênese 2026 (41862685) [ponte B16];
IL-33 meta 2023 (38025419).

## 5. NOVOS que NÃO recomendo entrar (com razão)
| Item | Razão da exclusão |
|---|---|
| Du 2022 GSDMD (35669106) | **TCE/TBI — fora de escopo permanente** |
| Moonen 2023 (36481964) | Alzheimer — outra condição; no máximo [EXTRAPOLAÇÃO] em M10-equivalente |
| McKenzie 2018 (29895691) | Esclerose múltipla — outra condição |
| Cheng 2022 minociclina (36332817) | Intervenção farmacológica — só como SINAL de alvo, com cautela P20; incremento baixo vs. corpus atual |
| 13 itens sem identificador | Marcados `[G1: a cravar]` se um dia necessários; clássicos (Dantzer & Walker 2014; Bay-Richter 2014) recuperáveis por busca dirigida — nossa B1 provavelmente já os cobre por nome |
| Regras "SE-ENTÃO", claims-mãe C01–C15 | Não são fontes; a formulação pode ser ADOTADA como texto de governança desde que cada claim empírico fique lastreado nas refs verificadas acima |

## 6. Avaliação estrutural do insumo (o que ele tem que a nossa não tem)
1. **Bloco de evidência NEGATIVA/controversa como núcleo obrigatório** (Hannestad; Böttcher;
   Schubert; heterogeneidade) — a nossa B1 tem ressalvas, mas esse núcleo ficaria mais forte.
2. **Bloco METHODOLOGY explícito** (TSPO≠micróglia; expressão≠função; sangue≠CSF; animal≠
   humano; cross-sectional≠causal) — compatível com nossa filosofia; pode enriquecer a
   seção de confundidores/inventário negativo.
3. **Regra "periferia ≠ cérebro"** (Enache) — nossa B1 afirma, mas sem a meta-âncora central.
4. **Arquitetura NLRP3 com saídas independentes de GSDMD** — nuance metodológica nova.
5. Requisitos já satisfeitos na nossa: regra TSPO/rs6971 e não-exclusividade de micróglia;
   rejeição do M1/M2 simplista; KP como interface; crosstalk com B3/B16.

## 7. Decisão proposta
ENTRAM (após G1✓ acima, passando por G2/G3 de vínculo na reconciliação): os ~55 itens do
bloco 4, priorizando (i) evidência negativa TSPO/central/micróglia, (ii) NLRP3/piroptose com
nuance GSDMD, (iii) KP humano, (iv) temporalidade/subgrupos, (v) antidepressivo→inflamação.
NÃO ENTRAM: bloco 5. Aplicação via fluxo de atualização ([AT]/P-7) com registro em
decisoes_B1 + revalidação dos 3 portões + P-4 da B1. Núcleo alvo final: insumo soma ~50–55
refs líquidas à B1 (188 → ~240), sem alterar a tese-mãe.

---

## 8. EXECUÇÃO (2026-09-08) — DECISÃO DO USUÁRIO: APLICAR AGORA
Reconciliação aplicada pelo fluxo P-7: **49 refs incorporadas** (não ~55 — poda final de
redundâncias e correção de rótulos de autoria contra o PubMed). Arquivos da execução:
- `matriz_b1_at_final.json` — 49 entrantes com metadados+abstract eutils + 20 rejeitados
  (motivo item a item);
- `../04_AT_ciclo_2026-09-08.json` — trilha do ciclo P-7 (encenagem CANDIDATO→APROVADO→V4).
Resultado: **B1 NEUROINFLAMAÇÃO V4 CANONICA.md** (18.525 palavras; v3 em `../historico/`).
Portões: gate P-5 APROVADO (237|257) · framework 0 ERRO · checklist 41/41.
