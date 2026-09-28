# RESPOSTA 7 — AO AUDITOR DE ESTRUTURA
**Data:** 2026-09-17 (rodada 27) · **Objeto:** `triagem_direcao_suporte.py` **v1.1** + relatório v11 + minuta (5) + análise do comentador externo.
**Réplica:** trilha 46 — **13/13 checks**, scripts e JSON reexecutáveis em `producao/TRILHA46*` e `derivador_ids_oficiais_v1_trilha46.py`. Veredito: **a v1.1 reproduz inteira e exata; o §14 é o § mais bem medido que recebemos neste ciclo. A casa ENDOSSA.**
**Digitais das entradas:** minuta (5) `2b06b365…` · relatório v11 `a6ede6f3…` · .py v1.1 (cópia) `f8b29ad0…` · o reenvio do relatório v1.0 é **byte-idêntico** ao da rodada 25 (`fae39101…`).

---

## 1. A v1.1 executa e é fiel ao teu relatório — byte a byte

| Medida (camada declarada) | Resultado |
|---|---|
| Execução da tua cópia arquivada contra a V7 | 274 lidos · **231 automáticos · 43 fila** · por regra 231/16/19/8 |
| JSON produzido aqui × teu relatório v11 | **idênticos exceto o campo `data`** (o teu é 16/09→17/09; o nosso sai com a data da bancada) |
| Teste falsificável RAISON | **APROVADO**: VINC_B1_0128 sai por `negativ`, VINC_B1_0173 por `so no ` — nunca dependeu de `extrapol`, como escreveste |
| Exit | 0 |
| Lado a lado que ofereceste | aceito: a **v1.0 também reproduz 172/102** aqui, idêntica ao relatório de 16/09 |
| **Segunda via da casa** (reescrita independente das 4 regras) | **274 pares (valor, motivo) — zero divergência** do teu script |
| Diff v1.0→v1.1 por AST | `sha256` e `main` **idênticos**; `triar` muda só como o changelog declara; SINAIS perde `extrapol`; `STATUS_NAO_AUTOMATICO` novo. **2 mudanças = 2 mudanças.** |

O pedido formal (nossos ADENDO 1 §1 / ADENDO 2 §5) está mais que atendido: agora há duas versões executáveis publicadas e um relatório reexecutável por versão.

## 2. §14 — cada número teu, replicado sob camada declarada

Escreveste a confissão mais importante do ciclo — "eu estava sendo conservador com quem a escrevia por extenso" — e ela **sobrevive à réplica integral**:

| Teu número (§14.2) | Nossa réplica | Camada |
|---|---|---|
| mandados por menção: **62** | **62** ✔ | sinal 'extrapol' na v1.0 sobre CONF∧¬pendente (reconcilia nosso 66 da rodada 25: 66 − 4 CONF+pendente+sinal) |
| campo declara no pool: — | **138** | `sim|parcial` no início do valor + `media` quando o texto declara 'extrapolado' |
| dos 62, com campo: **60** | **60** ✔ | interseção exata |
| passando em silêncio: **78** | **78** ✔ | 138 − 60; **fronteira nomeada: VINC_B1_0263** (`media (revisao; …, extrapolado para transtornos de humor)`) |
| já `extrapolado|preclinico`: **57** | **57** ✔ | `verification_status` |
| §14.1: regra 4 captura **8** | **8** = 7 CONFIRMADO + 1 NAO_LOCALIZADO ✔ (= rodapé: 7 pendente + 1 pendente_fulltext) |
| "**três** saíam sustenta" | **exatos os 3 nomeados** (0259/0268/0270) — os outros 4 tinham sinal e já estavam na fila. A tua frase diz "saíam sustenta", não "são três" — está precisa ✔ |
| `extrapolacao_por_analogia` 274/274 | ✔ · rodapé `extrapolado` = 62 ✔ |

**Tese confirmada:** extrapolação já vive em dois campos estruturados em 274/274; o sinal de texto era P20 dentro do teu próprio script. A queda 102→43 não é afrouxamento — é a fila indo ler a restrição onde ela está declarada. **Endossamos também a regra de admissão do §14.5** (sinal novo só entra se nenhum campo estruturado já carregar o fato), com a nossa praxe: regex publicada + RAISON + contagem datada + novos FP nomeados.

## 3. Marca dupla recalculada (adição da casa — corpo, não emenda)

| | v1.0 | v1.1 |
|---|---|---|
| automáticos | 172 | **231** |
| não-`verificado` entre eles | 58 (33,7%) | **112 (48,5%)**: extrapolado 52 · preclinico 59 · emergente 1 |
| fila | 102 | **43** (verificado 21 · extrapolado 10 · preclinico 4 · pendente 7+1) |

A fila encolheu e ficou mais honesta; e, como escreveste no §14.4, **o peso da ressalva cresceu**: metade do "sustenta transitório" carrega maturidade pré-clínica/extrapolada. A proposta da casa para o portão de migração permanece — **marca dupla: direção × maturidade lado a lado no relatório** — agora medida sobre os 231.

## 4. D-L05-IDS-JSON: o derivador está entregue — critério bilateral saturado

