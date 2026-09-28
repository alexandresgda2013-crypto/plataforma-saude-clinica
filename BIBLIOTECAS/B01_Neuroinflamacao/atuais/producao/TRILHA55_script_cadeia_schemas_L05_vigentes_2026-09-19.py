#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRILHA 55 — Rodada 37 (2026-09-19): Cadeia dos schemas L-05 (N1/N2) e entrega dos VIGENTES.
Pergunta do operador: "o schema_vinculo_v1.1.json não é o atualizado?"
Régua: python NFC trilateral · casefold declarado por check · comandos gravados no JSON.
0 ciência: shas V7/manifesto/vínculos conferidos no início e no fim.
"""
import json, hashlib, os, re, shutil, zipfile, unicodedata

RAIZ = "/home/user"
SERIE = os.path.join(RAIZ, "BIBLIOTECAS/_documentos_serie")
ENTREGA = os.path.join(RAIZ, "ENTREGAS/2026-09-19_SCHEMAS_L05_VIGENTES")
checks = []
def C(cid, titulo, camada, escopo, comando, medido, esperado, detalhe=""):
    checks.append({"id": cid, "titulo": titulo, "camada": camada, "escopo": escopo,
                   "comando": comando, "medido": medido, "esperado": esperado,
                   "ok": medido == esperado, "detalhe": detalhe})

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(65536), b""): h.update(b)
    return h.hexdigest()

def txt(p):
    return unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8"))

# ---------- 0 CIÊNCIA (início) ----------
V7   = os.path.join(RAIZ, "BIBLIOTECAS/B01_Neuroinflamacao/atuais/B1 NEUROINFLAMAÇÃO V7 CANONICA.md")
MAN  = os.path.join(RAIZ, "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia/_manifesto_biblioteca.json")
VINC = os.path.join(RAIZ, "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json")
# (fallbacks de caminho, medidos na hora)
for alvo in (V7, MAN, VINC):
    if not os.path.exists(alvo):
        print("FALTA", alvo)
ciencia_ini = {os.path.basename(p): sha(p) for p in (V7, MAN, VINC) if os.path.exists(p)}

# ---------- CADEIA N2 (schema_vinculo) ----------
cadeia_n2 = [
    ("v1.1", "uploads/schema_vinculo_v1.json",
             SERIE + "/L05_v1.1_recebido_2026-09-15/schema_vinculo_v1.1.json",
             "b0934412b010b7e0801f372ae57769fe0daa42c046e757128788159ec9ff4130", 10708, "2026-09-15"),
    ("v1.2", None, SERIE + "/L05_v1.2_schemas_recebidos_2026-09-16/schema_vinculo_v1.2_recebido_2026-09-16.json",
             "19f4f29a8763aa635a09d16c1bd960af2687da62a5f79700b8dfd57081d73360", 11122, "2026-09-16"),
    ("v1.3", "uploads/schema_vinculo_v1 (1).json",
             SERIE + "/AUDITOR2_triagem_L05v13_recebido_2026-09-17/schema_vinculo_v1.3_recebido_2026-09-17.json",
             "ec4f0de88fd0d845ad91f1d413132fa7d9a5c38d1f9f2f7abff1d3a27e7bf836", 12307, "2026-09-17"),
    ("v1.4", "uploads/schema_vinculo_v1 (2).json",
             SERIE + "/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json",
             "d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050", 12840, "2026-09-18"),
]
for ver, up, arq, sha_esp, tam_esp, data in cadeia_n2:
    ok_sha = sha(arq) == sha_esp
    C(f"N2-{ver}-sha", f"arquivado {ver} sha+tamanho", "bytes", arq,
      f"sha256sum {arq}", (ok_sha, os.path.getsize(arq)), (True, tam_esp),
      f"recebido {data}")
    if up:
        up_full = os.path.join(RAIZ, up)
        C(f"N2-{ver}-upload", f"upload ≡ arquivado ({ver})", "bytes", up_full,
          f"sha256sum \"{up_full}\"", sha(up_full) == sha(arq), True,
          "renomeado pelo navegador; conteúdo idêntico")
    j = json.loads(txt(arq))
    C(f"N2-{ver}-id", f"$id interno declara {ver}", "documental{NFC}", arq,
      "json.load()['$id']", j.get("$id"), f"L05/schema_vinculo_{ver}.json",
      "a versão real vive DENTRO do JSON ($id), não no nome do arquivo")

# ---------- CADEIA N1 (schema_referencia) ----------
cadeia_n1 = [
    ("v1.1", "uploads/schema_referencia_v1.json",
             SERIE + "/L05_v1.1_recebido_2026-09-15/schema_referencia_v1.1.json",
             "737bcda824b6c355d4f9b34faa3703e5ff94537b65751efbcc9d26b4b93553db", 7796, "2026-09-15"),
    ("v1.2", None, SERIE + "/L05_v1.2_schemas_recebidos_2026-09-16/schema_referencia_v1.2_recebido_2026-09-16.json",
             "b8bcea8084fc17a296ef2beebd709bb2c90a7d816918ddfda74a0667e6ec168a", 8674, "2026-09-16"),
    ("v1.3", "uploads/schema_referencia_v1 (1).json",
             SERIE + "/AUDITOR2_triagem_L05v13_recebido_2026-09-17/schema_referencia_recebido_2026-09-17.json",
             "b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da", 9582, "2026-09-17"),
]
for ver, up, arq, sha_esp, tam_esp, data in cadeia_n1:
    C(f"N1-{ver}-sha", f"arquivado {ver} sha+tamanho", "bytes", arq,
      f"sha256sum {arq}", (sha(arq) == sha_esp, os.path.getsize(arq)), (True, tam_esp), f"recebido {data}")
    j = json.loads(txt(arq))
    C(f"N1-{ver}-id", f"$id interno declara {ver}", "documental{NFC}", arq,
      "json.load()['$id']", j.get("$id"), f"L05/schema_referencia_{ver}.json", "")
# par de uploads N1 (1) e (2) byte-idênticos
C("N1-v1.3-par", "uploads referência (1) ≡ (2)", "bytes", "uploads/",
  'sha256sum "schema_referencia_v1 (1).json" "schema_referencia_v1 (2).json"',
  sha(os.path.join(RAIZ, "uploads/schema_referencia_v1 (1).json")) == sha(os.path.join(RAIZ, "uploads/schema_referencia_v1 (2).json")),
  True, "mesmo N1 v1.3 enviado duas vezes")

# ---------- RÓTULOS INTERNOS (fato a confessar) ----------
n2_v14 = cadeia_n2[3][2]; n1_v13 = cadeia_n1[2][2]
d14 = json.loads(txt(n2_v14)); d13 = json.loads(txt(n1_v13))
C("ROT-N2", "description do N2 v1.4 ainda diz PROPOSTA/não normativo", "documental{NFC,CS}", n2_v14,
  "startswith 'PROPOSTA v1.4'", d14.get("description","")[:13], "PROPOSTA v1.4",
  "rótulo interno nunca atualizado após o aceite do ciclo (r29)")
C("ROT-N1", "description do N1 v1.3 ainda diz PROPOSTA/não normativo", "documental{NFC,CS}", n1_v13,
  "'PROPOSTA' in description", "PROPOSTA" in d13.get("description",""), True, "idem N1 v1.3")

# ---------- V2.2 oficial cita nomes v1.1 (D-V22-SCHEMA-NOMES) ----------
V22 = SERIE + "/ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md"
C("V22-sha", "V2.2 oficial intacta", "bytes", V22, "sha256sum",
  sha(V22), "df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1", "")
raw = txt(V22)
C("V22-cita-ref", "V2.2 §5.1 cita schema_referencia_v1.1.json", "documental{NFC,CS}", V22,
  "txt.count('L05/schema_referencia_v1.1.json')", raw.count("L05/schema_referencia_v1.1.json"), 1,
  "nome defasado no texto oficial → dívida D-V22-SCHEMA-NOMES")
C("V22-cita-vin", "V2.2 §5.2 cita schema_vinculo_v1.1.json", "documental{NFC,CS}", V22,
  "txt.count('L05/schema_vinculo_v1.1.json')", raw.count("L05/schema_vinculo_v1.1.json"), 1,
  "idem §5.2")
C("V22-nao-cita", "V2.2 NÃO cita v1.3/v1.4", "documental{NFC,CS}", V22,
  "count v1.3/v1.4 de schemas", raw.count("schema_vinculo_v1.4")+raw.count("schema_referencia_v1.3"), 0, "")

# ---------- LOG: status de governança (precisão pós-regra nova) ----------
LOG = os.path.join(RAIZ, "BIBLIOTECAS/B01_Neuroinflamacao/atuais/Auditoria_B1/decisoes_B1.md")
log = txt(LOG)
C("LOG-aceite", "rev.36 registra aceite estrutural N1 v1.3 + N2 v1.4 (comentador, subscrito pela casa)",
  "documental{NFC,casefold}", LOG,
  "re.search(r'estruturalmente aprovados como base de fechamento', log, re.I)",
  bool(re.search(r"estruturalmente aprovados como base de fechamento", log, re.I)), True, "rodada 29")
# busca honesta por aprovação FORMAL do operador com sha dos schemas
padrao = [l.strip() for l in log.splitlines()
          if re.search(r"operador", l, re.I) and re.search(r"aprov|homolog", l, re.I)
          and re.search(r"schema|v1\.3|v1\.4|b06660fd|d96ad15b", l, re.I)]
pendencias = [l for l in padrao if re.search(r"falta|Pendência|pendente", l, re.I)]
C("LOG-aprov-formal", "aprovação FORMAL do operador (com sha) sobre N1 v1.3/N2 v1.4 consta no log?",
  "documental{NFC,casefold}", LOG,
  "regex tripla (operador ∧ aprov|homolog ∧ schema/versão/sha) → classificar cada linha: afirmação × pendência",
  {"linhas_casadas": len(padrao), "afirmacoes_aprovacao": len(padrao) - len(pendencias),
   "pendencias_homologacao": len(pendencias)},
  {"linhas_casadas": 2, "afirmacoes_aprovacao": 0, "pendencias_homologacao": 2},
  "as 2 linhas casadas são PENDÊNCIAS (D4 'falta só o aceno-homologação do operador'; 'homologação do operador "
  "do desfecho já aplicado da D4' como pendência) → aprovação formal do operador NÃO consta para os schemas; "
  "no padrão da regra nova (rev.42) o selo final falta. Sugestão: ato formal simples do operador.")
C("LOG-d4-pendente", "pendência de homologação D4 registrada", "documental{NFC,casefold}", LOG,
  "re.search(r'aceno-homologação do operador', log)", bool(re.search(r"aceno-homolog", log)), True, "")

# ---------- MONTA O PACOTE DE ENTREGA ----------
os.makedirs(ENTREGA, exist_ok=True)
MINUTA = SERIE + "/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4_PROPOSTA_78a0f2af.md"
copias = [
    (n2_v14, "schema_vinculo_v1.4__N2_VIGENTE.json"),
    (n1_v13, "schema_referencia_v1.3__N1_VIGENTE.json"),
    (MINUTA, "L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.4_PROPOSTA__ESPECIFICACAO.md"),
]
leiame = f"""SCHEMAS L-05 — VERSÕES VIGENTES (correntes) — entrega 2026-09-19 · rodada 37
================================================================================

