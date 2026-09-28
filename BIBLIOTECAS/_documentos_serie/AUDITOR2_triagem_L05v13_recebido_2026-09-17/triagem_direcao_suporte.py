#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
L-05 — TRIAGEM CONSERVADORA DE direcao_suporte
Relatorio de execucao reexecutavel — pedido formal da bancada (ADENDO 1 §1, ADENDO 2 §5).

Produz os numeros que a minuta publica (172 automaticos / 102 fila humana) de forma
que a bancada possa replicar byte a byte, e aplica o teste de aceitacao falsificavel.

USO
    python3 triagem_direcao_suporte.py <pasta_atuais> [--json saida.json]

    <pasta_atuais> deve conter Evidencias/Vinculos/vinculos_referencia_afirmacao.json
    (mesmo layout que gate_script.py e validar_auditoria.py esperam).

POR QUE A REGRA NAO E' DERIVAVEL DE status_auditoria SOZINHO
    status_auditoria responde "a citacao sustenta a frase ancorada?".
    direcao_suporte responde "o que a evidencia faz com a afirmacao?".
    Sao perguntas diferentes. REF_RAISON_2013 esta CONFIRMADO nos dois vinculos em que
    aparece, e o g3_notas de ambos registra amostra geral negativa com resposta apenas
    no subgrupo inflamado — perfil de 'condicional', nunca de 'sustenta'.

DEPENDENCIAS
    stdlib apenas. Nenhuma escrita no acervo: o script so le.

SAIDA
    stdout legivel + JSON opcional com a lista nominal dos enviados a fila humana.
    Exit 0 se o teste de aceitacao passar; exit 1 se falhar.