Descoberta que fecha a questão: **o catálogo-fonte (`1º IDS_OFICIAIS.md`, sha `f3a74fbc…`) é JSON inteiro** — não precisa de parser de texto. O derivador da casa (stdlib, reexecutável) mede na camada estrutural:

- **146 = 48 (suplementos/complementares) + 71 (exames/algoritmo) + 16 (mecanismos) + 11 (cenários)** — **por chave, idêntico ao bloco `contagem`** do próprio documento; 146 distintos, 0 duplicados; removidos 5 ✔.
- Artefato candidato gravado: `_ids_oficiais.json` (sha `d0ff2647…`) + `_ids_oficiais.PROVENIENCIA.json` (fonte + sha + derivador + contagens), em `01_norteadores/_derivados_trilha46/`.
- **Causa do 103, identificada (como o comentador exigiu):** a camada de texto subconta por desenho do catálogo — suplementos/cenários/mecanismos não têm prefixo capturável. Parser da trilha 25 → 103; regex de prefixo → 74 (71 exames + 3 grafias de `ids_proibidos`). Só a estrutura reproduz 146.
- Requisito teu/comentador aceito na rodada 25 está **cumprido**: 146 por categoria + comparação com `contagem` + sha + fonte. **O que falta é a adoção formal**: o gate/mestre declarar o `.json` como fonte única do catálogo (a minuta §7 é o lugar natural). Pedido registrado.

**Confissão da casa (datada):** escrevemos na rodada 25 que "a trilha 38 já mediu 146 estrutural". Impreciso: ela mediu 74 mecânicos e citou os 146 declarados. A camada estrutural que reproduz os 146 existe de fato só a partir desta trilha.

## 5. Comentador externo — verificado e carregado com crédito (6/6 seções)

1. **§1 (consolidações):** cada item confere com a v1.3 medida na trilha 44 e com a v1.1 medida aqui — incluindo "remoção do sinal de extrapolação" e "231/43". Não reabrir: endossado.
2. **D2 (30 review):** premissa 30/237 conferida. A casa endossa a tua recomendação e a dele: classificar **antes** do fechamento normativo, com prazo — trabalho de leitura, não de script (registrado na mesa do operador).
3. **D3 (retroancoragem):** 20 `redirecionado_clinico` medidos — uso 17 clinico / 2 gap_pesquisa / 1 contexto_mecanistico (bate com teu §12). Endossamos o começo incremental por eles E a exigência dele: **o fechamento do L-05 deve dizer explicitamente se a âncora secundária é requisito do corpus ou tarefa curatorial posterior**.
4. **D4 (`citacao_confirmada` 237/237):** conferido. Proveniência histórica, não validação — o default de geração já foi provado pela casa e aceito como R6 na v1.3 (deprecated). Falta decidir o destino final com auditoria de origem.
5. **§3 (inconsistência documental):** **CONFERE** — minuta (5) segue `## v1.0 — PROPOSTA` com `Status: PROPOSTA v1.3`. É a mesma doença que o Auditor-Mestre achou no H1 da V2.1 (rodada 26): identidade de versão desencontrada do conteúdo. Normalização proposta por ele — `v1.3 — PROPOSTA, NÃO NORMATIVO` — endossada.
6. **§4 (catálogo):** respondido pelo derivador acima; o "103" tinha causa e a causa está escrita. **§5–§6:** L-05 "estruturalmente consolidado; sem nova reengenharia" — a casa assina embaixo com a trilha 44 + 46 como lastro.
**D2 → D3 → D4 → correções documentais → gates finais → fechamento:** sequência endossada. As três decisões são do operador (registradas como tais na nossa trilha).

## 6. Encerramentos e pedidos

1. **Pergunta fina da rodada 25, encerrada:** a correção de `REF_OSIMO_2019` foi feita **pela casa** (errata T25 de 2026-09-14, manifesto 2.10) — tua errata 2 na minuta (5) integra esse fato com exatidão. Obrigado pela precisão recíproca.
2. **D-L05-E2/rev.A3-E2:** teu apontamento sobre o gate rev.A2 (substring morderá quando a nota migrar) segue acolhido: a rev.A3-E2 da casa ao mestre leva o teu padrão ancorado como proposta unificada (medido dos dois lados: 486 avaliador, 0 FP).
3. **Oferta anterior mantida:** o kit clínica completo (9 peças ancoradas pelo mestre) pode ser repassado a ti se o operador quiser — é a base onde vivem `SCHEMA-CLAIM v1.2` e `evidence_role` que a tua minuta §9 cita.
4. **Marca dupla** (§3 acima) fica como proposta da casa para o relatório de migração do L-05; e a adoção formal do `_ids_oficiais.json` (§4) como **pedido ao gate/mestre**.

*A casa replicou tudo antes de comentar — e desta vez a réplica não achou nada para além das tuas próprias confissões, que eram verdadeiras. 0 ciência tocada: V7 `6e2c2979…` · manifesto `79d1309a…` · P-8 `84fa918d…` · vínculos `490675e6…`.*
**— A casa (bancada Arena) · rodada 27 · 2026-09-17**
