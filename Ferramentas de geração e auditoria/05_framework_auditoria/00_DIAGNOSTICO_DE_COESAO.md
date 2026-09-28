# 00 — Diagnóstico de Coesão: as ferramentas reais vs. o processo de auditoria

**Objetivo:** responder sua pergunta — as ferramentas que você já tem (Molde GPM, Briefing, Prompt 4.0, Schema-Claim v3.1, Protocolo de Escopo, Como Executar, Lista Canônica, Bloco de Estado, checklists, Contrato/Decisões) estão coesas entre si e com a filosofia? E onde o "processo de auditoria científica de conteúdo" se encaixa?

**Conclusão curta:** as ferramentas são fortemente coesas entre si e fiéis à filosofia. Existe **um único estágio não formalizado** — a "Auditoria científica de conteúdo (etapa a formalizar)" do PROCESSO DE GERAÇÃO — e é exatamente ele que formalizamos neste pacote (documentos 02–08). A proposta anterior (pacote `pipeline_auditoria_cientifica`, criada sem conhecer suas ferramentas) estava **arquiteturalmente correta nos princípios**, mas colidia com vocabulários, nomes de campo, ordem do fluxo e com o design do Módulo 09 do Prompt 4.0. Por isso este pacote a substitui, reimplementando o que vale em cima das suas convenções reais.

---

## 1. O que as ferramentas já dizem (o estado real)

### 1.1 O pipeline oficial (PROCESSO DE GERAÇÃO v2.0)

```
Rodada 1: Molde GPM + Briefing(Bx) → GPM_Bx.md → [Checklist de Sanidade]
Rodada 2: Prompt 4.0 + IDs + Filosofia + Lista Canônica (se houver) + GPM →
          Biblioteca_Bx.md + Módulo 09 (5 arquivos) → [Checklist Estrutural]
Auditoria científica de conteúdo  ← ETAPA NÃO FORMALIZADA (é o que este pacote preenche)
Aprovação e integração
```

### 1.2 As duas trilhas de validação de claim (que já existem e funcionam)

- **Trilha clínica** (`B1.SM02.xxx`): pergunta epidemiológica — "este biomarcador/fenômeno existe, medido, em população MDD/ansiedade vs. controle?".
- **Trilha mecanística** (`B1.MEC.BLOCOxx.nnn`): pergunta causal — "como este processo funciona, passo a passo, por qual evidência experimental?".
- Ambas passam pelos portões **G1 (existência do PMID) → G2 (elegibilidade do desenho) → G3 (suporte ao claim: pertencimento, suporte causal, robustez)** e têm Lista Canônica, Bloco de Estado, filas (`fila_realocacao`, `redirecionados_modulo_clinico`, `resultados_nao_triados`, `fontes_rejeitadas`).
- O **GPM nunca é fonte de PMID**: ele usa `(Autor, Ano)` e tolera "referência específica a confirmar". Um achado do GPM só vira claim quando um PMID real é verificado em sessão.

### 1.3 A Lista Canônica mecanística B1 hoje

É um **seed de 83 `claim_alvo` em `status: em_busca`** (auditoria contra o GPM_B1 Arena), com queries prontas. Nenhum claim aprovado ainda na trilha mecanística (Bloco de Estado = estado zero). Ou seja: **a validação G1→G2→G3 da trilha mecanística ainda não começou em produção**.

### 1.4 O Módulo 09 (Prompt 4.0) é quem materializa as referências

- 5 arquivos JSON em `/Evidencias/Bibliografia/`: `01_pmids.json [OB]`, `02_meta_analises.json [MA]`, `03_ensaios_clinicos.json [EC]`, `04_atualizacoes_literatura.json [AT]`, `05_manuais_e_livros.json [ML]`.
- Citações no texto: `(Autor, Ano)[tipo]`, nunca PMID/DOI no corpo; âncoras `[REF_BLOCO_XX: Autor_Ano[tipo] | ...]` por bloco.
- Entradas podem ter `claim_id_origem` preenchido **apenas** quando já existe claim aprovado/ressalvado na Lista Canônica (aí o Prompt usa exatamente o PMID do claim). As demais vêm do GPM/Política de Fontes e nascem com `claim_id_origem` e `status_auditoria` vazios.

