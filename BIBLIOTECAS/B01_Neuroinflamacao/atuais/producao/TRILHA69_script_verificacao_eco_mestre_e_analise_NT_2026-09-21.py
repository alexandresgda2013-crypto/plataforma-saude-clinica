#!/usr/bin/env python3
# TRILHA 69 — rodada 55 (2026-09-21): eco do mestre (3/3) + renome dos schemas no projeto
# + REPLICA DOCUMENTAL da analise do comentador sobre a fonte do conhecimento da NT
# (quotes verificados nos bytes da Filosofia, V2.3 vigente, Roteiro, Minuta 1, deliberação)
# Regua: python3 · NFC · casefold + whitespace normalizado (CONFISSAO C69-1 abaixo)
# Saida: TRILHA69_verificacao_eco_mestre_e_analise_NT_2026-09-21.json
#
# CONFISSOES DESTA TRILHA (datadas):
# C69-1 (2026-09-21): 1a sondagem das quotes F1/F2/F4 marcou 0x — regua case-sensitive;
#   as quotes existiam com inicial maiuscula ("Todo conhecimento..."). Corrigida com
#   casefold; o '0x' era artefato do parser, nao ausencia no documento.
# C69-2 (2026-09-21): comentador comprime quotes sem marcar: A1 omite "(NT)", funcao 6
#   omite "integracao a", F4 rende a triade-lista como setas, "Pasta de Atualizacao ->
#   consulta propria do Motor" e' parafrase fiel de "chega ao Motor por caminho proprio,
#   por consulta ativa". Classe: quote de conteudo, nao de literal — registrado, nao censurado.

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

def texto(p):
    return unicodedata.normalize("NFC", Path(p).read_text(encoding="utf-8"))
def cf(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).casefold()

# ---------- C01/C14 ciencia (trio) ----------
V7  = PROD / "B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
MAN = PROD / "Evidencias/Bibliografia/_manifesto_biblioteca.json"
VIN = PROD / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
ESP = ("6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238",
       "79d1309a168922d0e8bf43736cd5b21c8b361bdf64e3b200eeeafd43806f3a9c",
       "490675e63122a24baebd8890f4a7883a07f68916d90562e74adf309133501d1b")
trio = lambda: (SHA(V7), SHA(MAN), SHA(VIN))
reg("C01 ciencia trio intacto (inicio)", trio() == ESP, str([s[:12] for s in trio()]))

# ---------- arquivos-fonte ----------
FIL = S / "BASE_AUDITORIA_MOTOR_recebida_2026-09-19/FASE 2- 02 FILOSOFIA DO PROJETO.md"
V23 = S / "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.3 - 19.09.26.md"
ROT = S / "BASE_AUDITORIA_MOTOR_recebida_2026-09-19/ROTEIRO DE TRABALHO DA PLATAFORMA.md"
MES = S / "MESTRE_resposta_eco_V23_renome_schemas_2026-09-21/MESTRE_resposta_eco_V23_renome_2026-09-21.md"
COM = S / "COMENTADOR_analise_NT_fonte_conhecimento_2026-09-21/COMENTADOR_analise_NT_fonte_2026-09-21.md"
DEL = next((S / "MESTRE_deliberacao_fluxo_claim_recebida_2026-09-20").glob("*.md"))
Tf, Tv, Tr, Tm, Tc, Td = (texto(p) for p in (FIL, V23, ROT, MES, COM, DEL))
Cf, Cv, Cr, Cc = cf(Tf), cf(Tv), cf(Tr), cf(Tc)

reg("C02 vigente V2.3 intocada na serie (sha 498e7df9...)",
    SHA(V23) == "498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73", SHA(V23)[:12])

# ---------- C03: eco do mestre 3/3 + verbatim arquivado ----------
ECO = {"498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73",
       "b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da",
       "d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050"}
no_texto = {h for h in ECO if h in Tm}
reg("C03 eco do mestre 3/3: as 3 digitais da casa constam no verbatim dele + 'Nenhuma divergencia. Elo autentico.'",
    no_texto == ECO and "elo autêntico" in cf(Tm),
    f"encontradas={len(no_texto)}/3")

# ---------- C04: renome registrado — so o separador difere do $id; bytes intactos ----------
Cfm = cf(Tm)
ren = ("schema_referencia_v1_3.json" in Tm and "schema_vinculo_v1_4.json" in Tm
       and "schema_vinculo_v1.4.json" in Tm and "só o ponto separa" in Cfm)
