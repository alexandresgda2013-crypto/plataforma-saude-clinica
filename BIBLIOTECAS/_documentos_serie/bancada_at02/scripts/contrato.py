#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
contrato.py — módulo único de escrita segura em artefato canônico.

MOTIVO DE EXISTIR
-----------------
Perícia de 36 scripts (LOTEs 1-7, 2026-09-10) concluiu:

    "O acervo não tem falta de verificação — tem verificação que não bloqueia."

10 dos 36 scripts calculam a lista de problemas, imprimem, e gravam mesmo
assim. Isso viola regra escrita do Processo v2.1, Bloco P-5:

    "Qualquer item falhado → o script aborta o avanço (exit != 0).
     Não há 'avançar mesmo assim': a validação é o portão."

Este módulo existe para que essa regra seja uma linha de import, não uma
decisão que cada autor de script toma de novo.

FONTE NORMATIVA (nada aqui é invenção deste módulo)
---------------------------------------------------
  - PROCESSO DE GERAÇÃO v2.1, Blocos P-5, P-6, P-7
  - PROMPT FINAL PMID v4.2, linhas 1256, 1427-1450
  - MAPEAR_VOCABULARIO.md (tabela de tradução oficial)
  - validar_auditoria.py (enums do ledger)

DEFEITOS QUE ESTE MÓDULO IMPEDE (todos observados em dados reais)
------------------------------------------------------------------
  F2  vocabulário de um artefato gravado em outro ......... regressão B14
  D1  natureza_relacao recebendo valor de forca_causal .... 30 vínculos B1
  D2  trecho_ancora fabricado por fallback `probe + "."` .. 7 geradores
  D3  checador que não diz quantos itens examinou ......... vários
  D4  escrita sem backup, corrompendo a fonte ............. vários

USO
---
    from contrato import Contrato, abortar_se

    c = Contrato(artefato="vinculo")
    problemas = c.validar(registros)
    abortar_se(problemas, "add_vinculos_b1")     # exit 1 se houver bloqueante
    c.gravar(caminho, registros)                 # backup + escrita atômica
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

__version__ = "1.0.0"

# ════════════════════════════════════════════════════════════════════
#  1. VOCABULÁRIO — POR ARTEFATO
# ════════════════════════════════════════════════════════════════════
# Furo F2 do validar_auditoria.py, causa provada da regressão da B14:
# `status_auditoria` tem DOIS enums oficiais, quase disjuntos (interseção =
# apenas NAO_LOCALIZADO). Qual vale depende do ARQUIVO em que o registro mora.
# Nenhuma ferramenta validava essa fronteira. Agora valida.

ENUM_VINCULO = {
    # MAPEAR_VOCABULARIO.md — coluna "Enum oficial (a gravar)"
    "status_auditoria": {
        "CONFIRMADO", "PARCIALMENTE_CONFIRMADO", "NAO_LOCALIZADO",
        "CITACAO_INCORRETA", "NAO_SUSTENTA_CLAIM",
    },
    "status_referencia": {"CANDIDATO", "TRIADO", "VALIDADO", "REJEITADO"},
    "verification_status": {
        "verificado", "preclinico", "extrapolado", "emergente", "pendente",
        "pendente_fulltext",
    },
    # PROMPT v4.2 linha 1438 — eixos ORTOGONAIS, nunca intercambiáveis
    "natureza_relacao": {
        "causal", "contributiva", "associativa", "compensatoria",
        "marcador", "nao_estabelecida",
    },
    "forca_causal": {
        "tier_1_necessidade_e_suficiencia", "tier_2_necessidade_ou_suficiencia",
        "tier_3_correlacional_mecanistico", "tier_4_descritivo_estrutural",
    },
    "grau_maturidade": {
        "muito_estabelecido", "bem_suportado", "moderadamente_suportado",
        "emergente", "hipotese_inicial",
    },
    # PROMPT v4.2 linha 1441
    "g2_elegibilidade": {
        "eligible", "redirecionado_clinico", "redirecionado_mecanistico",
        "excluido_contaminacao", "nao_avaliado",
    },
    "evid_role": {
        "preclinical_mechanistic", "human_clinical", "human_experimental",
        "post_mortem", "review",
    },
}

