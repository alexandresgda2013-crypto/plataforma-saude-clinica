# PARECER SOBRE A B1 V6 E CAMINHO PARA O TRIO PILOTO

**Auditor-Mestre · 2026-09-13 · rodada 3 do dia**
**Objeto:** `B1_NEUROINFLAMAÇÃO_V6_CANONICA.md` (1.324 linhas) + Resposta nº 2 da casa.

---

## 0. O que pude e o que não pude verificar

Verifiquei: sha256 da V6 (`d8f41662…` — **confere exatamente** com o declarado), diff integral V5→V6 (32 linhas, todas rastreadas ao REGISTRO item 10), texto das correções C3 e C4, conformidade P20, e coerência interna de classificadores.

**Não pude verificar** a afirmação central da carta — *P-8 = 0 ERRO / V-02 = 0 / 237 refs · 274 vínculos · 237 ledger*. Vocês enviaram apenas o `.md`. A camada `/Evidencias/` é exatamente onde os erros se esconderam nas duas rodadas anteriores (AUD-049 nasceu de uma correção que parou na prosa). **Um auditor que aceita "0 ERRO" sem o JSON está aceitando por declaração** — que é a regra que os dois lados combinaram não usar. Para a próxima rodada, o pacote mínimo é: canônica + `01/02/03` + `_manifesto` + `vinculos` + `ledger`.

---

## 1. C3 (Osimo 2019) — **ENCERRADA**

Execução correta e completa. A prosa do §11.1 agora lê:

> "…27% dos pacientes com depressão apresentam inflamação de baixo grau **conforme o limiar de PCR adotado na meta-análise de origem** (Osimo et al., 2019)[MA; humano], com razão de chances ~1,46 versus **controles pareados** (a faixa de referência e o ponto de corte operacional residem no módulo C-LAB — P20…)"

Três acertos que registro nominalmente:
- restaura o vínculo número↔limiar sem fixar corte — resolve a colisão P20×interpretabilidade que apontei;
- separa corretamente as duas metas Osimo: **2019** sustenta prevalência e OR; **2020** sustenta "subgrupo, não universal". Eram claims distintos ancorados na referência errada;
- acrescentou "controles pareados", que estava no abstract e faltava na V5.

Os números conferem com a fonte primária que verifiquei na rodada anterior (27%, IC 21–34%, 30 estudos; OR 1,46, IC 1,22–1,75, 17 estudos). **Nenhum overclaim.** R7(b) declarado executado no manifesto — não verificável sem o JSON.

## 2. C4 (BLOCO_11.4) — **PARCIALMENTE EXECUTADA**

A declaração é exemplar e vai além do que pedi: não-validação explícita, sensibilidade/especificidade/VPP/falso-positivo **desconhecidos**, uso autônomo **vedado**, e uma nota de circularidade que enuncia o problema com precisão — *"C prediz A por construção — não confirma; a carga classificatória pertence a A e B"*.

**Mas o algoritmo não mudou.** A tabela continua:

| Classificação | Critério A | Critério B | **Critério C** |
|---|---|---|---|
| Compatibilidade **alta** | ≥2 marcadores | ≥3 de 6 | **≥1 presente** |

Se C não pode confirmar e a carga pertence a A e B, **C não pode ser condição necessária para o tier mais alto** — e continua sendo. O comportamento produzido é idêntico ao da V5:

- **falso positivo inalterado:** obesidade + apneia (C ✓, e PCR/IL-6 elevadas *por* eles) + fadiga, queixa cognitiva e dor difusa (B ✓) → "Compatibilidade alta" por confundimento puro;
- **falso negativo novo, não discutido:** paciente com 2 marcadores alterados e 3 itens de fenótipo, **sem nenhum fator de contexto**, fica barrado de "alta" — exatamente o caso de inflamação sem causa sistêmica aparente, que é o subgrupo mais interessante do ponto de vista mecanístico.

Foi eu quem escreveu que se audita o **comportamento produzido, não a declaração**. Preciso ser consistente: declarar a circularidade e mantê-la operante é transparência, não correção. **C4 permanece aberta.**

*Correção mínima sugerida (decisão do autor científico):* mover C para fora da tabela, como modulador do a priori e da especificidade — não como critério de linha. Alternativa: manter C na tabela, mas invertido (contexto presente **reduz** a especificidade de A, portanto **rebaixa** de "alta" para "indeterminada" quando A depende só de marcadores inespecíficos).

---

## 3. Achado novo e grave: **três taxonomias de classificador, nenhuma autoritativa**

Este é o achado mais importante desta rodada e **bloqueia o motor**, não a biblioteca.

O código de duas letras (MA/EC/OB/ML) aparece em quatro camadas com significados que não coincidem:

| Camada | O que o código indica | Concordância com o Módulo 09 |
|---|---|---|
| Prosa `(Autor, ANO)[XX]` | desenho, como usado na frase | **37,1%** (76/205) |
| Apêndice `AUTOR_ANO[XX]` | desenho, herdado da geração | **21,3%** (50/235) |
| Arquivo do Módulo 09 (01/02/03) | balde onde a ficha mora | referência (200 de 236 em `01_pmids` = OB) |
| `desenho_estudo` da ficha | texto livre | não normalizado |

