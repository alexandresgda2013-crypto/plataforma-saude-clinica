# INSTRUÇÃO DE OPERAÇÃO DO ENSAIO — B1.SM02.014  (rev.2)
### (para colar nos participantes — versão simples)

rev.2.1 (2026-09-25): PONTOS DE PARADA explícitos (achado do ensaio:
as 3 IAs rodaram G1+G2+G3 de uma vez, sem envio intermediário) ·
contagem fixada: baseline 107 (mesma lista em todas as janelas; 92 =
regra de contagem do Estrutura — unificar contagem = parágrafo com DOI).

**Data:** 2026-09-25 · aprovada pelo operador · linguagem simples

---

## O que é este exercício

Um **teste da ferramenta** (não a prova oficial). Queremos ver se o
documento **COMO EXECUTAR v1.10** + **Contrato rev.2** + **Schema 1.3**
funcionam juntos na prática, de ponta a ponta.

**Nada aqui muda o status do claim `.014`.** Ele continua
`aprovado_com_ressalva` no Bloco. O que sai daqui é **registro de teste**.


## Nota de contagem (antes de congelar)

- O arquivo-pool medido pela Arena tem **107 referências com DOI** (107 únicos).
- O Auditor-Estrutura recebeu um anexo e contou **92 entradas**.
- **Os números não batem.** Antes de **congelar** a lista do ensaio: confirmar qual arquivo circulou e fixar **uma contagem única e verificável** (a baseline da deduplicação). Operacional — não trava a Rodada 1.

---

## As regras de ouro (3 frases)

1. **Cada IA trabalha SOZINHA na hora de decidir** — só depois a gente compara.
2. **A ciência manda; o claim se ajusta** (nunca o contrário).
3. **Nada muda em silêncio** — problema prático vira registro; problema de norma abre ciclo novo.

---

## O mapa — o que é o quê

| Etapa | Nome do documento | O que fazemos |
|---|---|---|
| A lista chega na tela (**107 refs com DOI — ver nota de contagem abaixo**) | **G1 — existe?** | A lista na tela **põe o G1 ao alcance** — não é G1 cumprido. Cada executor, **arquivo por arquivo**, resolve o PMID/DOI ao vivo e confere os metadados: **só aí** o G1 fica `verified_reference`. Busca sem conferência não vale; referência na tela sem resolução não vale |
| Cada IA filtra **sozinha** | **G2 — serve?** | É deste tema (TSPO × depressão)? Desenho/população/ano ok? É de Alzheimer/Parkinson/esquizofrenia? → **fica ou sai** |
| Comparar os 3 filtros | (rito do v1.10) | Cada uma mostra o **próprio** filtro; a gente cruza; sai a **lista acordada** (lista limpa congelada do ensaio) |
| Cada IA lê o texto e decide **sozinha** | **G3 — sustenta?** | Com o **texto do artigo na mesa** (busca ao vivo e **mostra a passagem**): o achado sustenta o claim? quais números? qual a direção **desta fonte** (`sentido_do_achado`)? |
| Comparar os 3 G3 | (rito) | Cruzar; divergência factual → vai **para o artigo**, não para votação |
| Fechamento | **4 decisões** | Estado · direção por fonte · tipo da ressalva · moderadores — no formato do Schema 1.3, com o operador aprovando |

**Resumo em uma frase:**  
`lista = G1 para ser executado (resolver PMID/DOI ao vivo)` · `filtro cego = G2` · `veredito cego com texto = G3` · `fechamento = 4 decisões`.

---

## As duas rodadas (mesma forma)

```
RODADA 1 — G2 (filtro)
  IA1 filtra sozinha → ENTREGA E PÁRA
  IA2 filtra sozinha → ENTREGA E PÁRA
  IA3 filtra sozinha → ENTREGA E PÁRA
  operador COMPARA → LISTA ACORDADA (congelada)
  ⛔ NINGUÉM AVANÇA PARA O G3 SEM COMANDO DO OPERADOR

RODADA 2 — G3 (veredito)  [só na lista acordada — comandada]
  IA1 → ENTREGA E PÁRA → IA2 → ENTREGA E PÁRA → IA3 → ENTREGA E PÁRA
  operador COMPARA → divergência factual = artigo manda
  → FECHAMENTO: 4 decisões + operador aprova
```

**PARADA OBRIGATÓRIA:** cada IA entrega a sua parte e **encerra a rodada ali**.
O operador é quem comanda a passagem. Quem avança sozinho para o G3
sem a lista acordada está fora do rito (achado E-04 do ensaio).

Cega = cada uma entrega a sua parte **antes** de ver a das outras.
Divergência entre as 3 na hora de filtrar/vereditar é **funcionamento
normal**, não erro.

---

## O que NÃO fazer

- ❌ Mudar o status do `.014` no Bloco
- ❌ “Consertar” documento/norma por fora (vira ciclo formal)
- ❌ Seguir o filtro da IA 1 sem ter feito o próprio
- ❌ Dar G3 sem o texto na tela / sem mostrar a passagem
- ❌ Usar artigo de outra doença como se sustentasse o claim de MDD
- ❌ Escrever “neuroinflamação” quando o artigo só mede TSPO (sinal ≠ causa)
- ❌ Tratar a concordância dos 4 como “voto” — fonte primária manda sempre

---

## Papéis neste ensaio — FIXADOS (rev.2, correção do Comentador)

**Quatro participantes, papéis definidos, sem “talvez”:**

| Participante | Papel no ensaio |
|---|---|
| **ChatGPT** | **executa G1/G2/G3** e apresenta seu parecer |
| **Arena Casa** | **executa G1/G2/G3** e apresenta seu parecer |
| **Auditor-Mestre** | **executa G1/G2/G3** (percurso do território dele: ciência e protocolo) e apresenta seu parecer |
| **Auditor-Estrutura** | **não executa G1/G2/G3** — percurso do território dele: conferir **contagem, digitais, coerência estrutura/schema/materialização** e registrar achados (observador + registrador estrutural; escolha do operador, aceita por ele) |

- Os **quatro resultados** são comparados **como resultados do ensaio** — não são “4 votos científicos”.
- **Não há maioria.** Concordância entre os quatro **nunca** substitui a fonte primária.
- Ao fim: todos **voltam aos territórios**.

**Piloto oficial (NÃO muda):** ChatGPT dedicado + Arena dedicado + Claude dedicado, análises cegas e independentes — só essa equipe mede o método.

---

## Atenções já encontradas (do teste até agora)

- Lista bruta tem artigo de muitas doenças → **isso o G2 filtra** (é pra isso que ele serve)
- 3 nomes de autor corrigidos na consolidação (`De Picker, *.` etc.) — arrumar **antes** de congelar
- Claim na tela veio resumido; o oficial é o do Bloco (completo) — o Bloco manda
- Sem data da busca no pool — anotar a data quando rodar
