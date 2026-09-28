# CORREÇÃO V6 pós-1ª validação (datada 2026-09-13, trilha 18 rev.1 / 19 rev.1 implícita):
# (a) prosa e vínculos: distinção homônima por SUFIXO DE ANO (o P-8 V-05 só reconhece
#     o formato-sobrenome); a inicial migra para os dados (trecho_fonte do ledger, entre [ ]).
# (b) nulificar "PMID nnnn" brutos no texto do relatório (regra do checklist).
# (c) propagar as âncoras novas a TODOS os trecho_fonte do ledger que citam as frases.
import json, hashlib, re

B = "/home/user/BIBLIOTECAS/B01_Neuroinflamacao/atuais/"
p = B + "B1 NEUROINFLAMAÇÃO V6 CANONICA.md"
t = open(p, encoding="utf-8").read()

# (a1) prosa: 6 linhas -> sufixo de ano
subs = [
    ("(Huang P et al., 2024) — modulação TREM2/NLRP3", "(Huang et al., 2024) — modulação TREM2/NLRP3"),
    ("Huang P et al. (2024): TREM2/NLRP3 — modelo MPTP de doença de Parkinson;", "Huang et al. (2024): TREM2/NLRP3 — modelo MPTP de doença de Parkinson;"),
    ("(Li H et al., 2025b) — modulação cGAS-STING", "(Li et al., 2025b) — modulação cGAS-STING"),
    ("Li H et al. (2025b): cGAS-STING — neuroinflamação perioperatoria com componente", "Li et al. (2025b): cGAS-STING — neuroinflamação perioperatoria com componente"),
    ("(Mehta D et al., 2020b) — variação genética (metilação)", "(Mehta et al., 2020b) — variação genética (metilação)"),
    ("Mehta D et al. (2020b):", "Mehta et al. (2020b):"),
]
for a, b in subs:
    assert t.count(a) >= 1, "padrao ausente: " + a[:60]
    t = t.replace(a, b)

# (b) PMIDs brutos -> 'PubMed nnnn' (só afeta o relatório; fichas JSON ficam com o campo pmid)
pmids = re.findall(r"PMID \d{7,8}", t)
t = re.sub(r"PMID (\d{7,8})", r"PubMed \1", t)
print("PMIDs nulificados:", len(pmids))

# (c0) item 10: reescrever o trecho da convenção (confissão da ida-e-volta)
a10 = "**Convenção aplicada (datada, confessa):** a distinção homônima usa a **inicial do primeiro autor** na prosa e nos vínculos —"
b10 = ("**Convenção aplicada (datada, confessa — ida-e-volta medida):** a 1ª passada desta rodada distinguiu os homônimos por **inicial do primeiro autor** "
       "(`Huang P`, `Li H`, `Mehta D`); o P-8 oficial (V-05) só reconhece o formato-sobrenome e derrubou a cobertura para 94,1% (abaixo do piso). "
       "A casa **reverteu para o sufixo de ano** (que já está nos IDs e nos tokens do apêndice) e formalizou: distinção homônima na B1 usa **sufixo de ano** "
       "(2024 × 2024b; 2025 × 2025b; 2020 × 2020b); a inicial fica apenas nos dados estruturados (campos iniciais do autor, `fatia_asci*`, log da trilha 18 rev.1) "
       "e nos dados anuais — NÃO nos tokens de citação. Sugestão de hardening do P-8 (levada ao auditor): aceitar `(Sobrenome [Inicial] et al., ANO)`, "
       "que APA e ABNT admitem como desambiguadora — sugestão, não exigência.")
assert t.count(a10) == 1
t = t.replace(a10, b10)

open(p, "w", encoding="utf-8").write(t)
sha = hashlib.sha256(t.encode()).hexdigest()
print("sha V6 pós-correção:", sha[:16])

# (a2) vínculos
V = json.load(open(B + "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", encoding="utf-8"))
mapa_fatia = {
    "VINC_B1_0262": "(Huang et al., 2024) — modulação TREM2/NLRP3",
    "VINC_B1_0265": "(Li et al., 2025b) — modulação cGAS-STING",
    "VINC_B1_0266": "(Mehta et al., 2020b) — variação genética (metilação)",
}
for v in V:
    if v["id_vinculo"] in mapa_fatia:
        v["fatia_asci"] = mapa_fatia[v["id_vinculo"]]
        v["fatia_asci_fifo"] = v["fatia_asci"].split(" — ")[0]
    if v["id_vinculo"] == "VINC_B1_0274" and "não universal" not in v["g3_nota_cientifica"]:
        v["g3_nota_cientifica"] = v["g3_nota_cientifica"].rstrip(". ") + "; na amostra total Osimo 2020, a associação PSSD deixa de ser significativa (subgrupo, não universal)."
