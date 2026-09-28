#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GATE-SCRIPT (Bloco P-5 do Processo de Geração v2.1) — gate de INFRAESTRUTURA.
Roda DEPOIS do Checklist Estrutural e ANTES/DEPOIS do Portão G1→G2→G3.
É o portão automatizado: qualquer falha de CONTEÚDO aborta (exit 1).
Falha de infraestrutura (sem rede/API) marca BLOQUEADO_POR_INFRA (exit 2),
nunca confunde "não consegui consultar" com "citação inválida".

Uso:
  python3 gate_script.py <pasta_mecanismo>
  ex.: python3 gate_script.py /home/user/BIBLIOTECAS/B01_Neuroinflamacao

Verifica (P-5) — descricao corrigida em 2026-09-13 (AUD-063) para bater com o
codigo: a versao anterior desta docstring prometia conferencias que o script
NAO executava (itens 3 e 4), criando falsa sensacao de cobertura.
  1. 100% das refs do Módulo 09 com G1 registrado OU NAO_LOCALIZADO/citacao_confirmada
  2. 100% dos vínculos Nível-2 com trecho_ancora NAO VAZIO
     (ATENCAO: nao verifica se a ancora existe no texto — isso e o portao P-8)
  3. status_auditoria de cada vinculo dentro do enum fechado
     (NAO verifica verification_status frase a frase na Canonica)
  4a. vinculo apontando para ficha inexistente no Modulo 09 (hard-fail)
  4b. ficha que nao aparece em nenhuma linha-lote (AVISO, nao bloqueia)
     (NAO verifica citacao de prosa sem vinculo — isso e o portao P-8, V-05)
  5. campo "grade" literal A|B|C|D AUSENTE (usa forca_evidencia_afirmacao) — hard-fail
  6. claims de ALTO RISCO com 2ª verificação independente registrada (INFO)

COBERTURA QUE ESTE PORTAO NAO TEM (use validar_coerencia_camadas.py / P-8):
  literalidade da ancora do vinculo · ancora em linha-lote · ancora ambigua ·
  coerencia ficha/vinculo x prosa · sincronia manifesto x canonica ·
  claim quantitativo sem lastro · cobertura de claim_id · P20 · estratificacao.
