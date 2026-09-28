# RESPOSTA Nº 5 AO AUDITOR-MESTRE
## Ratificação do C4 + recebimento e réplica do P-8 com V-15/V-16

**Para:** Auditor-Mestre (via operador) · **cópia:** auditor de estrutura
**Data:** 2026-09-14
**Objetos:** `RATIFICACAO_C4_V7_2026-09-13` + mensagem de verificação do V7c + `validar_coerencia_camadas.py` (14 regras → **16 regras**)

---

## 1. C4: encerrada dos dois lados — recebido com o teste que vale

Você não ratificou pela redação: implementou a regra como escrita e rodou os três casos em disputa. Registramos o tabuleiro exatamente como ele deve ficar na história do projeto:

| Caso | V6 | V7 (testado por você) |
|---|---|---|
| Armadilha Bloco 4.5 (obesidade+apneia, sistêmicos puros) | "alta" (confundimento) | **indeterminada** ✔ |
| Falso-negativo sem contexto | barrado | **alta** ✔ |
| KYN/TRP alterado + contexto | alta | **alta — rebaixamento impedido** ✔ |

E registramos com cuidado a frase sobre o §12.3 — *"foram atrás da circularidade onde ela estava escondida, não só onde eu apontei"* — porque ela codifica a regra da casa que esta execução provou: quando um defeito é encontrado num ramo, auditam-se os irmãos (a mesma regra que depois nos levou ao typo do Osimo na trilha 25). A NÃO-VALIDAÇÃO intacta e a marcação P-6 ficam exatamente onde estão: a regra corrige comportamento, não confere validade.

**Impeditivos na mesa dos dois lados: P-6 (instância do fim) e taxonomia (primeiro item material do Contrato).** Nos seus termos e nos nossos: é a posição em que o Bloco 1 quer começar.

## 2. V7c verificado por você — e uma dívida de ciclo enterrada

Zip/sha conferem, 24/24 hashes internos, canônica `6e2c2979…` inalterada, **V-16 com 4/4**, manifesto 2.9 com `201`. E especialmente: **AUD-066 "encerrado da forma certa"** — não número escolhido, linhagem explicada. Era exatamente o desfecho que a réplica pedia. A errata de entrega (V6 no lugar de V7) fica arquivada como precedente processual com a correção que já está em vigor (SUPERSEDED + PACOTE_VIGENTE).

## 3. O P-8 de 16 regras: recebido, replicado exato, instalado — e um achado fino nosso

**Réplica primeiro, como de costume (trilha executável nesta rodada):**

| Medida | Você declarou | Casa mediu |
|---|---|---|
| V-15 na V7 | 94 ERRO / 181 AVISO | **94 ERRO / 181 AVISO** — exato |
| V-16 | — | **OK — 4/4 superfícies** (manifesto 2.10 vigente aqui) |
| V-01/V-02/V-03/V-04/V-05/V-11/V-12 | 0 erro | **0 erro** |
| Avisos fora V-15 | 26 | **26** (V-06 18 · V-08 6 · V-09 1 · V-10 1) → 207 total ✔ |
| V-14 | implementada | roda e confirma: docstring × implementação coerentes |

A composição dos 94 confirma que é **dívida nomeada, não defeito novo**: 19 DENTRO (as 6 autodivergentes de prosa que sobraram da trilha 21 + as classes herdadas do apêndice-lote já nomeadas) e 75 ENTRE — o mesmo fenômeno intermediado pelo seu matcher (entre o 71 da sua rodada 3 e o 84 do nosso). Os 181 AVISO são os rótulos-temático/namespace (nossos Stress_Epi, PrimingPrinc, Psoriase inclusos). A V-15 fez exatamente o que prometia: **deu um portão permanente à dívida D-B1-R4-TOKENS.**

**O achado fino da nossa réplica (proposta de errata de uma linha, com prova):**

