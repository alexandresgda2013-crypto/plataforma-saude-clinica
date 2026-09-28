# RATIFICAÇÃO DO C4 SOBRE A V7 — AUDITOR-MESTRE

**2026-09-13 · rodada 5**
**Artefato auditado:** `pacote_auditoria_B1_V7b_2026-09-13.zip` → `B1 NEUROINFLAMAÇÃO V7 CANONICA.md`, sha256 `6e2c2979…` — **idêntico ao declarado na carta 3**. 25/25 hashes internos conferem.

*Nota de entrega: chegou o V7b, não o V7c. Como a canônica V7 é bit a bit a mesma nos dois (a diferença declarada é manifesto 2.8→2.9, trilha 24 e decisões rev.8), o C4 é auditável sobre este pacote. O que não é auditável aqui é a errata de manifesto da rodada 4 — ver §4.*

---

## 1. C4 — **ENCERRADA**

A correção está no algoritmo, não só na redação. O cabeçalho da coluna mudou de "Critério C (contexto)" para **"Papel do Critério C (modificador — nunca condição)"**, e a regra está escrita de forma executável:

> se A foi satisfeito **apenas** por marcadores sistêmicos inespecíficos (PCR-us, IL-6, TNF-α/sTNFR2, IL-1β — **sem** KYN/TRP alterado) **e** ≥1 fator de C está presente → rebaixa para **indeterminada**; C ausente não barra, C presente não eleva.

Não avaliei pela redação. Implementei a regra como está escrita e rodei os três casos que estavam em disputa:

| Caso | V6 | V7 |
|---|---|---|
| **Armadilha do Bloco 4.5** — obesidade + apneia, só PCR/IL-6, 3 itens de fenótipo | "alta" por confundimento puro | **indeterminada (rebaixada)** ✔ |
| **Falso negativo que apontei** — 2 marcadores, 3 itens, **sem** contexto | barrado de "alta" | **alta** ✔ |
| Inflamatório com marcador de via — KYN/TRP alterado + contexto presente | alta | **alta** (rebaixamento corretamente impedido) ✔ |

Os três comportamentos mudaram na direção certa. A escolha da alternativa (b) sobre a (a) está bem fundamentada: confundidor **reduz especificidade**, não aumenta sensibilidade — é a leitura epidemiologicamente correta, e é tabular, portanto determinística para o motor.

**O que mais me convenceu não estava na tabela.** Verifiquei o §12.3, que na V6 dizia "Compatibilidade **alta** quando o Critério C (trauma) está presente, **mesmo com Critério A parcial**" — era a circularidade operando em prosa, fora da tabela, onde uma correção de tabela não a alcançaria. A V7 lê: *"com o esquema V7 (decisão C4), o trauma presente **não eleva** a classe: com Critério A parcial a leitura fica **Compatibilidade indeterminada**"*. Vocês foram atrás da circularidade onde ela estava escondida, não só onde eu apontei. Isso é o que distingue corrigir de cumprir tabela.

A ressalva de NÃO-VALIDAÇÃO do topo permanece intacta, e a decisão está corretamente marcada como sujeita ao P-6. Correto: a regra corrige o comportamento da heurística, não lhe confere validade.

## 2. Estado verificado da V7

| Verificação | Resultado |
|---|---|
| sha256 da canônica | `6e2c2979…` ✔ idêntico ao declarado |
| Hashes internos do pacote | **25/25 OK** |
| Contagens | 201 + 33 + 3 = **237 refs** · **274 vínculos** · **237 ledger** ✔ |
| Migração Mehta 2020b | `02_meta_analises` → **`01_pmids`** ✔ (validei o desenho em fonte primária na rodada 4) |
| C1 (Comai, Enache) | persistiu ✔ |
| `REF_OSIMO_2019` | presente ✔ |
| Gate P-5 rev.A2 | **APROVADO** |
| Framework | **0 ERRO / 236 AVISO** |
| P-8 · V-01 âncora literal | **0 erro** (274/274) |
| P-8 · V-02 âncora em rodapé | **0 erro** |
| P-8 · V-04 integridade referencial | **0 erro** |
| P-8 · V-05 citação sem ficha | **0 erro** |

## 3. Contabilidade dos impedimentos

| # | Impedimento | Estado |
|---|---|---|
| 1 | **P-6** — revisão humana | Aberto por decisão do operador (instância do fim) |
| 2 | **C4** | **ENCERRADO** ✔ ratificado nesta rodada |
| 3 | **Taxonomia de classificador** | Aberto → L-05/1.2 |
| 4 | **Camada de evidência** | Encerrado ✔ |

**Restam dois**, e são exatamente os dois que o plano previa que restassem: o P-6, que é do fim, e a taxonomia, que é o primeiro item material do Contrato do Motor. É a posição em que o Bloco 1 quer começar.

## 4. Duas coisas que este pacote não fecha

**(a) V-16 acusa na V7b.** Rodei as 16 regras: `H1=V7 · artefato_rotulo=V7 · nome_do_arquivo=V7 · **manifesto=V5**`. Isso é coerente com o relato de vocês — a errata é o manifesto 2.9, que está no V7c e não neste pacote. Não conto como achado novo; conto como **não verificado**, e fecha quando o V7c chegar. Não é urgente.

**(b) V-15 mede 94 erros e 181 avisos na V7** — os mesmos da V6, como esperado, já que a taxonomia é a dívida em aberto. Mantenho a leitura de proporção da rodada 4: **isso não quebra rastreabilidade**, porque os 274 vínculos carregam a ligação frase↔referência com V-01, V-02, V-04 e V-05 todos zerados. É dívida de namespace, a resolver por decisão no L-05, não por mutirão de correção.

## 5. Veredito

### **B1 V7: APROVADA COM RESSALVAS — base piloto confirmada, com C4 encerrada**

A biblioteca está apta a servir de fonte para a Narrativa Transversal e o JSON Modular. O selo definitivo continua barrado apenas pelo P-6, que é instância do fim por decisão do operador.

Não tenho condição nova a impor para prosseguir. **O Bloco 1 pode começar.**

---

*Verificações desta rodada: 25/25 hashes; sha da canônica conferido contra o declarado na carta 3; três casos de estratificação simulados contra a regra como escrita; §12.3 lido na íntegra; contagens 237/274/237; migração Mehta; persistência de C1; gate, framework e P-8 (16 regras) re-executados de forma independente.*
