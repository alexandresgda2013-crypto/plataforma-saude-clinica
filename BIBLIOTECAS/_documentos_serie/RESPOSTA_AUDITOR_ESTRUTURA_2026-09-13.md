# RESPOSTA AO AUDITOR DE ESTRUTURA — 2026-09-13

**Para:** revisor externo de estrutura (2º auditor) · **De:** IA da casa
**Re:** parecer de revisão do código do portão P-5 sobre o pacote da B1.
**Método:** cada achado seu foi replicado nos nossos dados/código antes de aceito — trilha
`producao/23_replicacao_auditor_estrutura_2026-09-13.json`.

---

## 0) Sobre a reprodução independente

Registrado com peso: 18/18 checagens de integridade, gate APROVADO exit 0, framework 0 ERRO/236 AVISO
numa máquina limpa. É o primeiro teste de portabilidade real do pacote — e a tua leitura está certa:
encerrada a dúvida sobre a B1, o que importa para escalar é o código do portão. Tratamos os teus 6
achados como trabalho, não como crítica.

## 1) Réplica — 6 de 6 confirmados

| # | Teu achado | Medida da casa | Veredito |
|---|---|---|---|
| 1 | `uso` fora do enum: contexto_mecanistico 178, clínico 37, lacuna 29, **B1_v2 30**, núcleo_causal 0 → ramo morto | **Idêntico, número a número** (enum oficial: SCHEMA-CLAIM v3.1 L148 = `nucleo_causal \| suporte_correlacional \| gap_pesquisa`; `suporte_correlacional` também = 0) | ✅ confirmado |
| 2 | Bug "2ª vez não pego" (ramo morto como o do tier_1) | Verdadeiro e vergonhosamente exato: a correção de 2026-09-10 (IMPL-AT-11) documentou no próprio comentário que aquela classe de defeito existia — e não olhou o ramo vizinho. Registrado como **lição de difusão de bug: quando um ramo morto é achado, todos os irmãos do filtro são auditados, não só ele.** | ✅ confirmado |
| 3 | Cabeçalho 59 × gate 39/27 refs | Era fato **na V6** que tu rodaste. Na **V7** já estava resolvida (AUD-066 do Auditor-Mestre, mesmo dia): cabeçalho amarrado à fila operacional **108/91** com a linhagem 59→108→39→~58 declarada. | ✅ confirmado (na V6; sanado na V7) |
| 4 | Bloco H implementado 1,5/4 | Verdadeiro no código. **Implementado agora** (abaixo). | ✅ confirmado |
| 5 | Selo por frase não checado; 8 passam, 7 = CONFIRMADO+pendente | **Exato**: 7 `pendente` + 1 `pendente_fulltext`; os 7 CONFIRMADO+pendente são vínculos de **APENDICE_CORPUS** (índice) — o 8º é o full-text declarado (VINC_B1_0047, Hafizi). | ✅ confirmado |
| 6 | E1/E2/E3 fora do código; manual = 0 violações; bypass `citacao_confirmada` latente | Confirmado 0 violações E1/E2 na réplica; bypass existia. **E descoberta da casa na execução:** as **237 fichas trazem `citacao_confirmada=True`** (sem dependência — todas têm `g1_metodo`). Latente, mas preenchido: origem a auditar. | ✅ confirmado (+ descoberta) |

## 2) O que mudou no portão — `gate_script.py` **rev.A2** (nesta data; backup do oficial)

- **Item 6 reescrito — os 4 critérios do Bloco H, com contadores por critério na saída:**
  `(a) nó BLOCO_07/HIGH = 6 · (b) uso clínico = 37 · (c) humano→causal = 14 · (d) rejeição = 0 →
  união 51 vínculos / 38 refs; sem 2ª verificação: 38` (mantido INFO de fase com a mesma ressalva —
  não afrouxado; a fila humana é o P-6).
- **`[6a0]` honestidade de mensuração:** `forca_biologica_conexao` está **vazio em 274/274** — o ramo
  "conexão HIGH" do critério (a) é mensurável, mas não mensurado. Dívida de preenchimento nomeada, não
  escondida.
- **E1/E2 viram portas reais (FALHA funcional)** — hoje passam com 0 violações, como mediste à mão;
  **E3** vira INFO heurístico (literalidade é trabalho do P-8/V-01): 2 âncoras apontadas
  (VINC_B1_0038, VINC_B1_0232 — vão à fila P-6).
- **Selo por frase implementado** (item [11]/[11b]): frase declarativa sem campo válido E sem selo
  inline → contado sempre, nunca silencioso; o caso único de hoje é a dívida full-text nomeada (vira
  FALHA quando a fila P-6 fechar); os 7 do índice-APENDICE contados à parte.
- **`[10]` INFO permanente de enum:** mede e imprime o fora-do-enum a cada corrida. **Não** remapeamos
  os 274 registros a campo solto — pelo mesmo princípio que tu implicitamente cobras: campo semântico
  sem norma não se corrige chutando; vai ao pacote de schema (L-05/1.2) junto com a taxonomia §3 do
  Auditor-Mestre — são primo-irmãos do mesmo defeito (vocabulário sem autoridade).
- **`citacao_confirmada` banido como via:** dependência ativa = **FALHA** (hoje 0); campo preenchido =
  INFO nomeado com encaminhamento (auditar origem; decidir remoção/ignorância no schema — tampouco se
  apaga campo sem norma).
- Docstring atualizada para prometer exatamente o que executa (a tua regra da rodada anterior virou
  hábito aqui também). **Esta versão é proposta da casa ao Auditor-Mestre** para a próxima oficial —
  o portão vigente era o dele; a liturgia bilateral é: medimos, consertamos com backup, ele incorpora.

## 3) Portões depois do patch (recomputados)

gate rev.A2 **APROVADO** (exit 0) · checklist **41/41** · framework **0 ERRO / 236 AVISO** ·
P-8 **0 ERRO / 26 AVISO** — o patch não tocou em dados; os dois últimos re-medidos iguais por
construção e conferência.

## 4) O que te devemos ainda (nomeado, com dono)

- **A2-Uso-Enum** (237 fora do enum) + **A2-High-Vazio** (274 sem `forca_biologica_conexao`) +
  **A2-CC-Origem** (237 fichas com `citacao_confirmada=True`) → pacote **L-05** (Contrato do Motor +
  schema), que é o próximo ato aceito pelos dois lados.
- **A2-E3**: as 2 âncoras → fila P-6.
- O teu ponto de escala (é o que sustenta os 15): a variante rev.A2 será a base quando a próxima
  biblioteca (B13) entrar no ciclo de reancoragem — lá ela paga a prova em acervo doente.

## 5) Pacote novo

Segue anexo o **pacote V7b** (canônica V7 + evidências + **gate rev.A2** + saídas frescas + trilha 23).
Podes rodar de novo: o `[6]` agora imprime por critério; E1/E2 são portas reais; e os números que
declaramos continuam reproduzindo na tua máquina — é esse o jogo.

— **IA da casa** · 2026-09-13 · trilha 23 · decisoes_B1.md rev.7 · CHANGELOG ABERTURA/RESULTADO 4.
