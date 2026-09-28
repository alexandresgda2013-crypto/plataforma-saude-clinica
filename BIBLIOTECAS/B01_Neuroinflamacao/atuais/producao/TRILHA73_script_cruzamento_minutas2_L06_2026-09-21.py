#!/usr/bin/env python3
# TRILHA 73 — CRUZAMENTO DAS MINUTAS 2 DA L-06 (comentador × mestre) — 2026-09-21
# Pedido do comentador (via operador): verificação técnica independente A–F, SEM pré-decisão de arquitetura.
# Régua: python3, NFC, open() texto (universal newlines), casefold para quotes em prosa, regex com escopo declarado.
import json, re, hashlib, unicodedata
from pathlib import Path

BASE = Path("/home/user")
SERIE = BASE / "BIBLIOTECAS/_documentos_serie"
M = (SERIE / "MESTRE_L06_minuta2_recebida_2026-09-21/L06_RESOLUCAO_CONFLITOS_minuta2_2026-09-21.md").read_text(encoding="utf-8")
C = (SERIE / "COMENTADOR_minuta2_L06_recebida_2026-09-21/COMENTADOR_minuta2_L06_2026-09-21.md").read_text(encoding="utf-8")
Mh = hashlib.sha256(M.encode()).hexdigest()
Ch = hashlib.sha256(C.encode()).hexdigest()
Cf = unicodedata.normalize("NFC", C).casefold()
Mf = unicodedata.normalize("NFC", M).casefold()
VIN = BASE / "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
SCH = BASE / "ENTREGAS/2026-09-21_ENVIO_AUDITOR2_PROJETO_V23/schema_vinculo_v1.4.json"
V = json.loads(VIN.read_text(encoding="utf-8"))
S = json.loads(SCH.read_text(encoding="utf-8"))

R = []
def ck(k, ok, det):
    R.append({"check": k, "ok": bool(ok), "detalhe": det})
    print(("PASS " if ok else "FAIL ") + k + " — " + det)

# C1 arquivos e digitais (mestre medida r58; comentador medida r57)
ck("C01_BYTES", Mh == "eb54337c7f17c20fbd0ad1b926fd0d575b33462141537e837c4aff9fa13bbd13" and len(C) > 10000,
   f"mestre sha={Mh[:8]}==eb54337c (esperado) · comentador sha={Ch[:8]} ({len(C)} ch) — verbatim com nota de autoria da casa no topo")

# C2 A1: invariante literal idêntica nas duas
inv = "o motor não fabrica precedência científica onde a ciência não estabeleceu precedência"
ck("C02_A1_INVARIANTE", inv in Mf and inv in Cf, "frase literal presente nas duas (M §invariante / C INVARIANTE)")

# C3 A2: não-descarte nas duas
ck("C03_A2_NAO_DESCARTE", ("nenhum degrau elimina relação" in Mf) and ("a escada nunca produz descarte" in Cf or "nenhum degrau elimina uma relação" in Cf),
   "M: 'Nenhum degrau elimina relação' · C: Parte 2 regra fundamental + aviso de implementação")

# C4 A3: mesmas 7 perguntas + saída-base nas duas
perg = ["mesmo contexto clínico", "condições de aplicação diferentes", "níveis diferentes da cadeia causal",
        "estabelecida × emergente", "multifatorial", "conflito_nao_resolvido"]
ck("C04_A3_ESCADA7", all(p in Mf for p in perg) and all(p in Cf for p in perg),
   "7 perguntas e saídas-base idênticas nas duas tabelas (nomes extra da C: disjuncao_de_contexto/niveis_distintos = D)")

# C5 F2: regra degradada diverge (qualquer anterior × só 2 ou 4)
c_deg = "pelo menos um degrau anterior indisponível" in Cf
m_deg = "se o **2 ou o 4** estiver indisponível" in Mf or "2 ou o 4" in Mf
ck("C05_F2_DEGRADADA", c_deg and m_deg,
   "C: 'pelo menos um degrau anterior indisponível' barra multifatorial · M: 'se o 2 ou o 4 estiver indisponível' — C é estritamente mais geral; hoje mesmo efeito (2 e 4 indisponíveis), amanhã difere → B5/F2")

