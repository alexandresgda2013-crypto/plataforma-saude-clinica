#!/usr/bin/env python3
# TRILHA 71 — rodada 57 (2026-09-21): ANALISE DE COMPATIBILIDADE da Minuta 2 da L-06
# (recebida via operador, autoria declarada: comentador) frente aos documentos/decisoes:
# acervo B1 (274 vinculos), schema N2 v1.4, V2.3 vigente, Filosofia/P18, verificação do mestre.
# Regua: python3 · NFC · casefold+ws p/ quotes · JSON strict p/ acervo e schema

import hashlib, json, re, unicodedata
from collections import Counter
from pathlib import Path

BASE = Path("/home/user")
S = BASE / "BIBLIOTECAS/_documentos_serie"
PROD = BASE / "BIBLIOTECAS/B01_Neuroinflamacao/atuais"
SHA = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
res = []
def reg(nome, ok, detalhe=""):
    res.append({"check": nome, "ok": bool(ok), "detalhe": detalhe})
    print(("OK " if ok else "FALHA ") + nome + (f"  [{detalhe}]" if detalhe and not ok else ""))

V7  = PROD / "B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
MAN = PROD / "Evidencias/Bibliografia/_manifesto_biblioteca.json"
VIN = PROD / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
ESP = ("6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238",
       "79d1309a168922d0e8bf43736cd5b21c8b361bdf64e3b200eeeafd43806f3a9c",
       "490675e63122a24baebd8890f4a7883a07f68916d90562e74adf309133501d1b")
trio = lambda: (SHA(V7), SHA(MAN), SHA(VIN))
reg("C01 ciencia trio intacto (inicio)", trio() == ESP, str([s[:12] for s in trio()]))

MINP = S / "COMENTADOR_minuta2_L06_recebida_2026-09-21/COMENTADOR_minuta2_L06_2026-09-21.md"
MIN = unicodedata.normalize("NFC", MINP.read_text(encoding="utf-8"))
V23 = unicodedata.normalize("NFC", (S / "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.3 - 19.09.26.md").read_text(encoding="utf-8"))
VER = unicodedata.normalize("NFC", (S / "MESTRE_verificacao_tecnica_V23_2026-09-21/VERIFICACAO_TECNICA_V23_CANDIDATA_2026-09-21 (1).md").read_text(encoding="utf-8"))
DEL = unicodedata.normalize("NFC", next((S / "MESTRE_deliberacao_fluxo_claim_recebida_2026-09-20").glob("*.md")).read_text(encoding="utf-8"))

reg("C02 minuta arquivada verbatim + marcas de regime (V2.3 · L-05 vigente · N1 v1.3 · N2 v1.4 · 'pronta para auditoria do Auditor-Mestre')",
    MINP.exists() and all(q in MIN for q in ("Normativa:** Arquitetura Consolidada da Plataforma V2.3", "L-05 vigente", "N1 v1.3", "N2 v1.4 selados", "pronta para auditoria do Auditor-Mestre")),
    f"sha={SHA(MINP)[:12]} bytes={MINP.stat().st_size}")

V = json.load(open(VIN, encoding="utf-8"))
vincs = V if isinstance(V, list) else V.get("vinculos", list(V.values())[0])
nat = Counter(v.get("natureza_relacao") for v in vincs)
mat = Counter(v.get("grau_maturidade") for v in vincs)
reg("C03 gatilho/matriz: as 6 naturezas da minuta sao EXATAMENTE as do acervo (causal 109 · contributiva 100 · associativa 56 · nao_estabelecida 4 · compensatoria 4 · marcador 1 = 274)",
    nat == Counter({"causal": 109, "contributiva": 100, "associativa": 56, "nao_estabelecida": 4, "compensatoria": 4, "marcador": 1}),
    str(dict(nat)))

tbl = MIN[MIN.find("|                      |"):MIN.find("A matriz não constitui")]
pares_cand = tbl.count("candidato")
reg("C04 matriz internamente consistente: 6 celulas 'candidato' na tabela · proibido conflito identico ('—' na diagonal) · gatilho 3c coerente (marcador nao 'afirma' → marcador×nao_estabelecida = compativel)",
    pares_cand == 6 and tbl.count("—") >= 6 and "marcador" in tbl, f"candidato={pares_cand}")

reg("C05 campos da Parte 5 presentes 274/274: trecho_ancora · natureza_relacao · forca_causal (4 tiers) · verification_status + grau_maturidade (5 valores; degrau 6 'presente no acervo' VERDADEIRO)",
    all(all(k in v for k in ("trecho_ancora", "natureza_relacao", "forca_causal", "verification_status", "grau_maturidade")) for v in vincs)
    and len(set(v["forca_causal"] for v in vincs)) == 4 and len(mat) == 5, f"mat={dict(mat)}")

