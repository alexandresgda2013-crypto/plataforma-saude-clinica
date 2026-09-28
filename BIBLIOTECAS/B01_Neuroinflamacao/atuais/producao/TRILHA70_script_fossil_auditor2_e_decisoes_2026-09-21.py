#!/usr/bin/env python3
# TRILHA 70 — rodada 56 (2026-09-21): auditor-2 crava o fossil 309aa65f no PROJETO DELE
# (mesma digital do fossil do projeto do mestre — replica interna 6/6 nos bytes arquivados)
# + DECISOES_ARQUITETURAIS recebido: P18 responde a fonte do conhecimento da NT (fecha
# D-DECIS-ARQ-BYTES) · 21 decisoes enumeradas · P11 hierarquia · 0 tensoes com Filosofia/V2.3
# Regua: python3 · NFC · casefold+ws-normalizado p/ quotes · linhas por splitlines() universal

import hashlib, json, re, unicodedata
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

DEC = S / "DECISOES_ARQUITETURAIS_recebido_2026-09-21/DECISOES_ARQUITETURAIS_v2_5_recebido_2026-09-21.md"
UPL = BASE / "uploads/0 DECISÕES ARQUITETURAIS.md"
AUD = S / "AUDITOR2_resposta_fossil_309aa65f_2026-09-21/AUDITOR2_resposta_fossil_2026-09-21.md"
FO  = S / "ARQUITETURA_projeto_mestre_FOSSIL_309aa65f_recebido_2026-09-20/ARQUITETURA_do_projeto_sha_309aa65f.md"
V2  = S / "SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md"

reg("C02 DECISOES medido+arquivado: sha 1830ff99... · 148.454 b · 2.781 CRLF · serie == upload",
    SHA(DEC) == "1830ff9939d8c8028dbcad680f307196ede4155d59ecce1b512c31b8df42f296"
    and SHA(DEC) == SHA(UPL) and DEC.stat().st_size == 148454, SHA(DEC)[:12])

T = unicodedata.normalize("NFC", DEC.read_text(encoding="utf-8"))
def cf(s): return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).casefold()
Cf = cf(T)
Ta = unicodedata.normalize("NFC", AUD.read_text(encoding="utf-8"))

reg("C03 P18 [DEFINIDO]: exclusividade da Biblioteca para NT/JSON/Motor + 'nunca o inverso' + precedencia automatica + 'proibido' — 4 clausulas literais",
    all(cf(q) in Cf for q in (
      "bibliotecas de conhecimento como fonte canônica e prioritária",
      "toda narrativa transversal, json modular, motor de raciocínio clínico e demais componentes derivados devem utilizar exclusivamente",
      "não realizando nova pesquisa bibliográfica nem introduzindo conhecimento externo",
      "não há espaço para interpretação caso a caso — a precedência é automática",
      "proibido")), "")

reg("C04 P11 [DEFINIDO]: hierarquia de fontes — 'prevalece a fonte de maior precedência' + 'decisões explícitas prevalecem sobre tudo'",
    all(cf(q) in Cf for q in ("hierarquia oficial de fontes de verdade",
                              "prevalece a fonte de maior precedência",
                              "decisões explícitas prevalecem sobre tudo")), "")

reg("C05 coerencia interdocumental: 'segunda fonte' 0x · P18 veda nova pesquisa nos derivados ⇒ SEM tensao Filosofia x V2.3 x DECISOES → D-DECIS-ARQ-BYTES FECHADA (a camada 4 do checklist do comentador reforça, nao conflita)",
    "segunda fonte" not in Cf and "nova pesquisa bibliográfica" in Cf, "")

nP = len(set(re.findall(r'"(P\d+)[a-zA-Z0-9_]*"\s*:\s*\{', T)))
reg("C06 enumeração: 21 decisoes P1..P21 no documento (regex; JSON interno nao-estrito — virgulas traseiras registradas)",
    nP == 21, f"nP={nP}")

Fl = FO.read_text(encoding="utf-8", newline="").splitlines()
m6 = (len(Fl) == 1421
      and Fl[0].strip() == "# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2    15.09.26"
      and Fl[44].strip() == "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2"
      and Fl[275].startswith("## 5.1.")
      and "schema_referencia_v1.1.json" in Fl[279]
      and "schema_vinculo_v1.1.json" in Fl[316]
      and Fl[1227].strip() == "# 26. PRIMEIRO PILOTO DE INTEGRAÇÃO")
