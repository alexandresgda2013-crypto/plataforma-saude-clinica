# PARECER DA CASA Nº 2 AO AUDITOR DE ESTRUTURA
## Análise da proposta L-05 v1.0 — schema de evidência e vínculo multi-entidade

**De:** a casa (sob delegação científica e de engenharia do operador, 2026-09-14)
**Para:** auditor externo de estrutura (via operador) · **cópia:** Auditor-Mestre
**Data:** 2026-09-14
**Objeto:** `L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.0_PROPOSTA.md` + `schema_referencia_v1.json` + `schema_vinculo_v1.json`
**Método:** réplica empírica integral antes de qualquer aceite — trilha 25 (`producao/25_replicacao_L05_auditor_estrutura_2026-09-14.{py,json}`, rev.1), rodada contra o acervo real B1 V7 (237 refs / 274 vínculos / manifesto 2.10).

---

## 0. Veredito executivo

**VIÁVEL E CORRETO — a casa APROVA a proposta como base normativa do L-05/1.2 nos níveis 1–2, com 6 ajustes nomeados (R1–R6) e as 5 decisões respondidas abaixo (§4) com provas documentais.**

Antes do adjetivo, o fato que mais pesa a favor: o próprio autor escreveu a especificação como código e rodou contra o acervo antes de entregar — e nós rodamos de novo aqui. Na nossa execução, o schema dele **pegou um defeito real que os quatro portões oficiais da casa não pegavam** (§2-A9). Especificação que roda contra o acervo se paga; a frase final do documento dele vale para os dois lados.

## 1. Réplica da medição — 16 alvos verificados

| # | A proposta disse | A casa mediu (trilha 25) | Resultado |
|---|---|---|---|
| A1 | `uso`: 244/274 conformam o enum clínico | **244/274** (`contexto_mecanistico` 178, `clinico` 37, `gap_pesquisa` 29); enum existe no PROMPT v4.2 L1440 | ✔ exato |
| A2 | os 30 `B1_v2` = as 30 levas `/v2` | **30 × 30 × 30 — interseção perfeita**, ninguém sobra dos dois lados | ✔ exato |
| A3 | `evid_role`: 66/6/2/133/30 | **66 human_clinical, 6 human_experimental, 2 post_mortem, 133 preclinical_mechanistic, 30 review** | ✔ exato |
| A4 | 175 desenhos brutos distintos | **175** | ✔ exato |
| A5 | `secao_origem`: 21 valores, 100% B1 | **92 valores em 3 formatos**: 232 `BLOCO_XX` puro · 30 prefixados com o mecanismo · 12 `APENDICE_CORPUS`. Tese qualitativa: **274/274 dentro da B1, zero em exame/cenário/suplemento** | ◑ literal impreciso, **tese confirmada** |
| A6 | 20 `redirecionado_clinico` | **20** (dist.: eligible 242 · redir. 20 · nao_aplicavel 11 · nao_avaliado 1) | ✔ exato |
| A7 | `status_auditoria` ficha: 165 VALIDADO_G3_IA; 162 a separar | **165 / 162** | ✔ exato |
| A8 | `origem_pipeline`: 50 compostos | **50** | ✔ exato |
| A9 | 1 `verification_status` inválido (= full-text P-6) | 1 — mas a **identidade era outra**: ver §2-A9 | ◑ contagem ✔, atribuição ✗ |
| A10 | `forca_biologica_conexao` 274/274 vazio | 274/274 | ✔ exato (re-medido) |
| A11 | catálogo valida `id_oficial` | os 3 ids de exemplo **existem** no catálogo; mas **`_ids_oficiais.json` não existe como arquivo** (ver R2) | ◑ ver R2 |
| B0 | desenho precisa classificar 237 | **0/237** no enum proposto hoje — confirma o mapa | ✔ exato |
| C | migração majoritariamente mecânica | simulação completa da casa: após derivar âncora principal + `trilha`, **a única violação restante é o `uso` dos 30 `B1_v2`** (curadoria já mapeada); 0 ids fora do catálogo | ✔ confirmado por construção |
| D | E2 sem violações | vínculos: 0 · fichas: 0 **antes** da errata; 1 **falso-positivo** após a errata — ver R3 | ◑ ver R3 |
| E | (não declarado) — invariante da âncora | "exatamente 1 `principal: true`" **não é expressável** no draft-07 entregue | ver R1 |
| — | migração = "derivar de secao_origem" | precisa de 2 regras adicionais | ver R4 |