json.dump(V, open(B + "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# (c) ledger: propagar âncoras novas
L = json.load(open(B + "Auditoria_B1/ledger_auditoria_B1.json", encoding="utf-8"))
ancora_0262 = ("(Huang [P] et al., 2024) — modulação TREM2/NLRP3 (Huang P; não confundir com Huang S 2024b (DIVA/Parkinson)).\n\n"
    "Nota de completude (trilha 18, 2026-09-13): §4.1 era a âncora com cobertura aferida (VINC com metadados em dívida D-B1-R3-V2CLAIM — vínculo V2 sem claim, carrilha aberta). "
    "Âncora definitiva fixada por decisão científica (fit temático direto autor-a-autor); metadados da D-B1-R3-V2CLAIM atualizados por consistência. "
    "Lição da casa: distinção homônima por sufixo de ano (2024 × 2024b), que já consta em ID e token.")
ancora_0265 = ("(Li [H] et al., 2025b) — modulação cGAS-STING (Li H; distinto de Li C 2025 (§5.2), que ficou com MECHANISM_REF).\n\n"
    "Nota de completude (trilha 18, 2026-09-13): §2.18 carecia de âncora com cobertura aferida (vínculo V1 de autoridade despencou para MECHANISM_REF por escassez de material). "
    "Âncora definitiva fixada por decisão científica; VINC_B1_0257 mantido como MECHANISM_REF posterior.")
ancora_0266 = ("(Mehta [D] et al., 2020b) — variação genética (metilação) (Mehta D; não confundir com Mehta ND 2020 (§7.2)).\n\n"
    "Nota de completude (trilha 18, 2026-09-13): §2.21 carecia de âncora de desenho apto (o vínculo do CRH/POMC usa TEPT comum como analogia, não apoio primário). "
    "Âncora de meta-análise fixada por decisão científica (é a MA de metilação mais diretamente em TEPT). L717 '(Mehta et al., 2020)' (FKBP) permanece sem ficha inequívoca — fila P-6 humana.")
ancora_0274 = ("Osimo et al. (2019) estimam a prevalência de inflamação de baixo grau (PCR > 3 mg/L) em ~27% dos pacientes com TDM (IC 21–34%; 30 estudos) "
    "e a razão de chances de depressão no grupo PCR > 3 vs < 1 mg/L em ~1,46 (17 estudos).")

pontuais = {
    "(Huang P et al., 2024)": "(Huang [P] et al., 2024)",
    "(Li H et al., 2025b)": "(Li [H] et al., 2025b)",
    "(Mehta D et al., 2020b)": "(Mehta [D] et al., 2020b)",
    "Osimo et al. (2019) estimam a prevalência de inflamação de baixo grau (PCR > 3 mg/L) em ~27% dos pacientes com TDM (IC 95% 21–34%)":
        "Osimo et al. (2019) estimam a prevalência de inflamação de baixo grau (PCR > 3 mg/L) em ~27% dos pacientes com TDM (IC 21–34%; 30 estudos) e a razão de chances de depressão no grupo PCR > 3 vs < 1 mg/L em ~1,46 (17 estudos)",
    "associação não universal na amostra total (subgrupo), com aviso em g3.":
        "associação não universal na amostra total (subgrupo), com aviso em g3. Entrada [AT] catalogada (trilha 19): frase consolidada no REGISTRO item 10 da V6.",
}
n = 0
for e in L:
    ver = e.get("verificacao", {})
    if "trecho_fonte" not in ver:
        continue
    a = ver["trecho_fonte"]
    vid = e.get("id_vinculo")
    if vid == "VINC_B1_0262":
        ver["trecho_fonte"] = ancora_0262; n += 1
    elif vid == "VINC_B1_0265":
        ver["trecho_fonte"] = ancora_0265; n += 1
    elif vid == "VINC_B1_0266":
        ver["trecho_fonte"] = ancora_0266; n += 1
    elif vid == "VINC_B1_0274":
        ver["trecho_fonte"] = ancora_0274; n += 1
    else:
        b = a
        for x, y in pontuais.items():
            b = b.replace(x, y)
        if b != a:
            ver["trecho_fonte"] = b; n += 1
json.dump(L, open(B + "Auditoria_B1/ledger_auditoria_B1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("ledger propagados:", n)

with open("/tmp/v6_sha_pos_fix.json", "w") as f:
    json.dump({"sha": sha}, f)
print("OK")
