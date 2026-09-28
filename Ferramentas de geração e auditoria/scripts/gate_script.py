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
  1. 100% das refs do Módulo 09 com G1 registrado OU NAO_LOCALIZADO
     (2026-09-13 rev.A2: o atalho `citacao_confirmada` NÃO é mais via de portão —
     flag do auditor de estrutura: é campo gravável por modelo e o processo veda
     modelo escrevendo campo de verificação; uso vira FALHA até decisão de schema L-05)
  2. 100% dos vínculos Nível-2 com trecho_ancora NAO VAZIO
     (ATENCAO: nao verifica se a ancora existe no texto — isso e o portao P-8)
  3. status_auditoria de cada vinculo dentro do enum fechado
     (NAO verifica verification_status frase a frase na Canonica)
  4a. vinculo apontando para ficha inexistente no Modulo 09 (hard-fail)
  4b. ficha que nao aparece em nenhuma linha-lote (AVISO, nao bloqueia)
     (NAO verifica citacao de prosa sem vinculo — isso e o portao P-8, V-05)
  5. campo "grade" literal A|B|C|D AUSENTE (usa forca_evidencia_afirmacao) — hard-fail
  6. claims de ALTO RISCO com 2ª verificação independente registrada (INFO)
     — 2026-09-13 rev.A2: AGORA com os 4 critérios do Bloco H implementados
     (antes: 1,5 — uso/tier_1 apenas), com contadores por critério
  7. E1 anti-autocertificacao: g1_metodo é FERRAMENTA registrada (FALHA)
  8. E2 anti-autocertificacao: verification_status="verificado" exige
     g3_verificado_por de avaliador — sem 'eutils'/'script'/'retrofit' (FALHA)
  9. E3 anti-autocertificacao: âncora truncada com status G3 (INFO — heurística
     conservadora; literalidade quem mede é o P-8/V-01)
  10. uso dentro do enum SCHEMA-CLAIM v3.1 (INFO — flag rev.A2: acervo medido
     fora do enum; correção é decisão de schema L-05/1.2, não edição de campo)
  11. selo de verificação POR FRASE (Bloco H item 3 / P12): frase declarativa sem
     verification_status válido E sem selo inline (INFO nomeado — flags do
     auditor de estrutura; antes este portão checava status_auditoria em vez do selo)

