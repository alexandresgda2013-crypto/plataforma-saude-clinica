#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 36 — Verificação da revisão do Auditor-Mestre (P-8, 3 pontos da carta 11)
================================================================================
Data: 2026-09-16 · Rodada 20 · Ciência tocada: 0 (canônica e manifesto verificados
por sha antes e depois; manifesto adulterado SOMENTE em memória de teste e sempre
restaurado de backup byte a byte, com sha conferido após cada passo).

O que este script faz, na ordem (todos os comandos ficam gravados na trilha):
  1. Digitais iniciais: script oficial, canônica V7, manifesto.
  2. BASELINE: roda o P-8 oficial (76e526cf…) na pasta atuais → totais.
  3. F-C2 NO OFICIAL ANTIGO: adultera 1 ID de related_entities no manifesto
     (mecanismo_B16_neurogenese → mecanismo_B99_inexistente, 15 itens preservados),
     roda → expectativa: 2 ERRO / 299 AVISO / exit 1 com V-07 related_entities MUDA
     (réplica independente do contraexemplo que o mestre diz ter executado).
     Restaura o manifesto e confere o sha.
  4. CANDIDATO: aplica ao script EXATAMENTE a redação da carta 11 (3 pontos):
       L20 docstring (título V-06) · L22 docstring (título V-08)
       L445 comentário interno V-06 · bloco V-07 related_entities (conjuntos).
     Mede o diff (linhas +/-, hunks).
  5. Roda o candidato na V7 → expectativa: totais IDÊNTICOS (2/299/exit 1),
     V-07 muda (agora por identidade), V-14 verde com 16 regras.
  6. F-C2 NO CANDIDATO: mesma adulteração → expectativa: V-07 DISPARA ERRO
     nomeando os dois lados; placar 3 ERRO / 299 AVISO / exit 1. Restaura e confere.
  7. INSTALAÇÃO: backup .bak_oficial_pre_3pontos_R16_2026-09-16, candidato vira o
     oficial, roda a invocação oficial comum, grava B/A (diff + sha antes/depois).
  8. Digitais finais + vereditos. Saída: TRILHA36 JSON.
