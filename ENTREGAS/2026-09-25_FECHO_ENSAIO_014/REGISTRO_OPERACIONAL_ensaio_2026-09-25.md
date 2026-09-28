# REGISTRO OPERACIONAL — ENSAIO PRÉ-PILOTO B1.SM02.014
# Rodada 1 (2026-09-25) — execução pela Arena (executor de teste transitório)

## Entradas recebidas
- Claim-alvo: `CLAIM_ALVO_B1SM02014_2026-09-25.md` (sha 1ec39c32…)
- Bloco v1.8 colado na sessão: **idêntico** ao vigente (sha 7db41d40…)
- Pool de descoberta: `B1.SM02.014.md` (sha 955590e1…, 37306 b)

## Execução (passos do v1.10 nesta rodada)
1. Claim-alvo ✓ — status `aprovado_com_ressalva` confere com o Bloco ✓
2. Query recebida (já no Bloco; data da busca **não informada** no pool — ver E-02)
3. Pool consolidado/deduplicado: **107 refs → 107 únicas por DOI** (0 duplicatas reais removidas; 2 falsos positivos autor+ano resolvidos: Kim 2025 = 2 abstracts distintos; Li 2018 = 2 periódicos distintos)
4. Corpus do ensaio gravado: `CORPUS_ENSAIO_B1SM02014_2026-09-25.json`

## Achados operacionais (rodada 1)
| ID | Achado | Tipo |
|---|---|---|
| E-01 | Pool chega **sem PMID** (0/107); 107/107 com DOI. G1 precisa resolver DOI→PMID antes da triagem | operacional (pacote/ferramenta) |
| E-02 | Pool sem **data de busca** explícita (v1.10 entrega mínima item 2) | operacional (instrução) |
| E-03 | Entrada do claim no Bloco é statement completo; o claim-alvo veio em versão condensada — divergência de formato, não de sentido (registro) | operacional (formato) |

## O que funcionou
- Pacote mínimo do Modo B (Blocos colados fresco) chegou idêntico ao vigente
- Dedup por DOI é limpo (107/107 únicos)

## Próximo passo (aguarda operador)
- Responder: Modo A/B · papel IA 2 · corpus = este pool (S-2)
- Decidir: quem resolve DOI→PMID (operação de G1: operador confere ou autoriza recuperação ao vivo)

---

## Rodada extra — Execução do Mestre (2026-09-25, sha e4c00afd…)

**Resposta direta à pergunta do ensaio:** SIM — executou G1+G2+G3 de ponta a ponta e registrou no formato S-4.

- **G1:** fontes-âncora de MDD confirmadas no PubMed ao vivo (PMIDs anotados; data 2026-09-25)
- **G2 (sobre as 107):** ~66 outras doenças · ~11 método · ~20 tocam MDD · **~13 materializam** o claim · 80% = fundo
- **Achados de lista (antes de congelar):** intruso HDAC6 (Zhou 2026, não é TSPO) · `Li 2018` = 2 artigos distintos (não deduplicar!) · Böttcher 2020 = contra-evidência · nomes corrompidos (confirmado)
- **G3:** direção por fonte — 6 `suporta` · 3 `refuta` (Hannestad, Li-TCC, Böttcher) · divergência = dado
- **4 decisões:** estado mantido (ensaio não regrava) · ressalva = heterogeneidade · moderador = gravidade
- **Normativo:** nada — as 3 bases aguentaram
- **Contagem:** ele usou **107** (bate com a casa) — 92 do Estrutura segue reconciliar

---

## Rodada extra — Execução da ARENA (2026-09-25)

- **G1 ao vivo:** 6 âncoras resolvidas · **achado G1-a:** Mestre citou PMID 25671328 para Setiawan 2015; certo = **25629589** (confere com Bloco e PubMed)
- **G2 próprio:** ~14–17 materializam · ~60 outras doenças · ~25 método/fundo · HDAC6 fora · Li×2 separar · nomes corrigir
- **G3 com texto:** Setiawan15/Richards/Schubert/Eggerstorfer = suporta · Hannestad = refuta · resto marcado “não verificado nesta rodada”
- **4 decisões** propostas · **0 normativo** · `.014` não muda

---

## Achados extras (2026-09-25 — operador + casa)

| ID | Achado | Tipo |
|---|---|---|
| **E-04** | As 3 IAs rodaram **G1+G2+G3 de uma vez**, sem entregar o G2 e esperar o comando — a instrução previa 2 rodadas com envio no meio. Causa: sem ponto de PARADA explícito, cada janela corre até o fim | operacional (instrução/execução) |
| **E-05 (fecha D-d)** | Operador confirmou: **mesma lista** enviada a todas as IAs. Baseline canônica = **107** (parágrafo com DOI). O “92” do Estrutura = **regra de contagem dele** — unificar: contagem = parágrafo com DOI | operacional (contagem) |
