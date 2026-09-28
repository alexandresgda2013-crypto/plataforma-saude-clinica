#!/usr/bin/env python3
# TRILHA 77 — RÉPLICA MECÂNICA FINAL · MINUTA 3 rev.5 L-06 — 2026-09-21
# Pede o comentador (3 testes mecânicos) + a casa (diff integral, emendas, conceito-minuta-1).
# Comando gravado por medida (política da casa). Régua: NFC, linhas-inteiras como âncora, casefold p/ prosa, sha256.
import json, re, hashlib, unicodedata, difflib
from pathlib import Path

B = Path("/home/user"); S = B / "BIBLIOTECAS/_documentos_serie"
R1t = (S / "MESTRE_L06_minuta3_consolidada_rev1_recebida_2026-09-21/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev1_2026-09-21.md").read_text(encoding="utf-8")
R5t = (B / "uploads/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev5_2026-09-21.md").read_text(encoding="utf-8")
M1 = (S / "L06_minuta_mestre_recebida_2026-09-15/L06_RESOLUCAO_CONFLITOS_minuta1_2026-09-15.md").read_text(encoding="utf-8")
R1, R5 = R1t.splitlines(), R5t.splitlines()
def cf(x): return unicodedata.normalize("NFC", x).casefold()
r5, m1 = cf(R5t), cf(M1)
R = []
def ck(k, ok, det):
    R.append({"check": k, "ok": bool(ok), "detalhe": det}); print(("PASS " if ok else "FAIL ") + k + " — " + det)
def H(txt): return hashlib.sha256(txt.encode()).hexdigest()
def cut(lines):
    i = next(k for k, l in enumerate(lines) if l.strip() == "## 2. A ESCADA")
    j = next(k for k, l in enumerate(lines) if l.strip() == "## CRÉDITOS")
    return lines[i:j]
def neut(lines):  # PROCEDIMENTO DECLARADO: apaga o parêntese-final de crédito da linha §6.3 (regex \s*\*([^()]*\)\*\s*$ com âncora "Atribuição por relação"), rstrip na linha
    return [re.sub(r"\s*\*\([^()]*\)\*\s*$", "", l).rstrip() if "Atribuição por relação" in l else l for l in lines]
c1, c5 = cut(R1), cut(R5)
n1, n5 = neut(c1), neut(c5)
hl = lambda ls, trail=True: H("\n".join(ls) + ("\n" if trail else ""))

ck("C01_REV5_MEDIDA", H(R5t) == "601c1f18d074e6e4488dd8a6ee3364345e51713f7d0277cd1637add838a79608" and len(R5t.encode()) == 25581
    and "rev.3 (2026-09-21): retratada pela rev.4" in r5,
    "rev.5 sha=601c1f18 (25.581 b · LF) · nota rev.3 RETRATADA pela rev.4 registrada (2ª retratação do mestre no episódio — crédito de método)")

# C02 diff integral rev.1 × rev.5 — toda diferença confinada às zonas declaradas
zonas_hit, fora = set(), []
marks = {"header-notes": lambda l: l.casefold().startswith(("*rev.", "## minuta 3 · consolidada · rev.")), "proveniencia": lambda l: ("proveni" in l.casefold() or "| minuta 2 do comentador" in l.casefold() or "textoh" in l.casefold() or "8ad6bc15" in l or "1a51d9b9" in l or "frase-ponte" in l.casefold() or "cadeia final" in l.casefold()),
         "creditos": lambda l: ("do comentador, verificado no texto recebido" in l.casefold() or "órfã" in l or "verificado na versão canônica" in l.casefold() or "localizada no textoh" in l.casefold() or "engano à minha minuta 1" in l),
         "rito-rodape": lambda l: (l.casefold().startswith("*rito: esta minuta segue") or "estado documental atual" in l.casefold() or "nota histórica" in l.casefold() or "recorte §2-§13 comparado" in l)}
for l in difflib.unified_diff(R1, R5, lineterm=""):
    if l.startswith(("+", "-")) and not l.startswith(("+++", "---")):
        corpo = l[1:]
        if "Atribuição por relação" in corpo: zonas_hit.add("linha-§6.3")
        elif any(f(corpo) for f in marks.values()): [zonas_hit.add(k) for k, f in marks.items() if f(corpo)]
        elif corpo.strip() == "": pass
        else: fora.append(corpo)
ck("C02_DIFF_ZONAS", not fora and "linha-§6.3" in zonas_hit,
   f"toda diferença rev.1→rev.5 confinada em: {sorted(zonas_hit)} · fora das zonas: {len(fora)} → **conteúdo normativo §0–§13 (exceto a nota §6.3) byte-idêntico** o restante do corpo")

ck("C03_EMENDAS", "conceito: minuta 1 do mestre, §4" in r5 and "redação desta frase: comentador" in r5
    and "localizada no textoh" in r5 and "(não no textom" in r5 and "a casa mediu 0× nela e corrige a favor do comentador" in r5
    and "frase-ponte de proveniência (rev.2)" in r5,
    "3 emendas da carta 23 presentes e na forma acordada + auto-correção do mestre nos CRÉDITOS ('a casa mediu 0× nela e corrige a favor do Comentador') registrada")

