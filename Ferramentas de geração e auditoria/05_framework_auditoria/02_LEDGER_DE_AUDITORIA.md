# 02 — Ledger de Auditoria de Conteúdo (`/Auditoria_Bx/ledger_auditoria_Bx.json`)

**Por que um ledger separado do Módulo 09:** o Módulo 09 (Prompt 4.0) é uma entrada por referência e tem um schema estável que não deve ser quebrado. Mas a auditoria de conteúdo opera sobre **instâncias de citação** — o mesmo artigo pode sustentar uma frase e não sustentar outra. O ledger guarda essa relação 1:N fora dos 5 arquivos oficiais, referenciando-os por `id_referencia_interna`. É o artefato que prova, frase a frase, que a Biblioteca foi verificada.

---

## 1. Estrutura do arquivo

`Auditoria_Bx/ledger_auditoria_Bx.json` é um array de objetos. **Um objeto = um trecho-âncora citado no corpo da Biblioteca** (não um artigo). O mesmo `id_referencia_interna` aparece quantas vezes for citado.

```json
[
  {
    "id_auditoria": "AUD_B1_0001",
    "mecanismo": "B1",
    "id_referencia_interna": "REF_SOBRENOME_ANO",
    "arquivo_modulo09": "01_pmids.json",

    "bloco_origem": "BLOCO_02",
    "secao_origem": "mecanismo_B1_neuroinflamacao > BLOCO_02 > 2.1",
    "trecho_ancora": "Trecho LITERAL da Biblioteca que esta citação sustenta (copiado do corpo, frase completa).",
    "citacao_literal": "(Sobrenome, Ano)[OB]",
    "tipo_classificador": "OB",

    "claim_id": "",
    "claim_status_na_lista": "",
    "origem_entrada": "LISTA_CANONICA | GPM | POLITICA_FONTES",

    "natureza_da_relacao": "",
    "grau_maturidade_cientifica": "",
    "forca_causal": "",
    "forca_biologica_conexao": "",
    "extrapolacao_por_analogia": "",

    "portao_G1_existencia": "",
    "portao_G2_elegibilidade": "",
    "portao_G3_suporte": "",
    "status_auditoria": "",
    "destino": "",

    "verificacao": null,
    "acao_correcao": "",
    "reconciliado": false
  }
]
```

## 2. Campos — regra de preenchimento

### Identificação e ancoragem
- **`id_auditoria`** — `AUD_Bx_NNNN`, sequencial, único.
- **`id_referencia_interna`** — chave estrangeira para exatamente uma entrada do Módulo 09. Integridade referencial obrigatória.
- **`arquivo_modulo09`** — `01_pmids.json` … `05_manuais_e_livros.json`, conferido contra o classificador `[tipo]`.
- **`bloco_origem` / `secao_origem`** — onde a frase aparece (BLOCO do Prompt 4.0 e caminho).
- **`trecho_ancora`** — o trecho literal sustentado. **Obrigatório, não vazio.** É o objeto que o G3 julga.
- **`citacao_literal`** — como a citação aparece no texto, ex.: `(Miller, 2016)[OB]`.
- **`tipo_classificador`** — `MA | EC | OB | ML | AT`, deve bater com o arquivo do Módulo 09.

### Vínculo com claim (quando existir)
- **`claim_id`** — o claim oficial quando a frase corresponde a um claim: `B1.MEC.BLOCO02.001` ou `B1.SM02.007`. Vazio quando ainda não há claim.
- **`claim_status_na_lista`** — `aprovado | aprovado_com_ressalva | em_busca | rejeitado | aposentado` (vocabulário do Schema-Claim v3.1), ou `""`.
- **`origem_entrada`**:
  - `LISTA_CANONICA` — entrada que já entrou na Biblioteca por um claim aprovado/ressalvado (Prompt 4.0, Hierarquia de Fontes). Auditoria leve: conferir G1 e que o PMID/achado batem; **não re-julgar G3** de um claim já aprovado.
  - `GPM` — referência vinda do GPM (Autor, Ano), sem claim. **É o grosso da auditoria nova.**
  - `POLITICA_FONTES` — referência complementar adicionada pelo Prompt 4.0 fora do GPM (deve ter sido declarada como "não veio do GPM").