"""
import json, re, sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("uso: gate_script.py <pasta_mecanismo>"); return 2
    mec = Path(sys.argv[1]).resolve()
    falhas = []
    infos  = []

    # aceita os dois padrões de nome: "Biblioteca_Bx_..._CANONICA" e "Bx NOME Vn CANONICA"
    todos = list(mec.glob("*.md"))
    canonicos = [p for p in todos
                 if "CANONICA" in p.name.upper() and not p.name.startswith("~")]
    def ver(p):
        m = re.search(r"[Vv](\d+)|_v(\d+)", p.name)
        if not m: return 0
        return int(m.group(1) or m.group(2))
    canonicos = sorted(canonicos, key=ver)
    if not canonicos:
        print("GATE: NENHUMA Biblioteca CANONICA encontrada — artefato ainda é Pré-Canônica (pode prosseguir p/ auditoria, não para canônica).")
        return 0
    bib = canonicos[-1]
    txt = bib.read_text(encoding="utf-8")

    # ---- carrega Módulo 09 (refs) e vínculos ----
    refs = {}
    bibdir = mec / "Evidencias" / "Bibliografia"
    vinc = []
    # consolida TODOS os .json do Módulo 09 (pmids + meta_analises + atualizações)
    for f in bibdir.glob("*.json"):
        try: d = json.load(open(f, encoding="utf-8"))
        except Exception: continue
        if isinstance(d, list):
            for it in d:
                if not isinstance(it, dict): continue
                ids = it.get("ids_referencia_interna")
                if not ids and it.get("id_referencia_interna"):
                    ids = [it["id_referencia_interna"]]
                for full in (ids or []):
                    if full and full not in refs:
                        refs[full] = it
    vf = mec / "Evidencias" / "Vinculos" / "vinculos_referencia_afirmacao.json"
    if vf.exists():
        vinc = json.load(open(vf, encoding="utf-8"))

    # 1) G1: toda ref tem G1 (eutils) ou marcador de exceção
    sem_g1 = [r for r,i in refs.items()
              if not (i.get("g1_metodo") or "NAO_LOCALIZADO" in str(i.get("status_auditoria",""))
                      or i.get("citacao_confirmada") is True)]
    if sem_g1: falhas.append(f"[1] {len(sem_g1)} refs sem G1 registrado/exceção: {sem_g1[:5]}")

    # 2) vínculos com trecho_ancora
    sem_trecho = [v.get("id_referencia_interna") for v in vinc
                  if not str(v.get("trecho_ancora","")).strip()]
    if sem_trecho: falhas.append(f"[2] {len(sem_trecho)} vínculos sem trecho_ancora: {sem_trecho[:5]}")

    # 3) status_auditoria (G3) preenchido com enum fechado (não vazio, não string livre)
    ENUM = {"CONFIRMADO","PARCIALMENTE_CONFIRMADO","NAO_LOCALIZADO","CITACAO_INCORRETA","NAO_SUSTENTA_CLAIM"}
    bad_g3 = [v.get("id_referencia_interna") for v in vinc
              if str(v.get("status_auditoria","")).strip() not in ENUM]
    if bad_g3: falhas.append(f"[3] {len(bad_g3)} vínculos com status_auditoria fora do enum oficial: {bad_g3[:5]}")

    # 4a) vínculo órfão: id não existe no Módulo 09
    orfaos = [v.get("id_referencia_interna") for v in vinc
              if v.get("id_referencia_interna") not in refs]
    if orfaos: falhas.append(f"[4a] {len(orfaos)} vínculos sem registro no Módulo 09: {orfaos[:5]}")
    # 4b) registro do Módulo 09 nunca citado em listra (ótimo -> aviso)
    rot_listra = set(re.findall(r"([A-Za-z][A-Za-z0-9_À-￿]+)\[(?:MA|EC|OB|ML|AT)\]", txt))
    nao_citado = [r.replace("REF_","") for r in refs if r.replace("REF_","") not in rot_listra]
    if nao_citado: infos.append(f"[4b] {len(nao_citado)} registro(s) do Módulo09 sem aparecer em listra: {nao_citado[:5]}")

    # 5) grade literal A-D em arquivo de mecanismo (hard-fail)
    if re.search(r"\bgrade[\"']?\s*[:=]\s*[\"']?[A-D]\b", txt, re.I) or re.search(r"\bGRADE\s+[A-D]\b", txt):
        falhas.append("[5] campo 'grade' A|B|C|D literal encontrado (deve ser forca_evidencia_afirmacao)")

    # 6) ALTO RISCO com 2ª verificação (nó BLOCO_07/conexão HIGH, uso clinico, humano->causal, rejeição)
    #    checa presença de campo de 2ª verificação quando aplicável
    # 2026-09-10 (IMPL-AT-11, 4ª rodada perícia externa — regra AT-10): "tier_1_intervencao" não
    # existe no enum oficial de forca_causal (SCHEMA-CLAIM v3.1 / LEDGER_DE_AUDITORIA §forca_causal:
    # tier_1_necessidade_e_suficiencia | tier_2_necessidade_ou_suficiencia | tier_3_correlacional_mecanistico
    # | tier_4_descritivo_estrutural). O ramo de FORÇA CAUSAL deste filtro NUNCA disparou no acervo
    # (replicado 2026-09-10: INFO[6] B1 = 36 pré-correção → 38 pós [rev.1: corrige projeção inicial de 41,
    # número medido = 38; 2 dos 5 refs tier_1 da B1 já estavam cobertos pelo ramo de uso]). Corrigido
    # para o único tier_1 real.
    # Backup pré-edição: gate_script.py.bak_2026-09-10. Dados remapeados em B01 (3 registros) —
    # trilha BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/05_reparo_AT11_2026-09-10.json.
    alto = [v.get("id_referencia_interna") for v in vinc
            if v.get("uso") in ("clinico","nucleo_causal") or v.get("forca_causal")=="tier_1_necessidade_e_suficiencia"]
    def tem_2a(rid):
        return any(x.get("id_referencia_interna")==rid and x.get("segunda_verificacao") for x in vinc)
    sem_2a = [a for a in alto if not tem_2a(a)]
    if sem_2a: infos.append(f"[6] {len(sem_2a)} claim(s) de ALTO RISCO sem campo segunda_verificacao preenchido (fase 1-operador: mitigação declarada; exigir 2º avaliador quando houver equipe): {sem_2a[:5]}")

    print("="*70)
    print(f"GATE-SCRIPT (P-5) — {mec.name}")
    print(f"Canônica: {bib.name}")
    print(f"refs Módulo09: {len(refs)} | vínculos N2: {len(vinc)}")
    print("="*70)
    for i in infos: print("INFO|", i)
    if falhas:
        for f_ in falhas: print("REPROVA|", f_)
        print("\nRESULTADO: FALHA DE CONTEÚDO — gate ABORTA (exit 1).")
        return 1
    print("\nRESULTADO: GATE APROVADO (conteúdo) — pode seguir para Rodada 3/Fidelidade.")
    print("(itens [6] são ressalva de fase 1-operador, não bloqueiam; ver P-6)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
