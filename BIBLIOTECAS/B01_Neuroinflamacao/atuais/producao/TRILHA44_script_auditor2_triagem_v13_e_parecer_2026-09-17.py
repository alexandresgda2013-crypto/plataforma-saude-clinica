#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 44 — Pacote do auditor-estrutura (triagem .py + relatório 172/102 + schemas v1.3
+ minuta normativa) + parecer do comentador: RÉPLICA INTEGRAL da casa
================================================================================================
Data: 2026-09-17 · Rodada 25 · 0 ciência (execuções de leitura; o script dele é só-leitura por desenho).

Artefatos (sha registrado em W1):
  W1. parecer comentador (md) · triagem_direcao_suporte.py (colado pelo operador; sha nosso da cópia)
      · relatorio_triagem_direcao_2026-09-16.json · schema_vinculo v1.3 · schema_referencia v1.3
      · minuta normativa (496 linhas).
  W2. Execução do .py dele NA NOSSA bancada × relatório enviado: 9 confrontos.
  W3. ADIÇÃO medida da casa à ressalva §4/§5 do comentador: perfil verification_status dos 172.
  W4. §8-pt4 do parecer: saída transitória não gravada (direcao_suporte 0/274; campo 'direcao' None 274).
  W5. N2 v1.3: bloco condicao == proposta da casa (trilha 37) + complemento allOf[0] · prova jsonschema
      10 casos · separações do §2 do parecer · sentido_relacao só na meta · forca→portão sem número ·
      texto de uso 2+2+1 da casa.
  W6. N1 v1.3: required (status_validacao dentro / alias fora) · alias deprecated COM enum legado ·
      allOf pmid == proposta da casa (trilha 39) · cross-over restituído · sem '(?i' · sem 'Medido hoje'
      · status_auditoria_nota.
  W7. Superfície de migração contra os required v1.3: N1 237×3 (+162 compostos) · N2 274×3 · uso B1_v2 30.
  W8. Minuta: greps ancorados (§3 R1+R7 reescrito+confissão · §10.5 linha(ii) + falsificável RAISON +
      tabela 273/1→172/102 · §13 relatório inline · R2 critério derivador 146=48+71+16+11 · R3/E2 padrão).
  W9. R3/E2 medida dos 2 lados (486 campos avaliador / 0 FP / 5 positivos reprovam / avaliador legítimo
      não morde) · '(?i' 0 em v1.2/v1.3 · kit: evidence_role enum exatos 4 (§9 da minuta).
  W10. Errata §4B: atípico atual medido = VINC_B1_0047·HAFIZI·pendente_fulltext (dívida conhecida);
      ficha N1 REF_OSIMO_2019 = 'verificado' (a errata refere-se à v1.0 histórica) — coerência registrada.
  W11. §2 parecer: separações verificadas no schema (status_auditoria×verification_status · trilha×uso ·
      ancora_principal×ancoras · g3_verificado_por×g3_nota_metodo · papel×direcao_suporte).
  W12. §8 do parecer — 6 pontos respondidos um a um (agregado).
  W13. Selos 0 ciência (V7/manifesto/P-8).
