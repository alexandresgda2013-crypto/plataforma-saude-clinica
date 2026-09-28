#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validar_auditoria.py — Verificador mecânico da Auditoria Científica de Conteúdo.

Conferências (alinhadas às ferramentas reais do projeto):
  - Módulo 09 (Prompt 4.0): os 5 arquivos JSON de /Evidencias/Bibliografia,
    schema de entrada oficial (id_referencia_interna, pmid_oficial, doi, ...)
    + campos opcionais do delta v1.1 (citacao_confirmada, origem_referencia, ids_auditoria).
  - Ledger de auditoria (/Auditoria_Bx/ledger_auditoria_Bx.json):
    integridade referencial (id_referencia_interna -> Módulo 09),
    trecho_ancora literal na Biblioteca, enums oficiais (vocabulário
    Schema-Claim v3.1 / GPM v2.0 / portões G1-G3), verificação preenchida
    quando há decisão.
  - Checagem cruzada com Biblioteca_Bx.md:
    citações (Autor, Ano)[tipo] e âncoras [REF_BLOCO_XX: ...] com registro;
    referências órfãs.

Uso:
  python3 validar_auditoria.py <pasta_mecanismo> \
      --biblioteca Biblioteca_B1.md \
      --ledger Auditoria_B1/ledger_auditoria_B1.json

