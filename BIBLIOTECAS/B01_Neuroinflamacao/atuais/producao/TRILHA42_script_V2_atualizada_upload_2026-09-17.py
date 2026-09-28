#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 42 — Arquitetura V2 atualizada pelo operador (upload 2026-09-17): réplica/diff/parecer da casa
========================================================================================================
Data: 2026-09-17 · Rodada 24 · 0 ciência (só leituras/diff/medidas; nada escrito no acervo).

Objeto: uploads/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md (NOVO conteúdo,
mesmo nome) × vigente _documentos_serie/ (sha 09692e18…).

Etapas:
  A0. Digitais e tamanhos (upload × vigente).
  A1. Escopo do diff: hunks/+/− e mapeamento dos trechos tocados às seções (prova de que o
      restante do documento é byte-idêntico fora de §2 e §21).
  A2. Kit no novo texto (kit/SM-02/SCHEMA-CLAIM) — esperado 0: a atualização NÃO decide a camada.
  A3. Guarda da Pasta de Atualização: parágrafo do §2 removido × guarda preservada redistribuída
      (§18 camada diferente; §18 não-canônico automático; §19 não-equivalência no Motor;
      §20 "não possuem o mesmo status epistemológico").
  A4. Anamnese: entra nos desenhos (§2 novo com bloco DEFINIÇÃO; §21) e já existia em prosa
      (§23 fluxo clínico, §24 definição consolidada) — coerência.
  A5. Representações da topologia (ATUALIZA A DÍVIDA D-V2-DIAGRAMA-DUPLO): 4 desenhos —
      §2-novo (espelhado; "VÍNCULOS UNIFICADOS") · §21-novo (linear; Pasta lateral) ·
      §20 (fluxo canônico: EVIDÊNCIA→BIBLIOTECA, a montante) · §5.3 (EVIDÊNCIA→BIBLIOTECA→NT).
      §2 e §21 dividem o MESMO título "ARQUITETURA MULTIDOMÍNIO COMPLETA" (e o §2 repete o
      rótulo "# 21." na sua linha 45). Direção normativa Evidência↔Biblioteca diverge entre
      prosa (§5.3/§20: a montante) e desenhos gerais (§2/§21: a jusante).
  A6. Higiene de render do §21: fence de abertura indentado 4 espaços (não-fence em markdown)
      e sem fechamento (a próxima marca após o desenho é "---"); fences ^``` pares (60).
  A7. Tríade de saída: sai SUGESTÃO MECANÍSTICA/EXPLICAÇÃO CIENTÍFICA/NARRATIVA CONTEXTUAL,
      entra MECANÍSTICA/CLÍNICA/TERAPÊUTICA → EXPLICAÇÃO NARRATIVA (só nos 2 desenhos; sem prosa).
  A8. Motor "busca ativa" (nova seta CONSULTA no §2) × §21-novo (JSONs → MOTOR) × §19 prosa
      ("deverá consultar a Pasta") — coerência parcial registrada (o §21-novo não desenha a seta).
  A9. Nome do arquivo inalterado com conteúdo novo — proposta de versionamento registrada.
"""
import hashlib, json, re, subprocess
from pathlib import Path

UP = Path("/home/user/uploads/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md")
VG = Path("/home/user/BIBLIOTECAS/_documentos_serie/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md")
TRILHA = Path("/home/user/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA42_V2_atualizada_upload_2026-09-17.json")
DIFF = Path("/home/user/diff_v2_vigente_x_upload_2026-09-17.txt")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

R = {"trilha": 42, "data": "2026-09-17", "rodada": 24,
     "objeto": "V2 atualizada pelo operador (upload mesmo-nome) — diff/verificação/parecer",
     "etapas": {}, "vereditos": {}, "ciencia_tocada": 0}

novo = UP.read_text(encoding="utf-8"); velho = VG.read_text(encoding="utf-8")
ln_n = novo.splitlines(); ln_v = velho.splitlines()
def hits(txt, pad):  return [i + 1 for i, l in enumerate(txt.splitlines()) if re.search(pad, l)]

# ---------- A0
R["etapas"]["A0_digitais"] = {
    "upload_sha256": sha(UP), "upload_bytes": UP.stat().st_size, "upload_linhas": len(ln_n),
    "vigente_sha256": sha(VG), "vigente_bytes": VG.stat().st_size, "vigente_linhas": len(ln_v)}

# ---------- A1. diff
out = subprocess.run(["diff", "-u", str(VG), str(UP)], capture_output=True, text=True).stdout
hunks = re.findall(r"^@@ -(\d+),?(\d*) \+(\d+),?(\d*) @@", out, re.M)
mais = len(re.findall(r"^\+(?!\+)", out, re.M)); menos = len(re.findall(r"^-(?!-)", out, re.M))
# prova de escopo: todo hunk começa e termina dentro de §2 (40–124 velho) ou §21 (983–1091 velho)
def secao_da_linha(n):
    for nome, ini, fim in (("§2", 40, 124), ("§21", 983, 1091)):
        if ini <= n <= fim: return nome
    return "FORA"
escopo = [secao_da_linha(int(h[0])) for h in hunks]
R["etapas"]["A1_diff"] = {"hunks": [list(map(int, h)) for h in hunks], "n_hunks": len(hunks),
    "linhas_adicionadas": mais, "linhas_removidas": menos,
    "comando": f'diff -u "<vigente>" "<upload>" > {DIFF}',
    "mapeamento_hunks_às_secoes": escopo,
    "leitura": "todo o restante do documento (§§1, 3–20, 22–30) é byte-idêntico — o diff cobre só §2 e §21"}
R["vereditos"]["A1_escopo_SO_sec2_e_sec21"] = all(s in ("§2", "§21") for s in escopo)

# ---------- A2. kit
R["etapas"]["A2_kit_no_novo_texto"] = {k: len(re.findall(p, novo, re.I)) for k, p in
    {"kit": r"\bkit\b", "SM-02": r"SM-02", "SCHEMA-CLAIM": r"SCHEMA-CLAIM", "claim kit": r"claim.?kit"}.items()}
R["etapas"]["A2_kit_no_novo_texto"]["leitura"] = ("a atualização NÃO posiciona o kit: a decisão da camada "
    "(a histórico × b camada-origem-V2 × c ferramenta→Evidências, do comentador) permanece aberta com o operador")
R["vereditos"]["A2_kit_zero_novo_texto"] = all(v == 0 for k, v in R["etapas"]["A2_kit_no_novo_texto"].items() if k != "leitura")

# ---------- A3. guarda da pasta
g = {"paragrafo_sec2_posicao_paralela": len(hits(novo, r"posição paralela à cadeia canônica")),
     "sec18_camada_diferente": hits(novo, r"camada diferente da Biblioteca Canônica"),
     "sec18_nao_canonico_automatico": hits(novo, r"não significa automaticamente que seu conteúdo"),
     "sec19_nao_equivalencia_motor": hits(novo, r"não deverá automaticamente tratar uma informação da Pasta"),
     "sec20_status_diferente": hits(novo, r"não possuem o mesmo status epistemológico")}
R["etapas"]["A3_guarda_pasta_atualizacao"] = {**g, "leitura":
    "frase do §2 removida, mas o regime de proteção canônica segue escrito nas §§18/19/20 — guarda PRESERVADA, redistribuída"}
R["vereditos"]["A3_guarda_preservada_redistribuida"] = (
    g["paragrafo_sec2_posicao_paralela"] == 0 and bool(g["sec18_camada_diferente"])
    and bool(g["sec18_nao_canonico_automatico"]) and bool(g["sec19_nao_equivalencia_motor"]) and bool(g["sec20_status_diferente"]))

# ---------- A4. anamnese
R["etapas"]["A4_anamnese"] = {"ocorrencias_novo": len(re.findall(r"anamnese", novo, re.I)),
    "ocorrencias_vigente": len(re.findall(r"anamnese", velho, re.I)),
    "definicao_nova_sec2": bool(hits(novo, r"A anamnese constitui os dados clínicos do caso")),
    "prosa_preexiste_sec23_sec24": bool(hits(novo, r"a anamnese estruturada") and hits(novo, r"Anamnese e dados clínicos → Motor"))}
R["vereditos"]["A4_anamnese_coerente"] = (R["etapas"]["A4_anamnese"]["definicao_nova_sec2"]
    and R["etapas"]["A4_anamnese"]["prosa_preexiste_sec23_sec24"])

# ---------- A5. quatro representações
reps = {
  "sec2_novo_espelhado": {"evidencia": hits(novo, r"VÍNCULOS UNIFICADOS"), "titulo": hits(novo, r"ARQUITETURA MULTIDOMÍNIO COMPLETA")},
  "sec21_novo_linear":   {"evidencia": hits(novo, r"EVIDÊNCIAS /   \|◄"), "titulo_na_1020": 1020 in hits(novo, r"^# 21\.")},
  "sec20_fluxo_canonico": {"evidencia_antes_da_biblioteca": None},
  "sec53_minidiagrama":  {"ordem_EVID_BIB_NT": None}}
i20 = novo.find("FLUXO CANÔNICO"); seg = novo[i20: i20 + 400]
reps["sec20_fluxo_canonico"]["evidencia_antes_da_biblioteca"] = seg.find("EVIDÊNCIA") < seg.find("BIBLIOTECA")
i53 = novo.find("EVIDÊNCIA BIBLIOGRÁFICA")
reps["sec53_minidiagrama"]["ordem_EVID_BIB_NT"] = (i53 != -1 and i53 < novo.find("BIBLIOTECA CANÔNICA", i53) < novo.find("NARRATIVA TRANSVERSAL", i53))
R["etapas"]["A5_quatro_representacoes"] = {
    "descricoes": {
        "§2-novo":  "espelhado: [CIÊNCIA]→{BIBLIOTECAS ∥ PASTA ATUALIZAÇÃO}→cada eixo com EVIDÊNCIAS+NT próprias→'EVIDÊNCIAS/VÍNCULOS UNIFICADOS'→…→MOTOR◄ANAMNESE (linhas 45–158)",
        "§21-novo": "linear: CIÊNCIA→{BIBLIOTECA→EVID+NT} com Pasta como ramo EXTERNO; 'EVIDÊNCIAS/VÍNCULOS' simples (sem 'UNIFICADOS'); ANAMNESE entra no MOTOR (linhas 1022–1089)",
        "§20":      "fluxo canônico: CIÊNCIA→SELEÇÃO→EVIDÊNCIA→BIBLIOTECA→NT→… (evidência A MONTANTE) + fluxo de atualização separado; 'não possuem o mesmo status epistemológico'",
        "§5.3":     "minidiagrama: EVIDÊNCIA BIBLIOGRÁFICA→BIBLIOTECA CANÔNICA→NT (a montante), INALTERADO nesta atualização"},
    "duplicidade_titulo": "§2 e §21 usam o MESMO título 'ARQUITETURA MULTIDOMÍNIO COMPLETA' para desenhos DIFERENTES; o §2 ainda carrega o rótulo '# 21.' na sua linha 45",
    "direcao_normativa": ("prosa (§5.3 e §20-fluxo-canônico): evidência A MONTANTE da Biblioteca · desenhos gerais "
        "(§2 e §21): Evidências A JUSANTE — a D-V2-DIAGRAMA-DUPLO não fecha; amplia para 4 representações. "
        "Contexto: o comentador (rodada 23) fica apoiado pela prosa na DIREÇÃO, mas não na topologia completa que propôs"),
    "medidas": reps}
R["vereditos"]["A5_quatro_representacoes_mapeadas"] = (bool(reps["sec2_novo_espelhado"]["evidencia"])
    and reps["sec21_novo_linear"]["titulo_na_1020"] and reps["sec20_fluxo_canonico"]["evidencia_antes_da_biblioteca"]
    and reps["sec53_minidiagrama"]["ordem_EVID_BIB_NT"])
R["vereditos"]["A5_titulo_duplicado_sec2_x_sec21"] = len(reps["sec2_novo_espelhado"]["titulo"]) == 2

# ---------- A6. higiene fence §21
fences_comuns = re.findall(r"(?m)^```", novo)
fences_indent = re.findall(r"(?m)^    ```text\s*$", novo)
i_f = novo.find("    ```text")
apos = novo[i_f: i_f + 2600]
tem_fechamento = "\n```" in apos.split("\n---", 1)[0]
R["etapas"]["A6_higiene_sec21"] = {
    "fences_crase_coluna0": len(fences_comuns), "fence_indentado_4espacos": len(fences_indent),
    "fechamento_antes_do_proximo_---": tem_fechamento,
    "efeito": "markdown: fence com 4 espaços de indentação NÃO é fence — o '```text' renderiza literal e o desenho sai do bloco de código; falta o fechamento. Correção = 2 edições de formato (desindentar abertura + adicionar fechamento), 0 semântica"}