### Eixos de evidência (vocabulário oficial — nunca inventar variação)
- **`natureza_da_relacao`**: `causal | contributiva | associativa | compensatoria | marcador | nao_estabelecida` (enum do Schema-Claim v3.1, importado do GPM v2.0). Vazio até ser classificado.
- **`grau_maturidade_cientifica`**: `muito_estabelecido | bem_suportado | moderadamente_suportado | emergente | hipotese_inicial` (GPM v2.0/Schema-Claim).
- **`forca_causal`**: `tier_1_necessidade_e_suficiencia | tier_2_necessidade_ou_suficiencia | tier_3_correlacional_mecanistico | tier_4_descritivo_estrutural` (Protocolo de Escopo).
- **`forca_biologica_conexao`**: `HIGH | MEDIUM | LOW` (Prompt 4.0).
- **`extrapolacao_por_analogia`**: `""` ou o **texto idêntico** da tag `[EXTRAPOLAÇÃO POR ANALOGIA: ...]` aplicada no corpo.

> Os quatro eixos são preenchidos de forma **independente** e nenhum decide sozinho (regra de blindagem do Como Executar). Eles descrevem; a decisão é do G3.

### Portões (mapeados para o fluxo G1→G2→G3 oficial)
- **`portao_G1_existencia`**: `PENDENTE | VERIFIED_REFERENCE | FALHOU`
- **`portao_G2_elegibilidade`**: `PENDENTE | ELIGIBLE_SOURCE | FALHOU | NAO_APLICAVEL`
- **`portao_G3_suporte`**: `PENDENTE | APROVADO | APROVADO_COM_RESSALVA | REJEITADO | INCONCLUSIVO`
- **`status_auditoria`** (resultado consolidado, vocabulário controlado — ver §3).
- **`destino`** (para onde o PMID vai quando não fica no lugar): `FICA_MECANISMO | REDIRECIONADO_MODULO_CLINICO | REALOCADO_BLOCO | REALOCADO_MECANISMO | FONTES_REJEITADAS | RESULTADOS_NAO_TRIADOS`.

### Objeto `verificacao` (preenchido na sessão de auditoria — regras do Como Executar)
```json
"verificacao": {
  "pmid_consultado": "",
  "doi_consultado": "",
  "query_utilizada": "string da query no PubMed (Caso A/B/C registrado)",
  "caso_query": "A_encontrado | B_sem_resultado_inicial | C_falhou_reformulada",
  "fonte_lida": "abstract_colado_na_sessao | texto_completo | esearch_esummary_apenas",
  "abstract_ou_trecho": "CITAÇÃO LITERAL do abstract/texto (obrigatória para G3 — 'abstract colado nesta sessão')",
  "tipo_manipulacao": "knockout_genetico | knockdown_sirna_shrna | farmacologico_inibidor | ... | correlacional_sem_manipulacao | descritivo_estrutural",
  "contraste_experimental": "ex.: wild_type_litermates | shRNA_scramble | veiculo_salino",
  "especie": "humano | camundongo | rato | ... | tecido_post_mortem_humano",
  "achado_resumido": "1-3 frases: o que a fonte mostra vs. o que o trecho afirma",
  "dominios_grade_observados": {
    "risco_de_vies": "baixo | moderado | alto | nao_avaliado",
    "inconsistencia_com_outros_estudos": "consistente_com_literatura_correlata | inconsistente | nao_aplicavel_fonte_unica | nao_avaliado",
    "indirecao": "direto | indireto | nao_avaliado"
  },
  "data_verificacao": "AAAA-MM-DD",
  "sessao": "identificação da sessão/mini-rodada",
  "verificador": "operador responsável"
}
```

Regras duras do objeto:
- G3 só pode ser fechado com **abstract colado nesta sessão** (`abstract_ou_trecho` não vazio). Sem isso, o resultado é `INCONCLUSIVO`/`PENDENTE`, nunca aprovação.
- Gatilhos de texto completo (Como Executar): ≤3 fontes principais; dado de subanálise; leva caminhando para ressalva/rejeição; preenchimento de `risco_de_vies`; inibidor/agonista (off-target); claim que alimenta BLOCO_07/BLOCO_08.
- Número/dado só entra se a fonte esteve visível na sessão.

