# PARECER — Scripts de corpus/auditoria, lote 2 de 5
**Perícia contra os dados reais da B1.** 10/09/2026

---

# 1. Quadro de veredito

| # | Script | O que faz | Veredito |
|---|---|---|---|
| 1 | `03_efetch_abstracts` | Baixa abstracts do PubMed | 🟢 **Muito bom** — o melhor script visto até agora |
| 2 | `04_busca_ancoras` | esearch dirigido por rótulo | 🟡 **Correto, mas com 1 risco sério** |
| 3 | `consolida_pre_canonica` | Junta checkpoints na Canônica | 🔴 **Aqui nasce o defeito v2** |
| 4 | `prepara_lote_G2G3` | Planilha/JSONL para o avaliador | 🟢 **Bom desenho** |
| 5 | `aplica_vereditos` | Grava G2/G3 nos vínculos | 🔴 **Escrita sem validação — o executor do dano** |

---

# 2. 🔴 ACHADO PRINCIPAL: encontrei a origem do lote v2

Cruzei os campos que o **script 5** escreve com os 257 vínculos reais:

| Campo | Lote v2 (30) | Resto (227) |
|---|---|---|
| `g2_elegibilidade` | 30/30 ✅ | 227/227 |
| `status_auditoria` | 30/30 ✅ | 227/227 |
| `forca_causal` | 30/30 ✅ | 227/227 |
| `verification_status` | 30/30 ✅ | 227/227 |
| `g3_verificado_por` | 30/30 ✅ | 226/227 |
| **`g2_motivo`** | **0/30** ❌ | 227/227 |
| **`g3_notas`** | **0/30** ❌ | 227/227 |

Olhe o código do script 5:

```python
v["g2_motivo"] = d["g2_motivo"]      # KeyError se faltar
v["g3_notas"]  = d.get("nota","")    # silencioso
```

`g2_motivo` usa acesso direto — se o veredito não tivesse a chave, **estouraria**. Não estourou, logo veio presente **e vazio**. E `g3_notas` usa `.get(...,"")`, que engole a ausência sem ruído.

**Conclusão: os arquivos de veredito da rodada v2 vieram com esses dois campos vazios, e o script gravou o vazio sem reclamar.** Não foi o agente que "esqueceu" — foi o script que aceitou.

## A prova que fecha o caso

Filtrei por `g3_verificado_por` = `IA_G3_rodada_auditoria_cientifica`: **31 vínculos, não 30.**

O 31º é `VINC_B1_0030` — mesma rodada, mesmo dia, mesmo auditor, e está **perfeito**: `claim_id` = `B1.MEC.BLOCO02.008`, `natureza_relacao` = `associativa`, `uso` = `contexto_mecanistico`.

> **Isso derruba a hipótese de "agente com dialeto próprio".** O mesmo auditor, na mesma rodada, produziu 1 vínculo correto e 30 defeituosos. A diferença não está em quem auditou — está no **caminho de escrita**: os 30 entraram por um arquivo de veredito malformado que nenhum script validou.

E `natureza_relacao == forca_causal` em **30/30** confirma: alguém copiou uma coluna na outra ao montar o veredito, e o script 5 gravou.

---

# 3. 🔴 Script 5 — escreve sem validar nada

Além do que já mostrei, três defeitos:

**(a) Nenhuma validação de enum na escrita.** Grava `d["status"]`, `d.get("forca")`, `d.get("vs")` direto no JSON. Se o veredito disser `tier_2_intervencao`, entra. Um `assert` de 4 linhas contra o `SCHEMA_VINCULO_v1.json` teria bloqueado o lote inteiro.

**(b) `contagem[d["status"]] = contagem.get(...)` mascara status inválido.** O dicionário é pré-inicializado com os 5 válidos, mas o `.get` aceita qualquer chave nova. O relatório final imprime o status inventado como se fosse categoria legítima.

**(c) Não faz backup e sobrescreve os três JSONs.** Se o veredito estiver ruim, a versão anterior se perdeu. Combinado com (a), é a receita exata do que aconteceu.

**(d) `faltando` é reportado mas não bloqueia.** Imprime "faltando veredito: [...]" e sai com código 0. Sucesso aparente.

**Correção mínima:**