Nota de método (confissão): a 1ª prova jsonschema usou objeto-base com papel fora do enum; os casos 'ok'
falharam por CAMPO REQUIRED, não pelo bloco condicao — corrigido e refeito: 10/10.
Nota de método 2 (confissão datada 2026-09-17): a 1ª execução desta trilha apontou 4 falhas que eram
regex da casa apertadas demais — (a) 'forca sem número' lia dígitos de IDENTIFICADORES (draft-07, V-17)
como se fossem medição; (b) 'creditos' exigia 'a casa' minúsculo (texto tem 'A casa'); (c) errata 21→92
usava [^.]+ que parava no ponto seguinte; (d) REF_OSIMO_2019 sem a crase do markdown. Corrigidas as 4;
o material do auditor/comentador estava certo nos 4 pontos. JSON reescrito pela execução corrigida.
"""
import hashlib, json, re, subprocess, sys
from collections import Counter
from pathlib import Path

BASE  = Path("/home/user/BIBLIOTECAS")
AT    = BASE / "B01_Neuroinflamacao/atuais"
RECB  = BASE / "_documentos_serie/AUDITOR2_triagem_L05v13_recebido_2026-09-17"
V12   = BASE / "_documentos_serie/L05_v1.2_schemas_recebidos_2026-09-16"
P8    = Path("/home/user/Ferramentas de geração e auditoria/06_portao_P8_coerencia/scripts/validar_coerencia_camadas.py")
TRILHA = AT / "producao/TRILHA44_auditor2_triagem_v13_e_parecer_2026-09-17.json"
sha   = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

R = {"trilha": 44, "data": "2026-09-17", "rodada": 25,
     "objeto": "pacote auditor-2 (triagem+173/102+schemas v1.3+minuta) + parecer comentador — réplica integral",
     "etapas": {}, "vereditos": {}, "ciencia_tocada": 0}
F = {
 "parecer": RECB/"PARECER_COMENTADOR_L05V13_TRIAGEM_2026-09-17.md",
 "py":      RECB/"triagem_direcao_suporte.py",
 "rel":     RECB/"relatorio_triagem_direcao_2026-09-16.json",
 "n2v13":   RECB/"schema_vinculo_v1.3_recebido_2026-09-17.json",
 "n1v13":   RECB/"schema_referencia_recebido_2026-09-17.json",
 "minuta":  RECB/"L05_minuta_normativa_recebida_2026-09-17.md"}

# ---------- W1
R["etapas"]["W1_arquivamento"] = {k: {"sha256": sha(F[k]), "bytes": F[k].stat().st_size} for k in F}
R["etapas"]["W1_arquivamento"]["schemas_v12_de_referencia"] = {
    "n2_v12": sha(V12/"schema_vinculo_v1.2_recebido_2026-09-16.json"),
    "n1_v12": sha(V12/"schema_referencia_v1.2_recebido_2026-09-16.json")}

# ---------- W2. executa o .py dele
saidaj = AT / "producao/trilha44_reexec_triagem_auditor2_2026-09-17.json"
run = subprocess.run([sys.executable, str(F["py"]), str(AT), "--json", str(saidaj)],
                     capture_output=True, text=True)
casa, rel = json.load(open(saidaj)), json.load(open(F["rel"]))
lf = lambda L: sorted(x["id_vinculo"] for x in L)
w2 = {"exit_code": run.returncode,
      "sha256_entrada_bate": casa["sha256_entrada"] == rel["sha256_entrada"],
      "total_274": casa["total"] == rel["total"] == 274,
      "automaticos_172": casa["automaticos"] == rel["automaticos"] == 172,
      "fila_102": casa["fila_humana"] == rel["fila_humana"] == 102,
      "por_regra_82_19_1": casa["por_regra"] == rel["por_regra"] == {
          "regra_1_confirmado_sem_sinal": 172, "regra_2_confirmado_com_sinal": 82,
          "regra_3_parcialmente_confirmado": 19, "regra_0_status_nao_triavel": 1},
      "fila_ids_identicas": lf(casa["lista_fila_humana"]) == lf(rel["lista_fila_humana"]),
      "auto_ids_identicos": lf(casa["lista_automaticos"]) == lf(rel["lista_automaticos"]),
      "motivos_identicos": ({x["id_vinculo"]: x["motivo"] for x in casa["lista_fila_humana"]} ==
                            {x["id_vinculo"]: x["motivo"] for x in rel["lista_fila_humana"]}),
      "raison_aprovado": casa["teste_aceitacao"]["aprovado"] is True and rel["teste_aceitacao"]["aprovado"] is True,
      "raison_vinculos": [(x["id_vinculo"], x["direcao_suporte"]) for x in casa["teste_aceitacao"]["vinculos"]],
      "sha256_entrada": casa["sha256_entrada"]}
R["etapas"]["W2_reexecucao_x_relatorio"] = w2
for k, v in w2.items():
    if isinstance(v, bool): R["vereditos"]["W2_" + k] = v
R["vereditos"]["W2_exit_code_0"] = run.returncode == 0

vinc = json.load(open(AT/"Evidencias/Vinculos/vinculos_referencia_afirmacao.json"))
vinc = vinc if isinstance(vinc, list) else vinc["vinculos"]
idx = {x["id_vinculo"]: x for x in vinc}

# ---------- W3. adição: perfil dos 172
auto = [idx[i] for i in lf(casa["lista_automaticos"])]
pv = Counter(str(x.get("verification_status")) for x in auto)
R["etapas"]["W3_perfil_172_verification_status"] = {"dist": dict(pv.most_common()),
    "nao_verificado": sum(n for k, n in pv.items() if k != "verificado"),
    "leitura": ("corpo empírico à ressalva §4/§5 do comentador: 58/172 (33,7%) dos 'sustenta transitório' NÃO são "
                "'verificado' (inclui 5 extrapolado + 3 pendente que NÃO carregam sinal textual). Não é furo do "
                "script — ele mira DIREÇÃO; a cautela de maturidade mora em verification_status (eixo separado). "
                "Registro proposto: no portão/migração, os 172 transitórios carregam marca dupla: transitório-de-"
                "direção + value='verificado' apenas em 114.")}
R["vereditos"]["W3_medida_registrada"] = (pv.get("verificado") == 114 and len(auto) == 172)

# ---------- W4. §8-pt4: transitório não gravado
ds = sum(1 for x in vinc if x.get("direcao_suporte") not in (None, ""))
dvelho = Counter(str(x.get("direcao")) for x in vinc)
R["etapas"]["W4_transitorio_nao_gravado"] = {"direcao_suporte_no_acervo": ds, "campo_direcao_legado": dict(dvelho)}
R["vereditos"]["W4_nada_gravado_no_acervo"] = (ds == 0 and set(dvelho) == {"None"})

# ---------- W5. N2 v1.3
S2 = json.load(open(F["n2v13"]))
item = S2["properties"]["ancoras"]["items"]
allo = item["allOf"]
casa37 = {"if": {"properties": {"direcao_suporte": {"enum": ["sustenta", "refuta", "inconclusivo"]}}, "required": ["direcao_suporte"]},
          "then": {"properties": {"condicao": {"type": "null"}}}}
from jsonschema import Draft7Validator
Vv = Draft7Validator(item)
base_it = {"id_oficial": "mecanismo_B1_neuroinflamacao", "papel": "sustenta_mecanismo", "direcao_suporte": "sustenta"}
casos = [({}, True), ({"condicao": "x"}, False),
         ({"direcao_suporte": "refuta"}, True), ({"direcao_suporte": "refuta", "condicao": "x"}, False),
         ({"direcao_suporte": "inconclusivo"}, True), ({"direcao_suporte": "inconclusivo", "condicao": "x"}, False),
         ({"direcao_suporte": "condicional", "condicao": "só subgrupo"}, True),
         ({"direcao_suporte": "condicional"}, False),
         ({"direcao_suporte": "condicional", "condicao": ""}, False),
         ({"direcao_suporte": "pendente"}, False)]
n_ok = sum(Vv.is_valid({**base_it, **a}) == esp for a, esp in casos)
blob2 = json.dumps(S2, ensure_ascii=False)
R["etapas"]["W5_N2_v13"] = {
    "allOf0_obriga_condicao_quando_condicional": allo[0]["then"].get("required") == ["condicao"],
    "allOf1_igual_a_proposta_da_casa_trilha37": allo[1] == casa37,
    "jsonschema_10_casos": f"{n_ok}/10",
    "papel_enum_sem_refuta": item["properties"]["papel"].get("enum"),
    "direcao_suporte_4v": item["properties"]["direcao_suporte"].get("enum"),
    "ancora_principal_no_root_required": "ancora_principal" in S2.get("required", []),
    "ancoras_uniqueItems": S2["properties"]["ancoras"].get("uniqueItems"),
    "sentido_relacao_ocorrencias_total": blob2.count("sentido_relacao"),
    "forca_biologica_ponteiro_sem_medicao": (lambda d: ("port" in d.lower()
                                            and "relatorio de migracao" in d
                                            and not re.search(r"\b24\b", d)))(
                                            S2["properties"]["forca_biologica_conexao"].get("description", "")),
    "texto_uso_2mais2mais1": "clinica = {clinico, contexto_mecanistico}" in S2["properties"]["uso"].get("description", ""),
    "status_auditoria_N2_enum_limpo": S2["properties"]["status_auditoria"].get("enum")}
R["vereditos"]["W5_condicao_bloco_casa_adotado_e_10de10"] = (allo[1] == casa37 and n_ok == 10)
R["vereditos"]["W5_separacoes_e_prosa_ok"] = (R["etapas"]["W5_N2_v13"]["sentido_relacao_ocorrencias_total"] == 1
    and R["etapas"]["W5_N2_v13"]["forca_biologica_ponteiro_sem_medicao"] and R["etapas"]["W5_N2_v13"]["texto_uso_2mais2mais1"]
    and "refuta" not in str(item["properties"]["papel"].get("enum")))

# ---------- W6. N1 v1.3
S1 = json.load(open(F["n1v13"]))
blob1 = json.dumps(S1, ensure_ascii=False)
casa39 = {"if": {"properties": {"natureza_evidencia": {"not": {"const": "nao_aplicavel"}}}, "required": ["natureza_evidencia"]},
          "then": {"properties": {"pmid_oficial": {"pattern": "^[0-9]{1,8}$"}}}}
req13 = S1.get("required", [])
R["etapas"]["W6_N1_v13"] = {
    "required_tem_status_validacao": "status_validacao" in req13,
    "required_sem_alias": "status_auditoria" not in req13,
    "alias_deprecated_com_enum": bool(S1["properties"]["status_auditoria"].get("deprecated")) and bool(S1["properties"]["status_auditoria"].get("enum")),
    "allOf_pmid_igual_proposta_casa_trilha39": S1["allOf"][2] == casa39,
    "pmid_base_ainda_0a8_provisorio": S1["properties"]["pmid_oficial"].get("pattern") == "^[0-9]{0,8}$",
    "cross_over_restituido": "cross-over" in blob1,
    "sem_modificador_case_invalido": "(?i" not in blob1,
    "sem_Medido_hoje_em_descriptions": "Medido hoje" not in blob1,
    "status_auditoria_nota_presente": "status_auditoria_nota" in S1["properties"]}
for k, v in R["etapas"]["W6_N1_v13"].items(): R["vereditos"]["W6_" + k] = bool(v)

# ---------- W7. superfície
fichas = []
for fn in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
    fichas += json.load(open(AT/f"Evidencias/Bibliografia/{fn}"))
falt1 = Counter(r for f in fichas for r in req13 if r not in f or f.get(r) is None)
falt2 = Counter(r for x in vinc for r in S2.get("required", []) if r not in x or x.get(r) is None)
comp = sum(1 for f in fichas if isinstance(f.get("status_auditoria"), str) and "(" in str(f.get("status_auditoria")))
uso_fora = Counter(str(x.get("uso")) for x in vinc if str(x.get("uso")) not in
                   {"clinico", "contexto_mecanistico", "gap_pesquisa", "nucleo_causal", "suporte_correlacional"})
R["etapas"]["W7_superficie_vs_v13"] = {"N1_required_faltando": dict(falt1), "fichas_composto_a_migrar": comp,
    "ja_tem_status_validacao": sum(1 for f in fichas if "status_validacao" in f),
    "N2_required_faltando": dict(falt2), "uso_fora_do_enum": dict(uso_fora),
    "leitura": "idêntica à ADIÇÃO B da casa (trilha 37), agora contra os required FINAIS v1.3 — superfície de migração quantificada e convergente"}
R["vereditos"]["W7_superficie_convergente"] = (falt1.get("status_validacao") == 237 and comp == 162
    and falt2.get("trilha") == 274 and uso_fora == Counter({"B1_v2": 30}))

# ---------- W8. minuta greps ancorados
mt = F["minuta"].read_text(encoding="utf-8")
gh = lambda pad: bool(re.search(pad, mt, re.S))
R["etapas"]["W8_minuta"] = {
    "sec3_reescrito_R1_R7": gh(r"§3 reescrito na forma R1\+R7"),
    "confissao_e_creditos_casa": gh(r"(?i)a casa ampliou o achado para o R1; a ampliação procede"),
    "linha_ii_sec105": gh(r"10\.5 Linha \(ii\) — triagem de `direcao_suporte`: mantenho a recusa"),
    "criterio_falsificavel": gh(r"REF_RAISON_2013`? não sair `?sustenta"),
    "tabela_273_1_para_172_102": gh(r"}\s*=\s*\{" ) is False and ("| 273 | **172** |" in mt and "| 1 | **102**" in mt),
    "sec13_relatorio_inline": gh(r"13\. RELATÓRIO DE EXECUÇÃO DA TRIAGEM — 172/102"),
    "confissao_regra_nao_publicada": gh(r"a bancada não conseguiu reverter os 102[^.]+"),
    "R2_criterio_derivador_146": gh(r"146 IDs válidos[^.]+48 de suplementos[^.]+71 de exames[^.]+16 mecanismos[^.]+11 cenários"),
    "R3_E2_padrao_publicado": gh(r"\^\\s\*\(eutils\|script\|retrofit\)\[a-z0-9_\]\*\\s\*\$"),
    "errata_21_para_92": gh(r"21 valores distintos.*?92"),
    "errata_sec4b_osimo": gh(r"`REF_OSIMO_2019`, com valor livre e erro de digitação")}
for k, v in R["etapas"]["W8_minuta"].items(): R["vereditos"]["W8_" + k] = bool(v)

# ---------- W9. E2 dois lados + kit enum
pad = re.compile(r"^\s*(eutils|script|retrofit)[a-z0-9_]*\s*$", re.IGNORECASE)
alvos = []
for fn in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
    for f in fichas:
        pass
for f in fichas:
    for c in ("g3_verificado_por", "g3_nota_metodo"):
        if f.get(c) not in (None, ""): alvos.append(("N1", c, str(f[c])))
for x in vinc:
    for c in ("g3_verificado_por", "g3_nota_metodo"):
        if x.get(c) not in (None, ""): alvos.append(("N2", c, str(x[c])))
fp = sum(1 for _, c, s in alvos if pad.search(s))
kit = (BASE/"_documentos_serie/KIT_CLINICA_recebido_2026-09-15/3º SCHEMA-CLAIM — v1.2.md").read_text(encoding="utf-8")
m = re.search(r"evidence_role:\s*([^\n]+)", kit)
R["etapas"]["W9_E2_e_kit"] = {"campos_avaliador_varridos": len(alvos), "falsos_positivos": fp,
    "positivos_reprovados": {p: bool(pad.search(p)) for p in ("eutils", "eutils_automatico", "script", "retrofit", "EUTILS_AUTO")},
    "avaliador_legitimo_nao_morde": not pad.search("IA_casa (rito [AT]; abstract eutils colado no ledger AUD_B1_0238)"),
    "modificador_case_nos_dois_schemas": {"v12": open(V12/"schema_referencia_v1.2_recebido_2026-09-16.json", encoding="utf-8").read().count("(?i"),
                                          "v13": blob1.count("(?i")},
    "kit_evidence_role_enum": m.group(1).strip() if m else None}
R["vereditos"]["W9_E2_dois_lados_verde"] = (fp == 0 and all(R["etapas"]["W9_E2_e_kit"]["positivos_reprovados"].values())
    and R["etapas"]["W9_E2_e_kit"]["avaliador_legitimo_nao_morde"])
R["vereditos"]["W9_kit_enum_4_sem_review"] = bool(m and m.group(1).strip() == "human_clinical | human_experimental | post_mortem | preclinical_mechanistic")

# ---------- W10. errata §4B
atip = [(x["id_vinculo"], x.get("id_referencia_interna")) for x in vinc if "fulltext" in str(x.get("verification_status", "")).lower()]
os19 = next((f for f in fichas if f.get("id_referencia_interna") == "REF_OSIMO_2019"), {})
R["etapas"]["W10_errata_sec4B"] = {
    "atipico_hoje_no_274": atip,
    "REF_OSIMO_2019_hoje": {"verification_status": os19.get("verification_status"), "evid_role": os19.get("evid_role")},
    "leitura": ("a errata dele refere-se à v1.0 histórica (a identidade do inválido NA ÉPOCA: REF_OSIMO_2019, "
                "corrigido desde então — hoje 'verificado' no N1). No dado ATUAL o único atípico é "
                "VINC_B1_0047·HAFIZI_2007 'pendente_fulltext' = a dívida conhecida. Rodapé 274 recontado: bate.")}
rodape = Counter(str(x.get("verification_status")) for x in vinc)
R["vereditos"]["W10_rodape_bate_e_osimo_corrigido"] = (atip == [("VINC_B1_0047", "REF_HAFIZI_2007")]
    and os19.get("verification_status") == "verificado"
    and rodape == Counter({"verificado": 140, "preclinico": 63, "extrapolado": 62, "pendente": 7, "pendente_fulltext": 1, "emergente": 1}))

# ---------- W11/W12. §2 e §8 do parecer
R["etapas"]["W11_separacoes_sec2_parecer"] = {
    "papel_x_direcao_suporte": "papel" in item["properties"] and "direcao_suporte" in item["properties"],
    "status_auditoria_x_verification_status": "status_auditoria" in S2["properties"] and "verification_status" in S2["properties"],
    "trilha_x_uso": "trilha" in S2["properties"] and "uso" in S2["properties"],
    "ancora_principal_x_ancoras": "ancora_principal" in S2["properties"] and "ancoras" in S2["properties"],
    "forca_causal_x_forca_biologica": "forca_causal" in S2["properties"] and "forca_biologica_conexao" in S2["properties"],
    "avaliador_x_nota": "g3_verificado_por" in S2["properties"] and "g3_nota_metodo" in S2["properties"]}
R["vereditos"]["W11_separacoes_6de6"] = all(R["etapas"]["W11_separacoes_sec2_parecer"].values())
R["etapas"]["W12_sec8_parecer_6_pontos"] = {
    "1_relatorio_sobre_o_sha_apresentado": w2["sha256_entrada_bate"] and w2["sha256_entrada"] == casa["sha256_entrada"],
    "2_contagens_reproduziveis": w2["total_274"] and w2["automaticos_172"] and w2["fila_102"],
    "3_raison_falha_fechado": w2["raison_aprovado"],
    "4_nada_gravado_como_decisao_definitiva": R["vereditos"]["W4_nada_gravado_no_acervo"],
    "5_separacao_status_x_direcao": R["vereditos"]["W11_separacoes_6de6"],
    "6_campos_e_regras_iguais_ao_artefato": R["vereditos"]["W5_condicao_bloco_casa_adotado_e_10de10"] and all(R["etapas"]["W6_N1_v13"].values())}
R["vereditos"]["W12_sec8_6de6_atendidos"] = all(R["etapas"]["W12_sec8_parecer_6_pontos"].values())

# ---------- W13. selos
R["etapas"]["W13_selos"] = {"V7": sha(AT/"B1 NEUROINFLAMAÇÃO V7 CANONICA.md"),
                            "manifesto": sha(AT/"Evidencias/Bibliografia/_manifesto_biblioteca.json"),
                            "P8": sha(P8),
                            "esperados": {"V7": "6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238",
                                          "P8": "84fa918d09899d54995ae41d65b0787a7a52888ba6177ce77583483b1124fe8b"}}
R["vereditos"]["W13_ciencia_intacta"] = (R["etapas"]["W13_selos"]["V7"] == R["etapas"]["W13_selos"]["esperados"]["V7"]
    and R["etapas"]["W13_selos"]["manifesto"].startswith("79d1309a")
    and R["etapas"]["W13_selos"]["P8"] == R["etapas"]["W13_selos"]["esperados"]["P8"])

TRILHA.write_text(json.dumps(R, ensure_ascii=False, indent=2), encoding="utf-8")
falhas = {k: v for k, v in R["vereditos"].items() if v is not True}
print(f"VEREDITOS: {sum(1 for v in R['vereditos'].values() if v is True)}/{len(R['vereditos'])} verdes")
print("FALHAS:", json.dumps(falhas, ensure_ascii=False, indent=1) if falhas else "nenhuma")
print("\nW2 reexecução:", run.stdout.splitlines()[3:12])
print("\nW3 perfil 172:", dict(pv.most_common()))
print("W7 superfície:", R["etapas"]["W7_superficie_vs_v13"]["leitura"][:120])
