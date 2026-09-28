# CHECKLIST DE AUDITORIA ESTRUTURAL DA BIBLIOTECA
**Versão 1.1**
Uso: colar junto com a Biblioteca recém-gerada, em mini-rodada
própria, imediatamente após a Rodada 2 (geração da Biblioteca Pré-Canônica)
e antes do Portão de Auditoria Científica (G1→G2→G3)

## HISTÓRICO DE VERSÃO DESTE DOCUMENTO

**v1.0:** checklist de conformidade estrutural (blocos, referências mínimas, formato de citação, escopo P20, identificadores, sinalizadores, tamanho). Já continha, no próprio rodapé, a declaração de que "não avalia se as citações são reais" — reconhecendo a lacuna sem preenchê-la.

**v1.0 → v1.1 (esta versão):** insere **Bloco C-1** (declaração de escopo explícita no cabeçalho, para não confundir "bem-formatado" com "auditado"), **Bloco C-2** (itens de checagem para os artefatos de evidência de Nível 1 e Nível 2 — Módulo 09 e vínculos — introduzidos pelo Prompt 4.2), e **Bloco C-3** (veredito final com encaminhamento explícito ao Portão de Auditoria Científica). Atualiza terminologia de "GRADE" para `forca_evidencia_afirmacao`, coerente com o hard-fail do Prompt 4.2.

---

> **(ADENDO — BLOCO C-1, v1.1) ESCOPO DESTE CHECKLIST**
>
> Este checklist verifica **CONFORMIDADE ESTRUTURAL** (blocos, âncoras, formato de citação, contagem mínima, P20/P16, presença dos arquivos de Nível 1 e Nível 2). **NÃO verifica se citações são reais nem se sustentam as frases** — isso é do **PORTÃO DE AUDITORIA CIENTÍFICA** (G1 existência → G2 elegibilidade → G3 suporte), em mini-rodada separada, conduzida por quem não gerou o conteúdo. **"Aprovado estruturalmente" NÃO significa "auditado".** O artefato permanece rotulado **Pré-Canônica** mesmo após aprovação neste checklist.

---

## INSTRUÇÃO PARA A IA

Você vai receber uma Biblioteca de Conhecimento **Pré-Canônica** já gerada para um mecanismo específico (B1 a B16). Sua tarefa não é avaliar mérito
científico, veracidade das citações ou qualidade da argumentação.
Sua tarefa é aplicar os critérios objetivos abaixo e reportar
exatamente no formato de saída especificado.

**Não corrija o documento. Apenas reporte o que encontrou.**

---

## CRITÉRIOS DE VERIFICAÇÃO

### A. Completude de blocos obrigatórios
- [ ] BLOCO_00 até BLOCO_09 presentes, na ordem
- [ ] BLOCO_10: presente com conteúdo OU declaração explícita de N/A
- [ ] BLOCO_11: presente com conteúdo OU declaração explícita de N/A
- [ ] BLOCO_12: presente com conteúdo OU declaração explícita de N/A
- [ ] TABELA DE EVIDÊNCIAS presente
- [ ] CONTROVÉRSIAS E LACUNAS presente
- [ ] ELEMENTOS MOLECULARES CRÍTICOS presente
- [ ] MARCADORES_PARA_JSON presente e sem campos vazios não justificados, incluindo `artefato_rotulo: "PRE_CANONICA"` *(ADENDO v1.1)*

### B. Contagem mínima de referências por bloco
Contar chaves únicas em cada âncora `[REF_BLOCO_XX]`:

| Bloco | Mínimo exigido | Encontrado |
|-------|-----------------|------------|
| BLOCO_01 | 3 | |
| BLOCO_02 | 5 | |
| BLOCO_03 | 3 | |
| BLOCO_04 | 2 | |
| BLOCO_05 | 3 | |
| BLOCO_06 | 3 | |
| BLOCO_07 | 3 | |
| BLOCO_08 | 1 por conexão HIGH + forca_evidencia_afirmacao alto/medio | |
| BLOCO_09 | 4 | |
| BLOCO_10 | 3 (se aplicável) | |
| BLOCO_11 | 2 (se aplicável) | |
| BLOCO_12 | 1 por subtipo (se aplicável) | |
| **Total único** | **20** | |

