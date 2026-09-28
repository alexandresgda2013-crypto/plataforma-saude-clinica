# DELIBERAÇÃO — FLUXO DO CLAIM CLÍNICO
## Parecer do Auditor-Mestre, dentro do escopo do L-NT

**2026-09-18** · Objeto: `PROPOSTA DE FORMALIZAÇÃO DO FLUXO DOS CLAIMS CLÍNICOS`
**Verificado contra:** Arquitetura §6 (deveres da NT) · L-NT minuta 1 · kit clínico ancorado 9/9 · B1 V7 `6e2c2979…`

---

## VEREDITO: **B — concordância com ajustes**

Um ajuste é estrutural e precisa ser resolvido antes do L-NT fechar. Os outros três são de precisão.

---

## 1. O ajuste estrutural: o fluxo desenhado não tem rota para a ciência do claim

O §6 da arquitetura divide o trabalho da NT em dois deveres distintos, e a distinção é decisiva:

> 1. **consumir o conhecimento** da Biblioteca correspondente;
> 2. **utilizar as Evidências/Vínculos** necessárias à **rastreabilidade**.

Biblioteca = conhecimento. Evidências/Vínculos = rastreabilidade. São papéis diferentes, e a NT tira conhecimento de um só lugar.

O fluxo proposto manda o claim clínico aprovado para **Evidências/Bibliografia → N1 → N2 → NT**. A Biblioteca Canônica não aparece no percurso (§3 e §10 da proposta). A consequência, se o fluxo for adotado como desenhado:

> **A afirmação validada pelo claim clínico nunca se torna conhecimento.** A evidência é catalogada (N1) e vinculada (N2), mas a afirmação que ela sustenta não tem rota até a NT, porque a NT não tira conhecimento de vínculos.

O claim aprovado ficaria cientificamente inerte: auditado, com PMIDs verificados, e sem poder dizer nada no laudo.

Isso colide de frente com o L-NT minuta 1, onde a regra **NT-02** exige que todo `claim_origem` exista na Biblioteca. Sob o fluxo desenhado, NT-02 fica insatisfazível para claims clínicos — e eu teria de escolher entre reprovar todos eles ou abrir a porta que a regra existe para fechar.

**Não é problema de redação.** É a pergunta que a proposta precisa responder: *a Biblioteca Canônica continua sendo a única fonte de conhecimento da NT?*

### Duas saídas coerentes

**(i) Claim clínico é insumo de evidência, não de conhecimento.** A afirmação do claim aprovado entra na **Biblioteca da entidade correspondente** pelo rito normal — que é o que o §5.5 da arquitetura já manda ("a Biblioteca de origem explica a relação; a correspondente contém o aprofundamento do objeto") — e o N1/N2 carrega a rastreabilidade. **O fluxo precisa de uma bifurcação, não de um caminho:**

```
CLAIM APROVADO
     ├── afirmação  →  BIBLIOTECA da entidade  →  (conhecimento, §6 dever 1)
     └── evidência  →  N1 → N2                 →  (rastreabilidade, §6 dever 2)
                                      ↓
                                     NT
```

É a saída que recomendo. Preserva a fonte única de conhecimento, não altera contrato nenhum, e o L-NT fica como está.

**(ii) Claim clínico é segunda fonte de conhecimento.** Então o §6 dever 1 precisa ser emendado, o L-NT ganha um segundo namespace de origem com regras próprias, e o princípio "Biblioteca = fonte científica primária" muda. **Isso é alteração arquitetural — opção C, não B** — e eu não a recomendo sem necessidade demonstrada.

### O tamanho do problema, medido

Sob a saída (i), um claim cuja afirmação não exista na Biblioteca produz N1/N2 que unidade nenhuma consome — órfão em sentido novo. Hoje isso seria a regra, não a exceção: **39 dos 49 PMIDs do kit não estão na V7**, e o wiring claim→biblioteca é **zero**. Não é argumento contra a proposta; é a medida do trabalho que a bifurcação implica, e ela deve estar na mesa.

---

## 2. Precisão sobre os "35 claims"

A proposta usa 35 como se fosse um conjunto fechado. Medi o kit ancorado:

| Medida | Valor |
|---|---|
| Claims-alvo citados na Lista Canônica | **41** |
| Claims com entrada no Bloco de Estado | **22** |
| Alvos **sem** entrada | **21** |
| Status dos 22 | 8 `aprovado` · **14 `aprovado_com_ressalva`** |

