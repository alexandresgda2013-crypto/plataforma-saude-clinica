#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ancora_extrai.py v2 — 2026-09-11. AT-05 (B02 62 + B12 4) + literalidade (B06/B07/B08).
# Três classes de reparo (regra 5ª rodada: âncora = frase da Canônica com a citação
# NOMINAL da própria referência):
#   A) VAZIO/AUSENTE (placeholder D2, ex. "Apoio (Autor/Ano...) verificado em abstract")
#      → exatamente 1 frase de prosa com SOBRENOME+ANO da ref (linhas-lote não valem).
#   B) âncora É linha-lote (*A|B|C*) → re-ancorar à ÚNICA frase de prosa com a
#      citação nominal da ref; 0 ou N → fila humana.
#   C) âncora de prosa divergente (SELO/PROSA/ROTULO) → fuzzy-match contra as fatias
#      (SequenceMatcher em norm_selos): aplica se razão ≥ 0.85, margem ≥ 0.10 sobre o
#      2º colocado E a frase vencedora contém a citação nominal da própria ref.
# Nada é fabricado; tudo o que falha nas guardas vai à fila de confirmação humana.
import json, glob, re, sys, unicodedata, difflib
sys.path.insert(0, "/home/user/BIBLIOTECAS/_documentos_serie/scripts_serie")
import fatiador_md as F
sys.path.insert(0, "/home/user/BIBLIOTECAS/_documentos_serie/bancada_at02/scripts")
from contrato import verificar_literal, norm_selos, norm, Contrato

