# AO AUDITOR-MESTRE — RESPOSTA À RE-AUDITORIA DE 2026-09-13 (B1 V5, ferramentas e lacunas)
**Data:** 2026-09-13 · **Origem:** linha de produção da série mecanística (B1–B16)
**Objeto:** sua análise *FERRAMENTAS E LACUNAS* (F-01…F-10, condições C1–C6, novo portão P-8
`validar_coerencia_camadas.py`, reparo `reparo_coerencia_2026-09-13.py`, lacunas arquiteturais
L-01…L-16) + manifestos pós-reparo (2)/(3) + `PROPOSTA_AT_OSIMO_2019.json`.

Prezado Auditor-Mestre,

A regra da casa permanece a que o senhor mesmo nos impôs: **nenhum achado aceito por declaração —
nem o seu, nem o nosso**. Tudo foi replicado empiricamente contra os nossos arquivos antes de
qualquer ação; E-utilities ao vivo para os factos bibliográficos; números sempre computados de
arquivo. A sua frase-síntese desta rodada — *«os portões foram construídos para provar que as
referências existem e que os identificadores casam; nenhum deles foi construído para provar que a
afirmação escrita corresponde ao que a referência diz»* — passa a constar no cabeçalho honesto do
nosso portão P-5 (ver §4). Concordamos com o diagnóstico e com a ordem da Parte IV. Relato item a
item, com os números dos dois lados onde divergiram.

---

## A. Replicação das F-01…F-10 (todas confirmadas)

| Achado | Seu número | Nossa réplica | Posição |
|---|---|---|---|
| F-01 regex de citação cobre quase nada | 20/280 (~7%) | 22/280 (~8%) | **Confirmada** (classe real; a diferença 20×22 vem do conjunto exato de padrões testados — mérito intacto). O `CITACAO_RE` do P-8 cobre 270/280 (**96,4%**) |
| F-02 ramo `[REF_BLOCO_XX: …]` morto; listras não auditadas | 86 linhas-lote | 0 âncoras `[REF_BLOCO…]`; 102 linhas-lote | **Confirmada** (contagem de linha-lote difere por critério de contagem de tabela/índice — 86×102; o ramo é morto nos dois casos) |
| F-04 ledger ancorado em linha-lote e citacao_literal-TOKEN | 236/236 · 221/236 | 236/236 · 221/236 · 0 âncora com "(Autor, ANO)" | **Confirmada exata** |
| F-08 docstring do gate promete o que não faz (linhas 17–18) | — | verbatim confirmado | **Confirmada; corrigida hoje na casa** (§4.2) |
| F-09 checklist com `/home/user/...` hardcoded (linhas 43–44) | — | verbatim confirmado | **Confirmada; corrigida hoje na casa** (§4.1) |
| AUD-056/057 manifesto dessincronizado (corte 09-03×09-04; related 12×15; domains 3×4; sha ausente; placeholders {EC},{MA},{P},{T}) | — | todos os 5 itens reais | **Confirmado; resolvido pelo seu R-07/R-01** — nosso manifesto agora registra `sha256_canonica_vigente` |
| F-03/F-05/F-06/F-07/F-10 | — | replicados sem divergência | Confirmados |

**Variações transparentes (a esclarecer bilateralmente, sem impacto de mérito):**
P-8 ante-reparo: **nosso 22 ERRO / 60 AVISO** × seu 24/60 (varância de 2 ERRO; hipótese: o run dele
incidiu sobre estado intermediário entre trilhas; pedimos o log exato para reconciliar).

## B. Condições C1–C6

- **C1/AUD-049 (propagação) — CONFISSÃO DA CASA.** Confirmamos nos nossos arquivos, antes do reparo:
  ficha `REF_COMAI_2022` com achado "…bipolar/**TDM**" contradizendo a prosa R2; `VINC_B1_0219` g3_notas
  "**Meta tri-compartimental**"; `VINC_B1_0247` "**questão aberta do PET**"; ledger Enache
  "tri-compartimental"=True e Wijesinghe "questao aberta"=True. **As correções R2/R11 da nossa V5 não
  propagaram a ficha/g3/ledger — falha nossa, não sua.** Reparada pelo seu script (R-01 4 campos ·
  R-02 12/16 · R-05 34 · R-06 5 · R-07 0), trilha 15, backups ×6 registrados. Fica a lição de processo:
  toda correção de prosa passa a exigir checklist de propagação às 4 camadas (prosa→vínculo→ficha→ledger).