### Correção
- **`acao_correcao`**: `"" | MANTER | CORRIGIR_PMID | CORRIGIR_METADADOS | REBAIXAR_LINGUAGEM | REMOVER_TRECHO | ADICIONAR_SINALIZADOR | TROCAR_REFERENCIA`
- **`reconciliado`**: `true` depois que a mini-rodada C aplicou a ação na Biblioteca/Módulo 09.

---

## 3. `status_auditoria` — vocabulário controlado (mapeado para G1/G2/G3 e suas filas)

| status_auditoria | Significa | Portões | destino típico |
|---|---|---|---|
| `APROVADO` | G1 ok, G2 elegível, G3 sustenta o trecho no nível redigido | G1✓ G2✓ G3=aprovado | FICA_MECANISMO |
| `APROVADO_COM_RESSALVA` | Sustenta parcialmente / sistema experimental diferente / ferramenta com ressalva; exige nota de ressalva | G1✓ G2✓ G3=aprovado_com_ressalva | FICA_MECANISMO (com `[SINALIZADOR]`/tag) |
| `NAO_SUSTENTA` | A fonte é real e lida, mas **não diz** o que o trecho afirma (ou diz o contrário) | G1✓ G2✓ G3=rejeitado | TROCAR_REFERENCIA (resgate) ou REMOVER_TRECHO → se não há fonte, vira claim `rejeitado`/remoção |
| `NAO_LOCALIZADO` | PMID/DOI não resolve ou não acessível após busca | G1=FALHOU | resgate (1x); não achou → entrada fica `pmid_oficial:""` e o trecho é rebaixado/removido; **não** é "rejeição científica" |
| `PMID_INCORRETO` | O identificador existe mas aponta para outro artigo | G1=FALHOU | CORRIGIR_PMID via resgate; se o artigo certo existe e sustenta → APROVADO |
| `ASSOCIATIVO_REDIRECIONAR` | Fonte real, mas puramente associativa/epidemiológica em população clínica (sem manipulação causal) | G1✓ G2=FALHOU (para trilha MEC) | REDIRECIONADO_MODULO_CLINICO — **nunca** fontes_rejeitadas |
| `REALOCAR` | Elo causal real, mas de outro BLOCO/mecanismo | G1✓ G2=FALHOU (local) | REALOCADO_BLOCO / REALOCADO_MECANISMO (fila_realocacao) |
| `ELEGIBILIDADE_FALHOU` | Desenho excluído (especificidade contestada sem off-target, preprint, retratado, in silico sem validação, anedótico) | G1✓ G2=FALHOU | FONTES_REJEITADAS (com motivo do exclusion_criteria) |
| `NAO_TRIADO` | PMID retornado pela busca, ainda não lido | G1=PENDENTE | RESULTADOS_NAO_TRIADOS |
| `PENDENTE` | Ainda não auditado (estado inicial de todo trecho) | — | — |

**Diferença epistêmica central:** `NAO_LOCALIZADO` (problema de identificação; o conhecimento pode ser válido) ≠ `NAO_SUSTENTA` (a fonte não prova o que se diz). O primeiro leva a resgate/correção; o segundo, a troca/remoção.

---

## 4. Regras de preenchimento na geração (para a mini-rodada de auditoria)

1. O ledger é montado a partir da Biblioteca + Módulo 09 já aprovados estruturalmente: para cada entrada do Módulo 09, localizam-se todos os trechos do corpo onde ela é citada; cada trecho vira um objeto com `status_auditoria: "PENDENTE"`.
2. Entradas `origem_entrada: LISTA_CANONICA` nascem com `claim_id` e `claim_status_na_lista` preenchidos; vão para o fim da fila (auditoria de integridade).
3. A fila de auditoria é priorizada: primeiro `GPM`/`POLITICA_FONTES` com `grau_maturidade_cientifica` = `hipotese_inicial`/`emergente` e referências "a confirmar"; depois o restante.
4. Um `id_referencia_interna` com resultados mistos entre trechos é normal: cada trecho carrega seu próprio `status_auditoria`. O Módulo 09 não é alterado durante a auditoria — só na mini-rodada C (doc 06).
5. Nada no ledger inventa PMID. Na dúvida de identificador, `pmid_consultado: ""` e `status_auditoria: NAO_LOCALIZADO` com a query registrada.
