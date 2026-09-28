# 08 — Guia de Execução Passo a Passo (operador)

Este guia cobre o pedaço novo do processo — a **auditoria científica de conteúdo** — encaixado no seu PROCESSO DE GERAÇÃO v2.0. As Rodadas 1 e 2 e os dois checklists existentes continuam exatamente como você já roda.

---

## Ordem geral (lembrete)

1. Briefing escrito → Rodada 1 (Molde GPM + Briefing) → `GPM_Bx.md`
2. Checklist de Sanidade do GPM → aprovado
3. Rodada 2 (Prompt 4.0 → IDs+Filosofia+Contrato → Lista Canônica se houver → GPM) → `Biblioteca_Bx.md` + Módulo 09 (5 arquivos)
4. Checklist de Auditoria Estrutural → aprovado estruturalmente
5. **AUDITORIA DE CONTEÚDO (este guia, Passos A–F)** ← etapa antes "a formalizar"
6. Aprovação e integração; atualizar Lista Canônica/Bloco de Estado; arquivar GPM

---

## PASSO A — Preparar a pasta da auditoria

```
mecanismo_Bx_<nome>/
├── Biblioteca_Bx.md            (aprovada estruturalmente)
├── Evidencias/Bibliografia/    (01..05, Módulo 09)
└── Auditoria_Bx/               (criar agora)
    ├── ledger_auditoria_Bx.json
    └── decisoes_Bx.md
```

Inicialize `ledger_auditoria_Bx.json` como `[]`.

## PASSO B — Montar o ledger (mini-rodada de mapeamento)

Em uma sessão nova, forneça: a `Biblioteca_Bx.md`, os 5 arquivos do Módulo 09 e o doc 02 (spec do ledger). Peça:

> "Para cada entrada do Módulo 09, localize TODOS os trechos do corpo onde ela é citada (citação `(Autor, Ano)[tipo]` e âncoras `[REF_BLOCO_XX]`). Gere um objeto do ledger por trecho, com `trecho_ancora` literal, `citacao_literal`, `bloco_origem`, `tipo_classificador`, `origem_entrada` (LISTA_CANONICA se a entrada tem `claim_id_origem`; GPM se veio do GPM; POLITICA_FONTES se declarada complementar), e `status_auditoria: PENDENTE`. Não busque nada externo ainda — só mapeie."

Rode o validador (doc script) para conferir o mapeamento (trecho literal existe, referência existe, classificador bate com o arquivo). Corrija antes de seguir.

## PASSO C — Ordenar a fila de verificação

Prioridade (doc 04, §1):
1. `origem_entrada: GPM/POLITICA_FONTES` com `citacao_confirmada: false` ou "referência a confirmar";
2. `grau_maturidade_cientifica` = `hipotese_inicial`/`emergente`;
3. trechos que alimentam BLOCO_07/BLOCO_08 (síntese de nós/loops);
4. `origem_entrada: LISTA_CANONICA` (só conferir G1 e integridade — não re-julgar G3).

Trabalhe por BLOCO, usando o Briefing do GPM como fonte de termos de busca alternativos.

## PASSO D — Verificar (G1 → G2 → G3), trecho a trecho

Para cada trecho, na sessão de auditoria (pacote mínimo do Como Executar — B1 MEC):

1. **G1:** conferir `pmid_oficial`/DOI no PubMed (esearch/esummary) — ou, se vazio (entrada do GPM), montar a query a partir do trecho + Briefing e rodar a busca. Cole a lista de resultados.
2. **Selecionar** pela heurística oficial: força do desenho (tier 1→4, não a hierarquia clínica meta>RCT) → amostra/replicação independente → recência.
3. **Colar o abstract completo** (ou texto completo se houver gatilho — doc 04, §5). Sem abstract colado, não há G3.
4. **G2:** desenho elegível? Espécie? Contaminação por desfecho de tratamento? Associação puramente clínica → `redirecionados_modulo_clinico`; de outro bloco/mecanismo → `fila_realocacao`; exclusão → `fontes_rejeitadas`.
5. **G3:** as 3 perguntas (pertencimento → suporte causal/aresta → robustez). Decida `APROVADO` / `APROVADO_COM_RESSALVA` / `REJEITADO(NAO_SUSTENTA)` / `INCONCLUSIVO`.
6. Registre tudo no objeto `verificacao` do ledger (query, caso A/B/C, abstract literal, manipulação, contraste, espécie, domínios GRADE observados, data, sessão).
7. Resultado de identificação: `NAO_LOCALIZADO`/`PMID_INCORRETO` → dispare o **resgate único** (doc 04, §4), com query registrada.

