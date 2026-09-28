# P-4 — CHECKLIST DE FIDELIDADE CANÔNICA (Adendo v2.1) — B16 NEUROGÊNESE HIPOCAMPAL ADULTA

**Artefato:** `fidelidade_canonica_P4_B16.md` · Aplicado sobre `B16 NEUROGENESE V1 CANONICA.md`
+ Módulo 09 + vínculos N2 + ledger (Rodada 3/Fase 3). Relato item a item: SIM/NÃO + evidência.
Verificação por artefato (scripts oficiais + inspeção estrutural); **não substitui o P-6**
(avaliador cego independente — PENDENTE, ver fecho).

## A — Lastro das frases
| Item | Resultado | Evidência |
|---|---|---|
| A1 — Frase tem lastro | **SIM** | 288 claims no ledger, todos mapeados a refs do Módulo 09; 0 rótulo citado sem registro; 0 ref do Módulo 09 sem presença no texto (checagem programática de mão-dupla). |
| A2 — Nada de rejeitado/pendente residual | **SIM** | `status_auditoria=CONFIRMADO` em 288/288 refs; 0 `PENDENTE` residual; 2 pré-prints bioRxiv (37790349, 38352378) mantidos **com ressalva de emergência visível** e com versões publicadas fundidas (39228787; 39830600); 6 itens não-verificáveis (anais EWA ×2, resumos IJNPP ×2, venue não indexado, off-scope 26758842) **não fundidos** — fora do corpo. |
| A3 — Zero citação nova na Rodada 3 | **SIM** | `origem_pipeline=BUSCA_FERRAMENTA` em 288/288; nenhuma citação fora do conjunto G1 (288 PMIDs das tabelas do Briefing). |
| A4 — Log de reconciliação aplicado integralmente | **SIM** | `decisoes_B16.md` registra: 7 correções de autoria (Park 2019; Micheli 2018; Huckleberry 2018; Yamada 2019; Clarke 2017; Takamiya 2019; Gheorghe 2019) + 10 rótulos genéricos resolvidos por 1º autor PubMed + 6 sufixos de colisão + bug `revista_ano` (ano do nome do periódico) corrigido com pipeline reexecutado do zero. |

## B — Marcação de maturidade
| Item | Resultado | Evidência |
|---|---|---|
| B1 — Ressalva visível | **SIM** | 36 tokens de ressalva no corpo: `[APENAS PRÉ-CLÍNICO]` em causais animais, `[EXTRAPOLAÇÃO POR ANALOGIA]` (Norevik 2024; DA/envelhecimento), "pré-print bioRxiv — emergente" (Agrimi 2023; Chang 2024), `[G1]` (B11/lacuna; polimorfismo; elo quantitativo), "controvérsia VIVA e método-dependente", formulação canônica da existência humana. |
| B2 — Selos de verificação por frase | **SIM** | ledger 288/288 `APROVADO` (G1 VERIFIED_REFERENCE; G2 NAO_APLICAVEL; G3 APROVADO); 288 fora de fallback (0 "Entrada do Módulo 09"); 288 trechos = listra literal. |
| B3 — Pré-clínico/extrapolado não viram afirmação humana | **SIM** | 147 refs [ML] sempre com qualificador ("em modelo", "[APENAS PRÉ-CLÍNICO]"); hierarquia explícita: depressão = B/mecanístico-translacional (Peng 2026 + in vitro quinurenina), ansiedade = C/frontier (lastro humano indireto) — BLOCO_00 tese 8 e BLOCO_11; humano in vitro ≠ humano clínico (Zunszain/Borsini/Mandal qualificados). |

## C — Integridade estrutural
| Item | Resultado | Evidência |
|---|---|---|
| C1 — Mão-dupla texto ⇄ Módulo 09 | **SIM** | 288/288 ids do Módulo 09 presentes no texto (listras/prosa); 0 órfão texto→Mod09; framework 0 ERRO. |
| C2 — Vínculos íntegros | **SIM** | 288 vínculos N2; 0 órfãos; `trecho_ancora` >20 chars em 288/288; natureza/maturidade/tier preenchidos; `status_auditoria` no enum oficial. |
| C3 — Terminologia GRADE | **SIM** | Vocabulário "GRADE" ausente do corpo; graus A/B/C usados só como maturidade qualificada (B/mecanístico-translacional; C/frontier); tabela de evidências com `forca_evidencia` descritiva. |
| C4 — Sem PMID/DOI no texto corrido | **SIM** | 0 ocorrência de qualquer um dos 288 PMIDs no texto; 0 DOI; identificação só por (Autor, ano)[TAG] e rótulos de listra. |
| C5 — Escopo preservado | **SIM** | Neurogênese = escopo próprio (P16); SVZ/bulbo olfatório, câncer, desenvolvimento fetal fora (registrados); TCE/AVE fora; fármacos/compostos apenas como sinal (blocos 6.1/6.2; P20 sem doses); sem duplicação de B3/B15 (fronteiras editoriais 8.4/8.5 e BLOCO_09). |