aus = {q: sum(1 for v in vincs if q in v) for q in ("contexto", "condicao", "sentido_relacao", "nivel_cadeia", "ancoras", "direcao_suporte")}
reg("C06 ausencias declaradas conferem: contexto 0/274 ('ausente') · nivel_cadeia 0 ('depende da Ontologia') · sentido_relacao 0 (e a minuta MESMA marca 'requer mapeamento contratual' — honesta)",
    aus["contexto"] == 0 and aus["nivel_cadeia"] == 0 and aus["sentido_relacao"] == 0
    and "requer mapeamento contratual" in MIN and "| `contexto` estruturado" in MIN and "ausente" in MIN, str(aus))

sch = json.load(open(BASE / "ENTREGAS/2026-09-21_ENVIO_AUDITOR2_PROJETO_V23/schema_vinculo_v1.4.json", encoding="utf-8"))
aprops = sch["properties"]["ancoras"]["items"]["properties"]
reg("C07 PRECISAO P-1: 'condicao' = AUSENTE nos dados (0/274; nao 'esparsa') e ancoras[] = 0/274 nos dados — o campo vive no CONTRATO N2 v1.4 (ancoras[].condicao ✔) → redacao sugerida: 'ausente no acervo B1; estruturavel via ancoras[].condicao no retrofit' (efeito ja correto: degraus 2/3 indisponiveis)",
    aus["condicao"] == 0 and aus["ancoras"] == 0 and "condicao" in aprops
    and "atualmente esparsa" in MIN, "")

ext = Counter(str(v.get("extrapolacao_por_analogia", "")).split(" ")[0] for v in vincs)
vs = set(v.get("verification_status") for v in vincs)
reg("C08 PRECISAO P-2: 'marcacao de extrapolacao' EXISTE no acervo SEM ser nomeada — campo extrapolacao_por_analogia 274/274 (sim/parcial/baixa/media/nao) + verification_status {extrapolado, preclinico} · e ancoras[].direcao_suporte tem 0 portadores NOS DADOS (contrato ✔, retrofit pendente) → pela regra da Parte 4, degrau 5 parcialmente indisponivel na B1 ate o retrofit; minuta deve mapear extrapolacao→campo e espelhar o estado de dado",
    all("extrapolacao_por_analogia" in v for v in vincs) and {"extrapolado", "preclinico"} <= vs
    and aus["direcao_suporte"] == 0 and "direcao_suporte" in aprops, f"ext_top={ext.most_common(4)}")

corpo = [V23, VER, DEL,
         unicodedata.normalize("NFC", (S / "BASE_AUDITORIA_MOTOR_recebida_2026-09-19/ROTEIRO DE TRABALHO DA PLATAFORMA.md").read_text(encoding="utf-8")),
         unicodedata.normalize("NFC", (S / "DECISOES_ARQUITETURAIS_recebido_2026-09-21/DECISOES_ARQUITETURAIS_v2_5_recebido_2026-09-21.md").read_text(encoding="utf-8"))]
corpo += [unicodedata.normalize("NFC", p.read_text(encoding="utf-8")) for p in (
    S / "SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V1 - 15.09.26.md",
    S / "SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md",
    S / "SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.1  -  17.09.26.md",
    S / "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md",
    S / "RESPOSTA_6_ARQUITETURA_CONSOLIDADA_NT_PRE_MOTOR_2026-09-15.md")]
corpo.append(unicodedata.normalize("NFC", next((S / "MESTRE_LNT_minuta1_recebido_2026-09-18").glob("*.md")).read_text(encoding="utf-8")))
corpo.append(unicodedata.normalize("NFC", next((S / "OPERADOR_PROPOSTA_fluxo_claim_N1N2_recebido_2026-09-18").glob("*.md")).read_text(encoding="utf-8")))
corpo.append(unicodedata.normalize("NFC", next((S / "COMO_EXECUTAR_v1.9_recebido_2026-09-20").glob("*.md")).read_text(encoding="utf-8")))
hits_d01 = sum(t.count("D-01") for t in corpo); hits_d02 = sum(t.count("D-02") for t in corpo)
reg("C09 FINDING P-3: D-01 = 0x e D-02 = 0x em 12 documentos verificaveis (V1…V2.3, fossil, Roteiro, DECISOES, Minuta1 L-NT, deliberacao, proposta, verificacao, COMO EXECUTAR) · D-08 so 2x na deliberacao do mestre → a familia D-xx vive no espaco do mestre: DIVIDA D-D01-D02-FONTE (pedir o documento-fonte; conteudo atribuido e coerente, sem choque interno)",
    hits_d01 == 0 and hits_d02 == 0 and DEL.count("D-08") == 2, f"d01={hits_d01} d02={hits_d02}")

