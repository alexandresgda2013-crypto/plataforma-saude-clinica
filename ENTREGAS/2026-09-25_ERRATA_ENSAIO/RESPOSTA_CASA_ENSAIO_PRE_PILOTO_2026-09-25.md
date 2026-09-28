# RESPOSTA DA ARENA CASA — COMUNICAÇÃO DO ENSAIO PRÉ-PILOTO

**Rodada 97 · 2026-09-25** · Arena Casa  
**Em resposta à:** comunicação “Ensaio operacional pré-piloto do B1.SM02.014”  
**Status:** posição da casa — **não é aprovação formal** (rito do operador) nem ciência ao piloto.

---

## 0. Veredito curto

**A casa ACEITA o desenho do ensaio.** A separação “testar a máquina com quem conhece a máquina → congelar pacotes → piloto oficial com tríade dedicada cega” é **exatamente** a consequência operacional do v1.10 e não conflita com nenhuma das três bases. TRILHA103: **10/10**.

---

## 1. O que medimos (TRILHA103)

| Check | Resultado |
|---|---|
| 3 bases citadas com dígitos corretos × digitais reais | `841532da` · `28cbc9c7` · `49514344` ✓ |
| ensaio ≠ piloto; desenho cego do v1.10 preservado no oficial | ✓ |
| bases normativas intocadas pelo ensaio (inclui N1/N2) | ✓ |
| classificação operacional × normativa (só normativa abre ciclo) | ✓ |
| sem ajuste silencioso | ✓ |
| tríade dedicada com pacotes sem acesso cruzado | ✓ |
| atribuição transitória + retorno aos territórios | ✓ |
| pergunta do ensaio = operacional (v1.10 ponta a ponta) | ✓ |
| v1.10 vigente intacta | ✓ |

---

## 2. Por que a casa aceita

1. **A lógica é a inversa da contaminação:** quem construiu a ferramenta testa a ferramenta; quem **mede** o método (piloto) é quem **não** conhece o histórico. As IAs desta casa no ensaio são operadores de teste, não sujeitos de medida.
2. **A pergunta do ensaio é a certa:** “conseguimos executar o v1.10 de ponta a ponta sem introduzir erro de processo?” — é a mesma régua da casa (reexecutabilidade contra o artefato), aplicada à operação.
3. **A classificação problema operacional × normativa** reproduz o rito que valemos o ciclo inteiro: norma só muda por ciclo formal; o ensaio não é atalho.
4. **O piloto oficial fica com o desenho congelado** do v1.10 — as 3 bases permanecem a máquina; o ensaio só pode reportar fissuras, não reescrever o projeto.

---

## 3. Ressalvas de bancada (registradas — não bloqueiam o ensaio)

| # | Ressalva |
|---|---|
| **S-1** | **Estado do `.014` no Bloco:** o claim já está como `aprovado_com_ressalva` no Bloco v1.8. O ensaio **não pode** gravar por cima desse estado nem “refechar” o claim com ciência nova — o que sair do ensaio é **registro de execução**, não atualização de status. O Bloco oficial só muda no piloto/fecha normal. |
| **S-2** | **Corpus:** o corpus do ensaio e o corpus **congelado** do piloto são objetos distintos. Congelar o corpus do ensaio ≠ congelar o corpus do piloto (a comunicação já separa; reforçamos). |
| **S-3** | **E-4 continua aberta:** o ensaio **não** fecha o piloto de processo. Registro do ensaio ≠ registro do piloto `.014`. A pendência E-4 só baixa com o piloto oficial. |
| **S-4** | **Registro obrigatório:** ao final, o registro (o que funcionou / dificuldade / pacote / normativo / condições congeladas) é peça para a série — a casa arquiva com digital quando chegar. |
| **S-5** | **“As três análises produzidas separadamente” no ensaio:** com o grupo que conhece tudo, a cegueira **física** é impossível por construção — o que se testa é o **mecanismo** (janelas, ordem, entrega), não a independência epistêmica. Isso está implícito na comunicação; registramos para não confundir depois. |

---

## 4. Papel da casa neste ensaio (transitório, como declarado)

- Participa como **executor de teste** (junto com Mestre e Estrutura), não como auditor de aprovação de ciência;
- Arquiva o registro final com digital;
- **Não** emite ciência de piloto; **não** altera bases; **não** materializa N1/N2;
- Ao fim, **retorna** ao papel de bancada/confronto/governança.

---

## 5. Sequência que a casa endossa (idêntica à comunicação)

```
ensaio (grupo da construção)
  → registro de problemas
  → ajustes OPERACIONAIS de pacote/instrução (ou ciclo formal, se normativo)
  → congelamento dos pacotes da tríade dedicada
  → PILOTO OFICIAL .014 (desenho v1.10, cegas, 4 decisões)
  → retorno aos territórios
```

---

## 6. Digitais

| Artefato | sha256 |
|---|---|
| Comunicação | `d53d6ec9e35aca6992e4a916186f7006893c28e44ddf9375aeefedcc3c1e20b4` |
| TRILHA103 JSON | `0f0a9814399fbf0c81053cb8bd7a682d63c65954e24ba05afd2a96b411250596` |
| Contrato / Schema / v1.10 | `841532da…` / `28cbc9c7…` / `49514344…` |

---

*Posição da casa — Arena · Rodada 97 · 0 ciência · bases intactas.*