"""

import json
import os
import re
import sys
import hashlib
import collections
from datetime import date

PENDENTE = "__PENDENTE__"

# Marcadores de qualificacao. Screening deliberadamente AMPLO: o objetivo e' mandar
# para leitura humana tudo que cheire a restricao, nao classificar. Falso-positivo
# aqui custa uma leitura; falso-negativo grava veredito epistemico errado no dado.
SINAIS_QUALIFICACAO = re.compile(
    r"(negativ|subgrupo|apenas no|somente no|restrit"
    r"|nao e necessari|não é necessári|nao sustenta|não sustenta"
    r"|so no |só no |amostra toda|conceito geral"
    r"|mencao pontual|menção pontual|extrapol"
    r"|nao demonstra|não demonstra|inconclusiv|contradit)",
    re.IGNORECASE,
)

# Campos varridos em busca de qualificacao. g3_notas carrega o julgamento do avaliador;
# trecho_ancora carrega a frase literal. Os dois entram porque a restricao pode estar
# declarada em qualquer um dos dois.
CAMPOS_VARRIDOS = ("g3_notas", "trecho_ancora")

# Teste de aceitacao falsificavel: qualquer triagem que grave 'sustenta' aqui esta errada,
# por mais registros que acerte.
REF_ACEITACAO = "REF_RAISON_2013"


def sha256(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(65536), b""):
            h.update(bloco)
    return h.hexdigest()


def triar(vinculo):
    """Retorna (valor, motivo). Tres regras, nesta ordem."""
    status = str(vinculo.get("status_auditoria", ""))
    texto = " ".join(str(vinculo.get(c, "")) for c in CAMPOS_VARRIDOS)

    # Regra 3 — PARCIALMENTE_CONFIRMADO nunca e' automatico.
    # E' a vizinhanca semantica de 'condicional'; mapear para 'sustenta' apaga a
    # distincao na origem, que e' exatamente o que o eixo foi criado para preservar.
    if status == "PARCIALMENTE_CONFIRMADO":
        return PENDENTE, "regra_3_parcialmente_confirmado"

    # Regra 2 — CONFIRMADO com sinal de qualificacao vai para leitura.
    if status == "CONFIRMADO" and SINAIS_QUALIFICACAO.search(texto):
        achado = SINAIS_QUALIFICACAO.search(texto).group(0).strip()
        return PENDENTE, "regra_2_confirmado_com_sinal:" + achado

    # Regra 1 — CONFIRMADO sem sinal recebe 'sustenta' transitorio datado.
    if status == "CONFIRMADO":
        return "sustenta", "regra_1_confirmado_sem_sinal"

    # Qualquer outro status (NAO_LOCALIZADO, CITACAO_INCORRETA, NAO_SUSTENTA_CLAIM)
    # nao e' triavel sem leitura.
    return PENDENTE, "regra_0_status_nao_triavel:" + (status or "vazio")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    base = argv[1]
    destino_json = None
    if "--json" in argv:
        destino_json = argv[argv.index("--json") + 1]

    caminho = os.path.join(base, "Evidencias", "Vinculos", "vinculos_referencia_afirmacao.json")
    if not os.path.exists(caminho):
        print("ERRO: nao encontrei " + caminho)
        return 2

    vinculos = json.load(open(caminho, encoding="utf-8"))
    digital = sha256(caminho)

    automaticos, fila = [], []
    motivos = collections.Counter()
    por_status = collections.Counter()

    for v in vinculos:
        valor, motivo = triar(v)
        motivos[motivo.split(":")[0]] += 1
        por_status[(str(v.get("status_auditoria", "")), valor)] += 1
        registro = {
            "id_vinculo": v.get("id_vinculo"),
            "id_referencia_interna": v.get("id_referencia_interna"),
            "status_auditoria": v.get("status_auditoria"),
            "direcao_suporte": valor,
            "motivo": motivo,
        }
        (automaticos if valor == "sustenta" else fila).append(registro)

    print("=" * 72)
    print("TRIAGEM CONSERVADORA DE direcao_suporte — L-05")
    print("arquivo: " + caminho)
    print("sha256 : " + digital)
    print("data   : " + date.today().isoformat())
    print("=" * 72)
    print("vinculos lidos ........... %d" % len(vinculos))
    print("automaticos (sustenta) ... %d" % len(automaticos))
    print("fila humana (PENDENTE) ... %d" % len(fila))
    print()
    print("por regra:")
    for motivo, n in sorted(motivos.items()):
        print("   %-38s %4d" % (motivo, n))
    print()
    print("cruzamento status_auditoria x resultado:")
    for (status, valor), n in sorted(por_status.items()):
        print("   %-28s -> %-14s %4d" % (status or "(vazio)", valor, n))

    print()
    print("-" * 72)
    print("TESTE DE ACEITACAO — %s nao pode sair 'sustenta'" % REF_ACEITACAO)
    alvos = [r for r in (automaticos + fila) if r["id_referencia_interna"] == REF_ACEITACAO]
    if not alvos:
        print("INCONCLUSIVO: %s nao existe neste acervo." % REF_ACEITACAO)
        aprovado = None
    else:
        aprovado = all(r["direcao_suporte"] != "sustenta" for r in alvos)
        for r in alvos:
            print("   %s -> %s (%s)" % (r["id_vinculo"], r["direcao_suporte"], r["motivo"]))
        print("   VEREDITO: " + ("APROVADO" if aprovado else "REPROVADO"))
    print("-" * 72)

    if destino_json:
        json.dump(
            {
                "arquivo": caminho,
                "sha256_entrada": digital,
                "data": date.today().isoformat(),
                "total": len(vinculos),
                "automaticos": len(automaticos),
                "fila_humana": len(fila),
                "por_regra": dict(motivos),
                "teste_aceitacao": {"referencia": REF_ACEITACAO, "aprovado": aprovado,
                                    "vinculos": alvos},
                "lista_fila_humana": fila,
                "lista_automaticos": automaticos,
            },
            open(destino_json, "w", encoding="utf-8"),
            ensure_ascii=False,
            indent=2,
        )
        print("JSON gravado em " + destino_json)

    return 0 if aprovado else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
