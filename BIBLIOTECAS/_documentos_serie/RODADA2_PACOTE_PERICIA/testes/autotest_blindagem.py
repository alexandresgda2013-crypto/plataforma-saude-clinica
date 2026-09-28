#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# autotest_blindagem.py — 2026-09-11. Prova da blindagem dos 3 escritores (bancada
# sintética — NUNCA toca o vivo). Cada escritor deve: (a) passar quando limpo e
# gravar com backup; (b) ABORTAR (exit≠0, arquivo intacto) quando envenenado.
import json, shutil, subprocess, sys
from pathlib import Path

PAC = Path(__file__).resolve().parent.parent
B = PAC / "bancada_teste"
sys.path.insert(0, str(PAC))

CORPO = """# Mini Canônica

A micróglia ativada libera IL-1β e TNF-α (Silva et al., 2019)[OB].

O chaveamento glicolítico sustenta a ativação (Glicolato et al., 2021)[ML].

## Referências
Silva et al., 2019.
"""
V0 = [{"id_vinculo": "VINC_B1V2_0001", "id_referencia_interna": "REF_SILVA_2019",
       "claim_id": "", "mecanismo_origem": "mecanismo_B1_neuroinflamacao",
       "secao_origem": "mecanismo_B1_neuroinflamacao/BLOCO01",
       "trecho_ancora": "A micróglia ativada libera IL-1β e TNF-α (Silva et al., 2019)[OB].",
       "natureza_relacao": "contributiva", "grau_maturidade": "bem_suportado",
       "forca_causal": "tier_3_correlacional_mecanistico", "evid_role": "human_clinical",
       "status_auditoria": "PENDENTE" if False else "CONFIRMADO",
       "status_referencia": "TRIADO", "verification_status": "verificado",
       "g3_verificado_por": "IA G3 (teste)", "g2_elegibilidade": "eligible",
       "g2_motivo": "", "g1_metodo": "eutils_automatico",
       "data_verificacao": "2026-09-04", "g3_notas": "", "pmid_oficial": "12345678"}]
REFS = [{"id_referencia_interna": "REF_SILVA_2019", "ids_referencia_interna": ["REF_SILVA_2019"],
         "pmid_oficial": "12345678", "autores": "Silva A", "ano": 2019},
        {"id_referencia_interna": "REF_GLICOLATO_2021", "ids_referencia_interna": ["REF_GLICOLATO_2021"],
         "pmid_oficial": "87654321", "autores": "Glicolato B", "ano": 2021}]

