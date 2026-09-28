#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 25 — Réplica da proposta L-05 (auditor de estrutura, 2026-09-14)
Objeto: L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.0_PROPOSTA.md + 2 JSON Schemas (uploads).
Método: medir cada número que a proposta DECLARA ter medido, contra o acervo real B1 V7,
e validar os 237 registros + 274 vínculos contra os 2 schemas (mini-validador draft-07 subset).
Read-only: não toca artefato nenhum.
"""
import json, re, os, collections

HOME = "/home/user"
UP = os.path.join(HOME, "uploads")
AT = os.path.join(HOME, "BIBLIOTECAS/B01_Neuroinflamacao/atuais")
FER = os.path.join(HOME, "Ferramentas de geração e auditoria")

SCH_REF = json.load(open(os.path.join(UP, "schema_referencia_v1.json"), encoding="utf-8"))
SCH_VIN = json.load(open(os.path.join(UP, "schema_vinculo_v1.json"), encoding="utf-8"))
refs = []
for f in ["01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"]:
    d = json.load(open(os.path.join(AT, "Evidencias/Bibliografia", f), encoding="utf-8"))
    refs += [(f, x) for x in (d if isinstance(d, list) else [])]
VIN = json.load(open(os.path.join(AT, "Evidencias/Vinculos/vinculos_referencia_afirmacao.json"), encoding="utf-8"))
vincs = VIN if isinstance(VIN, list) else VIN.get("vinculos", [])

def dist(vals):
    c = collections.Counter(vals)
    return dict(sorted(c.items(), key=lambda kv: -kv[1]))

out = {"trilha": "25_replicacao_L05_auditor_estrutura_2026-09-14", "alvos": {}}

# ---------- A) réplica dos números da proposta ----------
# A1. uso: enum PROMPT v4.2 (trilha clínica) vs v3.1
ENUM_CLIN = {"clinico", "contexto_mecanistico", "gap_pesquisa"}
ENUM_MEC = {"nucleo_causal", "suporte_correlacional", "gap_pesquisa"}
uso = [v.get("uso", "∅") for v in vincs]
em_clin = sum(1 for u in uso if u in ENUM_CLIN)
out["alvos"]["A1_uso"] = {
    "distribuicao": dist(uso),
    "no_enum_clinico_PROMPTv4.2": f"{em_clin}/{len(uso)}",
    "proposta_disse": "244/274 conformam v1.2; 30 = B1_v2",
}

# A2. os 30 B1_v2 ↔ secao_origem das FICHAS terminando em /v2
ids_refs_b1v2 = {v.get("id_referencia_interna") for v in vincs if v.get("uso") == "B1_v2"}
sec = {x.get("id_referencia_interna"): (x.get("secao_origem") or "") for _, x in refs}
refs_v2 = {i for i, s in sec.items() if s.rstrip().lower().endswith("/v2") or "/v2" in s.lower()}
out["alvos"]["A2_B1v2_x_secao_v2"] = {
    "vinculos_com_uso_B1v2": len(ids_refs_b1v2),
    "fichas_com_secao_v2": len(refs_v2),
    "intersecao": len(ids_refs_b1v2 & refs_v2),
    "so_em_vinculos": sorted(ids_refs_b1v2 - refs_v2)[:10],
    "so_em_fichas": sorted(refs_v2 - ids_refs_b1v2)[:10],
    "proposta_disse": "mesmos 30; B1_v2 é etiqueta de leva vazada para 'uso'",
}

# A3. evid_role nas fichas (a proposta chama de natureza? medir os dois candidatos)
ev = [x.get("evid_role", "∅") for _, x in refs]
out["alvos"]["A3_evid_role_fichas"] = {"dist": dist(ev),
    "proposta_disse": "human_clinical 66, human_experimental 6, post_mortem 2, preclinical_mechanistic 133, review 30"}

# A4. 175 valores distintos de desenho_estudo
des = [x.get("desenho_estudo", "∅") for _, x in refs]
out["alvos"]["A4_desenho_bruto"] = {"distintos": len(set(des)), "proposta_disse": "175 distintos em 237"}

# A5. secao_origem dos vínculos: proposta disse 21 distintos/100% B1 — rev.1: medir tb. o FORMATO
so = [v.get("secao_origem", "∅") for v in vincs]
doms = {s.split("/")[0] for s in so}
fmt = collections.Counter()
for s in so:
    if s.startswith("mecanismo_"):
        fmt["com_prefixo_mecanismo"] += 1
    elif s.startswith("BLOCO_"):
        fmt["BLOCO_puro_sem_prefixo"] += 1
    elif s.startswith("APENDICE"):
        fmt["APENDICE_CORPUS"] += 1
    else:
        fmt["outro"] += 1
out["alvos"]["A5_secao_origem_vinculos"] = {"distintos": len(set(so)), "dominios": sorted(doms),
    "formatos_rev1": dict(fmt),
    "proposta_disse": "21 valores, 100% B1",
    "rev1_conclusao": ("literalmente impreciso (medido 92, não 21) mas a TESE QUALITATIVA confirma: 0 âncoras "
                       "fora da B1 (todos BLOCO_* dela, prefixados ou não, + 12 'APENDICE_CORPUS' = selos de índice). "
                       "Derivação da âncora principal exige normalização de prefixo + tratamento nomeado dos 12 de índice.")}

# A6. g2_elegibilidade
g2 = [v.get("g2_elegibilidade", "∅") for v in vincs]
out["alvos"]["A6_g2"] = {"dist": dist(g2), "proposta_disse": "20 redirecionado_clinico"}

# A7. status_auditoria nível 1 (fichas): VALIDADO_G3_IA 165? compostos 162?
sa1 = [x.get("status_auditoria", "∅") for _, x in refs]
comp1 = [s for s in sa1 if isinstance(s, str) and ("(" in s or "," in s or " - " in s.lower())]
out["alvos"]["A7_status_nivel1"] = {"dist": dist([s.split(" (")[0] for s in sa1]),
    "compostos_ou_com_texto_extra": len(comp1),
    "proposta_disse": "VALIDADO_G3_IA 165; 162 a separar (veredito×ressalva)"}

# A8. origem_pipeline compostos = 50?
op = [x.get("origem_pipeline", "∅") for _, x in refs]
comp_op = [s for s in op if isinstance(s, str) and ("(" in s or "," in s or re.search(r"\d{4}-\d{2}-\d{2}", s))]
out["alvos"]["A8_origem_pipeline"] = {"dist": dist([s.split(" (")[0].split(",")[0] for s in op]),
    "compostos": len(comp_op), "proposta_disse": "50 a separar"}

# A9. verification_status inválido nas fichas = 1?
ENUM_VS = {"verificado", "preclinico", "extrapolado", "emergente", "pendente", "pendente_fulltext"}
vs = [(x.get("id_referencia_interna"), x.get("verification_status", "∅")) for _, x in refs]
inv = [p for p in vs if p[1] not in ENUM_VS]
out["alvos"]["A9_verification_status"] = {"dist": dist([b for _, b in vs]), "invalidos": inv,
    "proposta_disse": "1 inválido = dívida full-text já nomeada P-6",
    "rev1_marcacao": ("A contagem 1 batia; a IDENTIDADE não: o inválido era REF_OSIMO_2019 com valor-livre "
                      "'confimado_G1_G3_2026-09-13' (typo da casa, rodada C3) — CORRIGIDO para 'verificado' nesta "
                      "rodada (02_meta_analises + manifesto 2.10, backup em antigos/historico/). Após a errata, "
                      "inv deve sair = [] e pendente_fulltext das fichas = 0 (a dívida full-text é dos VÍNCULOS).")}

# A10. forca_biologica_conexao vazio 274/274 (re-medido)
fb = [v.get("forca_biologica_conexao") for v in vincs]
out["alvos"]["A10_forca_biologica"] = {"vazios": sum(1 for x in fb if x in (None, "", "∅")), "total": len(fb)}

# A11. catálogo de IDs oficiais (extraído do MD; _ids_oficiais.json NÃO existe como arquivo)
md = open(os.path.join(FER, "01_norteadores/1º IDS_OFICIAIS.md"), encoding="utf-8").read()
ids = set(re.findall(r'"((?:mecanismo|exame|cenario|suplemento)_[A-Za-z0-9_À-ÿ]+)"', md))
out["alvos"]["A11_catalogo_ids"] = {"arquivo_json_existe": False,
    "fonte": "01_norteadores/1º IDS_OFICIAIS.md (blocos JSON embutidos)",
    "ids_parseados": len(ids),
    "presentes": {k: (k in ids) for k in ["mecanismo_B1_neuroinflamacao", "exame_il6", "cenario_E5"]}}

# ---------- B) mini-validador draft-07 subset ----------
def validate(inst, sch, path="$"):
    errs = []
    t = sch.get("type")
    def isinst(x, tt):
        return {"string": isinstance(x, str), "array": isinstance(x, list),
                "object": isinstance(x, dict), "boolean": isinstance(x, bool),
                "null": x is None,
                "number": isinstance(x, (int, float)) and not isinstance(x, bool)}[tt]
    if t is not None:
        ok = any(isinst(inst, tt) for tt in (t if isinstance(t, list) else [t]))
        if not ok:
            return [f"{path}: tipo {type(inst).__name__} ∉ {t}"]
    if "enum" in sch and inst not in sch["enum"]:
        errs.append(f"{path}: valor {inst!r} fora do enum {sch['enum']}")
    if isinstance(inst, str):
        if "minLength" in sch and len(inst) < sch["minLength"]:
            errs.append(f"{path}: vazio/curto demais")
        if "pattern" in sch and not re.search(sch["pattern"], inst):
            errs.append(f"{path}: '{inst}' não casa {sch['pattern']}")
        if "const" in sch and inst != sch["const"]:
            errs.append(f"{path}: const {sch['const']} ≠ '{inst}'")
    if "not" in sch and not validate_not(inst, sch["not"]):
        errs.append(f"{path}: viola restrição NOT {sch['not']}")
    if isinstance(inst, list):
        if "minItems" in sch and len(inst) < sch["minItems"]:
            errs.append(f"{path}: menos de {sch['minItems']} itens")
        if "items" in sch and isinstance(sch["items"], dict):
            for i, x in enumerate(inst):
                errs += validate(x, sch["items"], f"{path}[{i}]")
    if isinstance(inst, dict):
        for r in sch.get("required", []):
            if r not in inst:
                errs.append(f"{path}.{r}: AUSENTE (required)")
        for k, sub in sch.get("properties", {}).items():
            if k in inst:
                errs += validate(inst[k], sub, f"{path}.{k}")
    return errs

def validate_not(inst, notsch):
    matched = True
    if "pattern" in notsch:
        matched = isinstance(inst, str) and re.search(notsch["pattern"], inst) is not None
    if "const" in notsch:
        matched = inst == notsch["const"]
    if "enum" in notsch:
        matched = inst in notsch["enum"]
    return not matched

def validate_allOf(inst, sch):
    errs = validate(inst, sch)
    for sub in sch.get("allOf", []):
        cond = sub.get("if"); then = sub.get("then")
        if cond is None: continue
        ok = True
        for k, kv in cond.get("properties", {}).items():
            if k not in inst or ("const" in kv and inst[k] != kv["const"]):
                ok = False; break
        for r in cond.get("required", []):
            if r not in inst: ok = False
        if ok and then:
            merged = {**then}
            errs += validate(inst, merged, "$")
    return errs

def avaliar(registros, sch, nome_campos_novos):
    stats = collections.Counter(); exemplos = {}
    for rid, x in registros:
        errs = validate_allOf(x, sch)
        for e in errs:
            campo = re.sub(r"^\$\.?(\[?\w*\]?)\..*$", r"\1", e.split(":")[0])
            chave = e.split(":")[0]
            stats[chave] += 1
            exemplos.setdefault(chave, (rid, e[:90]))
    return dict(stats), exemplos

# fichas: medir violações IGNORANDO os campos novos (que obviamente não existem ainda)
CAMPOS_NOVOS_REF = {"natureza_evidencia", "desenho_estudo_bruto", "origem_detalhe",
                    "status_auditoria_nota", "leva_origem", "forca_evidencia_afirmacao"}
def avaliar_refs():
    stats = collections.Counter(); exemplos = {}
    for f, x in refs:
        rid = x.get("id_referencia_interna", "?")
        errs = validate_allOf(x, SCH_REF)
        for e in errs:
            campo = e.split(":")[0].replace("$.", "")
            base = campo.split(".")[0].split("[")[0]
            if base in CAMPOS_NOVOS_REF:
                continue  # esperado: campos novos da proposta
            stats[campo] += 1
            exemplos.setdefault(campo, (rid, e[:110]))
    return dict(stats), exemplos

# desenho_estudo existe nas fichas? (schema exige enum; hoje é texto livre)
out["alvos"]["B0_campo_desenho_hoje_enum?"] = {
    "fichas_com_desenho_no_enum_proposto": sum(1 for _, x in refs if x.get("desenho_estudo") in SCH_REF["properties"]["desenho_estudo"]["enum"]),
    "total": len(refs)}

stats_ref, ex_ref = avaliar_refs()
out["B_validacao_237_refs_contra_schema"] = {"violacoes_fora_campos_novos": stats_ref, "exemplos": ex_ref}

# vínculos: simular migração mínima (derivar ancoras+trilha) e medir o que ainda falha
CAMPOS_NOVOS_VIN = {"ancoras", "trilha"}
def sim_migracao(v):
    m = dict(v)
    so = v.get("secao_origem") or ""
    # rev.1: a casa mediu 3 formatos; a âncora principal é SEMPRE o mecanismo B1
    # (secao_origem só aponta para B1 — tese qualitativa da proposta confirmada);
    # escopo = o BLOCO/suBLOCO; os 12 'APENDICE_CORPUS' ficam como exceção nomeada (escopo).
    if so.startswith("mecanismo_B1_neuroinflamacao"):
        esc = so.split("/", 1)[1] if "/" in so else None
    else:
        esc = so or None
    m["ancoras"] = [{"id_oficial": "mecanismo_B1_neuroinflamacao", "papel": "sustenta_mecanismo",
                     "escopo": esc, "principal": True}]
    m["trilha"] = "clinica" if v.get("uso") in ENUM_CLIN else ("mecanistica" if v.get("uso") in ENUM_MEC else "clinica")
    if v.get("uso") == "B1_v2":
        m["leva_origem"] = "B1_v2"  # e 'uso' ficaria para curadoria — aqui mantemos B1_v2 p/ medir
    return m

viol_vin = collections.Counter(); ex_vin = {}; id_fora_catalogo = []
for v in vincs:
    m = sim_migracao(v)
    errs = validate_allOf(m, SCH_VIN)
    for a in m["ancoras"]:
        if a["id_oficial"] not in ids:
            id_fora_catalogo.append((v.get("id_vinculo"), a["id_oficial"]))
    for e in errs:
        campo = e.split(":")[0].replace("$.", "")
        viol_vin[campo] += 1
        ex_vin.setdefault(campo, (v.get("id_vinculo"), e[:110]))
out["C_validacao_274_vinculos_pós-migracao-minima"] = {"violacoes": dict(viol_vin), "exemplos": ex_vin,
    "id_oficial_fora_do_catalogo": id_fora_catalogo}
# entre os B1_v2: quantos seriam o único ponto restante
out["C_validacao_274_vinculos_pós-migracao-minima"]["nota"] = "B1_v2 falha o enum 'uso' até curadoria — esperado e já mapeado (30)."

# E2/allOf nos dados atuais (fichas verificado⇒g3 sem ferramenta)
e2 = []
for f, x in refs:
    if x.get("verification_status") == "verificado":
        g3 = str(x.get("g3_verificado_por", ""))
        if not g3 or re.search(r"(?i)(eutils|script|retrofit)", g3):
            e2.append(x.get("id_referencia_interna"))
out["D_E2_referencias_verificado_sem_avaliador"] = e2

# invariante não-expressável: exatamente-1 principal (informação para o parecer)
out["E_invariante_principal"] = {"expressavel_no_schema_entregue": False,
    "motivo": "minItems=1 garante >=1 âncora; nada força exatamente-1 principal:true (JSON Schema draft-07 não conta ocorrências por valor). Cobertura: portão imperativo."}

p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "25_replicacao_L05_auditor_estrutura_2026-09-14.json")
json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for k, v in out.items():
    if isinstance(v, dict) and len(json.dumps(v, ensure_ascii=False)) < 900:
        print(k, "=>", json.dumps(v, ensure_ascii=False)[:900])
    else:
        print(k, "=> (ver JSON)")
print("gravado:", p)
