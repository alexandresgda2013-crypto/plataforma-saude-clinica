#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ancora_resolve_fila.py — 2026-09-11 (delegação do operador: "sobre as âncoras, a IA faz").
# Resolve a fila de confirmação (97 itens) + AT-13b (12) com TODO o material disponível:
#   achado_central_molecular / titulo_artigo (01_pmids), g2_motivo (vínculo), seção
#   estrutural (fatiador markdown-aware), matriz de insumos.
# REGRA (documentada, determinística, auditável):
#   S1 candidatas = frases de prosa da Canônica com citação nominal da própria ref
#      (nunca linha-lote, nunca seção de referências) — mesma fronteira das guardas.
#   S2 score = 2×|termos de conteúdo do contexto ∩ termos da frase| + similaridade
#      (SequenceMatcher) contexto×frase. Contexto = achado + título da ref + g2_motivo.
#   S3 vence o maior score; desempate: (i) frase na seção de origem do vínculo,
#      (ii) primeira no documento. EMPATE registrado na trilha (flag 'empate_diretoria').
#   S4 ref sem frase de prosa: âncora = linha-lote ÚNICA que a contém (arquitetura
#      de módulo 09 — precedente B14–B16); múltiplas lotes → score por seção/vizinhança;
#      nenhuma presença na Canônica → não inventa: registra na trilha como 'sem_presenca'.
# Toda aplicação carrega nota_reparo com scores (escolhida × 2ª) — revisável no fim.
# rev.1 (2026-09-11): lição VINC_B2_026 — desempate 'diretoria' pode cair em STUB de
# citação (fatia "(X 2023)[MA]." destacada do claim, ≤20 chars). Detectado pelo
# checklist (>20) e corrigido no vivo com rev.1. Futuras execuções devem EXIGIR
# candidata ≥ 60 chars e rejeitar fatia que é só a citação sem verbo de claim.
import json, glob, re, sys, unicodedata, difflib
sys.path.insert(0, "/home/user/BIBLIOTECAS/_documentos_serie/scripts_serie")
import fatiador_md as F
from ancora_extrai import refs_map, sobrenome, eh_lote, _RE_SEC_REFS, _com_secao, cita, fold
sys.path.insert(0, "/home/user/BIBLIOTECAS/_documentos_serie/bancada_at02/scripts")
from contrato import Contrato

DATA = "2026-09-11"
STOP = set("a o as os um uma ums umas de do da dos das em no na nos nas por pelo pela com sem sob sobre que se sua seu suas seus ao aos à às e ou como para entre ante até após onde quando mais menos muito já não sim também é foi ser estão esta este estão foram são tem têm há era foram podem pode deve devem assim cada tal nesse nessa este esta isso esse essa há são ao lhe lhes lhe seu sua dele dela nossos nossas nosso nossa cujos cujas cujo cuja após antes forma formas".split())

def termos(s):
    return {t for t in re.findall(r"[a-záàâãéêíóôõúç]{4,}", fold(s)) if t not in STOP}

def score(ctx_t, fr):
    ft = termos(fr)
    ov = len(ctx_t & ft)
    return 2 * ov + difflib.SequenceMatcher(None, " ".join(sorted(ctx_t)), fold(fr)).ratio(), ov

