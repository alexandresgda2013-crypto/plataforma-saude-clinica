# RESPOSTA 11 — P-8: três precisões e um reforço (nota do comentador externo, replicada na bancada)

**Data:** 2026-09-15 · **Ref.:** P-8 oficial sha `76e526cf…` (harmonizado, carta nº 10) · **Trilha:** 32 · **Ciência tocada:** 0

---

## 0. Origem e método

O comentador externo leu o P-8 integralmente e trouxe **três pontos de precisão** — declaradamente **sem reabrir** o regime por camada, o V-15/V-16 ou a harmonização. Recebemos como na rodada 13: **réplica empírica antes de aceitar, inclusive de quem concorda conosco**. Cada ponto abaixo traz: o enunciado dele → o que a bancada mediu (linha, comando, dado) → o veredito → a ação. Regime e harmonização **intocados**; os 2 ERRO por desenho seguem exatamente como estão.

A nota crua dele **não** circulará: o que chega ao senhor é esta carta, com os pontos **verificados** — dois deles com reforços medidos pela bancada que o comentador não tinha como ver.

---

## 1. Ponto 1 — V-06: detector heurístico de deriva, não prova de coerência semântica → **ADOTADO**

**Enunciado dele:** declarar normativamente que a V-06 é detector heurístico de possível deriva, gerador de AVISO, nunca prova de coerência científica/semântica; validação semântica = G3/revisão humana.

**Verificação da bancada:**

- O comentário interno do código (L446–448) já diz literalmente *"Heurística de deriva"*; a única emissão da regra é `rel.aviso` (0 ERRO no acervo, 18 ocorrências); a mensagem é prudente (*"possível correção não propagada"*).
- A §FILOSOFIA da docstring (L32+) **já declara exatamente a norma pedida**: *"este portão NÃO julga verdade científica — isso é o G3 e a revisão humana."*
- **Desalinhamento residual encontrado:** o TÍTULO da regra (L20) — `V-06 COERÊNCIA SEMÂNTICA ...` em caixa-alta — contradiz o próprio qualificador entre parênteses e a §FILOSOFIA. O cabeçalho interno (L445) repete o rótulo.

**Veredito:** confirmado com atenuação — comportamento, severidade e mensagem **já estão corretos**; o defeito é de **superfície textual**, e é real. A bancada já opera sob a leitura pedida (nunca apresentamos a V-06 como verificação semântica; as cartas históricas a citam apenas como contagem de avisos — conferido).

**Ação proposta** (redação sugerida; autoridade sua):

```
L20:  V-06  DERIVA ficha/vínculo × prosa ancorada (detector heurístico — só AVISO;
            nunca prova de coerência semântica; semântica = G3/humano)
L445: # ---------------- V-06 detecção heurística de possível deriva (ficha/vínculo × prosa ancorada)
```

---

## 2. Ponto 2 — V-08: escopo "mesma linha" manter como alerta de triagem → **ADOTADO**

**Enunciado dele:** a ligação semântica pode viver em outra linha do mesmo bloco; manter a V-08 como alerta de triagem, nunca critério de ausência de lastro; lastro estrutural = V-01/V-04/V-05 e vínculos/claims.

**Verificação da bancada:**

- Mecânica confirmada: `for ln in prosa.split("\n")` (L520) — escopo **mesma linha**, literal.
- Já é **AVISO puro** (0 ERRO), e a mensagem emitida já confessa o escopo (*"sem âncora de vínculo na mesma linha"*). Ou seja: comportamento = exatamente o que ele pede.
- **Fato F-C1 (medido pela bancada):** as **6 ocorrências atuais** decompõem-se em **5 prosa de governança/editorial** (cabeçalho `artefato_rotulo` · literalidade 100% · R11 n=8 · C3/AUD-051 27% · trilha 21 39,6%) e **1 substantiva** (TSPO-PET 18%, linha rs6971). A RESPOSTA_2 (2026-09-13) já caracterizara esse padrão editorial. A leitura "alerta de triagem" não é concessão ao comentador — é o que o dado faz dela.
- Desalinhamento residual: o título (L22) diz *"sem referência ancorada"* sem o qualificador, prometendo mais do que o teste.

**Veredito:** confirmado na mecânica e corroborado pelo conteúdo medido. **Não propomos mudança de mecânica** (alargar para janela/bloco calaria a regra na outra direção); o regime de triagem é o correto, e a ocorrência substantiva (TSPO-PET) é justamente o tipo de item que a triagem deve pôr no radar humano.