RESPOSTA DIRETA: o arquivo "schema_vinculo_v1.1.json" NÃO é o atualizado.
É o PRIMEIRO elo da cadeia (recebido 2026-09-15), marcado internamente como
"PROPOSTA v1.1 — não normativo".

CADEIA N2 — Vínculo Evidência↔Afirmação↔Entidades (a versão real vive no $id interno):
  v1.1 · 2026-09-15 · 10.708 b · sha b0934412b010b7e0801f372ae57769fe0daa42c046e757128788159ec9ff4130  (histórico)
  v1.2 · 2026-09-16 · 11.122 b · sha 19f4f29a8763aa635a09d16c1bd960af2687da62a5f79700b8dfd57081d73360  (histórico)
  v1.3 · 2026-09-17 · 12.307 b · sha ec4f0de88fd0d845ad91f1d413132fa7d9a5c38d1f9f2f7abff1d3a27e7bf836  (histórico)
  v1.4 · 2026-09-18 · 12.840 b · sha d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050  <<< VIGENTE
CADEIA N1 — Registro de Referência:
  v1.1 · 2026-09-15 ·  7.796 b · sha 737bcda824b6c355d4f9b34faa3703e5ff94537b65751efbcc9d26b4b93553db  (histórico)
  v1.2 · 2026-09-16 ·  8.674 b · sha b8bcea8084fc17a296ef2beebd709bb2c90a7d816918ddfda74a0667e6ec168a  (histórico)
  v1.3 · 2026-09-17 ·  9.582 b · sha b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da  <<< VIGENTE