REVISAO 2026-09-13 (auditor externo de ESTRUTURA — replica da casa, trilha 23):
  Achados replicados e confirmados nos dados da B1 V7: (i) campo `uso` fora do
  enum v3.1 — medido: contexto_mecanistico 178, clinico 37, gap_pesquisa 29,
  B1_v2 30 (rótulo de versão em campo semântico), nucleo_causal 0,
  suporte_correlacional 0 → o ramo 'nucleo_causal' do item 6 era código morto
  (mesmo padrão do bug tier_1 de 2026-09-10, cuja correção não examinou o ramo
  uso — 2ª ocorrência do defeito); (ii) item 6 implementava 1,5 dos 4 critérios
  do Bloco H; (iii) selo por frase não era checado (medido: 7 pendente no
  APENDICE + 1 full-text declarado; 7 combinam CONFIRMADO+pendente — bate com os
  8/7 do revisor); (iv) E1/E2/E3 fora do código (réplica manual do revisor:
  0 violações hoje — confirmado); (v) bypass citacao_confirmada (hoje 0 usos).
  Backup pré-edição: gate_script.py.bak_gateOficial_pre_revA2_2026-09-13.
  Esta versão é PROPOSTA da casa ao Auditor-Mestre para a próxima oficial.

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
    # rev.A2 (2026-09-13): citacao_confirmada NÃO é via de portão (flag do auditor de estrutura —
    # campo gravável por modelo, e o processo veda modelo escrevendo campo de verificação).
    # Níveis: (i) DEPENDÊNCIA ativa do atalho (ref só passa por ele) = FALHA; (ii) campo preenchido
    # sem dependência = INFO nomeado (acervo legado medido; origem a auditar no pacote L-05; a
    # recomendação é ignorar/remover o campo como dado, com decisão de schema — não se apaga campo
    # sem norma, pelo mesmo princípio). Réplica 2026-09-13: 0 dependências (todas têm g1_metodo).
    cc_dep = [r for r,i in refs.items()
              if i.get("citacao_confirmada") is True
              and not i.get("g1_metodo")
              and "NAO_LOCALIZADO" not in str(i.get("status_auditoria",""))]
    if cc_dep: falhas.append(f"[1b] {len(cc_dep)} refs DEPENDEM de 'citacao_confirmada' para passar no portão "
                             f"(atalho banido desde 2026-09-13 rev.A2): {cc_dep[:5]}")
    cc_pre = [r for r,i in refs.items() if i.get("citacao_confirmada") is True]
    if cc_pre: infos.append(f"[1c] {len(cc_pre)} refs trazem o campo 'citacao_confirmada' preenchido (hoje "
                            "SEM dependência de portão — todas têm g1_metodo): campo banido como via desde "
                            "rev.A2; origem a auditar e remoção/ignorância a decidir no pacote de schema L-05.")
    sem_g1 = [r for r,i in refs.items()
              if not (i.get("g1_metodo") or "NAO_LOCALIZADO" in str(i.get("status_auditoria","")))]
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
    # rev.A2 (2026-09-13): item 6 reescrito com os 4 critérios do Bloco H (00_PROCESSO..., "GATE
    # OBRIGATÓRIO", item 3, a–d). Antes implementava 1,5 (uso/tier_1). Ver docstring para a réplica.
    def _ori(v): return str(v.get("secao_origem","")) + "|" + str(v.get("claim_id",""))
    cr_a = [v for v in vinc if "BLOCO_07" in _ori(v) or "BLOCO07" in _ori(v)
            or v.get("forca_biologica_conexao") == "HIGH"]
    if not any(v.get("forca_biologica_conexao") for v in vinc):
        infos.append("[6a0] campo 'forca_biologica_conexao' vazio em TODO o acervo — ramo 'conexão HIGH' do "
                     "critério (a) é mensurável mas não mensurado (dívida de preenchimento — pacote schema L-05)")
    cr_b = [v for v in vinc if v.get("uso") in ("clinico","nucleo_causal")]
    cr_c = [v for v in vinc if "human" in str(v.get("evid_role",""))
            and v.get("forca_causal") in ("tier_1_necessidade_e_suficiencia","tier_2_necessidade_ou_suficiencia")]
    cr_d = [v for v in vinc if v.get("status_auditoria") in ("NAO_SUSTENTA_CLAIM","CITACAO_INCORRETA")]
    alto_v = {v["id_vinculo"]: v for v in (cr_a + cr_b + cr_c + cr_d) if v.get("id_vinculo")}
    refs_alto = sorted({v.get("id_referencia_interna") for v in alto_v.values()})
    def tem_2a(rid):
        return any(x.get("id_referencia_interna")==rid and x.get("segunda_verificacao") for x in vinc)
    sem_2a = [a for a in refs_alto if not tem_2a(a)]
    infos.append(f"[6] ALTO RISCO por 4 critérios (Bloco H): (a)nó BLOCO_07/HIGH={len(cr_a)} (b)uso clínico={len(cr_b)} "
                 f"(c)humano→causal={len(cr_c)} (d)rejeição={len(cr_d)} → união {len(alto_v)} vínculos / {len(refs_alto)} refs; "
                 f"sem 2ª verificação: {len(sem_2a)} refs (fase 1-operador: mitigação declarada; exigir 2º avaliador quando houver equipe): {sem_2a[:5]}")

    # 7) E1 anti-autocertificação: g1_metodo é FERRAMENTA registrada
    FERR = ("eutils", "automatico", "ferramenta")
    e1 = [v.get("id_vinculo","?") for v in vinc
          if not any(x in str(v.get("g1_metodo","")).lower() for x in FERR)]
    if e1: falhas.append(f"[7/E1] {len(e1)} vínculos com g1_metodo que não é ferramenta registrada: {e1[:5]}")

    # 8) E2 anti-autocertificação: 'verificado' exige g3_verificado_por de avaliador
    e2 = [v.get("id_vinculo","?") for v in vinc
          if v.get("verification_status") == "verificado"
          and (not str(v.get("g3_verificado_por","")).strip()
               or any(x in str(v.get("g3_verificado_por","")).lower() for x in ("eutils","script","retrofit")))]
    if e2: falhas.append(f"[8/E2] {len(e2)} vínculos 'verificado' sem avaliador em g3_verificado_por (ou valor vedado): {e2[:5]}")

    # 9) E3 anti-autocertificação: âncora com status G3 aparentemente truncada (heurística INFO;
    #    literalidade quem mede é o P-8/V-01)
    FIMS = tuple(".!?)]}:*»”'’")
    e3 = [v.get("id_vinculo","?") for v in vinc
          if v.get("status_auditoria") == "CONFIRMADO"
          and str(v.get("trecho_ancora","")).strip()
          and not str(v.get("trecho_ancora","")).strip().endswith(FIMS)]
    if e3: infos.append(f"[9/E3] {len(e3)} âncoras de CONFIRMADO não terminam em fim de frase/tag "
                        f"(possível truncagem — INFO; P-8/V-01 mede literalidade): {e3[:5]}")

    # 10) uso dentro do enum SCHEMA-CLAIM v3.1
    ENUM_USO = {"nucleo_causal","suporte_correlacional","gap_pesquisa"}
    from collections import Counter as _C
    u_bad = _C(str(v.get("uso","<ausente>")) for v in vinc if str(v.get("uso","")) not in ENUM_USO)
    if u_bad: infos.append(f"[10] 'uso' fora do enum SCHEMA-CLAIM v3.1 (medido neste acervo): {dict(u_bad)} "
                           "— decisão de schema (L-05/1.2), NÃO remapear campo a campo sem norma.")

    # 11) selo por frase (Bloco H item 3 / 'NÍVEL DE VERIFICAÇÃO VISÍVEL' P12):
    #     frase declarativa sem verification_status válido E sem selo inline
    SELO = ("[VERIFICADO]","[PRÉ-CLÍNICO]","[EXT]","[EMERGENTE]","[NAO VERIFICADO]")
    OKS  = {"verificado","preclinico","extrapolado","emergente"}
    fora_selo = [v.get("id_vinculo","?") for v in vinc
                 if v.get("secao_origem") != "APENDICE_CORPUS"
                 and v.get("verification_status") not in OKS
                 and not any(s in str(v.get("trecho_ancora","")) for s in SELO)]
    if fora_selo:
        infos.append(f"[11] {len(fora_selo)} frase(s) declarativas sem campo verification_status válido E sem selo "
                     f"inline: {fora_selo} — contado sempre (não silencioso); hoje corresponde à dívida full-text "
                     f"nomeada na fila P-6. Vira FALHA quando a fila P-6 fechar.")
    na_ap = [v.get("id_vinculo","?") for v in vinc
             if v.get("secao_origem") == "APENDICE_CORPUS" and v.get("verification_status") not in OKS]
    if na_ap:
        infos.append(f"[11b] {len(na_ap)} vínculos de APENDICE_CORPUS (índice, não frase declarativa) com "
                     f"verification_status pendente: {na_ap} — índice de corpus; revisão no P-6.")

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
    print("(itens [6]/[9]/[10]/[11] são INFO nomeados de fase/dívida — ver P-6 e pacote L-05; [4b] é otimalidade)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