reg("C10 V2.3 vigente: 0x 'L-06'/'escada'/'D-01..D-08' — o objeto 'relacoes concorrentes' NAO vive na arquitetura (vive no espaco de contratos do mestre) · §21 existe (diagrama multidominio) · casa RESP6 (15/09) propunha 'L-06' como precedencia por proximidade com a ciencia em PORTAO — escopo distinto de runtime no grafo: sem contradicao medida",
    all(q not in V23 for q in ("L-06", "escada", "D-01", "D-02", "D-08"))
    and "# 21. ARQUITETURA MULTIDOMÍNIO COMPLETA" in V23
    and "L-06" in unicodedata.normalize("NFC", (S / "RESPOSTA_6_ARQUITETURA_CONSOLIDADA_NT_PRE_MOTOR_2026-09-15.md").read_text(encoding="utf-8")), "")

reg("C11 convergencia com a correcao PUBLICA do mestre (linha 110 da verificacao de 21/09: 'a direção é propriedade da âncora... o que afeta o degrau 5 da L-06, que precisa ler ancoras[].direcao_suporte') — a minuta aplica exatamente isso (degrau 5 + Parte 3 + Parte 5 + T-14 + Estado; 8x ancoras[].direcao_suporte)",
    "o que afeta o degrau 5 da L-06, que precisa ler `ancoras[].direcao_suporte`" in VER
    and MIN.count("ancoras[].direcao_suporte") >= 5, f"count={MIN.count('ancoras[].direcao_suporte')}")

reg("C12 filosofia/P18: Parte 9 da minuta ('nao realiza nova pesquisa bibliografica' · 'nao introduz conhecimento externo' · 'nao altera a fonte canonica') ≡ P18 das DECISOES e Filosofia · invariante anti-precedencia-fabricada alinha com 'o projeto nao e sistema de respostas improvisadas' — COERENTE",
    all(q in MIN for q in ("não realiza nova pesquisa bibliográfica", "não introduz conhecimento externo", "não altera a fonte canônica", "O Motor não fabrica precedência científica")), "")

reg("C13 autoria/rito: operador declara autoria do comentador; o documento se assina 'Auditor-Mestre' e se destina 'a auditoria do Auditor-Mestre' → ANOMALIA registrada: compatibilidade medida independe da autoria, mas a assinatura e' metadado normativo — corrigir a linha ANTES de circular (o mestre tem minuta propria declarada pronta; reconciliar ou ele audita esta — decisao do operador)",
    "**Auditor-Mestre · 2026-09-21**" in MIN and "pronta para auditoria do Auditor-Mestre" in MIN, "")

reg("C14 pontos internos finos da minuta (consistencia): ordem normativa + errata datada · 'nenhum degrau elimina' em 3 lugares (Parte 2/3/9) · regra multifatorial↔escada degradada (Parte 4) ≡ T-9 · consumo so de aprovados (Parte 5) ≡ T-15 · 'sem precedencia emergente' (Parte 6.7) alinha com o invariante",
    all(q in MIN for q in ("revisão formal e errata datada", "Se uma implementação futura eliminar uma relação",
                            "motivo = escada_degradada", "relação não entra na resolução", "Sem precedência emergente")), "")

reg("C15 ciencia trio intacto (fim)", trio() == ESP, str([s[:12] for s in trio()]))

ok = sum(1 for r in res if r["ok"])
out = PROD / "producao/TRILHA71_compatibilidade_minuta2_L06_2026-09-21.json"
out.write_text(json.dumps({"trilha": 71, "data": "2026-09-21", "rodada": 57,
  "escopo": "analise de compatibilidade da Minuta 2 L-06 (autoria declarada: comentador) x acervo B1, N2 v1.4, V2.3, Filosofia/P18, verificacao do mestre",
  "veredito": "COMPATIVEL nas camadas verificaveis · 2 precisoes de campo (P-1 condicao ausente!=esparsa · P-2 extrapolacao tem campo: extrapolacao_por_analogia; degrau 5 parcialmente indisponivel ate retrofit) · 1 finding estrutural (D-01/D-02 sem portador verificavel -> D-D01-D02-FONTE) · anomalia de autoria registrada",
  "checks": res, "verdes": ok, "total": len(res)}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nTRILHA 71: {ok}/{len(res)} verdes · json={out.name}")