```python
SCHEMA = json.load(open('canonico/SCHEMA_VINCULO_v1.json'))
OBRIG = ['g2_motivo','g3_notas']
erros = []
for vid, d in ver.items():
    for c in OBRIG:
        if not str(d.get(c,'')).strip(): erros.append(f'{vid}: {c} vazio')
    for campo, chave in [('status_auditoria','status'),('forca_causal','forca'),('verification_status','vs')]:
        val = d.get(chave)
        if val and val not in SCHEMA['enums'][campo]:
            erros.append(f'{vid}: {campo}={val} fora do enum')
if erros:
    print(f'ABORTADO: {len(erros)} vereditos inválidos'); print(*erros[:20], sep='\n')
    sys.exit(1)
```

Mais backup antes de gravar. **Isso teria impedido os 6 dias de invisibilidade.**

---

# 4. 🔴 Script 3 — três problemas graves

**(a) `limp_pmid` altera o `trecho_ancora` DEPOIS que ele foi extraído.**

```python
v['trecho_ancora'] = limp_pmid(v['trecho_ancora']).strip()
```

O trecho deixa de ser cópia literal do corpo. Se a mesma limpeza não for aplicada idêntica à prosa, a literalidade quebra — e literalidade é o alicerce da rastreabilidade. **Suspeito que essa seja a origem dos 140 trechos que só casaram por prefixo** no `validar_roundtrip.py`.

**(b) `id_vinculo` é reatribuído por posição:**

```python
for i,v in enumerate(n2,1): v['id_vinculo']=f'VINC_B1_{i:04d}'
```

O ID depende da ordem do `glob`. Rodar de novo com um arquivo a mais **renumera tudo** — e qualquer referência externa a `VINC_B1_0057` passa a apontar para outro vínculo. IDs devem ser estáveis e derivados do conteúdo, nunca da posição.

**(c) `extras` hard-coded dentro da função `ancora()`** — 17 IDs de referência escritos à mão para os blocos 1 e 8, com o comentário *"garante suas refs"*. Isso é remendo, não regra. Em outra biblioteca não existe.

Menor, mas revelador: `fix={3:(...)}` renomeia o título do BLOCO_03 por substituição literal. Se o título mudar um caractere, falha silenciosamente.

---

# 5. 🟢 Script 1 — o melhor do conjunto

Elogio com fundamento:

- **Retry com backoff** (`time.sleep(2 * tent)`) e respeito ao limite do NCBI
- **Lotes de 100** — uso correto do efetch
- **Log de proveniência** com `data_hora`, ferramenta e `g1_metodo` — é exatamente a rastreabilidade que a literatura exige
- Separa `sem_abstract` de `nao_retornados` — distinção que importa
- **Não decide nada**, e o docstring diz isso explicitamente: *"G3 é do avaliador, nunca deste script"*

Três reparos pequenos:

| # | Problema |
|---|---|
| 1 | `if a["pmid"] not in pmids` numa lista → O(n²). Com 237 tudo bem; com 3.000 trava. Use um `set` paralelo |
| 2 | Sem `api_key` do NCBI o teto é 3 req/s; com chave sobe para 10. `ESPERA=0.5` é conservador demais |
| 3 | Se o XML vier truncado, `ET.fromstring` estoura e **perde o lote inteiro** — sem checkpoint parcial |

---

# 6. 🟡 Script 2 — o risco está na lista, não no código

O código está correto. O problema é a estrutura `ALVOS`: **48 rótulos com queries escritas à mão**, e `retmax=3` por relevância.

O risco: `("Fiebich_2018", "Fiebich[au] AND 2018[dp] AND (microglia OR ...)")` devolve os 3 mais relevantes — que **podem não ser o artigo citado**. O script sabe disso e avisa no log (*"3 candidatos são sugestões; G3 confirma"*), o que é honesto. Mas se alguém a jusante tratar o candidato 1 como o artigo certo, entra uma referência errada com PMID real — o pior tipo de erro, porque passa em toda validação de existência.

Note que este script é a origem provável dos **11 rótulos de citação defasados** (IMPL-46): rótulos como `"Título em inglês, 2008"` são exatamente o formato `Autor_Ano` desta lista, não a citação nominal da Canônica.

Dois pontos: usa `importlib` para carregar `03_efetch_abstracts.py` porque o nome começa com dígito (não é importável normalmente) — renomear para `efetch_abstracts.py` resolve. E `abstracts_pubmed.json` é **sobrescrito sem backup**.

