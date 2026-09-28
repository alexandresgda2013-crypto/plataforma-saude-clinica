#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 37 — Schemas L-05 v1.2 (auditor-2) + análise do comentador: réplica da casa
=================================================================================
Data: 2026-09-16 · Rodada 21 · Ciência tocada: 0 (só leitura do acervo; validações
com instâncias sintéticas nunca escritas em disco de dados).

Bateria:
  A. Digitais + parse dos 3 recebidos (2 schemas + análise).
  B. Incorporação v1.2 × carta 4 (4 pontos do comentador + 2 reforços da casa) — checklist programático.
  C. Ponto 1 do comentador (condicao: obrigatoriedade SEM exclusividade) — prova executável
     com jsonschema: instância sustenta+condicao PASSA hoje (furo); proposta da casa
     (then condicao type null) medida em 5 casos.
  D. Ponto 2 (sentido_relacao): grep — 0 em dados, N em prosa.
  E. Ponto 3 (redirecionado_clinico × fronteira): perfil medido dos 20.
  F. Adição da casa A: paradoxo do alias N1 (v1.1 tinha enum; v1.2 exige alias SEM enum e
     não exige o canônico; 162/237 com valor composto passariam).
  G. Adição da casa B: superfície de migração medida (N1 e N2 × required/enums v1.2),
     incl. uso='B1_v2' (30) × leva_origem, desenho_estudo 175 valores / 0 dentro do enum,
     guarda regex casa×v1.2 (cross-over), forca_biologica BLOCO_07/08, origem_pipeline composto.
  H. Validação em massa do acervo contra os 2 schemas (superfície objetiva da régua 1.2).
  I. Observação final do comentador (PENDENTE DE DECISAO) — confirmação textual.