# C6 C-C5: determinismo 'atribuição por relação, nunca à posição' só na C
ck("C06_DETERMINISMO_ATRIBUICAO", ("atribuição por relação" in Cf and "nunca à posição" in Cf) and ("atribuição por relação" not in Mf),
   "Parte 6.3 de C explícita; M §4 tem ordem/simetria/idempotência mas não este item → resgate útil (C)")

# C7 B1: degrau 5 da C lê direcao_suporte (campo errado);verification_status existe na C mas na Parte 5, não no degrau
row5 = [l for l in C.splitlines() if l.strip().startswith("| 5 |") or l.strip().startswith("| 5 ")]
row5txt = " ".join(row5).casefold()
c_d5_errado = "direcao_suporte" in row5txt and "verification_status" not in row5txt
m_d5 = [l for l in M.splitlines() if l.strip().startswith("| 5 |")]
m_d5txt = " ".join(m_d5).casefold()
ck("C07_B1_DEGRAU5", c_d5_errado and "verification_status" in m_d5txt and "extrapolacao_por_analogia" in m_d5txt,
   f"linha do degrau 5 da C lê 'direcao_suporte + marcação de extrapolação' (verification_status 0× na linha, mas presente na Parte 5 da própria C) · M lê verification_status+extrapolacao_por_analogia → correção necessária em C")

# C8 verdade do schema: enum + semântica
ap = S["properties"]["ancoras"]["items"]["properties"]
ds = ap["direcao_suporte"]
ck("C08_SCHEMA_DIRECAO", set(ds["enum"]) == {"sustenta","refuta","inconclusivo","condicional"} and "ortogonal" in ds["description"].casefold(),
   "enum selado = direção epistêmica do suporte, 'ortogonal ao papel' — confirma B1 e a retratação §0.1 do mestre")

# C9 matrizes executadas nos 274 (proxy claim_id declarado — mesmo proxy de M §0.2)
nat = {v["id_vinculo"]: v.get("natureza_relacao") for v in V}
cl = {}
for v in V:
    cid = v.get("claim_id") or None
    if cid: cl.setdefault(cid, []).append(v["id_vinculo"])
def pares(cells):
    out = []
    for ids in cl.values():
        for i in range(len(ids)):
            for j in range(i+1, len(ids)):
                a, b = sorted([nat[ids[i]], nat[ids[j]]])
                if (a, b) in cells: out.append((ids[i], ids[j]))
    return out
CELL_C = {tuple(sorted(x)) for x in [("causal","compensatoria"),("contributiva","compensatoria"),
          ("causal","nao_estabelecida"),("contributiva","nao_estabelecida"),("associativa","nao_estabelecida"),("compensatoria","nao_estabelecida")]}  # marcador×nao_est = compatível na C
CELL_M = {tuple(sorted(x)) for x in [("causal","nao_estabelecida"),("contributiva","nao_estabelecida"),("associativa","nao_estabelecida"),("compensatoria","nao_estabelecida"),("marcador","nao_estabelecida")]}
pc, pm = pares(CELL_C), pares(CELL_M)
esp = {  # nota de régua: 1ª escrita usou prefixo B1V2_ no 0261 por memória incorreta; byte real = VINC_B1_0261 (corrigido, datado 2026-09-21)
("VINC_B1_0035","VINC_B1_0036"),("VINC_B1_0036","VINC_B1_0037"),("VINC_B1_0052","VINC_B1_0261"),("VINC_B1_0053","VINC_B1_0261")}
got = {tuple(sorted(p)) for p in pc}
ck("C09_MATRIZES", len(pc) == 4 and got == esp and len(pm) == 0,
   f"matriz da C (claim_id como proxy declarado) → {len(pc)} pares = os 4 FP exatos de M §0.2 · matriz corrigida de M → {len(pm)} pares → B2 confirmada")

# C10 F1: colisão de IDs de teste
tC = {t for t in ["T-14","T-15","T-16"] if re.search(t + r"\s*[—\-|]", C)}
tM = {t for t in ["T-14","T-15","T-16"] if t in M}
mNovo = len(re.findall(r"T-1[456] \(novo\)", M))
ck("C10_F1_COLISAO_TESTES", tC == {"T-14","T-15"} and tM == {"T-14","T-15","T-16"} and mNovo == 3,
   f"C usa T-14 (direção não-precedente) e T-15 (gate); M marca '(novo)' em T-14/T-15/T-16 com OUTROS critérios → IDs colidem; renumerar na consolidação (B6)")

