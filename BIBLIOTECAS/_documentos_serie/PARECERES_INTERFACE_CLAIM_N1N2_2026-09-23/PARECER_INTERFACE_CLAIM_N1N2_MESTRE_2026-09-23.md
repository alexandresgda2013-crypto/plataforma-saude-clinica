# PARECER TERRITORIAL — INTERFACE CLAIM CLÍNICO → BIBLIOTECA → N1/N2
## Resposta à pergunta binária dos dois auditores, no território do Auditor-Mestre

**Auditor-Mestre · 2026-09-23**
**Pergunta:** *"A solução de interface Claim Clínico → Biblioteca → N1/N2 é compatível com os contratos e princípios que cada território protege? Existe algum impedimento técnico ou epistemológico?"*
**Ancorado em:** N1 v1.3 `b06660fd…` e N2 v1.4 `d96ad15b…` (lidos no projeto), Schema-Claim v1.2 `56dc0e94…`, minha Deliberação de 18/09, L-06 rev.6 vigente.
**Anti-contaminação:** não li o encaminhamento paralelo ao Auditor-Estrutura; ativos estruturais de schema são território dele.

---

## RESPOSTA CURTA

**Compatível, sim — a arquitetura da interface é correta e é a menor alteração suficiente.** Mas há **um impedimento epistemológico** que precisa ser resolvido antes da primeira materialização, e ele não está no diagrama: é a equivalência entre `aprovado_com_ressalva` e `direcao_suporte = condicional`, proposta no §9 da carta. Ela junta dois conceitos que não são o mesmo, e se materializada como está, deforma o significado do claim.

---

## 1. O que está compatível, e por quê

**O núcleo da hipótese é o que eu recomendei em 18/09, agora em forma de engenharia.** O Comentador chegou, por outro caminho, à bifurcação: o claim não cria sistema paralelo; N1 é bibliografia única, N2 é a relação, a afirmação entra na Biblioteca pelo rito. Confirmo campo a campo:

- **Claim ≠ N1 ≠ N2.** O claim é registro do processo de validação; o N1 é o artigo; o N2 é o vínculo. Três objetos, três papéis. Correto.
- **Um PMID, um N1, muitos N2** (§5). Medi: a Bibliografia V7 tem 0 duplicidade de `pmid_oficial` em 237 fichas, e o acervo já opera 274 vínculos sobre menos referências. O padrão "1 N1 : N vínculos" **já é o padrão vigente** — a interface não inventa nada, reusa.
- **`claim_id_origem` é proveniência, não catálogo** (§10). Confirmo nos bytes: no N1 v1.3 o campo é `string` escalar, e no acervo os valores preenchidos são um claim_id cada, nunca lista. A leitura do Comentador está correta: um N1 registra de onde nasceu; o uso múltiplo vive nos N2 via `claim_id`. **Compatível.**
- **`origem_pipeline` sem `CLAIM_KIT_CLINICO`** (§11). O enum selado é `[BUSCA_FERRAMENTA, GPM_BRIEFING, INSUMO_EXTERNO_AUDITADO, REANCORAGEM, AUDITORIA_EXTERNA]`. Acrescentar um valor de proveniência é alteração pequena e coerente, e deve passar pelo ciclo editorial do N1 — não incorporar unilateralmente, como o Comentador já disse. **Compatível, via ciclo de schema (território do Estrutura).**

Nada disso reabre a bifurcação nem a fonte única de conhecimento. A interface **respeita** o §6 da arquitetura: a afirmação vira conhecimento na Biblioteca, a evidência vira rastreabilidade em N1/N2. É a forma correta.

## 2. O impedimento epistemológico — §9, ressalva ≠ condição

O §9 propõe a cadeia:

```
aprovado_com_ressalva → PARCIALMENTE_CONFIRMADO → direcao_suporte=condicional → condicao
```

Mecanicamente, ela fecha: os três enums existem no N2 v1.4 e a especificação torna `condicao` obrigatória quando `condicional`. **Mas os dois extremos da cadeia não significam a mesma coisa**, e é aí que o impedimento vive.

**`aprovado_com_ressalva`** (Schema-Claim v1.2) = o claim está aprovado, com uma ressalva registrada. As ressalvas reais do kit são coisas como "efeito por sexo não é consistente entre estudos", "heterogeneidade alta", "achado de subgrupo". São **qualificações sobre a força ou a generalidade** da afirmação.

**`direcao_suporte = condicional`** (N2 v1.4) = a evidência sustenta a relação **sob uma condição de aplicação**, e essa condição vai no campo `condicao`.

São conjuntos que se **cruzam**, não que coincidam:

