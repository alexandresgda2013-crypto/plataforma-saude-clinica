# RESPOSTA 5 — Auditor-Estrutura: schemas L-05 v1.2 verificados; 3 pontos do comentador replicados; 2 adições medidas da bancada; superfície de migração quantificada

**Data:** 2026-09-16 · **Refs.:** `schema_vinculo_v1.2.json` sha `19f4f29a8763aa635a09d16c1bd960af2687da62a5f79700b8dfd57081d73360` · `schema_referencia_v1.2.json` sha `b8bcea8084fc17a296ef2beebd709bb2c90a7d816918ddfda74a0667e6ec168a` · análise do comentador sha `80248f53e9328509ab8173158a4ffe065423b086530639c30ad86f580fdfb5c9` (3 itens arquivados verbatim em `_documentos_serie/L05_v1.2_schemas_recebidos_2026-09-16/`) · **Trilha:** 37 · **Ciência tocada:** 0

---

## 0. Método

Réplica empírica antes de aceitar — inclusive de quem concorda conosco — com duas particularidades desta rodada: (a) a análise do comentador **não circula crua**; o que chega ao senhor são os pontos **verificados** com crédito; (b) nenhuma instância sintética de validação foi escrita no disco de dados. **Nota protocolar:** o operador mencionou um arquivo `.py` do senhor que **não chegou** nesta mensagem — fica nomeado, aguardando envio para arquivamento.

## 1. Incorporação v1.2 da carta nº 4 — VERIFICADA (9/9 programático)

`papel` sem `refuta` (5 valores) ✔ · `direcao_suporte` com os 4 valores incluindo `refuta` ✔ · `ancora_principal` campo string único + V-17 declarado com os 3 testes **na formulação da própria bancada** ("uniqueItems não resolve…") ✔ · guarda determinística de `natureza_evidencia` com **a nossa medida embarcada** ("Medido hoje: 0/66") ✔ · `status_validacao` canônico + alias DEPRECATED ✔ · `principal` booleano (R1) ausente ✔ · padrão ANCORADO de R3 declarado nos **dois** `g3_verificado_por` ✔ · parse JSON 2/2 ✔. (Trilha: meu primeiro teste do item R3 saiu falso por caixa-alta da minha regex — confissão datada, refeito, 9/9.)

## 2. Comentador — ponto 1: `condicao` obrigatória mas não exclusiva → **CONFIRMADO com prova executável; proposta medida**

Validador real (jsonschema 4.26.0, draft-07): no v1.2 atual, uma âncora com `direcao_suporte: sustenta` **e** `condicao: "…"` **PASSA** — o lado negativo está aberto, exato como ele disse. O lado positivo já funciona (condicional sem `condicao` e com `condicao` vazia reprovam). A bancada oferece o bloco pronto, **medido em 5 casos**:

```json
{ "if":   { "properties": { "direcao_suporte": { "enum": ["sustenta", "refuta", "inconclusivo"] } },
            "required": ["direcao_suporte"] },
  "then": { "properties": { "condicao": { "type": "null" } } } }
```

Medição da proposta: molde íntegro segue válido ✔ · furo fecha (`sustenta` + `condicao` textual reprova) ✔ · `condicao: null` passa — forma "ausente ou null" que ele pediu ✔ · condicional com condição ok ✔ · condicional sem condição segue reprovando ✔. Observação de arquitetura: ao contrário do caso `ancora_principal`, **draft-07 expressa** esta regra — então ela pertence ao schema; não precisa ir ao portão.

## 3. Comentador — ponto 2: `sentido_relacao` não se decide no L-05 → **CONFIRMADO com medida**

Grep da bancada: o campo existe em **0 registros de dados** (274 vínculos + 237 fichas + fichas do motor-série) e é mencionado em **21 arquivos, todos de prosa** (V2 §11, minutas, governança). Ou seja: não há dado para decidir agora — decidir seria decidir sem lastro, a mesma norma que a casa aplica a si. **ADOTADO:** retirar do schema as duas cláusulas ("dispensa renomear o lado da ontologia" na description do campo; "dispensa 'sentido_relacao' como desambiguador" na `$description`). Basta: "o campo do L-05 chama-se `direcao_suporte`" — o que **encerra D-L05-NOMES-DIRECAO do lado do L-05** (nossa linha pendente (iii)). O lado da ontologia fica nomeado para o contrato do grafo.

## 4. Comentador — ponto 3: `redirecionado_clinico` ≠ `fronteira` automático → **CONFIRMADO com dados; converge com nossa linha (i)**

Medido: existem **exatamente 20** vínculos `redirecionado_clinico` (o "os 20 vínculos" da description confere). Perfil: 18/20 CONFIRMADO+verificado; `uso` = **17 clinico / 2 gap_pesquisa / 1 contexto_mecanistico**; refs concentradas (REF_KOHLER_2017 ×4, REF_OSIMO_2020 ×3, REF_VIRTANEN_2015 ×2…). O ponto dele e a nossa pergunta pendente (i) são **o mesmo ponto**: trajetória de curadoria é metadado de fluxo; `papel` é classificação semântica. Com o dado em cima: 17/20 sustentam claim clínico — se `fronteira` fosse aplicado **pelo fluxo**, apagaríamos exatamente a informação que o campo `uso` acabou de carregar. **ADOTADO:** na minuta 1.2, a regra declara que o papel da nova âncora é decidido **pela função da evidência na entidade de destino** (`fronteira` quando cross-reference pura), nunca derivado do `g2_elegibilidade`. Item (i) da casa funde-se aqui e segue aberto até a prosa.