ENUM_LEDGER = {
    # validar_auditoria.py — ENUM_STATUS_AUD e vizinhos
    "status_auditoria": {
        "PENDENTE", "APROVADO", "APROVADO_COM_RESSALVA", "NAO_SUSTENTA",
        "NAO_LOCALIZADO", "PMID_INCORRETO", "ASSOCIATIVO_REDIRECIONAR",
        "REALOCAR", "ELEGIBILIDADE_FALHOU", "NAO_TRIADO",
    },
    "portao_G1_existencia": {"PENDENTE", "VERIFIED_REFERENCE", "FALHOU"},
    "portao_G2_elegibilidade": {
        "PENDENTE", "ELIGIBLE_SOURCE", "FALHOU", "NAO_APLICAVEL",
    },
    "portao_G3_suporte": {
        "PENDENTE", "APROVADO", "APROVADO_COM_RESSALVA", "REJEITADO",
        "INCONCLUSIVO",
    },
    "natureza_da_relacao": ENUM_VINCULO["natureza_relacao"],
    "forca_causal": ENUM_VINCULO["forca_causal"],
    "grau_maturidade_cientifica": ENUM_VINCULO["grau_maturidade"],
    "forca_biologica_conexao": {"HIGH", "MEDIUM", "LOW"},
    "origem_entrada": {"LISTA_CANONICA", "GPM", "POLITICA_FONTES"},
    "tipo_classificador": {"MA", "EC", "OB", "ML", "AT"},
    "destino": {
        "FICA_MECANISMO", "REDIRECIONADO_MODULO_CLINICO", "REALOCADO_BLOCO",
        "REALOCADO_MECANISMO", "FONTES_REJEITADAS", "RESULTADOS_NAO_TRIADOS",
    },
    "acao_correcao": {
        "MANTER", "CORRIGIR_PMID", "CORRIGIR_METADADOS", "REBAIXAR_LINGUAGEM",
        "REMOVER_TRECHO", "ADICIONAR_SINALIZADOR", "TROCAR_REFERENCIA",
    },
}

ENUMS = {"vinculo": ENUM_VINCULO, "ledger": ENUM_LEDGER}

# Tabela de tradução oficial (MAPEAR_VOCABULARIO.md). Usada para EXPLICAR o
# erro, nunca para converter em silêncio: conversão automática esconderia a
# causa, que foi exatamente o modo de falha da B14.
TRADUCAO_LEDGER_PARA_VINCULO = {
    "APROVADO": "CONFIRMADO",
    "APROVADO_COM_RESSALVA": "PARCIALMENTE_CONFIRMADO",
    "NAO_SUSTENTA": "NAO_SUSTENTA_CLAIM",
    "PMID_INCORRETO": "CITACAO_INCORRETA",
    "NAO_LOCALIZADO": "NAO_LOCALIZADO",
}
TRADUCAO_VINCULO_PARA_LEDGER = {
    v: k for k, v in TRADUCAO_LEDGER_PARA_VINCULO.items()
}

# Vocabulário LEGADO: valores realmente usados na série antiga (B1 é a mais
# velha), já declarados como ressalva no Checklist de Fidelidade P-4. Não são
# invenção nem erro de operador — são dívida de harmonização conhecida.
# Reportados como AVISO nomeado, nunca silenciados e nunca confundidos com
# defeito novo. Sair desta lista exige decisão registrada, não edição de código.
LEGADO_CONHECIDO = {
    "vinculo": {
        "status_referencia": {
            "VALIDADO_G3_IA": "VALIDADO",
            "PENDENTE_FULLTEXT": "TRIADO",
        },
    },
    "ledger": {},
}

