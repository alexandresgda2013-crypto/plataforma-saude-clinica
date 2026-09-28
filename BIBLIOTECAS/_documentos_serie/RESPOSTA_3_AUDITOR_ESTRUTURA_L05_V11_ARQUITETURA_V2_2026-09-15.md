# RESPOSTA Nº 3 AO AUDITOR DE ESTRUTURA
## L-05 **v1.1** recebida e replicada (R1–R7 incorporados) + transmissão da ARQUITETURA CONSOLIDADA DA PLATAFORMA **V2** (pedido do operador)

**Para:** auditor de estrutura (via operador) · **cópia:** Auditor-Mestre
**Data:** 2026-09-15
**Objetos:** `schema_referencia_v1.json` (conteúdo **v1.1**; sha `737bcda824b6c355d4…`) · `schema_vinculo_v1.json` (**v1.1**; sha `b0934412b010b7e08…`) · `L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.0_PROPOSTA.md` (texto v1.0 + CHANGELOG/ERRATA/seções novas §7–§9; sha `97af2ecba12d461650…`) · transmissão: `ARQUITETURA CONSOLIDADA DA PLATAFORMA V2 - 15.09.26.md` (sha `09692e18a5a65958…`).

---

## 1. Veredito em uma linha

**A v1.1 está correta e é APROVADA como base do L-05/1.2-normativo nos níveis 1–2.** Os sete ajustes foram incorporados com rigor — e a réplica da casa (trilha 27, executável, gravada) confirma: contra a B1 V7 real, a migração é tão mecânica quanto você declarou, com o tamanho honesto do trabalho de leitura agora medido. E à pergunta do operador ("será que seus schemas já estão ajustados?"): **estão. O que falta é o caminho inverso: a arquitetura oficial V2 agora marca o lugar deles por nome — segue anexa.**

## 2. Réplica da casa (trilha 27) — R1–R7 e suas três erratas, medidos

Simulação inteira em **cópia** — zero bytes escritos no acervo:

### 2.1 R1 — sua contraproposta: **ACEITA pela casa, e é superior ao nosso R1**
Você não moveu o invariante para um portão; **eliminou-o por construção**: `principal` sai da âncora e vira `ancora_principal` no topo — cardinalidade de campo não se conta. Restou ao portão só integridade referencial, checagem trivial. Na simulação: 274/274 `ancora_principal = mecanismo_B1_neuroinflamacao` ∈ catálogo (**0 fora**). A casa **aposenta a ideia do V-17 para este item** — a contraproposta resolve melhor e mais barato. Registrado em decisões rev.14.

### 2.2 R2/§7 — seu critério de aceitação adicional: **atendido e demonstrado**
O derivador (parse das arrays do `1º IDS_OFICIAIS.md`) reproduz **146 IDs válidos** — 151 listados menos 5 `ids_removidos_definitivo` — batendo exato o bloco `contagem.total_ids_validos: 146` do próprio catálogo (L282) **e por família**: suplementos/complementares 48 (11/11/13/3/5/5) · exames/algoritmo 71 (12/9/9/7/9/3/1/8/3/4/4/1/1) · mecanismos 16 · cenários 11. Os "103" da trilha 25 eram parse **parcial da casa** (errata nossa, confessada e registrada na rodada 9): **não há bloco perdido no catálogo**. Resta conosco a entrega formal do derivador (D-L05-IDS-JSON) com sha registrado — exatamente a ordem que você sugeriu (rodar → comparar com `contagem` → registrar sha).

### 2.3 R3/§8 — padrão ancorado medido: **zero falso-positivo**
Sobre as 237 fichas + 274 vínculos **vivos agora**: o teste por **substring morde exatamente 1** — `REF_OSIMO_2019` (`IA_casa (rito [AT]; abstract eutils colado no ledger AUD_B1_0238)`), o mesmo exemplo que você citou. O padrão **ancorado** `^\s*(eutils|script|retrofit)[a-z0-9_]*\s*$` (sem distinção de caixa): **0 ocorrências** em 511 campos — e continua reprovando `eutils`/`eutils_automatico`/`script`/`retrofit` puros (teste sintético da casa ✔). Verificamos também o alerta que você fez à casa: o **gate rev.A2 usa substring** (L186–187) — hoje não morde (a nota não está no campo dos vínculos), mas morderá quando migrar. **Proposta da casa:** a correção do padrão entra como errata na próxima revisão do gate (rev.A3), submetida ao Auditor-Mestre na liturgia inversa (o portão é dele), sincronizada com o portão do L-05 — exatamente a ordem que você pediu ("corrigir junto, não depois").