DATA = "2026-09-11"
def fold(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()

def refs_map(b):
    # rev. 2026-09-11 (DISTRIBUICAO-MOD09-MA-EC): [MA]->02 e [EC]->03 migrados de 01;
    # refs_map agora varre os 5 arquivos da Bibliografia (id único global entre eles —
    # validar_auditoria.py). Nada muda na lógica consumidora.
    out = {}
    for nome in ("01_pmids", "02_meta_analises", "03_ensaios_clinicos",
                 "04_atualizacoes_literatura", "05_manuais_e_livros"):
        for p in sorted(glob.glob(f"/home/user/BIBLIOTECAS/{b}/atuais/Evidencias/Bibliografia/{nome}.json")):
            d = json.load(open(p, encoding="utf-8"))
            it = d if isinstance(d, list) else d.get("referencias", d.get("refs", d.get("registros", [])))
            for x in it:
                out[(x.get("id_referencia_interna") or x.get("id") or "")] = x
    return out

def sobrenome(ref, rid):
    a = ref.get("autores") or ref.get("autor") or ""
    if isinstance(a, list): a = a[0] if a else ""
    toks = re.split(r"\s+", str(a).strip().rstrip(","))
    if toks and toks[0].lower() in ("de", "van", "von", "der", "den", "dos", "da", "del", "le", "di") and len(toks) > 1:
        s = toks[0] + " " + toks[1].rstrip(",")
    else:
        s = re.split(r"[ ,]", str(a).strip())[0].strip(".,")
    return s if len(s.strip()) >= 4 else rid.replace("REF_", "").split("_")[0].title()

def eh_lote(fr):
    return fr.count("|") >= 2 and re.fullmatch(r"[\*\s\w\[\]|.\-]*", fr) is not None

_RE_SEC_REFS = re.compile(r"refer.ncias|bibliografia|fontes\s+e\s|lista\s+de\s+fontes", re.I)

def _com_secao(fs):
    """Anota cada fatia com o cabeçalho de seção vigente (para excluir seções de referências)."""
    sec = ""
    for x in fs:
        if x["tipo"] == "cabecalho":
            sec = x["frase"]
        x["secao"] = sec
    return fs

def cita(fr, sn, ano):
    f = fold(fr)
    return re.search(r"(?<!\w)" + re.escape(fold(sn)), f) is not None and ano in f

def analisa(b):
    cpath = glob.glob(f"/home/user/BIBLIOTECAS/{b}/atuais/*.md")[0]
    corpo = open(cpath, encoding="utf-8").read()
    fs = _com_secao(F.fatiar(corpo, incluir_cabecalho=True))
    vp = glob.glob(f"/home/user/BIBLIOTECAS/{b}/atuais/Evidencias/Vinculos/*.json")[0]
    V = json.load(open(vp, encoding="utf-8")); V = V if isinstance(V, list) else V.get("vinculos")
    refs = refs_map(b)
    aplica, fila = [], []
    for r in V:
        tre = r.get("trecho_ancora") or ""
        st = verificar_literal(tre, corpo)["status"] if tre.strip() else "VAZIO"
        if st == "LITERAL":
            continue
        rid = r["id_referencia_interna"]; ref = refs.get(rid, {})
        sn = sobrenome(ref, rid); ano = (str(ref.get("ano", ""))[:4] or rid.split("_")[-1][:4])
        prosa_own = [x["frase"] for x in fs if x["tipo"] != "cabecalho" and not eh_lote(x["frase"])
                     and not _RE_SEC_REFS.search(x.get("secao") or "")
                     and cita(x["frase"], sn, ano)]
        nova, modo, motivo = None, "", ""
        if st in ("VAZIO", "AUSENTE") and not eh_lote(tre):
            modo = "AT05"
            if len(prosa_own) == 1:
                nova = prosa_own[0]
            else:
                motivo = "0 frase de prosa com a citação nominal" if not prosa_own else f"{len(prosa_own)} frases citam a ref — humano escolhe a do claim"
        elif eh_lote(tre):
            modo = "LOTE→PROSA"
            if len(prosa_own) == 1:
                nova = prosa_own[0]
            else:
                motivo = "0 frase de prosa com a citação nominal" if not prosa_own else f"{len(prosa_own)} frases citam a ref — humano escolhe"
        else:
            modo = f"lit_{st}"
            base = norm_selos(tre)
            sims = sorted(((difflib.SequenceMatcher(None, base, norm_selos(x["frase"])).ratio(), x["frase"])
                           for x in fs if x["tipo"] != "cabecalho"
                           and not _RE_SEC_REFS.search(x.get("secao") or "")),
                          key=lambda t: -t[0])[:2]
            best = sims[0]; second = sims[1][0] if len(sims) > 1 else 0.0
            if best[0] >= 0.85 and (best[0] - second) >= 0.10 and cita(best[1], sn, ano):
                nova = best[1]
            else:
                motivo = (f"fuzzy insuficiente (best={best[0]:.2f}, margem={best[0]-second:.2f}"
                          + ("" if cita(best[1], sn, ano) else ", vencedora sem a citação da própria ref") + ")")
        if nova:
            aplica.append((r, nova, modo))
        else:
            fila.append({"id_vinculo": r["id_vinculo"], "ref": rid, "consulta": f"{sn} {ano}",
                         "status_atual": st, "motivo_fila": motivo, "ancora_atual": tre[:200],
                         "candidatas": prosa_own[:6]})
    return V, vp, corpo, aplica, fila

def main():
    bibs = ["B02_Eixo_HPA_cortisol", "B12_NeurobiologiaTrauma", "B06_EstresseOxidativo",
            "B07_EixoIntestinoCerebro", "B08_Micronutrientes"]
    apply_mode = "--apply" in sys.argv
    fila_total, resumo = {}, {}
    for b in bibs:
        V, vp, corpo, aplica, fila = analisa(b)
        bn = b.split("_")[0]
        print(f"{bn}: aplica={len(aplica)} fila_humana={len(fila)}  modos={ {m: sum(1 for _,_,mm in aplica if mm==m) for m in set(mm for _,_,mm in aplica)} }")
        resumo[bn] = (len(aplica), len(fila))
        if apply_mode and aplica:
            for r, nova, modo in aplica:
                velha = (r.get("trecho_ancora") or "")[:80]
                r["trecho_ancora"] = nova
                tag = f"{DATA} ÂNCORA-{modo}: re-extraída da prosa canônica c/ citação nominal da própria ref (guardas; era «{velha}…»)"
                r["nota_reparo"] = (r["nota_reparo"] + " || " if (r.get("nota_reparo") or "").strip() else "") + tag
                r["reancorado_em"] = DATA
            c = Contrato("vinculo", corpo_canonico=corpo)
            rest = [p for p in c.validar(V) if p.nivel == "BLOQUEANTE"]
            duros = [p for p in rest if p.campo not in {"id_vinculo", "g2_elegibilidade", "trecho_ancora"}]
            if duros:
                print("  !! ABORT", duros[0]); sys.exit(2)
            res = c.gravar(vp, V)
            tp = vp.split("/Evidencias/Vinculos")[0] + f"/producao/07_ancoras_{bn}_2026-09-11.json"
            json.dump({"data": DATA, "bib": bn, "backup": res["backup"],
                       "aplicadas": [{"id": r["id_vinculo"], "modo": m} for r, _, m in aplica],
                       "restantes_fila": len(fila)}, open(tp, "w"), ensure_ascii=False, indent=1)
            print(f"  gravado; trilha 07_ancoras_{bn}_2026-09-11.json")
        if fila:
            fila_total[bn] = fila
    json.dump(fila_total, open("/home/user/BIBLIOTECAS/_documentos_serie/CONFIRMACAO_HUMANA_ANCORAS_2026-09-11.json", "w"),
              ensure_ascii=False, indent=1)
    print("fila humana:", {k: len(v) for k, v in fila_total.items()})

if __name__ == "__main__":
    main()