Regras que não podem cair: PMID nunca de memória; número só de fonte visível; GPM não é fonte; 4 eixos independentes, nenhum decide sozinho; nada de descartar resultado de query sem registro.

## PASSO E — Fechar a leva e emitir o relatório

- Atualize o **Bloco de Estado** do mecanismo: claims aprovados (preencha Schema-Claim v3.1 completo, com `mapa_exportacao_modulo09`, para os achados novos), rejeitados, `fila_realocacao`, `redirecionados_modulo_clinico`, `resultados_nao_triados`.
- Escreva `Auditoria_Bx/decisoes_Bx.md` no formato do doc 05 (seção G).
- Aplique o **Checklist do doc 05**.
  - Tudo aprovado e sem trecho problemático → pule para o Passo F (integração).
  - Há trechos `NAO_SUSTENTA`/`NAO_LOCALIZADO`/ressalvas/violações → **mini-rodada C**.

## PASSO F — Mini-rodada C (correção) e aprovação final

1. Sessão nova: forneça Prompt 4.0 (trechos) + regra "reconciliar, não pesquisar" + o ledger (só ações ≠ MANTER) + Biblioteca + Módulo 09. Peça para aplicar cada `acao_correcao` (doc 06, §2): manter, sinalizar, rebaixar linguagem, trocar referência, corrigir PMID/metadados, remover trecho.
2. Receba a Biblioteca e o Módulo 09 revisados com a nota linha-antiga → linha-nova.
3. Marque `reconciliado: true` nos trechos; preencha `ids_auditoria`/`status_auditoria` agregado no Módulo 09 (se adotou o delta do doc 03).
4. **Rode de novo o Checklist Estrutural** (a forma mudou) e o validador.
5. Aplique o **Checklist de Aprovação Final (doc 07)**, incluindo o teste de rastreabilidade por amostragem (frase → ledger → Módulo 09 → PMID → abstract).
6. Aprovado:
   - incorpore os claims novos à Lista Canônica; marque `usado_em_biblioteca: sim` nos usados;
   - registre a declaração de aprovação (doc 07, E1);
   - a `Biblioteca_Bx.md` está canônica; arquive o GPM.

---

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---|---|---|
| Trecho sem entrada no Módulo 09 | Citação foi escrita sem registro | Voltar ao mapeamento (Passo B); não criar registro "de memória" |
| Entrada do Módulo 09 não aparece no corpo | Citação removida/órfã | Remover entrada ou registrar motivo |
| PMID não resolve | Entrada do GPM sem verificação / identificador incorreto | `NAO_LOCALIZADO` + resgate; campo vazio preferível a inventado (R04) |
| Artigo existe, mas é associação de população clínica | Natureza epistemológica diferente | `redirecionados_modulo_clinico` — não rejeitar |
| Artigo sustenta outra parte do mecanismo | Achado de outro BLOCO/Bx | `fila_realocacao` com destino oficial |
| Frase diz "causa em humanos", fonte é animal | Linguagem acima da evidência | Ressalva + `[APENAS PRÉ-CLÍNICO]`/extrapolação + rebaixar |
| Mesmo artigo aprova um trecho e reprova outro | Normal (status é por trecho) | Decisão por objeto do ledger; o Módulo 09 só agrega |
| Remoção derruba contagem mínima de referências | Bloco ficou fraco | Não preencher com qualquer fonte; registrar bloco para nova leva de busca (em_busca) |
| IA cita PMID sem abstract na sessão | Viés de memória | Recusar; exigir abstract colado ou esearch/esummary |

## Cadência

- Um mecanismo por vez (regra R12: máximo 1 mecanismo por sessão de geração).
- A auditoria de conteúdo também em sessões dedicadas, por BLOCO, estado salvo ao fim de cada leva (Bloco de Estado versionado).
- B1 é a calibração: o padrão de ledger e de decisões que você firmar aqui vira o molde para B2–B16.