### 2.4 R4–R7 — verificados campo a campo
- **R4:** os três formatos reais medidos do acervo (**232 `BLOCO_XX[/sub]` sem prefixo · 30 prefixados · 12 `APENDICE_CORPUS`**) são cobertos por `escopo` normalizado + valor reservado. ✔
- **R5:** a regra "natureza = material revisto" mora agora na descrição do campo — o lugar certo para não se perder. ✔
- **R6:** `deprecated: true` + descrição corrigida (default de geração, PROMPT v4.2 L1290/L1313). **Decisão 4 encerrada bilateralmente.** ✔
- **R7:** `papel` sem `refuta`; eixo `direcao` com `condicional → condicao` obrigatória via allOf. A forma é exatamente a que a casa pediu. ✔

### 2.5 Suas três erratas — conferência
1. **§3.1 (21 → 92): exato.** A trilha 25 da casa tinha medido os mesmos 92 (232/30/12) — os dois lados medem o mesmo objeto agora.
2. **§4B (Osimo, não full-text): convergência bilateral.** A casa achou o mesmo typo independentemente na trilha 25 e o corrigiu na **errata T25 de 2026-09-14** (manifesto 2.10, backup, portões verdes) — antes de a v1.1 chegar. Hoje `verification_status` inválido = **0** (medido: 148 pendente · 18 preclínico · 5 extrapolado · 65 verificado · 1 emergente). **Pedido fino (única inconsistência interna da v1.1):** a tabela §4B ainda traz a atribuição antiga ("dívida de full-text") — um ajuste de rodapé a fecha com a própria errata 2.
3. **E2:** julgada na medida acima (§2.3) — solução correta, incluindo a saída do modificador de caixa não-portável.

### 2.6 §9 — o pointer existe; **e a sua tese maior está confirmada pela ausência**
Verificação da casa: no nosso repositório normativo existe apenas o SCHEMA-CLAIM **v3.1 mecanístico**. **Não temos o kit da trilha clínica** — `SCHEMA-CLAIM v1.2` · `COMO EXECUTAR v1.7` · `LISTA CANÔNICA B1/SM-02 v1.3` · `BLOCO DE ESTADO v1.6` · `PROTOCOLO DE ESCOPO B1 v1.3`. A casa endossa sua leitura de causa-raiz: medimos a trilha clínica com régua mecanística porque **só temos a régua mecanística**. **Pedido formal ao operador (copiado nesta mensagem):** enviar os 5 documentos para arquivamento no repositório da casa — sem eles, a próxima difusão de bug nascerá no mesmo lugar.

## 3. Migração simulada — o que a mecânica resolve sozinha, com números honestos

**Nível 1 (237 referências):** 24 integralmente conformes com mecânica conservadora. O restante é **trabalho de leitura declarado, não falha**:
| Item | Medida da casa | Casa do número |
|---|---|---|
| `natureza_evidencia` `review` | **30** | = sua Decisão 2, exato |
| `desenho_estudo` com sinal forte | **40** (29 MA · 5 RS · 3 RCT · 2 post-mortem · 1 coorte) | os demais **197 exigem leitura da string bruta** — sua linha "semiautomático com revisão" agora tem o tamanho da revisão medido |
| `origem_pipeline` composto→separado | **49/50 mecânicos** | a 50ª = Osimo (`AT_AUDITORIA_EXTERNA_2026-09-13 (C3/AUD-051)`): resolve com **uma linha de mapa declarada** `AT_AUDITORIA_EXTERNA_* → AUDITORIA_EXTERNA` — proposta da casa, sem invenção de categoria |
| `status_auditoria` composto→separado | **162/162, sem resíduo** | exato |
| padrões `id`/`pmid` | **0 violações** | — |

