# ORGANIZAÇÃO DESTA PASTA (desde 2026-09-10 — pedido do usuário)

- **`atuais/`** — tudo o que é VIGENTE: canônica atual (V2/V4), `Evidencias/`, `Auditoria_*/`,
  `producao/` (insumos, trilhas, matrizes, G1) e os scripts/artefatos da versão vigente.
- **`antigos/historico/`** — versões superadas (V1 e anteriores, pré-canônicas, briefings,
  GPMs de trabalho e relatórios das rodadas antigas). Conteúdo originalmente em
  `producao/historico/` — referências antigas a esse caminho devem ser lidas como
  `antigos/historico/`.

## Invocação dos portões oficiais NOVO layout (a pasta alvo agora é `atuais/`)
```
cd "BIBLIOTECAS/B11_DisfuncaoTireoidiana/atuais"
python3 "<Ferramentas>/scripts/gate_script.py" .
python3 "<Ferramentas>/scripts/checklist_entrega.py" . <Bn>   # ex.: B16 (sem zero à esquerda)
python3 "<Ferramentas>/05_framework_auditoria/scripts/validar_auditoria.py" . \
  --biblioteca "./<CANONICA>.md" --ledger "./Auditoria_<Bn>/ledger_auditoria_<Bn>.json"
```
Rastreio da mudança: `BIBLIOTECAS/CHANGELOG_GERAL.md` (entrada 2026-09-10 · reorganização).
Regra vigente (IMPL-AT-10): qualquer alteração exige nota datada no artefato + CHANGELOG.
