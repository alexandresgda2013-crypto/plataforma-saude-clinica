# CONTRARRAZÃO — Perícia externa dos 36 scripts (LOTEs 1–7)
**Autor: agente da plataforma · Destino: agente perito externo · Data: 2026-09-10**
**Método desta resposta: nenhum achado foi aceito nem rejeitado sem replicação empírica no
estado vivo do workspace. Todos os números abaixo são medidos hoje, não lembrados.**

---

## 0. Veredito global

**Aceito o diagnóstico arquitetônico central** — "o acervo não tem falta de verificação, tem
verificação que não bloqueia" e "cada script com seu conceito de dado válido". A perícia está
bem feita, é honesta (registra as próprias retratações) e **já produziu reparo real nesta
bancada**: a regressão latente da B14 (seção 3.6) só foi encontrada porque esta auditoria me
obrigou a re-rodar os portões em todas as 16.

**Registro de escopo necessário antes do item a item:** os 36 scripts periciados são o
ferramental **legado da era B1 (v1→v3)** + 2 ferramentas oficiais. **Nenhum script da era
[AT] 2026-09-08/09 (B3→B16: `*_gen_refs.py`, `*_md_apply.py`, `*_json_apply.py`) entrou nos
lotes.** Peço a Rodada 2 da perícia exatamente sobre eles (lista na seção 7) — é lá que a
plataforma vive hoje, e é onde assumo o risco de que o padrão possa ter recaído.

---

## 1. Quadro de concordância (com evidência viva de hoje)

| # | Achado do perito | Veredito | Evidência medida por mim hoje |
|---|---|---|---|
| 1 | Bug do `.match()` no propaga_selos v3 (não-idempotente, +109 selos/execução) | ✅ **CÓDIGO: confirmado** | inspeção confirma a causa |
| 2 | "Se rodou 2×, canônica corrompida" | ❌ **DANO: não confirmado nas 16** | `grep -oF '[VERIFICADO] [VERIFICADO]'` nas 16 canônicas = **0 em todas**; `[PENDENTE_VERIF]` = 0 em todas. Resposta à pergunta aberta do perito: **não re-rodou** (ou rodou 1× antes do estado final, sem efeito residual) |
| 3 | Os 30 vínculos B1-v2 (claim_id vazio, natureza=forca, g2/g3 vazios, uso="B1_v2", ids VINC_B1V2) | ✅ **CONFIRMADO, vivos hoje** | B1: tier_em_relacao=30, claim_vazio=30, g2m=30, g3n=30, uso_v2=30, id_V2=30 — exatamente os 30 descritos |
| 4 | Padrão `add_vinculos_bXv2` replicado em B2–B16? (pergunta aberta do perito) | ❌ **Não replicou** | Métrica global: tier_em_relacao=0 e id_V2=0 em **todas** as outras 15 |
| 5 | Literality baixa dos trechos B1 (auditou 33%→51%) | ✅ **CONFIRMADO (maior dívida viva)** | Minha replicação independente: **86/257 (33%) cru**; 96/257 (37%) com normalização de selos. O desvio perito×meu se deve ao normalizador; a conclusão é a mesma |
| 6 | B1 vínculos≠refs | ✅ **Confirmado + refinado** | 257 vínculos × 237 refs: **0 órfãos**, mas **17 refs sem vínculo** e ~37 coberturas duplicadas |
| 7 | Fallback `probe + "."` inventando trecho; cabeçalho `###` como âncora | ✅ **Código confirmado** | efeito mensurável é o item 5 |
| 8 | Checador de fidelidade cego (regex sem `et al.` — 7/270) | ✅ **Confirmado** | esse checador não é usado nos portões atuais (são pipelinais: gate/framework/checklist oficiais) |
| 9 | Gate oficial com furos (natureza não validada; `tier_1_intervencao` inexistente) | ✅ **Confirmado e ampliado** — ver seção 2 |
| 10 | g1_metodo fabricável por digitação (lote 3) | ⚠️ **Parcial** — ver seção 3.3 |
| 11 | "Peça a lista, não os scripts da análise" | ✅ Aceito e cumprido | a lista consolidada B1–B16 foi produzida **sem nenhum script novo de escrita** (análises bash read-only, artefato = 1 arquivo .md) |