Exit code: 0 = sem ERRO (pode haver AVISO); 1 = há ERRO.
"""

import json
import re
import sys
import difflib
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------- configuração

PASTA_BIBLIO = Path("Evidencias") / "Bibliografia"
ARQUIVOS_MOD09 = {
    "01_pmids.json": "OB",
    "02_meta_analises.json": "MA",
    "03_ensaios_clinicos.json": "EC",
    "04_atualizacoes_literatura.json": "AT",
    "05_manuais_e_livros.json": "ML",
}
CAMPOS_OBRIGATORIOS_MOD09 = [
    "id_referencia_interna", "pmid_oficial", "doi", "titulo_artigo",
    "autores", "revista_ano", "desenho_estudo", "secao_origem",
    "achado_central_molecular", "extrapolacao_por_analogia",
    "status_auditoria", "claim_id_origem",
]

ID_REF_PAT = re.compile(r"^(REF|RCT)_[A-Z0-9_\-]+_\d{4}[a-z]?$")
ID_AUD_PAT = re.compile(r"^AUD_B\d{1,2}_\d{4}$")
MEC_PAT = re.compile(r"^B([1-9]|1[0-6])$")
PMID_PAT = re.compile(r"^$|^\d+$")
DOI_PAT = re.compile(r"^$|^10\.\S+/\S+$")
DATA_PAT = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CLAIM_ID_PAT = re.compile(
    r"^$|^B\d{1,2}\.(MEC\.BLOCO\d{2}(_\d{2})?|SM[\w.]*)\.\d{3}[a-z]?$"
)

ENUM_TIPO = {"MA", "EC", "OB", "ML", "AT", ""}
ENUM_ORIGEM = {"LISTA_CANONICA", "GPM", "POLITICA_FONTES"}
ENUM_NATUREZA = {
    "", "causal", "contributiva", "associativa", "compensatoria",
    "marcador", "nao_estabelecida",
}
ENUM_MATURIDADE = {
    "", "muito_estabelecido", "bem_suportado", "moderadamente_suportado",
    "emergente", "hipotese_inicial",
}
ENUM_FORCA_CAUSAL = {
    "", "tier_1_necessidade_e_suficiencia", "tier_2_necessidade_ou_suficiencia",
    "tier_3_correlacional_mecanistico", "tier_4_descritivo_estrutural",
}
ENUM_FORCA_BIO = {"", "HIGH", "MEDIUM", "LOW"}
ENUM_G1 = {"", "PENDENTE", "VERIFIED_REFERENCE", "FALHOU"}
ENUM_G2 = {"", "PENDENTE", "ELIGIBLE_SOURCE", "FALHOU", "NAO_APLICAVEL"}
ENUM_G3 = {
    "", "PENDENTE", "APROVADO", "APROVADO_COM_RESSALVA", "REJEITADO",
    "INCONCLUSIVO",
}
ENUM_STATUS_AUD = {
    "", "PENDENTE", "APROVADO", "APROVADO_COM_RESSALVA", "NAO_SUSTENTA",
    "NAO_LOCALIZADO", "PMID_INCORRETO", "ASSOCIATIVO_REDIRECIONAR",
    "REALOCAR", "ELEGIBILIDADE_FALHOU", "NAO_TRIADO",
}
ENUM_DESTINO = {
    "", "FICA_MECANISMO", "REDIRECIONADO_MODULO_CLINICO", "REALOCADO_BLOCO",
    "REALOCADO_MECANISMO", "FONTES_REJEITADAS", "RESULTADOS_NAO_TRIADOS",
}
ENUM_ACAO = {
    "", "MANTER", "CORRIGIR_PMID", "CORRIGIR_METADADOS", "REBAIXAR_LINGUAGEM",
    "REMOVER_TRECHO", "ADICIONAR_SINALIZADOR", "TROCAR_REFERENCIA",
}

# (Sobrenome, Ano)[XX]  ou  (Sobrenome et al., Ano)[XX]  /  (Sobrenome & X, Ano)[XX]
CITACAO_RE = re.compile(
    r"\(([A-ZÀ-Ú][A-Za-zÀ-ÿ]+)(?:\s+(?:&|e)\s+[A-ZÀ-Ú][A-Za-zÀ-ÿ]+| et al\.)?"
    r"(?:,?\s+et al\.)?,?\s+(\d{4})[a-z]?\)\[([A-Z]{2})\]"
)
# âncoras ficam numa única linha; capturamos até o fim da linha e
# removemos o ']' de fechamento (o corpo contém ']' dos classificadores [OB] etc.)
ANCHOR_RE = re.compile(r"\[REF_BLOCO_(\d{2}):([^\n]+)")

# ---------------------------------------------------------------- utilitários

def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s)
                   if not unicodedata.combining(c))

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

class Rel:
    def __init__(self):
        self.erros, self.avisos, self.info = [], [], []
    def erro(self, o, m): self.erros.append(f"[ERRO] {o}: {m}")
    def aviso(self, o, m): self.avisos.append(f"[AVISO] {o}: {m}")
    def ok(self, m): self.info.append(f"[OK]   {m}")
    def mostrar(self):
        print("\n".join(self.info + self.avisos + self.erros))
        print("\n" + "=" * 70)
        print(f"RESUMO: {len(self.erros)} ERRO(S), {len(self.avisos)} AVISO(S).")
        return not self.erros

# ---------------------------------------------------------------- Módulo 09

def carregar_mod09(raiz, rel):
    entradas = {}   # id_referencia_interna -> (registro, arquivo, tipo_esperado)
    aliases = {}    # sobrenome -> [ids] (do campo _aliases)
    pasta = raiz / PASTA_BIBLIO
    for nome, tipo in ARQUIVOS_MOD09.items():
        cam = pasta / nome
        if not cam.exists():
            rel.erro(nome, "arquivo ausente")
            continue
        try:
            dados = json.loads(cam.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            rel.erro(nome, f"JSON inválido: {e}")
            continue
        if not isinstance(dados, list):
            rel.erro(nome, "esperado array de objetos")
            continue
        rel.ok(f"{nome}: {len(dados)} entrada(s) [{tipo}]")
        for reg in dados:
            if not isinstance(reg, dict):
                rel.erro(nome, "entrada não é objeto")
                continue
            rid = reg.get("id_referencia_interna", "")
            faltando = [c for c in CAMPOS_OBRIGATORIOS_MOD09 if c not in reg]
            if faltando:
                rel.erro(nome, f"{rid}: campos obrigatórios ausentes: {faltando}")
            if not ID_REF_PAT.match(str(rid)):
                rel.erro(nome, f"id_referencia_interna inválido: {rid!r} (REF/RCT_SOBRENOME_ANO)")
            if not PMID_PAT.match(str(reg.get("pmid_oficial", ""))):
                rel.erro(nome, f"{rid}: pmid_oficial inválido (só dígitos ou ''; nunca inventar)")
            if not DOI_PAT.match(str(reg.get("doi", "")).lower()):
                rel.aviso(nome, f"{rid}: doi em formato não padrão: {reg.get('doi')!r}")
            # delta opcional
            if "citacao_confirmada" in reg and not isinstance(reg["citacao_confirmada"], bool):
                rel.erro(nome, f"{rid}: citacao_confirmada deve ser booleano")
            if "origem_referencia" in reg and reg["origem_referencia"] not in ENUM_ORIGEM:
                rel.erro(nome, f"{rid}: origem_referencia fora do enum: {reg.get('origem_referencia')!r}")
            if "ids_auditoria" in reg and not isinstance(reg["ids_auditoria"], list):
                rel.erro(nome, f"{rid}: ids_auditoria deve ser array")
            if rid in entradas:
                rel.erro(nome, f"id_referencia_interna duplicado: {rid}")
            entradas[rid] = (reg, nome, tipo)
            for al in reg.get("_aliases", []) or []:
                aliases.setdefault(sem_acento(al).lower(), []).append(rid)
    return entradas, aliases

# ---------------------------------------------------------------- Ledger

def validar_ledger(caminho, entradas, texto_bib, rel):
    if not caminho.exists():
        rel.aviso("ledger", f"não encontrado em {caminho} — auditoria ainda não montada?")
        return []
    try:
        ledger = json.loads(caminho.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        rel.erro("ledger", f"JSON inválido: {e}")
        return []
    if not isinstance(ledger, list):
        rel.erro("ledger", "esperado array de objetos")
        return []
    rel.ok(f"ledger: {len(ledger)} trecho(s) registrado(s)")

    texto_norm = norm(texto_bib) if texto_bib else ""
    paragrafos = [norm(p) for p in (texto_bib or "").split("\n\n") if len(p.strip()) > 30]
    vistos = set()

    for e in ledger:
        aid = e.get("id_auditoria", "?")
        if not ID_AUD_PAT.match(str(aid)):
            rel.erro(aid, f"id_auditoria inválido: {aid!r} (AUD_Bx_NNNN)")
        if aid in vistos:
            rel.erro(aid, "id_auditoria duplicado")
        vistos.add(aid)

        if not MEC_PAT.match(str(e.get("mecanismo", ""))):
            rel.erro(aid, f"mecanismo inválido: {e.get('mecanismo')!r}")

        rid = e.get("id_referencia_interna", "")
        if rid not in entradas:
            rel.erro(aid, f"id_referencia_interna {rid!r} não existe no Módulo 09 (integridade referencial)")
        else:
            _, arq, tipo_arq = entradas[rid]
            if e.get("arquivo_modulo09") and Path(e.get("arquivo_modulo09")).name != arq:
                rel.erro(aid, f"arquivo_modulo09 {e.get('arquivo_modulo09')} não bate com o Módulo 09 ({arq})")
            if e.get("tipo_classificador") and e["tipo_classificador"] != tipo_arq:
                rel.erro(aid, f"tipo_classificador {e.get('tipo_classificador')} não bate com o arquivo {arq} (esperado {tipo_arq})")

        for campo, enum in (
            ("tipo_classificador", ENUM_TIPO),
            ("origem_entrada", ENUM_ORIGEM),
            ("natureza_da_relacao", ENUM_NATUREZA),
            ("grau_maturidade_cientifica", ENUM_MATURIDADE),
            ("forca_causal", ENUM_FORCA_CAUSAL),
            ("forca_biologica_conexao", ENUM_FORCA_BIO),
            ("portao_G1_existencia", ENUM_G1),
            ("portao_G2_elegibilidade", ENUM_G2),
            ("portao_G3_suporte", ENUM_G3),
            ("status_auditoria", ENUM_STATUS_AUD),
            ("destino", ENUM_DESTINO),
            ("acao_correcao", ENUM_ACAO),
        ):
            if e.get(campo) not in enum:
                rel.erro(aid, f"{campo}={e.get(campo)!r} fora do vocabulário controlado")

        if not CLAIM_ID_PAT.match(str(e.get("claim_id", ""))):
            rel.erro(aid, f"claim_id em formato inválido: {e.get('claim_id')!r} (ex.: B1.MEC.BLOCO02.001 ou B1.SM02.007)")

        ancora = norm(str(e.get("trecho_ancora", "")))
        if len(ancora) < 20:
            rel.erro(aid, "trecho_ancora ausente ou curto demais (obrigatório, frase completa)")
        elif texto_norm:
            if ancora not in texto_norm:
                melhor = max((difflib.SequenceMatcher(None, ancora, p).ratio() for p in paragrafos), default=0)
                if melhor >= 0.85:
                    rel.aviso(aid, f"trecho_ancora próximo mas não literal (sim {melhor:.2f}) — texto editado?")
                else:
                    rel.erro(aid, f"trecho_ancora NÃO está na Biblioteca: \"{ancora[:60]}...\"")

        cit = norm(str(e.get("citacao_literal", "")))
        if not cit:
            rel.erro(aid, "citacao_literal ausente")
        elif texto_norm and cit not in texto_norm:
            rel.aviso(aid, f"citacao_literal {cit!r} não localizada literalmente no texto")

        # decisão exige verificação
        status = e.get("status_auditoria", "")
        v = e.get("verificacao")
        decidido = status in {"APROVADO", "APROVADO_COM_RESSALVA", "NAO_SUSTENTA",
                              "NAO_LOCALIZADO", "PMID_INCORRETO", "ASSOCIATIVO_REDIRECIONAR",
                              "REALOCAR", "ELEGIBILIDADE_FALHOU"}
        if decidido:
            if not isinstance(v, dict):
                rel.erro(aid, f"status {status} sem objeto 'verificacao' (decisão sem registro)")
            else:
                if not str(v.get("abstract_ou_trecho", "")).strip():
                    rel.erro(aid, f"status {status} exige abstract/trecho colado na sessão (G3 sem abstract não conta)")
                if not DATA_PAT.match(str(v.get("data_verificacao", ""))):
                    rel.erro(aid, "verificacao.data_verificacao inválida (AAAA-MM-DD)")
                if not str(v.get("query_utilizada", "")).strip():
                    rel.aviso(aid, "verificacao sem query_utilizada registrada")
                if not str(v.get("verificador", "")).strip():
                    rel.erro(aid, "verificacao sem verificador identificado")
        if e.get("reconciliado") and not e.get("acao_correcao"):
            rel.aviso(aid, "reconciliado=true sem acao_correcao definida")

    return ledger

# ---------------------------------------------------------------- Checagem cruzada

def checagem_cruzada(texto_bib, entradas, ledger, aliases, rel):
    if not texto_bib:
        rel.aviso("biblioteca", "--biblioteca não informado; checagem cruzada ignorada")
        return
    texto = texto_bib
    refs_citados = set()

    # 1) citações no corpo
    for m in CITACAO_RE.finditer(texto):
        sob, ano, tipo = m.group(1), m.group(2), m.group(3)
        if tipo not in ENUM_TIPO:
            rel.erro("Biblioteca", f"classificador inválido [{tipo}] em ({sob}, {ano})")
        candidatos = [rid for rid in entradas
                      if sem_acento(sob).upper() in sem_acento(rid).upper() and ano in rid]
        if not candidatos:
            candidatos = aliases.get(sem_acento(sob).lower(), [])
            candidatos = [rid for rid in candidatos if ano in rid]
        if not candidatos:
            rel.erro("Biblioteca", f"citação sem entrada no Módulo 09: ({sob}, {ano})[{tipo}]")
        else:
            refs_citados.update(candidatos)

    # 2) âncoras [REF_BLOCO_XX: Autor_Ano[tipo] | ...]
    for m in ANCHOR_RE.finditer(texto):
        bloco, corpo = m.group(1), m.group(2).rstrip().rstrip("]").strip()
        for item in corpo.split("|"):
            item = item.strip().rstrip("]").strip()
            mm = re.search(r"([A-Za-zÀ-ÿ]+)_(\d{4})(?:[a-z])?\s?\[([A-Z]{2})\]?", item)
            if not mm:
                rel.aviso(f"REF_BLOCO_{bloco}", f"item de âncora em formato inesperado: {item!r}")
                continue
            sob, ano, tipo = mm.group(1), mm.group(2), mm.group(3)
            if tipo not in ENUM_TIPO:
                rel.erro(f"REF_BLOCO_{bloco}", f"classificador inválido [{tipo}] em {item}")
            candidatos = [rid for rid in entradas
                          if sem_acento(sob).upper() in sem_acento(rid).upper() and ano in rid]
            if not candidatos:
                ids_als = aliases.get(sem_acento(sob).lower(), [])
                candidatos = [rid for rid in ids_als if ano in rid]
            if not candidatos:
                rel.erro(f"REF_BLOCO_{bloco}", f"âncora sem entrada no Módulo 09: {item}")
            else:
                refs_citados.update(candidatos)

    # 3) referências órfãs (no Módulo 09, nunca citadas)
    ids_ledger = {e.get("id_referencia_interna") for e in ledger}
    for rid in entradas:
        if rid not in refs_citados and rid not in ids_ledger:
            rel.aviso(rid, "entrada do Módulo 09 sem citação no corpo e sem ledger (órfã)")

    # 4) PMID/DOI no texto corrido é proibido
    if re.search(r"\b10\.\d{3,4}/\S+", texto) or re.search(r"\bPMID\s*:?\s*\d{5,}", texto):
        rel.erro("Biblioteca", "PMID/DOI encontrado no texto corrido (proibido pelo Prompt 4.0)")

# ---------------------------------------------------------------- main

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    raiz = Path(args[0])
    bib = None
    ledger_path = None
    if "--biblioteca" in args:
        i = args.index("--biblioteca"); bib = Path(args[i + 1])
    if "--ledger" in args:
        j = args.index("--ledger"); ledger_path = Path(args[j + 1])

    rel = Rel()
    if not raiz.is_dir():
        print(f"Pasta não encontrada: {raiz}"); sys.exit(2)

    entradas, aliases = carregar_mod09(raiz, rel)
    rel.ok(f"Módulo 09: {len(entradas)} referência(s) única(s)")

    texto_bib = None
    if bib is not None:
        cam_bib = bib if bib.is_absolute() else raiz / bib
        if cam_bib.exists():
            texto_bib = cam_bib.read_text(encoding="utf-8")
            rel.ok(f"Biblioteca lida: {cam_bib.name} ({len(texto_bib.split())} palavras)")
        else:
            rel.aviso("--biblioteca", f"não encontrado: {cam_bib}")

    if ledger_path is None:
        ledger_path = raiz / "Auditoria_Bx"  # pode não existir ainda
    cam_ledger = ledger_path if ledger_path.is_absolute() else raiz / ledger_path
    ledger = validar_ledger(cam_ledger, entradas, texto_bib, rel)
    checagem_cruzada(texto_bib or "", entradas, ledger, aliases, rel)

    sys.exit(0 if rel.mostrar() else 1)

if __name__ == "__main__":
    main()