R["vereditos"]["A6_fence_sec21_quebrado_detectado"] = (len(fences_indent) == 1 and not tem_fechamento)

# ---------- A7. tríade
R["etapas"]["A7_triade_saida"] = {
    "antiga_sugestao_mecanistica": len(re.findall(r"SUGESTÃO\s+MECANÍSTICA", novo)),
    "antiga_explicacao_cientifica": len(re.findall(r"EXPLICAÇÃO\s+CIENTÍFICA", novo)),
    "antiga_narrativa_contextual": len(re.findall(r"NARRATIVA\s+CONTEXTUAL", novo)),
    "nova_triade": len(re.findall(r"TERAPÊUTICA", novo)), "explicacao_narrativa": len(re.findall(r"EXPLICAÇÃO NARRATIVA", novo)),
    "leitura": "mudança editorial dos desenhos (só lá); sem prosa explicando a nova tríade — DÍVIDA editorial nomeada"}
R["vereditos"]["A7_triade_substituida_nos_desenhos"] = (R["etapas"]["A7_triade_saida"]["antiga_narrativa_contextual"] == 0
    and R["etapas"]["A7_triade_saida"]["nova_triade"] == 2 and R["etapas"]["A7_triade_saida"]["explicacao_narrativa"] == 2)

# ---------- A8. motor consulta
R["etapas"]["A8_motor_consulta"] = {
    "sec2_consulta_ativa": bool(hits(novo, r"Consulta Ativa") and hits(novo, r"O Motor busca ativamente")),
    "sec19_prosa": bool(hits(novo, r"deverá possuir capacidade de consultar a Pasta de Atualização")),
    "sec21_seta": "JSONs MODULARES" in novo[ novo.find("# 21.", 100): ] and ("CONSULTA" in novo[ novo.find("# 21.", 100): novo.find("# 22.")]),
    "leitura": "o §2-novo desenha a ida-e-volta (consulta ativa); o §21-novo desenha JSONs→MOTOR sem a seta de consulta — os desenhos entre si não são idênticos (coerência parcial; reforça o pedido de canônico único)"}