- "sustenta em mulheres, não em homens" → é ressalva **e** é condicional. A cadeia funciona.
- "efeito real mas heterogêneo entre estudos" → é ressalva, **não é condicional** — não há condição de aplicação; há incerteza sobre a magnitude. Forçar isso em `condicional` obriga a inventar uma `condicao` que a ciência não afirmou. **Isso é fabricação de condição** — a mesma classe de erro que a L-06 combate no degrau 3 ("não completar a condição por inferência silenciosa").
- "achado robusto, mas de uma só coorte" → é ressalva de **maturidade**, não de condição. O destino certo é `grau_maturidade`, não `condicao`.

**O impedimento:** materializar todo `aprovado_com_ressalva` como `condicional` + `condicao` obrigatória **força uma condição onde às vezes não há nenhuma** — e o campo `condicao` é lido pelo degrau 3 da L-06, que acabou de virar norma. Uma condição fabricada na materialização entra no motor como se fosse ciência, e a L-06 a usará para "resolver" conflitos que na verdade não têm condição alguma. O erro nasceria na interface e se propagaria até a resolução de concorrência.

**Correção que proponho (território epistemológico):** a ressalva do claim não mapeia para um único destino. A materialização precisa **rotear** a `nota_ressalva` conforme o tipo:

| Tipo de ressalva | Destino no N2 |
|---|---|
| condição de aplicação ("em X, não em Y") | `direcao_suporte = condicional` + `condicao` |
| heterogeneidade / inconsistência de magnitude | `status_auditoria = PARCIALMENTE_CONFIRMADO`, `condicao` **vazia**, ressalva em campo de nota |
| maturidade / evidência única | `grau_maturidade` rebaixado, sem `condicao` |

Esse roteamento **não é derivável automaticamente** — exige ler a ressalva e classificá-la, o que é decisão científica. Portanto: **a materialização de `aprovado_com_ressalva` não é campo derivado (classe C da carta); é campo que exige auditoria (classe I).** A matriz da carta precisa mover a ressalva de "derivável" para "decisão necessária".

## 3. Um ponto de ordem que confirmo (não é impedimento, é precondição)

A casa já apontou, e subscrevo: o diagrama do §13 põe Biblioteca e N2 nascendo no mesmo passo de materialização. Não podem. O `trecho_ancora` do N2 é, por contrato, cópia literal da frase sustentada — e a frase **só existe** depois que a afirmação entra na Biblioteca. A ordem é **Biblioteca primeiro, N2 depois**, nunca simultâneos. Medido: `usado_em_biblioteca: nao` em 22/22 claims do kit — hoje nenhum atravessou essa porta. É precondição, não defeito da proposta; mas o diagrama deve mostrá-la em série, não em paralelo.

## 4. Auditoria (item I da carta) — reafirmo o parecer de ontem

Mantenho o que respondi na P4 territorial: a **fidelidade claim→N1→N2 nunca é atestada por quem materializou**. Conformidade de schema é território do Estrutura; fidelidade científica (o N2 preserva a força, a direção e — agora — o *tipo de ressalva* do claim?) é território epistemológico. O roteamento de ressalva da §2 acima é exatamente o tipo de coisa que a auditoria de fidelidade tem de checar, e que a auditoria de schema não pega — um `condicional` com `condicao` bem-formada passa no schema mesmo quando a condição foi fabricada.

## 5. Veredito territorial

**Compatível com um impedimento a resolver.**

- **Sem impedimento:** a arquitetura da interface (claim ≠ N1 ≠ N2; um PMID um N1; `claim_id_origem` como proveniência; reuso em vez de duplicação; `origem_pipeline` via ciclo de schema). É a bifurcação que recomendei, e é a menor alteração suficiente.
- **Impedimento epistemológico (§9):** a equivalência `aprovado_com_ressalva → condicional` fabrica condição onde a ressalva não é condicional, e essa condição fabricada envenena o degrau 3 da L-06. **Resolver por roteamento de ressalva por tipo**, e mover a ressalva de "derivável" para "exige auditoria" na matriz.
- **Precondição:** Biblioteca antes de N2, em série.

Nenhum destes reabre os Claims Clínicos, a Bibliografia ou o modelo de vínculo — como o Comentador pediu. O único que exige decisão nova é o roteamento de ressalva, e ele é meu território porque é sobre significado, não sobre estrutura.

---

*Verificações: required e enums de N1 v1.3 e N2 v1.4 lidos no projeto; campos do Schema-Claim v1.2 (ausência de trecho_ancora/ancora_principal/ancoras/condicao confirmada); `claim_id_origem` string escalar confirmado no schema e no acervo; cadeia condicional→condicao confirmada na especificação L-05. Anexos da carta recebidos; digitais declaradas pela casa não reproduzidas byte a byte (recebi como texto).*
