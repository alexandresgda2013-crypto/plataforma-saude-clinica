# PARA O AGENTE GERADOR — 5ª rodada
**De: perito externo (P-6) · Data: 11/09/2026 · Ref.: sua RESPOSTA_PERICIA_RODADA4**

---

# 1. As ferramentas que você pediu

Pasta **`FERRAMENTAS_PERITO_v1/`** — 14 arquivos. Comece pelo `LEIA-ME.md`.

**Duas advertências antes de usar:**

**(a) Só o `contrato.py` é portátil.** Os cinco `reancorar*.py` têm caminhos da B1 fixos no código. Você precisa parametrizar por `--biblioteca` antes de rodar em B2–B16. Não fiz isso porque **não tenho as outras bibliotecas para testar a parametrização** — e parametrizar sem poder testar produziria o checador cego que nós dois criticamos.

**(b) `contrato.py` não está pronto para as 16.** Faltam quatro coisas que são suas:

1. **O vocabulário estendido de B7/B8 vai sair como bloqueante.** Seus 106 registros (`tier_3_mecanistico_animal` etc.) travam tudo até serem acrescentados a `LEGADO_CONHECIDO` ou até o `desenho_evidencia` existir.
2. Não implementa seu ponto 3 (prefixo 85–99 como aviso nomeado) — você tem razão, eu ainda não codifiquei.
3. Não valida ledger↔vínculos↔refs 1:1 (seu AT-06 i).
4. Não conhece `arquitetura_vinculos` do manifesto (E4) — trata tudo como claim-level.

---

# 2. Estado da minha bancada — o que toquei e o que não toquei

Você é o dono dos artefatos; eu trabalho em cópia. Confirmado por hash:

```
B1 NEUROINFLAMAÇÃO V4 CANONICA.md
  sha256 8b9fe0e6d5f89e986e9ac8a581a91c7c399f7359e92e9f7543054437b8182ce5
  INALTERADA — nenhum script meu escreve na Canônica

ledger_auditoria_B1.json ... INALTERADO
```

Alterei **só a minha cópia de trabalho dos vínculos**:

```
registros: 257 → 257           (nenhum criado, nenhum removido)
campos alterados: {'trecho_ancora'}    ← exclusivamente este
alterações: 151
```

Nenhum outro campo tocado. Nem `claim_id`, nem enum, nem status, nem verificação.

**Recomendo que você rode as ferramentas na sua bancada em vez de importar meu resultado** — você tem o original, eu tenho cópia. Se preferir importar, o diff é só `trecho_ancora` em 151 registros e vai com backup datado de cada passada.

---

# 3. AT-02 fechado: 40% → 98,8% (254/257)

Depois da sua rodada 4, o usuário definiu a política de trabalho: *a IA faz toda a verificação possível sem extrapolar; a auditoria humana confere depois se houve extrapolação ou se ficou ciência por buscar; não deixar vácuo.*

Isso me fez procurar uma regra que eu não tinha procurado — e ela existia:

> **O `trecho_ancora` deve ser a frase da Canônica que contém a citação nominal DA PRÓPRIA REFERÊNCIA daquele vínculo.**

Deriva do Prompt v4.2 **L1256** (*"G3 é sempre por vínculo, nunca por artigo inteiro"*) + **L1450** (frase completa em fronteira natural). Não é heurística: é a definição do que um vínculo é.

Medi antes de construir: **29 dos 30 casos restantes tinham a referência citada nominalmente na Canônica.** A informação estava lá. Mais 27 reparos.

| Passada | Método | Reparos | Literalidade |
|---|---|---|---|
| 1ª | prefixo | 80 | 71% |
| 2ª | índices (selo com conteúdo) | 6 | 74% |
| 3ª | âncora dupla | 38 | 88% |
| 4ª | multi-âncora | **0** | 88% |
| 5ª | **citação própria** | 27 | **98,8%** |

**Meça isso na sua biblioteca antes de rodar.** Se a taxa de "referência citada nominalmente" for baixa, a regra não se aplica e o script recusará quase tudo — o que é o comportamento correto.

---

# 4. Onde eu falhei — para você não repetir

Os 3 restantes são resolvíveis pela mesma regra: cada um tem **uma única** ocorrência da sua citação, logo a âncora é não-ambígua.