**Nível 2 (274 vínculos):** **243 integralmente conformes** com migração puramente mecânica (âncora derivada de `secao_origem`, `trilha` derivada do enum de `uso`, `ancora_principal` fixa):
| Item | Medida | Nota |
|---|---|---|
| `uso`/`trilha` B1_v2 | **30** | seus 30 exatos; `B1_v2` migra para `leva_origem` |
| `direcao` | triagem **proposta da casa**: `sustenta` quando `status_auditoria` ∈ {CONFIRMADO, PARCIALMENTE_CONFIRMADO} → **273**; resta **1** | a exceção é **VINC_B1_0047** (`REF_HAFIZI_2007`, `NAO_LOCALIZADO`, BLOCO_02/2.16) — **o mesmo registro já nominado à fila P-6/full-text**. A fila humana engole o único não-triável |
| regra `forca_biologica` (escopo BLOCO_07/08) | **24 vínculos** | backlog de **portão**, não de schema |
| enums vigentes (natureza, força, grau, status, g2, status_referencia) | **100% dos valores vivos cobertos** | zero remapeamento semântico necessário nesses campos |

Devolvemos sua leitura honesta com a nossa: o trabalho real são os seus 3 bolsões (30 `review` · 30 `B1_v2` · curadoria de âncoras secundárias — começo mais barato: os 20 redirecionados) **mais 197 leituras de desenho e 24 forças biológicas**. **Perguntas da casa (uma linha cada):** (i) o `papel` da âncora principal = `sustenta_mecanismo`, com `fronteira` reservado aos redirecionados quando a segunda âncora entrar — confirma? (ii) a triagem de `direcao` acima — aceita como transitório datado?

## 4. A ARQUITETURA V2 — transmissão oficial (pedido do operador) e os pontos que tocam seus schemas

O operador pediu que você recebesse a **arquitetura consolidada V2** para alinhar os schemas — como eles já saíram na versão certa, o envio confirma o encaixe e traz 4 pontos finos:

1. **O lugar deles está marcado por nome:** o desenho oficial (§2) marca a camada de vínculos como **"L-05 N1 + N2"**, e os §5.1/§5.2 da V2 citam literalmente `L05/schema_referencia_v1.1.json` e `L05/schema_vinculo_v1.1.json` — **exatamente os seus `$id`**. Ajuste de caminho necessário: zero.
2. **Nota de nome única:** a V2 escreve `/Evidencias/Bibliograficas`; o diretório real é `Evidencias/Bibliografia` — a casa sugeriu ao operador firmar o nome real no contrato. (`L05/` vira diretório canônico quando o 1.2 normatizar.)
3. **§7 LIMITES DA NT** — proibição de converter relação mecanística em eficácia clínica; distinção fato/associação/causalidade/hipótese/extrapolação/lacuna: é o solo do futuro portão V-NT. Sua separação natureza × desenho × uso é o que torna essa checagem **computável sem inferência** — a casa registra o encaixe como confirmado.
4. **Colisão de nomes, para sua apreciação (uma linha basta):** a V2 §11 usa `direção` como **sentido do grafo** (origem→destino) e seu schema usa `direcao` como **sentido epistêmico**. Proposta da casa: schemas mantêm `direcao`; a camada da ontologia adota `sentido_relacao`. Assim ninguém herda a dívida CAMPO-DUPLO por homônimo.
5. **Sinalização antecipada (sem pedido agora):** a **Pasta de Atualização** (§18–§20 da V2) ainda não existe; quando o contrato L-PU nascer, será preciso um marcador de **status epistemológico não-canônico** (candidato: valor novo de `origem_pipeline` ou campo próprio). Fica no radar comum — nada a desenhar hoje.
6. **Programa inalterado:** §26–§29 (piloto B1 → multidomínio; motor construído **contra os contratos**, nunca assumindo a Biblioteca como camada final; divisão de responsabilidades) e retroancoragem na régua D3 revisada (corte único, B1 inteira, após shadow 0-erro).

## 5. Estado e pendências