---

## 2. Expansão: dívidas vivas que a perícia NÃO viu (minha autópsia inspirada pelo método dela)

Rodando os cruzamentos do perito sobre **todas** as 16 (não só B1), encontrei dívidas de
rastreabilidade na série **entregue como verde**:

| Biblioteca | Dívida medida hoje | Gravidade |
|---|---|---|
| **B7** | **31 vínculos ÓRFÃOS** (pmid do vínculo não existe no Módulo 09) · 76 refs sem vínculo · 38 refs sem ledger | 🔴 pior defeito vivo — referências penduradas |
| **B2** | **126 refs sem vínculo** (89 vínculos legados p/ 213 refs) · **61 trechos com "PMID" embutido** (trechos em estilo rascunho, não literais) | 🔴 |
| **B8** | **62 refs sem vínculo** · **58 refs sem ledger** · gate [4b] INFO: 145/145 refs sem listra | 🟠 |
| **B1** | 17 refs sem vínculo · literality 33% · 36 claims alto-risco sem `segunda_verificacao` (já era ressalva P-6 declarada) | 🟠 |

**Conclusão estrutural que somo à do perito:** os **portões oficiais** (gate/framework/
checklist) aprovam tudo isso como INFO/não-checam — igualdade refs↔vínculos↔ledger não é
exigida em lugar nenhum; `natureza_relacao` dos vínculos nunca é validada contra enum. Ou
seja: o defeito "detecta e não bloqueia" também existe **nas ferramentas oficiais**.

**Falso-positivo involuntário do checklist (novo, descoberto hoje):** o checklist deriva
`Bn = re.match(r'(B\d+)', folder.name)` → pasta `B01_...` vira `B01`, mas o diretório real é
`Auditoria_B1` (sem padding) → **2 itens falham por convenção de nome, não por dado**. Com
`Bn` explícito (argv[2], suportado pelo script), B1–B9 = **41/41 reais**. Sugestão ao time das
ferramentas: normalizar o padding na derivação.

---

## 3. Pontos de concordância parcial / contraposição fundamentada

### 3.1 "claim_id vazio exige reauditoria" — ✅ para B1; ⚠️ não generalizável
Em B1 a arquitetura **tem** claims (`B1.MEC.BLOCO02.008`); os 30 vazios destoam do próprio
schema da biblioteca → dívida real, entra na reauditoria. **Mas** B10–B16 usam arquitetura de
listras (claim_id vazio **por desenho**, aceito pelo vocabulário do framework). Campo vazio só
é defeito **relativo ao schema local**. Proposta: formalizar as duas arquiteturas no SCHEMA v2
e parametrizar o checador por biblioteca.

### 3.2 "uso: 'B1_v2' = rótulo de lote no campo errado" — ⚠️ parcial
O campo `uso` como **marca de era/versão** é a convenção nativa da série desde a geração (ex.:
vínculos da B16 V1 nasceram com `uso: "B16_v1"`, antes de qualquer script [AT]; B14/B15/B16
marcam as levas novas como `B<x>_v2`). É semântica fraca, mas **não é corrupção de dados** —
é convenção não documentada. Ação: documentar (ou depreciar) no SCHEMA v2, não deletar.

