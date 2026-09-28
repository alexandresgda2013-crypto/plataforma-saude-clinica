# 01 — Mapa do Processo: onde a Auditoria de Conteúdo se encaixa

Este documento é a bússola. Os demais (02–08) detalham cada parte.

---

## 1. O pipeline completo com a etapa formalizada

```
RODADA 1 (produção do GPM)
  Molde GPM + Briefing(Bx)  →  GPM_Bx.md
        ↓
  [Checklist de Sanidade do GPM]  ── reprova → nova execução
        ↓
RODADA 2 (produção da Biblioteca)
  Prompt 4.0 + _ids_oficiais + Filosofia + Contrato (P12/P16/P17/P19/P20,R04/R06/R12)
  + Lista Canônica aprovada (se houver) + GPM_Bx.md
        ↓
  Biblioteca_Bx.md  +  /Evidencias/Bibliografia/ (Módulo 09: 5 arquivos JSON)
        ↓
  [Checklist de Auditoria ESTRUTURAL da Biblioteca]  ── reprova → correção
        ↓
AUDITORIA CIENTÍFICA DE CONTEÚDO  ◄══ ESTA É A ETAPA FORMALIZADA NESTE PACOTE
  (doc 02 ledger + doc 03 delta + doc 04 protocolo G1/G2/G3 + doc 05 checklist)
        ↓
  MINI-RODADA C — correção pós-auditoria (doc 06: reconciliar Biblioteca + Módulo 09)
        ↓
  [Checklist de Aprovação Final de Conteúdo] (doc 07)
        ↓
APROVAÇÃO E INTEGRAÇÃO  →  Biblioteca_Bx.md passa a ser a fonte canônica do mecanismo
        ↓
  Marcar used claims (usado_em_biblioteca: sim) na Lista Canônica;
  claims novos aprovados na auditoria são incorporados à Lista Canônica;
  GPM_Bx.md pode ser arquivado.
```

---

## 2. Quem faz o quê (papéis)

| Papel | Quem | Produz |
|---|---|---|
| **Gerador** | IA (Prompt 4.0 / Molde GPM) | GPM, Biblioteca, Módulo 09 |
| **Operador** | Humano | Conduz sessões, roda buscas no PubMed, cola abstracts, decide correções |
| **Auditor de conteúdo** | IA em **sessão/mini-rodada separada** + julgamento do operador nos portões G1/G2/G3 | Preenche o ledger, propõe decisões; **nunca** inventa PMID nem aprova sozinho |

Regra-mãe (já sua, nos checklists): **quem gera não audita no mesmo turno.** A auditoria de conteúdo é uma mini-rodada dedicada, como o Checklist de Sanidade e o Estrutural.

---

## 3. As duas trilhas e os dois destinos de um PMID

A auditoria de conteúdo opera sobre a Biblioteca de **mecanismo** (trilha `B1.MEC.*`), mas os PMIDs que ela encontra podem pertencer a outra natureza epistemológica. Os destinos oficiais (Como Executar — B1 MEC) são:

1. **Fica no mecanismo** → claim `B1.MEC.BLOCOxx.nnn`, fonte aprovada/ressalvada.
2. **`redirecionados_modulo_clinico`** → PMID puramente associativo/epidemiológico em população clínica (sem manipulação causal, sem contraste experimental). **Nunca** vai para `fontes_rejeitadas` por esse motivo — é evidência de outra natureza, não de má qualidade.
3. **`fila_realocacao`** → o elo causal é real mas pertence a outro BLOCO do B1 ou a outro mecanismo B2–B16.
4. **`fontes_rejeitadas`** → desenho/exclusão (ex.: ferramenta farmacológica de especificidade contestada sem controle de off-target, preprint sem peer review, artigo retratado, predição in silico sem validação).
5. **`resultados_nao_triados`** → PMIDs retornados e não lidos na leva (registrados, nunca descartados).

---

## 4. Princípios que governam a auditoria (herdados das suas ferramentas)

1. **PMID nunca de memória da IA.** Todo PMID vem de abstract colado na sessão ou verificado via G1 (esearch/esummary). "PMID não verificado nesta sessão = não existe para o sistema."
2. **Abstract obrigatório na sessão para G3.** Número só de fonte visível.
3. **GPM aponta território, nunca substitui G1.** "Referência específica a confirmar" do GPM é só um indicador de busca.
4. **Os 4 eixos de evidência nunca decidem sozinhos.** G3 é julgamento do avaliador sobre as 3 perguntas (pertencimento, suporte causal, robustez) — não fórmula automática.
5. **Campo vazio preferível a dado inventado** (R04).
6. **GRADE não é nota de fonte.** Fonte isolada só registra `dominios_grade_observados`; a certeza final é da síntese da Biblioteca.
7. **A Lista Canônica é a fonte de maior prioridade**, quando existe. O que nela está `aprovado/aprovado_com_ressalva` entra na Biblioteca com o PMID exato — a auditoria só confere integridade, não re-julga.

---

## 5. O que muda nos seus arquivos (e o que NÃO muda)

**Não muda (ferramentas oficiais intactas):**
- Molde GPM, Briefing, Prompt 4.0, Schema-Claim v3.1, Protocolo de Escopo, Como Executar, Lista Canônica, Bloco de Estado, os dois checklists existentes, Contrato/Decisões, `_ids_oficiais`.
- O Módulo 09 continua sendo os **5 arquivos JSON** do Prompt 4.0.

**Passa a existir (artefatos novos da auditoria):**
- `Auditoria_Bx/ledger_auditoria_Bx.json` — o livro-raio da auditoria (doc 02). Uma entrada por **instância de citação** (trecho), não por referência.
- `Auditoria_Bx/decisoes_Bx.md` — relatório por entrada (espelha o Bloco de Estado).
- O **delta mínimo opcional** do Schema de Entrada do Módulo 09 (doc 03): 3 campos novos, todos compatíveis com o schema atual.

**Passa a ser executado (mini-rodadas novas):**
- A auditoria de conteúdo (doc 04) e a mini-rodada C de correção (doc 06), com seus checklists (docs 05 e 07) e guia passo a passo (doc 08).
