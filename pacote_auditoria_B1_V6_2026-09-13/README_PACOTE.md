# PACOTE DE AUDITORIA — B1 Neuroinflamação · CANÔNICA V6 · 2026-09-13 (pós-rodada 2 do ciclo bilateral)

**Destinatário:** segundo agente auditor (análise da plataforma documento a documento).
**Conteúdo:** exatamente o que foi pedido — `/Evidencias/` (Módulo 09 nível 1 + arquivo de vínculos),
mais os dois programas de portão que a casa roda (gate P-5 e framework `validar_auditoria`) — **acrescidos
do mínimo necessário para você re-rodar tudo de forma autocontida** (a canônica V6, o ledger e as saídas
frescas). Tudo verificado hoje, direto dos arquivos — contagens abaixo.

## Conteúdo e estado (medido hoje)

| Item | Arquivo(s) | Estado medido |
|---|---|---|
| Canônica (fonte única da prosa) | `canonica/B1 NEUROINFLAMAÇÃO V6 CANONICA.md` | sha256 **e11dbd95…** (errata mesmo dia: H1 V5→V6; intermediário d8f41662… no histórico da casa; sem toque científico) |
| Módulo 09 nível 1 (referências) | `Evidencias/Bibliografia/01_pmids.json` (200) · `02_meta_analises.json` (34) · `03_ensaios_clinicos.json` (3) · `03_ensaios_clinicos.md` · `04_atualizacoes_literatura.json` (0) · `05_manuais_e_livros.json` (0) · `_manifesto_biblioteca.json` (v2.7) | **237 refs** (200+34+3) = o que o manifesto declara; **34 meta-análises** incl. **REF_OSIMO_2019** (trilha [AT] desta rodada; PMID 31258105, eutils real) |
| Vínculos frase↔referência (N2) | `Evidencias/Vinculos/vinculos_referencia_afirmacao.json` | **274 vínculos** |
| Ledger de auditoria (N3) | `Auditoria_B1/ledger_auditoria_B1.json` | **237 entradas** (237 = refs; cada decisão com objeto `verificacao`) |
| Decisões datadas | `Auditoria_B1/decisoes_B1.md` | rev.5 + adendo 5a (a errata do título) |
| Gate P-5 (programa, stdlib pura) | `ferramentas/gate_script.py` | roda com `python3 gate_script.py <pasta_atuais>` |
| Framework de auditoria (programa, stdlib pura) | `ferramentas/validar_auditoria.py` | roda com `python3 validar_auditoria.py <pasta_atuais> --biblioteca "B1 NEUROINFLAMAÇÃO V6 CANONICA.md" --ledger Auditoria_B1/ledger_auditoria_B1.json` |
| Saídas frescas (geradas sobre esta V6, com este sha) | `saidas/gate_P5_2026-09-13.txt` (**APROVADO**) · `saidas/checklist_2026-09-13.txt` (**41/41**) · `saidas/framework_validar_auditoria_2026-09-13.txt` (**0 ERRO / 236 AVISO**) · `saidas/P8_coerencia_camadas_2026-09-13.txt` (**0 ERRO / 25 AVISO** — incluída de contexto; o P-8 é o portão novo do ciclo, NÃO faz parte do pedido, mas os números de V-02=0 referem-se a ele) | reproduzíveis re-rodando |

## Como re-rodar (layout esperado)

Os programas esperam a estrutura da pasta `atuais/`. Para reproduzir:

```
mkdir atuais && cd atuais
cp ../pacote_auditoria_B1_V6_2026-09-13/canonica/*.md .
cp -r ../pacote_auditoria_B1_V6_2026-09-13/Evidencias .
cp -r ../pacote_auditoria_B1_V6_2026-09-13/Auditoria_B1 .
python3 ../pacote_auditoria_B1_V6_2026-09-13/ferramentas/gate_script.py .
python3 ../pacote_auditoria_B1_V6_2026-09-13/ferramentas/validar_auditoria.py . \
  --biblioteca "B1 NEUROINFLAMAÇÃO V6 CANONICA.md" --ledger Auditoria_B1/ledger_auditoria_B1.json
```

## Avisos conhecidos (nada escondido)

- **Framework: 236 avisos, 0 erros.** 235 são as `citacao_literal` por TOKEN (`SOBRENOME_ANO[TAG]`) em vez de
  citação literal — dívida nomeada L-13 (detector de deriva ledger×texto E o V-10 do P-8 ficam mudos até lá);
  prioridade máxima do próximo pacote de trabalho. +1 aviso informativo.
- **Gate [6]:** 39 claims de alto risco sem `segunda_verificacao` — ressalva de fase 1-operador **declarada**;
  a 2ª verificação cega é o portão humano P-6, que por decisão do operador acontece na revisão final da
  plataforma (delegação registrada em `decisoes_B1.md` rev.5).
- **P-8 (contexto):** V-06 tem 18 avisos (qualificador da prosa não propagado ao `g3`/achado — dívida
  D-B1-R3-G3NOTA) e V-08 tem 5 (números em prosa editorial do REGISTRO/rótulo, não científicos).
- **Backups `.bak_*` das fichas ficam na casa** (não incluídos para não poluir); a V5 e a V6-intermediária
  estão em `antigos/historico/` na casa, com sha registrado no manifesto (`historico_sha_v6`).

— Gerado pela IA da casa em 2026-09-13 · cada arquivo tem hash em `SHA256SUMS.txt`.