Três consequências para o piloto. O universo não é 35 — é 41 alvos com 22 trabalhados. "Concluir os 35" significa fechar **21 claims ainda sem entrada**, e é bom que o esforço seja dimensionado com o número certo. E **quase dois terços dos aprovados têm ressalva** — o item 13 da lista de decisões da proposta ("procedimento para claims aprovados com ressalva") não é detalhe de borda: é o caso majoritário. A ressalva precisa ter destino declarado em N2, ou ela se perde na materialização, que é precisamente o tipo de perda que este projeto passou seis rodadas corrigindo na B1.

---

## 3. O claim clínico já carrega os campos de N1 e de N2 — e um deles eu preciso

Medição no Bloco de Estado:

| Vira N1 (a referência) | Vira N2 (o vínculo) |
|---|---|
| `pmid` 158 · `autor` 37 · `ano` 41 · `nivel` 39 · `especie` 25 | `comparador` 48 · `achado` 52 · `papel` 36 · `evidence_role` 22 · **`uso` 23** · `moderadores` 22 · `statement` 22 |

A separação que a proposta faz entre "que artigo é este" e "o que ele sustenta" **corresponde a campos que já existem no claim**. Isso sustenta a viabilidade do derivador do §11 e é um ponto forte da proposta.

Registro o que me interessa diretamente: **`uso` está em N2 na proposta.** É o campo que pedi no L-NT (regra N-4) e que impede evidência pré-clínica de virar base de sugestão clínica. Hoje não existe no acervo. **Com esta proposta ele entra pela porta certa** — e isso, sozinho, já justifica a rodada.

---

## 4. Uma observação sobre papéis, que faço por dever e não por resistência

A proposta atribui ao Auditor-Mestre "coordenar a transformação do resultado em N1/N2". Isso me põe a **produzir** o artefato que depois alguém confere.

Até aqui a mesa funcionou porque eu audito e a casa mede — inclusive medindo-me, e já me pegou em quatro erros reais (V-14 não implementada, ramo morto no reparo, falso positivo do matcher, escopo errado nas contagens do kit). Se eu passar a produzir N1/N2, essa função some para esses artefatos, salvo se o Auditor de Estrutura assumir o papel adversarial completo sobre eles — não só conformidade de schema, mas fidelidade claim→N1→N2.

Não é objeção; é condição. **Produção e auditoria do mesmo artefato não devem ficar na mesma mão**, e foi exatamente isso que tornou a B1 auditável.

---

## 5. Concordâncias sem ressalva

- **§8, transversalidade:** concordo. O claim clínico como ferramenta transversal aos 146 IDs é a leitura certa, e tem consequência direta para o contrato do Motor: **a tipagem de risco da D-08** (contraindicação, interação) virá de intervenção, suplemento e exame — e só nasce se o claim clínico alcançar esses domínios. Hoje a D-08 tem cobertura de teste parcial justamente por isso.
- **§9, o que não deve acontecer:** a lista está correta e completa. "Elevar uma evidência apenas porque o claim foi aprovado" é a formulação exata do risco.
- **§4, Claim Kit ≠ L-05:** correto. São etapas, não concorrentes.
- **§11, derivador só depois:** correto. Especificar ferramenta antes de confirmar o fluxo seria construir sobre a pergunta em aberto.

---

## 6. O que peço para fechar

1. **Decidir entre (i) e (ii)** do item 1. Recomendo (i), com a bifurcação desenhada.
2. **Declarar o destino da ressalva** em N2 — 14 dos 22 dependem disso.
3. **Confirmar o número real do piloto**: 41 alvos, 22 trabalhados, 21 em aberto.
4. **Nomear quem audita os N1/N2 produzidos**, se a coordenação ficar comigo.

Nada disso bloqueia o L-NT minuta 2 — exceto o item 1, que decide se a regra NT-02 permanece como está ou ganha um segundo namespace. **Escrevo a minuta 2 assim que essa decisão for registrada**, e ela cabe em uma linha.

---

*Medições desta rodada: §6 lido integralmente no arquivo de arquitetura em meu poder; contagens de claims por regex sobre a Lista Canônica e o Bloco de Estado ancorados (sha `3252a920…` e `0a630dba…`); cobertura PMID kit × V7 reaproveitada da trilha 33, replicada por mim na rodada do kit. Camada declarada: substring case-sensitive sobre o texto integral dos arquivos.*