## 2. O que a casa corrigiu hoje por causa da proposta (provando o método)

**A9 — errata T25 (confessada e já aplicada).** O único valor de `verification_status` fora de enum em 237 fichas era **REF_OSIMO_2019**: `confimado_G1_G3_2026-09-13` — valor-livre com typo, escrito pela própria casa na rodada C3 (a ficha melhor do acervo, ironicamente), e que nenhum portão validava. A atribuição da proposta ("é a dívida de full-text") não bateu: a dívida de full-text mora nos **vínculos**, não nas fichas — o inválido real era este. Correção: `verificado` (estado já documentado: G1 eutils + G3 com abstract colado no ledger AUD_B1_0238; o vínculo-irmão VINC_B1_0274 sempre constou assim). Backup bit-a-bit em `antigos/historico/`, entrada datada no manifesto (**2.9 → 2.10**), irmãos auditados (grep global: valor-livre único). **Portões re-rodados e verdes:** gate rev.A2 APROVADO (exit 0) · checklist 41/41 · framework 0 ERRO/236 · P-8 0 ERRO/26.

## 3. Análise — ciência

1. **A separação em três eixos é a decomposição epistemologicamente correta.** `natureza` (o que foi estudado), `desenho` (como), `uso` (para que o sistema o emprega) são dimensões independentes que hoje colidem — `review` em `evid_role` é o caso exemplar (revisão é desenho; o objeto revisto é que é a natureza). É o mesmo raciocínio dos eixos ortogonais que o próprio projeto consagrou para `evid_role × forca_causal × grau_maturidade` (PROMPT v4.2 L1438), estendido uma camada acima. Aceito sem ressalva.
2. **Resolve a raiz do §3 na camada de evidência — sem fingir que resolve a outra metade.** As taxonomias conflitantes que o Auditor-Mestre mediu vivem em dois lugares: nas fichas/vínculos (esta proposta resolve, e bem) e **nos `[XX]` da prosa e do apêndice da canônica** (84 divergências + 7 autodivergentes da trilha 21 + os 11+1 tokens da trilha 24) — esses continuam precisando de decisão normativa própria (semântica do `[XX]`) que o 1.2 deve produzir, agora com o vocabulário certo: o `[XX]` colapsava exatamente desenho × papel-no-claim. A casa registra: **proposta ≠ substituto do 1.2-normativo da canônica; é a espinha dorsal dele nos níveis 1–2.**
3. **`papel: refuta` é cientificamente necessário e filosoficamente exigido** — achado negativo não desaparece por não confirmar. Aceito com destaque.
4. **A regra 5 ("ancorar não promove evidência") é a barreira epistêmica certa.** Sem ela, uma âncora em `exame_il6` poderia ser lida como atestado de utilidade clínica do marcador — exatamente a classe de erro que a canônica combate com `[EXT]`. Aceito e recomendado a virar texto do próprio L-13.
5. **`desenho_estudo_bruto` nunca descartado** — é a mesma liturgia bit-a-bit da casa (V5→V7, backups sempre). Aceito como regra de fidelidade fonte.
6. **Ressalva científica (não-obstáculo):** o enum de `desenho_estudo` cobre a epidemiologia clássica mas o acervo neuro-psiquiátrico tem formas frequentes sem casa óbvia (associação genética humana tipo Klengel 2013 — nem coorte nem caso-controle no sentido clássico; GWAS; estudos de PET in vivo). Sem um **manual de decisão** acompanhando o enum, o balde `outro` concentraria a ambiguidade que a proposta veio matar. A casa se oferece para redigir a árvore de classificação **a partir dos 175 valores brutos reais**, com triagem semiassistida (pubtype eutils + MeSH + bruto) e margem confessada por registro — mesma disciplina da L717. (R5)

## 4. Análise — engenharia de software

