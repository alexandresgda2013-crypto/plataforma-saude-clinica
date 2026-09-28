# ADENDO 1 À RESPOSTA Nº 6 AO AUDITOR-MESTRE
## Arquitetura consolidada **V2** recebida, verificada por diff e promovida a referência vigente

**Para:** Auditor-Mestre (via operador) · **cópia:** auditor de estrutura
**Data:** 2026-09-15
**Objeto:** `ARQUITETURA CONSOLIDADA DA PLATAFORMA V2 - 15.09.26.md` (do operador; sha256 `09692e18a5a65958bde4545ed6ff804c21c5945411159988654c7664c8a4a4e2`, 46.129 bytes, 1.351 linhas, 30 seções) — **substitui a V1** (sha `8f050469…`) como referência vigente da arquitetura. A resposta nº 6 desta mesma data segue válida; este adendo registra o que a V2 muda.

---

## 1. O que mudou V1 → V2 — diff computado linha a linha

O operador declarou: *"coloquei no desenho as evidências bibliográficas"*. **Confirmado — e o delta é maior que o declarado** (registramos tudo, como de costume):

| # | Mudança na V2 | Onde |
|---|---|---|
| 1 | Diagrama principal **redesenhado**: a Biblioteca ramifica para **EVIDÊNCIAS BIBLIOGRÁFICAS** e para as **NTs**; Evidências → **VÍNCULOS (com "L-05 N1 + N2" no desenho)**; ambos alimentam Ontologia/Grafo → JSONs → Motor; NTs também setam os Vínculos (rastreabilidade) | §2 |
| 2 | §5 reescrita e expandida com **5.1–5.5**: camada de evidência agora primeira da prateleira, com nomes de schema | §5 |
| 3 | **§5.1 cita `L05/schema_referencia_v1.1.json`** e **§5.2 cita `L05/schema_vinculo_v1.1.json`** | §5.1/§5.2 |
| 4 | Regra nova: a classificação da referência **não será duplicada por estrutura física de pastas por desenho de estudo** — natureza e desenho são propriedades do registro | §5 |
| 5 | **§5.4 não-duplicação** ("a evidência existe uma vez; os vínculos a reutilizam") + **§5.5 localização do aprofundamento** ("a Biblioteca de origem explica a relação; a correspondente aprofunda o objeto") | §5.4/§5.5 |
| 6 | **Nova seção §7 LIMITES DA NT**: proibições explícitas (zero PMID/DOI/claim novo; não elevar evidência; não converter hipótese em fato; **não converter relação mecanística em eficácia clínica sem sustentação**) e obrigação de preservar a distinção fato / associação / causalidade / hipótese / evidência direta / extrapolação / lacuna | §7 |
| 7 | Bloco final da V1 (que chegou com um trecho de formatação corrompida) **reescrito limpo** em três seções: §23 FLUXO CLÍNICO, §24 DEFINIÇÃO CONSOLIDADA, §25 PRINCÍPIO FUNDAMENTAL (+1 linha nova: **"Vínculos preservam a relação entre evidência, claim e entidade"**) | §23–§25 |
| 8 | **Novas seções de programa:** §26 PRIMEIRO PILOTO (B1 vertical), §27 EXPANSÃO MULTIDOMÍNIO (B1 + suplemento/exame/cenário/intervenção), §28 REGRA PARA O DESENVOLVIMENTO DO MOTOR, §29 DIVISÃO DE RESPONSABILIDADES NO PILOTO, §30 SÍNTESE FINAL (com evidências no fluxo) | §26–§30 |
| 9 | Renumeração geral: 23 → **30 seções**; inalterados: §3 catálogo (146 IDs), §8–§22 no conteúdo | — |

## 2. Re-verificação dos fatos da rodada 9 contra a V2