## E — Metadados de verificação
| Item | Resultado | Evidência |
|---|---|---|
| E1 — `g1_metodo` sempre ferramenta | **SIM** | 288/288 `g1_metodo="eutils_automatico"` com `citacao_confirmada=true`. |
| E2 — `verification_status="verificado"` só com avaliador | **SIM** | 288/288 verificados têm `g3_verificado_por="IA G3 (G1 esummary; autor+ano+tema conferidos); P-6 avaliador cego pendente"` — sem "eutils/script/retrofit" no campo e sem campo vazio; G1 não promoveu a G3. |
| E3 — Trecho truncado sem G3 | **SIM** | 0/288 entradas do ledger com `trecho_ancora` não-literal/truncada após correção da listra de 33 refs (dividida em duas listras temáticas ≤580 chars); todos os trechos terminam em `*` (listra completa). |

## Veredito
**APROVADO COMO CANÔNICA (B16)** — A/B/C/E = SIM nos 15 itens.
Portões oficiais na data de aplicação: Gate P-5 **APROVADO** (refs 288 | vínculos 288) ·
framework `validar_auditoria.py` **0 ERRO** (288 avisos não-bloqueantes de `citacao_literal`
— padrão já registrado em B14/B15) · `checklist_entrega.py` **41/41**.

**Observações registradas:** (i) correções de autoria de 7 refs (1º autor real PubMed vs.
rótulo do briefing) documentadas em `decisoes_B16.md`; (ii) bug de `revista_ano` corrigido e
pipeline reexecutado integralmente; (iii) números de efeito das coortes pós-morte 2025–2026
permanecem **alegação G3** (não cravados); (iv) lacunas `[G1]` honestas: B16↔B11,
polimorfismos humanos, elo quantitativo roedor→humano.

**P-6 — 2ª verificação cega independente: PENDENTE.** Claims de alto risco a enviar ao
avaliador cego: existência/magnitude da AHN humana (Sorrells vs. Boldrini/Moreno-Jiménez vs.
multiômica 2025–2026); "processo neurogênico interrompido na TDM não medicada" (Peng 2026);
regra temporal da cetamina (Ma 2017; Rawat 2024); exigência contestada de neurogênese por
antidepressivos; curva em U (Fuss 2010); volume/BDNF/sangue ≠ neurogênese. Este P-4 **não
autocertifica** o risco residual: é checklist estrutural, não juízo científico independente.

---

# ADENDO V2 — RODADA [AT 2026-09-09] (P-4, 15 itens)

| Item | Resposta | Evidência |
|---|---|---|
| A1 — refs conferidas | **SIM** | 285 identificadores numéricos + checagem autor-ano×DOI: 283 vigentes, 2 novos G1-eutils, 4 falsos expostos |
| A2 — PMIDs reais | **SIM** | 290/290 resolvem PubMed (2 novos via esearch DOI→esummary→efetch, abstracts lidos) |
| A3 — autoria/ano corretos | **SIM** | Doludda B 2026 / Zhou L 2025 conferidos em esummary (autor+ano+periódico) |
| A4 — sem invenção | **SIM** | 4 identificadores não verificáveis NÃO fundidos; exposição registrada no manifesto |
| B1 — escopo mantido | **SIM** | Siopi 2016 (ZSV/bulbo olfatório) fora por decisão oficial do insumo; EXC Alzheimer/morfina ratificadas |
| B2 — fronteira B3/B15 | **SIM** | nada da rodada invade plasticidade rápida (B3) ou mTOR/autofagia (B15); crosstalk apenas |
| B3 — TEPT/ansiedade/depressão separados | **SIM** | Zhou 2025 = modelo animal de pós-parto, selo [ML] + [APENAS PRÉ-CLÍNICO] |
| C1 — selos honestos | **SIM** | Doludda 2026 [OB] (consenso=revisão-teto, padrão Kempermann 2018); Zhou 2025 [ML] |
| C2 — sem dose/conduta | **SIM** | P20: 0 ocorrências; "nº de ensaios clínicos" tratado como sinal de interesse, não validação |
| C3 — dígitos/PMID na prosa | **SIM** | varredura 7–9 dígitos = 0 na V2 |
| C4 — listras/vínculos íntegros | **SIM** | 46 vínculos+ledger reancorados após edição das listras §1.2/§11.2; 0 órfãos |
| C5 — tríade consistente | **SIM** | 290/290/290 (pmids×vínculos×ledger); manifesto V2 com histórico |
| E1 — gate | **SIM** | APROVADO (290 refs / 290 vínculos) |
| E2 — framework | **SIM** | 0 ERRO (290 avisos legados não-bloqueantes) |
| E3 — checklist | **SIM** | 41/41 |

**Veredito do adendo:** V2 mantém o selo CANÔNICA; rodada classificada como **auditoria externa
com fusão dirigida (ENTRA 2)** — a falha silenciosa da rodada 0 foi detectada exatamente pelo
desenho "auditar antes de fundir". **P-6 (Via 2) permanece PENDENTE** — ampliado às 2 novas
âncoras — e este P-4 segue sem autocertificar risco residual.
