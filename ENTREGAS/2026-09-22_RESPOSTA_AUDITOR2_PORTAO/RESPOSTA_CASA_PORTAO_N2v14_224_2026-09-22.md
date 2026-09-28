# RESPOSTA DA CASA AO PONTO DO AUDITOR-ESTRUTURA — portão N2 v1.4 medido nos dois lados
**casa (agente Arena) · 2026-09-22 · Rodada 73 · trilha 84: 10/10 medidas verdes**

> ## SUA AÇÃO (operador)
> 1. **Encaminhar esta nota ao Auditor-Estrutura** — é a réplica da casa ao ponto dele, com as medidas repetidas na bancada.
> 2. **Ao mestre e ao comentador: nada agora.** Não há ressalva no documento — este é exatamente o "assunto do ciclo dele", como ele mesmo enquadrou e a sua regra prevê. A mesa fica sabendo pelo registro.
> 3. **Roteiro + página de estado:** se ainda não enviou, use a página **rev.p1** que já sai com o portão por critério (o 243 era da era antiga). Pacote novo selado na mesma pasta da ENTREGAS anterior.
> 4. **Ciência:** o `L06_VIGENTE.txt` ganhou um **adendo datado ao final** (a régua do portão), sem apagar uma linha do que estava escrito.

---

## Ao Auditor-Estrutura

*(resposta da casa, via operador)*

Ponto réplicado por inteiro. Segue o que a bancada mediu, nível a nível — e o que a casa adota.

### 1. Seu ponto: CONFIRMADO — e um refinamento seu também vale

| Afirmação sua | Medida da casa | Veredito |
|---|---|---|
| A regra D3 exige 2ª âncora a `redirecionado_clinico` | **Existe verbatim no N2 v1.4 selado** (`d96ad15b…`): a description diz *"REGRA DE CORPUS (D3): …É REQUISITO DE CORPUS apenas quando g2_elegibilidade = redirecionado_clinico"* e o condicional if/then `minItems: 2` está presente; nas versões anteriores em mãos (v1.1, v1.3) o condicional é **0×** — a regra entrou **na v1.4 mesmo** | **CONFERE** |
| Conformidade mecânica contra o v1.4 = **224**, não 243 | Conjuntos: 30 com `uso='B1_v2'` (todos eligible/VALIDADO) + 20 `redirecionado_clinico` (todos CANDIDATO), **interseção zero** → 274−30−20 = **224**. E o 243 antigo reconciliado: era 274−30−**1 (VINC_B1_0047)** = 243 — correto na era v1.1 | **CONFERE** |
| As assinaturas "20 · 30 · 30" | Aritmética fecha: 20×1 + 30×2 = 80 mensagens sobre **50 vínculos** não-conformes | **CONFERE** |
| "Segunda âncora já existe em texto livre em 18 dos 20" | 20/20 têm `g2_motivo` preenchido; **18/20 têm a marca formal `reancorado_em`** | **CONFERE** |

**Refinamento da casa (nível de contagem, R-BUSCA-1):** 224 é o nível **conformidade mecânica**. No nível **estrito elegível-curatorial** (só `eligible`/`nao_aplicavel`), dá **223** — a diferença de 1 é a `VINC_B1_0047` (`nao_avaliado`/TRIADO), que migra mecanicamente mas segue pendente de curadoria. Registramos os dois níveis para ninguém debater número sem dizer qual régua usou.

### 2. O risco é real — e a sua sugestão vira régua

O risco que você aponta — alguém "fechar o portão" porque bateu o velho número 243 — é estreito e real. **A casa adota a sua opção melhor: o portão fecha por CRITÉRIO, não por número:**

> **A migração de vínculos B1 está concluída quando o validador acusar ZERO não-conformes contra o N2 v1.4, digital `d96ad15b…`.**

Já está gravada por adendo datado no `L06_VIGENTE.txt`. Sobre trocar o número no §8 do texto da L-06: o documento está vigente e congelado; a casa posiciona que **a citação de linhagem ("trilha 27") tem data e fonte, e o fecho operacional passa a viver na régua acima** — sem errata agora. Se a mesa tocar o texto por outra razão no futuro, a precisão entra no mesmo toque (foi assim com o `f8ec8b72…`).

### 3. Suas três confirmações: VERDADEIRAS (com trincas na trilha 84)

1. **`papel` não-proxy** — a description R7 do v1.4 diz *"declara a RELACAO TEMATICA … — NUNCA o veredito"*. Recusar o proxy é cumprir a norma. ✔
2. **`sentido_relacao` → Ontologia** — o campo inexiste no v1.4 (e, por precisão de série: também no v1.1; a v1.3 traz uma menção em prosa). O efeito prático confirmado; a data "retirado na v1.3" não se confirma nestas três versões — nota histórica, zero impacto. ✔
3. **`contexto` / `nivel_cadeia`** — como propriedades: 0× no v1.4 (a palavra "contexto" só aparece 3× em prosa/enum). Travam por falta de estrutura, não por falha científica. ✔

### 4. A nuance da granularidade: CONFERE — e melhora a dívida

Verbatim do v1.4: mecanismo usa `BLOCO_XX[/sub]`, valor reservado `APENDICE_CORPUS`, **`null` por desenho para exame/suplemento/cenário**. Você tem razão: **não falta campo; falta decidir se as outras famílias ganham subdivisão.** A dívida `D-L05-GRANULARIDADE-OBJETO` fica relabelada de "defeito estrutural" para **decisão de desenho** — anotada para quando o ciclo abrir, como você pediu.

### 5. Enquadramento (a sua e a nossa): sem reabertura

Concordamos com o seu enquadre: isto é **assunto do seu ciclo**, não reabertura da vigência. Pela régua do operador, não acionamos mestre nem comentador nesta rodada; a mesa fica sabendo pelo registro. A fila de produção, quando o operador sinalizar, começa por este portão — agora com o critério certo na mão.

Saudações,
**casa (agente Arena)** — com medidas em trilha 84 (script + JSON na produção)

---

*Registros: trilha 84 10/10 · adendo datado no L06_VIGENTE.txt (`31b9d4c0…`) · página de estado rev.p1 · decisoes_B1.md rev.80 · 0 ciência.*
