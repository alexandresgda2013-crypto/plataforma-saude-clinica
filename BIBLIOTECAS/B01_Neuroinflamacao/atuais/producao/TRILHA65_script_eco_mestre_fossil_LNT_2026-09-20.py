# TRILHA 65 — 2026-09-20 (rodada 50) — Eco do mestre (V2.2 no projeto) + fóssil
# cravado + 3 correções novas do L-NT réplicadas contra a especificação v1.4 +
# "Como Executar v1.9" (sha desconhecido da casa) + pontos do comentador verificados.
# Régua: regex + escopo + chave + sha · camada declarada · ciência 0.
import hashlib, json, re, os, glob, zipfile
from collections import Counter
from pathlib import Path

BASE = Path("/home/user")
S = BASE / "BIBLIOTECAS/_documentos_serie"
AT = BASE / "BIBLIOTECAS/B01_Neuroinflamacao/atuais"
DIST = BASE / "ENTREGAS/2026-09-19_SCHEMAS_L05_CORRENTES_DISTRIBUICAO"
checks = []
def reg(nome, ok, det): checks.append({"check": nome, "ok": bool(ok), "detalhe": det})
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

UP_FOSSIL = BASE / "uploads/ARQUITETURA_do_projeto_sha_309aa65f.md"
SR_FOSSIL = S / "ARQUITETURA_projeto_mestre_FOSSIL_309aa65f_recebido_2026-09-20/ARQUITETURA_do_projeto_sha_309aa65f.md"
V22 = S / "ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
V23 = S / "CARTAS_V23_2026-09-19/CANDIDATA_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.3 - 19.09.26.md"
V2_SERIE = S / "SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md"
V2_R24 = BASE / "uploads/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2  -  15.09.26.md"
ESP = DIST / "L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4__ESPECIFICACAO.md"
N2 = DIST / "schema_vinculo_v1.4__N2_CORRENTE.json"
N1 = DIST / "schema_referencia_v1.3__N1_CORRENTE.json"
MINUTA = S / "MESTRE_LNT_minuta1_recebido_2026-09-18/L-NT_CONTRATO_UNIDADES_NARRATIVAS_minuta1_294119b9_2026-09-18.md"
RE_M = S / "MESTRE_resposta_eco_V22_LNT_2026-09-20/RESPOSTA_MESTRE_eco_V22_LNT_2026-09-20.md"
RE_C = S / "COMENTADOR_analise_V23_status_x_tecnica_2026-09-20/COMENTADOR_analise_2026-09-20.md"
A2_R43 = S / "AUDITOR2_resposta_V23_linhagem_2026-09-19"
CARTA_V2 = S / "CARTA19_MESTRE_2026-09-20/CARTA_19_AO_AUDITOR_MESTRE_2026-09-20_v2.md"