- **C2 (V-02, âncoras em frase nominal):** seus 12/16 reparados + nossa trilha 16 (VINC_B1_0005 com
  fatia literal multi-sentença, prova `nt(fatia)==nt(armazenada)`; VINC_B1_0175 Steiner re-ancorada da
  linha-lote §11 à frase nominal única L572). **Restam 4: VINC_B1_0261 (Han), 0262 (Huang), 0265
  (Li_2025b), 0266 (Mehta_2020b)** — cada um com 2–3 frases candidatas; a recusa automática está
  correta e os 4 seguem para a **fila humana de especialista** junto com os 58 demais da P-6.
- **C3/AUD-051 Osimo 2019 — DEFERIDO ao próximo [AT]**, com a ficha pronta
  (`B01.../producao/insumos/reauditoria_2026-09-13/PROPOSTA_AT_OSIMO_2019.json`) e as suas 6 ações
  obrigatórias adotadas como checklist do [AT]: G1 eutils (PMID 31258105), G2, G3 com abstract colado,
  vínculo na frase corrigida, referência cruzada a B1.SM02.007 (R7-b) e reavaliação de VINC_B1_0172.
  **Registramos com força a sua observação crítica:** o "27% / OR 1,46" do §11.1 era definido por PCR>3
  e a V5 (R7) removeu o corte — o número ficou relativo a limiar indefinido; a correção de prosa
  proposta (restaurar o vínculo número↔limiar **sem fixar corte**) é a linha que seguiremos.
- **C4/AUD-052 BLOCO_11.4** (declaração de não-validação/circularidade do Critério C): **autor
  científico** — fora da delegação que temos.
- **C5/C6:** reparados pelo seu R-05/R-06 (34 tipográficas + 5 ajustes) — verificados em dry-run com
  números exatos antes da execução.

## C. Execução do seu reparo — com 2 desvios registrados da casa

1. **`nota()` — patch da casa.** Seu script convertia `nota_reparo` existente para **lista**; mantivemos
   o formato **string com separador " || "** (padrão de toda a série; semântica idêntica). Desvio
   comentado no cabeçalho do nosso `reparo_coerencia_2026-09-13.py`.
2. **Ordem de leitura do patch:** execução em uma única passada sobre cópia de trabalho, com os 6
   backups `.bak_pre_reparo_20260913` antes de qualquer escrita.
**Resultado: manifesto final IDÊNTICO ao seu `_manifesto_biblioteca (2).json`** (0 campos divergentes,
comparação computada) e P-8 pós **6 ERRO / 24 AVISO** = seu número. Após as trilhas 16/17 abaixo:
**4 ERRO / 24 AVISO**.

## D. Trilha 17 — AUD-038/V-05 causa-raiz (Hafizi), completa e propagada

`REF_HAFIZI_2005 → REF_HAFIZI_2007`. eutils 2026-09-13: publicação **2007**, PMID 17639827, sem
abstract; o "2005" veio do NOME NLM do periódico (*British journal of hospital medicine (London,
England : 2005)*). O rename completo exigiu mais que os 3 artefatos: **25 âncoras do ledger citam a
mesma listra-índice** e 1 token permanecia no APÊNDICE da canônica. Fechamento: ficha (id + campo-
lista aninhada `ids_referencia_interna[0]` — achada no assert final, 1º passe só tocava strings de
topo; registrado na trilha), vínculo VINC_B1_0047, ledger (id + citacao_literal-TOKEN + 25 âncoras
propagadas), canônica (1 token do índice; **0 linhas de prosa**; sha `3c6dda4d…` → `5051080b…`),
manifesto com sha vigente registrado. Assert final: **nenhum campo vivo usa o id antigo** (notas
históricas datadas preservam-no, como manda a regra).
**Demonstração involuntária e valiosa:** o rename mostrou o acoplamento frágil F-04/L-03 — 1 token
editado propagou a 25 âncoras de listra. É a evidência concreta a favor da sua migração de âncoras.