---

## 2. O que estava CERTO na proposta anterior (e preservamos)

| Ideia da v1/v2 anterior | Status |
|---|---|
| Referência ≠ evidência; nada nasce validado | ✅ preservado (já é o espírito do seu sistema) |
| Precisa de um "trecho âncora" (o que a citação sustenta) para auditar conteúdo | ✅ preservado — mas como **ledger de auditoria**, não mexendo no Módulo 09 |
| A mesma referência pode sustentar claims com resultados diferentes | ✅ preservado — o ledger é 1:N por `id_referencia_interna` |
| Vocabulário fechado para `status_auditoria` | ✅ preservado, mapeado para os portões G1/G2/G3 que já existem |
| Árvore de decisão quando PMID não existe / não sustenta | ✅ preservada, mapeada para `fila_realocacao`, `redirecionados_*`, `resultados_nao_triados`, `fontes_rejeitadas` |
| Checagem cruzada texto↔registros; verificação mecânica por script | ✅ preservada, adaptada aos nomes/formatos reais |
| Quem gera não audita (mini-rodadas separadas) | ✅ já é seu princípio (Checklist de Sanidade/Estrutural) |
| Reconciliação do texto após rejeição | ✅ preservada como mini-rodada C de correção |

---

## 3. O que COLIDIA com suas ferramentas (e foi corrigido nesta versão)

| Erro da proposta anterior | Realidade das suas ferramentas | Correção aqui |
|---|---|---|
| Criava claim na Etapa 4 **depois** da Biblioteca ("extrair claims da Biblioteca") | Os claims são validados **antes/alimentam** a Biblioteca (Lista Canônica = entrada prioritária da Rodada 2). A Biblioteca consome claims aprovados. | A auditoria de conteúdo **não cria claims novos a partir do texto**; ela (a) re-verifica o que a Biblioteca usou e (b) devolve aprovados como claims novos à Lista Canônica pelo fluxo G1→G2→G3 já existente. |
| Inventava `id_claim CLAIM_B1_047`, status próprios (`CONFIRMADO`, `PENDENTE_EVIDENCIA`...) | Claim oficial é `B1.MEC.BLOCO02.001` / `B1.SM02.007`; status oficiais são `aprovado / aprovado_com_ressalva / em_busca / rejeitado / aposentado`; portões G1/G2/G3 | Tudo renomeado para o vocabulário oficial. O ledger referencia os IDs oficiais. |
| Inventava eixos `natureza_relacao`/`grau_maturidade` com grafia própria ("muito_estabelecida", "contributiva" etc.) | GPM v2.0 usa "muito estabelecido", "contributiva" (feminino); o Schema-Claim v3.1 fixou os enums | Adotados **exatamente** os enums do Schema-Claim v3.1 e do GPM. |
| Criava 4 eixos de evidência próprios | Já existem 4 eixos oficiais e **nunca devem ser fundidos**: `forca_causal` (tier 1–4), `classificador_tipo_fonte` [MA/EC/OB/ML/AT], `forca_biologica_conexao` (HIGH/MEDIUM/LOW), `dominios_grade_observados` (por fonte) | Ledger referencia o claim; os 4 eixos vivem no claim/Lista, não duplicados. |
| Mudava o Módulo 09 para registro mestre + tabela `06_vinculos` e RCT em `.md` com YAML | Prompt 4.0 fixou Módulo 09 v1.0: **5 arquivos JSON** (`03_ensaios_clinicos.json`), schema de entrada próprio. Mudar isso exigiria versionar o Prompt 4.0. | **Módulo 09 intacto.** O ledger de auditoria vive em `/Auditoria_Bx/`, fora dos 5 arquivos oficiais, e os referencia por `id_referencia_interna`. Zero alteração no Prompt 4.0. |
| Criava campos novos no mestre (`chave_canonica`, `citacao_confirmada`, `origem_pipeline`, `grade` no registro) | O Módulo 09 já tem `id_referencia_interna`, `status_auditoria`, `claim_id_origem`, `extrapolacao_por_analogia`; GRADE é da síntese (R04), não do registro | Propõe-se apenas um **delta mínimo opcional** (3 campos) ao Schema de Entrada do Módulo 09 — doc 03 — sem nada quebrar. |
| "Rodada 3 — Biblioteca Canônica" como nova geração | O artefato é a própria `Biblioteca_Bx.md`; correções são mini-rodadas; não existe regeneração "canônica" | Trocado por **mini-rodada C (correção pós-auditoria)**, seguida de aprovação/integração. |
| Validava qualquer PMID como "evidência" sem separar natureza epistemológica | PMID associativo em busca mecanística nunca é "rejeitado" — vai para `redirecionados_modulo_clinico`; PMID de outro bloco/mecanismo vai para `fila_realocacao` | Árvore de decisão reescrita usando suas filas oficiais (doc 04). |
| R04/GRADE tratado como nota por fonte | GRADE (Guyatt 2011) é propriedade de um **corpo de evidência**, calculado na síntese da Biblioteca; fonte isolada só registra `dominios_grade_observados` | Respeitado; o ledger não emite nota GRADE. |