---

# 7. 🟢 Script 4 — bom desenho, um cuidado

O acerto central: `sugestao_g2()` **nunca devolve `eligible` puro** — sempre `"eligible? (...)"` com interrogação e motivo. Separação correta entre o que a ferramenta sugere e o que o avaliador decide. A lista de alto-risco (humano/MA/RCT primeiro) também é boa priorização.

O cuidado: a sugestão vem pré-preenchida na coluna ao lado da decisão. Isso é **ancoragem** — o avaliador tende a confirmar a sugestão. E os campos `g2_elegibilidade`/`g3_*` saem vazios no CSV, mas no JSONL saem com `"nao_avaliado"` e `"pendente"` — **incoerência entre os dois artefatos do mesmo script**.

Sugestão: no CSV, deixar a sugestão numa aba/coluna distante, ou exigir que o avaliador escreva o motivo antes de aceitar.

---

# 8. O problema real: os scripts se multiplicam

> *"ele vai gerando mais scripts toda vez que eu peço algo... está gerando mais e mais scripts à medida que analisa"*

Isto é o achado mais importante das duas rodadas, e não é um problema de disciplina do agente.

**Por que acontece:** gerar um script novo é sempre mais barato, para o agente, do que ler o existente, entender e alterar. Cada pedido seu produz um artefato novo em vez de melhorar um artefato velho. O resultado é uma pasta onde ninguém sabe qual é o vigente — e foi exatamente assim que **três versões do propagador de selos** (lote 1) e **dois caminhos de escrita nos vínculos** (este lote) passaram a coexistir.

**Por que é grave:** com N scripts que escrevem nos mesmos arquivos, o estado final depende da **ordem de execução**, que não está registrada em lugar nenhum. Foi isso que produziu o lote v2 — e a prova é o `VINC_B1_0030`, correto no meio de 30 defeituosos da mesma rodada.

## A regra que sugiro, e que é uma só

> **Todo script que ESCREVE em artefato canônico deve validar contra o schema antes de gravar, fazer backup, e sair com código ≠ 0 se algo não conformar.**

Scripts que só **leem** podem se multiplicar à vontade — são inofensivos. A regra vale para os que escrevem. No lote de hoje, isso são os scripts 3 e 5. No lote anterior, o 1, o 4 e o 5.

**Sugestão prática, dois níveis:**

| Pasta | Regra |
|---|---|
| `ferramentas/` | Scripts vigentes. Um por trabalho. Quem escreve valida |
| `_analises/` | Scripts descartáveis de consulta. Podem ser N. Nunca escrevem |

Um script que grava em `Evidencias/` e não importa o `SCHEMA_VINCULO_v1.json` não deveria existir.

---

# 9. Ações

| # | Ação | Urgência |
|---|---|---|
| 1 | Achar os `vereditos_*.json` da rodada v2 — o defeito está lá, e talvez `g2_motivo`/`g3_notas` existam sob outro nome de chave | 🔴 **primeiro** |
| 2 | Blindar o script 5 (validação de enum + backup + exit 1) | 🔴 |
| 3 | Script 3: parar de mutar `trecho_ancora`; IDs estáveis | 🔴 |
| 4 | Investigar se `limp_pmid` causou os 140 prefixos | 🟠 |
| 5 | Mover scripts de consulta para `_analises/` | 🟠 |
| 6 | Script 1: `set` para dedup; considerar `api_key` | 🟡 |

**A ação 1 pode mudar tudo.** Se os vereditos originais tiverem os motivos sob outra chave, os 30 vínculos se recuperam sem reauditar nada — e a IMPL-45 encolhe de "reauditar 30" para "remapear 2 campos".

---

# 10. Sobre a lista que ele está gerando agora

Você disse que ele está listando as atualizações feitas nas 16 canônicas — e criando scripts para isso.

**Peça a lista, mas não os scripts dessa análise.** Uma lista de "o que mudou em cada canônica" é um artefato de leitura: útil, inofensivo. Os scripts que a produziram são descartáveis e só aumentam a confusão.

O que vale pedir junto: **quantas vezes cada script rodou em cada biblioteca**. Combinado com o `grep '\[VERIFICADO\] \[VERIFICADO\]'` do parecer anterior, isso fecha o mapa de dano das 16.

Mande os próximos 5.