1. **Decisão 1 → A, sem hesitação, e com prova documental.** O enum clínico `clinico | contexto_mecanistico | gap_pesquisa` é o enum oficial de **geração** — PROMPT FINAL v4.2, L1440. O acervo não derivou: foi **escrito** sob esse contrato. A régua v3.1 é do SCHEMA-CLAIM MECANISMO — outra pergunta ("qual o papel desta evidência na estrutura do mecanismo?"). Sumarizando o bug: o gate comparava dados da trilha A com a régua da trilha B; o ramo-morto `nucleo_causal` (0 ocorrências) era sintoma disso, não defeito dos dados. **Enum-união + discriminador `trilha`** é o sum type correto: preserva 244 valores corretos, não reescreve histórico, e torna o INFO [10] do gate rev.A2 uma verificação **trilha-aware** (cruza `trilha × uso`) em vez de alerta de fumaça perene. Opção B seria normalização destrutiva de dados corretos — reprovada por princípio (a casa não remapeia sem ganho semântico). **Único pedido factual:** o rótulo "SCHEMA-CLAIM v1.2 (trilha clínica)" não tem arquivo correspondente no workspace da casa — o que temos é o enum no PROMPT v4.2 e a LISTA CANÔNICA v1.2 (outro objeto). Se existe um SCHEMA-CLAIM v1.2 clínico fora da casa, pedimos o pointer para arquivá-lo no repositório normativo; se o nome era informal para "o contrato do PROMPT v4.2", a casa corrige a liturgia de citação.
2. **Ancoragem multi-entidade com `principal` única é a normalização certa.** Relação N:N sem duplicar evidência (P20), com a posse ("em cuja biblioteca a evidência foi trabalhada") separada das relações declaradas. Resolve os 20 `redirecionado_clinico` (o destino vira âncora `fronteira`, não texto solto — e `destino_sugerido` ausente deixa de ser campo fantasma). Prepara o chão do motor (C-LAB: "evidências do marcador IL-6" vira consulta). Aprovado o desenho.
3. **Transição com espelho + invariante 100% antes de aposentar colunas** (`secao_origem`/`mecanismo_origem`) — é o strangler pattern correto, mesma liturgia das nossas próprias transições medidas. Sem janela de divergência silenciosa.
4. **Ajuste R1 — invariante não-expressível.** O schema garante ≥1 âncora (`minItems`) mas **não pode garantir exatamente-1 `principal: true`** em draft-07 (contagem por valor não é expressa). Não é defeito fatal — é fronteira natural: invariante global sai do declarativo e vai para portão imperativo. Proposição da casa: nova checagem no P-8 (ou V-17 no lado do Auditor-Mestre): "exatamente 1 principal ∈ catálogo por vínculo".
5. **Ajuste R2 — o objeto `_ids_oficiais.json` não existe.** O catálogo oficial é o MD `01_norteadores/1º IDS_OFICIAIS.md` (a trilha 25 parseou 103 ids dos blocos JSON embutidos; os 3 exemplos da proposta existem nele). "Validar contra o catálogo" precisa de um artefato oficial derivado: script versionado + sha registrado + regra de fonte-única (o MD manda). A casa oferece o derivador (a trilha 25 já é o embrião dele).
6. **Ajuste R3 — E2 por substring morde o legítimo (falso-positivo demonstrado).** Após a errata T25, a ficha REF_OSIMO_2019 ficou inválida pelo `allOf` do schema: seu `g3_verificado_por` = `IA_casa (rito [AT]; abstract eutils colado no ledger AUD_B1_0238)` contém a palavra "eutils". Medido na trilha 25 (`D_E2 = ["REF_OSIMO_2019"]`). O avaliador é legítimo; a nota-metodológica menciona a **fonte** do abstract — e todo abstract do acervo veio do eutils. A regra E2 proíbe **assinar como ferramenta**, não **citar a ferramenta** na descrição do rito. Correções possíveis: ancorar o padrão (assinatura exata/padrões delimitados de ferramenta) ou separar `g3_verificado_por` (nome puro) de nota metodológica em campo próprio. **A casa não apagará informação legítima para satisfazer regex** — o projeto ajusta o padrão, não o dado. Registrar também que o gate [8]/E2 tem o mesmo formato de teste por substring; hoje não morde porque vínculos não carregam a nota.
7. **Ajuste R4 — migração da âncora principal tem 2 regras além do "derivar de secao_origem".** Medido: (a) **normalização de prefixo** — 232 registros `BLOCO_XX` puro × 30 prefixados; a âncora `id_oficial` é sempre `mecanismo_B1_neuroinflamacao`, o escopo carrega `BLOCO_XX[/sub]`; (b) **12 `APENDICE_CORPUS`** — são selos de índice, não afirmação mecanística; 7 deles já são os casos nomeados da fila P-6 do gate [11b]. Nomeá-los como exceção na migração (a casa sugere `papel: fronteira` + `escopo: "APENDICE_CORPUS"` + nota, até a P-6 julgar). Fora isso, a migração é de fato mecânica — a simulação completa da casa fecha só com os 30 `B1_v2` pendentes de curadoria.
8. **Ajuste R5 — o enum de desenho precisa do manual** (ver §3.6). E definir, para revisões/meta-análises, que `natureza_evidencia` refere-se **ao material revisto** (não ao formato): McColgan 2026 é meta-análise **de modelos animais** — com o 3-eixos ela fica `preclinica_in_vivo + meta_analise` sem contorção; Osimo 2019 fica `humana_observacional + meta_analise`. O schema suporta; o manual precisa dizer isso explicitamente, senão a Decisão 2 gera nova ambiguidade em outro balde.
9. **Compatibilidade confirmada por construção.** Os schemas só **adicionam** campos e regras aos níveis 1–2; nenhum portão oficial (gate rev.A2, checklist 41/41, framework, P-8, censo) quebra com a adoção — os campos novos começam em modo *shadow* (medir e reportar) e só viram bloqueio após a migração medir 0 não-conformes. Mesma política de INFO→FALHA já usada no gate rev.A2.

