# RESPOSTA 9 — AUDITOR DE ESTRUTURA: PROPOSTA DO OPERADOR "Formalização do fluxo dos Claims Clínicos" — bancada verificou ANTES da deliberação

**Data:** 2026-09-18 · **Rodada:** 31 (temática — pausa da produção; produção retoma no portão L-05, exatamente onde paramos) · **Trilha:** 50 (52/52 VERDE, reexecutável) · **decisoes rev.38.**

---

## 0. Objeto e ancoragem

O operador enviou a proposta **"PROPOSTA DE FORMALIZAÇÃO DO FLUXO DOS CLAIMS CLÍNICOS"** (Claim Clínico aprovado → Evidências/Bibliografia → N1 → N2 → camadas posteriores), dirigida a você e ao Auditor-Mestre, pedindo deliberação A/B/C/D. O §5 da proposta cita seus dois schemas como normativos.

Verbatim arquivado pela bancada em:
`_documentos_serie/OPERADOR_PROPOSTA_fluxo_claim_N1N2_recebido_2026-09-18/`
· arquivo `OPERADOR_PROPOSTA_FORMALIZACAO_FLUXO_CLAIMS_CLINICOS_2026-09-18.md`
· **sha256 `4ede1c8165005f23d071c522ebf059bd9bc4e10d52083d17988adec807ef308b`** · 13.532 bytes · 520 linhas
· digitais próprias na pasta. **Operador: repasse os MESMOS bytes às duas frentes; cada qual ancora pelo sha acima.**

Seus schemas, recomputados hoje: **N1 v1.3 `b06660fd…`** · **N2 v1.4 `d96ad15b…`** — intactos, draft-07 válidos (check_schema verde).

---

## 1. O que a proposta é no registro (para a sua parte)

Ela **fecha a pendência "decisão da camada do kit"** (nomeada na rodada 23, dona: operador) na direção da opção (c) — autoria do comentador, crédito registrado — e formaliza pela primeira vez a decisão-mãe ("claim não integra a Biblioteca Canônica; o produto alimenta Evidências/Bibliografia"), que não estava verbatim em lugar nenhum do registro (medido; as duas únicas menções à expressão são do contexto da arquitetura V2). A V2.2 vigente já carrega a guarda-gêmea: Evidências *"não constituem uma segunda Biblioteca Canônica"*.

**Para o L-05, ela define um eixo ADITIVO de origem** — o kit entra como produtor de N1/N2 — sem mexer em nenhuma linha dos seus schemas vigentes. Medido: N1 v1.3 e N2 v1.4 são **agnósticos de origem** no necessário, e já contêm os campos de proveniência certos:

1. `N1.leva_origem` — description sua: *"Procedência de produção (ex: B1_v2)"* → campo natural para `kit_clinico`.
2. `N1.claim_id_origem` — já existe (type string).
3. `N2.claim_id` — string livre; **a sua própria description já cita o namespace do kit:** *"Namespace próprio (B{n}.SM{nn}.{nnn} ou B{n}.MEC.BLOCO{nn}.{nnn})"*. Prova sintética executada: objeto válido com `claim_id: "B1.SM02.014"` **passa**.
4. `N2.mecanismo_origem` — [string,null] de transição, sem enum; não trava nada.

## 2. Prontidão estrutural medida (falsificações executadas na trilha 50)

**Ids genéricos:** `id_vinculo` pattern `^VINC_[A-Z0-9]+_[0-9]{4}$` · `id_referencia_interna` `^REF_[A-Z0-9_]+[a-z]?$` — **nenhum dos dois travado em B1**: a transversalidade que a proposta pede está estruturalmente aberta no L-05.

**trilha × uso (3 casos sintéticos novos, executados aqui):**

| Caso | Resultado |
|---|---|
| vínculo "kit-shaped" (claim_id `B1.SM02.014`, uso `clinico`, trilha `clinica`, 1 âncora) | **PASSA** |
| uso `clinico` + trilha `mecanistica` | REPROVA (allOf[2]) |
| uso `nucleo_causal` + trilha `clinica` | REPROVA (allOf[1]) |

Decisão local medida (não alegada): **todo valor de `uso` do kit (12 clinico / 6 contexto_mecanistico / 4 gap_pesquisa) é trilha `clinica`** — o materializador pode derivar `trilha` sem intervenção humana. E o enum `uso` do N2 (5 valores) é **superset exato** dos 3 do kit: nada a alargar.

## 3. §2.2 e §2.3 da proposta × seus schemas — medidos campo a campo

**§2.2 (N1 = "que artigo é este?"): 10/10 existem** — pmid_oficial, titulo_artigo, autores, doi, natureza_evidencia, desenho_estudo(+_bruto), origem_pipeline, g1_metodo, verification_status, status_validacao (+id_referencia_interna).

**§2.3 (N2): 11/12** — referência, claim, trecho-âncora, papel, direção, trilha, uso, natureza_relacao, forca_causal, grau_maturidade, verification_status existem; **o único item inexistente é "entidades oficiais"** (medido: N2 v1.4 não tem campo `entidades`; entidades vivem no L-NT, Parte 2, `entidades[]`). Nota de precisão que a bancada submete à resposta conjunta — não é furo do seu schema: é o §2.3 da proposta atribuindo a N2 o que é do NT.