**71 referências têm classificador diferente entre prosa e apêndice.** Exemplos: `Zdilar 2000` prosa [OB] × apêndice [MA]; `Comai 2022` prosa [EC] × apêndice [MA] × ficha em `01_pmids` (OB) × `desenho_estudo` = "EC humano"; `Su 2018` prosa [MA] × apêndice [EC] × ficha OB × desenho "MA (omega-3…)".

E **7 citações usam classificadores diferentes de si mesmas dentro da própria prosa**: Bull 2009 [EC]/[ML], Chen 2024 [EC]/[ML], Huang 2023 [ML]/[OB], Mehta 2020 [EC]/[OB], Yang 2024 [EC]/[ML], Yehuda 2016 [EC]/[ML], Zhang 2025 [EC]/[ML].

Por que isso é grave e por que agora: **o motor precisa ponderar evidência por desenho de estudo** — meta-análise pesa mais que revisão, ensaio humano pesa mais que modelo animal. Hoje não existe um campo único e confiável que diga o desenho. O único portão que checa classificador (`tipo_classificador` vs arquivo, no framework) valida a taxonomia menos informativa das três — a do balde, que diz "OB" para 85% do acervo.

Um motor determinístico construído sobre isso ou ignora o desenho (perde a hierarquia de evidência que é o coração da plataforma) ou lê uma camada arbitrária (produz ponderação errada e não reprodutível). **Isso precisa ser resolvido dentro do L-05, antes do JSON modular** — não depois.

*Ressalva de honestidade:* é possível que a intenção da prosa seja registrar o **papel da evidência naquele claim** e não o desenho do estudo — o que seria legítimo. Mas então são duas dimensões distintas usando o mesmo vocabulário de duas letras, sem declaração de qual é qual. Peço que a casa declare a semântica normativa antes de eu classificar isto como erro em vez de ambiguidade. De qualquer modo, **a inconsistência prosa×apêndice de 71 casos é defeito em qualquer das duas leituras.**

Portão novo recomendado — **V-15**: o classificador de uma referência tem de ser idêntico em prosa, apêndice, ficha e ledger; divergência é ERRO.

---

## 4. Outros achados na V6

**AUD-066 · MODERADO — o cabeçalho contradiz os próprios artefatos.** A V6 continua declarando que o status PROVISÓRIO está condicionado à *"revisão cega humana dos **59** vínculos de alto risco"*. A fila operacional que vocês mesmos produziram tem **108**; o gate desta rodada reporta **39** claims de alto risco; a carta fala em **~58**. São quatro números para a mesma condição, e é a condição que define quando a biblioteca deixa de ser provisória. Escolham um, derivado do artefato, e amarrem o cabeçalho a ele.

**AUD-067 · MODERADO — a ambiguidade Mehta foi resolvida pela metade.** Há **três** obras distintas na prosa e apenas dois tokens: L255 `(Mehta et al., 2020b)[OB; revisão sistemática]`, L647 `(Mehta et al., 2020)[EC; humano, fMRI]`, L717 `(Mehta et al., 2020)[OB; revisão]`. L647 e L717 compartilham o mesmo token com desenhos incompatíveis, e o apêndice atribui `MEHTA_2020[OB]`, que casa com L717 e conflita com L647 — sendo que L647 é justamente a que vocês definiram como a "reward". A observação-L717 que vocês deixaram aberta é correta, mas o problema é maior: **o token da reward está classificado como a revisão.**

**Conforme.** P20 limpo (zero cortes numéricos residuais). Versionamento correto (V5→V6 por mudança de conteúdo, V5 preservada). Nenhuma citação nova introduzida fora do rito [AT]. Nenhum overclaim novo. As 4 re-âncoras foram decididas por autoria conferida no PubMed, com a candidata descartada nominada — método correto.

**Sobre a ida-e-volta da inicial de autoria:** a casa tentou `Huang P et al.`, mediu que o V-05 derrubava a cobertura a 94,1%, e reverteu no mesmo dia, deixando o registro. Isso é o comportamento certo. E a sugestão de hardening é boa: **vou aceitá-la** — o V-05 passa a reconhecer opcionalmente `(Sobrenome Inicial et al., ANO)`, porque APA e ABNT admitem a inicial desambiguadora e a série terá mais homônimos. A ferramenta não deve ditar a convenção citacional.

---

## 5. VEREDITO SOBRE A B1 V6

### **APROVADA COM RESSALVAS — habilitada como BASE PILOTO, não como canônica definitiva**

Faço a distinção porque ela responde diretamente ao seu objetivo.

**O que está aprovado:** a B1 V6 pode ser usada **agora** como fonte para construir a Narrativa Transversal e o JSON Modular do trio piloto. A ciência do corpo está em bom estado, as duas correções GRAVE das rodadas anteriores estão fechadas e verificadas contra fonte primária, a rastreabilidade da prosa é a melhor da série, e o histórico de versões é auditável.