## 5. As 5 decisões — respondidas pela casa com provas

| # | Decisão da casa | Prova / consequência |
|---|---|---|
| **D1** | **A** (duas trilhas, `trilha` declarado) | PROMPT v4.2 L1440 (enum clínico de geração); v3.1 L148 (enum mecanístico). Réguas por pergunta distinta; dados corretos preservados; INFO [10] vira verificação trilha-aware. Pedido factual: pointer da "v1.2" (§4.1). |
| **D2** | **Transitório com data + triagem semiassistida ANTES da leitura** | Os 30 `review` não precisam nascer como leitura cega: pubtype (eutils) + espécie (MeSH) + `desenho_estudo_bruto` classificam com alta confiança a maioria (ex.: os MAs com bruto "Meta-Analysis; Systematic Review" + MeSH Humans). O residual provado-mínimo vai à leitura; a confirmação nominal pode acompanhar a P-6 humana. Valor transitório com data de expiração: aceito. Nunca classificar sem texto restando — margem confessada por registro. |
| **D3** | **B1 ANTES de B2, começando pelos 20 redirecionados** | A B1 é o piloto canônico ratificado dos dois lados; o teste do motor (Bloco 4) roda **sobre a B1** e precisa das âncoras secundárias C-LAB/cenários; e os 20 redirecionados já trazem o destino em `g2_motivo` — gradiente mais barato, exatamente como observado. Esperar B2 adiaria o próprio piloto. |
| **D4** | **Contornada por prova documental** | `citacao_confirmada` é **default de geração**: PROMPT v4.2 L1290/L1313 — *"default true"*, com `false` só na ressalva explícita do GPM. Não há origem oculta a auditar: há um default sem carga verificacional. Recomendação da casa: no L-05 oficial, marcar **deprecated** (sem remover — proibido remover sem norma), descrição corrigida para "default de geração, não-atestado", mantido banido como via de portão (já na rev.A2). Com a origem provada, o `_pendente_decisao` encurta. |
| **D5** | **Ampliada pela casa: são TRÊS escopos, não dois — e renomear agora é o remédio errado** | O contrato oficial da série (`contrato.py` L62) já documenta a ambivalência por **arquivo**: enum de vínculo × enum de ledger, quase disjuntos (interseção = NAO_LOCALIZADO) — e a ficha é o terceiro escopo (`VALIDADO_G3_IA`, valor LEGADO com tabela de conversão registrada na harmonização D1/2026-09-11). Renomear hoje = breaking em ≥3 scripts oficiais + 16 bibliotecas. Caminho da casa: (i) **declarar formalmente os três escopos no L-05** — o schema de referência já faz isso para a ficha, com o texto certo na descrição; (ii) aceitar `status_auditoria_nota` para separar veredito×ressalva (162 exatos — número dele batendo); (iii) dívida de longo prazo nomeada **D-L05-CAMPO-DUPLO**: renomeação com espelho no próximo major, quando o custo for escolha, não acidente. |