## E. Varredura da família-Hafizi nas 16 bibliotecas (2.689 fichas) — e o que achamos

Script read-only (`_documentos_serie/scripts_serie/varredura_familia_hafizi.py`) + relatório
(`VARREDURA_FAMILIA_HAFIZI_B1_B16_2026-09-13.md`). Resultado:

- **1 caso nominal, RESOLVIDO hoje: B13 `REF_SAITO_1999 → REF_SAITO_2010`** — o ano 1999 vinha do nome
  NLM (*Rev. bras. psiquiatr. (Sao Paulo, Brazil : 1999)*); eutils: pubdate **2010 May**, PMID 20512266.
  Rito idêntico ao da trilha 17 (backups ×5, 2+43+43+1 substituições, notas datadas, trilha própria na
  B13); B13 re-validada: gate APROVADO, framework 0 ERRO, censo série 32/32 BLOQ 0.
- **3 divergências epub×print (não são a doença Hafizi — ambos os anos são reais):** B09
  `REF_GEBARA_2020` (epub 2020-12-08 × print 2021), B09 `REF_SCAINI_2021` (epub 2021-10-14 × print
  2022), B14 `REF_SCHWEIZERSHUBERT_2021` (epub 2021-01-18 × volume 2020). **Não renomeamos:** tocar
  prosa citacional de 3 bibliotecas exige uma convenção da série. Fica a dívida nomeada
  **D-SERIE-CONVENCAO-ANO-ID** com a nossa recomendação: **adotar pubdate-ano NLM** (coerente com
  `revista_ano` e com a citação padrão PubMed) e replicar este mesmo rito. Decisão do autor científico.
- Falso-divergente da nossa própria varredura, confessado: B05 `REF_DU_2023` (parser v1 não conhecia o
  formato "MedComm (2020) 2023"; eutils confirma 2023 — ID correto). Parser rev.2 já cobre os 3
  formatos conviventes da série; sobraram só **3 fichas (B06) sem ano detectável** (trabalho nomeado).

## F. Achados nossos nos seus scripts (com respeito, para a sua errata)

1. **`validar_coerencia_camadas.py` — V-14 prometida na docstring, sem implementação.** Pedimos:
   implementar ou retirar da docstring (é o mesmo pecado da F-08 que o senhor nos cobrou — e
   reconhecemos que applies a nós também).
2. **`reparo_coerencia_2026-09-13.py` — ramo morto em R-05** (`bruto, cur = "", 0; for ch in nfc(texto): … break`):
   a âncora multi-sentença nunca é reparada por esse ramo; benigno porque VINC_B1_0005 ficou coberto
   pela nossa trilha 16. Sugerimos remover ou completar.
3. **Robustez série:** o validador assume `corte_literatura` como objeto; no schema mais antigo (B13 é
   exemplo) é string — crash `AttributeError`. **Patch defensivo da casa** datado no script (tolerar os
   dois formatos). Sem alteração de semântica: B1 permanece 4 ERRO / 24 AVISO após o patch.
4. **F-08/F-09 — os arquivos corrigidos não vieram anexados** (apenas descritos no relatório).
   Aplicamos na casa o **equivalente descrito**, com backups `.bak_F08_2026-09-13` e
   `.bak_F09_2026-09-13`: (i) `checklist_entrega.py` resolve `SCRIPTS`/`FW` relativos ao próprio
   `__file__`; (ii) `gate_script.py` com docstring reescrita honesta (o que faz de fato, item a item) +
   seção **"COBERTURA QUE ESTE PORTÃO NÃO TEM"** apontando para o P-8 como camada obrigatória seguinte.
   Pedimos a conferência bilateral das duas implementações.

## G. Descoberta arquitetural do dia: P-8 fora da B1

Primeira execução do seu portão em outra biblioteca: **B13 = 167 ERRO V-02** (âncoras em linha-lote;
perfil idêntico ao da B1 antes do ciclo R1–R13) + 1 ERRO V-09 + aviso V-13 (manifestos fora da B1 não
registram sha da canônica vigente — hoje as trilhas datadas cobrem isso). **Conclusão prática:** o P-8
generaliza e confirma, à escala da série, a sua etapa 5 — as demais 15 bibliotecas precisarão do mesmo
ciclo de reancoragem à frase nominal. Este achado entra no nosso roteiro como trabalho nomeado, na
ordem da sua Parte IV.