### C. Formato de citação
- [ ] Nenhum PMID ou DOI encontrado no texto corrido (buscar padrões numéricos típicos de PMID e formato "10.xxxx/")
- [ ] Toda citação (Autor, Ano) é seguida de classificador `[MA]/[EC]/[OB]/[ML]/[AT]`
- [ ] Toda âncora `[REF_BLOCO_XX]` contém ao menos uma referência
- [ ] **(ADENDO v1.1)** Nenhum campo ou rótulo literal `"grade"` com valor `A|B|C|D` presente em contexto de mecanismo — o termo correto neste tipo de artefato é `forca_evidencia_afirmacao (alto|medio|baixo)`. Ocorrência de `"grade": "A"` (ou B/C/D) em qualquer schema de mecanismo = falha deste item.
- [ ] **(ADENDO v1.1)** Classificador `[tipo]` único por tag (sem `[EC/OB]` ou similar combinado); `[MA]`→02, `[EC]`→03 (template RCT), `[OB]`/`[AT]`→01/04, `[ML]`→05.

### D. Cobertura das 16 conexões (BLOCO_08)
- [ ] As 16 chaves de `connection_strength` no JSON têm correspondência mínima no corpo do BLOCO_08 (ao menos uma linha com força biológica + justificativa, mesmo para as não priorizadas)
- [ ] 3 a 5 conexões desenvolvidas em narrativa completa (ambas direções, classificação, força biológica, força de evidência)

### E. Verificação cruzada com o GPM
- [ ] Checklist do Módulo 09 do GPM foi verificado categoria por categoria (vias, mediadores, células, genética, biomarcadores, interconexões, subtipos, controvérsias)
- [ ] Para cada categoria do GPM ausente na Biblioteca, existe declaração explícita de "N/A — motivo"

### F. Separação de escopo (regra P20)
- [ ] BLOCO_05 não contém valores numéricos de corte, protocolos de coleta ou algoritmos de interpretação
- [ ] Nenhum medicamento, suplemento ou intervenção terapêutica aparece como conteúdo principal em nenhum bloco
- [ ] BLOCO_12 não contém menção a fármaco, protocolo ou conduta clínica

### G. Identificadores e nomenclatura
- [ ] Todos os elementos em ELEMENTOS MOLECULARES CRÍTICOS têm UniProt/HGNC/HMDB declarados (ou null justificado)
- [ ] Biomarcadores em BLOCO_05 fecham com "ID oficial: [...]" ou declaração de ausência de ID catalogado

### H. Sinalizadores obrigatórios
- [ ] Ao menos uma ocorrência de sinalizador de evidência (`[CONTROVERSO]`, `[APENAS PRÉ-CLÍNICO]`, etc.) em blocos onde há exclusivamente evidência pré-clínica ou controversa citada
- [ ] Ocorrências de `[EXTRAPOLAÇÃO POR ANALOGIA]` presentes onde o texto cita estudo-fonte de condição diferente de ansiedade/depressão
- [ ] **(ADENDO v1.1)** Classificação de evidência por espécie explícita no texto onde a fonte é animal/in vitro: `[APENAS PRÉ-CLÍNICO]` presente; fonte de outra condição (esquizofrenia/Alzheimer/bipolar…) com `[EXTRAPOLAÇÃO POR ANALOGIA: ...]`. *(A confirmação do SUPORTE real da citação é G3, na auditoria científica; aqui só se verifica a PRESENÇA da tag.)*

### I. Tamanho mínimo
- [ ] Documento completo atinge no mínimo 7.000 palavras

---

### J. Artefatos de evidência — Nível 1 e Nível 2

*(ADENDO — BLOCO C-2, v1.1 — bloco novo, itens antes inexistentes neste checklist)*

- [ ] **MÓDULO 09 (Nível 1) presente:** os 5 arquivos de `/Evidencias/Bibliografia` existem (inicializados como `[]` mesmo quando vazios) e seguem schema 09.1–09.3.
- [ ] **NÍVEL 2 presente:** `/Evidencias/Vinculos/vinculos_referencia_afirmacao.json` existe, com UM vínculo por citação-âncora e `trecho_ancora` **LITERAL** (cópia, não resumo). Ausência de `trecho_ancora` = reprova.
- [ ] **Mão dupla TEXTO ⇄ MÓDULO 09:**
  - toda citação `(Autor, Ano)[tipo]` do corpo tem registro (Nível 1) e vínculo (Nível 2) correspondentes;
  - nenhuma entrada do Módulo 09/vínculos fica sem citação no corpo (órfã) — a menos que marcada explicitamente como adição prospectiva.
- [ ] **Campo `pmid_oficial`:** ou vazio (candidato) ou proveniente de busca por ferramenta — nenhum PMID digitado sem registro no `corpus_pubmed.json`/`log_de_busca`.
- [ ] **`status_auditoria` / `verification_status` / `forca_causal` não preenchidos nesta geração** (nascem vazios/`"pendente"`); a saída está rotulada Pré-Canônica.
- [ ] Campos `citacao_confirmada` e `origem_pipeline` presentes em cada entrada de Nível 1 (Schema 09.1/09.2).