CAMPOS_OBRIGATORIOS = {
    "vinculo": [
        "id_vinculo", "id_referencia_interna", "secao_origem", "trecho_ancora",
        "natureza_relacao", "forca_causal", "grau_maturidade", "evid_role",
        "status_auditoria", "verification_status",
    ],
    "ledger": [
        "id_auditoria", "mecanismo", "id_referencia_interna", "pmid_oficial",
        "trecho_ancora", "citacao_literal", "portao_G1_existencia",
        "portao_G2_elegibilidade", "portao_G3_suporte", "status_auditoria",
    ],
}

ID_PAT = {
    "vinculo": re.compile(r"^VINC_B\d{1,2}(V\d)?_\d{4}$"),
    "ledger": re.compile(r"^AUD_B\d{1,2}_\d{4}$"),
}
CAMPO_ID = {"vinculo": "id_vinculo", "ledger": "id_auditoria"}

# PROMPT v4.2 — status terminal de G3 exige registro de verificação.
STATUS_DECIDIDOS = {
    "vinculo": {"CONFIRMADO", "PARCIALMENTE_CONFIRMADO", "NAO_SUSTENTA_CLAIM",
                "CITACAO_INCORRETA"},
    "ledger": {"APROVADO", "APROVADO_COM_RESSALVA", "NAO_SUSTENTA",
               "PMID_INCORRETO", "ASSOCIATIVO_REDIRECIONAR", "REALOCAR",
               "ELEGIBILIDADE_FALHOU"},
}


# ════════════════════════════════════════════════════════════════════
#  2. LITERALIDADE
# ════════════════════════════════════════════════════════════════════
# Regra aprendida por erro próprio (2026-09-10): separar normalização de
# APRESENTAÇÃO (legítima) de remoção de CONTEÚDO (ilegítima). Misturá-las
# inflou uma medição de 33% para 51%.

SELOS = (
    "VERIFICADO", "PENDENTE_VERIF", "PRÉ-CLÍNICO", "PRE-CLINICO",
    "APENAS PRÉ-CLÍNICO", "APENAS PRE-CLINICO", "EMERGENTE", "EXTRAPOLADO",
    "EXTRAPOLAÇÃO POR ANALOGIA", "EXT", "G1",
)
_RE_SELO = re.compile(r"\s*\[(?:" + "|".join(re.escape(s) for s in SELOS) + r")\]")


def norm(s: str) -> str:
    """Normaliza APRESENTAÇÃO. Não remove conteúdo.

    Tags de classificador ([OB], [ML], [EC; humano]) e listras são CONTEÚDO
    e nunca são tocadas — removê-las mascara divergência real de texto.
    """
    s = unicodedata.normalize("NFC", s or "")
    s = (s.replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "—")
          .replace("\u201c", '"').replace("\u201d", '"')
          .replace("\u2018", "'").replace("\u2019", "'"))
    s = re.sub(r"\*\*|__|(?<!\w)[*_](?!\w)", "", s)
    s = re.sub(r"\]\s+\[", "][", s)
    return re.sub(r"\s+", " ", s).strip()