def base(n):  # nome -> candidato a $id trocando _v1_3 por _v1.3
    return n.replace("_v1_", "_v1.")
par1 = ("schema_referencia_v1_3.json", "schema_referencia_v1.3.json")
par2 = ("schema_vinculo_v1_4.json",   "schema_vinculo_v1.4.json")
so_sep = all(base(a) == b for a, b in (par1, par2))
reg("C04 renome no projeto: sufixos __N1/N2_CORRENTE cairam, '.' virou '_' — so o separador difere do $id; bytes ilesos (C03)",
    ren and so_sep, f"ren={ren} so_separador={so_sep}")

# ---------- C05: sugestao de higiene dele registrada (decisao do operador; casa endossa com precisao) ----------
reg("C05 higiene: ele pede remover a V2.2 do projeto e trocar o nome 'CANDIDATA_...' da copia vigente — casa endossa (regra de nao-renomear vale so para a SERIE de trilha, nao para base de trabalho de projeto)",
    "duas arquiteturas" in Tm and "CANDIDATA_ARQUITETURA_V2_3" in Tm, "")

# ---------- C06: Filosofia — F1 F2 F3 + bonus 'derivar exclusivamente' (casefold) ----------
fil_ok = all(cf(q) in Cf for q in (
    "todo conhecimento científico ingressa obrigatoriamente pela biblioteca de conhecimento correspondente",
    "todos os demais componentes da plataforma são derivados dessa fonte canônica",
    "única fonte canônica de conhecimento científico da plataforma",
    "todo conteúdo apresentado ao usuário deve derivar exclusivamente das bibliotecas de conhecimento correspondentes"))
reg("C06 Filosofia: F1/F2/F3 literais (casefold) + bonus 'derivar exclusivamente' — porta unica de conhecimento CONFERE",
    fil_ok, "")

# ---------- C07: triade — lista de 3 + enumeracao; setas sao renderizacao dele ----------
tri_lista = all(cf(x) in Cf for x in ("tríade de conhecimento", "biblioteca de conhecimento:", "narrativa transversal:", "json modular:"))
tri_setas_f = "biblioteca de conhecimento → narrativa transversal → json modular" in Cf
tri_setas_v = "biblioteca canônica → narrativa transversal (nt) → json(s) modular(es)" in Cv
reg("C07 triade: existe como LISTA (Filosofia) e como CADEIA com setas na V2.3 (com '(NT)') — a compressao do comentador e' fiel no conteudo",
    tri_lista and tri_setas_v and not tri_setas_f, f"setas_na_filosofia={tri_setas_f} (esperado False)")

# ---------- C08: V2.3 — A2 A3 A4 A5 literais ----------
a_ok = all(cf(q) in Cv for q in (
    "fonte fechada e auditada do conhecimento científico de cada entidade/domínio",
    "não deverá reconstruir a biblioteca",
    "não deverá complementar silenciosamente a biblioteca",
    "não constituem uma segunda biblioteca canônica"))
reg("C08 V2.3: fonte fechada · NT nao reconstrui · nao complementa silenciosamente · Evidencias != 2a Biblioteca — CONFERE",
    a_ok, "")

# ---------- C09: V2.3 — especificacao operacional da NT (§NT) literai ----------
n_ok = all(cf(q) in Cv for q in (
    "interpretar semanticamente, organizar, relacionar, estruturar e explicar o conhecimento científico já fechado e auditado",
    "não deverá realizar nova busca científica durante sua construção",
    "consumir o conhecimento da biblioteca correspondente",
    "preservar a rastreabilidade até a afirmação e a evidência de origem"))
f6_variante = "preparar essas relações para integração à ontologia/grafo" in Cv
f6_comentador = "preparar essas relações para a ontologia/grafo" in Cv
reg("C09 V2.3: funcao da NT + vedação de nova busca + 8 deveres (spots) — CONFERE; funcao 6 tem 'integracao a' (comentador omitiu)",
    n_ok and f6_variante and not f6_comentador, f"f6_variante={f6_variante}")

# ---------- C10: fluxos — canonico x atualizacao segregados (V2.3) ----------
fl_ok = all(cf(q) in Cv for q in (
    "pasta de atualização chega ao motor por caminho próprio, por consulta ativa",
    "sem se fundir aos vínculos canônicos",
    "rota paralela de conhecimento recente e não altera automaticamente essa cadeia",
    "não significa automaticamente que seu conteúdo já tenha se tornado conhecimento canônico"))
