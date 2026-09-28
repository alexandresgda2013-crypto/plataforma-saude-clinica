# RELATÓRIO DE AUDITORIA — INSUMOS B5 (2026-09-08)

**Insumos:** (1) consolidação externa "B5 — GABA/Glutamato" (colada); (2) anexo `Artigos cientificos do mecanismo B5 Gaba Glutamato.md` (**190 entradas compostas por autores/ano/título/DOI**); (3) `BRIEFING_CONSOLIDADO_B5_v1.md` (rodada 0 — tabela-semente de 19 PMIDs, **todos já vigentes na B5 V1 (44 refs)**; sem novidade bibliográfica).
**Método:** extração programática → **G1 eutils** (esearch `DOI[aid]` → esummary{autor/ano/título/fonte} → efetch abstracts completos dos 190 resolvidos) → conferência decl×real (autor 1º, ano ±1, jaccard de título) → triagem de escopo por título/abstract/MeSH → decisão editorial explícita por grupo.

## 1. Contagens finais (universo auditado = 190 resolvidos + 2 não-resolvidos)
| Destino | n | Detalhe |
|---|---|---|
| **ENTRA** | **116** | grupos abaixo (§2) |
| BAIXO incremento | 53 | nicho eletrofisiológico/química-medicinal, revisões derivadas, editorial, mistos |
| EXC escopo | 14 | Alzheimer×5 (Babaei, Escamilla, Govindpani, Leitch, Sanderson-2021) · autismo×4 (Hashemi, Kolodny, Maier, Hollestein) · epilepsia×3 (Drexel, Godoy, De Luca) · apneia (Kaczmarski) · carta redundante (Babber↔Xu 2020) |
| **FP — falso positivo** | 1 | **"Prosowski 2024 — Ketamine/Esketamine TRD": DOI do anexo (10.x citado) resolve para Zhang L 2026 "γ-Butyrolactones… autoregulatory systems" (jaccard título = 0,00). Artigo pretendido NÃO existe no PubMed (`Prosowski[author]` = 0) → `[G1]`, não entra** |
| FALHAS/não-resolvidos | 2 | Imiruaye 2025 (abstract congresso Alzheimer; não indexado + fora de escopo) · Prosowski 2024 (`[G1]`, ver FP) |
| Já vigentes (V1=44 refs) | 6 | 20724638 Li_2010, 27144355 Zanos_2016, 28697889 Fee_2017, 30914923 Fogaça_2019, 37543478 Lüscher_2023, 39368965 Asim_2024 — **não duplicar** |
| **Total** | **190 (+2)** | 116+53+14+1+6 = 190 ✓ |

## 2. ENTRA por grupo de alocação (116)
| Grupo | n | Âncoras |
|---|---|---|
| KET — cetamina/esketamina (arquitetura mecanística) | 21 | Duman 2018/2019, Abdallah 2016, Le 2026 ×2, (R)-ketamine Scotton, esketamine MoA van Hoogdalem 2026, Śledzikowska 2026, Serretti 2025, Freudenberg 2025, Zanos 2018 ×2, Deyama 2020, Kang-Wires 2022, Hess 2022, Krystal 2024, arketamine Wei 2022, scopolamina Wohleb 2017, Sial 2020 (crítica), Yun 2024 |
| GABA — receptores/síntese/inibição tônica/neuroesteroides | 20 | Pehrson 2015, Fee 2021, Fogaça 2021, Ghosal 2017/2020, Lu-allopregnanolone 2023, Carver 2013, Rudy 2011, Magnin 2019, Lee-Maguire 2014, Booker ×2, Antonoudiou 2020, Bryson 2020, Riedemann 2019, Vereczki 2021 (corrigida), Du 2023, Wen 2022, Thompson 2024, Yang SS 2021 |
| NMDA | 19 | Miller 2014, Pothula 2021 (CONT), Feyissa 2009 (postmortem), Amidfar 2019, Comai 2024, DAPK1 Li 2018, Francija 2019 (B1×B5), LHb Kang 2020, Bieler 2021, Treccani 2016, Zanos 2023 (CONT), Storey 2025 (corrigida), Brigman 2010, Shipton 2014, Massey 2004, Wang-GluN2A 2024, Elhussiny 2021, Chen QY 2021, Baez 2018 |
| PLAST — elo B3 | 14 | Lin-TrkB 2021, Brown&Gould 2024, Cavalleri 2018, Aleksandrova 2021, Piva 2021, Pardossi-BDNF 2024, Kim 2023, Kavalali 2012, Guntupalli 2023 (corrigida), Diering 2018, Purkey 2020, Sanderson 2016, Lüscher-Malenka 2012, Volianskis 2015 |
| MRS — biomarcadores humanos | 14 | **Godfrey 2018 (MA; GABA↓, glutamato sem diferença global — NEG/CONT)**, **Kantrowitz 2021 (Glx↑+GABA↓ — CONT)**, **Steel 2020 e Rideaux 2021/2022 (Glx×GABA+ — controle e contradição explícita; METH/NEG)**, Hu 2023, Yoshihara 2026 (7T ACC E/I), Steinholtz 2025 (RCT iTBS), Houtepen 2017 (7T estresse), Hu L 2024, Sarawagi 2021, Mamelak 2024, Duncan 2013, Lener 2017 |
| ANX — ansiedade | 10 | Nuss 2015, Arora 2024, Salimando 2020 (BNST GluN2D), Abraham 2023, Fuchs 2017 (SST anxiolítico), Volitaki 2024 (PV vHipp), Xiao 2021 (BNST→NAc), Mitten 2024, Singh 2023 (medo transdiagnóstico), Yu 2020 (LXRβ amígdala) |
| STR — estresse | 6 | **Wu 2026 (dmPFC→LHb dual-pathway)**, Ryazantseva 2025, Tao 2024, Perlman 2021 (PV sistemática), Page 2019 (E/I estresse), Xu 2020 (ciclo glutamina — **prioridade sobre a carta**) |
| IFACE — interfaces B1/B2/B4/B5.03/B7 | 7 | Hartmann 2017 (CRH1 glutamatérgico — B2), Rezaei 2024 (LPS — B1), Zhong 2022 (inflamação neonatal — B1), Shabel 2014 (habenula co-release), Sears 2021 (transporte Glu/GABA — B5.03), Zielińska 2026 (psicobióticos — **ponte B7 como ponte, não prova**), Pham 2019 (serotonina×glutamato — B4) |

