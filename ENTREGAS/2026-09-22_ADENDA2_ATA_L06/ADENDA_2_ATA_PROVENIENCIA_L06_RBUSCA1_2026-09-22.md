# ADENDA 2 À ATA DE PROVENIÊNCIA DA L-06 — buscar direito (regra R-BUSCA-1)
**casa (agente Arena) · 2026-09-22 · Rodada 65 · trilha 78: 10/10 medidas verdes**

> ## SUA AÇÃO (operador)
> 1. **Encaminhar esta adenda aos dois projetos** (mestre e comentador) — ela alinha o mapa dos três lados: todo mundo passa a procurar e a creditar da mesma forma.
> 2. **A aprovação da L-06 continua destravada.** A rev.5 já diz o certo no §6.3 (conceito do mestre, redação do comentador). A sua frase segue a mesma: *"Aprovo como vigente a L-06 — Minuta 3 consolidada rev.5, digital 601c1f18, de 21/09/2026."*
> 3. Se concordar, **aceitar a regra R-BUSCA-1** (abaixo) como régua comum da mesa — qualquer frente poderá cobrar dela qualquer "N×" que a casa publicar.

---

## 1. O que o operador achou — e está certo

A minuta 1 do mestre, **PARTE 4 (Determinismo), item 2 (Simetria), linha 97**, diz literalmente:

> *"Os degraus 5 e 6, que distinguem papéis, produzem rótulos **atribuídos por relação**, não por posição."*

A casa havia publicado "0× na minuta 1" e creditado tudo ao comentador. **O veredito estava errado.** Obrigado pela pescada — é assim que a mesa funciona: quem mede também é medido.

## 2. Autópsia do erro (com a linha de código, para não virar lenda)

Três falhas de procedimento, todas da casa:

1. **A régua quebrou no acento.** A trilha 74 (linha 40 do script) e a trilha 75 (linha 43) procuraram na minuta 1 o padrão de 7 letras `atribui`. A minuta 1 tem `atribuídos` — o sétimo caractere dela é `í` (i com acento), então o padrão não casa e o teste devolveu zero. Um zero fabricado por 1 byte de diferença.
2. **Régua assimétrica dentro do mesmo teste.** Na trilha 75, linha 43, a minuta 1 foi medida com 7 letras (`atribui`) e a RESPOSTA_10 com 6 (`atribu`). Duas réguas no mesmo teste — proibido a partir de hoje (o dito "o relatório não seguiu a fonte de pesquisa").
3. **Fonte trocada no segundo item.** Sobre o "não substituir silenciosamente": a ata registrou a raiz do conceito na RESPOSTA_10 (casa, l.79). Medição nova: a frase-raiz *"falta de dado vira afirmação de coexistência"* está na **minuta 1, linha 79 (mestre, 15/09)** e aparece **0× na RESPOSTA_10**. No conserto de um erro, a casa ainda errou o crédito a favor de si mesma. Confessado abaixo.

**E a regra nova já me pegou uma vez nesta mesma tarde:** na trilha 78, o primeiro teste saiu VERMELHO porque o radical `atribu` também casa com "atribuir força" no TextoM (linha 169) — outro sentido ("falso amigo do radical"). Radical encontra candidatos; **o veredito só sai depois de ler a linha que casou**. A regra me corrigiu antes de publicar — é para isso que ela existe.

## 3. Mapa corrigido final dos dois itens (vale a partir de 2026-09-22)

| Item | Conceito / raiz | Forma-regra (redação normativa) | Onde a rev.5 aponta |
|---|---|---|---|
| "Atribuição por relação, nunca por posição" | **Minuta 1, l.97 — PARTE 4 (mestre, 15/09)** | **TextoH Parte 6.3, l.229-230 (comentador)** | §6.3: *"Conceito: minuta 1 do Mestre, §4 · Redação desta frase: Comentador"* — **está certo, não mexe** |
| "Não substituir silenciosamente por campo parecido" | **Minuta 1, l.79 (mestre, 15/09):** *"desce silenciosamente a escada… falta de dado vira afirmação de coexistência"* | **TextoH Parte 8, l.278 (comentador)** | mantido: redação creditada ao comentador no rascunho arquivado |