1. **146 IDs:** mantido (§2/§3) — segue exato no catálogo (151 listados − 5 removidos).
2. **Constantes de segurança do motor:** mantidas e reforçadas (§24) — já oficiais no cabeçalho do catálogo. Nada muda.
3. **As convergências da carta 6 saem reforçadas:** a V2 **escreve no desenho oficial a peça que estávamos aguardando** — *"L-05 N1 + N2"* na camada de vínculos, com os caminhos `L05/schema_referencia_v1.1.json` / `L05/schema_vinculo_v1.1.json`. Ou seja: **o lugar dos schemas do auditor de estrutura na arquitetura está marcado, e exatamente com o número da versão pendente** (v1.0 recebida na rodada 6; v1.1 = a que incorpora R1–R7). Nada a corrigir — apenas cumprir.
4. **Dois alinhamentos de nome que a casa pede no contrato (não bloqueiam):**
   (a) o documento cita `/Evidencias/Bibliograficas`; o diretório **real** é `Evidencias/Bibliografia` — recomendação: adotar o nome real no contrato (renomear diretório seria breaking sem ganho);
   (b) idem acima: schemas em mãos = v1.0; documento cita v1.1 → é a entrega pendente do auditor de estrutura com R1–R7.
5. **§7 LIMITES DA NT = exatamente as regras que a casa havia proposto para o futuro portão V-NT**, mais um item que adotamos imediatamente no L-NT: **não converter relação mecanística em eficácia clínica sem sustentação** (é o caso Raison da rodada 7 elevado a princípio de plataforma).
6. **§28** (o motor pode ser desenvolvido em paralelo às NTs **desde que contra os contratos**; "não assumir a Biblioteca como camada final de consumo") e **§29** (divisão de responsabilidades: auditoria científica / NT / ontologia / JSONs / motor; *"nenhuma etapa deve alterar silenciosamente a autoridade científica da etapa anterior"*) **formalizam o arranjo de trabalho vigente** — múltiplos agentes, mesmos contratos — e dão ao §29 da V2 o status de norma de programa.
7. **Colisão de nome segue viva e nomeada:** o §5.2 agora lista "direção da relação" no **vínculo** (sentido epistêmico — casa com o `direcao` do R7 ✔) enquanto o §11 (ex-§10) mantém "direção" no sentido de **grafo** (B1 → S-X). Mantida a proposta da carta 6: no contrato, `sentido_relacao` (grafo) ≠ `direcao_suporte` (epistêmico).

## 3. Efeito administrativo (liturgia da casa)

- **Referência vigente da arquitetura = V2** (`_documentos_serie/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2 - 15.09.26.md`, verbatim, sha conferido byte a byte).
- A V1 foi **renomeada com o prefixo SUPERSEDED** (`SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V1 - 15.09.26.md`, sha inalterado `8f050469…`) e criado o ponteiro `_documentos_serie/ARQUITETURA_VIGENTE.txt` — mesma regra nascida da errata de entrega dos pacotes: ninguém pega a versão errada.
- A minuta do L-05 1.1 (Contrato da Cadeia) passa a citar a **V2** como fonte normativa (§2, §5, §7, §22, §25, §26–§29).
- **Ciência: 0 linhas.** sha da canônica V7 recomputado nesta data = `6e2c2979…` (intocado); portões da rodada 9 (medidos hoje): gate rev.A2 APROVADO · 41/41 · framework 0 ERRO/236 · P-8 (16) 94 ERRO/207 AVISO (dívida nomeada) · V-16 4/4 — não re-rodados para este adendo porque nem um byte do acervo mudou entre as duas ações.

## 4. Veredito

A V2 é uma **evolução editorial e estrutural** da própria norma do operador: traz a camada de evidência para o desenho, nomeia seus contratos (L-05 N1/N2, na versão que estamos aguardando), escreve os limites da NT como regra e transforma o piloto e a divisão de trabalho em seções de programa. **Nada diverge do que foi verificado na rodada 9; tudo que diverge é acréscimo — e todo acréscimo converge com posições já tomadas bilateralmente (R7, L-05, V-NT, "não-elevação").** A casa a adota como referência vigente e segue para a minuta do Contrato da Cadeia sobre ela.

---

*Rastreabilidade: diff V1→V2 computado sobre os arquivos vivos (delta líquido +332 linhas; seções 23→30; tabelas de mudança acima) · V2 arquivada verbatim com sha `09692e18…` · V1 SUPERSEDED com sha inalterado · ponteiro `ARQUITETURA_VIGENTE.txt` · decisoes_B1.md rev.13 · CHANGELOG ABERTURA/RESULTADO 10 · zero caracteres de ciência alterados.*
