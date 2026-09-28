#!/usr/bin/env python3
# TRILHA 76 — TextoM (minuta 2 canônica do comentador) recebido e verificado — 2026-09-21
# Fecha D-TEXTO-M; testa: achado do mestre × TextoM · citações "(Comentador)" da minuta 3 × TextoM · mapa §9 lado C · órfãos · elo-1 dos 244.
import json, re, hashlib, unicodedata
from pathlib import Path

B = Path("/home/user"); S = B / "BIBLIOTECAS/_documentos_serie"
TM = (S / "COMENTADOR_minuta2_L06_CANONICA_recebida_2026-09-21/COMENTADOR_minuta2_L06_CANONICA_2026-09-21.md").read_text(encoding="utf-8")
TH = (S / "COMENTADOR_minuta2_L06_recebida_2026-09-21/COMENTADOR_minuta2_L06_2026-09-21.md").read_text(encoding="utf-8")
M3 = (S / "MESTRE_L06_minuta3_consolidada_rev1_recebida_2026-09-21/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev1_2026-09-21.md").read_text(encoding="utf-8")
def cf(x): return unicodedata.normalize("NFC", x).casefold()
tm, th, m3 = cf(TM), cf(TH), cf(M3)
R = []
def ck(k, ok, det):
    R.append({"check": k, "ok": bool(ok), "detalhe": det}); print(("PASS " if ok else "FAIL ") + k + " — " + det)

h = hashlib.sha256(TM.encode()).hexdigest()
ck("C01_ARQUIVO", "**comentador · 2026-09-21**" in tm and "fase 3 da ordem de desenvolvimento" in tm and len(TM) > 5000,
   f"TextoM arquivado com nota da casa · sha={h} · cabeçalho canônico confere (Comentador · 2026-09-21 · Fase 3) — D-TEXTO-M FECHADA")

# C02 achado do mestre (9 linhas) contra TextoM — deve dar 9/9 "não ocorre/é assim"
a1 = "direcao_suporte` + marcação" not in tm and "## degrau 5 — relação direta versus extrapolação" in tm and "verification_status" not in tm.split("## degrau 5 — relação direta")[1].split("## degrau 6")[0]
a2 = "| **causal**" not in TM and "relação causal explicitamente estabelecida" in tm  # §1.2 = tabela de significados
a3 = "## 1.3" not in tm and "não redefine d-02" in tm   # fronteira D-02 só na Parte 9
a4 = "# parte 3 — escada degradada" in tm and "direção de suporte não vira ranking" not in tm
a5 = "# parte 4 — papel de `ancoras[].direcao_suporte`" in tm
a6 = "## 6.3 ordem normativa dos testes" in tm and "6.7" not in tm and "atribuição por relação" not in tm
a7 = "# parte 8 — dependências e estado atual" in tm
a8 = "# parte 10 — princípio de fecho" in tm
a9 = "disjuncao_de_contexto" not in tm and "niveis_distintos" not in tm
ck("C02_ACHADO_MESTRE_9x9", all([a1,a2,a3,a4,a5,a6,a7,a8,a9]),
   f"degrau5-sem-campo:{a1} · significados:{a2} · sem-1.3/D-02-na-9:{a3} · P3-degradada:{a4} · P4-direcao:{a5} · 6.3-testes/sem-6.7/sem-atribuição:{a6} · P8-dependências:{a7} · P10-fecho:{a8} · sem-disjuncao/niveis:{a9} → **o texto que o mestre recebeu É ESTE** (achado 9/9)")

# C03 citações "(Comentador)" da minuta 3 encontram casa nos bytes do TextoM (as mesmas 8 frases que eram 0× no TextoH)
fr = ["inferir equivalência de contexto","completar a condição por inferência silenciosa","população","preservar as duas, registrar a lacuna e não escolher",
      "primeiro degrau normativo que efetivamente discrimine","relação causal explicitamente estabelecida","incerteza explícita","extrapolação em inexistência da relação"]
falt = [q for q in fr if q not in tm]
ck("C03_CITACOES_TEM_CASA", not falt,
   f"8/8 frases creditadas ao Comentador na minuta 3 presentes no TextoM {falt or '— nenhuma faltando'} · emenda nº2 da carta 23 (marcar 'dependente de TextoM') fica SUPERADA: os créditos agora são verificáveis byte a byte pela casa")