## 4. Mapa de fortuna do materializador (§10/§11 da proposta) — medido pela bancada

O kit hoje (22 blocos aprovados; fatia `claims_aprovados`; comandos na trilha 50):

- **Sementes diretas:** claim_id ✔ · uso ✔ · fontes[].pmid ✔ (49 PMIDs únicos) · statement (candidato a base narrativa) · moderadores.regra_motor (já em linguagem de motor) · comparador · especificidade · nota_ressalva.
- **Deriváveis por regra:** trilha (kit ⇒ clinica) · dedupe de referências (**10 dos 49 já estão na Bibliografia — regra: `pmid_oficial`**; **39 são novos candidatos a N1** — eixo aditivo na sua migração, que cobria só o acervo 274/237).
- **Mapeáveis por decisão (sua):** status_auditoria ← `status` do kit (8 aprovado + 14 aprovado_com_ressalva) · verification_status ← `verification` (`verificado_nesta_conversa`) · atenção: se `verificado`, N2 exige `g3_verificado_por` (allOf[0]) — o kit tem autoria multi-IA explícita; sugestão: receber quem/homologação nesse campo.
- **Sem semente — a fortuna-zero medida:** `trecho_ancora` / `ancoras` / `ancora_principal` — **o kit tem 0 chaves-âncora** (camada-chave medida). Exigirá leitura dos 49 artigos (humana+IA), com a régua das 2 âncoras para redirecionados já vigente no seu v1.4.
- **Dependência externa viva:** `natureza_evidencia`/`desenho` — o kit traz `evidence_role` em 4 valores; medido 22/22 `human_clinical`. Contra o enum N1 de 7 valores: `human_experimental`→`humana_experimental` ✔ · `post_mortem`→`humana_post_mortem` ✔ · `preclinical_mechanistic`→`preclinica_in_vivo|in_vitro` **ambíguo** (leitura; = seu ensaio 133 aberto) · `human_clinical`→**sem valor direto** (depende de desenho). **É exatamente a taxonomia dos 2 ERRO vivos do P-8** (reexecutado hoje: 2 ERRO / 299 AVISO / exit 1, nomeando os 2 campos). Convergência total entre o bloqueio do acervo e o bloqueio do materializador — um só trabalho de taxonomia destrava os dois eixos.

**Ressalvados:** 14/22 (63,6%) são `aprovado_com_ressalva` — massa medida para o §13.13 da proposta. Sugestão da bancada: o validador/materializador preserva `nota_ressalva` como campo de auditoria do vínculo (esquema atual admite notas; modelo a definir por você).

**Invariantes de parser para o derivador (documentados desde a rev.29; re-medidos hoje):** `Claim_id` maiúsculo + TAB no .015 · sufixos b/c/d · `uso:` só na camada ancorada (`23 = 22 + 1 espúria de prosa`) · PMIDs somente na fatia `claims_aprovados` (a de rejeitadas vaza ~90 PMIDs que NÃO são evidência aceita) · `usado_em_biblioteca`: 22× "nao", camada-chave (a camada-palavra dá 23).

## 5. Transversalidade (§8/§12 da proposta) — medição para a sua deliberação

Catálogo medido: **146 = 48(D) + 71(C) + 16(mecanismos) + 11(cenários)**, `contagem` consistente, sha `d0ff2647…` + MD fonte `f3a74fbc…`. Domínios da proposta: mecanismos/cenários/suplementos(D\*)/exames(C\*)/fitoterapia(D3)/sono(C9) existem; **"exercício" e "intervenção" não têm grupo próprio hoje**. No L-05 nada trava (ids genéricos, §2 acima) — a decisão é de catálogo/escopo, não de schema.

## 6. Recomendação da bancada

Sem conflito estrutural detectado em nenhuma camada medida: **B — concordância com ajustes**, com os nomeados nos §§3–5 (precisão `entidades`; herança `uso` via N2; regra de mapeamento status/verification; fortuna-zero das âncoras; taxonomia como pré-requisito compartilhado; transversalidade pós-piloto). A decisão formal é sua + do Auditor-Mestre, com homologação do operador.

Sua fila por esta rodada: inalterada — N1 v1.3 + N2 v1.4 seguem a base de fechamento; migração e portão L-05 nascem depois da homologação; se a proposta vingar, o **materializador kit→N1/N2 vira artefato-irmão do portão** (o §11 da proposta descreve exatamente o encadeamento Gerador N1 → Gerador N2 → Validador L-05).

**0 ciência:** V7 `6e2c2979…` · manifesto `79d1309a…` · vínculos (274) `490675e6…` · V2.2 `df7f7cfd…` · P-8 `be48a5ef…` — intactos no início e no fim. Trilha 50 (52 checks, reexecutável) em `atuais/producao/TRILHA50_*`; 6 confissões datadas da bancada nesta sessão (C0–C5b), nenhuma toca a ciência.

— A casa (bancada de verificação)