"""
import json, re, time
from collections import Counter
from pathlib import Path

import jsonschema

BASE = Path("/home/user/BIBLIOTECAS")
ATUAL = BASE / "B01_Neuroinflamacao/atuais"
RECB = BASE / "_documentos_serie/L05_v1.2_schemas_recebidos_2026-09-16"
V11 = BASE / "_documentos_serie/L05_v1.1_recebido_2026-09-15"
TRILHA = ATUAL / "producao/TRILHA37_schemas_v12_e_analise_comentador_2026-09-16.json"
import hashlib
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

R = {"trilha": 37, "data": "2026-09-16", "rodada": 21,
     "objeto": "schemas L-05 v1.2 + análise do comentador — réplica empírica da casa",
     "etapas": {}, "vereditos": {}, "ciencia_tocada": 0}

SV = json.load(open(RECB / "schema_vinculo_v1.2_recebido_2026-09-16.json"))
SR = json.load(open(RECB / "schema_referencia_v1.2_recebido_2026-09-16.json"))
AA = (RECB / "ANALISE_COMENTADOR_SCHEMAS_V12_2026-09-16.md").read_text(encoding="utf-8")

R["etapas"]["A_digitais"] = {
    "schema_vinculo_v1.2": sha(RECB / "schema_vinculo_v1.2_recebido_2026-09-16.json"),
    "schema_referencia_v1.2": sha(RECB / "schema_referencia_v1.2_recebido_2026-09-16.json"),
    "analise_comentador": sha(RECB / "ANALISE_COMENTADOR_SCHEMAS_V12_2026-09-16.md"),
    "parse_json": "2/2 válidos", "jsonschema_versao": jsonschema.__version__,
    "nota_protocolo": "operador mencionou um '.py' do auditor-2 que NÃO chegou nesta mensagem — nomeado, aguardando envio",
}

# ---------- B. incorporação (4 pontos + 2 reforços)
papel_enum = SV["properties"]["ancoras"]["items"]["properties"]["papel"]["enum"]
dir_enum = SV["properties"]["ancoras"]["items"]["properties"]["direcao_suporte"]["enum"]
inc = {
    "p1_papel_sem_refuta": "refuta" not in papel_enum and len(papel_enum) == 5,
    "p1_direcao_suporte_4valores_com_refuta": dir_enum == ["sustenta", "refuta", "inconclusivo", "condicional"],
    "p2_ancora_principal_campo_string": SV["properties"]["ancora_principal"]["type"] == "string",
    "p2_V17_3testes_declarados_portao": all(s in SV["properties"]["ancora_principal"]["description"]
        for s in ("V-17", "ancoras[*].id_oficial", "uniqueItems")),
    "p3_guarda_natureza_com_0de66_medido": all(s in SR["properties"]["natureza_evidencia"]["description"]
        for s in ("GUARDA DETERMINISTICA", "fila de leitura", "0/66")),
    "p4_status_validacao_canonico_com_enum": SR["properties"]["status_validacao"]["enum"] == ["", "VALIDADO_G3_IA", "VALIDADO_G3_AVALIADOR", "NAO_VALIDADO", "REJEITADO"],
    "p4_alias_deprecated_presente": SR["properties"]["status_auditoria"].get("deprecated") is True,
    "casa_R1_principal_booleano_ausente": "principal" not in json.dumps(SV["properties"]["ancoras"]["items"]["properties"]),
    "casa_R3_padrao_ancorado_em_g3_ambos": ("ANCORADO" in SV["properties"]["g3_verificado_por"]["description"]
        and "ancorado" in SR["properties"]["g3_verificado_por"]["description"]),
}
R["etapas"]["B_incorporacao_verificada"] = inc

# ---------- dados do acervo
vinc = json.load(open(ATUAL / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json"))
vinc = vinc if isinstance(vinc, list) else vinc["vinculos"]
fichas = []
for fn in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
    d = json.load(open(ATUAL / f"Evidencias/Bibliografia/{fn}"))
    it = d if isinstance(d, list) else list(d.values())[0]
    fichas += (list(it.values()) if isinstance(it, dict) else it)

# ---------- C. ponto 1 — prova executável com validador real
tpl = {"id_vinculo": "VINC_B1_9999", "id_referencia_interna": "REF_TESTE_2026",
       "trecho_ancora": "frase ancora sintetica", "status_auditoria": "CONFIRMADO",
       "verification_status": "pendente", "trilha": "mecanistica", "uso": "nucleo_causal",
       "ancoras": [{"id_oficial": "mecanismo_B1_neuroinflamacao", "papel": "sustenta_mecanismo",
                    "direcao_suporte": "sustenta"}],
       "ancora_principal": "mecanismo_B1_neuroinflamacao"}
def valido(inst, schema=SV):
    try:
        jsonschema.validate(inst, schema); return True
    except jsonschema.ValidationError:
        return False
import copy
s1 = valido(tpl)                                              # molde íntegro
i2 = copy.deepcopy(tpl); i2["ancoras"][0]["condicao"] = "só no subgrupo de inflamação alta (sintético)"
s2 = valido(i2)                                               # FURO: sustenta + condicao
i3 = copy.deepcopy(tpl); i3["ancoras"][0]["direcao_suporte"] = "condicional"
s3 = valido(i3)                                               # condicional SEM condicao
i4 = copy.deepcopy(i3); i4["ancoras"][0]["condicao"] = ""
s4 = valido(i4)                                               # condicional com condicao vazia

FIX = {"if": {"properties": {"direcao_suporte": {"enum": ["sustenta", "refuta", "inconclusivo"]}},
              "required": ["direcao_suporte"]},
       "then": {"properties": {"condicao": {"type": "null"}}}}
SV2 = copy.deepcopy(SV)
SV2["properties"]["ancoras"]["items"]["allOf"].append(FIX)
f1 = valido(tpl, SV2)                                         # molde segue válido
f2 = valido(i2, SV2)                                          # furo fechado
i2b = copy.deepcopy(tpl); i2b["ancoras"][0]["condicao"] = None
f2b = valido(i2b, SV2)                                        # sustenta + condicao null (comentador permite)
i4b = copy.deepcopy(i3); i4b["ancoras"][0]["condicao"] = "limite curto"
f3 = valido(i4b, SV2)                                         # condicional + condicao ok
f4 = valido(i3, SV2)                                          # condicional sem condicao segue reprovando
C = {"S1_molde_valido": s1, "S2_FURO_sustenta_com_condicao_PASSA": s2,
     "S3_condicional_sem_condicao_reprova": (not s3), "S4_condicional_condicao_vazia_reprova": (not s4),
     "proposta_casa_bloco": FIX,
     "medicao_da_proposta": {"molde_segue_valido": f1, "furo_fechado": (not f2),
                             "sustenta_condicao_null_ok": f2b, "condicional_com_condicao_ok": f3,
                             "condicional_sem_condicao_segue_reprovando": (not f4)}}
R["etapas"]["C_ponto1_condicao_prova_executavel"] = C
R["vereditos"]["ponto1_comentador_CONFIRMADO_com_proposta"] = (
    s1 and s2 and (not s3) and (not s4) and f1 and (not f2) and f2b and f3 and (not f4))

# ---------- D. ponto 2 — sentido_relacao: dados × prosa
em_dados = sum(1 for x in vinc if "sentido_relacao" in x) + sum(1 for f in fichas if "sentido_relacao" in f)
arquivos_prosa = []
for raiz in (BASE, Path("/home/user/MOTOR_CLINICO"), Path("/home/user/Ferramentas de geração e auditoria")):
    if raiz.exists():
        for p in raiz.rglob("*"):
            if p.is_file() and p.suffix.lower() in (".md", ".json", ".py", ".txt"):
                try:
                    if "sentido_relacao" in p.read_text(encoding="utf-8", errors="ignore"):
                        arquivos_prosa.append(str(p.relative_to("/home/user")))
                except Exception:
                    pass
R["etapas"]["D_ponto2_sentido_relacao"] = {
    "ocorrencias_em_registros_de_dados": em_dados,
    "arquivos_de_prosa_que_mencionam": len(arquivos_prosa), "lista": arquivos_prosa}
R["vereditos"]["ponto2_comentador_CONFIRMADO_medido"] = (em_dados == 0 and len(arquivos_prosa) > 0)

# ---------- E. ponto 3 — os 20 redirecionados perfilados
redir = [x for x in vinc if x.get("g2_elegibilidade") == "redirecionado_clinico"]
perfil = [{"id": x["id_vinculo"], "ref": x.get("id_referencia_interna"),
           "vs": x.get("verification_status"), "sa": x.get("status_auditoria"),
           "uso": x.get("uso")} for x in redir]
R["etapas"]["E_ponto3_redirecionados"] = {
    "total": len(redir), "confere_com_o_texto_do_schema_os_20": len(redir) == 20,
    "dist_ref": dict(Counter(p["ref"] for p in perfil).most_common()),
    "dist_status": dict(Counter(f'{p["vs"]}|{p["sa"]}' for p in perfil)),
    "dist_uso": dict(Counter(p["uso"] for p in perfil)), "lista": perfil,
    "papel_atual_disponivel": "0/20 têm papel (estrutura ancoras não existe ainda) — a classificação semântica está TODA por fazer; a regra da minuta 1.2 decidirá sem lastro de fluxo"
}
R["vereditos"]["ponto3_comentador_CONFIRMADO_com_dados"] = len(redir) == 20

# ---------- F. adição da casa A — paradoxo do alias N1
sr11 = json.load(open(V11 / "schema_referencia_v1.1.json"))
alias_v11_tinha_enum = "enum" in sr11["properties"]["status_auditoria"]
requer_alias = "status_auditoria" in SR["required"]
requer_canonico = "status_validacao" in SR["required"]
alias_tem_enum = "enum" in SR["properties"]["status_auditoria"]
composto = [f["id_referencia_interna"] for f in fichas if "(" in str(f.get("status_auditoria", ""))]
F = {"v1_1_alias_tinha_enum": alias_v11_tinha_enum,
     "v1_2_required_exige_alias": requer_alias, "v1_2_required_exige_canonico": requer_canonico,
     "v1_2_alias_tem_enum": alias_tem_enum,
     "fichas_com_valor_composto_hoje": len(composto), "exemplos": composto[:5],
     "consequencia_medida": "na v1.2 como está, o campo LIMPO canônico pode faltar E o valor composto (162/237 hoje) passa no alias livre — o inverso do alvo normativo",
     "liturgia_espelho_do_proprio_autor": "secao_origem/mecanismo_origem NÃO estão em required no schema_vinculo v1.2 — o alias deveria seguir a mesma regra"}
R["etapas"]["F_adicao_casa_A_alias_N1"] = F
R["vereditos"]["casa_A_paradoxo_alias_CONFIRMADO"] = (alias_v11_tinha_enum and requer_alias
    and not requer_canonico and not alias_tem_enum and len(composto) == 162)

# ---------- G. adição da casa B — superfície de migração
enum_uso = {"clinico", "contexto_mecanistico", "gap_pesquisa", "nucleo_causal", "suporte_correlacional"}
uso_fora = Counter(str(x.get("uso")) for x in vinc if str(x.get("uso")) not in enum_uso)
enum_des = set(SR["properties"]["desenho_estudo"]["enum"])
des_vals = Counter(str(f.get("desenho_estudo")) for f in fichas)
des_fora = sum(n for v2, n in des_vals.items() if v2 not in enum_des)
rx_casa = re.compile(r"(?i)(random|ensaio|trial|duplo|double|placebo|crossover|cross-over|interven|controlled|cego|blind)")
rx_v12 = re.compile(r"(?i)(random|ensaio|trial|duplo|double|placebo|crossover|interven|controlled|cego|blind)")
textos_des = [str(f.get("desenho_estudo", "")) for f in fichas]
sec_dist = Counter(str(x.get("secao_origem")) for x in vinc)
b708 = [x["id_vinculo"] for x in vinc if re.search(r"BLOCO_0[78]", str(x.get("secao_origem", "")))]
op_vals = Counter(str(f.get("origem_pipeline")) for f in fichas)
op_enum = set(SR["properties"]["origem_pipeline"]["enum"])
G = {
    "N2_274": {c: sum(1 for x in vinc if c in x) for c in
               ("ancoras", "ancora_principal", "direcao", "direcao_suporte", "trilha", "condicao")},
    "N2_uso_fora_do_enum": dict(uso_fora),
    "N2_leva_origem_bate_na_descricao": uso_fora.get("B1_v2") == 30,
    "N1_237": {c: sum(1 for f in fichas if c in f) for c in
               ("natureza_evidencia", "desenho_estudo_bruto", "status_validacao")},
    "N1_desenho_valores_distintos": len(des_vals), "N1_desenho_fora_do_enum": des_fora,
    "N1_desenho_top10": des_vals.most_common(10),
    "guarda_regex": {"casa_crossover_e_cross-over_morde": sum(1 for t in textos_des if rx_casa.search(t)),
                     "v1.2_so_crossover_morde": sum(1 for t in textos_des if rx_v12.search(t)),
                     "cross-over_com_hifen_no_acervo": sum(1 for t in textos_des if re.search(r"(?i)cross-over", t)),
                     "nota": "impacto hoje = 0; pedido de restituição de 'cross-over' é preventivo p/ B2-B16 (custou só 1 alternativa na trilha 35)"},
    "forca_biologica": {"campo_0_de_274": sum(1 for x in vinc if "forca_biologica_conexao" in x),
                        "vinculos_com_secao_BLOCO_07_08": len(b708),
                        "nota": "obrigatoriedade BLOCO_07/08 só na prosa do description — sem if/then nem ponteiro de portão; sugerir simetria com V-17"},
    "origem_pipeline": {"fora_do_enum": sum(n for v2, n in op_vals.items() if v2 not in op_enum),
                        "valores": op_vals.most_common(8),
                        "nota": "compostos com data/observação grudada — é o que origem_detalhe recebe (descrição bate com o dado)"},
}
R["etapas"]["G_adicao_casa_B_superficie_migracao"] = G

# ---------- H. validação em massa (superfície objetiva)
def superficie(instancias, schema, idkey):
    falt = Counter(); enum_v = Counter(); outras = Counter(); ok = 0
    for x in instancias:
        errs = list(jsonschema.Draft7Validator(schema).iter_errors(x))
        if not errs:
            ok += 1
        for e in errs:
            if e.validator == "required":
                for m in re.findall(r"'([^']+)'", e.message):
                    falt[m] += 1
            elif e.validator == "enum":
                enum_v[str(e.path[-1] if e.path else "?")] += 1
            elif e.validator == "pattern":
                outras[f"pattern:{e.path[-1] if e.path else '?'}"] += 1
            else:
                outras[e.validator] += 1
    return {"total": len(instancias), "validas_hoje": ok,
            "required_faltando": dict(falt.most_common()),
            "enum_violado": dict(enum_v.most_common()), "outras": dict(outras.most_common())}
R["etapas"]["H_validacao_em_massa"] = {
    "N2_274_x_schema_vinculo_v1.2": superficie(vinc, SV, "id_vinculo"),
    "N1_237_x_schema_referencia_v1.2": superficie(fichas, SR, "id_referencia_interna"),
    "nota": "superfície ESPERADA — schema é PROPOSTA (alvo pós-migração); medida materializa a régua 1.2, não acusa",
}

# ---------- I. observação final do comentador
R["etapas"]["I_observacao_final"] = {
    "trilha_description_diz_PENDENTE_DE_DECISAO": "PENDENTE DE DECISAO" in SV["properties"]["trilha"]["description"],
    "allOf_trilha_condiciona_uso_implementado": any("trilha" in c.get("if", {}).get("required", []) for c in SV["allOf"]),
    "leitura_da_casa": "implementação comporta; o rótulo deve sair quando a Decisão 1 for registrada na minuta 1.2 — coerência de estado entre minuta, schema e registro (como ele pede)",
}
R["vereditos"]["obs_final_comentador_CONFIRMADO"] = R["etapas"]["I_observacao_final"]["trilha_description_diz_PENDENTE_DE_DECISAO"]

TRILHA.write_text(json.dumps(R, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(R["vereditos"], ensure_ascii=False, indent=2))
print("massa N2:", R["etapas"]["H_validacao_em_massa"]["N2_274_x_schema_vinculo_v1.2"]["validas_hoje"], "/274 válidas hoje")
print("massa N1:", R["etapas"]["H_validacao_em_massa"]["N1_237_x_schema_referencia_v1.2"]["validas_hoje"], "/237 válidas hoje")
print("trilha:", TRILHA.name)