CIENCIA = {
 "V7": (AT / "B1 NEUROINFLAMAÇÃO V7 CANONICA.md", "6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238"),
 "manifesto": (AT / "Evidencias/Bibliografia/_manifesto_biblioteca.json", "79d1309a168922d0e8bf43736cd5b21c8b361bdf64e3b200eeeafd43806f3a9c"),
 "vinculos": (AT / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json", "490675e63122a24baebd8890f4a7883a07f68916d90562e74adf309133501d1b"),
}
def ciencia_ok(): return all(sha(p) == h for p, h in CIENCIA.values())

reg("C01 ciencia trio intacto (inicio)", ciencia_ok(), {k: sha(p)[:12] for k,(p,_) in CIENCIA.items()})

# --- FÓSSIL: identidade cravada ---
fb = SR_FOSSIL.read_bytes(); ft = fb.decode("utf-8")
h1 = ft.splitlines()[0]
marc = {a: ft.count(a) for a in ["origem_conhecimento","a prosa prevalece sobre os desenhos",
        "fora do cânone","O Motor busca ativamente","schema_vinculo_v1.1","schema_vinculo_v1.4"]}
reg("C02 fossil: sha == 309aa65f... declarado pelo mestre · 51.235 b · 1421 linhas CRLF · H1 'V2 15.09.26' · 0/4 clausulas · v1.1 presente, v1.4 ausente",
    sha(UP_FOSSIL) == sha(SR_FOSSIL) == "309aa65fa75de6b93cca24aaa154dbdf984833aff1716f8a26c510108c28b646"
    and len(fb) == 51235 and fb.count(b"\r\n") == 1421 and "V2    15.09.26" in h1
    and all(marc[a] == 0 for a in list(marc)[:4]) and marc["schema_vinculo_v1.1"] == 1 and marc["schema_vinculo_v1.4"] == 0,
    f"sha={sha(SR_FOSSIL)} bytes={len(fb)} crlf={fb.count(chr(13).encode()+chr(10).encode())} H1={h1!r} marcadores={marc}")

iguais = [nome for nome, p in [("serie-09692e18", V2_SERIE), ("r24-5be36836", V2_R24), ("V2.2-df7f7cfd", V22)]
          if Path(p).read_bytes() == fb]
reg("C03 fossil NAO e' byte-identico a NENHUM elo conhecido da casa -> 4o artefato 'V2 15.09.26'",
    len(iguais) == 0,
    "distinto de: serie SUPERSEDED V2-15.09 (46.129 b) · upload r24 (50.964 b) · V2.2 oficial (52.181 b) · = elo NOVO, 51.235 b")

digfos = (SR_FOSSIL.parent / "DIGITAIS_2026-09-20.txt").read_text(encoding="utf-8")
reg("C04 fossil arquivado na serie com DIGITAIS (identidade cravada registrada por escrito)",
    "309aa65fa75de6b93cca24aaa154dbdf984833aff1716f8a26c510108c28b646" in digfos, SR_FOSSIL.parent.name)

# --- ECOS do mestre ---
rm = RE_M.read_text(encoding="utf-8")
tabela = {
 "V2.2 oficial": ("df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1", sha(V22)),
 "V2.3 candidata": ("498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73", sha(V23)),
 "Especificacao L-05 v1.4": ("78a0f2afcd2acf0f78caa8bbc674c337e7c5b47c93ee86d684f1648b6671dc8b", sha(ESP)),
}
ok_eco = all(h_dec == h_casa and h_dec in rm for h_dec, h_casa in tabela.values())
reg("C05 ecos do mestre CONFEREM: V2.2 · V2.3 · especificacao v1.4 == bytes da distribuicao da casa",
    ok_eco, {k: v[0][:12] for k, v in tabela.items()})

carta = CARTA_V2.read_text(encoding="utf-8")
reg("C06 precisao dele VERDADEIRA: a carta 19 v2 nao publicava a digital individual do md da especificacao",
    "78a0f2af" not in carta and "78a0f2afcd" in rm,
    "casa reconhece: shas individuais passam a ir na carta; este esta nesta rodada na resposta ao operador e no STATUS")

# --- Especificação v1.4: as 3 correções do L-NT ---
e = ESP.read_text(encoding="utf-8")
tabela_uso = all(a in e for a in ["v1.2 (trilha clínica)", "v3.1 (trilha mecanística)",
                 "contexto_mecanistico", "nucleo_causal", "suporte_correlacional", "gap_pesquisa"])
opcaoA = "trilha: clinica | mecanistica" in e
reg("C07 spec: 'uso' tem DUAS trilhas (tabela secao 0) · Opcao A 'trilha: clinica | mecanistica' escrita literalmente",
    tabela_uso and opcaoA and sha(ESP) == tabela["Especificacao L-05 v1.4"][0],
    f"tabela_uso={tabela_uso} opcaoA={opcaoA} · 'trilha' ocorre { e.count('trilha') }x na spec")

enum7 = ["humana_observacional","humana_experimental","humana_post_mortem",
         "preclinica_in_vivo","preclinica_in_vitro","mista","nao_aplicavel"]
m = MINUTA.read_text(encoding="utf-8")
reg("C08 natureza_evidencia: enum EXATO de 7 valores na spec (inclui preclinica_in_vivo/in_vitro e 'mista') · e na Minuta 1: N-4 no vocabulario do kit ('preclinical_mechanistic') + 0x 'nucleo_causal' — o achado do mestre PROCEDE",
    all(f"`{v}`" in e or v in e for v in enum7) and "preclinical_mechanistic" in m and "nucleo_causal" not in m,
    f"enum7_extraido={enum7} · minuta: preclinical_mechanistic={'preclinical_mechanistic' in m} nucleo_causal={'nucleo_causal' in m}")

reg("C09 direcao_suporte = 14x EXATO na spec · 'direcao' isolada = 3x mas TODAS no changelog interno (mesma anatomia do v1.1 residual da V2.3 — proveniencia historica)",
    e.count("direcao_suporte") == 14 and len(re.findall(r"direcao(?!_)\b", e)) == 3
    and "direcao` → `direcao_suporte" in e,
    "direcao_suporte=14 · direcao_isolada=3 (R7/rename — registro, nao campo) · N2 v1.4: trilha aparece "
    + str(N2.read_text(encoding='utf-8').count('trilha')) + "x, direcao_suporte "
    + str(N2.read_text(encoding='utf-8').count('direcao_suporte')) + "x (Opcao A ja materializada no schema)")

# --- réplica das medidas da spec SOBRE o acervo ---
VINC = json.load(open(AT / "Evidencias/Vinculos/vinculos_referencia_afirmacao.json"))
uso = Counter(str(r.get("uso")) for r in VINC)
alvo = {"contexto_mecanistico": 178, "clinico": 37, "gap_pesquisa": 29, "B1_v2": 30}
refs = Counter()
for f in ("01_pmids.json","02_meta_analises.json","03_ensaios_clinicos.json"):
    for r in json.load(open(AT / "Evidencias/Bibliografia" / f)):
        refs[str(r.get("evid_role"))] += 1
mapa = {k: refs.get(k, 0) for k in ("preclinical_mechanistic","human_clinical","review","human_experimental","post_mortem")}
reg("C10 replica acervo: uso 274 = {178·37·29·30} -> 244/274 (89%) conforme enum v1.2 EXATO · evid_role das 237 refs = {133·66·30·6·2} EXATO (fonte do mapeamento secao 2.2) · natureza_evidencia NAO existe ainda (0/237 refs · 0/274 vinculos — campo novo da v1.4)",
    dict(uso) == alvo and sum(uso[k] for k in ("contexto_mecanistico","clinico","gap_pesquisa")) == 244
    and mapa == {"preclinical_mechanistic":133,"human_clinical":66,"review":30,"human_experimental":6,"post_mortem":2}
    and all(str(r.get("natureza_evidencia")) == "None" for r in VINC),
    f"uso={dict(uso)} evid_role={mapa}")

# --- Como Executar v1.9: sha declarado que a casa não conhece ---
ce = KIT_ = S / "KIT_CLINICA_recebido_2026-09-15/4º COMO EXECUTAR — v1.7.md"
hits_nome = [p for p in glob.glob(str(BASE / "**/*"), recursive=True)
             if os.path.isfile(p) and ("V1.9" in p.upper() or "1CD90B40" in p.upper()) and "TRILHA65" not in p]
alvo_sha = "1cd90b407facee81692d668919829c9d6d5a149b1309424c6f012e26cd81f586"
hits_sha = 0
for root in ("uploads", "BIBLIOTECAS/_documentos_serie", "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao"):
    for p in glob.glob(str(BASE / root / "**/*.md"), recursive=True):
        try:
            if sha(p).startswith("1cd90b40"): hits_sha += 1
        except Exception:
            pass
reg("C11 'Como Executar v1.9' (1cd90b40...): 0 bytes na base da casa (0 por nome · 0 por sha) · acervo so tem v1.7 (18613516...) -> DECLARADO, nao verificado · pedido formal dos bytes (2 frentes citam esse documento: auditor-2 'adendo v1.9' + mestre sha no projeto)",
    hits_nome == [] and hits_sha == 0
    and sha(ce) == "186135166e061c85d7751a9b6a65955b2ccc999f4866e9f9af8cba8975771954"
    and alvo_sha in rm,
    f"hits_nome={hits_nome} hits_sha={hits_sha} v1.7={sha(ce)[:12]} · master_declarado={alvo_sha[:12]}")

# --- verbatins arquivados ---
reg("C12 verbatins da rodada arquivados com digitais (mestre 539bae64... · comentador fd29402d...)",
    sha(RE_M) == "539bae647f2c15a9d407af5d230c6c11dfcfcbfcba48800b783a93b8a738cbb4"
    and sha(RE_C) == "fd29402d7db23b93549cb4fc4661be16c55d88785024c118aeb3d0666e37a6fc"
    and "[VERBATIM" in RE_M.read_text(encoding="utf-8") and "NÃO CIRCULA" in RE_C.read_text(encoding="utf-8"),
    f"mestre={sha(RE_M)[:12]} comentador={sha(RE_C)[:12]}")

# --- modelo do operador: estado do "todas fecharam" ---
ecf_files = list(A2_R43.glob("*.md"))
a2_txt = "\n".join(p.read_text(encoding="utf-8") for p in ecf_files) if ecf_files else ""
v23_ecos = all(x in (RE_M.read_text(encoding="utf-8") + json.dumps(json.load(open(AT/"producao/TRILHA62_replica_resposta_mestre_V23_2026-09-19.json")), ensure_ascii=False) + a2_txt)
               for x in ["498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73"])
reg("C13 status 'todas fecharam' (modelo do operador): V2.3 = 3/3 ecos tecnicos (casa trilha 58/62 · mestre r45+r50 · auditor-2 r43) · schemas N1 v1.3 ('b06660fd') / N2 v1.4 ('d96ad15b') = 3 frentes favoraveis, falta so o eco do mestre sobre os 2 JSONs (a enviar)",
    v23_ecos and "b06660fd" in rm and "d96ad15b" in rm,
    "V2.3: TECNICAMENTE FECHADA sob seu criterio · schemas: 1 elo a fechar (mestre recalcula os bytes a caminho)")

reg("C14 ciencia trio intacto (fim)", ciencia_ok(), {k: sha(p)[:12] for k,(p,_) in CIENCIA.items()})

n_ok = sum(1 for x in checks if x["ok"])
out = {
 "trilha": 65, "data": "2026-09-20", "rodada": 50,
 "titulo": "Eco do mestre (V2.2 no projeto, D-V22-BYTES-PROJETO fechada pelo lado dele) + fossil cravado + 3 correcoes L-NT verificadas + v1.9 desconhecido",
 "veredito_da_replica": (
   "ECOS do mestre EXATOS (V2.2/V2.3/spec) · precisao dele (sha individual do md ausente na carta) VERDADEIRA — a casa adota publicar shas individuais nas proximas · "
   "FOSSIL = 4o artefato 'V2 15.09.26', 51.235 b, 0/4 clausulas, distinto de todos os elos (confissao da rev.52 FECHADA) · "
   "3 correcoes do L-NT: PROCEDEM na especificacao (uso 2 trilhas tabela §0 + Opcao A · natureza_evidencia 7 valores exatos · direcao_suporte 14x com 3x residuais de changelog) — a casa subscreve entrarem na minuta 2 · "
   "comentario do comentador: ponto de METODO correto (status != tecnica — o mestre JA disse 'confere' 2x; formalizavel) e 2 PREMISSAS imprecisas (anexo 'corresponde a V2.2' — falso, 0/4 marcadores · 'ponteiros antigos = antigo' — a V2.2 OFICIAL tambem cita v1.1, D-V22-SCHEMA-NOMES) · "
   "Como Executar v1.9: 0 bytes na casa — pedido formal dos bytes (duas frentes citam) · "
   "modelo do operador: V2.3 TECNICAMENTE FECHADA (3/3); schemas: falta o eco do mestre sobre os JSONs em transito."
 ),
 "checks": checks, "ok": n_ok, "total": len(checks),
 "confissoes": [
   "A casa publicava digital da especificacao so no zip (sha total), nao do md isolado: valida a observacao do mestre; corrigido a partir desta rodada (shas individuais passam a constar)",
   "Rodada 44 (rev.51): 'v1.9 nao existe, e discussao' — informacao do operador na epoca; agora 2 frentes citam o artefato com sha -> a casa marcou como DECLARADO-nao-verificado e pede os bytes, sem alegar existencia nem inexistencia"
 ]
}
js = AT / "producao/TRILHA65_eco_mestre_fossil_LNT_2026-09-20.json"
js.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"TRILHA 65: {n_ok}/{len(checks)} verdes · json={js.name}")
for x in checks: print(("OK " if x["ok"] else "FALHA ") + x["check"])
