#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reparo_coerencia_2026-09-13.py — execução das condições C1, C2, C5 e C6 da
re-auditoria do Auditor-Mestre (2026-09-13) sobre a B1 V5.

REGRAS OBEDECIDAS
  · nada é fabricado: todo valor novo é DERIVADO do próprio acervo (prosa da
    canônica, título PubMed já catalogado, ou marcador de bloco do texto);
  · nada é silencioso: backup .bak datado + trilha JSON por operação;
  · a CIÊNCIA da canônica NÃO é tocada (0 linhas do .md são alteradas);
  · o que exige decisão humana ou rito [AT] fica FORA daqui e vai para
    PENDENCIAS_HUMANAS (impresso ao final).

O QUE FAZ
  R-01 (C1) propaga as correções R2/R11 já aplicadas na prosa para as camadas
       que o motor lê: achado_central_molecular das fichas e g3_notas dos
       vínculos/ledger que ficaram descrevendo a versão anterior.
  R-02 (C2) re-ancora os 16 vínculos do R8 da linha-lote para a frase de prosa
       que cita nominalmente cada referência; deriva claim_id do marcador
       (BLOCOxx.yyy) da subseção que contém a frase.
  R-05 (C6) repara as 35 âncoras com deriva TIPOGRÁFICA (markdown, travessão,
       espaço antes de [TAG]) — reparo determinístico, sítio único conferido.
  R-06 (C5) sincroniza o manifesto com a canônica (fonte única) e resolve os
       placeholders de template.
  R-07 preenche citacao_literal do ledger com a citação real extraída da própria
       âncora, substituindo o token TIPO[TAG].

