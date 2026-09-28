#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
separa_ma_ec_09.py — Distribuição oficial Módulo 09 (rev. inicial 2026-09-11)
==============================================================================
Lei aplicada: instrução final de geração do PROMPT v4.2 — [MA]→02_meta_analises.json,
[EC]→03_ensaios_clinicos.json; id único GLOBAL entre os 5 arquivos (validar_auditoria.py:
"id_referencia_interna duplicado" = ERRO) → operação = MOVE, nunca cópia nos arquivos
de mecanismo. O "todos juntos" para o motor clínico vive em BIBLIOTECAS/MOTOR_CLINICO/.

Classificação (mecânica, replicável, sem invenção):
  MA: tag [MA...] em desenho_estudo (declarada pela canônica) OU título com
      meta-anal*/systematic review (sinal objetivo PubMed).
  EC: título OU desenho com randomized/randomised/double-blind/placebo-controlled/
      crossover/ensaio randomizado/duplo-cego (sinal objetivo de desenho RCT).
  Prioridade MA > EC quando ambos disparam (ex.: "mega-analysis of randomized trials").
  Casos tag-[EC] amplo sem sinal RCT NÃO migram (09.3 é reservado a RCT) — ficam
  nomeados na trilha para ratificação externa. Idem conflitos tag×título.

Escrita: backup .bak_AAAAMMDD_HHMMSS antes de gravar (atomicamente); campos de dados
(id, pmid, titulo, achado...) INTACTOS; acrescenta apenas:
  02:  bloco_origem (existente ou derivado-mecânico de secao_origem, marcado),
       forca_evidencia_afirmacao (existente ou "" — vazio = dívida, nunca fabricado),
  ambos: sinais_classificacao[], migrado_em, migracao_ref.
Consolidado série: MOTOR_CLINICO/evidencias_ma_serie.json + evidencias_ec_serie.json
(dedup por pmid_oficial; bibliotecas[] lista todas as casas).
Trilha: atuais/producao/09_distribuicao_MA_EC_<Bn>_2026-09-11.json + série.

Uso: python3 separa_ma_ec_09.py            (dry-run, padrão — não grava nada)
     python3 separa_ma_ec_09.py --apply    (executa a migração)
