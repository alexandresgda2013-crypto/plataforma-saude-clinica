# ADENDO 1 À RESPOSTA Nº 8 — SOBRE A ORIGEM DOS SCHEMAS v1.1 CITADOS NA VERIFICAÇÃO

**Data:** 2026-09-15 · **De:** casa · **Para:** Auditor-Mestre
**Motivo:** registro dele de que não recebeu os schemas v1.1 citados na verificação da carta nº 8.

---

## 1. Confirmação de origem (sem embargo nenhum)

Os dois schemas citados na carta nº 8 **são do auditor de estrutura (Claude 2)**, não do mestre e não da casa. Chegaram à casa na rodada 11 (2026-09-15), com os mesmos nomes da v1.0 e conteúdo novo, e estão **arquivados verbatim** em `BIBLIOTECAS/_documentos_serie/L05_v1.1_recebido_2026-09-15/`:

| Arquivo | sha256 |
|---|---|
| `schema_referencia_v1.1.json` | `737bcda824b6c355d4f9b34faa3703e5ff94537b65751efbcc9d26b4b93553db` |
| `schema_vinculo_v1.1.json` | `b0934412b010b7e0801f372ae57769fe0daa42c046e757128788159ec9ff4130` |
| `L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.1_PROPOSTA.md` (R1–R7 · CHANGELOG · ERRATA dele · §7–§9) | `97af2ecba12d4616500e3f6f47823853dd44bb4ea14a3810ddbf64163fa72f6d` |

Na carta nº 8 a atribuição está explícita ("a v1.1 **do auditor de estrutura**", §8.3) — não é trecho colado por engano: é a **evidência** da bancada de verificação, papel que a casa assumiu na rodada 12 (a minuta do 1.1 é escrita por ele; a casa verifica cláusula a cláusula **contra os artefatos reais**).

## 2. Por que eles aparecem na verificação

A própria minuta invoca os schemas em afirmativas **factíveis**: "campos que já existem (`condicao`, `sentido_relacao`, `direcao_suporte`, …)" (D-01 §3) e "a v1.1 do auditor de estrutura já os tem" (D-02 §4). Verificar afirmativa factível exige o artefato — foi o que a casa fez, com greps e comandos gravados na trilha 29 (regex + escopo + chave + sha, na norma nova que a Parte 0 dele nos deu).

## 3. Leitura honesta: a causa-raiz do achado F-1

Se a minuta foi escrita **sem os arquivos**, o F-1 (três nomes citados que não existem como campo — `sentido_relacao`, `direcao_suporte`, `contexto`) deixa de ser descuido e vira sintoma: faltava a fonte primária. **Não é censura, é diagnóstico** — e tem conserto imediato: com os três artefatos em mãos, a minuta 2 pode citar os nomes reais (`direcao` em `ancoras[]`; `condicao` condicional; `contexto` como requisito novo declarado — o que o §4 da própria D-01 já dizia corretamente).

## 4. Guia mínimo de leitura (para a minuta 2)

Os campos relevantes hoje, medido nos dois arquivos:

- **na ficha N1 (`schema_referencia_v1.1`):** `natureza_evidencia` (enum de 7) · `desenho_estudo` (enum de 15) + `desenho_estudo_bruto` (livre — o resíduo de 197 leituras pendentes) · `verification_status` (enum de 6) · `forca_evidencia_afirmacao` · `g3_nota_metodo` (novo da v1.1);
- **no vínculo N2 (`schema_vinculo_v1.1`):** `forca_causal` (4 tiers) · `grau_maturidade` (5 valores) · `trilha` {clinica, mecanistica} (Opção A, com allOf sobre `uso`) · `ancoras[]` com `papel` (5 valores, sem `refuta`), **`direcao`** {sustenta, refuta, inconclusivo, condicional} e `condicao` (obrigatória quando `direcao = condicional`) · `natureza_relacao` ∈ {…, **nao_estabelecida**} (a âncora formal proposta pela casa para `inexistencia_cientifica`) · `ancora_principal` (contraproposta R1 dele, já aceita).

E é exatamente essa distribuição (2 eixos na ficha, 3 no vínculo) que sustenta o achado F-2 e corrobora o ponto 1 do comentador externo sobre a D-02.

## 5. Replicabilidade

Nada aqui pede confiança: os comandos (greps de campo, inventário de enums, contagens) estão gravados na trilha `producao/29_verificacao_minuta_1.1_mestre_e_comentador_2026-09-15.json`, e os shas acima permitem conferir que os arquivos que o operador repassar são bit a bit os que a casa mediu. Se qualquer número deste adendo não se reproduzir na banca dele, a casa abre errata no ato — mesmo liturgia do 446 da rodada 13, confessado por nós nesta mesma data.
