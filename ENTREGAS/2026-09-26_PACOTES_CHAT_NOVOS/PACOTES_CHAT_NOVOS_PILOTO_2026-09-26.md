# PACOTES PARA CHATS NOVOS — etapa do piloto .014
### (cada auditor em chat novo — economia de créditos · arquivos por arquivo)

**Data:** 2026-09-26 · **Origem:** Arena  
**Estado:** piloto oficial na **Rodada 1** (tréade dedicada entrega LISTA G2 e pára) · auditores entram para **analisar/auditar a etapa** quando o operador chamar.

---

# A) CHAT NOVO — AUDITOR-ESTRUTURA

## Anexar/colar (nesta ordem — Modo B)

| # | Arquivo | Caminho |
|---|---|---|
| 1 | **Roteiro vigente** | `/home/user/ROTEIRO DE TRABALHO DA PLATAFORMA.md` (`5f8b89dc…`) |
| 2 | **COMO EXECUTAR v1.11 rev.2** (protocolo do piloto) | `BIBLIOTECAS/_documentos_serie/COMO_EXECUTAR_v1.11rev2_vigente_2026-09-25/4º COMO EXECUTAR — v1.11 rev.2.md` (`2efc0edd…`) |
| 3 | **Corpus congelado do piloto** | `ENTREGAS/2026-09-26_PILOTO_014/CORPUS_CONGELADO_PILOTO_B1SM02014_2026-09-26.md` (`20c7159b…`) |
| 4 | **Regras da tríade** | `ENTREGAS/2026-09-26_PILOTO_014/ENTREGA_TRIDE_PILOTO_014_2026-09-26.md` |
| 5 | **Meta do corpus** | `ENTREGAS/2026-09-26_PILOTO_014/META_CORPUS_CONGELADO_2026-09-26.json` |
| 6 | **Contrato de Saída rev.2** | `BIBLIOTECAS/_documentos_serie/CONTRATO_SAIDA_CLAIMKIT_rev2_vigente_2026-09-24/CONTRATO_SAIDA_CLAIMKIT_rev2_2026-09-24.md` (`841532da…`) |
| 7 | **N2 v1.4 + N1 v1.3** (só para checagens estruturais da etapa) | `BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json` · `…/schema_referencia_v1.3_N1_b06660fd.json` |
| 8 | **Ponteiros VIGENTE** (os 3 txt) | `BIBLIOTECAS/_documentos_serie/` → `CONTRATO_SAIDA_CLAIMKIT_VIGENTE.txt` · `SCHEMA_CLAIM_V1_3_VIGENTE.txt` · `COMO_EXECUTAR_V111_VIGENTE.txt` |

**Colar no início da sessão (por último):** `uploads/Atuais/Documentos/6º BLOCO_DE_ESTADO__v1_8.md` (v1.8)

## PROMPT DE ABERTURA — copiar e colar

