# REGISTRO FINAL DO ENSAIO PRÉ-PILOTO — B1.SM02.014
## (S-4 consolidado — o que funcionou, o que travou, o que congelar)

**Data:** 2026-09-25 · **Arena Casa** · encerramento da fase de ensaio  
**Natureza:** registro de teste. **`.014` NÃO mudou de status** (segue `aprovado_com_ressalva`).  
**Não é o piloto oficial** — esse fica com a tríade dedicada cega.

---

## 1. Resposta à pergunta do ensaio

> “Com as ferramentas e pacotes atuais, conseguimos executar o COMO EXECUTAR v1.10 de ponta a ponta sem introduzir erro de processo?”

**RESPOSTA: SIM, com correções de pacote e de instrução.**

As 3 bases (Contrato `841532da` · Schema `28cbc9c7` · v1.10 `49514344`) **sustentaram a execução inteira**. Nenhum achado deste ensaio pediu ciclo normativo.

---

## 2. O que funcionou

| Item | Resultado |
|---|---|
| Pacote mínimo (Modo B) | chegou íntegro; Bloco colado fresco = vigente |
| G1 ao vivo (resolver PMID) | executável — âncoras resolvidas nas 3 janelas |
| G2 (filtro) | executável — ~80% de fundo separado sem drama |
| G3 (veredito por fonte) | executável — direção por fonte representou o caso real |
| Schema-Claim v1.3 | comportou `sentido_do_achado` + `ressalva[heterogeneidade]` sem forçar |
| As 4 decisões | produzidas nas 3 janelas |
| Cruzamento | pegou erros que sozinhos passariam (ver §3) |
| Veredito comum (3 IAs) | **suporta + heterogeneidade · status mantido** |

## 3. O que travou / deu errado (operacional — nada de norma)

| ID | Achado |
|---|---|
| E-01→G1 | Lista chegou sem PMID — custo de resolução (depois classificado como execução do G1, não defeito) |
| E-02 | Pool sem data de busca — anotar sempre |
| E-03 | Claim resumido na tela × completo no Bloco — Bloco manda |
| **E-04** | As 3 IAs rodaram G1+G2+G3 **sem entregar no meio** — corrigido com **PARADAS** (rev.2.1) |
| **E-05** | Contagem 107×92 — confirmado: mesma lista; **baseline 107** (parágrafo com DOI); 92 = outra regra |
| D-a/D-b | Execução do Mestre: 2 PMIDs errados (Setiawan/Hannestad) — fonte primária decidiu |
| D-c | “Yrondi = protocolo” da IA1 — título é resultado; confirmar no texto |
| Lista | HDAC6 fora do lote TSPO · `Li 2018` = 2 artigos · autores corrompidos |
| Estrutura | 3 achados úteis + recusa legítima de G3 (papel de observador assumido) |

## 4. Itens ADIADOS pelo operador (registrados, não esquecidos)

1. **Redirecionar artigos de outros mecanismos** (SM-03/04/08 etc. — o campo `redirecionados` do v1.10) — *antes eu fazia isso; fica para a lista do piloto*
2. **Candidatos a ID oficial** — *idem, fora do fecho de agora*

## 5. Condições congeladas para o piloto oficial

1. Lista saneada: Li×2 separados · HDAC6 fora · nomes corrigidos · Yrondi confirmado
2. Contagem única: **107 = parágrafo com DOI**
3. Data de busca anotada
4. G1 resolvido das âncoras materializadoras
5. Fundo **marcado, não apagado**
6. Instrução **rev.2.1** (com PARADAS) como manual de execução
7. Tríade dedicada cega (ChatGPT dedicado · Arena dedicado · Claude dedicado)
8. Itens adiados (§4) decididos antes ou durante o piloto — a critério do operador

## 6. Papéis — encerramento

- **Ensaio:** ChatGPT, Arena, Mestre (executaram) · Estrutura (observador + registrador — como escolhido)
- **A partir do fecho:** todos **voltam aos territórios**
- **Piloto oficial:** só a tríade dedicada, com o desenho do v1.10

## 7. Encerramento

**Fase de ensaio ENCERRADA.** Registro arquivado com digital (S-4).  
Próximo marco do projeto: **piloto oficial B1.SM02.014** — depois de sanear a lista e congelar os pacotes da tríade.

---

*Registro final do ensaio — Arena · 2026-09-25 · sha no DIGITAIS.*
