# GUIA DE ENVIO — KIT CLÍNICA (7 documentos) + leitura medida da bancada

**Data:** 2026-09-15 · **Uso:** o operador repassa ao Auditor-Mestre **os MESMOS bytes** arquivados aqui (pasta `_documentos_serie/KIT_CLINICA_recebido_2026-09-15/`) junto com este guia. A casa não envia nada direto. **Trilha:** 33 · **Ciência tocada:** 0.

---

## 1. Digitais dos 7 arquivos (conferir antes do repasse)

| Arquivo | sha256 |
|---|---|
| 2º PROTOCOLO DE ESCOPO — B1 (v1.3).md | `8968394171d34fddbb86203a50b42d26ba03f76a09738a0cb0da700082aad5d1` |
| 3º SCHEMA-CLAIM — v1.2.md | `56dc0e94cc2e2983384190706bc00977db38f82d4d2663c1c4eca533683b0e79` |
| 4º COMO EXECUTAR — v1.7.md | `186135166e061c85d7751a9b6a65955b2ccc999f4866e9f9af8cba8975771954` |
| 5º LISTA CANÔNICA — B1 SM-02 V1.3.md | `3252a920c6e972f21804f0488d6fd34df49ea59c6e23c8dd21e3ebf1239a37dd` |
| 6º BLOCO DE ESTADO v1.6.md | `0a630dba84f2f03d0d0aa727308a9b6eefef15cd7e0be0e7ae080b7f377756ae` |
| ESTRUTURA MESTRE.md (v2.1, 2026-08-04) | `f432174ff2ee1dbd6007d67a1d77ed5ada25484e1a1571088f4926cc724922bc` |
| TEXTO EXPLICATIVO DOS OBJETIVOS | `36c7d6ad6dc2dcf7522c7121427da72b21ce0bcbd2bf286799cb102466f677fb` |

(A mesma tabela está gravada em `DIGITAIS_KIT_2026-09-15.txt` dentro da pasta.)

## 2. O que é o kit (mapa de leitura em 10 segundos)

É o **kit de produção manual da camada atômica de verdade** do projeto (documentos de 2026-08, origem): claims G1 (existência) → G2 (elegibilidade) → G3 (suporte, 3 desfechos), mecanismo B1, submódulo SM-02 "Prova de Existência", esquema de 35 claims por 6 grupos temáticos. Ordem de leitura declarada no próprio COMO EXECUTAR: 1º `_ids_oficiais.json` (**não veio neste envio** — item a cobrar) → 2º Protocolo de Escopo (fronteiras B1/B4/B5, trilha humana × pré-clínica, exclusões) → 3º Schema-Claim (formato do claim: `evidence_role`, `uso`, comparador, moderadores, `usado_em_biblioteca`) → 4º Como Executar (processo, gatilhos, blindagens) → 5º Lista Canônica (os 35 alvos + filas) → 6º Bloco de Estado (onde o trabalho está). Estrutura Mestre e Texto Explicativo são complementares (painel macro + propósito).

## 3. A medição central (B1 V7 tem os achados?)

Cruzamento por `pmid_oficial` das 237 fichas × PMIDs das fontes dos **22 claims aprovados** que o Bloco carrega (comandos e chaves na trilha 33):

- **49 PMIDs únicos · 10 (20,4%) existem na V7 · 39 (79,6%) não.** Por claim, dedup de citações (57): **13 em V7 / 44 ausentes** — cobertura integral em **4** (.002, .005, .005b, .010), parcial em **4** (.001, .001b, .007, .015), zero em **14** (.001c/.001d/.003/.004/.006/.007b/.008/.009/.011/.012/.012b/.012c/.013/.013b).
- **Ligação formal claim→biblioteca: zero.** A V7 usa namespace próprio de claims (`B1.MEC.BLOCOxx.nnn`, 11 distintos); nenhuma ficha tem `B1.SM02.*` em `claim_id_origem`; no kit, `usado_em_biblioteca: nao` em 22/22. As **duas linhas de claims (SM-02 manual × MEC pipeline) coexistem sem fio** — é a régua de anexos do 1.2 aplicada ao objeto real, agora medido.
- Filas do kit: futura (5) e redirecionados-pré-clínica (4) — 0 em V7; **realocação (35) — 3 em V7** (HOWREN_2009, SUBLETTE_2011, YANG_2024b), todas com destino de realocação registrado no kit → coerência de uso a conferir na régua 1.2. **Das 92 rejeitadas PRISMA, 1 está na V7**: GARCIAGARCIA_2022 (kit: rejeitada de SM-02 por pré/pós sem controle → destino INT_*/SM-14; V7: `evid_role=review`, claim `B1.MEC.BLOCO06.001`) — **coerente apenas se a V7 a usar como intervenção/modulação, nunca como prova basal.** Item de conferência, não acusação.
- Conteúdo de área existe na V7 (IL-6/PCR periférico, TSPO-PET geral); os **achados-curadoria** (QUIN-LCR suicídio Lund, maus-tratos×PCR RR=2.07, TNF/IL-1β distinção bipolar, LCR Mousten, S100B/sTREM2/GFAP, complemento C5-LCR/C1q contraditório) **não** — ausentes como ficha e como nome citado na canônica (medido, trilha 33 K7).