"""
import json, re, sys, shutil, datetime
from pathlib import Path

RAIZ = Path("/home/user/BIBLIOTECAS")
DATA = "2026-09-11"
APPLY = "--apply" in sys.argv

RE_TAG = re.compile(r"\[([^\]]{1,24})\]")
RE_MA_TIT = re.compile(r"meta[-\u2010 ]?anal|metaanal|systematic review", re.I)
RE_EC = re.compile(r"randomi[sz]ed|double[- ]?blind|placebo[- ]?controlled|crossover|"
                   r"randomly assigned|duplo[- ]?cego|ensaio cl[ií]nico randomizado", re.I)

def tag_primaria(desenho):
    """Primeira etiqueta [...] do desenho_estudo; família = texto antes da 1ª '/'."""
    m = RE_TAG.search(desenho or "")
    if not m:
        return "", ""
    bruta = m.group(1).strip()
    return bruta, bruta.split("/")[0].strip()

def classificar(r):
    """Retorna (classe, sinais, conflito). classe in {'MA','EC',None}."""
    des = r.get("desenho_estudo", "") or ""
    tit = r.get("titulo_artigo", "") or ""
    bruta, fam = tag_primaria(des)
    sinais, conflito = [], ""
    s_ma_tit = bool(RE_MA_TIT.search(tit))
    s_ec = bool(RE_EC.search(tit) or RE_EC.search(des))
    tag_ma = fam.upper() == "MA"
    tag_ec = fam.upper() == "EC"
    if tag_ma: sinais.append(f"tag_desenho:[{bruta}]")
    if s_ma_tit: sinais.append("titulo:meta-analise/revisao-sistematica")
    if tag_ec: sinais.append(f"tag_desenho:[{bruta}]")
    Classe = None
    if tag_ma or s_ma_tit:
        Classe = "MA"
        if tag_ec or (s_ec and not s_ma_tit):
            conflito = f"MA escolhida (prioridade); sinal EC presente [tag={bruta!r}]"
            sinais.append("conflito:" + conflito)
    elif s_ec:
        Classe = "EC"
        sinais.append("desenho_rct:" + ("titulo" if RE_EC.search(tit) else "desenho_estudo"))
        if tag_ec and not s_ec:
            Classe = None  # inalcançável; guarda
    elif tag_ec:
        Classe = None  # [EC] amplo sem sinal RCT -> NÃO migra (09.3 = RCT estrito)
    return Classe, sinais, conflito

def carrega(p):
    d = json.loads(p.read_text(encoding="utf-8"))
    assert isinstance(d, list), f"{p}: raiz não é lista"
    return d

def bibs():
    return sorted(p for p in RAIZ.glob("B*") if (p / "atuais").is_dir())

resumo = {}
cons_ma, cons_ec = {}, {}   # pmid -> (ficha, set(bibliotecas))
hoje = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

for bibdir in bibs():
    bn = bibdir.name
    pasta = bibdir / "atuais" / "Evidencias" / "Bibliografia"
    f01, f02, f03 = pasta / "01_pmids.json", pasta / "02_meta_analises.json", pasta / "03_ensaios_clinicos.json"
    pm = carrega(f01); ma_at = carrega(f02); ec_at = carrega(f03)
    assert not ma_at and not ec_at, f"{bn}: 02/03 já preenchidos — abortar (não é idempotente)"

    fica, vai_ma, vai_ec, conflitos, tag_ec_amplo = [], [], [], [], []
    for r in pm:
        classe, sinais, conf = classificar(r)
        rec = dict(r)
        if classe:
            rec["sinais_classificacao"] = sinais
            rec["migrado_em"] = DATA
            rec["migracao_ref"] = "09_distribuicao_MA_EC_2026-09-11_INSTRUCAO_FINAL_GERACAO_PROMPT_v4.2"
            if classe == "MA":
                if not rec.get("bloco_origem"):
                    rec["bloco_origem"] = rec.get("secao_origem", "")
                    rec["bloco_origem_derivado_de_secao"] = True
                rec.setdefault("forca_evidencia_afirmacao", rec.get("forca_evidencia_afirmacao", ""))
                vai_ma.append(rec)
            else:
                vai_ec.append(rec)
            if conf: conflitos.append({"id": r.get("id_referencia_interna"), "pmid": r.get("pmid_oficial"), "conflito": conf, "classe_dada": classe})
        else:
            _, fam = tag_primaria(r.get("desenho_estudo", ""))
            if fam.upper() == "EC":
                tag_ec_amplo.append({"id": r.get("id_referencia_interna"), "pmid": r.get("pmid_oficial"),
                                     "desenho_estudo": (r.get("desenho_estudo") or "")[:120],
                                     "titulo": (r.get("titulo_artigo") or "")[:140]})
            fica.append(r)

    ids_saindo = {r["id_referencia_interna"] for r in vai_ma + vai_ec}
    assert len(ids_saindo) == len(vai_ma) + len(vai_ec), f"{bn}: id duplicado na partição"
    assert not (ids_saindo & {r["id_referencia_interna"] for r in fica}), f"{bn}: sobreposição pós-migração"

    resumo[bn] = {"ficam_01": len(fica), "vao_02_MA": len(vai_ma), "vao_03_EC": len(vai_ec),
                  "conflitos": len(conflitos), "tag_EC_amplo_nao_migrado": len(tag_ec_amplo)}

    trilha = {"acao": "09_distribuicao_MA_EC_MODULO09", "data": DATA, "biblioteca": bn,
              "lei": "PROMPT_v4.2 instrução final: [MA]->02, [EC]->03; id único global (validar_auditoria.py)",
              "regra_classificacao": "MA: tag [MA] ou título meta-anal*/systematic review; EC: título/desenho randomized|double-blind|placebo-controlled|crossover|duplo-cego; prioridade MA>EC",
              "contagens": resumo[bn],
              "ids_para_02": [{"id": r["id_referencia_interna"], "pmid": r.get("pmid_oficial"), "sinais": r["sinais_classificacao"]} for r in vai_ma],
              "ids_para_03": [{"id": r["id_referencia_interna"], "pmid": r.get("pmid_oficial"), "sinais": r["sinais_classificacao"]} for r in vai_ec],
              "conflitos_tag_x_titulo_REVISAVEL": conflitos,
              "REVISAVEL_tag_EC_amplo_sem_sinal_RCT_nao_migrado": tag_ec_amplo,
              "divida_nomeada": "forca_evidencia_afirmacao vazio quando a ficha não trazia (schema 09.2 exige; preenchimento exige avaliação — não fabricar)"}

    if APPLY:
        prod = bibdir / "atuais" / "producao"; prod.mkdir(exist_ok=True)
        for f in (f01, f02, f03):
            shutil.copy2(f, f.with_suffix(f.suffix + f".bak_{hoje}"))
        tmp = f01.with_suffix(".tmp"); tmp.write_text(json.dumps(fica, indent=1, ensure_ascii=False), encoding="utf-8"); tmp.replace(f01)
        tmp = f02.with_suffix(".tmp"); tmp.write_text(json.dumps(vai_ma, indent=1, ensure_ascii=False), encoding="utf-8"); tmp.replace(f02)
        tmp = f03.with_suffix(".tmp"); tmp.write_text(json.dumps(vai_ec, indent=1, ensure_ascii=False), encoding="utf-8"); tmp.replace(f03)
        (prod / f"09_distribuicao_MA_EC_{bn.split('_')[0]}_{DATA}.json").write_text(
            json.dumps(trilha, indent=1, ensure_ascii=False), encoding="utf-8")

    for r in vai_ma:
        pmid = r.get("pmid_oficial") or r["id_referencia_interna"]
        e = cons_ma.setdefault(pmid, {"ficha": {k: v for k, v in r.items() if k not in ("migrado_em",)}, "bibliotecas": set()})
        e["bibliotecas"].add(bn)
    for r in vai_ec:
        pmid = r.get("pmid_oficial") or r["id_referencia_interna"]
        e = cons_ec.setdefault(pmid, {"ficha": {k: v for k, v in r.items() if k not in ("migrado_em",)}, "bibliotecas": set()})
        e["bibliotecas"].add(bn)

# ---- consolidado motor clínico ------------------------------------------------
def serie(cons, classe):
    saida = []
    for pmid, e in sorted(cons.items(), key=lambda kv: kv[1]["ficha"].get("revista_ano", "")):
        f = dict(e["ficha"]); f["classe_serie"] = classe
        f["bibliotecas"] = sorted(e["bibliotecas"])
        saida.append(f)
    return saida

ma_s, ec_s = serie(cons_ma, "meta_analise_ou_revisao_sistematica"), serie(cons_ec, "ensaio_clinico_randomizado")

tot = {"bibliotecas": {b: r for b, r in resumo.items()},
       "serie": {"ma_total_pre_dedup": sum(r["vao_02_MA"] for r in resumo.values()),
                 "ec_total_pre_dedup": sum(r["vao_03_EC"] for r in resumo.values()),
                 "ma_unicos_dedup_pmid": len(ma_s), "ec_unicos_dedup_pmid": len(ec_s),
                 "conflitos": sum(r["conflitos"] for r in resumo.values()),
                 "tag_EC_amplo_nao_migrado": sum(r["tag_EC_amplo_nao_migrado"] for r in resumo.values())}}

print(json.dumps(tot, indent=1, ensure_ascii=False))

if APPLY:
    mc = RAIZ / "MOTOR_CLINICO"; mc.mkdir(exist_ok=True)
    (mc / "evidencias_ma_serie.json").write_text(json.dumps(ma_s, indent=1, ensure_ascii=False), encoding="utf-8")
    (mc / "evidencias_ec_serie.json").write_text(json.dumps(ec_s, indent=1, ensure_ascii=False), encoding="utf-8")
    (RAIZ / "_documentos_serie" / "scripts_serie" / f"trilha_09_distribuicao_MA_EC_serie_{DATA}.json").write_text(
        json.dumps(tot, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nGRAVADO. MOTOR_CLINICO/: ma={len(ma_s)} ec={len(ec_s)} (dedup por PMID; bibliotecas[] por registro)")
else:
    print("\nDRY-RUN — nada gravado. Revise contagens/conflitos antes de --apply.")
