# RELATÓRIO DE AUDITORIA — INSUMO "MATRIZ CANÔNICA B2" (externo) vs. B2 V1 CANÔNICA
**Data:** 2026-09-08 · Auditoria ref a ref (regra permanente) · G1 eutils · Nada fundido sem verificação
**Arquivos:** `matriz_b2_g1.json` (35 resolvidos com metadados PubMed + flag de cobertura)

## 1. Identificadores totais do insumo
- 34 PMIDs + 1 DOI (`10.1210/endo.141.11.7767`, duplicata Müller/Ller 2000) + 21 itens apenas (Autor, Ano).
- **35/35 resolvidos no PubMed** (esummary/efetch). **Zero não localizado.**
- **ZERO FALSOS POSITIVOS:** todos os PMIDs correspondem ao paper declarado (autor+ano+tema).
  Única ressalva formal: `34566653` (meta HPA-treatments) veio sem autor — o autor real é
  **Ding Y 2021**. Não é erro de citação, é rótulo sem autor; corrigido na fusão.

## 2. Cobertura já existente na B2 V1 CANÔNICA (185 refs)
**Por PMID (7):** Stetler & Miller 2011 (21257974), Zorn 2017 (28012291), Keller 2017 (27528460),
Menke 2024 (37581323), Wang 2024 sexo (38176541), Zhang 2026 antenatal (41791598),
Thom 2026 reelin (41755883).
**Por nome/tema (referência equivalente já presente):** Klinger-König (34786441),
Ising 2008 (18179304), Khoury (36335755), Klengel/FKBP5 epigenética (23201972),
Stalder (28135674 — mas é outro paper, ver abaixo).

## 3. NOVOS verificados recomendados ENTRAR (28) — por eixo
**Metodologia de medida (maior ganho — a B2 carece de âncoras quantitativas aqui):**
- **Stalder 2016** (26563991) — guideline consensual do CAR [OB/consenso; humano].
- **Wesarg-Menzel 2024** (38308964) — meta: AUC/slope/CAR diurnos **sem** associação global
  com reatividade aguda (TSST) — a âncora da regra "diurno ≠ resposta aguda" [MA] [NEG].
- **Sugaya 2020** (32276241) — validação cabelo×30 dias: correlação moderada com cortisol
  integrado, **não** com CAR/slope [EC; validação, n=24].
**Núcleo HPA/TDM (humano):**
- **Swaab 2005** (15996533) — sistema de estresse cerebral humano [OB].
- **Von Werne Baes 2012** (28183380) — avaliação da atividade HPA, GR/MR, early-life stress [OB].
- **Ceruso 2020** (32203965) — revisão sistemática HPA em TDM + estresse precoce [OB].
- **Sahu 2022** (36458076) — revisão/meta cortisol sérico/plasmático no TDM [OB].
- **Machahary 2025** (41270487) — meta hormônios endógenos×fenótipos TDM [MA].
- **Jarcho 2013** (23410758) — ritmo diurno desregulado × resistência glicocorticoide [EC].
**B2↔B1 imunidade:**
- **Van Den Noortgate 2025** (40040865) — meta crosstalk imune-neuroendócrino [OB/revisão].
**Bloco FKBP5 (humano — a B2 tem Klengel 2013 mas carece do corpo de evidência G×E):**
- **Zobel 2010** (20047716) — variantes FKBP5 × depressão unipolar [EC].
- **Xie 2010** (20393453) — FKBP5×adversidade infantil→TEPT [EC].
- **Zimmermann 2011** (21865530) — coorte prospectiva 10 anos, n=884, FKBP5×trauma→TDM [EC].
- **Tozzi 2018** (29182159) — epigenética FKBP5 ligando risco a alterações cerebrais em TDM [EC].
- **Wang 2018** (28850857) — meta 14 estudos/15.109 participantes FKBP5×trauma→MDD/PTSD [MA].
- **Kaul 2026** (41849885) — variantes de splicing FKBP5 no córtex humano [EC; fronteira].
**CRH/PVN circuitos (novo eixo arquitetural: CRH não é só interruptor endócrino):**
- **Stanton 2023** (37078436) — neurônios PVN-CRH, contribuições sinápticas [OB].
- **Zheng 2026** (41935803) — circuitos sinápticos PVN^CRH além do HPA [OB; fronteira].
- **Sukhareva 2021** (34901719) — CRH e receptores na resposta ao estresse [OB].
**AVP/V1B:**
- **Spiga 2009** (19008333) — antagonismo V1B reduz ACTH ao estresse, não corticosterona [ML].
**Tratamento HPA (sonda/precisão, nunca recomendação):**
- **Ding 2021** (34566653) — meta eficácia HPA-targeting no TDM: efeito global pequeno [MA].
- **Lombardo 2019** (31499391) — cortisol basal × resposta a antiglicocorticoide [MA].
**Epigenética com downgrade (âncora anti-entusiasmo):**
- **Balfour 2026** (42009273) — metilação×resposta de cortisol: resultados mistos; só lactentes;
  certeza baixa [MA] [CALIBRAÇÃO].
**Zona pré-clínica estrita [ML; não promover a evidência humana]:**
- **Zhang S 2025** (40578604) — FKBP5 KO × NMDAR-LTD × resiliência [ML; camundongo].
- **Sun 2023** (36624454) — antagonista CRHR1 em modelo LPS [ML; camundongo].
- **Tatro 2009** (19545546) — FKBP51/FKBP52 e translocação nuclear do GR em neurônios [ML; célula].
- **Müller 2000** (11089561, via DOI) — CRHR1-deficiente: sistema vasopressinérgico [ML; camundongo].

## 4. NOVOS que NÃO recomendo entrar diretamente (com razão)
| Item | Razão |
|---|---|
| 21 itens só (Autor, Ano) sem identificador | `[G1: a cravar]` — não entram sem PMID/DOI. Peng 2018: próprio insumo admite referência incompleta (não atribuir por inferência). Klinger-König 2019, Ising 2008, Khoury 2019 e Klengel 2013 **já têm equivalente na B2** |
| Duplicata Müller/Ller 2000 | mesmo DOI — mantida **1 entrada** (Müller MB 2000, PMID 11089561) |
| Regras B2.R01–R20 e arquitetura de 52 submódulos | não são fontes; podem ser **adotadas como governança textual** desde que cada claim empírico fique lastreado nas refs verificadas |

## 5. Convergência arquitetural com a B2 vigente
O insumo e a nossa B2 **convergem nas regras-mãe** (dinâmica>mancha única; sexo/modificadores;
FKBP5/NR3C1×trauma; periferia≠centro; HPA↔B1 bidirecional; HPA-targeting≠recomendação).
Acréscimos reais do insumo: (i) âncoras quantitativas de medida (CAR guideline; meta nula
diurno×TSST; validação do cabelo); (ii) corpo G×E do FKBP5 com tamanhos de amostra;
(iii) eixo CRH/PVN como **circuito neural** (não só endócrino); (iv) downgrade anti-entusiasmo
da epigenética (Balfour); (v) âncora explícita do crosstalk B2↔B1 (Van Den Noortgate).

## 6. Decisão proposta
**ENTRAM (28)** após G1✓ — mini-ciclo P-7 igual ao da B1 (CANDIDATO→G1/G2/G3→nova versão V2;
V1 arquivada em historico/). Núcleo alvo: 185 → **213 refs**. NÃO ENTRAM: bloco 4.
Revalidação obrigatória: gate P-5 + framework + checklist 41/41 + P-4.
Correções de registro: `34566653` = Ding Y 2021 (rótulo do insumo sem autor — corrigido).