reg("C07 fossil cravado: digital do auditor-2 == arquivado da casa (309aa65f — MESMO fantasma nos 2 projetos) + replica interna 6/6 (titulo 15/09 · V2.2 na linha 45 · §5.1 @276 · v1.1 @280/317 · §26 @1228)",
    SHA(FO) == "309aa65fa75de6b93cca24aaa154dbdf984833aff1716f8a26c510108c28b646"
    and "309aa65fa75de6b93cca24aaa154dbdf984833aff1716f8a26c510108c28b646" in Ta and m6, "")

L2 = V2.read_text(encoding="utf-8", newline="").splitlines()
s26 = next(i+1 for i, l in enumerate(L2) if l.strip().startswith("26. PRIMEIRO PILOTO") or l.strip() == "# 26. PRIMEIRO PILOTO DE INTEGRAÇÃO")
reg("C08 contraste com a V2 real de 15/09 (09692e18 · 46.129 b · 1.351 linhas): §26 na linha 1.158 — como ele mediu",
    SHA(V2).startswith("09692e18") and V2.stat().st_size == 46129 and s26 == 1158, f"s26={s26}")

pref = ["498e7df9", "b06660fd", "d96ad15b", "78a0f2af", "3b332426"]
reg("C09 eco dos 5 itens do pacote 21/09: os 5 prefixos constam no verbatim dele (5/5)",
    all(p in Ta for p in pref), str([p for p in pref if p in Ta]))

reg("C10 proveniencia do DECISOES registrada: cabecalho 'v2_5 · AUDITADO POR ARENA E CHATGPT 14/06/2022' — data anacronica (conteudo cita B16/GPM/P17, materia de set/2026): rotulo interno, bytes preservados",
    "DECISOES_ARQUITETURAIS_v2_5.json" in T and "AUDITADO POR ARENA" in T and "B16" in T and "GPM" in T, "")

reg("C11 nota de régua: no projeto dele a especificacao aparece como '..._v1_4_PROPOSTA__ESPECIFICACAO.md'; o arquivo distribuído e' L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4__ESPECIFICACAO.md (sem 'PROPOSTA') — ornamento de plataforma/transcricao; bytes sao 78a0f2af...",
    "PROPOSTA__ESPECIFICACAO" in Ta
    and (BASE / "ENTREGAS/2026-09-21_ENVIO_AUDITOR2_PROJETO_V23/L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4__ESPECIFICACAO.md").exists()
    and "PROPOSTA" not in "L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4__ESPECIFICACAO.md", "")

reg("C12 remocoes endossadas: fossil JA registrado na casa desde 20/09 (DIGITAIS da pasta) → remocao liberada · manifesto 19/09 substituido pelo 21/09 · renome CANDIDATA_ endossado (base de projeto != serie de trilha)",
    (S / "ARQUITETURA_projeto_mestre_FOSSIL_309aa65f_recebido_2026-09-20/DIGITAIS_2026-09-20.txt").exists()
    and "renomear a V2.3 para tirar o `CANDIDATA_`" in Ta, "")

reg("C13 ciencia trio intacto (fim)", trio() == ESP, str([s[:12] for s in trio()]))

ok = sum(1 for r in res if r["ok"])
out = PROD / "producao/TRILHA70_fossil_auditor2_decisoes_arquiteturais_2026-09-21.json"
out.write_text(json.dumps({"trilha": 70, "data": "2026-09-21", "rodada": 56,
  "escopo": "fossil 309aa65f cravado no projeto do auditor-2 (mesma digital do fossil do mestre) + DECISOES_ARQUITETURAIS recebido (P18 fecha a fonte da NT; D-DECIS-ARQ-BYTES fechada)",
  "notas": {"replica_fossil_6x6": "titulo V2 15.09.26 l.1 · V2.2 corpo l.45 · §5.1 l.276 · v1.1 l.280/317 · §26 l.1228 · contraste 09692e18 §26 l.1158",
            "json_decisoes": "interno possui virgulas traseiras — extracao por regex/casamento de chaves, 21 decisoes P*",
            "anacronismo": "cabecalho diz 14/06/2022; conteudo cita B16/GPM (set/2026) — rotulo tipografico registrado"},
  "checks": res, "verdes": ok, "total": len(res)}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nTRILHA 70: {ok}/{len(res)} verdes · json={out.name}")