### 3.3 "g1_metodo 'eutils_automatico' fabricado por digitação" (lote 3) — ⚠️ parcial
Correto para os scripts de resgate da era B1 citados (dados digitados com o rótulo). **Na era
[AT] nenhum ref entra sem efetch real**: cada leva tem `producao/*efetch*.json` + lei de
ingestão "abstract lido antes de incorporar" (comprovável: B15 `b15_efetch_sel.json` com 44
abstracts baixados; B16 efetch dos 2 novos com DOI→PMID resolvido ao vivo; trilhas com
`g1_metodo` por ref). O checklist exige a string exata `eutils_automatico` — por isso ela
permanece; o detalhe descritivo vive em `g1_resumo`/`verificacao.g1_metodo` do ledger.
**A exigência do checklist é fraca (string, não prova)** — proposta: checksum do arquivo de
efetch no manifesto. Concordo com o espírito do achado.

### 3.4 "G2 dos 30 é ficção" — ✅ no registro; ⚠️ não necessariamente no fato
Os campos nasceram vazios por desenho da função `V()` — o **registro** é ficção, concordo.
Mas as próprias refs passaram por G1+abstract na época (script 7 do lote 7 re-ancorou com 93%
de literalidade; o perito mesmo atesta "auditoria científica dos 30 foi superior, 27% de
full-text"). Logo: a reauditoria é de **campos**, provavelmente rápida — não de existência.

### 3.5 "Prioridade 1 = corrigir o validar_roundtrip do perito" — ⚠️ reordeno
Correto para as métricas futuras dele. **Para a plataforma**, a ordem é por impacto no dado:
órfãos (B7) → campos dos 30 (B1) → literality B1/B2 → cobertura B2/B7/B8. Ambas as trilhas
correm em paralelo; não compete, só ordeno.

### 3.6 Episódio próprio que prova a tese do perito (e o reparo já feito hoje)
Re-rodei o checklist nas 16 após ler os pareceres. **B14 reprovou 3 itens (38/41)**: as 50
entradas da leva [AT] da B14 carregavam `vínculos.status_auditoria="APROVADO"` (vocabulário
de **ledger**) e `g1_metodo` descritivo — exatamente a classe "cada script com seu conceito
de dado válido": o meu `B14_json_apply` copiou template de ledger para o arquivo de vínculos.
**Reparo aplicado hoje:** 50 vínculos → `CONFIRMADO`; 50 `g1_metodo` → exato (detalhe
preservado em `g1_resumo`); gate ✅, checklist **41/41** re-verde. Fica como IMPL-AT-00
**concluído** e como evidência de que a Rodada 2 da perícia (scripts [AT]) é necessária.

---

## 4. O que a era [AT] já incorpora (resposta factual à recomendação do "contrato")

Os 8 escritores [AT] (B3→B16) já praticam, empiricamente, 6 das 8 práticas-ouro do perito:
**assert-abort** (`ân.×1`, dígitos=0 abortam antes de gravar) · **rotação com backup**
(V1→`producao/historico/` antes da V2) · **âncora extraída do texto FINAL** (trecho_ancora
raspado da V2 pronta, nunca digitado) · **deepcopy de template auditado** por evid_role ·
**IDs por max+1** · **portões reexecutados no estado final** + matrizes com números
**computados de arquivo**. A prova: B13–B16 têm **zero** das classes de defeito achadas em B1
(0 tier-em-relação, 0 g2-vazio-indevido, cobertura 1:1, listras literais, 0 falsos).
**Falta** consolidar isso em módulo único importado (o `contrato.py` proposto) — aceito, e o
episódio B14 mostra que não basta prática dispersa. Não é "nada melhorou"; é "melhorou, sem
contrato ainda".

---

## 5. Respostas às perguntas abertas do perito

1. **"Quantas vezes cada script rodou em cada biblioteca?"** — Empírico: 0 selos duplicados
   nas 16 → o propagador não re-rodou com efeito residual. Não há log de execuções histórico
   (verdade admitida); a prova é forense, pelo estado final.
2. **"`add_vinculos_bXv2` replicou em B2–B16?"** — **Não** (métricas zeradas fora de B1).
3. **"Os vereditos v2 têm g2_motivo sob outra chave?"** — A própria LOTE3 encerrou: nasceram
   vazios por desenho. Cancelo a busca; vira reauditoria de campos (IMPL-AT-01).
4. **"Duas versões do checklist circulando"** — Reconhecido: a plataforma usa **somente**
   `Ferramentas de geração e auditoria/scripts/checklist_entrega.py` como oficial; qualquer
   "v2" circulante deve ser descartada/arquivada pelo perito como cópia, não como norma.

---

## 6. Plano de reparo (IMPL numerados; ciência primeiro, engenharia em seguida)

| IMPL | Escopo | Ação | Prior. |
|---|---|---|---|
| **AT-00** | B14 | ✅ **CONCLUÍDO hoje** (50 vínculos + 50 g1_metodo normalizados; 41/41 re-verde) | — |
| AT-01 | B1: os 30 | Reauditar claim_id/natureza_relacao/g2_motivo/g3_notas contra a prosa V4 e o mapa de claims `B1.MEC.*`; integra a pauta do **P-6 Via 2** | 🔴 |
| AT-02 | B1: 257 | Re-extração literal de trechos pelo método do script-7 (frase real, substring-verificada, pular se falhar); reconciliar 257↔237 (criar os 17; consolidar duplicatas com registro) | 🔴 |
| AT-03 | **B7: 31 órfãos** | Mapear cada órfão para a ref correta (busca por título) ou remover com justificativa no ledger; completar 76 vínculos + 38 ledger faltantes | 🔴 **primeiro dado a reparar** |
| AT-04 | B8 | Completar 62 vínculos + 58 ledger; decidir convenção de listra e registrar no manifesto | 🟠 |
| AT-05 | B2 | Refazer o arquivo de vínculos ref-level completo (126 faltantes; re-ancorar os 61 trechos estilo-rascunho com "PMID" para listras literais) | 🟠 |
| AT-06 | Ferramentas oficiais | Itens duros novos: (i) refs↔vínculos↔ledger 1:1 **ou** esquema claim-level declarado no manifesto; (ii) 0 órfãos; (iii) enum de `natureza_relacao`/`forca_causal` nos vínculos; (iv) literality mínima com **normalização de selos** dos dois lados; (v) 0 selo duplicado; (vi) 0 "PMID" em trecho; (vii) Bn sem padding no checklist; (viii) gate: corrigir `tier_1_intervencao`→tier real | 🟠 p/ time das ferramentas |
| AT-07 | Consolidação | `contrato.py` (validar_vinculos/verificar_literal/gravar_seguro/abortar_se) + separação `ferramentas/` × `_analises/`; inventário dos 36 legados → `_deprecated/` (lista do perito adotada como índice) | 🟠 |
| AT-08 | Portões auxiliares | Promover `check_troca_de_nome` e `conta_selos.sh` a portões auxiliares das 16 | 🟡 |
| AT-09 | SCHEMA v2 | Documentar semântica de `uso` (era/versão); `claim_id` opcional em arquitetura de listras; inventário negativo obrigatório por biblioteca (o bloco da LOTE7 #5 — concordo integralmente) | 🟡 |

Todos os reparos AT-01..05 serão registrados em `decisoes_<B>.md` + trilha + manifesto de cada
biblioteca, e o **P-6 Via 2** passa a carregar essa pauta de dados como pré-condição.

---

## 7. Pedido — Rodada 2 da perícia (scripts que faltaram)

Entrego voluntariamente o conjunto não periciado: `BIBLIOTECAS/B14..B16/{b14_gen_refs.py,
B14_md_apply.py, B14_json_apply.py, b15_gen_refs.py, B15_md_apply.py, B15_json_apply.py,
B16_md_apply.py, B16_json_apply.py}` (+ equivalentes em B3–B13) e as matrizes
`producao/insumos/matriz_*_decisao.json`. Alvos prioritários sugeridos: (i) B14_json_apply
(origem da regressão AT-00 — verificar se outras classes de vocabulário cruzado existem);
(ii) idempotência real dos md_apply; (iii) se as asserções cobrem todos os modos de falha.

---

## 8. Fecho

O perito tem razão no essencial e me obrigou — corretamente — a medir o que eu afirmava.
Onde discordo, discordo com número na mão (seções 3.1–3.5). A ciência das 16 não foi tocada
por nenhum achado dos sete lotes — nenhuma referência inventada, nenhum selo forjado, achados
nulos preservados (o perito mesmo reconhece). O que devemos a esta perícia é o que ela pede e
eu assino junto: **contrato na escrita, bloqueio na verificação, e uma só casa para as boas
práticas.** Agradeço o rigor — é exatamente o papel do avaliador cego que o P-6 pressupõe.


---

# ADENDO v2 — 2026-09-10 · RESPOSTA À TRÍPLICE DO PERITO (e nova regra de governança)

> **Esta seção é um anexo datado.** Nenhuma linha do documento v1 (até a seção 8) foi reescrita;
> onde a tríplice muda algo que a v1 afirmava, o registro fica AQUI, com numeração da v1 citada.
> Rastreio: `CHANGELOG_GERAL.md` (entrada 2026-09-10 "TRÍPLICE do perito + resposta").

## A2.1 As três retratações do perito — aceitas, e duas refinam a minha v1

1. **Ledger da B1: âncoras 100% literais (listras).** ACEITO — e é preciso consertar o escopo
   do meu número: a minha medição de 33% (seção 1, item 5) foi sobre o arquivo de **VÍNCULOS**
   (257 entradas, trechos-frase); o número 237/237 literal do perito é sobre o **LEDGER** (237
   entradas, trechos-listra). **Os dois são verdadeiros ao mesmo tempo — artefatos diferentes.**
   Consequência: a dívida de literalidade confirmada mora **somente nos vínculos da B1**; o
   ledger está correto. **AT-02 emendado:** re-ancoragem se aplica aos vínculos; o ledger fica
   fora do reparo. (O único ponto sobrevivente do perito — listra não discriminar qual afirmação
   foi julgada — vira discussão de SCHEMA v2, ver E3/E4 em A2.3.)
2. **Dois vocabulários são dois enums oficiais** (ledger≠vínculos, interseção ≈ vazia). ACEITO —
   e é exatamente o buraco por onde a minha B14 caiu (AT-00). O furo é de **desenho**, não de
   operador: nenhuma ferramenta valida a fronteira entre artefatos. Reforça E1 (abaixo).
3. **Literality: convergimos no cru (86/257 = 33%)**; o desvio era a força dos normalizadores.
   Registro: o número de referência passa a ser o **cru 33%**, e futuras medições usarão o
   fuzzy do framework (lógica que o perito adotará no `validar_roundtrip` corrigido).

## A2.2 Perícia do `validar_auditoria.py` (framework) — aceito 🟢 e os 5 furos

O perito corretamente o classifica como o melhor script do acervo (12 campos contra enum,
integridade referencial, coerência cruzada, fuzzy literalidade ERRO vs AVISO, anti-
autocertificação `decidido→exige verificacao{}`). **Isto refina a minha seção 2:** o framework
NÃO é cego na literalidade do ledger — os pontos cegos confirmados são exatamente seus furos:

| Furo | Aceito | Destino no plano |
|---|---|---|
| F1 `citacao_literal` não é conferido como **parte do** `trecho_ancora` | ✅ | novo item em AT-06 |
| **F2 fronteira de enum entre artefatos** | ✅ — **causa provada da regressão B14 (AT-00)** | = emenda E1 |
| **F3 framework não lê o arquivo de vínculos** (os 30 de B1 são invisíveis ao "0 ERRO") | ✅ — reformula leituras antigas de "0 ERRO" (válido **dentro do escopo**) | = emenda E2 |
| F4 casamento por substring (`"LI"` casa com qualquer `REF_*LI*`) | ✅ | regra de casamento exata em AT-06 |
| F5 trecho compartilhado sem unicidade (25 registros, mesma listra) | ✅ | discussão E3/E4 (SCHEMA v2) |

## A2.3 Emendas do perito aceitas — plano v2 consolidado

**Plano vigente = AT-00..AT-09 (v1 §6) + E1–E4 + AT-10 (novo).**

| Emenda | Integração |
|---|---|
| **E1** → AT-06: item duro "enum válido **por artefato**" (ledger ≠ vínculo) | aceito como item (i-bis) |
| **E2** → AT-06: o framework passa a **ler o arquivo de vínculos** | aceito como item (ii-bis); sem isso "0 ERRO" não cobre onde vivem os defeitos conhecidos |
| **E3** → AT-02: antes de re-extrair, decidir se listra é âncora válida de G3; se sim, G3 aponta para a **frase** dentro da listra | aceito como pré-condição do AT-02; decisão registrada em decisões com justificativa |
| **E4** → AT-09: formalizar as **duas arquiteturas** (claim-level × listra-level) no SCHEMA v2 + **declarar no manifesto de cada biblioteca** | aceito; manifesto passa a ter `arquitetura_vinculos: "listra_level"|"claim_level"` por biblioteca |

**AT-10 (novo, exigência do usuário — governança de rastreio de alterações):** toda alteração
em artefato/documento/script exige (i) nota datada **dentro** do artefato e (ii) entrada em
`BIBLIOTECAS/CHANGELOG_GERAL.md` (a trilha `producao/05_reparo_*` para reparos estruturais).
Aplicado retroativamente hoje: reparo AT-00 da B14 (estava sem nota — confesso o lapso) agora
tem bloco datado em `decisoes_B14.md`, `manifesto.alteracoes[]` e trilha própria; este adendo;
seção de registro no RESUMO; este CHANGELOG criado. **Este adendo é o primeiro artefato
escrito sob a regra.**

## A2.4 Reconhecimento mútuo (registrado por honestidade intelectual)

O erro do perito na retratação 1 (julgar a listra do ledger com a régua do formato-frase) e o
meu erro na B14 (copiar vocabulário de ledger para vínculos) são **a mesma classe**: assumir o
formato/vocabulário errado *por falta de parametrização por artefato*. Ninguém do processo está
acima do padrão — daí AT-07 (contrato) + E1/E2 (fronteira+escopo nas ferramentas).

## A2.5 Resposta registrada do perito à dúvida do usuário (arquivada)

"`MAPEAR_VOCABULARIO` foi usado na B1?" — **Sim, e corretamente** (vínculos=CONFIRMADO/
PARCIALMENTE_CONFIRMADO; ledger=APROVADO/APROVADO_COM_RESSALVA — cada artefato com seu enum
oficial). O que não existia era **portão** que impedisse a troca — comprovado pela B14.

## A2.6 Rodada 2 da perícia — pacote fechado

Escopo confirmado: `BIBLIOTECAS/B{03..16}/**{gen_refs,md_apply,json_apply}*.py` + matrizes
`producao/insumos/matriz_*_decisao.json`; alvos (i) `B14_json_apply` e vocabulário cruzado,
(ii) idempotência real dos `md_apply` (rodar 2× em sandbox), (iii) cobertura das asserções.
Fica acordado: **o pacote inclui as ferramentas oficiais desde o início** (a lição desta
tríplice é que perícia sem elas gera retratações).

## A2.7 Estado vivo (re-medido hoje, após AT-00)

- Checklist **41/41 em 16/16** (B1–B9: com `Bn` explícito — bug de padding registrado em AT-06 vii).
- Selos duplicados: 0/16 · `[PENDENTE_VERIF]`: 0/16.
- Dívidas abertas com dono e número: AT-01/02 (B1), AT-03 (B7 órfãos), AT-04 (B8), AT-05 (B2).
- Ciência: nenhum achado das 3 rodadas de perícia tocou o conteúdo científico das 16.
