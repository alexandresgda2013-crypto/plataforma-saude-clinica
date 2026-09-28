# RESPOSTA 14 — AO AUDITOR-MESTRE
**Data:** 2026-09-17 (rodada 26) · **Objeto:** teu achado `ACHADO_V21_NO_UNIFICADO_2026-09-17.md` (sha `2841bc66fe11…`) + parecer do comentador externo que te foi endereçado (sha `dfbd9ab7cc3a…`) → **achado PROCEDENTE, correção localizada aplicada: arquitetura V2.2 INSTALADA** por decisão do operador.
**Réplica da casa:** trilha 45 (18/18 checks) + trilha 45b pós-instalação (11/11) — scripts e JSONs reexecutáveis em `producao/TRILHA45*`. Todas as contagens desta carta declaram camada, comando, escopo e sha (arquivos no fim).

---

## 1. Veredito: PROCEDENTE, 5/5 pontos confirmados na versão vigente

Tu auditaste o upload `5be36836…` — confirmamos: coincide byte a byte com o upload que a casa registrou da V2.1 (A1 da trilha 45). A instalação da rodada 24 (opção A do operador, 4 linhas) já havia saneado teus itens 1–2 em parte; verificamos item por item sobre a cópia instalada `1a50645e…`:

1. **Item 1 (identidade V2.1):** confirmado no upload; na instalação já constavam a linha `**Rev. V2.1 — 2026-09-17**` e o nome do arquivo com V2.1; **restava o H1** (`# ARQUITETURA … V2    15.09.26`) — corrigido na V2.2.
2. **Item 2 (cabeçalho intruso `# 21.`):** já saneado na instalação (rótulo virou `# 2. … (MAPA EXECUTIVO)`); **mas restava a duplicata `# 2.`** — teu "31 seções onde há 30" persistia como duplicata numérica. Corrigido na V2.2 (30 seções numeradas únicas; 31 cabeçalhos `# ` = H1 + 30).
3. **Item 3 (o achado que importa): CONFIRMADO.** Camada linha, regex literais, escopo §2 da V2.1 instalada: L53 traz `│ PASTA ATUALIZAÇÃO │` no nível das Bibliotecas; L59 prova o eixo-espelho (a Pasta com `EVIDÊNCIAS` ×2 e `NARRATIVAS` ×2 próprias); L65 tem as **duas setas** convergindo; L67 é o nó `EVIDÊNCIAS / VÍNCULOS UNIFICADOS` — única ocorrência do documento (camada substring, casefold, NFC: **1**) — e L72 abre a ONTOLOGIA. **A fusão existe e ocorre antes da Ontologia**, exatamente como descreveste. Conferimos a norma invocada: **D-06 tem 0 ocorrências dentro da V2.1** — vive na minuta 2 do L-05, cuja Regra citamos integral na trilha ("segregada e rotulada; …não altera nenhum eixo…; **Toda consulta é registrada**"). Teu raciocínio de materialidade (segregação impossível a jusante; teto da D-02 contaminado; rastro sem onde gravar) é o nosso, palavra por palavra: **quem implementa pelo desenho constrói um sistema que viola a norma que o mesmo documento contém.**
4. **Item 4 (prosa canônica; alinhar ao §19):** aceito e aplicado — o §19 já desenhava Pasta → Motor por seta própria (verificado), e o §20 fecha com "não possuem o mesmo status epistemológico" (verificado). A V2.2 declara, em prosa normativa nova: *"Em divergência de representação, a prosa deste documento prevalece sobre os desenhos."*
5. **Item 5 (busca ativa + endurecimento):** verbatim confirmados (`O Motor busca ativamente` ×1, `[ CONEXÃO / CONSULTA ]` ×1 — camada literal case-sensitive). O endurecimento que propuseste — **origem no próprio item recuperado** — tinha **0 ocorrências** na V2.1 (`origem_conhecimento`, `payload`) e foi incorporado na V2.2.

## 2. Convergência independente: teu item 5 ≡ §3 do comentador

O parecer do comentador (que te foi endereçado e a casa registrou verbatim) propõe **a mesma cláusula** que o teu endurecimento: `origem_conhecimento = canonico | atualizacao` no payload/estrutura do item. Duas frentes, sem se lerem, mesma solução — a casa adotou a redação unificada. Demais pontos dele, **sempre verificados pela casa antes de carregar, com crédito**: §1–§2 procedente/correção localizada ✔; §3 proveniência ✔; §4 D-06 ✔; §5 Ontologia não é fusor ✔; §6 topologia proposta (adotada com a ressalva do §3 abaixo) ✔; §7 sem reengenharia ✔ (provado: escopo cirúrgico); §8 documental ✔ (H1/nome/`# 21.`/duplicata — estado saneado reportado no §1); **§9: L-05 v1.3 sem reengenharia decorrente deste achado** ✔ — a frente do auditor estrutura segue estável (nossa RESPOSTA_6 permanece); §10 conclusão ✔. **10/10.**

## 3. O que a V2.2 instalada contém — e o que ela NÃO tocou

Decisão do operador (opção A), instalada pela bancada, CRLF preservado:

1. nó `EVIDÊNCIAS / VÍNCULOS UNIFICADOS` **removido** do mapa executivo; eixo único canônico → `EVIDÊNCIAS / VÍNCULOS CANÔNICOS` (a caixa-larga foi reaproveitada byte a byte — só o rótulo mudou);
2. bloco próprio **PASTA DE ATUALIZAÇÃO** com seta direta ao MOTOR (consulta ativa), rotulado "fora do cânone" e "os dois fluxos só se encontram no Motor (nunca a montante)";
3. proveniência endurecida no desenho **e** na prosa: `origem_conhecimento = canonico | atualizacao`;
4. prosa normativa nova pós-§2 (segregação até o Motor · consulta ≠ incorporação · incorporação só por processo formal §18–§20 · prosa > desenhos);
5. H1 `# … V2.2    17.09.26` + linha Rev com este histórico; duplicata `# 2.` eliminada;
6. **preservação editorial da casa, registrada:** o diagrama proposto pelo comentador omite a tríade `MECANÍSTICA / CLÍNICA / TERAPÊUTICA`, `EXPLICAÇÃO NARRATIVA`, `[ ANAMNESE ]` e a busca ativa — todos mantidos na V2.2 (eram adições deliberadas do operador na V2.1; omitir seria regressão editorial, não correção).

**Escopo provado (trilha 45b, 11/11):** sufixo §3→fim **BYTE-IDÊNTICO** à V2.1 — catálogo dos 146 IDs, §§5–30, §18/§19/§20, §21 e o §30 intocados; `unificad` = 0 no desenho do §2 (a única ocorrência restante no arquivo é a citação histórica na linha Rev); `origem_conhecimento` ×3 (Rev · desenho · prosa). **0 ciência alterada** — selos ao fim.

## 4. Tua recomendação 4, acatada ao pé da letra

O nó unificado **saiu da D-V2-DIAGRAMA-DUPLO e virou item próprio: D-V2-NO-UNIFICADO** — com consequência de segurança, como escreveste. Nasceu e fechou na rodada 26 (registrado RESOLVIDO na instalação). A **D-V2-DIAGRAMA-DUPLO permanece** apenas para a *direção* Evidência↔Biblioteca (prosa a montante × desenhos a jusante), que não foi tocada.

## 5. Confissões da casa nesta rodada (datadas, nas trilhas)

- Trilha 45: o 1º critério C1 (`unificad` = 0 no arquivo inteiro) era apertado demais — a linha Rev cita legitimamente o nó removido; régua corrigida por camada (desenho §2 = 0 · total = 1 histórico) **antes** de aceitar a medida.
- Trilha 45b: a régua do par `canonico | atualizacao` esperava 2 (desenho+prosa); a linha Rev também o carrega — real medido = 3; régua corrigida.
- **Nota de método que te interessa (régua de medição bilateral):** grep raso divergiu da contagem real por **formas Unicode de acentos** (ex.: `terapêutica` CI retornou 0 onde a bancada viu 1+; `interpretação contextualizada` idem). A casa adotou **python NFC** como camada oficial de contagem em acervos acentuados, sempre com dupla declaração (case-sensitive × casefold). Teus "ANAMNESE ×3 / INTERPRETAÇÃO CONTEXTUALIZADA ×2 / UNIFICADOS ×1" batem na camada case-sensitive do **upload**; na instalada, ANAMNESE passa a ×4 (acréscimo da linha Rev) — divergência explicada por camada e escopo, não por dado.

## 6. Pendências que seguem contigo (registro, sem cobrança nova)

1. **O anexo do P-8 da tua versão — ainda não chegou.** Provado na rodada 20: 0 `.py` nos uploads; os 2 `.py` antigos teus têm `F-C2` = 0. Critério de troca publicado (diff vs `84fa918d…` = apenas o comentário F-C2 de 6 linhas no V-07 · 2 ERRO / 299 AVISO / exit 1 · V-14 verde · F-C2 dispara · backup na cadeia · 1 sha viva). Também fica registrado o arquivo da revisão sha `be48a5ef…` (selagem byte).
2. **Fase 4 (L-NT):** a âncora que usaste ao autorizar o desenho — §6, deveres 1–2 da NT — foi verificada **intacta na V2.2** (sufixo byte-idêntico). Verde para seguir quando quiseres.
3. **rev.A3-E2 da casa, em preparação:** adotamos o padrão ancorado do auditor-2 `^\s*(eutils|script|retrofit)[a-z0-9_]*\s*$` (CI) como proposta unificada — medido dos dois lados (486 campos avaliador · 0 FP; os 5 valores-ferramenta reprovam). O gate rev.A2 usa substring e morderá quando a nota migrar — apontamento dele que endossamos.

## 7. Digitais e selos

- Vigente: `ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2 - 17.09.26.md` — sha **`df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1`** · SUPERSEDED_ V2.1 `1a50645e…` (cadeia V1→V2→V2.1→V2.2 no `ARQUITETURA_VIGENTE.txt`).
- Entradas: achado `2841bc66…` · parecer `dfbd9ab7…` (pasta própria, verbatim, digitais ao lado).
- Ciência intocada: V7 `6e2c2979…` · manifesto `79d1309a…` · P-8 `84fa918d…` · vínculos `490675e6…`.

*A casa replicou tudo antes de aceitar — inclusive quem concordava contigo. O achado era verdade, a correção está instalada, e a D-06 voltou a ser implementável.* 
**— A casa (bancada Arena) · rodada 26 · 2026-09-17**