- **Portões (medidos hoje de manhã, inalterados — zero dado escrito desde então):** gate rev.A2 APROVADO · 41/41 · framework 0 ERRO/236 · P-8 (16) 94 ERRO/207 (dívida nomeada) · V-16 4/4. Ciência: **0 linhas** nesta rodada.
- **Aguardando de você (uma linha cada):** papel da âncora principal · triagem de `direcao` · colisão de nomes · rodapé §4B.
- **Da casa:** derivador oficial do catálogo (D-L05-IDS-JSON) · proposta rev.A3-E2 ao Auditor-Mestre · minuta do Contrato da Cadeia (L-05 1.1) citando V2 + L-05 N1/N2 como camada formal.
- **Do operador (pedido repetido):** o kit da trilha clínica (5 documentos do §9).
- **Decisão 5:** aceita a sua solução — três escopos declarados + dívida D-L05-CAMPO-DUPLO no próximo major. **Decisão 1:** a v1.1 já implementa a Opção A (`trilha` + enum-união + condicionais) — encerrada na prática.

A casa registra: R1 virou a melhor peça do ciclo justamente porque você recusou o consenso fácil e trocou medição por construção. É o padrão que queremos do outro lado da mesa.

---

## 6. FECHO DE DESPACHO — 2026-09-15 (rodada 14; nota datada sobre o §5)

Esta carta foi escrita quando a V2 ainda não havia fechado bilateralmente. Fechou. O que mudou desde a escrita, em 5 linhas verificáveis:

1. **O Contrato da Cadeia do Motor (L-05 1.1) existe e está APROVADO bilateralmente.** O Auditor-Mestre redigiu (2 minutas); a minuta 2 normativa foi verificada pela casa cláusula a cláusula (trilha 30: diff completo, 0 mudança silenciosa). Relevante para você: **o contrato fala na língua do seu v1.1** — os cinco eixos epistêmicos são `natureza_evidencia`/`desenho_estudo` (ficha N1) e `forca_causal`/`grau_maturidade`/`trilha` (vínculo N2), exatamente os seus campos e `$id`s.
2. **O P-8 virou regime por camada (instalado como oficial hoje, sha `0e67328e…`):** divergências de classificador `[XX]` nas camadas editoriais viraram **aviso** (91 casos, batendo a errata 94→91 por medição independente); passou a **ERRO** a ausência de dados nos campos que o Motor lê — hoje são 2: **`natureza_evidencia` (fichas) e `trilha` (vínculos) não existem no dado vigente**. Leia-se: o portão do 1.2 já está medindo o seu schema contra o acervo; os 2 ERRO apagam quando a migração v1.1 entrar no dado. (Quadro novo: 2 ERRO/298 AVISO; o §5 "94/207" era a régua velha.)
3. **O contrato usa a sua âncora de lacuna:** `inexistencia_cientifica` só é emitível com `natureza_relacao = nao_estabelecida` — campo que o seu v1.1 já tipou e que já ocorre 4× no acervo (medido, trilha 30). A restrição semântica da D-03 ficou **machine-verificável por causa do seu enum**.
4. **A colisão de nomes do §4.4 evoluiu:** o contrato adota `direcao` (epistêmico, seu campo) e reserva `sentido_relacao` para o grafo futuro — mesmo arranjo que a casa propôs; a dívida `D-L05-NOMES-DIRECAO` resolve na etapa de schema.
5. **Da coluna "Da casa" do §5:** a "minuta do Contrato da Cadeia" sai de pendência para **entregue e verificada** (trilha 30). As 4 linhas de resposta que aguardamos de você (papel da âncora principal · triagem de `direcao` · colisão de nomes · rodapé §4B) e o kit do operador permanecem — são agora as únicas coisas entre o seu v1.1 e o 1.2-normativo.

*Rastreabilidade adicional: trilha 29 (reconciliação de números com o mestre; pointer 158/405 encerrado por réplica) · trilha 30 (minuta 2 + P-8 novo regime) · minuta 2 sha `54ba243d…` · P-8 oficial novo sha `0e67328e…`, anterior em `.bak_oficial_pre_REGIME_CAMADAS_2026-09-15`.*

---

*Rastreabilidade: trilha 27 gravada (`producao/27_replicacao_L05_v1.1_auditor_estrutura_2026-09-15.json`; hashes dos 3 arquivos recebidos dentro dela) · v1.1 arquivada verbatim em `_documentos_serie/L05_v1.1_recebido_2026-09-15/` · V2 em `_documentos_serie/` (ponteiro `ARQUITETURA_VIGENTE.txt`) · decisoes_B1.md rev.14 · CHANGELOG ABERTURA/RESULTADO 11 · zero caracteres de ciência alterados; simulação 100% em cópia.*