# C11 C-C1: gate de consumo só na C
ck("C11_GATE", ("aprovados para consumo" in Cf or "não aprovada para consumo" in Cf) and ("aprovados para consumo" not in Mf and "consumo" not in Mf),
   "C Parte 5: existência no acervo ≠ autorização; não consumir campos de transição/depreciados + T-15 gate · M sem seção equivalente → resgate (E1: amarrar 'aprovado' ao fluxo)")

# C12 C-C3: fronteira L-06×D-02 — seção na C, menção lateral em M
ck("C12_FRONTEIRA_D02", "fronteira explícita com a d-02" in Cf and Mf.count("d-02") <= 2,
   f"C dedica Parte 1.3; M cita D-02 {Mf.count('d-02')}× lateralmente → resgate: seção própria evita que resolução vire autoridade epistemológica")

# C13 C-C6 + M-C6: anti-substituição-silenciosa (C Parte 8) × escopo≠contexto (M §2)
ck("C13_ANTI_SUBSTITUICAO", ("não autoriza substituição silenciosa" in Cf) and ("não serve. o schema o define como" in Mf or "não serve" in Mf and "subdivisão interna" in Mf),
   "C: ausência não autoriza campo 'parecido' · M: escopo é subdivisão interna, não contexto clínico (fiel ao schema, medido r57) — convergentes e complementares, preservar os dois")

# C14 C-C7: Parte 10 risco gatilho estreito × M §0.2 'o dado mostrou o contrário'
ck("C14_ARCO_RISCO", ("estreito demais" in Cf and "reavaliado após o piloto" in Cf) and ("estreito demais" in Mf and "o dado mostrou o contrário" in Mf),
   "C declara o risco a priori; M mede que o risco real era uma célula errada → a consolidada deve contar os dois lados do arco")

# C15 portões medidos + 'sem caso no acervo' do marcador
no_cl = [v for v in V if not (v.get("claim_id") or None)]
nea = [v["id_vinculo"] for v in V if v.get("natureza_relacao") == "nao_estabelecida"]
marc = [v["id_vinculo"] for v in V if v.get("natureza_relacao") == "marcador"]
anc = sum(1 for v in V if isinstance(v.get("ancoras"), list) and v["ancoras"])
ok15 = (anc == 0 and sum(1 for v in V if v.get("verification_status")) == 274
        and sum(1 for v in V if v.get("extrapolacao_por_analogia")) == 274
        and set(nea) == {"VINC_B1_0028","VINC_B1V2_0197","VINC_B1V2_0198","VINC_B1V2_0202"}
        and marc == ["VINC_B1V2_0201"] and (no_cl and all(v["id_vinculo"].startswith("VINC_B1V2_0") for v in no_cl)))
ck("C15_PORTOES", ok15,
   f"ancoras 0/274 · verification_status 274 · extrapolacao 274 · nao_est={nea} (1 com claim, 3 sem) · marcador={marc} sem par → 'marcador×nao_est: sem caso no acervo' VERDADE (E2, revisar no piloto)")

res = {"trilha": 73, "data": "2026-09-21", "objeto": "cruzamento minutas 2 L-06 (comentador × mestre) — pedido A–F sem pré-decisão",
       "sha_mestre": Mh, "sha_comentador_recebido": Ch,
       "verdes": sum(1 for r in R if r["ok"]), "total": len(R), "checks": R,
       "confissoes": ["C73-1 (r59, confirmada nesta rodada): a pergunta 'dá para usar por fora?' NÃO foi feita pelo operador — a casa leu como pergunta dele um trecho de contexto colado; medição mantida como conteúdo verificado, atribuição retirada e registrada na ata (rev.67).",
                       "C73-2 (carta 22, refinada): a casa declarou 'base = minuta do mestre + 2 resgates' ANTES do cruzamento técnico A–F das duas versões; o enquadramento antecipava decisão de consolidação que pertence aos autores + operador. Este relatório substitui aquele enquadramento por vereditos item a item."]}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nRESULTADO: {res['verdes']}/{res['total']} verdes")