def monta(nome):
    d = B / nome
    shutil.rmtree(d, ignore_errors=True)
    (d / "Evidencias/Vinculos").mkdir(parents=True)
    (d / "Evidencias/Bibliografia").mkdir(parents=True)
    (d / "mini_canonica.md").write_text(CORPO, encoding="utf-8")
    json.dump([dict(x) for x in V0], open(d / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", "w"), ensure_ascii=False, indent=1)
    json.dump(REFS, open(d / "Evidencias/Bibliografia/01_pmids.json", "w"), ensure_ascii=False, indent=1)
    return d

def run(script, *args, cwd=None, env_extra=None):
    import os
    env = dict(os.environ, **(env_extra or {}))
    return subprocess.run([sys.executable, str(script), *map(str, args)],
                          capture_output=True, text=True, cwd=cwd, env=env)

casos = []
# ── 1. aplicar_vereditos: limpo grava c/ backup; envenenado aborta sem tocar ──
d = monta("t1")
vd = d / "ver"; vd.mkdir()
json.dump({"VINC_B1V2_0001": {"g2": "eligible", "g2_motivo": "ok", "status": "CONFIRMADO",
                              "forca": "tier_3_correlacional_mecanistico", "vs": "verificado",
                              "data": "2026-09-11"}}, open(vd / "vereditos_1.json", "w"))
r = run(PAC / "blindados/aplicar_vereditos_blindado.py", d, vd, "--aplicar")
casos.append((r.returncode == 0 and list((d / "Evidencias/Vinculos").glob("*.bak_*")), "vereditos limpo → grava c/ backup", r.stdout[-200:]))
v_antes = (d / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json").read_text()
json.dump({"VINC_B1V2_0001": {"g2": "eligible", "g2_motivo": "ok", "status": "CONFIRMADO",
                              "forca": "tier_2_intervencao", "vs": "verificado"}},
          open(vd / "vereditos_1.json", "w"))          # veneno: valor fantasma do AT-11
r = run(PAC / "blindados/aplicar_vereditos_blindado.py", d, vd, "--aplicar")
v_depois = (d / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json").read_text()
casos.append((r.returncode != 0 and v_antes == v_depois, "veredito com 'tier_2_intervencao' → ABORTA, arquivo intacto", r.stdout[-160:] + r.stderr[-160:]))

# ── 2. append blindado: reproduz linhas válidas; rejeita teto violado/âncora ausente ──
d = monta("t2")
linhas = {"linhas": [{"rotulo": "GLICOLATO_2021", "secao": "BLOCO02/2.25",
                      "ancora": "O chaveamento glicolítico sustenta a ativação (Glicolato et al., 2021)[ML].",
                      "natureza": "contributiva", "grau": "bem_suportado",
                      "forca": "tier_3_correlacional_mecanistico", "verif": "preclinico",
                      "role": "preclinical_mechanistic", "desenho": ""}]}
json.dump(linhas, open(PAC / "blindados/b1v2_linhas_teste.json", "w"), ensure_ascii=False)
r = run(PAC / "blindados/append_vinculos_b1v2_blindado.py", d, "--aplicar",
        env_extra={"B1V2_LINHAS": str(PAC / "blindados/b1v2_linhas_teste.json")})
V = json.load(open(d / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", encoding="utf-8"))
novo = [v for v in V if v["id_referencia_interna"] == "REF_GLICOLATO_2021"]
casos.append((r.returncode == 0 and len(novo) == 1 and novo[0]["id_vinculo"] == "VINC_B1V2_0002"
              and novo[0]["natureza_relacao"] == "contributiva", "append limpo → id 0002, natureza explícita, grava", r.stdout[-200:] + r.stderr[-200:]))
# veneno: âncora fora da prosa
linhas["linhas"][0]["rotulo"] = "SILVA_2019X"; linhas["linhas"][0]["ancora"] = "frase fabricada que nao existe (Silva, 2019)."
json.dump(linhas, open(PAC / "blindados/b1v2_linhas_teste.json", "w"), ensure_ascii=False)
v_antes = (d / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json").read_text()
r = run(PAC / "blindados/append_vinculos_b1v2_blindado.py", d, "--aplicar",
        env_extra={"B1V2_LINHAS": str(PAC / "blindados/b1v2_linhas_teste.json")})
casos.append((r.returncode != 0 and (d / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json").read_text() == v_antes,
              "append com âncora fabricada → ABORTA (D2)", r.stdout[-160:] + r.stderr[-160:]))

# ── 3. propaga selos: insere com literal; aborta com âncora não literal ──
d = monta("t3")
r = run(PAC / "blindados/propaga_selos_blindado.py", d / "mini_canonica.md",
        d / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", "--aplicar")
txt = (d / "mini_canonica.md").read_text(encoding="utf-8")
casos.append((r.returncode == 0 and txt.count("[VERIFICADO]") == 1 and list(d.glob("*.bak_*")),
              "propaga limpo → 1 selo [VERIFICADO] + backup", r.stdout[-200:] + r.stderr[-200:]))
V = json.load(open(d / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", encoding="utf-8"))
V[0]["trecho_ancora"] = "frase que não existe (Silva et al., 2019)[OB]."
json.dump(V, open(d / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", "w"), ensure_ascii=False)
md_antes = txt
r = run(PAC / "blindados/propaga_selos_blindado.py", d / "mini_canonica.md",
        d / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", "--aplicar")
casos.append((r.returncode != 0 and (d / "mini_canonica.md").read_text(encoding="utf-8") == md_antes,
              "propaga com âncora não literal → ABORTA, md intacto", r.stdout[-160:] + r.stderr[-160:]))

print("═" * 70)
for ok, nome, det in casos:
    print(("✅ " if ok else "❌ ") + nome)
    if not ok:
        print("   ", det[:300].replace(chr(10), " | "))
n = sum(1 for o, _, _ in casos if o)
print("═" * 70)
print(f"{n}/{len(casos)} casos corretos")
sys.exit(0 if n == len(casos) else 1)