## 6. Ajustes consolidados pedidos (R1–R6)

- **R1**: invariante "exatamente 1 principal" sai do JSON Schema → portão imperativo (P-8 da casa ou V-17 do mestre).
- **R2**: criar `_ids_oficiais.json` oficial derivado do MD (script versionado + sha; a casa oferece).
- **R3**: E2 com padrão ancorado (ou nota metodológica em campo separado) — falso-positivo demonstrado.
- **R4**: regras de migração da âncora: normalização de prefixo + 12 `APENDICE_CORPUS` nomeados.
- **R5**: manual de classificação de `desenho_estudo` (árvore a partir dos 175 brutos; casa escreve) + regra "natureza = material revisto" para sínteses.
- **R6**: `citacao_confirmada` com descrição corrigida (default de geração; deprecated; fora de portão — prova: PROMPT v4.2).

## 7. Encaixe no plano do trio

O Bloco 1 (L-05 1.1 → 1.2 → L-06 → L-13) está aceito bilateralmente. Esta proposta cobre o **1.2 nos níveis 1–2** com qualidade que a casa não precisa reescrever — a casa entra com o **1.1 (Contrato do Motor)**, com o **1.2-normativo da canônica** (semântica do `[XX]` + V-15, usando o 3-eixos como vocabulário para desambiguar) e com o manual R5; e pede ao Auditor-Mestre que tome ciência desta peça na mesma mesa (cópia enviada), pois ela muda o mapa antes prometido: D-A2-USO-ENUM deixa de ser "deriva" e vira "régua trocada — resolvida por trilha declarada".

## 8. Estado da casa após este ciclo

- Manifesto 2.10 (errata T25) · canônica V7 intocada (sha `6e2c2979…`) · portões: gate rev.A2 APROVADO · 41/41 · framework 0 ERRO/236 · P-8 0 ERRO/26 · censo 32/32.
- Novas dívidas nomeadas: **D-L05-CAMPO-DUPLO** (D5, longo prazo) · **D-L05-IDS-JSON** (R2) · **D-L05-E2-PATTERN** (R3) · **D-L05-MANUAL-DESENHO** (R5). Nada silenciado.

**Conclusão:** viável (migração majoritariamente mecânica — confirmada por simulação completa na casa), correto (epistemologicamente limpo, engenharia sóbria, aderente a P11/P20/Filosofia), e já utilidade-provada (achou defeito real no piloto). **Aprovado.** Enviando v1.1 com R1–R6, a casa instala em modo shadow na B1 e prepara o piloto de retroancoragem dos 20 redirecionados como primeira execução — com a mesma liturgia de sempre: medida, datada e reversível.

---

*Rastreabilidade: trilha 25 rev.1 com todos os números, listas e o mini-validador draft-07 usado na validação (subset declarativo: type/required/properties/enum/pattern/minLength/minItems/items/allOf-if-then-const-not) · manifesto 2.10 + backup `antigos/historico/02_meta_analises_pre_errataT25_verification_osimo_2026-09-14.json` · decisoes_B1.md rev.9 · CHANGELOG ABERTURA/RESULTADO 6. Provas documentais citadas: PROMPT FINAL v4.2 L1290/L1313/L1440 · SCHEMA-CLAIM MECANISMO v3.1 L148 · contrato.py L62 (dois enums por escopo) · IDS_OFICIAIS.md (103 ids parseados).*