**O que impede o selo definitivo:**
1. **P-6 não executado** — a revisão humana de especialista é a única barreira real contra erro de ciência, e nem eu nem a casa a substituímos. Isto sozinho mantém o PROVISÓRIO, e vocês já decidiram corretamente que fica para o fim.
2. **C4 aberta** — declaração sem mudança de comportamento.
3. **Taxonomia de classificador** — não impede a biblioteca; impede o motor.
4. **Não verifiquei a camada de evidência** desta versão.

---

## 6. CAMINHO PARA O TRIO E PARA O TESTE DO MOTOR

Você quer aprovar um trio + quatro bibliotecas de apoio e ver o motor rodar. A ordem abaixo é a que minimiza retrabalho, dado o que esta rodada revelou.

### Bloco 1 — antes de escrever qualquer NT ou JSON

| # | Entrega | Motivo |
|---|---|---|
| 1.1 | **Contrato do Motor Clínico (L-05)** | Define o consumidor. Sem ele, NT e JSON são escritos no escuro |
| 1.2 | **Taxonomia única de desenho/força de evidência** | O achado §3 mostra que hoje o motor não consegue ponderar. Entra dentro do 1.1 |
| 1.3 | **Regra de precedência entre bibliotecas (L-06)** | Quando B1 e B9 divergem, quem vence — sem isso a saída não é determinística |
| 1.4 | **`achado_verbatim_fonte` (L-13)** | Única forma de tornar mecânica a checagem de direção. Piloto: as 34 metas da B1 |
| 1.5 | **C4 decidida** | Precisa estar resolvida antes de virar JSON, ou a circularidade entra no motor |

### Bloco 2 — o trio piloto

| # | Entrega | Critério de aceite |
|---|---|---|
| 2.1 | `SCHEMA-NT v1.0` + gerador | NT não pode elevar força epistemológica: portão de não-elevação |
| 2.2 | **NT-B1** | 100% das afirmações rastreáveis a frase da B1 V6; zero claim novo |
| 2.3 | `SCHEMA-JSON-MODULAR v1.0` + gerador determinístico | Round-trip: o JSON reproduz a semântica sem perder incerteza |
| 2.4 | **JSON-B1** | P-8 estendido: 0 ERRO; toda incerteza da prosa preservada em campo |

### Bloco 3 — bibliotecas de apoio, no menor recorte possível

Recomendo **não** produzir as quatro inteiras. Para testar o motor basta o recorte que a B1 exige:

- **C-LAB / Exames:** só os marcadores que a B1 cita — PCR, IL-6, TNF-α, sTNFR2, KYN/TRP, TSPO-PET. É aqui que moram os cortes numéricos que a B1 deferiu; **sem isso o §11.1 não é executável**, e o "27%" continua pendurado.
- **Intervenções:** só as que a B1 usa como sonda mecanística — anti-TNF, minociclina, ômega-3, IFN-α (como causa, não intervenção).
- **Suplementos:** só ômega-3, no mesmo recorte.
- **Cenários clínicos:** um único cenário sintético.

Recorte pequeno é vantagem, não limitação: o objetivo é testar a **arquitetura**, e superfície menor significa que qualquer falha do motor é atribuível.

### Bloco 4 — o teste

Caso clínico sintético → anamnese → IDs → mecanismos ranqueados → sugestões → relatório.

**Critério de aprovação (o seu, com o meu acréscimo):**
1. 100% das frases do relatório rastreáveis até uma frase de biblioteca canônica;
2. P-5, P-8 e portão de saída verdes;
3. **o motor deve descartar corretamente ao menos um mecanismo** — se ele só sabe confirmar, não é raciocínio, é recuperação;
4. **rodar duas vezes com a mesma entrada e produzir saída idêntica** — determinismo é o requisito que a Filosofia impõe ao decidir não ter IA interna;
5. **um caso-armadilha**: paciente com obesidade e apneia sem depressão inflamatória. Se o motor devolver "Compatibilidade alta" para B1, o C4 não foi resolvido — e o teste terá encontrado isso antes de um paciente real.

---

## 7. Sobre replicar para as outras 15

Mantenho o critério de duas bibliotecas limpas, e acrescento uma observação de escala medida nesta sessão: **1.509 vínculos da série (60,5%) ainda estão ancorados em rodapé**. A B1 levou três rodadas bilaterais e ~20 trilhas para chegar aqui. Replicar o mesmo esforço 15 vezes de forma manual não termina.

Por isso a reancoragem de série **precisa virar script antes de virar trabalho** — e a B1 já provou que 75% dela é automatizável (12 de 16). O que não deve ser replicado é o ciclo artesanal; o que deve ser replicado é a ferramenta.

---

*Verificações desta rodada: sha256 da V6 conferido; diff V5→V6 linha a linha; 217 chaves de citação e 317 tokens de apêndice cruzados; taxa de concordância de classificador medida contra as 236 fichas; P20 varrido. A camada de evidência da V6 não foi enviada e portanto não foi auditada — nenhuma afirmação deste parecer depende dela.*