---

## 4. As duas pontas soltas REAIS que as ferramentas ainda não fecham (e que motivam este pacote)

1. **Entradas do Módulo 09 sem `claim_id_origem` não têm processo de verificação definido.**
   O Prompt 4.0 diz que o claim aprovado entra "com o PMID exato". Mas a maior parte das referências de uma Biblioteca nova vem do GPM/Política de Fontes **sem** claim aprovado (caso do B1 hoje: 0 claims mecanísticos aprovados). O PROCESSO DE GERAÇÃO manda para "auditoria científica de conteúdo (etapa a formalizar)" — sem dizer **como**. Resultado prático: como o Prompt 4.0 não tem busca externa na geração, essas entradas nascem com `pmid_oficial: ""` e metadados a resolver, e ninguém sabe o protocolo para verificar.

2. **Não existe o "trecho que esta citação sustenta" nem o registro 1:N.**
   O campo `status_auditoria` do Módulo 09 é um único campo por registro. Se um artigo sustentar uma frase e não sustentar outra, o registro (uma linha por entrada) não tem onde guardar isso. O ledger de auditoria (doc 02) resolve sem tocar no Módulo 09.

Fechar essas duas pontas é o conteúdo deste pacote. Tudo o mais já estava coberto pelas suas ferramentas.

---

## 5. Verificação de aderência à filosofia (FASE 2-02)

| Princípio da filosofia | Cobertura nas ferramentas | Na auditoria de conteúdo |
|---|---|---|
| Biblioteca = única fonte canônica; tudo deriva dela | Prompt 4.0 + P20 | A auditoria **protege** a canonicidade: só entra na Biblioteca aprovada o que passou por G1/G2/G3 |
| Toda afirmação rastreável à literatura | Citações `(Autor,Ano)[tipo]` + âncoras + Módulo 09 | Ledger fecha o caminho frase → entrada → PMID → abstract verificado |
| Não é diagnóstico, não substitui julgamento (P12) | Declaração `natureza_sistema` obrigatória | Auditoria não emite recomendação; só verifica suporte factual |
| Sem conteúdo especulativo/opinião | Política de Fontes (só PubMed/pares; sem blog/wiki) | Rejeição de fonte sem G1/G2 é o enforcement dessa regra |
| Evidência mais forte vence; robustez > recência | Política de Fontes + tiers de força causal | G2/G3 + heurística de leitura (tier > replicação > recência) |
| "Campo vazio preferível a dado inventado" (R04) | Regra absoluta do Contrato | G1 falho = não se inventa PMID; vai a resgate/fila |
| Separação de escopo P20 (sem dose/corte/protocolo na Biblioteca de mecanismo) | Checklist Estrutural item F | Auditoria confirma que entradas [EC] não arrastam prescrição |
| Extrapolação sinalizada (R04 sinalizador) | Tag `[EXTRAPOLAÇÃO POR ANALOGIA]` no corpo e no Módulo 09 | G3 checa sistema experimental; extrapolação indevida vira ressalva/remoção |

A filosofia e as ferramentas estão **coesas**. O pacote a seguir é a peça que faltava para que "auditado e rastreável" deixe de ser uma afirmação e passe a ser um procedimento verificável.
