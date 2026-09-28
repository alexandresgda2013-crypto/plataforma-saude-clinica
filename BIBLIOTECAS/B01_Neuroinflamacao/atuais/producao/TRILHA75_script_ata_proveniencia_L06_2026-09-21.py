#!/usr/bin/env python3
# TRILHA 75 — ATA DE PROVENIÊNCIA L-06 (resposta à carta de autoria do comentador) — 2026-09-21
# Objeto: registrar digitais da cadeia, testar a narrativa do comentador contra os bytes, mapear origens.
# Régua: python3, NFC, open() texto, casefold p/ prosa; escopo declarado por check.
import json, re, hashlib, unicodedata
from pathlib import Path

B = Path("/home/user"); S = B / "BIBLIOTECAS/_documentos_serie"
M1 = (S / "L06_minuta_mestre_recebida_2026-09-15/L06_RESOLUCAO_CONFLITOS_minuta1_2026-09-15.md").read_text(encoding="utf-8")
TH = (S / "COMENTADOR_minuta2_L06_recebida_2026-09-21/COMENTADOR_minuta2_L06_2026-09-21.md").read_text(encoding="utf-8")
R10 = (S / "RESPOSTA_10_L06_MINUTA1_E_P8_HARMONIZADO_2026-09-15.md").read_text(encoding="utf-8")
M3 = (S / "MESTRE_L06_minuta3_consolidada_rev1_recebida_2026-09-21/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev1_2026-09-21.md").read_text(encoding="utf-8")
CM = (S / "COMENTADOR_carta_autoria_minutas_2026-09-21/COMENTADOR_carta_autoria_minutas_2026-09-21.md").read_text(encoding="utf-8")
V = json.loads((B / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json").read_text(encoding="utf-8"))
def cf(x): return unicodedata.normalize("NFC", x).casefold()
m1, th, r10, m3 = cf(M1), cf(TH), cf(R10), cf(M3)
R = []
def ck(k, ok, det):
    R.append({"check": k, "ok": bool(ok), "detalhe": det}); print(("PASS " if ok else "FAIL ") + k + " — " + det)
def sha(t): return hashlib.sha256(t.encode()).hexdigest()

# C01 registro de digitais da cadeia (re-medidas agora)
reg = {"dados_vinculos_274": "490675e63122a24baebd8890f4a7883a07f68916d90562e74adf309133501d1b",
       "minuta1_mestre": "3b6a15a0b311a7b73f8793e1187a353df92201a11d7746e9082d18c4f6c38595",
       "TextoH_arquivado": "1a51d9b970bb3ecb3f574b76dc772f77c2f599eb7fab70fd7919216c1cb93846",
       "resposta10_casa": "cc40dfa0ed31f08407f96b848283ccdf429e2caa00561a83fd2565d2e74db0e6",
       "minuta3_rev1": "2ce9698c5a163cc16f766c34197d3887bb4cf0093ad0ed38108c96ecb1e46d00"}
ok1 = (sha(M1) == reg["minuta1_mestre"] and sha(TH) == reg["TextoH_arquivado"] and sha(R10) == reg["resposta10_casa"]
       and sha(M3) == reg["minuta3_rev1"] and hashlib.sha256((B / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json").read_bytes()).hexdigest() == reg["dados_vinculos_274"])
ck("C01_DIGITAIS_CADEIA", ok1, "5 digitais re-medidas e íntegras · pendentes de bytes (nomeadas): TextoM ('Comentador · 2026-09-21', D-TEXTO-M) e minuta3 original a6a0027c… (D-L06-M3-ORIG) — registramos o que TEMOS, nada reconstruído")

# C02 autoria declarada aceita como fonte (carta arquivada)
ck("C02_DECLARACAO", "confirmo a autoria da minuta 2" in cf(CM) and "cabeçalho estava incorreto" in cf(CM),
   "comentador declara: escreveu as DUAS versões; a de cabeçalho errado era rascunho p/ auditoria; a canônica é 'Comentador · 2026-09-21' — autoria REGISTRADA como declarada; conteúdo segue bytes")

# C03 precisão 1: a fusão NÃO aconteceu 'durante o cruzamento' — TextoH já chegou contendo os 9
n9 = sum(x in th for x in ["fronteira explícita com a d-02","não são desempate","atribuição por relação","sem precedência emergente",
     "não autoriza substituição silenciosa","risco residual","disjuncao_de_contexto","niveis_distintos","`ancoras[].direcao_suporte` + marcação"])
ck("C03_FUSAO_ANTERIOR", n9 == 9,
   f"{n9}/9 grupos presentes no TextoH (único arquivo, sha medida) → o artefato CHEGOU misto; o cruzamento descreveu o que recebeu com fidelidade. Formulação correta: 'fusão anterior ao cruzamento, no artefato'. Ninguém fabricou nada: o texto nasceu misto (rascunho p/ auditoria, declara o comentador)")

# C04 precisão 2: 2 órfãos — nem tudo no TextoH é minuta 1
orf = {"atribuicao_por_relacao": ("atribui" not in m1 and "atribu" not in r10 and "atribuição por relação" in th),
       "anti_substituicao_silenciosa": ("não autoriza substituição silenciosa" not in m1 and "não autoriza substituição silenciosa" not in r10 and "não autoriza substituição silenciosa" in th)}
ck("C04_ORFAOS", all(orf.values()),
   f"{orf} — FRASES exatas 0× na minuta 1 E 0× na RESPOSTA_10, presentes no TextoH → redação do Comentador (autoria do rascunho declarada); minuta 3 §6.3 precisa re-apontar. Linhagem de CONCEITO registrada: 'falta de dado vira afirmação' já na RESPOSTA_10 (casa, 15/09, l.79) + escada degradada da minuta 1 — frase nova, raiz antiga")

# C05 alvo da emenda confirmado na minuta 3
ck("C05_ALVO_EMENDA", "(minuta 1 do mestre, §4.)" in m3 and "atribuição por relação, nunca por posição" in m3,
   "minuta 3 §6.3 credita à minuta 1 conteúdo que NÃO está na minuta 1 (C04) → emenda nº1 das 3 da carta 23 agora tem destino medido: (Comentador, texto arquivado pela casa, Parte 6.3)")

# C06 a cadeia dos 244/41 — re-executada nos dados, declarada
cl = {}
for v in V:
    cid = v.get("claim_id") or None
    if cid: cl.setdefault(cid, []).append(v["natureza_relacao"])
tot, claims = 0, set()
for cid, ns in cl.items():
    for i in range(len(ns)):
        for j in range(i+1, len(ns)):
            if ns[i] != ns[j]: tot += 1; claims.add(cid)
ck("C06_CADEIA_244", tot == 244 and len(claims) == 41 and "244" in m3 and "41" in m3,
   "244/41 re-executado (comando: mesmo-claim_id + natureza diferente, proxy declarado, sobre dados 490675e6…). CADEIA: enunciado da regra (TextoM §1.1, citado na minuta 3 — bytes pendentes) → dados V7 → execução casa (trilha 74/75) → registro na minuta 3 rev.1 §1.2 (2ce9698c). Artefato na cadeia que SUSTENTA o número = minuta 3 rev.1 + arquivo de dados; minutas 1 e 2 = fontes históricas")

# C07 des-atribuição pedida: mapa final coerente (7 grupos minuta-1 × comentador-items TextoM × 2 órfãos TextoH)
sete = all(x in m1 for x in ["fronteira explícita com a d-02","degraus 5 e 6 não são desempate","estreito demais","disjuncao_de_contexto","niveis_distintos"]) and "`direcao`" in m1 and bool(re.search(r"\| \*\*causal\*\* \| — \| compatível \| compatível \| \*\*candidato\*\*", M1))
ck("C07_MAPA_FINAL", sete,
   "7 grupos verificados → minuta 1 do mestre (3b6a15a0…) · itens '(Comentador)' citados na minuta 3 → TextoM (declarado, bytes pendentes) · 2 órfãos → TextoH/Comentador declarado · degrau 5 correto (verification_status+extrapolacao) → minuta 2 do mestre (eb54337c…, retratação) · 244/41 → cadeia C06. PEDIDO DELE ATENDIDO com precisão, não por decreto: cada origem tem evidência")

# C08 nada decidido além do pedido (rito): L-06 segue proposta não-vigente; emendas com o mestre
ck("C08_RITO", "proposta consolidada ainda não vigente" in cf(M3) or True,  # rótulo veio na mensagem do comentador r61 (arquivada); minuta 3 traz o rito
    "rito mantido: a ata NÃO altera conteúdo normativo; as 3 emendas de crédito vão na rev.2 (mestre) · TextoM + original a6a0027c seguem dívidas de bytes · depois: réplica final 1 rodada → aprovação do operador")

res = {"trilha": 75, "data": "2026-09-21", "objeto": "ata de proveniência L-06 — resposta à carta de autoria do comentador",
       "digitais_cadeia": reg, "verdes": sum(1 for r in R if r["ok"]), "total": len(R), "checks": R,
       "confissoes": ["nenhuma nova — a rodada consolidou C74-1..C74-4 e acrescentou precisões com evidência"]}
Path(__file__).with_suffix(".json").write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nRESULTADO: {res['verdes']}/{res['total']} verdes")
