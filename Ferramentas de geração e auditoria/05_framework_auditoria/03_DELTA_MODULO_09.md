# 03 — Delta Mínimo do Schema de Entrada do Módulo 09 (opcional, não-quebrativo)

**Princípio:** o Módulo 09 do Prompt 4.0 (5 arquivos JSON) permanece como está. Este documento propõe apenas **3 campos adicionais opcionais**, todos compatíveis com o schema atual (ninguém precisa renomear nada), para que o resultado da auditoria de conteúdo fique registrado no próprio Módulo 09 depois da mini-rodada C. Se você preferir não tocar no schema do Prompt 4.0, ignore este documento — o ledger (doc 02) carrega sozinho toda a informação de auditoria.

---

## 1. Schema atual (Prompt 4.0, inalterado)

```json
{
  "id_referencia_interna": "REF_SOBRENOME_ANO",
  "pmid_oficial": "",
  "doi": "",
  "titulo_artigo": "",
  "autores": [],
  "revista_ano": "",
  "desenho_estudo": "",
  "secao_origem": "Seção/Bloco de origem (mecanismo_B0X_nome)",
  "achado_central_molecular": "",
  "extrapolacao_por_analogia": "",
  "status_auditoria": "",
  "claim_id_origem": ""
}
```

Regras existentes mantidas: `extrapolacao_por_analogia` espelha a tag do corpo; `claim_id_origem` só é preenchido com claim aprovado/ressalvado da Lista Canônica; `status_auditoria` começa vazio.

## 2. Campos propostos (aditivos)

```json
{
  "...": "campos atuais inalterados",

  "citacao_confirmada": true,
  "origem_referencia": "GPM",
  "ids_auditoria": []
}
```

| Campo | Tipo | Valor padrão | Regra |
|---|---|---|---|
| `citacao_confirmada` | booleano | `true` | `false` quando a referência entrou como "referência específica a confirmar" (GPM) ou quando o G1 (`pmid_oficial`/metadados) ainda não foi verificado. Sinaliza as entradas de maior risco para a fila de auditoria. **Não substitui** a verificação — só a prioriza. |
| `origem_referencia` | enum | `"GPM"` | `"LISTA_CANONICA"` (veio de claim aprovado, com PMID exato) / `"GPM"` (veio do GPM, Autor/Ano) / `"POLITICA_FONTES"` (complemento do Prompt 4.0 declarado como não-vindo do GPM). |
| `ids_auditoria` | array de strings | `[]` | Lista de `id_auditoria` (AUD_Bx_NNNN) do ledger que referenciam esta entrada. É a ponte Módulo 09 ↔ ledger, resolvendo o 1:N sem mudar a estrutura: o Módulo 09 continua 1 linha por referência; o ledger guarda 1 linha por trecho. |

## 3. Preenchimento do `status_auditoria` (campo que já existe)

Hoje o campo é string livre. Recomenda-se usar o **mesmo vocabulário controlado do ledger** (doc 02, §3), com regra de agregação por entrada:

- Entrada só com trechos `PENDENTE`/`NAO_TRIADO` → `status_auditoria: ""` (não auditada).
- Pelo menos um trecho `APROVADO`/`APROVADO_COM_RESSALVA` e nenhum problema de identificação → `"VERIFICADA"` (a referência é real e sustenta ao menos um trecho; **não** significa que todos os trechos foram aprovados).
| Todos os trechos resultaram em `NAO_LOCALIZADO`/`PMID_INCORRETO`/`ELEGIBILIDADE_FALHOU` após correção → `"REJEITADA"`.
| Resultados mistos sem aprovação → manter `""` com `ids_auditoria` apontando os trechos pendentes.

> Não usar `VALIDADO`/`CONFIRMADO` como valor de Módulo 09: a validação é sempre **por claim/trecho** (G3), nunca da referência abstrata. O Módulo 09 só agrega.

## 4. O que NÃO fazer (erros a evitar)

- **Não** mover o ledger para dentro do Módulo 09 (voltaria o problema do 1:N e quebraria o schema do Prompt 4.0).
- **Não** criar `06_vinculos.json` em `/Evidencias/Bibliografia/`: o Módulo 09 é definido pelo Prompt 4.0 como 5 arquivos. O ledger mora em `/Auditoria_Bx/`.
- **Não** preencher `pmid_oficial` por inferência. O Schema-Claim v3.1 já decide que doi/título/revista são recuperáveis por busca a partir do PMID; se não há PMID verificado, o campo fica vazio e `citacao_confirmada: false` — e a entrada entra na fila de auditoria.
- **Não** emitir nota GRADE no Módulo 09. GRADE é da síntese da Biblioteca (R04); fonte isolada só carrega `dominios_grade_observados` no claim/ledger.

## 5. Versionamento

Se este delta for adotado, o Módulo 09 passa de "v1.0" (rodapé do Prompt 4.0) para **v1.1**, apenas por adição de campos opcionais — nenhum arquivo existente deixa de ser válido. Recomenda-se registrar a mudança no `historico_correcoes`/changelog do Prompt 4.0 quando ele for revisado, sem necessidade de regenerar Bibliotecas já produzidas.
