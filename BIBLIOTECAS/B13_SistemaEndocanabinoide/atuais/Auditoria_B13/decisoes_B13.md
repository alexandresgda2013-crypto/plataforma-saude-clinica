# Auditoria B13 (Sistema Endocanabinoide)

Data: 2026-09-07 · P-6 (avaliador cego) PENDENTE.
- G1: 167/167 PMIDs do Briefing validados.
- Vínculos N2: 167
- SEC endógeno ≠ cannabis; bifasicidade; FAAH fase II nula; risco adolescencial; intervenções = sinal (P20).

---

## Rodada [AT] 2026-09-09 — reconciliação de insumo externo (P-7) → V2

**Insumos:** RODADA0 (38 âncoras; 66 não citadas; NAO-IDX), GPM molde v2.0 **reescrito**
(o antigo tinha 5 PMIDs vazando no corpo — higiene reconhecida), matriz ChatGPT B13, 2
briefings científicos adicionais (reconciliados: convergentes com a arquitetura em camadas).
Auditoria ref a ref: esearch (autor+tema nas divergências; DOI quando aplicável) + esummary +
efetch. Fusão: **completa** (instrução do operador).

**Universo:** 38 âncoras (20 já vigentes) + 66 não citadas (25 já vigentes) + NAO-IDX ×3.
**Decisão: ENTRA 40 (18 âncoras + 22 selecionados) · BAIXO 19 · EXC 4.** V1 (167) →
**V2 (207 refs; ~8.724 palavras; rodada 4)**.

**Correções/exposições:** 6 chaves divergentes normalizadas com alias (Cota→de Melo Reis;
Bedse→Borges-Assis; Mazurka→McWhirter; Gray→Gunduz-Cinar; Gamelin→Heyman; Zabik→
Zarazúa-Guzmán) · **falso mapeamento "Spohrs 2021"** = vídeo neurocirúrgico (EXC, exposto;
Spohrs real entrou pela versão publicada 2022) · **"Segev 2018" do dossiê = Șerban 2025**
(BAIXO); Segev real (29977073) localizado por busca **[G1] resolvido** · **[G1] McWhirter
(sexo feminino) e Zabik-RCT resolvidos** (este na via 10/camada exógena) · Ibarra-Lecue já
vigente na V1 (removido das pendências) · anos=print: Garani 2021 · Warren 2022 · Morena 2019
· GoldsteinFerber 2021 · Lu 2021 · Ribeiro 2021 · Uzuneser 2023.

**Regras fundadoras fixadas (B13-REGRA-01..10):** endógeno≠exógeno (via 10 isolada) ·
desregulação SELETIVA (AEA/PEA↑; 2-AG/OEA n.s.) · periférico não é diagnóstico · TEPT =
interface · animal≠clínica · reviews=arquitetura · causalidade experimental regional ·
exercício/PUFA interface · sandbox (preprint/congresso fora) · multi-tag.

**Portões:** gate P-5 ✅ · framework **0 ERRO** (167 avisos — ressalva de fase: listras
legadas com citacao_literal formato listra; não bloqueante) · checklist **41/41** ✅.
**Tríade 207/207/207** (mesmo conjunto de IDs; trechos literais 1× verificados por assert).
**P-6** pendente e ampliada (levas [AT] B1–B16).

---

## rev. datada 2026-09-13 — rename Saito (família-Hafizi; decisão da casa sob delegação vigente)

- **Fato:** varredura série B1–B16 (2.689 fichas, `_documentos_serie/VARREDURA_FAMILIA_HAFIZI_…`) achou
  1 caso NOMINAL da doença AUD-038/V-05: `REF_SAITO_1999` tinha o ano extraído do NOME NLM do periódico
  (Rev. bras. psiquiatr. "(Sao Paulo, Brazil : 1999)"). eutils esummary (2026-09-13, PMID 20512266):
  pubdate **2010 May**, sem epubdate. Citação padrão PubMed = 2010.
- **Aplicado:** rename `REF_SAITO_1999 → REF_SAITO_2010` em ficha (id + campo-lista), vínculo (id + 42
  âncoras de listra propagadas), ledger (id + 42 tokens/âncoras) e 1 token da listra-índice da canônica
  (§932) — **0 linhas de prosa científica**. Backups `.bak_saito_2026-09-13` ×5; notas datadas nos 3
  artefatos; trilha `producao/01_rename_saito_1999_2010_2026-09-13.json`; manifesto com entrada datada;
  sha novo da canônica `f01c9795f1a3799f…`.
- **Portões pós:** gate APROVADO · framework 0 ERRO · censo série 32/32 BLOQ 0 (re-rodado após).
- **Descoberta anexa (não tratada nesta decisão):** 1ª execução do portão P-8 na B13 = 167 ERRO V-02
  (âncoras em linha-lote) — perfil da B1 pré-R1–R13; fica nomeado para o ciclo de reancoragem da série.
- **Dívida nova (série):** D-SERIE-CONVENCAO-ANO-ID — 3 refs epub×print (B09 Gebara, B09 Scaini, B14
  Schweizer-Schubert) com ano do ID = epub e revista_ano = pubdate NLM; renomear toca prosa citacional;
  recomendação: adotar pubdate-ano NLM e replicar este rito. **Decisão do autor científico.**
