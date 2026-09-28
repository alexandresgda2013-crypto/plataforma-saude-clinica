#!/usr/bin/env python3
# TRILHA 74 — PARECER SOBRE MINUTA 3 CONSOLIDADA REV.1 + PEDIDO DO COMENTADOR (proveniência, A/B/C) — 2026-09-21
# Régua: python3, NFC, open() texto, casefold p/ prosa, igualdade exata p/ enums/ids. Escopo declarado por check.
import json, re, hashlib, unicodedata
from pathlib import Path

B = Path("/home/user"); SERIE = B / "BIBLIOTECAS/_documentos_serie"
M3 = (B / "uploads/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev1_2026-09-21.md").read_text(encoding="utf-8")
TH = (SERIE / "COMENTADOR_minuta2_L06_recebida_2026-09-21/COMENTADOR_minuta2_L06_2026-09-21.md").read_text(encoding="utf-8")
M1 = (SERIE / "L06_minuta_mestre_recebida_2026-09-15/L06_RESOLUCAO_CONFLITOS_minuta1_2026-09-15.md").read_text(encoding="utf-8")
L5 = (SERIE / "L05_1.1_minuta_mestre_recebida_2026-09-15/L05_1.1_CONTRATO_CADEIA_MOTOR_minuta1_2026-09-15.md").read_text(encoding="utf-8")
V = json.loads((B / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json").read_text(encoding="utf-8"))
cat = (B / "Ferramentas de geração e auditoria/01_norteadores/_derivados_trilha46/_ids_oficiais.json").read_text(encoding="utf-8")
def cf(s): return unicodedata.normalize("NFC", s).casefold()
m3, th, m1, l5 = cf(M3), cf(TH), cf(M1), cf(L5)
R = []
def ck(k, ok, det):
    R.append({"check": k, "ok": bool(ok), "detalhe": det}); print(("PASS " if ok else "FAIL ") + k + " — " + det)

h3 = hashlib.sha256(M3.encode()).hexdigest()
ck("C01_M3_MEDIDA", h3 == "2ce9698c5a163cc16f766c34197d3887bb4cf0093ad0ed38108c96ecb1e46d00" and len(M3.encode()) == 21729
    and "proveniência das entradas" in m3 and "créditos" in m3 and "réplica da casa" in m3,
    f"minuta3 rev.1 sha={h3[:8]} ({len(M3.encode())} b · {len(M3)} ch UTF-8 · seções-chave presentes · rev.1 declara mudar só proveniência (original a6a0027c sem bytes na casa → D-L06-M3-ORIG)")

ck("C02_MINUTA1_SHA", hashlib.sha256(M1.encode()).hexdigest() == "3b6a15a0b311a7b73f8793e1187a353df92201a11d7746e9082d18c4f6c38595",
    "digital declarada pelo mestre CONFERE — arquivada pela casa em 15/09 (regex: arquivo da série) · C74-2: rev.64 dizia 'nunca chegou': ERRADO, confissão datada")

# C03: proveniência-9 contra bytes da minuta 1 (linhas medidas na exploração; re-checadas aqui)
itens = {"degrau5_direcao": "`direcao` / marcação `[extrapolado]`" in m1,
         "matriz_celula": bool(re.search(r"\| \*\*causal\*\* \| — \| compatível \| compatível \| \*\*candidato\*\*", M1)),
         "fronteira_d02": "fronteira explícita com a d-02" in m1,
         "5e6_nao_desempate": "degraus 5 e 6 não são desempate" in m1,
         "risco_estreito": "estreito demais" in m1,
         "saidas": "disjuncao_de_contexto" in m1 and "niveis_distintos" in m1,
         "rastro": "campo ausente" in m1 or "indisponivel" in m1}
n_ok = sum(itens.values())
ck("C03_PROVENIENCIA_9", n_ok == 7, f"{n_ok}/7 grupos ENUMERADOS pelo mestre verificados nos bytes da minuta 1 {itens} — achado VERDADEIRO nesses; a linha 'Parte 8 anti-substituição' da TABELA ficou fora da enumeração dele e de fato 0× na minuta 1 (registrar); 'atribuição por relação' falha separada no C04")

# C04: a única célula FALSA do achado — 'atribuição por relação' NÃO está na minuta 1; está no TextoH
ck("C04_CELULA_FALSA", "atribui" not in m1 and "atribuição por relação" in th,
   "'atribuição por relação (nunca por posição)': 0× na minuta 1 (minuta 3 §6.3 credita a ela → CORRIGIR); presente no TextoH (Parte 6.3) — autoria do TextoH em aberto")

# C05: TextoH contém os 9 → cruzamento r60 foi fiel ao insumo
t9 = all(x in th for x in ["fronteira explícita com a d-02","não são desempate","atribuição por relação","sem precedência emergente",
     "não autoriza substituição silenciosa","risco residual","disjuncao_de_contexto","niveis_distintos","`ancoras[].direcao_suporte` + marcação"])
ck("C05_CRUZAMENTO_FIEL", t9, "TextoH (arquivo da casa, r57) contém TODOS os elementos que o cruzamento atribuiu — linha 5 da escada com ancoras[].direcao_suporte INCLUSIVE: a frase 'não ocorre em nenhum dos dois textos' é falsa p/ TextoH → TextoH ≠ texto recebido pelo mestre")

# C06: citações '(Comentador)' da minuta 3 — 0× no TextoH (suporte indireto a um 2º texto)
fr = ["inferir equivalência de contexto","completar a condição por inferência","população","preservar as duas, registrar a lacuna e não escolher",
      "degrau normativo que efetivamente discrimine","relação causal explicitamente estabelecida","incerteza explícita","extrapolação em inexistência"]
zeros = [q for q in fr if q not in th]
ck("C06_TEXTO_M_DISTINTO", len(zeros) == len(fr) and "preservar ambas e sinalizar a lacuna" in th,
   f"{len(zeros)}/{len(fr)} frases creditadas ao Comentador na minuta 3 NÃO existem no TextoH → corrobora (a partir dos NOSSOS bytes) que o mestre recebeu outro texto; bytes dele ainda não vieram → pedido fica de pé")

# C07: 244 executado
cl = {}
for v in V:
    cid = v.get("claim_id") or None
    if cid: cl.setdefault(cid, []).append(v["natureza_relacao"])
from collections import Counter
tot, dec, claims = 0, Counter(), set()
for cid, ns in cl.items():
    for i in range(len(ns)):
        for j in range(i+1, len(ns)):
            if ns[i] != ns[j]: tot += 1; claims.add(cid); dec[tuple(sorted((ns[i], ns[j])))] += 1
ck("C07_244", tot == 244 and len(claims) == 41 and dec[("causal","contributiva")] == 113 and dec[("associativa","contributiva")] == 96
    and dec[("associativa","causal")] == 31 and dec[("causal","compensatoria")] + dec[("compensatoria","contributiva")] == 4,
    f"regra ampla executada: {tot} pares / {len(claims)} claims · decomposição {dict(dec)} = EXATA com a minuta 3 (inclui os 4 FP) → T-23 válido")

# C08: A — regra degradada 1-4 resolutivos × 5-6 qualificadores
ck("C08_A_DEGRADADA", "qualquer degrau resolutivo — 1, 2, 3 ou 4 — estiver indisponível" in m3 and "não barra o 7" in m3 and "só rotulam" in m3,
   "texto e lógica confirmados: resolve a B5 do cruzamento de forma mais limpa (5-6 não deixam 'conflito aparente' em aberto porque não resolvem) — a casa ACEITA")

# C09: B — §7 fundamentado; TNFR 0× catálogo; 3 vínculos no mesmo claim
ids11 = {v["id_vinculo"] for v in V if v.get("claim_id") == "B1.MEC.BLOCO02.011"}
ok9 = ("subdivis" in m3 and "nenhum campo do n2 v1.4 separa os dois" in m3 and ids11 >= {"VINC_B1_0035","VINC_B1_0036","VINC_B1_0037"}
       and not re.search(r"tnfr1|tnfr2|tnfrsf1a|tnfrsf1b", cf(cat))
       and "d-l05-granularidade-objeto" in m3)
ck("C09_B_GRANULARIDADE", ok9, f"§7 fiel ao N2 v1.4 (escopo = subdivisão; nenhum campo separa sub-objetos) · TNFR1/TNFR2 0× no catálogo (146 ids) · bloco02.011 tem {sorted(ids11)} · dívida bem posta, capacidade NÃO atribuída ao schema")

# C10: matriz corrigida SOZINHA zera os 4 (precisão aceita = C74-1)
CELLM = {tuple(sorted(x)) for x in [("causal","nao_estabelecida"),("contributiva","nao_estabelecida"),("associativa","nao_estabelecida"),("compensatoria","nao_estabelecida"),("marcador","nao_estabelecida")]}
pm = 0
for cid, ns in cl.items():
    for i in range(len(ns)):
        for j in range(i+1, len(ns)):
            if tuple(sorted((ns[i], ns[j]))) in CELLM: pm += 1
ck("C10_MATRIZ_ZERA", pm == 0, "matriz corrigida → 0 pares mesmo com proxy claim_id: a zeroagem é obra da MATRIZ (§7 da minuta 3 tem razão) — C74-1: a frase da casa na r60 ('id_oficial+escopo evita os 4 FP') precisada; o objeto operacional protege de FUTUROS proxies")

# C11: suíte unificada T-01..T-23
ids = re.findall(r"\| (T-\d\d) \|", M3)
tmap_ok = "M T-14 (novo)" in M3 and "M T-16 (novo)" in M3 and "C T-14" in M3 and "C T-15" in M3 and "(T-18) não tem oráculo" in M3
ck("C11_SUITE_23", set(ids) == {f"T-{n:02d}" for n in range(1, 24)} and tmap_ok,
   f"{len(set(ids))} IDs únicos em {len(ids)} ocorrências (T-18 citado também nas dependências — régua corrigida: conjunto, não contagem) · mapa M×C presente · T-18 oráculo pendente E1 declarado · nota editorial: mapa C T-2..T-12 não casa 1:1 com o TextoH (T-1..T-7 genéricos) → congelar mapa até o comentador dizer qual texto é dele")

COM = (SERIE / "COMENTADOR_analise_minuta3_L06_2026-09-21/COMENTADOR_analise_minuta3_L06_2026-09-21.md").read_text(encoding="utf-8")
ck("C12_ESTADO_RITO", "proposta consolidada ainda não vigente" in cf(COM) and "aprovação do operador" in m3,
   "rótulo temporal no corpo dos documentos (comentador + rito da própria minuta 3), nunca no nome (regra da casa ok) · casa NÃO estampa 'candidata/proposta' em peça própria")

# C13: D-D01-D02-FONTE fechável por consumo interno
ck("C13_D0102_FECHAVEL", "minuta 1 · defaults d-01 a d-08" in l5 and "## d-01 · relações concorrentes" in l5 and "## d-02 · autoridade epistemológica" in l5 and m1.count("d-01") >= 5,
   "L05 1.1 (na casa desde 15/09) DEFINE D-01..D-08 (l.2/47/73) · minuta 1 L-06 cita D-01 5×/D-02 3×/D-08 1× — C74-3: varrimento r57 ('0× em 12 docs') excluiu as minutas da série: confissão datada; dívida FECHADA por consumo interno; remanescente pequena: mapa 'Fase 3' → D-ORDEM-FASES")

ck("C14_RESPOSTA10", hashlib.sha256((SERIE / "RESPOSTA_10_L06_MINUTA1_E_P8_HARMONIZADO_2026-09-15.md").read_bytes()).hexdigest().startswith("cc40dfa0"),
   "citada pela minuta 3 §8: existe na série (cc40dfa0…, 15/09) — a linhagem P-1 (condicao ausente) é legítima e anterior")

# C15: balas do comentador (mensagem do turno) mapeadas
bullets = ["gate de consumo", "não redefine a d-02", "granularidade", "princípio de fecho", "lista unificada", "escada degradada"]
ok15 = all(x in m3 for x in bullets)
ck("C15_BALAS_COMENTADOR", ok15, f"balas incorporadas mapeadas {bullets} · pedido dele = verificação, não decisão arquitetural — honrado (carta 23 = só verificação + parecer)")

res = {"trilha": 74, "data": "2026-09-21", "objeto": "minuta 3 consolidada rev.1 + análise do comentador (proveniência + A/B/C)",
       "sha_minuta3": h3, "verdes": sum(1 for r in R if r["ok"]), "total": len(R), "checks": R,
       "confissoes": ["C74-1 (precisão da casa, r60): a zeroagem dos 4 FP é obra da matriz corrigida, não da definição operacional de objeto — §7 da minuta 3 aceito.",
                       "C74-2 (rev.64 errada): 'a minuta 1 da L-06 nunca chegou à casa' — arquivada desde 15/09, sha 3b6a15a0… (confere com a declarada pelo mestre), com trilha 31 e RESPOSTA_10. Dívida estreitada.",
                       "C74-3 (varrimento r57 com escopo errado): 'D-01/D-02 = 0× em 12 documentos' excluiu as minutas da série; D-01..D-08 estão definidos na L05 1.1 (na casa desde 15/09) e citados na minuta 1 L-06. D-D01-D02-FONTE fechada por consumo interno; remanescente: D-ORDEM-FASES (mapa 'Fase 3').",
                       "C74-4 (régua, menor): sed do prefixo do id 0261 na trilha 73 corrigido com nota datada no próprio script — 1ª escrita por memória incorreta, byte real VINC_B1_0261."]}
Path(__file__).with_suffix(".json").write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nRESULTADO: {res['verdes']}/{res['total']} verdes")