O retrato final: **o mestre trouxe as ideias na minuta 1; o comentador vestiu as duas no formato de regra; a rev.5 já divide assim.** O que muda é só o meu histórico, que dizia "órfãos da minuta 1".

## 4. REGRA R-BUSCA-1 — a régua comum de busca e ausência (permanente)

Toda afirmação de contagem da casa ("N×", "0×", "ausente") passa a carregar seis campos obrigatórios:

1. **Corpus fechado:** a lista exata dos arquivos medidos, com a digital de cada um. Acabou o "e outros documentos".
2. **Padrão exato:** a frase literal buscada, entre aspas.
3. **Família de flexão:** o radical mínimo usado, escolhido para pegar todas as flexões conhecidas, **sem cruzar a fronteira de uma vogal que possa receber acento** (foi exatamente aí que `atribui` falhou); e a lista das formas que o radical cobre.
4. **Trinca de cada ocorrência:** arquivo + número da linha + trecho literal — e a leitura da trinca (o falso amigo morre aqui).
5. **Comando gravado:** script em trilha, reexecutável por qualquer frente.
6. **Nível do veredito, declarado:** L1 = forma exata · L2 = família/flexão · L3 = conceito (com citação literal obrigatória). **"Ausente" como veredito final só sai depois dos três níveis.** Um "0×" publicado sem nível declarado **não vale** — fica válido apenas o escopo em que foi medido.

E duas cláusulas permanentes: **mesma régua para todos os corpora do mesmo teste** (sem o 7-letras-de-um-lado, 6-do-outro); **toda correção de atribuição vira adenda datada, nunca reescrita silenciosa** — o que erramos fica no registro, com a correção ao lado. É a mesma simetria que cobramos dos colegas.

## 5. O que fica corrigido, e onde (append-only — nada é apagado)

- **Ata de proveniência (r62)** — mapa final, linha dos "2 órfãos": corrigida pela Tabela do §3 acima.
- **Adenda 1 (r63)** — seção "órfãos confirmados": idem.
- **Réplica final (r64), §3** — a confissão C77-1 já apontava a flexão; faltava dizer que **a partilha da rev.5 (Conceito: mestre · Redação: comentador) é a forma correta final** e que o "0×" antigo só valia no nível da forma exata (L1). Dito aqui.
- **Trilhas 74 e 75** — os vereditos C04 ficam no JSON original (história) com esta adenda como correção referenciada.
- **STATUS simples 62 e 63** — a frase "não estão na minuta 1" lê-se agora: "a forma-regra não estava; a ideia estava, na linha 97".
- **decisoes_B1.md** — correção registrada na rev.72.

## 6. O que NÃO muda (medido na trilha 78)

- Rev.5 intacta: digital `601c1f18…` re-medida hoje. Texto dela **já correto** no §6.3 e na frase-ponte — **sem emenda nº 4**; esta adenda não pede tocar no documento.
- Nenhum byte dos cinco artefatos, nenhum número duro (244 pares · 41 claims · matriz · trilha 77 11/11 · equalidade `4217cc63…` · `c863b8ed…`/`8a8ff986…` exatos).
- Estado da mesa: falta só a sua frase de aprovação (e, opcional, o rodapé do `f8ec8b72…`, no timing que você escolher).

## 7. Confissões datadas da casa (append-only)

- **C78-1 (2026-09-22):** publiquei "0× na minuta 1" medindo com o padrão de 7 letras `atribui`, cego ao `í` de `atribuídos`, e com régua assimétrica (7 letras na minuta 1, 6 na RESPOSTA_10) no mesmo teste. O zero era artefato de busca no nível L1 e foi publicado como ausência de conceito (L3). Corrigido na Tabela do §3; impedido pela R-BUSCA-1.
- **C78-2 (2026-09-22):** no conserto, creditei a raiz de "falta de dado vira afirmação de coexistência" à RESPOSTA_10 (casa) quando ela é da **minuta 1, linha 79 (mestre)** — fonte trocada, e por acaso a meu favor. Corrigido: raiz = mestre; norma-redação = comentador; casa = mediadora que errou e corrige com evidência.

Saudações da bancada,
**casa (agente Arena)** · env-arena · 2026-09-22
*Trilha 78: 10/10 (script + JSON na produção) · regra nova: R-BUSCA-1 · 0 ciência · mestre e comentador alinhados por esta adenda.*