CONTEÚDO DESTE PACOTE (cópias byte-verbatim do acervo):
  1) schema_vinculo_v1.4__N2_VIGENTE.json          sha d96ad15b…  ($id = L05/schema_vinculo_v1.4.json)
  2) schema_referencia_v1.3__N1_VIGENTE.json       sha b06660fd…  ($id = L05/schema_referencia_v1.3.json)
  3) L05_SCHEMA_..._v1.4_PROPOSTA__ESPECIFICACAO.md sha {sha(MINUTA)[:12]}… (minuta v1.4 que descreve os dois)

CAUSAS DA CONFUSÃO (nomeadas):
  a) os uploads vieram como "schema_vinculo_v1.json / (1) / (2)" — o número do arquivo é do
     navegador; a versão real está DENTRO do JSON, no campo $id;
  b) a Arquitetura V2.2 oficial (df7f7cfd…, aprovada 2026-09-19) ainda cita os nomes v1.1
     em §5.1/§5.2 → dívida já registrada: D-V22-SCHEMA-NOMES (correção editorial futura);
  c) os próprios vigentes trazem "PROPOSTA — não normativo" na description interna — rótulo
     que nunca foi atualizado após o aceite técnico.

STATUS DE GOVERNANÇA (declarado com precisão, sob a regra nova rev.42):
  · Aceite TÉCNICO do ciclo: N1 v1.3 + N2 v1.4 "estruturalmente aprovados como base de
    fechamento do L-05" — comentador (ChatGPT) na rodada 29 (2026-09-18), subscrito pela
    casa após réplica integral (trilha 48: 52/52; 26 casos sintéticos falsificáveis 26/26).
  · Aprovação FORMAL do operador com sha+data, no padrão da regra nova de versionamento,
    NÃO consta registrada para estes dois schemas (homologação pendente registrada apenas
    para o desfecho D4). Sugestão da casa: ato formal simples — "aprovado" do operador e
    a casa grava sha/data — para selar o conjunto, como foi feito com a V2.2 na rodada 36.

