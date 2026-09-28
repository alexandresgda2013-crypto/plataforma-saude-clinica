# Auditoria Científica de Conteúdo — B11 (Disfunção Tireoidiana)

**Data:** 2026-09-06 · **P-6** (avaliador cego) PENDENTE.
- 30 âncoras G1 (autor+ano+tema vs GPM); causalidade neural forte em animal [ML] (córtex Hochbaum, medo Maddox, GABA Mayerl, neurogênese Salas-Lucia/Valcárcel).
- Fenômeno endócrino (hipo=pseudodepressão, hiper=pseudoansiedade) reversível, bem estabelecido; associação com TDM primária modesta.
- Padrão de listras ENTRE submódulos (como B1), sem apêndice final.
- Falsos positivos / sem fonte sinalizados P-6: Siegmann meta-T3, Toma 2026 NTIS, Bode 2021, Watanave 2018; Samuels 2018 (neonatal, descartado); Mayerl id oficial corrigido (2022).
- Reposição/augmentation de T3 = sinal, não conduta (P20).


## Refazimento com GPM completo (Módulos 00–10) — 2026-09-06
- O GPM inicial estava **truncado** (só Módulos 00–05); o GPM completo adiciona Módulos 06–10.
- **Gate novo criado:** `check_gpm_completo.py` — rejeita GPM sem os 11 módulos antes de processar.
- Conteúdo novo (BLOCO_13): **relação em U** (hipo e hiper associam humor; Bode 2021/2022), **evidência negativa** (RCT TRUST: levotiroxina normaliza TSH mas não melhora sintomas; subclínico associação fraca), **anti-TPO superestimado** e **ansiedade inconclusiva** (Siegmann/Carta; meta populacional), subtipos F1–F8 (NTIS ≠ hipotireoidismo; lítio Lazarus; ciclagem rápida Walshaw; pós-parto Lucas), DIO2 Thr92Ala mecanismo forte mas replicação mista (Jo 2019).
- +10 refs validadas (Bode hipo/hiper, Odawara, Demet, Siegmann, Lazarus, Walshaw, Lucas, Carta, Jo); total 40.
- Samuels/TRUST, Nader/NTIS, Soheili-Nezhad UK Biobank não fecharam autor+ano+tema → sinalizadas P-6, sem forja.
- Padrão mantido: listras ENTRE submódulos (como B1).

---

## Rodada [AT] 2026-09-09 — reconciliação de insumo externo (P-7) → V2

**Insumos auditados:** RODADA0 (dossiê: 14 âncoras→PMID; 121 não citadas; 19 NAO-IDX), GPM
oficial (M00–M10, 10 regras fundadoras), matriz ChatGPT B11 (10 claims SM01–SM10; status
APROVADO_COM_RESSALVAS). Método: auditoria ref a ref ANTES de qualquer fusão; esearch
(DOI[aid]/autor+ano) + esummary (autor/ano/tema) + efetch (abstract lido antes de incorporar;
direção do resultado confirmada). Opção de escopo da fusão: **completa (aplicar tudo)** —
instrução permanente do operador nesta rodada.

**Universo:** 14 âncoras + 121 não citadas + 19 sem indexação verificável + 1 correção
editorial. **Decisão: ENTRA 56 (11 âncoras novas + 45 clínicos) · BAIXO 41 · EXC 11 grupos**
(inclui as 19 NAO-IDX). V1 (40 refs) → **V2 (96 refs; 9.700 palavras; rodada 4)**.

**Correções estruturais desta rodada:**
1. **Roca 1990**: o dossiê mapeava ao PMID do Romero-Gómez 2019. Roca 1990 real localizado por
   esearch independente (Endocr Res 1990; Roca RP, Blackman MR, Ackerley MB, Harman SM —
   hipertiroxinemia transitória em doença psiquiátrica aguda). Ambos ENTRAM corrigidos.
2. **"Zhang 2024" = correção editorial de Soheili 2023** → metadado/_aliases, não referência.
3. **Ao 2024**: dossiê dizia "TDM jovens"; abstract mostra tumor ósseo primário → EXC (câncer).
4. **Eckert 2020**: população diabetes tipo 1 → EXC (malha). **Kirnap 2020**: SCHiper
   iatrogênico em seguimento de DTC → EXC (oncologia).
5. **Toma 2026**: V1 sinalizava como pendente "NTIS/desiodinase"; artigo real = triagem
   hormonal rotineira em internados → tema corrigido na V2 (âncora estabelecida).
6. **"Watanave 2018"** (V1) não resolvido via eutils → permanece [G1], não forjado.
7. Anos canônicos = print: Forbes→2026, Wu→2021, Delitala→2016, Qiao→2022 (IDs ajustados).
8. 27 citações legadas re-costuradas + 6 trechos-âncora novos re-fundidos (higiene
   documentada; padrão B10). V1 arquivada em producao/historico/ e removida da raiz para o
   checklist apontar a V2 (aprendizado registrado).

**Classificações da matriz endereçadas:** SM01 CORE_ASSOCIATION (Roa Dueñas/Ma) · SM02
CORE_CLINICAL (fenótipos endócrinos: Aslan/Andrade/Almeida/Gorkhali/Dehesh) · SM03
CONTROVERSIAL_CORE (SCH: Zhao/Tang/Loh × Kim2018/Wildisen/Airaksinen/Roberts/Engum) · SM04
CORE_EPIDEMIOLOGICAL (Ittermann/Bensenor/Hong/Kumar/Liu/Baweja/Forbes/Hirtz) · SM05
CORE_ANXIETY (Fischer/Gonen/Zhao2023/Qiu/Panicker) · SM06 CORE_AUTOIMMUNITY
(Engum2005/Ayhan/Gulseren/Delitala/Wang2024/Karakatsoulis/Wu2021) · SM07
MECHANISTIC_GENETIC_SUPPORT (Soheili) · SM08 PROSPECTIVE_SIGNAL (Fan bidirecional; Hirtz;
Kim2018) · SM09 EMERGING_NONLINEARITY (Panicker/Qiu) · SM10 THERAPEUTIC_ADJUNCTIVE
(Bauer/Hilmon/Loh).

**Dez regras fundadoras fixadas** (B11-REGRA-01..10 no BLOCO_15): associação≠causalidade;
SCH≠causa registrável (evidência NEGATIVA canônica); AIT robusta mas "Hashimoto causa
depressão" proibido; genética compartilhada≠causalidade individual; não-linearidade≠faixa
ótima (P20 reforçado, nenhum corte fornecido); adjuvante≠conduta; bidirecionalidade
obrigatória; NEGATIVA com mesmo status; efeito do insumo = alegação a confirmar; multi-tag
permitida.

**Portões:** gate P-5 ✅ · framework 0 ERRO (40 avisos — ressalva de fase: listras legadas
com citacao_literal no formato listra, não bloqueante) · checklist **41/41** ✅.
**Tríade:** pmids 96 = vínculos 96 = ledger 96 (mesmo conjunto de IDs; trechos literais 1× na
V2 verificados por assert).
**P-6:** permanece pendência honesta (2ª verificação cega, Via 2), AMPLIADA a todas as levas
[AT] B1–B16; registrada em ledger/decisões/P-4/manifesto/fecho.
