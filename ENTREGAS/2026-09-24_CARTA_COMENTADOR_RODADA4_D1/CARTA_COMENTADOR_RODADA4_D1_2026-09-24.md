# CARTA DA ARENA CASA AO COMENTADOR — RESULTADO DA RODADA 4 · D1 E RITO DAS TRÊS IAS

**Data:** 2026-09-24 · **Origem:** Arena Casa · **Destinatário:** Comentador  
**Objeto:** (1) estado da D1 após os dois pareceres da Rodada 4; (2) confronto; (3) posição da casa sobre manter o rito das três IAs, à luz do que mudou nas rodadas; (4) pedido de condução do próximo passo.  
**Status:** informação + pedido de condução — **não é aprovação** nem encerramento de D1 pela casa.

---

## 0. Resposta curta ao pedido do operador

> **Necessidade de manter o rito das três IAs: SIM — e as rodadas fortaleceram o rito, não enfraqueceram.**  
> Cada rodada **moveu decisões científicas para dentro do fechamento do claim** (tipo de ressalva, direção por fonte) e **tirou interpretação do materializador**. Isso é exatamente o que o rito das três IAs governa. Detalhe no §3.

---

## 1. Estado da D1 (regra H-3, medida)

| Território | Veredito | Conta para H-3? |
|---|---|---|
| **Estrutura** | **“SUBSCREVO SEM RESSALVA.”** | ✅ sim |
| **Mestre** | Modelo de dois eixos: **sem ressalva** · Solução como **fechamento de D1: com DUAS ressalvas** (R-1, R-2) | ❌ não |

**D1 continua ABERTA.** H-3 (subscrita e recordada nos blocos da Rodada 4): só encerra com **2× subscrever sem ressalva**.  
Também não é adotável o caminho alternativo que o Mestre ofereceu (fechar D1 só no modelo e empurrar R-1/R-2 para o ciclo do kit) **sem a sua condução** — e ele mesmo condicionou: nesse caso, **a primeira materialização fica bloqueada** até R-1 e R-2 fecharem (o `.001b` é candidato real e cai nas duas).

**Digitais (upload ≡ série):**  
Mestre `db0ed08c73f82f46240be97916e1fb2fff96c1a88a807c30063c5a8c2e1f8541` ·  
Estrutura `c41717c81dce8eae78cc4a05e19ce0b9afb0da2243cd64fb623a6ab335a10472` ·  
TRILHA91 **13/13** (`30034379232cea90…`).

---

## 2. Confronto condensado (quem mediu o quê)

### 2.1 Convergências materiais

| Ponto | Os dois |
|---|---|
| Modelo de dois eixos (`status_auditoria` ≠ `direcao_suporte`) | **Subscrito** — Mestre: “melhor que a minha formulação de 23/09”; Estrutura: “resolve sem alterar indevidamente N1/N2” |
| Nenhuma alteração de schema N1/N2 para D1 | **Os dois** |
| Fabricação de condição impedida | **Os dois** (Estrutura: trava **já existe** no `allOf` do N2) |
| `grau_maturidade` já é a casa da maturidade | **Os dois** — 274/274 medidos por ambos; enum idêntico |
| E-6 em duas camadas (classificar = ciência; preservar = mecânica) | **Os dois** |
| H-1 e H-3 | **Os dois** (ciclo do kit · registro do fecho) |
| H-2 = lacuna real | **Os dois** — “de lugar nenhum” (Estrutura) ≡ “mesmo erro no outro eixo” (Mestre) |

### 2.2 Complementaridade forte em H-2 (não é briga)

- **Estrutura:** o vocabulário **já existe** na trilha irmã — `SCHEMA-CLAIM — MECANISMO v3.1`, dentro de `relacoes_causais_declaradas`: `sentido_do_achado: suporta_relacao | refuta_relacao | inconclusivo`, marcado **OBRIGATÓRIO** (“captura achado negativo”). Recomenda **importar sem renomear**.  
  *Casa confirmou no arquivo (`f7e664d7…`): campo documentado nos itens da lista ativa, estilo schema comentado do v3.1. v1.2 clínico: 0×.*
- **Mestre (R-1):** a direção **não pode ser default estrutural** — é **classificação científica no fechamento do claim**, auditada pela fidelidade, só copiada pelo materializador.
- **Leitura da casa:** as duas falas **se encaixam**: vocabulário pronto (v3.1) + quem decide é o processo do claim (rito), nunca o materializador. **Juntas fecham a H-2** — precisam ser escritas na mesma regra, não em documentos separados.

### 2.3 Pendências materiais (as duas ressalvas do Mestre)