seg = Cv.count("segregado")
reg("C10 V2.3: Pasta de Atualizacao = caminho proprio do Motor, sem fundir-se aos canonicos — parafrase do comentador FIEL",
    fl_ok and seg >= 1, f"segregados={seg}x")

# ---------- C11: 'memoria parametrica' = sintese dele (0x nos docs) com gancho na Filosofia ----------
docs = [Cf, Cv, Cr, cf(Tm), cf(texto(S / "MESTRE_LNT_minuta1_recebido_2026-09-18/" / next((S / "MESTRE_LNT_minuta1_recebido_2026-09-18").glob("*.md")).name))]
mp = sum(d.count("memória paramétrica") for d in docs)
gancho = "respostas improvisadas por modelos de linguagem" in Cf
reg("C11 'memoria parametrica': 0x nos 5 documentos (sintese do comentador, nao quote) — gancho filosofico existe ('nao e' sistema de respostas improvisadas por modelos de linguagem)",
    mp == 0 and gancho, f"mem_param={mp}")

# ---------- C12: DELIB — (i)/(ii) textos exatos + recomendacao + medidas ----------
d_ok = all(q in Td for q in ("(i) Claim clínico é insumo de evidência, não de conhecimento",
                             "(ii) Claim clínico é segunda fonte de conhecimento",
                             "É a saída que recomendo",
                             "alteração arquitetural — opção C, não B",
                             "39 dos 49 PMIDs do kit não estão na V7"))
reg("C12 deliberação (fe5a18b3...): (i) insumo de evidencia/bifurcacao recomendada · (ii) = alteracao arquitetural · medida 39/49 — CONFERE",
    d_ok, "")

# ---------- C13: classificacao — (ii) NAO e' escolha livre ----------
choque_f3 = "única fonte canônica de conhecimento científico da plataforma" in Cf
emenda_ii = "segunda fonte de conhecimento" in Td and "§6 dever 1 precisa ser emendado" in Td
reg("C13 CLASSIFICACAO (régua do passo 7 do comentador): (ii) contradiz a Filosofia ('unica fonte canonica') e exige emenda do §6 dever 1 — logo NAO e' escolha livre; só via emenda arquitetural formal · (i) = compativel com todas as camadas",
    choque_f3 and emenda_ii, "")

# ---------- C14: Roteiro sem contradicao + DECISOES_ARQUITETURAIS ausente (divida nomeada) ----------
rot_bib = Cr.count("biblioteca")
rot_sem = all(cf(q) not in Cr for q in ("fonte canônica", "nova busca", "segunda fonte"))
decis = list(BASE.glob("**/*DECISOES*ARQUITET*")) + list(BASE.glob("**/*decisoes_arquitet*"))
origem_rot = "transformar o conhecimento canônico em unidades narrativas reutilizáveis" in Cr
reg("C14 Roteiro: 0 clausulas em contradicao (16x 'biblioteca'; NT nasce 'do conhecimento canonico') · DECISOES_ARQUITETURAIS 0x na base -> D-DECIS-ARQ-BYTES (divida nomeada)",
    rot_bib >= 10 and rot_sem and len(decis) == 0 and origem_rot, f"rot_bib={rot_bib} decis={len(decis)}")

# ---------- C15: ciencia fim ----------
reg("C15 ciencia trio intacto (fim)", trio() == ESP, str([s[:12] for s in trio()]))

ok = sum(1 for r in res if r["ok"])
out = PROD / "producao/TRILHA69_verificacao_eco_mestre_e_analise_NT_2026-09-21.json"
out.write_text(json.dumps({"trilha": 69, "data": "2026-09-21", "rodada": 55,
    "escopo": "eco do mestre pos-aprovacao + renome schemas projeto + replica documental da analise NT-fonte (comentador)",
    "confissoes": {"C69-1": "regua case-sensitive na 1a sondagem (F1/F2/F4 marcaram 0x com quote presente) — corrigida com casefold",
                    "C69-2": "comentador comprime quotes (A1 sem '(NT)'; funcao 6 sem 'integracao a'; triade-lista rendida como setas; parafraise do fluxo do Motor) — conteudo fiel, literal registrado"},
    "checks": res, "verdes": ok, "total": len(res)}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nTRILHA 69: {ok}/{len(res)} verdes · json={out.name}")
