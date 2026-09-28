# PACOTE RODADA 2 — para a perícia externa (2026-09-11)

## Conteúdo
```
RODADA2_PACOTE_PERICIA/
├── README_RODADA2.md               ← este arquivo / mensagem de capa
├── contrato.py                     ← módulo da perícia, INTOCADO (cópia fiel)
├── originais/                      ← os 3 escritores exatamente como estão hoje
│   ├── 07_aplicar_vereditos.py
│   ├── append_vinculos_b1v2.py     ← fonte do bug D1 (ver abaixo)
│   └── _propaga_selos{,2,3}.py
├── blindados/                      ← versões blindadas (validação = portão, lei P-5)
│   ├── append_vinculos_b1v2_blindado.py   (+ b1v2_linhas.json = 30 linhas auditadas)
│   ├── aplicar_vereditos_blindado.py
│   └── propaga_selos_blindado.py
├── testes/autotest_blindagem.py    ← resultado: 6/6 em bancada sintética
├── serie_AT/<Bxx>/*.py             ← 97 scripts das levas [AT] B1–B16 (inventário)
└── bancada_teste/                  ← artefatos sintéticos do autoteste
```

## O que a blindagem fecha (defeito observado → contramedida)
1. **D1 — um parâmetro, dois campos** (`append_vinculos_b1v2.py`, função `V()`):
   escrevia `natureza_relacao=forca` e `forca_causal=forca`. É a origem exata do
   AT-11 e do AT-01 (30 vínculos B1-v2). Na versão blindada, `natureza` é parâmetro
   explícito linha-a-linha + regra **teto-por-tier** (tier_3 não aceita `causal`,
   tier_4 não aceita nada acima de associativa/marcador/nao_estabelecida).
2. **`tier_2_intervencao` (valor fantasma)** — não compila mais: qualquer valor fora
   do enum aborta **antes** de gravar (o autoteste injeta exatamente esse valor e
   prova exit≠0 com o arquivo intacto).
3. **`status_auditoria="G1_G2_G3_B1v2"`** (fora do enum) → enum oficial.
4. **D2 — âncora fabricada**: o gerador blindado valida cada `trecho_ancora` contra
   a Canônica (AUSENTE/VAZIO = bloqueante) antes de gravar.
5. **D4 — escrita sem backup**: os três blindados só gravam via `contrato.gravar`
   (backup datado + escrita atômica); `id` por varredura do máximo `\d{4}` (não `len+1`).
6. **D3 / lei P-5** ("10 dos 36 scripts calculam a lista de problemas, imprimem e
   gravam mesmo assim"): nos blindados a validação É o portão — `abortar_se` com
   exit 1; contagem de examinados sempre impressa.
7. **D1-legado não retorna**: vereditos blindados sobem `status_referencia` para o
   oficial `VALIDADO` (o legado `VALIDADO_G3_IA` foi harmonizado ao vivo hoje;
   regerá-lo reintroduziria a dívida).
8. **propaga_selos blindado**: portões de pré-condição (âncoras literais — o modo de
   falha "selo na frase errada") e pós-condição (sem selo duplicado colado); dry-run
   por padrão.

## Provas
- **Autoteste 6/6** (`testes/autotest_blindagem.py`): caminho limpo grava com backup;
  caminho envenenado aborta sem tocar o arquivo (inclui o fantasma do AT-11 e uma
  âncora fabricada).
- **Round-trip no B1 vivo (cópia de bancada)**: `append...blindado.py` sobre os 257
  vínculos atuais (linhas = estado pós-auditoria) produz **0 registro novo, 0
  bloqueantes, 0 avisos** — o gerador corrigido reproduz exatamente o estado auditado.
- `contrato.py` aceito como lei: **nenhuma linha alterada** pela nossa parte;
  as decisões que pedem ratificação estão em `SCHEMA_V2_PROPOSTA_2026-09-11.md`
  (documento irmão, em `_documentos_serie/`).

## Pedidos à perícia (resumo; detalhe no SCHEMA_V2_PROPOSTA)
Ratificar: traduções pt→oficiais (P5) · `desenho_evidencia` (P1) · extensões
`refutadora`/`nao_aplicavel` (P2/P3) · ids legados 3 dígitos (P4) · decisão F1
(arquitetura B14–B16, sem invenção de dado) · revisar os 3 escritores blindados
e dizer se passam a ser o padrão obrigatório de escrita.

## Nota de auditoria
Pacote montado pelo agente em 2026-09-11 (rodada de harmonização). Originais
preservados verbatim para comparação; blindados derivados com diffs comentados
nos cabeçalhos. Nada foi executado no vivo a partir deste pacote — provas em
bancada sintética e cópia de bancada do vivo.