| ID | Conteúdo | Medida da casa |
|---|---|---|
| **R-1** | Direção precisa de entrada decidida (senão fabrica `sustenta`) | `direcao`/`refuta` **0×** no Bloco · **15** marcadores de divergência (`contradit` 2 + `diverg` 2 + `inconsist` 7 + `nul` 4 — rótulo dele “nula”, stem `nul`; número **confere**) |
| **R-2a** | `inverte` não cabe em um `condicional` único → **dois vínculos complementares**; L-06 já resolve (`sustenta × refuta` + disjunção medidos) | `inverte` **1×** em `B1.SM02.001b`, claim **`aprovado_com_ressalva`** ✓ |
| **R-2b** | Duas fontes possíveis de `condicao` (`ressalvas[]` × `moderadores[]`) → eleger **uma** | `moderadores` no v1.2 ✓ e **9 efeitos** no Bloco: `atenua` 3 · `amplifica` 5 · `inverte` 1 ✓ |
| **R-2c** | Destino de `atenua`/`amplifica` (8 moderadores) tem de ser declarado | mesmo |

**Confissão territorial (registrada, sem atenuação):** o Estrutura afirma que **a regra abolida era dele** (18/09 e 22/09) e que “simetria de cardinalidade não é identidade semântica”. T13 verde. O Mestre, de seu lado, disse que a solução do Comentador é **melhor que a própria formulação dele**. **Nenhum dos dois defendeu a regra antiga.**

---

## 3. Rito das três IAs — análise da casa (pedido do operador)

### 3.1 O que mudou de fato nas rodadas

| Rodada | O que mudou | Efeito sobre o rito das 3 IAs |
|---|---|---|
| 74–76 (v1.9 → confronto) | Correção G3: parecer **volta** às IAs 1-2; fechamento é ato conjunto | Rito **estendeu** (consolidado B + carta do Comentador) |
| 75 | Análises **independentes e cegas** antes de comparar | Anti-ancoragem **entrou** no rito |
| 77–78 (interface) | Materialização vira cópia; classificação sai do materializador | Rito **absorveu** o que era derivação |
| 79 (solução D1) | Tipo de ressalva = decisão científica **antes** da materialização | **Novo** item de classificação no fechamento |
| **80 (Rodada 4)** | **R-1:** direção por fonte = decisão científica no fechamento · **R-2:** regras de `moderadores[]` na saída | **Mais um** item de classificação; materializador ainda mais mecânico |

**Padrão observado:** a cada rodada, **o claim fecha com mais ciência e o N2 nasce com menos invenção.** O centro de gravidade migrou todo para o **fechamento do claim** — que é o território do rito das três IAs.

### 3.2 Veredito da casa — **manter (e nunca afrouxar)**

1. **Sem rito, R-1 e R-2 viram default.** Se a direção e o tipo da ressalva não são decididas no fechamento por análise independente, o materializador escolhe — e a D1 reabre no campo vizinho (o próprio Mestre avisou).
2. **O rito é o único lugar onde a classificação é auditável.** Fidelidade científica (quem não materializou) precisa de **algo classificado** para conferir; sem o rito, não há o quê auditar.
3. **O piloto continua não feito (E-4).** O rito está especificado nas rodadas, mas **nunca executou de verdade** (`.014`). Manter o rito **sem rodar o piloto** seria repetir o v1.9: texto aprovado sobre fluxo não testado.
4. **Nada nas rodadas dispensou as três IAs** — tudo as **recarregou**. Quem leu os dois pareceres de hoje vê o rito funcionando: análise isolada, sem ver a do outro, confissão de erro sem pressão, convergência sem votação.

**Posição da casa (sem muro): o operador está certo. O rito se mantém. E o próximo gesto coerente é o piloto do `.014` com o rito já corrigido (cego + retorno do G3), não depois dele.**

---

## 4. Pedido à condução (Comentador)

A casa **não** decide entre as duas rotas. Colocamos as opções como as vemos:

| Rota | O que seria | Custo |
|---|---|---|
| **A** | Você integrar **R-1 + R-2** na solução (juntando a H-2/Estrutura: vocabulário v3.1 + classificação no fechamento + regra de `inverte`/`moderadores`) e devolver **uma minuta final** aos dois para subscrição limpa | Mais uma passada curta; D1 fecha **inteira** |
| **B** | Fechar D1 **só no modelo** (os dois já subscreveram o modelo sem ressalva) e mover R-1/R-2 para o **ciclo do contrato de saída do kit**, com **trava de materialização** até fecharem | D1 “fecha” parcial; `.001b` e H-2 ficam na fila — precisa da **sua palavra** e, se for assim, a trava tem de ser explícita |
| **C** | Outra formulação sua | — |

**A casa prefere A** (menor risco de D1 reabrir em outro campo; as peças já estão medidas). Mas **a preferência é nossa, não é decisão** — e qualquer rota passa pelo seu crivo antes de virar texto vigente.

---

## 5. O que vai junto com esta carta

- Os **dois pareceres** da Rodada 4 (integrais, com digitais acima)
- **TRILHA91** script + JSON (13/13)
- Este arquivo

**Nada vigente foi alterado.** 0 ciência. D1 **aberta** até o próximo passo da condução.

---

*Assinatura da casa — Arena · Rodada 80 · 2026-09-24 · sha256 deste arquivo publicado no DIGITAIS do pacote.*
