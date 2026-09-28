#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Correções finais pós-auditoria externa:
(1) 3 autores atribuídos sem registro correspondente -> PENDENTE_VERIF (não achar nome à força);
(2) 11 listras que não listavam o rótulo do autor citado (autor correto) -> adicionar rótulo."""
import re
P="/home/user/pipeline_auditoria_conteudo/BIBLIOTECAS/B01_Neuroinflamacao/Biblioteca_B1_NEUROINFLAMACAO_CANONICA.md"
t=open(P,encoding="utf-8").read()
log=[]

def sub(velho,novo,n=1,ok=True):
    global t
    c=t.count(velho)
    if c!=n:
        log.append(f"[!] esperado {n}, achado {c}: {velho[:70]}")
    t=t.replace(velho,novo)

# ---------- (1) autores sem registro correspondente -> PENDENTE ----------
# cGAS-STING aging review (Shen é IL-6/astrócito, errado)
sub("Vazamento de mtDNA e cGAS-STING no envelhecimento cerebral são alvo terapêutico emergente (Shen et al., 2025)[OB; revisão][EXT]",
    "Vazamento de mtDNA e cGAS-STING no envelhecimento cerebral são alvo terapêutico emergente (revisão cGAS-STING/envelhecimento — referência a verificar na Rodada 4)[OB; revisão] [PENDENTE_VERIF][EXT]")
# mitofagia-cGAS cross review (Poletti é mediadores TDM/bipolar, errado)
sub("o cruzamento mitofagia–cGAS-STING é revisado na neuroinflamação (Poletti et al., 2024)[OB] [EXTRAPOLADO: animal/célula→humano][EXT]",
    "o cruzamento mitofagia–cGAS-STING é revisado na neuroinflamação (revisão mitofagia–cGAS-STING — referência a verificar na Rodada 4)[OB] [PENDENTE_VERIF][EXT]")
# kynurenine balance hipocampo (Yehuda é Holocausto/FKBP5, errado)
sub("o balanço quinurenínico hipocampal é rompido por inflamação periférica (Yehuda et al., 2016)[ML; camundongo] [PRÉ-CLÍNICO]",
    "o balanço quinurenínico hipocampal é rompido por inflamação periférica (balanço quinurenínico hipocampal — referência a verificar na Rodada 4)[ML; camundongo] [PENDENTE_VERIF][PRÉ-CLÍNICO]")

# ---------- (2) listras: adicionar rótulo do autor já citado corretamente ----------
# (seção -> listra atual -> listra nova)
listras=[
 ("1.3","*Norden_2015[ML] | Barrientos_2015[ML] | Yang_2026_neonatal[ML] | Qiu_2026_mTBI[ML]*",
        "*Norden_2015[ML] | Barrientos_2015[ML] | Yang_2026_neonatal[ML] | Qiu_2026_mTBI[ML] | Perry_Teeling_2013[OB]*"),
 ("2.10","*KYN_gutbrain_2021[ML] | IDO1_aging_2022[ML]*",
         "*KYN_gutbrain_2021[ML] | IDO1_aging_2022[ML] | OConnor_2009[ML]*"),
 ("2.13","*Serhan_2014[ML] | PainResolv_2023[ML] | GPR37_2018[ML] | MaR2_2022[ML]*",
         "*Serhan_2014[ML] | Serhan_Levy_2018[OB] | PainResolv_2023[ML] | GPR37_2018[ML] | MaR2_2022[ML]*"),
 ("3.7","*A1block_2018[ML] | AstroSwitch_2024[ML]*",
        "*A1block_2018[ML] | AstroSwitch_2024[ML] | Antidep_microglia_2022[OB] | IFNg_PRIMING_2024[ML]*"),
 ("3.13","*IL18_2023[ML]*",
        "*IL18_2023[ML] | Quimio_meta82_2017[MA]*"),
 ("3.14","*Th17_2025[ML]*",
        "*Th17_2025[ML] | Psoriase_2025[OB]*"),
 ("4.3","*MAMs_P2X7_2024[ML]*",
        "*MAMs_P2X7_2024[ML] | PrimingPrinc_2018[OB]*"),
 ("5.2","*KYNTRP_WM_2022[EC] | Sublette_2011[EC] | BrainIDO_2017[ML]*",
        "*KYNTRP_WM_2022[EC] | Sublette_2011[EC] | BrainIDO_2017[ML] | Holocausto_2016[EC]*"),
 ("5.3","*IL6resol_2015[EC]*",
        "*IL6resol_2015[EC] | Osimo_2020[MA] | Obesidade_2025[EC]*"),
 ("5.5","*S100B_burnout_2016[EC] | S100B_dep_2019[OB]*",
        "*S100B_burnout_2016[EC] | S100B_dep_2019[OB] | HippVol_ECT_2020[EC]*"),
 ("8.1","*GR_repress_2018[ML] | IFN_HPA_2016[EC] | FKBP_inflam_2020[OB]*",
        "*GR_repress_2018[ML] | IFN_HPA_2016[EC] | FKBP_inflam_2020[OB] | RewardTrauma_2020[EC]*"),
]
for sec,velha,nova in listras:
    if velha in t:
        t=t.replace(velha,nova,1); log.append(f"[ok] listra {sec} atualizada")
    else:
        log.append(f"[!] listra {sec} não encontrada:\n     {velha[:80]}")

open(P,"w",encoding="utf-8").write(t)
print("\n".join(log))
print("\nPENDENTE_VERIF total:", t.count("[PENDENTE_VERIF]"))