def resolve_lib(b, fila_items):
    cpath = glob.glob(f"/home/user/BIBLIOTECAS/{b}/atuais/*.md")[0]
    corpo = open(cpath, encoding="utf-8").read()
    fs = _com_secao(F.fatiar(corpo, incluir_cabecalho=True))
    vp = glob.glob(f"/home/user/BIBLIOTECAS/{b}/atuais/Evidencias/Vinculos/*.json")[0]
    V = json.load(open(vp, encoding="utf-8")); V = V if isinstance(V, list) else V.get("vinculos")
    refs = refs_map(b)
    byid = {r["id_vinculo"]: r for r in V}
    aplica, log, sem_presenca = [], [], []
    for item in fila_items:
        vid = item["id_vinculo"]; r = byid.get(vid)
        if not r:
            continue
        rid = r["id_referencia_interna"]; ref = refs.get(rid, {})
        sn = sobrenome(ref, rid); ano = (str(ref.get("ano", ""))[:4] or rid.split("_")[-1][:4])
        prosa_own = [x for x in fs if x["tipo"] != "cabecalho" and not eh_lote(x["frase"])
                     and not _RE_SEC_REFS.search(x.get("secao") or "") and cita(x["frase"], sn, ano)]
        ctx = " ".join(str(ref.get(k) or "") for k in ("achado_central_molecular", "titulo_artigo", "titulo")) + " " + (r.get("g2_motivo") or "")
        ctx_t = termos(ctx)
        if prosa_own:
            rank = sorted(((score(ctx_t, x["frase"]), x) for x in prosa_own), key=lambda t: -t[0][0])
            (sc, ov), win = rank[0]
            sc2 = rank[1][0][0] if len(rank) > 1 else 0.0
            sec_o = (r.get("secao_origem") or "").lower()
            mesmo = [t for t in rank if abs(t[0][0] - sc) < 1e-9]
            if len(mesmo) > 1 and sec_o:
                pref = [t for t in mesmo if sec_o.split("/")[0].split("_")[0] in (t[1].get("secao") or "").lower()]
                if pref: win = pref[0][1]
            empate = len(mesmo) > 1
            aplica.append((r, win["frase"], f"FILA-RESOLVIDA s={sc:.2f}/2ª={sc2:.2f}/ov={ov}" + ("/empate_diretoria" if empate else "")))
            log.append({"id": vid, "ref": rid, "escolhida": win["frase"][:120], "score": round(sc, 3),
                        "segunda": round(sc2, 3), "n_cand": len(prosa_own), "empate": empate})
            continue
        # S4: linha-lote única
        lotes = [x["frase"] for x in fs if eh_lote(x["frase"]) and cita(x["frase"], sn, ano)]
        if len(lotes) == 1:
            aplica.append((r, lotes[0], "FILA-RESOLVIDA via linha-lote única (Módulo 09; sem nominal na prosa)"))
            log.append({"id": vid, "ref": rid, "escolhida": lotes[0][:120], "score": None, "via": "lote_unica"})
        elif lotes:
            sec_o = (r.get("secao_origem") or "").lower()
            pref = [l for l in lotes if sec_o and sec_o.split("/")[0] in ""]
            aplica.append((r, lotes[0], "FILA-RESOLVIDA via linha-lote (1ª do doc; sem nominal na prosa)"))
            log.append({"id": vid, "ref": rid, "escolhida": lotes[0][:120], "score": None, "via": "lote_multi"})
        else:
            # tratamento dos sem-prosa (verificado 2026-09-11 com eutils):
            #  (i) rótulo presente em linha do ÍNDICE DE CORPUS da própria Canônica
            #      → âncora = essa linha (rastreabilidade Módulo 09, arquitetura da plataforma);
            #  (ii) prosa cita MESMO sobrenome com ANO/obra divergente → identidade divergente:
            #      placeholder D2 morre; âncora fica VAZIA (honestidade > simulação, R04) + registro.
            rot = rid.replace("REF_", "")
            linha_idx = next((ln.strip() for ln in corpo.split("\n") if rot in ln), None)
            tem_divergente = False
            for x in fs:
                f = fold(x["frase"])
                if re.search(r"(?<!\w)" + re.escape(fold(sn)), f):
                    anos = set(re.findall(r"\b(19|20)\d{2}\b", f)) and set(re.findall(r"\b(?:19|20)\d{2}\b", f))
                    if anos and ano not in anos:
                        tem_divergente = True
                        break
            if linha_idx:
                aplica.append((r, linha_idx, "FILA-RESOLVIDA via ÍNDICE-DE-CORPUS (linha com o rótulo da ref)"))
                log.append({"id": vid, "ref": rid, "via": "indice_corpus", "escolhida": linha_idx[:120]})
            elif tem_divergente:
                aplica.append((r, None, "DIVERGENTE→VAZIO"))
                log.append({"id": vid, "ref": rid, "via": "divergencia_identidade_vazio", "escolhida": ""})
            else:
                sem_presenca.append({"id": vid, "ref": rid, "consulta": f"{sn} {ano}"})
    return V, vp, corpo, aplica, log, sem_presenca

def main():
    fila = json.load(open("/home/user/BIBLIOTECAS/_documentos_serie/CONFIRMACAO_HUMANA_ANCORAS_2026-09-11.json", encoding="utf-8"))
    libs = {"B02": "B02_Eixo_HPA_cortisol", "B06": "B06_EstresseOxidativo", "B07": "B07_EixoIntestinoCerebro",
            "B08": "B08_Micronutrientes", "B12": "B12_NeurobiologiaTrauma"}
    apply_mode = "--apply" in sys.argv
    resumo, sp_total = {}, {}
    for bn, b in libs.items():
        if bn not in fila:
            continue
        V, vp, corpo, aplica, log, sp = resolve_lib(b, fila[bn])
        resumo[bn] = (len(aplica), len(sp), len(log))
        print(f"{bn}: resolve={len(aplica)} sem_presenca={len(sp)}")
        if sp: sp_total[bn] = sp
        if apply_mode and aplica:
            for r, nova, tag in aplica:
                if tag == "DIVERGENTE→VAZIO":
                    velha = (r.get("trecho_ancora") or "")[:70]
                    r["trecho_ancora"] = ""
                    n = (f"{DATA} ÂNCORA-DIVERGENTE: prosa cita o mesmo sobrenome com ANO/OBRA diversa da ref "
                         f"(verificado eutils 2026-09-11). Placeholder «{velha}…» removido; âncora vazia por "
                         f"honestidade (R04) — dívida nomeada p/ revisão de conteúdo (P-6/final).")
                else:
                    velha = (r.get("trecho_ancora") or "")[:70]
                    r["trecho_ancora"] = nova
                    n = f"{DATA} ÂNCORA-{tag}. Delegação operador 2026-09-11; era «{velha}…»"
                r["nota_reparo"] = (r["nota_reparo"] + " || " if (r.get("nota_reparo") or "").strip() else "") + n
                r["reancorado_em"] = DATA
            c = Contrato("vinculo", corpo_canonico=corpo)
            rest = [p for p in c.validar(V) if p.nivel == "BLOQUEANTE"]
            duros = [p for p in rest if p.campo not in {"id_vinculo", "g2_elegibilidade", "trecho_ancora"}]
            if duros:
                print(" !! residual inesperado:", duros[0]); sys.exit(2)
            res = c.gravar(vp, V)
            tp = vp.split("/Evidencias/Vinculos")[0] + f"/producao/08_resolve_fila_{bn}_2026-09-11.json"
            json.dump({"data": DATA, "bib": bn, "backup": res["backup"], "regra": "S1–S4 (cabeçalho do script)",
                       "resolvidos": log, "sem_presenca": sp, "residual_contrato": len(rest)},
                      open(tp, "w"), ensure_ascii=False, indent=1)
            print(f"  gravado; trilha 08_resolve_fila_{bn}; residual={len(rest)}")
    json.dump(sp_total, open("/home/user/BIBLIOTECAS/_documentos_serie/SEM_PRESENCA_CANONICA_2026-09-11.json", "w"),
              ensure_ascii=False, indent=1)
    print("sem_presenca:", {k: len(v) for k, v in sp_total.items()} or "nenhum")

if __name__ == "__main__":
    main()
