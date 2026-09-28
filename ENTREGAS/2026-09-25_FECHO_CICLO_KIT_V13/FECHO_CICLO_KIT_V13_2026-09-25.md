# ATO DE FECHO — CICLO DO KIT · SCHEMA-CLAIM v1.3 rev.3

**Data:** 2026-09-25 · **Rodada 91** · Arena Casa  
**Critério:** Comentador (ciclo do kit §12–§14) — (1) Estrutura sem ressalva ✓ · (2) Mestre sem ressalva ✓ · (3) réplica da casa TRILHA100 10/10 ✓ · (4) palavra do operador para vigência (**pendente**).

---

## 1. Atos do ciclo

| Etapa | Resultado |
|---|---|
| Minuta v1.3 (P-K1..K5) · TRILHA97 13/13 | casa propõe |
| Comentador: aprovada + V-K3 | arquivada `162423a5…` |
| Rev.2 (V-K3) · TRILHA98 10/10 | janelas |
| Mestre sem ressalva (rev.2) · Estrutura com ressalva **V-K6** | TRILHA99 9/9 · armadilha medida |
| Rev.3 (V-K6+V-K7) sha `28cbc9c7…` | casa |
| Comentador aceita rev.3 | arquivada `7b9307e6…` |
| **Estrutura → sem ressalva (rev.3)** | arquivo errado detectado e registrado; rev.3 canônica conferida |
| **Mestre → sem ressalva (rev.3)** | `fa7edc88…` upload ≡ série; sha `28cbc9c7…` declarado |
| **TRILHA100 10/10** | `ciclo_kit = ENCAVEL` |

---

## 2. O que a rev.3 estabelece (se operador aprovar)

Schema-Claim **v1.3** como próxima versão do kit clínico:

- **P-K1** `sentido_do_achado` por fonte (enum v3.1)
- **P-K2** `ressalvas[]` com tipo (3 tipos)
- **P-K3** fonte única de `condicao`
- **P-K5** `grau_maturidade_cientifica`
- **V-K1..V-K5** validadores + **V-K6** precedência (condicao_aplicacao → condicional+condicao; sentido fica no claim) + **V-K7** ausência ≠ null
- Migração sem reescrita retroativa; falha dura na materialização

**Não altera:** N1 · N2 · contrato de saída rev.2 · D1 (encerrada).

## 3. Travas que permanecem

- **P-K1/P-K2 no kit:** a v1.3 **ainda não é vigente** — ao virar, a 1ª materialização exige claims fechados com os campos;
- **P-K6** (inverte): ciclo **N2 v1.5** — `.001b` segue em espera;
- Piloto `.014` de processo: segue aberto (E-4).

## 4. Nota de método (registro central do ciclo — Estrutura)

> “O que sustentou o rigor não foi a concordância entre as mesas, foi cada afirmação ter sido reexecutável contra o artefato.” — 3ª vez que a mesma classe de erro (dois eixos colidindo) **só** apareceu ao rodar contra o schema.

Epílogo honesto: arquivo rev.2 enviado por engano; detectado pelo território; rev.3 canônica confirmada por digital antes da assinatura.

---

## 5. Próximo passo

**Sua frase de aprovação** (padrão vigências anteriores), por exemplo:

> “Aprovo como vigente o Schema-Claim v1.3 — rev.3, digital 28cbc9c7, de 25/09/2026.”

Com ela: série + ponteiro VIGENTE + CHANGELOG de vigência → depois **v1.10**.

---

*Fecho por réplica — Arena · Rodada 91 · TRILHA100 10/10 · sha no DIGITAIS.*
