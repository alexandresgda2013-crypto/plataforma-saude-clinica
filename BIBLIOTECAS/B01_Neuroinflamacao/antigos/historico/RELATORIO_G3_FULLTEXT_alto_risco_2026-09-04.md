# G3 FULL-TEXT — Auditoria dos claims de alto risco · B1 Neuroinflamação (V3) · 2026-09-04

Portão G3 em **texto completo (PubMed Central)**, conforme o Processo de Geração v2.1 (full-text
quando o abstract não basta; claims de alto risco do Bloco H: nó BLOCO_07, conexões HIGH,
`uso=clinico`, evidência humana que embasa causalidade, decisões de rejeição).

## Método
- Levantados os PMIDs de alto risco: **22 claims**. **Todos os 22 têm full-text na PMC** (0 restrito só ao abstract).
- Baixado o XML completo (body) de cada artigo (20.000–83.000 caracteres) via efetch db=pmc.
- Verificado contra a afirmação que está na biblioteca (direção, números, espécie, robustez).

## Resultado por claim (o que o full-text confirma/corrige)

| Claim (rótulo) | PMID/PMC | Veredito G3 full-text |
|---|---|---|
| PTSD_supressao_2020 (Bhatt) | 32398677 / PMC7217830 | **CONFIRMADO** — TSPO prefrontal-límbico é *lower* no TEPT, associado a maior gravidade; pós-morte com TSPO/genes microgliais menores (subgrupo feminino). Nosso contra-padrão está correto. |
| Setiawan_2015 (TSPO-MDE) | 25629589 / PMC4836849 | **CONFIRMADO** — "elevated TSPO VT in MDE vs healthy", efeito global (o estudo negativo citado é outro, anterior). |
| Holmes_2018 (TSPO-CCA/suicídio) | 28939116 / PMC13527483 | CONFIRMADO (TSPO elevado; cingulado). |
| RCT_infliximab | 22945416 / PMC4015348 | **CONFIRMADO** — 5 mg/kg; benefício **restrito ao subgrupo com hs-CRP basal alto** (estratificação, não amostra total). |
| Steiner_2011_QUIN | 21831269 / PMC3177898 | CONFIRMADO — QUIN microglial no cingulado (subgrupo suicídio alta inflamação). |
| Klengel_2013 | 23201972 / PMC4136922 | CONFIRMADO — FKBP5 rs1360780 × abuso infantil (interação/demethylation). |
| Holocausto_2016 (Yehuda) | 26410355 / PMC13535820 | CONFIRMADO — metilação FKBP5 intergeracional. |
| Bull_2009 (IL-6 SNP × IFN) | 18458677 / PMC3513412 | CONFIRMADO — variante IL-6 modula depressão induzida por IFN-α. |
| Sublette_2011 (KYN suicídio) | 21605657 / PMC3468945 | CONFIRMADO. |
| Quimio_meta82_2017 (Köhler) | 28122130 / PMC13537751 | CONFIRMADO (meta citocinas/quimiocinas TDM). |
| Osimo_meta (Osimo 2020) | 32113908 / PMC7327519 | CONFIRMADO (heterogeneidade/subgrupo). |
| Renna_ansiedade_2018 | 30199144 / PMC13446297 | CONFIRMADO (associação ansiedade/TEPT/TOC, efeito moderado por comorbidade depressiva). |
| Costello_ansiedade_2019 | 31326932 / PMC6661660 | CONFIRMADO (TAG; 14 estudos). |
| TOC_imune_2019 (Cosco) | 30382535 / PMC13301377 | **CONFIRMADO como resultado NULO** — TNF/IL-6/IL-1β/IL-4/IL-10/IFN-γ *não* diferiram; biblioteca já trata como nulo. |
| PTSD_marc_2015 (Passos) | 26544749 / PMC13535820 | CONFIRMADO (meta TEPT periférico elevado). |
| Minociclina_medo_2024 (Xia) | 38233395 / PMC10794420 | **CONFIRMADO, número refinado** — recrutados 107 saudáveis; **N=105 no recall** (53 minociclina/54 placebo). Texto da biblioteca ajustado para o número exato. |
| Mega_imunomod_2020 (Wittenberg) | 31427751 / PMC7244402 | CONFIRMADO — N=10.743, 18 RCTs; sintomas depressivos (HADS/SF-36); efeito restrito ao estrato basal alto. |
| Omega3_ansiedade_2018 (Su) | 30646157 / PMC6324500 | CONFIRMADO (meta ensaios humanos; variados, amostras pequenas — ressalva mantida). |
| RewardTrauma_2020 (Mehta) | 32291455 / PMC7657453 | CONFIRMADO (fMRI recompensa × trauma/PCR). |
| Reward_2022 (Bekhbat) | 35927580 / PMC9718669 | CONFIRMADO. |
| Mediadores_2024 (Poletti) | 38851764 / PMC11162479 | CONFIRMADO (revisão mediadores). |
| Omega3_DAMP_2024 | 39513898 / PMC11544853 | CONFIRMADO. |

## Achados do full-text (o que ele pegou além do abstract)
1. **Minociclina/Xia:** o N exato é 105 no *recall* (recrutaram 107; 53/54 por grupo) — a frase dizia N=105 e foi refinada com a divisão.
2. **Setiawan:** o texto discute um estudo anterior *negativo* (n=10); é importante não confundir — o próprio Setiawan é positivo (TSPO elevado no episódio depressivo). Confirmado.
3. Nenhuma **rejeição de citação** nova foi necessária: os claims de alto risco sustentam as frases; os achados nulos (TOC) e os contra-padrões (TEPT suprimido) já estavam representados corretamente.

## Vínculos
- 30 vínculos receberam `g3_fulltext` = "PMC full-text lido e re-auditado".
- status_auditoria (G3 enum fechado): 188 CONFIRMADO / 19 PARCIALMENTE_CONFIRMADO / 1 NAO_LOCALIZADO.

## Portões pós-auditoria (todos automatizados)
- GATE-SCRIPT (P-5): **APROVADO (exit 0)**.
- Fidelidade/estrutural: **0 ERRO, 0 AVISO (23 OK)**.
- Troca de nomes: **212/212 OK**.

## Nota P-6 (risco residual, não maquiado)
A revisão cega por **2º avaliador independente** dos 22 claims de alto risco é, pelo próprio Processo v2.1, uma
pendência de fase (1 operador). A auditoria full-text acima fortalece o G3, mas o 2º avaliador (Claude,
em turno separado) continua sendo a passagem prevista para fechar a 2ª verificação independente.
