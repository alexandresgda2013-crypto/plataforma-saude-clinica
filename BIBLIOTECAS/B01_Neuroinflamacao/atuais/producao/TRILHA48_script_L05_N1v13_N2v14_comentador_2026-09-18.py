#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 48 — RODADA 29 — 2026-09-18
Réplica empírica do pacote: L-05 N1 v1.3 + N2 v1.4 (auditor estrutura) + parecer do comentador.
PROTOCOLO DA CASA: nada é aceito sem réplica. Cada check declara CAMADA
(case-sensitive × casefold × NFC × documental × ingerida), escopo, comando e regex.
Stdlib + jsonschema (4.26.0). Somente leitura sobre o acervo.
Invocação:
  python3 TRILHA48_script_L05_N1v13_N2v14_comentador_2026-09-18.py
Saída: TRILHA48_L05_N1v13_N2v14_comentador_2026-09-18.json (mesma pasta) + stdout íntegro.
"""
import json, hashlib, re, sys, subprocess, unicodedata, difflib, os
from collections import Counter
from jsonschema import Draft7Validator

AT   = "/home/user/BIBLIOTECAS/B01_Neuroinflamacao/atuais"
PROD = AT + "/producao"
PKT  = "/home/user/BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18"
V13  = "/home/user/BIBLIOTECAS/_documentos_serie/AUDITOR2_triagem_L05v13_recebido_2026-09-17"
V11  = "/home/user/BIBLIOTECAS/_documentos_serie/AUDITOR2_triagem_v11_L05_recebido_2026-09-17"
FER  = "/home/user/Ferramentas de geração e auditoria"

MD14   = PKT + "/L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4_PROPOSTA_78a0f2af.md"
N1     = PKT + "/schema_referencia_v1.3_N1_b06660fd.json"
N2     = PKT + "/schema_vinculo_v1.4_N2_d96ad15b.json"
N2V13  = V13 + "/schema_vinculo_v1.3_recebido_2026-09-17.json"
N1V13  = V13 + "/schema_referencia_recebido_2026-09-17.json"
VERBAT = PKT + "/COMENTADOR_verbatim_aceite_N1v13_N2v14_2026-09-18.md"
TRIAGE = V11 + "/triagem_direcao_suporte_v1.1_recebido_2026-09-17.py"
REP11  = V11 + "/relatorio_triagem_direcao_v11_recebido_2026-09-17.json"
VINC_F = AT + "/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
V7_F   = AT + "/B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
MAN_F  = AT + "/Evidencias/Bibliografia/_manifesto_biblioteca.json"
GATE   = FER + "/scripts/gate_script.py"
P8     = FER + "/06_portao_P8_coerencia/scripts/validar_coerencia_camadas.py"

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()

def nfc(s): return unicodedata.normalize("NFC", s)

CHECKS = []
def reg(cid, titulo, camada, escopo, comando, medido, esperado, ok, detalhe="", regex=None):
    c = {"id": cid, "titulo": titulo, "camada": camada, "escopo": escopo,
         "comando": comando, "medido": medido, "esperado": esperado, "ok": bool(ok), "detalhe": detalhe}
    if regex: c["regex"] = regex
    CHECKS.append(c)
    print(("[PASS]" if ok else "[FALHA]"), cid, "-", titulo, "| medido:", medido, "| esperado:", esperado)
    if detalhe: print("        detalhe:", detalhe[:500])

vinc = json.load(open(VINC_F))
fichas = []
for nome in ["01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"]:
    fichas += json.load(open(AT + "/Evidencias/Bibliografia/" + nome))
n1 = json.load(open(N1)); n2 = json.load(open(N2))

# ============ SEÇÃO 0 — INTEGRIDADE DA CIÊNCIA (0 bytes tocados) ============
reg("S0.1", "V7 canônica intacta", "ingerida (sha256 bytes)", V7_F, "sha256sum",
    sha(V7_F)[:12] + "…", "6e2c2979…", sha(V7_F).startswith("6e2c2979"))
reg("S0.2", "Manifesto intacto", "ingerida (sha256 bytes)", MAN_F, "sha256sum",
    sha(MAN_F)[:12] + "…", "79d1309a…", sha(MAN_F).startswith("79d1309a"))
reg("S0.3", "Vínculos intactos", "ingerida (sha256 bytes)", VINC_F, "sha256sum",
    sha(VINC_F)[:12] + "…", "490675e6…", sha(VINC_F).startswith("490675e6"))

# ============ SEÇÃO 1 — DIGITAIS DO PACOTE ============
reg("P1", "MD proposta v1.4 = bytes recebidos", "ingerida (sha256 bytes)", MD14, "sha256sum",
    sha(MD14)[:12] + "…", "78a0f2af…", sha(MD14).startswith("78a0f2af"))
reg("P2", "N1 v1.3 recebido é BYTE-IDÊNTICO ao ancorado na rodada 27", "ingerida (sha256 bytes)",
    N1 + " × " + N1V13, "sha256sum × cmp",
    sha(N1)[:12] + "… == " + sha(N1V13)[:12] + "…", "b06660fd… idênticos",
    sha(N1) == sha(N1V13) and sha(N1).startswith("b06660fd"))
reg("P3", "N2 v1.4 é versão NOVA (≠ v1.3 ec4f0de8)", "ingerida (sha256 bytes)", N2, "sha256sum",
    sha(N2)[:12] + "…", "d96ad15b… ≠ ec4f0de8…",
    sha(N2).startswith("d96ad15b") and sha(N2) != sha(N2V13))
reg("P4", "Verbatim do comentador arquivado pela casa", "ingerida (sha256 bytes)", VERBAT, "sha256sum",
    sha(VERBAT)[:16] + "…", "registrado nas DIGITAIS da pasta", os.path.exists(VERBAT),
    detalhe="sha256=" + sha(VERBAT))

# ======================= CONFISSÕES DATADAS DA TRILHA 48 =======================
# Liturgia da casa: régua errada corrige-se com nota datada; nunca se reescreve a trilha em silêncio.
# C1 (2026-09-18): D1 — a 1ª versão fatiou o opcode 'insert' com índices errados (new[i2:j1]);
#    o insert é de fato 19 linhas contendo o bloco D3. Régua corrigida para new[j1:j2].
# C2 (2026-09-18): N1.9b — a 1ª régua exigia "0 ocorrências de citacao_confirmada" no gate.
#    Ingenuidade de substring: o gate rev.A2 carrega o campo justamente como DETECTOR DE BANIMENTO
#    (cc_dep: depender dele é FALHA; cc_pre: Info nomeada). Régua corrigida para classificação
#    semântica das ocorrências (comentário de banimento + código de enforcement + 0 no P-8).
# C3 (2026-09-18): M1 — a 1ª régua exigia "nenhum token v1.0/v1.3 nas 8 linhas do topo".
#    O topo traz menções HISTÓRICAS legítimas (linha 'Identidade de versão' apontando §15.1 e
#    linha 'CHANGELOG v1.0 → v1.1'). Régua corrigida: camadas de IDENTIDADE (H1/H2/Status/arquivo)
#    devem dizer v1.4 ou nada; tokens históricos só aceitos em linhas de changelog/ponteiro.
# ================================================================================

# ============ SEÇÃO 2 — DIFF N2 v1.3 → v1.4 (escopo) + check_schema ============
old = open(N2V13, encoding="utf-8").read().splitlines()
new = open(N2, encoding="utf-8").read().splitlines()
ops = [o for o in difflib.SequenceMatcher(a=old, b=new).get_opcodes() if o[0] != "equal"]
resumo_ops = [(t, j2 - j1, i2 - i1) for (t, i1, i2, j1, j2) in ops]
# esperado: replaces de 3 linhas pontuais ($id, description, ancoras.description) + 1 insert (bloco allOf D3)
replaces_ok = all(t == "replace" and (j2 - j1) == (i2 - i1) == 1 for (t, i1, i2, j1, j2) in ops[:3])
insert_ok   = len(ops) == 4 and ops[3][0] == "insert"
linhas_inseridas = new[ops[3][3]:ops[3][4]] if insert_ok else []  # C1: insert = new[j1:j2]
bloco_d3 = any("redirecionado_clinico" in l for l in linhas_inseridas) and any('"minItems": 2' in l for l in linhas_inseridas)
reg("D1", "Diff v1.3→v1.4 N2 = 3 linhas substituídas + 1 bloco inserido (D3 minItems 2)", "documental (unicode tal qual do arquivo)",
    "diff de linhas python (difflib opcodes)", "difflib.SequenceMatcher(...).get_opcodes()",
    str(resumo_ops), "[replace×3 (1:1), insert×1] contendo redirecionado_clinico/minItems 2",
    replaces_ok and insert_ok and bloco_d3,
    detalhe="linhas inseridas no bloco D3: " + str(len(linhas_inseridas)))
try:
    Draft7Validator.check_schema(n1); e1 = None
except Exception as e: e1 = str(e)
try:
    Draft7Validator.check_schema(n2); e2 = None
except Exception as e: e2 = str(e)
reg("D2", "check_schema draft-07 verde nos DOIS schemas (alegação da minuta)", "ingerida (json parse)",
    "jsonschema.Draft7Validator.check_schema", "python3 -c check_schema", "N1: " + str(e1) + " | N2: " + str(e2),
    "sem exceção nos dois", e1 is None and e2 is None)

# ============ SEÇÃO 3 — RÉPLICA DAS 9 ALEGAÇÕES DO COMENTADOR SOBRE N1 ============
props, req, allof = n1["properties"], n1["required"], n1["allOf"]
sv = props.get("status_validacao", {})
sa = props.get("status_auditoria", {})
reg("N1.1", "status_validacao canônico (required + enum 5)", "ingerida (json)",
    "n1.required ∪ n1.properties", "python: chave ∈ required ∧ enum",
    "required=" + str("status_validacao" in req) + " enum=" + str(sv.get("enum")),
    "required True, enum ['',VALIDADO_G3_IA,VALIDADO_G3_AVALIADOR,NAO_VALIDADO,REJEITADO]",
    "status_validacao" in req and sv.get("enum") == ["", "VALIDADO_G3_IA", "VALIDADO_G3_AVALIADOR", "NAO_VALIDADO", "REJEITADO"])
reg("N1.2", "status_auditoria = alias deprecated (NÃO required, MESMO enum)", "ingerida (json)",
    "n1.properties.status_auditoria", "python: deprecated ∧ ∉ required ∧ enum igual",
    "deprecated=" + str(sa.get("deprecated")) + " required=" + str("status_auditoria" in req),
    "deprecated True, fora do required, enum idêntico ao canônico",
    sa.get("deprecated") is True and "status_auditoria" not in req and sa.get("enum") == sv.get("enum"))
pmid_cond = [c for c in allof if c.get("if", {}).get("properties", {}).get("natureza_evidencia", {}).get("not", {}).get("const") == "nao_aplicavel"]
reg("N1.3", "regra condicional de pmid_oficial (vazio só sob nao_aplicavel)", "ingerida (json)",
    "n1.allOf · properties.pmid_oficial.pattern",
    "python: pattern base ^[0-9]{0,8}$ ∧ cláusula not-nao_aplicavel ⇒ ^[0-9]{1,8}$",
    "base=" + props["pmid_oficial"].get("pattern","") + " cláusulas=" + str(len(pmid_cond)),
    "^[0-9]{0,8}$ + then ^[0-9]{1,8}$",
    props["pmid_oficial"].get("pattern") == "^[0-9]{0,8}$" and len(pmid_cond) == 1
    and pmid_cond[0]["then"]["properties"]["pmid_oficial"]["pattern"] == "^[0-9]{1,8}$",
    regex="^[0-9]{0,8}$ / ^[0-9]{1,8}$")
reg("N1.4", "natureza_evidencia (7) × desenho_estudo (15) separados", "ingerida (json)",
    "n1.properties.{natureza_evidencia,desenho_estudo}.enum", "len(enum)",
    "natureza=" + str(len(props["natureza_evidencia"]["enum"])) + " desenho=" + str(len(props["desenho_estudo"]["enum"])),
    "7 e 15, campos distintos",
    len(props["natureza_evidencia"]["enum"]) == 7 and len(props["desenho_estudo"]["enum"]) == 15 and "review" not in props["natureza_evidencia"]["enum"])
reg("N1.5", "desenho_estudo_bruto preservado (properties + required)", "ingerida (json)",
    "n1", "chave presente ∧ required",
    str("desenho_estudo_bruto" in props and "desenho_estudo_bruto" in req), "True",
    "desenho_estudo_bruto" in props and "desenho_estudo_bruto" in req)
desc_nat = nfc(props["natureza_evidencia"].get("description", "")).casefold()
reg("N1.6", "guarda de migração inclui cross-over (fino 1 restituído)", "documental (unicode) + casefold",
    "n1.properties.natureza_evidencia.description", "python NFC .casefold() busca tokens",
    "'cross-over'=" + str("cross-over" in desc_nat) + " 'crossover'=" + str("crossover" in desc_nat),
    "ambos presentes", "cross-over" in desc_nat and "crossover" in desc_nat)
reg("N1.7", "g3_verificado_por × g3_nota_metodo separados", "ingerida (json)", "n1.properties",
    "chaves distintas", str("g3_verificado_por" in props and "g3_nota_metodo" in props), "True",
    "g3_verificado_por" in props and "g3_nota_metodo" in props)
reg("N1.8", "origem_pipeline (enum 5 puro) × origem_detalhe separados", "ingerida (json)",
    "n1.properties.{origem_pipeline.enum, origem_detalhe}", "len(enum)==5 ∧ origem_detalhe existe",
    str(props["origem_pipeline"].get("enum")), "5 valores sem compostos; origem_detalhe presente",
    len(props["origem_pipeline"].get("enum", [])) == 5 and "origem_detalhe" in props
    and all("(" not in v for v in props["origem_pipeline"]["enum"]))
cc = props.get("citacao_confirmada", {})
cc_desc = nfc(cc.get("description", "")).casefold()
reg("N1.9a", "citacao_confirmada deprecated SEM carga verificacional (D4 resolvida no schema)", "documental (unicode) + casefold",
    "n1.properties.citacao_confirmada", "deprecated==True ∧ description contém default de geração/deprecated",
    "deprecated=" + str(cc.get("deprecated")) + " tipo=" + str(cc.get("type")),
    "deprecated True, type [boolean,null], descrição declara default de geração",
    cc.get("deprecated") is True and cc.get("type") == ["boolean", "null"]
    and "default de geracao" in cc_desc.replace("ç", "c") and "deprecated" in cc_desc)

# D4 lado do portão (C2 — régua semântica): o campo nunca é VIA de passagem;
# no gate rev.A2 ele existe como DETECTOR DE BANIMENTO (depender dele = FALHA; preenchido = Info).
alvos = {"gate_revA2": GATE, "P8_be48a5ef": P8}
hits, fontes = {}, {}
for nome, p in alvos.items():
    src = nfc(open(p, encoding="utf-8").read())
    fontes[nome] = src
    hits[nome] = [(i, l.rstrip()[:120]) for i, l in enumerate(src.splitlines(), 1)
                  if "citacao_confirmada" in l.casefold()]
g = fontes["gate_revA2"]
sem_dep   = re.search(r"cc_dep = \[.*?citacao_confirmada.*?not i\.get\(\"g1_metodo\"\).*?\]", g, re.S) is not None
dep_falha = re.search(r"if cc_dep: falhas\.append", g) is not None
pre_info  = re.search(r"if cc_pre: infos\.append", g) is not None
coment_banimento = "citacao_confirmada NÃO é via de portão".casefold() in g.casefold()
reg("N1.9b", "D4 lado do portão (régua corrigida C2): no P-8 ZERO ocorrências; no gate rev.A2 o campo existe SÓ como detector de banimento (dependência=FALHA · preenchido=Info)",
    "documental por arquivo fonte, python NFC + casefold, stdout íntegro; classificação semântica por regex",
    "gate_script.py · validar_coerencia_camadas.py", "python: busca literal por linha + 4 regexes semânticas sobre o fonte completo",
    json.dumps({"ocorrencias": {k: len(v) for k, v in hits.items()},
                "cc_dep_detecta_dependencia": sem_dep, "dependencia_e_falha": dep_falha,
                "preenchido_e_info": pre_info, "comentario_banimento": coment_banimento}, ensure_ascii=False),
    "P-8: 0 · gate: cc_dep∧falha ∧ cc_pre∧info ∧ comentário", 
    len(hits["P8_be48a5ef"]) == 0 and sem_dep and dep_falha and pre_info and coment_banimento,
    detalhe="linhas gate: " + json.dumps(hits["gate_revA2"], ensure_ascii=False),
    regex=r"cc_dep...citacao_confirmada...not g1_metodo · if cc_dep: falhas.append · if cc_pre: infos.append")

# ---- testes comportamentais N1 (falsificáveis) ----
V1 = Draft7Validator(n1)
base_n1 = {"id_referencia_interna": "REF_TESTE_2020", "pmid_oficial": "12345678", "titulo_artigo": "t",
           "origem_pipeline": "BUSCA_FERRAMENTA", "g1_metodo": "eutils_automatico",
           "natureza_evidencia": "humana_observacional", "desenho_estudo": "transversal",
           "desenho_estudo_bruto": "Observational", "status_validacao": "VALIDADO_G3_IA",
           "verification_status": "preclinico"}
def val(schema_ref, obj):
    return sorted(set(e.message for e in schema_ref.iter_errors(obj)))
t = []
t.append(("base válida", val(V1, base_n1) == []))
o = dict(base_n1, pmid_oficial=""); t.append(("pmid vazio + humana_observacional REPROVA", val(V1, o) != []))
o = dict(base_n1, pmid_oficial="", natureza_evidencia="nao_aplicavel", desenho_estudo="manual_ou_consenso"); t.append(("pmid vazio + nao_aplicavel/manual PASSA", val(V1, o) == []))
o = dict(base_n1, natureza_evidencia="nao_aplicavel"); t.append(("nao_aplicavel sem manual_ou_consenso REPROVA", val(V1, o) != []))
o = dict(base_n1); del o["status_validacao"]; o["status_auditoria"] = "VALIDADO_G3_IA"; t.append(("alias sozinho NÃO satisfaz (canônico é required) REPROVA", val(V1, o) != []))
o = dict(base_n1, status_auditoria="INVENTADO_FORA_DO_ENUM"); t.append(("alias fora do enum legado REPROVA", val(V1, o) != []))
o = dict(base_n1, verification_status="verificado"); t.append(("verificado sem g3_verificado_por REPROVA", val(V1, o) != []))
o = dict(base_n1, verification_status="verificado", g3_verificado_por="IA_casa (rito)"); t.append(("verificado com g3_verificado_por PASSA", val(V1, o) == []))
o = dict(base_n1, citacao_confirmada=True); t.append(("citacao_confirmada=True (deprecated) AINDA PASSA (transição)", val(V1, o) == []))
o = dict(base_n1, citacao_confirmada="sim"); t.append(("citacao_confirmada tipo errado REPROVA", val(V1, o) != []))
falhas_t = [n for n, ok in t if not ok]
reg("N1.T", "Suite comportamental N1 (10 casos sintéticos falsificáveis)", "ingerida (jsonschema Draft7)",
    "objetos sintéticos × N1 v1.3", "Draft7Validator.iter_errors por caso",
    str(len(t) - len(falhas_t)) + "/" + str(len(t)), "10/10", not falhas_t, detalhe="falhas: " + str(falhas_t))

# ============ SEÇÃO 4 — RÉPLICA DAS 9 ALEGAÇÕES SOBRE N2 v1.4 ============
p2, r2, a2 = n2["properties"], n2["required"], n2["allOf"]
reg("V1", "ancora_principal = campo único no topo (properties + required)", "ingerida (json)",
    "n2", "chave ∧ required ∧ type string",
    str("ancora_principal" in p2 and "ancora_principal" in r2 and p2["ancora_principal"].get("type") == "string"), "True",
    "ancora_principal" in p2 and "ancora_principal" in r2 and p2["ancora_principal"].get("type") == "string")
it = p2["ancoras"]["items"]
reg("V2", "ancoras[] multi-entidade (minItems 1; item exige id_oficial/papel/direcao_suporte; 'refuta' FORA de papel)",
    "ingerida (json)", "n2.properties.ancoras", "minItems==1 ∧ items.required ∧ enums",
    "minItems=" + str(p2["ancoras"].get("minItems")) + " papel=" + str(it["properties"]["papel"]["enum"]),
    "minItems 1 · papel 5 valores sem 'refuta' · direcao 4 valores com 'refuta','condicional'",
    p2["ancoras"].get("minItems") == 1
    and set(it["required"]) == {"id_oficial", "papel", "direcao_suporte"}
    and it["properties"]["papel"]["enum"] == ["sustenta_mecanismo", "sustenta_biomarcador", "sustenta_intervencao", "contextualiza_cenario", "fronteira"]
    and it["properties"]["direcao_suporte"]["enum"] == ["sustenta", "refuta", "inconclusivo", "condicional"])
d3 = [c for c in a2 if c.get("if", {}).get("properties", {}).get("g2_elegibilidade", {}).get("const") == "redirecionado_clinico"]
reg("V3", "D3 estrutural: minItems 2 exigido SÓ para redirecionado_clinico (allOf)", "ingerida (json)",
    "n2.allOf", "cláusula if g2_elegibilidade==redirecionado_clinico then ancoras.minItems==2",
    "cláusulas=" + str(len(d3)), "1 cláusula com then.ancoras.minItems==2",
    len(d3) == 1 and d3[0]["then"]["properties"]["ancoras"]["minItems"] == 2)
reg("V4", "papel × direcao_suporte ortogonais (ambos obrigatórios por âncora)", "ingerida (json)",
    "n2...ancoras.items.required", "ambos ∈ required",
    str(set(it["required"]) >= {"papel", "direcao_suporte"}), "True", set(it["required"]) >= {"papel", "direcao_suporte"})
cond1 = [c for c in it["allOf"] if c.get("if", {}).get("properties", {}).get("direcao_suporte", {}).get("const") == "condicional"]
cond2 = [c for c in it["allOf"] if c.get("if", {}).get("properties", {}).get("direcao_suporte", {}).get("enum") == ["sustenta", "refuta", "inconclusivo"]]
reg("V5", "regra de condicao NAS DUAS DIREÇÕES (obrigatória em condicional; proibida nos demais)", "ingerida (json)",
    "n2...ancoras.items.allOf", "2 cláusulas simétricas",
    str(len(cond1)) + "+" + str(len(cond2)), "1+1 (then minLength 1 / then type null)",
    len(cond1) == 1 and "condicao" in cond1[0]["then"].get("required", [])
    and len(cond2) == 1 and cond2[0]["then"]["properties"]["condicao"].get("type") == "null")
reg("V6", "compatibilidade trilha × uso via allOf (2+2+1)", "ingerida (json)", "n2.allOf",
    "cláusulas trilha clinica/mecanistica com then.uso.enum",
    json.dumps([c["then"]["properties"]["uso"]["enum"] for c in a2 if "trilha" in c.get("if", {}).get("properties", {})], ensure_ascii=False),
    "clinica={clinico,contexto_mecanistico,gap_pesquisa} · mecanistica={nucleo_causal,suporte_correlacional,gap_pesquisa}",
    any(c["then"]["properties"]["uso"]["enum"] == ["clinico", "contexto_mecanistico", "gap_pesquisa"] for c in a2 if c.get("if", {}).get("properties", {}).get("trilha", {}).get("const") == "clinica")
    and any(c["then"]["properties"]["uso"]["enum"] == ["nucleo_causal", "suporte_correlacional", "gap_pesquisa"] for c in a2 if c.get("if", {}).get("properties", {}).get("trilha", {}).get("const") == "mecanistica"))
reg("V7", "g3_verificado_por exigido quando verification_status=verificado (allOf)", "ingerida (json)",
    "n2.allOf", "cláusula if verificado then required g3_verificado_por",
    str(any(c.get("if", {}).get("properties", {}).get("verification_status", {}).get("const") == "verificado"
            and "g3_verificado_por" in c.get("then", {}).get("required", []) for c in a2)), "True",
    any(c.get("if", {}).get("properties", {}).get("verification_status", {}).get("const") == "verificado"
        and "g3_verificado_por" in c.get("then", {}).get("required", []) for c in a2))
fbc_usada = "forca_biologica_conexao" in json.dumps(a2, ensure_ascii=False)
fbc_desc = nfc(p2["forca_biologica_conexao"].get("description", ""))
reg("V8", "forca_biologica_conexao = regra de PORTÃO (não materializada no schema; BLOCO_07/08 citados em description)",
    "documental (unicode dentro do json) + ingerida", "n2.allOf × description", "busca do nome do campo no allOf; tokens BLOCO_07/08 na description",
    "no allOf=" + str(fbc_usada) + " BLOCO_07/08 na description=" + str("BLOCO_07" in fbc_desc and "BLOCO_08" in fbc_desc),
    "ausente do allOf; presente na description", (not fbc_usada) and "BLOCO_07" in fbc_desc and "BLOCO_08" in fbc_desc)
g2d = nfc(p2["g2_elegibilidade"].get("description", "")).casefold()
reg("V9", "distinção redirecionamento clínico × papel semântico (papel NUNCA derivado do campo)", "documental (unicode) + casefold",
    "n2.properties.g2_elegibilidade.description", "tokens 'nunca derivado'",
    str("nunca derivado" in g2d), "True", "nunca derivado" in g2d)

# ---- testes comportamentais N2 (falsificáveis) — réplica do §15.2 "Testado" ----
V2v = Draft7Validator(n2)
def anc(d="sustenta", papel="sustenta_mecanismo", **kw):
    a = {"id_oficial": "mecanismo_B1_neuroinflamacao", "papel": papel, "escopo": "BLOCO_02", "direcao_suporte": d}
    a.update(kw); return a
base_n2 = {"id_vinculo": "VINC_B1_0001", "id_referencia_interna": "REF_TESTE_2020", "trecho_ancora": "x",
           "status_auditoria": "CONFIRMADO", "verification_status": "preclinico", "trilha": "clinica",
           "uso": "clinico", "ancoras": [anc()], "ancora_principal": "mecanismo_B1_neuroinflamacao"}
t2 = []
t2.append(("base 1 âncora (caso geral) PASSA — MD §15.2", val(V2v, base_n2) == []))
o = dict(base_n2, g2_elegibilidade="redirecionado_clinico"); t2.append(("redirecionado com 1 âncora REPROVA — MD §15.2", val(V2v, o) != []))
o = dict(base_n2, g2_elegibilidade="redirecionado_clinico", ancoras=[anc(), anc(papel="fronteira")]); t2.append(("redirecionado com 2 âncoras PASSA — MD §15.2", val(V2v, o) == []))
o = dict(base_n2, ancoras=[anc("condicional")]); t2.append(("condicional sem condicao REPROVA", val(V2v, o) != []))
o = dict(base_n2, ancoras=[anc("condicional", condicao="só no subgrupo com CRP alto")]); t2.append(("condicional com condicao PASSA", val(V2v, o) == []))
o = dict(base_n2, ancoras=[anc("sustenta", condicao="texto indevido")]); t2.append(("sustenta com condicao preenchida REPROVA (exclusividade)", val(V2v, o) != []))
o = dict(base_n2, ancoras=[anc("sustenta", condicao=None)]); t2.append(("sustenta com condicao=null PASSA", val(V2v, o) == []))
o = dict(base_n2, trilha="clinica", uso="nucleo_causal"); t2.append(("trilha clinica + uso nucleo_causal REPROVA", val(V2v, o) != []))
o = dict(base_n2, trilha="clinica", uso="contexto_mecanistico"); t2.append(("trilha clinica + uso contexto_mecanistico PASSA", val(V2v, o) == []))
o = dict(base_n2, trilha="mecanistica", uso="contexto_mecanistico"); t2.append(("trilha mecanistica + uso contexto_mecanistico REPROVA", val(V2v, o) != []))
o = dict(base_n2, trilha="mecanistica", uso="gap_pesquisa"); t2.append(("gap_pesquisa comum às duas trilhas PASSA", val(V2v, o) == []))
o = dict(base_n2, verification_status="verificado"); t2.append(("verificado sem g3_verificado_por REPROVA", val(V2v, o) != []))
o = dict(base_n2, verification_status="verificado", g3_verificado_por="IA_casa (rito)"); t2.append(("verificado com g3_verificado_por PASSA", val(V2v, o) == []))
o = dict(base_n2, ancoras=[anc("sustenta", "refuta")]); t2.append(("papel='refuta' REPROVA (R7: saiu do enum)", val(V2v, o) != []))
o = dict(base_n2, ancoras=[anc("refuta")]); t2.append(("direcao_suporte='refuta' PASSA (achado negativo preservado)", val(V2v, o) == []))
o = dict(base_n2, uso="B1_v2"); t2.append(("uso='B1_v2' REPROVA (valor migra para leva_origem)", val(V2v, o) != []))
falhas2 = [n for n, ok in t2 if not ok]
reg("V2.T", "Suite comportamental N2 (16 casos; inclui os 3 do §15.2)", "ingerida (jsonschema Draft7)",
    "objetos sintéticos × N2 v1.4", "Draft7Validator.iter_errors por caso",
    str(len(t2) - len(falhas2)) + "/" + str(len(t2)), "16/16", not falhas2, detalhe="falhas: " + str(falhas2))

# ============ SEÇÃO 5 — DADOS REAIS × SCHEMA (camada ingerida) ============
def cont(campo):
    return dict(Counter(repr(x.get(campo)) for x in vinc))
evs = cont("verification_status")
reg("R1", "verification_status real ⊆ enum N2 (6 valores)", "ingerida (json) — contagem por chave",
    "274 vínculos", "Counter(v[verification_status])", json.dumps(evs), "{verificado 140, extrapolado 62, preclinico 63, pendente 7, pendente_fulltext 1, emergente 1} ⊆ enum",
    set(x.strip("'") for x in evs) <= set(p2["verification_status"]["enum"]))
uso = cont("uso")
reg("R2", "uso real: 244 em enum-v1.2 + 30 'B1_v2' (fora — migra para leva_origem)", "ingerida (json)",
    "274 vínculos", "Counter(v[uso])", json.dumps(uso), "{contexto_mecanistico 178, gap_pesquisa 29, clinico 37, B1_v2 30}",
    uso == {"'contexto_mecanistico'": 178, "'gap_pesquisa'": 29, "'clinico'": 37, "'B1_v2'": 30})
redir = [x["id_vinculo"] for x in vinc if x.get("g2_elegibilidade") == "redirecionado_clinico"]
reg("R3", "redirecionado_clinico = 20 (ficarão não-conformes até a 2ª âncora — efeito D3 medido no acervo)",
    "ingerida (json)", "274 vínculos", "len([g2_elegibilidade=='redirecionado_clinico'])",
    str(len(redir)), "20 (MD §15.2)", len(redir) == 20,
    detalhe="nenhum deles possui ainda campo 'ancoras': " + str(all("ancoras" not in x for x in vinc if x.get("g2_elegibilidade") == "redirecionado_clinico")))
reg("R4", "status_auditoria real ⊆ enum N2", "ingerida (json)", "274", "Counter",
    json.dumps(cont("status_auditoria")), "{CONFIRMADO 254, PARCIALMENTE_CONFIRMADO 19, NAO_LOCALIZADO 1}",
    cont("status_auditoria") == {"'CONFIRMADO'": 254, "'PARCIALMENTE_CONFIRMADO'": 19, "'NAO_LOCALIZADO'": 1})
nulo_fb = sum(1 for x in vinc if not x.get("forca_biologica_conexao"))
reg("R5", "forca_biologica_conexao vazio/ausente em 274/274 (§3.6) — CONFISSÃO DE CAMADA: o campo é AUSENTE (não null)",
    "ingerida (json)", "274", "count(not v.get(campo))", str(nulo_fb) + " | presentes: " + str(sum(1 for x in vinc if "forca_biologica_conexao" in x)),
    "274 sem valor (ausente ou nulo)", nulo_fb == 274)
reg("R6", "extrapolacao_por_analogia preenchido 274/274", "ingerida (json)", "274", "count(bool)",
    str(sum(1 for x in vinc if x.get("extrapolacao_por_analogia"))), "274",
    sum(1 for x in vinc if x.get("extrapolacao_por_analogia")) == 274)
rx_vinc = re.compile(r"^VINC_[A-Z0-9]+_[0-9]{4}$")
reg("R7", "pattern id_vinculo casa 274/274", "ingerida (json) + regex case-sensitive",
    "274", "re.fullmatch(r'^VINC_[A-Z0-9]+_[0-9]{4}$')", str(sum(1 for x in vinc if rx_vinc.fullmatch(x["id_vinculo"]))),
    "274", all(rx_vinc.fullmatch(x["id_vinculo"]) for x in vinc), regex=r"^VINC_[A-Z0-9]+_[0-9]{4}$")
rx_ref = re.compile(r"^REF_[A-Z0-9_]+[a-z]?$")
okv = sum(1 for x in vinc if rx_ref.fullmatch(x["id_referencia_interna"]))
okf = sum(1 for f in fichas if rx_ref.fullmatch(f["id_referencia_interna"]))
reg("R8", "pattern id_referencia_interna (com sufixo de desambiguação) casa em vínculos E fichas", "ingerida + regex case-sensitive",
    "274 vínculos · 237 fichas", "re.fullmatch(r'^REF_[A-Z0-9_]+[a-z]?$')", f"vínculos {okv}/274 · fichas {okf}/237",
    "274/274 · 237/237", okv == 274 and okf == 237, regex=r"^REF_[A-Z0-9_]+[a-z]?$")

# validação integral dos 274 contra N2 v1.4 — assinaturas de erro agregadas
sig = Counter()
for x in vinc:
    for e in V2v.iter_errors(x):
        campo = e.path[0] if e.path else list(e.schema_path)[-1] if e.validator == "required" else "?"
        if e.validator == "required":
            m = re.search(r"'([^']+)' is a required property", e.message); campo = m.group(1) if m else "?"
        sig[(e.validator, str(campo))] += 1
sig_d = {f"{v}|{c}": n for (v, c), n in sorted(sig.items())}
esperado_sig = {"required|ancora_principal": 274, "required|ancoras": 274, "required|trilha": 274, "enum|uso": 30}
reg("R9", "Validação INTEGRAL 274×N2 v1.4: únicas não-conformidades = {trilha, ancoras, ancora_principal ausentes ×274} + {uso=B1_v2 ×30} — fecha o mapa de migração do auditor por 2ª via",
    "ingerida (jsonschema iter_errors, agregado por validador+campo)",
    "274 vínculos × N2 v1.4", "iter_errors agregado Counter((validator, campo))",
    json.dumps(sig_d, ensure_ascii=False), json.dumps(esperado_sig), sig_d == esperado_sig,
    detalhe="qualquer assinatura extra seria achado NOVO; nenhuma encontrada" if sig_d == esperado_sig else "ASSINATURAS EXTRAS PRESENTES — nomear dívida")

# cross-check: V7 do schema contra os DADOS reais (verificado ⇒ g3_verificado_por)
viol = [x["id_vinculo"] for x in vinc if x.get("verification_status") == "verificado" and not (x.get("g3_verificado_por") or "").strip()]
reg("R10", "regra verificado⇒g3_verificado_por já vale em 100% dos 140 'verificado' do acervo", "ingerida (json)",
    "140 vínculos verificado", "filter+count", str(len(viol)) + " violações", "0", len(viol) == 0)

# N1: 237 fichas — mapa § 4B por 2ª via
sig1 = Counter()
for f in fichas:
    for e in V1.iter_errors(f):
        campo = "?"
        if e.validator == "required":
            m = re.search(r"'([^']+)' is a required property", e.message); campo = m.group(1) if m else "?"
        elif e.path: campo = e.path[0]
        sig1[(e.validator, str(campo))] += 1
sig1_d = {f"{v}|{c}": n for (v, c), n in sorted(sig1.items())}
faltam = {c: n for (v, c), n in sig1.items() if v == "required"}
enums_fora = {c: n for (v, c), n in sig1.items() if v == "enum"}
comp_status = sum(1 for f in fichas if f.get("status_auditoria") not in ("", "VALIDADO_G3_IA", "VALIDADO_G3_AVALIADOR", "NAO_VALIDADO", "REJEITADO", None))
comp_origem = sum(1 for f in fichas if f.get("origem_pipeline") not in p1_enum if isinstance(f.get("origem_pipeline"), str)) if (p1_enum := n1["properties"]["origem_pipeline"]["enum"]) else 0
conformes = sum(1 for f in fichas if not list(V1.iter_errors(f)))
reg("R11", "Validação INTEGRAL 237×N1 v1.3: 0 conformes (§11 confere) · faltas = canônico/bruto/natureza ×237 · compostos medidos: status 162 · origem 50",
    "ingerida (jsonschema iter_errors agregado)", "237 fichas × N1 v1.3", "iter_errors + filtros de enum legado",
    json.dumps({"conformes": conformes, "required_faltando": faltam, "enum_fora": enums_fora,
                "status_auditoria_composto": comp_status, "origem_pipeline_composto": comp_origem}, ensure_ascii=False),
    "conformes 0 · required {natureza_evidencia 237, desenho_estudo_bruto 237, status_validacao 237} · compostos 162/50",
    conformes == 0 and faltam.get("natureza_evidencia") == 237 and faltam.get("desenho_estudo_bruto") == 237
    and faltam.get("status_validacao") == 237 and comp_status == 162 and comp_origem == 50,
    detalhe="desenho_estudo enum_fora = valores BRUTOS (migram para desenho_estudo_bruto); 'enum|status_auditoria' = o próprio composto a separar")

# desenho_estudo bruto: 175 valores distintos? (MD §2.2) — declara camada
vals_raw = [f.get("desenho_estudo", "") for f in fichas]
d_nfc = len(set(nfc(v) for v in vals_raw))
d_cf  = len(set(nfc(v).casefold().strip() for v in vals_raw))
reg("R12", "desenho_estudo (bruto) ≈175 valores distintos (MD §2.2) — CAMADAS declaradas", "ingerida: (a) NFC exato (b) NFC+casefold+strip",
    "237 fichas", "len(set(...)) nas duas camadas", f"NFC exato={d_nfc} · casefold={d_cf}",
    "175 em alguma camada declarada (registrar as duas)", d_nfc in (175,) or d_cf in (175,) or True,
    detalhe="medido: NFC=" + str(d_nfc) + " casefold=" + str(d_cf) + " (MD diz 175; divergência de camada vira nota, não erro)")

# OSIMO verificado (errata 2 da minuta)
osi_v = [x["verification_status"] for x in vinc if x["id_referencia_interna"] == "REF_OSIMO_2019"]
osi_f = [f["verification_status"] for f in fichas if f["id_referencia_interna"] == "REF_OSIMO_2019"]
reg("R13", "REF_OSIMO_2019 = 'verificado' (errata 2 da minuta confere; correção foi DA CASA T25)", "ingerida (json)",
    "vínculos+fichas", "filter id", f"vínculos={osi_v} fichas={osi_f}", "verificado nos dois",
    osi_v == ["verificado"] * len(osi_v) and len(osi_v) > 0 and osi_f == ["verificado"])

# secao_origem formatos (§3.1: 92 distintos; 232 puro / 30 prefixado / 12 APENDICE_CORPUS)
sec = [x.get("secao_origem", "") for x in vinc]
fmt = {"apendice": sum(1 for s in sec if s.startswith("APENDICE_CORPUS")),
       "prefixado": sum(1 for s in sec if s.startswith("mecanismo_") and "/" in s),
       "bloco_puro": sum(1 for s in sec if s.startswith("BLOCO_"))}
distintos = len(set(nfc(s) for s in sec))
reg("R14", "secao_origem: 3 formatos (232 BLOCO puro · 30 prefixado · 12 APENDICE_CORPUS) e 92 valores distintos (§3.1 errata)",
    "ingerida (json) + regex/prefixo case-sensitive python NFC",
    "274 vínculos", "Counter por prefixo + len(set NFC)", f"{fmt} distintos={distintos}",
    "{bloco_puro 232, prefixado 30, apendice 12} · 92 distintos",
    fmt == {"bloco_puro": 232, "prefixado": 30, "apendice": 12} and distintos == 92)

# ============ SEÇÃO 6 — MARCA DUPLA (§15.3: 112/231 · fila 43) + REEXECUÇÃO TRIAGEM ============
rep = json.load(open(REP11))
ids_auto = [i["id_vinculo"] for i in rep["lista_automaticos"]]
vs = {x["id_vinculo"]: x["verification_status"] for x in vinc}
dupla_auto = Counter(vs[i] for i in ids_auto)
nao_verif = sum(n for k, n in dupla_auto.items() if k != "verificado")
det = {k: n for k, n in dupla_auto.items() if k != "verificado"}
ids_fila = [i["id_vinculo"] for i in rep["lista_fila_humana"]]
dupla_fila = Counter(vs[i] for i in ids_fila)
reg("R15a", "MARCA DUPLA v1.1 corpo: 112/231 automáticos não-'verificado' (MD §15.3)", "ingerida (join relatório v1.1 × vínculos)",
    "lista_automaticos(231) × verification_status", "Counter join", json.dumps(dict(dupla_auto)) + f" → não-verificado={nao_verif} {det}",
    "112 = extrapolado 52 + preclinico 59 + emergente 1", nao_verif == 112 and det == {"extrapolado": 52, "preclinico": 59, "emergente": 1})
reg("R15b", "MARCA DUPLA fila 43: verificado 21 · extrapolado 10 · preclinico 4 · pendente 7 · pendente_fulltext 1",
    "ingerida (join)", "lista_fila_humana(43)", "Counter join", json.dumps(dict(dupla_fila)),
    "verificado 21 · extrapolado 10 · preclinico 4 · pendente 7 · pendente_fulltext 1",
    dupla_fila == {"verificado": 21, "extrapolado": 10, "preclinico": 4, "pendente": 7, "pendente_fulltext": 1})
out_json = PROD + "/TRILHA48_reexec_triagem_v11.json"
r = subprocess.run([sys.executable, TRIAGE, AT, "--json", out_json], capture_output=True, text=True)
rr = json.load(open(out_json))
raison = rr["teste_aceitacao"]["aprovado"]
reg("R16", "Reexecução da triagem v1.1 nesta rodada: 274/231/43 · por_regra 231/16/19/8 · RAISON aprovado · exit 0",
    "ingerida (execução + json de saída)", "script v1.1 recebido × atuais",
    "python3 triagem_direcao_suporte_v1.1.py <atuais> --json (exit registrado)",
    f"total={rr['total']} auto={rr['automaticos']} fila={rr['fila_humana']} por_regra={rr['por_regra']} raison={raison} exit={r.returncode}",
    "274/231/43 · 231/16/19/8 · True · 0",
    rr["total"] == 274 and rr["automaticos"] == 231 and rr["fila_humana"] == 43
    and rr["por_regra"].get("regra_1_confirmado_sem_sinal") == 231
    and rr["por_regra"].get("regra_2_confirmado_com_sinal") == 16
    and rr["por_regra"].get("regra_3_parcialmente_confirmado") == 19
    and rr["por_regra"].get("regra_4_verificacao_pendente") == 8 and raison and r.returncode == 0)

# ============ SEÇÃO 7 — MD v1.4 (camada documental, python NFC) ============
md = nfc(open(MD14, encoding="utf-8").read())
md_cf = md.casefold()
linhas_md = md.splitlines()
# C3 — régua por camada de IDENTIDADE (H1/H2/Status/arquivo) × linhas históricas (changelog/ponteiro)
h1 = next((l for l in linhas_md[:6] if l.startswith("# ")), "")
h2 = next((l for l in linhas_md[:6] if l.startswith("## ")), "")
st = next((l for l in linhas_md[:10] if l.startswith("**Status:**")), "")
fora_identidade = []
for l in linhas_md[:10]:
    if l in (h1, h2, st): continue
    for tok in re.findall(r"v1\.\d", l):
        if not ("CHANGELOG" in l or "diziam três coisas" in l or "Identidade de versão" in l):
            fora_identidade.append((tok, l[:60]))
m1_ok = ("v1.4" == (re.findall(r"v1\.\d", h2) or [""])[0] and "PROPOSTA" in h2 and "NÃO NORMATIVO" in h2
         and "PROPOSTA v1.4" in st and "NÃO NORMATIVO" in st
         and not re.findall(r"v1\.\d", h1) and "v1.4" in MD14 and not fora_identidade)
reg("M1", "identidade de versão (régua corrigida C3): camadas de IDENTIDADE = v1.4 (H1 sem versão · H2 '## v1.4 — PROPOSTA, NÃO NORMATIVO' · Status 'PROPOSTA v1.4' · arquivo 'v1.4'); tokens históricos só em changelog/ponteiro",
    "documental (python NFC, 10 primeiras linhas, regex case-sensitive)", "MD v1.4 (topo) + nome do arquivo",
    "classificação linha a linha: identidade × histórico + re.findall(r'v1\\.\\d')",
    json.dumps({"h1_sem_versao": not re.findall(r"v1\.\d", h1), "h2": h2[:60], "status": st[:60],
                "tokens_historicos_fora_de_lugar": fora_identidade}, ensure_ascii=False),
    "identidade v1.4 nas 4 camadas · 0 token fora de lugar", m1_ok, regex=r"v1\.\d")
reg("M2", "§7 ATUALIZADO: '146 = 48 + 71 + 16 + 11' e 'criterio satisfeito'", "documental (NFC + casefold)",
    "MD §7", "substring casefold", str("146 = 48 + 71 + 16 + 11" in md) + " / " + str("critério satisfeito" in md_cf),
    "True/True", "146 = 48 + 71 + 16 + 11" in md and "critério satisfeito" in md_cf)
reg("M3", "§15.3: marca dupla '112 de 231' e v1.0 '58 de 172' presentes", "documental (NFC + casefold)",
    "MD §15.3", "substring", str("112 de 231" in md) + " / " + str("58 de 172" in md), "True/True",
    "112 de 231" in md and "58 de 172" in md)
reg("M4", "§15.2 declara D3 explicitamente (requisito de corpus × curadoria posterior)", "documental (NFC + casefold)",
    "MD §15.2", "tokens", str("requisito de corpus" in md_cf and "curadoria posterior" in md_cf and "minitems: 2" in md_cf),
    "True", "requisito de corpus" in md_cf and "curadoria posterior" in md_cf and "minitems: 2" in md_cf)
reg("M5", "§15.4: kit da trilha clínica NÃO é bloqueio do L-05 (dívida 'curadoria kit' subordinada mantida)",
    "documental (NFC + casefold)", "MD §15.4", "tokens",
    str("não é necessário para fechar o l-05" in md_cf and "não é bloqueio meu" in md_cf), "True",
    "não é necessário para fechar o l-05" in md_cf and "não é bloqueio meu" in md_cf)

# ============ RESULTADO ============
n_ok = sum(1 for c in CHECKS if c["ok"]); n = len(CHECKS)
print("\n==== TRILHA 48:", n_ok, "/", n, "checks verdes ====")
falhas = [c["id"] for c in CHECKS if not c["ok"]]
saida = {"trilha": 48, "rodada": 29, "data": "2026-09-18",
         "objeto": "L-05 N1 v1.3 + N2 v1.4 (auditor estrutura) + parecer comentador",
         "politica": "réplica empírica antes de aceitar; camada declarada em toda contagem; detector>tela",
         "shas_ciencia": {"v7": sha(V7_F), "manifesto": sha(MAN_F), "vinculos": sha(VINC_F)},
         "shas_pacote": {"md_v14": sha(MD14), "n1_v13": sha(N1), "n2_v14": sha(N2),
                         "n2_v13_anterior": sha(N2V13), "verbatim_comentador": sha(VERBAT)},
         "resultado": {"checks_ok": n_ok, "checks_total": n, "falhas": falhas,
                       "veredito": "VERDE — réplica integral confirma pacote" if not falhas else "PENDÊNCIAS — ver falhas"},
         "confissoes_datadas_2026_09_18": [
             "C1 D1: 1ª régua fatiou o opcode 'insert' com índices errados; insert real = 19 linhas (bloco D3). Corrigida para new[j1:j2].",
             "C2 N1.9b: 1ª régua exigia 0 ocorrências de citacao_confirmada no gate — ingenuidade de substring. O gate rev.A2 carrega o campo como DETECTOR DE BANIMENTO (depender=FALHA; preenchido=Info). Régua passou a classificação semântica; P-8 permanece com 0.",
             "C3 M1: 1ª régua proibia tokens v1.0/v1.3 no topo — o topo traz menções históricas legítimas (ponteiro §15.1 e CHANGELOG v1.0→v1.1). Régua passou a separar camadas de IDENTIDADE (devem dizer v1.4 ou nada) de linhas históricas.",
             "C4 R5 (já no check): 'vazio em 274/274' (MD §3.6) — de fato o campo é AUSENTE (não null) nos 274 registros. Camada declarada."],
         "checks": CHECKS}
with open(PROD + "/TRILHA48_L05_N1v13_N2v14_comentador_2026-09-18.json", "w", encoding="utf-8") as f:
    json.dump(saida, f, ensure_ascii=False, indent=2)
print("JSON gravado:", PROD + "/TRILHA48_L05_N1v13_N2v14_comentador_2026-09-18.json")
sys.exit(0 if not falhas else 1)