# C04 CONCEITO minuta 1 — C77-1
l97 = M1.splitlines()[96]
ck("C04_CONCEITO_M1", "atribuídos por relação**" in l97 and "não por posição" in l97,
    "M1 l.97: 'rótulos **atribuídos por relação**, não por posição' — o CONCEITO é do mestre e está na minuta 1 · forma-verbo encorpada ('Atribuição por relação, nunca por posição' como regra) é do TextoH → a partilha da rev.5 está CERTA · C77-1: réguas das trilhas 74/75 usavam 'atribui' (7 letras) e ficaram cegas à flexão 'atribuídos' — o '0×' valia só para a frase exata; confissão datada e registrada na ata")

# C05 recorte — pedido 2
chg = [l for l in difflib.unified_diff(c1, c5, lineterm="") if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]
ok5 = len(c1) == len(c5) == 186 and len(chg) == 2 and all("Atribuição por relação" in l for l in chg)
ck("C05_PEDIDO2_UMADIF", ok5, f"recortes §2–§13 (âncora linha-inteira) = 186 linhas nos dois · diff bruto = {len(chg)} linhas (−1/+1), TODAS na linha §6.3 → **exatamente UMA diferença: a nota de crédito** ✔")

# C06 neutralizado — pedido 1 (propriedade)
h_n = hl(n5)
ck("C06_PEDIDO1_IGUAIS", n1 == n5 and hl(n5) == hl(n1) and hl(n5, False) == hl(n1, False),
   f"neutralizados (procedimento declarado) byte-idênticos · digital-da-igualdade da casa = {h_n} (com \\n final; {hl(n5, False)[:8]} sem) → propriedade VERIFICADA com comando gravado")

# C07 com-nota — pedido 3
h5b, h1b = hl(c5), hl(c1)
ck("C07_PEDIDO3_COMNOTA", h5b.startswith("c863b8ed") and h1b.startswith("8a8ff986"),
   f"rev.5-com-nota = {h5b[:8]} ✔ · rev.1-com-nota = {h1b[:8]} ✔ — batem EXATO com os publicados; bônus: prova byte-a-byte de que a rev.1 == minuta 3 ORIGINAL dentro do recorte (a nota da rev.1 verificada pela 1ª vez)")

# C08 valores 95c7cb41/f8ec8b72 — status honesto
ck("C08_HASH_IDENTIDADE_DELES", "95c7cb41" not in R5t and "f8ec8b72" in R5t,
   "na rev.5: 95c7cb41 0× · f8ec8b72 só na nota histórica da rev.4 (rev.5 inteira lida) · bateria da casa: 6 procedimentos de neutralização × 4 serializações, nenhum reproduz 95c7cb41/f8ec8b72 → VEREDITO: a IGUALDADE está verificada (C06, digital da casa); o VALOR ESPECÍFICO deles exige o comando exato (pedido ao mestre) ou fica substituído pela digital da casa · comentador correto no zelo: f8ec8b72 deve ser marcado 'intermediário' quando houver toque editorial — não é normativo (concorda-se)")

ck("C09_NORMATIVO", all(x in R5t for x in ["**244**", "T-23", "resolutivo — 1, 2, 3 ou 4", "D-L05-GRANULARIDADE-OBJETO", "ancoras[].condicao", "marcador × nao_estabelecida` como candidato"]),
   "núcleo normativo presente e inalterado (gatilho · 244 · matriz · suíte 23 · degradada resolutivo/qualificador · §7) — conferido também pelo diff C02")

ck("C10_RITO", "réplica da casa e, depois, aprovação do operador" in r5,
   "rito na rev.5 conforme o combinado · estado: proposta consolidada ainda não vigente (a casa não estampa rótulo em peça própria)")

ck("C11_PROVENIENCIA_TAB", "| minuta 2 do comentador — textom canônico | primeiro recebido como texto colado; **versão canônica depois entregue em arquivo e arquivada pela casa** | `8ad6bc15" in r5
    and "| minuta 2 do comentador — textoh rascunho (o que a casa cruzou) | arquivado pela casa | `1a51d9b9…`" in r5,
   "tabela de proveniência reflete o estado pós-entrega (TextoM com digital plena · TextoH distinto) · frase-ponte presente (emenda 3)")

res = {"trilha": 77, "data": "2026-09-21", "objeto": "réplica mecânica final — minuta 3 rev.5 L-06",
       "sha_rev5": H(R5t), "digital_igualdade_casa": h_n, "rev1_comnota": h1b, "rev5_comnota": h5b,
       "verdes": sum(1 for r in R if r["ok"]), "total": len(R), "checks": R,
       "confissoes": ["C77-1: réguas das trilhas 74/75 pesquisaram 'atribui' (7 letras) e ficaram cegas à flexão 'atribuídos' — o '0× na minuta 1' valia apenas para a frase verbo encorpada; o CONCEITO existe na l.97 da minuta 1 ('rótulos atribuídos por relação, não por posição'). A partilha da rev.5 (conceito: M1 · redação: Comentador) está correta e a casa a subscreve, corrigindo a própria ata.",
                        "C77-2: 1ª leitura do recorte caiu na CITAÇÃO dos marcadores dentro da nota histórica da rev.4 ('## 2. A ESCADA…## CRÉDITOS' inline) — corrigida com âncoras de linha-inteira antes de qualquer conclusão (a falha apareceu e morreu dentro da mesma sessão de medição)."]}
Path(__file__).with_suffix(".json").write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nRESULTADO: {res['verdes']}/{res['total']} verdes")
