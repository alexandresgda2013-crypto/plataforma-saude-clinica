#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validar_coerencia_camadas.py — PORTÃO DE COERÊNCIA ENTRE CAMADAS (P-8)

Criado em 2026-09-13 pelo Auditor-Mestre após a re-auditoria da B1 V5, que
identificou que NENHUM portão existente cobria a classe de erro responsável
pelos achados AUD-026, AUD-027, AUD-030, AUD-032 e AUD-049..051.

O que os portões antigos cobriam:
  gate_script.py .............. existência de G1, âncora não-vazia, enum, integridade referencial
  validar_auditoria.py ........ schema do Módulo 09, enums do LEDGER, âncora do LEDGER

O que NINGUÉM cobria (e este portão passa a cobrir):
  V-01  literalidade das âncoras dos VÍNCULOS (o framework só validava o ledger)
  V-02  âncora apontando para linha-lote/apêndice em vez de prosa
  V-03  âncora ambígua (mais de uma ocorrência no texto)
  V-04  integridade referencial nos DOIS sentidos (vínculo→ficha e ficha→vínculo)
  V-05  checagem cruzada de citações com cobertura medida e reportada
  V-06  COERÊNCIA SEMÂNTICA ficha/vínculo × prosa ancorada (detector de deriva)
  V-07  sincronia manifesto × canônica (fonte única)
  V-08  claim quantitativo sem referência ancorada
  V-09  cobertura de claim_id
  V-10  citacao_literal do ledger degradada a token
  V-11  P20 — corte numérico, dose e posologia no corpo
  V-12  bloco de estratificação sem declaração de validação
  V-13  hash da canônica × hash registrado (detecção de edição fora de trilha)
  V-14  divergência entre docstring e implementação dos próprios portões
  V-15  identidade do classificador [XX] entre prosa, índice, apêndice e ficha
  V-16  concordância de versão entre H1, artefato_rotulo, nome do arquivo e manifesto

FILOSOFIA: este portão NÃO julga verdade científica — isso é o G3 e a revisão
humana. Ele garante que, uma vez que o G3 decidiu, a decisão esteja escrita de
forma IDÊNTICA em todas as camadas que o motor lê, e que nenhuma afirmação
chegue ao motor sem lastro localizável. Erro de ciência ele não pega; erro de
propagação, deriva e lastro ausente, pega todos.

Uso:
  python3 validar_coerencia_camadas.py <pasta_atuais> [--json saida.json] [--estrito]

  --estrito  promove os AVISOS de migração (V-10) a ERRO.