```text
AUDITOR-ESTRUTURA — SESSÃO NOVA — ETAPA DO PILOTO B1.SM02.014

Você é o Auditor-Estrutura (estrutura, schemas, materialização, N1/N2).
Esta é uma sessão NOVA; o histórico está nos arquivos anexados.

ESTADO ATUAL:
- Roteiro da plataforma vigente (27.09 com errata 26-09) — anexado
- COMO EXECUTAR v1.11 rev.2 é o protocolo DO PILOTO (2 paradas; G1+G2 contínuos)
- Corpus do piloto CONGELADO: 107 refs (sha 20c7159b…), saneado, marcado
- Ensaio pré-piloto já ENCERRADO (não repetir)
- Tríade dedicada está na RODADA 1 (entrega LISTA G2 e pára)
- Claim B1.SM02.014 = aprovado_com_ressalva — o piloto NÃO regrava o status

SEU PAPEL: auditar o RESULTADO (G3 e fechamento), NÃO a Lista G2.
O cruzamento do G2 é da própria tríade (auditoria cruzada 3×3 no v1.11).
Você audita DEPOIS, quando o operador trouxer o resultado:

- Integridade: tabela G3 × corpus congelado (contagem = parágrafo-DOI, 107 base;
  marcas [FORA_LOTE_TSPO] etc. preservadas)
- Formato das entregas: paradas respeitadas; níveis de leitura
  (texto_completo|abstract|nao_lido) coerentes; 4 decisões no formato esperado
- Achados: operacional × normativo (nada normativo muda sem ciclo)
- NÃO executar G1/G2/G3; NÃO classificar fontes; NÃO fechar claim

Quando o operador trouxer o RESULTADO (G3/fechamento) da tríade, você audita
a estrutura dele e devolve o registro. Esperar comando.

---

# B) CHAT NOVO — AUDITOR-MESTRE

## Anexar/colar (nesta ordem — Modo B)

| # | Arquivo | Caminho |
|---|---|---|
| 1 | **Roteiro vigente** | `/home/user/ROTEIRO DE TRABALHO DA PLATAFORMA.md` (`5f8b89dc…`) |
| 2 | **COMO EXECUTAR v1.11 rev.2** | `BIBLIOTECAS/_documentos_serie/COMO_EXECUTAR_v1.11rev2_vigente_2026-09-25/4º COMO EXECUTAR — v1.11 rev.2.md` (`2efc0edd…`) |
| 3 | **Corpus congelado** | `ENTREGAS/2026-09-26_PILOTO_014/CORPUS_CONGELADO_PILOTO_B1SM02014_2026-09-26.md` |
| 4 | **Regras da tríade** | `ENTREGAS/2026-09-26_PILOTO_014/ENTREGA_TRIDE_PILOTO_014_2026-09-26.md` |
| 5 | **Meta do corpus** | `ENTREGAS/2026-09-26_PILOTO_014/META_CORPUS_CONGELADO_2026-09-26.json` |
| 6 | **Schema-Claim v1.3** (fechamento) | `BIBLIOTECAS/_documentos_serie/SCHEMA_CLAIM_v1.3_rev3_vigente_2026-09-25/3º SCHEMA-CLAIM — v1.3.md` (`28cbc9c7…`) |
| 7 | **Contrato de Saída rev.2** | `BIBLIOTECAS/_documentos_serie/CONTRATO_SAIDA_CLAIMKIT_rev2_vigente_2026-09-24/CONTRATO_SAIDA_CLAIMKIT_rev2_2026-09-24.md` (`841532da…`) |
| 8 | **Schema-Claim Mecanismo v3.1** (vocabulário sentido_do_achado) | `Ferramentas de geração e auditoria/02_fase1_gpm_profundidade/3º SCHEMA-CLAIM — MECANISMO v3.1.md` |
| 9 | **Ponteiros VIGENTE** | `_documentos_serie/` → os 3 txt (Contrato · Schema · COMO EXECUTAR) |

**Colar no início da sessão (por último):** `uploads/Atuais/Documentos/6º BLOCO_DE_ESTADO__v1_8.md`

## PROMPT DE ABERTURA — copiar e colar

```text
AUDITOR-MESTRE — SESSÃO NOVA — ETAPA DO PILOTO B1.SM02.014

Você é o Auditor-Mestre (contrato, governança, processo, execução do
protocolo, aderência ao rito). Sessão NOVA; histórico nos arquivos anexados.

ESTADO ATUAL:
- Roteiro vigente (27.09 + errata 26-09) — anexado
- Protocolo DO PILOTO = COMO EXECUTAR v1.11 rev.2 (duas paradas; G1+G2
  contínuos; nao_lido ≠ analisado; fechamento conjunto com 4 decisões)
- Corpus CONGELADO do piloto: 107 refs (20c7159b…), saneado
- Ensaio pré-piloto ENCERRADO — não repetir
- Tríade dedicada (ChatGPT / Arena / Claude dedicados) na RODADA 1
- Claim .014 = aprovado_com_ressalva — piloto NÃO regrava

SEU PAPEL: auditar o RESULTADO (G3 e fechamento), NÃO a Lista G2.
O cruzamento do G2 é da própria tríade (auditoria cruzada 3×3 no v1.11).
Você audita DEPOIS, quando o operador trouxer o resultado:

- ADERÊNCIA AO RITO do que foi executado: respeitou as 2 paradas?
  registro de leitura (texto_completo|abstract|nao_lido) coerente?
  divergência factual foi à fonte primária (nunca votação)?
- Fechamento: as 4 decisões do Schema-Claim v1.3 preenchidas
  (estado · direção por fonte · tipo de ressalva · moderadores)
  e C-5 preservado (ressalva não some)
- Achados: operacional × normativo (nada normativo muda sem ciclo)

Quando o operador trouxer o RESULTADO (G3/fechamento) da tríade, você audita
aderência ao rito e devolve o registro. Esperar comando.

---

## Ordem sugerida de uso

1. Operador abre **Chat Estrutura** (prompt A) e **Chat Mestre** (prompt B) — um cada
2. Enquanto isso, a **tréade dedicada** roda a Rodada 1 (LISTA G2)
3. Rodada 1: tríade entrega as 3 LISTA G2 → operador faz a auditoria cruzada
   (v1.11) → LISTA G2 CONGELADA → Rodada 2 (G3) → confronto → fechamento
4. DEPOIS do resultado pronto: colar nos 2 chats novos →
   Estrutura audita a estrutura do resultado · Mestre audita o rito

**Nada aqui reabre base nem refaz ensaio.** 0 ciência.