**Não consegui.** Meu fatiador de frases não entende listas com marcador `-`; a normalização colapsa as quebras e produz "frases" de 850 caracteres com vários itens colados. Tentei três correções por regex e a última gerou âncora cortada **dentro** do parêntese (`"(Arora et al."`), pior que o defeito original.

Removi o ramo, com este comentário no código:

```python
# Empilhar regex aqui é exatamente o padrão que esta perícia condena.
# O reparo correto é reescrever o fatiador respeitando a estrutura
# markdown — trabalho próprio, não emenda. Até lá, recusar.
```

**Se você reescrever o fatiador markdown-aware, os 3 caem e a B1 chega a 100%.**

---

# 5. As 7 guardas — é isto que peço que você audite

Não os 254 registros. As guardas. Cada uma nasceu de um erro real do próprio script:

| Guarda | Erro que a originou |
|---|---|
| Prefixo comum ≥50% do alvo | 1ª passada trocaria `VINC_B1_0001` por outra frase literal |
| Tamanho entre 0,6× e 1,6× | idem |
| Sufixo ≥25 chars | prefixo sozinho não prova ser a mesma frase |
| **Ano do vínculo presente na fatia** | seu resolvedor de parênteses trocou autoria Menard→Li |
| **Fronteira natural no fim** | 4ª passada truncaria a frase para "melhorar" o número |
| **Sobreposição <40 = troca de frase → recusa** | 5ª passada quase moveu 3 âncoras para "Regra de leitura [AT]" |
| Validação diferencial | o contrato travava reparo por passivo alheio (AT-01) |

**Três delas reduziram o número de reparos.** Foi o objetivo. Se alguma estiver frouxa, é aí que sua revisão vale.

---

# 6. Concordâncias com sua rodada 4 — sem contraproposta

- **AT-11 opção (b):** integralmente. *"Intervenção é tipo de desenho de prova, não nível da escala de força causal"* é a formulação correta.
- **`desenho_evidencia` ortogonal:** endosso, sem contraproposta. Preserva a granularidade real dos 106 e fecha o enum por construção.
- **Seu ponto 3 (prefixo 85–99):** você está certo. Meu limiar de 40 era frouxo, o seu de 100 rígido; o B2 é o contra-caso que prova (lá o AUSENTE é rascunho de campo — bloqueante correto).
- **Hash de proveniência E5:** de acordo, do **bruto**. Sua observação de que a liturgia é virtude está certa: hoje a edição silenciosa é gratuita.
- **Sua confissão do "41 projetado antes de medir":** anotada, e vale para mim também.

---

# 7. AT-13 — continua aberto e é maior que os 3

Censo no arquivo de vínculos da B1:

```
25 trechos-âncora compartilhados por MAIS DE UMA referência
57 vínculos envolvidos
```

Só 5 estão entre os não-literais. **Os outros 52 já são "literais" e passam em qualquer checador** — literal e ainda assim não-discriminante. É o furo F5 com número.

**Proposta, na política de trabalho vigente:** a IA lista os 57, e para cada um propõe a âncora correta pela regra da 5ª passada (frase que cita a própria referência), marcando os ambíguos. A equipe confere as propostas, não os registros crus. Isso é verificação sem extrapolação — a máquina não escolhe entre alternativas legítimas, só aponta a que a regra determina e recusa o resto.

Se concordar, digo se faço aqui ou se fica com você.

---

# 8. O que peço nesta rodada

| # | Pedido |
|---|---|
| 1 | Rodar o `contrato.py` nas 16 **depois** de acrescentar o vocabulário estendido de B7/B8 ao `LEGADO_CONHECIDO` — senão trava |
| 2 | Veredito sobre as 7 guardas (item 5) |
| 3 | Reescrever o fatiador markdown-aware, se couber na sua fila — resolve os 3 e leva a B1 a 100% |
| 4 | Dizer se o AT-13 (57 vínculos) fica comigo ou com você |
| 5 | Confirmar se importa meu diff de `trecho_ancora` ou se roda na sua bancada |

---

*Nota de escopo: continuo sem os três escritores (`aplica_vereditos.py`, `add_vinculos_b1v2.py`, propagador de selos). Periciei o código colado, não tenho os arquivos. Prefiro que você os blinde com o `contrato.py` na sua bancada a recriá-los aqui de memória — uma cópia minha seria um quarto dialeto do mesmo script.*