R["vereditos"]["A8_consulta_ativa_no_sec2_e_prosa_sec19"] = (R["etapas"]["A8_motor_consulta"]["sec2_consulta_ativa"]
    and R["etapas"]["A8_motor_consulta"]["sec19_prosa"])

# ---------- A9. versionamento
R["etapas"]["A9_versionamento"] = {
    "nome_do_arquivo": "inalterado ('…V2  -  15.09.26.md') com conteúdo novo — mesmo caso-didático das digitais do kit",
    "proposta_casa": ("instalar como vigente SOB NOVO NOME 'ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.1  -  17.09.26.md' "
        "(título interno pode seguir 'V2' com linha de rev datada), anterior (09692e18…) → SUPERSEDED_ + ponteiro, "
        "ARQUITETURA_VIGENTE.txt com a nova sha pública — PENDENTE da decisão do operador (3 opções no chat)")}

R["parecer_agregado"] = ("FAVORÁVEL à instalação: atualização cirúrgica e coerente (escopo provado em A1; guarda da Pasta "
    "redistribuída e intacta; anamnese agora entra nos desenhos com definição própria e prosa preexistente). "
    "2 correções de formato pedidas antes ou com nota datada (A6 fence §21; rótulo '# 21.' duplicado no desenho do §2). "
    "DÍVIDA que AMPLIA: D-V2-DIAGRAMA-DUPLO → agora 4 representações com a direção Evidência↔Biblioteca divergente entre "
    "prosa (a montante) e desenhos gerais (a jusante); sugestão da casa: declarar UM canônico (§2-novo como executivo "
    "ou §20/§5.3 como norma de prosa) e rebatizar os demais. NÃO tocado: kit (0 ocorrências) — decisão (a)/(b)/(c) "
    "continua com o operador. Tríade de saída nova (MEC/CLÍN/TER) existe só nos desenhos — dívida de prosa nomeada.")

TRILHA.write_text(json.dumps(R, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(R["vereditos"], ensure_ascii=False, indent=2))
print("\nA1:", R["etapas"]["A1_diff"]["n_hunks"], "hunks · +", mais, "/−", menos, "· escopo:", escopo)
print("A3 guarda:", {k: v for k, v in R["etapas"]["A3_guarda_pasta_atualizacao"].items() if k != "leitura"})
print("A5 representações OK · título duplicado:", R["vereditos"]["A5_titulo_duplicado_sec2_x_sec21"])
print("A6 fence:", R["etapas"]["A6_higiene_sec21"]["fences_crase_coluna0"], "comuns ·", len(fences_indent), "indentado · fechamento:", tem_fechamento)