---

## FORMATO DE SAÍDA OBRIGATÓRIO

```
AUDITORIA ESTRUTURAL — BIBLIOTECA [nome do mecanismo] — status: PRÉ-CANÔNICA

A. Blocos obrigatórios: [X/8 categorias verificadas]
Ausentes sem justificativa: [listar ou "nenhum"]

B. Referências por bloco:
[tabela completa preenchida]
Total único de referências: [n] (mínimo: 20)
Blocos abaixo do mínimo: [listar ou "nenhum"]

C. Formato de citação: [conforme/não conforme]
Ocorrências fora do padrão: [listar ou "nenhuma"]
Ocorrências de "grade" literal A-D em contexto de mecanismo: [listar ou "nenhuma"]

D. Cobertura das 16 conexões: [16/16 com correspondência mínima]
Conexões sem registro no corpo do texto: [listar ou "nenhuma"]

E. Verificação cruzada com GPM: [realizada/não realizada]
Categorias do GPM ausentes sem justificativa: [listar ou "nenhuma"]

F. Separação de escopo (P20): [conforme/não conforme]
Violações encontradas: [listar ou "nenhuma"]

G. Identificadores: [conforme/não conforme]
Elementos sem ID declarado: [listar ou "nenhum"]

H. Sinalizadores obrigatórios: [conforme/não conforme]

I. Tamanho: [n palavras] (mínimo: 7.000)

J. Artefatos de evidência (Nível 1 e Nível 2): [conforme/não conforme]
Vínculos sem trecho_ancora: [n] (deve ser 0)
Órfãos (texto sem Módulo 09, ou Módulo 09 sem texto): [listar ou "nenhum"]
pmid_oficial preenchido sem origem em corpus_pubmed.json: [listar ou "nenhum"]

K. Rastreabilidade com a Lista Canônica (quando aplicável): [aplicável, X/Y claims aprovados com correspondência] ou [não aplicável — sem Lista Canônica para este mecanismo]
Divergências não sinalizadas: [listar ou "nenhuma"]

VEREDITO FINAL: [APROVADO ESTRUTURALMENTE — libera Portão de Auditoria 
Científica (G1→G2→G3)] ou [REQUER CORREÇÃO ESTRUTURAL — motivo: ...]
```

> **(ADENDO — BLOCO C-3, v1.1) Veredito com encaminhamento explícito:**
>
> "Aprovado estruturalmente" **apenas libera o PORTÃO DE AUDITORIA CIENTÍFICA (G1→G2→G3)**. Não atesta veracidade de citações, não confirma que os vínculos de Nível 2 realmente sustentam as frases às quais foram anexados, e **não gera Biblioteca Canônica**. O artefato permanece `Biblioteca_Bx_PRE_CANONICA.md` até completar o fluxo descrito no Processo de Geração v2.1 (Portão G1→G2→G3 → Gate-Script → Gate Obrigatório Bloco H → Rodada 3 → Checklist de Fidelidade Canônica).

---

## CRITÉRIO DE VEREDITO

Marcar **[REQUER CORREÇÃO ESTRUTURAL]** se qualquer condição for verdadeira:

- Qualquer bloco obrigatório ausente sem justificativa (item A)
- Total de referências únicas abaixo de 20 (item B)
- Qualquer PMID/DOI encontrado no texto corrido (item C)
- Qualquer ocorrência de `"grade"` literal A-D em contexto de mecanismo (item C) *(ADENDO v1.1)*
- Qualquer uma das 16 conexões sem registro mínimo (item D)
- Qualquer violação de escopo P20 encontrada (item F)
- Tamanho abaixo de 7.000 palavras (item I)
- Qualquer vínculo de Nível 2 sem `trecho_ancora`, ou ausência do arquivo `/Evidencias/Vinculos/vinculos_referencia_afirmacao.json` (item J) *(ADENDO v1.1)*
- Item K aplicável e com claim aprovado sem correspondência rastreável, ou com divergência não sinalizada

Caso contrário, **[APROVADO ESTRUTURALMENTE]**.

Este veredito verifica apenas conformidade de estrutura e formato.
**Não avalia se as citações são reais, se o conteúdo científico está
correto, ou se as classificações de força de evidência foram
atribuídas corretamente** — essa é a auditoria científica (Portão
G1→G2→G3), etapa posterior, distinta desta, e conduzida em sessão
separada de quem gerou o conteúdo (ver Processo de Geração v2.1).

---

Checklist de Auditoria Estrutural da Biblioteca — Clinical Dominion
**Versão do documento: 1.1** | Alinhado com Prompt 4.2 | Processo de Geração v2.1