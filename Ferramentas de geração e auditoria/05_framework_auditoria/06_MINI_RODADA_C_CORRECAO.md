# 06 — Mini-rodada C: Correção Pós-Auditoria (reconciliação Biblioteca + Módulo 09)

**Quando roda:** depois que a auditoria de conteúdo (docs 04–05) resultou em `REQUER MINI-RODADA C`.
**Objetivo:** fazer a Biblioteca e o Módulo 09 refletirem exatamente o que a verificação por fonte encontrou — sem deixar frases não sustentadas sobrevivendo, e sem reabrir o Prompt 4.0 para geração nova.

É uma mini-rodada dedicada (mensagens separadas, como as outras), não edição manual invisível. O gerador recebe o ledger com as decisões e corrige; **não introduz fato, citação ou claim novo** — qualquer necessidade de fato novo volta para a fila (resgate/Lista Canônica).

---

## 1. Entradas

- `Biblioteca_Bx.md` (aprovada estruturalmente)
- Módulo 09 (5 arquivos)
- `ledger_auditoria_Bx.json` com `status_auditoria` e `acao_correcao` definidos
- Bloco de Estado atualizado (claims aprovados/ressalvados, filas)

## 2. As ações de correção (por trecho)

| `acao_correcao` | Quando | O que muda na Biblioteca | O que muda no Módulo 09 |
|---|---|---|---|
| `MANTER` | `APROVADO` | Nada | Entrada fica; `status_auditoria` agregado → `VERIFICADA`; `ids_auditoria` preenchido |
| `ADICIONAR_SINALIZADOR` | ressalva por sistema experimental | Inserir `[APENAS PRÉ-CLÍNICO]` / `[EXTRAPOLAÇÃO POR ANALOGIA: ...]` junto à citação | Preencher `extrapolacao_por_analogia` com o texto idêntico da tag |
| `REBAIXAR_LINGUAGEM` | evidência mais fraca que a redação (associação virou causalidade; "demonstra" virou "sugere") | Reescrever a frase no nível da fonte | `achado_central_molecular` ajustado; nota de ressalva |
| `TROCAR_REFERENCIA` | fonte substituta validada no resgate | Trocar a citação para a referência correta | Corrigir `pmid_oficial`/metadados (ou apontar nova entrada); `citacao_confirmada: true` |
| `CORRIGIR_PMID` / `CORRIGIR_METADADOS` | `PMID_INCORRETO` ou metadado errado, frase sustentada | Citação/âncora ajustada se necessário | Corrigir identificadores; preencher `doi/titulo/revista` via busca |
| `REMOVER_TRECHO` | `NAO_SUSTENTA` sem resgate, ou `NAO_LOCALIZADO` sem fonte | Remover a afirmação; se quebrava uma ligação entre blocos, reescrever a ligação sem a afirmação (nunca deixar frase órfã) | Entrada sem nenhum trecho restante é removida ou marcada; vínculo com claim cortado |
| (nova entrada) | claim novo aprovado na auditoria | A citação passa a usar o PMID/achado do claim | Entrada com `claim_id_origem` preenchido, `origem_referencia: LISTA_CANONICA` |

### Regras de rebaixamento (linguagem espelha evidência)

| Redação acima da evidência | Redação reconciliada |
|---|---|
| "X está documentado em humanos" (só animal) | "X é documentado em modelos animais; em humanos, hipótese [APENAS PRÉ-CLÍNICO]" |
| "X causa Y" (fonte associativa) | "X está associado a Y; causalidade não estabelecida" |
| "O mecanismo está confirmado" (desenho tier_3/4) | "O mecanismo é proposto/sugerido, com suporte preliminar" |
| Frase sem fonte localizada | Remover, ou reescrever como hipótese explicitamente sinalizada (nunca como afirmação) |

## 3. Ordem de execução da mini-rodada

1. **Mensagem 1 — contexto:** colar Prompt 4.0 (trechos de estrutura/citações) + regra: "você vai reconciliar, não pesquisar". Aguardar confirmação.
2. **Mensagem 2 — dados:** colar o ledger (só os trechos com ação ≠ `MANTER`) + a Biblioteca + o Módulo 09. Pedir: aplicar cada `acao_correcao`, sem alterar nada que não esteja apontado, sem adicionar conteúdo.
3. **Mensagem 3 — saída:** Biblioteca_Bx revisada + Módulo 09 revisado + nota de cada alteração (linha antiga → linha nova).
4. O operador confere e marca `reconciliado: true` no ledger.

## 4. Verificação pós-correção

- [ ] Nenhum trecho `NAO_SUSTENTA`/`NAO_LOCALIZADO` sobrevive como afirmação.
- [ ] Toda ressalva tem sinalizador visível no corpo e tag espelhada no Módulo 09.
- [ ] Toda troca de referência aponta para fonte que passou por G1/G2/G3.
- [ ] Nenhuma remoção deixou citação/âncora `[REF_BLOCO_XX]` quebrada ou referência órfã.
- [ ] As âncoras `[REF_BLOCO_XX]` e o Módulo 09 continuam consistentes com o corpo (rodar o validador — doc 08/script).
- [ ] O texto segue com tamanho e blocos mínimos do Checklist Estrutural (uma remoção grande pode derrubar contagem — se cair abaixo do mínimo, o bloco precisa de nova rodada de evidência, não de preenchimento).
- [ ] Claims novos aprovados foram incorporados à Lista Canônica; `usado_em_biblioteca: sim` marcado nos claims efetivamente usados.
- [ ] Rodar o **Checklist Estrutural** de novo (a forma mudou) e depois o **Checklist de Aprovação Final** (doc 07).

## 5. Princípio

A correção não puni o texto — torna a Canônica digna de confiança. Na dúvida entre rebaixar e remover: se a fonte lida **contradiz** ou não existe, remova; se a afirmação é plausível mas a evidência é parcial/animal, rebaixe com sinalizador. Nunca manter formulação mais forte do que a fonte suporta.