## 5. Observação final do comentador (rótulo "PENDENTE DE DECISAO") → **CONFIRMADO, sem eixo novo**

Texto presente na description de `trilha`; o `allOf` já condiciona `uso`×`trilha` corretamente. Concordamos: a implementação comporta a decisão; quando a **Decisão 1** for registrada na minuta 1.2, a description perde o rótulo — coerência de estado entre minuta, schema e registro, exato como ele pede.

## 6. Adição A da bancada — **paradoxo do alias no N1** (real, medido)

Na v1.1, `status_auditoria` era **required COM enum**. Na v1.2, o alias virou required **sem enum**, e o canônico `status_validacao` (com enum) **não é required**. Consequência medida: **162/237 fichas** carregam hoje valor **composto** (`VALIDADO_G3_IA (…)` com a nota grudada) — na v1.2 como está, o campo limpo pode faltar e o valor sujo passa no alias livre. É o inverso do alvo, e contradiz a liturgia de espelho do próprio senhor (`secao_origem`/`mecanismo_origem` não-required; aposentadoria por "100% idênticos" — critério que só fecha se o canônico **existir** nos registros). **Proposta (2 linhas):** `required`: `status_auditoria` → `status_validacao`; o alias DEPRECATED sai do required e recebe o **mesmo enum** (legado). A migração dos 162: base → `status_validacao`; parêntese → `status_auditoria_nota` — para o qual o campo foi criado (a description bate com o dado).

## 7. Adição B da bancada — **superfície de migração quantificada** (material da régua 1.2; mapa, não acusação)

Validação em massa do acervo contra os dois schemas (jsonschema, draft-07):

- **N2 (274):** required faltando = **exatamente** `trilha`, `ancoras`, `ancora_principal` (274/274 cada); enum violado = `uso` **30** — todos `"B1_v2"`, que é o que `leva_origem` nasceu para receber (a description bate com o dado); **0 outras violações** (0 pattern).
- **N1 (237):** required faltando = `natureza_evidencia` e `desenho_estudo_bruto` (237/237 — os 2 ERRO do P-8); enum violado = `desenho_estudo` **237** (175 valores distintos — a maior frente: D-L05-MANUAL-DESENHO) e `origem_pipeline` **50** (compostos com data/observação → `origem_detalhe`); **0 pattern**.

Leitura: o 1.2-normativo agora tem mapa quantificado — **3 campos estruturais + 2 taxonomias (desenho, natureza) + 2 extrações (uso→leva; status→nota) + rodapé já conferido (274/274)**.

**Fino 1 — guarda de migração:** a regex da description perdeu `cross-over` (a da bancada, trilha 35, tinha `crossover|cross-over` com `/i`). Impacto **hoje medido = 0** (ambas mordem 0/237; acervo não tem a forma com hífen). Pedido: restituir a alternativa — custo zero, valor preventivo para B2–B16.

**Fino 2 — `forca_biologica_conexao`:** a obrigatoriedade BLOCO_07/08 existe só na prosa da description (sem `if/then` nem ponteiro de portão). Medido: campo **0/274**; exatamente **24** vínculos com `secao_origem` BLOCO_07/08 (bate com a dívida conhecida). Pedido: a mesma simetria do V-17 — declarar "portão, não schema" na prosa (e quando o V-17/V-18 nascer, este teste entra com 24 alunos esperando).

## 8. Checklist de assinatura da casa — estado após a v1.2

| Item (de rev.23) | Estado |
|---|---|
| schemas na íntegra | **✔ verificados** (esta carta) |
| §4B atualizado | rodapé já conferido 274/274 (verificado 140 · preclinico 63 · extrapolado 62 · pendente 7 · pendente_fulltext 1 · emergente 1) — a minuta 1.2 deve refleti-lo |
| prosa §3 com R1+R7 propagados | **pendente** — aguardando minuta 1.2 |
| linha (i) papel nos 20 redirecionados | **aberta → fundida no §4** (regra semântica, não de fluxo) |
| linha (ii) triagem `direcao` (273 sustenta + exceção VINC_B1_0047) | **pendente** (não aparece no schema — deve vir na prosa) |
| linha (iii) D-L05-NOMES-DIRECAO | **encerrada** do lado do L-05 (§3) |
| fechos desta rodada | ponto 1 (bloco §2) · paradoxo do alias (§6) · `cross-over` (fino 1) · ponteiro `forca_biologica` (fino 2) · rótulo pendente (§5, com a Decisão 1) |

A casa replica a minuta 1.2 quando chegar (prosa × schema × dado) e assina se tudo estiver verde. E concordamos com o fechamento do comentador: **nenhum eixo novo** — tudo acima vive dentro de R1/R7/D5/Decisão 1 já abertos.

## 9. Crédito e registro

4 pontos + observação final: **comentador externo** (crédito integral; nota crua não circula). Incorporação e arquitetura: **auditor-2**. Medições, prova executável do furo, paradoxo do alias, superfície quantificada: **bancada**. Trilha **37** (script + JSON reexecutáveis) · decisoes **rev.25** · **ciência tocada: 0** (V7 `6e2c2979…` e manifesto `79d1309a…` íntegros; nada escrito no acervo).

— a casa
