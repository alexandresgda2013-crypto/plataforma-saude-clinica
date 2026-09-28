#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 41 — Comentário do comentador (ChatGPT) sobre a resposta do mestre
(ancoragem do kit + diff + camada): réplica da casa
========================================================================================
Data: 2026-09-17 · Rodada 23 · 0 ciência (só leituras/greps/medidas; nada escrito no
acervo, no kit ou na V2).

Objeto: COMENTARIO_COMENTADOR_KIT_ANCORAGEM_E_ARQUITETURA_2026-09-17.md (9 seções).

Etapas:
  V0. Arquivamento: sha/bytes/linhas do verbatim recebido.
  V1. §3 — números do kit citados (uso 23 · ER 22/22 · comparador 59/8 · moderadores 22 ·
      usado_em_biblioteca 23 · 4 gap_pesquisa · 10 PMIDs na V7) — reexecução com as regex
      oficiais das trilhas 40/33 GRAVADAS abaixo (norma: medida sem comando não vale).
      Inclui NOTA DE MÉTODO: aspas opcionais em `pmid: "N"` (30/49) — grep raso sem aspas
      subcaptura (19 no escopo). Honestidade: mesma classe da confissão datada da trilha 40.
  V2. §1/§2 — aceites (ancoragem encerrada; diff reconciliado; pedido: "arquivo adotado
      identificado no registro final" — já é critério da casa desde rev.28: 1 sha publicada).
  V3. §4/§5/§8/§9 — confronto com o texto da V2 vigente (sha registrado; greps com linhas):
      (i) diagrama do §2: CATÁLOGO→BIBLIOTECA→{EVIDÊNCIAS, NT}→VÍNCULOS (Evidências ABAIXO
      da Biblioteca); (ii) §5.3: minidiagrama EVIDÊNCIA→BIBLIOTECA→NT (a leitura do
      comentador bate AQUI); (iii) única "posição paralela à cadeia canônica" no texto:
      Pasta de Atualização; (iv) NT deverá "1. consumir a Biblioteca; 2. utilizar
      Evidências/Vínculos" (§6 — redação vigente = o §5/§8 dele); (v) V2: 0 ocorrências de
      kit/SM-02/SCHEMA-CLAIM; (vi) §5: Evidências "não constituem uma segunda Biblioteca
      Canônica nem uma fonte... independente"; (vii) caminho §5.1 `/Evidencias/Bibliograficas`
      (raiz) × disco real `BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia`.
  V4. §6 — split sim/nao de usado_em_biblioteca (medido: nao 23 sim 0) · instrução textual
      do SCHEMA-CLAIM linhas 87-92 ("rastreabilidade de consumo rio abaixo... não bloqueia")
      · fichas V7 com claim_id_origem B1.SM02.* (0) → ponto do comentador SUSTENTADO pelos
      próprios artefatos.
  V5. §7 — 4 gap_pesquisa (kit) × 4 nao_estabelecida (acervo 274) — convergência registrada.
  V6. Selos de não-ciência: shas V7 canônica + manifesto + P-8 oficial conferidos ao final.
"""
import hashlib, json, re
from collections import Counter
from pathlib import Path

BASE  = Path("/home/user/BIBLIOTECAS")
ATUAL = BASE / "B01_Neuroinflamacao/atuais"
KIT   = BASE / "_documentos_serie/KIT_CLINICA_recebido_2026-09-15"
RECB  = BASE / "_documentos_serie/COMENTADOR_kit_arquitetura_recebido_2026-09-17"
V2    = BASE / "_documentos_serie/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md"
P8    = Path("/home/user/Ferramentas de geração e auditoria/06_portao_P8_coerencia/scripts/validar_coerencia_camadas.py")
TRILHA = ATUAL / "producao/TRILHA41_comentador_kit_arquitetura_2026-09-17.json"
sha   = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

R = {"trilha": 41, "data": "2026-09-17", "rodada": 23,
     "objeto": "comentário do comentador (ChatGPT) sobre a resposta do mestre (kit ancorado + diff + camada) — réplica",
     "etapas": {}, "vereditos": {}, "ciencia_tocada": 0}

# ---------- V0. arquivamento
doc = RECB / "COMENTARIO_COMENTADOR_KIT_ANCORAGEM_E_ARQUITETURA_2026-09-17.md"
R["etapas"]["V0_arquivamento"] = {
    "arquivo": str(doc), "sha256": sha(doc),
    "bytes": doc.stat().st_size,
    "linhas": len(doc.read_text(encoding="utf-8").splitlines()),
    "politica": "nota crua de comentador NUNCA circula — a casa carrega os pontos verificados em carta própria com crédito"}

# ---------- V1. §3 números do kit (regex oficiais trilhas 40/33)
bloco = KIT.joinpath("6º BLOCO DE ESTADO  v1.6.md").read_text(encoding="utf-8")
v1 = {"regex_escopo": {
        "uso":            r'(?:^|[^_a-z])uso:\s*([a-z_]+) @6ºBLOCO — camada VALOR',
        "evidence_role":  r'(?:^|[^_a-z])evidence_role:\s*([a-z_]+) @6ºBLOCO — camada VALOR',
        "comparador":     r'(?:^|[^_a-z])comparador:\s*([a-z_0-9]+) @6ºBLOCO — camada VALOR',
        "moderadores":    r'(?:^|[^_a-z])moderadores: @6ºBLOCO — camada CHAVE (inclui "[]" vazio)',
        "usado_em_biblioteca": r'(?:^|[^_a-z])usado_em_biblioteca:\s*([a-z]+) @6ºBLOCO — camada VALOR',
        "claim_id_aprovados":  r'(?:^|\s)-\s*[Cc]laim_id:\s*(B1\.SM02\.\S+) @escopo claims_aprovados (caixa-insensível: SM02.015 usa "Claim_id")',
        "pmids_kit":      r'pmid:\s*"?(\d{7,9})"? @escopo claims_aprovados (BLOCO) — aspas opcionais',
        "pmids_v7":       "campo pmid_oficial das 237 fichas (01_pmids/02_meta/03_ec)"},
      "granularidade_medida_quatro_camadas": {
        "uso":            {"palavra": 25, "chave_com_2pontos": 23, "valor_valido": 22,
                           "espuria": "L182 — papel_geral: \"Regra de uso: IL-1β…\" (prosa com ':'; não é campo)"},
        "usado_em_biblioteca": {"palavra": 23, "chave_com_2pontos": 22, "valor_valido": 22,
                           "espuria": "L28 — comentário do changelog interno ('adicionado campo usado_em_biblioteca…'; sem ':')"},
        "comparador":     {"palavra": 58, "chave_com_2pontos": 48, "valor_valido": 48,
                           "espurias": "prosa sem ':' ('comparadores impede…', 'comparador regional…', 'comparador — sem replicação…' etc.)"},
        "moderadores":    {"palavra": 22, "chave_com_2pontos": 22},
        "evidence_role":  {"valor_valido": 22},
        "regra_da_casa": "a camada VALOR é a única porta de entrada para conclusões; camadas acima contam texto"},
      "citado_X_medido": {
        "uso 23":            "camada 'chave com :' reproduz 23 (22 campos + 1 prosa L182) — número citado CONFERE nessa camada; valor útil = 22 (12 clinico/6 contexto/4 gap)",
        "usado_em_biblioteca 23": "camada 'palavra' reproduz 23 (22 valores + comentário L28) — CONFERE nessa camada; valor útil = 22, todos 'nao' (0 'sim' — o que importa p/ §6)",
        "comparador 59/8":   "8 valores CONFEM exatos (dist: 38/3/2/1/1/1/1/1). Total 59 NÃO reproduz no BLOCO isolado (palavra=58, chave/valor=48). Hipótese fechada: 58(BLOCO)+1('comparador: string' placeholder no SCHEMA-CLAIM)=59 → escopo do mestre provavelmente incluiu outro arquivo. Nota: a dist do mestre (38/3/2/…=48) não soma 59 — divergência de contagem pontual, sem efeito semântico",
        "moderadores 22 · evidence_role 22/22 · gap 4 · 10 PMIDs na V7": "CONFEM na camada de valor, pleno"},
      "errata_fina_rodada22_2026-09-17": ("a casa endossou na trilha 40 (M2b) os totais 23/23/59 por camada textual "
        "sem ainda nomear as linhas espúrias; esta trilha nomeia (L182/L28/prosa de comparador) e separa as "
        "camadas com comandos gravados. Nenhuma conclusão da rodada 22 muda. A trilha 40 permanece intocada "
        "(norma: corrigir com nota datada, nunca reescrever)."),
      "nota_metodo_V1b_2026-09-17": ("a 1ª execução desta trilha repetiu a regex ANCORADA já confessada como "
        "subcaptura na trilha 40; corrigido NA MESMA rodada, antes de qualquer JSON — confissão datada: "
        "reincidência da mesma classe de erro; o repositório nunca recebeu o número errado."),
      "notas_higiene_kit_para_decisao_da_camada": [
        "pmid com aspas opcionais: 30/49 como pmid: \"N\" — parser sem aspas-opcional subcaptura (49↔19)",
        "SM02.015 usa 'Claim_id' maiúsculo e indentação de 3 espaços/TAB (linhas 513/578/701/706) — parser sensível a caixa/recuo perde 1 de 22 claims",
        "chaves também aparecem em prosa (L182) e comentários (L28) — toda contagem precisa de camada declarada",
        "placeholder 'comparador: string' no SCHEMA-CLAIM contamina contagem textual se escopo > BLOCO"]}
uso  = re.findall(r"(?:^|[^_a-z])uso:\s*([a-z_]+)", bloco)
er   = re.findall(r"(?:^|[^_a-z])evidence_role:\s*([a-z_]+)", bloco)
comp = re.findall(r"(?:^|[^_a-z])comparador:\s*([a-z_0-9]+)", bloco)
mods = re.findall(r"(?:^|[^_a-z])moderadores:", bloco)
ub   = re.findall(r"(?:^|[^_a-z])usado_em_biblioteca:\s*([a-z]+)", bloco)
escopo = bloco.split("claims_aprovados:", 1)[1].split("# LOG DE EXCLUSÃO", 1)[0].split("# ====" * 8, 1)[0]
claims_ids = re.findall(r"(?m)^\s*-\s*[Cc]laim_id:\s*(B1\.SM02\.\S+)", escopo)
gap_ids = [re.match(r"\s*(B1\.SM02\.\S+)", b).group(1)
           for b in re.split(r"(?m)^\s*-\s*[Cc]laim_id:", escopo)[1:]
           if re.search(r"(?:^|[^_a-z])uso:\s*gap_pesquisa", b)]
pmids_kit = set(re.findall(r'pmid:\s*"?(\d{7,9})"?', escopo))
pmids_sem_aspas = set(re.findall(r"pmid:\s*(\d+)", escopo))
fichas = []
for fn in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json"):
    fichas += json.load(open(ATUAL / f"Evidencias/Bibliografia/{fn}"))
acervo = {str(f.get("pmid_oficial")).strip() for f in fichas
          if str(f.get("pmid_oficial") or "").strip().lower() not in ("none", "null", "")}
inter = sorted(pmids_kit & acervo)
v1["uso"]            = {"total": len(uso), "dist": dict(Counter(uso))}
v1["evidence_role"]  = {"total": len(er), "dist": dict(Counter(er))}
v1["comparador"]     = {"total": len(comp), "valores_distintos": len(set(comp))}
v1["moderadores_ocorrencias"] = len(mods)
v1["usado_em_biblioteca"] = {"total": len(ub), "dist": dict(Counter(ub))}
v1["claims_aprovados_distintos"] = len(set(claims_ids))
v1["gap_pesquisa"]   = {"total": len(gap_ids), "ids": sorted(set(gap_ids))}
v1["pmids"] = {"unicos_kit": len(pmids_kit), "presentes_na_V7": len(inter), "ausentes": len(pmids_kit - acervo),
               "lista_presentes": inter,
               "nota_metodo_aspas": (f"{len(pmids_sem_aspas)}/49 casam sem aspas-opcional; "
                                     f"{len(pmids_kit - pmids_sem_aspas)} campos vêm como pmid: \"N\". "
                                     "Grep raso sem aspas subcaptura — confissão da casa registrada: a mesma "
                                     "classe de erro da trilha 40 (regex sem cobertura do formato real). "
                                     "A medida 49/10/39 confere com a trilha 33 (comando gravado).")}
R["etapas"]["V1_secao3_numeros_do_kit"] = v1
n_uso_chave  = len(re.findall(r"(?:^|[^_a-z])uso:", bloco))
n_ub_palavra = len(re.findall(r"usado_em_biblioteca\b", bloco))
n_comp_palavra = len(re.findall(r"comparador\b", bloco))
R["vereditos"]["V1_uso_valor_22_12_6_4_e_citado23_reproduz_na_camada_chave"] = (
    len(uso) == 22 and Counter(uso) == Counter({"clinico": 12, "contexto_mecanistico": 6, "gap_pesquisa": 4})
    and n_uso_chave == 23)
R["vereditos"]["V1_evidence_role_22_22"] = (len(er) == 22 and set(er) == {"human_clinical"})
R["vereditos"]["V1_comparador_valor_48_8valores_8_do_citado_conferem"] = (
    len(comp) == 48 and len(set(comp)) == 8 and
    Counter(comp) == Counter({"controles_saudaveis": 38, "transtorno_bipolar": 3,
        "controles_com_hipertensao_intracraniana_idiopatica": 2, "outros_transtornos_psiquiatricos": 1,
        "mulheres_idosas_sem_depressao": 1, "correlacao_continua_dentro_coorte_gds15": 1,
        "controles_sem_comorbidades_inflamatorias_conhecidas": 1, "bipolar": 1}))
R["vereditos"]["V1_total_comparador_citado59_NAO_reproduz_no_BLOCO_isolado"] = (n_comp_palavra == 58)
R["vereditos"]["V1_moderadores_22"]    = len(mods) == 22
R["vereditos"]["V1_usado_em_biblioteca_valor_22_todos_nao_e_citado23_reproduz_na_camada_palavra"] = (
    len(ub) == 22 and set(ub) == {"nao"} and n_ub_palavra == 23)
R["vereditos"]["V1_gap_pesquisa_4"]    = len(set(gap_ids)) == 4
R["vereditos"]["V1_10_PMIDs_na_V7"]    = (len(pmids_kit) == 49 and len(inter) == 10)
R["vereditos"]["V1_claims_22_blocos_com_SM02015_Caixa_Maiuscula"] = (len(claims_ids) == 22 and len(set(claims_ids)) == 22)

# ---------- V3. confronto com a V2 vigente
v2txt = V2.read_text(encoding="utf-8")
linhas = v2txt.splitlines()
ln = lambda padrao: [i + 1 for i, l in enumerate(linhas) if re.search(padrao, l)]
v3 = {"sha_v2_vigente": sha(V2)}
i_bib  = v2txt.find("BIBLIOTECAS CANÔNICAS")
i_evid = v2txt.find("EVIDÊNCIAS", v2txt.find("# 2. VISÃO GERAL"))
v3["diagrama_sec2"] = {
    "evidencias_abaixo_da_biblioteca_no_desenho": i_bib < i_evid,
    "primeira_mencao_EVIDENCIAS_linha": (linhas[: i_evid and v2txt[:i_evid].count("\n") + 1] and v2txt[:i_evid].count("\n") + 1)}
v3["sec53_minidiagrama"] = {
    "padrao": "EVIDÊNCIA BIBLIOGRÁFICA → BIBLIOTECA CANÔNICA → NARRATIVA TRANSVERSAL",
    "linhas": {"EVIDÊNCIA BIBLIOGRÁFICA": ln(r"^EVIDÊNCIA BIBLIOGRÁFICA"),
               "BIBLIOTECA CANÔNICA_no_53": [x for x in ln(r"^BIBLIOTECA CANÔNICA")],
               "NARRATIVA TRANSVERSAL_no_53": [x for x in ln(r"^NARRATIVA TRANSVERSAL")]}}
sec53 = v2txt.find("EVIDÊNCIA BIBLIOGRÁFICA")
v3["sec53_ordem_confere"] = sec53 != -1 and sec53 < v2txt.find("BIBLIOTECA CANÔNICA", sec53) < v2txt.find("NARRATIVA TRANSVERSAL", sec53)
v3["posicao_paralela_so_pasta_atualizacao"] = {
    "ocorrencias_de_posicao_paralela": ln(r"posição paralela à cadeia canônica"),
    "contexto_e_pasta_de_atualizacao": "Pasta de Atualização" in "\n".join(linhas[max(0, (ln(r"posição paralela") or [1])[0] - 3):(ln(r"posição paralela") or [1])[0] + 1])}
v3["sec5_evidentes_nao_segunda_biblioteca"] = {
    "linhas": ln(r"não constituem uma segunda Biblioteca Canônica")}
v3["nt_deveres_1_e_2"] = {
    "consumir_biblioteca": ln(r"1\. consumir o conhecimento da Biblioteca correspondente"),
    "utilizar_evidencias": ln(r"2\. utilizar as Evidências/Vínculos necessárias à rastreabilidade"),
    "leitura": "§5/§8 do comentador = redação vigente da própria V2 (NT consome Biblioteca e usa Evidências/Vínculos)"}
v3["kit_na_V2"] = {k: len(re.findall(pad, v2txt, re.I)) for k, pad in
                   {"kit": r"\bkit\b", "claim kit": r"claim.?kit", "SM-02": r"SM-02", "SCHEMA-CLAIM": r"SCHEMA-CLAIM"}.items()}
v3["caminho_sec51_vs_disco"] = {
    "v2_declara": [l.strip() for l in linhas if "/Evidencias/Bibliograficas" in l],
    "disco_real": "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia (aninhado na B1; nome 'Bibliografia', sem 'cas')",
    "divergencia": "V2 desenha caminho de topo; implantação atual aninhou dentro da B1 — fato nomeado para a decisão da camada"}
R["etapas"]["V3_confronto_V2"] = v3
R["vereditos"]["V3_sec2_evidencias_abaixo"] = v3["diagrama_sec2"]["evidencias_abaixo_da_biblioteca_no_desenho"]
R["vereditos"]["V3_sec53_ordem_confere"] = v3["sec53_ordem_confere"]
R["vereditos"]["V3_paralela_so_pasta_atualizacao"] = v3["posicao_paralela_so_pasta_atualizacao"]["contexto_e_pasta_de_atualizacao"] and len(v3["posicao_paralela_so_pasta_atualizacao"]["ocorrencias_de_posicao_paralela"]) == 1
R["vereditos"]["V3_kit_zero_na_V2"] = all(v == 0 for v in v3["kit_na_V2"].values())
R["vereditos"]["V3_nt_deveres_batem"] = bool(v3["nt_deveres_1_e_2"]["consumir_biblioteca"] and v3["nt_deveres_1_e_2"]["utilizar_evidencias"])

# ---------- V4. §6 usado_em_biblioteca
sch = KIT.joinpath("3º SCHEMA-CLAIM — v1.2.md").read_text(encoding="utf-8").splitlines()
instr = [f"L{i+1}: {sch[i].strip()}" for i in range(len(sch)) if "usado_em_biblioteca" in sch[i] or "claim_id_origem preenchido" in sch[i] or "rastreabilidade de consumo" in sch[i] or "Não" in sch[i] and "bloqueia" in sch[i]]
sm02_fichas = sum(1 for f in fichas if str(f.get("claim_id_origem") or "").startswith("B1.SM02."))
mec_fichas  = sum(1 for f in fichas if str(f.get("claim_id_origem") or "").startswith("B1.MEC."))
R["etapas"]["V4_secao6_usado_em_biblioteca"] = {
    "split_sim_nao": v1["usado_em_biblioteca"]["dist"],
    "instrucao_schema_claim_linhas": instr,
    "fichas_V7_claim_id_origem_SM02": sm02_fichas,
    "fichas_V7_claim_id_origem_MEC": mec_fichas,
    "leitura": "o próprio kit define ub como 'rastreabilidade de consumo rio abaixo' que 'não bloqueia' o fluxo — "
               "o ponto §6 do comentador (ub=nao não é inconsistência) é SUSTENTADO pelo texto do kit; "
               "e é coerente com o dado: sim=0/23 casa com claim_id_origem SM02=0/237 (wiring nunca executado)"}
R["vereditos"]["V4_nao_22_sim_0"] = v1["usado_em_biblioteca"]["dist"] == {"nao": 22}
R["vereditos"]["V4_zero_fichas_SM02"] = sm02_fichas == 0
R["vereditos"]["V4_instrucao_citada"] = any("rastreabilidade de consumo" in s for s in instr)

# ---------- V5. §7 gap_pesquisa × nao_estabelecida
vinc = json.load(open(ATUAL / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json"))
vinc = vinc if isinstance(vinc, list) else vinc["vinculos"]
ne = sorted(x["id_vinculo"] for x in vinc if x.get("natureza_relacao") == "nao_estabelecida")
R["etapas"]["V5_secao7_gap_pesquisa"] = {
    "lado_kit": v1["gap_pesquisa"], "lado_acervo": {"total": len(ne), "ids": ne},
    "leitura": "convergência dos dois lados (D-03, trilha 40) — o comentador endossa; compromisso incondicional: os 4 sobrevivem em qualquer decisão da camada"}
R["vereditos"]["V5_4_x_4"] = len(set(gap_ids)) == 4 and len(ne) == 4

# ---------- V2. §1/§2 aceites
R["etapas"]["V2_secoes1e2_aceites"] = {
    "ancoragem": "fechada na rodada 22 (9/9 pelo mestre) — o comentador apenas registra encerramento",
    "diff": "casa já decidiu adotar as bytes do mestre quando o anexo chegar (rev.28); o pedido dele — "
            "'arquivo efetivamente adotado identificado no registro final' — JÁ É critério da casa: "
            "1 sha viva publicada em decisoes/CHANGELOG/STATUS + backup na cadeia .bak_*"}

# ---------- decisão (registro; não é da casa)
R["etapas"]["decisao_da_camada_registro"] = {
    "opcoes_em_mesa": {
        "(a) mestre/opção-histórica": "kit SUPERSEDED_; 39 PMIDs à curadoria arquivada",
        "(b) mestre/opção-V2": "kit como camada de origem pretendida na V2 (contrato do fio claim→biblioteca)",
        "(c) comentador (NOVA, desta nota)": "kit = ferramenta de curadoria; produto deposita em Evidências/Bibliografia "
            "(eixo tratado como paralelo); SEM nova camada e SEM contrato claim→biblioteca como condição; "
            "rastreabilidade quando houver utilização"},
    "fatos_medidos_relevantes": [
        "kit tem 0 ocorrências na V2 vigente (qualquer opção precisa resolver isso em texto)",
        "fio projetado nas 2 pontas e nunca executado: ub sim 0/23 × claim_id_origem SM02 0/237 (instrução SCHEMA L87-92)",
        "10/49 PMIDs do kit já estão no acervo por OUTRO caminho (pipeline; claim_id_origem B1.MEC.*)",
        "V2 tem DOIS desenhos internos para Evidências: §2 (abaixo da Biblioteca) × §5.3 (a montante, EVIDÊNCIA→BIBLIOTECA) — dívida D-V2-DIAGRAMA-DUPLO nomeada",
        "a topologia de (c) coincide parcialmente com o §5.3 vigente; diverge do §2",
        "o texto do kit não menciona Evidências/Bibliografia (0 ocorrências nos .md do kit — medido nesta rodada): o destino proposto por (c) não está escrito no próprio kit",
        "V2 declara Evidências 'não uma segunda Biblioteca nem fonte independente' × comentador 'eixo paralelo' — nuance de redação a ajustar se (c) for adotada"],
    "dono_da_decisao": "OPERADOR",
    "compromisso_incondicional": "D-03: 4 gap_pesquisa (kit) × 4 nao_estabelecida (acervo) sobrevivem em qualquer opção"}

# ---------- V6. selos 0 ciência
R["etapas"]["V6_selos"] = {
    "V7_canonica": sha(ATUAL / "B1 NEUROINFLAMAÇÃO V7 CANONICA.md"),
    "manifesto": sha(ATUAL / "Evidencias/Bibliografia/_manifesto_biblioteca.json"),
    "P8_oficial": sha(P8),
    "esperados": {"V7": "6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238",
                  "manifesto_prefixo": "79d1309a",
                  "P8": "84fa918d09899d54995ae41d65b0787a7a52888ba6177ce77583483b1124fe8b"}}
R["vereditos"]["V6_V7_intacta"]      = R["etapas"]["V6_selos"]["V7_canonica"] == R["etapas"]["V6_selos"]["esperados"]["V7"]
R["vereditos"]["V6_manifesto_intacto"] = R["etapas"]["V6_selos"]["manifesto"].startswith("79d1309a")
R["vereditos"]["V6_P8_intacto"]      = R["etapas"]["V6_selos"]["P8_oficial"] == R["etapas"]["V6_selos"]["esperados"]["P8"]

TRILHA.write_text(json.dumps(R, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(R["vereditos"], ensure_ascii=False, indent=2))
print("\nuso:", v1["uso"])
print("ub split:", v1["usado_em_biblioteca"]["dist"], "| gap:", v1["gap_pesquisa"]["ids"])
print("pmids:", v1["pmids"]["unicos_kit"], "ún ·", v1["pmids"]["presentes_na_V7"], "na V7 ·", v1["pmids"]["ausentes"], "aus")
print("kit na V2:", v3["kit_na_V2"], "| §5.3 ordem:", v3["sec53_ordem_confere"], "| paralela só pasta-atualização:", v3["posicao_paralela_so_pasta_atualizacao"]["contexto_e_pasta_de_atualizacao"])
print("instrução schema:", *instr, sep="\n  ")
print("selos:", R["etapas"]["V6_selos"]["V7_canonica"][:12], R["etapas"]["V6_selos"]["manifesto"][:12], R["etapas"]["V6_selos"]["P8_oficial"][:12])