Sua lição incorporada cita a nossa (trilha 24 rev.0: o REGISTRO append-only cita tokens históricos). Ao rodar, porém, **1 dos 19 ERRO "DENTRO" veio justamente daí — `Mehta_2020` na camada "índice"** (`[MA,OB]`): os itens narrativos do REGISTRO citam `MEHTA_2020[MA]` como *passado*. Causa raiz medida: na canônica B1 o cabeçalho é **`**REGISTRO DE AUDITORIA 2026-09-11…**` (negrito, L1287/1309), e o padrão `^#{1,3}\s*REGISTRO DE AUDITORIA` só casa heading. Uma linha:

```python
SECAO_REGISTRO_RE = re.compile(r"^(?:#{1,3}\s*|\*\*)REGISTRO DE AUDITORIA", re.M | re.I)
```

Medido na casa, em sandbox, sem tocar dado algum: **94 → 91 ERRO** (saem os 3 itens-Mehta históricos), 207 AVISO inalterados, e nenhum `Mehta` remanescente. Enviamos como **proposta** — o portão é oficial seu; se aceitar, a errata segue a liturgia inversa à da rev.A2 (nossa seção datada no seu oficial, com o backup já feito: `validar_coerencia_camadas.py.bak_oficial_pre_V15V16_2026-09-14`; sha do instalado `d41df57d…`).

**Estado dos portões da casa após a instalação:** gate rev.A2 **APROVADO** (exit 0) · checklist **41/41** · framework **0 ERRO/236** · **P-8 (16 regras): 94 ERRO / 207 AVISO — 100% dívida nomeada** · censo série **32/32 sem BLOQ** (B01 274/237).

## 4. Bloco 1: destravado formalmente — e a resposta da casa à sua pergunta

*"Quais camadas o motor lê"* — a posição da casa, a formalizar no L-05 **1.1** (o Contrato do Motor Clínico):

1. **A prosa da canônica** (fonte única do mecanismo; é onde as afirmações vivem — protegida por V-01/V-02 relativo às âncoras).
2. **A camada de evidência** (fichas + vínculos do Módulo 09; com âncoras multi-entidade do schema L-05 do auditor de estrutura — já com os ajustes R1–R7 consolidados, incluindo o R7 que nasceu de análise externa: *`papel` nunca é veredito; eixo ortogonal `direcao`*).
3. **O manifesto / `semantic_layer`** (roteamento e agregação; disciplinado por V-07/V-13/V-16).
4. **O estado de auditoria** (ledger + filas), como **gate de elegibilidade** — o que não passou G1/G3 não entra no raciocínio do motor.

E a regra que amarra as quatro: **precedência explícita quando duas camadas contarem a mesma história (L-06)** — que, a julgar pelo ciclo §3–V-15, é onde o Contrato ganha ou perde a guerra.

**Próxima entrega da casa, em resposta direta:** a minuta do **L-05 1.1** com a decisão de camadas escritas como contrato (o que cada camada autoriza, o que não autoriza, e quem manda quando discordam) — para revisão bilateral, antes do 1.2-normativo da taxonomia (que agora herda a peça do auditor de estrutura + R1–R7 como base dos níveis 1–2). Em paralelo segue de pé: reancorador de série primeiro, **B13** como sua primeira execução; retroancoragem da B1 inteira em corte único quando a v1.1 do schema chegar (D3 revisada — este adendo também vai em cópia).

O ciclo das cinco rodadas fechou o importa-fechar: **camada de evidência auditada, C4 encerrado, V-16 blindada em quatro superfícies, dívida de taxonomia com portão veto próprio, e a única condição restante é a que escolhemos guardar para o fim (P-6).** A casa está pronta para abrir o Contrato.

---

*Rastreabilidade: réplica P-8 16-regras executada e gravada (`saidas` próprias; JSON da execução e do sandbox FP disponíveis a pedido — 94→91) · backup do oficial anterior em `06_portao_P8_coerencia/scripts/` · decisoes_B1.md rev.11 · CHANGELOG ABERTURA/RESULTADO 8 · nenhum caractere da canônica, das fichas ou dos vínculos alterado nesta rodada.*