Uso: python3 reparo_coerencia_2026-09-13.py <pasta_atuais> [--dry-run]
"""
import json, re, sys, shutil, unicodedata
from datetime import date
from pathlib import Path

HOJE = "2026-09-13"
TAG = f".bak_pre_reparo_{HOJE.replace('-','')}"

def nfc(s): return unicodedata.normalize("NFC", str(s))
def ne(s):  return re.sub(r"\s+", " ", nfc(s).replace(" ", " ")).strip()
def nt(s):
    s = nfc(s)
    s = re.sub(r"[*`]", "", s)
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    return re.sub(r"\s+", "", s)
def sa(s):
    return "".join(c for c in unicodedata.normalize("NFKD", nfc(s)) if not unicodedata.combining(c))


def nota(obj, entrada):
    """Anexa nota_reparo preservando valor legado (alguns registros trazem string)."""
    atual = obj.get("nota_reparo")
    if atual is None:
        obj["nota_reparo"] = [entrada]
    elif isinstance(atual, list):
        atual.append(entrada)
    else:
        obj["nota_reparo"] = [{"data": "legado", "valor_anterior": atual}, entrada]


def fatia_literal(texto, ancora):
    """Recupera do texto ORIGINAL a fatia que corresponde à âncora, comparando
    na forma tipográfica normalizada. Devolve None se não houver sítio único."""
    orig = nfc(texto)
    mapa, buf = [], []
    for i, ch in enumerate(orig):
        n = nt(ch)
        if n:
            buf.append(n); mapa.append(i)
    Tn = "".join(buf)
    alvo = nt(ancora)
    if not alvo:
        return None
    if Tn.count(alvo) != 1:
        return None
    ini = Tn.find(alvo)
    return ne(orig[mapa[ini]: mapa[ini + len(alvo) - 1] + 1])

def backup(p: Path, dry):
    if not dry:
        shutil.copy2(p, p.with_name(p.name + TAG))

def salvar(p: Path, obj, dry):
    if not dry:
        p.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")

# --------------------------------------------------------------- correções C1
# Cada entrada: (id, campo, de -> para, justificativa ancorada na prosa da V5)
CORRECOES_C1 = {
    "REF_COMAI_2022": {
        "achado_central_molecular":
            "citocinas e razao KYN/TRP associam-se seletivamente a alteracoes de substancia "
            "branca em depressao BIPOLAR e NAO em unipolar (titulo PubMed 34847455)",
        "motivo": "R2/AUD-027: a prosa da V5 foi corrigida para a seletividade; o resumo da "
                  "ficha mantinha 'bipolar/TDM', contradizendo o titulo do proprio registro.",
    },
    "REF_ENACHE_2019": {
        "achado_central_molecular":
            "meta-analise de marcadores centrais no TDM em LCR e PET (69 estudos); pos-morte "
            "tratado como revisao narrativa, sem metanalise; marcadores centrais parcialmente "
            "independentes dos perifericos",
        "motivo": "R11/AUD-030: escopo corrigido na prosa da V5; ficha e ledger mantinham "
                  "'meta tri-compartimental'.",
    },
}
CORRECOES_C1_VINC = {
    "VINC_B1_0219": ("g3_notas",
        "Meta de LCR e PET (69 estudos); pos-morte apenas narrativo. Dissociacao "
        "central-periferica e heterogeneidade. "
        f"{HOJE} (R11/AUD-030, re-auditoria): escopo corrigido — nao e meta tri-compartimental."),
    "VINC_B1_0247": ("g3_notas",
        "[EXTRAPOLADO: PSP->TDM]. Unica validacao pos-morte (n=8, PSP): correlacao POSITIVA "
        "entre PK11195 in vivo e carga microglial CD68+/TSPO pos-morte. "
        f"{HOJE} (R11/AUD-029, re-auditoria): enquadramento 'questao aberta' substituido pelo "
        "resultado positivo, com limite de amostra e extrapolacao pendente."),
}
CORRECOES_C1_LEDGER = {
    "REF_ENACHE_2019": ("meta de LCR e PET (69 estudos); pos-morte narrativo", "tri-compartimental"),
    "REF_WIJESINGHE_2025": ("validacao pos-morte com correlacao positiva (n=8, PSP)", "questao aberta"),
}

def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    raiz = Path(sys.argv[1]).resolve()
    dry = "--dry-run" in sys.argv
    trilha = {"data": HOJE, "origem": "re-auditoria Auditor-Mestre 2026-09-13",
              "dry_run": dry, "operacoes": []}
    pend = []

    canon = sorted([p for p in raiz.glob("*.md") if "CANONICA" in p.name.upper()])[-1]
    texto = canon.read_text(encoding="utf-8")
    linhas = texto.split("\n")

    bibdir = raiz / "Evidencias" / "Bibliografia"
    vpath = raiz / "Evidencias" / "Vinculos" / "vinculos_referencia_afirmacao.json"
    lpath = next(raiz.glob("Auditoria_*/ledger_auditoria_*.json"))
    mpath = bibdir / "_manifesto_biblioteca.json"

    arqs = {n: json.loads((bibdir / n).read_text(encoding="utf-8"))
            for n in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json")
            if (bibdir / n).exists()}
    vinc = json.loads(vpath.read_text(encoding="utf-8"))
    led = json.loads(lpath.read_text(encoding="utf-8"))
    man = json.loads(mpath.read_text(encoding="utf-8"))

    # ============================================================ R-01 (C1)
    n = 0
    for nome, dados in arqs.items():
        for r in dados:
            rid = r.get("id_referencia_interna")
            if rid in CORRECOES_C1:
                antes = r.get("achado_central_molecular")
                novo = CORRECOES_C1[rid]["achado_central_molecular"]
                if ne(antes) != ne(novo):
                    r["achado_central_molecular"] = novo
                    nota(r, {
                        "data": HOJE, "regra": "C1/AUD-049", "campo": "achado_central_molecular",
                        "valor_anterior": antes, "motivo": CORRECOES_C1[rid]["motivo"]})
                    trilha["operacoes"].append({"op": "R-01", "arquivo": nome, "id": rid,
                                                "de": antes, "para": novo})
                    n += 1
    for v in vinc:
        vid = v.get("id_vinculo")
        if vid in CORRECOES_C1_VINC:
            campo, novo = CORRECOES_C1_VINC[vid]
            antes = v.get(campo)
            if ne(antes) != ne(novo):
                v[campo] = novo
                trilha["operacoes"].append({"op": "R-01", "arquivo": "vinculos", "id": vid,
                                            "de": antes, "para": novo})
                n += 1
    for e in led:
        rid = e.get("id_referencia_interna")
        if rid in CORRECOES_C1_LEDGER:
            novo, alvo = CORRECOES_C1_LEDGER[rid]
            blob = json.dumps(e, ensure_ascii=False)
            if sa(alvo).lower() in sa(blob).lower():
                for k, val in list(e.items()):
                    if isinstance(val, str) and sa(alvo).lower() in sa(val).lower():
                        antes = val
                        e[k] = re.sub(re.escape(alvo), novo, val, flags=re.I)
                        nota(e, {
                            "data": HOJE, "regra": "C1/AUD-049", "campo": k,
                            "valor_anterior": antes})
                        trilha["operacoes"].append({"op": "R-01", "arquivo": "ledger",
                                                    "id": e.get("id_auditoria"), "campo": k,
                                                    "de": antes, "para": e[k]})
                        n += 1
    print(f"R-01 (C1) propagação das correções à camada de evidência: {n} campo(s)")

    # ============================================================ R-02 (C2)
    # re-ancorar os 16 vínculos do R8 na frase de prosa que cita a referência
    LOTE_RE = re.compile(r"^\s*\*[A-Za-z0-9_À-ÿ]+\[[A-Z]{2}\].*\*\s*$")
    BLOCO_RE = re.compile(r"\(BLOCO(\d{2})\.(\d{3})\)")
    reanc, nao_reanc = 0, []
    for v in vinc:
        vid = v.get("id_vinculo", "")
        if not re.fullmatch(r"VINC_B1_02(5[89]|6\d|7[0-3])", vid):
            continue
        rid = v.get("id_referencia_interna", "")
        m = re.match(r"REF_([A-Z]+)_(\d{4})", rid)
        if not m:
            nao_reanc.append((vid, rid, "id fora do padrão")); continue
        sob, ano = m.group(1).title(), m.group(2)
        alvos = []
        for i, ln in enumerate(linhas):
            if LOTE_RE.match(ln) or ln.strip().startswith(("#", "|", "---")):
                continue
            if re.search(rf"\(\s*{re.escape(sob)}[^()]{{0,40}},\s*{ano}[a-z]?\)", ln, re.I):
                alvos.append(i)
        if len(alvos) != 1:
            nao_reanc.append((vid, rid, f"{len(alvos)} frase(s) de prosa candidatas"))
            continue
        i = alvos[0]
        frase = None
        for f in re.split(r"(?<=[.!?])\s+", linhas[i]):
            if re.search(rf"\(\s*{re.escape(sob)}[^()]{{0,40}},\s*{ano}[a-z]?\)", f, re.I):
                frase = ne(f); break
        if not frase or nt(frase) not in nt(texto):
            nao_reanc.append((vid, rid, "frase não isolável")); continue
        if nt(texto).count(nt(frase)) != 1:
            nao_reanc.append((vid, rid, "frase não é sítio único")); continue
        claim = ""
        for j in range(i, -1, -1):
            bm = BLOCO_RE.search(linhas[j])
            if bm:
                claim = f"B1.MEC.BLOCO{bm.group(1)}.{bm.group(2)}"; break
        antes_anc, antes_claim = v.get("trecho_ancora"), v.get("claim_id")
        v["trecho_ancora"] = frase
        if claim and not str(antes_claim or "").strip():
            v["claim_id"] = claim
        nota(v, {
            "data": HOJE, "regra": "C2/AUD-050",
            "motivo": "âncora apontava para linha-lote do apêndice; re-ancorada na frase de "
                      "prosa que cita nominalmente a referência; claim_id derivado do marcador "
                      "(BLOCOxx.yyy) da subseção que contém a frase.",
            "ancora_anterior": antes_anc, "claim_id_anterior": antes_claim})
        trilha["operacoes"].append({"op": "R-02", "id": vid, "ref": rid,
                                    "claim_id": v.get("claim_id"), "ancora_nova": frase[:120]})
        reanc += 1
    print(f"R-02 (C2) vínculos re-ancorados da linha-lote para prosa: {reanc}/16")
    for vid, rid, por in nao_reanc:
        pend.append(f"C2 · {vid} [{rid}] não re-ancorado automaticamente: {por} — exige olho humano")

    # ============================================================ R-05 (C6)
    Tn = nt(texto)
    frases_texto = []
    for ln in linhas:
        for f in re.split(r"(?<=[.!?])\s+", ln):
            if len(f.strip()) > 30:
                frases_texto.append(ne(f))
    rep_tip = 0
    for v in vinc:
        a = str(v.get("trecho_ancora", "") or "")
        if not a.strip() or ne(a) in ne(texto):
            continue
        if nt(a) not in Tn:
            continue  # deriva lexical: NÃO reparar automaticamente
        alvo = None
        for f in frases_texto:
            if nt(f) == nt(a):
                alvo = f; break
        if alvo is None:
            # Âncora multi-sentença. Corrigido em 2026-09-13: o ramo anterior era
            # CÓDIGO MORTO (break na 1ª iteração, alvo=None sempre) — apontado pela casa.
            # Agora recupera a fatia literal por mapa de posições nt->original.
            alvo = fatia_literal(texto, a)
        if alvo and nt(alvo) == nt(a) and ne(alvo) != ne(a):
            antes = v["trecho_ancora"]
            v["trecho_ancora"] = alvo
            nota(v, {
                "data": HOJE, "regra": "C6/AUD-058",
                "motivo": "deriva TIPOGRÁFICA (markdown/travessão/espaço antes de [TAG]); "
                          "nenhuma palavra alterada; sítio único conferido.",
                "ancora_anterior": antes})
            trilha["operacoes"].append({"op": "R-05", "id": v.get("id_vinculo"),
                                        "de": antes[:90], "para": alvo[:90]})
            rep_tip += 1
    print(f"R-05 (C6) âncoras com deriva tipográfica reparadas: {rep_tip}")

    # ============================================================ R-06 (C5)
    alt = []
    corte_txt = re.search(r"\*\*Corte de literatura:\*\*\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", texto)
    if corte_txt and (man.get("corte_literatura") or {}).get("valor") != corte_txt.group(1):
        antes = man["corte_literatura"]["valor"]
        man["corte_literatura"]["valor"] = corte_txt.group(1)
        alt.append(f"corte_literatura {antes} -> {corte_txt.group(1)}")
    relm = re.search(r"\*\*Mecanismos relacionados \(IDs oficiais\):\*\*\s*(.+)", texto)
    if relm:
        lst = [x.strip() for x in relm.group(1).split(",") if x.strip()]
        if man["semantic_layer"].get("related_entities") != lst:
            antes = len(man["semantic_layer"].get("related_entities") or [])
            man["semantic_layer"]["related_entities"] = lst
            alt.append(f"related_entities {antes} -> {len(lst)}")
    domm = re.search(r"clinical_domains \(máx 4\):\*\*\s*(.+)", texto)
    if domm:
        lst = [x.strip() for x in re.split(r"[·,]", domm.group(1)) if x.strip()]
        if man["semantic_layer"].get("clinical_domains") != lst:
            antes = man["semantic_layer"].get("clinical_domains")
            man["semantic_layer"]["clinical_domains"] = lst
            alt.append(f"clinical_domains {antes} -> {lst}")
    n1 = len(arqs.get("01_pmids.json", []))
    n2 = len(arqs.get("02_meta_analises.json", []))
    n3 = len(arqs.get("03_ensaios_clinicos.json", []))
    subs = {"{P}": str(n1 + n2 + n3), "{MA}": str(n2), "{EC}": str(n3),
            "{T}": str(n1 + n2 + n3), "{N1}": str(n1)}
    blob = json.dumps(man, ensure_ascii=False)
    if any(k in blob for k in subs):
        for k, val in subs.items():
            blob = blob.replace(k, val)
        man = json.loads(blob)
        alt.append("placeholders de template do log R6 resolvidos para os valores reais "
                   f"({n1+n2+n3}/{n2}/{n3}/{n1+n2+n3}/{n1})")
    import hashlib
    sha = hashlib.sha256(canon.read_bytes()).hexdigest()
    if man.get("sha256_canonica_vigente") != sha:
        man["sha256_canonica_vigente"] = sha
        man["sha256_registrado_em"] = HOJE
        alt.append("sha256 da canônica registrado (V-13)")
    man.setdefault("alteracoes", []).append({
        "data": HOJE, "id": "C5-COERENCIA-MANIFESTO",
        "tipo": "sincronizacao_fonte_unica",
        "o_que": "; ".join(alt) if alt else "nenhuma divergência",
        "origem": "re-auditoria Auditor-Mestre 2026-09-13 (AUD-056/057), portão P-8 V-07"})
    print(f"R-06 (C5) manifesto sincronizado: {len(alt)} ajuste(s) — {'; '.join(alt) if alt else 'nada a fazer'}")

    # ============================================================ R-07 (V-10)
    TOKEN = re.compile(r"^[A-Z0-9_]+\[[A-Z]{2,3}\]$")
    n7 = 0
    for e in led:
        cit = str(e.get("citacao_literal", "")).strip()
        if not TOKEN.match(cit):
            continue
        anc = str(e.get("trecho_ancora", "") or "")
        m = re.search(r"\([A-ZÀ-Ú][^()]{2,70}?,\s*\d{4}[a-z]?\)", anc)
        if m:
            antes = e["citacao_literal"]
            e["citacao_literal"] = m.group(0)
            nota(e, {
                "data": HOJE, "regra": "AUD-053/V-10",
                "motivo": "campo continha token de lote, não citação literal; substituído pela "
                          "citação extraída da própria âncora do registro.",
                "valor_anterior": antes})
            n7 += 1
    print(f"R-07 citacao_literal do ledger convertida de token para citação real: {n7}/236")
    pend.append("AUD-053 · registros de ledger cuja âncora não contém citação (Autor, ANO) "
                "seguem com token — verificar caso a caso.")

    # ============================================================ gravação
    if not dry:
        for nome, dados in arqs.items():
            backup(bibdir / nome, dry); salvar(bibdir / nome, dados, dry)
        backup(vpath, dry);  salvar(vpath, vinc, dry)
        backup(lpath, dry);  salvar(lpath, led, dry)
        backup(mpath, dry);  salvar(mpath, man, dry)
        tp = raiz / "producao" / f"15_reparo_coerencia_{HOJE}.json"
        tp.parent.mkdir(exist_ok=True)
        tp.write_text(json.dumps(trilha, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\ntrilha: {tp}")
        print(f"backups: *{TAG}")

    print("\n" + "=" * 74)
    print("PENDÊNCIAS QUE NÃO PODEM SER RESOLVIDAS POR SCRIPT")
    print("=" * 74)
    for p in pend:
        print(" ·", p)
    print(" · C3/AUD-051 · catalogar Osimo 2019 (PMID 31258105) exige rito [AT] "
          "(regra zero-citação-nova na consolidação) — ficha proposta em "
          "PROPOSTA_AT_OSIMO_2019.json; a prosa do §11.1 só muda no próximo [AT].")
    print(" · C4/AUD-052 · BLOCO_11.4: declaração de não-validação e remoção da "
          "circularidade do Critério C exigem decisão do autor científico.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