"""
import difflib
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

ATUAIS = Path("/home/user/BIBLIOTECAS/B01_Neuroinflamacao/atuais")
PROD = ATUAIS / "producao"
SCRIPTS = Path("/home/user/Ferramentas de geração e auditoria/06_portao_P8_coerencia/scripts")
OFICIAL = SCRIPTS / "validar_coerencia_camadas.py"
CANDIDATO = PROD / "validar_coerencia_camadas_R16_candidato_2026-09-16.py"
BACKUP = SCRIPTS / "validar_coerencia_camadas.py.bak_oficial_pre_3pontos_R16_2026-09-16"
CANONICA = ATUAIS / "B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
MANIFESTO = ATUAIS / "Evidencias/Bibliografia/_manifesto_biblioteca.json"
TRILHA = PROD / "TRILHA36_verificacao_instalacao_P8_3pontos_2026-09-16.json"

SHA_OFICIAL_ESPERADO = "76e526cf2cb5ba13ce67e9bf4f095af396d8978485ca480c1e381c13f979d0ac"
SHA_CANONICA_ESPERADO = "6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238"
SHA_MANIFESTO_ESPERADO = "79d1309a168922d0e8bf43736cd5b21c8b361bdf64e3b200eeeafd43806f3a9c"

R = {"trilha": 36, "data": "2026-09-16", "rodada": 20,
     "objeto": "verificação da revisão do mestre (P-8 3 pontos) + instalação do oficial rev.R16",
     "passos": [], "vereditos": {}, "ciencia_tocada": 0}

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def passo(nome, **kw):
    R["passos"].append({"passo": nome, "ts": time.strftime("%Y-%m-%d %H:%M:%S"), **kw})

def rodar_p8(script: Path, tag: str):
    saida_json = PROD / f"p8_trilha36_{tag}_2026-09-16.json"
    cmd = [sys.executable, str(script), ".", "--json", str(saida_json)]
    cp = subprocess.run(cmd, cwd=ATUAIS, capture_output=True, text=True)
    itens = json.loads(saida_json.read_text(encoding="utf-8"))["itens"]
    erros = [i for i in itens if i["nivel"] == "ERRO"]
    avisos = [i for i in itens if i["nivel"] == "AVISO"]
    v14 = [i for i in itens if i["regra"] == "V-14"]
    v07rel = [i for i in itens if i["regra"] == "V-07" and i["objeto"] == "related_entities"]
    return {"comando": cmd, "cwd": str(ATUAIS), "exit": cp.returncode,
            "json": saida_json.name,
            "totais": {"ERRO": len(erros), "AVISO": len(avisos)},
            "V14": v14, "V07_related_entities": v07rel}

def adulterar_manifesto():
    original = MANIFESTO.read_bytes()
    txt = original.decode("utf-8")
    assert txt.count("mecanismo_B16_neurogenese") == 1, "contraexemplo assume 1 ocorrência"
    MANIFESTO.write_text(txt.replace("mecanismo_B16_neurogenese",
                                     "mecanismo_B99_inexistente"), encoding="utf-8")
    return original

def restaurar_manifesto(original: bytes):
    MANIFESTO.write_bytes(original)
    assert sha(MANIFESTO) == SHA_MANIFESTO_ESPERADO, "MANIFESTO NÃO RESTAURADO"

# ---------------------------------------------------------------- 1. digitais iniciais
d0 = {"script_oficial": sha(OFICIAL), "canonica_V7": sha(CANONICA), "manifesto": sha(MANIFESTO)}
passo("1_digitais_iniciais", **d0, confere={
    "script==76e526cf…": d0["script_oficial"] == SHA_OFICIAL_ESPERADO,
    "canonica==6e2c2979…": d0["canonica_V7"] == SHA_CANONICA_ESPERADO,
    "manifesto==79d1309a…": d0["manifesto"] == SHA_MANIFESTO_ESPERADO})

# ---------------------------------------------------------------- 2. baseline oficial
base = rodar_p8(OFICIAL, "baseline_oficial_76e526cf")
passo("2_baseline_oficial", **base)
R["vereditos"]["baseline_2E_299A_exit1"] = (
    base["totais"] == {"ERRO": 2, "AVISO": 299} and base["exit"] == 1)

# ---------------------------------------------------------------- 3. F-C2 no oficial antigo
orig = adulterar_manifesto()
try:
    fc2_antigo = rodar_p8(OFICIAL, "fc2_oficial_antigo")
finally:
    restaurar_manifesto(orig)
passo("3_FC2_no_oficial_antigo", **fc2_antigo,
      manifesto_sha_apos_restaurar=sha(MANIFESTO))
R["vereditos"]["FC2_oficial_antigo_mudo_2E_299A_exit1"] = (
    fc2_antigo["totais"] == {"ERRO": 2, "AVISO": 299}
    and fc2_antigo["exit"] == 1 and fc2_antigo["V07_related_entities"] == [])

# ---------------------------------------------------------------- 4. candidato (redação carta 11)
src = OFICIAL.read_text(encoding="utf-8")
alvos = [
    ("L20 docstring título V-06",
     "  V-06  COERÊNCIA SEMÂNTICA ficha/vínculo × prosa ancorada (detector de deriva)\n",
     "  V-06  DERIVA ficha/vínculo × prosa ancorada (detector heurístico — só AVISO;\n"
     "        nunca prova de coerência semântica; semântica = G3/humano)\n"),
    ("L22 docstring título V-08",
     "  V-08  claim quantitativo sem referência ancorada\n",
     "  V-08  claim quantitativo sem âncora na MESMA LINHA (alerta de triagem; lastro = V-01/V-04/V-05)\n"),
    ("L445 comentário interno V-06",
     "    # ---------------- V-06 coerência semântica ficha/vínculo × prosa ancorada\n",
     "    # ---------------- V-06 detecção heurística de possível deriva (ficha/vínculo × prosa ancorada)\n"),
    ("bloco V-07 related_entities (cardinalidade → conjuntos)",
     '        rel_txt = do_texto(r"\\*\\*Mecanismos relacionados \\(IDs oficiais\\):\\*\\*\\s*(.+)")\n'
     "        if rel_txt:\n"
     '            n_txt = len([x for x in rel_txt.split(",") if x.strip()])\n'
     '            n_man = len((man.get("semantic_layer") or {}).get("related_entities") or [])\n'
     "            if n_txt != n_man:\n"
     '                rel.erro("V-07", "related_entities",\n'
     '                         f"manifesto tem {n_man} mecanismos relacionados × canônica tem {n_txt}")\n',
     '        rel_txt = do_texto(r"\\*\\*Mecanismos relacionados \\(IDs oficiais\\):\\*\\*\\s*(.+)")\n'
     "        if rel_txt:\n"
     '            s_txt = {x.strip() for x in rel_txt.split(",") if x.strip()}\n'
     '            s_man = {str(x).strip() for x in (man.get("semantic_layer") or {}).get("related_entities") or []}\n'
     "            if s_txt != s_man:\n"
     '                rel.erro("V-07", "related_entities",\n'
     '                         f"identidade divergente (fonte única violada) — "\n'
     '                         f"só na canônica: {sorted(s_txt - s_man)} · "\n'
     '                         f"só no manifesto: {sorted(s_man - s_txt)}")\n'),
]
aplicadas = []
for nome, velho, novo in alvos:
    n = src.count(velho)
    assert n == 1, f"alvo '{nome}' deveria aparecer 1 vez, apareceu {n}"
    src = src.replace(velho, novo)
    aplicadas.append({"alvo": nome, "ocorrencias_substituidas": n})
CANDIDATO.write_text(src, encoding="utf-8")

diff = list(difflib.unified_diff(
    OFICIAL.read_text(encoding="utf-8").splitlines(),
    CANDIDATO.read_text(encoding="utf-8").splitlines(),
    fromfile="oficial_76e526cf", tofile="candidato_R16", lineterm="", n=3))
hunks = [l for l in diff if l.startswith("@@")]
mais = [l for l in diff if l.startswith("+") and not l.startswith("+++")]
menos = [l for l in diff if l.startswith("-") and not l.startswith("---")]
passo("4_candidato_e_diff", edicoes=aplicadas,
      diff={"hunks": len(hunks), "linhas_adicionadas": len(mais), "linhas_removidas": len(menos),
            "linhas_tocadas_total": len(mais) + len(menos), "texto": "\n".join(diff)},
      sha_candidato=sha(CANDIDATO))

# ---------------------------------------------------------------- 5. candidato na V7
cand = rodar_p8(CANDIDATO, "candidato_R16_na_V7")
passo("5_candidato_na_V7", **cand)
R["vereditos"]["candidato_totais_identicos_2E_299A_exit1"] = (
    cand["totais"] == {"ERRO": 2, "AVISO": 299} and cand["exit"] == 1)
R["vereditos"]["candidato_V07_muda_por_identidade"] = (cand["V07_related_entities"] == [])
R["vereditos"]["candidato_V14_verde_16_regras"] = any(
    i["nivel"] == "OK" and "16 regras" in i["mensagem"] for i in cand["V14"])

# ---------------------------------------------------------------- 6. F-C2 no candidato
orig = adulterar_manifesto()
try:
    fc2_cand = rodar_p8(CANDIDATO, "fc2_candidato")
finally:
    restaurar_manifesto(orig)
passo("6_FC2_no_candidato", **fc2_cand,
      manifesto_sha_apos_restaurar=sha(MANIFESTO))
msgs = [i["mensagem"] for i in fc2_cand["V07_related_entities"] if i["nivel"] == "ERRO"]
R["vereditos"]["FC2_candidato_dispara_e_nomeia_os_dois_lados"] = any(
    "mecanismo_B16_neurogenese" in m and "mecanismo_B99_inexistente" in m for m in msgs)
R["vereditos"]["FC2_candidato_placar_3E_exit1"] = (
    fc2_cand["totais"]["ERRO"] == 3 and fc2_cand["exit"] == 1)

# ---------------------------------------------------------------- 7. instalação (backup + oficial novo + B/A)
todos_verdes = all(R["vereditos"].values())
R["vereditos"]["TODOS_OS_CRITERIOS"] = todos_verdes
if todos_verdes:
    BACKUP.write_bytes(OFICIAL.read_bytes())
    sha_antes = sha(BACKUP)
    OFICIAL.write_bytes(CANDIDATO.read_bytes())
    sha_depois = sha(OFICIAL)
    final = rodar_p8(OFICIAL, "oficial_instalado_R16")
    ba = "\n".join(difflib.unified_diff(
        BACKUP.read_text(encoding="utf-8").splitlines(),
        OFICIAL.read_text(encoding="utf-8").splitlines(),
        fromfile="antes_76e526cf", tofile="depois_R16", lineterm="", n=3))
    passo("7_instalacao", backup=str(BACKUP), sha_antes=sha_antes, sha_depois=sha_depois,
          execucao_oficial_instalado=final, BA_identico_ao_diff_medido=(ba == "\n".join(diff)), BA=ba)
    R["vereditos"]["instalacao_placar_final_2E_299A_exit1"] = (
        final["totais"] == {"ERRO": 2, "AVISO": 299} and final["exit"] == 1)
    R["novo_oficial"] = {"sha256": sha_depois, "backup": BACKUP.name,
                         "sha_antes_aposentado_com_backup": sha_antes}
else:
    passo("7_instalacao", abortada="critérios não verdes — oficial NÃO tocado")

# ---------------------------------------------------------------- 8. digitais finais
passo("8_digitais_finais", script_oficial=sha(OFICIAL), canonica_V7=sha(CANONICA),
      manifesto=sha(MANIFESTO))
R["vereditos"]["ciencia_intacta"] = (
    sha(CANONICA) == SHA_CANONICA_ESPERADO and sha(MANIFESTO) == SHA_MANIFESTO_ESPERADO)

TRILHA.write_text(json.dumps(R, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({k: v for k, v in R["vereditos"].items()}, ensure_ascii=False, indent=2))
print("diff:", R["passos"][3]["diff"]["hunks"], "hunks,",
      R["passos"][3]["diff"]["linhas_tocadas_total"], "linhas tocadas (+",
      R["passos"][3]["diff"]["linhas_adicionadas"], "/-",
      R["passos"][3]["diff"]["linhas_removidas"], ")")
print("trilha:", TRILHA.name)