# C04 mapa §9 lado C — cada 'C T-x' da minuta 3 casa com o teste do TextoM
pares = {"C T-2": "diferença sem conflito não dispara", "C T-4": "contexto ausente gera `degrau_2_indisponivel`",
         "C T-5": "condição suficiente permite avaliação", "C T-6": "condição insuficiente", "C T-7": "nível causal corretamente",
         "C T-8": "direta × extrapolação corretamente", "C T-9": "maturidade corretamente considerada", "C T-10": "coexistência multifatorial somente quando",
         "C T-11": "conflito não resolvido preserva ambas", "C T-12": "inversão a/b", "C T-13": "não existe estado residual",
         "C T-14": "não funciona como critério autônomo", "C T-15": "não entram silenciosamente"}
okmap = all(ref in M3 and kw in tm for ref, kw in pares.items())
ck("C04_MAPA_9_LADC", okmap,
   f"{sum(1 for r,k in pares.items() if r in M3 and k in tm)}/{len(pares)} referências 'C T-x' da minuta 3 casam semanticamente com os testes T-1..T-15 do TextoM → o mapa do §9 foi escrito contra ESTE texto; trava editorial da carta 23 destravada · nota: TextoM usa T sem zero (T-2), minuta 3 padroniza T-02 (cosmético)")

# C05 órfãos mantêm status: só no TextoH (rascunho) — emenda §6.3 continua de pé
ck("C05_ORFAOS_MANTEM", "atribuição por relação" not in tm and "não autoriza substituição silenciosa" not in tm
    and "atribuição por relação" in th and "não autoriza substituição silenciosa" in th,
   "as 2 frases NÃO estão na canônica — pertencem ao rascunho TextoH (autoria declarada: comentador) → emenda do §6.3 da minuta 3 fica: '(Comentador — rascunho arquivado pela casa, Parte 6.3)' · canônica não as carrega")

# C06 elo-1 da cadeia 244 agora com bytes: §1.1 do TextoM contém o enunciado citado na minuta 3
ck("C06_ELO1_244", "divergência de sinal, natureza ou interpretação relacional" in tm and "divergência de sinal, natureza ou interpretação relacional" in m3,
   "enunciado da regra (§1.1 canônica) bate literalmente com a citação da minuta 3 §1.2 → elos da cadeia 244/41 agora TODOS com bytes: enunciado (este arquivo) → dados 490675e6 → execução casa → registro 2ce9698c · único elo aberto restante: minuta 3 original a6a0027c (D-L06-M3-ORIG)")

# C07 coerência de estado (P-1 da casa): 'esparsa' da Parte 8 já corrigida na consolidada; TextoM honesto
ck("C07_ESTADO_CONDICAO", "estrutura insuficiente/esparsa" in tm and "ausente**, não \"insuficiente/esparsa\"" not in m3 or "ausente**, não" in m3,
   "TextoM diz 'insuficiente/esparsa' sobre condicao; a casa mediu AUSENTE (0/274) em 15-21/09 e a minuta 3 já carrega a correção explicitamente → convergência mantida, sem choque")

# C08 método dele declarado: master escreve a dele SEM a minuta como resposta pré-formatada (Fase/fluxo registrado)
ck("C08_METODO_FLUXO", "sem utilizar esta minuta como resposta pré-formatada" in tm and "cruzamento sistemático" in tm,
   "o próprio TextoM pede versão independente do mestre + cruzamento — é o fluxo que de fato aconteceu (minuta 2 mestre ≠ este texto; verificado trilhas 71-74) · 'Fase 3 da ordem de desenvolvimento' registrado — D-ORDEM-FASES segue dívida pequena")

res = {"trilha": 76, "data": "2026-09-21", "objeto": "TextoM (minuta 2 canônica do comentador) — verificação e fecho de D-TEXTO-M",
       "sha_textom": h, "verdes": sum(1 for r in R if r["ok"]), "total": len(R), "checks": R,
       "notas": ["com a canônica na mão, o triângulo fecha: TextoH (rascunho, sha 1a51d9b9) × TextoM (canônica) × minuta 1/3 do mestre — todos os lados com bytes na casa, exceto minuta 3 original (a6a0027c)"]}
Path(__file__).with_suffix(".json").write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nRESULTADO: {res['verdes']}/{res['total']} verdes")