VERIFICAÇÃO (no seu computador):
  sha256sum schema_vinculo_v1.4__N2_VIGENTE.json   → d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050
  sha256sum schema_referencia_v1.3__N1_VIGENTE.json → b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da
"""
with open(os.path.join(ENTREGA, "LEIAME.txt"), "w", encoding="utf-8") as f:
    f.write(leiame)
for src, dst in copias:
    shutil.copyfile(src, os.path.join(ENTREGA, dst))
C("PKG-copias", "cópias byte-verbatim na pasta de entrega", "bytes", ENTREGA,
  "sha256sum pasta == sha256sum origem",
  all(sha(os.path.join(ENTREGA, d)) == sha(s) for s, d in copias), True, "3 arquivos")

ZIP = os.path.join(ENTREGA, "SCHEMAS_L05_VIGENTES_2026-09-19.zip")
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(ENTREGA, "LEIAME.txt"), "LEIAME.txt")
    for _, d in copias:
        z.write(os.path.join(ENTREGA, d), d)
# re-extração pós-zip (medida, não suposição)
tmp = os.path.join(ENTREGA, "_verif_reextracao"); shutil.rmtree(tmp, ignore_errors=True)
with zipfile.ZipFile(ZIP) as z: z.extractall(tmp)
ok_zip = all(sha(os.path.join(tmp, d)) == sha(s) for s, d in copias) and \
         sha(os.path.join(tmp, "LEIAME.txt")) == sha(os.path.join(ENTREGA, "LEIAME.txt"))
C("PKG-zip", "zip re-extraído confere byte a byte", "bytes", ZIP,
  "unzip → sha256sum ×4 arquivos", ok_zip, True, f"zip = {os.path.getsize(ZIP)} b")
shutil.rmtree(tmp)

# ---------- 0 CIÊNCIA (fim) ----------
ciencia_fim = {os.path.basename(p): sha(p) for p in (V7, MAN, VINC) if os.path.exists(p)}
C("CIENCIA-0", "V7/manifesto/vínculos intactos início→fim", "bytes", "acervo B1",
  "sha256sum ×3 no início e no fim", ciencia_ini == ciencia_fim, True,
  json.dumps(ciencia_fim)[:160])

res = {"trilha": 55, "rodada": 37, "data": "2026-09-19", "tema": "cadeia schemas L-05 — v1.1 NÃO é o vigente; entrega dos vigentes",
       "total": len(checks), "verdes": sum(c["ok"] for c in checks),
       "checks": checks,
       "confissoes_regua": [
   "C55-1: 1ª execução — check LOG-aprov-formal esperava 0 linhas casadas; a regex tripla captou 2 linhas de "
   "PENDÊNCIA de homologação (não de aprovação). Régua ingênua: contagem ≠ classificação. Régua corrigida: "
   "toda linha casada passa a ser CLASSIFICADA (afirmação × pendência) antes do veredito. Veredito inalterado.",
   "C55-2: 1ª execução — slice [:14] incluía o espaço após 'PROPOSTA v1.4'; corrigido para [:13].",
   "C55-3: 1ª execução — caminhos do trio ciência desatualizados no script (V7 tem nome próprio; manifesto vive "
   "em Bibliografia/_manifesto_biblioteca.json). Corrigidos e medidos: 6e2c2979…/79d1309a…/490675e6…."],
"veredito_casa": "v1.1 = 1º elo (histórico). VIGENTES: N2 v1.4 d96ad15b… · N1 v1.3 b06660fd… (aceite técnico r29 subscrito; "
                        "aprovação formal do operador c/ sha+data ainda não registrada no padrão da regra nova — sugerido ato formal). "
                        "V2.2 oficial cita nomes v1.1 (D-V22-SCHEMA-NOMES confirmada no oficial df7f7cfd…)."}
saida = os.path.join(RAIZ, "BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA55_cadeia_schemas_L05_vigentes_2026-09-19.json")
with open(saida, "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=2)
print(f"{res['verdes']}/{res['total']} verdes"); [print("  FALHOU:", c["id"], c["medido"]) for c in checks if not c["ok"]]
print("zip:", ZIP, os.path.getsize(ZIP), "b · sha", sha(ZIP)[:16] + "…")