## 4. O que isto destrava na mão do senhor (causa-raiz que motivou o pedido do kit)

1. **caso `uso` (§9 da v1.1):** o kit já carrega por claim exatamente os campos que faltam ao acervo V7 — `uso {clinico|contexto_mecanistico|gap_pesquisa}`, `evidence_role` (4 valores), `trilha` (humana/preclínica, constante-documentada em SM-02), `comparador` obrigatório — ou seja, o **material de origem dos 2 ERRO do P-8** (`natureza_evidencia`, `trilha`) existe e está tipificado; a etapa é de encaixe na régua, não de produção do zero.
2. **régua dos anexos do 1.2:** as duas linhas de claims agora têm medida (0 wiring, 20,4% de cobertura); o enum `evid_role` da V7 tem `review` (30 fichas — a dívida D-B1-R3-V2CLAIM) fora do enum do kit (4 valores) → alinhamento pertence ao 1.2-normativo.
3. **tipagem de risco da D-08:** o kit já traz `moderadores[].regra_motor` escritos **em linguagem de motor** (ex.: sexo×IL-6; IMC atenuação; maus-tratos RR=2.07/B12; ACMSD rs2121337; método violento; <18 anos atenua .005) — matéria-prima pronta para a tipagem.
4. **piloto da L-06 (oferta da bancada):** dois candidatos **reais** na B1 — (i) conflito de disposição 33339712/30696814 (rejeitado × realocar a B4; decisão humana pendente no próprio kit); (ii) contradição C1q **Luo 2022 × Yao & Li 2020** documentada na `nota_ressalva` de .013 (par por objeto+natureza, direto na matriz 1.2).

## 5. Estado interno do kit — precisões medidas (não bloqueiam o repasse)

- BLOCO v1.6: cabeçalho (=13 aprovados, próximo alvo .008/.012/.013) **dessincronizado do corpo** (22 entries, incluindo .008/.012/.012b/.012c/.013/.013b/.015) — trabalho posterior anexado sem bump de versão; 69 linhas com TAB (o defeito que a própria v1.6 celebra ter removido); chave `fontes_rejeitadas:` reaparece como 2º bloco real; 1× `- Claim_id:` maiúsculo; **.017** teve o desfecho mudado conforme COMO EXECUTAR v1.7 mas não tem entrada no Bloco.
- LISTA v1.3: `aprovados: 13` com comentário listando 15 ids; .008/.012/.013 marcadas aprovadas e ao mesmo tempo listadas como `proximo_alvo`; enum de status com capitalização fora do valor exato (`.012 Aprovado_com_ressalva`, `.013 Aprovado`); `.013b` mal indentado. (A consolidação da `fila_realocacao` em chave única ficou íntegra — conferido.)
- Disposições duplas: **20132991** (rejeitado em .012 × corroborante de .012c) e o conflito já autodeclarado **33339712/30696814** — ambos aguardando decisão.
- Referências a arquivos **não enviados**: `_ids_oficiais.json` (item 1º), `CANDIDATOS_IDS_OFICIAIS.yaml` (NLR e S100B pendentes), `Estudos que não foram escolhidos.md` (17+ PMIDs).

## 6. Repartição (para o senhor não receber lixo de autoridade)

- **Do Mestre (contratos):** tratar os itens do §4 na ordem que escolher; nada aqui pede reescrita retroativa agora — entra na régua/migração já planejada; os 2 candidatos de piloto L-06 estão oferecidos com PMIDs e motivos na trilha 33.
- **Do operador (P-6/produção):** decidir 33339712/30696814; ressincronizar o Bloco (versão e `proximo_alvo` com o corpo; incluir .017); enviar os 3 arquivos referenciados se existirem; confirmar qual `_ids_oficiais.json` regia as sessões do kit.
- **Da casa (bancada):** manter os 7 arquivos byte a byte com digitais públicas; medir qualquer revisão deles que chegar (diff + B/A); **nenhuma ciência tocada** — kit arquivado como veio, acervo V7 intacto (`6e2c2979…`).

— a casa