**Ação proposta:**

```
L22:  V-08  claim quantitativo sem âncora na MESMA LINHA (alerta de triagem; lastro = V-01/V-04/V-05)
```

*(Candidato futuro, fora desta carta: se o custo dos 5/6 de governança incomodar na série, o ponto de ajuste é o escopo da prosa varrida, não a severidade.)*

---

## 3. Ponto 3 — V-07 `related_entities`: cardinalidade ≠ identidade → **ADOTADO — e mais grave que o enunciado**

**Enunciado dele:** o teste compara quantidade (`n_txt == n_man`), não identidade; duas listas de mesmo tamanho podem ter entidades diferentes; comparar **conjuntos normalizados**.

**Verificação da bancada:** L494–499 — exato como descrito. E dois reforços medidos que o comentador não podia ver:

- **F-C2 — o furo está na superfície bloqueante.** O ramo divergente emite `rel.erro` (L498), não aviso. Contraexemplo executado na bancada sobre o dado real: lista de 15 IDs com `mecanismo_B16_neurogenese` trocado por um ID falso → **teste atual SILENCIA; teste por conjunto DISPARA**. Ou seja: uma dessincronia de identidade com cardinalidade preservada atravessa hoje a classe bloqueante do portão. A recomendação dele é **mais necessária do que o próprio enunciado avaliava**.
- **F-C3 — padrão do próprio portão.** O ramo irmão na **mesma regra** (`clinical_domains`, L500–506) já compara **conjuntos** (`a != b`) e já reporta os dois lados. Auditoria dos irmãos (grep em todo o script): `related_entities` é o **único** teste por cardinalidade sobre identidade do portão; `referencias_total_modulo09` compara total declarado × total real — semântica correta, pois total não é lista.

**Medida no dado real (mesmo regex/escopo/chave do portão):** canônica V7 × manifesto (`79d1309a…`): `n_txt = 15`, `n_man = 15`, **conjuntos idênticos** (0 divergência escondida hoje). O reforço é portanto **preventivo** — e protege precisamente a ingestão B2…B16, que é quando IDs de mecanismo caminham.

**Ação proposta** (alinhamento ao padrão do irmão; `rel.erro` e a guarda `if rel_txt` mantidos):

```python
        rel_txt = do_texto(r"\*\*Mecanismos relacionados \(IDs oficiais\):\*\*\s*(.+)")
        if rel_txt:
            s_txt = {x.strip() for x in rel_txt.split(",") if x.strip()}
            s_man = {str(x).strip() for x in (man.get("semantic_layer") or {}).get("related_entities") or []}
            if s_txt != s_man:
                rel.erro("V-07", "related_entities",
                         f"identidade divergente (fonte única violada) — "
                         f"só na canônica: {sorted(s_txt - s_man)} · "
                         f"só no manifesto: {sorted(s_man - s_txt)}")
```

---

## 4. Critérios de aceite da bancada (quando o senhor emitir a revisão)

1. Diff contra `76e526cf…` = **somente** estes três pontos;
2. Execução na B1 V7 (`6e2c2979…`): **totais idênticos — 2 ERRO / 299 AVISO / exit 1** (no dado atual os conjuntos são iguais, então o reforço da V-07 não altera o placar); V-07-`related_entities` segue muda, agora por identidade; **V-14 verde** (IDs das regras não mudam, só redação);
3. Backup `.bak_*` + nota datada + B/A gravados (norma da casa).

## 5. Prioridade

**Não bloqueia nada de hoje** — os 2 ERRO por desenho e os 299 avisos permanecem intactos. O marco natural é **antes da ingestão da série (B2…B16)**: é lá que o reforço da V-07 passa a ter valor real de guarda. Pode ser emitido no seu ritmo (após a minuta 2 da L-06 / taxonomia, ou quando preferir).

## 6. Crédito e registro

Os três pontos foram **adotados com crédito ao comentador externo** — o ponto 1, que ele mesmo chamou de o mais importante, é reforço de honestidade de superfície que a §FILOSOFIA já professava; a bancada aponta que o **ponto 3 empata com ele em importância** (superfície bloqueante com furo demonstrado em contraexemplo). Reforços F-C1/F-C2/F-C3 são da bancada. Tudo com comandos gravados na **trilha 32**. **Ciência tocada: 0** (0 campos, 0 fichas, 0 vínculos — a canônica V7 segue `6e2c2979…`).

— a casa