Exit: 0 = sem ERRO; 1 = há ERRO; 2 = erro de invocação.
"""
import json, re, sys, hashlib, unicodedata
from pathlib import Path

# ------------------------------------------------------------------ normalização

def nfc(s):
    return unicodedata.normalize("NFC", str(s))

def norm_espaco(s):
    return re.sub(r"\s+", " ", nfc(s).replace(" ", " ")).strip()

def norm_tipografica(s):
    """Remove APENAS diferenças tipográficas: markdown, travessão, espaço.
    Serve para separar 'deriva de formatação' de 'deriva de palavra'."""
    s = nfc(s)
    s = re.sub(r"[*`]", "", s)
    s = re.sub(r"^#+\s*", "", s, flags=re.M)
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = s.replace("‘", "'").replace("’", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = re.sub(r"\s+", "", s)
    return s

def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFKD", nfc(s))
                   if not unicodedata.combining(c))

# ------------------------------------------------------------------ relatório

class Rel:
    def __init__(self):
        self.itens = []
        self.executadas = set()   # regras que RODARAM, mesmo sem achar nada
    def rodou(self, *regras):
        self.executadas.update(regras)
    def add(self, nivel, regra, obj, msg):
        self.itens.append({"nivel": nivel, "regra": regra, "objeto": obj, "mensagem": msg})
    def erro(self, regra, obj, msg):  self.add("ERRO", regra, obj, msg)
    def aviso(self, regra, obj, msg): self.add("AVISO", regra, obj, msg)
    def ok(self, regra, msg):         self.add("OK", regra, "-", msg)
    @property
    def erros(self):  return [i for i in self.itens if i["nivel"] == "ERRO"]
    @property
    def avisos(self): return [i for i in self.itens if i["nivel"] == "AVISO"]
    def mostrar(self, limite=12):
        por_regra = {}
        for i in self.itens:
            por_regra.setdefault(i["regra"], []).append(i)
        for regra in sorted(por_regra):
            grupo = por_regra[regra]
            e = sum(1 for g in grupo if g["nivel"] == "ERRO")
            a = sum(1 for g in grupo if g["nivel"] == "AVISO")
            ok = [g for g in grupo if g["nivel"] == "OK"]
            cab = f"{regra}: {e} erro(s), {a} aviso(s)"
            print(cab)
            for g in ok:
                print(f"     OK    {g['mensagem']}")
            for g in [x for x in grupo if x["nivel"] != "OK"][:limite]:
                print(f"     {g['nivel']:<5} {g['objeto']}: {g['mensagem']}")
            resto = len([x for x in grupo if x['nivel'] != 'OK']) - limite
            if resto > 0:
                print(f"     …e mais {resto}")
        print("=" * 74)
        print(f"RESUMO: {len(self.erros)} ERRO(S), {len(self.avisos)} AVISO(S).")
        return not self.erros

# ------------------------------------------------------------------ carga

def achar_canonica(raiz):
    cands = [p for p in raiz.glob("*.md") if "CANONICA" in p.name.upper()]
    if not cands:
        return None
    def ver(p):
        m = re.search(r"[Vv](\d+(?:\.\d+)?)", p.name)
        return float(m.group(1)) if m else 0.0
    return sorted(cands, key=ver)[-1]

def carregar(raiz):
    bibdir = raiz / "Evidencias" / "Bibliografia"
    refs = []
    for nome in ("01_pmids.json", "02_meta_analises.json", "03_ensaios_clinicos.json",
                 "04_atualizacoes_literatura.json", "05_manuais_e_livros.json"):
        p = bibdir / nome
        if p.exists():
            d = json.loads(p.read_text(encoding="utf-8"))
            if isinstance(d, list):
                for r in d:
                    r["_arquivo"] = nome
                    refs.append(r)
    vp = raiz / "Evidencias" / "Vinculos" / "vinculos_referencia_afirmacao.json"
    vinc = json.loads(vp.read_text(encoding="utf-8")) if vp.exists() else []
    led = []
    for p in raiz.glob("Auditoria_*/ledger_auditoria_*.json"):
        if p.suffix == ".json":
            led = json.loads(p.read_text(encoding="utf-8"))
            break
    man = {}
    mp = bibdir / "_manifesto_biblioteca.json"
    if mp.exists():
        man = json.loads(mp.read_text(encoding="utf-8"))
    return refs, vinc, led, man

# ------------------------------------------------------------------ regras

# Uma citação real do acervo: "(Autor et al., 2019)[OB; revisão, humano]"
# A regex antiga exigia ]\[([A-Z]{2})\] colado e via 7% do texto.
CITACAO_RE = re.compile(
    r"\(([A-ZÀ-Ú][A-Za-zÀ-ÿ'’\-]+(?:\s+(?:&|e|and)\s+[A-ZÀ-Ú][A-Za-zÀ-ÿ'’\-]+)?)"
    r"(?:\s+et\s+al\.)?,?\s+(\d{4})([a-z]?)\)"
    r"(?:\s*\[([A-Z]{2})[^\]]*\])?"
)
LINHA_LOTE_RE = re.compile(r"^\s*\*[A-Za-z0-9_À-ÿ]+\[[A-Z]{2}\].*\*\s*$")
NUMERO_CLAIM_RE = re.compile(
    r"(?<![\w.])(\d{1,3}(?:[.,]\d+)?\s?%"
    r"|OR\s*[~≈=]?\s*\d[.,]\d+|razão de chances\s*[~≈=]?\s*\d[.,]\d+"
    r"|SMD\s*[=~]?\s*-?\d[.,]\d+"
    r"|n\s*=\s*\d+)"
)
CORTE_RE = re.compile(
    r"(PCR\s*[><≥≤]\s*\d|>\s*\d+(?:[.,]\d+)?\s*mg/L|\d+(?:[.,]\d+)?\s*mg/dL"
    r"|\d+\s*mg/kg|\d+\s*(?:mg|g|mcg|µg|UI)\s*(?:/dia|por dia|ao dia|diários)"
    r"|posologia)", re.I)
NEGACAO_RE = re.compile(
    r"\b(não|nao|apenas|somente|exclusivamente|inalterad\w+|ausência|ausencia"
    r"|sem\s+diferença|sem\s+diferenca|negativ\w+|reduzid\w+|diminuíd\w+|diminuid\w+)\b",
    re.I)

def indexar_frases(texto):
    """Separa o corpo em blocos de prosa e blocos não-prosa (linha-lote, tabela,
    heading, citação de bloco). Necessário para V-02."""
    prosa, nao_prosa = [], []
    for ln in texto.split("\n"):
        s = ln.strip()
        if not s:
            continue
        if LINHA_LOTE_RE.match(ln) or s.startswith("#") or s.startswith("|") \
           or s.startswith("---") or (s.startswith("*") and "|" in s and s.endswith("*")):
            nao_prosa.append(ln)
        else:
            prosa.append(ln)
    return "\n".join(prosa), "\n".join(nao_prosa)



# ---------------------------------------------------------------- V-15 / V-16
# Criadas em 2026-09-13 após o ciclo bilateral da B1:
#  · V-15 nasce do achado das "três taxonomias" (84 divergências prosa×apêndice,
#    7 autodivergências, tokens com dois classificadores simultâneos).
#  · V-16 nasce da errata do H1 (o título dizia V5 enquanto o rótulo dizia V6),
#    achada por leitura humana e por nenhum portão. A casa depois mostrou que a
#    4ª superfície — o manifesto — também divergia.
# LIÇÃO INCORPORADA (falso positivo da casa, trilha 24 rev.0): o REGISTRO DE
# AUDITORIA é append-only e CITA tokens antigos em prosa histórica. Um parser de
# token que varre o arquivo inteiro inventa ambiguidade. Por isso delimitamos.

SECAO_REGISTRO_RE = re.compile(r"^#{1,3}\s*REGISTRO DE AUDITORIA", re.M | re.I)

def corpo_sem_registro(texto):
    """Remove o REGISTRO DE AUDITORIA (append-only, cita tokens históricos)."""
    m = SECAO_REGISTRO_RE.search(texto)
    return texto[:m.start()] if m else texto

TOKEN_RE = re.compile(r"\b([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9]*(?:_[A-Za-zÀ-ÿ0-9]+)*)_(\d{4}[a-z]?)"
                      r"(?:_[A-Za-zÀ-ÿ0-9]+)?\[([A-Z]{2})\]")

def validar_v15(texto, refs, rel):
    """Classificador [XX] tem de ser único e idêntico em todas as camadas."""
    rel.rodou("V-15")
    corpo = corpo_sem_registro(texto)
    linhas = corpo.split("\n")

    apendice, indice, prosa_cls = {}, {}, {}
    for ln in linhas:
        alvo = apendice if ln.strip().startswith("*") and ln.strip().endswith("*") else indice
        for m in TOKEN_RE.finditer(ln):
            chave = (re.sub(r"[^A-Z]", "", sem_acento(m.group(1)).upper()), m.group(2))
            alvo.setdefault(chave, set()).add(m.group(3))
    for m in CITACAO_RE.finditer(corpo):
        if m.group(4):
            chave = (re.sub(r"[^A-Z]", "",
                     sem_acento(re.split(r"\s+(?:&|e|and)\s+", m.group(1))[0]).upper()),
                     m.group(2) + (m.group(3) or ""))
            prosa_cls.setdefault(chave, set()).add(m.group(4))

    for nome, camada in (("prosa", prosa_cls), ("índice", indice), ("apêndice", apendice)):
        for k, v in sorted(camada.items()):
            if len(v) > 1:
                rel.erro("V-15", f"{k[0].title()}_{k[1]}",
                         f"classificador ambíguo DENTRO da camada {nome}: {sorted(v)}")

    chaves = set(prosa_cls) | set(indice) | set(apendice)
    entre = 0
    for k in sorted(chaves):
        vistos = {n: c[k] for n, c in (("prosa", prosa_cls), ("índice", indice),
                                       ("apêndice", apendice)) if k in c}
        if len(vistos) > 1:
            uniao = set().union(*vistos.values())
            inter = set.intersection(*vistos.values())
            if not inter:
                entre += 1
                rel.erro("V-15", f"{k[0].title()}_{k[1]}",
                         "classificador divergente entre camadas: "
                         + " × ".join(f"{n}{sorted(v)}" for n, v in vistos.items()))
    # Token composto (PERRY_TEELING_2013, RCT_infliximab) casa pela PRIMEIRA parte:
    # a ficha do Módulo 09 é nomeada pelo primeiro autor. Sem isso o teste gera
    # falso positivo em massa — medido: 167 avisos, quase todos espúrios.
    sem_ficha = []
    ids_norm = {re.sub(r"[^A-Z0-9]", "", sem_acento(r).upper()) for r in
                {x.get("id_referencia_interna", "") for x in refs}}
    for k in sorted(set(apendice) | set(indice)):
        partes = [p for p in re.split(r"(?=[A-Z])", k[0]) if p] or [k[0]]
        cands = {k[0], partes[0], k[0][:6]}
        if not any(i.startswith("REF" + c) or i.startswith("RCT" + c)
                   for c in cands if len(c) >= 3 for i in ids_norm):
            sem_ficha.append(f"{k[0].title()}_{k[1]}")
    for t in sem_ficha:
        rel.aviso("V-15", t, "token sem ficha correspondente — possível rótulo temático "
                             "ocupando o namespace das referências")
    rel.ok("V-15", f"classificadores: {len(chaves)} chaves · {entre} divergências entre camadas · "
                   f"{len(sem_ficha)} tokens sem ficha")


def validar_v16(texto, bib, man, rel):
    """H1, artefato_rotulo, nome do arquivo e manifesto têm de declarar a mesma versão."""
    rel.rodou("V-16")
    def ver(s):
        m = re.search(r"\bV\s*(\d+(?:\.\d+)?)", str(s), re.I)
        return m.group(1) if m else None
    sup = {
        "H1": ver(texto.split("\n", 1)[0]),
        "artefato_rotulo": ver((re.search(r"\*\*artefato_rotulo:\*\*\s*CAN[ÔO]NICA\s*V\s*[\d.]+",
                                          texto, re.I) or [""])[0] if re.search(
                                r"\*\*artefato_rotulo:\*\*", texto) else ""),
        "nome_do_arquivo": ver(bib.name),
        "manifesto": ver(man.get("artefato_rotulo") or man.get("versao_canonica") or ""),
    }
    presentes = {k: v for k, v in sup.items() if v}
    if not presentes:
        rel.aviso("V-16", "versao", "nenhuma superfície declara versão de forma reconhecível")
        return
    distintos = set(presentes.values())
    if len(distintos) > 1:
        rel.erro("V-16", "versao",
                 "superfícies discordam sobre a versão vigente: "
                 + " · ".join(f"{k}=V{v}" for k, v in presentes.items()))
    else:
        faltando = [k for k in sup if not sup[k]]
        rel.ok("V-16", f"versão V{distintos.pop()} concordante em {len(presentes)}/4 superfícies"
                       + (f" (não declarada em: {faltando})" if faltando else ""))


def validar(raiz, estrito=False):
    rel = Rel()
    bib = achar_canonica(raiz)
    if bib is None:
        rel.erro("V-00", "canonica", "nenhuma Biblioteca CANONICA encontrada")
        return rel, None
    texto = bib.read_text(encoding="utf-8")
    rel.ok("V-00", f"canônica: {bib.name} ({len(texto.split())} palavras)")

    refs, vinc, led, man = carregar(raiz)
    byid = {r.get("id_referencia_interna"): r for r in refs}
    rel.ok("V-00", f"Módulo 09: {len(refs)} · vínculos: {len(vinc)} · ledger: {len(led)}")

    T_esp = norm_espaco(texto)
    T_tip = norm_tipografica(texto)
    prosa, nao_prosa = indexar_frases(texto)
    P_tip = norm_tipografica(prosa)
    NP_tip = norm_tipografica(nao_prosa)

    rel.rodou("V-00", "V-01", "V-02", "V-03", "V-04", "V-05", "V-06",
              "V-08", "V-09", "V-13", "V-14")
    # ---------------- V-01 literalidade das âncoras dos vínculos
    lit, tipografica, lexical = 0, [], []
    for v in vinc:
        a = str(v.get("trecho_ancora", "") or "")
        vid = v.get("id_vinculo", "?")
        if not a.strip():
            rel.erro("V-01", vid, "trecho_ancora vazio")
            continue
        if norm_espaco(a) in T_esp:
            lit += 1
        elif norm_tipografica(a) in T_tip:
            tipografica.append(vid)
        else:
            lexical.append(vid)
    rel.ok("V-01", f"{lit}/{len(vinc)} âncoras literais; "
                   f"{len(tipografica)} com deriva TIPOGRÁFICA; {len(lexical)} com deriva LEXICAL")
    for vid in tipografica:
        rel.aviso("V-01", vid, "âncora difere só por markdown/travessão/espaço — reparo determinístico, não exige humano")
    for vid in lexical:
        rel.erro("V-01", vid, "âncora com troca de palavra: não localizável na canônica")

    # ---------------- V-02 âncora em prosa, não em linha-lote
    for v in vinc:
        a = norm_tipografica(v.get("trecho_ancora", ""))
        vid = v.get("id_vinculo", "?")
        if not a:
            continue
        if a not in P_tip and a in NP_tip:
            rel.erro("V-02", vid,
                     "âncora aponta para linha-lote/tabela/título, não para frase de prosa — "
                     "a referência não fica ligada a nenhuma afirmação científica")

    # ---------------- V-03 âncora ambígua
    for v in vinc:
        a = norm_tipografica(v.get("trecho_ancora", ""))
        if a and T_tip.count(a) > 1:
            rel.erro("V-03", v.get("id_vinculo", "?"),
                     f"âncora ocorre {T_tip.count(a)}× no texto — sítio não determinado")

    # ---------------- V-04 integridade referencial nos dois sentidos
    ids_ref = set(byid)
    ids_vin = {v.get("id_referencia_interna") for v in vinc}
    for x in sorted(ids_vin - ids_ref):
        rel.erro("V-04", x, "vínculo aponta para ficha inexistente no Módulo 09")
    for x in sorted(ids_ref - ids_vin):
        rel.erro("V-04", x, "ficha do Módulo 09 sem nenhum vínculo (órfã)")
    dup = [k for k in ids_ref if sum(1 for r in refs if r.get("id_referencia_interna") == k) > 1]
    for k in sorted(set(dup)):
        rel.erro("V-04", k, "id_referencia_interna duplicado no Módulo 09")
    if not (ids_vin - ids_ref) and not (ids_ref - ids_vin) and not dup:
        rel.ok("V-04", "integridade referencial íntegra nos dois sentidos")

    # ---------------- V-05 checagem cruzada de citações, com cobertura medida
    citacoes = list(CITACAO_RE.finditer(texto))
    grosseiras = re.findall(r"\([A-ZÀ-Ú][^()]{2,70}?,\s*\d{4}[a-z]?\)", texto)
    # 2026-09-13: denominador era len(grosseiras) e podia ser 0 (B02 imprimiu
    # "284/0 (100.0%)"), produzindo uma cobertura falsamente perfeita.
    universo = max(len(grosseiras), len(citacoes))
    cobertura = (len(citacoes) / universo * 100) if universo else 100.0
    rel.ok("V-05", f"citações reconhecidas: {len(citacoes)}/{len(grosseiras)} "
                   f"({cobertura:.1f}% de cobertura sobre universo de {universo})")
    if cobertura < 95:
        rel.erro("V-05", "regex",
                 f"cobertura de {cobertura:.1f}% — a checagem cruzada é cega para "
                 f"{len(grosseiras)-len(citacoes)} citações; corrija o padrão antes de confiar no portão")
    faltando = []
    for m in citacoes:
        sob, ano = m.group(1), m.group(2)
        # a ficha do Módulo 09 é nomeada pelo PRIMEIRO sobrenome; citações
        # "Perry & Teeling" / "Serhan & Levy" devem casar com REF_PERRY_/REF_SERHAN_
        primeiro = re.split(r"\s+(?:&|e|and)\s+", sob)[0]
        chave = re.sub(r"[^A-Z]", "", sem_acento(primeiro).upper())
        alvo = [rid for rid in ids_ref
                if re.sub(r"[^A-Z]", "", sem_acento(rid).upper()).startswith("REF" + chave)
                or re.sub(r"[^A-Z]", "", sem_acento(rid).upper()).startswith("RCT" + chave)]
        alvo = [rid for rid in alvo if ano in rid]
        if not alvo:
            for r in refs:
                for al in (r.get("_aliases") or []):
                    if sem_acento(al).lower() == sem_acento(primeiro).lower() \
                       and ano in str(r.get("id_referencia_interna", "")):
                        alvo.append(r["id_referencia_interna"])
        if not alvo:
            faltando.append(f"({sob}, {ano})")
    for f in sorted(set(faltando)):
        rel.erro("V-05", f, "citação na prosa sem ficha correspondente no Módulo 09")

    # ---------------- V-06 coerência semântica ficha/vínculo × prosa ancorada
    # Heurística de deriva: se a prosa ancorada carrega marcador de negação,
    # seletividade ou direção e o resumo da ficha / a nota g3 não carregam,
    # o resumo pode estar descrevendo uma versão anterior da afirmação.
    for v in vinc:
        vid = v.get("id_vinculo", "?")
        rid = v.get("id_referencia_interna")
        anc = str(v.get("trecho_ancora", "") or "")
        if not anc.strip() or rid not in byid:
            continue
        marc_anc = {m.group(0).lower() for m in NEGACAO_RE.finditer(anc)}
        if not marc_anc:
            continue
        resumo = str(byid[rid].get("achado_central_molecular", "") or "")
        nota = str(v.get("g3_notas", "") or "")
        alvo = sem_acento(resumo + " " + nota).lower()
        ausentes = [t for t in marc_anc
                    if sem_acento(t).lower() not in alvo]
        if len(ausentes) == len(marc_anc) and len(marc_anc) >= 1 and resumo.strip():
            rel.aviso("V-06", vid,
                      f"prosa ancorada qualifica o achado ({sorted(marc_anc)[:3]}) mas nem "
                      f"achado_central_molecular de {rid} nem g3_notas registram a qualificação — "
                      f"possível correção não propagada")

    # ---------------- V-07 sincronia manifesto × canônica
    if man:
        rel.rodou("V-07")
        def do_texto(pat, flags=0):
            m = re.search(pat, texto, flags)
            return m.group(1).strip() if m else None
        corte_txt = do_texto(r"\*\*Corte de literatura:\*\*\s*([0-9]{4}-[0-9]{2}-[0-9]{2})")
        # 2026-09-13: schema conviva — B01 usa objeto {valor,...}; B02-B15 usam
        # string livre; B16 vem None. Tolerar os três sem mascarar a divergência.
        _c = man.get("corte_literatura")
        if isinstance(_c, dict):
            corte_man = _c.get("valor")
        elif isinstance(_c, str):
            _m = re.search(r"(\d{4}-\d{2}-\d{2})", _c)
            corte_man = _m.group(1) if _m else None
            rel.aviso("V-07", "corte_literatura",
                      "campo em texto livre (schema antigo) — só a data foi extraída; "
                      "padronizar para objeto {valor, tipo} na série")
        else:
            corte_man = None
            rel.aviso("V-07", "corte_literatura", "campo ausente ou nulo no manifesto")
        if corte_txt and corte_man and corte_txt != corte_man:
            rel.erro("V-07", "corte_literatura",
                     f"manifesto={corte_man} × canônica={corte_txt} (fonte única violada)")
        rel_txt = do_texto(r"\*\*Mecanismos relacionados \(IDs oficiais\):\*\*\s*(.+)")
        if rel_txt:
            n_txt = len([x for x in rel_txt.split(",") if x.strip()])
            n_man = len((man.get("semantic_layer") or {}).get("related_entities") or [])
            if n_txt != n_man:
                rel.erro("V-07", "related_entities",
                         f"manifesto tem {n_man} mecanismos relacionados × canônica tem {n_txt}")
        dom_txt = do_texto(r"clinical_domains \(máx 4\):\*\*\s*(.+)")
        if dom_txt:
            a = {x.strip() for x in re.split(r"[·,]", dom_txt) if x.strip()}
            b = set((man.get("semantic_layer") or {}).get("clinical_domains") or [])
            if a != b:
                rel.erro("V-07", "clinical_domains",
                         f"manifesto={sorted(b)} × canônica={sorted(a)}")
        for campo, esperado in (("pmids_total", None), ("status_canonico", None)):
            if campo not in man:
                rel.aviso("V-07", campo, "campo ausente no manifesto")
        n_mod09 = len(refs)
        if man.get("referencias_total_modulo09") not in (None, n_mod09):
            rel.erro("V-07", "referencias_total_modulo09",
                     f"manifesto={man.get('referencias_total_modulo09')} × real={n_mod09}")
        placeholders = re.findall(r"\{[A-Z]{1,3}\}", json.dumps(man, ensure_ascii=False))
        if placeholders:
            rel.erro("V-07", "manifesto",
                     f"placeholders de template não substituídos: {sorted(set(placeholders))}")

    # ---------------- V-08 claim quantitativo sem lastro
    ancoras_tip = [norm_tipografica(v.get("trecho_ancora", "")) for v in vinc]
    for ln in prosa.split("\n"):
        nums = NUMERO_CLAIM_RE.findall(ln)
        if not nums:
            continue
        ln_tip = norm_tipografica(ln)
        coberto = any(a and (a in ln_tip or ln_tip in a) for a in ancoras_tip)
        if not coberto:
            rel.aviso("V-08", nums[0][:24],
                      f"claim quantitativo sem âncora de vínculo na mesma linha: «{norm_espaco(ln)[:90]}…»")

    # ---------------- V-09 cobertura de claim_id
    sem_claim = [v.get("id_vinculo") for v in vinc if not str(v.get("claim_id", "")).strip()]
    if sem_claim:
        pct = len(sem_claim) / len(vinc) * 100
        nivel = rel.erro if pct > 25 else rel.aviso
        nivel("V-09", "claim_id",
              f"{len(sem_claim)} de {len(vinc)} vínculos ({pct:.1f}%) sem claim_id — "
              f"malha de rastreabilidade não navegável por claim")
    else:
        rel.ok("V-09", "todos os vínculos têm claim_id")

    # ---------------- V-10 citacao_literal do ledger
    if led:
        token = [e.get("id_auditoria") for e in led
                 if re.fullmatch(r"[A-Z0-9_]+\[[A-Z]{2,3}\]", str(e.get("citacao_literal", "")).strip())]
        if token:
            pct = len(token) / len(led) * 100
            msg = (f"{len(token)} de {len(led)} ({pct:.0f}%) entradas com citacao_literal "
                   f"preenchida por TOKEN e não por citação literal — o detector de deriva "
                   f"ledger×texto está inoperante")
            (rel.erro if estrito else rel.aviso)("V-10", "ledger", msg)
        else:
            rel.ok("V-10", "citacao_literal preenchida com texto real")

    rel.rodou("V-10") if led else None
    rel.rodou("V-11", "V-12")
    # ---------------- V-11 P20
    for i, ln in enumerate(prosa.split("\n"), 1):
        for m in CORTE_RE.finditer(ln):
            ctx = norm_espaco(ln)
            if re.search(r"P20|C-LAB|módulo operacional|modulo operacional|nunca posologia|"
                         r"residem|pertencem|dose-dependente", ctx, re.I):
                continue
            rel.erro("V-11", m.group(0),
                     f"corte numérico/posologia em biblioteca de mecanismo: «{ctx[:90]}…»")

    # ---------------- V-12 estratificação exige declaração de validação
    for m in re.finditer(r"^#{2,4}\s*.*(estratifica|classifica|compatibilidade|escore|pontua)"
                         r".*$", texto, re.I | re.M):
        ini = m.start()
        bloco = texto[ini:ini + 6000]
        tem_tabela = "|" in bloco and re.search(r"\|\s*-{2,}", bloco)
        if not tem_tabela:
            continue
        declara = re.search(r"não[- ]validad|nao[- ]validad|sem validação (independente|externa)|"
                            r"não constitu\w+ diagnóstico|nao constitu\w+ diagnostico|"
                            r"hipótese mecanística|hipotese mecanistica", bloco, re.I)
        metricas = re.search(r"sensibilidade|especificidade|AUC|valor preditivo|falso[- ]positivo",
                             bloco, re.I)
        if not declara:
            rel.erro("V-12", m.group(0).strip()[:50],
                     "bloco de classificação sem declaração explícita de não-diagnóstico/não-validação")
        if not metricas:
            rel.aviso("V-12", m.group(0).strip()[:50],
                      "bloco de classificação sem qualquer menção a falso-positivo/acurácia — "
                      "risco de leitura como instrumento validado")

    # ---------------- V-13 hash da canônica
    h = hashlib.sha256(bib.read_bytes()).hexdigest()
    rel.ok("V-13", f"sha256 da canônica: {h[:16]}…")
    reg = None
    if man.get("sha256_canonica_vigente") == h:
        reg = f"campo sha256_canonica_vigente (registrado em {man.get('sha256_registrado_em','?')})"
    elif man.get("sha256_canonica_vigente"):
        rel.erro("V-13", "manifesto",
                 "sha256 registrado no manifesto NÃO corresponde à canônica vigente — "
                 "houve edição fora de trilha")
    for alt in (man.get("alteracoes") or []):
        for val in alt.values():
            if isinstance(val, str) and h[:16] in val:
                reg = reg or alt.get("id")
    if reg:
        rel.ok("V-13", f"hash conferido contra a trilha {reg}")
    else:
        rel.aviso("V-13", "manifesto",
                  "hash da canônica vigente não registrado no manifesto — "
                  "edição fora de trilha não seria detectável")

    validar_v15(texto, refs, rel)
    validar_v16(texto, bib, man, rel)

    # ---------------- V-14 auto-policiamento: docstring x implementação
    # Corrigido em 2026-09-13 após a casa apontar, com razão, que V-14 estava
    # prometida na docstring e não implementada — o mesmo pecado da F-08.
    prometidas = set(re.findall(r"^\s+\*\*?(V-\d{2})\*\*?\s", __doc__ or "", re.M)) \
                 or set(re.findall(r"(V-\d{2})\s{2,}\w", __doc__ or ""))
    executadas = {i["regra"] for i in rel.itens} | rel.executadas
    orfas = sorted(prometidas - executadas)
    if orfas:
        rel.erro("V-14", "docstring",
                 f"regras anunciadas na docstring e nunca emitidas em execução: {orfas} — "
                 f"documentação promete cobertura inexistente (defeito classe F-08)")
    else:
        rel.ok("V-14", f"docstring x implementação coerentes: "
                             f"{len(prometidas)} regras anunciadas, todas executadas")

    return rel, {"canonica": bib.name, "sha256": h,
                 "refs": len(refs), "vinculos": len(vinc), "ledger": len(led)}


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); return 2
    raiz = Path(args[0]).resolve()
    if not raiz.is_dir():
        print(f"pasta não encontrada: {raiz}"); return 2
    estrito = "--estrito" in args
    rel, meta = validar(raiz, estrito=estrito)
    print("=" * 74)
    print(f"PORTÃO DE COERÊNCIA ENTRE CAMADAS (P-8) — {raiz.name}")
    if meta:
        print(f"{meta['canonica']} · refs {meta['refs']} · vínculos {meta['vinculos']} · ledger {meta['ledger']}")
    print("=" * 74)
    ok = rel.mostrar()
    if "--json" in args:
        saida = Path(args[args.index("--json") + 1])
        saida.write_text(json.dumps({"meta": meta, "itens": rel.itens}, ensure_ascii=False, indent=2),
                         encoding="utf-8")
        print(f"[relatório JSON em {saida}]")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