## 3. Correções de autoria do anexo (provas efetch)
1. "Matthew & Samba 2013" → **Carver CM 2013** (PMID 24071826; neuroesteroides×GABA-A).
2. "Pich & Millan 2018" → **Cavalleri L 2018** (PMID 29158584; plasticidade estrutural cetamina; consta também na B3 V2).
3. Hollestein: anexo "2021" → publicado **2023** (PMID 36681677; EXC autismo).
4. Consolidação verificada **correta**: Guntupalli=37419688 (JNeurosci 2023, substituindo preprint) · Storey=39562042 · Vereczki=33837051 · **Xu 2020=32158215 prioridade** sobre a carta Babber & Sharma 2024 (39524246, EXC) · Duman/Sanacora/Krystal Neuron 2019 = 30946828.

## 4. Regras de leitura propostas (a fixar na V2, ecoando a consolidação)
- **B5.R01** — Não existe "glutamato alto + GABA baixo" como estado universal: a própria base humana discorda (Godfrey MA × Kantrowitz); a biblioteca modela **heterogeneidade por região/tempo/contexto**.
- **B5.R02** — Níveis de evidência separados: concentração (MRS) ≠ neurotransmissão ≠ receptor ≠ circuito ≠ comportamento. **GABA/Glx por MRS ≠ E/I sináptico** (Steel × Rideaux = salvaguarda explícita).
- **B5.R03** — NMDAR ≠ mecanismo unidirecional "ruim": potenciação alostérica também é antidepressivo-símile (Pothula 2021); **antagonismo NMDA ≠ descrição suficiente da cetamina** (Zanos 2016/2023, Aleksandrova, CP-AMPAR Zaytseva, AMPA-PET Nakajima 2026).
- **B5.R04** — glutamato↑ ≠ excitotoxicidade (exige Ca²⁺/estresse oxidativo/dano — elo B6).
- **B5.R05** — fundamentos (LTP/LTD, subunidades, inibição tônica, interneurônios) entram como **SUP mecanístico `[ML]`**, não como evidência clínica de MDD/ansiedade (R04).
- **B5.R06** — negativos/contraditórios preservados (Godfrey-NEG glutamato global; Rideaux-NEG correlação; Steel-contexto; Pothula-CONT; Sial/Lu-opioide críticas).
- **B5.R07** — psicobióticos GABA (Zielińska 2026) = ponte B5↔B7, não prova de GABA cerebral.
- Arquitetura B5.01–B5.24 da consolidação adotada como **destino** (seções §x já existentes na V1 serão expandidas nos grupos §2).

## 5. Portões honestos
- G1: 190/192 resolvidos com identidade verificada (98,9%); abstracts efetch completos para 190.
- 2ª verificação cega (P-6) NÃO feita — registra-se PENDENTE (como em B1–B4).
- Nada aplicado ainda: aplicação depende da decisão do usuário.