## H. L-01…L-16 — posição da casa

Concordamos com as 16 lacunas e com a ordem executiva da Parte IV (etapa 0 → 8). Registros específicos:

- **L-05 (contrato do Motor Clínico) com L-06 (precedência) aceitos como o maior risco do projeto** —
  etapa 1 imediata após fechar C3/C4 (etapa 0).
- **L-14 (`achado_verbatim_fonte`)**: aceito como o reparo de maior retorno; entra no schema do próximo
  [AT] (com o Osimo 2019 como piloto — o campo já consta da ficha proposta), com `populacao_agrupada`
  (L-12) no mesmo pacote.
- **L-04 (ontologia de 146 IDs)**: etapa 2, mínima-viável primeiro, versionada em `antigos/historico/`.
- **L-01/02/03 (NT schema, JSON modular, esquema de âncora)**: etapa 3; para L-03 a nossa trilha 17
  fornece o argumento empírico (§D).
- **L-09/L-10 (testes-armadilha AUD-026/027/032) + L-11 (CI)**: aceitos; a armadilha "Hafizi 2005" vira
  o 4º canário da suíte, junto com "Saito 1999".
- **L-15 (IDs opacos)**: adotado como regra de CRIAÇÃO futura (nenhum ID novo com dado mutável);
  **não faremos migração retroativa em massa** — renames pontuais seguem o rito da trilha 17.
- **L-16 (decisões arquiteturais como dado)** e **L-13 (orçamento de revisão humana ~10 mil vínculos)**:
  aceitos; o orçamento humano passa a constar do STATUS semanal da casa. Fila humana atual da B1: **4
  re-ancoras V-02 + 58 vínculos P-6 + 2 claims orfãos (R4)**.
- **Critério de replicação (seu marco de decisão)**: adotado verbatim — só replicamos o modelo para as
  demais quando **100% das frases do relatório clínico sintético forem rastreáveis a frase canônica
  com P-5, P-8 e portão de saída verdes**.

## I. Estado final medido (2026-09-13, todos os números computados de arquivo)

- **B1:** gate APROVADO · checklist 41/41 · framework 0 ERRO · **P-8 4 ERRO / 24 AVISO** (V-02 =
  0261/0262/0265/0266 → fila humana; V-01 0; V-05 0; V-13 OK sha 5051080b) · censo série **32/32 BLOQ 0**.
- **Dívidas:** D-B1-ANCORA-DERIVA **encerrada** (34 suas + VINC_B1_0005 nossa = 35/35) · D-B1-R8-CLAIM
  16→**residual 4** · nova **D-SERIE-CONVENCAO-ANO-ID (3)** · mantidas: D-B1-R3-V2CLAIM (30),
  D-B1-R3-G3NOTA (4), D-B1-R4-2CLAIMS (2), D-B1-R13-LOG (1).
- **Anexos desta carta:** trilhas `producao/15_reparo_coerencia_…`, `16_reparos_finos_…`,
  `17_rename_hafizi_2005_2007_…`; `B13.../producao/01_rename_saito_1999_2010_…`;
  `_documentos_serie/VARREDURA_FAMILIA_HAFIZI_B1_B16_2026-09-13.md` (+ script);
  `decisoes_B1.md` rev.4 (com a confissão C1) e `decisoes_B13.md` rev. 2026-09-13;
  `CHANGELOG_GERAL.md` (ABERTURA + RESULTADO desta data); `censo_pos_reauditoria_2026-09-13.txt`.

O ciclo bilateral segue aberto e contínuo. Próximos marcos pela sua Parte IV: C3 no próximo [AT]
(ficha pronta) e C4 ao autor científico; depois Contrato do Motor (L-05) + precedência (L-06).
Pedimos, para a sua próxima passada: (a) o log exato do seu P-8 ante-reparo (reconciliar 24×22);
(b) sua decisão sobre V-14 (implementar × retirar da docstring); (c) parecer sobre a convenção
pubdate-ano NLM para a D-SERIE-CONVENCAO-ANO-ID.

Com estima e método,
**a casa de produção da série mecanística**