def norm_selos(s: str) -> str:
    """norm() + remoção dos selos. SÓ para diagnóstico de causa.

    Um trecho que só casa aqui NÃO é conforme: é pendência de re-extração.
    Os selos são inseridos na prosa depois que os vínculos foram extraídos
    dela, quebrando a igualdade literal no meio da string.
    """
    s = _RE_SELO.sub(" ", norm(s))
    s = re.sub(r"\]\s+\[", "][", s)
    s = re.sub(r"\s+([.,;:!?])", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


def _prefixo_comum(agulha: str, palheiro: str) -> int:
    """Maior prefixo de `agulha` presente em `palheiro` (busca binária).

    Medir POR PREFIXO, não por booleano `in`: foi assim que se descobriu que
    trechos divergiam apenas na cauda (selo inserido depois, rótulo defasado).
    Um booleano não diria nada sobre a causa.
    """
    lo, hi = 0, len(agulha)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if agulha[:mid] in palheiro:
            lo = mid
        else:
            hi = mid - 1
    return lo


def verificar_literal(trecho: str, corpo: str) -> dict:
    """Classifica a literalidade de um trecho contra o corpo canônico.

    Devolve dict com `status`, `casados`, `total`, `divergencia`.
    NUNCA devolve booleano: a causa importa mais que o veredito, porque cada
    causa tem um reparo diferente.

    status:
      LITERAL  — conforme
      SELO     — só casa ignorando selos (prosa selada após a extração)
      ROTULO   — traz o título em inglês onde a Canônica tem (Autor, ano)
      PROSA    — a Canônica foi editada após a extração
      AUSENTE  — não está no corpo (candidato a fallback fabricado)
      VAZIO    — campo vazio
    """
    if not (trecho or "").strip():
        return {"status": "VAZIO", "casados": 0, "total": 0, "divergencia": ""}

    corpo_n, corpo_s = norm(corpo), norm_selos(corpo)
    t_n, t_s = norm(trecho), norm_selos(trecho)

    if t_n in corpo_n:
        return {"status": "LITERAL", "casados": len(t_n), "total": len(t_n),
                "divergencia": ""}
    if t_s in corpo_s:
        return {"status": "SELO", "casados": len(t_s), "total": len(t_s),
                "divergencia": ""}

    n = _prefixo_comum(t_s, corpo_s)
    resto = t_s[n:n + 70]
    if n < 40:
        status = "AUSENTE"
    elif (re.search(r"[a-z]{3,} [a-z]{3,}[^)]{0,40},\s*\d{4}\)", resto[:70])
          and not re.match(r"^\s*[a-zà-ú]", resto)):
        status = "ROTULO"
    else:
        status = "PROSA"
    return {"status": status, "casados": n, "total": len(t_s),
            "divergencia": resto}


# ════════════════════════════════════════════════════════════════════
#  3. VALIDAÇÃO
# ════════════════════════════════════════════════════════════════════

class Problema:
    """Um achado. BLOQUEANTE impede a gravação; AVISO não."""

    def __init__(self, nivel: str, item: str, campo: str, msg: str):
        self.nivel, self.item, self.campo, self.msg = nivel, item, campo, msg

    def __str__(self):
        marca = "❌" if self.nivel == "BLOQUEANTE" else "⚠️ "
        return f"{marca} [{self.item}] {self.campo}: {self.msg}"


class Contrato:
    """Validador + gravador para um tipo de artefato canônico."""

    def __init__(self, artefato: str, corpo_canonico: str | None = None,
                 exigir_literal: bool = True):
        if artefato not in ENUMS:
            raise ValueError(
                f"artefato deve ser um de {sorted(ENUMS)}, recebido {artefato!r}. "
                f"O tipo de artefato determina qual vocabulário é válido (F2)."
            )
        self.artefato = artefato
        self.enums = ENUMS[artefato]
        self.corpo = corpo_canonico
        self.exigir_literal = exigir_literal
        self.examinados = 0          # D3: todo checador reporta o denominador

    # ---------------------------------------------------------------- helpers
    def _enum_de_outro_campo(self, campo: str, valor) -> str | None:
        """Detecta valor pertencente ao enum de OUTRO campo.

        É o bug da função V() em add_vinculos_b1v2: um parâmetro alimentando
        dois campos gravou `tier_*` em natureza_relacao. Como cada valor era
        válido em ALGUM enum, nenhum checador de 'está preenchido?' pegou.
        """
        for outro, vals in self.enums.items():
            if outro != campo and valor in vals:
                return outro
        return None

    def _artefato_errado(self, campo: str, valor) -> str | None:
        """Detecta vocabulário do OUTRO artefato. Furo F2 / regressão B14."""
        outro = "ledger" if self.artefato == "vinculo" else "vinculo"
        if valor in ENUMS[outro].get(campo, set()):
            traducao = (TRADUCAO_LEDGER_PARA_VINCULO if self.artefato == "vinculo"
                        else TRADUCAO_VINCULO_PARA_LEDGER).get(valor)
            dica = f" Equivalente correto: {traducao!r}." if traducao else ""
            return (f"valor {valor!r} pertence ao vocabulário de '{outro}', "
                    f"não de '{self.artefato}'.{dica}")
        return None

    # ---------------------------------------------------------------- validar
    def validar(self, registros: list) -> list:
        """Valida uma lista de registros. Devolve lista de Problema."""
        p: list[Problema] = []
        self.examinados = len(registros)

        if not isinstance(registros, list):
            return [Problema("BLOQUEANTE", "-", "-", "esperado array de objetos")]

        campo_id = CAMPO_ID[self.artefato]
        vistos: dict[str, int] = {}

        for i, r in enumerate(registros):
            if not isinstance(r, dict):
                p.append(Problema("BLOQUEANTE", f"#{i}", "-", "registro não é objeto"))
                continue

            rid = str(r.get(campo_id, f"#{i}"))

            # -- identidade
            if not ID_PAT[self.artefato].match(rid):
                p.append(Problema("BLOQUEANTE", rid, campo_id,
                                  f"formato inválido para {self.artefato}"))
            if rid in vistos:
                p.append(Problema("BLOQUEANTE", rid, campo_id,
                                  f"ID duplicado (também em #{vistos[rid]})"))
            vistos[rid] = i

            # -- obrigatórios
            for campo in CAMPOS_OBRIGATORIOS[self.artefato]:
                if campo not in r:
                    p.append(Problema("BLOQUEANTE", rid, campo, "campo ausente"))
                elif isinstance(r[campo], str) and not r[campo].strip():
                    p.append(Problema("AVISO", rid, campo,
                                      "vazio (campo vazio é preferível a dado "
                                      "inventado — R04 — mas bloqueia uso downstream)"))

            # -- enums, com as duas fronteiras
            for campo, validos in self.enums.items():
                if campo not in r:
                    continue
                v = r[campo]
                if v in (None, ""):
                    continue
                if v in validos:
                    continue
                msg = self._artefato_errado(campo, v)
                if msg:
                    p.append(Problema("BLOQUEANTE", rid, campo, msg))
                    continue
                legado = LEGADO_CONHECIDO[self.artefato].get(campo, {})
                if v in legado:
                    p.append(Problema("AVISO", rid, campo,
                                      f"vocabulário LEGADO {v!r} (equivale a "
                                      f"{legado[v]!r}) — dívida de harmonização "
                                      f"já declarada na ressalva do P-4"))
                    continue
                outro = self._enum_de_outro_campo(campo, v)
                if outro:
                    p.append(Problema("BLOQUEANTE", rid, campo,
                                      f"valor {v!r} é do enum de {outro!r} — "
                                      f"campos trocados na origem"))
                    continue
                p.append(Problema("BLOQUEANTE", rid, campo,
                                  f"valor {v!r} fora do enum"))

            # -- literalidade do trecho
            if self.corpo and self.exigir_literal and r.get("trecho_ancora"):
                res = verificar_literal(r["trecho_ancora"], self.corpo)
                if res["status"] != "LITERAL":
                    nivel = "BLOQUEANTE" if res["status"] in ("AUSENTE", "VAZIO") else "AVISO"
                    p.append(Problema(
                        nivel, rid, "trecho_ancora",
                        f"{res['status']} — casa {res['casados']}/{res['total']} chars"
                        + (f"; diverge em «{res['divergencia'][:40]}…»"
                           if res["divergencia"] else "")))

            # -- decisão exige registro de verificação (anti-autocertificação)
            st = r.get("status_auditoria", "")
            if st in STATUS_DECIDIDOS[self.artefato]:
                ver = r.get("verificacao")
                quem = (r.get("g3_verificado_por") or "")
                if isinstance(ver, dict):
                    if not str(ver.get("verificador", "")).strip():
                        p.append(Problema("BLOQUEANTE", rid, "verificacao",
                                          f"status {st} sem verificador identificado"))
                    if not str(ver.get("abstract_ou_trecho", "")).strip():
                        p.append(Problema("BLOQUEANTE", rid, "verificacao",
                                          f"status {st} sem abstract/trecho registrado"))
                elif not quem.strip():
                    p.append(Problema("BLOQUEANTE", rid, "g3_verificado_por",
                                      f"status {st} sem registro de quem verificou "
                                      f"(o LLM não pode escrever campo de verificação)"))
                # G1 por ferramenta nunca é suporte científico
                if re.search(r"eutils|script|automatico", quem, re.I):
                    p.append(Problema("BLOQUEANTE", rid, "g3_verificado_por",
                                      f"{quem!r} é método de G1 (existência); "
                                      f"não pode assinar G3 (suporte)"))
        return p

    # ---------------------------------------------------------------- gravar
    def gravar(self, caminho, dados, *, dry_run: bool = False) -> dict:
        """Grava com backup e escrita atômica. Nunca sobrescreve direto."""
        caminho = Path(caminho)
        agora = datetime.now(timezone.utc).astimezone()
        carimbo = agora.strftime("%Y%m%d_%H%M%S")

        if dry_run:
            print(f"  [dry-run] gravaria {len(dados)} registro(s) em {caminho}")
            return {"gravado": False, "backup": None}

        backup = None
        if caminho.exists():
            backup = caminho.with_suffix(caminho.suffix + f".bak_{carimbo}")
            shutil.copy2(caminho, backup)

        tmp = caminho.with_suffix(caminho.suffix + ".tmp")
        tmp.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_text(json.dumps(dados, ensure_ascii=False, indent=1),
                       encoding="utf-8")
        tmp.replace(caminho)          # atômico

        return {"gravado": True, "backup": str(backup) if backup else None,
                "registros": len(dados), "quando": agora.isoformat()}


# ════════════════════════════════════════════════════════════════════
#  4. O PORTÃO
# ════════════════════════════════════════════════════════════════════

def abortar_se(problemas: list, origem: str = "", examinados: int | None = None):
    """Relata e aborta com exit 1 se houver BLOQUEANTE.

    É a linha que falta em 10 dos 36 scripts periciados. Processo v2.1, P-5:
    "Não há 'avançar mesmo assim': a validação é o portão."
    """
    bloq = [p for p in problemas if p.nivel == "BLOQUEANTE"]
    avisos = [p for p in problemas if p.nivel != "BLOQUEANTE"]

    cab = f"CONTRATO v{__version__}"
    if origem:
        cab += f" · {origem}"
    print("─" * 70)
    print(f"  {cab}")
    if examinados is not None:
        print(f"  EXAMINADOS: {examinados}")     # D3
    print("─" * 70)

    for p in (bloq + avisos)[:40]:
        print(f"  {p}")
    if len(bloq) + len(avisos) > 40:
        print(f"  … mais {len(bloq) + len(avisos) - 40} achado(s)")

    print("─" * 70)
    if bloq:
        print(f"  ABORTADO — {len(bloq)} bloqueante(s), {len(avisos)} aviso(s). "
              f"NADA FOI GRAVADO.")
        sys.exit(1)
    print(f"  OK — 0 bloqueante(s), {len(avisos)} aviso(s).")


# ════════════════════════════════════════════════════════════════════
#  5. AUTOTESTE
# ════════════════════════════════════════════════════════════════════

def _autoteste():
    """Reproduz os defeitos reais do acervo e exige que sejam pegos."""
    corpo = ("A micróglia ativada libera IL-1β (Silva et al., 2019)[OB]. "
             "Essa ativação é reversível em modelos animais.")
    casos = []

    base = {
        "id_vinculo": "VINC_B1_0001", "id_referencia_interna": "REF_SILVA_2019",
        "secao_origem": "BLOCO_02/2.1",
        "trecho_ancora": "A micróglia ativada libera IL-1β (Silva et al., 2019)[OB].",
        "natureza_relacao": "causal",
        "forca_causal": "tier_2_necessidade_ou_suficiencia",
        "grau_maturidade": "bem_suportado", "evid_role": "human_clinical",
        "status_auditoria": "CONFIRMADO", "verification_status": "verificado",
        "g3_verificado_por": "auditor_humano_1",
    }

    def roda(nome, mut, artefato="vinculo", espera_bloq=True):
        r = dict(base); r.update(mut)
        c = Contrato(artefato, corpo_canonico=corpo)
        probs = c.validar([r])
        houve = any(p.nivel == "BLOQUEANTE" for p in probs)
        ok = houve == espera_bloq
        casos.append((ok, nome, next((str(p) for p in probs
                                      if p.nivel == "BLOQUEANTE"), "—")))

    roda("registro correto passa", {}, espera_bloq=False)
    roda("D1 natureza_relacao com tier_* (bug da V(), 30 vínculos B1)",
         {"natureza_relacao": "tier_2_necessidade_ou_suficiencia"})
    roda("F2 vocabulário de ledger em vínculo (regressão B14)",
         {"status_auditoria": "APROVADO"})
    roda("D2 trecho fabricado por fallback probe+'.'",
         {"trecho_ancora": "Afirmação que nunca esteve no corpo do documento."})
    roda("G1 assinando G3 (eutils como verificador)",
         {"g3_verificado_por": "eutils_automatico"})
    roda("decisão sem registro de quem verificou",
         {"g3_verificado_por": ""})
    roda("cabeçalho markdown como âncora (VINC_B1_0019 real)",
         {"trecho_ancora": "### 2.2 — Outros inflamassomas no SNC: NLRP1, AIM2"})

    # o mesmo valor, no artefato certo, deve passar
    led = {
        "id_auditoria": "AUD_B1_0001", "mecanismo": "B1",
        "id_referencia_interna": "REF_SILVA_2019", "pmid_oficial": "12345678",
        "trecho_ancora": "A micróglia ativada libera IL-1β (Silva et al., 2019)[OB].",
        "citacao_literal": "SILVA_2019[OB]",
        "portao_G1_existencia": "VERIFIED_REFERENCE",
        "portao_G2_elegibilidade": "ELIGIBLE_SOURCE",
        "portao_G3_suporte": "APROVADO", "status_auditoria": "APROVADO",
        "verificacao": {"verificador": "IA_G3", "abstract_ou_trecho": "lido",
                        "data_verificacao": "2026-09-05"},
    }
    c = Contrato("ledger", corpo_canonico=corpo)
    probs = c.validar([led])
    bloq = [p for p in probs if p.nivel == "BLOQUEANTE"]
    casos.append((not bloq, "'APROVADO' no LEDGER é correto (não é erro)",
                  str(bloq[0]) if bloq else "—"))

    print("═" * 70)
    print(f"  AUTOTESTE contrato.py v{__version__}")
    print("═" * 70)
    for ok, nome, det in casos:
        print(f"  {'✅' if ok else '❌'} {nome}")
        if not ok:
            print(f"       obtido: {det}")
    n_ok = sum(1 for o, _, _ in casos if o)
    print("═" * 70)
    print(f"  {n_ok}/{len(casos)} casos corretos")
    return n_ok == len(casos)


if __name__ == "__main__":
    sys.exit(0 if _autoteste() else 1)
