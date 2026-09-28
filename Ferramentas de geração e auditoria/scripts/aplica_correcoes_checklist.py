#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica as correções apontadas pelo checklist de fidelidade B1 (rodada de correção estrutural)."""
import json, re, glob
from pathlib import Path
BASE=Path("/home/user/pipeline_auditoria_conteudo/BIBLIOTECAS/B01_Neuroinflamacao")
P=BASE/"Biblioteca_B1_NEUROINFLAMACAO_CANONICA.md"
t=P.read_text(encoding="utf-8")

def troca(velho,novo,esperado=1):
    global t
    n=t.count(velho)
    if n!=esperado:
        print(f"  [!] {esperado} esperado, {n} achado para: {velho[:60]}")
    t=t.replace(velho,novo)

# 1) paeoniflorina: Menard(2017, BHE/social) é ERRADO -> Li 2017 (Paeoniflorin_2017)
troca("(Menard et al., 2017)[ML; camundongo][EXT]",
      "(Li et al., 2017)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]")
# trans-cinamaldeído: Shen 2025 é IL-6/astrócito; trocar para pendente (sem registro dedicado)
troca("(Shen et al., 2025)[ML; camundongo].",
      "(trans-cinamaldeído/IFN-α/astrócito — referência a verificar na Rodada 4)[ML; camundongo] [PENDENTE_VERIF].")

# 2) 2.19 IL-10/galectina-3: Sacta(GR) é ERRADO -> Shirakawa 2018 (IL10_Gal3_2018)
troca("(Sacta et al., 2018)[ML; camundongo], e a entrega direcionada de IL-10 a microglia/macrófago melhora desfecho em hemorragia intracerebral (Yang et al., 2023)[ML; camundongo]",
      "(Shirakawa et al., 2018)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]; a entrega direcionada de IL-10 a microglia/macrófago melhora desfecho em hemorragia intracerebral (IL-10 direcionado a microglia/HIC — referência a verificar na Rodada 4)[ML; camundongo] [PENDENTE_VERIF]")

# 3) Referência: (Gastrodin...) e (GR-driven...) no fim (linha ~984) -> registros reais
troca("Referência: (Gastrodin TLR4/TRAF6/NF-κB — referência a verificar na Rodada 4)[ML] [PENDENTE_VERIF]; (GR-driven repression — referência a verificar na Rodada 4)[ML] [PENDENTE_VERIF]",
      "Referência: (Wang et al., 2024)[ML; camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]; (Sacta et al., 2018)[ML; célula/camundongo] [EXTRAPOLADO: animal/célula→humano][EXT]")

# 4) IL-18 "É elevada... (meta-análise quimiocinas PENDENTE)" -> Köhler 2017 (Quimio82)
troca("(meta-análise de quimiocinas/citocinas — referência a verificar na Rodada 4)[MA] [PENDENTE_VERIF]",
      "(Köhler et al., 2017)[MA; humano] [VERIFICADO]")

# 5) 5.5 S100B after ECT -> Belge 2020 (HippVol_ECT_2020) é inflamação/ECT/hipocampo; S100B-ECT específico não existe
troca("Após TCE, S100B cai (S100B after ECT — referência a verificar na Rodada 4)[EC; humano] [PENDENTE_VERIF].",
      "Após ECT, marcadores inflamatórios e de volume hipocampal mudam (Belge et al., 2020)[EC; humano] [VERIFICADO].")
# neopterina/cirurgia: sem registro no banco -> pendente honesto (mantém, mas reformula em PT)
troca("(Neopterin/IL-6 surgery — referência a verificar na Rodada 4)[EC; humano] [PENDENTE_VERIF]",
      "(neopterina/IL-6 em contexto cirúrgico — referência a verificar na Rodada 4)[EC; humano] [PENDENTE_VERIF]")

P.write_text(t,encoding="utf-8")
print("prosa corrigida. PENDENTE_VERIF agora:", t.count("[PENDENTE_VERIF]"))
